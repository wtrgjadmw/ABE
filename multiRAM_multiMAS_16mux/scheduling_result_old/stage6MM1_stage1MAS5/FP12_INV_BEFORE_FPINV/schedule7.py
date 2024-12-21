from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 168
	S = Scenario("schedule7", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 0
	c_aa_t3_t1_in += MM_in[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 0
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 0
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 1
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=6, delay_cost=1)
	S += c_aa_t3_t1 >= 1
	c_aa_t3_t1 += MM[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 1
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=1, delay_cost=1)
	S += c_bb_t3_t3 >= 1
	c_bb_t3_t3 += MAS[3]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 1
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=1, delay_cost=1)
	S += c_cc_a1_0 >= 1
	c_cc_a1_0 += MAS[4]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=1, delay_cost=1)
	S += c_cc_a1_1 >= 1
	c_cc_a1_1 += MAS[0]

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	S += c_cc_t10 >= 1
	c_cc_t10 += MAS[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	S += c_cc_t3_t3 >= 1
	c_cc_t3_t3 += MAS[2]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	S += c_aa_a1_0 >= 2
	c_aa_a1_0 += MAS[4]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	S += c_aa_a1_1 >= 2
	c_aa_a1_1 += MAS[3]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	S += c_bb_a1_0 >= 2
	c_bb_a1_0 += MAS[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 2
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 2
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=6, delay_cost=1)
	S += c_bb_t3_t0 >= 2
	c_bb_t3_t0 += MM[0]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 2
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=1, delay_cost=1)
	S += c_bb_t3_t2 >= 2
	c_bb_t3_t2 += MAS[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	S += c_cc_t3_t2 >= 2
	c_cc_t3_t2 += MAS[2]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 3
	c_aa_t3_t0_in += MM_in[0]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	S += c_ab_t0_t2 >= 3
	c_ab_t0_t2 += MAS[4]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	S += c_ab_t0_t3 >= 3
	c_ab_t0_t3 += MAS[1]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	S += c_bb_a1_1 >= 3
	c_bb_a1_1 += MAS[3]

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	S += c_bb_t10 >= 3
	c_bb_t10 += MAS[2]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=6, delay_cost=1)
	S += c_bb_t3_t1 >= 3
	c_bb_t3_t1 += MM[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 3
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 3
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=1, delay_cost=1)
	S += c_cc_t11 >= 3
	c_cc_t11 += MAS[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 4
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	S += c_aa_t10 >= 4
	c_aa_t10 += MAS[4]

	c_aa_t11 = S.Task('c_aa_t11', length=1, delay_cost=1)
	S += c_aa_t11 >= 4
	c_aa_t11 += MAS[3]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=6, delay_cost=1)
	S += c_aa_t3_t0 >= 4
	c_aa_t3_t0 += MM[0]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	S += c_aa_t3_t2 >= 4
	c_aa_t3_t2 += MAS[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	S += c_aa_t3_t3 >= 4
	c_aa_t3_t3 += MAS[2]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 4
	c_ab_t0_t0_in += MM_in[0]

	c_bb_t11 = S.Task('c_bb_t11', length=1, delay_cost=1)
	S += c_bb_t11 >= 4
	c_bb_t11 += MAS[1]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 4
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=6, delay_cost=1)
	S += c_ab_t0_t0 >= 5
	c_ab_t0_t0 += MM[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 5
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t30 = S.Task('c_ab_t30', length=1, delay_cost=1)
	S += c_ab_t30 >= 5
	c_ab_t30 += MAS[0]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=1, delay_cost=1)
	S += c_ac_t1_t2 >= 5
	c_ac_t1_t2 += MAS[1]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 5
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=1, delay_cost=1)
	S += c_bc_t0_t3 >= 5
	c_bc_t0_t3 += MAS[2]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=1, delay_cost=1)
	S += c_bc_t1_t2 >= 5
	c_bc_t1_t2 += MAS[3]

	c_bc_t31 = S.Task('c_bc_t31', length=1, delay_cost=1)
	S += c_bc_t31 >= 5
	c_bc_t31 += MAS[4]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 5
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 6
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=6, delay_cost=1)
	S += c_ab_t0_t1 >= 6
	c_ab_t0_t1 += MM[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 6
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=1, delay_cost=1)
	S += c_ab_t1_t2 >= 6
	c_ab_t1_t2 += MAS[4]

	c_ab_t21 = S.Task('c_ab_t21', length=1, delay_cost=1)
	S += c_ab_t21 >= 6
	c_ab_t21 += MAS[0]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=1, delay_cost=1)
	S += c_bc_t0_t2 >= 6
	c_bc_t0_t2 += MAS[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=1, delay_cost=1)
	S += c_bc_t1_t3 >= 6
	c_bc_t1_t3 += MAS[2]

	c_bc_t21 = S.Task('c_bc_t21', length=1, delay_cost=1)
	S += c_bc_t21 >= 6
	c_bc_t21 += MAS[3]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 6
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=6, delay_cost=1)
	S += c_ab_t1_t0 >= 7
	c_ab_t1_t0 += MM[0]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=1, delay_cost=1)
	S += c_ab_t1_t3 >= 7
	c_ab_t1_t3 += MAS[3]

	c_ab_t20 = S.Task('c_ab_t20', length=1, delay_cost=1)
	S += c_ab_t20 >= 7
	c_ab_t20 += MAS[1]

	c_ab_t31 = S.Task('c_ab_t31', length=1, delay_cost=1)
	S += c_ab_t31 >= 7
	c_ab_t31 += MAS[4]

	c_ac_t30 = S.Task('c_ac_t30', length=1, delay_cost=1)
	S += c_ac_t30 >= 7
	c_ac_t30 += MAS[0]

	c_bc_t20 = S.Task('c_bc_t20', length=1, delay_cost=1)
	S += c_bc_t20 >= 7
	c_bc_t20 += MAS[2]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 7
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 7
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 7
	c_cc_t3_t1_in += MM_in[0]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=1, delay_cost=1)
	S += c_ac_t0_t2 >= 8
	c_ac_t0_t2 += MAS[3]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=1, delay_cost=1)
	S += c_ac_t0_t3 >= 8
	c_ac_t0_t3 += MAS[0]

	c_ac_t20 = S.Task('c_ac_t20', length=1, delay_cost=1)
	S += c_ac_t20 >= 8
	c_ac_t20 += MAS[4]

	c_ac_t31 = S.Task('c_ac_t31', length=1, delay_cost=1)
	S += c_ac_t31 >= 8
	c_ac_t31 += MAS[2]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 8
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 8
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bc_t30 = S.Task('c_bc_t30', length=1, delay_cost=1)
	S += c_bc_t30 >= 8
	c_bc_t30 += MAS[1]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 8
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=6, delay_cost=1)
	S += c_cc_t3_t1 >= 8
	c_cc_t3_t1 += MM[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 9
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 9
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 9
	c_ab_t1_t1_in += MM_in[0]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=1, delay_cost=1)
	S += c_ac_t1_t3 >= 9
	c_ac_t1_t3 += MAS[2]

	c_ac_t21 = S.Task('c_ac_t21', length=1, delay_cost=1)
	S += c_ac_t21 >= 9
	c_ac_t21 += MAS[0]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=6, delay_cost=1)
	S += c_cc_t3_t0 >= 9
	c_cc_t3_t0 += MM[0]

	c_paa_t30 = S.Task('c_paa_t30', length=1, delay_cost=1)
	S += c_paa_t30 >= 9
	c_paa_t30 += MAS[1]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=1, delay_cost=1)
	S += c_pbc_t1_t3 >= 9
	c_pbc_t1_t3 += MAS[4]

	c_pcb_t31 = S.Task('c_pcb_t31', length=1, delay_cost=1)
	S += c_pcb_t31 >= 9
	c_pcb_t31 += MAS[3]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 10
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 10
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=6, delay_cost=1)
	S += c_ab_t1_t1 >= 10
	c_ab_t1_t1 += MM[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 10
	c_ac_t1_t0_in += MM_in[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 10
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 10
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=1, delay_cost=1)
	S += c_paa_t0_t3 >= 10
	c_paa_t0_t3 += MAS[2]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=1, delay_cost=1)
	S += c_paa_t1_t3 >= 10
	c_paa_t1_t3 += MAS[3]

	c_pbc_t31 = S.Task('c_pbc_t31', length=1, delay_cost=1)
	S += c_pbc_t31 >= 10
	c_pbc_t31 += MAS[1]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=1, delay_cost=1)
	S += c_pcb_t1_t3 >= 10
	c_pcb_t1_t3 += MAS[0]

	c_pcb_t30 = S.Task('c_pcb_t30', length=1, delay_cost=1)
	S += c_pcb_t30 >= 10
	c_pcb_t30 += MAS[4]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=1, delay_cost=1)
	S += c_aa_t3_t5 >= 11
	c_aa_t3_t5 += MAS[4]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 11
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 11
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 11
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=6, delay_cost=1)
	S += c_ac_t1_t0 >= 11
	c_ac_t1_t0 += MM[0]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 11
	c_ac_t4_t2_mem0 += MAS_MEM[8]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 11
	c_ac_t4_t2_mem1 += MAS_MEM[1]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 11
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 11
	c_ac_t4_t3_mem1 += MAS_MEM[5]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 11
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 11
	c_bc_t4_t2_mem0 += MAS_MEM[4]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 11
	c_bc_t4_t2_mem1 += MAS_MEM[7]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 11
	c_bc_t4_t3_mem0 += MAS_MEM[2]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 11
	c_bc_t4_t3_mem1 += MAS_MEM[9]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 11
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_paa_t31 = S.Task('c_paa_t31', length=1, delay_cost=1)
	S += c_paa_t31 >= 11
	c_paa_t31 += MAS[0]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=1, delay_cost=1)
	S += c_pbc_t0_t3 >= 11
	c_pbc_t0_t3 += MAS[2]

	c_pbc_t30 = S.Task('c_pbc_t30', length=1, delay_cost=1)
	S += c_pbc_t30 >= 11
	c_pbc_t30 += MAS[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=1, delay_cost=1)
	S += c_pcb_t0_t3 >= 11
	c_pcb_t0_t3 += MAS[3]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 12
	c_aa_t2_t3_mem0 += MAS_MEM[8]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 12
	c_aa_t2_t3_mem1 += MAS_MEM[7]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 12
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 12
	c_aa_t30_mem1 += MM_MEM[1]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=1, delay_cost=1)
	S += c_ab_t0_t5 >= 12
	c_ab_t0_t5 += MAS[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 12
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 12
	c_ab_t4_t2_mem0 += MAS_MEM[2]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 12
	c_ab_t4_t2_mem1 += MAS_MEM[1]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 12
	c_ab_t4_t3_mem0 += MAS_MEM[0]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 12
	c_ab_t4_t3_mem1 += MAS_MEM[9]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=6, delay_cost=1)
	S += c_ac_t0_t1 >= 12
	c_ac_t0_t1 += MM[0]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=1, delay_cost=1)
	S += c_ac_t4_t2 >= 12
	c_ac_t4_t2 += MAS[3]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=1, delay_cost=1)
	S += c_ac_t4_t3 >= 12
	c_ac_t4_t3 += MAS[2]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 12
	c_bb_t2_t3_mem0 += MAS_MEM[4]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 12
	c_bb_t2_t3_mem1 += MAS_MEM[3]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 12
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=1, delay_cost=1)
	S += c_bc_t4_t2 >= 12
	c_bc_t4_t2 += MAS[1]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=1, delay_cost=1)
	S += c_bc_t4_t3 >= 12
	c_bc_t4_t3 += MAS[4]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 12
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 13
	c_aa_t00_mem1 += MAS_MEM[9]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=1, delay_cost=1)
	S += c_aa_t2_t3 >= 13
	c_aa_t2_t3 += MAS[1]

	c_aa_t30 = S.Task('c_aa_t30', length=1, delay_cost=1)
	S += c_aa_t30 >= 13
	c_aa_t30 += MAS[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 13
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 13
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 13
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 13
	c_ab_t00_mem1 += MM_MEM[1]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=1, delay_cost=1)
	S += c_ab_t4_t2 >= 13
	c_ab_t4_t2 += MAS[3]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=1, delay_cost=1)
	S += c_ab_t4_t3 >= 13
	c_ab_t4_t3 += MAS[2]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 13
	c_ac_t0_t0_in += MM_in[0]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 13
	c_bb_t00_mem1 += MAS_MEM[1]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=1, delay_cost=1)
	S += c_bb_t2_t3 >= 13
	c_bb_t2_t3 += MAS[4]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=6, delay_cost=1)
	S += c_bc_t0_t0 >= 13
	c_bc_t0_t0 += MM[0]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 13
	c_pbc_t4_t3_mem0 += MAS_MEM[2]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 13
	c_pbc_t4_t3_mem1 += MAS_MEM[3]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 13
	c_pcb_t4_t3_mem0 += MAS_MEM[8]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 13
	c_pcb_t4_t3_mem1 += MAS_MEM[7]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 14
	c_aa10_mem0 += MAS_MEM[0]

	c_aa_t00 = S.Task('c_aa_t00', length=1, delay_cost=1)
	S += c_aa_t00 >= 14
	c_aa_t00 += MAS[2]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 14
	c_aa_t01_mem1 += MAS_MEM[7]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 14
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t00 = S.Task('c_ab_t00', length=1, delay_cost=1)
	S += c_ab_t00 >= 14
	c_ab_t00 += MAS[3]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=6, delay_cost=1)
	S += c_ac_t0_t0 >= 14
	c_ac_t0_t0 += MM[0]

	c_bb_t00 = S.Task('c_bb_t00', length=1, delay_cost=1)
	S += c_bb_t00 >= 14
	c_bb_t00 += MAS[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 14
	c_bc_t0_t1_in += MM_in[0]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 14
	c_cc_t00_mem1 += MAS_MEM[9]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 14
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 14
	c_cc_t2_t3_mem0 += MAS_MEM[2]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 14
	c_cc_t2_t3_mem1 += MAS_MEM[1]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 14
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 14
	c_cc_t30_mem1 += MM_MEM[1]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=1, delay_cost=1)
	S += c_pbc_t4_t3 >= 14
	c_pbc_t4_t3 += MAS[4]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=1, delay_cost=1)
	S += c_pcb_t4_t3 >= 14
	c_pcb_t4_t3 += MAS[1]

	c_aa10 = S.Task('c_aa10', length=1, delay_cost=1)
	S += c_aa10 >= 15
	c_aa10 += MAS[2]

	c_aa_t01 = S.Task('c_aa_t01', length=1, delay_cost=1)
	S += c_aa_t01 >= 15
	c_aa_t01 += MAS[0]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 15
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 15
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 15
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 15
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 15
	c_bb_t01_mem1 += MAS_MEM[7]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=6, delay_cost=1)
	S += c_bc_t0_t1 >= 15
	c_bc_t0_t1 += MM[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 15
	c_bc_t1_t0_in += MM_in[0]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 15
	c_cc10_mem0 += MAS_MEM[6]

	c_cc_t00 = S.Task('c_cc_t00', length=1, delay_cost=1)
	S += c_cc_t00 >= 15
	c_cc_t00 += MAS[1]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 15
	c_cc_t01_mem1 += MAS_MEM[1]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=1, delay_cost=1)
	S += c_cc_t2_t3 >= 15
	c_cc_t2_t3 += MAS[4]

	c_cc_t30 = S.Task('c_cc_t30', length=1, delay_cost=1)
	S += c_cc_t30 >= 15
	c_cc_t30 += MAS[3]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 16
	c_aa_t2_t2_mem0 += MAS_MEM[4]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 16
	c_aa_t2_t2_mem1 += MAS_MEM[1]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 16
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=1, delay_cost=1)
	S += c_ab_t1_t5 >= 16
	c_ab_t1_t5 += MAS[0]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 16
	c_ac_t1_t1_in += MM_in[0]

	c_bb_t01 = S.Task('c_bb_t01', length=1, delay_cost=1)
	S += c_bb_t01 >= 16
	c_bb_t01 += MAS[3]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 16
	c_bb_t2_t2_mem0 += MAS_MEM[0]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 16
	c_bb_t2_t2_mem1 += MAS_MEM[7]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 16
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 16
	c_bb_t30_mem1 += MM_MEM[1]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 16
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=6, delay_cost=1)
	S += c_bc_t1_t0 >= 16
	c_bc_t1_t0 += MM[0]

	c_cc10 = S.Task('c_cc10', length=1, delay_cost=1)
	S += c_cc10 >= 16
	c_cc10 += MAS[1]

	c_cc_t01 = S.Task('c_cc_t01', length=1, delay_cost=1)
	S += c_cc_t01 >= 16
	c_cc_t01 += MAS[4]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 16
	c_cc_t2_t2_mem0 += MAS_MEM[2]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 16
	c_cc_t2_t2_mem1 += MAS_MEM[9]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=1, delay_cost=1)
	S += c_aa_t2_t2 >= 17
	c_aa_t2_t2 += MAS[2]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 17
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 17
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 17
	c_ab_t10_mem1 += MM_MEM[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=6, delay_cost=1)
	S += c_ac_t1_t1 >= 17
	c_ac_t1_t1 += MM[0]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 17
	c_bb10_mem0 += MAS_MEM[0]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=1, delay_cost=1)
	S += c_bb_t2_t2 >= 17
	c_bb_t2_t2 += MAS[1]

	c_bb_t30 = S.Task('c_bb_t30', length=1, delay_cost=1)
	S += c_bb_t30 >= 17
	c_bb_t30 += MAS[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 17
	c_bc_t1_t1_in += MM_in[0]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=1, delay_cost=1)
	S += c_cc_t2_t2 >= 17
	c_cc_t2_t2 += MAS[3]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 17
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 17
	c_paa_t4_t3_mem0 += MAS_MEM[2]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 17
	c_paa_t4_t3_mem1 += MAS_MEM[1]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 18
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_ab_t10 = S.Task('c_ab_t10', length=1, delay_cost=1)
	S += c_ab_t10 >= 18
	c_ab_t10 += MAS[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 18
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 18
	c_ab_t4_t1_mem0 += MAS_MEM[0]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 18
	c_ab_t4_t1_mem1 += MAS_MEM[9]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 18
	c_ab_t50_mem0 += MAS_MEM[6]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 18
	c_ab_t50_mem1 += MAS_MEM[1]

	c_bb10 = S.Task('c_bb10', length=1, delay_cost=1)
	S += c_bb10 >= 18
	c_bb10 += MAS[1]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 18
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 18
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=6, delay_cost=1)
	S += c_bc_t1_t1 >= 18
	c_bc_t1_t1 += MM[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 18
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=1, delay_cost=1)
	S += c_paa_t4_t3 >= 18
	c_paa_t4_t3 += MAS[3]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 19
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 19
	c_aa_t3_t4_mem0 += MAS_MEM[0]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 19
	c_aa_t3_t4_mem1 += MAS_MEM[5]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 19
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=6, delay_cost=1)
	S += c_ab_t4_t1 >= 19
	c_ab_t4_t1 += MM[0]

	c_ab_t50 = S.Task('c_ab_t50', length=1, delay_cost=1)
	S += c_ab_t50 >= 19
	c_ab_t50 += MAS[2]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 19
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 19
	c_ac_t00_mem1 += MM_MEM[1]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 19
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=1, delay_cost=1)
	S += c_bb_t3_t5 >= 19
	c_bb_t3_t5 += MAS[4]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=6, delay_cost=1)
	S += c_aa_t3_t4 >= 20
	c_aa_t3_t4 += MM[0]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 20
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 20
	c_ab_t0_t4_mem0 += MAS_MEM[8]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 20
	c_ab_t0_t4_mem1 += MAS_MEM[3]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 20
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t00 = S.Task('c_ac_t00', length=1, delay_cost=1)
	S += c_ac_t00 >= 20
	c_ac_t00 += MAS[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 20
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 20
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 20
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=6, delay_cost=1)
	S += c_ab_t0_t4 >= 21
	c_ab_t0_t4 += MM[0]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 21
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 21
	c_ac_t0_t4_mem0 += MAS_MEM[6]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 21
	c_ac_t0_t4_mem1 += MAS_MEM[1]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 21
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 21
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 21
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 21
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=1, delay_cost=1)
	S += c_cc_t3_t5 >= 21
	c_cc_t3_t5 += MAS[2]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 22
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 22
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=6, delay_cost=1)
	S += c_ac_t0_t4 >= 22
	c_ac_t0_t4 += MM[0]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=1, delay_cost=1)
	S += c_ac_t0_t5 >= 22
	c_ac_t0_t5 += MAS[1]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 22
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 22
	c_ac_t10_mem1 += MM_MEM[1]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 22
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 22
	c_bc_t4_t1_mem0 += MAS_MEM[6]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 22
	c_bc_t4_t1_mem1 += MAS_MEM[9]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 23
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_ac_t10 = S.Task('c_ac_t10', length=1, delay_cost=1)
	S += c_ac_t10 >= 23
	c_ac_t10 += MAS[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 23
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 23
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 23
	c_ac_t50_mem0 += MAS_MEM[0]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 23
	c_ac_t50_mem1 += MAS_MEM[1]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 23
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 23
	c_bb_t3_t4_mem0 += MAS_MEM[2]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 23
	c_bb_t3_t4_mem1 += MAS_MEM[7]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=6, delay_cost=1)
	S += c_bc_t4_t1 >= 23
	c_bc_t4_t1 += MM[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 23
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 24
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 24
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=1, delay_cost=1)
	S += c_ac_t1_t5 >= 24
	c_ac_t1_t5 += MAS[3]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 24
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 24
	c_ac_t4_t0_mem0 += MAS_MEM[8]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 24
	c_ac_t4_t0_mem1 += MAS_MEM[1]

	c_ac_t50 = S.Task('c_ac_t50', length=1, delay_cost=1)
	S += c_ac_t50 >= 24
	c_ac_t50 += MAS[2]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=6, delay_cost=1)
	S += c_bb_t3_t4 >= 24
	c_bb_t3_t4 += MM[0]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 24
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 24
	c_bc_t10_mem1 += MM_MEM[1]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=6, delay_cost=1)
	S += c_ac_t4_t0 >= 25
	c_ac_t4_t0 += MM[0]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 25
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 25
	c_ac_t4_t1_mem0 += MAS_MEM[0]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 25
	c_ac_t4_t1_mem1 += MAS_MEM[5]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 25
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 25
	c_bc_t00_mem1 += MM_MEM[1]

	c_bc_t10 = S.Task('c_bc_t10', length=1, delay_cost=1)
	S += c_bc_t10 >= 25
	c_bc_t10 += MAS[1]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 25
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 25
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 26
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 26
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 26
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 26
	c_ac_t1_t4_mem0 += MAS_MEM[2]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 26
	c_ac_t1_t4_mem1 += MAS_MEM[5]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=6, delay_cost=1)
	S += c_ac_t4_t1 >= 26
	c_ac_t4_t1 += MM[0]

	c_bc_t00 = S.Task('c_bc_t00', length=1, delay_cost=1)
	S += c_bc_t00 >= 26
	c_bc_t00 += MAS[2]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 26
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 26
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 26
	c_bc_t50_mem0 += MAS_MEM[4]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 26
	c_bc_t50_mem1 += MAS_MEM[3]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 27
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=6, delay_cost=1)
	S += c_ac_t1_t4 >= 27
	c_ac_t1_t4 += MM[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 27
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 27
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 27
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=1, delay_cost=1)
	S += c_bc_t1_t5 >= 27
	c_bc_t1_t5 += MAS[2]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 27
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 27
	c_bc_t4_t0_mem0 += MAS_MEM[4]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 27
	c_bc_t4_t0_mem1 += MAS_MEM[3]

	c_bc_t50 = S.Task('c_bc_t50', length=1, delay_cost=1)
	S += c_bc_t50 >= 27
	c_bc_t50 += MAS[0]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 28
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 28
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 28
	c_ab_t4_t0_mem0 += MAS_MEM[2]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 28
	c_ab_t4_t0_mem1 += MAS_MEM[1]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 28
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 28
	c_ac_t01_mem1 += MAS_MEM[3]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=1, delay_cost=1)
	S += c_bc_t0_t5 >= 28
	c_bc_t0_t5 += MAS[4]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=6, delay_cost=1)
	S += c_bc_t4_t0 >= 28
	c_bc_t4_t0 += MM[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 28
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 29
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=6, delay_cost=1)
	S += c_ab_t4_t0 >= 29
	c_ab_t4_t0 += MM[0]

	c_ac_t01 = S.Task('c_ac_t01', length=1, delay_cost=1)
	S += c_ac_t01 >= 29
	c_ac_t01 += MAS[4]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 29
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 29
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 29
	c_bb_t31_mem1 += MAS_MEM[9]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 29
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 29
	c_cc_t3_t4_mem0 += MAS_MEM[4]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 29
	c_cc_t3_t4_mem1 += MAS_MEM[5]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 30
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 30
	c_aa_t31_mem1 += MAS_MEM[9]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 30
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 30
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t31 = S.Task('c_bb_t31', length=1, delay_cost=1)
	S += c_bb_t31 >= 30
	c_bb_t31 += MAS[4]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 30
	c_bb_t41_mem0 += MAS_MEM[8]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 30
	c_bb_t41_mem1 += MAS_MEM[1]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 30
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 30
	c_bc_t0_t4_mem0 += MAS_MEM[2]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 30
	c_bc_t0_t4_mem1 += MAS_MEM[5]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=6, delay_cost=1)
	S += c_cc_t3_t4 >= 30
	c_cc_t3_t4 += MM[0]

	c_aa_t31 = S.Task('c_aa_t31', length=1, delay_cost=1)
	S += c_aa_t31 >= 31
	c_aa_t31 += MAS[2]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 31
	c_aa_t40_mem0 += MAS_MEM[0]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 31
	c_aa_t40_mem1 += MAS_MEM[5]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 31
	c_aa_t41_mem0 += MAS_MEM[4]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 31
	c_aa_t41_mem1 += MAS_MEM[1]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 31
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 31
	c_ab_t1_t4_mem0 += MAS_MEM[8]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 31
	c_ab_t1_t4_mem1 += MAS_MEM[7]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 31
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 31
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 31
	c_ac_t40_mem1 += MM_MEM[1]

	c_bb_t41 = S.Task('c_bb_t41', length=1, delay_cost=1)
	S += c_bb_t41 >= 31
	c_bb_t41 += MAS[0]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=6, delay_cost=1)
	S += c_bc_t0_t4 >= 31
	c_bc_t0_t4 += MM[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 31
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 32
	c_aa11_mem0 += MAS_MEM[4]

	c_aa_t40 = S.Task('c_aa_t40', length=1, delay_cost=1)
	S += c_aa_t40 >= 32
	c_aa_t40 += MAS[2]

	c_aa_t41 = S.Task('c_aa_t41', length=1, delay_cost=1)
	S += c_aa_t41 >= 32
	c_aa_t41 += MAS[1]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=6, delay_cost=1)
	S += c_ab_t1_t4 >= 32
	c_ab_t1_t4 += MM[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 32
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 32
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 32
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 32
	c_ac_t11_mem1 += MAS_MEM[7]

	c_ac_t40 = S.Task('c_ac_t40', length=1, delay_cost=1)
	S += c_ac_t40 >= 32
	c_ac_t40 += MAS[0]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 32
	c_bb11_mem0 += MAS_MEM[8]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 32
	c_bb_t40_mem0 += MAS_MEM[0]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 32
	c_bb_t40_mem1 += MAS_MEM[9]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 32
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 32
	c_bc_t1_t4_mem0 += MAS_MEM[6]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 32
	c_bc_t1_t4_mem1 += MAS_MEM[5]

	c_aa11 = S.Task('c_aa11', length=1, delay_cost=1)
	S += c_aa11 >= 33
	c_aa11 += MAS[3]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 33
	c_ac10_mem0 += MAS_MEM[0]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 33
	c_ac10_mem1 += MAS_MEM[5]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 33
	c_ac_s01_mem0 += MAS_MEM[4]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 33
	c_ac_s01_mem1 += MAS_MEM[1]

	c_ac_t11 = S.Task('c_ac_t11', length=1, delay_cost=1)
	S += c_ac_t11 >= 33
	c_ac_t11 += MAS[2]

	c_bb11 = S.Task('c_bb11', length=1, delay_cost=1)
	S += c_bb11 >= 33
	c_bb11 += MAS[0]

	c_bb_t40 = S.Task('c_bb_t40', length=1, delay_cost=1)
	S += c_bb_t40 >= 33
	c_bb_t40 += MAS[1]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 33
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 33
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=6, delay_cost=1)
	S += c_bc_t1_t4 >= 33
	c_bc_t1_t4 += MM[0]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 33
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 33
	c_bc_t40_mem1 += MM_MEM[1]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 33
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 33
	c_cc_t2_t0_mem0 += MAS_MEM[2]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 33
	c_cc_t2_t0_mem1 += MAS_MEM[3]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 34
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 34
	c_ab_t01_mem1 += MAS_MEM[1]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 34
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 34
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 34
	c_ab_t4_t4_mem0 += MAS_MEM[6]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 34
	c_ab_t4_t4_mem1 += MAS_MEM[5]

	c_ac10 = S.Task('c_ac10', length=1, delay_cost=1)
	S += c_ac10 >= 34
	c_ac10 += MAS[3]

	c_ac_s01 = S.Task('c_ac_s01', length=1, delay_cost=1)
	S += c_ac_s01 >= 34
	c_ac_s01 += MAS[0]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	S += c_bb_t50_mem0 >= 34
	c_bb_t50_mem0 += MAS_MEM[0]

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	S += c_bb_t50_mem1 >= 34
	c_bb_t50_mem1 += MAS_MEM[3]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 34
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t40 = S.Task('c_bc_t40', length=1, delay_cost=1)
	S += c_bc_t40 >= 34
	c_bc_t40 += MAS[2]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=6, delay_cost=1)
	S += c_cc_t2_t0 >= 34
	c_cc_t2_t0 += MM[0]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	S += c_pc10_mem0 >= 34
	c_pc10_mem0 += MAS_MEM[2]

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	S += c_pc10_mem1 >= 34
	c_pc10_mem1 += MAS_MEM[7]

	c_ab_t01 = S.Task('c_ab_t01', length=1, delay_cost=1)
	S += c_ab_t01 >= 35
	c_ab_t01 += MAS[0]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 35
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=6, delay_cost=1)
	S += c_ab_t4_t4 >= 35
	c_ab_t4_t4 += MM[0]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 35
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 35
	c_bb_t2_t0_mem0 += MAS_MEM[0]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 35
	c_bb_t2_t0_mem1 += MAS_MEM[5]

	c_bb_t50 = S.Task('c_bb_t50', length=1, delay_cost=1)
	S += c_bb_t50 >= 35
	c_bb_t50 += MAS[1]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 35
	c_bc10_mem0 += MAS_MEM[4]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 35
	c_bc10_mem1 += MAS_MEM[1]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 35
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 35
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 35
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_pc10 = S.Task('c_pc10', length=1, delay_cost=1)
	S += c_pc10 >= 35
	c_pc10 += MAS[4]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 36
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 36
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 36
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 36
	c_ac_t51_mem0 += MAS_MEM[8]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 36
	c_ac_t51_mem1 += MAS_MEM[5]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=6, delay_cost=1)
	S += c_bb_t2_t0 >= 36
	c_bb_t2_t0 += MM[0]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 36
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 36
	c_bb_t2_t1_mem0 += MAS_MEM[6]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 36
	c_bb_t2_t1_mem1 += MAS_MEM[3]

	c_bc10 = S.Task('c_bc10', length=1, delay_cost=1)
	S += c_bc10 >= 36
	c_bc10 += MAS[3]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 36
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=1, delay_cost=1)
	S += c_bc_t4_t5 >= 36
	c_bc_t4_t5 += MAS[0]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	S += c_aa_t51_mem0 >= 37
	c_aa_t51_mem0 += MAS_MEM[4]

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	S += c_aa_t51_mem1 >= 37
	c_aa_t51_mem1 += MAS_MEM[3]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 37
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 37
	c_ab_t11_mem1 += MAS_MEM[1]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 37
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 37
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=1, delay_cost=1)
	S += c_ab_t4_t5 >= 37
	c_ab_t4_t5 += MAS[3]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 37
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 37
	c_ac_t4_t4_mem0 += MAS_MEM[6]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 37
	c_ac_t4_t4_mem1 += MAS_MEM[5]

	c_ac_t51 = S.Task('c_ac_t51', length=1, delay_cost=1)
	S += c_ac_t51 >= 37
	c_ac_t51 += MAS[2]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=6, delay_cost=1)
	S += c_bb_t2_t1 >= 37
	c_bb_t2_t1 += MM[0]

	c_aa_t51 = S.Task('c_aa_t51', length=1, delay_cost=1)
	S += c_aa_t51 >= 38
	c_aa_t51 += MAS[2]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 38
	c_ab_s00_mem0 += MAS_MEM[0]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 38
	c_ab_s00_mem1 += MAS_MEM[1]

	c_ab_t11 = S.Task('c_ab_t11', length=1, delay_cost=1)
	S += c_ab_t11 >= 38
	c_ab_t11 += MAS[0]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 38
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=6, delay_cost=1)
	S += c_ac_t4_t4 >= 38
	c_ac_t4_t4 += MM[0]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 38
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 38
	c_bc_t11_mem1 += MAS_MEM[5]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 38
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 38
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 38
	c_bc_t4_t4_mem0 += MAS_MEM[2]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 38
	c_bc_t4_t4_mem1 += MAS_MEM[9]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 39
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 39
	c_aa_t2_t1_mem0 += MAS_MEM[0]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 39
	c_aa_t2_t1_mem1 += MAS_MEM[7]

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	S += c_ab00_mem0 >= 39
	c_ab00_mem0 += MAS_MEM[6]

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	S += c_ab00_mem1 >= 39
	c_ab00_mem1 += MAS_MEM[1]

	c_ab_s00 = S.Task('c_ab_s00', length=1, delay_cost=1)
	S += c_ab_s00 >= 39
	c_ab_s00 += MAS[0]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 39
	c_bc_s00_mem0 += MAS_MEM[2]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 39
	c_bc_s00_mem1 += MAS_MEM[9]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 39
	c_bc_s01_mem0 += MAS_MEM[8]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 39
	c_bc_s01_mem1 += MAS_MEM[3]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 39
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t11 = S.Task('c_bc_t11', length=1, delay_cost=1)
	S += c_bc_t11 >= 39
	c_bc_t11 += MAS[4]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 39
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=6, delay_cost=1)
	S += c_bc_t4_t4 >= 39
	c_bc_t4_t4 += MM[0]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 39
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 39
	c_cc_t31_mem1 += MAS_MEM[5]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 40
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 40
	c_aa_t2_t0_mem0 += MAS_MEM[4]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 40
	c_aa_t2_t0_mem1 += MAS_MEM[9]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=6, delay_cost=1)
	S += c_aa_t2_t1 >= 40
	c_aa_t2_t1 += MM[0]

	c_ab00 = S.Task('c_ab00', length=1, delay_cost=1)
	S += c_ab00 >= 40
	c_ab00 += MAS[3]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 40
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 40
	c_ab_t40_mem1 += MM_MEM[1]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 40
	c_ab_t51_mem0 += MAS_MEM[0]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 40
	c_ab_t51_mem1 += MAS_MEM[1]

	c_bc_s00 = S.Task('c_bc_s00', length=1, delay_cost=1)
	S += c_bc_s00 >= 40
	c_bc_s00 += MAS[4]

	c_bc_s01 = S.Task('c_bc_s01', length=1, delay_cost=1)
	S += c_bc_s01 >= 40
	c_bc_s01 += MAS[0]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 40
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 40
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_cc_t31 = S.Task('c_cc_t31', length=1, delay_cost=1)
	S += c_cc_t31 >= 40
	c_cc_t31 += MAS[2]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 40
	c_cc_t40_mem0 += MAS_MEM[6]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 40
	c_cc_t40_mem1 += MAS_MEM[5]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=6, delay_cost=1)
	S += c_aa_t2_t0 >= 41
	c_aa_t2_t0 += MM[0]

	c_ab_t40 = S.Task('c_ab_t40', length=1, delay_cost=1)
	S += c_ab_t40 >= 41
	c_ab_t40 += MAS[2]

	c_ab_t51 = S.Task('c_ab_t51', length=1, delay_cost=1)
	S += c_ab_t51 >= 41
	c_ab_t51 += MAS[3]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 41
	c_ac_s00_mem0 += MAS_MEM[0]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 41
	c_ac_s00_mem1 += MAS_MEM[5]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 41
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 41
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 41
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 41
	c_bc_t01_mem1 += MAS_MEM[9]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 41
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 41
	c_cc_t2_t1_mem0 += MAS_MEM[8]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 41
	c_cc_t2_t1_mem1 += MAS_MEM[1]

	c_cc_t40 = S.Task('c_cc_t40', length=1, delay_cost=1)
	S += c_cc_t40 >= 41
	c_cc_t40 += MAS[0]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 41
	c_cc_t41_mem0 += MAS_MEM[4]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 41
	c_cc_t41_mem1 += MAS_MEM[7]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 42
	c_ab10_mem0 += MAS_MEM[4]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 42
	c_ab10_mem1 += MAS_MEM[5]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 42
	c_ab_s01_mem0 += MAS_MEM[0]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 42
	c_ab_s01_mem1 += MAS_MEM[1]

	c_ac_s00 = S.Task('c_ac_s00', length=1, delay_cost=1)
	S += c_ac_s00 >= 42
	c_ac_s00 += MAS[2]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 42
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 42
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 42
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 42
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_bc_t01 = S.Task('c_bc_t01', length=1, delay_cost=1)
	S += c_bc_t01 >= 42
	c_bc_t01 += MAS[0]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=6, delay_cost=1)
	S += c_cc_t2_t1 >= 42
	c_cc_t2_t1 += MM[0]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 42
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 42
	c_cc_t2_t4_mem0 += MAS_MEM[6]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 42
	c_cc_t2_t4_mem1 += MAS_MEM[9]

	c_cc_t41 = S.Task('c_cc_t41', length=1, delay_cost=1)
	S += c_cc_t41 >= 42
	c_cc_t41 += MAS[1]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 43
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 43
	c_aa_t2_t4_mem0 += MAS_MEM[4]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 43
	c_aa_t2_t4_mem1 += MAS_MEM[3]

	c_ab10 = S.Task('c_ab10', length=1, delay_cost=1)
	S += c_ab10 >= 43
	c_ab10 += MAS[3]

	c_ab_s01 = S.Task('c_ab_s01', length=1, delay_cost=1)
	S += c_ab_s01 >= 43
	c_ab_s01 += MAS[1]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 43
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 43
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 43
	c_ac_t41_mem1 += MAS_MEM[1]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=1, delay_cost=1)
	S += c_ac_t4_t5 >= 43
	c_ac_t4_t5 += MAS[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 43
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 43
	c_bc_t51_mem0 += MAS_MEM[0]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 43
	c_bc_t51_mem1 += MAS_MEM[9]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=6, delay_cost=1)
	S += c_cc_t2_t4 >= 43
	c_cc_t2_t4 += MM[0]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=6, delay_cost=1)
	S += c_aa_t2_t4 >= 44
	c_aa_t2_t4 += MM[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 44
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 44
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 44
	c_ab_t41_mem1 += MAS_MEM[7]

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	S += c_ac11_mem0 >= 44
	c_ac11_mem0 += MAS_MEM[0]

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	S += c_ac11_mem1 >= 44
	c_ac11_mem1 += MAS_MEM[5]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 44
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t41 = S.Task('c_ac_t41', length=1, delay_cost=1)
	S += c_ac_t41 >= 44
	c_ac_t41 += MAS[0]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 44
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 44
	c_bb_t2_t4_mem0 += MAS_MEM[2]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 44
	c_bb_t2_t4_mem1 += MAS_MEM[9]

	c_bc_t51 = S.Task('c_bc_t51', length=1, delay_cost=1)
	S += c_bc_t51 >= 44
	c_bc_t51 += MAS[3]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 44
	c_cc11_mem0 += MAS_MEM[4]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	S += c_cc_t50_mem0 >= 44
	c_cc_t50_mem0 += MAS_MEM[6]

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	S += c_cc_t50_mem1 >= 44
	c_cc_t50_mem1 += MAS_MEM[1]

	c_ab_t41 = S.Task('c_ab_t41', length=1, delay_cost=1)
	S += c_ab_t41 >= 45
	c_ab_t41 += MAS[2]

	c_ac11 = S.Task('c_ac11', length=1, delay_cost=1)
	S += c_ac11 >= 45
	c_ac11 += MAS[3]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 45
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=6, delay_cost=1)
	S += c_bb_t2_t4 >= 45
	c_bb_t2_t4 += MM[0]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	S += c_bc00_mem0 >= 45
	c_bc00_mem0 += MAS_MEM[4]

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	S += c_bc00_mem1 >= 45
	c_bc00_mem1 += MAS_MEM[9]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 45
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 45
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 45
	c_bc_t41_mem1 += MAS_MEM[1]

	c_cc11 = S.Task('c_cc11', length=1, delay_cost=1)
	S += c_cc11 >= 45
	c_cc11 += MAS[0]

	c_cc_t50 = S.Task('c_cc_t50', length=1, delay_cost=1)
	S += c_cc_t50 >= 45
	c_cc_t50 += MAS[1]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	S += c_pc11_mem0 >= 45
	c_pc11_mem0 += MAS_MEM[0]

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	S += c_pc11_mem1 >= 45
	c_pc11_mem1 += MAS_MEM[7]

	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	S += c_pcb_t1_t0_in >= 45
	c_pcb_t1_t0_in += MM_in[0]

	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem0 >= 45
	c_pcb_t1_t0_mem0 += MAS_MEM[8]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	S += c_ab01_mem0 >= 46
	c_ab01_mem0 += MAS_MEM[0]

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	S += c_ab01_mem1 >= 46
	c_ab01_mem1 += MAS_MEM[3]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 46
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 46
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 46
	c_bb_t2_t5_mem1 += MM_MEM[1]

	c_bc00 = S.Task('c_bc00', length=1, delay_cost=1)
	S += c_bc00 >= 46
	c_bc00 += MAS[2]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 46
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t41 = S.Task('c_bc_t41', length=1, delay_cost=1)
	S += c_bc_t41 >= 46
	c_bc_t41 += MAS[3]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem0 >= 46
	c_ccxi_y1_0_mem0 += MAS_MEM[2]

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem1 >= 46
	c_ccxi_y1_0_mem1 += MAS_MEM[1]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	S += c_pa10_mem0 >= 46
	c_pa10_mem0 += MAS_MEM[4]

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	S += c_pa10_mem1 >= 46
	c_pa10_mem1 += MAS_MEM[5]

	c_pc11 = S.Task('c_pc11', length=1, delay_cost=1)
	S += c_pc11 >= 46
	c_pc11 += MAS[4]

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=6, delay_cost=1)
	S += c_pcb_t1_t0 >= 46
	c_pcb_t1_t0 += MM[0]

	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	S += c_pcb_t1_t1_in >= 46
	c_pcb_t1_t1_in += MM_in[0]

	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem0 >= 46
	c_pcb_t1_t1_mem0 += MAS_MEM[8]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 47
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 47
	c_aa_t20_mem1 += MM_MEM[1]

	c_ab01 = S.Task('c_ab01', length=1, delay_cost=1)
	S += c_ab01 >= 47
	c_ab01 += MAS[0]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 47
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 47
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=1, delay_cost=1)
	S += c_bb_t2_t5 >= 47
	c_bb_t2_t5 += MAS[3]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	S += c_bc01_mem0 >= 47
	c_bc01_mem0 += MAS_MEM[0]

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	S += c_bc01_mem1 >= 47
	c_bc01_mem1 += MAS_MEM[1]

	c_cc_t51_mem0 = S.Task('c_cc_t51_mem0', length=1, delay_cost=1)
	S += c_cc_t51_mem0 >= 47
	c_cc_t51_mem0 += MAS_MEM[4]

	c_cc_t51_mem1 = S.Task('c_cc_t51_mem1', length=1, delay_cost=1)
	S += c_cc_t51_mem1 >= 47
	c_cc_t51_mem1 += MAS_MEM[3]

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=1, delay_cost=1)
	S += c_ccxi_y1_0 >= 47
	c_ccxi_y1_0 += MAS[4]

	c_pa10 = S.Task('c_pa10', length=1, delay_cost=1)
	S += c_pa10 >= 47
	c_pa10 += MAS[1]

	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	S += c_paa_t1_t0_in >= 47
	c_paa_t1_t0_in += MM_in[0]

	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem0 >= 47
	c_paa_t1_t0_mem0 += MAS_MEM[2]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	S += c_pb00_mem0 >= 47
	c_pb00_mem0 += MAS_MEM[8]

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	S += c_pb00_mem1 >= 47
	c_pb00_mem1 += MAS_MEM[7]

	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=6, delay_cost=1)
	S += c_pcb_t1_t1 >= 47
	c_pcb_t1_t1 += MM[0]

	c_aa_t20 = S.Task('c_aa_t20', length=1, delay_cost=1)
	S += c_aa_t20 >= 48
	c_aa_t20 += MAS[2]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 48
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 48
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 48
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 48
	c_bb_t20_mem1 += MM_MEM[1]

	c_bc01 = S.Task('c_bc01', length=1, delay_cost=1)
	S += c_bc01 >= 48
	c_bc01 += MAS[0]

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem0 >= 48
	c_bcxi_y1_1_mem0 += MAS_MEM[4]

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem1 >= 48
	c_bcxi_y1_1_mem1 += MAS_MEM[7]

	c_cc_t51 = S.Task('c_cc_t51', length=1, delay_cost=1)
	S += c_cc_t51 >= 48
	c_cc_t51 += MAS[4]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem0 >= 48
	c_ccxi_y1_1_mem0 += MAS_MEM[0]

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem1 >= 48
	c_ccxi_y1_1_mem1 += MAS_MEM[3]

	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=6, delay_cost=1)
	S += c_paa_t1_t0 >= 48
	c_paa_t1_t0 += MM[0]

	c_pb00 = S.Task('c_pb00', length=1, delay_cost=1)
	S += c_pb00 >= 48
	c_pb00 += MAS[1]

	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	S += c_pbc_t0_t0_in >= 48
	c_pbc_t0_t0_in += MM_in[0]

	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem0 >= 48
	c_pbc_t0_t0_mem0 += MAS_MEM[2]

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem0 >= 48
	c_pcb_t1_t2_mem0 += MAS_MEM[8]

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem1 >= 48
	c_pcb_t1_t2_mem1 += MAS_MEM[9]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	S += c_aa_t50_mem0 >= 49
	c_aa_t50_mem0 += MAS_MEM[0]

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	S += c_aa_t50_mem1 >= 49
	c_aa_t50_mem1 += MAS_MEM[5]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	S += c_ab11_mem0 >= 49
	c_ab11_mem0 += MAS_MEM[4]

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	S += c_ab11_mem1 >= 49
	c_ab11_mem1 += MAS_MEM[7]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 49
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t20 = S.Task('c_bb_t20', length=1, delay_cost=1)
	S += c_bb_t20 >= 49
	c_bb_t20 += MAS[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 49
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=1, delay_cost=1)
	S += c_bcxi_y1_1 >= 49
	c_bcxi_y1_1 += MAS[1]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 49
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 49
	c_cc_t2_t5_mem1 += MM_MEM[1]

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=1, delay_cost=1)
	S += c_ccxi_y1_1 >= 49
	c_ccxi_y1_1 += MAS[3]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	S += c_pb01_mem0 >= 49
	c_pb01_mem0 += MAS_MEM[6]

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	S += c_pb01_mem1 >= 49
	c_pb01_mem1 += MAS_MEM[1]

	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=6, delay_cost=1)
	S += c_pbc_t0_t0 >= 49
	c_pbc_t0_t0 += MM[0]

	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=1, delay_cost=1)
	S += c_pcb_t1_t2 >= 49
	c_pcb_t1_t2 += MAS[2]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	S += c_aa00_mem0 >= 50
	c_aa00_mem0 += MAS_MEM[4]

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	S += c_aa00_mem1 >= 50
	c_aa00_mem1 += MAS_MEM[5]

	c_aa_t50 = S.Task('c_aa_t50', length=1, delay_cost=1)
	S += c_aa_t50 >= 50
	c_aa_t50 += MAS[2]

	c_ab11 = S.Task('c_ab11', length=1, delay_cost=1)
	S += c_ab11 >= 50
	c_ab11 += MAS[1]

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	S += c_ac01_mem0 >= 50
	c_ac01_mem0 += MAS_MEM[8]

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	S += c_ac01_mem1 >= 50
	c_ac01_mem1 += MAS_MEM[1]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 50
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 50
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	S += c_bb00_mem0 >= 50
	c_bb00_mem0 += MAS_MEM[0]

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	S += c_bb00_mem1 >= 50
	c_bb00_mem1 += MAS_MEM[3]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 50
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 50
	c_cc_t20_mem1 += MM_MEM[1]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=1, delay_cost=1)
	S += c_cc_t2_t5 >= 50
	c_cc_t2_t5 += MAS[4]

	c_pb01 = S.Task('c_pb01', length=1, delay_cost=1)
	S += c_pb01 >= 50
	c_pb01 += MAS[3]

	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	S += c_pbc_t0_t1_in >= 50
	c_pbc_t0_t1_in += MM_in[0]

	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem0 >= 50
	c_pbc_t0_t1_mem0 += MAS_MEM[6]

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem0 >= 50
	c_pbc_t0_t2_mem0 += MAS_MEM[2]

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem1 >= 50
	c_pbc_t0_t2_mem1 += MAS_MEM[7]

	c_aa00 = S.Task('c_aa00', length=1, delay_cost=1)
	S += c_aa00 >= 51
	c_aa00 += MAS[3]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 51
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 51
	c_aa_t2_t5_mem1 += MM_MEM[1]

	c_ac01 = S.Task('c_ac01', length=1, delay_cost=1)
	S += c_ac01 >= 51
	c_ac01 += MAS[2]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 51
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 51
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_bb00 = S.Task('c_bb00', length=1, delay_cost=1)
	S += c_bb00 >= 51
	c_bb00 += MAS[4]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	S += c_bb_t51_mem0 >= 51
	c_bb_t51_mem0 += MAS_MEM[8]

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	S += c_bb_t51_mem1 >= 51
	c_bb_t51_mem1 += MAS_MEM[1]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	S += c_cc00_mem0 >= 51
	c_cc00_mem0 += MAS_MEM[0]

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	S += c_cc00_mem1 >= 51
	c_cc00_mem1 += MAS_MEM[3]

	c_cc_t20 = S.Task('c_cc_t20', length=1, delay_cost=1)
	S += c_cc_t20 >= 51
	c_cc_t20 += MAS[0]

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	S += c_pa00_mem0 >= 51
	c_pa00_mem0 += MAS_MEM[6]

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	S += c_pa00_mem1 >= 51
	c_pa00_mem1 += MAS_MEM[7]

	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=6, delay_cost=1)
	S += c_pbc_t0_t1 >= 51
	c_pbc_t0_t1 += MM[0]

	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=1, delay_cost=1)
	S += c_pbc_t0_t2 >= 51
	c_pbc_t0_t2 += MAS[1]

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=1, delay_cost=1)
	S += c_aa_t2_t5 >= 52
	c_aa_t2_t5 += MAS[3]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	S += c_ac00_mem0 >= 52
	c_ac00_mem0 += MAS_MEM[0]

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	S += c_ac00_mem1 >= 52
	c_ac00_mem1 += MAS_MEM[5]

	c_bb_t51 = S.Task('c_bb_t51', length=1, delay_cost=1)
	S += c_bb_t51 >= 52
	c_bb_t51 += MAS[0]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 52
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 52
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_cc00 = S.Task('c_cc00', length=1, delay_cost=1)
	S += c_cc00 >= 52
	c_cc00 += MAS[4]

	c_cc_t21_mem0 = S.Task('c_cc_t21_mem0', length=1, delay_cost=1)
	S += c_cc_t21_mem0 >= 52
	c_cc_t21_mem0 += MM_MEM[0]

	c_cc_t21_mem1 = S.Task('c_cc_t21_mem1', length=1, delay_cost=1)
	S += c_cc_t21_mem1 >= 52
	c_cc_t21_mem1 += MAS_MEM[9]

	c_pa00 = S.Task('c_pa00', length=1, delay_cost=1)
	S += c_pa00 >= 52
	c_pa00 += MAS[1]

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	S += c_pb10_mem0 >= 52
	c_pb10_mem0 += MAS_MEM[8]

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	S += c_pb10_mem1 >= 52
	c_pb10_mem1 += MAS_MEM[7]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t21_mem0 >= 53
	c_aa_t21_mem0 += MM_MEM[0]

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t21_mem1 >= 53
	c_aa_t21_mem1 += MAS_MEM[7]

	c_ac00 = S.Task('c_ac00', length=1, delay_cost=1)
	S += c_ac00 >= 53
	c_ac00 += MAS[2]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 53
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 53
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	S += c_cc01_mem0 >= 53
	c_cc01_mem0 += MAS_MEM[2]

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	S += c_cc01_mem1 >= 53
	c_cc01_mem1 += MAS_MEM[9]

	c_cc_t21 = S.Task('c_cc_t21', length=1, delay_cost=1)
	S += c_cc_t21 >= 53
	c_cc_t21 += MAS[1]

	c_pb10 = S.Task('c_pb10', length=1, delay_cost=1)
	S += c_pb10 >= 53
	c_pb10 += MAS[0]

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	S += c_pc00_mem0 >= 53
	c_pc00_mem0 += MAS_MEM[8]

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	S += c_pc00_mem1 >= 53
	c_pc00_mem1 += MAS_MEM[5]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	S += c_aa01_mem0 >= 54
	c_aa01_mem0 += MAS_MEM[6]

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	S += c_aa01_mem1 >= 54
	c_aa01_mem1 += MAS_MEM[5]

	c_aa_t21 = S.Task('c_aa_t21', length=1, delay_cost=1)
	S += c_aa_t21 >= 54
	c_aa_t21 += MAS[3]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 54
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	S += c_bb_t21_mem0 >= 54
	c_bb_t21_mem0 += MM_MEM[0]

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	S += c_bb_t21_mem1 >= 54
	c_bb_t21_mem1 += MAS_MEM[7]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 54
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_cc01 = S.Task('c_cc01', length=1, delay_cost=1)
	S += c_cc01 >= 54
	c_cc01 += MAS[4]

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	S += c_pb11_mem0 >= 54
	c_pb11_mem0 += MAS_MEM[8]

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	S += c_pb11_mem1 >= 54
	c_pb11_mem1 += MAS_MEM[3]

	c_pc00 = S.Task('c_pc00', length=1, delay_cost=1)
	S += c_pc00 >= 54
	c_pc00 += MAS[1]

	c_aa01 = S.Task('c_aa01', length=1, delay_cost=1)
	S += c_aa01 >= 55
	c_aa01 += MAS[3]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	S += c_bb01_mem0 >= 55
	c_bb01_mem0 += MAS_MEM[8]

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	S += c_bb01_mem1 >= 55
	c_bb01_mem1 += MAS_MEM[1]

	c_bb_t21 = S.Task('c_bb_t21', length=1, delay_cost=1)
	S += c_bb_t21 >= 55
	c_bb_t21 += MAS[4]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 55
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 55
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	S += c_pa01_mem0 >= 55
	c_pa01_mem0 += MAS_MEM[6]

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	S += c_pa01_mem1 >= 55
	c_pa01_mem1 += MAS_MEM[3]

	c_pb11 = S.Task('c_pb11', length=1, delay_cost=1)
	S += c_pb11 >= 55
	c_pb11 += MAS[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 56
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bb01 = S.Task('c_bb01', length=1, delay_cost=1)
	S += c_bb01 >= 56
	c_bb01 += MAS[2]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 56
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_pa01 = S.Task('c_pa01', length=1, delay_cost=1)
	S += c_pa01 >= 56
	c_pa01 += MAS[3]

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	S += c_pc01_mem0 >= 56
	c_pc01_mem0 += MAS_MEM[4]

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	S += c_pc01_mem1 >= 56
	c_pc01_mem1 += MAS_MEM[5]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 57
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 57
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_pc01 = S.Task('c_pc01', length=1, delay_cost=1)
	S += c_pc01 >= 57
	c_pc01 += MAS[3]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 58
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 58
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 59
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 59
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 60
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 60
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 61
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 61
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 62
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 62
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 63
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 63
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 64
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 64
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 65
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 65
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 66
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 66
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 67
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 67
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 68
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 68
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 69
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 69
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 70
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 70
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 71
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 71
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 72
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem1 >= 72
	c_pbc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 73
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 74
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem1 >= 74
	c_paa_t1_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 75
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem1 >= 75
	c_pcb_t1_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 76
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem1 >= 76
	c_pbc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 77
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem1 >= 77
	c_pcb_t1_t1_mem1 += MAIN_MEM_r[1]


	# new tasks
	c_bc11 = S.Task('c_bc11', length=1, delay_cost=1)
	c_bc11 += alt(MAS)

	S += c_bc11<48

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	c_bc11_mem0 += MAS_MEM[6]
	S += 46 < c_bc11_mem0
	S += c_bc11_mem0 <= c_bc11

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	c_bc11_mem1 += MAS_MEM[7]
	S += 44 < c_bc11_mem1
	S += c_bc11_mem1 <= c_bc11

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=1, delay_cost=1)
	c_bcxi_y1_0 += alt(MAS)

	S += c_bcxi_y1_0<52

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	c_bcxi_y1_0_mem0 += MAS_MEM[6]
	S += 36 < c_bcxi_y1_0_mem0
	S += c_bcxi_y1_0_mem0 <= c_bcxi_y1_0

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	c_bcxi_y1_0_mem1 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_0_mem1*MAS_MEM[1]
	S += (c_bc11*MAS[1])-1 < c_bcxi_y1_0_mem1*MAS_MEM[3]
	S += (c_bc11*MAS[2])-1 < c_bcxi_y1_0_mem1*MAS_MEM[5]
	S += (c_bc11*MAS[3])-1 < c_bcxi_y1_0_mem1*MAS_MEM[7]
	S += (c_bc11*MAS[4])-1 < c_bcxi_y1_0_mem1*MAS_MEM[9]
	S += c_bcxi_y1_0_mem1 <= c_bcxi_y1_0

	c_pa11 = S.Task('c_pa11', length=1, delay_cost=1)
	c_pa11 += alt(MAS)

	S += c_pa11<50

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	c_pa11_mem0 += MAS_MEM[6]
	S += 33 < c_pa11_mem0
	S += c_pa11_mem0 <= c_pa11

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	c_pa11_mem1 += MAS_MEM[1]
	S += 48 < c_pa11_mem1
	S += c_pa11_mem1 <= c_pa11

	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	c_paa_t1_t1_in += alt(MM_in)
	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=6, delay_cost=1)
	c_paa_t1_t1 += alt(MM)
	S += c_paa_t1_t1>=c_paa_t1_t1_in

	S += c_paa_t1_t1<1000

	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	c_paa_t1_t1_mem0 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t1_t1_mem0*MAS_MEM[0]
	S += (c_pa11*MAS[1])-1 < c_paa_t1_t1_mem0*MAS_MEM[2]
	S += (c_pa11*MAS[2])-1 < c_paa_t1_t1_mem0*MAS_MEM[4]
	S += (c_pa11*MAS[3])-1 < c_paa_t1_t1_mem0*MAS_MEM[6]
	S += (c_pa11*MAS[4])-1 < c_paa_t1_t1_mem0*MAS_MEM[8]
	S += c_paa_t1_t1_mem0 <= c_paa_t1_t1

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	c_paa_t1_t1_mem1 += MAIN_MEM_r[1]
	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=1, delay_cost=1)
	c_paa_t1_t2 += alt(MAS)

	S += c_paa_t1_t2<1000

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	c_paa_t1_t2_mem0 += MAS_MEM[2]
	S += 47 < c_paa_t1_t2_mem0
	S += c_paa_t1_t2_mem0 <= c_paa_t1_t2

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	c_paa_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t1_t2_mem1*MAS_MEM[1]
	S += (c_pa11*MAS[1])-1 < c_paa_t1_t2_mem1*MAS_MEM[3]
	S += (c_pa11*MAS[2])-1 < c_paa_t1_t2_mem1*MAS_MEM[5]
	S += (c_pa11*MAS[3])-1 < c_paa_t1_t2_mem1*MAS_MEM[7]
	S += (c_pa11*MAS[4])-1 < c_paa_t1_t2_mem1*MAS_MEM[9]
	S += c_paa_t1_t2_mem1 <= c_paa_t1_t2

	c_pbc_t0_t4_in = S.Task('c_pbc_t0_t4_in', length=1, delay_cost=1)
	c_pbc_t0_t4_in += alt(MM_in)
	c_pbc_t0_t4 = S.Task('c_pbc_t0_t4', length=6, delay_cost=1)
	c_pbc_t0_t4 += alt(MM)
	S += c_pbc_t0_t4>=c_pbc_t0_t4_in

	c_pbc_t0_t4_mem0 = S.Task('c_pbc_t0_t4_mem0', length=1, delay_cost=1)
	c_pbc_t0_t4_mem0 += MAS_MEM[2]
	S += 51 < c_pbc_t0_t4_mem0
	S += c_pbc_t0_t4_mem0 <= c_pbc_t0_t4

	c_pbc_t0_t4_mem1 = S.Task('c_pbc_t0_t4_mem1', length=1, delay_cost=1)
	c_pbc_t0_t4_mem1 += MAS_MEM[5]
	S += 11 < c_pbc_t0_t4_mem1
	S += c_pbc_t0_t4_mem1 <= c_pbc_t0_t4

	c_pbc_t00 = S.Task('c_pbc_t00', length=1, delay_cost=1)
	c_pbc_t00 += alt(MAS)

	c_pbc_t00_mem0 = S.Task('c_pbc_t00_mem0', length=1, delay_cost=1)
	c_pbc_t00_mem0 += MM_MEM[0]
	S += 54 < c_pbc_t00_mem0
	S += c_pbc_t00_mem0 <= c_pbc_t00

	c_pbc_t00_mem1 = S.Task('c_pbc_t00_mem1', length=1, delay_cost=1)
	c_pbc_t00_mem1 += MM_MEM[1]
	S += 56 < c_pbc_t00_mem1
	S += c_pbc_t00_mem1 <= c_pbc_t00

	c_pbc_t0_t5 = S.Task('c_pbc_t0_t5', length=1, delay_cost=1)
	c_pbc_t0_t5 += alt(MAS)

	c_pbc_t0_t5_mem0 = S.Task('c_pbc_t0_t5_mem0', length=1, delay_cost=1)
	c_pbc_t0_t5_mem0 += MM_MEM[0]
	S += 54 < c_pbc_t0_t5_mem0
	S += c_pbc_t0_t5_mem0 <= c_pbc_t0_t5

	c_pbc_t0_t5_mem1 = S.Task('c_pbc_t0_t5_mem1', length=1, delay_cost=1)
	c_pbc_t0_t5_mem1 += MM_MEM[1]
	S += 56 < c_pbc_t0_t5_mem1
	S += c_pbc_t0_t5_mem1 <= c_pbc_t0_t5

	c_pbc_t1_t0_in = S.Task('c_pbc_t1_t0_in', length=1, delay_cost=1)
	c_pbc_t1_t0_in += alt(MM_in)
	c_pbc_t1_t0 = S.Task('c_pbc_t1_t0', length=6, delay_cost=1)
	c_pbc_t1_t0 += alt(MM)
	S += c_pbc_t1_t0>=c_pbc_t1_t0_in

	c_pbc_t1_t0_mem0 = S.Task('c_pbc_t1_t0_mem0', length=1, delay_cost=1)
	c_pbc_t1_t0_mem0 += MAS_MEM[0]
	S += 53 < c_pbc_t1_t0_mem0
	S += c_pbc_t1_t0_mem0 <= c_pbc_t1_t0

	c_pbc_t1_t0_mem1 = S.Task('c_pbc_t1_t0_mem1', length=1, delay_cost=1)
	c_pbc_t1_t0_mem1 += MAIN_MEM_r[1]
	c_pbc_t1_t1_in = S.Task('c_pbc_t1_t1_in', length=1, delay_cost=1)
	c_pbc_t1_t1_in += alt(MM_in)
	c_pbc_t1_t1 = S.Task('c_pbc_t1_t1', length=6, delay_cost=1)
	c_pbc_t1_t1 += alt(MM)
	S += c_pbc_t1_t1>=c_pbc_t1_t1_in

	c_pbc_t1_t1_mem0 = S.Task('c_pbc_t1_t1_mem0', length=1, delay_cost=1)
	c_pbc_t1_t1_mem0 += MAS_MEM[0]
	S += 55 < c_pbc_t1_t1_mem0
	S += c_pbc_t1_t1_mem0 <= c_pbc_t1_t1

	c_pbc_t1_t1_mem1 = S.Task('c_pbc_t1_t1_mem1', length=1, delay_cost=1)
	c_pbc_t1_t1_mem1 += MAIN_MEM_r[1]
	c_pbc_t1_t2 = S.Task('c_pbc_t1_t2', length=1, delay_cost=1)
	c_pbc_t1_t2 += alt(MAS)

	c_pbc_t1_t2_mem0 = S.Task('c_pbc_t1_t2_mem0', length=1, delay_cost=1)
	c_pbc_t1_t2_mem0 += MAS_MEM[0]
	S += 53 < c_pbc_t1_t2_mem0
	S += c_pbc_t1_t2_mem0 <= c_pbc_t1_t2

	c_pbc_t1_t2_mem1 = S.Task('c_pbc_t1_t2_mem1', length=1, delay_cost=1)
	c_pbc_t1_t2_mem1 += MAS_MEM[1]
	S += 55 < c_pbc_t1_t2_mem1
	S += c_pbc_t1_t2_mem1 <= c_pbc_t1_t2

	c_pbc_t20 = S.Task('c_pbc_t20', length=1, delay_cost=1)
	c_pbc_t20 += alt(MAS)

	c_pbc_t20_mem0 = S.Task('c_pbc_t20_mem0', length=1, delay_cost=1)
	c_pbc_t20_mem0 += MAS_MEM[2]
	S += 48 < c_pbc_t20_mem0
	S += c_pbc_t20_mem0 <= c_pbc_t20

	c_pbc_t20_mem1 = S.Task('c_pbc_t20_mem1', length=1, delay_cost=1)
	c_pbc_t20_mem1 += MAS_MEM[1]
	S += 53 < c_pbc_t20_mem1
	S += c_pbc_t20_mem1 <= c_pbc_t20

	c_pbc_t21 = S.Task('c_pbc_t21', length=1, delay_cost=1)
	c_pbc_t21 += alt(MAS)

	c_pbc_t21_mem0 = S.Task('c_pbc_t21_mem0', length=1, delay_cost=1)
	c_pbc_t21_mem0 += MAS_MEM[6]
	S += 50 < c_pbc_t21_mem0
	S += c_pbc_t21_mem0 <= c_pbc_t21

	c_pbc_t21_mem1 = S.Task('c_pbc_t21_mem1', length=1, delay_cost=1)
	c_pbc_t21_mem1 += MAS_MEM[1]
	S += 55 < c_pbc_t21_mem1
	S += c_pbc_t21_mem1 <= c_pbc_t21

	c_pcb_t0_t0_in = S.Task('c_pcb_t0_t0_in', length=1, delay_cost=1)
	c_pcb_t0_t0_in += alt(MM_in)
	c_pcb_t0_t0 = S.Task('c_pcb_t0_t0', length=6, delay_cost=1)
	c_pcb_t0_t0 += alt(MM)
	S += c_pcb_t0_t0>=c_pcb_t0_t0_in

	c_pcb_t0_t0_mem0 = S.Task('c_pcb_t0_t0_mem0', length=1, delay_cost=1)
	c_pcb_t0_t0_mem0 += MAS_MEM[2]
	S += 54 < c_pcb_t0_t0_mem0
	S += c_pcb_t0_t0_mem0 <= c_pcb_t0_t0

	c_pcb_t0_t0_mem1 = S.Task('c_pcb_t0_t0_mem1', length=1, delay_cost=1)
	c_pcb_t0_t0_mem1 += MAIN_MEM_r[1]
	c_pcb_t0_t1_in = S.Task('c_pcb_t0_t1_in', length=1, delay_cost=1)
	c_pcb_t0_t1_in += alt(MM_in)
	c_pcb_t0_t1 = S.Task('c_pcb_t0_t1', length=6, delay_cost=1)
	c_pcb_t0_t1 += alt(MM)
	S += c_pcb_t0_t1>=c_pcb_t0_t1_in

	c_pcb_t0_t1_mem0 = S.Task('c_pcb_t0_t1_mem0', length=1, delay_cost=1)
	c_pcb_t0_t1_mem0 += MAS_MEM[6]
	S += 57 < c_pcb_t0_t1_mem0
	S += c_pcb_t0_t1_mem0 <= c_pcb_t0_t1

	c_pcb_t0_t1_mem1 = S.Task('c_pcb_t0_t1_mem1', length=1, delay_cost=1)
	c_pcb_t0_t1_mem1 += MAIN_MEM_r[1]
	c_pcb_t0_t2 = S.Task('c_pcb_t0_t2', length=1, delay_cost=1)
	c_pcb_t0_t2 += alt(MAS)

	c_pcb_t0_t2_mem0 = S.Task('c_pcb_t0_t2_mem0', length=1, delay_cost=1)
	c_pcb_t0_t2_mem0 += MAS_MEM[2]
	S += 54 < c_pcb_t0_t2_mem0
	S += c_pcb_t0_t2_mem0 <= c_pcb_t0_t2

	c_pcb_t0_t2_mem1 = S.Task('c_pcb_t0_t2_mem1', length=1, delay_cost=1)
	c_pcb_t0_t2_mem1 += MAS_MEM[7]
	S += 57 < c_pcb_t0_t2_mem1
	S += c_pcb_t0_t2_mem1 <= c_pcb_t0_t2

	c_pcb_t1_t4_in = S.Task('c_pcb_t1_t4_in', length=1, delay_cost=1)
	c_pcb_t1_t4_in += alt(MM_in)
	c_pcb_t1_t4 = S.Task('c_pcb_t1_t4', length=6, delay_cost=1)
	c_pcb_t1_t4 += alt(MM)
	S += c_pcb_t1_t4>=c_pcb_t1_t4_in

	c_pcb_t1_t4_mem0 = S.Task('c_pcb_t1_t4_mem0', length=1, delay_cost=1)
	c_pcb_t1_t4_mem0 += MAS_MEM[4]
	S += 49 < c_pcb_t1_t4_mem0
	S += c_pcb_t1_t4_mem0 <= c_pcb_t1_t4

	c_pcb_t1_t4_mem1 = S.Task('c_pcb_t1_t4_mem1', length=1, delay_cost=1)
	c_pcb_t1_t4_mem1 += MAS_MEM[1]
	S += 10 < c_pcb_t1_t4_mem1
	S += c_pcb_t1_t4_mem1 <= c_pcb_t1_t4

	c_pcb_t10 = S.Task('c_pcb_t10', length=1, delay_cost=1)
	c_pcb_t10 += alt(MAS)

	c_pcb_t10_mem0 = S.Task('c_pcb_t10_mem0', length=1, delay_cost=1)
	c_pcb_t10_mem0 += MM_MEM[0]
	S += 51 < c_pcb_t10_mem0
	S += c_pcb_t10_mem0 <= c_pcb_t10

	c_pcb_t10_mem1 = S.Task('c_pcb_t10_mem1', length=1, delay_cost=1)
	c_pcb_t10_mem1 += MM_MEM[1]
	S += 52 < c_pcb_t10_mem1
	S += c_pcb_t10_mem1 <= c_pcb_t10

	c_pcb_t1_t5 = S.Task('c_pcb_t1_t5', length=1, delay_cost=1)
	c_pcb_t1_t5 += alt(MAS)

	c_pcb_t1_t5_mem0 = S.Task('c_pcb_t1_t5_mem0', length=1, delay_cost=1)
	c_pcb_t1_t5_mem0 += MM_MEM[0]
	S += 51 < c_pcb_t1_t5_mem0
	S += c_pcb_t1_t5_mem0 <= c_pcb_t1_t5

	c_pcb_t1_t5_mem1 = S.Task('c_pcb_t1_t5_mem1', length=1, delay_cost=1)
	c_pcb_t1_t5_mem1 += MM_MEM[1]
	S += 52 < c_pcb_t1_t5_mem1
	S += c_pcb_t1_t5_mem1 <= c_pcb_t1_t5

	c_pcb_t20 = S.Task('c_pcb_t20', length=1, delay_cost=1)
	c_pcb_t20 += alt(MAS)

	c_pcb_t20_mem0 = S.Task('c_pcb_t20_mem0', length=1, delay_cost=1)
	c_pcb_t20_mem0 += MAS_MEM[2]
	S += 54 < c_pcb_t20_mem0
	S += c_pcb_t20_mem0 <= c_pcb_t20

	c_pcb_t20_mem1 = S.Task('c_pcb_t20_mem1', length=1, delay_cost=1)
	c_pcb_t20_mem1 += MAS_MEM[9]
	S += 35 < c_pcb_t20_mem1
	S += c_pcb_t20_mem1 <= c_pcb_t20

	c_pcb_t21 = S.Task('c_pcb_t21', length=1, delay_cost=1)
	c_pcb_t21 += alt(MAS)

	c_pcb_t21_mem0 = S.Task('c_pcb_t21_mem0', length=1, delay_cost=1)
	c_pcb_t21_mem0 += MAS_MEM[6]
	S += 57 < c_pcb_t21_mem0
	S += c_pcb_t21_mem0 <= c_pcb_t21

	c_pcb_t21_mem1 = S.Task('c_pcb_t21_mem1', length=1, delay_cost=1)
	c_pcb_t21_mem1 += MAS_MEM[9]
	S += 46 < c_pcb_t21_mem1
	S += c_pcb_t21_mem1 <= c_pcb_t21

	c_paa_t0_t0_in = S.Task('c_paa_t0_t0_in', length=1, delay_cost=1)
	c_paa_t0_t0_in += alt(MM_in)
	c_paa_t0_t0 = S.Task('c_paa_t0_t0', length=6, delay_cost=1)
	c_paa_t0_t0 += alt(MM)
	S += c_paa_t0_t0>=c_paa_t0_t0_in

	c_paa_t0_t0_mem0 = S.Task('c_paa_t0_t0_mem0', length=1, delay_cost=1)
	c_paa_t0_t0_mem0 += MAS_MEM[2]
	S += 52 < c_paa_t0_t0_mem0
	S += c_paa_t0_t0_mem0 <= c_paa_t0_t0

	c_paa_t0_t0_mem1 = S.Task('c_paa_t0_t0_mem1', length=1, delay_cost=1)
	c_paa_t0_t0_mem1 += MAIN_MEM_r[1]
	c_paa_t0_t1_in = S.Task('c_paa_t0_t1_in', length=1, delay_cost=1)
	c_paa_t0_t1_in += alt(MM_in)
	c_paa_t0_t1 = S.Task('c_paa_t0_t1', length=6, delay_cost=1)
	c_paa_t0_t1 += alt(MM)
	S += c_paa_t0_t1>=c_paa_t0_t1_in

	c_paa_t0_t1_mem0 = S.Task('c_paa_t0_t1_mem0', length=1, delay_cost=1)
	c_paa_t0_t1_mem0 += MAS_MEM[6]
	S += 56 < c_paa_t0_t1_mem0
	S += c_paa_t0_t1_mem0 <= c_paa_t0_t1

	c_paa_t0_t1_mem1 = S.Task('c_paa_t0_t1_mem1', length=1, delay_cost=1)
	c_paa_t0_t1_mem1 += MAIN_MEM_r[1]
	c_paa_t0_t2 = S.Task('c_paa_t0_t2', length=1, delay_cost=1)
	c_paa_t0_t2 += alt(MAS)

	c_paa_t0_t2_mem0 = S.Task('c_paa_t0_t2_mem0', length=1, delay_cost=1)
	c_paa_t0_t2_mem0 += MAS_MEM[2]
	S += 52 < c_paa_t0_t2_mem0
	S += c_paa_t0_t2_mem0 <= c_paa_t0_t2

	c_paa_t0_t2_mem1 = S.Task('c_paa_t0_t2_mem1', length=1, delay_cost=1)
	c_paa_t0_t2_mem1 += MAS_MEM[7]
	S += 56 < c_paa_t0_t2_mem1
	S += c_paa_t0_t2_mem1 <= c_paa_t0_t2

	c_paa_t1_t4_in = S.Task('c_paa_t1_t4_in', length=1, delay_cost=1)
	c_paa_t1_t4_in += alt(MM_in)
	c_paa_t1_t4 = S.Task('c_paa_t1_t4', length=6, delay_cost=1)
	c_paa_t1_t4 += alt(MM)
	S += c_paa_t1_t4>=c_paa_t1_t4_in

	c_paa_t1_t4_mem0 = S.Task('c_paa_t1_t4_mem0', length=1, delay_cost=1)
	c_paa_t1_t4_mem0 += alt(MAS_MEM)
	S += (c_paa_t1_t2*MAS[0])-1 < c_paa_t1_t4_mem0*MAS_MEM[0]
	S += (c_paa_t1_t2*MAS[1])-1 < c_paa_t1_t4_mem0*MAS_MEM[2]
	S += (c_paa_t1_t2*MAS[2])-1 < c_paa_t1_t4_mem0*MAS_MEM[4]
	S += (c_paa_t1_t2*MAS[3])-1 < c_paa_t1_t4_mem0*MAS_MEM[6]
	S += (c_paa_t1_t2*MAS[4])-1 < c_paa_t1_t4_mem0*MAS_MEM[8]
	S += c_paa_t1_t4_mem0 <= c_paa_t1_t4

	c_paa_t1_t4_mem1 = S.Task('c_paa_t1_t4_mem1', length=1, delay_cost=1)
	c_paa_t1_t4_mem1 += MAS_MEM[7]
	S += 10 < c_paa_t1_t4_mem1
	S += c_paa_t1_t4_mem1 <= c_paa_t1_t4

	c_paa_t10 = S.Task('c_paa_t10', length=1, delay_cost=1)
	c_paa_t10 += alt(MAS)

	c_paa_t10_mem0 = S.Task('c_paa_t10_mem0', length=1, delay_cost=1)
	c_paa_t10_mem0 += MM_MEM[0]
	S += 53 < c_paa_t10_mem0
	S += c_paa_t10_mem0 <= c_paa_t10

	c_paa_t10_mem1 = S.Task('c_paa_t10_mem1', length=1, delay_cost=1)
	c_paa_t10_mem1 += alt(MM_MEM)
	S += (c_paa_t1_t1*MM[0])-1 < c_paa_t10_mem1*MM_MEM[1]
	S += c_paa_t10_mem1 <= c_paa_t10

	c_paa_t1_t5 = S.Task('c_paa_t1_t5', length=1, delay_cost=1)
	c_paa_t1_t5 += alt(MAS)

	c_paa_t1_t5_mem0 = S.Task('c_paa_t1_t5_mem0', length=1, delay_cost=1)
	c_paa_t1_t5_mem0 += MM_MEM[0]
	S += 53 < c_paa_t1_t5_mem0
	S += c_paa_t1_t5_mem0 <= c_paa_t1_t5

	c_paa_t1_t5_mem1 = S.Task('c_paa_t1_t5_mem1', length=1, delay_cost=1)
	c_paa_t1_t5_mem1 += alt(MM_MEM)
	S += (c_paa_t1_t1*MM[0])-1 < c_paa_t1_t5_mem1*MM_MEM[1]
	S += c_paa_t1_t5_mem1 <= c_paa_t1_t5

	c_paa_t20 = S.Task('c_paa_t20', length=1, delay_cost=1)
	c_paa_t20 += alt(MAS)

	c_paa_t20_mem0 = S.Task('c_paa_t20_mem0', length=1, delay_cost=1)
	c_paa_t20_mem0 += MAS_MEM[2]
	S += 52 < c_paa_t20_mem0
	S += c_paa_t20_mem0 <= c_paa_t20

	c_paa_t20_mem1 = S.Task('c_paa_t20_mem1', length=1, delay_cost=1)
	c_paa_t20_mem1 += MAS_MEM[3]
	S += 47 < c_paa_t20_mem1
	S += c_paa_t20_mem1 <= c_paa_t20

	c_paa_t21 = S.Task('c_paa_t21', length=1, delay_cost=1)
	c_paa_t21 += alt(MAS)

	c_paa_t21_mem0 = S.Task('c_paa_t21_mem0', length=1, delay_cost=1)
	c_paa_t21_mem0 += MAS_MEM[6]
	S += 56 < c_paa_t21_mem0
	S += c_paa_t21_mem0 <= c_paa_t21

	c_paa_t21_mem1 = S.Task('c_paa_t21_mem1', length=1, delay_cost=1)
	c_paa_t21_mem1 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t21_mem1*MAS_MEM[1]
	S += (c_pa11*MAS[1])-1 < c_paa_t21_mem1*MAS_MEM[3]
	S += (c_pa11*MAS[2])-1 < c_paa_t21_mem1*MAS_MEM[5]
	S += (c_pa11*MAS[3])-1 < c_paa_t21_mem1*MAS_MEM[7]
	S += (c_pa11*MAS[4])-1 < c_paa_t21_mem1*MAS_MEM[9]
	S += c_paa_t21_mem1 <= c_paa_t21

	c_pbc_t01 = S.Task('c_pbc_t01', length=1, delay_cost=1)
	c_pbc_t01 += alt(MAS)

	c_pbc_t01_mem0 = S.Task('c_pbc_t01_mem0', length=1, delay_cost=1)
	c_pbc_t01_mem0 += alt(MM_MEM)
	S += (c_pbc_t0_t4*MM[0])-1 < c_pbc_t01_mem0*MM_MEM[0]
	S += c_pbc_t01_mem0 <= c_pbc_t01

	c_pbc_t01_mem1 = S.Task('c_pbc_t01_mem1', length=1, delay_cost=1)
	c_pbc_t01_mem1 += alt(MAS_MEM)
	S += (c_pbc_t0_t5*MAS[0])-1 < c_pbc_t01_mem1*MAS_MEM[1]
	S += (c_pbc_t0_t5*MAS[1])-1 < c_pbc_t01_mem1*MAS_MEM[3]
	S += (c_pbc_t0_t5*MAS[2])-1 < c_pbc_t01_mem1*MAS_MEM[5]
	S += (c_pbc_t0_t5*MAS[3])-1 < c_pbc_t01_mem1*MAS_MEM[7]
	S += (c_pbc_t0_t5*MAS[4])-1 < c_pbc_t01_mem1*MAS_MEM[9]
	S += c_pbc_t01_mem1 <= c_pbc_t01

	c_pbc_t1_t4_in = S.Task('c_pbc_t1_t4_in', length=1, delay_cost=1)
	c_pbc_t1_t4_in += alt(MM_in)
	c_pbc_t1_t4 = S.Task('c_pbc_t1_t4', length=6, delay_cost=1)
	c_pbc_t1_t4 += alt(MM)
	S += c_pbc_t1_t4>=c_pbc_t1_t4_in

	c_pbc_t1_t4_mem0 = S.Task('c_pbc_t1_t4_mem0', length=1, delay_cost=1)
	c_pbc_t1_t4_mem0 += alt(MAS_MEM)
	S += (c_pbc_t1_t2*MAS[0])-1 < c_pbc_t1_t4_mem0*MAS_MEM[0]
	S += (c_pbc_t1_t2*MAS[1])-1 < c_pbc_t1_t4_mem0*MAS_MEM[2]
	S += (c_pbc_t1_t2*MAS[2])-1 < c_pbc_t1_t4_mem0*MAS_MEM[4]
	S += (c_pbc_t1_t2*MAS[3])-1 < c_pbc_t1_t4_mem0*MAS_MEM[6]
	S += (c_pbc_t1_t2*MAS[4])-1 < c_pbc_t1_t4_mem0*MAS_MEM[8]
	S += c_pbc_t1_t4_mem0 <= c_pbc_t1_t4

	c_pbc_t1_t4_mem1 = S.Task('c_pbc_t1_t4_mem1', length=1, delay_cost=1)
	c_pbc_t1_t4_mem1 += MAS_MEM[9]
	S += 9 < c_pbc_t1_t4_mem1
	S += c_pbc_t1_t4_mem1 <= c_pbc_t1_t4

	c_pbc_t10 = S.Task('c_pbc_t10', length=1, delay_cost=1)
	c_pbc_t10 += alt(MAS)

	c_pbc_t10_mem0 = S.Task('c_pbc_t10_mem0', length=1, delay_cost=1)
	c_pbc_t10_mem0 += alt(MM_MEM)
	S += (c_pbc_t1_t0*MM[0])-1 < c_pbc_t10_mem0*MM_MEM[0]
	S += c_pbc_t10_mem0 <= c_pbc_t10

	c_pbc_t10_mem1 = S.Task('c_pbc_t10_mem1', length=1, delay_cost=1)
	c_pbc_t10_mem1 += alt(MM_MEM)
	S += (c_pbc_t1_t1*MM[0])-1 < c_pbc_t10_mem1*MM_MEM[1]
	S += c_pbc_t10_mem1 <= c_pbc_t10

	c_pbc_t1_t5 = S.Task('c_pbc_t1_t5', length=1, delay_cost=1)
	c_pbc_t1_t5 += alt(MAS)

	c_pbc_t1_t5_mem0 = S.Task('c_pbc_t1_t5_mem0', length=1, delay_cost=1)
	c_pbc_t1_t5_mem0 += alt(MM_MEM)
	S += (c_pbc_t1_t0*MM[0])-1 < c_pbc_t1_t5_mem0*MM_MEM[0]
	S += c_pbc_t1_t5_mem0 <= c_pbc_t1_t5

	c_pbc_t1_t5_mem1 = S.Task('c_pbc_t1_t5_mem1', length=1, delay_cost=1)
	c_pbc_t1_t5_mem1 += alt(MM_MEM)
	S += (c_pbc_t1_t1*MM[0])-1 < c_pbc_t1_t5_mem1*MM_MEM[1]
	S += c_pbc_t1_t5_mem1 <= c_pbc_t1_t5

	c_pbc_t4_t0_in = S.Task('c_pbc_t4_t0_in', length=1, delay_cost=1)
	c_pbc_t4_t0_in += alt(MM_in)
	c_pbc_t4_t0 = S.Task('c_pbc_t4_t0', length=6, delay_cost=1)
	c_pbc_t4_t0 += alt(MM)
	S += c_pbc_t4_t0>=c_pbc_t4_t0_in

	c_pbc_t4_t0_mem0 = S.Task('c_pbc_t4_t0_mem0', length=1, delay_cost=1)
	c_pbc_t4_t0_mem0 += alt(MAS_MEM)
	S += (c_pbc_t20*MAS[0])-1 < c_pbc_t4_t0_mem0*MAS_MEM[0]
	S += (c_pbc_t20*MAS[1])-1 < c_pbc_t4_t0_mem0*MAS_MEM[2]
	S += (c_pbc_t20*MAS[2])-1 < c_pbc_t4_t0_mem0*MAS_MEM[4]
	S += (c_pbc_t20*MAS[3])-1 < c_pbc_t4_t0_mem0*MAS_MEM[6]
	S += (c_pbc_t20*MAS[4])-1 < c_pbc_t4_t0_mem0*MAS_MEM[8]
	S += c_pbc_t4_t0_mem0 <= c_pbc_t4_t0

	c_pbc_t4_t0_mem1 = S.Task('c_pbc_t4_t0_mem1', length=1, delay_cost=1)
	c_pbc_t4_t0_mem1 += MAS_MEM[3]
	S += 11 < c_pbc_t4_t0_mem1
	S += c_pbc_t4_t0_mem1 <= c_pbc_t4_t0

	c_pbc_t4_t1_in = S.Task('c_pbc_t4_t1_in', length=1, delay_cost=1)
	c_pbc_t4_t1_in += alt(MM_in)
	c_pbc_t4_t1 = S.Task('c_pbc_t4_t1', length=6, delay_cost=1)
	c_pbc_t4_t1 += alt(MM)
	S += c_pbc_t4_t1>=c_pbc_t4_t1_in

	c_pbc_t4_t1_mem0 = S.Task('c_pbc_t4_t1_mem0', length=1, delay_cost=1)
	c_pbc_t4_t1_mem0 += alt(MAS_MEM)
	S += (c_pbc_t21*MAS[0])-1 < c_pbc_t4_t1_mem0*MAS_MEM[0]
	S += (c_pbc_t21*MAS[1])-1 < c_pbc_t4_t1_mem0*MAS_MEM[2]
	S += (c_pbc_t21*MAS[2])-1 < c_pbc_t4_t1_mem0*MAS_MEM[4]
	S += (c_pbc_t21*MAS[3])-1 < c_pbc_t4_t1_mem0*MAS_MEM[6]
	S += (c_pbc_t21*MAS[4])-1 < c_pbc_t4_t1_mem0*MAS_MEM[8]
	S += c_pbc_t4_t1_mem0 <= c_pbc_t4_t1

	c_pbc_t4_t1_mem1 = S.Task('c_pbc_t4_t1_mem1', length=1, delay_cost=1)
	c_pbc_t4_t1_mem1 += MAS_MEM[3]
	S += 10 < c_pbc_t4_t1_mem1
	S += c_pbc_t4_t1_mem1 <= c_pbc_t4_t1

	c_pbc_t4_t2 = S.Task('c_pbc_t4_t2', length=1, delay_cost=1)
	c_pbc_t4_t2 += alt(MAS)

	c_pbc_t4_t2_mem0 = S.Task('c_pbc_t4_t2_mem0', length=1, delay_cost=1)
	c_pbc_t4_t2_mem0 += alt(MAS_MEM)
	S += (c_pbc_t20*MAS[0])-1 < c_pbc_t4_t2_mem0*MAS_MEM[0]
	S += (c_pbc_t20*MAS[1])-1 < c_pbc_t4_t2_mem0*MAS_MEM[2]
	S += (c_pbc_t20*MAS[2])-1 < c_pbc_t4_t2_mem0*MAS_MEM[4]
	S += (c_pbc_t20*MAS[3])-1 < c_pbc_t4_t2_mem0*MAS_MEM[6]
	S += (c_pbc_t20*MAS[4])-1 < c_pbc_t4_t2_mem0*MAS_MEM[8]
	S += c_pbc_t4_t2_mem0 <= c_pbc_t4_t2

	c_pbc_t4_t2_mem1 = S.Task('c_pbc_t4_t2_mem1', length=1, delay_cost=1)
	c_pbc_t4_t2_mem1 += alt(MAS_MEM)
	S += (c_pbc_t21*MAS[0])-1 < c_pbc_t4_t2_mem1*MAS_MEM[1]
	S += (c_pbc_t21*MAS[1])-1 < c_pbc_t4_t2_mem1*MAS_MEM[3]
	S += (c_pbc_t21*MAS[2])-1 < c_pbc_t4_t2_mem1*MAS_MEM[5]
	S += (c_pbc_t21*MAS[3])-1 < c_pbc_t4_t2_mem1*MAS_MEM[7]
	S += (c_pbc_t21*MAS[4])-1 < c_pbc_t4_t2_mem1*MAS_MEM[9]
	S += c_pbc_t4_t2_mem1 <= c_pbc_t4_t2

	c_pcb_t0_t4_in = S.Task('c_pcb_t0_t4_in', length=1, delay_cost=1)
	c_pcb_t0_t4_in += alt(MM_in)
	c_pcb_t0_t4 = S.Task('c_pcb_t0_t4', length=6, delay_cost=1)
	c_pcb_t0_t4 += alt(MM)
	S += c_pcb_t0_t4>=c_pcb_t0_t4_in

	c_pcb_t0_t4_mem0 = S.Task('c_pcb_t0_t4_mem0', length=1, delay_cost=1)
	c_pcb_t0_t4_mem0 += alt(MAS_MEM)
	S += (c_pcb_t0_t2*MAS[0])-1 < c_pcb_t0_t4_mem0*MAS_MEM[0]
	S += (c_pcb_t0_t2*MAS[1])-1 < c_pcb_t0_t4_mem0*MAS_MEM[2]
	S += (c_pcb_t0_t2*MAS[2])-1 < c_pcb_t0_t4_mem0*MAS_MEM[4]
	S += (c_pcb_t0_t2*MAS[3])-1 < c_pcb_t0_t4_mem0*MAS_MEM[6]
	S += (c_pcb_t0_t2*MAS[4])-1 < c_pcb_t0_t4_mem0*MAS_MEM[8]
	S += c_pcb_t0_t4_mem0 <= c_pcb_t0_t4

	c_pcb_t0_t4_mem1 = S.Task('c_pcb_t0_t4_mem1', length=1, delay_cost=1)
	c_pcb_t0_t4_mem1 += MAS_MEM[7]
	S += 11 < c_pcb_t0_t4_mem1
	S += c_pcb_t0_t4_mem1 <= c_pcb_t0_t4

	c_pcb_t00 = S.Task('c_pcb_t00', length=1, delay_cost=1)
	c_pcb_t00 += alt(MAS)

	c_pcb_t00_mem0 = S.Task('c_pcb_t00_mem0', length=1, delay_cost=1)
	c_pcb_t00_mem0 += alt(MM_MEM)
	S += (c_pcb_t0_t0*MM[0])-1 < c_pcb_t00_mem0*MM_MEM[0]
	S += c_pcb_t00_mem0 <= c_pcb_t00

	c_pcb_t00_mem1 = S.Task('c_pcb_t00_mem1', length=1, delay_cost=1)
	c_pcb_t00_mem1 += alt(MM_MEM)
	S += (c_pcb_t0_t1*MM[0])-1 < c_pcb_t00_mem1*MM_MEM[1]
	S += c_pcb_t00_mem1 <= c_pcb_t00

	c_pcb_t0_t5 = S.Task('c_pcb_t0_t5', length=1, delay_cost=1)
	c_pcb_t0_t5 += alt(MAS)

	c_pcb_t0_t5_mem0 = S.Task('c_pcb_t0_t5_mem0', length=1, delay_cost=1)
	c_pcb_t0_t5_mem0 += alt(MM_MEM)
	S += (c_pcb_t0_t0*MM[0])-1 < c_pcb_t0_t5_mem0*MM_MEM[0]
	S += c_pcb_t0_t5_mem0 <= c_pcb_t0_t5

	c_pcb_t0_t5_mem1 = S.Task('c_pcb_t0_t5_mem1', length=1, delay_cost=1)
	c_pcb_t0_t5_mem1 += alt(MM_MEM)
	S += (c_pcb_t0_t1*MM[0])-1 < c_pcb_t0_t5_mem1*MM_MEM[1]
	S += c_pcb_t0_t5_mem1 <= c_pcb_t0_t5

	c_pcb_t11 = S.Task('c_pcb_t11', length=1, delay_cost=1)
	c_pcb_t11 += alt(MAS)

	c_pcb_t11_mem0 = S.Task('c_pcb_t11_mem0', length=1, delay_cost=1)
	c_pcb_t11_mem0 += alt(MM_MEM)
	S += (c_pcb_t1_t4*MM[0])-1 < c_pcb_t11_mem0*MM_MEM[0]
	S += c_pcb_t11_mem0 <= c_pcb_t11

	c_pcb_t11_mem1 = S.Task('c_pcb_t11_mem1', length=1, delay_cost=1)
	c_pcb_t11_mem1 += alt(MAS_MEM)
	S += (c_pcb_t1_t5*MAS[0])-1 < c_pcb_t11_mem1*MAS_MEM[1]
	S += (c_pcb_t1_t5*MAS[1])-1 < c_pcb_t11_mem1*MAS_MEM[3]
	S += (c_pcb_t1_t5*MAS[2])-1 < c_pcb_t11_mem1*MAS_MEM[5]
	S += (c_pcb_t1_t5*MAS[3])-1 < c_pcb_t11_mem1*MAS_MEM[7]
	S += (c_pcb_t1_t5*MAS[4])-1 < c_pcb_t11_mem1*MAS_MEM[9]
	S += c_pcb_t11_mem1 <= c_pcb_t11

	c_pcb_t4_t0_in = S.Task('c_pcb_t4_t0_in', length=1, delay_cost=1)
	c_pcb_t4_t0_in += alt(MM_in)
	c_pcb_t4_t0 = S.Task('c_pcb_t4_t0', length=6, delay_cost=1)
	c_pcb_t4_t0 += alt(MM)
	S += c_pcb_t4_t0>=c_pcb_t4_t0_in

	c_pcb_t4_t0_mem0 = S.Task('c_pcb_t4_t0_mem0', length=1, delay_cost=1)
	c_pcb_t4_t0_mem0 += alt(MAS_MEM)
	S += (c_pcb_t20*MAS[0])-1 < c_pcb_t4_t0_mem0*MAS_MEM[0]
	S += (c_pcb_t20*MAS[1])-1 < c_pcb_t4_t0_mem0*MAS_MEM[2]
	S += (c_pcb_t20*MAS[2])-1 < c_pcb_t4_t0_mem0*MAS_MEM[4]
	S += (c_pcb_t20*MAS[3])-1 < c_pcb_t4_t0_mem0*MAS_MEM[6]
	S += (c_pcb_t20*MAS[4])-1 < c_pcb_t4_t0_mem0*MAS_MEM[8]
	S += c_pcb_t4_t0_mem0 <= c_pcb_t4_t0

	c_pcb_t4_t0_mem1 = S.Task('c_pcb_t4_t0_mem1', length=1, delay_cost=1)
	c_pcb_t4_t0_mem1 += MAS_MEM[9]
	S += 10 < c_pcb_t4_t0_mem1
	S += c_pcb_t4_t0_mem1 <= c_pcb_t4_t0

	c_pcb_t4_t1_in = S.Task('c_pcb_t4_t1_in', length=1, delay_cost=1)
	c_pcb_t4_t1_in += alt(MM_in)
	c_pcb_t4_t1 = S.Task('c_pcb_t4_t1', length=6, delay_cost=1)
	c_pcb_t4_t1 += alt(MM)
	S += c_pcb_t4_t1>=c_pcb_t4_t1_in

	c_pcb_t4_t1_mem0 = S.Task('c_pcb_t4_t1_mem0', length=1, delay_cost=1)
	c_pcb_t4_t1_mem0 += alt(MAS_MEM)
	S += (c_pcb_t21*MAS[0])-1 < c_pcb_t4_t1_mem0*MAS_MEM[0]
	S += (c_pcb_t21*MAS[1])-1 < c_pcb_t4_t1_mem0*MAS_MEM[2]
	S += (c_pcb_t21*MAS[2])-1 < c_pcb_t4_t1_mem0*MAS_MEM[4]
	S += (c_pcb_t21*MAS[3])-1 < c_pcb_t4_t1_mem0*MAS_MEM[6]
	S += (c_pcb_t21*MAS[4])-1 < c_pcb_t4_t1_mem0*MAS_MEM[8]
	S += c_pcb_t4_t1_mem0 <= c_pcb_t4_t1

	c_pcb_t4_t1_mem1 = S.Task('c_pcb_t4_t1_mem1', length=1, delay_cost=1)
	c_pcb_t4_t1_mem1 += MAS_MEM[7]
	S += 9 < c_pcb_t4_t1_mem1
	S += c_pcb_t4_t1_mem1 <= c_pcb_t4_t1

	c_pcb_t4_t2 = S.Task('c_pcb_t4_t2', length=1, delay_cost=1)
	c_pcb_t4_t2 += alt(MAS)

	c_pcb_t4_t2_mem0 = S.Task('c_pcb_t4_t2_mem0', length=1, delay_cost=1)
	c_pcb_t4_t2_mem0 += alt(MAS_MEM)
	S += (c_pcb_t20*MAS[0])-1 < c_pcb_t4_t2_mem0*MAS_MEM[0]
	S += (c_pcb_t20*MAS[1])-1 < c_pcb_t4_t2_mem0*MAS_MEM[2]
	S += (c_pcb_t20*MAS[2])-1 < c_pcb_t4_t2_mem0*MAS_MEM[4]
	S += (c_pcb_t20*MAS[3])-1 < c_pcb_t4_t2_mem0*MAS_MEM[6]
	S += (c_pcb_t20*MAS[4])-1 < c_pcb_t4_t2_mem0*MAS_MEM[8]
	S += c_pcb_t4_t2_mem0 <= c_pcb_t4_t2

	c_pcb_t4_t2_mem1 = S.Task('c_pcb_t4_t2_mem1', length=1, delay_cost=1)
	c_pcb_t4_t2_mem1 += alt(MAS_MEM)
	S += (c_pcb_t21*MAS[0])-1 < c_pcb_t4_t2_mem1*MAS_MEM[1]
	S += (c_pcb_t21*MAS[1])-1 < c_pcb_t4_t2_mem1*MAS_MEM[3]
	S += (c_pcb_t21*MAS[2])-1 < c_pcb_t4_t2_mem1*MAS_MEM[5]
	S += (c_pcb_t21*MAS[3])-1 < c_pcb_t4_t2_mem1*MAS_MEM[7]
	S += (c_pcb_t21*MAS[4])-1 < c_pcb_t4_t2_mem1*MAS_MEM[9]
	S += c_pcb_t4_t2_mem1 <= c_pcb_t4_t2

	c_paa_t0_t4_in = S.Task('c_paa_t0_t4_in', length=1, delay_cost=1)
	c_paa_t0_t4_in += alt(MM_in)
	c_paa_t0_t4 = S.Task('c_paa_t0_t4', length=6, delay_cost=1)
	c_paa_t0_t4 += alt(MM)
	S += c_paa_t0_t4>=c_paa_t0_t4_in

	c_paa_t0_t4_mem0 = S.Task('c_paa_t0_t4_mem0', length=1, delay_cost=1)
	c_paa_t0_t4_mem0 += alt(MAS_MEM)
	S += (c_paa_t0_t2*MAS[0])-1 < c_paa_t0_t4_mem0*MAS_MEM[0]
	S += (c_paa_t0_t2*MAS[1])-1 < c_paa_t0_t4_mem0*MAS_MEM[2]
	S += (c_paa_t0_t2*MAS[2])-1 < c_paa_t0_t4_mem0*MAS_MEM[4]
	S += (c_paa_t0_t2*MAS[3])-1 < c_paa_t0_t4_mem0*MAS_MEM[6]
	S += (c_paa_t0_t2*MAS[4])-1 < c_paa_t0_t4_mem0*MAS_MEM[8]
	S += c_paa_t0_t4_mem0 <= c_paa_t0_t4

	c_paa_t0_t4_mem1 = S.Task('c_paa_t0_t4_mem1', length=1, delay_cost=1)
	c_paa_t0_t4_mem1 += MAS_MEM[5]
	S += 10 < c_paa_t0_t4_mem1
	S += c_paa_t0_t4_mem1 <= c_paa_t0_t4

	c_paa_t00 = S.Task('c_paa_t00', length=1, delay_cost=1)
	c_paa_t00 += alt(MAS)

	c_paa_t00_mem0 = S.Task('c_paa_t00_mem0', length=1, delay_cost=1)
	c_paa_t00_mem0 += alt(MM_MEM)
	S += (c_paa_t0_t0*MM[0])-1 < c_paa_t00_mem0*MM_MEM[0]
	S += c_paa_t00_mem0 <= c_paa_t00

	c_paa_t00_mem1 = S.Task('c_paa_t00_mem1', length=1, delay_cost=1)
	c_paa_t00_mem1 += alt(MM_MEM)
	S += (c_paa_t0_t1*MM[0])-1 < c_paa_t00_mem1*MM_MEM[1]
	S += c_paa_t00_mem1 <= c_paa_t00

	c_paa_t0_t5 = S.Task('c_paa_t0_t5', length=1, delay_cost=1)
	c_paa_t0_t5 += alt(MAS)

	c_paa_t0_t5_mem0 = S.Task('c_paa_t0_t5_mem0', length=1, delay_cost=1)
	c_paa_t0_t5_mem0 += alt(MM_MEM)
	S += (c_paa_t0_t0*MM[0])-1 < c_paa_t0_t5_mem0*MM_MEM[0]
	S += c_paa_t0_t5_mem0 <= c_paa_t0_t5

	c_paa_t0_t5_mem1 = S.Task('c_paa_t0_t5_mem1', length=1, delay_cost=1)
	c_paa_t0_t5_mem1 += alt(MM_MEM)
	S += (c_paa_t0_t1*MM[0])-1 < c_paa_t0_t5_mem1*MM_MEM[1]
	S += c_paa_t0_t5_mem1 <= c_paa_t0_t5

	c_paa_t11 = S.Task('c_paa_t11', length=1, delay_cost=1)
	c_paa_t11 += alt(MAS)

	c_paa_t11_mem0 = S.Task('c_paa_t11_mem0', length=1, delay_cost=1)
	c_paa_t11_mem0 += alt(MM_MEM)
	S += (c_paa_t1_t4*MM[0])-1 < c_paa_t11_mem0*MM_MEM[0]
	S += c_paa_t11_mem0 <= c_paa_t11

	c_paa_t11_mem1 = S.Task('c_paa_t11_mem1', length=1, delay_cost=1)
	c_paa_t11_mem1 += alt(MAS_MEM)
	S += (c_paa_t1_t5*MAS[0])-1 < c_paa_t11_mem1*MAS_MEM[1]
	S += (c_paa_t1_t5*MAS[1])-1 < c_paa_t11_mem1*MAS_MEM[3]
	S += (c_paa_t1_t5*MAS[2])-1 < c_paa_t11_mem1*MAS_MEM[5]
	S += (c_paa_t1_t5*MAS[3])-1 < c_paa_t11_mem1*MAS_MEM[7]
	S += (c_paa_t1_t5*MAS[4])-1 < c_paa_t11_mem1*MAS_MEM[9]
	S += c_paa_t11_mem1 <= c_paa_t11

	c_paa_t4_t0_in = S.Task('c_paa_t4_t0_in', length=1, delay_cost=1)
	c_paa_t4_t0_in += alt(MM_in)
	c_paa_t4_t0 = S.Task('c_paa_t4_t0', length=6, delay_cost=1)
	c_paa_t4_t0 += alt(MM)
	S += c_paa_t4_t0>=c_paa_t4_t0_in

	c_paa_t4_t0_mem0 = S.Task('c_paa_t4_t0_mem0', length=1, delay_cost=1)
	c_paa_t4_t0_mem0 += alt(MAS_MEM)
	S += (c_paa_t20*MAS[0])-1 < c_paa_t4_t0_mem0*MAS_MEM[0]
	S += (c_paa_t20*MAS[1])-1 < c_paa_t4_t0_mem0*MAS_MEM[2]
	S += (c_paa_t20*MAS[2])-1 < c_paa_t4_t0_mem0*MAS_MEM[4]
	S += (c_paa_t20*MAS[3])-1 < c_paa_t4_t0_mem0*MAS_MEM[6]
	S += (c_paa_t20*MAS[4])-1 < c_paa_t4_t0_mem0*MAS_MEM[8]
	S += c_paa_t4_t0_mem0 <= c_paa_t4_t0

	c_paa_t4_t0_mem1 = S.Task('c_paa_t4_t0_mem1', length=1, delay_cost=1)
	c_paa_t4_t0_mem1 += MAS_MEM[3]
	S += 9 < c_paa_t4_t0_mem1
	S += c_paa_t4_t0_mem1 <= c_paa_t4_t0

	c_paa_t4_t1_in = S.Task('c_paa_t4_t1_in', length=1, delay_cost=1)
	c_paa_t4_t1_in += alt(MM_in)
	c_paa_t4_t1 = S.Task('c_paa_t4_t1', length=6, delay_cost=1)
	c_paa_t4_t1 += alt(MM)
	S += c_paa_t4_t1>=c_paa_t4_t1_in

	c_paa_t4_t1_mem0 = S.Task('c_paa_t4_t1_mem0', length=1, delay_cost=1)
	c_paa_t4_t1_mem0 += alt(MAS_MEM)
	S += (c_paa_t21*MAS[0])-1 < c_paa_t4_t1_mem0*MAS_MEM[0]
	S += (c_paa_t21*MAS[1])-1 < c_paa_t4_t1_mem0*MAS_MEM[2]
	S += (c_paa_t21*MAS[2])-1 < c_paa_t4_t1_mem0*MAS_MEM[4]
	S += (c_paa_t21*MAS[3])-1 < c_paa_t4_t1_mem0*MAS_MEM[6]
	S += (c_paa_t21*MAS[4])-1 < c_paa_t4_t1_mem0*MAS_MEM[8]
	S += c_paa_t4_t1_mem0 <= c_paa_t4_t1

	c_paa_t4_t1_mem1 = S.Task('c_paa_t4_t1_mem1', length=1, delay_cost=1)
	c_paa_t4_t1_mem1 += MAS_MEM[1]
	S += 11 < c_paa_t4_t1_mem1
	S += c_paa_t4_t1_mem1 <= c_paa_t4_t1

	c_paa_t4_t2 = S.Task('c_paa_t4_t2', length=1, delay_cost=1)
	c_paa_t4_t2 += alt(MAS)

	c_paa_t4_t2_mem0 = S.Task('c_paa_t4_t2_mem0', length=1, delay_cost=1)
	c_paa_t4_t2_mem0 += alt(MAS_MEM)
	S += (c_paa_t20*MAS[0])-1 < c_paa_t4_t2_mem0*MAS_MEM[0]
	S += (c_paa_t20*MAS[1])-1 < c_paa_t4_t2_mem0*MAS_MEM[2]
	S += (c_paa_t20*MAS[2])-1 < c_paa_t4_t2_mem0*MAS_MEM[4]
	S += (c_paa_t20*MAS[3])-1 < c_paa_t4_t2_mem0*MAS_MEM[6]
	S += (c_paa_t20*MAS[4])-1 < c_paa_t4_t2_mem0*MAS_MEM[8]
	S += c_paa_t4_t2_mem0 <= c_paa_t4_t2

	c_paa_t4_t2_mem1 = S.Task('c_paa_t4_t2_mem1', length=1, delay_cost=1)
	c_paa_t4_t2_mem1 += alt(MAS_MEM)
	S += (c_paa_t21*MAS[0])-1 < c_paa_t4_t2_mem1*MAS_MEM[1]
	S += (c_paa_t21*MAS[1])-1 < c_paa_t4_t2_mem1*MAS_MEM[3]
	S += (c_paa_t21*MAS[2])-1 < c_paa_t4_t2_mem1*MAS_MEM[5]
	S += (c_paa_t21*MAS[3])-1 < c_paa_t4_t2_mem1*MAS_MEM[7]
	S += (c_paa_t21*MAS[4])-1 < c_paa_t4_t2_mem1*MAS_MEM[9]
	S += c_paa_t4_t2_mem1 <= c_paa_t4_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS5/FP12_INV_BEFORE_FPINV/schedule7.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

