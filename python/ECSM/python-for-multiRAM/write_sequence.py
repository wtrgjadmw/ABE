import os
import copy
import sys
import argparse
import traceback


def value2num(value):
    if len(value) == 4:
        num = int(value[1]) * 4 + int(value[2]) * 2 + int(value[3])
    elif len(value) == 5:
        num = int(value[1]) * 12 + int(value[2]) * 4 + int(value[3]) * 2 + int(value[4])
    else:
        raise Exception("the length of value: {0} is {1}".format(value, len(value)))
    return num


class schedulingData:
    def __init__(
            self,
            output_seq_filename: str,
            input: list,
            output: list,
            consts: list,
            scheduling_solution: list,
            formulas: list,
            mem_table: dict,
            MULnum: int,
            ADDnum: int) -> None:
        self.MULnum = MULnum
        self.ADDnum = ADDnum

        self.output_seq_filename = output_seq_filename
        self.input = input
        self.output = output
        self.consts = consts

        self.scheduling_solution = scheduling_solution
        self.formulas = formulas
        self.seq_finish_time = 0
        self.inv_start_time = -2
        self.solution_data = {}
        self.mem_table = mem_table
        self.mem_data = {}
        self.ram_num_list = {}
        self.mem_ctrl_seq = [[]]
        self.operator_init_seq = [[]]

        self.mem_addr_list = {}
        for i in range(MULnum):
            self.mem_addr_list["mm{num}".format(num=i)] = []
        for i in range(ADDnum):
            self.mem_addr_list["add{num}".format(num=i)] = []

        self.default_mem_is_second = {"input": False, "output": False}
        for i in range(MULnum):
            self.default_mem_is_second["mm{num}".format(num=i)] = False
        for i in range(ADDnum):
            self.default_mem_is_second["add{num}".format(num=i)] = False

    # c = a + bなら["c", "ADD", "a", "b"]
    def find_prev_formula(self, operand):
        for formula in self.formulas:
            if formula[0] == operand:
                return formula
        return None

    # 演算器がmm0/add0~3の内どれなのか出力
    def check_operator(self, operator, start_time):
        operator_name = operator[:-1]
        operator_num = operator[-1]
        if operator_name == "MUL":
            return "mm{num}".format(num=operator_num)
        elif operator_name == "ADD":
            return "add{num}".format(num=operator_num)
        elif operator == "INV":
            self.inv_start_time = start_time
            return "inv"
        else:
            raise Exception("invalid operator: " + operator)

    # 最初に実行
    # c = a + b, ["c", "ADD0", start_time, end_time] の時
    # self.solution_data["c"] = ["a", "b", "ADD", "add0", start_time, end_time]
    def set_solution_data(self):
        for sol in self.scheduling_solution:
            if sol[0][-3:] == "_in":
                continue
            if sol[0][-2:] == "_w":
                continue
            value_name = sol[0]
            operator_name = sol[1]
            start_time = int(sol[2])
            end_time = int(sol[3])
            self.seq_finish_time = max(self.seq_finish_time, end_time)
            if value_name in self.input:
                self.solution_data[value_name] = {"start_time": start_time, "end_time": end_time}
                # self.input_mem_list[start_time].append(value_name)
            elif "_mem" not in value_name:
                formula = self.find_prev_formula(value_name)
                operator = self.check_operator(operator_name, start_time)
                self.solution_data[value_name] = {
                    "opr1": formula[2],
                    "opr2": formula[3],
                    "ope_type": formula[1],
                    "operator": operator,
                    "start_time": start_time,
                    "end_time": end_time}

        self.operator_init_seq = [[] for i in range(self.seq_finish_time + 1)]
        self.mem_ctrl_seq = [[] for i in range(self.seq_finish_time + 1)]

    # cが10clk目で出力され、15clk目でオペランドとして最後に呼び出される時
    # self.mem_data["c"] = [11（RAMに入るのは11clk目）, 15]
    def set_mem_data(self):
        mem_is_second = copy.copy(self.default_mem_is_second)
        tmp = 0
        for sol in self.scheduling_solution:
            mem_value_name = sol[0]
            start_time = int(sol[2])
            end_time = int(sol[3])
            self.seq_finish_time = max(self.seq_finish_time, end_time)
            if tmp != start_time:
                mem_is_second = copy.copy(self.default_mem_is_second)
                tmp = start_time
            if "_w" in mem_value_name:
                operator = "output"
                self.ram_num_list[mem_value_name] = (2 if mem_is_second[operator] else 1)
                mem_is_second[operator] = True
            elif "_mem" in mem_value_name:
                value_name = self.mem_table[mem_value_name]
                if value_name in self.input:
                    operator = "input"
                    self.ram_num_list[mem_value_name] = (2 if mem_is_second[operator] else 1)
                    mem_is_second[operator] = True
                else:
                    operator = self.solution_data[value_name]["operator"]
                    if self.solution_data[value_name]["end_time"] < start_time:
                        self.ram_num_list[mem_value_name] = (2 if mem_is_second[operator] else 1)
                        mem_is_second[operator] = True
                        self.mem_data[value_name] = [self.solution_data[value_name]["end_time"], start_time]

    # RAMの書き込み信号、書き込み先アドレスの制御
    def ram_wctrl(self, operator, write_t, addr):
        if "ram_{operator}_wr_n <= 1;\n".format(operator=operator) in self.mem_ctrl_seq[write_t]:
            index = self.mem_ctrl_seq[write_t].index("ram_{operator}_wr_n <= 1;\n".format(operator=operator))
            self.mem_ctrl_seq[write_t][index] = "ram_{operator}_wr_n <= 0;\n".format(operator=operator)
        else:
            self.mem_ctrl_seq[write_t].append("ram_{operator}_wr_n <= 0;\n".format(operator=operator))
        self.mem_ctrl_seq[write_t].append("ram_{operator}_waddr <= {waddr};\n".format(operator=operator, waddr=addr))
        if "ram_{operator}_wr_n <= 0;\n".format(operator=operator) not in self.mem_ctrl_seq[write_t + 1]:
            self.mem_ctrl_seq[write_t + 1].append("ram_{operator}_wr_n <= 1;\n".format(operator=operator))

    # RAMの読み出し先アドレスの制御
    def ram_rctrl(self, operator, read_t, ram_num, addr):
        self.mem_ctrl_seq[read_t].append("ram_{operator}_raddr{ram_num} <= {raddr};\n".format(operator=operator, ram_num=ram_num, raddr=addr))

    # RAMのアドレス割り当て＋書き込み制御
    # cをアドレス2番地に割り当てる場合
    # self.mem_data["c"] = [10, 15, 2]
    def ram_assign(self):
        for value, time_list in self.mem_data.items():
            start_time = time_list[0]
            end_time = time_list[1]
            operator = self.solution_data[value]["operator"]
            is_added = False
            for i in range(len(self.mem_addr_list[operator])):
                if self.mem_addr_list[operator][i] <= start_time:
                    self.ram_wctrl(operator=operator, write_t=start_time, addr=i)
                    self.mem_data[value].append(i)
                    self.mem_addr_list[operator][i] = end_time
                    is_added = True
                    break
            if not is_added:
                self.ram_wctrl(operator=operator, write_t=start_time, addr=len(self.mem_addr_list[operator]))
                self.mem_data[value].append(len(self.mem_addr_list[operator]))
                self.mem_addr_list[operator].append(end_time)

    # 変数の保存先を調べる＋RAMに保存されてた場合は読み出しの制御命令生成

    def judge_input_ram_rctrl(self, value_name, mem_value_name, time):
        if value_name in self.consts:
            raddr = "`RAM_{0}".format(value_name)
        else:
            num = value2num(value_name)
            if value_name[0] == 'a':
                raddr = "inst_addr_opr1 + `RAM_ADDR_SIZE'd{0}".format(num)
            elif value_name[0] == 'b':
                raddr = "inst_addr_opr2 + `RAM_ADDR_SIZE'd{0}".format(num)
            else:
                print(value_name)
        ram_num = self.ram_num_list[mem_value_name]
        self.ram_rctrl(operator="input", read_t=time - 1, ram_num=ram_num, addr=raddr)
        return 1, "ram_input_out{ram_num}".format(ram_num=ram_num)

    def judge_save_place_ram_rctrl(self, value_name, mem_value_name, time):
        data = self.solution_data[value_name]
        operator = data["operator"]
        if data["end_time"] == time:
            if operator == "inv":
                return 1, "inv_out"
            return 1, "{operator}_out".format(operator=operator)
        if operator == "inv":
            return 1, "inv_out_reg"
        if data["end_time"] + 1 == time:
            return 1, "{operator}_out_reg".format(operator=operator)
        ram_num = self.ram_num_list[mem_value_name]
        self.ram_rctrl(operator=operator, read_t=time - 1, ram_num=ram_num, addr=self.mem_data[value_name][2])
        return 1, "ram_{operator}_out{ram_num}".format(operator=operator, ram_num=ram_num)

    # 演算器の入力の制御＋RAMの読み出しの制御命令生成
    def operator_init(self):
        for value_name, data in self.solution_data.items():
            if value_name in self.input:
                continue
            mem_value_name = "{value_name}_mem{num}".format(value_name=value_name, num=0)
            if data["opr1"] in self.input:
                num, opr1_save_place = self.judge_input_ram_rctrl(value_name=data["opr1"], mem_value_name=mem_value_name, time=data["start_time"])
            else:
                num, opr1_save_place = self.judge_save_place_ram_rctrl(
                    value_name=data["opr1"], mem_value_name=mem_value_name, time=data["start_time"])
            if data["opr1"] == data["opr2"]:
                opr2_save_place = opr1_save_place
            else:
                mem_value_name = "{value_name}_mem{num}".format(value_name=value_name, num=num)
                if data["opr2"] in self.input:
                    num, opr2_save_place = self.judge_input_ram_rctrl(value_name=data["opr2"], mem_value_name=mem_value_name, time=data["start_time"])
                else:
                    num, opr2_save_place = self.judge_save_place_ram_rctrl(
                        value_name=data["opr2"], mem_value_name=mem_value_name, time=data["start_time"])
            if data["operator"] == "inv":
                init_seq = "{operator}_opr <= {save1};".format(operator=data["operator"], save1=opr1_save_place)
            else:
                init_seq = "{operator}_opr1 <= {save1}; {operator}_opr2 <= {save2}; ".format(
                    operator=data["operator"], save1=opr1_save_place, save2=opr2_save_place)
            if "add" in data["operator"]:
                init_seq += "issub{operator_num} <= {issub};".format(operator_num=data["operator"]
                                                                     [-1], issub=('1' if data["ope_type"] == "SUB" else '0'))
            self.operator_init_seq[data["start_time"]].append(init_seq + "\n")
            # if value_name in self.output:
            #     self.operator_init_seq[data["end_time"]].append("{output_name}_reg <= {operator}_out;\n".format(output_name=value_name, operator=data["operator"]))

    # def ram_input(self):
    #     self.mem_ctrl_seq[0].append("ram_input_w1_n <= 0;\n")
    #     self.mem_ctrl_seq[0].append("ram_input_w2_n <= 0;\n")
    #     for i in range(24):
    #         for j in range(len(self.input_mem_list[i])):
    #             addr1 = "`RAM_{value}".format(value=self.input_mem_list[i][j])
    #             self.mem_ctrl_seq[i].append("ram_input_waddr{num} <= {waddr};\n".format(waddr=addr1, num=j+1))
    #             self.mem_ctrl_seq[i].append("ram_input_in{num} <= {value};\n".format(value=self.input_mem_list[i][j], num=j+1))
    #             # self.mem_ctrl_seq[i].append("raddr_suffix_reg <= {value};\n".format(value=self.input_mem_list[i][j]))
    #     self.mem_ctrl_seq[24].append("ram_input_w1_n <= 1;\n")
    #     self.mem_ctrl_seq[24].append("ram_input_w2_n <= 1;\n")

    def ram_result_input(self):
        for out in self.output:
            operator = self.solution_data[out]["operator"].upper()
            write_t = self.solution_data[out]["end_time"] - 1
            ram_num = self.ram_num_list[out + "_w"]
            if "w{ram_num}_n_reg <= 1;\n".format(ram_num=ram_num) in self.mem_ctrl_seq[write_t]:
                index = self.mem_ctrl_seq[write_t].index("w{ram_num}_n_reg <= 1;\n".format(ram_num=ram_num))
                self.mem_ctrl_seq[write_t][index] = "w{ram_num}_n_reg <= 0;\n".format(ram_num=ram_num)
            else:
                self.mem_ctrl_seq[write_t].append("w{ram_num}_n_reg <= 0;\n".format(ram_num=ram_num))
            is_const = False
            out = out.replace("NEW_", "").replace("_", "")
            for const in self.consts:
                if const in out:
                    waddr = "`RAM_{0}".format(const)
                    is_const = True
            if not is_const:
                num = value2num(out)
                waddr = "ret_addr + `RAM_ADDR_SIZE'd{0}".format(num)
            self.mem_ctrl_seq[write_t].append("waddr{ram_num}_reg <= {waddr};\n".format(ram_num=ram_num, waddr=waddr))
            self.mem_ctrl_seq[write_t].append("wdata_s{ram_num} <= `{operator};\n".format(ram_num=ram_num, operator=operator))
            if "w{ram_num}_n_reg <= 0;\n".format(ram_num=ram_num) not in self.mem_ctrl_seq[write_t + 1]:
                self.mem_ctrl_seq[write_t + 1].append("w{ram_num}_n_reg <= 1;\n".format(ram_num=ram_num))

    def make_sequence(self):
        self.set_solution_data()
        self.set_mem_data()
        self.ram_assign()
        self.operator_init()
        self.ram_result_input()

        f = open(self.output_seq_filename, "w")
        f.write("case (state)\n")
        for i in range(0, self.seq_finish_time + 1):
            f.write("{state}: begin\n".format(state=i))
            state_str = ""
            if i == self.inv_start_time:
                state_str += "\tstart <= 1;\n"
            elif i == self.inv_start_time + 1:
                state_str += "\tif (inv_comp == 1) begin\n"
            for operator_init in self.operator_init_seq[i]:
                state_str += "\t{operator_init_rtl}".format(operator_init_rtl=operator_init)
            for mem_ctrl in self.mem_ctrl_seq[i]:
                state_str += "\t{mem_ctrl_rtl}".format(mem_ctrl_rtl=mem_ctrl)
            if i == self.inv_start_time + 1:
                state_str += "\tstate <= state + 1;\n\tend\n"
            f.write(state_str)
            if (i == self.seq_finish_time):
                f.write("\tstate <= 0;\n")
            elif i != self.inv_start_time + 1:
                f.write("\tstate <= state + 1;\n")
            f.write("end\n")
        f.write("endcase\n")
        f.close()


def file_replace(old_filename, new_filename, old_str, new_str):
    with open(old_filename, "r") as file:
        content = file.read()
    updated_content = content.replace(old_str, new_str)
    with open(new_filename, "w") as file:
        file.write(updated_content)


if __name__ == "__main__":
    input = []
    output = []
    solution = [[]]
    formulas = [[]]
    mem_table = {}

    state_sizes = {}

    psr = argparse.ArgumentParser(
        usage='schedule.py -c <curve_group> -p <p[bit]>',
        description='Generate RTLs of sequencer based on scheduling results'
    )
    psr.add_argument("-c", "--curve", required=True, help="curve group")
    psr.add_argument("-p", "--characteristic", required=True, help="bit width of characteristic number p")
    args = psr.parse_args()
    curve_group = args.curve
    curve_name = args.characteristic

    if curve_group == "bls12":
        consts = ['BT0', 'BT1', 'PY', 'PY_', 'PX', 'PX_', 'QX0', 'QX1', 'QY0', 'QY1', 'QY_0', 'QY_1', 'TX0', 'TX1', 'TY0','TY1', 'TZ0', 'TZ1', 'XI10', 'XI11', 'XI20', 'XI21', 'XI30', 'XI31', 'XI40', 'XI41', 'XI50', 'XI51', 'ZERO', 'ONE']
    elif curve_group == "bls24":
        consts = ['BT00', 'BT01', 'BT10', 'BT11', 'PX', 'PX_', 'PY', 'PY_', 'QX00', 'QX01', 'QX10', 'QX11', 'QY00', 'QY01', 'QY10', 'QY11', 'QY_00', 'QY_01', 'QY_10', 'QY_11', 'TX00', 'TX01', 'TX10', 'TX11', 'TY00', 'TY01', 'TY10', 'TY11', 'TZ00', 'TZ01', 'TZ10', 'TZ11', 'XI100', 'XI101', 'XI110', 'XI111', 'XI200', 'XI201', 'XI210', 'XI211', 'XI300', 'XI301', 'XI310', 'XI311', 'XI400', 'XI401', 'XI410', 'XI411', 'XI500', 'XI501', 'XI510', 'XI511', 'K0', 'K1', 'ZERO', 'ONE']

    home_dir = os.path.dirname(os.getcwd())
    target_dir = "{}/{}-{}".format(home_dir, curve_group, curve_name)
    os.makedirs("{}/RTL/include/ALU_mode".format(target_dir), exist_ok=True)

    for root, dirs, files in os.walk("{}/scheduling/result".format(target_dir)):
        for file in files:
            if file[-4:] != ".txt":
                continue
            result_file_path = os.path.join(root, file)
            sequence_file_path = "{}/RTL/include/ALU_mode/seq_{}.v".format(target_dir, file[:-4])
            mem_table = {}
            print(result_file_path)
            # read scheduling result file
            exec(open(result_file_path, 'r', encoding="utf-8").read())
            sche_data = schedulingData(
                output_seq_filename=sequence_file_path,
                input=input,
                output=output,
                consts=consts,
                scheduling_solution=solution,
                formulas=formulas,
                mem_table=mem_table,
                MULnum=1,
                ADDnum=4)
            try:
                sche_data.make_sequence()
            except Exception:
                etype, value, tb = sys.exc_info()
                estr_list = traceback.format_exception(etype, value, tb)
                for estr in estr_list:
                    print(estr, end="")
            state_sizes[file[:-4].replace("_mul1_add4", "")] = sche_data.seq_finish_time + 1

    calc_state_size = max(state_sizes.values()).bit_length()
    calc_param_file = "{}/RTL/include/CalcCore_param.vh".format(target_dir)
    f = open(calc_param_file, 'a')
    f.write("`define CALC_STATE_SIZE " + str(calc_state_size) + "\n")
    for key, value in state_sizes.items():
        f.write("`define CALC_" + key.upper() + "_STATE_SIZE `CALC_STATE_SIZE'd" + str(value) + "\n")
    f.close()
