from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 189
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=2, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 0
	c_t1_t31_in += MAS_in[0]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 0
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 0
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 1
	c_t0_t1_t2_in += MAS_in[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 1
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 1
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=2, delay_cost=1)
	S += c_t1_t31 >= 1
	c_t1_t31 += MAS[0]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 2
	c_t0_t0_t2_in += MAS_in[1]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 2
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 2
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=2, delay_cost=1)
	S += c_t0_t1_t2 >= 2
	c_t0_t1_t2 += MAS[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=2, delay_cost=1)
	S += c_t0_t0_t2 >= 3
	c_t0_t0_t2 += MAS[1]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 3
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 3
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 3
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=2, delay_cost=1)
	S += c_t1_t0_t2 >= 4
	c_t1_t0_t2 += MAS[0]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 4
	c_t1_t1_t3_in += MAS_in[1]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 4
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 4
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 5
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 5
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 5
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=2, delay_cost=1)
	S += c_t1_t1_t3 >= 5
	c_t1_t1_t3 += MAS[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=8, delay_cost=1)
	S += c_t1_t0_t1 >= 6
	c_t1_t0_t1 += MM[0]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 6
	c_t1_t21_in += MAS_in[0]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 6
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 6
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 7
	c_t0_t20_in += MAS_in[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 7
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 7
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t21 = S.Task('c_t1_t21', length=2, delay_cost=1)
	S += c_t1_t21 >= 7
	c_t1_t21 += MAS[0]

	c_t0_t20 = S.Task('c_t0_t20', length=2, delay_cost=1)
	S += c_t0_t20 >= 8
	c_t0_t20 += MAS[1]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 8
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 8
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 8
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 9
	c_t0_t21_in += MAS_in[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 9
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 9
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 9
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 9
	c_t1_t4_t1_mem0 += MAS_MEM[0]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 9
	c_t1_t4_t1_mem1 += MAS_MEM[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=8, delay_cost=1)
	S += c_t2_t0_t0 >= 9
	c_t2_t0_t0 += MM[0]

	c_t0_t21 = S.Task('c_t0_t21', length=2, delay_cost=1)
	S += c_t0_t21 >= 10
	c_t0_t21 += MAS[1]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 10
	c_t0_t30_in += MAS_in[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 10
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 10
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=8, delay_cost=1)
	S += c_t1_t4_t1 >= 10
	c_t1_t4_t1 += MM[0]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 11
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 11
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 11
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t30 = S.Task('c_t0_t30', length=2, delay_cost=1)
	S += c_t0_t30 >= 11
	c_t0_t30 += MAS[0]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 11
	c_t0_t4_t2_in += MAS_in[1]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 11
	c_t0_t4_t2_mem0 += MAS_MEM[2]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 11
	c_t0_t4_t2_mem1 += MAS_MEM[3]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=2, delay_cost=1)
	S += c_t0_t1_t3 >= 12
	c_t0_t1_t3 += MAS[0]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 12
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 12
	c_t0_t4_t0_mem0 += MAS_MEM[2]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 12
	c_t0_t4_t0_mem1 += MAS_MEM[1]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=2, delay_cost=1)
	S += c_t0_t4_t2 >= 12
	c_t0_t4_t2 += MAS[1]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 12
	c_t1_t0_t3_in += MAS_in[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 12
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 12
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=8, delay_cost=1)
	S += c_t0_t4_t0 >= 13
	c_t0_t4_t0 += MM[0]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=2, delay_cost=1)
	S += c_t1_t0_t3 >= 13
	c_t1_t0_t3 += MAS[1]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 13
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 13
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 13
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 14
	c_t0_t1_t4_in += MM_in[0]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 14
	c_t0_t1_t4_mem0 += MAS_MEM[0]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 14
	c_t0_t1_t4_mem1 += MAS_MEM[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 14
	c_t0_t31_in += MAS_in[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 14
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 14
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=8, delay_cost=1)
	S += c_t1_t1_t1 >= 14
	c_t1_t1_t1 += MM[0]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=8, delay_cost=1)
	S += c_t0_t1_t4 >= 15
	c_t0_t1_t4 += MM[0]

	c_t0_t31 = S.Task('c_t0_t31', length=2, delay_cost=1)
	S += c_t0_t31 >= 15
	c_t0_t31 += MAS[0]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 15
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 15
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 15
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 16
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 16
	c_t0_t4_t1_mem0 += MAS_MEM[2]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 16
	c_t0_t4_t1_mem1 += MAS_MEM[1]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 16
	c_t1_t1_t2_in += MAS_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 16
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 16
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=8, delay_cost=1)
	S += c_t2_t0_t1 >= 16
	c_t2_t0_t1 += MM[0]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=8, delay_cost=1)
	S += c_t0_t4_t1 >= 17
	c_t0_t4_t1 += MM[0]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 17
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 17
	c_t1_t0_t4_mem0 += MAS_MEM[0]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 17
	c_t1_t0_t4_mem1 += MAS_MEM[3]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=2, delay_cost=1)
	S += c_t1_t1_t2 >= 17
	c_t1_t1_t2 += MAS[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 17
	c_t2_t0_t3_in += MAS_in[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 17
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 17
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 18
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 18
	c_t0_t4_t3_mem0 += MAS_MEM[0]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 18
	c_t0_t4_t3_mem1 += MAS_MEM[1]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=8, delay_cost=1)
	S += c_t1_t0_t4 >= 18
	c_t1_t0_t4 += MM[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 18
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 18
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 18
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=2, delay_cost=1)
	S += c_t2_t0_t3 >= 18
	c_t2_t0_t3 += MAS[0]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=2, delay_cost=1)
	S += c_t0_t4_t3 >= 19
	c_t0_t4_t3 += MAS[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=8, delay_cost=1)
	S += c_t1_t1_t0 >= 19
	c_t1_t1_t0 += MM[0]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 19
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 19
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 19
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=8, delay_cost=1)
	S += c_t2_t1_t0 >= 20
	c_t2_t1_t0 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 20
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 20
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 20
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 21
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 21
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 21
	c_t1_t1_t4_mem1 += MAS_MEM[3]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 21
	c_t1_t20_in += MAS_in[0]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 21
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 21
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=8, delay_cost=1)
	S += c_t2_t1_t1 >= 21
	c_t2_t1_t1 += MM[0]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 22
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 22
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 22
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=8, delay_cost=1)
	S += c_t1_t1_t4 >= 22
	c_t1_t1_t4 += MM[0]

	c_t1_t20 = S.Task('c_t1_t20', length=2, delay_cost=1)
	S += c_t1_t20 >= 22
	c_t1_t20 += MAS[0]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 23
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 23
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 23
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=8, delay_cost=1)
	S += c_t1_t0_t0 >= 23
	c_t1_t0_t0 += MM[0]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 23
	c_t1_t4_t2_in += MAS_in[0]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 23
	c_t1_t4_t2_mem0 += MAS_MEM[0]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 23
	c_t1_t4_t2_mem1 += MAS_MEM[1]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 23
	c_t2_t00_in += MAS_in[1]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 23
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 23
	c_t2_t00_mem1 += MM_MEM[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=8, delay_cost=1)
	S += c_t0_t1_t1 >= 24
	c_t0_t1_t1 += MM[0]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 24
	c_t1_t30_in += MAS_in[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 24
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 24
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=2, delay_cost=1)
	S += c_t1_t4_t2 >= 24
	c_t1_t4_t2 += MAS[0]

	c_t2_t00 = S.Task('c_t2_t00', length=2, delay_cost=1)
	S += c_t2_t00 >= 24
	c_t2_t00 += MAS[1]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 24
	c_t2_t0_t5_in += MAS_in[1]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 24
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 24
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 25
	c_t0_t0_t3_in += MAS_in[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 25
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 25
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=2, delay_cost=1)
	S += c_t1_t30 >= 25
	c_t1_t30 += MAS[0]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=2, delay_cost=1)
	S += c_t2_t0_t5 >= 25
	c_t2_t0_t5 += MAS[1]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=2, delay_cost=1)
	S += c_t0_t0_t3 >= 26
	c_t0_t0_t3 += MAS[0]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 26
	c_t1_t1_t5_in += MAS_in[0]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 26
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 26
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 26
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 26
	c_t1_t4_t0_mem0 += MAS_MEM[0]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 26
	c_t1_t4_t0_mem1 += MAS_MEM[1]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 26
	c_t2_t0_t2_in += MAS_in[1]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 26
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 26
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 27
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 27
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 27
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 27
	c_t1_t10_in += MAS_in[0]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 27
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 27
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=2, delay_cost=1)
	S += c_t1_t1_t5 >= 27
	c_t1_t1_t5 += MAS[0]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=8, delay_cost=1)
	S += c_t1_t4_t0 >= 27
	c_t1_t4_t0 += MM[0]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 27
	c_t1_t4_t3_in += MAS_in[1]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 27
	c_t1_t4_t3_mem0 += MAS_MEM[0]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 27
	c_t1_t4_t3_mem1 += MAS_MEM[1]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=2, delay_cost=1)
	S += c_t2_t0_t2 >= 27
	c_t2_t0_t2 += MAS[1]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 28
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 28
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 28
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=8, delay_cost=1)
	S += c_t0_t1_t0 >= 28
	c_t0_t1_t0 += MM[0]

	c_t1_t10 = S.Task('c_t1_t10', length=2, delay_cost=1)
	S += c_t1_t10 >= 28
	c_t1_t10 += MAS[0]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=2, delay_cost=1)
	S += c_t1_t4_t3 >= 28
	c_t1_t4_t3 += MAS[1]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 28
	c_t2_t1_t5_in += MAS_in[0]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 28
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 28
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 29
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 29
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 29
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=8, delay_cost=1)
	S += c_t0_t0_t1 >= 29
	c_t0_t0_t1 += MM[0]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 29
	c_t2_t10_in += MAS_in[1]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 29
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 29
	c_t2_t10_mem1 += MM_MEM[1]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=2, delay_cost=1)
	S += c_t2_t1_t5 >= 29
	c_t2_t1_t5 += MAS[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=8, delay_cost=1)
	S += c_t0_t0_t0 >= 30
	c_t0_t0_t0 += MM[0]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 30
	c_t1_t00_in += MAS_in[0]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 30
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 30
	c_t1_t00_mem1 += MM_MEM[1]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 30
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 30
	c_t2_t0_t4_mem0 += MAS_MEM[2]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 30
	c_t2_t0_t4_mem1 += MAS_MEM[1]

	c_t2_t10 = S.Task('c_t2_t10', length=2, delay_cost=1)
	S += c_t2_t10 >= 30
	c_t2_t10 += MAS[1]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 30
	c_t5110_in += MAS_in[1]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 30
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 30
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 31
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 31
	c_t0_t0_t4_mem0 += MAS_MEM[2]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 31
	c_t0_t0_t4_mem1 += MAS_MEM[1]

	c_t1_t00 = S.Task('c_t1_t00', length=2, delay_cost=1)
	S += c_t1_t00 >= 31
	c_t1_t00 += MAS[0]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 31
	c_t1_t0_t5_in += MAS_in[0]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 31
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 31
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=8, delay_cost=1)
	S += c_t2_t0_t4 >= 31
	c_t2_t0_t4 += MM[0]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 31
	c_t3100_in += MAS_in[1]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 31
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 31
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t5110 = S.Task('c_t5110', length=2, delay_cost=1)
	S += c_t5110 >= 31
	c_t5110 += MAS[1]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=8, delay_cost=1)
	S += c_t0_t0_t4 >= 32
	c_t0_t0_t4 += MM[0]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=2, delay_cost=1)
	S += c_t1_t0_t5 >= 32
	c_t1_t0_t5 += MAS[0]

	c_t3100 = S.Task('c_t3100', length=2, delay_cost=1)
	S += c_t3100 >= 32
	c_t3100 += MAS[1]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 32
	c_t5101_in += MAS_in[0]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 32
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 32
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5101 = S.Task('c_t5101', length=2, delay_cost=1)
	S += c_t5101 >= 33
	c_t5101 += MAS[0]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 33
	c_t5111_in += MAS_in[0]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 33
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 33
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 34
	c_t5000_in += MAS_in[0]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 34
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 34
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5111 = S.Task('c_t5111', length=2, delay_cost=1)
	S += c_t5111 >= 34
	c_t5111 += MAS[0]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 35
	c_t0_t10_in += MAS_in[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 35
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 35
	c_t0_t10_mem1 += MM_MEM[1]

	c_t5000 = S.Task('c_t5000', length=2, delay_cost=1)
	S += c_t5000 >= 35
	c_t5000 += MAS[0]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 35
	c_t5100_in += MAS_in[0]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 35
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 35
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t0_t10 = S.Task('c_t0_t10', length=2, delay_cost=1)
	S += c_t0_t10 >= 36
	c_t0_t10 += MAS[1]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 36
	c_t0_t1_t5_in += MAS_in[1]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 36
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 36
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 36
	c_t4010_in += MAS_in[0]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 36
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 36
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t5100 = S.Task('c_t5100', length=2, delay_cost=1)
	S += c_t5100 >= 36
	c_t5100 += MAS[0]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 37
	c_t0_t0_t5_in += MAS_in[1]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 37
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 37
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=2, delay_cost=1)
	S += c_t0_t1_t5 >= 37
	c_t0_t1_t5 += MAS[1]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 37
	c_t4001_in += MAS_in[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 37
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 37
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4010 = S.Task('c_t4010', length=2, delay_cost=1)
	S += c_t4010 >= 37
	c_t4010 += MAS[0]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 37
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 37
	c_t5_t0_t0_mem0 += MAS_MEM[0]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 37
	c_t5_t0_t0_mem1 += MAS_MEM[1]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 38
	c_t0_t00_in += MAS_in[0]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 38
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 38
	c_t0_t00_mem1 += MM_MEM[1]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=2, delay_cost=1)
	S += c_t0_t0_t5 >= 38
	c_t0_t0_t5 += MAS[1]

	c_t4001 = S.Task('c_t4001', length=2, delay_cost=1)
	S += c_t4001 >= 38
	c_t4001 += MAS[0]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 38
	c_t4101_in += MAS_in[1]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 38
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 38
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=8, delay_cost=1)
	S += c_t5_t0_t0 >= 38
	c_t5_t0_t0 += MM[0]

	c_t0_t00 = S.Task('c_t0_t00', length=2, delay_cost=1)
	S += c_t0_t00 >= 39
	c_t0_t00 += MAS[0]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 39
	c_t3001_in += MAS_in[1]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 39
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 39
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t4101 = S.Task('c_t4101', length=2, delay_cost=1)
	S += c_t4101 >= 39
	c_t4101 += MAS[1]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 39
	c_t5_t30_in += MAS_in[0]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 39
	c_t5_t30_mem0 += MAS_MEM[0]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 39
	c_t5_t30_mem1 += MAS_MEM[3]

	c_t3001 = S.Task('c_t3001', length=2, delay_cost=1)
	S += c_t3001 >= 40
	c_t3001 += MAS[1]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 40
	c_t4011_in += MAS_in[1]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 40
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 40
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 40
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 40
	c_t4_t0_t1_mem0 += MAS_MEM[0]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 40
	c_t4_t0_t1_mem1 += MAS_MEM[3]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 40
	c_t5_t1_t3_in += MAS_in[0]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 40
	c_t5_t1_t3_mem0 += MAS_MEM[2]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 40
	c_t5_t1_t3_mem1 += MAS_MEM[1]

	c_t5_t30 = S.Task('c_t5_t30', length=2, delay_cost=1)
	S += c_t5_t30 >= 40
	c_t5_t30 += MAS[0]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 41
	c_t2_t30_in += MAS_in[1]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 41
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 41
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t4011 = S.Task('c_t4011', length=2, delay_cost=1)
	S += c_t4011 >= 41
	c_t4011 += MAS[1]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=8, delay_cost=1)
	S += c_t4_t0_t1 >= 41
	c_t4_t0_t1 += MM[0]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=2, delay_cost=1)
	S += c_t5_t1_t3 >= 41
	c_t5_t1_t3 += MAS[0]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 41
	c_t5_t31_in += MAS_in[0]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 41
	c_t5_t31_mem0 += MAS_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 41
	c_t5_t31_mem1 += MAS_MEM[1]

	c_t2_t30 = S.Task('c_t2_t30', length=2, delay_cost=1)
	S += c_t2_t30 >= 42
	c_t2_t30 += MAS[1]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 42
	c_t4000_in += MAS_in[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 42
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 42
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 42
	c_t4_t1_t2_in += MAS_in[0]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 42
	c_t4_t1_t2_mem0 += MAS_MEM[0]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 42
	c_t4_t1_t2_mem1 += MAS_MEM[3]

	c_t5_t31 = S.Task('c_t5_t31', length=2, delay_cost=1)
	S += c_t5_t31 >= 42
	c_t5_t31 += MAS[0]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 43
	c_t3010_in += MAS_in[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 43
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 43
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=2, delay_cost=1)
	S += c_t4000 >= 43
	c_t4000 += MAS[1]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=2, delay_cost=1)
	S += c_t4_t1_t2 >= 43
	c_t4_t1_t2 += MAS[0]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 43
	c_t5_t0_t3_in += MAS_in[1]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 43
	c_t5_t0_t3_mem0 += MAS_MEM[0]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 43
	c_t5_t0_t3_mem1 += MAS_MEM[1]

	c_t3010 = S.Task('c_t3010', length=2, delay_cost=1)
	S += c_t3010 >= 44
	c_t3010 += MAS[0]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 44
	c_t3101_in += MAS_in[0]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 44
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 44
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 44
	c_t4_t0_t2_in += MAS_in[1]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 44
	c_t4_t0_t2_mem0 += MAS_MEM[2]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 44
	c_t4_t0_t2_mem1 += MAS_MEM[1]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=2, delay_cost=1)
	S += c_t5_t0_t3 >= 44
	c_t5_t0_t3 += MAS[1]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 45
	c_t3000_in += MAS_in[0]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 45
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 45
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3101 = S.Task('c_t3101', length=2, delay_cost=1)
	S += c_t3101 >= 45
	c_t3101 += MAS[0]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=2, delay_cost=1)
	S += c_t4_t0_t2 >= 45
	c_t4_t0_t2 += MAS[1]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 45
	c_t4_t21_in += MAS_in[1]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 45
	c_t4_t21_mem0 += MAS_MEM[0]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 45
	c_t4_t21_mem1 += MAS_MEM[3]

	c_t3000 = S.Task('c_t3000', length=2, delay_cost=1)
	S += c_t3000 >= 46
	c_t3000 += MAS[0]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 46
	c_t3_t0_t3_in += MAS_in[1]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 46
	c_t3_t0_t3_mem0 += MAS_MEM[2]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 46
	c_t3_t0_t3_mem1 += MAS_MEM[1]

	c_t4_t21 = S.Task('c_t4_t21', length=2, delay_cost=1)
	S += c_t4_t21 >= 46
	c_t4_t21 += MAS[1]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 46
	c_t5011_in += MAS_in[0]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 46
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 46
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 47
	c_t3111_in += MAS_in[1]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 47
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 47
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 47
	c_t3_t0_t1_in += MM_in[0]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 47
	c_t3_t0_t1_mem0 += MAS_MEM[2]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 47
	c_t3_t0_t1_mem1 += MAS_MEM[1]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 47
	c_t3_t0_t2_in += MAS_in[0]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 47
	c_t3_t0_t2_mem0 += MAS_MEM[0]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 47
	c_t3_t0_t2_mem1 += MAS_MEM[3]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=2, delay_cost=1)
	S += c_t3_t0_t3 >= 47
	c_t3_t0_t3 += MAS[1]

	c_t5011 = S.Task('c_t5011', length=2, delay_cost=1)
	S += c_t5011 >= 47
	c_t5011 += MAS[0]

	c_t3111 = S.Task('c_t3111', length=2, delay_cost=1)
	S += c_t3111 >= 48
	c_t3111 += MAS[1]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 48
	c_t3_t0_t0_in += MM_in[0]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 48
	c_t3_t0_t0_mem0 += MAS_MEM[0]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 48
	c_t3_t0_t0_mem1 += MAS_MEM[3]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=8, delay_cost=1)
	S += c_t3_t0_t1 >= 48
	c_t3_t0_t1 += MM[0]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=2, delay_cost=1)
	S += c_t3_t0_t2 >= 48
	c_t3_t0_t2 += MAS[0]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 48
	c_t4111_in += MAS_in[1]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 48
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 48
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 48
	c_t4_t20_in += MAS_in[0]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 48
	c_t4_t20_mem0 += MAS_MEM[2]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 48
	c_t4_t20_mem1 += MAS_MEM[1]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 49
	c_t2_t21_in += MAS_in[0]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 49
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 49
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=8, delay_cost=1)
	S += c_t3_t0_t0 >= 49
	c_t3_t0_t0 += MM[0]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 49
	c_t3_t31_in += MAS_in[1]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 49
	c_t3_t31_mem0 += MAS_MEM[0]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 49
	c_t3_t31_mem1 += MAS_MEM[3]

	c_t4111 = S.Task('c_t4111', length=2, delay_cost=1)
	S += c_t4111 >= 49
	c_t4111 += MAS[1]

	c_t4_t20 = S.Task('c_t4_t20', length=2, delay_cost=1)
	S += c_t4_t20 >= 49
	c_t4_t20 += MAS[0]

	c_t2_t21 = S.Task('c_t2_t21', length=2, delay_cost=1)
	S += c_t2_t21 >= 50
	c_t2_t21 += MAS[0]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 50
	c_t3_t20_in += MAS_in[1]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 50
	c_t3_t20_mem0 += MAS_MEM[0]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 50
	c_t3_t20_mem1 += MAS_MEM[1]

	c_t3_t31 = S.Task('c_t3_t31', length=2, delay_cost=1)
	S += c_t3_t31 >= 50
	c_t3_t31 += MAS[1]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 50
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 50
	c_t4_t1_t1_mem0 += MAS_MEM[2]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 50
	c_t4_t1_t1_mem1 += MAS_MEM[3]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 50
	c_t5010_in += MAS_in[0]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 50
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 50
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t3_t20 = S.Task('c_t3_t20', length=2, delay_cost=1)
	S += c_t3_t20 >= 51
	c_t3_t20 += MAS[1]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 51
	c_t4110_in += MAS_in[0]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 51
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 51
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=8, delay_cost=1)
	S += c_t4_t1_t1 >= 51
	c_t4_t1_t1 += MM[0]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 51
	c_t4_t31_in += MAS_in[1]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 51
	c_t4_t31_mem0 += MAS_MEM[2]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 51
	c_t4_t31_mem1 += MAS_MEM[3]

	c_t5010 = S.Task('c_t5010', length=2, delay_cost=1)
	S += c_t5010 >= 51
	c_t5010 += MAS[0]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 51
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 51
	c_t5_t1_t1_mem0 += MAS_MEM[0]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 51
	c_t5_t1_t1_mem1 += MAS_MEM[1]

	c_t4110 = S.Task('c_t4110', length=2, delay_cost=1)
	S += c_t4110 >= 52
	c_t4110 += MAS[0]

	c_t4_t31 = S.Task('c_t4_t31', length=2, delay_cost=1)
	S += c_t4_t31 >= 52
	c_t4_t31 += MAS[1]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 52
	c_t5001_in += MAS_in[1]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 52
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 52
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=8, delay_cost=1)
	S += c_t5_t1_t1 >= 52
	c_t5_t1_t1 += MM[0]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 52
	c_t5_t1_t2_in += MAS_in[0]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 52
	c_t5_t1_t2_mem0 += MAS_MEM[0]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 52
	c_t5_t1_t2_mem1 += MAS_MEM[1]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 53
	c_t3110_in += MAS_in[0]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 53
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 53
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 53
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 53
	c_t4_t1_t0_mem0 += MAS_MEM[0]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 53
	c_t4_t1_t0_mem1 += MAS_MEM[1]

	c_t5001 = S.Task('c_t5001', length=2, delay_cost=1)
	S += c_t5001 >= 53
	c_t5001 += MAS[1]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=2, delay_cost=1)
	S += c_t5_t1_t2 >= 53
	c_t5_t1_t2 += MAS[0]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 54
	c_t2_t31_in += MAS_in[0]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 54
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 54
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t3110 = S.Task('c_t3110', length=2, delay_cost=1)
	S += c_t3110 >= 54
	c_t3110 += MAS[0]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=8, delay_cost=1)
	S += c_t4_t1_t0 >= 54
	c_t4_t1_t0 += MM[0]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 54
	c_t4_t1_t3_in += MAS_in[1]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 54
	c_t4_t1_t3_mem0 += MAS_MEM[0]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 54
	c_t4_t1_t3_mem1 += MAS_MEM[3]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 54
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 54
	c_t5_t0_t1_mem0 += MAS_MEM[2]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 54
	c_t5_t0_t1_mem1 += MAS_MEM[1]

	c_t2_t31 = S.Task('c_t2_t31', length=2, delay_cost=1)
	S += c_t2_t31 >= 55
	c_t2_t31 += MAS[0]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 55
	c_t3011_in += MAS_in[1]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 55
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 55
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 55
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 55
	c_t3_t1_t0_mem0 += MAS_MEM[0]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 55
	c_t3_t1_t0_mem1 += MAS_MEM[1]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=2, delay_cost=1)
	S += c_t4_t1_t3 >= 55
	c_t4_t1_t3 += MAS[1]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=8, delay_cost=1)
	S += c_t5_t0_t1 >= 55
	c_t5_t0_t1 += MM[0]

	c_t3011 = S.Task('c_t3011', length=2, delay_cost=1)
	S += c_t3011 >= 56
	c_t3011 += MAS[1]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=8, delay_cost=1)
	S += c_t3_t1_t0 >= 56
	c_t3_t1_t0 += MM[0]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 56
	c_t3_t1_t3_in += MAS_in[1]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 56
	c_t3_t1_t3_mem0 += MAS_MEM[0]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 56
	c_t3_t1_t3_mem1 += MAS_MEM[3]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 56
	c_t4100_in += MAS_in[0]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 56
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 56
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 57
	c_t2_t20_in += MAS_in[0]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 57
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 57
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 57
	c_t2_t4_t1_in += MM_in[0]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 57
	c_t2_t4_t1_mem0 += MAS_MEM[0]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 57
	c_t2_t4_t1_mem1 += MAS_MEM[1]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=2, delay_cost=1)
	S += c_t3_t1_t3 >= 57
	c_t3_t1_t3 += MAS[1]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 57
	c_t3_t21_in += MAS_in[1]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 57
	c_t3_t21_mem0 += MAS_MEM[2]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 57
	c_t3_t21_mem1 += MAS_MEM[3]

	c_t4100 = S.Task('c_t4100', length=2, delay_cost=1)
	S += c_t4100 >= 57
	c_t4100 += MAS[0]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 58
	c_t2_t1_t3_in += MAS_in[0]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 58
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 58
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t20 = S.Task('c_t2_t20', length=2, delay_cost=1)
	S += c_t2_t20 >= 58
	c_t2_t20 += MAS[0]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=8, delay_cost=1)
	S += c_t2_t4_t1 >= 58
	c_t2_t4_t1 += MM[0]

	c_t3_t21 = S.Task('c_t3_t21', length=2, delay_cost=1)
	S += c_t3_t21 >= 58
	c_t3_t21 += MAS[1]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 58
	c_t4_t0_t0_in += MM_in[0]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 58
	c_t4_t0_t0_mem0 += MAS_MEM[2]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 58
	c_t4_t0_t0_mem1 += MAS_MEM[1]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 58
	c_t4_t0_t3_in += MAS_in[1]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 58
	c_t4_t0_t3_mem0 += MAS_MEM[0]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 58
	c_t4_t0_t3_mem1 += MAS_MEM[3]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 59
	c_t2_t1_t2_in += MAS_in[0]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 59
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 59
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=2, delay_cost=1)
	S += c_t2_t1_t3 >= 59
	c_t2_t1_t3 += MAS[0]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 59
	c_t2_t4_t2_in += MAS_in[1]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 59
	c_t2_t4_t2_mem0 += MAS_MEM[0]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 59
	c_t2_t4_t2_mem1 += MAS_MEM[1]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 59
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 59
	c_t3_t1_t1_mem0 += MAS_MEM[2]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 59
	c_t3_t1_t1_mem1 += MAS_MEM[3]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=8, delay_cost=1)
	S += c_t4_t0_t0 >= 59
	c_t4_t0_t0 += MM[0]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=2, delay_cost=1)
	S += c_t4_t0_t3 >= 59
	c_t4_t0_t3 += MAS[1]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=2, delay_cost=1)
	S += c_t2_t1_t2 >= 60
	c_t2_t1_t2 += MAS[0]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=2, delay_cost=1)
	S += c_t2_t4_t2 >= 60
	c_t2_t4_t2 += MAS[1]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 60
	c_t2_t4_t3_in += MAS_in[1]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 60
	c_t2_t4_t3_mem0 += MAS_MEM[2]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 60
	c_t2_t4_t3_mem1 += MAS_MEM[1]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=8, delay_cost=1)
	S += c_t3_t1_t1 >= 60
	c_t3_t1_t1 += MM[0]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 60
	c_t3_t1_t2_in += MAS_in[0]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 60
	c_t3_t1_t2_mem0 += MAS_MEM[0]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 60
	c_t3_t1_t2_mem1 += MAS_MEM[3]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 61
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 61
	c_t2_t4_t0_mem0 += MAS_MEM[0]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 61
	c_t2_t4_t0_mem1 += MAS_MEM[3]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=2, delay_cost=1)
	S += c_t2_t4_t3 >= 61
	c_t2_t4_t3 += MAS[1]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=2, delay_cost=1)
	S += c_t3_t1_t2 >= 61
	c_t3_t1_t2 += MAS[0]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 61
	c_t3_t30_in += MAS_in[0]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 61
	c_t3_t30_mem0 += MAS_MEM[2]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 61
	c_t3_t30_mem1 += MAS_MEM[1]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 62
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 62
	c_t2_t1_t4_mem0 += MAS_MEM[0]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 62
	c_t2_t1_t4_mem1 += MAS_MEM[1]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=8, delay_cost=1)
	S += c_t2_t4_t0 >= 62
	c_t2_t4_t0 += MM[0]

	c_t3_t30 = S.Task('c_t3_t30', length=2, delay_cost=1)
	S += c_t3_t30 >= 62
	c_t3_t30 += MAS[0]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=8, delay_cost=1)
	S += c_t2_t1_t4 >= 63
	c_t2_t1_t4 += MM[0]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 63
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 63
	c_t5_t1_t0_mem0 += MAS_MEM[0]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 63
	c_t5_t1_t0_mem1 += MAS_MEM[3]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 63
	c_t5_t21_in += MAS_in[0]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 63
	c_t5_t21_mem0 += MAS_MEM[2]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 63
	c_t5_t21_mem1 += MAS_MEM[1]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=8, delay_cost=1)
	S += c_t5_t1_t0 >= 64
	c_t5_t1_t0 += MM[0]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 64
	c_t5_t20_in += MAS_in[1]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 64
	c_t5_t20_mem0 += MAS_MEM[0]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 64
	c_t5_t20_mem1 += MAS_MEM[1]

	c_t5_t21 = S.Task('c_t5_t21', length=2, delay_cost=1)
	S += c_t5_t21 >= 64
	c_t5_t21 += MAS[0]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 65
	c_t5_t0_t2_in += MAS_in[1]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 65
	c_t5_t0_t2_mem0 += MAS_MEM[0]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 65
	c_t5_t0_t2_mem1 += MAS_MEM[3]

	c_t5_t20 = S.Task('c_t5_t20', length=2, delay_cost=1)
	S += c_t5_t20 >= 65
	c_t5_t20 += MAS[1]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 66
	c_t4_t30_in += MAS_in[1]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 66
	c_t4_t30_mem0 += MAS_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 66
	c_t4_t30_mem1 += MAS_MEM[1]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=2, delay_cost=1)
	S += c_t5_t0_t2 >= 66
	c_t5_t0_t2 += MAS[1]

	c_t4_t30 = S.Task('c_t4_t30', length=2, delay_cost=1)
	S += c_t4_t30 >= 67
	c_t4_t30 += MAS[1]


	# new tasks
	c_t0_t01 = S.Task('c_t0_t01', length=2, delay_cost=1)
	c_t0_t01 += alt(MAS)
	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	c_t0_t01_in += alt(MAS_in)
	S += c_t0_t01_in*MAS_in[0]<=c_t0_t01*MAS[0]

	S += c_t0_t01_in*MAS_in[1]<=c_t0_t01*MAS[1]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	c_t0_t01_mem0 += MM_MEM[0]
	S += 39 < c_t0_t01_mem0
	S += c_t0_t01_mem0 <= c_t0_t01

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	c_t0_t01_mem1 += MAS_MEM[3]
	S += 39 < c_t0_t01_mem1
	S += c_t0_t01_mem1 <= c_t0_t01

	c_t0_t11 = S.Task('c_t0_t11', length=2, delay_cost=1)
	c_t0_t11 += alt(MAS)
	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	c_t0_t11_in += alt(MAS_in)
	S += c_t0_t11_in*MAS_in[0]<=c_t0_t11*MAS[0]

	S += c_t0_t11_in*MAS_in[1]<=c_t0_t11*MAS[1]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	c_t0_t11_mem0 += MM_MEM[0]
	S += 22 < c_t0_t11_mem0
	S += c_t0_t11_mem0 <= c_t0_t11

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	c_t0_t11_mem1 += MAS_MEM[3]
	S += 38 < c_t0_t11_mem1
	S += c_t0_t11_mem1 <= c_t0_t11

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=8, delay_cost=1)
	c_t0_t4_t4 += alt(MM)
	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	c_t0_t4_t4_in += alt(MM_in)
	S += c_t0_t4_t4_in*MM_in[0]<=c_t0_t4_t4*MM[0]
	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	c_t0_t4_t4_mem0 += MAS_MEM[2]
	S += 13 < c_t0_t4_t4_mem0
	S += c_t0_t4_t4_mem0 <= c_t0_t4_t4

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	c_t0_t4_t4_mem1 += MAS_MEM[3]
	S += 20 < c_t0_t4_t4_mem1
	S += c_t0_t4_t4_mem1 <= c_t0_t4_t4

	c_t0_t40 = S.Task('c_t0_t40', length=2, delay_cost=1)
	c_t0_t40 += alt(MAS)
	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	c_t0_t40_in += alt(MAS_in)
	S += c_t0_t40_in*MAS_in[0]<=c_t0_t40*MAS[0]

	S += c_t0_t40_in*MAS_in[1]<=c_t0_t40*MAS[1]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	c_t0_t40_mem0 += MM_MEM[0]
	S += 20 < c_t0_t40_mem0
	S += c_t0_t40_mem0 <= c_t0_t40

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	c_t0_t40_mem1 += MM_MEM[1]
	S += 24 < c_t0_t40_mem1
	S += c_t0_t40_mem1 <= c_t0_t40

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=2, delay_cost=1)
	c_t0_t4_t5 += alt(MAS)
	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	c_t0_t4_t5_in += alt(MAS_in)
	S += c_t0_t4_t5_in*MAS_in[0]<=c_t0_t4_t5*MAS[0]

	S += c_t0_t4_t5_in*MAS_in[1]<=c_t0_t4_t5*MAS[1]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	c_t0_t4_t5_mem0 += MM_MEM[0]
	S += 20 < c_t0_t4_t5_mem0
	S += c_t0_t4_t5_mem0 <= c_t0_t4_t5

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	c_t0_t4_t5_mem1 += MM_MEM[1]
	S += 24 < c_t0_t4_t5_mem1
	S += c_t0_t4_t5_mem1 <= c_t0_t4_t5

	c_t0_t50 = S.Task('c_t0_t50', length=2, delay_cost=1)
	c_t0_t50 += alt(MAS)
	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	c_t0_t50_in += alt(MAS_in)
	S += c_t0_t50_in*MAS_in[0]<=c_t0_t50*MAS[0]

	S += c_t0_t50_in*MAS_in[1]<=c_t0_t50*MAS[1]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	c_t0_t50_mem0 += MAS_MEM[0]
	S += 40 < c_t0_t50_mem0
	S += c_t0_t50_mem0 <= c_t0_t50

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	c_t0_t50_mem1 += MAS_MEM[3]
	S += 37 < c_t0_t50_mem1
	S += c_t0_t50_mem1 <= c_t0_t50

	c_t1_t01 = S.Task('c_t1_t01', length=2, delay_cost=1)
	c_t1_t01 += alt(MAS)
	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	c_t1_t01_in += alt(MAS_in)
	S += c_t1_t01_in*MAS_in[0]<=c_t1_t01*MAS[0]

	S += c_t1_t01_in*MAS_in[1]<=c_t1_t01*MAS[1]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	c_t1_t01_mem0 += MM_MEM[0]
	S += 25 < c_t1_t01_mem0
	S += c_t1_t01_mem0 <= c_t1_t01

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	c_t1_t01_mem1 += MAS_MEM[1]
	S += 33 < c_t1_t01_mem1
	S += c_t1_t01_mem1 <= c_t1_t01

	c_t1_t11 = S.Task('c_t1_t11', length=2, delay_cost=1)
	c_t1_t11 += alt(MAS)
	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	c_t1_t11_in += alt(MAS_in)
	S += c_t1_t11_in*MAS_in[0]<=c_t1_t11*MAS[0]

	S += c_t1_t11_in*MAS_in[1]<=c_t1_t11*MAS[1]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	c_t1_t11_mem0 += MM_MEM[0]
	S += 29 < c_t1_t11_mem0
	S += c_t1_t11_mem0 <= c_t1_t11

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	c_t1_t11_mem1 += MAS_MEM[1]
	S += 28 < c_t1_t11_mem1
	S += c_t1_t11_mem1 <= c_t1_t11

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=8, delay_cost=1)
	c_t1_t4_t4 += alt(MM)
	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	c_t1_t4_t4_in += alt(MM_in)
	S += c_t1_t4_t4_in*MM_in[0]<=c_t1_t4_t4*MM[0]
	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	c_t1_t4_t4_mem0 += MAS_MEM[0]
	S += 25 < c_t1_t4_t4_mem0
	S += c_t1_t4_t4_mem0 <= c_t1_t4_t4

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	c_t1_t4_t4_mem1 += MAS_MEM[3]
	S += 29 < c_t1_t4_t4_mem1
	S += c_t1_t4_t4_mem1 <= c_t1_t4_t4

	c_t1_t40 = S.Task('c_t1_t40', length=2, delay_cost=1)
	c_t1_t40 += alt(MAS)
	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	c_t1_t40_in += alt(MAS_in)
	S += c_t1_t40_in*MAS_in[0]<=c_t1_t40*MAS[0]

	S += c_t1_t40_in*MAS_in[1]<=c_t1_t40*MAS[1]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	c_t1_t40_mem0 += MM_MEM[0]
	S += 34 < c_t1_t40_mem0
	S += c_t1_t40_mem0 <= c_t1_t40

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	c_t1_t40_mem1 += MM_MEM[1]
	S += 17 < c_t1_t40_mem1
	S += c_t1_t40_mem1 <= c_t1_t40

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=2, delay_cost=1)
	c_t1_t4_t5 += alt(MAS)
	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	c_t1_t4_t5_in += alt(MAS_in)
	S += c_t1_t4_t5_in*MAS_in[0]<=c_t1_t4_t5*MAS[0]

	S += c_t1_t4_t5_in*MAS_in[1]<=c_t1_t4_t5*MAS[1]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	c_t1_t4_t5_mem0 += MM_MEM[0]
	S += 34 < c_t1_t4_t5_mem0
	S += c_t1_t4_t5_mem0 <= c_t1_t4_t5

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	c_t1_t4_t5_mem1 += MM_MEM[1]
	S += 17 < c_t1_t4_t5_mem1
	S += c_t1_t4_t5_mem1 <= c_t1_t4_t5

	c_t1_t50 = S.Task('c_t1_t50', length=2, delay_cost=1)
	c_t1_t50 += alt(MAS)
	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	c_t1_t50_in += alt(MAS_in)
	S += c_t1_t50_in*MAS_in[0]<=c_t1_t50*MAS[0]

	S += c_t1_t50_in*MAS_in[1]<=c_t1_t50*MAS[1]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	c_t1_t50_mem0 += MAS_MEM[0]
	S += 32 < c_t1_t50_mem0
	S += c_t1_t50_mem0 <= c_t1_t50

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	c_t1_t50_mem1 += MAS_MEM[1]
	S += 29 < c_t1_t50_mem1
	S += c_t1_t50_mem1 <= c_t1_t50

	c_t2_t01 = S.Task('c_t2_t01', length=2, delay_cost=1)
	c_t2_t01 += alt(MAS)
	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	c_t2_t01_in += alt(MAS_in)
	S += c_t2_t01_in*MAS_in[0]<=c_t2_t01*MAS[0]

	S += c_t2_t01_in*MAS_in[1]<=c_t2_t01*MAS[1]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	c_t2_t01_mem0 += MM_MEM[0]
	S += 38 < c_t2_t01_mem0
	S += c_t2_t01_mem0 <= c_t2_t01

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	c_t2_t01_mem1 += MAS_MEM[3]
	S += 26 < c_t2_t01_mem1
	S += c_t2_t01_mem1 <= c_t2_t01

	c_t2_t11 = S.Task('c_t2_t11', length=2, delay_cost=1)
	c_t2_t11 += alt(MAS)
	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	c_t2_t11_in += alt(MAS_in)
	S += c_t2_t11_in*MAS_in[0]<=c_t2_t11*MAS[0]

	S += c_t2_t11_in*MAS_in[1]<=c_t2_t11*MAS[1]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	c_t2_t11_mem0 += MM_MEM[0]
	S += 70 < c_t2_t11_mem0
	S += c_t2_t11_mem0 <= c_t2_t11

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	c_t2_t11_mem1 += MAS_MEM[1]
	S += 30 < c_t2_t11_mem1
	S += c_t2_t11_mem1 <= c_t2_t11

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=8, delay_cost=1)
	c_t2_t4_t4 += alt(MM)
	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	c_t2_t4_t4_in += alt(MM_in)
	S += c_t2_t4_t4_in*MM_in[0]<=c_t2_t4_t4*MM[0]
	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	c_t2_t4_t4_mem0 += MAS_MEM[2]
	S += 61 < c_t2_t4_t4_mem0
	S += c_t2_t4_t4_mem0 <= c_t2_t4_t4

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	c_t2_t4_t4_mem1 += MAS_MEM[3]
	S += 62 < c_t2_t4_t4_mem1
	S += c_t2_t4_t4_mem1 <= c_t2_t4_t4

	c_t2_t40 = S.Task('c_t2_t40', length=2, delay_cost=1)
	c_t2_t40 += alt(MAS)
	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	c_t2_t40_in += alt(MAS_in)
	S += c_t2_t40_in*MAS_in[0]<=c_t2_t40*MAS[0]

	S += c_t2_t40_in*MAS_in[1]<=c_t2_t40*MAS[1]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	c_t2_t40_mem0 += MM_MEM[0]
	S += 69 < c_t2_t40_mem0
	S += c_t2_t40_mem0 <= c_t2_t40

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	c_t2_t40_mem1 += MM_MEM[1]
	S += 65 < c_t2_t40_mem1
	S += c_t2_t40_mem1 <= c_t2_t40

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=2, delay_cost=1)
	c_t2_t4_t5 += alt(MAS)
	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	c_t2_t4_t5_in += alt(MAS_in)
	S += c_t2_t4_t5_in*MAS_in[0]<=c_t2_t4_t5*MAS[0]

	S += c_t2_t4_t5_in*MAS_in[1]<=c_t2_t4_t5*MAS[1]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	c_t2_t4_t5_mem0 += MM_MEM[0]
	S += 69 < c_t2_t4_t5_mem0
	S += c_t2_t4_t5_mem0 <= c_t2_t4_t5

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	c_t2_t4_t5_mem1 += MM_MEM[1]
	S += 65 < c_t2_t4_t5_mem1
	S += c_t2_t4_t5_mem1 <= c_t2_t4_t5

	c_t2_t50 = S.Task('c_t2_t50', length=2, delay_cost=1)
	c_t2_t50 += alt(MAS)
	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	c_t2_t50_in += alt(MAS_in)
	S += c_t2_t50_in*MAS_in[0]<=c_t2_t50*MAS[0]

	S += c_t2_t50_in*MAS_in[1]<=c_t2_t50*MAS[1]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	c_t2_t50_mem0 += MAS_MEM[2]
	S += 25 < c_t2_t50_mem0
	S += c_t2_t50_mem0 <= c_t2_t50

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	c_t2_t50_mem1 += MAS_MEM[3]
	S += 31 < c_t2_t50_mem1
	S += c_t2_t50_mem1 <= c_t2_t50

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=8, delay_cost=1)
	c_t3_t0_t4 += alt(MM)
	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	c_t3_t0_t4_in += alt(MM_in)
	S += c_t3_t0_t4_in*MM_in[0]<=c_t3_t0_t4*MM[0]
	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	c_t3_t0_t4_mem0 += MAS_MEM[0]
	S += 49 < c_t3_t0_t4_mem0
	S += c_t3_t0_t4_mem0 <= c_t3_t0_t4

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	c_t3_t0_t4_mem1 += MAS_MEM[3]
	S += 48 < c_t3_t0_t4_mem1
	S += c_t3_t0_t4_mem1 <= c_t3_t0_t4

	c_t3_t00 = S.Task('c_t3_t00', length=2, delay_cost=1)
	c_t3_t00 += alt(MAS)
	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	c_t3_t00_in += alt(MAS_in)
	S += c_t3_t00_in*MAS_in[0]<=c_t3_t00*MAS[0]

	S += c_t3_t00_in*MAS_in[1]<=c_t3_t00*MAS[1]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	c_t3_t00_mem0 += MM_MEM[0]
	S += 56 < c_t3_t00_mem0
	S += c_t3_t00_mem0 <= c_t3_t00

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	c_t3_t00_mem1 += MM_MEM[1]
	S += 55 < c_t3_t00_mem1
	S += c_t3_t00_mem1 <= c_t3_t00

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=2, delay_cost=1)
	c_t3_t0_t5 += alt(MAS)
	c_t3_t0_t5_in = S.Task('c_t3_t0_t5_in', length=1, delay_cost=1)
	c_t3_t0_t5_in += alt(MAS_in)
	S += c_t3_t0_t5_in*MAS_in[0]<=c_t3_t0_t5*MAS[0]

	S += c_t3_t0_t5_in*MAS_in[1]<=c_t3_t0_t5*MAS[1]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	c_t3_t0_t5_mem0 += MM_MEM[0]
	S += 56 < c_t3_t0_t5_mem0
	S += c_t3_t0_t5_mem0 <= c_t3_t0_t5

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	c_t3_t0_t5_mem1 += MM_MEM[1]
	S += 55 < c_t3_t0_t5_mem1
	S += c_t3_t0_t5_mem1 <= c_t3_t0_t5

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=8, delay_cost=1)
	c_t3_t1_t4 += alt(MM)
	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	c_t3_t1_t4_in += alt(MM_in)
	S += c_t3_t1_t4_in*MM_in[0]<=c_t3_t1_t4*MM[0]
	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	c_t3_t1_t4_mem0 += MAS_MEM[0]
	S += 62 < c_t3_t1_t4_mem0
	S += c_t3_t1_t4_mem0 <= c_t3_t1_t4

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	c_t3_t1_t4_mem1 += MAS_MEM[3]
	S += 58 < c_t3_t1_t4_mem1
	S += c_t3_t1_t4_mem1 <= c_t3_t1_t4

	c_t3_t10 = S.Task('c_t3_t10', length=2, delay_cost=1)
	c_t3_t10 += alt(MAS)
	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	c_t3_t10_in += alt(MAS_in)
	S += c_t3_t10_in*MAS_in[0]<=c_t3_t10*MAS[0]

	S += c_t3_t10_in*MAS_in[1]<=c_t3_t10*MAS[1]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	c_t3_t10_mem0 += MM_MEM[0]
	S += 63 < c_t3_t10_mem0
	S += c_t3_t10_mem0 <= c_t3_t10

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	c_t3_t10_mem1 += MM_MEM[1]
	S += 67 < c_t3_t10_mem1
	S += c_t3_t10_mem1 <= c_t3_t10

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=2, delay_cost=1)
	c_t3_t1_t5 += alt(MAS)
	c_t3_t1_t5_in = S.Task('c_t3_t1_t5_in', length=1, delay_cost=1)
	c_t3_t1_t5_in += alt(MAS_in)
	S += c_t3_t1_t5_in*MAS_in[0]<=c_t3_t1_t5*MAS[0]

	S += c_t3_t1_t5_in*MAS_in[1]<=c_t3_t1_t5*MAS[1]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	c_t3_t1_t5_mem0 += MM_MEM[0]
	S += 63 < c_t3_t1_t5_mem0
	S += c_t3_t1_t5_mem0 <= c_t3_t1_t5

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	c_t3_t1_t5_mem1 += MM_MEM[1]
	S += 67 < c_t3_t1_t5_mem1
	S += c_t3_t1_t5_mem1 <= c_t3_t1_t5

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=8, delay_cost=1)
	c_t3_t4_t0 += alt(MM)
	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	c_t3_t4_t0_in += alt(MM_in)
	S += c_t3_t4_t0_in*MM_in[0]<=c_t3_t4_t0*MM[0]
	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	c_t3_t4_t0_mem0 += MAS_MEM[2]
	S += 52 < c_t3_t4_t0_mem0
	S += c_t3_t4_t0_mem0 <= c_t3_t4_t0

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	c_t3_t4_t0_mem1 += MAS_MEM[1]
	S += 63 < c_t3_t4_t0_mem1
	S += c_t3_t4_t0_mem1 <= c_t3_t4_t0

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=8, delay_cost=1)
	c_t3_t4_t1 += alt(MM)
	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	c_t3_t4_t1_in += alt(MM_in)
	S += c_t3_t4_t1_in*MM_in[0]<=c_t3_t4_t1*MM[0]
	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	c_t3_t4_t1_mem0 += MAS_MEM[2]
	S += 59 < c_t3_t4_t1_mem0
	S += c_t3_t4_t1_mem0 <= c_t3_t4_t1

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	c_t3_t4_t1_mem1 += MAS_MEM[3]
	S += 51 < c_t3_t4_t1_mem1
	S += c_t3_t4_t1_mem1 <= c_t3_t4_t1

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=2, delay_cost=1)
	c_t3_t4_t2 += alt(MAS)
	c_t3_t4_t2_in = S.Task('c_t3_t4_t2_in', length=1, delay_cost=1)
	c_t3_t4_t2_in += alt(MAS_in)
	S += c_t3_t4_t2_in*MAS_in[0]<=c_t3_t4_t2*MAS[0]

	S += c_t3_t4_t2_in*MAS_in[1]<=c_t3_t4_t2*MAS[1]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	c_t3_t4_t2_mem0 += MAS_MEM[2]
	S += 52 < c_t3_t4_t2_mem0
	S += c_t3_t4_t2_mem0 <= c_t3_t4_t2

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	c_t3_t4_t2_mem1 += MAS_MEM[3]
	S += 59 < c_t3_t4_t2_mem1
	S += c_t3_t4_t2_mem1 <= c_t3_t4_t2

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=2, delay_cost=1)
	c_t3_t4_t3 += alt(MAS)
	c_t3_t4_t3_in = S.Task('c_t3_t4_t3_in', length=1, delay_cost=1)
	c_t3_t4_t3_in += alt(MAS_in)
	S += c_t3_t4_t3_in*MAS_in[0]<=c_t3_t4_t3*MAS[0]

	S += c_t3_t4_t3_in*MAS_in[1]<=c_t3_t4_t3*MAS[1]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	c_t3_t4_t3_mem0 += MAS_MEM[0]
	S += 63 < c_t3_t4_t3_mem0
	S += c_t3_t4_t3_mem0 <= c_t3_t4_t3

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	c_t3_t4_t3_mem1 += MAS_MEM[3]
	S += 51 < c_t3_t4_t3_mem1
	S += c_t3_t4_t3_mem1 <= c_t3_t4_t3

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=8, delay_cost=1)
	c_t4_t0_t4 += alt(MM)
	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	c_t4_t0_t4_in += alt(MM_in)
	S += c_t4_t0_t4_in*MM_in[0]<=c_t4_t0_t4*MM[0]
	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	c_t4_t0_t4_mem0 += MAS_MEM[2]
	S += 46 < c_t4_t0_t4_mem0
	S += c_t4_t0_t4_mem0 <= c_t4_t0_t4

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	c_t4_t0_t4_mem1 += MAS_MEM[3]
	S += 60 < c_t4_t0_t4_mem1
	S += c_t4_t0_t4_mem1 <= c_t4_t0_t4

	c_t4_t00 = S.Task('c_t4_t00', length=2, delay_cost=1)
	c_t4_t00 += alt(MAS)
	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	c_t4_t00_in += alt(MAS_in)
	S += c_t4_t00_in*MAS_in[0]<=c_t4_t00*MAS[0]

	S += c_t4_t00_in*MAS_in[1]<=c_t4_t00*MAS[1]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	c_t4_t00_mem0 += MM_MEM[0]
	S += 66 < c_t4_t00_mem0
	S += c_t4_t00_mem0 <= c_t4_t00

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	c_t4_t00_mem1 += MM_MEM[1]
	S += 48 < c_t4_t00_mem1
	S += c_t4_t00_mem1 <= c_t4_t00

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=2, delay_cost=1)
	c_t4_t0_t5 += alt(MAS)
	c_t4_t0_t5_in = S.Task('c_t4_t0_t5_in', length=1, delay_cost=1)
	c_t4_t0_t5_in += alt(MAS_in)
	S += c_t4_t0_t5_in*MAS_in[0]<=c_t4_t0_t5*MAS[0]

	S += c_t4_t0_t5_in*MAS_in[1]<=c_t4_t0_t5*MAS[1]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	c_t4_t0_t5_mem0 += MM_MEM[0]
	S += 66 < c_t4_t0_t5_mem0
	S += c_t4_t0_t5_mem0 <= c_t4_t0_t5

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	c_t4_t0_t5_mem1 += MM_MEM[1]
	S += 48 < c_t4_t0_t5_mem1
	S += c_t4_t0_t5_mem1 <= c_t4_t0_t5

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=8, delay_cost=1)
	c_t4_t1_t4 += alt(MM)
	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	c_t4_t1_t4_in += alt(MM_in)
	S += c_t4_t1_t4_in*MM_in[0]<=c_t4_t1_t4*MM[0]
	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	c_t4_t1_t4_mem0 += MAS_MEM[0]
	S += 44 < c_t4_t1_t4_mem0
	S += c_t4_t1_t4_mem0 <= c_t4_t1_t4

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	c_t4_t1_t4_mem1 += MAS_MEM[3]
	S += 56 < c_t4_t1_t4_mem1
	S += c_t4_t1_t4_mem1 <= c_t4_t1_t4

	c_t4_t10 = S.Task('c_t4_t10', length=2, delay_cost=1)
	c_t4_t10 += alt(MAS)
	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	c_t4_t10_in += alt(MAS_in)
	S += c_t4_t10_in*MAS_in[0]<=c_t4_t10*MAS[0]

	S += c_t4_t10_in*MAS_in[1]<=c_t4_t10*MAS[1]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	c_t4_t10_mem0 += MM_MEM[0]
	S += 61 < c_t4_t10_mem0
	S += c_t4_t10_mem0 <= c_t4_t10

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	c_t4_t10_mem1 += MM_MEM[1]
	S += 58 < c_t4_t10_mem1
	S += c_t4_t10_mem1 <= c_t4_t10

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=2, delay_cost=1)
	c_t4_t1_t5 += alt(MAS)
	c_t4_t1_t5_in = S.Task('c_t4_t1_t5_in', length=1, delay_cost=1)
	c_t4_t1_t5_in += alt(MAS_in)
	S += c_t4_t1_t5_in*MAS_in[0]<=c_t4_t1_t5*MAS[0]

	S += c_t4_t1_t5_in*MAS_in[1]<=c_t4_t1_t5*MAS[1]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	c_t4_t1_t5_mem0 += MM_MEM[0]
	S += 61 < c_t4_t1_t5_mem0
	S += c_t4_t1_t5_mem0 <= c_t4_t1_t5

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	c_t4_t1_t5_mem1 += MM_MEM[1]
	S += 58 < c_t4_t1_t5_mem1
	S += c_t4_t1_t5_mem1 <= c_t4_t1_t5

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=8, delay_cost=1)
	c_t4_t4_t0 += alt(MM)
	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	c_t4_t4_t0_in += alt(MM_in)
	S += c_t4_t4_t0_in*MM_in[0]<=c_t4_t4_t0*MM[0]
	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	c_t4_t4_t0_mem0 += MAS_MEM[0]
	S += 50 < c_t4_t4_t0_mem0
	S += c_t4_t4_t0_mem0 <= c_t4_t4_t0

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	c_t4_t4_t0_mem1 += MAS_MEM[3]
	S += 68 < c_t4_t4_t0_mem1
	S += c_t4_t4_t0_mem1 <= c_t4_t4_t0

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=8, delay_cost=1)
	c_t4_t4_t1 += alt(MM)
	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	c_t4_t4_t1_in += alt(MM_in)
	S += c_t4_t4_t1_in*MM_in[0]<=c_t4_t4_t1*MM[0]
	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	c_t4_t4_t1_mem0 += MAS_MEM[2]
	S += 47 < c_t4_t4_t1_mem0
	S += c_t4_t4_t1_mem0 <= c_t4_t4_t1

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	c_t4_t4_t1_mem1 += MAS_MEM[3]
	S += 53 < c_t4_t4_t1_mem1
	S += c_t4_t4_t1_mem1 <= c_t4_t4_t1

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=2, delay_cost=1)
	c_t4_t4_t2 += alt(MAS)
	c_t4_t4_t2_in = S.Task('c_t4_t4_t2_in', length=1, delay_cost=1)
	c_t4_t4_t2_in += alt(MAS_in)
	S += c_t4_t4_t2_in*MAS_in[0]<=c_t4_t4_t2*MAS[0]

	S += c_t4_t4_t2_in*MAS_in[1]<=c_t4_t4_t2*MAS[1]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	c_t4_t4_t2_mem0 += MAS_MEM[0]
	S += 50 < c_t4_t4_t2_mem0
	S += c_t4_t4_t2_mem0 <= c_t4_t4_t2

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	c_t4_t4_t2_mem1 += MAS_MEM[3]
	S += 47 < c_t4_t4_t2_mem1
	S += c_t4_t4_t2_mem1 <= c_t4_t4_t2

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=2, delay_cost=1)
	c_t4_t4_t3 += alt(MAS)
	c_t4_t4_t3_in = S.Task('c_t4_t4_t3_in', length=1, delay_cost=1)
	c_t4_t4_t3_in += alt(MAS_in)
	S += c_t4_t4_t3_in*MAS_in[0]<=c_t4_t4_t3*MAS[0]

	S += c_t4_t4_t3_in*MAS_in[1]<=c_t4_t4_t3*MAS[1]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	c_t4_t4_t3_mem0 += MAS_MEM[2]
	S += 68 < c_t4_t4_t3_mem0
	S += c_t4_t4_t3_mem0 <= c_t4_t4_t3

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	c_t4_t4_t3_mem1 += MAS_MEM[3]
	S += 53 < c_t4_t4_t3_mem1
	S += c_t4_t4_t3_mem1 <= c_t4_t4_t3

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=8, delay_cost=1)
	c_t5_t0_t4 += alt(MM)
	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	c_t5_t0_t4_in += alt(MM_in)
	S += c_t5_t0_t4_in*MM_in[0]<=c_t5_t0_t4*MM[0]
	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	c_t5_t0_t4_mem0 += MAS_MEM[2]
	S += 67 < c_t5_t0_t4_mem0
	S += c_t5_t0_t4_mem0 <= c_t5_t0_t4

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	c_t5_t0_t4_mem1 += MAS_MEM[3]
	S += 45 < c_t5_t0_t4_mem1
	S += c_t5_t0_t4_mem1 <= c_t5_t0_t4

	c_t5_t00 = S.Task('c_t5_t00', length=2, delay_cost=1)
	c_t5_t00 += alt(MAS)
	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	c_t5_t00_in += alt(MAS_in)
	S += c_t5_t00_in*MAS_in[0]<=c_t5_t00*MAS[0]

	S += c_t5_t00_in*MAS_in[1]<=c_t5_t00*MAS[1]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	c_t5_t00_mem0 += MM_MEM[0]
	S += 45 < c_t5_t00_mem0
	S += c_t5_t00_mem0 <= c_t5_t00

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	c_t5_t00_mem1 += MM_MEM[1]
	S += 62 < c_t5_t00_mem1
	S += c_t5_t00_mem1 <= c_t5_t00

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=2, delay_cost=1)
	c_t5_t0_t5 += alt(MAS)
	c_t5_t0_t5_in = S.Task('c_t5_t0_t5_in', length=1, delay_cost=1)
	c_t5_t0_t5_in += alt(MAS_in)
	S += c_t5_t0_t5_in*MAS_in[0]<=c_t5_t0_t5*MAS[0]

	S += c_t5_t0_t5_in*MAS_in[1]<=c_t5_t0_t5*MAS[1]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	c_t5_t0_t5_mem0 += MM_MEM[0]
	S += 45 < c_t5_t0_t5_mem0
	S += c_t5_t0_t5_mem0 <= c_t5_t0_t5

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	c_t5_t0_t5_mem1 += MM_MEM[1]
	S += 62 < c_t5_t0_t5_mem1
	S += c_t5_t0_t5_mem1 <= c_t5_t0_t5

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=8, delay_cost=1)
	c_t5_t1_t4 += alt(MM)
	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	c_t5_t1_t4_in += alt(MM_in)
	S += c_t5_t1_t4_in*MM_in[0]<=c_t5_t1_t4*MM[0]
	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	c_t5_t1_t4_mem0 += MAS_MEM[0]
	S += 54 < c_t5_t1_t4_mem0
	S += c_t5_t1_t4_mem0 <= c_t5_t1_t4

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	c_t5_t1_t4_mem1 += MAS_MEM[1]
	S += 42 < c_t5_t1_t4_mem1
	S += c_t5_t1_t4_mem1 <= c_t5_t1_t4

	c_t5_t10 = S.Task('c_t5_t10', length=2, delay_cost=1)
	c_t5_t10 += alt(MAS)
	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	c_t5_t10_in += alt(MAS_in)
	S += c_t5_t10_in*MAS_in[0]<=c_t5_t10*MAS[0]

	S += c_t5_t10_in*MAS_in[1]<=c_t5_t10*MAS[1]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	c_t5_t10_mem0 += MM_MEM[0]
	S += 71 < c_t5_t10_mem0
	S += c_t5_t10_mem0 <= c_t5_t10

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	c_t5_t10_mem1 += MM_MEM[1]
	S += 59 < c_t5_t10_mem1
	S += c_t5_t10_mem1 <= c_t5_t10

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=2, delay_cost=1)
	c_t5_t1_t5 += alt(MAS)
	c_t5_t1_t5_in = S.Task('c_t5_t1_t5_in', length=1, delay_cost=1)
	c_t5_t1_t5_in += alt(MAS_in)
	S += c_t5_t1_t5_in*MAS_in[0]<=c_t5_t1_t5*MAS[0]

	S += c_t5_t1_t5_in*MAS_in[1]<=c_t5_t1_t5*MAS[1]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	c_t5_t1_t5_mem0 += MM_MEM[0]
	S += 71 < c_t5_t1_t5_mem0
	S += c_t5_t1_t5_mem0 <= c_t5_t1_t5

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	c_t5_t1_t5_mem1 += MM_MEM[1]
	S += 59 < c_t5_t1_t5_mem1
	S += c_t5_t1_t5_mem1 <= c_t5_t1_t5

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=8, delay_cost=1)
	c_t5_t4_t0 += alt(MM)
	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	c_t5_t4_t0_in += alt(MM_in)
	S += c_t5_t4_t0_in*MM_in[0]<=c_t5_t4_t0*MM[0]
	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	c_t5_t4_t0_mem0 += MAS_MEM[2]
	S += 66 < c_t5_t4_t0_mem0
	S += c_t5_t4_t0_mem0 <= c_t5_t4_t0

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	c_t5_t4_t0_mem1 += MAS_MEM[1]
	S += 41 < c_t5_t4_t0_mem1
	S += c_t5_t4_t0_mem1 <= c_t5_t4_t0

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=8, delay_cost=1)
	c_t5_t4_t1 += alt(MM)
	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	c_t5_t4_t1_in += alt(MM_in)
	S += c_t5_t4_t1_in*MM_in[0]<=c_t5_t4_t1*MM[0]
	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	c_t5_t4_t1_mem0 += MAS_MEM[0]
	S += 65 < c_t5_t4_t1_mem0
	S += c_t5_t4_t1_mem0 <= c_t5_t4_t1

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	c_t5_t4_t1_mem1 += MAS_MEM[1]
	S += 43 < c_t5_t4_t1_mem1
	S += c_t5_t4_t1_mem1 <= c_t5_t4_t1

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=2, delay_cost=1)
	c_t5_t4_t2 += alt(MAS)
	c_t5_t4_t2_in = S.Task('c_t5_t4_t2_in', length=1, delay_cost=1)
	c_t5_t4_t2_in += alt(MAS_in)
	S += c_t5_t4_t2_in*MAS_in[0]<=c_t5_t4_t2*MAS[0]

	S += c_t5_t4_t2_in*MAS_in[1]<=c_t5_t4_t2*MAS[1]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	c_t5_t4_t2_mem0 += MAS_MEM[2]
	S += 66 < c_t5_t4_t2_mem0
	S += c_t5_t4_t2_mem0 <= c_t5_t4_t2

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	c_t5_t4_t2_mem1 += MAS_MEM[1]
	S += 65 < c_t5_t4_t2_mem1
	S += c_t5_t4_t2_mem1 <= c_t5_t4_t2

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=2, delay_cost=1)
	c_t5_t4_t3 += alt(MAS)
	c_t5_t4_t3_in = S.Task('c_t5_t4_t3_in', length=1, delay_cost=1)
	c_t5_t4_t3_in += alt(MAS_in)
	S += c_t5_t4_t3_in*MAS_in[0]<=c_t5_t4_t3*MAS[0]

	S += c_t5_t4_t3_in*MAS_in[1]<=c_t5_t4_t3*MAS[1]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	c_t5_t4_t3_mem0 += MAS_MEM[0]
	S += 41 < c_t5_t4_t3_mem0
	S += c_t5_t4_t3_mem0 <= c_t5_t4_t3

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	c_t5_t4_t3_mem1 += MAS_MEM[1]
	S += 43 < c_t5_t4_t3_mem1
	S += c_t5_t4_t3_mem1 <= c_t5_t4_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage2MAS2/MUL/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution
