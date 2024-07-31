from inst_lib import set_init_inst, ALURAMIndex

alu_ram_index = ALURAMIndex(18, 3)
init_inst_list = set_init_inst(alu_ram_index)
print(alu_ram_index.inst_bits)
with open("test.txt", "w") as f:
    for init_inst in init_inst_list:
        f.write(format(init_inst, f'0{alu_ram_index.inst_bits}b')+"\n")