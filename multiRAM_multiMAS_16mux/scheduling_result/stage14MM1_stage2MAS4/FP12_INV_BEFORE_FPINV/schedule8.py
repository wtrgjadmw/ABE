from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 247
	S = Scenario("schedule8", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=14)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
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

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=14, delay_cost=1)
	S += c_aa_t3_t0 >= 1
	c_aa_t3_t0 += MM[0]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 1
	c_aa_t3_t2_in += MAS_in[1]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 1
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 1
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=2, delay_cost=1)
	S += c_aa_t3_t2 >= 2
	c_aa_t3_t2 += MAS[1]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 2
	c_bb_a1_0_in += MAS_in[0]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 2
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 2
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 3
	c_aa_t10_in += MAS_in[0]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 3
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 3
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=2, delay_cost=1)
	S += c_bb_a1_0 >= 3
	c_bb_a1_0 += MAS[0]

	c_aa_t10 = S.Task('c_aa_t10', length=2, delay_cost=1)
	S += c_aa_t10 >= 4
	c_aa_t10 += MAS[0]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 4
	c_bb_a1_1_in += MAS_in[0]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 4
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 4
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=2, delay_cost=1)
	S += c_bb_a1_1 >= 5
	c_bb_a1_1 += MAS[0]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 5
	c_cc_t3_t2_in += MAS_in[0]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 5
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 5
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 6
	c_aa_t11_in += MAS_in[0]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 6
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 6
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=2, delay_cost=1)
	S += c_cc_t3_t2 >= 6
	c_cc_t3_t2 += MAS[0]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 7
	c_aa_a1_0_in += MAS_in[2]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 7
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 7
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_aa_t11 = S.Task('c_aa_t11', length=2, delay_cost=1)
	S += c_aa_t11 >= 7
	c_aa_t11 += MAS[0]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=2, delay_cost=1)
	S += c_aa_a1_0 >= 8
	c_aa_a1_0 += MAS[2]

	c_aa_t2_t3_in = S.Task('c_aa_t2_t3_in', length=1, delay_cost=1)
	S += c_aa_t2_t3_in >= 8
	c_aa_t2_t3_in += MAS_in[1]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 8
	c_aa_t2_t3_mem0 += MAS_MEM[0]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 8
	c_aa_t2_t3_mem1 += MAS_MEM[1]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 8
	c_bb_t3_t2_in += MAS_in[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 8
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 8
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=2, delay_cost=1)
	S += c_aa_t2_t3 >= 9
	c_aa_t2_t3 += MAS[1]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 9
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 9
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 9
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=2, delay_cost=1)
	S += c_bb_t3_t2 >= 9
	c_bb_t3_t2 += MAS[0]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=14, delay_cost=1)
	S += c_aa_t3_t1 >= 10
	c_aa_t3_t1 += MM[0]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 10
	c_cc_a1_1_in += MAS_in[0]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 10
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 10
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 11
	c_aa_t3_t3_in += MAS_in[0]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 11
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 11
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=2, delay_cost=1)
	S += c_cc_a1_1 >= 11
	c_cc_a1_1 += MAS[0]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=2, delay_cost=1)
	S += c_aa_t3_t3 >= 12
	c_aa_t3_t3 += MAS[0]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 12
	c_cc_t10_in += MAS_in[0]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 12
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 12
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 13
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 13
	c_aa_t3_t4_mem0 += MAS_MEM[2]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 13
	c_aa_t3_t4_mem1 += MAS_MEM[1]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 13
	c_bb_t11_in += MAS_in[0]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 13
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 13
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t10 = S.Task('c_cc_t10', length=2, delay_cost=1)
	S += c_cc_t10 >= 13
	c_cc_t10 += MAS[0]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=14, delay_cost=1)
	S += c_aa_t3_t4 >= 14
	c_aa_t3_t4 += MM[0]

	c_bb_t11 = S.Task('c_bb_t11', length=2, delay_cost=1)
	S += c_bb_t11 >= 14
	c_bb_t11 += MAS[0]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 14
	c_cc_t3_t3_in += MAS_in[0]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 14
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 14
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 15
	c_cc_t11_in += MAS_in[0]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 15
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 15
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=2, delay_cost=1)
	S += c_cc_t3_t3 >= 15
	c_cc_t3_t3 += MAS[0]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 16
	c_ab_t0_t2_in += MAS_in[0]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 16
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 16
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=2, delay_cost=1)
	S += c_cc_t11 >= 16
	c_cc_t11 += MAS[0]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 16
	c_cc_t3_t4_in += MM_in[0]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 16
	c_cc_t3_t4_mem0 += MAS_MEM[0]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 16
	c_cc_t3_t4_mem1 += MAS_MEM[1]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 17
	c_aa_a1_1_in += MAS_in[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 17
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 17
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=2, delay_cost=1)
	S += c_ab_t0_t2 >= 17
	c_ab_t0_t2 += MAS[0]

	c_cc_t2_t3_in = S.Task('c_cc_t2_t3_in', length=1, delay_cost=1)
	S += c_cc_t2_t3_in >= 17
	c_cc_t2_t3_in += MAS_in[2]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 17
	c_cc_t2_t3_mem0 += MAS_MEM[0]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 17
	c_cc_t2_t3_mem1 += MAS_MEM[1]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=14, delay_cost=1)
	S += c_cc_t3_t4 >= 17
	c_cc_t3_t4 += MM[0]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=2, delay_cost=1)
	S += c_aa_a1_1 >= 18
	c_aa_a1_1 += MAS[0]

	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 18
	c_ab_t0_t3_in += MAS_in[0]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 18
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 18
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=2, delay_cost=1)
	S += c_cc_t2_t3 >= 18
	c_cc_t2_t3 += MAS[2]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=2, delay_cost=1)
	S += c_ab_t0_t3 >= 19
	c_ab_t0_t3 += MAS[0]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 19
	c_bb_t10_in += MAS_in[3]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 19
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 19
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 20
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 20
	c_ab_t0_t4_mem0 += MAS_MEM[0]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 20
	c_ab_t0_t4_mem1 += MAS_MEM[1]

	c_bb_t10 = S.Task('c_bb_t10', length=2, delay_cost=1)
	S += c_bb_t10 >= 20
	c_bb_t10 += MAS[3]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 20
	c_cc_a1_0_in += MAS_in[0]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 20
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 20
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=14, delay_cost=1)
	S += c_ab_t0_t4 >= 21
	c_ab_t0_t4 += MM[0]

	c_bb_t2_t3_in = S.Task('c_bb_t2_t3_in', length=1, delay_cost=1)
	S += c_bb_t2_t3_in >= 21
	c_bb_t2_t3_in += MAS_in[0]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 21
	c_bb_t2_t3_mem0 += MAS_MEM[6]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 21
	c_bb_t2_t3_mem1 += MAS_MEM[1]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 21
	c_bb_t3_t3_in += MAS_in[1]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 21
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 21
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=2, delay_cost=1)
	S += c_cc_a1_0 >= 21
	c_cc_a1_0 += MAS[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 22
	c_ab_t1_t1_in += MM_in[0]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 22
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 22
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=2, delay_cost=1)
	S += c_bb_t2_t3 >= 22
	c_bb_t2_t3 += MAS[0]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=2, delay_cost=1)
	S += c_bb_t3_t3 >= 22
	c_bb_t3_t3 += MAS[1]

	c_aa_t3_t5_in = S.Task('c_aa_t3_t5_in', length=1, delay_cost=1)
	S += c_aa_t3_t5_in >= 23
	c_aa_t3_t5_in += MAS_in[0]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 23
	c_aa_t3_t5_mem0 += MM_MEM[0]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 23
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 23
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 23
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 23
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=14, delay_cost=1)
	S += c_ab_t1_t1 >= 23
	c_ab_t1_t1 += MM[0]

	c_aa_t30_in = S.Task('c_aa_t30_in', length=1, delay_cost=1)
	S += c_aa_t30_in >= 24
	c_aa_t30_in += MAS_in[3]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 24
	c_aa_t30_mem0 += MM_MEM[0]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 24
	c_aa_t30_mem1 += MM_MEM[1]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=2, delay_cost=1)
	S += c_aa_t3_t5 >= 24
	c_aa_t3_t5 += MAS[0]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 24
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 24
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 24
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=14, delay_cost=1)
	S += c_ab_t1_t0 >= 24
	c_ab_t1_t0 += MM[0]

	c_aa_t30 = S.Task('c_aa_t30', length=2, delay_cost=1)
	S += c_aa_t30 >= 25
	c_aa_t30 += MAS[3]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 25
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 25
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 25
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=14, delay_cost=1)
	S += c_ab_t0_t1 >= 25
	c_ab_t0_t1 += MM[0]

	c_aa10_in = S.Task('c_aa10_in', length=1, delay_cost=1)
	S += c_aa10_in >= 26
	c_aa10_in += MAS_in[2]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 26
	c_aa10_mem0 += MAS_MEM[6]

	c_aa10_mem1 = S.Task('c_aa10_mem1', length=1, delay_cost=1)
	S += c_aa10_mem1 >= 26
	c_aa10_mem1 += MAS_MEM[7]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=14, delay_cost=1)
	S += c_ab_t0_t0 >= 26
	c_ab_t0_t0 += MM[0]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 26
	c_cc_t3_t1_in += MM_in[0]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 26
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 26
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa10 = S.Task('c_aa10', length=2, delay_cost=1)
	S += c_aa10 >= 27
	c_aa10 += MAS[2]

	c_aa_t31_in = S.Task('c_aa_t31_in', length=1, delay_cost=1)
	S += c_aa_t31_in >= 27
	c_aa_t31_in += MAS_in[3]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 27
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 27
	c_aa_t31_mem1 += MAS_MEM[1]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 27
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 27
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 27
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=14, delay_cost=1)
	S += c_cc_t3_t1 >= 27
	c_cc_t3_t1 += MM[0]

	c_aa_t31 = S.Task('c_aa_t31', length=2, delay_cost=1)
	S += c_aa_t31 >= 28
	c_aa_t31 += MAS[3]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 28
	c_bb_t3_t1_in += MM_in[0]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 28
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 28
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=14, delay_cost=1)
	S += c_cc_t3_t0 >= 28
	c_cc_t3_t0 += MM[0]

	c_aa11_in = S.Task('c_aa11_in', length=1, delay_cost=1)
	S += c_aa11_in >= 29
	c_aa11_in += MAS_in[2]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	S += c_aa11_mem0 >= 29
	c_aa11_mem0 += MAS_MEM[6]

	c_aa11_mem1 = S.Task('c_aa11_mem1', length=1, delay_cost=1)
	S += c_aa11_mem1 >= 29
	c_aa11_mem1 += MAS_MEM[7]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 29
	c_bb_t3_t0_in += MM_in[0]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 29
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 29
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=14, delay_cost=1)
	S += c_bb_t3_t1 >= 29
	c_bb_t3_t1 += MM[0]

	c_aa11 = S.Task('c_aa11', length=2, delay_cost=1)
	S += c_aa11 >= 30
	c_aa11 += MAS[2]

	c_aa_t41_in = S.Task('c_aa_t41_in', length=1, delay_cost=1)
	S += c_aa_t41_in >= 30
	c_aa_t41_in += MAS_in[2]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	S += c_aa_t41_mem0 >= 30
	c_aa_t41_mem0 += MAS_MEM[6]

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	S += c_aa_t41_mem1 >= 30
	c_aa_t41_mem1 += MAS_MEM[7]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 30
	c_ab_t1_t2_in += MAS_in[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 30
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 30
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=14, delay_cost=1)
	S += c_bb_t3_t0 >= 30
	c_bb_t3_t0 += MM[0]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 30
	c_bb_t3_t4_in += MM_in[0]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 30
	c_bb_t3_t4_mem0 += MAS_MEM[0]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 30
	c_bb_t3_t4_mem1 += MAS_MEM[3]

	c_aa_t40_in = S.Task('c_aa_t40_in', length=1, delay_cost=1)
	S += c_aa_t40_in >= 31
	c_aa_t40_in += MAS_in[2]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	S += c_aa_t40_mem0 >= 31
	c_aa_t40_mem0 += MAS_MEM[6]

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	S += c_aa_t40_mem1 >= 31
	c_aa_t40_mem1 += MAS_MEM[7]

	c_aa_t41 = S.Task('c_aa_t41', length=2, delay_cost=1)
	S += c_aa_t41 >= 31
	c_aa_t41 += MAS[2]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=2, delay_cost=1)
	S += c_ab_t1_t2 >= 31
	c_ab_t1_t2 += MAS[0]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 31
	c_ab_t21_in += MAS_in[0]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 31
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 31
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=14, delay_cost=1)
	S += c_bb_t3_t4 >= 31
	c_bb_t3_t4 += MM[0]

	c_aa_t40 = S.Task('c_aa_t40', length=2, delay_cost=1)
	S += c_aa_t40 >= 32
	c_aa_t40 += MAS[2]

	c_aa_t51_in = S.Task('c_aa_t51_in', length=1, delay_cost=1)
	S += c_aa_t51_in >= 32
	c_aa_t51_in += MAS_in[0]

	c_aa_t51_mem0 = S.Task('c_aa_t51_mem0', length=1, delay_cost=1)
	S += c_aa_t51_mem0 >= 32
	c_aa_t51_mem0 += MAS_MEM[6]

	c_aa_t51_mem1 = S.Task('c_aa_t51_mem1', length=1, delay_cost=1)
	S += c_aa_t51_mem1 >= 32
	c_aa_t51_mem1 += MAS_MEM[5]

	c_ab_t21 = S.Task('c_ab_t21', length=2, delay_cost=1)
	S += c_ab_t21 >= 32
	c_ab_t21 += MAS[0]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 32
	c_ab_t30_in += MAS_in[2]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 32
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 32
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_aa_t50_in = S.Task('c_aa_t50_in', length=1, delay_cost=1)
	S += c_aa_t50_in >= 33
	c_aa_t50_in += MAS_in[1]

	c_aa_t50_mem0 = S.Task('c_aa_t50_mem0', length=1, delay_cost=1)
	S += c_aa_t50_mem0 >= 33
	c_aa_t50_mem0 += MAS_MEM[6]

	c_aa_t50_mem1 = S.Task('c_aa_t50_mem1', length=1, delay_cost=1)
	S += c_aa_t50_mem1 >= 33
	c_aa_t50_mem1 += MAS_MEM[5]

	c_aa_t51 = S.Task('c_aa_t51', length=2, delay_cost=1)
	S += c_aa_t51 >= 33
	c_aa_t51 += MAS[0]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 33
	c_ab_t20_in += MAS_in[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 33
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 33
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t30 = S.Task('c_ab_t30', length=2, delay_cost=1)
	S += c_ab_t30 >= 33
	c_ab_t30 += MAS[2]

	c_aa_t50 = S.Task('c_aa_t50', length=2, delay_cost=1)
	S += c_aa_t50 >= 34
	c_aa_t50 += MAS[1]

	c_ab_t20 = S.Task('c_ab_t20', length=2, delay_cost=1)
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

	c_ab_t4_t2_in = S.Task('c_ab_t4_t2_in', length=1, delay_cost=1)
	S += c_ab_t4_t2_in >= 35
	c_ab_t4_t2_in += MAS_in[2]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 35
	c_ab_t4_t2_mem0 += MAS_MEM[0]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 35
	c_ab_t4_t2_mem1 += MAS_MEM[1]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 35
	c_bc_t0_t3_in += MAS_in[0]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 35
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 35
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=2, delay_cost=1)
	S += c_bc_t1_t2 >= 35
	c_bc_t1_t2 += MAS[0]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 36
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 36
	c_ab_t4_t0_mem0 += MAS_MEM[0]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 36
	c_ab_t4_t0_mem1 += MAS_MEM[5]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=2, delay_cost=1)
	S += c_ab_t4_t2 >= 36
	c_ab_t4_t2 += MAS[2]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=2, delay_cost=1)
	S += c_bc_t0_t3 >= 36
	c_bc_t0_t3 += MAS[0]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 36
	c_bc_t1_t3_in += MAS_in[0]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 36
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 36
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t5_in = S.Task('c_ab_t1_t5_in', length=1, delay_cost=1)
	S += c_ab_t1_t5_in >= 37
	c_ab_t1_t5_in += MAS_in[3]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 37
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 37
	c_ab_t1_t5_mem1 += MM_MEM[1]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=14, delay_cost=1)
	S += c_ab_t4_t0 >= 37
	c_ab_t4_t0 += MM[0]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 37
	c_bc_t0_t2_in += MAS_in[0]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 37
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 37
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=2, delay_cost=1)
	S += c_bc_t1_t3 >= 37
	c_bc_t1_t3 += MAS[0]

	c_ab_t10_in = S.Task('c_ab_t10_in', length=1, delay_cost=1)
	S += c_ab_t10_in >= 38
	c_ab_t10_in += MAS_in[3]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 38
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 38
	c_ab_t10_mem1 += MM_MEM[1]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=2, delay_cost=1)
	S += c_ab_t1_t5 >= 38
	c_ab_t1_t5 += MAS[3]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 38
	c_ac_t1_t2_in += MAS_in[0]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 38
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 38
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=2, delay_cost=1)
	S += c_bc_t0_t2 >= 38
	c_bc_t0_t2 += MAS[0]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 38
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 38
	c_bc_t1_t4_mem0 += MAS_MEM[0]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 38
	c_bc_t1_t4_mem1 += MAS_MEM[1]

	c_ab_t00_in = S.Task('c_ab_t00_in', length=1, delay_cost=1)
	S += c_ab_t00_in >= 39
	c_ab_t00_in += MAS_in[3]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 39
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 39
	c_ab_t00_mem1 += MM_MEM[1]

	c_ab_t10 = S.Task('c_ab_t10', length=2, delay_cost=1)
	S += c_ab_t10 >= 39
	c_ab_t10 += MAS[3]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=2, delay_cost=1)
	S += c_ac_t1_t2 >= 39
	c_ac_t1_t2 += MAS[0]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 39
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 39
	c_bc_t0_t4_mem0 += MAS_MEM[0]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 39
	c_bc_t0_t4_mem1 += MAS_MEM[1]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=14, delay_cost=1)
	S += c_bc_t1_t4 >= 39
	c_bc_t1_t4 += MM[0]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 39
	c_bc_t30_in += MAS_in[0]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 39
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 39
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t00 = S.Task('c_ab_t00', length=2, delay_cost=1)
	S += c_ab_t00 >= 40
	c_ab_t00 += MAS[3]

	c_ab_t0_t5_in = S.Task('c_ab_t0_t5_in', length=1, delay_cost=1)
	S += c_ab_t0_t5_in >= 40
	c_ab_t0_t5_in += MAS_in[3]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 40
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 40
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 40
	c_ab_t31_in += MAS_in[0]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 40
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 40
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=14, delay_cost=1)
	S += c_bc_t0_t4 >= 40
	c_bc_t0_t4 += MM[0]

	c_bc_t30 = S.Task('c_bc_t30', length=2, delay_cost=1)
	S += c_bc_t30 >= 40
	c_bc_t30 += MAS[0]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=2, delay_cost=1)
	S += c_ab_t0_t5 >= 41
	c_ab_t0_t5 += MAS[3]

	c_ab_t31 = S.Task('c_ab_t31', length=2, delay_cost=1)
	S += c_ab_t31 >= 41
	c_ab_t31 += MAS[0]

	c_ab_t50_in = S.Task('c_ab_t50_in', length=1, delay_cost=1)
	S += c_ab_t50_in >= 41
	c_ab_t50_in += MAS_in[3]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 41
	c_ab_t50_mem0 += MAS_MEM[6]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 41
	c_ab_t50_mem1 += MAS_MEM[7]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 41
	c_ac_t30_in += MAS_in[0]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 41
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 41
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t5_in = S.Task('c_cc_t3_t5_in', length=1, delay_cost=1)
	S += c_cc_t3_t5_in >= 41
	c_cc_t3_t5_in += MAS_in[1]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 41
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 41
	c_cc_t3_t5_mem1 += MM_MEM[1]

	c_ab_t4_t3_in = S.Task('c_ab_t4_t3_in', length=1, delay_cost=1)
	S += c_ab_t4_t3_in >= 42
	c_ab_t4_t3_in += MAS_in[3]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 42
	c_ab_t4_t3_mem0 += MAS_MEM[4]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 42
	c_ab_t4_t3_mem1 += MAS_MEM[1]

	c_ab_t50 = S.Task('c_ab_t50', length=2, delay_cost=1)
	S += c_ab_t50 >= 42
	c_ab_t50 += MAS[3]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 42
	c_ac_t1_t3_in += MAS_in[0]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 42
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 42
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t30 = S.Task('c_ac_t30', length=2, delay_cost=1)
	S += c_ac_t30 >= 42
	c_ac_t30 += MAS[0]

	c_cc_t30_in = S.Task('c_cc_t30_in', length=1, delay_cost=1)
	S += c_cc_t30_in >= 42
	c_cc_t30_in += MAS_in[2]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 42
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 42
	c_cc_t30_mem1 += MM_MEM[1]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=2, delay_cost=1)
	S += c_cc_t3_t5 >= 42
	c_cc_t3_t5 += MAS[1]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 43
	c_ab_t4_t1_in += MM_in[0]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 43
	c_ab_t4_t1_mem0 += MAS_MEM[0]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 43
	c_ab_t4_t1_mem1 += MAS_MEM[1]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=2, delay_cost=1)
	S += c_ab_t4_t3 >= 43
	c_ab_t4_t3 += MAS[3]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=2, delay_cost=1)
	S += c_ac_t1_t3 >= 43
	c_ac_t1_t3 += MAS[0]

	c_bb_t3_t5_in = S.Task('c_bb_t3_t5_in', length=1, delay_cost=1)
	S += c_bb_t3_t5_in >= 43
	c_bb_t3_t5_in += MAS_in[3]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 43
	c_bb_t3_t5_mem0 += MM_MEM[0]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 43
	c_bb_t3_t5_mem1 += MM_MEM[1]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 43
	c_bc_t21_in += MAS_in[0]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 43
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 43
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_cc_t30 = S.Task('c_cc_t30', length=2, delay_cost=1)
	S += c_cc_t30 >= 43
	c_cc_t30 += MAS[2]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 44
	c_ab_t1_t3_in += MAS_in[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 44
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 44
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=14, delay_cost=1)
	S += c_ab_t4_t1 >= 44
	c_ab_t4_t1 += MM[0]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 44
	c_ac_t1_t4_in += MM_in[0]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 44
	c_ac_t1_t4_mem0 += MAS_MEM[0]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 44
	c_ac_t1_t4_mem1 += MAS_MEM[1]

	c_bb_t30_in = S.Task('c_bb_t30_in', length=1, delay_cost=1)
	S += c_bb_t30_in >= 44
	c_bb_t30_in += MAS_in[1]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 44
	c_bb_t30_mem0 += MM_MEM[0]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 44
	c_bb_t30_mem1 += MM_MEM[1]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=2, delay_cost=1)
	S += c_bb_t3_t5 >= 44
	c_bb_t3_t5 += MAS[3]

	c_bc_t21 = S.Task('c_bc_t21', length=2, delay_cost=1)
	S += c_bc_t21 >= 44
	c_bc_t21 += MAS[0]

	c_cc10_in = S.Task('c_cc10_in', length=1, delay_cost=1)
	S += c_cc10_in >= 44
	c_cc10_in += MAS_in[2]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 44
	c_cc10_mem0 += MAS_MEM[4]

	c_cc10_mem1 = S.Task('c_cc10_mem1', length=1, delay_cost=1)
	S += c_cc10_mem1 >= 44
	c_cc10_mem1 += MAS_MEM[5]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=2, delay_cost=1)
	S += c_ab_t1_t3 >= 45
	c_ab_t1_t3 += MAS[0]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 45
	c_ab_t4_t4_in += MM_in[0]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 45
	c_ab_t4_t4_mem0 += MAS_MEM[4]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 45
	c_ab_t4_t4_mem1 += MAS_MEM[7]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 45
	c_ac_t0_t2_in += MAS_in[0]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 45
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 45
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=14, delay_cost=1)
	S += c_ac_t1_t4 >= 45
	c_ac_t1_t4 += MM[0]

	c_bb_t30 = S.Task('c_bb_t30', length=2, delay_cost=1)
	S += c_bb_t30 >= 45
	c_bb_t30 += MAS[1]

	c_cc10 = S.Task('c_cc10', length=2, delay_cost=1)
	S += c_cc10 >= 45
	c_cc10 += MAS[2]

	c_cc_t31_in = S.Task('c_cc_t31_in', length=1, delay_cost=1)
	S += c_cc_t31_in >= 45
	c_cc_t31_in += MAS_in[1]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 45
	c_cc_t31_mem0 += MM_MEM[0]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 45
	c_cc_t31_mem1 += MAS_MEM[3]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 46
	c_ab_t1_t4_in += MM_in[0]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 46
	c_ab_t1_t4_mem0 += MAS_MEM[0]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 46
	c_ab_t1_t4_mem1 += MAS_MEM[1]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=14, delay_cost=1)
	S += c_ab_t4_t4 >= 46
	c_ab_t4_t4 += MM[0]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=2, delay_cost=1)
	S += c_ac_t0_t2 >= 46
	c_ac_t0_t2 += MAS[0]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 46
	c_ac_t21_in += MAS_in[0]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 46
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 46
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_bb10_in = S.Task('c_bb10_in', length=1, delay_cost=1)
	S += c_bb10_in >= 46
	c_bb10_in += MAS_in[2]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 46
	c_bb10_mem0 += MAS_MEM[2]

	c_bb10_mem1 = S.Task('c_bb10_mem1', length=1, delay_cost=1)
	S += c_bb10_mem1 >= 46
	c_bb10_mem1 += MAS_MEM[3]

	c_bb_t31_in = S.Task('c_bb_t31_in', length=1, delay_cost=1)
	S += c_bb_t31_in >= 46
	c_bb_t31_in += MAS_in[3]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 46
	c_bb_t31_mem0 += MM_MEM[0]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 46
	c_bb_t31_mem1 += MAS_MEM[7]

	c_cc_t31 = S.Task('c_cc_t31', length=2, delay_cost=1)
	S += c_cc_t31 >= 46
	c_cc_t31 += MAS[1]

	c_ab_t01_in = S.Task('c_ab_t01_in', length=1, delay_cost=1)
	S += c_ab_t01_in >= 47
	c_ab_t01_in += MAS_in[0]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 47
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 47
	c_ab_t01_mem1 += MAS_MEM[7]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=14, delay_cost=1)
	S += c_ab_t1_t4 >= 47
	c_ab_t1_t4 += MM[0]

	c_ac_t21 = S.Task('c_ac_t21', length=2, delay_cost=1)
	S += c_ac_t21 >= 47
	c_ac_t21 += MAS[0]

	c_bb10 = S.Task('c_bb10', length=2, delay_cost=1)
	S += c_bb10 >= 47
	c_bb10 += MAS[2]

	c_bb_t31 = S.Task('c_bb_t31', length=2, delay_cost=1)
	S += c_bb_t31 >= 47
	c_bb_t31 += MAS[3]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 47
	c_bc_t20_in += MAS_in[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 47
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 47
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_cc_t40_in = S.Task('c_cc_t40_in', length=1, delay_cost=1)
	S += c_cc_t40_in >= 47
	c_cc_t40_in += MAS_in[3]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	S += c_cc_t40_mem0 >= 47
	c_cc_t40_mem0 += MAS_MEM[4]

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	S += c_cc_t40_mem1 >= 47
	c_cc_t40_mem1 += MAS_MEM[3]

	c_cc_t41_in = S.Task('c_cc_t41_in', length=1, delay_cost=1)
	S += c_cc_t41_in >= 47
	c_cc_t41_in += MAS_in[2]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	S += c_cc_t41_mem0 >= 47
	c_cc_t41_mem0 += MAS_MEM[2]

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	S += c_cc_t41_mem1 >= 47
	c_cc_t41_mem1 += MAS_MEM[5]

	c_ab_t01 = S.Task('c_ab_t01', length=2, delay_cost=1)
	S += c_ab_t01 >= 48
	c_ab_t01 += MAS[0]

	c_bb11_in = S.Task('c_bb11_in', length=1, delay_cost=1)
	S += c_bb11_in >= 48
	c_bb11_in += MAS_in[0]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	S += c_bb11_mem0 >= 48
	c_bb11_mem0 += MAS_MEM[6]

	c_bb11_mem1 = S.Task('c_bb11_mem1', length=1, delay_cost=1)
	S += c_bb11_mem1 >= 48
	c_bb11_mem1 += MAS_MEM[7]

	c_bc_t20 = S.Task('c_bc_t20', length=2, delay_cost=1)
	S += c_bc_t20 >= 48
	c_bc_t20 += MAS[1]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 48
	c_bc_t31_in += MAS_in[2]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 48
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 48
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_cc11_in = S.Task('c_cc11_in', length=1, delay_cost=1)
	S += c_cc11_in >= 48
	c_cc11_in += MAS_in[1]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	S += c_cc11_mem0 >= 48
	c_cc11_mem0 += MAS_MEM[2]

	c_cc11_mem1 = S.Task('c_cc11_mem1', length=1, delay_cost=1)
	S += c_cc11_mem1 >= 48
	c_cc11_mem1 += MAS_MEM[3]

	c_cc_t40 = S.Task('c_cc_t40', length=2, delay_cost=1)
	S += c_cc_t40 >= 48
	c_cc_t40 += MAS[3]

	c_cc_t41 = S.Task('c_cc_t41', length=2, delay_cost=1)
	S += c_cc_t41 >= 48
	c_cc_t41 += MAS[2]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 49
	c_ac_t20_in += MAS_in[2]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 49
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 49
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_bb11 = S.Task('c_bb11', length=2, delay_cost=1)
	S += c_bb11 >= 49
	c_bb11 += MAS[0]

	c_bb_t41_in = S.Task('c_bb_t41_in', length=1, delay_cost=1)
	S += c_bb_t41_in >= 49
	c_bb_t41_in += MAS_in[1]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	S += c_bb_t41_mem0 >= 49
	c_bb_t41_mem0 += MAS_MEM[6]

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	S += c_bb_t41_mem1 >= 49
	c_bb_t41_mem1 += MAS_MEM[3]

	c_bc_t31 = S.Task('c_bc_t31', length=2, delay_cost=1)
	S += c_bc_t31 >= 49
	c_bc_t31 += MAS[2]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 49
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 49
	c_bc_t4_t0_mem0 += MAS_MEM[2]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 49
	c_bc_t4_t0_mem1 += MAS_MEM[1]

	c_cc11 = S.Task('c_cc11', length=2, delay_cost=1)
	S += c_cc11 >= 49
	c_cc11 += MAS[1]

	c_cc_t50_in = S.Task('c_cc_t50_in', length=1, delay_cost=1)
	S += c_cc_t50_in >= 49
	c_cc_t50_in += MAS_in[0]

	c_cc_t50_mem0 = S.Task('c_cc_t50_mem0', length=1, delay_cost=1)
	S += c_cc_t50_mem0 >= 49
	c_cc_t50_mem0 += MAS_MEM[4]

	c_cc_t50_mem1 = S.Task('c_cc_t50_mem1', length=1, delay_cost=1)
	S += c_cc_t50_mem1 >= 49
	c_cc_t50_mem1 += MAS_MEM[7]

	c_ac_t20 = S.Task('c_ac_t20', length=2, delay_cost=1)
	S += c_ac_t20 >= 50
	c_ac_t20 += MAS[2]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 50
	c_ac_t31_in += MAS_in[2]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 50
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 50
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_bb_t41 = S.Task('c_bb_t41', length=2, delay_cost=1)
	S += c_bb_t41 >= 50
	c_bb_t41 += MAS[1]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=14, delay_cost=1)
	S += c_bc_t4_t0 >= 50
	c_bc_t4_t0 += MM[0]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 50
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 50
	c_bc_t4_t1_mem0 += MAS_MEM[0]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 50
	c_bc_t4_t1_mem1 += MAS_MEM[5]

	c_bc_t4_t2_in = S.Task('c_bc_t4_t2_in', length=1, delay_cost=1)
	S += c_bc_t4_t2_in >= 50
	c_bc_t4_t2_in += MAS_in[1]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 50
	c_bc_t4_t2_mem0 += MAS_MEM[2]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 50
	c_bc_t4_t2_mem1 += MAS_MEM[1]

	c_cc_t50 = S.Task('c_cc_t50', length=2, delay_cost=1)
	S += c_cc_t50 >= 50
	c_cc_t50 += MAS[0]

	c_ccxi_y1_0_in = S.Task('c_ccxi_y1_0_in', length=1, delay_cost=1)
	S += c_ccxi_y1_0_in >= 50
	c_ccxi_y1_0_in += MAS_in[0]

	c_ccxi_y1_0_mem0 = S.Task('c_ccxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem0 >= 50
	c_ccxi_y1_0_mem0 += MAS_MEM[4]

	c_ccxi_y1_0_mem1 = S.Task('c_ccxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_0_mem1 >= 50
	c_ccxi_y1_0_mem1 += MAS_MEM[3]

	c_ac_t31 = S.Task('c_ac_t31', length=2, delay_cost=1)
	S += c_ac_t31 >= 51
	c_ac_t31 += MAS[2]

	c_ac_t4_t2_in = S.Task('c_ac_t4_t2_in', length=1, delay_cost=1)
	S += c_ac_t4_t2_in >= 51
	c_ac_t4_t2_in += MAS_in[2]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 51
	c_ac_t4_t2_mem0 += MAS_MEM[4]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 51
	c_ac_t4_t2_mem1 += MAS_MEM[1]

	c_bb_t40_in = S.Task('c_bb_t40_in', length=1, delay_cost=1)
	S += c_bb_t40_in >= 51
	c_bb_t40_in += MAS_in[0]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	S += c_bb_t40_mem0 >= 51
	c_bb_t40_mem0 += MAS_MEM[2]

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	S += c_bb_t40_mem1 >= 51
	c_bb_t40_mem1 += MAS_MEM[7]

	c_bb_t51_in = S.Task('c_bb_t51_in', length=1, delay_cost=1)
	S += c_bb_t51_in >= 51
	c_bb_t51_in += MAS_in[3]

	c_bb_t51_mem0 = S.Task('c_bb_t51_mem0', length=1, delay_cost=1)
	S += c_bb_t51_mem0 >= 51
	c_bb_t51_mem0 += MAS_MEM[6]

	c_bb_t51_mem1 = S.Task('c_bb_t51_mem1', length=1, delay_cost=1)
	S += c_bb_t51_mem1 >= 51
	c_bb_t51_mem1 += MAS_MEM[3]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 51
	c_bc_t0_t1_in += MM_in[0]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 51
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 51
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=14, delay_cost=1)
	S += c_bc_t4_t1 >= 51
	c_bc_t4_t1 += MM[0]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=2, delay_cost=1)
	S += c_bc_t4_t2 >= 51
	c_bc_t4_t2 += MAS[1]

	c_bc_t4_t3_in = S.Task('c_bc_t4_t3_in', length=1, delay_cost=1)
	S += c_bc_t4_t3_in >= 51
	c_bc_t4_t3_in += MAS_in[1]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 51
	c_bc_t4_t3_mem0 += MAS_MEM[0]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 51
	c_bc_t4_t3_mem1 += MAS_MEM[5]

	c_ccxi_y1_0 = S.Task('c_ccxi_y1_0', length=2, delay_cost=1)
	S += c_ccxi_y1_0 >= 51
	c_ccxi_y1_0 += MAS[0]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=2, delay_cost=1)
	S += c_ac_t4_t2 >= 52
	c_ac_t4_t2 += MAS[2]

	c_ac_t4_t3_in = S.Task('c_ac_t4_t3_in', length=1, delay_cost=1)
	S += c_ac_t4_t3_in >= 52
	c_ac_t4_t3_in += MAS_in[2]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 52
	c_ac_t4_t3_mem0 += MAS_MEM[0]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 52
	c_ac_t4_t3_mem1 += MAS_MEM[5]

	c_bb_t40 = S.Task('c_bb_t40', length=2, delay_cost=1)
	S += c_bb_t40 >= 52
	c_bb_t40 += MAS[0]

	c_bb_t51 = S.Task('c_bb_t51', length=2, delay_cost=1)
	S += c_bb_t51 >= 52
	c_bb_t51 += MAS[3]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 52
	c_bc_t0_t0_in += MM_in[0]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 52
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 52
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=14, delay_cost=1)
	S += c_bc_t0_t1 >= 52
	c_bc_t0_t1 += MM[0]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=2, delay_cost=1)
	S += c_bc_t4_t3 >= 52
	c_bc_t4_t3 += MAS[1]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 53
	c_ac_t1_t1_in += MM_in[0]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 53
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 53
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=2, delay_cost=1)
	S += c_ac_t4_t3 >= 53
	c_ac_t4_t3 += MAS[2]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=14, delay_cost=1)
	S += c_bc_t0_t0 >= 53
	c_bc_t0_t0 += MM[0]

	c_ccxi_y1_1_in = S.Task('c_ccxi_y1_1_in', length=1, delay_cost=1)
	S += c_ccxi_y1_1_in >= 53
	c_ccxi_y1_1_in += MAS_in[0]

	c_ccxi_y1_1_mem0 = S.Task('c_ccxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem0 >= 53
	c_ccxi_y1_1_mem0 += MAS_MEM[2]

	c_ccxi_y1_1_mem1 = S.Task('c_ccxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_ccxi_y1_1_mem1 >= 53
	c_ccxi_y1_1_mem1 += MAS_MEM[5]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 54
	c_ac_t0_t3_in += MAS_in[2]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 54
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 54
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=14, delay_cost=1)
	S += c_ac_t1_t1 >= 54
	c_ac_t1_t1 += MM[0]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 54
	c_ac_t4_t1_in += MM_in[0]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 54
	c_ac_t4_t1_mem0 += MAS_MEM[0]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 54
	c_ac_t4_t1_mem1 += MAS_MEM[5]

	c_bb_t50_in = S.Task('c_bb_t50_in', length=1, delay_cost=1)
	S += c_bb_t50_in >= 54
	c_bb_t50_in += MAS_in[1]

	c_bb_t50_mem0 = S.Task('c_bb_t50_mem0', length=1, delay_cost=1)
	S += c_bb_t50_mem0 >= 54
	c_bb_t50_mem0 += MAS_MEM[2]

	c_bb_t50_mem1 = S.Task('c_bb_t50_mem1', length=1, delay_cost=1)
	S += c_bb_t50_mem1 >= 54
	c_bb_t50_mem1 += MAS_MEM[1]

	c_ccxi_y1_1 = S.Task('c_ccxi_y1_1', length=2, delay_cost=1)
	S += c_ccxi_y1_1 >= 54
	c_ccxi_y1_1 += MAS[0]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=2, delay_cost=1)
	S += c_ac_t0_t3 >= 55
	c_ac_t0_t3 += MAS[2]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 55
	c_ac_t1_t0_in += MM_in[0]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 55
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 55
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=14, delay_cost=1)
	S += c_ac_t4_t1 >= 55
	c_ac_t4_t1 += MM[0]

	c_bb_t50 = S.Task('c_bb_t50', length=2, delay_cost=1)
	S += c_bb_t50 >= 55
	c_bb_t50 += MAS[1]

	c_cc_t51_in = S.Task('c_cc_t51_in', length=1, delay_cost=1)
	S += c_cc_t51_in >= 55
	c_cc_t51_in += MAS_in[1]

	c_cc_t51_mem0 = S.Task('c_cc_t51_mem0', length=1, delay_cost=1)
	S += c_cc_t51_mem0 >= 55
	c_cc_t51_mem0 += MAS_MEM[2]

	c_cc_t51_mem1 = S.Task('c_cc_t51_mem1', length=1, delay_cost=1)
	S += c_cc_t51_mem1 >= 55
	c_cc_t51_mem1 += MAS_MEM[5]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 56
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 56
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 56
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=14, delay_cost=1)
	S += c_ac_t1_t0 >= 56
	c_ac_t1_t0 += MM[0]

	c_cc_t51 = S.Task('c_cc_t51', length=2, delay_cost=1)
	S += c_cc_t51 >= 56
	c_cc_t51 += MAS[1]

	c_ab_t4_t5_in = S.Task('c_ab_t4_t5_in', length=1, delay_cost=1)
	S += c_ab_t4_t5_in >= 57
	c_ab_t4_t5_in += MAS_in[1]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 57
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 57
	c_ab_t4_t5_mem1 += MM_MEM[1]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 57
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 57
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 57
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=14, delay_cost=1)
	S += c_ac_t0_t1 >= 57
	c_ac_t0_t1 += MM[0]

	c_ab_t40_in = S.Task('c_ab_t40_in', length=1, delay_cost=1)
	S += c_ab_t40_in >= 58
	c_ab_t40_in += MAS_in[2]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 58
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 58
	c_ab_t40_mem1 += MM_MEM[1]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=2, delay_cost=1)
	S += c_ab_t4_t5 >= 58
	c_ab_t4_t5 += MAS[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=14, delay_cost=1)
	S += c_ac_t0_t0 >= 58
	c_ac_t0_t0 += MM[0]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 58
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 58
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 58
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t40 = S.Task('c_ab_t40', length=2, delay_cost=1)
	S += c_ab_t40 >= 59
	c_ab_t40 += MAS[2]

	c_ab_t41_in = S.Task('c_ab_t41_in', length=1, delay_cost=1)
	S += c_ab_t41_in >= 59
	c_ab_t41_in += MAS_in[1]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	S += c_ab_t41_mem0 >= 59
	c_ab_t41_mem0 += MM_MEM[0]

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	S += c_ab_t41_mem1 >= 59
	c_ab_t41_mem1 += MAS_MEM[3]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 59
	c_bc_t1_t0_in += MM_in[0]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 59
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 59
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=14, delay_cost=1)
	S += c_bc_t1_t1 >= 59
	c_bc_t1_t1 += MM[0]

	c_ab_t11_in = S.Task('c_ab_t11_in', length=1, delay_cost=1)
	S += c_ab_t11_in >= 60
	c_ab_t11_in += MAS_in[3]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 60
	c_ab_t11_mem0 += MM_MEM[0]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 60
	c_ab_t11_mem1 += MAS_MEM[7]

	c_ab_t41 = S.Task('c_ab_t41', length=2, delay_cost=1)
	S += c_ab_t41 >= 60
	c_ab_t41 += MAS[1]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 60
	c_ac_t0_t4_in += MM_in[0]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 60
	c_ac_t0_t4_mem0 += MAS_MEM[0]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 60
	c_ac_t0_t4_mem1 += MAS_MEM[5]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=14, delay_cost=1)
	S += c_bc_t1_t0 >= 60
	c_bc_t1_t0 += MM[0]

	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	S += c_pbc_t0_t3_in >= 60
	c_pbc_t0_t3_in += MAS_in[0]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 60
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 60
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t11 = S.Task('c_ab_t11', length=2, delay_cost=1)
	S += c_ab_t11 >= 61
	c_ab_t11 += MAS[3]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=14, delay_cost=1)
	S += c_ac_t0_t4 >= 61
	c_ac_t0_t4 += MM[0]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 61
	c_ac_t4_t0_in += MM_in[0]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 61
	c_ac_t4_t0_mem0 += MAS_MEM[4]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 61
	c_ac_t4_t0_mem1 += MAS_MEM[1]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=2, delay_cost=1)
	S += c_pbc_t0_t3 >= 61
	c_pbc_t0_t3 += MAS[0]

	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	S += c_pbc_t30_in >= 61
	c_pbc_t30_in += MAS_in[0]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 61
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 61
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t51_in = S.Task('c_ab_t51_in', length=1, delay_cost=1)
	S += c_ab_t51_in >= 62
	c_ab_t51_in += MAS_in[2]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	S += c_ab_t51_mem0 >= 62
	c_ab_t51_mem0 += MAS_MEM[0]

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	S += c_ab_t51_mem1 >= 62
	c_ab_t51_mem1 += MAS_MEM[7]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=14, delay_cost=1)
	S += c_ac_t4_t0 >= 62
	c_ac_t4_t0 += MM[0]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 62
	c_ac_t4_t4_in += MM_in[0]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 62
	c_ac_t4_t4_mem0 += MAS_MEM[4]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 62
	c_ac_t4_t4_mem1 += MAS_MEM[5]

	c_pbc_t30 = S.Task('c_pbc_t30', length=2, delay_cost=1)
	S += c_pbc_t30 >= 62
	c_pbc_t30 += MAS[0]

	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	S += c_pcb_t0_t3_in >= 62
	c_pcb_t0_t3_in += MAS_in[0]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 62
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 62
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_s01_in = S.Task('c_ab_s01_in', length=1, delay_cost=1)
	S += c_ab_s01_in >= 63
	c_ab_s01_in += MAS_in[1]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	S += c_ab_s01_mem0 >= 63
	c_ab_s01_mem0 += MAS_MEM[6]

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	S += c_ab_s01_mem1 >= 63
	c_ab_s01_mem1 += MAS_MEM[7]

	c_ab_t51 = S.Task('c_ab_t51', length=2, delay_cost=1)
	S += c_ab_t51 >= 63
	c_ab_t51 += MAS[2]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=14, delay_cost=1)
	S += c_ac_t4_t4 >= 63
	c_ac_t4_t4 += MM[0]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 63
	c_bc_t4_t4_in += MM_in[0]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 63
	c_bc_t4_t4_mem0 += MAS_MEM[2]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 63
	c_bc_t4_t4_mem1 += MAS_MEM[3]

	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	S += c_paa_t0_t3_in >= 63
	c_paa_t0_t3_in += MAS_in[3]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 63
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 63
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=2, delay_cost=1)
	S += c_pcb_t0_t3 >= 63
	c_pcb_t0_t3 += MAS[0]

	c_ab10_in = S.Task('c_ab10_in', length=1, delay_cost=1)
	S += c_ab10_in >= 64
	c_ab10_in += MAS_in[2]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	S += c_ab10_mem0 >= 64
	c_ab10_mem0 += MAS_MEM[4]

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	S += c_ab10_mem1 >= 64
	c_ab10_mem1 += MAS_MEM[7]

	c_ab11_in = S.Task('c_ab11_in', length=1, delay_cost=1)
	S += c_ab11_in >= 64
	c_ab11_in += MAS_in[1]

	c_ab11_mem0 = S.Task('c_ab11_mem0', length=1, delay_cost=1)
	S += c_ab11_mem0 >= 64
	c_ab11_mem0 += MAS_MEM[2]

	c_ab11_mem1 = S.Task('c_ab11_mem1', length=1, delay_cost=1)
	S += c_ab11_mem1 >= 64
	c_ab11_mem1 += MAS_MEM[5]

	c_ab_s01 = S.Task('c_ab_s01', length=2, delay_cost=1)
	S += c_ab_s01 >= 64
	c_ab_s01 += MAS[1]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=14, delay_cost=1)
	S += c_bc_t4_t4 >= 64
	c_bc_t4_t4 += MM[0]

	c_bc_t4_t5_in = S.Task('c_bc_t4_t5_in', length=1, delay_cost=1)
	S += c_bc_t4_t5_in >= 64
	c_bc_t4_t5_in += MAS_in[0]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 64
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 64
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=2, delay_cost=1)
	S += c_paa_t0_t3 >= 64
	c_paa_t0_t3 += MAS[3]

	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	S += c_pbc_t1_t3_in >= 64
	c_pbc_t1_t3_in += MAS_in[3]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 64
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 64
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ab01_in = S.Task('c_ab01_in', length=1, delay_cost=1)
	S += c_ab01_in >= 65
	c_ab01_in += MAS_in[2]

	c_ab01_mem0 = S.Task('c_ab01_mem0', length=1, delay_cost=1)
	S += c_ab01_mem0 >= 65
	c_ab01_mem0 += MAS_MEM[0]

	c_ab01_mem1 = S.Task('c_ab01_mem1', length=1, delay_cost=1)
	S += c_ab01_mem1 >= 65
	c_ab01_mem1 += MAS_MEM[3]

	c_ab10 = S.Task('c_ab10', length=2, delay_cost=1)
	S += c_ab10 >= 65
	c_ab10 += MAS[2]

	c_ab11 = S.Task('c_ab11', length=2, delay_cost=1)
	S += c_ab11 >= 65
	c_ab11 += MAS[1]

	c_ab_s00_in = S.Task('c_ab_s00_in', length=1, delay_cost=1)
	S += c_ab_s00_in >= 65
	c_ab_s00_in += MAS_in[0]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	S += c_ab_s00_mem0 >= 65
	c_ab_s00_mem0 += MAS_MEM[6]

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	S += c_ab_s00_mem1 >= 65
	c_ab_s00_mem1 += MAS_MEM[7]

	c_bc_t40_in = S.Task('c_bc_t40_in', length=1, delay_cost=1)
	S += c_bc_t40_in >= 65
	c_bc_t40_in += MAS_in[3]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 65
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 65
	c_bc_t40_mem1 += MM_MEM[1]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=2, delay_cost=1)
	S += c_bc_t4_t5 >= 65
	c_bc_t4_t5 += MAS[0]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=2, delay_cost=1)
	S += c_pbc_t1_t3 >= 65
	c_pbc_t1_t3 += MAS[3]

	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	S += c_pcb_t31_in >= 65
	c_pcb_t31_in += MAS_in[1]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 65
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 65
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_ab01 = S.Task('c_ab01', length=2, delay_cost=1)
	S += c_ab01 >= 66
	c_ab01 += MAS[2]

	c_ab_s00 = S.Task('c_ab_s00', length=2, delay_cost=1)
	S += c_ab_s00 >= 66
	c_ab_s00 += MAS[0]

	c_bc_t0_t5_in = S.Task('c_bc_t0_t5_in', length=1, delay_cost=1)
	S += c_bc_t0_t5_in >= 66
	c_bc_t0_t5_in += MAS_in[0]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 66
	c_bc_t0_t5_mem0 += MM_MEM[0]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 66
	c_bc_t0_t5_mem1 += MM_MEM[1]

	c_bc_t40 = S.Task('c_bc_t40', length=2, delay_cost=1)
	S += c_bc_t40 >= 66
	c_bc_t40 += MAS[3]

	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	S += c_pcb_t1_t3_in >= 66
	c_pcb_t1_t3_in += MAS_in[3]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 66
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 66
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t31 = S.Task('c_pcb_t31', length=2, delay_cost=1)
	S += c_pcb_t31 >= 66
	c_pcb_t31 += MAS[1]

	c_ab00_in = S.Task('c_ab00_in', length=1, delay_cost=1)
	S += c_ab00_in >= 67
	c_ab00_in += MAS_in[2]

	c_ab00_mem0 = S.Task('c_ab00_mem0', length=1, delay_cost=1)
	S += c_ab00_mem0 >= 67
	c_ab00_mem0 += MAS_MEM[6]

	c_ab00_mem1 = S.Task('c_ab00_mem1', length=1, delay_cost=1)
	S += c_ab00_mem1 >= 67
	c_ab00_mem1 += MAS_MEM[1]

	c_bc_t00_in = S.Task('c_bc_t00_in', length=1, delay_cost=1)
	S += c_bc_t00_in >= 67
	c_bc_t00_in += MAS_in[1]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 67
	c_bc_t00_mem0 += MM_MEM[0]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 67
	c_bc_t00_mem1 += MM_MEM[1]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=2, delay_cost=1)
	S += c_bc_t0_t5 >= 67
	c_bc_t0_t5 += MAS[0]

	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	S += c_paa_t1_t3_in >= 67
	c_paa_t1_t3_in += MAS_in[0]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 67
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 67
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pb01_in = S.Task('c_pb01_in', length=1, delay_cost=1)
	S += c_pb01_in >= 67
	c_pb01_in += MAS_in[3]

	c_pb01_mem0 = S.Task('c_pb01_mem0', length=1, delay_cost=1)
	S += c_pb01_mem0 >= 67
	c_pb01_mem0 += MAS_MEM[0]

	c_pb01_mem1 = S.Task('c_pb01_mem1', length=1, delay_cost=1)
	S += c_pb01_mem1 >= 67
	c_pb01_mem1 += MAS_MEM[5]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=2, delay_cost=1)
	S += c_pcb_t1_t3 >= 67
	c_pcb_t1_t3 += MAS[3]

	c_ab00 = S.Task('c_ab00', length=2, delay_cost=1)
	S += c_ab00 >= 68
	c_ab00 += MAS[2]

	c_bc_t00 = S.Task('c_bc_t00', length=2, delay_cost=1)
	S += c_bc_t00 >= 68
	c_bc_t00 += MAS[1]

	c_bc_t01_in = S.Task('c_bc_t01_in', length=1, delay_cost=1)
	S += c_bc_t01_in >= 68
	c_bc_t01_in += MAS_in[0]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 68
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 68
	c_bc_t01_mem1 += MAS_MEM[1]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=2, delay_cost=1)
	S += c_paa_t1_t3 >= 68
	c_paa_t1_t3 += MAS[0]

	c_pb01 = S.Task('c_pb01', length=2, delay_cost=1)
	S += c_pb01 >= 68
	c_pb01 += MAS[3]

	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	S += c_pbc_t31_in >= 68
	c_pbc_t31_in += MAS_in[3]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 68
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 68
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t10_in = S.Task('c_ac_t10_in', length=1, delay_cost=1)
	S += c_ac_t10_in >= 69
	c_ac_t10_in += MAS_in[1]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 69
	c_ac_t10_mem0 += MM_MEM[0]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 69
	c_ac_t10_mem1 += MM_MEM[1]

	c_bc_t01 = S.Task('c_bc_t01', length=2, delay_cost=1)
	S += c_bc_t01 >= 69
	c_bc_t01 += MAS[0]

	c_pb00_in = S.Task('c_pb00_in', length=1, delay_cost=1)
	S += c_pb00_in >= 69
	c_pb00_in += MAS_in[3]

	c_pb00_mem0 = S.Task('c_pb00_mem0', length=1, delay_cost=1)
	S += c_pb00_mem0 >= 69
	c_pb00_mem0 += MAS_MEM[0]

	c_pb00_mem1 = S.Task('c_pb00_mem1', length=1, delay_cost=1)
	S += c_pb00_mem1 >= 69
	c_pb00_mem1 += MAS_MEM[5]

	c_pbc_t31 = S.Task('c_pbc_t31', length=2, delay_cost=1)
	S += c_pbc_t31 >= 69
	c_pbc_t31 += MAS[3]

	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	S += c_pcb_t30_in >= 69
	c_pcb_t30_in += MAS_in[0]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 69
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 69
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t10 = S.Task('c_ac_t10', length=2, delay_cost=1)
	S += c_ac_t10 >= 70
	c_ac_t10 += MAS[1]

	c_ac_t1_t5_in = S.Task('c_ac_t1_t5_in', length=1, delay_cost=1)
	S += c_ac_t1_t5_in >= 70
	c_ac_t1_t5_in += MAS_in[1]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 70
	c_ac_t1_t5_mem0 += MM_MEM[0]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 70
	c_ac_t1_t5_mem1 += MM_MEM[1]

	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	S += c_paa_t31_in >= 70
	c_paa_t31_in += MAS_in[3]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 70
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 70
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_pb00 = S.Task('c_pb00', length=2, delay_cost=1)
	S += c_pb00 >= 70
	c_pb00 += MAS[3]

	c_pbc_t4_t3_in = S.Task('c_pbc_t4_t3_in', length=1, delay_cost=1)
	S += c_pbc_t4_t3_in >= 70
	c_pbc_t4_t3_in += MAS_in[0]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 70
	c_pbc_t4_t3_mem0 += MAS_MEM[0]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 70
	c_pbc_t4_t3_mem1 += MAS_MEM[7]

	c_pcb_t30 = S.Task('c_pcb_t30', length=2, delay_cost=1)
	S += c_pcb_t30 >= 70
	c_pcb_t30 += MAS[0]

	c_ac_t00_in = S.Task('c_ac_t00_in', length=1, delay_cost=1)
	S += c_ac_t00_in >= 71
	c_ac_t00_in += MAS_in[0]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 71
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 71
	c_ac_t00_mem1 += MM_MEM[1]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=2, delay_cost=1)
	S += c_ac_t1_t5 >= 71
	c_ac_t1_t5 += MAS[1]

	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	S += c_paa_t30_in >= 71
	c_paa_t30_in += MAS_in[2]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 71
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 71
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_paa_t31 = S.Task('c_paa_t31', length=2, delay_cost=1)
	S += c_paa_t31 >= 71
	c_paa_t31 += MAS[3]

	c_pbc_t0_t2_in = S.Task('c_pbc_t0_t2_in', length=1, delay_cost=1)
	S += c_pbc_t0_t2_in >= 71
	c_pbc_t0_t2_in += MAS_in[1]

	c_pbc_t0_t2_mem0 = S.Task('c_pbc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem0 >= 71
	c_pbc_t0_t2_mem0 += MAS_MEM[6]

	c_pbc_t0_t2_mem1 = S.Task('c_pbc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t2_mem1 >= 71
	c_pbc_t0_t2_mem1 += MAS_MEM[7]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=2, delay_cost=1)
	S += c_pbc_t4_t3 >= 71
	c_pbc_t4_t3 += MAS[0]

	c_pcb_t4_t3_in = S.Task('c_pcb_t4_t3_in', length=1, delay_cost=1)
	S += c_pcb_t4_t3_in >= 71
	c_pcb_t4_t3_in += MAS_in[3]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 71
	c_pcb_t4_t3_mem0 += MAS_MEM[0]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 71
	c_pcb_t4_t3_mem1 += MAS_MEM[3]

	c_ac_t00 = S.Task('c_ac_t00', length=2, delay_cost=1)
	S += c_ac_t00 >= 72
	c_ac_t00 += MAS[0]

	c_ac_t0_t5_in = S.Task('c_ac_t0_t5_in', length=1, delay_cost=1)
	S += c_ac_t0_t5_in >= 72
	c_ac_t0_t5_in += MAS_in[3]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 72
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 72
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_bb_t00_in = S.Task('c_bb_t00_in', length=1, delay_cost=1)
	S += c_bb_t00_in >= 72
	c_bb_t00_in += MAS_in[1]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 72
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 72
	c_bb_t00_mem1 += MAS_MEM[1]

	c_paa_t30 = S.Task('c_paa_t30', length=2, delay_cost=1)
	S += c_paa_t30 >= 72
	c_paa_t30 += MAS[2]

	c_pbc_t0_t1_in = S.Task('c_pbc_t0_t1_in', length=1, delay_cost=1)
	S += c_pbc_t0_t1_in >= 72
	c_pbc_t0_t1_in += MM_in[0]

	c_pbc_t0_t1_mem0 = S.Task('c_pbc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem0 >= 72
	c_pbc_t0_t1_mem0 += MAS_MEM[6]

	c_pbc_t0_t1_mem1 = S.Task('c_pbc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t1_mem1 >= 72
	c_pbc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t2 = S.Task('c_pbc_t0_t2', length=2, delay_cost=1)
	S += c_pbc_t0_t2 >= 72
	c_pbc_t0_t2 += MAS[1]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=2, delay_cost=1)
	S += c_pcb_t4_t3 >= 72
	c_pcb_t4_t3 += MAS[3]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=2, delay_cost=1)
	S += c_ac_t0_t5 >= 73
	c_ac_t0_t5 += MAS[3]

	c_ac_t50_in = S.Task('c_ac_t50_in', length=1, delay_cost=1)
	S += c_ac_t50_in >= 73
	c_ac_t50_in += MAS_in[1]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 73
	c_ac_t50_mem0 += MAS_MEM[0]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 73
	c_ac_t50_mem1 += MAS_MEM[3]

	c_bb_t00 = S.Task('c_bb_t00', length=2, delay_cost=1)
	S += c_bb_t00 >= 73
	c_bb_t00 += MAS[1]

	c_bc_t1_t5_in = S.Task('c_bc_t1_t5_in', length=1, delay_cost=1)
	S += c_bc_t1_t5_in >= 73
	c_bc_t1_t5_in += MAS_in[0]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 73
	c_bc_t1_t5_mem0 += MM_MEM[0]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 73
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_cc_t00_in = S.Task('c_cc_t00_in', length=1, delay_cost=1)
	S += c_cc_t00_in >= 73
	c_cc_t00_in += MAS_in[2]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 73
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 73
	c_cc_t00_mem1 += MAS_MEM[1]

	c_paa_t4_t3_in = S.Task('c_paa_t4_t3_in', length=1, delay_cost=1)
	S += c_paa_t4_t3_in >= 73
	c_paa_t4_t3_in += MAS_in[3]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 73
	c_paa_t4_t3_mem0 += MAS_MEM[4]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 73
	c_paa_t4_t3_mem1 += MAS_MEM[7]

	c_pbc_t0_t0_in = S.Task('c_pbc_t0_t0_in', length=1, delay_cost=1)
	S += c_pbc_t0_t0_in >= 73
	c_pbc_t0_t0_in += MM_in[0]

	c_pbc_t0_t0_mem0 = S.Task('c_pbc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem0 >= 73
	c_pbc_t0_t0_mem0 += MAS_MEM[6]

	c_pbc_t0_t0_mem1 = S.Task('c_pbc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t0_mem1 >= 73
	c_pbc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_pbc_t0_t1 = S.Task('c_pbc_t0_t1', length=14, delay_cost=1)
	S += c_pbc_t0_t1 >= 73
	c_pbc_t0_t1 += MM[0]

	c_ac_t50 = S.Task('c_ac_t50', length=2, delay_cost=1)
	S += c_ac_t50 >= 74
	c_ac_t50 += MAS[1]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 74
	c_bb_t2_t0_in += MM_in[0]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 74
	c_bb_t2_t0_mem0 += MAS_MEM[2]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 74
	c_bb_t2_t0_mem1 += MAS_MEM[7]

	c_bc_t10_in = S.Task('c_bc_t10_in', length=1, delay_cost=1)
	S += c_bc_t10_in >= 74
	c_bc_t10_in += MAS_in[3]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 74
	c_bc_t10_mem0 += MM_MEM[0]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 74
	c_bc_t10_mem1 += MM_MEM[1]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=2, delay_cost=1)
	S += c_bc_t1_t5 >= 74
	c_bc_t1_t5 += MAS[0]

	c_cc_t00 = S.Task('c_cc_t00', length=2, delay_cost=1)
	S += c_cc_t00 >= 74
	c_cc_t00 += MAS[2]

	c_cc_t01_in = S.Task('c_cc_t01_in', length=1, delay_cost=1)
	S += c_cc_t01_in >= 74
	c_cc_t01_in += MAS_in[1]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 74
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 74
	c_cc_t01_mem1 += MAS_MEM[1]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=2, delay_cost=1)
	S += c_paa_t4_t3 >= 74
	c_paa_t4_t3 += MAS[3]

	c_pbc_t0_t0 = S.Task('c_pbc_t0_t0', length=14, delay_cost=1)
	S += c_pbc_t0_t0 >= 74
	c_pbc_t0_t0 += MM[0]

	c_aa_t00_in = S.Task('c_aa_t00_in', length=1, delay_cost=1)
	S += c_aa_t00_in >= 75
	c_aa_t00_in += MAS_in[3]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 75
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 75
	c_aa_t00_mem1 += MAS_MEM[5]

	c_ac_t4_t5_in = S.Task('c_ac_t4_t5_in', length=1, delay_cost=1)
	S += c_ac_t4_t5_in >= 75
	c_ac_t4_t5_in += MAS_in[0]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 75
	c_ac_t4_t5_mem0 += MM_MEM[0]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 75
	c_ac_t4_t5_mem1 += MM_MEM[1]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=14, delay_cost=1)
	S += c_bb_t2_t0 >= 75
	c_bb_t2_t0 += MM[0]

	c_bc_t10 = S.Task('c_bc_t10', length=2, delay_cost=1)
	S += c_bc_t10 >= 75
	c_bc_t10 += MAS[3]

	c_cc_t01 = S.Task('c_cc_t01', length=2, delay_cost=1)
	S += c_cc_t01 >= 75
	c_cc_t01 += MAS[1]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 75
	c_cc_t2_t0_in += MM_in[0]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 75
	c_cc_t2_t0_mem0 += MAS_MEM[4]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 75
	c_cc_t2_t0_mem1 += MAS_MEM[1]

	c_aa_t00 = S.Task('c_aa_t00', length=2, delay_cost=1)
	S += c_aa_t00 >= 76
	c_aa_t00 += MAS[3]

	c_ac_t40_in = S.Task('c_ac_t40_in', length=1, delay_cost=1)
	S += c_ac_t40_in >= 76
	c_ac_t40_in += MAS_in[3]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 76
	c_ac_t40_mem0 += MM_MEM[0]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 76
	c_ac_t40_mem1 += MM_MEM[1]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=2, delay_cost=1)
	S += c_ac_t4_t5 >= 76
	c_ac_t4_t5 += MAS[0]

	c_bb_t01_in = S.Task('c_bb_t01_in', length=1, delay_cost=1)
	S += c_bb_t01_in >= 76
	c_bb_t01_in += MAS_in[1]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 76
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 76
	c_bb_t01_mem1 += MAS_MEM[1]

	c_bc_t50_in = S.Task('c_bc_t50_in', length=1, delay_cost=1)
	S += c_bc_t50_in >= 76
	c_bc_t50_in += MAS_in[2]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 76
	c_bc_t50_mem0 += MAS_MEM[2]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 76
	c_bc_t50_mem1 += MAS_MEM[7]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=14, delay_cost=1)
	S += c_cc_t2_t0 >= 76
	c_cc_t2_t0 += MM[0]

	c_cc_t2_t2_in = S.Task('c_cc_t2_t2_in', length=1, delay_cost=1)
	S += c_cc_t2_t2_in >= 76
	c_cc_t2_t2_in += MAS_in[0]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 76
	c_cc_t2_t2_mem0 += MAS_MEM[4]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 76
	c_cc_t2_t2_mem1 += MAS_MEM[3]

	c_aa_t01_in = S.Task('c_aa_t01_in', length=1, delay_cost=1)
	S += c_aa_t01_in >= 77
	c_aa_t01_in += MAS_in[1]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 77
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 77
	c_aa_t01_mem1 += MAS_MEM[1]

	c_ac_t11_in = S.Task('c_ac_t11_in', length=1, delay_cost=1)
	S += c_ac_t11_in >= 77
	c_ac_t11_in += MAS_in[3]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 77
	c_ac_t11_mem0 += MM_MEM[0]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 77
	c_ac_t11_mem1 += MAS_MEM[3]

	c_ac_t40 = S.Task('c_ac_t40', length=2, delay_cost=1)
	S += c_ac_t40 >= 77
	c_ac_t40 += MAS[3]

	c_bb_t01 = S.Task('c_bb_t01', length=2, delay_cost=1)
	S += c_bb_t01 >= 77
	c_bb_t01 += MAS[1]

	c_bc_t50 = S.Task('c_bc_t50', length=2, delay_cost=1)
	S += c_bc_t50 >= 77
	c_bc_t50 += MAS[2]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=2, delay_cost=1)
	S += c_cc_t2_t2 >= 77
	c_cc_t2_t2 += MAS[0]

	c_aa_t01 = S.Task('c_aa_t01', length=2, delay_cost=1)
	S += c_aa_t01 >= 78
	c_aa_t01 += MAS[1]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 78
	c_aa_t2_t0_in += MM_in[0]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 78
	c_aa_t2_t0_mem0 += MAS_MEM[6]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 78
	c_aa_t2_t0_mem1 += MAS_MEM[1]

	c_ac_t01_in = S.Task('c_ac_t01_in', length=1, delay_cost=1)
	S += c_ac_t01_in >= 78
	c_ac_t01_in += MAS_in[2]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 78
	c_ac_t01_mem0 += MM_MEM[0]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 78
	c_ac_t01_mem1 += MAS_MEM[7]

	c_ac_t11 = S.Task('c_ac_t11', length=2, delay_cost=1)
	S += c_ac_t11 >= 78
	c_ac_t11 += MAS[3]

	c_bb_t2_t2_in = S.Task('c_bb_t2_t2_in', length=1, delay_cost=1)
	S += c_bb_t2_t2_in >= 78
	c_bb_t2_t2_in += MAS_in[3]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 78
	c_bb_t2_t2_mem0 += MAS_MEM[2]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 78
	c_bb_t2_t2_mem1 += MAS_MEM[3]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=14, delay_cost=1)
	S += c_aa_t2_t0 >= 79
	c_aa_t2_t0 += MM[0]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 79
	c_aa_t2_t1_in += MM_in[0]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 79
	c_aa_t2_t1_mem0 += MAS_MEM[2]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 79
	c_aa_t2_t1_mem1 += MAS_MEM[1]

	c_aa_t2_t2_in = S.Task('c_aa_t2_t2_in', length=1, delay_cost=1)
	S += c_aa_t2_t2_in >= 79
	c_aa_t2_t2_in += MAS_in[2]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 79
	c_aa_t2_t2_mem0 += MAS_MEM[6]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 79
	c_aa_t2_t2_mem1 += MAS_MEM[3]

	c_ac_t01 = S.Task('c_ac_t01', length=2, delay_cost=1)
	S += c_ac_t01 >= 79
	c_ac_t01 += MAS[2]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=2, delay_cost=1)
	S += c_bb_t2_t2 >= 79
	c_bb_t2_t2 += MAS[3]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=14, delay_cost=1)
	S += c_aa_t2_t1 >= 80
	c_aa_t2_t1 += MM[0]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=2, delay_cost=1)
	S += c_aa_t2_t2 >= 80
	c_aa_t2_t2 += MAS[2]

	c_ac_t51_in = S.Task('c_ac_t51_in', length=1, delay_cost=1)
	S += c_ac_t51_in >= 80
	c_ac_t51_in += MAS_in[2]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	S += c_ac_t51_mem0 >= 80
	c_ac_t51_mem0 += MAS_MEM[4]

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	S += c_ac_t51_mem1 >= 80
	c_ac_t51_mem1 += MAS_MEM[7]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 80
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 80
	c_bb_t2_t1_mem0 += MAS_MEM[2]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 80
	c_bb_t2_t1_mem1 += MAS_MEM[1]

	c_bc10_in = S.Task('c_bc10_in', length=1, delay_cost=1)
	S += c_bc10_in >= 80
	c_bc10_in += MAS_in[1]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	S += c_bc10_mem0 >= 80
	c_bc10_mem0 += MAS_MEM[6]

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	S += c_bc10_mem1 >= 80
	c_bc10_mem1 += MAS_MEM[5]

	c_ac10_in = S.Task('c_ac10_in', length=1, delay_cost=1)
	S += c_ac10_in >= 81
	c_ac10_in += MAS_in[2]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	S += c_ac10_mem0 >= 81
	c_ac10_mem0 += MAS_MEM[6]

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	S += c_ac10_mem1 >= 81
	c_ac10_mem1 += MAS_MEM[3]

	c_ac_t51 = S.Task('c_ac_t51', length=2, delay_cost=1)
	S += c_ac_t51 >= 81
	c_ac_t51 += MAS[2]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=14, delay_cost=1)
	S += c_bb_t2_t1 >= 81
	c_bb_t2_t1 += MM[0]

	c_bc10 = S.Task('c_bc10', length=2, delay_cost=1)
	S += c_bc10 >= 81
	c_bc10 += MAS[1]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 81
	c_cc_t2_t1_in += MM_in[0]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 81
	c_cc_t2_t1_mem0 += MAS_MEM[2]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 81
	c_cc_t2_t1_mem1 += MAS_MEM[1]

	c_ac10 = S.Task('c_ac10', length=2, delay_cost=1)
	S += c_ac10 >= 82
	c_ac10 += MAS[2]

	c_ac_s00_in = S.Task('c_ac_s00_in', length=1, delay_cost=1)
	S += c_ac_s00_in >= 82
	c_ac_s00_in += MAS_in[1]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	S += c_ac_s00_mem0 >= 82
	c_ac_s00_mem0 += MAS_MEM[2]

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	S += c_ac_s00_mem1 >= 82
	c_ac_s00_mem1 += MAS_MEM[7]

	c_ac_s01_in = S.Task('c_ac_s01_in', length=1, delay_cost=1)
	S += c_ac_s01_in >= 82
	c_ac_s01_in += MAS_in[0]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	S += c_ac_s01_mem0 >= 82
	c_ac_s01_mem0 += MAS_MEM[6]

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	S += c_ac_s01_mem1 >= 82
	c_ac_s01_mem1 += MAS_MEM[3]

	c_bc_t11_in = S.Task('c_bc_t11_in', length=1, delay_cost=1)
	S += c_bc_t11_in >= 82
	c_bc_t11_in += MAS_in[2]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 82
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 82
	c_bc_t11_mem1 += MAS_MEM[1]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=14, delay_cost=1)
	S += c_cc_t2_t1 >= 82
	c_cc_t2_t1 += MM[0]

	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	S += c_cc_t2_t4_in >= 82
	c_cc_t2_t4_in += MM_in[0]

	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem0 >= 82
	c_cc_t2_t4_mem0 += MAS_MEM[0]

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t4_mem1 >= 82
	c_cc_t2_t4_mem1 += MAS_MEM[5]

	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	S += c_aa_t2_t4_in >= 83
	c_aa_t2_t4_in += MM_in[0]

	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem0 >= 83
	c_aa_t2_t4_mem0 += MAS_MEM[4]

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t4_mem1 >= 83
	c_aa_t2_t4_mem1 += MAS_MEM[3]

	c_ac_s00 = S.Task('c_ac_s00', length=2, delay_cost=1)
	S += c_ac_s00 >= 83
	c_ac_s00 += MAS[1]

	c_ac_s01 = S.Task('c_ac_s01', length=2, delay_cost=1)
	S += c_ac_s01 >= 83
	c_ac_s01 += MAS[0]

	c_bc_t11 = S.Task('c_bc_t11', length=2, delay_cost=1)
	S += c_bc_t11 >= 83
	c_bc_t11 += MAS[2]

	c_bc_t41_in = S.Task('c_bc_t41_in', length=1, delay_cost=1)
	S += c_bc_t41_in >= 83
	c_bc_t41_in += MAS_in[3]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	S += c_bc_t41_mem0 >= 83
	c_bc_t41_mem0 += MM_MEM[0]

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	S += c_bc_t41_mem1 >= 83
	c_bc_t41_mem1 += MAS_MEM[1]

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=14, delay_cost=1)
	S += c_cc_t2_t4 >= 83
	c_cc_t2_t4 += MM[0]

	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=14, delay_cost=1)
	S += c_aa_t2_t4 >= 84
	c_aa_t2_t4 += MM[0]

	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	S += c_bb_t2_t4_in >= 84
	c_bb_t2_t4_in += MM_in[0]

	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem0 >= 84
	c_bb_t2_t4_mem0 += MAS_MEM[6]

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t4_mem1 >= 84
	c_bb_t2_t4_mem1 += MAS_MEM[1]

	c_bc_s01_in = S.Task('c_bc_s01_in', length=1, delay_cost=1)
	S += c_bc_s01_in >= 84
	c_bc_s01_in += MAS_in[3]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	S += c_bc_s01_mem0 >= 84
	c_bc_s01_mem0 += MAS_MEM[4]

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	S += c_bc_s01_mem1 >= 84
	c_bc_s01_mem1 += MAS_MEM[7]

	c_bc_t41 = S.Task('c_bc_t41', length=2, delay_cost=1)
	S += c_bc_t41 >= 84
	c_bc_t41 += MAS[3]

	c_bc_t51_in = S.Task('c_bc_t51_in', length=1, delay_cost=1)
	S += c_bc_t51_in >= 84
	c_bc_t51_in += MAS_in[2]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	S += c_bc_t51_mem0 >= 84
	c_bc_t51_mem0 += MAS_MEM[0]

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	S += c_bc_t51_mem1 >= 84
	c_bc_t51_mem1 += MAS_MEM[5]

	c_ac00_in = S.Task('c_ac00_in', length=1, delay_cost=1)
	S += c_ac00_in >= 85
	c_ac00_in += MAS_in[3]

	c_ac00_mem0 = S.Task('c_ac00_mem0', length=1, delay_cost=1)
	S += c_ac00_mem0 >= 85
	c_ac00_mem0 += MAS_MEM[0]

	c_ac00_mem1 = S.Task('c_ac00_mem1', length=1, delay_cost=1)
	S += c_ac00_mem1 >= 85
	c_ac00_mem1 += MAS_MEM[3]

	c_ac_t41_in = S.Task('c_ac_t41_in', length=1, delay_cost=1)
	S += c_ac_t41_in >= 85
	c_ac_t41_in += MAS_in[0]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	S += c_ac_t41_mem0 >= 85
	c_ac_t41_mem0 += MM_MEM[0]

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	S += c_ac_t41_mem1 >= 85
	c_ac_t41_mem1 += MAS_MEM[1]

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=14, delay_cost=1)
	S += c_bb_t2_t4 >= 85
	c_bb_t2_t4 += MM[0]

	c_bc_s00_in = S.Task('c_bc_s00_in', length=1, delay_cost=1)
	S += c_bc_s00_in >= 85
	c_bc_s00_in += MAS_in[2]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	S += c_bc_s00_mem0 >= 85
	c_bc_s00_mem0 += MAS_MEM[6]

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	S += c_bc_s00_mem1 >= 85
	c_bc_s00_mem1 += MAS_MEM[5]

	c_bc_s01 = S.Task('c_bc_s01', length=2, delay_cost=1)
	S += c_bc_s01 >= 85
	c_bc_s01 += MAS[3]

	c_bc_t51 = S.Task('c_bc_t51', length=2, delay_cost=1)
	S += c_bc_t51 >= 85
	c_bc_t51 += MAS[2]

	c_ac00 = S.Task('c_ac00', length=2, delay_cost=1)
	S += c_ac00 >= 86
	c_ac00 += MAS[3]

	c_ac01_in = S.Task('c_ac01_in', length=1, delay_cost=1)
	S += c_ac01_in >= 86
	c_ac01_in += MAS_in[1]

	c_ac01_mem0 = S.Task('c_ac01_mem0', length=1, delay_cost=1)
	S += c_ac01_mem0 >= 86
	c_ac01_mem0 += MAS_MEM[4]

	c_ac01_mem1 = S.Task('c_ac01_mem1', length=1, delay_cost=1)
	S += c_ac01_mem1 >= 86
	c_ac01_mem1 += MAS_MEM[1]

	c_ac_t41 = S.Task('c_ac_t41', length=2, delay_cost=1)
	S += c_ac_t41 >= 86
	c_ac_t41 += MAS[0]

	c_bc01_in = S.Task('c_bc01_in', length=1, delay_cost=1)
	S += c_bc01_in >= 86
	c_bc01_in += MAS_in[3]

	c_bc01_mem0 = S.Task('c_bc01_mem0', length=1, delay_cost=1)
	S += c_bc01_mem0 >= 86
	c_bc01_mem0 += MAS_MEM[0]

	c_bc01_mem1 = S.Task('c_bc01_mem1', length=1, delay_cost=1)
	S += c_bc01_mem1 >= 86
	c_bc01_mem1 += MAS_MEM[7]

	c_bc11_in = S.Task('c_bc11_in', length=1, delay_cost=1)
	S += c_bc11_in >= 86
	c_bc11_in += MAS_in[0]

	c_bc11_mem0 = S.Task('c_bc11_mem0', length=1, delay_cost=1)
	S += c_bc11_mem0 >= 86
	c_bc11_mem0 += MAS_MEM[6]

	c_bc11_mem1 = S.Task('c_bc11_mem1', length=1, delay_cost=1)
	S += c_bc11_mem1 >= 86
	c_bc11_mem1 += MAS_MEM[5]

	c_bc_s00 = S.Task('c_bc_s00', length=2, delay_cost=1)
	S += c_bc_s00 >= 86
	c_bc_s00 += MAS[2]

	c_ac01 = S.Task('c_ac01', length=2, delay_cost=1)
	S += c_ac01 >= 87
	c_ac01 += MAS[1]

	c_ac11_in = S.Task('c_ac11_in', length=1, delay_cost=1)
	S += c_ac11_in >= 87
	c_ac11_in += MAS_in[1]

	c_ac11_mem0 = S.Task('c_ac11_mem0', length=1, delay_cost=1)
	S += c_ac11_mem0 >= 87
	c_ac11_mem0 += MAS_MEM[0]

	c_ac11_mem1 = S.Task('c_ac11_mem1', length=1, delay_cost=1)
	S += c_ac11_mem1 >= 87
	c_ac11_mem1 += MAS_MEM[5]

	c_bc01 = S.Task('c_bc01', length=2, delay_cost=1)
	S += c_bc01 >= 87
	c_bc01 += MAS[3]

	c_bc11 = S.Task('c_bc11', length=2, delay_cost=1)
	S += c_bc11 >= 87
	c_bc11 += MAS[0]

	c_pbc_t0_t4_in = S.Task('c_pbc_t0_t4_in', length=1, delay_cost=1)
	S += c_pbc_t0_t4_in >= 87
	c_pbc_t0_t4_in += MM_in[0]

	c_pbc_t0_t4_mem0 = S.Task('c_pbc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t4_mem0 >= 87
	c_pbc_t0_t4_mem0 += MAS_MEM[2]

	c_pbc_t0_t4_mem1 = S.Task('c_pbc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t4_mem1 >= 87
	c_pbc_t0_t4_mem1 += MAS_MEM[1]

	c_pbc_t0_t5_in = S.Task('c_pbc_t0_t5_in', length=1, delay_cost=1)
	S += c_pbc_t0_t5_in >= 87
	c_pbc_t0_t5_in += MAS_in[0]

	c_pbc_t0_t5_mem0 = S.Task('c_pbc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t5_mem0 >= 87
	c_pbc_t0_t5_mem0 += MM_MEM[0]

	c_pbc_t0_t5_mem1 = S.Task('c_pbc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t5_mem1 >= 87
	c_pbc_t0_t5_mem1 += MM_MEM[1]

	c_ac11 = S.Task('c_ac11', length=2, delay_cost=1)
	S += c_ac11 >= 88
	c_ac11 += MAS[1]

	c_bc00_in = S.Task('c_bc00_in', length=1, delay_cost=1)
	S += c_bc00_in >= 88
	c_bc00_in += MAS_in[3]

	c_bc00_mem0 = S.Task('c_bc00_mem0', length=1, delay_cost=1)
	S += c_bc00_mem0 >= 88
	c_bc00_mem0 += MAS_MEM[2]

	c_bc00_mem1 = S.Task('c_bc00_mem1', length=1, delay_cost=1)
	S += c_bc00_mem1 >= 88
	c_bc00_mem1 += MAS_MEM[5]

	c_bcxi_y1_1_in = S.Task('c_bcxi_y1_1_in', length=1, delay_cost=1)
	S += c_bcxi_y1_1_in >= 88
	c_bcxi_y1_1_in += MAS_in[2]

	c_bcxi_y1_1_mem0 = S.Task('c_bcxi_y1_1_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem0 >= 88
	c_bcxi_y1_1_mem0 += MAS_MEM[0]

	c_bcxi_y1_1_mem1 = S.Task('c_bcxi_y1_1_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_1_mem1 >= 88
	c_bcxi_y1_1_mem1 += MAS_MEM[3]

	c_pa11_in = S.Task('c_pa11_in', length=1, delay_cost=1)
	S += c_pa11_in >= 88
	c_pa11_in += MAS_in[0]

	c_pa11_mem0 = S.Task('c_pa11_mem0', length=1, delay_cost=1)
	S += c_pa11_mem0 >= 88
	c_pa11_mem0 += MAS_MEM[4]

	c_pa11_mem1 = S.Task('c_pa11_mem1', length=1, delay_cost=1)
	S += c_pa11_mem1 >= 88
	c_pa11_mem1 += MAS_MEM[7]

	c_pbc_t00_in = S.Task('c_pbc_t00_in', length=1, delay_cost=1)
	S += c_pbc_t00_in >= 88
	c_pbc_t00_in += MAS_in[1]

	c_pbc_t00_mem0 = S.Task('c_pbc_t00_mem0', length=1, delay_cost=1)
	S += c_pbc_t00_mem0 >= 88
	c_pbc_t00_mem0 += MM_MEM[0]

	c_pbc_t00_mem1 = S.Task('c_pbc_t00_mem1', length=1, delay_cost=1)
	S += c_pbc_t00_mem1 >= 88
	c_pbc_t00_mem1 += MM_MEM[1]

	c_pbc_t0_t4 = S.Task('c_pbc_t0_t4', length=14, delay_cost=1)
	S += c_pbc_t0_t4 >= 88
	c_pbc_t0_t4 += MM[0]

	c_pbc_t0_t5 = S.Task('c_pbc_t0_t5', length=2, delay_cost=1)
	S += c_pbc_t0_t5 >= 88
	c_pbc_t0_t5 += MAS[0]

	c_bc00 = S.Task('c_bc00', length=2, delay_cost=1)
	S += c_bc00 >= 89
	c_bc00 += MAS[3]

	c_bcxi_y1_0_in = S.Task('c_bcxi_y1_0_in', length=1, delay_cost=1)
	S += c_bcxi_y1_0_in >= 89
	c_bcxi_y1_0_in += MAS_in[0]

	c_bcxi_y1_0_mem0 = S.Task('c_bcxi_y1_0_mem0', length=1, delay_cost=1)
	S += c_bcxi_y1_0_mem0 >= 89
	c_bcxi_y1_0_mem0 += MAS_MEM[2]

	c_bcxi_y1_0_mem1 = S.Task('c_bcxi_y1_0_mem1', length=1, delay_cost=1)
	S += c_bcxi_y1_0_mem1 >= 89
	c_bcxi_y1_0_mem1 += MAS_MEM[1]

	c_bcxi_y1_1 = S.Task('c_bcxi_y1_1', length=2, delay_cost=1)
	S += c_bcxi_y1_1 >= 89
	c_bcxi_y1_1 += MAS[2]

	c_pa11 = S.Task('c_pa11', length=2, delay_cost=1)
	S += c_pa11 >= 89
	c_pa11 += MAS[0]

	c_pbc_t00 = S.Task('c_pbc_t00', length=2, delay_cost=1)
	S += c_pbc_t00 >= 89
	c_pbc_t00 += MAS[1]

	c_pc10_in = S.Task('c_pc10_in', length=1, delay_cost=1)
	S += c_pc10_in >= 89
	c_pc10_in += MAS_in[1]

	c_pc10_mem0 = S.Task('c_pc10_mem0', length=1, delay_cost=1)
	S += c_pc10_mem0 >= 89
	c_pc10_mem0 += MAS_MEM[4]

	c_pc10_mem1 = S.Task('c_pc10_mem1', length=1, delay_cost=1)
	S += c_pc10_mem1 >= 89
	c_pc10_mem1 += MAS_MEM[5]

	c_pc11_in = S.Task('c_pc11_in', length=1, delay_cost=1)
	S += c_pc11_in >= 89
	c_pc11_in += MAS_in[3]

	c_pc11_mem0 = S.Task('c_pc11_mem0', length=1, delay_cost=1)
	S += c_pc11_mem0 >= 89
	c_pc11_mem0 += MAS_MEM[0]

	c_pc11_mem1 = S.Task('c_pc11_mem1', length=1, delay_cost=1)
	S += c_pc11_mem1 >= 89
	c_pc11_mem1 += MAS_MEM[3]

	c_bcxi_y1_0 = S.Task('c_bcxi_y1_0', length=2, delay_cost=1)
	S += c_bcxi_y1_0 >= 90
	c_bcxi_y1_0 += MAS[0]

	c_pa10_in = S.Task('c_pa10_in', length=1, delay_cost=1)
	S += c_pa10_in >= 90
	c_pa10_in += MAS_in[2]

	c_pa10_mem0 = S.Task('c_pa10_mem0', length=1, delay_cost=1)
	S += c_pa10_mem0 >= 90
	c_pa10_mem0 += MAS_MEM[4]

	c_pa10_mem1 = S.Task('c_pa10_mem1', length=1, delay_cost=1)
	S += c_pa10_mem1 >= 90
	c_pa10_mem1 += MAS_MEM[7]

	c_paa_t1_t1_in = S.Task('c_paa_t1_t1_in', length=1, delay_cost=1)
	S += c_paa_t1_t1_in >= 90
	c_paa_t1_t1_in += MM_in[0]

	c_paa_t1_t1_mem0 = S.Task('c_paa_t1_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t1_mem0 >= 90
	c_paa_t1_t1_mem0 += MAS_MEM[0]

	c_paa_t1_t1_mem1 = S.Task('c_paa_t1_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t1_mem1 >= 90
	c_paa_t1_t1_mem1 += MAIN_MEM_r[1]

	c_pc10 = S.Task('c_pc10', length=2, delay_cost=1)
	S += c_pc10 >= 90
	c_pc10 += MAS[1]

	c_pc11 = S.Task('c_pc11', length=2, delay_cost=1)
	S += c_pc11 >= 90
	c_pc11 += MAS[3]

	c_pa10 = S.Task('c_pa10', length=2, delay_cost=1)
	S += c_pa10 >= 91
	c_pa10 += MAS[2]

	c_paa_t1_t1 = S.Task('c_paa_t1_t1', length=14, delay_cost=1)
	S += c_paa_t1_t1 >= 91
	c_paa_t1_t1 += MM[0]

	c_pcb_t1_t1_in = S.Task('c_pcb_t1_t1_in', length=1, delay_cost=1)
	S += c_pcb_t1_t1_in >= 91
	c_pcb_t1_t1_in += MM_in[0]

	c_pcb_t1_t1_mem0 = S.Task('c_pcb_t1_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem0 >= 91
	c_pcb_t1_t1_mem0 += MAS_MEM[6]

	c_pcb_t1_t1_mem1 = S.Task('c_pcb_t1_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t1_mem1 >= 91
	c_pcb_t1_t1_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t2_in = S.Task('c_pcb_t1_t2_in', length=1, delay_cost=1)
	S += c_pcb_t1_t2_in >= 91
	c_pcb_t1_t2_in += MAS_in[1]

	c_pcb_t1_t2_mem0 = S.Task('c_pcb_t1_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem0 >= 91
	c_pcb_t1_t2_mem0 += MAS_MEM[2]

	c_pcb_t1_t2_mem1 = S.Task('c_pcb_t1_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t2_mem1 >= 91
	c_pcb_t1_t2_mem1 += MAS_MEM[7]

	c_paa_t1_t2_in = S.Task('c_paa_t1_t2_in', length=1, delay_cost=1)
	S += c_paa_t1_t2_in >= 92
	c_paa_t1_t2_in += MAS_in[2]

	c_paa_t1_t2_mem0 = S.Task('c_paa_t1_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t2_mem0 >= 92
	c_paa_t1_t2_mem0 += MAS_MEM[4]

	c_paa_t1_t2_mem1 = S.Task('c_paa_t1_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t2_mem1 >= 92
	c_paa_t1_t2_mem1 += MAS_MEM[1]

	c_pcb_t1_t0_in = S.Task('c_pcb_t1_t0_in', length=1, delay_cost=1)
	S += c_pcb_t1_t0_in >= 92
	c_pcb_t1_t0_in += MM_in[0]

	c_pcb_t1_t0_mem0 = S.Task('c_pcb_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem0 >= 92
	c_pcb_t1_t0_mem0 += MAS_MEM[2]

	c_pcb_t1_t0_mem1 = S.Task('c_pcb_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t0_mem1 >= 92
	c_pcb_t1_t0_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t1 = S.Task('c_pcb_t1_t1', length=14, delay_cost=1)
	S += c_pcb_t1_t1 >= 92
	c_pcb_t1_t1 += MM[0]

	c_pcb_t1_t2 = S.Task('c_pcb_t1_t2', length=2, delay_cost=1)
	S += c_pcb_t1_t2 >= 92
	c_pcb_t1_t2 += MAS[1]

	c_aa_t2_t5_in = S.Task('c_aa_t2_t5_in', length=1, delay_cost=1)
	S += c_aa_t2_t5_in >= 93
	c_aa_t2_t5_in += MAS_in[1]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem0 >= 93
	c_aa_t2_t5_mem0 += MM_MEM[0]

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t5_mem1 >= 93
	c_aa_t2_t5_mem1 += MM_MEM[1]

	c_paa_t1_t0_in = S.Task('c_paa_t1_t0_in', length=1, delay_cost=1)
	S += c_paa_t1_t0_in >= 93
	c_paa_t1_t0_in += MM_in[0]

	c_paa_t1_t0_mem0 = S.Task('c_paa_t1_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem0 >= 93
	c_paa_t1_t0_mem0 += MAS_MEM[4]

	c_paa_t1_t0_mem1 = S.Task('c_paa_t1_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t0_mem1 >= 93
	c_paa_t1_t0_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t2 = S.Task('c_paa_t1_t2', length=2, delay_cost=1)
	S += c_paa_t1_t2 >= 93
	c_paa_t1_t2 += MAS[2]

	c_pcb_t1_t0 = S.Task('c_pcb_t1_t0', length=14, delay_cost=1)
	S += c_pcb_t1_t0 >= 93
	c_pcb_t1_t0 += MM[0]

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=2, delay_cost=1)
	S += c_aa_t2_t5 >= 94
	c_aa_t2_t5 += MAS[1]

	c_bb_t20_in = S.Task('c_bb_t20_in', length=1, delay_cost=1)
	S += c_bb_t20_in >= 94
	c_bb_t20_in += MAS_in[3]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	S += c_bb_t20_mem0 >= 94
	c_bb_t20_mem0 += MM_MEM[0]

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	S += c_bb_t20_mem1 >= 94
	c_bb_t20_mem1 += MM_MEM[1]

	c_paa_t1_t0 = S.Task('c_paa_t1_t0', length=14, delay_cost=1)
	S += c_paa_t1_t0 >= 94
	c_paa_t1_t0 += MM[0]

	c_pcb_t1_t4_in = S.Task('c_pcb_t1_t4_in', length=1, delay_cost=1)
	S += c_pcb_t1_t4_in >= 94
	c_pcb_t1_t4_in += MM_in[0]

	c_pcb_t1_t4_mem0 = S.Task('c_pcb_t1_t4_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t4_mem0 >= 94
	c_pcb_t1_t4_mem0 += MAS_MEM[2]

	c_pcb_t1_t4_mem1 = S.Task('c_pcb_t1_t4_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t4_mem1 >= 94
	c_pcb_t1_t4_mem1 += MAS_MEM[7]

	c_aa_t20_in = S.Task('c_aa_t20_in', length=1, delay_cost=1)
	S += c_aa_t20_in >= 95
	c_aa_t20_in += MAS_in[1]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	S += c_aa_t20_mem0 >= 95
	c_aa_t20_mem0 += MM_MEM[0]

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	S += c_aa_t20_mem1 >= 95
	c_aa_t20_mem1 += MM_MEM[1]

	c_bb_t20 = S.Task('c_bb_t20', length=2, delay_cost=1)
	S += c_bb_t20 >= 95
	c_bb_t20 += MAS[3]

	c_paa_t1_t4_in = S.Task('c_paa_t1_t4_in', length=1, delay_cost=1)
	S += c_paa_t1_t4_in >= 95
	c_paa_t1_t4_in += MM_in[0]

	c_paa_t1_t4_mem0 = S.Task('c_paa_t1_t4_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t4_mem0 >= 95
	c_paa_t1_t4_mem0 += MAS_MEM[4]

	c_paa_t1_t4_mem1 = S.Task('c_paa_t1_t4_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t4_mem1 >= 95
	c_paa_t1_t4_mem1 += MAS_MEM[1]

	c_pcb_t1_t4 = S.Task('c_pcb_t1_t4', length=14, delay_cost=1)
	S += c_pcb_t1_t4 >= 95
	c_pcb_t1_t4 += MM[0]

	c_aa_t20 = S.Task('c_aa_t20', length=2, delay_cost=1)
	S += c_aa_t20 >= 96
	c_aa_t20 += MAS[1]

	c_bb00_in = S.Task('c_bb00_in', length=1, delay_cost=1)
	S += c_bb00_in >= 96
	c_bb00_in += MAS_in[1]

	c_bb00_mem0 = S.Task('c_bb00_mem0', length=1, delay_cost=1)
	S += c_bb00_mem0 >= 96
	c_bb00_mem0 += MAS_MEM[6]

	c_bb00_mem1 = S.Task('c_bb00_mem1', length=1, delay_cost=1)
	S += c_bb00_mem1 >= 96
	c_bb00_mem1 += MAS_MEM[3]

	c_cc_t20_in = S.Task('c_cc_t20_in', length=1, delay_cost=1)
	S += c_cc_t20_in >= 96
	c_cc_t20_in += MAS_in[2]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	S += c_cc_t20_mem0 >= 96
	c_cc_t20_mem0 += MM_MEM[0]

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	S += c_cc_t20_mem1 >= 96
	c_cc_t20_mem1 += MM_MEM[1]

	c_paa_t1_t4 = S.Task('c_paa_t1_t4', length=14, delay_cost=1)
	S += c_paa_t1_t4 >= 96
	c_paa_t1_t4 += MM[0]

	c_aa00_in = S.Task('c_aa00_in', length=1, delay_cost=1)
	S += c_aa00_in >= 97
	c_aa00_in += MAS_in[1]

	c_aa00_mem0 = S.Task('c_aa00_mem0', length=1, delay_cost=1)
	S += c_aa00_mem0 >= 97
	c_aa00_mem0 += MAS_MEM[2]

	c_aa00_mem1 = S.Task('c_aa00_mem1', length=1, delay_cost=1)
	S += c_aa00_mem1 >= 97
	c_aa00_mem1 += MAS_MEM[3]

	c_bb00 = S.Task('c_bb00', length=2, delay_cost=1)
	S += c_bb00 >= 97
	c_bb00 += MAS[1]

	c_cc_t20 = S.Task('c_cc_t20', length=2, delay_cost=1)
	S += c_cc_t20 >= 97
	c_cc_t20 += MAS[2]

	c_cc_t2_t5_in = S.Task('c_cc_t2_t5_in', length=1, delay_cost=1)
	S += c_cc_t2_t5_in >= 97
	c_cc_t2_t5_in += MAS_in[3]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem0 >= 97
	c_cc_t2_t5_mem0 += MM_MEM[0]

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t5_mem1 >= 97
	c_cc_t2_t5_mem1 += MM_MEM[1]

	c_aa00 = S.Task('c_aa00', length=2, delay_cost=1)
	S += c_aa00 >= 98
	c_aa00 += MAS[1]

	c_bb_t2_t5_in = S.Task('c_bb_t2_t5_in', length=1, delay_cost=1)
	S += c_bb_t2_t5_in >= 98
	c_bb_t2_t5_in += MAS_in[0]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem0 >= 98
	c_bb_t2_t5_mem0 += MM_MEM[0]

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t5_mem1 >= 98
	c_bb_t2_t5_mem1 += MM_MEM[1]

	c_cc00_in = S.Task('c_cc00_in', length=1, delay_cost=1)
	S += c_cc00_in >= 98
	c_cc00_in += MAS_in[2]

	c_cc00_mem0 = S.Task('c_cc00_mem0', length=1, delay_cost=1)
	S += c_cc00_mem0 >= 98
	c_cc00_mem0 += MAS_MEM[4]

	c_cc00_mem1 = S.Task('c_cc00_mem1', length=1, delay_cost=1)
	S += c_cc00_mem1 >= 98
	c_cc00_mem1 += MAS_MEM[1]

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=2, delay_cost=1)
	S += c_cc_t2_t5 >= 98
	c_cc_t2_t5 += MAS[3]

	c_pc00_in = S.Task('c_pc00_in', length=1, delay_cost=1)
	S += c_pc00_in >= 98
	c_pc00_in += MAS_in[3]

	c_pc00_mem0 = S.Task('c_pc00_mem0', length=1, delay_cost=1)
	S += c_pc00_mem0 >= 98
	c_pc00_mem0 += MAS_MEM[2]

	c_pc00_mem1 = S.Task('c_pc00_mem1', length=1, delay_cost=1)
	S += c_pc00_mem1 >= 98
	c_pc00_mem1 += MAS_MEM[7]

	c_aa_t21_in = S.Task('c_aa_t21_in', length=1, delay_cost=1)
	S += c_aa_t21_in >= 99
	c_aa_t21_in += MAS_in[1]

	c_aa_t21_mem0 = S.Task('c_aa_t21_mem0', length=1, delay_cost=1)
	S += c_aa_t21_mem0 >= 99
	c_aa_t21_mem0 += MM_MEM[0]

	c_aa_t21_mem1 = S.Task('c_aa_t21_mem1', length=1, delay_cost=1)
	S += c_aa_t21_mem1 >= 99
	c_aa_t21_mem1 += MAS_MEM[3]

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=2, delay_cost=1)
	S += c_bb_t2_t5 >= 99
	c_bb_t2_t5 += MAS[0]

	c_cc00 = S.Task('c_cc00', length=2, delay_cost=1)
	S += c_cc00 >= 99
	c_cc00 += MAS[2]

	c_pa00_in = S.Task('c_pa00_in', length=1, delay_cost=1)
	S += c_pa00_in >= 99
	c_pa00_in += MAS_in[2]

	c_pa00_mem0 = S.Task('c_pa00_mem0', length=1, delay_cost=1)
	S += c_pa00_mem0 >= 99
	c_pa00_mem0 += MAS_MEM[2]

	c_pa00_mem1 = S.Task('c_pa00_mem1', length=1, delay_cost=1)
	S += c_pa00_mem1 >= 99
	c_pa00_mem1 += MAS_MEM[1]

	c_pc00 = S.Task('c_pc00', length=2, delay_cost=1)
	S += c_pc00 >= 99
	c_pc00 += MAS[3]

	c_aa_t21 = S.Task('c_aa_t21', length=2, delay_cost=1)
	S += c_aa_t21 >= 100
	c_aa_t21 += MAS[1]

	c_bb_t21_in = S.Task('c_bb_t21_in', length=1, delay_cost=1)
	S += c_bb_t21_in >= 100
	c_bb_t21_in += MAS_in[0]

	c_bb_t21_mem0 = S.Task('c_bb_t21_mem0', length=1, delay_cost=1)
	S += c_bb_t21_mem0 >= 100
	c_bb_t21_mem0 += MM_MEM[0]

	c_bb_t21_mem1 = S.Task('c_bb_t21_mem1', length=1, delay_cost=1)
	S += c_bb_t21_mem1 >= 100
	c_bb_t21_mem1 += MAS_MEM[1]

	c_pa00 = S.Task('c_pa00', length=2, delay_cost=1)
	S += c_pa00 >= 100
	c_pa00 += MAS[2]

	c_pb10_in = S.Task('c_pb10_in', length=1, delay_cost=1)
	S += c_pb10_in >= 100
	c_pb10_in += MAS_in[2]

	c_pb10_mem0 = S.Task('c_pb10_mem0', length=1, delay_cost=1)
	S += c_pb10_mem0 >= 100
	c_pb10_mem0 += MAS_MEM[4]

	c_pb10_mem1 = S.Task('c_pb10_mem1', length=1, delay_cost=1)
	S += c_pb10_mem1 >= 100
	c_pb10_mem1 += MAS_MEM[5]

	c_pcb_t0_t0_in = S.Task('c_pcb_t0_t0_in', length=1, delay_cost=1)
	S += c_pcb_t0_t0_in >= 100
	c_pcb_t0_t0_in += MM_in[0]

	c_pcb_t0_t0_mem0 = S.Task('c_pcb_t0_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t0_mem0 >= 100
	c_pcb_t0_t0_mem0 += MAS_MEM[6]

	c_pcb_t0_t0_mem1 = S.Task('c_pcb_t0_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t0_mem1 >= 100
	c_pcb_t0_t0_mem1 += MAIN_MEM_r[1]

	c_aa01_in = S.Task('c_aa01_in', length=1, delay_cost=1)
	S += c_aa01_in >= 101
	c_aa01_in += MAS_in[0]

	c_aa01_mem0 = S.Task('c_aa01_mem0', length=1, delay_cost=1)
	S += c_aa01_mem0 >= 101
	c_aa01_mem0 += MAS_MEM[2]

	c_aa01_mem1 = S.Task('c_aa01_mem1', length=1, delay_cost=1)
	S += c_aa01_mem1 >= 101
	c_aa01_mem1 += MAS_MEM[1]

	c_bb_t21 = S.Task('c_bb_t21', length=2, delay_cost=1)
	S += c_bb_t21 >= 101
	c_bb_t21 += MAS[0]

	c_cc_t21_in = S.Task('c_cc_t21_in', length=1, delay_cost=1)
	S += c_cc_t21_in >= 101
	c_cc_t21_in += MAS_in[3]

	c_cc_t21_mem0 = S.Task('c_cc_t21_mem0', length=1, delay_cost=1)
	S += c_cc_t21_mem0 >= 101
	c_cc_t21_mem0 += MM_MEM[0]

	c_cc_t21_mem1 = S.Task('c_cc_t21_mem1', length=1, delay_cost=1)
	S += c_cc_t21_mem1 >= 101
	c_cc_t21_mem1 += MAS_MEM[7]

	c_paa_t0_t0_in = S.Task('c_paa_t0_t0_in', length=1, delay_cost=1)
	S += c_paa_t0_t0_in >= 101
	c_paa_t0_t0_in += MM_in[0]

	c_paa_t0_t0_mem0 = S.Task('c_paa_t0_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t0_mem0 >= 101
	c_paa_t0_t0_mem0 += MAS_MEM[4]

	c_paa_t0_t0_mem1 = S.Task('c_paa_t0_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t0_mem1 >= 101
	c_paa_t0_t0_mem1 += MAIN_MEM_r[1]

	c_pb10 = S.Task('c_pb10', length=2, delay_cost=1)
	S += c_pb10 >= 101
	c_pb10 += MAS[2]

	c_pcb_t0_t0 = S.Task('c_pcb_t0_t0', length=14, delay_cost=1)
	S += c_pcb_t0_t0 >= 101
	c_pcb_t0_t0 += MM[0]

	c_pcb_t20_in = S.Task('c_pcb_t20_in', length=1, delay_cost=1)
	S += c_pcb_t20_in >= 101
	c_pcb_t20_in += MAS_in[1]

	c_pcb_t20_mem0 = S.Task('c_pcb_t20_mem0', length=1, delay_cost=1)
	S += c_pcb_t20_mem0 >= 101
	c_pcb_t20_mem0 += MAS_MEM[6]

	c_pcb_t20_mem1 = S.Task('c_pcb_t20_mem1', length=1, delay_cost=1)
	S += c_pcb_t20_mem1 >= 101
	c_pcb_t20_mem1 += MAS_MEM[3]

	c_aa01 = S.Task('c_aa01', length=2, delay_cost=1)
	S += c_aa01 >= 102
	c_aa01 += MAS[0]

	c_bb01_in = S.Task('c_bb01_in', length=1, delay_cost=1)
	S += c_bb01_in >= 102
	c_bb01_in += MAS_in[2]

	c_bb01_mem0 = S.Task('c_bb01_mem0', length=1, delay_cost=1)
	S += c_bb01_mem0 >= 102
	c_bb01_mem0 += MAS_MEM[0]

	c_bb01_mem1 = S.Task('c_bb01_mem1', length=1, delay_cost=1)
	S += c_bb01_mem1 >= 102
	c_bb01_mem1 += MAS_MEM[7]

	c_cc_t21 = S.Task('c_cc_t21', length=2, delay_cost=1)
	S += c_cc_t21 >= 102
	c_cc_t21 += MAS[3]

	c_paa_t0_t0 = S.Task('c_paa_t0_t0', length=14, delay_cost=1)
	S += c_paa_t0_t0 >= 102
	c_paa_t0_t0 += MM[0]

	c_pbc_t01_in = S.Task('c_pbc_t01_in', length=1, delay_cost=1)
	S += c_pbc_t01_in >= 102
	c_pbc_t01_in += MAS_in[0]

	c_pbc_t01_mem0 = S.Task('c_pbc_t01_mem0', length=1, delay_cost=1)
	S += c_pbc_t01_mem0 >= 102
	c_pbc_t01_mem0 += MM_MEM[0]

	c_pbc_t01_mem1 = S.Task('c_pbc_t01_mem1', length=1, delay_cost=1)
	S += c_pbc_t01_mem1 >= 102
	c_pbc_t01_mem1 += MAS_MEM[1]

	c_pbc_t1_t0_in = S.Task('c_pbc_t1_t0_in', length=1, delay_cost=1)
	S += c_pbc_t1_t0_in >= 102
	c_pbc_t1_t0_in += MM_in[0]

	c_pbc_t1_t0_mem0 = S.Task('c_pbc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t0_mem0 >= 102
	c_pbc_t1_t0_mem0 += MAS_MEM[4]

	c_pbc_t1_t0_mem1 = S.Task('c_pbc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t0_mem1 >= 102
	c_pbc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_pbc_t20_in = S.Task('c_pbc_t20_in', length=1, delay_cost=1)
	S += c_pbc_t20_in >= 102
	c_pbc_t20_in += MAS_in[1]

	c_pbc_t20_mem0 = S.Task('c_pbc_t20_mem0', length=1, delay_cost=1)
	S += c_pbc_t20_mem0 >= 102
	c_pbc_t20_mem0 += MAS_MEM[6]

	c_pbc_t20_mem1 = S.Task('c_pbc_t20_mem1', length=1, delay_cost=1)
	S += c_pbc_t20_mem1 >= 102
	c_pbc_t20_mem1 += MAS_MEM[5]

	c_pcb_t20 = S.Task('c_pcb_t20', length=2, delay_cost=1)
	S += c_pcb_t20 >= 102
	c_pcb_t20 += MAS[1]

	c_bb01 = S.Task('c_bb01', length=2, delay_cost=1)
	S += c_bb01 >= 103
	c_bb01 += MAS[2]

	c_cc01_in = S.Task('c_cc01_in', length=1, delay_cost=1)
	S += c_cc01_in >= 103
	c_cc01_in += MAS_in[2]

	c_cc01_mem0 = S.Task('c_cc01_mem0', length=1, delay_cost=1)
	S += c_cc01_mem0 >= 103
	c_cc01_mem0 += MAS_MEM[6]

	c_cc01_mem1 = S.Task('c_cc01_mem1', length=1, delay_cost=1)
	S += c_cc01_mem1 >= 103
	c_cc01_mem1 += MAS_MEM[3]

	c_pa01_in = S.Task('c_pa01_in', length=1, delay_cost=1)
	S += c_pa01_in >= 103
	c_pa01_in += MAS_in[1]

	c_pa01_mem0 = S.Task('c_pa01_mem0', length=1, delay_cost=1)
	S += c_pa01_mem0 >= 103
	c_pa01_mem0 += MAS_MEM[0]

	c_pa01_mem1 = S.Task('c_pa01_mem1', length=1, delay_cost=1)
	S += c_pa01_mem1 >= 103
	c_pa01_mem1 += MAS_MEM[5]

	c_pbc_t01 = S.Task('c_pbc_t01', length=2, delay_cost=1)
	S += c_pbc_t01 >= 103
	c_pbc_t01 += MAS[0]

	c_pbc_t1_t0 = S.Task('c_pbc_t1_t0', length=14, delay_cost=1)
	S += c_pbc_t1_t0 >= 103
	c_pbc_t1_t0 += MM[0]

	c_pbc_t20 = S.Task('c_pbc_t20', length=2, delay_cost=1)
	S += c_pbc_t20 >= 103
	c_pbc_t20 += MAS[1]

	c_pcb_t4_t0_in = S.Task('c_pcb_t4_t0_in', length=1, delay_cost=1)
	S += c_pcb_t4_t0_in >= 103
	c_pcb_t4_t0_in += MM_in[0]

	c_pcb_t4_t0_mem0 = S.Task('c_pcb_t4_t0_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t0_mem0 >= 103
	c_pcb_t4_t0_mem0 += MAS_MEM[2]

	c_pcb_t4_t0_mem1 = S.Task('c_pcb_t4_t0_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t0_mem1 >= 103
	c_pcb_t4_t0_mem1 += MAS_MEM[1]

	c_cc01 = S.Task('c_cc01', length=2, delay_cost=1)
	S += c_cc01 >= 104
	c_cc01 += MAS[2]

	c_pa01 = S.Task('c_pa01', length=2, delay_cost=1)
	S += c_pa01 >= 104
	c_pa01 += MAS[1]

	c_pbc_t4_t0_in = S.Task('c_pbc_t4_t0_in', length=1, delay_cost=1)
	S += c_pbc_t4_t0_in >= 104
	c_pbc_t4_t0_in += MM_in[0]

	c_pbc_t4_t0_mem0 = S.Task('c_pbc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t0_mem0 >= 104
	c_pbc_t4_t0_mem0 += MAS_MEM[2]

	c_pbc_t4_t0_mem1 = S.Task('c_pbc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t0_mem1 >= 104
	c_pbc_t4_t0_mem1 += MAS_MEM[1]

	c_pc01_in = S.Task('c_pc01_in', length=1, delay_cost=1)
	S += c_pc01_in >= 104
	c_pc01_in += MAS_in[2]

	c_pc01_mem0 = S.Task('c_pc01_mem0', length=1, delay_cost=1)
	S += c_pc01_mem0 >= 104
	c_pc01_mem0 += MAS_MEM[4]

	c_pc01_mem1 = S.Task('c_pc01_mem1', length=1, delay_cost=1)
	S += c_pc01_mem1 >= 104
	c_pc01_mem1 += MAS_MEM[3]

	c_pcb_t4_t0 = S.Task('c_pcb_t4_t0', length=14, delay_cost=1)
	S += c_pcb_t4_t0 >= 104
	c_pcb_t4_t0 += MM[0]

	c_paa_t0_t1_in = S.Task('c_paa_t0_t1_in', length=1, delay_cost=1)
	S += c_paa_t0_t1_in >= 105
	c_paa_t0_t1_in += MM_in[0]

	c_paa_t0_t1_mem0 = S.Task('c_paa_t0_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t1_mem0 >= 105
	c_paa_t0_t1_mem0 += MAS_MEM[2]

	c_paa_t0_t1_mem1 = S.Task('c_paa_t0_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t1_mem1 >= 105
	c_paa_t0_t1_mem1 += MAIN_MEM_r[1]

	c_pb11_in = S.Task('c_pb11_in', length=1, delay_cost=1)
	S += c_pb11_in >= 105
	c_pb11_in += MAS_in[3]

	c_pb11_mem0 = S.Task('c_pb11_mem0', length=1, delay_cost=1)
	S += c_pb11_mem0 >= 105
	c_pb11_mem0 += MAS_MEM[4]

	c_pb11_mem1 = S.Task('c_pb11_mem1', length=1, delay_cost=1)
	S += c_pb11_mem1 >= 105
	c_pb11_mem1 += MAS_MEM[3]

	c_pbc_t4_t0 = S.Task('c_pbc_t4_t0', length=14, delay_cost=1)
	S += c_pbc_t4_t0 >= 105
	c_pbc_t4_t0 += MM[0]

	c_pc01 = S.Task('c_pc01', length=2, delay_cost=1)
	S += c_pc01 >= 105
	c_pc01 += MAS[2]

	c_paa_t0_t1 = S.Task('c_paa_t0_t1', length=14, delay_cost=1)
	S += c_paa_t0_t1 >= 106
	c_paa_t0_t1 += MM[0]

	c_paa_t21_in = S.Task('c_paa_t21_in', length=1, delay_cost=1)
	S += c_paa_t21_in >= 106
	c_paa_t21_in += MAS_in[0]

	c_paa_t21_mem0 = S.Task('c_paa_t21_mem0', length=1, delay_cost=1)
	S += c_paa_t21_mem0 >= 106
	c_paa_t21_mem0 += MAS_MEM[2]

	c_paa_t21_mem1 = S.Task('c_paa_t21_mem1', length=1, delay_cost=1)
	S += c_paa_t21_mem1 >= 106
	c_paa_t21_mem1 += MAS_MEM[1]

	c_pb11 = S.Task('c_pb11', length=2, delay_cost=1)
	S += c_pb11 >= 106
	c_pb11 += MAS[3]

	c_pcb_t0_t1_in = S.Task('c_pcb_t0_t1_in', length=1, delay_cost=1)
	S += c_pcb_t0_t1_in >= 106
	c_pcb_t0_t1_in += MM_in[0]

	c_pcb_t0_t1_mem0 = S.Task('c_pcb_t0_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t1_mem0 >= 106
	c_pcb_t0_t1_mem0 += MAS_MEM[4]

	c_pcb_t0_t1_mem1 = S.Task('c_pcb_t0_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t1_mem1 >= 106
	c_pcb_t0_t1_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t2_in = S.Task('c_pcb_t0_t2_in', length=1, delay_cost=1)
	S += c_pcb_t0_t2_in >= 106
	c_pcb_t0_t2_in += MAS_in[1]

	c_pcb_t0_t2_mem0 = S.Task('c_pcb_t0_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t2_mem0 >= 106
	c_pcb_t0_t2_mem0 += MAS_MEM[6]

	c_pcb_t0_t2_mem1 = S.Task('c_pcb_t0_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t2_mem1 >= 106
	c_pcb_t0_t2_mem1 += MAS_MEM[5]

	c_pcb_t1_t5_in = S.Task('c_pcb_t1_t5_in', length=1, delay_cost=1)
	S += c_pcb_t1_t5_in >= 106
	c_pcb_t1_t5_in += MAS_in[2]

	c_pcb_t1_t5_mem0 = S.Task('c_pcb_t1_t5_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t5_mem0 >= 106
	c_pcb_t1_t5_mem0 += MM_MEM[0]

	c_pcb_t1_t5_mem1 = S.Task('c_pcb_t1_t5_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t5_mem1 >= 106
	c_pcb_t1_t5_mem1 += MM_MEM[1]

	c_paa_t1_t5_in = S.Task('c_paa_t1_t5_in', length=1, delay_cost=1)
	S += c_paa_t1_t5_in >= 107
	c_paa_t1_t5_in += MAS_in[3]

	c_paa_t1_t5_mem0 = S.Task('c_paa_t1_t5_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t5_mem0 >= 107
	c_paa_t1_t5_mem0 += MM_MEM[0]

	c_paa_t1_t5_mem1 = S.Task('c_paa_t1_t5_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t5_mem1 >= 107
	c_paa_t1_t5_mem1 += MM_MEM[1]

	c_paa_t21 = S.Task('c_paa_t21', length=2, delay_cost=1)
	S += c_paa_t21 >= 107
	c_paa_t21 += MAS[0]

	c_pbc_t1_t1_in = S.Task('c_pbc_t1_t1_in', length=1, delay_cost=1)
	S += c_pbc_t1_t1_in >= 107
	c_pbc_t1_t1_in += MM_in[0]

	c_pbc_t1_t1_mem0 = S.Task('c_pbc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t1_mem0 >= 107
	c_pbc_t1_t1_mem0 += MAS_MEM[6]

	c_pbc_t1_t1_mem1 = S.Task('c_pbc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t1_mem1 >= 107
	c_pbc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_pcb_t0_t1 = S.Task('c_pcb_t0_t1', length=14, delay_cost=1)
	S += c_pcb_t0_t1 >= 107
	c_pcb_t0_t1 += MM[0]

	c_pcb_t0_t2 = S.Task('c_pcb_t0_t2', length=2, delay_cost=1)
	S += c_pcb_t0_t2 >= 107
	c_pcb_t0_t2 += MAS[1]

	c_pcb_t1_t5 = S.Task('c_pcb_t1_t5', length=2, delay_cost=1)
	S += c_pcb_t1_t5 >= 107
	c_pcb_t1_t5 += MAS[2]

	c_pcb_t21_in = S.Task('c_pcb_t21_in', length=1, delay_cost=1)
	S += c_pcb_t21_in >= 107
	c_pcb_t21_in += MAS_in[0]

	c_pcb_t21_mem0 = S.Task('c_pcb_t21_mem0', length=1, delay_cost=1)
	S += c_pcb_t21_mem0 >= 107
	c_pcb_t21_mem0 += MAS_MEM[4]

	c_pcb_t21_mem1 = S.Task('c_pcb_t21_mem1', length=1, delay_cost=1)
	S += c_pcb_t21_mem1 >= 107
	c_pcb_t21_mem1 += MAS_MEM[7]

	c_paa_t10_in = S.Task('c_paa_t10_in', length=1, delay_cost=1)
	S += c_paa_t10_in >= 108
	c_paa_t10_in += MAS_in[0]

	c_paa_t10_mem0 = S.Task('c_paa_t10_mem0', length=1, delay_cost=1)
	S += c_paa_t10_mem0 >= 108
	c_paa_t10_mem0 += MM_MEM[0]

	c_paa_t10_mem1 = S.Task('c_paa_t10_mem1', length=1, delay_cost=1)
	S += c_paa_t10_mem1 >= 108
	c_paa_t10_mem1 += MM_MEM[1]

	c_paa_t1_t5 = S.Task('c_paa_t1_t5', length=2, delay_cost=1)
	S += c_paa_t1_t5 >= 108
	c_paa_t1_t5 += MAS[3]

	c_paa_t20_in = S.Task('c_paa_t20_in', length=1, delay_cost=1)
	S += c_paa_t20_in >= 108
	c_paa_t20_in += MAS_in[3]

	c_paa_t20_mem0 = S.Task('c_paa_t20_mem0', length=1, delay_cost=1)
	S += c_paa_t20_mem0 >= 108
	c_paa_t20_mem0 += MAS_MEM[4]

	c_paa_t20_mem1 = S.Task('c_paa_t20_mem1', length=1, delay_cost=1)
	S += c_paa_t20_mem1 >= 108
	c_paa_t20_mem1 += MAS_MEM[5]

	c_pbc_t1_t1 = S.Task('c_pbc_t1_t1', length=14, delay_cost=1)
	S += c_pbc_t1_t1 >= 108
	c_pbc_t1_t1 += MM[0]

	c_pbc_t21_in = S.Task('c_pbc_t21_in', length=1, delay_cost=1)
	S += c_pbc_t21_in >= 108
	c_pbc_t21_in += MAS_in[2]

	c_pbc_t21_mem0 = S.Task('c_pbc_t21_mem0', length=1, delay_cost=1)
	S += c_pbc_t21_mem0 >= 108
	c_pbc_t21_mem0 += MAS_MEM[6]

	c_pbc_t21_mem1 = S.Task('c_pbc_t21_mem1', length=1, delay_cost=1)
	S += c_pbc_t21_mem1 >= 108
	c_pbc_t21_mem1 += MAS_MEM[7]

	c_pcb_t0_t4_in = S.Task('c_pcb_t0_t4_in', length=1, delay_cost=1)
	S += c_pcb_t0_t4_in >= 108
	c_pcb_t0_t4_in += MM_in[0]

	c_pcb_t0_t4_mem0 = S.Task('c_pcb_t0_t4_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t4_mem0 >= 108
	c_pcb_t0_t4_mem0 += MAS_MEM[2]

	c_pcb_t0_t4_mem1 = S.Task('c_pcb_t0_t4_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t4_mem1 >= 108
	c_pcb_t0_t4_mem1 += MAS_MEM[1]

	c_pcb_t21 = S.Task('c_pcb_t21', length=2, delay_cost=1)
	S += c_pcb_t21 >= 108
	c_pcb_t21 += MAS[0]

	c_paa_t0_t2_in = S.Task('c_paa_t0_t2_in', length=1, delay_cost=1)
	S += c_paa_t0_t2_in >= 109
	c_paa_t0_t2_in += MAS_in[2]

	c_paa_t0_t2_mem0 = S.Task('c_paa_t0_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t2_mem0 >= 109
	c_paa_t0_t2_mem0 += MAS_MEM[4]

	c_paa_t0_t2_mem1 = S.Task('c_paa_t0_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t2_mem1 >= 109
	c_paa_t0_t2_mem1 += MAS_MEM[3]

	c_paa_t10 = S.Task('c_paa_t10', length=2, delay_cost=1)
	S += c_paa_t10 >= 109
	c_paa_t10 += MAS[0]

	c_paa_t20 = S.Task('c_paa_t20', length=2, delay_cost=1)
	S += c_paa_t20 >= 109
	c_paa_t20 += MAS[3]

	c_paa_t4_t1_in = S.Task('c_paa_t4_t1_in', length=1, delay_cost=1)
	S += c_paa_t4_t1_in >= 109
	c_paa_t4_t1_in += MM_in[0]

	c_paa_t4_t1_mem0 = S.Task('c_paa_t4_t1_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t1_mem0 >= 109
	c_paa_t4_t1_mem0 += MAS_MEM[0]

	c_paa_t4_t1_mem1 = S.Task('c_paa_t4_t1_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t1_mem1 >= 109
	c_paa_t4_t1_mem1 += MAS_MEM[7]

	c_pbc_t21 = S.Task('c_pbc_t21', length=2, delay_cost=1)
	S += c_pbc_t21 >= 109
	c_pbc_t21 += MAS[2]

	c_pcb_t0_t4 = S.Task('c_pcb_t0_t4', length=14, delay_cost=1)
	S += c_pcb_t0_t4 >= 109
	c_pcb_t0_t4 += MM[0]

	c_pcb_t11_in = S.Task('c_pcb_t11_in', length=1, delay_cost=1)
	S += c_pcb_t11_in >= 109
	c_pcb_t11_in += MAS_in[3]

	c_pcb_t11_mem0 = S.Task('c_pcb_t11_mem0', length=1, delay_cost=1)
	S += c_pcb_t11_mem0 >= 109
	c_pcb_t11_mem0 += MM_MEM[0]

	c_pcb_t11_mem1 = S.Task('c_pcb_t11_mem1', length=1, delay_cost=1)
	S += c_pcb_t11_mem1 >= 109
	c_pcb_t11_mem1 += MAS_MEM[5]

	c_pcb_t4_t2_in = S.Task('c_pcb_t4_t2_in', length=1, delay_cost=1)
	S += c_pcb_t4_t2_in >= 109
	c_pcb_t4_t2_in += MAS_in[0]

	c_pcb_t4_t2_mem0 = S.Task('c_pcb_t4_t2_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t2_mem0 >= 109
	c_pcb_t4_t2_mem0 += MAS_MEM[2]

	c_pcb_t4_t2_mem1 = S.Task('c_pcb_t4_t2_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t2_mem1 >= 109
	c_pcb_t4_t2_mem1 += MAS_MEM[1]

	c_paa_t0_t2 = S.Task('c_paa_t0_t2', length=2, delay_cost=1)
	S += c_paa_t0_t2 >= 110
	c_paa_t0_t2 += MAS[2]

	c_paa_t4_t1 = S.Task('c_paa_t4_t1', length=14, delay_cost=1)
	S += c_paa_t4_t1 >= 110
	c_paa_t4_t1 += MM[0]

	c_paa_t4_t2_in = S.Task('c_paa_t4_t2_in', length=1, delay_cost=1)
	S += c_paa_t4_t2_in >= 110
	c_paa_t4_t2_in += MAS_in[3]

	c_paa_t4_t2_mem0 = S.Task('c_paa_t4_t2_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t2_mem0 >= 110
	c_paa_t4_t2_mem0 += MAS_MEM[6]

	c_paa_t4_t2_mem1 = S.Task('c_paa_t4_t2_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t2_mem1 >= 110
	c_paa_t4_t2_mem1 += MAS_MEM[1]

	c_pbc_t1_t2_in = S.Task('c_pbc_t1_t2_in', length=1, delay_cost=1)
	S += c_pbc_t1_t2_in >= 110
	c_pbc_t1_t2_in += MAS_in[0]

	c_pbc_t1_t2_mem0 = S.Task('c_pbc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t2_mem0 >= 110
	c_pbc_t1_t2_mem0 += MAS_MEM[4]

	c_pbc_t1_t2_mem1 = S.Task('c_pbc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t2_mem1 >= 110
	c_pbc_t1_t2_mem1 += MAS_MEM[7]

	c_pbc_t4_t2_in = S.Task('c_pbc_t4_t2_in', length=1, delay_cost=1)
	S += c_pbc_t4_t2_in >= 110
	c_pbc_t4_t2_in += MAS_in[1]

	c_pbc_t4_t2_mem0 = S.Task('c_pbc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t2_mem0 >= 110
	c_pbc_t4_t2_mem0 += MAS_MEM[2]

	c_pbc_t4_t2_mem1 = S.Task('c_pbc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t2_mem1 >= 110
	c_pbc_t4_t2_mem1 += MAS_MEM[5]

	c_pcb_t10_in = S.Task('c_pcb_t10_in', length=1, delay_cost=1)
	S += c_pcb_t10_in >= 110
	c_pcb_t10_in += MAS_in[2]

	c_pcb_t10_mem0 = S.Task('c_pcb_t10_mem0', length=1, delay_cost=1)
	S += c_pcb_t10_mem0 >= 110
	c_pcb_t10_mem0 += MM_MEM[0]

	c_pcb_t10_mem1 = S.Task('c_pcb_t10_mem1', length=1, delay_cost=1)
	S += c_pcb_t10_mem1 >= 110
	c_pcb_t10_mem1 += MM_MEM[1]

	c_pcb_t11 = S.Task('c_pcb_t11', length=2, delay_cost=1)
	S += c_pcb_t11 >= 110
	c_pcb_t11 += MAS[3]

	c_pcb_t4_t1_in = S.Task('c_pcb_t4_t1_in', length=1, delay_cost=1)
	S += c_pcb_t4_t1_in >= 110
	c_pcb_t4_t1_in += MM_in[0]

	c_pcb_t4_t1_mem0 = S.Task('c_pcb_t4_t1_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t1_mem0 >= 110
	c_pcb_t4_t1_mem0 += MAS_MEM[0]

	c_pcb_t4_t1_mem1 = S.Task('c_pcb_t4_t1_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t1_mem1 >= 110
	c_pcb_t4_t1_mem1 += MAS_MEM[3]

	c_pcb_t4_t2 = S.Task('c_pcb_t4_t2', length=2, delay_cost=1)
	S += c_pcb_t4_t2 >= 110
	c_pcb_t4_t2 += MAS[0]

	c_paa_t11_in = S.Task('c_paa_t11_in', length=1, delay_cost=1)
	S += c_paa_t11_in >= 111
	c_paa_t11_in += MAS_in[2]

	c_paa_t11_mem0 = S.Task('c_paa_t11_mem0', length=1, delay_cost=1)
	S += c_paa_t11_mem0 >= 111
	c_paa_t11_mem0 += MM_MEM[0]

	c_paa_t11_mem1 = S.Task('c_paa_t11_mem1', length=1, delay_cost=1)
	S += c_paa_t11_mem1 >= 111
	c_paa_t11_mem1 += MAS_MEM[7]

	c_paa_t4_t0_in = S.Task('c_paa_t4_t0_in', length=1, delay_cost=1)
	S += c_paa_t4_t0_in >= 111
	c_paa_t4_t0_in += MM_in[0]

	c_paa_t4_t0_mem0 = S.Task('c_paa_t4_t0_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t0_mem0 >= 111
	c_paa_t4_t0_mem0 += MAS_MEM[6]

	c_paa_t4_t0_mem1 = S.Task('c_paa_t4_t0_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t0_mem1 >= 111
	c_paa_t4_t0_mem1 += MAS_MEM[5]

	c_paa_t4_t2 = S.Task('c_paa_t4_t2', length=2, delay_cost=1)
	S += c_paa_t4_t2 >= 111
	c_paa_t4_t2 += MAS[3]

	c_pbc_t1_t2 = S.Task('c_pbc_t1_t2', length=2, delay_cost=1)
	S += c_pbc_t1_t2 >= 111
	c_pbc_t1_t2 += MAS[0]

	c_pbc_t4_t2 = S.Task('c_pbc_t4_t2', length=2, delay_cost=1)
	S += c_pbc_t4_t2 >= 111
	c_pbc_t4_t2 += MAS[1]

	c_pcb_t10 = S.Task('c_pcb_t10', length=2, delay_cost=1)
	S += c_pcb_t10 >= 111
	c_pcb_t10 += MAS[2]

	c_pcb_t4_t1 = S.Task('c_pcb_t4_t1', length=14, delay_cost=1)
	S += c_pcb_t4_t1 >= 111
	c_pcb_t4_t1 += MM[0]

	c_paa_t11 = S.Task('c_paa_t11', length=2, delay_cost=1)
	S += c_paa_t11 >= 112
	c_paa_t11 += MAS[2]

	c_paa_t4_t0 = S.Task('c_paa_t4_t0', length=14, delay_cost=1)
	S += c_paa_t4_t0 >= 112
	c_paa_t4_t0 += MM[0]

	c_pbc_t1_t4_in = S.Task('c_pbc_t1_t4_in', length=1, delay_cost=1)
	S += c_pbc_t1_t4_in >= 112
	c_pbc_t1_t4_in += MM_in[0]

	c_pbc_t1_t4_mem0 = S.Task('c_pbc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t4_mem0 >= 112
	c_pbc_t1_t4_mem0 += MAS_MEM[0]

	c_pbc_t1_t4_mem1 = S.Task('c_pbc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t4_mem1 >= 112
	c_pbc_t1_t4_mem1 += MAS_MEM[7]

	c_paa_t0_t4_in = S.Task('c_paa_t0_t4_in', length=1, delay_cost=1)
	S += c_paa_t0_t4_in >= 113
	c_paa_t0_t4_in += MM_in[0]

	c_paa_t0_t4_mem0 = S.Task('c_paa_t0_t4_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t4_mem0 >= 113
	c_paa_t0_t4_mem0 += MAS_MEM[4]

	c_paa_t0_t4_mem1 = S.Task('c_paa_t0_t4_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t4_mem1 >= 113
	c_paa_t0_t4_mem1 += MAS_MEM[7]

	c_pbc_t1_t4 = S.Task('c_pbc_t1_t4', length=14, delay_cost=1)
	S += c_pbc_t1_t4 >= 113
	c_pbc_t1_t4 += MM[0]

	c_paa_t0_t4 = S.Task('c_paa_t0_t4', length=14, delay_cost=1)
	S += c_paa_t0_t4 >= 114
	c_paa_t0_t4 += MM[0]

	c_pbc_t4_t1_in = S.Task('c_pbc_t4_t1_in', length=1, delay_cost=1)
	S += c_pbc_t4_t1_in >= 114
	c_pbc_t4_t1_in += MM_in[0]

	c_pbc_t4_t1_mem0 = S.Task('c_pbc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t1_mem0 >= 114
	c_pbc_t4_t1_mem0 += MAS_MEM[4]

	c_pbc_t4_t1_mem1 = S.Task('c_pbc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t1_mem1 >= 114
	c_pbc_t4_t1_mem1 += MAS_MEM[7]

	c_pbc_t4_t1 = S.Task('c_pbc_t4_t1', length=14, delay_cost=1)
	S += c_pbc_t4_t1 >= 115
	c_pbc_t4_t1 += MM[0]

	c_paa_t00_in = S.Task('c_paa_t00_in', length=1, delay_cost=1)
	S += c_paa_t00_in >= 119
	c_paa_t00_in += MAS_in[2]

	c_paa_t00_mem0 = S.Task('c_paa_t00_mem0', length=1, delay_cost=1)
	S += c_paa_t00_mem0 >= 119
	c_paa_t00_mem0 += MM_MEM[0]

	c_paa_t00_mem1 = S.Task('c_paa_t00_mem1', length=1, delay_cost=1)
	S += c_paa_t00_mem1 >= 119
	c_paa_t00_mem1 += MM_MEM[1]

	c_paa_t00 = S.Task('c_paa_t00', length=2, delay_cost=1)
	S += c_paa_t00 >= 120
	c_paa_t00 += MAS[2]

	c_paa_t0_t5_in = S.Task('c_paa_t0_t5_in', length=1, delay_cost=1)
	S += c_paa_t0_t5_in >= 120
	c_paa_t0_t5_in += MAS_in[0]

	c_paa_t0_t5_mem0 = S.Task('c_paa_t0_t5_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t5_mem0 >= 120
	c_paa_t0_t5_mem0 += MM_MEM[0]

	c_paa_t0_t5_mem1 = S.Task('c_paa_t0_t5_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t5_mem1 >= 120
	c_paa_t0_t5_mem1 += MM_MEM[1]

	c_paa_t0_t5 = S.Task('c_paa_t0_t5', length=2, delay_cost=1)
	S += c_paa_t0_t5 >= 121
	c_paa_t0_t5 += MAS[0]

	c_pbc_t10_in = S.Task('c_pbc_t10_in', length=1, delay_cost=1)
	S += c_pbc_t10_in >= 121
	c_pbc_t10_in += MAS_in[3]

	c_pbc_t10_mem0 = S.Task('c_pbc_t10_mem0', length=1, delay_cost=1)
	S += c_pbc_t10_mem0 >= 121
	c_pbc_t10_mem0 += MM_MEM[0]

	c_pbc_t10_mem1 = S.Task('c_pbc_t10_mem1', length=1, delay_cost=1)
	S += c_pbc_t10_mem1 >= 121
	c_pbc_t10_mem1 += MM_MEM[1]

	c_pbc_t10 = S.Task('c_pbc_t10', length=2, delay_cost=1)
	S += c_pbc_t10 >= 122
	c_pbc_t10 += MAS[3]

	c_pbc_t1_t5_in = S.Task('c_pbc_t1_t5_in', length=1, delay_cost=1)
	S += c_pbc_t1_t5_in >= 122
	c_pbc_t1_t5_in += MAS_in[0]

	c_pbc_t1_t5_mem0 = S.Task('c_pbc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t5_mem0 >= 122
	c_pbc_t1_t5_mem0 += MM_MEM[0]

	c_pbc_t1_t5_mem1 = S.Task('c_pbc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t5_mem1 >= 122
	c_pbc_t1_t5_mem1 += MM_MEM[1]

	c_pbc_t1_t5 = S.Task('c_pbc_t1_t5', length=2, delay_cost=1)
	S += c_pbc_t1_t5 >= 123
	c_pbc_t1_t5 += MAS[0]

	c_pcb_t0_t5_in = S.Task('c_pcb_t0_t5_in', length=1, delay_cost=1)
	S += c_pcb_t0_t5_in >= 123
	c_pcb_t0_t5_in += MAS_in[3]

	c_pcb_t0_t5_mem0 = S.Task('c_pcb_t0_t5_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t5_mem0 >= 123
	c_pcb_t0_t5_mem0 += MM_MEM[0]

	c_pcb_t0_t5_mem1 = S.Task('c_pcb_t0_t5_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t5_mem1 >= 123
	c_pcb_t0_t5_mem1 += MM_MEM[1]

	c_pcb_t00_in = S.Task('c_pcb_t00_in', length=1, delay_cost=1)
	S += c_pcb_t00_in >= 124
	c_pcb_t00_in += MAS_in[3]

	c_pcb_t00_mem0 = S.Task('c_pcb_t00_mem0', length=1, delay_cost=1)
	S += c_pcb_t00_mem0 >= 124
	c_pcb_t00_mem0 += MM_MEM[0]

	c_pcb_t00_mem1 = S.Task('c_pcb_t00_mem1', length=1, delay_cost=1)
	S += c_pcb_t00_mem1 >= 124
	c_pcb_t00_mem1 += MM_MEM[1]

	c_pcb_t0_t5 = S.Task('c_pcb_t0_t5', length=2, delay_cost=1)
	S += c_pcb_t0_t5 >= 124
	c_pcb_t0_t5 += MAS[3]

	c_pcb_t00 = S.Task('c_pcb_t00', length=2, delay_cost=1)
	S += c_pcb_t00 >= 125
	c_pcb_t00 += MAS[3]


	# new tasks
	c_pbc_t11 = S.Task('c_pbc_t11', length=2, delay_cost=1)
	c_pbc_t11 += alt(MAS)
	c_pbc_t11_in = S.Task('c_pbc_t11_in', length=1, delay_cost=1)
	c_pbc_t11_in += alt(MAS_in)
	S += c_pbc_t11_in*MAS_in[0]<=c_pbc_t11*MAS[0]

	S += c_pbc_t11_in*MAS_in[1]<=c_pbc_t11*MAS[1]

	S += c_pbc_t11_in*MAS_in[2]<=c_pbc_t11*MAS[2]

	S += c_pbc_t11_in*MAS_in[3]<=c_pbc_t11*MAS[3]

	c_pbc_t11_mem0 = S.Task('c_pbc_t11_mem0', length=1, delay_cost=1)
	c_pbc_t11_mem0 += MM_MEM[0]
	S += 126 < c_pbc_t11_mem0
	S += c_pbc_t11_mem0 <= c_pbc_t11

	c_pbc_t11_mem1 = S.Task('c_pbc_t11_mem1', length=1, delay_cost=1)
	c_pbc_t11_mem1 += MAS_MEM[1]
	S += 124 < c_pbc_t11_mem1
	S += c_pbc_t11_mem1 <= c_pbc_t11

	c_pbc_t4_t4 = S.Task('c_pbc_t4_t4', length=14, delay_cost=1)
	c_pbc_t4_t4 += alt(MM)
	c_pbc_t4_t4_in = S.Task('c_pbc_t4_t4_in', length=1, delay_cost=1)
	c_pbc_t4_t4_in += alt(MM_in)
	S += c_pbc_t4_t4_in*MM_in[0]<=c_pbc_t4_t4*MM[0]
	c_pbc_t4_t4_mem0 = S.Task('c_pbc_t4_t4_mem0', length=1, delay_cost=1)
	c_pbc_t4_t4_mem0 += MAS_MEM[2]
	S += 112 < c_pbc_t4_t4_mem0
	S += c_pbc_t4_t4_mem0 <= c_pbc_t4_t4

	c_pbc_t4_t4_mem1 = S.Task('c_pbc_t4_t4_mem1', length=1, delay_cost=1)
	c_pbc_t4_t4_mem1 += MAS_MEM[1]
	S += 72 < c_pbc_t4_t4_mem1
	S += c_pbc_t4_t4_mem1 <= c_pbc_t4_t4

	c_pbc_t40 = S.Task('c_pbc_t40', length=2, delay_cost=1)
	c_pbc_t40 += alt(MAS)
	c_pbc_t40_in = S.Task('c_pbc_t40_in', length=1, delay_cost=1)
	c_pbc_t40_in += alt(MAS_in)
	S += c_pbc_t40_in*MAS_in[0]<=c_pbc_t40*MAS[0]

	S += c_pbc_t40_in*MAS_in[1]<=c_pbc_t40*MAS[1]

	S += c_pbc_t40_in*MAS_in[2]<=c_pbc_t40*MAS[2]

	S += c_pbc_t40_in*MAS_in[3]<=c_pbc_t40*MAS[3]

	c_pbc_t40_mem0 = S.Task('c_pbc_t40_mem0', length=1, delay_cost=1)
	c_pbc_t40_mem0 += MM_MEM[0]
	S += 118 < c_pbc_t40_mem0
	S += c_pbc_t40_mem0 <= c_pbc_t40

	c_pbc_t40_mem1 = S.Task('c_pbc_t40_mem1', length=1, delay_cost=1)
	c_pbc_t40_mem1 += MM_MEM[1]
	S += 128 < c_pbc_t40_mem1
	S += c_pbc_t40_mem1 <= c_pbc_t40

	c_pbc_t4_t5 = S.Task('c_pbc_t4_t5', length=2, delay_cost=1)
	c_pbc_t4_t5 += alt(MAS)
	c_pbc_t4_t5_in = S.Task('c_pbc_t4_t5_in', length=1, delay_cost=1)
	c_pbc_t4_t5_in += alt(MAS_in)
	S += c_pbc_t4_t5_in*MAS_in[0]<=c_pbc_t4_t5*MAS[0]

	S += c_pbc_t4_t5_in*MAS_in[1]<=c_pbc_t4_t5*MAS[1]

	S += c_pbc_t4_t5_in*MAS_in[2]<=c_pbc_t4_t5*MAS[2]

	S += c_pbc_t4_t5_in*MAS_in[3]<=c_pbc_t4_t5*MAS[3]

	c_pbc_t4_t5_mem0 = S.Task('c_pbc_t4_t5_mem0', length=1, delay_cost=1)
	c_pbc_t4_t5_mem0 += MM_MEM[0]
	S += 118 < c_pbc_t4_t5_mem0
	S += c_pbc_t4_t5_mem0 <= c_pbc_t4_t5

	c_pbc_t4_t5_mem1 = S.Task('c_pbc_t4_t5_mem1', length=1, delay_cost=1)
	c_pbc_t4_t5_mem1 += MM_MEM[1]
	S += 128 < c_pbc_t4_t5_mem1
	S += c_pbc_t4_t5_mem1 <= c_pbc_t4_t5

	c_pbc_t50 = S.Task('c_pbc_t50', length=2, delay_cost=1)
	c_pbc_t50 += alt(MAS)
	c_pbc_t50_in = S.Task('c_pbc_t50_in', length=1, delay_cost=1)
	c_pbc_t50_in += alt(MAS_in)
	S += c_pbc_t50_in*MAS_in[0]<=c_pbc_t50*MAS[0]

	S += c_pbc_t50_in*MAS_in[1]<=c_pbc_t50*MAS[1]

	S += c_pbc_t50_in*MAS_in[2]<=c_pbc_t50*MAS[2]

	S += c_pbc_t50_in*MAS_in[3]<=c_pbc_t50*MAS[3]

	c_pbc_t50_mem0 = S.Task('c_pbc_t50_mem0', length=1, delay_cost=1)
	c_pbc_t50_mem0 += MAS_MEM[2]
	S += 90 < c_pbc_t50_mem0
	S += c_pbc_t50_mem0 <= c_pbc_t50

	c_pbc_t50_mem1 = S.Task('c_pbc_t50_mem1', length=1, delay_cost=1)
	c_pbc_t50_mem1 += MAS_MEM[7]
	S += 123 < c_pbc_t50_mem1
	S += c_pbc_t50_mem1 <= c_pbc_t50

	c_pcb_t01 = S.Task('c_pcb_t01', length=2, delay_cost=1)
	c_pcb_t01 += alt(MAS)
	c_pcb_t01_in = S.Task('c_pcb_t01_in', length=1, delay_cost=1)
	c_pcb_t01_in += alt(MAS_in)
	S += c_pcb_t01_in*MAS_in[0]<=c_pcb_t01*MAS[0]

	S += c_pcb_t01_in*MAS_in[1]<=c_pcb_t01*MAS[1]

	S += c_pcb_t01_in*MAS_in[2]<=c_pcb_t01*MAS[2]

	S += c_pcb_t01_in*MAS_in[3]<=c_pcb_t01*MAS[3]

	c_pcb_t01_mem0 = S.Task('c_pcb_t01_mem0', length=1, delay_cost=1)
	c_pcb_t01_mem0 += MM_MEM[0]
	S += 122 < c_pcb_t01_mem0
	S += c_pcb_t01_mem0 <= c_pcb_t01

	c_pcb_t01_mem1 = S.Task('c_pcb_t01_mem1', length=1, delay_cost=1)
	c_pcb_t01_mem1 += MAS_MEM[7]
	S += 125 < c_pcb_t01_mem1
	S += c_pcb_t01_mem1 <= c_pcb_t01

	c_pcb_t4_t4 = S.Task('c_pcb_t4_t4', length=14, delay_cost=1)
	c_pcb_t4_t4 += alt(MM)
	c_pcb_t4_t4_in = S.Task('c_pcb_t4_t4_in', length=1, delay_cost=1)
	c_pcb_t4_t4_in += alt(MM_in)
	S += c_pcb_t4_t4_in*MM_in[0]<=c_pcb_t4_t4*MM[0]
	c_pcb_t4_t4_mem0 = S.Task('c_pcb_t4_t4_mem0', length=1, delay_cost=1)
	c_pcb_t4_t4_mem0 += MAS_MEM[0]
	S += 111 < c_pcb_t4_t4_mem0
	S += c_pcb_t4_t4_mem0 <= c_pcb_t4_t4

	c_pcb_t4_t4_mem1 = S.Task('c_pcb_t4_t4_mem1', length=1, delay_cost=1)
	c_pcb_t4_t4_mem1 += MAS_MEM[7]
	S += 73 < c_pcb_t4_t4_mem1
	S += c_pcb_t4_t4_mem1 <= c_pcb_t4_t4

	c_pcb_t40 = S.Task('c_pcb_t40', length=2, delay_cost=1)
	c_pcb_t40 += alt(MAS)
	c_pcb_t40_in = S.Task('c_pcb_t40_in', length=1, delay_cost=1)
	c_pcb_t40_in += alt(MAS_in)
	S += c_pcb_t40_in*MAS_in[0]<=c_pcb_t40*MAS[0]

	S += c_pcb_t40_in*MAS_in[1]<=c_pcb_t40*MAS[1]

	S += c_pcb_t40_in*MAS_in[2]<=c_pcb_t40*MAS[2]

	S += c_pcb_t40_in*MAS_in[3]<=c_pcb_t40*MAS[3]

	c_pcb_t40_mem0 = S.Task('c_pcb_t40_mem0', length=1, delay_cost=1)
	c_pcb_t40_mem0 += MM_MEM[0]
	S += 117 < c_pcb_t40_mem0
	S += c_pcb_t40_mem0 <= c_pcb_t40

	c_pcb_t40_mem1 = S.Task('c_pcb_t40_mem1', length=1, delay_cost=1)
	c_pcb_t40_mem1 += MM_MEM[1]
	S += 124 < c_pcb_t40_mem1
	S += c_pcb_t40_mem1 <= c_pcb_t40

	c_pcb_t4_t5 = S.Task('c_pcb_t4_t5', length=2, delay_cost=1)
	c_pcb_t4_t5 += alt(MAS)
	c_pcb_t4_t5_in = S.Task('c_pcb_t4_t5_in', length=1, delay_cost=1)
	c_pcb_t4_t5_in += alt(MAS_in)
	S += c_pcb_t4_t5_in*MAS_in[0]<=c_pcb_t4_t5*MAS[0]

	S += c_pcb_t4_t5_in*MAS_in[1]<=c_pcb_t4_t5*MAS[1]

	S += c_pcb_t4_t5_in*MAS_in[2]<=c_pcb_t4_t5*MAS[2]

	S += c_pcb_t4_t5_in*MAS_in[3]<=c_pcb_t4_t5*MAS[3]

	c_pcb_t4_t5_mem0 = S.Task('c_pcb_t4_t5_mem0', length=1, delay_cost=1)
	c_pcb_t4_t5_mem0 += MM_MEM[0]
	S += 117 < c_pcb_t4_t5_mem0
	S += c_pcb_t4_t5_mem0 <= c_pcb_t4_t5

	c_pcb_t4_t5_mem1 = S.Task('c_pcb_t4_t5_mem1', length=1, delay_cost=1)
	c_pcb_t4_t5_mem1 += MM_MEM[1]
	S += 124 < c_pcb_t4_t5_mem1
	S += c_pcb_t4_t5_mem1 <= c_pcb_t4_t5

	c_pcb_s00 = S.Task('c_pcb_s00', length=2, delay_cost=1)
	c_pcb_s00 += alt(MAS)
	c_pcb_s00_in = S.Task('c_pcb_s00_in', length=1, delay_cost=1)
	c_pcb_s00_in += alt(MAS_in)
	S += c_pcb_s00_in*MAS_in[0]<=c_pcb_s00*MAS[0]

	S += c_pcb_s00_in*MAS_in[1]<=c_pcb_s00*MAS[1]

	S += c_pcb_s00_in*MAS_in[2]<=c_pcb_s00*MAS[2]

	S += c_pcb_s00_in*MAS_in[3]<=c_pcb_s00*MAS[3]

	c_pcb_s00_mem0 = S.Task('c_pcb_s00_mem0', length=1, delay_cost=1)
	c_pcb_s00_mem0 += MAS_MEM[4]
	S += 112 < c_pcb_s00_mem0
	S += c_pcb_s00_mem0 <= c_pcb_s00

	c_pcb_s00_mem1 = S.Task('c_pcb_s00_mem1', length=1, delay_cost=1)
	c_pcb_s00_mem1 += MAS_MEM[7]
	S += 111 < c_pcb_s00_mem1
	S += c_pcb_s00_mem1 <= c_pcb_s00

	c_pcb_s01 = S.Task('c_pcb_s01', length=2, delay_cost=1)
	c_pcb_s01 += alt(MAS)
	c_pcb_s01_in = S.Task('c_pcb_s01_in', length=1, delay_cost=1)
	c_pcb_s01_in += alt(MAS_in)
	S += c_pcb_s01_in*MAS_in[0]<=c_pcb_s01*MAS[0]

	S += c_pcb_s01_in*MAS_in[1]<=c_pcb_s01*MAS[1]

	S += c_pcb_s01_in*MAS_in[2]<=c_pcb_s01*MAS[2]

	S += c_pcb_s01_in*MAS_in[3]<=c_pcb_s01*MAS[3]

	c_pcb_s01_mem0 = S.Task('c_pcb_s01_mem0', length=1, delay_cost=1)
	c_pcb_s01_mem0 += MAS_MEM[6]
	S += 111 < c_pcb_s01_mem0
	S += c_pcb_s01_mem0 <= c_pcb_s01

	c_pcb_s01_mem1 = S.Task('c_pcb_s01_mem1', length=1, delay_cost=1)
	c_pcb_s01_mem1 += MAS_MEM[5]
	S += 112 < c_pcb_s01_mem1
	S += c_pcb_s01_mem1 <= c_pcb_s01

	c_pcb_t50 = S.Task('c_pcb_t50', length=2, delay_cost=1)
	c_pcb_t50 += alt(MAS)
	c_pcb_t50_in = S.Task('c_pcb_t50_in', length=1, delay_cost=1)
	c_pcb_t50_in += alt(MAS_in)
	S += c_pcb_t50_in*MAS_in[0]<=c_pcb_t50*MAS[0]

	S += c_pcb_t50_in*MAS_in[1]<=c_pcb_t50*MAS[1]

	S += c_pcb_t50_in*MAS_in[2]<=c_pcb_t50*MAS[2]

	S += c_pcb_t50_in*MAS_in[3]<=c_pcb_t50*MAS[3]

	c_pcb_t50_mem0 = S.Task('c_pcb_t50_mem0', length=1, delay_cost=1)
	c_pcb_t50_mem0 += MAS_MEM[6]
	S += 126 < c_pcb_t50_mem0
	S += c_pcb_t50_mem0 <= c_pcb_t50

	c_pcb_t50_mem1 = S.Task('c_pcb_t50_mem1', length=1, delay_cost=1)
	c_pcb_t50_mem1 += MAS_MEM[5]
	S += 112 < c_pcb_t50_mem1
	S += c_pcb_t50_mem1 <= c_pcb_t50

	c_paa_t01 = S.Task('c_paa_t01', length=2, delay_cost=1)
	c_paa_t01 += alt(MAS)
	c_paa_t01_in = S.Task('c_paa_t01_in', length=1, delay_cost=1)
	c_paa_t01_in += alt(MAS_in)
	S += c_paa_t01_in*MAS_in[0]<=c_paa_t01*MAS[0]

	S += c_paa_t01_in*MAS_in[1]<=c_paa_t01*MAS[1]

	S += c_paa_t01_in*MAS_in[2]<=c_paa_t01*MAS[2]

	S += c_paa_t01_in*MAS_in[3]<=c_paa_t01*MAS[3]

	c_paa_t01_mem0 = S.Task('c_paa_t01_mem0', length=1, delay_cost=1)
	c_paa_t01_mem0 += MM_MEM[0]
	S += 127 < c_paa_t01_mem0
	S += c_paa_t01_mem0 <= c_paa_t01

	c_paa_t01_mem1 = S.Task('c_paa_t01_mem1', length=1, delay_cost=1)
	c_paa_t01_mem1 += MAS_MEM[1]
	S += 122 < c_paa_t01_mem1
	S += c_paa_t01_mem1 <= c_paa_t01

	c_paa_t4_t4 = S.Task('c_paa_t4_t4', length=14, delay_cost=1)
	c_paa_t4_t4 += alt(MM)
	c_paa_t4_t4_in = S.Task('c_paa_t4_t4_in', length=1, delay_cost=1)
	c_paa_t4_t4_in += alt(MM_in)
	S += c_paa_t4_t4_in*MM_in[0]<=c_paa_t4_t4*MM[0]
	c_paa_t4_t4_mem0 = S.Task('c_paa_t4_t4_mem0', length=1, delay_cost=1)
	c_paa_t4_t4_mem0 += MAS_MEM[6]
	S += 112 < c_paa_t4_t4_mem0
	S += c_paa_t4_t4_mem0 <= c_paa_t4_t4

	c_paa_t4_t4_mem1 = S.Task('c_paa_t4_t4_mem1', length=1, delay_cost=1)
	c_paa_t4_t4_mem1 += MAS_MEM[7]
	S += 75 < c_paa_t4_t4_mem1
	S += c_paa_t4_t4_mem1 <= c_paa_t4_t4

	c_paa_t40 = S.Task('c_paa_t40', length=2, delay_cost=1)
	c_paa_t40 += alt(MAS)
	c_paa_t40_in = S.Task('c_paa_t40_in', length=1, delay_cost=1)
	c_paa_t40_in += alt(MAS_in)
	S += c_paa_t40_in*MAS_in[0]<=c_paa_t40*MAS[0]

	S += c_paa_t40_in*MAS_in[1]<=c_paa_t40*MAS[1]

	S += c_paa_t40_in*MAS_in[2]<=c_paa_t40*MAS[2]

	S += c_paa_t40_in*MAS_in[3]<=c_paa_t40*MAS[3]

	c_paa_t40_mem0 = S.Task('c_paa_t40_mem0', length=1, delay_cost=1)
	c_paa_t40_mem0 += MM_MEM[0]
	S += 125 < c_paa_t40_mem0
	S += c_paa_t40_mem0 <= c_paa_t40

	c_paa_t40_mem1 = S.Task('c_paa_t40_mem1', length=1, delay_cost=1)
	c_paa_t40_mem1 += MM_MEM[1]
	S += 123 < c_paa_t40_mem1
	S += c_paa_t40_mem1 <= c_paa_t40

	c_paa_t4_t5 = S.Task('c_paa_t4_t5', length=2, delay_cost=1)
	c_paa_t4_t5 += alt(MAS)
	c_paa_t4_t5_in = S.Task('c_paa_t4_t5_in', length=1, delay_cost=1)
	c_paa_t4_t5_in += alt(MAS_in)
	S += c_paa_t4_t5_in*MAS_in[0]<=c_paa_t4_t5*MAS[0]

	S += c_paa_t4_t5_in*MAS_in[1]<=c_paa_t4_t5*MAS[1]

	S += c_paa_t4_t5_in*MAS_in[2]<=c_paa_t4_t5*MAS[2]

	S += c_paa_t4_t5_in*MAS_in[3]<=c_paa_t4_t5*MAS[3]

	c_paa_t4_t5_mem0 = S.Task('c_paa_t4_t5_mem0', length=1, delay_cost=1)
	c_paa_t4_t5_mem0 += MM_MEM[0]
	S += 125 < c_paa_t4_t5_mem0
	S += c_paa_t4_t5_mem0 <= c_paa_t4_t5

	c_paa_t4_t5_mem1 = S.Task('c_paa_t4_t5_mem1', length=1, delay_cost=1)
	c_paa_t4_t5_mem1 += MM_MEM[1]
	S += 123 < c_paa_t4_t5_mem1
	S += c_paa_t4_t5_mem1 <= c_paa_t4_t5

	c_paa_s00 = S.Task('c_paa_s00', length=2, delay_cost=1)
	c_paa_s00 += alt(MAS)
	c_paa_s00_in = S.Task('c_paa_s00_in', length=1, delay_cost=1)
	c_paa_s00_in += alt(MAS_in)
	S += c_paa_s00_in*MAS_in[0]<=c_paa_s00*MAS[0]

	S += c_paa_s00_in*MAS_in[1]<=c_paa_s00*MAS[1]

	S += c_paa_s00_in*MAS_in[2]<=c_paa_s00*MAS[2]

	S += c_paa_s00_in*MAS_in[3]<=c_paa_s00*MAS[3]

	c_paa_s00_mem0 = S.Task('c_paa_s00_mem0', length=1, delay_cost=1)
	c_paa_s00_mem0 += MAS_MEM[0]
	S += 110 < c_paa_s00_mem0
	S += c_paa_s00_mem0 <= c_paa_s00

	c_paa_s00_mem1 = S.Task('c_paa_s00_mem1', length=1, delay_cost=1)
	c_paa_s00_mem1 += MAS_MEM[5]
	S += 113 < c_paa_s00_mem1
	S += c_paa_s00_mem1 <= c_paa_s00

	c_paa_s01 = S.Task('c_paa_s01', length=2, delay_cost=1)
	c_paa_s01 += alt(MAS)
	c_paa_s01_in = S.Task('c_paa_s01_in', length=1, delay_cost=1)
	c_paa_s01_in += alt(MAS_in)
	S += c_paa_s01_in*MAS_in[0]<=c_paa_s01*MAS[0]

	S += c_paa_s01_in*MAS_in[1]<=c_paa_s01*MAS[1]

	S += c_paa_s01_in*MAS_in[2]<=c_paa_s01*MAS[2]

	S += c_paa_s01_in*MAS_in[3]<=c_paa_s01*MAS[3]

	c_paa_s01_mem0 = S.Task('c_paa_s01_mem0', length=1, delay_cost=1)
	c_paa_s01_mem0 += MAS_MEM[4]
	S += 113 < c_paa_s01_mem0
	S += c_paa_s01_mem0 <= c_paa_s01

	c_paa_s01_mem1 = S.Task('c_paa_s01_mem1', length=1, delay_cost=1)
	c_paa_s01_mem1 += MAS_MEM[1]
	S += 110 < c_paa_s01_mem1
	S += c_paa_s01_mem1 <= c_paa_s01

	c_paa_t50 = S.Task('c_paa_t50', length=2, delay_cost=1)
	c_paa_t50 += alt(MAS)
	c_paa_t50_in = S.Task('c_paa_t50_in', length=1, delay_cost=1)
	c_paa_t50_in += alt(MAS_in)
	S += c_paa_t50_in*MAS_in[0]<=c_paa_t50*MAS[0]

	S += c_paa_t50_in*MAS_in[1]<=c_paa_t50*MAS[1]

	S += c_paa_t50_in*MAS_in[2]<=c_paa_t50*MAS[2]

	S += c_paa_t50_in*MAS_in[3]<=c_paa_t50*MAS[3]

	c_paa_t50_mem0 = S.Task('c_paa_t50_mem0', length=1, delay_cost=1)
	c_paa_t50_mem0 += MAS_MEM[4]
	S += 121 < c_paa_t50_mem0
	S += c_paa_t50_mem0 <= c_paa_t50

	c_paa_t50_mem1 = S.Task('c_paa_t50_mem1', length=1, delay_cost=1)
	c_paa_t50_mem1 += MAS_MEM[1]
	S += 110 < c_paa_t50_mem1
	S += c_paa_t50_mem1 <= c_paa_t50

	c_pbc_t41 = S.Task('c_pbc_t41', length=2, delay_cost=1)
	c_pbc_t41 += alt(MAS)
	c_pbc_t41_in = S.Task('c_pbc_t41_in', length=1, delay_cost=1)
	c_pbc_t41_in += alt(MAS_in)
	S += c_pbc_t41_in*MAS_in[0]<=c_pbc_t41*MAS[0]

	S += c_pbc_t41_in*MAS_in[1]<=c_pbc_t41*MAS[1]

	S += c_pbc_t41_in*MAS_in[2]<=c_pbc_t41*MAS[2]

	S += c_pbc_t41_in*MAS_in[3]<=c_pbc_t41*MAS[3]

	c_pbc_t41_mem0 = S.Task('c_pbc_t41_mem0', length=1, delay_cost=1)
	c_pbc_t41_mem0 += alt(MM_MEM)
	S += (c_pbc_t4_t4*MM[0])-1 < c_pbc_t41_mem0*MM_MEM[0]
	S += c_pbc_t41_mem0 <= c_pbc_t41

	c_pbc_t41_mem1 = S.Task('c_pbc_t41_mem1', length=1, delay_cost=1)
	c_pbc_t41_mem1 += alt(MAS_MEM)
	S += (c_pbc_t4_t5*MAS[0])-1 < c_pbc_t41_mem1*MAS_MEM[1]
	S += (c_pbc_t4_t5*MAS[1])-1 < c_pbc_t41_mem1*MAS_MEM[3]
	S += (c_pbc_t4_t5*MAS[2])-1 < c_pbc_t41_mem1*MAS_MEM[5]
	S += (c_pbc_t4_t5*MAS[3])-1 < c_pbc_t41_mem1*MAS_MEM[7]
	S += c_pbc_t41_mem1 <= c_pbc_t41

	c_pbc_s00 = S.Task('c_pbc_s00', length=2, delay_cost=1)
	c_pbc_s00 += alt(MAS)
	c_pbc_s00_in = S.Task('c_pbc_s00_in', length=1, delay_cost=1)
	c_pbc_s00_in += alt(MAS_in)
	S += c_pbc_s00_in*MAS_in[0]<=c_pbc_s00*MAS[0]

	S += c_pbc_s00_in*MAS_in[1]<=c_pbc_s00*MAS[1]

	S += c_pbc_s00_in*MAS_in[2]<=c_pbc_s00*MAS[2]

	S += c_pbc_s00_in*MAS_in[3]<=c_pbc_s00*MAS[3]

	c_pbc_s00_mem0 = S.Task('c_pbc_s00_mem0', length=1, delay_cost=1)
	c_pbc_s00_mem0 += MAS_MEM[6]
	S += 123 < c_pbc_s00_mem0
	S += c_pbc_s00_mem0 <= c_pbc_s00

	c_pbc_s00_mem1 = S.Task('c_pbc_s00_mem1', length=1, delay_cost=1)
	c_pbc_s00_mem1 += alt(MAS_MEM)
	S += (c_pbc_t11*MAS[0])-1 < c_pbc_s00_mem1*MAS_MEM[1]
	S += (c_pbc_t11*MAS[1])-1 < c_pbc_s00_mem1*MAS_MEM[3]
	S += (c_pbc_t11*MAS[2])-1 < c_pbc_s00_mem1*MAS_MEM[5]
	S += (c_pbc_t11*MAS[3])-1 < c_pbc_s00_mem1*MAS_MEM[7]
	S += c_pbc_s00_mem1 <= c_pbc_s00

	c_pbc_s01 = S.Task('c_pbc_s01', length=2, delay_cost=1)
	c_pbc_s01 += alt(MAS)
	c_pbc_s01_in = S.Task('c_pbc_s01_in', length=1, delay_cost=1)
	c_pbc_s01_in += alt(MAS_in)
	S += c_pbc_s01_in*MAS_in[0]<=c_pbc_s01*MAS[0]

	S += c_pbc_s01_in*MAS_in[1]<=c_pbc_s01*MAS[1]

	S += c_pbc_s01_in*MAS_in[2]<=c_pbc_s01*MAS[2]

	S += c_pbc_s01_in*MAS_in[3]<=c_pbc_s01*MAS[3]

	c_pbc_s01_mem0 = S.Task('c_pbc_s01_mem0', length=1, delay_cost=1)
	c_pbc_s01_mem0 += alt(MAS_MEM)
	S += (c_pbc_t11*MAS[0])-1 < c_pbc_s01_mem0*MAS_MEM[0]
	S += (c_pbc_t11*MAS[1])-1 < c_pbc_s01_mem0*MAS_MEM[2]
	S += (c_pbc_t11*MAS[2])-1 < c_pbc_s01_mem0*MAS_MEM[4]
	S += (c_pbc_t11*MAS[3])-1 < c_pbc_s01_mem0*MAS_MEM[6]
	S += c_pbc_s01_mem0 <= c_pbc_s01

	c_pbc_s01_mem1 = S.Task('c_pbc_s01_mem1', length=1, delay_cost=1)
	c_pbc_s01_mem1 += MAS_MEM[7]
	S += 123 < c_pbc_s01_mem1
	S += c_pbc_s01_mem1 <= c_pbc_s01

	c_pbc_t51 = S.Task('c_pbc_t51', length=2, delay_cost=1)
	c_pbc_t51 += alt(MAS)
	c_pbc_t51_in = S.Task('c_pbc_t51_in', length=1, delay_cost=1)
	c_pbc_t51_in += alt(MAS_in)
	S += c_pbc_t51_in*MAS_in[0]<=c_pbc_t51*MAS[0]

	S += c_pbc_t51_in*MAS_in[1]<=c_pbc_t51*MAS[1]

	S += c_pbc_t51_in*MAS_in[2]<=c_pbc_t51*MAS[2]

	S += c_pbc_t51_in*MAS_in[3]<=c_pbc_t51*MAS[3]

	c_pbc_t51_mem0 = S.Task('c_pbc_t51_mem0', length=1, delay_cost=1)
	c_pbc_t51_mem0 += MAS_MEM[0]
	S += 104 < c_pbc_t51_mem0
	S += c_pbc_t51_mem0 <= c_pbc_t51

	c_pbc_t51_mem1 = S.Task('c_pbc_t51_mem1', length=1, delay_cost=1)
	c_pbc_t51_mem1 += alt(MAS_MEM)
	S += (c_pbc_t11*MAS[0])-1 < c_pbc_t51_mem1*MAS_MEM[1]
	S += (c_pbc_t11*MAS[1])-1 < c_pbc_t51_mem1*MAS_MEM[3]
	S += (c_pbc_t11*MAS[2])-1 < c_pbc_t51_mem1*MAS_MEM[5]
	S += (c_pbc_t11*MAS[3])-1 < c_pbc_t51_mem1*MAS_MEM[7]
	S += c_pbc_t51_mem1 <= c_pbc_t51

	c_pbc10 = S.Task('c_pbc10', length=2, delay_cost=1)
	c_pbc10 += alt(MAS)
	c_pbc10_in = S.Task('c_pbc10_in', length=1, delay_cost=1)
	c_pbc10_in += alt(MAS_in)
	S += c_pbc10_in*MAS_in[0]<=c_pbc10*MAS[0]

	S += c_pbc10_in*MAS_in[1]<=c_pbc10*MAS[1]

	S += c_pbc10_in*MAS_in[2]<=c_pbc10*MAS[2]

	S += c_pbc10_in*MAS_in[3]<=c_pbc10*MAS[3]

	c_pbc10_mem0 = S.Task('c_pbc10_mem0', length=1, delay_cost=1)
	c_pbc10_mem0 += alt(MAS_MEM)
	S += (c_pbc_t40*MAS[0])-1 < c_pbc10_mem0*MAS_MEM[0]
	S += (c_pbc_t40*MAS[1])-1 < c_pbc10_mem0*MAS_MEM[2]
	S += (c_pbc_t40*MAS[2])-1 < c_pbc10_mem0*MAS_MEM[4]
	S += (c_pbc_t40*MAS[3])-1 < c_pbc10_mem0*MAS_MEM[6]
	S += c_pbc10_mem0 <= c_pbc10

	c_pbc10_mem1 = S.Task('c_pbc10_mem1', length=1, delay_cost=1)
	c_pbc10_mem1 += alt(MAS_MEM)
	S += (c_pbc_t50*MAS[0])-1 < c_pbc10_mem1*MAS_MEM[1]
	S += (c_pbc_t50*MAS[1])-1 < c_pbc10_mem1*MAS_MEM[3]
	S += (c_pbc_t50*MAS[2])-1 < c_pbc10_mem1*MAS_MEM[5]
	S += (c_pbc_t50*MAS[3])-1 < c_pbc10_mem1*MAS_MEM[7]
	S += c_pbc10_mem1 <= c_pbc10

	c_pcb_t41 = S.Task('c_pcb_t41', length=2, delay_cost=1)
	c_pcb_t41 += alt(MAS)
	c_pcb_t41_in = S.Task('c_pcb_t41_in', length=1, delay_cost=1)
	c_pcb_t41_in += alt(MAS_in)
	S += c_pcb_t41_in*MAS_in[0]<=c_pcb_t41*MAS[0]

	S += c_pcb_t41_in*MAS_in[1]<=c_pcb_t41*MAS[1]

	S += c_pcb_t41_in*MAS_in[2]<=c_pcb_t41*MAS[2]

	S += c_pcb_t41_in*MAS_in[3]<=c_pcb_t41*MAS[3]

	c_pcb_t41_mem0 = S.Task('c_pcb_t41_mem0', length=1, delay_cost=1)
	c_pcb_t41_mem0 += alt(MM_MEM)
	S += (c_pcb_t4_t4*MM[0])-1 < c_pcb_t41_mem0*MM_MEM[0]
	S += c_pcb_t41_mem0 <= c_pcb_t41

	c_pcb_t41_mem1 = S.Task('c_pcb_t41_mem1', length=1, delay_cost=1)
	c_pcb_t41_mem1 += alt(MAS_MEM)
	S += (c_pcb_t4_t5*MAS[0])-1 < c_pcb_t41_mem1*MAS_MEM[1]
	S += (c_pcb_t4_t5*MAS[1])-1 < c_pcb_t41_mem1*MAS_MEM[3]
	S += (c_pcb_t4_t5*MAS[2])-1 < c_pcb_t41_mem1*MAS_MEM[5]
	S += (c_pcb_t4_t5*MAS[3])-1 < c_pcb_t41_mem1*MAS_MEM[7]
	S += c_pcb_t41_mem1 <= c_pcb_t41

	c_pcb00 = S.Task('c_pcb00', length=2, delay_cost=1)
	c_pcb00 += alt(MAS)
	c_pcb00_in = S.Task('c_pcb00_in', length=1, delay_cost=1)
	c_pcb00_in += alt(MAS_in)
	S += c_pcb00_in*MAS_in[0]<=c_pcb00*MAS[0]

	S += c_pcb00_in*MAS_in[1]<=c_pcb00*MAS[1]

	S += c_pcb00_in*MAS_in[2]<=c_pcb00*MAS[2]

	S += c_pcb00_in*MAS_in[3]<=c_pcb00*MAS[3]

	c_pcb00_mem0 = S.Task('c_pcb00_mem0', length=1, delay_cost=1)
	c_pcb00_mem0 += MAS_MEM[6]
	S += 126 < c_pcb00_mem0
	S += c_pcb00_mem0 <= c_pcb00

	c_pcb00_mem1 = S.Task('c_pcb00_mem1', length=1, delay_cost=1)
	c_pcb00_mem1 += alt(MAS_MEM)
	S += (c_pcb_s00*MAS[0])-1 < c_pcb00_mem1*MAS_MEM[1]
	S += (c_pcb_s00*MAS[1])-1 < c_pcb00_mem1*MAS_MEM[3]
	S += (c_pcb_s00*MAS[2])-1 < c_pcb00_mem1*MAS_MEM[5]
	S += (c_pcb_s00*MAS[3])-1 < c_pcb00_mem1*MAS_MEM[7]
	S += c_pcb00_mem1 <= c_pcb00

	c_pcb01 = S.Task('c_pcb01', length=2, delay_cost=1)
	c_pcb01 += alt(MAS)
	c_pcb01_in = S.Task('c_pcb01_in', length=1, delay_cost=1)
	c_pcb01_in += alt(MAS_in)
	S += c_pcb01_in*MAS_in[0]<=c_pcb01*MAS[0]

	S += c_pcb01_in*MAS_in[1]<=c_pcb01*MAS[1]

	S += c_pcb01_in*MAS_in[2]<=c_pcb01*MAS[2]

	S += c_pcb01_in*MAS_in[3]<=c_pcb01*MAS[3]

	c_pcb01_mem0 = S.Task('c_pcb01_mem0', length=1, delay_cost=1)
	c_pcb01_mem0 += alt(MAS_MEM)
	S += (c_pcb_t01*MAS[0])-1 < c_pcb01_mem0*MAS_MEM[0]
	S += (c_pcb_t01*MAS[1])-1 < c_pcb01_mem0*MAS_MEM[2]
	S += (c_pcb_t01*MAS[2])-1 < c_pcb01_mem0*MAS_MEM[4]
	S += (c_pcb_t01*MAS[3])-1 < c_pcb01_mem0*MAS_MEM[6]
	S += c_pcb01_mem0 <= c_pcb01

	c_pcb01_mem1 = S.Task('c_pcb01_mem1', length=1, delay_cost=1)
	c_pcb01_mem1 += alt(MAS_MEM)
	S += (c_pcb_s01*MAS[0])-1 < c_pcb01_mem1*MAS_MEM[1]
	S += (c_pcb_s01*MAS[1])-1 < c_pcb01_mem1*MAS_MEM[3]
	S += (c_pcb_s01*MAS[2])-1 < c_pcb01_mem1*MAS_MEM[5]
	S += (c_pcb_s01*MAS[3])-1 < c_pcb01_mem1*MAS_MEM[7]
	S += c_pcb01_mem1 <= c_pcb01

	c_pcb_t51 = S.Task('c_pcb_t51', length=2, delay_cost=1)
	c_pcb_t51 += alt(MAS)
	c_pcb_t51_in = S.Task('c_pcb_t51_in', length=1, delay_cost=1)
	c_pcb_t51_in += alt(MAS_in)
	S += c_pcb_t51_in*MAS_in[0]<=c_pcb_t51*MAS[0]

	S += c_pcb_t51_in*MAS_in[1]<=c_pcb_t51*MAS[1]

	S += c_pcb_t51_in*MAS_in[2]<=c_pcb_t51*MAS[2]

	S += c_pcb_t51_in*MAS_in[3]<=c_pcb_t51*MAS[3]

	c_pcb_t51_mem0 = S.Task('c_pcb_t51_mem0', length=1, delay_cost=1)
	c_pcb_t51_mem0 += alt(MAS_MEM)
	S += (c_pcb_t01*MAS[0])-1 < c_pcb_t51_mem0*MAS_MEM[0]
	S += (c_pcb_t01*MAS[1])-1 < c_pcb_t51_mem0*MAS_MEM[2]
	S += (c_pcb_t01*MAS[2])-1 < c_pcb_t51_mem0*MAS_MEM[4]
	S += (c_pcb_t01*MAS[3])-1 < c_pcb_t51_mem0*MAS_MEM[6]
	S += c_pcb_t51_mem0 <= c_pcb_t51

	c_pcb_t51_mem1 = S.Task('c_pcb_t51_mem1', length=1, delay_cost=1)
	c_pcb_t51_mem1 += MAS_MEM[7]
	S += 111 < c_pcb_t51_mem1
	S += c_pcb_t51_mem1 <= c_pcb_t51

	c_pcb10 = S.Task('c_pcb10', length=2, delay_cost=1)
	c_pcb10 += alt(MAS)
	c_pcb10_in = S.Task('c_pcb10_in', length=1, delay_cost=1)
	c_pcb10_in += alt(MAS_in)
	S += c_pcb10_in*MAS_in[0]<=c_pcb10*MAS[0]

	S += c_pcb10_in*MAS_in[1]<=c_pcb10*MAS[1]

	S += c_pcb10_in*MAS_in[2]<=c_pcb10*MAS[2]

	S += c_pcb10_in*MAS_in[3]<=c_pcb10*MAS[3]

	c_pcb10_mem0 = S.Task('c_pcb10_mem0', length=1, delay_cost=1)
	c_pcb10_mem0 += alt(MAS_MEM)
	S += (c_pcb_t40*MAS[0])-1 < c_pcb10_mem0*MAS_MEM[0]
	S += (c_pcb_t40*MAS[1])-1 < c_pcb10_mem0*MAS_MEM[2]
	S += (c_pcb_t40*MAS[2])-1 < c_pcb10_mem0*MAS_MEM[4]
	S += (c_pcb_t40*MAS[3])-1 < c_pcb10_mem0*MAS_MEM[6]
	S += c_pcb10_mem0 <= c_pcb10

	c_pcb10_mem1 = S.Task('c_pcb10_mem1', length=1, delay_cost=1)
	c_pcb10_mem1 += alt(MAS_MEM)
	S += (c_pcb_t50*MAS[0])-1 < c_pcb10_mem1*MAS_MEM[1]
	S += (c_pcb_t50*MAS[1])-1 < c_pcb10_mem1*MAS_MEM[3]
	S += (c_pcb_t50*MAS[2])-1 < c_pcb10_mem1*MAS_MEM[5]
	S += (c_pcb_t50*MAS[3])-1 < c_pcb10_mem1*MAS_MEM[7]
	S += c_pcb10_mem1 <= c_pcb10

	c_paa_t41 = S.Task('c_paa_t41', length=2, delay_cost=1)
	c_paa_t41 += alt(MAS)
	c_paa_t41_in = S.Task('c_paa_t41_in', length=1, delay_cost=1)
	c_paa_t41_in += alt(MAS_in)
	S += c_paa_t41_in*MAS_in[0]<=c_paa_t41*MAS[0]

	S += c_paa_t41_in*MAS_in[1]<=c_paa_t41*MAS[1]

	S += c_paa_t41_in*MAS_in[2]<=c_paa_t41*MAS[2]

	S += c_paa_t41_in*MAS_in[3]<=c_paa_t41*MAS[3]

	c_paa_t41_mem0 = S.Task('c_paa_t41_mem0', length=1, delay_cost=1)
	c_paa_t41_mem0 += alt(MM_MEM)
	S += (c_paa_t4_t4*MM[0])-1 < c_paa_t41_mem0*MM_MEM[0]
	S += c_paa_t41_mem0 <= c_paa_t41

	c_paa_t41_mem1 = S.Task('c_paa_t41_mem1', length=1, delay_cost=1)
	c_paa_t41_mem1 += alt(MAS_MEM)
	S += (c_paa_t4_t5*MAS[0])-1 < c_paa_t41_mem1*MAS_MEM[1]
	S += (c_paa_t4_t5*MAS[1])-1 < c_paa_t41_mem1*MAS_MEM[3]
	S += (c_paa_t4_t5*MAS[2])-1 < c_paa_t41_mem1*MAS_MEM[5]
	S += (c_paa_t4_t5*MAS[3])-1 < c_paa_t41_mem1*MAS_MEM[7]
	S += c_paa_t41_mem1 <= c_paa_t41

	c_paa00 = S.Task('c_paa00', length=2, delay_cost=1)
	c_paa00 += alt(MAS)
	c_paa00_in = S.Task('c_paa00_in', length=1, delay_cost=1)
	c_paa00_in += alt(MAS_in)
	S += c_paa00_in*MAS_in[0]<=c_paa00*MAS[0]

	S += c_paa00_in*MAS_in[1]<=c_paa00*MAS[1]

	S += c_paa00_in*MAS_in[2]<=c_paa00*MAS[2]

	S += c_paa00_in*MAS_in[3]<=c_paa00*MAS[3]

	c_paa00_mem0 = S.Task('c_paa00_mem0', length=1, delay_cost=1)
	c_paa00_mem0 += MAS_MEM[4]
	S += 121 < c_paa00_mem0
	S += c_paa00_mem0 <= c_paa00

	c_paa00_mem1 = S.Task('c_paa00_mem1', length=1, delay_cost=1)
	c_paa00_mem1 += alt(MAS_MEM)
	S += (c_paa_s00*MAS[0])-1 < c_paa00_mem1*MAS_MEM[1]
	S += (c_paa_s00*MAS[1])-1 < c_paa00_mem1*MAS_MEM[3]
	S += (c_paa_s00*MAS[2])-1 < c_paa00_mem1*MAS_MEM[5]
	S += (c_paa_s00*MAS[3])-1 < c_paa00_mem1*MAS_MEM[7]
	S += c_paa00_mem1 <= c_paa00

	c_paa01 = S.Task('c_paa01', length=2, delay_cost=1)
	c_paa01 += alt(MAS)
	c_paa01_in = S.Task('c_paa01_in', length=1, delay_cost=1)
	c_paa01_in += alt(MAS_in)
	S += c_paa01_in*MAS_in[0]<=c_paa01*MAS[0]

	S += c_paa01_in*MAS_in[1]<=c_paa01*MAS[1]

	S += c_paa01_in*MAS_in[2]<=c_paa01*MAS[2]

	S += c_paa01_in*MAS_in[3]<=c_paa01*MAS[3]

	c_paa01_mem0 = S.Task('c_paa01_mem0', length=1, delay_cost=1)
	c_paa01_mem0 += alt(MAS_MEM)
	S += (c_paa_t01*MAS[0])-1 < c_paa01_mem0*MAS_MEM[0]
	S += (c_paa_t01*MAS[1])-1 < c_paa01_mem0*MAS_MEM[2]
	S += (c_paa_t01*MAS[2])-1 < c_paa01_mem0*MAS_MEM[4]
	S += (c_paa_t01*MAS[3])-1 < c_paa01_mem0*MAS_MEM[6]
	S += c_paa01_mem0 <= c_paa01

	c_paa01_mem1 = S.Task('c_paa01_mem1', length=1, delay_cost=1)
	c_paa01_mem1 += alt(MAS_MEM)
	S += (c_paa_s01*MAS[0])-1 < c_paa01_mem1*MAS_MEM[1]
	S += (c_paa_s01*MAS[1])-1 < c_paa01_mem1*MAS_MEM[3]
	S += (c_paa_s01*MAS[2])-1 < c_paa01_mem1*MAS_MEM[5]
	S += (c_paa_s01*MAS[3])-1 < c_paa01_mem1*MAS_MEM[7]
	S += c_paa01_mem1 <= c_paa01

	c_paa_t51 = S.Task('c_paa_t51', length=2, delay_cost=1)
	c_paa_t51 += alt(MAS)
	c_paa_t51_in = S.Task('c_paa_t51_in', length=1, delay_cost=1)
	c_paa_t51_in += alt(MAS_in)
	S += c_paa_t51_in*MAS_in[0]<=c_paa_t51*MAS[0]

	S += c_paa_t51_in*MAS_in[1]<=c_paa_t51*MAS[1]

	S += c_paa_t51_in*MAS_in[2]<=c_paa_t51*MAS[2]

	S += c_paa_t51_in*MAS_in[3]<=c_paa_t51*MAS[3]

	c_paa_t51_mem0 = S.Task('c_paa_t51_mem0', length=1, delay_cost=1)
	c_paa_t51_mem0 += alt(MAS_MEM)
	S += (c_paa_t01*MAS[0])-1 < c_paa_t51_mem0*MAS_MEM[0]
	S += (c_paa_t01*MAS[1])-1 < c_paa_t51_mem0*MAS_MEM[2]
	S += (c_paa_t01*MAS[2])-1 < c_paa_t51_mem0*MAS_MEM[4]
	S += (c_paa_t01*MAS[3])-1 < c_paa_t51_mem0*MAS_MEM[6]
	S += c_paa_t51_mem0 <= c_paa_t51

	c_paa_t51_mem1 = S.Task('c_paa_t51_mem1', length=1, delay_cost=1)
	c_paa_t51_mem1 += MAS_MEM[5]
	S += 113 < c_paa_t51_mem1
	S += c_paa_t51_mem1 <= c_paa_t51

	c_paa10 = S.Task('c_paa10', length=2, delay_cost=1)
	c_paa10 += alt(MAS)
	c_paa10_in = S.Task('c_paa10_in', length=1, delay_cost=1)
	c_paa10_in += alt(MAS_in)
	S += c_paa10_in*MAS_in[0]<=c_paa10*MAS[0]

	S += c_paa10_in*MAS_in[1]<=c_paa10*MAS[1]

	S += c_paa10_in*MAS_in[2]<=c_paa10*MAS[2]

	S += c_paa10_in*MAS_in[3]<=c_paa10*MAS[3]

	c_paa10_mem0 = S.Task('c_paa10_mem0', length=1, delay_cost=1)
	c_paa10_mem0 += alt(MAS_MEM)
	S += (c_paa_t40*MAS[0])-1 < c_paa10_mem0*MAS_MEM[0]
	S += (c_paa_t40*MAS[1])-1 < c_paa10_mem0*MAS_MEM[2]
	S += (c_paa_t40*MAS[2])-1 < c_paa10_mem0*MAS_MEM[4]
	S += (c_paa_t40*MAS[3])-1 < c_paa10_mem0*MAS_MEM[6]
	S += c_paa10_mem0 <= c_paa10

	c_paa10_mem1 = S.Task('c_paa10_mem1', length=1, delay_cost=1)
	c_paa10_mem1 += alt(MAS_MEM)
	S += (c_paa_t50*MAS[0])-1 < c_paa10_mem1*MAS_MEM[1]
	S += (c_paa_t50*MAS[1])-1 < c_paa10_mem1*MAS_MEM[3]
	S += (c_paa_t50*MAS[2])-1 < c_paa10_mem1*MAS_MEM[5]
	S += (c_paa_t50*MAS[3])-1 < c_paa10_mem1*MAS_MEM[7]
	S += c_paa10_mem1 <= c_paa10

	c_pbc00 = S.Task('c_pbc00', length=2, delay_cost=1)
	c_pbc00 += alt(MAS)
	c_pbc00_in = S.Task('c_pbc00_in', length=1, delay_cost=1)
	c_pbc00_in += alt(MAS_in)
	S += c_pbc00_in*MAS_in[0]<=c_pbc00*MAS[0]

	S += c_pbc00_in*MAS_in[1]<=c_pbc00*MAS[1]

	S += c_pbc00_in*MAS_in[2]<=c_pbc00*MAS[2]

	S += c_pbc00_in*MAS_in[3]<=c_pbc00*MAS[3]

	c_pbc00_mem0 = S.Task('c_pbc00_mem0', length=1, delay_cost=1)
	c_pbc00_mem0 += MAS_MEM[2]
	S += 90 < c_pbc00_mem0
	S += c_pbc00_mem0 <= c_pbc00

	c_pbc00_mem1 = S.Task('c_pbc00_mem1', length=1, delay_cost=1)
	c_pbc00_mem1 += alt(MAS_MEM)
	S += (c_pbc_s00*MAS[0])-1 < c_pbc00_mem1*MAS_MEM[1]
	S += (c_pbc_s00*MAS[1])-1 < c_pbc00_mem1*MAS_MEM[3]
	S += (c_pbc_s00*MAS[2])-1 < c_pbc00_mem1*MAS_MEM[5]
	S += (c_pbc_s00*MAS[3])-1 < c_pbc00_mem1*MAS_MEM[7]
	S += c_pbc00_mem1 <= c_pbc00

	c_pbc01 = S.Task('c_pbc01', length=2, delay_cost=1)
	c_pbc01 += alt(MAS)
	c_pbc01_in = S.Task('c_pbc01_in', length=1, delay_cost=1)
	c_pbc01_in += alt(MAS_in)
	S += c_pbc01_in*MAS_in[0]<=c_pbc01*MAS[0]

	S += c_pbc01_in*MAS_in[1]<=c_pbc01*MAS[1]

	S += c_pbc01_in*MAS_in[2]<=c_pbc01*MAS[2]

	S += c_pbc01_in*MAS_in[3]<=c_pbc01*MAS[3]

	c_pbc01_mem0 = S.Task('c_pbc01_mem0', length=1, delay_cost=1)
	c_pbc01_mem0 += MAS_MEM[0]
	S += 104 < c_pbc01_mem0
	S += c_pbc01_mem0 <= c_pbc01

	c_pbc01_mem1 = S.Task('c_pbc01_mem1', length=1, delay_cost=1)
	c_pbc01_mem1 += alt(MAS_MEM)
	S += (c_pbc_s01*MAS[0])-1 < c_pbc01_mem1*MAS_MEM[1]
	S += (c_pbc_s01*MAS[1])-1 < c_pbc01_mem1*MAS_MEM[3]
	S += (c_pbc_s01*MAS[2])-1 < c_pbc01_mem1*MAS_MEM[5]
	S += (c_pbc_s01*MAS[3])-1 < c_pbc01_mem1*MAS_MEM[7]
	S += c_pbc01_mem1 <= c_pbc01

	c_pbc11 = S.Task('c_pbc11', length=2, delay_cost=1)
	c_pbc11 += alt(MAS)
	c_pbc11_in = S.Task('c_pbc11_in', length=1, delay_cost=1)
	c_pbc11_in += alt(MAS_in)
	S += c_pbc11_in*MAS_in[0]<=c_pbc11*MAS[0]

	S += c_pbc11_in*MAS_in[1]<=c_pbc11*MAS[1]

	S += c_pbc11_in*MAS_in[2]<=c_pbc11*MAS[2]

	S += c_pbc11_in*MAS_in[3]<=c_pbc11*MAS[3]

	c_pbc11_mem0 = S.Task('c_pbc11_mem0', length=1, delay_cost=1)
	c_pbc11_mem0 += alt(MAS_MEM)
	S += (c_pbc_t41*MAS[0])-1 < c_pbc11_mem0*MAS_MEM[0]
	S += (c_pbc_t41*MAS[1])-1 < c_pbc11_mem0*MAS_MEM[2]
	S += (c_pbc_t41*MAS[2])-1 < c_pbc11_mem0*MAS_MEM[4]
	S += (c_pbc_t41*MAS[3])-1 < c_pbc11_mem0*MAS_MEM[6]
	S += c_pbc11_mem0 <= c_pbc11

	c_pbc11_mem1 = S.Task('c_pbc11_mem1', length=1, delay_cost=1)
	c_pbc11_mem1 += alt(MAS_MEM)
	S += (c_pbc_t51*MAS[0])-1 < c_pbc11_mem1*MAS_MEM[1]
	S += (c_pbc_t51*MAS[1])-1 < c_pbc11_mem1*MAS_MEM[3]
	S += (c_pbc_t51*MAS[2])-1 < c_pbc11_mem1*MAS_MEM[5]
	S += (c_pbc_t51*MAS[3])-1 < c_pbc11_mem1*MAS_MEM[7]
	S += c_pbc11_mem1 <= c_pbc11

	c_pcb11 = S.Task('c_pcb11', length=2, delay_cost=1)
	c_pcb11 += alt(MAS)
	c_pcb11_in = S.Task('c_pcb11_in', length=1, delay_cost=1)
	c_pcb11_in += alt(MAS_in)
	S += c_pcb11_in*MAS_in[0]<=c_pcb11*MAS[0]

	S += c_pcb11_in*MAS_in[1]<=c_pcb11*MAS[1]

	S += c_pcb11_in*MAS_in[2]<=c_pcb11*MAS[2]

	S += c_pcb11_in*MAS_in[3]<=c_pcb11*MAS[3]

	c_pcb11_mem0 = S.Task('c_pcb11_mem0', length=1, delay_cost=1)
	c_pcb11_mem0 += alt(MAS_MEM)
	S += (c_pcb_t41*MAS[0])-1 < c_pcb11_mem0*MAS_MEM[0]
	S += (c_pcb_t41*MAS[1])-1 < c_pcb11_mem0*MAS_MEM[2]
	S += (c_pcb_t41*MAS[2])-1 < c_pcb11_mem0*MAS_MEM[4]
	S += (c_pcb_t41*MAS[3])-1 < c_pcb11_mem0*MAS_MEM[6]
	S += c_pcb11_mem0 <= c_pcb11

	c_pcb11_mem1 = S.Task('c_pcb11_mem1', length=1, delay_cost=1)
	c_pcb11_mem1 += alt(MAS_MEM)
	S += (c_pcb_t51*MAS[0])-1 < c_pcb11_mem1*MAS_MEM[1]
	S += (c_pcb_t51*MAS[1])-1 < c_pcb11_mem1*MAS_MEM[3]
	S += (c_pcb_t51*MAS[2])-1 < c_pcb11_mem1*MAS_MEM[5]
	S += (c_pcb_t51*MAS[3])-1 < c_pcb11_mem1*MAS_MEM[7]
	S += c_pcb11_mem1 <= c_pcb11

	c_pbccb10 = S.Task('c_pbccb10', length=2, delay_cost=1)
	c_pbccb10 += alt(MAS)
	c_pbccb10_in = S.Task('c_pbccb10_in', length=1, delay_cost=1)
	c_pbccb10_in += alt(MAS_in)
	S += c_pbccb10_in*MAS_in[0]<=c_pbccb10*MAS[0]

	S += c_pbccb10_in*MAS_in[1]<=c_pbccb10*MAS[1]

	S += c_pbccb10_in*MAS_in[2]<=c_pbccb10*MAS[2]

	S += c_pbccb10_in*MAS_in[3]<=c_pbccb10*MAS[3]

	c_pbccb10_mem0 = S.Task('c_pbccb10_mem0', length=1, delay_cost=1)
	c_pbccb10_mem0 += alt(MAS_MEM)
	S += (c_pbc10*MAS[0])-1 < c_pbccb10_mem0*MAS_MEM[0]
	S += (c_pbc10*MAS[1])-1 < c_pbccb10_mem0*MAS_MEM[2]
	S += (c_pbc10*MAS[2])-1 < c_pbccb10_mem0*MAS_MEM[4]
	S += (c_pbc10*MAS[3])-1 < c_pbccb10_mem0*MAS_MEM[6]
	S += c_pbccb10_mem0 <= c_pbccb10

	c_pbccb10_mem1 = S.Task('c_pbccb10_mem1', length=1, delay_cost=1)
	c_pbccb10_mem1 += alt(MAS_MEM)
	S += (c_pcb10*MAS[0])-1 < c_pbccb10_mem1*MAS_MEM[1]
	S += (c_pcb10*MAS[1])-1 < c_pbccb10_mem1*MAS_MEM[3]
	S += (c_pcb10*MAS[2])-1 < c_pbccb10_mem1*MAS_MEM[5]
	S += (c_pcb10*MAS[3])-1 < c_pbccb10_mem1*MAS_MEM[7]
	S += c_pbccb10_mem1 <= c_pbccb10

	c_paa11 = S.Task('c_paa11', length=2, delay_cost=1)
	c_paa11 += alt(MAS)
	c_paa11_in = S.Task('c_paa11_in', length=1, delay_cost=1)
	c_paa11_in += alt(MAS_in)
	S += c_paa11_in*MAS_in[0]<=c_paa11*MAS[0]

	S += c_paa11_in*MAS_in[1]<=c_paa11*MAS[1]

	S += c_paa11_in*MAS_in[2]<=c_paa11*MAS[2]

	S += c_paa11_in*MAS_in[3]<=c_paa11*MAS[3]

	c_paa11_mem0 = S.Task('c_paa11_mem0', length=1, delay_cost=1)
	c_paa11_mem0 += alt(MAS_MEM)
	S += (c_paa_t41*MAS[0])-1 < c_paa11_mem0*MAS_MEM[0]
	S += (c_paa_t41*MAS[1])-1 < c_paa11_mem0*MAS_MEM[2]
	S += (c_paa_t41*MAS[2])-1 < c_paa11_mem0*MAS_MEM[4]
	S += (c_paa_t41*MAS[3])-1 < c_paa11_mem0*MAS_MEM[6]
	S += c_paa11_mem0 <= c_paa11

	c_paa11_mem1 = S.Task('c_paa11_mem1', length=1, delay_cost=1)
	c_paa11_mem1 += alt(MAS_MEM)
	S += (c_paa_t51*MAS[0])-1 < c_paa11_mem1*MAS_MEM[1]
	S += (c_paa_t51*MAS[1])-1 < c_paa11_mem1*MAS_MEM[3]
	S += (c_paa_t51*MAS[2])-1 < c_paa11_mem1*MAS_MEM[5]
	S += (c_paa_t51*MAS[3])-1 < c_paa11_mem1*MAS_MEM[7]
	S += c_paa11_mem1 <= c_paa11

	c_pbccb00 = S.Task('c_pbccb00', length=2, delay_cost=1)
	c_pbccb00 += alt(MAS)
	c_pbccb00_in = S.Task('c_pbccb00_in', length=1, delay_cost=1)
	c_pbccb00_in += alt(MAS_in)
	S += c_pbccb00_in*MAS_in[0]<=c_pbccb00*MAS[0]

	S += c_pbccb00_in*MAS_in[1]<=c_pbccb00*MAS[1]

	S += c_pbccb00_in*MAS_in[2]<=c_pbccb00*MAS[2]

	S += c_pbccb00_in*MAS_in[3]<=c_pbccb00*MAS[3]

	c_pbccb00_mem0 = S.Task('c_pbccb00_mem0', length=1, delay_cost=1)
	c_pbccb00_mem0 += alt(MAS_MEM)
	S += (c_pbc00*MAS[0])-1 < c_pbccb00_mem0*MAS_MEM[0]
	S += (c_pbc00*MAS[1])-1 < c_pbccb00_mem0*MAS_MEM[2]
	S += (c_pbc00*MAS[2])-1 < c_pbccb00_mem0*MAS_MEM[4]
	S += (c_pbc00*MAS[3])-1 < c_pbccb00_mem0*MAS_MEM[6]
	S += c_pbccb00_mem0 <= c_pbccb00

	c_pbccb00_mem1 = S.Task('c_pbccb00_mem1', length=1, delay_cost=1)
	c_pbccb00_mem1 += alt(MAS_MEM)
	S += (c_pcb00*MAS[0])-1 < c_pbccb00_mem1*MAS_MEM[1]
	S += (c_pcb00*MAS[1])-1 < c_pbccb00_mem1*MAS_MEM[3]
	S += (c_pcb00*MAS[2])-1 < c_pbccb00_mem1*MAS_MEM[5]
	S += (c_pcb00*MAS[3])-1 < c_pbccb00_mem1*MAS_MEM[7]
	S += c_pbccb00_mem1 <= c_pbccb00

	c_pbccb01 = S.Task('c_pbccb01', length=2, delay_cost=1)
	c_pbccb01 += alt(MAS)
	c_pbccb01_in = S.Task('c_pbccb01_in', length=1, delay_cost=1)
	c_pbccb01_in += alt(MAS_in)
	S += c_pbccb01_in*MAS_in[0]<=c_pbccb01*MAS[0]

	S += c_pbccb01_in*MAS_in[1]<=c_pbccb01*MAS[1]

	S += c_pbccb01_in*MAS_in[2]<=c_pbccb01*MAS[2]

	S += c_pbccb01_in*MAS_in[3]<=c_pbccb01*MAS[3]

	c_pbccb01_mem0 = S.Task('c_pbccb01_mem0', length=1, delay_cost=1)
	c_pbccb01_mem0 += alt(MAS_MEM)
	S += (c_pbc01*MAS[0])-1 < c_pbccb01_mem0*MAS_MEM[0]
	S += (c_pbc01*MAS[1])-1 < c_pbccb01_mem0*MAS_MEM[2]
	S += (c_pbc01*MAS[2])-1 < c_pbccb01_mem0*MAS_MEM[4]
	S += (c_pbc01*MAS[3])-1 < c_pbccb01_mem0*MAS_MEM[6]
	S += c_pbccb01_mem0 <= c_pbccb01

	c_pbccb01_mem1 = S.Task('c_pbccb01_mem1', length=1, delay_cost=1)
	c_pbccb01_mem1 += alt(MAS_MEM)
	S += (c_pcb01*MAS[0])-1 < c_pbccb01_mem1*MAS_MEM[1]
	S += (c_pcb01*MAS[1])-1 < c_pbccb01_mem1*MAS_MEM[3]
	S += (c_pcb01*MAS[2])-1 < c_pbccb01_mem1*MAS_MEM[5]
	S += (c_pcb01*MAS[3])-1 < c_pbccb01_mem1*MAS_MEM[7]
	S += c_pbccb01_mem1 <= c_pbccb01

	c_pbccb11 = S.Task('c_pbccb11', length=2, delay_cost=1)
	c_pbccb11 += alt(MAS)
	c_pbccb11_in = S.Task('c_pbccb11_in', length=1, delay_cost=1)
	c_pbccb11_in += alt(MAS_in)
	S += c_pbccb11_in*MAS_in[0]<=c_pbccb11*MAS[0]

	S += c_pbccb11_in*MAS_in[1]<=c_pbccb11*MAS[1]

	S += c_pbccb11_in*MAS_in[2]<=c_pbccb11*MAS[2]

	S += c_pbccb11_in*MAS_in[3]<=c_pbccb11*MAS[3]

	c_pbccb11_mem0 = S.Task('c_pbccb11_mem0', length=1, delay_cost=1)
	c_pbccb11_mem0 += alt(MAS_MEM)
	S += (c_pbc11*MAS[0])-1 < c_pbccb11_mem0*MAS_MEM[0]
	S += (c_pbc11*MAS[1])-1 < c_pbccb11_mem0*MAS_MEM[2]
	S += (c_pbc11*MAS[2])-1 < c_pbccb11_mem0*MAS_MEM[4]
	S += (c_pbc11*MAS[3])-1 < c_pbccb11_mem0*MAS_MEM[6]
	S += c_pbccb11_mem0 <= c_pbccb11

	c_pbccb11_mem1 = S.Task('c_pbccb11_mem1', length=1, delay_cost=1)
	c_pbccb11_mem1 += alt(MAS_MEM)
	S += (c_pcb11*MAS[0])-1 < c_pbccb11_mem1*MAS_MEM[1]
	S += (c_pcb11*MAS[1])-1 < c_pbccb11_mem1*MAS_MEM[3]
	S += (c_pcb11*MAS[2])-1 < c_pbccb11_mem1*MAS_MEM[5]
	S += (c_pcb11*MAS[3])-1 < c_pbccb11_mem1*MAS_MEM[7]
	S += c_pbccb11_mem1 <= c_pbccb11

	c_pxi_y1_0 = S.Task('c_pxi_y1_0', length=2, delay_cost=1)
	c_pxi_y1_0 += alt(MAS)
	c_pxi_y1_0_in = S.Task('c_pxi_y1_0_in', length=1, delay_cost=1)
	c_pxi_y1_0_in += alt(MAS_in)
	S += c_pxi_y1_0_in*MAS_in[0]<=c_pxi_y1_0*MAS[0]

	S += c_pxi_y1_0_in*MAS_in[1]<=c_pxi_y1_0*MAS[1]

	S += c_pxi_y1_0_in*MAS_in[2]<=c_pxi_y1_0*MAS[2]

	S += c_pxi_y1_0_in*MAS_in[3]<=c_pxi_y1_0*MAS[3]

	c_pxi_y1_0_mem0 = S.Task('c_pxi_y1_0_mem0', length=1, delay_cost=1)
	c_pxi_y1_0_mem0 += alt(MAS_MEM)
	S += (c_pbccb10*MAS[0])-1 < c_pxi_y1_0_mem0*MAS_MEM[0]
	S += (c_pbccb10*MAS[1])-1 < c_pxi_y1_0_mem0*MAS_MEM[2]
	S += (c_pbccb10*MAS[2])-1 < c_pxi_y1_0_mem0*MAS_MEM[4]
	S += (c_pbccb10*MAS[3])-1 < c_pxi_y1_0_mem0*MAS_MEM[6]
	S += c_pxi_y1_0_mem0 <= c_pxi_y1_0

	c_pxi_y1_0_mem1 = S.Task('c_pxi_y1_0_mem1', length=1, delay_cost=1)
	c_pxi_y1_0_mem1 += alt(MAS_MEM)
	S += (c_pbccb11*MAS[0])-1 < c_pxi_y1_0_mem1*MAS_MEM[1]
	S += (c_pbccb11*MAS[1])-1 < c_pxi_y1_0_mem1*MAS_MEM[3]
	S += (c_pbccb11*MAS[2])-1 < c_pxi_y1_0_mem1*MAS_MEM[5]
	S += (c_pbccb11*MAS[3])-1 < c_pxi_y1_0_mem1*MAS_MEM[7]
	S += c_pxi_y1_0_mem1 <= c_pxi_y1_0

	c_pxi_y1_1 = S.Task('c_pxi_y1_1', length=2, delay_cost=1)
	c_pxi_y1_1 += alt(MAS)
	c_pxi_y1_1_in = S.Task('c_pxi_y1_1_in', length=1, delay_cost=1)
	c_pxi_y1_1_in += alt(MAS_in)
	S += c_pxi_y1_1_in*MAS_in[0]<=c_pxi_y1_1*MAS[0]

	S += c_pxi_y1_1_in*MAS_in[1]<=c_pxi_y1_1*MAS[1]

	S += c_pxi_y1_1_in*MAS_in[2]<=c_pxi_y1_1*MAS[2]

	S += c_pxi_y1_1_in*MAS_in[3]<=c_pxi_y1_1*MAS[3]

	c_pxi_y1_1_mem0 = S.Task('c_pxi_y1_1_mem0', length=1, delay_cost=1)
	c_pxi_y1_1_mem0 += alt(MAS_MEM)
	S += (c_pbccb11*MAS[0])-1 < c_pxi_y1_1_mem0*MAS_MEM[0]
	S += (c_pbccb11*MAS[1])-1 < c_pxi_y1_1_mem0*MAS_MEM[2]
	S += (c_pbccb11*MAS[2])-1 < c_pxi_y1_1_mem0*MAS_MEM[4]
	S += (c_pbccb11*MAS[3])-1 < c_pxi_y1_1_mem0*MAS_MEM[6]
	S += c_pxi_y1_1_mem0 <= c_pxi_y1_1

	c_pxi_y1_1_mem1 = S.Task('c_pxi_y1_1_mem1', length=1, delay_cost=1)
	c_pxi_y1_1_mem1 += alt(MAS_MEM)
	S += (c_pbccb10*MAS[0])-1 < c_pxi_y1_1_mem1*MAS_MEM[1]
	S += (c_pbccb10*MAS[1])-1 < c_pxi_y1_1_mem1*MAS_MEM[3]
	S += (c_pbccb10*MAS[2])-1 < c_pxi_y1_1_mem1*MAS_MEM[5]
	S += (c_pbccb10*MAS[3])-1 < c_pxi_y1_1_mem1*MAS_MEM[7]
	S += c_pxi_y1_1_mem1 <= c_pxi_y1_1

	c_q10 = S.Task('c_q10', length=2, delay_cost=1)
	c_q10 += alt(MAS)
	c_q10_in = S.Task('c_q10_in', length=1, delay_cost=1)
	c_q10_in += alt(MAS_in)
	S += c_q10_in*MAS_in[0]<=c_q10*MAS[0]

	S += c_q10_in*MAS_in[1]<=c_q10*MAS[1]

	S += c_q10_in*MAS_in[2]<=c_q10*MAS[2]

	S += c_q10_in*MAS_in[3]<=c_q10*MAS[3]

	c_q10_mem0 = S.Task('c_q10_mem0', length=1, delay_cost=1)
	c_q10_mem0 += alt(MAS_MEM)
	S += (c_pbccb00*MAS[0])-1 < c_q10_mem0*MAS_MEM[0]
	S += (c_pbccb00*MAS[1])-1 < c_q10_mem0*MAS_MEM[2]
	S += (c_pbccb00*MAS[2])-1 < c_q10_mem0*MAS_MEM[4]
	S += (c_pbccb00*MAS[3])-1 < c_q10_mem0*MAS_MEM[6]
	S += c_q10_mem0 <= c_q10

	c_q10_mem1 = S.Task('c_q10_mem1', length=1, delay_cost=1)
	c_q10_mem1 += alt(MAS_MEM)
	S += (c_paa10*MAS[0])-1 < c_q10_mem1*MAS_MEM[1]
	S += (c_paa10*MAS[1])-1 < c_q10_mem1*MAS_MEM[3]
	S += (c_paa10*MAS[2])-1 < c_q10_mem1*MAS_MEM[5]
	S += (c_paa10*MAS[3])-1 < c_q10_mem1*MAS_MEM[7]
	S += c_q10_mem1 <= c_q10

	c_q11 = S.Task('c_q11', length=2, delay_cost=1)
	c_q11 += alt(MAS)
	c_q11_in = S.Task('c_q11_in', length=1, delay_cost=1)
	c_q11_in += alt(MAS_in)
	S += c_q11_in*MAS_in[0]<=c_q11*MAS[0]

	S += c_q11_in*MAS_in[1]<=c_q11*MAS[1]

	S += c_q11_in*MAS_in[2]<=c_q11*MAS[2]

	S += c_q11_in*MAS_in[3]<=c_q11*MAS[3]

	c_q11_mem0 = S.Task('c_q11_mem0', length=1, delay_cost=1)
	c_q11_mem0 += alt(MAS_MEM)
	S += (c_pbccb01*MAS[0])-1 < c_q11_mem0*MAS_MEM[0]
	S += (c_pbccb01*MAS[1])-1 < c_q11_mem0*MAS_MEM[2]
	S += (c_pbccb01*MAS[2])-1 < c_q11_mem0*MAS_MEM[4]
	S += (c_pbccb01*MAS[3])-1 < c_q11_mem0*MAS_MEM[6]
	S += c_q11_mem0 <= c_q11

	c_q11_mem1 = S.Task('c_q11_mem1', length=1, delay_cost=1)
	c_q11_mem1 += alt(MAS_MEM)
	S += (c_paa11*MAS[0])-1 < c_q11_mem1*MAS_MEM[1]
	S += (c_paa11*MAS[1])-1 < c_q11_mem1*MAS_MEM[3]
	S += (c_paa11*MAS[2])-1 < c_q11_mem1*MAS_MEM[5]
	S += (c_paa11*MAS[3])-1 < c_q11_mem1*MAS_MEM[7]
	S += c_q11_mem1 <= c_q11

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM1_stage2MAS4/FP12_INV_BEFORE_FPINV/schedule8.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

