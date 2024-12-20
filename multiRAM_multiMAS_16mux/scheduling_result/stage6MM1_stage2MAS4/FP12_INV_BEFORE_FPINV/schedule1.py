from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 156
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 0
	c_cc_t3_t3_in += MAS_in[2]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 0
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 0
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 1
	c_aa_t3_t2_in += MAS_in[2]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 1
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 1
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=2, delay_cost=1)
	S += c_cc_t3_t3 >= 1
	c_cc_t3_t3 += MAS[2]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=2, delay_cost=1)
	S += c_aa_t3_t2 >= 2
	c_aa_t3_t2 += MAS[2]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 2
	c_bb_t10_in += MAS_in[1]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 2
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 2
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t10 = S.Task('c_bb_t10', length=2, delay_cost=1)
	S += c_bb_t10 >= 3
	c_bb_t10 += MAS[1]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 3
	c_cc_a1_1_in += MAS_in[3]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 3
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 3
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 4
	c_bb_t3_t3_in += MAS_in[0]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 4
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 4
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=2, delay_cost=1)
	S += c_cc_a1_1 >= 4
	c_cc_a1_1 += MAS[3]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=2, delay_cost=1)
	S += c_bb_t3_t3 >= 5
	c_bb_t3_t3 += MAS[0]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 5
	c_cc_t10_in += MAS_in[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 5
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 5
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 6
	c_bb_a1_1_in += MAS_in[2]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 6
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 6
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=2, delay_cost=1)
	S += c_cc_t10 >= 6
	c_cc_t10 += MAS[0]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 7
	c_aa_a1_0_in += MAS_in[3]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 7
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 7
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=2, delay_cost=1)
	S += c_bb_a1_1 >= 7
	c_bb_a1_1 += MAS[2]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=2, delay_cost=1)
	S += c_aa_a1_0 >= 8
	c_aa_a1_0 += MAS[3]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 8
	c_aa_t11_in += MAS_in[0]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 8
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 8
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t11 = S.Task('c_aa_t11', length=2, delay_cost=1)
	S += c_aa_t11 >= 9
	c_aa_t11 += MAS[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 9
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 9
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 9
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=6, delay_cost=1)
	S += c_ab_t1_t0 >= 10
	c_ab_t1_t0 += MM[0]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 10
	c_cc_t3_t2_in += MAS_in[2]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 10
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 10
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 11
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 11
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 11
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=2, delay_cost=1)
	S += c_cc_t3_t2 >= 11
	c_cc_t3_t2 += MAS[2]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 12
	c_aa_t10_in += MAS_in[2]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 12
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 12
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=6, delay_cost=1)
	S += c_cc_t3_t0 >= 12
	c_cc_t3_t0 += MM[0]

	c_aa_t10 = S.Task('c_aa_t10', length=2, delay_cost=1)
	S += c_aa_t10 >= 13
	c_aa_t10 += MAS[2]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 13
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 13
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 13
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=6, delay_cost=1)
	S += c_bb_t3_t1 >= 14
	c_bb_t3_t1 += MM[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 14
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 14
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 14
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 15
	c_bb_t3_t2_in += MAS_in[3]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 15
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 15
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=6, delay_cost=1)
	S += c_cc_t3_t1 >= 15
	c_cc_t3_t1 += MM[0]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 16
	c_bb_a1_0_in += MAS_in[3]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 16
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 16
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=2, delay_cost=1)
	S += c_bb_t3_t2 >= 16
	c_bb_t3_t2 += MAS[3]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 17
	c_aa_t3_t3_in += MAS_in[1]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 17
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 17
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=2, delay_cost=1)
	S += c_bb_a1_0 >= 17
	c_bb_a1_0 += MAS[3]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=2, delay_cost=1)
	S += c_aa_t3_t3 >= 18
	c_aa_t3_t3 += MAS[1]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 18
	c_cc_a1_0_in += MAS_in[2]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 18
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 18
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 19
	c_aa_a1_1_in += MAS_in[1]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 19
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 19
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=2, delay_cost=1)
	S += c_cc_a1_0 >= 19
	c_cc_a1_0 += MAS[2]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=2, delay_cost=1)
	S += c_aa_a1_1 >= 20
	c_aa_a1_1 += MAS[1]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 20
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 20
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 20
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=6, delay_cost=1)
	S += c_ab_t1_t1 >= 21
	c_ab_t1_t1 += MM[0]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 21
	c_cc_t11_in += MAS_in[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 21
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 21
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 22
	c_ab_t0_t3_in += MAS_in[3]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 22
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 22
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=2, delay_cost=1)
	S += c_cc_t11 >= 22
	c_cc_t11 += MAS[0]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=2, delay_cost=1)
	S += c_ab_t0_t3 >= 23
	c_ab_t0_t3 += MAS[3]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 23
	c_bb_t11_in += MAS_in[2]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 23
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 23
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 24
	c_ab_t0_t2_in += MAS_in[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 24
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 24
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t11 = S.Task('c_bb_t11', length=2, delay_cost=1)
	S += c_bb_t11 >= 24
	c_bb_t11 += MAS[2]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=2, delay_cost=1)
	S += c_ab_t0_t2 >= 25
	c_ab_t0_t2 += MAS[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 25
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 25
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 25
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 26
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 26
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 26
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=6, delay_cost=1)
	S += c_bb_t3_t0 >= 26
	c_bb_t3_t0 += MM[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 27
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 27
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 27
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=6, delay_cost=1)
	S += c_ab_t0_t1 >= 27
	c_ab_t0_t1 += MM[0]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 28
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 28
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 28
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=6, delay_cost=1)
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

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=6, delay_cost=1)
	S += c_aa_t3_t1 >= 29
	c_aa_t3_t1 += MM[0]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=6, delay_cost=1)
	S += c_aa_t3_t0 >= 30
	c_aa_t3_t0 += MM[0]


	# new tasks
	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=2, delay_cost=1)
	c_ab_t1_t2 += alt(MAS)
	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	c_ab_t1_t2_in += alt(MAS_in)
	S += c_ab_t1_t2_in*MAS_in[0]<=c_ab_t1_t2*MAS[0]

	S += c_ab_t1_t2_in*MAS_in[1]<=c_ab_t1_t2*MAS[1]

	S += c_ab_t1_t2_in*MAS_in[2]<=c_ab_t1_t2*MAS[2]

	S += c_ab_t1_t2_in*MAS_in[3]<=c_ab_t1_t2*MAS[3]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c_ab_t1_t2_mem0 <= c_ab_t1_t2

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c_ab_t1_t2_mem1 <= c_ab_t1_t2

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=2, delay_cost=1)
	c_ab_t1_t3 += alt(MAS)
	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	c_ab_t1_t3_in += alt(MAS_in)
	S += c_ab_t1_t3_in*MAS_in[0]<=c_ab_t1_t3*MAS[0]

	S += c_ab_t1_t3_in*MAS_in[1]<=c_ab_t1_t3*MAS[1]

	S += c_ab_t1_t3_in*MAS_in[2]<=c_ab_t1_t3*MAS[2]

	S += c_ab_t1_t3_in*MAS_in[3]<=c_ab_t1_t3*MAS[3]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_ab_t1_t3_mem0 <= c_ab_t1_t3

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_ab_t1_t3_mem1 <= c_ab_t1_t3

	c_ab_t20 = S.Task('c_ab_t20', length=2, delay_cost=1)
	c_ab_t20 += alt(MAS)
	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	c_ab_t20_in += alt(MAS_in)
	S += c_ab_t20_in*MAS_in[0]<=c_ab_t20*MAS[0]

	S += c_ab_t20_in*MAS_in[1]<=c_ab_t20*MAS[1]

	S += c_ab_t20_in*MAS_in[2]<=c_ab_t20*MAS[2]

	S += c_ab_t20_in*MAS_in[3]<=c_ab_t20*MAS[3]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	c_ab_t20_mem0 += MAIN_MEM_r[0]
	S += c_ab_t20_mem0 <= c_ab_t20

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	c_ab_t20_mem1 += MAIN_MEM_r[1]
	S += c_ab_t20_mem1 <= c_ab_t20

	c_ab_t21 = S.Task('c_ab_t21', length=2, delay_cost=1)
	c_ab_t21 += alt(MAS)
	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	c_ab_t21_in += alt(MAS_in)
	S += c_ab_t21_in*MAS_in[0]<=c_ab_t21*MAS[0]

	S += c_ab_t21_in*MAS_in[1]<=c_ab_t21*MAS[1]

	S += c_ab_t21_in*MAS_in[2]<=c_ab_t21*MAS[2]

	S += c_ab_t21_in*MAS_in[3]<=c_ab_t21*MAS[3]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	c_ab_t21_mem0 += MAIN_MEM_r[0]
	S += c_ab_t21_mem0 <= c_ab_t21

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	c_ab_t21_mem1 += MAIN_MEM_r[1]
	S += c_ab_t21_mem1 <= c_ab_t21

	c_ab_t30 = S.Task('c_ab_t30', length=2, delay_cost=1)
	c_ab_t30 += alt(MAS)
	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	c_ab_t30_in += alt(MAS_in)
	S += c_ab_t30_in*MAS_in[0]<=c_ab_t30*MAS[0]

	S += c_ab_t30_in*MAS_in[1]<=c_ab_t30*MAS[1]

	S += c_ab_t30_in*MAS_in[2]<=c_ab_t30*MAS[2]

	S += c_ab_t30_in*MAS_in[3]<=c_ab_t30*MAS[3]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	c_ab_t30_mem0 += MAIN_MEM_r[0]
	S += c_ab_t30_mem0 <= c_ab_t30

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	c_ab_t30_mem1 += MAIN_MEM_r[1]
	S += c_ab_t30_mem1 <= c_ab_t30

	c_ab_t31 = S.Task('c_ab_t31', length=2, delay_cost=1)
	c_ab_t31 += alt(MAS)
	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	c_ab_t31_in += alt(MAS_in)
	S += c_ab_t31_in*MAS_in[0]<=c_ab_t31*MAS[0]

	S += c_ab_t31_in*MAS_in[1]<=c_ab_t31*MAS[1]

	S += c_ab_t31_in*MAS_in[2]<=c_ab_t31*MAS[2]

	S += c_ab_t31_in*MAS_in[3]<=c_ab_t31*MAS[3]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	c_ab_t31_mem0 += MAIN_MEM_r[0]
	S += c_ab_t31_mem0 <= c_ab_t31

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	c_ab_t31_mem1 += MAIN_MEM_r[1]
	S += c_ab_t31_mem1 <= c_ab_t31

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=6, delay_cost=1)
	c_bc_t0_t0 += alt(MM)
	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	c_bc_t0_t0_in += alt(MM_in)
	S += c_bc_t0_t0_in*MM_in[0]<=c_bc_t0_t0*MM[0]
	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c_bc_t0_t0_mem0 <= c_bc_t0_t0

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_bc_t0_t0_mem1 <= c_bc_t0_t0

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=6, delay_cost=1)
	c_bc_t0_t1 += alt(MM)
	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	c_bc_t0_t1_in += alt(MM_in)
	S += c_bc_t0_t1_in*MM_in[0]<=c_bc_t0_t1*MM[0]
	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c_bc_t0_t1_mem0 <= c_bc_t0_t1

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_bc_t0_t1_mem1 <= c_bc_t0_t1

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=2, delay_cost=1)
	c_bc_t0_t2 += alt(MAS)
	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	c_bc_t0_t2_in += alt(MAS_in)
	S += c_bc_t0_t2_in*MAS_in[0]<=c_bc_t0_t2*MAS[0]

	S += c_bc_t0_t2_in*MAS_in[1]<=c_bc_t0_t2*MAS[1]

	S += c_bc_t0_t2_in*MAS_in[2]<=c_bc_t0_t2*MAS[2]

	S += c_bc_t0_t2_in*MAS_in[3]<=c_bc_t0_t2*MAS[3]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c_bc_t0_t2_mem0 <= c_bc_t0_t2

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c_bc_t0_t2_mem1 <= c_bc_t0_t2

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=2, delay_cost=1)
	c_bc_t0_t3 += alt(MAS)
	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	c_bc_t0_t3_in += alt(MAS_in)
	S += c_bc_t0_t3_in*MAS_in[0]<=c_bc_t0_t3*MAS[0]

	S += c_bc_t0_t3_in*MAS_in[1]<=c_bc_t0_t3*MAS[1]

	S += c_bc_t0_t3_in*MAS_in[2]<=c_bc_t0_t3*MAS[2]

	S += c_bc_t0_t3_in*MAS_in[3]<=c_bc_t0_t3*MAS[3]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_bc_t0_t3_mem0 <= c_bc_t0_t3

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_bc_t0_t3_mem1 <= c_bc_t0_t3

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=6, delay_cost=1)
	c_bc_t1_t0 += alt(MM)
	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	c_bc_t1_t0_in += alt(MM_in)
	S += c_bc_t1_t0_in*MM_in[0]<=c_bc_t1_t0*MM[0]
	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c_bc_t1_t0_mem0 <= c_bc_t1_t0

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_bc_t1_t0_mem1 <= c_bc_t1_t0

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=6, delay_cost=1)
	c_bc_t1_t1 += alt(MM)
	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	c_bc_t1_t1_in += alt(MM_in)
	S += c_bc_t1_t1_in*MM_in[0]<=c_bc_t1_t1*MM[0]
	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c_bc_t1_t1_mem0 <= c_bc_t1_t1

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_bc_t1_t1_mem1 <= c_bc_t1_t1

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=2, delay_cost=1)
	c_bc_t1_t2 += alt(MAS)
	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	c_bc_t1_t2_in += alt(MAS_in)
	S += c_bc_t1_t2_in*MAS_in[0]<=c_bc_t1_t2*MAS[0]

	S += c_bc_t1_t2_in*MAS_in[1]<=c_bc_t1_t2*MAS[1]

	S += c_bc_t1_t2_in*MAS_in[2]<=c_bc_t1_t2*MAS[2]

	S += c_bc_t1_t2_in*MAS_in[3]<=c_bc_t1_t2*MAS[3]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c_bc_t1_t2_mem0 <= c_bc_t1_t2

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c_bc_t1_t2_mem1 <= c_bc_t1_t2

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=2, delay_cost=1)
	c_bc_t1_t3 += alt(MAS)
	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	c_bc_t1_t3_in += alt(MAS_in)
	S += c_bc_t1_t3_in*MAS_in[0]<=c_bc_t1_t3*MAS[0]

	S += c_bc_t1_t3_in*MAS_in[1]<=c_bc_t1_t3*MAS[1]

	S += c_bc_t1_t3_in*MAS_in[2]<=c_bc_t1_t3*MAS[2]

	S += c_bc_t1_t3_in*MAS_in[3]<=c_bc_t1_t3*MAS[3]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_bc_t1_t3_mem0 <= c_bc_t1_t3

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_bc_t1_t3_mem1 <= c_bc_t1_t3

	c_bc_t20 = S.Task('c_bc_t20', length=2, delay_cost=1)
	c_bc_t20 += alt(MAS)
	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	c_bc_t20_in += alt(MAS_in)
	S += c_bc_t20_in*MAS_in[0]<=c_bc_t20*MAS[0]

	S += c_bc_t20_in*MAS_in[1]<=c_bc_t20*MAS[1]

	S += c_bc_t20_in*MAS_in[2]<=c_bc_t20*MAS[2]

	S += c_bc_t20_in*MAS_in[3]<=c_bc_t20*MAS[3]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	c_bc_t20_mem0 += MAIN_MEM_r[0]
	S += c_bc_t20_mem0 <= c_bc_t20

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	c_bc_t20_mem1 += MAIN_MEM_r[1]
	S += c_bc_t20_mem1 <= c_bc_t20

	c_bc_t21 = S.Task('c_bc_t21', length=2, delay_cost=1)
	c_bc_t21 += alt(MAS)
	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	c_bc_t21_in += alt(MAS_in)
	S += c_bc_t21_in*MAS_in[0]<=c_bc_t21*MAS[0]

	S += c_bc_t21_in*MAS_in[1]<=c_bc_t21*MAS[1]

	S += c_bc_t21_in*MAS_in[2]<=c_bc_t21*MAS[2]

	S += c_bc_t21_in*MAS_in[3]<=c_bc_t21*MAS[3]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	c_bc_t21_mem0 += MAIN_MEM_r[0]
	S += c_bc_t21_mem0 <= c_bc_t21

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	c_bc_t21_mem1 += MAIN_MEM_r[1]
	S += c_bc_t21_mem1 <= c_bc_t21

	c_bc_t30 = S.Task('c_bc_t30', length=2, delay_cost=1)
	c_bc_t30 += alt(MAS)
	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	c_bc_t30_in += alt(MAS_in)
	S += c_bc_t30_in*MAS_in[0]<=c_bc_t30*MAS[0]

	S += c_bc_t30_in*MAS_in[1]<=c_bc_t30*MAS[1]

	S += c_bc_t30_in*MAS_in[2]<=c_bc_t30*MAS[2]

	S += c_bc_t30_in*MAS_in[3]<=c_bc_t30*MAS[3]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	c_bc_t30_mem0 += MAIN_MEM_r[0]
	S += c_bc_t30_mem0 <= c_bc_t30

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	c_bc_t30_mem1 += MAIN_MEM_r[1]
	S += c_bc_t30_mem1 <= c_bc_t30

	c_bc_t31 = S.Task('c_bc_t31', length=2, delay_cost=1)
	c_bc_t31 += alt(MAS)
	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	c_bc_t31_in += alt(MAS_in)
	S += c_bc_t31_in*MAS_in[0]<=c_bc_t31*MAS[0]

	S += c_bc_t31_in*MAS_in[1]<=c_bc_t31*MAS[1]

	S += c_bc_t31_in*MAS_in[2]<=c_bc_t31*MAS[2]

	S += c_bc_t31_in*MAS_in[3]<=c_bc_t31*MAS[3]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	c_bc_t31_mem0 += MAIN_MEM_r[0]
	S += c_bc_t31_mem0 <= c_bc_t31

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	c_bc_t31_mem1 += MAIN_MEM_r[1]
	S += c_bc_t31_mem1 <= c_bc_t31

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=6, delay_cost=1)
	c_ac_t0_t0 += alt(MM)
	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	c_ac_t0_t0_in += alt(MM_in)
	S += c_ac_t0_t0_in*MM_in[0]<=c_ac_t0_t0*MM[0]
	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c_ac_t0_t0_mem0 <= c_ac_t0_t0

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_ac_t0_t0_mem1 <= c_ac_t0_t0

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=6, delay_cost=1)
	c_ac_t0_t1 += alt(MM)
	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	c_ac_t0_t1_in += alt(MM_in)
	S += c_ac_t0_t1_in*MM_in[0]<=c_ac_t0_t1*MM[0]
	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c_ac_t0_t1_mem0 <= c_ac_t0_t1

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_ac_t0_t1_mem1 <= c_ac_t0_t1

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=2, delay_cost=1)
	c_ac_t0_t2 += alt(MAS)
	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	c_ac_t0_t2_in += alt(MAS_in)
	S += c_ac_t0_t2_in*MAS_in[0]<=c_ac_t0_t2*MAS[0]

	S += c_ac_t0_t2_in*MAS_in[1]<=c_ac_t0_t2*MAS[1]

	S += c_ac_t0_t2_in*MAS_in[2]<=c_ac_t0_t2*MAS[2]

	S += c_ac_t0_t2_in*MAS_in[3]<=c_ac_t0_t2*MAS[3]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c_ac_t0_t2_mem0 <= c_ac_t0_t2

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c_ac_t0_t2_mem1 <= c_ac_t0_t2

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=2, delay_cost=1)
	c_ac_t0_t3 += alt(MAS)
	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	c_ac_t0_t3_in += alt(MAS_in)
	S += c_ac_t0_t3_in*MAS_in[0]<=c_ac_t0_t3*MAS[0]

	S += c_ac_t0_t3_in*MAS_in[1]<=c_ac_t0_t3*MAS[1]

	S += c_ac_t0_t3_in*MAS_in[2]<=c_ac_t0_t3*MAS[2]

	S += c_ac_t0_t3_in*MAS_in[3]<=c_ac_t0_t3*MAS[3]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_ac_t0_t3_mem0 <= c_ac_t0_t3

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_ac_t0_t3_mem1 <= c_ac_t0_t3

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=6, delay_cost=1)
	c_ac_t1_t0 += alt(MM)
	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	c_ac_t1_t0_in += alt(MM_in)
	S += c_ac_t1_t0_in*MM_in[0]<=c_ac_t1_t0*MM[0]
	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c_ac_t1_t0_mem0 <= c_ac_t1_t0

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_ac_t1_t0_mem1 <= c_ac_t1_t0

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=6, delay_cost=1)
	c_ac_t1_t1 += alt(MM)
	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	c_ac_t1_t1_in += alt(MM_in)
	S += c_ac_t1_t1_in*MM_in[0]<=c_ac_t1_t1*MM[0]
	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c_ac_t1_t1_mem0 <= c_ac_t1_t1

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_ac_t1_t1_mem1 <= c_ac_t1_t1

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=2, delay_cost=1)
	c_ac_t1_t2 += alt(MAS)
	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	c_ac_t1_t2_in += alt(MAS_in)
	S += c_ac_t1_t2_in*MAS_in[0]<=c_ac_t1_t2*MAS[0]

	S += c_ac_t1_t2_in*MAS_in[1]<=c_ac_t1_t2*MAS[1]

	S += c_ac_t1_t2_in*MAS_in[2]<=c_ac_t1_t2*MAS[2]

	S += c_ac_t1_t2_in*MAS_in[3]<=c_ac_t1_t2*MAS[3]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c_ac_t1_t2_mem0 <= c_ac_t1_t2

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c_ac_t1_t2_mem1 <= c_ac_t1_t2

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=2, delay_cost=1)
	c_ac_t1_t3 += alt(MAS)
	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	c_ac_t1_t3_in += alt(MAS_in)
	S += c_ac_t1_t3_in*MAS_in[0]<=c_ac_t1_t3*MAS[0]

	S += c_ac_t1_t3_in*MAS_in[1]<=c_ac_t1_t3*MAS[1]

	S += c_ac_t1_t3_in*MAS_in[2]<=c_ac_t1_t3*MAS[2]

	S += c_ac_t1_t3_in*MAS_in[3]<=c_ac_t1_t3*MAS[3]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_ac_t1_t3_mem0 <= c_ac_t1_t3

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_ac_t1_t3_mem1 <= c_ac_t1_t3

	c_ac_t20 = S.Task('c_ac_t20', length=2, delay_cost=1)
	c_ac_t20 += alt(MAS)
	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	c_ac_t20_in += alt(MAS_in)
	S += c_ac_t20_in*MAS_in[0]<=c_ac_t20*MAS[0]

	S += c_ac_t20_in*MAS_in[1]<=c_ac_t20*MAS[1]

	S += c_ac_t20_in*MAS_in[2]<=c_ac_t20*MAS[2]

	S += c_ac_t20_in*MAS_in[3]<=c_ac_t20*MAS[3]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	c_ac_t20_mem0 += MAIN_MEM_r[0]
	S += c_ac_t20_mem0 <= c_ac_t20

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	c_ac_t20_mem1 += MAIN_MEM_r[1]
	S += c_ac_t20_mem1 <= c_ac_t20

	c_ac_t21 = S.Task('c_ac_t21', length=2, delay_cost=1)
	c_ac_t21 += alt(MAS)
	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	c_ac_t21_in += alt(MAS_in)
	S += c_ac_t21_in*MAS_in[0]<=c_ac_t21*MAS[0]

	S += c_ac_t21_in*MAS_in[1]<=c_ac_t21*MAS[1]

	S += c_ac_t21_in*MAS_in[2]<=c_ac_t21*MAS[2]

	S += c_ac_t21_in*MAS_in[3]<=c_ac_t21*MAS[3]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	c_ac_t21_mem0 += MAIN_MEM_r[0]
	S += c_ac_t21_mem0 <= c_ac_t21

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	c_ac_t21_mem1 += MAIN_MEM_r[1]
	S += c_ac_t21_mem1 <= c_ac_t21

	c_ac_t30 = S.Task('c_ac_t30', length=2, delay_cost=1)
	c_ac_t30 += alt(MAS)
	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	c_ac_t30_in += alt(MAS_in)
	S += c_ac_t30_in*MAS_in[0]<=c_ac_t30*MAS[0]

	S += c_ac_t30_in*MAS_in[1]<=c_ac_t30*MAS[1]

	S += c_ac_t30_in*MAS_in[2]<=c_ac_t30*MAS[2]

	S += c_ac_t30_in*MAS_in[3]<=c_ac_t30*MAS[3]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	c_ac_t30_mem0 += MAIN_MEM_r[0]
	S += c_ac_t30_mem0 <= c_ac_t30

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	c_ac_t30_mem1 += MAIN_MEM_r[1]
	S += c_ac_t30_mem1 <= c_ac_t30

	c_ac_t31 = S.Task('c_ac_t31', length=2, delay_cost=1)
	c_ac_t31 += alt(MAS)
	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	c_ac_t31_in += alt(MAS_in)
	S += c_ac_t31_in*MAS_in[0]<=c_ac_t31*MAS[0]

	S += c_ac_t31_in*MAS_in[1]<=c_ac_t31*MAS[1]

	S += c_ac_t31_in*MAS_in[2]<=c_ac_t31*MAS[2]

	S += c_ac_t31_in*MAS_in[3]<=c_ac_t31*MAS[3]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	c_ac_t31_mem0 += MAIN_MEM_r[0]
	S += c_ac_t31_mem0 <= c_ac_t31

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	c_ac_t31_mem1 += MAIN_MEM_r[1]
	S += c_ac_t31_mem1 <= c_ac_t31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage2MAS4/FP12_INV_BEFORE_FPINV/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

