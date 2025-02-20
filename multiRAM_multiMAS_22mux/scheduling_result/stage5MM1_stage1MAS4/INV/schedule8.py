from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 181
	S = Scenario("schedule8", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling
	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 0
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 0
	c_aa_t3_t0_mem0 += MAIN_MEM_r

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 0
	c_aa_t3_t0_mem1 += MAIN_MEM_r

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=5, delay_cost=1)
	S += c_aa_t3_t0 >= 1
	c_aa_t3_t0 += MM[0]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 1
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 1
	c_bb_t3_t1_mem0 += MAIN_MEM_r

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 1
	c_bb_t3_t1_mem1 += MAIN_MEM_r

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 2
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 2
	c_aa_t3_t1_mem0 += MAIN_MEM_r

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 2
	c_aa_t3_t1_mem1 += MAIN_MEM_r

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=5, delay_cost=1)
	S += c_bb_t3_t1 >= 2
	c_bb_t3_t1 += MM[0]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=5, delay_cost=1)
	S += c_aa_t3_t1 >= 3
	c_aa_t3_t1 += MM[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 3
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 3
	c_bb_t3_t0_mem0 += MAIN_MEM_r

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 3
	c_bb_t3_t0_mem1 += MAIN_MEM_r

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 4
	c_aa_t3_t3_mem0 += MAIN_MEM_r

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 4
	c_aa_t3_t3_mem1 += MAIN_MEM_r

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=5, delay_cost=1)
	S += c_bb_t3_t0 >= 4
	c_bb_t3_t0 += MM[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=1, delay_cost=1)
	S += c_aa_t3_t3 >= 5
	c_aa_t3_t3 += MAS[2]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 5
	c_cc_t10_mem0 += MAIN_MEM_r

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 5
	c_cc_t10_mem1 += MAIN_MEM_r

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 6
	c_bb_t3_t3_mem0 += MAIN_MEM_r

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 6
	c_bb_t3_t3_mem1 += MAIN_MEM_r

	c_cc_t10 = S.Task('c_cc_t10', length=1, delay_cost=1)
	S += c_cc_t10 >= 6
	c_cc_t10 += MAS[0]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 7
	c_aa_a1_0_mem0 += MAIN_MEM_r

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 7
	c_aa_a1_0_mem1 += MAIN_MEM_r

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 7
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 7
	c_aa_t3_t5_mem1 += MM_MEM[0]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=1, delay_cost=1)
	S += c_bb_t3_t3 >= 7
	c_bb_t3_t3 += MAS[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=1, delay_cost=1)
	S += c_aa_a1_0 >= 8
	c_aa_a1_0 += MAS[1]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 8
	c_aa_t3_t2_mem0 += MAIN_MEM_r

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 8
	c_aa_t3_t2_mem1 += MAIN_MEM_r

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=1, delay_cost=1)
	S += c_aa_t3_t5 >= 8
	c_aa_t3_t5 += MAS[2]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 8
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 8
	c_bb_t30_mem1 += MM_MEM[0]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=1, delay_cost=1)
	S += c_aa_t3_t2 >= 9
	c_aa_t3_t2 += MAS[0]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 9
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 9
	c_aa_t3_t4_mem0 += MAS_MEM[0]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 9
	c_aa_t3_t4_mem1 += MAS_MEM[2]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 9
	c_bb10_mem0 += MAS_MEM[1]

	c_bb10_mem1 = S.Task('c_bb10_mem1', length=1, delay_cost=1)
	S += c_bb10_mem1 >= 9
	c_bb10_mem1 += MAS_MEM[1]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 9
	c_bb_a1_0_mem0 += MAIN_MEM_r

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 9
	c_bb_a1_0_mem1 += MAIN_MEM_r

	c_bb_t30 = S.Task('c_bb_t30', length=1, delay_cost=1)
	S += c_bb_t30 >= 9
	c_bb_t30 += MAS[1]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 9
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 9
	c_bb_t3_t5_mem1 += MM_MEM[0]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 10
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 10
	c_aa_t30_mem1 += MM_MEM[0]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=5, delay_cost=1)
	S += c_aa_t3_t4 >= 10
	c_aa_t3_t4 += MM[0]

	c_bb10 = S.Task('c_bb10', length=1, delay_cost=1)
	S += c_bb10 >= 10
	c_bb10 += MAS[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=1, delay_cost=1)
	S += c_bb_a1_0 >= 10
	c_bb_a1_0 += MAS[2]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 10
	c_bb_t10_mem0 += MAIN_MEM_r

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 10
	c_bb_t10_mem1 += MAIN_MEM_r

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=1, delay_cost=1)
	S += c_bb_t3_t5 >= 10
	c_bb_t3_t5 += MAS[0]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 11
	c_aa10_mem0 += MAS_MEM[0]

	c_aa10_mem1 = S.Task('c_aa10_mem1', length=1, delay_cost=1)
	S += c_aa10_mem1 >= 11
	c_aa10_mem1 += MAS_MEM[0]

	c_aa_t30 = S.Task('c_aa_t30', length=1, delay_cost=1)
	S += c_aa_t30 >= 11
	c_aa_t30 += MAS[0]

	c_bb_t10 = S.Task('c_bb_t10', length=1, delay_cost=1)
	S += c_bb_t10 >= 11
	c_bb_t10 += MAS[1]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 11
	c_cc_a1_0_mem0 += MAIN_MEM_r

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 11
	c_cc_a1_0_mem1 += MAIN_MEM_r

	c_aa10 = S.Task('c_aa10', length=1, delay_cost=1)
	S += c_aa10 >= 12
	c_aa10 += MAS[1]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 12
	c_bb_t11_mem0 += MAIN_MEM_r

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 12
	c_bb_t11_mem1 += MAIN_MEM_r

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=1, delay_cost=1)
	S += c_cc_a1_0 >= 12
	c_cc_a1_0 += MAS[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 13
	c_aa_a1_1_mem0 += MAIN_MEM_r

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 13
	c_aa_a1_1_mem1 += MAIN_MEM_r

	c_bb_t11 = S.Task('c_bb_t11', length=1, delay_cost=1)
	S += c_bb_t11 >= 13
	c_bb_t11 += MAS[1]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 13
	c_bb_t2_t3_mem0 += MAS_MEM[1]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 13
	c_bb_t2_t3_mem1 += MAS_MEM[1]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=1, delay_cost=1)
	S += c_aa_a1_1 >= 14
	c_aa_a1_1 += MAS[0]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 14
	c_aa_t11_mem0 += MAIN_MEM_r

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 14
	c_aa_t11_mem1 += MAIN_MEM_r

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 14
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 14
	c_aa_t31_mem1 += MAS_MEM[2]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=1, delay_cost=1)
	S += c_bb_t2_t3 >= 14
	c_bb_t2_t3 += MAS[1]

	c_aa_t11 = S.Task('c_aa_t11', length=1, delay_cost=1)
	S += c_aa_t11 >= 15
	c_aa_t11 += MAS[1]

	c_aa_t31 = S.Task('c_aa_t31', length=1, delay_cost=1)
	S += c_aa_t31 >= 15
	c_aa_t31 += MAS[0]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 15
	c_aa_t40_mem0 += MAS_MEM[0]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 15
	c_aa_t40_mem1 += MAS_MEM[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 15
	c_bb_a1_1_mem0 += MAIN_MEM_r

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 15
	c_bb_a1_1_mem1 += MAIN_MEM_r

	c_aa_t40 = S.Task('c_aa_t40', length=1, delay_cost=1)
	S += c_aa_t40 >= 16
	c_aa_t40 += MAS[0]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 16
	c_aa_t41_mem0 += MAS_MEM[0]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 16
	c_aa_t41_mem1 += MAS_MEM[0]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=1, delay_cost=1)
	S += c_bb_a1_1 >= 16
	c_bb_a1_1 += MAS[2]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 16
	c_bb_t3_t2_mem0 += MAIN_MEM_r

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 16
	c_bb_t3_t2_mem1 += MAIN_MEM_r

	c_aa_t41 = S.Task('c_aa_t41', length=1, delay_cost=1)
	S += c_aa_t41 >= 17
	c_aa_t41 += MAS[2]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=1, delay_cost=1)
	S += c_bb_t3_t2 >= 17
	c_bb_t3_t2 += MAS[0]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 17
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 17
	c_bb_t3_t4_mem0 += MAS_MEM[0]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 17
	c_bb_t3_t4_mem1 += MAS_MEM[0]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 17
	c_cc_a1_1_mem0 += MAIN_MEM_r

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 17
	c_cc_a1_1_mem1 += MAIN_MEM_r

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 18
	c_aa11_mem0 += MAS_MEM[0]

	c_aa11_mem1 = S.Task('c_aa11_mem1', length=1, delay_cost=1)
	S += c_aa11_mem1 >= 18
	c_aa11_mem1 += MAS_MEM[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 18
	c_aa_t10_mem0 += MAIN_MEM_r

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 18
	c_aa_t10_mem1 += MAIN_MEM_r

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=5, delay_cost=1)
	S += c_bb_t3_t4 >= 18
	c_bb_t3_t4 += MM[0]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=1, delay_cost=1)
	S += c_cc_a1_1 >= 18
	c_cc_a1_1 += MAS[3]

	c_aa11 = S.Task('c_aa11', length=1, delay_cost=1)
	S += c_aa11 >= 19
	c_aa11 += MAS[0]

	c_aa_t10 = S.Task('c_aa_t10', length=1, delay_cost=1)
	S += c_aa_t10 >= 19
	c_aa_t10 += MAS[1]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 19
	c_aa_t2_t3_mem0 += MAS_MEM[1]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 19
	c_aa_t2_t3_mem1 += MAS_MEM[1]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	S += c_aa_t50_mem0 >= 19
	c_aa_t50_mem0 += MAS_MEM[0]

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	S += c_aa_t50_mem1 >= 19
	c_aa_t50_mem1 += MAS_MEM[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 19
	c_cc_t11_mem0 += MAIN_MEM_r

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 19
	c_cc_t11_mem1 += MAIN_MEM_r

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=1, delay_cost=1)
	S += c_aa_t2_t3 >= 20
	c_aa_t2_t3 += MAS[0]

	c_aa_t50 = S.Task('c_aa_t50', length=1, delay_cost=1)
	S += c_aa_t50 >= 20
	c_aa_t50 += MAS[3]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	S += c_aa_t51_mem0 >= 20
	c_aa_t51_mem0 += MAS_MEM[0]

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	S += c_aa_t51_mem1 >= 20
	c_aa_t51_mem1 += MAS_MEM[2]

	c_cc_t11 = S.Task('c_cc_t11', length=1, delay_cost=1)
	S += c_cc_t11 >= 20
	c_cc_t11 += MAS[2]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 20
	c_cc_t2_t3_mem0 += MAS_MEM[0]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 20
	c_cc_t2_t3_mem1 += MAS_MEM[2]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 20
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 20
	c_cc_t3_t1_mem0 += MAIN_MEM_r

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 20
	c_cc_t3_t1_mem1 += MAIN_MEM_r

	c_aa_t51 = S.Task('c_aa_t51', length=1, delay_cost=1)
	S += c_aa_t51 >= 21
	c_aa_t51 += MAS[3]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 21
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 21
	c_ab_t1_t1_mem0 += MAIN_MEM_r

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 21
	c_ab_t1_t1_mem1 += MAIN_MEM_r

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=1, delay_cost=1)
	S += c_cc_t2_t3 >= 21
	c_cc_t2_t3 += MAS[0]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=5, delay_cost=1)
	S += c_cc_t3_t1 >= 21
	c_cc_t3_t1 += MM[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 22
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 22
	c_ab_t1_t0_mem0 += MAIN_MEM_r

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 22
	c_ab_t1_t0_mem1 += MAIN_MEM_r

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=5, delay_cost=1)
	S += c_ab_t1_t1 >= 22
	c_ab_t1_t1 += MM[0]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 22
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 22
	c_bb_t31_mem1 += MAS_MEM[0]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=5, delay_cost=1)
	S += c_ab_t1_t0 >= 23
	c_ab_t1_t0 += MM[0]

	c_bb_t31 = S.Task('c_bb_t31', length=1, delay_cost=1)
	S += c_bb_t31 >= 23
	c_bb_t31 += MAS[3]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 23
	c_bb_t40_mem0 += MAS_MEM[1]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 23
	c_bb_t40_mem1 += MAS_MEM[3]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 23
	c_bb_t41_mem0 += MAS_MEM[3]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 23
	c_bb_t41_mem1 += MAS_MEM[1]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 23
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 23
	c_bc_t0_t0_mem0 += MAIN_MEM_r

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 23
	c_bc_t0_t0_mem1 += MAIN_MEM_r

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 24
	c_bb11_mem0 += MAS_MEM[3]

	c_bb11_mem1 = S.Task('c_bb11_mem1', length=1, delay_cost=1)
	S += c_bb11_mem1 >= 24
	c_bb11_mem1 += MAS_MEM[3]

	c_bb_t40 = S.Task('c_bb_t40', length=1, delay_cost=1)
	S += c_bb_t40 >= 24
	c_bb_t40 += MAS[0]

	c_bb_t41 = S.Task('c_bb_t41', length=1, delay_cost=1)
	S += c_bb_t41 >= 24
	c_bb_t41 += MAS[3]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	S += c_bb_t50_mem0 >= 24
	c_bb_t50_mem0 += MAS_MEM[1]

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	S += c_bb_t50_mem1 >= 24
	c_bb_t50_mem1 += MAS_MEM[0]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=5, delay_cost=1)
	S += c_bc_t0_t0 >= 24
	c_bc_t0_t0 += MM[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 24
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 24
	c_bc_t0_t1_mem0 += MAIN_MEM_r

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 24
	c_bc_t0_t1_mem1 += MAIN_MEM_r

	c_bb11 = S.Task('c_bb11', length=1, delay_cost=1)
	S += c_bb11 >= 25
	c_bb11 += MAS[0]

	c_bb_t50 = S.Task('c_bb_t50', length=1, delay_cost=1)
	S += c_bb_t50 >= 25
	c_bb_t50 += MAS[1]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	S += c_bb_t51_mem0 >= 25
	c_bb_t51_mem0 += MAS_MEM[3]

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	S += c_bb_t51_mem1 >= 25
	c_bb_t51_mem1 += MAS_MEM[3]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=5, delay_cost=1)
	S += c_bc_t0_t1 >= 25
	c_bc_t0_t1 += MM[0]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 25
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 25
	c_cc_t3_t0_mem0 += MAIN_MEM_r

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 25
	c_cc_t3_t0_mem1 += MAIN_MEM_r

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 26
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 26
	c_ab_t0_t1_mem0 += MAIN_MEM_r

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 26
	c_ab_t0_t1_mem1 += MAIN_MEM_r

	c_bb_t51 = S.Task('c_bb_t51', length=1, delay_cost=1)
	S += c_bb_t51 >= 26
	c_bb_t51 += MAS[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=5, delay_cost=1)
	S += c_cc_t3_t0 >= 26
	c_cc_t3_t0 += MM[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 27
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 27
	c_ab_t0_t0_mem0 += MAIN_MEM_r

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 27
	c_ab_t0_t0_mem1 += MAIN_MEM_r

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=5, delay_cost=1)
	S += c_ab_t0_t1 >= 27
	c_ab_t0_t1 += MM[0]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 27
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 27
	c_ab_t10_mem1 += MM_MEM[0]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=5, delay_cost=1)
	S += c_ab_t0_t0 >= 28
	c_ab_t0_t0 += MM[0]

	c_ab_t10 = S.Task('c_ab_t10', length=1, delay_cost=1)
	S += c_ab_t10 >= 28
	c_ab_t10 += MAS[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 28
	c_ab_t1_t3_mem0 += MAIN_MEM_r

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 28
	c_ab_t1_t3_mem1 += MAIN_MEM_r

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 28
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 28
	c_ab_t1_t5_mem1 += MM_MEM[0]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=1, delay_cost=1)
	S += c_ab_t1_t3 >= 29
	c_ab_t1_t3 += MAS[0]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=1, delay_cost=1)
	S += c_ab_t1_t5 >= 29
	c_ab_t1_t5 += MAS[1]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 29
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 29
	c_bc_t00_mem1 += MM_MEM[0]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 29
	c_bc_t0_t3_mem0 += MAIN_MEM_r

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 29
	c_bc_t0_t3_mem1 += MAIN_MEM_r

	c_bc_t00 = S.Task('c_bc_t00', length=1, delay_cost=1)
	S += c_bc_t00 >= 30
	c_bc_t00 += MAS[0]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 30
	c_bc_t0_t2_mem0 += MAIN_MEM_r

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 30
	c_bc_t0_t2_mem1 += MAIN_MEM_r

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=1, delay_cost=1)
	S += c_bc_t0_t3 >= 30
	c_bc_t0_t3 += MAS[1]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 30
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 30
	c_cc_t3_t5_mem1 += MM_MEM[0]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 31
	c_ab_t31_mem0 += MAIN_MEM_r

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 31
	c_ab_t31_mem1 += MAIN_MEM_r

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=1, delay_cost=1)
	S += c_bc_t0_t2 >= 31
	c_bc_t0_t2 += MAS[3]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 31
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 31
	c_bc_t0_t4_mem0 += MAS_MEM[3]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 31
	c_bc_t0_t4_mem1 += MAS_MEM[1]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 31
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 31
	c_cc_t30_mem1 += MM_MEM[0]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=1, delay_cost=1)
	S += c_cc_t3_t5 >= 31
	c_cc_t3_t5 += MAS[0]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 32
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 32
	c_ab_t00_mem1 += MM_MEM[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 32
	c_ab_t1_t2_mem0 += MAIN_MEM_r

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 32
	c_ab_t1_t2_mem1 += MAIN_MEM_r

	c_ab_t31 = S.Task('c_ab_t31', length=1, delay_cost=1)
	S += c_ab_t31 >= 32
	c_ab_t31 += MAS[1]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=5, delay_cost=1)
	S += c_bc_t0_t4 >= 32
	c_bc_t0_t4 += MM[0]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 32
	c_cc10_mem0 += MAS_MEM[0]

	c_cc10_mem1 = S.Task('c_cc10_mem1', length=1, delay_cost=1)
	S += c_cc10_mem1 >= 32
	c_cc10_mem1 += MAS_MEM[0]

	c_cc_t30 = S.Task('c_cc_t30', length=1, delay_cost=1)
	S += c_cc_t30 >= 32
	c_cc_t30 += MAS[0]

	c_ab_t00 = S.Task('c_ab_t00', length=1, delay_cost=1)
	S += c_ab_t00 >= 33
	c_ab_t00 += MAS[0]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 33
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 33
	c_ab_t0_t5_mem1 += MM_MEM[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=1, delay_cost=1)
	S += c_ab_t1_t2 >= 33
	c_ab_t1_t2 += MAS[1]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 33
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 33
	c_ab_t1_t4_mem0 += MAS_MEM[1]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 33
	c_ab_t1_t4_mem1 += MAS_MEM[0]

	c_cc10 = S.Task('c_cc10', length=1, delay_cost=1)
	S += c_cc10 >= 33
	c_cc10 += MAS[2]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 33
	c_cc_t3_t3_mem0 += MAIN_MEM_r

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 33
	c_cc_t3_t3_mem1 += MAIN_MEM_r

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 34
	c_ab_t0_t2_mem0 += MAIN_MEM_r

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 34
	c_ab_t0_t2_mem1 += MAIN_MEM_r

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=1, delay_cost=1)
	S += c_ab_t0_t5 >= 34
	c_ab_t0_t5 += MAS[0]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=5, delay_cost=1)
	S += c_ab_t1_t4 >= 34
	c_ab_t1_t4 += MM[0]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 34
	c_ab_t50_mem0 += MAS_MEM[0]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 34
	c_ab_t50_mem1 += MAS_MEM[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 34
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 34
	c_bc_t0_t5_mem1 += MM_MEM[0]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=1, delay_cost=1)
	S += c_cc_t3_t3 >= 34
	c_cc_t3_t3 += MAS[2]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=1, delay_cost=1)
	S += c_ab_t0_t2 >= 35
	c_ab_t0_t2 += MAS[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 35
	c_ab_t20_mem0 += MAIN_MEM_r

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 35
	c_ab_t20_mem1 += MAIN_MEM_r

	c_ab_t50 = S.Task('c_ab_t50', length=1, delay_cost=1)
	S += c_ab_t50 >= 35
	c_ab_t50 += MAS[3]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=1, delay_cost=1)
	S += c_bc_t0_t5 >= 35
	c_bc_t0_t5 += MAS[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 36
	c_ab_t0_t3_mem0 += MAIN_MEM_r

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 36
	c_ab_t0_t3_mem1 += MAIN_MEM_r

	c_ab_t20 = S.Task('c_ab_t20', length=1, delay_cost=1)
	S += c_ab_t20 >= 36
	c_ab_t20 += MAS[2]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 36
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 36
	c_bc_t01_mem1 += MAS_MEM[1]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=1, delay_cost=1)
	S += c_ab_t0_t3 >= 37
	c_ab_t0_t3 += MAS[2]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 37
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 37
	c_ab_t0_t4_mem0 += MAS_MEM[0]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 37
	c_ab_t0_t4_mem1 += MAS_MEM[2]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 37
	c_ab_t30_mem0 += MAIN_MEM_r

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 37
	c_ab_t30_mem1 += MAIN_MEM_r

	c_bc_t01 = S.Task('c_bc_t01', length=1, delay_cost=1)
	S += c_bc_t01 >= 37
	c_bc_t01 += MAS[0]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=5, delay_cost=1)
	S += c_ab_t0_t4 >= 38
	c_ab_t0_t4 += MM[0]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 38
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 38
	c_ab_t11_mem1 += MAS_MEM[1]

	c_ab_t30 = S.Task('c_ab_t30', length=1, delay_cost=1)
	S += c_ab_t30 >= 38
	c_ab_t30 += MAS[3]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 38
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 38
	c_ab_t4_t0_mem0 += MAS_MEM[2]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 38
	c_ab_t4_t0_mem1 += MAS_MEM[3]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 38
	c_ab_t4_t3_mem0 += MAS_MEM[3]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 38
	c_ab_t4_t3_mem1 += MAS_MEM[1]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 38
	c_cc_t3_t2_mem0 += MAIN_MEM_r

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 38
	c_cc_t3_t2_mem1 += MAIN_MEM_r

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 39
	c_ab_s01_mem0 += MAS_MEM[2]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 39
	c_ab_s01_mem1 += MAS_MEM[0]

	c_ab_t11 = S.Task('c_ab_t11', length=1, delay_cost=1)
	S += c_ab_t11 >= 39
	c_ab_t11 += MAS[2]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 39
	c_ab_t21_mem0 += MAIN_MEM_r

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 39
	c_ab_t21_mem1 += MAIN_MEM_r

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=5, delay_cost=1)
	S += c_ab_t4_t0 >= 39
	c_ab_t4_t0 += MM[0]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=1, delay_cost=1)
	S += c_ab_t4_t3 >= 39
	c_ab_t4_t3 += MAS[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=1, delay_cost=1)
	S += c_cc_t3_t2 >= 39
	c_cc_t3_t2 += MAS[0]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 39
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 39
	c_cc_t3_t4_mem0 += MAS_MEM[0]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 39
	c_cc_t3_t4_mem1 += MAS_MEM[2]

	c_ab_s01 = S.Task('c_ab_s01', length=1, delay_cost=1)
	S += c_ab_s01 >= 40
	c_ab_s01 += MAS[0]

	c_ab_t21 = S.Task('c_ab_t21', length=1, delay_cost=1)
	S += c_ab_t21 >= 40
	c_ab_t21 += MAS[2]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 40
	c_ab_t4_t2_mem0 += MAS_MEM[2]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 40
	c_ab_t4_t2_mem1 += MAS_MEM[2]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 40
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 40
	c_ac_t1_t0_mem0 += MAIN_MEM_r

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 40
	c_ac_t1_t0_mem1 += MAIN_MEM_r

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=5, delay_cost=1)
	S += c_cc_t3_t4 >= 40
	c_cc_t3_t4 += MM[0]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 41
	c_ab_s00_mem0 += MAS_MEM[0]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 41
	c_ab_s00_mem1 += MAS_MEM[2]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=1, delay_cost=1)
	S += c_ab_t4_t2 >= 41
	c_ab_t4_t2 += MAS[0]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 41
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 41
	c_ac_t0_t1_mem0 += MAIN_MEM_r

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 41
	c_ac_t0_t1_mem1 += MAIN_MEM_r

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=5, delay_cost=1)
	S += c_ac_t1_t0 >= 41
	c_ac_t1_t0 += MM[0]

	c_ab_s00 = S.Task('c_ab_s00', length=1, delay_cost=1)
	S += c_ab_s00 >= 42
	c_ab_s00 += MAS[0]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 42
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 42
	c_ab_t01_mem1 += MAS_MEM[0]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=5, delay_cost=1)
	S += c_ac_t0_t1 >= 42
	c_ac_t0_t1 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 42
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 42
	c_bc_t1_t1_mem0 += MAIN_MEM_r

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 42
	c_bc_t1_t1_mem1 += MAIN_MEM_r

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	S += c_ab00_mem0 >= 43
	c_ab00_mem0 += MAS_MEM[0]

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	S += c_ab00_mem1 >= 43
	c_ab00_mem1 += MAS_MEM[0]

	c_ab_t01 = S.Task('c_ab_t01', length=1, delay_cost=1)
	S += c_ab_t01 >= 43
	c_ab_t01 += MAS[1]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 43
	c_ab_t51_mem0 += MAS_MEM[1]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 43
	c_ab_t51_mem1 += MAS_MEM[2]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 43
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 43
	c_bc_t1_t0_mem0 += MAIN_MEM_r

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 43
	c_bc_t1_t0_mem1 += MAIN_MEM_r

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=5, delay_cost=1)
	S += c_bc_t1_t1 >= 43
	c_bc_t1_t1 += MM[0]

	c_ab00 = S.Task('c_ab00', length=1, delay_cost=1)
	S += c_ab00 >= 44
	c_ab00 += MAS[0]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	S += c_ab01_mem0 >= 44
	c_ab01_mem0 += MAS_MEM[1]

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	S += c_ab01_mem1 >= 44
	c_ab01_mem1 += MAS_MEM[0]

	c_ab_t51 = S.Task('c_ab_t51', length=1, delay_cost=1)
	S += c_ab_t51 >= 44
	c_ab_t51 += MAS[1]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 44
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 44
	c_ac_t1_t1_mem0 += MAIN_MEM_r

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 44
	c_ac_t1_t1_mem1 += MAIN_MEM_r

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=5, delay_cost=1)
	S += c_bc_t1_t0 >= 44
	c_bc_t1_t0 += MM[0]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 44
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 44
	c_cc_t31_mem1 += MAS_MEM[0]

	c_ab01 = S.Task('c_ab01', length=1, delay_cost=1)
	S += c_ab01 >= 45
	c_ab01 += MAS[1]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 45
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 45
	c_ac_t0_t0_mem0 += MAIN_MEM_r

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 45
	c_ac_t0_t0_mem1 += MAIN_MEM_r

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=5, delay_cost=1)
	S += c_ac_t1_t1 >= 45
	c_ac_t1_t1 += MM[0]

	c_cc_t31 = S.Task('c_cc_t31', length=1, delay_cost=1)
	S += c_cc_t31 >= 45
	c_cc_t31 += MAS[0]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 45
	c_cc_t41_mem0 += MAS_MEM[0]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 45
	c_cc_t41_mem1 += MAS_MEM[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 46
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 46
	c_ab_t4_t1_mem0 += MAS_MEM[2]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 46
	c_ab_t4_t1_mem1 += MAS_MEM[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=5, delay_cost=1)
	S += c_ac_t0_t0 >= 46
	c_ac_t0_t0 += MM[0]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 46
	c_bc_t1_t3_mem0 += MAIN_MEM_r

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 46
	c_bc_t1_t3_mem1 += MAIN_MEM_r

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 46
	c_cc_t40_mem0 += MAS_MEM[0]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 46
	c_cc_t40_mem1 += MAS_MEM[0]

	c_cc_t41 = S.Task('c_cc_t41', length=1, delay_cost=1)
	S += c_cc_t41 >= 46
	c_cc_t41 += MAS[0]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=5, delay_cost=1)
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

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=1, delay_cost=1)
	S += c_bc_t1_t3 >= 47
	c_bc_t1_t3 += MAS[1]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 47
	c_bc_t21_mem0 += MAIN_MEM_r

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 47
	c_bc_t21_mem1 += MAIN_MEM_r

	c_cc_t40 = S.Task('c_cc_t40', length=1, delay_cost=1)
	S += c_cc_t40 >= 47
	c_cc_t40 += MAS[3]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	S += c_cc_t50_mem0 >= 47
	c_cc_t50_mem0 += MAS_MEM[0]

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	S += c_cc_t50_mem1 >= 47
	c_cc_t50_mem1 += MAS_MEM[3]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=5, delay_cost=1)
	S += c_ab_t4_t4 >= 48
	c_ab_t4_t4 += MM[0]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 48
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 48
	c_bc_t10_mem1 += MM_MEM[0]

	c_bc_t21 = S.Task('c_bc_t21', length=1, delay_cost=1)
	S += c_bc_t21 >= 48
	c_bc_t21 += MAS[1]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 48
	c_bc_t31_mem0 += MAIN_MEM_r

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 48
	c_bc_t31_mem1 += MAIN_MEM_r

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 48
	c_cc11_mem0 += MAS_MEM[0]

	c_cc11_mem1 = S.Task('c_cc11_mem1', length=1, delay_cost=1)
	S += c_cc11_mem1 >= 48
	c_cc11_mem1 += MAS_MEM[0]

	c_cc_t50 = S.Task('c_cc_t50', length=1, delay_cost=1)
	S += c_cc_t50 >= 48
	c_cc_t50 += MAS[3]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 49
	c_ac_t20_mem0 += MAIN_MEM_r

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 49
	c_ac_t20_mem1 += MAIN_MEM_r

	c_bc_t10 = S.Task('c_bc_t10', length=1, delay_cost=1)
	S += c_bc_t10 >= 49
	c_bc_t10 += MAS[1]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 49
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 49
	c_bc_t1_t5_mem1 += MM_MEM[0]

	c_bc_t31 = S.Task('c_bc_t31', length=1, delay_cost=1)
	S += c_bc_t31 >= 49
	c_bc_t31 += MAS[0]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 49
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 49
	c_bc_t4_t1_mem0 += MAS_MEM[1]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 49
	c_bc_t4_t1_mem1 += MAS_MEM[0]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 49
	c_bc_t50_mem0 += MAS_MEM[0]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 49
	c_bc_t50_mem1 += MAS_MEM[1]

	c_cc11 = S.Task('c_cc11', length=1, delay_cost=1)
	S += c_cc11 >= 49
	c_cc11 += MAS[3]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem0 >= 49
	c_ccxi_y1_1_mem0 += MAS_MEM[3]

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem1 >= 49
	c_ccxi_y1_1_mem1 += MAS_MEM[2]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 50
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 50
	c_ac_t00_mem1 += MM_MEM[0]

	c_ac_t20 = S.Task('c_ac_t20', length=1, delay_cost=1)
	S += c_ac_t20 >= 50
	c_ac_t20 += MAS[2]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 50
	c_ac_t21_mem0 += MAIN_MEM_r

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 50
	c_ac_t21_mem1 += MAIN_MEM_r

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=1, delay_cost=1)
	S += c_bc_t1_t5 >= 50
	c_bc_t1_t5 += MAS[0]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=5, delay_cost=1)
	S += c_bc_t4_t1 >= 50
	c_bc_t4_t1 += MM[0]

	c_bc_t50 = S.Task('c_bc_t50', length=1, delay_cost=1)
	S += c_bc_t50 >= 50
	c_bc_t50 += MAS[1]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem0 >= 50
	c_ccxi_y1_0_mem0 += MAS_MEM[2]

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem1 >= 50
	c_ccxi_y1_0_mem1 += MAS_MEM[3]

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=1, delay_cost=1)
	S += c_ccxi_y1_1 >= 50
	c_ccxi_y1_1 += MAS[3]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	S += c_pb01_mem0 >= 50
	c_pb01_mem0 += MAS_MEM[3]

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	S += c_pb01_mem1 >= 50
	c_pb01_mem1 += MAS_MEM[1]

	c_ac_t00 = S.Task('c_ac_t00', length=1, delay_cost=1)
	S += c_ac_t00 >= 51
	c_ac_t00 += MAS[0]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 51
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 51
	c_ac_t0_t5_mem1 += MM_MEM[0]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 51
	c_ac_t1_t3_mem0 += MAIN_MEM_r

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 51
	c_ac_t1_t3_mem1 += MAIN_MEM_r

	c_ac_t21 = S.Task('c_ac_t21', length=1, delay_cost=1)
	S += c_ac_t21 >= 51
	c_ac_t21 += MAS[2]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 51
	c_ac_t4_t2_mem0 += MAS_MEM[2]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 51
	c_ac_t4_t2_mem1 += MAS_MEM[2]

	c_cc_t51_mem0 = S.Task('c_cc_t51_mem0', length=1, delay_cost=1)
	S += c_cc_t51_mem0 >= 51
	c_cc_t51_mem0 += MAS_MEM[0]

	c_cc_t51_mem1 = S.Task('c_cc_t51_mem1', length=1, delay_cost=1)
	S += c_cc_t51_mem1 >= 51
	c_cc_t51_mem1 += MAS_MEM[0]

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=1, delay_cost=1)
	S += c_ccxi_y1_0 >= 51
	c_ccxi_y1_0 += MAS[1]

	c_pb01 = S.Task('c_pb01', length=1, delay_cost=1)
	S += c_pb01 >= 51
	c_pb01 += MAS[3]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=1, delay_cost=1)
	S += c_ac_t0_t5 >= 52
	c_ac_t0_t5 += MAS[0]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 52
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 52
	c_ac_t10_mem1 += MM_MEM[0]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=1, delay_cost=1)
	S += c_ac_t1_t3 >= 52
	c_ac_t1_t3 += MAS[1]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=1, delay_cost=1)
	S += c_ac_t4_t2 >= 52
	c_ac_t4_t2 += MAS[3]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 52
	c_bc_t30_mem0 += MAIN_MEM_r

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 52
	c_bc_t30_mem1 += MAIN_MEM_r

	c_cc_t51 = S.Task('c_cc_t51', length=1, delay_cost=1)
	S += c_cc_t51 >= 52
	c_cc_t51 += MAS[2]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	S += c_pb00_mem0 >= 52
	c_pb00_mem0 += MAS_MEM[1]

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	S += c_pb00_mem1 >= 52
	c_pb00_mem1 += MAS_MEM[0]

	c_ac_t10 = S.Task('c_ac_t10', length=1, delay_cost=1)
	S += c_ac_t10 >= 53
	c_ac_t10 += MAS[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 53
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 53
	c_ac_t1_t5_mem1 += MM_MEM[0]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 53
	c_ac_t31_mem0 += MAIN_MEM_r

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 53
	c_ac_t31_mem1 += MAIN_MEM_r

	c_bc_t30 = S.Task('c_bc_t30', length=1, delay_cost=1)
	S += c_bc_t30 >= 53
	c_bc_t30 += MAS[3]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 53
	c_bc_t4_t3_mem0 += MAS_MEM[3]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 53
	c_bc_t4_t3_mem1 += MAS_MEM[0]

	c_pb00 = S.Task('c_pb00', length=1, delay_cost=1)
	S += c_pb00 >= 53
	c_pb00 += MAS[2]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 54
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 54
	c_ab_t4_t5_mem1 += MM_MEM[0]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=1, delay_cost=1)
	S += c_ac_t1_t5 >= 54
	c_ac_t1_t5 += MAS[1]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 54
	c_ac_t30_mem0 += MAIN_MEM_r

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 54
	c_ac_t30_mem1 += MAIN_MEM_r

	c_ac_t31 = S.Task('c_ac_t31', length=1, delay_cost=1)
	S += c_ac_t31 >= 54
	c_ac_t31 += MAS[0]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 54
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 54
	c_ac_t4_t1_mem0 += MAS_MEM[2]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 54
	c_ac_t4_t1_mem1 += MAS_MEM[0]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=1, delay_cost=1)
	S += c_bc_t4_t3 >= 54
	c_bc_t4_t3 += MAS[3]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 55
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 55
	c_ab_t40_mem1 += MM_MEM[0]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=1, delay_cost=1)
	S += c_ab_t4_t5 >= 55
	c_ab_t4_t5 += MAS[1]

	c_ac_t30 = S.Task('c_ac_t30', length=1, delay_cost=1)
	S += c_ac_t30 >= 55
	c_ac_t30 += MAS[0]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 55
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 55
	c_ac_t4_t0_mem0 += MAS_MEM[2]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 55
	c_ac_t4_t0_mem1 += MAS_MEM[0]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=5, delay_cost=1)
	S += c_ac_t4_t1 >= 55
	c_ac_t4_t1 += MM[0]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 55
	c_bc_t20_mem0 += MAIN_MEM_r

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 55
	c_bc_t20_mem1 += MAIN_MEM_r

	c_ab_t40 = S.Task('c_ab_t40', length=1, delay_cost=1)
	S += c_ab_t40 >= 56
	c_ab_t40 += MAS[1]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 56
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 56
	c_ab_t41_mem1 += MAS_MEM[1]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=5, delay_cost=1)
	S += c_ac_t4_t0 >= 56
	c_ac_t4_t0 += MM[0]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 56
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 56
	c_ac_t4_t3_mem1 += MAS_MEM[0]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 56
	c_bc_t1_t2_mem0 += MAIN_MEM_r

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 56
	c_bc_t1_t2_mem1 += MAIN_MEM_r

	c_bc_t20 = S.Task('c_bc_t20', length=1, delay_cost=1)
	S += c_bc_t20 >= 56
	c_bc_t20 += MAS[3]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 56
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 56
	c_bc_t4_t0_mem0 += MAS_MEM[3]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 56
	c_bc_t4_t0_mem1 += MAS_MEM[3]

	c_ab_t41 = S.Task('c_ab_t41', length=1, delay_cost=1)
	S += c_ab_t41 >= 57
	c_ab_t41 += MAS[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 57
	c_ac_t1_t2_mem0 += MAIN_MEM_r

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 57
	c_ac_t1_t2_mem1 += MAIN_MEM_r

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=1, delay_cost=1)
	S += c_ac_t4_t3 >= 57
	c_ac_t4_t3 += MAS[1]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 57
	c_ac_t50_mem0 += MAS_MEM[0]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 57
	c_ac_t50_mem1 += MAS_MEM[0]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=1, delay_cost=1)
	S += c_bc_t1_t2 >= 57
	c_bc_t1_t2 += MAS[2]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 57
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 57
	c_bc_t1_t4_mem0 += MAS_MEM[2]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 57
	c_bc_t1_t4_mem1 += MAS_MEM[1]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=5, delay_cost=1)
	S += c_bc_t4_t0 >= 57
	c_bc_t4_t0 += MM[0]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 57
	c_bc_t4_t2_mem0 += MAS_MEM[3]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 57
	c_bc_t4_t2_mem1 += MAS_MEM[1]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 58
	c_ab10_mem0 += MAS_MEM[1]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 58
	c_ab10_mem1 += MAS_MEM[3]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 58
	c_ac_t0_t3_mem0 += MAIN_MEM_r

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 58
	c_ac_t0_t3_mem1 += MAIN_MEM_r

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
	c_ac_t1_t4_mem1 += MAS_MEM[1]

	c_ac_t50 = S.Task('c_ac_t50', length=1, delay_cost=1)
	S += c_ac_t50 >= 58
	c_ac_t50 += MAS[1]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=5, delay_cost=1)
	S += c_bc_t1_t4 >= 58
	c_bc_t1_t4 += MM[0]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=1, delay_cost=1)
	S += c_bc_t4_t2 >= 58
	c_bc_t4_t2 += MAS[3]

	c_ab10 = S.Task('c_ab10', length=1, delay_cost=1)
	S += c_ab10 >= 59
	c_ab10 += MAS[0]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	S += c_ab11_mem0 >= 59
	c_ab11_mem0 += MAS_MEM[0]

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	S += c_ab11_mem1 >= 59
	c_ab11_mem1 += MAS_MEM[1]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 59
	c_ac_t0_t2_mem0 += MAIN_MEM_r

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 59
	c_ac_t0_t2_mem1 += MAIN_MEM_r

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=1, delay_cost=1)
	S += c_ac_t0_t3 >= 59
	c_ac_t0_t3 += MAS[3]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=5, delay_cost=1)
	S += c_ac_t1_t4 >= 59
	c_ac_t1_t4 += MM[0]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 59
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 59
	c_ac_t4_t4_mem0 += MAS_MEM[3]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 59
	c_ac_t4_t4_mem1 += MAS_MEM[1]

	c_ab11 = S.Task('c_ab11', length=1, delay_cost=1)
	S += c_ab11 >= 60
	c_ab11 += MAS[0]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=1, delay_cost=1)
	S += c_ac_t0_t2 >= 60
	c_ac_t0_t2 += MAS[3]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 60
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 60
	c_ac_t0_t4_mem0 += MAS_MEM[3]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 60
	c_ac_t0_t4_mem1 += MAS_MEM[3]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=5, delay_cost=1)
	S += c_ac_t4_t4 >= 60
	c_ac_t4_t4 += MM[0]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 60
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 60
	c_ac_t4_t5_mem1 += MM_MEM[0]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 60
	c_pcb_t1_t3_mem0 += MAIN_MEM_r

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 60
	c_pcb_t1_t3_mem1 += MAIN_MEM_r

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=5, delay_cost=1)
	S += c_ac_t0_t4 >= 61
	c_ac_t0_t4 += MM[0]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=1, delay_cost=1)
	S += c_ac_t4_t5 >= 61
	c_ac_t4_t5 += MAS[1]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 61
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 61
	c_bc_t40_mem1 += MM_MEM[0]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 61
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 61
	c_bc_t4_t4_mem0 += MAS_MEM[3]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 61
	c_bc_t4_t4_mem1 += MAS_MEM[3]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=1, delay_cost=1)
	S += c_pcb_t1_t3 >= 61
	c_pcb_t1_t3 += MAS[0]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 61
	c_pcb_t30_mem0 += MAIN_MEM_r

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 61
	c_pcb_t30_mem1 += MAIN_MEM_r

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 62
	c_bc10_mem0 += MAS_MEM[1]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 62
	c_bc10_mem1 += MAS_MEM[1]

	c_bc_t40 = S.Task('c_bc_t40', length=1, delay_cost=1)
	S += c_bc_t40 >= 62
	c_bc_t40 += MAS[1]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=5, delay_cost=1)
	S += c_bc_t4_t4 >= 62
	c_bc_t4_t4 += MM[0]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 62
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 62
	c_bc_t4_t5_mem1 += MM_MEM[0]

	c_pcb_t30 = S.Task('c_pcb_t30', length=1, delay_cost=1)
	S += c_pcb_t30 >= 62
	c_pcb_t30 += MAS[0]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 62
	c_pcb_t31_mem0 += MAIN_MEM_r

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 62
	c_pcb_t31_mem1 += MAIN_MEM_r

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 63
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 63
	c_ac_t40_mem1 += MM_MEM[0]

	c_bc10 = S.Task('c_bc10', length=1, delay_cost=1)
	S += c_bc10 >= 63
	c_bc10 += MAS[2]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=1, delay_cost=1)
	S += c_bc_t4_t5 >= 63
	c_bc_t4_t5 += MAS[1]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 63
	c_paa_t0_t3_mem0 += MAIN_MEM_r

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 63
	c_paa_t0_t3_mem1 += MAIN_MEM_r

	c_pcb_t31 = S.Task('c_pcb_t31', length=1, delay_cost=1)
	S += c_pcb_t31 >= 63
	c_pcb_t31 += MAS[0]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 63
	c_pcb_t4_t3_mem0 += MAS_MEM[0]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 63
	c_pcb_t4_t3_mem1 += MAS_MEM[0]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 64
	c_ac10_mem0 += MAS_MEM[2]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 64
	c_ac10_mem1 += MAS_MEM[1]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 64
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 64
	c_ac_t11_mem1 += MAS_MEM[1]

	c_ac_t40 = S.Task('c_ac_t40', length=1, delay_cost=1)
	S += c_ac_t40 >= 64
	c_ac_t40 += MAS[2]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 64
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 64
	c_bc_t11_mem1 += MAS_MEM[0]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=1, delay_cost=1)
	S += c_paa_t0_t3 >= 64
	c_paa_t0_t3 += MAS[0]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 64
	c_paa_t1_t3_mem0 += MAIN_MEM_r

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 64
	c_paa_t1_t3_mem1 += MAIN_MEM_r

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=1, delay_cost=1)
	S += c_pcb_t4_t3 >= 64
	c_pcb_t4_t3 += MAS[1]

	c_ac10 = S.Task('c_ac10', length=1, delay_cost=1)
	S += c_ac10 >= 65
	c_ac10 += MAS[0]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 65
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 65
	c_ac_t01_mem1 += MAS_MEM[0]

	c_ac_t11 = S.Task('c_ac_t11', length=1, delay_cost=1)
	S += c_ac_t11 >= 65
	c_ac_t11 += MAS[1]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 65
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 65
	c_ac_t41_mem1 += MAS_MEM[1]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 65
	c_bc_s01_mem0 += MAS_MEM[2]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 65
	c_bc_s01_mem1 += MAS_MEM[1]

	c_bc_t11 = S.Task('c_bc_t11', length=1, delay_cost=1)
	S += c_bc_t11 >= 65
	c_bc_t11 += MAS[2]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=1, delay_cost=1)
	S += c_paa_t1_t3 >= 65
	c_paa_t1_t3 += MAS[3]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 65
	c_paa_t30_mem0 += MAIN_MEM_r

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 65
	c_paa_t30_mem1 += MAIN_MEM_r

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 66
	c_ac_s01_mem0 += MAS_MEM[1]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 66
	c_ac_s01_mem1 += MAS_MEM[0]

	c_ac_t01 = S.Task('c_ac_t01', length=1, delay_cost=1)
	S += c_ac_t01 >= 66
	c_ac_t01 += MAS[0]

	c_ac_t41 = S.Task('c_ac_t41', length=1, delay_cost=1)
	S += c_ac_t41 >= 66
	c_ac_t41 += MAS[2]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 66
	c_bc_s00_mem0 += MAS_MEM[1]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 66
	c_bc_s00_mem1 += MAS_MEM[2]

	c_bc_s01 = S.Task('c_bc_s01', length=1, delay_cost=1)
	S += c_bc_s01 >= 66
	c_bc_s01 += MAS[3]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 66
	c_bc_t51_mem0 += MAS_MEM[0]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 66
	c_bc_t51_mem1 += MAS_MEM[2]

	c_paa_t30 = S.Task('c_paa_t30', length=1, delay_cost=1)
	S += c_paa_t30 >= 66
	c_paa_t30 += MAS[1]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 66
	c_paa_t31_mem0 += MAIN_MEM_r

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 66
	c_paa_t31_mem1 += MAIN_MEM_r

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 67
	c_ac_s00_mem0 += MAS_MEM[0]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 67
	c_ac_s00_mem1 += MAS_MEM[1]

	c_ac_s01 = S.Task('c_ac_s01', length=1, delay_cost=1)
	S += c_ac_s01 >= 67
	c_ac_s01 += MAS[1]

	c_bc_s00 = S.Task('c_bc_s00', length=1, delay_cost=1)
	S += c_bc_s00 >= 67
	c_bc_s00 += MAS[3]

	c_bc_t51 = S.Task('c_bc_t51', length=1, delay_cost=1)
	S += c_bc_t51 >= 67
	c_bc_t51 += MAS[2]

	c_paa_t31 = S.Task('c_paa_t31', length=1, delay_cost=1)
	S += c_paa_t31 >= 67
	c_paa_t31 += MAS[0]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 67
	c_paa_t4_t3_mem0 += MAS_MEM[1]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 67
	c_paa_t4_t3_mem1 += MAS_MEM[0]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 67
	c_pbc_t0_t3_mem0 += MAIN_MEM_r

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 67
	c_pbc_t0_t3_mem1 += MAIN_MEM_r

	c_ac_s00 = S.Task('c_ac_s00', length=1, delay_cost=1)
	S += c_ac_s00 >= 68
	c_ac_s00 += MAS[2]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 68
	c_ac_t51_mem0 += MAS_MEM[0]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 68
	c_ac_t51_mem1 += MAS_MEM[1]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	S += c_bc01_mem0 >= 68
	c_bc01_mem0 += MAS_MEM[0]

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	S += c_bc01_mem1 >= 68
	c_bc01_mem1 += MAS_MEM[3]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 68
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 68
	c_bc_t41_mem1 += MAS_MEM[1]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=1, delay_cost=1)
	S += c_paa_t4_t3 >= 68
	c_paa_t4_t3 += MAS[1]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=1, delay_cost=1)
	S += c_pbc_t0_t3 >= 68
	c_pbc_t0_t3 += MAS[0]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 68
	c_pbc_t30_mem0 += MAIN_MEM_r

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 68
	c_pbc_t30_mem1 += MAIN_MEM_r

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	S += c_ac11_mem0 >= 69
	c_ac11_mem0 += MAS_MEM[2]

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	S += c_ac11_mem1 >= 69
	c_ac11_mem1 += MAS_MEM[3]

	c_ac_t51 = S.Task('c_ac_t51', length=1, delay_cost=1)
	S += c_ac_t51 >= 69
	c_ac_t51 += MAS[3]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	S += c_bc00_mem0 >= 69
	c_bc00_mem0 += MAS_MEM[0]

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	S += c_bc00_mem1 >= 69
	c_bc00_mem1 += MAS_MEM[3]

	c_bc01 = S.Task('c_bc01', length=1, delay_cost=1)
	S += c_bc01 >= 69
	c_bc01 += MAS[2]

	c_bc_t41 = S.Task('c_bc_t41', length=1, delay_cost=1)
	S += c_bc_t41 >= 69
	c_bc_t41 += MAS[1]

	c_pbc_t30 = S.Task('c_pbc_t30', length=1, delay_cost=1)
	S += c_pbc_t30 >= 69
	c_pbc_t30 += MAS[0]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 69
	c_pbc_t31_mem0 += MAIN_MEM_r

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 69
	c_pbc_t31_mem1 += MAIN_MEM_r

	c_ac11 = S.Task('c_ac11', length=1, delay_cost=1)
	S += c_ac11 >= 70
	c_ac11 += MAS[1]

	c_bc00 = S.Task('c_bc00', length=1, delay_cost=1)
	S += c_bc00 >= 70
	c_bc00 += MAS[3]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	S += c_pa10_mem0 >= 70
	c_pa10_mem0 += MAS_MEM[1]

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	S += c_pa10_mem1 >= 70
	c_pa10_mem1 += MAS_MEM[3]

	c_pbc_t31 = S.Task('c_pbc_t31', length=1, delay_cost=1)
	S += c_pbc_t31 >= 70
	c_pbc_t31 += MAS[0]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 70
	c_pbc_t4_t3_mem0 += MAS_MEM[0]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 70
	c_pbc_t4_t3_mem1 += MAS_MEM[0]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 70
	c_pcb_t0_t3_mem0 += MAIN_MEM_r

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 70
	c_pcb_t0_t3_mem1 += MAIN_MEM_r

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	S += c_ac01_mem0 >= 71
	c_ac01_mem0 += MAS_MEM[0]

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	S += c_ac01_mem1 >= 71
	c_ac01_mem1 += MAS_MEM[1]

	c_pa10 = S.Task('c_pa10', length=1, delay_cost=1)
	S += c_pa10 >= 71
	c_pa10 += MAS[1]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 71
	c_pbc_t1_t3_mem0 += MAIN_MEM_r

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 71
	c_pbc_t1_t3_mem1 += MAIN_MEM_r

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=1, delay_cost=1)
	S += c_pbc_t4_t3 >= 71
	c_pbc_t4_t3 += MAS[0]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	S += c_pc10_mem0 >= 71
	c_pc10_mem0 += MAS_MEM[1]

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	S += c_pc10_mem1 >= 71
	c_pc10_mem1 += MAS_MEM[0]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=1, delay_cost=1)
	S += c_pcb_t0_t3 >= 71
	c_pcb_t0_t3 += MAS[3]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 72
	c_aa_t00_mem0 += MAIN_MEM_r

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 72
	c_aa_t00_mem1 += MAS_MEM[1]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	S += c_ac00_mem0 >= 72
	c_ac00_mem0 += MAS_MEM[0]

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	S += c_ac00_mem1 >= 72
	c_ac00_mem1 += MAS_MEM[2]

	c_ac01 = S.Task('c_ac01', length=1, delay_cost=1)
	S += c_ac01 >= 72
	c_ac01 += MAS[0]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 72
	c_bb_t00_mem0 += MAIN_MEM_r

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 72
	c_bb_t00_mem1 += MAS_MEM[2]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=1, delay_cost=1)
	S += c_pbc_t1_t3 >= 72
	c_pbc_t1_t3 += MAS[1]

	c_pc10 = S.Task('c_pc10', length=1, delay_cost=1)
	S += c_pc10 >= 72
	c_pc10 += MAS[2]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	S += c_pc11_mem0 >= 72
	c_pc11_mem0 += MAS_MEM[0]

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	S += c_pc11_mem1 >= 72
	c_pc11_mem1 += MAS_MEM[1]

	c_aa_t00 = S.Task('c_aa_t00', length=1, delay_cost=1)
	S += c_aa_t00 >= 73
	c_aa_t00 += MAS[2]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 73
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 73
	c_aa_t2_t0_mem0 += MAS_MEM[2]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 73
	c_aa_t2_t0_mem1 += MAS_MEM[1]

	c_ac00 = S.Task('c_ac00', length=1, delay_cost=1)
	S += c_ac00 >= 73
	c_ac00 += MAS[0]

	c_bb_t00 = S.Task('c_bb_t00', length=1, delay_cost=1)
	S += c_bb_t00 >= 73
	c_bb_t00 += MAS[3]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 73
	c_cc_t00_mem0 += MAIN_MEM_r

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 73
	c_cc_t00_mem1 += MAS_MEM[0]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 73
	c_cc_t01_mem0 += MAIN_MEM_r

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 73
	c_cc_t01_mem1 += MAS_MEM[3]

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	S += c_pa11_mem0 >= 73
	c_pa11_mem0 += MAS_MEM[0]

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	S += c_pa11_mem1 >= 73
	c_pa11_mem1 += MAS_MEM[2]

	c_pc11 = S.Task('c_pc11', length=1, delay_cost=1)
	S += c_pc11 >= 73
	c_pc11 += MAS[1]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 74
	c_aa_t01_mem0 += MAIN_MEM_r

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 74
	c_aa_t01_mem1 += MAS_MEM[0]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=5, delay_cost=1)
	S += c_aa_t2_t0 >= 74
	c_aa_t2_t0 += MM[0]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 74
	c_bb_t01_mem0 += MAIN_MEM_r

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 74
	c_bb_t01_mem1 += MAS_MEM[2]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 74
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 74
	c_bb_t2_t0_mem0 += MAS_MEM[3]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 74
	c_bb_t2_t0_mem1 += MAS_MEM[1]

	c_cc_t00 = S.Task('c_cc_t00', length=1, delay_cost=1)
	S += c_cc_t00 >= 74
	c_cc_t00 += MAS[0]

	c_cc_t01 = S.Task('c_cc_t01', length=1, delay_cost=1)
	S += c_cc_t01 >= 74
	c_cc_t01 += MAS[2]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 74
	c_cc_t2_t2_mem0 += MAS_MEM[0]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 74
	c_cc_t2_t2_mem1 += MAS_MEM[2]

	c_pa11 = S.Task('c_pa11', length=1, delay_cost=1)
	S += c_pa11 >= 74
	c_pa11 += MAS[3]

	c_aa_t01 = S.Task('c_aa_t01', length=1, delay_cost=1)
	S += c_aa_t01 >= 75
	c_aa_t01 += MAS[2]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 75
	c_aa_t2_t2_mem0 += MAS_MEM[2]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 75
	c_aa_t2_t2_mem1 += MAS_MEM[2]

	c_bb_t01 = S.Task('c_bb_t01', length=1, delay_cost=1)
	S += c_bb_t01 >= 75
	c_bb_t01 += MAS[1]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=5, delay_cost=1)
	S += c_bb_t2_t0 >= 75
	c_bb_t2_t0 += MM[0]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 75
	c_bb_t2_t2_mem0 += MAS_MEM[3]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 75
	c_bb_t2_t2_mem1 += MAS_MEM[1]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 75
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 75
	c_cc_t2_t0_mem0 += MAS_MEM[0]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 75
	c_cc_t2_t0_mem1 += MAS_MEM[0]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=1, delay_cost=1)
	S += c_cc_t2_t2 >= 75
	c_cc_t2_t2 += MAS[0]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=1, delay_cost=1)
	S += c_aa_t2_t2 >= 76
	c_aa_t2_t2 += MAS[0]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=1, delay_cost=1)
	S += c_bb_t2_t2 >= 76
	c_bb_t2_t2 += MAS[1]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=5, delay_cost=1)
	S += c_cc_t2_t0 >= 76
	c_cc_t2_t0 += MM[0]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 76
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 76
	c_cc_t2_t1_mem0 += MAS_MEM[2]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 76
	c_cc_t2_t1_mem1 += MAS_MEM[2]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 77
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 77
	c_aa_t2_t1_mem0 += MAS_MEM[2]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 77
	c_aa_t2_t1_mem1 += MAS_MEM[1]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=5, delay_cost=1)
	S += c_cc_t2_t1 >= 77
	c_cc_t2_t1 += MM[0]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=5, delay_cost=1)
	S += c_aa_t2_t1 >= 78
	c_aa_t2_t1 += MM[0]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 78
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 78
	c_bb_t2_t1_mem0 += MAS_MEM[1]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 78
	c_bb_t2_t1_mem1 += MAS_MEM[1]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=5, delay_cost=1)
	S += c_bb_t2_t1 >= 79
	c_bb_t2_t1 += MM[0]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 79
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 79
	c_cc_t2_t4_mem0 += MAS_MEM[0]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 79
	c_cc_t2_t4_mem1 += MAS_MEM[0]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 80
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 80
	c_aa_t2_t4_mem0 += MAS_MEM[0]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 80
	c_aa_t2_t4_mem1 += MAS_MEM[0]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=5, delay_cost=1)
	S += c_cc_t2_t4 >= 80
	c_cc_t2_t4 += MM[0]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=5, delay_cost=1)
	S += c_aa_t2_t4 >= 81
	c_aa_t2_t4 += MM[0]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 81
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 81
	c_bb_t2_t4_mem0 += MAS_MEM[1]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 81
	c_bb_t2_t4_mem1 += MAS_MEM[1]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 81
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 81
	c_cc_t2_t5_mem1 += MM_MEM[0]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 82
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 82
	c_aa_t2_t5_mem1 += MM_MEM[0]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=5, delay_cost=1)
	S += c_bb_t2_t4 >= 82
	c_bb_t2_t4 += MM[0]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=1, delay_cost=1)
	S += c_cc_t2_t5 >= 82
	c_cc_t2_t5 += MAS[0]

	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	S += c_pcb_t1_t0_in >= 82
	c_pcb_t1_t0_in += MM_in[0]

	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem0 >= 82
	c_pcb_t1_t0_mem0 += MAS_MEM[2]

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem1 >= 82
	c_pcb_t1_t0_mem1 += MAIN_MEM_r

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=1, delay_cost=1)
	S += c_aa_t2_t5 >= 83
	c_aa_t2_t5 += MAS[0]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 83
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 83
	c_bb_t20_mem1 += MM_MEM[0]

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=5, delay_cost=1)
	S += c_pcb_t1_t0 >= 83
	c_pcb_t1_t0 += MM[0]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	S += c_bb00_mem0 >= 84
	c_bb00_mem0 += MAS_MEM[0]

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	S += c_bb00_mem1 >= 84
	c_bb00_mem1 += MAS_MEM[1]

	c_bb_t20 = S.Task('c_bb_t20', length=1, delay_cost=1)
	S += c_bb_t20 >= 84
	c_bb_t20 += MAS[0]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 84
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 84
	c_bb_t2_t5_mem1 += MM_MEM[0]

	c_bb00 = S.Task('c_bb00', length=1, delay_cost=1)
	S += c_bb00 >= 85
	c_bb00 += MAS[0]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=1, delay_cost=1)
	S += c_bb_t2_t5 >= 85
	c_bb_t2_t5 += MAS[3]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 85
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 85
	c_cc_t20_mem1 += MM_MEM[0]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 86
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 86
	c_aa_t20_mem1 += MM_MEM[0]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	S += c_cc00_mem0 >= 86
	c_cc00_mem0 += MAS_MEM[2]

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	S += c_cc00_mem1 >= 86
	c_cc00_mem1 += MAS_MEM[3]

	c_cc_t20 = S.Task('c_cc_t20', length=1, delay_cost=1)
	S += c_cc_t20 >= 86
	c_cc_t20 += MAS[2]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	S += c_aa00_mem0 >= 87
	c_aa00_mem0 += MAS_MEM[0]

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	S += c_aa00_mem1 >= 87
	c_aa00_mem1 += MAS_MEM[3]

	c_aa_t20 = S.Task('c_aa_t20', length=1, delay_cost=1)
	S += c_aa_t20 >= 87
	c_aa_t20 += MAS[0]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t21_mem0 >= 87
	c_aa_t21_mem0 += MM_MEM[0]

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t21_mem1 >= 87
	c_aa_t21_mem1 += MAS_MEM[0]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	S += c_bb_t21_mem0 >= 87
	c_bb_t21_mem0 += MM_MEM[0]

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	S += c_bb_t21_mem1 >= 87
	c_bb_t21_mem1 += MAS_MEM[3]

	c_cc00 = S.Task('c_cc00', length=1, delay_cost=1)
	S += c_cc00 >= 87
	c_cc00 += MAS[1]

	c_aa00 = S.Task('c_aa00', length=1, delay_cost=1)
	S += c_aa00 >= 88
	c_aa00 += MAS[1]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	S += c_aa01_mem0 >= 88
	c_aa01_mem0 += MAS_MEM[0]

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	S += c_aa01_mem1 >= 88
	c_aa01_mem1 += MAS_MEM[3]

	c_aa_t21 = S.Task('c_aa_t21', length=1, delay_cost=1)
	S += c_aa_t21 >= 88
	c_aa_t21 += MAS[0]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	S += c_bb01_mem0 >= 88
	c_bb01_mem0 += MAS_MEM[2]

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	S += c_bb01_mem1 >= 88
	c_bb01_mem1 += MAS_MEM[1]

	c_bb_t21 = S.Task('c_bb_t21', length=1, delay_cost=1)
	S += c_bb_t21 >= 88
	c_bb_t21 += MAS[2]

	c_cc_t21_mem0 = S.Task('c_cc_t21_mem0', length=1, delay_cost=1)
	S += c_cc_t21_mem0 >= 88
	c_cc_t21_mem0 += MM_MEM[0]

	c_cc_t21_mem1 = S.Task('c_cc_t21_mem1', length=1, delay_cost=1)
	S += c_cc_t21_mem1 >= 88
	c_cc_t21_mem1 += MAS_MEM[0]

	c_aa01 = S.Task('c_aa01', length=1, delay_cost=1)
	S += c_aa01 >= 89
	c_aa01 += MAS[2]

	c_bb01 = S.Task('c_bb01', length=1, delay_cost=1)
	S += c_bb01 >= 89
	c_bb01 += MAS[1]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	S += c_cc01_mem0 >= 89
	c_cc01_mem0 += MAS_MEM[0]

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	S += c_cc01_mem1 >= 89
	c_cc01_mem1 += MAS_MEM[2]

	c_cc_t21 = S.Task('c_cc_t21', length=1, delay_cost=1)
	S += c_cc_t21 >= 89
	c_cc_t21 += MAS[0]

	c_cc01 = S.Task('c_cc01', length=1, delay_cost=1)
	S += c_cc01 >= 90
	c_cc01 += MAS[2]


	# new tasks
	c_bc11 = S.Task('c_bc11', length=1, delay_cost=1)
	c_bc11 += alt(MAS)

	S += c_bc11<71

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	c_bc11_mem0 += MAS_MEM[1]
	S += 69 < c_bc11_mem0
	S += c_bc11_mem0 <= c_bc11

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	c_bc11_mem1 += MAS_MEM[2]
	S += 67 < c_bc11_mem1
	S += c_bc11_mem1 <= c_bc11

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=1, delay_cost=1)
	c_bcxi_y1_0 += alt(MAS)

	S += c_bcxi_y1_0<1000

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	c_bcxi_y1_0_mem0 += MAS_MEM[2]
	S += 63 < c_bcxi_y1_0_mem0
	S += c_bcxi_y1_0_mem0 <= c_bcxi_y1_0

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	c_bcxi_y1_0_mem1 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_0_mem1*MAS_MEM[0]
	S += (c_bc11*MAS[1])-1 < c_bcxi_y1_0_mem1*MAS_MEM[1]
	S += (c_bc11*MAS[2])-1 < c_bcxi_y1_0_mem1*MAS_MEM[2]
	S += (c_bc11*MAS[3])-1 < c_bcxi_y1_0_mem1*MAS_MEM[3]
	S += c_bcxi_y1_0_mem1 <= c_bcxi_y1_0

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=1, delay_cost=1)
	c_bcxi_y1_1 += alt(MAS)

	S += c_bcxi_y1_1<1000

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	c_bcxi_y1_1_mem0 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_1_mem0*MAS_MEM[0]
	S += (c_bc11*MAS[1])-1 < c_bcxi_y1_1_mem0*MAS_MEM[1]
	S += (c_bc11*MAS[2])-1 < c_bcxi_y1_1_mem0*MAS_MEM[2]
	S += (c_bc11*MAS[3])-1 < c_bcxi_y1_1_mem0*MAS_MEM[3]
	S += c_bcxi_y1_1_mem0 <= c_bcxi_y1_1

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	c_bcxi_y1_1_mem1 += MAS_MEM[2]
	S += 63 < c_bcxi_y1_1_mem1
	S += c_bcxi_y1_1_mem1 <= c_bcxi_y1_1

	c_pa00 = S.Task('c_pa00', length=1, delay_cost=1)
	c_pa00 += alt(MAS)

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	c_pa00_mem0 += MAS_MEM[1]
	S += 88 < c_pa00_mem0
	S += c_pa00_mem0 <= c_pa00

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	c_pa00_mem1 += alt(MAS_MEM)
	S += (c_bcxi_y1_0*MAS[0])-1 < c_pa00_mem1*MAS_MEM[0]
	S += (c_bcxi_y1_0*MAS[1])-1 < c_pa00_mem1*MAS_MEM[1]
	S += (c_bcxi_y1_0*MAS[2])-1 < c_pa00_mem1*MAS_MEM[2]
	S += (c_bcxi_y1_0*MAS[3])-1 < c_pa00_mem1*MAS_MEM[3]
	S += c_pa00_mem1 <= c_pa00

	c_pa01 = S.Task('c_pa01', length=1, delay_cost=1)
	c_pa01 += alt(MAS)

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	c_pa01_mem0 += MAS_MEM[2]
	S += 89 < c_pa01_mem0
	S += c_pa01_mem0 <= c_pa01

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	c_pa01_mem1 += alt(MAS_MEM)
	S += (c_bcxi_y1_1*MAS[0])-1 < c_pa01_mem1*MAS_MEM[0]
	S += (c_bcxi_y1_1*MAS[1])-1 < c_pa01_mem1*MAS_MEM[1]
	S += (c_bcxi_y1_1*MAS[2])-1 < c_pa01_mem1*MAS_MEM[2]
	S += (c_bcxi_y1_1*MAS[3])-1 < c_pa01_mem1*MAS_MEM[3]
	S += c_pa01_mem1 <= c_pa01

	c_pb10 = S.Task('c_pb10', length=1, delay_cost=1)
	c_pb10 += alt(MAS)

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	c_pb10_mem0 += MAS_MEM[1]
	S += 87 < c_pb10_mem0
	S += c_pb10_mem0 <= c_pb10

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	c_pb10_mem1 += MAS_MEM[0]
	S += 59 < c_pb10_mem1
	S += c_pb10_mem1 <= c_pb10

	c_pb11 = S.Task('c_pb11', length=1, delay_cost=1)
	c_pb11 += alt(MAS)

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	c_pb11_mem0 += MAS_MEM[2]
	S += 90 < c_pb11_mem0
	S += c_pb11_mem0 <= c_pb11

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	c_pb11_mem1 += MAS_MEM[0]
	S += 60 < c_pb11_mem1
	S += c_pb11_mem1 <= c_pb11

	c_pc00 = S.Task('c_pc00', length=1, delay_cost=1)
	c_pc00 += alt(MAS)

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	c_pc00_mem0 += MAS_MEM[0]
	S += 85 < c_pc00_mem0
	S += c_pc00_mem0 <= c_pc00

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	c_pc00_mem1 += MAS_MEM[0]
	S += 73 < c_pc00_mem1
	S += c_pc00_mem1 <= c_pc00

	c_pc01 = S.Task('c_pc01', length=1, delay_cost=1)
	c_pc01 += alt(MAS)

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	c_pc01_mem0 += MAS_MEM[1]
	S += 89 < c_pc01_mem0
	S += c_pc01_mem0 <= c_pc01

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	c_pc01_mem1 += MAS_MEM[0]
	S += 72 < c_pc01_mem1
	S += c_pc01_mem1 <= c_pc01

	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	c_pbc_t0_t0_in += alt(MM_in)
	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=5, delay_cost=1)
	c_pbc_t0_t0 += alt(MM)
	S += c_pbc_t0_t0>=c_pbc_t0_t0_in

	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	c_pbc_t0_t0_mem0 += MAS_MEM[2]
	S += 53 < c_pbc_t0_t0_mem0
	S += c_pbc_t0_t0_mem0 <= c_pbc_t0_t0

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	c_pbc_t0_t0_mem1 += MAIN_MEM_r
	S += c_pbc_t0_t0_mem1 <= c_pbc_t0_t0

	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	c_pbc_t0_t1_in += alt(MM_in)
	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=5, delay_cost=1)
	c_pbc_t0_t1 += alt(MM)
	S += c_pbc_t0_t1>=c_pbc_t0_t1_in

	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	c_pbc_t0_t1_mem0 += MAS_MEM[3]
	S += 51 < c_pbc_t0_t1_mem0
	S += c_pbc_t0_t1_mem0 <= c_pbc_t0_t1

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	c_pbc_t0_t1_mem1 += MAIN_MEM_r
	S += c_pbc_t0_t1_mem1 <= c_pbc_t0_t1

	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=1, delay_cost=1)
	c_pbc_t0_t2 += alt(MAS)

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	c_pbc_t0_t2_mem0 += MAS_MEM[2]
	S += 53 < c_pbc_t0_t2_mem0
	S += c_pbc_t0_t2_mem0 <= c_pbc_t0_t2

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	c_pbc_t0_t2_mem1 += MAS_MEM[3]
	S += 51 < c_pbc_t0_t2_mem1
	S += c_pbc_t0_t2_mem1 <= c_pbc_t0_t2

	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	c_pcb_t1_t1_in += alt(MM_in)
	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=5, delay_cost=1)
	c_pcb_t1_t1 += alt(MM)
	S += c_pcb_t1_t1>=c_pcb_t1_t1_in

	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	c_pcb_t1_t1_mem0 += MAS_MEM[1]
	S += 73 < c_pcb_t1_t1_mem0
	S += c_pcb_t1_t1_mem0 <= c_pcb_t1_t1

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	c_pcb_t1_t1_mem1 += MAIN_MEM_r
	S += c_pcb_t1_t1_mem1 <= c_pcb_t1_t1

	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=1, delay_cost=1)
	c_pcb_t1_t2 += alt(MAS)

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	c_pcb_t1_t2_mem0 += MAS_MEM[2]
	S += 72 < c_pcb_t1_t2_mem0
	S += c_pcb_t1_t2_mem0 <= c_pcb_t1_t2

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	c_pcb_t1_t2_mem1 += MAS_MEM[1]
	S += 73 < c_pcb_t1_t2_mem1
	S += c_pcb_t1_t2_mem1 <= c_pcb_t1_t2

	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	c_paa_t1_t0_in += alt(MM_in)
	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=5, delay_cost=1)
	c_paa_t1_t0 += alt(MM)
	S += c_paa_t1_t0>=c_paa_t1_t0_in

	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	c_paa_t1_t0_mem0 += MAS_MEM[1]
	S += 71 < c_paa_t1_t0_mem0
	S += c_paa_t1_t0_mem0 <= c_paa_t1_t0

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	c_paa_t1_t0_mem1 += MAIN_MEM_r
	S += c_paa_t1_t0_mem1 <= c_paa_t1_t0

	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	c_paa_t1_t1_in += alt(MM_in)
	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=5, delay_cost=1)
	c_paa_t1_t1 += alt(MM)
	S += c_paa_t1_t1>=c_paa_t1_t1_in

	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	c_paa_t1_t1_mem0 += MAS_MEM[3]
	S += 74 < c_paa_t1_t1_mem0
	S += c_paa_t1_t1_mem0 <= c_paa_t1_t1

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	c_paa_t1_t1_mem1 += MAIN_MEM_r
	S += c_paa_t1_t1_mem1 <= c_paa_t1_t1

	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=1, delay_cost=1)
	c_paa_t1_t2 += alt(MAS)

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	c_paa_t1_t2_mem0 += MAS_MEM[1]
	S += 71 < c_paa_t1_t2_mem0
	S += c_paa_t1_t2_mem0 <= c_paa_t1_t2

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	c_paa_t1_t2_mem1 += MAS_MEM[3]
	S += 74 < c_paa_t1_t2_mem1
	S += c_paa_t1_t2_mem1 <= c_paa_t1_t2

	c0_t1_t2 = S.Task('c0_t1_t2', length=1, delay_cost=1)
	c0_t1_t2 += alt(MAS)

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	c0_t1_t2_mem0 += MAS_MEM[1]
	S += 71 < c0_t1_t2_mem0
	S += c0_t1_t2_mem0 <= c0_t1_t2

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	c0_t1_t2_mem1 += MAS_MEM[3]
	S += 74 < c0_t1_t2_mem1
	S += c0_t1_t2_mem1 <= c0_t1_t2

	c1_t0_t2 = S.Task('c1_t0_t2', length=1, delay_cost=1)
	c1_t0_t2 += alt(MAS)

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	c1_t0_t2_mem0 += MAS_MEM[2]
	S += 53 < c1_t0_t2_mem0
	S += c1_t0_t2_mem0 <= c1_t0_t2

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	c1_t0_t2_mem1 += MAS_MEM[3]
	S += 51 < c1_t0_t2_mem1
	S += c1_t0_t2_mem1 <= c1_t0_t2

	c2_t1_t2 = S.Task('c2_t1_t2', length=1, delay_cost=1)
	c2_t1_t2 += alt(MAS)

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	c2_t1_t2_mem0 += MAS_MEM[2]
	S += 72 < c2_t1_t2_mem0
	S += c2_t1_t2_mem0 <= c2_t1_t2

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	c2_t1_t2_mem1 += MAS_MEM[1]
	S += 73 < c2_t1_t2_mem1
	S += c2_t1_t2_mem1 <= c2_t1_t2

	c_pbc_t0_t4_in = S.Task('c_pbc_t0_t4_in', length=1, delay_cost=1)
	c_pbc_t0_t4_in += alt(MM_in)
	c_pbc_t0_t4 = S.Task('c_pbc_t0_t4', length=5, delay_cost=1)
	c_pbc_t0_t4 += alt(MM)
	S += c_pbc_t0_t4>=c_pbc_t0_t4_in

	c_pbc_t0_t4_mem0 = S.Task('c_pbc_t0_t4_mem0', length=1, delay_cost=1)
	c_pbc_t0_t4_mem0 += alt(MAS_MEM)
	S += (c_pbc_t0_t2*MAS[0])-1 < c_pbc_t0_t4_mem0*MAS_MEM[0]
	S += (c_pbc_t0_t2*MAS[1])-1 < c_pbc_t0_t4_mem0*MAS_MEM[1]
	S += (c_pbc_t0_t2*MAS[2])-1 < c_pbc_t0_t4_mem0*MAS_MEM[2]
	S += (c_pbc_t0_t2*MAS[3])-1 < c_pbc_t0_t4_mem0*MAS_MEM[3]
	S += c_pbc_t0_t4_mem0 <= c_pbc_t0_t4

	c_pbc_t0_t4_mem1 = S.Task('c_pbc_t0_t4_mem1', length=1, delay_cost=1)
	c_pbc_t0_t4_mem1 += MAS_MEM[0]
	S += 68 < c_pbc_t0_t4_mem1
	S += c_pbc_t0_t4_mem1 <= c_pbc_t0_t4

	c_pbc_t00 = S.Task('c_pbc_t00', length=1, delay_cost=1)
	c_pbc_t00 += alt(MAS)

	c_pbc_t00_mem0 = S.Task('c_pbc_t00_mem0', length=1, delay_cost=1)
	c_pbc_t00_mem0 += alt(MM_MEM)
	S += (c_pbc_t0_t0*MM[0])-1 < c_pbc_t00_mem0*MM_MEM[0]
	S += c_pbc_t00_mem0 <= c_pbc_t00

	c_pbc_t00_mem1 = S.Task('c_pbc_t00_mem1', length=1, delay_cost=1)
	c_pbc_t00_mem1 += alt(MM_MEM)
	S += (c_pbc_t0_t1*MM[0])-1 < c_pbc_t00_mem1*MM_MEM[0]
	S += c_pbc_t00_mem1 <= c_pbc_t00

	c_pbc_t0_t5 = S.Task('c_pbc_t0_t5', length=1, delay_cost=1)
	c_pbc_t0_t5 += alt(MAS)

	c_pbc_t0_t5_mem0 = S.Task('c_pbc_t0_t5_mem0', length=1, delay_cost=1)
	c_pbc_t0_t5_mem0 += alt(MM_MEM)
	S += (c_pbc_t0_t0*MM[0])-1 < c_pbc_t0_t5_mem0*MM_MEM[0]
	S += c_pbc_t0_t5_mem0 <= c_pbc_t0_t5

	c_pbc_t0_t5_mem1 = S.Task('c_pbc_t0_t5_mem1', length=1, delay_cost=1)
	c_pbc_t0_t5_mem1 += alt(MM_MEM)
	S += (c_pbc_t0_t1*MM[0])-1 < c_pbc_t0_t5_mem1*MM_MEM[0]
	S += c_pbc_t0_t5_mem1 <= c_pbc_t0_t5

	c_pbc_t1_t0_in = S.Task('c_pbc_t1_t0_in', length=1, delay_cost=1)
	c_pbc_t1_t0_in += alt(MM_in)
	c_pbc_t1_t0 = S.Task('c_pbc_t1_t0', length=5, delay_cost=1)
	c_pbc_t1_t0 += alt(MM)
	S += c_pbc_t1_t0>=c_pbc_t1_t0_in

	c_pbc_t1_t0_mem0 = S.Task('c_pbc_t1_t0_mem0', length=1, delay_cost=1)
	c_pbc_t1_t0_mem0 += alt(MAS_MEM)
	S += (c_pb10*MAS[0])-1 < c_pbc_t1_t0_mem0*MAS_MEM[0]
	S += (c_pb10*MAS[1])-1 < c_pbc_t1_t0_mem0*MAS_MEM[1]
	S += (c_pb10*MAS[2])-1 < c_pbc_t1_t0_mem0*MAS_MEM[2]
	S += (c_pb10*MAS[3])-1 < c_pbc_t1_t0_mem0*MAS_MEM[3]
	S += c_pbc_t1_t0_mem0 <= c_pbc_t1_t0

	c_pbc_t1_t0_mem1 = S.Task('c_pbc_t1_t0_mem1', length=1, delay_cost=1)
	c_pbc_t1_t0_mem1 += MAIN_MEM_r
	S += c_pbc_t1_t0_mem1 <= c_pbc_t1_t0

	c_pbc_t1_t1_in = S.Task('c_pbc_t1_t1_in', length=1, delay_cost=1)
	c_pbc_t1_t1_in += alt(MM_in)
	c_pbc_t1_t1 = S.Task('c_pbc_t1_t1', length=5, delay_cost=1)
	c_pbc_t1_t1 += alt(MM)
	S += c_pbc_t1_t1>=c_pbc_t1_t1_in

	c_pbc_t1_t1_mem0 = S.Task('c_pbc_t1_t1_mem0', length=1, delay_cost=1)
	c_pbc_t1_t1_mem0 += alt(MAS_MEM)
	S += (c_pb11*MAS[0])-1 < c_pbc_t1_t1_mem0*MAS_MEM[0]
	S += (c_pb11*MAS[1])-1 < c_pbc_t1_t1_mem0*MAS_MEM[1]
	S += (c_pb11*MAS[2])-1 < c_pbc_t1_t1_mem0*MAS_MEM[2]
	S += (c_pb11*MAS[3])-1 < c_pbc_t1_t1_mem0*MAS_MEM[3]
	S += c_pbc_t1_t1_mem0 <= c_pbc_t1_t1

	c_pbc_t1_t1_mem1 = S.Task('c_pbc_t1_t1_mem1', length=1, delay_cost=1)
	c_pbc_t1_t1_mem1 += MAIN_MEM_r
	S += c_pbc_t1_t1_mem1 <= c_pbc_t1_t1

	c_pbc_t1_t2 = S.Task('c_pbc_t1_t2', length=1, delay_cost=1)
	c_pbc_t1_t2 += alt(MAS)

	c_pbc_t1_t2_mem0 = S.Task('c_pbc_t1_t2_mem0', length=1, delay_cost=1)
	c_pbc_t1_t2_mem0 += alt(MAS_MEM)
	S += (c_pb10*MAS[0])-1 < c_pbc_t1_t2_mem0*MAS_MEM[0]
	S += (c_pb10*MAS[1])-1 < c_pbc_t1_t2_mem0*MAS_MEM[1]
	S += (c_pb10*MAS[2])-1 < c_pbc_t1_t2_mem0*MAS_MEM[2]
	S += (c_pb10*MAS[3])-1 < c_pbc_t1_t2_mem0*MAS_MEM[3]
	S += c_pbc_t1_t2_mem0 <= c_pbc_t1_t2

	c_pbc_t1_t2_mem1 = S.Task('c_pbc_t1_t2_mem1', length=1, delay_cost=1)
	c_pbc_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pb11*MAS[0])-1 < c_pbc_t1_t2_mem1*MAS_MEM[0]
	S += (c_pb11*MAS[1])-1 < c_pbc_t1_t2_mem1*MAS_MEM[1]
	S += (c_pb11*MAS[2])-1 < c_pbc_t1_t2_mem1*MAS_MEM[2]
	S += (c_pb11*MAS[3])-1 < c_pbc_t1_t2_mem1*MAS_MEM[3]
	S += c_pbc_t1_t2_mem1 <= c_pbc_t1_t2

	c_pbc_t20 = S.Task('c_pbc_t20', length=1, delay_cost=1)
	c_pbc_t20 += alt(MAS)

	c_pbc_t20_mem0 = S.Task('c_pbc_t20_mem0', length=1, delay_cost=1)
	c_pbc_t20_mem0 += MAS_MEM[2]
	S += 53 < c_pbc_t20_mem0
	S += c_pbc_t20_mem0 <= c_pbc_t20

	c_pbc_t20_mem1 = S.Task('c_pbc_t20_mem1', length=1, delay_cost=1)
	c_pbc_t20_mem1 += alt(MAS_MEM)
	S += (c_pb10*MAS[0])-1 < c_pbc_t20_mem1*MAS_MEM[0]
	S += (c_pb10*MAS[1])-1 < c_pbc_t20_mem1*MAS_MEM[1]
	S += (c_pb10*MAS[2])-1 < c_pbc_t20_mem1*MAS_MEM[2]
	S += (c_pb10*MAS[3])-1 < c_pbc_t20_mem1*MAS_MEM[3]
	S += c_pbc_t20_mem1 <= c_pbc_t20

	c_pbc_t21 = S.Task('c_pbc_t21', length=1, delay_cost=1)
	c_pbc_t21 += alt(MAS)

	c_pbc_t21_mem0 = S.Task('c_pbc_t21_mem0', length=1, delay_cost=1)
	c_pbc_t21_mem0 += MAS_MEM[3]
	S += 51 < c_pbc_t21_mem0
	S += c_pbc_t21_mem0 <= c_pbc_t21

	c_pbc_t21_mem1 = S.Task('c_pbc_t21_mem1', length=1, delay_cost=1)
	c_pbc_t21_mem1 += alt(MAS_MEM)
	S += (c_pb11*MAS[0])-1 < c_pbc_t21_mem1*MAS_MEM[0]
	S += (c_pb11*MAS[1])-1 < c_pbc_t21_mem1*MAS_MEM[1]
	S += (c_pb11*MAS[2])-1 < c_pbc_t21_mem1*MAS_MEM[2]
	S += (c_pb11*MAS[3])-1 < c_pbc_t21_mem1*MAS_MEM[3]
	S += c_pbc_t21_mem1 <= c_pbc_t21

	c_pcb_t0_t0_in = S.Task('c_pcb_t0_t0_in', length=1, delay_cost=1)
	c_pcb_t0_t0_in += alt(MM_in)
	c_pcb_t0_t0 = S.Task('c_pcb_t0_t0', length=5, delay_cost=1)
	c_pcb_t0_t0 += alt(MM)
	S += c_pcb_t0_t0>=c_pcb_t0_t0_in

	c_pcb_t0_t0_mem0 = S.Task('c_pcb_t0_t0_mem0', length=1, delay_cost=1)
	c_pcb_t0_t0_mem0 += alt(MAS_MEM)
	S += (c_pc00*MAS[0])-1 < c_pcb_t0_t0_mem0*MAS_MEM[0]
	S += (c_pc00*MAS[1])-1 < c_pcb_t0_t0_mem0*MAS_MEM[1]
	S += (c_pc00*MAS[2])-1 < c_pcb_t0_t0_mem0*MAS_MEM[2]
	S += (c_pc00*MAS[3])-1 < c_pcb_t0_t0_mem0*MAS_MEM[3]
	S += c_pcb_t0_t0_mem0 <= c_pcb_t0_t0

	c_pcb_t0_t0_mem1 = S.Task('c_pcb_t0_t0_mem1', length=1, delay_cost=1)
	c_pcb_t0_t0_mem1 += MAIN_MEM_r
	S += c_pcb_t0_t0_mem1 <= c_pcb_t0_t0

	c_pcb_t0_t1_in = S.Task('c_pcb_t0_t1_in', length=1, delay_cost=1)
	c_pcb_t0_t1_in += alt(MM_in)
	c_pcb_t0_t1 = S.Task('c_pcb_t0_t1', length=5, delay_cost=1)
	c_pcb_t0_t1 += alt(MM)
	S += c_pcb_t0_t1>=c_pcb_t0_t1_in

	c_pcb_t0_t1_mem0 = S.Task('c_pcb_t0_t1_mem0', length=1, delay_cost=1)
	c_pcb_t0_t1_mem0 += alt(MAS_MEM)
	S += (c_pc01*MAS[0])-1 < c_pcb_t0_t1_mem0*MAS_MEM[0]
	S += (c_pc01*MAS[1])-1 < c_pcb_t0_t1_mem0*MAS_MEM[1]
	S += (c_pc01*MAS[2])-1 < c_pcb_t0_t1_mem0*MAS_MEM[2]
	S += (c_pc01*MAS[3])-1 < c_pcb_t0_t1_mem0*MAS_MEM[3]
	S += c_pcb_t0_t1_mem0 <= c_pcb_t0_t1

	c_pcb_t0_t1_mem1 = S.Task('c_pcb_t0_t1_mem1', length=1, delay_cost=1)
	c_pcb_t0_t1_mem1 += MAIN_MEM_r
	S += c_pcb_t0_t1_mem1 <= c_pcb_t0_t1

	c_pcb_t0_t2 = S.Task('c_pcb_t0_t2', length=1, delay_cost=1)
	c_pcb_t0_t2 += alt(MAS)

	c_pcb_t0_t2_mem0 = S.Task('c_pcb_t0_t2_mem0', length=1, delay_cost=1)
	c_pcb_t0_t2_mem0 += alt(MAS_MEM)
	S += (c_pc00*MAS[0])-1 < c_pcb_t0_t2_mem0*MAS_MEM[0]
	S += (c_pc00*MAS[1])-1 < c_pcb_t0_t2_mem0*MAS_MEM[1]
	S += (c_pc00*MAS[2])-1 < c_pcb_t0_t2_mem0*MAS_MEM[2]
	S += (c_pc00*MAS[3])-1 < c_pcb_t0_t2_mem0*MAS_MEM[3]
	S += c_pcb_t0_t2_mem0 <= c_pcb_t0_t2

	c_pcb_t0_t2_mem1 = S.Task('c_pcb_t0_t2_mem1', length=1, delay_cost=1)
	c_pcb_t0_t2_mem1 += alt(MAS_MEM)
	S += (c_pc01*MAS[0])-1 < c_pcb_t0_t2_mem1*MAS_MEM[0]
	S += (c_pc01*MAS[1])-1 < c_pcb_t0_t2_mem1*MAS_MEM[1]
	S += (c_pc01*MAS[2])-1 < c_pcb_t0_t2_mem1*MAS_MEM[2]
	S += (c_pc01*MAS[3])-1 < c_pcb_t0_t2_mem1*MAS_MEM[3]
	S += c_pcb_t0_t2_mem1 <= c_pcb_t0_t2

	c_pcb_t1_t4_in = S.Task('c_pcb_t1_t4_in', length=1, delay_cost=1)
	c_pcb_t1_t4_in += alt(MM_in)
	c_pcb_t1_t4 = S.Task('c_pcb_t1_t4', length=5, delay_cost=1)
	c_pcb_t1_t4 += alt(MM)
	S += c_pcb_t1_t4>=c_pcb_t1_t4_in

	c_pcb_t1_t4_mem0 = S.Task('c_pcb_t1_t4_mem0', length=1, delay_cost=1)
	c_pcb_t1_t4_mem0 += alt(MAS_MEM)
	S += (c_pcb_t1_t2*MAS[0])-1 < c_pcb_t1_t4_mem0*MAS_MEM[0]
	S += (c_pcb_t1_t2*MAS[1])-1 < c_pcb_t1_t4_mem0*MAS_MEM[1]
	S += (c_pcb_t1_t2*MAS[2])-1 < c_pcb_t1_t4_mem0*MAS_MEM[2]
	S += (c_pcb_t1_t2*MAS[3])-1 < c_pcb_t1_t4_mem0*MAS_MEM[3]
	S += c_pcb_t1_t4_mem0 <= c_pcb_t1_t4

	c_pcb_t1_t4_mem1 = S.Task('c_pcb_t1_t4_mem1', length=1, delay_cost=1)
	c_pcb_t1_t4_mem1 += MAS_MEM[0]
	S += 61 < c_pcb_t1_t4_mem1
	S += c_pcb_t1_t4_mem1 <= c_pcb_t1_t4

	c_pcb_t10 = S.Task('c_pcb_t10', length=1, delay_cost=1)
	c_pcb_t10 += alt(MAS)

	c_pcb_t10_mem0 = S.Task('c_pcb_t10_mem0', length=1, delay_cost=1)
	c_pcb_t10_mem0 += MM_MEM[0]
	S += 87 < c_pcb_t10_mem0
	S += c_pcb_t10_mem0 <= c_pcb_t10

	c_pcb_t10_mem1 = S.Task('c_pcb_t10_mem1', length=1, delay_cost=1)
	c_pcb_t10_mem1 += alt(MM_MEM)
	S += (c_pcb_t1_t1*MM[0])-1 < c_pcb_t10_mem1*MM_MEM[0]
	S += c_pcb_t10_mem1 <= c_pcb_t10

	c_pcb_t1_t5 = S.Task('c_pcb_t1_t5', length=1, delay_cost=1)
	c_pcb_t1_t5 += alt(MAS)

	c_pcb_t1_t5_mem0 = S.Task('c_pcb_t1_t5_mem0', length=1, delay_cost=1)
	c_pcb_t1_t5_mem0 += MM_MEM[0]
	S += 87 < c_pcb_t1_t5_mem0
	S += c_pcb_t1_t5_mem0 <= c_pcb_t1_t5

	c_pcb_t1_t5_mem1 = S.Task('c_pcb_t1_t5_mem1', length=1, delay_cost=1)
	c_pcb_t1_t5_mem1 += alt(MM_MEM)
	S += (c_pcb_t1_t1*MM[0])-1 < c_pcb_t1_t5_mem1*MM_MEM[0]
	S += c_pcb_t1_t5_mem1 <= c_pcb_t1_t5

	c_pcb_t20 = S.Task('c_pcb_t20', length=1, delay_cost=1)
	c_pcb_t20 += alt(MAS)

	c_pcb_t20_mem0 = S.Task('c_pcb_t20_mem0', length=1, delay_cost=1)
	c_pcb_t20_mem0 += alt(MAS_MEM)
	S += (c_pc00*MAS[0])-1 < c_pcb_t20_mem0*MAS_MEM[0]
	S += (c_pc00*MAS[1])-1 < c_pcb_t20_mem0*MAS_MEM[1]
	S += (c_pc00*MAS[2])-1 < c_pcb_t20_mem0*MAS_MEM[2]
	S += (c_pc00*MAS[3])-1 < c_pcb_t20_mem0*MAS_MEM[3]
	S += c_pcb_t20_mem0 <= c_pcb_t20

	c_pcb_t20_mem1 = S.Task('c_pcb_t20_mem1', length=1, delay_cost=1)
	c_pcb_t20_mem1 += MAS_MEM[2]
	S += 72 < c_pcb_t20_mem1
	S += c_pcb_t20_mem1 <= c_pcb_t20

	c_pcb_t21 = S.Task('c_pcb_t21', length=1, delay_cost=1)
	c_pcb_t21 += alt(MAS)

	c_pcb_t21_mem0 = S.Task('c_pcb_t21_mem0', length=1, delay_cost=1)
	c_pcb_t21_mem0 += alt(MAS_MEM)
	S += (c_pc01*MAS[0])-1 < c_pcb_t21_mem0*MAS_MEM[0]
	S += (c_pc01*MAS[1])-1 < c_pcb_t21_mem0*MAS_MEM[1]
	S += (c_pc01*MAS[2])-1 < c_pcb_t21_mem0*MAS_MEM[2]
	S += (c_pc01*MAS[3])-1 < c_pcb_t21_mem0*MAS_MEM[3]
	S += c_pcb_t21_mem0 <= c_pcb_t21

	c_pcb_t21_mem1 = S.Task('c_pcb_t21_mem1', length=1, delay_cost=1)
	c_pcb_t21_mem1 += MAS_MEM[1]
	S += 73 < c_pcb_t21_mem1
	S += c_pcb_t21_mem1 <= c_pcb_t21

	c_paa_t0_t0_in = S.Task('c_paa_t0_t0_in', length=1, delay_cost=1)
	c_paa_t0_t0_in += alt(MM_in)
	c_paa_t0_t0 = S.Task('c_paa_t0_t0', length=5, delay_cost=1)
	c_paa_t0_t0 += alt(MM)
	S += c_paa_t0_t0>=c_paa_t0_t0_in

	c_paa_t0_t0_mem0 = S.Task('c_paa_t0_t0_mem0', length=1, delay_cost=1)
	c_paa_t0_t0_mem0 += alt(MAS_MEM)
	S += (c_pa00*MAS[0])-1 < c_paa_t0_t0_mem0*MAS_MEM[0]
	S += (c_pa00*MAS[1])-1 < c_paa_t0_t0_mem0*MAS_MEM[1]
	S += (c_pa00*MAS[2])-1 < c_paa_t0_t0_mem0*MAS_MEM[2]
	S += (c_pa00*MAS[3])-1 < c_paa_t0_t0_mem0*MAS_MEM[3]
	S += c_paa_t0_t0_mem0 <= c_paa_t0_t0

	c_paa_t0_t0_mem1 = S.Task('c_paa_t0_t0_mem1', length=1, delay_cost=1)
	c_paa_t0_t0_mem1 += MAIN_MEM_r
	S += c_paa_t0_t0_mem1 <= c_paa_t0_t0

	c_paa_t0_t1_in = S.Task('c_paa_t0_t1_in', length=1, delay_cost=1)
	c_paa_t0_t1_in += alt(MM_in)
	c_paa_t0_t1 = S.Task('c_paa_t0_t1', length=5, delay_cost=1)
	c_paa_t0_t1 += alt(MM)
	S += c_paa_t0_t1>=c_paa_t0_t1_in

	c_paa_t0_t1_mem0 = S.Task('c_paa_t0_t1_mem0', length=1, delay_cost=1)
	c_paa_t0_t1_mem0 += alt(MAS_MEM)
	S += (c_pa01*MAS[0])-1 < c_paa_t0_t1_mem0*MAS_MEM[0]
	S += (c_pa01*MAS[1])-1 < c_paa_t0_t1_mem0*MAS_MEM[1]
	S += (c_pa01*MAS[2])-1 < c_paa_t0_t1_mem0*MAS_MEM[2]
	S += (c_pa01*MAS[3])-1 < c_paa_t0_t1_mem0*MAS_MEM[3]
	S += c_paa_t0_t1_mem0 <= c_paa_t0_t1

	c_paa_t0_t1_mem1 = S.Task('c_paa_t0_t1_mem1', length=1, delay_cost=1)
	c_paa_t0_t1_mem1 += MAIN_MEM_r
	S += c_paa_t0_t1_mem1 <= c_paa_t0_t1

	c_paa_t0_t2 = S.Task('c_paa_t0_t2', length=1, delay_cost=1)
	c_paa_t0_t2 += alt(MAS)

	c_paa_t0_t2_mem0 = S.Task('c_paa_t0_t2_mem0', length=1, delay_cost=1)
	c_paa_t0_t2_mem0 += alt(MAS_MEM)
	S += (c_pa00*MAS[0])-1 < c_paa_t0_t2_mem0*MAS_MEM[0]
	S += (c_pa00*MAS[1])-1 < c_paa_t0_t2_mem0*MAS_MEM[1]
	S += (c_pa00*MAS[2])-1 < c_paa_t0_t2_mem0*MAS_MEM[2]
	S += (c_pa00*MAS[3])-1 < c_paa_t0_t2_mem0*MAS_MEM[3]
	S += c_paa_t0_t2_mem0 <= c_paa_t0_t2

	c_paa_t0_t2_mem1 = S.Task('c_paa_t0_t2_mem1', length=1, delay_cost=1)
	c_paa_t0_t2_mem1 += alt(MAS_MEM)
	S += (c_pa01*MAS[0])-1 < c_paa_t0_t2_mem1*MAS_MEM[0]
	S += (c_pa01*MAS[1])-1 < c_paa_t0_t2_mem1*MAS_MEM[1]
	S += (c_pa01*MAS[2])-1 < c_paa_t0_t2_mem1*MAS_MEM[2]
	S += (c_pa01*MAS[3])-1 < c_paa_t0_t2_mem1*MAS_MEM[3]
	S += c_paa_t0_t2_mem1 <= c_paa_t0_t2

	c_paa_t1_t4_in = S.Task('c_paa_t1_t4_in', length=1, delay_cost=1)
	c_paa_t1_t4_in += alt(MM_in)
	c_paa_t1_t4 = S.Task('c_paa_t1_t4', length=5, delay_cost=1)
	c_paa_t1_t4 += alt(MM)
	S += c_paa_t1_t4>=c_paa_t1_t4_in

	c_paa_t1_t4_mem0 = S.Task('c_paa_t1_t4_mem0', length=1, delay_cost=1)
	c_paa_t1_t4_mem0 += alt(MAS_MEM)
	S += (c_paa_t1_t2*MAS[0])-1 < c_paa_t1_t4_mem0*MAS_MEM[0]
	S += (c_paa_t1_t2*MAS[1])-1 < c_paa_t1_t4_mem0*MAS_MEM[1]
	S += (c_paa_t1_t2*MAS[2])-1 < c_paa_t1_t4_mem0*MAS_MEM[2]
	S += (c_paa_t1_t2*MAS[3])-1 < c_paa_t1_t4_mem0*MAS_MEM[3]
	S += c_paa_t1_t4_mem0 <= c_paa_t1_t4

	c_paa_t1_t4_mem1 = S.Task('c_paa_t1_t4_mem1', length=1, delay_cost=1)
	c_paa_t1_t4_mem1 += MAS_MEM[3]
	S += 65 < c_paa_t1_t4_mem1
	S += c_paa_t1_t4_mem1 <= c_paa_t1_t4

	c_paa_t10 = S.Task('c_paa_t10', length=1, delay_cost=1)
	c_paa_t10 += alt(MAS)

	c_paa_t10_mem0 = S.Task('c_paa_t10_mem0', length=1, delay_cost=1)
	c_paa_t10_mem0 += alt(MM_MEM)
	S += (c_paa_t1_t0*MM[0])-1 < c_paa_t10_mem0*MM_MEM[0]
	S += c_paa_t10_mem0 <= c_paa_t10

	c_paa_t10_mem1 = S.Task('c_paa_t10_mem1', length=1, delay_cost=1)
	c_paa_t10_mem1 += alt(MM_MEM)
	S += (c_paa_t1_t1*MM[0])-1 < c_paa_t10_mem1*MM_MEM[0]
	S += c_paa_t10_mem1 <= c_paa_t10

	c_paa_t1_t5 = S.Task('c_paa_t1_t5', length=1, delay_cost=1)
	c_paa_t1_t5 += alt(MAS)

	c_paa_t1_t5_mem0 = S.Task('c_paa_t1_t5_mem0', length=1, delay_cost=1)
	c_paa_t1_t5_mem0 += alt(MM_MEM)
	S += (c_paa_t1_t0*MM[0])-1 < c_paa_t1_t5_mem0*MM_MEM[0]
	S += c_paa_t1_t5_mem0 <= c_paa_t1_t5

	c_paa_t1_t5_mem1 = S.Task('c_paa_t1_t5_mem1', length=1, delay_cost=1)
	c_paa_t1_t5_mem1 += alt(MM_MEM)
	S += (c_paa_t1_t1*MM[0])-1 < c_paa_t1_t5_mem1*MM_MEM[0]
	S += c_paa_t1_t5_mem1 <= c_paa_t1_t5

	c_paa_t20 = S.Task('c_paa_t20', length=1, delay_cost=1)
	c_paa_t20 += alt(MAS)

	c_paa_t20_mem0 = S.Task('c_paa_t20_mem0', length=1, delay_cost=1)
	c_paa_t20_mem0 += alt(MAS_MEM)
	S += (c_pa00*MAS[0])-1 < c_paa_t20_mem0*MAS_MEM[0]
	S += (c_pa00*MAS[1])-1 < c_paa_t20_mem0*MAS_MEM[1]
	S += (c_pa00*MAS[2])-1 < c_paa_t20_mem0*MAS_MEM[2]
	S += (c_pa00*MAS[3])-1 < c_paa_t20_mem0*MAS_MEM[3]
	S += c_paa_t20_mem0 <= c_paa_t20

	c_paa_t20_mem1 = S.Task('c_paa_t20_mem1', length=1, delay_cost=1)
	c_paa_t20_mem1 += MAS_MEM[1]
	S += 71 < c_paa_t20_mem1
	S += c_paa_t20_mem1 <= c_paa_t20

	c_paa_t21 = S.Task('c_paa_t21', length=1, delay_cost=1)
	c_paa_t21 += alt(MAS)

	c_paa_t21_mem0 = S.Task('c_paa_t21_mem0', length=1, delay_cost=1)
	c_paa_t21_mem0 += alt(MAS_MEM)
	S += (c_pa01*MAS[0])-1 < c_paa_t21_mem0*MAS_MEM[0]
	S += (c_pa01*MAS[1])-1 < c_paa_t21_mem0*MAS_MEM[1]
	S += (c_pa01*MAS[2])-1 < c_paa_t21_mem0*MAS_MEM[2]
	S += (c_pa01*MAS[3])-1 < c_paa_t21_mem0*MAS_MEM[3]
	S += c_paa_t21_mem0 <= c_paa_t21

	c_paa_t21_mem1 = S.Task('c_paa_t21_mem1', length=1, delay_cost=1)
	c_paa_t21_mem1 += MAS_MEM[3]
	S += 74 < c_paa_t21_mem1
	S += c_paa_t21_mem1 <= c_paa_t21

	c0_t0_t2 = S.Task('c0_t0_t2', length=1, delay_cost=1)
	c0_t0_t2 += alt(MAS)

	c0_t0_t2_mem0 = S.Task('c0_t0_t2_mem0', length=1, delay_cost=1)
	c0_t0_t2_mem0 += alt(MAS_MEM)
	S += (c_pa00*MAS[0])-1 < c0_t0_t2_mem0*MAS_MEM[0]
	S += (c_pa00*MAS[1])-1 < c0_t0_t2_mem0*MAS_MEM[1]
	S += (c_pa00*MAS[2])-1 < c0_t0_t2_mem0*MAS_MEM[2]
	S += (c_pa00*MAS[3])-1 < c0_t0_t2_mem0*MAS_MEM[3]
	S += c0_t0_t2_mem0 <= c0_t0_t2

	c0_t0_t2_mem1 = S.Task('c0_t0_t2_mem1', length=1, delay_cost=1)
	c0_t0_t2_mem1 += alt(MAS_MEM)
	S += (c_pa01*MAS[0])-1 < c0_t0_t2_mem1*MAS_MEM[0]
	S += (c_pa01*MAS[1])-1 < c0_t0_t2_mem1*MAS_MEM[1]
	S += (c_pa01*MAS[2])-1 < c0_t0_t2_mem1*MAS_MEM[2]
	S += (c_pa01*MAS[3])-1 < c0_t0_t2_mem1*MAS_MEM[3]
	S += c0_t0_t2_mem1 <= c0_t0_t2

	c0_t20 = S.Task('c0_t20', length=1, delay_cost=1)
	c0_t20 += alt(MAS)

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	c0_t20_mem0 += alt(MAS_MEM)
	S += (c_pa00*MAS[0])-1 < c0_t20_mem0*MAS_MEM[0]
	S += (c_pa00*MAS[1])-1 < c0_t20_mem0*MAS_MEM[1]
	S += (c_pa00*MAS[2])-1 < c0_t20_mem0*MAS_MEM[2]
	S += (c_pa00*MAS[3])-1 < c0_t20_mem0*MAS_MEM[3]
	S += c0_t20_mem0 <= c0_t20

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	c0_t20_mem1 += MAS_MEM[1]
	S += 71 < c0_t20_mem1
	S += c0_t20_mem1 <= c0_t20

	c0_t21 = S.Task('c0_t21', length=1, delay_cost=1)
	c0_t21 += alt(MAS)

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	c0_t21_mem0 += alt(MAS_MEM)
	S += (c_pa01*MAS[0])-1 < c0_t21_mem0*MAS_MEM[0]
	S += (c_pa01*MAS[1])-1 < c0_t21_mem0*MAS_MEM[1]
	S += (c_pa01*MAS[2])-1 < c0_t21_mem0*MAS_MEM[2]
	S += (c_pa01*MAS[3])-1 < c0_t21_mem0*MAS_MEM[3]
	S += c0_t21_mem0 <= c0_t21

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	c0_t21_mem1 += MAS_MEM[3]
	S += 74 < c0_t21_mem1
	S += c0_t21_mem1 <= c0_t21

	c1_t1_t2 = S.Task('c1_t1_t2', length=1, delay_cost=1)
	c1_t1_t2 += alt(MAS)

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	c1_t1_t2_mem0 += alt(MAS_MEM)
	S += (c_pb10*MAS[0])-1 < c1_t1_t2_mem0*MAS_MEM[0]
	S += (c_pb10*MAS[1])-1 < c1_t1_t2_mem0*MAS_MEM[1]
	S += (c_pb10*MAS[2])-1 < c1_t1_t2_mem0*MAS_MEM[2]
	S += (c_pb10*MAS[3])-1 < c1_t1_t2_mem0*MAS_MEM[3]
	S += c1_t1_t2_mem0 <= c1_t1_t2

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	c1_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pb11*MAS[0])-1 < c1_t1_t2_mem1*MAS_MEM[0]
	S += (c_pb11*MAS[1])-1 < c1_t1_t2_mem1*MAS_MEM[1]
	S += (c_pb11*MAS[2])-1 < c1_t1_t2_mem1*MAS_MEM[2]
	S += (c_pb11*MAS[3])-1 < c1_t1_t2_mem1*MAS_MEM[3]
	S += c1_t1_t2_mem1 <= c1_t1_t2

	c1_t20 = S.Task('c1_t20', length=1, delay_cost=1)
	c1_t20 += alt(MAS)

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	c1_t20_mem0 += MAS_MEM[2]
	S += 53 < c1_t20_mem0
	S += c1_t20_mem0 <= c1_t20

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	c1_t20_mem1 += alt(MAS_MEM)
	S += (c_pb10*MAS[0])-1 < c1_t20_mem1*MAS_MEM[0]
	S += (c_pb10*MAS[1])-1 < c1_t20_mem1*MAS_MEM[1]
	S += (c_pb10*MAS[2])-1 < c1_t20_mem1*MAS_MEM[2]
	S += (c_pb10*MAS[3])-1 < c1_t20_mem1*MAS_MEM[3]
	S += c1_t20_mem1 <= c1_t20

	c1_t21 = S.Task('c1_t21', length=1, delay_cost=1)
	c1_t21 += alt(MAS)

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	c1_t21_mem0 += MAS_MEM[3]
	S += 51 < c1_t21_mem0
	S += c1_t21_mem0 <= c1_t21

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	c1_t21_mem1 += alt(MAS_MEM)
	S += (c_pb11*MAS[0])-1 < c1_t21_mem1*MAS_MEM[0]
	S += (c_pb11*MAS[1])-1 < c1_t21_mem1*MAS_MEM[1]
	S += (c_pb11*MAS[2])-1 < c1_t21_mem1*MAS_MEM[2]
	S += (c_pb11*MAS[3])-1 < c1_t21_mem1*MAS_MEM[3]
	S += c1_t21_mem1 <= c1_t21

	c2_t0_t2 = S.Task('c2_t0_t2', length=1, delay_cost=1)
	c2_t0_t2 += alt(MAS)

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	c2_t0_t2_mem0 += alt(MAS_MEM)
	S += (c_pc00*MAS[0])-1 < c2_t0_t2_mem0*MAS_MEM[0]
	S += (c_pc00*MAS[1])-1 < c2_t0_t2_mem0*MAS_MEM[1]
	S += (c_pc00*MAS[2])-1 < c2_t0_t2_mem0*MAS_MEM[2]
	S += (c_pc00*MAS[3])-1 < c2_t0_t2_mem0*MAS_MEM[3]
	S += c2_t0_t2_mem0 <= c2_t0_t2

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	c2_t0_t2_mem1 += alt(MAS_MEM)
	S += (c_pc01*MAS[0])-1 < c2_t0_t2_mem1*MAS_MEM[0]
	S += (c_pc01*MAS[1])-1 < c2_t0_t2_mem1*MAS_MEM[1]
	S += (c_pc01*MAS[2])-1 < c2_t0_t2_mem1*MAS_MEM[2]
	S += (c_pc01*MAS[3])-1 < c2_t0_t2_mem1*MAS_MEM[3]
	S += c2_t0_t2_mem1 <= c2_t0_t2

	c2_t20 = S.Task('c2_t20', length=1, delay_cost=1)
	c2_t20 += alt(MAS)

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	c2_t20_mem0 += alt(MAS_MEM)
	S += (c_pc00*MAS[0])-1 < c2_t20_mem0*MAS_MEM[0]
	S += (c_pc00*MAS[1])-1 < c2_t20_mem0*MAS_MEM[1]
	S += (c_pc00*MAS[2])-1 < c2_t20_mem0*MAS_MEM[2]
	S += (c_pc00*MAS[3])-1 < c2_t20_mem0*MAS_MEM[3]
	S += c2_t20_mem0 <= c2_t20

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	c2_t20_mem1 += MAS_MEM[2]
	S += 72 < c2_t20_mem1
	S += c2_t20_mem1 <= c2_t20

	c2_t21 = S.Task('c2_t21', length=1, delay_cost=1)
	c2_t21 += alt(MAS)

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	c2_t21_mem0 += alt(MAS_MEM)
	S += (c_pc01*MAS[0])-1 < c2_t21_mem0*MAS_MEM[0]
	S += (c_pc01*MAS[1])-1 < c2_t21_mem0*MAS_MEM[1]
	S += (c_pc01*MAS[2])-1 < c2_t21_mem0*MAS_MEM[2]
	S += (c_pc01*MAS[3])-1 < c2_t21_mem0*MAS_MEM[3]
	S += c2_t21_mem0 <= c2_t21

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	c2_t21_mem1 += MAS_MEM[1]
	S += 73 < c2_t21_mem1
	S += c2_t21_mem1 <= c2_t21

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/INV/schedule8.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

