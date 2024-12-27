from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 160
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=8)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t4_t41_in = S.Task('t4_t41_in', length=1, delay_cost=1)
	S += t4_t41_in >= 0
	t4_t41_in += MAS_in[4]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 0
	t4_t41_mem0 += MAIN_MEM_r[0]

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 0
	t4_t41_mem1 += MAIN_MEM_r[1]

	t4_t41 = S.Task('t4_t41', length=2, delay_cost=1)
	S += t4_t41 >= 1
	t4_t41 += MAS[4]

	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	S += t4_t8_t0_in >= 1
	t4_t8_t0_in += MM_in[0]

	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	S += t4_t8_t0_mem0 >= 1
	t4_t8_t0_mem0 += MAIN_MEM_r[0]

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	S += t4_t8_t0_mem1 >= 1
	t4_t8_t0_mem1 += MAIN_MEM_r[1]

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	S += t4_t2_t0_in >= 2
	t4_t2_t0_in += MM_in[1]

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	S += t4_t2_t0_mem0 >= 2
	t4_t2_t0_mem0 += MAIN_MEM_r[0]

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	S += t4_t2_t0_mem1 >= 2
	t4_t2_t0_mem1 += MAIN_MEM_r[1]

	t4_t8_t0 = S.Task('t4_t8_t0', length=10, delay_cost=1)
	S += t4_t8_t0 >= 2
	t4_t8_t0 += MM[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 3
	t0_t3_in += MAS_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 3
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 3
	t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t2_t0 = S.Task('t4_t2_t0', length=10, delay_cost=1)
	S += t4_t2_t0 >= 3
	t4_t2_t0 += MM[1]

	t0_t3 = S.Task('t0_t3', length=2, delay_cost=1)
	S += t0_t3 >= 4
	t0_t3 += MAS[0]

	t4_t40_in = S.Task('t4_t40_in', length=1, delay_cost=1)
	S += t4_t40_in >= 4
	t4_t40_in += MAS_in[0]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 4
	t4_t40_mem0 += MAIN_MEM_r[0]

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 4
	t4_t40_mem1 += MAIN_MEM_r[1]

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_in >= 5
	t4_t0_t0_in += MM_in[0]

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_mem0 >= 5
	t4_t0_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_mem1 >= 5
	t4_t0_t0_mem1 += MAIN_MEM_r[1]

	t4_t40 = S.Task('t4_t40', length=2, delay_cost=1)
	S += t4_t40 >= 5
	t4_t40 += MAS[0]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 6
	t0_t2_in += MAS_in[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 6
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 6
	t0_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_t0 = S.Task('t4_t0_t0', length=10, delay_cost=1)
	S += t4_t0_t0 >= 6
	t4_t0_t0 += MM[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 7
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 7
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 7
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t2 = S.Task('t0_t2', length=2, delay_cost=1)
	S += t0_t2 >= 7
	t0_t2 += MAS[1]

	t0_t0 = S.Task('t0_t0', length=10, delay_cost=1)
	S += t0_t0 >= 8
	t0_t0 += MM[0]

	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_in >= 8
	t4_t1_t1_in += MM_in[0]

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_mem0 >= 8
	t4_t1_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_mem1 >= 8
	t4_t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t1_t1 = S.Task('t4_t1_t1', length=10, delay_cost=1)
	S += t4_t1_t1 >= 9
	t4_t1_t1 += MM[0]

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 9
	t4_t2_t1_in += MM_in[1]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 9
	t4_t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 9
	t4_t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t0_t3_in = S.Task('t4_t0_t3_in', length=1, delay_cost=1)
	S += t4_t0_t3_in >= 10
	t4_t0_t3_in += MAS_in[1]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 10
	t4_t0_t3_mem0 += MAIN_MEM_r[0]

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 10
	t4_t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t2_t1 = S.Task('t4_t2_t1', length=10, delay_cost=1)
	S += t4_t2_t1 >= 10
	t4_t2_t1 += MM[1]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 11
	t2_t3_in += MAS_in[2]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 11
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 11
	t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t0_t3 = S.Task('t4_t0_t3', length=2, delay_cost=1)
	S += t4_t0_t3 >= 11
	t4_t0_t3 += MAS[1]

	t2_t3 = S.Task('t2_t3', length=2, delay_cost=1)
	S += t2_t3 >= 12
	t2_t3 += MAS[2]

	t4_t51_in = S.Task('t4_t51_in', length=1, delay_cost=1)
	S += t4_t51_in >= 12
	t4_t51_in += MAS_in[3]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 12
	t4_t51_mem0 += MAIN_MEM_r[0]

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 12
	t4_t51_mem1 += MAIN_MEM_r[1]

	t4_t0_t2_in = S.Task('t4_t0_t2_in', length=1, delay_cost=1)
	S += t4_t0_t2_in >= 13
	t4_t0_t2_in += MAS_in[0]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 13
	t4_t0_t2_mem0 += MAIN_MEM_r[0]

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 13
	t4_t0_t2_mem1 += MAIN_MEM_r[1]

	t4_t51 = S.Task('t4_t51', length=2, delay_cost=1)
	S += t4_t51 >= 13
	t4_t51 += MAS[3]

	t4_t0_t2 = S.Task('t4_t0_t2', length=2, delay_cost=1)
	S += t4_t0_t2 >= 14
	t4_t0_t2 += MAS[0]

	t4_t2_t2_in = S.Task('t4_t2_t2_in', length=1, delay_cost=1)
	S += t4_t2_t2_in >= 14
	t4_t2_t2_in += MAS_in[6]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 14
	t4_t2_t2_mem0 += MAIN_MEM_r[0]

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 14
	t4_t2_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_in >= 15
	t4_t1_t0_in += MM_in[1]

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_mem0 >= 15
	t4_t1_t0_mem0 += MAIN_MEM_r[0]

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_mem1 >= 15
	t4_t1_t0_mem1 += MAIN_MEM_r[1]

	t4_t2_t2 = S.Task('t4_t2_t2', length=2, delay_cost=1)
	S += t4_t2_t2 >= 15
	t4_t2_t2 += MAS[6]

	t4_t1_t0 = S.Task('t4_t1_t0', length=10, delay_cost=1)
	S += t4_t1_t0 >= 16
	t4_t1_t0 += MM[1]

	t4_t2_t3_in = S.Task('t4_t2_t3_in', length=1, delay_cost=1)
	S += t4_t2_t3_in >= 16
	t4_t2_t3_in += MAS_in[1]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 16
	t4_t2_t3_mem0 += MAIN_MEM_r[0]

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 16
	t4_t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t2_t3 = S.Task('t4_t2_t3', length=2, delay_cost=1)
	S += t4_t2_t3 >= 17
	t4_t2_t3 += MAS[1]

	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	S += t4_t8_t1_in >= 17
	t4_t8_t1_in += MM_in[0]

	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	S += t4_t8_t1_mem0 >= 17
	t4_t8_t1_mem0 += MAIN_MEM_r[0]

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	S += t4_t8_t1_mem1 >= 17
	t4_t8_t1_mem1 += MAIN_MEM_r[1]

	t4_t1_t2_in = S.Task('t4_t1_t2_in', length=1, delay_cost=1)
	S += t4_t1_t2_in >= 18
	t4_t1_t2_in += MAS_in[5]

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t2_mem0 >= 18
	t4_t1_t2_mem0 += MAIN_MEM_r[0]

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t2_mem1 >= 18
	t4_t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t8_t1 = S.Task('t4_t8_t1', length=10, delay_cost=1)
	S += t4_t8_t1 >= 18
	t4_t8_t1 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 19
	t0_t1_in += MM_in[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 19
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 19
	t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t1_t2 = S.Task('t4_t1_t2', length=2, delay_cost=1)
	S += t4_t1_t2 >= 19
	t4_t1_t2 += MAS[5]

	t0_t1 = S.Task('t0_t1', length=10, delay_cost=1)
	S += t0_t1 >= 20
	t0_t1 += MM[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 20
	t2_t0_in += MM_in[1]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 20
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 20
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=10, delay_cost=1)
	S += t2_t0 >= 21
	t2_t0 += MM[1]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 21
	t2_t2_in += MAS_in[6]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 21
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 21
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=2, delay_cost=1)
	S += t2_t2 >= 22
	t2_t2 += MAS[6]

	t4_t1_t3_in = S.Task('t4_t1_t3_in', length=1, delay_cost=1)
	S += t4_t1_t3_in >= 22
	t4_t1_t3_in += MAS_in[1]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 22
	t4_t1_t3_mem0 += MAIN_MEM_r[0]

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 22
	t4_t1_t3_mem1 += MAIN_MEM_r[1]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 23
	t1_t2_in += MAS_in[7]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 23
	t1_t2_mem0 += MAIN_MEM_r[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 23
	t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_t3 = S.Task('t4_t1_t3', length=2, delay_cost=1)
	S += t4_t1_t3 >= 23
	t4_t1_t3 += MAS[1]

	t1_t2 = S.Task('t1_t2', length=2, delay_cost=1)
	S += t1_t2 >= 24
	t1_t2 += MAS[7]

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_in >= 24
	t4_t0_t1_in += MM_in[0]

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_mem0 >= 24
	t4_t0_t1_mem0 += MAIN_MEM_r[0]

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_mem1 >= 24
	t4_t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t0_t1 = S.Task('t4_t0_t1', length=10, delay_cost=1)
	S += t4_t0_t1 >= 25
	t4_t0_t1 += MM[0]

	t4_t50_in = S.Task('t4_t50_in', length=1, delay_cost=1)
	S += t4_t50_in >= 25
	t4_t50_in += MAS_in[4]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 25
	t4_t50_mem0 += MAIN_MEM_r[0]

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 25
	t4_t50_mem1 += MAIN_MEM_r[1]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 26
	t1_t1_in += MM_in[1]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 26
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 26
	t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t50 = S.Task('t4_t50', length=2, delay_cost=1)
	S += t4_t50 >= 26
	t4_t50 += MAS[4]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 27
	t1_t0_in += MM_in[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 27
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 27
	t1_t0_mem1 += MAIN_MEM_r[1]

	t1_t1 = S.Task('t1_t1', length=10, delay_cost=1)
	S += t1_t1 >= 27
	t1_t1 += MM[1]

	t1_t0 = S.Task('t1_t0', length=10, delay_cost=1)
	S += t1_t0 >= 28
	t1_t0 += MM[0]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 28
	t1_t3_in += MAS_in[1]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 28
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 28
	t1_t3_mem1 += MAIN_MEM_r[1]

	t1_t3 = S.Task('t1_t3', length=2, delay_cost=1)
	S += t1_t3 >= 29
	t1_t3 += MAS[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 29
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 29
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 29
	t2_t1_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=10, delay_cost=1)
	S += t2_t1 >= 30
	t2_t1 += MM[0]


	# new tasks
	t4_t8_t2 = S.Task('t4_t8_t2', length=2, delay_cost=1)
	t4_t8_t2 += alt(MAS)
	t4_t8_t2_in = S.Task('t4_t8_t2_in', length=1, delay_cost=1)
	t4_t8_t2_in += alt(MAS_in)
	S += t4_t8_t2_in*MAS_in[0]<=t4_t8_t2*MAS[0]

	S += t4_t8_t2_in*MAS_in[1]<=t4_t8_t2*MAS[1]

	S += t4_t8_t2_in*MAS_in[2]<=t4_t8_t2*MAS[2]

	S += t4_t8_t2_in*MAS_in[3]<=t4_t8_t2*MAS[3]

	S += t4_t8_t2_in*MAS_in[4]<=t4_t8_t2*MAS[4]

	S += t4_t8_t2_in*MAS_in[5]<=t4_t8_t2*MAS[5]

	S += t4_t8_t2_in*MAS_in[6]<=t4_t8_t2*MAS[6]

	S += t4_t8_t2_in*MAS_in[7]<=t4_t8_t2*MAS[7]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	t4_t8_t2_mem0 += MAIN_MEM_r[0]
	S += t4_t8_t2_mem0 <= t4_t8_t2

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	t4_t8_t2_mem1 += MAIN_MEM_r[1]
	S += t4_t8_t2_mem1 <= t4_t8_t2

	t4_t8_t3 = S.Task('t4_t8_t3', length=2, delay_cost=1)
	t4_t8_t3 += alt(MAS)
	t4_t8_t3_in = S.Task('t4_t8_t3_in', length=1, delay_cost=1)
	t4_t8_t3_in += alt(MAS_in)
	S += t4_t8_t3_in*MAS_in[0]<=t4_t8_t3*MAS[0]

	S += t4_t8_t3_in*MAS_in[1]<=t4_t8_t3*MAS[1]

	S += t4_t8_t3_in*MAS_in[2]<=t4_t8_t3*MAS[2]

	S += t4_t8_t3_in*MAS_in[3]<=t4_t8_t3*MAS[3]

	S += t4_t8_t3_in*MAS_in[4]<=t4_t8_t3*MAS[4]

	S += t4_t8_t3_in*MAS_in[5]<=t4_t8_t3*MAS[5]

	S += t4_t8_t3_in*MAS_in[6]<=t4_t8_t3*MAS[6]

	S += t4_t8_t3_in*MAS_in[7]<=t4_t8_t3*MAS[7]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	t4_t8_t3_mem0 += MAIN_MEM_r[0]
	S += t4_t8_t3_mem0 <= t4_t8_t3

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	t4_t8_t3_mem1 += MAIN_MEM_r[1]
	S += t4_t8_t3_mem1 <= t4_t8_t3

	t70 = S.Task('t70', length=2, delay_cost=1)
	t70 += alt(MAS)
	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	t70_in += alt(MAS_in)
	S += t70_in*MAS_in[0]<=t70*MAS[0]

	S += t70_in*MAS_in[1]<=t70*MAS[1]

	S += t70_in*MAS_in[2]<=t70*MAS[2]

	S += t70_in*MAS_in[3]<=t70*MAS[3]

	S += t70_in*MAS_in[4]<=t70*MAS[4]

	S += t70_in*MAS_in[5]<=t70*MAS[5]

	S += t70_in*MAS_in[6]<=t70*MAS[6]

	S += t70_in*MAS_in[7]<=t70*MAS[7]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += MAIN_MEM_r[0]
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += MAIN_MEM_r[1]
	S += t70_mem1 <= t70

	t71 = S.Task('t71', length=2, delay_cost=1)
	t71 += alt(MAS)
	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	t71_in += alt(MAS_in)
	S += t71_in*MAS_in[0]<=t71*MAS[0]

	S += t71_in*MAS_in[1]<=t71*MAS[1]

	S += t71_in*MAS_in[2]<=t71*MAS[2]

	S += t71_in*MAS_in[3]<=t71*MAS[3]

	S += t71_in*MAS_in[4]<=t71*MAS[4]

	S += t71_in*MAS_in[5]<=t71*MAS[5]

	S += t71_in*MAS_in[6]<=t71*MAS[6]

	S += t71_in*MAS_in[7]<=t71*MAS[7]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	t71_mem0 += MAIN_MEM_r[0]
	S += t71_mem0 <= t71

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	t71_mem1 += MAIN_MEM_r[1]
	S += t71_mem1 <= t71

	t80 = S.Task('t80', length=2, delay_cost=1)
	t80 += alt(MAS)
	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	t80_in += alt(MAS_in)
	S += t80_in*MAS_in[0]<=t80*MAS[0]

	S += t80_in*MAS_in[1]<=t80*MAS[1]

	S += t80_in*MAS_in[2]<=t80*MAS[2]

	S += t80_in*MAS_in[3]<=t80*MAS[3]

	S += t80_in*MAS_in[4]<=t80*MAS[4]

	S += t80_in*MAS_in[5]<=t80*MAS[5]

	S += t80_in*MAS_in[6]<=t80*MAS[6]

	S += t80_in*MAS_in[7]<=t80*MAS[7]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += MAIN_MEM_r[0]
	S += t80_mem0 <= t80

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	t80_mem1 += MAIN_MEM_r[1]
	S += t80_mem1 <= t80

	t81 = S.Task('t81', length=2, delay_cost=1)
	t81 += alt(MAS)
	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	t81_in += alt(MAS_in)
	S += t81_in*MAS_in[0]<=t81*MAS[0]

	S += t81_in*MAS_in[1]<=t81*MAS[1]

	S += t81_in*MAS_in[2]<=t81*MAS[2]

	S += t81_in*MAS_in[3]<=t81*MAS[3]

	S += t81_in*MAS_in[4]<=t81*MAS[4]

	S += t81_in*MAS_in[5]<=t81*MAS[5]

	S += t81_in*MAS_in[6]<=t81*MAS[6]

	S += t81_in*MAS_in[7]<=t81*MAS[7]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += MAIN_MEM_r[0]
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += MAIN_MEM_r[1]
	S += t81_mem1 <= t81

	t90 = S.Task('t90', length=2, delay_cost=1)
	t90 += alt(MAS)
	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	t90_in += alt(MAS_in)
	S += t90_in*MAS_in[0]<=t90*MAS[0]

	S += t90_in*MAS_in[1]<=t90*MAS[1]

	S += t90_in*MAS_in[2]<=t90*MAS[2]

	S += t90_in*MAS_in[3]<=t90*MAS[3]

	S += t90_in*MAS_in[4]<=t90*MAS[4]

	S += t90_in*MAS_in[5]<=t90*MAS[5]

	S += t90_in*MAS_in[6]<=t90*MAS[6]

	S += t90_in*MAS_in[7]<=t90*MAS[7]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += MAIN_MEM_r[0]
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += MAIN_MEM_r[1]
	S += t90_mem1 <= t90

	t91 = S.Task('t91', length=2, delay_cost=1)
	t91 += alt(MAS)
	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	t91_in += alt(MAS_in)
	S += t91_in*MAS_in[0]<=t91*MAS[0]

	S += t91_in*MAS_in[1]<=t91*MAS[1]

	S += t91_in*MAS_in[2]<=t91*MAS[2]

	S += t91_in*MAS_in[3]<=t91*MAS[3]

	S += t91_in*MAS_in[4]<=t91*MAS[4]

	S += t91_in*MAS_in[5]<=t91*MAS[5]

	S += t91_in*MAS_in[6]<=t91*MAS[6]

	S += t91_in*MAS_in[7]<=t91*MAS[7]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	t91_mem0 += MAIN_MEM_r[0]
	S += t91_mem0 <= t91

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	t91_mem1 += MAIN_MEM_r[1]
	S += t91_mem1 <= t91

	t100 = S.Task('t100', length=2, delay_cost=1)
	t100 += alt(MAS)
	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	t100_in += alt(MAS_in)
	S += t100_in*MAS_in[0]<=t100*MAS[0]

	S += t100_in*MAS_in[1]<=t100*MAS[1]

	S += t100_in*MAS_in[2]<=t100*MAS[2]

	S += t100_in*MAS_in[3]<=t100*MAS[3]

	S += t100_in*MAS_in[4]<=t100*MAS[4]

	S += t100_in*MAS_in[5]<=t100*MAS[5]

	S += t100_in*MAS_in[6]<=t100*MAS[6]

	S += t100_in*MAS_in[7]<=t100*MAS[7]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += MAIN_MEM_r[0]
	S += t100_mem0 <= t100

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	t100_mem1 += MAIN_MEM_r[1]
	S += t100_mem1 <= t100

	t101 = S.Task('t101', length=2, delay_cost=1)
	t101 += alt(MAS)
	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	t101_in += alt(MAS_in)
	S += t101_in*MAS_in[0]<=t101*MAS[0]

	S += t101_in*MAS_in[1]<=t101*MAS[1]

	S += t101_in*MAS_in[2]<=t101*MAS[2]

	S += t101_in*MAS_in[3]<=t101*MAS[3]

	S += t101_in*MAS_in[4]<=t101*MAS[4]

	S += t101_in*MAS_in[5]<=t101*MAS[5]

	S += t101_in*MAS_in[6]<=t101*MAS[6]

	S += t101_in*MAS_in[7]<=t101*MAS[7]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += MAIN_MEM_r[0]
	S += t101_mem0 <= t101

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	t101_mem1 += MAIN_MEM_r[1]
	S += t101_mem1 <= t101

	t5_t0_t2 = S.Task('t5_t0_t2', length=2, delay_cost=1)
	t5_t0_t2 += alt(MAS)
	t5_t0_t2_in = S.Task('t5_t0_t2_in', length=1, delay_cost=1)
	t5_t0_t2_in += alt(MAS_in)
	S += t5_t0_t2_in*MAS_in[0]<=t5_t0_t2*MAS[0]

	S += t5_t0_t2_in*MAS_in[1]<=t5_t0_t2*MAS[1]

	S += t5_t0_t2_in*MAS_in[2]<=t5_t0_t2*MAS[2]

	S += t5_t0_t2_in*MAS_in[3]<=t5_t0_t2*MAS[3]

	S += t5_t0_t2_in*MAS_in[4]<=t5_t0_t2*MAS[4]

	S += t5_t0_t2_in*MAS_in[5]<=t5_t0_t2*MAS[5]

	S += t5_t0_t2_in*MAS_in[6]<=t5_t0_t2*MAS[6]

	S += t5_t0_t2_in*MAS_in[7]<=t5_t0_t2*MAS[7]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	t5_t0_t2_mem0 += MAIN_MEM_r[0]
	S += t5_t0_t2_mem0 <= t5_t0_t2

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	t5_t0_t2_mem1 += MAIN_MEM_r[1]
	S += t5_t0_t2_mem1 <= t5_t0_t2

	t5_t8_t2 = S.Task('t5_t8_t2', length=2, delay_cost=1)
	t5_t8_t2 += alt(MAS)
	t5_t8_t2_in = S.Task('t5_t8_t2_in', length=1, delay_cost=1)
	t5_t8_t2_in += alt(MAS_in)
	S += t5_t8_t2_in*MAS_in[0]<=t5_t8_t2*MAS[0]

	S += t5_t8_t2_in*MAS_in[1]<=t5_t8_t2*MAS[1]

	S += t5_t8_t2_in*MAS_in[2]<=t5_t8_t2*MAS[2]

	S += t5_t8_t2_in*MAS_in[3]<=t5_t8_t2*MAS[3]

	S += t5_t8_t2_in*MAS_in[4]<=t5_t8_t2*MAS[4]

	S += t5_t8_t2_in*MAS_in[5]<=t5_t8_t2*MAS[5]

	S += t5_t8_t2_in*MAS_in[6]<=t5_t8_t2*MAS[6]

	S += t5_t8_t2_in*MAS_in[7]<=t5_t8_t2*MAS[7]

	t5_t8_t2_mem0 = S.Task('t5_t8_t2_mem0', length=1, delay_cost=1)
	t5_t8_t2_mem0 += MAIN_MEM_r[0]
	S += t5_t8_t2_mem0 <= t5_t8_t2

	t5_t8_t2_mem1 = S.Task('t5_t8_t2_mem1', length=1, delay_cost=1)
	t5_t8_t2_mem1 += MAIN_MEM_r[1]
	S += t5_t8_t2_mem1 <= t5_t8_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage2MAS8/SPARSE/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

