from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 211
	S = Scenario("schedule10", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 0
	c_ab_t0_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 0
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 0
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=2, delay_cost=1)
	S += c_aa_t3_t2 >= 1
	c_aa_t3_t2 += MAS[2]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=7, delay_cost=1)
	S += c_ab_t0_t0 >= 1
	c_ab_t0_t0 += MM[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 1
	c_ab_t1_t1_in += MM_in[0]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=2, delay_cost=1)
	S += c_bb_a1_1 >= 1
	c_bb_a1_1 += MAS[2]

	c_bb_t10 = S.Task('c_bb_t10', length=2, delay_cost=1)
	S += c_bb_t10 >= 1
	c_bb_t10 += MAS[0]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=2, delay_cost=1)
	S += c_cc_a1_0 >= 1
	c_cc_a1_0 += MAS[3]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 1
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 1
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=2, delay_cost=1)
	S += c_cc_a1_1 >= 1
	c_cc_a1_1 += MAS[1]

	c_cc_t10 = S.Task('c_cc_t10', length=2, delay_cost=1)
	S += c_cc_t10 >= 1
	c_cc_t10 += MAS[1]

	c_cc_t11 = S.Task('c_cc_t11', length=2, delay_cost=1)
	S += c_cc_t11 >= 1
	c_cc_t11 += MAS[3]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=2, delay_cost=1)
	S += c_cc_t3_t2 >= 1
	c_cc_t3_t2 += MAS[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 2
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 2
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=7, delay_cost=1)
	S += c_ab_t1_t1 >= 2
	c_ab_t1_t1 += MM[0]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 2
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=2, delay_cost=1)
	S += c_aa_a1_0 >= 3
	c_aa_a1_0 += MAS[2]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=2, delay_cost=1)
	S += c_aa_a1_1 >= 3
	c_aa_a1_1 += MAS[3]

	c_aa_t11 = S.Task('c_aa_t11', length=2, delay_cost=1)
	S += c_aa_t11 >= 3
	c_aa_t11 += MAS[2]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=2, delay_cost=1)
	S += c_aa_t3_t3 >= 3
	c_aa_t3_t3 += MAS[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=7, delay_cost=1)
	S += c_ab_t0_t1 >= 3
	c_ab_t0_t1 += MM[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 3
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 3
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=2, delay_cost=1)
	S += c_bb_a1_0 >= 3
	c_bb_a1_0 += MAS[3]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=2, delay_cost=1)
	S += c_bb_t3_t2 >= 3
	c_bb_t3_t2 += MAS[1]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=2, delay_cost=1)
	S += c_bb_t3_t3 >= 3
	c_bb_t3_t3 += MAS[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 3
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=2, delay_cost=1)
	S += c_cc_t3_t3 >= 3
	c_cc_t3_t3 += MAS[1]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 4
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 4
	c_bb_t3_t1_in += MM_in[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 4
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=7, delay_cost=1)
	S += c_cc_t3_t1 >= 4
	c_cc_t3_t1 += MM[0]

	c_aa_t10 = S.Task('c_aa_t10', length=2, delay_cost=1)
	S += c_aa_t10 >= 5
	c_aa_t10 += MAS[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 5
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=2, delay_cost=1)
	S += c_ab_t0_t2 >= 5
	c_ab_t0_t2 += MAS[1]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=2, delay_cost=1)
	S += c_ab_t0_t3 >= 5
	c_ab_t0_t3 += MAS[3]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=2, delay_cost=1)
	S += c_ab_t1_t2 >= 5
	c_ab_t1_t2 += MAS[2]

	c_bb_t11 = S.Task('c_bb_t11', length=2, delay_cost=1)
	S += c_bb_t11 >= 5
	c_bb_t11 += MAS[0]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=7, delay_cost=1)
	S += c_bb_t3_t1 >= 5
	c_bb_t3_t1 += MM[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 5
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=2, delay_cost=1)
	S += c_bc_t0_t3 >= 5
	c_bc_t0_t3 += MAS[3]

	c_bc_t21 = S.Task('c_bc_t21', length=2, delay_cost=1)
	S += c_bc_t21 >= 5
	c_bc_t21 += MAS[1]

	c_bc_t31 = S.Task('c_bc_t31', length=2, delay_cost=1)
	S += c_bc_t31 >= 5
	c_bc_t31 += MAS[2]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 5
	c_cc_t3_t0_in += MM_in[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 6
	c_aa_t3_t0_in += MM_in[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 6
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 6
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=7, delay_cost=1)
	S += c_cc_t3_t0 >= 6
	c_cc_t3_t0 += MM[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 7
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=7, delay_cost=1)
	S += c_aa_t3_t0 >= 7
	c_aa_t3_t0 += MM[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 7
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t20 = S.Task('c_ab_t20', length=2, delay_cost=1)
	S += c_ab_t20 >= 7
	c_ab_t20 += MAS[2]

	c_ab_t30 = S.Task('c_ab_t30', length=2, delay_cost=1)
	S += c_ab_t30 >= 7
	c_ab_t30 += MAS[0]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=2, delay_cost=1)
	S += c_ac_t0_t2 >= 7
	c_ac_t0_t2 += MAS[1]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=2, delay_cost=1)
	S += c_ac_t1_t2 >= 7
	c_ac_t1_t2 += MAS[1]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=2, delay_cost=1)
	S += c_ac_t1_t3 >= 7
	c_ac_t1_t3 += MAS[0]

	c_ac_t20 = S.Task('c_ac_t20', length=2, delay_cost=1)
	S += c_ac_t20 >= 7
	c_ac_t20 += MAS[3]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 7
	c_bb_t3_t0_in += MM_in[0]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=2, delay_cost=1)
	S += c_bc_t0_t2 >= 7
	c_bc_t0_t2 += MAS[2]

	c_bc_t20 = S.Task('c_bc_t20', length=2, delay_cost=1)
	S += c_bc_t20 >= 7
	c_bc_t20 += MAS[3]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 8
	c_aa_t3_t1_in += MM_in[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 8
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=7, delay_cost=1)
	S += c_bb_t3_t0 >= 8
	c_bb_t3_t0 += MM[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 8
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=7, delay_cost=1)
	S += c_aa_t3_t1 >= 9
	c_aa_t3_t1 += MM[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 9
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t21 = S.Task('c_ab_t21', length=2, delay_cost=1)
	S += c_ab_t21 >= 9
	c_ab_t21 += MAS[0]

	c_ab_t31 = S.Task('c_ab_t31', length=2, delay_cost=1)
	S += c_ab_t31 >= 9
	c_ab_t31 += MAS[2]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=2, delay_cost=1)
	S += c_ac_t0_t3 >= 9
	c_ac_t0_t3 += MAS[1]

	c_ac_t21 = S.Task('c_ac_t21', length=2, delay_cost=1)
	S += c_ac_t21 >= 9
	c_ac_t21 += MAS[0]

	c_ac_t31 = S.Task('c_ac_t31', length=2, delay_cost=1)
	S += c_ac_t31 >= 9
	c_ac_t31 += MAS[1]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 9
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=2, delay_cost=1)
	S += c_bc_t1_t2 >= 9
	c_bc_t1_t2 += MAS[3]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=2, delay_cost=1)
	S += c_bc_t1_t3 >= 9
	c_bc_t1_t3 += MAS[2]

	c_bc_t30 = S.Task('c_bc_t30', length=2, delay_cost=1)
	S += c_bc_t30 >= 9
	c_bc_t30 += MAS[3]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 9
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 10
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=7, delay_cost=1)
	S += c_ab_t1_t0 >= 10
	c_ab_t1_t0 += MM[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 10
	c_bc_t1_t0_in += MM_in[0]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 10
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=2, delay_cost=1)
	S += c_ab_t1_t3 >= 11
	c_ab_t1_t3 += MAS[3]

	c_ac_t30 = S.Task('c_ac_t30', length=2, delay_cost=1)
	S += c_ac_t30 >= 11
	c_ac_t30 += MAS[0]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 11
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 11
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=7, delay_cost=1)
	S += c_bc_t1_t0 >= 11
	c_bc_t1_t0 += MM[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 11
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=2, delay_cost=1)
	S += c_paa_t0_t3 >= 11
	c_paa_t0_t3 += MAS[1]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=2, delay_cost=1)
	S += c_paa_t1_t3 >= 11
	c_paa_t1_t3 += MAS[2]

	c_paa_t30 = S.Task('c_paa_t30', length=2, delay_cost=1)
	S += c_paa_t30 >= 11
	c_paa_t30 += MAS[2]

	c_paa_t31 = S.Task('c_paa_t31', length=2, delay_cost=1)
	S += c_paa_t31 >= 11
	c_paa_t31 += MAS[3]

	c_pcb_t30 = S.Task('c_pcb_t30', length=2, delay_cost=1)
	S += c_pcb_t30 >= 11
	c_pcb_t30 += MAS[1]

	c_pcb_t31 = S.Task('c_pcb_t31', length=2, delay_cost=1)
	S += c_pcb_t31 >= 11
	c_pcb_t31 += MAS[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 12
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 12
	c_ac_t0_t0_in += MM_in[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 12
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=7, delay_cost=1)
	S += c_bc_t0_t1 >= 12
	c_bc_t0_t1 += MM[0]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 12
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 12
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 13
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 13
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 13
	c_ab_t00_mem1 += MM_MEM[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=7, delay_cost=1)
	S += c_ac_t0_t0 >= 13
	c_ac_t0_t0 += MM[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 13
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 13
	c_bc_t0_t0_in += MM_in[0]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=2, delay_cost=1)
	S += c_cc_t3_t5 >= 13
	c_cc_t3_t5 += MAS[1]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=2, delay_cost=1)
	S += c_pbc_t0_t3 >= 13
	c_pbc_t0_t3 += MAS[0]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=2, delay_cost=1)
	S += c_pbc_t1_t3 >= 13
	c_pbc_t1_t3 += MAS[0]

	c_pbc_t30 = S.Task('c_pbc_t30', length=2, delay_cost=1)
	S += c_pbc_t30 >= 13
	c_pbc_t30 += MAS[3]

	c_pbc_t31 = S.Task('c_pbc_t31', length=2, delay_cost=1)
	S += c_pbc_t31 >= 13
	c_pbc_t31 += MAS[3]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=2, delay_cost=1)
	S += c_pcb_t0_t3 >= 13
	c_pcb_t0_t3 += MAS[2]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=2, delay_cost=1)
	S += c_pcb_t1_t3 >= 13
	c_pcb_t1_t3 += MAS[2]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 14
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_ab_t00 = S.Task('c_ab_t00', length=2, delay_cost=1)
	S += c_ab_t00 >= 14
	c_ab_t00 += MAS[1]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 14
	c_ab_t4_t2_mem0 += MAS_MEM[4]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 14
	c_ab_t4_t2_mem1 += MAS_MEM[1]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 14
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 14
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 14
	c_ac_t4_t3_mem1 += MAS_MEM[3]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=7, delay_cost=1)
	S += c_bc_t0_t0 >= 14
	c_bc_t0_t0 += MM[0]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 14
	c_bc_t4_t3_mem0 += MAS_MEM[6]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 14
	c_bc_t4_t3_mem1 += MAS_MEM[5]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 14
	c_cc_t2_t3_mem0 += MAS_MEM[2]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 14
	c_cc_t2_t3_mem1 += MAS_MEM[7]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 14
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 14
	c_cc_t30_mem1 += MM_MEM[1]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 14
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 15
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 15
	c_aa_t2_t3_mem0 += MAS_MEM[0]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 15
	c_aa_t2_t3_mem1 += MAS_MEM[5]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 15
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 15
	c_aa_t30_mem1 += MM_MEM[1]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=2, delay_cost=1)
	S += c_ab_t4_t2 >= 15
	c_ab_t4_t2 += MAS[2]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 15
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=7, delay_cost=1)
	S += c_ac_t1_t1 >= 15
	c_ac_t1_t1 += MM[0]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 15
	c_ac_t4_t2_mem0 += MAS_MEM[6]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 15
	c_ac_t4_t2_mem1 += MAS_MEM[1]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=2, delay_cost=1)
	S += c_ac_t4_t3 >= 15
	c_ac_t4_t3 += MAS[2]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=2, delay_cost=1)
	S += c_bc_t4_t3 >= 15
	c_bc_t4_t3 += MAS[1]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=2, delay_cost=1)
	S += c_cc_t2_t3 >= 15
	c_cc_t2_t3 += MAS[3]

	c_cc_t30 = S.Task('c_cc_t30', length=2, delay_cost=1)
	S += c_cc_t30 >= 15
	c_cc_t30 += MAS[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 15
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 16
	c_aa_t01_mem1 += MAS_MEM[7]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=2, delay_cost=1)
	S += c_aa_t2_t3 >= 16
	c_aa_t2_t3 += MAS[0]

	c_aa_t30 = S.Task('c_aa_t30', length=2, delay_cost=1)
	S += c_aa_t30 >= 16
	c_aa_t30 += MAS[3]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 16
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 16
	c_ab_t4_t3_mem0 += MAS_MEM[0]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 16
	c_ab_t4_t3_mem1 += MAS_MEM[5]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 16
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=7, delay_cost=1)
	S += c_ac_t1_t0 >= 16
	c_ac_t1_t0 += MM[0]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=2, delay_cost=1)
	S += c_ac_t4_t2 >= 16
	c_ac_t4_t2 += MAS[1]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 16
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 16
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 16
	c_bb_t30_mem1 += MM_MEM[1]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 16
	c_bc_t4_t2_mem0 += MAS_MEM[6]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 16
	c_bc_t4_t2_mem1 += MAS_MEM[3]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 16
	c_pcb_t4_t3_mem0 += MAS_MEM[2]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 16
	c_pcb_t4_t3_mem1 += MAS_MEM[1]

	c_aa_t01 = S.Task('c_aa_t01', length=2, delay_cost=1)
	S += c_aa_t01 >= 17
	c_aa_t01 += MAS[0]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 17
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 17
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 17
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=2, delay_cost=1)
	S += c_ab_t4_t3 >= 17
	c_ab_t4_t3 += MAS[3]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=7, delay_cost=1)
	S += c_ac_t0_t1 >= 17
	c_ac_t0_t1 += MM[0]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 17
	c_bb_t2_t3_mem0 += MAS_MEM[0]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 17
	c_bb_t2_t3_mem1 += MAS_MEM[1]

	c_bb_t30 = S.Task('c_bb_t30', length=2, delay_cost=1)
	S += c_bb_t30 >= 17
	c_bb_t30 += MAS[1]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 17
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=2, delay_cost=1)
	S += c_bc_t4_t2 >= 17
	c_bc_t4_t2 += MAS[2]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 17
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 17
	c_pbc_t4_t3_mem0 += MAS_MEM[6]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 17
	c_pbc_t4_t3_mem1 += MAS_MEM[7]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=2, delay_cost=1)
	S += c_pcb_t4_t3 >= 17
	c_pcb_t4_t3 += MAS[2]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 18
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 18
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 18
	c_aa_t3_t4_mem0 += MAS_MEM[4]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 18
	c_aa_t3_t4_mem1 += MAS_MEM[1]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=2, delay_cost=1)
	S += c_ab_t0_t5 >= 18
	c_ab_t0_t5 += MAS[3]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 18
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 18
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 18
	c_bb_t01_mem1 += MAS_MEM[5]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=2, delay_cost=1)
	S += c_bb_t2_t3 >= 18
	c_bb_t2_t3 += MAS[0]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=7, delay_cost=1)
	S += c_bc_t1_t1 >= 18
	c_bc_t1_t1 += MM[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 18
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 18
	c_cc_t00_mem1 += MAS_MEM[7]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 18
	c_cc_t01_mem1 += MAS_MEM[3]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=2, delay_cost=1)
	S += c_pbc_t4_t3 >= 18
	c_pbc_t4_t3 += MAS[1]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 19
	c_aa10_mem0 += MAS_MEM[6]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 19
	c_aa_t00_mem1 += MAS_MEM[5]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=7, delay_cost=1)
	S += c_aa_t3_t4 >= 19
	c_aa_t3_t4 += MM[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 19
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 19
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=2, delay_cost=1)
	S += c_ab_t1_t5 >= 19
	c_ab_t1_t5 += MAS[2]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 19
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 19
	c_ac_t1_t4_mem0 += MAS_MEM[2]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 19
	c_ac_t1_t4_mem1 += MAS_MEM[1]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 19
	c_bb_t00_mem1 += MAS_MEM[7]

	c_bb_t01 = S.Task('c_bb_t01', length=2, delay_cost=1)
	S += c_bb_t01 >= 19
	c_bb_t01 += MAS[2]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 19
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 19
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_cc_t00 = S.Task('c_cc_t00', length=2, delay_cost=1)
	S += c_cc_t00 >= 19
	c_cc_t00 += MAS[1]

	c_cc_t01 = S.Task('c_cc_t01', length=2, delay_cost=1)
	S += c_cc_t01 >= 19
	c_cc_t01 += MAS[0]

	c_aa10 = S.Task('c_aa10', length=2, delay_cost=1)
	S += c_aa10 >= 20
	c_aa10 += MAS[1]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 20
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t00 = S.Task('c_aa_t00', length=2, delay_cost=1)
	S += c_aa_t00 >= 20
	c_aa_t00 += MAS[3]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=7, delay_cost=1)
	S += c_ac_t1_t4 >= 20
	c_ac_t1_t4 += MM[0]

	c_bb_t00 = S.Task('c_bb_t00', length=2, delay_cost=1)
	S += c_bb_t00 >= 20
	c_bb_t00 += MAS[3]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=2, delay_cost=1)
	S += c_bb_t3_t5 >= 20
	c_bb_t3_t5 += MAS[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 20
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 20
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 20
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 20
	c_bc_t4_t0_mem0 += MAS_MEM[6]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 20
	c_bc_t4_t0_mem1 += MAS_MEM[7]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 20
	c_cc10_mem0 += MAS_MEM[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 20
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 20
	c_cc_t2_t2_mem0 += MAS_MEM[2]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 20
	c_cc_t2_t2_mem1 += MAS_MEM[1]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 21
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 21
	c_ab_t10_mem1 += MM_MEM[1]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 21
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 21
	c_ab_t4_t0_mem0 += MAS_MEM[4]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 21
	c_ab_t4_t0_mem1 += MAS_MEM[1]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 21
	c_bb10_mem0 += MAS_MEM[2]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 21
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 21
	c_bb_t2_t2_mem0 += MAS_MEM[6]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 21
	c_bb_t2_t2_mem1 += MAS_MEM[5]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=2, delay_cost=1)
	S += c_bc_t0_t5 >= 21
	c_bc_t0_t5 += MAS[0]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=7, delay_cost=1)
	S += c_bc_t4_t0 >= 21
	c_bc_t4_t0 += MM[0]

	c_cc10 = S.Task('c_cc10', length=2, delay_cost=1)
	S += c_cc10 >= 21
	c_cc10 += MAS[2]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=2, delay_cost=1)
	S += c_cc_t2_t2 >= 21
	c_cc_t2_t2 += MAS[1]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 21
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 22
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t10 = S.Task('c_ab_t10', length=2, delay_cost=1)
	S += c_ab_t10 >= 22
	c_ab_t10 += MAS[2]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=7, delay_cost=1)
	S += c_ab_t4_t0 >= 22
	c_ab_t4_t0 += MM[0]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 22
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 22
	c_ac_t10_mem1 += MM_MEM[1]

	c_bb10 = S.Task('c_bb10', length=2, delay_cost=1)
	S += c_bb10 >= 22
	c_bb10 += MAS[0]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=2, delay_cost=1)
	S += c_bb_t2_t2 >= 22
	c_bb_t2_t2 += MAS[3]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 22
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 22
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 22
	c_bb_t3_t4_mem0 += MAS_MEM[2]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 22
	c_bb_t3_t4_mem1 += MAS_MEM[1]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 22
	c_paa_t4_t3_mem0 += MAS_MEM[4]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 22
	c_paa_t4_t3_mem1 += MAS_MEM[7]

	c_ac_t10 = S.Task('c_ac_t10', length=2, delay_cost=1)
	S += c_ac_t10 >= 23
	c_ac_t10 += MAS[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 23
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 23
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 23
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=7, delay_cost=1)
	S += c_bb_t3_t4 >= 23
	c_bb_t3_t4 += MM[0]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 23
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 23
	c_bc_t1_t4_mem0 += MAS_MEM[6]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 23
	c_bc_t1_t4_mem1 += MAS_MEM[5]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 23
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=2, delay_cost=1)
	S += c_paa_t4_t3 >= 23
	c_paa_t4_t3 += MAS[2]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 24
	c_aa_t2_t2_mem0 += MAS_MEM[6]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 24
	c_aa_t2_t2_mem1 += MAS_MEM[1]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 24
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 24
	c_ab_t50_mem0 += MAS_MEM[2]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 24
	c_ab_t50_mem1 += MAS_MEM[5]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=2, delay_cost=1)
	S += c_ac_t1_t5 >= 24
	c_ac_t1_t5 += MAS[2]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 24
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 24
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 24
	c_bc_t0_t4_mem0 += MAS_MEM[4]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 24
	c_bc_t0_t4_mem1 += MAS_MEM[7]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=7, delay_cost=1)
	S += c_bc_t1_t4 >= 24
	c_bc_t1_t4 += MM[0]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 24
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 24
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=2, delay_cost=1)
	S += c_aa_t2_t2 >= 25
	c_aa_t2_t2 += MAS[2]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 25
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 25
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t50 = S.Task('c_ab_t50', length=2, delay_cost=1)
	S += c_ab_t50 >= 25
	c_ab_t50 += MAS[0]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 25
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 25
	c_ac_t00_mem1 += MM_MEM[1]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 25
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 25
	c_ac_t0_t4_mem0 += MAS_MEM[2]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 25
	c_ac_t0_t4_mem1 += MAS_MEM[3]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=7, delay_cost=1)
	S += c_bc_t0_t4 >= 25
	c_bc_t0_t4 += MM[0]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=2, delay_cost=1)
	S += c_bc_t1_t5 >= 25
	c_bc_t1_t5 += MAS[3]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 26
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t00 = S.Task('c_ac_t00', length=2, delay_cost=1)
	S += c_ac_t00 >= 26
	c_ac_t00 += MAS[0]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=7, delay_cost=1)
	S += c_ac_t0_t4 >= 26
	c_ac_t0_t4 += MM[0]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 26
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 26
	c_bc_t10_mem1 += MM_MEM[1]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 26
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 26
	c_bc_t4_t1_mem0 += MAS_MEM[2]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 26
	c_bc_t4_t1_mem1 += MAS_MEM[5]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 26
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 27
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 27
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 27
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 27
	c_ab_t1_t4_mem0 += MAS_MEM[4]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 27
	c_ab_t1_t4_mem1 += MAS_MEM[7]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 27
	c_ac_t50_mem0 += MAS_MEM[0]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 27
	c_ac_t50_mem1 += MAS_MEM[1]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 27
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 27
	c_bc_t00_mem1 += MM_MEM[1]

	c_bc_t10 = S.Task('c_bc_t10', length=2, delay_cost=1)
	S += c_bc_t10 >= 27
	c_bc_t10 += MAS[1]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=7, delay_cost=1)
	S += c_bc_t4_t1 >= 27
	c_bc_t4_t1 += MM[0]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 28
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=7, delay_cost=1)
	S += c_ab_t1_t4 >= 28
	c_ab_t1_t4 += MM[0]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 28
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 28
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_ac_t50 = S.Task('c_ac_t50', length=2, delay_cost=1)
	S += c_ac_t50 >= 28
	c_ac_t50 += MAS[1]

	c_bc_t00 = S.Task('c_bc_t00', length=2, delay_cost=1)
	S += c_bc_t00 >= 28
	c_bc_t00 += MAS[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 28
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 28
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 28
	c_cc_t3_t4_mem0 += MAS_MEM[0]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 28
	c_cc_t3_t4_mem1 += MAS_MEM[3]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 29
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 29
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 29
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=2, delay_cost=1)
	S += c_ac_t0_t5 >= 29
	c_ac_t0_t5 += MAS[2]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 29
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 29
	c_ac_t4_t0_mem0 += MAS_MEM[6]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 29
	c_ac_t4_t0_mem1 += MAS_MEM[1]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 29
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 29
	c_bc_t50_mem0 += MAS_MEM[0]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 29
	c_bc_t50_mem1 += MAS_MEM[3]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=7, delay_cost=1)
	S += c_cc_t3_t4 >= 29
	c_cc_t3_t4 += MM[0]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=2, delay_cost=1)
	S += c_aa_t3_t5 >= 30
	c_aa_t3_t5 += MAS[0]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 30
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=7, delay_cost=1)
	S += c_ac_t4_t0 >= 30
	c_ac_t4_t0 += MM[0]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 30
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 30
	c_ac_t4_t1_mem0 += MAS_MEM[0]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 30
	c_ac_t4_t1_mem1 += MAS_MEM[3]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 30
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 30
	c_bc_t11_mem1 += MAS_MEM[7]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 30
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t50 = S.Task('c_bc_t50', length=2, delay_cost=1)
	S += c_bc_t50 >= 30
	c_bc_t50 += MAS[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 31
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 31
	c_ab_t4_t1_mem0 += MAS_MEM[0]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 31
	c_ab_t4_t1_mem1 += MAS_MEM[5]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 31
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=7, delay_cost=1)
	S += c_ac_t4_t1 >= 31
	c_ac_t4_t1 += MM[0]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 31
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 31
	c_bb_t31_mem1 += MAS_MEM[1]

	c_bc_t11 = S.Task('c_bc_t11', length=2, delay_cost=1)
	S += c_bc_t11 >= 31
	c_bc_t11 += MAS[3]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 31
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 32
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 32
	c_ab_t0_t4_mem0 += MAS_MEM[2]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 32
	c_ab_t0_t4_mem1 += MAS_MEM[7]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=7, delay_cost=1)
	S += c_ab_t4_t1 >= 32
	c_ab_t4_t1 += MM[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 32
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 32
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t31 = S.Task('c_bb_t31', length=2, delay_cost=1)
	S += c_bb_t31 >= 32
	c_bb_t31 += MAS[0]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 32
	c_bc_s01_mem0 += MAS_MEM[6]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 32
	c_bc_s01_mem1 += MAS_MEM[3]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 32
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 32
	c_bc_t01_mem1 += MAS_MEM[1]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 33
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 33
	c_aa_t2_t0_mem0 += MAS_MEM[6]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 33
	c_aa_t2_t0_mem1 += MAS_MEM[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=7, delay_cost=1)
	S += c_ab_t0_t4 >= 33
	c_ab_t0_t4 += MM[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 33
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 33
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 33
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 33
	c_ac_t11_mem1 += MAS_MEM[5]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 33
	c_bb_t41_mem0 += MAS_MEM[0]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 33
	c_bb_t41_mem1 += MAS_MEM[3]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 33
	c_bc_s00_mem0 += MAS_MEM[2]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 33
	c_bc_s00_mem1 += MAS_MEM[7]

	c_bc_s01 = S.Task('c_bc_s01', length=2, delay_cost=1)
	S += c_bc_s01 >= 33
	c_bc_s01 += MAS[1]

	c_bc_t01 = S.Task('c_bc_t01', length=2, delay_cost=1)
	S += c_bc_t01 >= 33
	c_bc_t01 += MAS[0]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=7, delay_cost=1)
	S += c_aa_t2_t0 >= 34
	c_aa_t2_t0 += MM[0]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 34
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 34
	c_aa_t31_mem1 += MAS_MEM[1]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 34
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t11 = S.Task('c_ac_t11', length=2, delay_cost=1)
	S += c_ac_t11 >= 34
	c_ac_t11 += MAS[1]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 34
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t41 = S.Task('c_bb_t41', length=2, delay_cost=1)
	S += c_bb_t41 >= 34
	c_bb_t41 += MAS[0]

	c_bc_s00 = S.Task('c_bc_s00', length=2, delay_cost=1)
	S += c_bc_s00 >= 34
	c_bc_s00 += MAS[2]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 34
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 34
	c_cc_t2_t1_mem0 += MAS_MEM[0]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 34
	c_cc_t2_t1_mem1 += MAS_MEM[7]

	c_aa_t31 = S.Task('c_aa_t31', length=2, delay_cost=1)
	S += c_aa_t31 >= 35
	c_aa_t31 += MAS[0]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 35
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 35
	c_ab_t11_mem1 += MAS_MEM[5]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 35
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 35
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 35
	c_bc_t51_mem0 += MAS_MEM[0]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 35
	c_bc_t51_mem1 += MAS_MEM[7]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 35
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 35
	c_cc_t2_t0_mem0 += MAS_MEM[2]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 35
	c_cc_t2_t0_mem1 += MAS_MEM[3]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=7, delay_cost=1)
	S += c_cc_t2_t1 >= 35
	c_cc_t2_t1 += MM[0]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 36
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 36
	c_aa_t2_t1_mem0 += MAS_MEM[0]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 36
	c_aa_t2_t1_mem1 += MAS_MEM[5]

	c_ab_t11 = S.Task('c_ab_t11', length=2, delay_cost=1)
	S += c_ab_t11 >= 36
	c_ab_t11 += MAS[1]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 36
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 36
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 36
	c_bb_t40_mem0 += MAS_MEM[2]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 36
	c_bb_t40_mem1 += MAS_MEM[1]

	c_bc_t51 = S.Task('c_bc_t51', length=2, delay_cost=1)
	S += c_bc_t51 >= 36
	c_bc_t51 += MAS[1]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=7, delay_cost=1)
	S += c_cc_t2_t0 >= 36
	c_cc_t2_t0 += MM[0]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 36
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 36
	c_cc_t31_mem1 += MAS_MEM[3]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=7, delay_cost=1)
	S += c_aa_t2_t1 >= 37
	c_aa_t2_t1 += MM[0]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 37
	c_aa_t41_mem0 += MAS_MEM[0]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 37
	c_aa_t41_mem1 += MAS_MEM[7]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 37
	c_ac_s01_mem0 += MAS_MEM[2]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 37
	c_ac_s01_mem1 += MAS_MEM[1]

	c_bb_t40 = S.Task('c_bb_t40', length=2, delay_cost=1)
	S += c_bb_t40 >= 37
	c_bb_t40 += MAS[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 37
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 37
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 37
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 37
	c_bc_t40_mem1 += MM_MEM[1]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 37
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 37
	c_bc_t4_t4_mem0 += MAS_MEM[4]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 37
	c_bc_t4_t4_mem1 += MAS_MEM[3]

	c_cc_t31 = S.Task('c_cc_t31', length=2, delay_cost=1)
	S += c_cc_t31 >= 37
	c_cc_t31 += MAS[0]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 38
	c_aa_t40_mem0 += MAS_MEM[6]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 38
	c_aa_t40_mem1 += MAS_MEM[1]

	c_aa_t41 = S.Task('c_aa_t41', length=2, delay_cost=1)
	S += c_aa_t41 >= 38
	c_aa_t41 += MAS[1]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 38
	c_ab_s00_mem0 += MAS_MEM[4]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 38
	c_ab_s00_mem1 += MAS_MEM[3]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 38
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 38
	c_ab_t40_mem1 += MM_MEM[1]

	c_ac_s01 = S.Task('c_ac_s01', length=2, delay_cost=1)
	S += c_ac_s01 >= 38
	c_ac_s01 += MAS[3]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 38
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 38
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 38
	c_ac_t4_t4_mem0 += MAS_MEM[2]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 38
	c_ac_t4_t4_mem1 += MAS_MEM[5]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 38
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t40 = S.Task('c_bc_t40', length=2, delay_cost=1)
	S += c_bc_t40 >= 38
	c_bc_t40 += MAS[2]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=7, delay_cost=1)
	S += c_bc_t4_t4 >= 38
	c_bc_t4_t4 += MM[0]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 38
	c_cc11_mem0 += MAS_MEM[0]

	c_aa_t40 = S.Task('c_aa_t40', length=2, delay_cost=1)
	S += c_aa_t40 >= 39
	c_aa_t40 += MAS[1]

	c_ab_s00 = S.Task('c_ab_s00', length=2, delay_cost=1)
	S += c_ab_s00 >= 39
	c_ab_s00 += MAS[0]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 39
	c_ab_s01_mem0 += MAS_MEM[2]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 39
	c_ab_s01_mem1 += MAS_MEM[5]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 39
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 39
	c_ab_t01_mem1 += MAS_MEM[7]

	c_ab_t40 = S.Task('c_ab_t40', length=2, delay_cost=1)
	S += c_ab_t40 >= 39
	c_ab_t40 += MAS[2]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 39
	c_ac_s00_mem0 += MAS_MEM[0]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 39
	c_ac_s00_mem1 += MAS_MEM[3]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 39
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=7, delay_cost=1)
	S += c_ac_t4_t4 >= 39
	c_ac_t4_t4 += MM[0]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 39
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 39
	c_bb_t2_t0_mem0 += MAS_MEM[6]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 39
	c_bb_t2_t0_mem1 += MAS_MEM[1]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 39
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_cc11 = S.Task('c_cc11', length=2, delay_cost=1)
	S += c_cc11 >= 39
	c_cc11 += MAS[3]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 40
	c_aa11_mem0 += MAS_MEM[0]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	S += c_aa_t50_mem0 >= 40
	c_aa_t50_mem0 += MAS_MEM[6]

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	S += c_aa_t50_mem1 >= 40
	c_aa_t50_mem1 += MAS_MEM[3]

	c_ab_s01 = S.Task('c_ab_s01', length=2, delay_cost=1)
	S += c_ab_s01 >= 40
	c_ab_s01 += MAS[2]

	c_ab_t01 = S.Task('c_ab_t01', length=2, delay_cost=1)
	S += c_ab_t01 >= 40
	c_ab_t01 += MAS[1]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 40
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_s00 = S.Task('c_ac_s00', length=2, delay_cost=1)
	S += c_ac_s00 >= 40
	c_ac_s00 += MAS[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 40
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 40
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 40
	c_ac_t40_mem1 += MM_MEM[1]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=7, delay_cost=1)
	S += c_bb_t2_t0 >= 40
	c_bb_t2_t0 += MM[0]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 40
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 40
	c_bb_t2_t1_mem0 += MAS_MEM[4]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 40
	c_bb_t2_t1_mem1 += MAS_MEM[1]

	c_aa11 = S.Task('c_aa11', length=2, delay_cost=1)
	S += c_aa11 >= 41
	c_aa11 += MAS[1]

	c_aa_t50 = S.Task('c_aa_t50', length=2, delay_cost=1)
	S += c_aa_t50 >= 41
	c_aa_t50 += MAS[2]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 41
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 41
	c_ab_t4_t4_mem0 += MAS_MEM[4]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 41
	c_ab_t4_t4_mem1 += MAS_MEM[7]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 41
	c_ab_t51_mem0 += MAS_MEM[2]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 41
	c_ab_t51_mem1 += MAS_MEM[3]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 41
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 41
	c_ac_t01_mem1 += MAS_MEM[5]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 41
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t40 = S.Task('c_ac_t40', length=2, delay_cost=1)
	S += c_ac_t40 >= 41
	c_ac_t40 += MAS[0]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=7, delay_cost=1)
	S += c_bb_t2_t1 >= 41
	c_bb_t2_t1 += MM[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 41
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 41
	c_cc_t41_mem0 += MAS_MEM[0]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 41
	c_cc_t41_mem1 += MAS_MEM[1]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 42
	c_ab10_mem0 += MAS_MEM[4]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 42
	c_ab10_mem1 += MAS_MEM[1]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 42
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=7, delay_cost=1)
	S += c_ab_t4_t4 >= 42
	c_ab_t4_t4 += MM[0]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 42
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 42
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ab_t51 = S.Task('c_ab_t51', length=2, delay_cost=1)
	S += c_ab_t51 >= 42
	c_ab_t51 += MAS[3]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 42
	c_ac10_mem0 += MAS_MEM[0]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 42
	c_ac10_mem1 += MAS_MEM[3]

	c_ac_t01 = S.Task('c_ac_t01', length=2, delay_cost=1)
	S += c_ac_t01 >= 42
	c_ac_t01 += MAS[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 42
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 42
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 42
	c_cc_t2_t4_mem0 += MAS_MEM[2]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 42
	c_cc_t2_t4_mem1 += MAS_MEM[7]

	c_cc_t41 = S.Task('c_cc_t41', length=2, delay_cost=1)
	S += c_cc_t41 >= 42
	c_cc_t41 += MAS[1]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem0 >= 42
	c_ccxi_y1_1_mem0 += MAS_MEM[6]

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem1 >= 42
	c_ccxi_y1_1_mem1 += MAS_MEM[5]

	c_ab10 = S.Task('c_ab10', length=2, delay_cost=1)
	S += c_ab10 >= 43
	c_ab10 += MAS[2]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=2, delay_cost=1)
	S += c_ab_t4_t5 >= 43
	c_ab_t4_t5 += MAS[3]

	c_ac10 = S.Task('c_ac10', length=2, delay_cost=1)
	S += c_ac10 >= 43
	c_ac10 += MAS[0]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 43
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 43
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 43
	c_ac_t51_mem0 += MAS_MEM[0]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 43
	c_ac_t51_mem1 += MAS_MEM[3]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 43
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 43
	c_bb_t2_t4_mem0 += MAS_MEM[6]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 43
	c_bb_t2_t4_mem1 += MAS_MEM[1]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 43
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 43
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=7, delay_cost=1)
	S += c_cc_t2_t4 >= 43
	c_cc_t2_t4 += MM[0]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem0 >= 43
	c_ccxi_y1_0_mem0 += MAS_MEM[4]

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem1 >= 43
	c_ccxi_y1_0_mem1 += MAS_MEM[7]

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=2, delay_cost=1)
	S += c_ccxi_y1_1 >= 43
	c_ccxi_y1_1 += MAS[1]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 44
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 44
	c_aa_t2_t4_mem0 += MAS_MEM[4]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 44
	c_aa_t2_t4_mem1 += MAS_MEM[1]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	S += c_ab01_mem0 >= 44
	c_ab01_mem0 += MAS_MEM[2]

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	S += c_ab01_mem1 >= 44
	c_ab01_mem1 += MAS_MEM[5]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 44
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 44
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=2, delay_cost=1)
	S += c_ac_t4_t5 >= 44
	c_ac_t4_t5 += MAS[1]

	c_ac_t51 = S.Task('c_ac_t51', length=2, delay_cost=1)
	S += c_ac_t51 >= 44
	c_ac_t51 += MAS[3]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 44
	c_bb11_mem0 += MAS_MEM[0]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=7, delay_cost=1)
	S += c_bb_t2_t4 >= 44
	c_bb_t2_t4 += MM[0]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 44
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 44
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=2, delay_cost=1)
	S += c_ccxi_y1_0 >= 44
	c_ccxi_y1_0 += MAS[2]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=7, delay_cost=1)
	S += c_aa_t2_t4 >= 45
	c_aa_t2_t4 += MM[0]

	c_ab01 = S.Task('c_ab01', length=2, delay_cost=1)
	S += c_ab01 >= 45
	c_ab01 += MAS[3]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 45
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 45
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 45
	c_ac_t41_mem1 += MAS_MEM[3]

	c_bb11 = S.Task('c_bb11', length=2, delay_cost=1)
	S += c_bb11 >= 45
	c_bb11 += MAS[1]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	S += c_bc00_mem0 >= 45
	c_bc00_mem0 += MAS_MEM[0]

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	S += c_bc00_mem1 >= 45
	c_bc00_mem1 += MAS_MEM[5]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 45
	c_bc10_mem0 += MAS_MEM[4]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 45
	c_bc10_mem1 += MAS_MEM[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 45
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=2, delay_cost=1)
	S += c_bc_t4_t5 >= 45
	c_bc_t4_t5 += MAS[2]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 46
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 46
	c_aa_t2_t5_mem1 += MM_MEM[1]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 46
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t41 = S.Task('c_ac_t41', length=2, delay_cost=1)
	S += c_ac_t41 >= 46
	c_ac_t41 += MAS[2]

	c_bc00 = S.Task('c_bc00', length=2, delay_cost=1)
	S += c_bc00 >= 46
	c_bc00 += MAS[1]

	c_bc10 = S.Task('c_bc10', length=2, delay_cost=1)
	S += c_bc10 >= 46
	c_bc10 += MAS[0]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 46
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 46
	c_cc_t40_mem0 += MAS_MEM[0]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 46
	c_cc_t40_mem1 += MAS_MEM[1]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	S += c_pb01_mem0 >= 46
	c_pb01_mem0 += MAS_MEM[2]

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	S += c_pb01_mem1 >= 46
	c_pb01_mem1 += MAS_MEM[7]

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=2, delay_cost=1)
	S += c_aa_t2_t5 >= 47
	c_aa_t2_t5 += MAS[3]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	S += c_aa_t51_mem0 >= 47
	c_aa_t51_mem0 += MAS_MEM[0]

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	S += c_aa_t51_mem1 >= 47
	c_aa_t51_mem1 += MAS_MEM[3]

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	S += c_ab00_mem0 >= 47
	c_ab00_mem0 += MAS_MEM[2]

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	S += c_ab00_mem1 >= 47
	c_ab00_mem1 += MAS_MEM[1]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 47
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	S += c_ac11_mem0 >= 47
	c_ac11_mem0 += MAS_MEM[4]

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	S += c_ac11_mem1 >= 47
	c_ac11_mem1 += MAS_MEM[7]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 47
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 47
	c_bb_t20_mem1 += MM_MEM[1]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 47
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t40 = S.Task('c_cc_t40', length=2, delay_cost=1)
	S += c_cc_t40 >= 47
	c_cc_t40 += MAS[0]

	c_pb01 = S.Task('c_pb01', length=2, delay_cost=1)
	S += c_pb01 >= 47
	c_pb01 += MAS[3]

	c_aa_t51 = S.Task('c_aa_t51', length=2, delay_cost=1)
	S += c_aa_t51 >= 48
	c_aa_t51 += MAS[1]

	c_ab00 = S.Task('c_ab00', length=2, delay_cost=1)
	S += c_ab00 >= 48
	c_ab00 += MAS[2]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 48
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	S += c_ac00_mem0 >= 48
	c_ac00_mem0 += MAS_MEM[0]

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	S += c_ac00_mem1 >= 48
	c_ac00_mem1 += MAS_MEM[1]

	c_ac11 = S.Task('c_ac11', length=2, delay_cost=1)
	S += c_ac11 >= 48
	c_ac11 += MAS[0]

	c_bb_t20 = S.Task('c_bb_t20', length=2, delay_cost=1)
	S += c_bb_t20 >= 48
	c_bb_t20 += MAS[2]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 48
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 48
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 48
	c_bc_t41_mem1 += MAS_MEM[5]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	S += c_pa10_mem0 >= 48
	c_pa10_mem0 += MAS_MEM[2]

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	S += c_pa10_mem1 >= 48
	c_pa10_mem1 += MAS_MEM[3]

	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	S += c_pbc_t0_t1_in >= 48
	c_pbc_t0_t1_in += MM_in[0]

	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem0 >= 48
	c_pbc_t0_t1_mem0 += MAS_MEM[6]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 49
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 49
	c_ab_t41_mem1 += MAS_MEM[7]

	c_ac00 = S.Task('c_ac00', length=2, delay_cost=1)
	S += c_ac00 >= 49
	c_ac00 += MAS[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 49
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	S += c_bb_t50_mem0 >= 49
	c_bb_t50_mem0 += MAS_MEM[2]

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	S += c_bb_t50_mem1 >= 49
	c_bb_t50_mem1 += MAS_MEM[1]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	S += c_bc01_mem0 >= 49
	c_bc01_mem0 += MAS_MEM[0]

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	S += c_bc01_mem1 >= 49
	c_bc01_mem1 += MAS_MEM[3]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 49
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t41 = S.Task('c_bc_t41', length=2, delay_cost=1)
	S += c_bc_t41 >= 49
	c_bc_t41 += MAS[1]

	c_pa10 = S.Task('c_pa10', length=2, delay_cost=1)
	S += c_pa10 >= 49
	c_pa10 += MAS[3]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	S += c_pb00_mem0 >= 49
	c_pb00_mem0 += MAS_MEM[4]

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	S += c_pb00_mem1 >= 49
	c_pb00_mem1 += MAS_MEM[5]

	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=7, delay_cost=1)
	S += c_pbc_t0_t1 >= 49
	c_pbc_t0_t1 += MM[0]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 50
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 50
	c_aa_t20_mem1 += MM_MEM[1]

	c_ab_t41 = S.Task('c_ab_t41', length=2, delay_cost=1)
	S += c_ab_t41 >= 50
	c_ab_t41 += MAS[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 50
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_bb_t50 = S.Task('c_bb_t50', length=2, delay_cost=1)
	S += c_bb_t50 >= 50
	c_bb_t50 += MAS[1]

	c_bc01 = S.Task('c_bc01', length=2, delay_cost=1)
	S += c_bc01 >= 50
	c_bc01 += MAS[2]

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	S += c_bc11_mem0 >= 50
	c_bc11_mem0 += MAS_MEM[2]

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	S += c_bc11_mem1 >= 50
	c_bc11_mem1 += MAS_MEM[3]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 50
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	S += c_paa_t1_t0_in >= 50
	c_paa_t1_t0_in += MM_in[0]

	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem0 >= 50
	c_paa_t1_t0_mem0 += MAS_MEM[6]

	c_pb00 = S.Task('c_pb00', length=2, delay_cost=1)
	S += c_pb00 >= 50
	c_pb00 += MAS[3]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	S += c_pc10_mem0 >= 50
	c_pc10_mem0 += MAS_MEM[0]

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	S += c_pc10_mem1 >= 50
	c_pc10_mem1 += MAS_MEM[1]

	c_aa_t20 = S.Task('c_aa_t20', length=2, delay_cost=1)
	S += c_aa_t20 >= 51
	c_aa_t20 += MAS[0]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	S += c_bb00_mem0 >= 51
	c_bb00_mem0 += MAS_MEM[4]

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	S += c_bb00_mem1 >= 51
	c_bb00_mem1 += MAS_MEM[3]

	c_bc11 = S.Task('c_bc11', length=2, delay_cost=1)
	S += c_bc11 >= 51
	c_bc11 += MAS[1]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 51
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 51
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 51
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 51
	c_cc_t20_mem1 += MM_MEM[1]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	S += c_cc_t50_mem0 >= 51
	c_cc_t50_mem0 += MAS_MEM[0]

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	S += c_cc_t50_mem1 >= 51
	c_cc_t50_mem1 += MAS_MEM[1]

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	S += c_pa11_mem0 >= 51
	c_pa11_mem0 += MAS_MEM[2]

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	S += c_pa11_mem1 >= 51
	c_pa11_mem1 += MAS_MEM[5]

	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=7, delay_cost=1)
	S += c_paa_t1_t0 >= 51
	c_paa_t1_t0 += MM[0]

	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	S += c_pbc_t0_t0_in >= 51
	c_pbc_t0_t0_in += MM_in[0]

	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem0 >= 51
	c_pbc_t0_t0_mem0 += MAS_MEM[6]

	c_pc10 = S.Task('c_pc10', length=2, delay_cost=1)
	S += c_pc10 >= 51
	c_pc10 += MAS[2]

	c_bb00 = S.Task('c_bb00', length=2, delay_cost=1)
	S += c_bb00 >= 52
	c_bb00 += MAS[3]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 52
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 52
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_0_mem0 >= 52
	c_bcxi_y1_0_mem0 += MAS_MEM[0]

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_0_mem1 >= 52
	c_bcxi_y1_0_mem1 += MAS_MEM[3]

	c_cc_t20 = S.Task('c_cc_t20', length=2, delay_cost=1)
	S += c_cc_t20 >= 52
	c_cc_t20 += MAS[0]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 52
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 52
	c_cc_t2_t5_mem1 += MM_MEM[1]

	c_cc_t50 = S.Task('c_cc_t50', length=2, delay_cost=1)
	S += c_cc_t50 >= 52
	c_cc_t50 += MAS[1]

	c_pa11 = S.Task('c_pa11', length=2, delay_cost=1)
	S += c_pa11 >= 52
	c_pa11 += MAS[2]

	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=7, delay_cost=1)
	S += c_pbc_t0_t0 >= 52
	c_pbc_t0_t0 += MM[0]

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem0 >= 52
	c_pbc_t0_t2_mem0 += MAS_MEM[6]

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem1 >= 52
	c_pbc_t0_t2_mem1 += MAS_MEM[7]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	S += c_pc11_mem0 >= 52
	c_pc11_mem0 += MAS_MEM[2]

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	S += c_pc11_mem1 >= 52
	c_pc11_mem1 += MAS_MEM[1]

	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	S += c_pcb_t1_t0_in >= 52
	c_pcb_t1_t0_in += MM_in[0]

	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem0 >= 52
	c_pcb_t1_t0_mem0 += MAS_MEM[4]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 53
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 53
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 53
	c_bb_t2_t5_mem1 += MM_MEM[1]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 53
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=2, delay_cost=1)
	S += c_bcxi_y1_0 >= 53
	c_bcxi_y1_0 += MAS[2]

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem0 >= 53
	c_bcxi_y1_1_mem0 += MAS_MEM[2]

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem1 >= 53
	c_bcxi_y1_1_mem1 += MAS_MEM[1]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	S += c_cc00_mem0 >= 53
	c_cc00_mem0 += MAS_MEM[0]

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	S += c_cc00_mem1 >= 53
	c_cc00_mem1 += MAS_MEM[3]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=2, delay_cost=1)
	S += c_cc_t2_t5 >= 53
	c_cc_t2_t5 += MAS[3]

	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	S += c_paa_t1_t1_in >= 53
	c_paa_t1_t1_in += MM_in[0]

	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t1_mem0 >= 53
	c_paa_t1_t1_mem0 += MAS_MEM[4]

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t2_mem0 >= 53
	c_paa_t1_t2_mem0 += MAS_MEM[6]

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t2_mem1 >= 53
	c_paa_t1_t2_mem1 += MAS_MEM[5]

	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=2, delay_cost=1)
	S += c_pbc_t0_t2 >= 53
	c_pbc_t0_t2 += MAS[0]

	c_pc11 = S.Task('c_pc11', length=2, delay_cost=1)
	S += c_pc11 >= 53
	c_pc11 += MAS[1]

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=7, delay_cost=1)
	S += c_pcb_t1_t0 >= 53
	c_pcb_t1_t0 += MM[0]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	S += c_aa00_mem0 >= 54
	c_aa00_mem0 += MAS_MEM[0]

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	S += c_aa00_mem1 >= 54
	c_aa00_mem1 += MAS_MEM[5]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t21_mem0 >= 54
	c_aa_t21_mem0 += MM_MEM[0]

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t21_mem1 >= 54
	c_aa_t21_mem1 += MAS_MEM[7]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 54
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 54
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=2, delay_cost=1)
	S += c_bb_t2_t5 >= 54
	c_bb_t2_t5 += MAS[3]

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=2, delay_cost=1)
	S += c_bcxi_y1_1 >= 54
	c_bcxi_y1_1 += MAS[1]

	c_cc00 = S.Task('c_cc00', length=2, delay_cost=1)
	S += c_cc00 >= 54
	c_cc00 += MAS[2]

	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=7, delay_cost=1)
	S += c_paa_t1_t1 >= 54
	c_paa_t1_t1 += MM[0]

	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=2, delay_cost=1)
	S += c_paa_t1_t2 >= 54
	c_paa_t1_t2 += MAS[0]

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	S += c_pc00_mem0 >= 54
	c_pc00_mem0 += MAS_MEM[6]

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	S += c_pc00_mem1 >= 54
	c_pc00_mem1 += MAS_MEM[1]

	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	S += c_pcb_t1_t1_in >= 54
	c_pcb_t1_t1_in += MM_in[0]

	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem0 >= 54
	c_pcb_t1_t1_mem0 += MAS_MEM[2]

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem0 >= 54
	c_pcb_t1_t2_mem0 += MAS_MEM[4]

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem1 >= 54
	c_pcb_t1_t2_mem1 += MAS_MEM[3]

	c_aa00 = S.Task('c_aa00', length=2, delay_cost=1)
	S += c_aa00 >= 55
	c_aa00 += MAS[2]

	c_aa_t21 = S.Task('c_aa_t21', length=2, delay_cost=1)
	S += c_aa_t21 >= 55
	c_aa_t21 += MAS[3]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 55
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 55
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

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
	c_cc_t51_mem1 += MAS_MEM[3]

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	S += c_pb10_mem0 >= 55
	c_pb10_mem0 += MAS_MEM[4]

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	S += c_pb10_mem1 >= 55
	c_pb10_mem1 += MAS_MEM[5]

	c_pc00 = S.Task('c_pc00', length=2, delay_cost=1)
	S += c_pc00 >= 55
	c_pc00 += MAS[0]

	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=7, delay_cost=1)
	S += c_pcb_t1_t1 >= 55
	c_pcb_t1_t1 += MM[0]

	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=2, delay_cost=1)
	S += c_pcb_t1_t2 >= 55
	c_pcb_t1_t2 += MAS[1]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	S += c_aa01_mem0 >= 56
	c_aa01_mem0 += MAS_MEM[6]

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	S += c_aa01_mem1 >= 56
	c_aa01_mem1 += MAS_MEM[3]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 56
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	S += c_bb_t21_mem0 >= 56
	c_bb_t21_mem0 += MM_MEM[0]

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	S += c_bb_t21_mem1 >= 56
	c_bb_t21_mem1 += MAS_MEM[7]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	S += c_bb_t51_mem0 >= 56
	c_bb_t51_mem0 += MAS_MEM[0]

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	S += c_bb_t51_mem1 >= 56
	c_bb_t51_mem1 += MAS_MEM[1]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 56
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t21 = S.Task('c_cc_t21', length=2, delay_cost=1)
	S += c_cc_t21 >= 56
	c_cc_t21 += MAS[3]

	c_cc_t51 = S.Task('c_cc_t51', length=2, delay_cost=1)
	S += c_cc_t51 >= 56
	c_cc_t51 += MAS[0]

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	S += c_pa00_mem0 >= 56
	c_pa00_mem0 += MAS_MEM[4]

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	S += c_pa00_mem1 >= 56
	c_pa00_mem1 += MAS_MEM[5]

	c_pb10 = S.Task('c_pb10', length=2, delay_cost=1)
	S += c_pb10 >= 56
	c_pb10 += MAS[2]

	c_aa01 = S.Task('c_aa01', length=2, delay_cost=1)
	S += c_aa01 >= 57
	c_aa01 += MAS[3]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	S += c_ab11_mem0 >= 57
	c_ab11_mem0 += MAS_MEM[0]

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	S += c_ab11_mem1 >= 57
	c_ab11_mem1 += MAS_MEM[7]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 57
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_bb_t21 = S.Task('c_bb_t21', length=2, delay_cost=1)
	S += c_bb_t21 >= 57
	c_bb_t21 += MAS[1]

	c_bb_t51 = S.Task('c_bb_t51', length=2, delay_cost=1)
	S += c_bb_t51 >= 57
	c_bb_t51 += MAS[2]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 57
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	S += c_cc01_mem0 >= 57
	c_cc01_mem0 += MAS_MEM[6]

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	S += c_cc01_mem1 >= 57
	c_cc01_mem1 += MAS_MEM[1]

	c_pa00 = S.Task('c_pa00', length=2, delay_cost=1)
	S += c_pa00 >= 57
	c_pa00 += MAS[1]

	c_pcb_t1_t4_in = S.Task('c_pcb_t1_t4_in', length=1, delay_cost=1)
	S += c_pcb_t1_t4_in >= 57
	c_pcb_t1_t4_in += MM_in[0]

	c_pcb_t1_t4_mem0 = S.Task('c_pcb_t1_t4_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t4_mem0 >= 57
	c_pcb_t1_t4_mem0 += MAS_MEM[2]

	c_pcb_t1_t4_mem1 = S.Task('c_pcb_t1_t4_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t4_mem1 >= 57
	c_pcb_t1_t4_mem1 += MAS_MEM[5]

	c_ab11 = S.Task('c_ab11', length=2, delay_cost=1)
	S += c_ab11 >= 58
	c_ab11 += MAS[2]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 58
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 58
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	S += c_ac01_mem0 >= 58
	c_ac01_mem0 += MAS_MEM[0]

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	S += c_ac01_mem1 >= 58
	c_ac01_mem1 += MAS_MEM[7]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	S += c_bb01_mem0 >= 58
	c_bb01_mem0 += MAS_MEM[2]

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	S += c_bb01_mem1 >= 58
	c_bb01_mem1 += MAS_MEM[5]

	c_cc01 = S.Task('c_cc01', length=2, delay_cost=1)
	S += c_cc01 >= 58
	c_cc01 += MAS[3]

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	S += c_pa01_mem0 >= 58
	c_pa01_mem0 += MAS_MEM[6]

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	S += c_pa01_mem1 >= 58
	c_pa01_mem1 += MAS_MEM[3]

	c_pbc_t00_mem0 = S.Task('c_pbc_t00_mem0', length=1, delay_cost=1)
	S += c_pbc_t00_mem0 >= 58
	c_pbc_t00_mem0 += MM_MEM[0]

	c_pbc_t00_mem1 = S.Task('c_pbc_t00_mem1', length=1, delay_cost=1)
	S += c_pbc_t00_mem1 >= 58
	c_pbc_t00_mem1 += MM_MEM[1]

	c_pbc_t1_t0_in = S.Task('c_pbc_t1_t0_in', length=1, delay_cost=1)
	S += c_pbc_t1_t0_in >= 58
	c_pbc_t1_t0_in += MM_in[0]

	c_pbc_t1_t0_mem0 = S.Task('c_pbc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t0_mem0 >= 58
	c_pbc_t1_t0_mem0 += MAS_MEM[4]

	c_pcb_t1_t4 = S.Task('c_pcb_t1_t4', length=7, delay_cost=1)
	S += c_pcb_t1_t4 >= 58
	c_pcb_t1_t4 += MM[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 59
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ac01 = S.Task('c_ac01', length=2, delay_cost=1)
	S += c_ac01 >= 59
	c_ac01 += MAS[0]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 59
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bb01 = S.Task('c_bb01', length=2, delay_cost=1)
	S += c_bb01 >= 59
	c_bb01 += MAS[1]

	c_pa01 = S.Task('c_pa01', length=2, delay_cost=1)
	S += c_pa01 >= 59
	c_pa01 += MAS[2]

	c_paa_t20_mem0 = S.Task('c_paa_t20_mem0', length=1, delay_cost=1)
	S += c_paa_t20_mem0 >= 59
	c_paa_t20_mem0 += MAS_MEM[2]

	c_paa_t20_mem1 = S.Task('c_paa_t20_mem1', length=1, delay_cost=1)
	S += c_paa_t20_mem1 >= 59
	c_paa_t20_mem1 += MAS_MEM[7]

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	S += c_pb11_mem0 >= 59
	c_pb11_mem0 += MAS_MEM[6]

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	S += c_pb11_mem1 >= 59
	c_pb11_mem1 += MAS_MEM[5]

	c_pbc_t00 = S.Task('c_pbc_t00', length=2, delay_cost=1)
	S += c_pbc_t00 >= 59
	c_pbc_t00 += MAS[3]

	c_pbc_t0_t4_in = S.Task('c_pbc_t0_t4_in', length=1, delay_cost=1)
	S += c_pbc_t0_t4_in >= 59
	c_pbc_t0_t4_in += MM_in[0]

	c_pbc_t0_t4_mem0 = S.Task('c_pbc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t4_mem0 >= 59
	c_pbc_t0_t4_mem0 += MAS_MEM[0]

	c_pbc_t0_t4_mem1 = S.Task('c_pbc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t4_mem1 >= 59
	c_pbc_t0_t4_mem1 += MAS_MEM[1]

	c_pbc_t0_t5_mem0 = S.Task('c_pbc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t5_mem0 >= 59
	c_pbc_t0_t5_mem0 += MM_MEM[0]

	c_pbc_t0_t5_mem1 = S.Task('c_pbc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t5_mem1 >= 59
	c_pbc_t0_t5_mem1 += MM_MEM[1]

	c_pbc_t1_t0 = S.Task('c_pbc_t1_t0', length=7, delay_cost=1)
	S += c_pbc_t1_t0 >= 59
	c_pbc_t1_t0 += MM[0]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 60
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 60
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t4_in = S.Task('c_paa_t1_t4_in', length=1, delay_cost=1)
	S += c_paa_t1_t4_in >= 60
	c_paa_t1_t4_in += MM_in[0]

	c_paa_t1_t4_mem0 = S.Task('c_paa_t1_t4_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t4_mem0 >= 60
	c_paa_t1_t4_mem0 += MAS_MEM[0]

	c_paa_t1_t4_mem1 = S.Task('c_paa_t1_t4_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t4_mem1 >= 60
	c_paa_t1_t4_mem1 += MAS_MEM[5]

	c_paa_t1_t5_mem0 = S.Task('c_paa_t1_t5_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t5_mem0 >= 60
	c_paa_t1_t5_mem0 += MM_MEM[0]

	c_paa_t1_t5_mem1 = S.Task('c_paa_t1_t5_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t5_mem1 >= 60
	c_paa_t1_t5_mem1 += MM_MEM[1]

	c_paa_t20 = S.Task('c_paa_t20', length=2, delay_cost=1)
	S += c_paa_t20 >= 60
	c_paa_t20 += MAS[2]

	c_pb11 = S.Task('c_pb11', length=2, delay_cost=1)
	S += c_pb11 >= 60
	c_pb11 += MAS[1]

	c_pbc_t0_t4 = S.Task('c_pbc_t0_t4', length=7, delay_cost=1)
	S += c_pbc_t0_t4 >= 60
	c_pbc_t0_t4 += MM[0]

	c_pbc_t0_t5 = S.Task('c_pbc_t0_t5', length=2, delay_cost=1)
	S += c_pbc_t0_t5 >= 60
	c_pbc_t0_t5 += MAS[0]

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	S += c_pc01_mem0 >= 60
	c_pc01_mem0 += MAS_MEM[2]

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	S += c_pc01_mem1 >= 60
	c_pc01_mem1 += MAS_MEM[1]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 61
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 61
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t4 = S.Task('c_paa_t1_t4', length=7, delay_cost=1)
	S += c_paa_t1_t4 >= 61
	c_paa_t1_t4 += MM[0]

	c_paa_t1_t5 = S.Task('c_paa_t1_t5', length=2, delay_cost=1)
	S += c_paa_t1_t5 >= 61
	c_paa_t1_t5 += MAS[2]

	c_pbc_t1_t1_in = S.Task('c_pbc_t1_t1_in', length=1, delay_cost=1)
	S += c_pbc_t1_t1_in >= 61
	c_pbc_t1_t1_in += MM_in[0]

	c_pbc_t1_t1_mem0 = S.Task('c_pbc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t1_mem0 >= 61
	c_pbc_t1_t1_mem0 += MAS_MEM[2]

	c_pbc_t1_t2_mem0 = S.Task('c_pbc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t2_mem0 >= 61
	c_pbc_t1_t2_mem0 += MAS_MEM[4]

	c_pbc_t1_t2_mem1 = S.Task('c_pbc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t2_mem1 >= 61
	c_pbc_t1_t2_mem1 += MAS_MEM[3]

	c_pc01 = S.Task('c_pc01', length=2, delay_cost=1)
	S += c_pc01 >= 61
	c_pc01 += MAS[0]

	c_pcb_t10_mem0 = S.Task('c_pcb_t10_mem0', length=1, delay_cost=1)
	S += c_pcb_t10_mem0 >= 61
	c_pcb_t10_mem0 += MM_MEM[0]

	c_pcb_t10_mem1 = S.Task('c_pcb_t10_mem1', length=1, delay_cost=1)
	S += c_pcb_t10_mem1 >= 61
	c_pcb_t10_mem1 += MM_MEM[1]

	c_pcb_t20_mem0 = S.Task('c_pcb_t20_mem0', length=1, delay_cost=1)
	S += c_pcb_t20_mem0 >= 61
	c_pcb_t20_mem0 += MAS_MEM[0]

	c_pcb_t20_mem1 = S.Task('c_pcb_t20_mem1', length=1, delay_cost=1)
	S += c_pcb_t20_mem1 >= 61
	c_pcb_t20_mem1 += MAS_MEM[5]

	c_paa_t0_t0_in = S.Task('c_paa_t0_t0_in', length=1, delay_cost=1)
	S += c_paa_t0_t0_in >= 62
	c_paa_t0_t0_in += MM_in[0]

	c_paa_t0_t0_mem0 = S.Task('c_paa_t0_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t0_mem0 >= 62
	c_paa_t0_t0_mem0 += MAS_MEM[2]

	c_paa_t21_mem0 = S.Task('c_paa_t21_mem0', length=1, delay_cost=1)
	S += c_paa_t21_mem0 >= 62
	c_paa_t21_mem0 += MAS_MEM[4]

	c_paa_t21_mem1 = S.Task('c_paa_t21_mem1', length=1, delay_cost=1)
	S += c_paa_t21_mem1 >= 62
	c_paa_t21_mem1 += MAS_MEM[5]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 62
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 62
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t1 = S.Task('c_pbc_t1_t1', length=7, delay_cost=1)
	S += c_pbc_t1_t1 >= 62
	c_pbc_t1_t1 += MM[0]

	c_pbc_t1_t2 = S.Task('c_pbc_t1_t2', length=2, delay_cost=1)
	S += c_pbc_t1_t2 >= 62
	c_pbc_t1_t2 += MAS[1]

	c_pbc_t21_mem0 = S.Task('c_pbc_t21_mem0', length=1, delay_cost=1)
	S += c_pbc_t21_mem0 >= 62
	c_pbc_t21_mem0 += MAS_MEM[6]

	c_pbc_t21_mem1 = S.Task('c_pbc_t21_mem1', length=1, delay_cost=1)
	S += c_pbc_t21_mem1 >= 62
	c_pbc_t21_mem1 += MAS_MEM[3]

	c_pcb_t0_t2_mem0 = S.Task('c_pcb_t0_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t2_mem0 >= 62
	c_pcb_t0_t2_mem0 += MAS_MEM[0]

	c_pcb_t0_t2_mem1 = S.Task('c_pcb_t0_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t2_mem1 >= 62
	c_pcb_t0_t2_mem1 += MAS_MEM[1]

	c_pcb_t10 = S.Task('c_pcb_t10', length=2, delay_cost=1)
	S += c_pcb_t10 >= 62
	c_pcb_t10 += MAS[2]

	c_pcb_t1_t5_mem0 = S.Task('c_pcb_t1_t5_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t5_mem0 >= 62
	c_pcb_t1_t5_mem0 += MM_MEM[0]

	c_pcb_t1_t5_mem1 = S.Task('c_pcb_t1_t5_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t5_mem1 >= 62
	c_pcb_t1_t5_mem1 += MM_MEM[1]

	c_pcb_t20 = S.Task('c_pcb_t20', length=2, delay_cost=1)
	S += c_pcb_t20 >= 62
	c_pcb_t20 += MAS[3]

	c_paa_t0_t0 = S.Task('c_paa_t0_t0', length=7, delay_cost=1)
	S += c_paa_t0_t0 >= 63
	c_paa_t0_t0 += MM[0]

	c_paa_t0_t1_in = S.Task('c_paa_t0_t1_in', length=1, delay_cost=1)
	S += c_paa_t0_t1_in >= 63
	c_paa_t0_t1_in += MM_in[0]

	c_paa_t0_t1_mem0 = S.Task('c_paa_t0_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t1_mem0 >= 63
	c_paa_t0_t1_mem0 += MAS_MEM[4]

	c_paa_t10_mem0 = S.Task('c_paa_t10_mem0', length=1, delay_cost=1)
	S += c_paa_t10_mem0 >= 63
	c_paa_t10_mem0 += MM_MEM[0]

	c_paa_t10_mem1 = S.Task('c_paa_t10_mem1', length=1, delay_cost=1)
	S += c_paa_t10_mem1 >= 63
	c_paa_t10_mem1 += MM_MEM[1]

	c_paa_t21 = S.Task('c_paa_t21', length=2, delay_cost=1)
	S += c_paa_t21 >= 63
	c_paa_t21 += MAS[1]

	c_pbc_t20_mem0 = S.Task('c_pbc_t20_mem0', length=1, delay_cost=1)
	S += c_pbc_t20_mem0 >= 63
	c_pbc_t20_mem0 += MAS_MEM[6]

	c_pbc_t20_mem1 = S.Task('c_pbc_t20_mem1', length=1, delay_cost=1)
	S += c_pbc_t20_mem1 >= 63
	c_pbc_t20_mem1 += MAS_MEM[5]

	c_pbc_t21 = S.Task('c_pbc_t21', length=2, delay_cost=1)
	S += c_pbc_t21 >= 63
	c_pbc_t21 += MAS[0]

	c_pcb_t0_t2 = S.Task('c_pcb_t0_t2', length=2, delay_cost=1)
	S += c_pcb_t0_t2 >= 63
	c_pcb_t0_t2 += MAS[3]

	c_pcb_t1_t5 = S.Task('c_pcb_t1_t5', length=2, delay_cost=1)
	S += c_pcb_t1_t5 >= 63
	c_pcb_t1_t5 += MAS[0]

	c_pcb_t21_mem0 = S.Task('c_pcb_t21_mem0', length=1, delay_cost=1)
	S += c_pcb_t21_mem0 >= 63
	c_pcb_t21_mem0 += MAS_MEM[0]

	c_pcb_t21_mem1 = S.Task('c_pcb_t21_mem1', length=1, delay_cost=1)
	S += c_pcb_t21_mem1 >= 63
	c_pcb_t21_mem1 += MAS_MEM[3]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 63
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 63
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t1 = S.Task('c_paa_t0_t1', length=7, delay_cost=1)
	S += c_paa_t0_t1 >= 64
	c_paa_t0_t1 += MM[0]

	c_paa_t0_t2_mem0 = S.Task('c_paa_t0_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t2_mem0 >= 64
	c_paa_t0_t2_mem0 += MAS_MEM[2]

	c_paa_t0_t2_mem1 = S.Task('c_paa_t0_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t2_mem1 >= 64
	c_paa_t0_t2_mem1 += MAS_MEM[5]

	c_paa_t10 = S.Task('c_paa_t10', length=2, delay_cost=1)
	S += c_paa_t10 >= 64
	c_paa_t10 += MAS[2]

	c_paa_t4_t2_mem0 = S.Task('c_paa_t4_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t2_mem0 >= 64
	c_paa_t4_t2_mem0 += MAS_MEM[4]

	c_paa_t4_t2_mem1 = S.Task('c_paa_t4_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t2_mem1 >= 64
	c_paa_t4_t2_mem1 += MAS_MEM[3]

	c_pbc_t20 = S.Task('c_pbc_t20', length=2, delay_cost=1)
	S += c_pbc_t20 >= 64
	c_pbc_t20 += MAS[1]

	c_pcb_t0_t1_in = S.Task('c_pcb_t0_t1_in', length=1, delay_cost=1)
	S += c_pcb_t0_t1_in >= 64
	c_pcb_t0_t1_in += MM_in[0]

	c_pcb_t0_t1_mem0 = S.Task('c_pcb_t0_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t1_mem0 >= 64
	c_pcb_t0_t1_mem0 += MAS_MEM[0]

	c_pcb_t11_mem0 = S.Task('c_pcb_t11_mem0', length=1, delay_cost=1)
	S += c_pcb_t11_mem0 >= 64
	c_pcb_t11_mem0 += MM_MEM[0]

	c_pcb_t11_mem1 = S.Task('c_pcb_t11_mem1', length=1, delay_cost=1)
	S += c_pcb_t11_mem1 >= 64
	c_pcb_t11_mem1 += MAS_MEM[1]

	c_pcb_t21 = S.Task('c_pcb_t21', length=2, delay_cost=1)
	S += c_pcb_t21 >= 64
	c_pcb_t21 += MAS[3]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 64
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 64
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t2 = S.Task('c_paa_t0_t2', length=2, delay_cost=1)
	S += c_paa_t0_t2 >= 65
	c_paa_t0_t2 += MAS[0]

	c_paa_t4_t2 = S.Task('c_paa_t4_t2', length=2, delay_cost=1)
	S += c_paa_t4_t2 >= 65
	c_paa_t4_t2 += MAS[1]

	c_pbc_t4_t2_mem0 = S.Task('c_pbc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t2_mem0 >= 65
	c_pbc_t4_t2_mem0 += MAS_MEM[2]

	c_pbc_t4_t2_mem1 = S.Task('c_pbc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t2_mem1 >= 65
	c_pbc_t4_t2_mem1 += MAS_MEM[1]

	c_pcb_t0_t0_in = S.Task('c_pcb_t0_t0_in', length=1, delay_cost=1)
	S += c_pcb_t0_t0_in >= 65
	c_pcb_t0_t0_in += MM_in[0]

	c_pcb_t0_t0_mem0 = S.Task('c_pcb_t0_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t0_mem0 >= 65
	c_pcb_t0_t0_mem0 += MAS_MEM[0]

	c_pcb_t0_t1 = S.Task('c_pcb_t0_t1', length=7, delay_cost=1)
	S += c_pcb_t0_t1 >= 65
	c_pcb_t0_t1 += MM[0]

	c_pcb_t11 = S.Task('c_pcb_t11', length=2, delay_cost=1)
	S += c_pcb_t11 >= 65
	c_pcb_t11 += MAS[0]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 65
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 65
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t4_t2_mem0 = S.Task('c_pcb_t4_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t2_mem0 >= 65
	c_pcb_t4_t2_mem0 += MAS_MEM[6]

	c_pcb_t4_t2_mem1 = S.Task('c_pcb_t4_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t2_mem1 >= 65
	c_pcb_t4_t2_mem1 += MAS_MEM[7]

	c_pbc_t01_mem0 = S.Task('c_pbc_t01_mem0', length=1, delay_cost=1)
	S += c_pbc_t01_mem0 >= 66
	c_pbc_t01_mem0 += MM_MEM[0]

	c_pbc_t01_mem1 = S.Task('c_pbc_t01_mem1', length=1, delay_cost=1)
	S += c_pbc_t01_mem1 >= 66
	c_pbc_t01_mem1 += MAS_MEM[1]

	c_pbc_t4_t2 = S.Task('c_pbc_t4_t2', length=2, delay_cost=1)
	S += c_pbc_t4_t2 >= 66
	c_pbc_t4_t2 += MAS[3]

	c_pcb_t0_t0 = S.Task('c_pcb_t0_t0', length=7, delay_cost=1)
	S += c_pcb_t0_t0 >= 66
	c_pcb_t0_t0 += MM[0]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 66
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 66
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t4_in = S.Task('c_pcb_t0_t4_in', length=1, delay_cost=1)
	S += c_pcb_t0_t4_in >= 66
	c_pcb_t0_t4_in += MM_in[0]

	c_pcb_t0_t4_mem0 = S.Task('c_pcb_t0_t4_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t4_mem0 >= 66
	c_pcb_t0_t4_mem0 += MAS_MEM[6]

	c_pcb_t0_t4_mem1 = S.Task('c_pcb_t0_t4_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t4_mem1 >= 66
	c_pcb_t0_t4_mem1 += MAS_MEM[5]

	c_pcb_t4_t2 = S.Task('c_pcb_t4_t2', length=2, delay_cost=1)
	S += c_pcb_t4_t2 >= 66
	c_pcb_t4_t2 += MAS[3]

	c_paa_t11_mem0 = S.Task('c_paa_t11_mem0', length=1, delay_cost=1)
	S += c_paa_t11_mem0 >= 67
	c_paa_t11_mem0 += MM_MEM[0]

	c_paa_t11_mem1 = S.Task('c_paa_t11_mem1', length=1, delay_cost=1)
	S += c_paa_t11_mem1 >= 67
	c_paa_t11_mem1 += MAS_MEM[5]

	c_pbc_t01 = S.Task('c_pbc_t01', length=2, delay_cost=1)
	S += c_pbc_t01 >= 67
	c_pbc_t01 += MAS[2]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 67
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 67
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_pcb_s00_mem0 = S.Task('c_pcb_s00_mem0', length=1, delay_cost=1)
	S += c_pcb_s00_mem0 >= 67
	c_pcb_s00_mem0 += MAS_MEM[4]

	c_pcb_s00_mem1 = S.Task('c_pcb_s00_mem1', length=1, delay_cost=1)
	S += c_pcb_s00_mem1 >= 67
	c_pcb_s00_mem1 += MAS_MEM[1]

	c_pcb_t0_t4 = S.Task('c_pcb_t0_t4', length=7, delay_cost=1)
	S += c_pcb_t0_t4 >= 67
	c_pcb_t0_t4 += MM[0]

	c_pcb_t4_t0_in = S.Task('c_pcb_t4_t0_in', length=1, delay_cost=1)
	S += c_pcb_t4_t0_in >= 67
	c_pcb_t4_t0_in += MM_in[0]

	c_pcb_t4_t0_mem0 = S.Task('c_pcb_t4_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t0_mem0 >= 67
	c_pcb_t4_t0_mem0 += MAS_MEM[6]

	c_pcb_t4_t0_mem1 = S.Task('c_pcb_t4_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t0_mem1 >= 67
	c_pcb_t4_t0_mem1 += MAS_MEM[3]

	c_paa_t11 = S.Task('c_paa_t11', length=2, delay_cost=1)
	S += c_paa_t11 >= 68
	c_paa_t11 += MAS[0]

	c_pbc_t10_mem0 = S.Task('c_pbc_t10_mem0', length=1, delay_cost=1)
	S += c_pbc_t10_mem0 >= 68
	c_pbc_t10_mem0 += MM_MEM[0]

	c_pbc_t10_mem1 = S.Task('c_pbc_t10_mem1', length=1, delay_cost=1)
	S += c_pbc_t10_mem1 >= 68
	c_pbc_t10_mem1 += MM_MEM[1]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 68
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 68
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t4_t1_in = S.Task('c_pbc_t4_t1_in', length=1, delay_cost=1)
	S += c_pbc_t4_t1_in >= 68
	c_pbc_t4_t1_in += MM_in[0]

	c_pbc_t4_t1_mem0 = S.Task('c_pbc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t1_mem0 >= 68
	c_pbc_t4_t1_mem0 += MAS_MEM[0]

	c_pbc_t4_t1_mem1 = S.Task('c_pbc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t1_mem1 >= 68
	c_pbc_t4_t1_mem1 += MAS_MEM[7]

	c_pcb_s00 = S.Task('c_pcb_s00', length=2, delay_cost=1)
	S += c_pcb_s00 >= 68
	c_pcb_s00 += MAS[1]

	c_pcb_t4_t0 = S.Task('c_pcb_t4_t0', length=7, delay_cost=1)
	S += c_pcb_t4_t0 >= 68
	c_pcb_t4_t0 += MM[0]

	c_pbc_t10 = S.Task('c_pbc_t10', length=2, delay_cost=1)
	S += c_pbc_t10 >= 69
	c_pbc_t10 += MAS[3]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 69
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 69
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t5_mem0 = S.Task('c_pbc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t5_mem0 >= 69
	c_pbc_t1_t5_mem0 += MM_MEM[0]

	c_pbc_t1_t5_mem1 = S.Task('c_pbc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t5_mem1 >= 69
	c_pbc_t1_t5_mem1 += MM_MEM[1]

	c_pbc_t4_t1 = S.Task('c_pbc_t4_t1', length=7, delay_cost=1)
	S += c_pbc_t4_t1 >= 69
	c_pbc_t4_t1 += MM[0]

	c_pcb_s01_mem0 = S.Task('c_pcb_s01_mem0', length=1, delay_cost=1)
	S += c_pcb_s01_mem0 >= 69
	c_pcb_s01_mem0 += MAS_MEM[0]

	c_pcb_s01_mem1 = S.Task('c_pcb_s01_mem1', length=1, delay_cost=1)
	S += c_pcb_s01_mem1 >= 69
	c_pcb_s01_mem1 += MAS_MEM[5]

	c_pcb_t4_t1_in = S.Task('c_pcb_t4_t1_in', length=1, delay_cost=1)
	S += c_pcb_t4_t1_in >= 69
	c_pcb_t4_t1_in += MM_in[0]

	c_pcb_t4_t1_mem0 = S.Task('c_pcb_t4_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t1_mem0 >= 69
	c_pcb_t4_t1_mem0 += MAS_MEM[6]

	c_pcb_t4_t1_mem1 = S.Task('c_pcb_t4_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t1_mem1 >= 69
	c_pcb_t4_t1_mem1 += MAS_MEM[1]

	c_paa_s00_mem0 = S.Task('c_paa_s00_mem0', length=1, delay_cost=1)
	S += c_paa_s00_mem0 >= 70
	c_paa_s00_mem0 += MAS_MEM[4]

	c_paa_s00_mem1 = S.Task('c_paa_s00_mem1', length=1, delay_cost=1)
	S += c_paa_s00_mem1 >= 70
	c_paa_s00_mem1 += MAS_MEM[1]

	c_paa_t00_mem0 = S.Task('c_paa_t00_mem0', length=1, delay_cost=1)
	S += c_paa_t00_mem0 >= 70
	c_paa_t00_mem0 += MM_MEM[0]

	c_paa_t00_mem1 = S.Task('c_paa_t00_mem1', length=1, delay_cost=1)
	S += c_paa_t00_mem1 >= 70
	c_paa_t00_mem1 += MM_MEM[1]

	c_paa_t0_t4_in = S.Task('c_paa_t0_t4_in', length=1, delay_cost=1)
	S += c_paa_t0_t4_in >= 70
	c_paa_t0_t4_in += MM_in[0]

	c_paa_t0_t4_mem0 = S.Task('c_paa_t0_t4_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t4_mem0 >= 70
	c_paa_t0_t4_mem0 += MAS_MEM[0]

	c_paa_t0_t4_mem1 = S.Task('c_paa_t0_t4_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t4_mem1 >= 70
	c_paa_t0_t4_mem1 += MAS_MEM[3]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 70
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 70
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t5 = S.Task('c_pbc_t1_t5', length=2, delay_cost=1)
	S += c_pbc_t1_t5 >= 70
	c_pbc_t1_t5 += MAS[0]

	c_pbc_t50_mem0 = S.Task('c_pbc_t50_mem0', length=1, delay_cost=1)
	S += c_pbc_t50_mem0 >= 70
	c_pbc_t50_mem0 += MAS_MEM[6]

	c_pbc_t50_mem1 = S.Task('c_pbc_t50_mem1', length=1, delay_cost=1)
	S += c_pbc_t50_mem1 >= 70
	c_pbc_t50_mem1 += MAS_MEM[7]

	c_pcb_s01 = S.Task('c_pcb_s01', length=2, delay_cost=1)
	S += c_pcb_s01 >= 70
	c_pcb_s01 += MAS[1]

	c_pcb_t4_t1 = S.Task('c_pcb_t4_t1', length=7, delay_cost=1)
	S += c_pcb_t4_t1 >= 70
	c_pcb_t4_t1 += MM[0]

	c_paa_s00 = S.Task('c_paa_s00', length=2, delay_cost=1)
	S += c_paa_s00 >= 71
	c_paa_s00 += MAS[2]

	c_paa_s01_mem0 = S.Task('c_paa_s01_mem0', length=1, delay_cost=1)
	S += c_paa_s01_mem0 >= 71
	c_paa_s01_mem0 += MAS_MEM[0]

	c_paa_s01_mem1 = S.Task('c_paa_s01_mem1', length=1, delay_cost=1)
	S += c_paa_s01_mem1 >= 71
	c_paa_s01_mem1 += MAS_MEM[5]

	c_paa_t00 = S.Task('c_paa_t00', length=2, delay_cost=1)
	S += c_paa_t00 >= 71
	c_paa_t00 += MAS[0]

	c_paa_t0_t4 = S.Task('c_paa_t0_t4', length=7, delay_cost=1)
	S += c_paa_t0_t4 >= 71
	c_paa_t0_t4 += MM[0]

	c_paa_t0_t5_mem0 = S.Task('c_paa_t0_t5_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t5_mem0 >= 71
	c_paa_t0_t5_mem0 += MM_MEM[0]

	c_paa_t0_t5_mem1 = S.Task('c_paa_t0_t5_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t5_mem1 >= 71
	c_paa_t0_t5_mem1 += MM_MEM[1]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 71
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 71
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t4_t0_in = S.Task('c_pbc_t4_t0_in', length=1, delay_cost=1)
	S += c_pbc_t4_t0_in >= 71
	c_pbc_t4_t0_in += MM_in[0]

	c_pbc_t4_t0_mem0 = S.Task('c_pbc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t0_mem0 >= 71
	c_pbc_t4_t0_mem0 += MAS_MEM[2]

	c_pbc_t4_t0_mem1 = S.Task('c_pbc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t0_mem1 >= 71
	c_pbc_t4_t0_mem1 += MAS_MEM[7]

	c_pbc_t50 = S.Task('c_pbc_t50', length=2, delay_cost=1)
	S += c_pbc_t50 >= 71
	c_pbc_t50 += MAS[2]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 72
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_paa_s01 = S.Task('c_paa_s01', length=2, delay_cost=1)
	S += c_paa_s01 >= 72
	c_paa_s01 += MAS[1]

	c_paa_t0_t5 = S.Task('c_paa_t0_t5', length=2, delay_cost=1)
	S += c_paa_t0_t5 >= 72
	c_paa_t0_t5 += MAS[3]

	c_paa_t4_t1_in = S.Task('c_paa_t4_t1_in', length=1, delay_cost=1)
	S += c_paa_t4_t1_in >= 72
	c_paa_t4_t1_in += MM_in[0]

	c_paa_t4_t1_mem0 = S.Task('c_paa_t4_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t1_mem0 >= 72
	c_paa_t4_t1_mem0 += MAS_MEM[2]

	c_paa_t4_t1_mem1 = S.Task('c_paa_t4_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t1_mem1 >= 72
	c_paa_t4_t1_mem1 += MAS_MEM[7]

	c_paa_t50_mem0 = S.Task('c_paa_t50_mem0', length=1, delay_cost=1)
	S += c_paa_t50_mem0 >= 72
	c_paa_t50_mem0 += MAS_MEM[0]

	c_paa_t50_mem1 = S.Task('c_paa_t50_mem1', length=1, delay_cost=1)
	S += c_paa_t50_mem1 >= 72
	c_paa_t50_mem1 += MAS_MEM[5]

	c_pbc_t4_t0 = S.Task('c_pbc_t4_t0', length=7, delay_cost=1)
	S += c_pbc_t4_t0 >= 72
	c_pbc_t4_t0 += MM[0]

	c_pcb_t00_mem0 = S.Task('c_pcb_t00_mem0', length=1, delay_cost=1)
	S += c_pcb_t00_mem0 >= 72
	c_pcb_t00_mem0 += MM_MEM[0]

	c_pcb_t00_mem1 = S.Task('c_pcb_t00_mem1', length=1, delay_cost=1)
	S += c_pcb_t00_mem1 >= 72
	c_pcb_t00_mem1 += MM_MEM[1]

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem1 >= 72
	c_pcb_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 73
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_paa00_mem0 = S.Task('c_paa00_mem0', length=1, delay_cost=1)
	S += c_paa00_mem0 >= 73
	c_paa00_mem0 += MAS_MEM[0]

	c_paa00_mem1 = S.Task('c_paa00_mem1', length=1, delay_cost=1)
	S += c_paa00_mem1 >= 73
	c_paa00_mem1 += MAS_MEM[5]

	c_paa_t4_t1 = S.Task('c_paa_t4_t1', length=7, delay_cost=1)
	S += c_paa_t4_t1 >= 73
	c_paa_t4_t1 += MM[0]

	c_paa_t50 = S.Task('c_paa_t50', length=2, delay_cost=1)
	S += c_paa_t50 >= 73
	c_paa_t50 += MAS[1]

	c_pbc_t1_t4_in = S.Task('c_pbc_t1_t4_in', length=1, delay_cost=1)
	S += c_pbc_t1_t4_in >= 73
	c_pbc_t1_t4_in += MM_in[0]

	c_pbc_t1_t4_mem0 = S.Task('c_pbc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t4_mem0 >= 73
	c_pbc_t1_t4_mem0 += MAS_MEM[2]

	c_pbc_t1_t4_mem1 = S.Task('c_pbc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t4_mem1 >= 73
	c_pbc_t1_t4_mem1 += MAS_MEM[1]

	c_pcb_t00 = S.Task('c_pcb_t00', length=2, delay_cost=1)
	S += c_pcb_t00 >= 73
	c_pcb_t00 += MAS[0]

	c_pcb_t0_t0_mem1 = S.Task('c_pcb_t0_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t0_mem1 >= 73
	c_pcb_t0_t0_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t5_mem0 = S.Task('c_pcb_t0_t5_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t5_mem0 >= 73
	c_pcb_t0_t5_mem0 += MM_MEM[0]

	c_pcb_t0_t5_mem1 = S.Task('c_pcb_t0_t5_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t5_mem1 >= 73
	c_pcb_t0_t5_mem1 += MM_MEM[1]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 74
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_paa00 = S.Task('c_paa00', length=2, delay_cost=1)
	S += c_paa00 >= 74
	c_paa00 += MAS[1]

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem1 >= 74
	c_paa_t1_t0_mem1 += MAIN_MEM_r[1]

	c_paa_t4_t0_in = S.Task('c_paa_t4_t0_in', length=1, delay_cost=1)
	S += c_paa_t4_t0_in >= 74
	c_paa_t4_t0_in += MM_in[0]

	c_paa_t4_t0_mem0 = S.Task('c_paa_t4_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t0_mem0 >= 74
	c_paa_t4_t0_mem0 += MAS_MEM[4]

	c_paa_t4_t0_mem1 = S.Task('c_paa_t4_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t0_mem1 >= 74
	c_paa_t4_t0_mem1 += MAS_MEM[5]

	c_pbc_t1_t4 = S.Task('c_pbc_t1_t4', length=7, delay_cost=1)
	S += c_pbc_t1_t4 >= 74
	c_pbc_t1_t4 += MM[0]

	c_pcb00_mem0 = S.Task('c_pcb00_mem0', length=1, delay_cost=1)
	S += c_pcb00_mem0 >= 74
	c_pcb00_mem0 += MAS_MEM[0]

	c_pcb00_mem1 = S.Task('c_pcb00_mem1', length=1, delay_cost=1)
	S += c_pcb00_mem1 >= 74
	c_pcb00_mem1 += MAS_MEM[3]

	c_pcb_t0_t5 = S.Task('c_pcb_t0_t5', length=2, delay_cost=1)
	S += c_pcb_t0_t5 >= 74
	c_pcb_t0_t5 += MAS[2]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 75
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_paa_t4_t0 = S.Task('c_paa_t4_t0', length=7, delay_cost=1)
	S += c_paa_t4_t0 >= 75
	c_paa_t4_t0 += MM[0]

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem1 >= 75
	c_pbc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_pbc_t4_t4_in = S.Task('c_pbc_t4_t4_in', length=1, delay_cost=1)
	S += c_pbc_t4_t4_in >= 75
	c_pbc_t4_t4_in += MM_in[0]

	c_pbc_t4_t4_mem0 = S.Task('c_pbc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t4_mem0 >= 75
	c_pbc_t4_t4_mem0 += MAS_MEM[6]

	c_pbc_t4_t4_mem1 = S.Task('c_pbc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t4_mem1 >= 75
	c_pbc_t4_t4_mem1 += MAS_MEM[3]

	c_pcb00 = S.Task('c_pcb00', length=2, delay_cost=1)
	S += c_pcb00 >= 75
	c_pcb00 += MAS[1]

	c_pcb_t01_mem0 = S.Task('c_pcb_t01_mem0', length=1, delay_cost=1)
	S += c_pcb_t01_mem0 >= 75
	c_pcb_t01_mem0 += MM_MEM[0]

	c_pcb_t01_mem1 = S.Task('c_pcb_t01_mem1', length=1, delay_cost=1)
	S += c_pcb_t01_mem1 >= 75
	c_pcb_t01_mem1 += MAS_MEM[5]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 76
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_pbc_t4_t4 = S.Task('c_pbc_t4_t4', length=7, delay_cost=1)
	S += c_pbc_t4_t4 >= 76
	c_pbc_t4_t4 += MM[0]

	c_pcb_t01 = S.Task('c_pcb_t01', length=2, delay_cost=1)
	S += c_pcb_t01 >= 76
	c_pcb_t01 += MAS[2]

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem1 >= 76
	c_pcb_t1_t1_mem1 += MAIN_MEM_r[1]

	c_pcb_t40_mem0 = S.Task('c_pcb_t40_mem0', length=1, delay_cost=1)
	S += c_pcb_t40_mem0 >= 76
	c_pcb_t40_mem0 += MM_MEM[0]

	c_pcb_t40_mem1 = S.Task('c_pcb_t40_mem1', length=1, delay_cost=1)
	S += c_pcb_t40_mem1 >= 76
	c_pcb_t40_mem1 += MM_MEM[1]

	c_pcb_t4_t4_in = S.Task('c_pcb_t4_t4_in', length=1, delay_cost=1)
	S += c_pcb_t4_t4_in >= 76
	c_pcb_t4_t4_in += MM_in[0]

	c_pcb_t4_t4_mem0 = S.Task('c_pcb_t4_t4_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t4_mem0 >= 76
	c_pcb_t4_t4_mem0 += MAS_MEM[6]

	c_pcb_t4_t4_mem1 = S.Task('c_pcb_t4_t4_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t4_mem1 >= 76
	c_pcb_t4_t4_mem1 += MAS_MEM[5]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 77
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_paa_t01_mem0 = S.Task('c_paa_t01_mem0', length=1, delay_cost=1)
	S += c_paa_t01_mem0 >= 77
	c_paa_t01_mem0 += MM_MEM[0]

	c_paa_t01_mem1 = S.Task('c_paa_t01_mem1', length=1, delay_cost=1)
	S += c_paa_t01_mem1 >= 77
	c_paa_t01_mem1 += MAS_MEM[7]

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t1_mem1 >= 77
	c_paa_t1_t1_mem1 += MAIN_MEM_r[1]

	c_pcb01_mem0 = S.Task('c_pcb01_mem0', length=1, delay_cost=1)
	S += c_pcb01_mem0 >= 77
	c_pcb01_mem0 += MAS_MEM[4]

	c_pcb01_mem1 = S.Task('c_pcb01_mem1', length=1, delay_cost=1)
	S += c_pcb01_mem1 >= 77
	c_pcb01_mem1 += MAS_MEM[3]

	c_pcb_t40 = S.Task('c_pcb_t40', length=2, delay_cost=1)
	S += c_pcb_t40 >= 77
	c_pcb_t40 += MAS[1]

	c_pcb_t4_t4 = S.Task('c_pcb_t4_t4', length=7, delay_cost=1)
	S += c_pcb_t4_t4 >= 77
	c_pcb_t4_t4 += MM[0]

	c_pcb_t50_mem0 = S.Task('c_pcb_t50_mem0', length=1, delay_cost=1)
	S += c_pcb_t50_mem0 >= 77
	c_pcb_t50_mem0 += MAS_MEM[0]

	c_pcb_t50_mem1 = S.Task('c_pcb_t50_mem1', length=1, delay_cost=1)
	S += c_pcb_t50_mem1 >= 77
	c_pcb_t50_mem1 += MAS_MEM[5]

	c_paa_t01 = S.Task('c_paa_t01', length=2, delay_cost=1)
	S += c_paa_t01 >= 78
	c_paa_t01 += MAS[3]

	c_paa_t4_t4_in = S.Task('c_paa_t4_t4_in', length=1, delay_cost=1)
	S += c_paa_t4_t4_in >= 78
	c_paa_t4_t4_in += MM_in[0]

	c_paa_t4_t4_mem0 = S.Task('c_paa_t4_t4_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t4_mem0 >= 78
	c_paa_t4_t4_mem0 += MAS_MEM[2]

	c_paa_t4_t4_mem1 = S.Task('c_paa_t4_t4_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t4_mem1 >= 78
	c_paa_t4_t4_mem1 += MAS_MEM[5]

	c_pbc_t1_t0_mem1 = S.Task('c_pbc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t0_mem1 >= 78
	c_pbc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_pbc_t40_mem0 = S.Task('c_pbc_t40_mem0', length=1, delay_cost=1)
	S += c_pbc_t40_mem0 >= 78
	c_pbc_t40_mem0 += MM_MEM[0]

	c_pbc_t40_mem1 = S.Task('c_pbc_t40_mem1', length=1, delay_cost=1)
	S += c_pbc_t40_mem1 >= 78
	c_pbc_t40_mem1 += MM_MEM[1]

	c_pcb01 = S.Task('c_pcb01', length=2, delay_cost=1)
	S += c_pcb01 >= 78
	c_pcb01 += MAS[2]

	c_pcb_t50 = S.Task('c_pcb_t50', length=2, delay_cost=1)
	S += c_pcb_t50 >= 78
	c_pcb_t50 += MAS[1]

	c_pcb_t51_mem0 = S.Task('c_pcb_t51_mem0', length=1, delay_cost=1)
	S += c_pcb_t51_mem0 >= 78
	c_pcb_t51_mem0 += MAS_MEM[4]

	c_pcb_t51_mem1 = S.Task('c_pcb_t51_mem1', length=1, delay_cost=1)
	S += c_pcb_t51_mem1 >= 78
	c_pcb_t51_mem1 += MAS_MEM[1]

	c_paa_t0_t1_mem1 = S.Task('c_paa_t0_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t1_mem1 >= 79
	c_paa_t0_t1_mem1 += MAIN_MEM_r[1]

	c_paa_t4_t4 = S.Task('c_paa_t4_t4', length=7, delay_cost=1)
	S += c_paa_t4_t4 >= 79
	c_paa_t4_t4 += MM[0]

	c_paa_t51_mem0 = S.Task('c_paa_t51_mem0', length=1, delay_cost=1)
	S += c_paa_t51_mem0 >= 79
	c_paa_t51_mem0 += MAS_MEM[6]

	c_paa_t51_mem1 = S.Task('c_paa_t51_mem1', length=1, delay_cost=1)
	S += c_paa_t51_mem1 >= 79
	c_paa_t51_mem1 += MAS_MEM[1]

	c_pbc_t40 = S.Task('c_pbc_t40', length=2, delay_cost=1)
	S += c_pbc_t40 >= 79
	c_pbc_t40 += MAS[2]

	c_pbc_t4_t5_mem0 = S.Task('c_pbc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t5_mem0 >= 79
	c_pbc_t4_t5_mem0 += MM_MEM[0]

	c_pbc_t4_t5_mem1 = S.Task('c_pbc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t5_mem1 >= 79
	c_pbc_t4_t5_mem1 += MM_MEM[1]

	c_pcb10_mem0 = S.Task('c_pcb10_mem0', length=1, delay_cost=1)
	S += c_pcb10_mem0 >= 79
	c_pcb10_mem0 += MAS_MEM[2]

	c_pcb10_mem1 = S.Task('c_pcb10_mem1', length=1, delay_cost=1)
	S += c_pcb10_mem1 >= 79
	c_pcb10_mem1 += MAS_MEM[3]

	c_pcb_t51 = S.Task('c_pcb_t51', length=2, delay_cost=1)
	S += c_pcb_t51 >= 79
	c_pcb_t51 += MAS[0]

	c_paa01_mem0 = S.Task('c_paa01_mem0', length=1, delay_cost=1)
	S += c_paa01_mem0 >= 80
	c_paa01_mem0 += MAS_MEM[6]

	c_paa01_mem1 = S.Task('c_paa01_mem1', length=1, delay_cost=1)
	S += c_paa01_mem1 >= 80
	c_paa01_mem1 += MAS_MEM[3]

	c_paa_t51 = S.Task('c_paa_t51', length=2, delay_cost=1)
	S += c_paa_t51 >= 80
	c_paa_t51 += MAS[3]

	c_pbc10_mem0 = S.Task('c_pbc10_mem0', length=1, delay_cost=1)
	S += c_pbc10_mem0 >= 80
	c_pbc10_mem0 += MAS_MEM[4]

	c_pbc10_mem1 = S.Task('c_pbc10_mem1', length=1, delay_cost=1)
	S += c_pbc10_mem1 >= 80
	c_pbc10_mem1 += MAS_MEM[5]

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem1 >= 80
	c_pbc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_pbc_t11_mem0 = S.Task('c_pbc_t11_mem0', length=1, delay_cost=1)
	S += c_pbc_t11_mem0 >= 80
	c_pbc_t11_mem0 += MM_MEM[0]

	c_pbc_t11_mem1 = S.Task('c_pbc_t11_mem1', length=1, delay_cost=1)
	S += c_pbc_t11_mem1 >= 80
	c_pbc_t11_mem1 += MAS_MEM[1]

	c_pbc_t4_t5 = S.Task('c_pbc_t4_t5', length=2, delay_cost=1)
	S += c_pbc_t4_t5 >= 80
	c_pbc_t4_t5 += MAS[0]

	c_pcb10 = S.Task('c_pcb10', length=2, delay_cost=1)
	S += c_pcb10 >= 80
	c_pcb10 += MAS[1]

	c_paa01 = S.Task('c_paa01', length=2, delay_cost=1)
	S += c_paa01 >= 81
	c_paa01 += MAS[1]

	c_paa_t0_t0_mem1 = S.Task('c_paa_t0_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t0_mem1 >= 81
	c_paa_t0_t0_mem1 += MAIN_MEM_r[1]

	c_pbc10 = S.Task('c_pbc10', length=2, delay_cost=1)
	S += c_pbc10 >= 81
	c_pbc10 += MAS[0]

	c_pbc_t11 = S.Task('c_pbc_t11', length=2, delay_cost=1)
	S += c_pbc_t11 >= 81
	c_pbc_t11 += MAS[2]

	c_pcb_t4_t5_mem0 = S.Task('c_pcb_t4_t5_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t5_mem0 >= 81
	c_pcb_t4_t5_mem0 += MM_MEM[0]

	c_pcb_t4_t5_mem1 = S.Task('c_pcb_t4_t5_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t5_mem1 >= 81
	c_pcb_t4_t5_mem1 += MM_MEM[1]

	c_pbc_s00_mem0 = S.Task('c_pbc_s00_mem0', length=1, delay_cost=1)
	S += c_pbc_s00_mem0 >= 82
	c_pbc_s00_mem0 += MAS_MEM[6]

	c_pbc_s00_mem1 = S.Task('c_pbc_s00_mem1', length=1, delay_cost=1)
	S += c_pbc_s00_mem1 >= 82
	c_pbc_s00_mem1 += MAS_MEM[5]

	c_pbc_s01_mem0 = S.Task('c_pbc_s01_mem0', length=1, delay_cost=1)
	S += c_pbc_s01_mem0 >= 82
	c_pbc_s01_mem0 += MAS_MEM[4]

	c_pbc_s01_mem1 = S.Task('c_pbc_s01_mem1', length=1, delay_cost=1)
	S += c_pbc_s01_mem1 >= 82
	c_pbc_s01_mem1 += MAS_MEM[7]

	c_pbc_t1_t1_mem1 = S.Task('c_pbc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t1_mem1 >= 82
	c_pbc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_pbc_t41_mem0 = S.Task('c_pbc_t41_mem0', length=1, delay_cost=1)
	S += c_pbc_t41_mem0 >= 82
	c_pbc_t41_mem0 += MM_MEM[0]

	c_pbc_t41_mem1 = S.Task('c_pbc_t41_mem1', length=1, delay_cost=1)
	S += c_pbc_t41_mem1 >= 82
	c_pbc_t41_mem1 += MAS_MEM[1]

	c_pbccb10_mem0 = S.Task('c_pbccb10_mem0', length=1, delay_cost=1)
	S += c_pbccb10_mem0 >= 82
	c_pbccb10_mem0 += MAS_MEM[0]

	c_pbccb10_mem1 = S.Task('c_pbccb10_mem1', length=1, delay_cost=1)
	S += c_pbccb10_mem1 >= 82
	c_pbccb10_mem1 += MAS_MEM[3]

	c_pcb_t4_t5 = S.Task('c_pcb_t4_t5', length=2, delay_cost=1)
	S += c_pcb_t4_t5 >= 82
	c_pcb_t4_t5 += MAS[0]

	c_pbc_s00 = S.Task('c_pbc_s00', length=2, delay_cost=1)
	S += c_pbc_s00 >= 83
	c_pbc_s00 += MAS[2]

	c_pbc_s01 = S.Task('c_pbc_s01', length=2, delay_cost=1)
	S += c_pbc_s01 >= 83
	c_pbc_s01 += MAS[3]

	c_pbc_t41 = S.Task('c_pbc_t41', length=2, delay_cost=1)
	S += c_pbc_t41 >= 83
	c_pbc_t41 += MAS[1]

	c_pbc_t51_mem0 = S.Task('c_pbc_t51_mem0', length=1, delay_cost=1)
	S += c_pbc_t51_mem0 >= 83
	c_pbc_t51_mem0 += MAS_MEM[4]

	c_pbc_t51_mem1 = S.Task('c_pbc_t51_mem1', length=1, delay_cost=1)
	S += c_pbc_t51_mem1 >= 83
	c_pbc_t51_mem1 += MAS_MEM[5]

	c_pbccb10 = S.Task('c_pbccb10', length=2, delay_cost=1)
	S += c_pbccb10 >= 83
	c_pbccb10 += MAS[3]

	c_pcb_t0_t1_mem1 = S.Task('c_pcb_t0_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t1_mem1 >= 83
	c_pcb_t0_t1_mem1 += MAIN_MEM_r[1]

	c_pcb_t41_mem0 = S.Task('c_pcb_t41_mem0', length=1, delay_cost=1)
	S += c_pcb_t41_mem0 >= 83
	c_pcb_t41_mem0 += MM_MEM[0]

	c_pcb_t41_mem1 = S.Task('c_pcb_t41_mem1', length=1, delay_cost=1)
	S += c_pcb_t41_mem1 >= 83
	c_pcb_t41_mem1 += MAS_MEM[1]

	c_paa_t4_t5_mem0 = S.Task('c_paa_t4_t5_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t5_mem0 >= 84
	c_paa_t4_t5_mem0 += MM_MEM[0]

	c_paa_t4_t5_mem1 = S.Task('c_paa_t4_t5_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t5_mem1 >= 84
	c_paa_t4_t5_mem1 += MM_MEM[1]

	c_pbc00_mem0 = S.Task('c_pbc00_mem0', length=1, delay_cost=1)
	S += c_pbc00_mem0 >= 84
	c_pbc00_mem0 += MAS_MEM[6]

	c_pbc00_mem1 = S.Task('c_pbc00_mem1', length=1, delay_cost=1)
	S += c_pbc00_mem1 >= 84
	c_pbc00_mem1 += MAS_MEM[5]

	c_pbc01_mem0 = S.Task('c_pbc01_mem0', length=1, delay_cost=1)
	S += c_pbc01_mem0 >= 84
	c_pbc01_mem0 += MAS_MEM[4]

	c_pbc01_mem1 = S.Task('c_pbc01_mem1', length=1, delay_cost=1)
	S += c_pbc01_mem1 >= 84
	c_pbc01_mem1 += MAS_MEM[7]

	c_pbc_t51 = S.Task('c_pbc_t51', length=2, delay_cost=1)
	S += c_pbc_t51 >= 84
	c_pbc_t51 += MAS[1]

	c_pcb_t41 = S.Task('c_pcb_t41', length=2, delay_cost=1)
	S += c_pcb_t41 >= 84
	c_pcb_t41 += MAS[2]

	c_paa_t40_mem0 = S.Task('c_paa_t40_mem0', length=1, delay_cost=1)
	S += c_paa_t40_mem0 >= 85
	c_paa_t40_mem0 += MM_MEM[0]

	c_paa_t40_mem1 = S.Task('c_paa_t40_mem1', length=1, delay_cost=1)
	S += c_paa_t40_mem1 >= 85
	c_paa_t40_mem1 += MM_MEM[1]

	c_paa_t4_t5 = S.Task('c_paa_t4_t5', length=2, delay_cost=1)
	S += c_paa_t4_t5 >= 85
	c_paa_t4_t5 += MAS[0]

	c_pbc00 = S.Task('c_pbc00', length=2, delay_cost=1)
	S += c_pbc00 >= 85
	c_pbc00 += MAS[3]

	c_pbc01 = S.Task('c_pbc01', length=2, delay_cost=1)
	S += c_pbc01 >= 85
	c_pbc01 += MAS[1]

	c_pbc11_mem0 = S.Task('c_pbc11_mem0', length=1, delay_cost=1)
	S += c_pbc11_mem0 >= 85
	c_pbc11_mem0 += MAS_MEM[2]

	c_pbc11_mem1 = S.Task('c_pbc11_mem1', length=1, delay_cost=1)
	S += c_pbc11_mem1 >= 85
	c_pbc11_mem1 += MAS_MEM[3]

	c_pcb11_mem0 = S.Task('c_pcb11_mem0', length=1, delay_cost=1)
	S += c_pcb11_mem0 >= 85
	c_pcb11_mem0 += MAS_MEM[4]

	c_pcb11_mem1 = S.Task('c_pcb11_mem1', length=1, delay_cost=1)
	S += c_pcb11_mem1 >= 85
	c_pcb11_mem1 += MAS_MEM[1]

	c_paa_t40 = S.Task('c_paa_t40', length=2, delay_cost=1)
	S += c_paa_t40 >= 86
	c_paa_t40 += MAS[1]

	c_paa_t41_mem0 = S.Task('c_paa_t41_mem0', length=1, delay_cost=1)
	S += c_paa_t41_mem0 >= 86
	c_paa_t41_mem0 += MM_MEM[0]

	c_paa_t41_mem1 = S.Task('c_paa_t41_mem1', length=1, delay_cost=1)
	S += c_paa_t41_mem1 >= 86
	c_paa_t41_mem1 += MAS_MEM[1]

	c_pbc11 = S.Task('c_pbc11', length=2, delay_cost=1)
	S += c_pbc11 >= 86
	c_pbc11 += MAS[3]

	c_pbccb00_mem0 = S.Task('c_pbccb00_mem0', length=1, delay_cost=1)
	S += c_pbccb00_mem0 >= 86
	c_pbccb00_mem0 += MAS_MEM[6]

	c_pbccb00_mem1 = S.Task('c_pbccb00_mem1', length=1, delay_cost=1)
	S += c_pbccb00_mem1 >= 86
	c_pbccb00_mem1 += MAS_MEM[3]

	c_pbccb01_mem0 = S.Task('c_pbccb01_mem0', length=1, delay_cost=1)
	S += c_pbccb01_mem0 >= 86
	c_pbccb01_mem0 += MAS_MEM[2]

	c_pbccb01_mem1 = S.Task('c_pbccb01_mem1', length=1, delay_cost=1)
	S += c_pbccb01_mem1 >= 86
	c_pbccb01_mem1 += MAS_MEM[5]

	c_pcb11 = S.Task('c_pcb11', length=2, delay_cost=1)
	S += c_pcb11 >= 86
	c_pcb11 += MAS[0]

	c_paa10_mem0 = S.Task('c_paa10_mem0', length=1, delay_cost=1)
	S += c_paa10_mem0 >= 87
	c_paa10_mem0 += MAS_MEM[2]

	c_paa10_mem1 = S.Task('c_paa10_mem1', length=1, delay_cost=1)
	S += c_paa10_mem1 >= 87
	c_paa10_mem1 += MAS_MEM[3]

	c_paa_t41 = S.Task('c_paa_t41', length=2, delay_cost=1)
	S += c_paa_t41 >= 87
	c_paa_t41 += MAS[0]

	c_pbccb00 = S.Task('c_pbccb00', length=2, delay_cost=1)
	S += c_pbccb00 >= 87
	c_pbccb00 += MAS[2]

	c_pbccb01 = S.Task('c_pbccb01', length=2, delay_cost=1)
	S += c_pbccb01 >= 87
	c_pbccb01 += MAS[3]

	c_pbccb11_mem0 = S.Task('c_pbccb11_mem0', length=1, delay_cost=1)
	S += c_pbccb11_mem0 >= 87
	c_pbccb11_mem0 += MAS_MEM[6]

	c_pbccb11_mem1 = S.Task('c_pbccb11_mem1', length=1, delay_cost=1)
	S += c_pbccb11_mem1 >= 87
	c_pbccb11_mem1 += MAS_MEM[1]

	c_paa10 = S.Task('c_paa10', length=2, delay_cost=1)
	S += c_paa10 >= 88
	c_paa10 += MAS[2]

	c_paa11_mem0 = S.Task('c_paa11_mem0', length=1, delay_cost=1)
	S += c_paa11_mem0 >= 88
	c_paa11_mem0 += MAS_MEM[0]

	c_paa11_mem1 = S.Task('c_paa11_mem1', length=1, delay_cost=1)
	S += c_paa11_mem1 >= 88
	c_paa11_mem1 += MAS_MEM[7]

	c_pbccb11 = S.Task('c_pbccb11', length=2, delay_cost=1)
	S += c_pbccb11 >= 88
	c_pbccb11 += MAS[0]

	c_paa11 = S.Task('c_paa11', length=2, delay_cost=1)
	S += c_paa11 >= 89
	c_paa11 += MAS[1]

	c_pxi_y1_0_mem0 = S.Task('c_pxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_pxi_y1_0_mem0 >= 89
	c_pxi_y1_0_mem0 += MAS_MEM[6]

	c_pxi_y1_0_mem1 = S.Task('c_pxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_pxi_y1_0_mem1 >= 89
	c_pxi_y1_0_mem1 += MAS_MEM[1]

	c_pxi_y1_1_mem0 = S.Task('c_pxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_pxi_y1_1_mem0 >= 89
	c_pxi_y1_1_mem0 += MAS_MEM[0]

	c_pxi_y1_1_mem1 = S.Task('c_pxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_pxi_y1_1_mem1 >= 89
	c_pxi_y1_1_mem1 += MAS_MEM[7]

	c_q10_mem0 = S.Task('c_q10_mem0', length=1, delay_cost=1)
	S += c_q10_mem0 >= 89
	c_q10_mem0 += MAS_MEM[4]

	c_q10_mem1 = S.Task('c_q10_mem1', length=1, delay_cost=1)
	S += c_q10_mem1 >= 89
	c_q10_mem1 += MAS_MEM[5]

	c_pxi_y1_0 = S.Task('c_pxi_y1_0', length=2, delay_cost=1)
	S += c_pxi_y1_0 >= 90
	c_pxi_y1_0 += MAS[0]

	c_pxi_y1_1 = S.Task('c_pxi_y1_1', length=2, delay_cost=1)
	S += c_pxi_y1_1 >= 90
	c_pxi_y1_1 += MAS[1]

	c_q10 = S.Task('c_q10', length=2, delay_cost=1)
	S += c_q10 >= 90
	c_q10 += MAS[3]

	c_q11_mem0 = S.Task('c_q11_mem0', length=1, delay_cost=1)
	S += c_q11_mem0 >= 90
	c_q11_mem0 += MAS_MEM[6]

	c_q11_mem1 = S.Task('c_q11_mem1', length=1, delay_cost=1)
	S += c_q11_mem1 >= 90
	c_q11_mem1 += MAS_MEM[3]

	c_q00_mem0 = S.Task('c_q00_mem0', length=1, delay_cost=1)
	S += c_q00_mem0 >= 91
	c_q00_mem0 += MAS_MEM[0]

	c_q00_mem1 = S.Task('c_q00_mem1', length=1, delay_cost=1)
	S += c_q00_mem1 >= 91
	c_q00_mem1 += MAS_MEM[3]

	c_q11 = S.Task('c_q11', length=2, delay_cost=1)
	S += c_q11 >= 91
	c_q11 += MAS[3]

	c_qinv_bb_t0_in = S.Task('c_qinv_bb_t0_in', length=1, delay_cost=1)
	S += c_qinv_bb_t0_in >= 91
	c_qinv_bb_t0_in += MM_in[0]

	c_qinv_bb_t0_mem0 = S.Task('c_qinv_bb_t0_mem0', length=1, delay_cost=1)
	S += c_qinv_bb_t0_mem0 >= 91
	c_qinv_bb_t0_mem0 += MAS_MEM[6]

	c_q00 = S.Task('c_q00', length=2, delay_cost=1)
	S += c_q00 >= 92
	c_q00 += MAS[2]

	c_qinv_bb_t0 = S.Task('c_qinv_bb_t0', length=7, delay_cost=1)
	S += c_qinv_bb_t0 >= 92
	c_qinv_bb_t0 += MM[0]

	c_qinv_bb_t1_in = S.Task('c_qinv_bb_t1_in', length=1, delay_cost=1)
	S += c_qinv_bb_t1_in >= 92
	c_qinv_bb_t1_in += MM_in[0]

	c_qinv_bb_t1_mem0 = S.Task('c_qinv_bb_t1_mem0', length=1, delay_cost=1)
	S += c_qinv_bb_t1_mem0 >= 92
	c_qinv_bb_t1_mem0 += MAS_MEM[6]

	c_qinv_aa_t0_in = S.Task('c_qinv_aa_t0_in', length=1, delay_cost=1)
	S += c_qinv_aa_t0_in >= 93
	c_qinv_aa_t0_in += MM_in[0]

	c_qinv_aa_t0_mem0 = S.Task('c_qinv_aa_t0_mem0', length=1, delay_cost=1)
	S += c_qinv_aa_t0_mem0 >= 93
	c_qinv_aa_t0_mem0 += MAS_MEM[4]

	c_qinv_bb_t1 = S.Task('c_qinv_bb_t1', length=7, delay_cost=1)
	S += c_qinv_bb_t1 >= 93
	c_qinv_bb_t1 += MM[0]

	c_qinv_bb_t3_mem0 = S.Task('c_qinv_bb_t3_mem0', length=1, delay_cost=1)
	S += c_qinv_bb_t3_mem0 >= 93
	c_qinv_bb_t3_mem0 += MAS_MEM[6]

	c_qinv_bb_t3_mem1 = S.Task('c_qinv_bb_t3_mem1', length=1, delay_cost=1)
	S += c_qinv_bb_t3_mem1 >= 93
	c_qinv_bb_t3_mem1 += MAS_MEM[7]

	c_qinv_aa_t0 = S.Task('c_qinv_aa_t0', length=7, delay_cost=1)
	S += c_qinv_aa_t0 >= 94
	c_qinv_aa_t0 += MM[0]

	c_qinv_bb_t2_mem0 = S.Task('c_qinv_bb_t2_mem0', length=1, delay_cost=1)
	S += c_qinv_bb_t2_mem0 >= 94
	c_qinv_bb_t2_mem0 += MAS_MEM[6]

	c_qinv_bb_t2_mem1 = S.Task('c_qinv_bb_t2_mem1', length=1, delay_cost=1)
	S += c_qinv_bb_t2_mem1 >= 94
	c_qinv_bb_t2_mem1 += MAS_MEM[7]

	c_qinv_bb_t3 = S.Task('c_qinv_bb_t3', length=2, delay_cost=1)
	S += c_qinv_bb_t3 >= 94
	c_qinv_bb_t3 += MAS[0]

	c_qinv_bb_t2 = S.Task('c_qinv_bb_t2', length=2, delay_cost=1)
	S += c_qinv_bb_t2 >= 95
	c_qinv_bb_t2 += MAS[0]

	c_qinv_bb_t4_in = S.Task('c_qinv_bb_t4_in', length=1, delay_cost=1)
	S += c_qinv_bb_t4_in >= 96
	c_qinv_bb_t4_in += MM_in[0]

	c_qinv_bb_t4_mem0 = S.Task('c_qinv_bb_t4_mem0', length=1, delay_cost=1)
	S += c_qinv_bb_t4_mem0 >= 96
	c_qinv_bb_t4_mem0 += MAS_MEM[0]

	c_qinv_bb_t4_mem1 = S.Task('c_qinv_bb_t4_mem1', length=1, delay_cost=1)
	S += c_qinv_bb_t4_mem1 >= 96
	c_qinv_bb_t4_mem1 += MAS_MEM[1]

	c_qinv_aa_t4_in = S.Task('c_qinv_aa_t4_in', length=1, delay_cost=1)
	S += c_qinv_aa_t4_in >= 97
	c_qinv_aa_t4_in += MM_in[0]

	c_qinv_aa_t4_mem0 = S.Task('c_qinv_aa_t4_mem0', length=1, delay_cost=1)
	S += c_qinv_aa_t4_mem0 >= 97
	c_qinv_aa_t4_mem0 += MAS_MEM[0]

	c_qinv_aa_t4_mem1 = S.Task('c_qinv_aa_t4_mem1', length=1, delay_cost=1)
	S += c_qinv_aa_t4_mem1 >= 97
	c_qinv_aa_t4_mem1 += MAS_MEM[7]

	c_qinv_bb_t4 = S.Task('c_qinv_bb_t4', length=7, delay_cost=1)
	S += c_qinv_bb_t4 >= 97
	c_qinv_bb_t4 += MM[0]

	c_qinv_aa_t4 = S.Task('c_qinv_aa_t4', length=7, delay_cost=1)
	S += c_qinv_aa_t4 >= 98
	c_qinv_aa_t4 += MM[0]

	c_qinv_bb0_mem0 = S.Task('c_qinv_bb0_mem0', length=1, delay_cost=1)
	S += c_qinv_bb0_mem0 >= 99
	c_qinv_bb0_mem0 += MM_MEM[0]

	c_qinv_bb0_mem1 = S.Task('c_qinv_bb0_mem1', length=1, delay_cost=1)
	S += c_qinv_bb0_mem1 >= 99
	c_qinv_bb0_mem1 += MM_MEM[1]

	c_qinv_bb0 = S.Task('c_qinv_bb0', length=2, delay_cost=1)
	S += c_qinv_bb0 >= 100
	c_qinv_bb0 += MAS[2]

	c_qinv_bb_t5_mem0 = S.Task('c_qinv_bb_t5_mem0', length=1, delay_cost=1)
	S += c_qinv_bb_t5_mem0 >= 100
	c_qinv_bb_t5_mem0 += MM_MEM[0]

	c_qinv_bb_t5_mem1 = S.Task('c_qinv_bb_t5_mem1', length=1, delay_cost=1)
	S += c_qinv_bb_t5_mem1 >= 100
	c_qinv_bb_t5_mem1 += MM_MEM[1]

	c_qinv_aa_t5_mem0 = S.Task('c_qinv_aa_t5_mem0', length=1, delay_cost=1)
	S += c_qinv_aa_t5_mem0 >= 101
	c_qinv_aa_t5_mem0 += MM_MEM[0]

	c_qinv_aa_t5_mem1 = S.Task('c_qinv_aa_t5_mem1', length=1, delay_cost=1)
	S += c_qinv_aa_t5_mem1 >= 101
	c_qinv_aa_t5_mem1 += MM_MEM[1]

	c_qinv_bb_t5 = S.Task('c_qinv_bb_t5', length=2, delay_cost=1)
	S += c_qinv_bb_t5 >= 101
	c_qinv_bb_t5 += MAS[3]

	c_qinv_aa0_mem0 = S.Task('c_qinv_aa0_mem0', length=1, delay_cost=1)
	S += c_qinv_aa0_mem0 >= 102
	c_qinv_aa0_mem0 += MM_MEM[0]

	c_qinv_aa0_mem1 = S.Task('c_qinv_aa0_mem1', length=1, delay_cost=1)
	S += c_qinv_aa0_mem1 >= 102
	c_qinv_aa0_mem1 += MM_MEM[1]

	c_qinv_aa_t5 = S.Task('c_qinv_aa_t5', length=2, delay_cost=1)
	S += c_qinv_aa_t5 >= 102
	c_qinv_aa_t5 += MAS[3]

	c_qinv_aa0 = S.Task('c_qinv_aa0', length=2, delay_cost=1)
	S += c_qinv_aa0 >= 103
	c_qinv_aa0 += MAS[1]

	c_qinv_bb1_mem0 = S.Task('c_qinv_bb1_mem0', length=1, delay_cost=1)
	S += c_qinv_bb1_mem0 >= 103
	c_qinv_bb1_mem0 += MM_MEM[0]

	c_qinv_bb1_mem1 = S.Task('c_qinv_bb1_mem1', length=1, delay_cost=1)
	S += c_qinv_bb1_mem1 >= 103
	c_qinv_bb1_mem1 += MAS_MEM[7]

	c_qinv_aa1_mem0 = S.Task('c_qinv_aa1_mem0', length=1, delay_cost=1)
	S += c_qinv_aa1_mem0 >= 104
	c_qinv_aa1_mem0 += MM_MEM[0]

	c_qinv_aa1_mem1 = S.Task('c_qinv_aa1_mem1', length=1, delay_cost=1)
	S += c_qinv_aa1_mem1 >= 104
	c_qinv_aa1_mem1 += MAS_MEM[7]

	c_qinv_bb1 = S.Task('c_qinv_bb1', length=2, delay_cost=1)
	S += c_qinv_bb1 >= 104
	c_qinv_bb1 += MAS[1]

	c_qinv_aa1 = S.Task('c_qinv_aa1', length=2, delay_cost=1)
	S += c_qinv_aa1 >= 105
	c_qinv_aa1 += MAS[0]

	c_qinv_bbxi0_mem0 = S.Task('c_qinv_bbxi0_mem0', length=1, delay_cost=1)
	S += c_qinv_bbxi0_mem0 >= 105
	c_qinv_bbxi0_mem0 += MAS_MEM[4]

	c_qinv_bbxi0_mem1 = S.Task('c_qinv_bbxi0_mem1', length=1, delay_cost=1)
	S += c_qinv_bbxi0_mem1 >= 105
	c_qinv_bbxi0_mem1 += MAS_MEM[3]

	c_qinv_bbxi1_mem0 = S.Task('c_qinv_bbxi1_mem0', length=1, delay_cost=1)
	S += c_qinv_bbxi1_mem0 >= 105
	c_qinv_bbxi1_mem0 += MAS_MEM[2]

	c_qinv_bbxi1_mem1 = S.Task('c_qinv_bbxi1_mem1', length=1, delay_cost=1)
	S += c_qinv_bbxi1_mem1 >= 105
	c_qinv_bbxi1_mem1 += MAS_MEM[5]

	c_qinv_bbxi0 = S.Task('c_qinv_bbxi0', length=2, delay_cost=1)
	S += c_qinv_bbxi0 >= 106
	c_qinv_bbxi0 += MAS[0]

	c_qinv_bbxi1 = S.Task('c_qinv_bbxi1', length=2, delay_cost=1)
	S += c_qinv_bbxi1 >= 106
	c_qinv_bbxi1 += MAS[3]

	c_qinv_denom0_mem0 = S.Task('c_qinv_denom0_mem0', length=1, delay_cost=1)
	S += c_qinv_denom0_mem0 >= 107
	c_qinv_denom0_mem0 += MAS_MEM[2]

	c_qinv_denom0_mem1 = S.Task('c_qinv_denom0_mem1', length=1, delay_cost=1)
	S += c_qinv_denom0_mem1 >= 107
	c_qinv_denom0_mem1 += MAS_MEM[1]

	c_qinv_denom1_mem0 = S.Task('c_qinv_denom1_mem0', length=1, delay_cost=1)
	S += c_qinv_denom1_mem0 >= 107
	c_qinv_denom1_mem0 += MAS_MEM[0]

	c_qinv_denom1_mem1 = S.Task('c_qinv_denom1_mem1', length=1, delay_cost=1)
	S += c_qinv_denom1_mem1 >= 107
	c_qinv_denom1_mem1 += MAS_MEM[7]

	c_qinv_denom0 = S.Task('c_qinv_denom0', length=2, delay_cost=1)
	S += c_qinv_denom0 >= 108
	c_qinv_denom0 += MAS[1]

	c_qinv_denom1 = S.Task('c_qinv_denom1', length=2, delay_cost=1)
	S += c_qinv_denom1 >= 108
	c_qinv_denom1 += MAS[3]

	c_qinv_denom_inv_bb_in = S.Task('c_qinv_denom_inv_bb_in', length=1, delay_cost=1)
	S += c_qinv_denom_inv_bb_in >= 109
	c_qinv_denom_inv_bb_in += MM_in[0]

	c_qinv_denom_inv_bb_mem0 = S.Task('c_qinv_denom_inv_bb_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv_bb_mem0 >= 109
	c_qinv_denom_inv_bb_mem0 += MAS_MEM[6]

	c_qinv_denom_inv_aa_in = S.Task('c_qinv_denom_inv_aa_in', length=1, delay_cost=1)
	S += c_qinv_denom_inv_aa_in >= 110
	c_qinv_denom_inv_aa_in += MM_in[0]

	c_qinv_denom_inv_aa_mem0 = S.Task('c_qinv_denom_inv_aa_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv_aa_mem0 >= 110
	c_qinv_denom_inv_aa_mem0 += MAS_MEM[2]

	c_qinv_denom_inv_bb = S.Task('c_qinv_denom_inv_bb', length=7, delay_cost=1)
	S += c_qinv_denom_inv_bb >= 110
	c_qinv_denom_inv_bb += MM[0]

	c_qinv_denom_inv_aa = S.Task('c_qinv_denom_inv_aa', length=7, delay_cost=1)
	S += c_qinv_denom_inv_aa >= 111
	c_qinv_denom_inv_aa += MM[0]

	c_qinv_denom_inv_denom_mem0 = S.Task('c_qinv_denom_inv_denom_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv_denom_mem0 >= 117
	c_qinv_denom_inv_denom_mem0 += MM_MEM[0]

	c_qinv_denom_inv_denom_mem1 = S.Task('c_qinv_denom_inv_denom_mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv_denom_mem1 >= 117
	c_qinv_denom_inv_denom_mem1 += MM_MEM[1]

	c_qinv_denom_inv_denom = S.Task('c_qinv_denom_inv_denom', length=2, delay_cost=1)
	S += c_qinv_denom_inv_denom >= 118
	c_qinv_denom_inv_denom += MAS[0]

	c_qinv_denom_inv_denom_w = S.Task('c_qinv_denom_inv_denom_w', length=1, delay_cost=1)
	S += c_qinv_denom_inv_denom_w >= 120
	c_qinv_denom_inv_denom_w += MAIN_MEM_w


	# new tasks
	c_q01 = S.Task('c_q01', length=2, delay_cost=1)
	c_q01 += alt(MAS)

	S += c_q01<95

	c_q01_mem0 = S.Task('c_q01_mem0', length=1, delay_cost=1)
	c_q01_mem0 += MAS_MEM[2]
	S += 91 < c_q01_mem0
	S += c_q01_mem0 <= c_q01

	c_q01_mem1 = S.Task('c_q01_mem1', length=1, delay_cost=1)
	c_q01_mem1 += MAS_MEM[3]
	S += 82 < c_q01_mem1
	S += c_q01_mem1 <= c_q01

	c_qinv_aa_t1_in = S.Task('c_qinv_aa_t1_in', length=1, delay_cost=1)
	c_qinv_aa_t1_in += alt(MM_in)
	c_qinv_aa_t1 = S.Task('c_qinv_aa_t1', length=7, delay_cost=1)
	c_qinv_aa_t1 += alt(MM)
	S += c_qinv_aa_t1>=c_qinv_aa_t1_in

	S += c_qinv_aa_t1<102

	c_qinv_aa_t1_mem0 = S.Task('c_qinv_aa_t1_mem0', length=1, delay_cost=1)
	c_qinv_aa_t1_mem0 += alt(MAS_MEM)
	S += (c_q01*MAS[0])-1 < c_qinv_aa_t1_mem0*MAS_MEM[0]
	S += (c_q01*MAS[1])-1 < c_qinv_aa_t1_mem0*MAS_MEM[2]
	S += (c_q01*MAS[2])-1 < c_qinv_aa_t1_mem0*MAS_MEM[4]
	S += (c_q01*MAS[3])-1 < c_qinv_aa_t1_mem0*MAS_MEM[6]
	S += c_qinv_aa_t1_mem0 <= c_qinv_aa_t1

	c_qinv_aa_t2 = S.Task('c_qinv_aa_t2', length=2, delay_cost=1)
	c_qinv_aa_t2 += alt(MAS)

	S += c_qinv_aa_t2<98

	c_qinv_aa_t2_mem0 = S.Task('c_qinv_aa_t2_mem0', length=1, delay_cost=1)
	c_qinv_aa_t2_mem0 += MAS_MEM[4]
	S += 93 < c_qinv_aa_t2_mem0
	S += c_qinv_aa_t2_mem0 <= c_qinv_aa_t2

	c_qinv_aa_t2_mem1 = S.Task('c_qinv_aa_t2_mem1', length=1, delay_cost=1)
	c_qinv_aa_t2_mem1 += alt(MAS_MEM)
	S += (c_q01*MAS[0])-1 < c_qinv_aa_t2_mem1*MAS_MEM[1]
	S += (c_q01*MAS[1])-1 < c_qinv_aa_t2_mem1*MAS_MEM[3]
	S += (c_q01*MAS[2])-1 < c_qinv_aa_t2_mem1*MAS_MEM[5]
	S += (c_q01*MAS[3])-1 < c_qinv_aa_t2_mem1*MAS_MEM[7]
	S += c_qinv_aa_t2_mem1 <= c_qinv_aa_t2

	c_qinv_aa_t3 = S.Task('c_qinv_aa_t3', length=2, delay_cost=1)
	c_qinv_aa_t3 += alt(MAS)

	S += c_qinv_aa_t3<98

	c_qinv_aa_t3_mem0 = S.Task('c_qinv_aa_t3_mem0', length=1, delay_cost=1)
	c_qinv_aa_t3_mem0 += MAS_MEM[4]
	S += 93 < c_qinv_aa_t3_mem0
	S += c_qinv_aa_t3_mem0 <= c_qinv_aa_t3

	c_qinv_aa_t3_mem1 = S.Task('c_qinv_aa_t3_mem1', length=1, delay_cost=1)
	c_qinv_aa_t3_mem1 += alt(MAS_MEM)
	S += (c_q01*MAS[0])-1 < c_qinv_aa_t3_mem1*MAS_MEM[1]
	S += (c_q01*MAS[1])-1 < c_qinv_aa_t3_mem1*MAS_MEM[3]
	S += (c_q01*MAS[2])-1 < c_qinv_aa_t3_mem1*MAS_MEM[5]
	S += (c_q01*MAS[3])-1 < c_qinv_aa_t3_mem1*MAS_MEM[7]
	S += c_qinv_aa_t3_mem1 <= c_qinv_aa_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM1_stage2MAS4/FP12_INV_BEFORE_FPINV/schedule10.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

