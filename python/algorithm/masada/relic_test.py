from field import Fp
verilog_sim_result = open("/mnt/rose/usr5/masada/nakayama/PairingBLSV0_done_for_others/v/sim_result0.txt", "r")
ref_result = open("pairing_output3.txt", "r")
lines = verilog_sim_result.readlines()
ref_lines = ref_result.readlines()
sim_index = 0
ref_index = 0
while sim_index + 11 < len(lines):
    verilog_sim_values = [int(lines[sim_index + i], 16) for i in range(12)]
    ref_values = [int(ref_lines[ref_index + i], 16) for i in range(12)]
    #print(lines[sim_index])
    #print(ref_lines[ref_index])
    #print(verilog_sim_values)
    #print(ref_values)
    for i in range(12):
        print(lines[sim_index + i])
        print(ref_lines[ref_index + i])
        assert verilog_sim_values[i] == ref_values[i]
    print(sim_index // 12, ": ok")
    sim_index += 12
    ref_index += 12
    #if sim_index > 24:
    #     break
