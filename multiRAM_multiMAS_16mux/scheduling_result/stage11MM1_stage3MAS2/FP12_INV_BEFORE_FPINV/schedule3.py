from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 195
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=11)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=2, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 0
	c_ab_t0_t2_in += MAS_in[1]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 0
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 0
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=3, delay_cost=1)
	S += c_ab_t0_t2 >= 1
	c_ab_t0_t2 += MAS[1]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 1
	c_bb_t3_t2_in += MAS_in[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 1
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 1
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=3, delay_cost=1)
	S += c_bb_t3_t2 >= 2
	c_bb_t3_t2 += MAS[0]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 2
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 2
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 2
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=11, delay_cost=1)
	S += c_cc_t3_t0 >= 3
	c_cc_t3_t0 += MM[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 3
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 3
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 3
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=11, delay_cost=1)
	S += c_cc_t3_t1 >= 4
	c_cc_t3_t1 += MM[0]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 4
	c_cc_t3_t2_in += MAS_in[0]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 4
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 4
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 5
	c_cc_a1_0_in += MAS_in[1]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 5
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 5
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=3, delay_cost=1)
	S += c_cc_t3_t2 >= 5
	c_cc_t3_t2 += MAS[0]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=3, delay_cost=1)
	S += c_cc_a1_0 >= 6
	c_cc_a1_0 += MAS[1]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 6
	c_cc_t3_t3_in += MAS_in[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 6
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 6
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 7
	c_ab_t0_t3_in += MAS_in[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 7
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 7
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=3, delay_cost=1)
	S += c_cc_t3_t3 >= 7
	c_cc_t3_t3 += MAS[0]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=3, delay_cost=1)
	S += c_ab_t0_t3 >= 8
	c_ab_t0_t3 += MAS[1]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 8
	c_bb_t11_in += MAS_in[0]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 8
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 8
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 9
	c_bb_a1_1_in += MAS_in[1]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 9
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 9
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_t11 = S.Task('c_bb_t11', length=3, delay_cost=1)
	S += c_bb_t11 >= 9
	c_bb_t11 += MAS[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 10
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 10
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 10
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=3, delay_cost=1)
	S += c_bb_a1_1 >= 10
	c_bb_a1_1 += MAS[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=11, delay_cost=1)
	S += c_ab_t1_t1 >= 11
	c_ab_t1_t1 += MM[0]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 11
	c_bb_t10_in += MAS_in[1]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 11
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 11
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t10 = S.Task('c_bb_t10', length=3, delay_cost=1)
	S += c_bb_t10 >= 12
	c_bb_t10 += MAS[1]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 12
	c_cc_a1_1_in += MAS_in[0]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 12
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 12
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 13
	c_aa_t3_t3_in += MAS_in[0]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 13
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 13
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=3, delay_cost=1)
	S += c_cc_a1_1 >= 13
	c_cc_a1_1 += MAS[0]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 14
	c_aa_a1_1_in += MAS_in[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 14
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 14
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=3, delay_cost=1)
	S += c_aa_t3_t3 >= 14
	c_aa_t3_t3 += MAS[0]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=3, delay_cost=1)
	S += c_aa_a1_1 >= 15
	c_aa_a1_1 += MAS[0]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 15
	c_cc_t11_in += MAS_in[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 15
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 15
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 16
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 16
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 16
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=3, delay_cost=1)
	S += c_cc_t11 >= 16
	c_cc_t11 += MAS[0]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=11, delay_cost=1)
	S += c_ab_t1_t0 >= 17
	c_ab_t1_t0 += MM[0]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 17
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 17
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 17
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 18
	c_aa_t3_t2_in += MAS_in[0]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 18
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 18
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=11, delay_cost=1)
	S += c_bb_t3_t1 >= 18
	c_bb_t3_t1 += MM[0]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=3, delay_cost=1)
	S += c_aa_t3_t2 >= 19
	c_aa_t3_t2 += MAS[0]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 19
	c_cc_t10_in += MAS_in[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 19
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 19
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 20
	c_aa_t10_in += MAS_in[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 20
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 20
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=3, delay_cost=1)
	S += c_cc_t10 >= 20
	c_cc_t10 += MAS[0]

	c_aa_t10 = S.Task('c_aa_t10', length=3, delay_cost=1)
	S += c_aa_t10 >= 21
	c_aa_t10 += MAS[0]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 21
	c_aa_t11_in += MAS_in[1]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 21
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 21
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t11 = S.Task('c_aa_t11', length=3, delay_cost=1)
	S += c_aa_t11 >= 22
	c_aa_t11 += MAS[1]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 22
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 22
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 22
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 23
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 23
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 23
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=11, delay_cost=1)
	S += c_bb_t3_t0 >= 23
	c_bb_t3_t0 += MM[0]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=11, delay_cost=1)
	S += c_ab_t0_t1 >= 24
	c_ab_t0_t1 += MM[0]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 24
	c_bb_a1_0_in += MAS_in[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 24
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 24
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=3, delay_cost=1)
	S += c_bb_a1_0 >= 25
	c_bb_a1_0 += MAS[0]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 25
	c_bb_t3_t3_in += MAS_in[0]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 25
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 25
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 26
	c_aa_a1_0_in += MAS_in[1]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 26
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 26
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=3, delay_cost=1)
	S += c_bb_t3_t3 >= 26
	c_bb_t3_t3 += MAS[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=3, delay_cost=1)
	S += c_aa_a1_0 >= 27
	c_aa_a1_0 += MAS[1]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 27
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 27
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 27
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 28
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 28
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 28
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=11, delay_cost=1)
	S += c_ab_t0_t0 >= 28
	c_ab_t0_t0 += MM[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 29
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 29
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 29
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=11, delay_cost=1)
	S += c_aa_t3_t1 >= 29
	c_aa_t3_t1 += MM[0]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=11, delay_cost=1)
	S += c_aa_t3_t0 >= 30
	c_aa_t3_t0 += MM[0]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 30
	c_ac_t21_in += MAS_in[1]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 30
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 30
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 31
	c_ac_t1_t2_in += MAS_in[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 31
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 31
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t21 = S.Task('c_ac_t21', length=3, delay_cost=1)
	S += c_ac_t21 >= 31
	c_ac_t21 += MAS[1]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=3, delay_cost=1)
	S += c_ac_t1_t2 >= 32
	c_ac_t1_t2 += MAS[0]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 32
	c_ac_t20_in += MAS_in[0]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 32
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 32
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 33
	c_ab_t20_in += MAS_in[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 33
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 33
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t20 = S.Task('c_ac_t20', length=3, delay_cost=1)
	S += c_ac_t20 >= 33
	c_ac_t20 += MAS[0]

	c_ab_t20 = S.Task('c_ab_t20', length=3, delay_cost=1)
	S += c_ab_t20 >= 34
	c_ab_t20 += MAS[0]

	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	S += c_bc_t1_t2_in >= 34
	c_bc_t1_t2_in += MAS_in[0]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 34
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 34
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 35
	c_ab_t30_in += MAS_in[0]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 35
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 35
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=3, delay_cost=1)
	S += c_bc_t1_t2 >= 35
	c_bc_t1_t2 += MAS[0]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 36
	c_ab_t1_t2_in += MAS_in[1]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 36
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 36
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t30 = S.Task('c_ab_t30', length=3, delay_cost=1)
	S += c_ab_t30 >= 36
	c_ab_t30 += MAS[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=3, delay_cost=1)
	S += c_ab_t1_t2 >= 37
	c_ab_t1_t2 += MAS[1]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 37
	c_bc_t0_t2_in += MAS_in[0]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 37
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 37
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 38
	c_ac_t0_t3_in += MAS_in[0]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 38
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 38
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=3, delay_cost=1)
	S += c_bc_t0_t2 >= 38
	c_bc_t0_t2 += MAS[0]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=3, delay_cost=1)
	S += c_ac_t0_t3 >= 39
	c_ac_t0_t3 += MAS[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 39
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 39
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 39
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 40
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 40
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 40
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=11, delay_cost=1)
	S += c_bc_t1_t0 >= 40
	c_bc_t1_t0 += MM[0]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=11, delay_cost=1)
	S += c_bc_t0_t1 >= 41
	c_bc_t0_t1 += MM[0]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 41
	c_bc_t20_in += MAS_in[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 41
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 41
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_bc_t20 = S.Task('c_bc_t20', length=3, delay_cost=1)
	S += c_bc_t20 >= 42
	c_bc_t20 += MAS[1]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 42
	c_bc_t30_in += MAS_in[0]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 42
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 42
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 43
	c_ab_t1_t3_in += MAS_in[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 43
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 43
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t30 = S.Task('c_bc_t30', length=3, delay_cost=1)
	S += c_bc_t30 >= 43
	c_bc_t30 += MAS[0]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=3, delay_cost=1)
	S += c_ab_t1_t3 >= 44
	c_ab_t1_t3 += MAS[0]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 44
	c_ac_t31_in += MAS_in[0]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 44
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 44
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 45
	c_ac_t1_t3_in += MAS_in[1]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 45
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 45
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t31 = S.Task('c_ac_t31', length=3, delay_cost=1)
	S += c_ac_t31 >= 45
	c_ac_t31 += MAS[0]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=3, delay_cost=1)
	S += c_ac_t1_t3 >= 46
	c_ac_t1_t3 += MAS[1]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 46
	c_ac_t30_in += MAS_in[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 46
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 46
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t30 = S.Task('c_ac_t30', length=3, delay_cost=1)
	S += c_ac_t30 >= 47
	c_ac_t30 += MAS[0]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 47
	c_bc_t21_in += MAS_in[1]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 47
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 47
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t21 = S.Task('c_bc_t21', length=3, delay_cost=1)
	S += c_bc_t21 >= 48
	c_bc_t21 += MAS[1]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 48
	c_bc_t31_in += MAS_in[0]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 48
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 48
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 49
	c_bc_t0_t3_in += MAS_in[1]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 49
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 49
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t31 = S.Task('c_bc_t31', length=3, delay_cost=1)
	S += c_bc_t31 >= 49
	c_bc_t31 += MAS[0]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=3, delay_cost=1)
	S += c_bc_t0_t3 >= 50
	c_bc_t0_t3 += MAS[1]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 50
	c_bc_t1_t3_in += MAS_in[0]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 50
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 50
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 51
	c_ab_t21_in += MAS_in[1]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 51
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 51
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=3, delay_cost=1)
	S += c_bc_t1_t3 >= 51
	c_bc_t1_t3 += MAS[0]

	c_ab_t21 = S.Task('c_ab_t21', length=3, delay_cost=1)
	S += c_ab_t21 >= 52
	c_ab_t21 += MAS[1]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 52
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 52
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 52
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 53
	c_ac_t0_t2_in += MAS_in[0]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 53
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 53
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=11, delay_cost=1)
	S += c_bc_t0_t0 >= 53
	c_bc_t0_t0 += MM[0]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 54
	c_ab_t31_in += MAS_in[0]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 54
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 54
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=3, delay_cost=1)
	S += c_ac_t0_t2 >= 54
	c_ac_t0_t2 += MAS[0]

	c_ab_t31 = S.Task('c_ab_t31', length=3, delay_cost=1)
	S += c_ab_t31 >= 55
	c_ab_t31 += MAS[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 55
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 55
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 55
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 56
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 56
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 56
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=11, delay_cost=1)
	S += c_bc_t1_t1 >= 56
	c_bc_t1_t1 += MM[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 57
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 57
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 57
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=11, delay_cost=1)
	S += c_ac_t1_t1 >= 57
	c_ac_t1_t1 += MM[0]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 58
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 58
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 58
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=11, delay_cost=1)
	S += c_ac_t1_t0 >= 58
	c_ac_t1_t0 += MM[0]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 59
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 59
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 59
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=11, delay_cost=1)
	S += c_ac_t0_t1 >= 59
	c_ac_t0_t1 += MM[0]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=11, delay_cost=1)
	S += c_ac_t0_t0 >= 60
	c_ac_t0_t0 += MM[0]

	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	S += c_paa_t31_in >= 60
	c_paa_t31_in += MAS_in[0]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 60
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 60
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	S += c_paa_t0_t3_in >= 61
	c_paa_t0_t3_in += MAS_in[1]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 61
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 61
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t31 = S.Task('c_paa_t31', length=3, delay_cost=1)
	S += c_paa_t31 >= 61
	c_paa_t31 += MAS[0]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=3, delay_cost=1)
	S += c_paa_t0_t3 >= 62
	c_paa_t0_t3 += MAS[1]

	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	S += c_pcb_t1_t3_in >= 62
	c_pcb_t1_t3_in += MAS_in[1]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 62
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 62
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	S += c_paa_t1_t3_in >= 63
	c_paa_t1_t3_in += MAS_in[0]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 63
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 63
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=3, delay_cost=1)
	S += c_pcb_t1_t3 >= 63
	c_pcb_t1_t3 += MAS[1]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=3, delay_cost=1)
	S += c_paa_t1_t3 >= 64
	c_paa_t1_t3 += MAS[0]

	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	S += c_pbc_t31_in >= 64
	c_pbc_t31_in += MAS_in[0]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 64
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 64
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t31 = S.Task('c_pbc_t31', length=3, delay_cost=1)
	S += c_pbc_t31 >= 65
	c_pbc_t31 += MAS[0]

	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	S += c_pcb_t0_t3_in >= 65
	c_pcb_t0_t3_in += MAS_in[1]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 65
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 65
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	S += c_paa_t30_in >= 66
	c_paa_t30_in += MAS_in[1]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 66
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 66
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=3, delay_cost=1)
	S += c_pcb_t0_t3 >= 66
	c_pcb_t0_t3 += MAS[1]

	c_paa_t30 = S.Task('c_paa_t30', length=3, delay_cost=1)
	S += c_paa_t30 >= 67
	c_paa_t30 += MAS[1]

	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	S += c_pbc_t0_t3_in >= 67
	c_pbc_t0_t3_in += MAS_in[1]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 67
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 67
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=3, delay_cost=1)
	S += c_pbc_t0_t3 >= 68
	c_pbc_t0_t3 += MAS[1]

	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	S += c_pcb_t31_in >= 68
	c_pcb_t31_in += MAS_in[1]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 68
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 68
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	S += c_pbc_t1_t3_in >= 69
	c_pbc_t1_t3_in += MAS_in[0]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 69
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 69
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t31 = S.Task('c_pcb_t31', length=3, delay_cost=1)
	S += c_pcb_t31 >= 69
	c_pcb_t31 += MAS[1]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=3, delay_cost=1)
	S += c_pbc_t1_t3 >= 70
	c_pbc_t1_t3 += MAS[0]

	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	S += c_pbc_t30_in >= 70
	c_pbc_t30_in += MAS_in[0]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 70
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 70
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t30 = S.Task('c_pbc_t30', length=3, delay_cost=1)
	S += c_pbc_t30 >= 71
	c_pbc_t30 += MAS[0]

	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	S += c_pcb_t30_in >= 71
	c_pcb_t30_in += MAS_in[1]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 71
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 71
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_pcb_t30 = S.Task('c_pcb_t30', length=3, delay_cost=1)
	S += c_pcb_t30 >= 72
	c_pcb_t30 += MAS[1]


	# new tasks
	c_aa_t00 = S.Task('c_aa_t00', length=3, delay_cost=1)
	c_aa_t00 += alt(MAS)
	c_aa_t00_in = S.Task('c_aa_t00_in', length=1, delay_cost=1)
	c_aa_t00_in += alt(MAS_in)
	S += c_aa_t00_in*MAS_in[0]<=c_aa_t00*MAS[0]

	S += c_aa_t00_in*MAS_in[1]<=c_aa_t00*MAS[1]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	c_aa_t00_mem0 += MAIN_MEM_r[0]
	S += c_aa_t00_mem0 <= c_aa_t00

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	c_aa_t00_mem1 += MAS_MEM[3]
	S += 29 < c_aa_t00_mem1
	S += c_aa_t00_mem1 <= c_aa_t00

	c_aa_t01 = S.Task('c_aa_t01', length=3, delay_cost=1)
	c_aa_t01 += alt(MAS)
	c_aa_t01_in = S.Task('c_aa_t01_in', length=1, delay_cost=1)
	c_aa_t01_in += alt(MAS_in)
	S += c_aa_t01_in*MAS_in[0]<=c_aa_t01*MAS[0]

	S += c_aa_t01_in*MAS_in[1]<=c_aa_t01*MAS[1]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	c_aa_t01_mem0 += MAIN_MEM_r[0]
	S += c_aa_t01_mem0 <= c_aa_t01

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	c_aa_t01_mem1 += MAS_MEM[1]
	S += 17 < c_aa_t01_mem1
	S += c_aa_t01_mem1 <= c_aa_t01

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=3, delay_cost=1)
	c_aa_t2_t3 += alt(MAS)
	c_aa_t2_t3_in = S.Task('c_aa_t2_t3_in', length=1, delay_cost=1)
	c_aa_t2_t3_in += alt(MAS_in)
	S += c_aa_t2_t3_in*MAS_in[0]<=c_aa_t2_t3*MAS[0]

	S += c_aa_t2_t3_in*MAS_in[1]<=c_aa_t2_t3*MAS[1]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	c_aa_t2_t3_mem0 += MAS_MEM[0]
	S += 23 < c_aa_t2_t3_mem0
	S += c_aa_t2_t3_mem0 <= c_aa_t2_t3

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	c_aa_t2_t3_mem1 += MAS_MEM[3]
	S += 24 < c_aa_t2_t3_mem1
	S += c_aa_t2_t3_mem1 <= c_aa_t2_t3

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=11, delay_cost=1)
	c_aa_t3_t4 += alt(MM)
	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	c_aa_t3_t4_in += alt(MM_in)
	S += c_aa_t3_t4_in*MM_in[0]<=c_aa_t3_t4*MM[0]
	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	c_aa_t3_t4_mem0 += MAS_MEM[0]
	S += 21 < c_aa_t3_t4_mem0
	S += c_aa_t3_t4_mem0 <= c_aa_t3_t4

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	c_aa_t3_t4_mem1 += MAS_MEM[1]
	S += 16 < c_aa_t3_t4_mem1
	S += c_aa_t3_t4_mem1 <= c_aa_t3_t4

	c_aa_t30 = S.Task('c_aa_t30', length=3, delay_cost=1)
	c_aa_t30 += alt(MAS)
	c_aa_t30_in = S.Task('c_aa_t30_in', length=1, delay_cost=1)
	c_aa_t30_in += alt(MAS_in)
	S += c_aa_t30_in*MAS_in[0]<=c_aa_t30*MAS[0]

	S += c_aa_t30_in*MAS_in[1]<=c_aa_t30*MAS[1]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	c_aa_t30_mem0 += MM_MEM[0]
	S += 40 < c_aa_t30_mem0
	S += c_aa_t30_mem0 <= c_aa_t30

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	c_aa_t30_mem1 += MM_MEM[1]
	S += 39 < c_aa_t30_mem1
	S += c_aa_t30_mem1 <= c_aa_t30

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=3, delay_cost=1)
	c_aa_t3_t5 += alt(MAS)
	c_aa_t3_t5_in = S.Task('c_aa_t3_t5_in', length=1, delay_cost=1)
	c_aa_t3_t5_in += alt(MAS_in)
	S += c_aa_t3_t5_in*MAS_in[0]<=c_aa_t3_t5*MAS[0]

	S += c_aa_t3_t5_in*MAS_in[1]<=c_aa_t3_t5*MAS[1]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	c_aa_t3_t5_mem0 += MM_MEM[0]
	S += 40 < c_aa_t3_t5_mem0
	S += c_aa_t3_t5_mem0 <= c_aa_t3_t5

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	c_aa_t3_t5_mem1 += MM_MEM[1]
	S += 39 < c_aa_t3_t5_mem1
	S += c_aa_t3_t5_mem1 <= c_aa_t3_t5

	c_bb_t00 = S.Task('c_bb_t00', length=3, delay_cost=1)
	c_bb_t00 += alt(MAS)
	c_bb_t00_in = S.Task('c_bb_t00_in', length=1, delay_cost=1)
	c_bb_t00_in += alt(MAS_in)
	S += c_bb_t00_in*MAS_in[0]<=c_bb_t00*MAS[0]

	S += c_bb_t00_in*MAS_in[1]<=c_bb_t00*MAS[1]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	c_bb_t00_mem0 += MAIN_MEM_r[0]
	S += c_bb_t00_mem0 <= c_bb_t00

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	c_bb_t00_mem1 += MAS_MEM[1]
	S += 27 < c_bb_t00_mem1
	S += c_bb_t00_mem1 <= c_bb_t00

	c_bb_t01 = S.Task('c_bb_t01', length=3, delay_cost=1)
	c_bb_t01 += alt(MAS)
	c_bb_t01_in = S.Task('c_bb_t01_in', length=1, delay_cost=1)
	c_bb_t01_in += alt(MAS_in)
	S += c_bb_t01_in*MAS_in[0]<=c_bb_t01*MAS[0]

	S += c_bb_t01_in*MAS_in[1]<=c_bb_t01*MAS[1]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	c_bb_t01_mem0 += MAIN_MEM_r[0]
	S += c_bb_t01_mem0 <= c_bb_t01

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	c_bb_t01_mem1 += MAS_MEM[3]
	S += 12 < c_bb_t01_mem1
	S += c_bb_t01_mem1 <= c_bb_t01

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=3, delay_cost=1)
	c_bb_t2_t3 += alt(MAS)
	c_bb_t2_t3_in = S.Task('c_bb_t2_t3_in', length=1, delay_cost=1)
	c_bb_t2_t3_in += alt(MAS_in)
	S += c_bb_t2_t3_in*MAS_in[0]<=c_bb_t2_t3*MAS[0]

	S += c_bb_t2_t3_in*MAS_in[1]<=c_bb_t2_t3*MAS[1]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	c_bb_t2_t3_mem0 += MAS_MEM[2]
	S += 14 < c_bb_t2_t3_mem0
	S += c_bb_t2_t3_mem0 <= c_bb_t2_t3

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	c_bb_t2_t3_mem1 += MAS_MEM[1]
	S += 11 < c_bb_t2_t3_mem1
	S += c_bb_t2_t3_mem1 <= c_bb_t2_t3

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=11, delay_cost=1)
	c_bb_t3_t4 += alt(MM)
	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	c_bb_t3_t4_in += alt(MM_in)
	S += c_bb_t3_t4_in*MM_in[0]<=c_bb_t3_t4*MM[0]
	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	c_bb_t3_t4_mem0 += MAS_MEM[0]
	S += 4 < c_bb_t3_t4_mem0
	S += c_bb_t3_t4_mem0 <= c_bb_t3_t4

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	c_bb_t3_t4_mem1 += MAS_MEM[1]
	S += 28 < c_bb_t3_t4_mem1
	S += c_bb_t3_t4_mem1 <= c_bb_t3_t4

	c_bb_t30 = S.Task('c_bb_t30', length=3, delay_cost=1)
	c_bb_t30 += alt(MAS)
	c_bb_t30_in = S.Task('c_bb_t30_in', length=1, delay_cost=1)
	c_bb_t30_in += alt(MAS_in)
	S += c_bb_t30_in*MAS_in[0]<=c_bb_t30*MAS[0]

	S += c_bb_t30_in*MAS_in[1]<=c_bb_t30*MAS[1]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	c_bb_t30_mem0 += MM_MEM[0]
	S += 33 < c_bb_t30_mem0
	S += c_bb_t30_mem0 <= c_bb_t30

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	c_bb_t30_mem1 += MM_MEM[1]
	S += 28 < c_bb_t30_mem1
	S += c_bb_t30_mem1 <= c_bb_t30

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=3, delay_cost=1)
	c_bb_t3_t5 += alt(MAS)
	c_bb_t3_t5_in = S.Task('c_bb_t3_t5_in', length=1, delay_cost=1)
	c_bb_t3_t5_in += alt(MAS_in)
	S += c_bb_t3_t5_in*MAS_in[0]<=c_bb_t3_t5*MAS[0]

	S += c_bb_t3_t5_in*MAS_in[1]<=c_bb_t3_t5*MAS[1]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	c_bb_t3_t5_mem0 += MM_MEM[0]
	S += 33 < c_bb_t3_t5_mem0
	S += c_bb_t3_t5_mem0 <= c_bb_t3_t5

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	c_bb_t3_t5_mem1 += MM_MEM[1]
	S += 28 < c_bb_t3_t5_mem1
	S += c_bb_t3_t5_mem1 <= c_bb_t3_t5

	c_cc_t00 = S.Task('c_cc_t00', length=3, delay_cost=1)
	c_cc_t00 += alt(MAS)
	c_cc_t00_in = S.Task('c_cc_t00_in', length=1, delay_cost=1)
	c_cc_t00_in += alt(MAS_in)
	S += c_cc_t00_in*MAS_in[0]<=c_cc_t00*MAS[0]

	S += c_cc_t00_in*MAS_in[1]<=c_cc_t00*MAS[1]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	c_cc_t00_mem0 += MAIN_MEM_r[0]
	S += c_cc_t00_mem0 <= c_cc_t00

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	c_cc_t00_mem1 += MAS_MEM[3]
	S += 8 < c_cc_t00_mem1
	S += c_cc_t00_mem1 <= c_cc_t00

	c_cc_t01 = S.Task('c_cc_t01', length=3, delay_cost=1)
	c_cc_t01 += alt(MAS)
	c_cc_t01_in = S.Task('c_cc_t01_in', length=1, delay_cost=1)
	c_cc_t01_in += alt(MAS_in)
	S += c_cc_t01_in*MAS_in[0]<=c_cc_t01*MAS[0]

	S += c_cc_t01_in*MAS_in[1]<=c_cc_t01*MAS[1]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	c_cc_t01_mem0 += MAIN_MEM_r[0]
	S += c_cc_t01_mem0 <= c_cc_t01

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	c_cc_t01_mem1 += MAS_MEM[1]
	S += 15 < c_cc_t01_mem1
	S += c_cc_t01_mem1 <= c_cc_t01

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=3, delay_cost=1)
	c_cc_t2_t3 += alt(MAS)
	c_cc_t2_t3_in = S.Task('c_cc_t2_t3_in', length=1, delay_cost=1)
	c_cc_t2_t3_in += alt(MAS_in)
	S += c_cc_t2_t3_in*MAS_in[0]<=c_cc_t2_t3*MAS[0]

	S += c_cc_t2_t3_in*MAS_in[1]<=c_cc_t2_t3*MAS[1]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	c_cc_t2_t3_mem0 += MAS_MEM[0]
	S += 22 < c_cc_t2_t3_mem0
	S += c_cc_t2_t3_mem0 <= c_cc_t2_t3

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	c_cc_t2_t3_mem1 += MAS_MEM[1]
	S += 18 < c_cc_t2_t3_mem1
	S += c_cc_t2_t3_mem1 <= c_cc_t2_t3

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=11, delay_cost=1)
	c_cc_t3_t4 += alt(MM)
	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	c_cc_t3_t4_in += alt(MM_in)
	S += c_cc_t3_t4_in*MM_in[0]<=c_cc_t3_t4*MM[0]
	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	c_cc_t3_t4_mem0 += MAS_MEM[0]
	S += 7 < c_cc_t3_t4_mem0
	S += c_cc_t3_t4_mem0 <= c_cc_t3_t4

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	c_cc_t3_t4_mem1 += MAS_MEM[1]
	S += 9 < c_cc_t3_t4_mem1
	S += c_cc_t3_t4_mem1 <= c_cc_t3_t4

	c_cc_t30 = S.Task('c_cc_t30', length=3, delay_cost=1)
	c_cc_t30 += alt(MAS)
	c_cc_t30_in = S.Task('c_cc_t30_in', length=1, delay_cost=1)
	c_cc_t30_in += alt(MAS_in)
	S += c_cc_t30_in*MAS_in[0]<=c_cc_t30*MAS[0]

	S += c_cc_t30_in*MAS_in[1]<=c_cc_t30*MAS[1]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	c_cc_t30_mem0 += MM_MEM[0]
	S += 13 < c_cc_t30_mem0
	S += c_cc_t30_mem0 <= c_cc_t30

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	c_cc_t30_mem1 += MM_MEM[1]
	S += 14 < c_cc_t30_mem1
	S += c_cc_t30_mem1 <= c_cc_t30

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=3, delay_cost=1)
	c_cc_t3_t5 += alt(MAS)
	c_cc_t3_t5_in = S.Task('c_cc_t3_t5_in', length=1, delay_cost=1)
	c_cc_t3_t5_in += alt(MAS_in)
	S += c_cc_t3_t5_in*MAS_in[0]<=c_cc_t3_t5*MAS[0]

	S += c_cc_t3_t5_in*MAS_in[1]<=c_cc_t3_t5*MAS[1]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	c_cc_t3_t5_mem0 += MM_MEM[0]
	S += 13 < c_cc_t3_t5_mem0
	S += c_cc_t3_t5_mem0 <= c_cc_t3_t5

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	c_cc_t3_t5_mem1 += MM_MEM[1]
	S += 14 < c_cc_t3_t5_mem1
	S += c_cc_t3_t5_mem1 <= c_cc_t3_t5

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=11, delay_cost=1)
	c_ab_t0_t4 += alt(MM)
	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	c_ab_t0_t4_in += alt(MM_in)
	S += c_ab_t0_t4_in*MM_in[0]<=c_ab_t0_t4*MM[0]
	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	c_ab_t0_t4_mem0 += MAS_MEM[2]
	S += 3 < c_ab_t0_t4_mem0
	S += c_ab_t0_t4_mem0 <= c_ab_t0_t4

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	c_ab_t0_t4_mem1 += MAS_MEM[3]
	S += 10 < c_ab_t0_t4_mem1
	S += c_ab_t0_t4_mem1 <= c_ab_t0_t4

	c_ab_t00 = S.Task('c_ab_t00', length=3, delay_cost=1)
	c_ab_t00 += alt(MAS)
	c_ab_t00_in = S.Task('c_ab_t00_in', length=1, delay_cost=1)
	c_ab_t00_in += alt(MAS_in)
	S += c_ab_t00_in*MAS_in[0]<=c_ab_t00*MAS[0]

	S += c_ab_t00_in*MAS_in[1]<=c_ab_t00*MAS[1]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	c_ab_t00_mem0 += MM_MEM[0]
	S += 38 < c_ab_t00_mem0
	S += c_ab_t00_mem0 <= c_ab_t00

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	c_ab_t00_mem1 += MM_MEM[1]
	S += 34 < c_ab_t00_mem1
	S += c_ab_t00_mem1 <= c_ab_t00

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=3, delay_cost=1)
	c_ab_t0_t5 += alt(MAS)
	c_ab_t0_t5_in = S.Task('c_ab_t0_t5_in', length=1, delay_cost=1)
	c_ab_t0_t5_in += alt(MAS_in)
	S += c_ab_t0_t5_in*MAS_in[0]<=c_ab_t0_t5*MAS[0]

	S += c_ab_t0_t5_in*MAS_in[1]<=c_ab_t0_t5*MAS[1]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	c_ab_t0_t5_mem0 += MM_MEM[0]
	S += 38 < c_ab_t0_t5_mem0
	S += c_ab_t0_t5_mem0 <= c_ab_t0_t5

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	c_ab_t0_t5_mem1 += MM_MEM[1]
	S += 34 < c_ab_t0_t5_mem1
	S += c_ab_t0_t5_mem1 <= c_ab_t0_t5

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=11, delay_cost=1)
	c_ab_t1_t4 += alt(MM)
	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	c_ab_t1_t4_in += alt(MM_in)
	S += c_ab_t1_t4_in*MM_in[0]<=c_ab_t1_t4*MM[0]
	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	c_ab_t1_t4_mem0 += MAS_MEM[2]
	S += 39 < c_ab_t1_t4_mem0
	S += c_ab_t1_t4_mem0 <= c_ab_t1_t4

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	c_ab_t1_t4_mem1 += MAS_MEM[1]
	S += 46 < c_ab_t1_t4_mem1
	S += c_ab_t1_t4_mem1 <= c_ab_t1_t4

	c_ab_t10 = S.Task('c_ab_t10', length=3, delay_cost=1)
	c_ab_t10 += alt(MAS)
	c_ab_t10_in = S.Task('c_ab_t10_in', length=1, delay_cost=1)
	c_ab_t10_in += alt(MAS_in)
	S += c_ab_t10_in*MAS_in[0]<=c_ab_t10*MAS[0]

	S += c_ab_t10_in*MAS_in[1]<=c_ab_t10*MAS[1]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	c_ab_t10_mem0 += MM_MEM[0]
	S += 27 < c_ab_t10_mem0
	S += c_ab_t10_mem0 <= c_ab_t10

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	c_ab_t10_mem1 += MM_MEM[1]
	S += 21 < c_ab_t10_mem1
	S += c_ab_t10_mem1 <= c_ab_t10

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=3, delay_cost=1)
	c_ab_t1_t5 += alt(MAS)
	c_ab_t1_t5_in = S.Task('c_ab_t1_t5_in', length=1, delay_cost=1)
	c_ab_t1_t5_in += alt(MAS_in)
	S += c_ab_t1_t5_in*MAS_in[0]<=c_ab_t1_t5*MAS[0]

	S += c_ab_t1_t5_in*MAS_in[1]<=c_ab_t1_t5*MAS[1]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	c_ab_t1_t5_mem0 += MM_MEM[0]
	S += 27 < c_ab_t1_t5_mem0
	S += c_ab_t1_t5_mem0 <= c_ab_t1_t5

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	c_ab_t1_t5_mem1 += MM_MEM[1]
	S += 21 < c_ab_t1_t5_mem1
	S += c_ab_t1_t5_mem1 <= c_ab_t1_t5

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=11, delay_cost=1)
	c_ab_t4_t0 += alt(MM)
	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	c_ab_t4_t0_in += alt(MM_in)
	S += c_ab_t4_t0_in*MM_in[0]<=c_ab_t4_t0*MM[0]
	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	c_ab_t4_t0_mem0 += MAS_MEM[0]
	S += 36 < c_ab_t4_t0_mem0
	S += c_ab_t4_t0_mem0 <= c_ab_t4_t0

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	c_ab_t4_t0_mem1 += MAS_MEM[1]
	S += 38 < c_ab_t4_t0_mem1
	S += c_ab_t4_t0_mem1 <= c_ab_t4_t0

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=11, delay_cost=1)
	c_ab_t4_t1 += alt(MM)
	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	c_ab_t4_t1_in += alt(MM_in)
	S += c_ab_t4_t1_in*MM_in[0]<=c_ab_t4_t1*MM[0]
	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	c_ab_t4_t1_mem0 += MAS_MEM[2]
	S += 54 < c_ab_t4_t1_mem0
	S += c_ab_t4_t1_mem0 <= c_ab_t4_t1

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	c_ab_t4_t1_mem1 += MAS_MEM[1]
	S += 57 < c_ab_t4_t1_mem1
	S += c_ab_t4_t1_mem1 <= c_ab_t4_t1

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=3, delay_cost=1)
	c_ab_t4_t2 += alt(MAS)
	c_ab_t4_t2_in = S.Task('c_ab_t4_t2_in', length=1, delay_cost=1)
	c_ab_t4_t2_in += alt(MAS_in)
	S += c_ab_t4_t2_in*MAS_in[0]<=c_ab_t4_t2*MAS[0]

	S += c_ab_t4_t2_in*MAS_in[1]<=c_ab_t4_t2*MAS[1]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	c_ab_t4_t2_mem0 += MAS_MEM[0]
	S += 36 < c_ab_t4_t2_mem0
	S += c_ab_t4_t2_mem0 <= c_ab_t4_t2

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	c_ab_t4_t2_mem1 += MAS_MEM[3]
	S += 54 < c_ab_t4_t2_mem1
	S += c_ab_t4_t2_mem1 <= c_ab_t4_t2

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=3, delay_cost=1)
	c_ab_t4_t3 += alt(MAS)
	c_ab_t4_t3_in = S.Task('c_ab_t4_t3_in', length=1, delay_cost=1)
	c_ab_t4_t3_in += alt(MAS_in)
	S += c_ab_t4_t3_in*MAS_in[0]<=c_ab_t4_t3*MAS[0]

	S += c_ab_t4_t3_in*MAS_in[1]<=c_ab_t4_t3*MAS[1]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	c_ab_t4_t3_mem0 += MAS_MEM[0]
	S += 38 < c_ab_t4_t3_mem0
	S += c_ab_t4_t3_mem0 <= c_ab_t4_t3

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	c_ab_t4_t3_mem1 += MAS_MEM[1]
	S += 57 < c_ab_t4_t3_mem1
	S += c_ab_t4_t3_mem1 <= c_ab_t4_t3

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=11, delay_cost=1)
	c_bc_t0_t4 += alt(MM)
	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	c_bc_t0_t4_in += alt(MM_in)
	S += c_bc_t0_t4_in*MM_in[0]<=c_bc_t0_t4*MM[0]
	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	c_bc_t0_t4_mem0 += MAS_MEM[0]
	S += 40 < c_bc_t0_t4_mem0
	S += c_bc_t0_t4_mem0 <= c_bc_t0_t4

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	c_bc_t0_t4_mem1 += MAS_MEM[3]
	S += 52 < c_bc_t0_t4_mem1
	S += c_bc_t0_t4_mem1 <= c_bc_t0_t4

	c_bc_t00 = S.Task('c_bc_t00', length=3, delay_cost=1)
	c_bc_t00 += alt(MAS)
	c_bc_t00_in = S.Task('c_bc_t00_in', length=1, delay_cost=1)
	c_bc_t00_in += alt(MAS_in)
	S += c_bc_t00_in*MAS_in[0]<=c_bc_t00*MAS[0]

	S += c_bc_t00_in*MAS_in[1]<=c_bc_t00*MAS[1]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	c_bc_t00_mem0 += MM_MEM[0]
	S += 63 < c_bc_t00_mem0
	S += c_bc_t00_mem0 <= c_bc_t00

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	c_bc_t00_mem1 += MM_MEM[1]
	S += 51 < c_bc_t00_mem1
	S += c_bc_t00_mem1 <= c_bc_t00

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=3, delay_cost=1)
	c_bc_t0_t5 += alt(MAS)
	c_bc_t0_t5_in = S.Task('c_bc_t0_t5_in', length=1, delay_cost=1)
	c_bc_t0_t5_in += alt(MAS_in)
	S += c_bc_t0_t5_in*MAS_in[0]<=c_bc_t0_t5*MAS[0]

	S += c_bc_t0_t5_in*MAS_in[1]<=c_bc_t0_t5*MAS[1]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	c_bc_t0_t5_mem0 += MM_MEM[0]
	S += 63 < c_bc_t0_t5_mem0
	S += c_bc_t0_t5_mem0 <= c_bc_t0_t5

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	c_bc_t0_t5_mem1 += MM_MEM[1]
	S += 51 < c_bc_t0_t5_mem1
	S += c_bc_t0_t5_mem1 <= c_bc_t0_t5

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=11, delay_cost=1)
	c_bc_t1_t4 += alt(MM)
	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	c_bc_t1_t4_in += alt(MM_in)
	S += c_bc_t1_t4_in*MM_in[0]<=c_bc_t1_t4*MM[0]
	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	c_bc_t1_t4_mem0 += MAS_MEM[0]
	S += 37 < c_bc_t1_t4_mem0
	S += c_bc_t1_t4_mem0 <= c_bc_t1_t4

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	c_bc_t1_t4_mem1 += MAS_MEM[1]
	S += 53 < c_bc_t1_t4_mem1
	S += c_bc_t1_t4_mem1 <= c_bc_t1_t4

	c_bc_t10 = S.Task('c_bc_t10', length=3, delay_cost=1)
	c_bc_t10 += alt(MAS)
	c_bc_t10_in = S.Task('c_bc_t10_in', length=1, delay_cost=1)
	c_bc_t10_in += alt(MAS_in)
	S += c_bc_t10_in*MAS_in[0]<=c_bc_t10*MAS[0]

	S += c_bc_t10_in*MAS_in[1]<=c_bc_t10*MAS[1]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	c_bc_t10_mem0 += MM_MEM[0]
	S += 50 < c_bc_t10_mem0
	S += c_bc_t10_mem0 <= c_bc_t10

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	c_bc_t10_mem1 += MM_MEM[1]
	S += 66 < c_bc_t10_mem1
	S += c_bc_t10_mem1 <= c_bc_t10

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=3, delay_cost=1)
	c_bc_t1_t5 += alt(MAS)
	c_bc_t1_t5_in = S.Task('c_bc_t1_t5_in', length=1, delay_cost=1)
	c_bc_t1_t5_in += alt(MAS_in)
	S += c_bc_t1_t5_in*MAS_in[0]<=c_bc_t1_t5*MAS[0]

	S += c_bc_t1_t5_in*MAS_in[1]<=c_bc_t1_t5*MAS[1]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	c_bc_t1_t5_mem0 += MM_MEM[0]
	S += 50 < c_bc_t1_t5_mem0
	S += c_bc_t1_t5_mem0 <= c_bc_t1_t5

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	c_bc_t1_t5_mem1 += MM_MEM[1]
	S += 66 < c_bc_t1_t5_mem1
	S += c_bc_t1_t5_mem1 <= c_bc_t1_t5

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=11, delay_cost=1)
	c_bc_t4_t0 += alt(MM)
	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	c_bc_t4_t0_in += alt(MM_in)
	S += c_bc_t4_t0_in*MM_in[0]<=c_bc_t4_t0*MM[0]
	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	c_bc_t4_t0_mem0 += MAS_MEM[2]
	S += 44 < c_bc_t4_t0_mem0
	S += c_bc_t4_t0_mem0 <= c_bc_t4_t0

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	c_bc_t4_t0_mem1 += MAS_MEM[1]
	S += 45 < c_bc_t4_t0_mem1
	S += c_bc_t4_t0_mem1 <= c_bc_t4_t0

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=11, delay_cost=1)
	c_bc_t4_t1 += alt(MM)
	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	c_bc_t4_t1_in += alt(MM_in)
	S += c_bc_t4_t1_in*MM_in[0]<=c_bc_t4_t1*MM[0]
	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	c_bc_t4_t1_mem0 += MAS_MEM[2]
	S += 50 < c_bc_t4_t1_mem0
	S += c_bc_t4_t1_mem0 <= c_bc_t4_t1

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	c_bc_t4_t1_mem1 += MAS_MEM[1]
	S += 51 < c_bc_t4_t1_mem1
	S += c_bc_t4_t1_mem1 <= c_bc_t4_t1

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=3, delay_cost=1)
	c_bc_t4_t2 += alt(MAS)
	c_bc_t4_t2_in = S.Task('c_bc_t4_t2_in', length=1, delay_cost=1)
	c_bc_t4_t2_in += alt(MAS_in)
	S += c_bc_t4_t2_in*MAS_in[0]<=c_bc_t4_t2*MAS[0]

	S += c_bc_t4_t2_in*MAS_in[1]<=c_bc_t4_t2*MAS[1]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	c_bc_t4_t2_mem0 += MAS_MEM[2]
	S += 44 < c_bc_t4_t2_mem0
	S += c_bc_t4_t2_mem0 <= c_bc_t4_t2

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	c_bc_t4_t2_mem1 += MAS_MEM[3]
	S += 50 < c_bc_t4_t2_mem1
	S += c_bc_t4_t2_mem1 <= c_bc_t4_t2

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=3, delay_cost=1)
	c_bc_t4_t3 += alt(MAS)
	c_bc_t4_t3_in = S.Task('c_bc_t4_t3_in', length=1, delay_cost=1)
	c_bc_t4_t3_in += alt(MAS_in)
	S += c_bc_t4_t3_in*MAS_in[0]<=c_bc_t4_t3*MAS[0]

	S += c_bc_t4_t3_in*MAS_in[1]<=c_bc_t4_t3*MAS[1]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	c_bc_t4_t3_mem0 += MAS_MEM[0]
	S += 45 < c_bc_t4_t3_mem0
	S += c_bc_t4_t3_mem0 <= c_bc_t4_t3

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	c_bc_t4_t3_mem1 += MAS_MEM[1]
	S += 51 < c_bc_t4_t3_mem1
	S += c_bc_t4_t3_mem1 <= c_bc_t4_t3

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=11, delay_cost=1)
	c_ac_t0_t4 += alt(MM)
	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	c_ac_t0_t4_in += alt(MM_in)
	S += c_ac_t0_t4_in*MM_in[0]<=c_ac_t0_t4*MM[0]
	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	c_ac_t0_t4_mem0 += MAS_MEM[0]
	S += 56 < c_ac_t0_t4_mem0
	S += c_ac_t0_t4_mem0 <= c_ac_t0_t4

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	c_ac_t0_t4_mem1 += MAS_MEM[1]
	S += 41 < c_ac_t0_t4_mem1
	S += c_ac_t0_t4_mem1 <= c_ac_t0_t4

	c_ac_t00 = S.Task('c_ac_t00', length=3, delay_cost=1)
	c_ac_t00 += alt(MAS)
	c_ac_t00_in = S.Task('c_ac_t00_in', length=1, delay_cost=1)
	c_ac_t00_in += alt(MAS_in)
	S += c_ac_t00_in*MAS_in[0]<=c_ac_t00*MAS[0]

	S += c_ac_t00_in*MAS_in[1]<=c_ac_t00*MAS[1]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	c_ac_t00_mem0 += MM_MEM[0]
	S += 70 < c_ac_t00_mem0
	S += c_ac_t00_mem0 <= c_ac_t00

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	c_ac_t00_mem1 += MM_MEM[1]
	S += 69 < c_ac_t00_mem1
	S += c_ac_t00_mem1 <= c_ac_t00

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=3, delay_cost=1)
	c_ac_t0_t5 += alt(MAS)
	c_ac_t0_t5_in = S.Task('c_ac_t0_t5_in', length=1, delay_cost=1)
	c_ac_t0_t5_in += alt(MAS_in)
	S += c_ac_t0_t5_in*MAS_in[0]<=c_ac_t0_t5*MAS[0]

	S += c_ac_t0_t5_in*MAS_in[1]<=c_ac_t0_t5*MAS[1]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	c_ac_t0_t5_mem0 += MM_MEM[0]
	S += 70 < c_ac_t0_t5_mem0
	S += c_ac_t0_t5_mem0 <= c_ac_t0_t5

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	c_ac_t0_t5_mem1 += MM_MEM[1]
	S += 69 < c_ac_t0_t5_mem1
	S += c_ac_t0_t5_mem1 <= c_ac_t0_t5

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=11, delay_cost=1)
	c_ac_t1_t4 += alt(MM)
	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	c_ac_t1_t4_in += alt(MM_in)
	S += c_ac_t1_t4_in*MM_in[0]<=c_ac_t1_t4*MM[0]
	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	c_ac_t1_t4_mem0 += MAS_MEM[0]
	S += 34 < c_ac_t1_t4_mem0
	S += c_ac_t1_t4_mem0 <= c_ac_t1_t4

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	c_ac_t1_t4_mem1 += MAS_MEM[3]
	S += 48 < c_ac_t1_t4_mem1
	S += c_ac_t1_t4_mem1 <= c_ac_t1_t4

	c_ac_t10 = S.Task('c_ac_t10', length=3, delay_cost=1)
	c_ac_t10 += alt(MAS)
	c_ac_t10_in = S.Task('c_ac_t10_in', length=1, delay_cost=1)
	c_ac_t10_in += alt(MAS_in)
	S += c_ac_t10_in*MAS_in[0]<=c_ac_t10*MAS[0]

	S += c_ac_t10_in*MAS_in[1]<=c_ac_t10*MAS[1]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	c_ac_t10_mem0 += MM_MEM[0]
	S += 68 < c_ac_t10_mem0
	S += c_ac_t10_mem0 <= c_ac_t10

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	c_ac_t10_mem1 += MM_MEM[1]
	S += 67 < c_ac_t10_mem1
	S += c_ac_t10_mem1 <= c_ac_t10

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=3, delay_cost=1)
	c_ac_t1_t5 += alt(MAS)
	c_ac_t1_t5_in = S.Task('c_ac_t1_t5_in', length=1, delay_cost=1)
	c_ac_t1_t5_in += alt(MAS_in)
	S += c_ac_t1_t5_in*MAS_in[0]<=c_ac_t1_t5*MAS[0]

	S += c_ac_t1_t5_in*MAS_in[1]<=c_ac_t1_t5*MAS[1]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	c_ac_t1_t5_mem0 += MM_MEM[0]
	S += 68 < c_ac_t1_t5_mem0
	S += c_ac_t1_t5_mem0 <= c_ac_t1_t5

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	c_ac_t1_t5_mem1 += MM_MEM[1]
	S += 67 < c_ac_t1_t5_mem1
	S += c_ac_t1_t5_mem1 <= c_ac_t1_t5

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=11, delay_cost=1)
	c_ac_t4_t0 += alt(MM)
	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	c_ac_t4_t0_in += alt(MM_in)
	S += c_ac_t4_t0_in*MM_in[0]<=c_ac_t4_t0*MM[0]
	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	c_ac_t4_t0_mem0 += MAS_MEM[0]
	S += 35 < c_ac_t4_t0_mem0
	S += c_ac_t4_t0_mem0 <= c_ac_t4_t0

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	c_ac_t4_t0_mem1 += MAS_MEM[1]
	S += 49 < c_ac_t4_t0_mem1
	S += c_ac_t4_t0_mem1 <= c_ac_t4_t0

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=11, delay_cost=1)
	c_ac_t4_t1 += alt(MM)
	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	c_ac_t4_t1_in += alt(MM_in)
	S += c_ac_t4_t1_in*MM_in[0]<=c_ac_t4_t1*MM[0]
	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	c_ac_t4_t1_mem0 += MAS_MEM[2]
	S += 33 < c_ac_t4_t1_mem0
	S += c_ac_t4_t1_mem0 <= c_ac_t4_t1

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	c_ac_t4_t1_mem1 += MAS_MEM[1]
	S += 47 < c_ac_t4_t1_mem1
	S += c_ac_t4_t1_mem1 <= c_ac_t4_t1

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=3, delay_cost=1)
	c_ac_t4_t2 += alt(MAS)
	c_ac_t4_t2_in = S.Task('c_ac_t4_t2_in', length=1, delay_cost=1)
	c_ac_t4_t2_in += alt(MAS_in)
	S += c_ac_t4_t2_in*MAS_in[0]<=c_ac_t4_t2*MAS[0]

	S += c_ac_t4_t2_in*MAS_in[1]<=c_ac_t4_t2*MAS[1]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	c_ac_t4_t2_mem0 += MAS_MEM[0]
	S += 35 < c_ac_t4_t2_mem0
	S += c_ac_t4_t2_mem0 <= c_ac_t4_t2

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	c_ac_t4_t2_mem1 += MAS_MEM[3]
	S += 33 < c_ac_t4_t2_mem1
	S += c_ac_t4_t2_mem1 <= c_ac_t4_t2

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=3, delay_cost=1)
	c_ac_t4_t3 += alt(MAS)
	c_ac_t4_t3_in = S.Task('c_ac_t4_t3_in', length=1, delay_cost=1)
	c_ac_t4_t3_in += alt(MAS_in)
	S += c_ac_t4_t3_in*MAS_in[0]<=c_ac_t4_t3*MAS[0]

	S += c_ac_t4_t3_in*MAS_in[1]<=c_ac_t4_t3*MAS[1]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	c_ac_t4_t3_mem0 += MAS_MEM[0]
	S += 49 < c_ac_t4_t3_mem0
	S += c_ac_t4_t3_mem0 <= c_ac_t4_t3

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	c_ac_t4_t3_mem1 += MAS_MEM[1]
	S += 47 < c_ac_t4_t3_mem1
	S += c_ac_t4_t3_mem1 <= c_ac_t4_t3

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=3, delay_cost=1)
	c_pbc_t4_t3 += alt(MAS)
	c_pbc_t4_t3_in = S.Task('c_pbc_t4_t3_in', length=1, delay_cost=1)
	c_pbc_t4_t3_in += alt(MAS_in)
	S += c_pbc_t4_t3_in*MAS_in[0]<=c_pbc_t4_t3*MAS[0]

	S += c_pbc_t4_t3_in*MAS_in[1]<=c_pbc_t4_t3*MAS[1]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	c_pbc_t4_t3_mem0 += MAS_MEM[0]
	S += 73 < c_pbc_t4_t3_mem0
	S += c_pbc_t4_t3_mem0 <= c_pbc_t4_t3

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	c_pbc_t4_t3_mem1 += MAS_MEM[1]
	S += 67 < c_pbc_t4_t3_mem1
	S += c_pbc_t4_t3_mem1 <= c_pbc_t4_t3

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=3, delay_cost=1)
	c_pcb_t4_t3 += alt(MAS)
	c_pcb_t4_t3_in = S.Task('c_pcb_t4_t3_in', length=1, delay_cost=1)
	c_pcb_t4_t3_in += alt(MAS_in)
	S += c_pcb_t4_t3_in*MAS_in[0]<=c_pcb_t4_t3*MAS[0]

	S += c_pcb_t4_t3_in*MAS_in[1]<=c_pcb_t4_t3*MAS[1]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	c_pcb_t4_t3_mem0 += MAS_MEM[2]
	S += 74 < c_pcb_t4_t3_mem0
	S += c_pcb_t4_t3_mem0 <= c_pcb_t4_t3

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	c_pcb_t4_t3_mem1 += MAS_MEM[3]
	S += 71 < c_pcb_t4_t3_mem1
	S += c_pcb_t4_t3_mem1 <= c_pcb_t4_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS2/FP12_INV_BEFORE_FPINV/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution

