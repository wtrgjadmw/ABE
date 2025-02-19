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

def value2alphabet(value):
    return "A" if value == 0 else "B"


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
        mux_dict["MM{}_MEM".format(i)] = i*3
        mux_dict["MM{}_SC".format(i)] = i*3 + 1
        mux_dict["MM{}_REG".format(i)] = i*3 + 2
    for i in range(MASnum):
        mux_dict["MAS{}_MEM".format(i)] = i*3 + MMnum*3
        mux_dict["MAS{}_SC".format(i)] = i*3 + 1 + MMnum*3
        mux_dict["MAS{}_REG".format(i)] = i*3 + 2 + MMnum*3
    mux_dict["MAIN_MEM"] = MASnum*3 + MMnum*3
    return mux_dict

class schedulingData:
    def __init__(
            self,
            input: list,
            output: list,
            scheduling_solution: list,
            formulas: list,
            mem_table: dict,
            const_addr_list: dict,
            MMnum: int,
            MASnum: int) -> None:
        self.MMnum = MMnum
        self.MASnum = MASnum

        self.input = input
        self.output = output
        # saved in MAIN_MEM
        self.const_addr_list = const_addr_list
        self.mux_dict = setMUXDict(MMnum, MASnum)
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
        # self.ram_num_list = {}
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
                    operands=formula[1], operator=operator_name, operation=formula[2], start=start_time, end=end_time, csel_flag=formula[3])
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
                    # self.ram_num_list[mem_value_name] = ("A" if "MAIN" in mem_is_used else "B")
                    mem_is_used.append("MAIN")
                    continue
                operator = self.solution_data_list[value_name].operator
                if self.solution_data_list[value_name].end + 1 < start_time:
                    # self.ram_num_list[mem_value_name] = ("A" if operator in mem_is_used else "B")
                    mem_is_used.append(operator)
                    self.mem_data_list[value_name] = memoryData(start=self.solution_data_list[value_name].end, end=start_time, ram_type=operator)
            if "_w" in mem_value_name:
                for output_value in self.output:
                    if output_value == mem_value_name[:-2]:
                        #print(mem_value_name, self.const_addr_list[output_value[:-4]])
                        self.inst_list[start_time-1].set_mem_write(output_operator=self.solution_data_list[output_value].operator, ram_type="MAIN", waddr=self.const_addr_list[output_value])
                        #self.inst_list[start_time-1].set_mem_write(output_operator=self.solution_data_list[output_value].operator, ram_type="MAIN", waddr=self.const_addr_list[output_value[:-4]])

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
            # self.inst_list[start_time].set_mem_write(operator=operator, waddr=waddr)

    def set_operator_inst(self, value_name: str, data: solutionData):
        time = data.start
        operator = data.operator
        #print("{}: {}clk".format(value_name, time), end=", ")
        # print(data.operands)
        for i in range(len(data.operands)):
            operand_name = data.operands[i]
            if operand_name in self.input:
                # print(value_name, time, operand_name, self.const_addr_list[operand_name])
                # read_port = self.ram_num_list["{}_mem{}".format(value_name, i)]
                if data.operator == "CSEL":
                    self.inst_list[time].inst_dict["CSL_START"] = 1
                    self.inst_list[time].inst_dict["CSL_MODE"] = data.csel_flag
                    self.inst_list[time+i].set_mem_read(
                    ram_type="MAIN",
                    read_port = "A",
                    raddr=self.const_addr_list[operand_name])
                else:
                    self.inst_list[time].set_mem_read(
                        ram_type="MAIN",
                        read_port = value2alphabet(i),
                        raddr=self.const_addr_list[operand_name])
                    #print(value_name, data.operation)
                    self.inst_list[time].set_operator_init(solution_data=data, operand_index=i, mux=self.mux_dict["MAIN_MEM"])
                continue
            operand_data = self.solution_data_list[operand_name]
            #print("{}: {}clk".format(operand_name, operand_data.end), end=", ")
            if time > operand_data.end+1:
                ram_type = self.mem_data_list[operand_name].ram_type
                #print("{}_MEM".format(ram_type))
                raddr = self.mem_data_list[operand_name].addr
                # read_port = self.ram_num_list["{}_mem{}".format(value_name, i)]
                read_port = value2alphabet(i)
                #print(time, value_name, operand_name, ram_type, raddr)
                self.inst_list[time].set_mem_read(ram_type=ram_type, read_port = read_port,raddr=raddr)
                self.inst_list[time].set_operator_init(solution_data=data, operand_index=i, mux=self.mux_dict["{}_MEM".format(ram_type)])
                continue
            pre_operator = operand_data.operator
            # print(time, value_name, operand_name, operand_operator)
            if time == operand_data.end+1:
                #print("{}_REG".format(pre_operator))
                self.inst_list[time].set_operator_init(solution_data=data, operand_index=i, mux=self.mux_dict["{}_REG".format(pre_operator)])
            elif time == operand_data.end:
                #print("{}_SC".format(pre_operator))
                self.inst_list[time].set_operator_init(solution_data=data, operand_index=i, mux=self.mux_dict["{}_SC".format(pre_operator)])
            if "INV" in pre_operator:
                # TODO: fix
                self.inst_list[time].set_operator_init(solution_data=data, operand_index=i, mux=1)
            # else:
            #     raise Exception("invalid operator: {}".format(pre_operator))
        if value_name in self.mem_data_list.keys():
            self.inst_list[time].set_mem_write(output_operator=data.operation, ram_type=self.mem_data_list[value_name].ram_type, waddr=self.mem_data_list[value_name].addr)

    # 演算器の入力の制御＋RAMの読み出しの制御命令生成
    def operator_init(self):
        for value_name, data in self.solution_data_list.items():
            if value_name in self.input and value_name not in self.output:
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
        "-can", "--config_addNum", default=1, help="number of Modular Adders/Subtractors (default is 4)"
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
    psr.add_argument("-n", "--name", required=True, help="スケジューリング対象の名前")
    args = psr.parse_args()

    MMnum = int(args.mulNum)
    MULstage = int(args.mulStage)
    MASnum = int(args.addNum)
    config_MASnum = int(args.config_addNum)
    MASstage = int(args.addStage)
    algo_name = args.name

    scheduling_config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=MMnum, ms=MULstage, an=config_MASnum, as_=MASstage)
    config = "stage{ms}MM{mn}_stage{as_}MAS{an}".format(mn=MMnum, ms=MULstage, an=MASnum, as_=MASstage)
    target_dir = "./RTL_result/{}".format(config)
    os.makedirs(target_dir, exist_ok=True)

    alu_ram_index = ALUInstIndex(MMnum, MASnum)
    alu_ram_index.writeHeaderCoreVH("{}/header_core.vh".format(target_dir))
    writeABEALU(MMnum, MASnum, "{}/abe_core_alu.v".format(target_dir))

    def write_instructions(algo_name: str, const_addr_list: dict):
        output_file_path = "{}/RAMINIT_Inst_{}_bin.mem".format(target_dir, algo_name)
        result_file_path = "./scheduling_result/{}/{}/result.txt".format(scheduling_config, algo_name)
        # read scheduling result file
        namespace = {}
        exec(open(result_file_path, 'r', encoding="utf-8").read(), globals(), namespace)

        sche_data = schedulingData(
            input=namespace['input'],
            output=namespace['output'],
            scheduling_solution=namespace['solution'],
            formulas=namespace['formulas'],
            mem_table=namespace['mem_table'],
            const_addr_list=const_addr_list,
            MMnum=MMnum,
            MASnum=MASnum)
        sche_data.make_sequence()

        sche_data_inst_list = alu_ram_index.convertClass2Inst(sche_data.inst_list)
        with open(output_file_path, "w") as f:
            for sche_data_inst in sche_data_inst_list:
                f.write(format(sche_data_inst, f'0{alu_ram_index.inst_bits}b')+"\n") 
                # hex表記
                # f.write(format(sche_data_inst, f'0{alu_ram_index.inst_bytes}X')+"\n") 

    # SSWU map
    const_addr_list = {'t0': 0, 't1': 1, 'UV30': 18, 'UV31': 20, 'UV3_exp0': 19, 'UV3_exp1': 21, 'Z_Hash0': 4, 'Z_Hash1': 5, 'UV0': 6, 'UV1': 7, 'V0': 8, 'V1': 9, 'U0': 10, 'U1': 11, 'N0': 12, 'N1': 13, 't20': 14, 't21': 15, 'xit20': 22, 'xit21': 23, 'D0': 16, 'D1': 17, 'X_Hash0': 24, 'X_Hash1': 25, 'Y_Hash0': 26, 'Y_Hash1': 27, 'xit2N0': 28, 'xit2N1': 29, 'alpha2V_U0': 30, 'y20': 31, 'alpha0': 32, 'alpha2V_U1': 33, 'y21': 34, 'alpha1': 35, 'y0': 36, 'y_alt0': 37, 'y1': 38, 'y_alt1': 39, 'Y_0': 40, 'Y_1': 41, "X1": 0, "X2": 1, "Z1": 2, "Z2": 3, "PX": 4, "PY": 5, "X10": 6, "X11": 8, "X20": 7, "X21": 9, "Z10": 10, "Z11": 12, "Z20": 11, "Z21": 13, "QX0": 14, "QX1": 15, "QY0": 16, "QY1": 17, "B3_": 170, "xiA": 172, 'negA_': 173, "sqrt_negxi3": 174, "A_": 175, "B_": 176, "xi": 177, 'k0_0': 178, 'k0_1': 179, 'k0_2': 180, 'k0_3': 181, 'k0_4': 182, 'k0_5': 183, 'k0_6': 184, 'k0_7': 185, 'k0_8': 186, 'k0_9': 187, 'k0_10': 188, 'k0_11': 189, 'k2_0': 190, 'k2_1': 191, 'k2_2': 192, 'k2_3': 193, 'k2_4': 194, 'k2_5': 195, 'k2_6': 196, 'k2_7': 197, 'k2_8': 198, 'k2_9': 199, 'k2_10': 200, 'k2_11': 201, 'k2_12': 202, 'k2_13': 203, 'k2_14': 204, 'k2_15': 205, 'k1_0': 206, 'k1_1': 207, 'k1_2': 208, 'k1_3': 209, 'k1_4': 210, 'k1_5': 211, 'k1_6': 212, 'k1_7': 213, 'k1_8': 214, 'k1_9': 215, 'k1_10': 216, 'k3_0': 217, 'k3_1': 218, 'k3_2': 219, 'k3_3': 220, 'k3_4': 221, 'k3_5': 222, 'k3_6': 223, 'k3_7': 224, 'k3_8': 225, 'k3_9': 226, 'k3_10': 227, 'k3_11': 228, 'k3_12': 229, 'k3_13': 230, 'k3_14': 231, 'k3_15': 232, "B3": 249, "ZERO": 250, "ONE": 251, "A": 252, "B": 253, "4B": 254}
    # pairing ML
    # const_addr_list = {"PX": 0, "PY": 1, "PX_": 2, "PY_": 3, "3PX": 4, "QX0": 5, "QX1": 6, "QY0": 7, "QY1": 8, "-QY0": 9, "-QY1": 10, "TX0": 11, "TX1": 12, "TY0": 13, "TY1": 14, "TZ0": 15, "TZ1": 16, "a000": 17, "a001": 18, "a010": 19, "a011": 20, "a100": 21, "a101": 22, "a110": 23, "a111": 24, "a200": 25, "a201": 26, "a210": 27, "a211": 28, "b000": 29, "b001": 30, "b010": 31, "b011": 32, "b100": 33, "b101": 34, "b110": 35, "b111": 36, "b200": 37, "b201": 38, "b210": 39, "b211": 40, "c000": 17, "c001": 18, "c010": 19, "c011": 20, "c100": 21, "c101": 22, "c110": 23, "c111": 24, "c200": 25, "c201": 26, "c210": 27, "c211": 28, "d000": 29, "d001": 30, "d010": 31, "d011": 32, "d100": 33, "d101": 34, "d110": 35, "d111": 36, "d200": 37, "d201": 38, "d210": 39, "d211": 40, "ZERO": 250, "BT0": 253, "BT1": 253}
    # pairing FE
    # const_addr_list = {'XI10': 233, 'XI11': 234, 'XI20': 235, 'XI21': 236, 'XI30': 237, 'XI31': 238, 'XI40': 239, 'XI41': 240, 'XI50': 241, 'XI51': 242, "b000": 29, "b001": 30, "b010": 31, "b011": 32, "b100": 33, "b101": 34, "b110": 35, "b111": 36, "b200": 37, "b201": 38, "b210": 39, "b211": 40, "a000": 17, "a001": 18, "a010": 19, "a011": 20, "a100": 21, "a101": 22, "a110": 23, "a111": 24, "a200": 25, "a201": 26, "a210": 27, "a211": 28, "c000": 29, "c001": 30, "c010": 31, "c011": 32, "c100": 33, "c101": 34, "c110": 35, "c111": 36, "c200": 37, "c201": 38, "c210": 39, "c211": 40, 'c_qinv_denom_inv_denom': 41, 'c_qinv_denom0': 42, 'c_qinv_denom1': 43, 'c_q00': 44, 'c_q01': 45, 'c_q10': 46, 'c_q11': 47, 'c_pa00': 48, 'c_pa01': 49, 'c_pa10': 50, 'c_pa11': 51, 'c_pb00': 52, 'c_pb01': 53, 'c_pb10': 54, 'c_pb11': 55, 'c_pc00': 56, 'c_pc01': 57, 'c_pc10': 58, 'c_pc11': 59,"ZERO": 250, "ONE": 251}
    # Fp12 exp
    # const_addr_list = {'a000': 0, 'b000': 1, 'a001': 2, 'b001': 3, 'a010': 4, 'b010': 5, 'a011': 6, 'b011': 7, 'a100': 8, 'b100': 9, 'a101': 10, 'b101': 11, 'a110': 12, 'b110': 13, 'a111': 14, 'b111': 15, 'a200': 16, 'b200': 17, 'a201': 18, 'b201': 19, 'a210': 20, 'b210': 21, 'a211': 22, 'b211': 23, 'd000': 0, 'c000': 1, 'd001': 2, 'c001': 3, 'd010': 4, 'c010': 5, 'd011': 6, 'c011': 7, 'd100': 8, 'c100': 9, 'd101': 10, 'c101': 11, 'd110': 12, 'c110': 13, 'd111': 14, 'c111': 15, 'd200': 16, 'c200': 17, 'd201': 18, 'c201': 19, 'd210': 20, 'c210': 21, 'd211': 22, 'c211': 23}
    write_instructions(algo_name, const_addr_list)
