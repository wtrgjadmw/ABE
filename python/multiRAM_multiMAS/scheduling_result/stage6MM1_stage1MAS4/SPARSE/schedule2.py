from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 131
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_in >= 0
	t4_t1_t1_in += MM_in[0]

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_mem0 >= 0
	t4_t1_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_mem1 >= 0
	t4_t1_t1_mem1 += MAIN_MEM_r[1]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 1
	t1_t0_in += MM_in[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 1
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 1
	t1_t0_mem1 += MAIN_MEM_r[1]

	t4_t1_t1 = S.Task('t4_t1_t1', length=6, delay_cost=1)
	S += t4_t1_t1 >= 1
	t4_t1_t1 += MM[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 2
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 2
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 2
	t0_t0_mem1 += MAIN_MEM_r[1]

	t1_t0 = S.Task('t1_t0', length=6, delay_cost=1)
	S += t1_t0 >= 2
	t1_t0 += MM[0]

	t0_t0 = S.Task('t0_t0', length=6, delay_cost=1)
	S += t0_t0 >= 3
	t0_t0 += MM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 3
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 3
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 3
	t2_t1_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=6, delay_cost=1)
	S += t2_t1 >= 4
	t2_t1 += MM[0]

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_in >= 4
	t4_t0_t0_in += MM_in[0]

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_mem0 >= 4
	t4_t0_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_mem1 >= 4
	t4_t0_t0_mem1 += MAIN_MEM_r[1]

	t4_t0_t0 = S.Task('t4_t0_t0', length=6, delay_cost=1)
	S += t4_t0_t0 >= 5
	t4_t0_t0 += MM[0]

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_in >= 5
	t4_t0_t1_in += MM_in[0]

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_mem0 >= 5
	t4_t0_t1_mem0 += MAIN_MEM_r[0]

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_mem1 >= 5
	t4_t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 6
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 6
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 6
	t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t0_t1 = S.Task('t4_t0_t1', length=6, delay_cost=1)
	S += t4_t0_t1 >= 6
	t4_t0_t1 += MM[0]

	t0_t1 = S.Task('t0_t1', length=6, delay_cost=1)
	S += t0_t1 >= 7
	t0_t1 += MM[0]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 7
	t1_t1_in += MM_in[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 7
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 7
	t1_t1_mem1 += MAIN_MEM_r[1]

	t1_t1 = S.Task('t1_t1', length=6, delay_cost=1)
	S += t1_t1 >= 8
	t1_t1 += MM[0]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 8
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 8
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 8
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=6, delay_cost=1)
	S += t2_t0 >= 9
	t2_t0 += MM[0]

	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_in >= 9
	t4_t1_t0_in += MM_in[0]

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_mem0 >= 9
	t4_t1_t0_mem0 += MAIN_MEM_r[0]

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_mem1 >= 9
	t4_t1_t0_mem1 += MAIN_MEM_r[1]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 10
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 10
	t2_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_t0 = S.Task('t4_t1_t0', length=6, delay_cost=1)
	S += t4_t1_t0 >= 10
	t4_t1_t0 += MM[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 11
	t1_t2_mem0 += MAIN_MEM_r[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 11
	t1_t2_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 11
	t2_t2 += MAS[0]

	t1_t2 = S.Task('t1_t2', length=1, delay_cost=1)
	S += t1_t2 >= 12
	t1_t2 += MAS[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 12
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 12
	t2_t3_mem1 += MAIN_MEM_r[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 13
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 13
	t0_t3_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 13
	t2_t3 += MAS[0]

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 14
	t0_t3 += MAS[2]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 14
	t4_t0_t2_mem0 += MAIN_MEM_r[0]

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 14
	t4_t0_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_t2 = S.Task('t4_t0_t2', length=1, delay_cost=1)
	S += t4_t0_t2 >= 15
	t4_t0_t2 += MAS[2]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 15
	t4_t1_t3_mem0 += MAIN_MEM_r[0]

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 15
	t4_t1_t3_mem1 += MAIN_MEM_r[1]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 16
	t4_t0_t3_mem0 += MAIN_MEM_r[0]

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 16
	t4_t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t1_t3 = S.Task('t4_t1_t3', length=1, delay_cost=1)
	S += t4_t1_t3 >= 16
	t4_t1_t3 += MAS[0]

	t4_t0_t3 = S.Task('t4_t0_t3', length=1, delay_cost=1)
	S += t4_t0_t3 >= 17
	t4_t0_t3 += MAS[0]

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t2_mem0 >= 17
	t4_t1_t2_mem0 += MAIN_MEM_r[0]

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t2_mem1 >= 17
	t4_t1_t2_mem1 += MAIN_MEM_r[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 18
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 18
	t0_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_t2 = S.Task('t4_t1_t2', length=1, delay_cost=1)
	S += t4_t1_t2 >= 18
	t4_t1_t2 += MAS[3]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 19
	t0_t2 += MAS[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 19
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 19
	t1_t3_mem1 += MAIN_MEM_r[1]

	t1_t3 = S.Task('t1_t3', length=1, delay_cost=1)
	S += t1_t3 >= 20
	t1_t3 += MAS[0]

	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	S += t4_t8_t0_in >= 20
	t4_t8_t0_in += MM_in[0]

	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	S += t4_t8_t0_mem0 >= 20
	t4_t8_t0_mem0 += MAIN_MEM_r[0]

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	S += t4_t8_t0_mem1 >= 20
	t4_t8_t0_mem1 += MAIN_MEM_r[1]

	t4_t8_t0 = S.Task('t4_t8_t0', length=6, delay_cost=1)
	S += t4_t8_t0 >= 21
	t4_t8_t0 += MM[0]

	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	S += t4_t8_t1_in >= 21
	t4_t8_t1_in += MM_in[0]

	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	S += t4_t8_t1_mem0 >= 21
	t4_t8_t1_mem0 += MAIN_MEM_r[0]

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	S += t4_t8_t1_mem1 >= 21
	t4_t8_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	S += t4_t2_t0_in >= 22
	t4_t2_t0_in += MM_in[0]

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	S += t4_t2_t0_mem0 >= 22
	t4_t2_t0_mem0 += MAIN_MEM_r[0]

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	S += t4_t2_t0_mem1 >= 22
	t4_t2_t0_mem1 += MAIN_MEM_r[1]

	t4_t8_t1 = S.Task('t4_t8_t1', length=6, delay_cost=1)
	S += t4_t8_t1 >= 22
	t4_t8_t1 += MM[0]

	t4_t2_t0 = S.Task('t4_t2_t0', length=6, delay_cost=1)
	S += t4_t2_t0 >= 23
	t4_t2_t0 += MM[0]

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 23
	t4_t2_t1_in += MM_in[0]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 23
	t4_t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 23
	t4_t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t1 = S.Task('t4_t2_t1', length=6, delay_cost=1)
	S += t4_t2_t1 >= 24
	t4_t2_t1 += MM[0]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 24
	t4_t51_mem0 += MAIN_MEM_r[0]

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 24
	t4_t51_mem1 += MAIN_MEM_r[1]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 25
	t4_t41_mem0 += MAIN_MEM_r[0]

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 25
	t4_t41_mem1 += MAIN_MEM_r[1]

	t4_t51 = S.Task('t4_t51', length=1, delay_cost=1)
	S += t4_t51 >= 25
	t4_t51 += MAS[0]

	t4_t41 = S.Task('t4_t41', length=1, delay_cost=1)
	S += t4_t41 >= 26
	t4_t41 += MAS[2]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 26
	t4_t50_mem0 += MAIN_MEM_r[0]

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 26
	t4_t50_mem1 += MAIN_MEM_r[1]

	t4_t50 = S.Task('t4_t50', length=1, delay_cost=1)
	S += t4_t50 >= 27
	t4_t50 += MAS[3]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 27
	t81_mem0 += MAIN_MEM_r[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 27
	t81_mem1 += MAIN_MEM_r[1]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 28
	t81 += MAS[3]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 28
	t91_mem0 += MAIN_MEM_r[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 28
	t91_mem1 += MAIN_MEM_r[1]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 29
	t100_mem0 += MAIN_MEM_r[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 29
	t100_mem1 += MAIN_MEM_r[1]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 29
	t91 += MAS[2]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 30
	t100 += MAS[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 30
	t80_mem0 += MAIN_MEM_r[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 30
	t80_mem1 += MAIN_MEM_r[1]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 31
	t4_t2_t2_mem0 += MAIN_MEM_r[0]

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 31
	t4_t2_t2_mem1 += MAIN_MEM_r[1]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 31
	t80 += MAS[0]

	t4_t2_t2 = S.Task('t4_t2_t2', length=1, delay_cost=1)
	S += t4_t2_t2 >= 32
	t4_t2_t2 += MAS[1]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 32
	t4_t40_mem0 += MAIN_MEM_r[0]

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 32
	t4_t40_mem1 += MAIN_MEM_r[1]

	t4_t40 = S.Task('t4_t40', length=1, delay_cost=1)
	S += t4_t40 >= 33
	t4_t40 += MAS[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 33
	t90_mem0 += MAIN_MEM_r[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 33
	t90_mem1 += MAIN_MEM_r[1]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 34
	t4_t8_t3_mem0 += MAIN_MEM_r[0]

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 34
	t4_t8_t3_mem1 += MAIN_MEM_r[1]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 34
	t90 += MAS[3]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 35
	t101_mem0 += MAIN_MEM_r[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 35
	t101_mem1 += MAIN_MEM_r[1]

	t4_t8_t3 = S.Task('t4_t8_t3', length=1, delay_cost=1)
	S += t4_t8_t3 >= 35
	t4_t8_t3 += MAS[0]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 36
	t101 += MAS[1]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 36
	t4_t8_t2_mem0 += MAIN_MEM_r[0]

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 36
	t4_t8_t2_mem1 += MAIN_MEM_r[1]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 37
	t4_t2_t3_mem0 += MAIN_MEM_r[0]

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 37
	t4_t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t8_t2 = S.Task('t4_t8_t2', length=1, delay_cost=1)
	S += t4_t8_t2 >= 37
	t4_t8_t2 += MAS[0]

	t4_t2_t3 = S.Task('t4_t2_t3', length=1, delay_cost=1)
	S += t4_t2_t3 >= 38
	t4_t2_t3 += MAS[2]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 38
	t71_mem0 += MAIN_MEM_r[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 38
	t71_mem1 += MAIN_MEM_r[1]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 39
	t70_mem0 += MAIN_MEM_r[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 39
	t70_mem1 += MAIN_MEM_r[1]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 39
	t71 += MAS[0]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 40
	t70 += MAS[1]


	# new tasks
	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	t5_t0_t2 += alt(MAS)

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	t5_t0_t2_mem0 += MAIN_MEM_r[0]
	S += t5_t0_t2_mem0 <= t5_t0_t2

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	t5_t0_t2_mem1 += MAIN_MEM_r[1]
	S += t5_t0_t2_mem1 <= t5_t0_t2

	t5_t8_t2 = S.Task('t5_t8_t2', length=1, delay_cost=1)
	t5_t8_t2 += alt(MAS)

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

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage6MM1_stage1MAS4/SPARSE/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

