from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 168
	S = Scenario("schedule7", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 0
	c_bb_t3_t1_in += MM_in[0]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 0
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 0
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	S += c_aa_a1_0 >= 1
	c_aa_a1_0 += MAS[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 1
	c_ab_t1_t0_in += MM_in[0]

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	S += c_bb_t10 >= 1
	c_bb_t10 += MAS[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=8, delay_cost=1)
	S += c_bb_t3_t1 >= 1
	c_bb_t3_t1 += MM[0]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 1
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 1
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=1, delay_cost=1)
	S += c_cc_t11 >= 1
	c_cc_t11 += MAS[3]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	S += c_cc_t3_t2 >= 1
	c_cc_t3_t2 += MAS[2]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 2
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t11 = S.Task('c_aa_t11', length=1, delay_cost=1)
	S += c_aa_t11 >= 2
	c_aa_t11 += MAS[2]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 2
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	S += c_aa_t3_t3 >= 2
	c_aa_t3_t3 += MAS[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=8, delay_cost=1)
	S += c_ab_t1_t0 >= 2
	c_ab_t1_t0 += MM[0]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=1, delay_cost=1)
	S += c_cc_a1_0 >= 2
	c_cc_a1_0 += MAS[3]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=1, delay_cost=1)
	S += c_cc_a1_1 >= 2
	c_cc_a1_1 += MAS[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 2
	c_cc_t3_t1_in += MM_in[0]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	S += c_aa_a1_1 >= 3
	c_aa_a1_1 += MAS[3]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 3
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 3
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	S += c_aa_t3_t2 >= 3
	c_aa_t3_t2 += MAS[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	S += c_bb_a1_0 >= 3
	c_bb_a1_0 += MAS[0]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=1, delay_cost=1)
	S += c_bb_t3_t2 >= 3
	c_bb_t3_t2 += MAS[2]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 3
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=8, delay_cost=1)
	S += c_cc_t3_t1 >= 3
	c_cc_t3_t1 += MM[0]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=8, delay_cost=1)
	S += c_aa_t3_t0 >= 4
	c_aa_t3_t0 += MM[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 4
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	S += c_ab_t0_t3 >= 4
	c_ab_t0_t3 += MAS[2]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	S += c_bb_a1_1 >= 4
	c_bb_a1_1 += MAS[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 4
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=1, delay_cost=1)
	S += c_bb_t3_t3 >= 4
	c_bb_t3_t3 += MAS[1]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 4
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	S += c_cc_t3_t3 >= 4
	c_cc_t3_t3 += MAS[3]

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	S += c_aa_t10 >= 5
	c_aa_t10 += MAS[1]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 5
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	S += c_ab_t0_t2 >= 5
	c_ab_t0_t2 += MAS[3]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 5
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t11 = S.Task('c_bb_t11', length=1, delay_cost=1)
	S += c_bb_t11 >= 5
	c_bb_t11 += MAS[2]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=8, delay_cost=1)
	S += c_bb_t3_t0 >= 5
	c_bb_t3_t0 += MM[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 5
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	S += c_cc_t10 >= 5
	c_cc_t10 += MAS[0]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 6
	c_aa_t3_t1_in += MM_in[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=8, delay_cost=1)
	S += c_ab_t0_t1 >= 6
	c_ab_t0_t1 += MM[0]

	c_ab_t21 = S.Task('c_ab_t21', length=1, delay_cost=1)
	S += c_ab_t21 >= 6
	c_ab_t21 += MAS[0]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=1, delay_cost=1)
	S += c_ac_t1_t3 >= 6
	c_ac_t1_t3 += MAS[2]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 6
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 6
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bc_t20 = S.Task('c_bc_t20', length=1, delay_cost=1)
	S += c_bc_t20 >= 6
	c_bc_t20 += MAS[3]

	c_bc_t21 = S.Task('c_bc_t21', length=1, delay_cost=1)
	S += c_bc_t21 >= 6
	c_bc_t21 += MAS[1]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 7
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=8, delay_cost=1)
	S += c_aa_t3_t1 >= 7
	c_aa_t3_t1 += MM[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 7
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=1, delay_cost=1)
	S += c_ab_t1_t2 >= 7
	c_ab_t1_t2 += MAS[1]

	c_ab_t20 = S.Task('c_ab_t20', length=1, delay_cost=1)
	S += c_ab_t20 >= 7
	c_ab_t20 += MAS[3]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=1, delay_cost=1)
	S += c_ac_t0_t2 >= 7
	c_ac_t0_t2 += MAS[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 7
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=1, delay_cost=1)
	S += c_bc_t0_t2 >= 7
	c_bc_t0_t2 += MAS[2]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 8
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=8, delay_cost=1)
	S += c_ab_t1_t1 >= 8
	c_ab_t1_t1 += MM[0]

	c_ac_t20 = S.Task('c_ac_t20', length=1, delay_cost=1)
	S += c_ac_t20 >= 8
	c_ac_t20 += MAS[1]

	c_ac_t31 = S.Task('c_ac_t31', length=1, delay_cost=1)
	S += c_ac_t31 >= 8
	c_ac_t31 += MAS[3]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=1, delay_cost=1)
	S += c_bc_t1_t2 >= 8
	c_bc_t1_t2 += MAS[2]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=1, delay_cost=1)
	S += c_bc_t1_t3 >= 8
	c_bc_t1_t3 += MAS[0]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 8
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 8
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 9
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 9
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t30 = S.Task('c_ab_t30', length=1, delay_cost=1)
	S += c_ab_t30 >= 9
	c_ab_t30 += MAS[0]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=1, delay_cost=1)
	S += c_ac_t1_t2 >= 9
	c_ac_t1_t2 += MAS[3]

	c_ac_t21 = S.Task('c_ac_t21', length=1, delay_cost=1)
	S += c_ac_t21 >= 9
	c_ac_t21 += MAS[2]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=1, delay_cost=1)
	S += c_bc_t0_t3 >= 9
	c_bc_t0_t3 += MAS[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=8, delay_cost=1)
	S += c_cc_t3_t0 >= 9
	c_cc_t3_t0 += MM[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 9
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=8, delay_cost=1)
	S += c_ab_t0_t0 >= 10
	c_ab_t0_t0 += MM[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 10
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=1, delay_cost=1)
	S += c_ac_t0_t3 >= 10
	c_ac_t0_t3 += MAS[3]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 10
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t30 = S.Task('c_ac_t30', length=1, delay_cost=1)
	S += c_ac_t30 >= 10
	c_ac_t30 += MAS[0]

	c_bc_t30 = S.Task('c_bc_t30', length=1, delay_cost=1)
	S += c_bc_t30 >= 10
	c_bc_t30 += MAS[2]

	c_bc_t31 = S.Task('c_bc_t31', length=1, delay_cost=1)
	S += c_bc_t31 >= 10
	c_bc_t31 += MAS[1]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 10
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 11
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 11
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=1, delay_cost=1)
	S += c_ab_t1_t3 >= 11
	c_ab_t1_t3 += MAS[3]

	c_ab_t31 = S.Task('c_ab_t31', length=1, delay_cost=1)
	S += c_ab_t31 >= 11
	c_ab_t31 += MAS[2]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=8, delay_cost=1)
	S += c_ac_t1_t0 >= 11
	c_ac_t1_t0 += MM[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 11
	c_bc_t1_t0_in += MM_in[0]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=1, delay_cost=1)
	S += c_pbc_t0_t3 >= 11
	c_pbc_t0_t3 += MAS[1]

	c_pcb_t30 = S.Task('c_pcb_t30', length=1, delay_cost=1)
	S += c_pcb_t30 >= 11
	c_pcb_t30 += MAS[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 12
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 12
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=8, delay_cost=1)
	S += c_bc_t1_t0 >= 12
	c_bc_t1_t0 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 12
	c_bc_t1_t1_in += MM_in[0]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=1, delay_cost=1)
	S += c_paa_t0_t3 >= 12
	c_paa_t0_t3 += MAS[0]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=1, delay_cost=1)
	S += c_paa_t1_t3 >= 12
	c_paa_t1_t3 += MAS[1]

	c_paa_t30 = S.Task('c_paa_t30', length=1, delay_cost=1)
	S += c_paa_t30 >= 12
	c_paa_t30 += MAS[2]

	c_paa_t31 = S.Task('c_paa_t31', length=1, delay_cost=1)
	S += c_paa_t31 >= 12
	c_paa_t31 += MAS[3]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 13
	c_ac_t0_t1_in += MM_in[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 13
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 13
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 13
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=8, delay_cost=1)
	S += c_bc_t1_t1 >= 13
	c_bc_t1_t1 += MM[0]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 13
	c_bc_t4_t3_mem0 += MAS_MEM[4]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 13
	c_bc_t4_t3_mem1 += MAS_MEM[3]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 13
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=1, delay_cost=1)
	S += c_pbc_t1_t3 >= 13
	c_pbc_t1_t3 += MAS[3]

	c_pbc_t30 = S.Task('c_pbc_t30', length=1, delay_cost=1)
	S += c_pbc_t30 >= 13
	c_pbc_t30 += MAS[2]

	c_pbc_t31 = S.Task('c_pbc_t31', length=1, delay_cost=1)
	S += c_pbc_t31 >= 13
	c_pbc_t31 += MAS[1]

	c_pcb_t31 = S.Task('c_pcb_t31', length=1, delay_cost=1)
	S += c_pcb_t31 >= 13
	c_pcb_t31 += MAS[0]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 14
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 14
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 14
	c_aa_t30_mem1 += MM_MEM[1]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 14
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 14
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=8, delay_cost=1)
	S += c_ac_t0_t1 >= 14
	c_ac_t0_t1 += MM[0]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 14
	c_bb_t2_t3_mem0 += MAS_MEM[2]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 14
	c_bb_t2_t3_mem1 += MAS_MEM[5]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=1, delay_cost=1)
	S += c_bb_t3_t5 >= 14
	c_bb_t3_t5 += MAS[1]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 14
	c_bc_t4_t2_mem0 += MAS_MEM[6]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 14
	c_bc_t4_t2_mem1 += MAS_MEM[3]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=1, delay_cost=1)
	S += c_bc_t4_t3 >= 14
	c_bc_t4_t3 += MAS[0]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=1, delay_cost=1)
	S += c_pcb_t0_t3 >= 14
	c_pcb_t0_t3 += MAS[3]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=1, delay_cost=1)
	S += c_pcb_t1_t3 >= 14
	c_pcb_t1_t3 += MAS[2]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 14
	c_pcb_t4_t3_mem0 += MAS_MEM[0]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 14
	c_pcb_t4_t3_mem1 += MAS_MEM[1]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 15
	c_aa_t2_t3_mem0 += MAS_MEM[2]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 15
	c_aa_t2_t3_mem1 += MAS_MEM[5]

	c_aa_t30 = S.Task('c_aa_t30', length=1, delay_cost=1)
	S += c_aa_t30 >= 15
	c_aa_t30 += MAS[1]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 15
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 15
	c_ab_t10_mem1 += MM_MEM[1]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 15
	c_ab_t4_t2_mem0 += MAS_MEM[6]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 15
	c_ab_t4_t2_mem1 += MAS_MEM[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=8, delay_cost=1)
	S += c_ac_t0_t0 >= 15
	c_ac_t0_t0 += MM[0]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 15
	c_ac_t1_t1_in += MM_in[0]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=1, delay_cost=1)
	S += c_bb_t2_t3 >= 15
	c_bb_t2_t3 += MAS[0]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=1, delay_cost=1)
	S += c_bc_t4_t2 >= 15
	c_bc_t4_t2 += MAS[2]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 15
	c_cc_t2_t3_mem0 += MAS_MEM[0]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 15
	c_cc_t2_t3_mem1 += MAS_MEM[7]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 15
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 15
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=1, delay_cost=1)
	S += c_pcb_t4_t3 >= 15
	c_pcb_t4_t3 += MAS[3]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=1, delay_cost=1)
	S += c_aa_t2_t3 >= 16
	c_aa_t2_t3 += MAS[1]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 16
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 16
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 16
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t10 = S.Task('c_ab_t10', length=1, delay_cost=1)
	S += c_ab_t10 >= 16
	c_ab_t10 += MAS[0]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=1, delay_cost=1)
	S += c_ab_t4_t2 >= 16
	c_ab_t4_t2 += MAS[2]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=8, delay_cost=1)
	S += c_ac_t1_t1 >= 16
	c_ac_t1_t1 += MM[0]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 16
	c_ac_t4_t2_mem0 += MAS_MEM[2]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 16
	c_ac_t4_t2_mem1 += MAS_MEM[5]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 16
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 16
	c_ac_t4_t3_mem1 += MAS_MEM[7]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 16
	c_bb_t01_mem1 += MAS_MEM[1]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 16
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 16
	c_bc_t0_t0_in += MM_in[0]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=1, delay_cost=1)
	S += c_cc_t2_t3 >= 16
	c_cc_t2_t3 += MAS[3]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 17
	c_aa_t01_mem1 += MAS_MEM[7]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=1, delay_cost=1)
	S += c_aa_t3_t5 >= 17
	c_aa_t3_t5 += MAS[3]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 17
	c_ab_t4_t3_mem0 += MAS_MEM[0]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 17
	c_ab_t4_t3_mem1 += MAS_MEM[5]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=1, delay_cost=1)
	S += c_ac_t4_t2 >= 17
	c_ac_t4_t2 += MAS[1]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=1, delay_cost=1)
	S += c_ac_t4_t3 >= 17
	c_ac_t4_t3 += MAS[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 17
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_t01 = S.Task('c_bb_t01', length=1, delay_cost=1)
	S += c_bb_t01 >= 17
	c_bb_t01 += MAS[2]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 17
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 17
	c_bb_t30_mem1 += MM_MEM[1]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 17
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=8, delay_cost=1)
	S += c_bc_t0_t0 >= 17
	c_bc_t0_t0 += MM[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 17
	c_bc_t0_t1_in += MM_in[0]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 17
	c_cc_t01_mem1 += MAS_MEM[1]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 18
	c_aa_t00_mem1 += MAS_MEM[1]

	c_aa_t01 = S.Task('c_aa_t01', length=1, delay_cost=1)
	S += c_aa_t01 >= 18
	c_aa_t01 += MAS[3]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 18
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 18
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=1, delay_cost=1)
	S += c_ab_t4_t3 >= 18
	c_ab_t4_t3 += MAS[0]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 18
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 18
	c_ac_t1_t4_mem0 += MAS_MEM[6]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 18
	c_ac_t1_t4_mem1 += MAS_MEM[5]

	c_bb_t30 = S.Task('c_bb_t30', length=1, delay_cost=1)
	S += c_bb_t30 >= 18
	c_bb_t30 += MAS[1]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=8, delay_cost=1)
	S += c_bc_t0_t1 >= 18
	c_bc_t0_t1 += MM[0]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 18
	c_cc_t00_mem1 += MAS_MEM[7]

	c_cc_t01 = S.Task('c_cc_t01', length=1, delay_cost=1)
	S += c_cc_t01 >= 18
	c_cc_t01 += MAS[2]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 18
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 18
	c_cc_t30_mem1 += MM_MEM[1]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 18
	c_pbc_t4_t3_mem0 += MAS_MEM[4]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 18
	c_pbc_t4_t3_mem1 += MAS_MEM[3]

	c_aa_t00 = S.Task('c_aa_t00', length=1, delay_cost=1)
	S += c_aa_t00 >= 19
	c_aa_t00 += MAS[1]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 19
	c_aa_t2_t2_mem0 += MAS_MEM[2]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 19
	c_aa_t2_t2_mem1 += MAS_MEM[7]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 19
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 19
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 19
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=8, delay_cost=1)
	S += c_ac_t1_t4 >= 19
	c_ac_t1_t4 += MM[0]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 19
	c_bb_t00_mem1 += MAS_MEM[1]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 19
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 19
	c_bb_t3_t4_mem0 += MAS_MEM[4]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 19
	c_bb_t3_t4_mem1 += MAS_MEM[3]

	c_cc_t00 = S.Task('c_cc_t00', length=1, delay_cost=1)
	S += c_cc_t00 >= 19
	c_cc_t00 += MAS[3]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 19
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 19
	c_cc_t2_t2_mem0 += MAS_MEM[6]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 19
	c_cc_t2_t2_mem1 += MAS_MEM[5]

	c_cc_t30 = S.Task('c_cc_t30', length=1, delay_cost=1)
	S += c_cc_t30 >= 19
	c_cc_t30 += MAS[2]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=1, delay_cost=1)
	S += c_pbc_t4_t3 >= 19
	c_pbc_t4_t3 += MAS[0]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=1, delay_cost=1)
	S += c_aa_t2_t2 >= 20
	c_aa_t2_t2 += MAS[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 20
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=1, delay_cost=1)
	S += c_ab_t1_t5 >= 20
	c_ab_t1_t5 += MAS[2]

	c_bb_t00 = S.Task('c_bb_t00', length=1, delay_cost=1)
	S += c_bb_t00 >= 20
	c_bb_t00 += MAS[1]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=8, delay_cost=1)
	S += c_bb_t3_t4 >= 20
	c_bb_t3_t4 += MM[0]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 20
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 20
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 20
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 20
	c_bc_t4_t1_mem0 += MAS_MEM[2]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 20
	c_bc_t4_t1_mem1 += MAS_MEM[3]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 20
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=1, delay_cost=1)
	S += c_cc_t2_t2 >= 20
	c_cc_t2_t2 += MAS[3]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 20
	c_paa_t4_t3_mem0 += MAS_MEM[4]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 20
	c_paa_t4_t3_mem1 += MAS_MEM[7]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 21
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 21
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 21
	c_ab_t00_mem1 += MM_MEM[1]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 21
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 21
	c_ab_t1_t4_mem0 += MAS_MEM[2]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 21
	c_ab_t1_t4_mem1 += MAS_MEM[7]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 21
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=1, delay_cost=1)
	S += c_bc_t1_t5 >= 21
	c_bc_t1_t5 += MAS[0]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=8, delay_cost=1)
	S += c_bc_t4_t1 >= 21
	c_bc_t4_t1 += MM[0]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 21
	c_cc10_mem0 += MAS_MEM[4]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=1, delay_cost=1)
	S += c_paa_t4_t3 >= 21
	c_paa_t4_t3 += MAS[2]

	c_ab_t00 = S.Task('c_ab_t00', length=1, delay_cost=1)
	S += c_ab_t00 >= 22
	c_ab_t00 += MAS[1]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=8, delay_cost=1)
	S += c_ab_t1_t4 >= 22
	c_ab_t1_t4 += MM[0]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 22
	c_ab_t50_mem0 += MAS_MEM[2]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 22
	c_ab_t50_mem1 += MAS_MEM[1]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 22
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 22
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 22
	c_bc_t10_mem1 += MM_MEM[1]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 22
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 22
	c_bc_t4_t0_mem0 += MAS_MEM[6]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 22
	c_bc_t4_t0_mem1 += MAS_MEM[5]

	c_cc10 = S.Task('c_cc10', length=1, delay_cost=1)
	S += c_cc10 >= 22
	c_cc10 += MAS[2]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 22
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 23
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 23
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t50 = S.Task('c_ab_t50', length=1, delay_cost=1)
	S += c_ab_t50 >= 23
	c_ab_t50 += MAS[1]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 23
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 23
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 23
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 23
	c_ac_t4_t1_mem0 += MAS_MEM[4]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 23
	c_ac_t4_t1_mem1 += MAS_MEM[7]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 23
	c_bb_t2_t2_mem0 += MAS_MEM[2]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 23
	c_bb_t2_t2_mem1 += MAS_MEM[5]

	c_bc_t10 = S.Task('c_bc_t10', length=1, delay_cost=1)
	S += c_bc_t10 >= 23
	c_bc_t10 += MAS[0]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=8, delay_cost=1)
	S += c_bc_t4_t0 >= 23
	c_bc_t4_t0 += MM[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 24
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 24
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 24
	c_ac_t00_mem1 += MM_MEM[1]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=1, delay_cost=1)
	S += c_ac_t0_t5 >= 24
	c_ac_t0_t5 += MAS[1]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 24
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 24
	c_ac_t4_t0_mem0 += MAS_MEM[2]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 24
	c_ac_t4_t0_mem1 += MAS_MEM[1]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=8, delay_cost=1)
	S += c_ac_t4_t1 >= 24
	c_ac_t4_t1 += MM[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 24
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=1, delay_cost=1)
	S += c_bb_t2_t2 >= 24
	c_bb_t2_t2 += MAS[0]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 25
	c_aa10_mem0 += MAS_MEM[2]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 25
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 25
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t00 = S.Task('c_ac_t00', length=1, delay_cost=1)
	S += c_ac_t00 >= 25
	c_ac_t00 += MAS[1]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 25
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 25
	c_ac_t10_mem1 += MM_MEM[1]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=8, delay_cost=1)
	S += c_ac_t4_t0 >= 25
	c_ac_t4_t0 += MM[0]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 25
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 25
	c_bc_t1_t4_mem0 += MAS_MEM[4]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 25
	c_bc_t1_t4_mem1 += MAS_MEM[1]

	c_aa10 = S.Task('c_aa10', length=1, delay_cost=1)
	S += c_aa10 >= 26
	c_aa10 += MAS[2]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 26
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 26
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 26
	c_ab_t4_t1_mem0 += MAS_MEM[0]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 26
	c_ab_t4_t1_mem1 += MAS_MEM[5]

	c_ac_t10 = S.Task('c_ac_t10', length=1, delay_cost=1)
	S += c_ac_t10 >= 26
	c_ac_t10 += MAS[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 26
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 26
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 26
	c_ac_t50_mem0 += MAS_MEM[2]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 26
	c_ac_t50_mem1 += MAS_MEM[1]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 26
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=8, delay_cost=1)
	S += c_bc_t1_t4 >= 26
	c_bc_t1_t4 += MM[0]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 27
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=8, delay_cost=1)
	S += c_ab_t4_t1 >= 27
	c_ab_t4_t1 += MM[0]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=1, delay_cost=1)
	S += c_ac_t1_t5 >= 27
	c_ac_t1_t5 += MAS[2]

	c_ac_t50 = S.Task('c_ac_t50', length=1, delay_cost=1)
	S += c_ac_t50 >= 27
	c_ac_t50 += MAS[0]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 27
	c_bb10_mem0 += MAS_MEM[2]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 27
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 27
	c_bc_t0_t4_mem0 += MAS_MEM[4]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 27
	c_bc_t0_t4_mem1 += MAS_MEM[3]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 27
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 27
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 27
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 28
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 28
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 28
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 28
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 28
	c_ac_t0_t4_mem0 += MAS_MEM[0]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 28
	c_ac_t0_t4_mem1 += MAS_MEM[7]

	c_bb10 = S.Task('c_bb10', length=1, delay_cost=1)
	S += c_bb10 >= 28
	c_bb10 += MAS[0]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=8, delay_cost=1)
	S += c_bc_t0_t4 >= 28
	c_bc_t0_t4 += MM[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 28
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=1, delay_cost=1)
	S += c_cc_t3_t5 >= 28
	c_cc_t3_t5 += MAS[3]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 29
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 29
	c_aa_t3_t4_mem0 += MAS_MEM[2]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 29
	c_aa_t3_t4_mem1 += MAS_MEM[3]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=1, delay_cost=1)
	S += c_ab_t0_t5 >= 29
	c_ab_t0_t5 += MAS[1]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=8, delay_cost=1)
	S += c_ac_t0_t4 >= 29
	c_ac_t0_t4 += MM[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 29
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 29
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 29
	c_bc_t00_mem1 += MM_MEM[1]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 29
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=8, delay_cost=1)
	S += c_aa_t3_t4 >= 30
	c_aa_t3_t4 += MM[0]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 30
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 30
	c_ab_t0_t4_mem0 += MAS_MEM[6]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 30
	c_ab_t0_t4_mem1 += MAS_MEM[5]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 30
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t00 = S.Task('c_bc_t00', length=1, delay_cost=1)
	S += c_bc_t00 >= 30
	c_bc_t00 += MAS[1]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 30
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 30
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 30
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 30
	c_bc_t50_mem0 += MAS_MEM[2]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 30
	c_bc_t50_mem1 += MAS_MEM[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=8, delay_cost=1)
	S += c_ab_t0_t4 >= 31
	c_ab_t0_t4 += MM[0]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 31
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 31
	c_ab_t11_mem1 += MAS_MEM[5]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 31
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 31
	c_ab_t4_t0_mem0 += MAS_MEM[6]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 31
	c_ab_t4_t0_mem1 += MAS_MEM[1]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 31
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 31
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=1, delay_cost=1)
	S += c_bc_t0_t5 >= 31
	c_bc_t0_t5 += MAS[3]

	c_bc_t50 = S.Task('c_bc_t50', length=1, delay_cost=1)
	S += c_bc_t50 >= 31
	c_bc_t50 += MAS[0]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 32
	c_ab_s00_mem0 += MAS_MEM[0]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 32
	c_ab_s00_mem1 += MAS_MEM[3]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 32
	c_ab_s01_mem0 += MAS_MEM[2]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 32
	c_ab_s01_mem1 += MAS_MEM[1]

	c_ab_t11 = S.Task('c_ab_t11', length=1, delay_cost=1)
	S += c_ab_t11 >= 32
	c_ab_t11 += MAS[1]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 32
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=8, delay_cost=1)
	S += c_ab_t4_t0 >= 32
	c_ab_t4_t0 += MM[0]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 32
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 32
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 32
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 32
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 32
	c_cc_t3_t4_mem0 += MAS_MEM[4]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 32
	c_cc_t3_t4_mem1 += MAS_MEM[7]

	c_ab_s00 = S.Task('c_ab_s00', length=1, delay_cost=1)
	S += c_ab_s00 >= 33
	c_ab_s00 += MAS[0]

	c_ab_s01 = S.Task('c_ab_s01', length=1, delay_cost=1)
	S += c_ab_s01 >= 33
	c_ab_s01 += MAS[2]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 33
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 33
	c_ac_t4_t4_mem0 += MAS_MEM[2]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 33
	c_ac_t4_t4_mem1 += MAS_MEM[1]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=1, delay_cost=1)
	S += c_ac_t4_t5 >= 33
	c_ac_t4_t5 += MAS[3]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 33
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 33
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 33
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 33
	c_bc_t40_mem1 += MM_MEM[1]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=8, delay_cost=1)
	S += c_cc_t3_t4 >= 33
	c_cc_t3_t4 += MM[0]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 34
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 34
	c_ac_t11_mem1 += MAS_MEM[5]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 34
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=8, delay_cost=1)
	S += c_ac_t4_t4 >= 34
	c_ac_t4_t4 += MM[0]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 34
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t40 = S.Task('c_bc_t40', length=1, delay_cost=1)
	S += c_bc_t40 >= 34
	c_bc_t40 += MAS[2]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 34
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 34
	c_bc_t4_t4_mem0 += MAS_MEM[4]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 34
	c_bc_t4_t4_mem1 += MAS_MEM[1]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 35
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t11 = S.Task('c_ac_t11', length=1, delay_cost=1)
	S += c_ac_t11 >= 35
	c_ac_t11 += MAS[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 35
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 35
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 35
	c_bb_t2_t1_mem0 += MAS_MEM[4]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 35
	c_bb_t2_t1_mem1 += MAS_MEM[5]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 35
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 35
	c_bc_t11_mem1 += MAS_MEM[1]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=8, delay_cost=1)
	S += c_bc_t4_t4 >= 35
	c_bc_t4_t4 += MM[0]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 36
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 36
	c_ab_t4_t4_mem0 += MAS_MEM[4]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 36
	c_ab_t4_t4_mem1 += MAS_MEM[1]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 36
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=8, delay_cost=1)
	S += c_bb_t2_t1 >= 36
	c_bb_t2_t1 += MM[0]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 36
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 36
	c_bc_t01_mem1 += MAS_MEM[7]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 36
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t11 = S.Task('c_bc_t11', length=1, delay_cost=1)
	S += c_bc_t11 >= 36
	c_bc_t11 += MAS[0]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 37
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 37
	c_aa_t2_t1_mem0 += MAS_MEM[6]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 37
	c_aa_t2_t1_mem1 += MAS_MEM[5]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 37
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 37
	c_aa_t31_mem1 += MAS_MEM[7]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 37
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=8, delay_cost=1)
	S += c_ab_t4_t4 >= 37
	c_ab_t4_t4 += MM[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 37
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 37
	c_bc_s01_mem0 += MAS_MEM[0]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 37
	c_bc_s01_mem1 += MAS_MEM[1]

	c_bc_t01 = S.Task('c_bc_t01', length=1, delay_cost=1)
	S += c_bc_t01 >= 37
	c_bc_t01 += MAS[0]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=8, delay_cost=1)
	S += c_aa_t2_t1 >= 38
	c_aa_t2_t1 += MM[0]

	c_aa_t31 = S.Task('c_aa_t31', length=1, delay_cost=1)
	S += c_aa_t31 >= 38
	c_aa_t31 += MAS[1]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 38
	c_aa_t41_mem0 += MAS_MEM[2]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 38
	c_aa_t41_mem1 += MAS_MEM[3]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 38
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_bc_s01 = S.Task('c_bc_s01', length=1, delay_cost=1)
	S += c_bc_s01 >= 38
	c_bc_s01 += MAS[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 38
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 38
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 38
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 38
	c_bc_t51_mem0 += MAS_MEM[0]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 38
	c_bc_t51_mem1 += MAS_MEM[1]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 38
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 38
	c_cc_t2_t1_mem0 += MAS_MEM[4]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 38
	c_cc_t2_t1_mem1 += MAS_MEM[7]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 39
	c_aa11_mem0 += MAS_MEM[2]

	c_aa_t41 = S.Task('c_aa_t41', length=1, delay_cost=1)
	S += c_aa_t41 >= 39
	c_aa_t41 += MAS[1]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 39
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 39
	c_ac_t01_mem1 += MAS_MEM[3]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 39
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 39
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=1, delay_cost=1)
	S += c_bc_t4_t5 >= 39
	c_bc_t4_t5 += MAS[0]

	c_bc_t51 = S.Task('c_bc_t51', length=1, delay_cost=1)
	S += c_bc_t51 >= 39
	c_bc_t51 += MAS[2]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 39
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 39
	c_cc_t2_t0_mem0 += MAS_MEM[6]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 39
	c_cc_t2_t0_mem1 += MAS_MEM[1]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=8, delay_cost=1)
	S += c_cc_t2_t1 >= 39
	c_cc_t2_t1 += MM[0]

	c_aa11 = S.Task('c_aa11', length=1, delay_cost=1)
	S += c_aa11 >= 40
	c_aa11 += MAS[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 40
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 40
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 40
	c_ac_s00_mem0 += MAS_MEM[0]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 40
	c_ac_s00_mem1 += MAS_MEM[1]

	c_ac_t01 = S.Task('c_ac_t01', length=1, delay_cost=1)
	S += c_ac_t01 >= 40
	c_ac_t01 += MAS[2]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 40
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 40
	c_bb_t2_t0_mem0 += MAS_MEM[2]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 40
	c_bb_t2_t0_mem1 += MAS_MEM[3]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=8, delay_cost=1)
	S += c_cc_t2_t0 >= 40
	c_cc_t2_t0 += MM[0]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 40
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 40
	c_cc_t31_mem1 += MAS_MEM[7]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 41
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 41
	c_aa_t2_t0_mem0 += MAS_MEM[2]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 41
	c_aa_t2_t0_mem1 += MAS_MEM[3]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 41
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 41
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ac_s00 = S.Task('c_ac_s00', length=1, delay_cost=1)
	S += c_ac_s00 >= 41
	c_ac_s00 += MAS[3]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 41
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=8, delay_cost=1)
	S += c_bb_t2_t0 >= 41
	c_bb_t2_t0 += MM[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 41
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_cc_t31 = S.Task('c_cc_t31', length=1, delay_cost=1)
	S += c_cc_t31 >= 41
	c_cc_t31 += MAS[0]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 41
	c_cc_t40_mem0 += MAS_MEM[4]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 41
	c_cc_t40_mem1 += MAS_MEM[1]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 41
	c_cc_t41_mem0 += MAS_MEM[0]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 41
	c_cc_t41_mem1 += MAS_MEM[5]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=8, delay_cost=1)
	S += c_aa_t2_t0 >= 42
	c_aa_t2_t0 += MM[0]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 42
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 42
	c_ab_t01_mem1 += MAS_MEM[3]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=1, delay_cost=1)
	S += c_ab_t4_t5 >= 42
	c_ab_t4_t5 += MAS[1]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 42
	c_ac_t51_mem0 += MAS_MEM[4]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 42
	c_ac_t51_mem1 += MAS_MEM[1]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 42
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 42
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 42
	c_cc11_mem0 += MAS_MEM[0]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 42
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 42
	c_cc_t2_t4_mem0 += MAS_MEM[6]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 42
	c_cc_t2_t4_mem1 += MAS_MEM[7]

	c_cc_t40 = S.Task('c_cc_t40', length=1, delay_cost=1)
	S += c_cc_t40 >= 42
	c_cc_t40 += MAS[3]

	c_cc_t41 = S.Task('c_cc_t41', length=1, delay_cost=1)
	S += c_cc_t41 >= 42
	c_cc_t41 += MAS[0]

	c_ab_t01 = S.Task('c_ab_t01', length=1, delay_cost=1)
	S += c_ab_t01 >= 43
	c_ab_t01 += MAS[3]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 43
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t51 = S.Task('c_ac_t51', length=1, delay_cost=1)
	S += c_ac_t51 >= 43
	c_ac_t51 += MAS[2]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 43
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 43
	c_bb_t2_t4_mem0 += MAS_MEM[0]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 43
	c_bb_t2_t4_mem1 += MAS_MEM[1]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 43
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 43
	c_bb_t31_mem1 += MAS_MEM[3]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 43
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_cc11 = S.Task('c_cc11', length=1, delay_cost=1)
	S += c_cc11 >= 43
	c_cc11 += MAS[1]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=8, delay_cost=1)
	S += c_cc_t2_t4 >= 43
	c_cc_t2_t4 += MM[0]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	S += c_cc_t50_mem0 >= 43
	c_cc_t50_mem0 += MAS_MEM[4]

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	S += c_cc_t50_mem1 >= 43
	c_cc_t50_mem1 += MAS_MEM[7]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem0 >= 43
	c_ccxi_y1_1_mem0 += MAS_MEM[2]

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem1 >= 43
	c_ccxi_y1_1_mem1 += MAS_MEM[5]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 44
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 44
	c_aa_t2_t4_mem0 += MAS_MEM[0]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 44
	c_aa_t2_t4_mem1 += MAS_MEM[3]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	S += c_ab01_mem0 >= 44
	c_ab01_mem0 += MAS_MEM[6]

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	S += c_ab01_mem1 >= 44
	c_ab01_mem1 += MAS_MEM[5]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 44
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 44
	c_ab_t40_mem1 += MM_MEM[1]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 44
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 44
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 44
	c_bb11_mem0 += MAS_MEM[2]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=8, delay_cost=1)
	S += c_bb_t2_t4 >= 44
	c_bb_t2_t4 += MM[0]

	c_bb_t31 = S.Task('c_bb_t31', length=1, delay_cost=1)
	S += c_bb_t31 >= 44
	c_bb_t31 += MAS[1]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 44
	c_bc10_mem0 += MAS_MEM[4]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 44
	c_bc10_mem1 += MAS_MEM[1]

	c_cc_t50 = S.Task('c_cc_t50', length=1, delay_cost=1)
	S += c_cc_t50 >= 44
	c_cc_t50 += MAS[2]

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=1, delay_cost=1)
	S += c_ccxi_y1_1 >= 44
	c_ccxi_y1_1 += MAS[3]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=8, delay_cost=1)
	S += c_aa_t2_t4 >= 45
	c_aa_t2_t4 += MM[0]

	c_ab01 = S.Task('c_ab01', length=1, delay_cost=1)
	S += c_ab01 >= 45
	c_ab01 += MAS[3]

	c_ab_t40 = S.Task('c_ab_t40', length=1, delay_cost=1)
	S += c_ab_t40 >= 45
	c_ab_t40 += MAS[0]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 45
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 45
	c_ac_t40_mem1 += MM_MEM[1]

	c_bb11 = S.Task('c_bb11', length=1, delay_cost=1)
	S += c_bb11 >= 45
	c_bb11 += MAS[1]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 45
	c_bb_t41_mem0 += MAS_MEM[2]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 45
	c_bb_t41_mem1 += MAS_MEM[3]

	c_bc10 = S.Task('c_bc10', length=1, delay_cost=1)
	S += c_bc10 >= 45
	c_bc10 += MAS[2]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 45
	c_bc_s00_mem0 += MAS_MEM[0]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 45
	c_bc_s00_mem1 += MAS_MEM[1]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 45
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 45
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	S += c_pb01_mem0 >= 45
	c_pb01_mem0 += MAS_MEM[6]

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	S += c_pb01_mem1 >= 45
	c_pb01_mem1 += MAS_MEM[7]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 46
	c_aa_t40_mem0 += MAS_MEM[2]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 46
	c_aa_t40_mem1 += MAS_MEM[3]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 46
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 46
	c_ac10_mem0 += MAS_MEM[6]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 46
	c_ac10_mem1 += MAS_MEM[1]

	c_ac_t40 = S.Task('c_ac_t40', length=1, delay_cost=1)
	S += c_ac_t40 >= 46
	c_ac_t40 += MAS[3]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 46
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 46
	c_ac_t41_mem1 += MAS_MEM[7]

	c_bb_t41 = S.Task('c_bb_t41', length=1, delay_cost=1)
	S += c_bb_t41 >= 46
	c_bb_t41 += MAS[0]

	c_bc_s00 = S.Task('c_bc_s00', length=1, delay_cost=1)
	S += c_bc_s00 >= 46
	c_bc_s00 += MAS[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 46
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_pb01 = S.Task('c_pb01', length=1, delay_cost=1)
	S += c_pb01 >= 46
	c_pb01 += MAS[2]

	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	S += c_pbc_t0_t1_in >= 46
	c_pbc_t0_t1_in += MM_in[0]

	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem0 >= 46
	c_pbc_t0_t1_mem0 += MAS_MEM[4]

	c_aa_t40 = S.Task('c_aa_t40', length=1, delay_cost=1)
	S += c_aa_t40 >= 47
	c_aa_t40 += MAS[3]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	S += c_aa_t50_mem0 >= 47
	c_aa_t50_mem0 += MAS_MEM[2]

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	S += c_aa_t50_mem1 >= 47
	c_aa_t50_mem1 += MAS_MEM[7]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 47
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 47
	c_ab_t51_mem0 += MAS_MEM[6]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 47
	c_ab_t51_mem1 += MAS_MEM[3]

	c_ac10 = S.Task('c_ac10', length=1, delay_cost=1)
	S += c_ac10 >= 47
	c_ac10 += MAS[0]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 47
	c_ac_s01_mem0 += MAS_MEM[0]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 47
	c_ac_s01_mem1 += MAS_MEM[1]

	c_ac_t41 = S.Task('c_ac_t41', length=1, delay_cost=1)
	S += c_ac_t41 >= 47
	c_ac_t41 += MAS[1]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 47
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 47
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 47
	c_cc_t2_t5_mem1 += MM_MEM[1]

	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=8, delay_cost=1)
	S += c_pbc_t0_t1 >= 47
	c_pbc_t0_t1 += MM[0]

	c_aa_t50 = S.Task('c_aa_t50', length=1, delay_cost=1)
	S += c_aa_t50 >= 48
	c_aa_t50 += MAS[1]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 48
	c_ab10_mem0 += MAS_MEM[0]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 48
	c_ab10_mem1 += MAS_MEM[3]

	c_ab_t51 = S.Task('c_ab_t51', length=1, delay_cost=1)
	S += c_ab_t51 >= 48
	c_ab_t51 += MAS[2]

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	S += c_ac01_mem0 >= 48
	c_ac01_mem0 += MAS_MEM[4]

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	S += c_ac01_mem1 >= 48
	c_ac01_mem1 += MAS_MEM[1]

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	S += c_ac11_mem0 >= 48
	c_ac11_mem0 += MAS_MEM[2]

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	S += c_ac11_mem1 >= 48
	c_ac11_mem1 += MAS_MEM[5]

	c_ac_s01 = S.Task('c_ac_s01', length=1, delay_cost=1)
	S += c_ac_s01 >= 48
	c_ac_s01 += MAS[0]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 48
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 48
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 48
	c_bb_t2_t5_mem1 += MM_MEM[1]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 48
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=1, delay_cost=1)
	S += c_cc_t2_t5 >= 48
	c_cc_t2_t5 += MAS[3]

	c_ab10 = S.Task('c_ab10', length=1, delay_cost=1)
	S += c_ab10 >= 49
	c_ab10 += MAS[2]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 49
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ac01 = S.Task('c_ac01', length=1, delay_cost=1)
	S += c_ac01 >= 49
	c_ac01 += MAS[0]

	c_ac11 = S.Task('c_ac11', length=1, delay_cost=1)
	S += c_ac11 >= 49
	c_ac11 += MAS[3]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 49
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 49
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 49
	c_bb_t20_mem1 += MM_MEM[1]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=1, delay_cost=1)
	S += c_bb_t2_t5 >= 49
	c_bb_t2_t5 += MAS[1]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 49
	c_bb_t40_mem0 += MAS_MEM[2]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 49
	c_bb_t40_mem1 += MAS_MEM[3]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	S += c_bc01_mem0 >= 49
	c_bc01_mem0 += MAS_MEM[0]

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	S += c_bc01_mem1 >= 49
	c_bc01_mem1 += MAS_MEM[1]

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	S += c_ab00_mem0 >= 50
	c_ab00_mem0 += MAS_MEM[2]

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	S += c_ab00_mem1 >= 50
	c_ab00_mem1 += MAS_MEM[1]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 50
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_bb_t20 = S.Task('c_bb_t20', length=1, delay_cost=1)
	S += c_bb_t20 >= 50
	c_bb_t20 += MAS[3]

	c_bb_t40 = S.Task('c_bb_t40', length=1, delay_cost=1)
	S += c_bb_t40 >= 50
	c_bb_t40 += MAS[0]

	c_bc01 = S.Task('c_bc01', length=1, delay_cost=1)
	S += c_bc01 >= 50
	c_bc01 += MAS[2]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 50
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 50
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 50
	c_cc_t20_mem1 += MM_MEM[1]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem0 >= 50
	c_ccxi_y1_0_mem0 += MAS_MEM[4]

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem1 >= 50
	c_ccxi_y1_0_mem1 += MAS_MEM[3]

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	S += c_pa11_mem0 >= 50
	c_pa11_mem0 += MAS_MEM[0]

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	S += c_pa11_mem1 >= 50
	c_pa11_mem1 += MAS_MEM[5]

	c_ab00 = S.Task('c_ab00', length=1, delay_cost=1)
	S += c_ab00 >= 51
	c_ab00 += MAS[1]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 51
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 51
	c_ab_t41_mem1 += MAS_MEM[3]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 51
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 51
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	S += c_cc00_mem0 >= 51
	c_cc00_mem0 += MAS_MEM[6]

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	S += c_cc00_mem1 >= 51
	c_cc00_mem1 += MAS_MEM[5]

	c_cc_t20 = S.Task('c_cc_t20', length=1, delay_cost=1)
	S += c_cc_t20 >= 51
	c_cc_t20 += MAS[3]

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=1, delay_cost=1)
	S += c_ccxi_y1_0 >= 51
	c_ccxi_y1_0 += MAS[0]

	c_pa11 = S.Task('c_pa11', length=1, delay_cost=1)
	S += c_pa11 >= 51
	c_pa11 += MAS[2]

	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	S += c_paa_t1_t1_in >= 51
	c_paa_t1_t1_in += MM_in[0]

	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t1_mem0 >= 51
	c_paa_t1_t1_mem0 += MAS_MEM[4]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	S += c_pc10_mem0 >= 51
	c_pc10_mem0 += MAS_MEM[0]

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	S += c_pc10_mem1 >= 51
	c_pc10_mem1 += MAS_MEM[1]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	S += c_pc11_mem0 >= 51
	c_pc11_mem0 += MAS_MEM[2]

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	S += c_pc11_mem1 >= 51
	c_pc11_mem1 += MAS_MEM[7]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 52
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t41 = S.Task('c_ab_t41', length=1, delay_cost=1)
	S += c_ab_t41 >= 52
	c_ab_t41 += MAS[1]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	S += c_ac00_mem0 >= 52
	c_ac00_mem0 += MAS_MEM[2]

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	S += c_ac00_mem1 >= 52
	c_ac00_mem1 += MAS_MEM[7]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 52
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 52
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 52
	c_bc_t41_mem1 += MAS_MEM[1]

	c_cc00 = S.Task('c_cc00', length=1, delay_cost=1)
	S += c_cc00 >= 52
	c_cc00 += MAS[3]

	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=8, delay_cost=1)
	S += c_paa_t1_t1 >= 52
	c_paa_t1_t1 += MM[0]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	S += c_pb00_mem0 >= 52
	c_pb00_mem0 += MAS_MEM[0]

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	S += c_pb00_mem1 >= 52
	c_pb00_mem1 += MAS_MEM[3]

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	S += c_pb10_mem0 >= 52
	c_pb10_mem0 += MAS_MEM[6]

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	S += c_pb10_mem1 >= 52
	c_pb10_mem1 += MAS_MEM[5]

	c_pc10 = S.Task('c_pc10', length=1, delay_cost=1)
	S += c_pc10 >= 52
	c_pc10 += MAS[2]

	c_pc11 = S.Task('c_pc11', length=1, delay_cost=1)
	S += c_pc11 >= 52
	c_pc11 += MAS[0]

	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	S += c_pcb_t1_t0_in >= 52
	c_pcb_t1_t0_in += MM_in[0]

	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem0 >= 52
	c_pcb_t1_t0_mem0 += MAS_MEM[4]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 53
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 53
	c_aa_t2_t5_mem1 += MM_MEM[1]

	c_ac00 = S.Task('c_ac00', length=1, delay_cost=1)
	S += c_ac00 >= 53
	c_ac00 += MAS[2]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 53
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	S += c_bc00_mem0 >= 53
	c_bc00_mem0 += MAS_MEM[2]

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	S += c_bc00_mem1 >= 53
	c_bc00_mem1 += MAS_MEM[3]

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	S += c_bc11_mem0 >= 53
	c_bc11_mem0 += MAS_MEM[0]

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	S += c_bc11_mem1 >= 53
	c_bc11_mem1 += MAS_MEM[5]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 53
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t41 = S.Task('c_bc_t41', length=1, delay_cost=1)
	S += c_bc_t41 >= 53
	c_bc_t41 += MAS[0]

	c_pb00 = S.Task('c_pb00', length=1, delay_cost=1)
	S += c_pb00 >= 53
	c_pb00 += MAS[3]

	c_pb10 = S.Task('c_pb10', length=1, delay_cost=1)
	S += c_pb10 >= 53
	c_pb10 += MAS[1]

	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	S += c_pbc_t0_t0_in >= 53
	c_pbc_t0_t0_in += MM_in[0]

	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem0 >= 53
	c_pbc_t0_t0_mem0 += MAS_MEM[6]

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=8, delay_cost=1)
	S += c_pcb_t1_t0 >= 53
	c_pcb_t1_t0 += MM[0]

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem0 >= 53
	c_pcb_t1_t2_mem0 += MAS_MEM[4]

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem1 >= 53
	c_pcb_t1_t2_mem1 += MAS_MEM[1]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 54
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 54
	c_aa_t20_mem1 += MM_MEM[1]

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=1, delay_cost=1)
	S += c_aa_t2_t5 >= 54
	c_aa_t2_t5 += MAS[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 54
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 54
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	S += c_bb_t51_mem0 >= 54
	c_bb_t51_mem0 += MAS_MEM[2]

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	S += c_bb_t51_mem1 >= 54
	c_bb_t51_mem1 += MAS_MEM[1]

	c_bc00 = S.Task('c_bc00', length=1, delay_cost=1)
	S += c_bc00 >= 54
	c_bc00 += MAS[1]

	c_bc11 = S.Task('c_bc11', length=1, delay_cost=1)
	S += c_bc11 >= 54
	c_bc11 += MAS[3]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	S += c_pa10_mem0 >= 54
	c_pa10_mem0 += MAS_MEM[4]

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	S += c_pa10_mem1 >= 54
	c_pa10_mem1 += MAS_MEM[3]

	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=8, delay_cost=1)
	S += c_pbc_t0_t0 >= 54
	c_pbc_t0_t0 += MM[0]

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem0 >= 54
	c_pbc_t0_t2_mem0 += MAS_MEM[6]

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem1 >= 54
	c_pbc_t0_t2_mem1 += MAS_MEM[5]

	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	S += c_pcb_t1_t1_in >= 54
	c_pcb_t1_t1_in += MM_in[0]

	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem0 >= 54
	c_pcb_t1_t1_mem0 += MAS_MEM[0]

	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=1, delay_cost=1)
	S += c_pcb_t1_t2 >= 54
	c_pcb_t1_t2 += MAS[2]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	S += c_aa00_mem0 >= 55
	c_aa00_mem0 += MAS_MEM[6]

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	S += c_aa00_mem1 >= 55
	c_aa00_mem1 += MAS_MEM[3]

	c_aa_t20 = S.Task('c_aa_t20', length=1, delay_cost=1)
	S += c_aa_t20 >= 55
	c_aa_t20 += MAS[3]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	S += c_ab11_mem0 >= 55
	c_ab11_mem0 += MAS_MEM[2]

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	S += c_ab11_mem1 >= 55
	c_ab11_mem1 += MAS_MEM[5]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 55
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 55
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_bb_t51 = S.Task('c_bb_t51', length=1, delay_cost=1)
	S += c_bb_t51 >= 55
	c_bb_t51 += MAS[1]

	c_cc_t21_mem0 = S.Task('c_cc_t21_mem0', length=1, delay_cost=1)
	S += c_cc_t21_mem0 >= 55
	c_cc_t21_mem0 += MM_MEM[0]

	c_cc_t21_mem1 = S.Task('c_cc_t21_mem1', length=1, delay_cost=1)
	S += c_cc_t21_mem1 >= 55
	c_cc_t21_mem1 += MAS_MEM[7]

	c_cc_t51_mem0 = S.Task('c_cc_t51_mem0', length=1, delay_cost=1)
	S += c_cc_t51_mem0 >= 55
	c_cc_t51_mem0 += MAS_MEM[0]

	c_cc_t51_mem1 = S.Task('c_cc_t51_mem1', length=1, delay_cost=1)
	S += c_cc_t51_mem1 >= 55
	c_cc_t51_mem1 += MAS_MEM[1]

	c_pa10 = S.Task('c_pa10', length=1, delay_cost=1)
	S += c_pa10 >= 55
	c_pa10 += MAS[2]

	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	S += c_paa_t1_t0_in >= 55
	c_paa_t1_t0_in += MM_in[0]

	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem0 >= 55
	c_paa_t1_t0_mem0 += MAS_MEM[4]

	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=1, delay_cost=1)
	S += c_pbc_t0_t2 >= 55
	c_pbc_t0_t2 += MAS[0]

	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=8, delay_cost=1)
	S += c_pcb_t1_t1 >= 55
	c_pcb_t1_t1 += MM[0]

	c_aa00 = S.Task('c_aa00', length=1, delay_cost=1)
	S += c_aa00 >= 56
	c_aa00 += MAS[2]

	c_ab11 = S.Task('c_ab11', length=1, delay_cost=1)
	S += c_ab11 >= 56
	c_ab11 += MAS[1]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 56
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	S += c_bb_t21_mem0 >= 56
	c_bb_t21_mem0 += MM_MEM[0]

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	S += c_bb_t21_mem1 >= 56
	c_bb_t21_mem1 += MAS_MEM[3]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	S += c_bb_t50_mem0 >= 56
	c_bb_t50_mem0 += MAS_MEM[2]

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	S += c_bb_t50_mem1 >= 56
	c_bb_t50_mem1 += MAS_MEM[1]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 56
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	S += c_cc01_mem0 >= 56
	c_cc01_mem0 += MAS_MEM[0]

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	S += c_cc01_mem1 >= 56
	c_cc01_mem1 += MAS_MEM[7]

	c_cc_t21 = S.Task('c_cc_t21', length=1, delay_cost=1)
	S += c_cc_t21 >= 56
	c_cc_t21 += MAS[0]

	c_cc_t51 = S.Task('c_cc_t51', length=1, delay_cost=1)
	S += c_cc_t51 >= 56
	c_cc_t51 += MAS[3]

	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=8, delay_cost=1)
	S += c_paa_t1_t0 >= 56
	c_paa_t1_t0 += MM[0]

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t2_mem0 >= 56
	c_paa_t1_t2_mem0 += MAS_MEM[4]

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t2_mem1 >= 56
	c_paa_t1_t2_mem1 += MAS_MEM[5]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t21_mem0 >= 57
	c_aa_t21_mem0 += MM_MEM[0]

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t21_mem1 >= 57
	c_aa_t21_mem1 += MAS_MEM[1]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	S += c_aa_t51_mem0 >= 57
	c_aa_t51_mem0 += MAS_MEM[2]

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	S += c_aa_t51_mem1 >= 57
	c_aa_t51_mem1 += MAS_MEM[3]

	c_bb_t21 = S.Task('c_bb_t21', length=1, delay_cost=1)
	S += c_bb_t21 >= 57
	c_bb_t21 += MAS[0]

	c_bb_t50 = S.Task('c_bb_t50', length=1, delay_cost=1)
	S += c_bb_t50 >= 57
	c_bb_t50 += MAS[3]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 57
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 57
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_0_mem0 >= 57
	c_bcxi_y1_0_mem0 += MAS_MEM[4]

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_0_mem1 >= 57
	c_bcxi_y1_0_mem1 += MAS_MEM[7]

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem0 >= 57
	c_bcxi_y1_1_mem0 += MAS_MEM[6]

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem1 >= 57
	c_bcxi_y1_1_mem1 += MAS_MEM[5]

	c_cc01 = S.Task('c_cc01', length=1, delay_cost=1)
	S += c_cc01 >= 57
	c_cc01 += MAS[2]

	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=1, delay_cost=1)
	S += c_paa_t1_t2 >= 57
	c_paa_t1_t2 += MAS[1]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	S += c_aa01_mem0 >= 58
	c_aa01_mem0 += MAS_MEM[2]

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	S += c_aa01_mem1 >= 58
	c_aa01_mem1 += MAS_MEM[5]

	c_aa_t21 = S.Task('c_aa_t21', length=1, delay_cost=1)
	S += c_aa_t21 >= 58
	c_aa_t21 += MAS[1]

	c_aa_t51 = S.Task('c_aa_t51', length=1, delay_cost=1)
	S += c_aa_t51 >= 58
	c_aa_t51 += MAS[2]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 58
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 58
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	S += c_bb00_mem0 >= 58
	c_bb00_mem0 += MAS_MEM[6]

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	S += c_bb00_mem1 >= 58
	c_bb00_mem1 += MAS_MEM[7]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	S += c_bb01_mem0 >= 58
	c_bb01_mem0 += MAS_MEM[0]

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	S += c_bb01_mem1 >= 58
	c_bb01_mem1 += MAS_MEM[3]

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=1, delay_cost=1)
	S += c_bcxi_y1_0 >= 58
	c_bcxi_y1_0 += MAS[0]

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=1, delay_cost=1)
	S += c_bcxi_y1_1 >= 58
	c_bcxi_y1_1 += MAS[3]

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	S += c_pa00_mem0 >= 58
	c_pa00_mem0 += MAS_MEM[4]

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	S += c_pa00_mem1 >= 58
	c_pa00_mem1 += MAS_MEM[1]

	c_aa01 = S.Task('c_aa01', length=1, delay_cost=1)
	S += c_aa01 >= 59
	c_aa01 += MAS[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 59
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb00 = S.Task('c_bb00', length=1, delay_cost=1)
	S += c_bb00 >= 59
	c_bb00 += MAS[3]

	c_bb01 = S.Task('c_bb01', length=1, delay_cost=1)
	S += c_bb01 >= 59
	c_bb01 += MAS[1]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 59
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_pa00 = S.Task('c_pa00', length=1, delay_cost=1)
	S += c_pa00 >= 59
	c_pa00 += MAS[2]

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	S += c_pa01_mem0 >= 59
	c_pa01_mem0 += MAS_MEM[0]

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	S += c_pa01_mem1 >= 59
	c_pa01_mem1 += MAS_MEM[7]

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	S += c_pb11_mem0 >= 59
	c_pb11_mem0 += MAS_MEM[4]

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	S += c_pb11_mem1 >= 59
	c_pb11_mem1 += MAS_MEM[3]

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	S += c_pc00_mem0 >= 59
	c_pc00_mem0 += MAS_MEM[6]

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	S += c_pc00_mem1 >= 59
	c_pc00_mem1 += MAS_MEM[5]

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	S += c_pc01_mem0 >= 59
	c_pc01_mem0 += MAS_MEM[2]

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	S += c_pc01_mem1 >= 59
	c_pc01_mem1 += MAS_MEM[1]

	c_pa01 = S.Task('c_pa01', length=1, delay_cost=1)
	S += c_pa01 >= 60
	c_pa01 += MAS[1]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 60
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 60
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pb11 = S.Task('c_pb11', length=1, delay_cost=1)
	S += c_pb11 >= 60
	c_pb11 += MAS[3]

	c_pc00 = S.Task('c_pc00', length=1, delay_cost=1)
	S += c_pc00 >= 60
	c_pc00 += MAS[2]

	c_pc01 = S.Task('c_pc01', length=1, delay_cost=1)
	S += c_pc01 >= 60
	c_pc01 += MAS[0]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 61
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 61
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 62
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 62
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 63
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 63
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 64
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 64
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 65
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 65
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 66
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 66
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 67
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 67
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 68
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 68
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 69
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 69
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 70
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 70
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 71
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 71
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 72
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem1 >= 72
	c_pcb_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 73
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem1 >= 73
	c_pcb_t1_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 74
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem1 >= 74
	c_pbc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 75
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem1 >= 75
	c_pbc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 76
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t1_mem1 >= 76
	c_paa_t1_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 77
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem1 >= 77
	c_paa_t1_t0_mem1 += MAIN_MEM_r[1]


	# new tasks
	c_pbc_t0_t4_in = S.Task('c_pbc_t0_t4_in', length=1, delay_cost=1)
	c_pbc_t0_t4_in += alt(MM_in)
	c_pbc_t0_t4 = S.Task('c_pbc_t0_t4', length=8, delay_cost=1)
	c_pbc_t0_t4 += alt(MM)
	S += c_pbc_t0_t4>=c_pbc_t0_t4_in

	c_pbc_t0_t4_mem0 = S.Task('c_pbc_t0_t4_mem0', length=1, delay_cost=1)
	c_pbc_t0_t4_mem0 += MAS_MEM[0]
	S += 55 < c_pbc_t0_t4_mem0
	S += c_pbc_t0_t4_mem0 <= c_pbc_t0_t4

	c_pbc_t0_t4_mem1 = S.Task('c_pbc_t0_t4_mem1', length=1, delay_cost=1)
	c_pbc_t0_t4_mem1 += MAS_MEM[3]
	S += 11 < c_pbc_t0_t4_mem1
	S += c_pbc_t0_t4_mem1 <= c_pbc_t0_t4

	c_pbc_t00 = S.Task('c_pbc_t00', length=1, delay_cost=1)
	c_pbc_t00 += alt(MAS)

	c_pbc_t00_mem0 = S.Task('c_pbc_t00_mem0', length=1, delay_cost=1)
	c_pbc_t00_mem0 += MM_MEM[0]
	S += 61 < c_pbc_t00_mem0
	S += c_pbc_t00_mem0 <= c_pbc_t00

	c_pbc_t00_mem1 = S.Task('c_pbc_t00_mem1', length=1, delay_cost=1)
	c_pbc_t00_mem1 += MM_MEM[1]
	S += 54 < c_pbc_t00_mem1
	S += c_pbc_t00_mem1 <= c_pbc_t00

	c_pbc_t0_t5 = S.Task('c_pbc_t0_t5', length=1, delay_cost=1)
	c_pbc_t0_t5 += alt(MAS)

	c_pbc_t0_t5_mem0 = S.Task('c_pbc_t0_t5_mem0', length=1, delay_cost=1)
	c_pbc_t0_t5_mem0 += MM_MEM[0]
	S += 61 < c_pbc_t0_t5_mem0
	S += c_pbc_t0_t5_mem0 <= c_pbc_t0_t5

	c_pbc_t0_t5_mem1 = S.Task('c_pbc_t0_t5_mem1', length=1, delay_cost=1)
	c_pbc_t0_t5_mem1 += MM_MEM[1]
	S += 54 < c_pbc_t0_t5_mem1
	S += c_pbc_t0_t5_mem1 <= c_pbc_t0_t5

	c_pbc_t1_t0_in = S.Task('c_pbc_t1_t0_in', length=1, delay_cost=1)
	c_pbc_t1_t0_in += alt(MM_in)
	c_pbc_t1_t0 = S.Task('c_pbc_t1_t0', length=8, delay_cost=1)
	c_pbc_t1_t0 += alt(MM)
	S += c_pbc_t1_t0>=c_pbc_t1_t0_in

	c_pbc_t1_t0_mem0 = S.Task('c_pbc_t1_t0_mem0', length=1, delay_cost=1)
	c_pbc_t1_t0_mem0 += MAS_MEM[2]
	S += 53 < c_pbc_t1_t0_mem0
	S += c_pbc_t1_t0_mem0 <= c_pbc_t1_t0

	c_pbc_t1_t0_mem1 = S.Task('c_pbc_t1_t0_mem1', length=1, delay_cost=1)
	c_pbc_t1_t0_mem1 += MAIN_MEM_r[1]
	c_pbc_t1_t1_in = S.Task('c_pbc_t1_t1_in', length=1, delay_cost=1)
	c_pbc_t1_t1_in += alt(MM_in)
	c_pbc_t1_t1 = S.Task('c_pbc_t1_t1', length=8, delay_cost=1)
	c_pbc_t1_t1 += alt(MM)
	S += c_pbc_t1_t1>=c_pbc_t1_t1_in

	c_pbc_t1_t1_mem0 = S.Task('c_pbc_t1_t1_mem0', length=1, delay_cost=1)
	c_pbc_t1_t1_mem0 += MAS_MEM[6]
	S += 60 < c_pbc_t1_t1_mem0
	S += c_pbc_t1_t1_mem0 <= c_pbc_t1_t1

	c_pbc_t1_t1_mem1 = S.Task('c_pbc_t1_t1_mem1', length=1, delay_cost=1)
	c_pbc_t1_t1_mem1 += MAIN_MEM_r[1]
	c_pbc_t1_t2 = S.Task('c_pbc_t1_t2', length=1, delay_cost=1)
	c_pbc_t1_t2 += alt(MAS)

	c_pbc_t1_t2_mem0 = S.Task('c_pbc_t1_t2_mem0', length=1, delay_cost=1)
	c_pbc_t1_t2_mem0 += MAS_MEM[2]
	S += 53 < c_pbc_t1_t2_mem0
	S += c_pbc_t1_t2_mem0 <= c_pbc_t1_t2

	c_pbc_t1_t2_mem1 = S.Task('c_pbc_t1_t2_mem1', length=1, delay_cost=1)
	c_pbc_t1_t2_mem1 += MAS_MEM[7]
	S += 60 < c_pbc_t1_t2_mem1
	S += c_pbc_t1_t2_mem1 <= c_pbc_t1_t2

	c_pbc_t20 = S.Task('c_pbc_t20', length=1, delay_cost=1)
	c_pbc_t20 += alt(MAS)

	c_pbc_t20_mem0 = S.Task('c_pbc_t20_mem0', length=1, delay_cost=1)
	c_pbc_t20_mem0 += MAS_MEM[6]
	S += 53 < c_pbc_t20_mem0
	S += c_pbc_t20_mem0 <= c_pbc_t20

	c_pbc_t20_mem1 = S.Task('c_pbc_t20_mem1', length=1, delay_cost=1)
	c_pbc_t20_mem1 += MAS_MEM[3]
	S += 53 < c_pbc_t20_mem1
	S += c_pbc_t20_mem1 <= c_pbc_t20

	c_pbc_t21 = S.Task('c_pbc_t21', length=1, delay_cost=1)
	c_pbc_t21 += alt(MAS)

	c_pbc_t21_mem0 = S.Task('c_pbc_t21_mem0', length=1, delay_cost=1)
	c_pbc_t21_mem0 += MAS_MEM[4]
	S += 46 < c_pbc_t21_mem0
	S += c_pbc_t21_mem0 <= c_pbc_t21

	c_pbc_t21_mem1 = S.Task('c_pbc_t21_mem1', length=1, delay_cost=1)
	c_pbc_t21_mem1 += MAS_MEM[7]
	S += 60 < c_pbc_t21_mem1
	S += c_pbc_t21_mem1 <= c_pbc_t21

	c_pcb_t0_t0_in = S.Task('c_pcb_t0_t0_in', length=1, delay_cost=1)
	c_pcb_t0_t0_in += alt(MM_in)
	c_pcb_t0_t0 = S.Task('c_pcb_t0_t0', length=8, delay_cost=1)
	c_pcb_t0_t0 += alt(MM)
	S += c_pcb_t0_t0>=c_pcb_t0_t0_in

	c_pcb_t0_t0_mem0 = S.Task('c_pcb_t0_t0_mem0', length=1, delay_cost=1)
	c_pcb_t0_t0_mem0 += MAS_MEM[4]
	S += 60 < c_pcb_t0_t0_mem0
	S += c_pcb_t0_t0_mem0 <= c_pcb_t0_t0

	c_pcb_t0_t0_mem1 = S.Task('c_pcb_t0_t0_mem1', length=1, delay_cost=1)
	c_pcb_t0_t0_mem1 += MAIN_MEM_r[1]
	c_pcb_t0_t1_in = S.Task('c_pcb_t0_t1_in', length=1, delay_cost=1)
	c_pcb_t0_t1_in += alt(MM_in)
	c_pcb_t0_t1 = S.Task('c_pcb_t0_t1', length=8, delay_cost=1)
	c_pcb_t0_t1 += alt(MM)
	S += c_pcb_t0_t1>=c_pcb_t0_t1_in

	c_pcb_t0_t1_mem0 = S.Task('c_pcb_t0_t1_mem0', length=1, delay_cost=1)
	c_pcb_t0_t1_mem0 += MAS_MEM[0]
	S += 60 < c_pcb_t0_t1_mem0
	S += c_pcb_t0_t1_mem0 <= c_pcb_t0_t1

	c_pcb_t0_t1_mem1 = S.Task('c_pcb_t0_t1_mem1', length=1, delay_cost=1)
	c_pcb_t0_t1_mem1 += MAIN_MEM_r[1]
	c_pcb_t0_t2 = S.Task('c_pcb_t0_t2', length=1, delay_cost=1)
	c_pcb_t0_t2 += alt(MAS)

	c_pcb_t0_t2_mem0 = S.Task('c_pcb_t0_t2_mem0', length=1, delay_cost=1)
	c_pcb_t0_t2_mem0 += MAS_MEM[4]
	S += 60 < c_pcb_t0_t2_mem0
	S += c_pcb_t0_t2_mem0 <= c_pcb_t0_t2

	c_pcb_t0_t2_mem1 = S.Task('c_pcb_t0_t2_mem1', length=1, delay_cost=1)
	c_pcb_t0_t2_mem1 += MAS_MEM[1]
	S += 60 < c_pcb_t0_t2_mem1
	S += c_pcb_t0_t2_mem1 <= c_pcb_t0_t2

	c_pcb_t1_t4_in = S.Task('c_pcb_t1_t4_in', length=1, delay_cost=1)
	c_pcb_t1_t4_in += alt(MM_in)
	c_pcb_t1_t4 = S.Task('c_pcb_t1_t4', length=8, delay_cost=1)
	c_pcb_t1_t4 += alt(MM)
	S += c_pcb_t1_t4>=c_pcb_t1_t4_in

	c_pcb_t1_t4_mem0 = S.Task('c_pcb_t1_t4_mem0', length=1, delay_cost=1)
	c_pcb_t1_t4_mem0 += MAS_MEM[4]
	S += 54 < c_pcb_t1_t4_mem0
	S += c_pcb_t1_t4_mem0 <= c_pcb_t1_t4

	c_pcb_t1_t4_mem1 = S.Task('c_pcb_t1_t4_mem1', length=1, delay_cost=1)
	c_pcb_t1_t4_mem1 += MAS_MEM[5]
	S += 14 < c_pcb_t1_t4_mem1
	S += c_pcb_t1_t4_mem1 <= c_pcb_t1_t4

	c_pcb_t10 = S.Task('c_pcb_t10', length=1, delay_cost=1)
	c_pcb_t10 += alt(MAS)

	c_pcb_t10_mem0 = S.Task('c_pcb_t10_mem0', length=1, delay_cost=1)
	c_pcb_t10_mem0 += MM_MEM[0]
	S += 60 < c_pcb_t10_mem0
	S += c_pcb_t10_mem0 <= c_pcb_t10

	c_pcb_t10_mem1 = S.Task('c_pcb_t10_mem1', length=1, delay_cost=1)
	c_pcb_t10_mem1 += MM_MEM[1]
	S += 62 < c_pcb_t10_mem1
	S += c_pcb_t10_mem1 <= c_pcb_t10

	c_pcb_t1_t5 = S.Task('c_pcb_t1_t5', length=1, delay_cost=1)
	c_pcb_t1_t5 += alt(MAS)

	c_pcb_t1_t5_mem0 = S.Task('c_pcb_t1_t5_mem0', length=1, delay_cost=1)
	c_pcb_t1_t5_mem0 += MM_MEM[0]
	S += 60 < c_pcb_t1_t5_mem0
	S += c_pcb_t1_t5_mem0 <= c_pcb_t1_t5

	c_pcb_t1_t5_mem1 = S.Task('c_pcb_t1_t5_mem1', length=1, delay_cost=1)
	c_pcb_t1_t5_mem1 += MM_MEM[1]
	S += 62 < c_pcb_t1_t5_mem1
	S += c_pcb_t1_t5_mem1 <= c_pcb_t1_t5

	c_pcb_t20 = S.Task('c_pcb_t20', length=1, delay_cost=1)
	c_pcb_t20 += alt(MAS)

	c_pcb_t20_mem0 = S.Task('c_pcb_t20_mem0', length=1, delay_cost=1)
	c_pcb_t20_mem0 += MAS_MEM[4]
	S += 60 < c_pcb_t20_mem0
	S += c_pcb_t20_mem0 <= c_pcb_t20

	c_pcb_t20_mem1 = S.Task('c_pcb_t20_mem1', length=1, delay_cost=1)
	c_pcb_t20_mem1 += MAS_MEM[5]
	S += 52 < c_pcb_t20_mem1
	S += c_pcb_t20_mem1 <= c_pcb_t20

	c_pcb_t21 = S.Task('c_pcb_t21', length=1, delay_cost=1)
	c_pcb_t21 += alt(MAS)

	c_pcb_t21_mem0 = S.Task('c_pcb_t21_mem0', length=1, delay_cost=1)
	c_pcb_t21_mem0 += MAS_MEM[0]
	S += 60 < c_pcb_t21_mem0
	S += c_pcb_t21_mem0 <= c_pcb_t21

	c_pcb_t21_mem1 = S.Task('c_pcb_t21_mem1', length=1, delay_cost=1)
	c_pcb_t21_mem1 += MAS_MEM[1]
	S += 52 < c_pcb_t21_mem1
	S += c_pcb_t21_mem1 <= c_pcb_t21

	c_paa_t0_t0_in = S.Task('c_paa_t0_t0_in', length=1, delay_cost=1)
	c_paa_t0_t0_in += alt(MM_in)
	c_paa_t0_t0 = S.Task('c_paa_t0_t0', length=8, delay_cost=1)
	c_paa_t0_t0 += alt(MM)
	S += c_paa_t0_t0>=c_paa_t0_t0_in

	c_paa_t0_t0_mem0 = S.Task('c_paa_t0_t0_mem0', length=1, delay_cost=1)
	c_paa_t0_t0_mem0 += MAS_MEM[4]
	S += 59 < c_paa_t0_t0_mem0
	S += c_paa_t0_t0_mem0 <= c_paa_t0_t0

	c_paa_t0_t0_mem1 = S.Task('c_paa_t0_t0_mem1', length=1, delay_cost=1)
	c_paa_t0_t0_mem1 += MAIN_MEM_r[1]
	c_paa_t0_t1_in = S.Task('c_paa_t0_t1_in', length=1, delay_cost=1)
	c_paa_t0_t1_in += alt(MM_in)
	c_paa_t0_t1 = S.Task('c_paa_t0_t1', length=8, delay_cost=1)
	c_paa_t0_t1 += alt(MM)
	S += c_paa_t0_t1>=c_paa_t0_t1_in

	c_paa_t0_t1_mem0 = S.Task('c_paa_t0_t1_mem0', length=1, delay_cost=1)
	c_paa_t0_t1_mem0 += MAS_MEM[2]
	S += 60 < c_paa_t0_t1_mem0
	S += c_paa_t0_t1_mem0 <= c_paa_t0_t1

	c_paa_t0_t1_mem1 = S.Task('c_paa_t0_t1_mem1', length=1, delay_cost=1)
	c_paa_t0_t1_mem1 += MAIN_MEM_r[1]
	c_paa_t0_t2 = S.Task('c_paa_t0_t2', length=1, delay_cost=1)
	c_paa_t0_t2 += alt(MAS)

	c_paa_t0_t2_mem0 = S.Task('c_paa_t0_t2_mem0', length=1, delay_cost=1)
	c_paa_t0_t2_mem0 += MAS_MEM[4]
	S += 59 < c_paa_t0_t2_mem0
	S += c_paa_t0_t2_mem0 <= c_paa_t0_t2

	c_paa_t0_t2_mem1 = S.Task('c_paa_t0_t2_mem1', length=1, delay_cost=1)
	c_paa_t0_t2_mem1 += MAS_MEM[3]
	S += 60 < c_paa_t0_t2_mem1
	S += c_paa_t0_t2_mem1 <= c_paa_t0_t2

	c_paa_t1_t4_in = S.Task('c_paa_t1_t4_in', length=1, delay_cost=1)
	c_paa_t1_t4_in += alt(MM_in)
	c_paa_t1_t4 = S.Task('c_paa_t1_t4', length=8, delay_cost=1)
	c_paa_t1_t4 += alt(MM)
	S += c_paa_t1_t4>=c_paa_t1_t4_in

	c_paa_t1_t4_mem0 = S.Task('c_paa_t1_t4_mem0', length=1, delay_cost=1)
	c_paa_t1_t4_mem0 += MAS_MEM[2]
	S += 57 < c_paa_t1_t4_mem0
	S += c_paa_t1_t4_mem0 <= c_paa_t1_t4

	c_paa_t1_t4_mem1 = S.Task('c_paa_t1_t4_mem1', length=1, delay_cost=1)
	c_paa_t1_t4_mem1 += MAS_MEM[3]
	S += 12 < c_paa_t1_t4_mem1
	S += c_paa_t1_t4_mem1 <= c_paa_t1_t4

	c_paa_t10 = S.Task('c_paa_t10', length=1, delay_cost=1)
	c_paa_t10 += alt(MAS)

	c_paa_t10_mem0 = S.Task('c_paa_t10_mem0', length=1, delay_cost=1)
	c_paa_t10_mem0 += MM_MEM[0]
	S += 63 < c_paa_t10_mem0
	S += c_paa_t10_mem0 <= c_paa_t10

	c_paa_t10_mem1 = S.Task('c_paa_t10_mem1', length=1, delay_cost=1)
	c_paa_t10_mem1 += MM_MEM[1]
	S += 59 < c_paa_t10_mem1
	S += c_paa_t10_mem1 <= c_paa_t10

	c_paa_t1_t5 = S.Task('c_paa_t1_t5', length=1, delay_cost=1)
	c_paa_t1_t5 += alt(MAS)

	c_paa_t1_t5_mem0 = S.Task('c_paa_t1_t5_mem0', length=1, delay_cost=1)
	c_paa_t1_t5_mem0 += MM_MEM[0]
	S += 63 < c_paa_t1_t5_mem0
	S += c_paa_t1_t5_mem0 <= c_paa_t1_t5

	c_paa_t1_t5_mem1 = S.Task('c_paa_t1_t5_mem1', length=1, delay_cost=1)
	c_paa_t1_t5_mem1 += MM_MEM[1]
	S += 59 < c_paa_t1_t5_mem1
	S += c_paa_t1_t5_mem1 <= c_paa_t1_t5

	c_paa_t20 = S.Task('c_paa_t20', length=1, delay_cost=1)
	c_paa_t20 += alt(MAS)

	c_paa_t20_mem0 = S.Task('c_paa_t20_mem0', length=1, delay_cost=1)
	c_paa_t20_mem0 += MAS_MEM[4]
	S += 59 < c_paa_t20_mem0
	S += c_paa_t20_mem0 <= c_paa_t20

	c_paa_t20_mem1 = S.Task('c_paa_t20_mem1', length=1, delay_cost=1)
	c_paa_t20_mem1 += MAS_MEM[5]
	S += 55 < c_paa_t20_mem1
	S += c_paa_t20_mem1 <= c_paa_t20

	c_paa_t21 = S.Task('c_paa_t21', length=1, delay_cost=1)
	c_paa_t21 += alt(MAS)

	c_paa_t21_mem0 = S.Task('c_paa_t21_mem0', length=1, delay_cost=1)
	c_paa_t21_mem0 += MAS_MEM[2]
	S += 60 < c_paa_t21_mem0
	S += c_paa_t21_mem0 <= c_paa_t21

	c_paa_t21_mem1 = S.Task('c_paa_t21_mem1', length=1, delay_cost=1)
	c_paa_t21_mem1 += MAS_MEM[5]
	S += 51 < c_paa_t21_mem1
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
	S += c_pbc_t01_mem1 <= c_pbc_t01

	c_pbc_t1_t4_in = S.Task('c_pbc_t1_t4_in', length=1, delay_cost=1)
	c_pbc_t1_t4_in += alt(MM_in)
	c_pbc_t1_t4 = S.Task('c_pbc_t1_t4', length=8, delay_cost=1)
	c_pbc_t1_t4 += alt(MM)
	S += c_pbc_t1_t4>=c_pbc_t1_t4_in

	c_pbc_t1_t4_mem0 = S.Task('c_pbc_t1_t4_mem0', length=1, delay_cost=1)
	c_pbc_t1_t4_mem0 += alt(MAS_MEM)
	S += (c_pbc_t1_t2*MAS[0])-1 < c_pbc_t1_t4_mem0*MAS_MEM[0]
	S += (c_pbc_t1_t2*MAS[1])-1 < c_pbc_t1_t4_mem0*MAS_MEM[2]
	S += (c_pbc_t1_t2*MAS[2])-1 < c_pbc_t1_t4_mem0*MAS_MEM[4]
	S += (c_pbc_t1_t2*MAS[3])-1 < c_pbc_t1_t4_mem0*MAS_MEM[6]
	S += c_pbc_t1_t4_mem0 <= c_pbc_t1_t4

	c_pbc_t1_t4_mem1 = S.Task('c_pbc_t1_t4_mem1', length=1, delay_cost=1)
	c_pbc_t1_t4_mem1 += MAS_MEM[7]
	S += 13 < c_pbc_t1_t4_mem1
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
	c_pbc_t4_t0 = S.Task('c_pbc_t4_t0', length=8, delay_cost=1)
	c_pbc_t4_t0 += alt(MM)
	S += c_pbc_t4_t0>=c_pbc_t4_t0_in

	c_pbc_t4_t0_mem0 = S.Task('c_pbc_t4_t0_mem0', length=1, delay_cost=1)
	c_pbc_t4_t0_mem0 += alt(MAS_MEM)
	S += (c_pbc_t20*MAS[0])-1 < c_pbc_t4_t0_mem0*MAS_MEM[0]
	S += (c_pbc_t20*MAS[1])-1 < c_pbc_t4_t0_mem0*MAS_MEM[2]
	S += (c_pbc_t20*MAS[2])-1 < c_pbc_t4_t0_mem0*MAS_MEM[4]
	S += (c_pbc_t20*MAS[3])-1 < c_pbc_t4_t0_mem0*MAS_MEM[6]
	S += c_pbc_t4_t0_mem0 <= c_pbc_t4_t0

	c_pbc_t4_t0_mem1 = S.Task('c_pbc_t4_t0_mem1', length=1, delay_cost=1)
	c_pbc_t4_t0_mem1 += MAS_MEM[5]
	S += 13 < c_pbc_t4_t0_mem1
	S += c_pbc_t4_t0_mem1 <= c_pbc_t4_t0

	c_pbc_t4_t1_in = S.Task('c_pbc_t4_t1_in', length=1, delay_cost=1)
	c_pbc_t4_t1_in += alt(MM_in)
	c_pbc_t4_t1 = S.Task('c_pbc_t4_t1', length=8, delay_cost=1)
	c_pbc_t4_t1 += alt(MM)
	S += c_pbc_t4_t1>=c_pbc_t4_t1_in

	c_pbc_t4_t1_mem0 = S.Task('c_pbc_t4_t1_mem0', length=1, delay_cost=1)
	c_pbc_t4_t1_mem0 += alt(MAS_MEM)
	S += (c_pbc_t21*MAS[0])-1 < c_pbc_t4_t1_mem0*MAS_MEM[0]
	S += (c_pbc_t21*MAS[1])-1 < c_pbc_t4_t1_mem0*MAS_MEM[2]
	S += (c_pbc_t21*MAS[2])-1 < c_pbc_t4_t1_mem0*MAS_MEM[4]
	S += (c_pbc_t21*MAS[3])-1 < c_pbc_t4_t1_mem0*MAS_MEM[6]
	S += c_pbc_t4_t1_mem0 <= c_pbc_t4_t1

	c_pbc_t4_t1_mem1 = S.Task('c_pbc_t4_t1_mem1', length=1, delay_cost=1)
	c_pbc_t4_t1_mem1 += MAS_MEM[3]
	S += 13 < c_pbc_t4_t1_mem1
	S += c_pbc_t4_t1_mem1 <= c_pbc_t4_t1

	c_pbc_t4_t2 = S.Task('c_pbc_t4_t2', length=1, delay_cost=1)
	c_pbc_t4_t2 += alt(MAS)

	c_pbc_t4_t2_mem0 = S.Task('c_pbc_t4_t2_mem0', length=1, delay_cost=1)
	c_pbc_t4_t2_mem0 += alt(MAS_MEM)
	S += (c_pbc_t20*MAS[0])-1 < c_pbc_t4_t2_mem0*MAS_MEM[0]
	S += (c_pbc_t20*MAS[1])-1 < c_pbc_t4_t2_mem0*MAS_MEM[2]
	S += (c_pbc_t20*MAS[2])-1 < c_pbc_t4_t2_mem0*MAS_MEM[4]
	S += (c_pbc_t20*MAS[3])-1 < c_pbc_t4_t2_mem0*MAS_MEM[6]
	S += c_pbc_t4_t2_mem0 <= c_pbc_t4_t2

	c_pbc_t4_t2_mem1 = S.Task('c_pbc_t4_t2_mem1', length=1, delay_cost=1)
	c_pbc_t4_t2_mem1 += alt(MAS_MEM)
	S += (c_pbc_t21*MAS[0])-1 < c_pbc_t4_t2_mem1*MAS_MEM[1]
	S += (c_pbc_t21*MAS[1])-1 < c_pbc_t4_t2_mem1*MAS_MEM[3]
	S += (c_pbc_t21*MAS[2])-1 < c_pbc_t4_t2_mem1*MAS_MEM[5]
	S += (c_pbc_t21*MAS[3])-1 < c_pbc_t4_t2_mem1*MAS_MEM[7]
	S += c_pbc_t4_t2_mem1 <= c_pbc_t4_t2

	c_pcb_t0_t4_in = S.Task('c_pcb_t0_t4_in', length=1, delay_cost=1)
	c_pcb_t0_t4_in += alt(MM_in)
	c_pcb_t0_t4 = S.Task('c_pcb_t0_t4', length=8, delay_cost=1)
	c_pcb_t0_t4 += alt(MM)
	S += c_pcb_t0_t4>=c_pcb_t0_t4_in

	c_pcb_t0_t4_mem0 = S.Task('c_pcb_t0_t4_mem0', length=1, delay_cost=1)
	c_pcb_t0_t4_mem0 += alt(MAS_MEM)
	S += (c_pcb_t0_t2*MAS[0])-1 < c_pcb_t0_t4_mem0*MAS_MEM[0]
	S += (c_pcb_t0_t2*MAS[1])-1 < c_pcb_t0_t4_mem0*MAS_MEM[2]
	S += (c_pcb_t0_t2*MAS[2])-1 < c_pcb_t0_t4_mem0*MAS_MEM[4]
	S += (c_pcb_t0_t2*MAS[3])-1 < c_pcb_t0_t4_mem0*MAS_MEM[6]
	S += c_pcb_t0_t4_mem0 <= c_pcb_t0_t4

	c_pcb_t0_t4_mem1 = S.Task('c_pcb_t0_t4_mem1', length=1, delay_cost=1)
	c_pcb_t0_t4_mem1 += MAS_MEM[7]
	S += 14 < c_pcb_t0_t4_mem1
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
	S += c_pcb_t11_mem1 <= c_pcb_t11

	c_pcb_t4_t0_in = S.Task('c_pcb_t4_t0_in', length=1, delay_cost=1)
	c_pcb_t4_t0_in += alt(MM_in)
	c_pcb_t4_t0 = S.Task('c_pcb_t4_t0', length=8, delay_cost=1)
	c_pcb_t4_t0 += alt(MM)
	S += c_pcb_t4_t0>=c_pcb_t4_t0_in

	c_pcb_t4_t0_mem0 = S.Task('c_pcb_t4_t0_mem0', length=1, delay_cost=1)
	c_pcb_t4_t0_mem0 += alt(MAS_MEM)
	S += (c_pcb_t20*MAS[0])-1 < c_pcb_t4_t0_mem0*MAS_MEM[0]
	S += (c_pcb_t20*MAS[1])-1 < c_pcb_t4_t0_mem0*MAS_MEM[2]
	S += (c_pcb_t20*MAS[2])-1 < c_pcb_t4_t0_mem0*MAS_MEM[4]
	S += (c_pcb_t20*MAS[3])-1 < c_pcb_t4_t0_mem0*MAS_MEM[6]
	S += c_pcb_t4_t0_mem0 <= c_pcb_t4_t0

	c_pcb_t4_t0_mem1 = S.Task('c_pcb_t4_t0_mem1', length=1, delay_cost=1)
	c_pcb_t4_t0_mem1 += MAS_MEM[1]
	S += 11 < c_pcb_t4_t0_mem1
	S += c_pcb_t4_t0_mem1 <= c_pcb_t4_t0

	c_pcb_t4_t1_in = S.Task('c_pcb_t4_t1_in', length=1, delay_cost=1)
	c_pcb_t4_t1_in += alt(MM_in)
	c_pcb_t4_t1 = S.Task('c_pcb_t4_t1', length=8, delay_cost=1)
	c_pcb_t4_t1 += alt(MM)
	S += c_pcb_t4_t1>=c_pcb_t4_t1_in

	c_pcb_t4_t1_mem0 = S.Task('c_pcb_t4_t1_mem0', length=1, delay_cost=1)
	c_pcb_t4_t1_mem0 += alt(MAS_MEM)
	S += (c_pcb_t21*MAS[0])-1 < c_pcb_t4_t1_mem0*MAS_MEM[0]
	S += (c_pcb_t21*MAS[1])-1 < c_pcb_t4_t1_mem0*MAS_MEM[2]
	S += (c_pcb_t21*MAS[2])-1 < c_pcb_t4_t1_mem0*MAS_MEM[4]
	S += (c_pcb_t21*MAS[3])-1 < c_pcb_t4_t1_mem0*MAS_MEM[6]
	S += c_pcb_t4_t1_mem0 <= c_pcb_t4_t1

	c_pcb_t4_t1_mem1 = S.Task('c_pcb_t4_t1_mem1', length=1, delay_cost=1)
	c_pcb_t4_t1_mem1 += MAS_MEM[1]
	S += 13 < c_pcb_t4_t1_mem1
	S += c_pcb_t4_t1_mem1 <= c_pcb_t4_t1

	c_pcb_t4_t2 = S.Task('c_pcb_t4_t2', length=1, delay_cost=1)
	c_pcb_t4_t2 += alt(MAS)

	c_pcb_t4_t2_mem0 = S.Task('c_pcb_t4_t2_mem0', length=1, delay_cost=1)
	c_pcb_t4_t2_mem0 += alt(MAS_MEM)
	S += (c_pcb_t20*MAS[0])-1 < c_pcb_t4_t2_mem0*MAS_MEM[0]
	S += (c_pcb_t20*MAS[1])-1 < c_pcb_t4_t2_mem0*MAS_MEM[2]
	S += (c_pcb_t20*MAS[2])-1 < c_pcb_t4_t2_mem0*MAS_MEM[4]
	S += (c_pcb_t20*MAS[3])-1 < c_pcb_t4_t2_mem0*MAS_MEM[6]
	S += c_pcb_t4_t2_mem0 <= c_pcb_t4_t2

	c_pcb_t4_t2_mem1 = S.Task('c_pcb_t4_t2_mem1', length=1, delay_cost=1)
	c_pcb_t4_t2_mem1 += alt(MAS_MEM)
	S += (c_pcb_t21*MAS[0])-1 < c_pcb_t4_t2_mem1*MAS_MEM[1]
	S += (c_pcb_t21*MAS[1])-1 < c_pcb_t4_t2_mem1*MAS_MEM[3]
	S += (c_pcb_t21*MAS[2])-1 < c_pcb_t4_t2_mem1*MAS_MEM[5]
	S += (c_pcb_t21*MAS[3])-1 < c_pcb_t4_t2_mem1*MAS_MEM[7]
	S += c_pcb_t4_t2_mem1 <= c_pcb_t4_t2

	c_paa_t0_t4_in = S.Task('c_paa_t0_t4_in', length=1, delay_cost=1)
	c_paa_t0_t4_in += alt(MM_in)
	c_paa_t0_t4 = S.Task('c_paa_t0_t4', length=8, delay_cost=1)
	c_paa_t0_t4 += alt(MM)
	S += c_paa_t0_t4>=c_paa_t0_t4_in

	c_paa_t0_t4_mem0 = S.Task('c_paa_t0_t4_mem0', length=1, delay_cost=1)
	c_paa_t0_t4_mem0 += alt(MAS_MEM)
	S += (c_paa_t0_t2*MAS[0])-1 < c_paa_t0_t4_mem0*MAS_MEM[0]
	S += (c_paa_t0_t2*MAS[1])-1 < c_paa_t0_t4_mem0*MAS_MEM[2]
	S += (c_paa_t0_t2*MAS[2])-1 < c_paa_t0_t4_mem0*MAS_MEM[4]
	S += (c_paa_t0_t2*MAS[3])-1 < c_paa_t0_t4_mem0*MAS_MEM[6]
	S += c_paa_t0_t4_mem0 <= c_paa_t0_t4

	c_paa_t0_t4_mem1 = S.Task('c_paa_t0_t4_mem1', length=1, delay_cost=1)
	c_paa_t0_t4_mem1 += MAS_MEM[1]
	S += 12 < c_paa_t0_t4_mem1
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
	S += c_paa_t11_mem1 <= c_paa_t11

	c_paa_t4_t0_in = S.Task('c_paa_t4_t0_in', length=1, delay_cost=1)
	c_paa_t4_t0_in += alt(MM_in)
	c_paa_t4_t0 = S.Task('c_paa_t4_t0', length=8, delay_cost=1)
	c_paa_t4_t0 += alt(MM)
	S += c_paa_t4_t0>=c_paa_t4_t0_in

	c_paa_t4_t0_mem0 = S.Task('c_paa_t4_t0_mem0', length=1, delay_cost=1)
	c_paa_t4_t0_mem0 += alt(MAS_MEM)
	S += (c_paa_t20*MAS[0])-1 < c_paa_t4_t0_mem0*MAS_MEM[0]
	S += (c_paa_t20*MAS[1])-1 < c_paa_t4_t0_mem0*MAS_MEM[2]
	S += (c_paa_t20*MAS[2])-1 < c_paa_t4_t0_mem0*MAS_MEM[4]
	S += (c_paa_t20*MAS[3])-1 < c_paa_t4_t0_mem0*MAS_MEM[6]
	S += c_paa_t4_t0_mem0 <= c_paa_t4_t0

	c_paa_t4_t0_mem1 = S.Task('c_paa_t4_t0_mem1', length=1, delay_cost=1)
	c_paa_t4_t0_mem1 += MAS_MEM[5]
	S += 12 < c_paa_t4_t0_mem1
	S += c_paa_t4_t0_mem1 <= c_paa_t4_t0

	c_paa_t4_t1_in = S.Task('c_paa_t4_t1_in', length=1, delay_cost=1)
	c_paa_t4_t1_in += alt(MM_in)
	c_paa_t4_t1 = S.Task('c_paa_t4_t1', length=8, delay_cost=1)
	c_paa_t4_t1 += alt(MM)
	S += c_paa_t4_t1>=c_paa_t4_t1_in

	c_paa_t4_t1_mem0 = S.Task('c_paa_t4_t1_mem0', length=1, delay_cost=1)
	c_paa_t4_t1_mem0 += alt(MAS_MEM)
	S += (c_paa_t21*MAS[0])-1 < c_paa_t4_t1_mem0*MAS_MEM[0]
	S += (c_paa_t21*MAS[1])-1 < c_paa_t4_t1_mem0*MAS_MEM[2]
	S += (c_paa_t21*MAS[2])-1 < c_paa_t4_t1_mem0*MAS_MEM[4]
	S += (c_paa_t21*MAS[3])-1 < c_paa_t4_t1_mem0*MAS_MEM[6]
	S += c_paa_t4_t1_mem0 <= c_paa_t4_t1

	c_paa_t4_t1_mem1 = S.Task('c_paa_t4_t1_mem1', length=1, delay_cost=1)
	c_paa_t4_t1_mem1 += MAS_MEM[7]
	S += 12 < c_paa_t4_t1_mem1
	S += c_paa_t4_t1_mem1 <= c_paa_t4_t1

	c_paa_t4_t2 = S.Task('c_paa_t4_t2', length=1, delay_cost=1)
	c_paa_t4_t2 += alt(MAS)

	c_paa_t4_t2_mem0 = S.Task('c_paa_t4_t2_mem0', length=1, delay_cost=1)
	c_paa_t4_t2_mem0 += alt(MAS_MEM)
	S += (c_paa_t20*MAS[0])-1 < c_paa_t4_t2_mem0*MAS_MEM[0]
	S += (c_paa_t20*MAS[1])-1 < c_paa_t4_t2_mem0*MAS_MEM[2]
	S += (c_paa_t20*MAS[2])-1 < c_paa_t4_t2_mem0*MAS_MEM[4]
	S += (c_paa_t20*MAS[3])-1 < c_paa_t4_t2_mem0*MAS_MEM[6]
	S += c_paa_t4_t2_mem0 <= c_paa_t4_t2

	c_paa_t4_t2_mem1 = S.Task('c_paa_t4_t2_mem1', length=1, delay_cost=1)
	c_paa_t4_t2_mem1 += alt(MAS_MEM)
	S += (c_paa_t21*MAS[0])-1 < c_paa_t4_t2_mem1*MAS_MEM[1]
	S += (c_paa_t21*MAS[1])-1 < c_paa_t4_t2_mem1*MAS_MEM[3]
	S += (c_paa_t21*MAS[2])-1 < c_paa_t4_t2_mem1*MAS_MEM[5]
	S += (c_paa_t21*MAS[3])-1 < c_paa_t4_t2_mem1*MAS_MEM[7]
	S += c_paa_t4_t2_mem1 <= c_paa_t4_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage1MAS4/FP12_INV_BEFORE_FPINV/schedule7.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

