from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 132
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 0
	t1_t0_mem0 += MAIN_MEM_r[0]

	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_in >= 0
	t4_t1_t1_in += MM_in[0]

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 0
	t4_t41_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 1
	t0_t3 += MAS[0]

	t1_t2 = S.Task('t1_t2', length=1, delay_cost=1)
	S += t1_t2 >= 1
	t1_t2 += MAS[4]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 1
	t4_t0_t2_mem0 += MAIN_MEM_r[0]

	t4_t1_t1 = S.Task('t4_t1_t1', length=8, delay_cost=1)
	S += t4_t1_t1 >= 1
	t4_t1_t1 += MM[0]

	t4_t1_t3 = S.Task('t4_t1_t3', length=1, delay_cost=1)
	S += t4_t1_t3 >= 1
	t4_t1_t3 += MAS[3]

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 1
	t4_t1_t3_mem1 += MAIN_MEM_r[1]

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	S += t4_t2_t0_in >= 1
	t4_t2_t0_in += MM_in[0]

	t4_t2_t3 = S.Task('t4_t2_t3', length=1, delay_cost=1)
	S += t4_t2_t3 >= 1
	t4_t2_t3 += MAS[2]

	t4_t40 = S.Task('t4_t40', length=1, delay_cost=1)
	S += t4_t40 >= 1
	t4_t40 += MAS[1]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 2
	t0_t2 += MAS[0]

	t4_t1_t2 = S.Task('t4_t1_t2', length=1, delay_cost=1)
	S += t4_t1_t2 >= 2
	t4_t1_t2 += MAS[2]

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t2_mem1 >= 2
	t4_t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t2_t0 = S.Task('t4_t2_t0', length=8, delay_cost=1)
	S += t4_t2_t0 >= 2
	t4_t2_t0 += MM[0]

	t4_t2_t2 = S.Task('t4_t2_t2', length=1, delay_cost=1)
	S += t4_t2_t2 >= 2
	t4_t2_t2 += MAS[4]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 2
	t4_t40_mem0 += MAIN_MEM_r[0]

	t4_t41 = S.Task('t4_t41', length=1, delay_cost=1)
	S += t4_t41 >= 2
	t4_t41 += MAS[1]

	t4_t50 = S.Task('t4_t50', length=1, delay_cost=1)
	S += t4_t50 >= 2
	t4_t50 += MAS[3]

	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	S += t4_t8_t0_in >= 2
	t4_t8_t0_in += MM_in[0]

	t1_t3 = S.Task('t1_t3', length=1, delay_cost=1)
	S += t1_t3 >= 3
	t1_t3 += MAS[4]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 3
	t2_t2 += MAS[1]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 3
	t2_t3 += MAS[2]

	t4_t0_t2 = S.Task('t4_t0_t2', length=1, delay_cost=1)
	S += t4_t0_t2 >= 3
	t4_t0_t2 += MAS[3]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 3
	t4_t0_t3_mem0 += MAIN_MEM_r[0]

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 3
	t4_t2_t1_in += MM_in[0]

	t4_t51 = S.Task('t4_t51', length=1, delay_cost=1)
	S += t4_t51 >= 3
	t4_t51 += MAS[0]

	t4_t8_t0 = S.Task('t4_t8_t0', length=8, delay_cost=1)
	S += t4_t8_t0 >= 3
	t4_t8_t0 += MM[0]

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	S += t4_t8_t0_mem1 >= 3
	t4_t8_t0_mem1 += MAIN_MEM_r[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 4
	t0_t1_in += MM_in[0]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 4
	t101 += MAS[4]

	t4_t0_t3 = S.Task('t4_t0_t3', length=1, delay_cost=1)
	S += t4_t0_t3 >= 4
	t4_t0_t3 += MAS[1]

	t4_t2_t1 = S.Task('t4_t2_t1', length=8, delay_cost=1)
	S += t4_t2_t1 >= 4
	t4_t2_t1 += MM[0]

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 4
	t4_t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 4
	t4_t2_t3_mem0 += MAIN_MEM_r[0]

	t5_t8_t2 = S.Task('t5_t8_t2', length=1, delay_cost=1)
	S += t5_t8_t2 >= 4
	t5_t8_t2 += MAS[0]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 4
	t71 += MAS[2]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 4
	t80 += MAS[3]

	t0_t1 = S.Task('t0_t1', length=8, delay_cost=1)
	S += t0_t1 >= 5
	t0_t1 += MM[0]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 5
	t100 += MAS[3]

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_in >= 5
	t4_t0_t0_in += MM_in[0]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 5
	t4_t1_t3_mem0 += MAIN_MEM_r[0]

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 5
	t4_t50_mem1 += MAIN_MEM_r[1]

	t4_t8_t2 = S.Task('t4_t8_t2', length=1, delay_cost=1)
	S += t4_t8_t2 >= 5
	t4_t8_t2 += MAS[1]

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	S += t5_t0_t2 >= 5
	t5_t0_t2 += MAS[0]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 5
	t70 += MAS[4]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 5
	t90 += MAS[2]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 6
	t1_t0_in += MM_in[0]

	t4_t0_t0 = S.Task('t4_t0_t0', length=8, delay_cost=1)
	S += t4_t0_t0 >= 6
	t4_t0_t0 += MM[0]

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_mem0 >= 6
	t4_t0_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_mem1 >= 6
	t4_t1_t0_mem1 += MAIN_MEM_r[1]

	t4_t8_t3 = S.Task('t4_t8_t3', length=1, delay_cost=1)
	S += t4_t8_t3 >= 6
	t4_t8_t3 += MAS[3]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 6
	t81 += MAS[1]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 6
	t91 += MAS[0]

	t1_t0 = S.Task('t1_t0', length=8, delay_cost=1)
	S += t1_t0 >= 7
	t1_t0 += MM[0]

	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_in >= 7
	t4_t1_t0_in += MM_in[0]

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_mem0 >= 7
	t4_t1_t1_mem0 += MAIN_MEM_r[0]

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 7
	t4_t51_mem1 += MAIN_MEM_r[1]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 8
	t1_t1_in += MM_in[0]

	t4_t1_t0 = S.Task('t4_t1_t0', length=8, delay_cost=1)
	S += t4_t1_t0 >= 8
	t4_t1_t0 += MM[0]

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_mem1 >= 8
	t4_t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	S += t4_t8_t1_mem0 >= 8
	t4_t8_t1_mem0 += MAIN_MEM_r[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 9
	t0_t0_in += MM_in[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 9
	t0_t1_mem1 += MAIN_MEM_r[1]

	t1_t1 = S.Task('t1_t1', length=8, delay_cost=1)
	S += t1_t1 >= 9
	t1_t1 += MM[0]

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t2_mem0 >= 9
	t4_t1_t2_mem0 += MAIN_MEM_r[0]

	t0_t0 = S.Task('t0_t0', length=8, delay_cost=1)
	S += t0_t0 >= 10
	t0_t0 += MM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 10
	t2_t1_in += MM_in[0]

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 10
	t4_t2_t2_mem1 += MAIN_MEM_r[1]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 10
	t4_t51_mem0 += MAIN_MEM_r[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 11
	t0_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 11
	t1_t1_mem1 += MAIN_MEM_r[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 11
	t2_t0_in += MM_in[0]

	t2_t1 = S.Task('t2_t1', length=8, delay_cost=1)
	S += t2_t1 >= 11
	t2_t1 += MM[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 12
	t0_t2_mem0 += MAIN_MEM_r[0]

	t2_t0 = S.Task('t2_t0', length=8, delay_cost=1)
	S += t2_t0 >= 12
	t2_t0 += MM[0]

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 12
	t4_t40_mem1 += MAIN_MEM_r[1]

	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	S += t4_t8_t1_in >= 12
	t4_t8_t1_in += MM_in[0]

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_in >= 13
	t4_t0_t1_in += MM_in[0]

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	S += t4_t2_t0_mem0 >= 13
	t4_t2_t0_mem0 += MAIN_MEM_r[0]

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 13
	t4_t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t8_t1 = S.Task('t4_t8_t1', length=8, delay_cost=1)
	S += t4_t8_t1 >= 13
	t4_t8_t1 += MM[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 14
	t0_t0_mem1 += MAIN_MEM_r[1]

	t4_t0_t1 = S.Task('t4_t0_t1', length=8, delay_cost=1)
	S += t4_t0_t1 >= 14
	t4_t0_t1 += MM[0]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 14
	t4_t41_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 15
	t1_t0_mem1 += MAIN_MEM_r[1]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 15
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 16
	t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 16
	t4_t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 17
	t4_t50_mem0 += MAIN_MEM_r[0]

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	S += t4_t8_t1_mem1 >= 17
	t4_t8_t1_mem1 += MAIN_MEM_r[1]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 18
	t0_t2_mem1 += MAIN_MEM_r[1]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 18
	t1_t2_mem0 += MAIN_MEM_r[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 19
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 19
	t0_t3_mem1 += MAIN_MEM_r[1]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 20
	t0_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 20
	t4_t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_mem1 >= 21
	t4_t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	S += t4_t8_t0_mem0 >= 21
	t4_t8_t0_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 22
	t1_t3_mem1 += MAIN_MEM_r[1]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 22
	t4_t2_t2_mem0 += MAIN_MEM_r[0]

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_mem0 >= 23
	t4_t0_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_mem1 >= 23
	t4_t0_t0_mem1 += MAIN_MEM_r[1]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 24
	t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	S += t4_t2_t0_mem1 >= 24
	t4_t2_t0_mem1 += MAIN_MEM_r[1]

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 25
	t4_t0_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_mem0 >= 25
	t4_t1_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 26
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 26
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 27
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 27
	t2_t3_mem1 += MAIN_MEM_r[1]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 28
	t1_t3_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 28
	t2_t1_mem1 += MAIN_MEM_r[1]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 29
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 29
	t2_t2_mem1 += MAIN_MEM_r[1]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 30
	t81_mem0 += MAIN_MEM_r[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 30
	t81_mem1 += MAIN_MEM_r[1]

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 31
	t4_t8_t2_mem1 += MAIN_MEM_r[1]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 31
	t5_t0_t2_mem0 += MAIN_MEM_r[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 32
	t71_mem1 += MAIN_MEM_r[1]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 32
	t80_mem0 += MAIN_MEM_r[0]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 33
	t100_mem0 += MAIN_MEM_r[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 33
	t91_mem1 += MAIN_MEM_r[1]

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 34
	t4_t8_t3_mem1 += MAIN_MEM_r[1]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 34
	t91_mem0 += MAIN_MEM_r[0]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 35
	t4_t8_t3_mem0 += MAIN_MEM_r[0]

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 35
	t5_t0_t2_mem1 += MAIN_MEM_r[1]

	t5_t8_t2_mem0 = S.Task('t5_t8_t2_mem0', length=1, delay_cost=1)
	S += t5_t8_t2_mem0 >= 36
	t5_t8_t2_mem0 += MAIN_MEM_r[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 36
	t70_mem1 += MAIN_MEM_r[1]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 37
	t71_mem0 += MAIN_MEM_r[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 37
	t80_mem1 += MAIN_MEM_r[1]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 38
	t90_mem0 += MAIN_MEM_r[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 38
	t90_mem1 += MAIN_MEM_r[1]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 39
	t100_mem1 += MAIN_MEM_r[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 39
	t101_mem0 += MAIN_MEM_r[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 40
	t101_mem1 += MAIN_MEM_r[1]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 40
	t70_mem0 += MAIN_MEM_r[0]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 41
	t4_t8_t2_mem0 += MAIN_MEM_r[0]

	t5_t8_t2_mem1 = S.Task('t5_t8_t2_mem1', length=1, delay_cost=1)
	S += t5_t8_t2_mem1 >= 41
	t5_t8_t2_mem1 += MAIN_MEM_r[1]


	# new tasks
	t1_t4_in = S.Task('t1_t4_in', length=1, delay_cost=1)
	t1_t4_in += alt(MM_in)
	t1_t4 = S.Task('t1_t4', length=8, delay_cost=1)
	t1_t4 += alt(MM)
	S += t1_t4>=t1_t4_in

	t1_t4_mem0 = S.Task('t1_t4_mem0', length=1, delay_cost=1)
	t1_t4_mem0 += MAS_MEM[8]
	S += 1 < t1_t4_mem0
	S += t1_t4_mem0 <= t1_t4

	t1_t4_mem1 = S.Task('t1_t4_mem1', length=1, delay_cost=1)
	t1_t4_mem1 += MAS_MEM[9]
	S += 3 < t1_t4_mem1
	S += t1_t4_mem1 <= t1_t4

	t10 = S.Task('t10', length=1, delay_cost=1)
	t10 += alt(MAS)

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += MM_MEM[0]
	S += 14 < t10_mem0
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += MM_MEM[1]
	S += 16 < t10_mem1
	S += t10_mem1 <= t10

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	t1_t5 += alt(MAS)

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	t1_t5_mem0 += MM_MEM[0]
	S += 14 < t1_t5_mem0
	S += t1_t5_mem0 <= t1_t5

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	t1_t5_mem1 += MM_MEM[1]
	S += 16 < t1_t5_mem1
	S += t1_t5_mem1 <= t1_t5

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	t2_t4_in += alt(MM_in)
	t2_t4 = S.Task('t2_t4', length=8, delay_cost=1)
	t2_t4 += alt(MM)
	S += t2_t4>=t2_t4_in

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	t2_t4_mem0 += MAS_MEM[2]
	S += 3 < t2_t4_mem0
	S += t2_t4_mem0 <= t2_t4

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	t2_t4_mem1 += MAS_MEM[5]
	S += 3 < t2_t4_mem1
	S += t2_t4_mem1 <= t2_t4

	t20 = S.Task('t20', length=1, delay_cost=1)
	t20 += alt(MAS)

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += MM_MEM[0]
	S += 19 < t20_mem0
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += MM_MEM[1]
	S += 18 < t20_mem1
	S += t20_mem1 <= t20

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	t2_t5 += alt(MAS)

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	t2_t5_mem0 += MM_MEM[0]
	S += 19 < t2_t5_mem0
	S += t2_t5_mem0 <= t2_t5

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	t2_t5_mem1 += MM_MEM[1]
	S += 18 < t2_t5_mem1
	S += t2_t5_mem1 <= t2_t5

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	t0_t4_in += alt(MM_in)
	t0_t4 = S.Task('t0_t4', length=8, delay_cost=1)
	t0_t4 += alt(MM)
	S += t0_t4>=t0_t4_in

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	t0_t4_mem0 += MAS_MEM[0]
	S += 2 < t0_t4_mem0
	S += t0_t4_mem0 <= t0_t4

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	t0_t4_mem1 += MAS_MEM[1]
	S += 1 < t0_t4_mem1
	S += t0_t4_mem1 <= t0_t4

	t00 = S.Task('t00', length=1, delay_cost=1)
	t00 += alt(MAS)

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += MM_MEM[0]
	S += 17 < t00_mem0
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += MM_MEM[1]
	S += 12 < t00_mem1
	S += t00_mem1 <= t00

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	t0_t5 += alt(MAS)

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MM_MEM[0]
	S += 17 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	t0_t5_mem1 += MM_MEM[1]
	S += 12 < t0_t5_mem1
	S += t0_t5_mem1 <= t0_t5

	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	t4_t0_t4_in += alt(MM_in)
	t4_t0_t4 = S.Task('t4_t0_t4', length=8, delay_cost=1)
	t4_t0_t4 += alt(MM)
	S += t4_t0_t4>=t4_t0_t4_in

	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	t4_t0_t4_mem0 += MAS_MEM[6]
	S += 3 < t4_t0_t4_mem0
	S += t4_t0_t4_mem0 <= t4_t0_t4

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	t4_t0_t4_mem1 += MAS_MEM[3]
	S += 4 < t4_t0_t4_mem1
	S += t4_t0_t4_mem1 <= t4_t0_t4

	t4_t00 = S.Task('t4_t00', length=1, delay_cost=1)
	t4_t00 += alt(MAS)

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	t4_t00_mem0 += MM_MEM[0]
	S += 13 < t4_t00_mem0
	S += t4_t00_mem0 <= t4_t00

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	t4_t00_mem1 += MM_MEM[1]
	S += 21 < t4_t00_mem1
	S += t4_t00_mem1 <= t4_t00

	t4_t0_t5 = S.Task('t4_t0_t5', length=1, delay_cost=1)
	t4_t0_t5 += alt(MAS)

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	t4_t0_t5_mem0 += MM_MEM[0]
	S += 13 < t4_t0_t5_mem0
	S += t4_t0_t5_mem0 <= t4_t0_t5

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	t4_t0_t5_mem1 += MM_MEM[1]
	S += 21 < t4_t0_t5_mem1
	S += t4_t0_t5_mem1 <= t4_t0_t5

	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	t4_t1_t4_in += alt(MM_in)
	t4_t1_t4 = S.Task('t4_t1_t4', length=8, delay_cost=1)
	t4_t1_t4 += alt(MM)
	S += t4_t1_t4>=t4_t1_t4_in

	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	t4_t1_t4_mem0 += MAS_MEM[4]
	S += 2 < t4_t1_t4_mem0
	S += t4_t1_t4_mem0 <= t4_t1_t4

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	t4_t1_t4_mem1 += MAS_MEM[7]
	S += 1 < t4_t1_t4_mem1
	S += t4_t1_t4_mem1 <= t4_t1_t4

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	t4_t10 += alt(MAS)

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	t4_t10_mem0 += MM_MEM[0]
	S += 15 < t4_t10_mem0
	S += t4_t10_mem0 <= t4_t10

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	t4_t10_mem1 += MM_MEM[1]
	S += 8 < t4_t10_mem1
	S += t4_t10_mem1 <= t4_t10

	t4_t1_t5 = S.Task('t4_t1_t5', length=1, delay_cost=1)
	t4_t1_t5 += alt(MAS)

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	t4_t1_t5_mem0 += MM_MEM[0]
	S += 15 < t4_t1_t5_mem0
	S += t4_t1_t5_mem0 <= t4_t1_t5

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	t4_t1_t5_mem1 += MM_MEM[1]
	S += 8 < t4_t1_t5_mem1
	S += t4_t1_t5_mem1 <= t4_t1_t5

	t4_t2_t4_in = S.Task('t4_t2_t4_in', length=1, delay_cost=1)
	t4_t2_t4_in += alt(MM_in)
	t4_t2_t4 = S.Task('t4_t2_t4', length=8, delay_cost=1)
	t4_t2_t4 += alt(MM)
	S += t4_t2_t4>=t4_t2_t4_in

	t4_t2_t4_mem0 = S.Task('t4_t2_t4_mem0', length=1, delay_cost=1)
	t4_t2_t4_mem0 += MAS_MEM[8]
	S += 2 < t4_t2_t4_mem0
	S += t4_t2_t4_mem0 <= t4_t2_t4

	t4_t2_t4_mem1 = S.Task('t4_t2_t4_mem1', length=1, delay_cost=1)
	t4_t2_t4_mem1 += MAS_MEM[5]
	S += 1 < t4_t2_t4_mem1
	S += t4_t2_t4_mem1 <= t4_t2_t4

	t4_t20 = S.Task('t4_t20', length=1, delay_cost=1)
	t4_t20 += alt(MAS)

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	t4_t20_mem0 += MM_MEM[0]
	S += 9 < t4_t20_mem0
	S += t4_t20_mem0 <= t4_t20

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	t4_t20_mem1 += MM_MEM[1]
	S += 11 < t4_t20_mem1
	S += t4_t20_mem1 <= t4_t20

	t4_t2_t5 = S.Task('t4_t2_t5', length=1, delay_cost=1)
	t4_t2_t5 += alt(MAS)

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	t4_t2_t5_mem0 += MM_MEM[0]
	S += 9 < t4_t2_t5_mem0
	S += t4_t2_t5_mem0 <= t4_t2_t5

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	t4_t2_t5_mem1 += MM_MEM[1]
	S += 11 < t4_t2_t5_mem1
	S += t4_t2_t5_mem1 <= t4_t2_t5

	t4_t6_t0_in = S.Task('t4_t6_t0_in', length=1, delay_cost=1)
	t4_t6_t0_in += alt(MM_in)
	t4_t6_t0 = S.Task('t4_t6_t0', length=8, delay_cost=1)
	t4_t6_t0 += alt(MM)
	S += t4_t6_t0>=t4_t6_t0_in

	t4_t6_t0_mem0 = S.Task('t4_t6_t0_mem0', length=1, delay_cost=1)
	t4_t6_t0_mem0 += MAS_MEM[2]
	S += 1 < t4_t6_t0_mem0
	S += t4_t6_t0_mem0 <= t4_t6_t0

	t4_t6_t0_mem1 = S.Task('t4_t6_t0_mem1', length=1, delay_cost=1)
	t4_t6_t0_mem1 += MAS_MEM[7]
	S += 2 < t4_t6_t0_mem1
	S += t4_t6_t0_mem1 <= t4_t6_t0

	t4_t6_t1_in = S.Task('t4_t6_t1_in', length=1, delay_cost=1)
	t4_t6_t1_in += alt(MM_in)
	t4_t6_t1 = S.Task('t4_t6_t1', length=8, delay_cost=1)
	t4_t6_t1 += alt(MM)
	S += t4_t6_t1>=t4_t6_t1_in

	t4_t6_t1_mem0 = S.Task('t4_t6_t1_mem0', length=1, delay_cost=1)
	t4_t6_t1_mem0 += MAS_MEM[2]
	S += 2 < t4_t6_t1_mem0
	S += t4_t6_t1_mem0 <= t4_t6_t1

	t4_t6_t1_mem1 = S.Task('t4_t6_t1_mem1', length=1, delay_cost=1)
	t4_t6_t1_mem1 += MAS_MEM[1]
	S += 3 < t4_t6_t1_mem1
	S += t4_t6_t1_mem1 <= t4_t6_t1

	t4_t6_t2 = S.Task('t4_t6_t2', length=1, delay_cost=1)
	t4_t6_t2 += alt(MAS)

	t4_t6_t2_mem0 = S.Task('t4_t6_t2_mem0', length=1, delay_cost=1)
	t4_t6_t2_mem0 += MAS_MEM[2]
	S += 1 < t4_t6_t2_mem0
	S += t4_t6_t2_mem0 <= t4_t6_t2

	t4_t6_t2_mem1 = S.Task('t4_t6_t2_mem1', length=1, delay_cost=1)
	t4_t6_t2_mem1 += MAS_MEM[3]
	S += 2 < t4_t6_t2_mem1
	S += t4_t6_t2_mem1 <= t4_t6_t2

	t4_t6_t3 = S.Task('t4_t6_t3', length=1, delay_cost=1)
	t4_t6_t3 += alt(MAS)

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	t4_t6_t3_mem0 += MAS_MEM[6]
	S += 2 < t4_t6_t3_mem0
	S += t4_t6_t3_mem0 <= t4_t6_t3

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	t4_t6_t3_mem1 += MAS_MEM[1]
	S += 3 < t4_t6_t3_mem1
	S += t4_t6_t3_mem1 <= t4_t6_t3

	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	t4_t8_t4_in += alt(MM_in)
	t4_t8_t4 = S.Task('t4_t8_t4', length=8, delay_cost=1)
	t4_t8_t4 += alt(MM)
	S += t4_t8_t4>=t4_t8_t4_in

	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	t4_t8_t4_mem0 += MAS_MEM[2]
	S += 5 < t4_t8_t4_mem0
	S += t4_t8_t4_mem0 <= t4_t8_t4

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	t4_t8_t4_mem1 += MAS_MEM[7]
	S += 6 < t4_t8_t4_mem1
	S += t4_t8_t4_mem1 <= t4_t8_t4

	t4_t80 = S.Task('t4_t80', length=1, delay_cost=1)
	t4_t80 += alt(MAS)

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	t4_t80_mem0 += MM_MEM[0]
	S += 10 < t4_t80_mem0
	S += t4_t80_mem0 <= t4_t80

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	t4_t80_mem1 += MM_MEM[1]
	S += 20 < t4_t80_mem1
	S += t4_t80_mem1 <= t4_t80

	t4_t8_t5 = S.Task('t4_t8_t5', length=1, delay_cost=1)
	t4_t8_t5 += alt(MAS)

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	t4_t8_t5_mem0 += MM_MEM[0]
	S += 10 < t4_t8_t5_mem0
	S += t4_t8_t5_mem0 <= t4_t8_t5

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	t4_t8_t5_mem1 += MM_MEM[1]
	S += 20 < t4_t8_t5_mem1
	S += t4_t8_t5_mem1 <= t4_t8_t5

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	t5_t0_t0_in += alt(MM_in)
	t5_t0_t0 = S.Task('t5_t0_t0', length=8, delay_cost=1)
	t5_t0_t0 += alt(MM)
	S += t5_t0_t0>=t5_t0_t0_in

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	t5_t0_t0_mem0 += MAIN_MEM_r[0]
	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	t5_t0_t0_mem1 += MAS_MEM[7]
	S += 4 < t5_t0_t0_mem1
	S += t5_t0_t0_mem1 <= t5_t0_t0

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	t5_t0_t1_in += alt(MM_in)
	t5_t0_t1 = S.Task('t5_t0_t1', length=8, delay_cost=1)
	t5_t0_t1 += alt(MM)
	S += t5_t0_t1>=t5_t0_t1_in

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	t5_t0_t1_mem0 += MAIN_MEM_r[0]
	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	t5_t0_t1_mem1 += MAS_MEM[3]
	S += 6 < t5_t0_t1_mem1
	S += t5_t0_t1_mem1 <= t5_t0_t1

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	t5_t0_t3 += alt(MAS)

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	t5_t0_t3_mem0 += MAS_MEM[6]
	S += 4 < t5_t0_t3_mem0
	S += t5_t0_t3_mem0 <= t5_t0_t3

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	t5_t0_t3_mem1 += MAS_MEM[3]
	S += 6 < t5_t0_t3_mem1
	S += t5_t0_t3_mem1 <= t5_t0_t3

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	t5_t1_t0_in += alt(MM_in)
	t5_t1_t0 = S.Task('t5_t1_t0', length=8, delay_cost=1)
	t5_t1_t0 += alt(MM)
	S += t5_t1_t0>=t5_t1_t0_in

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	t5_t1_t0_mem0 += MAS_MEM[8]
	S += 5 < t5_t1_t0_mem0
	S += t5_t1_t0_mem0 <= t5_t1_t0

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	t5_t1_t0_mem1 += MAS_MEM[5]
	S += 5 < t5_t1_t0_mem1
	S += t5_t1_t0_mem1 <= t5_t1_t0

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	t5_t1_t1_in += alt(MM_in)
	t5_t1_t1 = S.Task('t5_t1_t1', length=8, delay_cost=1)
	t5_t1_t1 += alt(MM)
	S += t5_t1_t1>=t5_t1_t1_in

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	t5_t1_t1_mem0 += MAS_MEM[4]
	S += 4 < t5_t1_t1_mem0
	S += t5_t1_t1_mem0 <= t5_t1_t1

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	t5_t1_t1_mem1 += MAS_MEM[1]
	S += 6 < t5_t1_t1_mem1
	S += t5_t1_t1_mem1 <= t5_t1_t1

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	t5_t1_t2 += alt(MAS)

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	t5_t1_t2_mem0 += MAS_MEM[8]
	S += 5 < t5_t1_t2_mem0
	S += t5_t1_t2_mem0 <= t5_t1_t2

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	t5_t1_t2_mem1 += MAS_MEM[5]
	S += 4 < t5_t1_t2_mem1
	S += t5_t1_t2_mem1 <= t5_t1_t2

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	t5_t1_t3 += alt(MAS)

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	t5_t1_t3_mem0 += MAS_MEM[4]
	S += 5 < t5_t1_t3_mem0
	S += t5_t1_t3_mem0 <= t5_t1_t3

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	t5_t1_t3_mem1 += MAS_MEM[1]
	S += 6 < t5_t1_t3_mem1
	S += t5_t1_t3_mem1 <= t5_t1_t3

	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	t5_t2_t0_in += alt(MM_in)
	t5_t2_t0 = S.Task('t5_t2_t0', length=8, delay_cost=1)
	t5_t2_t0 += alt(MM)
	S += t5_t2_t0>=t5_t2_t0_in

	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	t5_t2_t0_mem0 += MAS_MEM[8]
	S += 5 < t5_t2_t0_mem0
	S += t5_t2_t0_mem0 <= t5_t2_t0

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	t5_t2_t0_mem1 += MAS_MEM[7]
	S += 5 < t5_t2_t0_mem1
	S += t5_t2_t0_mem1 <= t5_t2_t0

	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	t5_t2_t1_in += alt(MM_in)
	t5_t2_t1 = S.Task('t5_t2_t1', length=8, delay_cost=1)
	t5_t2_t1 += alt(MM)
	S += t5_t2_t1>=t5_t2_t1_in

	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	t5_t2_t1_mem0 += MAS_MEM[4]
	S += 4 < t5_t2_t1_mem0
	S += t5_t2_t1_mem0 <= t5_t2_t1

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	t5_t2_t1_mem1 += MAS_MEM[9]
	S += 4 < t5_t2_t1_mem1
	S += t5_t2_t1_mem1 <= t5_t2_t1

	t5_t2_t2 = S.Task('t5_t2_t2', length=1, delay_cost=1)
	t5_t2_t2 += alt(MAS)

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	t5_t2_t2_mem0 += MAS_MEM[8]
	S += 5 < t5_t2_t2_mem0
	S += t5_t2_t2_mem0 <= t5_t2_t2

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	t5_t2_t2_mem1 += MAS_MEM[5]
	S += 4 < t5_t2_t2_mem1
	S += t5_t2_t2_mem1 <= t5_t2_t2

	t5_t2_t3 = S.Task('t5_t2_t3', length=1, delay_cost=1)
	t5_t2_t3 += alt(MAS)

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	t5_t2_t3_mem0 += MAS_MEM[6]
	S += 5 < t5_t2_t3_mem0
	S += t5_t2_t3_mem0 <= t5_t2_t3

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	t5_t2_t3_mem1 += MAS_MEM[9]
	S += 4 < t5_t2_t3_mem1
	S += t5_t2_t3_mem1 <= t5_t2_t3

	t5_t40 = S.Task('t5_t40', length=1, delay_cost=1)
	t5_t40 += alt(MAS)

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	t5_t40_mem0 += MAIN_MEM_r[0]
	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	t5_t40_mem1 += MAS_MEM[9]
	S += 5 < t5_t40_mem1
	S += t5_t40_mem1 <= t5_t40

	t5_t41 = S.Task('t5_t41', length=1, delay_cost=1)
	t5_t41 += alt(MAS)

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	t5_t41_mem0 += MAIN_MEM_r[0]
	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	t5_t41_mem1 += MAS_MEM[5]
	S += 4 < t5_t41_mem1
	S += t5_t41_mem1 <= t5_t41

	t5_t50 = S.Task('t5_t50', length=1, delay_cost=1)
	t5_t50 += alt(MAS)

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	t5_t50_mem0 += MAS_MEM[6]
	S += 4 < t5_t50_mem0
	S += t5_t50_mem0 <= t5_t50

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	t5_t50_mem1 += MAS_MEM[5]
	S += 5 < t5_t50_mem1
	S += t5_t50_mem1 <= t5_t50

	t5_t51 = S.Task('t5_t51', length=1, delay_cost=1)
	t5_t51 += alt(MAS)

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	t5_t51_mem0 += MAS_MEM[2]
	S += 6 < t5_t51_mem0
	S += t5_t51_mem0 <= t5_t51

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	t5_t51_mem1 += MAS_MEM[1]
	S += 6 < t5_t51_mem1
	S += t5_t51_mem1 <= t5_t51

	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	t5_t8_t0_in += alt(MM_in)
	t5_t8_t0 = S.Task('t5_t8_t0', length=8, delay_cost=1)
	t5_t8_t0 += alt(MM)
	S += t5_t8_t0>=t5_t8_t0_in

	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	t5_t8_t0_mem0 += MAIN_MEM_r[0]
	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	t5_t8_t0_mem1 += MAS_MEM[7]
	S += 5 < t5_t8_t0_mem1
	S += t5_t8_t0_mem1 <= t5_t8_t0

	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	t5_t8_t1_in += alt(MM_in)
	t5_t8_t1 = S.Task('t5_t8_t1', length=8, delay_cost=1)
	t5_t8_t1 += alt(MM)
	S += t5_t8_t1>=t5_t8_t1_in

	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	t5_t8_t1_mem0 += MAIN_MEM_r[0]
	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	t5_t8_t1_mem1 += MAS_MEM[9]
	S += 4 < t5_t8_t1_mem1
	S += t5_t8_t1_mem1 <= t5_t8_t1

	t5_t8_t3 = S.Task('t5_t8_t3', length=1, delay_cost=1)
	t5_t8_t3 += alt(MAS)

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	t5_t8_t3_mem0 += MAS_MEM[6]
	S += 5 < t5_t8_t3_mem0
	S += t5_t8_t3_mem0 <= t5_t8_t3

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	t5_t8_t3_mem1 += MAS_MEM[9]
	S += 4 < t5_t8_t3_mem1
	S += t5_t8_t3_mem1 <= t5_t8_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage1MAS5/SPARSE/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

