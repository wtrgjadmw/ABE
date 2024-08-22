import os
import copy
import sys
import argparse
import traceback

from inst_lib import solutionData, ALURAMIndex, ALUInstruction, new_inst, set_init_inst, set_Fpinv_preprocess_inst, set_Fpinv_inst, set_yrecover2_inst, write_header, write_raminit_aluram, write_raminit_cmdaddr


def value2num(value):
    if len(value) == 4:
        num = int(value[1]) * 4 + int(value[2]) * 2 + int(value[3])
    elif len(value) == 5:
        num = int(value[1]) * 12 + int(value[2]) * 4 + int(value[3]) * 2 + int(value[4])
    else:
        raise Exception("the length of value: {0} is {1}".format(value, len(value)))
    return num


# cが10clk目で出力 -> アドレス2に保存 -> 15clk目でオペランドとして最後に呼び出される場合，
# memoryData = {start: RAMに入るのは11clk目, end: 15, addr: x}
class memoryData:
    def __init__(self, start, end, operator, is_output=False) -> None:
        self.start = start
        self.end = end
        self.operator = operator
        self.addr = -1
        self.is_output = is_output

    def set_addr(self, addr):
        self.addr = addr


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
            MASnum: int) -> None:
        self.MULnum = MULnum
        self.MASnum = MASnum

        self.output_seq_filename = output_seq_filename
        self.input = input
        self.output = output
        # saved in MAIN_MEM
        self.const_addr_list = {"X1": 0, "X2": 1, "Z1": 2, "Z2": 3, "PX": 4, "PY": 5, "ZERO": 6, "ONE": 7, "A": 8, "B": 9, "4B": 10}
        self.index_to_add = 11

        self.scheduling_solution = scheduling_solution[1:]
        self.formulas = formulas
        self.seq_finish_time = 0
        self.inv_start_time = -2
        self.solution_data_list = {}
        self.mem_table = mem_table
        self.mem_data_list: dict[memoryData] = {}
        self.ram_num_list = {}
        self.mem_ctrl_seq = [[]]
        self.operator_init_seq = [[]]

        self.inst_list: list[ALUInstruction] = []
        self.mem_addr_list = {}
        for i in range(MULnum):
            self.mem_addr_list["MM{num}".format(num=i)] = []
        for i in range(MASnum):
            self.mem_addr_list["MAS{num}".format(num=i)] = []

        # self.default_mem_is_second = {"input": False, "output": False}
        # for i in range(MULnum):
        #     self.default_mem_is_second["MM{num}".format(num=i)] = False
        # for i in range(MASnum):
        #     self.default_mem_is_second["MAS{num}".format(num=i)] = False

    # c = a + bなら["c", "ADD", "a", "b"]
    def find_formula(self, valuable):
        for formula in self.formulas:
            if formula[0] == valuable:
                return formula
        raise Exception("invalid valuable: {}".format(valuable))

    # # 演算器がmm0/add0~3の内どれなのか出力
    # def check_operator(self, operator, start_time):
    #     operator_name = operator[:-1]
    #     operator_num = operator[-1]
    #     if operator_name == "MUL":
    #         return "mm{num}".format(num=operator_num)
    #     elif operator_name == "ADD":
    #         return "add{num}".format(num=operator_num)
    #     elif operator == "INV":
    #         self.inv_start_time = start_time
    #         return "inv"
    #     else:
    #         raise Exception("invalid operator: " + operator)

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
            start_time = int(sol[2]) - 1
            end_time = int(sol[3]) - 1
            self.seq_finish_time = max(self.seq_finish_time, end_time)
            if "_mem" not in value_name:
                formula = self.find_formula(value_name)
                self.solution_data_list[value_name] = solutionData(
                    opr1=formula[2], opr2=formula[3], operator=operator_name, operation=formula[1], start=start_time, end=end_time)
        self.operator_init_seq = [[] for i in range(self.seq_finish_time + 1)]
        self.mem_ctrl_seq = [[] for i in range(self.seq_finish_time + 1)]
        self.inst_list = [ALUInstruction() for i in range(self.seq_finish_time + 1)]

    def set_mem_data(self):
        # mem_is_second = copy.copy(self.default_mem_is_second)
        # tmp = 0
        for sol in self.scheduling_solution:
            mem_value_name = sol[0]
            start_time = int(sol[2]) - 1
            end_time = int(sol[3]) - 1
            if "_mem" in mem_value_name:
                value_name = self.mem_table[mem_value_name]
                if value_name in self.input:
                    continue
                operator = self.solution_data_list[value_name].operator
                if self.solution_data_list[value_name].end < start_time:
                    self.mem_data_list[value_name] = memoryData(start=self.solution_data_list[value_name].end, end=start_time, operator=operator)
        if "_w" in mem_value_name:
                for output_value in self.output:
                    if output_value == mem_value_name[:-2]:
                        self.mem_data_list[output_value] = memoryData(start=start_time, end=end_time, operator="MAIN", is_output=True)
                        self.mem_data_list[output_value].set_addr(self.const_addr_list[output_value[:-4]])

    # RAMのアドレス割り当て＋書き込み制御
    # cをアドレス2番地に割り当てる場合
    # self.mem_data["c"] = [10, 15, 2]
    def ram_assign(self):
        for value, memory_data in self.mem_data_list.items():
            start_time = memory_data.start
            end_time = memory_data.end
            operator = memory_data.operator
            is_added = False
            if memory_data.is_output:
                self.inst_list[start_time].set_mem_write(operator=operator, waddr=memory_data.addr, mask=self.is_ladder)
                continue
            for i in range(len(self.mem_addr_list[operator])):
                if self.mem_addr_list[operator][i] <= start_time:
                    waddr = i + self.index_to_add
                    self.inst_list[start_time].set_mem_write(operator=operator, waddr=waddr, mask=self.is_ladder)
                    memory_data.set_addr(waddr)
                    self.mem_addr_list[operator][i] = end_time
                    is_added = True
                    break
            if not is_added:
                waddr = len(self.mem_addr_list[operator]) + self.index_to_add
                self.inst_list[start_time].set_mem_write(operator=operator, waddr=waddr, mask=self.is_ladder)
                memory_data.set_addr(waddr)
                self.mem_addr_list[operator].append(end_time)

    def set_operator_inst(self, data: solutionData):
        for i in range(2):
            operand_name = data.opr1 if i == 0 else data.opr2
            time = data.start
            if operand_name in self.input:
                # print(time, value_name, operand_name, self.const_addr_list[operand_name])
                self.inst_list[time].set_operator_inst(
                    operation=data.operation,
                    operand_index=i,
                    raddr=self.const_addr_list[operand_name],
                    mux=0,
                    mask=self.is_ladder)
                continue
            operand_data = self.solution_data_list[operand_name]
            if time > operand_data.end:
                ram_type = self.mem_data_list[operand_name].operator
                ram_addr = self.mem_data_list[operand_name].addr
                # print(time, value_name, operand_name, ram_addr)
                self.inst_list[time].set_operator_inst(operation=data.operation, operand_index=i, ram_type=ram_type, raddr=ram_addr, mux=0, mask=self.is_ladder)
                continue
            operand_operator = operand_data.operator
            # print(time, value_name, operand_name, operand_operator)
            if "MUL" in operand_operator:
                self.inst_list[time].set_operator_inst(operation=data.operation, operand_index=i, ram_type="", raddr=0, mux=1, mask=self.is_ladder)
            elif "MAS" in operand_operator:
                self.inst_list[time].set_operator_inst(operation=data.operation, operand_index=i, ram_type="", raddr=0, mux=2, mask=self.is_ladder)
            elif "INV" in operand_operator:
                # TODO: fix
                self.inst_list[time].set_operator_inst(operation=data.operation, operand_index=i, ram_type="", raddr=0, mux=3, mask=self.is_ladder)
            else:
                raise Exception("invalid operator: {}".format(operand_operator))

    # 演算器の入力の制御＋RAMの読み出しの制御命令生成
    def operator_init(self):
        for value_name, data in self.solution_data_list.items():
            if value_name in self.input:
                continue
            self.set_operator_inst(data)

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
        # self.ram_result_input()

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
                MASnum=4)
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
