from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 203
	S = Scenario("schedule5", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_ab_t0_t3_in = S.Task('c_ab_t0_t3_in', length=1, delay_cost=1)
	S += c_ab_t0_t3_in >= 0
	c_ab_t0_t3_in += MAS_in[1]

	c_ab_t0_t3_mem0 = S.Task('c_ab_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem0 >= 0
	c_ab_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t3_mem1 = S.Task('c_ab_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t3_mem1 >= 0
	c_ab_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1_in = S.Task('c_ab_t0_t1_in', length=1, delay_cost=1)
	S += c_ab_t0_t1_in >= 1
	c_ab_t0_t1_in += MM_in[0]

	c_ab_t0_t1_mem0 = S.Task('c_ab_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem0 >= 1
	c_ab_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t1_mem1 = S.Task('c_ab_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t1_mem1 >= 1
	c_ab_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t3 = S.Task('c_ab_t0_t3', length=2, delay_cost=1)
	S += c_ab_t0_t3 >= 1
	c_ab_t0_t3 += MAS[1]

	c_ab_t0_t0_in = S.Task('c_ab_t0_t0_in', length=1, delay_cost=1)
	S += c_ab_t0_t0_in >= 2
	c_ab_t0_t0_in += MM_in[0]

	c_ab_t0_t0_mem0 = S.Task('c_ab_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem0 >= 2
	c_ab_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t0_mem1 = S.Task('c_ab_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t0_mem1 >= 2
	c_ab_t0_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t1 = S.Task('c_ab_t0_t1', length=11, delay_cost=1)
	S += c_ab_t0_t1 >= 2
	c_ab_t0_t1 += MM[0]

	c_ab_t0_t0 = S.Task('c_ab_t0_t0', length=11, delay_cost=1)
	S += c_ab_t0_t0 >= 3
	c_ab_t0_t0 += MM[0]

	c_cc_a1_1_in = S.Task('c_cc_a1_1_in', length=1, delay_cost=1)
	S += c_cc_a1_1_in >= 3
	c_cc_a1_1_in += MAS_in[1]

	c_cc_a1_1_mem0 = S.Task('c_cc_a1_1_mem0', length=1, delay_cost=1)
	S += c_cc_a1_1_mem0 >= 3
	c_cc_a1_1_mem0 += MAIN_MEM_r[0]

	c_cc_a1_1_mem1 = S.Task('c_cc_a1_1_mem1', length=1, delay_cost=1)
	S += c_cc_a1_1_mem1 >= 3
	c_cc_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_a1_1 = S.Task('c_cc_a1_1', length=2, delay_cost=1)
	S += c_cc_a1_1 >= 4
	c_cc_a1_1 += MAS[1]

	c_cc_t11_in = S.Task('c_cc_t11_in', length=1, delay_cost=1)
	S += c_cc_t11_in >= 4
	c_cc_t11_in += MAS_in[4]

	c_cc_t11_mem0 = S.Task('c_cc_t11_mem0', length=1, delay_cost=1)
	S += c_cc_t11_mem0 >= 4
	c_cc_t11_mem0 += MAIN_MEM_r[0]

	c_cc_t11_mem1 = S.Task('c_cc_t11_mem1', length=1, delay_cost=1)
	S += c_cc_t11_mem1 >= 4
	c_cc_t11_mem1 += MAIN_MEM_r[1]

	c_cc_t11 = S.Task('c_cc_t11', length=2, delay_cost=1)
	S += c_cc_t11 >= 5
	c_cc_t11 += MAS[4]

	c_cc_t3_t1_in = S.Task('c_cc_t3_t1_in', length=1, delay_cost=1)
	S += c_cc_t3_t1_in >= 5
	c_cc_t3_t1_in += MM_in[1]

	c_cc_t3_t1_mem0 = S.Task('c_cc_t3_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem0 >= 5
	c_cc_t3_t1_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t1_mem1 = S.Task('c_cc_t3_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t1_mem1 >= 5
	c_cc_t3_t1_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t1_in = S.Task('c_aa_t3_t1_in', length=1, delay_cost=1)
	S += c_aa_t3_t1_in >= 6
	c_aa_t3_t1_in += MM_in[0]

	c_aa_t3_t1_mem0 = S.Task('c_aa_t3_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem0 >= 6
	c_aa_t3_t1_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t1_mem1 = S.Task('c_aa_t3_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t1_mem1 >= 6
	c_aa_t3_t1_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t1 = S.Task('c_cc_t3_t1', length=11, delay_cost=1)
	S += c_cc_t3_t1 >= 6
	c_cc_t3_t1 += MM[1]

	c_aa_t3_t1 = S.Task('c_aa_t3_t1', length=11, delay_cost=1)
	S += c_aa_t3_t1 >= 7
	c_aa_t3_t1 += MM[0]

	c_ab_t1_t1_in = S.Task('c_ab_t1_t1_in', length=1, delay_cost=1)
	S += c_ab_t1_t1_in >= 7
	c_ab_t1_t1_in += MM_in[1]

	c_ab_t1_t1_mem0 = S.Task('c_ab_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem0 >= 7
	c_ab_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t1_mem1 = S.Task('c_ab_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t1_mem1 >= 7
	c_ab_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t1 = S.Task('c_ab_t1_t1', length=11, delay_cost=1)
	S += c_ab_t1_t1 >= 8
	c_ab_t1_t1 += MM[1]

	c_bb_t3_t0_in = S.Task('c_bb_t3_t0_in', length=1, delay_cost=1)
	S += c_bb_t3_t0_in >= 8
	c_bb_t3_t0_in += MM_in[1]

	c_bb_t3_t0_mem0 = S.Task('c_bb_t3_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem0 >= 8
	c_bb_t3_t0_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t0_mem1 = S.Task('c_bb_t3_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t0_mem1 >= 8
	c_bb_t3_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2_in = S.Task('c_ab_t0_t2_in', length=1, delay_cost=1)
	S += c_ab_t0_t2_in >= 9
	c_ab_t0_t2_in += MAS_in[2]

	c_ab_t0_t2_mem0 = S.Task('c_ab_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem0 >= 9
	c_ab_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t0_t2_mem1 = S.Task('c_ab_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t2_mem1 >= 9
	c_ab_t0_t2_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t0 = S.Task('c_bb_t3_t0', length=11, delay_cost=1)
	S += c_bb_t3_t0 >= 9
	c_bb_t3_t0 += MM[1]

	c_aa_t3_t2_in = S.Task('c_aa_t3_t2_in', length=1, delay_cost=1)
	S += c_aa_t3_t2_in >= 10
	c_aa_t3_t2_in += MAS_in[5]

	c_aa_t3_t2_mem0 = S.Task('c_aa_t3_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem0 >= 10
	c_aa_t3_t2_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t2_mem1 = S.Task('c_aa_t3_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t2_mem1 >= 10
	c_aa_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t2 = S.Task('c_ab_t0_t2', length=2, delay_cost=1)
	S += c_ab_t0_t2 >= 10
	c_ab_t0_t2 += MAS[2]

	c_aa_t3_t2 = S.Task('c_aa_t3_t2', length=2, delay_cost=1)
	S += c_aa_t3_t2 >= 11
	c_aa_t3_t2 += MAS[5]

	c_ab_t0_t4_in = S.Task('c_ab_t0_t4_in', length=1, delay_cost=1)
	S += c_ab_t0_t4_in >= 11
	c_ab_t0_t4_in += MM_in[0]

	c_ab_t0_t4_mem0 = S.Task('c_ab_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem0 >= 11
	c_ab_t0_t4_mem0 += MAS_MEM[4]

	c_ab_t0_t4_mem1 = S.Task('c_ab_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t4_mem1 >= 11
	c_ab_t0_t4_mem1 += MAS_MEM[3]

	c_cc_t3_t3_in = S.Task('c_cc_t3_t3_in', length=1, delay_cost=1)
	S += c_cc_t3_t3_in >= 11
	c_cc_t3_t3_in += MAS_in[5]

	c_cc_t3_t3_mem0 = S.Task('c_cc_t3_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem0 >= 11
	c_cc_t3_t3_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t3_mem1 = S.Task('c_cc_t3_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t3_mem1 >= 11
	c_cc_t3_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t4 = S.Task('c_ab_t0_t4', length=11, delay_cost=1)
	S += c_ab_t0_t4 >= 12
	c_ab_t0_t4 += MM[0]

	c_bb_t3_t3_in = S.Task('c_bb_t3_t3_in', length=1, delay_cost=1)
	S += c_bb_t3_t3_in >= 12
	c_bb_t3_t3_in += MAS_in[5]

	c_bb_t3_t3_mem0 = S.Task('c_bb_t3_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem0 >= 12
	c_bb_t3_t3_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t3_mem1 = S.Task('c_bb_t3_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t3_mem1 >= 12
	c_bb_t3_t3_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t3 = S.Task('c_cc_t3_t3', length=2, delay_cost=1)
	S += c_cc_t3_t3 >= 12
	c_cc_t3_t3 += MAS[5]

	c_ab_t00_in = S.Task('c_ab_t00_in', length=1, delay_cost=1)
	S += c_ab_t00_in >= 13
	c_ab_t00_in += MAS_in[4]

	c_ab_t00_mem0 = S.Task('c_ab_t00_mem0', length=1, delay_cost=1)
	S += c_ab_t00_mem0 >= 13
	c_ab_t00_mem0 += MM_MEM[0]

	c_ab_t00_mem1 = S.Task('c_ab_t00_mem1', length=1, delay_cost=1)
	S += c_ab_t00_mem1 >= 13
	c_ab_t00_mem1 += MM_MEM[1]

	c_bb_t3_t3 = S.Task('c_bb_t3_t3', length=2, delay_cost=1)
	S += c_bb_t3_t3 >= 13
	c_bb_t3_t3 += MAS[5]

	c_cc_t3_t2_in = S.Task('c_cc_t3_t2_in', length=1, delay_cost=1)
	S += c_cc_t3_t2_in >= 13
	c_cc_t3_t2_in += MAS_in[5]

	c_cc_t3_t2_mem0 = S.Task('c_cc_t3_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem0 >= 13
	c_cc_t3_t2_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t2_mem1 = S.Task('c_cc_t3_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t2_mem1 >= 13
	c_cc_t3_t2_mem1 += MAIN_MEM_r[1]

	c_ab_t00 = S.Task('c_ab_t00', length=2, delay_cost=1)
	S += c_ab_t00 >= 14
	c_ab_t00 += MAS[4]

	c_ab_t0_t5_in = S.Task('c_ab_t0_t5_in', length=1, delay_cost=1)
	S += c_ab_t0_t5_in >= 14
	c_ab_t0_t5_in += MAS_in[3]

	c_ab_t0_t5_mem0 = S.Task('c_ab_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem0 >= 14
	c_ab_t0_t5_mem0 += MM_MEM[0]

	c_ab_t0_t5_mem1 = S.Task('c_ab_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t0_t5_mem1 >= 14
	c_ab_t0_t5_mem1 += MM_MEM[1]

	c_cc_t10_in = S.Task('c_cc_t10_in', length=1, delay_cost=1)
	S += c_cc_t10_in >= 14
	c_cc_t10_in += MAS_in[4]

	c_cc_t10_mem0 = S.Task('c_cc_t10_mem0', length=1, delay_cost=1)
	S += c_cc_t10_mem0 >= 14
	c_cc_t10_mem0 += MAIN_MEM_r[0]

	c_cc_t10_mem1 = S.Task('c_cc_t10_mem1', length=1, delay_cost=1)
	S += c_cc_t10_mem1 >= 14
	c_cc_t10_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t2 = S.Task('c_cc_t3_t2', length=2, delay_cost=1)
	S += c_cc_t3_t2 >= 14
	c_cc_t3_t2 += MAS[5]

	c_aa_a1_0_in = S.Task('c_aa_a1_0_in', length=1, delay_cost=1)
	S += c_aa_a1_0_in >= 15
	c_aa_a1_0_in += MAS_in[5]

	c_aa_a1_0_mem0 = S.Task('c_aa_a1_0_mem0', length=1, delay_cost=1)
	S += c_aa_a1_0_mem0 >= 15
	c_aa_a1_0_mem0 += MAIN_MEM_r[0]

	c_aa_a1_0_mem1 = S.Task('c_aa_a1_0_mem1', length=1, delay_cost=1)
	S += c_aa_a1_0_mem1 >= 15
	c_aa_a1_0_mem1 += MAIN_MEM_r[1]

	c_ab_t0_t5 = S.Task('c_ab_t0_t5', length=2, delay_cost=1)
	S += c_ab_t0_t5 >= 15
	c_ab_t0_t5 += MAS[3]

	c_cc_t10 = S.Task('c_cc_t10', length=2, delay_cost=1)
	S += c_cc_t10 >= 15
	c_cc_t10 += MAS[4]

	c_cc_t3_t4_in = S.Task('c_cc_t3_t4_in', length=1, delay_cost=1)
	S += c_cc_t3_t4_in >= 15
	c_cc_t3_t4_in += MM_in[1]

	c_cc_t3_t4_mem0 = S.Task('c_cc_t3_t4_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem0 >= 15
	c_cc_t3_t4_mem0 += MAS_MEM[10]

	c_cc_t3_t4_mem1 = S.Task('c_cc_t3_t4_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t4_mem1 >= 15
	c_cc_t3_t4_mem1 += MAS_MEM[11]

	c_aa_a1_0 = S.Task('c_aa_a1_0', length=2, delay_cost=1)
	S += c_aa_a1_0 >= 16
	c_aa_a1_0 += MAS[5]

	c_cc_t2_t3_in = S.Task('c_cc_t2_t3_in', length=1, delay_cost=1)
	S += c_cc_t2_t3_in >= 16
	c_cc_t2_t3_in += MAS_in[0]

	c_cc_t2_t3_mem0 = S.Task('c_cc_t2_t3_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem0 >= 16
	c_cc_t2_t3_mem0 += MAS_MEM[8]

	c_cc_t2_t3_mem1 = S.Task('c_cc_t2_t3_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t3_mem1 >= 16
	c_cc_t2_t3_mem1 += MAS_MEM[9]

	c_cc_t3_t0_in = S.Task('c_cc_t3_t0_in', length=1, delay_cost=1)
	S += c_cc_t3_t0_in >= 16
	c_cc_t3_t0_in += MM_in[0]

	c_cc_t3_t0_mem0 = S.Task('c_cc_t3_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem0 >= 16
	c_cc_t3_t0_mem0 += MAIN_MEM_r[0]

	c_cc_t3_t0_mem1 = S.Task('c_cc_t3_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t0_mem1 >= 16
	c_cc_t3_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t3_t4 = S.Task('c_cc_t3_t4', length=11, delay_cost=1)
	S += c_cc_t3_t4 >= 16
	c_cc_t3_t4 += MM[1]

	c_bb_a1_1_in = S.Task('c_bb_a1_1_in', length=1, delay_cost=1)
	S += c_bb_a1_1_in >= 17
	c_bb_a1_1_in += MAS_in[5]

	c_bb_a1_1_mem0 = S.Task('c_bb_a1_1_mem0', length=1, delay_cost=1)
	S += c_bb_a1_1_mem0 >= 17
	c_bb_a1_1_mem0 += MAIN_MEM_r[0]

	c_bb_a1_1_mem1 = S.Task('c_bb_a1_1_mem1', length=1, delay_cost=1)
	S += c_bb_a1_1_mem1 >= 17
	c_bb_a1_1_mem1 += MAIN_MEM_r[1]

	c_cc_t2_t3 = S.Task('c_cc_t2_t3', length=2, delay_cost=1)
	S += c_cc_t2_t3 >= 17
	c_cc_t2_t3 += MAS[0]

	c_cc_t3_t0 = S.Task('c_cc_t3_t0', length=11, delay_cost=1)
	S += c_cc_t3_t0 >= 17
	c_cc_t3_t0 += MM[0]

	c_bb_a1_1 = S.Task('c_bb_a1_1', length=2, delay_cost=1)
	S += c_bb_a1_1 >= 18
	c_bb_a1_1 += MAS[5]

	c_bb_t11_in = S.Task('c_bb_t11_in', length=1, delay_cost=1)
	S += c_bb_t11_in >= 18
	c_bb_t11_in += MAS_in[4]

	c_bb_t11_mem0 = S.Task('c_bb_t11_mem0', length=1, delay_cost=1)
	S += c_bb_t11_mem0 >= 18
	c_bb_t11_mem0 += MAIN_MEM_r[0]

	c_bb_t11_mem1 = S.Task('c_bb_t11_mem1', length=1, delay_cost=1)
	S += c_bb_t11_mem1 >= 18
	c_bb_t11_mem1 += MAIN_MEM_r[1]

	c_aa_a1_1_in = S.Task('c_aa_a1_1_in', length=1, delay_cost=1)
	S += c_aa_a1_1_in >= 19
	c_aa_a1_1_in += MAS_in[0]

	c_aa_a1_1_mem0 = S.Task('c_aa_a1_1_mem0', length=1, delay_cost=1)
	S += c_aa_a1_1_mem0 >= 19
	c_aa_a1_1_mem0 += MAIN_MEM_r[0]

	c_aa_a1_1_mem1 = S.Task('c_aa_a1_1_mem1', length=1, delay_cost=1)
	S += c_aa_a1_1_mem1 >= 19
	c_aa_a1_1_mem1 += MAIN_MEM_r[1]

	c_bb_t11 = S.Task('c_bb_t11', length=2, delay_cost=1)
	S += c_bb_t11 >= 19
	c_bb_t11 += MAS[4]

	c_aa_a1_1 = S.Task('c_aa_a1_1', length=2, delay_cost=1)
	S += c_aa_a1_1 >= 20
	c_aa_a1_1 += MAS[0]

	c_aa_t3_t0_in = S.Task('c_aa_t3_t0_in', length=1, delay_cost=1)
	S += c_aa_t3_t0_in >= 20
	c_aa_t3_t0_in += MM_in[1]

	c_aa_t3_t0_mem0 = S.Task('c_aa_t3_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem0 >= 20
	c_aa_t3_t0_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t0_mem1 = S.Task('c_aa_t3_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t0_mem1 >= 20
	c_aa_t3_t0_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t0 = S.Task('c_aa_t3_t0', length=11, delay_cost=1)
	S += c_aa_t3_t0 >= 21
	c_aa_t3_t0 += MM[1]

	c_bb_t3_t1_in = S.Task('c_bb_t3_t1_in', length=1, delay_cost=1)
	S += c_bb_t3_t1_in >= 21
	c_bb_t3_t1_in += MM_in[1]

	c_bb_t3_t1_mem0 = S.Task('c_bb_t3_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem0 >= 21
	c_bb_t3_t1_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t1_mem1 = S.Task('c_bb_t3_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t1_mem1 >= 21
	c_bb_t3_t1_mem1 += MAIN_MEM_r[1]

	c_ab_t01_in = S.Task('c_ab_t01_in', length=1, delay_cost=1)
	S += c_ab_t01_in >= 22
	c_ab_t01_in += MAS_in[2]

	c_ab_t01_mem0 = S.Task('c_ab_t01_mem0', length=1, delay_cost=1)
	S += c_ab_t01_mem0 >= 22
	c_ab_t01_mem0 += MM_MEM[0]

	c_ab_t01_mem1 = S.Task('c_ab_t01_mem1', length=1, delay_cost=1)
	S += c_ab_t01_mem1 >= 22
	c_ab_t01_mem1 += MAS_MEM[7]

	c_bb_t10_in = S.Task('c_bb_t10_in', length=1, delay_cost=1)
	S += c_bb_t10_in >= 22
	c_bb_t10_in += MAS_in[5]

	c_bb_t10_mem0 = S.Task('c_bb_t10_mem0', length=1, delay_cost=1)
	S += c_bb_t10_mem0 >= 22
	c_bb_t10_mem0 += MAIN_MEM_r[0]

	c_bb_t10_mem1 = S.Task('c_bb_t10_mem1', length=1, delay_cost=1)
	S += c_bb_t10_mem1 >= 22
	c_bb_t10_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t1 = S.Task('c_bb_t3_t1', length=11, delay_cost=1)
	S += c_bb_t3_t1 >= 22
	c_bb_t3_t1 += MM[1]

	c_ab_t01 = S.Task('c_ab_t01', length=2, delay_cost=1)
	S += c_ab_t01 >= 23
	c_ab_t01 += MAS[2]

	c_bb_t10 = S.Task('c_bb_t10', length=2, delay_cost=1)
	S += c_bb_t10 >= 23
	c_bb_t10 += MAS[5]

	c_cc_a1_0_in = S.Task('c_cc_a1_0_in', length=1, delay_cost=1)
	S += c_cc_a1_0_in >= 23
	c_cc_a1_0_in += MAS_in[4]

	c_cc_a1_0_mem0 = S.Task('c_cc_a1_0_mem0', length=1, delay_cost=1)
	S += c_cc_a1_0_mem0 >= 23
	c_cc_a1_0_mem0 += MAIN_MEM_r[0]

	c_cc_a1_0_mem1 = S.Task('c_cc_a1_0_mem1', length=1, delay_cost=1)
	S += c_cc_a1_0_mem1 >= 23
	c_cc_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t3_in = S.Task('c_bb_t2_t3_in', length=1, delay_cost=1)
	S += c_bb_t2_t3_in >= 24
	c_bb_t2_t3_in += MAS_in[4]

	c_bb_t2_t3_mem0 = S.Task('c_bb_t2_t3_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem0 >= 24
	c_bb_t2_t3_mem0 += MAS_MEM[10]

	c_bb_t2_t3_mem1 = S.Task('c_bb_t2_t3_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t3_mem1 >= 24
	c_bb_t2_t3_mem1 += MAS_MEM[9]

	c_bb_t3_t2_in = S.Task('c_bb_t3_t2_in', length=1, delay_cost=1)
	S += c_bb_t3_t2_in >= 24
	c_bb_t3_t2_in += MAS_in[0]

	c_bb_t3_t2_mem0 = S.Task('c_bb_t3_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem0 >= 24
	c_bb_t3_t2_mem0 += MAIN_MEM_r[0]

	c_bb_t3_t2_mem1 = S.Task('c_bb_t3_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t2_mem1 >= 24
	c_bb_t3_t2_mem1 += MAIN_MEM_r[1]

	c_cc_a1_0 = S.Task('c_cc_a1_0', length=2, delay_cost=1)
	S += c_cc_a1_0 >= 24
	c_cc_a1_0 += MAS[4]

	c_ab_t1_t0_in = S.Task('c_ab_t1_t0_in', length=1, delay_cost=1)
	S += c_ab_t1_t0_in >= 25
	c_ab_t1_t0_in += MM_in[0]

	c_ab_t1_t0_mem0 = S.Task('c_ab_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem0 >= 25
	c_ab_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t0_mem1 = S.Task('c_ab_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t0_mem1 >= 25
	c_ab_t1_t0_mem1 += MAIN_MEM_r[1]

	c_bb_t2_t3 = S.Task('c_bb_t2_t3', length=2, delay_cost=1)
	S += c_bb_t2_t3 >= 25
	c_bb_t2_t3 += MAS[4]

	c_bb_t3_t2 = S.Task('c_bb_t3_t2', length=2, delay_cost=1)
	S += c_bb_t3_t2 >= 25
	c_bb_t3_t2 += MAS[0]

	c_ab_t1_t0 = S.Task('c_ab_t1_t0', length=11, delay_cost=1)
	S += c_ab_t1_t0 >= 26
	c_ab_t1_t0 += MM[0]

	c_bb_a1_0_in = S.Task('c_bb_a1_0_in', length=1, delay_cost=1)
	S += c_bb_a1_0_in >= 26
	c_bb_a1_0_in += MAS_in[5]

	c_bb_a1_0_mem0 = S.Task('c_bb_a1_0_mem0', length=1, delay_cost=1)
	S += c_bb_a1_0_mem0 >= 26
	c_bb_a1_0_mem0 += MAIN_MEM_r[0]

	c_bb_a1_0_mem1 = S.Task('c_bb_a1_0_mem1', length=1, delay_cost=1)
	S += c_bb_a1_0_mem1 >= 26
	c_bb_a1_0_mem1 += MAIN_MEM_r[1]

	c_bb_t3_t4_in = S.Task('c_bb_t3_t4_in', length=1, delay_cost=1)
	S += c_bb_t3_t4_in >= 26
	c_bb_t3_t4_in += MM_in[1]

	c_bb_t3_t4_mem0 = S.Task('c_bb_t3_t4_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem0 >= 26
	c_bb_t3_t4_mem0 += MAS_MEM[0]

	c_bb_t3_t4_mem1 = S.Task('c_bb_t3_t4_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t4_mem1 >= 26
	c_bb_t3_t4_mem1 += MAS_MEM[11]

	c_aa_t3_t3_in = S.Task('c_aa_t3_t3_in', length=1, delay_cost=1)
	S += c_aa_t3_t3_in >= 27
	c_aa_t3_t3_in += MAS_in[5]

	c_aa_t3_t3_mem0 = S.Task('c_aa_t3_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem0 >= 27
	c_aa_t3_t3_mem0 += MAIN_MEM_r[0]

	c_aa_t3_t3_mem1 = S.Task('c_aa_t3_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t3_mem1 >= 27
	c_aa_t3_t3_mem1 += MAIN_MEM_r[1]

	c_bb_a1_0 = S.Task('c_bb_a1_0', length=2, delay_cost=1)
	S += c_bb_a1_0 >= 27
	c_bb_a1_0 += MAS[5]

	c_bb_t3_t4 = S.Task('c_bb_t3_t4', length=11, delay_cost=1)
	S += c_bb_t3_t4 >= 27
	c_bb_t3_t4 += MM[1]

	c_cc_t30_in = S.Task('c_cc_t30_in', length=1, delay_cost=1)
	S += c_cc_t30_in >= 27
	c_cc_t30_in += MAS_in[4]

	c_cc_t30_mem0 = S.Task('c_cc_t30_mem0', length=1, delay_cost=1)
	S += c_cc_t30_mem0 >= 27
	c_cc_t30_mem0 += MM_MEM[0]

	c_cc_t30_mem1 = S.Task('c_cc_t30_mem1', length=1, delay_cost=1)
	S += c_cc_t30_mem1 >= 27
	c_cc_t30_mem1 += MM_MEM[3]

	c_aa_t11_in = S.Task('c_aa_t11_in', length=1, delay_cost=1)
	S += c_aa_t11_in >= 28
	c_aa_t11_in += MAS_in[5]

	c_aa_t11_mem0 = S.Task('c_aa_t11_mem0', length=1, delay_cost=1)
	S += c_aa_t11_mem0 >= 28
	c_aa_t11_mem0 += MAIN_MEM_r[0]

	c_aa_t11_mem1 = S.Task('c_aa_t11_mem1', length=1, delay_cost=1)
	S += c_aa_t11_mem1 >= 28
	c_aa_t11_mem1 += MAIN_MEM_r[1]

	c_aa_t3_t3 = S.Task('c_aa_t3_t3', length=2, delay_cost=1)
	S += c_aa_t3_t3 >= 28
	c_aa_t3_t3 += MAS[5]

	c_cc_t30 = S.Task('c_cc_t30', length=2, delay_cost=1)
	S += c_cc_t30 >= 28
	c_cc_t30 += MAS[4]

	c_cc_t3_t5_in = S.Task('c_cc_t3_t5_in', length=1, delay_cost=1)
	S += c_cc_t3_t5_in >= 28
	c_cc_t3_t5_in += MAS_in[0]

	c_cc_t3_t5_mem0 = S.Task('c_cc_t3_t5_mem0', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem0 >= 28
	c_cc_t3_t5_mem0 += MM_MEM[0]

	c_cc_t3_t5_mem1 = S.Task('c_cc_t3_t5_mem1', length=1, delay_cost=1)
	S += c_cc_t3_t5_mem1 >= 28
	c_cc_t3_t5_mem1 += MM_MEM[3]

	c_aa_t10_in = S.Task('c_aa_t10_in', length=1, delay_cost=1)
	S += c_aa_t10_in >= 29
	c_aa_t10_in += MAS_in[5]

	c_aa_t10_mem0 = S.Task('c_aa_t10_mem0', length=1, delay_cost=1)
	S += c_aa_t10_mem0 >= 29
	c_aa_t10_mem0 += MAIN_MEM_r[0]

	c_aa_t10_mem1 = S.Task('c_aa_t10_mem1', length=1, delay_cost=1)
	S += c_aa_t10_mem1 >= 29
	c_aa_t10_mem1 += MAIN_MEM_r[1]

	c_aa_t11 = S.Task('c_aa_t11', length=2, delay_cost=1)
	S += c_aa_t11 >= 29
	c_aa_t11 += MAS[5]

	c_aa_t3_t4_in = S.Task('c_aa_t3_t4_in', length=1, delay_cost=1)
	S += c_aa_t3_t4_in >= 29
	c_aa_t3_t4_in += MM_in[0]

	c_aa_t3_t4_mem0 = S.Task('c_aa_t3_t4_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem0 >= 29
	c_aa_t3_t4_mem0 += MAS_MEM[10]

	c_aa_t3_t4_mem1 = S.Task('c_aa_t3_t4_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t4_mem1 >= 29
	c_aa_t3_t4_mem1 += MAS_MEM[11]

	c_cc10_in = S.Task('c_cc10_in', length=1, delay_cost=1)
	S += c_cc10_in >= 29
	c_cc10_in += MAS_in[3]

	c_cc10_mem0 = S.Task('c_cc10_mem0', length=1, delay_cost=1)
	S += c_cc10_mem0 >= 29
	c_cc10_mem0 += MAS_MEM[8]

	c_cc10_mem1 = S.Task('c_cc10_mem1', length=1, delay_cost=1)
	S += c_cc10_mem1 >= 29
	c_cc10_mem1 += MAS_MEM[9]

	c_cc_t3_t5 = S.Task('c_cc_t3_t5', length=2, delay_cost=1)
	S += c_cc_t3_t5 >= 29
	c_cc_t3_t5 += MAS[0]

	c_aa_t10 = S.Task('c_aa_t10', length=2, delay_cost=1)
	S += c_aa_t10 >= 30
	c_aa_t10 += MAS[5]

	c_aa_t3_t4 = S.Task('c_aa_t3_t4', length=11, delay_cost=1)
	S += c_aa_t3_t4 >= 30
	c_aa_t3_t4 += MM[0]

	c_ac_t0_t0_in = S.Task('c_ac_t0_t0_in', length=1, delay_cost=1)
	S += c_ac_t0_t0_in >= 30
	c_ac_t0_t0_in += MM_in[0]

	c_ac_t0_t0_mem0 = S.Task('c_ac_t0_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem0 >= 30
	c_ac_t0_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t0_mem1 = S.Task('c_ac_t0_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t0_mem1 >= 30
	c_ac_t0_t0_mem1 += MAIN_MEM_r[1]

	c_cc10 = S.Task('c_cc10', length=2, delay_cost=1)
	S += c_cc10 >= 30
	c_cc10 += MAS[3]

	c_cc_t31_in = S.Task('c_cc_t31_in', length=1, delay_cost=1)
	S += c_cc_t31_in >= 30
	c_cc_t31_in += MAS_in[5]

	c_cc_t31_mem0 = S.Task('c_cc_t31_mem0', length=1, delay_cost=1)
	S += c_cc_t31_mem0 >= 30
	c_cc_t31_mem0 += MM_MEM[2]

	c_cc_t31_mem1 = S.Task('c_cc_t31_mem1', length=1, delay_cost=1)
	S += c_cc_t31_mem1 >= 30
	c_cc_t31_mem1 += MAS_MEM[1]

	c_aa_t2_t3_in = S.Task('c_aa_t2_t3_in', length=1, delay_cost=1)
	S += c_aa_t2_t3_in >= 31
	c_aa_t2_t3_in += MAS_in[4]

	c_aa_t2_t3_mem0 = S.Task('c_aa_t2_t3_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem0 >= 31
	c_aa_t2_t3_mem0 += MAS_MEM[10]

	c_aa_t2_t3_mem1 = S.Task('c_aa_t2_t3_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t3_mem1 >= 31
	c_aa_t2_t3_mem1 += MAS_MEM[11]

	c_aa_t3_t5_in = S.Task('c_aa_t3_t5_in', length=1, delay_cost=1)
	S += c_aa_t3_t5_in >= 31
	c_aa_t3_t5_in += MAS_in[5]

	c_aa_t3_t5_mem0 = S.Task('c_aa_t3_t5_mem0', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem0 >= 31
	c_aa_t3_t5_mem0 += MM_MEM[2]

	c_aa_t3_t5_mem1 = S.Task('c_aa_t3_t5_mem1', length=1, delay_cost=1)
	S += c_aa_t3_t5_mem1 >= 31
	c_aa_t3_t5_mem1 += MM_MEM[1]

	c_ac_t0_t0 = S.Task('c_ac_t0_t0', length=11, delay_cost=1)
	S += c_ac_t0_t0 >= 31
	c_ac_t0_t0 += MM[0]

	c_ac_t1_t0_in = S.Task('c_ac_t1_t0_in', length=1, delay_cost=1)
	S += c_ac_t1_t0_in >= 31
	c_ac_t1_t0_in += MM_in[1]

	c_ac_t1_t0_mem0 = S.Task('c_ac_t1_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem0 >= 31
	c_ac_t1_t0_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t0_mem1 = S.Task('c_ac_t1_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t0_mem1 >= 31
	c_ac_t1_t0_mem1 += MAIN_MEM_r[1]

	c_cc_t31 = S.Task('c_cc_t31', length=2, delay_cost=1)
	S += c_cc_t31 >= 31
	c_cc_t31 += MAS[5]

	c_aa_t2_t3 = S.Task('c_aa_t2_t3', length=2, delay_cost=1)
	S += c_aa_t2_t3 >= 32
	c_aa_t2_t3 += MAS[4]

	c_aa_t3_t5 = S.Task('c_aa_t3_t5', length=2, delay_cost=1)
	S += c_aa_t3_t5 >= 32
	c_aa_t3_t5 += MAS[5]

	c_ac_t1_t0 = S.Task('c_ac_t1_t0', length=11, delay_cost=1)
	S += c_ac_t1_t0 >= 32
	c_ac_t1_t0 += MM[1]

	c_bb_t30_in = S.Task('c_bb_t30_in', length=1, delay_cost=1)
	S += c_bb_t30_in >= 32
	c_bb_t30_in += MAS_in[5]

	c_bb_t30_mem0 = S.Task('c_bb_t30_mem0', length=1, delay_cost=1)
	S += c_bb_t30_mem0 >= 32
	c_bb_t30_mem0 += MM_MEM[2]

	c_bb_t30_mem1 = S.Task('c_bb_t30_mem1', length=1, delay_cost=1)
	S += c_bb_t30_mem1 >= 32
	c_bb_t30_mem1 += MM_MEM[3]

	c_bc_t0_t3_in = S.Task('c_bc_t0_t3_in', length=1, delay_cost=1)
	S += c_bc_t0_t3_in >= 32
	c_bc_t0_t3_in += MAS_in[2]

	c_bc_t0_t3_mem0 = S.Task('c_bc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem0 >= 32
	c_bc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t3_mem1 = S.Task('c_bc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t3_mem1 >= 32
	c_bc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_aa_t30_in = S.Task('c_aa_t30_in', length=1, delay_cost=1)
	S += c_aa_t30_in >= 33
	c_aa_t30_in += MAS_in[4]

	c_aa_t30_mem0 = S.Task('c_aa_t30_mem0', length=1, delay_cost=1)
	S += c_aa_t30_mem0 >= 33
	c_aa_t30_mem0 += MM_MEM[2]

	c_aa_t30_mem1 = S.Task('c_aa_t30_mem1', length=1, delay_cost=1)
	S += c_aa_t30_mem1 >= 33
	c_aa_t30_mem1 += MM_MEM[1]

	c_ac_t0_t1_in = S.Task('c_ac_t0_t1_in', length=1, delay_cost=1)
	S += c_ac_t0_t1_in >= 33
	c_ac_t0_t1_in += MM_in[0]

	c_ac_t0_t1_mem0 = S.Task('c_ac_t0_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem0 >= 33
	c_ac_t0_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t1_mem1 = S.Task('c_ac_t0_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t1_mem1 >= 33
	c_ac_t0_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t30 = S.Task('c_bb_t30', length=2, delay_cost=1)
	S += c_bb_t30 >= 33
	c_bb_t30 += MAS[5]

	c_bc_t0_t3 = S.Task('c_bc_t0_t3', length=2, delay_cost=1)
	S += c_bc_t0_t3 >= 33
	c_bc_t0_t3 += MAS[2]

	c_aa_t30 = S.Task('c_aa_t30', length=2, delay_cost=1)
	S += c_aa_t30 >= 34
	c_aa_t30 += MAS[4]

	c_ac_t0_t1 = S.Task('c_ac_t0_t1', length=11, delay_cost=1)
	S += c_ac_t0_t1 >= 34
	c_ac_t0_t1 += MM[0]

	c_ac_t31_in = S.Task('c_ac_t31_in', length=1, delay_cost=1)
	S += c_ac_t31_in >= 34
	c_ac_t31_in += MAS_in[5]

	c_ac_t31_mem0 = S.Task('c_ac_t31_mem0', length=1, delay_cost=1)
	S += c_ac_t31_mem0 >= 34
	c_ac_t31_mem0 += MAIN_MEM_r[0]

	c_ac_t31_mem1 = S.Task('c_ac_t31_mem1', length=1, delay_cost=1)
	S += c_ac_t31_mem1 >= 34
	c_ac_t31_mem1 += MAIN_MEM_r[1]

	c_bb10_in = S.Task('c_bb10_in', length=1, delay_cost=1)
	S += c_bb10_in >= 34
	c_bb10_in += MAS_in[1]

	c_bb10_mem0 = S.Task('c_bb10_mem0', length=1, delay_cost=1)
	S += c_bb10_mem0 >= 34
	c_bb10_mem0 += MAS_MEM[10]

	c_bb10_mem1 = S.Task('c_bb10_mem1', length=1, delay_cost=1)
	S += c_bb10_mem1 >= 34
	c_bb10_mem1 += MAS_MEM[11]

	c_bb_t3_t5_in = S.Task('c_bb_t3_t5_in', length=1, delay_cost=1)
	S += c_bb_t3_t5_in >= 34
	c_bb_t3_t5_in += MAS_in[2]

	c_bb_t3_t5_mem0 = S.Task('c_bb_t3_t5_mem0', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem0 >= 34
	c_bb_t3_t5_mem0 += MM_MEM[2]

	c_bb_t3_t5_mem1 = S.Task('c_bb_t3_t5_mem1', length=1, delay_cost=1)
	S += c_bb_t3_t5_mem1 >= 34
	c_bb_t3_t5_mem1 += MM_MEM[3]

	c_aa10_in = S.Task('c_aa10_in', length=1, delay_cost=1)
	S += c_aa10_in >= 35
	c_aa10_in += MAS_in[3]

	c_aa10_mem0 = S.Task('c_aa10_mem0', length=1, delay_cost=1)
	S += c_aa10_mem0 >= 35
	c_aa10_mem0 += MAS_MEM[8]

	c_aa10_mem1 = S.Task('c_aa10_mem1', length=1, delay_cost=1)
	S += c_aa10_mem1 >= 35
	c_aa10_mem1 += MAS_MEM[9]

	c_ac_t31 = S.Task('c_ac_t31', length=2, delay_cost=1)
	S += c_ac_t31 >= 35
	c_ac_t31 += MAS[5]

	c_bb10 = S.Task('c_bb10', length=2, delay_cost=1)
	S += c_bb10 >= 35
	c_bb10 += MAS[1]

	c_bb_t3_t5 = S.Task('c_bb_t3_t5', length=2, delay_cost=1)
	S += c_bb_t3_t5 >= 35
	c_bb_t3_t5 += MAS[2]

	c_bc_t1_t3_in = S.Task('c_bc_t1_t3_in', length=1, delay_cost=1)
	S += c_bc_t1_t3_in >= 35
	c_bc_t1_t3_in += MAS_in[1]

	c_bc_t1_t3_mem0 = S.Task('c_bc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem0 >= 35
	c_bc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t3_mem1 = S.Task('c_bc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t3_mem1 >= 35
	c_bc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_aa10 = S.Task('c_aa10', length=2, delay_cost=1)
	S += c_aa10 >= 36
	c_aa10 += MAS[3]

	c_ab_t1_t5_in = S.Task('c_ab_t1_t5_in', length=1, delay_cost=1)
	S += c_ab_t1_t5_in >= 36
	c_ab_t1_t5_in += MAS_in[5]

	c_ab_t1_t5_mem0 = S.Task('c_ab_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem0 >= 36
	c_ab_t1_t5_mem0 += MM_MEM[0]

	c_ab_t1_t5_mem1 = S.Task('c_ab_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t5_mem1 >= 36
	c_ab_t1_t5_mem1 += MM_MEM[3]

	c_ac_t0_t3_in = S.Task('c_ac_t0_t3_in', length=1, delay_cost=1)
	S += c_ac_t0_t3_in >= 36
	c_ac_t0_t3_in += MAS_in[2]

	c_ac_t0_t3_mem0 = S.Task('c_ac_t0_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem0 >= 36
	c_ac_t0_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t3_mem1 = S.Task('c_ac_t0_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t3_mem1 >= 36
	c_ac_t0_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t1_t3 = S.Task('c_bc_t1_t3', length=2, delay_cost=1)
	S += c_bc_t1_t3 >= 36
	c_bc_t1_t3 += MAS[1]

	c_ab_t10_in = S.Task('c_ab_t10_in', length=1, delay_cost=1)
	S += c_ab_t10_in >= 37
	c_ab_t10_in += MAS_in[0]

	c_ab_t10_mem0 = S.Task('c_ab_t10_mem0', length=1, delay_cost=1)
	S += c_ab_t10_mem0 >= 37
	c_ab_t10_mem0 += MM_MEM[0]

	c_ab_t10_mem1 = S.Task('c_ab_t10_mem1', length=1, delay_cost=1)
	S += c_ab_t10_mem1 >= 37
	c_ab_t10_mem1 += MM_MEM[3]

	c_ab_t1_t5 = S.Task('c_ab_t1_t5', length=2, delay_cost=1)
	S += c_ab_t1_t5 >= 37
	c_ab_t1_t5 += MAS[5]

	c_ac_t0_t3 = S.Task('c_ac_t0_t3', length=2, delay_cost=1)
	S += c_ac_t0_t3 >= 37
	c_ac_t0_t3 += MAS[2]

	c_ac_t1_t1_in = S.Task('c_ac_t1_t1_in', length=1, delay_cost=1)
	S += c_ac_t1_t1_in >= 37
	c_ac_t1_t1_in += MM_in[1]

	c_ac_t1_t1_mem0 = S.Task('c_ac_t1_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem0 >= 37
	c_ac_t1_t1_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t1_mem1 = S.Task('c_ac_t1_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t1_mem1 >= 37
	c_ac_t1_t1_mem1 += MAIN_MEM_r[1]

	c_bb_t31_in = S.Task('c_bb_t31_in', length=1, delay_cost=1)
	S += c_bb_t31_in >= 37
	c_bb_t31_in += MAS_in[4]

	c_bb_t31_mem0 = S.Task('c_bb_t31_mem0', length=1, delay_cost=1)
	S += c_bb_t31_mem0 >= 37
	c_bb_t31_mem0 += MM_MEM[2]

	c_bb_t31_mem1 = S.Task('c_bb_t31_mem1', length=1, delay_cost=1)
	S += c_bb_t31_mem1 >= 37
	c_bb_t31_mem1 += MAS_MEM[5]

	c_ab_t10 = S.Task('c_ab_t10', length=2, delay_cost=1)
	S += c_ab_t10 >= 38
	c_ab_t10 += MAS[0]

	c_ac_t1_t1 = S.Task('c_ac_t1_t1', length=11, delay_cost=1)
	S += c_ac_t1_t1 >= 38
	c_ac_t1_t1 += MM[1]

	c_bb_t31 = S.Task('c_bb_t31', length=2, delay_cost=1)
	S += c_bb_t31 >= 38
	c_bb_t31 += MAS[4]

	c_bc_t1_t0_in = S.Task('c_bc_t1_t0_in', length=1, delay_cost=1)
	S += c_bc_t1_t0_in >= 38
	c_bc_t1_t0_in += MM_in[1]

	c_bc_t1_t0_mem0 = S.Task('c_bc_t1_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem0 >= 38
	c_bc_t1_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t0_mem1 = S.Task('c_bc_t1_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t0_mem1 >= 38
	c_bc_t1_t0_mem1 += MAIN_MEM_r[1]

	c_ab_t50_in = S.Task('c_ab_t50_in', length=1, delay_cost=1)
	S += c_ab_t50_in >= 39
	c_ab_t50_in += MAS_in[4]

	c_ab_t50_mem0 = S.Task('c_ab_t50_mem0', length=1, delay_cost=1)
	S += c_ab_t50_mem0 >= 39
	c_ab_t50_mem0 += MAS_MEM[8]

	c_ab_t50_mem1 = S.Task('c_ab_t50_mem1', length=1, delay_cost=1)
	S += c_ab_t50_mem1 >= 39
	c_ab_t50_mem1 += MAS_MEM[1]

	c_bc_t1_t0 = S.Task('c_bc_t1_t0', length=11, delay_cost=1)
	S += c_bc_t1_t0 >= 39
	c_bc_t1_t0 += MM[1]

	c_bc_t31_in = S.Task('c_bc_t31_in', length=1, delay_cost=1)
	S += c_bc_t31_in >= 39
	c_bc_t31_in += MAS_in[0]

	c_bc_t31_mem0 = S.Task('c_bc_t31_mem0', length=1, delay_cost=1)
	S += c_bc_t31_mem0 >= 39
	c_bc_t31_mem0 += MAIN_MEM_r[0]

	c_bc_t31_mem1 = S.Task('c_bc_t31_mem1', length=1, delay_cost=1)
	S += c_bc_t31_mem1 >= 39
	c_bc_t31_mem1 += MAIN_MEM_r[1]

	c_aa_t31_in = S.Task('c_aa_t31_in', length=1, delay_cost=1)
	S += c_aa_t31_in >= 40
	c_aa_t31_in += MAS_in[2]

	c_aa_t31_mem0 = S.Task('c_aa_t31_mem0', length=1, delay_cost=1)
	S += c_aa_t31_mem0 >= 40
	c_aa_t31_mem0 += MM_MEM[0]

	c_aa_t31_mem1 = S.Task('c_aa_t31_mem1', length=1, delay_cost=1)
	S += c_aa_t31_mem1 >= 40
	c_aa_t31_mem1 += MAS_MEM[11]

	c_ab_t50 = S.Task('c_ab_t50', length=2, delay_cost=1)
	S += c_ab_t50 >= 40
	c_ab_t50 += MAS[4]

	c_ac_t21_in = S.Task('c_ac_t21_in', length=1, delay_cost=1)
	S += c_ac_t21_in >= 40
	c_ac_t21_in += MAS_in[0]

	c_ac_t21_mem0 = S.Task('c_ac_t21_mem0', length=1, delay_cost=1)
	S += c_ac_t21_mem0 >= 40
	c_ac_t21_mem0 += MAIN_MEM_r[0]

	c_ac_t21_mem1 = S.Task('c_ac_t21_mem1', length=1, delay_cost=1)
	S += c_ac_t21_mem1 >= 40
	c_ac_t21_mem1 += MAIN_MEM_r[1]

	c_bc_t31 = S.Task('c_bc_t31', length=2, delay_cost=1)
	S += c_bc_t31 >= 40
	c_bc_t31 += MAS[0]

	c_aa_t31 = S.Task('c_aa_t31', length=2, delay_cost=1)
	S += c_aa_t31 >= 41
	c_aa_t31 += MAS[2]

	c_ac_t21 = S.Task('c_ac_t21', length=2, delay_cost=1)
	S += c_ac_t21 >= 41
	c_ac_t21 += MAS[0]

	c_bc_t0_t1_in = S.Task('c_bc_t0_t1_in', length=1, delay_cost=1)
	S += c_bc_t0_t1_in >= 41
	c_bc_t0_t1_in += MM_in[1]

	c_bc_t0_t1_mem0 = S.Task('c_bc_t0_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem0 >= 41
	c_bc_t0_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t1_mem1 = S.Task('c_bc_t0_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t1_mem1 >= 41
	c_bc_t0_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t1_in = S.Task('c_ac_t4_t1_in', length=1, delay_cost=1)
	S += c_ac_t4_t1_in >= 42
	c_ac_t4_t1_in += MM_in[1]

	c_ac_t4_t1_mem0 = S.Task('c_ac_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem0 >= 42
	c_ac_t4_t1_mem0 += MAS_MEM[0]

	c_ac_t4_t1_mem1 = S.Task('c_ac_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t1_mem1 >= 42
	c_ac_t4_t1_mem1 += MAS_MEM[11]

	c_bc_t0_t1 = S.Task('c_bc_t0_t1', length=11, delay_cost=1)
	S += c_bc_t0_t1 >= 42
	c_bc_t0_t1 += MM[1]

	c_bc_t1_t1_in = S.Task('c_bc_t1_t1_in', length=1, delay_cost=1)
	S += c_bc_t1_t1_in >= 42
	c_bc_t1_t1_in += MM_in[0]

	c_bc_t1_t1_mem0 = S.Task('c_bc_t1_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem0 >= 42
	c_bc_t1_t1_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t1_mem1 = S.Task('c_bc_t1_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t1_mem1 >= 42
	c_bc_t1_t1_mem1 += MAIN_MEM_r[1]

	c_ac_t30_in = S.Task('c_ac_t30_in', length=1, delay_cost=1)
	S += c_ac_t30_in >= 43
	c_ac_t30_in += MAS_in[5]

	c_ac_t30_mem0 = S.Task('c_ac_t30_mem0', length=1, delay_cost=1)
	S += c_ac_t30_mem0 >= 43
	c_ac_t30_mem0 += MAIN_MEM_r[0]

	c_ac_t30_mem1 = S.Task('c_ac_t30_mem1', length=1, delay_cost=1)
	S += c_ac_t30_mem1 >= 43
	c_ac_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t1 = S.Task('c_ac_t4_t1', length=11, delay_cost=1)
	S += c_ac_t4_t1 >= 43
	c_ac_t4_t1 += MM[1]

	c_bc_t1_t1 = S.Task('c_bc_t1_t1', length=11, delay_cost=1)
	S += c_bc_t1_t1 >= 43
	c_bc_t1_t1 += MM[0]

	c_ac_t0_t2_in = S.Task('c_ac_t0_t2_in', length=1, delay_cost=1)
	S += c_ac_t0_t2_in >= 44
	c_ac_t0_t2_in += MAS_in[2]

	c_ac_t0_t2_mem0 = S.Task('c_ac_t0_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem0 >= 44
	c_ac_t0_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t0_t2_mem1 = S.Task('c_ac_t0_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t2_mem1 >= 44
	c_ac_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t5_in = S.Task('c_ac_t0_t5_in', length=1, delay_cost=1)
	S += c_ac_t0_t5_in >= 44
	c_ac_t0_t5_in += MAS_in[4]

	c_ac_t0_t5_mem0 = S.Task('c_ac_t0_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem0 >= 44
	c_ac_t0_t5_mem0 += MM_MEM[0]

	c_ac_t0_t5_mem1 = S.Task('c_ac_t0_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t5_mem1 >= 44
	c_ac_t0_t5_mem1 += MM_MEM[1]

	c_ac_t30 = S.Task('c_ac_t30', length=2, delay_cost=1)
	S += c_ac_t30 >= 44
	c_ac_t30 += MAS[5]

	c_ac_t00_in = S.Task('c_ac_t00_in', length=1, delay_cost=1)
	S += c_ac_t00_in >= 45
	c_ac_t00_in += MAS_in[0]

	c_ac_t00_mem0 = S.Task('c_ac_t00_mem0', length=1, delay_cost=1)
	S += c_ac_t00_mem0 >= 45
	c_ac_t00_mem0 += MM_MEM[0]

	c_ac_t00_mem1 = S.Task('c_ac_t00_mem1', length=1, delay_cost=1)
	S += c_ac_t00_mem1 >= 45
	c_ac_t00_mem1 += MM_MEM[1]

	c_ac_t0_t2 = S.Task('c_ac_t0_t2', length=2, delay_cost=1)
	S += c_ac_t0_t2 >= 45
	c_ac_t0_t2 += MAS[2]

	c_ac_t0_t5 = S.Task('c_ac_t0_t5', length=2, delay_cost=1)
	S += c_ac_t0_t5 >= 45
	c_ac_t0_t5 += MAS[4]

	c_ac_t4_t3_in = S.Task('c_ac_t4_t3_in', length=1, delay_cost=1)
	S += c_ac_t4_t3_in >= 45
	c_ac_t4_t3_in += MAS_in[3]

	c_ac_t4_t3_mem0 = S.Task('c_ac_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem0 >= 45
	c_ac_t4_t3_mem0 += MAS_MEM[10]

	c_ac_t4_t3_mem1 = S.Task('c_ac_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t3_mem1 >= 45
	c_ac_t4_t3_mem1 += MAS_MEM[11]

	c_bc_t0_t2_in = S.Task('c_bc_t0_t2_in', length=1, delay_cost=1)
	S += c_bc_t0_t2_in >= 45
	c_bc_t0_t2_in += MAS_in[4]

	c_bc_t0_t2_mem0 = S.Task('c_bc_t0_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem0 >= 45
	c_bc_t0_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t2_mem1 = S.Task('c_bc_t0_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t2_mem1 >= 45
	c_bc_t0_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t00 = S.Task('c_ac_t00', length=2, delay_cost=1)
	S += c_ac_t00 >= 46
	c_ac_t00 += MAS[0]

	c_ac_t0_t4_in = S.Task('c_ac_t0_t4_in', length=1, delay_cost=1)
	S += c_ac_t0_t4_in >= 46
	c_ac_t0_t4_in += MM_in[1]

	c_ac_t0_t4_mem0 = S.Task('c_ac_t0_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem0 >= 46
	c_ac_t0_t4_mem0 += MAS_MEM[4]

	c_ac_t0_t4_mem1 = S.Task('c_ac_t0_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t0_t4_mem1 >= 46
	c_ac_t0_t4_mem1 += MAS_MEM[5]

	c_ac_t4_t3 = S.Task('c_ac_t4_t3', length=2, delay_cost=1)
	S += c_ac_t4_t3 >= 46
	c_ac_t4_t3 += MAS[3]

	c_bc_t0_t2 = S.Task('c_bc_t0_t2', length=2, delay_cost=1)
	S += c_bc_t0_t2 >= 46
	c_bc_t0_t2 += MAS[4]

	c_bc_t1_t2_in = S.Task('c_bc_t1_t2_in', length=1, delay_cost=1)
	S += c_bc_t1_t2_in >= 46
	c_bc_t1_t2_in += MAS_in[4]

	c_bc_t1_t2_mem0 = S.Task('c_bc_t1_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem0 >= 46
	c_bc_t1_t2_mem0 += MAIN_MEM_r[0]

	c_bc_t1_t2_mem1 = S.Task('c_bc_t1_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t2_mem1 >= 46
	c_bc_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t0_t4 = S.Task('c_ac_t0_t4', length=11, delay_cost=1)
	S += c_ac_t0_t4 >= 47
	c_ac_t0_t4 += MM[1]

	c_bc_t0_t4_in = S.Task('c_bc_t0_t4_in', length=1, delay_cost=1)
	S += c_bc_t0_t4_in >= 47
	c_bc_t0_t4_in += MM_in[0]

	c_bc_t0_t4_mem0 = S.Task('c_bc_t0_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem0 >= 47
	c_bc_t0_t4_mem0 += MAS_MEM[8]

	c_bc_t0_t4_mem1 = S.Task('c_bc_t0_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t4_mem1 >= 47
	c_bc_t0_t4_mem1 += MAS_MEM[5]

	c_bc_t1_t2 = S.Task('c_bc_t1_t2', length=2, delay_cost=1)
	S += c_bc_t1_t2 >= 47
	c_bc_t1_t2 += MAS[4]

	c_bc_t30_in = S.Task('c_bc_t30_in', length=1, delay_cost=1)
	S += c_bc_t30_in >= 47
	c_bc_t30_in += MAS_in[0]

	c_bc_t30_mem0 = S.Task('c_bc_t30_mem0', length=1, delay_cost=1)
	S += c_bc_t30_mem0 >= 47
	c_bc_t30_mem0 += MAIN_MEM_r[0]

	c_bc_t30_mem1 = S.Task('c_bc_t30_mem1', length=1, delay_cost=1)
	S += c_bc_t30_mem1 >= 47
	c_bc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t1_t2_in = S.Task('c_ab_t1_t2_in', length=1, delay_cost=1)
	S += c_ab_t1_t2_in >= 48
	c_ab_t1_t2_in += MAS_in[0]

	c_ab_t1_t2_mem0 = S.Task('c_ab_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem0 >= 48
	c_ab_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t2_mem1 = S.Task('c_ab_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t2_mem1 >= 48
	c_ab_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t10_in = S.Task('c_ac_t10_in', length=1, delay_cost=1)
	S += c_ac_t10_in >= 48
	c_ac_t10_in += MAS_in[4]

	c_ac_t10_mem0 = S.Task('c_ac_t10_mem0', length=1, delay_cost=1)
	S += c_ac_t10_mem0 >= 48
	c_ac_t10_mem0 += MM_MEM[2]

	c_ac_t10_mem1 = S.Task('c_ac_t10_mem1', length=1, delay_cost=1)
	S += c_ac_t10_mem1 >= 48
	c_ac_t10_mem1 += MM_MEM[3]

	c_bc_t0_t4 = S.Task('c_bc_t0_t4', length=11, delay_cost=1)
	S += c_bc_t0_t4 >= 48
	c_bc_t0_t4 += MM[0]

	c_bc_t1_t4_in = S.Task('c_bc_t1_t4_in', length=1, delay_cost=1)
	S += c_bc_t1_t4_in >= 48
	c_bc_t1_t4_in += MM_in[0]

	c_bc_t1_t4_mem0 = S.Task('c_bc_t1_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem0 >= 48
	c_bc_t1_t4_mem0 += MAS_MEM[8]

	c_bc_t1_t4_mem1 = S.Task('c_bc_t1_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t4_mem1 >= 48
	c_bc_t1_t4_mem1 += MAS_MEM[3]

	c_bc_t30 = S.Task('c_bc_t30', length=2, delay_cost=1)
	S += c_bc_t30 >= 48
	c_bc_t30 += MAS[0]

	c_ab_t1_t2 = S.Task('c_ab_t1_t2', length=2, delay_cost=1)
	S += c_ab_t1_t2 >= 49
	c_ab_t1_t2 += MAS[0]

	c_ab_t31_in = S.Task('c_ab_t31_in', length=1, delay_cost=1)
	S += c_ab_t31_in >= 49
	c_ab_t31_in += MAS_in[2]

	c_ab_t31_mem0 = S.Task('c_ab_t31_mem0', length=1, delay_cost=1)
	S += c_ab_t31_mem0 >= 49
	c_ab_t31_mem0 += MAIN_MEM_r[0]

	c_ab_t31_mem1 = S.Task('c_ab_t31_mem1', length=1, delay_cost=1)
	S += c_ab_t31_mem1 >= 49
	c_ab_t31_mem1 += MAIN_MEM_r[1]

	c_ac_t10 = S.Task('c_ac_t10', length=2, delay_cost=1)
	S += c_ac_t10 >= 49
	c_ac_t10 += MAS[4]

	c_ac_t1_t5_in = S.Task('c_ac_t1_t5_in', length=1, delay_cost=1)
	S += c_ac_t1_t5_in >= 49
	c_ac_t1_t5_in += MAS_in[0]

	c_ac_t1_t5_mem0 = S.Task('c_ac_t1_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem0 >= 49
	c_ac_t1_t5_mem0 += MM_MEM[2]

	c_ac_t1_t5_mem1 = S.Task('c_ac_t1_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t5_mem1 >= 49
	c_ac_t1_t5_mem1 += MM_MEM[3]

	c_bc_t1_t4 = S.Task('c_bc_t1_t4', length=11, delay_cost=1)
	S += c_bc_t1_t4 >= 49
	c_bc_t1_t4 += MM[0]

	c_bc_t4_t3_in = S.Task('c_bc_t4_t3_in', length=1, delay_cost=1)
	S += c_bc_t4_t3_in >= 49
	c_bc_t4_t3_in += MAS_in[1]

	c_bc_t4_t3_mem0 = S.Task('c_bc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem0 >= 49
	c_bc_t4_t3_mem0 += MAS_MEM[0]

	c_bc_t4_t3_mem1 = S.Task('c_bc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t3_mem1 >= 49
	c_bc_t4_t3_mem1 += MAS_MEM[1]

	c_ab_t31 = S.Task('c_ab_t31', length=2, delay_cost=1)
	S += c_ab_t31 >= 50
	c_ab_t31 += MAS[2]

	c_ac_t1_t5 = S.Task('c_ac_t1_t5', length=2, delay_cost=1)
	S += c_ac_t1_t5 >= 50
	c_ac_t1_t5 += MAS[0]

	c_ac_t20_in = S.Task('c_ac_t20_in', length=1, delay_cost=1)
	S += c_ac_t20_in >= 50
	c_ac_t20_in += MAS_in[0]

	c_ac_t20_mem0 = S.Task('c_ac_t20_mem0', length=1, delay_cost=1)
	S += c_ac_t20_mem0 >= 50
	c_ac_t20_mem0 += MAIN_MEM_r[0]

	c_ac_t20_mem1 = S.Task('c_ac_t20_mem1', length=1, delay_cost=1)
	S += c_ac_t20_mem1 >= 50
	c_ac_t20_mem1 += MAIN_MEM_r[1]

	c_ac_t50_in = S.Task('c_ac_t50_in', length=1, delay_cost=1)
	S += c_ac_t50_in >= 50
	c_ac_t50_in += MAS_in[1]

	c_ac_t50_mem0 = S.Task('c_ac_t50_mem0', length=1, delay_cost=1)
	S += c_ac_t50_mem0 >= 50
	c_ac_t50_mem0 += MAS_MEM[0]

	c_ac_t50_mem1 = S.Task('c_ac_t50_mem1', length=1, delay_cost=1)
	S += c_ac_t50_mem1 >= 50
	c_ac_t50_mem1 += MAS_MEM[9]

	c_bc_t4_t3 = S.Task('c_bc_t4_t3', length=2, delay_cost=1)
	S += c_bc_t4_t3 >= 50
	c_bc_t4_t3 += MAS[1]

	c_ac_t20 = S.Task('c_ac_t20', length=2, delay_cost=1)
	S += c_ac_t20 >= 51
	c_ac_t20 += MAS[0]

	c_ac_t50 = S.Task('c_ac_t50', length=2, delay_cost=1)
	S += c_ac_t50 >= 51
	c_ac_t50 += MAS[1]

	c_bc_t21_in = S.Task('c_bc_t21_in', length=1, delay_cost=1)
	S += c_bc_t21_in >= 51
	c_bc_t21_in += MAS_in[3]

	c_bc_t21_mem0 = S.Task('c_bc_t21_mem0', length=1, delay_cost=1)
	S += c_bc_t21_mem0 >= 51
	c_bc_t21_mem0 += MAIN_MEM_r[0]

	c_bc_t21_mem1 = S.Task('c_bc_t21_mem1', length=1, delay_cost=1)
	S += c_bc_t21_mem1 >= 51
	c_bc_t21_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t2_in = S.Task('c_ac_t4_t2_in', length=1, delay_cost=1)
	S += c_ac_t4_t2_in >= 52
	c_ac_t4_t2_in += MAS_in[2]

	c_ac_t4_t2_mem0 = S.Task('c_ac_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem0 >= 52
	c_ac_t4_t2_mem0 += MAS_MEM[0]

	c_ac_t4_t2_mem1 = S.Task('c_ac_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t2_mem1 >= 52
	c_ac_t4_t2_mem1 += MAS_MEM[1]

	c_bc_t20_in = S.Task('c_bc_t20_in', length=1, delay_cost=1)
	S += c_bc_t20_in >= 52
	c_bc_t20_in += MAS_in[1]

	c_bc_t20_mem0 = S.Task('c_bc_t20_mem0', length=1, delay_cost=1)
	S += c_bc_t20_mem0 >= 52
	c_bc_t20_mem0 += MAIN_MEM_r[0]

	c_bc_t20_mem1 = S.Task('c_bc_t20_mem1', length=1, delay_cost=1)
	S += c_bc_t20_mem1 >= 52
	c_bc_t20_mem1 += MAIN_MEM_r[1]

	c_bc_t21 = S.Task('c_bc_t21', length=2, delay_cost=1)
	S += c_bc_t21 >= 52
	c_bc_t21 += MAS[3]

	c_ac_t1_t3_in = S.Task('c_ac_t1_t3_in', length=1, delay_cost=1)
	S += c_ac_t1_t3_in >= 53
	c_ac_t1_t3_in += MAS_in[2]

	c_ac_t1_t3_mem0 = S.Task('c_ac_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem0 >= 53
	c_ac_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t3_mem1 = S.Task('c_ac_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t3_mem1 >= 53
	c_ac_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t4_t0_in = S.Task('c_ac_t4_t0_in', length=1, delay_cost=1)
	S += c_ac_t4_t0_in >= 53
	c_ac_t4_t0_in += MM_in[1]

	c_ac_t4_t0_mem0 = S.Task('c_ac_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem0 >= 53
	c_ac_t4_t0_mem0 += MAS_MEM[0]

	c_ac_t4_t0_mem1 = S.Task('c_ac_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t0_mem1 >= 53
	c_ac_t4_t0_mem1 += MAS_MEM[11]

	c_ac_t4_t2 = S.Task('c_ac_t4_t2', length=2, delay_cost=1)
	S += c_ac_t4_t2 >= 53
	c_ac_t4_t2 += MAS[2]

	c_bc_t1_t5_in = S.Task('c_bc_t1_t5_in', length=1, delay_cost=1)
	S += c_bc_t1_t5_in >= 53
	c_bc_t1_t5_in += MAS_in[4]

	c_bc_t1_t5_mem0 = S.Task('c_bc_t1_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem0 >= 53
	c_bc_t1_t5_mem0 += MM_MEM[2]

	c_bc_t1_t5_mem1 = S.Task('c_bc_t1_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t1_t5_mem1 >= 53
	c_bc_t1_t5_mem1 += MM_MEM[1]

	c_bc_t20 = S.Task('c_bc_t20', length=2, delay_cost=1)
	S += c_bc_t20 >= 53
	c_bc_t20 += MAS[1]

	c_bc_t4_t1_in = S.Task('c_bc_t4_t1_in', length=1, delay_cost=1)
	S += c_bc_t4_t1_in >= 53
	c_bc_t4_t1_in += MM_in[0]

	c_bc_t4_t1_mem0 = S.Task('c_bc_t4_t1_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem0 >= 53
	c_bc_t4_t1_mem0 += MAS_MEM[6]

	c_bc_t4_t1_mem1 = S.Task('c_bc_t4_t1_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t1_mem1 >= 53
	c_bc_t4_t1_mem1 += MAS_MEM[1]

	c_ac_t1_t2_in = S.Task('c_ac_t1_t2_in', length=1, delay_cost=1)
	S += c_ac_t1_t2_in >= 54
	c_ac_t1_t2_in += MAS_in[1]

	c_ac_t1_t2_mem0 = S.Task('c_ac_t1_t2_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem0 >= 54
	c_ac_t1_t2_mem0 += MAIN_MEM_r[0]

	c_ac_t1_t2_mem1 = S.Task('c_ac_t1_t2_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t2_mem1 >= 54
	c_ac_t1_t2_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t3 = S.Task('c_ac_t1_t3', length=2, delay_cost=1)
	S += c_ac_t1_t3 >= 54
	c_ac_t1_t3 += MAS[2]

	c_ac_t4_t0 = S.Task('c_ac_t4_t0', length=11, delay_cost=1)
	S += c_ac_t4_t0 >= 54
	c_ac_t4_t0 += MM[1]

	c_ac_t4_t4_in = S.Task('c_ac_t4_t4_in', length=1, delay_cost=1)
	S += c_ac_t4_t4_in >= 54
	c_ac_t4_t4_in += MM_in[1]

	c_ac_t4_t4_mem0 = S.Task('c_ac_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem0 >= 54
	c_ac_t4_t4_mem0 += MAS_MEM[4]

	c_ac_t4_t4_mem1 = S.Task('c_ac_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t4_mem1 >= 54
	c_ac_t4_t4_mem1 += MAS_MEM[7]

	c_bc_t10_in = S.Task('c_bc_t10_in', length=1, delay_cost=1)
	S += c_bc_t10_in >= 54
	c_bc_t10_in += MAS_in[0]

	c_bc_t10_mem0 = S.Task('c_bc_t10_mem0', length=1, delay_cost=1)
	S += c_bc_t10_mem0 >= 54
	c_bc_t10_mem0 += MM_MEM[2]

	c_bc_t10_mem1 = S.Task('c_bc_t10_mem1', length=1, delay_cost=1)
	S += c_bc_t10_mem1 >= 54
	c_bc_t10_mem1 += MM_MEM[1]

	c_bc_t1_t5 = S.Task('c_bc_t1_t5', length=2, delay_cost=1)
	S += c_bc_t1_t5 >= 54
	c_bc_t1_t5 += MAS[4]

	c_bc_t4_t0_in = S.Task('c_bc_t4_t0_in', length=1, delay_cost=1)
	S += c_bc_t4_t0_in >= 54
	c_bc_t4_t0_in += MM_in[0]

	c_bc_t4_t0_mem0 = S.Task('c_bc_t4_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem0 >= 54
	c_bc_t4_t0_mem0 += MAS_MEM[2]

	c_bc_t4_t0_mem1 = S.Task('c_bc_t4_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t0_mem1 >= 54
	c_bc_t4_t0_mem1 += MAS_MEM[1]

	c_bc_t4_t1 = S.Task('c_bc_t4_t1', length=11, delay_cost=1)
	S += c_bc_t4_t1 >= 54
	c_bc_t4_t1 += MM[0]

	c_ac_t1_t2 = S.Task('c_ac_t1_t2', length=2, delay_cost=1)
	S += c_ac_t1_t2 >= 55
	c_ac_t1_t2 += MAS[1]

	c_ac_t4_t4 = S.Task('c_ac_t4_t4', length=11, delay_cost=1)
	S += c_ac_t4_t4 >= 55
	c_ac_t4_t4 += MM[1]

	c_bc_t0_t0_in = S.Task('c_bc_t0_t0_in', length=1, delay_cost=1)
	S += c_bc_t0_t0_in >= 55
	c_bc_t0_t0_in += MM_in[1]

	c_bc_t0_t0_mem0 = S.Task('c_bc_t0_t0_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem0 >= 55
	c_bc_t0_t0_mem0 += MAIN_MEM_r[0]

	c_bc_t0_t0_mem1 = S.Task('c_bc_t0_t0_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t0_mem1 >= 55
	c_bc_t0_t0_mem1 += MAIN_MEM_r[1]

	c_bc_t10 = S.Task('c_bc_t10', length=2, delay_cost=1)
	S += c_bc_t10 >= 55
	c_bc_t10 += MAS[0]

	c_bc_t4_t0 = S.Task('c_bc_t4_t0', length=11, delay_cost=1)
	S += c_bc_t4_t0 >= 55
	c_bc_t4_t0 += MM[0]

	c_bc_t4_t2_in = S.Task('c_bc_t4_t2_in', length=1, delay_cost=1)
	S += c_bc_t4_t2_in >= 55
	c_bc_t4_t2_in += MAS_in[3]

	c_bc_t4_t2_mem0 = S.Task('c_bc_t4_t2_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem0 >= 55
	c_bc_t4_t2_mem0 += MAS_MEM[2]

	c_bc_t4_t2_mem1 = S.Task('c_bc_t4_t2_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t2_mem1 >= 55
	c_bc_t4_t2_mem1 += MAS_MEM[7]

	c_ab_t1_t3_in = S.Task('c_ab_t1_t3_in', length=1, delay_cost=1)
	S += c_ab_t1_t3_in >= 56
	c_ab_t1_t3_in += MAS_in[0]

	c_ab_t1_t3_mem0 = S.Task('c_ab_t1_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem0 >= 56
	c_ab_t1_t3_mem0 += MAIN_MEM_r[0]

	c_ab_t1_t3_mem1 = S.Task('c_ab_t1_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t3_mem1 >= 56
	c_ab_t1_t3_mem1 += MAIN_MEM_r[1]

	c_ac_t1_t4_in = S.Task('c_ac_t1_t4_in', length=1, delay_cost=1)
	S += c_ac_t1_t4_in >= 56
	c_ac_t1_t4_in += MM_in[1]

	c_ac_t1_t4_mem0 = S.Task('c_ac_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem0 >= 56
	c_ac_t1_t4_mem0 += MAS_MEM[2]

	c_ac_t1_t4_mem1 = S.Task('c_ac_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ac_t1_t4_mem1 >= 56
	c_ac_t1_t4_mem1 += MAS_MEM[5]

	c_bc_t0_t0 = S.Task('c_bc_t0_t0', length=11, delay_cost=1)
	S += c_bc_t0_t0 >= 56
	c_bc_t0_t0 += MM[1]

	c_bc_t4_t2 = S.Task('c_bc_t4_t2', length=2, delay_cost=1)
	S += c_bc_t4_t2 >= 56
	c_bc_t4_t2 += MAS[3]

	c_ab_t1_t3 = S.Task('c_ab_t1_t3', length=2, delay_cost=1)
	S += c_ab_t1_t3 >= 57
	c_ab_t1_t3 += MAS[0]

	c_ab_t30_in = S.Task('c_ab_t30_in', length=1, delay_cost=1)
	S += c_ab_t30_in >= 57
	c_ab_t30_in += MAS_in[0]

	c_ab_t30_mem0 = S.Task('c_ab_t30_mem0', length=1, delay_cost=1)
	S += c_ab_t30_mem0 >= 57
	c_ab_t30_mem0 += MAIN_MEM_r[0]

	c_ab_t30_mem1 = S.Task('c_ab_t30_mem1', length=1, delay_cost=1)
	S += c_ab_t30_mem1 >= 57
	c_ab_t30_mem1 += MAIN_MEM_r[1]

	c_ac_t01_in = S.Task('c_ac_t01_in', length=1, delay_cost=1)
	S += c_ac_t01_in >= 57
	c_ac_t01_in += MAS_in[4]

	c_ac_t01_mem0 = S.Task('c_ac_t01_mem0', length=1, delay_cost=1)
	S += c_ac_t01_mem0 >= 57
	c_ac_t01_mem0 += MM_MEM[2]

	c_ac_t01_mem1 = S.Task('c_ac_t01_mem1', length=1, delay_cost=1)
	S += c_ac_t01_mem1 >= 57
	c_ac_t01_mem1 += MAS_MEM[9]

	c_ac_t1_t4 = S.Task('c_ac_t1_t4', length=11, delay_cost=1)
	S += c_ac_t1_t4 >= 57
	c_ac_t1_t4 += MM[1]

	c_bc_t4_t4_in = S.Task('c_bc_t4_t4_in', length=1, delay_cost=1)
	S += c_bc_t4_t4_in >= 57
	c_bc_t4_t4_in += MM_in[1]

	c_bc_t4_t4_mem0 = S.Task('c_bc_t4_t4_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem0 >= 57
	c_bc_t4_t4_mem0 += MAS_MEM[6]

	c_bc_t4_t4_mem1 = S.Task('c_bc_t4_t4_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t4_mem1 >= 57
	c_bc_t4_t4_mem1 += MAS_MEM[3]

	c_ab_t1_t4_in = S.Task('c_ab_t1_t4_in', length=1, delay_cost=1)
	S += c_ab_t1_t4_in >= 58
	c_ab_t1_t4_in += MM_in[1]

	c_ab_t1_t4_mem0 = S.Task('c_ab_t1_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem0 >= 58
	c_ab_t1_t4_mem0 += MAS_MEM[0]

	c_ab_t1_t4_mem1 = S.Task('c_ab_t1_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t1_t4_mem1 >= 58
	c_ab_t1_t4_mem1 += MAS_MEM[1]

	c_ab_t20_in = S.Task('c_ab_t20_in', length=1, delay_cost=1)
	S += c_ab_t20_in >= 58
	c_ab_t20_in += MAS_in[0]

	c_ab_t20_mem0 = S.Task('c_ab_t20_mem0', length=1, delay_cost=1)
	S += c_ab_t20_mem0 >= 58
	c_ab_t20_mem0 += MAIN_MEM_r[0]

	c_ab_t20_mem1 = S.Task('c_ab_t20_mem1', length=1, delay_cost=1)
	S += c_ab_t20_mem1 >= 58
	c_ab_t20_mem1 += MAIN_MEM_r[1]

	c_ab_t30 = S.Task('c_ab_t30', length=2, delay_cost=1)
	S += c_ab_t30 >= 58
	c_ab_t30 += MAS[0]

	c_ac_t01 = S.Task('c_ac_t01', length=2, delay_cost=1)
	S += c_ac_t01 >= 58
	c_ac_t01 += MAS[4]

	c_bc_t4_t4 = S.Task('c_bc_t4_t4', length=11, delay_cost=1)
	S += c_bc_t4_t4 >= 58
	c_bc_t4_t4 += MM[1]

	c_ab_t1_t4 = S.Task('c_ab_t1_t4', length=11, delay_cost=1)
	S += c_ab_t1_t4 >= 59
	c_ab_t1_t4 += MM[1]

	c_ab_t20 = S.Task('c_ab_t20', length=2, delay_cost=1)
	S += c_ab_t20 >= 59
	c_ab_t20 += MAS[0]

	c_ab_t21_in = S.Task('c_ab_t21_in', length=1, delay_cost=1)
	S += c_ab_t21_in >= 59
	c_ab_t21_in += MAS_in[3]

	c_ab_t21_mem0 = S.Task('c_ab_t21_mem0', length=1, delay_cost=1)
	S += c_ab_t21_mem0 >= 59
	c_ab_t21_mem0 += MAIN_MEM_r[0]

	c_ab_t21_mem1 = S.Task('c_ab_t21_mem1', length=1, delay_cost=1)
	S += c_ab_t21_mem1 >= 59
	c_ab_t21_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t3_in = S.Task('c_ab_t4_t3_in', length=1, delay_cost=1)
	S += c_ab_t4_t3_in >= 59
	c_ab_t4_t3_in += MAS_in[0]

	c_ab_t4_t3_mem0 = S.Task('c_ab_t4_t3_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem0 >= 59
	c_ab_t4_t3_mem0 += MAS_MEM[0]

	c_ab_t4_t3_mem1 = S.Task('c_ab_t4_t3_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t3_mem1 >= 59
	c_ab_t4_t3_mem1 += MAS_MEM[5]

	c_bc_t11_in = S.Task('c_bc_t11_in', length=1, delay_cost=1)
	S += c_bc_t11_in >= 59
	c_bc_t11_in += MAS_in[2]

	c_bc_t11_mem0 = S.Task('c_bc_t11_mem0', length=1, delay_cost=1)
	S += c_bc_t11_mem0 >= 59
	c_bc_t11_mem0 += MM_MEM[0]

	c_bc_t11_mem1 = S.Task('c_bc_t11_mem1', length=1, delay_cost=1)
	S += c_bc_t11_mem1 >= 59
	c_bc_t11_mem1 += MAS_MEM[9]

	c_ab_t21 = S.Task('c_ab_t21', length=2, delay_cost=1)
	S += c_ab_t21 >= 60
	c_ab_t21 += MAS[3]

	c_ab_t4_t0_in = S.Task('c_ab_t4_t0_in', length=1, delay_cost=1)
	S += c_ab_t4_t0_in >= 60
	c_ab_t4_t0_in += MM_in[0]

	c_ab_t4_t0_mem0 = S.Task('c_ab_t4_t0_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem0 >= 60
	c_ab_t4_t0_mem0 += MAS_MEM[0]

	c_ab_t4_t0_mem1 = S.Task('c_ab_t4_t0_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t0_mem1 >= 60
	c_ab_t4_t0_mem1 += MAS_MEM[1]

	c_ab_t4_t3 = S.Task('c_ab_t4_t3', length=2, delay_cost=1)
	S += c_ab_t4_t3 >= 60
	c_ab_t4_t3 += MAS[0]

	c_bc_t11 = S.Task('c_bc_t11', length=2, delay_cost=1)
	S += c_bc_t11 >= 60
	c_bc_t11 += MAS[2]

	c_pbc_t30_in = S.Task('c_pbc_t30_in', length=1, delay_cost=1)
	S += c_pbc_t30_in >= 60
	c_pbc_t30_in += MAS_in[5]

	c_pbc_t30_mem0 = S.Task('c_pbc_t30_mem0', length=1, delay_cost=1)
	S += c_pbc_t30_mem0 >= 60
	c_pbc_t30_mem0 += MAIN_MEM_r[0]

	c_pbc_t30_mem1 = S.Task('c_pbc_t30_mem1', length=1, delay_cost=1)
	S += c_pbc_t30_mem1 >= 60
	c_pbc_t30_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t0 = S.Task('c_ab_t4_t0', length=11, delay_cost=1)
	S += c_ab_t4_t0 >= 61
	c_ab_t4_t0 += MM[0]

	c_ab_t4_t1_in = S.Task('c_ab_t4_t1_in', length=1, delay_cost=1)
	S += c_ab_t4_t1_in >= 61
	c_ab_t4_t1_in += MM_in[1]

	c_ab_t4_t1_mem0 = S.Task('c_ab_t4_t1_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem0 >= 61
	c_ab_t4_t1_mem0 += MAS_MEM[6]

	c_ab_t4_t1_mem1 = S.Task('c_ab_t4_t1_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t1_mem1 >= 61
	c_ab_t4_t1_mem1 += MAS_MEM[5]

	c_ab_t4_t2_in = S.Task('c_ab_t4_t2_in', length=1, delay_cost=1)
	S += c_ab_t4_t2_in >= 61
	c_ab_t4_t2_in += MAS_in[4]

	c_ab_t4_t2_mem0 = S.Task('c_ab_t4_t2_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem0 >= 61
	c_ab_t4_t2_mem0 += MAS_MEM[0]

	c_ab_t4_t2_mem1 = S.Task('c_ab_t4_t2_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t2_mem1 >= 61
	c_ab_t4_t2_mem1 += MAS_MEM[7]

	c_pbc_t30 = S.Task('c_pbc_t30', length=2, delay_cost=1)
	S += c_pbc_t30 >= 61
	c_pbc_t30 += MAS[5]

	c_pbc_t31_in = S.Task('c_pbc_t31_in', length=1, delay_cost=1)
	S += c_pbc_t31_in >= 61
	c_pbc_t31_in += MAS_in[0]

	c_pbc_t31_mem0 = S.Task('c_pbc_t31_mem0', length=1, delay_cost=1)
	S += c_pbc_t31_mem0 >= 61
	c_pbc_t31_mem0 += MAIN_MEM_r[0]

	c_pbc_t31_mem1 = S.Task('c_pbc_t31_mem1', length=1, delay_cost=1)
	S += c_pbc_t31_mem1 >= 61
	c_pbc_t31_mem1 += MAIN_MEM_r[1]

	c_ab_t4_t1 = S.Task('c_ab_t4_t1', length=11, delay_cost=1)
	S += c_ab_t4_t1 >= 62
	c_ab_t4_t1 += MM[1]

	c_ab_t4_t2 = S.Task('c_ab_t4_t2', length=2, delay_cost=1)
	S += c_ab_t4_t2 >= 62
	c_ab_t4_t2 += MAS[4]

	c_pbc_t31 = S.Task('c_pbc_t31', length=2, delay_cost=1)
	S += c_pbc_t31 >= 62
	c_pbc_t31 += MAS[0]

	c_pcb_t0_t3_in = S.Task('c_pcb_t0_t3_in', length=1, delay_cost=1)
	S += c_pcb_t0_t3_in >= 62
	c_pcb_t0_t3_in += MAS_in[0]

	c_pcb_t0_t3_mem0 = S.Task('c_pcb_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem0 >= 62
	c_pcb_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t0_t3_mem1 = S.Task('c_pcb_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t0_t3_mem1 >= 62
	c_pcb_t0_t3_mem1 += MAIN_MEM_r[1]

	c_paa_t1_t3_in = S.Task('c_paa_t1_t3_in', length=1, delay_cost=1)
	S += c_paa_t1_t3_in >= 63
	c_paa_t1_t3_in += MAS_in[0]

	c_paa_t1_t3_mem0 = S.Task('c_paa_t1_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem0 >= 63
	c_paa_t1_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t1_t3_mem1 = S.Task('c_paa_t1_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t1_t3_mem1 >= 63
	c_paa_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t4_t3_in = S.Task('c_pbc_t4_t3_in', length=1, delay_cost=1)
	S += c_pbc_t4_t3_in >= 63
	c_pbc_t4_t3_in += MAS_in[4]

	c_pbc_t4_t3_mem0 = S.Task('c_pbc_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem0 >= 63
	c_pbc_t4_t3_mem0 += MAS_MEM[10]

	c_pbc_t4_t3_mem1 = S.Task('c_pbc_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t4_t3_mem1 >= 63
	c_pbc_t4_t3_mem1 += MAS_MEM[1]

	c_pcb_t0_t3 = S.Task('c_pcb_t0_t3', length=2, delay_cost=1)
	S += c_pcb_t0_t3 >= 63
	c_pcb_t0_t3 += MAS[0]

	c_ab_t4_t4_in = S.Task('c_ab_t4_t4_in', length=1, delay_cost=1)
	S += c_ab_t4_t4_in >= 64
	c_ab_t4_t4_in += MM_in[1]

	c_ab_t4_t4_mem0 = S.Task('c_ab_t4_t4_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem0 >= 64
	c_ab_t4_t4_mem0 += MAS_MEM[8]

	c_ab_t4_t4_mem1 = S.Task('c_ab_t4_t4_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t4_mem1 >= 64
	c_ab_t4_t4_mem1 += MAS_MEM[1]

	c_ac_t40_in = S.Task('c_ac_t40_in', length=1, delay_cost=1)
	S += c_ac_t40_in >= 64
	c_ac_t40_in += MAS_in[4]

	c_ac_t40_mem0 = S.Task('c_ac_t40_mem0', length=1, delay_cost=1)
	S += c_ac_t40_mem0 >= 64
	c_ac_t40_mem0 += MM_MEM[2]

	c_ac_t40_mem1 = S.Task('c_ac_t40_mem1', length=1, delay_cost=1)
	S += c_ac_t40_mem1 >= 64
	c_ac_t40_mem1 += MM_MEM[3]

	c_paa_t1_t3 = S.Task('c_paa_t1_t3', length=2, delay_cost=1)
	S += c_paa_t1_t3 >= 64
	c_paa_t1_t3 += MAS[0]

	c_pbc_t1_t3_in = S.Task('c_pbc_t1_t3_in', length=1, delay_cost=1)
	S += c_pbc_t1_t3_in >= 64
	c_pbc_t1_t3_in += MAS_in[0]

	c_pbc_t1_t3_mem0 = S.Task('c_pbc_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem0 >= 64
	c_pbc_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t1_t3_mem1 = S.Task('c_pbc_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t1_t3_mem1 >= 64
	c_pbc_t1_t3_mem1 += MAIN_MEM_r[1]

	c_pbc_t4_t3 = S.Task('c_pbc_t4_t3', length=2, delay_cost=1)
	S += c_pbc_t4_t3 >= 64
	c_pbc_t4_t3 += MAS[4]

	c_ab_t4_t4 = S.Task('c_ab_t4_t4', length=11, delay_cost=1)
	S += c_ab_t4_t4 >= 65
	c_ab_t4_t4 += MM[1]

	c_ac_t40 = S.Task('c_ac_t40', length=2, delay_cost=1)
	S += c_ac_t40 >= 65
	c_ac_t40 += MAS[4]

	c_ac_t4_t5_in = S.Task('c_ac_t4_t5_in', length=1, delay_cost=1)
	S += c_ac_t4_t5_in >= 65
	c_ac_t4_t5_in += MAS_in[4]

	c_ac_t4_t5_mem0 = S.Task('c_ac_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem0 >= 65
	c_ac_t4_t5_mem0 += MM_MEM[2]

	c_ac_t4_t5_mem1 = S.Task('c_ac_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ac_t4_t5_mem1 >= 65
	c_ac_t4_t5_mem1 += MM_MEM[3]

	c_bc_t40_in = S.Task('c_bc_t40_in', length=1, delay_cost=1)
	S += c_bc_t40_in >= 65
	c_bc_t40_in += MAS_in[5]

	c_bc_t40_mem0 = S.Task('c_bc_t40_mem0', length=1, delay_cost=1)
	S += c_bc_t40_mem0 >= 65
	c_bc_t40_mem0 += MM_MEM[0]

	c_bc_t40_mem1 = S.Task('c_bc_t40_mem1', length=1, delay_cost=1)
	S += c_bc_t40_mem1 >= 65
	c_bc_t40_mem1 += MM_MEM[1]

	c_paa_t30_in = S.Task('c_paa_t30_in', length=1, delay_cost=1)
	S += c_paa_t30_in >= 65
	c_paa_t30_in += MAS_in[0]

	c_paa_t30_mem0 = S.Task('c_paa_t30_mem0', length=1, delay_cost=1)
	S += c_paa_t30_mem0 >= 65
	c_paa_t30_mem0 += MAIN_MEM_r[0]

	c_paa_t30_mem1 = S.Task('c_paa_t30_mem1', length=1, delay_cost=1)
	S += c_paa_t30_mem1 >= 65
	c_paa_t30_mem1 += MAIN_MEM_r[1]

	c_pbc_t1_t3 = S.Task('c_pbc_t1_t3', length=2, delay_cost=1)
	S += c_pbc_t1_t3 >= 65
	c_pbc_t1_t3 += MAS[0]

	c_ac_t4_t5 = S.Task('c_ac_t4_t5', length=2, delay_cost=1)
	S += c_ac_t4_t5 >= 66
	c_ac_t4_t5 += MAS[4]

	c_bc_t0_t5_in = S.Task('c_bc_t0_t5_in', length=1, delay_cost=1)
	S += c_bc_t0_t5_in >= 66
	c_bc_t0_t5_in += MAS_in[4]

	c_bc_t0_t5_mem0 = S.Task('c_bc_t0_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem0 >= 66
	c_bc_t0_t5_mem0 += MM_MEM[2]

	c_bc_t0_t5_mem1 = S.Task('c_bc_t0_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t0_t5_mem1 >= 66
	c_bc_t0_t5_mem1 += MM_MEM[3]

	c_bc_t40 = S.Task('c_bc_t40', length=2, delay_cost=1)
	S += c_bc_t40 >= 66
	c_bc_t40 += MAS[5]

	c_bc_t4_t5_in = S.Task('c_bc_t4_t5_in', length=1, delay_cost=1)
	S += c_bc_t4_t5_in >= 66
	c_bc_t4_t5_in += MAS_in[3]

	c_bc_t4_t5_mem0 = S.Task('c_bc_t4_t5_mem0', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem0 >= 66
	c_bc_t4_t5_mem0 += MM_MEM[0]

	c_bc_t4_t5_mem1 = S.Task('c_bc_t4_t5_mem1', length=1, delay_cost=1)
	S += c_bc_t4_t5_mem1 >= 66
	c_bc_t4_t5_mem1 += MM_MEM[1]

	c_paa_t30 = S.Task('c_paa_t30', length=2, delay_cost=1)
	S += c_paa_t30 >= 66
	c_paa_t30 += MAS[0]

	c_pcb_t1_t3_in = S.Task('c_pcb_t1_t3_in', length=1, delay_cost=1)
	S += c_pcb_t1_t3_in >= 66
	c_pcb_t1_t3_in += MAS_in[0]

	c_pcb_t1_t3_mem0 = S.Task('c_pcb_t1_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem0 >= 66
	c_pcb_t1_t3_mem0 += MAIN_MEM_r[0]

	c_pcb_t1_t3_mem1 = S.Task('c_pcb_t1_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t1_t3_mem1 >= 66
	c_pcb_t1_t3_mem1 += MAIN_MEM_r[1]

	c_bc_t00_in = S.Task('c_bc_t00_in', length=1, delay_cost=1)
	S += c_bc_t00_in >= 67
	c_bc_t00_in += MAS_in[1]

	c_bc_t00_mem0 = S.Task('c_bc_t00_mem0', length=1, delay_cost=1)
	S += c_bc_t00_mem0 >= 67
	c_bc_t00_mem0 += MM_MEM[2]

	c_bc_t00_mem1 = S.Task('c_bc_t00_mem1', length=1, delay_cost=1)
	S += c_bc_t00_mem1 >= 67
	c_bc_t00_mem1 += MM_MEM[3]

	c_bc_t0_t5 = S.Task('c_bc_t0_t5', length=2, delay_cost=1)
	S += c_bc_t0_t5 >= 67
	c_bc_t0_t5 += MAS[4]

	c_bc_t4_t5 = S.Task('c_bc_t4_t5', length=2, delay_cost=1)
	S += c_bc_t4_t5 >= 67
	c_bc_t4_t5 += MAS[3]

	c_paa_t0_t3_in = S.Task('c_paa_t0_t3_in', length=1, delay_cost=1)
	S += c_paa_t0_t3_in >= 67
	c_paa_t0_t3_in += MAS_in[0]

	c_paa_t0_t3_mem0 = S.Task('c_paa_t0_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem0 >= 67
	c_paa_t0_t3_mem0 += MAIN_MEM_r[0]

	c_paa_t0_t3_mem1 = S.Task('c_paa_t0_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t0_t3_mem1 >= 67
	c_paa_t0_t3_mem1 += MAIN_MEM_r[1]

	c_pcb_t1_t3 = S.Task('c_pcb_t1_t3', length=2, delay_cost=1)
	S += c_pcb_t1_t3 >= 67
	c_pcb_t1_t3 += MAS[0]

	c_ac_t11_in = S.Task('c_ac_t11_in', length=1, delay_cost=1)
	S += c_ac_t11_in >= 68
	c_ac_t11_in += MAS_in[3]

	c_ac_t11_mem0 = S.Task('c_ac_t11_mem0', length=1, delay_cost=1)
	S += c_ac_t11_mem0 >= 68
	c_ac_t11_mem0 += MM_MEM[2]

	c_ac_t11_mem1 = S.Task('c_ac_t11_mem1', length=1, delay_cost=1)
	S += c_ac_t11_mem1 >= 68
	c_ac_t11_mem1 += MAS_MEM[1]

	c_bc_t00 = S.Task('c_bc_t00', length=2, delay_cost=1)
	S += c_bc_t00 >= 68
	c_bc_t00 += MAS[1]

	c_bc_t01_in = S.Task('c_bc_t01_in', length=1, delay_cost=1)
	S += c_bc_t01_in >= 68
	c_bc_t01_in += MAS_in[4]

	c_bc_t01_mem0 = S.Task('c_bc_t01_mem0', length=1, delay_cost=1)
	S += c_bc_t01_mem0 >= 68
	c_bc_t01_mem0 += MM_MEM[0]

	c_bc_t01_mem1 = S.Task('c_bc_t01_mem1', length=1, delay_cost=1)
	S += c_bc_t01_mem1 >= 68
	c_bc_t01_mem1 += MAS_MEM[9]

	c_paa_t0_t3 = S.Task('c_paa_t0_t3', length=2, delay_cost=1)
	S += c_paa_t0_t3 >= 68
	c_paa_t0_t3 += MAS[0]

	c_paa_t31_in = S.Task('c_paa_t31_in', length=1, delay_cost=1)
	S += c_paa_t31_in >= 68
	c_paa_t31_in += MAS_in[0]

	c_paa_t31_mem0 = S.Task('c_paa_t31_mem0', length=1, delay_cost=1)
	S += c_paa_t31_mem0 >= 68
	c_paa_t31_mem0 += MAIN_MEM_r[0]

	c_paa_t31_mem1 = S.Task('c_paa_t31_mem1', length=1, delay_cost=1)
	S += c_paa_t31_mem1 >= 68
	c_paa_t31_mem1 += MAIN_MEM_r[1]

	c_ab_t11_in = S.Task('c_ab_t11_in', length=1, delay_cost=1)
	S += c_ab_t11_in >= 69
	c_ab_t11_in += MAS_in[5]

	c_ab_t11_mem0 = S.Task('c_ab_t11_mem0', length=1, delay_cost=1)
	S += c_ab_t11_mem0 >= 69
	c_ab_t11_mem0 += MM_MEM[2]

	c_ab_t11_mem1 = S.Task('c_ab_t11_mem1', length=1, delay_cost=1)
	S += c_ab_t11_mem1 >= 69
	c_ab_t11_mem1 += MAS_MEM[11]

	c_ac_t11 = S.Task('c_ac_t11', length=2, delay_cost=1)
	S += c_ac_t11 >= 69
	c_ac_t11 += MAS[3]

	c_bc_t01 = S.Task('c_bc_t01', length=2, delay_cost=1)
	S += c_bc_t01 >= 69
	c_bc_t01 += MAS[4]

	c_bc_t50_in = S.Task('c_bc_t50_in', length=1, delay_cost=1)
	S += c_bc_t50_in >= 69
	c_bc_t50_in += MAS_in[3]

	c_bc_t50_mem0 = S.Task('c_bc_t50_mem0', length=1, delay_cost=1)
	S += c_bc_t50_mem0 >= 69
	c_bc_t50_mem0 += MAS_MEM[2]

	c_bc_t50_mem1 = S.Task('c_bc_t50_mem1', length=1, delay_cost=1)
	S += c_bc_t50_mem1 >= 69
	c_bc_t50_mem1 += MAS_MEM[1]

	c_paa_t31 = S.Task('c_paa_t31', length=2, delay_cost=1)
	S += c_paa_t31 >= 69
	c_paa_t31 += MAS[0]

	c_pbc_t0_t3_in = S.Task('c_pbc_t0_t3_in', length=1, delay_cost=1)
	S += c_pbc_t0_t3_in >= 69
	c_pbc_t0_t3_in += MAS_in[4]

	c_pbc_t0_t3_mem0 = S.Task('c_pbc_t0_t3_mem0', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem0 >= 69
	c_pbc_t0_t3_mem0 += MAIN_MEM_r[0]

	c_pbc_t0_t3_mem1 = S.Task('c_pbc_t0_t3_mem1', length=1, delay_cost=1)
	S += c_pbc_t0_t3_mem1 >= 69
	c_pbc_t0_t3_mem1 += MAIN_MEM_r[1]

	c_ab_t11 = S.Task('c_ab_t11', length=2, delay_cost=1)
	S += c_ab_t11 >= 70
	c_ab_t11 += MAS[5]

	c_bc_t50 = S.Task('c_bc_t50', length=2, delay_cost=1)
	S += c_bc_t50 >= 70
	c_bc_t50 += MAS[3]

	c_paa_t4_t3_in = S.Task('c_paa_t4_t3_in', length=1, delay_cost=1)
	S += c_paa_t4_t3_in >= 70
	c_paa_t4_t3_in += MAS_in[4]

	c_paa_t4_t3_mem0 = S.Task('c_paa_t4_t3_mem0', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem0 >= 70
	c_paa_t4_t3_mem0 += MAS_MEM[0]

	c_paa_t4_t3_mem1 = S.Task('c_paa_t4_t3_mem1', length=1, delay_cost=1)
	S += c_paa_t4_t3_mem1 >= 70
	c_paa_t4_t3_mem1 += MAS_MEM[1]

	c_pbc_t0_t3 = S.Task('c_pbc_t0_t3', length=2, delay_cost=1)
	S += c_pbc_t0_t3 >= 70
	c_pbc_t0_t3 += MAS[4]

	c_pcb_t30_in = S.Task('c_pcb_t30_in', length=1, delay_cost=1)
	S += c_pcb_t30_in >= 70
	c_pcb_t30_in += MAS_in[3]

	c_pcb_t30_mem0 = S.Task('c_pcb_t30_mem0', length=1, delay_cost=1)
	S += c_pcb_t30_mem0 >= 70
	c_pcb_t30_mem0 += MAIN_MEM_r[0]

	c_pcb_t30_mem1 = S.Task('c_pcb_t30_mem1', length=1, delay_cost=1)
	S += c_pcb_t30_mem1 >= 70
	c_pcb_t30_mem1 += MAIN_MEM_r[1]

	c_paa_t4_t3 = S.Task('c_paa_t4_t3', length=2, delay_cost=1)
	S += c_paa_t4_t3 >= 71
	c_paa_t4_t3 += MAS[4]

	c_pcb_t30 = S.Task('c_pcb_t30', length=2, delay_cost=1)
	S += c_pcb_t30 >= 71
	c_pcb_t30 += MAS[3]

	c_pcb_t31_in = S.Task('c_pcb_t31_in', length=1, delay_cost=1)
	S += c_pcb_t31_in >= 71
	c_pcb_t31_in += MAS_in[4]

	c_pcb_t31_mem0 = S.Task('c_pcb_t31_mem0', length=1, delay_cost=1)
	S += c_pcb_t31_mem0 >= 71
	c_pcb_t31_mem0 += MAIN_MEM_r[0]

	c_pcb_t31_mem1 = S.Task('c_pcb_t31_mem1', length=1, delay_cost=1)
	S += c_pcb_t31_mem1 >= 71
	c_pcb_t31_mem1 += MAIN_MEM_r[1]

	c_aa_t00_in = S.Task('c_aa_t00_in', length=1, delay_cost=1)
	S += c_aa_t00_in >= 72
	c_aa_t00_in += MAS_in[4]

	c_aa_t00_mem0 = S.Task('c_aa_t00_mem0', length=1, delay_cost=1)
	S += c_aa_t00_mem0 >= 72
	c_aa_t00_mem0 += MAIN_MEM_r[0]

	c_aa_t00_mem1 = S.Task('c_aa_t00_mem1', length=1, delay_cost=1)
	S += c_aa_t00_mem1 >= 72
	c_aa_t00_mem1 += MAS_MEM[11]

	c_ab_t40_in = S.Task('c_ab_t40_in', length=1, delay_cost=1)
	S += c_ab_t40_in >= 72
	c_ab_t40_in += MAS_in[3]

	c_ab_t40_mem0 = S.Task('c_ab_t40_mem0', length=1, delay_cost=1)
	S += c_ab_t40_mem0 >= 72
	c_ab_t40_mem0 += MM_MEM[0]

	c_ab_t40_mem1 = S.Task('c_ab_t40_mem1', length=1, delay_cost=1)
	S += c_ab_t40_mem1 >= 72
	c_ab_t40_mem1 += MM_MEM[3]

	c_pcb_t31 = S.Task('c_pcb_t31', length=2, delay_cost=1)
	S += c_pcb_t31 >= 72
	c_pcb_t31 += MAS[4]

	c_aa_t00 = S.Task('c_aa_t00', length=2, delay_cost=1)
	S += c_aa_t00 >= 73
	c_aa_t00 += MAS[4]

	c_ab_t40 = S.Task('c_ab_t40', length=2, delay_cost=1)
	S += c_ab_t40 >= 73
	c_ab_t40 += MAS[3]

	c_ab_t4_t5_in = S.Task('c_ab_t4_t5_in', length=1, delay_cost=1)
	S += c_ab_t4_t5_in >= 73
	c_ab_t4_t5_in += MAS_in[0]

	c_ab_t4_t5_mem0 = S.Task('c_ab_t4_t5_mem0', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem0 >= 73
	c_ab_t4_t5_mem0 += MM_MEM[0]

	c_ab_t4_t5_mem1 = S.Task('c_ab_t4_t5_mem1', length=1, delay_cost=1)
	S += c_ab_t4_t5_mem1 >= 73
	c_ab_t4_t5_mem1 += MM_MEM[3]

	c_bb_t01_in = S.Task('c_bb_t01_in', length=1, delay_cost=1)
	S += c_bb_t01_in >= 73
	c_bb_t01_in += MAS_in[3]

	c_bb_t01_mem0 = S.Task('c_bb_t01_mem0', length=1, delay_cost=1)
	S += c_bb_t01_mem0 >= 73
	c_bb_t01_mem0 += MAIN_MEM_r[0]

	c_bb_t01_mem1 = S.Task('c_bb_t01_mem1', length=1, delay_cost=1)
	S += c_bb_t01_mem1 >= 73
	c_bb_t01_mem1 += MAS_MEM[11]

	c_pcb_t4_t3_in = S.Task('c_pcb_t4_t3_in', length=1, delay_cost=1)
	S += c_pcb_t4_t3_in >= 73
	c_pcb_t4_t3_in += MAS_in[4]

	c_pcb_t4_t3_mem0 = S.Task('c_pcb_t4_t3_mem0', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem0 >= 73
	c_pcb_t4_t3_mem0 += MAS_MEM[6]

	c_pcb_t4_t3_mem1 = S.Task('c_pcb_t4_t3_mem1', length=1, delay_cost=1)
	S += c_pcb_t4_t3_mem1 >= 73
	c_pcb_t4_t3_mem1 += MAS_MEM[9]

	c_aa_t2_t0_in = S.Task('c_aa_t2_t0_in', length=1, delay_cost=1)
	S += c_aa_t2_t0_in >= 74
	c_aa_t2_t0_in += MM_in[1]

	c_aa_t2_t0_mem0 = S.Task('c_aa_t2_t0_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem0 >= 74
	c_aa_t2_t0_mem0 += MAS_MEM[8]

	c_aa_t2_t0_mem1 = S.Task('c_aa_t2_t0_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t0_mem1 >= 74
	c_aa_t2_t0_mem1 += MAS_MEM[11]

	c_ab_t4_t5 = S.Task('c_ab_t4_t5', length=2, delay_cost=1)
	S += c_ab_t4_t5 >= 74
	c_ab_t4_t5 += MAS[0]

	c_bb_t01 = S.Task('c_bb_t01', length=2, delay_cost=1)
	S += c_bb_t01 >= 74
	c_bb_t01 += MAS[3]

	c_cc_t01_in = S.Task('c_cc_t01_in', length=1, delay_cost=1)
	S += c_cc_t01_in >= 74
	c_cc_t01_in += MAS_in[4]

	c_cc_t01_mem0 = S.Task('c_cc_t01_mem0', length=1, delay_cost=1)
	S += c_cc_t01_mem0 >= 74
	c_cc_t01_mem0 += MAIN_MEM_r[0]

	c_cc_t01_mem1 = S.Task('c_cc_t01_mem1', length=1, delay_cost=1)
	S += c_cc_t01_mem1 >= 74
	c_cc_t01_mem1 += MAS_MEM[3]

	c_pcb_t4_t3 = S.Task('c_pcb_t4_t3', length=2, delay_cost=1)
	S += c_pcb_t4_t3 >= 74
	c_pcb_t4_t3 += MAS[4]

	c_aa_t2_t0 = S.Task('c_aa_t2_t0', length=11, delay_cost=1)
	S += c_aa_t2_t0 >= 75
	c_aa_t2_t0 += MM[1]

	c_cc_t00_in = S.Task('c_cc_t00_in', length=1, delay_cost=1)
	S += c_cc_t00_in >= 75
	c_cc_t00_in += MAS_in[1]

	c_cc_t00_mem0 = S.Task('c_cc_t00_mem0', length=1, delay_cost=1)
	S += c_cc_t00_mem0 >= 75
	c_cc_t00_mem0 += MAIN_MEM_r[0]

	c_cc_t00_mem1 = S.Task('c_cc_t00_mem1', length=1, delay_cost=1)
	S += c_cc_t00_mem1 >= 75
	c_cc_t00_mem1 += MAS_MEM[9]

	c_cc_t01 = S.Task('c_cc_t01', length=2, delay_cost=1)
	S += c_cc_t01 >= 75
	c_cc_t01 += MAS[4]

	c_aa_t01_in = S.Task('c_aa_t01_in', length=1, delay_cost=1)
	S += c_aa_t01_in >= 76
	c_aa_t01_in += MAS_in[2]

	c_aa_t01_mem0 = S.Task('c_aa_t01_mem0', length=1, delay_cost=1)
	S += c_aa_t01_mem0 >= 76
	c_aa_t01_mem0 += MAIN_MEM_r[0]

	c_aa_t01_mem1 = S.Task('c_aa_t01_mem1', length=1, delay_cost=1)
	S += c_aa_t01_mem1 >= 76
	c_aa_t01_mem1 += MAS_MEM[1]

	c_cc_t00 = S.Task('c_cc_t00', length=2, delay_cost=1)
	S += c_cc_t00 >= 76
	c_cc_t00 += MAS[1]

	c_cc_t2_t1_in = S.Task('c_cc_t2_t1_in', length=1, delay_cost=1)
	S += c_cc_t2_t1_in >= 76
	c_cc_t2_t1_in += MM_in[1]

	c_cc_t2_t1_mem0 = S.Task('c_cc_t2_t1_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem0 >= 76
	c_cc_t2_t1_mem0 += MAS_MEM[8]

	c_cc_t2_t1_mem1 = S.Task('c_cc_t2_t1_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t1_mem1 >= 76
	c_cc_t2_t1_mem1 += MAS_MEM[9]

	c_aa_t01 = S.Task('c_aa_t01', length=2, delay_cost=1)
	S += c_aa_t01 >= 77
	c_aa_t01 += MAS[2]

	c_bb_t00_in = S.Task('c_bb_t00_in', length=1, delay_cost=1)
	S += c_bb_t00_in >= 77
	c_bb_t00_in += MAS_in[4]

	c_bb_t00_mem0 = S.Task('c_bb_t00_mem0', length=1, delay_cost=1)
	S += c_bb_t00_mem0 >= 77
	c_bb_t00_mem0 += MAIN_MEM_r[0]

	c_bb_t00_mem1 = S.Task('c_bb_t00_mem1', length=1, delay_cost=1)
	S += c_bb_t00_mem1 >= 77
	c_bb_t00_mem1 += MAS_MEM[11]

	c_cc_t2_t0_in = S.Task('c_cc_t2_t0_in', length=1, delay_cost=1)
	S += c_cc_t2_t0_in >= 77
	c_cc_t2_t0_in += MM_in[1]

	c_cc_t2_t0_mem0 = S.Task('c_cc_t2_t0_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem0 >= 77
	c_cc_t2_t0_mem0 += MAS_MEM[2]

	c_cc_t2_t0_mem1 = S.Task('c_cc_t2_t0_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t0_mem1 >= 77
	c_cc_t2_t0_mem1 += MAS_MEM[9]

	c_cc_t2_t1 = S.Task('c_cc_t2_t1', length=11, delay_cost=1)
	S += c_cc_t2_t1 >= 77
	c_cc_t2_t1 += MM[1]

	c_aa_t2_t1_in = S.Task('c_aa_t2_t1_in', length=1, delay_cost=1)
	S += c_aa_t2_t1_in >= 78
	c_aa_t2_t1_in += MM_in[1]

	c_aa_t2_t1_mem0 = S.Task('c_aa_t2_t1_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem0 >= 78
	c_aa_t2_t1_mem0 += MAS_MEM[4]

	c_aa_t2_t1_mem1 = S.Task('c_aa_t2_t1_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t1_mem1 >= 78
	c_aa_t2_t1_mem1 += MAS_MEM[11]

	c_aa_t2_t2_in = S.Task('c_aa_t2_t2_in', length=1, delay_cost=1)
	S += c_aa_t2_t2_in >= 78
	c_aa_t2_t2_in += MAS_in[2]

	c_aa_t2_t2_mem0 = S.Task('c_aa_t2_t2_mem0', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem0 >= 78
	c_aa_t2_t2_mem0 += MAS_MEM[8]

	c_aa_t2_t2_mem1 = S.Task('c_aa_t2_t2_mem1', length=1, delay_cost=1)
	S += c_aa_t2_t2_mem1 >= 78
	c_aa_t2_t2_mem1 += MAS_MEM[5]

	c_bb_t00 = S.Task('c_bb_t00', length=2, delay_cost=1)
	S += c_bb_t00 >= 78
	c_bb_t00 += MAS[4]

	c_cc_t2_t0 = S.Task('c_cc_t2_t0', length=11, delay_cost=1)
	S += c_cc_t2_t0 >= 78
	c_cc_t2_t0 += MM[1]

	c_cc_t2_t2_in = S.Task('c_cc_t2_t2_in', length=1, delay_cost=1)
	S += c_cc_t2_t2_in >= 78
	c_cc_t2_t2_in += MAS_in[4]

	c_cc_t2_t2_mem0 = S.Task('c_cc_t2_t2_mem0', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem0 >= 78
	c_cc_t2_t2_mem0 += MAS_MEM[2]

	c_cc_t2_t2_mem1 = S.Task('c_cc_t2_t2_mem1', length=1, delay_cost=1)
	S += c_cc_t2_t2_mem1 >= 78
	c_cc_t2_t2_mem1 += MAS_MEM[9]

	c_aa_t2_t1 = S.Task('c_aa_t2_t1', length=11, delay_cost=1)
	S += c_aa_t2_t1 >= 79
	c_aa_t2_t1 += MM[1]

	c_aa_t2_t2 = S.Task('c_aa_t2_t2', length=2, delay_cost=1)
	S += c_aa_t2_t2 >= 79
	c_aa_t2_t2 += MAS[2]

	c_bb_t2_t0_in = S.Task('c_bb_t2_t0_in', length=1, delay_cost=1)
	S += c_bb_t2_t0_in >= 79
	c_bb_t2_t0_in += MM_in[1]

	c_bb_t2_t0_mem0 = S.Task('c_bb_t2_t0_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem0 >= 79
	c_bb_t2_t0_mem0 += MAS_MEM[8]

	c_bb_t2_t0_mem1 = S.Task('c_bb_t2_t0_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t0_mem1 >= 79
	c_bb_t2_t0_mem1 += MAS_MEM[11]

	c_bb_t2_t1_in = S.Task('c_bb_t2_t1_in', length=1, delay_cost=1)
	S += c_bb_t2_t1_in >= 79
	c_bb_t2_t1_in += MM_in[0]

	c_bb_t2_t1_mem0 = S.Task('c_bb_t2_t1_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem0 >= 79
	c_bb_t2_t1_mem0 += MAS_MEM[6]

	c_bb_t2_t1_mem1 = S.Task('c_bb_t2_t1_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t1_mem1 >= 79
	c_bb_t2_t1_mem1 += MAS_MEM[9]

	c_cc_t2_t2 = S.Task('c_cc_t2_t2', length=2, delay_cost=1)
	S += c_cc_t2_t2 >= 79
	c_cc_t2_t2 += MAS[4]

	c_bb_t2_t0 = S.Task('c_bb_t2_t0', length=11, delay_cost=1)
	S += c_bb_t2_t0 >= 80
	c_bb_t2_t0 += MM[1]

	c_bb_t2_t1 = S.Task('c_bb_t2_t1', length=11, delay_cost=1)
	S += c_bb_t2_t1 >= 80
	c_bb_t2_t1 += MM[0]

	c_bb_t2_t2_in = S.Task('c_bb_t2_t2_in', length=1, delay_cost=1)
	S += c_bb_t2_t2_in >= 80
	c_bb_t2_t2_in += MAS_in[2]

	c_bb_t2_t2_mem0 = S.Task('c_bb_t2_t2_mem0', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem0 >= 80
	c_bb_t2_t2_mem0 += MAS_MEM[8]

	c_bb_t2_t2_mem1 = S.Task('c_bb_t2_t2_mem1', length=1, delay_cost=1)
	S += c_bb_t2_t2_mem1 >= 80
	c_bb_t2_t2_mem1 += MAS_MEM[7]

	c_bb_t2_t2 = S.Task('c_bb_t2_t2', length=2, delay_cost=1)
	S += c_bb_t2_t2 >= 81
	c_bb_t2_t2 += MAS[2]


	# new tasks
	c_aa_t2_t4 = S.Task('c_aa_t2_t4', length=11, delay_cost=1)
	c_aa_t2_t4 += alt(MM)
	c_aa_t2_t4_in = S.Task('c_aa_t2_t4_in', length=1, delay_cost=1)
	c_aa_t2_t4_in += alt(MM_in)
	S += c_aa_t2_t4_in*MM_in[0]<=c_aa_t2_t4*MM[0]
	S += c_aa_t2_t4_in*MM_in[1]<=c_aa_t2_t4*MM[1]
	c_aa_t2_t4_mem0 = S.Task('c_aa_t2_t4_mem0', length=1, delay_cost=1)
	c_aa_t2_t4_mem0 += MAS_MEM[4]
	S += 80 < c_aa_t2_t4_mem0
	S += c_aa_t2_t4_mem0 <= c_aa_t2_t4

	c_aa_t2_t4_mem1 = S.Task('c_aa_t2_t4_mem1', length=1, delay_cost=1)
	c_aa_t2_t4_mem1 += MAS_MEM[9]
	S += 33 < c_aa_t2_t4_mem1
	S += c_aa_t2_t4_mem1 <= c_aa_t2_t4

	c_aa_t20 = S.Task('c_aa_t20', length=2, delay_cost=1)
	c_aa_t20 += alt(MAS)
	c_aa_t20_in = S.Task('c_aa_t20_in', length=1, delay_cost=1)
	c_aa_t20_in += alt(MAS_in)
	S += c_aa_t20_in*MAS_in[0]<=c_aa_t20*MAS[0]

	S += c_aa_t20_in*MAS_in[1]<=c_aa_t20*MAS[1]

	S += c_aa_t20_in*MAS_in[2]<=c_aa_t20*MAS[2]

	S += c_aa_t20_in*MAS_in[3]<=c_aa_t20*MAS[3]

	S += c_aa_t20_in*MAS_in[4]<=c_aa_t20*MAS[4]

	S += c_aa_t20_in*MAS_in[5]<=c_aa_t20*MAS[5]

	c_aa_t20_mem0 = S.Task('c_aa_t20_mem0', length=1, delay_cost=1)
	c_aa_t20_mem0 += MM_MEM[2]
	S += 85 < c_aa_t20_mem0
	S += c_aa_t20_mem0 <= c_aa_t20

	c_aa_t20_mem1 = S.Task('c_aa_t20_mem1', length=1, delay_cost=1)
	c_aa_t20_mem1 += MM_MEM[3]
	S += 89 < c_aa_t20_mem1
	S += c_aa_t20_mem1 <= c_aa_t20

	c_aa_t2_t5 = S.Task('c_aa_t2_t5', length=2, delay_cost=1)
	c_aa_t2_t5 += alt(MAS)
	c_aa_t2_t5_in = S.Task('c_aa_t2_t5_in', length=1, delay_cost=1)
	c_aa_t2_t5_in += alt(MAS_in)
	S += c_aa_t2_t5_in*MAS_in[0]<=c_aa_t2_t5*MAS[0]

	S += c_aa_t2_t5_in*MAS_in[1]<=c_aa_t2_t5*MAS[1]

	S += c_aa_t2_t5_in*MAS_in[2]<=c_aa_t2_t5*MAS[2]

	S += c_aa_t2_t5_in*MAS_in[3]<=c_aa_t2_t5*MAS[3]

	S += c_aa_t2_t5_in*MAS_in[4]<=c_aa_t2_t5*MAS[4]

	S += c_aa_t2_t5_in*MAS_in[5]<=c_aa_t2_t5*MAS[5]

	c_aa_t2_t5_mem0 = S.Task('c_aa_t2_t5_mem0', length=1, delay_cost=1)
	c_aa_t2_t5_mem0 += MM_MEM[2]
	S += 85 < c_aa_t2_t5_mem0
	S += c_aa_t2_t5_mem0 <= c_aa_t2_t5

	c_aa_t2_t5_mem1 = S.Task('c_aa_t2_t5_mem1', length=1, delay_cost=1)
	c_aa_t2_t5_mem1 += MM_MEM[3]
	S += 89 < c_aa_t2_t5_mem1
	S += c_aa_t2_t5_mem1 <= c_aa_t2_t5

	c_aa_t40 = S.Task('c_aa_t40', length=2, delay_cost=1)
	c_aa_t40 += alt(MAS)
	c_aa_t40_in = S.Task('c_aa_t40_in', length=1, delay_cost=1)
	c_aa_t40_in += alt(MAS_in)
	S += c_aa_t40_in*MAS_in[0]<=c_aa_t40*MAS[0]

	S += c_aa_t40_in*MAS_in[1]<=c_aa_t40*MAS[1]

	S += c_aa_t40_in*MAS_in[2]<=c_aa_t40*MAS[2]

	S += c_aa_t40_in*MAS_in[3]<=c_aa_t40*MAS[3]

	S += c_aa_t40_in*MAS_in[4]<=c_aa_t40*MAS[4]

	S += c_aa_t40_in*MAS_in[5]<=c_aa_t40*MAS[5]

	c_aa_t40_mem0 = S.Task('c_aa_t40_mem0', length=1, delay_cost=1)
	c_aa_t40_mem0 += MAS_MEM[8]
	S += 35 < c_aa_t40_mem0
	S += c_aa_t40_mem0 <= c_aa_t40

	c_aa_t40_mem1 = S.Task('c_aa_t40_mem1', length=1, delay_cost=1)
	c_aa_t40_mem1 += MAS_MEM[5]
	S += 42 < c_aa_t40_mem1
	S += c_aa_t40_mem1 <= c_aa_t40

	c_aa_t41 = S.Task('c_aa_t41', length=2, delay_cost=1)
	c_aa_t41 += alt(MAS)
	c_aa_t41_in = S.Task('c_aa_t41_in', length=1, delay_cost=1)
	c_aa_t41_in += alt(MAS_in)
	S += c_aa_t41_in*MAS_in[0]<=c_aa_t41*MAS[0]

	S += c_aa_t41_in*MAS_in[1]<=c_aa_t41*MAS[1]

	S += c_aa_t41_in*MAS_in[2]<=c_aa_t41*MAS[2]

	S += c_aa_t41_in*MAS_in[3]<=c_aa_t41*MAS[3]

	S += c_aa_t41_in*MAS_in[4]<=c_aa_t41*MAS[4]

	S += c_aa_t41_in*MAS_in[5]<=c_aa_t41*MAS[5]

	c_aa_t41_mem0 = S.Task('c_aa_t41_mem0', length=1, delay_cost=1)
	c_aa_t41_mem0 += MAS_MEM[4]
	S += 42 < c_aa_t41_mem0
	S += c_aa_t41_mem0 <= c_aa_t41

	c_aa_t41_mem1 = S.Task('c_aa_t41_mem1', length=1, delay_cost=1)
	c_aa_t41_mem1 += MAS_MEM[9]
	S += 35 < c_aa_t41_mem1
	S += c_aa_t41_mem1 <= c_aa_t41

	c_aa11 = S.Task('c_aa11', length=2, delay_cost=1)
	c_aa11 += alt(MAS)
	c_aa11_in = S.Task('c_aa11_in', length=1, delay_cost=1)
	c_aa11_in += alt(MAS_in)
	S += c_aa11_in*MAS_in[0]<=c_aa11*MAS[0]

	S += c_aa11_in*MAS_in[1]<=c_aa11*MAS[1]

	S += c_aa11_in*MAS_in[2]<=c_aa11*MAS[2]

	S += c_aa11_in*MAS_in[3]<=c_aa11*MAS[3]

	S += c_aa11_in*MAS_in[4]<=c_aa11*MAS[4]

	S += c_aa11_in*MAS_in[5]<=c_aa11*MAS[5]

	c_aa11_mem0 = S.Task('c_aa11_mem0', length=1, delay_cost=1)
	c_aa11_mem0 += MAS_MEM[4]
	S += 42 < c_aa11_mem0
	S += c_aa11_mem0 <= c_aa11

	c_aa11_mem1 = S.Task('c_aa11_mem1', length=1, delay_cost=1)
	c_aa11_mem1 += MAS_MEM[5]
	S += 42 < c_aa11_mem1
	S += c_aa11_mem1 <= c_aa11

	c_bb_t2_t4 = S.Task('c_bb_t2_t4', length=11, delay_cost=1)
	c_bb_t2_t4 += alt(MM)
	c_bb_t2_t4_in = S.Task('c_bb_t2_t4_in', length=1, delay_cost=1)
	c_bb_t2_t4_in += alt(MM_in)
	S += c_bb_t2_t4_in*MM_in[0]<=c_bb_t2_t4*MM[0]
	S += c_bb_t2_t4_in*MM_in[1]<=c_bb_t2_t4*MM[1]
	c_bb_t2_t4_mem0 = S.Task('c_bb_t2_t4_mem0', length=1, delay_cost=1)
	c_bb_t2_t4_mem0 += MAS_MEM[4]
	S += 82 < c_bb_t2_t4_mem0
	S += c_bb_t2_t4_mem0 <= c_bb_t2_t4

	c_bb_t2_t4_mem1 = S.Task('c_bb_t2_t4_mem1', length=1, delay_cost=1)
	c_bb_t2_t4_mem1 += MAS_MEM[9]
	S += 26 < c_bb_t2_t4_mem1
	S += c_bb_t2_t4_mem1 <= c_bb_t2_t4

	c_bb_t20 = S.Task('c_bb_t20', length=2, delay_cost=1)
	c_bb_t20 += alt(MAS)
	c_bb_t20_in = S.Task('c_bb_t20_in', length=1, delay_cost=1)
	c_bb_t20_in += alt(MAS_in)
	S += c_bb_t20_in*MAS_in[0]<=c_bb_t20*MAS[0]

	S += c_bb_t20_in*MAS_in[1]<=c_bb_t20*MAS[1]

	S += c_bb_t20_in*MAS_in[2]<=c_bb_t20*MAS[2]

	S += c_bb_t20_in*MAS_in[3]<=c_bb_t20*MAS[3]

	S += c_bb_t20_in*MAS_in[4]<=c_bb_t20*MAS[4]

	S += c_bb_t20_in*MAS_in[5]<=c_bb_t20*MAS[5]

	c_bb_t20_mem0 = S.Task('c_bb_t20_mem0', length=1, delay_cost=1)
	c_bb_t20_mem0 += MM_MEM[2]
	S += 90 < c_bb_t20_mem0
	S += c_bb_t20_mem0 <= c_bb_t20

	c_bb_t20_mem1 = S.Task('c_bb_t20_mem1', length=1, delay_cost=1)
	c_bb_t20_mem1 += MM_MEM[1]
	S += 90 < c_bb_t20_mem1
	S += c_bb_t20_mem1 <= c_bb_t20

	c_bb_t2_t5 = S.Task('c_bb_t2_t5', length=2, delay_cost=1)
	c_bb_t2_t5 += alt(MAS)
	c_bb_t2_t5_in = S.Task('c_bb_t2_t5_in', length=1, delay_cost=1)
	c_bb_t2_t5_in += alt(MAS_in)
	S += c_bb_t2_t5_in*MAS_in[0]<=c_bb_t2_t5*MAS[0]

	S += c_bb_t2_t5_in*MAS_in[1]<=c_bb_t2_t5*MAS[1]

	S += c_bb_t2_t5_in*MAS_in[2]<=c_bb_t2_t5*MAS[2]

	S += c_bb_t2_t5_in*MAS_in[3]<=c_bb_t2_t5*MAS[3]

	S += c_bb_t2_t5_in*MAS_in[4]<=c_bb_t2_t5*MAS[4]

	S += c_bb_t2_t5_in*MAS_in[5]<=c_bb_t2_t5*MAS[5]

	c_bb_t2_t5_mem0 = S.Task('c_bb_t2_t5_mem0', length=1, delay_cost=1)
	c_bb_t2_t5_mem0 += MM_MEM[2]
	S += 90 < c_bb_t2_t5_mem0
	S += c_bb_t2_t5_mem0 <= c_bb_t2_t5

	c_bb_t2_t5_mem1 = S.Task('c_bb_t2_t5_mem1', length=1, delay_cost=1)
	c_bb_t2_t5_mem1 += MM_MEM[1]
	S += 90 < c_bb_t2_t5_mem1
	S += c_bb_t2_t5_mem1 <= c_bb_t2_t5

	c_bb_t40 = S.Task('c_bb_t40', length=2, delay_cost=1)
	c_bb_t40 += alt(MAS)
	c_bb_t40_in = S.Task('c_bb_t40_in', length=1, delay_cost=1)
	c_bb_t40_in += alt(MAS_in)
	S += c_bb_t40_in*MAS_in[0]<=c_bb_t40*MAS[0]

	S += c_bb_t40_in*MAS_in[1]<=c_bb_t40*MAS[1]

	S += c_bb_t40_in*MAS_in[2]<=c_bb_t40*MAS[2]

	S += c_bb_t40_in*MAS_in[3]<=c_bb_t40*MAS[3]

	S += c_bb_t40_in*MAS_in[4]<=c_bb_t40*MAS[4]

	S += c_bb_t40_in*MAS_in[5]<=c_bb_t40*MAS[5]

	c_bb_t40_mem0 = S.Task('c_bb_t40_mem0', length=1, delay_cost=1)
	c_bb_t40_mem0 += MAS_MEM[10]
	S += 34 < c_bb_t40_mem0
	S += c_bb_t40_mem0 <= c_bb_t40

	c_bb_t40_mem1 = S.Task('c_bb_t40_mem1', length=1, delay_cost=1)
	c_bb_t40_mem1 += MAS_MEM[9]
	S += 39 < c_bb_t40_mem1
	S += c_bb_t40_mem1 <= c_bb_t40

	c_bb_t41 = S.Task('c_bb_t41', length=2, delay_cost=1)
	c_bb_t41 += alt(MAS)
	c_bb_t41_in = S.Task('c_bb_t41_in', length=1, delay_cost=1)
	c_bb_t41_in += alt(MAS_in)
	S += c_bb_t41_in*MAS_in[0]<=c_bb_t41*MAS[0]

	S += c_bb_t41_in*MAS_in[1]<=c_bb_t41*MAS[1]

	S += c_bb_t41_in*MAS_in[2]<=c_bb_t41*MAS[2]

	S += c_bb_t41_in*MAS_in[3]<=c_bb_t41*MAS[3]

	S += c_bb_t41_in*MAS_in[4]<=c_bb_t41*MAS[4]

	S += c_bb_t41_in*MAS_in[5]<=c_bb_t41*MAS[5]

	c_bb_t41_mem0 = S.Task('c_bb_t41_mem0', length=1, delay_cost=1)
	c_bb_t41_mem0 += MAS_MEM[8]
	S += 39 < c_bb_t41_mem0
	S += c_bb_t41_mem0 <= c_bb_t41

	c_bb_t41_mem1 = S.Task('c_bb_t41_mem1', length=1, delay_cost=1)
	c_bb_t41_mem1 += MAS_MEM[11]
	S += 34 < c_bb_t41_mem1
	S += c_bb_t41_mem1 <= c_bb_t41

	c_bb11 = S.Task('c_bb11', length=2, delay_cost=1)
	c_bb11 += alt(MAS)
	c_bb11_in = S.Task('c_bb11_in', length=1, delay_cost=1)
	c_bb11_in += alt(MAS_in)
	S += c_bb11_in*MAS_in[0]<=c_bb11*MAS[0]

	S += c_bb11_in*MAS_in[1]<=c_bb11*MAS[1]

	S += c_bb11_in*MAS_in[2]<=c_bb11*MAS[2]

	S += c_bb11_in*MAS_in[3]<=c_bb11*MAS[3]

	S += c_bb11_in*MAS_in[4]<=c_bb11*MAS[4]

	S += c_bb11_in*MAS_in[5]<=c_bb11*MAS[5]

	c_bb11_mem0 = S.Task('c_bb11_mem0', length=1, delay_cost=1)
	c_bb11_mem0 += MAS_MEM[8]
	S += 39 < c_bb11_mem0
	S += c_bb11_mem0 <= c_bb11

	c_bb11_mem1 = S.Task('c_bb11_mem1', length=1, delay_cost=1)
	c_bb11_mem1 += MAS_MEM[9]
	S += 39 < c_bb11_mem1
	S += c_bb11_mem1 <= c_bb11

	c_cc_t2_t4 = S.Task('c_cc_t2_t4', length=11, delay_cost=1)
	c_cc_t2_t4 += alt(MM)
	c_cc_t2_t4_in = S.Task('c_cc_t2_t4_in', length=1, delay_cost=1)
	c_cc_t2_t4_in += alt(MM_in)
	S += c_cc_t2_t4_in*MM_in[0]<=c_cc_t2_t4*MM[0]
	S += c_cc_t2_t4_in*MM_in[1]<=c_cc_t2_t4*MM[1]
	c_cc_t2_t4_mem0 = S.Task('c_cc_t2_t4_mem0', length=1, delay_cost=1)
	c_cc_t2_t4_mem0 += MAS_MEM[8]
	S += 80 < c_cc_t2_t4_mem0
	S += c_cc_t2_t4_mem0 <= c_cc_t2_t4

	c_cc_t2_t4_mem1 = S.Task('c_cc_t2_t4_mem1', length=1, delay_cost=1)
	c_cc_t2_t4_mem1 += MAS_MEM[1]
	S += 18 < c_cc_t2_t4_mem1
	S += c_cc_t2_t4_mem1 <= c_cc_t2_t4

	c_cc_t20 = S.Task('c_cc_t20', length=2, delay_cost=1)
	c_cc_t20 += alt(MAS)
	c_cc_t20_in = S.Task('c_cc_t20_in', length=1, delay_cost=1)
	c_cc_t20_in += alt(MAS_in)
	S += c_cc_t20_in*MAS_in[0]<=c_cc_t20*MAS[0]

	S += c_cc_t20_in*MAS_in[1]<=c_cc_t20*MAS[1]

	S += c_cc_t20_in*MAS_in[2]<=c_cc_t20*MAS[2]

	S += c_cc_t20_in*MAS_in[3]<=c_cc_t20*MAS[3]

	S += c_cc_t20_in*MAS_in[4]<=c_cc_t20*MAS[4]

	S += c_cc_t20_in*MAS_in[5]<=c_cc_t20*MAS[5]

	c_cc_t20_mem0 = S.Task('c_cc_t20_mem0', length=1, delay_cost=1)
	c_cc_t20_mem0 += MM_MEM[2]
	S += 88 < c_cc_t20_mem0
	S += c_cc_t20_mem0 <= c_cc_t20

	c_cc_t20_mem1 = S.Task('c_cc_t20_mem1', length=1, delay_cost=1)
	c_cc_t20_mem1 += MM_MEM[3]
	S += 87 < c_cc_t20_mem1
	S += c_cc_t20_mem1 <= c_cc_t20

	c_cc_t2_t5 = S.Task('c_cc_t2_t5', length=2, delay_cost=1)
	c_cc_t2_t5 += alt(MAS)
	c_cc_t2_t5_in = S.Task('c_cc_t2_t5_in', length=1, delay_cost=1)
	c_cc_t2_t5_in += alt(MAS_in)
	S += c_cc_t2_t5_in*MAS_in[0]<=c_cc_t2_t5*MAS[0]

	S += c_cc_t2_t5_in*MAS_in[1]<=c_cc_t2_t5*MAS[1]

	S += c_cc_t2_t5_in*MAS_in[2]<=c_cc_t2_t5*MAS[2]

	S += c_cc_t2_t5_in*MAS_in[3]<=c_cc_t2_t5*MAS[3]

	S += c_cc_t2_t5_in*MAS_in[4]<=c_cc_t2_t5*MAS[4]

	S += c_cc_t2_t5_in*MAS_in[5]<=c_cc_t2_t5*MAS[5]

	c_cc_t2_t5_mem0 = S.Task('c_cc_t2_t5_mem0', length=1, delay_cost=1)
	c_cc_t2_t5_mem0 += MM_MEM[2]
	S += 88 < c_cc_t2_t5_mem0
	S += c_cc_t2_t5_mem0 <= c_cc_t2_t5

	c_cc_t2_t5_mem1 = S.Task('c_cc_t2_t5_mem1', length=1, delay_cost=1)
	c_cc_t2_t5_mem1 += MM_MEM[3]
	S += 87 < c_cc_t2_t5_mem1
	S += c_cc_t2_t5_mem1 <= c_cc_t2_t5

	c_cc_t40 = S.Task('c_cc_t40', length=2, delay_cost=1)
	c_cc_t40 += alt(MAS)
	c_cc_t40_in = S.Task('c_cc_t40_in', length=1, delay_cost=1)
	c_cc_t40_in += alt(MAS_in)
	S += c_cc_t40_in*MAS_in[0]<=c_cc_t40*MAS[0]

	S += c_cc_t40_in*MAS_in[1]<=c_cc_t40*MAS[1]

	S += c_cc_t40_in*MAS_in[2]<=c_cc_t40*MAS[2]

	S += c_cc_t40_in*MAS_in[3]<=c_cc_t40*MAS[3]

	S += c_cc_t40_in*MAS_in[4]<=c_cc_t40*MAS[4]

	S += c_cc_t40_in*MAS_in[5]<=c_cc_t40*MAS[5]

	c_cc_t40_mem0 = S.Task('c_cc_t40_mem0', length=1, delay_cost=1)
	c_cc_t40_mem0 += MAS_MEM[8]
	S += 29 < c_cc_t40_mem0
	S += c_cc_t40_mem0 <= c_cc_t40

	c_cc_t40_mem1 = S.Task('c_cc_t40_mem1', length=1, delay_cost=1)
	c_cc_t40_mem1 += MAS_MEM[11]
	S += 32 < c_cc_t40_mem1
	S += c_cc_t40_mem1 <= c_cc_t40

	c_cc_t41 = S.Task('c_cc_t41', length=2, delay_cost=1)
	c_cc_t41 += alt(MAS)
	c_cc_t41_in = S.Task('c_cc_t41_in', length=1, delay_cost=1)
	c_cc_t41_in += alt(MAS_in)
	S += c_cc_t41_in*MAS_in[0]<=c_cc_t41*MAS[0]

	S += c_cc_t41_in*MAS_in[1]<=c_cc_t41*MAS[1]

	S += c_cc_t41_in*MAS_in[2]<=c_cc_t41*MAS[2]

	S += c_cc_t41_in*MAS_in[3]<=c_cc_t41*MAS[3]

	S += c_cc_t41_in*MAS_in[4]<=c_cc_t41*MAS[4]

	S += c_cc_t41_in*MAS_in[5]<=c_cc_t41*MAS[5]

	c_cc_t41_mem0 = S.Task('c_cc_t41_mem0', length=1, delay_cost=1)
	c_cc_t41_mem0 += MAS_MEM[10]
	S += 32 < c_cc_t41_mem0
	S += c_cc_t41_mem0 <= c_cc_t41

	c_cc_t41_mem1 = S.Task('c_cc_t41_mem1', length=1, delay_cost=1)
	c_cc_t41_mem1 += MAS_MEM[9]
	S += 29 < c_cc_t41_mem1
	S += c_cc_t41_mem1 <= c_cc_t41

	c_cc11 = S.Task('c_cc11', length=2, delay_cost=1)
	c_cc11 += alt(MAS)
	c_cc11_in = S.Task('c_cc11_in', length=1, delay_cost=1)
	c_cc11_in += alt(MAS_in)
	S += c_cc11_in*MAS_in[0]<=c_cc11*MAS[0]

	S += c_cc11_in*MAS_in[1]<=c_cc11*MAS[1]

	S += c_cc11_in*MAS_in[2]<=c_cc11*MAS[2]

	S += c_cc11_in*MAS_in[3]<=c_cc11*MAS[3]

	S += c_cc11_in*MAS_in[4]<=c_cc11*MAS[4]

	S += c_cc11_in*MAS_in[5]<=c_cc11*MAS[5]

	c_cc11_mem0 = S.Task('c_cc11_mem0', length=1, delay_cost=1)
	c_cc11_mem0 += MAS_MEM[10]
	S += 32 < c_cc11_mem0
	S += c_cc11_mem0 <= c_cc11

	c_cc11_mem1 = S.Task('c_cc11_mem1', length=1, delay_cost=1)
	c_cc11_mem1 += MAS_MEM[11]
	S += 32 < c_cc11_mem1
	S += c_cc11_mem1 <= c_cc11

	c_ab_t41 = S.Task('c_ab_t41', length=2, delay_cost=1)
	c_ab_t41 += alt(MAS)
	c_ab_t41_in = S.Task('c_ab_t41_in', length=1, delay_cost=1)
	c_ab_t41_in += alt(MAS_in)
	S += c_ab_t41_in*MAS_in[0]<=c_ab_t41*MAS[0]

	S += c_ab_t41_in*MAS_in[1]<=c_ab_t41*MAS[1]

	S += c_ab_t41_in*MAS_in[2]<=c_ab_t41*MAS[2]

	S += c_ab_t41_in*MAS_in[3]<=c_ab_t41*MAS[3]

	S += c_ab_t41_in*MAS_in[4]<=c_ab_t41*MAS[4]

	S += c_ab_t41_in*MAS_in[5]<=c_ab_t41*MAS[5]

	c_ab_t41_mem0 = S.Task('c_ab_t41_mem0', length=1, delay_cost=1)
	c_ab_t41_mem0 += MM_MEM[2]
	S += 75 < c_ab_t41_mem0
	S += c_ab_t41_mem0 <= c_ab_t41

	c_ab_t41_mem1 = S.Task('c_ab_t41_mem1', length=1, delay_cost=1)
	c_ab_t41_mem1 += MAS_MEM[1]
	S += 75 < c_ab_t41_mem1
	S += c_ab_t41_mem1 <= c_ab_t41

	c_ab_s00 = S.Task('c_ab_s00', length=2, delay_cost=1)
	c_ab_s00 += alt(MAS)
	c_ab_s00_in = S.Task('c_ab_s00_in', length=1, delay_cost=1)
	c_ab_s00_in += alt(MAS_in)
	S += c_ab_s00_in*MAS_in[0]<=c_ab_s00*MAS[0]

	S += c_ab_s00_in*MAS_in[1]<=c_ab_s00*MAS[1]

	S += c_ab_s00_in*MAS_in[2]<=c_ab_s00*MAS[2]

	S += c_ab_s00_in*MAS_in[3]<=c_ab_s00*MAS[3]

	S += c_ab_s00_in*MAS_in[4]<=c_ab_s00*MAS[4]

	S += c_ab_s00_in*MAS_in[5]<=c_ab_s00*MAS[5]

	c_ab_s00_mem0 = S.Task('c_ab_s00_mem0', length=1, delay_cost=1)
	c_ab_s00_mem0 += MAS_MEM[0]
	S += 39 < c_ab_s00_mem0
	S += c_ab_s00_mem0 <= c_ab_s00

	c_ab_s00_mem1 = S.Task('c_ab_s00_mem1', length=1, delay_cost=1)
	c_ab_s00_mem1 += MAS_MEM[11]
	S += 71 < c_ab_s00_mem1
	S += c_ab_s00_mem1 <= c_ab_s00

	c_ab_s01 = S.Task('c_ab_s01', length=2, delay_cost=1)
	c_ab_s01 += alt(MAS)
	c_ab_s01_in = S.Task('c_ab_s01_in', length=1, delay_cost=1)
	c_ab_s01_in += alt(MAS_in)
	S += c_ab_s01_in*MAS_in[0]<=c_ab_s01*MAS[0]

	S += c_ab_s01_in*MAS_in[1]<=c_ab_s01*MAS[1]

	S += c_ab_s01_in*MAS_in[2]<=c_ab_s01*MAS[2]

	S += c_ab_s01_in*MAS_in[3]<=c_ab_s01*MAS[3]

	S += c_ab_s01_in*MAS_in[4]<=c_ab_s01*MAS[4]

	S += c_ab_s01_in*MAS_in[5]<=c_ab_s01*MAS[5]

	c_ab_s01_mem0 = S.Task('c_ab_s01_mem0', length=1, delay_cost=1)
	c_ab_s01_mem0 += MAS_MEM[10]
	S += 71 < c_ab_s01_mem0
	S += c_ab_s01_mem0 <= c_ab_s01

	c_ab_s01_mem1 = S.Task('c_ab_s01_mem1', length=1, delay_cost=1)
	c_ab_s01_mem1 += MAS_MEM[1]
	S += 39 < c_ab_s01_mem1
	S += c_ab_s01_mem1 <= c_ab_s01

	c_ab_t51 = S.Task('c_ab_t51', length=2, delay_cost=1)
	c_ab_t51 += alt(MAS)
	c_ab_t51_in = S.Task('c_ab_t51_in', length=1, delay_cost=1)
	c_ab_t51_in += alt(MAS_in)
	S += c_ab_t51_in*MAS_in[0]<=c_ab_t51*MAS[0]

	S += c_ab_t51_in*MAS_in[1]<=c_ab_t51*MAS[1]

	S += c_ab_t51_in*MAS_in[2]<=c_ab_t51*MAS[2]

	S += c_ab_t51_in*MAS_in[3]<=c_ab_t51*MAS[3]

	S += c_ab_t51_in*MAS_in[4]<=c_ab_t51*MAS[4]

	S += c_ab_t51_in*MAS_in[5]<=c_ab_t51*MAS[5]

	c_ab_t51_mem0 = S.Task('c_ab_t51_mem0', length=1, delay_cost=1)
	c_ab_t51_mem0 += MAS_MEM[4]
	S += 24 < c_ab_t51_mem0
	S += c_ab_t51_mem0 <= c_ab_t51

	c_ab_t51_mem1 = S.Task('c_ab_t51_mem1', length=1, delay_cost=1)
	c_ab_t51_mem1 += MAS_MEM[11]
	S += 71 < c_ab_t51_mem1
	S += c_ab_t51_mem1 <= c_ab_t51

	c_ab10 = S.Task('c_ab10', length=2, delay_cost=1)
	c_ab10 += alt(MAS)
	c_ab10_in = S.Task('c_ab10_in', length=1, delay_cost=1)
	c_ab10_in += alt(MAS_in)
	S += c_ab10_in*MAS_in[0]<=c_ab10*MAS[0]

	S += c_ab10_in*MAS_in[1]<=c_ab10*MAS[1]

	S += c_ab10_in*MAS_in[2]<=c_ab10*MAS[2]

	S += c_ab10_in*MAS_in[3]<=c_ab10*MAS[3]

	S += c_ab10_in*MAS_in[4]<=c_ab10*MAS[4]

	S += c_ab10_in*MAS_in[5]<=c_ab10*MAS[5]

	c_ab10_mem0 = S.Task('c_ab10_mem0', length=1, delay_cost=1)
	c_ab10_mem0 += MAS_MEM[6]
	S += 74 < c_ab10_mem0
	S += c_ab10_mem0 <= c_ab10

	c_ab10_mem1 = S.Task('c_ab10_mem1', length=1, delay_cost=1)
	c_ab10_mem1 += MAS_MEM[9]
	S += 41 < c_ab10_mem1
	S += c_ab10_mem1 <= c_ab10

	c_bc_t41 = S.Task('c_bc_t41', length=2, delay_cost=1)
	c_bc_t41 += alt(MAS)
	c_bc_t41_in = S.Task('c_bc_t41_in', length=1, delay_cost=1)
	c_bc_t41_in += alt(MAS_in)
	S += c_bc_t41_in*MAS_in[0]<=c_bc_t41*MAS[0]

	S += c_bc_t41_in*MAS_in[1]<=c_bc_t41*MAS[1]

	S += c_bc_t41_in*MAS_in[2]<=c_bc_t41*MAS[2]

	S += c_bc_t41_in*MAS_in[3]<=c_bc_t41*MAS[3]

	S += c_bc_t41_in*MAS_in[4]<=c_bc_t41*MAS[4]

	S += c_bc_t41_in*MAS_in[5]<=c_bc_t41*MAS[5]

	c_bc_t41_mem0 = S.Task('c_bc_t41_mem0', length=1, delay_cost=1)
	c_bc_t41_mem0 += MM_MEM[2]
	S += 68 < c_bc_t41_mem0
	S += c_bc_t41_mem0 <= c_bc_t41

	c_bc_t41_mem1 = S.Task('c_bc_t41_mem1', length=1, delay_cost=1)
	c_bc_t41_mem1 += MAS_MEM[7]
	S += 68 < c_bc_t41_mem1
	S += c_bc_t41_mem1 <= c_bc_t41

	c_bc_s00 = S.Task('c_bc_s00', length=2, delay_cost=1)
	c_bc_s00 += alt(MAS)
	c_bc_s00_in = S.Task('c_bc_s00_in', length=1, delay_cost=1)
	c_bc_s00_in += alt(MAS_in)
	S += c_bc_s00_in*MAS_in[0]<=c_bc_s00*MAS[0]

	S += c_bc_s00_in*MAS_in[1]<=c_bc_s00*MAS[1]

	S += c_bc_s00_in*MAS_in[2]<=c_bc_s00*MAS[2]

	S += c_bc_s00_in*MAS_in[3]<=c_bc_s00*MAS[3]

	S += c_bc_s00_in*MAS_in[4]<=c_bc_s00*MAS[4]

	S += c_bc_s00_in*MAS_in[5]<=c_bc_s00*MAS[5]

	c_bc_s00_mem0 = S.Task('c_bc_s00_mem0', length=1, delay_cost=1)
	c_bc_s00_mem0 += MAS_MEM[0]
	S += 56 < c_bc_s00_mem0
	S += c_bc_s00_mem0 <= c_bc_s00

	c_bc_s00_mem1 = S.Task('c_bc_s00_mem1', length=1, delay_cost=1)
	c_bc_s00_mem1 += MAS_MEM[5]
	S += 61 < c_bc_s00_mem1
	S += c_bc_s00_mem1 <= c_bc_s00

	c_bc_s01 = S.Task('c_bc_s01', length=2, delay_cost=1)
	c_bc_s01 += alt(MAS)
	c_bc_s01_in = S.Task('c_bc_s01_in', length=1, delay_cost=1)
	c_bc_s01_in += alt(MAS_in)
	S += c_bc_s01_in*MAS_in[0]<=c_bc_s01*MAS[0]

	S += c_bc_s01_in*MAS_in[1]<=c_bc_s01*MAS[1]

	S += c_bc_s01_in*MAS_in[2]<=c_bc_s01*MAS[2]

	S += c_bc_s01_in*MAS_in[3]<=c_bc_s01*MAS[3]

	S += c_bc_s01_in*MAS_in[4]<=c_bc_s01*MAS[4]

	S += c_bc_s01_in*MAS_in[5]<=c_bc_s01*MAS[5]

	c_bc_s01_mem0 = S.Task('c_bc_s01_mem0', length=1, delay_cost=1)
	c_bc_s01_mem0 += MAS_MEM[4]
	S += 61 < c_bc_s01_mem0
	S += c_bc_s01_mem0 <= c_bc_s01

	c_bc_s01_mem1 = S.Task('c_bc_s01_mem1', length=1, delay_cost=1)
	c_bc_s01_mem1 += MAS_MEM[1]
	S += 56 < c_bc_s01_mem1
	S += c_bc_s01_mem1 <= c_bc_s01

	c_bc_t51 = S.Task('c_bc_t51', length=2, delay_cost=1)
	c_bc_t51 += alt(MAS)
	c_bc_t51_in = S.Task('c_bc_t51_in', length=1, delay_cost=1)
	c_bc_t51_in += alt(MAS_in)
	S += c_bc_t51_in*MAS_in[0]<=c_bc_t51*MAS[0]

	S += c_bc_t51_in*MAS_in[1]<=c_bc_t51*MAS[1]

	S += c_bc_t51_in*MAS_in[2]<=c_bc_t51*MAS[2]

	S += c_bc_t51_in*MAS_in[3]<=c_bc_t51*MAS[3]

	S += c_bc_t51_in*MAS_in[4]<=c_bc_t51*MAS[4]

	S += c_bc_t51_in*MAS_in[5]<=c_bc_t51*MAS[5]

	c_bc_t51_mem0 = S.Task('c_bc_t51_mem0', length=1, delay_cost=1)
	c_bc_t51_mem0 += MAS_MEM[8]
	S += 70 < c_bc_t51_mem0
	S += c_bc_t51_mem0 <= c_bc_t51

	c_bc_t51_mem1 = S.Task('c_bc_t51_mem1', length=1, delay_cost=1)
	c_bc_t51_mem1 += MAS_MEM[5]
	S += 61 < c_bc_t51_mem1
	S += c_bc_t51_mem1 <= c_bc_t51

	c_bc10 = S.Task('c_bc10', length=2, delay_cost=1)
	c_bc10 += alt(MAS)
	c_bc10_in = S.Task('c_bc10_in', length=1, delay_cost=1)
	c_bc10_in += alt(MAS_in)
	S += c_bc10_in*MAS_in[0]<=c_bc10*MAS[0]

	S += c_bc10_in*MAS_in[1]<=c_bc10*MAS[1]

	S += c_bc10_in*MAS_in[2]<=c_bc10*MAS[2]

	S += c_bc10_in*MAS_in[3]<=c_bc10*MAS[3]

	S += c_bc10_in*MAS_in[4]<=c_bc10*MAS[4]

	S += c_bc10_in*MAS_in[5]<=c_bc10*MAS[5]

	c_bc10_mem0 = S.Task('c_bc10_mem0', length=1, delay_cost=1)
	c_bc10_mem0 += MAS_MEM[10]
	S += 67 < c_bc10_mem0
	S += c_bc10_mem0 <= c_bc10

	c_bc10_mem1 = S.Task('c_bc10_mem1', length=1, delay_cost=1)
	c_bc10_mem1 += MAS_MEM[7]
	S += 71 < c_bc10_mem1
	S += c_bc10_mem1 <= c_bc10

	c_ac_t41 = S.Task('c_ac_t41', length=2, delay_cost=1)
	c_ac_t41 += alt(MAS)
	c_ac_t41_in = S.Task('c_ac_t41_in', length=1, delay_cost=1)
	c_ac_t41_in += alt(MAS_in)
	S += c_ac_t41_in*MAS_in[0]<=c_ac_t41*MAS[0]

	S += c_ac_t41_in*MAS_in[1]<=c_ac_t41*MAS[1]

	S += c_ac_t41_in*MAS_in[2]<=c_ac_t41*MAS[2]

	S += c_ac_t41_in*MAS_in[3]<=c_ac_t41*MAS[3]

	S += c_ac_t41_in*MAS_in[4]<=c_ac_t41*MAS[4]

	S += c_ac_t41_in*MAS_in[5]<=c_ac_t41*MAS[5]

	c_ac_t41_mem0 = S.Task('c_ac_t41_mem0', length=1, delay_cost=1)
	c_ac_t41_mem0 += MM_MEM[2]
	S += 65 < c_ac_t41_mem0
	S += c_ac_t41_mem0 <= c_ac_t41

	c_ac_t41_mem1 = S.Task('c_ac_t41_mem1', length=1, delay_cost=1)
	c_ac_t41_mem1 += MAS_MEM[9]
	S += 67 < c_ac_t41_mem1
	S += c_ac_t41_mem1 <= c_ac_t41

	c_ac_s00 = S.Task('c_ac_s00', length=2, delay_cost=1)
	c_ac_s00 += alt(MAS)
	c_ac_s00_in = S.Task('c_ac_s00_in', length=1, delay_cost=1)
	c_ac_s00_in += alt(MAS_in)
	S += c_ac_s00_in*MAS_in[0]<=c_ac_s00*MAS[0]

	S += c_ac_s00_in*MAS_in[1]<=c_ac_s00*MAS[1]

	S += c_ac_s00_in*MAS_in[2]<=c_ac_s00*MAS[2]

	S += c_ac_s00_in*MAS_in[3]<=c_ac_s00*MAS[3]

	S += c_ac_s00_in*MAS_in[4]<=c_ac_s00*MAS[4]

	S += c_ac_s00_in*MAS_in[5]<=c_ac_s00*MAS[5]

	c_ac_s00_mem0 = S.Task('c_ac_s00_mem0', length=1, delay_cost=1)
	c_ac_s00_mem0 += MAS_MEM[8]
	S += 50 < c_ac_s00_mem0
	S += c_ac_s00_mem0 <= c_ac_s00

	c_ac_s00_mem1 = S.Task('c_ac_s00_mem1', length=1, delay_cost=1)
	c_ac_s00_mem1 += MAS_MEM[7]
	S += 70 < c_ac_s00_mem1
	S += c_ac_s00_mem1 <= c_ac_s00

	c_ac_s01 = S.Task('c_ac_s01', length=2, delay_cost=1)
	c_ac_s01 += alt(MAS)
	c_ac_s01_in = S.Task('c_ac_s01_in', length=1, delay_cost=1)
	c_ac_s01_in += alt(MAS_in)
	S += c_ac_s01_in*MAS_in[0]<=c_ac_s01*MAS[0]

	S += c_ac_s01_in*MAS_in[1]<=c_ac_s01*MAS[1]

	S += c_ac_s01_in*MAS_in[2]<=c_ac_s01*MAS[2]

	S += c_ac_s01_in*MAS_in[3]<=c_ac_s01*MAS[3]

	S += c_ac_s01_in*MAS_in[4]<=c_ac_s01*MAS[4]

	S += c_ac_s01_in*MAS_in[5]<=c_ac_s01*MAS[5]

	c_ac_s01_mem0 = S.Task('c_ac_s01_mem0', length=1, delay_cost=1)
	c_ac_s01_mem0 += MAS_MEM[6]
	S += 70 < c_ac_s01_mem0
	S += c_ac_s01_mem0 <= c_ac_s01

	c_ac_s01_mem1 = S.Task('c_ac_s01_mem1', length=1, delay_cost=1)
	c_ac_s01_mem1 += MAS_MEM[9]
	S += 50 < c_ac_s01_mem1
	S += c_ac_s01_mem1 <= c_ac_s01

	c_ac_t51 = S.Task('c_ac_t51', length=2, delay_cost=1)
	c_ac_t51 += alt(MAS)
	c_ac_t51_in = S.Task('c_ac_t51_in', length=1, delay_cost=1)
	c_ac_t51_in += alt(MAS_in)
	S += c_ac_t51_in*MAS_in[0]<=c_ac_t51*MAS[0]

	S += c_ac_t51_in*MAS_in[1]<=c_ac_t51*MAS[1]

	S += c_ac_t51_in*MAS_in[2]<=c_ac_t51*MAS[2]

	S += c_ac_t51_in*MAS_in[3]<=c_ac_t51*MAS[3]

	S += c_ac_t51_in*MAS_in[4]<=c_ac_t51*MAS[4]

	S += c_ac_t51_in*MAS_in[5]<=c_ac_t51*MAS[5]

	c_ac_t51_mem0 = S.Task('c_ac_t51_mem0', length=1, delay_cost=1)
	c_ac_t51_mem0 += MAS_MEM[8]
	S += 59 < c_ac_t51_mem0
	S += c_ac_t51_mem0 <= c_ac_t51

	c_ac_t51_mem1 = S.Task('c_ac_t51_mem1', length=1, delay_cost=1)
	c_ac_t51_mem1 += MAS_MEM[7]
	S += 70 < c_ac_t51_mem1
	S += c_ac_t51_mem1 <= c_ac_t51

	c_ac10 = S.Task('c_ac10', length=2, delay_cost=1)
	c_ac10 += alt(MAS)
	c_ac10_in = S.Task('c_ac10_in', length=1, delay_cost=1)
	c_ac10_in += alt(MAS_in)
	S += c_ac10_in*MAS_in[0]<=c_ac10*MAS[0]

	S += c_ac10_in*MAS_in[1]<=c_ac10*MAS[1]

	S += c_ac10_in*MAS_in[2]<=c_ac10*MAS[2]

	S += c_ac10_in*MAS_in[3]<=c_ac10*MAS[3]

	S += c_ac10_in*MAS_in[4]<=c_ac10*MAS[4]

	S += c_ac10_in*MAS_in[5]<=c_ac10*MAS[5]

	c_ac10_mem0 = S.Task('c_ac10_mem0', length=1, delay_cost=1)
	c_ac10_mem0 += MAS_MEM[8]
	S += 66 < c_ac10_mem0
	S += c_ac10_mem0 <= c_ac10

	c_ac10_mem1 = S.Task('c_ac10_mem1', length=1, delay_cost=1)
	c_ac10_mem1 += MAS_MEM[3]
	S += 52 < c_ac10_mem1
	S += c_ac10_mem1 <= c_ac10

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage2MAS6/FP12_INV_BEFORE_FPINV/schedule5.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

