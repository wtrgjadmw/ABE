from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 0
	c_t1_t0_t1_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 0
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 0
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 1
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=1, delay_cost=1)
	S += c_t0_t1_t2 >= 1
	c_t0_t1_t2 += MAS[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=4, delay_cost=1)
	S += c_t1_t0_t1 >= 1
	c_t1_t0_t1 += MM[0]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 1
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	S += c_t1_t20 >= 1
	c_t1_t20 += MAS[2]

	c_t1_t21 = S.Task('c_t1_t21', length=1, delay_cost=1)
	S += c_t1_t21 >= 1
	c_t1_t21 += MAS[3]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 1
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=1, delay_cost=1)
	S += c_t2_t0_t2 >= 1
	c_t2_t0_t2 += MAS[0]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=1, delay_cost=1)
	S += c_t0_t0_t3 >= 2
	c_t0_t0_t3 += MAS[3]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 2
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=1, delay_cost=1)
	S += c_t0_t1_t3 >= 2
	c_t0_t1_t3 += MAS[0]

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	S += c_t0_t20 >= 2
	c_t0_t20 += MAS[1]

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	S += c_t0_t31 >= 2
	c_t0_t31 += MAS[2]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 2
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=4, delay_cost=1)
	S += c_t2_t0_t1 >= 2
	c_t2_t0_t1 += MM[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 2
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 3
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=4, delay_cost=1)
	S += c_t0_t1_t0 >= 3
	c_t0_t1_t0 += MM[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 3
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=1, delay_cost=1)
	S += c_t1_t0_t2 >= 3
	c_t1_t0_t2 += MAS[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=1, delay_cost=1)
	S += c_t1_t0_t3 >= 3
	c_t1_t0_t3 += MAS[2]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=1, delay_cost=1)
	S += c_t1_t1_t3 >= 3
	c_t1_t1_t3 += MAS[3]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 3
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	S += c_t1_t31 >= 3
	c_t1_t31 += MAS[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=4, delay_cost=1)
	S += c_t0_t0_t0 >= 4
	c_t0_t0_t0 += MM[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=1, delay_cost=1)
	S += c_t0_t0_t2 >= 4
	c_t0_t0_t2 += MAS[2]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 4
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 4
	c_t0_t30 += MAS[0]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=1, delay_cost=1)
	S += c_t1_t1_t2 >= 4
	c_t1_t1_t2 += MAS[1]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 4
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=1, delay_cost=1)
	S += c_t2_t0_t3 >= 4
	c_t2_t0_t3 += MAS[3]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 4
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 5
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=4, delay_cost=1)
	S += c_t0_t1_t1 >= 5
	c_t0_t1_t1 += MM[0]

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	S += c_t0_t21 >= 5
	c_t0_t21 += MAS[0]

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 5
	c_t1_t30 += MAS[2]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 5
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 5
	c_t2_t1_t1_in += MM_in[0]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 6
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 6
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 6
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=4, delay_cost=1)
	S += c_t2_t1_t1 >= 6
	c_t2_t1_t1 += MM[0]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=4, delay_cost=1)
	S += c_t0_t0_t1 >= 7
	c_t0_t0_t1 += MM[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 7
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 7
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 7
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 8
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=4, delay_cost=1)
	S += c_t1_t1_t1 >= 8
	c_t1_t1_t1 += MM[0]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 8
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 8
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 9
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 9
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 9
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=4, delay_cost=1)
	S += c_t2_t0_t0 >= 9
	c_t2_t0_t0 += MM[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 10
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=4, delay_cost=1)
	S += c_t1_t0_t0 >= 10
	c_t1_t0_t0 += MM[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 10
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 10
	c_t2_t1_t0_in += MM_in[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 11
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 11
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 11
	c_t1_t1_t0_in += MM_in[0]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=4, delay_cost=1)
	S += c_t2_t1_t0 >= 11
	c_t2_t1_t0 += MM[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 12
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 12
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=4, delay_cost=1)
	S += c_t1_t1_t0 >= 12
	c_t1_t1_t0 += MM[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 13
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 13
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 14
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 14
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 15
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 15
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 16
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 16
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 17
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 17
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 18
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 18
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 19
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 19
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 20
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 20
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 21
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 21
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 22
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 22
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 23
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 23
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 24
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 24
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 25
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 25
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 26
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 26
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 27
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 27
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 28
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 28
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 29
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 29
	c_t1_t30_mem0 += MAIN_MEM_r[0]


	# new tasks
	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=1, delay_cost=1)
	c_t2_t1_t2 += alt(MAS)

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]
	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]
	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=1, delay_cost=1)
	c_t2_t1_t3 += alt(MAS)

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]
	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]
	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	c_t2_t20 += alt(MAS)

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	c_t2_t20_mem0 += MAIN_MEM_r[0]
	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	c_t2_t20_mem1 += MAIN_MEM_r[1]
	c_t2_t21 = S.Task('c_t2_t21', length=1, delay_cost=1)
	c_t2_t21 += alt(MAS)

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	c_t2_t21_mem0 += MAIN_MEM_r[0]
	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	c_t2_t21_mem1 += MAIN_MEM_r[1]
	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	c_t2_t30 += alt(MAS)

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	c_t2_t30_mem0 += MAIN_MEM_r[0]
	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	c_t2_t30_mem1 += MAIN_MEM_r[1]
	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	c_t2_t31 += alt(MAS)

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	c_t2_t31_mem0 += MAIN_MEM_r[0]
	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	c_t2_t31_mem1 += MAIN_MEM_r[1]
	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	c_t3000 += alt(MAS)

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	c_t3000_mem0 += MAIN_MEM_r[0]
	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	c_t3000_mem1 += MAIN_MEM_r[1]
	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	c_t3001 += alt(MAS)

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	c_t3001_mem0 += MAIN_MEM_r[0]
	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	c_t3001_mem1 += MAIN_MEM_r[1]
	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	c_t3010 += alt(MAS)

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	c_t3010_mem0 += MAIN_MEM_r[0]
	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	c_t3010_mem1 += MAIN_MEM_r[1]
	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	c_t3011 += alt(MAS)

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	c_t3011_mem0 += MAIN_MEM_r[0]
	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	c_t3011_mem1 += MAIN_MEM_r[1]
	c_t3100 = S.Task('c_t3100', length=1, delay_cost=1)
	c_t3100 += alt(MAS)

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	c_t3100_mem0 += MAIN_MEM_r[0]
	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	c_t3100_mem1 += MAIN_MEM_r[1]
	c_t3101 = S.Task('c_t3101', length=1, delay_cost=1)
	c_t3101 += alt(MAS)

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	c_t3101_mem0 += MAIN_MEM_r[0]
	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	c_t3101_mem1 += MAIN_MEM_r[1]
	c_t3110 = S.Task('c_t3110', length=1, delay_cost=1)
	c_t3110 += alt(MAS)

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	c_t3110_mem0 += MAIN_MEM_r[0]
	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	c_t3110_mem1 += MAIN_MEM_r[1]
	c_t3111 = S.Task('c_t3111', length=1, delay_cost=1)
	c_t3111 += alt(MAS)

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	c_t3111_mem0 += MAIN_MEM_r[0]
	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	c_t3111_mem1 += MAIN_MEM_r[1]
	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	c_t4000 += alt(MAS)

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	c_t4000_mem0 += MAIN_MEM_r[0]
	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	c_t4000_mem1 += MAIN_MEM_r[1]
	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	c_t4001 += alt(MAS)

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	c_t4001_mem0 += MAIN_MEM_r[0]
	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	c_t4001_mem1 += MAIN_MEM_r[1]
	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	c_t4010 += alt(MAS)

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	c_t4010_mem0 += MAIN_MEM_r[0]
	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	c_t4010_mem1 += MAIN_MEM_r[1]
	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	c_t4011 += alt(MAS)

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	c_t4011_mem0 += MAIN_MEM_r[0]
	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	c_t4011_mem1 += MAIN_MEM_r[1]
	c_t4100 = S.Task('c_t4100', length=1, delay_cost=1)
	c_t4100 += alt(MAS)

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	c_t4100_mem0 += MAIN_MEM_r[0]
	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	c_t4100_mem1 += MAIN_MEM_r[1]
	c_t4101 = S.Task('c_t4101', length=1, delay_cost=1)
	c_t4101 += alt(MAS)

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	c_t4101_mem0 += MAIN_MEM_r[0]
	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	c_t4101_mem1 += MAIN_MEM_r[1]
	c_t4110 = S.Task('c_t4110', length=1, delay_cost=1)
	c_t4110 += alt(MAS)

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	c_t4110_mem0 += MAIN_MEM_r[0]
	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	c_t4110_mem1 += MAIN_MEM_r[1]
	c_t4111 = S.Task('c_t4111', length=1, delay_cost=1)
	c_t4111 += alt(MAS)

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	c_t4111_mem0 += MAIN_MEM_r[0]
	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	c_t4111_mem1 += MAIN_MEM_r[1]
	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	c_t5000 += alt(MAS)

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	c_t5000_mem0 += MAIN_MEM_r[0]
	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	c_t5000_mem1 += MAIN_MEM_r[1]
	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	c_t5001 += alt(MAS)

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	c_t5001_mem0 += MAIN_MEM_r[0]
	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	c_t5001_mem1 += MAIN_MEM_r[1]
	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	c_t5010 += alt(MAS)

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	c_t5010_mem0 += MAIN_MEM_r[0]
	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	c_t5010_mem1 += MAIN_MEM_r[1]
	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	c_t5011 += alt(MAS)

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	c_t5011_mem0 += MAIN_MEM_r[0]
	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	c_t5011_mem1 += MAIN_MEM_r[1]
	c_t5100 = S.Task('c_t5100', length=1, delay_cost=1)
	c_t5100 += alt(MAS)

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	c_t5100_mem0 += MAIN_MEM_r[0]
	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	c_t5100_mem1 += MAIN_MEM_r[1]
	c_t5101 = S.Task('c_t5101', length=1, delay_cost=1)
	c_t5101 += alt(MAS)

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	c_t5101_mem0 += MAIN_MEM_r[0]
	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	c_t5101_mem1 += MAIN_MEM_r[1]
	c_t5110 = S.Task('c_t5110', length=1, delay_cost=1)
	c_t5110 += alt(MAS)

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	c_t5110_mem0 += MAIN_MEM_r[0]
	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	c_t5110_mem1 += MAIN_MEM_r[1]
	c_t5111 = S.Task('c_t5111', length=1, delay_cost=1)
	c_t5111 += alt(MAS)

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	c_t5111_mem0 += MAIN_MEM_r[0]
	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	c_t5111_mem1 += MAIN_MEM_r[1]
	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage1MAS4/MUL/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

