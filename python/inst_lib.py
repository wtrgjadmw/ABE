from inst_template import init_insts, Fpinv_insts, Fpinv_preprocess_insts, yrecover2_insts


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

        self.condKey0 = 0
        self.condKey1 = 0
        self.conInst = 0
        self.endInst = 0
        self.DRAM_addra = 0
        self.DRAM_wea = 0
        self.DRAM_addrb = 0
        self.DRAM_web = 0

    def set_operator_inst(self, operation, operand_index, raddr: int, mux: int, mask=False):
        is_masked_addr = mask and raddr < 4
        if "MUL" == operation:
            if operand_index == 0:
                self.REGF_raddra = raddr
                self.REGF_raddr_maska = 1 if is_masked_addr else 0
                self.muxa = mux
            else:  # operand_index == 1
                self.REGF_raddrb = raddr
                self.REGF_raddr_maskb = 1 if is_masked_addr else 0
                self.muxb = mux
            self.MM_val = 1
        elif "ADD" == operation or "SUB" == operation:
            if operand_index == 0:
                self.REGF_raddrc = raddr
                self.muxc = mux
            else:  # operand_index == 1
                self.REGF_raddrd = raddr
                self.muxd = mux
            self.MAS_val = 1
            self.issub = 1 if "SUB" == operation else 0
        else:
            raise Exception("invalid operator: {}".format(operation))

    def set_mem_write(self, operator, waddr: int, mask=False):
        is_masked_addr = mask and waddr < 4
        if "MUL" in operator:
            self.REGF_waddra = waddr
            self.REGF_waddr_maska = 1 if is_masked_addr else 0
            self.REGF_wea = 1
        elif "MAS" in operator:
            self.REGF_waddrb = waddr
            self.REGF_waddr_maskb = 1 if is_masked_addr else 0
            self.REGF_web = 1
        else:
            raise Exception("invalid operator: {}".format(operator))

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


class ALURAMIndex:
    def __init__(self, max_addr: int, cal_mux: int) -> None:
        self.mem_size = max_addr + 1
        self.addr_bits = max_addr.bit_length()
        self.cal_mux_bits = cal_mux.bit_length()
        mm_inst_bits = self.addr_bits + self.cal_mux_bits + 1
        add_inst_bits = self.addr_bits + self.cal_mux_bits
        self.alu_inst_bits = mm_inst_bits * 2 + add_inst_bits * 2 + self.addr_bits * 2 + 8
        self.outbram_addr_bits = 4
        self.inst_bits = self.alu_inst_bits + 14
        self.inst_bytes = self.inst_bits // 4 + (0 if self.inst_bits % 4 == 0 else 1)

        self.bit_index_list = {
            "REGF_raddra": 0,
            "REGF_raddr_maska": self.addr_bits,
            "muxa": self.addr_bits + 1,
            "REGF_raddrb": mm_inst_bits,
            "REGF_raddr_maskb": mm_inst_bits + self.addr_bits,
            "muxb": mm_inst_bits + self.addr_bits + 1,
            "REGF_raddrc": mm_inst_bits * 2,
            "muxc": mm_inst_bits * 2 + self.addr_bits,
            "REGF_raddrd": mm_inst_bits * 2 + add_inst_bits,
            "muxd": mm_inst_bits * 2 + add_inst_bits + self.addr_bits,
            "issub": mm_inst_bits * 2 + add_inst_bits * 2,
            "MM_val": mm_inst_bits * 2 + add_inst_bits * 2 + 1,
            "MAS_val": mm_inst_bits * 2 + add_inst_bits * 2 + 2,
            "REGF_waddra": mm_inst_bits * 2 + add_inst_bits * 2 + 3,
            "REGF_waddr_maska": mm_inst_bits * 2 + add_inst_bits * 2 + self.addr_bits + 3,
            "REGF_wea": mm_inst_bits * 2 + add_inst_bits * 2 + self.addr_bits + 4,
            "wmuxa": mm_inst_bits * 2 + add_inst_bits * 2 + self.addr_bits + 5,
            "REGF_waddrb": mm_inst_bits * 2 + add_inst_bits * 2 + self.addr_bits + 6,
            "REGF_waddr_maskb": mm_inst_bits * 2 + add_inst_bits * 2 + self.addr_bits*2 + 6,
            "REGF_web": mm_inst_bits * 2 + add_inst_bits * 2 + self.addr_bits*2 + 7,
            "condKey0": self.alu_inst_bits,
            "condKey1": self.alu_inst_bits + 1,
            "conInst": self.alu_inst_bits + 2,
            "endInst": self.alu_inst_bits + 3,
            "DRAM_addra": self.alu_inst_bits + 4,
            "DRAM_wea": self.alu_inst_bits + self.outbram_addr_bits + 4,
            "DRAM_addrb": self.alu_inst_bits + self.outbram_addr_bits + 5,
            "DRAM_web": self.alu_inst_bits + self.outbram_addr_bits * 2 + 5,
        }

    def convertInst(self, instList: list[ALUInstruction]):
        hexInstList = []
        for inst in instList:
            tmp_hexinst = 0
            for key, value in inst.__dict__.items():
                tmp_hexinst |= value << self.bit_index_list[key]
                # print(key, self.bit_index_list[key])
            hexInstList.append(tmp_hexinst)
        return hexInstList


def new_inst(inst):
    alu_inst = ALUInstruction()
    alu_inst.init_default_value(inst)
    return alu_inst

def set_init_inst(alu_ram_index: ALURAMIndex):
    inst_list = []
    for stage5_inst in init_insts:
        inst_list.append(new_inst(stage5_inst))
    inst_hex_list = alu_ram_index.convertInst(inst_list)
    return inst_hex_list


def set_Fpinv_preprocess_inst(alu_ram_index: ALURAMIndex, stage_num: int):
    inst_list: list[ALUInstruction] = []
    inst_list.append(new_inst(Fpinv_preprocess_insts[0]))
    for i in range(stage_num-1):
        inst_list.append(new_inst([0 for j in range(len(Fpinv_preprocess_insts[0]))]))
    inst_list.append(new_inst(Fpinv_preprocess_insts[1]))
    inst_list[-3].condKey1 = 1
    inst_hex_list = alu_ram_index.convertInst(inst_list)
    return inst_hex_list


def set_Fpinv_inst(alu_ram_index: ALURAMIndex, stage_num: int):
    inst_list: list[ALUInstruction] = []
    inst_list.append(new_inst(Fpinv_insts[0]))
    inst_list.append(new_inst(Fpinv_insts[1]))
    for i in range(stage_num-2):
        inst_list.append(new_inst([0 for j in range(len(Fpinv_insts[0]))]))
    inst_list.append(new_inst(Fpinv_insts[2]))
    inst_list.append(new_inst(Fpinv_insts[3]))
    inst_list[-5].conInst = 1
    inst_list[-3].condKey1 = 1
    inst_list[-3].condKey0 = 1
    inst_hex_list = alu_ram_index.convertInst(inst_list)
    return inst_hex_list


def set_yrecover2_inst(alu_ram_index: ALURAMIndex, stage_num: int):
    inst_list: list[ALUInstruction] = []
    inst_list.append(new_inst(yrecover2_insts[0]))
    inst_list.append(new_inst(yrecover2_insts[1]))
    for i in range(stage_num-2):
        inst_list.append(new_inst([0 for j in range(len(yrecover2_insts[0]))]))
    inst_list.append(new_inst(yrecover2_insts[2]))
    inst_list.append(new_inst(yrecover2_insts[3]))
    inst_list.append(new_inst(yrecover2_insts[4]))
    inst_list.append(new_inst(yrecover2_insts[5]))
    inst_hex_list = alu_ram_index.convertInst(inst_list)
    return inst_hex_list

def write_header(target_dir: str, alu_ram_index: ALURAMIndex):
    with open("{}/header_ALU.vh".format(target_dir), "w") as f:
        f.write("`define ALU_INST_BITS {}\n".format(alu_ram_index.alu_inst_bits))
        f.write("`define MEM_SIZE {}\n".format(alu_ram_index.mem_size))
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
            
def write_raminit_cmdaddr(target_dir: str, stage_num, ladder_cycle, yrecover_cycle):
    cmdaddr_list = [
        1 << 7 + 0,
        255 << 7 | 5,
        1 << 7 | (5 + ladder_cycle),
        379 << 7 | (5 + ladder_cycle + yrecover_cycle + stage_num + 1),
        1 << 7 | (5 + ladder_cycle + yrecover_cycle + stage_num*2 + 3)
    ]
    with open("{}/RAMINIT_CmdAddr.mem".format(target_dir), "w") as f:
        for cmdaddr in cmdaddr_list:
            f.write("{:0=16b}\n".format(cmdaddr))
