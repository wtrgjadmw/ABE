from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 150
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 0
	c_aa_a1_1_in += MAS_in[1]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 0
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 0
	c_aa_t10_in += MAS_in[3]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 0
	c_aa_t3_t2_in += MAS_in[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 0
	c_ab_t1_t1_in += MM_in[0]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 0
	c_bb_t10_in += MAS_in[2]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 0
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 1
	c_aa_a1_0_in += MAS_in[3]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=3, delay_cost=1)
	S += c_aa_a1_1 >= 1
	c_aa_a1_1 += MAS[1]

	c_aa_t10 = S.Task('c_aa_t10', length=3, delay_cost=1)
	S += c_aa_t10 >= 1
	c_aa_t10 += MAS[3]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=3, delay_cost=1)
	S += c_aa_t3_t2 >= 1
	c_aa_t3_t2 += MAS[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 1
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=5, delay_cost=1)
	S += c_ab_t1_t1 >= 1
	c_ab_t1_t1 += MM[0]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 1
	c_bb_a1_0_in += MAS_in[0]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 1
	c_bb_a1_1_in += MAS_in[1]

	c_bb_t10 = S.Task('c_bb_t10', length=3, delay_cost=1)
	S += c_bb_t10 >= 1
	c_bb_t10 += MAS[2]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 1
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 1
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 1
	c_cc_t3_t3_in += MAS_in[2]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=3, delay_cost=1)
	S += c_aa_a1_0 >= 2
	c_aa_a1_0 += MAS[3]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 2
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 2
	c_aa_t3_t3_in += MAS_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 2
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 2
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=5, delay_cost=1)
	S += c_ab_t1_t0 >= 2
	c_ab_t1_t0 += MM[0]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=3, delay_cost=1)
	S += c_bb_a1_0 >= 2
	c_bb_a1_0 += MAS[0]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=3, delay_cost=1)
	S += c_bb_a1_1 >= 2
	c_bb_a1_1 += MAS[1]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 2
	c_bb_t3_t3_in += MAS_in[1]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 2
	c_cc_a1_0_in += MAS_in[3]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 2
	c_cc_t3_t2_in += MAS_in[2]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=3, delay_cost=1)
	S += c_cc_t3_t3 >= 2
	c_cc_t3_t3 += MAS[2]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 3
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=5, delay_cost=1)
	S += c_aa_t3_t1 >= 3
	c_aa_t3_t1 += MM[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=3, delay_cost=1)
	S += c_aa_t3_t3 >= 3
	c_aa_t3_t3 += MAS[0]

	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 3
	c_ab_t0_t3_in += MAS_in[2]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 3
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 3
	c_bb_t11_in += MAS_in[3]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=3, delay_cost=1)
	S += c_bb_t3_t3 >= 3
	c_bb_t3_t3 += MAS[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=3, delay_cost=1)
	S += c_cc_a1_0 >= 3
	c_cc_a1_0 += MAS[3]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 3
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 3
	c_cc_a1_1_in += MAS_in[1]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 3
	c_cc_t11_in += MAS_in[0]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=3, delay_cost=1)
	S += c_cc_t3_t2 >= 3
	c_cc_t3_t2 += MAS[2]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 4
	c_aa_t11_in += MAS_in[0]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=5, delay_cost=1)
	S += c_aa_t3_t0 >= 4
	c_aa_t3_t0 += MM[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 4
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 4
	c_ab_t0_t2_in += MAS_in[2]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=3, delay_cost=1)
	S += c_ab_t0_t3 >= 4
	c_ab_t0_t3 += MAS[2]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 4
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_t11 = S.Task('c_bb_t11', length=3, delay_cost=1)
	S += c_bb_t11 >= 4
	c_bb_t11 += MAS[3]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 4
	c_bb_t3_t2_in += MAS_in[3]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=3, delay_cost=1)
	S += c_cc_a1_1 >= 4
	c_cc_a1_1 += MAS[1]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 4
	c_cc_t10_in += MAS_in[1]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 4
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=3, delay_cost=1)
	S += c_cc_t11 >= 4
	c_cc_t11 += MAS[0]

	c_aa_t11 = S.Task('c_aa_t11', length=3, delay_cost=1)
	S += c_aa_t11 >= 5
	c_aa_t11 += MAS[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 5
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=5, delay_cost=1)
	S += c_ab_t0_t1 >= 5
	c_ab_t0_t1 += MM[0]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=3, delay_cost=1)
	S += c_ab_t0_t2 >= 5
	c_ab_t0_t2 += MAS[2]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 5
	c_ab_t1_t3_in += MAS_in[0]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 5
	c_ab_t21_in += MAS_in[2]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 5
	c_ac_t0_t3_in += MAS_in[1]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=3, delay_cost=1)
	S += c_bb_t3_t2 >= 5
	c_bb_t3_t2 += MAS[3]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 5
	c_bc_t30_in += MAS_in[3]

	c_cc_t10 = S.Task('c_cc_t10', length=3, delay_cost=1)
	S += c_cc_t10 >= 5
	c_cc_t10 += MAS[1]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 5
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 5
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=3, delay_cost=1)
	S += c_ab_t1_t3 >= 6
	c_ab_t1_t3 += MAS[0]

	c_ab_t21 = S.Task('c_ab_t21', length=3, delay_cost=1)
	S += c_ab_t21 >= 6
	c_ab_t21 += MAS[2]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 6
	c_ac_t0_t2_in += MAS_in[3]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=3, delay_cost=1)
	S += c_ac_t0_t3 >= 6
	c_ac_t0_t3 += MAS[1]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 6
	c_ac_t1_t2_in += MAS_in[1]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 6
	c_ac_t1_t3_in += MAS_in[2]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 6
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 6
	c_bc_t21_in += MAS_in[0]

	c_bc_t30 = S.Task('c_bc_t30', length=3, delay_cost=1)
	S += c_bc_t30 >= 6
	c_bc_t30 += MAS[3]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 6
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 6
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=5, delay_cost=1)
	S += c_cc_t3_t1 >= 6
	c_cc_t3_t1 += MM[0]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 7
	c_ab_t20_in += MAS_in[1]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=3, delay_cost=1)
	S += c_ac_t0_t2 >= 7
	c_ac_t0_t2 += MAS[3]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=3, delay_cost=1)
	S += c_ac_t1_t2 >= 7
	c_ac_t1_t2 += MAS[1]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=3, delay_cost=1)
	S += c_ac_t1_t3 >= 7
	c_ac_t1_t3 += MAS[2]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 7
	c_ac_t31_in += MAS_in[2]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 7
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 7
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 7
	c_bc_t0_t2_in += MAS_in[0]

	c_bc_t21 = S.Task('c_bc_t21', length=3, delay_cost=1)
	S += c_bc_t21 >= 7
	c_bc_t21 += MAS[0]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 7
	c_bc_t31_in += MAS_in[3]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 7
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=5, delay_cost=1)
	S += c_cc_t3_t0 >= 7
	c_cc_t3_t0 += MM[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 8
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 8
	c_ab_t1_t2_in += MAS_in[0]

	c_ab_t20 = S.Task('c_ab_t20', length=3, delay_cost=1)
	S += c_ab_t20 >= 8
	c_ab_t20 += MAS[1]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 8
	c_ab_t30_in += MAS_in[2]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 8
	c_ac_t20_in += MAS_in[1]

	c_ac_t31 = S.Task('c_ac_t31', length=3, delay_cost=1)
	S += c_ac_t31 >= 8
	c_ac_t31 += MAS[2]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 8
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=5, delay_cost=1)
	S += c_bb_t3_t1 >= 8
	c_bb_t3_t1 += MM[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 8
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=3, delay_cost=1)
	S += c_bc_t0_t2 >= 8
	c_bc_t0_t2 += MAS[0]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 8
	c_bc_t0_t3_in += MAS_in[3]

	c_bc_t31 = S.Task('c_bc_t31', length=3, delay_cost=1)
	S += c_bc_t31 >= 8
	c_bc_t31 += MAS[3]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=5, delay_cost=1)
	S += c_ab_t0_t0 >= 9
	c_ab_t0_t0 += MM[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 9
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 9
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=3, delay_cost=1)
	S += c_ab_t1_t2 >= 9
	c_ab_t1_t2 += MAS[0]

	c_ab_t30 = S.Task('c_ab_t30', length=3, delay_cost=1)
	S += c_ab_t30 >= 9
	c_ab_t30 += MAS[2]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 9
	c_ab_t31_in += MAS_in[3]

	c_ac_t20 = S.Task('c_ac_t20', length=3, delay_cost=1)
	S += c_ac_t20 >= 9
	c_ac_t20 += MAS[1]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 9
	c_ac_t30_in += MAS_in[2]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 9
	c_bb_t3_t0_in += MM_in[0]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=3, delay_cost=1)
	S += c_bc_t0_t3 >= 9
	c_bc_t0_t3 += MAS[3]

	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	S += c_bc_t1_t2_in >= 9
	c_bc_t1_t2_in += MAS_in[0]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 9
	c_bc_t20_in += MAS_in[1]

	c_ab_t31 = S.Task('c_ab_t31', length=3, delay_cost=1)
	S += c_ab_t31 >= 10
	c_ab_t31 += MAS[3]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 10
	c_ac_t21_in += MAS_in[1]

	c_ac_t30 = S.Task('c_ac_t30', length=3, delay_cost=1)
	S += c_ac_t30 >= 10
	c_ac_t30 += MAS[2]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=5, delay_cost=1)
	S += c_bb_t3_t0 >= 10
	c_bb_t3_t0 += MM[0]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 10
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 10
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=3, delay_cost=1)
	S += c_bc_t1_t2 >= 10
	c_bc_t1_t2 += MAS[0]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 10
	c_bc_t1_t3_in += MAS_in[0]

	c_bc_t20 = S.Task('c_bc_t20', length=3, delay_cost=1)
	S += c_bc_t20 >= 10
	c_bc_t20 += MAS[1]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 10
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 11
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 11
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t21 = S.Task('c_ac_t21', length=3, delay_cost=1)
	S += c_ac_t21 >= 11
	c_ac_t21 += MAS[1]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=5, delay_cost=1)
	S += c_bc_t0_t0 >= 11
	c_bc_t0_t0 += MM[0]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=3, delay_cost=1)
	S += c_bc_t1_t3 >= 11
	c_bc_t1_t3 += MAS[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 11
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 12
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=5, delay_cost=1)
	S += c_ac_t0_t0 >= 12
	c_ac_t0_t0 += MM[0]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 12
	c_ac_t0_t1_in += MM_in[0]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 12
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 13
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=5, delay_cost=1)
	S += c_ac_t0_t1 >= 13
	c_ac_t0_t1 += MM[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 13
	c_ac_t1_t0_in += MM_in[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 13
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 14
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 14
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=5, delay_cost=1)
	S += c_ac_t1_t0 >= 14
	c_ac_t1_t0 += MM[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 14
	c_bc_t1_t0_in += MM_in[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 15
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 15
	c_ac_t1_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 15
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=5, delay_cost=1)
	S += c_bc_t1_t0 >= 15
	c_bc_t1_t0 += MM[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 16
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=5, delay_cost=1)
	S += c_ac_t1_t1 >= 16
	c_ac_t1_t1 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 16
	c_bc_t1_t1_in += MM_in[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 16
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 17
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 17
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 17
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=5, delay_cost=1)
	S += c_bc_t1_t1 >= 17
	c_bc_t1_t1 += MM[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 18
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 18
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=5, delay_cost=1)
	S += c_bc_t0_t1 >= 18
	c_bc_t0_t1 += MM[0]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 19
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 19
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 20
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 20
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 21
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 21
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 22
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 22
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 23
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 23
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 24
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 24
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 25
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 25
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 26
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 26
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 27
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 27
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 28
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 28
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 29
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 29
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 30
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 30
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 31
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 31
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 32
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 32
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 33
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 33
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 34
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 34
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 35
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 35
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 36
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 36
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 37
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 37
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 38
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 38
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 39
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 39
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 40
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 40
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 41
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 41
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 42
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 42
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 43
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 43
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 44
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 44
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 45
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 45
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 46
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 46
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 47
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 47
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 48
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 48
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 49
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 49
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 50
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 50
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 51
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 51
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 52
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 52
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 53
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 53
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 54
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 54
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 55
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 55
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 56
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 56
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 57
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 57
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 58
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 58
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 59
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 59
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]


	# new tasks
	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=3, delay_cost=1)
	c_pbc_t0_t3 += alt(MAS)
	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	c_pbc_t0_t3_in += alt(MAS_in)
	S += c_pbc_t0_t3_in*MAS_in[0]<=c_pbc_t0_t3*MAS[0]

	S += c_pbc_t0_t3_in*MAS_in[1]<=c_pbc_t0_t3*MAS[1]

	S += c_pbc_t0_t3_in*MAS_in[2]<=c_pbc_t0_t3*MAS[2]

	S += c_pbc_t0_t3_in*MAS_in[3]<=c_pbc_t0_t3*MAS[3]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]
	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]
	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=3, delay_cost=1)
	c_pbc_t1_t3 += alt(MAS)
	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	c_pbc_t1_t3_in += alt(MAS_in)
	S += c_pbc_t1_t3_in*MAS_in[0]<=c_pbc_t1_t3*MAS[0]

	S += c_pbc_t1_t3_in*MAS_in[1]<=c_pbc_t1_t3*MAS[1]

	S += c_pbc_t1_t3_in*MAS_in[2]<=c_pbc_t1_t3*MAS[2]

	S += c_pbc_t1_t3_in*MAS_in[3]<=c_pbc_t1_t3*MAS[3]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]
	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]
	c_pbc_t30 = S.Task('c_pbc_t30', length=3, delay_cost=1)
	c_pbc_t30 += alt(MAS)
	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	c_pbc_t30_in += alt(MAS_in)
	S += c_pbc_t30_in*MAS_in[0]<=c_pbc_t30*MAS[0]

	S += c_pbc_t30_in*MAS_in[1]<=c_pbc_t30*MAS[1]

	S += c_pbc_t30_in*MAS_in[2]<=c_pbc_t30*MAS[2]

	S += c_pbc_t30_in*MAS_in[3]<=c_pbc_t30*MAS[3]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	c_pbc_t30_mem0 += MAIN_MEM_r[0]
	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	c_pbc_t30_mem1 += MAIN_MEM_r[1]
	c_pbc_t31 = S.Task('c_pbc_t31', length=3, delay_cost=1)
	c_pbc_t31 += alt(MAS)
	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	c_pbc_t31_in += alt(MAS_in)
	S += c_pbc_t31_in*MAS_in[0]<=c_pbc_t31*MAS[0]

	S += c_pbc_t31_in*MAS_in[1]<=c_pbc_t31*MAS[1]

	S += c_pbc_t31_in*MAS_in[2]<=c_pbc_t31*MAS[2]

	S += c_pbc_t31_in*MAS_in[3]<=c_pbc_t31*MAS[3]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	c_pbc_t31_mem0 += MAIN_MEM_r[0]
	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	c_pbc_t31_mem1 += MAIN_MEM_r[1]
	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=3, delay_cost=1)
	c_pcb_t0_t3 += alt(MAS)
	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	c_pcb_t0_t3_in += alt(MAS_in)
	S += c_pcb_t0_t3_in*MAS_in[0]<=c_pcb_t0_t3*MAS[0]

	S += c_pcb_t0_t3_in*MAS_in[1]<=c_pcb_t0_t3*MAS[1]

	S += c_pcb_t0_t3_in*MAS_in[2]<=c_pcb_t0_t3*MAS[2]

	S += c_pcb_t0_t3_in*MAS_in[3]<=c_pcb_t0_t3*MAS[3]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]
	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]
	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=3, delay_cost=1)
	c_pcb_t1_t3 += alt(MAS)
	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	c_pcb_t1_t3_in += alt(MAS_in)
	S += c_pcb_t1_t3_in*MAS_in[0]<=c_pcb_t1_t3*MAS[0]

	S += c_pcb_t1_t3_in*MAS_in[1]<=c_pcb_t1_t3*MAS[1]

	S += c_pcb_t1_t3_in*MAS_in[2]<=c_pcb_t1_t3*MAS[2]

	S += c_pcb_t1_t3_in*MAS_in[3]<=c_pcb_t1_t3*MAS[3]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]
	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]
	c_pcb_t30 = S.Task('c_pcb_t30', length=3, delay_cost=1)
	c_pcb_t30 += alt(MAS)
	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	c_pcb_t30_in += alt(MAS_in)
	S += c_pcb_t30_in*MAS_in[0]<=c_pcb_t30*MAS[0]

	S += c_pcb_t30_in*MAS_in[1]<=c_pcb_t30*MAS[1]

	S += c_pcb_t30_in*MAS_in[2]<=c_pcb_t30*MAS[2]

	S += c_pcb_t30_in*MAS_in[3]<=c_pcb_t30*MAS[3]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	c_pcb_t30_mem0 += MAIN_MEM_r[0]
	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	c_pcb_t30_mem1 += MAIN_MEM_r[1]
	c_pcb_t31 = S.Task('c_pcb_t31', length=3, delay_cost=1)
	c_pcb_t31 += alt(MAS)
	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	c_pcb_t31_in += alt(MAS_in)
	S += c_pcb_t31_in*MAS_in[0]<=c_pcb_t31*MAS[0]

	S += c_pcb_t31_in*MAS_in[1]<=c_pcb_t31*MAS[1]

	S += c_pcb_t31_in*MAS_in[2]<=c_pcb_t31*MAS[2]

	S += c_pcb_t31_in*MAS_in[3]<=c_pcb_t31*MAS[3]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	c_pcb_t31_mem0 += MAIN_MEM_r[0]
	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	c_pcb_t31_mem1 += MAIN_MEM_r[1]
	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=3, delay_cost=1)
	c_paa_t0_t3 += alt(MAS)
	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	c_paa_t0_t3_in += alt(MAS_in)
	S += c_paa_t0_t3_in*MAS_in[0]<=c_paa_t0_t3*MAS[0]

	S += c_paa_t0_t3_in*MAS_in[1]<=c_paa_t0_t3*MAS[1]

	S += c_paa_t0_t3_in*MAS_in[2]<=c_paa_t0_t3*MAS[2]

	S += c_paa_t0_t3_in*MAS_in[3]<=c_paa_t0_t3*MAS[3]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]
	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]
	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=3, delay_cost=1)
	c_paa_t1_t3 += alt(MAS)
	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	c_paa_t1_t3_in += alt(MAS_in)
	S += c_paa_t1_t3_in*MAS_in[0]<=c_paa_t1_t3*MAS[0]

	S += c_paa_t1_t3_in*MAS_in[1]<=c_paa_t1_t3*MAS[1]

	S += c_paa_t1_t3_in*MAS_in[2]<=c_paa_t1_t3*MAS[2]

	S += c_paa_t1_t3_in*MAS_in[3]<=c_paa_t1_t3*MAS[3]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]
	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]
	c_paa_t30 = S.Task('c_paa_t30', length=3, delay_cost=1)
	c_paa_t30 += alt(MAS)
	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	c_paa_t30_in += alt(MAS_in)
	S += c_paa_t30_in*MAS_in[0]<=c_paa_t30*MAS[0]

	S += c_paa_t30_in*MAS_in[1]<=c_paa_t30*MAS[1]

	S += c_paa_t30_in*MAS_in[2]<=c_paa_t30*MAS[2]

	S += c_paa_t30_in*MAS_in[3]<=c_paa_t30*MAS[3]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	c_paa_t30_mem0 += MAIN_MEM_r[0]
	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	c_paa_t30_mem1 += MAIN_MEM_r[1]
	c_paa_t31 = S.Task('c_paa_t31', length=3, delay_cost=1)
	c_paa_t31 += alt(MAS)
	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	c_paa_t31_in += alt(MAS_in)
	S += c_paa_t31_in*MAS_in[0]<=c_paa_t31*MAS[0]

	S += c_paa_t31_in*MAS_in[1]<=c_paa_t31*MAS[1]

	S += c_paa_t31_in*MAS_in[2]<=c_paa_t31*MAS[2]

	S += c_paa_t31_in*MAS_in[3]<=c_paa_t31*MAS[3]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	c_paa_t31_mem0 += MAIN_MEM_r[0]
	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	c_paa_t31_mem1 += MAIN_MEM_r[1]
	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage3MAS4/FP12_INV_BEFORE_FPINV/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

