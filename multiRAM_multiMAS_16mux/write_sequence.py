import os
import copy
import sys
import argparse
import traceback

from inst_lib import solutionData, ALUInstIndex, ALUInstruction, new_inst, set_init_inst, set_Fpinv_preprocess_inst, set_Fpinv_inst, set_yrecover2_inst, write_raminit_aluram, write_raminit_cmdaddr, writeABEALU


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
    def __init__(self, start, end, ram_type, addr=-1) -> None:
        self.start = start
        self.end = end
        self.ram_type = ram_type
        self.addr = addr

    def set_addr(self, addr):
        self.addr = addr


def setMUXDict(MMnum, MASnum):
    mux_dict = {}
    for i in range(MMnum):
        mux_dict["MM{}_MEMA".format(i)] = i*4
        mux_dict["MM{}_MEMB".format(i)] = i*4 + 1
        mux_dict["MM{}_SC".format(i)] = i*4 + 2
        mux_dict["MM{}_REG".format(i)] = i*4 + 3
    for i in range(MASnum):
        mux_dict["MAS{}_MEMA".format(i)] = i*4 + MMnum*4
        mux_dict["MAS{}_MEMB".format(i)] = i*4 + 1 + MMnum*4
        mux_dict["MAS{}_SC".format(i)] = i*4 + 2 + MMnum*4
        mux_dict["MAS{}_REG".format(i)] = i*4 + 3 + MMnum*4
    mux_dict["MAIN_MEMA"] = MASnum*4 + MMnum*4
    mux_dict["MAIN_MEMB"] = MASnum*4 + MMnum*4 + 1
    return mux_dict

class schedulingData:
    def __init__(
            self,
            output_file_path: str,
            input: list,
            output: list,
            scheduling_solution: list,
            formulas: list,
            mem_table: dict,
            MMnum: int,
            MASnum: int,
            is_ladder: bool) -> None:
        self.MMnum = MMnum
        self.MASnum = MASnum
        self.is_ladder = is_ladder

        self.output_file_path = output_file_path
        self.input = input
        self.output = output
        # saved in MAIN_MEM
        self.const_addr_list = {"X1": 0, "X2": 1, "Z1": 2, "Z2": 3, "PX": 4, "PY": 5, "A": 6, "B": 7, "4B": 8, "ZERO": 9, "ONE": 10}
        self.mux_dict = setMUXDict(MMnum, MASnum)

        self.scheduling_solution = scheduling_solution
        self.formulas = formulas
        self.seq_finish_time = 0
        self.inv_start_time = -2
        self.solution_data_list: dict[str, solutionData] = {}
        self.mem_table = mem_table
        self.mem_data_list: dict[str, memoryData] = {}
        self.operator_init_seq = [[]]

        self.inst_list: list[ALUInstruction] = []
        self.mem_addr_list: dict[str, list[int]] = {}
        self.ram_num_list = {}
        for i in range(MMnum):
            self.mem_addr_list["MM{num}".format(num=i)] = []
        for i in range(MASnum):
            self.mem_addr_list["MAS{num}".format(num=i)] = []

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
            start_time = int(sol[2]) - 1
            end_time = int(sol[3]) - 1
            if sol[0][-2:] == "_w":
                self.seq_finish_time = max(self.seq_finish_time, end_time)
                continue
            value_name = sol[0]
            operator_name = sol[1]
            if "_mem" not in value_name:
                formula = self.find_formula(value_name)
                self.solution_data_list[value_name] = solutionData(
                    opr1=formula[2], opr2=formula[3], operator=operator_name, operation=formula[1], start=start_time, end=end_time)
        self.operator_init_seq = [[] for i in range(self.seq_finish_time)]
        self.inst_list = [ALUInstruction(self.MMnum, self.MASnum) for i in range(self.seq_finish_time)]

    def set_mem_data(self):
        mem_is_used = []
        prev_start_time = -1
        for sol in self.scheduling_solution:
            mem_value_name = sol[0]
            start_time = int(sol[2])
            if prev_start_time != start_time:
                mem_is_used = []
            prev_start_time = start_time
            end_time = int(sol[3])
            if "_mem" in mem_value_name:
                value_name = self.mem_table[mem_value_name]
                if value_name in self.input:
                    self.ram_num_list[mem_value_name] = ("A" if "MAIN" in mem_is_used else "B")
                    mem_is_used.append("MAIN")
                    continue
                operator = self.solution_data_list[value_name].operator
                if self.solution_data_list[value_name].end + 1 < start_time:
                    self.ram_num_list[mem_value_name] = ("A" if operator in mem_is_used else "B")
                    mem_is_used.append(operator)
                    self.mem_data_list[value_name] = memoryData(start=self.solution_data_list[value_name].end, end=start_time, ram_type=operator)
            if "_w" in mem_value_name:
                for output_value in self.output:
                    if output_value == mem_value_name[:-2]:
                        self.inst_list[start_time-1].set_mem_write(output_operator=self.solution_data_list[mem_value_name[:-2]].operator, ram_type="MAIN", waddr=self.const_addr_list[output_value[:-4]], mask=self.is_ladder)

    # RAMのアドレス割り当て＋書き込み制御
    # cをアドレス2番地に割り当てる場合
    # self.mem_data["c"] = [10, 15, 2]
    def assign_ram_addr(self):
        for value, memory_data in self.mem_data_list.items():
            start_time = memory_data.start
            end_time = memory_data.end
            ram_type = memory_data.ram_type
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
        time = data.start
        operator = data.operator
        for i in range(2):
            operand_name = data.opr1 if i == 0 else data.opr2
            if operand_name in self.input:
                # print(value_name, time, operand_name, self.const_addr_list[operand_name])
                read_port = self.ram_num_list["{}_mem{}".format(value_name, i)]
                self.inst_list[time].set_mem_read(
                    ram_type="MAIN",
                    read_port = read_port,
                    raddr=self.const_addr_list[operand_name],
                    mask=self.is_ladder)
                self.inst_list[time].set_operator_init(operator=operator, operation=data.operation, operand_index=i, mux=self.mux_dict["MAIN_MEM{}".format(read_port)])
                continue
            operand_data = self.solution_data_list[operand_name]
            if time > operand_data.end+1:
                # print(value_name, operand_name)
                ram_type = self.mem_data_list[operand_name].ram_type
                raddr = self.mem_data_list[operand_name].addr
                read_port = self.ram_num_list["{}_mem{}".format(value_name, i)]
                # print(time, value_name, operand_name, ram_addr)
                self.inst_list[time].set_mem_read(ram_type=ram_type, read_port = read_port,raddr=raddr, mask=self.is_ladder)
                self.inst_list[time].set_operator_init(operator=operator, operation=data.operation, operand_index=i, mux=self.mux_dict["{}_MEM{}".format(ram_type, read_port)])
                continue
            pre_operator = operand_data.operator
            # print(time, value_name, operand_name, operand_operator)
            if time == operand_data.end+1:
                self.inst_list[time].set_operator_init(operator=operator, operation=data.operation, operand_index=i, mux=self.mux_dict["{}_REG".format(pre_operator)])
            elif time == operand_data.end:
                self.inst_list[time].set_operator_init(operator=operator, operation=data.operation, operand_index=i, mux=self.mux_dict["{}_SC".format(pre_operator)])
            if "INV" in pre_operator:
                # TODO: fix
                self.inst_list[time].set_operator_init(operator=operator, operation=data.operation, operand_index=i, mux=1)
            # else:
            #     raise Exception("invalid operator: {}".format(pre_operator))
        if value_name in self.mem_data_list.keys():
            self.inst_list[time].set_mem_write(output_operator=data.operation, ram_type=self.mem_data_list[value_name].ram_type, waddr=self.mem_data_list[value_name].addr, mask=self.is_ladder)

    # 演算器の入力の制御＋RAMの読み出しの制御命令生成
    def operator_init(self):
        for value_name, data in self.solution_data_list.items():
            if value_name in self.input:
                continue
            self.set_operator_inst(value_name, data)

    def make_sequence(self):
        self.set_solution_data()
        self.set_mem_data()
        self.assign_ram_addr()
        self.operator_init()

    
if __name__ == "__main__":
    psr = argparse.ArgumentParser(
        usage="write_sequence.py -mn <number_of_MM> -ms <stages_of_MM> -an <number_of_MAS> -as <stages_of_MAS> -n <algorithm_name>",
        description="Execute scheduling with a 7-stage pipelined Fp montgomery multiplier, four Fp adders/subtractors, an Fp inversion operator",
    )
    psr.add_argument(
        "-mn",
        "--mulNum",
        default=1,
        help="number of Modular Multiplier (default is 1)",
    )
    psr.add_argument(
        "-ms",
        "--mulStage",
        required=True,
        help="number of stages of Modular Multiplier",
    )
    psr.add_argument(
        "-an", "--addNum", default=1, help="number of Modular Adders/Subtractors (default is 4)"
    )
    psr.add_argument(
        "-as",
        "--addStage",
        required=True,
        help="number of stages of Modular Adder/Subtractor",
    )
    # psr.add_argument("-n", "--name", required=True, help="スケジューリング対象の名前")
    args = psr.parse_args()

    MMnum = int(args.mulNum)
    MULstage = int(args.mulStage)
    MASnum = int(args.addNum)
    MASstage = int(args.addStage)

    config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=MMnum, ms=MULstage, an=MASnum, as_=MASstage)
    target_dir = "./RTL_result/{}".format(config)
    os.makedirs(target_dir, exist_ok=True)

    alu_ram_index = ALUInstIndex(MMnum, MASnum)
    alu_ram_index.writeHeaderCoreVH("{}/header_core.vh".format(target_dir))
    writeABEALU(MMnum, MASnum, "{}/abe_core_alu.v".format(target_dir))

    def write_instructions(algo_name: str):
        output_file_path = "{}/RAMINIT_Inst_{}.mem".format(target_dir, algo_name)
        result_file_path = "./scheduling_result/{}/{}/result.txt".format(config, algo_name)
        # read scheduling result file
        namespace = {}
        exec(open(result_file_path, 'r', encoding="utf-8").read(), globals(), namespace)

        sche_data = schedulingData(
            output_file_path=output_file_path,
            input=namespace['input'],
            output=namespace['output'],
            scheduling_solution=namespace['solution'],
            formulas=namespace['formulas'],
            mem_table=namespace['mem_table'],
            MMnum=MMnum,
            MASnum=MASnum,
            is_ladder=(algo_name == "ladderMul"))
        sche_data.make_sequence()
        # print(sche_data.mem_data_list)
        # for value, memory_data in sche_data.mem_data_list.items():
        #     print(value, vars(memory_data))
        # for inst in sche_data.inst_list:
        #     print(vars(inst))
        if (algo_name == "ladderMul"):
            sche_data.inst_list[-3].inst_dict["INST_CONT"] = 1
            sche_data.inst_list[-3].inst_dict["CONDKEY0"] = 1
            sche_data.inst_list[-3].inst_dict["CONDKEY1"] = 1

        sche_data_inst_list = alu_ram_index.convertClass2Inst(sche_data.inst_list)
        with open(output_file_path, "w") as f:
            for sche_data_inst in sche_data_inst_list:
                f.write(format(sche_data_inst, f'0{alu_ram_index.inst_bytes}X')+"\n")


    write_instructions("ladderMul")
    write_instructions("yrecover")
    




    