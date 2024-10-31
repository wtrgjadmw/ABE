from field import Fp
verilog_sim_result = open("/mnt/rose/usr5/masada/nakayama/bls_signature/testbench/sage_verilog_sim_result.txt", "r")
ref_result = open("/mnt/rose/usr5/masada/nakayama/bls_signature/testbench/sage_result_100000.txt", "r")
lines = verilog_sim_result.readlines()
ref_lines = ref_result.readlines()
sim_index = 0
ref_index = 0
while sim_index + 2 < len(lines):
    x = Fp(int(lines[sim_index]))
    y = Fp(int(lines[sim_index + 1]))
    z = Fp(int(lines[sim_index + 2]))
    z2 = z ** 2
    z3 = z ** 3
    aff_x = x / z2
    aff_y = y / z3
    aff_x.Mont_change()
    aff_y.Mont_change()
    sim_resultx = aff_x.value
    sim_resulty = aff_y.value
    ref_x = int(ref_lines[ref_index])
    ref_y = int(ref_lines[ref_index + 1])
    print(sim_resultx)
    #print(sim_resulty)
    print(ref_x)
    #print(ref_y)
    assert sim_resultx == ref_x, "sim_index:" + str(sim_index)
    assert sim_resulty == ref_y, "sim_index:" + str(sim_index)
    print(sim_index // 3, ": ok")
    sim_index += 3
    ref_index += 2
