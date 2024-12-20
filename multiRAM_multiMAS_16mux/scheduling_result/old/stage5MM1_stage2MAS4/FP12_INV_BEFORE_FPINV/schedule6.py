from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 168
	S = Scenario("schedule6", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 0
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 0
	c_aa_t3_t3_in += MAS_in[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 0
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 0
	c_bb_t3_t2_in += MAS_in[1]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 0
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 0
	c_cc_a1_0_in += MAS_in[2]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 0
	c_cc_t3_t2_in += MAS_in[3]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 1
	c_aa_a1_1_in += MAS_in[3]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 1
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=5, delay_cost=1)
	S += c_aa_t3_t1 >= 1
	c_aa_t3_t1 += MM[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=2, delay_cost=1)
	S += c_aa_t3_t3 >= 1
	c_aa_t3_t3 += MAS[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 1
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 1
	c_ab_t1_t0_in += MM_in[0]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 1
	c_bb_a1_0_in += MAS_in[1]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 1
	c_bb_a1_1_in += MAS_in[2]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 1
	c_bb_t11_in += MAS_in[0]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=2, delay_cost=1)
	S += c_bb_t3_t2 >= 1
	c_bb_t3_t2 += MAS[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=2, delay_cost=1)
	S += c_cc_a1_0 >= 1
	c_cc_a1_0 += MAS[2]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=2, delay_cost=1)
	S += c_cc_t3_t2 >= 1
	c_cc_t3_t2 += MAS[3]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=2, delay_cost=1)
	S += c_aa_a1_1 >= 2
	c_aa_a1_1 += MAS[3]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 2
	c_aa_t11_in += MAS_in[1]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 2
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 2
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 2
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 2
	c_ab_t0_t3_in += MAS_in[3]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=5, delay_cost=1)
	S += c_ab_t1_t0 >= 2
	c_ab_t1_t0 += MM[0]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=2, delay_cost=1)
	S += c_bb_a1_0 >= 2
	c_bb_a1_0 += MAS[1]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=2, delay_cost=1)
	S += c_bb_a1_1 >= 2
	c_bb_a1_1 += MAS[2]

	c_bb_t11 = S.Task('c_bb_t11', length=2, delay_cost=1)
	S += c_bb_t11 >= 2
	c_bb_t11 += MAS[0]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 2
	c_cc_t11_in += MAS_in[0]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 2
	c_cc_t3_t3_in += MAS_in[2]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 3
	c_aa_a1_0_in += MAS_in[2]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 3
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t11 = S.Task('c_aa_t11', length=2, delay_cost=1)
	S += c_aa_t11 >= 3
	c_aa_t11 += MAS[1]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=5, delay_cost=1)
	S += c_ab_t0_t0 >= 3
	c_ab_t0_t0 += MM[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 3
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 3
	c_ab_t0_t2_in += MAS_in[1]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=2, delay_cost=1)
	S += c_ab_t0_t3 >= 3
	c_ab_t0_t3 += MAS[3]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 3
	c_bb_t3_t3_in += MAS_in[0]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 3
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 3
	c_cc_t10_in += MAS_in[3]

	c_cc_t11 = S.Task('c_cc_t11', length=2, delay_cost=1)
	S += c_cc_t11 >= 3
	c_cc_t11 += MAS[0]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=2, delay_cost=1)
	S += c_cc_t3_t3 >= 3
	c_cc_t3_t3 += MAS[2]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=2, delay_cost=1)
	S += c_aa_a1_0 >= 4
	c_aa_a1_0 += MAS[2]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 4
	c_aa_t10_in += MAS_in[2]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 4
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 4
	c_aa_t3_t2_in += MAS_in[1]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=5, delay_cost=1)
	S += c_ab_t0_t1 >= 4
	c_ab_t0_t1 += MM[0]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=2, delay_cost=1)
	S += c_ab_t0_t2 >= 4
	c_ab_t0_t2 += MAS[1]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 4
	c_bb_t10_in += MAS_in[3]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=2, delay_cost=1)
	S += c_bb_t3_t3 >= 4
	c_bb_t3_t3 += MAS[0]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 4
	c_cc_a1_1_in += MAS_in[0]

	c_cc_t10 = S.Task('c_cc_t10', length=2, delay_cost=1)
	S += c_cc_t10 >= 4
	c_cc_t10 += MAS[3]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 4
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 4
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t10 = S.Task('c_aa_t10', length=2, delay_cost=1)
	S += c_aa_t10 >= 5
	c_aa_t10 += MAS[2]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 5
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=2, delay_cost=1)
	S += c_aa_t3_t2 >= 5
	c_aa_t3_t2 += MAS[1]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 5
	c_ab_t31_in += MAS_in[2]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 5
	c_ac_t1_t2_in += MAS_in[1]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 5
	c_ac_t20_in += MAS_in[0]

	c_bb_t10 = S.Task('c_bb_t10', length=2, delay_cost=1)
	S += c_bb_t10 >= 5
	c_bb_t10 += MAS[3]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 5
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	S += c_bc_t1_t2_in >= 5
	c_bc_t1_t2_in += MAS_in[3]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=2, delay_cost=1)
	S += c_cc_a1_1 >= 5
	c_cc_a1_1 += MAS[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 5
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=5, delay_cost=1)
	S += c_cc_t3_t0 >= 5
	c_cc_t3_t0 += MM[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 6
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=5, delay_cost=1)
	S += c_aa_t3_t0 >= 6
	c_aa_t3_t0 += MM[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 6
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 6
	c_ab_t1_t3_in += MAS_in[1]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 6
	c_ab_t21_in += MAS_in[2]

	c_ab_t31 = S.Task('c_ab_t31', length=2, delay_cost=1)
	S += c_ab_t31 >= 6
	c_ab_t31 += MAS[2]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=2, delay_cost=1)
	S += c_ac_t1_t2 >= 6
	c_ac_t1_t2 += MAS[1]

	c_ac_t20 = S.Task('c_ac_t20', length=2, delay_cost=1)
	S += c_ac_t20 >= 6
	c_ac_t20 += MAS[0]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 6
	c_ac_t30_in += MAS_in[3]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 6
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=2, delay_cost=1)
	S += c_bc_t1_t2 >= 6
	c_bc_t1_t2 += MAS[3]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 6
	c_bc_t21_in += MAS_in[0]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=5, delay_cost=1)
	S += c_ab_t1_t1 >= 7
	c_ab_t1_t1 += MM[0]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=2, delay_cost=1)
	S += c_ab_t1_t3 >= 7
	c_ab_t1_t3 += MAS[1]

	c_ab_t21 = S.Task('c_ab_t21', length=2, delay_cost=1)
	S += c_ab_t21 >= 7
	c_ab_t21 += MAS[2]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 7
	c_ac_t0_t2_in += MAS_in[1]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 7
	c_ac_t21_in += MAS_in[2]

	c_ac_t30 = S.Task('c_ac_t30', length=2, delay_cost=1)
	S += c_ac_t30 >= 7
	c_ac_t30 += MAS[3]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 7
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 7
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 7
	c_bc_t1_t3_in += MAS_in[3]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 7
	c_bc_t20_in += MAS_in[0]

	c_bc_t21 = S.Task('c_bc_t21', length=2, delay_cost=1)
	S += c_bc_t21 >= 7
	c_bc_t21 += MAS[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 7
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 8
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 8
	c_ab_t1_t2_in += MAS_in[0]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 8
	c_ab_t20_in += MAS_in[3]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 8
	c_ab_t30_in += MAS_in[2]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=2, delay_cost=1)
	S += c_ac_t0_t2 >= 8
	c_ac_t0_t2 += MAS[1]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 8
	c_ac_t0_t3_in += MAS_in[1]

	c_ac_t21 = S.Task('c_ac_t21', length=2, delay_cost=1)
	S += c_ac_t21 >= 8
	c_ac_t21 += MAS[2]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 8
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=5, delay_cost=1)
	S += c_bb_t3_t1 >= 8
	c_bb_t3_t1 += MM[0]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=2, delay_cost=1)
	S += c_bc_t1_t3 >= 8
	c_bc_t1_t3 += MAS[3]

	c_bc_t20 = S.Task('c_bc_t20', length=2, delay_cost=1)
	S += c_bc_t20 >= 8
	c_bc_t20 += MAS[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 8
	c_cc_t3_t1_in += MM_in[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=2, delay_cost=1)
	S += c_ab_t1_t2 >= 9
	c_ab_t1_t2 += MAS[0]

	c_ab_t20 = S.Task('c_ab_t20', length=2, delay_cost=1)
	S += c_ab_t20 >= 9
	c_ab_t20 += MAS[3]

	c_ab_t30 = S.Task('c_ab_t30', length=2, delay_cost=1)
	S += c_ab_t30 >= 9
	c_ab_t30 += MAS[2]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=2, delay_cost=1)
	S += c_ac_t0_t3 >= 9
	c_ac_t0_t3 += MAS[1]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 9
	c_ac_t1_t3_in += MAS_in[3]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 9
	c_ac_t31_in += MAS_in[2]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 9
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 9
	c_bb_t3_t0_in += MM_in[0]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 9
	c_bc_t0_t2_in += MAS_in[0]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 9
	c_bc_t30_in += MAS_in[1]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 9
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=5, delay_cost=1)
	S += c_cc_t3_t1 >= 9
	c_cc_t3_t1 += MM[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 10
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 10
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 10
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=2, delay_cost=1)
	S += c_ac_t1_t3 >= 10
	c_ac_t1_t3 += MAS[3]

	c_ac_t31 = S.Task('c_ac_t31', length=2, delay_cost=1)
	S += c_ac_t31 >= 10
	c_ac_t31 += MAS[2]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=5, delay_cost=1)
	S += c_bb_t3_t0 >= 10
	c_bb_t3_t0 += MM[0]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=2, delay_cost=1)
	S += c_bc_t0_t2 >= 10
	c_bc_t0_t2 += MAS[0]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 10
	c_bc_t0_t3_in += MAS_in[0]

	c_bc_t30 = S.Task('c_bc_t30', length=2, delay_cost=1)
	S += c_bc_t30 >= 10
	c_bc_t30 += MAS[1]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 10
	c_bc_t31_in += MAS_in[2]

	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	S += c_paa_t0_t3_in >= 10
	c_paa_t0_t3_in += MAS_in[1]

	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	S += c_paa_t31_in >= 10
	c_paa_t31_in += MAS_in[3]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 11
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 11
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=5, delay_cost=1)
	S += c_ac_t1_t1 >= 11
	c_ac_t1_t1 += MM[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 11
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=2, delay_cost=1)
	S += c_bc_t0_t3 >= 11
	c_bc_t0_t3 += MAS[0]

	c_bc_t31 = S.Task('c_bc_t31', length=2, delay_cost=1)
	S += c_bc_t31 >= 11
	c_bc_t31 += MAS[2]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=2, delay_cost=1)
	S += c_paa_t0_t3 >= 11
	c_paa_t0_t3 += MAS[1]

	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	S += c_paa_t1_t3_in >= 11
	c_paa_t1_t3_in += MAS_in[3]

	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	S += c_paa_t30_in >= 11
	c_paa_t30_in += MAS_in[1]

	c_paa_t31 = S.Task('c_paa_t31', length=2, delay_cost=1)
	S += c_paa_t31 >= 11
	c_paa_t31 += MAS[3]

	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	S += c_pcb_t1_t3_in >= 11
	c_pcb_t1_t3_in += MAS_in[2]

	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	S += c_pcb_t31_in >= 11
	c_pcb_t31_in += MAS_in[0]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 12
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 12
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=5, delay_cost=1)
	S += c_ac_t0_t0 >= 12
	c_ac_t0_t0 += MM[0]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 12
	c_ac_t0_t1_in += MM_in[0]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=2, delay_cost=1)
	S += c_paa_t1_t3 >= 12
	c_paa_t1_t3 += MAS[3]

	c_paa_t30 = S.Task('c_paa_t30', length=2, delay_cost=1)
	S += c_paa_t30 >= 12
	c_paa_t30 += MAS[1]

	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	S += c_pbc_t1_t3_in >= 12
	c_pbc_t1_t3_in += MAS_in[3]

	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	S += c_pbc_t30_in >= 12
	c_pbc_t30_in += MAS_in[0]

	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	S += c_pbc_t31_in >= 12
	c_pbc_t31_in += MAS_in[1]

	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	S += c_pcb_t0_t3_in >= 12
	c_pcb_t0_t3_in += MAS_in[2]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=2, delay_cost=1)
	S += c_pcb_t1_t3 >= 12
	c_pcb_t1_t3 += MAS[2]

	c_pcb_t31 = S.Task('c_pcb_t31', length=2, delay_cost=1)
	S += c_pcb_t31 >= 12
	c_pcb_t31 += MAS[0]

	c_ab_t4_t2_in = S.Task('c_ab_t4_t2_in', length=1, delay_cost=1)
	S += c_ab_t4_t2_in >= 13
	c_ab_t4_t2_in += MAS_in[2]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 13
	c_ab_t4_t2_mem0 += MAS_MEM[6]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 13
	c_ab_t4_t2_mem1 += MAS_MEM[5]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=5, delay_cost=1)
	S += c_ac_t0_t1 >= 13
	c_ac_t0_t1 += MM[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 13
	c_ac_t1_t0_in += MM_in[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 13
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 13
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t5_in = S.Task('c_cc_t3_t5_in', length=1, delay_cost=1)
	S += c_cc_t3_t5_in >= 13
	c_cc_t3_t5_in += MAS_in[3]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 13
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 13
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	S += c_pbc_t0_t3_in >= 13
	c_pbc_t0_t3_in += MAS_in[0]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=2, delay_cost=1)
	S += c_pbc_t1_t3 >= 13
	c_pbc_t1_t3 += MAS[3]

	c_pbc_t30 = S.Task('c_pbc_t30', length=2, delay_cost=1)
	S += c_pbc_t30 >= 13
	c_pbc_t30 += MAS[0]

	c_pbc_t31 = S.Task('c_pbc_t31', length=2, delay_cost=1)
	S += c_pbc_t31 >= 13
	c_pbc_t31 += MAS[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=2, delay_cost=1)
	S += c_pcb_t0_t3 >= 13
	c_pcb_t0_t3 += MAS[2]

	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	S += c_pcb_t30_in >= 13
	c_pcb_t30_in += MAS_in[1]

	c_aa_t2_t3_in = S.Task('c_aa_t2_t3_in', length=1, delay_cost=1)
	S += c_aa_t2_t3_in >= 14
	c_aa_t2_t3_in += MAS_in[2]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 14
	c_aa_t2_t3_mem0 += MAS_MEM[4]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 14
	c_aa_t2_t3_mem1 += MAS_MEM[3]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 14
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t10_in = S.Task('c_ab_t10_in', length=1, delay_cost=1)
	S += c_ab_t10_in >= 14
	c_ab_t10_in += MAS_in[3]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 14
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 14
	c_ab_t10_mem1 += MM_MEM[1]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=2, delay_cost=1)
	S += c_ab_t4_t2 >= 14
	c_ab_t4_t2 += MAS[2]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=5, delay_cost=1)
	S += c_ac_t1_t0 >= 14
	c_ac_t1_t0 += MM[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 14
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t4_t2_in = S.Task('c_bc_t4_t2_in', length=1, delay_cost=1)
	S += c_bc_t4_t2_in >= 14
	c_bc_t4_t2_in += MAS_in[0]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 14
	c_bc_t4_t2_mem0 += MAS_MEM[0]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 14
	c_bc_t4_t2_mem1 += MAS_MEM[1]

	c_bc_t4_t3_in = S.Task('c_bc_t4_t3_in', length=1, delay_cost=1)
	S += c_bc_t4_t3_in >= 14
	c_bc_t4_t3_in += MAS_in[1]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 14
	c_bc_t4_t3_mem0 += MAS_MEM[2]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 14
	c_bc_t4_t3_mem1 += MAS_MEM[5]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 14
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=2, delay_cost=1)
	S += c_cc_t3_t5 >= 14
	c_cc_t3_t5 += MAS[3]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=2, delay_cost=1)
	S += c_pbc_t0_t3 >= 14
	c_pbc_t0_t3 += MAS[0]

	c_pcb_t30 = S.Task('c_pcb_t30', length=2, delay_cost=1)
	S += c_pcb_t30 >= 14
	c_pcb_t30 += MAS[1]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=2, delay_cost=1)
	S += c_aa_t2_t3 >= 15
	c_aa_t2_t3 += MAS[2]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 15
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t10 = S.Task('c_ab_t10', length=2, delay_cost=1)
	S += c_ab_t10 >= 15
	c_ab_t10 += MAS[3]

	c_ab_t1_t5_in = S.Task('c_ab_t1_t5_in', length=1, delay_cost=1)
	S += c_ab_t1_t5_in >= 15
	c_ab_t1_t5_in += MAS_in[3]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 15
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 15
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_ab_t4_t3_in = S.Task('c_ab_t4_t3_in', length=1, delay_cost=1)
	S += c_ab_t4_t3_in >= 15
	c_ab_t4_t3_in += MAS_in[0]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 15
	c_ab_t4_t3_mem0 += MAS_MEM[4]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 15
	c_ab_t4_t3_mem1 += MAS_MEM[5]

	c_bb_t2_t3_in = S.Task('c_bb_t2_t3_in', length=1, delay_cost=1)
	S += c_bb_t2_t3_in >= 15
	c_bb_t2_t3_in += MAS_in[2]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 15
	c_bb_t2_t3_mem0 += MAS_MEM[6]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 15
	c_bb_t2_t3_mem1 += MAS_MEM[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=5, delay_cost=1)
	S += c_bc_t1_t0 >= 15
	c_bc_t1_t0 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 15
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=2, delay_cost=1)
	S += c_bc_t4_t2 >= 15
	c_bc_t4_t2 += MAS[0]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=2, delay_cost=1)
	S += c_bc_t4_t3 >= 15
	c_bc_t4_t3 += MAS[1]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 15
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_pbc_t4_t3_in = S.Task('c_pbc_t4_t3_in', length=1, delay_cost=1)
	S += c_pbc_t4_t3_in >= 15
	c_pbc_t4_t3_in += MAS_in[1]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 15
	c_pbc_t4_t3_mem0 += MAS_MEM[0]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 15
	c_pbc_t4_t3_mem1 += MAS_MEM[3]

	c_aa_t01_in = S.Task('c_aa_t01_in', length=1, delay_cost=1)
	S += c_aa_t01_in >= 16
	c_aa_t01_in += MAS_in[3]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 16
	c_aa_t01_mem1 += MAS_MEM[7]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 16
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=2, delay_cost=1)
	S += c_ab_t1_t5 >= 16
	c_ab_t1_t5 += MAS[3]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=2, delay_cost=1)
	S += c_ab_t4_t3 >= 16
	c_ab_t4_t3 += MAS[0]

	c_ac_t4_t2_in = S.Task('c_ac_t4_t2_in', length=1, delay_cost=1)
	S += c_ac_t4_t2_in >= 16
	c_ac_t4_t2_in += MAS_in[0]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 16
	c_ac_t4_t2_mem0 += MAS_MEM[0]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 16
	c_ac_t4_t2_mem1 += MAS_MEM[5]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=2, delay_cost=1)
	S += c_bb_t2_t3 >= 16
	c_bb_t2_t3 += MAS[2]

	c_bb_t30_in = S.Task('c_bb_t30_in', length=1, delay_cost=1)
	S += c_bb_t30_in >= 16
	c_bb_t30_in += MAS_in[1]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 16
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 16
	c_bb_t30_mem1 += MM_MEM[1]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 16
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=5, delay_cost=1)
	S += c_bc_t1_t1 >= 16
	c_bc_t1_t1 += MM[0]

	c_cc_t2_t3_in = S.Task('c_cc_t2_t3_in', length=1, delay_cost=1)
	S += c_cc_t2_t3_in >= 16
	c_cc_t2_t3_in += MAS_in[2]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 16
	c_cc_t2_t3_mem0 += MAS_MEM[6]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 16
	c_cc_t2_t3_mem1 += MAS_MEM[1]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 16
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=2, delay_cost=1)
	S += c_pbc_t4_t3 >= 16
	c_pbc_t4_t3 += MAS[1]

	c_aa_t01 = S.Task('c_aa_t01', length=2, delay_cost=1)
	S += c_aa_t01 >= 17
	c_aa_t01 += MAS[3]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 17
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=2, delay_cost=1)
	S += c_ac_t4_t2 >= 17
	c_ac_t4_t2 += MAS[0]

	c_ac_t4_t3_in = S.Task('c_ac_t4_t3_in', length=1, delay_cost=1)
	S += c_ac_t4_t3_in >= 17
	c_ac_t4_t3_in += MAS_in[3]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 17
	c_ac_t4_t3_mem0 += MAS_MEM[6]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 17
	c_ac_t4_t3_mem1 += MAS_MEM[5]

	c_bb_t00_in = S.Task('c_bb_t00_in', length=1, delay_cost=1)
	S += c_bb_t00_in >= 17
	c_bb_t00_in += MAS_in[2]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 17
	c_bb_t00_mem1 += MAS_MEM[3]

	c_bb_t30 = S.Task('c_bb_t30', length=2, delay_cost=1)
	S += c_bb_t30 >= 17
	c_bb_t30 += MAS[1]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 17
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=5, delay_cost=1)
	S += c_bc_t0_t1 >= 17
	c_bc_t0_t1 += MM[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 17
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=2, delay_cost=1)
	S += c_cc_t2_t3 >= 17
	c_cc_t2_t3 += MAS[2]

	c_cc_t30_in = S.Task('c_cc_t30_in', length=1, delay_cost=1)
	S += c_cc_t30_in >= 17
	c_cc_t30_in += MAS_in[0]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 17
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 17
	c_cc_t30_mem1 += MM_MEM[1]

	c_pcb_t4_t3_in = S.Task('c_pcb_t4_t3_in', length=1, delay_cost=1)
	S += c_pcb_t4_t3_in >= 17
	c_pcb_t4_t3_in += MAS_in[1]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 17
	c_pcb_t4_t3_mem0 += MAS_MEM[2]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 17
	c_pcb_t4_t3_mem1 += MAS_MEM[1]

	c_aa_t00_in = S.Task('c_aa_t00_in', length=1, delay_cost=1)
	S += c_aa_t00_in >= 18
	c_aa_t00_in += MAS_in[2]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 18
	c_aa_t00_mem1 += MAS_MEM[5]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 18
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t5_in = S.Task('c_ac_t1_t5_in', length=1, delay_cost=1)
	S += c_ac_t1_t5_in >= 18
	c_ac_t1_t5_in += MAS_in[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 18
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 18
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 18
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 18
	c_ac_t4_t0_mem0 += MAS_MEM[0]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 18
	c_ac_t4_t0_mem1 += MAS_MEM[7]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=2, delay_cost=1)
	S += c_ac_t4_t3 >= 18
	c_ac_t4_t3 += MAS[3]

	c_bb10_in = S.Task('c_bb10_in', length=1, delay_cost=1)
	S += c_bb10_in >= 18
	c_bb10_in += MAS_in[1]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 18
	c_bb10_mem0 += MAS_MEM[2]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 18
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t00 = S.Task('c_bb_t00', length=2, delay_cost=1)
	S += c_bb_t00 >= 18
	c_bb_t00 += MAS[2]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=5, delay_cost=1)
	S += c_bc_t0_t0 >= 18
	c_bc_t0_t0 += MM[0]

	c_cc_t01_in = S.Task('c_cc_t01_in', length=1, delay_cost=1)
	S += c_cc_t01_in >= 18
	c_cc_t01_in += MAS_in[3]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 18
	c_cc_t01_mem1 += MAS_MEM[1]

	c_cc_t30 = S.Task('c_cc_t30', length=2, delay_cost=1)
	S += c_cc_t30 >= 18
	c_cc_t30 += MAS[0]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=2, delay_cost=1)
	S += c_pcb_t4_t3 >= 18
	c_pcb_t4_t3 += MAS[1]

	c_aa_t00 = S.Task('c_aa_t00', length=2, delay_cost=1)
	S += c_aa_t00 >= 19
	c_aa_t00 += MAS[2]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 19
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 19
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 19
	c_ac_t0_t4_mem0 += MAS_MEM[2]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 19
	c_ac_t0_t4_mem1 += MAS_MEM[3]

	c_ac_t0_t5_in = S.Task('c_ac_t0_t5_in', length=1, delay_cost=1)
	S += c_ac_t0_t5_in >= 19
	c_ac_t0_t5_in += MAS_in[2]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 19
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 19
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=2, delay_cost=1)
	S += c_ac_t1_t5 >= 19
	c_ac_t1_t5 += MAS[0]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=5, delay_cost=1)
	S += c_ac_t4_t0 >= 19
	c_ac_t4_t0 += MM[0]

	c_bb10 = S.Task('c_bb10', length=2, delay_cost=1)
	S += c_bb10 >= 19
	c_bb10 += MAS[1]

	c_bb_t01_in = S.Task('c_bb_t01_in', length=1, delay_cost=1)
	S += c_bb_t01_in >= 19
	c_bb_t01_in += MAS_in[1]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 19
	c_bb_t01_mem1 += MAS_MEM[5]

	c_cc10_in = S.Task('c_cc10_in', length=1, delay_cost=1)
	S += c_cc10_in >= 19
	c_cc10_in += MAS_in[0]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 19
	c_cc10_mem0 += MAS_MEM[0]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 19
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_t01 = S.Task('c_cc_t01', length=2, delay_cost=1)
	S += c_cc_t01 >= 19
	c_cc_t01 += MAS[3]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 20
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t2_t2_in = S.Task('c_aa_t2_t2_in', length=1, delay_cost=1)
	S += c_aa_t2_t2_in >= 20
	c_aa_t2_t2_in += MAS_in[2]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 20
	c_aa_t2_t2_mem0 += MAS_MEM[4]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 20
	c_aa_t2_t2_mem1 += MAS_MEM[7]

	c_aa_t30_in = S.Task('c_aa_t30_in', length=1, delay_cost=1)
	S += c_aa_t30_in >= 20
	c_aa_t30_in += MAS_in[3]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 20
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 20
	c_aa_t30_mem1 += MM_MEM[1]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 20
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 20
	c_aa_t3_t4_mem0 += MAS_MEM[2]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 20
	c_aa_t3_t4_mem1 += MAS_MEM[1]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=5, delay_cost=1)
	S += c_ac_t0_t4 >= 20
	c_ac_t0_t4 += MM[0]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=2, delay_cost=1)
	S += c_ac_t0_t5 >= 20
	c_ac_t0_t5 += MAS[2]

	c_bb_t01 = S.Task('c_bb_t01', length=2, delay_cost=1)
	S += c_bb_t01 >= 20
	c_bb_t01 += MAS[1]

	c_cc10 = S.Task('c_cc10', length=2, delay_cost=1)
	S += c_cc10 >= 20
	c_cc10 += MAS[0]

	c_cc_t00_in = S.Task('c_cc_t00_in', length=1, delay_cost=1)
	S += c_cc_t00_in >= 20
	c_cc_t00_in += MAS_in[1]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 20
	c_cc_t00_mem1 += MAS_MEM[5]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 20
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=2, delay_cost=1)
	S += c_aa_t2_t2 >= 21
	c_aa_t2_t2 += MAS[2]

	c_aa_t30 = S.Task('c_aa_t30', length=2, delay_cost=1)
	S += c_aa_t30 >= 21
	c_aa_t30 += MAS[3]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=5, delay_cost=1)
	S += c_aa_t3_t4 >= 21
	c_aa_t3_t4 += MM[0]

	c_aa_t3_t5_in = S.Task('c_aa_t3_t5_in', length=1, delay_cost=1)
	S += c_aa_t3_t5_in >= 21
	c_aa_t3_t5_in += MAS_in[1]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 21
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 21
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 21
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 21
	c_ab_t0_t4_mem0 += MAS_MEM[2]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 21
	c_ab_t0_t4_mem1 += MAS_MEM[7]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 21
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 21
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t2_t2_in = S.Task('c_bb_t2_t2_in', length=1, delay_cost=1)
	S += c_bb_t2_t2_in >= 21
	c_bb_t2_t2_in += MAS_in[3]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 21
	c_bb_t2_t2_mem0 += MAS_MEM[4]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 21
	c_bb_t2_t2_mem1 += MAS_MEM[3]

	c_cc_t00 = S.Task('c_cc_t00', length=2, delay_cost=1)
	S += c_cc_t00 >= 21
	c_cc_t00 += MAS[1]

	c_aa10_in = S.Task('c_aa10_in', length=1, delay_cost=1)
	S += c_aa10_in >= 22
	c_aa10_in += MAS_in[3]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 22
	c_aa10_mem0 += MAS_MEM[6]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 22
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=2, delay_cost=1)
	S += c_aa_t3_t5 >= 22
	c_aa_t3_t5 += MAS[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=5, delay_cost=1)
	S += c_ab_t0_t4 >= 22
	c_ab_t0_t4 += MM[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 22
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=2, delay_cost=1)
	S += c_bb_t2_t2 >= 22
	c_bb_t2_t2 += MAS[3]

	c_bc_t1_t5_in = S.Task('c_bc_t1_t5_in', length=1, delay_cost=1)
	S += c_bc_t1_t5_in >= 22
	c_bc_t1_t5_in += MAS_in[0]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 22
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 22
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 22
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 22
	c_bc_t4_t0_mem0 += MAS_MEM[0]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 22
	c_bc_t4_t0_mem1 += MAS_MEM[3]

	c_paa_t4_t3_in = S.Task('c_paa_t4_t3_in', length=1, delay_cost=1)
	S += c_paa_t4_t3_in >= 22
	c_paa_t4_t3_in += MAS_in[2]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 22
	c_paa_t4_t3_mem0 += MAS_MEM[2]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 22
	c_paa_t4_t3_mem1 += MAS_MEM[7]

	c_aa10 = S.Task('c_aa10', length=2, delay_cost=1)
	S += c_aa10 >= 23
	c_aa10 += MAS[3]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 23
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 23
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t5_in = S.Task('c_bc_t0_t5_in', length=1, delay_cost=1)
	S += c_bc_t0_t5_in >= 23
	c_bc_t0_t5_in += MAS_in[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 23
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 23
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 23
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 23
	c_bc_t1_t4_mem0 += MAS_MEM[6]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 23
	c_bc_t1_t4_mem1 += MAS_MEM[7]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=2, delay_cost=1)
	S += c_bc_t1_t5 >= 23
	c_bc_t1_t5 += MAS[0]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=5, delay_cost=1)
	S += c_bc_t4_t0 >= 23
	c_bc_t4_t0 += MM[0]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=2, delay_cost=1)
	S += c_paa_t4_t3 >= 23
	c_paa_t4_t3 += MAS[2]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 24
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 24
	c_ab_t1_t4_mem0 += MAS_MEM[0]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 24
	c_ab_t1_t4_mem1 += MAS_MEM[3]

	c_ac_t00_in = S.Task('c_ac_t00_in', length=1, delay_cost=1)
	S += c_ac_t00_in >= 24
	c_ac_t00_in += MAS_in[2]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 24
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 24
	c_ac_t00_mem1 += MM_MEM[1]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 24
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=2, delay_cost=1)
	S += c_bc_t0_t5 >= 24
	c_bc_t0_t5 += MAS[0]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=5, delay_cost=1)
	S += c_bc_t1_t4 >= 24
	c_bc_t1_t4 += MM[0]

	c_cc_t2_t2_in = S.Task('c_cc_t2_t2_in', length=1, delay_cost=1)
	S += c_cc_t2_t2_in >= 24
	c_cc_t2_t2_in += MAS_in[0]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 24
	c_cc_t2_t2_mem0 += MAS_MEM[2]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 24
	c_cc_t2_t2_mem1 += MAS_MEM[7]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 24
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 25
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 25
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=5, delay_cost=1)
	S += c_ab_t1_t4 >= 25
	c_ab_t1_t4 += MM[0]

	c_ac_t00 = S.Task('c_ac_t00', length=2, delay_cost=1)
	S += c_ac_t00 >= 25
	c_ac_t00 += MAS[2]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 25
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 25
	c_ac_t4_t1_mem0 += MAS_MEM[4]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 25
	c_ac_t4_t1_mem1 += MAS_MEM[5]

	c_bb_t3_t5_in = S.Task('c_bb_t3_t5_in', length=1, delay_cost=1)
	S += c_bb_t3_t5_in >= 25
	c_bb_t3_t5_in += MAS_in[0]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 25
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 25
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=2, delay_cost=1)
	S += c_cc_t2_t2 >= 25
	c_cc_t2_t2 += MAS[0]

	c_ab_t00_in = S.Task('c_ab_t00_in', length=1, delay_cost=1)
	S += c_ab_t00_in >= 26
	c_ab_t00_in += MAS_in[2]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 26
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 26
	c_ab_t00_mem1 += MM_MEM[1]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 26
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 26
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 26
	c_ab_t4_t0_mem0 += MAS_MEM[6]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 26
	c_ab_t4_t0_mem1 += MAS_MEM[5]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=5, delay_cost=1)
	S += c_ac_t4_t1 >= 26
	c_ac_t4_t1 += MM[0]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=2, delay_cost=1)
	S += c_bb_t3_t5 >= 26
	c_bb_t3_t5 += MAS[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 26
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 27
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t00 = S.Task('c_ab_t00', length=2, delay_cost=1)
	S += c_ab_t00 >= 27
	c_ab_t00 += MAS[2]

	c_ab_t0_t5_in = S.Task('c_ab_t0_t5_in', length=1, delay_cost=1)
	S += c_ab_t0_t5_in >= 27
	c_ab_t0_t5_in += MAS_in[2]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 27
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 27
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=5, delay_cost=1)
	S += c_ab_t4_t0 >= 27
	c_ab_t4_t0 += MM[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 27
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 27
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 27
	c_cc_t3_t4_mem0 += MAS_MEM[6]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 27
	c_cc_t3_t4_mem1 += MAS_MEM[5]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 28
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=2, delay_cost=1)
	S += c_ab_t0_t5 >= 28
	c_ab_t0_t5 += MAS[2]

	c_ab_t50_in = S.Task('c_ab_t50_in', length=1, delay_cost=1)
	S += c_ab_t50_in >= 28
	c_ab_t50_in += MAS_in[1]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 28
	c_ab_t50_mem0 += MAS_MEM[4]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 28
	c_ab_t50_mem1 += MAS_MEM[7]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 28
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t00_in = S.Task('c_bc_t00_in', length=1, delay_cost=1)
	S += c_bc_t00_in >= 28
	c_bc_t00_in += MAS_in[3]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 28
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 28
	c_bc_t00_mem1 += MM_MEM[1]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 28
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 28
	c_bc_t4_t1_mem0 += MAS_MEM[0]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 28
	c_bc_t4_t1_mem1 += MAS_MEM[5]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=5, delay_cost=1)
	S += c_cc_t3_t4 >= 28
	c_cc_t3_t4 += MM[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 29
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 29
	c_ab_t4_t1_mem0 += MAS_MEM[4]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 29
	c_ab_t4_t1_mem1 += MAS_MEM[5]

	c_ab_t50 = S.Task('c_ab_t50', length=2, delay_cost=1)
	S += c_ab_t50 >= 29
	c_ab_t50 += MAS[1]

	c_ac_t10_in = S.Task('c_ac_t10_in', length=1, delay_cost=1)
	S += c_ac_t10_in >= 29
	c_ac_t10_in += MAS_in[0]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 29
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 29
	c_ac_t10_mem1 += MM_MEM[1]

	c_bc_t00 = S.Task('c_bc_t00', length=2, delay_cost=1)
	S += c_bc_t00 >= 29
	c_bc_t00 += MAS[3]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=5, delay_cost=1)
	S += c_bc_t4_t1 >= 29
	c_bc_t4_t1 += MM[0]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 29
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 29
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 30
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=5, delay_cost=1)
	S += c_ab_t4_t1 >= 30
	c_ab_t4_t1 += MM[0]

	c_ac_t10 = S.Task('c_ac_t10', length=2, delay_cost=1)
	S += c_ac_t10 >= 30
	c_ac_t10 += MAS[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 30
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 30
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 30
	c_bc_t0_t4_mem0 += MAS_MEM[0]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 30
	c_bc_t0_t4_mem1 += MAS_MEM[1]

	c_bc_t10_in = S.Task('c_bc_t10_in', length=1, delay_cost=1)
	S += c_bc_t10_in >= 30
	c_bc_t10_in += MAS_in[0]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 30
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 30
	c_bc_t10_mem1 += MM_MEM[1]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 31
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 31
	c_ac_t1_t4_mem0 += MAS_MEM[2]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 31
	c_ac_t1_t4_mem1 += MAS_MEM[7]

	c_ac_t4_t5_in = S.Task('c_ac_t4_t5_in', length=1, delay_cost=1)
	S += c_ac_t4_t5_in >= 31
	c_ac_t4_t5_in += MAS_in[1]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 31
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 31
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_ac_t50_in = S.Task('c_ac_t50_in', length=1, delay_cost=1)
	S += c_ac_t50_in >= 31
	c_ac_t50_in += MAS_in[0]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 31
	c_ac_t50_mem0 += MAS_MEM[4]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 31
	c_ac_t50_mem1 += MAS_MEM[1]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 31
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=5, delay_cost=1)
	S += c_bc_t0_t4 >= 31
	c_bc_t0_t4 += MM[0]

	c_bc_t10 = S.Task('c_bc_t10', length=2, delay_cost=1)
	S += c_bc_t10 >= 31
	c_bc_t10 += MAS[0]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 31
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 32
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 32
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=5, delay_cost=1)
	S += c_ac_t1_t4 >= 32
	c_ac_t1_t4 += MM[0]

	c_ac_t40_in = S.Task('c_ac_t40_in', length=1, delay_cost=1)
	S += c_ac_t40_in >= 32
	c_ac_t40_in += MAS_in[1]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 32
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 32
	c_ac_t40_mem1 += MM_MEM[1]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=2, delay_cost=1)
	S += c_ac_t4_t5 >= 32
	c_ac_t4_t5 += MAS[1]

	c_ac_t50 = S.Task('c_ac_t50', length=2, delay_cost=1)
	S += c_ac_t50 >= 32
	c_ac_t50 += MAS[0]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 32
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 32
	c_bb_t3_t4_mem0 += MAS_MEM[2]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 32
	c_bb_t3_t4_mem1 += MAS_MEM[1]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 33
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 33
	c_aa_t2_t0_mem0 += MAS_MEM[4]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 33
	c_aa_t2_t0_mem1 += MAS_MEM[5]

	c_ac_t40 = S.Task('c_ac_t40', length=2, delay_cost=1)
	S += c_ac_t40 >= 33
	c_ac_t40 += MAS[1]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=5, delay_cost=1)
	S += c_bb_t3_t4 >= 33
	c_bb_t3_t4 += MM[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 33
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 33
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t50_in = S.Task('c_bc_t50_in', length=1, delay_cost=1)
	S += c_bc_t50_in >= 33
	c_bc_t50_in += MAS_in[3]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 33
	c_bc_t50_mem0 += MAS_MEM[6]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 33
	c_bc_t50_mem1 += MAS_MEM[1]

	c_cc_t31_in = S.Task('c_cc_t31_in', length=1, delay_cost=1)
	S += c_cc_t31_in >= 33
	c_cc_t31_in += MAS_in[1]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 33
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 33
	c_cc_t31_mem1 += MAS_MEM[7]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=5, delay_cost=1)
	S += c_aa_t2_t0 >= 34
	c_aa_t2_t0 += MM[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 34
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac10_in = S.Task('c_ac10_in', length=1, delay_cost=1)
	S += c_ac10_in >= 34
	c_ac10_in += MAS_in[2]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 34
	c_ac10_mem0 += MAS_MEM[2]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 34
	c_ac10_mem1 += MAS_MEM[1]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 34
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 34
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 34
	c_bc_t4_t4_mem0 += MAS_MEM[0]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 34
	c_bc_t4_t4_mem1 += MAS_MEM[3]

	c_bc_t4_t5_in = S.Task('c_bc_t4_t5_in', length=1, delay_cost=1)
	S += c_bc_t4_t5_in >= 34
	c_bc_t4_t5_in += MAS_in[0]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 34
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 34
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_bc_t50 = S.Task('c_bc_t50', length=2, delay_cost=1)
	S += c_bc_t50 >= 34
	c_bc_t50 += MAS[3]

	c_cc_t31 = S.Task('c_cc_t31', length=2, delay_cost=1)
	S += c_cc_t31 >= 34
	c_cc_t31 += MAS[1]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 35
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t4_t5_in = S.Task('c_ab_t4_t5_in', length=1, delay_cost=1)
	S += c_ab_t4_t5_in >= 35
	c_ab_t4_t5_in += MAS_in[0]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 35
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 35
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ac10 = S.Task('c_ac10', length=2, delay_cost=1)
	S += c_ac10 >= 35
	c_ac10 += MAS[2]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 35
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=5, delay_cost=1)
	S += c_bc_t4_t4 >= 35
	c_bc_t4_t4 += MM[0]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=2, delay_cost=1)
	S += c_bc_t4_t5 >= 35
	c_bc_t4_t5 += MAS[0]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 35
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 35
	c_cc_t2_t0_mem0 += MAS_MEM[2]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 35
	c_cc_t2_t0_mem1 += MAS_MEM[7]

	c_cc_t40_in = S.Task('c_cc_t40_in', length=1, delay_cost=1)
	S += c_cc_t40_in >= 35
	c_cc_t40_in += MAS_in[3]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 35
	c_cc_t40_mem0 += MAS_MEM[0]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 35
	c_cc_t40_mem1 += MAS_MEM[3]

	c_ab_t40_in = S.Task('c_ab_t40_in', length=1, delay_cost=1)
	S += c_ab_t40_in >= 36
	c_ab_t40_in += MAS_in[3]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 36
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 36
	c_ab_t40_mem1 += MM_MEM[1]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=2, delay_cost=1)
	S += c_ab_t4_t5 >= 36
	c_ab_t4_t5 += MAS[0]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 36
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 36
	c_bb_t2_t1_mem0 += MAS_MEM[2]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 36
	c_bb_t2_t1_mem1 += MAS_MEM[1]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 36
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 36
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=5, delay_cost=1)
	S += c_cc_t2_t0 >= 36
	c_cc_t2_t0 += MM[0]

	c_cc_t40 = S.Task('c_cc_t40', length=2, delay_cost=1)
	S += c_cc_t40 >= 36
	c_cc_t40 += MAS[3]

	c_ab_t01_in = S.Task('c_ab_t01_in', length=1, delay_cost=1)
	S += c_ab_t01_in >= 37
	c_ab_t01_in += MAS_in[3]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 37
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 37
	c_ab_t01_mem1 += MAS_MEM[5]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 37
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t40 = S.Task('c_ab_t40', length=2, delay_cost=1)
	S += c_ab_t40 >= 37
	c_ab_t40 += MAS[3]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 37
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 37
	c_ab_t4_t4_mem0 += MAS_MEM[4]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 37
	c_ab_t4_t4_mem1 += MAS_MEM[1]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=5, delay_cost=1)
	S += c_bb_t2_t1 >= 37
	c_bb_t2_t1 += MM[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 37
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_cc11_in = S.Task('c_cc11_in', length=1, delay_cost=1)
	S += c_cc11_in >= 37
	c_cc11_in += MAS_in[1]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 37
	c_cc11_mem0 += MAS_MEM[2]

	c_ab10_in = S.Task('c_ab10_in', length=1, delay_cost=1)
	S += c_ab10_in >= 38
	c_ab10_in += MAS_in[3]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 38
	c_ab10_mem0 += MAS_MEM[6]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 38
	c_ab10_mem1 += MAS_MEM[3]

	c_ab_t01 = S.Task('c_ab_t01', length=2, delay_cost=1)
	S += c_ab_t01 >= 38
	c_ab_t01 += MAS[3]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=5, delay_cost=1)
	S += c_ab_t4_t4 >= 38
	c_ab_t4_t4 += MM[0]

	c_ac_t01_in = S.Task('c_ac_t01_in', length=1, delay_cost=1)
	S += c_ac_t01_in >= 38
	c_ac_t01_in += MAS_in[0]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 38
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 38
	c_ac_t01_mem1 += MAS_MEM[5]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 38
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 38
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 38
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 38
	c_bb_t2_t0_mem0 += MAS_MEM[4]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 38
	c_bb_t2_t0_mem1 += MAS_MEM[7]

	c_cc11 = S.Task('c_cc11', length=2, delay_cost=1)
	S += c_cc11 >= 38
	c_cc11 += MAS[1]

	c_cc_t41_in = S.Task('c_cc_t41_in', length=1, delay_cost=1)
	S += c_cc_t41_in >= 38
	c_cc_t41_in += MAS_in[1]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 38
	c_cc_t41_mem0 += MAS_MEM[2]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 38
	c_cc_t41_mem1 += MAS_MEM[1]

	c_aa_t31_in = S.Task('c_aa_t31_in', length=1, delay_cost=1)
	S += c_aa_t31_in >= 39
	c_aa_t31_in += MAS_in[3]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 39
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 39
	c_aa_t31_mem1 += MAS_MEM[3]

	c_ab10 = S.Task('c_ab10', length=2, delay_cost=1)
	S += c_ab10 >= 39
	c_ab10 += MAS[3]

	c_ac_t01 = S.Task('c_ac_t01', length=2, delay_cost=1)
	S += c_ac_t01 >= 39
	c_ac_t01 += MAS[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 39
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 39
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 39
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 39
	c_ac_t4_t4_mem0 += MAS_MEM[0]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 39
	c_ac_t4_t4_mem1 += MAS_MEM[7]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=5, delay_cost=1)
	S += c_bb_t2_t0 >= 39
	c_bb_t2_t0 += MM[0]

	c_cc_t41 = S.Task('c_cc_t41', length=2, delay_cost=1)
	S += c_cc_t41 >= 39
	c_cc_t41 += MAS[1]

	c_aa_t31 = S.Task('c_aa_t31', length=2, delay_cost=1)
	S += c_aa_t31 >= 40
	c_aa_t31 += MAS[3]

	c_ab_t11_in = S.Task('c_ab_t11_in', length=1, delay_cost=1)
	S += c_ab_t11_in >= 40
	c_ab_t11_in += MAS_in[3]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 40
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 40
	c_ab_t11_mem1 += MAS_MEM[7]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 40
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=5, delay_cost=1)
	S += c_ac_t4_t4 >= 40
	c_ac_t4_t4 += MM[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 40
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 40
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 40
	c_cc_t2_t1_mem0 += MAS_MEM[6]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 40
	c_cc_t2_t1_mem1 += MAS_MEM[1]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 41
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 41
	c_aa_t2_t1_mem0 += MAS_MEM[6]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 41
	c_aa_t2_t1_mem1 += MAS_MEM[3]

	c_ab_t11 = S.Task('c_ab_t11', length=2, delay_cost=1)
	S += c_ab_t11 >= 41
	c_ab_t11 += MAS[3]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 41
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t11_in = S.Task('c_ac_t11_in', length=1, delay_cost=1)
	S += c_ac_t11_in >= 41
	c_ac_t11_in += MAS_in[3]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 41
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 41
	c_ac_t11_mem1 += MAS_MEM[1]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 41
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=5, delay_cost=1)
	S += c_cc_t2_t1 >= 41
	c_cc_t2_t1 += MM[0]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=5, delay_cost=1)
	S += c_aa_t2_t1 >= 42
	c_aa_t2_t1 += MM[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 42
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t51_in = S.Task('c_ab_t51_in', length=1, delay_cost=1)
	S += c_ab_t51_in >= 42
	c_ab_t51_in += MAS_in[0]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 42
	c_ab_t51_mem0 += MAS_MEM[6]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 42
	c_ab_t51_mem1 += MAS_MEM[7]

	c_ac_t11 = S.Task('c_ac_t11', length=2, delay_cost=1)
	S += c_ac_t11 >= 42
	c_ac_t11 += MAS[3]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 42
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t11_in = S.Task('c_bc_t11_in', length=1, delay_cost=1)
	S += c_bc_t11_in >= 42
	c_bc_t11_in += MAS_in[2]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 42
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 42
	c_bc_t11_mem1 += MAS_MEM[1]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 42
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 42
	c_cc_t2_t4_mem0 += MAS_MEM[0]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 42
	c_cc_t2_t4_mem1 += MAS_MEM[5]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 43
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 43
	c_aa_t2_t4_mem0 += MAS_MEM[4]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 43
	c_aa_t2_t4_mem1 += MAS_MEM[5]

	c_ab_t51 = S.Task('c_ab_t51', length=2, delay_cost=1)
	S += c_ab_t51 >= 43
	c_ab_t51 += MAS[0]

	c_ac_s00_in = S.Task('c_ac_s00_in', length=1, delay_cost=1)
	S += c_ac_s00_in >= 43
	c_ac_s00_in += MAS_in[3]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 43
	c_ac_s00_mem0 += MAS_MEM[0]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 43
	c_ac_s00_mem1 += MAS_MEM[7]

	c_ac_s01_in = S.Task('c_ac_s01_in', length=1, delay_cost=1)
	S += c_ac_s01_in >= 43
	c_ac_s01_in += MAS_in[0]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 43
	c_ac_s01_mem0 += MAS_MEM[6]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 43
	c_ac_s01_mem1 += MAS_MEM[1]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 43
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 43
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t11 = S.Task('c_bc_t11', length=2, delay_cost=1)
	S += c_bc_t11 >= 43
	c_bc_t11 += MAS[2]

	c_bc_t40_in = S.Task('c_bc_t40_in', length=1, delay_cost=1)
	S += c_bc_t40_in >= 43
	c_bc_t40_in += MAS_in[1]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 43
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 43
	c_bc_t40_mem1 += MM_MEM[1]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=5, delay_cost=1)
	S += c_cc_t2_t4 >= 43
	c_cc_t2_t4 += MM[0]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=5, delay_cost=1)
	S += c_aa_t2_t4 >= 44
	c_aa_t2_t4 += MM[0]

	c_ac_s00 = S.Task('c_ac_s00', length=2, delay_cost=1)
	S += c_ac_s00 >= 44
	c_ac_s00 += MAS[3]

	c_ac_s01 = S.Task('c_ac_s01', length=2, delay_cost=1)
	S += c_ac_s01 >= 44
	c_ac_s01 += MAS[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 44
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t51_in = S.Task('c_ac_t51_in', length=1, delay_cost=1)
	S += c_ac_t51_in >= 44
	c_ac_t51_in += MAS_in[0]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 44
	c_ac_t51_mem0 += MAS_MEM[0]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 44
	c_ac_t51_mem1 += MAS_MEM[7]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 44
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 44
	c_bb_t2_t4_mem0 += MAS_MEM[6]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 44
	c_bb_t2_t4_mem1 += MAS_MEM[5]

	c_bc_t01_in = S.Task('c_bc_t01_in', length=1, delay_cost=1)
	S += c_bc_t01_in >= 44
	c_bc_t01_in += MAS_in[2]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 44
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 44
	c_bc_t01_mem1 += MAS_MEM[1]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 44
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t40 = S.Task('c_bc_t40', length=2, delay_cost=1)
	S += c_bc_t40 >= 44
	c_bc_t40 += MAS[1]

	c_aa11_in = S.Task('c_aa11_in', length=1, delay_cost=1)
	S += c_aa11_in >= 45
	c_aa11_in += MAS_in[0]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 45
	c_aa11_mem0 += MAS_MEM[6]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 45
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t51 = S.Task('c_ac_t51', length=2, delay_cost=1)
	S += c_ac_t51 >= 45
	c_ac_t51 += MAS[0]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=5, delay_cost=1)
	S += c_bb_t2_t4 >= 45
	c_bb_t2_t4 += MM[0]

	c_bb_t31_in = S.Task('c_bb_t31_in', length=1, delay_cost=1)
	S += c_bb_t31_in >= 45
	c_bb_t31_in += MAS_in[1]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 45
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 45
	c_bb_t31_mem1 += MAS_MEM[1]

	c_bc10_in = S.Task('c_bc10_in', length=1, delay_cost=1)
	S += c_bc10_in >= 45
	c_bc10_in += MAS_in[2]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 45
	c_bc10_mem0 += MAS_MEM[2]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 45
	c_bc10_mem1 += MAS_MEM[7]

	c_bc_s00_in = S.Task('c_bc_s00_in', length=1, delay_cost=1)
	S += c_bc_s00_in >= 45
	c_bc_s00_in += MAS_in[3]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 45
	c_bc_s00_mem0 += MAS_MEM[0]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 45
	c_bc_s00_mem1 += MAS_MEM[5]

	c_bc_t01 = S.Task('c_bc_t01', length=2, delay_cost=1)
	S += c_bc_t01 >= 45
	c_bc_t01 += MAS[2]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 45
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_aa11 = S.Task('c_aa11', length=2, delay_cost=1)
	S += c_aa11 >= 46
	c_aa11 += MAS[0]

	c_ab_s01_in = S.Task('c_ab_s01_in', length=1, delay_cost=1)
	S += c_ab_s01_in >= 46
	c_ab_s01_in += MAS_in[3]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 46
	c_ab_s01_mem0 += MAS_MEM[6]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 46
	c_ab_s01_mem1 += MAS_MEM[7]

	c_bb_t20_in = S.Task('c_bb_t20_in', length=1, delay_cost=1)
	S += c_bb_t20_in >= 46
	c_bb_t20_in += MAS_in[2]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 46
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 46
	c_bb_t20_mem1 += MM_MEM[1]

	c_bb_t31 = S.Task('c_bb_t31', length=2, delay_cost=1)
	S += c_bb_t31 >= 46
	c_bb_t31 += MAS[1]

	c_bc10 = S.Task('c_bc10', length=2, delay_cost=1)
	S += c_bc10 >= 46
	c_bc10 += MAS[2]

	c_bc_s00 = S.Task('c_bc_s00', length=2, delay_cost=1)
	S += c_bc_s00 >= 46
	c_bc_s00 += MAS[3]

	c_bc_s01_in = S.Task('c_bc_s01_in', length=1, delay_cost=1)
	S += c_bc_s01_in >= 46
	c_bc_s01_in += MAS_in[0]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 46
	c_bc_s01_mem0 += MAS_MEM[4]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 46
	c_bc_s01_mem1 += MAS_MEM[1]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 46
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 46
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_aa_t2_t5_in = S.Task('c_aa_t2_t5_in', length=1, delay_cost=1)
	S += c_aa_t2_t5_in >= 47
	c_aa_t2_t5_in += MAS_in[3]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 47
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 47
	c_aa_t2_t5_mem1 += MM_MEM[1]

	c_ab_s00_in = S.Task('c_ab_s00_in', length=1, delay_cost=1)
	S += c_ab_s00_in >= 47
	c_ab_s00_in += MAS_in[2]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 47
	c_ab_s00_mem0 += MAS_MEM[6]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 47
	c_ab_s00_mem1 += MAS_MEM[7]

	c_ab_s01 = S.Task('c_ab_s01', length=2, delay_cost=1)
	S += c_ab_s01 >= 47
	c_ab_s01 += MAS[3]

	c_bb_t20 = S.Task('c_bb_t20', length=2, delay_cost=1)
	S += c_bb_t20 >= 47
	c_bb_t20 += MAS[2]

	c_bb_t40_in = S.Task('c_bb_t40_in', length=1, delay_cost=1)
	S += c_bb_t40_in >= 47
	c_bb_t40_in += MAS_in[1]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 47
	c_bb_t40_mem0 += MAS_MEM[2]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 47
	c_bb_t40_mem1 += MAS_MEM[3]

	c_bc_s01 = S.Task('c_bc_s01', length=2, delay_cost=1)
	S += c_bc_s01 >= 47
	c_bc_s01 += MAS[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 47
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 47
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t51_in = S.Task('c_bc_t51_in', length=1, delay_cost=1)
	S += c_bc_t51_in >= 47
	c_bc_t51_in += MAS_in[0]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 47
	c_bc_t51_mem0 += MAS_MEM[4]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 47
	c_bc_t51_mem1 += MAS_MEM[5]

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=2, delay_cost=1)
	S += c_aa_t2_t5 >= 48
	c_aa_t2_t5 += MAS[3]

	c_aa_t41_in = S.Task('c_aa_t41_in', length=1, delay_cost=1)
	S += c_aa_t41_in >= 48
	c_aa_t41_in += MAS_in[2]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 48
	c_aa_t41_mem0 += MAS_MEM[6]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 48
	c_aa_t41_mem1 += MAS_MEM[7]

	c_ab_s00 = S.Task('c_ab_s00', length=2, delay_cost=1)
	S += c_ab_s00 >= 48
	c_ab_s00 += MAS[2]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 48
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 48
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_bb_t40 = S.Task('c_bb_t40', length=2, delay_cost=1)
	S += c_bb_t40 >= 48
	c_bb_t40 += MAS[1]

	c_bb_t41_in = S.Task('c_bb_t41_in', length=1, delay_cost=1)
	S += c_bb_t41_in >= 48
	c_bb_t41_in += MAS_in[0]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 48
	c_bb_t41_mem0 += MAS_MEM[2]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 48
	c_bb_t41_mem1 += MAS_MEM[3]

	c_bc_t51 = S.Task('c_bc_t51', length=2, delay_cost=1)
	S += c_bc_t51 >= 48
	c_bc_t51 += MAS[0]

	c_cc_t20_in = S.Task('c_cc_t20_in', length=1, delay_cost=1)
	S += c_cc_t20_in >= 48
	c_cc_t20_in += MAS_in[1]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 48
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 48
	c_cc_t20_mem1 += MM_MEM[1]

	c_aa_t20_in = S.Task('c_aa_t20_in', length=1, delay_cost=1)
	S += c_aa_t20_in >= 49
	c_aa_t20_in += MAS_in[2]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 49
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 49
	c_aa_t20_mem1 += MM_MEM[1]

	c_aa_t40_in = S.Task('c_aa_t40_in', length=1, delay_cost=1)
	S += c_aa_t40_in >= 49
	c_aa_t40_in += MAS_in[1]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 49
	c_aa_t40_mem0 += MAS_MEM[6]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 49
	c_aa_t40_mem1 += MAS_MEM[7]

	c_aa_t41 = S.Task('c_aa_t41', length=2, delay_cost=1)
	S += c_aa_t41 >= 49
	c_aa_t41 += MAS[2]

	c_bb11_in = S.Task('c_bb11_in', length=1, delay_cost=1)
	S += c_bb11_in >= 49
	c_bb11_in += MAS_in[3]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 49
	c_bb11_mem0 += MAS_MEM[2]

	c_bb_t41 = S.Task('c_bb_t41', length=2, delay_cost=1)
	S += c_bb_t41 >= 49
	c_bb_t41 += MAS[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 49
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 49
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t20 = S.Task('c_cc_t20', length=2, delay_cost=1)
	S += c_cc_t20 >= 49
	c_cc_t20 += MAS[1]

	c_aa_t20 = S.Task('c_aa_t20', length=2, delay_cost=1)
	S += c_aa_t20 >= 50
	c_aa_t20 += MAS[2]

	c_aa_t40 = S.Task('c_aa_t40', length=2, delay_cost=1)
	S += c_aa_t40 >= 50
	c_aa_t40 += MAS[1]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 50
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb11 = S.Task('c_bb11', length=2, delay_cost=1)
	S += c_bb11 >= 50
	c_bb11 += MAS[3]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 50
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_cc_t2_t5_in = S.Task('c_cc_t2_t5_in', length=1, delay_cost=1)
	S += c_cc_t2_t5_in >= 50
	c_cc_t2_t5_in += MAS_in[1]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 50
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 50
	c_cc_t2_t5_mem1 += MM_MEM[1]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 51
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 51
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t41_in = S.Task('c_ac_t41_in', length=1, delay_cost=1)
	S += c_ac_t41_in >= 51
	c_ac_t41_in += MAS_in[2]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 51
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 51
	c_ac_t41_mem1 += MAS_MEM[3]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=2, delay_cost=1)
	S += c_cc_t2_t5 >= 51
	c_cc_t2_t5 += MAS[1]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 52
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 52
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t41 = S.Task('c_ac_t41', length=2, delay_cost=1)
	S += c_ac_t41 >= 52
	c_ac_t41 += MAS[2]

	c_bc_t41_in = S.Task('c_bc_t41_in', length=1, delay_cost=1)
	S += c_bc_t41_in >= 52
	c_bc_t41_in += MAS_in[3]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 52
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 52
	c_bc_t41_mem1 += MAS_MEM[1]

	c_bb_t2_t5_in = S.Task('c_bb_t2_t5_in', length=1, delay_cost=1)
	S += c_bb_t2_t5_in >= 53
	c_bb_t2_t5_in += MAS_in[1]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 53
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 53
	c_bb_t2_t5_mem1 += MM_MEM[1]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 53
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 53
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t41 = S.Task('c_bc_t41', length=2, delay_cost=1)
	S += c_bc_t41 >= 53
	c_bc_t41 += MAS[3]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 54
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_ab_t41_in = S.Task('c_ab_t41_in', length=1, delay_cost=1)
	S += c_ab_t41_in >= 54
	c_ab_t41_in += MAS_in[2]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 54
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 54
	c_ab_t41_mem1 += MAS_MEM[1]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=2, delay_cost=1)
	S += c_bb_t2_t5 >= 54
	c_bb_t2_t5 += MAS[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 54
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 55
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ab_t41 = S.Task('c_ab_t41', length=2, delay_cost=1)
	S += c_ab_t41 >= 55
	c_ab_t41 += MAS[2]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 55
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 56
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 56
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 57
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 57
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 58
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 58
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 59
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 59
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

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

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 72
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 73
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 74
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 75
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 76
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 77
	c_bb_t01_mem0 += MAIN_MEM_r[0]


	# new tasks
	c_aa_t21 = S.Task('c_aa_t21', length=2, delay_cost=1)
	c_aa_t21 += alt(MAS)
	c_aa_t21_in = S.Task('c_aa_t21_in', length=1, delay_cost=1)
	c_aa_t21_in += alt(MAS_in)
	S += c_aa_t21_in*MAS_in[0]<=c_aa_t21*MAS[0]

	S += c_aa_t21_in*MAS_in[1]<=c_aa_t21*MAS[1]

	S += c_aa_t21_in*MAS_in[2]<=c_aa_t21*MAS[2]

	S += c_aa_t21_in*MAS_in[3]<=c_aa_t21*MAS[3]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	c_aa_t21_mem0 += MM_MEM[0]
	S += 48 < c_aa_t21_mem0
	S += c_aa_t21_mem0 <= c_aa_t21

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	c_aa_t21_mem1 += MAS_MEM[7]
	S += 49 < c_aa_t21_mem1
	S += c_aa_t21_mem1 <= c_aa_t21

	c_aa_t50 = S.Task('c_aa_t50', length=2, delay_cost=1)
	c_aa_t50 += alt(MAS)
	c_aa_t50_in = S.Task('c_aa_t50_in', length=1, delay_cost=1)
	c_aa_t50_in += alt(MAS_in)
	S += c_aa_t50_in*MAS_in[0]<=c_aa_t50*MAS[0]

	S += c_aa_t50_in*MAS_in[1]<=c_aa_t50*MAS[1]

	S += c_aa_t50_in*MAS_in[2]<=c_aa_t50*MAS[2]

	S += c_aa_t50_in*MAS_in[3]<=c_aa_t50*MAS[3]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	c_aa_t50_mem0 += MAS_MEM[6]
	S += 22 < c_aa_t50_mem0
	S += c_aa_t50_mem0 <= c_aa_t50

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	c_aa_t50_mem1 += MAS_MEM[3]
	S += 51 < c_aa_t50_mem1
	S += c_aa_t50_mem1 <= c_aa_t50

	c_aa_t51 = S.Task('c_aa_t51', length=2, delay_cost=1)
	c_aa_t51 += alt(MAS)
	c_aa_t51_in = S.Task('c_aa_t51_in', length=1, delay_cost=1)
	c_aa_t51_in += alt(MAS_in)
	S += c_aa_t51_in*MAS_in[0]<=c_aa_t51*MAS[0]

	S += c_aa_t51_in*MAS_in[1]<=c_aa_t51*MAS[1]

	S += c_aa_t51_in*MAS_in[2]<=c_aa_t51*MAS[2]

	S += c_aa_t51_in*MAS_in[3]<=c_aa_t51*MAS[3]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	c_aa_t51_mem0 += MAS_MEM[6]
	S += 41 < c_aa_t51_mem0
	S += c_aa_t51_mem0 <= c_aa_t51

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	c_aa_t51_mem1 += MAS_MEM[5]
	S += 50 < c_aa_t51_mem1
	S += c_aa_t51_mem1 <= c_aa_t51

	c_bb_t21 = S.Task('c_bb_t21', length=2, delay_cost=1)
	c_bb_t21 += alt(MAS)
	c_bb_t21_in = S.Task('c_bb_t21_in', length=1, delay_cost=1)
	c_bb_t21_in += alt(MAS_in)
	S += c_bb_t21_in*MAS_in[0]<=c_bb_t21*MAS[0]

	S += c_bb_t21_in*MAS_in[1]<=c_bb_t21*MAS[1]

	S += c_bb_t21_in*MAS_in[2]<=c_bb_t21*MAS[2]

	S += c_bb_t21_in*MAS_in[3]<=c_bb_t21*MAS[3]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	c_bb_t21_mem0 += MM_MEM[0]
	S += 49 < c_bb_t21_mem0
	S += c_bb_t21_mem0 <= c_bb_t21

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	c_bb_t21_mem1 += MAS_MEM[3]
	S += 55 < c_bb_t21_mem1
	S += c_bb_t21_mem1 <= c_bb_t21

	c_bb_t50 = S.Task('c_bb_t50', length=2, delay_cost=1)
	c_bb_t50 += alt(MAS)
	c_bb_t50_in = S.Task('c_bb_t50_in', length=1, delay_cost=1)
	c_bb_t50_in += alt(MAS_in)
	S += c_bb_t50_in*MAS_in[0]<=c_bb_t50*MAS[0]

	S += c_bb_t50_in*MAS_in[1]<=c_bb_t50*MAS[1]

	S += c_bb_t50_in*MAS_in[2]<=c_bb_t50*MAS[2]

	S += c_bb_t50_in*MAS_in[3]<=c_bb_t50*MAS[3]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	c_bb_t50_mem0 += MAS_MEM[2]
	S += 18 < c_bb_t50_mem0
	S += c_bb_t50_mem0 <= c_bb_t50

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	c_bb_t50_mem1 += MAS_MEM[3]
	S += 49 < c_bb_t50_mem1
	S += c_bb_t50_mem1 <= c_bb_t50

	c_bb_t51 = S.Task('c_bb_t51', length=2, delay_cost=1)
	c_bb_t51 += alt(MAS)
	c_bb_t51_in = S.Task('c_bb_t51_in', length=1, delay_cost=1)
	c_bb_t51_in += alt(MAS_in)
	S += c_bb_t51_in*MAS_in[0]<=c_bb_t51*MAS[0]

	S += c_bb_t51_in*MAS_in[1]<=c_bb_t51*MAS[1]

	S += c_bb_t51_in*MAS_in[2]<=c_bb_t51*MAS[2]

	S += c_bb_t51_in*MAS_in[3]<=c_bb_t51*MAS[3]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	c_bb_t51_mem0 += MAS_MEM[2]
	S += 47 < c_bb_t51_mem0
	S += c_bb_t51_mem0 <= c_bb_t51

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	c_bb_t51_mem1 += MAS_MEM[1]
	S += 50 < c_bb_t51_mem1
	S += c_bb_t51_mem1 <= c_bb_t51

	c_cc_t21 = S.Task('c_cc_t21', length=2, delay_cost=1)
	c_cc_t21 += alt(MAS)
	c_cc_t21_in = S.Task('c_cc_t21_in', length=1, delay_cost=1)
	c_cc_t21_in += alt(MAS_in)
	S += c_cc_t21_in*MAS_in[0]<=c_cc_t21*MAS[0]

	S += c_cc_t21_in*MAS_in[1]<=c_cc_t21*MAS[1]

	S += c_cc_t21_in*MAS_in[2]<=c_cc_t21*MAS[2]

	S += c_cc_t21_in*MAS_in[3]<=c_cc_t21*MAS[3]

	c_cc_t21_mem0 = S.Task('c_cc_t21_mem0', length=1, delay_cost=1)
	c_cc_t21_mem0 += MM_MEM[0]
	S += 47 < c_cc_t21_mem0
	S += c_cc_t21_mem0 <= c_cc_t21

	c_cc_t21_mem1 = S.Task('c_cc_t21_mem1', length=1, delay_cost=1)
	c_cc_t21_mem1 += MAS_MEM[3]
	S += 52 < c_cc_t21_mem1
	S += c_cc_t21_mem1 <= c_cc_t21

	c_cc_t50 = S.Task('c_cc_t50', length=2, delay_cost=1)
	c_cc_t50 += alt(MAS)
	c_cc_t50_in = S.Task('c_cc_t50_in', length=1, delay_cost=1)
	c_cc_t50_in += alt(MAS_in)
	S += c_cc_t50_in*MAS_in[0]<=c_cc_t50*MAS[0]

	S += c_cc_t50_in*MAS_in[1]<=c_cc_t50*MAS[1]

	S += c_cc_t50_in*MAS_in[2]<=c_cc_t50*MAS[2]

	S += c_cc_t50_in*MAS_in[3]<=c_cc_t50*MAS[3]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	c_cc_t50_mem0 += MAS_MEM[0]
	S += 19 < c_cc_t50_mem0
	S += c_cc_t50_mem0 <= c_cc_t50

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	c_cc_t50_mem1 += MAS_MEM[7]
	S += 37 < c_cc_t50_mem1
	S += c_cc_t50_mem1 <= c_cc_t50

	c_cc_t51 = S.Task('c_cc_t51', length=2, delay_cost=1)
	c_cc_t51 += alt(MAS)
	c_cc_t51_in = S.Task('c_cc_t51_in', length=1, delay_cost=1)
	c_cc_t51_in += alt(MAS_in)
	S += c_cc_t51_in*MAS_in[0]<=c_cc_t51*MAS[0]

	S += c_cc_t51_in*MAS_in[1]<=c_cc_t51*MAS[1]

	S += c_cc_t51_in*MAS_in[2]<=c_cc_t51*MAS[2]

	S += c_cc_t51_in*MAS_in[3]<=c_cc_t51*MAS[3]

	c_cc_t51_mem0 = S.Task('c_cc_t51_mem0', length=1, delay_cost=1)
	c_cc_t51_mem0 += MAS_MEM[2]
	S += 35 < c_cc_t51_mem0
	S += c_cc_t51_mem0 <= c_cc_t51

	c_cc_t51_mem1 = S.Task('c_cc_t51_mem1', length=1, delay_cost=1)
	c_cc_t51_mem1 += MAS_MEM[3]
	S += 40 < c_cc_t51_mem1
	S += c_cc_t51_mem1 <= c_cc_t51

	c_ab00 = S.Task('c_ab00', length=2, delay_cost=1)
	c_ab00 += alt(MAS)
	c_ab00_in = S.Task('c_ab00_in', length=1, delay_cost=1)
	c_ab00_in += alt(MAS_in)
	S += c_ab00_in*MAS_in[0]<=c_ab00*MAS[0]

	S += c_ab00_in*MAS_in[1]<=c_ab00*MAS[1]

	S += c_ab00_in*MAS_in[2]<=c_ab00*MAS[2]

	S += c_ab00_in*MAS_in[3]<=c_ab00*MAS[3]

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	c_ab00_mem0 += MAS_MEM[4]
	S += 28 < c_ab00_mem0
	S += c_ab00_mem0 <= c_ab00

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	c_ab00_mem1 += MAS_MEM[5]
	S += 49 < c_ab00_mem1
	S += c_ab00_mem1 <= c_ab00

	c_ab01 = S.Task('c_ab01', length=2, delay_cost=1)
	c_ab01 += alt(MAS)
	c_ab01_in = S.Task('c_ab01_in', length=1, delay_cost=1)
	c_ab01_in += alt(MAS_in)
	S += c_ab01_in*MAS_in[0]<=c_ab01*MAS[0]

	S += c_ab01_in*MAS_in[1]<=c_ab01*MAS[1]

	S += c_ab01_in*MAS_in[2]<=c_ab01*MAS[2]

	S += c_ab01_in*MAS_in[3]<=c_ab01*MAS[3]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	c_ab01_mem0 += MAS_MEM[6]
	S += 39 < c_ab01_mem0
	S += c_ab01_mem0 <= c_ab01

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	c_ab01_mem1 += MAS_MEM[7]
	S += 48 < c_ab01_mem1
	S += c_ab01_mem1 <= c_ab01

	c_ab11 = S.Task('c_ab11', length=2, delay_cost=1)
	c_ab11 += alt(MAS)
	c_ab11_in = S.Task('c_ab11_in', length=1, delay_cost=1)
	c_ab11_in += alt(MAS_in)
	S += c_ab11_in*MAS_in[0]<=c_ab11*MAS[0]

	S += c_ab11_in*MAS_in[1]<=c_ab11*MAS[1]

	S += c_ab11_in*MAS_in[2]<=c_ab11*MAS[2]

	S += c_ab11_in*MAS_in[3]<=c_ab11*MAS[3]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	c_ab11_mem0 += MAS_MEM[4]
	S += 56 < c_ab11_mem0
	S += c_ab11_mem0 <= c_ab11

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	c_ab11_mem1 += MAS_MEM[1]
	S += 44 < c_ab11_mem1
	S += c_ab11_mem1 <= c_ab11

	c_bc00 = S.Task('c_bc00', length=2, delay_cost=1)
	c_bc00 += alt(MAS)
	c_bc00_in = S.Task('c_bc00_in', length=1, delay_cost=1)
	c_bc00_in += alt(MAS_in)
	S += c_bc00_in*MAS_in[0]<=c_bc00*MAS[0]

	S += c_bc00_in*MAS_in[1]<=c_bc00*MAS[1]

	S += c_bc00_in*MAS_in[2]<=c_bc00*MAS[2]

	S += c_bc00_in*MAS_in[3]<=c_bc00*MAS[3]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	c_bc00_mem0 += MAS_MEM[6]
	S += 30 < c_bc00_mem0
	S += c_bc00_mem0 <= c_bc00

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	c_bc00_mem1 += MAS_MEM[7]
	S += 47 < c_bc00_mem1
	S += c_bc00_mem1 <= c_bc00

	c_bc01 = S.Task('c_bc01', length=2, delay_cost=1)
	c_bc01 += alt(MAS)
	c_bc01_in = S.Task('c_bc01_in', length=1, delay_cost=1)
	c_bc01_in += alt(MAS_in)
	S += c_bc01_in*MAS_in[0]<=c_bc01*MAS[0]

	S += c_bc01_in*MAS_in[1]<=c_bc01*MAS[1]

	S += c_bc01_in*MAS_in[2]<=c_bc01*MAS[2]

	S += c_bc01_in*MAS_in[3]<=c_bc01*MAS[3]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	c_bc01_mem0 += MAS_MEM[4]
	S += 46 < c_bc01_mem0
	S += c_bc01_mem0 <= c_bc01

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	c_bc01_mem1 += MAS_MEM[1]
	S += 48 < c_bc01_mem1
	S += c_bc01_mem1 <= c_bc01

	c_bc11 = S.Task('c_bc11', length=2, delay_cost=1)
	c_bc11 += alt(MAS)
	c_bc11_in = S.Task('c_bc11_in', length=1, delay_cost=1)
	c_bc11_in += alt(MAS_in)
	S += c_bc11_in*MAS_in[0]<=c_bc11*MAS[0]

	S += c_bc11_in*MAS_in[1]<=c_bc11*MAS[1]

	S += c_bc11_in*MAS_in[2]<=c_bc11*MAS[2]

	S += c_bc11_in*MAS_in[3]<=c_bc11*MAS[3]

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	c_bc11_mem0 += MAS_MEM[6]
	S += 54 < c_bc11_mem0
	S += c_bc11_mem0 <= c_bc11

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	c_bc11_mem1 += MAS_MEM[1]
	S += 49 < c_bc11_mem1
	S += c_bc11_mem1 <= c_bc11

	c_ac00 = S.Task('c_ac00', length=2, delay_cost=1)
	c_ac00 += alt(MAS)
	c_ac00_in = S.Task('c_ac00_in', length=1, delay_cost=1)
	c_ac00_in += alt(MAS_in)
	S += c_ac00_in*MAS_in[0]<=c_ac00*MAS[0]

	S += c_ac00_in*MAS_in[1]<=c_ac00*MAS[1]

	S += c_ac00_in*MAS_in[2]<=c_ac00*MAS[2]

	S += c_ac00_in*MAS_in[3]<=c_ac00*MAS[3]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	c_ac00_mem0 += MAS_MEM[4]
	S += 26 < c_ac00_mem0
	S += c_ac00_mem0 <= c_ac00

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	c_ac00_mem1 += MAS_MEM[7]
	S += 45 < c_ac00_mem1
	S += c_ac00_mem1 <= c_ac00

	c_ac01 = S.Task('c_ac01', length=2, delay_cost=1)
	c_ac01 += alt(MAS)
	c_ac01_in = S.Task('c_ac01_in', length=1, delay_cost=1)
	c_ac01_in += alt(MAS_in)
	S += c_ac01_in*MAS_in[0]<=c_ac01*MAS[0]

	S += c_ac01_in*MAS_in[1]<=c_ac01*MAS[1]

	S += c_ac01_in*MAS_in[2]<=c_ac01*MAS[2]

	S += c_ac01_in*MAS_in[3]<=c_ac01*MAS[3]

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	c_ac01_mem0 += MAS_MEM[0]
	S += 40 < c_ac01_mem0
	S += c_ac01_mem0 <= c_ac01

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	c_ac01_mem1 += MAS_MEM[1]
	S += 45 < c_ac01_mem1
	S += c_ac01_mem1 <= c_ac01

	c_ac11 = S.Task('c_ac11', length=2, delay_cost=1)
	c_ac11 += alt(MAS)
	c_ac11_in = S.Task('c_ac11_in', length=1, delay_cost=1)
	c_ac11_in += alt(MAS_in)
	S += c_ac11_in*MAS_in[0]<=c_ac11*MAS[0]

	S += c_ac11_in*MAS_in[1]<=c_ac11*MAS[1]

	S += c_ac11_in*MAS_in[2]<=c_ac11*MAS[2]

	S += c_ac11_in*MAS_in[3]<=c_ac11*MAS[3]

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	c_ac11_mem0 += MAS_MEM[4]
	S += 53 < c_ac11_mem0
	S += c_ac11_mem0 <= c_ac11

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	c_ac11_mem1 += MAS_MEM[1]
	S += 46 < c_ac11_mem1
	S += c_ac11_mem1 <= c_ac11

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=2, delay_cost=1)
	c_ccxi_y1_0 += alt(MAS)
	c_ccxi_y1_0_in = S.Task('c_ccxi_y1_0_in', length=1, delay_cost=1)
	c_ccxi_y1_0_in += alt(MAS_in)
	S += c_ccxi_y1_0_in*MAS_in[0]<=c_ccxi_y1_0*MAS[0]

	S += c_ccxi_y1_0_in*MAS_in[1]<=c_ccxi_y1_0*MAS[1]

	S += c_ccxi_y1_0_in*MAS_in[2]<=c_ccxi_y1_0*MAS[2]

	S += c_ccxi_y1_0_in*MAS_in[3]<=c_ccxi_y1_0*MAS[3]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	c_ccxi_y1_0_mem0 += MAS_MEM[0]
	S += 21 < c_ccxi_y1_0_mem0
	S += c_ccxi_y1_0_mem0 <= c_ccxi_y1_0

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	c_ccxi_y1_0_mem1 += MAS_MEM[3]
	S += 39 < c_ccxi_y1_0_mem1
	S += c_ccxi_y1_0_mem1 <= c_ccxi_y1_0

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=2, delay_cost=1)
	c_ccxi_y1_1 += alt(MAS)
	c_ccxi_y1_1_in = S.Task('c_ccxi_y1_1_in', length=1, delay_cost=1)
	c_ccxi_y1_1_in += alt(MAS_in)
	S += c_ccxi_y1_1_in*MAS_in[0]<=c_ccxi_y1_1*MAS[0]

	S += c_ccxi_y1_1_in*MAS_in[1]<=c_ccxi_y1_1*MAS[1]

	S += c_ccxi_y1_1_in*MAS_in[2]<=c_ccxi_y1_1*MAS[2]

	S += c_ccxi_y1_1_in*MAS_in[3]<=c_ccxi_y1_1*MAS[3]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	c_ccxi_y1_1_mem0 += MAS_MEM[2]
	S += 39 < c_ccxi_y1_1_mem0
	S += c_ccxi_y1_1_mem0 <= c_ccxi_y1_1

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	c_ccxi_y1_1_mem1 += MAS_MEM[1]
	S += 21 < c_ccxi_y1_1_mem1
	S += c_ccxi_y1_1_mem1 <= c_ccxi_y1_1

	c_pc10 = S.Task('c_pc10', length=2, delay_cost=1)
	c_pc10 += alt(MAS)
	c_pc10_in = S.Task('c_pc10_in', length=1, delay_cost=1)
	c_pc10_in += alt(MAS_in)
	S += c_pc10_in*MAS_in[0]<=c_pc10*MAS[0]

	S += c_pc10_in*MAS_in[1]<=c_pc10*MAS[1]

	S += c_pc10_in*MAS_in[2]<=c_pc10*MAS[2]

	S += c_pc10_in*MAS_in[3]<=c_pc10*MAS[3]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	c_pc10_mem0 += MAS_MEM[2]
	S += 20 < c_pc10_mem0
	S += c_pc10_mem0 <= c_pc10

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	c_pc10_mem1 += MAS_MEM[5]
	S += 36 < c_pc10_mem1
	S += c_pc10_mem1 <= c_pc10

	c_aa00 = S.Task('c_aa00', length=2, delay_cost=1)
	c_aa00 += alt(MAS)
	c_aa00_in = S.Task('c_aa00_in', length=1, delay_cost=1)
	c_aa00_in += alt(MAS_in)
	S += c_aa00_in*MAS_in[0]<=c_aa00*MAS[0]

	S += c_aa00_in*MAS_in[1]<=c_aa00*MAS[1]

	S += c_aa00_in*MAS_in[2]<=c_aa00*MAS[2]

	S += c_aa00_in*MAS_in[3]<=c_aa00*MAS[3]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	c_aa00_mem0 += MAS_MEM[4]
	S += 51 < c_aa00_mem0
	S += c_aa00_mem0 <= c_aa00

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	c_aa00_mem1 += alt(MAS_MEM)
	S += (c_aa_t50*MAS[0])-1 < c_aa00_mem1*MAS_MEM[1]
	S += (c_aa_t50*MAS[1])-1 < c_aa00_mem1*MAS_MEM[3]
	S += (c_aa_t50*MAS[2])-1 < c_aa00_mem1*MAS_MEM[5]
	S += (c_aa_t50*MAS[3])-1 < c_aa00_mem1*MAS_MEM[7]
	S += c_aa00_mem1 <= c_aa00

	c_aa01 = S.Task('c_aa01', length=2, delay_cost=1)
	c_aa01 += alt(MAS)
	c_aa01_in = S.Task('c_aa01_in', length=1, delay_cost=1)
	c_aa01_in += alt(MAS_in)
	S += c_aa01_in*MAS_in[0]<=c_aa01*MAS[0]

	S += c_aa01_in*MAS_in[1]<=c_aa01*MAS[1]

	S += c_aa01_in*MAS_in[2]<=c_aa01*MAS[2]

	S += c_aa01_in*MAS_in[3]<=c_aa01*MAS[3]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	c_aa01_mem0 += alt(MAS_MEM)
	S += (c_aa_t21*MAS[0])-1 < c_aa01_mem0*MAS_MEM[0]
	S += (c_aa_t21*MAS[1])-1 < c_aa01_mem0*MAS_MEM[2]
	S += (c_aa_t21*MAS[2])-1 < c_aa01_mem0*MAS_MEM[4]
	S += (c_aa_t21*MAS[3])-1 < c_aa01_mem0*MAS_MEM[6]
	S += c_aa01_mem0 <= c_aa01

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	c_aa01_mem1 += alt(MAS_MEM)
	S += (c_aa_t51*MAS[0])-1 < c_aa01_mem1*MAS_MEM[1]
	S += (c_aa_t51*MAS[1])-1 < c_aa01_mem1*MAS_MEM[3]
	S += (c_aa_t51*MAS[2])-1 < c_aa01_mem1*MAS_MEM[5]
	S += (c_aa_t51*MAS[3])-1 < c_aa01_mem1*MAS_MEM[7]
	S += c_aa01_mem1 <= c_aa01

	c_bb00 = S.Task('c_bb00', length=2, delay_cost=1)
	c_bb00 += alt(MAS)
	c_bb00_in = S.Task('c_bb00_in', length=1, delay_cost=1)
	c_bb00_in += alt(MAS_in)
	S += c_bb00_in*MAS_in[0]<=c_bb00*MAS[0]

	S += c_bb00_in*MAS_in[1]<=c_bb00*MAS[1]

	S += c_bb00_in*MAS_in[2]<=c_bb00*MAS[2]

	S += c_bb00_in*MAS_in[3]<=c_bb00*MAS[3]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	c_bb00_mem0 += MAS_MEM[4]
	S += 48 < c_bb00_mem0
	S += c_bb00_mem0 <= c_bb00

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	c_bb00_mem1 += alt(MAS_MEM)
	S += (c_bb_t50*MAS[0])-1 < c_bb00_mem1*MAS_MEM[1]
	S += (c_bb_t50*MAS[1])-1 < c_bb00_mem1*MAS_MEM[3]
	S += (c_bb_t50*MAS[2])-1 < c_bb00_mem1*MAS_MEM[5]
	S += (c_bb_t50*MAS[3])-1 < c_bb00_mem1*MAS_MEM[7]
	S += c_bb00_mem1 <= c_bb00

	c_bb01 = S.Task('c_bb01', length=2, delay_cost=1)
	c_bb01 += alt(MAS)
	c_bb01_in = S.Task('c_bb01_in', length=1, delay_cost=1)
	c_bb01_in += alt(MAS_in)
	S += c_bb01_in*MAS_in[0]<=c_bb01*MAS[0]

	S += c_bb01_in*MAS_in[1]<=c_bb01*MAS[1]

	S += c_bb01_in*MAS_in[2]<=c_bb01*MAS[2]

	S += c_bb01_in*MAS_in[3]<=c_bb01*MAS[3]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	c_bb01_mem0 += alt(MAS_MEM)
	S += (c_bb_t21*MAS[0])-1 < c_bb01_mem0*MAS_MEM[0]
	S += (c_bb_t21*MAS[1])-1 < c_bb01_mem0*MAS_MEM[2]
	S += (c_bb_t21*MAS[2])-1 < c_bb01_mem0*MAS_MEM[4]
	S += (c_bb_t21*MAS[3])-1 < c_bb01_mem0*MAS_MEM[6]
	S += c_bb01_mem0 <= c_bb01

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	c_bb01_mem1 += alt(MAS_MEM)
	S += (c_bb_t51*MAS[0])-1 < c_bb01_mem1*MAS_MEM[1]
	S += (c_bb_t51*MAS[1])-1 < c_bb01_mem1*MAS_MEM[3]
	S += (c_bb_t51*MAS[2])-1 < c_bb01_mem1*MAS_MEM[5]
	S += (c_bb_t51*MAS[3])-1 < c_bb01_mem1*MAS_MEM[7]
	S += c_bb01_mem1 <= c_bb01

	c_cc00 = S.Task('c_cc00', length=2, delay_cost=1)
	c_cc00 += alt(MAS)
	c_cc00_in = S.Task('c_cc00_in', length=1, delay_cost=1)
	c_cc00_in += alt(MAS_in)
	S += c_cc00_in*MAS_in[0]<=c_cc00*MAS[0]

	S += c_cc00_in*MAS_in[1]<=c_cc00*MAS[1]

	S += c_cc00_in*MAS_in[2]<=c_cc00*MAS[2]

	S += c_cc00_in*MAS_in[3]<=c_cc00*MAS[3]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	c_cc00_mem0 += MAS_MEM[2]
	S += 50 < c_cc00_mem0
	S += c_cc00_mem0 <= c_cc00

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	c_cc00_mem1 += alt(MAS_MEM)
	S += (c_cc_t50*MAS[0])-1 < c_cc00_mem1*MAS_MEM[1]
	S += (c_cc_t50*MAS[1])-1 < c_cc00_mem1*MAS_MEM[3]
	S += (c_cc_t50*MAS[2])-1 < c_cc00_mem1*MAS_MEM[5]
	S += (c_cc_t50*MAS[3])-1 < c_cc00_mem1*MAS_MEM[7]
	S += c_cc00_mem1 <= c_cc00

	c_cc01 = S.Task('c_cc01', length=2, delay_cost=1)
	c_cc01 += alt(MAS)
	c_cc01_in = S.Task('c_cc01_in', length=1, delay_cost=1)
	c_cc01_in += alt(MAS_in)
	S += c_cc01_in*MAS_in[0]<=c_cc01*MAS[0]

	S += c_cc01_in*MAS_in[1]<=c_cc01*MAS[1]

	S += c_cc01_in*MAS_in[2]<=c_cc01*MAS[2]

	S += c_cc01_in*MAS_in[3]<=c_cc01*MAS[3]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	c_cc01_mem0 += alt(MAS_MEM)
	S += (c_cc_t21*MAS[0])-1 < c_cc01_mem0*MAS_MEM[0]
	S += (c_cc_t21*MAS[1])-1 < c_cc01_mem0*MAS_MEM[2]
	S += (c_cc_t21*MAS[2])-1 < c_cc01_mem0*MAS_MEM[4]
	S += (c_cc_t21*MAS[3])-1 < c_cc01_mem0*MAS_MEM[6]
	S += c_cc01_mem0 <= c_cc01

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	c_cc01_mem1 += alt(MAS_MEM)
	S += (c_cc_t51*MAS[0])-1 < c_cc01_mem1*MAS_MEM[1]
	S += (c_cc_t51*MAS[1])-1 < c_cc01_mem1*MAS_MEM[3]
	S += (c_cc_t51*MAS[2])-1 < c_cc01_mem1*MAS_MEM[5]
	S += (c_cc_t51*MAS[3])-1 < c_cc01_mem1*MAS_MEM[7]
	S += c_cc01_mem1 <= c_cc01

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=2, delay_cost=1)
	c_bcxi_y1_0 += alt(MAS)
	c_bcxi_y1_0_in = S.Task('c_bcxi_y1_0_in', length=1, delay_cost=1)
	c_bcxi_y1_0_in += alt(MAS_in)
	S += c_bcxi_y1_0_in*MAS_in[0]<=c_bcxi_y1_0*MAS[0]

	S += c_bcxi_y1_0_in*MAS_in[1]<=c_bcxi_y1_0*MAS[1]

	S += c_bcxi_y1_0_in*MAS_in[2]<=c_bcxi_y1_0*MAS[2]

	S += c_bcxi_y1_0_in*MAS_in[3]<=c_bcxi_y1_0*MAS[3]

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	c_bcxi_y1_0_mem0 += MAS_MEM[4]
	S += 47 < c_bcxi_y1_0_mem0
	S += c_bcxi_y1_0_mem0 <= c_bcxi_y1_0

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	c_bcxi_y1_0_mem1 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_0_mem1*MAS_MEM[1]
	S += (c_bc11*MAS[1])-1 < c_bcxi_y1_0_mem1*MAS_MEM[3]
	S += (c_bc11*MAS[2])-1 < c_bcxi_y1_0_mem1*MAS_MEM[5]
	S += (c_bc11*MAS[3])-1 < c_bcxi_y1_0_mem1*MAS_MEM[7]
	S += c_bcxi_y1_0_mem1 <= c_bcxi_y1_0

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=2, delay_cost=1)
	c_bcxi_y1_1 += alt(MAS)
	c_bcxi_y1_1_in = S.Task('c_bcxi_y1_1_in', length=1, delay_cost=1)
	c_bcxi_y1_1_in += alt(MAS_in)
	S += c_bcxi_y1_1_in*MAS_in[0]<=c_bcxi_y1_1*MAS[0]

	S += c_bcxi_y1_1_in*MAS_in[1]<=c_bcxi_y1_1*MAS[1]

	S += c_bcxi_y1_1_in*MAS_in[2]<=c_bcxi_y1_1*MAS[2]

	S += c_bcxi_y1_1_in*MAS_in[3]<=c_bcxi_y1_1*MAS[3]

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	c_bcxi_y1_1_mem0 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_1_mem0*MAS_MEM[0]
	S += (c_bc11*MAS[1])-1 < c_bcxi_y1_1_mem0*MAS_MEM[2]
	S += (c_bc11*MAS[2])-1 < c_bcxi_y1_1_mem0*MAS_MEM[4]
	S += (c_bc11*MAS[3])-1 < c_bcxi_y1_1_mem0*MAS_MEM[6]
	S += c_bcxi_y1_1_mem0 <= c_bcxi_y1_1

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	c_bcxi_y1_1_mem1 += MAS_MEM[5]
	S += 47 < c_bcxi_y1_1_mem1
	S += c_bcxi_y1_1_mem1 <= c_bcxi_y1_1

	c_pa10 = S.Task('c_pa10', length=2, delay_cost=1)
	c_pa10 += alt(MAS)
	c_pa10_in = S.Task('c_pa10_in', length=1, delay_cost=1)
	c_pa10_in += alt(MAS_in)
	S += c_pa10_in*MAS_in[0]<=c_pa10*MAS[0]

	S += c_pa10_in*MAS_in[1]<=c_pa10*MAS[1]

	S += c_pa10_in*MAS_in[2]<=c_pa10*MAS[2]

	S += c_pa10_in*MAS_in[3]<=c_pa10*MAS[3]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	c_pa10_mem0 += MAS_MEM[6]
	S += 24 < c_pa10_mem0
	S += c_pa10_mem0 <= c_pa10

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	c_pa10_mem1 += alt(MAS_MEM)
	S += (c_bc00*MAS[0])-1 < c_pa10_mem1*MAS_MEM[1]
	S += (c_bc00*MAS[1])-1 < c_pa10_mem1*MAS_MEM[3]
	S += (c_bc00*MAS[2])-1 < c_pa10_mem1*MAS_MEM[5]
	S += (c_bc00*MAS[3])-1 < c_pa10_mem1*MAS_MEM[7]
	S += c_pa10_mem1 <= c_pa10

	c_pa11 = S.Task('c_pa11', length=2, delay_cost=1)
	c_pa11 += alt(MAS)
	c_pa11_in = S.Task('c_pa11_in', length=1, delay_cost=1)
	c_pa11_in += alt(MAS_in)
	S += c_pa11_in*MAS_in[0]<=c_pa11*MAS[0]

	S += c_pa11_in*MAS_in[1]<=c_pa11*MAS[1]

	S += c_pa11_in*MAS_in[2]<=c_pa11*MAS[2]

	S += c_pa11_in*MAS_in[3]<=c_pa11*MAS[3]

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	c_pa11_mem0 += MAS_MEM[0]
	S += 47 < c_pa11_mem0
	S += c_pa11_mem0 <= c_pa11

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	c_pa11_mem1 += alt(MAS_MEM)
	S += (c_bc01*MAS[0])-1 < c_pa11_mem1*MAS_MEM[1]
	S += (c_bc01*MAS[1])-1 < c_pa11_mem1*MAS_MEM[3]
	S += (c_bc01*MAS[2])-1 < c_pa11_mem1*MAS_MEM[5]
	S += (c_bc01*MAS[3])-1 < c_pa11_mem1*MAS_MEM[7]
	S += c_pa11_mem1 <= c_pa11

	c_pb00 = S.Task('c_pb00', length=2, delay_cost=1)
	c_pb00 += alt(MAS)
	c_pb00_in = S.Task('c_pb00_in', length=1, delay_cost=1)
	c_pb00_in += alt(MAS_in)
	S += c_pb00_in*MAS_in[0]<=c_pb00*MAS[0]

	S += c_pb00_in*MAS_in[1]<=c_pb00*MAS[1]

	S += c_pb00_in*MAS_in[2]<=c_pb00*MAS[2]

	S += c_pb00_in*MAS_in[3]<=c_pb00*MAS[3]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	c_pb00_mem0 += alt(MAS_MEM)
	S += (c_ccxi_y1_0*MAS[0])-1 < c_pb00_mem0*MAS_MEM[0]
	S += (c_ccxi_y1_0*MAS[1])-1 < c_pb00_mem0*MAS_MEM[2]
	S += (c_ccxi_y1_0*MAS[2])-1 < c_pb00_mem0*MAS_MEM[4]
	S += (c_ccxi_y1_0*MAS[3])-1 < c_pb00_mem0*MAS_MEM[6]
	S += c_pb00_mem0 <= c_pb00

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	c_pb00_mem1 += alt(MAS_MEM)
	S += (c_ab00*MAS[0])-1 < c_pb00_mem1*MAS_MEM[1]
	S += (c_ab00*MAS[1])-1 < c_pb00_mem1*MAS_MEM[3]
	S += (c_ab00*MAS[2])-1 < c_pb00_mem1*MAS_MEM[5]
	S += (c_ab00*MAS[3])-1 < c_pb00_mem1*MAS_MEM[7]
	S += c_pb00_mem1 <= c_pb00

	c_pb01 = S.Task('c_pb01', length=2, delay_cost=1)
	c_pb01 += alt(MAS)
	c_pb01_in = S.Task('c_pb01_in', length=1, delay_cost=1)
	c_pb01_in += alt(MAS_in)
	S += c_pb01_in*MAS_in[0]<=c_pb01*MAS[0]

	S += c_pb01_in*MAS_in[1]<=c_pb01*MAS[1]

	S += c_pb01_in*MAS_in[2]<=c_pb01*MAS[2]

	S += c_pb01_in*MAS_in[3]<=c_pb01*MAS[3]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	c_pb01_mem0 += alt(MAS_MEM)
	S += (c_ccxi_y1_1*MAS[0])-1 < c_pb01_mem0*MAS_MEM[0]
	S += (c_ccxi_y1_1*MAS[1])-1 < c_pb01_mem0*MAS_MEM[2]
	S += (c_ccxi_y1_1*MAS[2])-1 < c_pb01_mem0*MAS_MEM[4]
	S += (c_ccxi_y1_1*MAS[3])-1 < c_pb01_mem0*MAS_MEM[6]
	S += c_pb01_mem0 <= c_pb01

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	c_pb01_mem1 += alt(MAS_MEM)
	S += (c_ab01*MAS[0])-1 < c_pb01_mem1*MAS_MEM[1]
	S += (c_ab01*MAS[1])-1 < c_pb01_mem1*MAS_MEM[3]
	S += (c_ab01*MAS[2])-1 < c_pb01_mem1*MAS_MEM[5]
	S += (c_ab01*MAS[3])-1 < c_pb01_mem1*MAS_MEM[7]
	S += c_pb01_mem1 <= c_pb01

	c_pc11 = S.Task('c_pc11', length=2, delay_cost=1)
	c_pc11 += alt(MAS)
	c_pc11_in = S.Task('c_pc11_in', length=1, delay_cost=1)
	c_pc11_in += alt(MAS_in)
	S += c_pc11_in*MAS_in[0]<=c_pc11*MAS[0]

	S += c_pc11_in*MAS_in[1]<=c_pc11*MAS[1]

	S += c_pc11_in*MAS_in[2]<=c_pc11*MAS[2]

	S += c_pc11_in*MAS_in[3]<=c_pc11*MAS[3]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	c_pc11_mem0 += MAS_MEM[6]
	S += 51 < c_pc11_mem0
	S += c_pc11_mem0 <= c_pc11

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	c_pc11_mem1 += alt(MAS_MEM)
	S += (c_ac11*MAS[0])-1 < c_pc11_mem1*MAS_MEM[1]
	S += (c_ac11*MAS[1])-1 < c_pc11_mem1*MAS_MEM[3]
	S += (c_ac11*MAS[2])-1 < c_pc11_mem1*MAS_MEM[5]
	S += (c_ac11*MAS[3])-1 < c_pc11_mem1*MAS_MEM[7]
	S += c_pc11_mem1 <= c_pc11

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=5, delay_cost=1)
	c_pcb_t1_t0 += alt(MM)
	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	c_pcb_t1_t0_in += alt(MM_in)
	S += c_pcb_t1_t0_in*MM_in[0]<=c_pcb_t1_t0*MM[0]

	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	c_pcb_t1_t0_mem0 += alt(MAS_MEM)
	S += (c_pc10*MAS[0])-1 < c_pcb_t1_t0_mem0*MAS_MEM[0]
	S += (c_pc10*MAS[1])-1 < c_pcb_t1_t0_mem0*MAS_MEM[2]
	S += (c_pc10*MAS[2])-1 < c_pcb_t1_t0_mem0*MAS_MEM[4]
	S += (c_pc10*MAS[3])-1 < c_pcb_t1_t0_mem0*MAS_MEM[6]
	S += c_pcb_t1_t0_mem0 <= c_pcb_t1_t0

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	c_pcb_t1_t0_mem1 += MAIN_MEM_r[1]
	c_pa00 = S.Task('c_pa00', length=2, delay_cost=1)
	c_pa00 += alt(MAS)
	c_pa00_in = S.Task('c_pa00_in', length=1, delay_cost=1)
	c_pa00_in += alt(MAS_in)
	S += c_pa00_in*MAS_in[0]<=c_pa00*MAS[0]

	S += c_pa00_in*MAS_in[1]<=c_pa00*MAS[1]

	S += c_pa00_in*MAS_in[2]<=c_pa00*MAS[2]

	S += c_pa00_in*MAS_in[3]<=c_pa00*MAS[3]

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	c_pa00_mem0 += alt(MAS_MEM)
	S += (c_aa00*MAS[0])-1 < c_pa00_mem0*MAS_MEM[0]
	S += (c_aa00*MAS[1])-1 < c_pa00_mem0*MAS_MEM[2]
	S += (c_aa00*MAS[2])-1 < c_pa00_mem0*MAS_MEM[4]
	S += (c_aa00*MAS[3])-1 < c_pa00_mem0*MAS_MEM[6]
	S += c_pa00_mem0 <= c_pa00

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	c_pa00_mem1 += alt(MAS_MEM)
	S += (c_bcxi_y1_0*MAS[0])-1 < c_pa00_mem1*MAS_MEM[1]
	S += (c_bcxi_y1_0*MAS[1])-1 < c_pa00_mem1*MAS_MEM[3]
	S += (c_bcxi_y1_0*MAS[2])-1 < c_pa00_mem1*MAS_MEM[5]
	S += (c_bcxi_y1_0*MAS[3])-1 < c_pa00_mem1*MAS_MEM[7]
	S += c_pa00_mem1 <= c_pa00

	c_pa01 = S.Task('c_pa01', length=2, delay_cost=1)
	c_pa01 += alt(MAS)
	c_pa01_in = S.Task('c_pa01_in', length=1, delay_cost=1)
	c_pa01_in += alt(MAS_in)
	S += c_pa01_in*MAS_in[0]<=c_pa01*MAS[0]

	S += c_pa01_in*MAS_in[1]<=c_pa01*MAS[1]

	S += c_pa01_in*MAS_in[2]<=c_pa01*MAS[2]

	S += c_pa01_in*MAS_in[3]<=c_pa01*MAS[3]

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	c_pa01_mem0 += alt(MAS_MEM)
	S += (c_aa01*MAS[0])-1 < c_pa01_mem0*MAS_MEM[0]
	S += (c_aa01*MAS[1])-1 < c_pa01_mem0*MAS_MEM[2]
	S += (c_aa01*MAS[2])-1 < c_pa01_mem0*MAS_MEM[4]
	S += (c_aa01*MAS[3])-1 < c_pa01_mem0*MAS_MEM[6]
	S += c_pa01_mem0 <= c_pa01

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	c_pa01_mem1 += alt(MAS_MEM)
	S += (c_bcxi_y1_1*MAS[0])-1 < c_pa01_mem1*MAS_MEM[1]
	S += (c_bcxi_y1_1*MAS[1])-1 < c_pa01_mem1*MAS_MEM[3]
	S += (c_bcxi_y1_1*MAS[2])-1 < c_pa01_mem1*MAS_MEM[5]
	S += (c_bcxi_y1_1*MAS[3])-1 < c_pa01_mem1*MAS_MEM[7]
	S += c_pa01_mem1 <= c_pa01

	c_pb10 = S.Task('c_pb10', length=2, delay_cost=1)
	c_pb10 += alt(MAS)
	c_pb10_in = S.Task('c_pb10_in', length=1, delay_cost=1)
	c_pb10_in += alt(MAS_in)
	S += c_pb10_in*MAS_in[0]<=c_pb10*MAS[0]

	S += c_pb10_in*MAS_in[1]<=c_pb10*MAS[1]

	S += c_pb10_in*MAS_in[2]<=c_pb10*MAS[2]

	S += c_pb10_in*MAS_in[3]<=c_pb10*MAS[3]

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	c_pb10_mem0 += alt(MAS_MEM)
	S += (c_cc00*MAS[0])-1 < c_pb10_mem0*MAS_MEM[0]
	S += (c_cc00*MAS[1])-1 < c_pb10_mem0*MAS_MEM[2]
	S += (c_cc00*MAS[2])-1 < c_pb10_mem0*MAS_MEM[4]
	S += (c_cc00*MAS[3])-1 < c_pb10_mem0*MAS_MEM[6]
	S += c_pb10_mem0 <= c_pb10

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	c_pb10_mem1 += MAS_MEM[7]
	S += 40 < c_pb10_mem1
	S += c_pb10_mem1 <= c_pb10

	c_pb11 = S.Task('c_pb11', length=2, delay_cost=1)
	c_pb11 += alt(MAS)
	c_pb11_in = S.Task('c_pb11_in', length=1, delay_cost=1)
	c_pb11_in += alt(MAS_in)
	S += c_pb11_in*MAS_in[0]<=c_pb11*MAS[0]

	S += c_pb11_in*MAS_in[1]<=c_pb11*MAS[1]

	S += c_pb11_in*MAS_in[2]<=c_pb11*MAS[2]

	S += c_pb11_in*MAS_in[3]<=c_pb11*MAS[3]

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	c_pb11_mem0 += alt(MAS_MEM)
	S += (c_cc01*MAS[0])-1 < c_pb11_mem0*MAS_MEM[0]
	S += (c_cc01*MAS[1])-1 < c_pb11_mem0*MAS_MEM[2]
	S += (c_cc01*MAS[2])-1 < c_pb11_mem0*MAS_MEM[4]
	S += (c_cc01*MAS[3])-1 < c_pb11_mem0*MAS_MEM[6]
	S += c_pb11_mem0 <= c_pb11

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	c_pb11_mem1 += alt(MAS_MEM)
	S += (c_ab11*MAS[0])-1 < c_pb11_mem1*MAS_MEM[1]
	S += (c_ab11*MAS[1])-1 < c_pb11_mem1*MAS_MEM[3]
	S += (c_ab11*MAS[2])-1 < c_pb11_mem1*MAS_MEM[5]
	S += (c_ab11*MAS[3])-1 < c_pb11_mem1*MAS_MEM[7]
	S += c_pb11_mem1 <= c_pb11

	c_pc00 = S.Task('c_pc00', length=2, delay_cost=1)
	c_pc00 += alt(MAS)
	c_pc00_in = S.Task('c_pc00_in', length=1, delay_cost=1)
	c_pc00_in += alt(MAS_in)
	S += c_pc00_in*MAS_in[0]<=c_pc00*MAS[0]

	S += c_pc00_in*MAS_in[1]<=c_pc00*MAS[1]

	S += c_pc00_in*MAS_in[2]<=c_pc00*MAS[2]

	S += c_pc00_in*MAS_in[3]<=c_pc00*MAS[3]

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	c_pc00_mem0 += alt(MAS_MEM)
	S += (c_bb00*MAS[0])-1 < c_pc00_mem0*MAS_MEM[0]
	S += (c_bb00*MAS[1])-1 < c_pc00_mem0*MAS_MEM[2]
	S += (c_bb00*MAS[2])-1 < c_pc00_mem0*MAS_MEM[4]
	S += (c_bb00*MAS[3])-1 < c_pc00_mem0*MAS_MEM[6]
	S += c_pc00_mem0 <= c_pc00

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	c_pc00_mem1 += alt(MAS_MEM)
	S += (c_ac00*MAS[0])-1 < c_pc00_mem1*MAS_MEM[1]
	S += (c_ac00*MAS[1])-1 < c_pc00_mem1*MAS_MEM[3]
	S += (c_ac00*MAS[2])-1 < c_pc00_mem1*MAS_MEM[5]
	S += (c_ac00*MAS[3])-1 < c_pc00_mem1*MAS_MEM[7]
	S += c_pc00_mem1 <= c_pc00

	c_pc01 = S.Task('c_pc01', length=2, delay_cost=1)
	c_pc01 += alt(MAS)
	c_pc01_in = S.Task('c_pc01_in', length=1, delay_cost=1)
	c_pc01_in += alt(MAS_in)
	S += c_pc01_in*MAS_in[0]<=c_pc01*MAS[0]

	S += c_pc01_in*MAS_in[1]<=c_pc01*MAS[1]

	S += c_pc01_in*MAS_in[2]<=c_pc01*MAS[2]

	S += c_pc01_in*MAS_in[3]<=c_pc01*MAS[3]

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	c_pc01_mem0 += alt(MAS_MEM)
	S += (c_bb01*MAS[0])-1 < c_pc01_mem0*MAS_MEM[0]
	S += (c_bb01*MAS[1])-1 < c_pc01_mem0*MAS_MEM[2]
	S += (c_bb01*MAS[2])-1 < c_pc01_mem0*MAS_MEM[4]
	S += (c_bb01*MAS[3])-1 < c_pc01_mem0*MAS_MEM[6]
	S += c_pc01_mem0 <= c_pc01

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	c_pc01_mem1 += alt(MAS_MEM)
	S += (c_ac01*MAS[0])-1 < c_pc01_mem1*MAS_MEM[1]
	S += (c_ac01*MAS[1])-1 < c_pc01_mem1*MAS_MEM[3]
	S += (c_ac01*MAS[2])-1 < c_pc01_mem1*MAS_MEM[5]
	S += (c_ac01*MAS[3])-1 < c_pc01_mem1*MAS_MEM[7]
	S += c_pc01_mem1 <= c_pc01

	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=5, delay_cost=1)
	c_pbc_t0_t0 += alt(MM)
	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	c_pbc_t0_t0_in += alt(MM_in)
	S += c_pbc_t0_t0_in*MM_in[0]<=c_pbc_t0_t0*MM[0]

	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	c_pbc_t0_t0_mem0 += alt(MAS_MEM)
	S += (c_pb00*MAS[0])-1 < c_pbc_t0_t0_mem0*MAS_MEM[0]
	S += (c_pb00*MAS[1])-1 < c_pbc_t0_t0_mem0*MAS_MEM[2]
	S += (c_pb00*MAS[2])-1 < c_pbc_t0_t0_mem0*MAS_MEM[4]
	S += (c_pb00*MAS[3])-1 < c_pbc_t0_t0_mem0*MAS_MEM[6]
	S += c_pbc_t0_t0_mem0 <= c_pbc_t0_t0

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	c_pbc_t0_t0_mem1 += MAIN_MEM_r[1]
	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=5, delay_cost=1)
	c_pbc_t0_t1 += alt(MM)
	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	c_pbc_t0_t1_in += alt(MM_in)
	S += c_pbc_t0_t1_in*MM_in[0]<=c_pbc_t0_t1*MM[0]

	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	c_pbc_t0_t1_mem0 += alt(MAS_MEM)
	S += (c_pb01*MAS[0])-1 < c_pbc_t0_t1_mem0*MAS_MEM[0]
	S += (c_pb01*MAS[1])-1 < c_pbc_t0_t1_mem0*MAS_MEM[2]
	S += (c_pb01*MAS[2])-1 < c_pbc_t0_t1_mem0*MAS_MEM[4]
	S += (c_pb01*MAS[3])-1 < c_pbc_t0_t1_mem0*MAS_MEM[6]
	S += c_pbc_t0_t1_mem0 <= c_pbc_t0_t1

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	c_pbc_t0_t1_mem1 += MAIN_MEM_r[1]
	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=2, delay_cost=1)
	c_pbc_t0_t2 += alt(MAS)
	c_pbc_t0_t2_in = S.Task('c_pbc_t0_t2_in', length=1, delay_cost=1)
	c_pbc_t0_t2_in += alt(MAS_in)
	S += c_pbc_t0_t2_in*MAS_in[0]<=c_pbc_t0_t2*MAS[0]

	S += c_pbc_t0_t2_in*MAS_in[1]<=c_pbc_t0_t2*MAS[1]

	S += c_pbc_t0_t2_in*MAS_in[2]<=c_pbc_t0_t2*MAS[2]

	S += c_pbc_t0_t2_in*MAS_in[3]<=c_pbc_t0_t2*MAS[3]

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	c_pbc_t0_t2_mem0 += alt(MAS_MEM)
	S += (c_pb00*MAS[0])-1 < c_pbc_t0_t2_mem0*MAS_MEM[0]
	S += (c_pb00*MAS[1])-1 < c_pbc_t0_t2_mem0*MAS_MEM[2]
	S += (c_pb00*MAS[2])-1 < c_pbc_t0_t2_mem0*MAS_MEM[4]
	S += (c_pb00*MAS[3])-1 < c_pbc_t0_t2_mem0*MAS_MEM[6]
	S += c_pbc_t0_t2_mem0 <= c_pbc_t0_t2

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	c_pbc_t0_t2_mem1 += alt(MAS_MEM)
	S += (c_pb01*MAS[0])-1 < c_pbc_t0_t2_mem1*MAS_MEM[1]
	S += (c_pb01*MAS[1])-1 < c_pbc_t0_t2_mem1*MAS_MEM[3]
	S += (c_pb01*MAS[2])-1 < c_pbc_t0_t2_mem1*MAS_MEM[5]
	S += (c_pb01*MAS[3])-1 < c_pbc_t0_t2_mem1*MAS_MEM[7]
	S += c_pbc_t0_t2_mem1 <= c_pbc_t0_t2

	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=5, delay_cost=1)
	c_pcb_t1_t1 += alt(MM)
	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	c_pcb_t1_t1_in += alt(MM_in)
	S += c_pcb_t1_t1_in*MM_in[0]<=c_pcb_t1_t1*MM[0]

	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	c_pcb_t1_t1_mem0 += alt(MAS_MEM)
	S += (c_pc11*MAS[0])-1 < c_pcb_t1_t1_mem0*MAS_MEM[0]
	S += (c_pc11*MAS[1])-1 < c_pcb_t1_t1_mem0*MAS_MEM[2]
	S += (c_pc11*MAS[2])-1 < c_pcb_t1_t1_mem0*MAS_MEM[4]
	S += (c_pc11*MAS[3])-1 < c_pcb_t1_t1_mem0*MAS_MEM[6]
	S += c_pcb_t1_t1_mem0 <= c_pcb_t1_t1

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	c_pcb_t1_t1_mem1 += MAIN_MEM_r[1]
	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=2, delay_cost=1)
	c_pcb_t1_t2 += alt(MAS)
	c_pcb_t1_t2_in = S.Task('c_pcb_t1_t2_in', length=1, delay_cost=1)
	c_pcb_t1_t2_in += alt(MAS_in)
	S += c_pcb_t1_t2_in*MAS_in[0]<=c_pcb_t1_t2*MAS[0]

	S += c_pcb_t1_t2_in*MAS_in[1]<=c_pcb_t1_t2*MAS[1]

	S += c_pcb_t1_t2_in*MAS_in[2]<=c_pcb_t1_t2*MAS[2]

	S += c_pcb_t1_t2_in*MAS_in[3]<=c_pcb_t1_t2*MAS[3]

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	c_pcb_t1_t2_mem0 += alt(MAS_MEM)
	S += (c_pc10*MAS[0])-1 < c_pcb_t1_t2_mem0*MAS_MEM[0]
	S += (c_pc10*MAS[1])-1 < c_pcb_t1_t2_mem0*MAS_MEM[2]
	S += (c_pc10*MAS[2])-1 < c_pcb_t1_t2_mem0*MAS_MEM[4]
	S += (c_pc10*MAS[3])-1 < c_pcb_t1_t2_mem0*MAS_MEM[6]
	S += c_pcb_t1_t2_mem0 <= c_pcb_t1_t2

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	c_pcb_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pc11*MAS[0])-1 < c_pcb_t1_t2_mem1*MAS_MEM[1]
	S += (c_pc11*MAS[1])-1 < c_pcb_t1_t2_mem1*MAS_MEM[3]
	S += (c_pc11*MAS[2])-1 < c_pcb_t1_t2_mem1*MAS_MEM[5]
	S += (c_pc11*MAS[3])-1 < c_pcb_t1_t2_mem1*MAS_MEM[7]
	S += c_pcb_t1_t2_mem1 <= c_pcb_t1_t2

	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=5, delay_cost=1)
	c_paa_t1_t0 += alt(MM)
	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	c_paa_t1_t0_in += alt(MM_in)
	S += c_paa_t1_t0_in*MM_in[0]<=c_paa_t1_t0*MM[0]

	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	c_paa_t1_t0_mem0 += alt(MAS_MEM)
	S += (c_pa10*MAS[0])-1 < c_paa_t1_t0_mem0*MAS_MEM[0]
	S += (c_pa10*MAS[1])-1 < c_paa_t1_t0_mem0*MAS_MEM[2]
	S += (c_pa10*MAS[2])-1 < c_paa_t1_t0_mem0*MAS_MEM[4]
	S += (c_pa10*MAS[3])-1 < c_paa_t1_t0_mem0*MAS_MEM[6]
	S += c_paa_t1_t0_mem0 <= c_paa_t1_t0

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	c_paa_t1_t0_mem1 += MAIN_MEM_r[1]
	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=5, delay_cost=1)
	c_paa_t1_t1 += alt(MM)
	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	c_paa_t1_t1_in += alt(MM_in)
	S += c_paa_t1_t1_in*MM_in[0]<=c_paa_t1_t1*MM[0]

	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	c_paa_t1_t1_mem0 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t1_t1_mem0*MAS_MEM[0]
	S += (c_pa11*MAS[1])-1 < c_paa_t1_t1_mem0*MAS_MEM[2]
	S += (c_pa11*MAS[2])-1 < c_paa_t1_t1_mem0*MAS_MEM[4]
	S += (c_pa11*MAS[3])-1 < c_paa_t1_t1_mem0*MAS_MEM[6]
	S += c_paa_t1_t1_mem0 <= c_paa_t1_t1

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	c_paa_t1_t1_mem1 += MAIN_MEM_r[1]
	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=2, delay_cost=1)
	c_paa_t1_t2 += alt(MAS)
	c_paa_t1_t2_in = S.Task('c_paa_t1_t2_in', length=1, delay_cost=1)
	c_paa_t1_t2_in += alt(MAS_in)
	S += c_paa_t1_t2_in*MAS_in[0]<=c_paa_t1_t2*MAS[0]

	S += c_paa_t1_t2_in*MAS_in[1]<=c_paa_t1_t2*MAS[1]

	S += c_paa_t1_t2_in*MAS_in[2]<=c_paa_t1_t2*MAS[2]

	S += c_paa_t1_t2_in*MAS_in[3]<=c_paa_t1_t2*MAS[3]

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	c_paa_t1_t2_mem0 += alt(MAS_MEM)
	S += (c_pa10*MAS[0])-1 < c_paa_t1_t2_mem0*MAS_MEM[0]
	S += (c_pa10*MAS[1])-1 < c_paa_t1_t2_mem0*MAS_MEM[2]
	S += (c_pa10*MAS[2])-1 < c_paa_t1_t2_mem0*MAS_MEM[4]
	S += (c_pa10*MAS[3])-1 < c_paa_t1_t2_mem0*MAS_MEM[6]
	S += c_paa_t1_t2_mem0 <= c_paa_t1_t2

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	c_paa_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t1_t2_mem1*MAS_MEM[1]
	S += (c_pa11*MAS[1])-1 < c_paa_t1_t2_mem1*MAS_MEM[3]
	S += (c_pa11*MAS[2])-1 < c_paa_t1_t2_mem1*MAS_MEM[5]
	S += (c_pa11*MAS[3])-1 < c_paa_t1_t2_mem1*MAS_MEM[7]
	S += c_paa_t1_t2_mem1 <= c_paa_t1_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage2MAS4/FP12_INV_BEFORE_FPINV/schedule6.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

