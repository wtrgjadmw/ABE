from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 274
	S = Scenario("schedule6", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=11)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=1, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 0
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 0
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 0
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 1
	c_cc_a1_0_in += MAS_in[0]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 1
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 1
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=11, delay_cost=1)
	S += c_cc_t3_t1 >= 1
	c_cc_t3_t1 += MM[0]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 2
	c_bb_t11_in += MAS_in[0]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 2
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 2
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=3, delay_cost=1)
	S += c_cc_a1_0 >= 2
	c_cc_a1_0 += MAS[0]

	c_bb_t11 = S.Task('c_bb_t11', length=3, delay_cost=1)
	S += c_bb_t11 >= 3
	c_bb_t11 += MAS[0]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 3
	c_bb_t3_t3_in += MAS_in[0]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 3
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 3
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 4
	c_bb_a1_1_in += MAS_in[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 4
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 4
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=3, delay_cost=1)
	S += c_bb_t3_t3 >= 4
	c_bb_t3_t3 += MAS[0]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=3, delay_cost=1)
	S += c_bb_a1_1 >= 5
	c_bb_a1_1 += MAS[0]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 5
	c_cc_t11_in += MAS_in[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 5
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 5
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 6
	c_aa_t3_t0_in += MM_in[0]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 6
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 6
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=3, delay_cost=1)
	S += c_cc_t11 >= 6
	c_cc_t11 += MAS[0]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 7
	c_aa_t11_in += MAS_in[0]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 7
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 7
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=11, delay_cost=1)
	S += c_aa_t3_t0 >= 7
	c_aa_t3_t0 += MM[0]

	c_aa_t11 = S.Task('c_aa_t11', length=3, delay_cost=1)
	S += c_aa_t11 >= 8
	c_aa_t11 += MAS[0]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 8
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 8
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 8
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=11, delay_cost=1)
	S += c_ab_t1_t0 >= 9
	c_ab_t1_t0 += MM[0]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 9
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 9
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 9
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=11, delay_cost=1)
	S += c_cc_t3_t0 >= 10
	c_cc_t3_t0 += MM[0]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 10
	c_cc_t3_t3_in += MAS_in[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 10
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 10
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 11
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 11
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 11
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=3, delay_cost=1)
	S += c_cc_t3_t3 >= 11
	c_cc_t3_t3 += MAS[0]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 12
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 12
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 12
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=11, delay_cost=1)
	S += c_ab_t0_t1 >= 12
	c_ab_t0_t1 += MM[0]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=11, delay_cost=1)
	S += c_ab_t0_t0 >= 13
	c_ab_t0_t0 += MM[0]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 13
	c_cc_t10_in += MAS_in[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 13
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 13
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 14
	c_cc_a1_1_in += MAS_in[0]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 14
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 14
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=3, delay_cost=1)
	S += c_cc_t10 >= 14
	c_cc_t10 += MAS[0]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 15
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 15
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 15
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=3, delay_cost=1)
	S += c_cc_a1_1 >= 15
	c_cc_a1_1 += MAS[0]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 16
	c_bb_a1_0_in += MAS_in[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 16
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 16
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=11, delay_cost=1)
	S += c_bb_t3_t0 >= 16
	c_bb_t3_t0 += MM[0]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 17
	c_aa_t3_t3_in += MAS_in[0]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 17
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 17
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=3, delay_cost=1)
	S += c_bb_a1_0 >= 17
	c_bb_a1_0 += MAS[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=3, delay_cost=1)
	S += c_aa_t3_t3 >= 18
	c_aa_t3_t3 += MAS[0]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 18
	c_cc_t3_t2_in += MAS_in[0]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 18
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 18
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 19
	c_bb_t10_in += MAS_in[0]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 19
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 19
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=3, delay_cost=1)
	S += c_cc_t3_t2 >= 19
	c_cc_t3_t2 += MAS[0]

	c_bb_t10 = S.Task('c_bb_t10', length=3, delay_cost=1)
	S += c_bb_t10 >= 20
	c_bb_t10 += MAS[0]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 20
	c_bb_t3_t2_in += MAS_in[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 20
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 20
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 21
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 21
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 21
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=3, delay_cost=1)
	S += c_bb_t3_t2 >= 21
	c_bb_t3_t2 += MAS[0]

	c_cc_t2_t3_in = S.Task('c_cc_t2_t3_in', length=1, delay_cost=1)
	S += c_cc_t2_t3_in >= 21
	c_cc_t2_t3_in += MAS_in[0]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 21
	c_cc_t2_t3_mem0 += MAS_MEM[0]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 21
	c_cc_t2_t3_mem1 += MAS_MEM[1]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 22
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 22
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 22
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=11, delay_cost=1)
	S += c_bb_t3_t1 >= 22
	c_bb_t3_t1 += MM[0]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=3, delay_cost=1)
	S += c_cc_t2_t3 >= 22
	c_cc_t2_t3 += MAS[0]

	c_cc_t3_t5_in = S.Task('c_cc_t3_t5_in', length=1, delay_cost=1)
	S += c_cc_t3_t5_in >= 22
	c_cc_t3_t5_in += MAS_in[0]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 22
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 22
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 23
	c_ab_t0_t2_in += MAS_in[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 23
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 23
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=11, delay_cost=1)
	S += c_ab_t1_t1 >= 23
	c_ab_t1_t1 += MM[0]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 23
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 23
	c_bb_t3_t4_mem0 += MAS_MEM[0]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 23
	c_bb_t3_t4_mem1 += MAS_MEM[1]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=3, delay_cost=1)
	S += c_cc_t3_t5 >= 23
	c_cc_t3_t5 += MAS[0]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=3, delay_cost=1)
	S += c_ab_t0_t2 >= 24
	c_ab_t0_t2 += MAS[0]

	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 24
	c_ab_t0_t3_in += MAS_in[0]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 24
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 24
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=11, delay_cost=1)
	S += c_bb_t3_t4 >= 24
	c_bb_t3_t4 += MM[0]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 24
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 24
	c_cc_t3_t4_mem0 += MAS_MEM[0]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 24
	c_cc_t3_t4_mem1 += MAS_MEM[1]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 25
	c_aa_t3_t2_in += MAS_in[0]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 25
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 25
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=3, delay_cost=1)
	S += c_ab_t0_t3 >= 25
	c_ab_t0_t3 += MAS[0]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=11, delay_cost=1)
	S += c_cc_t3_t4 >= 25
	c_cc_t3_t4 += MM[0]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 26
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 26
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 26
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=3, delay_cost=1)
	S += c_aa_t3_t2 >= 26
	c_aa_t3_t2 += MAS[0]

	c_cc_t30_in = S.Task('c_cc_t30_in', length=1, delay_cost=1)
	S += c_cc_t30_in >= 26
	c_cc_t30_in += MAS_in[0]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 26
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 26
	c_cc_t30_mem1 += MM_MEM[1]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 27
	c_aa_t10_in += MAS_in[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 27
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 27
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=11, delay_cost=1)
	S += c_aa_t3_t1 >= 27
	c_aa_t3_t1 += MM[0]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 27
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 27
	c_ab_t0_t4_mem0 += MAS_MEM[0]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 27
	c_ab_t0_t4_mem1 += MAS_MEM[1]

	c_cc_t30 = S.Task('c_cc_t30', length=3, delay_cost=1)
	S += c_cc_t30 >= 27
	c_cc_t30 += MAS[0]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 28
	c_aa_a1_1_in += MAS_in[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 28
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 28
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t10 = S.Task('c_aa_t10', length=3, delay_cost=1)
	S += c_aa_t10 >= 28
	c_aa_t10 += MAS[0]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 28
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 28
	c_aa_t3_t4_mem0 += MAS_MEM[0]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 28
	c_aa_t3_t4_mem1 += MAS_MEM[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=11, delay_cost=1)
	S += c_ab_t0_t4 >= 28
	c_ab_t0_t4 += MM[0]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 29
	c_aa_a1_0_in += MAS_in[0]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 29
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 29
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=3, delay_cost=1)
	S += c_aa_a1_1 >= 29
	c_aa_a1_1 += MAS[0]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=11, delay_cost=1)
	S += c_aa_t3_t4 >= 29
	c_aa_t3_t4 += MM[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=3, delay_cost=1)
	S += c_aa_a1_0 >= 30
	c_aa_a1_0 += MAS[0]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 30
	c_bc_t20_in += MAS_in[0]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 30
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 30
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 31
	c_ab_t31_in += MAS_in[0]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 31
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 31
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t20 = S.Task('c_bc_t20', length=3, delay_cost=1)
	S += c_bc_t20 >= 31
	c_bc_t20 += MAS[0]

	c_ab_t31 = S.Task('c_ab_t31', length=3, delay_cost=1)
	S += c_ab_t31 >= 32
	c_ab_t31 += MAS[0]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 32
	c_ac_t31_in += MAS_in[0]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 32
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 32
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t31 = S.Task('c_ac_t31', length=3, delay_cost=1)
	S += c_ac_t31 >= 33
	c_ac_t31 += MAS[0]

	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	S += c_bc_t1_t2_in >= 33
	c_bc_t1_t2_in += MAS_in[0]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 33
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 33
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=3, delay_cost=1)
	S += c_bc_t1_t2 >= 34
	c_bc_t1_t2 += MAS[0]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 34
	c_bc_t31_in += MAS_in[0]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 34
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 34
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 35
	c_bc_t0_t3_in += MAS_in[0]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 35
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 35
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t31 = S.Task('c_bc_t31', length=3, delay_cost=1)
	S += c_bc_t31 >= 35
	c_bc_t31 += MAS[0]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 36
	c_ac_t30_in += MAS_in[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 36
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 36
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=3, delay_cost=1)
	S += c_bc_t0_t3 >= 36
	c_bc_t0_t3 += MAS[0]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 37
	c_ac_t20_in += MAS_in[0]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 37
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 37
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t30 = S.Task('c_ac_t30', length=3, delay_cost=1)
	S += c_ac_t30 >= 37
	c_ac_t30 += MAS[0]

	c_ac_t20 = S.Task('c_ac_t20', length=3, delay_cost=1)
	S += c_ac_t20 >= 38
	c_ac_t20 += MAS[0]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 38
	c_bc_t0_t2_in += MAS_in[0]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 38
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 38
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 39
	c_ac_t1_t3_in += MAS_in[0]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 39
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 39
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=3, delay_cost=1)
	S += c_bc_t0_t2 >= 39
	c_bc_t0_t2 += MAS[0]

	c_aa_t3_t5_in = S.Task('c_aa_t3_t5_in', length=1, delay_cost=1)
	S += c_aa_t3_t5_in >= 40
	c_aa_t3_t5_in += MAS_in[0]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 40
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 40
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=3, delay_cost=1)
	S += c_ac_t1_t3 >= 40
	c_ac_t1_t3 += MAS[0]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 40
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 40
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 40
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=3, delay_cost=1)
	S += c_aa_t3_t5 >= 41
	c_aa_t3_t5 += MAS[0]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 41
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 41
	c_ac_t4_t0_mem0 += MAS_MEM[0]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 41
	c_ac_t4_t0_mem1 += MAS_MEM[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=11, delay_cost=1)
	S += c_bc_t1_t0 >= 41
	c_bc_t1_t0 += MM[0]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 41
	c_bc_t30_in += MAS_in[0]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 41
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 41
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 42
	c_ac_t0_t3_in += MAS_in[0]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 42
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 42
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=11, delay_cost=1)
	S += c_ac_t4_t0 >= 42
	c_ac_t4_t0 += MM[0]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 42
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 42
	c_bc_t0_t4_mem0 += MAS_MEM[0]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 42
	c_bc_t0_t4_mem1 += MAS_MEM[1]

	c_bc_t30 = S.Task('c_bc_t30', length=3, delay_cost=1)
	S += c_bc_t30 >= 42
	c_bc_t30 += MAS[0]

	c_ab_t00_in = S.Task('c_ab_t00_in', length=1, delay_cost=1)
	S += c_ab_t00_in >= 43
	c_ab_t00_in += MAS_in[0]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 43
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 43
	c_ab_t00_mem1 += MM_MEM[1]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=3, delay_cost=1)
	S += c_ac_t0_t3 >= 43
	c_ac_t0_t3 += MAS[0]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=11, delay_cost=1)
	S += c_bc_t0_t4 >= 43
	c_bc_t0_t4 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 43
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 43
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 43
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t00 = S.Task('c_ab_t00', length=3, delay_cost=1)
	S += c_ab_t00 >= 44
	c_ab_t00 += MAS[0]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 44
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 44
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 44
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t3_in = S.Task('c_bb_t2_t3_in', length=1, delay_cost=1)
	S += c_bb_t2_t3_in >= 44
	c_bb_t2_t3_in += MAS_in[0]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 44
	c_bb_t2_t3_mem0 += MAS_MEM[0]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 44
	c_bb_t2_t3_mem1 += MAS_MEM[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=11, delay_cost=1)
	S += c_bc_t1_t1 >= 44
	c_bc_t1_t1 += MM[0]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=11, delay_cost=1)
	S += c_ac_t0_t1 >= 45
	c_ac_t0_t1 += MM[0]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 45
	c_ac_t1_t2_in += MAS_in[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 45
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 45
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=3, delay_cost=1)
	S += c_bb_t2_t3 >= 45
	c_bb_t2_t3 += MAS[0]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 45
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 45
	c_bc_t4_t0_mem0 += MAS_MEM[0]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 45
	c_bc_t4_t0_mem1 += MAS_MEM[1]

	c_aa_t30_in = S.Task('c_aa_t30_in', length=1, delay_cost=1)
	S += c_aa_t30_in >= 46
	c_aa_t30_in += MAS_in[0]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 46
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 46
	c_aa_t30_mem1 += MM_MEM[1]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 46
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 46
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 46
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=3, delay_cost=1)
	S += c_ac_t1_t2 >= 46
	c_ac_t1_t2 += MAS[0]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=11, delay_cost=1)
	S += c_bc_t4_t0 >= 46
	c_bc_t4_t0 += MM[0]

	c_aa_t30 = S.Task('c_aa_t30', length=3, delay_cost=1)
	S += c_aa_t30 >= 47
	c_aa_t30 += MAS[0]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=11, delay_cost=1)
	S += c_ac_t0_t0 >= 47
	c_ac_t0_t0 += MM[0]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 47
	c_ac_t0_t2_in += MAS_in[0]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 47
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 47
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 48
	c_ab_t30_in += MAS_in[0]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 48
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 48
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=3, delay_cost=1)
	S += c_ac_t0_t2 >= 48
	c_ac_t0_t2 += MAS[0]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 48
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 48
	c_ac_t1_t4_mem0 += MAS_MEM[0]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 48
	c_ac_t1_t4_mem1 += MAS_MEM[1]

	c_ab_t30 = S.Task('c_ab_t30', length=3, delay_cost=1)
	S += c_ab_t30 >= 49
	c_ab_t30 += MAS[0]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 49
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 49
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 49
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=11, delay_cost=1)
	S += c_ac_t1_t4 >= 49
	c_ac_t1_t4 += MM[0]

	c_bb_t30_in = S.Task('c_bb_t30_in', length=1, delay_cost=1)
	S += c_bb_t30_in >= 49
	c_bb_t30_in += MAS_in[0]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 49
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 49
	c_bb_t30_mem1 += MM_MEM[1]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 50
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 50
	c_ac_t0_t4_mem0 += MAS_MEM[0]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 50
	c_ac_t0_t4_mem1 += MAS_MEM[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=11, delay_cost=1)
	S += c_ac_t1_t1 >= 50
	c_ac_t1_t1 += MM[0]

	c_bb_t30 = S.Task('c_bb_t30', length=3, delay_cost=1)
	S += c_bb_t30 >= 50
	c_bb_t30 += MAS[0]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 50
	c_bc_t1_t3_in += MAS_in[0]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 50
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 50
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t5_in = S.Task('c_ab_t1_t5_in', length=1, delay_cost=1)
	S += c_ab_t1_t5_in >= 51
	c_ab_t1_t5_in += MAS_in[0]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 51
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 51
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=11, delay_cost=1)
	S += c_ac_t0_t4 >= 51
	c_ac_t0_t4 += MM[0]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 51
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 51
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 51
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=3, delay_cost=1)
	S += c_bc_t1_t3 >= 51
	c_bc_t1_t3 += MAS[0]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=3, delay_cost=1)
	S += c_ab_t1_t5 >= 52
	c_ab_t1_t5 += MAS[0]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 52
	c_ab_t21_in += MAS_in[0]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 52
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 52
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=11, delay_cost=1)
	S += c_bc_t0_t0 >= 52
	c_bc_t0_t0 += MM[0]

	c_ab_t21 = S.Task('c_ab_t21', length=3, delay_cost=1)
	S += c_ab_t21 >= 53
	c_ab_t21 += MAS[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 53
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 53
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 53
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t3_in = S.Task('c_bc_t4_t3_in', length=1, delay_cost=1)
	S += c_bc_t4_t3_in >= 53
	c_bc_t4_t3_in += MAS_in[0]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 53
	c_bc_t4_t3_mem0 += MAS_MEM[0]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 53
	c_bc_t4_t3_mem1 += MAS_MEM[1]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 54
	c_ac_t21_in += MAS_in[0]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 54
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 54
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=11, delay_cost=1)
	S += c_bc_t0_t1 >= 54
	c_bc_t0_t1 += MM[0]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 54
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 54
	c_bc_t1_t4_mem0 += MAS_MEM[0]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 54
	c_bc_t1_t4_mem1 += MAS_MEM[1]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=3, delay_cost=1)
	S += c_bc_t4_t3 >= 54
	c_bc_t4_t3 += MAS[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 55
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 55
	c_ab_t4_t1_mem0 += MAS_MEM[0]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 55
	c_ab_t4_t1_mem1 += MAS_MEM[1]

	c_ac_t21 = S.Task('c_ac_t21', length=3, delay_cost=1)
	S += c_ac_t21 >= 55
	c_ac_t21 += MAS[0]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=11, delay_cost=1)
	S += c_bc_t1_t4 >= 55
	c_bc_t1_t4 += MM[0]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 55
	c_bc_t21_in += MAS_in[0]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 55
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 55
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=11, delay_cost=1)
	S += c_ab_t4_t1 >= 56
	c_ab_t4_t1 += MM[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 56
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 56
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 56
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t5_in = S.Task('c_bc_t1_t5_in', length=1, delay_cost=1)
	S += c_bc_t1_t5_in >= 56
	c_bc_t1_t5_in += MAS_in[0]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 56
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 56
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_bc_t21 = S.Task('c_bc_t21', length=3, delay_cost=1)
	S += c_bc_t21 >= 56
	c_bc_t21 += MAS[0]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 57
	c_ab_t20_in += MAS_in[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 57
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 57
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=11, delay_cost=1)
	S += c_ac_t1_t0 >= 57
	c_ac_t1_t0 += MM[0]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 57
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 57
	c_ac_t4_t1_mem0 += MAS_MEM[0]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 57
	c_ac_t4_t1_mem1 += MAS_MEM[1]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=3, delay_cost=1)
	S += c_bc_t1_t5 >= 57
	c_bc_t1_t5 += MAS[0]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 58
	c_ab_t1_t3_in += MAS_in[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 58
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 58
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t20 = S.Task('c_ab_t20', length=3, delay_cost=1)
	S += c_ab_t20 >= 58
	c_ab_t20 += MAS[0]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=11, delay_cost=1)
	S += c_ac_t4_t1 >= 58
	c_ac_t4_t1 += MM[0]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 58
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 58
	c_bc_t4_t1_mem0 += MAS_MEM[0]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 58
	c_bc_t4_t1_mem1 += MAS_MEM[1]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 59
	c_ab_t1_t2_in += MAS_in[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 59
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 59
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=3, delay_cost=1)
	S += c_ab_t1_t3 >= 59
	c_ab_t1_t3 += MAS[0]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=11, delay_cost=1)
	S += c_bc_t4_t1 >= 59
	c_bc_t4_t1 += MM[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=3, delay_cost=1)
	S += c_ab_t1_t2 >= 60
	c_ab_t1_t2 += MAS[0]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 60
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 60
	c_ab_t4_t0_mem0 += MAS_MEM[0]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 60
	c_ab_t4_t0_mem1 += MAS_MEM[1]

	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	S += c_pbc_t30_in >= 60
	c_pbc_t30_in += MAS_in[0]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 60
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 60
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=11, delay_cost=1)
	S += c_ab_t4_t0 >= 61
	c_ab_t4_t0 += MM[0]

	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	S += c_pbc_t1_t3_in >= 61
	c_pbc_t1_t3_in += MAS_in[0]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 61
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 61
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t30 = S.Task('c_pbc_t30', length=3, delay_cost=1)
	S += c_pbc_t30 >= 61
	c_pbc_t30 += MAS[0]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 62
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 62
	c_ab_t1_t4_mem0 += MAS_MEM[0]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 62
	c_ab_t1_t4_mem1 += MAS_MEM[1]

	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	S += c_paa_t30_in >= 62
	c_paa_t30_in += MAS_in[0]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 62
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 62
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=3, delay_cost=1)
	S += c_pbc_t1_t3 >= 62
	c_pbc_t1_t3 += MAS[0]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=11, delay_cost=1)
	S += c_ab_t1_t4 >= 63
	c_ab_t1_t4 += MM[0]

	c_paa_t30 = S.Task('c_paa_t30', length=3, delay_cost=1)
	S += c_paa_t30 >= 63
	c_paa_t30 += MAS[0]

	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	S += c_pcb_t30_in >= 63
	c_pcb_t30_in += MAS_in[0]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 63
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 63
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_pcb_t30 = S.Task('c_pcb_t30', length=3, delay_cost=1)
	S += c_pcb_t30 >= 64
	c_pcb_t30 += MAS[0]

	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	S += c_pcb_t31_in >= 64
	c_pcb_t31_in += MAS_in[0]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 64
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 64
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	S += c_pbc_t0_t3_in >= 65
	c_pbc_t0_t3_in += MAS_in[0]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 65
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 65
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t31 = S.Task('c_pcb_t31', length=3, delay_cost=1)
	S += c_pcb_t31 >= 65
	c_pcb_t31 += MAS[0]

	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	S += c_paa_t1_t3_in >= 66
	c_paa_t1_t3_in += MAS_in[0]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 66
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 66
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=3, delay_cost=1)
	S += c_pbc_t0_t3 >= 66
	c_pbc_t0_t3 += MAS[0]

	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	S += c_paa_t0_t3_in >= 67
	c_paa_t0_t3_in += MAS_in[0]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 67
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 67
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=3, delay_cost=1)
	S += c_paa_t1_t3 >= 67
	c_paa_t1_t3 += MAS[0]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=3, delay_cost=1)
	S += c_paa_t0_t3 >= 68
	c_paa_t0_t3 += MAS[0]

	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	S += c_pbc_t31_in >= 68
	c_pbc_t31_in += MAS_in[0]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 68
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 68
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_pbc_t31 = S.Task('c_pbc_t31', length=3, delay_cost=1)
	S += c_pbc_t31 >= 69
	c_pbc_t31 += MAS[0]

	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	S += c_pcb_t0_t3_in >= 69
	c_pcb_t0_t3_in += MAS_in[0]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 69
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 69
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	S += c_paa_t31_in >= 70
	c_paa_t31_in += MAS_in[0]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 70
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 70
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=3, delay_cost=1)
	S += c_pcb_t0_t3 >= 70
	c_pcb_t0_t3 += MAS[0]

	c_paa_t31 = S.Task('c_paa_t31', length=3, delay_cost=1)
	S += c_paa_t31 >= 71
	c_paa_t31 += MAS[0]

	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	S += c_pcb_t1_t3_in >= 71
	c_pcb_t1_t3_in += MAS_in[0]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 71
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 71
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t00_in = S.Task('c_cc_t00_in', length=1, delay_cost=1)
	S += c_cc_t00_in >= 72
	c_cc_t00_in += MAS_in[0]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 72
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 72
	c_cc_t00_mem1 += MAS_MEM[1]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=3, delay_cost=1)
	S += c_pcb_t1_t3 >= 72
	c_pcb_t1_t3 += MAS[0]

	c_cc_t00 = S.Task('c_cc_t00', length=3, delay_cost=1)
	S += c_cc_t00 >= 73
	c_cc_t00 += MAS[0]

	c_pbc_t4_t3_in = S.Task('c_pbc_t4_t3_in', length=1, delay_cost=1)
	S += c_pbc_t4_t3_in >= 73
	c_pbc_t4_t3_in += MAS_in[0]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 73
	c_pbc_t4_t3_mem0 += MAS_MEM[0]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 73
	c_pbc_t4_t3_mem1 += MAS_MEM[1]

	c_bc_t4_t2_in = S.Task('c_bc_t4_t2_in', length=1, delay_cost=1)
	S += c_bc_t4_t2_in >= 74
	c_bc_t4_t2_in += MAS_in[0]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 74
	c_bc_t4_t2_mem0 += MAS_MEM[0]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 74
	c_bc_t4_t2_mem1 += MAS_MEM[1]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=3, delay_cost=1)
	S += c_pbc_t4_t3 >= 74
	c_pbc_t4_t3 += MAS[0]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=3, delay_cost=1)
	S += c_bc_t4_t2 >= 75
	c_bc_t4_t2 += MAS[0]

	c_cc_t01_in = S.Task('c_cc_t01_in', length=1, delay_cost=1)
	S += c_cc_t01_in >= 75
	c_cc_t01_in += MAS_in[0]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 75
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 75
	c_cc_t01_mem1 += MAS_MEM[1]

	c_ac_t4_t3_in = S.Task('c_ac_t4_t3_in', length=1, delay_cost=1)
	S += c_ac_t4_t3_in >= 76
	c_ac_t4_t3_in += MAS_in[0]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 76
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 76
	c_ac_t4_t3_mem1 += MAS_MEM[1]

	c_cc_t01 = S.Task('c_cc_t01', length=3, delay_cost=1)
	S += c_cc_t01 >= 76
	c_cc_t01 += MAS[0]

	c_ac_t0_t5_in = S.Task('c_ac_t0_t5_in', length=1, delay_cost=1)
	S += c_ac_t0_t5_in >= 77
	c_ac_t0_t5_in += MAS_in[0]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 77
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 77
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=3, delay_cost=1)
	S += c_ac_t4_t3 >= 77
	c_ac_t4_t3 += MAS[0]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 77
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 77
	c_bc_t4_t4_mem0 += MAS_MEM[0]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 77
	c_bc_t4_t4_mem1 += MAS_MEM[1]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=3, delay_cost=1)
	S += c_ac_t0_t5 >= 78
	c_ac_t0_t5 += MAS[0]

	c_bc_t00_in = S.Task('c_bc_t00_in', length=1, delay_cost=1)
	S += c_bc_t00_in >= 78
	c_bc_t00_in += MAS_in[0]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 78
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 78
	c_bc_t00_mem1 += MM_MEM[1]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=11, delay_cost=1)
	S += c_bc_t4_t4 >= 78
	c_bc_t4_t4 += MM[0]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 78
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 78
	c_cc_t2_t1_mem0 += MAS_MEM[0]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 78
	c_cc_t2_t1_mem1 += MAS_MEM[1]

	c_aa_t01_in = S.Task('c_aa_t01_in', length=1, delay_cost=1)
	S += c_aa_t01_in >= 79
	c_aa_t01_in += MAS_in[0]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 79
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 79
	c_aa_t01_mem1 += MAS_MEM[1]

	c_bc_t00 = S.Task('c_bc_t00', length=3, delay_cost=1)
	S += c_bc_t00 >= 79
	c_bc_t00 += MAS[0]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=11, delay_cost=1)
	S += c_cc_t2_t1 >= 79
	c_cc_t2_t1 += MM[0]

	c_aa_t01 = S.Task('c_aa_t01', length=3, delay_cost=1)
	S += c_aa_t01 >= 80
	c_aa_t01 += MAS[0]

	c_ac_t4_t2_in = S.Task('c_ac_t4_t2_in', length=1, delay_cost=1)
	S += c_ac_t4_t2_in >= 80
	c_ac_t4_t2_in += MAS_in[0]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 80
	c_ac_t4_t2_mem0 += MAS_MEM[0]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 80
	c_ac_t4_t2_mem1 += MAS_MEM[1]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=3, delay_cost=1)
	S += c_ac_t4_t2 >= 81
	c_ac_t4_t2 += MAS[0]

	c_bc_t10_in = S.Task('c_bc_t10_in', length=1, delay_cost=1)
	S += c_bc_t10_in >= 81
	c_bc_t10_in += MAS_in[0]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 81
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 81
	c_bc_t10_mem1 += MM_MEM[1]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 81
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 81
	c_cc_t2_t0_mem0 += MAS_MEM[0]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 81
	c_cc_t2_t0_mem1 += MAS_MEM[1]

	c_aa_t00_in = S.Task('c_aa_t00_in', length=1, delay_cost=1)
	S += c_aa_t00_in >= 82
	c_aa_t00_in += MAS_in[0]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 82
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 82
	c_aa_t00_mem1 += MAS_MEM[1]

	c_bc_t10 = S.Task('c_bc_t10', length=3, delay_cost=1)
	S += c_bc_t10 >= 82
	c_bc_t10 += MAS[0]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=11, delay_cost=1)
	S += c_cc_t2_t0 >= 82
	c_cc_t2_t0 += MM[0]

	c_aa_t00 = S.Task('c_aa_t00', length=3, delay_cost=1)
	S += c_aa_t00 >= 83
	c_aa_t00 += MAS[0]

	c_ab_t4_t2_in = S.Task('c_ab_t4_t2_in', length=1, delay_cost=1)
	S += c_ab_t4_t2_in >= 83
	c_ab_t4_t2_in += MAS_in[0]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 83
	c_ab_t4_t2_mem0 += MAS_MEM[0]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 83
	c_ab_t4_t2_mem1 += MAS_MEM[1]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=3, delay_cost=1)
	S += c_ab_t4_t2 >= 84
	c_ab_t4_t2 += MAS[0]

	c_ab_t4_t3_in = S.Task('c_ab_t4_t3_in', length=1, delay_cost=1)
	S += c_ab_t4_t3_in >= 84
	c_ab_t4_t3_in += MAS_in[0]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 84
	c_ab_t4_t3_mem0 += MAS_MEM[0]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 84
	c_ab_t4_t3_mem1 += MAS_MEM[1]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 85
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 85
	c_aa_t2_t0_mem0 += MAS_MEM[0]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 85
	c_aa_t2_t0_mem1 += MAS_MEM[1]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=3, delay_cost=1)
	S += c_ab_t4_t3 >= 85
	c_ab_t4_t3 += MAS[0]

	c_ac_t00_in = S.Task('c_ac_t00_in', length=1, delay_cost=1)
	S += c_ac_t00_in >= 85
	c_ac_t00_in += MAS_in[0]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 85
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 85
	c_ac_t00_mem1 += MM_MEM[1]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=11, delay_cost=1)
	S += c_aa_t2_t0 >= 86
	c_aa_t2_t0 += MM[0]

	c_ac_t00 = S.Task('c_ac_t00', length=3, delay_cost=1)
	S += c_ac_t00 >= 86
	c_ac_t00 += MAS[0]

	c_bb_t01_in = S.Task('c_bb_t01_in', length=1, delay_cost=1)
	S += c_bb_t01_in >= 86
	c_bb_t01_in += MAS_in[0]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 86
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 86
	c_bb_t01_mem1 += MAS_MEM[1]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 87
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 87
	c_aa_t2_t1_mem0 += MAS_MEM[0]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 87
	c_aa_t2_t1_mem1 += MAS_MEM[1]

	c_bb_t01 = S.Task('c_bb_t01', length=3, delay_cost=1)
	S += c_bb_t01 >= 87
	c_bb_t01 += MAS[0]

	c_bb_t3_t5_in = S.Task('c_bb_t3_t5_in', length=1, delay_cost=1)
	S += c_bb_t3_t5_in >= 87
	c_bb_t3_t5_in += MAS_in[0]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 87
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 87
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=11, delay_cost=1)
	S += c_aa_t2_t1 >= 88
	c_aa_t2_t1 += MM[0]

	c_aa_t2_t3_in = S.Task('c_aa_t2_t3_in', length=1, delay_cost=1)
	S += c_aa_t2_t3_in >= 88
	c_aa_t2_t3_in += MAS_in[0]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 88
	c_aa_t2_t3_mem0 += MAS_MEM[0]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 88
	c_aa_t2_t3_mem1 += MAS_MEM[1]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=3, delay_cost=1)
	S += c_bb_t3_t5 >= 88
	c_bb_t3_t5 += MAS[0]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=3, delay_cost=1)
	S += c_aa_t2_t3 >= 89
	c_aa_t2_t3 += MAS[0]

	c_ab_t10_in = S.Task('c_ab_t10_in', length=1, delay_cost=1)
	S += c_ab_t10_in >= 89
	c_ab_t10_in += MAS_in[0]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 89
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 89
	c_ab_t10_mem1 += MM_MEM[1]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 89
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 89
	c_bb_t2_t1_mem0 += MAS_MEM[0]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 89
	c_bb_t2_t1_mem1 += MAS_MEM[1]

	c_ab_t10 = S.Task('c_ab_t10', length=3, delay_cost=1)
	S += c_ab_t10 >= 90
	c_ab_t10 += MAS[0]

	c_ac_t1_t5_in = S.Task('c_ac_t1_t5_in', length=1, delay_cost=1)
	S += c_ac_t1_t5_in >= 90
	c_ac_t1_t5_in += MAS_in[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 90
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 90
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 90
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 90
	c_ac_t4_t4_mem0 += MAS_MEM[0]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 90
	c_ac_t4_t4_mem1 += MAS_MEM[1]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=11, delay_cost=1)
	S += c_bb_t2_t1 >= 90
	c_bb_t2_t1 += MM[0]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=3, delay_cost=1)
	S += c_ac_t1_t5 >= 91
	c_ac_t1_t5 += MAS[0]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=11, delay_cost=1)
	S += c_ac_t4_t4 >= 91
	c_ac_t4_t4 += MM[0]

	c_pcb_t4_t3_in = S.Task('c_pcb_t4_t3_in', length=1, delay_cost=1)
	S += c_pcb_t4_t3_in >= 91
	c_pcb_t4_t3_in += MAS_in[0]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 91
	c_pcb_t4_t3_mem0 += MAS_MEM[0]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 91
	c_pcb_t4_t3_mem1 += MAS_MEM[1]

	c_bb_t00_in = S.Task('c_bb_t00_in', length=1, delay_cost=1)
	S += c_bb_t00_in >= 92
	c_bb_t00_in += MAS_in[0]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 92
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 92
	c_bb_t00_mem1 += MAS_MEM[1]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=3, delay_cost=1)
	S += c_pcb_t4_t3 >= 92
	c_pcb_t4_t3 += MAS[0]

	c_ab_t0_t5_in = S.Task('c_ab_t0_t5_in', length=1, delay_cost=1)
	S += c_ab_t0_t5_in >= 93
	c_ab_t0_t5_in += MAS_in[0]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 93
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 93
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 93
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 93
	c_ab_t4_t4_mem0 += MAS_MEM[0]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 93
	c_ab_t4_t4_mem1 += MAS_MEM[1]

	c_bb_t00 = S.Task('c_bb_t00', length=3, delay_cost=1)
	S += c_bb_t00 >= 93
	c_bb_t00 += MAS[0]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=3, delay_cost=1)
	S += c_ab_t0_t5 >= 94
	c_ab_t0_t5 += MAS[0]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=11, delay_cost=1)
	S += c_ab_t4_t4 >= 94
	c_ab_t4_t4 += MM[0]

	c_ac_t10_in = S.Task('c_ac_t10_in', length=1, delay_cost=1)
	S += c_ac_t10_in >= 94
	c_ac_t10_in += MAS_in[0]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 94
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 94
	c_ac_t10_mem1 += MM_MEM[1]

	c_ac_t10 = S.Task('c_ac_t10', length=3, delay_cost=1)
	S += c_ac_t10 >= 95
	c_ac_t10 += MAS[0]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 95
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 95
	c_bb_t2_t0_mem0 += MAS_MEM[0]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 95
	c_bb_t2_t0_mem1 += MAS_MEM[1]

	c_bc_t0_t5_in = S.Task('c_bc_t0_t5_in', length=1, delay_cost=1)
	S += c_bc_t0_t5_in >= 95
	c_bc_t0_t5_in += MAS_in[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 95
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 95
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=11, delay_cost=1)
	S += c_bb_t2_t0 >= 96
	c_bb_t2_t0 += MM[0]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=3, delay_cost=1)
	S += c_bc_t0_t5 >= 96
	c_bc_t0_t5 += MAS[0]

	c_bc_t40_in = S.Task('c_bc_t40_in', length=1, delay_cost=1)
	S += c_bc_t40_in >= 96
	c_bc_t40_in += MAS_in[0]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 96
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 96
	c_bc_t40_mem1 += MM_MEM[1]

	c_ac_t11_in = S.Task('c_ac_t11_in', length=1, delay_cost=1)
	S += c_ac_t11_in >= 97
	c_ac_t11_in += MAS_in[0]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 97
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 97
	c_ac_t11_mem1 += MAS_MEM[1]

	c_bc_t40 = S.Task('c_bc_t40', length=3, delay_cost=1)
	S += c_bc_t40 >= 97
	c_bc_t40 += MAS[0]

	c_aa_t31_in = S.Task('c_aa_t31_in', length=1, delay_cost=1)
	S += c_aa_t31_in >= 98
	c_aa_t31_in += MAS_in[0]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 98
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 98
	c_aa_t31_mem1 += MAS_MEM[1]

	c_ac_t11 = S.Task('c_ac_t11', length=3, delay_cost=1)
	S += c_ac_t11 >= 98
	c_ac_t11 += MAS[0]

	c_aa_t31 = S.Task('c_aa_t31', length=3, delay_cost=1)
	S += c_aa_t31 >= 99
	c_aa_t31 += MAS[0]

	c_cc_t31_in = S.Task('c_cc_t31_in', length=1, delay_cost=1)
	S += c_cc_t31_in >= 99
	c_cc_t31_in += MAS_in[0]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 99
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 99
	c_cc_t31_mem1 += MAS_MEM[1]

	c_bc_t01_in = S.Task('c_bc_t01_in', length=1, delay_cost=1)
	S += c_bc_t01_in >= 100
	c_bc_t01_in += MAS_in[0]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 100
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 100
	c_bc_t01_mem1 += MAS_MEM[1]

	c_cc_t31 = S.Task('c_cc_t31', length=3, delay_cost=1)
	S += c_cc_t31 >= 100
	c_cc_t31 += MAS[0]

	c_aa_t2_t2_in = S.Task('c_aa_t2_t2_in', length=1, delay_cost=1)
	S += c_aa_t2_t2_in >= 101
	c_aa_t2_t2_in += MAS_in[0]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 101
	c_aa_t2_t2_mem0 += MAS_MEM[0]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 101
	c_aa_t2_t2_mem1 += MAS_MEM[1]

	c_bc_t01 = S.Task('c_bc_t01', length=3, delay_cost=1)
	S += c_bc_t01 >= 101
	c_bc_t01 += MAS[0]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=3, delay_cost=1)
	S += c_aa_t2_t2 >= 102
	c_aa_t2_t2 += MAS[0]

	c_ab_t50_in = S.Task('c_ab_t50_in', length=1, delay_cost=1)
	S += c_ab_t50_in >= 102
	c_ab_t50_in += MAS_in[0]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 102
	c_ab_t50_mem0 += MAS_MEM[0]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 102
	c_ab_t50_mem1 += MAS_MEM[1]

	c_ab_t11_in = S.Task('c_ab_t11_in', length=1, delay_cost=1)
	S += c_ab_t11_in >= 103
	c_ab_t11_in += MAS_in[0]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 103
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 103
	c_ab_t11_mem1 += MAS_MEM[1]

	c_ab_t50 = S.Task('c_ab_t50', length=3, delay_cost=1)
	S += c_ab_t50 >= 103
	c_ab_t50 += MAS[0]

	c_ab_t11 = S.Task('c_ab_t11', length=3, delay_cost=1)
	S += c_ab_t11 >= 104
	c_ab_t11 += MAS[0]

	c_bb10_in = S.Task('c_bb10_in', length=1, delay_cost=1)
	S += c_bb10_in >= 104
	c_bb10_in += MAS_in[0]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 104
	c_bb10_mem0 += MAS_MEM[0]

	c_bb10_mem1 = S.Task('c_bb10_mem1', length=1, delay_cost=1)
	S += c_bb10_mem1 >= 104
	c_bb10_mem1 += MAS_MEM[1]

	c_bb10 = S.Task('c_bb10', length=3, delay_cost=1)
	S += c_bb10 >= 105
	c_bb10 += MAS[0]

	c_bc_t11_in = S.Task('c_bc_t11_in', length=1, delay_cost=1)
	S += c_bc_t11_in >= 105
	c_bc_t11_in += MAS_in[0]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 105
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 105
	c_bc_t11_mem1 += MAS_MEM[1]

	c_ac_t50_in = S.Task('c_ac_t50_in', length=1, delay_cost=1)
	S += c_ac_t50_in >= 106
	c_ac_t50_in += MAS_in[0]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 106
	c_ac_t50_mem0 += MAS_MEM[0]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 106
	c_ac_t50_mem1 += MAS_MEM[1]

	c_bc_t11 = S.Task('c_bc_t11', length=3, delay_cost=1)
	S += c_bc_t11 >= 106
	c_bc_t11 += MAS[0]

	c_ab_t01_in = S.Task('c_ab_t01_in', length=1, delay_cost=1)
	S += c_ab_t01_in >= 107
	c_ab_t01_in += MAS_in[0]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 107
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 107
	c_ab_t01_mem1 += MAS_MEM[1]

	c_ac_t50 = S.Task('c_ac_t50', length=3, delay_cost=1)
	S += c_ac_t50 >= 107
	c_ac_t50 += MAS[0]

	c_ab_t01 = S.Task('c_ab_t01', length=3, delay_cost=1)
	S += c_ab_t01 >= 108
	c_ab_t01 += MAS[0]

	c_paa_t4_t3_in = S.Task('c_paa_t4_t3_in', length=1, delay_cost=1)
	S += c_paa_t4_t3_in >= 108
	c_paa_t4_t3_in += MAS_in[0]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 108
	c_paa_t4_t3_mem0 += MAS_MEM[0]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 108
	c_paa_t4_t3_mem1 += MAS_MEM[1]

	c_cc_t2_t2_in = S.Task('c_cc_t2_t2_in', length=1, delay_cost=1)
	S += c_cc_t2_t2_in >= 109
	c_cc_t2_t2_in += MAS_in[0]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 109
	c_cc_t2_t2_mem0 += MAS_MEM[0]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 109
	c_cc_t2_t2_mem1 += MAS_MEM[1]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=3, delay_cost=1)
	S += c_paa_t4_t3 >= 109
	c_paa_t4_t3 += MAS[0]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 110
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 110
	c_aa_t2_t4_mem0 += MAS_MEM[0]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 110
	c_aa_t2_t4_mem1 += MAS_MEM[1]

	c_bc_t4_t5_in = S.Task('c_bc_t4_t5_in', length=1, delay_cost=1)
	S += c_bc_t4_t5_in >= 110
	c_bc_t4_t5_in += MAS_in[0]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 110
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 110
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=3, delay_cost=1)
	S += c_cc_t2_t2 >= 110
	c_cc_t2_t2 += MAS[0]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=11, delay_cost=1)
	S += c_aa_t2_t4 >= 111
	c_aa_t2_t4 += MM[0]

	c_bb_t31_in = S.Task('c_bb_t31_in', length=1, delay_cost=1)
	S += c_bb_t31_in >= 111
	c_bb_t31_in += MAS_in[0]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 111
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 111
	c_bb_t31_mem1 += MAS_MEM[1]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=3, delay_cost=1)
	S += c_bc_t4_t5 >= 111
	c_bc_t4_t5 += MAS[0]

	c_bb_t2_t2_in = S.Task('c_bb_t2_t2_in', length=1, delay_cost=1)
	S += c_bb_t2_t2_in >= 112
	c_bb_t2_t2_in += MAS_in[0]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 112
	c_bb_t2_t2_mem0 += MAS_MEM[0]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 112
	c_bb_t2_t2_mem1 += MAS_MEM[1]

	c_bb_t31 = S.Task('c_bb_t31', length=3, delay_cost=1)
	S += c_bb_t31 >= 112
	c_bb_t31 += MAS[0]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=3, delay_cost=1)
	S += c_bb_t2_t2 >= 113
	c_bb_t2_t2 += MAS[0]

	c_cc10_in = S.Task('c_cc10_in', length=1, delay_cost=1)
	S += c_cc10_in >= 113
	c_cc10_in += MAS_in[0]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 113
	c_cc10_mem0 += MAS_MEM[0]

	c_cc10_mem1 = S.Task('c_cc10_mem1', length=1, delay_cost=1)
	S += c_cc10_mem1 >= 113
	c_cc10_mem1 += MAS_MEM[1]

	c_bc_t50_in = S.Task('c_bc_t50_in', length=1, delay_cost=1)
	S += c_bc_t50_in >= 114
	c_bc_t50_in += MAS_in[0]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 114
	c_bc_t50_mem0 += MAS_MEM[0]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 114
	c_bc_t50_mem1 += MAS_MEM[1]

	c_cc10 = S.Task('c_cc10', length=3, delay_cost=1)
	S += c_cc10 >= 114
	c_cc10 += MAS[0]

	c_aa10_in = S.Task('c_aa10_in', length=1, delay_cost=1)
	S += c_aa10_in >= 115
	c_aa10_in += MAS_in[0]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 115
	c_aa10_mem0 += MAS_MEM[0]

	c_aa10_mem1 = S.Task('c_aa10_mem1', length=1, delay_cost=1)
	S += c_aa10_mem1 >= 115
	c_aa10_mem1 += MAS_MEM[1]

	c_bc_t50 = S.Task('c_bc_t50', length=3, delay_cost=1)
	S += c_bc_t50 >= 115
	c_bc_t50 += MAS[0]

	c_aa10 = S.Task('c_aa10', length=3, delay_cost=1)
	S += c_aa10 >= 116
	c_aa10 += MAS[0]

	c_ac_t4_t5_in = S.Task('c_ac_t4_t5_in', length=1, delay_cost=1)
	S += c_ac_t4_t5_in >= 116
	c_ac_t4_t5_in += MAS_in[0]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 116
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 116
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 116
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 116
	c_bb_t2_t4_mem0 += MAS_MEM[0]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 116
	c_bb_t2_t4_mem1 += MAS_MEM[1]

	c_ab_t4_t5_in = S.Task('c_ab_t4_t5_in', length=1, delay_cost=1)
	S += c_ab_t4_t5_in >= 117
	c_ab_t4_t5_in += MAS_in[0]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 117
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 117
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=3, delay_cost=1)
	S += c_ac_t4_t5 >= 117
	c_ac_t4_t5 += MAS[0]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=11, delay_cost=1)
	S += c_bb_t2_t4 >= 117
	c_bb_t2_t4 += MM[0]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 117
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 117
	c_cc_t2_t4_mem0 += MAS_MEM[0]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 117
	c_cc_t2_t4_mem1 += MAS_MEM[1]

	c_ab_t40_in = S.Task('c_ab_t40_in', length=1, delay_cost=1)
	S += c_ab_t40_in >= 118
	c_ab_t40_in += MAS_in[0]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 118
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 118
	c_ab_t40_mem1 += MM_MEM[1]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=3, delay_cost=1)
	S += c_ab_t4_t5 >= 118
	c_ab_t4_t5 += MAS[0]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=11, delay_cost=1)
	S += c_cc_t2_t4 >= 118
	c_cc_t2_t4 += MM[0]

	c_ab_t40 = S.Task('c_ab_t40', length=3, delay_cost=1)
	S += c_ab_t40 >= 119
	c_ab_t40 += MAS[0]

	c_ac_t01_in = S.Task('c_ac_t01_in', length=1, delay_cost=1)
	S += c_ac_t01_in >= 119
	c_ac_t01_in += MAS_in[0]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 119
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 119
	c_ac_t01_mem1 += MAS_MEM[1]

	c_ac_t01 = S.Task('c_ac_t01', length=3, delay_cost=1)
	S += c_ac_t01 >= 120
	c_ac_t01 += MAS[0]

	c_ac_t40_in = S.Task('c_ac_t40_in', length=1, delay_cost=1)
	S += c_ac_t40_in >= 120
	c_ac_t40_in += MAS_in[0]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 120
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 120
	c_ac_t40_mem1 += MM_MEM[1]

	c_ac_t40 = S.Task('c_ac_t40', length=3, delay_cost=1)
	S += c_ac_t40 >= 121
	c_ac_t40 += MAS[0]

	c_bb_t41_in = S.Task('c_bb_t41_in', length=1, delay_cost=1)
	S += c_bb_t41_in >= 121
	c_bb_t41_in += MAS_in[0]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 121
	c_bb_t41_mem0 += MAS_MEM[0]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 121
	c_bb_t41_mem1 += MAS_MEM[1]

	c_ac_s00_in = S.Task('c_ac_s00_in', length=1, delay_cost=1)
	S += c_ac_s00_in >= 122
	c_ac_s00_in += MAS_in[0]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 122
	c_ac_s00_mem0 += MAS_MEM[0]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 122
	c_ac_s00_mem1 += MAS_MEM[1]

	c_bb_t41 = S.Task('c_bb_t41', length=3, delay_cost=1)
	S += c_bb_t41 >= 122
	c_bb_t41 += MAS[0]

	c_ac_s00 = S.Task('c_ac_s00', length=3, delay_cost=1)
	S += c_ac_s00 >= 123
	c_ac_s00 += MAS[0]

	c_bc_s01_in = S.Task('c_bc_s01_in', length=1, delay_cost=1)
	S += c_bc_s01_in >= 123
	c_bc_s01_in += MAS_in[0]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 123
	c_bc_s01_mem0 += MAS_MEM[0]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 123
	c_bc_s01_mem1 += MAS_MEM[1]

	c_aa11_in = S.Task('c_aa11_in', length=1, delay_cost=1)
	S += c_aa11_in >= 124
	c_aa11_in += MAS_in[0]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 124
	c_aa11_mem0 += MAS_MEM[0]

	c_aa11_mem1 = S.Task('c_aa11_mem1', length=1, delay_cost=1)
	S += c_aa11_mem1 >= 124
	c_aa11_mem1 += MAS_MEM[1]

	c_bc_s01 = S.Task('c_bc_s01', length=3, delay_cost=1)
	S += c_bc_s01 >= 124
	c_bc_s01 += MAS[0]

	c_aa11 = S.Task('c_aa11', length=3, delay_cost=1)
	S += c_aa11 >= 125
	c_aa11 += MAS[0]

	c_ab_s01_in = S.Task('c_ab_s01_in', length=1, delay_cost=1)
	S += c_ab_s01_in >= 125
	c_ab_s01_in += MAS_in[0]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 125
	c_ab_s01_mem0 += MAS_MEM[0]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 125
	c_ab_s01_mem1 += MAS_MEM[1]

	c_ab10_in = S.Task('c_ab10_in', length=1, delay_cost=1)
	S += c_ab10_in >= 126
	c_ab10_in += MAS_in[0]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 126
	c_ab10_mem0 += MAS_MEM[0]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 126
	c_ab10_mem1 += MAS_MEM[1]

	c_ab_s01 = S.Task('c_ab_s01', length=3, delay_cost=1)
	S += c_ab_s01 >= 126
	c_ab_s01 += MAS[0]

	c_ab10 = S.Task('c_ab10', length=3, delay_cost=1)
	S += c_ab10 >= 127
	c_ab10 += MAS[0]

	c_ac10_in = S.Task('c_ac10_in', length=1, delay_cost=1)
	S += c_ac10_in >= 127
	c_ac10_in += MAS_in[0]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 127
	c_ac10_mem0 += MAS_MEM[0]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 127
	c_ac10_mem1 += MAS_MEM[1]

	c_ac10 = S.Task('c_ac10', length=3, delay_cost=1)
	S += c_ac10 >= 128
	c_ac10 += MAS[0]

	c_bb11_in = S.Task('c_bb11_in', length=1, delay_cost=1)
	S += c_bb11_in >= 128
	c_bb11_in += MAS_in[0]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 128
	c_bb11_mem0 += MAS_MEM[0]

	c_bb11_mem1 = S.Task('c_bb11_mem1', length=1, delay_cost=1)
	S += c_bb11_mem1 >= 128
	c_bb11_mem1 += MAS_MEM[1]

	c_bb11 = S.Task('c_bb11', length=3, delay_cost=1)
	S += c_bb11 >= 129
	c_bb11 += MAS[0]

	c_bc_t51_in = S.Task('c_bc_t51_in', length=1, delay_cost=1)
	S += c_bc_t51_in >= 129
	c_bc_t51_in += MAS_in[0]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 129
	c_bc_t51_mem0 += MAS_MEM[0]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 129
	c_bc_t51_mem1 += MAS_MEM[1]

	c_ab_t41_in = S.Task('c_ab_t41_in', length=1, delay_cost=1)
	S += c_ab_t41_in >= 130
	c_ab_t41_in += MAS_in[0]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 130
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 130
	c_ab_t41_mem1 += MAS_MEM[1]

	c_bc_t51 = S.Task('c_bc_t51', length=3, delay_cost=1)
	S += c_bc_t51 >= 130
	c_bc_t51 += MAS[0]

	c_ab_t41 = S.Task('c_ab_t41', length=3, delay_cost=1)
	S += c_ab_t41 >= 131
	c_ab_t41 += MAS[0]

	c_bc_s00_in = S.Task('c_bc_s00_in', length=1, delay_cost=1)
	S += c_bc_s00_in >= 131
	c_bc_s00_in += MAS_in[0]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 131
	c_bc_s00_mem0 += MAS_MEM[0]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 131
	c_bc_s00_mem1 += MAS_MEM[1]

	c_bc_s00 = S.Task('c_bc_s00', length=3, delay_cost=1)
	S += c_bc_s00 >= 132
	c_bc_s00 += MAS[0]

	c_cc_t2_t5_in = S.Task('c_cc_t2_t5_in', length=1, delay_cost=1)
	S += c_cc_t2_t5_in >= 132
	c_cc_t2_t5_in += MAS_in[0]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 132
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 132
	c_cc_t2_t5_mem1 += MM_MEM[1]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=3, delay_cost=1)
	S += c_cc_t2_t5 >= 133
	c_cc_t2_t5 += MAS[0]

	c_cc_t41_in = S.Task('c_cc_t41_in', length=1, delay_cost=1)
	S += c_cc_t41_in >= 133
	c_cc_t41_in += MAS_in[0]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 133
	c_cc_t41_mem0 += MAS_MEM[0]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 133
	c_cc_t41_mem1 += MAS_MEM[1]

	c_bc10_in = S.Task('c_bc10_in', length=1, delay_cost=1)
	S += c_bc10_in >= 134
	c_bc10_in += MAS_in[0]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 134
	c_bc10_mem0 += MAS_MEM[0]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 134
	c_bc10_mem1 += MAS_MEM[1]

	c_cc_t41 = S.Task('c_cc_t41', length=3, delay_cost=1)
	S += c_cc_t41 >= 134
	c_cc_t41 += MAS[0]

	c_bb_t40_in = S.Task('c_bb_t40_in', length=1, delay_cost=1)
	S += c_bb_t40_in >= 135
	c_bb_t40_in += MAS_in[0]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 135
	c_bb_t40_mem0 += MAS_MEM[0]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 135
	c_bb_t40_mem1 += MAS_MEM[1]

	c_bc10 = S.Task('c_bc10', length=3, delay_cost=1)
	S += c_bc10 >= 135
	c_bc10 += MAS[0]

	c_ac_t51_in = S.Task('c_ac_t51_in', length=1, delay_cost=1)
	S += c_ac_t51_in >= 136
	c_ac_t51_in += MAS_in[0]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 136
	c_ac_t51_mem0 += MAS_MEM[0]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 136
	c_ac_t51_mem1 += MAS_MEM[1]

	c_bb_t40 = S.Task('c_bb_t40', length=3, delay_cost=1)
	S += c_bb_t40 >= 136
	c_bb_t40 += MAS[0]

	c_ac_t51 = S.Task('c_ac_t51', length=3, delay_cost=1)
	S += c_ac_t51 >= 137
	c_ac_t51 += MAS[0]

	c_cc11_in = S.Task('c_cc11_in', length=1, delay_cost=1)
	S += c_cc11_in >= 137
	c_cc11_in += MAS_in[0]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 137
	c_cc11_mem0 += MAS_MEM[0]

	c_cc11_mem1 = S.Task('c_cc11_mem1', length=1, delay_cost=1)
	S += c_cc11_mem1 >= 137
	c_cc11_mem1 += MAS_MEM[1]

	c_bc_t41_in = S.Task('c_bc_t41_in', length=1, delay_cost=1)
	S += c_bc_t41_in >= 138
	c_bc_t41_in += MAS_in[0]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 138
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 138
	c_bc_t41_mem1 += MAS_MEM[1]

	c_cc11 = S.Task('c_cc11', length=3, delay_cost=1)
	S += c_cc11 >= 138
	c_cc11 += MAS[0]

	c_ab_s00_in = S.Task('c_ab_s00_in', length=1, delay_cost=1)
	S += c_ab_s00_in >= 139
	c_ab_s00_in += MAS_in[0]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 139
	c_ab_s00_mem0 += MAS_MEM[0]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 139
	c_ab_s00_mem1 += MAS_MEM[1]

	c_bc_t41 = S.Task('c_bc_t41', length=3, delay_cost=1)
	S += c_bc_t41 >= 139
	c_bc_t41 += MAS[0]

	c_ab_s00 = S.Task('c_ab_s00', length=3, delay_cost=1)
	S += c_ab_s00 >= 140
	c_ab_s00 += MAS[0]

	c_cc_t40_in = S.Task('c_cc_t40_in', length=1, delay_cost=1)
	S += c_cc_t40_in >= 140
	c_cc_t40_in += MAS_in[0]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 140
	c_cc_t40_mem0 += MAS_MEM[0]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 140
	c_cc_t40_mem1 += MAS_MEM[1]

	c_aa_t40_in = S.Task('c_aa_t40_in', length=1, delay_cost=1)
	S += c_aa_t40_in >= 141
	c_aa_t40_in += MAS_in[0]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 141
	c_aa_t40_mem0 += MAS_MEM[0]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 141
	c_aa_t40_mem1 += MAS_MEM[1]

	c_cc_t40 = S.Task('c_cc_t40', length=3, delay_cost=1)
	S += c_cc_t40 >= 141
	c_cc_t40 += MAS[0]

	c_aa_t40 = S.Task('c_aa_t40', length=3, delay_cost=1)
	S += c_aa_t40 >= 142
	c_aa_t40 += MAS[0]

	c_ac_t41_in = S.Task('c_ac_t41_in', length=1, delay_cost=1)
	S += c_ac_t41_in >= 142
	c_ac_t41_in += MAS_in[0]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 142
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 142
	c_ac_t41_mem1 += MAS_MEM[1]

	c_ac_t41 = S.Task('c_ac_t41', length=3, delay_cost=1)
	S += c_ac_t41 >= 143
	c_ac_t41 += MAS[0]

	c_cc_t20_in = S.Task('c_cc_t20_in', length=1, delay_cost=1)
	S += c_cc_t20_in >= 143
	c_cc_t20_in += MAS_in[0]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 143
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 143
	c_cc_t20_mem1 += MM_MEM[1]

	c_bb_t2_t5_in = S.Task('c_bb_t2_t5_in', length=1, delay_cost=1)
	S += c_bb_t2_t5_in >= 144
	c_bb_t2_t5_in += MAS_in[0]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 144
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 144
	c_bb_t2_t5_mem1 += MM_MEM[1]

	c_cc_t20 = S.Task('c_cc_t20', length=3, delay_cost=1)
	S += c_cc_t20 >= 144
	c_cc_t20 += MAS[0]

	c_aa_t41_in = S.Task('c_aa_t41_in', length=1, delay_cost=1)
	S += c_aa_t41_in >= 145
	c_aa_t41_in += MAS_in[0]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 145
	c_aa_t41_mem0 += MAS_MEM[0]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 145
	c_aa_t41_mem1 += MAS_MEM[1]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=3, delay_cost=1)
	S += c_bb_t2_t5 >= 145
	c_bb_t2_t5 += MAS[0]

	c_aa_t41 = S.Task('c_aa_t41', length=3, delay_cost=1)
	S += c_aa_t41 >= 146
	c_aa_t41 += MAS[0]

	c_ab_t51_in = S.Task('c_ab_t51_in', length=1, delay_cost=1)
	S += c_ab_t51_in >= 146
	c_ab_t51_in += MAS_in[0]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 146
	c_ab_t51_mem0 += MAS_MEM[0]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 146
	c_ab_t51_mem1 += MAS_MEM[1]

	c_ab_t51 = S.Task('c_ab_t51', length=3, delay_cost=1)
	S += c_ab_t51 >= 147
	c_ab_t51 += MAS[0]

	c_ac_s01_in = S.Task('c_ac_s01_in', length=1, delay_cost=1)
	S += c_ac_s01_in >= 147
	c_ac_s01_in += MAS_in[0]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 147
	c_ac_s01_mem0 += MAS_MEM[0]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 147
	c_ac_s01_mem1 += MAS_MEM[1]

	c_ac_s01 = S.Task('c_ac_s01', length=3, delay_cost=1)
	S += c_ac_s01 >= 148
	c_ac_s01 += MAS[0]

	c_bb_t20_in = S.Task('c_bb_t20_in', length=1, delay_cost=1)
	S += c_bb_t20_in >= 148
	c_bb_t20_in += MAS_in[0]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 148
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 148
	c_bb_t20_mem1 += MM_MEM[1]

	c_aa_t2_t5_in = S.Task('c_aa_t2_t5_in', length=1, delay_cost=1)
	S += c_aa_t2_t5_in >= 149
	c_aa_t2_t5_in += MAS_in[0]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 149
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 149
	c_aa_t2_t5_mem1 += MM_MEM[1]

	c_bb_t20 = S.Task('c_bb_t20', length=3, delay_cost=1)
	S += c_bb_t20 >= 149
	c_bb_t20 += MAS[0]

	c_aa_t20_in = S.Task('c_aa_t20_in', length=1, delay_cost=1)
	S += c_aa_t20_in >= 150
	c_aa_t20_in += MAS_in[0]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 150
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 150
	c_aa_t20_mem1 += MM_MEM[1]

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=3, delay_cost=1)
	S += c_aa_t2_t5 >= 150
	c_aa_t2_t5 += MAS[0]

	c_aa_t20 = S.Task('c_aa_t20', length=3, delay_cost=1)
	S += c_aa_t20 >= 151
	c_aa_t20 += MAS[0]


	# new tasks
	c_aa_t21 = S.Task('c_aa_t21', length=3, delay_cost=1)
	c_aa_t21 += alt(MAS)
	c_aa_t21_in = S.Task('c_aa_t21_in', length=1, delay_cost=1)
	c_aa_t21_in += alt(MAS_in)
	S += c_aa_t21_in*MAS_in[0]<=c_aa_t21*MAS[0]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	c_aa_t21_mem0 += MM_MEM[0]
	S += 121 < c_aa_t21_mem0
	S += c_aa_t21_mem0 <= c_aa_t21

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	c_aa_t21_mem1 += MAS_MEM[1]
	S += 152 < c_aa_t21_mem1
	S += c_aa_t21_mem1 <= c_aa_t21

	c_aa_t50 = S.Task('c_aa_t50', length=3, delay_cost=1)
	c_aa_t50 += alt(MAS)
	c_aa_t50_in = S.Task('c_aa_t50_in', length=1, delay_cost=1)
	c_aa_t50_in += alt(MAS_in)
	S += c_aa_t50_in*MAS_in[0]<=c_aa_t50*MAS[0]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	c_aa_t50_mem0 += MAS_MEM[0]
	S += 49 < c_aa_t50_mem0
	S += c_aa_t50_mem0 <= c_aa_t50

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	c_aa_t50_mem1 += MAS_MEM[1]
	S += 144 < c_aa_t50_mem1
	S += c_aa_t50_mem1 <= c_aa_t50

	c_aa_t51 = S.Task('c_aa_t51', length=3, delay_cost=1)
	c_aa_t51 += alt(MAS)
	c_aa_t51_in = S.Task('c_aa_t51_in', length=1, delay_cost=1)
	c_aa_t51_in += alt(MAS_in)
	S += c_aa_t51_in*MAS_in[0]<=c_aa_t51*MAS[0]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	c_aa_t51_mem0 += MAS_MEM[0]
	S += 101 < c_aa_t51_mem0
	S += c_aa_t51_mem0 <= c_aa_t51

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	c_aa_t51_mem1 += MAS_MEM[1]
	S += 148 < c_aa_t51_mem1
	S += c_aa_t51_mem1 <= c_aa_t51

	c_bb_t21 = S.Task('c_bb_t21', length=3, delay_cost=1)
	c_bb_t21 += alt(MAS)
	c_bb_t21_in = S.Task('c_bb_t21_in', length=1, delay_cost=1)
	c_bb_t21_in += alt(MAS_in)
	S += c_bb_t21_in*MAS_in[0]<=c_bb_t21*MAS[0]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	c_bb_t21_mem0 += MM_MEM[0]
	S += 127 < c_bb_t21_mem0
	S += c_bb_t21_mem0 <= c_bb_t21

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	c_bb_t21_mem1 += MAS_MEM[1]
	S += 147 < c_bb_t21_mem1
	S += c_bb_t21_mem1 <= c_bb_t21

	c_bb_t50 = S.Task('c_bb_t50', length=3, delay_cost=1)
	c_bb_t50 += alt(MAS)
	c_bb_t50_in = S.Task('c_bb_t50_in', length=1, delay_cost=1)
	c_bb_t50_in += alt(MAS_in)
	S += c_bb_t50_in*MAS_in[0]<=c_bb_t50*MAS[0]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	c_bb_t50_mem0 += MAS_MEM[0]
	S += 52 < c_bb_t50_mem0
	S += c_bb_t50_mem0 <= c_bb_t50

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	c_bb_t50_mem1 += MAS_MEM[1]
	S += 138 < c_bb_t50_mem1
	S += c_bb_t50_mem1 <= c_bb_t50

	c_bb_t51 = S.Task('c_bb_t51', length=3, delay_cost=1)
	c_bb_t51 += alt(MAS)
	c_bb_t51_in = S.Task('c_bb_t51_in', length=1, delay_cost=1)
	c_bb_t51_in += alt(MAS_in)
	S += c_bb_t51_in*MAS_in[0]<=c_bb_t51*MAS[0]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	c_bb_t51_mem0 += MAS_MEM[0]
	S += 114 < c_bb_t51_mem0
	S += c_bb_t51_mem0 <= c_bb_t51

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	c_bb_t51_mem1 += MAS_MEM[1]
	S += 124 < c_bb_t51_mem1
	S += c_bb_t51_mem1 <= c_bb_t51

	c_cc_t21 = S.Task('c_cc_t21', length=3, delay_cost=1)
	c_cc_t21 += alt(MAS)
	c_cc_t21_in = S.Task('c_cc_t21_in', length=1, delay_cost=1)
	c_cc_t21_in += alt(MAS_in)
	S += c_cc_t21_in*MAS_in[0]<=c_cc_t21*MAS[0]

	c_cc_t21_mem0 = S.Task('c_cc_t21_mem0', length=1, delay_cost=1)
	c_cc_t21_mem0 += MM_MEM[0]
	S += 128 < c_cc_t21_mem0
	S += c_cc_t21_mem0 <= c_cc_t21

	c_cc_t21_mem1 = S.Task('c_cc_t21_mem1', length=1, delay_cost=1)
	c_cc_t21_mem1 += MAS_MEM[1]
	S += 135 < c_cc_t21_mem1
	S += c_cc_t21_mem1 <= c_cc_t21

	c_cc_t50 = S.Task('c_cc_t50', length=3, delay_cost=1)
	c_cc_t50 += alt(MAS)
	c_cc_t50_in = S.Task('c_cc_t50_in', length=1, delay_cost=1)
	c_cc_t50_in += alt(MAS_in)
	S += c_cc_t50_in*MAS_in[0]<=c_cc_t50*MAS[0]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	c_cc_t50_mem0 += MAS_MEM[0]
	S += 29 < c_cc_t50_mem0
	S += c_cc_t50_mem0 <= c_cc_t50

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	c_cc_t50_mem1 += MAS_MEM[1]
	S += 143 < c_cc_t50_mem1
	S += c_cc_t50_mem1 <= c_cc_t50

	c_cc_t51 = S.Task('c_cc_t51', length=3, delay_cost=1)
	c_cc_t51 += alt(MAS)
	c_cc_t51_in = S.Task('c_cc_t51_in', length=1, delay_cost=1)
	c_cc_t51_in += alt(MAS_in)
	S += c_cc_t51_in*MAS_in[0]<=c_cc_t51*MAS[0]

	c_cc_t51_mem0 = S.Task('c_cc_t51_mem0', length=1, delay_cost=1)
	c_cc_t51_mem0 += MAS_MEM[0]
	S += 102 < c_cc_t51_mem0
	S += c_cc_t51_mem0 <= c_cc_t51

	c_cc_t51_mem1 = S.Task('c_cc_t51_mem1', length=1, delay_cost=1)
	c_cc_t51_mem1 += MAS_MEM[1]
	S += 136 < c_cc_t51_mem1
	S += c_cc_t51_mem1 <= c_cc_t51

	c_ab00 = S.Task('c_ab00', length=3, delay_cost=1)
	c_ab00 += alt(MAS)
	c_ab00_in = S.Task('c_ab00_in', length=1, delay_cost=1)
	c_ab00_in += alt(MAS_in)
	S += c_ab00_in*MAS_in[0]<=c_ab00*MAS[0]

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	c_ab00_mem0 += MAS_MEM[0]
	S += 46 < c_ab00_mem0
	S += c_ab00_mem0 <= c_ab00

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	c_ab00_mem1 += MAS_MEM[1]
	S += 142 < c_ab00_mem1
	S += c_ab00_mem1 <= c_ab00

	c_ab01 = S.Task('c_ab01', length=3, delay_cost=1)
	c_ab01 += alt(MAS)
	c_ab01_in = S.Task('c_ab01_in', length=1, delay_cost=1)
	c_ab01_in += alt(MAS_in)
	S += c_ab01_in*MAS_in[0]<=c_ab01*MAS[0]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	c_ab01_mem0 += MAS_MEM[0]
	S += 110 < c_ab01_mem0
	S += c_ab01_mem0 <= c_ab01

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	c_ab01_mem1 += MAS_MEM[1]
	S += 128 < c_ab01_mem1
	S += c_ab01_mem1 <= c_ab01

	c_ab11 = S.Task('c_ab11', length=3, delay_cost=1)
	c_ab11 += alt(MAS)
	c_ab11_in = S.Task('c_ab11_in', length=1, delay_cost=1)
	c_ab11_in += alt(MAS_in)
	S += c_ab11_in*MAS_in[0]<=c_ab11*MAS[0]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	c_ab11_mem0 += MAS_MEM[0]
	S += 133 < c_ab11_mem0
	S += c_ab11_mem0 <= c_ab11

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	c_ab11_mem1 += MAS_MEM[1]
	S += 149 < c_ab11_mem1
	S += c_ab11_mem1 <= c_ab11

	c_bc00 = S.Task('c_bc00', length=3, delay_cost=1)
	c_bc00 += alt(MAS)
	c_bc00_in = S.Task('c_bc00_in', length=1, delay_cost=1)
	c_bc00_in += alt(MAS_in)
	S += c_bc00_in*MAS_in[0]<=c_bc00*MAS[0]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	c_bc00_mem0 += MAS_MEM[0]
	S += 81 < c_bc00_mem0
	S += c_bc00_mem0 <= c_bc00

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	c_bc00_mem1 += MAS_MEM[1]
	S += 134 < c_bc00_mem1
	S += c_bc00_mem1 <= c_bc00

	c_bc01 = S.Task('c_bc01', length=3, delay_cost=1)
	c_bc01 += alt(MAS)
	c_bc01_in = S.Task('c_bc01_in', length=1, delay_cost=1)
	c_bc01_in += alt(MAS_in)
	S += c_bc01_in*MAS_in[0]<=c_bc01*MAS[0]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	c_bc01_mem0 += MAS_MEM[0]
	S += 103 < c_bc01_mem0
	S += c_bc01_mem0 <= c_bc01

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	c_bc01_mem1 += MAS_MEM[1]
	S += 126 < c_bc01_mem1
	S += c_bc01_mem1 <= c_bc01

	c_bc11 = S.Task('c_bc11', length=3, delay_cost=1)
	c_bc11 += alt(MAS)
	c_bc11_in = S.Task('c_bc11_in', length=1, delay_cost=1)
	c_bc11_in += alt(MAS_in)
	S += c_bc11_in*MAS_in[0]<=c_bc11*MAS[0]

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	c_bc11_mem0 += MAS_MEM[0]
	S += 141 < c_bc11_mem0
	S += c_bc11_mem0 <= c_bc11

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	c_bc11_mem1 += MAS_MEM[1]
	S += 132 < c_bc11_mem1
	S += c_bc11_mem1 <= c_bc11

	c_ac00 = S.Task('c_ac00', length=3, delay_cost=1)
	c_ac00 += alt(MAS)
	c_ac00_in = S.Task('c_ac00_in', length=1, delay_cost=1)
	c_ac00_in += alt(MAS_in)
	S += c_ac00_in*MAS_in[0]<=c_ac00*MAS[0]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	c_ac00_mem0 += MAS_MEM[0]
	S += 88 < c_ac00_mem0
	S += c_ac00_mem0 <= c_ac00

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	c_ac00_mem1 += MAS_MEM[1]
	S += 125 < c_ac00_mem1
	S += c_ac00_mem1 <= c_ac00

	c_ac01 = S.Task('c_ac01', length=3, delay_cost=1)
	c_ac01 += alt(MAS)
	c_ac01_in = S.Task('c_ac01_in', length=1, delay_cost=1)
	c_ac01_in += alt(MAS_in)
	S += c_ac01_in*MAS_in[0]<=c_ac01*MAS[0]

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	c_ac01_mem0 += MAS_MEM[0]
	S += 122 < c_ac01_mem0
	S += c_ac01_mem0 <= c_ac01

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	c_ac01_mem1 += MAS_MEM[1]
	S += 150 < c_ac01_mem1
	S += c_ac01_mem1 <= c_ac01

	c_ac11 = S.Task('c_ac11', length=3, delay_cost=1)
	c_ac11 += alt(MAS)
	c_ac11_in = S.Task('c_ac11_in', length=1, delay_cost=1)
	c_ac11_in += alt(MAS_in)
	S += c_ac11_in*MAS_in[0]<=c_ac11*MAS[0]

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	c_ac11_mem0 += MAS_MEM[0]
	S += 145 < c_ac11_mem0
	S += c_ac11_mem0 <= c_ac11

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	c_ac11_mem1 += MAS_MEM[1]
	S += 139 < c_ac11_mem1
	S += c_ac11_mem1 <= c_ac11

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=3, delay_cost=1)
	c_ccxi_y1_0 += alt(MAS)
	c_ccxi_y1_0_in = S.Task('c_ccxi_y1_0_in', length=1, delay_cost=1)
	c_ccxi_y1_0_in += alt(MAS_in)
	S += c_ccxi_y1_0_in*MAS_in[0]<=c_ccxi_y1_0*MAS[0]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	c_ccxi_y1_0_mem0 += MAS_MEM[0]
	S += 116 < c_ccxi_y1_0_mem0
	S += c_ccxi_y1_0_mem0 <= c_ccxi_y1_0

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	c_ccxi_y1_0_mem1 += MAS_MEM[1]
	S += 140 < c_ccxi_y1_0_mem1
	S += c_ccxi_y1_0_mem1 <= c_ccxi_y1_0

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=3, delay_cost=1)
	c_ccxi_y1_1 += alt(MAS)
	c_ccxi_y1_1_in = S.Task('c_ccxi_y1_1_in', length=1, delay_cost=1)
	c_ccxi_y1_1_in += alt(MAS_in)
	S += c_ccxi_y1_1_in*MAS_in[0]<=c_ccxi_y1_1*MAS[0]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	c_ccxi_y1_1_mem0 += MAS_MEM[0]
	S += 140 < c_ccxi_y1_1_mem0
	S += c_ccxi_y1_1_mem0 <= c_ccxi_y1_1

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	c_ccxi_y1_1_mem1 += MAS_MEM[1]
	S += 116 < c_ccxi_y1_1_mem1
	S += c_ccxi_y1_1_mem1 <= c_ccxi_y1_1

	c_pc10 = S.Task('c_pc10', length=3, delay_cost=1)
	c_pc10 += alt(MAS)
	c_pc10_in = S.Task('c_pc10_in', length=1, delay_cost=1)
	c_pc10_in += alt(MAS_in)
	S += c_pc10_in*MAS_in[0]<=c_pc10*MAS[0]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	c_pc10_mem0 += MAS_MEM[0]
	S += 107 < c_pc10_mem0
	S += c_pc10_mem0 <= c_pc10

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	c_pc10_mem1 += MAS_MEM[1]
	S += 130 < c_pc10_mem1
	S += c_pc10_mem1 <= c_pc10

	c_aa00 = S.Task('c_aa00', length=3, delay_cost=1)
	c_aa00 += alt(MAS)
	c_aa00_in = S.Task('c_aa00_in', length=1, delay_cost=1)
	c_aa00_in += alt(MAS_in)
	S += c_aa00_in*MAS_in[0]<=c_aa00*MAS[0]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	c_aa00_mem0 += MAS_MEM[0]
	S += 153 < c_aa00_mem0
	S += c_aa00_mem0 <= c_aa00

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	c_aa00_mem1 += alt(MAS_MEM)
	S += (c_aa_t50*MAS[0])-1 < c_aa00_mem1*MAS_MEM[1]
	S += c_aa00_mem1 <= c_aa00

	c_aa01 = S.Task('c_aa01', length=3, delay_cost=1)
	c_aa01 += alt(MAS)
	c_aa01_in = S.Task('c_aa01_in', length=1, delay_cost=1)
	c_aa01_in += alt(MAS_in)
	S += c_aa01_in*MAS_in[0]<=c_aa01*MAS[0]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	c_aa01_mem0 += alt(MAS_MEM)
	S += (c_aa_t21*MAS[0])-1 < c_aa01_mem0*MAS_MEM[0]
	S += c_aa01_mem0 <= c_aa01

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	c_aa01_mem1 += alt(MAS_MEM)
	S += (c_aa_t51*MAS[0])-1 < c_aa01_mem1*MAS_MEM[1]
	S += c_aa01_mem1 <= c_aa01

	c_bb00 = S.Task('c_bb00', length=3, delay_cost=1)
	c_bb00 += alt(MAS)
	c_bb00_in = S.Task('c_bb00_in', length=1, delay_cost=1)
	c_bb00_in += alt(MAS_in)
	S += c_bb00_in*MAS_in[0]<=c_bb00*MAS[0]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	c_bb00_mem0 += MAS_MEM[0]
	S += 151 < c_bb00_mem0
	S += c_bb00_mem0 <= c_bb00

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	c_bb00_mem1 += alt(MAS_MEM)
	S += (c_bb_t50*MAS[0])-1 < c_bb00_mem1*MAS_MEM[1]
	S += c_bb00_mem1 <= c_bb00

	c_bb01 = S.Task('c_bb01', length=3, delay_cost=1)
	c_bb01 += alt(MAS)
	c_bb01_in = S.Task('c_bb01_in', length=1, delay_cost=1)
	c_bb01_in += alt(MAS_in)
	S += c_bb01_in*MAS_in[0]<=c_bb01*MAS[0]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	c_bb01_mem0 += alt(MAS_MEM)
	S += (c_bb_t21*MAS[0])-1 < c_bb01_mem0*MAS_MEM[0]
	S += c_bb01_mem0 <= c_bb01

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	c_bb01_mem1 += alt(MAS_MEM)
	S += (c_bb_t51*MAS[0])-1 < c_bb01_mem1*MAS_MEM[1]
	S += c_bb01_mem1 <= c_bb01

	c_cc00 = S.Task('c_cc00', length=3, delay_cost=1)
	c_cc00 += alt(MAS)
	c_cc00_in = S.Task('c_cc00_in', length=1, delay_cost=1)
	c_cc00_in += alt(MAS_in)
	S += c_cc00_in*MAS_in[0]<=c_cc00*MAS[0]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	c_cc00_mem0 += MAS_MEM[0]
	S += 146 < c_cc00_mem0
	S += c_cc00_mem0 <= c_cc00

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	c_cc00_mem1 += alt(MAS_MEM)
	S += (c_cc_t50*MAS[0])-1 < c_cc00_mem1*MAS_MEM[1]
	S += c_cc00_mem1 <= c_cc00

	c_cc01 = S.Task('c_cc01', length=3, delay_cost=1)
	c_cc01 += alt(MAS)
	c_cc01_in = S.Task('c_cc01_in', length=1, delay_cost=1)
	c_cc01_in += alt(MAS_in)
	S += c_cc01_in*MAS_in[0]<=c_cc01*MAS[0]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	c_cc01_mem0 += alt(MAS_MEM)
	S += (c_cc_t21*MAS[0])-1 < c_cc01_mem0*MAS_MEM[0]
	S += c_cc01_mem0 <= c_cc01

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	c_cc01_mem1 += alt(MAS_MEM)
	S += (c_cc_t51*MAS[0])-1 < c_cc01_mem1*MAS_MEM[1]
	S += c_cc01_mem1 <= c_cc01

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=3, delay_cost=1)
	c_bcxi_y1_0 += alt(MAS)
	c_bcxi_y1_0_in = S.Task('c_bcxi_y1_0_in', length=1, delay_cost=1)
	c_bcxi_y1_0_in += alt(MAS_in)
	S += c_bcxi_y1_0_in*MAS_in[0]<=c_bcxi_y1_0*MAS[0]

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	c_bcxi_y1_0_mem0 += MAS_MEM[0]
	S += 137 < c_bcxi_y1_0_mem0
	S += c_bcxi_y1_0_mem0 <= c_bcxi_y1_0

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	c_bcxi_y1_0_mem1 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_0_mem1*MAS_MEM[1]
	S += c_bcxi_y1_0_mem1 <= c_bcxi_y1_0

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=3, delay_cost=1)
	c_bcxi_y1_1 += alt(MAS)
	c_bcxi_y1_1_in = S.Task('c_bcxi_y1_1_in', length=1, delay_cost=1)
	c_bcxi_y1_1_in += alt(MAS_in)
	S += c_bcxi_y1_1_in*MAS_in[0]<=c_bcxi_y1_1*MAS[0]

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	c_bcxi_y1_1_mem0 += alt(MAS_MEM)
	S += (c_bc11*MAS[0])-1 < c_bcxi_y1_1_mem0*MAS_MEM[0]
	S += c_bcxi_y1_1_mem0 <= c_bcxi_y1_1

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	c_bcxi_y1_1_mem1 += MAS_MEM[1]
	S += 137 < c_bcxi_y1_1_mem1
	S += c_bcxi_y1_1_mem1 <= c_bcxi_y1_1

	c_pa10 = S.Task('c_pa10', length=3, delay_cost=1)
	c_pa10 += alt(MAS)
	c_pa10_in = S.Task('c_pa10_in', length=1, delay_cost=1)
	c_pa10_in += alt(MAS_in)
	S += c_pa10_in*MAS_in[0]<=c_pa10*MAS[0]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	c_pa10_mem0 += MAS_MEM[0]
	S += 118 < c_pa10_mem0
	S += c_pa10_mem0 <= c_pa10

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	c_pa10_mem1 += alt(MAS_MEM)
	S += (c_bc00*MAS[0])-1 < c_pa10_mem1*MAS_MEM[1]
	S += c_pa10_mem1 <= c_pa10

	c_pa11 = S.Task('c_pa11', length=3, delay_cost=1)
	c_pa11 += alt(MAS)
	c_pa11_in = S.Task('c_pa11_in', length=1, delay_cost=1)
	c_pa11_in += alt(MAS_in)
	S += c_pa11_in*MAS_in[0]<=c_pa11*MAS[0]

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	c_pa11_mem0 += MAS_MEM[0]
	S += 127 < c_pa11_mem0
	S += c_pa11_mem0 <= c_pa11

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	c_pa11_mem1 += alt(MAS_MEM)
	S += (c_bc01*MAS[0])-1 < c_pa11_mem1*MAS_MEM[1]
	S += c_pa11_mem1 <= c_pa11

	c_pb00 = S.Task('c_pb00', length=3, delay_cost=1)
	c_pb00 += alt(MAS)
	c_pb00_in = S.Task('c_pb00_in', length=1, delay_cost=1)
	c_pb00_in += alt(MAS_in)
	S += c_pb00_in*MAS_in[0]<=c_pb00*MAS[0]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	c_pb00_mem0 += alt(MAS_MEM)
	S += (c_ccxi_y1_0*MAS[0])-1 < c_pb00_mem0*MAS_MEM[0]
	S += c_pb00_mem0 <= c_pb00

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	c_pb00_mem1 += alt(MAS_MEM)
	S += (c_ab00*MAS[0])-1 < c_pb00_mem1*MAS_MEM[1]
	S += c_pb00_mem1 <= c_pb00

	c_pb01 = S.Task('c_pb01', length=3, delay_cost=1)
	c_pb01 += alt(MAS)
	c_pb01_in = S.Task('c_pb01_in', length=1, delay_cost=1)
	c_pb01_in += alt(MAS_in)
	S += c_pb01_in*MAS_in[0]<=c_pb01*MAS[0]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	c_pb01_mem0 += alt(MAS_MEM)
	S += (c_ccxi_y1_1*MAS[0])-1 < c_pb01_mem0*MAS_MEM[0]
	S += c_pb01_mem0 <= c_pb01

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	c_pb01_mem1 += alt(MAS_MEM)
	S += (c_ab01*MAS[0])-1 < c_pb01_mem1*MAS_MEM[1]
	S += c_pb01_mem1 <= c_pb01

	c_pc11 = S.Task('c_pc11', length=3, delay_cost=1)
	c_pc11 += alt(MAS)
	c_pc11_in = S.Task('c_pc11_in', length=1, delay_cost=1)
	c_pc11_in += alt(MAS_in)
	S += c_pc11_in*MAS_in[0]<=c_pc11*MAS[0]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	c_pc11_mem0 += MAS_MEM[0]
	S += 131 < c_pc11_mem0
	S += c_pc11_mem0 <= c_pc11

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	c_pc11_mem1 += alt(MAS_MEM)
	S += (c_ac11*MAS[0])-1 < c_pc11_mem1*MAS_MEM[1]
	S += c_pc11_mem1 <= c_pc11

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=11, delay_cost=1)
	c_pcb_t1_t0 += alt(MM)
	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	c_pcb_t1_t0_in += alt(MM_in)
	S += c_pcb_t1_t0_in*MM_in[0]<=c_pcb_t1_t0*MM[0]
	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	c_pcb_t1_t0_mem0 += alt(MAS_MEM)
	S += (c_pc10*MAS[0])-1 < c_pcb_t1_t0_mem0*MAS_MEM[0]
	S += c_pcb_t1_t0_mem0 <= c_pcb_t1_t0

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	c_pcb_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_pcb_t1_t0_mem1 <= c_pcb_t1_t0

	c_pa00 = S.Task('c_pa00', length=3, delay_cost=1)
	c_pa00 += alt(MAS)
	c_pa00_in = S.Task('c_pa00_in', length=1, delay_cost=1)
	c_pa00_in += alt(MAS_in)
	S += c_pa00_in*MAS_in[0]<=c_pa00*MAS[0]

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	c_pa00_mem0 += alt(MAS_MEM)
	S += (c_aa00*MAS[0])-1 < c_pa00_mem0*MAS_MEM[0]
	S += c_pa00_mem0 <= c_pa00

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	c_pa00_mem1 += alt(MAS_MEM)
	S += (c_bcxi_y1_0*MAS[0])-1 < c_pa00_mem1*MAS_MEM[1]
	S += c_pa00_mem1 <= c_pa00

	c_pa01 = S.Task('c_pa01', length=3, delay_cost=1)
	c_pa01 += alt(MAS)
	c_pa01_in = S.Task('c_pa01_in', length=1, delay_cost=1)
	c_pa01_in += alt(MAS_in)
	S += c_pa01_in*MAS_in[0]<=c_pa01*MAS[0]

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	c_pa01_mem0 += alt(MAS_MEM)
	S += (c_aa01*MAS[0])-1 < c_pa01_mem0*MAS_MEM[0]
	S += c_pa01_mem0 <= c_pa01

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	c_pa01_mem1 += alt(MAS_MEM)
	S += (c_bcxi_y1_1*MAS[0])-1 < c_pa01_mem1*MAS_MEM[1]
	S += c_pa01_mem1 <= c_pa01

	c_pb10 = S.Task('c_pb10', length=3, delay_cost=1)
	c_pb10 += alt(MAS)
	c_pb10_in = S.Task('c_pb10_in', length=1, delay_cost=1)
	c_pb10_in += alt(MAS_in)
	S += c_pb10_in*MAS_in[0]<=c_pb10*MAS[0]

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	c_pb10_mem0 += alt(MAS_MEM)
	S += (c_cc00*MAS[0])-1 < c_pb10_mem0*MAS_MEM[0]
	S += c_pb10_mem0 <= c_pb10

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	c_pb10_mem1 += MAS_MEM[1]
	S += 129 < c_pb10_mem1
	S += c_pb10_mem1 <= c_pb10

	c_pb11 = S.Task('c_pb11', length=3, delay_cost=1)
	c_pb11 += alt(MAS)
	c_pb11_in = S.Task('c_pb11_in', length=1, delay_cost=1)
	c_pb11_in += alt(MAS_in)
	S += c_pb11_in*MAS_in[0]<=c_pb11*MAS[0]

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	c_pb11_mem0 += alt(MAS_MEM)
	S += (c_cc01*MAS[0])-1 < c_pb11_mem0*MAS_MEM[0]
	S += c_pb11_mem0 <= c_pb11

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	c_pb11_mem1 += alt(MAS_MEM)
	S += (c_ab11*MAS[0])-1 < c_pb11_mem1*MAS_MEM[1]
	S += c_pb11_mem1 <= c_pb11

	c_pc00 = S.Task('c_pc00', length=3, delay_cost=1)
	c_pc00 += alt(MAS)
	c_pc00_in = S.Task('c_pc00_in', length=1, delay_cost=1)
	c_pc00_in += alt(MAS_in)
	S += c_pc00_in*MAS_in[0]<=c_pc00*MAS[0]

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	c_pc00_mem0 += alt(MAS_MEM)
	S += (c_bb00*MAS[0])-1 < c_pc00_mem0*MAS_MEM[0]
	S += c_pc00_mem0 <= c_pc00

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	c_pc00_mem1 += alt(MAS_MEM)
	S += (c_ac00*MAS[0])-1 < c_pc00_mem1*MAS_MEM[1]
	S += c_pc00_mem1 <= c_pc00

	c_pc01 = S.Task('c_pc01', length=3, delay_cost=1)
	c_pc01 += alt(MAS)
	c_pc01_in = S.Task('c_pc01_in', length=1, delay_cost=1)
	c_pc01_in += alt(MAS_in)
	S += c_pc01_in*MAS_in[0]<=c_pc01*MAS[0]

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	c_pc01_mem0 += alt(MAS_MEM)
	S += (c_bb01*MAS[0])-1 < c_pc01_mem0*MAS_MEM[0]
	S += c_pc01_mem0 <= c_pc01

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	c_pc01_mem1 += alt(MAS_MEM)
	S += (c_ac01*MAS[0])-1 < c_pc01_mem1*MAS_MEM[1]
	S += c_pc01_mem1 <= c_pc01

	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=11, delay_cost=1)
	c_pbc_t0_t0 += alt(MM)
	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	c_pbc_t0_t0_in += alt(MM_in)
	S += c_pbc_t0_t0_in*MM_in[0]<=c_pbc_t0_t0*MM[0]
	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	c_pbc_t0_t0_mem0 += alt(MAS_MEM)
	S += (c_pb00*MAS[0])-1 < c_pbc_t0_t0_mem0*MAS_MEM[0]
	S += c_pbc_t0_t0_mem0 <= c_pbc_t0_t0

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	c_pbc_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_pbc_t0_t0_mem1 <= c_pbc_t0_t0

	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=11, delay_cost=1)
	c_pbc_t0_t1 += alt(MM)
	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	c_pbc_t0_t1_in += alt(MM_in)
	S += c_pbc_t0_t1_in*MM_in[0]<=c_pbc_t0_t1*MM[0]
	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	c_pbc_t0_t1_mem0 += alt(MAS_MEM)
	S += (c_pb01*MAS[0])-1 < c_pbc_t0_t1_mem0*MAS_MEM[0]
	S += c_pbc_t0_t1_mem0 <= c_pbc_t0_t1

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	c_pbc_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_pbc_t0_t1_mem1 <= c_pbc_t0_t1

	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=3, delay_cost=1)
	c_pbc_t0_t2 += alt(MAS)
	c_pbc_t0_t2_in = S.Task('c_pbc_t0_t2_in', length=1, delay_cost=1)
	c_pbc_t0_t2_in += alt(MAS_in)
	S += c_pbc_t0_t2_in*MAS_in[0]<=c_pbc_t0_t2*MAS[0]

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	c_pbc_t0_t2_mem0 += alt(MAS_MEM)
	S += (c_pb00*MAS[0])-1 < c_pbc_t0_t2_mem0*MAS_MEM[0]
	S += c_pbc_t0_t2_mem0 <= c_pbc_t0_t2

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	c_pbc_t0_t2_mem1 += alt(MAS_MEM)
	S += (c_pb01*MAS[0])-1 < c_pbc_t0_t2_mem1*MAS_MEM[1]
	S += c_pbc_t0_t2_mem1 <= c_pbc_t0_t2

	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=11, delay_cost=1)
	c_pcb_t1_t1 += alt(MM)
	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	c_pcb_t1_t1_in += alt(MM_in)
	S += c_pcb_t1_t1_in*MM_in[0]<=c_pcb_t1_t1*MM[0]
	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	c_pcb_t1_t1_mem0 += alt(MAS_MEM)
	S += (c_pc11*MAS[0])-1 < c_pcb_t1_t1_mem0*MAS_MEM[0]
	S += c_pcb_t1_t1_mem0 <= c_pcb_t1_t1

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	c_pcb_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_pcb_t1_t1_mem1 <= c_pcb_t1_t1

	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=3, delay_cost=1)
	c_pcb_t1_t2 += alt(MAS)
	c_pcb_t1_t2_in = S.Task('c_pcb_t1_t2_in', length=1, delay_cost=1)
	c_pcb_t1_t2_in += alt(MAS_in)
	S += c_pcb_t1_t2_in*MAS_in[0]<=c_pcb_t1_t2*MAS[0]

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	c_pcb_t1_t2_mem0 += alt(MAS_MEM)
	S += (c_pc10*MAS[0])-1 < c_pcb_t1_t2_mem0*MAS_MEM[0]
	S += c_pcb_t1_t2_mem0 <= c_pcb_t1_t2

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	c_pcb_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pc11*MAS[0])-1 < c_pcb_t1_t2_mem1*MAS_MEM[1]
	S += c_pcb_t1_t2_mem1 <= c_pcb_t1_t2

	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=11, delay_cost=1)
	c_paa_t1_t0 += alt(MM)
	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	c_paa_t1_t0_in += alt(MM_in)
	S += c_paa_t1_t0_in*MM_in[0]<=c_paa_t1_t0*MM[0]
	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	c_paa_t1_t0_mem0 += alt(MAS_MEM)
	S += (c_pa10*MAS[0])-1 < c_paa_t1_t0_mem0*MAS_MEM[0]
	S += c_paa_t1_t0_mem0 <= c_paa_t1_t0

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	c_paa_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_paa_t1_t0_mem1 <= c_paa_t1_t0

	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=11, delay_cost=1)
	c_paa_t1_t1 += alt(MM)
	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	c_paa_t1_t1_in += alt(MM_in)
	S += c_paa_t1_t1_in*MM_in[0]<=c_paa_t1_t1*MM[0]
	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	c_paa_t1_t1_mem0 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t1_t1_mem0*MAS_MEM[0]
	S += c_paa_t1_t1_mem0 <= c_paa_t1_t1

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	c_paa_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_paa_t1_t1_mem1 <= c_paa_t1_t1

	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=3, delay_cost=1)
	c_paa_t1_t2 += alt(MAS)
	c_paa_t1_t2_in = S.Task('c_paa_t1_t2_in', length=1, delay_cost=1)
	c_paa_t1_t2_in += alt(MAS_in)
	S += c_paa_t1_t2_in*MAS_in[0]<=c_paa_t1_t2*MAS[0]

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	c_paa_t1_t2_mem0 += alt(MAS_MEM)
	S += (c_pa10*MAS[0])-1 < c_paa_t1_t2_mem0*MAS_MEM[0]
	S += c_paa_t1_t2_mem0 <= c_paa_t1_t2

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	c_paa_t1_t2_mem1 += alt(MAS_MEM)
	S += (c_pa11*MAS[0])-1 < c_paa_t1_t2_mem1*MAS_MEM[1]
	S += c_paa_t1_t2_mem1 <= c_paa_t1_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS1/FP12_INV_BEFORE_FPINV/schedule6.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution

