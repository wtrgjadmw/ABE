import os
import copy
import sys
import argparse
import traceback
import csv


def value2num(value):
    if len(value) == 4:
        num = int(value[1]) * 4 + int(value[2]) * 2 + int(value[3])
    elif len(value) == 5:
        num = int(value[1]) * 12 + int(value[2]) * 4 + int(value[3]) * 2 + int(value[4])
    else:
        raise Exception("the length of value: {0} is {1}".format(value, len(value)))
    return num

class ALUInstruction:
    def __init__(self) -> None:
        self.REGF_raddra = 0
        self.REGF_raddr_maska = 0
        self.muxa = 0
        self.REGF_raddrb = 0
        self.REGF_raddr_maskb = 0
        self.muxb = 0
        self.REGF_raddrc = 0
        self.muxc = 0
        self.REGF_raddrd = 0
        self.muxd = 0
        
        self.issub = 0
        self.MM_val = 0
        self.MAS_val = 0
        
        self.REGF_waddra = 0
        self.REGF_waddr_maska = 0
        self.REGF_wea = 0
        self.wmuxa = 0
        
        self.REGF_waddrb = 0
        self.REGF_waddr_maskb = 0
        self.REGF_web = 0
        
        self.inst: int = 0
        
        self.bit_index_list = {
            "REGF_raddra": 0, "REGF_raddr_maska": 4, "muxa": 5,
            "REGF_raddrb": 7, "REGF_raddr_maskb": 11, "muxb": 12,
            "REGF_raddrc": 14, "muxc": 18,
            "REGF_raddrd": 20, "muxd": 24,
            "issub": 26, "MM_val": 27, "MAS_val": 28,
            "REGF_waddra": 29, "REGF_waddr_maska": 33, "REGF_wea": 34, "wmuxa": 35,
            "REGF_waddrb": 36, "REGF_waddr_maskb": 40, "REGF_web": 41
        }
        self.command_length_16bit = 15  # 58/4
        
    def set_operator_inst(self, operator, operand_index, raddr: int, mux: int, mask=False):
        is_masked_addr = mask and raddr < 4
        if "MUL" in operator:
            if operand_index == 0:
                self.REGF_raddra = raddr
                self.REGF_raddr_maska = 1 if is_masked_addr else 0
                self.muxa = mux
            else: # operand_index == 1
                self.REGF_raddrb = raddr
                self.REGF_raddr_maskb = 1 if is_masked_addr else 0
                self.muxb = mux
            self.MM_val = 1
        elif "ADD" in operator or "SUB" in operator:
            if operand_index == 0:
                self.REGF_raddrc = raddr
                self.muxc = mux
            else: # operand_index == 1
                self.REGF_raddrd = raddr
                self.muxd = mux
            self.MAS_val = 1
            self.issub = 1 if "SUB" in operator else 0
        else:
            raise Exception("invalid operator: {}".format(operator))

    def set_mem_write(self, operator, waddr: int, mask=False):
        is_masked_addr = mask and waddr < 4
        if "MUL" in operator:
            self.REGF_waddra = waddr
            self.REGF_waddr_maska = 1 if is_masked_addr else 0
            self.REGF_wea = 1
        elif "ADD" in operator or "SUB" in operator:
            self.REGF_waddrb = waddr
            self.REGF_waddr_maskb = 1 if is_masked_addr else 0
            self.REGF_web = 1
        else:
            raise Exception("invalid operator: {}".format(operator))
                
    def to_string(self):
        self.inst = 0
        for key, value in self.__dict__.items():
            if key == 'bit_index_list' or key == 'command_length_16bit' or key == 'inst':
                continue
            # print(value, end=" ")
            self.inst += value << self.bit_index_list[key]
        # print(format(self.inst, f'0{self.command_length_16bit}x'))
        # print(format(res, f'0{self.command_length_16bit*4}b'))

    def to_list(self):
        return [self.REGF_web, self.REGF_waddr_maskb, self.REGF_waddrb, self.wmuxa, self.REGF_wea, self.REGF_waddr_maska, self.REGF_waddra, self.MAS_val, self.MM_val, self.issub, self.muxd, self.REGF_raddrd, self.muxc, self.REGF_raddrc, self.muxb, self.REGF_raddr_maskb, self.REGF_raddrb, self.muxa, self.REGF_raddr_maska, self.REGF_raddra]

class solutionData:
    def __init__(self, opr1, opr2, operator, start, end) -> None:
        self.opr1 = opr1
        self.opr2 = opr2
        self.operator = operator
        self.start = start
        self.end = end
    
    
# cが10clk目で出力 -> アドレス2に保存 -> 15clk目でオペランドとして最後に呼び出される場合，
# memoryData = {start: RAMに入るのは11clk目, end: 15, addr: x}
class memoryData:
    def __init__(self, start, end, is_output=False) -> None:
        self.start = start
        self.end = end
        self.addr = -1
        self.is_output = is_output
        
    def set_addr(self, addr):
        self.addr = addr

class schedulingData:
    def __init__(
            self,
            output_file_path: str,
            input: list,
            output: list,
            scheduling_solution: list,
            formulas: list,
            mem_table: dict,
            MULnum: int,
            ADDnum: int,
            is_ladder: bool) -> None:
        self.MULnum = MULnum
        self.ADDnum = ADDnum

        self.output_file_path = output_file_path

        self.is_ladder = is_ladder
        self.input = input
        self.output = output
        self.const_addr_list = {"X1": 0, "X2": 1, "Z1": 2, "Z2": 3, "PX": 4, "PY": 5, "ZERO": 6, "ONE": 7, "A": 8, "B": 9, "4B": 10}
        self.index_to_add = 11

        self.scheduling_solution = scheduling_solution[1:]
        self.formulas = formulas
        self.seq_finish_time = 0
        self.inv_start_time = -2
        self.solution_data_list = {}
        self.mem_table = mem_table
        self.mem_data_list = {}
        self.ram_num_list = {}
        self.mem_ctrl_seq = [[]]
        self.operator_init_seq = [[]]
        
        self.inst_list: list[ALUInstruction] = []
        self.mem_addr_list = []

        self.default_mem_is_second = {"input": False, "output": False}
        for i in range(MULnum):
            self.default_mem_is_second["mm{num}".format(num=i)] = False
        for i in range(ADDnum):
            self.default_mem_is_second["add{num}".format(num=i)] = False

    # c = a + bなら["c", "ADD", "a", "b"]
    def find_formula(self, valuable):
        for formula in self.formulas:
            if formula[0] == valuable:
                return formula
        raise Exception("invalid valuable: {}".format(valuable))

    # 演算器がmm0/add0~3の内どれなのか出力
    def check_operator(self, operator, start_time):
        operator_name = operator[:-1]
        operator_num = operator[-1]
        if operator_name == "MUL":
            return "mm{num}".format(num=operator_num)
        elif operator_name == "ADD":
            return "add{num}".format(num=operator_num)
        elif operator_name == "ADD":
            return "add{num}".format(num=operator_num)
        elif operator == "INV":
            self.inv_start_time = start_time
            return "inv"
        else:
            raise Exception("invalid operator: " + operator)

    # 最初に実行
    # c = a + b, ["c", "ADD0", start_time, end_time] の時
    # self.solution_data_list["c"] = ["a", "b", "ADD", "add0", start_time, end_time]
    def set_solution_data(self):
        for sol in self.scheduling_solution:
            if sol[0][-3:] == "_in":
                continue
            if sol[0][-2:] == "_w":
                continue
            value_name = sol[0]
            operator_name = sol[1]
            start_time = int(sol[2])-1
            end_time = int(sol[3])-1
            self.seq_finish_time = max(self.seq_finish_time, end_time)
            if "_mem" not in value_name:
                formula = self.find_formula(value_name)
                # operator = self.check_operator(operator_name, start_time)
                self.solution_data_list[value_name] = solutionData(opr1=formula[2], opr2=formula[3], operator=operator_name, start=start_time, end=end_time)
                # print("{}, {}".format(value_name, start_time))

        self.operator_init_seq = [[] for i in range(self.seq_finish_time+1)]
        self.mem_ctrl_seq = [[] for i in range(self.seq_finish_time+1)]
        self.inst_list = [ALUInstruction() for i in range(self.seq_finish_time+1)]


    def set_mem_data(self):
        for sol in self.scheduling_solution:
            mem_value_name = sol[0]
            start_time = int(sol[2])-1
            end_time = int(sol[3])-1
            if "_mem" in mem_value_name:
                value_name = self.mem_table[mem_value_name]
                if value_name in self.input:
                    continue
                if self.solution_data_list[value_name].end < start_time:
                    self.mem_data_list[value_name] = memoryData(start=self.solution_data_list[value_name].end, end=start_time)
            if "_w" in mem_value_name:
                for output_value in self.output:
                    if output_value == mem_value_name[:-2]:
                        self.mem_data_list[output_value] = memoryData(start=start_time, end=end_time, is_output=True)
                        self.mem_data_list[output_value].set_addr(self.const_addr_list[output_value[:-4]])
                        # print(self.const_addr_list[output_value[:-4]])

    # RAMのアドレス割り当て＋書き込み制御
    # cをアドレス2番地に割り当てる場合
    # self.mem_data_list["c"] = [10, 15, 2]
    def ram_assign(self):
        for value, memory_data in self.mem_data_list.items():
            start_time = memory_data.start
            end_time = memory_data.end
            operator = self.solution_data_list[value].operator
            is_added = False
            if self.mem_data_list[value].is_output:
                self.inst_list[start_time].set_mem_write(operator=operator, waddr=self.mem_data_list[value].addr, mask=self.is_ladder)
                continue
            for i in range(len(self.mem_addr_list)):
                if self.mem_addr_list[i] <= start_time:
                    self.inst_list[start_time].set_mem_write(operator=operator, waddr=i+self.index_to_add, mask=self.is_ladder)
                    self.mem_data_list[value].set_addr(i+self.index_to_add)
                    self.mem_addr_list[i] = end_time
                    is_added = True
                    break
            if not is_added:
                self.inst_list[start_time].set_mem_write(operator=operator, waddr=len(self.mem_addr_list)+self.index_to_add, mask=self.is_ladder)
                self.mem_data_list[value].set_addr(len(self.mem_addr_list)+self.index_to_add)
                self.mem_addr_list.append(end_time)
            # print(self.mem_addr_list)

    def set_operator_inst(self, data, value_name):
        for i in range(2):
            operand_name = data.opr1 if i == 0 else data.opr2
            time = data.start
            if operand_name in self.input:
                # print(time, value_name, operand_name, self.const_addr_list[operand_name])
                self.inst_list[time].set_operator_inst(operator=data.operator, operand_index=i, raddr=self.const_addr_list[operand_name], mux=0, mask=self.is_ladder)
                continue
            operand_data = self.solution_data_list[operand_name]
            if time > operand_data.end:
                ram_addr = self.mem_data_list[operand_name].addr
                # print(time, value_name, operand_name, ram_addr)
                self.inst_list[time].set_operator_inst(operator=data.operator, operand_index=i, raddr=ram_addr, mux=0, mask=self.is_ladder)
                continue
            operand_operator = operand_data.operator
            # print(time, value_name, operand_name, operand_operator)
            if "MUL" in operand_operator:
                self.inst_list[time].set_operator_inst(operator=data.operator, operand_index=i, raddr=0, mux=1, mask=self.is_ladder)
            elif "ADD" in operand_operator or "SUB" in operand_operator:
                self.inst_list[time].set_operator_inst(operator=data.operator, operand_index=i, raddr=0, mux=2, mask=self.is_ladder)
            elif "INV" in operand_operator:
                # TODO: fix
                self.inst_list[time].set_operator_inst(operator=data.operator, operand_index=i, raddr=0, mux=3, mask=self.is_ladder)
            else:
                raise Exception("invalid operator: {}".format(operand_operator))

    # 演算器の入力の制御＋RAMの読み出しの制御命令生成
    def operator_init(self):
        for value_name, data in self.solution_data_list.items():
            if value_name in self.input:
                continue
            self.set_operator_inst(data, value_name)


    def ram_result_input(self):
        for out in self.output:
            operator = self.solution_data_list[out]["operator"].upper()
            write_t = self.solution_data_list[out]["end_time"] - 1
            ram_num = self.ram_num_list[out + "_w"]
            if "w{ram_num}_n_reg <= 1;\n".format(ram_num=ram_num) in self.mem_ctrl_seq[write_t]:
                index = self.mem_ctrl_seq[write_t].index("w{ram_num}_n_reg <= 1;\n".format(ram_num=ram_num))
                self.mem_ctrl_seq[write_t][index] = "w{ram_num}_n_reg <= 0;\n".format(ram_num=ram_num)
            else:
                self.mem_ctrl_seq[write_t].append("w{ram_num}_n_reg <= 0;\n".format(ram_num=ram_num))
            is_const = False
            out = out.replace("NEW_", "").replace("_", "")
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
        for inst in self.inst_list:
            inst.to_string()
            
    def write_csv(self):
        with open(self.output_file_path, 'a') as f:
            writer = csv.writer(f)
            for inst in self.inst_list:
                writer.writerow(inst.to_list())


def file_replace(old_filename, new_filename, old_str, new_str):
    with open(old_filename, "r") as file:
        content = file.read()
    updated_content = content.replace(old_str, new_str)
    with open(new_filename, "w") as file:
        file.write(updated_content)
        

if __name__ == "__main__":
    mulNum = 1
    mulStage = 4
    addNum = 1
    addStage = 1
    
    input = []
    output = []
    solution = [[]]
    formulas = [[]]
    mem_table = {}

    state_sizes = {}

    # for root, dirs, files in os.walk("{}/scheduling/result".format(target_dir)):
    #     for file in files:
    #         if file[-4:] != ".txt":
    #             continue
    output_file_path = "./inst_result/stage{}.csv".format(mulStage)
    result_file_path = "./scheduling/ladderMul_mul{}_{}_add{}_{}/result.txt".format(mulNum, mulStage, addNum, addStage)
    result_file_path = "./scheduling/ladderMul_mul1_4_add1_1/result.txt"
    mem_table = {}
    # read scheduling result file
    exec(open(result_file_path, 'r', encoding="utf-8").read())

    sche_data = schedulingData(
        output_file_path=output_file_path,
        input=input,
        output=output,
        scheduling_solution=solution,
        formulas=formulas,
        mem_table=mem_table,
        MULnum=1,
        ADDnum=1,
        is_ladder=True)
    try:
        sche_data.make_sequence()
        sche_data.write_csv()
        
    except Exception:
        etype, value, tb = sys.exc_info()
        estr_list = traceback.format_exception(etype, value, tb)
        for estr in estr_list:
            print(estr, end="")
            
            
    result_file_path = "./scheduling/yrecover_mul{}_{}_add{}_{}/result.txt".format(mulNum, mulStage, addNum, addStage)
    mem_table = {}
    # read scheduling result file
    exec(open(result_file_path, 'r', encoding="utf-8").read())
    sche_data = schedulingData(
        output_file_path=output_file_path,
        input=input,
        output=output,
        scheduling_solution=solution,
        formulas=formulas,
        mem_table=mem_table,
        MULnum=1,
        ADDnum=1,
        is_ladder=False)
    try:
        sche_data.make_sequence()
        sche_data.write_csv()
        
    except Exception:
        etype, value, tb = sys.exc_info()
        estr_list = traceback.format_exception(etype, value, tb)
        for estr in estr_list:
            print(estr, end="")

    # calc_state_size = max(state_sizes.values()).bit_length()
    # calc_param_file = "{}/RTL/include/CalcCore_param.vh".format(target_dir)
    # f = open(calc_param_file, 'a')
    # f.write("`define CALC_STATE_SIZE " + str(calc_state_size) + "\n")
    # for key, value in state_sizes.items():
    #     f.write("`define CALC_" + key.upper() + "_STATE_SIZE `CALC_STATE_SIZE'd" + str(value) + "\n")
    # f.close()
    # inst = ALUInstruction()
    # inst.to_string()