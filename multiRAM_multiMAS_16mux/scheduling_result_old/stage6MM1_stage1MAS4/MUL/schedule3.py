from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 151
	S = Scenario("schedule3", horizon=horizon)

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
	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 0
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 0
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 0
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 1
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 1
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 1
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=6, delay_cost=1)
	S += c_t1_t1_t1 >= 1
	c_t1_t1_t1 += MM[0]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 2
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 2
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 2
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=6, delay_cost=1)
	S += c_t1_t0_t0 >= 2
	c_t1_t0_t0 += MM[0]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=6, delay_cost=1)
	S += c_t0_t1_t0 >= 3
	c_t0_t1_t0 += MM[0]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 3
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 3
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 3
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=6, delay_cost=1)
	S += c_t0_t1_t1 >= 4
	c_t0_t1_t1 += MM[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 4
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 4
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 4
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 5
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 5
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 5
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=6, delay_cost=1)
	S += c_t1_t1_t0 >= 5
	c_t1_t1_t0 += MM[0]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 6
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 6
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 6
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=6, delay_cost=1)
	S += c_t1_t0_t1 >= 6
	c_t1_t0_t1 += MM[0]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 7
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 7
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 7
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=6, delay_cost=1)
	S += c_t0_t0_t1 >= 7
	c_t0_t0_t1 += MM[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=6, delay_cost=1)
	S += c_t0_t0_t0 >= 8
	c_t0_t0_t0 += MM[0]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 8
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 8
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 9
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 9
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	S += c_t0_t20 >= 9
	c_t0_t20 += MAS[1]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=1, delay_cost=1)
	S += c_t0_t0_t2 >= 10
	c_t0_t0_t2 += MAS[2]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 10
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 10
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 11
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 11
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	S += c_t0_t31 >= 11
	c_t0_t31 += MAS[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=1, delay_cost=1)
	S += c_t0_t1_t3 >= 12
	c_t0_t1_t3 += MAS[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 12
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 12
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 13
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 13
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 13
	c_t0_t30 += MAS[0]

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	S += c_t0_t21 >= 14
	c_t0_t21 += MAS[2]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 14
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 14
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 15
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 15
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=1, delay_cost=1)
	S += c_t1_t0_t2 >= 15
	c_t1_t0_t2 += MAS[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 16
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 16
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=1, delay_cost=1)
	S += c_t0_t1_t2 >= 16
	c_t0_t1_t2 += MAS[3]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=1, delay_cost=1)
	S += c_t0_t0_t3 >= 17
	c_t0_t0_t3 += MAS[3]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 17
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 17
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 18
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 18
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=1, delay_cost=1)
	S += c_t1_t1_t3 >= 18
	c_t1_t1_t3 += MAS[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 19
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 19
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=1, delay_cost=1)
	S += c_t1_t1_t2 >= 19
	c_t1_t1_t2 += MAS[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=1, delay_cost=1)
	S += c_t1_t0_t3 >= 20
	c_t1_t0_t3 += MAS[3]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 20
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 20
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 20
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=6, delay_cost=1)
	S += c_t2_t0_t0 >= 21
	c_t2_t0_t0 += MM[0]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 21
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 21
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 21
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=6, delay_cost=1)
	S += c_t2_t1_t0 >= 22
	c_t2_t1_t0 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 22
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 22
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 22
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 23
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 23
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 23
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=6, delay_cost=1)
	S += c_t2_t1_t1 >= 23
	c_t2_t1_t1 += MM[0]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=6, delay_cost=1)
	S += c_t2_t0_t1 >= 24
	c_t2_t0_t1 += MM[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 24
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 24
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 25
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 25
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	S += c_t3010 >= 25
	c_t3010 += MAS[1]

	c_t1_t21 = S.Task('c_t1_t21', length=1, delay_cost=1)
	S += c_t1_t21 >= 26
	c_t1_t21 += MAS[1]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 26
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 26
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=1, delay_cost=1)
	S += c_t2_t0_t3 >= 27
	c_t2_t0_t3 += MAS[3]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 27
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 27
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=1, delay_cost=1)
	S += c_t2_t1_t3 >= 28
	c_t2_t1_t3 += MAS[0]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 28
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 28
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 29
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 29
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	S += c_t3011 >= 29
	c_t3011 += MAS[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 30
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 30
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	S += c_t1_t31 >= 30
	c_t1_t31 += MAS[0]

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 31
	c_t1_t30 += MAS[2]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 31
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 31
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 32
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 32
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	S += c_t2_t31 >= 32
	c_t2_t31 += MAS[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=1, delay_cost=1)
	S += c_t2_t0_t2 >= 33
	c_t2_t0_t2 += MAS[2]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 33
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 33
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	S += c_t2_t30 >= 34
	c_t2_t30 += MAS[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 34
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 34
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 35
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 35
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	S += c_t3000 >= 35
	c_t3000 += MAS[2]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=1, delay_cost=1)
	S += c_t2_t1_t2 >= 36
	c_t2_t1_t2 += MAS[0]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 36
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 36
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 37
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 37
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	S += c_t3001 >= 37
	c_t3001 += MAS[1]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 38
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 38
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t21 = S.Task('c_t2_t21', length=1, delay_cost=1)
	S += c_t2_t21 >= 38
	c_t2_t21 += MAS[0]

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	S += c_t1_t20 >= 39
	c_t1_t20 += MAS[2]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 39
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 39
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	S += c_t2_t20 >= 40
	c_t2_t20 += MAS[0]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 40
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 40
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	S += c_t4011 >= 41
	c_t4011 += MAS[1]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 41
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 41
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t4100 = S.Task('c_t4100', length=1, delay_cost=1)
	S += c_t4100 >= 42
	c_t4100 += MAS[2]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 42
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 42
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t4101 = S.Task('c_t4101', length=1, delay_cost=1)
	S += c_t4101 >= 43
	c_t4101 += MAS[3]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 43
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 43
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4110 = S.Task('c_t4110', length=1, delay_cost=1)
	S += c_t4110 >= 44
	c_t4110 += MAS[2]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 44
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 44
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4111 = S.Task('c_t4111', length=1, delay_cost=1)
	S += c_t4111 >= 45
	c_t4111 += MAS[0]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 45
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 45
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 46
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 46
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	S += c_t5000 >= 46
	c_t5000 += MAS[1]

	c_t3100 = S.Task('c_t3100', length=1, delay_cost=1)
	S += c_t3100 >= 47
	c_t3100 += MAS[0]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 47
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 47
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	S += c_t5001 >= 48
	c_t5001 += MAS[0]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 48
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 48
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	S += c_t5010 >= 49
	c_t5010 += MAS[0]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 49
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 49
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	S += c_t5011 >= 50
	c_t5011 += MAS[2]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 50
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 50
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5100 = S.Task('c_t5100', length=1, delay_cost=1)
	S += c_t5100 >= 51
	c_t5100 += MAS[0]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 51
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 51
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5101 = S.Task('c_t5101', length=1, delay_cost=1)
	S += c_t5101 >= 52
	c_t5101 += MAS[0]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 52
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 52
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t5110 = S.Task('c_t5110', length=1, delay_cost=1)
	S += c_t5110 >= 53
	c_t5110 += MAS[0]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 53
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 53
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 54
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 54
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t5111 = S.Task('c_t5111', length=1, delay_cost=1)
	S += c_t5111 >= 54
	c_t5111 += MAS[2]

	c_t3101 = S.Task('c_t3101', length=1, delay_cost=1)
	S += c_t3101 >= 55
	c_t3101 += MAS[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 55
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 55
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 56
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 56
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	S += c_t4001 >= 56
	c_t4001 += MAS[0]

	c_t3110 = S.Task('c_t3110', length=1, delay_cost=1)
	S += c_t3110 >= 57
	c_t3110 += MAS[2]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 57
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 57
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t3111 = S.Task('c_t3111', length=1, delay_cost=1)
	S += c_t3111 >= 58
	c_t3111 += MAS[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 58
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 58
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 59
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 59
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	S += c_t4010 >= 59
	c_t4010 += MAS[0]

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	S += c_t4000 >= 60
	c_t4000 += MAS[1]


	# new tasks
	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	c_t0_t0_t4_in += alt(MM_in)
	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=6, delay_cost=1)
	c_t0_t0_t4 += alt(MM)
	S += c_t0_t0_t4>=c_t0_t0_t4_in

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	c_t0_t0_t4_mem0 += MAS_MEM[4]
	S += 10 < c_t0_t0_t4_mem0
	S += c_t0_t0_t4_mem0 <= c_t0_t0_t4

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	c_t0_t0_t4_mem1 += MAS_MEM[7]
	S += 17 < c_t0_t0_t4_mem1
	S += c_t0_t0_t4_mem1 <= c_t0_t0_t4

	c_t0_t00 = S.Task('c_t0_t00', length=1, delay_cost=1)
	c_t0_t00 += alt(MAS)

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	c_t0_t00_mem0 += MM_MEM[0]
	S += 13 < c_t0_t00_mem0
	S += c_t0_t00_mem0 <= c_t0_t00

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	c_t0_t00_mem1 += MM_MEM[1]
	S += 12 < c_t0_t00_mem1
	S += c_t0_t00_mem1 <= c_t0_t00

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=1, delay_cost=1)
	c_t0_t0_t5 += alt(MAS)

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	c_t0_t0_t5_mem0 += MM_MEM[0]
	S += 13 < c_t0_t0_t5_mem0
	S += c_t0_t0_t5_mem0 <= c_t0_t0_t5

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	c_t0_t0_t5_mem1 += MM_MEM[1]
	S += 12 < c_t0_t0_t5_mem1
	S += c_t0_t0_t5_mem1 <= c_t0_t0_t5

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	c_t0_t1_t4_in += alt(MM_in)
	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=6, delay_cost=1)
	c_t0_t1_t4 += alt(MM)
	S += c_t0_t1_t4>=c_t0_t1_t4_in

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	c_t0_t1_t4_mem0 += MAS_MEM[6]
	S += 16 < c_t0_t1_t4_mem0
	S += c_t0_t1_t4_mem0 <= c_t0_t1_t4

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	c_t0_t1_t4_mem1 += MAS_MEM[1]
	S += 12 < c_t0_t1_t4_mem1
	S += c_t0_t1_t4_mem1 <= c_t0_t1_t4

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	c_t0_t10 += alt(MAS)

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	c_t0_t10_mem0 += MM_MEM[0]
	S += 8 < c_t0_t10_mem0
	S += c_t0_t10_mem0 <= c_t0_t10

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	c_t0_t10_mem1 += MM_MEM[1]
	S += 9 < c_t0_t10_mem1
	S += c_t0_t10_mem1 <= c_t0_t10

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=1, delay_cost=1)
	c_t0_t1_t5 += alt(MAS)

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	c_t0_t1_t5_mem0 += MM_MEM[0]
	S += 8 < c_t0_t1_t5_mem0
	S += c_t0_t1_t5_mem0 <= c_t0_t1_t5

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	c_t0_t1_t5_mem1 += MM_MEM[1]
	S += 9 < c_t0_t1_t5_mem1
	S += c_t0_t1_t5_mem1 <= c_t0_t1_t5

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	c_t0_t4_t0_in += alt(MM_in)
	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=6, delay_cost=1)
	c_t0_t4_t0 += alt(MM)
	S += c_t0_t4_t0>=c_t0_t4_t0_in

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	c_t0_t4_t0_mem0 += MAS_MEM[2]
	S += 9 < c_t0_t4_t0_mem0
	S += c_t0_t4_t0_mem0 <= c_t0_t4_t0

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	c_t0_t4_t0_mem1 += MAS_MEM[1]
	S += 13 < c_t0_t4_t0_mem1
	S += c_t0_t4_t0_mem1 <= c_t0_t4_t0

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	c_t0_t4_t1_in += alt(MM_in)
	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=6, delay_cost=1)
	c_t0_t4_t1 += alt(MM)
	S += c_t0_t4_t1>=c_t0_t4_t1_in

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	c_t0_t4_t1_mem0 += MAS_MEM[4]
	S += 14 < c_t0_t4_t1_mem0
	S += c_t0_t4_t1_mem0 <= c_t0_t4_t1

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	c_t0_t4_t1_mem1 += MAS_MEM[1]
	S += 11 < c_t0_t4_t1_mem1
	S += c_t0_t4_t1_mem1 <= c_t0_t4_t1

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=1, delay_cost=1)
	c_t0_t4_t2 += alt(MAS)

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	c_t0_t4_t2_mem0 += MAS_MEM[2]
	S += 9 < c_t0_t4_t2_mem0
	S += c_t0_t4_t2_mem0 <= c_t0_t4_t2

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	c_t0_t4_t2_mem1 += MAS_MEM[5]
	S += 14 < c_t0_t4_t2_mem1
	S += c_t0_t4_t2_mem1 <= c_t0_t4_t2

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=1, delay_cost=1)
	c_t0_t4_t3 += alt(MAS)

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	c_t0_t4_t3_mem0 += MAS_MEM[0]
	S += 13 < c_t0_t4_t3_mem0
	S += c_t0_t4_t3_mem0 <= c_t0_t4_t3

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	c_t0_t4_t3_mem1 += MAS_MEM[1]
	S += 11 < c_t0_t4_t3_mem1
	S += c_t0_t4_t3_mem1 <= c_t0_t4_t3

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	c_t1_t0_t4_in += alt(MM_in)
	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=6, delay_cost=1)
	c_t1_t0_t4 += alt(MM)
	S += c_t1_t0_t4>=c_t1_t0_t4_in

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	c_t1_t0_t4_mem0 += MAS_MEM[0]
	S += 15 < c_t1_t0_t4_mem0
	S += c_t1_t0_t4_mem0 <= c_t1_t0_t4

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	c_t1_t0_t4_mem1 += MAS_MEM[7]
	S += 20 < c_t1_t0_t4_mem1
	S += c_t1_t0_t4_mem1 <= c_t1_t0_t4

	c_t1_t00 = S.Task('c_t1_t00', length=1, delay_cost=1)
	c_t1_t00 += alt(MAS)

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	c_t1_t00_mem0 += MM_MEM[0]
	S += 7 < c_t1_t00_mem0
	S += c_t1_t00_mem0 <= c_t1_t00

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	c_t1_t00_mem1 += MM_MEM[1]
	S += 11 < c_t1_t00_mem1
	S += c_t1_t00_mem1 <= c_t1_t00

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=1, delay_cost=1)
	c_t1_t0_t5 += alt(MAS)

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	c_t1_t0_t5_mem0 += MM_MEM[0]
	S += 7 < c_t1_t0_t5_mem0
	S += c_t1_t0_t5_mem0 <= c_t1_t0_t5

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	c_t1_t0_t5_mem1 += MM_MEM[1]
	S += 11 < c_t1_t0_t5_mem1
	S += c_t1_t0_t5_mem1 <= c_t1_t0_t5

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	c_t1_t1_t4_in += alt(MM_in)
	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=6, delay_cost=1)
	c_t1_t1_t4 += alt(MM)
	S += c_t1_t1_t4>=c_t1_t1_t4_in

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	c_t1_t1_t4_mem0 += MAS_MEM[2]
	S += 19 < c_t1_t1_t4_mem0
	S += c_t1_t1_t4_mem0 <= c_t1_t1_t4

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	c_t1_t1_t4_mem1 += MAS_MEM[3]
	S += 18 < c_t1_t1_t4_mem1
	S += c_t1_t1_t4_mem1 <= c_t1_t1_t4

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	c_t1_t10 += alt(MAS)

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	c_t1_t10_mem0 += MM_MEM[0]
	S += 10 < c_t1_t10_mem0
	S += c_t1_t10_mem0 <= c_t1_t10

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	c_t1_t10_mem1 += MM_MEM[1]
	S += 6 < c_t1_t10_mem1
	S += c_t1_t10_mem1 <= c_t1_t10

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=1, delay_cost=1)
	c_t1_t1_t5 += alt(MAS)

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	c_t1_t1_t5_mem0 += MM_MEM[0]
	S += 10 < c_t1_t1_t5_mem0
	S += c_t1_t1_t5_mem0 <= c_t1_t1_t5

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	c_t1_t1_t5_mem1 += MM_MEM[1]
	S += 6 < c_t1_t1_t5_mem1
	S += c_t1_t1_t5_mem1 <= c_t1_t1_t5

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	c_t1_t4_t0_in += alt(MM_in)
	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=6, delay_cost=1)
	c_t1_t4_t0 += alt(MM)
	S += c_t1_t4_t0>=c_t1_t4_t0_in

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	c_t1_t4_t0_mem0 += MAS_MEM[4]
	S += 39 < c_t1_t4_t0_mem0
	S += c_t1_t4_t0_mem0 <= c_t1_t4_t0

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	c_t1_t4_t0_mem1 += MAS_MEM[5]
	S += 31 < c_t1_t4_t0_mem1
	S += c_t1_t4_t0_mem1 <= c_t1_t4_t0

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	c_t1_t4_t1_in += alt(MM_in)
	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=6, delay_cost=1)
	c_t1_t4_t1 += alt(MM)
	S += c_t1_t4_t1>=c_t1_t4_t1_in

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	c_t1_t4_t1_mem0 += MAS_MEM[2]
	S += 26 < c_t1_t4_t1_mem0
	S += c_t1_t4_t1_mem0 <= c_t1_t4_t1

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	c_t1_t4_t1_mem1 += MAS_MEM[1]
	S += 30 < c_t1_t4_t1_mem1
	S += c_t1_t4_t1_mem1 <= c_t1_t4_t1

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=1, delay_cost=1)
	c_t1_t4_t2 += alt(MAS)

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	c_t1_t4_t2_mem0 += MAS_MEM[4]
	S += 39 < c_t1_t4_t2_mem0
	S += c_t1_t4_t2_mem0 <= c_t1_t4_t2

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	c_t1_t4_t2_mem1 += MAS_MEM[3]
	S += 26 < c_t1_t4_t2_mem1
	S += c_t1_t4_t2_mem1 <= c_t1_t4_t2

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=1, delay_cost=1)
	c_t1_t4_t3 += alt(MAS)

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	c_t1_t4_t3_mem0 += MAS_MEM[4]
	S += 31 < c_t1_t4_t3_mem0
	S += c_t1_t4_t3_mem0 <= c_t1_t4_t3

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	c_t1_t4_t3_mem1 += MAS_MEM[1]
	S += 30 < c_t1_t4_t3_mem1
	S += c_t1_t4_t3_mem1 <= c_t1_t4_t3

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	c_t2_t0_t4_in += alt(MM_in)
	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=6, delay_cost=1)
	c_t2_t0_t4 += alt(MM)
	S += c_t2_t0_t4>=c_t2_t0_t4_in

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	c_t2_t0_t4_mem0 += MAS_MEM[4]
	S += 33 < c_t2_t0_t4_mem0
	S += c_t2_t0_t4_mem0 <= c_t2_t0_t4

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	c_t2_t0_t4_mem1 += MAS_MEM[7]
	S += 27 < c_t2_t0_t4_mem1
	S += c_t2_t0_t4_mem1 <= c_t2_t0_t4

	c_t2_t00 = S.Task('c_t2_t00', length=1, delay_cost=1)
	c_t2_t00 += alt(MAS)

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	c_t2_t00_mem0 += MM_MEM[0]
	S += 26 < c_t2_t00_mem0
	S += c_t2_t00_mem0 <= c_t2_t00

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	c_t2_t00_mem1 += MM_MEM[1]
	S += 29 < c_t2_t00_mem1
	S += c_t2_t00_mem1 <= c_t2_t00

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=1, delay_cost=1)
	c_t2_t0_t5 += alt(MAS)

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	c_t2_t0_t5_mem0 += MM_MEM[0]
	S += 26 < c_t2_t0_t5_mem0
	S += c_t2_t0_t5_mem0 <= c_t2_t0_t5

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	c_t2_t0_t5_mem1 += MM_MEM[1]
	S += 29 < c_t2_t0_t5_mem1
	S += c_t2_t0_t5_mem1 <= c_t2_t0_t5

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	c_t2_t1_t4_in += alt(MM_in)
	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=6, delay_cost=1)
	c_t2_t1_t4 += alt(MM)
	S += c_t2_t1_t4>=c_t2_t1_t4_in

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	c_t2_t1_t4_mem0 += MAS_MEM[0]
	S += 36 < c_t2_t1_t4_mem0
	S += c_t2_t1_t4_mem0 <= c_t2_t1_t4

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	c_t2_t1_t4_mem1 += MAS_MEM[1]
	S += 28 < c_t2_t1_t4_mem1
	S += c_t2_t1_t4_mem1 <= c_t2_t1_t4

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	c_t2_t10 += alt(MAS)

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	c_t2_t10_mem0 += MM_MEM[0]
	S += 27 < c_t2_t10_mem0
	S += c_t2_t10_mem0 <= c_t2_t10

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	c_t2_t10_mem1 += MM_MEM[1]
	S += 28 < c_t2_t10_mem1
	S += c_t2_t10_mem1 <= c_t2_t10

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=1, delay_cost=1)
	c_t2_t1_t5 += alt(MAS)

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	c_t2_t1_t5_mem0 += MM_MEM[0]
	S += 27 < c_t2_t1_t5_mem0
	S += c_t2_t1_t5_mem0 <= c_t2_t1_t5

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	c_t2_t1_t5_mem1 += MM_MEM[1]
	S += 28 < c_t2_t1_t5_mem1
	S += c_t2_t1_t5_mem1 <= c_t2_t1_t5

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	c_t2_t4_t0_in += alt(MM_in)
	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=6, delay_cost=1)
	c_t2_t4_t0 += alt(MM)
	S += c_t2_t4_t0>=c_t2_t4_t0_in

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	c_t2_t4_t0_mem0 += MAS_MEM[0]
	S += 40 < c_t2_t4_t0_mem0
	S += c_t2_t4_t0_mem0 <= c_t2_t4_t0

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	c_t2_t4_t0_mem1 += MAS_MEM[7]
	S += 34 < c_t2_t4_t0_mem1
	S += c_t2_t4_t0_mem1 <= c_t2_t4_t0

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	c_t2_t4_t1_in += alt(MM_in)
	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=6, delay_cost=1)
	c_t2_t4_t1 += alt(MM)
	S += c_t2_t4_t1>=c_t2_t4_t1_in

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	c_t2_t4_t1_mem0 += MAS_MEM[0]
	S += 38 < c_t2_t4_t1_mem0
	S += c_t2_t4_t1_mem0 <= c_t2_t4_t1

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	c_t2_t4_t1_mem1 += MAS_MEM[1]
	S += 32 < c_t2_t4_t1_mem1
	S += c_t2_t4_t1_mem1 <= c_t2_t4_t1

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=1, delay_cost=1)
	c_t2_t4_t2 += alt(MAS)

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	c_t2_t4_t2_mem0 += MAS_MEM[0]
	S += 40 < c_t2_t4_t2_mem0
	S += c_t2_t4_t2_mem0 <= c_t2_t4_t2

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	c_t2_t4_t2_mem1 += MAS_MEM[1]
	S += 38 < c_t2_t4_t2_mem1
	S += c_t2_t4_t2_mem1 <= c_t2_t4_t2

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=1, delay_cost=1)
	c_t2_t4_t3 += alt(MAS)

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	c_t2_t4_t3_mem0 += MAS_MEM[6]
	S += 34 < c_t2_t4_t3_mem0
	S += c_t2_t4_t3_mem0 <= c_t2_t4_t3

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	c_t2_t4_t3_mem1 += MAS_MEM[1]
	S += 32 < c_t2_t4_t3_mem1
	S += c_t2_t4_t3_mem1 <= c_t2_t4_t3

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	c_t3_t0_t0_in += alt(MM_in)
	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=6, delay_cost=1)
	c_t3_t0_t0 += alt(MM)
	S += c_t3_t0_t0>=c_t3_t0_t0_in

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	c_t3_t0_t0_mem0 += MAS_MEM[4]
	S += 35 < c_t3_t0_t0_mem0
	S += c_t3_t0_t0_mem0 <= c_t3_t0_t0

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	c_t3_t0_t0_mem1 += MAS_MEM[1]
	S += 47 < c_t3_t0_t0_mem1
	S += c_t3_t0_t0_mem1 <= c_t3_t0_t0

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	c_t3_t0_t1_in += alt(MM_in)
	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=6, delay_cost=1)
	c_t3_t0_t1 += alt(MM)
	S += c_t3_t0_t1>=c_t3_t0_t1_in

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	c_t3_t0_t1_mem0 += MAS_MEM[2]
	S += 37 < c_t3_t0_t1_mem0
	S += c_t3_t0_t1_mem0 <= c_t3_t0_t1

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	c_t3_t0_t1_mem1 += MAS_MEM[3]
	S += 55 < c_t3_t0_t1_mem1
	S += c_t3_t0_t1_mem1 <= c_t3_t0_t1

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=1, delay_cost=1)
	c_t3_t0_t2 += alt(MAS)

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	c_t3_t0_t2_mem0 += MAS_MEM[4]
	S += 35 < c_t3_t0_t2_mem0
	S += c_t3_t0_t2_mem0 <= c_t3_t0_t2

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	c_t3_t0_t2_mem1 += MAS_MEM[3]
	S += 37 < c_t3_t0_t2_mem1
	S += c_t3_t0_t2_mem1 <= c_t3_t0_t2

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=1, delay_cost=1)
	c_t3_t0_t3 += alt(MAS)

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	c_t3_t0_t3_mem0 += MAS_MEM[0]
	S += 47 < c_t3_t0_t3_mem0
	S += c_t3_t0_t3_mem0 <= c_t3_t0_t3

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	c_t3_t0_t3_mem1 += MAS_MEM[3]
	S += 55 < c_t3_t0_t3_mem1
	S += c_t3_t0_t3_mem1 <= c_t3_t0_t3

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	c_t3_t1_t0_in += alt(MM_in)
	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=6, delay_cost=1)
	c_t3_t1_t0 += alt(MM)
	S += c_t3_t1_t0>=c_t3_t1_t0_in

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	c_t3_t1_t0_mem0 += MAS_MEM[2]
	S += 25 < c_t3_t1_t0_mem0
	S += c_t3_t1_t0_mem0 <= c_t3_t1_t0

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	c_t3_t1_t0_mem1 += MAS_MEM[5]
	S += 57 < c_t3_t1_t0_mem1
	S += c_t3_t1_t0_mem1 <= c_t3_t1_t0

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	c_t3_t1_t1_in += alt(MM_in)
	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=6, delay_cost=1)
	c_t3_t1_t1 += alt(MM)
	S += c_t3_t1_t1>=c_t3_t1_t1_in

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	c_t3_t1_t1_mem0 += MAS_MEM[0]
	S += 29 < c_t3_t1_t1_mem0
	S += c_t3_t1_t1_mem0 <= c_t3_t1_t1

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	c_t3_t1_t1_mem1 += MAS_MEM[3]
	S += 58 < c_t3_t1_t1_mem1
	S += c_t3_t1_t1_mem1 <= c_t3_t1_t1

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=1, delay_cost=1)
	c_t3_t1_t2 += alt(MAS)

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	c_t3_t1_t2_mem0 += MAS_MEM[2]
	S += 25 < c_t3_t1_t2_mem0
	S += c_t3_t1_t2_mem0 <= c_t3_t1_t2

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	c_t3_t1_t2_mem1 += MAS_MEM[1]
	S += 29 < c_t3_t1_t2_mem1
	S += c_t3_t1_t2_mem1 <= c_t3_t1_t2

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=1, delay_cost=1)
	c_t3_t1_t3 += alt(MAS)

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	c_t3_t1_t3_mem0 += MAS_MEM[4]
	S += 57 < c_t3_t1_t3_mem0
	S += c_t3_t1_t3_mem0 <= c_t3_t1_t3

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	c_t3_t1_t3_mem1 += MAS_MEM[3]
	S += 58 < c_t3_t1_t3_mem1
	S += c_t3_t1_t3_mem1 <= c_t3_t1_t3

	c_t3_t20 = S.Task('c_t3_t20', length=1, delay_cost=1)
	c_t3_t20 += alt(MAS)

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	c_t3_t20_mem0 += MAS_MEM[4]
	S += 35 < c_t3_t20_mem0
	S += c_t3_t20_mem0 <= c_t3_t20

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	c_t3_t20_mem1 += MAS_MEM[3]
	S += 25 < c_t3_t20_mem1
	S += c_t3_t20_mem1 <= c_t3_t20

	c_t3_t21 = S.Task('c_t3_t21', length=1, delay_cost=1)
	c_t3_t21 += alt(MAS)

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	c_t3_t21_mem0 += MAS_MEM[2]
	S += 37 < c_t3_t21_mem0
	S += c_t3_t21_mem0 <= c_t3_t21

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	c_t3_t21_mem1 += MAS_MEM[1]
	S += 29 < c_t3_t21_mem1
	S += c_t3_t21_mem1 <= c_t3_t21

	c_t3_t30 = S.Task('c_t3_t30', length=1, delay_cost=1)
	c_t3_t30 += alt(MAS)

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	c_t3_t30_mem0 += MAS_MEM[0]
	S += 47 < c_t3_t30_mem0
	S += c_t3_t30_mem0 <= c_t3_t30

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	c_t3_t30_mem1 += MAS_MEM[5]
	S += 57 < c_t3_t30_mem1
	S += c_t3_t30_mem1 <= c_t3_t30

	c_t3_t31 = S.Task('c_t3_t31', length=1, delay_cost=1)
	c_t3_t31 += alt(MAS)

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	c_t3_t31_mem0 += MAS_MEM[2]
	S += 55 < c_t3_t31_mem0
	S += c_t3_t31_mem0 <= c_t3_t31

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	c_t3_t31_mem1 += MAS_MEM[3]
	S += 58 < c_t3_t31_mem1
	S += c_t3_t31_mem1 <= c_t3_t31

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	c_t4_t0_t0_in += alt(MM_in)
	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=6, delay_cost=1)
	c_t4_t0_t0 += alt(MM)
	S += c_t4_t0_t0>=c_t4_t0_t0_in

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	c_t4_t0_t0_mem0 += MAS_MEM[2]
	S += 60 < c_t4_t0_t0_mem0
	S += c_t4_t0_t0_mem0 <= c_t4_t0_t0

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	c_t4_t0_t0_mem1 += MAS_MEM[5]
	S += 42 < c_t4_t0_t0_mem1
	S += c_t4_t0_t0_mem1 <= c_t4_t0_t0

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	c_t4_t0_t1_in += alt(MM_in)
	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=6, delay_cost=1)
	c_t4_t0_t1 += alt(MM)
	S += c_t4_t0_t1>=c_t4_t0_t1_in

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	c_t4_t0_t1_mem0 += MAS_MEM[0]
	S += 56 < c_t4_t0_t1_mem0
	S += c_t4_t0_t1_mem0 <= c_t4_t0_t1

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	c_t4_t0_t1_mem1 += MAS_MEM[7]
	S += 43 < c_t4_t0_t1_mem1
	S += c_t4_t0_t1_mem1 <= c_t4_t0_t1

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=1, delay_cost=1)
	c_t4_t0_t2 += alt(MAS)

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	c_t4_t0_t2_mem0 += MAS_MEM[2]
	S += 60 < c_t4_t0_t2_mem0
	S += c_t4_t0_t2_mem0 <= c_t4_t0_t2

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	c_t4_t0_t2_mem1 += MAS_MEM[1]
	S += 56 < c_t4_t0_t2_mem1
	S += c_t4_t0_t2_mem1 <= c_t4_t0_t2

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=1, delay_cost=1)
	c_t4_t0_t3 += alt(MAS)

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	c_t4_t0_t3_mem0 += MAS_MEM[4]
	S += 42 < c_t4_t0_t3_mem0
	S += c_t4_t0_t3_mem0 <= c_t4_t0_t3

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	c_t4_t0_t3_mem1 += MAS_MEM[7]
	S += 43 < c_t4_t0_t3_mem1
	S += c_t4_t0_t3_mem1 <= c_t4_t0_t3

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	c_t4_t1_t0_in += alt(MM_in)
	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=6, delay_cost=1)
	c_t4_t1_t0 += alt(MM)
	S += c_t4_t1_t0>=c_t4_t1_t0_in

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	c_t4_t1_t0_mem0 += MAS_MEM[0]
	S += 59 < c_t4_t1_t0_mem0
	S += c_t4_t1_t0_mem0 <= c_t4_t1_t0

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	c_t4_t1_t0_mem1 += MAS_MEM[5]
	S += 44 < c_t4_t1_t0_mem1
	S += c_t4_t1_t0_mem1 <= c_t4_t1_t0

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	c_t4_t1_t1_in += alt(MM_in)
	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=6, delay_cost=1)
	c_t4_t1_t1 += alt(MM)
	S += c_t4_t1_t1>=c_t4_t1_t1_in

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	c_t4_t1_t1_mem0 += MAS_MEM[2]
	S += 41 < c_t4_t1_t1_mem0
	S += c_t4_t1_t1_mem0 <= c_t4_t1_t1

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	c_t4_t1_t1_mem1 += MAS_MEM[1]
	S += 45 < c_t4_t1_t1_mem1
	S += c_t4_t1_t1_mem1 <= c_t4_t1_t1

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=1, delay_cost=1)
	c_t4_t1_t2 += alt(MAS)

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	c_t4_t1_t2_mem0 += MAS_MEM[0]
	S += 59 < c_t4_t1_t2_mem0
	S += c_t4_t1_t2_mem0 <= c_t4_t1_t2

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	c_t4_t1_t2_mem1 += MAS_MEM[3]
	S += 41 < c_t4_t1_t2_mem1
	S += c_t4_t1_t2_mem1 <= c_t4_t1_t2

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=1, delay_cost=1)
	c_t4_t1_t3 += alt(MAS)

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	c_t4_t1_t3_mem0 += MAS_MEM[4]
	S += 44 < c_t4_t1_t3_mem0
	S += c_t4_t1_t3_mem0 <= c_t4_t1_t3

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	c_t4_t1_t3_mem1 += MAS_MEM[1]
	S += 45 < c_t4_t1_t3_mem1
	S += c_t4_t1_t3_mem1 <= c_t4_t1_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage6MM1_stage1MAS4/MUL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

