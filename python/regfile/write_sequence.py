import os
import copy
import sys
import argparse
import traceback
import csv
from python.gen_inst.regfile.inst_lib import solutionData, ALURAMIndex, ALUInstruction, new_inst, set_init_inst, set_Fpinv_preprocess_inst, set_Fpinv_inst, set_yrecover2_inst, write_header, write_raminit_aluram, write_raminit_cmdaddr


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
        self.solution_data_list: dict[solutionData] = {}
        self.mem_table = mem_table
        self.mem_data_list = {}
        self.ram_num_list = {}
        self.mem_ctrl_seq = [[]]
        self.operator_init_seq = [[]]

        self.inst_list: list[ALUInstruction] = []
        self.mem_addr_list = []

    # c = a + bなら["c", "ADD", "a", "b"]
    def find_formula(self, valuable):
        for formula in self.formulas:
            if formula[0] == valuable:
                return formula
        raise Exception("invalid valuable: {}".format(valuable))

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
            start_time = int(sol[2]) - 1
            end_time = int(sol[3]) - 1
            self.seq_finish_time = max(self.seq_finish_time, end_time)
            if "_mem" not in value_name:
                formula = self.find_formula(value_name)
                self.solution_data_list[value_name] = solutionData(
                    opr1=formula[2], opr2=formula[3], operator=operator_name, operation=formula[1], start=start_time, end=end_time)
                # print("{}, {}".format(value_name, start_time))

        self.operator_init_seq = [[] for i in range(self.seq_finish_time + 1)]
        self.mem_ctrl_seq = [[] for i in range(self.seq_finish_time + 1)]
        self.inst_list = [ALUInstruction() for i in range(self.seq_finish_time + 1)]

    def set_mem_data(self):
        for sol in self.scheduling_solution:
            mem_value_name = sol[0]
            start_time = int(sol[2]) - 1
            end_time = int(sol[3]) - 1
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
            if memory_data.is_output:
                self.inst_list[start_time].set_mem_write(operator=operator, waddr=memory_data.addr, mask=self.is_ladder)
                continue
            for i in range(len(self.mem_addr_list)):
                if self.mem_addr_list[i] <= start_time:
                    self.inst_list[start_time].set_mem_write(operator=operator, waddr=i + self.index_to_add, mask=self.is_ladder)
                    memory_data.set_addr(i + self.index_to_add)
                    self.mem_addr_list[i] = end_time
                    is_added = True
                    break
            if not is_added:
                self.inst_list[start_time].set_mem_write(operator=operator, waddr=len(self.mem_addr_list) + self.index_to_add, mask=self.is_ladder)
                memory_data.set_addr(len(self.mem_addr_list) + self.index_to_add)
                self.mem_addr_list.append(end_time)
            # print(self.mem_addr_list)

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
                ram_addr = self.mem_data_list[operand_name].addr
                # print(time, value_name, operand_name, ram_addr)
                self.inst_list[time].set_operator_inst(operation=data.operation, operand_index=i, raddr=ram_addr, mux=0, mask=self.is_ladder)
                continue
            operand_operator = operand_data.operator
            # print(time, value_name, operand_name, operand_operator)
            if "MUL" in operand_operator:
                self.inst_list[time].set_operator_inst(operation=data.operation, operand_index=i, raddr=0, mux=1, mask=self.is_ladder)
            elif "MAS" in operand_operator:
                self.inst_list[time].set_operator_inst(operation=data.operation, operand_index=i, raddr=0, mux=2, mask=self.is_ladder)
            elif "INV" in operand_operator:
                # TODO: fix
                self.inst_list[time].set_operator_inst(operation=data.operation, operand_index=i, raddr=0, mux=3, mask=self.is_ladder)
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

    state_sizes = {}

    # for root, dirs, files in os.walk("{}/scheduling/result".format(target_dir)):
    #     for file in files:
    #         if file[-4:] != ".txt":
    #             continue
    target_dir = "./RTL_result/stage{}".format(mul_stage)
    os.makedirs(target_dir, exist_ok=True)
    output_file_path = "{}/RAMINIT_Inst.mem".format(target_dir)
    result_file_path = "./scheduling/ladderMul_mul{}_{}_add{}_{}/result.txt".format(mulNum, mul_stage, addNum, add_stage)
    mem_table = {}
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
        ADDnum=1,
        is_ladder=True)
    try:
        ladder_sche_data.make_sequence()
        # ladder_sche_data.write_csv()
    except Exception:
        etype, value, tb = sys.exc_info()
        estr_list = traceback.format_exception(etype, value, tb)
        for estr in estr_list:
            print(estr, end="")
    ladder_sche_data.inst_list[-5].conInst = 1
    ladder_sche_data.inst_list[-3].condKey1 = 1
    ladder_sche_data.inst_list[-3].condKey0 = 1

    result_file_path = "./scheduling/yrecover_mul{}_{}_add{}_{}/result.txt".format(mulNum, mul_stage, addNum, add_stage)
    mem_table = {}
    # read scheduling result file
    exec(open(result_file_path, 'r', encoding="utf-8").read())
    yrecover_sche_result = schedulingData(
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
        yrecover_sche_result.make_sequence()
        # yrecover_sche_result.write_csv()

    except Exception:
        etype, value, tb = sys.exc_info()
        estr_list = traceback.format_exception(etype, value, tb)
        for estr in estr_list:
            print(estr, end="")

    max_addr = max(len(ladder_sche_data.mem_addr_list), len(yrecover_sche_result.mem_addr_list)) - 1 + yrecover_sche_result.index_to_add
    alu_ram_index = ALURAMIndex(max_addr, 3)
    ladder_inst_list = alu_ram_index.convertInst(ladder_sche_data.inst_list)
    yrecover_inst_list = alu_ram_index.convertInst(yrecover_sche_result.inst_list)
    
    init_inst_list = set_init_inst(alu_ram_index, add_stage)
    Fpinv_preprocess_inst_list = set_Fpinv_preprocess_inst(alu_ram_index, mul_stage)
    Fpinv_inst_list = set_Fpinv_inst(alu_ram_index, mul_stage)
    yrecover2_inst_list = set_yrecover2_inst(alu_ram_index, mul_stage)
    inst_num = len(init_inst_list) + len(ladder_inst_list) + len(yrecover_inst_list) + len(Fpinv_preprocess_inst_list) + len(Fpinv_inst_list) + len(yrecover2_inst_list)

    with open(output_file_path, "w") as f:
        for init_inst in init_inst_list:
            f.write(format(init_inst, f'0{alu_ram_index.inst_bytes}X')+"\n")
        for ladder_inst in ladder_inst_list:
            f.write(format(ladder_inst, f'0{alu_ram_index.inst_bytes}X')+"\n")
        for yrecover_inst in yrecover_inst_list:
            f.write(format(yrecover_inst, f'0{alu_ram_index.inst_bytes}X')+"\n")
        for Fpinv_preprocess_inst in Fpinv_preprocess_inst_list:
            f.write(format(Fpinv_preprocess_inst, f'0{alu_ram_index.inst_bytes}X')+"\n")
        for Fpinv_inst in Fpinv_inst_list:
            f.write(format(Fpinv_inst, f'0{alu_ram_index.inst_bytes}X')+"\n")
        for yrecover2_inst in yrecover2_inst_list:
            f.write(format(yrecover2_inst, f'0{alu_ram_index.inst_bytes}X')+"\n")

    write_header(target_dir, alu_ram_index, inst_num)
    write_raminit_aluram(target_dir, max_addr)
    write_raminit_cmdaddr(target_dir, mul_stage, add_stage, len(ladder_inst_list), len(yrecover_inst_list))
