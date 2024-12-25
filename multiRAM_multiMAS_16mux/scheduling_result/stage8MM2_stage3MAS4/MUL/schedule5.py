from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 205
	S = Scenario("schedule5", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=8)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 0
	c_t0_t0_t1_in += MM_in[1]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 0
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 0
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=8, delay_cost=1)
	S += c_t0_t0_t1 >= 1
	c_t0_t0_t1 += MM[1]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 1
	c_t0_t21_in += MAS_in[0]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 1
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 1
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t21 = S.Task('c_t0_t21', length=3, delay_cost=1)
	S += c_t0_t21 >= 2
	c_t0_t21 += MAS[0]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 2
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 2
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 2
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 3
	c_t0_t0_t3_in += MAS_in[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 3
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 3
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=3, delay_cost=1)
	S += c_t1_t0_t2 >= 3
	c_t1_t0_t2 += MAS[0]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=3, delay_cost=1)
	S += c_t0_t0_t3 >= 4
	c_t0_t0_t3 += MAS[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 4
	c_t0_t1_t2_in += MAS_in[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 4
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 4
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=3, delay_cost=1)
	S += c_t0_t1_t2 >= 5
	c_t0_t1_t2 += MAS[0]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 5
	c_t0_t30_in += MAS_in[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 5
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 5
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 6
	c_t0_t20_in += MAS_in[0]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 6
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 6
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t30 = S.Task('c_t0_t30', length=3, delay_cost=1)
	S += c_t0_t30 >= 6
	c_t0_t30 += MAS[0]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 7
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 7
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 7
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t20 = S.Task('c_t0_t20', length=3, delay_cost=1)
	S += c_t0_t20 >= 7
	c_t0_t20 += MAS[0]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=8, delay_cost=1)
	S += c_t0_t1_t1 >= 8
	c_t0_t1_t1 += MM[0]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 8
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 8
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 8
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=3, delay_cost=1)
	S += c_t0_t1_t3 >= 9
	c_t0_t1_t3 += MAS[0]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 9
	c_t0_t4_t2_in += MAS_in[2]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 9
	c_t0_t4_t2_mem0 += MAS_MEM[0]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 9
	c_t0_t4_t2_mem1 += MAS_MEM[1]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 9
	c_t1_t0_t3_in += MAS_in[0]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 9
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 9
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 10
	c_t0_t4_t0_in += MM_in[1]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 10
	c_t0_t4_t0_mem0 += MAS_MEM[0]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 10
	c_t0_t4_t0_mem1 += MAS_MEM[1]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=3, delay_cost=1)
	S += c_t0_t4_t2 >= 10
	c_t0_t4_t2 += MAS[2]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 10
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 10
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 10
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=3, delay_cost=1)
	S += c_t1_t0_t3 >= 10
	c_t1_t0_t3 += MAS[0]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 11
	c_t0_t1_t4_in += MM_in[1]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 11
	c_t0_t1_t4_mem0 += MAS_MEM[0]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 11
	c_t0_t1_t4_mem1 += MAS_MEM[1]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=8, delay_cost=1)
	S += c_t0_t4_t0 >= 11
	c_t0_t4_t0 += MM[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=8, delay_cost=1)
	S += c_t1_t0_t0 >= 11
	c_t1_t0_t0 += MM[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 11
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 11
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 11
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 12
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 12
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 12
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=8, delay_cost=1)
	S += c_t0_t1_t4 >= 12
	c_t0_t1_t4 += MM[1]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 12
	c_t1_t0_t4_in += MM_in[1]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 12
	c_t1_t0_t4_mem0 += MAS_MEM[0]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 12
	c_t1_t0_t4_mem1 += MAS_MEM[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=8, delay_cost=1)
	S += c_t1_t1_t0 >= 12
	c_t1_t1_t0 += MM[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=8, delay_cost=1)
	S += c_t0_t0_t0 >= 13
	c_t0_t0_t0 += MM[0]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 13
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 13
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 13
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=8, delay_cost=1)
	S += c_t1_t0_t4 >= 13
	c_t1_t0_t4 += MM[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=8, delay_cost=1)
	S += c_t1_t0_t1 >= 14
	c_t1_t0_t1 += MM[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 14
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 14
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 14
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=8, delay_cost=1)
	S += c_t1_t1_t1 >= 15
	c_t1_t1_t1 += MM[0]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 15
	c_t1_t1_t2_in += MAS_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 15
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 15
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=3, delay_cost=1)
	S += c_t1_t1_t2 >= 16
	c_t1_t1_t2 += MAS[0]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 16
	c_t1_t1_t3_in += MAS_in[0]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 16
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 16
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 17
	c_t0_t31_in += MAS_in[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 17
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 17
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=3, delay_cost=1)
	S += c_t1_t1_t3 >= 17
	c_t1_t1_t3 += MAS[0]

	c_t0_t31 = S.Task('c_t0_t31', length=3, delay_cost=1)
	S += c_t0_t31 >= 18
	c_t0_t31 += MAS[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 18
	c_t1_t20_in += MAS_in[0]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 18
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 18
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 19
	c_t0_t1_t0_in += MM_in[1]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 19
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 19
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 19
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 19
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 19
	c_t1_t1_t4_mem1 += MAS_MEM[1]

	c_t1_t20 = S.Task('c_t1_t20', length=3, delay_cost=1)
	S += c_t1_t20 >= 19
	c_t1_t20 += MAS[0]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 20
	c_t0_t0_t5_in += MAS_in[2]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 20
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 20
	c_t0_t0_t5_mem1 += MM_MEM[3]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=8, delay_cost=1)
	S += c_t0_t1_t0 >= 20
	c_t0_t1_t0 += MM[1]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 20
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 20
	c_t0_t4_t3_mem0 += MAS_MEM[0]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 20
	c_t0_t4_t3_mem1 += MAS_MEM[1]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=8, delay_cost=1)
	S += c_t1_t1_t4 >= 20
	c_t1_t1_t4 += MM[0]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 20
	c_t1_t30_in += MAS_in[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 20
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 20
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 21
	c_t0_t00_in += MAS_in[3]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 21
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 21
	c_t0_t00_mem1 += MM_MEM[3]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 21
	c_t0_t0_t2_in += MAS_in[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 21
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 21
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=3, delay_cost=1)
	S += c_t0_t0_t5 >= 21
	c_t0_t0_t5 += MAS[2]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 21
	c_t0_t4_t1_in += MM_in[1]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 21
	c_t0_t4_t1_mem0 += MAS_MEM[0]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 21
	c_t0_t4_t1_mem1 += MAS_MEM[1]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=3, delay_cost=1)
	S += c_t0_t4_t3 >= 21
	c_t0_t4_t3 += MAS[1]

	c_t1_t30 = S.Task('c_t1_t30', length=3, delay_cost=1)
	S += c_t1_t30 >= 21
	c_t1_t30 += MAS[0]

	c_t0_t00 = S.Task('c_t0_t00', length=3, delay_cost=1)
	S += c_t0_t00 >= 22
	c_t0_t00 += MAS[3]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=3, delay_cost=1)
	S += c_t0_t0_t2 >= 22
	c_t0_t0_t2 += MAS[0]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=8, delay_cost=1)
	S += c_t0_t4_t1 >= 22
	c_t0_t4_t1 += MM[1]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 22
	c_t1_t0_t5_in += MAS_in[2]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 22
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 22
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 22
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 22
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 22
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	S += c_t0_t4_t4_in >= 23
	c_t0_t4_t4_in += MM_in[1]

	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem0 >= 23
	c_t0_t4_t4_mem0 += MAS_MEM[4]

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem1 >= 23
	c_t0_t4_t4_mem1 += MAS_MEM[3]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=3, delay_cost=1)
	S += c_t1_t0_t5 >= 23
	c_t1_t0_t5 += MAS[2]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 23
	c_t1_t1_t5_in += MAS_in[1]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 23
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 23
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 23
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 23
	c_t1_t4_t0_mem0 += MAS_MEM[0]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 23
	c_t1_t4_t0_mem1 += MAS_MEM[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=8, delay_cost=1)
	S += c_t2_t0_t0 >= 23
	c_t2_t0_t0 += MM[0]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 23
	c_t2_t0_t2_in += MAS_in[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 23
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 23
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 24
	c_t0_t0_t4_in += MM_in[1]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 24
	c_t0_t0_t4_mem0 += MAS_MEM[0]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 24
	c_t0_t0_t4_mem1 += MAS_MEM[1]

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=8, delay_cost=1)
	S += c_t0_t4_t4 >= 24
	c_t0_t4_t4 += MM[1]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 24
	c_t1_t10_in += MAS_in[2]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 24
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 24
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=3, delay_cost=1)
	S += c_t1_t1_t5 >= 24
	c_t1_t1_t5 += MAS[1]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=8, delay_cost=1)
	S += c_t1_t4_t0 >= 24
	c_t1_t4_t0 += MM[0]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 24
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 24
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 24
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=3, delay_cost=1)
	S += c_t2_t0_t2 >= 24
	c_t2_t0_t2 += MAS[0]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=8, delay_cost=1)
	S += c_t0_t0_t4 >= 25
	c_t0_t0_t4 += MM[1]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 25
	c_t1_t00_in += MAS_in[0]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 25
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 25
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 25
	c_t1_t01_in += MAS_in[1]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 25
	c_t1_t01_mem0 += MM_MEM[2]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 25
	c_t1_t01_mem1 += MAS_MEM[5]

	c_t1_t10 = S.Task('c_t1_t10', length=3, delay_cost=1)
	S += c_t1_t10 >= 25
	c_t1_t10 += MAS[2]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 25
	c_t1_t31_in += MAS_in[3]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 25
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 25
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=8, delay_cost=1)
	S += c_t2_t0_t1 >= 25
	c_t2_t0_t1 += MM[0]

	c_t1_t00 = S.Task('c_t1_t00', length=3, delay_cost=1)
	S += c_t1_t00 >= 26
	c_t1_t00 += MAS[0]

	c_t1_t01 = S.Task('c_t1_t01', length=3, delay_cost=1)
	S += c_t1_t01 >= 26
	c_t1_t01 += MAS[1]

	c_t1_t31 = S.Task('c_t1_t31', length=3, delay_cost=1)
	S += c_t1_t31 >= 26
	c_t1_t31 += MAS[3]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 26
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 26
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 26
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 27
	c_t0_t1_t5_in += MAS_in[3]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 27
	c_t0_t1_t5_mem0 += MM_MEM[2]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 27
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 27
	c_t1_t11_in += MAS_in[1]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 27
	c_t1_t11_mem0 += MM_MEM[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 27
	c_t1_t11_mem1 += MAS_MEM[3]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 27
	c_t2_t0_t3_in += MAS_in[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 27
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 27
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=8, delay_cost=1)
	S += c_t2_t1_t0 >= 27
	c_t2_t1_t0 += MM[0]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 28
	c_t0_t10_in += MAS_in[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 28
	c_t0_t10_mem0 += MM_MEM[2]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 28
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=3, delay_cost=1)
	S += c_t0_t1_t5 >= 28
	c_t0_t1_t5 += MAS[3]

	c_t1_t11 = S.Task('c_t1_t11', length=3, delay_cost=1)
	S += c_t1_t11 >= 28
	c_t1_t11 += MAS[1]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 28
	c_t1_t21_in += MAS_in[2]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 28
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 28
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 28
	c_t1_t4_t3_in += MAS_in[0]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 28
	c_t1_t4_t3_mem0 += MAS_MEM[0]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 28
	c_t1_t4_t3_mem1 += MAS_MEM[7]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=3, delay_cost=1)
	S += c_t2_t0_t3 >= 28
	c_t2_t0_t3 += MAS[0]

	c_t0_t10 = S.Task('c_t0_t10', length=3, delay_cost=1)
	S += c_t0_t10 >= 29
	c_t0_t10 += MAS[1]

	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	S += c_t0_t40_in >= 29
	c_t0_t40_in += MAS_in[1]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 29
	c_t0_t40_mem0 += MM_MEM[2]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 29
	c_t0_t40_mem1 += MM_MEM[3]

	c_t1_t21 = S.Task('c_t1_t21', length=3, delay_cost=1)
	S += c_t1_t21 >= 29
	c_t1_t21 += MAS[2]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=3, delay_cost=1)
	S += c_t1_t4_t3 >= 29
	c_t1_t4_t3 += MAS[0]

	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	S += c_t1_t50_in >= 29
	c_t1_t50_in += MAS_in[0]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 29
	c_t1_t50_mem0 += MAS_MEM[0]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 29
	c_t1_t50_mem1 += MAS_MEM[5]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 29
	c_t2_t1_t1_in += MM_in[1]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 29
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 29
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 30
	c_t0_t11_in += MAS_in[0]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 30
	c_t0_t11_mem0 += MM_MEM[2]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 30
	c_t0_t11_mem1 += MAS_MEM[7]

	c_t0_t40 = S.Task('c_t0_t40', length=3, delay_cost=1)
	S += c_t0_t40 >= 30
	c_t0_t40 += MAS[1]

	c_t1_t50 = S.Task('c_t1_t50', length=3, delay_cost=1)
	S += c_t1_t50 >= 30
	c_t1_t50 += MAS[0]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 30
	c_t2_t0_t4_in += MM_in[1]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 30
	c_t2_t0_t4_mem0 += MAS_MEM[0]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 30
	c_t2_t0_t4_mem1 += MAS_MEM[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=8, delay_cost=1)
	S += c_t2_t1_t1 >= 30
	c_t2_t1_t1 += MM[1]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 30
	c_t2_t1_t3_in += MAS_in[3]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 30
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 30
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t11 = S.Task('c_t0_t11', length=3, delay_cost=1)
	S += c_t0_t11 >= 31
	c_t0_t11 += MAS[0]

	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	S += c_t0_t4_t5_in >= 31
	c_t0_t4_t5_in += MAS_in[3]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem0 >= 31
	c_t0_t4_t5_mem0 += MM_MEM[2]

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem1 >= 31
	c_t0_t4_t5_mem1 += MM_MEM[3]

	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	S += c_t0_t50_in >= 31
	c_t0_t50_in += MAS_in[2]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 31
	c_t0_t50_mem0 += MAS_MEM[6]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 31
	c_t0_t50_mem1 += MAS_MEM[3]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 31
	c_t1_t4_t1_in += MM_in[1]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 31
	c_t1_t4_t1_mem0 += MAS_MEM[4]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 31
	c_t1_t4_t1_mem1 += MAS_MEM[7]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 31
	c_t1_t4_t2_in += MAS_in[0]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 31
	c_t1_t4_t2_mem0 += MAS_MEM[0]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 31
	c_t1_t4_t2_mem1 += MAS_MEM[5]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=8, delay_cost=1)
	S += c_t2_t0_t4 >= 31
	c_t2_t0_t4 += MM[1]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 31
	c_t2_t1_t2_in += MAS_in[1]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 31
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 31
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=3, delay_cost=1)
	S += c_t2_t1_t3 >= 31
	c_t2_t1_t3 += MAS[3]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 32
	c_t0_t01_in += MAS_in[1]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 32
	c_t0_t01_mem0 += MM_MEM[2]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 32
	c_t0_t01_mem1 += MAS_MEM[5]

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=3, delay_cost=1)
	S += c_t0_t4_t5 >= 32
	c_t0_t4_t5 += MAS[3]

	c_t0_t50 = S.Task('c_t0_t50', length=3, delay_cost=1)
	S += c_t0_t50 >= 32
	c_t0_t50 += MAS[2]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=8, delay_cost=1)
	S += c_t1_t4_t1 >= 32
	c_t1_t4_t1 += MM[1]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=3, delay_cost=1)
	S += c_t1_t4_t2 >= 32
	c_t1_t4_t2 += MAS[0]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 32
	c_t2_t0_t5_in += MAS_in[0]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 32
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 32
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=3, delay_cost=1)
	S += c_t2_t1_t2 >= 32
	c_t2_t1_t2 += MAS[1]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 32
	c_t2_t30_in += MAS_in[3]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 32
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 32
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t01 = S.Task('c_t0_t01', length=3, delay_cost=1)
	S += c_t0_t01 >= 33
	c_t0_t01 += MAS[1]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 33
	c_t2_t00_in += MAS_in[0]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 33
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 33
	c_t2_t00_mem1 += MM_MEM[1]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=3, delay_cost=1)
	S += c_t2_t0_t5 >= 33
	c_t2_t0_t5 += MAS[0]

	c_t2_t30 = S.Task('c_t2_t30', length=3, delay_cost=1)
	S += c_t2_t30 >= 33
	c_t2_t30 += MAS[3]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 33
	c_t3010_in += MAS_in[2]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 33
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 33
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	S += c_t1_t4_t4_in >= 34
	c_t1_t4_t4_in += MM_in[0]

	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem0 >= 34
	c_t1_t4_t4_mem0 += MAS_MEM[0]

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem1 >= 34
	c_t1_t4_t4_mem1 += MAS_MEM[1]

	c_t2_t00 = S.Task('c_t2_t00', length=3, delay_cost=1)
	S += c_t2_t00 >= 34
	c_t2_t00 += MAS[0]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 34
	c_t2_t1_t4_in += MM_in[1]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 34
	c_t2_t1_t4_mem0 += MAS_MEM[2]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 34
	c_t2_t1_t4_mem1 += MAS_MEM[7]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 34
	c_t3001_in += MAS_in[3]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 34
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 34
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3010 = S.Task('c_t3010', length=3, delay_cost=1)
	S += c_t3010 >= 34
	c_t3010 += MAS[2]

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=8, delay_cost=1)
	S += c_t1_t4_t4 >= 35
	c_t1_t4_t4 += MM[0]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=8, delay_cost=1)
	S += c_t2_t1_t4 >= 35
	c_t2_t1_t4 += MM[1]

	c_t3001 = S.Task('c_t3001', length=3, delay_cost=1)
	S += c_t3001 >= 35
	c_t3001 += MAS[3]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 35
	c_t3011_in += MAS_in[1]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 35
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 35
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=3, delay_cost=1)
	S += c_t3011 >= 36
	c_t3011 += MAS[1]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 36
	c_t5011_in += MAS_in[0]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 36
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 36
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 37
	c_t2_t10_in += MAS_in[0]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 37
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 37
	c_t2_t10_mem1 += MM_MEM[3]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 37
	c_t2_t21_in += MAS_in[1]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 37
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 37
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=3, delay_cost=1)
	S += c_t5011 >= 37
	c_t5011 += MAS[0]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 38
	c_t2_t01_in += MAS_in[3]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 38
	c_t2_t01_mem0 += MM_MEM[2]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 38
	c_t2_t01_mem1 += MAS_MEM[1]

	c_t2_t10 = S.Task('c_t2_t10', length=3, delay_cost=1)
	S += c_t2_t10 >= 38
	c_t2_t10 += MAS[0]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 38
	c_t2_t1_t5_in += MAS_in[2]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 38
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 38
	c_t2_t1_t5_mem1 += MM_MEM[3]

	c_t2_t21 = S.Task('c_t2_t21', length=3, delay_cost=1)
	S += c_t2_t21 >= 38
	c_t2_t21 += MAS[1]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 38
	c_t3100_in += MAS_in[0]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 38
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 38
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 38
	c_t3_t21_in += MAS_in[1]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 38
	c_t3_t21_mem0 += MAS_MEM[6]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 38
	c_t3_t21_mem1 += MAS_MEM[3]

	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	S += c_t1_t4_t5_in >= 39
	c_t1_t4_t5_in += MAS_in[3]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem0 >= 39
	c_t1_t4_t5_mem0 += MM_MEM[0]

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem1 >= 39
	c_t1_t4_t5_mem1 += MM_MEM[3]

	c_t2_t01 = S.Task('c_t2_t01', length=3, delay_cost=1)
	S += c_t2_t01 >= 39
	c_t2_t01 += MAS[3]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=3, delay_cost=1)
	S += c_t2_t1_t5 >= 39
	c_t2_t1_t5 += MAS[2]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 39
	c_t2_t31_in += MAS_in[0]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 39
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 39
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t3100 = S.Task('c_t3100', length=3, delay_cost=1)
	S += c_t3100 >= 39
	c_t3100 += MAS[0]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 39
	c_t3_t1_t2_in += MAS_in[2]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 39
	c_t3_t1_t2_mem0 += MAS_MEM[4]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 39
	c_t3_t1_t2_mem1 += MAS_MEM[3]

	c_t3_t21 = S.Task('c_t3_t21', length=3, delay_cost=1)
	S += c_t3_t21 >= 39
	c_t3_t21 += MAS[1]

	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	S += c_t1_t40_in >= 40
	c_t1_t40_in += MAS_in[1]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 40
	c_t1_t40_mem0 += MM_MEM[0]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 40
	c_t1_t40_mem1 += MM_MEM[3]

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=3, delay_cost=1)
	S += c_t1_t4_t5 >= 40
	c_t1_t4_t5 += MAS[3]

	c_t2_t31 = S.Task('c_t2_t31', length=3, delay_cost=1)
	S += c_t2_t31 >= 40
	c_t2_t31 += MAS[0]

	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	S += c_t2_t50_in >= 40
	c_t2_t50_in += MAS_in[3]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 40
	c_t2_t50_mem0 += MAS_MEM[0]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 40
	c_t2_t50_mem1 += MAS_MEM[1]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 40
	c_t3000_in += MAS_in[0]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 40
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 40
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=3, delay_cost=1)
	S += c_t3_t1_t2 >= 40
	c_t3_t1_t2 += MAS[2]

	c_t1_t40 = S.Task('c_t1_t40', length=3, delay_cost=1)
	S += c_t1_t40 >= 41
	c_t1_t40 += MAS[1]

	c_t2_t50 = S.Task('c_t2_t50', length=3, delay_cost=1)
	S += c_t2_t50 >= 41
	c_t2_t50 += MAS[3]

	c_t3000 = S.Task('c_t3000', length=3, delay_cost=1)
	S += c_t3000 >= 41
	c_t3000 += MAS[0]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 41
	c_t3101_in += MAS_in[0]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 41
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 41
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 42
	c_t2_t11_in += MAS_in[3]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 42
	c_t2_t11_mem0 += MM_MEM[2]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 42
	c_t2_t11_mem1 += MAS_MEM[5]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 42
	c_t2_t4_t1_in += MM_in[1]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 42
	c_t2_t4_t1_mem0 += MAS_MEM[2]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 42
	c_t2_t4_t1_mem1 += MAS_MEM[1]

	c_t3101 = S.Task('c_t3101', length=3, delay_cost=1)
	S += c_t3101 >= 42
	c_t3101 += MAS[0]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 42
	c_t3110_in += MAS_in[0]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 42
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 42
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=3, delay_cost=1)
	S += c_t2_t11 >= 43
	c_t2_t11 += MAS[3]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=8, delay_cost=1)
	S += c_t2_t4_t1 >= 43
	c_t2_t4_t1 += MM[1]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 43
	c_t2_t4_t3_in += MAS_in[1]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 43
	c_t2_t4_t3_mem0 += MAS_MEM[6]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 43
	c_t2_t4_t3_mem1 += MAS_MEM[1]

	c_t3110 = S.Task('c_t3110', length=3, delay_cost=1)
	S += c_t3110 >= 43
	c_t3110 += MAS[0]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 43
	c_t3_t20_in += MAS_in[3]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 43
	c_t3_t20_mem0 += MAS_MEM[0]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 43
	c_t3_t20_mem1 += MAS_MEM[5]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 43
	c_t5111_in += MAS_in[0]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 43
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 43
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=3, delay_cost=1)
	S += c_t2_t4_t3 >= 44
	c_t2_t4_t3 += MAS[1]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 44
	c_t3111_in += MAS_in[0]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 44
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 44
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 44
	c_t3_t0_t1_in += MM_in[1]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 44
	c_t3_t0_t1_mem0 += MAS_MEM[6]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 44
	c_t3_t0_t1_mem1 += MAS_MEM[1]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 44
	c_t3_t0_t2_in += MAS_in[2]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 44
	c_t3_t0_t2_mem0 += MAS_MEM[0]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 44
	c_t3_t0_t2_mem1 += MAS_MEM[7]

	c_t3_t20 = S.Task('c_t3_t20', length=3, delay_cost=1)
	S += c_t3_t20 >= 44
	c_t3_t20 += MAS[3]

	c_t5111 = S.Task('c_t5111', length=3, delay_cost=1)
	S += c_t5111 >= 44
	c_t5111 += MAS[0]

	c_t3111 = S.Task('c_t3111', length=3, delay_cost=1)
	S += c_t3111 >= 45
	c_t3111 += MAS[0]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=8, delay_cost=1)
	S += c_t3_t0_t1 >= 45
	c_t3_t0_t1 += MM[1]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=3, delay_cost=1)
	S += c_t3_t0_t2 >= 45
	c_t3_t0_t2 += MAS[2]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 45
	c_t3_t1_t0_in += MM_in[1]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 45
	c_t3_t1_t0_mem0 += MAS_MEM[4]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 45
	c_t3_t1_t0_mem1 += MAS_MEM[1]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 45
	c_t4000_in += MAS_in[0]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 45
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 45
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 46
	c_t3_t0_t0_in += MM_in[1]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 46
	c_t3_t0_t0_mem0 += MAS_MEM[0]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 46
	c_t3_t0_t0_mem1 += MAS_MEM[1]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=8, delay_cost=1)
	S += c_t3_t1_t0 >= 46
	c_t3_t1_t0 += MM[1]

	c_t3_t4_t2_in = S.Task('c_t3_t4_t2_in', length=1, delay_cost=1)
	S += c_t3_t4_t2_in >= 46
	c_t3_t4_t2_in += MAS_in[2]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem0 >= 46
	c_t3_t4_t2_mem0 += MAS_MEM[6]

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem1 >= 46
	c_t3_t4_t2_mem1 += MAS_MEM[3]

	c_t4000 = S.Task('c_t4000', length=3, delay_cost=1)
	S += c_t4000 >= 46
	c_t4000 += MAS[0]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 46
	c_t4110_in += MAS_in[0]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 46
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 46
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=8, delay_cost=1)
	S += c_t3_t0_t0 >= 47
	c_t3_t0_t0 += MM[1]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 47
	c_t3_t31_in += MAS_in[2]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 47
	c_t3_t31_mem0 += MAS_MEM[0]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 47
	c_t3_t31_mem1 += MAS_MEM[1]

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=3, delay_cost=1)
	S += c_t3_t4_t2 >= 47
	c_t3_t4_t2 += MAS[2]

	c_t4110 = S.Task('c_t4110', length=3, delay_cost=1)
	S += c_t4110 >= 47
	c_t4110 += MAS[0]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 47
	c_t4111_in += MAS_in[0]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 47
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 47
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 48
	c_t3_t1_t3_in += MAS_in[3]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 48
	c_t3_t1_t3_mem0 += MAS_MEM[0]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 48
	c_t3_t1_t3_mem1 += MAS_MEM[1]

	c_t3_t31 = S.Task('c_t3_t31', length=3, delay_cost=1)
	S += c_t3_t31 >= 48
	c_t3_t31 += MAS[2]

	c_t4111 = S.Task('c_t4111', length=3, delay_cost=1)
	S += c_t4111 >= 48
	c_t4111 += MAS[0]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 48
	c_t5010_in += MAS_in[0]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 48
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 48
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 49
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 49
	c_t3_t1_t1_mem0 += MAS_MEM[2]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 49
	c_t3_t1_t1_mem1 += MAS_MEM[1]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=3, delay_cost=1)
	S += c_t3_t1_t3 >= 49
	c_t3_t1_t3 += MAS[3]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 49
	c_t5000_in += MAS_in[0]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 49
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 49
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5010 = S.Task('c_t5010', length=3, delay_cost=1)
	S += c_t5010 >= 49
	c_t5010 += MAS[0]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 50
	c_t3_t0_t3_in += MAS_in[2]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 50
	c_t3_t0_t3_mem0 += MAS_MEM[0]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 50
	c_t3_t0_t3_mem1 += MAS_MEM[1]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=8, delay_cost=1)
	S += c_t3_t1_t1 >= 50
	c_t3_t1_t1 += MM[0]

	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	S += c_t3_t4_t1_in >= 50
	c_t3_t4_t1_in += MM_in[1]

	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem0 >= 50
	c_t3_t4_t1_mem0 += MAS_MEM[2]

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem1 >= 50
	c_t3_t4_t1_mem1 += MAS_MEM[5]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 50
	c_t4010_in += MAS_in[0]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 50
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 50
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t5000 = S.Task('c_t5000', length=3, delay_cost=1)
	S += c_t5000 >= 50
	c_t5000 += MAS[0]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=3, delay_cost=1)
	S += c_t3_t0_t3 >= 51
	c_t3_t0_t3 += MAS[2]

	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	S += c_t3_t1_t4_in >= 51
	c_t3_t1_t4_in += MM_in[0]

	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem0 >= 51
	c_t3_t1_t4_mem0 += MAS_MEM[4]

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem1 >= 51
	c_t3_t1_t4_mem1 += MAS_MEM[7]

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=8, delay_cost=1)
	S += c_t3_t4_t1 >= 51
	c_t3_t4_t1 += MM[1]

	c_t4010 = S.Task('c_t4010', length=3, delay_cost=1)
	S += c_t4010 >= 51
	c_t4010 += MAS[0]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 51
	c_t4_t1_t3_in += MAS_in[3]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 51
	c_t4_t1_t3_mem0 += MAS_MEM[0]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 51
	c_t4_t1_t3_mem1 += MAS_MEM[1]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 51
	c_t5100_in += MAS_in[0]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 51
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 51
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=8, delay_cost=1)
	S += c_t3_t1_t4 >= 52
	c_t3_t1_t4 += MM[0]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 52
	c_t3_t30_in += MAS_in[2]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 52
	c_t3_t30_mem0 += MAS_MEM[0]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 52
	c_t3_t30_mem1 += MAS_MEM[1]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 52
	c_t4001_in += MAS_in[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 52
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 52
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=3, delay_cost=1)
	S += c_t4_t1_t3 >= 52
	c_t4_t1_t3 += MAS[3]

	c_t5100 = S.Task('c_t5100', length=3, delay_cost=1)
	S += c_t5100 >= 52
	c_t5100 += MAS[0]

	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	S += c_t3_t0_t4_in >= 53
	c_t3_t0_t4_in += MM_in[0]

	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem0 >= 53
	c_t3_t0_t4_mem0 += MAS_MEM[4]

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem1 >= 53
	c_t3_t0_t4_mem1 += MAS_MEM[5]

	c_t3_t30 = S.Task('c_t3_t30', length=3, delay_cost=1)
	S += c_t3_t30 >= 53
	c_t3_t30 += MAS[2]

	c_t4001 = S.Task('c_t4001', length=3, delay_cost=1)
	S += c_t4001 >= 53
	c_t4001 += MAS[0]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 53
	c_t4_t1_t0_in += MM_in[1]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 53
	c_t4_t1_t0_mem0 += MAS_MEM[0]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 53
	c_t4_t1_t0_mem1 += MAS_MEM[1]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 53
	c_t5001_in += MAS_in[0]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 53
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 53
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	S += c_t3_t00_in >= 54
	c_t3_t00_in += MAS_in[1]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 54
	c_t3_t00_mem0 += MM_MEM[2]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 54
	c_t3_t00_mem1 += MM_MEM[3]

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=8, delay_cost=1)
	S += c_t3_t0_t4 >= 54
	c_t3_t0_t4 += MM[0]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 54
	c_t4101_in += MAS_in[0]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 54
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 54
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=8, delay_cost=1)
	S += c_t4_t1_t0 >= 54
	c_t4_t1_t0 += MM[1]

	c_t5001 = S.Task('c_t5001', length=3, delay_cost=1)
	S += c_t5001 >= 54
	c_t5001 += MAS[0]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 54
	c_t5_t20_in += MAS_in[2]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 54
	c_t5_t20_mem0 += MAS_MEM[0]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 54
	c_t5_t20_mem1 += MAS_MEM[1]

	c_t3_t00 = S.Task('c_t3_t00', length=3, delay_cost=1)
	S += c_t3_t00 >= 55
	c_t3_t00 += MAS[1]

	c_t3_t0_t5_in = S.Task('c_t3_t0_t5_in', length=1, delay_cost=1)
	S += c_t3_t0_t5_in >= 55
	c_t3_t0_t5_in += MAS_in[1]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem0 >= 55
	c_t3_t0_t5_mem0 += MM_MEM[2]

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem1 >= 55
	c_t3_t0_t5_mem1 += MM_MEM[3]

	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	S += c_t3_t4_t0_in >= 55
	c_t3_t4_t0_in += MM_in[1]

	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem0 >= 55
	c_t3_t4_t0_mem0 += MAS_MEM[6]

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem1 >= 55
	c_t3_t4_t0_mem1 += MAS_MEM[5]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 55
	c_t4011_in += MAS_in[0]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 55
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 55
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4101 = S.Task('c_t4101', length=3, delay_cost=1)
	S += c_t4101 >= 55
	c_t4101 += MAS[0]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 55
	c_t4_t0_t2_in += MAS_in[2]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 55
	c_t4_t0_t2_mem0 += MAS_MEM[0]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 55
	c_t4_t0_t2_mem1 += MAS_MEM[1]

	c_t5_t20 = S.Task('c_t5_t20', length=3, delay_cost=1)
	S += c_t5_t20 >= 55
	c_t5_t20 += MAS[2]

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=3, delay_cost=1)
	S += c_t3_t0_t5 >= 56
	c_t3_t0_t5 += MAS[1]

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=8, delay_cost=1)
	S += c_t3_t4_t0 >= 56
	c_t3_t4_t0 += MM[1]

	c_t3_t4_t3_in = S.Task('c_t3_t4_t3_in', length=1, delay_cost=1)
	S += c_t3_t4_t3_in >= 56
	c_t3_t4_t3_in += MAS_in[3]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem0 >= 56
	c_t3_t4_t3_mem0 += MAS_MEM[4]

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem1 >= 56
	c_t3_t4_t3_mem1 += MAS_MEM[5]

	c_t4011 = S.Task('c_t4011', length=3, delay_cost=1)
	S += c_t4011 >= 56
	c_t4011 += MAS[0]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=3, delay_cost=1)
	S += c_t4_t0_t2 >= 56
	c_t4_t0_t2 += MAS[2]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 56
	c_t5101_in += MAS_in[0]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 56
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 56
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 56
	c_t5_t21_in += MAS_in[2]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 56
	c_t5_t21_mem0 += MAS_MEM[0]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 56
	c_t5_t21_mem1 += MAS_MEM[1]

	c_t3_t1_t5_in = S.Task('c_t3_t1_t5_in', length=1, delay_cost=1)
	S += c_t3_t1_t5_in >= 57
	c_t3_t1_t5_in += MAS_in[1]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem0 >= 57
	c_t3_t1_t5_mem0 += MM_MEM[2]

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem1 >= 57
	c_t3_t1_t5_mem1 += MM_MEM[1]

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=3, delay_cost=1)
	S += c_t3_t4_t3 >= 57
	c_t3_t4_t3 += MAS[3]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 57
	c_t4100_in += MAS_in[0]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 57
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 57
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 57
	c_t4_t0_t1_in += MM_in[1]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 57
	c_t4_t0_t1_mem0 += MAS_MEM[0]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 57
	c_t4_t0_t1_mem1 += MAS_MEM[1]

	c_t5101 = S.Task('c_t5101', length=3, delay_cost=1)
	S += c_t5101 >= 57
	c_t5101 += MAS[0]

	c_t5_t21 = S.Task('c_t5_t21', length=3, delay_cost=1)
	S += c_t5_t21 >= 57
	c_t5_t21 += MAS[2]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 58
	c_t3_t10_in += MAS_in[0]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 58
	c_t3_t10_mem0 += MM_MEM[2]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 58
	c_t3_t10_mem1 += MM_MEM[1]

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=3, delay_cost=1)
	S += c_t3_t1_t5 >= 58
	c_t3_t1_t5 += MAS[1]

	c_t4100 = S.Task('c_t4100', length=3, delay_cost=1)
	S += c_t4100 >= 58
	c_t4100 += MAS[0]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=8, delay_cost=1)
	S += c_t4_t0_t1 >= 58
	c_t4_t0_t1 += MM[1]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 58
	c_t4_t1_t1_in += MM_in[1]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 58
	c_t4_t1_t1_mem0 += MAS_MEM[0]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 58
	c_t4_t1_t1_mem1 += MAS_MEM[1]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 58
	c_t5110_in += MAS_in[3]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 58
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 58
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 59
	c_t2_t20_in += MAS_in[1]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 59
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 59
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t3_t10 = S.Task('c_t3_t10', length=3, delay_cost=1)
	S += c_t3_t10 >= 59
	c_t3_t10 += MAS[0]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=8, delay_cost=1)
	S += c_t4_t1_t1 >= 59
	c_t4_t1_t1 += MM[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 59
	c_t4_t1_t2_in += MAS_in[0]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 59
	c_t4_t1_t2_mem0 += MAS_MEM[0]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 59
	c_t4_t1_t2_mem1 += MAS_MEM[1]

	c_t5110 = S.Task('c_t5110', length=3, delay_cost=1)
	S += c_t5110 >= 59
	c_t5110 += MAS[3]

	c_t5_t4_t2_in = S.Task('c_t5_t4_t2_in', length=1, delay_cost=1)
	S += c_t5_t4_t2_in >= 59
	c_t5_t4_t2_in += MAS_in[2]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem0 >= 59
	c_t5_t4_t2_mem0 += MAS_MEM[4]

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem1 >= 59
	c_t5_t4_t2_mem1 += MAS_MEM[5]

	c_t2_t20 = S.Task('c_t2_t20', length=3, delay_cost=1)
	S += c_t2_t20 >= 60
	c_t2_t20 += MAS[1]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 60
	c_t4_t0_t3_in += MAS_in[2]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 60
	c_t4_t0_t3_mem0 += MAS_MEM[0]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 60
	c_t4_t0_t3_mem1 += MAS_MEM[1]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=3, delay_cost=1)
	S += c_t4_t1_t2 >= 60
	c_t4_t1_t2 += MAS[0]

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=3, delay_cost=1)
	S += c_t5_t4_t2 >= 60
	c_t5_t4_t2 += MAS[2]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 61
	c_t4_t0_t0_in += MM_in[1]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 61
	c_t4_t0_t0_mem0 += MAS_MEM[0]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 61
	c_t4_t0_t0_mem1 += MAS_MEM[1]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=3, delay_cost=1)
	S += c_t4_t0_t3 >= 61
	c_t4_t0_t3 += MAS[2]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 62
	c_t2_t4_t2_in += MAS_in[2]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 62
	c_t2_t4_t2_mem0 += MAS_MEM[2]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 62
	c_t2_t4_t2_mem1 += MAS_MEM[3]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=8, delay_cost=1)
	S += c_t4_t0_t0 >= 62
	c_t4_t0_t0 += MM[1]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 62
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 62
	c_t5_t1_t0_mem0 += MAS_MEM[0]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 62
	c_t5_t1_t0_mem1 += MAS_MEM[7]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 62
	c_t5_t1_t3_in += MAS_in[1]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 62
	c_t5_t1_t3_mem0 += MAS_MEM[6]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 62
	c_t5_t1_t3_mem1 += MAS_MEM[1]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 63
	c_t2_t4_t0_in += MM_in[1]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 63
	c_t2_t4_t0_mem0 += MAS_MEM[2]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 63
	c_t2_t4_t0_mem1 += MAS_MEM[7]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=3, delay_cost=1)
	S += c_t2_t4_t2 >= 63
	c_t2_t4_t2 += MAS[2]

	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	S += c_t4_t0_t4_in >= 63
	c_t4_t0_t4_in += MM_in[0]

	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem0 >= 63
	c_t4_t0_t4_mem0 += MAS_MEM[4]

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem1 >= 63
	c_t4_t0_t4_mem1 += MAS_MEM[5]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 63
	c_t4_t20_in += MAS_in[0]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 63
	c_t4_t20_mem0 += MAS_MEM[0]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 63
	c_t4_t20_mem1 += MAS_MEM[1]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=8, delay_cost=1)
	S += c_t5_t1_t0 >= 63
	c_t5_t1_t0 += MM[0]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=3, delay_cost=1)
	S += c_t5_t1_t3 >= 63
	c_t5_t1_t3 += MAS[1]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=8, delay_cost=1)
	S += c_t2_t4_t0 >= 64
	c_t2_t4_t0 += MM[1]

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=8, delay_cost=1)
	S += c_t4_t0_t4 >= 64
	c_t4_t0_t4 += MM[0]

	c_t4_t20 = S.Task('c_t4_t20', length=3, delay_cost=1)
	S += c_t4_t20 >= 64
	c_t4_t20 += MAS[0]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 64
	c_t4_t31_in += MAS_in[0]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 64
	c_t4_t31_mem0 += MAS_MEM[0]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 64
	c_t4_t31_mem1 += MAS_MEM[1]

	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	S += c_t2_t4_t4_in >= 65
	c_t2_t4_t4_in += MM_in[0]

	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem0 >= 65
	c_t2_t4_t4_mem0 += MAS_MEM[4]

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem1 >= 65
	c_t2_t4_t4_mem1 += MAS_MEM[3]

	c_t4_t31 = S.Task('c_t4_t31', length=3, delay_cost=1)
	S += c_t4_t31 >= 65
	c_t4_t31 += MAS[0]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 65
	c_t5_t0_t1_in += MM_in[1]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 65
	c_t5_t0_t1_mem0 += MAS_MEM[0]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 65
	c_t5_t0_t1_mem1 += MAS_MEM[1]

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=8, delay_cost=1)
	S += c_t2_t4_t4 >= 66
	c_t2_t4_t4 += MM[0]

	c_t4_t1_t5_in = S.Task('c_t4_t1_t5_in', length=1, delay_cost=1)
	S += c_t4_t1_t5_in >= 66
	c_t4_t1_t5_in += MAS_in[1]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem0 >= 66
	c_t4_t1_t5_mem0 += MM_MEM[2]

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem1 >= 66
	c_t4_t1_t5_mem1 += MM_MEM[3]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=8, delay_cost=1)
	S += c_t5_t0_t1 >= 66
	c_t5_t0_t1 += MM[1]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 66
	c_t5_t0_t3_in += MAS_in[2]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 66
	c_t5_t0_t3_mem0 += MAS_MEM[0]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 66
	c_t5_t0_t3_mem1 += MAS_MEM[1]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 67
	c_t4_t10_in += MAS_in[0]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 67
	c_t4_t10_mem0 += MM_MEM[2]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 67
	c_t4_t10_mem1 += MM_MEM[3]

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=3, delay_cost=1)
	S += c_t4_t1_t5 >= 67
	c_t4_t1_t5 += MAS[1]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=3, delay_cost=1)
	S += c_t5_t0_t3 >= 67
	c_t5_t0_t3 += MAS[2]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 67
	c_t5_t31_in += MAS_in[3]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 67
	c_t5_t31_mem0 += MAS_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 67
	c_t5_t31_mem1 += MAS_MEM[1]

	c_t4_t10 = S.Task('c_t4_t10', length=3, delay_cost=1)
	S += c_t4_t10 >= 68
	c_t4_t10 += MAS[0]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 68
	c_t5_t0_t2_in += MAS_in[3]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 68
	c_t5_t0_t2_mem0 += MAS_MEM[0]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 68
	c_t5_t0_t2_mem1 += MAS_MEM[1]

	c_t5_t31 = S.Task('c_t5_t31', length=3, delay_cost=1)
	S += c_t5_t31 >= 68
	c_t5_t31 += MAS[3]

	c_t4_t0_t5_in = S.Task('c_t4_t0_t5_in', length=1, delay_cost=1)
	S += c_t4_t0_t5_in >= 69
	c_t4_t0_t5_in += MAS_in[2]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem0 >= 69
	c_t4_t0_t5_mem0 += MM_MEM[2]

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem1 >= 69
	c_t4_t0_t5_mem1 += MM_MEM[3]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=3, delay_cost=1)
	S += c_t5_t0_t2 >= 69
	c_t5_t0_t2 += MAS[3]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 69
	c_t5_t1_t2_in += MAS_in[0]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 69
	c_t5_t1_t2_mem0 += MAS_MEM[0]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 69
	c_t5_t1_t2_mem1 += MAS_MEM[1]

	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	S += c_t4_t00_in >= 70
	c_t4_t00_in += MAS_in[0]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 70
	c_t4_t00_mem0 += MM_MEM[2]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 70
	c_t4_t00_mem1 += MM_MEM[3]

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=3, delay_cost=1)
	S += c_t4_t0_t5 >= 70
	c_t4_t0_t5 += MAS[2]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 70
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 70
	c_t5_t0_t0_mem0 += MAS_MEM[0]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 70
	c_t5_t0_t0_mem1 += MAS_MEM[1]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=3, delay_cost=1)
	S += c_t5_t1_t2 >= 70
	c_t5_t1_t2 += MAS[0]

	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	S += c_t5_t4_t1_in >= 70
	c_t5_t4_t1_in += MM_in[1]

	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem0 >= 70
	c_t5_t4_t1_mem0 += MAS_MEM[4]

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem1 >= 70
	c_t5_t4_t1_mem1 += MAS_MEM[7]

	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	S += c_t2_t40_in >= 71
	c_t2_t40_in += MAS_in[0]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 71
	c_t2_t40_mem0 += MM_MEM[2]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 71
	c_t2_t40_mem1 += MM_MEM[3]

	c_t4_t00 = S.Task('c_t4_t00', length=3, delay_cost=1)
	S += c_t4_t00 >= 71
	c_t4_t00 += MAS[0]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 71
	c_t4_t30_in += MAS_in[1]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 71
	c_t4_t30_mem0 += MAS_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 71
	c_t4_t30_mem1 += MAS_MEM[1]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=8, delay_cost=1)
	S += c_t5_t0_t0 >= 71
	c_t5_t0_t0 += MM[0]

	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	S += c_t5_t0_t4_in >= 71
	c_t5_t0_t4_in += MM_in[0]

	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem0 >= 71
	c_t5_t0_t4_mem0 += MAS_MEM[6]

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem1 >= 71
	c_t5_t0_t4_mem1 += MAS_MEM[5]

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=8, delay_cost=1)
	S += c_t5_t4_t1 >= 71
	c_t5_t4_t1 += MM[1]

	c_t2_t40 = S.Task('c_t2_t40', length=3, delay_cost=1)
	S += c_t2_t40 >= 72
	c_t2_t40 += MAS[0]

	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	S += c_t2_t4_t5_in >= 72
	c_t2_t4_t5_in += MAS_in[0]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem0 >= 72
	c_t2_t4_t5_mem0 += MM_MEM[2]

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem1 >= 72
	c_t2_t4_t5_mem1 += MM_MEM[3]

	c_t4_t30 = S.Task('c_t4_t30', length=3, delay_cost=1)
	S += c_t4_t30 >= 72
	c_t4_t30 += MAS[1]

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=8, delay_cost=1)
	S += c_t5_t0_t4 >= 72
	c_t5_t0_t4 += MM[0]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 72
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 72
	c_t5_t1_t1_mem0 += MAS_MEM[0]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 72
	c_t5_t1_t1_mem1 += MAS_MEM[1]

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=3, delay_cost=1)
	S += c_t2_t4_t5 >= 73
	c_t2_t4_t5 += MAS[0]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=8, delay_cost=1)
	S += c_t5_t1_t1 >= 73
	c_t5_t1_t1 += MM[0]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 73
	c_t5_t30_in += MAS_in[1]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 73
	c_t5_t30_mem0 += MAS_MEM[0]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 73
	c_t5_t30_mem1 += MAS_MEM[7]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 74
	c_t4_t21_in += MAS_in[1]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 74
	c_t4_t21_mem0 += MAS_MEM[0]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 74
	c_t4_t21_mem1 += MAS_MEM[1]

	c_t5_t30 = S.Task('c_t5_t30', length=3, delay_cost=1)
	S += c_t5_t30 >= 74
	c_t5_t30 += MAS[1]

	c_t4_t21 = S.Task('c_t4_t21', length=3, delay_cost=1)
	S += c_t4_t21 >= 75
	c_t4_t21 += MAS[1]

	c_t4_t4_t3_in = S.Task('c_t4_t4_t3_in', length=1, delay_cost=1)
	S += c_t4_t4_t3_in >= 75
	c_t4_t4_t3_in += MAS_in[2]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem0 >= 75
	c_t4_t4_t3_mem0 += MAS_MEM[2]

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem1 >= 75
	c_t4_t4_t3_mem1 += MAS_MEM[1]

	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	S += c_t5_t1_t4_in >= 75
	c_t5_t1_t4_in += MM_in[0]

	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem0 >= 75
	c_t5_t1_t4_mem0 += MAS_MEM[0]

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem1 >= 75
	c_t5_t1_t4_mem1 += MAS_MEM[3]

	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	S += c_t4_t1_t4_in >= 76
	c_t4_t1_t4_in += MM_in[1]

	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem0 >= 76
	c_t4_t1_t4_mem0 += MAS_MEM[0]

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem1 >= 76
	c_t4_t1_t4_mem1 += MAS_MEM[7]

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=3, delay_cost=1)
	S += c_t4_t4_t3 >= 76
	c_t4_t4_t3 += MAS[2]

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=8, delay_cost=1)
	S += c_t5_t1_t4 >= 76
	c_t5_t1_t4 += MM[0]

	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	S += c_t5_t4_t0_in >= 76
	c_t5_t4_t0_in += MM_in[0]

	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem0 >= 76
	c_t5_t4_t0_mem0 += MAS_MEM[4]

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem1 >= 76
	c_t5_t4_t0_mem1 += MAS_MEM[3]

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=8, delay_cost=1)
	S += c_t4_t1_t4 >= 77
	c_t4_t1_t4 += MM[1]

	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	S += c_t4_t4_t0_in >= 77
	c_t4_t4_t0_in += MM_in[1]

	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem0 >= 77
	c_t4_t4_t0_mem0 += MAS_MEM[0]

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem1 >= 77
	c_t4_t4_t0_mem1 += MAS_MEM[3]

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=8, delay_cost=1)
	S += c_t5_t4_t0 >= 77
	c_t5_t4_t0 += MM[0]

	c_t5_t4_t3_in = S.Task('c_t5_t4_t3_in', length=1, delay_cost=1)
	S += c_t5_t4_t3_in >= 77
	c_t5_t4_t3_in += MAS_in[2]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem0 >= 77
	c_t5_t4_t3_mem0 += MAS_MEM[2]

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem1 >= 77
	c_t5_t4_t3_mem1 += MAS_MEM[7]

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=8, delay_cost=1)
	S += c_t4_t4_t0 >= 78
	c_t4_t4_t0 += MM[1]

	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	S += c_t4_t4_t1_in >= 78
	c_t4_t4_t1_in += MM_in[0]

	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem0 >= 78
	c_t4_t4_t1_mem0 += MAS_MEM[2]

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem1 >= 78
	c_t4_t4_t1_mem1 += MAS_MEM[1]

	c_t4_t4_t2_in = S.Task('c_t4_t4_t2_in', length=1, delay_cost=1)
	S += c_t4_t4_t2_in >= 78
	c_t4_t4_t2_in += MAS_in[2]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem0 >= 78
	c_t4_t4_t2_mem0 += MAS_MEM[0]

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem1 >= 78
	c_t4_t4_t2_mem1 += MAS_MEM[3]

	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	S += c_t5_t00_in >= 78
	c_t5_t00_in += MAS_in[0]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 78
	c_t5_t00_mem0 += MM_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 78
	c_t5_t00_mem1 += MM_MEM[3]

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=3, delay_cost=1)
	S += c_t5_t4_t3 >= 78
	c_t5_t4_t3 += MAS[2]

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=8, delay_cost=1)
	S += c_t4_t4_t1 >= 79
	c_t4_t4_t1 += MM[0]

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=3, delay_cost=1)
	S += c_t4_t4_t2 >= 79
	c_t4_t4_t2 += MAS[2]

	c_t5_t00 = S.Task('c_t5_t00', length=3, delay_cost=1)
	S += c_t5_t00 >= 79
	c_t5_t00 += MAS[0]

	c_t5_t0_t5_in = S.Task('c_t5_t0_t5_in', length=1, delay_cost=1)
	S += c_t5_t0_t5_in >= 79
	c_t5_t0_t5_in += MAS_in[3]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem0 >= 79
	c_t5_t0_t5_mem0 += MM_MEM[0]

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem1 >= 79
	c_t5_t0_t5_mem1 += MM_MEM[3]

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=3, delay_cost=1)
	S += c_t5_t0_t5 >= 80
	c_t5_t0_t5 += MAS[3]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 80
	c_t5_t10_in += MAS_in[0]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 80
	c_t5_t10_mem0 += MM_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 80
	c_t5_t10_mem1 += MM_MEM[1]

	c_t5_t10 = S.Task('c_t5_t10', length=3, delay_cost=1)
	S += c_t5_t10 >= 81
	c_t5_t10 += MAS[0]

	c_t5_t1_t5_in = S.Task('c_t5_t1_t5_in', length=1, delay_cost=1)
	S += c_t5_t1_t5_in >= 81
	c_t5_t1_t5_in += MAS_in[0]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem0 >= 81
	c_t5_t1_t5_mem0 += MM_MEM[0]

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem1 >= 81
	c_t5_t1_t5_mem1 += MM_MEM[1]

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=3, delay_cost=1)
	S += c_t5_t1_t5 >= 82
	c_t5_t1_t5 += MAS[0]


	# new tasks
	c_t0_t41 = S.Task('c_t0_t41', length=3, delay_cost=1)
	c_t0_t41 += alt(MAS)
	c_t0_t41_in = S.Task('c_t0_t41_in', length=1, delay_cost=1)
	c_t0_t41_in += alt(MAS_in)
	S += c_t0_t41_in*MAS_in[0]<=c_t0_t41*MAS[0]

	S += c_t0_t41_in*MAS_in[1]<=c_t0_t41*MAS[1]

	S += c_t0_t41_in*MAS_in[2]<=c_t0_t41*MAS[2]

	S += c_t0_t41_in*MAS_in[3]<=c_t0_t41*MAS[3]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	c_t0_t41_mem0 += MM_MEM[2]
	S += 31 < c_t0_t41_mem0
	S += c_t0_t41_mem0 <= c_t0_t41

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	c_t0_t41_mem1 += MAS_MEM[7]
	S += 34 < c_t0_t41_mem1
	S += c_t0_t41_mem1 <= c_t0_t41

	c_t0_s00 = S.Task('c_t0_s00', length=3, delay_cost=1)
	c_t0_s00 += alt(MAS)
	c_t0_s00_in = S.Task('c_t0_s00_in', length=1, delay_cost=1)
	c_t0_s00_in += alt(MAS_in)
	S += c_t0_s00_in*MAS_in[0]<=c_t0_s00*MAS[0]

	S += c_t0_s00_in*MAS_in[1]<=c_t0_s00*MAS[1]

	S += c_t0_s00_in*MAS_in[2]<=c_t0_s00*MAS[2]

	S += c_t0_s00_in*MAS_in[3]<=c_t0_s00*MAS[3]

	c_t0_s00_mem0 = S.Task('c_t0_s00_mem0', length=1, delay_cost=1)
	c_t0_s00_mem0 += MAS_MEM[2]
	S += 31 < c_t0_s00_mem0
	S += c_t0_s00_mem0 <= c_t0_s00

	c_t0_s00_mem1 = S.Task('c_t0_s00_mem1', length=1, delay_cost=1)
	c_t0_s00_mem1 += MAS_MEM[1]
	S += 33 < c_t0_s00_mem1
	S += c_t0_s00_mem1 <= c_t0_s00

	c_t0_s01 = S.Task('c_t0_s01', length=3, delay_cost=1)
	c_t0_s01 += alt(MAS)
	c_t0_s01_in = S.Task('c_t0_s01_in', length=1, delay_cost=1)
	c_t0_s01_in += alt(MAS_in)
	S += c_t0_s01_in*MAS_in[0]<=c_t0_s01*MAS[0]

	S += c_t0_s01_in*MAS_in[1]<=c_t0_s01*MAS[1]

	S += c_t0_s01_in*MAS_in[2]<=c_t0_s01*MAS[2]

	S += c_t0_s01_in*MAS_in[3]<=c_t0_s01*MAS[3]

	c_t0_s01_mem0 = S.Task('c_t0_s01_mem0', length=1, delay_cost=1)
	c_t0_s01_mem0 += MAS_MEM[0]
	S += 33 < c_t0_s01_mem0
	S += c_t0_s01_mem0 <= c_t0_s01

	c_t0_s01_mem1 = S.Task('c_t0_s01_mem1', length=1, delay_cost=1)
	c_t0_s01_mem1 += MAS_MEM[3]
	S += 31 < c_t0_s01_mem1
	S += c_t0_s01_mem1 <= c_t0_s01

	c_t0_t51 = S.Task('c_t0_t51', length=3, delay_cost=1)
	c_t0_t51 += alt(MAS)
	c_t0_t51_in = S.Task('c_t0_t51_in', length=1, delay_cost=1)
	c_t0_t51_in += alt(MAS_in)
	S += c_t0_t51_in*MAS_in[0]<=c_t0_t51*MAS[0]

	S += c_t0_t51_in*MAS_in[1]<=c_t0_t51*MAS[1]

	S += c_t0_t51_in*MAS_in[2]<=c_t0_t51*MAS[2]

	S += c_t0_t51_in*MAS_in[3]<=c_t0_t51*MAS[3]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	c_t0_t51_mem0 += MAS_MEM[2]
	S += 35 < c_t0_t51_mem0
	S += c_t0_t51_mem0 <= c_t0_t51

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	c_t0_t51_mem1 += MAS_MEM[1]
	S += 33 < c_t0_t51_mem1
	S += c_t0_t51_mem1 <= c_t0_t51

	c_t010 = S.Task('c_t010', length=3, delay_cost=1)
	c_t010 += alt(MAS)
	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	c_t010_in += alt(MAS_in)
	S += c_t010_in*MAS_in[0]<=c_t010*MAS[0]

	S += c_t010_in*MAS_in[1]<=c_t010*MAS[1]

	S += c_t010_in*MAS_in[2]<=c_t010*MAS[2]

	S += c_t010_in*MAS_in[3]<=c_t010*MAS[3]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	c_t010_mem0 += MAS_MEM[2]
	S += 32 < c_t010_mem0
	S += c_t010_mem0 <= c_t010

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	c_t010_mem1 += MAS_MEM[5]
	S += 34 < c_t010_mem1
	S += c_t010_mem1 <= c_t010

	c_t1_t41 = S.Task('c_t1_t41', length=3, delay_cost=1)
	c_t1_t41 += alt(MAS)
	c_t1_t41_in = S.Task('c_t1_t41_in', length=1, delay_cost=1)
	c_t1_t41_in += alt(MAS_in)
	S += c_t1_t41_in*MAS_in[0]<=c_t1_t41*MAS[0]

	S += c_t1_t41_in*MAS_in[1]<=c_t1_t41*MAS[1]

	S += c_t1_t41_in*MAS_in[2]<=c_t1_t41*MAS[2]

	S += c_t1_t41_in*MAS_in[3]<=c_t1_t41*MAS[3]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	c_t1_t41_mem0 += MM_MEM[0]
	S += 42 < c_t1_t41_mem0
	S += c_t1_t41_mem0 <= c_t1_t41

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	c_t1_t41_mem1 += MAS_MEM[7]
	S += 42 < c_t1_t41_mem1
	S += c_t1_t41_mem1 <= c_t1_t41

	c_t1_s00 = S.Task('c_t1_s00', length=3, delay_cost=1)
	c_t1_s00 += alt(MAS)
	c_t1_s00_in = S.Task('c_t1_s00_in', length=1, delay_cost=1)
	c_t1_s00_in += alt(MAS_in)
	S += c_t1_s00_in*MAS_in[0]<=c_t1_s00*MAS[0]

	S += c_t1_s00_in*MAS_in[1]<=c_t1_s00*MAS[1]

	S += c_t1_s00_in*MAS_in[2]<=c_t1_s00*MAS[2]

	S += c_t1_s00_in*MAS_in[3]<=c_t1_s00*MAS[3]

	c_t1_s00_mem0 = S.Task('c_t1_s00_mem0', length=1, delay_cost=1)
	c_t1_s00_mem0 += MAS_MEM[4]
	S += 27 < c_t1_s00_mem0
	S += c_t1_s00_mem0 <= c_t1_s00

	c_t1_s00_mem1 = S.Task('c_t1_s00_mem1', length=1, delay_cost=1)
	c_t1_s00_mem1 += MAS_MEM[3]
	S += 30 < c_t1_s00_mem1
	S += c_t1_s00_mem1 <= c_t1_s00

	c_t1_s01 = S.Task('c_t1_s01', length=3, delay_cost=1)
	c_t1_s01 += alt(MAS)
	c_t1_s01_in = S.Task('c_t1_s01_in', length=1, delay_cost=1)
	c_t1_s01_in += alt(MAS_in)
	S += c_t1_s01_in*MAS_in[0]<=c_t1_s01*MAS[0]

	S += c_t1_s01_in*MAS_in[1]<=c_t1_s01*MAS[1]

	S += c_t1_s01_in*MAS_in[2]<=c_t1_s01*MAS[2]

	S += c_t1_s01_in*MAS_in[3]<=c_t1_s01*MAS[3]

	c_t1_s01_mem0 = S.Task('c_t1_s01_mem0', length=1, delay_cost=1)
	c_t1_s01_mem0 += MAS_MEM[2]
	S += 30 < c_t1_s01_mem0
	S += c_t1_s01_mem0 <= c_t1_s01

	c_t1_s01_mem1 = S.Task('c_t1_s01_mem1', length=1, delay_cost=1)
	c_t1_s01_mem1 += MAS_MEM[5]
	S += 27 < c_t1_s01_mem1
	S += c_t1_s01_mem1 <= c_t1_s01

	c_t1_t51 = S.Task('c_t1_t51', length=3, delay_cost=1)
	c_t1_t51 += alt(MAS)
	c_t1_t51_in = S.Task('c_t1_t51_in', length=1, delay_cost=1)
	c_t1_t51_in += alt(MAS_in)
	S += c_t1_t51_in*MAS_in[0]<=c_t1_t51*MAS[0]

	S += c_t1_t51_in*MAS_in[1]<=c_t1_t51*MAS[1]

	S += c_t1_t51_in*MAS_in[2]<=c_t1_t51*MAS[2]

	S += c_t1_t51_in*MAS_in[3]<=c_t1_t51*MAS[3]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	c_t1_t51_mem0 += MAS_MEM[2]
	S += 28 < c_t1_t51_mem0
	S += c_t1_t51_mem0 <= c_t1_t51

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	c_t1_t51_mem1 += MAS_MEM[3]
	S += 30 < c_t1_t51_mem1
	S += c_t1_t51_mem1 <= c_t1_t51

	c_t110 = S.Task('c_t110', length=3, delay_cost=1)
	c_t110 += alt(MAS)
	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	c_t110_in += alt(MAS_in)
	S += c_t110_in*MAS_in[0]<=c_t110*MAS[0]

	S += c_t110_in*MAS_in[1]<=c_t110*MAS[1]

	S += c_t110_in*MAS_in[2]<=c_t110*MAS[2]

	S += c_t110_in*MAS_in[3]<=c_t110*MAS[3]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	c_t110_mem0 += MAS_MEM[2]
	S += 43 < c_t110_mem0
	S += c_t110_mem0 <= c_t110

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	c_t110_mem1 += MAS_MEM[1]
	S += 32 < c_t110_mem1
	S += c_t110_mem1 <= c_t110

	c_t2_t41 = S.Task('c_t2_t41', length=3, delay_cost=1)
	c_t2_t41 += alt(MAS)
	c_t2_t41_in = S.Task('c_t2_t41_in', length=1, delay_cost=1)
	c_t2_t41_in += alt(MAS_in)
	S += c_t2_t41_in*MAS_in[0]<=c_t2_t41*MAS[0]

	S += c_t2_t41_in*MAS_in[1]<=c_t2_t41*MAS[1]

	S += c_t2_t41_in*MAS_in[2]<=c_t2_t41*MAS[2]

	S += c_t2_t41_in*MAS_in[3]<=c_t2_t41*MAS[3]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	c_t2_t41_mem0 += MM_MEM[0]
	S += 73 < c_t2_t41_mem0
	S += c_t2_t41_mem0 <= c_t2_t41

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	c_t2_t41_mem1 += MAS_MEM[1]
	S += 75 < c_t2_t41_mem1
	S += c_t2_t41_mem1 <= c_t2_t41

	c_t2_s00 = S.Task('c_t2_s00', length=3, delay_cost=1)
	c_t2_s00 += alt(MAS)
	c_t2_s00_in = S.Task('c_t2_s00_in', length=1, delay_cost=1)
	c_t2_s00_in += alt(MAS_in)
	S += c_t2_s00_in*MAS_in[0]<=c_t2_s00*MAS[0]

	S += c_t2_s00_in*MAS_in[1]<=c_t2_s00*MAS[1]

	S += c_t2_s00_in*MAS_in[2]<=c_t2_s00*MAS[2]

	S += c_t2_s00_in*MAS_in[3]<=c_t2_s00*MAS[3]

	c_t2_s00_mem0 = S.Task('c_t2_s00_mem0', length=1, delay_cost=1)
	c_t2_s00_mem0 += MAS_MEM[0]
	S += 40 < c_t2_s00_mem0
	S += c_t2_s00_mem0 <= c_t2_s00

	c_t2_s00_mem1 = S.Task('c_t2_s00_mem1', length=1, delay_cost=1)
	c_t2_s00_mem1 += MAS_MEM[7]
	S += 45 < c_t2_s00_mem1
	S += c_t2_s00_mem1 <= c_t2_s00

	c_t2_s01 = S.Task('c_t2_s01', length=3, delay_cost=1)
	c_t2_s01 += alt(MAS)
	c_t2_s01_in = S.Task('c_t2_s01_in', length=1, delay_cost=1)
	c_t2_s01_in += alt(MAS_in)
	S += c_t2_s01_in*MAS_in[0]<=c_t2_s01*MAS[0]

	S += c_t2_s01_in*MAS_in[1]<=c_t2_s01*MAS[1]

	S += c_t2_s01_in*MAS_in[2]<=c_t2_s01*MAS[2]

	S += c_t2_s01_in*MAS_in[3]<=c_t2_s01*MAS[3]

	c_t2_s01_mem0 = S.Task('c_t2_s01_mem0', length=1, delay_cost=1)
	c_t2_s01_mem0 += MAS_MEM[6]
	S += 45 < c_t2_s01_mem0
	S += c_t2_s01_mem0 <= c_t2_s01

	c_t2_s01_mem1 = S.Task('c_t2_s01_mem1', length=1, delay_cost=1)
	c_t2_s01_mem1 += MAS_MEM[1]
	S += 40 < c_t2_s01_mem1
	S += c_t2_s01_mem1 <= c_t2_s01

	c_t2_t51 = S.Task('c_t2_t51', length=3, delay_cost=1)
	c_t2_t51 += alt(MAS)
	c_t2_t51_in = S.Task('c_t2_t51_in', length=1, delay_cost=1)
	c_t2_t51_in += alt(MAS_in)
	S += c_t2_t51_in*MAS_in[0]<=c_t2_t51*MAS[0]

	S += c_t2_t51_in*MAS_in[1]<=c_t2_t51*MAS[1]

	S += c_t2_t51_in*MAS_in[2]<=c_t2_t51*MAS[2]

	S += c_t2_t51_in*MAS_in[3]<=c_t2_t51*MAS[3]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	c_t2_t51_mem0 += MAS_MEM[6]
	S += 41 < c_t2_t51_mem0
	S += c_t2_t51_mem0 <= c_t2_t51

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	c_t2_t51_mem1 += MAS_MEM[7]
	S += 45 < c_t2_t51_mem1
	S += c_t2_t51_mem1 <= c_t2_t51

	c_t210 = S.Task('c_t210', length=3, delay_cost=1)
	c_t210 += alt(MAS)
	c_t210_in = S.Task('c_t210_in', length=1, delay_cost=1)
	c_t210_in += alt(MAS_in)
	S += c_t210_in*MAS_in[0]<=c_t210*MAS[0]

	S += c_t210_in*MAS_in[1]<=c_t210*MAS[1]

	S += c_t210_in*MAS_in[2]<=c_t210*MAS[2]

	S += c_t210_in*MAS_in[3]<=c_t210*MAS[3]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	c_t210_mem0 += MAS_MEM[0]
	S += 74 < c_t210_mem0
	S += c_t210_mem0 <= c_t210

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	c_t210_mem1 += MAS_MEM[7]
	S += 43 < c_t210_mem1
	S += c_t210_mem1 <= c_t210

	c_t3_t01 = S.Task('c_t3_t01', length=3, delay_cost=1)
	c_t3_t01 += alt(MAS)
	c_t3_t01_in = S.Task('c_t3_t01_in', length=1, delay_cost=1)
	c_t3_t01_in += alt(MAS_in)
	S += c_t3_t01_in*MAS_in[0]<=c_t3_t01*MAS[0]

	S += c_t3_t01_in*MAS_in[1]<=c_t3_t01*MAS[1]

	S += c_t3_t01_in*MAS_in[2]<=c_t3_t01*MAS[2]

	S += c_t3_t01_in*MAS_in[3]<=c_t3_t01*MAS[3]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	c_t3_t01_mem0 += MM_MEM[0]
	S += 61 < c_t3_t01_mem0
	S += c_t3_t01_mem0 <= c_t3_t01

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	c_t3_t01_mem1 += MAS_MEM[3]
	S += 58 < c_t3_t01_mem1
	S += c_t3_t01_mem1 <= c_t3_t01

	c_t3_t11 = S.Task('c_t3_t11', length=3, delay_cost=1)
	c_t3_t11 += alt(MAS)
	c_t3_t11_in = S.Task('c_t3_t11_in', length=1, delay_cost=1)
	c_t3_t11_in += alt(MAS_in)
	S += c_t3_t11_in*MAS_in[0]<=c_t3_t11*MAS[0]

	S += c_t3_t11_in*MAS_in[1]<=c_t3_t11*MAS[1]

	S += c_t3_t11_in*MAS_in[2]<=c_t3_t11*MAS[2]

	S += c_t3_t11_in*MAS_in[3]<=c_t3_t11*MAS[3]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	c_t3_t11_mem0 += MM_MEM[0]
	S += 59 < c_t3_t11_mem0
	S += c_t3_t11_mem0 <= c_t3_t11

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	c_t3_t11_mem1 += MAS_MEM[3]
	S += 60 < c_t3_t11_mem1
	S += c_t3_t11_mem1 <= c_t3_t11

	c_t3_t4_t4 = S.Task('c_t3_t4_t4', length=8, delay_cost=1)
	c_t3_t4_t4 += alt(MM)
	c_t3_t4_t4_in = S.Task('c_t3_t4_t4_in', length=1, delay_cost=1)
	c_t3_t4_t4_in += alt(MM_in)
	S += c_t3_t4_t4_in*MM_in[0]<=c_t3_t4_t4*MM[0]
	S += c_t3_t4_t4_in*MM_in[1]<=c_t3_t4_t4*MM[1]
	c_t3_t4_t4_mem0 = S.Task('c_t3_t4_t4_mem0', length=1, delay_cost=1)
	c_t3_t4_t4_mem0 += MAS_MEM[4]
	S += 49 < c_t3_t4_t4_mem0
	S += c_t3_t4_t4_mem0 <= c_t3_t4_t4

	c_t3_t4_t4_mem1 = S.Task('c_t3_t4_t4_mem1', length=1, delay_cost=1)
	c_t3_t4_t4_mem1 += MAS_MEM[7]
	S += 59 < c_t3_t4_t4_mem1
	S += c_t3_t4_t4_mem1 <= c_t3_t4_t4

	c_t3_t40 = S.Task('c_t3_t40', length=3, delay_cost=1)
	c_t3_t40 += alt(MAS)
	c_t3_t40_in = S.Task('c_t3_t40_in', length=1, delay_cost=1)
	c_t3_t40_in += alt(MAS_in)
	S += c_t3_t40_in*MAS_in[0]<=c_t3_t40*MAS[0]

	S += c_t3_t40_in*MAS_in[1]<=c_t3_t40*MAS[1]

	S += c_t3_t40_in*MAS_in[2]<=c_t3_t40*MAS[2]

	S += c_t3_t40_in*MAS_in[3]<=c_t3_t40*MAS[3]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	c_t3_t40_mem0 += MM_MEM[2]
	S += 63 < c_t3_t40_mem0
	S += c_t3_t40_mem0 <= c_t3_t40

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	c_t3_t40_mem1 += MM_MEM[3]
	S += 58 < c_t3_t40_mem1
	S += c_t3_t40_mem1 <= c_t3_t40

	c_t3_t4_t5 = S.Task('c_t3_t4_t5', length=3, delay_cost=1)
	c_t3_t4_t5 += alt(MAS)
	c_t3_t4_t5_in = S.Task('c_t3_t4_t5_in', length=1, delay_cost=1)
	c_t3_t4_t5_in += alt(MAS_in)
	S += c_t3_t4_t5_in*MAS_in[0]<=c_t3_t4_t5*MAS[0]

	S += c_t3_t4_t5_in*MAS_in[1]<=c_t3_t4_t5*MAS[1]

	S += c_t3_t4_t5_in*MAS_in[2]<=c_t3_t4_t5*MAS[2]

	S += c_t3_t4_t5_in*MAS_in[3]<=c_t3_t4_t5*MAS[3]

	c_t3_t4_t5_mem0 = S.Task('c_t3_t4_t5_mem0', length=1, delay_cost=1)
	c_t3_t4_t5_mem0 += MM_MEM[2]
	S += 63 < c_t3_t4_t5_mem0
	S += c_t3_t4_t5_mem0 <= c_t3_t4_t5

	c_t3_t4_t5_mem1 = S.Task('c_t3_t4_t5_mem1', length=1, delay_cost=1)
	c_t3_t4_t5_mem1 += MM_MEM[3]
	S += 58 < c_t3_t4_t5_mem1
	S += c_t3_t4_t5_mem1 <= c_t3_t4_t5

	c_t3_t50 = S.Task('c_t3_t50', length=3, delay_cost=1)
	c_t3_t50 += alt(MAS)
	c_t3_t50_in = S.Task('c_t3_t50_in', length=1, delay_cost=1)
	c_t3_t50_in += alt(MAS_in)
	S += c_t3_t50_in*MAS_in[0]<=c_t3_t50*MAS[0]

	S += c_t3_t50_in*MAS_in[1]<=c_t3_t50*MAS[1]

	S += c_t3_t50_in*MAS_in[2]<=c_t3_t50*MAS[2]

	S += c_t3_t50_in*MAS_in[3]<=c_t3_t50*MAS[3]

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	c_t3_t50_mem0 += MAS_MEM[2]
	S += 57 < c_t3_t50_mem0
	S += c_t3_t50_mem0 <= c_t3_t50

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	c_t3_t50_mem1 += MAS_MEM[1]
	S += 61 < c_t3_t50_mem1
	S += c_t3_t50_mem1 <= c_t3_t50

	c_t4_t01 = S.Task('c_t4_t01', length=3, delay_cost=1)
	c_t4_t01 += alt(MAS)
	c_t4_t01_in = S.Task('c_t4_t01_in', length=1, delay_cost=1)
	c_t4_t01_in += alt(MAS_in)
	S += c_t4_t01_in*MAS_in[0]<=c_t4_t01*MAS[0]

	S += c_t4_t01_in*MAS_in[1]<=c_t4_t01*MAS[1]

	S += c_t4_t01_in*MAS_in[2]<=c_t4_t01*MAS[2]

	S += c_t4_t01_in*MAS_in[3]<=c_t4_t01*MAS[3]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	c_t4_t01_mem0 += MM_MEM[0]
	S += 71 < c_t4_t01_mem0
	S += c_t4_t01_mem0 <= c_t4_t01

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	c_t4_t01_mem1 += MAS_MEM[5]
	S += 72 < c_t4_t01_mem1
	S += c_t4_t01_mem1 <= c_t4_t01

	c_t4_t11 = S.Task('c_t4_t11', length=3, delay_cost=1)
	c_t4_t11 += alt(MAS)
	c_t4_t11_in = S.Task('c_t4_t11_in', length=1, delay_cost=1)
	c_t4_t11_in += alt(MAS_in)
	S += c_t4_t11_in*MAS_in[0]<=c_t4_t11*MAS[0]

	S += c_t4_t11_in*MAS_in[1]<=c_t4_t11*MAS[1]

	S += c_t4_t11_in*MAS_in[2]<=c_t4_t11*MAS[2]

	S += c_t4_t11_in*MAS_in[3]<=c_t4_t11*MAS[3]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	c_t4_t11_mem0 += MM_MEM[2]
	S += 84 < c_t4_t11_mem0
	S += c_t4_t11_mem0 <= c_t4_t11

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	c_t4_t11_mem1 += MAS_MEM[3]
	S += 69 < c_t4_t11_mem1
	S += c_t4_t11_mem1 <= c_t4_t11

	c_t4_t4_t4 = S.Task('c_t4_t4_t4', length=8, delay_cost=1)
	c_t4_t4_t4 += alt(MM)
	c_t4_t4_t4_in = S.Task('c_t4_t4_t4_in', length=1, delay_cost=1)
	c_t4_t4_t4_in += alt(MM_in)
	S += c_t4_t4_t4_in*MM_in[0]<=c_t4_t4_t4*MM[0]
	S += c_t4_t4_t4_in*MM_in[1]<=c_t4_t4_t4*MM[1]
	c_t4_t4_t4_mem0 = S.Task('c_t4_t4_t4_mem0', length=1, delay_cost=1)
	c_t4_t4_t4_mem0 += MAS_MEM[4]
	S += 81 < c_t4_t4_t4_mem0
	S += c_t4_t4_t4_mem0 <= c_t4_t4_t4

	c_t4_t4_t4_mem1 = S.Task('c_t4_t4_t4_mem1', length=1, delay_cost=1)
	c_t4_t4_t4_mem1 += MAS_MEM[5]
	S += 78 < c_t4_t4_t4_mem1
	S += c_t4_t4_t4_mem1 <= c_t4_t4_t4

	c_t4_t40 = S.Task('c_t4_t40', length=3, delay_cost=1)
	c_t4_t40 += alt(MAS)
	c_t4_t40_in = S.Task('c_t4_t40_in', length=1, delay_cost=1)
	c_t4_t40_in += alt(MAS_in)
	S += c_t4_t40_in*MAS_in[0]<=c_t4_t40*MAS[0]

	S += c_t4_t40_in*MAS_in[1]<=c_t4_t40*MAS[1]

	S += c_t4_t40_in*MAS_in[2]<=c_t4_t40*MAS[2]

	S += c_t4_t40_in*MAS_in[3]<=c_t4_t40*MAS[3]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	c_t4_t40_mem0 += MM_MEM[2]
	S += 85 < c_t4_t40_mem0
	S += c_t4_t40_mem0 <= c_t4_t40

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	c_t4_t40_mem1 += MM_MEM[1]
	S += 86 < c_t4_t40_mem1
	S += c_t4_t40_mem1 <= c_t4_t40

	c_t4_t4_t5 = S.Task('c_t4_t4_t5', length=3, delay_cost=1)
	c_t4_t4_t5 += alt(MAS)
	c_t4_t4_t5_in = S.Task('c_t4_t4_t5_in', length=1, delay_cost=1)
	c_t4_t4_t5_in += alt(MAS_in)
	S += c_t4_t4_t5_in*MAS_in[0]<=c_t4_t4_t5*MAS[0]

	S += c_t4_t4_t5_in*MAS_in[1]<=c_t4_t4_t5*MAS[1]

	S += c_t4_t4_t5_in*MAS_in[2]<=c_t4_t4_t5*MAS[2]

	S += c_t4_t4_t5_in*MAS_in[3]<=c_t4_t4_t5*MAS[3]

	c_t4_t4_t5_mem0 = S.Task('c_t4_t4_t5_mem0', length=1, delay_cost=1)
	c_t4_t4_t5_mem0 += MM_MEM[2]
	S += 85 < c_t4_t4_t5_mem0
	S += c_t4_t4_t5_mem0 <= c_t4_t4_t5

	c_t4_t4_t5_mem1 = S.Task('c_t4_t4_t5_mem1', length=1, delay_cost=1)
	c_t4_t4_t5_mem1 += MM_MEM[1]
	S += 86 < c_t4_t4_t5_mem1
	S += c_t4_t4_t5_mem1 <= c_t4_t4_t5

	c_t4_t50 = S.Task('c_t4_t50', length=3, delay_cost=1)
	c_t4_t50 += alt(MAS)
	c_t4_t50_in = S.Task('c_t4_t50_in', length=1, delay_cost=1)
	c_t4_t50_in += alt(MAS_in)
	S += c_t4_t50_in*MAS_in[0]<=c_t4_t50*MAS[0]

	S += c_t4_t50_in*MAS_in[1]<=c_t4_t50*MAS[1]

	S += c_t4_t50_in*MAS_in[2]<=c_t4_t50*MAS[2]

	S += c_t4_t50_in*MAS_in[3]<=c_t4_t50*MAS[3]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	c_t4_t50_mem0 += MAS_MEM[0]
	S += 73 < c_t4_t50_mem0
	S += c_t4_t50_mem0 <= c_t4_t50

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	c_t4_t50_mem1 += MAS_MEM[1]
	S += 70 < c_t4_t50_mem1
	S += c_t4_t50_mem1 <= c_t4_t50

	c_t5_t01 = S.Task('c_t5_t01', length=3, delay_cost=1)
	c_t5_t01 += alt(MAS)
	c_t5_t01_in = S.Task('c_t5_t01_in', length=1, delay_cost=1)
	c_t5_t01_in += alt(MAS_in)
	S += c_t5_t01_in*MAS_in[0]<=c_t5_t01*MAS[0]

	S += c_t5_t01_in*MAS_in[1]<=c_t5_t01*MAS[1]

	S += c_t5_t01_in*MAS_in[2]<=c_t5_t01*MAS[2]

	S += c_t5_t01_in*MAS_in[3]<=c_t5_t01*MAS[3]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	c_t5_t01_mem0 += MM_MEM[0]
	S += 79 < c_t5_t01_mem0
	S += c_t5_t01_mem0 <= c_t5_t01

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	c_t5_t01_mem1 += MAS_MEM[7]
	S += 82 < c_t5_t01_mem1
	S += c_t5_t01_mem1 <= c_t5_t01

	c_t5_t11 = S.Task('c_t5_t11', length=3, delay_cost=1)
	c_t5_t11 += alt(MAS)
	c_t5_t11_in = S.Task('c_t5_t11_in', length=1, delay_cost=1)
	c_t5_t11_in += alt(MAS_in)
	S += c_t5_t11_in*MAS_in[0]<=c_t5_t11*MAS[0]

	S += c_t5_t11_in*MAS_in[1]<=c_t5_t11*MAS[1]

	S += c_t5_t11_in*MAS_in[2]<=c_t5_t11*MAS[2]

	S += c_t5_t11_in*MAS_in[3]<=c_t5_t11*MAS[3]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	c_t5_t11_mem0 += MM_MEM[0]
	S += 83 < c_t5_t11_mem0
	S += c_t5_t11_mem0 <= c_t5_t11

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	c_t5_t11_mem1 += MAS_MEM[1]
	S += 84 < c_t5_t11_mem1
	S += c_t5_t11_mem1 <= c_t5_t11

	c_t5_t4_t4 = S.Task('c_t5_t4_t4', length=8, delay_cost=1)
	c_t5_t4_t4 += alt(MM)
	c_t5_t4_t4_in = S.Task('c_t5_t4_t4_in', length=1, delay_cost=1)
	c_t5_t4_t4_in += alt(MM_in)
	S += c_t5_t4_t4_in*MM_in[0]<=c_t5_t4_t4*MM[0]
	S += c_t5_t4_t4_in*MM_in[1]<=c_t5_t4_t4*MM[1]
	c_t5_t4_t4_mem0 = S.Task('c_t5_t4_t4_mem0', length=1, delay_cost=1)
	c_t5_t4_t4_mem0 += MAS_MEM[4]
	S += 62 < c_t5_t4_t4_mem0
	S += c_t5_t4_t4_mem0 <= c_t5_t4_t4

	c_t5_t4_t4_mem1 = S.Task('c_t5_t4_t4_mem1', length=1, delay_cost=1)
	c_t5_t4_t4_mem1 += MAS_MEM[5]
	S += 80 < c_t5_t4_t4_mem1
	S += c_t5_t4_t4_mem1 <= c_t5_t4_t4

	c_t5_t40 = S.Task('c_t5_t40', length=3, delay_cost=1)
	c_t5_t40 += alt(MAS)
	c_t5_t40_in = S.Task('c_t5_t40_in', length=1, delay_cost=1)
	c_t5_t40_in += alt(MAS_in)
	S += c_t5_t40_in*MAS_in[0]<=c_t5_t40*MAS[0]

	S += c_t5_t40_in*MAS_in[1]<=c_t5_t40*MAS[1]

	S += c_t5_t40_in*MAS_in[2]<=c_t5_t40*MAS[2]

	S += c_t5_t40_in*MAS_in[3]<=c_t5_t40*MAS[3]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	c_t5_t40_mem0 += MM_MEM[0]
	S += 84 < c_t5_t40_mem0
	S += c_t5_t40_mem0 <= c_t5_t40

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	c_t5_t40_mem1 += MM_MEM[3]
	S += 78 < c_t5_t40_mem1
	S += c_t5_t40_mem1 <= c_t5_t40

	c_t5_t4_t5 = S.Task('c_t5_t4_t5', length=3, delay_cost=1)
	c_t5_t4_t5 += alt(MAS)
	c_t5_t4_t5_in = S.Task('c_t5_t4_t5_in', length=1, delay_cost=1)
	c_t5_t4_t5_in += alt(MAS_in)
	S += c_t5_t4_t5_in*MAS_in[0]<=c_t5_t4_t5*MAS[0]

	S += c_t5_t4_t5_in*MAS_in[1]<=c_t5_t4_t5*MAS[1]

	S += c_t5_t4_t5_in*MAS_in[2]<=c_t5_t4_t5*MAS[2]

	S += c_t5_t4_t5_in*MAS_in[3]<=c_t5_t4_t5*MAS[3]

	c_t5_t4_t5_mem0 = S.Task('c_t5_t4_t5_mem0', length=1, delay_cost=1)
	c_t5_t4_t5_mem0 += MM_MEM[0]
	S += 84 < c_t5_t4_t5_mem0
	S += c_t5_t4_t5_mem0 <= c_t5_t4_t5

	c_t5_t4_t5_mem1 = S.Task('c_t5_t4_t5_mem1', length=1, delay_cost=1)
	c_t5_t4_t5_mem1 += MM_MEM[3]
	S += 78 < c_t5_t4_t5_mem1
	S += c_t5_t4_t5_mem1 <= c_t5_t4_t5

	c_t5_t50 = S.Task('c_t5_t50', length=3, delay_cost=1)
	c_t5_t50 += alt(MAS)
	c_t5_t50_in = S.Task('c_t5_t50_in', length=1, delay_cost=1)
	c_t5_t50_in += alt(MAS_in)
	S += c_t5_t50_in*MAS_in[0]<=c_t5_t50*MAS[0]

	S += c_t5_t50_in*MAS_in[1]<=c_t5_t50*MAS[1]

	S += c_t5_t50_in*MAS_in[2]<=c_t5_t50*MAS[2]

	S += c_t5_t50_in*MAS_in[3]<=c_t5_t50*MAS[3]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	c_t5_t50_mem0 += MAS_MEM[0]
	S += 81 < c_t5_t50_mem0
	S += c_t5_t50_mem0 <= c_t5_t50

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	c_t5_t50_mem1 += MAS_MEM[1]
	S += 83 < c_t5_t50_mem1
	S += c_t5_t50_mem1 <= c_t5_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM2_stage3MAS4/MUL/schedule5.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

