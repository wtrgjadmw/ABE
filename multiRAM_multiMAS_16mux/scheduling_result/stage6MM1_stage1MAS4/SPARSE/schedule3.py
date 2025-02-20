from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 170
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 0
	t4_t2_t1_in += MM_in[0]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 0
	t4_t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 0
	t4_t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_in >= 1
	t4_t1_t1_in += MM_in[0]

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_mem0 >= 1
	t4_t1_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_mem1 >= 1
	t4_t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t2_t1 = S.Task('t4_t2_t1', length=6, delay_cost=1)
	S += t4_t2_t1 >= 1
	t4_t2_t1 += MM[0]

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_in >= 2
	t4_t0_t1_in += MM_in[0]

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_mem0 >= 2
	t4_t0_t1_mem0 += MAIN_MEM_r[0]

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_mem1 >= 2
	t4_t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t1_t1 = S.Task('t4_t1_t1', length=6, delay_cost=1)
	S += t4_t1_t1 >= 2
	t4_t1_t1 += MM[0]

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_in >= 3
	t4_t0_t0_in += MM_in[0]

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_mem0 >= 3
	t4_t0_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_mem1 >= 3
	t4_t0_t0_mem1 += MAIN_MEM_r[1]

	t4_t0_t1 = S.Task('t4_t0_t1', length=6, delay_cost=1)
	S += t4_t0_t1 >= 3
	t4_t0_t1 += MM[0]

	t4_t0_t0 = S.Task('t4_t0_t0', length=6, delay_cost=1)
	S += t4_t0_t0 >= 4
	t4_t0_t0 += MM[0]

	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	S += t4_t8_t0_in >= 4
	t4_t8_t0_in += MM_in[0]

	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	S += t4_t8_t0_mem0 >= 4
	t4_t8_t0_mem0 += MAIN_MEM_r[0]

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	S += t4_t8_t0_mem1 >= 4
	t4_t8_t0_mem1 += MAIN_MEM_r[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 5
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 5
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 5
	t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t8_t0 = S.Task('t4_t8_t0', length=6, delay_cost=1)
	S += t4_t8_t0 >= 5
	t4_t8_t0 += MM[0]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 6
	t1_t1_in += MM_in[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 6
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 6
	t1_t1_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=6, delay_cost=1)
	S += t2_t1 >= 6
	t2_t1 += MM[0]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 7
	t1_t0_in += MM_in[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 7
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 7
	t1_t0_mem1 += MAIN_MEM_r[1]

	t1_t1 = S.Task('t1_t1', length=6, delay_cost=1)
	S += t1_t1 >= 7
	t1_t1 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 8
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 8
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 8
	t0_t1_mem1 += MAIN_MEM_r[1]

	t1_t0 = S.Task('t1_t0', length=6, delay_cost=1)
	S += t1_t0 >= 8
	t1_t0 += MM[0]

	t0_t1 = S.Task('t0_t1', length=6, delay_cost=1)
	S += t0_t1 >= 9
	t0_t1 += MM[0]

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	S += t4_t00_mem0 >= 9
	t4_t00_mem0 += MM_MEM[0]

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	S += t4_t00_mem1 >= 9
	t4_t00_mem1 += MM_MEM[1]

	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	S += t4_t8_t1_in >= 9
	t4_t8_t1_in += MM_in[0]

	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	S += t4_t8_t1_mem0 >= 9
	t4_t8_t1_mem0 += MAIN_MEM_r[0]

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	S += t4_t8_t1_mem1 >= 9
	t4_t8_t1_mem1 += MAIN_MEM_r[1]

	t4_t00 = S.Task('t4_t00', length=1, delay_cost=1)
	S += t4_t00 >= 10
	t4_t00 += MAS[3]

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	S += t4_t0_t5_mem0 >= 10
	t4_t0_t5_mem0 += MM_MEM[0]

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	S += t4_t0_t5_mem1 >= 10
	t4_t0_t5_mem1 += MM_MEM[1]

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	S += t4_t2_t0_in >= 10
	t4_t2_t0_in += MM_in[0]

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	S += t4_t2_t0_mem0 >= 10
	t4_t2_t0_mem0 += MAIN_MEM_r[0]

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	S += t4_t2_t0_mem1 >= 10
	t4_t2_t0_mem1 += MAIN_MEM_r[1]

	t4_t8_t1 = S.Task('t4_t8_t1', length=6, delay_cost=1)
	S += t4_t8_t1 >= 10
	t4_t8_t1 += MM[0]

	t4_t0_t5 = S.Task('t4_t0_t5', length=1, delay_cost=1)
	S += t4_t0_t5 >= 11
	t4_t0_t5 += MAS[1]

	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_in >= 11
	t4_t1_t0_in += MM_in[0]

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_mem0 >= 11
	t4_t1_t0_mem0 += MAIN_MEM_r[0]

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_mem1 >= 11
	t4_t1_t0_mem1 += MAIN_MEM_r[1]

	t4_t2_t0 = S.Task('t4_t2_t0', length=6, delay_cost=1)
	S += t4_t2_t0 >= 11
	t4_t2_t0 += MM[0]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 12
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 12
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 12
	t2_t0_mem1 += MAIN_MEM_r[1]

	t4_t1_t0 = S.Task('t4_t1_t0', length=6, delay_cost=1)
	S += t4_t1_t0 >= 12
	t4_t1_t0 += MM[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 13
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 13
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 13
	t0_t0_mem1 += MAIN_MEM_r[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 13
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 13
	t10_mem1 += MM_MEM[1]

	t2_t0 = S.Task('t2_t0', length=6, delay_cost=1)
	S += t2_t0 >= 13
	t2_t0 += MM[0]

	t0_t0 = S.Task('t0_t0', length=6, delay_cost=1)
	S += t0_t0 >= 14
	t0_t0 += MM[0]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 14
	t10 += MAS[3]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 14
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 14
	t1_t5_mem1 += MM_MEM[1]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 14
	t4_t50_mem0 += MAIN_MEM_r[0]

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 14
	t4_t50_mem1 += MAIN_MEM_r[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 15
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 15
	t0_t2_mem1 += MAIN_MEM_r[1]

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	S += t1_t5 >= 15
	t1_t5 += MAS[2]

	t4_t50 = S.Task('t4_t50', length=1, delay_cost=1)
	S += t4_t50 >= 15
	t4_t50 += MAS[0]

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	S += t4_t8_t5_mem0 >= 15
	t4_t8_t5_mem0 += MM_MEM[0]

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	S += t4_t8_t5_mem1 >= 15
	t4_t8_t5_mem1 += MM_MEM[1]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 16
	t0_t2 += MAS[3]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 16
	t4_t0_t3_mem0 += MAIN_MEM_r[0]

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 16
	t4_t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	S += t4_t20_mem0 >= 16
	t4_t20_mem0 += MM_MEM[0]

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	S += t4_t20_mem1 >= 16
	t4_t20_mem1 += MM_MEM[1]

	t4_t8_t5 = S.Task('t4_t8_t5', length=1, delay_cost=1)
	S += t4_t8_t5 >= 16
	t4_t8_t5 += MAS[1]

	t4_t0_t3 = S.Task('t4_t0_t3', length=1, delay_cost=1)
	S += t4_t0_t3 >= 17
	t4_t0_t3 += MAS[0]

	t4_t20 = S.Task('t4_t20', length=1, delay_cost=1)
	S += t4_t20 >= 17
	t4_t20 += MAS[1]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 17
	t4_t41_mem0 += MAIN_MEM_r[0]

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 17
	t4_t41_mem1 += MAIN_MEM_r[1]

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	S += t4_t80_mem0 >= 17
	t4_t80_mem0 += MM_MEM[0]

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	S += t4_t80_mem1 >= 17
	t4_t80_mem1 += MM_MEM[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 18
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 18
	t0_t3_mem1 += MAIN_MEM_r[1]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 18
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 18
	t2_t5_mem1 += MM_MEM[1]

	t4_t41 = S.Task('t4_t41', length=1, delay_cost=1)
	S += t4_t41 >= 18
	t4_t41 += MAS[0]

	t4_t80 = S.Task('t4_t80', length=1, delay_cost=1)
	S += t4_t80 >= 18
	t4_t80 += MAS[1]

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 19
	t0_t3 += MAS[3]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 19
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 19
	t0_t4_mem0 += MAS_MEM[6]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 19
	t0_t4_mem1 += MAS_MEM[7]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 19
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 19
	t20_mem1 += MM_MEM[1]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 19
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 19
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 19
	t2_t5 += MAS[0]

	t0_t4 = S.Task('t0_t4', length=6, delay_cost=1)
	S += t0_t4 >= 20
	t0_t4 += MM[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 20
	t1_t2_mem0 += MAIN_MEM_r[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 20
	t1_t2_mem1 += MAIN_MEM_r[1]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 20
	t20 += MAS[3]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 20
	t2_t2 += MAS[0]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 20
	t4_t10_mem0 += MM_MEM[0]

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 20
	t4_t10_mem1 += MM_MEM[1]

	t1_t2 = S.Task('t1_t2', length=1, delay_cost=1)
	S += t1_t2 >= 21
	t1_t2 += MAS[2]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 21
	t4_t0_t2_mem0 += MAIN_MEM_r[0]

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 21
	t4_t0_t2_mem1 += MAIN_MEM_r[1]

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	S += t4_t10 >= 21
	t4_t10 += MAS[1]

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	S += t4_t1_t5_mem0 >= 21
	t4_t1_t5_mem0 += MM_MEM[0]

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	S += t4_t1_t5_mem1 >= 21
	t4_t1_t5_mem1 += MM_MEM[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 22
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 22
	t00_mem1 += MM_MEM[1]

	t4_t0_t2 = S.Task('t4_t0_t2', length=1, delay_cost=1)
	S += t4_t0_t2 >= 22
	t4_t0_t2 += MAS[3]

	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	S += t4_t0_t4_in >= 22
	t4_t0_t4_in += MM_in[0]

	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	S += t4_t0_t4_mem0 >= 22
	t4_t0_t4_mem0 += MAS_MEM[6]

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	S += t4_t0_t4_mem1 >= 22
	t4_t0_t4_mem1 += MAS_MEM[1]

	t4_t1_t5 = S.Task('t4_t1_t5', length=1, delay_cost=1)
	S += t4_t1_t5 >= 22
	t4_t1_t5 += MAS[1]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 22
	t4_t51_mem0 += MAIN_MEM_r[0]

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 22
	t4_t51_mem1 += MAIN_MEM_r[1]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 23
	t00 += MAS[1]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 23
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 23
	t0_t5_mem1 += MM_MEM[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 23
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 23
	t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t0_t4 = S.Task('t4_t0_t4', length=6, delay_cost=1)
	S += t4_t0_t4 >= 23
	t4_t0_t4 += MM[0]

	t4_t51 = S.Task('t4_t51', length=1, delay_cost=1)
	S += t4_t51 >= 23
	t4_t51 += MAS[0]

	t4_t6_t1_in = S.Task('t4_t6_t1_in', length=1, delay_cost=1)
	S += t4_t6_t1_in >= 23
	t4_t6_t1_in += MM_in[0]

	t4_t6_t1_mem0 = S.Task('t4_t6_t1_mem0', length=1, delay_cost=1)
	S += t4_t6_t1_mem0 >= 23
	t4_t6_t1_mem0 += MAS_MEM[0]

	t4_t6_t1_mem1 = S.Task('t4_t6_t1_mem1', length=1, delay_cost=1)
	S += t4_t6_t1_mem1 >= 23
	t4_t6_t1_mem1 += MAS_MEM[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 24
	t0_t5 += MAS[2]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 24
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 24
	t1_t3_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 24
	t2_t3 += MAS[0]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 24
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 24
	t2_t4_mem0 += MAS_MEM[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 24
	t2_t4_mem1 += MAS_MEM[1]

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	S += t4_t2_t5_mem0 >= 24
	t4_t2_t5_mem0 += MM_MEM[0]

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	S += t4_t2_t5_mem1 >= 24
	t4_t2_t5_mem1 += MM_MEM[1]

	t4_t6_t1 = S.Task('t4_t6_t1', length=6, delay_cost=1)
	S += t4_t6_t1 >= 24
	t4_t6_t1 += MM[0]

	t1_t3 = S.Task('t1_t3', length=1, delay_cost=1)
	S += t1_t3 >= 25
	t1_t3 += MAS[0]

	t1_t4_in = S.Task('t1_t4_in', length=1, delay_cost=1)
	S += t1_t4_in >= 25
	t1_t4_in += MM_in[0]

	t1_t4_mem0 = S.Task('t1_t4_mem0', length=1, delay_cost=1)
	S += t1_t4_mem0 >= 25
	t1_t4_mem0 += MAS_MEM[4]

	t1_t4_mem1 = S.Task('t1_t4_mem1', length=1, delay_cost=1)
	S += t1_t4_mem1 >= 25
	t1_t4_mem1 += MAS_MEM[1]

	t2_t4 = S.Task('t2_t4', length=6, delay_cost=1)
	S += t2_t4 >= 25
	t2_t4 += MM[0]

	t4_t2_t5 = S.Task('t4_t2_t5', length=1, delay_cost=1)
	S += t4_t2_t5 >= 25
	t4_t2_t5 += MAS[1]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 25
	t4_t40_mem0 += MAIN_MEM_r[0]

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 25
	t4_t40_mem1 += MAIN_MEM_r[1]

	t1_t4 = S.Task('t1_t4', length=6, delay_cost=1)
	S += t1_t4 >= 26
	t1_t4 += MM[0]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 26
	t4_t2_t3_mem0 += MAIN_MEM_r[0]

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 26
	t4_t2_t3_mem1 += MAIN_MEM_r[1]

	t4_t40 = S.Task('t4_t40', length=1, delay_cost=1)
	S += t4_t40 >= 26
	t4_t40 += MAS[0]

	t4_t6_t0_in = S.Task('t4_t6_t0_in', length=1, delay_cost=1)
	S += t4_t6_t0_in >= 26
	t4_t6_t0_in += MM_in[0]

	t4_t6_t0_mem0 = S.Task('t4_t6_t0_mem0', length=1, delay_cost=1)
	S += t4_t6_t0_mem0 >= 26
	t4_t6_t0_mem0 += MAS_MEM[0]

	t4_t6_t0_mem1 = S.Task('t4_t6_t0_mem1', length=1, delay_cost=1)
	S += t4_t6_t0_mem1 >= 26
	t4_t6_t0_mem1 += MAS_MEM[1]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 27
	t4_t2_t2_mem0 += MAIN_MEM_r[0]

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 27
	t4_t2_t2_mem1 += MAIN_MEM_r[1]

	t4_t2_t3 = S.Task('t4_t2_t3', length=1, delay_cost=1)
	S += t4_t2_t3 >= 27
	t4_t2_t3 += MAS[3]

	t4_t6_t0 = S.Task('t4_t6_t0', length=6, delay_cost=1)
	S += t4_t6_t0 >= 27
	t4_t6_t0 += MM[0]

	t4_t6_t2_mem0 = S.Task('t4_t6_t2_mem0', length=1, delay_cost=1)
	S += t4_t6_t2_mem0 >= 27
	t4_t6_t2_mem0 += MAS_MEM[0]

	t4_t6_t2_mem1 = S.Task('t4_t6_t2_mem1', length=1, delay_cost=1)
	S += t4_t6_t2_mem1 >= 27
	t4_t6_t2_mem1 += MAS_MEM[1]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 28
	t4_t1_t3_mem0 += MAIN_MEM_r[0]

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 28
	t4_t1_t3_mem1 += MAIN_MEM_r[1]

	t4_t2_t2 = S.Task('t4_t2_t2', length=1, delay_cost=1)
	S += t4_t2_t2 >= 28
	t4_t2_t2 += MAS[0]

	t4_t2_t4_in = S.Task('t4_t2_t4_in', length=1, delay_cost=1)
	S += t4_t2_t4_in >= 28
	t4_t2_t4_in += MM_in[0]

	t4_t2_t4_mem0 = S.Task('t4_t2_t4_mem0', length=1, delay_cost=1)
	S += t4_t2_t4_mem0 >= 28
	t4_t2_t4_mem0 += MAS_MEM[0]

	t4_t2_t4_mem1 = S.Task('t4_t2_t4_mem1', length=1, delay_cost=1)
	S += t4_t2_t4_mem1 >= 28
	t4_t2_t4_mem1 += MAS_MEM[7]

	t4_t6_t2 = S.Task('t4_t6_t2', length=1, delay_cost=1)
	S += t4_t6_t2 >= 28
	t4_t6_t2 += MAS[2]

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t2_mem0 >= 29
	t4_t1_t2_mem0 += MAIN_MEM_r[0]

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t2_mem1 >= 29
	t4_t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_t3 = S.Task('t4_t1_t3', length=1, delay_cost=1)
	S += t4_t1_t3 >= 29
	t4_t1_t3 += MAS[0]

	t4_t2_t4 = S.Task('t4_t2_t4', length=6, delay_cost=1)
	S += t4_t2_t4 >= 29
	t4_t2_t4 += MM[0]

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	S += t4_t6_t3_mem0 >= 29
	t4_t6_t3_mem0 += MAS_MEM[0]

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	S += t4_t6_t3_mem1 >= 29
	t4_t6_t3_mem1 += MAS_MEM[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 30
	t101_mem0 += MAIN_MEM_r[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 30
	t101_mem1 += MAIN_MEM_r[1]

	t4_t1_t2 = S.Task('t4_t1_t2', length=1, delay_cost=1)
	S += t4_t1_t2 >= 30
	t4_t1_t2 += MAS[0]

	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	S += t4_t1_t4_in >= 30
	t4_t1_t4_in += MM_in[0]

	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	S += t4_t1_t4_mem0 >= 30
	t4_t1_t4_mem0 += MAS_MEM[0]

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	S += t4_t1_t4_mem1 >= 30
	t4_t1_t4_mem1 += MAS_MEM[1]

	t4_t6_t3 = S.Task('t4_t6_t3', length=1, delay_cost=1)
	S += t4_t6_t3 >= 30
	t4_t6_t3 += MAS[2]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 31
	t101 += MAS[2]

	t4_t1_t4 = S.Task('t4_t1_t4', length=6, delay_cost=1)
	S += t4_t1_t4 >= 31
	t4_t1_t4 += MM[0]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 31
	t5_t0_t2_mem0 += MAIN_MEM_r[0]

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 31
	t5_t0_t2_mem1 += MAIN_MEM_r[1]

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	S += t5_t0_t2 >= 32
	t5_t0_t2 += MAS[2]

	t5_t8_t2_mem0 = S.Task('t5_t8_t2_mem0', length=1, delay_cost=1)
	S += t5_t8_t2_mem0 >= 32
	t5_t8_t2_mem0 += MAIN_MEM_r[0]

	t5_t8_t2_mem1 = S.Task('t5_t8_t2_mem1', length=1, delay_cost=1)
	S += t5_t8_t2_mem1 >= 32
	t5_t8_t2_mem1 += MAIN_MEM_r[1]

	t5_t8_t2 = S.Task('t5_t8_t2', length=1, delay_cost=1)
	S += t5_t8_t2 >= 33
	t5_t8_t2 += MAS[3]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 33
	t80_mem0 += MAIN_MEM_r[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 33
	t80_mem1 += MAIN_MEM_r[1]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 34
	t80 += MAS[3]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 34
	t90_mem0 += MAIN_MEM_r[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 34
	t90_mem1 += MAIN_MEM_r[1]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 35
	t4_t8_t3_mem0 += MAIN_MEM_r[0]

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 35
	t4_t8_t3_mem1 += MAIN_MEM_r[1]

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	S += t5_t50_mem0 >= 35
	t5_t50_mem0 += MAS_MEM[6]

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	S += t5_t50_mem1 >= 35
	t5_t50_mem1 += MAS_MEM[5]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 35
	t90 += MAS[2]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 36
	t4_t8_t2_mem0 += MAIN_MEM_r[0]

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 36
	t4_t8_t2_mem1 += MAIN_MEM_r[1]

	t4_t8_t3 = S.Task('t4_t8_t3', length=1, delay_cost=1)
	S += t4_t8_t3 >= 36
	t4_t8_t3 += MAS[3]

	t5_t50 = S.Task('t5_t50', length=1, delay_cost=1)
	S += t5_t50 >= 36
	t5_t50 += MAS[0]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 37
	t100_mem0 += MAIN_MEM_r[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 37
	t100_mem1 += MAIN_MEM_r[1]

	t4_t8_t2 = S.Task('t4_t8_t2', length=1, delay_cost=1)
	S += t4_t8_t2 >= 37
	t4_t8_t2 += MAS[2]

	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	S += t4_t8_t4_in >= 37
	t4_t8_t4_in += MM_in[0]

	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	S += t4_t8_t4_mem0 >= 37
	t4_t8_t4_mem0 += MAS_MEM[4]

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	S += t4_t8_t4_mem1 >= 37
	t4_t8_t4_mem1 += MAS_MEM[7]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 38
	t100 += MAS[3]

	t4_t8_t4 = S.Task('t4_t8_t4', length=6, delay_cost=1)
	S += t4_t8_t4 >= 38
	t4_t8_t4 += MM[0]

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	S += t5_t2_t3_mem0 >= 38
	t5_t2_t3_mem0 += MAS_MEM[6]

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	S += t5_t2_t3_mem1 >= 38
	t5_t2_t3_mem1 += MAS_MEM[5]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 38
	t71_mem0 += MAIN_MEM_r[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 38
	t71_mem1 += MAIN_MEM_r[1]

	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	S += t5_t2_t1_in >= 39
	t5_t2_t1_in += MM_in[0]

	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	S += t5_t2_t1_mem0 >= 39
	t5_t2_t1_mem0 += MAS_MEM[6]

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	S += t5_t2_t1_mem1 >= 39
	t5_t2_t1_mem1 += MAS_MEM[5]

	t5_t2_t3 = S.Task('t5_t2_t3', length=1, delay_cost=1)
	S += t5_t2_t3 >= 39
	t5_t2_t3 += MAS[0]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 39
	t71 += MAS[3]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 39
	t81_mem0 += MAIN_MEM_r[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 39
	t81_mem1 += MAIN_MEM_r[1]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 40
	t5_t0_t3_mem0 += MAS_MEM[6]

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 40
	t5_t0_t3_mem1 += MAS_MEM[7]

	t5_t2_t1 = S.Task('t5_t2_t1', length=6, delay_cost=1)
	S += t5_t2_t1 >= 40
	t5_t2_t1 += MM[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 40
	t70_mem0 += MAIN_MEM_r[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 40
	t70_mem1 += MAIN_MEM_r[1]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 40
	t81 += MAS[3]

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	S += t5_t0_t3 >= 41
	t5_t0_t3 += MAS[2]

	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	S += t5_t2_t0_in >= 41
	t5_t2_t0_in += MM_in[0]

	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	S += t5_t2_t0_mem0 >= 41
	t5_t2_t0_mem0 += MAS_MEM[2]

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	S += t5_t2_t0_mem1 >= 41
	t5_t2_t0_mem1 += MAS_MEM[7]

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	S += t5_t8_t3_mem0 >= 41
	t5_t8_t3_mem0 += MAS_MEM[6]

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	S += t5_t8_t3_mem1 >= 41
	t5_t8_t3_mem1 += MAS_MEM[5]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 41
	t70 += MAS[1]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 41
	t91_mem0 += MAIN_MEM_r[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 41
	t91_mem1 += MAIN_MEM_r[1]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 42
	t5_t1_t0_in += MM_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 42
	t5_t1_t0_mem0 += MAS_MEM[2]

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 42
	t5_t1_t0_mem1 += MAS_MEM[5]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 42
	t5_t1_t3_mem0 += MAS_MEM[4]

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 42
	t5_t1_t3_mem1 += MAS_MEM[3]

	t5_t2_t0 = S.Task('t5_t2_t0', length=6, delay_cost=1)
	S += t5_t2_t0 >= 42
	t5_t2_t0 += MM[0]

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	S += t5_t41_mem0 >= 42
	t5_t41_mem0 += MAIN_MEM_r[0]

	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	S += t5_t41_mem1 >= 42
	t5_t41_mem1 += MAS_MEM[7]

	t5_t8_t3 = S.Task('t5_t8_t3', length=1, delay_cost=1)
	S += t5_t8_t3 >= 42
	t5_t8_t3 += MAS[2]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 42
	t91 += MAS[1]

	t5_t1_t0 = S.Task('t5_t1_t0', length=6, delay_cost=1)
	S += t5_t1_t0 >= 43
	t5_t1_t0 += MM[0]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 43
	t5_t1_t2_mem0 += MAS_MEM[2]

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 43
	t5_t1_t2_mem1 += MAS_MEM[7]

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	S += t5_t1_t3 >= 43
	t5_t1_t3 += MAS[1]

	t5_t41 = S.Task('t5_t41', length=1, delay_cost=1)
	S += t5_t41 >= 43
	t5_t41 += MAS[0]

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	S += t5_t51_mem0 >= 43
	t5_t51_mem0 += MAS_MEM[6]

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	S += t5_t51_mem1 >= 43
	t5_t51_mem1 += MAS_MEM[3]

	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	S += t5_t8_t1_in >= 43
	t5_t8_t1_in += MM_in[0]

	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	S += t5_t8_t1_mem0 >= 43
	t5_t8_t1_mem0 += MAIN_MEM_r[0]

	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	S += t5_t8_t1_mem1 >= 43
	t5_t8_t1_mem1 += MAS_MEM[5]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 44
	t5_t1_t1_in += MM_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 44
	t5_t1_t1_mem0 += MAS_MEM[6]

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 44
	t5_t1_t1_mem1 += MAS_MEM[3]

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	S += t5_t1_t2 >= 44
	t5_t1_t2 += MAS[2]

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_t2_mem0 >= 44
	t5_t2_t2_mem0 += MAS_MEM[2]

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_t2_mem1 >= 44
	t5_t2_t2_mem1 += MAS_MEM[7]

	t5_t51 = S.Task('t5_t51', length=1, delay_cost=1)
	S += t5_t51 >= 44
	t5_t51 += MAS[3]

	t5_t8_t1 = S.Task('t5_t8_t1', length=6, delay_cost=1)
	S += t5_t8_t1 >= 44
	t5_t8_t1 += MM[0]

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 45
	t5_t0_t0_in += MM_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 45
	t5_t0_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 45
	t5_t0_t0_mem1 += MAS_MEM[7]

	t5_t1_t1 = S.Task('t5_t1_t1', length=6, delay_cost=1)
	S += t5_t1_t1 >= 45
	t5_t1_t1 += MM[0]

	t5_t2_t2 = S.Task('t5_t2_t2', length=1, delay_cost=1)
	S += t5_t2_t2 >= 45
	t5_t2_t2 += MAS[3]

	t5_t0_t0 = S.Task('t5_t0_t0', length=6, delay_cost=1)
	S += t5_t0_t0 >= 46
	t5_t0_t0 += MM[0]

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 46
	t5_t0_t1_in += MM_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 46
	t5_t0_t1_mem0 += MAIN_MEM_r[0]

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 46
	t5_t0_t1_mem1 += MAS_MEM[7]

	t5_t0_t1 = S.Task('t5_t0_t1', length=6, delay_cost=1)
	S += t5_t0_t1 >= 47
	t5_t0_t1 += MM[0]

	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	S += t5_t8_t0_in >= 47
	t5_t8_t0_in += MM_in[0]

	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	S += t5_t8_t0_mem0 >= 47
	t5_t8_t0_mem0 += MAIN_MEM_r[0]

	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	S += t5_t8_t0_mem1 >= 47
	t5_t8_t0_mem1 += MAS_MEM[7]

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	S += t5_t40_mem0 >= 48
	t5_t40_mem0 += MAIN_MEM_r[0]

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	S += t5_t40_mem1 >= 48
	t5_t40_mem1 += MAS_MEM[3]

	t5_t8_t0 = S.Task('t5_t8_t0', length=6, delay_cost=1)
	S += t5_t8_t0 >= 48
	t5_t8_t0 += MM[0]

	t5_t40 = S.Task('t5_t40', length=1, delay_cost=1)
	S += t5_t40 >= 49
	t5_t40 += MAS[3]


	# new tasks
	t11 = S.Task('t11', length=1, delay_cost=1)
	t11 += alt(MAS)
	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += MM_MEM[0]
	S += 31 < t11_mem0
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += MAS_MEM[5]
	S += 15 < t11_mem1
	S += t11_mem1 <= t11

	t21 = S.Task('t21', length=1, delay_cost=1)
	t21 += alt(MAS)
	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MM_MEM[0]
	S += 30 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAS_MEM[1]
	S += 19 < t21_mem1
	S += t21_mem1 <= t21

	t01 = S.Task('t01', length=1, delay_cost=1)
	t01 += alt(MAS)
	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MM_MEM[0]
	S += 25 < t01_mem0
	S += t01_mem0 <= t01

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	t01_mem1 += MAS_MEM[5]
	S += 24 < t01_mem1
	S += t01_mem1 <= t01

	t4_t01 = S.Task('t4_t01', length=1, delay_cost=1)
	t4_t01 += alt(MAS)
	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	t4_t01_mem0 += MM_MEM[0]
	S += 28 < t4_t01_mem0
	S += t4_t01_mem0 <= t4_t01

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	t4_t01_mem1 += MAS_MEM[3]
	S += 11 < t4_t01_mem1
	S += t4_t01_mem1 <= t4_t01

	t4_t11 = S.Task('t4_t11', length=1, delay_cost=1)
	t4_t11 += alt(MAS)
	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	t4_t11_mem0 += MM_MEM[0]
	S += 36 < t4_t11_mem0
	S += t4_t11_mem0 <= t4_t11

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	t4_t11_mem1 += MAS_MEM[3]
	S += 22 < t4_t11_mem1
	S += t4_t11_mem1 <= t4_t11

	t4_t21 = S.Task('t4_t21', length=1, delay_cost=1)
	t4_t21 += alt(MAS)
	t4_t21_mem0 = S.Task('t4_t21_mem0', length=1, delay_cost=1)
	t4_t21_mem0 += MM_MEM[0]
	S += 34 < t4_t21_mem0
	S += t4_t21_mem0 <= t4_t21

	t4_t21_mem1 = S.Task('t4_t21_mem1', length=1, delay_cost=1)
	t4_t21_mem1 += MAS_MEM[3]
	S += 25 < t4_t21_mem1
	S += t4_t21_mem1 <= t4_t21

	t4_t6_t4 = S.Task('t4_t6_t4', length=6, delay_cost=1)
	t4_t6_t4 += alt(MM)
	t4_t6_t4_in = S.Task('t4_t6_t4_in', length=1, delay_cost=1)
	t4_t6_t4_in += alt(MM_in)
	S += t4_t6_t4_in*MM_in[0]<=t4_t6_t4*MM[0]
	t4_t6_t4_mem0 = S.Task('t4_t6_t4_mem0', length=1, delay_cost=1)
	t4_t6_t4_mem0 += MAS_MEM[4]
	S += 28 < t4_t6_t4_mem0
	S += t4_t6_t4_mem0 <= t4_t6_t4

	t4_t6_t4_mem1 = S.Task('t4_t6_t4_mem1', length=1, delay_cost=1)
	t4_t6_t4_mem1 += MAS_MEM[5]
	S += 30 < t4_t6_t4_mem1
	S += t4_t6_t4_mem1 <= t4_t6_t4

	t4_t60 = S.Task('t4_t60', length=1, delay_cost=1)
	t4_t60 += alt(MAS)
	t4_t60_mem0 = S.Task('t4_t60_mem0', length=1, delay_cost=1)
	t4_t60_mem0 += MM_MEM[0]
	S += 32 < t4_t60_mem0
	S += t4_t60_mem0 <= t4_t60

	t4_t60_mem1 = S.Task('t4_t60_mem1', length=1, delay_cost=1)
	t4_t60_mem1 += MM_MEM[1]
	S += 29 < t4_t60_mem1
	S += t4_t60_mem1 <= t4_t60

	t4_t6_t5 = S.Task('t4_t6_t5', length=1, delay_cost=1)
	t4_t6_t5 += alt(MAS)
	t4_t6_t5_mem0 = S.Task('t4_t6_t5_mem0', length=1, delay_cost=1)
	t4_t6_t5_mem0 += MM_MEM[0]
	S += 32 < t4_t6_t5_mem0
	S += t4_t6_t5_mem0 <= t4_t6_t5

	t4_t6_t5_mem1 = S.Task('t4_t6_t5_mem1', length=1, delay_cost=1)
	t4_t6_t5_mem1 += MM_MEM[1]
	S += 29 < t4_t6_t5_mem1
	S += t4_t6_t5_mem1 <= t4_t6_t5

	t4_t70 = S.Task('t4_t70', length=1, delay_cost=1)
	t4_t70 += alt(MAS)
	t4_t70_mem0 = S.Task('t4_t70_mem0', length=1, delay_cost=1)
	t4_t70_mem0 += MAS_MEM[6]
	S += 10 < t4_t70_mem0
	S += t4_t70_mem0 <= t4_t70

	t4_t70_mem1 = S.Task('t4_t70_mem1', length=1, delay_cost=1)
	t4_t70_mem1 += MAS_MEM[3]
	S += 21 < t4_t70_mem1
	S += t4_t70_mem1 <= t4_t70

	t4_t81 = S.Task('t4_t81', length=1, delay_cost=1)
	t4_t81 += alt(MAS)
	t4_t81_mem0 = S.Task('t4_t81_mem0', length=1, delay_cost=1)
	t4_t81_mem0 += MM_MEM[0]
	S += 43 < t4_t81_mem0
	S += t4_t81_mem0 <= t4_t81

	t4_t81_mem1 = S.Task('t4_t81_mem1', length=1, delay_cost=1)
	t4_t81_mem1 += MAS_MEM[3]
	S += 16 < t4_t81_mem1
	S += t4_t81_mem1 <= t4_t81

	t420 = S.Task('t420', length=1, delay_cost=1)
	t420 += alt(MAS)
	t420_mem0 = S.Task('t420_mem0', length=1, delay_cost=1)
	t420_mem0 += MAS_MEM[2]
	S += 18 < t420_mem0
	S += t420_mem0 <= t420

	t420_mem1 = S.Task('t420_mem1', length=1, delay_cost=1)
	t420_mem1 += MAS_MEM[3]
	S += 21 < t420_mem1
	S += t420_mem1 <= t420

	t5_t0_t4 = S.Task('t5_t0_t4', length=6, delay_cost=1)
	t5_t0_t4 += alt(MM)
	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	t5_t0_t4_in += alt(MM_in)
	S += t5_t0_t4_in*MM_in[0]<=t5_t0_t4*MM[0]
	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	t5_t0_t4_mem0 += MAS_MEM[4]
	S += 32 < t5_t0_t4_mem0
	S += t5_t0_t4_mem0 <= t5_t0_t4

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	t5_t0_t4_mem1 += MAS_MEM[5]
	S += 41 < t5_t0_t4_mem1
	S += t5_t0_t4_mem1 <= t5_t0_t4

	t5_t00 = S.Task('t5_t00', length=1, delay_cost=1)
	t5_t00 += alt(MAS)
	t5_t00_mem0 = S.Task('t5_t00_mem0', length=1, delay_cost=1)
	t5_t00_mem0 += MM_MEM[0]
	S += 51 < t5_t00_mem0
	S += t5_t00_mem0 <= t5_t00

	t5_t00_mem1 = S.Task('t5_t00_mem1', length=1, delay_cost=1)
	t5_t00_mem1 += MM_MEM[1]
	S += 52 < t5_t00_mem1
	S += t5_t00_mem1 <= t5_t00

	t5_t0_t5 = S.Task('t5_t0_t5', length=1, delay_cost=1)
	t5_t0_t5 += alt(MAS)
	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	t5_t0_t5_mem0 += MM_MEM[0]
	S += 51 < t5_t0_t5_mem0
	S += t5_t0_t5_mem0 <= t5_t0_t5

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	t5_t0_t5_mem1 += MM_MEM[1]
	S += 52 < t5_t0_t5_mem1
	S += t5_t0_t5_mem1 <= t5_t0_t5

	t5_t1_t4 = S.Task('t5_t1_t4', length=6, delay_cost=1)
	t5_t1_t4 += alt(MM)
	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	t5_t1_t4_in += alt(MM_in)
	S += t5_t1_t4_in*MM_in[0]<=t5_t1_t4*MM[0]
	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	t5_t1_t4_mem0 += MAS_MEM[4]
	S += 44 < t5_t1_t4_mem0
	S += t5_t1_t4_mem0 <= t5_t1_t4

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	t5_t1_t4_mem1 += MAS_MEM[3]
	S += 43 < t5_t1_t4_mem1
	S += t5_t1_t4_mem1 <= t5_t1_t4

	t5_t10 = S.Task('t5_t10', length=1, delay_cost=1)
	t5_t10 += alt(MAS)
	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	t5_t10_mem0 += MM_MEM[0]
	S += 48 < t5_t10_mem0
	S += t5_t10_mem0 <= t5_t10

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	t5_t10_mem1 += MM_MEM[1]
	S += 50 < t5_t10_mem1
	S += t5_t10_mem1 <= t5_t10

	t5_t1_t5 = S.Task('t5_t1_t5', length=1, delay_cost=1)
	t5_t1_t5 += alt(MAS)
	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	t5_t1_t5_mem0 += MM_MEM[0]
	S += 48 < t5_t1_t5_mem0
	S += t5_t1_t5_mem0 <= t5_t1_t5

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	t5_t1_t5_mem1 += MM_MEM[1]
	S += 50 < t5_t1_t5_mem1
	S += t5_t1_t5_mem1 <= t5_t1_t5

	t5_t2_t4 = S.Task('t5_t2_t4', length=6, delay_cost=1)
	t5_t2_t4 += alt(MM)
	t5_t2_t4_in = S.Task('t5_t2_t4_in', length=1, delay_cost=1)
	t5_t2_t4_in += alt(MM_in)
	S += t5_t2_t4_in*MM_in[0]<=t5_t2_t4*MM[0]
	t5_t2_t4_mem0 = S.Task('t5_t2_t4_mem0', length=1, delay_cost=1)
	t5_t2_t4_mem0 += MAS_MEM[6]
	S += 45 < t5_t2_t4_mem0
	S += t5_t2_t4_mem0 <= t5_t2_t4

	t5_t2_t4_mem1 = S.Task('t5_t2_t4_mem1', length=1, delay_cost=1)
	t5_t2_t4_mem1 += MAS_MEM[1]
	S += 39 < t5_t2_t4_mem1
	S += t5_t2_t4_mem1 <= t5_t2_t4

	t5_t20 = S.Task('t5_t20', length=1, delay_cost=1)
	t5_t20 += alt(MAS)
	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	t5_t20_mem0 += MM_MEM[0]
	S += 47 < t5_t20_mem0
	S += t5_t20_mem0 <= t5_t20

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	t5_t20_mem1 += MM_MEM[1]
	S += 45 < t5_t20_mem1
	S += t5_t20_mem1 <= t5_t20

	t5_t2_t5 = S.Task('t5_t2_t5', length=1, delay_cost=1)
	t5_t2_t5 += alt(MAS)
	t5_t2_t5_mem0 = S.Task('t5_t2_t5_mem0', length=1, delay_cost=1)
	t5_t2_t5_mem0 += MM_MEM[0]
	S += 47 < t5_t2_t5_mem0
	S += t5_t2_t5_mem0 <= t5_t2_t5

	t5_t2_t5_mem1 = S.Task('t5_t2_t5_mem1', length=1, delay_cost=1)
	t5_t2_t5_mem1 += MM_MEM[1]
	S += 45 < t5_t2_t5_mem1
	S += t5_t2_t5_mem1 <= t5_t2_t5

	t5_t6_t0 = S.Task('t5_t6_t0', length=6, delay_cost=1)
	t5_t6_t0 += alt(MM)
	t5_t6_t0_in = S.Task('t5_t6_t0_in', length=1, delay_cost=1)
	t5_t6_t0_in += alt(MM_in)
	S += t5_t6_t0_in*MM_in[0]<=t5_t6_t0*MM[0]
	t5_t6_t0_mem0 = S.Task('t5_t6_t0_mem0', length=1, delay_cost=1)
	t5_t6_t0_mem0 += MAS_MEM[6]
	S += 49 < t5_t6_t0_mem0
	S += t5_t6_t0_mem0 <= t5_t6_t0

	t5_t6_t0_mem1 = S.Task('t5_t6_t0_mem1', length=1, delay_cost=1)
	t5_t6_t0_mem1 += MAS_MEM[1]
	S += 36 < t5_t6_t0_mem1
	S += t5_t6_t0_mem1 <= t5_t6_t0

	t5_t6_t1 = S.Task('t5_t6_t1', length=6, delay_cost=1)
	t5_t6_t1 += alt(MM)
	t5_t6_t1_in = S.Task('t5_t6_t1_in', length=1, delay_cost=1)
	t5_t6_t1_in += alt(MM_in)
	S += t5_t6_t1_in*MM_in[0]<=t5_t6_t1*MM[0]
	t5_t6_t1_mem0 = S.Task('t5_t6_t1_mem0', length=1, delay_cost=1)
	t5_t6_t1_mem0 += MAS_MEM[0]
	S += 43 < t5_t6_t1_mem0
	S += t5_t6_t1_mem0 <= t5_t6_t1

	t5_t6_t1_mem1 = S.Task('t5_t6_t1_mem1', length=1, delay_cost=1)
	t5_t6_t1_mem1 += MAS_MEM[7]
	S += 44 < t5_t6_t1_mem1
	S += t5_t6_t1_mem1 <= t5_t6_t1

	t5_t6_t2 = S.Task('t5_t6_t2', length=1, delay_cost=1)
	t5_t6_t2 += alt(MAS)
	t5_t6_t2_mem0 = S.Task('t5_t6_t2_mem0', length=1, delay_cost=1)
	t5_t6_t2_mem0 += MAS_MEM[6]
	S += 49 < t5_t6_t2_mem0
	S += t5_t6_t2_mem0 <= t5_t6_t2

	t5_t6_t2_mem1 = S.Task('t5_t6_t2_mem1', length=1, delay_cost=1)
	t5_t6_t2_mem1 += MAS_MEM[1]
	S += 43 < t5_t6_t2_mem1
	S += t5_t6_t2_mem1 <= t5_t6_t2

	t5_t6_t3 = S.Task('t5_t6_t3', length=1, delay_cost=1)
	t5_t6_t3 += alt(MAS)
	t5_t6_t3_mem0 = S.Task('t5_t6_t3_mem0', length=1, delay_cost=1)
	t5_t6_t3_mem0 += MAS_MEM[0]
	S += 36 < t5_t6_t3_mem0
	S += t5_t6_t3_mem0 <= t5_t6_t3

	t5_t6_t3_mem1 = S.Task('t5_t6_t3_mem1', length=1, delay_cost=1)
	t5_t6_t3_mem1 += MAS_MEM[7]
	S += 44 < t5_t6_t3_mem1
	S += t5_t6_t3_mem1 <= t5_t6_t3

	t5_t8_t4 = S.Task('t5_t8_t4', length=6, delay_cost=1)
	t5_t8_t4 += alt(MM)
	t5_t8_t4_in = S.Task('t5_t8_t4_in', length=1, delay_cost=1)
	t5_t8_t4_in += alt(MM_in)
	S += t5_t8_t4_in*MM_in[0]<=t5_t8_t4*MM[0]
	t5_t8_t4_mem0 = S.Task('t5_t8_t4_mem0', length=1, delay_cost=1)
	t5_t8_t4_mem0 += MAS_MEM[6]
	S += 33 < t5_t8_t4_mem0
	S += t5_t8_t4_mem0 <= t5_t8_t4

	t5_t8_t4_mem1 = S.Task('t5_t8_t4_mem1', length=1, delay_cost=1)
	t5_t8_t4_mem1 += MAS_MEM[5]
	S += 42 < t5_t8_t4_mem1
	S += t5_t8_t4_mem1 <= t5_t8_t4

	t5_t80 = S.Task('t5_t80', length=1, delay_cost=1)
	t5_t80 += alt(MAS)
	t5_t80_mem0 = S.Task('t5_t80_mem0', length=1, delay_cost=1)
	t5_t80_mem0 += MM_MEM[0]
	S += 53 < t5_t80_mem0
	S += t5_t80_mem0 <= t5_t80

	t5_t80_mem1 = S.Task('t5_t80_mem1', length=1, delay_cost=1)
	t5_t80_mem1 += MM_MEM[1]
	S += 49 < t5_t80_mem1
	S += t5_t80_mem1 <= t5_t80

	t5_t8_t5 = S.Task('t5_t8_t5', length=1, delay_cost=1)
	t5_t8_t5 += alt(MAS)
	t5_t8_t5_mem0 = S.Task('t5_t8_t5_mem0', length=1, delay_cost=1)
	t5_t8_t5_mem0 += MM_MEM[0]
	S += 53 < t5_t8_t5_mem0
	S += t5_t8_t5_mem0 <= t5_t8_t5

	t5_t8_t5_mem1 = S.Task('t5_t8_t5_mem1', length=1, delay_cost=1)
	t5_t8_t5_mem1 += MM_MEM[1]
	S += 49 < t5_t8_t5_mem1
	S += t5_t8_t5_mem1 <= t5_t8_t5

	t30 = S.Task('t30', length=1, delay_cost=1)
	t30 += alt(MAS)
	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MAS_MEM[2]
	S += 23 < t30_mem0
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t30_mem1*MAS_MEM[1]
	S += (t01*MAS[1])-1 < t30_mem1*MAS_MEM[3]
	S += (t01*MAS[2])-1 < t30_mem1*MAS_MEM[5]
	S += (t01*MAS[3])-1 < t30_mem1*MAS_MEM[7]
	S += t30_mem1 <= t30

	t31 = S.Task('t31', length=1, delay_cost=1)
	t31 += alt(MAS)
	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t31_mem0*MAS_MEM[0]
	S += (t01*MAS[1])-1 < t31_mem0*MAS_MEM[2]
	S += (t01*MAS[2])-1 < t31_mem0*MAS_MEM[4]
	S += (t01*MAS[3])-1 < t31_mem0*MAS_MEM[6]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += MAS_MEM[3]
	S += 23 < t31_mem1
	S += t31_mem1 <= t31

	t4_t100 = S.Task('t4_t100', length=1, delay_cost=1)
	t4_t100 += alt(MAS)
	t4_t100_mem0 = S.Task('t4_t100_mem0', length=1, delay_cost=1)
	t4_t100_mem0 += MAS_MEM[2]
	S += 17 < t4_t100_mem0
	S += t4_t100_mem0 <= t4_t100

	t4_t100_mem1 = S.Task('t4_t100_mem1', length=1, delay_cost=1)
	t4_t100_mem1 += alt(MAS_MEM)
	S += (t4_t21*MAS[0])-1 < t4_t100_mem1*MAS_MEM[1]
	S += (t4_t21*MAS[1])-1 < t4_t100_mem1*MAS_MEM[3]
	S += (t4_t21*MAS[2])-1 < t4_t100_mem1*MAS_MEM[5]
	S += (t4_t21*MAS[3])-1 < t4_t100_mem1*MAS_MEM[7]
	S += t4_t100_mem1 <= t4_t100

	t4_t101 = S.Task('t4_t101', length=1, delay_cost=1)
	t4_t101 += alt(MAS)
	t4_t101_mem0 = S.Task('t4_t101_mem0', length=1, delay_cost=1)
	t4_t101_mem0 += alt(MAS_MEM)
	S += (t4_t21*MAS[0])-1 < t4_t101_mem0*MAS_MEM[0]
	S += (t4_t21*MAS[1])-1 < t4_t101_mem0*MAS_MEM[2]
	S += (t4_t21*MAS[2])-1 < t4_t101_mem0*MAS_MEM[4]
	S += (t4_t21*MAS[3])-1 < t4_t101_mem0*MAS_MEM[6]
	S += t4_t101_mem0 <= t4_t101

	t4_t101_mem1 = S.Task('t4_t101_mem1', length=1, delay_cost=1)
	t4_t101_mem1 += MAS_MEM[3]
	S += 17 < t4_t101_mem1
	S += t4_t101_mem1 <= t4_t101

	t4_t61 = S.Task('t4_t61', length=1, delay_cost=1)
	t4_t61 += alt(MAS)
	t4_t61_mem0 = S.Task('t4_t61_mem0', length=1, delay_cost=1)
	t4_t61_mem0 += alt(MM_MEM)
	S += (t4_t6_t4*MM[0])-1 < t4_t61_mem0*MM_MEM[0]
	S += t4_t61_mem0 <= t4_t61

	t4_t61_mem1 = S.Task('t4_t61_mem1', length=1, delay_cost=1)
	t4_t61_mem1 += alt(MAS_MEM)
	S += (t4_t6_t5*MAS[0])-1 < t4_t61_mem1*MAS_MEM[1]
	S += (t4_t6_t5*MAS[1])-1 < t4_t61_mem1*MAS_MEM[3]
	S += (t4_t6_t5*MAS[2])-1 < t4_t61_mem1*MAS_MEM[5]
	S += (t4_t6_t5*MAS[3])-1 < t4_t61_mem1*MAS_MEM[7]
	S += t4_t61_mem1 <= t4_t61

	t4_t71 = S.Task('t4_t71', length=1, delay_cost=1)
	t4_t71 += alt(MAS)
	t4_t71_mem0 = S.Task('t4_t71_mem0', length=1, delay_cost=1)
	t4_t71_mem0 += alt(MAS_MEM)
	S += (t4_t01*MAS[0])-1 < t4_t71_mem0*MAS_MEM[0]
	S += (t4_t01*MAS[1])-1 < t4_t71_mem0*MAS_MEM[2]
	S += (t4_t01*MAS[2])-1 < t4_t71_mem0*MAS_MEM[4]
	S += (t4_t01*MAS[3])-1 < t4_t71_mem0*MAS_MEM[6]
	S += t4_t71_mem0 <= t4_t71

	t4_t71_mem1 = S.Task('t4_t71_mem1', length=1, delay_cost=1)
	t4_t71_mem1 += alt(MAS_MEM)
	S += (t4_t11*MAS[0])-1 < t4_t71_mem1*MAS_MEM[1]
	S += (t4_t11*MAS[1])-1 < t4_t71_mem1*MAS_MEM[3]
	S += (t4_t11*MAS[2])-1 < t4_t71_mem1*MAS_MEM[5]
	S += (t4_t11*MAS[3])-1 < t4_t71_mem1*MAS_MEM[7]
	S += t4_t71_mem1 <= t4_t71

	t410 = S.Task('t410', length=1, delay_cost=1)
	t410 += alt(MAS)
	t410_mem0 = S.Task('t410_mem0', length=1, delay_cost=1)
	t410_mem0 += alt(MAS_MEM)
	S += (t4_t60*MAS[0])-1 < t410_mem0*MAS_MEM[0]
	S += (t4_t60*MAS[1])-1 < t410_mem0*MAS_MEM[2]
	S += (t4_t60*MAS[2])-1 < t410_mem0*MAS_MEM[4]
	S += (t4_t60*MAS[3])-1 < t410_mem0*MAS_MEM[6]
	S += t410_mem0 <= t410

	t410_mem1 = S.Task('t410_mem1', length=1, delay_cost=1)
	t410_mem1 += alt(MAS_MEM)
	S += (t4_t70*MAS[0])-1 < t410_mem1*MAS_MEM[1]
	S += (t4_t70*MAS[1])-1 < t410_mem1*MAS_MEM[3]
	S += (t4_t70*MAS[2])-1 < t410_mem1*MAS_MEM[5]
	S += (t4_t70*MAS[3])-1 < t410_mem1*MAS_MEM[7]
	S += t410_mem1 <= t410

	t421 = S.Task('t421', length=1, delay_cost=1)
	t421 += alt(MAS)
	t421_mem0 = S.Task('t421_mem0', length=1, delay_cost=1)
	t421_mem0 += alt(MAS_MEM)
	S += (t4_t81*MAS[0])-1 < t421_mem0*MAS_MEM[0]
	S += (t4_t81*MAS[1])-1 < t421_mem0*MAS_MEM[2]
	S += (t4_t81*MAS[2])-1 < t421_mem0*MAS_MEM[4]
	S += (t4_t81*MAS[3])-1 < t421_mem0*MAS_MEM[6]
	S += t421_mem0 <= t421

	t421_mem1 = S.Task('t421_mem1', length=1, delay_cost=1)
	t421_mem1 += alt(MAS_MEM)
	S += (t4_t11*MAS[0])-1 < t421_mem1*MAS_MEM[1]
	S += (t4_t11*MAS[1])-1 < t421_mem1*MAS_MEM[3]
	S += (t4_t11*MAS[2])-1 < t421_mem1*MAS_MEM[5]
	S += (t4_t11*MAS[3])-1 < t421_mem1*MAS_MEM[7]
	S += t421_mem1 <= t421

	t5_t01 = S.Task('t5_t01', length=1, delay_cost=1)
	t5_t01 += alt(MAS)
	t5_t01_mem0 = S.Task('t5_t01_mem0', length=1, delay_cost=1)
	t5_t01_mem0 += alt(MM_MEM)
	S += (t5_t0_t4*MM[0])-1 < t5_t01_mem0*MM_MEM[0]
	S += t5_t01_mem0 <= t5_t01

	t5_t01_mem1 = S.Task('t5_t01_mem1', length=1, delay_cost=1)
	t5_t01_mem1 += alt(MAS_MEM)
	S += (t5_t0_t5*MAS[0])-1 < t5_t01_mem1*MAS_MEM[1]
	S += (t5_t0_t5*MAS[1])-1 < t5_t01_mem1*MAS_MEM[3]
	S += (t5_t0_t5*MAS[2])-1 < t5_t01_mem1*MAS_MEM[5]
	S += (t5_t0_t5*MAS[3])-1 < t5_t01_mem1*MAS_MEM[7]
	S += t5_t01_mem1 <= t5_t01

	t5_t11 = S.Task('t5_t11', length=1, delay_cost=1)
	t5_t11 += alt(MAS)
	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	t5_t11_mem0 += alt(MM_MEM)
	S += (t5_t1_t4*MM[0])-1 < t5_t11_mem0*MM_MEM[0]
	S += t5_t11_mem0 <= t5_t11

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	t5_t11_mem1 += alt(MAS_MEM)
	S += (t5_t1_t5*MAS[0])-1 < t5_t11_mem1*MAS_MEM[1]
	S += (t5_t1_t5*MAS[1])-1 < t5_t11_mem1*MAS_MEM[3]
	S += (t5_t1_t5*MAS[2])-1 < t5_t11_mem1*MAS_MEM[5]
	S += (t5_t1_t5*MAS[3])-1 < t5_t11_mem1*MAS_MEM[7]
	S += t5_t11_mem1 <= t5_t11

	t5_t21 = S.Task('t5_t21', length=1, delay_cost=1)
	t5_t21 += alt(MAS)
	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	t5_t21_mem0 += alt(MM_MEM)
	S += (t5_t2_t4*MM[0])-1 < t5_t21_mem0*MM_MEM[0]
	S += t5_t21_mem0 <= t5_t21

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	t5_t21_mem1 += alt(MAS_MEM)
	S += (t5_t2_t5*MAS[0])-1 < t5_t21_mem1*MAS_MEM[1]
	S += (t5_t2_t5*MAS[1])-1 < t5_t21_mem1*MAS_MEM[3]
	S += (t5_t2_t5*MAS[2])-1 < t5_t21_mem1*MAS_MEM[5]
	S += (t5_t2_t5*MAS[3])-1 < t5_t21_mem1*MAS_MEM[7]
	S += t5_t21_mem1 <= t5_t21

	t5_t6_t4 = S.Task('t5_t6_t4', length=6, delay_cost=1)
	t5_t6_t4 += alt(MM)
	t5_t6_t4_in = S.Task('t5_t6_t4_in', length=1, delay_cost=1)
	t5_t6_t4_in += alt(MM_in)
	S += t5_t6_t4_in*MM_in[0]<=t5_t6_t4*MM[0]
	t5_t6_t4_mem0 = S.Task('t5_t6_t4_mem0', length=1, delay_cost=1)
	t5_t6_t4_mem0 += alt(MAS_MEM)
	S += (t5_t6_t2*MAS[0])-1 < t5_t6_t4_mem0*MAS_MEM[0]
	S += (t5_t6_t2*MAS[1])-1 < t5_t6_t4_mem0*MAS_MEM[2]
	S += (t5_t6_t2*MAS[2])-1 < t5_t6_t4_mem0*MAS_MEM[4]
	S += (t5_t6_t2*MAS[3])-1 < t5_t6_t4_mem0*MAS_MEM[6]
	S += t5_t6_t4_mem0 <= t5_t6_t4

	t5_t6_t4_mem1 = S.Task('t5_t6_t4_mem1', length=1, delay_cost=1)
	t5_t6_t4_mem1 += alt(MAS_MEM)
	S += (t5_t6_t3*MAS[0])-1 < t5_t6_t4_mem1*MAS_MEM[1]
	S += (t5_t6_t3*MAS[1])-1 < t5_t6_t4_mem1*MAS_MEM[3]
	S += (t5_t6_t3*MAS[2])-1 < t5_t6_t4_mem1*MAS_MEM[5]
	S += (t5_t6_t3*MAS[3])-1 < t5_t6_t4_mem1*MAS_MEM[7]
	S += t5_t6_t4_mem1 <= t5_t6_t4

	t5_t60 = S.Task('t5_t60', length=1, delay_cost=1)
	t5_t60 += alt(MAS)
	t5_t60_mem0 = S.Task('t5_t60_mem0', length=1, delay_cost=1)
	t5_t60_mem0 += alt(MM_MEM)
	S += (t5_t6_t0*MM[0])-1 < t5_t60_mem0*MM_MEM[0]
	S += t5_t60_mem0 <= t5_t60

	t5_t60_mem1 = S.Task('t5_t60_mem1', length=1, delay_cost=1)
	t5_t60_mem1 += alt(MM_MEM)
	S += (t5_t6_t1*MM[0])-1 < t5_t60_mem1*MM_MEM[1]
	S += t5_t60_mem1 <= t5_t60

	t5_t6_t5 = S.Task('t5_t6_t5', length=1, delay_cost=1)
	t5_t6_t5 += alt(MAS)
	t5_t6_t5_mem0 = S.Task('t5_t6_t5_mem0', length=1, delay_cost=1)
	t5_t6_t5_mem0 += alt(MM_MEM)
	S += (t5_t6_t0*MM[0])-1 < t5_t6_t5_mem0*MM_MEM[0]
	S += t5_t6_t5_mem0 <= t5_t6_t5

	t5_t6_t5_mem1 = S.Task('t5_t6_t5_mem1', length=1, delay_cost=1)
	t5_t6_t5_mem1 += alt(MM_MEM)
	S += (t5_t6_t1*MM[0])-1 < t5_t6_t5_mem1*MM_MEM[1]
	S += t5_t6_t5_mem1 <= t5_t6_t5

	t5_t70 = S.Task('t5_t70', length=1, delay_cost=1)
	t5_t70 += alt(MAS)
	t5_t70_mem0 = S.Task('t5_t70_mem0', length=1, delay_cost=1)
	t5_t70_mem0 += alt(MAS_MEM)
	S += (t5_t00*MAS[0])-1 < t5_t70_mem0*MAS_MEM[0]
	S += (t5_t00*MAS[1])-1 < t5_t70_mem0*MAS_MEM[2]
	S += (t5_t00*MAS[2])-1 < t5_t70_mem0*MAS_MEM[4]
	S += (t5_t00*MAS[3])-1 < t5_t70_mem0*MAS_MEM[6]
	S += t5_t70_mem0 <= t5_t70

	t5_t70_mem1 = S.Task('t5_t70_mem1', length=1, delay_cost=1)
	t5_t70_mem1 += alt(MAS_MEM)
	S += (t5_t10*MAS[0])-1 < t5_t70_mem1*MAS_MEM[1]
	S += (t5_t10*MAS[1])-1 < t5_t70_mem1*MAS_MEM[3]
	S += (t5_t10*MAS[2])-1 < t5_t70_mem1*MAS_MEM[5]
	S += (t5_t10*MAS[3])-1 < t5_t70_mem1*MAS_MEM[7]
	S += t5_t70_mem1 <= t5_t70

	t5_t81 = S.Task('t5_t81', length=1, delay_cost=1)
	t5_t81 += alt(MAS)
	t5_t81_mem0 = S.Task('t5_t81_mem0', length=1, delay_cost=1)
	t5_t81_mem0 += alt(MM_MEM)
	S += (t5_t8_t4*MM[0])-1 < t5_t81_mem0*MM_MEM[0]
	S += t5_t81_mem0 <= t5_t81

	t5_t81_mem1 = S.Task('t5_t81_mem1', length=1, delay_cost=1)
	t5_t81_mem1 += alt(MAS_MEM)
	S += (t5_t8_t5*MAS[0])-1 < t5_t81_mem1*MAS_MEM[1]
	S += (t5_t8_t5*MAS[1])-1 < t5_t81_mem1*MAS_MEM[3]
	S += (t5_t8_t5*MAS[2])-1 < t5_t81_mem1*MAS_MEM[5]
	S += (t5_t8_t5*MAS[3])-1 < t5_t81_mem1*MAS_MEM[7]
	S += t5_t81_mem1 <= t5_t81

	t520 = S.Task('t520', length=1, delay_cost=1)
	t520 += alt(MAS)
	t520_mem0 = S.Task('t520_mem0', length=1, delay_cost=1)
	t520_mem0 += alt(MAS_MEM)
	S += (t5_t80*MAS[0])-1 < t520_mem0*MAS_MEM[0]
	S += (t5_t80*MAS[1])-1 < t520_mem0*MAS_MEM[2]
	S += (t5_t80*MAS[2])-1 < t520_mem0*MAS_MEM[4]
	S += (t5_t80*MAS[3])-1 < t520_mem0*MAS_MEM[6]
	S += t520_mem0 <= t520

	t520_mem1 = S.Task('t520_mem1', length=1, delay_cost=1)
	t520_mem1 += alt(MAS_MEM)
	S += (t5_t10*MAS[0])-1 < t520_mem1*MAS_MEM[1]
	S += (t5_t10*MAS[1])-1 < t520_mem1*MAS_MEM[3]
	S += (t5_t10*MAS[2])-1 < t520_mem1*MAS_MEM[5]
	S += (t5_t10*MAS[3])-1 < t520_mem1*MAS_MEM[7]
	S += t520_mem1 <= t520

	t160 = S.Task('t160', length=1, delay_cost=1)
	t160 += alt(MAS)
	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += MAS_MEM[6]
	S += 20 < t160_mem0
	S += t160_mem0 <= t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(MAS_MEM)
	S += (t420*MAS[0])-1 < t160_mem1*MAS_MEM[1]
	S += (t420*MAS[1])-1 < t160_mem1*MAS_MEM[3]
	S += (t420*MAS[2])-1 < t160_mem1*MAS_MEM[5]
	S += (t420*MAS[3])-1 < t160_mem1*MAS_MEM[7]
	S += t160_mem1 <= t160

	t170 = S.Task('t170', length=1, delay_cost=1)
	t170 += alt(MAS)
	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += MAS_MEM[6]
	S += 20 < t170_mem0
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t170_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t170_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t170_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t170_mem1*MAS_MEM[7]
	S += t170_mem1 <= t170

	t171 = S.Task('t171', length=1, delay_cost=1)
	t171 += alt(MAS)
	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t171_mem0*MAS_MEM[0]
	S += (t21*MAS[1])-1 < t171_mem0*MAS_MEM[2]
	S += (t21*MAS[2])-1 < t171_mem0*MAS_MEM[4]
	S += (t21*MAS[3])-1 < t171_mem0*MAS_MEM[6]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += MAS_MEM[7]
	S += 20 < t171_mem1
	S += t171_mem1 <= t171

	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(MAS)
	S += 38<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[6]
	S += 14 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += alt(MAS_MEM)
	S += (t420*MAS[0])-1 < c110_mem1*MAS_MEM[1]
	S += (t420*MAS[1])-1 < c110_mem1*MAS_MEM[3]
	S += (t420*MAS[2])-1 < c110_mem1*MAS_MEM[5]
	S += (t420*MAS[3])-1 < c110_mem1*MAS_MEM[7]
	S += c110_mem1 <= c110

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS4/SPARSE/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

