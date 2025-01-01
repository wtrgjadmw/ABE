from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 185
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=1, size=2, periods=range(1, horizon))
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

	t4_t50 = S.Task('t4_t50', length=2, delay_cost=1)
	S += t4_t50 >= 1
	t4_t50 += MAS[0]

	t1_t2 = S.Task('t1_t2', length=2, delay_cost=1)
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

	t4_t2_t2 = S.Task('t4_t2_t2', length=2, delay_cost=1)
	S += t4_t2_t2 >= 3
	t4_t2_t2 += MAS[0]

	t4_t0_t1 = S.Task('t4_t0_t1', length=8, delay_cost=1)
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

	t4_t2_t0 = S.Task('t4_t2_t0', length=8, delay_cost=1)
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

	t2_t1 = S.Task('t2_t1', length=8, delay_cost=1)
	S += t2_t1 >= 6
	t2_t1 += MM[0]

	t1_t0 = S.Task('t1_t0', length=8, delay_cost=1)
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

	t4_t0_t2 = S.Task('t4_t0_t2', length=2, delay_cost=1)
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

	t4_t1_t0 = S.Task('t4_t1_t0', length=8, delay_cost=1)
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

	t4_t8_t0 = S.Task('t4_t8_t0', length=8, delay_cost=1)
	S += t4_t8_t0 >= 10
	t4_t8_t0 += MM[0]

	t2_t2 = S.Task('t2_t2', length=2, delay_cost=1)
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

	t4_t0_t3 = S.Task('t4_t0_t3', length=2, delay_cost=1)
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

	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	S += t4_t0_t4_in >= 13
	t4_t0_t4_in += MM_in[0]

	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	S += t4_t0_t4_mem0 >= 13
	t4_t0_t4_mem0 += MAS_MEM[0]

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	S += t4_t0_t4_mem1 >= 13
	t4_t0_t4_mem1 += MAS_MEM[1]

	t4_t1_t3_in = S.Task('t4_t1_t3_in', length=1, delay_cost=1)
	S += t4_t1_t3_in >= 13
	t4_t1_t3_in += MAS_in[0]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 13
	t4_t1_t3_mem0 += MAIN_MEM_r[0]

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 13
	t4_t1_t3_mem1 += MAIN_MEM_r[1]

	t4_t40 = S.Task('t4_t40', length=2, delay_cost=1)
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

	t4_t0_t4 = S.Task('t4_t0_t4', length=8, delay_cost=1)
	S += t4_t0_t4 >= 14
	t4_t0_t4 += MM[0]

	t4_t1_t3 = S.Task('t4_t1_t3', length=2, delay_cost=1)
	S += t4_t1_t3 >= 14
	t4_t1_t3 += MAS[0]

	t4_t0_t0 = S.Task('t4_t0_t0', length=8, delay_cost=1)
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

	t4_t41 = S.Task('t4_t41', length=2, delay_cost=1)
	S += t4_t41 >= 16
	t4_t41 += MAS[0]

	t4_t6_t0 = S.Task('t4_t6_t0', length=8, delay_cost=1)
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

	t4_t1_t1 = S.Task('t4_t1_t1', length=8, delay_cost=1)
	S += t4_t1_t1 >= 17
	t4_t1_t1 += MM[0]

	t1_t3 = S.Task('t1_t3', length=2, delay_cost=1)
	S += t1_t3 >= 18
	t1_t3 += MAS[0]

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

	t4_t6_t2 = S.Task('t4_t6_t2', length=2, delay_cost=1)
	S += t4_t6_t2 >= 19
	t4_t6_t2 += MAS[0]

	t4_t8_t1 = S.Task('t4_t8_t1', length=8, delay_cost=1)
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

	t2_t0 = S.Task('t2_t0', length=8, delay_cost=1)
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

	t1_t4 = S.Task('t1_t4', length=8, delay_cost=1)
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

	t4_t51 = S.Task('t4_t51', length=2, delay_cost=1)
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

	t4_t0_t5_in = S.Task('t4_t0_t5_in', length=1, delay_cost=1)
	S += t4_t0_t5_in >= 22
	t4_t0_t5_in += MAS_in[0]

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	S += t4_t0_t5_mem0 >= 22
	t4_t0_t5_mem0 += MM_MEM[0]

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	S += t4_t0_t5_mem1 >= 22
	t4_t0_t5_mem1 += MM_MEM[1]

	t4_t2_t3 = S.Task('t4_t2_t3', length=2, delay_cost=1)
	S += t4_t2_t3 >= 22
	t4_t2_t3 += MAS[0]

	t1_t1 = S.Task('t1_t1', length=8, delay_cost=1)
	S += t1_t1 >= 23
	t1_t1 += MM[0]

	t4_t0_t5 = S.Task('t4_t0_t5', length=2, delay_cost=1)
	S += t4_t0_t5 >= 23
	t4_t0_t5 += MAS[0]

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

	t4_t1_t2 = S.Task('t4_t1_t2', length=2, delay_cost=1)
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

	t4_t6_t1 = S.Task('t4_t6_t1', length=8, delay_cost=1)
	S += t4_t6_t1 >= 24
	t4_t6_t1 += MM[0]

	t2_t3 = S.Task('t2_t3', length=2, delay_cost=1)
	S += t2_t3 >= 25
	t2_t3 += MAS[0]

	t4_t00_in = S.Task('t4_t00_in', length=1, delay_cost=1)
	S += t4_t00_in >= 25
	t4_t00_in += MAS_in[0]

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	S += t4_t00_mem0 >= 25
	t4_t00_mem0 += MM_MEM[0]

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	S += t4_t00_mem1 >= 25
	t4_t00_mem1 += MM_MEM[1]

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 25
	t4_t2_t1_in += MM_in[0]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 25
	t4_t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 25
	t4_t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t4 = S.Task('t4_t2_t4', length=8, delay_cost=1)
	S += t4_t2_t4 >= 25
	t4_t2_t4 += MM[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 26
	t0_t3_in += MAS_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 26
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 26
	t0_t3_mem1 += MAIN_MEM_r[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 26
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 26
	t2_t4_mem0 += MAS_MEM[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 26
	t2_t4_mem1 += MAS_MEM[1]

	t4_t00 = S.Task('t4_t00', length=2, delay_cost=1)
	S += t4_t00 >= 26
	t4_t00 += MAS[0]

	t4_t2_t1 = S.Task('t4_t2_t1', length=8, delay_cost=1)
	S += t4_t2_t1 >= 26
	t4_t2_t1 += MM[0]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 27
	t0_t2_in += MAS_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 27
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 27
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=2, delay_cost=1)
	S += t0_t3 >= 27
	t0_t3 += MAS[0]

	t2_t4 = S.Task('t2_t4', length=8, delay_cost=1)
	S += t2_t4 >= 27
	t2_t4 += MM[0]

	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	S += t4_t1_t4_in >= 27
	t4_t1_t4_in += MM_in[0]

	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	S += t4_t1_t4_mem0 >= 27
	t4_t1_t4_mem0 += MAS_MEM[0]

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	S += t4_t1_t4_mem1 >= 27
	t4_t1_t4_mem1 += MAS_MEM[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 28
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 28
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 28
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t2 = S.Task('t0_t2', length=2, delay_cost=1)
	S += t0_t2 >= 28
	t0_t2 += MAS[0]

	t4_t1_t4 = S.Task('t4_t1_t4', length=8, delay_cost=1)
	S += t4_t1_t4 >= 28
	t4_t1_t4 += MM[0]

	t4_t80_in = S.Task('t4_t80_in', length=1, delay_cost=1)
	S += t4_t80_in >= 28
	t4_t80_in += MAS_in[0]

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	S += t4_t80_mem0 >= 28
	t4_t80_mem0 += MM_MEM[0]

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	S += t4_t80_mem1 >= 28
	t4_t80_mem1 += MM_MEM[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 29
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 29
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 29
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=8, delay_cost=1)
	S += t0_t1 >= 29
	t0_t1 += MM[0]

	t4_t6_t3_in = S.Task('t4_t6_t3_in', length=1, delay_cost=1)
	S += t4_t6_t3_in >= 29
	t4_t6_t3_in += MAS_in[0]

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	S += t4_t6_t3_mem0 >= 29
	t4_t6_t3_mem0 += MAS_MEM[0]

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	S += t4_t6_t3_mem1 >= 29
	t4_t6_t3_mem1 += MAS_MEM[1]

	t4_t80 = S.Task('t4_t80', length=2, delay_cost=1)
	S += t4_t80 >= 29
	t4_t80 += MAS[0]

	t0_t0 = S.Task('t0_t0', length=8, delay_cost=1)
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

	t4_t6_t3 = S.Task('t4_t6_t3', length=2, delay_cost=1)
	S += t4_t6_t3 >= 30
	t4_t6_t3 += MAS[0]

	t5_t8_t2_in = S.Task('t5_t8_t2_in', length=1, delay_cost=1)
	S += t5_t8_t2_in >= 30
	t5_t8_t2_in += MAS_in[0]

	t5_t8_t2_mem0 = S.Task('t5_t8_t2_mem0', length=1, delay_cost=1)
	S += t5_t8_t2_mem0 >= 30
	t5_t8_t2_mem0 += MAIN_MEM_r[0]

	t5_t8_t2_mem1 = S.Task('t5_t8_t2_mem1', length=1, delay_cost=1)
	S += t5_t8_t2_mem1 >= 30
	t5_t8_t2_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=8, delay_cost=1)
	S += t0_t4 >= 31
	t0_t4 += MM[0]

	t5_t0_t2_in = S.Task('t5_t0_t2_in', length=1, delay_cost=1)
	S += t5_t0_t2_in >= 31
	t5_t0_t2_in += MAS_in[0]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 31
	t5_t0_t2_mem0 += MAIN_MEM_r[0]

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 31
	t5_t0_t2_mem1 += MAIN_MEM_r[1]

	t5_t8_t2 = S.Task('t5_t8_t2', length=2, delay_cost=1)
	S += t5_t8_t2 >= 31
	t5_t8_t2 += MAS[0]

	t4_t8_t3_in = S.Task('t4_t8_t3_in', length=1, delay_cost=1)
	S += t4_t8_t3_in >= 32
	t4_t8_t3_in += MAS_in[0]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 32
	t4_t8_t3_mem0 += MAIN_MEM_r[0]

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 32
	t4_t8_t3_mem1 += MAIN_MEM_r[1]

	t5_t0_t2 = S.Task('t5_t0_t2', length=2, delay_cost=1)
	S += t5_t0_t2 >= 32
	t5_t0_t2 += MAS[0]

	t4_t8_t3 = S.Task('t4_t8_t3', length=2, delay_cost=1)
	S += t4_t8_t3 >= 33
	t4_t8_t3 += MAS[0]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 33
	t71_in += MAS_in[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 33
	t71_mem0 += MAIN_MEM_r[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 33
	t71_mem1 += MAIN_MEM_r[1]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 34
	t101_in += MAS_in[0]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 34
	t101_mem0 += MAIN_MEM_r[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 34
	t101_mem1 += MAIN_MEM_r[1]

	t71 = S.Task('t71', length=2, delay_cost=1)
	S += t71 >= 34
	t71 += MAS[0]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 35
	t100_in += MAS_in[0]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 35
	t100_mem0 += MAIN_MEM_r[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 35
	t100_mem1 += MAIN_MEM_r[1]

	t101 = S.Task('t101', length=2, delay_cost=1)
	S += t101 >= 35
	t101 += MAS[0]

	t100 = S.Task('t100', length=2, delay_cost=1)
	S += t100 >= 36
	t100 += MAS[0]

	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	S += t5_t2_t1_in >= 36
	t5_t2_t1_in += MM_in[0]

	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	S += t5_t2_t1_mem0 >= 36
	t5_t2_t1_mem0 += MAS_MEM[0]

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	S += t5_t2_t1_mem1 >= 36
	t5_t2_t1_mem1 += MAS_MEM[1]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 36
	t91_in += MAS_in[0]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 36
	t91_mem0 += MAIN_MEM_r[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 36
	t91_mem1 += MAIN_MEM_r[1]

	t5_t2_t1 = S.Task('t5_t2_t1', length=8, delay_cost=1)
	S += t5_t2_t1 >= 37
	t5_t2_t1 += MM[0]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 37
	t80_in += MAS_in[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 37
	t80_mem0 += MAIN_MEM_r[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 37
	t80_mem1 += MAIN_MEM_r[1]

	t91 = S.Task('t91', length=2, delay_cost=1)
	S += t91 >= 37
	t91 += MAS[0]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 38
	t5_t1_t1_in += MM_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 38
	t5_t1_t1_mem0 += MAS_MEM[0]

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 38
	t5_t1_t1_mem1 += MAS_MEM[1]

	t80 = S.Task('t80', length=2, delay_cost=1)
	S += t80 >= 38
	t80 += MAS[0]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 38
	t81_in += MAS_in[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 38
	t81_mem0 += MAIN_MEM_r[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 38
	t81_mem1 += MAIN_MEM_r[1]

	t5_t1_t1 = S.Task('t5_t1_t1', length=8, delay_cost=1)
	S += t5_t1_t1 >= 39
	t5_t1_t1 += MM[0]

	t81 = S.Task('t81', length=2, delay_cost=1)
	S += t81 >= 39
	t81 += MAS[0]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 39
	t90_in += MAS_in[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 39
	t90_mem0 += MAIN_MEM_r[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 39
	t90_mem1 += MAIN_MEM_r[1]

	t4_t8_t2_in = S.Task('t4_t8_t2_in', length=1, delay_cost=1)
	S += t4_t8_t2_in >= 40
	t4_t8_t2_in += MAS_in[0]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 40
	t4_t8_t2_mem0 += MAIN_MEM_r[0]

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 40
	t4_t8_t2_mem1 += MAIN_MEM_r[1]

	t90 = S.Task('t90', length=2, delay_cost=1)
	S += t90 >= 40
	t90 += MAS[0]

	t4_t8_t2 = S.Task('t4_t8_t2', length=2, delay_cost=1)
	S += t4_t8_t2 >= 41
	t4_t8_t2 += MAS[0]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 41
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 41
	t70_mem0 += MAIN_MEM_r[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 41
	t70_mem1 += MAIN_MEM_r[1]

	t4_t2_t5_in = S.Task('t4_t2_t5_in', length=1, delay_cost=1)
	S += t4_t2_t5_in >= 42
	t4_t2_t5_in += MAS_in[0]

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	S += t4_t2_t5_mem0 >= 42
	t4_t2_t5_mem0 += MM_MEM[0]

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	S += t4_t2_t5_mem1 >= 42
	t4_t2_t5_mem1 += MM_MEM[1]

	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	S += t5_t8_t1_in >= 42
	t5_t8_t1_in += MM_in[0]

	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	S += t5_t8_t1_mem0 >= 42
	t5_t8_t1_mem0 += MAIN_MEM_r[0]

	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	S += t5_t8_t1_mem1 >= 42
	t5_t8_t1_mem1 += MAS_MEM[1]

	t70 = S.Task('t70', length=2, delay_cost=1)
	S += t70 >= 42
	t70 += MAS[0]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 43
	t20_in += MAS_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 43
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 43
	t20_mem1 += MM_MEM[1]

	t4_t2_t5 = S.Task('t4_t2_t5', length=2, delay_cost=1)
	S += t4_t2_t5 >= 43
	t4_t2_t5 += MAS[0]

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 43
	t5_t0_t1_in += MM_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 43
	t5_t0_t1_mem0 += MAIN_MEM_r[0]

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 43
	t5_t0_t1_mem1 += MAS_MEM[1]

	t5_t8_t1 = S.Task('t5_t8_t1', length=8, delay_cost=1)
	S += t5_t8_t1 >= 43
	t5_t8_t1 += MM[0]

	t1_t5_in = S.Task('t1_t5_in', length=1, delay_cost=1)
	S += t1_t5_in >= 44
	t1_t5_in += MAS_in[0]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 44
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 44
	t1_t5_mem1 += MM_MEM[1]

	t20 = S.Task('t20', length=2, delay_cost=1)
	S += t20 >= 44
	t20 += MAS[0]

	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	S += t4_t8_t4_in >= 44
	t4_t8_t4_in += MM_in[0]

	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	S += t4_t8_t4_mem0 >= 44
	t4_t8_t4_mem0 += MAS_MEM[0]

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	S += t4_t8_t4_mem1 >= 44
	t4_t8_t4_mem1 += MAS_MEM[1]

	t5_t0_t1 = S.Task('t5_t0_t1', length=8, delay_cost=1)
	S += t5_t0_t1 >= 44
	t5_t0_t1 += MM[0]

	t1_t5 = S.Task('t1_t5', length=2, delay_cost=1)
	S += t1_t5 >= 45
	t1_t5 += MAS[0]

	t4_t1_t5_in = S.Task('t4_t1_t5_in', length=1, delay_cost=1)
	S += t4_t1_t5_in >= 45
	t4_t1_t5_in += MAS_in[0]

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	S += t4_t1_t5_mem0 >= 45
	t4_t1_t5_mem0 += MM_MEM[0]

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	S += t4_t1_t5_mem1 >= 45
	t4_t1_t5_mem1 += MM_MEM[1]

	t4_t8_t4 = S.Task('t4_t8_t4', length=8, delay_cost=1)
	S += t4_t8_t4 >= 45
	t4_t8_t4 += MM[0]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 45
	t5_t1_t0_in += MM_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 45
	t5_t1_t0_mem0 += MAS_MEM[0]

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 45
	t5_t1_t0_mem1 += MAS_MEM[1]

	t4_t1_t5 = S.Task('t4_t1_t5', length=2, delay_cost=1)
	S += t4_t1_t5 >= 46
	t4_t1_t5 += MAS[0]

	t4_t20_in = S.Task('t4_t20_in', length=1, delay_cost=1)
	S += t4_t20_in >= 46
	t4_t20_in += MAS_in[0]

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	S += t4_t20_mem0 >= 46
	t4_t20_mem0 += MM_MEM[0]

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	S += t4_t20_mem1 >= 46
	t4_t20_mem1 += MM_MEM[1]

	t5_t1_t0 = S.Task('t5_t1_t0', length=8, delay_cost=1)
	S += t5_t1_t0 >= 46
	t5_t1_t0 += MM[0]

	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	S += t5_t8_t0_in >= 46
	t5_t8_t0_in += MM_in[0]

	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	S += t5_t8_t0_mem0 >= 46
	t5_t8_t0_mem0 += MAIN_MEM_r[0]

	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	S += t5_t8_t0_mem1 >= 46
	t5_t8_t0_mem1 += MAS_MEM[1]

	t4_t20 = S.Task('t4_t20', length=2, delay_cost=1)
	S += t4_t20 >= 47
	t4_t20 += MAS[0]

	t4_t8_t5_in = S.Task('t4_t8_t5_in', length=1, delay_cost=1)
	S += t4_t8_t5_in >= 47
	t4_t8_t5_in += MAS_in[0]

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	S += t4_t8_t5_mem0 >= 47
	t4_t8_t5_mem0 += MM_MEM[0]

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	S += t4_t8_t5_mem1 >= 47
	t4_t8_t5_mem1 += MM_MEM[1]

	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	S += t5_t2_t0_in >= 47
	t5_t2_t0_in += MM_in[0]

	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	S += t5_t2_t0_mem0 >= 47
	t5_t2_t0_mem0 += MAS_MEM[0]

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	S += t5_t2_t0_mem1 >= 47
	t5_t2_t0_mem1 += MAS_MEM[1]

	t5_t8_t0 = S.Task('t5_t8_t0', length=8, delay_cost=1)
	S += t5_t8_t0 >= 47
	t5_t8_t0 += MM[0]

	t4_t10_in = S.Task('t4_t10_in', length=1, delay_cost=1)
	S += t4_t10_in >= 48
	t4_t10_in += MAS_in[0]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 48
	t4_t10_mem0 += MM_MEM[0]

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 48
	t4_t10_mem1 += MM_MEM[1]

	t4_t8_t5 = S.Task('t4_t8_t5', length=2, delay_cost=1)
	S += t4_t8_t5 >= 48
	t4_t8_t5 += MAS[0]

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 48
	t5_t0_t0_in += MM_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 48
	t5_t0_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 48
	t5_t0_t0_mem1 += MAS_MEM[1]

	t5_t2_t0 = S.Task('t5_t2_t0', length=8, delay_cost=1)
	S += t5_t2_t0 >= 48
	t5_t2_t0 += MM[0]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 49
	t2_t5_in += MAS_in[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 49
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 49
	t2_t5_mem1 += MM_MEM[1]

	t4_t10 = S.Task('t4_t10', length=2, delay_cost=1)
	S += t4_t10 >= 49
	t4_t10 += MAS[0]

	t5_t0_t0 = S.Task('t5_t0_t0', length=8, delay_cost=1)
	S += t5_t0_t0 >= 49
	t5_t0_t0 += MM[0]

	t2_t5 = S.Task('t2_t5', length=2, delay_cost=1)
	S += t2_t5 >= 50
	t2_t5 += MAS[0]

	t5_t1_t3_in = S.Task('t5_t1_t3_in', length=1, delay_cost=1)
	S += t5_t1_t3_in >= 50
	t5_t1_t3_in += MAS_in[0]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 50
	t5_t1_t3_mem0 += MAS_MEM[0]

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 50
	t5_t1_t3_mem1 += MAS_MEM[1]

	t5_t1_t3 = S.Task('t5_t1_t3', length=2, delay_cost=1)
	S += t5_t1_t3 >= 51
	t5_t1_t3 += MAS[0]

	t5_t50_in = S.Task('t5_t50_in', length=1, delay_cost=1)
	S += t5_t50_in >= 51
	t5_t50_in += MAS_in[0]

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	S += t5_t50_mem0 >= 51
	t5_t50_mem0 += MAS_MEM[0]

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	S += t5_t50_mem1 >= 51
	t5_t50_mem1 += MAS_MEM[1]

	t5_t41_in = S.Task('t5_t41_in', length=1, delay_cost=1)
	S += t5_t41_in >= 52
	t5_t41_in += MAS_in[0]

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	S += t5_t41_mem0 >= 52
	t5_t41_mem0 += MAIN_MEM_r[0]

	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	S += t5_t41_mem1 >= 52
	t5_t41_mem1 += MAS_MEM[1]

	t5_t50 = S.Task('t5_t50', length=2, delay_cost=1)
	S += t5_t50 >= 52
	t5_t50 += MAS[0]

	t5_t41 = S.Task('t5_t41', length=2, delay_cost=1)
	S += t5_t41 >= 53
	t5_t41 += MAS[0]

	t5_t51_in = S.Task('t5_t51_in', length=1, delay_cost=1)
	S += t5_t51_in >= 53
	t5_t51_in += MAS_in[0]

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	S += t5_t51_mem0 >= 53
	t5_t51_mem0 += MAS_MEM[0]

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	S += t5_t51_mem1 >= 53
	t5_t51_mem1 += MAS_MEM[1]

	t5_t51 = S.Task('t5_t51', length=2, delay_cost=1)
	S += t5_t51 >= 54
	t5_t51 += MAS[0]

	t5_t8_t3_in = S.Task('t5_t8_t3_in', length=1, delay_cost=1)
	S += t5_t8_t3_in >= 54
	t5_t8_t3_in += MAS_in[0]

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	S += t5_t8_t3_mem0 >= 54
	t5_t8_t3_mem0 += MAS_MEM[0]

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	S += t5_t8_t3_mem1 >= 54
	t5_t8_t3_mem1 += MAS_MEM[1]

	t5_t2_t3_in = S.Task('t5_t2_t3_in', length=1, delay_cost=1)
	S += t5_t2_t3_in >= 55
	t5_t2_t3_in += MAS_in[0]

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	S += t5_t2_t3_mem0 >= 55
	t5_t2_t3_mem0 += MAS_MEM[0]

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	S += t5_t2_t3_mem1 >= 55
	t5_t2_t3_mem1 += MAS_MEM[1]

	t5_t8_t3 = S.Task('t5_t8_t3', length=2, delay_cost=1)
	S += t5_t8_t3 >= 55
	t5_t8_t3 += MAS[0]

	t5_t0_t3_in = S.Task('t5_t0_t3_in', length=1, delay_cost=1)
	S += t5_t0_t3_in >= 56
	t5_t0_t3_in += MAS_in[0]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 56
	t5_t0_t3_mem0 += MAS_MEM[0]

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 56
	t5_t0_t3_mem1 += MAS_MEM[1]

	t5_t2_t3 = S.Task('t5_t2_t3', length=2, delay_cost=1)
	S += t5_t2_t3 >= 56
	t5_t2_t3 += MAS[0]

	t5_t0_t3 = S.Task('t5_t0_t3', length=2, delay_cost=1)
	S += t5_t0_t3 >= 57
	t5_t0_t3 += MAS[0]

	t5_t2_t2_in = S.Task('t5_t2_t2_in', length=1, delay_cost=1)
	S += t5_t2_t2_in >= 57
	t5_t2_t2_in += MAS_in[0]

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_t2_mem0 >= 57
	t5_t2_t2_mem0 += MAS_MEM[0]

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_t2_mem1 >= 57
	t5_t2_t2_mem1 += MAS_MEM[1]

	t5_t1_t2_in = S.Task('t5_t1_t2_in', length=1, delay_cost=1)
	S += t5_t1_t2_in >= 58
	t5_t1_t2_in += MAS_in[0]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 58
	t5_t1_t2_mem0 += MAS_MEM[0]

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 58
	t5_t1_t2_mem1 += MAS_MEM[1]

	t5_t2_t2 = S.Task('t5_t2_t2', length=2, delay_cost=1)
	S += t5_t2_t2 >= 58
	t5_t2_t2 += MAS[0]

	t5_t1_t2 = S.Task('t5_t1_t2', length=2, delay_cost=1)
	S += t5_t1_t2 >= 59
	t5_t1_t2 += MAS[0]

	t5_t40_in = S.Task('t5_t40_in', length=1, delay_cost=1)
	S += t5_t40_in >= 59
	t5_t40_in += MAS_in[0]

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	S += t5_t40_mem0 >= 59
	t5_t40_mem0 += MAIN_MEM_r[0]

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	S += t5_t40_mem1 >= 59
	t5_t40_mem1 += MAS_MEM[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 60
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 60
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 60
	t10_mem1 += MM_MEM[1]

	t5_t40 = S.Task('t5_t40', length=2, delay_cost=1)
	S += t5_t40 >= 60
	t5_t40 += MAS[0]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 61
	t0_t5_in += MAS_in[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 61
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 61
	t0_t5_mem1 += MM_MEM[1]

	t10 = S.Task('t10', length=2, delay_cost=1)
	S += t10 >= 61
	t10 += MAS[0]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 62
	t00_in += MAS_in[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 62
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 62
	t00_mem1 += MM_MEM[1]

	t0_t5 = S.Task('t0_t5', length=2, delay_cost=1)
	S += t0_t5 >= 62
	t0_t5 += MAS[0]

	t00 = S.Task('t00', length=2, delay_cost=1)
	S += t00 >= 63
	t00 += MAS[0]


	# new tasks
	t11 = S.Task('t11', length=2, delay_cost=1)
	t11 += alt(MAS)
	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	t11_in += alt(MAS_in)
	S += t11_in*MAS_in[0]<=t11*MAS[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += MM_MEM[0]
	S += 28 < t11_mem0
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += MAS_MEM[1]
	S += 46 < t11_mem1
	S += t11_mem1 <= t11

	t21 = S.Task('t21', length=2, delay_cost=1)
	t21 += alt(MAS)
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	t21_in += alt(MAS_in)
	S += t21_in*MAS_in[0]<=t21*MAS[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MM_MEM[0]
	S += 34 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAS_MEM[1]
	S += 51 < t21_mem1
	S += t21_mem1 <= t21

	t01 = S.Task('t01', length=2, delay_cost=1)
	t01 += alt(MAS)
	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	t01_in += alt(MAS_in)
	S += t01_in*MAS_in[0]<=t01*MAS[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MM_MEM[0]
	S += 38 < t01_mem0
	S += t01_mem0 <= t01

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	t01_mem1 += MAS_MEM[1]
	S += 63 < t01_mem1
	S += t01_mem1 <= t01

	t4_t01 = S.Task('t4_t01', length=2, delay_cost=1)
	t4_t01 += alt(MAS)
	t4_t01_in = S.Task('t4_t01_in', length=1, delay_cost=1)
	t4_t01_in += alt(MAS_in)
	S += t4_t01_in*MAS_in[0]<=t4_t01*MAS[0]

	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	t4_t01_mem0 += MM_MEM[0]
	S += 21 < t4_t01_mem0
	S += t4_t01_mem0 <= t4_t01

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	t4_t01_mem1 += MAS_MEM[1]
	S += 24 < t4_t01_mem1
	S += t4_t01_mem1 <= t4_t01

	t4_t11 = S.Task('t4_t11', length=2, delay_cost=1)
	t4_t11 += alt(MAS)
	t4_t11_in = S.Task('t4_t11_in', length=1, delay_cost=1)
	t4_t11_in += alt(MAS_in)
	S += t4_t11_in*MAS_in[0]<=t4_t11*MAS[0]

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	t4_t11_mem0 += MM_MEM[0]
	S += 35 < t4_t11_mem0
	S += t4_t11_mem0 <= t4_t11

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	t4_t11_mem1 += MAS_MEM[1]
	S += 47 < t4_t11_mem1
	S += t4_t11_mem1 <= t4_t11

	t4_t21 = S.Task('t4_t21', length=2, delay_cost=1)
	t4_t21 += alt(MAS)
	t4_t21_in = S.Task('t4_t21_in', length=1, delay_cost=1)
	t4_t21_in += alt(MAS_in)
	S += t4_t21_in*MAS_in[0]<=t4_t21*MAS[0]

	t4_t21_mem0 = S.Task('t4_t21_mem0', length=1, delay_cost=1)
	t4_t21_mem0 += MM_MEM[0]
	S += 32 < t4_t21_mem0
	S += t4_t21_mem0 <= t4_t21

	t4_t21_mem1 = S.Task('t4_t21_mem1', length=1, delay_cost=1)
	t4_t21_mem1 += MAS_MEM[1]
	S += 44 < t4_t21_mem1
	S += t4_t21_mem1 <= t4_t21

	t4_t6_t4 = S.Task('t4_t6_t4', length=8, delay_cost=1)
	t4_t6_t4 += alt(MM)
	t4_t6_t4_in = S.Task('t4_t6_t4_in', length=1, delay_cost=1)
	t4_t6_t4_in += alt(MM_in)
	S += t4_t6_t4_in*MM_in[0]<=t4_t6_t4*MM[0]
	t4_t6_t4_mem0 = S.Task('t4_t6_t4_mem0', length=1, delay_cost=1)
	t4_t6_t4_mem0 += MAS_MEM[0]
	S += 20 < t4_t6_t4_mem0
	S += t4_t6_t4_mem0 <= t4_t6_t4

	t4_t6_t4_mem1 = S.Task('t4_t6_t4_mem1', length=1, delay_cost=1)
	t4_t6_t4_mem1 += MAS_MEM[1]
	S += 31 < t4_t6_t4_mem1
	S += t4_t6_t4_mem1 <= t4_t6_t4

	t4_t60 = S.Task('t4_t60', length=2, delay_cost=1)
	t4_t60 += alt(MAS)
	t4_t60_in = S.Task('t4_t60_in', length=1, delay_cost=1)
	t4_t60_in += alt(MAS_in)
	S += t4_t60_in*MAS_in[0]<=t4_t60*MAS[0]

	t4_t60_mem0 = S.Task('t4_t60_mem0', length=1, delay_cost=1)
	t4_t60_mem0 += MM_MEM[0]
	S += 23 < t4_t60_mem0
	S += t4_t60_mem0 <= t4_t60

	t4_t60_mem1 = S.Task('t4_t60_mem1', length=1, delay_cost=1)
	t4_t60_mem1 += MM_MEM[1]
	S += 31 < t4_t60_mem1
	S += t4_t60_mem1 <= t4_t60

	t4_t6_t5 = S.Task('t4_t6_t5', length=2, delay_cost=1)
	t4_t6_t5 += alt(MAS)
	t4_t6_t5_in = S.Task('t4_t6_t5_in', length=1, delay_cost=1)
	t4_t6_t5_in += alt(MAS_in)
	S += t4_t6_t5_in*MAS_in[0]<=t4_t6_t5*MAS[0]

	t4_t6_t5_mem0 = S.Task('t4_t6_t5_mem0', length=1, delay_cost=1)
	t4_t6_t5_mem0 += MM_MEM[0]
	S += 23 < t4_t6_t5_mem0
	S += t4_t6_t5_mem0 <= t4_t6_t5

	t4_t6_t5_mem1 = S.Task('t4_t6_t5_mem1', length=1, delay_cost=1)
	t4_t6_t5_mem1 += MM_MEM[1]
	S += 31 < t4_t6_t5_mem1
	S += t4_t6_t5_mem1 <= t4_t6_t5

	t4_t70 = S.Task('t4_t70', length=2, delay_cost=1)
	t4_t70 += alt(MAS)
	t4_t70_in = S.Task('t4_t70_in', length=1, delay_cost=1)
	t4_t70_in += alt(MAS_in)
	S += t4_t70_in*MAS_in[0]<=t4_t70*MAS[0]

	t4_t70_mem0 = S.Task('t4_t70_mem0', length=1, delay_cost=1)
	t4_t70_mem0 += MAS_MEM[0]
	S += 27 < t4_t70_mem0
	S += t4_t70_mem0 <= t4_t70

	t4_t70_mem1 = S.Task('t4_t70_mem1', length=1, delay_cost=1)
	t4_t70_mem1 += MAS_MEM[1]
	S += 50 < t4_t70_mem1
	S += t4_t70_mem1 <= t4_t70

	t4_t81 = S.Task('t4_t81', length=2, delay_cost=1)
	t4_t81 += alt(MAS)
	t4_t81_in = S.Task('t4_t81_in', length=1, delay_cost=1)
	t4_t81_in += alt(MAS_in)
	S += t4_t81_in*MAS_in[0]<=t4_t81*MAS[0]

	t4_t81_mem0 = S.Task('t4_t81_mem0', length=1, delay_cost=1)
	t4_t81_mem0 += MM_MEM[0]
	S += 52 < t4_t81_mem0
	S += t4_t81_mem0 <= t4_t81

	t4_t81_mem1 = S.Task('t4_t81_mem1', length=1, delay_cost=1)
	t4_t81_mem1 += MAS_MEM[1]
	S += 49 < t4_t81_mem1
	S += t4_t81_mem1 <= t4_t81

	t420 = S.Task('t420', length=2, delay_cost=1)
	t420 += alt(MAS)
	t420_in = S.Task('t420_in', length=1, delay_cost=1)
	t420_in += alt(MAS_in)
	S += t420_in*MAS_in[0]<=t420*MAS[0]

	t420_mem0 = S.Task('t420_mem0', length=1, delay_cost=1)
	t420_mem0 += MAS_MEM[0]
	S += 30 < t420_mem0
	S += t420_mem0 <= t420

	t420_mem1 = S.Task('t420_mem1', length=1, delay_cost=1)
	t420_mem1 += MAS_MEM[1]
	S += 50 < t420_mem1
	S += t420_mem1 <= t420

	t5_t0_t4 = S.Task('t5_t0_t4', length=8, delay_cost=1)
	t5_t0_t4 += alt(MM)
	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	t5_t0_t4_in += alt(MM_in)
	S += t5_t0_t4_in*MM_in[0]<=t5_t0_t4*MM[0]
	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	t5_t0_t4_mem0 += MAS_MEM[0]
	S += 33 < t5_t0_t4_mem0
	S += t5_t0_t4_mem0 <= t5_t0_t4

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	t5_t0_t4_mem1 += MAS_MEM[1]
	S += 58 < t5_t0_t4_mem1
	S += t5_t0_t4_mem1 <= t5_t0_t4

	t5_t00 = S.Task('t5_t00', length=2, delay_cost=1)
	t5_t00 += alt(MAS)
	t5_t00_in = S.Task('t5_t00_in', length=1, delay_cost=1)
	t5_t00_in += alt(MAS_in)
	S += t5_t00_in*MAS_in[0]<=t5_t00*MAS[0]

	t5_t00_mem0 = S.Task('t5_t00_mem0', length=1, delay_cost=1)
	t5_t00_mem0 += MM_MEM[0]
	S += 56 < t5_t00_mem0
	S += t5_t00_mem0 <= t5_t00

	t5_t00_mem1 = S.Task('t5_t00_mem1', length=1, delay_cost=1)
	t5_t00_mem1 += MM_MEM[1]
	S += 51 < t5_t00_mem1
	S += t5_t00_mem1 <= t5_t00

	t5_t0_t5 = S.Task('t5_t0_t5', length=2, delay_cost=1)
	t5_t0_t5 += alt(MAS)
	t5_t0_t5_in = S.Task('t5_t0_t5_in', length=1, delay_cost=1)
	t5_t0_t5_in += alt(MAS_in)
	S += t5_t0_t5_in*MAS_in[0]<=t5_t0_t5*MAS[0]

	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	t5_t0_t5_mem0 += MM_MEM[0]
	S += 56 < t5_t0_t5_mem0
	S += t5_t0_t5_mem0 <= t5_t0_t5

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	t5_t0_t5_mem1 += MM_MEM[1]
	S += 51 < t5_t0_t5_mem1
	S += t5_t0_t5_mem1 <= t5_t0_t5

	t5_t1_t4 = S.Task('t5_t1_t4', length=8, delay_cost=1)
	t5_t1_t4 += alt(MM)
	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	t5_t1_t4_in += alt(MM_in)
	S += t5_t1_t4_in*MM_in[0]<=t5_t1_t4*MM[0]
	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	t5_t1_t4_mem0 += MAS_MEM[0]
	S += 60 < t5_t1_t4_mem0
	S += t5_t1_t4_mem0 <= t5_t1_t4

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	t5_t1_t4_mem1 += MAS_MEM[1]
	S += 52 < t5_t1_t4_mem1
	S += t5_t1_t4_mem1 <= t5_t1_t4

	t5_t10 = S.Task('t5_t10', length=2, delay_cost=1)
	t5_t10 += alt(MAS)
	t5_t10_in = S.Task('t5_t10_in', length=1, delay_cost=1)
	t5_t10_in += alt(MAS_in)
	S += t5_t10_in*MAS_in[0]<=t5_t10*MAS[0]

	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	t5_t10_mem0 += MM_MEM[0]
	S += 53 < t5_t10_mem0
	S += t5_t10_mem0 <= t5_t10

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	t5_t10_mem1 += MM_MEM[1]
	S += 46 < t5_t10_mem1
	S += t5_t10_mem1 <= t5_t10

	t5_t1_t5 = S.Task('t5_t1_t5', length=2, delay_cost=1)
	t5_t1_t5 += alt(MAS)
	t5_t1_t5_in = S.Task('t5_t1_t5_in', length=1, delay_cost=1)
	t5_t1_t5_in += alt(MAS_in)
	S += t5_t1_t5_in*MAS_in[0]<=t5_t1_t5*MAS[0]

	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	t5_t1_t5_mem0 += MM_MEM[0]
	S += 53 < t5_t1_t5_mem0
	S += t5_t1_t5_mem0 <= t5_t1_t5

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	t5_t1_t5_mem1 += MM_MEM[1]
	S += 46 < t5_t1_t5_mem1
	S += t5_t1_t5_mem1 <= t5_t1_t5

	t5_t2_t4 = S.Task('t5_t2_t4', length=8, delay_cost=1)
	t5_t2_t4 += alt(MM)
	t5_t2_t4_in = S.Task('t5_t2_t4_in', length=1, delay_cost=1)
	t5_t2_t4_in += alt(MM_in)
	S += t5_t2_t4_in*MM_in[0]<=t5_t2_t4*MM[0]
	t5_t2_t4_mem0 = S.Task('t5_t2_t4_mem0', length=1, delay_cost=1)
	t5_t2_t4_mem0 += MAS_MEM[0]
	S += 59 < t5_t2_t4_mem0
	S += t5_t2_t4_mem0 <= t5_t2_t4

	t5_t2_t4_mem1 = S.Task('t5_t2_t4_mem1', length=1, delay_cost=1)
	t5_t2_t4_mem1 += MAS_MEM[1]
	S += 57 < t5_t2_t4_mem1
	S += t5_t2_t4_mem1 <= t5_t2_t4

	t5_t20 = S.Task('t5_t20', length=2, delay_cost=1)
	t5_t20 += alt(MAS)
	t5_t20_in = S.Task('t5_t20_in', length=1, delay_cost=1)
	t5_t20_in += alt(MAS_in)
	S += t5_t20_in*MAS_in[0]<=t5_t20*MAS[0]

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	t5_t20_mem0 += MM_MEM[0]
	S += 55 < t5_t20_mem0
	S += t5_t20_mem0 <= t5_t20

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	t5_t20_mem1 += MM_MEM[1]
	S += 44 < t5_t20_mem1
	S += t5_t20_mem1 <= t5_t20

	t5_t2_t5 = S.Task('t5_t2_t5', length=2, delay_cost=1)
	t5_t2_t5 += alt(MAS)
	t5_t2_t5_in = S.Task('t5_t2_t5_in', length=1, delay_cost=1)
	t5_t2_t5_in += alt(MAS_in)
	S += t5_t2_t5_in*MAS_in[0]<=t5_t2_t5*MAS[0]

	t5_t2_t5_mem0 = S.Task('t5_t2_t5_mem0', length=1, delay_cost=1)
	t5_t2_t5_mem0 += MM_MEM[0]
	S += 55 < t5_t2_t5_mem0
	S += t5_t2_t5_mem0 <= t5_t2_t5

	t5_t2_t5_mem1 = S.Task('t5_t2_t5_mem1', length=1, delay_cost=1)
	t5_t2_t5_mem1 += MM_MEM[1]
	S += 44 < t5_t2_t5_mem1
	S += t5_t2_t5_mem1 <= t5_t2_t5

	t5_t6_t0 = S.Task('t5_t6_t0', length=8, delay_cost=1)
	t5_t6_t0 += alt(MM)
	t5_t6_t0_in = S.Task('t5_t6_t0_in', length=1, delay_cost=1)
	t5_t6_t0_in += alt(MM_in)
	S += t5_t6_t0_in*MM_in[0]<=t5_t6_t0*MM[0]
	t5_t6_t0_mem0 = S.Task('t5_t6_t0_mem0', length=1, delay_cost=1)
	t5_t6_t0_mem0 += MAS_MEM[0]
	S += 61 < t5_t6_t0_mem0
	S += t5_t6_t0_mem0 <= t5_t6_t0

	t5_t6_t0_mem1 = S.Task('t5_t6_t0_mem1', length=1, delay_cost=1)
	t5_t6_t0_mem1 += MAS_MEM[1]
	S += 53 < t5_t6_t0_mem1
	S += t5_t6_t0_mem1 <= t5_t6_t0

	t5_t6_t1 = S.Task('t5_t6_t1', length=8, delay_cost=1)
	t5_t6_t1 += alt(MM)
	t5_t6_t1_in = S.Task('t5_t6_t1_in', length=1, delay_cost=1)
	t5_t6_t1_in += alt(MM_in)
	S += t5_t6_t1_in*MM_in[0]<=t5_t6_t1*MM[0]
	t5_t6_t1_mem0 = S.Task('t5_t6_t1_mem0', length=1, delay_cost=1)
	t5_t6_t1_mem0 += MAS_MEM[0]
	S += 54 < t5_t6_t1_mem0
	S += t5_t6_t1_mem0 <= t5_t6_t1

	t5_t6_t1_mem1 = S.Task('t5_t6_t1_mem1', length=1, delay_cost=1)
	t5_t6_t1_mem1 += MAS_MEM[1]
	S += 55 < t5_t6_t1_mem1
	S += t5_t6_t1_mem1 <= t5_t6_t1

	t5_t6_t2 = S.Task('t5_t6_t2', length=2, delay_cost=1)
	t5_t6_t2 += alt(MAS)
	t5_t6_t2_in = S.Task('t5_t6_t2_in', length=1, delay_cost=1)
	t5_t6_t2_in += alt(MAS_in)
	S += t5_t6_t2_in*MAS_in[0]<=t5_t6_t2*MAS[0]

	t5_t6_t2_mem0 = S.Task('t5_t6_t2_mem0', length=1, delay_cost=1)
	t5_t6_t2_mem0 += MAS_MEM[0]
	S += 61 < t5_t6_t2_mem0
	S += t5_t6_t2_mem0 <= t5_t6_t2

	t5_t6_t2_mem1 = S.Task('t5_t6_t2_mem1', length=1, delay_cost=1)
	t5_t6_t2_mem1 += MAS_MEM[1]
	S += 54 < t5_t6_t2_mem1
	S += t5_t6_t2_mem1 <= t5_t6_t2

	t5_t6_t3 = S.Task('t5_t6_t3', length=2, delay_cost=1)
	t5_t6_t3 += alt(MAS)
	t5_t6_t3_in = S.Task('t5_t6_t3_in', length=1, delay_cost=1)
	t5_t6_t3_in += alt(MAS_in)
	S += t5_t6_t3_in*MAS_in[0]<=t5_t6_t3*MAS[0]

	t5_t6_t3_mem0 = S.Task('t5_t6_t3_mem0', length=1, delay_cost=1)
	t5_t6_t3_mem0 += MAS_MEM[0]
	S += 53 < t5_t6_t3_mem0
	S += t5_t6_t3_mem0 <= t5_t6_t3

	t5_t6_t3_mem1 = S.Task('t5_t6_t3_mem1', length=1, delay_cost=1)
	t5_t6_t3_mem1 += MAS_MEM[1]
	S += 55 < t5_t6_t3_mem1
	S += t5_t6_t3_mem1 <= t5_t6_t3

	t5_t8_t4 = S.Task('t5_t8_t4', length=8, delay_cost=1)
	t5_t8_t4 += alt(MM)
	t5_t8_t4_in = S.Task('t5_t8_t4_in', length=1, delay_cost=1)
	t5_t8_t4_in += alt(MM_in)
	S += t5_t8_t4_in*MM_in[0]<=t5_t8_t4*MM[0]
	t5_t8_t4_mem0 = S.Task('t5_t8_t4_mem0', length=1, delay_cost=1)
	t5_t8_t4_mem0 += MAS_MEM[0]
	S += 32 < t5_t8_t4_mem0
	S += t5_t8_t4_mem0 <= t5_t8_t4

	t5_t8_t4_mem1 = S.Task('t5_t8_t4_mem1', length=1, delay_cost=1)
	t5_t8_t4_mem1 += MAS_MEM[1]
	S += 56 < t5_t8_t4_mem1
	S += t5_t8_t4_mem1 <= t5_t8_t4

	t5_t80 = S.Task('t5_t80', length=2, delay_cost=1)
	t5_t80 += alt(MAS)
	t5_t80_in = S.Task('t5_t80_in', length=1, delay_cost=1)
	t5_t80_in += alt(MAS_in)
	S += t5_t80_in*MAS_in[0]<=t5_t80*MAS[0]

	t5_t80_mem0 = S.Task('t5_t80_mem0', length=1, delay_cost=1)
	t5_t80_mem0 += MM_MEM[0]
	S += 54 < t5_t80_mem0
	S += t5_t80_mem0 <= t5_t80

	t5_t80_mem1 = S.Task('t5_t80_mem1', length=1, delay_cost=1)
	t5_t80_mem1 += MM_MEM[1]
	S += 50 < t5_t80_mem1
	S += t5_t80_mem1 <= t5_t80

	t5_t8_t5 = S.Task('t5_t8_t5', length=2, delay_cost=1)
	t5_t8_t5 += alt(MAS)
	t5_t8_t5_in = S.Task('t5_t8_t5_in', length=1, delay_cost=1)
	t5_t8_t5_in += alt(MAS_in)
	S += t5_t8_t5_in*MAS_in[0]<=t5_t8_t5*MAS[0]

	t5_t8_t5_mem0 = S.Task('t5_t8_t5_mem0', length=1, delay_cost=1)
	t5_t8_t5_mem0 += MM_MEM[0]
	S += 54 < t5_t8_t5_mem0
	S += t5_t8_t5_mem0 <= t5_t8_t5

	t5_t8_t5_mem1 = S.Task('t5_t8_t5_mem1', length=1, delay_cost=1)
	t5_t8_t5_mem1 += MM_MEM[1]
	S += 50 < t5_t8_t5_mem1
	S += t5_t8_t5_mem1 <= t5_t8_t5

	t30 = S.Task('t30', length=2, delay_cost=1)
	t30 += alt(MAS)
	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	t30_in += alt(MAS_in)
	S += t30_in*MAS_in[0]<=t30*MAS[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MAS_MEM[0]
	S += 64 < t30_mem0
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t30_mem1*MAS_MEM[1]
	S += t30_mem1 <= t30

	t31 = S.Task('t31', length=2, delay_cost=1)
	t31 += alt(MAS)
	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	t31_in += alt(MAS_in)
	S += t31_in*MAS_in[0]<=t31*MAS[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t31_mem0*MAS_MEM[0]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += MAS_MEM[1]
	S += 64 < t31_mem1
	S += t31_mem1 <= t31

	t4_t100 = S.Task('t4_t100', length=2, delay_cost=1)
	t4_t100 += alt(MAS)
	t4_t100_in = S.Task('t4_t100_in', length=1, delay_cost=1)
	t4_t100_in += alt(MAS_in)
	S += t4_t100_in*MAS_in[0]<=t4_t100*MAS[0]

	t4_t100_mem0 = S.Task('t4_t100_mem0', length=1, delay_cost=1)
	t4_t100_mem0 += MAS_MEM[0]
	S += 48 < t4_t100_mem0
	S += t4_t100_mem0 <= t4_t100

	t4_t100_mem1 = S.Task('t4_t100_mem1', length=1, delay_cost=1)
	t4_t100_mem1 += alt(MAS_MEM)
	S += (t4_t21*MAS[0])-1 < t4_t100_mem1*MAS_MEM[1]
	S += t4_t100_mem1 <= t4_t100

	t4_t101 = S.Task('t4_t101', length=2, delay_cost=1)
	t4_t101 += alt(MAS)
	t4_t101_in = S.Task('t4_t101_in', length=1, delay_cost=1)
	t4_t101_in += alt(MAS_in)
	S += t4_t101_in*MAS_in[0]<=t4_t101*MAS[0]

	t4_t101_mem0 = S.Task('t4_t101_mem0', length=1, delay_cost=1)
	t4_t101_mem0 += alt(MAS_MEM)
	S += (t4_t21*MAS[0])-1 < t4_t101_mem0*MAS_MEM[0]
	S += t4_t101_mem0 <= t4_t101

	t4_t101_mem1 = S.Task('t4_t101_mem1', length=1, delay_cost=1)
	t4_t101_mem1 += MAS_MEM[1]
	S += 48 < t4_t101_mem1
	S += t4_t101_mem1 <= t4_t101

	t4_t61 = S.Task('t4_t61', length=2, delay_cost=1)
	t4_t61 += alt(MAS)
	t4_t61_in = S.Task('t4_t61_in', length=1, delay_cost=1)
	t4_t61_in += alt(MAS_in)
	S += t4_t61_in*MAS_in[0]<=t4_t61*MAS[0]

	t4_t61_mem0 = S.Task('t4_t61_mem0', length=1, delay_cost=1)
	t4_t61_mem0 += alt(MM_MEM)
	S += (t4_t6_t4*MM[0])-1 < t4_t61_mem0*MM_MEM[0]
	S += t4_t61_mem0 <= t4_t61

	t4_t61_mem1 = S.Task('t4_t61_mem1', length=1, delay_cost=1)
	t4_t61_mem1 += alt(MAS_MEM)
	S += (t4_t6_t5*MAS[0])-1 < t4_t61_mem1*MAS_MEM[1]
	S += t4_t61_mem1 <= t4_t61

	t4_t71 = S.Task('t4_t71', length=2, delay_cost=1)
	t4_t71 += alt(MAS)
	t4_t71_in = S.Task('t4_t71_in', length=1, delay_cost=1)
	t4_t71_in += alt(MAS_in)
	S += t4_t71_in*MAS_in[0]<=t4_t71*MAS[0]

	t4_t71_mem0 = S.Task('t4_t71_mem0', length=1, delay_cost=1)
	t4_t71_mem0 += alt(MAS_MEM)
	S += (t4_t01*MAS[0])-1 < t4_t71_mem0*MAS_MEM[0]
	S += t4_t71_mem0 <= t4_t71

	t4_t71_mem1 = S.Task('t4_t71_mem1', length=1, delay_cost=1)
	t4_t71_mem1 += alt(MAS_MEM)
	S += (t4_t11*MAS[0])-1 < t4_t71_mem1*MAS_MEM[1]
	S += t4_t71_mem1 <= t4_t71

	t410 = S.Task('t410', length=2, delay_cost=1)
	t410 += alt(MAS)
	t410_in = S.Task('t410_in', length=1, delay_cost=1)
	t410_in += alt(MAS_in)
	S += t410_in*MAS_in[0]<=t410*MAS[0]

	t410_mem0 = S.Task('t410_mem0', length=1, delay_cost=1)
	t410_mem0 += alt(MAS_MEM)
	S += (t4_t60*MAS[0])-1 < t410_mem0*MAS_MEM[0]
	S += t410_mem0 <= t410

	t410_mem1 = S.Task('t410_mem1', length=1, delay_cost=1)
	t410_mem1 += alt(MAS_MEM)
	S += (t4_t70*MAS[0])-1 < t410_mem1*MAS_MEM[1]
	S += t410_mem1 <= t410

	t421 = S.Task('t421', length=2, delay_cost=1)
	t421 += alt(MAS)
	t421_in = S.Task('t421_in', length=1, delay_cost=1)
	t421_in += alt(MAS_in)
	S += t421_in*MAS_in[0]<=t421*MAS[0]

	t421_mem0 = S.Task('t421_mem0', length=1, delay_cost=1)
	t421_mem0 += alt(MAS_MEM)
	S += (t4_t81*MAS[0])-1 < t421_mem0*MAS_MEM[0]
	S += t421_mem0 <= t421

	t421_mem1 = S.Task('t421_mem1', length=1, delay_cost=1)
	t421_mem1 += alt(MAS_MEM)
	S += (t4_t11*MAS[0])-1 < t421_mem1*MAS_MEM[1]
	S += t421_mem1 <= t421

	t5_t01 = S.Task('t5_t01', length=2, delay_cost=1)
	t5_t01 += alt(MAS)
	t5_t01_in = S.Task('t5_t01_in', length=1, delay_cost=1)
	t5_t01_in += alt(MAS_in)
	S += t5_t01_in*MAS_in[0]<=t5_t01*MAS[0]

	t5_t01_mem0 = S.Task('t5_t01_mem0', length=1, delay_cost=1)
	t5_t01_mem0 += alt(MM_MEM)
	S += (t5_t0_t4*MM[0])-1 < t5_t01_mem0*MM_MEM[0]
	S += t5_t01_mem0 <= t5_t01

	t5_t01_mem1 = S.Task('t5_t01_mem1', length=1, delay_cost=1)
	t5_t01_mem1 += alt(MAS_MEM)
	S += (t5_t0_t5*MAS[0])-1 < t5_t01_mem1*MAS_MEM[1]
	S += t5_t01_mem1 <= t5_t01

	t5_t11 = S.Task('t5_t11', length=2, delay_cost=1)
	t5_t11 += alt(MAS)
	t5_t11_in = S.Task('t5_t11_in', length=1, delay_cost=1)
	t5_t11_in += alt(MAS_in)
	S += t5_t11_in*MAS_in[0]<=t5_t11*MAS[0]

	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	t5_t11_mem0 += alt(MM_MEM)
	S += (t5_t1_t4*MM[0])-1 < t5_t11_mem0*MM_MEM[0]
	S += t5_t11_mem0 <= t5_t11

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	t5_t11_mem1 += alt(MAS_MEM)
	S += (t5_t1_t5*MAS[0])-1 < t5_t11_mem1*MAS_MEM[1]
	S += t5_t11_mem1 <= t5_t11

	t5_t21 = S.Task('t5_t21', length=2, delay_cost=1)
	t5_t21 += alt(MAS)
	t5_t21_in = S.Task('t5_t21_in', length=1, delay_cost=1)
	t5_t21_in += alt(MAS_in)
	S += t5_t21_in*MAS_in[0]<=t5_t21*MAS[0]

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	t5_t21_mem0 += alt(MM_MEM)
	S += (t5_t2_t4*MM[0])-1 < t5_t21_mem0*MM_MEM[0]
	S += t5_t21_mem0 <= t5_t21

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	t5_t21_mem1 += alt(MAS_MEM)
	S += (t5_t2_t5*MAS[0])-1 < t5_t21_mem1*MAS_MEM[1]
	S += t5_t21_mem1 <= t5_t21

	t5_t6_t4 = S.Task('t5_t6_t4', length=8, delay_cost=1)
	t5_t6_t4 += alt(MM)
	t5_t6_t4_in = S.Task('t5_t6_t4_in', length=1, delay_cost=1)
	t5_t6_t4_in += alt(MM_in)
	S += t5_t6_t4_in*MM_in[0]<=t5_t6_t4*MM[0]
	t5_t6_t4_mem0 = S.Task('t5_t6_t4_mem0', length=1, delay_cost=1)
	t5_t6_t4_mem0 += alt(MAS_MEM)
	S += (t5_t6_t2*MAS[0])-1 < t5_t6_t4_mem0*MAS_MEM[0]
	S += t5_t6_t4_mem0 <= t5_t6_t4

	t5_t6_t4_mem1 = S.Task('t5_t6_t4_mem1', length=1, delay_cost=1)
	t5_t6_t4_mem1 += alt(MAS_MEM)
	S += (t5_t6_t3*MAS[0])-1 < t5_t6_t4_mem1*MAS_MEM[1]
	S += t5_t6_t4_mem1 <= t5_t6_t4

	t5_t60 = S.Task('t5_t60', length=2, delay_cost=1)
	t5_t60 += alt(MAS)
	t5_t60_in = S.Task('t5_t60_in', length=1, delay_cost=1)
	t5_t60_in += alt(MAS_in)
	S += t5_t60_in*MAS_in[0]<=t5_t60*MAS[0]

	t5_t60_mem0 = S.Task('t5_t60_mem0', length=1, delay_cost=1)
	t5_t60_mem0 += alt(MM_MEM)
	S += (t5_t6_t0*MM[0])-1 < t5_t60_mem0*MM_MEM[0]
	S += t5_t60_mem0 <= t5_t60

	t5_t60_mem1 = S.Task('t5_t60_mem1', length=1, delay_cost=1)
	t5_t60_mem1 += alt(MM_MEM)
	S += (t5_t6_t1*MM[0])-1 < t5_t60_mem1*MM_MEM[1]
	S += t5_t60_mem1 <= t5_t60

	t5_t6_t5 = S.Task('t5_t6_t5', length=2, delay_cost=1)
	t5_t6_t5 += alt(MAS)
	t5_t6_t5_in = S.Task('t5_t6_t5_in', length=1, delay_cost=1)
	t5_t6_t5_in += alt(MAS_in)
	S += t5_t6_t5_in*MAS_in[0]<=t5_t6_t5*MAS[0]

	t5_t6_t5_mem0 = S.Task('t5_t6_t5_mem0', length=1, delay_cost=1)
	t5_t6_t5_mem0 += alt(MM_MEM)
	S += (t5_t6_t0*MM[0])-1 < t5_t6_t5_mem0*MM_MEM[0]
	S += t5_t6_t5_mem0 <= t5_t6_t5

	t5_t6_t5_mem1 = S.Task('t5_t6_t5_mem1', length=1, delay_cost=1)
	t5_t6_t5_mem1 += alt(MM_MEM)
	S += (t5_t6_t1*MM[0])-1 < t5_t6_t5_mem1*MM_MEM[1]
	S += t5_t6_t5_mem1 <= t5_t6_t5

	t5_t70 = S.Task('t5_t70', length=2, delay_cost=1)
	t5_t70 += alt(MAS)
	t5_t70_in = S.Task('t5_t70_in', length=1, delay_cost=1)
	t5_t70_in += alt(MAS_in)
	S += t5_t70_in*MAS_in[0]<=t5_t70*MAS[0]

	t5_t70_mem0 = S.Task('t5_t70_mem0', length=1, delay_cost=1)
	t5_t70_mem0 += alt(MAS_MEM)
	S += (t5_t00*MAS[0])-1 < t5_t70_mem0*MAS_MEM[0]
	S += t5_t70_mem0 <= t5_t70

	t5_t70_mem1 = S.Task('t5_t70_mem1', length=1, delay_cost=1)
	t5_t70_mem1 += alt(MAS_MEM)
	S += (t5_t10*MAS[0])-1 < t5_t70_mem1*MAS_MEM[1]
	S += t5_t70_mem1 <= t5_t70

	t5_t81 = S.Task('t5_t81', length=2, delay_cost=1)
	t5_t81 += alt(MAS)
	t5_t81_in = S.Task('t5_t81_in', length=1, delay_cost=1)
	t5_t81_in += alt(MAS_in)
	S += t5_t81_in*MAS_in[0]<=t5_t81*MAS[0]

	t5_t81_mem0 = S.Task('t5_t81_mem0', length=1, delay_cost=1)
	t5_t81_mem0 += alt(MM_MEM)
	S += (t5_t8_t4*MM[0])-1 < t5_t81_mem0*MM_MEM[0]
	S += t5_t81_mem0 <= t5_t81

	t5_t81_mem1 = S.Task('t5_t81_mem1', length=1, delay_cost=1)
	t5_t81_mem1 += alt(MAS_MEM)
	S += (t5_t8_t5*MAS[0])-1 < t5_t81_mem1*MAS_MEM[1]
	S += t5_t81_mem1 <= t5_t81

	t520 = S.Task('t520', length=2, delay_cost=1)
	t520 += alt(MAS)
	t520_in = S.Task('t520_in', length=1, delay_cost=1)
	t520_in += alt(MAS_in)
	S += t520_in*MAS_in[0]<=t520*MAS[0]

	t520_mem0 = S.Task('t520_mem0', length=1, delay_cost=1)
	t520_mem0 += alt(MAS_MEM)
	S += (t5_t80*MAS[0])-1 < t520_mem0*MAS_MEM[0]
	S += t520_mem0 <= t520

	t520_mem1 = S.Task('t520_mem1', length=1, delay_cost=1)
	t520_mem1 += alt(MAS_MEM)
	S += (t5_t10*MAS[0])-1 < t520_mem1*MAS_MEM[1]
	S += t520_mem1 <= t520

	t160 = S.Task('t160', length=2, delay_cost=1)
	t160 += alt(MAS)
	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	t160_in += alt(MAS_in)
	S += t160_in*MAS_in[0]<=t160*MAS[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += MAS_MEM[0]
	S += 45 < t160_mem0
	S += t160_mem0 <= t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(MAS_MEM)
	S += (t420*MAS[0])-1 < t160_mem1*MAS_MEM[1]
	S += t160_mem1 <= t160

	t170 = S.Task('t170', length=2, delay_cost=1)
	t170 += alt(MAS)
	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	t170_in += alt(MAS_in)
	S += t170_in*MAS_in[0]<=t170*MAS[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += MAS_MEM[0]
	S += 45 < t170_mem0
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t170_mem1*MAS_MEM[1]
	S += t170_mem1 <= t170

	t171 = S.Task('t171', length=2, delay_cost=1)
	t171 += alt(MAS)
	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	t171_in += alt(MAS_in)
	S += t171_in*MAS_in[0]<=t171*MAS[0]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t171_mem0*MAS_MEM[0]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += MAS_MEM[1]
	S += 45 < t171_mem1
	S += t171_mem1 <= t171

	c110 = S.Task('c110', length=2, delay_cost=1)
	c110 += alt(MAS)
	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	c110_in += alt(MAS_in)
	S += c110_in*MAS_in[0]<=c110*MAS[0]

	S += 36<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[0]
	S += 62 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += alt(MAS_MEM)
	S += (t420*MAS[0])-1 < c110_mem1*MAS_MEM[1]
	S += c110_mem1 <= c110

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage2MAS1/SPARSE/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution

