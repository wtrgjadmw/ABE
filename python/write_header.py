def write_header(target_dir: str, max_addr: int, cal_mux: int):
    addr_bits = max_addr.bit_length()
    cal_mux_bits = cal_mux.bit_length()
    mm_inst_bits = addr_bits + cal_mux_bits + 1
    add_inst_bits = addr_bits + cal_mux_bits
    alu_inst_bits = mm_inst_bits * 2 + add_inst_bits * 2 + addr_bits * 2 + 8

    with open("{}/header_ALU.vh".format(target_dir), "w") as f:
        f.write("`define ALU_INST_BITS {}\n".format(alu_inst_bits))
        f.write("`define ADDR_BITS {}\n".format(addr_bits))
        f.write("`define CAL_MUX_BIT {}\n\n".format(cal_mux_bits))

        f.write("`define MM_INST_BITS {}\n".format(mm_inst_bits))
        f.write("`define ADD_INST_BITS {}\n\n".format(add_inst_bits))

        f.write("`define INDEX_READA {}\n".format(0))
        f.write("`define INDEX_READB {}\n".format(mm_inst_bits))
        f.write("`define INDEX_READC {}\n".format(mm_inst_bits * 2))
        f.write("`define INDEX_READD {}\n".format(mm_inst_bits * 2 + add_inst_bits))
        f.write("`define INDEX_ISSUB {}\n".format(mm_inst_bits * 2 + add_inst_bits * 2))
        f.write("`define INDEX_MMVAL {}\n".format(mm_inst_bits * 2 + add_inst_bits * 2 + 1))
        f.write("`define INDEX_MASVAL {}\n".format(mm_inst_bits * 2 + add_inst_bits * 2 + 2))
        f.write("`define INDEX_WRITEA {}\n".format(mm_inst_bits * 2 + add_inst_bits * 2 + 3))
        f.write("`define INDEX_WRITEB {}\n".format(mm_inst_bits * 2 + add_inst_bits * 2 + addr_bits + 6))

    outbram_addr_bits = 4
    with open("{}/header_core.vh".format(target_dir), "w") as f:
        f.write("`define INST_BITS {}\n".format(alu_inst_bits + 14))
        f.write("`define INST_RAM_addr_BITS {}\n".format(7))
        f.write("`define CMDADDR_repeat_BITS {}\n".format(9))
        f.write("`define OUTBRAM_ADDR_BITS {}\n\n".format(outbram_addr_bits))

        f.write("`define INDEX_CONDKEY {}\n".format(alu_inst_bits))
        f.write("`define INDEX_CONINST {}\n".format(alu_inst_bits + 2))
        f.write("`define INDEX_ENDINST {}\n".format(alu_inst_bits + 3))
        f.write("`define INDEX_DRAMA {}\n".format(alu_inst_bits + 4))
        f.write("`define INDEX_DRAMB {}\n".format(alu_inst_bits + outbram_addr_bits + 5))


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
