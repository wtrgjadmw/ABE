from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 174
	S = Scenario("schedule2", horizon=horizon)

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
	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 0
	t7_t0_in += MAS_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 0
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 0
	t7_t0_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=3, delay_cost=1)
	S += t7_t0 >= 1
	t7_t0 += MAS[0]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 1
	t7_t3_in += MM_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 1
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 1
	t7_t3_mem1 += MAIN_MEM_r[1]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 2
	t10_t1_in += MM_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 2
	t10_t1_mem0 += MAIN_MEM_r[0]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 2
	t10_t1_mem1 += MAIN_MEM_r[1]

	t7_t3 = S.Task('t7_t3', length=11, delay_cost=1)
	S += t7_t3 >= 2
	t7_t3 += MM[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 3
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 3
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 3
	t0_t3_mem1 += MAIN_MEM_r[1]

	t10_t1 = S.Task('t10_t1', length=11, delay_cost=1)
	S += t10_t1 >= 3
	t10_t1 += MM[0]

	t0_t3 = S.Task('t0_t3', length=11, delay_cost=1)
	S += t0_t3 >= 4
	t0_t3 += MM[0]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 4
	t5_t0_in += MM_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 4
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 4
	t5_t0_mem1 += MAIN_MEM_r[1]

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 5
	t10_t0_in += MM_in[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 5
	t10_t0_mem0 += MAIN_MEM_r[0]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 5
	t10_t0_mem1 += MAIN_MEM_r[1]

	t5_t0 = S.Task('t5_t0', length=11, delay_cost=1)
	S += t5_t0 >= 5
	t5_t0 += MM[0]

	t10_t0 = S.Task('t10_t0', length=11, delay_cost=1)
	S += t10_t0 >= 6
	t10_t0 += MM[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 6
	t7_t1_in += MAS_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 6
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 6
	t7_t1_mem1 += MAIN_MEM_r[1]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 7
	t1_t3_in += MM_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 7
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 7
	t1_t3_mem1 += MAIN_MEM_r[1]

	t7_t1 = S.Task('t7_t1', length=3, delay_cost=1)
	S += t7_t1 >= 7
	t7_t1 += MAS[0]

	t1_t3 = S.Task('t1_t3', length=11, delay_cost=1)
	S += t1_t3 >= 8
	t1_t3 += MM[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 8
	t5_t2_in += MAS_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 8
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 8
	t5_t2_mem1 += MAIN_MEM_r[1]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 9
	t1_t1_in += MAS_in[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 9
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 9
	t1_t1_mem1 += MAIN_MEM_r[1]

	t5_t2 = S.Task('t5_t2', length=3, delay_cost=1)
	S += t5_t2 >= 9
	t5_t2 += MAS[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 9
	t7_t2_in += MM_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 9
	t7_t2_mem0 += MAS_MEM[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 9
	t7_t2_mem1 += MAS_MEM[1]

	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	S += t10_t2_in >= 10
	t10_t2_in += MAS_in[0]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 10
	t10_t2_mem0 += MAIN_MEM_r[0]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 10
	t10_t2_mem1 += MAIN_MEM_r[1]

	t1_t1 = S.Task('t1_t1', length=3, delay_cost=1)
	S += t1_t1 >= 10
	t1_t1 += MAS[0]

	t7_t2 = S.Task('t7_t2', length=11, delay_cost=1)
	S += t7_t2 >= 10
	t7_t2 += MM[0]

	t10_t2 = S.Task('t10_t2', length=3, delay_cost=1)
	S += t10_t2 >= 11
	t10_t2 += MAS[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 11
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 11
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 11
	t5_t1_mem1 += MAIN_MEM_r[1]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 12
	t1_t0_in += MAS_in[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 12
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 12
	t1_t0_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=11, delay_cost=1)
	S += t5_t1 >= 12
	t5_t1 += MM[0]

	t1_t0 = S.Task('t1_t0', length=3, delay_cost=1)
	S += t1_t0 >= 13
	t1_t0 += MAS[0]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 13
	t2_t2_in += MAS_in[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 13
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 13
	t2_t2_mem1 += MAIN_MEM_r[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 14
	t0_t0_in += MAS_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 14
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 14
	t0_t0_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=3, delay_cost=1)
	S += t2_t2 >= 14
	t2_t2 += MAS[0]

	t0_t0 = S.Task('t0_t0', length=3, delay_cost=1)
	S += t0_t0 >= 15
	t0_t0 += MAS[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 15
	t0_t1_in += MAS_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 15
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 15
	t0_t1_mem1 += MAIN_MEM_r[1]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 15
	t1_t2_in += MM_in[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 15
	t1_t2_mem0 += MAS_MEM[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 15
	t1_t2_mem1 += MAS_MEM[1]

	t0_t1 = S.Task('t0_t1', length=3, delay_cost=1)
	S += t0_t1 >= 16
	t0_t1 += MAS[0]

	t1_t2 = S.Task('t1_t2', length=11, delay_cost=1)
	S += t1_t2 >= 16
	t1_t2 += MM[0]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 16
	t5_t3_in += MAS_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 16
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 16
	t5_t3_mem1 += MAIN_MEM_r[1]

	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	S += t10_t3_in >= 17
	t10_t3_in += MAS_in[0]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 17
	t10_t3_mem0 += MAIN_MEM_r[0]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 17
	t10_t3_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=3, delay_cost=1)
	S += t5_t3 >= 17
	t5_t3 += MAS[0]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 18
	t0_t2_in += MM_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 18
	t0_t2_mem0 += MAS_MEM[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 18
	t0_t2_mem1 += MAS_MEM[1]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 18
	t100_in += MAS_in[0]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 18
	t100_mem0 += MM_MEM[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 18
	t100_mem1 += MM_MEM[1]

	t10_t3 = S.Task('t10_t3', length=3, delay_cost=1)
	S += t10_t3 >= 18
	t10_t3 += MAS[0]

	t0_t2 = S.Task('t0_t2', length=11, delay_cost=1)
	S += t0_t2 >= 19
	t0_t2 += MM[0]

	t100 = S.Task('t100', length=3, delay_cost=1)
	S += t100 >= 19
	t100 += MAS[0]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 19
	t5_t4_in += MM_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 19
	t5_t4_mem0 += MAS_MEM[0]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 19
	t5_t4_mem1 += MAS_MEM[1]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 19
	t71_in += MAS_in[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 19
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 19
	t71_mem1 += MM_MEM[1]

	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	S += t10_t4_in >= 20
	t10_t4_in += MM_in[0]

	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	S += t10_t4_mem0 >= 20
	t10_t4_mem0 += MAS_MEM[0]

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	S += t10_t4_mem1 >= 20
	t10_t4_mem1 += MAS_MEM[1]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 20
	t11_in += MAS_in[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 20
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 20
	t11_mem1 += MM_MEM[1]

	t5_t4 = S.Task('t5_t4', length=11, delay_cost=1)
	S += t5_t4 >= 20
	t5_t4 += MM[0]

	t71 = S.Task('t71', length=3, delay_cost=1)
	S += t71 >= 20
	t71 += MAS[0]

	t10_t4 = S.Task('t10_t4', length=11, delay_cost=1)
	S += t10_t4 >= 21
	t10_t4 += MM[0]

	t11 = S.Task('t11', length=3, delay_cost=1)
	S += t11 >= 21
	t11 += MAS[0]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 21
	t110_in += MAS_in[0]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 21
	t110_mem0 += MAS_MEM[0]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 21
	t110_mem1 += MAS_MEM[1]

	t110 = S.Task('t110', length=3, delay_cost=1)
	S += t110 >= 22
	t110 += MAS[0]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 22
	t81_in += MAS_in[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 22
	t81_mem0 += MAS_MEM[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 22
	t81_mem1 += MAS_MEM[1]

	t1_t5_in = S.Task('t1_t5_in', length=1, delay_cost=1)
	S += t1_t5_in >= 23
	t1_t5_in += MAS_in[0]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 23
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 23
	t1_t5_mem1 += MM_MEM[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 23
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 23
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 23
	t2_t1_mem1 += MAS_MEM[1]

	t81 = S.Task('t81', length=3, delay_cost=1)
	S += t81 >= 23
	t81 += MAS[0]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 24
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 24
	c010_mem0 += MAS_MEM[0]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 24
	c010_mem1 += MAIN_MEM_r[1]

	t1_t5 = S.Task('t1_t5', length=3, delay_cost=1)
	S += t1_t5 >= 24
	t1_t5 += MAS[0]

	t2_t1 = S.Task('t2_t1', length=11, delay_cost=1)
	S += t2_t1 >= 24
	t2_t1 += MM[0]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 24
	t7_t5_in += MAS_in[0]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 24
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 24
	t7_t5_mem1 += MM_MEM[1]

	c010 = S.Task('c010', length=11, delay_cost=1)
	S += c010 >= 25
	c010 += MM[0]

	t7_t5 = S.Task('t7_t5', length=3, delay_cost=1)
	S += t7_t5 >= 25
	t7_t5 += MAS[0]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 25
	t91_in += MAS_in[0]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 25
	t91_mem0 += MAS_MEM[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 25
	t91_mem1 += MAS_MEM[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 26
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 26
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 26
	t10_mem1 += MAS_MEM[1]

	t91 = S.Task('t91', length=3, delay_cost=1)
	S += t91 >= 26
	t91 += MAS[0]

	t10 = S.Task('t10', length=3, delay_cost=1)
	S += t10 >= 27
	t10 += MAS[0]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 27
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 27
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 27
	t70_mem1 += MAS_MEM[1]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 28
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 28
	c201_mem0 += MAS_MEM[0]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 28
	c201_mem1 += MAIN_MEM_r[1]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 28
	t0_t5_in += MAS_in[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 28
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 28
	t0_t5_mem1 += MM_MEM[1]

	t70 = S.Task('t70', length=3, delay_cost=1)
	S += t70 >= 28
	t70 += MAS[0]

	c201 = S.Task('c201', length=11, delay_cost=1)
	S += c201 >= 29
	c201 += MM[0]

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	S += t0_t5 >= 29
	t0_t5 += MAS[0]

	t10_t5_in = S.Task('t10_t5_in', length=1, delay_cost=1)
	S += t10_t5_in >= 29
	t10_t5_in += MAS_in[0]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 29
	t10_t5_mem0 += MM_MEM[0]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 29
	t10_t5_mem1 += MM_MEM[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 29
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 29
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 29
	t2_t0_mem1 += MAS_MEM[1]

	t10_t5 = S.Task('t10_t5', length=3, delay_cost=1)
	S += t10_t5 >= 30
	t10_t5 += MAS[0]

	t2_t0 = S.Task('t2_t0', length=11, delay_cost=1)
	S += t2_t0 >= 30
	t2_t0 += MM[0]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 30
	t2_t3_in += MAS_in[0]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 30
	t2_t3_mem0 += MAS_MEM[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 30
	t2_t3_mem1 += MAS_MEM[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 31
	t00_in += MAS_in[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 31
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 31
	t00_mem1 += MAS_MEM[1]

	t2_t3 = S.Task('t2_t3', length=3, delay_cost=1)
	S += t2_t3 >= 31
	t2_t3 += MAS[0]

	t00 = S.Task('t00', length=3, delay_cost=1)
	S += t00 >= 32
	t00 += MAS[0]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 32
	t101_in += MAS_in[0]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 32
	t101_mem0 += MM_MEM[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 32
	t101_mem1 += MAS_MEM[1]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 33
	t01_in += MAS_in[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 33
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 33
	t01_mem1 += MM_MEM[1]

	t101 = S.Task('t101', length=3, delay_cost=1)
	S += t101 >= 33
	t101 += MAS[0]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 33
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 33
	t2_t4_mem0 += MAS_MEM[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 33
	t2_t4_mem1 += MAS_MEM[1]

	t01 = S.Task('t01', length=3, delay_cost=1)
	S += t01 >= 34
	t01 += MAS[0]

	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	S += t12_t0_in >= 34
	t12_t0_in += MM_in[0]

	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	S += t12_t0_mem0 >= 34
	t12_t0_mem0 += MAS_MEM[0]

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	S += t12_t0_mem1 >= 34
	t12_t0_mem1 += MAS_MEM[1]

	t2_t4 = S.Task('t2_t4', length=11, delay_cost=1)
	S += t2_t4 >= 34
	t2_t4 += MM[0]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 34
	t5_t5_in += MAS_in[0]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 34
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 34
	t5_t5_mem1 += MM_MEM[1]

	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	S += t111_in >= 35
	t111_in += MAS_in[0]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 35
	t111_mem0 += MAS_MEM[0]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 35
	t111_mem1 += MAS_MEM[1]

	t12_t0 = S.Task('t12_t0', length=11, delay_cost=1)
	S += t12_t0 >= 35
	t12_t0 += MM[0]

	t5_t5 = S.Task('t5_t5', length=3, delay_cost=1)
	S += t5_t5 >= 35
	t5_t5 += MAS[0]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 36
	c010_w += MAIN_MEM_w

	t111 = S.Task('t111', length=3, delay_cost=1)
	S += t111 >= 36
	t111 += MAS[0]

	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	S += t18_t3_in >= 36
	t18_t3_in += MM_in[0]

	t18_t3_mem0 = S.Task('t18_t3_mem0', length=1, delay_cost=1)
	S += t18_t3_mem0 >= 36
	t18_t3_mem0 += MAS_MEM[0]

	t18_t3_mem1 = S.Task('t18_t3_mem1', length=1, delay_cost=1)
	S += t18_t3_mem1 >= 36
	t18_t3_mem1 += MAS_MEM[1]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 36
	t50_in += MAS_in[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 36
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 36
	t50_mem1 += MM_MEM[1]

	t18_t0_in = S.Task('t18_t0_in', length=1, delay_cost=1)
	S += t18_t0_in >= 37
	t18_t0_in += MAS_in[0]

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	S += t18_t0_mem0 >= 37
	t18_t0_mem0 += MAS_MEM[0]

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	S += t18_t0_mem1 >= 37
	t18_t0_mem1 += MAS_MEM[1]

	t18_t3 = S.Task('t18_t3', length=11, delay_cost=1)
	S += t18_t3 >= 37
	t18_t3 += MM[0]

	t50 = S.Task('t50', length=3, delay_cost=1)
	S += t50 >= 37
	t50 += MAS[0]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 38
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 38
	c011_mem0 += MAS_MEM[0]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 38
	c011_mem1 += MAIN_MEM_r[1]

	t18_t0 = S.Task('t18_t0', length=3, delay_cost=1)
	S += t18_t0 >= 38
	t18_t0 += MAS[0]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 38
	t51_in += MAS_in[0]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 38
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 38
	t51_mem1 += MAS_MEM[1]

	c011 = S.Task('c011', length=11, delay_cost=1)
	S += c011 >= 39
	c011 += MM[0]

	t18_t1_in = S.Task('t18_t1_in', length=1, delay_cost=1)
	S += t18_t1_in >= 39
	t18_t1_in += MAS_in[0]

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	S += t18_t1_mem0 >= 39
	t18_t1_mem0 += MAS_MEM[0]

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	S += t18_t1_mem1 >= 39
	t18_t1_mem1 += MAS_MEM[1]

	t51 = S.Task('t51', length=3, delay_cost=1)
	S += t51 >= 39
	t51 += MAS[0]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 40
	c201_w += MAIN_MEM_w

	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	S += t12_t1_in >= 40
	t12_t1_in += MM_in[0]

	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	S += t12_t1_mem0 >= 40
	t12_t1_mem0 += MAS_MEM[0]

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	S += t12_t1_mem1 >= 40
	t12_t1_mem1 += MAS_MEM[1]

	t18_t1 = S.Task('t18_t1', length=3, delay_cost=1)
	S += t18_t1 >= 40
	t18_t1 += MAS[0]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 40
	t20_in += MAS_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 40
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 40
	t20_mem1 += MM_MEM[1]

	t12_t1 = S.Task('t12_t1', length=11, delay_cost=1)
	S += t12_t1 >= 41
	t12_t1 += MM[0]

	t20 = S.Task('t20', length=3, delay_cost=1)
	S += t20 >= 41
	t20 += MAS[0]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 41
	t80_in += MAS_in[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 41
	t80_mem0 += MAS_MEM[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 41
	t80_mem1 += MAS_MEM[1]

	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	S += t18_t2_in >= 42
	t18_t2_in += MM_in[0]

	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	S += t18_t2_mem0 >= 42
	t18_t2_mem0 += MAS_MEM[0]

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	S += t18_t2_mem1 >= 42
	t18_t2_mem1 += MAS_MEM[1]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 42
	t2_t5_in += MAS_in[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 42
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 42
	t2_t5_mem1 += MM_MEM[1]

	t80 = S.Task('t80', length=3, delay_cost=1)
	S += t80 >= 42
	t80 += MAS[0]

	t18_t2 = S.Task('t18_t2', length=11, delay_cost=1)
	S += t18_t2 >= 43
	t18_t2 += MM[0]

	t2_t5 = S.Task('t2_t5', length=3, delay_cost=1)
	S += t2_t5 >= 43
	t2_t5 += MAS[0]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 43
	t61_in += MAS_in[0]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 43
	t61_mem0 += MAS_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 43
	t61_mem1 += MAS_MEM[1]

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 44
	t60_in += MAS_in[0]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 44
	t60_mem0 += MAS_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 44
	t60_mem1 += MAS_MEM[1]

	t61 = S.Task('t61', length=3, delay_cost=1)
	S += t61 >= 44
	t61 += MAS[0]

	t12_t3_in = S.Task('t12_t3_in', length=1, delay_cost=1)
	S += t12_t3_in >= 45
	t12_t3_in += MAS_in[0]

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	S += t12_t3_mem0 >= 45
	t12_t3_mem0 += MAS_MEM[0]

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	S += t12_t3_mem1 >= 45
	t12_t3_mem1 += MAS_MEM[1]

	t60 = S.Task('t60', length=3, delay_cost=1)
	S += t60 >= 45
	t60 += MAS[0]

	t12_t2_in = S.Task('t12_t2_in', length=1, delay_cost=1)
	S += t12_t2_in >= 46
	t12_t2_in += MAS_in[0]

	t12_t2_mem0 = S.Task('t12_t2_mem0', length=1, delay_cost=1)
	S += t12_t2_mem0 >= 46
	t12_t2_mem0 += MAS_MEM[0]

	t12_t2_mem1 = S.Task('t12_t2_mem1', length=1, delay_cost=1)
	S += t12_t2_mem1 >= 46
	t12_t2_mem1 += MAS_MEM[1]

	t12_t3 = S.Task('t12_t3', length=3, delay_cost=1)
	S += t12_t3 >= 46
	t12_t3 += MAS[0]

	t12_t2 = S.Task('t12_t2', length=3, delay_cost=1)
	S += t12_t2 >= 47
	t12_t2 += MAS[0]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 47
	t90_in += MAS_in[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 47
	t90_mem0 += MAS_MEM[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 47
	t90_mem1 += MAS_MEM[1]

	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	S += new_TX_t3_in >= 48
	new_TX_t3_in += MAS_in[0]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 48
	new_TX_t3_mem0 += MAS_MEM[0]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 48
	new_TX_t3_mem1 += MAS_MEM[1]

	t90 = S.Task('t90', length=3, delay_cost=1)
	S += t90 >= 48
	t90 += MAS[0]

	new_TX_t3 = S.Task('new_TX_t3', length=3, delay_cost=1)
	S += new_TX_t3 >= 49
	new_TX_t3 += MAS[0]

	t18_t5_in = S.Task('t18_t5_in', length=1, delay_cost=1)
	S += t18_t5_in >= 49
	t18_t5_in += MAS_in[0]

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	S += t18_t5_mem0 >= 49
	t18_t5_mem0 += MM_MEM[0]

	t18_t5_mem1 = S.Task('t18_t5_mem1', length=1, delay_cost=1)
	S += t18_t5_mem1 >= 49
	t18_t5_mem1 += MM_MEM[1]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 50
	c011_w += MAIN_MEM_w

	t181_in = S.Task('t181_in', length=1, delay_cost=1)
	S += t181_in >= 50
	t181_in += MAS_in[0]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 50
	t181_mem0 += MM_MEM[0]

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	S += t181_mem1 >= 50
	t181_mem1 += MM_MEM[1]

	t18_t5 = S.Task('t18_t5', length=3, delay_cost=1)
	S += t18_t5 >= 50
	t18_t5 += MAS[0]

	t181 = S.Task('t181', length=3, delay_cost=1)
	S += t181 >= 51
	t181 += MAS[0]


	# new tasks
	t21 = S.Task('t21', length=3, delay_cost=1)
	t21 += alt(MAS)
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	t21_in += alt(MAS_in)
	S += t21_in*MAS_in[0]<=t21*MAS[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MM_MEM[0]
	S += 44 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAS_MEM[1]
	S += 45 < t21_mem1
	S += t21_mem1 <= t21

	t30 = S.Task('t30', length=3, delay_cost=1)
	t30 += alt(MAS)
	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	t30_in += alt(MAS_in)
	S += t30_in*MAS_in[0]<=t30*MAS[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MAS_MEM[0]
	S += 43 < t30_mem0
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += MAS_MEM[1]
	S += 43 < t30_mem1
	S += t30_mem1 <= t30

	t12_t4 = S.Task('t12_t4', length=11, delay_cost=1)
	t12_t4 += alt(MM)
	t12_t4_in = S.Task('t12_t4_in', length=1, delay_cost=1)
	t12_t4_in += alt(MM_in)
	S += t12_t4_in*MM_in[0]<=t12_t4*MM[0]
	t12_t4_mem0 = S.Task('t12_t4_mem0', length=1, delay_cost=1)
	t12_t4_mem0 += MAS_MEM[0]
	S += 49 < t12_t4_mem0
	S += t12_t4_mem0 <= t12_t4

	t12_t4_mem1 = S.Task('t12_t4_mem1', length=1, delay_cost=1)
	t12_t4_mem1 += MAS_MEM[1]
	S += 48 < t12_t4_mem1
	S += t12_t4_mem1 <= t12_t4

	t120 = S.Task('t120', length=3, delay_cost=1)
	t120 += alt(MAS)
	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	t120_in += alt(MAS_in)
	S += t120_in*MAS_in[0]<=t120*MAS[0]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += MM_MEM[0]
	S += 45 < t120_mem0
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += MM_MEM[1]
	S += 51 < t120_mem1
	S += t120_mem1 <= t120

	t12_t5 = S.Task('t12_t5', length=3, delay_cost=1)
	t12_t5 += alt(MAS)
	t12_t5_in = S.Task('t12_t5_in', length=1, delay_cost=1)
	t12_t5_in += alt(MAS_in)
	S += t12_t5_in*MAS_in[0]<=t12_t5*MAS[0]

	t12_t5_mem0 = S.Task('t12_t5_mem0', length=1, delay_cost=1)
	t12_t5_mem0 += MM_MEM[0]
	S += 45 < t12_t5_mem0
	S += t12_t5_mem0 <= t12_t5

	t12_t5_mem1 = S.Task('t12_t5_mem1', length=1, delay_cost=1)
	t12_t5_mem1 += MM_MEM[1]
	S += 51 < t12_t5_mem1
	S += t12_t5_mem1 <= t12_t5

	t180 = S.Task('t180', length=3, delay_cost=1)
	t180 += alt(MAS)
	t180_in = S.Task('t180_in', length=1, delay_cost=1)
	t180_in += alt(MAS_in)
	S += t180_in*MAS_in[0]<=t180*MAS[0]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	t180_mem0 += MM_MEM[0]
	S += 53 < t180_mem0
	S += t180_mem0 <= t180

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	t180_mem1 += MAS_MEM[1]
	S += 52 < t180_mem1
	S += t180_mem1 <= t180

	c200 = S.Task('c200', length=11, delay_cost=1)
	c200 += alt(MM)
	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MM_in)
	S += c200_in*MM_in[0]<=c200*MM[0]
	S += 0<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += MAS_MEM[0]
	S += 50 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAIN_MEM_r[1]
	S += c200_mem1 <= c200

	t31 = S.Task('t31', length=3, delay_cost=1)
	t31 += alt(MAS)
	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	t31_in += alt(MAS_in)
	S += t31_in*MAS_in[0]<=t31*MAS[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t31_mem0*MAS_MEM[0]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t31_mem1*MAS_MEM[1]
	S += t31_mem1 <= t31

	t40 = S.Task('t40', length=3, delay_cost=1)
	t40 += alt(MAS)
	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	t40_in += alt(MAS_in)
	S += t40_in*MAS_in[0]<=t40*MAS[0]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	t40_mem0 += alt(MAS_MEM)
	S += (t30*MAS[0])-1 < t40_mem0*MAS_MEM[0]
	S += t40_mem0 <= t40

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	t40_mem1 += MAS_MEM[1]
	S += 43 < t40_mem1
	S += t40_mem1 <= t40

	t121 = S.Task('t121', length=3, delay_cost=1)
	t121 += alt(MAS)
	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	t121_in += alt(MAS_in)
	S += t121_in*MAS_in[0]<=t121*MAS[0]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	t121_mem0 += alt(MM_MEM)
	S += (t12_t4*MM[0])-1 < t121_mem0*MM_MEM[0]
	S += t121_mem0 <= t121

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	t121_mem1 += alt(MAS_MEM)
	S += (t12_t5*MAS[0])-1 < t121_mem1*MAS_MEM[1]
	S += t121_mem1 <= t121

	t130 = S.Task('t130', length=3, delay_cost=1)
	t130 += alt(MAS)
	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	t130_in += alt(MAS_in)
	S += t130_in*MAS_in[0]<=t130*MAS[0]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	t130_mem0 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t130_mem0*MAS_MEM[0]
	S += t130_mem0 <= t130

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	t130_mem1 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t130_mem1*MAS_MEM[1]
	S += t130_mem1 <= t130

	t41 = S.Task('t41', length=3, delay_cost=1)
	t41 += alt(MAS)
	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	t41_in += alt(MAS_in)
	S += t41_in*MAS_in[0]<=t41*MAS[0]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	t41_mem0 += alt(MAS_MEM)
	S += (t31*MAS[0])-1 < t41_mem0*MAS_MEM[0]
	S += t41_mem0 <= t41

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	t41_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t41_mem1*MAS_MEM[1]
	S += t41_mem1 <= t41

	t131 = S.Task('t131', length=3, delay_cost=1)
	t131 += alt(MAS)
	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	t131_in += alt(MAS_in)
	S += t131_in*MAS_in[0]<=t131*MAS[0]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += alt(MAS_MEM)
	S += (t121*MAS[0])-1 < t131_mem0*MAS_MEM[0]
	S += t131_mem0 <= t131

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	t131_mem1 += alt(MAS_MEM)
	S += (t121*MAS[0])-1 < t131_mem1*MAS_MEM[1]
	S += t131_mem1 <= t131

	new_TZ0 = S.Task('new_TZ0', length=3, delay_cost=1)
	new_TZ0 += alt(MAS)
	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	new_TZ0_in += alt(MAS_in)
	S += new_TZ0_in*MAS_in[0]<=new_TZ0*MAS[0]

	S += 18<new_TZ0

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	new_TZ0_w += alt(MAIN_MEM_w)
	S += new_TZ0 <= new_TZ0_w

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	new_TZ0_mem0 += alt(MAS_MEM)
	S += (t130*MAS[0])-1 < new_TZ0_mem0*MAS_MEM[0]
	S += new_TZ0_mem0 <= new_TZ0

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	new_TZ0_mem1 += alt(MAS_MEM)
	S += (t130*MAS[0])-1 < new_TZ0_mem1*MAS_MEM[1]
	S += new_TZ0_mem1 <= new_TZ0

	c000 = S.Task('c000', length=3, delay_cost=1)
	c000 += alt(MAS)
	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	c000_in += alt(MAS_in)
	S += c000_in*MAS_in[0]<=c000*MAS[0]

	S += 0<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[0]
	S += 34 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += c000_mem1 <= c000

	t140 = S.Task('t140', length=3, delay_cost=1)
	t140 += alt(MAS)
	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	t140_in += alt(MAS_in)
	S += t140_in*MAS_in[0]<=t140*MAS[0]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < t140_mem0*MAS_MEM[0]
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < t140_mem1*MAS_MEM[1]
	S += t140_mem1 <= t140

	new_TZ1 = S.Task('new_TZ1', length=3, delay_cost=1)
	new_TZ1 += alt(MAS)
	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	new_TZ1_in += alt(MAS_in)
	S += new_TZ1_in*MAS_in[0]<=new_TZ1*MAS[0]

	S += 18<new_TZ1

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	new_TZ1_w += alt(MAIN_MEM_w)
	S += new_TZ1 <= new_TZ1_w

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	new_TZ1_mem0 += alt(MAS_MEM)
	S += (t131*MAS[0])-1 < new_TZ1_mem0*MAS_MEM[0]
	S += new_TZ1_mem0 <= new_TZ1

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	new_TZ1_mem1 += alt(MAS_MEM)
	S += (t131*MAS[0])-1 < new_TZ1_mem1*MAS_MEM[1]
	S += new_TZ1_mem1 <= new_TZ1

	c001 = S.Task('c001', length=3, delay_cost=1)
	c001 += alt(MAS)
	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	c001_in += alt(MAS_in)
	S += c001_in*MAS_in[0]<=c001*MAS[0]

	S += 0<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[0]
	S += 36 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += c001_mem1 <= c001

	t141 = S.Task('t141', length=3, delay_cost=1)
	t141 += alt(MAS)
	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	t141_in += alt(MAS_in)
	S += t141_in*MAS_in[0]<=t141*MAS[0]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < t141_mem0*MAS_MEM[0]
	S += t141_mem0 <= t141

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	t141_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < t141_mem1*MAS_MEM[1]
	S += t141_mem1 <= t141

	t150 = S.Task('t150', length=3, delay_cost=1)
	t150 += alt(MAS)
	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	t150_in += alt(MAS_in)
	S += t150_in*MAS_in[0]<=t150*MAS[0]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += alt(MAS_MEM)
	S += (c000*MAS[0])-1 < t150_mem0*MAS_MEM[0]
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < t150_mem1*MAS_MEM[1]
	S += t150_mem1 <= t150

	t160 = S.Task('t160', length=3, delay_cost=1)
	t160 += alt(MAS)
	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	t160_in += alt(MAS_in)
	S += t160_in*MAS_in[0]<=t160*MAS[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += MAS_MEM[0]
	S += 34 < t160_mem0
	S += t160_mem0 <= t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(MAS_MEM)
	S += (c000*MAS[0])-1 < t160_mem1*MAS_MEM[1]
	S += t160_mem1 <= t160

	b30 = S.Task('b30', length=3, delay_cost=1)
	b30 += alt(MAS)
	b30_in = S.Task('b30_in', length=1, delay_cost=1)
	b30_in += alt(MAS_in)
	S += b30_in*MAS_in[0]<=b30*MAS[0]

	b30_mem0 = S.Task('b30_mem0', length=1, delay_cost=1)
	b30_mem0 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < b30_mem0*MAS_MEM[0]
	S += b30_mem0 <= b30

	b30_mem1 = S.Task('b30_mem1', length=1, delay_cost=1)
	b30_mem1 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < b30_mem1*MAS_MEM[1]
	S += b30_mem1 <= b30

	t151 = S.Task('t151', length=3, delay_cost=1)
	t151 += alt(MAS)
	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	t151_in += alt(MAS_in)
	S += t151_in*MAS_in[0]<=t151*MAS[0]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += alt(MAS_MEM)
	S += (c001*MAS[0])-1 < t151_mem0*MAS_MEM[0]
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < t151_mem1*MAS_MEM[1]
	S += t151_mem1 <= t151

	new_TX_t0 = S.Task('new_TX_t0', length=11, delay_cost=1)
	new_TX_t0 += alt(MM)
	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	new_TX_t0_in += alt(MM_in)
	S += new_TX_t0_in*MM_in[0]<=new_TX_t0*MM[0]
	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	new_TX_t0_mem0 += alt(MAS_MEM)
	S += (t150*MAS[0])-1 < new_TX_t0_mem0*MAS_MEM[0]
	S += new_TX_t0_mem0 <= new_TX_t0

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	new_TX_t0_mem1 += MAS_MEM[1]
	S += 47 < new_TX_t0_mem1
	S += new_TX_t0_mem1 <= new_TX_t0

	t161 = S.Task('t161', length=3, delay_cost=1)
	t161 += alt(MAS)
	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	t161_in += alt(MAS_in)
	S += t161_in*MAS_in[0]<=t161*MAS[0]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += MAS_MEM[0]
	S += 36 < t161_mem0
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += alt(MAS_MEM)
	S += (c001*MAS[0])-1 < t161_mem1*MAS_MEM[1]
	S += t161_mem1 <= t161

	b31 = S.Task('b31', length=3, delay_cost=1)
	b31 += alt(MAS)
	b31_in = S.Task('b31_in', length=1, delay_cost=1)
	b31_in += alt(MAS_in)
	S += b31_in*MAS_in[0]<=b31*MAS[0]

	b31_mem0 = S.Task('b31_mem0', length=1, delay_cost=1)
	b31_mem0 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < b31_mem0*MAS_MEM[0]
	S += b31_mem0 <= b31

	b31_mem1 = S.Task('b31_mem1', length=1, delay_cost=1)
	b31_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < b31_mem1*MAS_MEM[1]
	S += b31_mem1 <= b31

	t17_t0 = S.Task('t17_t0', length=11, delay_cost=1)
	t17_t0 += alt(MM)
	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	t17_t0_in += alt(MM_in)
	S += t17_t0_in*MM_in[0]<=t17_t0*MM[0]
	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	t17_t0_mem0 += alt(MAS_MEM)
	S += (b30*MAS[0])-1 < t17_t0_mem0*MAS_MEM[0]
	S += t17_t0_mem0 <= t17_t0

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	t17_t0_mem1 += alt(MAS_MEM)
	S += (t160*MAS[0])-1 < t17_t0_mem1*MAS_MEM[1]
	S += t17_t0_mem1 <= t17_t0

	new_TX_t1 = S.Task('new_TX_t1', length=11, delay_cost=1)
	new_TX_t1 += alt(MM)
	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	new_TX_t1_in += alt(MM_in)
	S += new_TX_t1_in*MM_in[0]<=new_TX_t1*MM[0]
	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	new_TX_t1_mem0 += alt(MAS_MEM)
	S += (t151*MAS[0])-1 < new_TX_t1_mem0*MAS_MEM[0]
	S += new_TX_t1_mem0 <= new_TX_t1

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	new_TX_t1_mem1 += MAS_MEM[1]
	S += 46 < new_TX_t1_mem1
	S += new_TX_t1_mem1 <= new_TX_t1

	new_TX_t2 = S.Task('new_TX_t2', length=3, delay_cost=1)
	new_TX_t2 += alt(MAS)
	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	new_TX_t2_in += alt(MAS_in)
	S += new_TX_t2_in*MAS_in[0]<=new_TX_t2*MAS[0]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	new_TX_t2_mem0 += alt(MAS_MEM)
	S += (t150*MAS[0])-1 < new_TX_t2_mem0*MAS_MEM[0]
	S += new_TX_t2_mem0 <= new_TX_t2

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	new_TX_t2_mem1 += alt(MAS_MEM)
	S += (t151*MAS[0])-1 < new_TX_t2_mem1*MAS_MEM[1]
	S += new_TX_t2_mem1 <= new_TX_t2

	t17_t1 = S.Task('t17_t1', length=11, delay_cost=1)
	t17_t1 += alt(MM)
	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	t17_t1_in += alt(MM_in)
	S += t17_t1_in*MM_in[0]<=t17_t1*MM[0]
	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	t17_t1_mem0 += alt(MAS_MEM)
	S += (b31*MAS[0])-1 < t17_t1_mem0*MAS_MEM[0]
	S += t17_t1_mem0 <= t17_t1

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	t17_t1_mem1 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < t17_t1_mem1*MAS_MEM[1]
	S += t17_t1_mem1 <= t17_t1

	t17_t2 = S.Task('t17_t2', length=3, delay_cost=1)
	t17_t2 += alt(MAS)
	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	t17_t2_in += alt(MAS_in)
	S += t17_t2_in*MAS_in[0]<=t17_t2*MAS[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	t17_t2_mem0 += alt(MAS_MEM)
	S += (b30*MAS[0])-1 < t17_t2_mem0*MAS_MEM[0]
	S += t17_t2_mem0 <= t17_t2

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	t17_t2_mem1 += alt(MAS_MEM)
	S += (b31*MAS[0])-1 < t17_t2_mem1*MAS_MEM[1]
	S += t17_t2_mem1 <= t17_t2

	t17_t3 = S.Task('t17_t3', length=3, delay_cost=1)
	t17_t3 += alt(MAS)
	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	t17_t3_in += alt(MAS_in)
	S += t17_t3_in*MAS_in[0]<=t17_t3*MAS[0]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	t17_t3_mem0 += alt(MAS_MEM)
	S += (t160*MAS[0])-1 < t17_t3_mem0*MAS_MEM[0]
	S += t17_t3_mem0 <= t17_t3

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	t17_t3_mem1 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < t17_t3_mem1*MAS_MEM[1]
	S += t17_t3_mem1 <= t17_t3

	new_TX_t4 = S.Task('new_TX_t4', length=11, delay_cost=1)
	new_TX_t4 += alt(MM)
	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	new_TX_t4_in += alt(MM_in)
	S += new_TX_t4_in*MM_in[0]<=new_TX_t4*MM[0]
	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	new_TX_t4_mem0 += alt(MAS_MEM)
	S += (new_TX_t2*MAS[0])-1 < new_TX_t4_mem0*MAS_MEM[0]
	S += new_TX_t4_mem0 <= new_TX_t4

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	new_TX_t4_mem1 += MAS_MEM[1]
	S += 51 < new_TX_t4_mem1
	S += new_TX_t4_mem1 <= new_TX_t4

	new_TX0 = S.Task('new_TX0', length=3, delay_cost=1)
	new_TX0 += alt(MAS)
	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	new_TX0_in += alt(MAS_in)
	S += new_TX0_in*MAS_in[0]<=new_TX0*MAS[0]

	S += 9<new_TX0

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	new_TX0_w += alt(MAIN_MEM_w)
	S += new_TX0 <= new_TX0_w

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	new_TX0_mem0 += alt(MM_MEM)
	S += (new_TX_t0*MM[0])-1 < new_TX0_mem0*MM_MEM[0]
	S += new_TX0_mem0 <= new_TX0

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	new_TX0_mem1 += alt(MM_MEM)
	S += (new_TX_t1*MM[0])-1 < new_TX0_mem1*MM_MEM[1]
	S += new_TX0_mem1 <= new_TX0

	new_TX_t5 = S.Task('new_TX_t5', length=3, delay_cost=1)
	new_TX_t5 += alt(MAS)
	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	new_TX_t5_in += alt(MAS_in)
	S += new_TX_t5_in*MAS_in[0]<=new_TX_t5*MAS[0]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	new_TX_t5_mem0 += alt(MM_MEM)
	S += (new_TX_t0*MM[0])-1 < new_TX_t5_mem0*MM_MEM[0]
	S += new_TX_t5_mem0 <= new_TX_t5

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	new_TX_t5_mem1 += alt(MM_MEM)
	S += (new_TX_t1*MM[0])-1 < new_TX_t5_mem1*MM_MEM[1]
	S += new_TX_t5_mem1 <= new_TX_t5

	t17_t4 = S.Task('t17_t4', length=11, delay_cost=1)
	t17_t4 += alt(MM)
	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	t17_t4_in += alt(MM_in)
	S += t17_t4_in*MM_in[0]<=t17_t4*MM[0]
	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	t17_t4_mem0 += alt(MAS_MEM)
	S += (t17_t2*MAS[0])-1 < t17_t4_mem0*MAS_MEM[0]
	S += t17_t4_mem0 <= t17_t4

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	t17_t4_mem1 += alt(MAS_MEM)
	S += (t17_t3*MAS[0])-1 < t17_t4_mem1*MAS_MEM[1]
	S += t17_t4_mem1 <= t17_t4

	t170 = S.Task('t170', length=3, delay_cost=1)
	t170 += alt(MAS)
	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	t170_in += alt(MAS_in)
	S += t170_in*MAS_in[0]<=t170*MAS[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += alt(MM_MEM)
	S += (t17_t0*MM[0])-1 < t170_mem0*MM_MEM[0]
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(MM_MEM)
	S += (t17_t1*MM[0])-1 < t170_mem1*MM_MEM[1]
	S += t170_mem1 <= t170

	t17_t5 = S.Task('t17_t5', length=3, delay_cost=1)
	t17_t5 += alt(MAS)
	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	t17_t5_in += alt(MAS_in)
	S += t17_t5_in*MAS_in[0]<=t17_t5*MAS[0]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	t17_t5_mem0 += alt(MM_MEM)
	S += (t17_t0*MM[0])-1 < t17_t5_mem0*MM_MEM[0]
	S += t17_t5_mem0 <= t17_t5

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	t17_t5_mem1 += alt(MM_MEM)
	S += (t17_t1*MM[0])-1 < t17_t5_mem1*MM_MEM[1]
	S += t17_t5_mem1 <= t17_t5

	new_TX1 = S.Task('new_TX1', length=3, delay_cost=1)
	new_TX1 += alt(MAS)
	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	new_TX1_in += alt(MAS_in)
	S += new_TX1_in*MAS_in[0]<=new_TX1*MAS[0]

	S += 12<new_TX1

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	new_TX1_w += alt(MAIN_MEM_w)
	S += new_TX1 <= new_TX1_w

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	new_TX1_mem0 += alt(MM_MEM)
	S += (new_TX_t4*MM[0])-1 < new_TX1_mem0*MM_MEM[0]
	S += new_TX1_mem0 <= new_TX1

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	new_TX1_mem1 += alt(MAS_MEM)
	S += (new_TX_t5*MAS[0])-1 < new_TX1_mem1*MAS_MEM[1]
	S += new_TX1_mem1 <= new_TX1

	t171 = S.Task('t171', length=3, delay_cost=1)
	t171 += alt(MAS)
	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	t171_in += alt(MAS_in)
	S += t171_in*MAS_in[0]<=t171*MAS[0]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(MM_MEM)
	S += (t17_t4*MM[0])-1 < t171_mem0*MM_MEM[0]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += alt(MAS_MEM)
	S += (t17_t5*MAS[0])-1 < t171_mem1*MAS_MEM[1]
	S += t171_mem1 <= t171

	new_TY0 = S.Task('new_TY0', length=3, delay_cost=1)
	new_TY0 += alt(MAS)
	new_TY0_in = S.Task('new_TY0_in', length=1, delay_cost=1)
	new_TY0_in += alt(MAS_in)
	S += new_TY0_in*MAS_in[0]<=new_TY0*MAS[0]

	S += 17<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += alt(MAS_MEM)
	S += (t170*MAS[0])-1 < new_TY0_mem0*MAS_MEM[0]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += alt(MAS_MEM)
	S += (t180*MAS[0])-1 < new_TY0_mem1*MAS_MEM[1]
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=3, delay_cost=1)
	new_TY1 += alt(MAS)
	new_TY1_in = S.Task('new_TY1_in', length=1, delay_cost=1)
	new_TY1_in += alt(MAS_in)
	S += new_TY1_in*MAS_in[0]<=new_TY1*MAS[0]

	S += 17<new_TY1

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	new_TY1_w += alt(MAIN_MEM_w)
	S += new_TY1 <= new_TY1_w

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	new_TY1_mem0 += alt(MAS_MEM)
	S += (t171*MAS[0])-1 < new_TY1_mem0*MAS_MEM[0]
	S += new_TY1_mem0 <= new_TY1

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	new_TY1_mem1 += MAS_MEM[1]
	S += 53 < new_TY1_mem1
	S += new_TY1_mem1 <= new_TY1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS1/EP2_DBL_w_EVAL/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution

