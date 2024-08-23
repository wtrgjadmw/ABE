from inst_template import init_insts, Fpinv_insts, Fpinv_preprocess_insts, yrecover2_insts

class MUXConstClass:
    MM_MEM = 0
    MAS_MEM = 1
    MM_SC = 2
    MAS_SC = 3
    MAIN_MEM = 4

MUXConst = MUXConstClass()


class solutionData:
    def __init__(self, opr1, opr2, operator, operation, start, end) -> None:
        self.opr1 = opr1
        self.opr2 = opr2
        self.operator = operator
        self.operation = operation
        self.start = start
        self.end = end

class ALUInstruction:
    def __init__(self) -> None:
        self.MM_raddra = 0
        self.MM_muxa = 0
        self.MM_raddrb = 0
        self.MM_muxb = 0
        self.MM_val = 0

        self.MM_waddr = 0
        self.MM_we = 0


        self.MAS_raddra = 0
        self.MAS_muxa = 0
        self.MAS_raddrb = 0
        self.MAS_muxb = 0
        self.issub = 0
        self.MAS_val = 0

        self.MAS_waddr = 0
        self.MAS_we = 0


        self.MAIN_raddra = 0
        self.MAIN_raddrb = 0
        self.MAIN_waddr = 0
        self.MAIN_we = 0
        self.MAIN_WRITE_mux = 0

        self.MAIN_READ_maska = 0
        self.MAIN_READ_maskb = 0
        self.MAIN_WRITE_mask = 0

        self.condKey0 = 0
        self.condKey1 = 0
        self.conInst = 0
        self.endInst = 0

    def set_mem_read(self, operand_index, ram_type, raddr: int, mask=False):
        is_masked_addr = mask and raddr < 4
        if "MUL" in ram_type:
            if operand_index == 0:
                self.MM_raddra = raddr
            else:
                self.MM_raddrb = raddr
            mux = MUXConst.MM_MEM
        elif "MAS" in ram_type:
            if operand_index == 0:
                self.MAS_raddra = raddr
            else:
                self.MAS_raddrb = raddr
            mux = MUXConst.MAS_MEM
        elif ram_type == "MAIN":
            if operand_index == 0:
                self.MAIN_raddra = raddr
                self.MAIN_READ_maska = 1 if is_masked_addr else 0
            else:
                self.MAIN_raddrb = raddr
                self.MAIN_READ_maskb = 1 if is_masked_addr else 0
            mux = MUXConst.MAIN_MEM
        else:
            raise Exception("invalid BRAM type: {}".format(ram_type))
        return mux

    def set_operator_mux(self, operation, operand_index, mux):
        if "MUL" == operation:
            if operand_index == 0:
                self.MM_muxa = mux
            else:  # operand_index == 1
                self.MM_muxb = mux
            self.MM_val = 1
        elif "ADD" == operation or "SUB" == operation:
            if operand_index == 0:
                self.MAS_muxa = mux
            else:  # operand_index == 1
                self.MAS_muxb = mux
            self.MAS_val = 1
            self.issub = 1 if "SUB" == operation else 0
        else:
            raise Exception("invalid operator: {}".format(operation))

    def set_mem_write(self, output_operator, ram_type, waddr: int, mask=False):
        is_masked_addr = mask and waddr < 4
        if "MUL" in ram_type:
            self.MM_waddr = waddr
            self.MM_we = 1
        elif "MAS" in ram_type:
            self.MAS_waddr = waddr
            self.MAS_we = 1
        elif "MAIN" in ram_type:
            self.MAIN_waddr = waddr
            self.MAIN_WRITE_mask = 1 if is_masked_addr else 0
            self.MAIN_we = 1
            self.MAIN_WRITE_mux = 0 if output_operator == "MUL" else 0
        else:
            raise Exception("invalid ram_type: {}".format(ram_type))

    def to_list(self):
        return [
            self.REGF_web,
            self.REGF_waddr_maskb,
            self.REGF_waddrb,
            self.wmuxa,
            self.REGF_wea,
            self.REGF_waddr_maska,
            self.REGF_waddra,
            self.MAS_val,
            self.MM_val,
            self.issub,
            self.muxd,
            self.REGF_raddrd,
            self.muxc,
            self.REGF_raddrc,
            self.muxb,
            self.REGF_raddr_maskb,
            self.REGF_raddrb,
            self.muxa,
            self.REGF_raddr_maska,
            self.REGF_raddra]

    def init_default_value(self, addr_list: list[int]):
        [
            self.DRAM_web,
            self.DRAM_addrb,
            self.DRAM_wea,
            self.DRAM_addra,
            self.endInst,
            self.conInst,
            self.condKey1,
            self.condKey0,
            self.REGF_web,
            self.REGF_waddr_maskb,
            self.REGF_waddrb,
            self.wmuxa,
            self.REGF_wea,
            self.REGF_waddr_maska,
            self.REGF_waddra,
            self.MAS_val,
            self.MM_val,
            self.issub,
            self.muxd,
            self.REGF_raddrd,
            self.muxc,
            self.REGF_raddrc,
            self.muxb,
            self.REGF_raddr_maskb,
            self.REGF_raddrb,
            self.muxa,
            self.REGF_raddr_maska,
            self.REGF_raddra
        ] = addr_list


class ALUInstIndex:
    def __init__(self):
        MM_MEM_ADDR_BITS = 8
        MAS_MEM_ADDR_BITS = 7
        MAIN_MEM_ADDR_BITS = 7

        INST_CAL_MUX_BIT = 3
        INST_MAIN_MEM_MUX_BIT = 2
        INST_ADDR_MASK_BIT = 1
        INST_MM_MAS_VAL_BIT = 1
        INST_MAS_ISSUB_BIT = 1
        INST_WRITE_MUX_BIT = 1
        INST_WRITE_EN_BIT = 1

        MM_raddra = 0
        MM_muxa = MM_raddra + MM_MEM_ADDR_BITS
        MM_raddrb = MM_muxa + INST_CAL_MUX_BIT
        MM_muxb = MM_raddrb + MM_MEM_ADDR_BITS
        MM_val = MM_muxb + INST_CAL_MUX_BIT
        MM_waddr = MM_val + INST_MM_MAS_VAL_BIT
        MM_we = MM_waddr + MM_MEM_ADDR_BITS

        MAS_raddra = MM_we + INST_WRITE_EN_BIT
        MAS_muxa = MAS_raddra + MAS_MEM_ADDR_BITS
        MAS_raddrb = MAS_muxa + INST_CAL_MUX_BIT
        MAS_muxb = MAS_raddrb + MAS_MEM_ADDR_BITS
        issub = MAS_muxb + INST_CAL_MUX_BIT
        MAS_val = issub + INST_MAS_ISSUB_BIT
        MAS_waddr = MAS_val + INST_MM_MAS_VAL_BIT
        MAS_we = MAS_waddr + MAS_MEM_ADDR_BITS

        MAIN_raddra = MAS_we + INST_WRITE_EN_BIT
        MAIN_raddrb = MAIN_raddra + MAIN_MEM_ADDR_BITS
        MAIN_waddr = MAIN_raddrb + MAIN_MEM_ADDR_BITS
        MAIN_we = MAIN_waddr + MAIN_MEM_ADDR_BITS
        MAIN_WRITE_mux = MAIN_we + INST_WRITE_EN_BIT
        self.alu_inst_bits = MAIN_WRITE_mux + INST_WRITE_MUX_BIT

        MAIN_READ_maska = MAIN_WRITE_mux + INST_WRITE_MUX_BIT
        MAIN_READ_maskb = MAIN_READ_maska + INST_ADDR_MASK_BIT
        MAIN_WRITE_mask = MAIN_READ_maskb + INST_ADDR_MASK_BIT

        condKey0 = MAIN_WRITE_mask + INST_ADDR_MASK_BIT
        condKey1 = condKey0 + 1
        conInst = condKey1 + 1
        endInst = conInst + 1
        self.inst_bits = endInst + 1
        self.inst_bytes = self.inst_bits // 4 + (0 if self.inst_bits % 4 == 0 else 1)


        self.index_list = {
            "MM_raddra": MM_raddra,
            "MM_muxa": MM_muxa,
            "MM_raddrb": MM_raddrb,
            "MM_muxb": MM_muxb,
            "MM_val": MM_val,
            "MM_waddr": MM_waddr,
            "MM_we": MM_we,
            "MAS_raddra": MAS_raddra,
            "MAS_muxa": MAS_muxa,
            "MAS_raddrb": MAS_raddrb,
            "MAS_muxb": MAS_muxb,
            "issub": issub,
            "MAS_val": MAS_val,
            "MAS_waddr": MAS_waddr,
            "MAS_we": MAS_we,
            "MAIN_raddra": MAIN_raddra,
            "MAIN_raddrb": MAIN_raddrb,
            "MAIN_waddr": MAIN_waddr,
            "MAIN_we": MAIN_we,
            "MAIN_WRITE_mux": MAIN_WRITE_mux,
            "MAIN_READ_maska": MAIN_READ_maska,
            "MAIN_READ_maskb": MAIN_READ_maskb,
            "MAIN_WRITE_mask": MAIN_WRITE_mask,
            "condKey0": condKey0,
            "condKey1": condKey1,
            "conInst": conInst,
            "endInst": endInst
        }

    def convertClass2Inst(self, instList: list[ALUInstruction]):
        hexInstList = []
        for inst in instList:
            tmp_hexinst = 0
            for key, value in inst.__dict__.items():
                tmp_hexinst |= value << self.index_list[key]
                # print(key, self.bit_index_list[key])
            hexInstList.append(tmp_hexinst)
        return hexInstList


def new_inst(inst):
    alu_inst = ALUInstruction()
    alu_inst.init_default_value(inst)
    return alu_inst

def set_init_inst(add_stage: int):
    inst_list = [ALUInstruction() for i in range(max(5, 3 + add_stage))]
    inst_list[0].set_operator_inst("ADD", 0, 6, 0)
    inst_list[0].set_operator_inst("ADD", 1, 7, 0)
    inst_list[add_stage].set_mem_write("MAS", 0)
    inst_list[1].set_operator_inst("ADD", 0, 6, 0)
    inst_list[1].set_operator_inst("ADD", 1, 7, 0)
    inst_list[add_stage+1].set_mem_write("MAS", 3)
    inst_list[2].set_operator_inst("ADD", 0, 6, 0)
    inst_list[2].set_operator_inst("ADD", 1, 6, 0)
    inst_list[add_stage+2].set_mem_write("MAS", 2)
    
    inst_list[0].DRAM_addrb = 2
    inst_list[1].condKey0 = 1
    inst_list[2].DRAM_addra = 1
    inst_list[2].set_mem_write("MUL", 1)
    inst_list[2].wmuxa = 1
    inst_list[3].set_mem_write("MUL", 4)
    inst_list[3].wmuxa = 1
    inst_list[4].set_mem_write("MUL", 5)
    inst_list[4].wmuxa = 1
    
    inst_hex_list = convertClass2Inst(inst_list)
    return inst_hex_list


def set_Fpinv_preprocess_inst(mul_stage: int):
    inst_list: list[ALUInstruction] = []
    inst_list.append(new_inst(Fpinv_preprocess_insts[0]))
    for i in range(mul_stage-1):
        inst_list.append(new_inst([0 for j in range(len(Fpinv_preprocess_insts[0]))]))
    inst_list.append(new_inst(Fpinv_preprocess_insts[1]))
    inst_list[-3].condKey1 = 1
    inst_hex_list = convertClass2Inst(inst_list)
    return inst_hex_list


def set_Fpinv_inst(mul_stage: int):
    inst_list: list[ALUInstruction] = []
    inst_list.append(new_inst(Fpinv_insts[0]))
    inst_list.append(new_inst(Fpinv_insts[1]))
    for i in range(mul_stage-2):
        inst_list.append(new_inst([0 for j in range(len(Fpinv_insts[0]))]))
    inst_list.append(new_inst(Fpinv_insts[2]))
    inst_list.append(new_inst(Fpinv_insts[3]))
    inst_list[-5].conInst = 1
    inst_list[-3].condKey1 = 1
    inst_list[-3].condKey0 = 1
    inst_hex_list = convertClass2Inst(inst_list)
    return inst_hex_list


def set_yrecover2_inst(mul_stage: int):
    inst_list: list[ALUInstruction] = []
    inst_list.append(new_inst(yrecover2_insts[0]))
    inst_list.append(new_inst(yrecover2_insts[1]))
    for i in range(mul_stage-2):
        inst_list.append(new_inst([0 for j in range(len(yrecover2_insts[0]))]))
    inst_list.append(new_inst(yrecover2_insts[2]))
    inst_list.append(new_inst(yrecover2_insts[3]))
    inst_list.append(new_inst(yrecover2_insts[4]))
    inst_list.append(new_inst(yrecover2_insts[5]))
    inst_hex_list = convertClass2Inst(inst_list)
    return inst_hex_list

# def write_header(target_dir: str, inst_num: int):
    with open("{}/header_ALU.vh".format(target_dir), "w") as f:
        f.write("`define ALU_INST_BITS {}\n".format(alu_ram_index.alu_inst_bits))
        f.write("`define ALU_MEM_SIZE {}\n".format(alu_ram_index.mem_size))
        f.write("`define ADDR_BITS {}\n".format(alu_ram_index.addr_bits))
        f.write("`define CAL_MUX_BIT {}\n\n".format(alu_ram_index.cal_mux_bits))

        f.write("`define INDEX_READA {}\n".format(alu_ram_index.bit_index_list["REGF_raddra"]))
        f.write("`define INDEX_READB {}\n".format(alu_ram_index.bit_index_list["REGF_raddrb"]))
        f.write("`define INDEX_READC {}\n".format(alu_ram_index.bit_index_list["REGF_raddrc"]))
        f.write("`define INDEX_READD {}\n".format(alu_ram_index.bit_index_list["REGF_raddrd"]))
        f.write("`define INDEX_ISSUB {}\n".format(alu_ram_index.bit_index_list["issub"]))
        f.write("`define INDEX_MMVAL {}\n".format(alu_ram_index.bit_index_list["MM_val"]))
        f.write("`define INDEX_MASVAL {}\n".format(alu_ram_index.bit_index_list["MAS_val"]))
        f.write("`define INDEX_WRITEA {}\n".format(alu_ram_index.bit_index_list["REGF_waddra"]))
        f.write("`define INDEX_WRITEB {}\n".format(alu_ram_index.bit_index_list["REGF_waddrb"]))

    with open("{}/header_core.vh".format(target_dir), "w") as f:
        f.write("`define INST_BITS {}\n".format(alu_ram_index.inst_bits))
        f.write("`define MEM_SIZE {}\n".format(inst_num))
        f.write("`define INST_RAM_addr_BITS {}\n".format(7))
        f.write("`define CMDADDR_repeat_BITS {}\n".format(9))
        f.write("`define OUTBRAM_ADDR_BITS {}\n\n".format(alu_ram_index.outbram_addr_bits))

        f.write("`define INDEX_CONDKEY {}\n".format(alu_ram_index.bit_index_list["condKey0"]))
        f.write("`define INDEX_CONINST {}\n".format(alu_ram_index.bit_index_list["conInst"]))
        f.write("`define INDEX_ENDINST {}\n".format(alu_ram_index.bit_index_list["endInst"]))
        f.write("`define INDEX_DRAMA {}\n".format(alu_ram_index.bit_index_list["DRAM_addra"]))
        f.write("`define INDEX_DRAMB {}\n".format(alu_ram_index.bit_index_list["DRAM_addrb"]))


def write_raminit_aluram(target_dir: str, max_addr):
    with open("{}/RAMINIT_ALURAM.mem".format(target_dir), "w") as f:
        for i in range(7):  # for X1, X2, Z1, Z2, PX, PY, ZERO
            f.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n")
        f.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001\n")   # for ONE
        f.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n")   # for A
        f.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004\n")   # for B
        f.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010\n")   # for 4B
        for i in range(max_addr - 10):  # for midway results
            f.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n")
            
def write_raminit_cmdaddr(target_dir: str, mul_stage, add_stage, ladder_cycle, yrecover_cycle):
    init_cycles = max(5, 3 + add_stage)
    cmdaddr_list = [
        1 << 7 + 0,
        255 << 7 | init_cycles,
        1 << 7 | (init_cycles + ladder_cycle),
        379 << 7 | (init_cycles + ladder_cycle + yrecover_cycle + mul_stage + 1),
        1 << 7 | (init_cycles + ladder_cycle + yrecover_cycle + mul_stage*2 + 3)
    ]
    with open("{}/RAMINIT_CmdAddr.mem".format(target_dir), "w") as f:
        for cmdaddr in cmdaddr_list:
            f.write("{:0=16b}\n".format(cmdaddr))
    
