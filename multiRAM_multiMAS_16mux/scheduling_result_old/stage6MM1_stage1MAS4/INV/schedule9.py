from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 191
	S = Scenario("schedule9", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 0
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 0
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 0
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=6, delay_cost=1)
	S += c_aa_t3_t0 >= 1
	c_aa_t3_t0 += MM[0]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 1
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 1
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 1
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 2
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 2
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 2
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=6, delay_cost=1)
	S += c_bb_t3_t1 >= 2
	c_bb_t3_t1 += MM[0]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=6, delay_cost=1)
	S += c_aa_t3_t1 >= 3
	c_aa_t3_t1 += MM[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 3
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 3
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 3
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 4
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 4
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=6, delay_cost=1)
	S += c_bb_t3_t0 >= 4
	c_bb_t3_t0 += MM[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	S += c_aa_t3_t3 >= 5
	c_aa_t3_t3 += MAS[3]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 5
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 5
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 6
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 6
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t11 = S.Task('c_bb_t11', length=1, delay_cost=1)
	S += c_bb_t11 >= 6
	c_bb_t11 += MAS[0]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	S += c_aa_t3_t2 >= 7
	c_aa_t3_t2 += MAS[3]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 7
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 7
	c_aa_t3_t4_mem0 += MAS_MEM[6]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 7
	c_aa_t3_t4_mem1 += MAS_MEM[7]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 7
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 7
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 8
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 8
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=6, delay_cost=1)
	S += c_aa_t3_t4 >= 8
	c_aa_t3_t4 += MM[0]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 8
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 8
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	S += c_bb_a1_1 >= 8
	c_bb_a1_1 += MAS[0]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	S += c_aa_a1_1 >= 9
	c_aa_a1_1 += MAS[0]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 9
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 9
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=1, delay_cost=1)
	S += c_aa_t3_t5 >= 9
	c_aa_t3_t5 += MAS[1]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 9
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 9
	c_bb_t30_mem1 += MM_MEM[1]

	c_aa_t11 = S.Task('c_aa_t11', length=1, delay_cost=1)
	S += c_aa_t11 >= 10
	c_aa_t11 += MAS[0]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 10
	c_bb10_mem0 += MAS_MEM[4]

	c_bb10_mem1 = S.Task('c_bb10_mem1', length=1, delay_cost=1)
	S += c_bb10_mem1 >= 10
	c_bb10_mem1 += MAS_MEM[5]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 10
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 10
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t30 = S.Task('c_bb_t30', length=1, delay_cost=1)
	S += c_bb_t30 >= 10
	c_bb_t30 += MAS[2]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 10
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 10
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 11
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 11
	c_aa_t30_mem1 += MM_MEM[1]

	c_bb10 = S.Task('c_bb10', length=1, delay_cost=1)
	S += c_bb10 >= 11
	c_bb10 += MAS[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	S += c_bb_a1_0 >= 11
	c_bb_a1_0 += MAS[0]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=1, delay_cost=1)
	S += c_bb_t3_t5 >= 11
	c_bb_t3_t5 += MAS[3]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 11
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 11
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 12
	c_aa10_mem0 += MAS_MEM[4]

	c_aa10_mem1 = S.Task('c_aa10_mem1', length=1, delay_cost=1)
	S += c_aa10_mem1 >= 12
	c_aa10_mem1 += MAS_MEM[5]

	c_aa_t30 = S.Task('c_aa_t30', length=1, delay_cost=1)
	S += c_aa_t30 >= 12
	c_aa_t30 += MAS[2]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 12
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 12
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=1, delay_cost=1)
	S += c_cc_t11 >= 12
	c_cc_t11 += MAS[0]

	c_aa10 = S.Task('c_aa10', length=1, delay_cost=1)
	S += c_aa10 >= 13
	c_aa10 += MAS[1]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 13
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 13
	c_aa_t31_mem1 += MAS_MEM[3]

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	S += c_bb_t10 >= 13
	c_bb_t10 += MAS[0]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 13
	c_bb_t2_t3_mem0 += MAS_MEM[0]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 13
	c_bb_t2_t3_mem1 += MAS_MEM[1]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 13
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 13
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t31 = S.Task('c_aa_t31', length=1, delay_cost=1)
	S += c_aa_t31 >= 14
	c_aa_t31 += MAS[2]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 14
	c_aa_t41_mem0 += MAS_MEM[4]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 14
	c_aa_t41_mem1 += MAS_MEM[5]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=1, delay_cost=1)
	S += c_bb_t2_t3 >= 14
	c_bb_t2_t3 += MAS[0]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 14
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 14
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=1, delay_cost=1)
	S += c_cc_a1_1 >= 14
	c_cc_a1_1 += MAS[1]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 15
	c_aa_t40_mem0 += MAS_MEM[4]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 15
	c_aa_t40_mem1 += MAS_MEM[5]

	c_aa_t41 = S.Task('c_aa_t41', length=1, delay_cost=1)
	S += c_aa_t41 >= 15
	c_aa_t41 += MAS[2]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=1, delay_cost=1)
	S += c_bb_t3_t3 >= 15
	c_bb_t3_t3 += MAS[3]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 15
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 15
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 16
	c_aa11_mem0 += MAS_MEM[4]

	c_aa11_mem1 = S.Task('c_aa11_mem1', length=1, delay_cost=1)
	S += c_aa11_mem1 >= 16
	c_aa11_mem1 += MAS_MEM[5]

	c_aa_t40 = S.Task('c_aa_t40', length=1, delay_cost=1)
	S += c_aa_t40 >= 16
	c_aa_t40 += MAS[1]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 16
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 16
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	S += c_cc_t10 >= 16
	c_cc_t10 += MAS[0]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 16
	c_cc_t2_t3_mem0 += MAS_MEM[0]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 16
	c_cc_t2_t3_mem1 += MAS_MEM[1]

	c_aa11 = S.Task('c_aa11', length=1, delay_cost=1)
	S += c_aa11 >= 17
	c_aa11 += MAS[2]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	S += c_aa_t50_mem0 >= 17
	c_aa_t50_mem0 += MAS_MEM[4]

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	S += c_aa_t50_mem1 >= 17
	c_aa_t50_mem1 += MAS_MEM[3]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 17
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 17
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=1, delay_cost=1)
	S += c_cc_a1_0 >= 17
	c_cc_a1_0 += MAS[0]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=1, delay_cost=1)
	S += c_cc_t2_t3 >= 17
	c_cc_t2_t3 += MAS[1]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 18
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 18
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t50 = S.Task('c_aa_t50', length=1, delay_cost=1)
	S += c_aa_t50 >= 18
	c_aa_t50 += MAS[3]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	S += c_aa_t51_mem0 >= 18
	c_aa_t51_mem0 += MAS_MEM[4]

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	S += c_aa_t51_mem1 >= 18
	c_aa_t51_mem1 += MAS_MEM[5]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=1, delay_cost=1)
	S += c_bb_t3_t2 >= 18
	c_bb_t3_t2 += MAS[0]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 18
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 18
	c_bb_t3_t4_mem0 += MAS_MEM[0]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 18
	c_bb_t3_t4_mem1 += MAS_MEM[7]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	S += c_aa_a1_0 >= 19
	c_aa_a1_0 += MAS[2]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 19
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 19
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t51 = S.Task('c_aa_t51', length=1, delay_cost=1)
	S += c_aa_t51 >= 19
	c_aa_t51 += MAS[0]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=6, delay_cost=1)
	S += c_bb_t3_t4 >= 19
	c_bb_t3_t4 += MM[0]

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	S += c_aa_t10 >= 20
	c_aa_t10 += MAS[0]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 20
	c_aa_t2_t3_mem0 += MAS_MEM[0]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 20
	c_aa_t2_t3_mem1 += MAS_MEM[1]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 20
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 20
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 20
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=1, delay_cost=1)
	S += c_aa_t2_t3 >= 21
	c_aa_t2_t3 += MAS[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 21
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 21
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 21
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=6, delay_cost=1)
	S += c_bc_t0_t1 >= 21
	c_bc_t0_t1 += MM[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 22
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 22
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 22
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=6, delay_cost=1)
	S += c_ab_t1_t1 >= 22
	c_ab_t1_t1 += MM[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=6, delay_cost=1)
	S += c_ab_t0_t1 >= 23
	c_ab_t0_t1 += MM[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 23
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 23
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 23
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=6, delay_cost=1)
	S += c_ab_t1_t0 >= 24
	c_ab_t1_t0 += MM[0]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 24
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 24
	c_bb_t31_mem1 += MAS_MEM[7]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 24
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 24
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 24
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t31 = S.Task('c_bb_t31', length=1, delay_cost=1)
	S += c_bb_t31 >= 25
	c_bb_t31 += MAS[0]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 25
	c_bb_t40_mem0 += MAS_MEM[4]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 25
	c_bb_t40_mem1 += MAS_MEM[1]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 25
	c_bb_t41_mem0 += MAS_MEM[0]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 25
	c_bb_t41_mem1 += MAS_MEM[5]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 25
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 25
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 25
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=6, delay_cost=1)
	S += c_cc_t3_t1 >= 25
	c_cc_t3_t1 += MM[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 26
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 26
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 26
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 26
	c_bb11_mem0 += MAS_MEM[0]

	c_bb11_mem1 = S.Task('c_bb11_mem1', length=1, delay_cost=1)
	S += c_bb11_mem1 >= 26
	c_bb11_mem1 += MAS_MEM[1]

	c_bb_t40 = S.Task('c_bb_t40', length=1, delay_cost=1)
	S += c_bb_t40 >= 26
	c_bb_t40 += MAS[1]

	c_bb_t41 = S.Task('c_bb_t41', length=1, delay_cost=1)
	S += c_bb_t41 >= 26
	c_bb_t41 += MAS[0]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	S += c_bb_t50_mem0 >= 26
	c_bb_t50_mem0 += MAS_MEM[4]

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	S += c_bb_t50_mem1 >= 26
	c_bb_t50_mem1 += MAS_MEM[3]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=6, delay_cost=1)
	S += c_cc_t3_t0 >= 26
	c_cc_t3_t0 += MM[0]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=6, delay_cost=1)
	S += c_ab_t0_t0 >= 27
	c_ab_t0_t0 += MM[0]

	c_bb11 = S.Task('c_bb11', length=1, delay_cost=1)
	S += c_bb11 >= 27
	c_bb11 += MAS[0]

	c_bb_t50 = S.Task('c_bb_t50', length=1, delay_cost=1)
	S += c_bb_t50 >= 27
	c_bb_t50 += MAS[1]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	S += c_bb_t51_mem0 >= 27
	c_bb_t51_mem0 += MAS_MEM[0]

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	S += c_bb_t51_mem1 >= 27
	c_bb_t51_mem1 += MAS_MEM[1]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 27
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 27
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 27
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 28
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 28
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t51 = S.Task('c_bb_t51', length=1, delay_cost=1)
	S += c_bb_t51 >= 28
	c_bb_t51 += MAS[0]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=6, delay_cost=1)
	S += c_bc_t0_t0 >= 28
	c_bc_t0_t0 += MM[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=1, delay_cost=1)
	S += c_ab_t1_t2 >= 29
	c_ab_t1_t2 += MAS[2]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 29
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 29
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 29
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 29
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 30
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 30
	c_ab_t10_mem1 += MM_MEM[1]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=1, delay_cost=1)
	S += c_ab_t1_t5 >= 30
	c_ab_t1_t5 += MAS[0]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=1, delay_cost=1)
	S += c_bc_t0_t2 >= 30
	c_bc_t0_t2 += MAS[2]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 30
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 30
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t10 = S.Task('c_ab_t10', length=1, delay_cost=1)
	S += c_ab_t10 >= 31
	c_ab_t10 += MAS[1]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=1, delay_cost=1)
	S += c_bc_t0_t3 >= 31
	c_bc_t0_t3 += MAS[0]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 31
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 31
	c_bc_t0_t4_mem0 += MAS_MEM[4]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 31
	c_bc_t0_t4_mem1 += MAS_MEM[1]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 31
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 31
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 31
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 31
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 32
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 32
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 32
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 32
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=6, delay_cost=1)
	S += c_bc_t0_t4 >= 32
	c_bc_t0_t4 += MM[0]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	S += c_cc_t3_t3 >= 32
	c_cc_t3_t3 += MAS[1]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=1, delay_cost=1)
	S += c_cc_t3_t5 >= 32
	c_cc_t3_t5 += MAS[0]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=1, delay_cost=1)
	S += c_ab_t0_t5 >= 33
	c_ab_t0_t5 += MAS[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 33
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 33
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t31 = S.Task('c_ab_t31', length=1, delay_cost=1)
	S += c_ab_t31 >= 33
	c_ab_t31 += MAS[2]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 33
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 33
	c_bc_t00_mem1 += MM_MEM[1]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 34
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 34
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t20 = S.Task('c_ab_t20', length=1, delay_cost=1)
	S += c_ab_t20 >= 34
	c_ab_t20 += MAS[2]

	c_bc_t00 = S.Task('c_bc_t00', length=1, delay_cost=1)
	S += c_bc_t00 >= 34
	c_bc_t00 += MAS[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 34
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 34
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 35
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 35
	c_ab_t00_mem1 += MM_MEM[1]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	S += c_ab_t0_t2 >= 35
	c_ab_t0_t2 += MAS[0]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 35
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 35
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=1, delay_cost=1)
	S += c_bc_t0_t5 >= 35
	c_bc_t0_t5 += MAS[1]

	c_ab_t00 = S.Task('c_ab_t00', length=1, delay_cost=1)
	S += c_ab_t00 >= 36
	c_ab_t00 += MAS[3]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	S += c_ab_t0_t3 >= 36
	c_ab_t0_t3 += MAS[1]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 36
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 36
	c_ab_t0_t4_mem0 += MAS_MEM[0]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 36
	c_ab_t0_t4_mem1 += MAS_MEM[3]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 36
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 36
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 36
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 36
	c_cc_t30_mem1 += MM_MEM[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=6, delay_cost=1)
	S += c_ab_t0_t4 >= 37
	c_ab_t0_t4 += MM[0]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=1, delay_cost=1)
	S += c_ab_t1_t3 >= 37
	c_ab_t1_t3 += MAS[0]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 37
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 37
	c_ab_t1_t4_mem0 += MAS_MEM[4]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 37
	c_ab_t1_t4_mem1 += MAS_MEM[1]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 37
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 37
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 37
	c_ab_t50_mem0 += MAS_MEM[6]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 37
	c_ab_t50_mem1 += MAS_MEM[3]

	c_cc_t30 = S.Task('c_cc_t30', length=1, delay_cost=1)
	S += c_cc_t30 >= 37
	c_cc_t30 += MAS[2]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=6, delay_cost=1)
	S += c_ab_t1_t4 >= 38
	c_ab_t1_t4 += MM[0]

	c_ab_t30 = S.Task('c_ab_t30', length=1, delay_cost=1)
	S += c_ab_t30 >= 38
	c_ab_t30 += MAS[3]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 38
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 38
	c_ab_t4_t0_mem0 += MAS_MEM[4]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 38
	c_ab_t4_t0_mem1 += MAS_MEM[7]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 38
	c_ab_t4_t3_mem0 += MAS_MEM[6]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 38
	c_ab_t4_t3_mem1 += MAS_MEM[5]

	c_ab_t50 = S.Task('c_ab_t50', length=1, delay_cost=1)
	S += c_ab_t50 >= 38
	c_ab_t50 += MAS[0]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 38
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 38
	c_bc_t01_mem1 += MAS_MEM[3]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 38
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 38
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 39
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 39
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=6, delay_cost=1)
	S += c_ab_t4_t0 >= 39
	c_ab_t4_t0 += MM[0]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=1, delay_cost=1)
	S += c_ab_t4_t3 >= 39
	c_ab_t4_t3 += MAS[0]

	c_bc_t01 = S.Task('c_bc_t01', length=1, delay_cost=1)
	S += c_bc_t01 >= 39
	c_bc_t01 += MAS[2]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 39
	c_cc10_mem0 += MAS_MEM[4]

	c_cc10_mem1 = S.Task('c_cc10_mem1', length=1, delay_cost=1)
	S += c_cc10_mem1 >= 39
	c_cc10_mem1 += MAS_MEM[5]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	S += c_cc_t3_t2 >= 39
	c_cc_t3_t2 += MAS[3]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 39
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 39
	c_cc_t3_t4_mem0 += MAS_MEM[6]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 39
	c_cc_t3_t4_mem1 += MAS_MEM[3]

	c_ab_t21 = S.Task('c_ab_t21', length=1, delay_cost=1)
	S += c_ab_t21 >= 40
	c_ab_t21 += MAS[2]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 40
	c_ab_t4_t2_mem0 += MAS_MEM[4]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 40
	c_ab_t4_t2_mem1 += MAS_MEM[5]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 40
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 40
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 40
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_cc10 = S.Task('c_cc10', length=1, delay_cost=1)
	S += c_cc10 >= 40
	c_cc10 += MAS[0]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=6, delay_cost=1)
	S += c_cc_t3_t4 >= 40
	c_cc_t3_t4 += MM[0]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=1, delay_cost=1)
	S += c_ab_t4_t2 >= 41
	c_ab_t4_t2 += MAS[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 41
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 41
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 41
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=6, delay_cost=1)
	S += c_ac_t1_t1 >= 41
	c_ac_t1_t1 += MM[0]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 42
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 42
	c_ab_t01_mem1 += MAS_MEM[1]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 42
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 42
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 42
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=6, delay_cost=1)
	S += c_ac_t1_t0 >= 42
	c_ac_t1_t0 += MM[0]

	c_ab_t01 = S.Task('c_ab_t01', length=1, delay_cost=1)
	S += c_ab_t01 >= 43
	c_ab_t01 += MAS[0]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 43
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 43
	c_ab_t11_mem1 += MAS_MEM[1]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=6, delay_cost=1)
	S += c_ac_t0_t1 >= 43
	c_ac_t0_t1 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 43
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 43
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 43
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 44
	c_ab_s00_mem0 += MAS_MEM[2]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 44
	c_ab_s00_mem1 += MAS_MEM[1]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 44
	c_ab_s01_mem0 += MAS_MEM[0]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 44
	c_ab_s01_mem1 += MAS_MEM[3]

	c_ab_t11 = S.Task('c_ab_t11', length=1, delay_cost=1)
	S += c_ab_t11 >= 44
	c_ab_t11 += MAS[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 44
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 44
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 44
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=6, delay_cost=1)
	S += c_bc_t1_t1 >= 44
	c_bc_t1_t1 += MM[0]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	S += c_ab01_mem0 >= 45
	c_ab01_mem0 += MAS_MEM[0]

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	S += c_ab01_mem1 >= 45
	c_ab01_mem1 += MAS_MEM[3]

	c_ab_s00 = S.Task('c_ab_s00', length=1, delay_cost=1)
	S += c_ab_s00 >= 45
	c_ab_s00 += MAS[0]

	c_ab_s01 = S.Task('c_ab_s01', length=1, delay_cost=1)
	S += c_ab_s01 >= 45
	c_ab_s01 += MAS[1]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 45
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 45
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 45
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=6, delay_cost=1)
	S += c_bc_t1_t0 >= 45
	c_bc_t1_t0 += MM[0]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 45
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 45
	c_cc_t31_mem1 += MAS_MEM[1]

	c_ab01 = S.Task('c_ab01', length=1, delay_cost=1)
	S += c_ab01 >= 46
	c_ab01 += MAS[2]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 46
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 46
	c_ab_t4_t1_mem0 += MAS_MEM[4]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 46
	c_ab_t4_t1_mem1 += MAS_MEM[5]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 46
	c_ab_t51_mem0 += MAS_MEM[0]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 46
	c_ab_t51_mem1 += MAS_MEM[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=6, delay_cost=1)
	S += c_ac_t0_t0 >= 46
	c_ac_t0_t0 += MM[0]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 46
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 46
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_cc_t31 = S.Task('c_cc_t31', length=1, delay_cost=1)
	S += c_cc_t31 >= 46
	c_cc_t31 += MAS[0]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=6, delay_cost=1)
	S += c_ab_t4_t1 >= 47
	c_ab_t4_t1 += MM[0]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 47
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 47
	c_ab_t4_t4_mem0 += MAS_MEM[0]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 47
	c_ab_t4_t4_mem1 += MAS_MEM[1]

	c_ab_t51 = S.Task('c_ab_t51', length=1, delay_cost=1)
	S += c_ab_t51 >= 47
	c_ab_t51 += MAS[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 47
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 47
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 47
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 47
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_bc_t31 = S.Task('c_bc_t31', length=1, delay_cost=1)
	S += c_bc_t31 >= 47
	c_bc_t31 += MAS[2]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=6, delay_cost=1)
	S += c_ab_t4_t4 >= 48
	c_ab_t4_t4 += MM[0]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 48
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 48
	c_ac_t10_mem1 += MM_MEM[1]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 48
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 48
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=1, delay_cost=1)
	S += c_ac_t1_t5 >= 48
	c_ac_t1_t5 += MAS[0]

	c_ac_t20 = S.Task('c_ac_t20', length=1, delay_cost=1)
	S += c_ac_t20 >= 48
	c_ac_t20 += MAS[2]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 48
	c_cc_t40_mem0 += MAS_MEM[4]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 48
	c_cc_t40_mem1 += MAS_MEM[1]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 48
	c_cc_t41_mem0 += MAS_MEM[0]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 48
	c_cc_t41_mem1 += MAS_MEM[5]

	c_ac_t10 = S.Task('c_ac_t10', length=1, delay_cost=1)
	S += c_ac_t10 >= 49
	c_ac_t10 += MAS[2]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=1, delay_cost=1)
	S += c_ac_t1_t3 >= 49
	c_ac_t1_t3 += MAS[1]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 49
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 49
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 49
	c_cc11_mem0 += MAS_MEM[0]

	c_cc11_mem1 = S.Task('c_cc11_mem1', length=1, delay_cost=1)
	S += c_cc11_mem1 >= 49
	c_cc11_mem1 += MAS_MEM[1]

	c_cc_t40 = S.Task('c_cc_t40', length=1, delay_cost=1)
	S += c_cc_t40 >= 49
	c_cc_t40 += MAS[0]

	c_cc_t41 = S.Task('c_cc_t41', length=1, delay_cost=1)
	S += c_cc_t41 >= 49
	c_cc_t41 += MAS[3]

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	S += c_ab00_mem0 >= 50
	c_ab00_mem0 += MAS_MEM[6]

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	S += c_ab00_mem1 >= 50
	c_ab00_mem1 += MAS_MEM[1]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 50
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 50
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=1, delay_cost=1)
	S += c_bc_t1_t3 >= 50
	c_bc_t1_t3 += MAS[2]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 50
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 50
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_cc11 = S.Task('c_cc11', length=1, delay_cost=1)
	S += c_cc11 >= 50
	c_cc11 += MAS[0]

	c_cc_t51_mem0 = S.Task('c_cc_t51_mem0', length=1, delay_cost=1)
	S += c_cc_t51_mem0 >= 50
	c_cc_t51_mem0 += MAS_MEM[0]

	c_cc_t51_mem1 = S.Task('c_cc_t51_mem1', length=1, delay_cost=1)
	S += c_cc_t51_mem1 >= 50
	c_cc_t51_mem1 += MAS_MEM[7]

	c_ab00 = S.Task('c_ab00', length=1, delay_cost=1)
	S += c_ab00 >= 51
	c_ab00 += MAS[3]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 51
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 51
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=1, delay_cost=1)
	S += c_bc_t1_t2 >= 51
	c_bc_t1_t2 += MAS[2]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 51
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 51
	c_bc_t1_t4_mem0 += MAS_MEM[4]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 51
	c_bc_t1_t4_mem1 += MAS_MEM[5]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=1, delay_cost=1)
	S += c_bc_t1_t5 >= 51
	c_bc_t1_t5 += MAS[0]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 51
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 51
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_cc_t51 = S.Task('c_cc_t51', length=1, delay_cost=1)
	S += c_cc_t51 >= 51
	c_cc_t51 += MAS[1]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem0 >= 51
	c_ccxi_y1_1_mem0 += MAS_MEM[0]

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem1 >= 51
	c_ccxi_y1_1_mem1 += MAS_MEM[1]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 52
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 52
	c_ac_t00_mem1 += MM_MEM[1]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=1, delay_cost=1)
	S += c_ac_t0_t5 >= 52
	c_ac_t0_t5 += MAS[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 52
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 52
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=6, delay_cost=1)
	S += c_bc_t1_t4 >= 52
	c_bc_t1_t4 += MM[0]

	c_bc_t20 = S.Task('c_bc_t20', length=1, delay_cost=1)
	S += c_bc_t20 >= 52
	c_bc_t20 += MAS[3]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem0 >= 52
	c_ccxi_y1_0_mem0 += MAS_MEM[0]

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem1 >= 52
	c_ccxi_y1_0_mem1 += MAS_MEM[1]

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=1, delay_cost=1)
	S += c_ccxi_y1_1 >= 52
	c_ccxi_y1_1 += MAS[1]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	S += c_pb01_mem0 >= 52
	c_pb01_mem0 += MAS_MEM[2]

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	S += c_pb01_mem1 >= 52
	c_pb01_mem1 += MAS_MEM[5]

	c_ac_t00 = S.Task('c_ac_t00', length=1, delay_cost=1)
	S += c_ac_t00 >= 53
	c_ac_t00 += MAS[3]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 53
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 53
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t30 = S.Task('c_ac_t30', length=1, delay_cost=1)
	S += c_ac_t30 >= 53
	c_ac_t30 += MAS[0]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 53
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 53
	c_ac_t4_t0_mem0 += MAS_MEM[4]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 53
	c_ac_t4_t0_mem1 += MAS_MEM[1]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 53
	c_ac_t50_mem0 += MAS_MEM[6]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 53
	c_ac_t50_mem1 += MAS_MEM[5]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 53
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 53
	c_bc_t10_mem1 += MM_MEM[1]

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=1, delay_cost=1)
	S += c_ccxi_y1_0 >= 53
	c_ccxi_y1_0 += MAS[1]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	S += c_pb00_mem0 >= 53
	c_pb00_mem0 += MAS_MEM[2]

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	S += c_pb00_mem1 >= 53
	c_pb00_mem1 += MAS_MEM[7]

	c_pb01 = S.Task('c_pb01', length=1, delay_cost=1)
	S += c_pb01 >= 53
	c_pb01 += MAS[2]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 54
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 54
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ac_t21 = S.Task('c_ac_t21', length=1, delay_cost=1)
	S += c_ac_t21 >= 54
	c_ac_t21 += MAS[1]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=6, delay_cost=1)
	S += c_ac_t4_t0 >= 54
	c_ac_t4_t0 += MM[0]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 54
	c_ac_t4_t2_mem0 += MAS_MEM[4]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 54
	c_ac_t4_t2_mem1 += MAS_MEM[3]

	c_ac_t50 = S.Task('c_ac_t50', length=1, delay_cost=1)
	S += c_ac_t50 >= 54
	c_ac_t50 += MAS[3]

	c_bc_t10 = S.Task('c_bc_t10', length=1, delay_cost=1)
	S += c_bc_t10 >= 54
	c_bc_t10 += MAS[0]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 54
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 54
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 54
	c_bc_t50_mem0 += MAS_MEM[0]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 54
	c_bc_t50_mem1 += MAS_MEM[1]

	c_pb00 = S.Task('c_pb00', length=1, delay_cost=1)
	S += c_pb00 >= 54
	c_pb00 += MAS[2]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 55
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 55
	c_ab_t40_mem1 += MM_MEM[1]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=1, delay_cost=1)
	S += c_ab_t4_t5 >= 55
	c_ab_t4_t5 += MAS[2]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=1, delay_cost=1)
	S += c_ac_t4_t2 >= 55
	c_ac_t4_t2 += MAS[1]

	c_bc_t21 = S.Task('c_bc_t21', length=1, delay_cost=1)
	S += c_bc_t21 >= 55
	c_bc_t21 += MAS[3]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 55
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 55
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 55
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 55
	c_bc_t4_t1_mem0 += MAS_MEM[6]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 55
	c_bc_t4_t1_mem1 += MAS_MEM[5]

	c_bc_t50 = S.Task('c_bc_t50', length=1, delay_cost=1)
	S += c_bc_t50 >= 55
	c_bc_t50 += MAS[0]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	S += c_cc_t50_mem0 >= 55
	c_cc_t50_mem0 += MAS_MEM[4]

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	S += c_cc_t50_mem1 >= 55
	c_cc_t50_mem1 += MAS_MEM[1]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 56
	c_ab10_mem0 += MAS_MEM[2]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 56
	c_ab10_mem1 += MAS_MEM[1]

	c_ab_t40 = S.Task('c_ab_t40', length=1, delay_cost=1)
	S += c_ab_t40 >= 56
	c_ab_t40 += MAS[1]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 56
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 56
	c_ab_t41_mem1 += MAS_MEM[5]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 56
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 56
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t30 = S.Task('c_bc_t30', length=1, delay_cost=1)
	S += c_bc_t30 >= 56
	c_bc_t30 += MAS[3]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 56
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 56
	c_bc_t4_t0_mem0 += MAS_MEM[6]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 56
	c_bc_t4_t0_mem1 += MAS_MEM[7]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=6, delay_cost=1)
	S += c_bc_t4_t1 >= 56
	c_bc_t4_t1 += MM[0]

	c_cc_t50 = S.Task('c_cc_t50', length=1, delay_cost=1)
	S += c_cc_t50 >= 56
	c_cc_t50 += MAS[0]

	c_ab10 = S.Task('c_ab10', length=1, delay_cost=1)
	S += c_ab10 >= 57
	c_ab10 += MAS[1]

	c_ab_t41 = S.Task('c_ab_t41', length=1, delay_cost=1)
	S += c_ab_t41 >= 57
	c_ab_t41 += MAS[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 57
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 57
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t31 = S.Task('c_ac_t31', length=1, delay_cost=1)
	S += c_ac_t31 >= 57
	c_ac_t31 += MAS[3]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 57
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 57
	c_ac_t4_t1_mem0 += MAS_MEM[2]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 57
	c_ac_t4_t1_mem1 += MAS_MEM[7]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 57
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 57
	c_bc_t11_mem1 += MAS_MEM[1]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=6, delay_cost=1)
	S += c_bc_t4_t0 >= 57
	c_bc_t4_t0 += MM[0]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 57
	c_bc_t4_t3_mem0 += MAS_MEM[6]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 57
	c_bc_t4_t3_mem1 += MAS_MEM[5]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 58
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 58
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=1, delay_cost=1)
	S += c_ac_t1_t2 >= 58
	c_ac_t1_t2 += MAS[0]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 58
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 58
	c_ac_t1_t4_mem0 += MAS_MEM[0]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 58
	c_ac_t1_t4_mem1 += MAS_MEM[3]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=6, delay_cost=1)
	S += c_ac_t4_t1 >= 58
	c_ac_t4_t1 += MM[0]

	c_bc_t11 = S.Task('c_bc_t11', length=1, delay_cost=1)
	S += c_bc_t11 >= 58
	c_bc_t11 += MAS[2]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 58
	c_bc_t4_t2_mem0 += MAS_MEM[6]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 58
	c_bc_t4_t2_mem1 += MAS_MEM[7]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=1, delay_cost=1)
	S += c_bc_t4_t3 >= 58
	c_bc_t4_t3 += MAS[3]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 58
	c_bc_t51_mem0 += MAS_MEM[4]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 58
	c_bc_t51_mem1 += MAS_MEM[5]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 59
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 59
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=1, delay_cost=1)
	S += c_ac_t0_t3 >= 59
	c_ac_t0_t3 += MAS[0]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=6, delay_cost=1)
	S += c_ac_t1_t4 >= 59
	c_ac_t1_t4 += MM[0]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 59
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 59
	c_ac_t4_t3_mem1 += MAS_MEM[7]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 59
	c_bc_s01_mem0 += MAS_MEM[4]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 59
	c_bc_s01_mem1 += MAS_MEM[1]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=1, delay_cost=1)
	S += c_bc_t4_t2 >= 59
	c_bc_t4_t2 += MAS[3]

	c_bc_t51 = S.Task('c_bc_t51', length=1, delay_cost=1)
	S += c_bc_t51 >= 59
	c_bc_t51 += MAS[1]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=1, delay_cost=1)
	S += c_ac_t0_t2 >= 60
	c_ac_t0_t2 += MAS[0]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 60
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 60
	c_ac_t0_t4_mem0 += MAS_MEM[0]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 60
	c_ac_t0_t4_mem1 += MAS_MEM[1]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=1, delay_cost=1)
	S += c_ac_t4_t3 >= 60
	c_ac_t4_t3 += MAS[3]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	S += c_bc01_mem0 >= 60
	c_bc01_mem0 += MAS_MEM[4]

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	S += c_bc01_mem1 >= 60
	c_bc01_mem1 += MAS_MEM[5]

	c_bc_s01 = S.Task('c_bc_s01', length=1, delay_cost=1)
	S += c_bc_s01 >= 60
	c_bc_s01 += MAS[2]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 60
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 60
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=6, delay_cost=1)
	S += c_ac_t0_t4 >= 61
	c_ac_t0_t4 += MM[0]

	c_bc01 = S.Task('c_bc01', length=1, delay_cost=1)
	S += c_bc01 >= 61
	c_bc01 += MAS[0]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 61
	c_bc_s00_mem0 += MAS_MEM[0]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 61
	c_bc_s00_mem1 += MAS_MEM[5]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 61
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 61
	c_bc_t4_t4_mem0 += MAS_MEM[6]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 61
	c_bc_t4_t4_mem1 += MAS_MEM[7]

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	S += c_pa11_mem0 >= 61
	c_pa11_mem0 += MAS_MEM[4]

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	S += c_pa11_mem1 >= 61
	c_pa11_mem1 += MAS_MEM[1]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=1, delay_cost=1)
	S += c_pcb_t1_t3 >= 61
	c_pcb_t1_t3 += MAS[3]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 61
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 61
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	S += c1_t0_t2_mem0 >= 62
	c1_t0_t2_mem0 += MAS_MEM[4]

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	S += c1_t0_t2_mem1 >= 62
	c1_t0_t2_mem1 += MAS_MEM[5]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	S += c_ab11_mem0 >= 62
	c_ab11_mem0 += MAS_MEM[0]

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	S += c_ab11_mem1 >= 62
	c_ab11_mem1 += MAS_MEM[1]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 62
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 62
	c_ac_t4_t4_mem0 += MAS_MEM[2]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 62
	c_ac_t4_t4_mem1 += MAS_MEM[7]

	c_bc_s00 = S.Task('c_bc_s00', length=1, delay_cost=1)
	S += c_bc_s00 >= 62
	c_bc_s00 += MAS[3]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 62
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 62
	c_bc_t40_mem1 += MM_MEM[1]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=6, delay_cost=1)
	S += c_bc_t4_t4 >= 62
	c_bc_t4_t4 += MM[0]

	c_pa11 = S.Task('c_pa11', length=1, delay_cost=1)
	S += c_pa11 >= 62
	c_pa11 += MAS[1]

	c_pcb_t30 = S.Task('c_pcb_t30', length=1, delay_cost=1)
	S += c_pcb_t30 >= 62
	c_pcb_t30 += MAS[0]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 62
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 62
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c1_t0_t2 = S.Task('c1_t0_t2', length=1, delay_cost=1)
	S += c1_t0_t2 >= 63
	c1_t0_t2 += MAS[1]

	c_ab11 = S.Task('c_ab11', length=1, delay_cost=1)
	S += c_ab11 >= 63
	c_ab11 += MAS[3]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 63
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 63
	c_ac_t40_mem1 += MM_MEM[1]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=6, delay_cost=1)
	S += c_ac_t4_t4 >= 63
	c_ac_t4_t4 += MM[0]

	c_bc_t40 = S.Task('c_bc_t40', length=1, delay_cost=1)
	S += c_bc_t40 >= 63
	c_bc_t40 += MAS[0]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 63
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 63
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t31 = S.Task('c_pcb_t31', length=1, delay_cost=1)
	S += c_pcb_t31 >= 63
	c_pcb_t31 += MAS[2]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 63
	c_pcb_t4_t3_mem0 += MAS_MEM[0]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 63
	c_pcb_t4_t3_mem1 += MAS_MEM[5]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 64
	c_ac10_mem0 += MAS_MEM[0]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 64
	c_ac10_mem1 += MAS_MEM[7]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 64
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 64
	c_ac_t11_mem1 += MAS_MEM[1]

	c_ac_t40 = S.Task('c_ac_t40', length=1, delay_cost=1)
	S += c_ac_t40 >= 64
	c_ac_t40 += MAS[0]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=1, delay_cost=1)
	S += c_paa_t0_t3 >= 64
	c_paa_t0_t3 += MAS[2]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 64
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 64
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem0 >= 64
	c_pbc_t0_t2_mem0 += MAS_MEM[4]

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem1 >= 64
	c_pbc_t0_t2_mem1 += MAS_MEM[5]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=1, delay_cost=1)
	S += c_pcb_t4_t3 >= 64
	c_pcb_t4_t3 += MAS[1]

	c_ac10 = S.Task('c_ac10', length=1, delay_cost=1)
	S += c_ac10 >= 65
	c_ac10 += MAS[0]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 65
	c_ac_s00_mem0 += MAS_MEM[4]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 65
	c_ac_s00_mem1 += MAS_MEM[7]

	c_ac_t11 = S.Task('c_ac_t11', length=1, delay_cost=1)
	S += c_ac_t11 >= 65
	c_ac_t11 += MAS[3]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 65
	c_bc10_mem0 += MAS_MEM[0]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 65
	c_bc10_mem1 += MAS_MEM[1]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 65
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 65
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=1, delay_cost=1)
	S += c_paa_t1_t3 >= 65
	c_paa_t1_t3 += MAS[1]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 65
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 65
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=1, delay_cost=1)
	S += c_pbc_t0_t2 >= 65
	c_pbc_t0_t2 += MAS[2]

	c_ac_s00 = S.Task('c_ac_s00', length=1, delay_cost=1)
	S += c_ac_s00 >= 66
	c_ac_s00 += MAS[2]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 66
	c_ac_s01_mem0 += MAS_MEM[6]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 66
	c_ac_s01_mem1 += MAS_MEM[5]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 66
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 66
	c_ac_t01_mem1 += MAS_MEM[1]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	S += c_bc00_mem0 >= 66
	c_bc00_mem0 += MAS_MEM[0]

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	S += c_bc00_mem1 >= 66
	c_bc00_mem1 += MAS_MEM[7]

	c_bc10 = S.Task('c_bc10', length=1, delay_cost=1)
	S += c_bc10 >= 66
	c_bc10 += MAS[0]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=1, delay_cost=1)
	S += c_bc_t4_t5 >= 66
	c_bc_t4_t5 += MAS[1]

	c_paa_t30 = S.Task('c_paa_t30', length=1, delay_cost=1)
	S += c_paa_t30 >= 66
	c_paa_t30 += MAS[3]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 66
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 66
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_ac_s01 = S.Task('c_ac_s01', length=1, delay_cost=1)
	S += c_ac_s01 >= 67
	c_ac_s01 += MAS[2]

	c_ac_t01 = S.Task('c_ac_t01', length=1, delay_cost=1)
	S += c_ac_t01 >= 67
	c_ac_t01 += MAS[0]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 67
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 67
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 67
	c_ac_t51_mem0 += MAS_MEM[0]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 67
	c_ac_t51_mem1 += MAS_MEM[7]

	c_bc00 = S.Task('c_bc00', length=1, delay_cost=1)
	S += c_bc00 >= 67
	c_bc00 += MAS[3]

	c_paa_t31 = S.Task('c_paa_t31', length=1, delay_cost=1)
	S += c_paa_t31 >= 67
	c_paa_t31 += MAS[1]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 67
	c_paa_t4_t3_mem0 += MAS_MEM[6]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 67
	c_paa_t4_t3_mem1 += MAS_MEM[3]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 67
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 67
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	S += c_ac01_mem0 >= 68
	c_ac01_mem0 += MAS_MEM[0]

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	S += c_ac01_mem1 >= 68
	c_ac01_mem1 += MAS_MEM[5]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=1, delay_cost=1)
	S += c_ac_t4_t5 >= 68
	c_ac_t4_t5 += MAS[1]

	c_ac_t51 = S.Task('c_ac_t51', length=1, delay_cost=1)
	S += c_ac_t51 >= 68
	c_ac_t51 += MAS[2]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 68
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 68
	c_bc_t41_mem1 += MAS_MEM[3]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=1, delay_cost=1)
	S += c_paa_t4_t3 >= 68
	c_paa_t4_t3 += MAS[3]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 68
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 68
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	S += c_pc10_mem0 >= 68
	c_pc10_mem0 += MAS_MEM[2]

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	S += c_pc10_mem1 >= 68
	c_pc10_mem1 += MAS_MEM[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=1, delay_cost=1)
	S += c_pcb_t0_t3 >= 68
	c_pcb_t0_t3 += MAS[0]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	S += c_ac00_mem0 >= 69
	c_ac00_mem0 += MAS_MEM[6]

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	S += c_ac00_mem1 >= 69
	c_ac00_mem1 += MAS_MEM[5]

	c_ac01 = S.Task('c_ac01', length=1, delay_cost=1)
	S += c_ac01 >= 69
	c_ac01 += MAS[3]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 69
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 69
	c_ac_t41_mem1 += MAS_MEM[3]

	c_bc_t41 = S.Task('c_bc_t41', length=1, delay_cost=1)
	S += c_bc_t41 >= 69
	c_bc_t41 += MAS[1]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	S += c_pa10_mem0 >= 69
	c_pa10_mem0 += MAS_MEM[2]

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	S += c_pa10_mem1 >= 69
	c_pa10_mem1 += MAS_MEM[7]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=1, delay_cost=1)
	S += c_pbc_t0_t3 >= 69
	c_pbc_t0_t3 += MAS[0]

	c_pbc_t0_t4_in = S.Task('c_pbc_t0_t4_in', length=1, delay_cost=1)
	S += c_pbc_t0_t4_in >= 69
	c_pbc_t0_t4_in += MM_in[0]

	c_pbc_t0_t4_mem0 = S.Task('c_pbc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t4_mem0 >= 69
	c_pbc_t0_t4_mem0 += MAS_MEM[4]

	c_pbc_t0_t4_mem1 = S.Task('c_pbc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t4_mem1 >= 69
	c_pbc_t0_t4_mem1 += MAS_MEM[1]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 69
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 69
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_pc10 = S.Task('c_pc10', length=1, delay_cost=1)
	S += c_pc10 >= 69
	c_pc10 += MAS[2]

	c_ac00 = S.Task('c_ac00', length=1, delay_cost=1)
	S += c_ac00 >= 70
	c_ac00 += MAS[3]

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	S += c_ac11_mem0 >= 70
	c_ac11_mem0 += MAS_MEM[0]

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	S += c_ac11_mem1 >= 70
	c_ac11_mem1 += MAS_MEM[5]

	c_ac_t41 = S.Task('c_ac_t41', length=1, delay_cost=1)
	S += c_ac_t41 >= 70
	c_ac_t41 += MAS[0]

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	S += c_bc11_mem0 >= 70
	c_bc11_mem0 += MAS_MEM[2]

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	S += c_bc11_mem1 >= 70
	c_bc11_mem1 += MAS_MEM[3]

	c_pa10 = S.Task('c_pa10', length=1, delay_cost=1)
	S += c_pa10 >= 70
	c_pa10 += MAS[1]

	c_pbc_t0_t4 = S.Task('c_pbc_t0_t4', length=6, delay_cost=1)
	S += c_pbc_t0_t4 >= 70
	c_pbc_t0_t4 += MM[0]

	c_pbc_t30 = S.Task('c_pbc_t30', length=1, delay_cost=1)
	S += c_pbc_t30 >= 70
	c_pbc_t30 += MAS[2]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 70
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 70
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_ac11 = S.Task('c_ac11', length=1, delay_cost=1)
	S += c_ac11 >= 71
	c_ac11 += MAS[2]

	c_bc11 = S.Task('c_bc11', length=1, delay_cost=1)
	S += c_bc11 >= 71
	c_bc11 += MAS[1]

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem0 >= 71
	c_bcxi_y1_1_mem0 += MAS_MEM[2]

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem1 >= 71
	c_bcxi_y1_1_mem1 += MAS_MEM[1]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 71
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 71
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t31 = S.Task('c_pbc_t31', length=1, delay_cost=1)
	S += c_pbc_t31 >= 71
	c_pbc_t31 += MAS[3]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 71
	c_pbc_t4_t3_mem0 += MAS_MEM[4]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 71
	c_pbc_t4_t3_mem1 += MAS_MEM[7]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	S += c_pc11_mem0 >= 71
	c_pc11_mem0 += MAS_MEM[0]

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	S += c_pc11_mem1 >= 71
	c_pc11_mem1 += MAS_MEM[5]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 72
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 72
	c_bb_t00_mem1 += MAS_MEM[1]

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_0_mem0 >= 72
	c_bcxi_y1_0_mem0 += MAS_MEM[0]

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_0_mem1 >= 72
	c_bcxi_y1_0_mem1 += MAS_MEM[3]

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=1, delay_cost=1)
	S += c_bcxi_y1_1 >= 72
	c_bcxi_y1_1 += MAS[2]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=1, delay_cost=1)
	S += c_pbc_t1_t3 >= 72
	c_pbc_t1_t3 += MAS[1]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=1, delay_cost=1)
	S += c_pbc_t4_t3 >= 72
	c_pbc_t4_t3 += MAS[0]

	c_pc11 = S.Task('c_pc11', length=1, delay_cost=1)
	S += c_pc11 >= 72
	c_pc11 += MAS[3]

	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	S += c_pcb_t1_t0_in >= 72
	c_pcb_t1_t0_in += MM_in[0]

	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem0 >= 72
	c_pcb_t1_t0_mem0 += MAS_MEM[4]

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem1 >= 72
	c_pcb_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t00 = S.Task('c_bb_t00', length=1, delay_cost=1)
	S += c_bb_t00 >= 73
	c_bb_t00 += MAS[1]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 73
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 73
	c_bb_t01_mem1 += MAS_MEM[1]

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=1, delay_cost=1)
	S += c_bcxi_y1_0 >= 73
	c_bcxi_y1_0 += MAS[0]

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t2_mem0 >= 73
	c_paa_t1_t2_mem0 += MAS_MEM[2]

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t2_mem1 >= 73
	c_paa_t1_t2_mem1 += MAS_MEM[3]

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=6, delay_cost=1)
	S += c_pcb_t1_t0 >= 73
	c_pcb_t1_t0 += MM[0]

	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	S += c_pcb_t1_t1_in >= 73
	c_pcb_t1_t1_in += MM_in[0]

	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem0 >= 73
	c_pcb_t1_t1_mem0 += MAS_MEM[6]

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem1 >= 73
	c_pcb_t1_t1_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem0 >= 73
	c_pcb_t1_t2_mem0 += MAS_MEM[4]

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem1 >= 73
	c_pcb_t1_t2_mem1 += MAS_MEM[7]

	c_bb_t01 = S.Task('c_bb_t01', length=1, delay_cost=1)
	S += c_bb_t01 >= 74
	c_bb_t01 += MAS[2]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 74
	c_bb_t2_t2_mem0 += MAS_MEM[2]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 74
	c_bb_t2_t2_mem1 += MAS_MEM[5]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 74
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 74
	c_cc_t00_mem1 += MAS_MEM[1]

	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=1, delay_cost=1)
	S += c_paa_t1_t2 >= 74
	c_paa_t1_t2 += MAS[1]

	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	S += c_pbc_t0_t1_in >= 74
	c_pbc_t0_t1_in += MM_in[0]

	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem0 >= 74
	c_pbc_t0_t1_mem0 += MAS_MEM[4]

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem1 >= 74
	c_pbc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=6, delay_cost=1)
	S += c_pcb_t1_t1 >= 74
	c_pcb_t1_t1 += MM[0]

	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=1, delay_cost=1)
	S += c_pcb_t1_t2 >= 74
	c_pcb_t1_t2 += MAS[0]

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	S += c0_t1_t2_mem0 >= 75
	c0_t1_t2_mem0 += MAS_MEM[2]

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	S += c0_t1_t2_mem1 >= 75
	c0_t1_t2_mem1 += MAS_MEM[3]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 75
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 75
	c_aa_t01_mem1 += MAS_MEM[1]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=1, delay_cost=1)
	S += c_bb_t2_t2 >= 75
	c_bb_t2_t2 += MAS[1]

	c_cc_t00 = S.Task('c_cc_t00', length=1, delay_cost=1)
	S += c_cc_t00 >= 75
	c_cc_t00 += MAS[0]

	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	S += c_pbc_t0_t0_in >= 75
	c_pbc_t0_t0_in += MM_in[0]

	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem0 >= 75
	c_pbc_t0_t0_mem0 += MAS_MEM[4]

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem1 >= 75
	c_pbc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=6, delay_cost=1)
	S += c_pbc_t0_t1 >= 75
	c_pbc_t0_t1 += MM[0]

	c0_t1_t2 = S.Task('c0_t1_t2', length=1, delay_cost=1)
	S += c0_t1_t2 >= 76
	c0_t1_t2 += MAS[2]

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	S += c2_t1_t2_mem0 >= 76
	c2_t1_t2_mem0 += MAS_MEM[4]

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	S += c2_t1_t2_mem1 >= 76
	c2_t1_t2_mem1 += MAS_MEM[7]

	c_aa_t01 = S.Task('c_aa_t01', length=1, delay_cost=1)
	S += c_aa_t01 >= 76
	c_aa_t01 += MAS[0]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 76
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 76
	c_aa_t2_t1_mem0 += MAS_MEM[0]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 76
	c_aa_t2_t1_mem1 += MAS_MEM[1]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 76
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 76
	c_cc_t01_mem1 += MAS_MEM[3]

	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=6, delay_cost=1)
	S += c_pbc_t0_t0 >= 76
	c_pbc_t0_t0 += MM[0]

	c2_t1_t2 = S.Task('c2_t1_t2', length=1, delay_cost=1)
	S += c2_t1_t2 >= 77
	c2_t1_t2 += MAS[0]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 77
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 77
	c_aa_t00_mem1 += MAS_MEM[5]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=6, delay_cost=1)
	S += c_aa_t2_t1 >= 77
	c_aa_t2_t1 += MM[0]

	c_cc_t01 = S.Task('c_cc_t01', length=1, delay_cost=1)
	S += c_cc_t01 >= 77
	c_cc_t01 += MAS[2]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 77
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 77
	c_cc_t2_t1_mem0 += MAS_MEM[4]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 77
	c_cc_t2_t1_mem1 += MAS_MEM[1]

	c_aa_t00 = S.Task('c_aa_t00', length=1, delay_cost=1)
	S += c_aa_t00 >= 78
	c_aa_t00 += MAS[2]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 78
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 78
	c_aa_t2_t0_mem0 += MAS_MEM[4]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 78
	c_aa_t2_t0_mem1 += MAS_MEM[1]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=6, delay_cost=1)
	S += c_cc_t2_t1 >= 78
	c_cc_t2_t1 += MM[0]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 78
	c_cc_t2_t2_mem0 += MAS_MEM[0]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 78
	c_cc_t2_t2_mem1 += MAS_MEM[5]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=6, delay_cost=1)
	S += c_aa_t2_t0 >= 79
	c_aa_t2_t0 += MM[0]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 79
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 79
	c_bb_t2_t1_mem0 += MAS_MEM[4]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 79
	c_bb_t2_t1_mem1 += MAS_MEM[1]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=1, delay_cost=1)
	S += c_cc_t2_t2 >= 79
	c_cc_t2_t2 += MAS[0]

	c_pcb_t10_mem0 = S.Task('c_pcb_t10_mem0', length=1, delay_cost=1)
	S += c_pcb_t10_mem0 >= 79
	c_pcb_t10_mem0 += MM_MEM[0]

	c_pcb_t10_mem1 = S.Task('c_pcb_t10_mem1', length=1, delay_cost=1)
	S += c_pcb_t10_mem1 >= 79
	c_pcb_t10_mem1 += MM_MEM[1]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=6, delay_cost=1)
	S += c_bb_t2_t1 >= 80
	c_bb_t2_t1 += MM[0]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 80
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 80
	c_cc_t2_t0_mem0 += MAS_MEM[0]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 80
	c_cc_t2_t0_mem1 += MAS_MEM[1]

	c_pcb_t10 = S.Task('c_pcb_t10', length=1, delay_cost=1)
	S += c_pcb_t10 >= 80
	c_pcb_t10 += MAS[1]

	c_pcb_t1_t5_mem0 = S.Task('c_pcb_t1_t5_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t5_mem0 >= 80
	c_pcb_t1_t5_mem0 += MM_MEM[0]

	c_pcb_t1_t5_mem1 = S.Task('c_pcb_t1_t5_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t5_mem1 >= 80
	c_pcb_t1_t5_mem1 += MM_MEM[1]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 81
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 81
	c_bb_t2_t0_mem0 += MAS_MEM[2]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 81
	c_bb_t2_t0_mem1 += MAS_MEM[1]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=6, delay_cost=1)
	S += c_cc_t2_t0 >= 81
	c_cc_t2_t0 += MM[0]

	c_pbc_t00_mem0 = S.Task('c_pbc_t00_mem0', length=1, delay_cost=1)
	S += c_pbc_t00_mem0 >= 81
	c_pbc_t00_mem0 += MM_MEM[0]

	c_pbc_t00_mem1 = S.Task('c_pbc_t00_mem1', length=1, delay_cost=1)
	S += c_pbc_t00_mem1 >= 81
	c_pbc_t00_mem1 += MM_MEM[1]

	c_pcb_t1_t5 = S.Task('c_pcb_t1_t5', length=1, delay_cost=1)
	S += c_pcb_t1_t5 >= 81
	c_pcb_t1_t5 += MAS[1]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 82
	c_aa_t2_t2_mem0 += MAS_MEM[4]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 82
	c_aa_t2_t2_mem1 += MAS_MEM[1]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=6, delay_cost=1)
	S += c_bb_t2_t0 >= 82
	c_bb_t2_t0 += MM[0]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 82
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 82
	c_cc_t2_t4_mem0 += MAS_MEM[0]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 82
	c_cc_t2_t4_mem1 += MAS_MEM[3]

	c_pbc_t00 = S.Task('c_pbc_t00', length=1, delay_cost=1)
	S += c_pbc_t00 >= 82
	c_pbc_t00 += MAS[2]

	c_pbc_t0_t5_mem0 = S.Task('c_pbc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t5_mem0 >= 82
	c_pbc_t0_t5_mem0 += MM_MEM[0]

	c_pbc_t0_t5_mem1 = S.Task('c_pbc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t5_mem1 >= 82
	c_pbc_t0_t5_mem1 += MM_MEM[1]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=1, delay_cost=1)
	S += c_aa_t2_t2 >= 83
	c_aa_t2_t2 += MAS[3]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 83
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 83
	c_aa_t2_t4_mem0 += MAS_MEM[6]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 83
	c_aa_t2_t4_mem1 += MAS_MEM[1]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=6, delay_cost=1)
	S += c_cc_t2_t4 >= 83
	c_cc_t2_t4 += MM[0]

	c_pbc_t0_t5 = S.Task('c_pbc_t0_t5', length=1, delay_cost=1)
	S += c_pbc_t0_t5 >= 83
	c_pbc_t0_t5 += MAS[0]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 84
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 84
	c_aa_t20_mem1 += MM_MEM[1]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=6, delay_cost=1)
	S += c_aa_t2_t4 >= 84
	c_aa_t2_t4 += MM[0]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 84
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 84
	c_bb_t2_t4_mem0 += MAS_MEM[2]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 84
	c_bb_t2_t4_mem1 += MAS_MEM[1]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	S += c_aa00_mem0 >= 85
	c_aa00_mem0 += MAS_MEM[0]

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	S += c_aa00_mem1 >= 85
	c_aa00_mem1 += MAS_MEM[7]

	c_aa_t20 = S.Task('c_aa_t20', length=1, delay_cost=1)
	S += c_aa_t20 >= 85
	c_aa_t20 += MAS[0]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 85
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 85
	c_aa_t2_t5_mem1 += MM_MEM[1]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=6, delay_cost=1)
	S += c_bb_t2_t4 >= 85
	c_bb_t2_t4 += MM[0]

	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	S += c_paa_t1_t0_in >= 85
	c_paa_t1_t0_in += MM_in[0]

	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem0 >= 85
	c_paa_t1_t0_mem0 += MAS_MEM[2]

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem1 >= 85
	c_paa_t1_t0_mem1 += MAIN_MEM_r[1]

	c_aa00 = S.Task('c_aa00', length=1, delay_cost=1)
	S += c_aa00 >= 86
	c_aa00 += MAS[0]

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=1, delay_cost=1)
	S += c_aa_t2_t5 >= 86
	c_aa_t2_t5 += MAS[1]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 86
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 86
	c_cc_t20_mem1 += MM_MEM[1]

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	S += c_pa00_mem0 >= 86
	c_pa00_mem0 += MAS_MEM[0]

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	S += c_pa00_mem1 >= 86
	c_pa00_mem1 += MAS_MEM[1]

	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=6, delay_cost=1)
	S += c_paa_t1_t0 >= 86
	c_paa_t1_t0 += MM[0]

	c_paa_t1_t4_in = S.Task('c_paa_t1_t4_in', length=1, delay_cost=1)
	S += c_paa_t1_t4_in >= 86
	c_paa_t1_t4_in += MM_in[0]

	c_paa_t1_t4_mem0 = S.Task('c_paa_t1_t4_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t4_mem0 >= 86
	c_paa_t1_t4_mem0 += MAS_MEM[2]

	c_paa_t1_t4_mem1 = S.Task('c_paa_t1_t4_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t4_mem1 >= 86
	c_paa_t1_t4_mem1 += MAS_MEM[3]

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	S += c0_t20_mem0 >= 87
	c0_t20_mem0 += MAS_MEM[6]

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	S += c0_t20_mem1 >= 87
	c0_t20_mem1 += MAS_MEM[3]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 87
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 87
	c_bb_t20_mem1 += MM_MEM[1]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	S += c_cc00_mem0 >= 87
	c_cc00_mem0 += MAS_MEM[0]

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	S += c_cc00_mem1 >= 87
	c_cc00_mem1 += MAS_MEM[1]

	c_cc_t20 = S.Task('c_cc_t20', length=1, delay_cost=1)
	S += c_cc_t20 >= 87
	c_cc_t20 += MAS[0]

	c_pa00 = S.Task('c_pa00', length=1, delay_cost=1)
	S += c_pa00 >= 87
	c_pa00 += MAS[3]

	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	S += c_paa_t1_t1_in >= 87
	c_paa_t1_t1_in += MM_in[0]

	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t1_mem0 >= 87
	c_paa_t1_t1_mem0 += MAS_MEM[2]

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t1_mem1 >= 87
	c_paa_t1_t1_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t4 = S.Task('c_paa_t1_t4', length=6, delay_cost=1)
	S += c_paa_t1_t4 >= 87
	c_paa_t1_t4 += MM[0]

	c0_t20 = S.Task('c0_t20', length=1, delay_cost=1)
	S += c0_t20 >= 88
	c0_t20 += MAS[1]

	c_bb_t20 = S.Task('c_bb_t20', length=1, delay_cost=1)
	S += c_bb_t20 >= 88
	c_bb_t20 += MAS[0]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 88
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 88
	c_bb_t2_t5_mem1 += MM_MEM[1]

	c_cc00 = S.Task('c_cc00', length=1, delay_cost=1)
	S += c_cc00 >= 88
	c_cc00 += MAS[2]

	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=6, delay_cost=1)
	S += c_paa_t1_t1 >= 88
	c_paa_t1_t1 += MM[0]

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	S += c_pb10_mem0 >= 88
	c_pb10_mem0 += MAS_MEM[4]

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	S += c_pb10_mem1 >= 88
	c_pb10_mem1 += MAS_MEM[3]

	c_pcb_t1_t4_in = S.Task('c_pcb_t1_t4_in', length=1, delay_cost=1)
	S += c_pcb_t1_t4_in >= 88
	c_pcb_t1_t4_in += MM_in[0]

	c_pcb_t1_t4_mem0 = S.Task('c_pcb_t1_t4_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t4_mem0 >= 88
	c_pcb_t1_t4_mem0 += MAS_MEM[0]

	c_pcb_t1_t4_mem1 = S.Task('c_pcb_t1_t4_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t4_mem1 >= 88
	c_pcb_t1_t4_mem1 += MAS_MEM[7]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	S += c_bb00_mem0 >= 89
	c_bb00_mem0 += MAS_MEM[0]

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	S += c_bb00_mem1 >= 89
	c_bb00_mem1 += MAS_MEM[3]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=1, delay_cost=1)
	S += c_bb_t2_t5 >= 89
	c_bb_t2_t5 += MAS[3]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 89
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 89
	c_cc_t2_t5_mem1 += MM_MEM[1]

	c_paa_t0_t0_in = S.Task('c_paa_t0_t0_in', length=1, delay_cost=1)
	S += c_paa_t0_t0_in >= 89
	c_paa_t0_t0_in += MM_in[0]

	c_paa_t0_t0_mem0 = S.Task('c_paa_t0_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t0_mem0 >= 89
	c_paa_t0_t0_mem0 += MAS_MEM[6]

	c_paa_t0_t0_mem1 = S.Task('c_paa_t0_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t0_mem1 >= 89
	c_paa_t0_t0_mem1 += MAIN_MEM_r[1]

	c_pb10 = S.Task('c_pb10', length=1, delay_cost=1)
	S += c_pb10 >= 89
	c_pb10 += MAS[0]

	c_pbc_t20_mem0 = S.Task('c_pbc_t20_mem0', length=1, delay_cost=1)
	S += c_pbc_t20_mem0 >= 89
	c_pbc_t20_mem0 += MAS_MEM[4]

	c_pbc_t20_mem1 = S.Task('c_pbc_t20_mem1', length=1, delay_cost=1)
	S += c_pbc_t20_mem1 >= 89
	c_pbc_t20_mem1 += MAS_MEM[1]

	c_pcb_t1_t4 = S.Task('c_pcb_t1_t4', length=6, delay_cost=1)
	S += c_pcb_t1_t4 >= 89
	c_pcb_t1_t4 += MM[0]

	c_bb00 = S.Task('c_bb00', length=1, delay_cost=1)
	S += c_bb00 >= 90
	c_bb00 += MAS[2]

	c_cc_t21_mem0 = S.Task('c_cc_t21_mem0', length=1, delay_cost=1)
	S += c_cc_t21_mem0 >= 90
	c_cc_t21_mem0 += MM_MEM[0]

	c_cc_t21_mem1 = S.Task('c_cc_t21_mem1', length=1, delay_cost=1)
	S += c_cc_t21_mem1 >= 90
	c_cc_t21_mem1 += MAS_MEM[1]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=1, delay_cost=1)
	S += c_cc_t2_t5 >= 90
	c_cc_t2_t5 += MAS[0]

	c_paa_t0_t0 = S.Task('c_paa_t0_t0', length=6, delay_cost=1)
	S += c_paa_t0_t0 >= 90
	c_paa_t0_t0 += MM[0]

	c_paa_t20_mem0 = S.Task('c_paa_t20_mem0', length=1, delay_cost=1)
	S += c_paa_t20_mem0 >= 90
	c_paa_t20_mem0 += MAS_MEM[6]

	c_paa_t20_mem1 = S.Task('c_paa_t20_mem1', length=1, delay_cost=1)
	S += c_paa_t20_mem1 >= 90
	c_paa_t20_mem1 += MAS_MEM[3]

	c_pbc_t1_t0_in = S.Task('c_pbc_t1_t0_in', length=1, delay_cost=1)
	S += c_pbc_t1_t0_in >= 90
	c_pbc_t1_t0_in += MM_in[0]

	c_pbc_t1_t0_mem0 = S.Task('c_pbc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t0_mem0 >= 90
	c_pbc_t1_t0_mem0 += MAS_MEM[0]

	c_pbc_t1_t0_mem1 = S.Task('c_pbc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t0_mem1 >= 90
	c_pbc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_pbc_t20 = S.Task('c_pbc_t20', length=1, delay_cost=1)
	S += c_pbc_t20 >= 90
	c_pbc_t20 += MAS[3]

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	S += c_pc00_mem0 >= 90
	c_pc00_mem0 += MAS_MEM[4]

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	S += c_pc00_mem1 >= 90
	c_pc00_mem1 += MAS_MEM[7]

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	S += c1_t20_mem0 >= 91
	c1_t20_mem0 += MAS_MEM[4]

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	S += c1_t20_mem1 >= 91
	c1_t20_mem1 += MAS_MEM[1]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	S += c_bb_t21_mem0 >= 91
	c_bb_t21_mem0 += MM_MEM[0]

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	S += c_bb_t21_mem1 >= 91
	c_bb_t21_mem1 += MAS_MEM[7]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	S += c_cc01_mem0 >= 91
	c_cc01_mem0 += MAS_MEM[6]

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	S += c_cc01_mem1 >= 91
	c_cc01_mem1 += MAS_MEM[3]

	c_cc_t21 = S.Task('c_cc_t21', length=1, delay_cost=1)
	S += c_cc_t21 >= 91
	c_cc_t21 += MAS[3]

	c_paa_t20 = S.Task('c_paa_t20', length=1, delay_cost=1)
	S += c_paa_t20 >= 91
	c_paa_t20 += MAS[2]

	c_pbc_t1_t0 = S.Task('c_pbc_t1_t0', length=6, delay_cost=1)
	S += c_pbc_t1_t0 >= 91
	c_pbc_t1_t0 += MM[0]

	c_pc00 = S.Task('c_pc00', length=1, delay_cost=1)
	S += c_pc00 >= 91
	c_pc00 += MAS[1]

	c_pcb_t0_t0_in = S.Task('c_pcb_t0_t0_in', length=1, delay_cost=1)
	S += c_pcb_t0_t0_in >= 91
	c_pcb_t0_t0_in += MM_in[0]

	c_pcb_t0_t0_mem0 = S.Task('c_pcb_t0_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t0_mem0 >= 91
	c_pcb_t0_t0_mem0 += MAS_MEM[2]

	c_pcb_t0_t0_mem1 = S.Task('c_pcb_t0_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t0_mem1 >= 91
	c_pcb_t0_t0_mem1 += MAIN_MEM_r[1]

	c1_t20 = S.Task('c1_t20', length=1, delay_cost=1)
	S += c1_t20 >= 92
	c1_t20 += MAS[3]

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	S += c2_t20_mem0 >= 92
	c2_t20_mem0 += MAS_MEM[2]

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	S += c2_t20_mem1 >= 92
	c2_t20_mem1 += MAS_MEM[5]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t21_mem0 >= 92
	c_aa_t21_mem0 += MM_MEM[0]

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t21_mem1 >= 92
	c_aa_t21_mem1 += MAS_MEM[3]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	S += c_bb01_mem0 >= 92
	c_bb01_mem0 += MAS_MEM[0]

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	S += c_bb01_mem1 >= 92
	c_bb01_mem1 += MAS_MEM[1]

	c_bb_t21 = S.Task('c_bb_t21', length=1, delay_cost=1)
	S += c_bb_t21 >= 92
	c_bb_t21 += MAS[0]

	c_cc01 = S.Task('c_cc01', length=1, delay_cost=1)
	S += c_cc01 >= 92
	c_cc01 += MAS[2]

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	S += c_pb11_mem0 >= 92
	c_pb11_mem0 += MAS_MEM[4]

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	S += c_pb11_mem1 >= 92
	c_pb11_mem1 += MAS_MEM[7]

	c_pcb_t0_t0 = S.Task('c_pcb_t0_t0', length=6, delay_cost=1)
	S += c_pcb_t0_t0 >= 92
	c_pcb_t0_t0 += MM[0]

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	S += c1_t21_mem0 >= 93
	c1_t21_mem0 += MAS_MEM[4]

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	S += c1_t21_mem1 >= 93
	c1_t21_mem1 += MAS_MEM[7]

	c2_t20 = S.Task('c2_t20', length=1, delay_cost=1)
	S += c2_t20 >= 93
	c2_t20 += MAS[2]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	S += c_aa01_mem0 >= 93
	c_aa01_mem0 += MAS_MEM[0]

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	S += c_aa01_mem1 >= 93
	c_aa01_mem1 += MAS_MEM[1]

	c_aa_t21 = S.Task('c_aa_t21', length=1, delay_cost=1)
	S += c_aa_t21 >= 93
	c_aa_t21 += MAS[0]

	c_bb01 = S.Task('c_bb01', length=1, delay_cost=1)
	S += c_bb01 >= 93
	c_bb01 += MAS[1]

	c_paa_t10_mem0 = S.Task('c_paa_t10_mem0', length=1, delay_cost=1)
	S += c_paa_t10_mem0 >= 93
	c_paa_t10_mem0 += MM_MEM[0]

	c_paa_t10_mem1 = S.Task('c_paa_t10_mem1', length=1, delay_cost=1)
	S += c_paa_t10_mem1 >= 93
	c_paa_t10_mem1 += MM_MEM[1]

	c_pb11 = S.Task('c_pb11', length=1, delay_cost=1)
	S += c_pb11 >= 93
	c_pb11 += MAS[3]

	c_pbc_t1_t1_in = S.Task('c_pbc_t1_t1_in', length=1, delay_cost=1)
	S += c_pbc_t1_t1_in >= 93
	c_pbc_t1_t1_in += MM_in[0]

	c_pbc_t1_t1_mem0 = S.Task('c_pbc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t1_mem0 >= 93
	c_pbc_t1_t1_mem0 += MAS_MEM[6]

	c_pbc_t1_t1_mem1 = S.Task('c_pbc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t1_mem1 >= 93
	c_pbc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_pcb_t20_mem0 = S.Task('c_pcb_t20_mem0', length=1, delay_cost=1)
	S += c_pcb_t20_mem0 >= 93
	c_pcb_t20_mem0 += MAS_MEM[2]

	c_pcb_t20_mem1 = S.Task('c_pcb_t20_mem1', length=1, delay_cost=1)
	S += c_pcb_t20_mem1 >= 93
	c_pcb_t20_mem1 += MAS_MEM[5]

	c1_t21 = S.Task('c1_t21', length=1, delay_cost=1)
	S += c1_t21 >= 94
	c1_t21 += MAS[3]

	c_aa01 = S.Task('c_aa01', length=1, delay_cost=1)
	S += c_aa01 >= 94
	c_aa01 += MAS[0]

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	S += c_pa01_mem0 >= 94
	c_pa01_mem0 += MAS_MEM[0]

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	S += c_pa01_mem1 >= 94
	c_pa01_mem1 += MAS_MEM[5]

	c_paa_t10 = S.Task('c_paa_t10', length=1, delay_cost=1)
	S += c_paa_t10 >= 94
	c_paa_t10 += MAS[1]

	c_paa_t1_t5_mem0 = S.Task('c_paa_t1_t5_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t5_mem0 >= 94
	c_paa_t1_t5_mem0 += MM_MEM[0]

	c_paa_t1_t5_mem1 = S.Task('c_paa_t1_t5_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t5_mem1 >= 94
	c_paa_t1_t5_mem1 += MM_MEM[1]

	c_pbc_t1_t1 = S.Task('c_pbc_t1_t1', length=6, delay_cost=1)
	S += c_pbc_t1_t1 >= 94
	c_pbc_t1_t1 += MM[0]

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	S += c_pc01_mem0 >= 94
	c_pc01_mem0 += MAS_MEM[2]

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	S += c_pc01_mem1 >= 94
	c_pc01_mem1 += MAS_MEM[7]

	c_pcb_t20 = S.Task('c_pcb_t20', length=1, delay_cost=1)
	S += c_pcb_t20 >= 94
	c_pcb_t20 += MAS[2]

	c0_t0_t2_mem0 = S.Task('c0_t0_t2_mem0', length=1, delay_cost=1)
	S += c0_t0_t2_mem0 >= 95
	c0_t0_t2_mem0 += MAS_MEM[6]

	c0_t0_t2_mem1 = S.Task('c0_t0_t2_mem1', length=1, delay_cost=1)
	S += c0_t0_t2_mem1 >= 95
	c0_t0_t2_mem1 += MAS_MEM[5]

	c_pa01 = S.Task('c_pa01', length=1, delay_cost=1)
	S += c_pa01 >= 95
	c_pa01 += MAS[2]

	c_paa_t1_t5 = S.Task('c_paa_t1_t5', length=1, delay_cost=1)
	S += c_paa_t1_t5 >= 95
	c_paa_t1_t5 += MAS[0]

	c_paa_t21_mem0 = S.Task('c_paa_t21_mem0', length=1, delay_cost=1)
	S += c_paa_t21_mem0 >= 95
	c_paa_t21_mem0 += MAS_MEM[4]

	c_paa_t21_mem1 = S.Task('c_paa_t21_mem1', length=1, delay_cost=1)
	S += c_paa_t21_mem1 >= 95
	c_paa_t21_mem1 += MAS_MEM[3]

	c_pbc_t1_t2_mem0 = S.Task('c_pbc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t2_mem0 >= 95
	c_pbc_t1_t2_mem0 += MAS_MEM[0]

	c_pbc_t1_t2_mem1 = S.Task('c_pbc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t2_mem1 >= 95
	c_pbc_t1_t2_mem1 += MAS_MEM[7]

	c_pc01 = S.Task('c_pc01', length=1, delay_cost=1)
	S += c_pc01 >= 95
	c_pc01 += MAS[1]

	c_pcb_t0_t1_in = S.Task('c_pcb_t0_t1_in', length=1, delay_cost=1)
	S += c_pcb_t0_t1_in >= 95
	c_pcb_t0_t1_in += MM_in[0]

	c_pcb_t0_t1_mem0 = S.Task('c_pcb_t0_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t1_mem0 >= 95
	c_pcb_t0_t1_mem0 += MAS_MEM[2]

	c_pcb_t0_t1_mem1 = S.Task('c_pcb_t0_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t1_mem1 >= 95
	c_pcb_t0_t1_mem1 += MAIN_MEM_r[1]

	c0_t0_t2 = S.Task('c0_t0_t2', length=1, delay_cost=1)
	S += c0_t0_t2 >= 96
	c0_t0_t2 += MAS[3]

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	S += c1_t1_t2_mem0 >= 96
	c1_t1_t2_mem0 += MAS_MEM[0]

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	S += c1_t1_t2_mem1 >= 96
	c1_t1_t2_mem1 += MAS_MEM[7]

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	S += c2_t0_t2_mem0 >= 96
	c2_t0_t2_mem0 += MAS_MEM[2]

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	S += c2_t0_t2_mem1 >= 96
	c2_t0_t2_mem1 += MAS_MEM[3]

	c_paa_t0_t1_in = S.Task('c_paa_t0_t1_in', length=1, delay_cost=1)
	S += c_paa_t0_t1_in >= 96
	c_paa_t0_t1_in += MM_in[0]

	c_paa_t0_t1_mem0 = S.Task('c_paa_t0_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t1_mem0 >= 96
	c_paa_t0_t1_mem0 += MAS_MEM[4]

	c_paa_t0_t1_mem1 = S.Task('c_paa_t0_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t1_mem1 >= 96
	c_paa_t0_t1_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t2_mem0 = S.Task('c_paa_t0_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t2_mem0 >= 96
	c_paa_t0_t2_mem0 += MAS_MEM[6]

	c_paa_t0_t2_mem1 = S.Task('c_paa_t0_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t2_mem1 >= 96
	c_paa_t0_t2_mem1 += MAS_MEM[5]

	c_paa_t21 = S.Task('c_paa_t21', length=1, delay_cost=1)
	S += c_paa_t21 >= 96
	c_paa_t21 += MAS[1]

	c_pbc_t1_t2 = S.Task('c_pbc_t1_t2', length=1, delay_cost=1)
	S += c_pbc_t1_t2 >= 96
	c_pbc_t1_t2 += MAS[2]

	c_pcb_t0_t1 = S.Task('c_pcb_t0_t1', length=6, delay_cost=1)
	S += c_pcb_t0_t1 >= 96
	c_pcb_t0_t1 += MM[0]

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	S += c0_t21_mem0 >= 97
	c0_t21_mem0 += MAS_MEM[4]

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	S += c0_t21_mem1 >= 97
	c0_t21_mem1 += MAS_MEM[3]

	c1_t1_t2 = S.Task('c1_t1_t2', length=1, delay_cost=1)
	S += c1_t1_t2 >= 97
	c1_t1_t2 += MAS[1]

	c2_t0_t2 = S.Task('c2_t0_t2', length=1, delay_cost=1)
	S += c2_t0_t2 >= 97
	c2_t0_t2 += MAS[0]

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	S += c2_t21_mem0 >= 97
	c2_t21_mem0 += MAS_MEM[2]

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	S += c2_t21_mem1 >= 97
	c2_t21_mem1 += MAS_MEM[7]

	c_paa_t0_t1 = S.Task('c_paa_t0_t1', length=6, delay_cost=1)
	S += c_paa_t0_t1 >= 97
	c_paa_t0_t1 += MM[0]

	c_paa_t0_t2 = S.Task('c_paa_t0_t2', length=1, delay_cost=1)
	S += c_paa_t0_t2 >= 97
	c_paa_t0_t2 += MAS[2]

	c0_t21 = S.Task('c0_t21', length=1, delay_cost=1)
	S += c0_t21 >= 98
	c0_t21 += MAS[2]

	c2_t21 = S.Task('c2_t21', length=1, delay_cost=1)
	S += c2_t21 >= 98
	c2_t21 += MAS[3]

	c_pbc_t21_mem0 = S.Task('c_pbc_t21_mem0', length=1, delay_cost=1)
	S += c_pbc_t21_mem0 >= 98
	c_pbc_t21_mem0 += MAS_MEM[4]

	c_pbc_t21_mem1 = S.Task('c_pbc_t21_mem1', length=1, delay_cost=1)
	S += c_pbc_t21_mem1 >= 98
	c_pbc_t21_mem1 += MAS_MEM[7]

	c_pcb_t0_t2_mem0 = S.Task('c_pcb_t0_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t2_mem0 >= 98
	c_pcb_t0_t2_mem0 += MAS_MEM[2]

	c_pcb_t0_t2_mem1 = S.Task('c_pcb_t0_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t2_mem1 >= 98
	c_pcb_t0_t2_mem1 += MAS_MEM[3]

	c_pbc_t21 = S.Task('c_pbc_t21', length=1, delay_cost=1)
	S += c_pbc_t21 >= 99
	c_pbc_t21 += MAS[0]

	c_pcb_t0_t2 = S.Task('c_pcb_t0_t2', length=1, delay_cost=1)
	S += c_pcb_t0_t2 >= 99
	c_pcb_t0_t2 += MAS[2]

	c_pcb_t21_mem0 = S.Task('c_pcb_t21_mem0', length=1, delay_cost=1)
	S += c_pcb_t21_mem0 >= 99
	c_pcb_t21_mem0 += MAS_MEM[2]

	c_pcb_t21_mem1 = S.Task('c_pcb_t21_mem1', length=1, delay_cost=1)
	S += c_pcb_t21_mem1 >= 99
	c_pcb_t21_mem1 += MAS_MEM[7]

	c_pcb_t21 = S.Task('c_pcb_t21', length=1, delay_cost=1)
	S += c_pcb_t21 >= 100
	c_pcb_t21 += MAS[2]


	# new tasks
	c_pbc_t01 = S.Task('c_pbc_t01', length=1, delay_cost=1)
	c_pbc_t01 += alt(MAS)

	c_pbc_t01_mem0 = S.Task('c_pbc_t01_mem0', length=1, delay_cost=1)
	c_pbc_t01_mem0 += MM_MEM[0]
	S += 75 < c_pbc_t01_mem0
	S += c_pbc_t01_mem0 <= c_pbc_t01

	c_pbc_t01_mem1 = S.Task('c_pbc_t01_mem1', length=1, delay_cost=1)
	c_pbc_t01_mem1 += MAS_MEM[1]
	S += 83 < c_pbc_t01_mem1
	S += c_pbc_t01_mem1 <= c_pbc_t01

	c_pbc_t1_t4_in = S.Task('c_pbc_t1_t4_in', length=1, delay_cost=1)
	c_pbc_t1_t4_in += alt(MM_in)
	c_pbc_t1_t4 = S.Task('c_pbc_t1_t4', length=6, delay_cost=1)
	c_pbc_t1_t4 += alt(MM)
	S += c_pbc_t1_t4>=c_pbc_t1_t4_in

	c_pbc_t1_t4_mem0 = S.Task('c_pbc_t1_t4_mem0', length=1, delay_cost=1)
	c_pbc_t1_t4_mem0 += MAS_MEM[4]
	S += 96 < c_pbc_t1_t4_mem0
	S += c_pbc_t1_t4_mem0 <= c_pbc_t1_t4

	c_pbc_t1_t4_mem1 = S.Task('c_pbc_t1_t4_mem1', length=1, delay_cost=1)
	c_pbc_t1_t4_mem1 += MAS_MEM[3]
	S += 72 < c_pbc_t1_t4_mem1
	S += c_pbc_t1_t4_mem1 <= c_pbc_t1_t4

	c_pbc_t10 = S.Task('c_pbc_t10', length=1, delay_cost=1)
	c_pbc_t10 += alt(MAS)

	c_pbc_t10_mem0 = S.Task('c_pbc_t10_mem0', length=1, delay_cost=1)
	c_pbc_t10_mem0 += MM_MEM[0]
	S += 96 < c_pbc_t10_mem0
	S += c_pbc_t10_mem0 <= c_pbc_t10

	c_pbc_t10_mem1 = S.Task('c_pbc_t10_mem1', length=1, delay_cost=1)
	c_pbc_t10_mem1 += MM_MEM[1]
	S += 99 < c_pbc_t10_mem1
	S += c_pbc_t10_mem1 <= c_pbc_t10

	c_pbc_t1_t5 = S.Task('c_pbc_t1_t5', length=1, delay_cost=1)
	c_pbc_t1_t5 += alt(MAS)

	c_pbc_t1_t5_mem0 = S.Task('c_pbc_t1_t5_mem0', length=1, delay_cost=1)
	c_pbc_t1_t5_mem0 += MM_MEM[0]
	S += 96 < c_pbc_t1_t5_mem0
	S += c_pbc_t1_t5_mem0 <= c_pbc_t1_t5

	c_pbc_t1_t5_mem1 = S.Task('c_pbc_t1_t5_mem1', length=1, delay_cost=1)
	c_pbc_t1_t5_mem1 += MM_MEM[1]
	S += 99 < c_pbc_t1_t5_mem1
	S += c_pbc_t1_t5_mem1 <= c_pbc_t1_t5

	c_pbc_t4_t0_in = S.Task('c_pbc_t4_t0_in', length=1, delay_cost=1)
	c_pbc_t4_t0_in += alt(MM_in)
	c_pbc_t4_t0 = S.Task('c_pbc_t4_t0', length=6, delay_cost=1)
	c_pbc_t4_t0 += alt(MM)
	S += c_pbc_t4_t0>=c_pbc_t4_t0_in

	c_pbc_t4_t0_mem0 = S.Task('c_pbc_t4_t0_mem0', length=1, delay_cost=1)
	c_pbc_t4_t0_mem0 += MAS_MEM[6]
	S += 90 < c_pbc_t4_t0_mem0
	S += c_pbc_t4_t0_mem0 <= c_pbc_t4_t0

	c_pbc_t4_t0_mem1 = S.Task('c_pbc_t4_t0_mem1', length=1, delay_cost=1)
	c_pbc_t4_t0_mem1 += MAS_MEM[5]
	S += 70 < c_pbc_t4_t0_mem1
	S += c_pbc_t4_t0_mem1 <= c_pbc_t4_t0

	c_pbc_t4_t1_in = S.Task('c_pbc_t4_t1_in', length=1, delay_cost=1)
	c_pbc_t4_t1_in += alt(MM_in)
	c_pbc_t4_t1 = S.Task('c_pbc_t4_t1', length=6, delay_cost=1)
	c_pbc_t4_t1 += alt(MM)
	S += c_pbc_t4_t1>=c_pbc_t4_t1_in

	c_pbc_t4_t1_mem0 = S.Task('c_pbc_t4_t1_mem0', length=1, delay_cost=1)
	c_pbc_t4_t1_mem0 += MAS_MEM[0]
	S += 99 < c_pbc_t4_t1_mem0
	S += c_pbc_t4_t1_mem0 <= c_pbc_t4_t1

	c_pbc_t4_t1_mem1 = S.Task('c_pbc_t4_t1_mem1', length=1, delay_cost=1)
	c_pbc_t4_t1_mem1 += MAS_MEM[7]
	S += 71 < c_pbc_t4_t1_mem1
	S += c_pbc_t4_t1_mem1 <= c_pbc_t4_t1

	c_pbc_t4_t2 = S.Task('c_pbc_t4_t2', length=1, delay_cost=1)
	c_pbc_t4_t2 += alt(MAS)

	c_pbc_t4_t2_mem0 = S.Task('c_pbc_t4_t2_mem0', length=1, delay_cost=1)
	c_pbc_t4_t2_mem0 += MAS_MEM[6]
	S += 90 < c_pbc_t4_t2_mem0
	S += c_pbc_t4_t2_mem0 <= c_pbc_t4_t2

	c_pbc_t4_t2_mem1 = S.Task('c_pbc_t4_t2_mem1', length=1, delay_cost=1)
	c_pbc_t4_t2_mem1 += MAS_MEM[1]
	S += 99 < c_pbc_t4_t2_mem1
	S += c_pbc_t4_t2_mem1 <= c_pbc_t4_t2

	c_pcb_t0_t4_in = S.Task('c_pcb_t0_t4_in', length=1, delay_cost=1)
	c_pcb_t0_t4_in += alt(MM_in)
	c_pcb_t0_t4 = S.Task('c_pcb_t0_t4', length=6, delay_cost=1)
	c_pcb_t0_t4 += alt(MM)
	S += c_pcb_t0_t4>=c_pcb_t0_t4_in

	c_pcb_t0_t4_mem0 = S.Task('c_pcb_t0_t4_mem0', length=1, delay_cost=1)
	c_pcb_t0_t4_mem0 += MAS_MEM[4]
	S += 99 < c_pcb_t0_t4_mem0
	S += c_pcb_t0_t4_mem0 <= c_pcb_t0_t4

	c_pcb_t0_t4_mem1 = S.Task('c_pcb_t0_t4_mem1', length=1, delay_cost=1)
	c_pcb_t0_t4_mem1 += MAS_MEM[1]
	S += 68 < c_pcb_t0_t4_mem1
	S += c_pcb_t0_t4_mem1 <= c_pcb_t0_t4

	c_pcb_t00 = S.Task('c_pcb_t00', length=1, delay_cost=1)
	c_pcb_t00 += alt(MAS)

	c_pcb_t00_mem0 = S.Task('c_pcb_t00_mem0', length=1, delay_cost=1)
	c_pcb_t00_mem0 += MM_MEM[0]
	S += 97 < c_pcb_t00_mem0
	S += c_pcb_t00_mem0 <= c_pcb_t00

	c_pcb_t00_mem1 = S.Task('c_pcb_t00_mem1', length=1, delay_cost=1)
	c_pcb_t00_mem1 += MM_MEM[1]
	S += 101 < c_pcb_t00_mem1
	S += c_pcb_t00_mem1 <= c_pcb_t00

	c_pcb_t0_t5 = S.Task('c_pcb_t0_t5', length=1, delay_cost=1)
	c_pcb_t0_t5 += alt(MAS)

	c_pcb_t0_t5_mem0 = S.Task('c_pcb_t0_t5_mem0', length=1, delay_cost=1)
	c_pcb_t0_t5_mem0 += MM_MEM[0]
	S += 97 < c_pcb_t0_t5_mem0
	S += c_pcb_t0_t5_mem0 <= c_pcb_t0_t5

	c_pcb_t0_t5_mem1 = S.Task('c_pcb_t0_t5_mem1', length=1, delay_cost=1)
	c_pcb_t0_t5_mem1 += MM_MEM[1]
	S += 101 < c_pcb_t0_t5_mem1
	S += c_pcb_t0_t5_mem1 <= c_pcb_t0_t5

	c_pcb_t11 = S.Task('c_pcb_t11', length=1, delay_cost=1)
	c_pcb_t11 += alt(MAS)

	c_pcb_t11_mem0 = S.Task('c_pcb_t11_mem0', length=1, delay_cost=1)
	c_pcb_t11_mem0 += MM_MEM[0]
	S += 94 < c_pcb_t11_mem0
	S += c_pcb_t11_mem0 <= c_pcb_t11

	c_pcb_t11_mem1 = S.Task('c_pcb_t11_mem1', length=1, delay_cost=1)
	c_pcb_t11_mem1 += MAS_MEM[3]
	S += 81 < c_pcb_t11_mem1
	S += c_pcb_t11_mem1 <= c_pcb_t11

	c_pcb_t4_t0_in = S.Task('c_pcb_t4_t0_in', length=1, delay_cost=1)
	c_pcb_t4_t0_in += alt(MM_in)
	c_pcb_t4_t0 = S.Task('c_pcb_t4_t0', length=6, delay_cost=1)
	c_pcb_t4_t0 += alt(MM)
	S += c_pcb_t4_t0>=c_pcb_t4_t0_in

	c_pcb_t4_t0_mem0 = S.Task('c_pcb_t4_t0_mem0', length=1, delay_cost=1)
	c_pcb_t4_t0_mem0 += MAS_MEM[4]
	S += 94 < c_pcb_t4_t0_mem0
	S += c_pcb_t4_t0_mem0 <= c_pcb_t4_t0

	c_pcb_t4_t0_mem1 = S.Task('c_pcb_t4_t0_mem1', length=1, delay_cost=1)
	c_pcb_t4_t0_mem1 += MAS_MEM[1]
	S += 62 < c_pcb_t4_t0_mem1
	S += c_pcb_t4_t0_mem1 <= c_pcb_t4_t0

	c_pcb_t4_t1_in = S.Task('c_pcb_t4_t1_in', length=1, delay_cost=1)
	c_pcb_t4_t1_in += alt(MM_in)
	c_pcb_t4_t1 = S.Task('c_pcb_t4_t1', length=6, delay_cost=1)
	c_pcb_t4_t1 += alt(MM)
	S += c_pcb_t4_t1>=c_pcb_t4_t1_in

	c_pcb_t4_t1_mem0 = S.Task('c_pcb_t4_t1_mem0', length=1, delay_cost=1)
	c_pcb_t4_t1_mem0 += MAS_MEM[4]
	S += 100 < c_pcb_t4_t1_mem0
	S += c_pcb_t4_t1_mem0 <= c_pcb_t4_t1

	c_pcb_t4_t1_mem1 = S.Task('c_pcb_t4_t1_mem1', length=1, delay_cost=1)
	c_pcb_t4_t1_mem1 += MAS_MEM[5]
	S += 63 < c_pcb_t4_t1_mem1
	S += c_pcb_t4_t1_mem1 <= c_pcb_t4_t1

	c_pcb_t4_t2 = S.Task('c_pcb_t4_t2', length=1, delay_cost=1)
	c_pcb_t4_t2 += alt(MAS)

	c_pcb_t4_t2_mem0 = S.Task('c_pcb_t4_t2_mem0', length=1, delay_cost=1)
	c_pcb_t4_t2_mem0 += MAS_MEM[4]
	S += 94 < c_pcb_t4_t2_mem0
	S += c_pcb_t4_t2_mem0 <= c_pcb_t4_t2

	c_pcb_t4_t2_mem1 = S.Task('c_pcb_t4_t2_mem1', length=1, delay_cost=1)
	c_pcb_t4_t2_mem1 += MAS_MEM[5]
	S += 100 < c_pcb_t4_t2_mem1
	S += c_pcb_t4_t2_mem1 <= c_pcb_t4_t2

	c_paa_t0_t4_in = S.Task('c_paa_t0_t4_in', length=1, delay_cost=1)
	c_paa_t0_t4_in += alt(MM_in)
	c_paa_t0_t4 = S.Task('c_paa_t0_t4', length=6, delay_cost=1)
	c_paa_t0_t4 += alt(MM)
	S += c_paa_t0_t4>=c_paa_t0_t4_in

	c_paa_t0_t4_mem0 = S.Task('c_paa_t0_t4_mem0', length=1, delay_cost=1)
	c_paa_t0_t4_mem0 += MAS_MEM[4]
	S += 97 < c_paa_t0_t4_mem0
	S += c_paa_t0_t4_mem0 <= c_paa_t0_t4

	c_paa_t0_t4_mem1 = S.Task('c_paa_t0_t4_mem1', length=1, delay_cost=1)
	c_paa_t0_t4_mem1 += MAS_MEM[5]
	S += 64 < c_paa_t0_t4_mem1
	S += c_paa_t0_t4_mem1 <= c_paa_t0_t4

	c_paa_t00 = S.Task('c_paa_t00', length=1, delay_cost=1)
	c_paa_t00 += alt(MAS)

	c_paa_t00_mem0 = S.Task('c_paa_t00_mem0', length=1, delay_cost=1)
	c_paa_t00_mem0 += MM_MEM[0]
	S += 95 < c_paa_t00_mem0
	S += c_paa_t00_mem0 <= c_paa_t00

	c_paa_t00_mem1 = S.Task('c_paa_t00_mem1', length=1, delay_cost=1)
	c_paa_t00_mem1 += MM_MEM[1]
	S += 102 < c_paa_t00_mem1
	S += c_paa_t00_mem1 <= c_paa_t00

	c_paa_t0_t5 = S.Task('c_paa_t0_t5', length=1, delay_cost=1)
	c_paa_t0_t5 += alt(MAS)

	c_paa_t0_t5_mem0 = S.Task('c_paa_t0_t5_mem0', length=1, delay_cost=1)
	c_paa_t0_t5_mem0 += MM_MEM[0]
	S += 95 < c_paa_t0_t5_mem0
	S += c_paa_t0_t5_mem0 <= c_paa_t0_t5

	c_paa_t0_t5_mem1 = S.Task('c_paa_t0_t5_mem1', length=1, delay_cost=1)
	c_paa_t0_t5_mem1 += MM_MEM[1]
	S += 102 < c_paa_t0_t5_mem1
	S += c_paa_t0_t5_mem1 <= c_paa_t0_t5

	c_paa_t11 = S.Task('c_paa_t11', length=1, delay_cost=1)
	c_paa_t11 += alt(MAS)

	c_paa_t11_mem0 = S.Task('c_paa_t11_mem0', length=1, delay_cost=1)
	c_paa_t11_mem0 += MM_MEM[0]
	S += 92 < c_paa_t11_mem0
	S += c_paa_t11_mem0 <= c_paa_t11

	c_paa_t11_mem1 = S.Task('c_paa_t11_mem1', length=1, delay_cost=1)
	c_paa_t11_mem1 += MAS_MEM[1]
	S += 95 < c_paa_t11_mem1
	S += c_paa_t11_mem1 <= c_paa_t11

	c_paa_t4_t0_in = S.Task('c_paa_t4_t0_in', length=1, delay_cost=1)
	c_paa_t4_t0_in += alt(MM_in)
	c_paa_t4_t0 = S.Task('c_paa_t4_t0', length=6, delay_cost=1)
	c_paa_t4_t0 += alt(MM)
	S += c_paa_t4_t0>=c_paa_t4_t0_in

	c_paa_t4_t0_mem0 = S.Task('c_paa_t4_t0_mem0', length=1, delay_cost=1)
	c_paa_t4_t0_mem0 += MAS_MEM[4]
	S += 91 < c_paa_t4_t0_mem0
	S += c_paa_t4_t0_mem0 <= c_paa_t4_t0

	c_paa_t4_t0_mem1 = S.Task('c_paa_t4_t0_mem1', length=1, delay_cost=1)
	c_paa_t4_t0_mem1 += MAS_MEM[7]
	S += 66 < c_paa_t4_t0_mem1
	S += c_paa_t4_t0_mem1 <= c_paa_t4_t0

	c_paa_t4_t1_in = S.Task('c_paa_t4_t1_in', length=1, delay_cost=1)
	c_paa_t4_t1_in += alt(MM_in)
	c_paa_t4_t1 = S.Task('c_paa_t4_t1', length=6, delay_cost=1)
	c_paa_t4_t1 += alt(MM)
	S += c_paa_t4_t1>=c_paa_t4_t1_in

	c_paa_t4_t1_mem0 = S.Task('c_paa_t4_t1_mem0', length=1, delay_cost=1)
	c_paa_t4_t1_mem0 += MAS_MEM[2]
	S += 96 < c_paa_t4_t1_mem0
	S += c_paa_t4_t1_mem0 <= c_paa_t4_t1

	c_paa_t4_t1_mem1 = S.Task('c_paa_t4_t1_mem1', length=1, delay_cost=1)
	c_paa_t4_t1_mem1 += MAS_MEM[3]
	S += 67 < c_paa_t4_t1_mem1
	S += c_paa_t4_t1_mem1 <= c_paa_t4_t1

	c_paa_t4_t2 = S.Task('c_paa_t4_t2', length=1, delay_cost=1)
	c_paa_t4_t2 += alt(MAS)

	c_paa_t4_t2_mem0 = S.Task('c_paa_t4_t2_mem0', length=1, delay_cost=1)
	c_paa_t4_t2_mem0 += MAS_MEM[4]
	S += 91 < c_paa_t4_t2_mem0
	S += c_paa_t4_t2_mem0 <= c_paa_t4_t2

	c_paa_t4_t2_mem1 = S.Task('c_paa_t4_t2_mem1', length=1, delay_cost=1)
	c_paa_t4_t2_mem1 += MAS_MEM[3]
	S += 96 < c_paa_t4_t2_mem1
	S += c_paa_t4_t2_mem1 <= c_paa_t4_t2

	c0_t4_t2 = S.Task('c0_t4_t2', length=1, delay_cost=1)
	c0_t4_t2 += alt(MAS)

	c0_t4_t2_mem0 = S.Task('c0_t4_t2_mem0', length=1, delay_cost=1)
	c0_t4_t2_mem0 += MAS_MEM[2]
	S += 88 < c0_t4_t2_mem0
	S += c0_t4_t2_mem0 <= c0_t4_t2

	c0_t4_t2_mem1 = S.Task('c0_t4_t2_mem1', length=1, delay_cost=1)
	c0_t4_t2_mem1 += MAS_MEM[5]
	S += 98 < c0_t4_t2_mem1
	S += c0_t4_t2_mem1 <= c0_t4_t2

	c1_t4_t2 = S.Task('c1_t4_t2', length=1, delay_cost=1)
	c1_t4_t2 += alt(MAS)

	c1_t4_t2_mem0 = S.Task('c1_t4_t2_mem0', length=1, delay_cost=1)
	c1_t4_t2_mem0 += MAS_MEM[6]
	S += 92 < c1_t4_t2_mem0
	S += c1_t4_t2_mem0 <= c1_t4_t2

	c1_t4_t2_mem1 = S.Task('c1_t4_t2_mem1', length=1, delay_cost=1)
	c1_t4_t2_mem1 += MAS_MEM[7]
	S += 94 < c1_t4_t2_mem1
	S += c1_t4_t2_mem1 <= c1_t4_t2

	c2_t4_t2 = S.Task('c2_t4_t2', length=1, delay_cost=1)
	c2_t4_t2 += alt(MAS)

	c2_t4_t2_mem0 = S.Task('c2_t4_t2_mem0', length=1, delay_cost=1)
	c2_t4_t2_mem0 += MAS_MEM[4]
	S += 93 < c2_t4_t2_mem0
	S += c2_t4_t2_mem0 <= c2_t4_t2

	c2_t4_t2_mem1 = S.Task('c2_t4_t2_mem1', length=1, delay_cost=1)
	c2_t4_t2_mem1 += MAS_MEM[7]
	S += 98 < c2_t4_t2_mem1
	S += c2_t4_t2_mem1 <= c2_t4_t2

	c_pbc_t11 = S.Task('c_pbc_t11', length=1, delay_cost=1)
	c_pbc_t11 += alt(MAS)

	c_pbc_t11_mem0 = S.Task('c_pbc_t11_mem0', length=1, delay_cost=1)
	c_pbc_t11_mem0 += alt(MM_MEM)
	S += (c_pbc_t1_t4*MM[0])-1 < c_pbc_t11_mem0*MM_MEM[0]
	S += c_pbc_t11_mem0 <= c_pbc_t11

	c_pbc_t11_mem1 = S.Task('c_pbc_t11_mem1', length=1, delay_cost=1)
	c_pbc_t11_mem1 += alt(MAS_MEM)
	S += (c_pbc_t1_t5*MAS[0])-1 < c_pbc_t11_mem1*MAS_MEM[1]
	S += (c_pbc_t1_t5*MAS[1])-1 < c_pbc_t11_mem1*MAS_MEM[3]
	S += (c_pbc_t1_t5*MAS[2])-1 < c_pbc_t11_mem1*MAS_MEM[5]
	S += (c_pbc_t1_t5*MAS[3])-1 < c_pbc_t11_mem1*MAS_MEM[7]
	S += c_pbc_t11_mem1 <= c_pbc_t11

	c_pbc_t4_t4_in = S.Task('c_pbc_t4_t4_in', length=1, delay_cost=1)
	c_pbc_t4_t4_in += alt(MM_in)
	c_pbc_t4_t4 = S.Task('c_pbc_t4_t4', length=6, delay_cost=1)
	c_pbc_t4_t4 += alt(MM)
	S += c_pbc_t4_t4>=c_pbc_t4_t4_in

	c_pbc_t4_t4_mem0 = S.Task('c_pbc_t4_t4_mem0', length=1, delay_cost=1)
	c_pbc_t4_t4_mem0 += alt(MAS_MEM)
	S += (c_pbc_t4_t2*MAS[0])-1 < c_pbc_t4_t4_mem0*MAS_MEM[0]
	S += (c_pbc_t4_t2*MAS[1])-1 < c_pbc_t4_t4_mem0*MAS_MEM[2]
	S += (c_pbc_t4_t2*MAS[2])-1 < c_pbc_t4_t4_mem0*MAS_MEM[4]
	S += (c_pbc_t4_t2*MAS[3])-1 < c_pbc_t4_t4_mem0*MAS_MEM[6]
	S += c_pbc_t4_t4_mem0 <= c_pbc_t4_t4

	c_pbc_t4_t4_mem1 = S.Task('c_pbc_t4_t4_mem1', length=1, delay_cost=1)
	c_pbc_t4_t4_mem1 += MAS_MEM[1]
	S += 72 < c_pbc_t4_t4_mem1
	S += c_pbc_t4_t4_mem1 <= c_pbc_t4_t4

	c_pbc_t40 = S.Task('c_pbc_t40', length=1, delay_cost=1)
	c_pbc_t40 += alt(MAS)

	c_pbc_t40_mem0 = S.Task('c_pbc_t40_mem0', length=1, delay_cost=1)
	c_pbc_t40_mem0 += alt(MM_MEM)
	S += (c_pbc_t4_t0*MM[0])-1 < c_pbc_t40_mem0*MM_MEM[0]
	S += c_pbc_t40_mem0 <= c_pbc_t40

	c_pbc_t40_mem1 = S.Task('c_pbc_t40_mem1', length=1, delay_cost=1)
	c_pbc_t40_mem1 += alt(MM_MEM)
	S += (c_pbc_t4_t1*MM[0])-1 < c_pbc_t40_mem1*MM_MEM[1]
	S += c_pbc_t40_mem1 <= c_pbc_t40

	c_pbc_t4_t5 = S.Task('c_pbc_t4_t5', length=1, delay_cost=1)
	c_pbc_t4_t5 += alt(MAS)

	c_pbc_t4_t5_mem0 = S.Task('c_pbc_t4_t5_mem0', length=1, delay_cost=1)
	c_pbc_t4_t5_mem0 += alt(MM_MEM)
	S += (c_pbc_t4_t0*MM[0])-1 < c_pbc_t4_t5_mem0*MM_MEM[0]
	S += c_pbc_t4_t5_mem0 <= c_pbc_t4_t5

	c_pbc_t4_t5_mem1 = S.Task('c_pbc_t4_t5_mem1', length=1, delay_cost=1)
	c_pbc_t4_t5_mem1 += alt(MM_MEM)
	S += (c_pbc_t4_t1*MM[0])-1 < c_pbc_t4_t5_mem1*MM_MEM[1]
	S += c_pbc_t4_t5_mem1 <= c_pbc_t4_t5

	c_pbc_t50 = S.Task('c_pbc_t50', length=1, delay_cost=1)
	c_pbc_t50 += alt(MAS)

	c_pbc_t50_mem0 = S.Task('c_pbc_t50_mem0', length=1, delay_cost=1)
	c_pbc_t50_mem0 += MAS_MEM[4]
	S += 82 < c_pbc_t50_mem0
	S += c_pbc_t50_mem0 <= c_pbc_t50

	c_pbc_t50_mem1 = S.Task('c_pbc_t50_mem1', length=1, delay_cost=1)
	c_pbc_t50_mem1 += alt(MAS_MEM)
	S += (c_pbc_t10*MAS[0])-1 < c_pbc_t50_mem1*MAS_MEM[1]
	S += (c_pbc_t10*MAS[1])-1 < c_pbc_t50_mem1*MAS_MEM[3]
	S += (c_pbc_t10*MAS[2])-1 < c_pbc_t50_mem1*MAS_MEM[5]
	S += (c_pbc_t10*MAS[3])-1 < c_pbc_t50_mem1*MAS_MEM[7]
	S += c_pbc_t50_mem1 <= c_pbc_t50

	c_pcb_t01 = S.Task('c_pcb_t01', length=1, delay_cost=1)
	c_pcb_t01 += alt(MAS)

	c_pcb_t01_mem0 = S.Task('c_pcb_t01_mem0', length=1, delay_cost=1)
	c_pcb_t01_mem0 += alt(MM_MEM)
	S += (c_pcb_t0_t4*MM[0])-1 < c_pcb_t01_mem0*MM_MEM[0]
	S += c_pcb_t01_mem0 <= c_pcb_t01

	c_pcb_t01_mem1 = S.Task('c_pcb_t01_mem1', length=1, delay_cost=1)
	c_pcb_t01_mem1 += alt(MAS_MEM)
	S += (c_pcb_t0_t5*MAS[0])-1 < c_pcb_t01_mem1*MAS_MEM[1]
	S += (c_pcb_t0_t5*MAS[1])-1 < c_pcb_t01_mem1*MAS_MEM[3]
	S += (c_pcb_t0_t5*MAS[2])-1 < c_pcb_t01_mem1*MAS_MEM[5]
	S += (c_pcb_t0_t5*MAS[3])-1 < c_pcb_t01_mem1*MAS_MEM[7]
	S += c_pcb_t01_mem1 <= c_pcb_t01

	c_pcb_t4_t4_in = S.Task('c_pcb_t4_t4_in', length=1, delay_cost=1)
	c_pcb_t4_t4_in += alt(MM_in)
	c_pcb_t4_t4 = S.Task('c_pcb_t4_t4', length=6, delay_cost=1)
	c_pcb_t4_t4 += alt(MM)
	S += c_pcb_t4_t4>=c_pcb_t4_t4_in

	c_pcb_t4_t4_mem0 = S.Task('c_pcb_t4_t4_mem0', length=1, delay_cost=1)
	c_pcb_t4_t4_mem0 += alt(MAS_MEM)
	S += (c_pcb_t4_t2*MAS[0])-1 < c_pcb_t4_t4_mem0*MAS_MEM[0]
	S += (c_pcb_t4_t2*MAS[1])-1 < c_pcb_t4_t4_mem0*MAS_MEM[2]
	S += (c_pcb_t4_t2*MAS[2])-1 < c_pcb_t4_t4_mem0*MAS_MEM[4]
	S += (c_pcb_t4_t2*MAS[3])-1 < c_pcb_t4_t4_mem0*MAS_MEM[6]
	S += c_pcb_t4_t4_mem0 <= c_pcb_t4_t4

	c_pcb_t4_t4_mem1 = S.Task('c_pcb_t4_t4_mem1', length=1, delay_cost=1)
	c_pcb_t4_t4_mem1 += MAS_MEM[3]
	S += 64 < c_pcb_t4_t4_mem1
	S += c_pcb_t4_t4_mem1 <= c_pcb_t4_t4

	c_pcb_t40 = S.Task('c_pcb_t40', length=1, delay_cost=1)
	c_pcb_t40 += alt(MAS)

	c_pcb_t40_mem0 = S.Task('c_pcb_t40_mem0', length=1, delay_cost=1)
	c_pcb_t40_mem0 += alt(MM_MEM)
	S += (c_pcb_t4_t0*MM[0])-1 < c_pcb_t40_mem0*MM_MEM[0]
	S += c_pcb_t40_mem0 <= c_pcb_t40

	c_pcb_t40_mem1 = S.Task('c_pcb_t40_mem1', length=1, delay_cost=1)
	c_pcb_t40_mem1 += alt(MM_MEM)
	S += (c_pcb_t4_t1*MM[0])-1 < c_pcb_t40_mem1*MM_MEM[1]
	S += c_pcb_t40_mem1 <= c_pcb_t40

	c_pcb_t4_t5 = S.Task('c_pcb_t4_t5', length=1, delay_cost=1)
	c_pcb_t4_t5 += alt(MAS)

	c_pcb_t4_t5_mem0 = S.Task('c_pcb_t4_t5_mem0', length=1, delay_cost=1)
	c_pcb_t4_t5_mem0 += alt(MM_MEM)
	S += (c_pcb_t4_t0*MM[0])-1 < c_pcb_t4_t5_mem0*MM_MEM[0]
	S += c_pcb_t4_t5_mem0 <= c_pcb_t4_t5

	c_pcb_t4_t5_mem1 = S.Task('c_pcb_t4_t5_mem1', length=1, delay_cost=1)
	c_pcb_t4_t5_mem1 += alt(MM_MEM)
	S += (c_pcb_t4_t1*MM[0])-1 < c_pcb_t4_t5_mem1*MM_MEM[1]
	S += c_pcb_t4_t5_mem1 <= c_pcb_t4_t5

	c_pcb_s00 = S.Task('c_pcb_s00', length=1, delay_cost=1)
	c_pcb_s00 += alt(MAS)

	c_pcb_s00_mem0 = S.Task('c_pcb_s00_mem0', length=1, delay_cost=1)
	c_pcb_s00_mem0 += MAS_MEM[2]
	S += 80 < c_pcb_s00_mem0
	S += c_pcb_s00_mem0 <= c_pcb_s00

	c_pcb_s00_mem1 = S.Task('c_pcb_s00_mem1', length=1, delay_cost=1)
	c_pcb_s00_mem1 += alt(MAS_MEM)
	S += (c_pcb_t11*MAS[0])-1 < c_pcb_s00_mem1*MAS_MEM[1]
	S += (c_pcb_t11*MAS[1])-1 < c_pcb_s00_mem1*MAS_MEM[3]
	S += (c_pcb_t11*MAS[2])-1 < c_pcb_s00_mem1*MAS_MEM[5]
	S += (c_pcb_t11*MAS[3])-1 < c_pcb_s00_mem1*MAS_MEM[7]
	S += c_pcb_s00_mem1 <= c_pcb_s00

	c_pcb_s01 = S.Task('c_pcb_s01', length=1, delay_cost=1)
	c_pcb_s01 += alt(MAS)

	c_pcb_s01_mem0 = S.Task('c_pcb_s01_mem0', length=1, delay_cost=1)
	c_pcb_s01_mem0 += alt(MAS_MEM)
	S += (c_pcb_t11*MAS[0])-1 < c_pcb_s01_mem0*MAS_MEM[0]
	S += (c_pcb_t11*MAS[1])-1 < c_pcb_s01_mem0*MAS_MEM[2]
	S += (c_pcb_t11*MAS[2])-1 < c_pcb_s01_mem0*MAS_MEM[4]
	S += (c_pcb_t11*MAS[3])-1 < c_pcb_s01_mem0*MAS_MEM[6]
	S += c_pcb_s01_mem0 <= c_pcb_s01

	c_pcb_s01_mem1 = S.Task('c_pcb_s01_mem1', length=1, delay_cost=1)
	c_pcb_s01_mem1 += MAS_MEM[3]
	S += 80 < c_pcb_s01_mem1
	S += c_pcb_s01_mem1 <= c_pcb_s01

	c_pcb_t50 = S.Task('c_pcb_t50', length=1, delay_cost=1)
	c_pcb_t50 += alt(MAS)

	c_pcb_t50_mem0 = S.Task('c_pcb_t50_mem0', length=1, delay_cost=1)
	c_pcb_t50_mem0 += alt(MAS_MEM)
	S += (c_pcb_t00*MAS[0])-1 < c_pcb_t50_mem0*MAS_MEM[0]
	S += (c_pcb_t00*MAS[1])-1 < c_pcb_t50_mem0*MAS_MEM[2]
	S += (c_pcb_t00*MAS[2])-1 < c_pcb_t50_mem0*MAS_MEM[4]
	S += (c_pcb_t00*MAS[3])-1 < c_pcb_t50_mem0*MAS_MEM[6]
	S += c_pcb_t50_mem0 <= c_pcb_t50

	c_pcb_t50_mem1 = S.Task('c_pcb_t50_mem1', length=1, delay_cost=1)
	c_pcb_t50_mem1 += MAS_MEM[3]
	S += 80 < c_pcb_t50_mem1
	S += c_pcb_t50_mem1 <= c_pcb_t50

	c_paa_t01 = S.Task('c_paa_t01', length=1, delay_cost=1)
	c_paa_t01 += alt(MAS)

	c_paa_t01_mem0 = S.Task('c_paa_t01_mem0', length=1, delay_cost=1)
	c_paa_t01_mem0 += alt(MM_MEM)
	S += (c_paa_t0_t4*MM[0])-1 < c_paa_t01_mem0*MM_MEM[0]
	S += c_paa_t01_mem0 <= c_paa_t01

	c_paa_t01_mem1 = S.Task('c_paa_t01_mem1', length=1, delay_cost=1)
	c_paa_t01_mem1 += alt(MAS_MEM)
	S += (c_paa_t0_t5*MAS[0])-1 < c_paa_t01_mem1*MAS_MEM[1]
	S += (c_paa_t0_t5*MAS[1])-1 < c_paa_t01_mem1*MAS_MEM[3]
	S += (c_paa_t0_t5*MAS[2])-1 < c_paa_t01_mem1*MAS_MEM[5]
	S += (c_paa_t0_t5*MAS[3])-1 < c_paa_t01_mem1*MAS_MEM[7]
	S += c_paa_t01_mem1 <= c_paa_t01

	c_paa_t4_t4_in = S.Task('c_paa_t4_t4_in', length=1, delay_cost=1)
	c_paa_t4_t4_in += alt(MM_in)
	c_paa_t4_t4 = S.Task('c_paa_t4_t4', length=6, delay_cost=1)
	c_paa_t4_t4 += alt(MM)
	S += c_paa_t4_t4>=c_paa_t4_t4_in

	c_paa_t4_t4_mem0 = S.Task('c_paa_t4_t4_mem0', length=1, delay_cost=1)
	c_paa_t4_t4_mem0 += alt(MAS_MEM)
	S += (c_paa_t4_t2*MAS[0])-1 < c_paa_t4_t4_mem0*MAS_MEM[0]
	S += (c_paa_t4_t2*MAS[1])-1 < c_paa_t4_t4_mem0*MAS_MEM[2]
	S += (c_paa_t4_t2*MAS[2])-1 < c_paa_t4_t4_mem0*MAS_MEM[4]
	S += (c_paa_t4_t2*MAS[3])-1 < c_paa_t4_t4_mem0*MAS_MEM[6]
	S += c_paa_t4_t4_mem0 <= c_paa_t4_t4

	c_paa_t4_t4_mem1 = S.Task('c_paa_t4_t4_mem1', length=1, delay_cost=1)
	c_paa_t4_t4_mem1 += MAS_MEM[7]
	S += 68 < c_paa_t4_t4_mem1
	S += c_paa_t4_t4_mem1 <= c_paa_t4_t4

	c_paa_t40 = S.Task('c_paa_t40', length=1, delay_cost=1)
	c_paa_t40 += alt(MAS)

	c_paa_t40_mem0 = S.Task('c_paa_t40_mem0', length=1, delay_cost=1)
	c_paa_t40_mem0 += alt(MM_MEM)
	S += (c_paa_t4_t0*MM[0])-1 < c_paa_t40_mem0*MM_MEM[0]
	S += c_paa_t40_mem0 <= c_paa_t40

	c_paa_t40_mem1 = S.Task('c_paa_t40_mem1', length=1, delay_cost=1)
	c_paa_t40_mem1 += alt(MM_MEM)
	S += (c_paa_t4_t1*MM[0])-1 < c_paa_t40_mem1*MM_MEM[1]
	S += c_paa_t40_mem1 <= c_paa_t40

	c_paa_t4_t5 = S.Task('c_paa_t4_t5', length=1, delay_cost=1)
	c_paa_t4_t5 += alt(MAS)

	c_paa_t4_t5_mem0 = S.Task('c_paa_t4_t5_mem0', length=1, delay_cost=1)
	c_paa_t4_t5_mem0 += alt(MM_MEM)
	S += (c_paa_t4_t0*MM[0])-1 < c_paa_t4_t5_mem0*MM_MEM[0]
	S += c_paa_t4_t5_mem0 <= c_paa_t4_t5

	c_paa_t4_t5_mem1 = S.Task('c_paa_t4_t5_mem1', length=1, delay_cost=1)
	c_paa_t4_t5_mem1 += alt(MM_MEM)
	S += (c_paa_t4_t1*MM[0])-1 < c_paa_t4_t5_mem1*MM_MEM[1]
	S += c_paa_t4_t5_mem1 <= c_paa_t4_t5

	c_paa_s00 = S.Task('c_paa_s00', length=1, delay_cost=1)
	c_paa_s00 += alt(MAS)

	c_paa_s00_mem0 = S.Task('c_paa_s00_mem0', length=1, delay_cost=1)
	c_paa_s00_mem0 += MAS_MEM[2]
	S += 94 < c_paa_s00_mem0
	S += c_paa_s00_mem0 <= c_paa_s00

	c_paa_s00_mem1 = S.Task('c_paa_s00_mem1', length=1, delay_cost=1)
	c_paa_s00_mem1 += alt(MAS_MEM)
	S += (c_paa_t11*MAS[0])-1 < c_paa_s00_mem1*MAS_MEM[1]
	S += (c_paa_t11*MAS[1])-1 < c_paa_s00_mem1*MAS_MEM[3]
	S += (c_paa_t11*MAS[2])-1 < c_paa_s00_mem1*MAS_MEM[5]
	S += (c_paa_t11*MAS[3])-1 < c_paa_s00_mem1*MAS_MEM[7]
	S += c_paa_s00_mem1 <= c_paa_s00

	c_paa_s01 = S.Task('c_paa_s01', length=1, delay_cost=1)
	c_paa_s01 += alt(MAS)

	c_paa_s01_mem0 = S.Task('c_paa_s01_mem0', length=1, delay_cost=1)
	c_paa_s01_mem0 += alt(MAS_MEM)
	S += (c_paa_t11*MAS[0])-1 < c_paa_s01_mem0*MAS_MEM[0]
	S += (c_paa_t11*MAS[1])-1 < c_paa_s01_mem0*MAS_MEM[2]
	S += (c_paa_t11*MAS[2])-1 < c_paa_s01_mem0*MAS_MEM[4]
	S += (c_paa_t11*MAS[3])-1 < c_paa_s01_mem0*MAS_MEM[6]
	S += c_paa_s01_mem0 <= c_paa_s01

	c_paa_s01_mem1 = S.Task('c_paa_s01_mem1', length=1, delay_cost=1)
	c_paa_s01_mem1 += MAS_MEM[3]
	S += 94 < c_paa_s01_mem1
	S += c_paa_s01_mem1 <= c_paa_s01

	c_paa_t50 = S.Task('c_paa_t50', length=1, delay_cost=1)
	c_paa_t50 += alt(MAS)

	c_paa_t50_mem0 = S.Task('c_paa_t50_mem0', length=1, delay_cost=1)
	c_paa_t50_mem0 += alt(MAS_MEM)
	S += (c_paa_t00*MAS[0])-1 < c_paa_t50_mem0*MAS_MEM[0]
	S += (c_paa_t00*MAS[1])-1 < c_paa_t50_mem0*MAS_MEM[2]
	S += (c_paa_t00*MAS[2])-1 < c_paa_t50_mem0*MAS_MEM[4]
	S += (c_paa_t00*MAS[3])-1 < c_paa_t50_mem0*MAS_MEM[6]
	S += c_paa_t50_mem0 <= c_paa_t50

	c_paa_t50_mem1 = S.Task('c_paa_t50_mem1', length=1, delay_cost=1)
	c_paa_t50_mem1 += MAS_MEM[3]
	S += 94 < c_paa_t50_mem1
	S += c_paa_t50_mem1 <= c_paa_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage6MM1_stage1MAS4/INV/schedule9.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

