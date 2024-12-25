from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 184
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=9)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	S += t10_t2_in >= 0
	t10_t2_in += MAS_in[5]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 0
	t10_t2_mem0 += MAIN_MEM_r[0]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 0
	t10_t2_mem1 += MAIN_MEM_r[1]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 1
	t10_t1_in += MM_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 1
	t10_t1_mem0 += MAIN_MEM_r[0]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 1
	t10_t1_mem1 += MAIN_MEM_r[1]

	t10_t2 = S.Task('t10_t2', length=2, delay_cost=1)
	S += t10_t2 >= 1
	t10_t2 += MAS[5]

	t10_t1 = S.Task('t10_t1', length=9, delay_cost=1)
	S += t10_t1 >= 2
	t10_t1 += MM[0]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 2
	t7_t0_in += MAS_in[1]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 2
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 2
	t7_t0_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=2, delay_cost=1)
	S += t7_t0 >= 3
	t7_t0 += MAS[1]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 3
	t7_t3_in += MM_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 3
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 3
	t7_t3_mem1 += MAIN_MEM_r[1]

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 4
	t10_t0_in += MM_in[1]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 4
	t10_t0_mem0 += MAIN_MEM_r[0]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 4
	t10_t0_mem1 += MAIN_MEM_r[1]

	t7_t3 = S.Task('t7_t3', length=9, delay_cost=1)
	S += t7_t3 >= 4
	t7_t3 += MM[0]

	t10_t0 = S.Task('t10_t0', length=9, delay_cost=1)
	S += t10_t0 >= 5
	t10_t0 += MM[1]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 5
	t1_t0_in += MAS_in[2]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 5
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 5
	t1_t0_mem1 += MAIN_MEM_r[1]

	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	S += t10_t3_in >= 6
	t10_t3_in += MAS_in[5]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 6
	t10_t3_mem0 += MAIN_MEM_r[0]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 6
	t10_t3_mem1 += MAIN_MEM_r[1]

	t1_t0 = S.Task('t1_t0', length=2, delay_cost=1)
	S += t1_t0 >= 6
	t1_t0 += MAS[2]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 7
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 7
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 7
	t0_t3_mem1 += MAIN_MEM_r[1]

	t10_t3 = S.Task('t10_t3', length=2, delay_cost=1)
	S += t10_t3 >= 7
	t10_t3 += MAS[5]

	t0_t3 = S.Task('t0_t3', length=9, delay_cost=1)
	S += t0_t3 >= 8
	t0_t3 += MM[0]

	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	S += t10_t4_in >= 8
	t10_t4_in += MM_in[1]

	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	S += t10_t4_mem0 >= 8
	t10_t4_mem0 += MAS_MEM[10]

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	S += t10_t4_mem1 >= 8
	t10_t4_mem1 += MAS_MEM[11]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 8
	t7_t1_in += MAS_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 8
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 8
	t7_t1_mem1 += MAIN_MEM_r[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 9
	t0_t0_in += MAS_in[1]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 9
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 9
	t0_t0_mem1 += MAIN_MEM_r[1]

	t10_t4 = S.Task('t10_t4', length=9, delay_cost=1)
	S += t10_t4 >= 9
	t10_t4 += MM[1]

	t7_t1 = S.Task('t7_t1', length=2, delay_cost=1)
	S += t7_t1 >= 9
	t7_t1 += MAS[0]

	t0_t0 = S.Task('t0_t0', length=2, delay_cost=1)
	S += t0_t0 >= 10
	t0_t0 += MAS[1]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 10
	t5_t1_in += MM_in[1]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 10
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 10
	t5_t1_mem1 += MAIN_MEM_r[1]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 10
	t7_t2_in += MM_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 10
	t7_t2_mem0 += MAS_MEM[2]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 10
	t7_t2_mem1 += MAS_MEM[1]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 11
	t1_t3_in += MM_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 11
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 11
	t1_t3_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=9, delay_cost=1)
	S += t5_t1 >= 11
	t5_t1 += MM[1]

	t7_t2 = S.Task('t7_t2', length=9, delay_cost=1)
	S += t7_t2 >= 11
	t7_t2 += MM[0]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 12
	t1_t1_in += MAS_in[2]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 12
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 12
	t1_t1_mem1 += MAIN_MEM_r[1]

	t1_t3 = S.Task('t1_t3', length=9, delay_cost=1)
	S += t1_t3 >= 12
	t1_t3 += MM[0]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 12
	t71_in += MAS_in[1]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 12
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 12
	t71_mem1 += MM_MEM[1]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 13
	t100_in += MAS_in[3]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 13
	t100_mem0 += MM_MEM[2]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 13
	t100_mem1 += MM_MEM[1]

	t1_t1 = S.Task('t1_t1', length=2, delay_cost=1)
	S += t1_t1 >= 13
	t1_t1 += MAS[2]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 13
	t5_t3_in += MAS_in[1]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 13
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 13
	t5_t3_mem1 += MAIN_MEM_r[1]

	t71 = S.Task('t71', length=2, delay_cost=1)
	S += t71 >= 13
	t71 += MAS[1]

	t100 = S.Task('t100', length=2, delay_cost=1)
	S += t100 >= 14
	t100 += MAS[3]

	t10_t5_in = S.Task('t10_t5_in', length=1, delay_cost=1)
	S += t10_t5_in >= 14
	t10_t5_in += MAS_in[5]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 14
	t10_t5_mem0 += MM_MEM[2]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 14
	t10_t5_mem1 += MM_MEM[1]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 14
	t1_t2_in += MM_in[1]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 14
	t1_t2_mem0 += MAS_MEM[4]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 14
	t1_t2_mem1 += MAS_MEM[5]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 14
	t2_t2_in += MAS_in[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 14
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 14
	t2_t2_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=2, delay_cost=1)
	S += t5_t3 >= 14
	t5_t3 += MAS[1]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 14
	t81_in += MAS_in[2]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 14
	t81_mem0 += MAS_MEM[2]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 14
	t81_mem1 += MAS_MEM[3]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 15
	t0_t1_in += MAS_in[2]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 15
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 15
	t0_t1_mem1 += MAIN_MEM_r[1]

	t10_t5 = S.Task('t10_t5', length=2, delay_cost=1)
	S += t10_t5 >= 15
	t10_t5 += MAS[5]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 15
	t110_in += MAS_in[0]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 15
	t110_mem0 += MAS_MEM[6]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 15
	t110_mem1 += MAS_MEM[7]

	t1_t2 = S.Task('t1_t2', length=9, delay_cost=1)
	S += t1_t2 >= 15
	t1_t2 += MM[1]

	t2_t2 = S.Task('t2_t2', length=2, delay_cost=1)
	S += t2_t2 >= 15
	t2_t2 += MAS[0]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 15
	t7_t5_in += MAS_in[5]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 15
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 15
	t7_t5_mem1 += MM_MEM[1]

	t81 = S.Task('t81', length=2, delay_cost=1)
	S += t81 >= 15
	t81 += MAS[2]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 16
	t01_in += MAS_in[4]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 16
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 16
	t01_mem1 += MM_MEM[1]

	t0_t1 = S.Task('t0_t1', length=2, delay_cost=1)
	S += t0_t1 >= 16
	t0_t1 += MAS[2]

	t110 = S.Task('t110', length=2, delay_cost=1)
	S += t110 >= 16
	t110 += MAS[0]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 16
	t5_t0_in += MM_in[1]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 16
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 16
	t5_t0_mem1 += MAIN_MEM_r[1]

	t7_t5 = S.Task('t7_t5', length=2, delay_cost=1)
	S += t7_t5 >= 16
	t7_t5 += MAS[5]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 16
	t91_in += MAS_in[1]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 16
	t91_mem0 += MAS_MEM[4]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 16
	t91_mem1 += MAS_MEM[3]

	t01 = S.Task('t01', length=2, delay_cost=1)
	S += t01 >= 17
	t01 += MAS[4]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 17
	t0_t2_in += MM_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 17
	t0_t2_mem0 += MAS_MEM[2]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 17
	t0_t2_mem1 += MAS_MEM[5]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 17
	t0_t5_in += MAS_in[3]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 17
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 17
	t0_t5_mem1 += MM_MEM[1]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 17
	t101_in += MAS_in[2]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 17
	t101_mem0 += MM_MEM[2]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 17
	t101_mem1 += MAS_MEM[11]

	t5_t0 = S.Task('t5_t0', length=9, delay_cost=1)
	S += t5_t0 >= 17
	t5_t0 += MM[1]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 17
	t5_t2_in += MAS_in[4]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 17
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 17
	t5_t2_mem1 += MAIN_MEM_r[1]

	t91 = S.Task('t91', length=2, delay_cost=1)
	S += t91 >= 17
	t91 += MAS[1]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 18
	c010_in += MM_in[1]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 18
	c010_mem0 += MAS_MEM[0]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 18
	c010_mem1 += MAIN_MEM_r[1]

	t0_t2 = S.Task('t0_t2', length=9, delay_cost=1)
	S += t0_t2 >= 18
	t0_t2 += MM[0]

	t0_t5 = S.Task('t0_t5', length=2, delay_cost=1)
	S += t0_t5 >= 18
	t0_t5 += MAS[3]

	t101 = S.Task('t101', length=2, delay_cost=1)
	S += t101 >= 18
	t101 += MAS[2]

	t5_t2 = S.Task('t5_t2', length=2, delay_cost=1)
	S += t5_t2 >= 18
	t5_t2 += MAS[4]

	c010 = S.Task('c010', length=9, delay_cost=1)
	S += c010 >= 19
	c010 += MM[1]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 19
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 19
	c201_mem0 += MAS_MEM[2]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 19
	c201_mem1 += MAIN_MEM_r[1]

	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	S += t111_in >= 19
	t111_in += MAS_in[5]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 19
	t111_mem0 += MAS_MEM[4]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 19
	t111_mem1 += MAS_MEM[5]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 19
	t5_t4_in += MM_in[1]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 19
	t5_t4_mem0 += MAS_MEM[8]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 19
	t5_t4_mem1 += MAS_MEM[3]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 19
	t70_in += MAS_in[4]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 19
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 19
	t70_mem1 += MAS_MEM[11]

	c201 = S.Task('c201', length=9, delay_cost=1)
	S += c201 >= 20
	c201 += MM[0]

	t111 = S.Task('t111', length=2, delay_cost=1)
	S += t111 >= 20
	t111 += MAS[5]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 20
	t11_in += MAS_in[2]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 20
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 20
	t11_mem1 += MM_MEM[1]

	t5_t4 = S.Task('t5_t4', length=9, delay_cost=1)
	S += t5_t4 >= 20
	t5_t4 += MM[1]

	t70 = S.Task('t70', length=2, delay_cost=1)
	S += t70 >= 20
	t70 += MAS[4]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 21
	c011_in += MM_in[1]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 21
	c011_mem0 += MAS_MEM[10]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 21
	c011_mem1 += MAIN_MEM_r[1]

	t11 = S.Task('t11', length=2, delay_cost=1)
	S += t11 >= 21
	t11 += MAS[2]

	t12_t3_in = S.Task('t12_t3_in', length=1, delay_cost=1)
	S += t12_t3_in >= 21
	t12_t3_in += MAS_in[5]

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	S += t12_t3_mem0 >= 21
	t12_t3_mem0 += MAS_MEM[0]

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	S += t12_t3_mem1 >= 21
	t12_t3_mem1 += MAS_MEM[11]

	t1_t5_in = S.Task('t1_t5_in', length=1, delay_cost=1)
	S += t1_t5_in >= 21
	t1_t5_in += MAS_in[2]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 21
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 21
	t1_t5_mem1 += MM_MEM[1]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 21
	t80_in += MAS_in[4]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 21
	t80_mem0 += MAS_MEM[8]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 21
	t80_mem1 += MAS_MEM[9]

	c011 = S.Task('c011', length=9, delay_cost=1)
	S += c011 >= 22
	c011 += MM[1]

	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	S += t12_t1_in >= 22
	t12_t1_in += MM_in[1]

	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	S += t12_t1_mem0 >= 22
	t12_t1_mem0 += MAS_MEM[8]

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	S += t12_t1_mem1 >= 22
	t12_t1_mem1 += MAS_MEM[11]

	t12_t3 = S.Task('t12_t3', length=2, delay_cost=1)
	S += t12_t3 >= 22
	t12_t3 += MAS[5]

	t1_t5 = S.Task('t1_t5', length=2, delay_cost=1)
	S += t1_t5 >= 22
	t1_t5 += MAS[2]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 22
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 22
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 22
	t2_t1_mem1 += MAS_MEM[5]

	t80 = S.Task('t80', length=2, delay_cost=1)
	S += t80 >= 22
	t80 += MAS[4]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 23
	t10_in += MAS_in[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 23
	t10_mem0 += MM_MEM[2]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 23
	t10_mem1 += MAS_MEM[5]

	t12_t1 = S.Task('t12_t1', length=9, delay_cost=1)
	S += t12_t1 >= 23
	t12_t1 += MM[1]

	t2_t1 = S.Task('t2_t1', length=9, delay_cost=1)
	S += t2_t1 >= 23
	t2_t1 += MM[0]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 23
	t90_in += MAS_in[2]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 23
	t90_mem0 += MAS_MEM[8]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 23
	t90_mem1 += MAS_MEM[9]

	t10 = S.Task('t10', length=2, delay_cost=1)
	S += t10 >= 24
	t10 += MAS[1]

	t90 = S.Task('t90', length=2, delay_cost=1)
	S += t90 >= 24
	t90 += MAS[2]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 25
	c200_in += MM_in[1]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 25
	c200_mem0 += MAS_MEM[4]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 25
	c200_mem1 += MAIN_MEM_r[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 25
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 25
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 25
	t2_t0_mem1 += MAS_MEM[3]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 25
	t2_t3_in += MAS_in[2]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 25
	t2_t3_mem0 += MAS_MEM[2]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 25
	t2_t3_mem1 += MAS_MEM[5]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 25
	t50_in += MAS_in[5]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 25
	t50_mem0 += MM_MEM[2]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 25
	t50_mem1 += MM_MEM[3]

	c200 = S.Task('c200', length=9, delay_cost=1)
	S += c200 >= 26
	c200 += MM[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 26
	t00_in += MAS_in[4]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 26
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 26
	t00_mem1 += MAS_MEM[7]

	t2_t0 = S.Task('t2_t0', length=9, delay_cost=1)
	S += t2_t0 >= 26
	t2_t0 += MM[0]

	t2_t3 = S.Task('t2_t3', length=2, delay_cost=1)
	S += t2_t3 >= 26
	t2_t3 += MAS[2]

	t50 = S.Task('t50', length=2, delay_cost=1)
	S += t50 >= 26
	t50 += MAS[5]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 26
	t5_t5_in += MAS_in[5]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 26
	t5_t5_mem0 += MM_MEM[2]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 26
	t5_t5_mem1 += MM_MEM[3]

	t00 = S.Task('t00', length=2, delay_cost=1)
	S += t00 >= 27
	t00 += MAS[4]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 27
	t2_t4_in += MM_in[1]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 27
	t2_t4_mem0 += MAS_MEM[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 27
	t2_t4_mem1 += MAS_MEM[5]

	t5_t5 = S.Task('t5_t5', length=2, delay_cost=1)
	S += t5_t5 >= 27
	t5_t5 += MAS[5]

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 27
	t60_in += MAS_in[1]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 27
	t60_mem0 += MAS_MEM[10]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 27
	t60_mem1 += MAS_MEM[11]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 28
	c010_w += MAIN_MEM_w

	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	S += t18_t3_in >= 28
	t18_t3_in += MM_in[0]

	t18_t3_mem0 = S.Task('t18_t3_mem0', length=1, delay_cost=1)
	S += t18_t3_mem0 >= 28
	t18_t3_mem0 += MAS_MEM[8]

	t18_t3_mem1 = S.Task('t18_t3_mem1', length=1, delay_cost=1)
	S += t18_t3_mem1 >= 28
	t18_t3_mem1 += MAS_MEM[9]

	t2_t4 = S.Task('t2_t4', length=9, delay_cost=1)
	S += t2_t4 >= 28
	t2_t4 += MM[1]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 28
	t51_in += MAS_in[2]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 28
	t51_mem0 += MM_MEM[2]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 28
	t51_mem1 += MAS_MEM[11]

	t60 = S.Task('t60', length=2, delay_cost=1)
	S += t60 >= 28
	t60 += MAS[1]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 29
	c201_w += MAIN_MEM_w

	t18_t0_in = S.Task('t18_t0_in', length=1, delay_cost=1)
	S += t18_t0_in >= 29
	t18_t0_in += MAS_in[2]

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	S += t18_t0_mem0 >= 29
	t18_t0_mem0 += MAS_MEM[8]

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	S += t18_t0_mem1 >= 29
	t18_t0_mem1 += MAS_MEM[9]

	t18_t3 = S.Task('t18_t3', length=9, delay_cost=1)
	S += t18_t3 >= 29
	t18_t3 += MM[0]

	t51 = S.Task('t51', length=2, delay_cost=1)
	S += t51 >= 29
	t51 += MAS[2]

	t18_t0 = S.Task('t18_t0', length=2, delay_cost=1)
	S += t18_t0 >= 30
	t18_t0 += MAS[2]

	t18_t1_in = S.Task('t18_t1_in', length=1, delay_cost=1)
	S += t18_t1_in >= 30
	t18_t1_in += MAS_in[2]

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	S += t18_t1_mem0 >= 30
	t18_t1_mem0 += MAS_MEM[8]

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	S += t18_t1_mem1 >= 30
	t18_t1_mem1 += MAS_MEM[9]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 30
	t61_in += MAS_in[5]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 30
	t61_mem0 += MAS_MEM[4]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 30
	t61_mem1 += MAS_MEM[5]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 31
	c011_w += MAIN_MEM_w

	t12_t2_in = S.Task('t12_t2_in', length=1, delay_cost=1)
	S += t12_t2_in >= 31
	t12_t2_in += MAS_in[5]

	t12_t2_mem0 = S.Task('t12_t2_mem0', length=1, delay_cost=1)
	S += t12_t2_mem0 >= 31
	t12_t2_mem0 += MAS_MEM[8]

	t12_t2_mem1 = S.Task('t12_t2_mem1', length=1, delay_cost=1)
	S += t12_t2_mem1 >= 31
	t12_t2_mem1 += MAS_MEM[9]

	t18_t1 = S.Task('t18_t1', length=2, delay_cost=1)
	S += t18_t1 >= 31
	t18_t1 += MAS[2]

	t61 = S.Task('t61', length=2, delay_cost=1)
	S += t61 >= 31
	t61 += MAS[5]

	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	S += new_TX_t3_in >= 32
	new_TX_t3_in += MAS_in[2]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 32
	new_TX_t3_mem0 += MAS_MEM[2]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 32
	new_TX_t3_mem1 += MAS_MEM[11]

	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	S += t12_t0_in >= 32
	t12_t0_in += MM_in[1]

	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	S += t12_t0_mem0 >= 32
	t12_t0_mem0 += MAS_MEM[8]

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	S += t12_t0_mem1 >= 32
	t12_t0_mem1 += MAS_MEM[1]

	t12_t2 = S.Task('t12_t2', length=2, delay_cost=1)
	S += t12_t2 >= 32
	t12_t2 += MAS[5]

	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	S += t18_t2_in >= 32
	t18_t2_in += MM_in[0]

	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	S += t18_t2_mem0 >= 32
	t18_t2_mem0 += MAS_MEM[4]

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	S += t18_t2_mem1 >= 32
	t18_t2_mem1 += MAS_MEM[5]

	new_TX_t3 = S.Task('new_TX_t3', length=2, delay_cost=1)
	S += new_TX_t3 >= 33
	new_TX_t3 += MAS[2]

	t12_t0 = S.Task('t12_t0', length=9, delay_cost=1)
	S += t12_t0 >= 33
	t12_t0 += MM[1]

	t12_t4_in = S.Task('t12_t4_in', length=1, delay_cost=1)
	S += t12_t4_in >= 33
	t12_t4_in += MM_in[1]

	t12_t4_mem0 = S.Task('t12_t4_mem0', length=1, delay_cost=1)
	S += t12_t4_mem0 >= 33
	t12_t4_mem0 += MAS_MEM[10]

	t12_t4_mem1 = S.Task('t12_t4_mem1', length=1, delay_cost=1)
	S += t12_t4_mem1 >= 33
	t12_t4_mem1 += MAS_MEM[11]

	t18_t2 = S.Task('t18_t2', length=9, delay_cost=1)
	S += t18_t2 >= 33
	t18_t2 += MM[0]

	t12_t4 = S.Task('t12_t4', length=9, delay_cost=1)
	S += t12_t4 >= 34
	t12_t4 += MM[1]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 34
	t2_t5_in += MAS_in[2]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 34
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 34
	t2_t5_mem1 += MM_MEM[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 35
	c200_w += MAIN_MEM_w

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 35
	t20_in += MAS_in[2]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 35
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 35
	t20_mem1 += MM_MEM[1]

	t2_t5 = S.Task('t2_t5', length=2, delay_cost=1)
	S += t2_t5 >= 35
	t2_t5 += MAS[2]

	t20 = S.Task('t20', length=2, delay_cost=1)
	S += t20 >= 36
	t20 += MAS[2]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 36
	t21_in += MAS_in[4]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 36
	t21_mem0 += MM_MEM[2]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 36
	t21_mem1 += MAS_MEM[5]

	t18_t5_in = S.Task('t18_t5_in', length=1, delay_cost=1)
	S += t18_t5_in >= 37
	t18_t5_in += MAS_in[2]

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	S += t18_t5_mem0 >= 37
	t18_t5_mem0 += MM_MEM[0]

	t18_t5_mem1 = S.Task('t18_t5_mem1', length=1, delay_cost=1)
	S += t18_t5_mem1 >= 37
	t18_t5_mem1 += MM_MEM[1]

	t21 = S.Task('t21', length=2, delay_cost=1)
	S += t21 >= 37
	t21 += MAS[4]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 37
	t30_in += MAS_in[3]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 37
	t30_mem0 += MAS_MEM[4]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 37
	t30_mem1 += MAS_MEM[5]

	t181_in = S.Task('t181_in', length=1, delay_cost=1)
	S += t181_in >= 38
	t181_in += MAS_in[3]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 38
	t181_mem0 += MM_MEM[0]

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	S += t181_mem1 >= 38
	t181_mem1 += MM_MEM[1]

	t18_t5 = S.Task('t18_t5', length=2, delay_cost=1)
	S += t18_t5 >= 38
	t18_t5 += MAS[2]

	t30 = S.Task('t30', length=2, delay_cost=1)
	S += t30 >= 38
	t30 += MAS[3]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 38
	t31_in += MAS_in[2]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 38
	t31_mem0 += MAS_MEM[8]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 38
	t31_mem1 += MAS_MEM[9]

	t181 = S.Task('t181', length=2, delay_cost=1)
	S += t181 >= 39
	t181 += MAS[3]

	t31 = S.Task('t31', length=2, delay_cost=1)
	S += t31 >= 39
	t31 += MAS[2]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 39
	t40_in += MAS_in[5]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 39
	t40_mem0 += MAS_MEM[6]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 39
	t40_mem1 += MAS_MEM[5]

	t40 = S.Task('t40', length=2, delay_cost=1)
	S += t40 >= 40
	t40 += MAS[5]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 40
	t41_in += MAS_in[0]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 40
	t41_mem0 += MAS_MEM[4]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 40
	t41_mem1 += MAS_MEM[9]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 41
	c000_in += MAS_in[2]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 41
	c000_mem0 += MAS_MEM[8]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 41
	c000_mem1 += MAS_MEM[11]

	t12_t5_in = S.Task('t12_t5_in', length=1, delay_cost=1)
	S += t12_t5_in >= 41
	t12_t5_in += MAS_in[1]

	t12_t5_mem0 = S.Task('t12_t5_mem0', length=1, delay_cost=1)
	S += t12_t5_mem0 >= 41
	t12_t5_mem0 += MM_MEM[2]

	t12_t5_mem1 = S.Task('t12_t5_mem1', length=1, delay_cost=1)
	S += t12_t5_mem1 >= 41
	t12_t5_mem1 += MM_MEM[3]

	t180_in = S.Task('t180_in', length=1, delay_cost=1)
	S += t180_in >= 41
	t180_in += MAS_in[5]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 41
	t180_mem0 += MM_MEM[0]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 41
	t180_mem1 += MAS_MEM[5]

	t41 = S.Task('t41', length=2, delay_cost=1)
	S += t41 >= 41
	t41 += MAS[0]

	c000 = S.Task('c000', length=2, delay_cost=1)
	S += c000 >= 42
	c000 += MAS[2]

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 42
	c001_in += MAS_in[0]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 42
	c001_mem0 += MAS_MEM[8]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 42
	c001_mem1 += MAS_MEM[1]

	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	S += t120_in >= 42
	t120_in += MAS_in[1]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 42
	t120_mem0 += MM_MEM[2]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 42
	t120_mem1 += MM_MEM[3]

	t12_t5 = S.Task('t12_t5', length=2, delay_cost=1)
	S += t12_t5 >= 42
	t12_t5 += MAS[1]

	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	S += t140_in >= 42
	t140_in += MAS_in[3]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 42
	t140_mem0 += MAS_MEM[10]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 42
	t140_mem1 += MAS_MEM[11]

	t180 = S.Task('t180', length=2, delay_cost=1)
	S += t180 >= 42
	t180 += MAS[5]

	c001 = S.Task('c001', length=2, delay_cost=1)
	S += c001 >= 43
	c001 += MAS[0]

	t120 = S.Task('t120', length=2, delay_cost=1)
	S += t120 >= 43
	t120 += MAS[1]

	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	S += t121_in >= 43
	t121_in += MAS_in[5]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 43
	t121_mem0 += MM_MEM[2]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 43
	t121_mem1 += MAS_MEM[3]

	t140 = S.Task('t140', length=2, delay_cost=1)
	S += t140 >= 43
	t140 += MAS[3]

	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	S += t141_in >= 43
	t141_in += MAS_in[1]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 43
	t141_mem0 += MAS_MEM[0]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 43
	t141_mem1 += MAS_MEM[1]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 43
	t160_in += MAS_in[4]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 43
	t160_mem0 += MAS_MEM[8]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 43
	t160_mem1 += MAS_MEM[5]

	b30_in = S.Task('b30_in', length=1, delay_cost=1)
	S += b30_in >= 44
	b30_in += MAS_in[5]

	b30_mem0 = S.Task('b30_mem0', length=1, delay_cost=1)
	S += b30_mem0 >= 44
	b30_mem0 += MAS_MEM[6]

	b30_mem1 = S.Task('b30_mem1', length=1, delay_cost=1)
	S += b30_mem1 >= 44
	b30_mem1 += MAS_MEM[11]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 44
	c000_w += MAIN_MEM_w

	t121 = S.Task('t121', length=2, delay_cost=1)
	S += t121 >= 44
	t121 += MAS[5]

	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	S += t130_in >= 44
	t130_in += MAS_in[2]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 44
	t130_mem0 += MAS_MEM[2]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 44
	t130_mem1 += MAS_MEM[3]

	t141 = S.Task('t141', length=2, delay_cost=1)
	S += t141 >= 44
	t141 += MAS[1]

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 44
	t150_in += MAS_in[1]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 44
	t150_mem0 += MAS_MEM[4]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 44
	t150_mem1 += MAS_MEM[7]

	t160 = S.Task('t160', length=2, delay_cost=1)
	S += t160 >= 44
	t160 += MAS[4]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 44
	t161_in += MAS_in[3]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 44
	t161_mem0 += MAS_MEM[8]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 44
	t161_mem1 += MAS_MEM[1]

	b30 = S.Task('b30', length=2, delay_cost=1)
	S += b30 >= 45
	b30 += MAS[5]

	b31_in = S.Task('b31_in', length=1, delay_cost=1)
	S += b31_in >= 45
	b31_in += MAS_in[4]

	b31_mem0 = S.Task('b31_mem0', length=1, delay_cost=1)
	S += b31_mem0 >= 45
	b31_mem0 += MAS_MEM[2]

	b31_mem1 = S.Task('b31_mem1', length=1, delay_cost=1)
	S += b31_mem1 >= 45
	b31_mem1 += MAS_MEM[1]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 45
	c001_w += MAIN_MEM_w

	t130 = S.Task('t130', length=2, delay_cost=1)
	S += t130 >= 45
	t130 += MAS[2]

	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	S += t131_in >= 45
	t131_in += MAS_in[0]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 45
	t131_mem0 += MAS_MEM[10]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 45
	t131_mem1 += MAS_MEM[11]

	t150 = S.Task('t150', length=2, delay_cost=1)
	S += t150 >= 45
	t150 += MAS[1]

	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	S += t151_in >= 45
	t151_in += MAS_in[2]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 45
	t151_mem0 += MAS_MEM[0]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 45
	t151_mem1 += MAS_MEM[3]

	t161 = S.Task('t161', length=2, delay_cost=1)
	S += t161 >= 45
	t161 += MAS[3]

	b31 = S.Task('b31', length=2, delay_cost=1)
	S += b31 >= 46
	b31 += MAS[4]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 46
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 46
	new_TX_t0_mem0 += MAS_MEM[2]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 46
	new_TX_t0_mem1 += MAS_MEM[3]

	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	S += new_TZ0_in >= 46
	new_TZ0_in += MAS_in[2]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 46
	new_TZ0_mem0 += MAS_MEM[4]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 46
	new_TZ0_mem1 += MAS_MEM[5]

	t131 = S.Task('t131', length=2, delay_cost=1)
	S += t131 >= 46
	t131 += MAS[0]

	t151 = S.Task('t151', length=2, delay_cost=1)
	S += t151 >= 46
	t151 += MAS[2]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 46
	t17_t0_in += MM_in[1]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 46
	t17_t0_mem0 += MAS_MEM[10]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 46
	t17_t0_mem1 += MAS_MEM[9]

	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	S += t17_t3_in >= 46
	t17_t3_in += MAS_in[5]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 46
	t17_t3_mem0 += MAS_MEM[8]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 46
	t17_t3_mem1 += MAS_MEM[7]

	new_TX_t0 = S.Task('new_TX_t0', length=9, delay_cost=1)
	S += new_TX_t0 >= 47
	new_TX_t0 += MM[0]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 47
	new_TX_t1_in += MM_in[1]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 47
	new_TX_t1_mem0 += MAS_MEM[4]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 47
	new_TX_t1_mem1 += MAS_MEM[11]

	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	S += new_TX_t2_in >= 47
	new_TX_t2_in += MAS_in[3]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 47
	new_TX_t2_mem0 += MAS_MEM[2]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 47
	new_TX_t2_mem1 += MAS_MEM[5]

	new_TZ0 = S.Task('new_TZ0', length=2, delay_cost=1)
	S += new_TZ0 >= 47
	new_TZ0 += MAS[2]

	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	S += new_TZ1_in >= 47
	new_TZ1_in += MAS_in[2]

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 47
	new_TZ1_mem0 += MAS_MEM[0]

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	S += new_TZ1_mem1 >= 47
	new_TZ1_mem1 += MAS_MEM[1]

	t17_t0 = S.Task('t17_t0', length=9, delay_cost=1)
	S += t17_t0 >= 47
	t17_t0 += MM[1]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 47
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 47
	t17_t1_mem0 += MAS_MEM[8]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 47
	t17_t1_mem1 += MAS_MEM[7]

	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	S += t17_t2_in >= 47
	t17_t2_in += MAS_in[1]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 47
	t17_t2_mem0 += MAS_MEM[10]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 47
	t17_t2_mem1 += MAS_MEM[9]

	t17_t3 = S.Task('t17_t3', length=2, delay_cost=1)
	S += t17_t3 >= 47
	t17_t3 += MAS[5]

	new_TX_t1 = S.Task('new_TX_t1', length=9, delay_cost=1)
	S += new_TX_t1 >= 48
	new_TX_t1 += MM[1]

	new_TX_t2 = S.Task('new_TX_t2', length=2, delay_cost=1)
	S += new_TX_t2 >= 48
	new_TX_t2 += MAS[3]

	new_TZ1 = S.Task('new_TZ1', length=2, delay_cost=1)
	S += new_TZ1 >= 48
	new_TZ1 += MAS[2]

	t17_t1 = S.Task('t17_t1', length=9, delay_cost=1)
	S += t17_t1 >= 48
	t17_t1 += MM[0]

	t17_t2 = S.Task('t17_t2', length=2, delay_cost=1)
	S += t17_t2 >= 48
	t17_t2 += MAS[1]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 49
	new_TX_t4_in += MM_in[1]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 49
	new_TX_t4_mem0 += MAS_MEM[6]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 49
	new_TX_t4_mem1 += MAS_MEM[5]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 49
	new_TZ0_w += MAIN_MEM_w

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 49
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 49
	t17_t4_mem0 += MAS_MEM[2]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 49
	t17_t4_mem1 += MAS_MEM[11]

	new_TX_t4 = S.Task('new_TX_t4', length=9, delay_cost=1)
	S += new_TX_t4 >= 50
	new_TX_t4 += MM[1]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 50
	new_TZ1_w += MAIN_MEM_w

	t17_t4 = S.Task('t17_t4', length=9, delay_cost=1)
	S += t17_t4 >= 50
	t17_t4 += MM[0]

	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	S += new_TX_t5_in >= 56
	new_TX_t5_in += MAS_in[1]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 56
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 56
	new_TX_t5_mem1 += MM_MEM[3]

	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	S += new_TX0_in >= 57
	new_TX0_in += MAS_in[5]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 57
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 57
	new_TX0_mem1 += MM_MEM[3]

	new_TX_t5 = S.Task('new_TX_t5', length=2, delay_cost=1)
	S += new_TX_t5 >= 57
	new_TX_t5 += MAS[1]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 57
	t170_in += MAS_in[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 57
	t170_mem0 += MM_MEM[2]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 57
	t170_mem1 += MM_MEM[1]

	new_TX0 = S.Task('new_TX0', length=2, delay_cost=1)
	S += new_TX0 >= 58
	new_TX0 += MAS[5]

	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	S += new_TX1_in >= 58
	new_TX1_in += MAS_in[0]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 58
	new_TX1_mem0 += MM_MEM[2]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 58
	new_TX1_mem1 += MAS_MEM[3]

	t170 = S.Task('t170', length=2, delay_cost=1)
	S += t170 >= 58
	t170 += MAS[0]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 58
	t171_in += MAS_in[3]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 58
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 58
	t171_mem1 += MAS_MEM[1]

	new_TX1 = S.Task('new_TX1', length=2, delay_cost=1)
	S += new_TX1 >= 59
	new_TX1 += MAS[0]

	new_TY0_in = S.Task('new_TY0_in', length=1, delay_cost=1)
	S += new_TY0_in >= 59
	new_TY0_in += MAS_in[0]

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	S += new_TY0_mem0 >= 59
	new_TY0_mem0 += MAS_MEM[0]

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	S += new_TY0_mem1 >= 59
	new_TY0_mem1 += MAS_MEM[11]

	t171 = S.Task('t171', length=2, delay_cost=1)
	S += t171 >= 59
	t171 += MAS[3]

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 60
	new_TX0_w += MAIN_MEM_w

	new_TY0 = S.Task('new_TY0', length=2, delay_cost=1)
	S += new_TY0 >= 60
	new_TY0 += MAS[0]

	new_TY1_in = S.Task('new_TY1_in', length=1, delay_cost=1)
	S += new_TY1_in >= 60
	new_TY1_in += MAS_in[2]

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	S += new_TY1_mem0 >= 60
	new_TY1_mem0 += MAS_MEM[6]

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	S += new_TY1_mem1 >= 60
	new_TY1_mem1 += MAS_MEM[7]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 61
	new_TX1_w += MAIN_MEM_w

	new_TY1 = S.Task('new_TY1', length=2, delay_cost=1)
	S += new_TY1 >= 61
	new_TY1 += MAS[2]

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	S += new_TY0_w >= 62
	new_TY0_w += MAIN_MEM_w

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	S += new_TY1_w >= 63
	new_TY1_w += MAIN_MEM_w


	# new tasks
	t17_t5 = S.Task('t17_t5', length=2, delay_cost=1)
	t17_t5 += alt(MAS)
	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	t17_t5_in += alt(MAS_in)
	S += t17_t5_in*MAS_in[0]<=t17_t5*MAS[0]

	S += t17_t5_in*MAS_in[1]<=t17_t5*MAS[1]

	S += t17_t5_in*MAS_in[2]<=t17_t5*MAS[2]

	S += t17_t5_in*MAS_in[3]<=t17_t5*MAS[3]

	S += t17_t5_in*MAS_in[4]<=t17_t5*MAS[4]

	S += t17_t5_in*MAS_in[5]<=t17_t5*MAS[5]

	S += t17_t5<59

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	t17_t5_mem0 += MM_MEM[2]
	S += 55 < t17_t5_mem0
	S += t17_t5_mem0 <= t17_t5

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	t17_t5_mem1 += MM_MEM[1]
	S += 56 < t17_t5_mem1
	S += t17_t5_mem1 <= t17_t5

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM2_stage2MAS6/EP2_DBL_w_EVAL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

