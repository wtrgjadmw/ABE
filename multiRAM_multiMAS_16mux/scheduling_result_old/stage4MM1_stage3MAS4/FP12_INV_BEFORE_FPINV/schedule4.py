from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 168
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 0
	c_aa_a1_0_in += MAS_in[0]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 0
	c_aa_a1_1_in += MAS_in[2]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 0
	c_aa_t10_in += MAS_in[3]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 0
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 0
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 0
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 0
	c_bb_t3_t2_in += MAS_in[1]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=3, delay_cost=1)
	S += c_aa_a1_0 >= 1
	c_aa_a1_0 += MAS[0]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=3, delay_cost=1)
	S += c_aa_a1_1 >= 1
	c_aa_a1_1 += MAS[2]

	c_aa_t10 = S.Task('c_aa_t10', length=3, delay_cost=1)
	S += c_aa_t10 >= 1
	c_aa_t10 += MAS[3]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 1
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 1
	c_aa_t11_in += MAS_in[3]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 1
	c_ab_t0_t2_in += MAS_in[2]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=4, delay_cost=1)
	S += c_ab_t1_t1 >= 1
	c_ab_t1_t1 += MM[0]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 1
	c_bb_t10_in += MAS_in[0]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=3, delay_cost=1)
	S += c_bb_t3_t2 >= 1
	c_bb_t3_t2 += MAS[1]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 1
	c_cc_a1_1_in += MAS_in[1]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 1
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 1
	c_cc_t3_t1_in += MM_in[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 2
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_t11 = S.Task('c_aa_t11', length=3, delay_cost=1)
	S += c_aa_t11 >= 2
	c_aa_t11 += MAS[3]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 2
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 2
	c_aa_t3_t2_in += MAS_in[1]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=3, delay_cost=1)
	S += c_ab_t0_t2 >= 2
	c_ab_t0_t2 += MAS[2]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 2
	c_bb_a1_0_in += MAS_in[3]

	c_bb_t10 = S.Task('c_bb_t10', length=3, delay_cost=1)
	S += c_bb_t10 >= 2
	c_bb_t10 += MAS[0]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 2
	c_bb_t11_in += MAS_in[0]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=3, delay_cost=1)
	S += c_cc_a1_1 >= 2
	c_cc_a1_1 += MAS[1]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 2
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=4, delay_cost=1)
	S += c_cc_t3_t1 >= 2
	c_cc_t3_t1 += MM[0]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 2
	c_cc_t3_t2_in += MAS_in[2]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=3, delay_cost=1)
	S += c_aa_t3_t2 >= 3
	c_aa_t3_t2 += MAS[1]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 3
	c_aa_t3_t3_in += MAS_in[2]

	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 3
	c_ab_t0_t3_in += MAS_in[3]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=3, delay_cost=1)
	S += c_bb_a1_0 >= 3
	c_bb_a1_0 += MAS[3]

	c_bb_t11 = S.Task('c_bb_t11', length=3, delay_cost=1)
	S += c_bb_t11 >= 3
	c_bb_t11 += MAS[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 3
	c_bb_t3_t0_in += MM_in[0]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 3
	c_cc_t11_in += MAS_in[0]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=4, delay_cost=1)
	S += c_cc_t3_t0 >= 3
	c_cc_t3_t0 += MM[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 3
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=3, delay_cost=1)
	S += c_cc_t3_t2 >= 3
	c_cc_t3_t2 += MAS[2]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 3
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 3
	c_cc_t3_t3_in += MAS_in[1]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=3, delay_cost=1)
	S += c_aa_t3_t3 >= 4
	c_aa_t3_t3 += MAS[2]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=3, delay_cost=1)
	S += c_ab_t0_t3 >= 4
	c_ab_t0_t3 += MAS[3]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 4
	c_bb_a1_1_in += MAS_in[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=4, delay_cost=1)
	S += c_bb_t3_t0 >= 4
	c_bb_t3_t0 += MM[0]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 4
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 4
	c_bb_t3_t3_in += MAS_in[0]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 4
	c_cc_a1_0_in += MAS_in[3]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 4
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 4
	c_cc_t10_in += MAS_in[2]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 4
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=3, delay_cost=1)
	S += c_cc_t11 >= 4
	c_cc_t11 += MAS[0]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=3, delay_cost=1)
	S += c_cc_t3_t3 >= 4
	c_cc_t3_t3 += MAS[1]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 5
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 5
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 5
	c_ab_t1_t3_in += MAS_in[0]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 5
	c_ac_t30_in += MAS_in[3]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=3, delay_cost=1)
	S += c_bb_a1_1 >= 5
	c_bb_a1_1 += MAS[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=4, delay_cost=1)
	S += c_bb_t3_t1 >= 5
	c_bb_t3_t1 += MM[0]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=3, delay_cost=1)
	S += c_bb_t3_t3 >= 5
	c_bb_t3_t3 += MAS[0]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 5
	c_bc_t0_t2_in += MAS_in[1]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 5
	c_bc_t31_in += MAS_in[2]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=3, delay_cost=1)
	S += c_cc_a1_0 >= 5
	c_cc_a1_0 += MAS[3]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 5
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=3, delay_cost=1)
	S += c_cc_t10 >= 5
	c_cc_t10 += MAS[2]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=4, delay_cost=1)
	S += c_aa_t3_t1 >= 6
	c_aa_t3_t1 += MM[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 6
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 6
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 6
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=3, delay_cost=1)
	S += c_ab_t1_t3 >= 6
	c_ab_t1_t3 += MAS[0]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 6
	c_ac_t0_t3_in += MAS_in[3]

	c_ac_t30 = S.Task('c_ac_t30', length=3, delay_cost=1)
	S += c_ac_t30 >= 6
	c_ac_t30 += MAS[3]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 6
	c_ac_t31_in += MAS_in[1]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=3, delay_cost=1)
	S += c_bc_t0_t2 >= 6
	c_bc_t0_t2 += MAS[1]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 6
	c_bc_t0_t3_in += MAS_in[2]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 6
	c_bc_t21_in += MAS_in[0]

	c_bc_t31 = S.Task('c_bc_t31', length=3, delay_cost=1)
	S += c_bc_t31 >= 6
	c_bc_t31 += MAS[2]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=4, delay_cost=1)
	S += c_ab_t0_t0 >= 7
	c_ab_t0_t0 += MM[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 7
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 7
	c_ab_t20_in += MAS_in[1]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 7
	c_ac_t0_t2_in += MAS_in[2]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=3, delay_cost=1)
	S += c_ac_t0_t3 >= 7
	c_ac_t0_t3 += MAS[3]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 7
	c_ac_t1_t3_in += MAS_in[3]

	c_ac_t31 = S.Task('c_ac_t31', length=3, delay_cost=1)
	S += c_ac_t31 >= 7
	c_ac_t31 += MAS[1]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 7
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 7
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=3, delay_cost=1)
	S += c_bc_t0_t3 >= 7
	c_bc_t0_t3 += MAS[2]

	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	S += c_bc_t1_t2_in >= 7
	c_bc_t1_t2_in += MAS_in[0]

	c_bc_t21 = S.Task('c_bc_t21', length=3, delay_cost=1)
	S += c_bc_t21 >= 7
	c_bc_t21 += MAS[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 8
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=4, delay_cost=1)
	S += c_ab_t1_t0 >= 8
	c_ab_t1_t0 += MM[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 8
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 8
	c_ab_t1_t2_in += MAS_in[0]

	c_ab_t20 = S.Task('c_ab_t20', length=3, delay_cost=1)
	S += c_ab_t20 >= 8
	c_ab_t20 += MAS[1]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 8
	c_ab_t30_in += MAS_in[2]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=3, delay_cost=1)
	S += c_ac_t0_t2 >= 8
	c_ac_t0_t2 += MAS[2]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=3, delay_cost=1)
	S += c_ac_t1_t3 >= 8
	c_ac_t1_t3 += MAS[3]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 8
	c_ac_t20_in += MAS_in[1]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 8
	c_ac_t21_in += MAS_in[3]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 8
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=3, delay_cost=1)
	S += c_bc_t1_t2 >= 8
	c_bc_t1_t2 += MAS[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 9
	c_aa_t3_t0_in += MM_in[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=4, delay_cost=1)
	S += c_ab_t0_t1 >= 9
	c_ab_t0_t1 += MM[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=3, delay_cost=1)
	S += c_ab_t1_t2 >= 9
	c_ab_t1_t2 += MAS[0]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 9
	c_ab_t21_in += MAS_in[1]

	c_ab_t30 = S.Task('c_ab_t30', length=3, delay_cost=1)
	S += c_ab_t30 >= 9
	c_ab_t30 += MAS[2]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 9
	c_ac_t1_t2_in += MAS_in[0]

	c_ac_t20 = S.Task('c_ac_t20', length=3, delay_cost=1)
	S += c_ac_t20 >= 9
	c_ac_t20 += MAS[1]

	c_ac_t21 = S.Task('c_ac_t21', length=3, delay_cost=1)
	S += c_ac_t21 >= 9
	c_ac_t21 += MAS[3]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 9
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 9
	c_bc_t20_in += MAS_in[3]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 9
	c_bc_t30_in += MAS_in[2]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 9
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=4, delay_cost=1)
	S += c_aa_t3_t0 >= 10
	c_aa_t3_t0 += MM[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 10
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t21 = S.Task('c_ab_t21', length=3, delay_cost=1)
	S += c_ab_t21 >= 10
	c_ab_t21 += MAS[1]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 10
	c_ab_t31_in += MAS_in[1]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 10
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=3, delay_cost=1)
	S += c_ac_t1_t2 >= 10
	c_ac_t1_t2 += MAS[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 10
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 10
	c_bc_t1_t3_in += MAS_in[0]

	c_bc_t20 = S.Task('c_bc_t20', length=3, delay_cost=1)
	S += c_bc_t20 >= 10
	c_bc_t20 += MAS[3]

	c_bc_t30 = S.Task('c_bc_t30', length=3, delay_cost=1)
	S += c_bc_t30 >= 10
	c_bc_t30 += MAS[2]

	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	S += c_pbc_t0_t3_in >= 10
	c_pbc_t0_t3_in += MAS_in[2]

	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	S += c_pbc_t30_in >= 10
	c_pbc_t30_in += MAS_in[3]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 11
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t31 = S.Task('c_ab_t31', length=3, delay_cost=1)
	S += c_ab_t31 >= 11
	c_ab_t31 += MAS[1]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=4, delay_cost=1)
	S += c_ac_t1_t0 >= 11
	c_ac_t1_t0 += MM[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 11
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 11
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=3, delay_cost=1)
	S += c_bc_t1_t3 >= 11
	c_bc_t1_t3 += MAS[0]

	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	S += c_paa_t31_in >= 11
	c_paa_t31_in += MAS_in[0]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=3, delay_cost=1)
	S += c_pbc_t0_t3 >= 11
	c_pbc_t0_t3 += MAS[2]

	c_pbc_t30 = S.Task('c_pbc_t30', length=3, delay_cost=1)
	S += c_pbc_t30 >= 11
	c_pbc_t30 += MAS[3]

	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	S += c_pbc_t31_in >= 11
	c_pbc_t31_in += MAS_in[3]

	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	S += c_pcb_t1_t3_in >= 11
	c_pcb_t1_t3_in += MAS_in[1]

	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	S += c_pcb_t30_in >= 11
	c_pcb_t30_in += MAS_in[2]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 12
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 12
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=4, delay_cost=1)
	S += c_bc_t1_t0 >= 12
	c_bc_t1_t0 += MM[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 12
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	S += c_paa_t1_t3_in >= 12
	c_paa_t1_t3_in += MAS_in[0]

	c_paa_t31 = S.Task('c_paa_t31', length=3, delay_cost=1)
	S += c_paa_t31 >= 12
	c_paa_t31 += MAS[0]

	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	S += c_pbc_t1_t3_in >= 12
	c_pbc_t1_t3_in += MAS_in[1]

	c_pbc_t31 = S.Task('c_pbc_t31', length=3, delay_cost=1)
	S += c_pbc_t31 >= 12
	c_pbc_t31 += MAS[3]

	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	S += c_pcb_t0_t3_in >= 12
	c_pcb_t0_t3_in += MAS_in[3]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=3, delay_cost=1)
	S += c_pcb_t1_t3 >= 12
	c_pcb_t1_t3 += MAS[1]

	c_pcb_t30 = S.Task('c_pcb_t30', length=3, delay_cost=1)
	S += c_pcb_t30 >= 12
	c_pcb_t30 += MAS[2]

	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	S += c_pcb_t31_in >= 12
	c_pcb_t31_in += MAS_in[2]

	c_ab_t00_in = S.Task('c_ab_t00_in', length=1, delay_cost=1)
	S += c_ab_t00_in >= 13
	c_ab_t00_in += MAS_in[2]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 13
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 13
	c_ab_t00_mem1 += MM_MEM[1]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 13
	c_ac_t0_t1_in += MM_in[0]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 13
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=4, delay_cost=1)
	S += c_bc_t0_t1 >= 13
	c_bc_t0_t1 += MM[0]

	c_cc_t2_t3_in = S.Task('c_cc_t2_t3_in', length=1, delay_cost=1)
	S += c_cc_t2_t3_in >= 13
	c_cc_t2_t3_in += MAS_in[3]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 13
	c_cc_t2_t3_mem0 += MAS_MEM[4]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 13
	c_cc_t2_t3_mem1 += MAS_MEM[1]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 13
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	S += c_paa_t0_t3_in >= 13
	c_paa_t0_t3_in += MAS_in[0]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=3, delay_cost=1)
	S += c_paa_t1_t3 >= 13
	c_paa_t1_t3 += MAS[0]

	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	S += c_paa_t30_in >= 13
	c_paa_t30_in += MAS_in[1]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=3, delay_cost=1)
	S += c_pbc_t1_t3 >= 13
	c_pbc_t1_t3 += MAS[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=3, delay_cost=1)
	S += c_pcb_t0_t3 >= 13
	c_pcb_t0_t3 += MAS[3]

	c_pcb_t31 = S.Task('c_pcb_t31', length=3, delay_cost=1)
	S += c_pcb_t31 >= 13
	c_pcb_t31 += MAS[2]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 14
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t5_in = S.Task('c_aa_t3_t5_in', length=1, delay_cost=1)
	S += c_aa_t3_t5_in >= 14
	c_aa_t3_t5_in += MAS_in[3]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 14
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 14
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ab_t00 = S.Task('c_ab_t00', length=3, delay_cost=1)
	S += c_ab_t00 >= 14
	c_ab_t00 += MAS[2]

	c_ab_t4_t3_in = S.Task('c_ab_t4_t3_in', length=1, delay_cost=1)
	S += c_ab_t4_t3_in >= 14
	c_ab_t4_t3_in += MAS_in[0]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 14
	c_ab_t4_t3_mem0 += MAS_MEM[4]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 14
	c_ab_t4_t3_mem1 += MAS_MEM[3]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=4, delay_cost=1)
	S += c_ac_t0_t1 >= 14
	c_ac_t0_t1 += MM[0]

	c_bb_t2_t3_in = S.Task('c_bb_t2_t3_in', length=1, delay_cost=1)
	S += c_bb_t2_t3_in >= 14
	c_bb_t2_t3_in += MAS_in[1]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 14
	c_bb_t2_t3_mem0 += MAS_MEM[0]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 14
	c_bb_t2_t3_mem1 += MAS_MEM[1]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 14
	c_bc_t0_t0_in += MM_in[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 14
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=3, delay_cost=1)
	S += c_cc_t2_t3 >= 14
	c_cc_t2_t3 += MAS[3]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=3, delay_cost=1)
	S += c_paa_t0_t3 >= 14
	c_paa_t0_t3 += MAS[0]

	c_paa_t30 = S.Task('c_paa_t30', length=3, delay_cost=1)
	S += c_paa_t30 >= 14
	c_paa_t30 += MAS[1]

	c_pbc_t4_t3_in = S.Task('c_pbc_t4_t3_in', length=1, delay_cost=1)
	S += c_pbc_t4_t3_in >= 14
	c_pbc_t4_t3_in += MAS_in[2]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 14
	c_pbc_t4_t3_mem0 += MAS_MEM[6]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 14
	c_pbc_t4_t3_mem1 += MAS_MEM[7]

	c_aa_t2_t3_in = S.Task('c_aa_t2_t3_in', length=1, delay_cost=1)
	S += c_aa_t2_t3_in >= 15
	c_aa_t2_t3_in += MAS_in[3]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 15
	c_aa_t2_t3_mem0 += MAS_MEM[6]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 15
	c_aa_t2_t3_mem1 += MAS_MEM[7]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=3, delay_cost=1)
	S += c_aa_t3_t5 >= 15
	c_aa_t3_t5 += MAS[3]

	c_ab_t0_t5_in = S.Task('c_ab_t0_t5_in', length=1, delay_cost=1)
	S += c_ab_t0_t5_in >= 15
	c_ab_t0_t5_in += MAS_in[2]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 15
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 15
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ab_t4_t2_in = S.Task('c_ab_t4_t2_in', length=1, delay_cost=1)
	S += c_ab_t4_t2_in >= 15
	c_ab_t4_t2_in += MAS_in[0]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 15
	c_ab_t4_t2_mem0 += MAS_MEM[2]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 15
	c_ab_t4_t2_mem1 += MAS_MEM[3]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=3, delay_cost=1)
	S += c_ab_t4_t3 >= 15
	c_ab_t4_t3 += MAS[0]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=3, delay_cost=1)
	S += c_bb_t2_t3 >= 15
	c_bb_t2_t3 += MAS[1]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=4, delay_cost=1)
	S += c_bc_t0_t0 >= 15
	c_bc_t0_t0 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 15
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t4_t3_in = S.Task('c_bc_t4_t3_in', length=1, delay_cost=1)
	S += c_bc_t4_t3_in >= 15
	c_bc_t4_t3_in += MAS_in[1]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 15
	c_bc_t4_t3_mem0 += MAS_MEM[4]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 15
	c_bc_t4_t3_mem1 += MAS_MEM[5]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 15
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 15
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=3, delay_cost=1)
	S += c_pbc_t4_t3 >= 15
	c_pbc_t4_t3 += MAS[2]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 16
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=3, delay_cost=1)
	S += c_aa_t2_t3 >= 16
	c_aa_t2_t3 += MAS[3]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 16
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=3, delay_cost=1)
	S += c_ab_t0_t5 >= 16
	c_ab_t0_t5 += MAS[2]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=3, delay_cost=1)
	S += c_ab_t4_t2 >= 16
	c_ab_t4_t2 += MAS[0]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 16
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t4_t2_in = S.Task('c_ac_t4_t2_in', length=1, delay_cost=1)
	S += c_ac_t4_t2_in >= 16
	c_ac_t4_t2_in += MAS_in[3]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 16
	c_ac_t4_t2_mem0 += MAS_MEM[2]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 16
	c_ac_t4_t2_mem1 += MAS_MEM[7]

	c_ac_t4_t3_in = S.Task('c_ac_t4_t3_in', length=1, delay_cost=1)
	S += c_ac_t4_t3_in >= 16
	c_ac_t4_t3_in += MAS_in[2]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 16
	c_ac_t4_t3_mem0 += MAS_MEM[6]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 16
	c_ac_t4_t3_mem1 += MAS_MEM[3]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=4, delay_cost=1)
	S += c_bc_t1_t1 >= 16
	c_bc_t1_t1 += MM[0]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=3, delay_cost=1)
	S += c_bc_t4_t3 >= 16
	c_bc_t4_t3 += MAS[1]

	c_cc_t3_t5_in = S.Task('c_cc_t3_t5_in', length=1, delay_cost=1)
	S += c_cc_t3_t5_in >= 16
	c_cc_t3_t5_in += MAS_in[0]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 16
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 16
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_pcb_t4_t3_in = S.Task('c_pcb_t4_t3_in', length=1, delay_cost=1)
	S += c_pcb_t4_t3_in >= 16
	c_pcb_t4_t3_in += MAS_in[1]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 16
	c_pcb_t4_t3_mem0 += MAS_MEM[4]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 16
	c_pcb_t4_t3_mem1 += MAS_MEM[5]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 17
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_t01_in = S.Task('c_aa_t01_in', length=1, delay_cost=1)
	S += c_aa_t01_in >= 17
	c_aa_t01_in += MAS_in[0]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 17
	c_aa_t01_mem1 += MAS_MEM[5]

	c_aa_t30_in = S.Task('c_aa_t30_in', length=1, delay_cost=1)
	S += c_aa_t30_in >= 17
	c_aa_t30_in += MAS_in[2]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 17
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 17
	c_aa_t30_mem1 += MM_MEM[1]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 17
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=4, delay_cost=1)
	S += c_ac_t0_t0 >= 17
	c_ac_t0_t0 += MM[0]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 17
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=3, delay_cost=1)
	S += c_ac_t4_t2 >= 17
	c_ac_t4_t2 += MAS[3]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=3, delay_cost=1)
	S += c_ac_t4_t3 >= 17
	c_ac_t4_t3 += MAS[2]

	c_bc_t4_t2_in = S.Task('c_bc_t4_t2_in', length=1, delay_cost=1)
	S += c_bc_t4_t2_in >= 17
	c_bc_t4_t2_in += MAS_in[1]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 17
	c_bc_t4_t2_mem0 += MAS_MEM[6]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 17
	c_bc_t4_t2_mem1 += MAS_MEM[1]

	c_cc_t00_in = S.Task('c_cc_t00_in', length=1, delay_cost=1)
	S += c_cc_t00_in >= 17
	c_cc_t00_in += MAS_in[3]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 17
	c_cc_t00_mem1 += MAS_MEM[7]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=3, delay_cost=1)
	S += c_cc_t3_t5 >= 17
	c_cc_t3_t5 += MAS[0]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=3, delay_cost=1)
	S += c_pcb_t4_t3 >= 17
	c_pcb_t4_t3 += MAS[1]

	c_aa_t00_in = S.Task('c_aa_t00_in', length=1, delay_cost=1)
	S += c_aa_t00_in >= 18
	c_aa_t00_in += MAS_in[1]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 18
	c_aa_t00_mem1 += MAS_MEM[1]

	c_aa_t01 = S.Task('c_aa_t01', length=3, delay_cost=1)
	S += c_aa_t01 >= 18
	c_aa_t01 += MAS[0]

	c_aa_t30 = S.Task('c_aa_t30', length=3, delay_cost=1)
	S += c_aa_t30 >= 18
	c_aa_t30 += MAS[2]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 18
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t10_in = S.Task('c_ab_t10_in', length=1, delay_cost=1)
	S += c_ab_t10_in >= 18
	c_ab_t10_in += MAS_in[2]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 18
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 18
	c_ab_t10_mem1 += MM_MEM[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=4, delay_cost=1)
	S += c_ac_t1_t1 >= 18
	c_ac_t1_t1 += MM[0]

	c_bb_t00_in = S.Task('c_bb_t00_in', length=1, delay_cost=1)
	S += c_bb_t00_in >= 18
	c_bb_t00_in += MAS_in[3]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 18
	c_bb_t00_mem1 += MAS_MEM[7]

	c_bb_t01_in = S.Task('c_bb_t01_in', length=1, delay_cost=1)
	S += c_bb_t01_in >= 18
	c_bb_t01_in += MAS_in[0]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 18
	c_bb_t01_mem1 += MAS_MEM[3]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 18
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 18
	c_bc_t4_t0_mem0 += MAS_MEM[6]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 18
	c_bc_t4_t0_mem1 += MAS_MEM[5]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=3, delay_cost=1)
	S += c_bc_t4_t2 >= 18
	c_bc_t4_t2 += MAS[1]

	c_cc_t00 = S.Task('c_cc_t00', length=3, delay_cost=1)
	S += c_cc_t00 >= 18
	c_cc_t00 += MAS[3]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 18
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t00 = S.Task('c_aa_t00', length=3, delay_cost=1)
	S += c_aa_t00 >= 19
	c_aa_t00 += MAS[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 19
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t10 = S.Task('c_ab_t10', length=3, delay_cost=1)
	S += c_ab_t10 >= 19
	c_ab_t10 += MAS[2]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 19
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 19
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 19
	c_ac_t4_t0_mem0 += MAS_MEM[2]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 19
	c_ac_t4_t0_mem1 += MAS_MEM[7]

	c_bb_t00 = S.Task('c_bb_t00', length=3, delay_cost=1)
	S += c_bb_t00 >= 19
	c_bb_t00 += MAS[3]

	c_bb_t01 = S.Task('c_bb_t01', length=3, delay_cost=1)
	S += c_bb_t01 >= 19
	c_bb_t01 += MAS[0]

	c_bb_t3_t5_in = S.Task('c_bb_t3_t5_in', length=1, delay_cost=1)
	S += c_bb_t3_t5_in >= 19
	c_bb_t3_t5_in += MAS_in[2]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 19
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 19
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=4, delay_cost=1)
	S += c_bc_t4_t0 >= 19
	c_bc_t4_t0 += MM[0]

	c_cc_t01_in = S.Task('c_cc_t01_in', length=1, delay_cost=1)
	S += c_cc_t01_in >= 19
	c_cc_t01_in += MAS_in[3]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 19
	c_cc_t01_mem1 += MAS_MEM[3]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 20
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 20
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 20
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 20
	c_ab_t0_t4_mem0 += MAS_MEM[4]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 20
	c_ab_t0_t4_mem1 += MAS_MEM[7]

	c_ac_t00_in = S.Task('c_ac_t00_in', length=1, delay_cost=1)
	S += c_ac_t00_in >= 20
	c_ac_t00_in += MAS_in[3]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 20
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 20
	c_ac_t00_mem1 += MM_MEM[1]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=4, delay_cost=1)
	S += c_ac_t4_t0 >= 20
	c_ac_t4_t0 += MM[0]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=3, delay_cost=1)
	S += c_bb_t3_t5 >= 20
	c_bb_t3_t5 += MAS[2]

	c_cc_t01 = S.Task('c_cc_t01', length=3, delay_cost=1)
	S += c_cc_t01 >= 20
	c_cc_t01 += MAS[3]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 21
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=4, delay_cost=1)
	S += c_ab_t0_t4 >= 21
	c_ab_t0_t4 += MM[0]

	c_ab_t1_t5_in = S.Task('c_ab_t1_t5_in', length=1, delay_cost=1)
	S += c_ab_t1_t5_in >= 21
	c_ab_t1_t5_in += MAS_in[3]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 21
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 21
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_ac_t00 = S.Task('c_ac_t00', length=3, delay_cost=1)
	S += c_ac_t00 >= 21
	c_ac_t00 += MAS[3]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 21
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 21
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 21
	c_bc_t4_t1_mem0 += MAS_MEM[0]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 21
	c_bc_t4_t1_mem1 += MAS_MEM[5]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=3, delay_cost=1)
	S += c_ab_t1_t5 >= 22
	c_ab_t1_t5 += MAS[3]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 22
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 22
	c_ab_t4_t0_mem0 += MAS_MEM[2]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 22
	c_ab_t4_t0_mem1 += MAS_MEM[5]

	c_ac_t10_in = S.Task('c_ac_t10_in', length=1, delay_cost=1)
	S += c_ac_t10_in >= 22
	c_ac_t10_in += MAS_in[0]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 22
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 22
	c_ac_t10_mem1 += MM_MEM[1]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 22
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=4, delay_cost=1)
	S += c_bc_t4_t1 >= 22
	c_bc_t4_t1 += MM[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 22
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=4, delay_cost=1)
	S += c_ab_t4_t0 >= 23
	c_ab_t4_t0 += MM[0]

	c_ac_t0_t5_in = S.Task('c_ac_t0_t5_in', length=1, delay_cost=1)
	S += c_ac_t0_t5_in >= 23
	c_ac_t0_t5_in += MAS_in[0]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 23
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 23
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_ac_t10 = S.Task('c_ac_t10', length=3, delay_cost=1)
	S += c_ac_t10 >= 23
	c_ac_t10 += MAS[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 23
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 23
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 23
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 23
	c_bb_t3_t4_mem0 += MAS_MEM[2]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 23
	c_bb_t3_t4_mem1 += MAS_MEM[1]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 24
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 24
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 24
	c_ac_t0_t4_mem0 += MAS_MEM[4]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 24
	c_ac_t0_t4_mem1 += MAS_MEM[7]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=3, delay_cost=1)
	S += c_ac_t0_t5 >= 24
	c_ac_t0_t5 += MAS[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 24
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=4, delay_cost=1)
	S += c_bb_t3_t4 >= 24
	c_bb_t3_t4 += MM[0]

	c_cc_t30_in = S.Task('c_cc_t30_in', length=1, delay_cost=1)
	S += c_cc_t30_in >= 24
	c_cc_t30_in += MAS_in[0]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 24
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 24
	c_cc_t30_mem1 += MM_MEM[1]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 25
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 25
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 25
	c_ab_t4_t1_mem0 += MAS_MEM[2]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 25
	c_ab_t4_t1_mem1 += MAS_MEM[3]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=4, delay_cost=1)
	S += c_ac_t0_t4 >= 25
	c_ac_t0_t4 += MM[0]

	c_ac_t1_t5_in = S.Task('c_ac_t1_t5_in', length=1, delay_cost=1)
	S += c_ac_t1_t5_in >= 25
	c_ac_t1_t5_in += MAS_in[3]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 25
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 25
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_cc_t30 = S.Task('c_cc_t30', length=3, delay_cost=1)
	S += c_cc_t30 >= 25
	c_cc_t30 += MAS[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 25
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 26
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=4, delay_cost=1)
	S += c_ab_t4_t1 >= 26
	c_ab_t4_t1 += MM[0]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=3, delay_cost=1)
	S += c_ac_t1_t5 >= 26
	c_ac_t1_t5 += MAS[3]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 26
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bc_t10_in = S.Task('c_bc_t10_in', length=1, delay_cost=1)
	S += c_bc_t10_in >= 26
	c_bc_t10_in += MAS_in[3]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 26
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 26
	c_bc_t10_mem1 += MM_MEM[1]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 26
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 26
	c_bc_t1_t4_mem0 += MAS_MEM[0]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 26
	c_bc_t1_t4_mem1 += MAS_MEM[1]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 27
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 27
	c_aa_t3_t4_mem0 += MAS_MEM[2]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 27
	c_aa_t3_t4_mem1 += MAS_MEM[5]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 27
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t30_in = S.Task('c_bb_t30_in', length=1, delay_cost=1)
	S += c_bb_t30_in >= 27
	c_bb_t30_in += MAS_in[1]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 27
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 27
	c_bb_t30_mem1 += MM_MEM[1]

	c_bc_t10 = S.Task('c_bc_t10', length=3, delay_cost=1)
	S += c_bc_t10 >= 27
	c_bc_t10 += MAS[3]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=4, delay_cost=1)
	S += c_bc_t1_t4 >= 27
	c_bc_t1_t4 += MM[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 27
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 28
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=4, delay_cost=1)
	S += c_aa_t3_t4 >= 28
	c_aa_t3_t4 += MM[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 28
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_t30 = S.Task('c_bb_t30', length=3, delay_cost=1)
	S += c_bb_t30 >= 28
	c_bb_t30 += MAS[1]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 28
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 28
	c_bc_t0_t4_mem0 += MAS_MEM[2]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 28
	c_bc_t0_t4_mem1 += MAS_MEM[5]

	c_bc_t1_t5_in = S.Task('c_bc_t1_t5_in', length=1, delay_cost=1)
	S += c_bc_t1_t5_in >= 28
	c_bc_t1_t5_in += MAS_in[1]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 28
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 28
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 29
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 29
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 29
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 29
	c_ac_t4_t1_mem0 += MAS_MEM[6]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 29
	c_ac_t4_t1_mem1 += MAS_MEM[3]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=4, delay_cost=1)
	S += c_bc_t0_t4 >= 29
	c_bc_t0_t4 += MM[0]

	c_bc_t0_t5_in = S.Task('c_bc_t0_t5_in', length=1, delay_cost=1)
	S += c_bc_t0_t5_in >= 29
	c_bc_t0_t5_in += MAS_in[2]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 29
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 29
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=3, delay_cost=1)
	S += c_bc_t1_t5 >= 29
	c_bc_t1_t5 += MAS[1]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 30
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 30
	c_ac_t1_t4_mem0 += MAS_MEM[0]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 30
	c_ac_t1_t4_mem1 += MAS_MEM[7]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=4, delay_cost=1)
	S += c_ac_t4_t1 >= 30
	c_ac_t4_t1 += MM[0]

	c_bc_t00_in = S.Task('c_bc_t00_in', length=1, delay_cost=1)
	S += c_bc_t00_in >= 30
	c_bc_t00_in += MAS_in[2]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 30
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 30
	c_bc_t00_mem1 += MM_MEM[1]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 30
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 30
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=3, delay_cost=1)
	S += c_bc_t0_t5 >= 30
	c_bc_t0_t5 += MAS[2]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 31
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 31
	c_ab_t1_t4_mem0 += MAS_MEM[0]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 31
	c_ab_t1_t4_mem1 += MAS_MEM[1]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 31
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=4, delay_cost=1)
	S += c_ac_t1_t4 >= 31
	c_ac_t1_t4 += MM[0]

	c_bc_t00 = S.Task('c_bc_t00', length=3, delay_cost=1)
	S += c_bc_t00 >= 31
	c_bc_t00 += MAS[2]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 31
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=4, delay_cost=1)
	S += c_ab_t1_t4 >= 32
	c_ab_t1_t4 += MM[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 32
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 32
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 32
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 32
	c_cc_t3_t4_mem0 += MAS_MEM[4]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 32
	c_cc_t3_t4_mem1 += MAS_MEM[3]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 33
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 33
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=4, delay_cost=1)
	S += c_cc_t3_t4 >= 33
	c_cc_t3_t4 += MM[0]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 34
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 34
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 35
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 35
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 36
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 36
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 37
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 37
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 38
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 38
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 39
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 39
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 40
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 40
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 41
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 41
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 42
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 42
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 43
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 43
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 44
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 44
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 45
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 45
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 46
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 46
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 47
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 47
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 48
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 48
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 49
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 49
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 50
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 50
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 51
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 51
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 52
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 52
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 53
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 53
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 54
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 54
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 55
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 55
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 56
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 56
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 57
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 57
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 58
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 58
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 59
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 59
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 60
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 60
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 61
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 61
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 62
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 62
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 63
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 63
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 64
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 64
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 65
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 65
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 66
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 66
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 67
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 67
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 68
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 68
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 69
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 69
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 70
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 70
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 71
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 71
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 72
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 73
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 74
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 75
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 76
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 77
	c_bb_t00_mem0 += MAIN_MEM_r[0]


	# new tasks
	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=3, delay_cost=1)
	c_paa_t4_t3 += alt(MAS)
	c_paa_t4_t3_in = S.Task('c_paa_t4_t3_in', length=1, delay_cost=1)
	c_paa_t4_t3_in += alt(MAS_in)
	S += c_paa_t4_t3_in*MAS_in[0]<=c_paa_t4_t3*MAS[0]

	S += c_paa_t4_t3_in*MAS_in[1]<=c_paa_t4_t3*MAS[1]

	S += c_paa_t4_t3_in*MAS_in[2]<=c_paa_t4_t3*MAS[2]

	S += c_paa_t4_t3_in*MAS_in[3]<=c_paa_t4_t3*MAS[3]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	c_paa_t4_t3_mem0 += MAS_MEM[2]
	S += 16 < c_paa_t4_t3_mem0
	S += c_paa_t4_t3_mem0 <= c_paa_t4_t3

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	c_paa_t4_t3_mem1 += MAS_MEM[1]
	S += 14 < c_paa_t4_t3_mem1
	S += c_paa_t4_t3_mem1 <= c_paa_t4_t3

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=4, delay_cost=1)
	c_aa_t2_t0 += alt(MM)
	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	c_aa_t2_t0_in += alt(MM_in)
	S += c_aa_t2_t0_in*MM_in[0]<=c_aa_t2_t0*MM[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	c_aa_t2_t0_mem0 += MAS_MEM[2]
	S += 21 < c_aa_t2_t0_mem0
	S += c_aa_t2_t0_mem0 <= c_aa_t2_t0

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	c_aa_t2_t0_mem1 += MAS_MEM[7]
	S += 3 < c_aa_t2_t0_mem1
	S += c_aa_t2_t0_mem1 <= c_aa_t2_t0

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=4, delay_cost=1)
	c_aa_t2_t1 += alt(MM)
	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	c_aa_t2_t1_in += alt(MM_in)
	S += c_aa_t2_t1_in*MM_in[0]<=c_aa_t2_t1*MM[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	c_aa_t2_t1_mem0 += MAS_MEM[0]
	S += 20 < c_aa_t2_t1_mem0
	S += c_aa_t2_t1_mem0 <= c_aa_t2_t1

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	c_aa_t2_t1_mem1 += MAS_MEM[7]
	S += 4 < c_aa_t2_t1_mem1
	S += c_aa_t2_t1_mem1 <= c_aa_t2_t1

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=3, delay_cost=1)
	c_aa_t2_t2 += alt(MAS)
	c_aa_t2_t2_in = S.Task('c_aa_t2_t2_in', length=1, delay_cost=1)
	c_aa_t2_t2_in += alt(MAS_in)
	S += c_aa_t2_t2_in*MAS_in[0]<=c_aa_t2_t2*MAS[0]

	S += c_aa_t2_t2_in*MAS_in[1]<=c_aa_t2_t2*MAS[1]

	S += c_aa_t2_t2_in*MAS_in[2]<=c_aa_t2_t2*MAS[2]

	S += c_aa_t2_t2_in*MAS_in[3]<=c_aa_t2_t2*MAS[3]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	c_aa_t2_t2_mem0 += MAS_MEM[2]
	S += 21 < c_aa_t2_t2_mem0
	S += c_aa_t2_t2_mem0 <= c_aa_t2_t2

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	c_aa_t2_t2_mem1 += MAS_MEM[1]
	S += 20 < c_aa_t2_t2_mem1
	S += c_aa_t2_t2_mem1 <= c_aa_t2_t2

	c_aa_t31 = S.Task('c_aa_t31', length=3, delay_cost=1)
	c_aa_t31 += alt(MAS)
	c_aa_t31_in = S.Task('c_aa_t31_in', length=1, delay_cost=1)
	c_aa_t31_in += alt(MAS_in)
	S += c_aa_t31_in*MAS_in[0]<=c_aa_t31*MAS[0]

	S += c_aa_t31_in*MAS_in[1]<=c_aa_t31*MAS[1]

	S += c_aa_t31_in*MAS_in[2]<=c_aa_t31*MAS[2]

	S += c_aa_t31_in*MAS_in[3]<=c_aa_t31*MAS[3]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	c_aa_t31_mem0 += MM_MEM[0]
	S += 31 < c_aa_t31_mem0
	S += c_aa_t31_mem0 <= c_aa_t31

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	c_aa_t31_mem1 += MAS_MEM[7]
	S += 17 < c_aa_t31_mem1
	S += c_aa_t31_mem1 <= c_aa_t31

	c_aa10 = S.Task('c_aa10', length=3, delay_cost=1)
	c_aa10 += alt(MAS)
	c_aa10_in = S.Task('c_aa10_in', length=1, delay_cost=1)
	c_aa10_in += alt(MAS_in)
	S += c_aa10_in*MAS_in[0]<=c_aa10*MAS[0]

	S += c_aa10_in*MAS_in[1]<=c_aa10*MAS[1]

	S += c_aa10_in*MAS_in[2]<=c_aa10*MAS[2]

	S += c_aa10_in*MAS_in[3]<=c_aa10*MAS[3]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	c_aa10_mem0 += MAS_MEM[4]
	S += 20 < c_aa10_mem0
	S += c_aa10_mem0 <= c_aa10

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=4, delay_cost=1)
	c_bb_t2_t0 += alt(MM)
	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	c_bb_t2_t0_in += alt(MM_in)
	S += c_bb_t2_t0_in*MM_in[0]<=c_bb_t2_t0*MM[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	c_bb_t2_t0_mem0 += MAS_MEM[6]
	S += 21 < c_bb_t2_t0_mem0
	S += c_bb_t2_t0_mem0 <= c_bb_t2_t0

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	c_bb_t2_t0_mem1 += MAS_MEM[1]
	S += 4 < c_bb_t2_t0_mem1
	S += c_bb_t2_t0_mem1 <= c_bb_t2_t0

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=4, delay_cost=1)
	c_bb_t2_t1 += alt(MM)
	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	c_bb_t2_t1_in += alt(MM_in)
	S += c_bb_t2_t1_in*MM_in[0]<=c_bb_t2_t1*MM[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	c_bb_t2_t1_mem0 += MAS_MEM[0]
	S += 21 < c_bb_t2_t1_mem0
	S += c_bb_t2_t1_mem0 <= c_bb_t2_t1

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	c_bb_t2_t1_mem1 += MAS_MEM[1]
	S += 5 < c_bb_t2_t1_mem1
	S += c_bb_t2_t1_mem1 <= c_bb_t2_t1

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=3, delay_cost=1)
	c_bb_t2_t2 += alt(MAS)
	c_bb_t2_t2_in = S.Task('c_bb_t2_t2_in', length=1, delay_cost=1)
	c_bb_t2_t2_in += alt(MAS_in)
	S += c_bb_t2_t2_in*MAS_in[0]<=c_bb_t2_t2*MAS[0]

	S += c_bb_t2_t2_in*MAS_in[1]<=c_bb_t2_t2*MAS[1]

	S += c_bb_t2_t2_in*MAS_in[2]<=c_bb_t2_t2*MAS[2]

	S += c_bb_t2_t2_in*MAS_in[3]<=c_bb_t2_t2*MAS[3]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	c_bb_t2_t2_mem0 += MAS_MEM[6]
	S += 21 < c_bb_t2_t2_mem0
	S += c_bb_t2_t2_mem0 <= c_bb_t2_t2

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	c_bb_t2_t2_mem1 += MAS_MEM[1]
	S += 21 < c_bb_t2_t2_mem1
	S += c_bb_t2_t2_mem1 <= c_bb_t2_t2

	c_bb_t31 = S.Task('c_bb_t31', length=3, delay_cost=1)
	c_bb_t31 += alt(MAS)
	c_bb_t31_in = S.Task('c_bb_t31_in', length=1, delay_cost=1)
	c_bb_t31_in += alt(MAS_in)
	S += c_bb_t31_in*MAS_in[0]<=c_bb_t31*MAS[0]

	S += c_bb_t31_in*MAS_in[1]<=c_bb_t31*MAS[1]

	S += c_bb_t31_in*MAS_in[2]<=c_bb_t31*MAS[2]

	S += c_bb_t31_in*MAS_in[3]<=c_bb_t31*MAS[3]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	c_bb_t31_mem0 += MM_MEM[0]
	S += 27 < c_bb_t31_mem0
	S += c_bb_t31_mem0 <= c_bb_t31

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	c_bb_t31_mem1 += MAS_MEM[5]
	S += 22 < c_bb_t31_mem1
	S += c_bb_t31_mem1 <= c_bb_t31

	c_bb10 = S.Task('c_bb10', length=3, delay_cost=1)
	c_bb10 += alt(MAS)
	c_bb10_in = S.Task('c_bb10_in', length=1, delay_cost=1)
	c_bb10_in += alt(MAS_in)
	S += c_bb10_in*MAS_in[0]<=c_bb10*MAS[0]

	S += c_bb10_in*MAS_in[1]<=c_bb10*MAS[1]

	S += c_bb10_in*MAS_in[2]<=c_bb10*MAS[2]

	S += c_bb10_in*MAS_in[3]<=c_bb10*MAS[3]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	c_bb10_mem0 += MAS_MEM[2]
	S += 30 < c_bb10_mem0
	S += c_bb10_mem0 <= c_bb10

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=4, delay_cost=1)
	c_cc_t2_t0 += alt(MM)
	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	c_cc_t2_t0_in += alt(MM_in)
	S += c_cc_t2_t0_in*MM_in[0]<=c_cc_t2_t0*MM[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	c_cc_t2_t0_mem0 += MAS_MEM[6]
	S += 20 < c_cc_t2_t0_mem0
	S += c_cc_t2_t0_mem0 <= c_cc_t2_t0

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	c_cc_t2_t0_mem1 += MAS_MEM[5]
	S += 7 < c_cc_t2_t0_mem1
	S += c_cc_t2_t0_mem1 <= c_cc_t2_t0

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=4, delay_cost=1)
	c_cc_t2_t1 += alt(MM)
	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	c_cc_t2_t1_in += alt(MM_in)
	S += c_cc_t2_t1_in*MM_in[0]<=c_cc_t2_t1*MM[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	c_cc_t2_t1_mem0 += MAS_MEM[6]
	S += 22 < c_cc_t2_t1_mem0
	S += c_cc_t2_t1_mem0 <= c_cc_t2_t1

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	c_cc_t2_t1_mem1 += MAS_MEM[1]
	S += 6 < c_cc_t2_t1_mem1
	S += c_cc_t2_t1_mem1 <= c_cc_t2_t1

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=3, delay_cost=1)
	c_cc_t2_t2 += alt(MAS)
	c_cc_t2_t2_in = S.Task('c_cc_t2_t2_in', length=1, delay_cost=1)
	c_cc_t2_t2_in += alt(MAS_in)
	S += c_cc_t2_t2_in*MAS_in[0]<=c_cc_t2_t2*MAS[0]

	S += c_cc_t2_t2_in*MAS_in[1]<=c_cc_t2_t2*MAS[1]

	S += c_cc_t2_t2_in*MAS_in[2]<=c_cc_t2_t2*MAS[2]

	S += c_cc_t2_t2_in*MAS_in[3]<=c_cc_t2_t2*MAS[3]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	c_cc_t2_t2_mem0 += MAS_MEM[6]
	S += 20 < c_cc_t2_t2_mem0
	S += c_cc_t2_t2_mem0 <= c_cc_t2_t2

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	c_cc_t2_t2_mem1 += MAS_MEM[7]
	S += 22 < c_cc_t2_t2_mem1
	S += c_cc_t2_t2_mem1 <= c_cc_t2_t2

	c_cc_t31 = S.Task('c_cc_t31', length=3, delay_cost=1)
	c_cc_t31 += alt(MAS)
	c_cc_t31_in = S.Task('c_cc_t31_in', length=1, delay_cost=1)
	c_cc_t31_in += alt(MAS_in)
	S += c_cc_t31_in*MAS_in[0]<=c_cc_t31*MAS[0]

	S += c_cc_t31_in*MAS_in[1]<=c_cc_t31*MAS[1]

	S += c_cc_t31_in*MAS_in[2]<=c_cc_t31*MAS[2]

	S += c_cc_t31_in*MAS_in[3]<=c_cc_t31*MAS[3]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	c_cc_t31_mem0 += MM_MEM[0]
	S += 36 < c_cc_t31_mem0
	S += c_cc_t31_mem0 <= c_cc_t31

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	c_cc_t31_mem1 += MAS_MEM[1]
	S += 19 < c_cc_t31_mem1
	S += c_cc_t31_mem1 <= c_cc_t31

	c_cc10 = S.Task('c_cc10', length=3, delay_cost=1)
	c_cc10 += alt(MAS)
	c_cc10_in = S.Task('c_cc10_in', length=1, delay_cost=1)
	c_cc10_in += alt(MAS_in)
	S += c_cc10_in*MAS_in[0]<=c_cc10*MAS[0]

	S += c_cc10_in*MAS_in[1]<=c_cc10*MAS[1]

	S += c_cc10_in*MAS_in[2]<=c_cc10*MAS[2]

	S += c_cc10_in*MAS_in[3]<=c_cc10*MAS[3]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	c_cc10_mem0 += MAS_MEM[0]
	S += 27 < c_cc10_mem0
	S += c_cc10_mem0 <= c_cc10

	c_ab_t01 = S.Task('c_ab_t01', length=3, delay_cost=1)
	c_ab_t01 += alt(MAS)
	c_ab_t01_in = S.Task('c_ab_t01_in', length=1, delay_cost=1)
	c_ab_t01_in += alt(MAS_in)
	S += c_ab_t01_in*MAS_in[0]<=c_ab_t01*MAS[0]

	S += c_ab_t01_in*MAS_in[1]<=c_ab_t01*MAS[1]

	S += c_ab_t01_in*MAS_in[2]<=c_ab_t01*MAS[2]

	S += c_ab_t01_in*MAS_in[3]<=c_ab_t01*MAS[3]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	c_ab_t01_mem0 += MM_MEM[0]
	S += 24 < c_ab_t01_mem0
	S += c_ab_t01_mem0 <= c_ab_t01

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	c_ab_t01_mem1 += MAS_MEM[5]
	S += 18 < c_ab_t01_mem1
	S += c_ab_t01_mem1 <= c_ab_t01

	c_ab_t11 = S.Task('c_ab_t11', length=3, delay_cost=1)
	c_ab_t11 += alt(MAS)
	c_ab_t11_in = S.Task('c_ab_t11_in', length=1, delay_cost=1)
	c_ab_t11_in += alt(MAS_in)
	S += c_ab_t11_in*MAS_in[0]<=c_ab_t11*MAS[0]

	S += c_ab_t11_in*MAS_in[1]<=c_ab_t11*MAS[1]

	S += c_ab_t11_in*MAS_in[2]<=c_ab_t11*MAS[2]

	S += c_ab_t11_in*MAS_in[3]<=c_ab_t11*MAS[3]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	c_ab_t11_mem0 += MM_MEM[0]
	S += 35 < c_ab_t11_mem0
	S += c_ab_t11_mem0 <= c_ab_t11

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	c_ab_t11_mem1 += MAS_MEM[7]
	S += 24 < c_ab_t11_mem1
	S += c_ab_t11_mem1 <= c_ab_t11

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=4, delay_cost=1)
	c_ab_t4_t4 += alt(MM)
	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	c_ab_t4_t4_in += alt(MM_in)
	S += c_ab_t4_t4_in*MM_in[0]<=c_ab_t4_t4*MM[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	c_ab_t4_t4_mem0 += MAS_MEM[0]
	S += 18 < c_ab_t4_t4_mem0
	S += c_ab_t4_t4_mem0 <= c_ab_t4_t4

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	c_ab_t4_t4_mem1 += MAS_MEM[1]
	S += 17 < c_ab_t4_t4_mem1
	S += c_ab_t4_t4_mem1 <= c_ab_t4_t4

	c_ab_t40 = S.Task('c_ab_t40', length=3, delay_cost=1)
	c_ab_t40 += alt(MAS)
	c_ab_t40_in = S.Task('c_ab_t40_in', length=1, delay_cost=1)
	c_ab_t40_in += alt(MAS_in)
	S += c_ab_t40_in*MAS_in[0]<=c_ab_t40*MAS[0]

	S += c_ab_t40_in*MAS_in[1]<=c_ab_t40*MAS[1]

	S += c_ab_t40_in*MAS_in[2]<=c_ab_t40*MAS[2]

	S += c_ab_t40_in*MAS_in[3]<=c_ab_t40*MAS[3]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	c_ab_t40_mem0 += MM_MEM[0]
	S += 26 < c_ab_t40_mem0
	S += c_ab_t40_mem0 <= c_ab_t40

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	c_ab_t40_mem1 += MM_MEM[1]
	S += 29 < c_ab_t40_mem1
	S += c_ab_t40_mem1 <= c_ab_t40

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=3, delay_cost=1)
	c_ab_t4_t5 += alt(MAS)
	c_ab_t4_t5_in = S.Task('c_ab_t4_t5_in', length=1, delay_cost=1)
	c_ab_t4_t5_in += alt(MAS_in)
	S += c_ab_t4_t5_in*MAS_in[0]<=c_ab_t4_t5*MAS[0]

	S += c_ab_t4_t5_in*MAS_in[1]<=c_ab_t4_t5*MAS[1]

	S += c_ab_t4_t5_in*MAS_in[2]<=c_ab_t4_t5*MAS[2]

	S += c_ab_t4_t5_in*MAS_in[3]<=c_ab_t4_t5*MAS[3]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	c_ab_t4_t5_mem0 += MM_MEM[0]
	S += 26 < c_ab_t4_t5_mem0
	S += c_ab_t4_t5_mem0 <= c_ab_t4_t5

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	c_ab_t4_t5_mem1 += MM_MEM[1]
	S += 29 < c_ab_t4_t5_mem1
	S += c_ab_t4_t5_mem1 <= c_ab_t4_t5

	c_ab_t50 = S.Task('c_ab_t50', length=3, delay_cost=1)
	c_ab_t50 += alt(MAS)
	c_ab_t50_in = S.Task('c_ab_t50_in', length=1, delay_cost=1)
	c_ab_t50_in += alt(MAS_in)
	S += c_ab_t50_in*MAS_in[0]<=c_ab_t50*MAS[0]

	S += c_ab_t50_in*MAS_in[1]<=c_ab_t50*MAS[1]

	S += c_ab_t50_in*MAS_in[2]<=c_ab_t50*MAS[2]

	S += c_ab_t50_in*MAS_in[3]<=c_ab_t50*MAS[3]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	c_ab_t50_mem0 += MAS_MEM[4]
	S += 16 < c_ab_t50_mem0
	S += c_ab_t50_mem0 <= c_ab_t50

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	c_ab_t50_mem1 += MAS_MEM[5]
	S += 21 < c_ab_t50_mem1
	S += c_ab_t50_mem1 <= c_ab_t50

	c_bc_t01 = S.Task('c_bc_t01', length=3, delay_cost=1)
	c_bc_t01 += alt(MAS)
	c_bc_t01_in = S.Task('c_bc_t01_in', length=1, delay_cost=1)
	c_bc_t01_in += alt(MAS_in)
	S += c_bc_t01_in*MAS_in[0]<=c_bc_t01*MAS[0]

	S += c_bc_t01_in*MAS_in[1]<=c_bc_t01*MAS[1]

	S += c_bc_t01_in*MAS_in[2]<=c_bc_t01*MAS[2]

	S += c_bc_t01_in*MAS_in[3]<=c_bc_t01*MAS[3]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	c_bc_t01_mem0 += MM_MEM[0]
	S += 32 < c_bc_t01_mem0
	S += c_bc_t01_mem0 <= c_bc_t01

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	c_bc_t01_mem1 += MAS_MEM[5]
	S += 32 < c_bc_t01_mem1
	S += c_bc_t01_mem1 <= c_bc_t01

	c_bc_t11 = S.Task('c_bc_t11', length=3, delay_cost=1)
	c_bc_t11 += alt(MAS)
	c_bc_t11_in = S.Task('c_bc_t11_in', length=1, delay_cost=1)
	c_bc_t11_in += alt(MAS_in)
	S += c_bc_t11_in*MAS_in[0]<=c_bc_t11*MAS[0]

	S += c_bc_t11_in*MAS_in[1]<=c_bc_t11*MAS[1]

	S += c_bc_t11_in*MAS_in[2]<=c_bc_t11*MAS[2]

	S += c_bc_t11_in*MAS_in[3]<=c_bc_t11*MAS[3]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	c_bc_t11_mem0 += MM_MEM[0]
	S += 30 < c_bc_t11_mem0
	S += c_bc_t11_mem0 <= c_bc_t11

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	c_bc_t11_mem1 += MAS_MEM[3]
	S += 31 < c_bc_t11_mem1
	S += c_bc_t11_mem1 <= c_bc_t11

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=4, delay_cost=1)
	c_bc_t4_t4 += alt(MM)
	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	c_bc_t4_t4_in += alt(MM_in)
	S += c_bc_t4_t4_in*MM_in[0]<=c_bc_t4_t4*MM[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	c_bc_t4_t4_mem0 += MAS_MEM[2]
	S += 20 < c_bc_t4_t4_mem0
	S += c_bc_t4_t4_mem0 <= c_bc_t4_t4

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	c_bc_t4_t4_mem1 += MAS_MEM[3]
	S += 18 < c_bc_t4_t4_mem1
	S += c_bc_t4_t4_mem1 <= c_bc_t4_t4

	c_bc_t40 = S.Task('c_bc_t40', length=3, delay_cost=1)
	c_bc_t40 += alt(MAS)
	c_bc_t40_in = S.Task('c_bc_t40_in', length=1, delay_cost=1)
	c_bc_t40_in += alt(MAS_in)
	S += c_bc_t40_in*MAS_in[0]<=c_bc_t40*MAS[0]

	S += c_bc_t40_in*MAS_in[1]<=c_bc_t40*MAS[1]

	S += c_bc_t40_in*MAS_in[2]<=c_bc_t40*MAS[2]

	S += c_bc_t40_in*MAS_in[3]<=c_bc_t40*MAS[3]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	c_bc_t40_mem0 += MM_MEM[0]
	S += 22 < c_bc_t40_mem0
	S += c_bc_t40_mem0 <= c_bc_t40

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	c_bc_t40_mem1 += MM_MEM[1]
	S += 25 < c_bc_t40_mem1
	S += c_bc_t40_mem1 <= c_bc_t40

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=3, delay_cost=1)
	c_bc_t4_t5 += alt(MAS)
	c_bc_t4_t5_in = S.Task('c_bc_t4_t5_in', length=1, delay_cost=1)
	c_bc_t4_t5_in += alt(MAS_in)
	S += c_bc_t4_t5_in*MAS_in[0]<=c_bc_t4_t5*MAS[0]

	S += c_bc_t4_t5_in*MAS_in[1]<=c_bc_t4_t5*MAS[1]

	S += c_bc_t4_t5_in*MAS_in[2]<=c_bc_t4_t5*MAS[2]

	S += c_bc_t4_t5_in*MAS_in[3]<=c_bc_t4_t5*MAS[3]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	c_bc_t4_t5_mem0 += MM_MEM[0]
	S += 22 < c_bc_t4_t5_mem0
	S += c_bc_t4_t5_mem0 <= c_bc_t4_t5

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	c_bc_t4_t5_mem1 += MM_MEM[1]
	S += 25 < c_bc_t4_t5_mem1
	S += c_bc_t4_t5_mem1 <= c_bc_t4_t5

	c_bc_t50 = S.Task('c_bc_t50', length=3, delay_cost=1)
	c_bc_t50 += alt(MAS)
	c_bc_t50_in = S.Task('c_bc_t50_in', length=1, delay_cost=1)
	c_bc_t50_in += alt(MAS_in)
	S += c_bc_t50_in*MAS_in[0]<=c_bc_t50*MAS[0]

	S += c_bc_t50_in*MAS_in[1]<=c_bc_t50*MAS[1]

	S += c_bc_t50_in*MAS_in[2]<=c_bc_t50*MAS[2]

	S += c_bc_t50_in*MAS_in[3]<=c_bc_t50*MAS[3]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	c_bc_t50_mem0 += MAS_MEM[4]
	S += 33 < c_bc_t50_mem0
	S += c_bc_t50_mem0 <= c_bc_t50

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	c_bc_t50_mem1 += MAS_MEM[7]
	S += 29 < c_bc_t50_mem1
	S += c_bc_t50_mem1 <= c_bc_t50

	c_ac_t01 = S.Task('c_ac_t01', length=3, delay_cost=1)
	c_ac_t01 += alt(MAS)
	c_ac_t01_in = S.Task('c_ac_t01_in', length=1, delay_cost=1)
	c_ac_t01_in += alt(MAS_in)
	S += c_ac_t01_in*MAS_in[0]<=c_ac_t01*MAS[0]

	S += c_ac_t01_in*MAS_in[1]<=c_ac_t01*MAS[1]

	S += c_ac_t01_in*MAS_in[2]<=c_ac_t01*MAS[2]

	S += c_ac_t01_in*MAS_in[3]<=c_ac_t01*MAS[3]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	c_ac_t01_mem0 += MM_MEM[0]
	S += 28 < c_ac_t01_mem0
	S += c_ac_t01_mem0 <= c_ac_t01

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	c_ac_t01_mem1 += MAS_MEM[1]
	S += 26 < c_ac_t01_mem1
	S += c_ac_t01_mem1 <= c_ac_t01

	c_ac_t11 = S.Task('c_ac_t11', length=3, delay_cost=1)
	c_ac_t11 += alt(MAS)
	c_ac_t11_in = S.Task('c_ac_t11_in', length=1, delay_cost=1)
	c_ac_t11_in += alt(MAS_in)
	S += c_ac_t11_in*MAS_in[0]<=c_ac_t11*MAS[0]

	S += c_ac_t11_in*MAS_in[1]<=c_ac_t11*MAS[1]

	S += c_ac_t11_in*MAS_in[2]<=c_ac_t11*MAS[2]

	S += c_ac_t11_in*MAS_in[3]<=c_ac_t11*MAS[3]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	c_ac_t11_mem0 += MM_MEM[0]
	S += 34 < c_ac_t11_mem0
	S += c_ac_t11_mem0 <= c_ac_t11

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	c_ac_t11_mem1 += MAS_MEM[7]
	S += 28 < c_ac_t11_mem1
	S += c_ac_t11_mem1 <= c_ac_t11

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=4, delay_cost=1)
	c_ac_t4_t4 += alt(MM)
	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	c_ac_t4_t4_in += alt(MM_in)
	S += c_ac_t4_t4_in*MM_in[0]<=c_ac_t4_t4*MM[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	c_ac_t4_t4_mem0 += MAS_MEM[6]
	S += 19 < c_ac_t4_t4_mem0
	S += c_ac_t4_t4_mem0 <= c_ac_t4_t4

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	c_ac_t4_t4_mem1 += MAS_MEM[5]
	S += 19 < c_ac_t4_t4_mem1
	S += c_ac_t4_t4_mem1 <= c_ac_t4_t4

	c_ac_t40 = S.Task('c_ac_t40', length=3, delay_cost=1)
	c_ac_t40 += alt(MAS)
	c_ac_t40_in = S.Task('c_ac_t40_in', length=1, delay_cost=1)
	c_ac_t40_in += alt(MAS_in)
	S += c_ac_t40_in*MAS_in[0]<=c_ac_t40*MAS[0]

	S += c_ac_t40_in*MAS_in[1]<=c_ac_t40*MAS[1]

	S += c_ac_t40_in*MAS_in[2]<=c_ac_t40*MAS[2]

	S += c_ac_t40_in*MAS_in[3]<=c_ac_t40*MAS[3]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	c_ac_t40_mem0 += MM_MEM[0]
	S += 23 < c_ac_t40_mem0
	S += c_ac_t40_mem0 <= c_ac_t40

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	c_ac_t40_mem1 += MM_MEM[1]
	S += 33 < c_ac_t40_mem1
	S += c_ac_t40_mem1 <= c_ac_t40

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=3, delay_cost=1)
	c_ac_t4_t5 += alt(MAS)
	c_ac_t4_t5_in = S.Task('c_ac_t4_t5_in', length=1, delay_cost=1)
	c_ac_t4_t5_in += alt(MAS_in)
	S += c_ac_t4_t5_in*MAS_in[0]<=c_ac_t4_t5*MAS[0]

	S += c_ac_t4_t5_in*MAS_in[1]<=c_ac_t4_t5*MAS[1]

	S += c_ac_t4_t5_in*MAS_in[2]<=c_ac_t4_t5*MAS[2]

	S += c_ac_t4_t5_in*MAS_in[3]<=c_ac_t4_t5*MAS[3]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	c_ac_t4_t5_mem0 += MM_MEM[0]
	S += 23 < c_ac_t4_t5_mem0
	S += c_ac_t4_t5_mem0 <= c_ac_t4_t5

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	c_ac_t4_t5_mem1 += MM_MEM[1]
	S += 33 < c_ac_t4_t5_mem1
	S += c_ac_t4_t5_mem1 <= c_ac_t4_t5

	c_ac_t50 = S.Task('c_ac_t50', length=3, delay_cost=1)
	c_ac_t50 += alt(MAS)
	c_ac_t50_in = S.Task('c_ac_t50_in', length=1, delay_cost=1)
	c_ac_t50_in += alt(MAS_in)
	S += c_ac_t50_in*MAS_in[0]<=c_ac_t50*MAS[0]

	S += c_ac_t50_in*MAS_in[1]<=c_ac_t50*MAS[1]

	S += c_ac_t50_in*MAS_in[2]<=c_ac_t50*MAS[2]

	S += c_ac_t50_in*MAS_in[3]<=c_ac_t50*MAS[3]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	c_ac_t50_mem0 += MAS_MEM[6]
	S += 23 < c_ac_t50_mem0
	S += c_ac_t50_mem0 <= c_ac_t50

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	c_ac_t50_mem1 += MAS_MEM[1]
	S += 25 < c_ac_t50_mem1
	S += c_ac_t50_mem1 <= c_ac_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage3MAS4/FP12_INV_BEFORE_FPINV/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

