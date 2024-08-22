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
    def __init__(self, start, end, ram_type, addr=-1, is_output=False) -> None:
        self.start = start
        self.end = end
        self.ram_type = ram_type
        self.addr = addr
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
            MASnum: int,
            is_ladder: bool) -> None:
        self.MULnum = MULnum
        self.MASnum = MASnum
        self.is_ladder = is_ladder

        self.output_file_path = output_file_path
        self.input = input
        self.output = output
        # saved in MAIN_MEM
        self.const_addr_list = {"X1": 0, "X2": 1, "Z1": 2, "Z2": 3, "PX": 4, "PY": 5, "ZERO": 6, "ONE": 7, "A": 8, "B": 9, "4B": 10}
        self.index_to_add = 11

        self.scheduling_solution = scheduling_solution[1:]
        self.formulas = formulas
        self.seq_finish_time = 0
        self.inv_start_time = -2
        self.solution_data_list: dict[str, solutionData] = {}
        self.mem_table = mem_table
        self.mem_data_list: dict[str, memoryData] = {}
        self.mem_ctrl_seq = [[]]
        self.operator_init_seq = [[]]

        self.inst_list: list[ALUInstruction] = []
        self.mem_addr_list: dict[str, list[int]] = {}
        for i in range(MULnum):
            self.mem_addr_list["MUL{num}".format(num=i)] = []
        for i in range(MASnum):
            self.mem_addr_list["MAS{num}".format(num=i)] = []

        # self.default_mem_is_second = {"input": False, "output": False}
        # for i in range(MULnum):
        #     self.default_mem_is_second["MUL{num}".format(num=i)] = False
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
                    self.mem_data_list[value_name] = memoryData(start=self.solution_data_list[value_name].end, end=start_time, ram_type=operator)
            if "_w" in mem_value_name:
                for output_value in self.output:
                    if output_value == mem_value_name[:-2]:
                        self.mem_data_list[output_value] = memoryData(start=start_time, end=end_time, ram_type="MAIN", addr=self.const_addr_list[output_value[:-4]], is_output=True)
                        self.mem_data_list[output_value].set_addr(self.const_addr_list[output_value[:-4]])

    # RAMのアドレス割り当て＋書き込み制御
    # cをアドレス2番地に割り当てる場合
    # self.mem_data["c"] = [10, 15, 2]
    def assign_ram_addr(self):
        for value, memory_data in self.mem_data_list.items():
            start_time = memory_data.start
            end_time = memory_data.end
            ram_type = memory_data.ram_type
            if memory_data.is_output:
                # self.inst_list[start_time].set_mem_write(operator=operator, waddr=memory_data.addr, mask=self.is_ladder)
                continue
            is_added = False
            for i in range(len(self.mem_addr_list[ram_type])):
                if self.mem_addr_list[ram_type][i] <= start_time:
                    waddr = i
                    self.mem_addr_list[ram_type][i] = end_time
                    is_added = True
                    break
            if not is_added:
                waddr = len(self.mem_addr_list[ram_type])
                self.mem_addr_list[ram_type].append(end_time)
            memory_data.set_addr(waddr)
            # self.inst_list[start_time].set_mem_write(operator=operator, waddr=waddr, mask=self.is_ladder)

    def set_operator_inst(self, value_name: str, data: solutionData):
        for i in range(2):
            operand_name = data.opr1 if i == 0 else data.opr2
            time = data.start
            if operand_name in self.input:
                # print(time, value_name, operand_name, self.const_addr_list[operand_name])
                self.inst_list[time].set_mem_read(
                    operation=data.operation,
                    operand_index=i,
                    ram_type="MAIN",
                    raddr=self.const_addr_list[operand_name],
                    mux=0,
                    mask=self.is_ladder)
                continue
            operand_data = self.solution_data_list[operand_name]
            if time > operand_data.end:
                ram_type = self.mem_data_list[operand_name].ram_type
                raddr = self.mem_data_list[operand_name].addr
                # print(time, value_name, operand_name, ram_addr)
                self.inst_list[time].set_mem_read(operation=data.operation, operand_index=i, ram_type=ram_type, raddr=raddr, mux=0, mask=self.is_ladder)
                continue
            operand_operator = operand_data.operator
            # print(time, value_name, operand_name, operand_operator)
            if "MUL" in operand_operator:
                self.inst_list[time].set_mem_read(operation=data.operation, operand_index=i, ram_type="", raddr=0, mux=1, mask=self.is_ladder)
            elif "MAS" in operand_operator:
                self.inst_list[time].set_mem_read(operation=data.operation, operand_index=i, ram_type="", raddr=0, mux=2, mask=self.is_ladder)
            elif "INV" in operand_operator:
                # TODO: fix
                self.inst_list[time].set_mem_read(operation=data.operation, operand_index=i, ram_type="", raddr=0, mux=3, mask=self.is_ladder)
            else:
                raise Exception("invalid operator: {}".format(operand_operator))
        if value_name in self.mem_data_list.keys():
            self.inst_list[time].set_mem_write(output_operator=data.operation, ram_type=self.mem_data_list[value_name].ram_type, waddr=self.mem_data_list[value_name].addr, mask=self.is_ladder)

    # 演算器の入力の制御＋RAMの読み出しの制御命令生成
    def operator_init(self):
        for value_name, data in self.solution_data_list.items():
            if value_name in self.input:
                continue
            self.set_operator_inst(value_name, data)

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
        self.assign_ram_addr()
        self.operator_init()
        # self.ram_result_input()

def file_replace(old_filename, new_filename, old_str, new_str):
    with open(old_filename, "r") as file:
        content = file.read()
    updated_content = content.replace(old_str, new_str)
    with open(new_filename, "w") as file:
        file.write(updated_content)


if __name__ == "__main__":
    psr = argparse.ArgumentParser(
        usage="write_sequence.py -ms <stages_of_multiplier> -as <stages_of_adder>",
        description="Execute scheduling with a 7-stage pipelined Fp montgomery multiplier, four Fp adders/subtractors, an Fp inversion operator",
    )
    psr.add_argument(
        "-ms",
        "--mul_stage",
        required=True,
        help="number of stages of Fp montgomery multipliers",
    )
    psr.add_argument(
        "-as",
        "--add_stage",
        default=1,
        help="number of stages of Fp adder/subtractor",
    )
    args = psr.parse_args()

    mulNum = 1
    mul_stage = int(args.mul_stage)
    addNum = 1
    add_stage = int(args.add_stage)

    input = []
    output = []
    solution = [[]]
    formulas = [[]]
    mem_table = {}

    # target_dir = "./RTL_result/stage{}".format(mul_stage)
    # os.makedirs(target_dir, exist_ok=True)
    # output_file_path = "{}/RAMINIT_Inst.mem".format(target_dir)
    output_file_path = "./RAMINIT_Inst.mem"
    result_file_path = "./scheduling_result/ladderMul_mul{}_{}_add{}_{}/result.txt".format(mulNum, mul_stage, addNum, add_stage)
    # read scheduling result file
    exec(open(result_file_path, 'r', encoding="utf-8").read())

    ladder_sche_data = schedulingData(
        output_file_path=output_file_path,
        input=input,
        output=output,
        scheduling_solution=solution,
        formulas=formulas,
        mem_table=mem_table,
        MULnum=1,
        MASnum=1,
        is_ladder=True)
    ladder_sche_data.make_sequence()

    # print(ladder_sche_data.mem_data_list)
    for value, memory_data in ladder_sche_data.mem_data_list.items():
        print(value, vars(memory_data))