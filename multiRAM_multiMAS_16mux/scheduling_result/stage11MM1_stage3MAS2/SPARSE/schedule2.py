from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 165
	S = Scenario("schedule2", horizon=horizon)

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
	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 0
	t2_t2_in += MAS_in[1]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 0
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 0
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=3, delay_cost=1)
	S += t2_t2 >= 1
	t2_t2 += MAS[1]

	t4_t41_in = S.Task('t4_t41_in', length=1, delay_cost=1)
	S += t4_t41_in >= 1
	t4_t41_in += MAS_in[0]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 1
	t4_t41_mem0 += MAIN_MEM_r[0]

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 1
	t4_t41_mem1 += MAIN_MEM_r[1]

	t4_t41 = S.Task('t4_t41', length=3, delay_cost=1)
	S += t4_t41 >= 2
	t4_t41 += MAS[0]

	t4_t51_in = S.Task('t4_t51_in', length=1, delay_cost=1)
	S += t4_t51_in >= 2
	t4_t51_in += MAS_in[0]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 2
	t4_t51_mem0 += MAIN_MEM_r[0]

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 2
	t4_t51_mem1 += MAIN_MEM_r[1]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 3
	t1_t2_in += MAS_in[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 3
	t1_t2_mem0 += MAIN_MEM_r[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 3
	t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t51 = S.Task('t4_t51', length=3, delay_cost=1)
	S += t4_t51 >= 3
	t4_t51 += MAS[0]

	t1_t2 = S.Task('t1_t2', length=3, delay_cost=1)
	S += t1_t2 >= 4
	t1_t2 += MAS[0]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 4
	t1_t3_in += MAS_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 4
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 4
	t1_t3_mem1 += MAIN_MEM_r[1]

	t1_t3 = S.Task('t1_t3', length=3, delay_cost=1)
	S += t1_t3 >= 5
	t1_t3 += MAS[0]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 5
	t2_t3_in += MAS_in[0]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 5
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 5
	t2_t3_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=3, delay_cost=1)
	S += t2_t3 >= 6
	t2_t3 += MAS[0]

	t4_t1_t2_in = S.Task('t4_t1_t2_in', length=1, delay_cost=1)
	S += t4_t1_t2_in >= 6
	t4_t1_t2_in += MAS_in[0]

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t2_mem0 >= 6
	t4_t1_t2_mem0 += MAIN_MEM_r[0]

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t2_mem1 >= 6
	t4_t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_t2_in = S.Task('t4_t0_t2_in', length=1, delay_cost=1)
	S += t4_t0_t2_in >= 7
	t4_t0_t2_in += MAS_in[1]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 7
	t4_t0_t2_mem0 += MAIN_MEM_r[0]

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 7
	t4_t0_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_t2 = S.Task('t4_t1_t2', length=3, delay_cost=1)
	S += t4_t1_t2 >= 7
	t4_t1_t2 += MAS[0]

	t4_t0_t2 = S.Task('t4_t0_t2', length=3, delay_cost=1)
	S += t4_t0_t2 >= 8
	t4_t0_t2 += MAS[1]

	t4_t0_t3_in = S.Task('t4_t0_t3_in', length=1, delay_cost=1)
	S += t4_t0_t3_in >= 8
	t4_t0_t3_in += MAS_in[0]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 8
	t4_t0_t3_mem0 += MAIN_MEM_r[0]

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 8
	t4_t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t0_t3 = S.Task('t4_t0_t3', length=3, delay_cost=1)
	S += t4_t0_t3 >= 9
	t4_t0_t3 += MAS[0]

	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	S += t4_t8_t0_in >= 9
	t4_t8_t0_in += MM_in[0]

	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	S += t4_t8_t0_mem0 >= 9
	t4_t8_t0_mem0 += MAIN_MEM_r[0]

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	S += t4_t8_t0_mem1 >= 9
	t4_t8_t0_mem1 += MAIN_MEM_r[1]

	t4_t2_t2_in = S.Task('t4_t2_t2_in', length=1, delay_cost=1)
	S += t4_t2_t2_in >= 10
	t4_t2_t2_in += MAS_in[0]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 10
	t4_t2_t2_mem0 += MAIN_MEM_r[0]

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 10
	t4_t2_t2_mem1 += MAIN_MEM_r[1]

	t4_t8_t0 = S.Task('t4_t8_t0', length=11, delay_cost=1)
	S += t4_t8_t0 >= 10
	t4_t8_t0 += MM[0]

	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_in >= 11
	t4_t1_t1_in += MM_in[0]

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_mem0 >= 11
	t4_t1_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_mem1 >= 11
	t4_t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t2 = S.Task('t4_t2_t2', length=3, delay_cost=1)
	S += t4_t2_t2 >= 11
	t4_t2_t2 += MAS[0]

	t4_t1_t1 = S.Task('t4_t1_t1', length=11, delay_cost=1)
	S += t4_t1_t1 >= 12
	t4_t1_t1 += MM[0]

	t4_t2_t3_in = S.Task('t4_t2_t3_in', length=1, delay_cost=1)
	S += t4_t2_t3_in >= 12
	t4_t2_t3_in += MAS_in[0]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 12
	t4_t2_t3_mem0 += MAIN_MEM_r[0]

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 12
	t4_t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_in >= 13
	t4_t1_t0_in += MM_in[0]

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_mem0 >= 13
	t4_t1_t0_mem0 += MAIN_MEM_r[0]

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_mem1 >= 13
	t4_t1_t0_mem1 += MAIN_MEM_r[1]

	t4_t2_t3 = S.Task('t4_t2_t3', length=3, delay_cost=1)
	S += t4_t2_t3 >= 13
	t4_t2_t3 += MAS[0]

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_in >= 14
	t4_t0_t0_in += MM_in[0]

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_mem0 >= 14
	t4_t0_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_mem1 >= 14
	t4_t0_t0_mem1 += MAIN_MEM_r[1]

	t4_t1_t0 = S.Task('t4_t1_t0', length=11, delay_cost=1)
	S += t4_t1_t0 >= 14
	t4_t1_t0 += MM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 15
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 15
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 15
	t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t0_t0 = S.Task('t4_t0_t0', length=11, delay_cost=1)
	S += t4_t0_t0 >= 15
	t4_t0_t0 += MM[0]

	t2_t1 = S.Task('t2_t1', length=11, delay_cost=1)
	S += t2_t1 >= 16
	t2_t1 += MM[0]

	t4_t40_in = S.Task('t4_t40_in', length=1, delay_cost=1)
	S += t4_t40_in >= 16
	t4_t40_in += MAS_in[0]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 16
	t4_t40_mem0 += MAIN_MEM_r[0]

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 16
	t4_t40_mem1 += MAIN_MEM_r[1]

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 17
	t4_t2_t1_in += MM_in[0]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 17
	t4_t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 17
	t4_t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t40 = S.Task('t4_t40', length=3, delay_cost=1)
	S += t4_t40 >= 17
	t4_t40 += MAS[0]

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_in >= 18
	t4_t0_t1_in += MM_in[0]

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_mem0 >= 18
	t4_t0_t1_mem0 += MAIN_MEM_r[0]

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_mem1 >= 18
	t4_t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t1 = S.Task('t4_t2_t1', length=11, delay_cost=1)
	S += t4_t2_t1 >= 18
	t4_t2_t1 += MM[0]

	t4_t0_t1 = S.Task('t4_t0_t1', length=11, delay_cost=1)
	S += t4_t0_t1 >= 19
	t4_t0_t1 += MM[0]

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	S += t4_t2_t0_in >= 19
	t4_t2_t0_in += MM_in[0]

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	S += t4_t2_t0_mem0 >= 19
	t4_t2_t0_mem0 += MAIN_MEM_r[0]

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	S += t4_t2_t0_mem1 >= 19
	t4_t2_t0_mem1 += MAIN_MEM_r[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 20
	t0_t3_in += MAS_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 20
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 20
	t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t2_t0 = S.Task('t4_t2_t0', length=11, delay_cost=1)
	S += t4_t2_t0 >= 20
	t4_t2_t0 += MM[0]

	t0_t3 = S.Task('t0_t3', length=3, delay_cost=1)
	S += t0_t3 >= 21
	t0_t3 += MAS[0]

	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	S += t4_t8_t1_in >= 21
	t4_t8_t1_in += MM_in[0]

	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	S += t4_t8_t1_mem0 >= 21
	t4_t8_t1_mem0 += MAIN_MEM_r[0]

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	S += t4_t8_t1_mem1 >= 21
	t4_t8_t1_mem1 += MAIN_MEM_r[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 22
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 22
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 22
	t2_t0_mem1 += MAIN_MEM_r[1]

	t4_t8_t1 = S.Task('t4_t8_t1', length=11, delay_cost=1)
	S += t4_t8_t1 >= 22
	t4_t8_t1 += MM[0]

	t2_t0 = S.Task('t2_t0', length=11, delay_cost=1)
	S += t2_t0 >= 23
	t2_t0 += MM[0]

	t4_t1_t3_in = S.Task('t4_t1_t3_in', length=1, delay_cost=1)
	S += t4_t1_t3_in >= 23
	t4_t1_t3_in += MAS_in[1]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 23
	t4_t1_t3_mem0 += MAIN_MEM_r[0]

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 23
	t4_t1_t3_mem1 += MAIN_MEM_r[1]

	t4_t1_t3 = S.Task('t4_t1_t3', length=3, delay_cost=1)
	S += t4_t1_t3 >= 24
	t4_t1_t3 += MAS[1]

	t4_t50_in = S.Task('t4_t50_in', length=1, delay_cost=1)
	S += t4_t50_in >= 24
	t4_t50_in += MAS_in[1]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 24
	t4_t50_mem0 += MAIN_MEM_r[0]

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 24
	t4_t50_mem1 += MAIN_MEM_r[1]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 25
	t1_t1_in += MM_in[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 25
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 25
	t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t50 = S.Task('t4_t50', length=3, delay_cost=1)
	S += t4_t50 >= 25
	t4_t50 += MAS[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 26
	t0_t2_in += MAS_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 26
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 26
	t0_t2_mem1 += MAIN_MEM_r[1]

	t1_t1 = S.Task('t1_t1', length=11, delay_cost=1)
	S += t1_t1 >= 26
	t1_t1 += MM[0]

	t0_t2 = S.Task('t0_t2', length=3, delay_cost=1)
	S += t0_t2 >= 27
	t0_t2 += MAS[0]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 27
	t1_t0_in += MM_in[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 27
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 27
	t1_t0_mem1 += MAIN_MEM_r[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 28
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 28
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 28
	t0_t1_mem1 += MAIN_MEM_r[1]

	t1_t0 = S.Task('t1_t0', length=11, delay_cost=1)
	S += t1_t0 >= 28
	t1_t0 += MM[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 29
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 29
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 29
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=11, delay_cost=1)
	S += t0_t1 >= 29
	t0_t1 += MM[0]

	t0_t0 = S.Task('t0_t0', length=11, delay_cost=1)
	S += t0_t0 >= 30
	t0_t0 += MM[0]

	t5_t0_t2_in = S.Task('t5_t0_t2_in', length=1, delay_cost=1)
	S += t5_t0_t2_in >= 30
	t5_t0_t2_in += MAS_in[0]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 30
	t5_t0_t2_mem0 += MAIN_MEM_r[0]

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 30
	t5_t0_t2_mem1 += MAIN_MEM_r[1]

	t5_t0_t2 = S.Task('t5_t0_t2', length=3, delay_cost=1)
	S += t5_t0_t2 >= 31
	t5_t0_t2 += MAS[0]

	t5_t8_t2_in = S.Task('t5_t8_t2_in', length=1, delay_cost=1)
	S += t5_t8_t2_in >= 31
	t5_t8_t2_in += MAS_in[0]

	t5_t8_t2_mem0 = S.Task('t5_t8_t2_mem0', length=1, delay_cost=1)
	S += t5_t8_t2_mem0 >= 31
	t5_t8_t2_mem0 += MAIN_MEM_r[0]

	t5_t8_t2_mem1 = S.Task('t5_t8_t2_mem1', length=1, delay_cost=1)
	S += t5_t8_t2_mem1 >= 31
	t5_t8_t2_mem1 += MAIN_MEM_r[1]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 32
	t101_in += MAS_in[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 32
	t101_mem0 += MAIN_MEM_r[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 32
	t101_mem1 += MAIN_MEM_r[1]

	t5_t8_t2 = S.Task('t5_t8_t2', length=3, delay_cost=1)
	S += t5_t8_t2 >= 32
	t5_t8_t2 += MAS[0]

	t101 = S.Task('t101', length=3, delay_cost=1)
	S += t101 >= 33
	t101 += MAS[1]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 33
	t71_in += MAS_in[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 33
	t71_mem0 += MAIN_MEM_r[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 33
	t71_mem1 += MAIN_MEM_r[1]

	t71 = S.Task('t71', length=3, delay_cost=1)
	S += t71 >= 34
	t71 += MAS[0]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 34
	t80_in += MAS_in[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 34
	t80_mem0 += MAIN_MEM_r[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 34
	t80_mem1 += MAIN_MEM_r[1]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 35
	t100_in += MAS_in[1]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 35
	t100_mem0 += MAIN_MEM_r[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 35
	t100_mem1 += MAIN_MEM_r[1]

	t80 = S.Task('t80', length=3, delay_cost=1)
	S += t80 >= 35
	t80 += MAS[0]

	t100 = S.Task('t100', length=3, delay_cost=1)
	S += t100 >= 36
	t100 += MAS[1]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 36
	t90_in += MAS_in[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 36
	t90_mem0 += MAIN_MEM_r[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 36
	t90_mem1 += MAIN_MEM_r[1]

	t90 = S.Task('t90', length=3, delay_cost=1)
	S += t90 >= 37
	t90 += MAS[0]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 37
	t91_in += MAS_in[1]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 37
	t91_mem0 += MAIN_MEM_r[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 37
	t91_mem1 += MAIN_MEM_r[1]

	t4_t8_t3_in = S.Task('t4_t8_t3_in', length=1, delay_cost=1)
	S += t4_t8_t3_in >= 38
	t4_t8_t3_in += MAS_in[0]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 38
	t4_t8_t3_mem0 += MAIN_MEM_r[0]

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 38
	t4_t8_t3_mem1 += MAIN_MEM_r[1]

	t91 = S.Task('t91', length=3, delay_cost=1)
	S += t91 >= 38
	t91 += MAS[1]

	t4_t8_t3 = S.Task('t4_t8_t3', length=3, delay_cost=1)
	S += t4_t8_t3 >= 39
	t4_t8_t3 += MAS[0]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 39
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 39
	t70_mem0 += MAIN_MEM_r[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 39
	t70_mem1 += MAIN_MEM_r[1]

	t4_t8_t2_in = S.Task('t4_t8_t2_in', length=1, delay_cost=1)
	S += t4_t8_t2_in >= 40
	t4_t8_t2_in += MAS_in[1]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 40
	t4_t8_t2_mem0 += MAIN_MEM_r[0]

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 40
	t4_t8_t2_mem1 += MAIN_MEM_r[1]

	t70 = S.Task('t70', length=3, delay_cost=1)
	S += t70 >= 40
	t70 += MAS[0]

	t4_t8_t2 = S.Task('t4_t8_t2', length=3, delay_cost=1)
	S += t4_t8_t2 >= 41
	t4_t8_t2 += MAS[1]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 41
	t81_in += MAS_in[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 41
	t81_mem0 += MAIN_MEM_r[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 41
	t81_mem1 += MAIN_MEM_r[1]

	t81 = S.Task('t81', length=3, delay_cost=1)
	S += t81 >= 42
	t81 += MAS[0]


	# new tasks
	t1_t4 = S.Task('t1_t4', length=11, delay_cost=1)
	t1_t4 += alt(MM)
	t1_t4_in = S.Task('t1_t4_in', length=1, delay_cost=1)
	t1_t4_in += alt(MM_in)
	S += t1_t4_in*MM_in[0]<=t1_t4*MM[0]
	t1_t4_mem0 = S.Task('t1_t4_mem0', length=1, delay_cost=1)
	t1_t4_mem0 += MAS_MEM[0]
	S += 6 < t1_t4_mem0
	S += t1_t4_mem0 <= t1_t4

	t1_t4_mem1 = S.Task('t1_t4_mem1', length=1, delay_cost=1)
	t1_t4_mem1 += MAS_MEM[1]
	S += 7 < t1_t4_mem1
	S += t1_t4_mem1 <= t1_t4

	t10 = S.Task('t10', length=3, delay_cost=1)
	t10 += alt(MAS)
	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	t10_in += alt(MAS_in)
	S += t10_in*MAS_in[0]<=t10*MAS[0]

	S += t10_in*MAS_in[1]<=t10*MAS[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += MM_MEM[0]
	S += 38 < t10_mem0
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += MM_MEM[1]
	S += 36 < t10_mem1
	S += t10_mem1 <= t10

	t1_t5 = S.Task('t1_t5', length=3, delay_cost=1)
	t1_t5 += alt(MAS)
	t1_t5_in = S.Task('t1_t5_in', length=1, delay_cost=1)
	t1_t5_in += alt(MAS_in)
	S += t1_t5_in*MAS_in[0]<=t1_t5*MAS[0]

	S += t1_t5_in*MAS_in[1]<=t1_t5*MAS[1]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	t1_t5_mem0 += MM_MEM[0]
	S += 38 < t1_t5_mem0
	S += t1_t5_mem0 <= t1_t5

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	t1_t5_mem1 += MM_MEM[1]
	S += 36 < t1_t5_mem1
	S += t1_t5_mem1 <= t1_t5

	t2_t4 = S.Task('t2_t4', length=11, delay_cost=1)
	t2_t4 += alt(MM)
	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	t2_t4_in += alt(MM_in)
	S += t2_t4_in*MM_in[0]<=t2_t4*MM[0]
	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	t2_t4_mem0 += MAS_MEM[2]
	S += 3 < t2_t4_mem0
	S += t2_t4_mem0 <= t2_t4

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	t2_t4_mem1 += MAS_MEM[1]
	S += 8 < t2_t4_mem1
	S += t2_t4_mem1 <= t2_t4

	t20 = S.Task('t20', length=3, delay_cost=1)
	t20 += alt(MAS)
	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	t20_in += alt(MAS_in)
	S += t20_in*MAS_in[0]<=t20*MAS[0]

	S += t20_in*MAS_in[1]<=t20*MAS[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += MM_MEM[0]
	S += 33 < t20_mem0
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += MM_MEM[1]
	S += 26 < t20_mem1
	S += t20_mem1 <= t20

	t2_t5 = S.Task('t2_t5', length=3, delay_cost=1)
	t2_t5 += alt(MAS)
	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	t2_t5_in += alt(MAS_in)
	S += t2_t5_in*MAS_in[0]<=t2_t5*MAS[0]

	S += t2_t5_in*MAS_in[1]<=t2_t5*MAS[1]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	t2_t5_mem0 += MM_MEM[0]
	S += 33 < t2_t5_mem0
	S += t2_t5_mem0 <= t2_t5

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	t2_t5_mem1 += MM_MEM[1]
	S += 26 < t2_t5_mem1
	S += t2_t5_mem1 <= t2_t5

	t0_t4 = S.Task('t0_t4', length=11, delay_cost=1)
	t0_t4 += alt(MM)
	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	t0_t4_in += alt(MM_in)
	S += t0_t4_in*MM_in[0]<=t0_t4*MM[0]
	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	t0_t4_mem0 += MAS_MEM[0]
	S += 29 < t0_t4_mem0
	S += t0_t4_mem0 <= t0_t4

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	t0_t4_mem1 += MAS_MEM[1]
	S += 23 < t0_t4_mem1
	S += t0_t4_mem1 <= t0_t4

	t00 = S.Task('t00', length=3, delay_cost=1)
	t00 += alt(MAS)
	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	t00_in += alt(MAS_in)
	S += t00_in*MAS_in[0]<=t00*MAS[0]

	S += t00_in*MAS_in[1]<=t00*MAS[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += MM_MEM[0]
	S += 40 < t00_mem0
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += MM_MEM[1]
	S += 39 < t00_mem1
	S += t00_mem1 <= t00

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	t0_t5 += alt(MAS)
	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	t0_t5_in += alt(MAS_in)
	S += t0_t5_in*MAS_in[0]<=t0_t5*MAS[0]

	S += t0_t5_in*MAS_in[1]<=t0_t5*MAS[1]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MM_MEM[0]
	S += 40 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	t0_t5_mem1 += MM_MEM[1]
	S += 39 < t0_t5_mem1
	S += t0_t5_mem1 <= t0_t5

	t4_t0_t4 = S.Task('t4_t0_t4', length=11, delay_cost=1)
	t4_t0_t4 += alt(MM)
	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	t4_t0_t4_in += alt(MM_in)
	S += t4_t0_t4_in*MM_in[0]<=t4_t0_t4*MM[0]
	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	t4_t0_t4_mem0 += MAS_MEM[2]
	S += 10 < t4_t0_t4_mem0
	S += t4_t0_t4_mem0 <= t4_t0_t4

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	t4_t0_t4_mem1 += MAS_MEM[1]
	S += 11 < t4_t0_t4_mem1
	S += t4_t0_t4_mem1 <= t4_t0_t4

	t4_t00 = S.Task('t4_t00', length=3, delay_cost=1)
	t4_t00 += alt(MAS)
	t4_t00_in = S.Task('t4_t00_in', length=1, delay_cost=1)
	t4_t00_in += alt(MAS_in)
	S += t4_t00_in*MAS_in[0]<=t4_t00*MAS[0]

	S += t4_t00_in*MAS_in[1]<=t4_t00*MAS[1]

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	t4_t00_mem0 += MM_MEM[0]
	S += 25 < t4_t00_mem0
	S += t4_t00_mem0 <= t4_t00

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	t4_t00_mem1 += MM_MEM[1]
	S += 29 < t4_t00_mem1
	S += t4_t00_mem1 <= t4_t00

	t4_t0_t5 = S.Task('t4_t0_t5', length=3, delay_cost=1)
	t4_t0_t5 += alt(MAS)
	t4_t0_t5_in = S.Task('t4_t0_t5_in', length=1, delay_cost=1)
	t4_t0_t5_in += alt(MAS_in)
	S += t4_t0_t5_in*MAS_in[0]<=t4_t0_t5*MAS[0]

	S += t4_t0_t5_in*MAS_in[1]<=t4_t0_t5*MAS[1]

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	t4_t0_t5_mem0 += MM_MEM[0]
	S += 25 < t4_t0_t5_mem0
	S += t4_t0_t5_mem0 <= t4_t0_t5

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	t4_t0_t5_mem1 += MM_MEM[1]
	S += 29 < t4_t0_t5_mem1
	S += t4_t0_t5_mem1 <= t4_t0_t5

	t4_t1_t4 = S.Task('t4_t1_t4', length=11, delay_cost=1)
	t4_t1_t4 += alt(MM)
	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	t4_t1_t4_in += alt(MM_in)
	S += t4_t1_t4_in*MM_in[0]<=t4_t1_t4*MM[0]
	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	t4_t1_t4_mem0 += MAS_MEM[0]
	S += 9 < t4_t1_t4_mem0
	S += t4_t1_t4_mem0 <= t4_t1_t4

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	t4_t1_t4_mem1 += MAS_MEM[3]
	S += 26 < t4_t1_t4_mem1
	S += t4_t1_t4_mem1 <= t4_t1_t4

	t4_t10 = S.Task('t4_t10', length=3, delay_cost=1)
	t4_t10 += alt(MAS)
	t4_t10_in = S.Task('t4_t10_in', length=1, delay_cost=1)
	t4_t10_in += alt(MAS_in)
	S += t4_t10_in*MAS_in[0]<=t4_t10*MAS[0]

	S += t4_t10_in*MAS_in[1]<=t4_t10*MAS[1]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	t4_t10_mem0 += MM_MEM[0]
	S += 24 < t4_t10_mem0
	S += t4_t10_mem0 <= t4_t10

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	t4_t10_mem1 += MM_MEM[1]
	S += 22 < t4_t10_mem1
	S += t4_t10_mem1 <= t4_t10

	t4_t1_t5 = S.Task('t4_t1_t5', length=3, delay_cost=1)
	t4_t1_t5 += alt(MAS)
	t4_t1_t5_in = S.Task('t4_t1_t5_in', length=1, delay_cost=1)
	t4_t1_t5_in += alt(MAS_in)
	S += t4_t1_t5_in*MAS_in[0]<=t4_t1_t5*MAS[0]

	S += t4_t1_t5_in*MAS_in[1]<=t4_t1_t5*MAS[1]

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	t4_t1_t5_mem0 += MM_MEM[0]
	S += 24 < t4_t1_t5_mem0
	S += t4_t1_t5_mem0 <= t4_t1_t5

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	t4_t1_t5_mem1 += MM_MEM[1]
	S += 22 < t4_t1_t5_mem1
	S += t4_t1_t5_mem1 <= t4_t1_t5

	t4_t2_t4 = S.Task('t4_t2_t4', length=11, delay_cost=1)
	t4_t2_t4 += alt(MM)
	t4_t2_t4_in = S.Task('t4_t2_t4_in', length=1, delay_cost=1)
	t4_t2_t4_in += alt(MM_in)
	S += t4_t2_t4_in*MM_in[0]<=t4_t2_t4*MM[0]
	t4_t2_t4_mem0 = S.Task('t4_t2_t4_mem0', length=1, delay_cost=1)
	t4_t2_t4_mem0 += MAS_MEM[0]
	S += 13 < t4_t2_t4_mem0
	S += t4_t2_t4_mem0 <= t4_t2_t4

	t4_t2_t4_mem1 = S.Task('t4_t2_t4_mem1', length=1, delay_cost=1)
	t4_t2_t4_mem1 += MAS_MEM[1]
	S += 15 < t4_t2_t4_mem1
	S += t4_t2_t4_mem1 <= t4_t2_t4

	t4_t20 = S.Task('t4_t20', length=3, delay_cost=1)
	t4_t20 += alt(MAS)
	t4_t20_in = S.Task('t4_t20_in', length=1, delay_cost=1)
	t4_t20_in += alt(MAS_in)
	S += t4_t20_in*MAS_in[0]<=t4_t20*MAS[0]

	S += t4_t20_in*MAS_in[1]<=t4_t20*MAS[1]

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	t4_t20_mem0 += MM_MEM[0]
	S += 30 < t4_t20_mem0
	S += t4_t20_mem0 <= t4_t20

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	t4_t20_mem1 += MM_MEM[1]
	S += 28 < t4_t20_mem1
	S += t4_t20_mem1 <= t4_t20

	t4_t2_t5 = S.Task('t4_t2_t5', length=3, delay_cost=1)
	t4_t2_t5 += alt(MAS)
	t4_t2_t5_in = S.Task('t4_t2_t5_in', length=1, delay_cost=1)
	t4_t2_t5_in += alt(MAS_in)
	S += t4_t2_t5_in*MAS_in[0]<=t4_t2_t5*MAS[0]

	S += t4_t2_t5_in*MAS_in[1]<=t4_t2_t5*MAS[1]

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	t4_t2_t5_mem0 += MM_MEM[0]
	S += 30 < t4_t2_t5_mem0
	S += t4_t2_t5_mem0 <= t4_t2_t5

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	t4_t2_t5_mem1 += MM_MEM[1]
	S += 28 < t4_t2_t5_mem1
	S += t4_t2_t5_mem1 <= t4_t2_t5

	t4_t6_t0 = S.Task('t4_t6_t0', length=11, delay_cost=1)
	t4_t6_t0 += alt(MM)
	t4_t6_t0_in = S.Task('t4_t6_t0_in', length=1, delay_cost=1)
	t4_t6_t0_in += alt(MM_in)
	S += t4_t6_t0_in*MM_in[0]<=t4_t6_t0*MM[0]
	t4_t6_t0_mem0 = S.Task('t4_t6_t0_mem0', length=1, delay_cost=1)
	t4_t6_t0_mem0 += MAS_MEM[0]
	S += 19 < t4_t6_t0_mem0
	S += t4_t6_t0_mem0 <= t4_t6_t0

	t4_t6_t0_mem1 = S.Task('t4_t6_t0_mem1', length=1, delay_cost=1)
	t4_t6_t0_mem1 += MAS_MEM[3]
	S += 27 < t4_t6_t0_mem1
	S += t4_t6_t0_mem1 <= t4_t6_t0

	t4_t6_t1 = S.Task('t4_t6_t1', length=11, delay_cost=1)
	t4_t6_t1 += alt(MM)
	t4_t6_t1_in = S.Task('t4_t6_t1_in', length=1, delay_cost=1)
	t4_t6_t1_in += alt(MM_in)
	S += t4_t6_t1_in*MM_in[0]<=t4_t6_t1*MM[0]
	t4_t6_t1_mem0 = S.Task('t4_t6_t1_mem0', length=1, delay_cost=1)
	t4_t6_t1_mem0 += MAS_MEM[0]
	S += 4 < t4_t6_t1_mem0
	S += t4_t6_t1_mem0 <= t4_t6_t1

	t4_t6_t1_mem1 = S.Task('t4_t6_t1_mem1', length=1, delay_cost=1)
	t4_t6_t1_mem1 += MAS_MEM[1]
	S += 5 < t4_t6_t1_mem1
	S += t4_t6_t1_mem1 <= t4_t6_t1

	t4_t6_t2 = S.Task('t4_t6_t2', length=3, delay_cost=1)
	t4_t6_t2 += alt(MAS)
	t4_t6_t2_in = S.Task('t4_t6_t2_in', length=1, delay_cost=1)
	t4_t6_t2_in += alt(MAS_in)
	S += t4_t6_t2_in*MAS_in[0]<=t4_t6_t2*MAS[0]

	S += t4_t6_t2_in*MAS_in[1]<=t4_t6_t2*MAS[1]

	t4_t6_t2_mem0 = S.Task('t4_t6_t2_mem0', length=1, delay_cost=1)
	t4_t6_t2_mem0 += MAS_MEM[0]
	S += 19 < t4_t6_t2_mem0
	S += t4_t6_t2_mem0 <= t4_t6_t2

	t4_t6_t2_mem1 = S.Task('t4_t6_t2_mem1', length=1, delay_cost=1)
	t4_t6_t2_mem1 += MAS_MEM[1]
	S += 4 < t4_t6_t2_mem1
	S += t4_t6_t2_mem1 <= t4_t6_t2

	t4_t6_t3 = S.Task('t4_t6_t3', length=3, delay_cost=1)
	t4_t6_t3 += alt(MAS)
	t4_t6_t3_in = S.Task('t4_t6_t3_in', length=1, delay_cost=1)
	t4_t6_t3_in += alt(MAS_in)
	S += t4_t6_t3_in*MAS_in[0]<=t4_t6_t3*MAS[0]

	S += t4_t6_t3_in*MAS_in[1]<=t4_t6_t3*MAS[1]

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	t4_t6_t3_mem0 += MAS_MEM[2]
	S += 27 < t4_t6_t3_mem0
	S += t4_t6_t3_mem0 <= t4_t6_t3

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	t4_t6_t3_mem1 += MAS_MEM[1]
	S += 5 < t4_t6_t3_mem1
	S += t4_t6_t3_mem1 <= t4_t6_t3

	t4_t8_t4 = S.Task('t4_t8_t4', length=11, delay_cost=1)
	t4_t8_t4 += alt(MM)
	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	t4_t8_t4_in += alt(MM_in)
	S += t4_t8_t4_in*MM_in[0]<=t4_t8_t4*MM[0]
	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	t4_t8_t4_mem0 += MAS_MEM[2]
	S += 43 < t4_t8_t4_mem0
	S += t4_t8_t4_mem0 <= t4_t8_t4

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	t4_t8_t4_mem1 += MAS_MEM[1]
	S += 41 < t4_t8_t4_mem1
	S += t4_t8_t4_mem1 <= t4_t8_t4

	t4_t80 = S.Task('t4_t80', length=3, delay_cost=1)
	t4_t80 += alt(MAS)
	t4_t80_in = S.Task('t4_t80_in', length=1, delay_cost=1)
	t4_t80_in += alt(MAS_in)
	S += t4_t80_in*MAS_in[0]<=t4_t80*MAS[0]

	S += t4_t80_in*MAS_in[1]<=t4_t80*MAS[1]

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	t4_t80_mem0 += MM_MEM[0]
	S += 20 < t4_t80_mem0
	S += t4_t80_mem0 <= t4_t80

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	t4_t80_mem1 += MM_MEM[1]
	S += 32 < t4_t80_mem1
	S += t4_t80_mem1 <= t4_t80

	t4_t8_t5 = S.Task('t4_t8_t5', length=3, delay_cost=1)
	t4_t8_t5 += alt(MAS)
	t4_t8_t5_in = S.Task('t4_t8_t5_in', length=1, delay_cost=1)
	t4_t8_t5_in += alt(MAS_in)
	S += t4_t8_t5_in*MAS_in[0]<=t4_t8_t5*MAS[0]

	S += t4_t8_t5_in*MAS_in[1]<=t4_t8_t5*MAS[1]

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	t4_t8_t5_mem0 += MM_MEM[0]
	S += 20 < t4_t8_t5_mem0
	S += t4_t8_t5_mem0 <= t4_t8_t5

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	t4_t8_t5_mem1 += MM_MEM[1]
	S += 32 < t4_t8_t5_mem1
	S += t4_t8_t5_mem1 <= t4_t8_t5

	t5_t0_t0 = S.Task('t5_t0_t0', length=11, delay_cost=1)
	t5_t0_t0 += alt(MM)
	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	t5_t0_t0_in += alt(MM_in)
	S += t5_t0_t0_in*MM_in[0]<=t5_t0_t0*MM[0]
	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	t5_t0_t0_mem0 += MAIN_MEM_r[0]
	S += t5_t0_t0_mem0 <= t5_t0_t0

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	t5_t0_t0_mem1 += MAS_MEM[1]
	S += 37 < t5_t0_t0_mem1
	S += t5_t0_t0_mem1 <= t5_t0_t0

	t5_t0_t1 = S.Task('t5_t0_t1', length=11, delay_cost=1)
	t5_t0_t1 += alt(MM)
	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	t5_t0_t1_in += alt(MM_in)
	S += t5_t0_t1_in*MM_in[0]<=t5_t0_t1*MM[0]
	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	t5_t0_t1_mem0 += MAIN_MEM_r[0]
	S += t5_t0_t1_mem0 <= t5_t0_t1

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	t5_t0_t1_mem1 += MAS_MEM[1]
	S += 44 < t5_t0_t1_mem1
	S += t5_t0_t1_mem1 <= t5_t0_t1

	t5_t0_t3 = S.Task('t5_t0_t3', length=3, delay_cost=1)
	t5_t0_t3 += alt(MAS)
	t5_t0_t3_in = S.Task('t5_t0_t3_in', length=1, delay_cost=1)
	t5_t0_t3_in += alt(MAS_in)
	S += t5_t0_t3_in*MAS_in[0]<=t5_t0_t3*MAS[0]

	S += t5_t0_t3_in*MAS_in[1]<=t5_t0_t3*MAS[1]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	t5_t0_t3_mem0 += MAS_MEM[0]
	S += 37 < t5_t0_t3_mem0
	S += t5_t0_t3_mem0 <= t5_t0_t3

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	t5_t0_t3_mem1 += MAS_MEM[1]
	S += 44 < t5_t0_t3_mem1
	S += t5_t0_t3_mem1 <= t5_t0_t3

	t5_t1_t0 = S.Task('t5_t1_t0', length=11, delay_cost=1)
	t5_t1_t0 += alt(MM)
	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	t5_t1_t0_in += alt(MM_in)
	S += t5_t1_t0_in*MM_in[0]<=t5_t1_t0*MM[0]
	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	t5_t1_t0_mem0 += MAS_MEM[0]
	S += 42 < t5_t1_t0_mem0
	S += t5_t1_t0_mem0 <= t5_t1_t0

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	t5_t1_t0_mem1 += MAS_MEM[1]
	S += 39 < t5_t1_t0_mem1
	S += t5_t1_t0_mem1 <= t5_t1_t0

	t5_t1_t1 = S.Task('t5_t1_t1', length=11, delay_cost=1)
	t5_t1_t1 += alt(MM)
	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	t5_t1_t1_in += alt(MM_in)
	S += t5_t1_t1_in*MM_in[0]<=t5_t1_t1*MM[0]
	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	t5_t1_t1_mem0 += MAS_MEM[0]
	S += 36 < t5_t1_t1_mem0
	S += t5_t1_t1_mem0 <= t5_t1_t1

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	t5_t1_t1_mem1 += MAS_MEM[3]
	S += 40 < t5_t1_t1_mem1
	S += t5_t1_t1_mem1 <= t5_t1_t1

	t5_t1_t2 = S.Task('t5_t1_t2', length=3, delay_cost=1)
	t5_t1_t2 += alt(MAS)
	t5_t1_t2_in = S.Task('t5_t1_t2_in', length=1, delay_cost=1)
	t5_t1_t2_in += alt(MAS_in)
	S += t5_t1_t2_in*MAS_in[0]<=t5_t1_t2*MAS[0]

	S += t5_t1_t2_in*MAS_in[1]<=t5_t1_t2*MAS[1]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	t5_t1_t2_mem0 += MAS_MEM[0]
	S += 42 < t5_t1_t2_mem0
	S += t5_t1_t2_mem0 <= t5_t1_t2

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	t5_t1_t2_mem1 += MAS_MEM[1]
	S += 36 < t5_t1_t2_mem1
	S += t5_t1_t2_mem1 <= t5_t1_t2

	t5_t1_t3 = S.Task('t5_t1_t3', length=3, delay_cost=1)
	t5_t1_t3 += alt(MAS)
	t5_t1_t3_in = S.Task('t5_t1_t3_in', length=1, delay_cost=1)
	t5_t1_t3_in += alt(MAS_in)
	S += t5_t1_t3_in*MAS_in[0]<=t5_t1_t3*MAS[0]

	S += t5_t1_t3_in*MAS_in[1]<=t5_t1_t3*MAS[1]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	t5_t1_t3_mem0 += MAS_MEM[0]
	S += 39 < t5_t1_t3_mem0
	S += t5_t1_t3_mem0 <= t5_t1_t3

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	t5_t1_t3_mem1 += MAS_MEM[3]
	S += 40 < t5_t1_t3_mem1
	S += t5_t1_t3_mem1 <= t5_t1_t3

	t5_t2_t0 = S.Task('t5_t2_t0', length=11, delay_cost=1)
	t5_t2_t0 += alt(MM)
	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	t5_t2_t0_in += alt(MM_in)
	S += t5_t2_t0_in*MM_in[0]<=t5_t2_t0*MM[0]
	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	t5_t2_t0_mem0 += MAS_MEM[0]
	S += 42 < t5_t2_t0_mem0
	S += t5_t2_t0_mem0 <= t5_t2_t0

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	t5_t2_t0_mem1 += MAS_MEM[3]
	S += 38 < t5_t2_t0_mem1
	S += t5_t2_t0_mem1 <= t5_t2_t0

	t5_t2_t1 = S.Task('t5_t2_t1', length=11, delay_cost=1)
	t5_t2_t1 += alt(MM)
	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	t5_t2_t1_in += alt(MM_in)
	S += t5_t2_t1_in*MM_in[0]<=t5_t2_t1*MM[0]
	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	t5_t2_t1_mem0 += MAS_MEM[0]
	S += 36 < t5_t2_t1_mem0
	S += t5_t2_t1_mem0 <= t5_t2_t1

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	t5_t2_t1_mem1 += MAS_MEM[3]
	S += 35 < t5_t2_t1_mem1
	S += t5_t2_t1_mem1 <= t5_t2_t1

	t5_t2_t2 = S.Task('t5_t2_t2', length=3, delay_cost=1)
	t5_t2_t2 += alt(MAS)
	t5_t2_t2_in = S.Task('t5_t2_t2_in', length=1, delay_cost=1)
	t5_t2_t2_in += alt(MAS_in)
	S += t5_t2_t2_in*MAS_in[0]<=t5_t2_t2*MAS[0]

	S += t5_t2_t2_in*MAS_in[1]<=t5_t2_t2*MAS[1]

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	t5_t2_t2_mem0 += MAS_MEM[0]
	S += 42 < t5_t2_t2_mem0
	S += t5_t2_t2_mem0 <= t5_t2_t2

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	t5_t2_t2_mem1 += MAS_MEM[1]
	S += 36 < t5_t2_t2_mem1
	S += t5_t2_t2_mem1 <= t5_t2_t2

	t5_t2_t3 = S.Task('t5_t2_t3', length=3, delay_cost=1)
	t5_t2_t3 += alt(MAS)
	t5_t2_t3_in = S.Task('t5_t2_t3_in', length=1, delay_cost=1)
	t5_t2_t3_in += alt(MAS_in)
	S += t5_t2_t3_in*MAS_in[0]<=t5_t2_t3*MAS[0]

	S += t5_t2_t3_in*MAS_in[1]<=t5_t2_t3*MAS[1]

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	t5_t2_t3_mem0 += MAS_MEM[2]
	S += 38 < t5_t2_t3_mem0
	S += t5_t2_t3_mem0 <= t5_t2_t3

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	t5_t2_t3_mem1 += MAS_MEM[3]
	S += 35 < t5_t2_t3_mem1
	S += t5_t2_t3_mem1 <= t5_t2_t3

	t5_t40 = S.Task('t5_t40', length=3, delay_cost=1)
	t5_t40 += alt(MAS)
	t5_t40_in = S.Task('t5_t40_in', length=1, delay_cost=1)
	t5_t40_in += alt(MAS_in)
	S += t5_t40_in*MAS_in[0]<=t5_t40*MAS[0]

	S += t5_t40_in*MAS_in[1]<=t5_t40*MAS[1]

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	t5_t40_mem0 += MAIN_MEM_r[0]
	S += t5_t40_mem0 <= t5_t40

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	t5_t40_mem1 += MAS_MEM[1]
	S += 42 < t5_t40_mem1
	S += t5_t40_mem1 <= t5_t40

	t5_t41 = S.Task('t5_t41', length=3, delay_cost=1)
	t5_t41 += alt(MAS)
	t5_t41_in = S.Task('t5_t41_in', length=1, delay_cost=1)
	t5_t41_in += alt(MAS_in)
	S += t5_t41_in*MAS_in[0]<=t5_t41*MAS[0]

	S += t5_t41_in*MAS_in[1]<=t5_t41*MAS[1]

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	t5_t41_mem0 += MAIN_MEM_r[0]
	S += t5_t41_mem0 <= t5_t41

	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	t5_t41_mem1 += MAS_MEM[1]
	S += 36 < t5_t41_mem1
	S += t5_t41_mem1 <= t5_t41

	t5_t50 = S.Task('t5_t50', length=3, delay_cost=1)
	t5_t50 += alt(MAS)
	t5_t50_in = S.Task('t5_t50_in', length=1, delay_cost=1)
	t5_t50_in += alt(MAS_in)
	S += t5_t50_in*MAS_in[0]<=t5_t50*MAS[0]

	S += t5_t50_in*MAS_in[1]<=t5_t50*MAS[1]

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	t5_t50_mem0 += MAS_MEM[0]
	S += 37 < t5_t50_mem0
	S += t5_t50_mem0 <= t5_t50

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	t5_t50_mem1 += MAS_MEM[1]
	S += 39 < t5_t50_mem1
	S += t5_t50_mem1 <= t5_t50

	t5_t51 = S.Task('t5_t51', length=3, delay_cost=1)
	t5_t51 += alt(MAS)
	t5_t51_in = S.Task('t5_t51_in', length=1, delay_cost=1)
	t5_t51_in += alt(MAS_in)
	S += t5_t51_in*MAS_in[0]<=t5_t51*MAS[0]

	S += t5_t51_in*MAS_in[1]<=t5_t51*MAS[1]

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	t5_t51_mem0 += MAS_MEM[0]
	S += 44 < t5_t51_mem0
	S += t5_t51_mem0 <= t5_t51

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	t5_t51_mem1 += MAS_MEM[3]
	S += 40 < t5_t51_mem1
	S += t5_t51_mem1 <= t5_t51

	t5_t8_t0 = S.Task('t5_t8_t0', length=11, delay_cost=1)
	t5_t8_t0 += alt(MM)
	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	t5_t8_t0_in += alt(MM_in)
	S += t5_t8_t0_in*MM_in[0]<=t5_t8_t0*MM[0]
	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	t5_t8_t0_mem0 += MAIN_MEM_r[0]
	S += t5_t8_t0_mem0 <= t5_t8_t0

	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	t5_t8_t0_mem1 += MAS_MEM[3]
	S += 38 < t5_t8_t0_mem1
	S += t5_t8_t0_mem1 <= t5_t8_t0

	t5_t8_t1 = S.Task('t5_t8_t1', length=11, delay_cost=1)
	t5_t8_t1 += alt(MM)
	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	t5_t8_t1_in += alt(MM_in)
	S += t5_t8_t1_in*MM_in[0]<=t5_t8_t1*MM[0]
	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	t5_t8_t1_mem0 += MAIN_MEM_r[0]
	S += t5_t8_t1_mem0 <= t5_t8_t1

	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	t5_t8_t1_mem1 += MAS_MEM[3]
	S += 35 < t5_t8_t1_mem1
	S += t5_t8_t1_mem1 <= t5_t8_t1

	t5_t8_t3 = S.Task('t5_t8_t3', length=3, delay_cost=1)
	t5_t8_t3 += alt(MAS)
	t5_t8_t3_in = S.Task('t5_t8_t3_in', length=1, delay_cost=1)
	t5_t8_t3_in += alt(MAS_in)
	S += t5_t8_t3_in*MAS_in[0]<=t5_t8_t3*MAS[0]

	S += t5_t8_t3_in*MAS_in[1]<=t5_t8_t3*MAS[1]

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	t5_t8_t3_mem0 += MAS_MEM[2]
	S += 38 < t5_t8_t3_mem0
	S += t5_t8_t3_mem0 <= t5_t8_t3

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	t5_t8_t3_mem1 += MAS_MEM[3]
	S += 35 < t5_t8_t3_mem1
	S += t5_t8_t3_mem1 <= t5_t8_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS2/SPARSE/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution
