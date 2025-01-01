from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 257
	S = Scenario("schedule5", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=14)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=1, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t4_t50_in = S.Task('t4_t50_in', length=1, delay_cost=1)
	S += t4_t50_in >= 0
	t4_t50_in += MAS_in[0]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 0
	t4_t50_mem0 += MAIN_MEM_r[0]

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 0
	t4_t50_mem1 += MAIN_MEM_r[1]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 1
	t1_t2_in += MAS_in[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 1
	t1_t2_mem0 += MAIN_MEM_r[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 1
	t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t50 = S.Task('t4_t50', length=3, delay_cost=1)
	S += t4_t50 >= 1
	t4_t50 += MAS[0]

	t1_t2 = S.Task('t1_t2', length=3, delay_cost=1)
	S += t1_t2 >= 2
	t1_t2 += MAS[0]

	t4_t2_t2_in = S.Task('t4_t2_t2_in', length=1, delay_cost=1)
	S += t4_t2_t2_in >= 2
	t4_t2_t2_in += MAS_in[0]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 2
	t4_t2_t2_mem0 += MAIN_MEM_r[0]

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 2
	t4_t2_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_in >= 3
	t4_t0_t1_in += MM_in[0]

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_mem0 >= 3
	t4_t0_t1_mem0 += MAIN_MEM_r[0]

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_mem1 >= 3
	t4_t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t2 = S.Task('t4_t2_t2', length=3, delay_cost=1)
	S += t4_t2_t2 >= 3
	t4_t2_t2 += MAS[0]

	t4_t0_t1 = S.Task('t4_t0_t1', length=14, delay_cost=1)
	S += t4_t0_t1 >= 4
	t4_t0_t1 += MM[0]

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	S += t4_t2_t0_in >= 4
	t4_t2_t0_in += MM_in[0]

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	S += t4_t2_t0_mem0 >= 4
	t4_t2_t0_mem0 += MAIN_MEM_r[0]

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	S += t4_t2_t0_mem1 >= 4
	t4_t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 5
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 5
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 5
	t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t0 = S.Task('t4_t2_t0', length=14, delay_cost=1)
	S += t4_t2_t0 >= 5
	t4_t2_t0 += MM[0]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 6
	t1_t0_in += MM_in[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 6
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 6
	t1_t0_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=14, delay_cost=1)
	S += t2_t1 >= 6
	t2_t1 += MM[0]

	t1_t0 = S.Task('t1_t0', length=14, delay_cost=1)
	S += t1_t0 >= 7
	t1_t0 += MM[0]

	t4_t0_t2_in = S.Task('t4_t0_t2_in', length=1, delay_cost=1)
	S += t4_t0_t2_in >= 7
	t4_t0_t2_in += MAS_in[0]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 7
	t4_t0_t2_mem0 += MAIN_MEM_r[0]

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 7
	t4_t0_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_t2 = S.Task('t4_t0_t2', length=3, delay_cost=1)
	S += t4_t0_t2 >= 8
	t4_t0_t2 += MAS[0]

	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_in >= 8
	t4_t1_t0_in += MM_in[0]

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_mem0 >= 8
	t4_t1_t0_mem0 += MAIN_MEM_r[0]

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_mem1 >= 8
	t4_t1_t0_mem1 += MAIN_MEM_r[1]

	t4_t1_t0 = S.Task('t4_t1_t0', length=14, delay_cost=1)
	S += t4_t1_t0 >= 9
	t4_t1_t0 += MM[0]

	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	S += t4_t8_t0_in >= 9
	t4_t8_t0_in += MM_in[0]

	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	S += t4_t8_t0_mem0 >= 9
	t4_t8_t0_mem0 += MAIN_MEM_r[0]

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	S += t4_t8_t0_mem1 >= 9
	t4_t8_t0_mem1 += MAIN_MEM_r[1]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 10
	t2_t2_in += MAS_in[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 10
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 10
	t2_t2_mem1 += MAIN_MEM_r[1]

	t4_t8_t0 = S.Task('t4_t8_t0', length=14, delay_cost=1)
	S += t4_t8_t0 >= 10
	t4_t8_t0 += MM[0]

	t2_t2 = S.Task('t2_t2', length=3, delay_cost=1)
	S += t2_t2 >= 11
	t2_t2 += MAS[0]

	t4_t0_t3_in = S.Task('t4_t0_t3_in', length=1, delay_cost=1)
	S += t4_t0_t3_in >= 11
	t4_t0_t3_in += MAS_in[0]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 11
	t4_t0_t3_mem0 += MAIN_MEM_r[0]

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 11
	t4_t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t0_t3 = S.Task('t4_t0_t3', length=3, delay_cost=1)
	S += t4_t0_t3 >= 12
	t4_t0_t3 += MAS[0]

	t4_t40_in = S.Task('t4_t40_in', length=1, delay_cost=1)
	S += t4_t40_in >= 12
	t4_t40_in += MAS_in[0]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 12
	t4_t40_mem0 += MAIN_MEM_r[0]

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 12
	t4_t40_mem1 += MAIN_MEM_r[1]

	t4_t1_t3_in = S.Task('t4_t1_t3_in', length=1, delay_cost=1)
	S += t4_t1_t3_in >= 13
	t4_t1_t3_in += MAS_in[0]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 13
	t4_t1_t3_mem0 += MAIN_MEM_r[0]

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 13
	t4_t1_t3_mem1 += MAIN_MEM_r[1]

	t4_t40 = S.Task('t4_t40', length=3, delay_cost=1)
	S += t4_t40 >= 13
	t4_t40 += MAS[0]

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_in >= 14
	t4_t0_t0_in += MM_in[0]

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_mem0 >= 14
	t4_t0_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_mem1 >= 14
	t4_t0_t0_mem1 += MAIN_MEM_r[1]

	t4_t1_t3 = S.Task('t4_t1_t3', length=3, delay_cost=1)
	S += t4_t1_t3 >= 14
	t4_t1_t3 += MAS[0]

	t4_t0_t0 = S.Task('t4_t0_t0', length=14, delay_cost=1)
	S += t4_t0_t0 >= 15
	t4_t0_t0 += MM[0]

	t4_t41_in = S.Task('t4_t41_in', length=1, delay_cost=1)
	S += t4_t41_in >= 15
	t4_t41_in += MAS_in[0]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 15
	t4_t41_mem0 += MAIN_MEM_r[0]

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 15
	t4_t41_mem1 += MAIN_MEM_r[1]

	t4_t6_t0_in = S.Task('t4_t6_t0_in', length=1, delay_cost=1)
	S += t4_t6_t0_in >= 15
	t4_t6_t0_in += MM_in[0]

	t4_t6_t0_mem0 = S.Task('t4_t6_t0_mem0', length=1, delay_cost=1)
	S += t4_t6_t0_mem0 >= 15
	t4_t6_t0_mem0 += MAS_MEM[0]

	t4_t6_t0_mem1 = S.Task('t4_t6_t0_mem1', length=1, delay_cost=1)
	S += t4_t6_t0_mem1 >= 15
	t4_t6_t0_mem1 += MAS_MEM[1]

	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_in >= 16
	t4_t1_t1_in += MM_in[0]

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_mem0 >= 16
	t4_t1_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_mem1 >= 16
	t4_t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t41 = S.Task('t4_t41', length=3, delay_cost=1)
	S += t4_t41 >= 16
	t4_t41 += MAS[0]

	t4_t6_t0 = S.Task('t4_t6_t0', length=14, delay_cost=1)
	S += t4_t6_t0 >= 16
	t4_t6_t0 += MM[0]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 17
	t1_t3_in += MAS_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 17
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 17
	t1_t3_mem1 += MAIN_MEM_r[1]

	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	S += t4_t0_t4_in >= 17
	t4_t0_t4_in += MM_in[0]

	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	S += t4_t0_t4_mem0 >= 17
	t4_t0_t4_mem0 += MAS_MEM[0]

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	S += t4_t0_t4_mem1 >= 17
	t4_t0_t4_mem1 += MAS_MEM[1]

	t4_t1_t1 = S.Task('t4_t1_t1', length=14, delay_cost=1)
	S += t4_t1_t1 >= 17
	t4_t1_t1 += MM[0]

	t1_t3 = S.Task('t1_t3', length=3, delay_cost=1)
	S += t1_t3 >= 18
	t1_t3 += MAS[0]

	t4_t0_t4 = S.Task('t4_t0_t4', length=14, delay_cost=1)
	S += t4_t0_t4 >= 18
	t4_t0_t4 += MM[0]

	t4_t6_t2_in = S.Task('t4_t6_t2_in', length=1, delay_cost=1)
	S += t4_t6_t2_in >= 18
	t4_t6_t2_in += MAS_in[0]

	t4_t6_t2_mem0 = S.Task('t4_t6_t2_mem0', length=1, delay_cost=1)
	S += t4_t6_t2_mem0 >= 18
	t4_t6_t2_mem0 += MAS_MEM[0]

	t4_t6_t2_mem1 = S.Task('t4_t6_t2_mem1', length=1, delay_cost=1)
	S += t4_t6_t2_mem1 >= 18
	t4_t6_t2_mem1 += MAS_MEM[1]

	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	S += t4_t8_t1_in >= 18
	t4_t8_t1_in += MM_in[0]

	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	S += t4_t8_t1_mem0 >= 18
	t4_t8_t1_mem0 += MAIN_MEM_r[0]

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	S += t4_t8_t1_mem1 >= 18
	t4_t8_t1_mem1 += MAIN_MEM_r[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 19
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 19
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 19
	t2_t0_mem1 += MAIN_MEM_r[1]

	t4_t6_t2 = S.Task('t4_t6_t2', length=3, delay_cost=1)
	S += t4_t6_t2 >= 19
	t4_t6_t2 += MAS[0]

	t4_t8_t1 = S.Task('t4_t8_t1', length=14, delay_cost=1)
	S += t4_t8_t1 >= 19
	t4_t8_t1 += MM[0]

	t1_t4_in = S.Task('t1_t4_in', length=1, delay_cost=1)
	S += t1_t4_in >= 20
	t1_t4_in += MM_in[0]

	t1_t4_mem0 = S.Task('t1_t4_mem0', length=1, delay_cost=1)
	S += t1_t4_mem0 >= 20
	t1_t4_mem0 += MAS_MEM[0]

	t1_t4_mem1 = S.Task('t1_t4_mem1', length=1, delay_cost=1)
	S += t1_t4_mem1 >= 20
	t1_t4_mem1 += MAS_MEM[1]

	t2_t0 = S.Task('t2_t0', length=14, delay_cost=1)
	S += t2_t0 >= 20
	t2_t0 += MM[0]

	t4_t51_in = S.Task('t4_t51_in', length=1, delay_cost=1)
	S += t4_t51_in >= 20
	t4_t51_in += MAS_in[0]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 20
	t4_t51_mem0 += MAIN_MEM_r[0]

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 20
	t4_t51_mem1 += MAIN_MEM_r[1]

	t1_t4 = S.Task('t1_t4', length=14, delay_cost=1)
	S += t1_t4 >= 21
	t1_t4 += MM[0]

	t4_t2_t3_in = S.Task('t4_t2_t3_in', length=1, delay_cost=1)
	S += t4_t2_t3_in >= 21
	t4_t2_t3_in += MAS_in[0]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 21
	t4_t2_t3_mem0 += MAIN_MEM_r[0]

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 21
	t4_t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t51 = S.Task('t4_t51', length=3, delay_cost=1)
	S += t4_t51 >= 21
	t4_t51 += MAS[0]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 22
	t1_t1_in += MM_in[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 22
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 22
	t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t3 = S.Task('t4_t2_t3', length=3, delay_cost=1)
	S += t4_t2_t3 >= 22
	t4_t2_t3 += MAS[0]

	t1_t1 = S.Task('t1_t1', length=14, delay_cost=1)
	S += t1_t1 >= 23
	t1_t1 += MM[0]

	t4_t1_t2_in = S.Task('t4_t1_t2_in', length=1, delay_cost=1)
	S += t4_t1_t2_in >= 23
	t4_t1_t2_in += MAS_in[0]

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t2_mem0 >= 23
	t4_t1_t2_mem0 += MAIN_MEM_r[0]

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t2_mem1 >= 23
	t4_t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t6_t1_in = S.Task('t4_t6_t1_in', length=1, delay_cost=1)
	S += t4_t6_t1_in >= 23
	t4_t6_t1_in += MM_in[0]

	t4_t6_t1_mem0 = S.Task('t4_t6_t1_mem0', length=1, delay_cost=1)
	S += t4_t6_t1_mem0 >= 23
	t4_t6_t1_mem0 += MAS_MEM[0]

	t4_t6_t1_mem1 = S.Task('t4_t6_t1_mem1', length=1, delay_cost=1)
	S += t4_t6_t1_mem1 >= 23
	t4_t6_t1_mem1 += MAS_MEM[1]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 24
	t2_t3_in += MAS_in[0]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 24
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 24
	t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t1_t2 = S.Task('t4_t1_t2', length=3, delay_cost=1)
	S += t4_t1_t2 >= 24
	t4_t1_t2 += MAS[0]

	t4_t2_t4_in = S.Task('t4_t2_t4_in', length=1, delay_cost=1)
	S += t4_t2_t4_in >= 24
	t4_t2_t4_in += MM_in[0]

	t4_t2_t4_mem0 = S.Task('t4_t2_t4_mem0', length=1, delay_cost=1)
	S += t4_t2_t4_mem0 >= 24
	t4_t2_t4_mem0 += MAS_MEM[0]

	t4_t2_t4_mem1 = S.Task('t4_t2_t4_mem1', length=1, delay_cost=1)
	S += t4_t2_t4_mem1 >= 24
	t4_t2_t4_mem1 += MAS_MEM[1]

	t4_t6_t1 = S.Task('t4_t6_t1', length=14, delay_cost=1)
	S += t4_t6_t1 >= 24
	t4_t6_t1 += MM[0]

	t2_t3 = S.Task('t2_t3', length=3, delay_cost=1)
	S += t2_t3 >= 25
	t2_t3 += MAS[0]

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 25
	t4_t2_t1_in += MM_in[0]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 25
	t4_t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 25
	t4_t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t4 = S.Task('t4_t2_t4', length=14, delay_cost=1)
	S += t4_t2_t4 >= 25
	t4_t2_t4 += MM[0]

	t4_t6_t3_in = S.Task('t4_t6_t3_in', length=1, delay_cost=1)
	S += t4_t6_t3_in >= 25
	t4_t6_t3_in += MAS_in[0]

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	S += t4_t6_t3_mem0 >= 25
	t4_t6_t3_mem0 += MAS_MEM[0]

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	S += t4_t6_t3_mem1 >= 25
	t4_t6_t3_mem1 += MAS_MEM[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 26
	t0_t3_in += MAS_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 26
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 26
	t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	S += t4_t1_t4_in >= 26
	t4_t1_t4_in += MM_in[0]

	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	S += t4_t1_t4_mem0 >= 26
	t4_t1_t4_mem0 += MAS_MEM[0]

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	S += t4_t1_t4_mem1 >= 26
	t4_t1_t4_mem1 += MAS_MEM[1]

	t4_t2_t1 = S.Task('t4_t2_t1', length=14, delay_cost=1)
	S += t4_t2_t1 >= 26
	t4_t2_t1 += MM[0]

	t4_t6_t3 = S.Task('t4_t6_t3', length=3, delay_cost=1)
	S += t4_t6_t3 >= 26
	t4_t6_t3 += MAS[0]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 27
	t0_t2_in += MAS_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 27
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 27
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=3, delay_cost=1)
	S += t0_t3 >= 27
	t0_t3 += MAS[0]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 27
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 27
	t2_t4_mem0 += MAS_MEM[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 27
	t2_t4_mem1 += MAS_MEM[1]

	t4_t1_t4 = S.Task('t4_t1_t4', length=14, delay_cost=1)
	S += t4_t1_t4 >= 27
	t4_t1_t4 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 28
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 28
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 28
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t2 = S.Task('t0_t2', length=3, delay_cost=1)
	S += t0_t2 >= 28
	t0_t2 += MAS[0]

	t2_t4 = S.Task('t2_t4', length=14, delay_cost=1)
	S += t2_t4 >= 28
	t2_t4 += MM[0]

	t4_t0_t5_in = S.Task('t4_t0_t5_in', length=1, delay_cost=1)
	S += t4_t0_t5_in >= 28
	t4_t0_t5_in += MAS_in[0]

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	S += t4_t0_t5_mem0 >= 28
	t4_t0_t5_mem0 += MM_MEM[0]

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	S += t4_t0_t5_mem1 >= 28
	t4_t0_t5_mem1 += MM_MEM[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 29
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 29
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 29
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=14, delay_cost=1)
	S += t0_t1 >= 29
	t0_t1 += MM[0]

	t4_t00_in = S.Task('t4_t00_in', length=1, delay_cost=1)
	S += t4_t00_in >= 29
	t4_t00_in += MAS_in[0]

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	S += t4_t00_mem0 >= 29
	t4_t00_mem0 += MM_MEM[0]

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	S += t4_t00_mem1 >= 29
	t4_t00_mem1 += MM_MEM[1]

	t4_t0_t5 = S.Task('t4_t0_t5', length=3, delay_cost=1)
	S += t4_t0_t5 >= 29
	t4_t0_t5 += MAS[0]

	t0_t0 = S.Task('t0_t0', length=14, delay_cost=1)
	S += t0_t0 >= 30
	t0_t0 += MM[0]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 30
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 30
	t0_t4_mem0 += MAS_MEM[0]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 30
	t0_t4_mem1 += MAS_MEM[1]

	t4_t00 = S.Task('t4_t00', length=3, delay_cost=1)
	S += t4_t00 >= 30
	t4_t00 += MAS[0]

	t4_t8_t2_in = S.Task('t4_t8_t2_in', length=1, delay_cost=1)
	S += t4_t8_t2_in >= 30
	t4_t8_t2_in += MAS_in[0]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 30
	t4_t8_t2_mem0 += MAIN_MEM_r[0]

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 30
	t4_t8_t2_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=14, delay_cost=1)
	S += t0_t4 >= 31
	t0_t4 += MM[0]

	t4_t6_t4_in = S.Task('t4_t6_t4_in', length=1, delay_cost=1)
	S += t4_t6_t4_in >= 31
	t4_t6_t4_in += MM_in[0]

	t4_t6_t4_mem0 = S.Task('t4_t6_t4_mem0', length=1, delay_cost=1)
	S += t4_t6_t4_mem0 >= 31
	t4_t6_t4_mem0 += MAS_MEM[0]

	t4_t6_t4_mem1 = S.Task('t4_t6_t4_mem1', length=1, delay_cost=1)
	S += t4_t6_t4_mem1 >= 31
	t4_t6_t4_mem1 += MAS_MEM[1]

	t4_t8_t2 = S.Task('t4_t8_t2', length=3, delay_cost=1)
	S += t4_t8_t2 >= 31
	t4_t8_t2 += MAS[0]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 31
	t91_in += MAS_in[0]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 31
	t91_mem0 += MAIN_MEM_r[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 31
	t91_mem1 += MAIN_MEM_r[1]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 32
	t101_in += MAS_in[0]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 32
	t101_mem0 += MAIN_MEM_r[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 32
	t101_mem1 += MAIN_MEM_r[1]

	t4_t6_t4 = S.Task('t4_t6_t4', length=14, delay_cost=1)
	S += t4_t6_t4 >= 32
	t4_t6_t4 += MM[0]

	t91 = S.Task('t91', length=3, delay_cost=1)
	S += t91 >= 32
	t91 += MAS[0]

	t101 = S.Task('t101', length=3, delay_cost=1)
	S += t101 >= 33
	t101 += MAS[0]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 33
	t71_in += MAS_in[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 33
	t71_mem0 += MAIN_MEM_r[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 33
	t71_mem1 += MAIN_MEM_r[1]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 34
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 34
	t70_mem0 += MAIN_MEM_r[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 34
	t70_mem1 += MAIN_MEM_r[1]

	t71 = S.Task('t71', length=3, delay_cost=1)
	S += t71 >= 34
	t71 += MAS[0]

	t5_t0_t2_in = S.Task('t5_t0_t2_in', length=1, delay_cost=1)
	S += t5_t0_t2_in >= 35
	t5_t0_t2_in += MAS_in[0]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 35
	t5_t0_t2_mem0 += MAIN_MEM_r[0]

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 35
	t5_t0_t2_mem1 += MAIN_MEM_r[1]

	t70 = S.Task('t70', length=3, delay_cost=1)
	S += t70 >= 35
	t70 += MAS[0]

	t5_t0_t2 = S.Task('t5_t0_t2', length=3, delay_cost=1)
	S += t5_t0_t2 >= 36
	t5_t0_t2 += MAS[0]

	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	S += t5_t2_t1_in >= 36
	t5_t2_t1_in += MM_in[0]

	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	S += t5_t2_t1_mem0 >= 36
	t5_t2_t1_mem0 += MAS_MEM[0]

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	S += t5_t2_t1_mem1 >= 36
	t5_t2_t1_mem1 += MAS_MEM[1]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 36
	t90_in += MAS_in[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 36
	t90_mem0 += MAIN_MEM_r[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 36
	t90_mem1 += MAIN_MEM_r[1]

	t4_t8_t3_in = S.Task('t4_t8_t3_in', length=1, delay_cost=1)
	S += t4_t8_t3_in >= 37
	t4_t8_t3_in += MAS_in[0]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 37
	t4_t8_t3_mem0 += MAIN_MEM_r[0]

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 37
	t4_t8_t3_mem1 += MAIN_MEM_r[1]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 37
	t5_t1_t1_in += MM_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 37
	t5_t1_t1_mem0 += MAS_MEM[0]

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 37
	t5_t1_t1_mem1 += MAS_MEM[1]

	t5_t2_t1 = S.Task('t5_t2_t1', length=14, delay_cost=1)
	S += t5_t2_t1 >= 37
	t5_t2_t1 += MM[0]

	t90 = S.Task('t90', length=3, delay_cost=1)
	S += t90 >= 37
	t90 += MAS[0]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 38
	t100_in += MAS_in[0]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 38
	t100_mem0 += MAIN_MEM_r[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 38
	t100_mem1 += MAIN_MEM_r[1]

	t4_t8_t3 = S.Task('t4_t8_t3', length=3, delay_cost=1)
	S += t4_t8_t3 >= 38
	t4_t8_t3 += MAS[0]

	t5_t1_t1 = S.Task('t5_t1_t1', length=14, delay_cost=1)
	S += t5_t1_t1 >= 38
	t5_t1_t1 += MM[0]

	t100 = S.Task('t100', length=3, delay_cost=1)
	S += t100 >= 39
	t100 += MAS[0]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 39
	t5_t1_t0_in += MM_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 39
	t5_t1_t0_mem0 += MAS_MEM[0]

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 39
	t5_t1_t0_mem1 += MAS_MEM[1]

	t5_t8_t2_in = S.Task('t5_t8_t2_in', length=1, delay_cost=1)
	S += t5_t8_t2_in >= 39
	t5_t8_t2_in += MAS_in[0]

	t5_t8_t2_mem0 = S.Task('t5_t8_t2_mem0', length=1, delay_cost=1)
	S += t5_t8_t2_mem0 >= 39
	t5_t8_t2_mem0 += MAIN_MEM_r[0]

	t5_t8_t2_mem1 = S.Task('t5_t8_t2_mem1', length=1, delay_cost=1)
	S += t5_t8_t2_mem1 >= 39
	t5_t8_t2_mem1 += MAIN_MEM_r[1]

	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	S += t4_t8_t4_in >= 40
	t4_t8_t4_in += MM_in[0]

	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	S += t4_t8_t4_mem0 >= 40
	t4_t8_t4_mem0 += MAS_MEM[0]

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	S += t4_t8_t4_mem1 >= 40
	t4_t8_t4_mem1 += MAS_MEM[1]

	t5_t1_t0 = S.Task('t5_t1_t0', length=14, delay_cost=1)
	S += t5_t1_t0 >= 40
	t5_t1_t0 += MM[0]

	t5_t8_t2 = S.Task('t5_t8_t2', length=3, delay_cost=1)
	S += t5_t8_t2 >= 40
	t5_t8_t2 += MAS[0]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 40
	t81_in += MAS_in[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 40
	t81_mem0 += MAIN_MEM_r[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 40
	t81_mem1 += MAIN_MEM_r[1]

	t4_t8_t4 = S.Task('t4_t8_t4', length=14, delay_cost=1)
	S += t4_t8_t4 >= 41
	t4_t8_t4 += MM[0]

	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	S += t5_t2_t0_in >= 41
	t5_t2_t0_in += MM_in[0]

	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	S += t5_t2_t0_mem0 >= 41
	t5_t2_t0_mem0 += MAS_MEM[0]

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	S += t5_t2_t0_mem1 >= 41
	t5_t2_t0_mem1 += MAS_MEM[1]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 41
	t80_in += MAS_in[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 41
	t80_mem0 += MAIN_MEM_r[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 41
	t80_mem1 += MAIN_MEM_r[1]

	t81 = S.Task('t81', length=3, delay_cost=1)
	S += t81 >= 41
	t81 += MAS[0]

	t4_t80_in = S.Task('t4_t80_in', length=1, delay_cost=1)
	S += t4_t80_in >= 42
	t4_t80_in += MAS_in[0]

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	S += t4_t80_mem0 >= 42
	t4_t80_mem0 += MM_MEM[0]

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	S += t4_t80_mem1 >= 42
	t4_t80_mem1 += MM_MEM[1]

	t5_t2_t0 = S.Task('t5_t2_t0', length=14, delay_cost=1)
	S += t5_t2_t0 >= 42
	t5_t2_t0 += MM[0]

	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	S += t5_t8_t0_in >= 42
	t5_t8_t0_in += MM_in[0]

	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	S += t5_t8_t0_mem0 >= 42
	t5_t8_t0_mem0 += MAIN_MEM_r[0]

	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	S += t5_t8_t0_mem1 >= 42
	t5_t8_t0_mem1 += MAS_MEM[1]

	t80 = S.Task('t80', length=3, delay_cost=1)
	S += t80 >= 42
	t80 += MAS[0]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 43
	t2_t5_in += MAS_in[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 43
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 43
	t2_t5_mem1 += MM_MEM[1]

	t4_t80 = S.Task('t4_t80', length=3, delay_cost=1)
	S += t4_t80 >= 43
	t4_t80 += MAS[0]

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 43
	t5_t0_t1_in += MM_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 43
	t5_t0_t1_mem0 += MAIN_MEM_r[0]

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 43
	t5_t0_t1_mem1 += MAS_MEM[1]

	t5_t8_t0 = S.Task('t5_t8_t0', length=14, delay_cost=1)
	S += t5_t8_t0 >= 43
	t5_t8_t0 += MM[0]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 44
	t20_in += MAS_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 44
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 44
	t20_mem1 += MM_MEM[1]

	t2_t5 = S.Task('t2_t5', length=3, delay_cost=1)
	S += t2_t5 >= 44
	t2_t5 += MAS[0]

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 44
	t5_t0_t0_in += MM_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 44
	t5_t0_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 44
	t5_t0_t0_mem1 += MAS_MEM[1]

	t5_t0_t1 = S.Task('t5_t0_t1', length=14, delay_cost=1)
	S += t5_t0_t1 >= 44
	t5_t0_t1 += MM[0]

	t20 = S.Task('t20', length=3, delay_cost=1)
	S += t20 >= 45
	t20 += MAS[0]

	t4_t10_in = S.Task('t4_t10_in', length=1, delay_cost=1)
	S += t4_t10_in >= 45
	t4_t10_in += MAS_in[0]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 45
	t4_t10_mem0 += MM_MEM[0]

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 45
	t4_t10_mem1 += MM_MEM[1]

	t5_t0_t0 = S.Task('t5_t0_t0', length=14, delay_cost=1)
	S += t5_t0_t0 >= 45
	t5_t0_t0 += MM[0]

	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	S += t5_t8_t1_in >= 45
	t5_t8_t1_in += MM_in[0]

	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	S += t5_t8_t1_mem0 >= 45
	t5_t8_t1_mem0 += MAIN_MEM_r[0]

	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	S += t5_t8_t1_mem1 >= 45
	t5_t8_t1_mem1 += MAS_MEM[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 46
	t00_in += MAS_in[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 46
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 46
	t00_mem1 += MM_MEM[1]

	t4_t10 = S.Task('t4_t10', length=3, delay_cost=1)
	S += t4_t10 >= 46
	t4_t10 += MAS[0]

	t5_t8_t1 = S.Task('t5_t8_t1', length=14, delay_cost=1)
	S += t5_t8_t1 >= 46
	t5_t8_t1 += MM[0]

	t00 = S.Task('t00', length=3, delay_cost=1)
	S += t00 >= 47
	t00 += MAS[0]

	t5_t2_t2_in = S.Task('t5_t2_t2_in', length=1, delay_cost=1)
	S += t5_t2_t2_in >= 47
	t5_t2_t2_in += MAS_in[0]

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_t2_mem0 >= 47
	t5_t2_t2_mem0 += MAS_MEM[0]

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_t2_mem1 >= 47
	t5_t2_t2_mem1 += MAS_MEM[1]

	t4_t2_t5_in = S.Task('t4_t2_t5_in', length=1, delay_cost=1)
	S += t4_t2_t5_in >= 48
	t4_t2_t5_in += MAS_in[0]

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	S += t4_t2_t5_mem0 >= 48
	t4_t2_t5_mem0 += MM_MEM[0]

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	S += t4_t2_t5_mem1 >= 48
	t4_t2_t5_mem1 += MM_MEM[1]

	t5_t2_t2 = S.Task('t5_t2_t2', length=3, delay_cost=1)
	S += t5_t2_t2 >= 48
	t5_t2_t2 += MAS[0]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 49
	t0_t5_in += MAS_in[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 49
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 49
	t0_t5_mem1 += MM_MEM[1]

	t4_t2_t5 = S.Task('t4_t2_t5', length=3, delay_cost=1)
	S += t4_t2_t5 >= 49
	t4_t2_t5 += MAS[0]

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	S += t0_t5 >= 50
	t0_t5 += MAS[0]

	t5_t8_t3_in = S.Task('t5_t8_t3_in', length=1, delay_cost=1)
	S += t5_t8_t3_in >= 50
	t5_t8_t3_in += MAS_in[0]

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	S += t5_t8_t3_mem0 >= 50
	t5_t8_t3_mem0 += MAS_MEM[0]

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	S += t5_t8_t3_mem1 >= 50
	t5_t8_t3_mem1 += MAS_MEM[1]

	t5_t1_t2_in = S.Task('t5_t1_t2_in', length=1, delay_cost=1)
	S += t5_t1_t2_in >= 51
	t5_t1_t2_in += MAS_in[0]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 51
	t5_t1_t2_mem0 += MAS_MEM[0]

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 51
	t5_t1_t2_mem1 += MAS_MEM[1]

	t5_t8_t3 = S.Task('t5_t8_t3', length=3, delay_cost=1)
	S += t5_t8_t3 >= 51
	t5_t8_t3 += MAS[0]

	t5_t0_t3_in = S.Task('t5_t0_t3_in', length=1, delay_cost=1)
	S += t5_t0_t3_in >= 52
	t5_t0_t3_in += MAS_in[0]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 52
	t5_t0_t3_mem0 += MAS_MEM[0]

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 52
	t5_t0_t3_mem1 += MAS_MEM[1]

	t5_t1_t2 = S.Task('t5_t1_t2', length=3, delay_cost=1)
	S += t5_t1_t2 >= 52
	t5_t1_t2 += MAS[0]

	t4_t8_t5_in = S.Task('t4_t8_t5_in', length=1, delay_cost=1)
	S += t4_t8_t5_in >= 53
	t4_t8_t5_in += MAS_in[0]

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	S += t4_t8_t5_mem0 >= 53
	t4_t8_t5_mem0 += MM_MEM[0]

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	S += t4_t8_t5_mem1 >= 53
	t4_t8_t5_mem1 += MM_MEM[1]

	t5_t0_t3 = S.Task('t5_t0_t3', length=3, delay_cost=1)
	S += t5_t0_t3 >= 53
	t5_t0_t3 += MAS[0]

	t5_t8_t4_in = S.Task('t5_t8_t4_in', length=1, delay_cost=1)
	S += t5_t8_t4_in >= 53
	t5_t8_t4_in += MM_in[0]

	t5_t8_t4_mem0 = S.Task('t5_t8_t4_mem0', length=1, delay_cost=1)
	S += t5_t8_t4_mem0 >= 53
	t5_t8_t4_mem0 += MAS_MEM[0]

	t5_t8_t4_mem1 = S.Task('t5_t8_t4_mem1', length=1, delay_cost=1)
	S += t5_t8_t4_mem1 >= 53
	t5_t8_t4_mem1 += MAS_MEM[1]

	t4_t20_in = S.Task('t4_t20_in', length=1, delay_cost=1)
	S += t4_t20_in >= 54
	t4_t20_in += MAS_in[0]

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	S += t4_t20_mem0 >= 54
	t4_t20_mem0 += MM_MEM[0]

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	S += t4_t20_mem1 >= 54
	t4_t20_mem1 += MM_MEM[1]

	t4_t8_t5 = S.Task('t4_t8_t5', length=3, delay_cost=1)
	S += t4_t8_t5 >= 54
	t4_t8_t5 += MAS[0]

	t5_t8_t4 = S.Task('t5_t8_t4', length=14, delay_cost=1)
	S += t5_t8_t4 >= 54
	t5_t8_t4 += MM[0]

	t4_t20 = S.Task('t4_t20', length=3, delay_cost=1)
	S += t4_t20 >= 55
	t4_t20 += MAS[0]

	t5_t50_in = S.Task('t5_t50_in', length=1, delay_cost=1)
	S += t5_t50_in >= 55
	t5_t50_in += MAS_in[0]

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	S += t5_t50_mem0 >= 55
	t5_t50_mem0 += MAS_MEM[0]

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	S += t5_t50_mem1 >= 55
	t5_t50_mem1 += MAS_MEM[1]

	t4_t1_t5_in = S.Task('t4_t1_t5_in', length=1, delay_cost=1)
	S += t4_t1_t5_in >= 56
	t4_t1_t5_in += MAS_in[0]

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	S += t4_t1_t5_mem0 >= 56
	t4_t1_t5_mem0 += MM_MEM[0]

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	S += t4_t1_t5_mem1 >= 56
	t4_t1_t5_mem1 += MM_MEM[1]

	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	S += t5_t0_t4_in >= 56
	t5_t0_t4_in += MM_in[0]

	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	S += t5_t0_t4_mem0 >= 56
	t5_t0_t4_mem0 += MAS_MEM[0]

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	S += t5_t0_t4_mem1 >= 56
	t5_t0_t4_mem1 += MAS_MEM[1]

	t5_t50 = S.Task('t5_t50', length=3, delay_cost=1)
	S += t5_t50 >= 56
	t5_t50 += MAS[0]

	t4_t1_t5 = S.Task('t4_t1_t5', length=3, delay_cost=1)
	S += t4_t1_t5 >= 57
	t4_t1_t5 += MAS[0]

	t5_t0_t4 = S.Task('t5_t0_t4', length=14, delay_cost=1)
	S += t5_t0_t4 >= 57
	t5_t0_t4 += MM[0]

	t5_t51_in = S.Task('t5_t51_in', length=1, delay_cost=1)
	S += t5_t51_in >= 57
	t5_t51_in += MAS_in[0]

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	S += t5_t51_mem0 >= 57
	t5_t51_mem0 += MAS_MEM[0]

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	S += t5_t51_mem1 >= 57
	t5_t51_mem1 += MAS_MEM[1]

	t5_t2_t3_in = S.Task('t5_t2_t3_in', length=1, delay_cost=1)
	S += t5_t2_t3_in >= 58
	t5_t2_t3_in += MAS_in[0]

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	S += t5_t2_t3_mem0 >= 58
	t5_t2_t3_mem0 += MAS_MEM[0]

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	S += t5_t2_t3_mem1 >= 58
	t5_t2_t3_mem1 += MAS_MEM[1]

	t5_t51 = S.Task('t5_t51', length=3, delay_cost=1)
	S += t5_t51 >= 58
	t5_t51 += MAS[0]

	t5_t1_t3_in = S.Task('t5_t1_t3_in', length=1, delay_cost=1)
	S += t5_t1_t3_in >= 59
	t5_t1_t3_in += MAS_in[0]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 59
	t5_t1_t3_mem0 += MAS_MEM[0]

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 59
	t5_t1_t3_mem1 += MAS_MEM[1]

	t5_t2_t3 = S.Task('t5_t2_t3', length=3, delay_cost=1)
	S += t5_t2_t3 >= 59
	t5_t2_t3 += MAS[0]

	t5_t1_t3 = S.Task('t5_t1_t3', length=3, delay_cost=1)
	S += t5_t1_t3 >= 60
	t5_t1_t3 += MAS[0]

	t5_t41_in = S.Task('t5_t41_in', length=1, delay_cost=1)
	S += t5_t41_in >= 60
	t5_t41_in += MAS_in[0]

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	S += t5_t41_mem0 >= 60
	t5_t41_mem0 += MAIN_MEM_r[0]

	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	S += t5_t41_mem1 >= 60
	t5_t41_mem1 += MAS_MEM[1]

	t1_t5_in = S.Task('t1_t5_in', length=1, delay_cost=1)
	S += t1_t5_in >= 61
	t1_t5_in += MAS_in[0]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 61
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 61
	t1_t5_mem1 += MM_MEM[1]

	t5_t2_t4_in = S.Task('t5_t2_t4_in', length=1, delay_cost=1)
	S += t5_t2_t4_in >= 61
	t5_t2_t4_in += MM_in[0]

	t5_t2_t4_mem0 = S.Task('t5_t2_t4_mem0', length=1, delay_cost=1)
	S += t5_t2_t4_mem0 >= 61
	t5_t2_t4_mem0 += MAS_MEM[0]

	t5_t2_t4_mem1 = S.Task('t5_t2_t4_mem1', length=1, delay_cost=1)
	S += t5_t2_t4_mem1 >= 61
	t5_t2_t4_mem1 += MAS_MEM[1]

	t5_t41 = S.Task('t5_t41', length=3, delay_cost=1)
	S += t5_t41 >= 61
	t5_t41 += MAS[0]

	t1_t5 = S.Task('t1_t5', length=3, delay_cost=1)
	S += t1_t5 >= 62
	t1_t5 += MAS[0]

	t5_t2_t4 = S.Task('t5_t2_t4', length=14, delay_cost=1)
	S += t5_t2_t4 >= 62
	t5_t2_t4 += MM[0]

	t5_t40_in = S.Task('t5_t40_in', length=1, delay_cost=1)
	S += t5_t40_in >= 62
	t5_t40_in += MAS_in[0]

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	S += t5_t40_mem0 >= 62
	t5_t40_mem0 += MAIN_MEM_r[0]

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	S += t5_t40_mem1 >= 62
	t5_t40_mem1 += MAS_MEM[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 63
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 63
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 63
	t10_mem1 += MM_MEM[1]

	t5_t40 = S.Task('t5_t40', length=3, delay_cost=1)
	S += t5_t40 >= 63
	t5_t40 += MAS[0]

	t5_t6_t1_in = S.Task('t5_t6_t1_in', length=1, delay_cost=1)
	S += t5_t6_t1_in >= 63
	t5_t6_t1_in += MM_in[0]

	t5_t6_t1_mem0 = S.Task('t5_t6_t1_mem0', length=1, delay_cost=1)
	S += t5_t6_t1_mem0 >= 63
	t5_t6_t1_mem0 += MAS_MEM[0]

	t5_t6_t1_mem1 = S.Task('t5_t6_t1_mem1', length=1, delay_cost=1)
	S += t5_t6_t1_mem1 >= 63
	t5_t6_t1_mem1 += MAS_MEM[1]

	t10 = S.Task('t10', length=3, delay_cost=1)
	S += t10 >= 64
	t10 += MAS[0]

	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	S += t5_t1_t4_in >= 64
	t5_t1_t4_in += MM_in[0]

	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	S += t5_t1_t4_mem0 >= 64
	t5_t1_t4_mem0 += MAS_MEM[0]

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	S += t5_t1_t4_mem1 >= 64
	t5_t1_t4_mem1 += MAS_MEM[1]

	t5_t6_t1 = S.Task('t5_t6_t1', length=14, delay_cost=1)
	S += t5_t6_t1 >= 64
	t5_t6_t1 += MM[0]

	t5_t8_t5_in = S.Task('t5_t8_t5_in', length=1, delay_cost=1)
	S += t5_t8_t5_in >= 64
	t5_t8_t5_in += MAS_in[0]

	t5_t8_t5_mem0 = S.Task('t5_t8_t5_mem0', length=1, delay_cost=1)
	S += t5_t8_t5_mem0 >= 64
	t5_t8_t5_mem0 += MM_MEM[0]

	t5_t8_t5_mem1 = S.Task('t5_t8_t5_mem1', length=1, delay_cost=1)
	S += t5_t8_t5_mem1 >= 64
	t5_t8_t5_mem1 += MM_MEM[1]

	t5_t1_t4 = S.Task('t5_t1_t4', length=14, delay_cost=1)
	S += t5_t1_t4 >= 65
	t5_t1_t4 += MM[0]

	t5_t6_t0_in = S.Task('t5_t6_t0_in', length=1, delay_cost=1)
	S += t5_t6_t0_in >= 65
	t5_t6_t0_in += MM_in[0]

	t5_t6_t0_mem0 = S.Task('t5_t6_t0_mem0', length=1, delay_cost=1)
	S += t5_t6_t0_mem0 >= 65
	t5_t6_t0_mem0 += MAS_MEM[0]

	t5_t6_t0_mem1 = S.Task('t5_t6_t0_mem1', length=1, delay_cost=1)
	S += t5_t6_t0_mem1 >= 65
	t5_t6_t0_mem1 += MAS_MEM[1]

	t5_t80_in = S.Task('t5_t80_in', length=1, delay_cost=1)
	S += t5_t80_in >= 65
	t5_t80_in += MAS_in[0]

	t5_t80_mem0 = S.Task('t5_t80_mem0', length=1, delay_cost=1)
	S += t5_t80_mem0 >= 65
	t5_t80_mem0 += MM_MEM[0]

	t5_t80_mem1 = S.Task('t5_t80_mem1', length=1, delay_cost=1)
	S += t5_t80_mem1 >= 65
	t5_t80_mem1 += MM_MEM[1]

	t5_t8_t5 = S.Task('t5_t8_t5', length=3, delay_cost=1)
	S += t5_t8_t5 >= 65
	t5_t8_t5 += MAS[0]

	t5_t6_t0 = S.Task('t5_t6_t0', length=14, delay_cost=1)
	S += t5_t6_t0 >= 66
	t5_t6_t0 += MM[0]

	t5_t6_t2_in = S.Task('t5_t6_t2_in', length=1, delay_cost=1)
	S += t5_t6_t2_in >= 66
	t5_t6_t2_in += MAS_in[0]

	t5_t6_t2_mem0 = S.Task('t5_t6_t2_mem0', length=1, delay_cost=1)
	S += t5_t6_t2_mem0 >= 66
	t5_t6_t2_mem0 += MAS_MEM[0]

	t5_t6_t2_mem1 = S.Task('t5_t6_t2_mem1', length=1, delay_cost=1)
	S += t5_t6_t2_mem1 >= 66
	t5_t6_t2_mem1 += MAS_MEM[1]

	t5_t80 = S.Task('t5_t80', length=3, delay_cost=1)
	S += t5_t80 >= 66
	t5_t80 += MAS[0]

	t5_t6_t2 = S.Task('t5_t6_t2', length=3, delay_cost=1)
	S += t5_t6_t2 >= 67
	t5_t6_t2 += MAS[0]

	t5_t6_t3_in = S.Task('t5_t6_t3_in', length=1, delay_cost=1)
	S += t5_t6_t3_in >= 67
	t5_t6_t3_in += MAS_in[0]

	t5_t6_t3_mem0 = S.Task('t5_t6_t3_mem0', length=1, delay_cost=1)
	S += t5_t6_t3_mem0 >= 67
	t5_t6_t3_mem0 += MAS_MEM[0]

	t5_t6_t3_mem1 = S.Task('t5_t6_t3_mem1', length=1, delay_cost=1)
	S += t5_t6_t3_mem1 >= 67
	t5_t6_t3_mem1 += MAS_MEM[1]

	t420_in = S.Task('t420_in', length=1, delay_cost=1)
	S += t420_in >= 68
	t420_in += MAS_in[0]

	t420_mem0 = S.Task('t420_mem0', length=1, delay_cost=1)
	S += t420_mem0 >= 68
	t420_mem0 += MAS_MEM[0]

	t420_mem1 = S.Task('t420_mem1', length=1, delay_cost=1)
	S += t420_mem1 >= 68
	t420_mem1 += MAS_MEM[1]

	t5_t6_t3 = S.Task('t5_t6_t3', length=3, delay_cost=1)
	S += t5_t6_t3 >= 68
	t5_t6_t3 += MAS[0]

	t420 = S.Task('t420', length=3, delay_cost=1)
	S += t420 >= 69
	t420 += MAS[0]

	t4_t21_in = S.Task('t4_t21_in', length=1, delay_cost=1)
	S += t4_t21_in >= 69
	t4_t21_in += MAS_in[0]

	t4_t21_mem0 = S.Task('t4_t21_mem0', length=1, delay_cost=1)
	S += t4_t21_mem0 >= 69
	t4_t21_mem0 += MM_MEM[0]

	t4_t21_mem1 = S.Task('t4_t21_mem1', length=1, delay_cost=1)
	S += t4_t21_mem1 >= 69
	t4_t21_mem1 += MAS_MEM[1]

	t4_t21 = S.Task('t4_t21', length=3, delay_cost=1)
	S += t4_t21 >= 70
	t4_t21 += MAS[0]

	t5_t10_in = S.Task('t5_t10_in', length=1, delay_cost=1)
	S += t5_t10_in >= 70
	t5_t10_in += MAS_in[0]

	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	S += t5_t10_mem0 >= 70
	t5_t10_mem0 += MM_MEM[0]

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	S += t5_t10_mem1 >= 70
	t5_t10_mem1 += MM_MEM[1]

	t5_t6_t4_in = S.Task('t5_t6_t4_in', length=1, delay_cost=1)
	S += t5_t6_t4_in >= 70
	t5_t6_t4_in += MM_in[0]

	t5_t6_t4_mem0 = S.Task('t5_t6_t4_mem0', length=1, delay_cost=1)
	S += t5_t6_t4_mem0 >= 70
	t5_t6_t4_mem0 += MAS_MEM[0]

	t5_t6_t4_mem1 = S.Task('t5_t6_t4_mem1', length=1, delay_cost=1)
	S += t5_t6_t4_mem1 >= 70
	t5_t6_t4_mem1 += MAS_MEM[1]

	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	S += c110_in >= 71
	c110_in += MAS_in[0]

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	S += c110_mem0 >= 71
	c110_mem0 += MAS_MEM[0]

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	S += c110_mem1 >= 71
	c110_mem1 += MAS_MEM[1]

	t5_t10 = S.Task('t5_t10', length=3, delay_cost=1)
	S += t5_t10 >= 71
	t5_t10 += MAS[0]

	t5_t6_t4 = S.Task('t5_t6_t4', length=14, delay_cost=1)
	S += t5_t6_t4 >= 71
	t5_t6_t4 += MM[0]

	c110 = S.Task('c110', length=3, delay_cost=1)
	S += c110 >= 72
	c110 += MAS[0]

	t4_t11_in = S.Task('t4_t11_in', length=1, delay_cost=1)
	S += t4_t11_in >= 72
	t4_t11_in += MAS_in[0]

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	S += t4_t11_mem0 >= 72
	t4_t11_mem0 += MM_MEM[0]

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	S += t4_t11_mem1 >= 72
	t4_t11_mem1 += MAS_MEM[1]

	t4_t100_in = S.Task('t4_t100_in', length=1, delay_cost=1)
	S += t4_t100_in >= 73
	t4_t100_in += MAS_in[0]

	t4_t100_mem0 = S.Task('t4_t100_mem0', length=1, delay_cost=1)
	S += t4_t100_mem0 >= 73
	t4_t100_mem0 += MAS_MEM[0]

	t4_t100_mem1 = S.Task('t4_t100_mem1', length=1, delay_cost=1)
	S += t4_t100_mem1 >= 73
	t4_t100_mem1 += MAS_MEM[1]

	t4_t11 = S.Task('t4_t11', length=3, delay_cost=1)
	S += t4_t11 >= 73
	t4_t11 += MAS[0]

	t4_t100 = S.Task('t4_t100', length=3, delay_cost=1)
	S += t4_t100 >= 74
	t4_t100 += MAS[0]

	t4_t81_in = S.Task('t4_t81_in', length=1, delay_cost=1)
	S += t4_t81_in >= 74
	t4_t81_in += MAS_in[0]

	t4_t81_mem0 = S.Task('t4_t81_mem0', length=1, delay_cost=1)
	S += t4_t81_mem0 >= 74
	t4_t81_mem0 += MM_MEM[0]

	t4_t81_mem1 = S.Task('t4_t81_mem1', length=1, delay_cost=1)
	S += t4_t81_mem1 >= 74
	t4_t81_mem1 += MAS_MEM[1]

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	S += c110_w >= 75
	c110_w += MAIN_MEM_w

	t4_t81 = S.Task('t4_t81', length=3, delay_cost=1)
	S += t4_t81 >= 75
	t4_t81 += MAS[0]

	t520_in = S.Task('t520_in', length=1, delay_cost=1)
	S += t520_in >= 75
	t520_in += MAS_in[0]

	t520_mem0 = S.Task('t520_mem0', length=1, delay_cost=1)
	S += t520_mem0 >= 75
	t520_mem0 += MAS_MEM[0]

	t520_mem1 = S.Task('t520_mem1', length=1, delay_cost=1)
	S += t520_mem1 >= 75
	t520_mem1 += MAS_MEM[1]

	t520 = S.Task('t520', length=3, delay_cost=1)
	S += t520 >= 76
	t520 += MAS[0]

	t5_t0_t5_in = S.Task('t5_t0_t5_in', length=1, delay_cost=1)
	S += t5_t0_t5_in >= 76
	t5_t0_t5_in += MAS_in[0]

	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	S += t5_t0_t5_mem0 >= 76
	t5_t0_t5_mem0 += MM_MEM[0]

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	S += t5_t0_t5_mem1 >= 76
	t5_t0_t5_mem1 += MM_MEM[1]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 77
	t21_in += MAS_in[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 77
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 77
	t21_mem1 += MAS_MEM[1]

	t5_t0_t5 = S.Task('t5_t0_t5', length=3, delay_cost=1)
	S += t5_t0_t5 >= 77
	t5_t0_t5 += MAS[0]

	t21 = S.Task('t21', length=3, delay_cost=1)
	S += t21 >= 78
	t21 += MAS[0]

	t4_t01_in = S.Task('t4_t01_in', length=1, delay_cost=1)
	S += t4_t01_in >= 78
	t4_t01_in += MAS_in[0]

	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	S += t4_t01_mem0 >= 78
	t4_t01_mem0 += MM_MEM[0]

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	S += t4_t01_mem1 >= 78
	t4_t01_mem1 += MAS_MEM[1]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 79
	t160_in += MAS_in[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 79
	t160_mem0 += MAS_MEM[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 79
	t160_mem1 += MAS_MEM[1]

	t4_t01 = S.Task('t4_t01', length=3, delay_cost=1)
	S += t4_t01 >= 79
	t4_t01 += MAS[0]

	t160 = S.Task('t160', length=3, delay_cost=1)
	S += t160 >= 80
	t160 += MAS[0]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 80
	t170_in += MAS_in[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 80
	t170_mem0 += MAS_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 80
	t170_mem1 += MAS_MEM[1]

	t170 = S.Task('t170', length=3, delay_cost=1)
	S += t170 >= 81
	t170 += MAS[0]

	t4_t71_in = S.Task('t4_t71_in', length=1, delay_cost=1)
	S += t4_t71_in >= 81
	t4_t71_in += MAS_in[0]

	t4_t71_mem0 = S.Task('t4_t71_mem0', length=1, delay_cost=1)
	S += t4_t71_mem0 >= 81
	t4_t71_mem0 += MAS_MEM[0]

	t4_t71_mem1 = S.Task('t4_t71_mem1', length=1, delay_cost=1)
	S += t4_t71_mem1 >= 81
	t4_t71_mem1 += MAS_MEM[1]

	t421_in = S.Task('t421_in', length=1, delay_cost=1)
	S += t421_in >= 82
	t421_in += MAS_in[0]

	t421_mem0 = S.Task('t421_mem0', length=1, delay_cost=1)
	S += t421_mem0 >= 82
	t421_mem0 += MAS_MEM[0]

	t421_mem1 = S.Task('t421_mem1', length=1, delay_cost=1)
	S += t421_mem1 >= 82
	t421_mem1 += MAS_MEM[1]

	t4_t71 = S.Task('t4_t71', length=3, delay_cost=1)
	S += t4_t71 >= 82
	t4_t71 += MAS[0]

	t421 = S.Task('t421', length=3, delay_cost=1)
	S += t421 >= 83
	t421 += MAS[0]

	t4_t6_t5_in = S.Task('t4_t6_t5_in', length=1, delay_cost=1)
	S += t4_t6_t5_in >= 83
	t4_t6_t5_in += MAS_in[0]

	t4_t6_t5_mem0 = S.Task('t4_t6_t5_mem0', length=1, delay_cost=1)
	S += t4_t6_t5_mem0 >= 83
	t4_t6_t5_mem0 += MM_MEM[0]

	t4_t6_t5_mem1 = S.Task('t4_t6_t5_mem1', length=1, delay_cost=1)
	S += t4_t6_t5_mem1 >= 83
	t4_t6_t5_mem1 += MM_MEM[1]

	t4_t6_t5 = S.Task('t4_t6_t5', length=3, delay_cost=1)
	S += t4_t6_t5 >= 84
	t4_t6_t5 += MAS[0]

	t5_t01_in = S.Task('t5_t01_in', length=1, delay_cost=1)
	S += t5_t01_in >= 84
	t5_t01_in += MAS_in[0]

	t5_t01_mem0 = S.Task('t5_t01_mem0', length=1, delay_cost=1)
	S += t5_t01_mem0 >= 84
	t5_t01_mem0 += MM_MEM[0]

	t5_t01_mem1 = S.Task('t5_t01_mem1', length=1, delay_cost=1)
	S += t5_t01_mem1 >= 84
	t5_t01_mem1 += MAS_MEM[1]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 85
	t11_in += MAS_in[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 85
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 85
	t11_mem1 += MAS_MEM[1]

	t5_t01 = S.Task('t5_t01', length=3, delay_cost=1)
	S += t5_t01 >= 85
	t5_t01 += MAS[0]

	t11 = S.Task('t11', length=3, delay_cost=1)
	S += t11 >= 86
	t11 += MAS[0]

	t5_t1_t5_in = S.Task('t5_t1_t5_in', length=1, delay_cost=1)
	S += t5_t1_t5_in >= 86
	t5_t1_t5_in += MAS_in[0]

	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	S += t5_t1_t5_mem0 >= 86
	t5_t1_t5_mem0 += MM_MEM[0]

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	S += t5_t1_t5_mem1 >= 86
	t5_t1_t5_mem1 += MM_MEM[1]

	t4_t60_in = S.Task('t4_t60_in', length=1, delay_cost=1)
	S += t4_t60_in >= 87
	t4_t60_in += MAS_in[0]

	t4_t60_mem0 = S.Task('t4_t60_mem0', length=1, delay_cost=1)
	S += t4_t60_mem0 >= 87
	t4_t60_mem0 += MM_MEM[0]

	t4_t60_mem1 = S.Task('t4_t60_mem1', length=1, delay_cost=1)
	S += t4_t60_mem1 >= 87
	t4_t60_mem1 += MM_MEM[1]

	t5_t1_t5 = S.Task('t5_t1_t5', length=3, delay_cost=1)
	S += t5_t1_t5 >= 87
	t5_t1_t5 += MAS[0]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 88
	t01_in += MAS_in[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 88
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 88
	t01_mem1 += MAS_MEM[1]

	t4_t60 = S.Task('t4_t60', length=3, delay_cost=1)
	S += t4_t60 >= 88
	t4_t60 += MAS[0]

	t01 = S.Task('t01', length=3, delay_cost=1)
	S += t01 >= 89
	t01 += MAS[0]

	t5_t11_in = S.Task('t5_t11_in', length=1, delay_cost=1)
	S += t5_t11_in >= 89
	t5_t11_in += MAS_in[0]

	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	S += t5_t11_mem0 >= 89
	t5_t11_mem0 += MM_MEM[0]

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	S += t5_t11_mem1 >= 89
	t5_t11_mem1 += MAS_MEM[1]

	t4_t70_in = S.Task('t4_t70_in', length=1, delay_cost=1)
	S += t4_t70_in >= 90
	t4_t70_in += MAS_in[0]

	t4_t70_mem0 = S.Task('t4_t70_mem0', length=1, delay_cost=1)
	S += t4_t70_mem0 >= 90
	t4_t70_mem0 += MAS_MEM[0]

	t4_t70_mem1 = S.Task('t4_t70_mem1', length=1, delay_cost=1)
	S += t4_t70_mem1 >= 90
	t4_t70_mem1 += MAS_MEM[1]

	t5_t11 = S.Task('t5_t11', length=3, delay_cost=1)
	S += t5_t11 >= 90
	t5_t11 += MAS[0]

	t4_t61_in = S.Task('t4_t61_in', length=1, delay_cost=1)
	S += t4_t61_in >= 91
	t4_t61_in += MAS_in[0]

	t4_t61_mem0 = S.Task('t4_t61_mem0', length=1, delay_cost=1)
	S += t4_t61_mem0 >= 91
	t4_t61_mem0 += MM_MEM[0]

	t4_t61_mem1 = S.Task('t4_t61_mem1', length=1, delay_cost=1)
	S += t4_t61_mem1 >= 91
	t4_t61_mem1 += MAS_MEM[1]

	t4_t70 = S.Task('t4_t70', length=3, delay_cost=1)
	S += t4_t70 >= 91
	t4_t70 += MAS[0]

	t4_t61 = S.Task('t4_t61', length=3, delay_cost=1)
	S += t4_t61 >= 92
	t4_t61 += MAS[0]

	t5_t81_in = S.Task('t5_t81_in', length=1, delay_cost=1)
	S += t5_t81_in >= 92
	t5_t81_in += MAS_in[0]

	t5_t81_mem0 = S.Task('t5_t81_mem0', length=1, delay_cost=1)
	S += t5_t81_mem0 >= 92
	t5_t81_mem0 += MM_MEM[0]

	t5_t81_mem1 = S.Task('t5_t81_mem1', length=1, delay_cost=1)
	S += t5_t81_mem1 >= 92
	t5_t81_mem1 += MAS_MEM[1]

	t5_t20_in = S.Task('t5_t20_in', length=1, delay_cost=1)
	S += t5_t20_in >= 93
	t5_t20_in += MAS_in[0]

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	S += t5_t20_mem0 >= 93
	t5_t20_mem0 += MM_MEM[0]

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	S += t5_t20_mem1 >= 93
	t5_t20_mem1 += MM_MEM[1]

	t5_t81 = S.Task('t5_t81', length=3, delay_cost=1)
	S += t5_t81 >= 93
	t5_t81 += MAS[0]

	t5_t20 = S.Task('t5_t20', length=3, delay_cost=1)
	S += t5_t20 >= 94
	t5_t20 += MAS[0]

	t5_t60_in = S.Task('t5_t60_in', length=1, delay_cost=1)
	S += t5_t60_in >= 94
	t5_t60_in += MAS_in[0]

	t5_t60_mem0 = S.Task('t5_t60_mem0', length=1, delay_cost=1)
	S += t5_t60_mem0 >= 94
	t5_t60_mem0 += MM_MEM[0]

	t5_t60_mem1 = S.Task('t5_t60_mem1', length=1, delay_cost=1)
	S += t5_t60_mem1 >= 94
	t5_t60_mem1 += MM_MEM[1]

	t410_in = S.Task('t410_in', length=1, delay_cost=1)
	S += t410_in >= 95
	t410_in += MAS_in[0]

	t410_mem0 = S.Task('t410_mem0', length=1, delay_cost=1)
	S += t410_mem0 >= 95
	t410_mem0 += MAS_MEM[0]

	t410_mem1 = S.Task('t410_mem1', length=1, delay_cost=1)
	S += t410_mem1 >= 95
	t410_mem1 += MAS_MEM[1]

	t5_t60 = S.Task('t5_t60', length=3, delay_cost=1)
	S += t5_t60 >= 95
	t5_t60 += MAS[0]

	t410 = S.Task('t410', length=3, delay_cost=1)
	S += t410 >= 96
	t410 += MAS[0]

	t5_t2_t5_in = S.Task('t5_t2_t5_in', length=1, delay_cost=1)
	S += t5_t2_t5_in >= 96
	t5_t2_t5_in += MAS_in[0]

	t5_t2_t5_mem0 = S.Task('t5_t2_t5_mem0', length=1, delay_cost=1)
	S += t5_t2_t5_mem0 >= 96
	t5_t2_t5_mem0 += MM_MEM[0]

	t5_t2_t5_mem1 = S.Task('t5_t2_t5_mem1', length=1, delay_cost=1)
	S += t5_t2_t5_mem1 >= 96
	t5_t2_t5_mem1 += MM_MEM[1]

	t5_t00_in = S.Task('t5_t00_in', length=1, delay_cost=1)
	S += t5_t00_in >= 97
	t5_t00_in += MAS_in[0]

	t5_t00_mem0 = S.Task('t5_t00_mem0', length=1, delay_cost=1)
	S += t5_t00_mem0 >= 97
	t5_t00_mem0 += MM_MEM[0]

	t5_t00_mem1 = S.Task('t5_t00_mem1', length=1, delay_cost=1)
	S += t5_t00_mem1 >= 97
	t5_t00_mem1 += MM_MEM[1]

	t5_t2_t5 = S.Task('t5_t2_t5', length=3, delay_cost=1)
	S += t5_t2_t5 >= 97
	t5_t2_t5 += MAS[0]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 98
	t31_in += MAS_in[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 98
	t31_mem0 += MAS_MEM[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 98
	t31_mem1 += MAS_MEM[1]

	t5_t00 = S.Task('t5_t00', length=3, delay_cost=1)
	S += t5_t00 >= 98
	t5_t00 += MAS[0]

	t31 = S.Task('t31', length=3, delay_cost=1)
	S += t31 >= 99
	t31 += MAS[0]

	t5_t6_t5_in = S.Task('t5_t6_t5_in', length=1, delay_cost=1)
	S += t5_t6_t5_in >= 99
	t5_t6_t5_in += MAS_in[0]

	t5_t6_t5_mem0 = S.Task('t5_t6_t5_mem0', length=1, delay_cost=1)
	S += t5_t6_t5_mem0 >= 99
	t5_t6_t5_mem0 += MM_MEM[0]

	t5_t6_t5_mem1 = S.Task('t5_t6_t5_mem1', length=1, delay_cost=1)
	S += t5_t6_t5_mem1 >= 99
	t5_t6_t5_mem1 += MM_MEM[1]

	t5_t21_in = S.Task('t5_t21_in', length=1, delay_cost=1)
	S += t5_t21_in >= 100
	t5_t21_in += MAS_in[0]

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	S += t5_t21_mem0 >= 100
	t5_t21_mem0 += MM_MEM[0]

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	S += t5_t21_mem1 >= 100
	t5_t21_mem1 += MAS_MEM[1]

	t5_t6_t5 = S.Task('t5_t6_t5', length=3, delay_cost=1)
	S += t5_t6_t5 >= 100
	t5_t6_t5 += MAS[0]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 101
	t171_in += MAS_in[0]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 101
	t171_mem0 += MAS_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 101
	t171_mem1 += MAS_MEM[1]

	t5_t21 = S.Task('t5_t21', length=3, delay_cost=1)
	S += t5_t21 >= 101
	t5_t21 += MAS[0]

	t171 = S.Task('t171', length=3, delay_cost=1)
	S += t171 >= 102
	t171 += MAS[0]

	t4_t101_in = S.Task('t4_t101_in', length=1, delay_cost=1)
	S += t4_t101_in >= 102
	t4_t101_in += MAS_in[0]

	t4_t101_mem0 = S.Task('t4_t101_mem0', length=1, delay_cost=1)
	S += t4_t101_mem0 >= 102
	t4_t101_mem0 += MAS_MEM[0]

	t4_t101_mem1 = S.Task('t4_t101_mem1', length=1, delay_cost=1)
	S += t4_t101_mem1 >= 102
	t4_t101_mem1 += MAS_MEM[1]

	t4_t101 = S.Task('t4_t101', length=3, delay_cost=1)
	S += t4_t101 >= 103
	t4_t101 += MAS[0]

	t5_t70_in = S.Task('t5_t70_in', length=1, delay_cost=1)
	S += t5_t70_in >= 103
	t5_t70_in += MAS_in[0]

	t5_t70_mem0 = S.Task('t5_t70_mem0', length=1, delay_cost=1)
	S += t5_t70_mem0 >= 103
	t5_t70_mem0 += MAS_MEM[0]

	t5_t70_mem1 = S.Task('t5_t70_mem1', length=1, delay_cost=1)
	S += t5_t70_mem1 >= 103
	t5_t70_mem1 += MAS_MEM[1]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 104
	t30_in += MAS_in[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 104
	t30_mem0 += MAS_MEM[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 104
	t30_mem1 += MAS_MEM[1]

	t5_t70 = S.Task('t5_t70', length=3, delay_cost=1)
	S += t5_t70 >= 104
	t5_t70 += MAS[0]

	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	S += c210_in >= 105
	c210_in += MAS_in[0]

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	S += c210_mem0 >= 105
	c210_mem0 += MAS_MEM[0]

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	S += c210_mem1 >= 105
	c210_mem1 += MAS_MEM[1]

	t30 = S.Task('t30', length=3, delay_cost=1)
	S += t30 >= 105
	t30 += MAS[0]

	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	S += c111_in >= 106
	c111_in += MAS_in[0]

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	S += c111_mem0 >= 106
	c111_mem0 += MAS_MEM[0]

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	S += c111_mem1 >= 106
	c111_mem1 += MAS_MEM[1]

	c210 = S.Task('c210', length=3, delay_cost=1)
	S += c210 >= 106
	c210 += MAS[0]

	c111 = S.Task('c111', length=3, delay_cost=1)
	S += c111 >= 107
	c111 += MAS[0]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 107
	c200_in += MAS_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 107
	c200_mem0 += MAS_MEM[0]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 107
	c200_mem1 += MAS_MEM[1]

	c200 = S.Task('c200', length=3, delay_cost=1)
	S += c200 >= 108
	c200 += MAS[0]

	t400_in = S.Task('t400_in', length=1, delay_cost=1)
	S += t400_in >= 108
	t400_in += MAS_in[0]

	t400_mem0 = S.Task('t400_mem0', length=1, delay_cost=1)
	S += t400_mem0 >= 108
	t400_mem0 += MAS_MEM[0]

	t400_mem1 = S.Task('t400_mem1', length=1, delay_cost=1)
	S += t400_mem1 >= 108
	t400_mem1 += MAS_MEM[1]

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	S += c210_w >= 109
	c210_w += MAIN_MEM_w

	t400 = S.Task('t400', length=3, delay_cost=1)
	S += t400 >= 109
	t400 += MAS[0]

	t401_in = S.Task('t401_in', length=1, delay_cost=1)
	S += t401_in >= 109
	t401_in += MAS_in[0]

	t401_mem0 = S.Task('t401_mem0', length=1, delay_cost=1)
	S += t401_mem0 >= 109
	t401_mem0 += MAS_MEM[0]

	t401_mem1 = S.Task('t401_mem1', length=1, delay_cost=1)
	S += t401_mem1 >= 109
	t401_mem1 += MAS_MEM[1]

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	S += c111_w >= 110
	c111_w += MAIN_MEM_w

	t401 = S.Task('t401', length=3, delay_cost=1)
	S += t401 >= 110
	t401 += MAS[0]

	t411_in = S.Task('t411_in', length=1, delay_cost=1)
	S += t411_in >= 110
	t411_in += MAS_in[0]

	t411_mem0 = S.Task('t411_mem0', length=1, delay_cost=1)
	S += t411_mem0 >= 110
	t411_mem0 += MAS_MEM[0]

	t411_mem1 = S.Task('t411_mem1', length=1, delay_cost=1)
	S += t411_mem1 >= 110
	t411_mem1 += MAS_MEM[1]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 111
	c000_in += MAS_in[0]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 111
	c000_mem0 += MAS_MEM[0]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 111
	c000_mem1 += MAS_MEM[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 111
	c200_w += MAIN_MEM_w

	t411 = S.Task('t411', length=3, delay_cost=1)
	S += t411 >= 111
	t411 += MAS[0]

	c000 = S.Task('c000', length=3, delay_cost=1)
	S += c000 >= 112
	c000 += MAS[0]

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 112
	c001_in += MAS_in[0]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 112
	c001_mem0 += MAS_MEM[0]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 112
	c001_mem1 += MAS_MEM[1]

	c001 = S.Task('c001', length=3, delay_cost=1)
	S += c001 >= 113
	c001 += MAS[0]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 113
	c201_in += MAS_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 113
	c201_mem0 += MAS_MEM[0]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 113
	c201_mem1 += MAS_MEM[1]

	c201 = S.Task('c201', length=3, delay_cost=1)
	S += c201 >= 114
	c201 += MAS[0]

	t510_in = S.Task('t510_in', length=1, delay_cost=1)
	S += t510_in >= 114
	t510_in += MAS_in[0]

	t510_mem0 = S.Task('t510_mem0', length=1, delay_cost=1)
	S += t510_mem0 >= 114
	t510_mem0 += MAS_MEM[0]

	t510_mem1 = S.Task('t510_mem1', length=1, delay_cost=1)
	S += t510_mem1 >= 114
	t510_mem1 += MAS_MEM[1]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 115
	c000_w += MAIN_MEM_w

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 115
	t150_in += MAS_in[0]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 115
	t150_mem0 += MAS_MEM[0]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 115
	t150_mem1 += MAS_MEM[1]

	t510 = S.Task('t510', length=3, delay_cost=1)
	S += t510 >= 115
	t510 += MAS[0]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 116
	c001_w += MAIN_MEM_w

	t150 = S.Task('t150', length=3, delay_cost=1)
	S += t150 >= 116
	t150 += MAS[0]

	t521_in = S.Task('t521_in', length=1, delay_cost=1)
	S += t521_in >= 116
	t521_in += MAS_in[0]

	t521_mem0 = S.Task('t521_mem0', length=1, delay_cost=1)
	S += t521_mem0 >= 116
	t521_mem0 += MAS_MEM[0]

	t521_mem1 = S.Task('t521_mem1', length=1, delay_cost=1)
	S += t521_mem1 >= 116
	t521_mem1 += MAS_MEM[1]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 117
	c201_w += MAIN_MEM_w

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 117
	t161_in += MAS_in[0]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 117
	t161_mem0 += MAS_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 117
	t161_mem1 += MAS_MEM[1]

	t521 = S.Task('t521', length=3, delay_cost=1)
	S += t521 >= 117
	t521 += MAS[0]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 118
	c010_in += MAS_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 118
	c010_mem0 += MAS_MEM[0]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 118
	c010_mem1 += MAS_MEM[1]

	t161 = S.Task('t161', length=3, delay_cost=1)
	S += t161 >= 118
	t161 += MAS[0]

	c010 = S.Task('c010', length=3, delay_cost=1)
	S += c010 >= 119
	c010 += MAS[0]

	t5_t100_in = S.Task('t5_t100_in', length=1, delay_cost=1)
	S += t5_t100_in >= 119
	t5_t100_in += MAS_in[0]

	t5_t100_mem0 = S.Task('t5_t100_mem0', length=1, delay_cost=1)
	S += t5_t100_mem0 >= 119
	t5_t100_mem0 += MAS_MEM[0]

	t5_t100_mem1 = S.Task('t5_t100_mem1', length=1, delay_cost=1)
	S += t5_t100_mem1 >= 119
	t5_t100_mem1 += MAS_MEM[1]

	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	S += c211_in >= 120
	c211_in += MAS_in[0]

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	S += c211_mem0 >= 120
	c211_mem0 += MAS_MEM[0]

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	S += c211_mem1 >= 120
	c211_mem1 += MAS_MEM[1]

	t5_t100 = S.Task('t5_t100', length=3, delay_cost=1)
	S += t5_t100 >= 120
	t5_t100 += MAS[0]

	c211 = S.Task('c211', length=3, delay_cost=1)
	S += c211 >= 121
	c211 += MAS[0]

	t5_t71_in = S.Task('t5_t71_in', length=1, delay_cost=1)
	S += t5_t71_in >= 121
	t5_t71_in += MAS_in[0]

	t5_t71_mem0 = S.Task('t5_t71_mem0', length=1, delay_cost=1)
	S += t5_t71_mem0 >= 121
	t5_t71_mem0 += MAS_MEM[0]

	t5_t71_mem1 = S.Task('t5_t71_mem1', length=1, delay_cost=1)
	S += t5_t71_mem1 >= 121
	t5_t71_mem1 += MAS_MEM[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 122
	c010_w += MAIN_MEM_w

	t5_t61_in = S.Task('t5_t61_in', length=1, delay_cost=1)
	S += t5_t61_in >= 122
	t5_t61_in += MAS_in[0]

	t5_t61_mem0 = S.Task('t5_t61_mem0', length=1, delay_cost=1)
	S += t5_t61_mem0 >= 122
	t5_t61_mem0 += MM_MEM[0]

	t5_t61_mem1 = S.Task('t5_t61_mem1', length=1, delay_cost=1)
	S += t5_t61_mem1 >= 122
	t5_t61_mem1 += MAS_MEM[1]

	t5_t71 = S.Task('t5_t71', length=3, delay_cost=1)
	S += t5_t71 >= 122
	t5_t71 += MAS[0]

	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	S += t140_in >= 123
	t140_in += MAS_in[0]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 123
	t140_mem0 += MAS_MEM[0]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 123
	t140_mem1 += MAS_MEM[1]

	t5_t61 = S.Task('t5_t61', length=3, delay_cost=1)
	S += t5_t61 >= 123
	t5_t61 += MAS[0]

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	S += c211_w >= 124
	c211_w += MAIN_MEM_w

	t140 = S.Task('t140', length=3, delay_cost=1)
	S += t140 >= 124
	t140 += MAS[0]

	t5_t101_in = S.Task('t5_t101_in', length=1, delay_cost=1)
	S += t5_t101_in >= 124
	t5_t101_in += MAS_in[0]

	t5_t101_mem0 = S.Task('t5_t101_mem0', length=1, delay_cost=1)
	S += t5_t101_mem0 >= 124
	t5_t101_mem0 += MAS_MEM[0]

	t5_t101_mem1 = S.Task('t5_t101_mem1', length=1, delay_cost=1)
	S += t5_t101_mem1 >= 124
	t5_t101_mem1 += MAS_MEM[1]

	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	S += t151_in >= 125
	t151_in += MAS_in[0]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 125
	t151_mem0 += MAS_MEM[0]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 125
	t151_mem1 += MAS_MEM[1]

	t5_t101 = S.Task('t5_t101', length=3, delay_cost=1)
	S += t5_t101 >= 125
	t5_t101 += MAS[0]

	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	S += t141_in >= 126
	t141_in += MAS_in[0]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 126
	t141_mem0 += MAS_MEM[0]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 126
	t141_mem1 += MAS_MEM[1]

	t151 = S.Task('t151', length=3, delay_cost=1)
	S += t151 >= 126
	t151 += MAS[0]

	t141 = S.Task('t141', length=3, delay_cost=1)
	S += t141 >= 127
	t141 += MAS[0]

	t500_in = S.Task('t500_in', length=1, delay_cost=1)
	S += t500_in >= 128
	t500_in += MAS_in[0]

	t500_mem0 = S.Task('t500_mem0', length=1, delay_cost=1)
	S += t500_mem0 >= 128
	t500_mem0 += MAS_MEM[0]

	t500_mem1 = S.Task('t500_mem1', length=1, delay_cost=1)
	S += t500_mem1 >= 128
	t500_mem1 += MAS_MEM[1]

	t500 = S.Task('t500', length=3, delay_cost=1)
	S += t500 >= 129
	t500 += MAS[0]

	t501_in = S.Task('t501_in', length=1, delay_cost=1)
	S += t501_in >= 129
	t501_in += MAS_in[0]

	t501_mem0 = S.Task('t501_mem0', length=1, delay_cost=1)
	S += t501_mem0 >= 129
	t501_mem0 += MAS_MEM[0]

	t501_mem1 = S.Task('t501_mem1', length=1, delay_cost=1)
	S += t501_mem1 >= 129
	t501_mem1 += MAS_MEM[1]

	t501 = S.Task('t501', length=3, delay_cost=1)
	S += t501 >= 130
	t501 += MAS[0]

	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	S += c100_in >= 131
	c100_in += MAS_in[0]

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	S += c100_mem0 >= 131
	c100_mem0 += MAS_MEM[0]

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	S += c100_mem1 >= 131
	c100_mem1 += MAS_MEM[1]

	c100 = S.Task('c100', length=3, delay_cost=1)
	S += c100 >= 132
	c100 += MAS[0]

	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	S += c101_in >= 132
	c101_in += MAS_in[0]

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	S += c101_mem0 >= 132
	c101_mem0 += MAS_MEM[0]

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	S += c101_mem1 >= 132
	c101_mem1 += MAS_MEM[1]

	c101 = S.Task('c101', length=3, delay_cost=1)
	S += c101 >= 133
	c101 += MAS[0]

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	S += c100_w >= 135
	c100_w += MAIN_MEM_w

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	S += c101_w >= 136
	c101_w += MAIN_MEM_w


	# new tasks
	t511 = S.Task('t511', length=3, delay_cost=1)
	t511 += alt(MAS)
	t511_in = S.Task('t511_in', length=1, delay_cost=1)
	t511_in += alt(MAS_in)
	S += t511_in*MAS_in[0]<=t511*MAS[0]

	S += t511<1000

	t511_mem0 = S.Task('t511_mem0', length=1, delay_cost=1)
	t511_mem0 += MAS_MEM[0]
	S += 125 < t511_mem0
	S += t511_mem0 <= t511

	t511_mem1 = S.Task('t511_mem1', length=1, delay_cost=1)
	t511_mem1 += MAS_MEM[1]
	S += 124 < t511_mem1
	S += t511_mem1 <= t511

	c011 = S.Task('c011', length=3, delay_cost=1)
	c011 += alt(MAS)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MAS_in)
	S += c011_in*MAS_in[0]<=c011*MAS[0]

	S += 34<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	S += c011<1000

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(MAS_MEM)
	S += (t511*MAS[0])-1 < c011_mem0*MAS_MEM[0]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += MAS_MEM[1]
	S += 128 < c011_mem1
	S += c011_mem1 <= c011

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM1_stage3MAS1/SPARSE/schedule5.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution
