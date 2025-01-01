from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 194
	S = Scenario("schedule4", horizon=horizon)

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

	t4_t6_t1_in = S.Task('t4_t6_t1_in', length=1, delay_cost=1)
	S += t4_t6_t1_in >= 5
	t4_t6_t1_in += MM_in[0]

	t4_t6_t1_mem0 = S.Task('t4_t6_t1_mem0', length=1, delay_cost=1)
	S += t4_t6_t1_mem0 >= 5
	t4_t6_t1_mem0 += MAS_MEM[0]

	t4_t6_t1_mem1 = S.Task('t4_t6_t1_mem1', length=1, delay_cost=1)
	S += t4_t6_t1_mem1 >= 5
	t4_t6_t1_mem1 += MAS_MEM[1]

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

	t4_t6_t1 = S.Task('t4_t6_t1', length=11, delay_cost=1)
	S += t4_t6_t1 >= 6
	t4_t6_t1 += MM[0]

	t1_t4_in = S.Task('t1_t4_in', length=1, delay_cost=1)
	S += t1_t4_in >= 7
	t1_t4_in += MM_in[0]

	t1_t4_mem0 = S.Task('t1_t4_mem0', length=1, delay_cost=1)
	S += t1_t4_mem0 >= 7
	t1_t4_mem0 += MAS_MEM[0]

	t1_t4_mem1 = S.Task('t1_t4_mem1', length=1, delay_cost=1)
	S += t1_t4_mem1 >= 7
	t1_t4_mem1 += MAS_MEM[1]

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

	t1_t4 = S.Task('t1_t4', length=11, delay_cost=1)
	S += t1_t4 >= 8
	t1_t4 += MM[0]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 8
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 8
	t2_t4_mem0 += MAS_MEM[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 8
	t2_t4_mem1 += MAS_MEM[1]

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

	t2_t4 = S.Task('t2_t4', length=11, delay_cost=1)
	S += t2_t4 >= 9
	t2_t4 += MM[0]

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

	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	S += t4_t0_t4_in >= 12
	t4_t0_t4_in += MM_in[0]

	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	S += t4_t0_t4_mem0 >= 12
	t4_t0_t4_mem0 += MAS_MEM[2]

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	S += t4_t0_t4_mem1 >= 12
	t4_t0_t4_mem1 += MAS_MEM[1]

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

	t4_t0_t4 = S.Task('t4_t0_t4', length=11, delay_cost=1)
	S += t4_t0_t4 >= 13
	t4_t0_t4 += MM[0]

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

	t4_t2_t4_in = S.Task('t4_t2_t4_in', length=1, delay_cost=1)
	S += t4_t2_t4_in >= 16
	t4_t2_t4_in += MM_in[0]

	t4_t2_t4_mem0 = S.Task('t4_t2_t4_mem0', length=1, delay_cost=1)
	S += t4_t2_t4_mem0 >= 16
	t4_t2_t4_mem0 += MAS_MEM[0]

	t4_t2_t4_mem1 = S.Task('t4_t2_t4_mem1', length=1, delay_cost=1)
	S += t4_t2_t4_mem1 >= 16
	t4_t2_t4_mem1 += MAS_MEM[1]

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

	t4_t2_t4 = S.Task('t4_t2_t4', length=11, delay_cost=1)
	S += t4_t2_t4 >= 17
	t4_t2_t4 += MM[0]

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

	t4_t6_t2_in = S.Task('t4_t6_t2_in', length=1, delay_cost=1)
	S += t4_t6_t2_in >= 19
	t4_t6_t2_in += MAS_in[0]

	t4_t6_t2_mem0 = S.Task('t4_t6_t2_mem0', length=1, delay_cost=1)
	S += t4_t6_t2_mem0 >= 19
	t4_t6_t2_mem0 += MAS_MEM[0]

	t4_t6_t2_mem1 = S.Task('t4_t6_t2_mem1', length=1, delay_cost=1)
	S += t4_t6_t2_mem1 >= 19
	t4_t6_t2_mem1 += MAS_MEM[1]

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

	t4_t6_t2 = S.Task('t4_t6_t2', length=3, delay_cost=1)
	S += t4_t6_t2 >= 20
	t4_t6_t2 += MAS[0]

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

	t4_t1_t5_in = S.Task('t4_t1_t5_in', length=1, delay_cost=1)
	S += t4_t1_t5_in >= 24
	t4_t1_t5_in += MAS_in[0]

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	S += t4_t1_t5_mem0 >= 24
	t4_t1_t5_mem0 += MM_MEM[0]

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	S += t4_t1_t5_mem1 >= 24
	t4_t1_t5_mem1 += MM_MEM[1]

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

	t4_t10_in = S.Task('t4_t10_in', length=1, delay_cost=1)
	S += t4_t10_in >= 25
	t4_t10_in += MAS_in[0]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 25
	t4_t10_mem0 += MM_MEM[0]

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 25
	t4_t10_mem1 += MM_MEM[1]

	t4_t1_t5 = S.Task('t4_t1_t5', length=3, delay_cost=1)
	S += t4_t1_t5 >= 25
	t4_t1_t5 += MAS[0]

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

	t4_t10 = S.Task('t4_t10', length=3, delay_cost=1)
	S += t4_t10 >= 26
	t4_t10 += MAS[0]

	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	S += t4_t1_t4_in >= 26
	t4_t1_t4_in += MM_in[0]

	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	S += t4_t1_t4_mem0 >= 26
	t4_t1_t4_mem0 += MAS_MEM[0]

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	S += t4_t1_t4_mem1 >= 26
	t4_t1_t4_mem1 += MAS_MEM[3]

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

	t4_t1_t4 = S.Task('t4_t1_t4', length=11, delay_cost=1)
	S += t4_t1_t4 >= 27
	t4_t1_t4 += MM[0]

	t4_t6_t3_in = S.Task('t4_t6_t3_in', length=1, delay_cost=1)
	S += t4_t6_t3_in >= 27
	t4_t6_t3_in += MAS_in[1]

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	S += t4_t6_t3_mem0 >= 27
	t4_t6_t3_mem0 += MAS_MEM[2]

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	S += t4_t6_t3_mem1 >= 27
	t4_t6_t3_mem1 += MAS_MEM[1]

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

	t4_t6_t3 = S.Task('t4_t6_t3', length=3, delay_cost=1)
	S += t4_t6_t3 >= 28
	t4_t6_t3 += MAS[1]

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

	t4_t00_in = S.Task('t4_t00_in', length=1, delay_cost=1)
	S += t4_t00_in >= 29
	t4_t00_in += MAS_in[0]

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	S += t4_t00_mem0 >= 29
	t4_t00_mem0 += MM_MEM[0]

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	S += t4_t00_mem1 >= 29
	t4_t00_mem1 += MM_MEM[1]

	t0_t0 = S.Task('t0_t0', length=11, delay_cost=1)
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

	t4_t20_in = S.Task('t4_t20_in', length=1, delay_cost=1)
	S += t4_t20_in >= 30
	t4_t20_in += MAS_in[1]

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	S += t4_t20_mem0 >= 30
	t4_t20_mem0 += MM_MEM[0]

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	S += t4_t20_mem1 >= 30
	t4_t20_mem1 += MM_MEM[1]

	t5_t0_t2_in = S.Task('t5_t0_t2_in', length=1, delay_cost=1)
	S += t5_t0_t2_in >= 30
	t5_t0_t2_in += MAS_in[0]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 30
	t5_t0_t2_mem0 += MAIN_MEM_r[0]

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 30
	t5_t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=11, delay_cost=1)
	S += t0_t4 >= 31
	t0_t4 += MM[0]

	t4_t20 = S.Task('t4_t20', length=3, delay_cost=1)
	S += t4_t20 >= 31
	t4_t20 += MAS[1]

	t4_t2_t5_in = S.Task('t4_t2_t5_in', length=1, delay_cost=1)
	S += t4_t2_t5_in >= 31
	t4_t2_t5_in += MAS_in[1]

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	S += t4_t2_t5_mem0 >= 31
	t4_t2_t5_mem0 += MM_MEM[0]

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	S += t4_t2_t5_mem1 >= 31
	t4_t2_t5_mem1 += MM_MEM[1]

	t4_t6_t0_in = S.Task('t4_t6_t0_in', length=1, delay_cost=1)
	S += t4_t6_t0_in >= 31
	t4_t6_t0_in += MM_in[0]

	t4_t6_t0_mem0 = S.Task('t4_t6_t0_mem0', length=1, delay_cost=1)
	S += t4_t6_t0_mem0 >= 31
	t4_t6_t0_mem0 += MAS_MEM[0]

	t4_t6_t0_mem1 = S.Task('t4_t6_t0_mem1', length=1, delay_cost=1)
	S += t4_t6_t0_mem1 >= 31
	t4_t6_t0_mem1 += MAS_MEM[3]

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

	t4_t2_t5 = S.Task('t4_t2_t5', length=3, delay_cost=1)
	S += t4_t2_t5 >= 32
	t4_t2_t5 += MAS[1]

	t4_t6_t0 = S.Task('t4_t6_t0', length=11, delay_cost=1)
	S += t4_t6_t0 >= 32
	t4_t6_t0 += MM[0]

	t4_t6_t4_in = S.Task('t4_t6_t4_in', length=1, delay_cost=1)
	S += t4_t6_t4_in >= 32
	t4_t6_t4_in += MM_in[0]

	t4_t6_t4_mem0 = S.Task('t4_t6_t4_mem0', length=1, delay_cost=1)
	S += t4_t6_t4_mem0 >= 32
	t4_t6_t4_mem0 += MAS_MEM[0]

	t4_t6_t4_mem1 = S.Task('t4_t6_t4_mem1', length=1, delay_cost=1)
	S += t4_t6_t4_mem1 >= 32
	t4_t6_t4_mem1 += MAS_MEM[3]

	t4_t8_t5_in = S.Task('t4_t8_t5_in', length=1, delay_cost=1)
	S += t4_t8_t5_in >= 32
	t4_t8_t5_in += MAS_in[0]

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	S += t4_t8_t5_mem0 >= 32
	t4_t8_t5_mem0 += MM_MEM[0]

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	S += t4_t8_t5_mem1 >= 32
	t4_t8_t5_mem1 += MM_MEM[1]

	t5_t8_t2 = S.Task('t5_t8_t2', length=3, delay_cost=1)
	S += t5_t8_t2 >= 32
	t5_t8_t2 += MAS[0]

	t101 = S.Task('t101', length=3, delay_cost=1)
	S += t101 >= 33
	t101 += MAS[1]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 33
	t20_in += MAS_in[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 33
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 33
	t20_mem1 += MM_MEM[1]

	t4_t6_t4 = S.Task('t4_t6_t4', length=11, delay_cost=1)
	S += t4_t6_t4 >= 33
	t4_t6_t4 += MM[0]

	t4_t8_t5 = S.Task('t4_t8_t5', length=3, delay_cost=1)
	S += t4_t8_t5 >= 33
	t4_t8_t5 += MAS[0]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 33
	t71_in += MAS_in[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 33
	t71_mem0 += MAIN_MEM_r[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 33
	t71_mem1 += MAIN_MEM_r[1]

	t20 = S.Task('t20', length=3, delay_cost=1)
	S += t20 >= 34
	t20 += MAS[1]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 34
	t2_t5_in += MAS_in[1]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 34
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 34
	t2_t5_mem1 += MM_MEM[1]

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

	t2_t5 = S.Task('t2_t5', length=3, delay_cost=1)
	S += t2_t5 >= 35
	t2_t5 += MAS[1]

	t4_t0_t5_in = S.Task('t4_t0_t5_in', length=1, delay_cost=1)
	S += t4_t0_t5_in >= 35
	t4_t0_t5_in += MAS_in[0]

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	S += t4_t0_t5_mem0 >= 35
	t4_t0_t5_mem0 += MM_MEM[0]

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	S += t4_t0_t5_mem1 >= 35
	t4_t0_t5_mem1 += MM_MEM[1]

	t80 = S.Task('t80', length=3, delay_cost=1)
	S += t80 >= 35
	t80 += MAS[0]

	t100 = S.Task('t100', length=3, delay_cost=1)
	S += t100 >= 36
	t100 += MAS[1]

	t4_t0_t5 = S.Task('t4_t0_t5', length=3, delay_cost=1)
	S += t4_t0_t5 >= 36
	t4_t0_t5 += MAS[0]

	t4_t80_in = S.Task('t4_t80_in', length=1, delay_cost=1)
	S += t4_t80_in >= 36
	t4_t80_in += MAS_in[1]

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	S += t4_t80_mem0 >= 36
	t4_t80_mem0 += MM_MEM[0]

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	S += t4_t80_mem1 >= 36
	t4_t80_mem1 += MM_MEM[1]

	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	S += t5_t2_t1_in >= 36
	t5_t2_t1_in += MM_in[0]

	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	S += t5_t2_t1_mem0 >= 36
	t5_t2_t1_mem0 += MAS_MEM[0]

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	S += t5_t2_t1_mem1 >= 36
	t5_t2_t1_mem1 += MAS_MEM[3]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 36
	t90_in += MAS_in[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 36
	t90_mem0 += MAIN_MEM_r[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 36
	t90_mem1 += MAIN_MEM_r[1]

	t4_t11_in = S.Task('t4_t11_in', length=1, delay_cost=1)
	S += t4_t11_in >= 37
	t4_t11_in += MAS_in[0]

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	S += t4_t11_mem0 >= 37
	t4_t11_mem0 += MM_MEM[0]

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	S += t4_t11_mem1 >= 37
	t4_t11_mem1 += MAS_MEM[1]

	t4_t80 = S.Task('t4_t80', length=3, delay_cost=1)
	S += t4_t80 >= 37
	t4_t80 += MAS[1]

	t5_t2_t1 = S.Task('t5_t2_t1', length=11, delay_cost=1)
	S += t5_t2_t1 >= 37
	t5_t2_t1 += MM[0]

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

	t4_t11 = S.Task('t4_t11', length=3, delay_cost=1)
	S += t4_t11 >= 38
	t4_t11 += MAS[0]

	t4_t8_t3_in = S.Task('t4_t8_t3_in', length=1, delay_cost=1)
	S += t4_t8_t3_in >= 38
	t4_t8_t3_in += MAS_in[0]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 38
	t4_t8_t3_mem0 += MAIN_MEM_r[0]

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 38
	t4_t8_t3_mem1 += MAIN_MEM_r[1]

	t5_t2_t3_in = S.Task('t5_t2_t3_in', length=1, delay_cost=1)
	S += t5_t2_t3_in >= 38
	t5_t2_t3_in += MAS_in[1]

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	S += t5_t2_t3_mem0 >= 38
	t5_t2_t3_mem0 += MAS_MEM[2]

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	S += t5_t2_t3_mem1 >= 38
	t5_t2_t3_mem1 += MAS_MEM[3]

	t91 = S.Task('t91', length=3, delay_cost=1)
	S += t91 >= 38
	t91 += MAS[1]

	t4_t8_t3 = S.Task('t4_t8_t3', length=3, delay_cost=1)
	S += t4_t8_t3 >= 39
	t4_t8_t3 += MAS[0]

	t5_t2_t3 = S.Task('t5_t2_t3', length=3, delay_cost=1)
	S += t5_t2_t3 >= 39
	t5_t2_t3 += MAS[1]

	t5_t50_in = S.Task('t5_t50_in', length=1, delay_cost=1)
	S += t5_t50_in >= 39
	t5_t50_in += MAS_in[1]

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	S += t5_t50_mem0 >= 39
	t5_t50_mem0 += MAS_MEM[0]

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	S += t5_t50_mem1 >= 39
	t5_t50_mem1 += MAS_MEM[1]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 39
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 39
	t70_mem0 += MAIN_MEM_r[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 39
	t70_mem1 += MAIN_MEM_r[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 40
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 40
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 40
	t10_mem1 += MM_MEM[1]

	t4_t8_t2_in = S.Task('t4_t8_t2_in', length=1, delay_cost=1)
	S += t4_t8_t2_in >= 40
	t4_t8_t2_in += MAS_in[1]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 40
	t4_t8_t2_mem0 += MAIN_MEM_r[0]

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 40
	t4_t8_t2_mem1 += MAIN_MEM_r[1]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 40
	t5_t1_t1_in += MM_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 40
	t5_t1_t1_mem0 += MAS_MEM[0]

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 40
	t5_t1_t1_mem1 += MAS_MEM[3]

	t5_t50 = S.Task('t5_t50', length=3, delay_cost=1)
	S += t5_t50 >= 40
	t5_t50 += MAS[1]

	t70 = S.Task('t70', length=3, delay_cost=1)
	S += t70 >= 40
	t70 += MAS[0]

	t10 = S.Task('t10', length=3, delay_cost=1)
	S += t10 >= 41
	t10 += MAS[0]

	t4_t8_t2 = S.Task('t4_t8_t2', length=3, delay_cost=1)
	S += t4_t8_t2 >= 41
	t4_t8_t2 += MAS[1]

	t5_t1_t1 = S.Task('t5_t1_t1', length=11, delay_cost=1)
	S += t5_t1_t1 >= 41
	t5_t1_t1 += MM[0]

	t5_t1_t3_in = S.Task('t5_t1_t3_in', length=1, delay_cost=1)
	S += t5_t1_t3_in >= 41
	t5_t1_t3_in += MAS_in[1]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 41
	t5_t1_t3_mem0 += MAS_MEM[0]

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 41
	t5_t1_t3_mem1 += MAS_MEM[3]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 41
	t81_in += MAS_in[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 41
	t81_mem0 += MAIN_MEM_r[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 41
	t81_mem1 += MAIN_MEM_r[1]

	t1_t5_in = S.Task('t1_t5_in', length=1, delay_cost=1)
	S += t1_t5_in >= 42
	t1_t5_in += MAS_in[1]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 42
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 42
	t1_t5_mem1 += MM_MEM[1]

	t5_t1_t3 = S.Task('t5_t1_t3', length=3, delay_cost=1)
	S += t5_t1_t3 >= 42
	t5_t1_t3 += MAS[1]

	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	S += t5_t2_t0_in >= 42
	t5_t2_t0_in += MM_in[0]

	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	S += t5_t2_t0_mem0 >= 42
	t5_t2_t0_mem0 += MAS_MEM[0]

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	S += t5_t2_t0_mem1 >= 42
	t5_t2_t0_mem1 += MAS_MEM[3]

	t5_t41_in = S.Task('t5_t41_in', length=1, delay_cost=1)
	S += t5_t41_in >= 42
	t5_t41_in += MAS_in[0]

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	S += t5_t41_mem0 >= 42
	t5_t41_mem0 += MAIN_MEM_r[0]

	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	S += t5_t41_mem1 >= 42
	t5_t41_mem1 += MAS_MEM[1]

	t81 = S.Task('t81', length=3, delay_cost=1)
	S += t81 >= 42
	t81 += MAS[0]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 43
	t00_in += MAS_in[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 43
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 43
	t00_mem1 += MM_MEM[1]

	t1_t5 = S.Task('t1_t5', length=3, delay_cost=1)
	S += t1_t5 >= 43
	t1_t5 += MAS[1]

	t5_t1_t2_in = S.Task('t5_t1_t2_in', length=1, delay_cost=1)
	S += t5_t1_t2_in >= 43
	t5_t1_t2_in += MAS_in[1]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 43
	t5_t1_t2_mem0 += MAS_MEM[0]

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 43
	t5_t1_t2_mem1 += MAS_MEM[1]

	t5_t2_t0 = S.Task('t5_t2_t0', length=11, delay_cost=1)
	S += t5_t2_t0 >= 43
	t5_t2_t0 += MM[0]

	t5_t41 = S.Task('t5_t41', length=3, delay_cost=1)
	S += t5_t41 >= 43
	t5_t41 += MAS[0]

	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	S += t5_t8_t0_in >= 43
	t5_t8_t0_in += MM_in[0]

	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	S += t5_t8_t0_mem0 >= 43
	t5_t8_t0_mem0 += MAIN_MEM_r[0]

	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	S += t5_t8_t0_mem1 >= 43
	t5_t8_t0_mem1 += MAS_MEM[3]

	t00 = S.Task('t00', length=3, delay_cost=1)
	S += t00 >= 44
	t00 += MAS[0]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 44
	t0_t5_in += MAS_in[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 44
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 44
	t0_t5_mem1 += MM_MEM[1]

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 44
	t5_t0_t0_in += MM_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 44
	t5_t0_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 44
	t5_t0_t0_mem1 += MAS_MEM[1]

	t5_t1_t2 = S.Task('t5_t1_t2', length=3, delay_cost=1)
	S += t5_t1_t2 >= 44
	t5_t1_t2 += MAS[1]

	t5_t8_t0 = S.Task('t5_t8_t0', length=11, delay_cost=1)
	S += t5_t8_t0 >= 44
	t5_t8_t0 += MM[0]

	t5_t8_t3_in = S.Task('t5_t8_t3_in', length=1, delay_cost=1)
	S += t5_t8_t3_in >= 44
	t5_t8_t3_in += MAS_in[1]

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	S += t5_t8_t3_mem0 >= 44
	t5_t8_t3_mem0 += MAS_MEM[2]

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	S += t5_t8_t3_mem1 >= 44
	t5_t8_t3_mem1 += MAS_MEM[3]

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	S += t0_t5 >= 45
	t0_t5 += MAS[0]

	t4_t60_in = S.Task('t4_t60_in', length=1, delay_cost=1)
	S += t4_t60_in >= 45
	t4_t60_in += MAS_in[0]

	t4_t60_mem0 = S.Task('t4_t60_mem0', length=1, delay_cost=1)
	S += t4_t60_mem0 >= 45
	t4_t60_mem0 += MM_MEM[0]

	t4_t60_mem1 = S.Task('t4_t60_mem1', length=1, delay_cost=1)
	S += t4_t60_mem1 >= 45
	t4_t60_mem1 += MM_MEM[1]

	t5_t0_t0 = S.Task('t5_t0_t0', length=11, delay_cost=1)
	S += t5_t0_t0 >= 45
	t5_t0_t0 += MM[0]

	t5_t2_t2_in = S.Task('t5_t2_t2_in', length=1, delay_cost=1)
	S += t5_t2_t2_in >= 45
	t5_t2_t2_in += MAS_in[1]

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_t2_mem0 >= 45
	t5_t2_t2_mem0 += MAS_MEM[0]

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_t2_mem1 >= 45
	t5_t2_t2_mem1 += MAS_MEM[1]

	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	S += t5_t8_t1_in >= 45
	t5_t8_t1_in += MM_in[0]

	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	S += t5_t8_t1_mem0 >= 45
	t5_t8_t1_mem0 += MAIN_MEM_r[0]

	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	S += t5_t8_t1_mem1 >= 45
	t5_t8_t1_mem1 += MAS_MEM[3]

	t5_t8_t3 = S.Task('t5_t8_t3', length=3, delay_cost=1)
	S += t5_t8_t3 >= 45
	t5_t8_t3 += MAS[1]

	t4_t60 = S.Task('t4_t60', length=3, delay_cost=1)
	S += t4_t60 >= 46
	t4_t60 += MAS[0]

	t4_t6_t5_in = S.Task('t4_t6_t5_in', length=1, delay_cost=1)
	S += t4_t6_t5_in >= 46
	t4_t6_t5_in += MAS_in[1]

	t4_t6_t5_mem0 = S.Task('t4_t6_t5_mem0', length=1, delay_cost=1)
	S += t4_t6_t5_mem0 >= 46
	t4_t6_t5_mem0 += MM_MEM[0]

	t4_t6_t5_mem1 = S.Task('t4_t6_t5_mem1', length=1, delay_cost=1)
	S += t4_t6_t5_mem1 >= 46
	t4_t6_t5_mem1 += MM_MEM[1]

	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	S += t4_t8_t4_in >= 46
	t4_t8_t4_in += MM_in[0]

	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	S += t4_t8_t4_mem0 >= 46
	t4_t8_t4_mem0 += MAS_MEM[2]

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	S += t4_t8_t4_mem1 >= 46
	t4_t8_t4_mem1 += MAS_MEM[1]

	t5_t2_t2 = S.Task('t5_t2_t2', length=3, delay_cost=1)
	S += t5_t2_t2 >= 46
	t5_t2_t2 += MAS[1]

	t5_t51_in = S.Task('t5_t51_in', length=1, delay_cost=1)
	S += t5_t51_in >= 46
	t5_t51_in += MAS_in[0]

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	S += t5_t51_mem0 >= 46
	t5_t51_mem0 += MAS_MEM[0]

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	S += t5_t51_mem1 >= 46
	t5_t51_mem1 += MAS_MEM[3]

	t5_t8_t1 = S.Task('t5_t8_t1', length=11, delay_cost=1)
	S += t5_t8_t1 >= 46
	t5_t8_t1 += MM[0]

	t4_t21_in = S.Task('t4_t21_in', length=1, delay_cost=1)
	S += t4_t21_in >= 47
	t4_t21_in += MAS_in[0]

	t4_t21_mem0 = S.Task('t4_t21_mem0', length=1, delay_cost=1)
	S += t4_t21_mem0 >= 47
	t4_t21_mem0 += MM_MEM[0]

	t4_t21_mem1 = S.Task('t4_t21_mem1', length=1, delay_cost=1)
	S += t4_t21_mem1 >= 47
	t4_t21_mem1 += MAS_MEM[3]

	t4_t6_t5 = S.Task('t4_t6_t5', length=3, delay_cost=1)
	S += t4_t6_t5 >= 47
	t4_t6_t5 += MAS[1]

	t4_t8_t4 = S.Task('t4_t8_t4', length=11, delay_cost=1)
	S += t4_t8_t4 >= 47
	t4_t8_t4 += MM[0]

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 47
	t5_t0_t1_in += MM_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 47
	t5_t0_t1_mem0 += MAIN_MEM_r[0]

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 47
	t5_t0_t1_mem1 += MAS_MEM[1]

	t5_t51 = S.Task('t5_t51', length=3, delay_cost=1)
	S += t5_t51 >= 47
	t5_t51 += MAS[0]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 48
	t21_in += MAS_in[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 48
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 48
	t21_mem1 += MAS_MEM[3]

	t4_t21 = S.Task('t4_t21', length=3, delay_cost=1)
	S += t4_t21 >= 48
	t4_t21 += MAS[0]

	t5_t0_t1 = S.Task('t5_t0_t1', length=11, delay_cost=1)
	S += t5_t0_t1 >= 48
	t5_t0_t1 += MM[0]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 48
	t5_t1_t0_in += MM_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 48
	t5_t1_t0_mem0 += MAS_MEM[0]

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 48
	t5_t1_t0_mem1 += MAS_MEM[1]

	t21 = S.Task('t21', length=3, delay_cost=1)
	S += t21 >= 49
	t21 += MAS[1]

	t4_t61_in = S.Task('t4_t61_in', length=1, delay_cost=1)
	S += t4_t61_in >= 49
	t4_t61_in += MAS_in[1]

	t4_t61_mem0 = S.Task('t4_t61_mem0', length=1, delay_cost=1)
	S += t4_t61_mem0 >= 49
	t4_t61_mem0 += MM_MEM[0]

	t4_t61_mem1 = S.Task('t4_t61_mem1', length=1, delay_cost=1)
	S += t4_t61_mem1 >= 49
	t4_t61_mem1 += MAS_MEM[3]

	t5_t1_t0 = S.Task('t5_t1_t0', length=11, delay_cost=1)
	S += t5_t1_t0 >= 49
	t5_t1_t0 += MM[0]

	t5_t40_in = S.Task('t5_t40_in', length=1, delay_cost=1)
	S += t5_t40_in >= 49
	t5_t40_in += MAS_in[0]

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	S += t5_t40_mem0 >= 49
	t5_t40_mem0 += MAIN_MEM_r[0]

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	S += t5_t40_mem1 >= 49
	t5_t40_mem1 += MAS_MEM[1]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 50
	t11_in += MAS_in[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 50
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 50
	t11_mem1 += MAS_MEM[3]

	t4_t61 = S.Task('t4_t61', length=3, delay_cost=1)
	S += t4_t61 >= 50
	t4_t61 += MAS[1]

	t5_t0_t3_in = S.Task('t5_t0_t3_in', length=1, delay_cost=1)
	S += t5_t0_t3_in >= 50
	t5_t0_t3_in += MAS_in[1]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 50
	t5_t0_t3_mem0 += MAS_MEM[0]

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 50
	t5_t0_t3_mem1 += MAS_MEM[1]

	t5_t40 = S.Task('t5_t40', length=3, delay_cost=1)
	S += t5_t40 >= 50
	t5_t40 += MAS[0]

	t11 = S.Task('t11', length=3, delay_cost=1)
	S += t11 >= 51
	t11 += MAS[0]

	t420_in = S.Task('t420_in', length=1, delay_cost=1)
	S += t420_in >= 51
	t420_in += MAS_in[1]

	t420_mem0 = S.Task('t420_mem0', length=1, delay_cost=1)
	S += t420_mem0 >= 51
	t420_mem0 += MAS_MEM[2]

	t420_mem1 = S.Task('t420_mem1', length=1, delay_cost=1)
	S += t420_mem1 >= 51
	t420_mem1 += MAS_MEM[1]

	t4_t101_in = S.Task('t4_t101_in', length=1, delay_cost=1)
	S += t4_t101_in >= 51
	t4_t101_in += MAS_in[0]

	t4_t101_mem0 = S.Task('t4_t101_mem0', length=1, delay_cost=1)
	S += t4_t101_mem0 >= 51
	t4_t101_mem0 += MAS_MEM[0]

	t4_t101_mem1 = S.Task('t4_t101_mem1', length=1, delay_cost=1)
	S += t4_t101_mem1 >= 51
	t4_t101_mem1 += MAS_MEM[3]

	t5_t0_t3 = S.Task('t5_t0_t3', length=3, delay_cost=1)
	S += t5_t0_t3 >= 51
	t5_t0_t3 += MAS[1]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 52
	t01_in += MAS_in[1]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 52
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 52
	t01_mem1 += MAS_MEM[1]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 52
	t171_in += MAS_in[0]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 52
	t171_mem0 += MAS_MEM[2]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 52
	t171_mem1 += MAS_MEM[3]

	t420 = S.Task('t420', length=3, delay_cost=1)
	S += t420 >= 52
	t420 += MAS[1]

	t4_t101 = S.Task('t4_t101', length=3, delay_cost=1)
	S += t4_t101 >= 52
	t4_t101 += MAS[0]

	t01 = S.Task('t01', length=3, delay_cost=1)
	S += t01 >= 53
	t01 += MAS[1]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 53
	t170_in += MAS_in[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 53
	t170_mem0 += MAS_MEM[2]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 53
	t170_mem1 += MAS_MEM[3]

	t171 = S.Task('t171', length=3, delay_cost=1)
	S += t171 >= 53
	t171 += MAS[0]

	t5_t2_t5_in = S.Task('t5_t2_t5_in', length=1, delay_cost=1)
	S += t5_t2_t5_in >= 53
	t5_t2_t5_in += MAS_in[1]

	t5_t2_t5_mem0 = S.Task('t5_t2_t5_mem0', length=1, delay_cost=1)
	S += t5_t2_t5_mem0 >= 53
	t5_t2_t5_mem0 += MM_MEM[0]

	t5_t2_t5_mem1 = S.Task('t5_t2_t5_mem1', length=1, delay_cost=1)
	S += t5_t2_t5_mem1 >= 53
	t5_t2_t5_mem1 += MM_MEM[1]

	t5_t6_t1_in = S.Task('t5_t6_t1_in', length=1, delay_cost=1)
	S += t5_t6_t1_in >= 53
	t5_t6_t1_in += MM_in[0]

	t5_t6_t1_mem0 = S.Task('t5_t6_t1_mem0', length=1, delay_cost=1)
	S += t5_t6_t1_mem0 >= 53
	t5_t6_t1_mem0 += MAS_MEM[0]

	t5_t6_t1_mem1 = S.Task('t5_t6_t1_mem1', length=1, delay_cost=1)
	S += t5_t6_t1_mem1 >= 53
	t5_t6_t1_mem1 += MAS_MEM[1]

	t170 = S.Task('t170', length=3, delay_cost=1)
	S += t170 >= 54
	t170 += MAS[0]

	t5_t20_in = S.Task('t5_t20_in', length=1, delay_cost=1)
	S += t5_t20_in >= 54
	t5_t20_in += MAS_in[1]

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	S += t5_t20_mem0 >= 54
	t5_t20_mem0 += MM_MEM[0]

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	S += t5_t20_mem1 >= 54
	t5_t20_mem1 += MM_MEM[1]

	t5_t2_t5 = S.Task('t5_t2_t5', length=3, delay_cost=1)
	S += t5_t2_t5 >= 54
	t5_t2_t5 += MAS[1]

	t5_t6_t0_in = S.Task('t5_t6_t0_in', length=1, delay_cost=1)
	S += t5_t6_t0_in >= 54
	t5_t6_t0_in += MM_in[0]

	t5_t6_t0_mem0 = S.Task('t5_t6_t0_mem0', length=1, delay_cost=1)
	S += t5_t6_t0_mem0 >= 54
	t5_t6_t0_mem0 += MAS_MEM[0]

	t5_t6_t0_mem1 = S.Task('t5_t6_t0_mem1', length=1, delay_cost=1)
	S += t5_t6_t0_mem1 >= 54
	t5_t6_t0_mem1 += MAS_MEM[3]

	t5_t6_t1 = S.Task('t5_t6_t1', length=11, delay_cost=1)
	S += t5_t6_t1 >= 54
	t5_t6_t1 += MM[0]

	t5_t6_t3_in = S.Task('t5_t6_t3_in', length=1, delay_cost=1)
	S += t5_t6_t3_in >= 54
	t5_t6_t3_in += MAS_in[0]

	t5_t6_t3_mem0 = S.Task('t5_t6_t3_mem0', length=1, delay_cost=1)
	S += t5_t6_t3_mem0 >= 54
	t5_t6_t3_mem0 += MAS_MEM[2]

	t5_t6_t3_mem1 = S.Task('t5_t6_t3_mem1', length=1, delay_cost=1)
	S += t5_t6_t3_mem1 >= 54
	t5_t6_t3_mem1 += MAS_MEM[1]

	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	S += c110_in >= 55
	c110_in += MAS_in[0]

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	S += c110_mem0 >= 55
	c110_mem0 += MAS_MEM[0]

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	S += c110_mem1 >= 55
	c110_mem1 += MAS_MEM[3]

	t4_t01_in = S.Task('t4_t01_in', length=1, delay_cost=1)
	S += t4_t01_in >= 55
	t4_t01_in += MAS_in[1]

	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	S += t4_t01_mem0 >= 55
	t4_t01_mem0 += MM_MEM[0]

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	S += t4_t01_mem1 >= 55
	t4_t01_mem1 += MAS_MEM[1]

	t5_t20 = S.Task('t5_t20', length=3, delay_cost=1)
	S += t5_t20 >= 55
	t5_t20 += MAS[1]

	t5_t6_t0 = S.Task('t5_t6_t0', length=11, delay_cost=1)
	S += t5_t6_t0 >= 55
	t5_t6_t0 += MM[0]

	t5_t6_t3 = S.Task('t5_t6_t3', length=3, delay_cost=1)
	S += t5_t6_t3 >= 55
	t5_t6_t3 += MAS[0]

	c110 = S.Task('c110', length=3, delay_cost=1)
	S += c110 >= 56
	c110 += MAS[0]

	t4_t01 = S.Task('t4_t01', length=3, delay_cost=1)
	S += t4_t01 >= 56
	t4_t01 += MAS[1]

	t5_t2_t4_in = S.Task('t5_t2_t4_in', length=1, delay_cost=1)
	S += t5_t2_t4_in >= 56
	t5_t2_t4_in += MM_in[0]

	t5_t2_t4_mem0 = S.Task('t5_t2_t4_mem0', length=1, delay_cost=1)
	S += t5_t2_t4_mem0 >= 56
	t5_t2_t4_mem0 += MAS_MEM[2]

	t5_t2_t4_mem1 = S.Task('t5_t2_t4_mem1', length=1, delay_cost=1)
	S += t5_t2_t4_mem1 >= 56
	t5_t2_t4_mem1 += MAS_MEM[3]

	t5_t6_t2_in = S.Task('t5_t6_t2_in', length=1, delay_cost=1)
	S += t5_t6_t2_in >= 56
	t5_t6_t2_in += MAS_in[0]

	t5_t6_t2_mem0 = S.Task('t5_t6_t2_mem0', length=1, delay_cost=1)
	S += t5_t6_t2_mem0 >= 56
	t5_t6_t2_mem0 += MAS_MEM[0]

	t5_t6_t2_mem1 = S.Task('t5_t6_t2_mem1', length=1, delay_cost=1)
	S += t5_t6_t2_mem1 >= 56
	t5_t6_t2_mem1 += MAS_MEM[1]

	t5_t80_in = S.Task('t5_t80_in', length=1, delay_cost=1)
	S += t5_t80_in >= 56
	t5_t80_in += MAS_in[1]

	t5_t80_mem0 = S.Task('t5_t80_mem0', length=1, delay_cost=1)
	S += t5_t80_mem0 >= 56
	t5_t80_mem0 += MM_MEM[0]

	t5_t80_mem1 = S.Task('t5_t80_mem1', length=1, delay_cost=1)
	S += t5_t80_mem1 >= 56
	t5_t80_mem1 += MM_MEM[1]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 57
	t31_in += MAS_in[1]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 57
	t31_mem0 += MAS_MEM[2]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 57
	t31_mem1 += MAS_MEM[1]

	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	S += t5_t0_t4_in >= 57
	t5_t0_t4_in += MM_in[0]

	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	S += t5_t0_t4_mem0 >= 57
	t5_t0_t4_mem0 += MAS_MEM[0]

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	S += t5_t0_t4_mem1 >= 57
	t5_t0_t4_mem1 += MAS_MEM[3]

	t5_t2_t4 = S.Task('t5_t2_t4', length=11, delay_cost=1)
	S += t5_t2_t4 >= 57
	t5_t2_t4 += MM[0]

	t5_t6_t2 = S.Task('t5_t6_t2', length=3, delay_cost=1)
	S += t5_t6_t2 >= 57
	t5_t6_t2 += MAS[0]

	t5_t80 = S.Task('t5_t80', length=3, delay_cost=1)
	S += t5_t80 >= 57
	t5_t80 += MAS[1]

	t5_t8_t5_in = S.Task('t5_t8_t5_in', length=1, delay_cost=1)
	S += t5_t8_t5_in >= 57
	t5_t8_t5_in += MAS_in[0]

	t5_t8_t5_mem0 = S.Task('t5_t8_t5_mem0', length=1, delay_cost=1)
	S += t5_t8_t5_mem0 >= 57
	t5_t8_t5_mem0 += MM_MEM[0]

	t5_t8_t5_mem1 = S.Task('t5_t8_t5_mem1', length=1, delay_cost=1)
	S += t5_t8_t5_mem1 >= 57
	t5_t8_t5_mem1 += MM_MEM[1]

	t31 = S.Task('t31', length=3, delay_cost=1)
	S += t31 >= 58
	t31 += MAS[1]

	t4_t70_in = S.Task('t4_t70_in', length=1, delay_cost=1)
	S += t4_t70_in >= 58
	t4_t70_in += MAS_in[0]

	t4_t70_mem0 = S.Task('t4_t70_mem0', length=1, delay_cost=1)
	S += t4_t70_mem0 >= 58
	t4_t70_mem0 += MAS_MEM[0]

	t4_t70_mem1 = S.Task('t4_t70_mem1', length=1, delay_cost=1)
	S += t4_t70_mem1 >= 58
	t4_t70_mem1 += MAS_MEM[1]

	t5_t00_in = S.Task('t5_t00_in', length=1, delay_cost=1)
	S += t5_t00_in >= 58
	t5_t00_in += MAS_in[1]

	t5_t00_mem0 = S.Task('t5_t00_mem0', length=1, delay_cost=1)
	S += t5_t00_mem0 >= 58
	t5_t00_mem0 += MM_MEM[0]

	t5_t00_mem1 = S.Task('t5_t00_mem1', length=1, delay_cost=1)
	S += t5_t00_mem1 >= 58
	t5_t00_mem1 += MM_MEM[1]

	t5_t0_t4 = S.Task('t5_t0_t4', length=11, delay_cost=1)
	S += t5_t0_t4 >= 58
	t5_t0_t4 += MM[0]

	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	S += t5_t1_t4_in >= 58
	t5_t1_t4_in += MM_in[0]

	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	S += t5_t1_t4_mem0 >= 58
	t5_t1_t4_mem0 += MAS_MEM[2]

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	S += t5_t1_t4_mem1 >= 58
	t5_t1_t4_mem1 += MAS_MEM[3]

	t5_t8_t5 = S.Task('t5_t8_t5', length=3, delay_cost=1)
	S += t5_t8_t5 >= 58
	t5_t8_t5 += MAS[0]

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	S += c110_w >= 59
	c110_w += MAIN_MEM_w

	t4_t70 = S.Task('t4_t70', length=3, delay_cost=1)
	S += t4_t70 >= 59
	t4_t70 += MAS[0]

	t4_t71_in = S.Task('t4_t71_in', length=1, delay_cost=1)
	S += t4_t71_in >= 59
	t4_t71_in += MAS_in[1]

	t4_t71_mem0 = S.Task('t4_t71_mem0', length=1, delay_cost=1)
	S += t4_t71_mem0 >= 59
	t4_t71_mem0 += MAS_MEM[2]

	t4_t71_mem1 = S.Task('t4_t71_mem1', length=1, delay_cost=1)
	S += t4_t71_mem1 >= 59
	t4_t71_mem1 += MAS_MEM[1]

	t5_t00 = S.Task('t5_t00', length=3, delay_cost=1)
	S += t5_t00 >= 59
	t5_t00 += MAS[1]

	t5_t0_t5_in = S.Task('t5_t0_t5_in', length=1, delay_cost=1)
	S += t5_t0_t5_in >= 59
	t5_t0_t5_in += MAS_in[0]

	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	S += t5_t0_t5_mem0 >= 59
	t5_t0_t5_mem0 += MM_MEM[0]

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	S += t5_t0_t5_mem1 >= 59
	t5_t0_t5_mem1 += MM_MEM[1]

	t5_t1_t4 = S.Task('t5_t1_t4', length=11, delay_cost=1)
	S += t5_t1_t4 >= 59
	t5_t1_t4 += MM[0]

	t5_t8_t4_in = S.Task('t5_t8_t4_in', length=1, delay_cost=1)
	S += t5_t8_t4_in >= 59
	t5_t8_t4_in += MM_in[0]

	t5_t8_t4_mem0 = S.Task('t5_t8_t4_mem0', length=1, delay_cost=1)
	S += t5_t8_t4_mem0 >= 59
	t5_t8_t4_mem0 += MAS_MEM[0]

	t5_t8_t4_mem1 = S.Task('t5_t8_t4_mem1', length=1, delay_cost=1)
	S += t5_t8_t4_mem1 >= 59
	t5_t8_t4_mem1 += MAS_MEM[3]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 60
	t160_in += MAS_in[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 60
	t160_mem0 += MAS_MEM[2]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 60
	t160_mem1 += MAS_MEM[3]

	t4_t71 = S.Task('t4_t71', length=3, delay_cost=1)
	S += t4_t71 >= 60
	t4_t71 += MAS[1]

	t5_t0_t5 = S.Task('t5_t0_t5', length=3, delay_cost=1)
	S += t5_t0_t5 >= 60
	t5_t0_t5 += MAS[0]

	t5_t10_in = S.Task('t5_t10_in', length=1, delay_cost=1)
	S += t5_t10_in >= 60
	t5_t10_in += MAS_in[1]

	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	S += t5_t10_mem0 >= 60
	t5_t10_mem0 += MM_MEM[0]

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	S += t5_t10_mem1 >= 60
	t5_t10_mem1 += MM_MEM[1]

	t5_t6_t4_in = S.Task('t5_t6_t4_in', length=1, delay_cost=1)
	S += t5_t6_t4_in >= 60
	t5_t6_t4_in += MM_in[0]

	t5_t6_t4_mem0 = S.Task('t5_t6_t4_mem0', length=1, delay_cost=1)
	S += t5_t6_t4_mem0 >= 60
	t5_t6_t4_mem0 += MAS_MEM[0]

	t5_t6_t4_mem1 = S.Task('t5_t6_t4_mem1', length=1, delay_cost=1)
	S += t5_t6_t4_mem1 >= 60
	t5_t6_t4_mem1 += MAS_MEM[1]

	t5_t8_t4 = S.Task('t5_t8_t4', length=11, delay_cost=1)
	S += t5_t8_t4 >= 60
	t5_t8_t4 += MM[0]

	t160 = S.Task('t160', length=3, delay_cost=1)
	S += t160 >= 61
	t160 += MAS[0]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 61
	t30_in += MAS_in[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 61
	t30_mem0 += MAS_MEM[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 61
	t30_mem1 += MAS_MEM[3]

	t4_t81_in = S.Task('t4_t81_in', length=1, delay_cost=1)
	S += t4_t81_in >= 61
	t4_t81_in += MAS_in[0]

	t4_t81_mem0 = S.Task('t4_t81_mem0', length=1, delay_cost=1)
	S += t4_t81_mem0 >= 61
	t4_t81_mem0 += MM_MEM[0]

	t4_t81_mem1 = S.Task('t4_t81_mem1', length=1, delay_cost=1)
	S += t4_t81_mem1 >= 61
	t4_t81_mem1 += MAS_MEM[1]

	t5_t10 = S.Task('t5_t10', length=3, delay_cost=1)
	S += t5_t10 >= 61
	t5_t10 += MAS[1]

	t5_t6_t4 = S.Task('t5_t6_t4', length=11, delay_cost=1)
	S += t5_t6_t4 >= 61
	t5_t6_t4 += MM[0]

	t30 = S.Task('t30', length=3, delay_cost=1)
	S += t30 >= 62
	t30 += MAS[1]

	t4_t100_in = S.Task('t4_t100_in', length=1, delay_cost=1)
	S += t4_t100_in >= 62
	t4_t100_in += MAS_in[0]

	t4_t100_mem0 = S.Task('t4_t100_mem0', length=1, delay_cost=1)
	S += t4_t100_mem0 >= 62
	t4_t100_mem0 += MAS_MEM[2]

	t4_t100_mem1 = S.Task('t4_t100_mem1', length=1, delay_cost=1)
	S += t4_t100_mem1 >= 62
	t4_t100_mem1 += MAS_MEM[1]

	t4_t81 = S.Task('t4_t81', length=3, delay_cost=1)
	S += t4_t81 >= 62
	t4_t81 += MAS[0]

	t5_t1_t5_in = S.Task('t5_t1_t5_in', length=1, delay_cost=1)
	S += t5_t1_t5_in >= 62
	t5_t1_t5_in += MAS_in[1]

	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	S += t5_t1_t5_mem0 >= 62
	t5_t1_t5_mem0 += MM_MEM[0]

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	S += t5_t1_t5_mem1 >= 62
	t5_t1_t5_mem1 += MM_MEM[1]

	t410_in = S.Task('t410_in', length=1, delay_cost=1)
	S += t410_in >= 63
	t410_in += MAS_in[1]

	t410_mem0 = S.Task('t410_mem0', length=1, delay_cost=1)
	S += t410_mem0 >= 63
	t410_mem0 += MAS_MEM[0]

	t410_mem1 = S.Task('t410_mem1', length=1, delay_cost=1)
	S += t410_mem1 >= 63
	t410_mem1 += MAS_MEM[1]

	t4_t100 = S.Task('t4_t100', length=3, delay_cost=1)
	S += t4_t100 >= 63
	t4_t100 += MAS[0]

	t520_in = S.Task('t520_in', length=1, delay_cost=1)
	S += t520_in >= 63
	t520_in += MAS_in[0]

	t520_mem0 = S.Task('t520_mem0', length=1, delay_cost=1)
	S += t520_mem0 >= 63
	t520_mem0 += MAS_MEM[2]

	t520_mem1 = S.Task('t520_mem1', length=1, delay_cost=1)
	S += t520_mem1 >= 63
	t520_mem1 += MAS_MEM[3]

	t5_t1_t5 = S.Task('t5_t1_t5', length=3, delay_cost=1)
	S += t5_t1_t5 >= 63
	t5_t1_t5 += MAS[1]

	t410 = S.Task('t410', length=3, delay_cost=1)
	S += t410 >= 64
	t410 += MAS[1]

	t421_in = S.Task('t421_in', length=1, delay_cost=1)
	S += t421_in >= 64
	t421_in += MAS_in[1]

	t421_mem0 = S.Task('t421_mem0', length=1, delay_cost=1)
	S += t421_mem0 >= 64
	t421_mem0 += MAS_MEM[0]

	t421_mem1 = S.Task('t421_mem1', length=1, delay_cost=1)
	S += t421_mem1 >= 64
	t421_mem1 += MAS_MEM[1]

	t520 = S.Task('t520', length=3, delay_cost=1)
	S += t520 >= 64
	t520 += MAS[0]

	t5_t70_in = S.Task('t5_t70_in', length=1, delay_cost=1)
	S += t5_t70_in >= 64
	t5_t70_in += MAS_in[0]

	t5_t70_mem0 = S.Task('t5_t70_mem0', length=1, delay_cost=1)
	S += t5_t70_mem0 >= 64
	t5_t70_mem0 += MAS_MEM[2]

	t5_t70_mem1 = S.Task('t5_t70_mem1', length=1, delay_cost=1)
	S += t5_t70_mem1 >= 64
	t5_t70_mem1 += MAS_MEM[3]

	t421 = S.Task('t421', length=3, delay_cost=1)
	S += t421 >= 65
	t421 += MAS[1]

	t5_t60_in = S.Task('t5_t60_in', length=1, delay_cost=1)
	S += t5_t60_in >= 65
	t5_t60_in += MAS_in[1]

	t5_t60_mem0 = S.Task('t5_t60_mem0', length=1, delay_cost=1)
	S += t5_t60_mem0 >= 65
	t5_t60_mem0 += MM_MEM[0]

	t5_t60_mem1 = S.Task('t5_t60_mem1', length=1, delay_cost=1)
	S += t5_t60_mem1 >= 65
	t5_t60_mem1 += MM_MEM[1]

	t5_t70 = S.Task('t5_t70', length=3, delay_cost=1)
	S += t5_t70 >= 65
	t5_t70 += MAS[0]

	t5_t60 = S.Task('t5_t60', length=3, delay_cost=1)
	S += t5_t60 >= 66
	t5_t60 += MAS[1]

	t5_t6_t5_in = S.Task('t5_t6_t5_in', length=1, delay_cost=1)
	S += t5_t6_t5_in >= 66
	t5_t6_t5_in += MAS_in[0]

	t5_t6_t5_mem0 = S.Task('t5_t6_t5_mem0', length=1, delay_cost=1)
	S += t5_t6_t5_mem0 >= 66
	t5_t6_t5_mem0 += MM_MEM[0]

	t5_t6_t5_mem1 = S.Task('t5_t6_t5_mem1', length=1, delay_cost=1)
	S += t5_t6_t5_mem1 >= 66
	t5_t6_t5_mem1 += MM_MEM[1]

	t5_t21_in = S.Task('t5_t21_in', length=1, delay_cost=1)
	S += t5_t21_in >= 67
	t5_t21_in += MAS_in[0]

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	S += t5_t21_mem0 >= 67
	t5_t21_mem0 += MM_MEM[0]

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	S += t5_t21_mem1 >= 67
	t5_t21_mem1 += MAS_MEM[3]

	t5_t6_t5 = S.Task('t5_t6_t5', length=3, delay_cost=1)
	S += t5_t6_t5 >= 67
	t5_t6_t5 += MAS[0]

	t5_t01_in = S.Task('t5_t01_in', length=1, delay_cost=1)
	S += t5_t01_in >= 68
	t5_t01_in += MAS_in[0]

	t5_t01_mem0 = S.Task('t5_t01_mem0', length=1, delay_cost=1)
	S += t5_t01_mem0 >= 68
	t5_t01_mem0 += MM_MEM[0]

	t5_t01_mem1 = S.Task('t5_t01_mem1', length=1, delay_cost=1)
	S += t5_t01_mem1 >= 68
	t5_t01_mem1 += MAS_MEM[1]

	t5_t21 = S.Task('t5_t21', length=3, delay_cost=1)
	S += t5_t21 >= 68
	t5_t21 += MAS[0]

	t5_t01 = S.Task('t5_t01', length=3, delay_cost=1)
	S += t5_t01 >= 69
	t5_t01 += MAS[0]

	t5_t11_in = S.Task('t5_t11_in', length=1, delay_cost=1)
	S += t5_t11_in >= 69
	t5_t11_in += MAS_in[0]

	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	S += t5_t11_mem0 >= 69
	t5_t11_mem0 += MM_MEM[0]

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	S += t5_t11_mem1 >= 69
	t5_t11_mem1 += MAS_MEM[3]

	t5_t11 = S.Task('t5_t11', length=3, delay_cost=1)
	S += t5_t11 >= 70
	t5_t11 += MAS[0]

	t5_t81_in = S.Task('t5_t81_in', length=1, delay_cost=1)
	S += t5_t81_in >= 70
	t5_t81_in += MAS_in[1]

	t5_t81_mem0 = S.Task('t5_t81_mem0', length=1, delay_cost=1)
	S += t5_t81_mem0 >= 70
	t5_t81_mem0 += MM_MEM[0]

	t5_t81_mem1 = S.Task('t5_t81_mem1', length=1, delay_cost=1)
	S += t5_t81_mem1 >= 70
	t5_t81_mem1 += MAS_MEM[1]

	t5_t81 = S.Task('t5_t81', length=3, delay_cost=1)
	S += t5_t81 >= 71
	t5_t81 += MAS[1]


	# new tasks
	t400 = S.Task('t400', length=3, delay_cost=1)
	t400 += alt(MAS)
	t400_in = S.Task('t400_in', length=1, delay_cost=1)
	t400_in += alt(MAS_in)
	S += t400_in*MAS_in[0]<=t400*MAS[0]

	S += t400_in*MAS_in[1]<=t400*MAS[1]

	t400_mem0 = S.Task('t400_mem0', length=1, delay_cost=1)
	t400_mem0 += MAS_MEM[0]
	S += 32 < t400_mem0
	S += t400_mem0 <= t400

	t400_mem1 = S.Task('t400_mem1', length=1, delay_cost=1)
	t400_mem1 += MAS_MEM[1]
	S += 65 < t400_mem1
	S += t400_mem1 <= t400

	t401 = S.Task('t401', length=3, delay_cost=1)
	t401 += alt(MAS)
	t401_in = S.Task('t401_in', length=1, delay_cost=1)
	t401_in += alt(MAS_in)
	S += t401_in*MAS_in[0]<=t401*MAS[0]

	S += t401_in*MAS_in[1]<=t401*MAS[1]

	t401_mem0 = S.Task('t401_mem0', length=1, delay_cost=1)
	t401_mem0 += MAS_MEM[2]
	S += 58 < t401_mem0
	S += t401_mem0 <= t401

	t401_mem1 = S.Task('t401_mem1', length=1, delay_cost=1)
	t401_mem1 += MAS_MEM[1]
	S += 54 < t401_mem1
	S += t401_mem1 <= t401

	t411 = S.Task('t411', length=3, delay_cost=1)
	t411 += alt(MAS)
	t411_in = S.Task('t411_in', length=1, delay_cost=1)
	t411_in += alt(MAS_in)
	S += t411_in*MAS_in[0]<=t411*MAS[0]

	S += t411_in*MAS_in[1]<=t411*MAS[1]

	t411_mem0 = S.Task('t411_mem0', length=1, delay_cost=1)
	t411_mem0 += MAS_MEM[2]
	S += 52 < t411_mem0
	S += t411_mem0 <= t411

	t411_mem1 = S.Task('t411_mem1', length=1, delay_cost=1)
	t411_mem1 += MAS_MEM[3]
	S += 62 < t411_mem1
	S += t411_mem1 <= t411

	t5_t100 = S.Task('t5_t100', length=3, delay_cost=1)
	t5_t100 += alt(MAS)
	t5_t100_in = S.Task('t5_t100_in', length=1, delay_cost=1)
	t5_t100_in += alt(MAS_in)
	S += t5_t100_in*MAS_in[0]<=t5_t100*MAS[0]

	S += t5_t100_in*MAS_in[1]<=t5_t100*MAS[1]

	t5_t100_mem0 = S.Task('t5_t100_mem0', length=1, delay_cost=1)
	t5_t100_mem0 += MAS_MEM[2]
	S += 57 < t5_t100_mem0
	S += t5_t100_mem0 <= t5_t100

	t5_t100_mem1 = S.Task('t5_t100_mem1', length=1, delay_cost=1)
	t5_t100_mem1 += MAS_MEM[1]
	S += 70 < t5_t100_mem1
	S += t5_t100_mem1 <= t5_t100

	t5_t101 = S.Task('t5_t101', length=3, delay_cost=1)
	t5_t101 += alt(MAS)
	t5_t101_in = S.Task('t5_t101_in', length=1, delay_cost=1)
	t5_t101_in += alt(MAS_in)
	S += t5_t101_in*MAS_in[0]<=t5_t101*MAS[0]

	S += t5_t101_in*MAS_in[1]<=t5_t101*MAS[1]

	t5_t101_mem0 = S.Task('t5_t101_mem0', length=1, delay_cost=1)
	t5_t101_mem0 += MAS_MEM[0]
	S += 70 < t5_t101_mem0
	S += t5_t101_mem0 <= t5_t101

	t5_t101_mem1 = S.Task('t5_t101_mem1', length=1, delay_cost=1)
	t5_t101_mem1 += MAS_MEM[3]
	S += 57 < t5_t101_mem1
	S += t5_t101_mem1 <= t5_t101

	t5_t61 = S.Task('t5_t61', length=3, delay_cost=1)
	t5_t61 += alt(MAS)
	t5_t61_in = S.Task('t5_t61_in', length=1, delay_cost=1)
	t5_t61_in += alt(MAS_in)
	S += t5_t61_in*MAS_in[0]<=t5_t61*MAS[0]

	S += t5_t61_in*MAS_in[1]<=t5_t61*MAS[1]

	t5_t61_mem0 = S.Task('t5_t61_mem0', length=1, delay_cost=1)
	t5_t61_mem0 += MM_MEM[0]
	S += 71 < t5_t61_mem0
	S += t5_t61_mem0 <= t5_t61

	t5_t61_mem1 = S.Task('t5_t61_mem1', length=1, delay_cost=1)
	t5_t61_mem1 += MAS_MEM[1]
	S += 69 < t5_t61_mem1
	S += t5_t61_mem1 <= t5_t61

	t5_t71 = S.Task('t5_t71', length=3, delay_cost=1)
	t5_t71 += alt(MAS)
	t5_t71_in = S.Task('t5_t71_in', length=1, delay_cost=1)
	t5_t71_in += alt(MAS_in)
	S += t5_t71_in*MAS_in[0]<=t5_t71*MAS[0]

	S += t5_t71_in*MAS_in[1]<=t5_t71*MAS[1]

	t5_t71_mem0 = S.Task('t5_t71_mem0', length=1, delay_cost=1)
	t5_t71_mem0 += MAS_MEM[0]
	S += 71 < t5_t71_mem0
	S += t5_t71_mem0 <= t5_t71

	t5_t71_mem1 = S.Task('t5_t71_mem1', length=1, delay_cost=1)
	t5_t71_mem1 += MAS_MEM[1]
	S += 72 < t5_t71_mem1
	S += t5_t71_mem1 <= t5_t71

	t510 = S.Task('t510', length=3, delay_cost=1)
	t510 += alt(MAS)
	t510_in = S.Task('t510_in', length=1, delay_cost=1)
	t510_in += alt(MAS_in)
	S += t510_in*MAS_in[0]<=t510*MAS[0]

	S += t510_in*MAS_in[1]<=t510*MAS[1]

	t510_mem0 = S.Task('t510_mem0', length=1, delay_cost=1)
	t510_mem0 += MAS_MEM[2]
	S += 68 < t510_mem0
	S += t510_mem0 <= t510

	t510_mem1 = S.Task('t510_mem1', length=1, delay_cost=1)
	t510_mem1 += MAS_MEM[1]
	S += 67 < t510_mem1
	S += t510_mem1 <= t510

	t521 = S.Task('t521', length=3, delay_cost=1)
	t521 += alt(MAS)
	t521_in = S.Task('t521_in', length=1, delay_cost=1)
	t521_in += alt(MAS_in)
	S += t521_in*MAS_in[0]<=t521*MAS[0]

	S += t521_in*MAS_in[1]<=t521*MAS[1]

	t521_mem0 = S.Task('t521_mem0', length=1, delay_cost=1)
	t521_mem0 += MAS_MEM[2]
	S += 73 < t521_mem0
	S += t521_mem0 <= t521

	t521_mem1 = S.Task('t521_mem1', length=1, delay_cost=1)
	t521_mem1 += MAS_MEM[1]
	S += 72 < t521_mem1
	S += t521_mem1 <= t521

	t150 = S.Task('t150', length=3, delay_cost=1)
	t150 += alt(MAS)
	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	t150_in += alt(MAS_in)
	S += t150_in*MAS_in[0]<=t150*MAS[0]

	S += t150_in*MAS_in[1]<=t150*MAS[1]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += MAS_MEM[0]
	S += 43 < t150_mem0
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += MAS_MEM[3]
	S += 66 < t150_mem1
	S += t150_mem1 <= t150

	t161 = S.Task('t161', length=3, delay_cost=1)
	t161 += alt(MAS)
	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	t161_in += alt(MAS_in)
	S += t161_in*MAS_in[0]<=t161*MAS[0]

	S += t161_in*MAS_in[1]<=t161*MAS[1]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += MAS_MEM[2]
	S += 51 < t161_mem0
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += MAS_MEM[3]
	S += 67 < t161_mem1
	S += t161_mem1 <= t161

	c210 = S.Task('c210', length=3, delay_cost=1)
	c210 += alt(MAS)
	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	c210_in += alt(MAS_in)
	S += c210_in*MAS_in[0]<=c210*MAS[0]

	S += c210_in*MAS_in[1]<=c210*MAS[1]

	S += 36<c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MAS_MEM[0]
	S += 66 < c210_mem0
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MAS_MEM[1]
	S += 63 < c210_mem1
	S += c210_mem1 <= c210

	c200 = S.Task('c200', length=3, delay_cost=1)
	c200 += alt(MAS)
	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MAS_in)
	S += c200_in*MAS_in[0]<=c200*MAS[0]

	S += c200_in*MAS_in[1]<=c200*MAS[1]

	S += 40<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += MAS_MEM[2]
	S += 64 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAS_MEM[3]
	S += 66 < c200_mem1
	S += c200_mem1 <= c200

	c111 = S.Task('c111', length=3, delay_cost=1)
	c111 += alt(MAS)
	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	c111_in += alt(MAS_in)
	S += c111_in*MAS_in[0]<=c111*MAS[0]

	S += c111_in*MAS_in[1]<=c111*MAS[1]

	S += 39<c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += MAS_MEM[0]
	S += 53 < c111_mem0
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += MAS_MEM[3]
	S += 67 < c111_mem1
	S += c111_mem1 <= c111

	t500 = S.Task('t500', length=3, delay_cost=1)
	t500 += alt(MAS)
	t500_in = S.Task('t500_in', length=1, delay_cost=1)
	t500_in += alt(MAS_in)
	S += t500_in*MAS_in[0]<=t500*MAS[0]

	S += t500_in*MAS_in[1]<=t500*MAS[1]

	t500_mem0 = S.Task('t500_mem0', length=1, delay_cost=1)
	t500_mem0 += MAS_MEM[2]
	S += 61 < t500_mem0
	S += t500_mem0 <= t500

	t500_mem1 = S.Task('t500_mem1', length=1, delay_cost=1)
	t500_mem1 += alt(MAS_MEM)
	S += (t5_t100*MAS[0])-1 < t500_mem1*MAS_MEM[1]
	S += (t5_t100*MAS[1])-1 < t500_mem1*MAS_MEM[3]
	S += t500_mem1 <= t500

	t501 = S.Task('t501', length=3, delay_cost=1)
	t501 += alt(MAS)
	t501_in = S.Task('t501_in', length=1, delay_cost=1)
	t501_in += alt(MAS_in)
	S += t501_in*MAS_in[0]<=t501*MAS[0]

	S += t501_in*MAS_in[1]<=t501*MAS[1]

	t501_mem0 = S.Task('t501_mem0', length=1, delay_cost=1)
	t501_mem0 += MAS_MEM[0]
	S += 71 < t501_mem0
	S += t501_mem0 <= t501

	t501_mem1 = S.Task('t501_mem1', length=1, delay_cost=1)
	t501_mem1 += alt(MAS_MEM)
	S += (t5_t101*MAS[0])-1 < t501_mem1*MAS_MEM[1]
	S += (t5_t101*MAS[1])-1 < t501_mem1*MAS_MEM[3]
	S += t501_mem1 <= t501

	t511 = S.Task('t511', length=3, delay_cost=1)
	t511 += alt(MAS)
	t511_in = S.Task('t511_in', length=1, delay_cost=1)
	t511_in += alt(MAS_in)
	S += t511_in*MAS_in[0]<=t511*MAS[0]

	S += t511_in*MAS_in[1]<=t511*MAS[1]

	t511_mem0 = S.Task('t511_mem0', length=1, delay_cost=1)
	t511_mem0 += alt(MAS_MEM)
	S += (t5_t61*MAS[0])-1 < t511_mem0*MAS_MEM[0]
	S += (t5_t61*MAS[1])-1 < t511_mem0*MAS_MEM[2]
	S += t511_mem0 <= t511

	t511_mem1 = S.Task('t511_mem1', length=1, delay_cost=1)
	t511_mem1 += alt(MAS_MEM)
	S += (t5_t71*MAS[0])-1 < t511_mem1*MAS_MEM[1]
	S += (t5_t71*MAS[1])-1 < t511_mem1*MAS_MEM[3]
	S += t511_mem1 <= t511

	t140 = S.Task('t140', length=3, delay_cost=1)
	t140 += alt(MAS)
	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	t140_in += alt(MAS_in)
	S += t140_in*MAS_in[0]<=t140*MAS[0]

	S += t140_in*MAS_in[1]<=t140*MAS[1]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += MAS_MEM[2]
	S += 64 < t140_mem0
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += alt(MAS_MEM)
	S += (t400*MAS[0])-1 < t140_mem1*MAS_MEM[1]
	S += (t400*MAS[1])-1 < t140_mem1*MAS_MEM[3]
	S += t140_mem1 <= t140

	t141 = S.Task('t141', length=3, delay_cost=1)
	t141 += alt(MAS)
	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	t141_in += alt(MAS_in)
	S += t141_in*MAS_in[0]<=t141*MAS[0]

	S += t141_in*MAS_in[1]<=t141*MAS[1]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += MAS_MEM[2]
	S += 60 < t141_mem0
	S += t141_mem0 <= t141

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	t141_mem1 += alt(MAS_MEM)
	S += (t401*MAS[0])-1 < t141_mem1*MAS_MEM[1]
	S += (t401*MAS[1])-1 < t141_mem1*MAS_MEM[3]
	S += t141_mem1 <= t141

	t151 = S.Task('t151', length=3, delay_cost=1)
	t151 += alt(MAS)
	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	t151_in += alt(MAS_in)
	S += t151_in*MAS_in[0]<=t151*MAS[0]

	S += t151_in*MAS_in[1]<=t151*MAS[1]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[0]
	S += 53 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(MAS_MEM)
	S += (t411*MAS[0])-1 < t151_mem1*MAS_MEM[1]
	S += (t411*MAS[1])-1 < t151_mem1*MAS_MEM[3]
	S += t151_mem1 <= t151

	c010 = S.Task('c010', length=3, delay_cost=1)
	c010 += alt(MAS)
	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MAS_in)
	S += c010_in*MAS_in[0]<=c010*MAS[0]

	S += c010_in*MAS_in[1]<=c010*MAS[1]

	S += 40<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += alt(MAS_MEM)
	S += (t510*MAS[0])-1 < c010_mem0*MAS_MEM[0]
	S += (t510*MAS[1])-1 < c010_mem0*MAS_MEM[2]
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += alt(MAS_MEM)
	S += (t150*MAS[0])-1 < c010_mem1*MAS_MEM[1]
	S += (t150*MAS[1])-1 < c010_mem1*MAS_MEM[3]
	S += c010_mem1 <= c010

	c211 = S.Task('c211', length=3, delay_cost=1)
	c211 += alt(MAS)
	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	c211_in += alt(MAS_in)
	S += c211_in*MAS_in[0]<=c211*MAS[0]

	S += c211_in*MAS_in[1]<=c211*MAS[1]

	S += 33<c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(MAS_MEM)
	S += (t521*MAS[0])-1 < c211_mem0*MAS_MEM[0]
	S += (t521*MAS[1])-1 < c211_mem0*MAS_MEM[2]
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < c211_mem1*MAS_MEM[1]
	S += (t161*MAS[1])-1 < c211_mem1*MAS_MEM[3]
	S += c211_mem1 <= c211

	c000 = S.Task('c000', length=3, delay_cost=1)
	c000 += alt(MAS)
	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	c000_in += alt(MAS_in)
	S += c000_in*MAS_in[0]<=c000*MAS[0]

	S += c000_in*MAS_in[1]<=c000*MAS[1]

	S += 50<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[0]
	S += 56 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (t400*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (t400*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += c000_mem1 <= c000

	c001 = S.Task('c001', length=3, delay_cost=1)
	c001 += alt(MAS)
	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	c001_in += alt(MAS_in)
	S += c001_in*MAS_in[0]<=c001*MAS[0]

	S += c001_in*MAS_in[1]<=c001*MAS[1]

	S += 48<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[0]
	S += 55 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (t401*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += (t401*MAS[1])-1 < c001_mem1*MAS_MEM[3]
	S += c001_mem1 <= c001

	c201 = S.Task('c201', length=3, delay_cost=1)
	c201 += alt(MAS)
	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MAS_in)
	S += c201_in*MAS_in[0]<=c201*MAS[0]

	S += c201_in*MAS_in[1]<=c201*MAS[1]

	S += 38<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += MAS_MEM[2]
	S += 60 < c201_mem0
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += alt(MAS_MEM)
	S += (t411*MAS[0])-1 < c201_mem1*MAS_MEM[1]
	S += (t411*MAS[1])-1 < c201_mem1*MAS_MEM[3]
	S += c201_mem1 <= c201

	c100 = S.Task('c100', length=3, delay_cost=1)
	c100 += alt(MAS)
	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	c100_in += alt(MAS_in)
	S += c100_in*MAS_in[0]<=c100*MAS[0]

	S += c100_in*MAS_in[1]<=c100*MAS[1]

	S += 35<c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(MAS_MEM)
	S += (t500*MAS[0])-1 < c100_mem0*MAS_MEM[0]
	S += (t500*MAS[1])-1 < c100_mem0*MAS_MEM[2]
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < c100_mem1*MAS_MEM[1]
	S += (t140*MAS[1])-1 < c100_mem1*MAS_MEM[3]
	S += c100_mem1 <= c100

	c101 = S.Task('c101', length=3, delay_cost=1)
	c101 += alt(MAS)
	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	c101_in += alt(MAS_in)
	S += c101_in*MAS_in[0]<=c101*MAS[0]

	S += c101_in*MAS_in[1]<=c101*MAS[1]

	S += 42<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MAS_MEM)
	S += (t501*MAS[0])-1 < c101_mem0*MAS_MEM[0]
	S += (t501*MAS[1])-1 < c101_mem0*MAS_MEM[2]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < c101_mem1*MAS_MEM[1]
	S += (t141*MAS[1])-1 < c101_mem1*MAS_MEM[3]
	S += c101_mem1 <= c101

	c011 = S.Task('c011', length=3, delay_cost=1)
	c011 += alt(MAS)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MAS_in)
	S += c011_in*MAS_in[0]<=c011*MAS[0]

	S += c011_in*MAS_in[1]<=c011*MAS[1]

	S += 38<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(MAS_MEM)
	S += (t511*MAS[0])-1 < c011_mem0*MAS_MEM[0]
	S += (t511*MAS[1])-1 < c011_mem0*MAS_MEM[2]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(MAS_MEM)
	S += (t151*MAS[0])-1 < c011_mem1*MAS_MEM[1]
	S += (t151*MAS[1])-1 < c011_mem1*MAS_MEM[3]
	S += c011_mem1 <= c011

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS2/SPARSE/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution
