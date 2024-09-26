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
    def __init__(self, MMnum, MASnum) -> None:
        self.MMnum = MMnum
        self.MASnum = MASnum
        self.inst_dict = {}

        for i in range(MMnum):
            self.inst_dict["MM{}_READA".format(i)] = 0
            self.inst_dict["MM{}_MUXA".format(i)] = 0
            self.inst_dict["MM{}_READB".format(i)] = 0
            self.inst_dict["MM{}_MUXB".format(i)] = 0
            self.inst_dict["MM{}_VAL".format(i)] = 0
            self.inst_dict["MM{}_WRITE".format(i)] = 0
            self.inst_dict["MM{}_WE".format(i)] = 0

        for i in range(MASnum):
            self.inst_dict["MAS{}_READA".format(i)] = 0
            self.inst_dict["MAS{}_MUXA".format(i)] = 0
            self.inst_dict["MAS{}_READB".format(i)] = 0
            self.inst_dict["MAS{}_MUXB".format(i)] = 0
            self.inst_dict["MAS{}_ISSUB".format(i)] = 0
            self.inst_dict["MAS{}_VAL".format(i)] = 0
            self.inst_dict["MAS{}_WRITE".format(i)] = 0
            self.inst_dict["MAS{}_WE".format(i)] = 0


        self.inst_dict["MAIN_READA"] = 0
        self.inst_dict["MAIN_READB"] = 0
        self.inst_dict["MAIN_WRITE"] = 0
        self.inst_dict["MAIN_WE"] = 0
        self.inst_dict["MAIN_WRITE_MUX"] = 0
        self.inst_dict["MAIN_READ_MASKA"] = 0
        self.inst_dict["MAIN_READ_MASKB"] = 0
        self.inst_dict["MAIN_WRITE_MASK"] = 0

        self.inst_dict["CONDKEY0"] = 0
        self.inst_dict["CONDKEY1"] = 0
        self.inst_dict["INST_CONT"] = 0
        self.inst_dict["INST_END"] = 0

    def index2alphabet(self, index: int):
        return chr(65+index)

    def set_mem_read(self, operand_index: int, ram_type, raddr: int, mask=False):
        suffix = self.index2alphabet(operand_index)
        if ram_type == "MAIN":
            is_masked_addr = mask and 0 <= raddr <= 3
            self.inst_dict["MAIN_READ{}".format(suffix)] = raddr
            self.inst_dict["MAIN_READ_MASK{}".format(suffix)] = 1 if is_masked_addr else 0
        else:
            self.inst_dict["{}_READ{}".format(ram_type, suffix)] = raddr

    def set_operator_init(self, operator, operation, operand_index, mux):
        suffix = self.index2alphabet(operand_index)
        self.inst_dict["{}_MUX{}".format(operator, suffix)] = mux
        self.inst_dict["{}_VAL".format(operator)] = 1
        if "MAS" in operator:
            self.inst_dict["{}_ISSUB".format(operator)] = 1 if "SUB" == operation else 0

    def set_mem_write(self, output_operator, ram_type, waddr: int, mask=False):
        if ram_type == "MAIN":
            self.inst_dict["MAIN_WRITE"] = waddr
            is_masked_addr = mask and 0 <= waddr <= 3
            self.inst_dict["MAIN_WRITE_MASK"] = 1 if is_masked_addr else 0
            self.inst_dict["MAIN_WE"] = 1
            operator_index = int(output_operator[-1])
            self.inst_dict["MAIN_WRITE_MUX"] = operator_index if "MM" in output_operator else self.MMnum + operator_index
        else:
            self.inst_dict["{}_WRITE".format(ram_type)] = waddr
            self.inst_dict["{}_WE".format(ram_type)] = 1



class ALUInstIndex:
    def __init__(self, MMnum:int, MASnum:int):
        self.MMnum = MMnum
        self.MASnum = MASnum
        self.MM_MEM_ADDR_BITS = 7
        self.MAS_MEM_ADDR_BITS = 6
        self.MAIN_MEM_ADDR_BITS = 8

        self.INST_CAL_MUX_BIT = (MMnum*4 + MASnum*4).bit_length()
        self.INST_ADDR_MASK_BIT = 1
        self.INST_MM_MAS_VAL_BIT = 1
        self.INST_MAS_ISSUB_BIT = 1
        self.INST_WRITE_MUX_BIT = (MMnum + MASnum - 1).bit_length()
        self.INST_WRITE_EN_BIT = 1

        self.index_list = {}
        cnt = 0
        for i in range(MMnum):
            self.index_list["MM{}_READA".format(i)] = cnt
            self.index_list["MM{}_MUXA".format(i)] = self.index_list["MM{}_READA".format(i)] + self.MM_MEM_ADDR_BITS
            self.index_list["MM{}_READB".format(i)] = self.index_list["MM{}_MUXA".format(i)] + self.INST_CAL_MUX_BIT
            self.index_list["MM{}_MUXB".format(i)] = self.index_list["MM{}_READB".format(i)] + self.MM_MEM_ADDR_BITS
            self.index_list["MM{}_VAL".format(i)] = self.index_list["MM{}_MUXB".format(i)] + self.INST_CAL_MUX_BIT
            self.index_list["MM{}_WRITE".format(i)] = self.index_list["MM{}_VAL".format(i)] + self.INST_MM_MAS_VAL_BIT
            self.index_list["MM{}_WE".format(i)] = self.index_list["MM{}_WRITE".format(i)] + self.MM_MEM_ADDR_BITS
            cnt = self.index_list["MM{}_WE".format(i)] + self.INST_WRITE_EN_BIT

        for i in range(MASnum):
            self.index_list["MAS{}_READA".format(i)] = cnt
            self.index_list["MAS{}_MUXA".format(i)] = self.index_list["MAS{}_READA".format(i)] + self.MAS_MEM_ADDR_BITS
            self.index_list["MAS{}_READB".format(i)] = self.index_list["MAS{}_MUXA".format(i)] + self.INST_CAL_MUX_BIT
            self.index_list["MAS{}_MUXB".format(i)] = self.index_list["MAS{}_READB".format(i)] + self.MAS_MEM_ADDR_BITS
            self.index_list["MAS{}_ISSUB".format(i)] = self.index_list["MAS{}_MUXB".format(i)] + self.INST_CAL_MUX_BIT
            self.index_list["MAS{}_VAL".format(i)] = self.index_list["MAS{}_ISSUB".format(i)] + self.INST_MAS_ISSUB_BIT
            self.index_list["MAS{}_WRITE".format(i)] = self.index_list["MAS{}_VAL".format(i)] + self.INST_MM_MAS_VAL_BIT
            self.index_list["MAS{}_WE".format(i)] = self.index_list["MAS{}_WRITE".format(i)] + self.MAS_MEM_ADDR_BITS
            cnt = self.index_list["MAS{}_WE".format(i)] + self.INST_WRITE_EN_BIT

        self.index_list["MAIN_READA"] = cnt
        self.index_list["MAIN_READB"] = self.index_list["MAIN_READA"] + self.MAIN_MEM_ADDR_BITS
        self.index_list["MAIN_WRITE"] = self.index_list["MAIN_READB"] + self.MAIN_MEM_ADDR_BITS
        self.index_list["MAIN_WE"] = self.index_list["MAIN_WRITE"] + self.MAIN_MEM_ADDR_BITS
        self.index_list["MAIN_WRITE_MUX"] = self.index_list["MAIN_WE"] + self.INST_WRITE_EN_BIT
        self.index_list["MAIN_READ_MASKA"] = self.index_list["MAIN_WRITE_MUX"] + self.INST_WRITE_MUX_BIT
        self.index_list["MAIN_READ_MASKB"] = self.index_list["MAIN_READ_MASKA"] + self.INST_ADDR_MASK_BIT
        self.index_list["MAIN_WRITE_MASK"] = self.index_list["MAIN_READ_MASKB"] + self.INST_ADDR_MASK_BIT
        self.index_list["CONDKEY0"] = self.index_list["MAIN_WRITE_MASK"] + self.INST_ADDR_MASK_BIT
        self.index_list["CONDKEY1"] = self.index_list["CONDKEY0"] + 1
        self.index_list["INST_CONT"] = self.index_list["CONDKEY1"] + 1
        self.index_list["INST_END"] = self.index_list["INST_CONT"] + 1

        self.alu_inst_bits = self.index_list["MAIN_READ_MASKA"]
        self.inst_bits = self.index_list["INST_END"] + 1
        self.inst_bytes = self.inst_bits // 4 + (0 if self.inst_bits % 4 == 0 else 1)

    def writeHeaderCoreVH(self, output_file:str):
        f = open(output_file, 'w')
        f.write("// ALU MM Memory\n")
        f.write("`define ALU_MM_MEM_SIZE\t\t{}\n".format(2**self.MM_MEM_ADDR_BITS))
        f.write("`define ALU_MM_MEM_ADDR_BITS\t{}\n\n".format(self.MM_MEM_ADDR_BITS))

        f.write("// ALU MAS Memory\n")
        f.write("`define ALU_MAS_MEM_SIZE\t\t{}\n".format(2**self.MAS_MEM_ADDR_BITS))
        f.write("`define ALU_MAS_MEM_ADDR_BITS\t{}\n\n".format(self.MAS_MEM_ADDR_BITS))

        f.write("// ALU MAIN Memory\n")
        f.write("`define ALU_MAIN_MEM_SIZE\t\t{}\n".format(2**self.MAIN_MEM_ADDR_BITS))
        f.write("`define ALU_MAIN_MEM_ADDR_BITS\t{}\n\n".format(self.MAIN_MEM_ADDR_BITS))

        f.write("// ===================================================================================\n")
        f.write("`define INST_CAL_MUX_BIT\t\t{}\n".format(self.INST_CAL_MUX_BIT))
        f.write("`define INST_MAIN_MEM_MUX_BIT\t{}\n".format(self.INST_WRITE_MUX_BIT))
        f.write("`define INST_ADDR_MASK_BIT\t\t{}\n".format(self.INST_ADDR_MASK_BIT))
        f.write("`define INST_MM_MAS_VAL_BIT\t\t{}\n".format(self.INST_MM_MAS_VAL_BIT))
        f.write("`define INST_MAS_ISSUB_BIT\t\t{}\n".format(self.INST_MAS_ISSUB_BIT))
        f.write("`define INST_WRITE_EN_BIT\t\t{}\n".format(self.INST_WRITE_EN_BIT))
        f.write("`define INST_CONDKEY_BIT\t\t2\n\n")

        f.write("// ALU Instructions Index\n")
        for key, value in self.index_list.items():
            if "CONDKEY" in key:
                continue
            f.write("`define INDEX_{}\t\t{}\n".format(key, value))
        f.write("\n`define INDEX_CONDKEY\t\t\t{}\n".format(self.index_list["CONDKEY0"]))
        f.write("\n`define ALU_INST_BITS\t\t\t{}\n".format(self.alu_inst_bits))
        f.write("`define INST_BITS\t\t\t\t{}\n".format(self.inst_bits))
        f.close()

    def convertClass2Inst(self, instList: list[ALUInstruction]):
        hexInstList = []
        for inst in instList:
            tmp_hexinst = 0
            for key, value in inst.inst_dict.items():
                tmp_hexinst |= value << self.index_list[key]
                # print(key, self.bit_index_list[key])
            hexInstList.append(tmp_hexinst)
        return hexInstList


def writeABEALU(MMnum: int, MASnum: int, filename: str):
    f_output = open(filename, "w")
    f_mainmemory = open("./verilog_template/mainmemory_define.txt", "r")
    f_output.write(f_mainmemory.read())
    f_mainmemory.close()

    f_output.write("\n\n\t// CAL_MUX_MODE\n")
    for i in range(MMnum):
        f_output.write("\tlocalparam mux_MM{}_MEM = `INST_CAL_MUX_BIT'd{};\n".format(i, i*3))
        f_output.write("\tlocalparam mux_MM{}_SC = `INST_CAL_MUX_BIT'd{};\n".format(i, i*3 + 1))
        f_output.write("\tlocalparam mux_MM{}_REG = `INST_CAL_MUX_BIT'd{};\n".format(i, i*3 + 2))
    for i in range(MASnum):
        f_output.write("\tlocalparam mux_MAS{}_MEM = `INST_CAL_MUX_BIT'd{};\n".format(i, i*3 + MMnum*3))
        f_output.write("\tlocalparam mux_MAS{}_SC = `INST_CAL_MUX_BIT'd{};\n".format(i, i*3 + 1 + MMnum*3))
        f_output.write("\tlocalparam mux_MAS{}_REG = `INST_CAL_MUX_BIT'd{};\n".format(i, i*3 + 2 + MMnum*3))
    f_output.write("\tlocalparam mux_MAIN_MEM = `INST_CAL_MUX_BIT'd{};\n".format(MASnum*3 + MMnum*3))

    f_output.write("\n\n\t// MAIN_MEM_INPUT_MODE\n")
    for i in range(MMnum):
        f_output.write("\tlocalparam mux_MAIN_MM{} = `INST_MAIN_MEM_MUX_BIT'd{};\n".format(i, i))
    for i in range(MASnum):
        f_output.write("\tlocalparam mux_MAIN_MAS{} = `INST_MAIN_MEM_MUX_BIT'd{};\n".format(i, i+MMnum))
    
    f_output.write("\tassign MAIN_MEM_din = ALU_din_en_pipe == 1'b1 ? ALU_din_reg\n")
    for i in range(MMnum):
        f_output.write("\t\t\t: (Main_MEM_MUX == mux_MAIN_MM{0} ? MM{0}_dout\n".format(i))
    for i in range(MASnum):
        f_output.write("\t\t\t: (Main_MEM_MUX == mux_MAIN_MAS{0} ? MAS{0}_dout\n".format(i))
    f_output.write("\t\t\t: 0 {close_bracket};\n".format(close_bracket=")"*(MMnum+MASnum)))

    f_mm = open("./verilog_template/MM_define.txt", "r")
    mm_template = f_mm.read()
    for i in range(MMnum):
        f_output.write(mm_template.format(index=i))
        for c_i in range(2):
            c = chr(97+c_i)
            f_output.write("\tassign MM{index}_din{alphabet} = \n".format(index=i, alphabet=c))
            for j in range(MMnum):
                f_output.write("\t\t\t\t\tMM{index}_mux{alphabet} == mux_MM{mux_index}_MEM ? MM{mux_index}_MEM_dout{alphabet}\n".format(index=i, mux_index=j, alphabet=c))
                f_output.write("\t\t\t\t\t : (MM{index}_mux{alphabet} == mux_MM{mux_index}_SC ? MM{mux_index}_dout\n".format(index=i, mux_index=j, alphabet=c))
                f_output.write("\t\t\t\t\t : (MM{index}_mux{alphabet} == mux_MM{mux_index}_REG ? MM{mux_index}_dout_reg\n".format(index=i, mux_index=j, alphabet=c))
            for j in range(MASnum):
                f_output.write("\t\t\t\t\t : (MM{index}_mux{alphabet} == mux_MAS{mux_index}_MEM ? MAS{mux_index}_MEM_dout{alphabet}\n".format(index=i, mux_index=j, alphabet=c))
                f_output.write("\t\t\t\t\t : (MM{index}_mux{alphabet} == mux_MAS{mux_index}_SC ? MAS{mux_index}_dout\n".format(index=i, mux_index=j, alphabet=c))
                f_output.write("\t\t\t\t\t : (MM{index}_mux{alphabet} == mux_MAS{mux_index}_REG ? MAS{mux_index}_dout_reg\n".format(index=i, mux_index=j, alphabet=c))
            f_output.write("\t\t\t\t\t: MAIN_MEM_dout{alphabet} {close_bracket};\n\n".format(index=i, alphabet=c, close_bracket=")"*(MMnum*3+MASnum*3-1)))
        
    f_mm.close()

    f_mas = open("./verilog_template/MAS_define.txt", "r")
    mas_template = f_mas.read()
    for i in range(MASnum):
        f_output.write(mas_template.format(index=i))
        for c_i in range(2):
            c = chr(97+c_i)
            f_output.write("\tassign MAS{index}_din{alphabet} = \n".format(index=i, alphabet=c))
            for j in range(MMnum):
                f_output.write("\t\t\t\t\tMAS{index}_mux{alphabet} == mux_MM{mux_index}_MEM ? MM{mux_index}_MEM_dout{alphabet}\n".format(index=i, mux_index=j, alphabet=c))
                f_output.write("\t\t\t\t\t : (MAS{index}_mux{alphabet} == mux_MM{mux_index}_SC ? MM{mux_index}_dout\n".format(index=i, mux_index=j, alphabet=c))
                f_output.write("\t\t\t\t\t : (MAS{index}_mux{alphabet} == mux_MM{mux_index}_REG ? MM{mux_index}_dout_reg\n".format(index=i, mux_index=j, alphabet=c))
            for j in range(MASnum):
                f_output.write("\t\t\t\t\t : (MAS{index}_mux{alphabet} == mux_MAS{mux_index}_MEM ? MAS{mux_index}_MEM_dout{alphabet}\n".format(index=i, mux_index=j, alphabet=c))
                f_output.write("\t\t\t\t\t : (MAS{index}_mux{alphabet} == mux_MAS{mux_index}_SC ? MAS{mux_index}_dout\n".format(index=i, mux_index=j, alphabet=c))
                f_output.write("\t\t\t\t\t : (MAS{index}_mux{alphabet} == mux_MAS{mux_index}_REG ? MAS{mux_index}_dout_reg\n".format(index=i, mux_index=j, alphabet=c))
            f_output.write("\t\t\t\t\t: MAIN_MEM_dout{alphabet} {close_bracket};\n\n".format(index=i, alphabet=c, close_bracket=")"*(MMnum*3+MASnum*3-1)))
    f_mas.close()

    f_output.write("\t// Instructions assignment\n")
    f_output.write("\treg [`ALU_INST_BITS-1:0] INST2;\n")
    f_output.write("\talways @ (posedge clk or posedge rst) begin\n")
    f_output.write("\t\tif (rst) begin\n")
    f_output.write("\t\t\tINST2 <= 'b0;\n")
    for i in range(MMnum):
        f_output.write("\t\t\tMM{}_dout_reg <= 'b0;\n".format(i))
    for i in range(MASnum):
        f_output.write("\t\t\tMAS{}_dout_reg <= 'b0;\n".format(i))
    f_output.write("\t\tend else begin\n")
    f_output.write("\t\t\tINST2 <= INST1;\n")
    for i in range(MMnum):
        f_output.write("\t\t\tMM{0}_dout_reg <= MM{0}_dout;\n".format(i))
    for i in range(MASnum):
        f_output.write("\t\t\tMAS{0}_dout_reg <= MAS{0}_dout;\n".format(i))
    f_output.write("\t\tend\n")
    f_output.write("\tend\n\n")

    f_output.write("endmodule\n")

    f_output.close()



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
    inst_list[1].CONDKEY0 = 1
    inst_list[2].DRAM_addra = 1
    inst_list[2].set_mem_write("MUL", 1)
    inst_list[2].wMUXA = 1
    inst_list[3].set_mem_write("MUL", 4)
    inst_list[3].wMUXA = 1
    inst_list[4].set_mem_write("MUL", 5)
    inst_list[4].wMUXA = 1
    
    inst_hex_list = convertClass2Inst(inst_list)
    return inst_hex_list


def set_Fpinv_preprocess_inst(mul_stage: int):
    inst_list: list[ALUInstruction] = []
    inst_list.append(new_inst(Fpinv_preprocess_insts[0]))
    for i in range(mul_stage-1):
        inst_list.append(new_inst([0 for j in range(len(Fpinv_preprocess_insts[0]))]))
    inst_list.append(new_inst(Fpinv_preprocess_insts[1]))
    inst_list[-3].CONDKEY1 = 1
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
    inst_list[-5].INST_CONT = 1
    inst_list[-3].CONDKEY1 = 1
    inst_list[-3].CONDKEY0 = 1
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
        f.write("`define CAL_MUX_BIT {}\n\n".format(alu_ram_index.cal_MUX_bits))

        f.write("`define INDEX_READA {}\n".format(alu_ram_index.bit_index_list["REGF_READA"]))
        f.write("`define INDEX_READB {}\n".format(alu_ram_index.bit_index_list["REGF_READB"]))
        f.write("`define INDEX_READC {}\n".format(alu_ram_index.bit_index_list["REGF_raddrc"]))
        f.write("`define INDEX_READD {}\n".format(alu_ram_index.bit_index_list["REGF_raddrd"]))
        f.write("`define INDEX_ISSUB {}\n".format(alu_ram_index.bit_index_list["ISSUB"]))
        f.write("`define INDEX_MMVAL {}\n".format(alu_ram_index.bit_index_list["MM_VAL"]))
        f.write("`define INDEX_MASVAL {}\n".format(alu_ram_index.bit_index_list["MAS_VAL"]))
        f.write("`define INDEX_WRITEA {}\n".format(alu_ram_index.bit_index_list["REGF_WRITEa"]))
        f.write("`define INDEX_WRITEB {}\n".format(alu_ram_index.bit_index_list["REGF_WRITEb"]))

    with open("{}/header_core.vh".format(target_dir), "w") as f:
        f.write("`define INST_BITS {}\n".format(alu_ram_index.inst_bits))
        f.write("`define MEM_SIZE {}\n".format(inst_num))
        f.write("`define INST_RAM_addr_BITS {}\n".format(7))
        f.write("`define CMDADDR_repeat_BITS {}\n".format(9))
        f.write("`define OUTBRAM_ADDR_BITS {}\n\n".format(alu_ram_index.outbram_addr_bits))

        f.write("`define INDEX_CONDKEY {}\n".format(alu_ram_index.bit_index_list["CONDKEY0"]))
        f.write("`define INDEX_CONINST {}\n".format(alu_ram_index.bit_index_list["INST_CONT"]))
        f.write("`define INDEX_ENDINST {}\n".format(alu_ram_index.bit_index_list["INST_END"]))
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
    
