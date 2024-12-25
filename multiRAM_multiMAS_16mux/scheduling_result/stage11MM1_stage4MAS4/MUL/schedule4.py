from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 191
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=11)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
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

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 1
	c_t1_t30_in += MAS_in[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 1
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 1
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=4, delay_cost=1)
	S += c_t1_t31 >= 1
	c_t1_t31 += MAS[0]

	c_t1_t30 = S.Task('c_t1_t30', length=4, delay_cost=1)
	S += c_t1_t30 >= 2
	c_t1_t30 += MAS[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 2
	c_t2_t0_t3_in += MAS_in[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 2
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 2
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 3
	c_t0_t31_in += MAS_in[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 3
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 3
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=4, delay_cost=1)
	S += c_t2_t0_t3 >= 3
	c_t2_t0_t3 += MAS[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 4
	c_t0_t1_t2_in += MAS_in[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 4
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 4
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t31 = S.Task('c_t0_t31', length=4, delay_cost=1)
	S += c_t0_t31 >= 4
	c_t0_t31 += MAS[0]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=4, delay_cost=1)
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

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 5
	c_t1_t4_t3_in += MAS_in[1]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 5
	c_t1_t4_t3_mem0 += MAS_MEM[0]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 5
	c_t1_t4_t3_mem1 += MAS_MEM[1]

	c_t0_t30 = S.Task('c_t0_t30', length=4, delay_cost=1)
	S += c_t0_t30 >= 6
	c_t0_t30 += MAS[0]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 6
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 6
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 6
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=4, delay_cost=1)
	S += c_t1_t4_t3 >= 6
	c_t1_t4_t3 += MAS[1]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 7
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 7
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 7
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=11, delay_cost=1)
	S += c_t1_t0_t1 >= 7
	c_t1_t0_t1 += MM[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=4, delay_cost=1)
	S += c_t0_t1_t3 >= 8
	c_t0_t1_t3 += MAS[0]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 8
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 8
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 8
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 9
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 9
	c_t0_t4_t3_mem0 += MAS_MEM[0]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 9
	c_t0_t4_t3_mem1 += MAS_MEM[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=11, delay_cost=1)
	S += c_t1_t0_t0 >= 9
	c_t1_t0_t0 += MM[0]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 9
	c_t1_t1_t3_in += MAS_in[0]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 9
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 9
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=4, delay_cost=1)
	S += c_t0_t4_t3 >= 10
	c_t0_t4_t3 += MAS[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=4, delay_cost=1)
	S += c_t1_t1_t3 >= 10
	c_t1_t1_t3 += MAS[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 10
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 10
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 10
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 11
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 11
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 11
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=11, delay_cost=1)
	S += c_t2_t1_t1 >= 11
	c_t2_t1_t1 += MM[0]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 12
	c_t0_t1_t4_in += MM_in[0]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 12
	c_t0_t1_t4_mem0 += MAS_MEM[0]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 12
	c_t0_t1_t4_mem1 += MAS_MEM[1]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 12
	c_t1_t20_in += MAS_in[2]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 12
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 12
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=11, delay_cost=1)
	S += c_t2_t1_t0 >= 12
	c_t2_t1_t0 += MM[0]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=11, delay_cost=1)
	S += c_t0_t1_t4 >= 13
	c_t0_t1_t4 += MM[0]

	c_t1_t20 = S.Task('c_t1_t20', length=4, delay_cost=1)
	S += c_t1_t20 >= 13
	c_t1_t20 += MAS[2]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 13
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 13
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 13
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 14
	c_t1_t1_t2_in += MAS_in[1]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 14
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 14
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=11, delay_cost=1)
	S += c_t2_t0_t0 >= 14
	c_t2_t0_t0 += MM[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 15
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 15
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 15
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=4, delay_cost=1)
	S += c_t1_t1_t2 >= 15
	c_t1_t1_t2 += MAS[1]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 16
	c_t1_t0_t3_in += MAS_in[2]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 16
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 16
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=11, delay_cost=1)
	S += c_t1_t1_t1 >= 16
	c_t1_t1_t1 += MM[0]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 16
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 16
	c_t1_t4_t0_mem0 += MAS_MEM[4]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 16
	c_t1_t4_t0_mem1 += MAS_MEM[1]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 17
	c_t0_t0_t3_in += MAS_in[2]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 17
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 17
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=4, delay_cost=1)
	S += c_t1_t0_t3 >= 17
	c_t1_t0_t3 += MAS[2]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=11, delay_cost=1)
	S += c_t1_t4_t0 >= 17
	c_t1_t4_t0 += MM[0]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=4, delay_cost=1)
	S += c_t0_t0_t3 >= 18
	c_t0_t0_t3 += MAS[2]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 18
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 18
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 18
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 19
	c_t0_t20_in += MAS_in[3]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 19
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 19
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 19
	c_t1_t0_t5_in += MAS_in[0]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 19
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 19
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 19
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 19
	c_t1_t1_t4_mem0 += MAS_MEM[2]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 19
	c_t1_t1_t4_mem1 += MAS_MEM[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=11, delay_cost=1)
	S += c_t2_t0_t1 >= 19
	c_t2_t0_t1 += MM[0]

	c_t0_t20 = S.Task('c_t0_t20', length=4, delay_cost=1)
	S += c_t0_t20 >= 20
	c_t0_t20 += MAS[3]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 20
	c_t1_t00_in += MAS_in[1]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 20
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 20
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=4, delay_cost=1)
	S += c_t1_t0_t5 >= 20
	c_t1_t0_t5 += MAS[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 20
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 20
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 20
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=11, delay_cost=1)
	S += c_t1_t1_t4 >= 20
	c_t1_t1_t4 += MM[0]

	c_t1_t00 = S.Task('c_t1_t00', length=4, delay_cost=1)
	S += c_t1_t00 >= 21
	c_t1_t00 += MAS[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=11, delay_cost=1)
	S += c_t1_t1_t0 >= 21
	c_t1_t1_t0 += MM[0]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 21
	c_t1_t21_in += MAS_in[3]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 21
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 21
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 22
	c_t0_t21_in += MAS_in[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 22
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 22
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t21 = S.Task('c_t1_t21', length=4, delay_cost=1)
	S += c_t1_t21 >= 22
	c_t1_t21 += MAS[3]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 22
	c_t2_t10_in += MAS_in[0]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 22
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 22
	c_t2_t10_mem1 += MM_MEM[1]

	c_t0_t21 = S.Task('c_t0_t21', length=4, delay_cost=1)
	S += c_t0_t21 >= 23
	c_t0_t21 += MAS[1]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 23
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 23
	c_t0_t4_t0_mem0 += MAS_MEM[6]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 23
	c_t0_t4_t0_mem1 += MAS_MEM[1]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 23
	c_t2_t0_t2_in += MAS_in[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 23
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 23
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=4, delay_cost=1)
	S += c_t2_t10 >= 23
	c_t2_t10 += MAS[0]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 23
	c_t2_t1_t5_in += MAS_in[2]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 23
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 23
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 24
	c_t0_t0_t2_in += MAS_in[1]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 24
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 24
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=11, delay_cost=1)
	S += c_t0_t4_t0 >= 24
	c_t0_t4_t0 += MM[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=4, delay_cost=1)
	S += c_t2_t0_t2 >= 24
	c_t2_t0_t2 += MAS[0]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=4, delay_cost=1)
	S += c_t2_t1_t5 >= 24
	c_t2_t1_t5 += MAS[2]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=4, delay_cost=1)
	S += c_t0_t0_t2 >= 25
	c_t0_t0_t2 += MAS[1]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 25
	c_t1_t0_t2_in += MAS_in[1]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 25
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 25
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 25
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 25
	c_t1_t4_t1_mem0 += MAS_MEM[6]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 25
	c_t1_t4_t1_mem1 += MAS_MEM[1]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 25
	c_t1_t4_t2_in += MAS_in[3]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 25
	c_t1_t4_t2_mem0 += MAS_MEM[4]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 25
	c_t1_t4_t2_mem1 += MAS_MEM[7]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 26
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 26
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 26
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 26
	c_t0_t4_t2_in += MAS_in[2]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 26
	c_t0_t4_t2_mem0 += MAS_MEM[6]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 26
	c_t0_t4_t2_mem1 += MAS_MEM[3]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=4, delay_cost=1)
	S += c_t1_t0_t2 >= 26
	c_t1_t0_t2 += MAS[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=11, delay_cost=1)
	S += c_t1_t4_t1 >= 26
	c_t1_t4_t1 += MM[0]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=4, delay_cost=1)
	S += c_t1_t4_t2 >= 26
	c_t1_t4_t2 += MAS[3]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 27
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 27
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 27
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=11, delay_cost=1)
	S += c_t0_t1_t1 >= 27
	c_t0_t1_t1 += MM[0]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=4, delay_cost=1)
	S += c_t0_t4_t2 >= 27
	c_t0_t4_t2 += MAS[2]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 28
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 28
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 28
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=11, delay_cost=1)
	S += c_t0_t1_t0 >= 28
	c_t0_t1_t0 += MM[0]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 29
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 29
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 29
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=11, delay_cost=1)
	S += c_t0_t0_t1 >= 29
	c_t0_t0_t1 += MM[0]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 29
	c_t2_t0_t5_in += MAS_in[1]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 29
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 29
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=11, delay_cost=1)
	S += c_t0_t0_t0 >= 30
	c_t0_t0_t0 += MM[0]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 30
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 30
	c_t0_t0_t4_mem0 += MAS_MEM[2]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 30
	c_t0_t0_t4_mem1 += MAS_MEM[5]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 30
	c_t2_t00_in += MAS_in[2]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 30
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 30
	c_t2_t00_mem1 += MM_MEM[1]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=4, delay_cost=1)
	S += c_t2_t0_t5 >= 30
	c_t2_t0_t5 += MAS[1]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 30
	c_t2_t21_in += MAS_in[1]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 30
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 30
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=11, delay_cost=1)
	S += c_t0_t0_t4 >= 31
	c_t0_t0_t4 += MM[0]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 31
	c_t1_t1_t5_in += MAS_in[0]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 31
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 31
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t2_t00 = S.Task('c_t2_t00', length=4, delay_cost=1)
	S += c_t2_t00 >= 31
	c_t2_t00 += MAS[2]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 31
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 31
	c_t2_t0_t4_mem0 += MAS_MEM[0]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 31
	c_t2_t0_t4_mem1 += MAS_MEM[1]

	c_t2_t21 = S.Task('c_t2_t21', length=4, delay_cost=1)
	S += c_t2_t21 >= 31
	c_t2_t21 += MAS[1]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 31
	c_t2_t31_in += MAS_in[2]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 31
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 31
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 32
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 32
	c_t0_t4_t1_mem0 += MAS_MEM[2]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 32
	c_t0_t4_t1_mem1 += MAS_MEM[1]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 32
	c_t1_t10_in += MAS_in[1]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 32
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 32
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=4, delay_cost=1)
	S += c_t1_t1_t5 >= 32
	c_t1_t1_t5 += MAS[0]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=11, delay_cost=1)
	S += c_t2_t0_t4 >= 32
	c_t2_t0_t4 += MM[0]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 32
	c_t2_t20_in += MAS_in[2]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 32
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 32
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t31 = S.Task('c_t2_t31', length=4, delay_cost=1)
	S += c_t2_t31 >= 32
	c_t2_t31 += MAS[2]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=11, delay_cost=1)
	S += c_t0_t4_t1 >= 33
	c_t0_t4_t1 += MM[0]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 33
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 33
	c_t1_t0_t4_mem0 += MAS_MEM[2]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 33
	c_t1_t0_t4_mem1 += MAS_MEM[5]

	c_t1_t10 = S.Task('c_t1_t10', length=4, delay_cost=1)
	S += c_t1_t10 >= 33
	c_t1_t10 += MAS[1]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 33
	c_t2_t1_t3_in += MAS_in[3]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 33
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 33
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t20 = S.Task('c_t2_t20', length=4, delay_cost=1)
	S += c_t2_t20 >= 33
	c_t2_t20 += MAS[2]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=11, delay_cost=1)
	S += c_t1_t0_t4 >= 34
	c_t1_t0_t4 += MM[0]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=4, delay_cost=1)
	S += c_t2_t1_t3 >= 34
	c_t2_t1_t3 += MAS[3]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 34
	c_t3011_in += MAS_in[2]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 34
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 34
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 35
	c_t2_t4_t1_in += MM_in[0]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 35
	c_t2_t4_t1_mem0 += MAS_MEM[2]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 35
	c_t2_t4_t1_mem1 += MAS_MEM[5]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 35
	c_t3001_in += MAS_in[2]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 35
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 35
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=4, delay_cost=1)
	S += c_t3011 >= 35
	c_t3011 += MAS[2]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=11, delay_cost=1)
	S += c_t2_t4_t1 >= 36
	c_t2_t4_t1 += MM[0]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 36
	c_t2_t4_t2_in += MAS_in[0]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 36
	c_t2_t4_t2_mem0 += MAS_MEM[4]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 36
	c_t2_t4_t2_mem1 += MAS_MEM[3]

	c_t3001 = S.Task('c_t3001', length=4, delay_cost=1)
	S += c_t3001 >= 36
	c_t3001 += MAS[2]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 36
	c_t3100_in += MAS_in[1]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 36
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 36
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 37
	c_t2_t30_in += MAS_in[1]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 37
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 37
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=4, delay_cost=1)
	S += c_t2_t4_t2 >= 37
	c_t2_t4_t2 += MAS[0]

	c_t3100 = S.Task('c_t3100', length=4, delay_cost=1)
	S += c_t3100 >= 37
	c_t3100 += MAS[1]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 38
	c_t0_t1_t5_in += MAS_in[0]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 38
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 38
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t2_t30 = S.Task('c_t2_t30', length=4, delay_cost=1)
	S += c_t2_t30 >= 38
	c_t2_t30 += MAS[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 38
	c_t4010_in += MAS_in[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 38
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 38
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 39
	c_t0_t10_in += MAS_in[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 39
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 39
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=4, delay_cost=1)
	S += c_t0_t1_t5 >= 39
	c_t0_t1_t5 += MAS[0]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 39
	c_t3_t21_in += MAS_in[0]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 39
	c_t3_t21_mem0 += MAS_MEM[4]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 39
	c_t3_t21_mem1 += MAS_MEM[5]

	c_t4010 = S.Task('c_t4010', length=4, delay_cost=1)
	S += c_t4010 >= 39
	c_t4010 += MAS[1]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 39
	c_t4011_in += MAS_in[3]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 39
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 39
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 40
	c_t0_t0_t5_in += MAS_in[3]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 40
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 40
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t10 = S.Task('c_t0_t10', length=4, delay_cost=1)
	S += c_t0_t10 >= 40
	c_t0_t10 += MAS[1]

	c_t3_t21 = S.Task('c_t3_t21', length=4, delay_cost=1)
	S += c_t3_t21 >= 40
	c_t3_t21 += MAS[0]

	c_t4011 = S.Task('c_t4011', length=4, delay_cost=1)
	S += c_t4011 >= 40
	c_t4011 += MAS[3]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 40
	c_t4100_in += MAS_in[0]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 40
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 40
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 41
	c_t0_t00_in += MAS_in[2]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 41
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 41
	c_t0_t00_mem1 += MM_MEM[1]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=4, delay_cost=1)
	S += c_t0_t0_t5 >= 41
	c_t0_t0_t5 += MAS[3]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 41
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 41
	c_t2_t4_t0_mem0 += MAS_MEM[4]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 41
	c_t2_t4_t0_mem1 += MAS_MEM[3]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 41
	c_t2_t4_t3_in += MAS_in[0]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 41
	c_t2_t4_t3_mem0 += MAS_MEM[2]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 41
	c_t2_t4_t3_mem1 += MAS_MEM[5]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 41
	c_t3110_in += MAS_in[3]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 41
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 41
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t4100 = S.Task('c_t4100', length=4, delay_cost=1)
	S += c_t4100 >= 41
	c_t4100 += MAS[0]

	c_t0_t00 = S.Task('c_t0_t00', length=4, delay_cost=1)
	S += c_t0_t00 >= 42
	c_t0_t00 += MAS[2]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=11, delay_cost=1)
	S += c_t2_t4_t0 >= 42
	c_t2_t4_t0 += MM[0]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=4, delay_cost=1)
	S += c_t2_t4_t3 >= 42
	c_t2_t4_t3 += MAS[0]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 42
	c_t3010_in += MAS_in[3]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 42
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 42
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3110 = S.Task('c_t3110', length=4, delay_cost=1)
	S += c_t3110 >= 42
	c_t3110 += MAS[3]

	c_t3010 = S.Task('c_t3010', length=4, delay_cost=1)
	S += c_t3010 >= 43
	c_t3010 += MAS[3]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 43
	c_t3101_in += MAS_in[1]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 43
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 43
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 43
	c_t4_t1_t2_in += MAS_in[2]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 43
	c_t4_t1_t2_mem0 += MAS_MEM[2]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 43
	c_t4_t1_t2_mem1 += MAS_MEM[7]

	c_t3101 = S.Task('c_t3101', length=4, delay_cost=1)
	S += c_t3101 >= 44
	c_t3101 += MAS[1]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=4, delay_cost=1)
	S += c_t4_t1_t2 >= 44
	c_t4_t1_t2 += MAS[2]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 44
	c_t5100_in += MAS_in[2]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 44
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 44
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 45
	c_t3_t30_in += MAS_in[0]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 45
	c_t3_t30_mem0 += MAS_MEM[2]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 45
	c_t3_t30_mem1 += MAS_MEM[7]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 45
	c_t4101_in += MAS_in[3]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 45
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 45
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t5100 = S.Task('c_t5100', length=4, delay_cost=1)
	S += c_t5100 >= 45
	c_t5100 += MAS[2]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 46
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 46
	c_t3_t1_t0_mem0 += MAS_MEM[6]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 46
	c_t3_t1_t0_mem1 += MAS_MEM[7]

	c_t3_t30 = S.Task('c_t3_t30', length=4, delay_cost=1)
	S += c_t3_t30 >= 46
	c_t3_t30 += MAS[0]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 46
	c_t4000_in += MAS_in[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 46
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 46
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4101 = S.Task('c_t4101', length=4, delay_cost=1)
	S += c_t4101 >= 46
	c_t4101 += MAS[3]

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
	c_t3_t0_t1_mem0 += MAS_MEM[4]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 47
	c_t3_t0_t1_mem1 += MAS_MEM[3]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=11, delay_cost=1)
	S += c_t3_t1_t0 >= 47
	c_t3_t1_t0 += MM[0]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 47
	c_t3_t1_t2_in += MAS_in[2]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 47
	c_t3_t1_t2_mem0 += MAS_MEM[6]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 47
	c_t3_t1_t2_mem1 += MAS_MEM[5]

	c_t4000 = S.Task('c_t4000', length=4, delay_cost=1)
	S += c_t4000 >= 47
	c_t4000 += MAS[1]

	c_t3111 = S.Task('c_t3111', length=4, delay_cost=1)
	S += c_t3111 >= 48
	c_t3111 += MAS[1]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=11, delay_cost=1)
	S += c_t3_t0_t1 >= 48
	c_t3_t0_t1 += MM[0]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 48
	c_t3_t0_t3_in += MAS_in[2]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 48
	c_t3_t0_t3_mem0 += MAS_MEM[2]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 48
	c_t3_t0_t3_mem1 += MAS_MEM[3]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=4, delay_cost=1)
	S += c_t3_t1_t2 >= 48
	c_t3_t1_t2 += MAS[2]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 48
	c_t5101_in += MAS_in[1]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 48
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 48
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=4, delay_cost=1)
	S += c_t3_t0_t3 >= 49
	c_t3_t0_t3 += MAS[2]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 49
	c_t4111_in += MAS_in[3]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 49
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 49
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 49
	c_t4_t0_t3_in += MAS_in[1]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 49
	c_t4_t0_t3_mem0 += MAS_MEM[0]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 49
	c_t4_t0_t3_mem1 += MAS_MEM[7]

	c_t5101 = S.Task('c_t5101', length=4, delay_cost=1)
	S += c_t5101 >= 49
	c_t5101 += MAS[1]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 50
	c_t4110_in += MAS_in[3]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 50
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 50
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4111 = S.Task('c_t4111', length=4, delay_cost=1)
	S += c_t4111 >= 50
	c_t4111 += MAS[3]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 50
	c_t4_t0_t0_in += MM_in[0]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 50
	c_t4_t0_t0_mem0 += MAS_MEM[2]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 50
	c_t4_t0_t0_mem1 += MAS_MEM[1]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=4, delay_cost=1)
	S += c_t4_t0_t3 >= 50
	c_t4_t0_t3 += MAS[1]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 51
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 51
	c_t3_t1_t1_mem0 += MAS_MEM[4]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 51
	c_t3_t1_t1_mem1 += MAS_MEM[3]

	c_t4110 = S.Task('c_t4110', length=4, delay_cost=1)
	S += c_t4110 >= 51
	c_t4110 += MAS[3]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=11, delay_cost=1)
	S += c_t4_t0_t0 >= 51
	c_t4_t0_t0 += MM[0]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 51
	c_t5001_in += MAS_in[1]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 51
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 51
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=11, delay_cost=1)
	S += c_t3_t1_t1 >= 52
	c_t3_t1_t1 += MM[0]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 52
	c_t3_t1_t3_in += MAS_in[1]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 52
	c_t3_t1_t3_mem0 += MAS_MEM[6]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 52
	c_t3_t1_t3_mem1 += MAS_MEM[3]

	c_t5001 = S.Task('c_t5001', length=4, delay_cost=1)
	S += c_t5001 >= 52
	c_t5001 += MAS[1]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 52
	c_t5011_in += MAS_in[3]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 52
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 52
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=4, delay_cost=1)
	S += c_t3_t1_t3 >= 53
	c_t3_t1_t3 += MAS[1]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 53
	c_t3_t31_in += MAS_in[2]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 53
	c_t3_t31_mem0 += MAS_MEM[2]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 53
	c_t3_t31_mem1 += MAS_MEM[3]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 53
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 53
	c_t4_t1_t1_mem0 += MAS_MEM[6]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 53
	c_t4_t1_t1_mem1 += MAS_MEM[7]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 53
	c_t5000_in += MAS_in[1]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 53
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 53
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=4, delay_cost=1)
	S += c_t5011 >= 53
	c_t5011 += MAS[3]

	c_t3_t31 = S.Task('c_t3_t31', length=4, delay_cost=1)
	S += c_t3_t31 >= 54
	c_t3_t31 += MAS[2]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 54
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 54
	c_t4_t1_t0_mem0 += MAS_MEM[2]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 54
	c_t4_t1_t0_mem1 += MAS_MEM[7]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=11, delay_cost=1)
	S += c_t4_t1_t1 >= 54
	c_t4_t1_t1 += MM[0]

	c_t5000 = S.Task('c_t5000', length=4, delay_cost=1)
	S += c_t5000 >= 54
	c_t5000 += MAS[1]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 54
	c_t5010_in += MAS_in[2]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 54
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 54
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 54
	c_t5_t0_t3_in += MAS_in[0]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 54
	c_t5_t0_t3_mem0 += MAS_MEM[4]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 54
	c_t5_t0_t3_mem1 += MAS_MEM[3]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 55
	c_t4001_in += MAS_in[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 55
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 55
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=11, delay_cost=1)
	S += c_t4_t1_t0 >= 55
	c_t4_t1_t0 += MM[0]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 55
	c_t4_t1_t3_in += MAS_in[2]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 55
	c_t4_t1_t3_mem0 += MAS_MEM[6]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 55
	c_t4_t1_t3_mem1 += MAS_MEM[7]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 55
	c_t4_t20_in += MAS_in[3]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 55
	c_t4_t20_mem0 += MAS_MEM[2]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 55
	c_t4_t20_mem1 += MAS_MEM[3]

	c_t5010 = S.Task('c_t5010', length=4, delay_cost=1)
	S += c_t5010 >= 55
	c_t5010 += MAS[2]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=4, delay_cost=1)
	S += c_t5_t0_t3 >= 55
	c_t5_t0_t3 += MAS[0]

	c_t4001 = S.Task('c_t4001', length=4, delay_cost=1)
	S += c_t4001 >= 56
	c_t4001 += MAS[1]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=4, delay_cost=1)
	S += c_t4_t1_t3 >= 56
	c_t4_t1_t3 += MAS[2]

	c_t4_t20 = S.Task('c_t4_t20', length=4, delay_cost=1)
	S += c_t4_t20 >= 56
	c_t4_t20 += MAS[3]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 56
	c_t4_t31_in += MAS_in[1]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 56
	c_t4_t31_mem0 += MAS_MEM[6]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 56
	c_t4_t31_mem1 += MAS_MEM[7]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 56
	c_t5111_in += MAS_in[2]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 56
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 56
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 56
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 56
	c_t5_t0_t1_mem0 += MAS_MEM[2]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 56
	c_t5_t0_t1_mem1 += MAS_MEM[3]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 57
	c_t3000_in += MAS_in[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 57
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 57
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 57
	c_t4_t30_in += MAS_in[1]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 57
	c_t4_t30_mem0 += MAS_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 57
	c_t4_t30_mem1 += MAS_MEM[7]

	c_t4_t31 = S.Task('c_t4_t31', length=4, delay_cost=1)
	S += c_t4_t31 >= 57
	c_t4_t31 += MAS[1]

	c_t5111 = S.Task('c_t5111', length=4, delay_cost=1)
	S += c_t5111 >= 57
	c_t5111 += MAS[2]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 57
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 57
	c_t5_t0_t0_mem0 += MAS_MEM[2]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 57
	c_t5_t0_t0_mem1 += MAS_MEM[5]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=11, delay_cost=1)
	S += c_t5_t0_t1 >= 57
	c_t5_t0_t1 += MM[0]

	c_t3000 = S.Task('c_t3000', length=4, delay_cost=1)
	S += c_t3000 >= 58
	c_t3000 += MAS[3]

	c_t4_t30 = S.Task('c_t4_t30', length=4, delay_cost=1)
	S += c_t4_t30 >= 58
	c_t4_t30 += MAS[1]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 58
	c_t5110_in += MAS_in[3]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 58
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 58
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=11, delay_cost=1)
	S += c_t5_t0_t0 >= 58
	c_t5_t0_t0 += MM[0]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 58
	c_t5_t1_t2_in += MAS_in[0]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 58
	c_t5_t1_t2_mem0 += MAS_MEM[4]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 58
	c_t5_t1_t2_mem1 += MAS_MEM[7]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 58
	c_t5_t20_in += MAS_in[2]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 58
	c_t5_t20_mem0 += MAS_MEM[2]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 58
	c_t5_t20_mem1 += MAS_MEM[5]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 59
	c_t2_t1_t2_in += MAS_in[0]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 59
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 59
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 59
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 59
	c_t4_t0_t1_mem0 += MAS_MEM[2]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 59
	c_t4_t0_t1_mem1 += MAS_MEM[7]

	c_t5110 = S.Task('c_t5110', length=4, delay_cost=1)
	S += c_t5110 >= 59
	c_t5110 += MAS[3]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=4, delay_cost=1)
	S += c_t5_t1_t2 >= 59
	c_t5_t1_t2 += MAS[0]

	c_t5_t20 = S.Task('c_t5_t20', length=4, delay_cost=1)
	S += c_t5_t20 >= 59
	c_t5_t20 += MAS[2]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=4, delay_cost=1)
	S += c_t2_t1_t2 >= 60
	c_t2_t1_t2 += MAS[0]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=11, delay_cost=1)
	S += c_t4_t0_t1 >= 60
	c_t4_t0_t1 += MM[0]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 60
	c_t4_t0_t2_in += MAS_in[2]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 60
	c_t4_t0_t2_mem0 += MAS_MEM[2]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 60
	c_t4_t0_t2_mem1 += MAS_MEM[3]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 60
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 60
	c_t5_t1_t1_mem0 += MAS_MEM[6]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 60
	c_t5_t1_t1_mem1 += MAS_MEM[5]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 61
	c_t3_t0_t0_in += MM_in[0]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 61
	c_t3_t0_t0_mem0 += MAS_MEM[6]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 61
	c_t3_t0_t0_mem1 += MAS_MEM[3]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=4, delay_cost=1)
	S += c_t4_t0_t2 >= 61
	c_t4_t0_t2 += MAS[2]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 61
	c_t4_t21_in += MAS_in[3]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 61
	c_t4_t21_mem0 += MAS_MEM[2]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 61
	c_t4_t21_mem1 += MAS_MEM[7]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=11, delay_cost=1)
	S += c_t5_t1_t1 >= 61
	c_t5_t1_t1 += MM[0]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=11, delay_cost=1)
	S += c_t3_t0_t0 >= 62
	c_t3_t0_t0 += MM[0]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 62
	c_t3_t20_in += MAS_in[2]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 62
	c_t3_t20_mem0 += MAS_MEM[6]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 62
	c_t3_t20_mem1 += MAS_MEM[7]

	c_t4_t21 = S.Task('c_t4_t21', length=4, delay_cost=1)
	S += c_t4_t21 >= 62
	c_t4_t21 += MAS[3]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 62
	c_t5_t31_in += MAS_in[3]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 62
	c_t5_t31_mem0 += MAS_MEM[2]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 62
	c_t5_t31_mem1 += MAS_MEM[5]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 63
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 63
	c_t2_t1_t4_mem0 += MAS_MEM[0]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 63
	c_t2_t1_t4_mem1 += MAS_MEM[7]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 63
	c_t3_t0_t2_in += MAS_in[0]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 63
	c_t3_t0_t2_mem0 += MAS_MEM[6]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 63
	c_t3_t0_t2_mem1 += MAS_MEM[5]

	c_t3_t20 = S.Task('c_t3_t20', length=4, delay_cost=1)
	S += c_t3_t20 >= 63
	c_t3_t20 += MAS[2]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 63
	c_t5_t0_t2_in += MAS_in[3]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 63
	c_t5_t0_t2_mem0 += MAS_MEM[2]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 63
	c_t5_t0_t2_mem1 += MAS_MEM[3]

	c_t5_t31 = S.Task('c_t5_t31', length=4, delay_cost=1)
	S += c_t5_t31 >= 63
	c_t5_t31 += MAS[3]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=11, delay_cost=1)
	S += c_t2_t1_t4 >= 64
	c_t2_t1_t4 += MM[0]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=4, delay_cost=1)
	S += c_t3_t0_t2 >= 64
	c_t3_t0_t2 += MAS[0]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=4, delay_cost=1)
	S += c_t5_t0_t2 >= 64
	c_t5_t0_t2 += MAS[3]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 64
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 64
	c_t5_t1_t0_mem0 += MAS_MEM[4]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 64
	c_t5_t1_t0_mem1 += MAS_MEM[7]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 64
	c_t5_t1_t3_in += MAS_in[2]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 64
	c_t5_t1_t3_mem0 += MAS_MEM[6]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 64
	c_t5_t1_t3_mem1 += MAS_MEM[5]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=11, delay_cost=1)
	S += c_t5_t1_t0 >= 65
	c_t5_t1_t0 += MM[0]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=4, delay_cost=1)
	S += c_t5_t1_t3 >= 65
	c_t5_t1_t3 += MAS[2]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 65
	c_t5_t30_in += MAS_in[2]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 65
	c_t5_t30_mem0 += MAS_MEM[4]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 65
	c_t5_t30_mem1 += MAS_MEM[7]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 66
	c_t5_t21_in += MAS_in[3]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 66
	c_t5_t21_mem0 += MAS_MEM[2]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 66
	c_t5_t21_mem1 += MAS_MEM[7]

	c_t5_t30 = S.Task('c_t5_t30', length=4, delay_cost=1)
	S += c_t5_t30 >= 66
	c_t5_t30 += MAS[2]

	c_t5_t21 = S.Task('c_t5_t21', length=4, delay_cost=1)
	S += c_t5_t21 >= 67
	c_t5_t21 += MAS[3]


	# new tasks
	c_t0_t01 = S.Task('c_t0_t01', length=4, delay_cost=1)
	c_t0_t01 += alt(MAS)
	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	c_t0_t01_in += alt(MAS_in)
	S += c_t0_t01_in*MAS_in[0]<=c_t0_t01*MAS[0]

	S += c_t0_t01_in*MAS_in[1]<=c_t0_t01*MAS[1]

	S += c_t0_t01_in*MAS_in[2]<=c_t0_t01*MAS[2]

	S += c_t0_t01_in*MAS_in[3]<=c_t0_t01*MAS[3]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	c_t0_t01_mem0 += MM_MEM[0]
	S += 41 < c_t0_t01_mem0
	S += c_t0_t01_mem0 <= c_t0_t01

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	c_t0_t01_mem1 += MAS_MEM[7]
	S += 44 < c_t0_t01_mem1
	S += c_t0_t01_mem1 <= c_t0_t01

	c_t0_t11 = S.Task('c_t0_t11', length=4, delay_cost=1)
	c_t0_t11 += alt(MAS)
	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	c_t0_t11_in += alt(MAS_in)
	S += c_t0_t11_in*MAS_in[0]<=c_t0_t11*MAS[0]

	S += c_t0_t11_in*MAS_in[1]<=c_t0_t11*MAS[1]

	S += c_t0_t11_in*MAS_in[2]<=c_t0_t11*MAS[2]

	S += c_t0_t11_in*MAS_in[3]<=c_t0_t11*MAS[3]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	c_t0_t11_mem0 += MM_MEM[0]
	S += 23 < c_t0_t11_mem0
	S += c_t0_t11_mem0 <= c_t0_t11

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	c_t0_t11_mem1 += MAS_MEM[1]
	S += 42 < c_t0_t11_mem1
	S += c_t0_t11_mem1 <= c_t0_t11

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=11, delay_cost=1)
	c_t0_t4_t4 += alt(MM)
	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	c_t0_t4_t4_in += alt(MM_in)
	S += c_t0_t4_t4_in*MM_in[0]<=c_t0_t4_t4*MM[0]
	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	c_t0_t4_t4_mem0 += MAS_MEM[4]
	S += 30 < c_t0_t4_t4_mem0
	S += c_t0_t4_t4_mem0 <= c_t0_t4_t4

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	c_t0_t4_t4_mem1 += MAS_MEM[3]
	S += 13 < c_t0_t4_t4_mem1
	S += c_t0_t4_t4_mem1 <= c_t0_t4_t4

	c_t0_t40 = S.Task('c_t0_t40', length=4, delay_cost=1)
	c_t0_t40 += alt(MAS)
	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	c_t0_t40_in += alt(MAS_in)
	S += c_t0_t40_in*MAS_in[0]<=c_t0_t40*MAS[0]

	S += c_t0_t40_in*MAS_in[1]<=c_t0_t40*MAS[1]

	S += c_t0_t40_in*MAS_in[2]<=c_t0_t40*MAS[2]

	S += c_t0_t40_in*MAS_in[3]<=c_t0_t40*MAS[3]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	c_t0_t40_mem0 += MM_MEM[0]
	S += 34 < c_t0_t40_mem0
	S += c_t0_t40_mem0 <= c_t0_t40

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	c_t0_t40_mem1 += MM_MEM[1]
	S += 43 < c_t0_t40_mem1
	S += c_t0_t40_mem1 <= c_t0_t40

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=4, delay_cost=1)
	c_t0_t4_t5 += alt(MAS)
	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	c_t0_t4_t5_in += alt(MAS_in)
	S += c_t0_t4_t5_in*MAS_in[0]<=c_t0_t4_t5*MAS[0]

	S += c_t0_t4_t5_in*MAS_in[1]<=c_t0_t4_t5*MAS[1]

	S += c_t0_t4_t5_in*MAS_in[2]<=c_t0_t4_t5*MAS[2]

	S += c_t0_t4_t5_in*MAS_in[3]<=c_t0_t4_t5*MAS[3]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	c_t0_t4_t5_mem0 += MM_MEM[0]
	S += 34 < c_t0_t4_t5_mem0
	S += c_t0_t4_t5_mem0 <= c_t0_t4_t5

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	c_t0_t4_t5_mem1 += MM_MEM[1]
	S += 43 < c_t0_t4_t5_mem1
	S += c_t0_t4_t5_mem1 <= c_t0_t4_t5

	c_t0_t50 = S.Task('c_t0_t50', length=4, delay_cost=1)
	c_t0_t50 += alt(MAS)
	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	c_t0_t50_in += alt(MAS_in)
	S += c_t0_t50_in*MAS_in[0]<=c_t0_t50*MAS[0]

	S += c_t0_t50_in*MAS_in[1]<=c_t0_t50*MAS[1]

	S += c_t0_t50_in*MAS_in[2]<=c_t0_t50*MAS[2]

	S += c_t0_t50_in*MAS_in[3]<=c_t0_t50*MAS[3]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	c_t0_t50_mem0 += MAS_MEM[4]
	S += 45 < c_t0_t50_mem0
	S += c_t0_t50_mem0 <= c_t0_t50

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	c_t0_t50_mem1 += MAS_MEM[3]
	S += 43 < c_t0_t50_mem1
	S += c_t0_t50_mem1 <= c_t0_t50

	c_t1_t01 = S.Task('c_t1_t01', length=4, delay_cost=1)
	c_t1_t01 += alt(MAS)
	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	c_t1_t01_in += alt(MAS_in)
	S += c_t1_t01_in*MAS_in[0]<=c_t1_t01*MAS[0]

	S += c_t1_t01_in*MAS_in[1]<=c_t1_t01*MAS[1]

	S += c_t1_t01_in*MAS_in[2]<=c_t1_t01*MAS[2]

	S += c_t1_t01_in*MAS_in[3]<=c_t1_t01*MAS[3]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	c_t1_t01_mem0 += MM_MEM[0]
	S += 44 < c_t1_t01_mem0
	S += c_t1_t01_mem0 <= c_t1_t01

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	c_t1_t01_mem1 += MAS_MEM[1]
	S += 23 < c_t1_t01_mem1
	S += c_t1_t01_mem1 <= c_t1_t01

	c_t1_t11 = S.Task('c_t1_t11', length=4, delay_cost=1)
	c_t1_t11 += alt(MAS)
	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	c_t1_t11_in += alt(MAS_in)
	S += c_t1_t11_in*MAS_in[0]<=c_t1_t11*MAS[0]

	S += c_t1_t11_in*MAS_in[1]<=c_t1_t11*MAS[1]

	S += c_t1_t11_in*MAS_in[2]<=c_t1_t11*MAS[2]

	S += c_t1_t11_in*MAS_in[3]<=c_t1_t11*MAS[3]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	c_t1_t11_mem0 += MM_MEM[0]
	S += 30 < c_t1_t11_mem0
	S += c_t1_t11_mem0 <= c_t1_t11

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	c_t1_t11_mem1 += MAS_MEM[1]
	S += 35 < c_t1_t11_mem1
	S += c_t1_t11_mem1 <= c_t1_t11

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=11, delay_cost=1)
	c_t1_t4_t4 += alt(MM)
	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	c_t1_t4_t4_in += alt(MM_in)
	S += c_t1_t4_t4_in*MM_in[0]<=c_t1_t4_t4*MM[0]
	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	c_t1_t4_t4_mem0 += MAS_MEM[6]
	S += 29 < c_t1_t4_t4_mem0
	S += c_t1_t4_t4_mem0 <= c_t1_t4_t4

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	c_t1_t4_t4_mem1 += MAS_MEM[3]
	S += 9 < c_t1_t4_t4_mem1
	S += c_t1_t4_t4_mem1 <= c_t1_t4_t4

	c_t1_t40 = S.Task('c_t1_t40', length=4, delay_cost=1)
	c_t1_t40 += alt(MAS)
	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	c_t1_t40_in += alt(MAS_in)
	S += c_t1_t40_in*MAS_in[0]<=c_t1_t40*MAS[0]

	S += c_t1_t40_in*MAS_in[1]<=c_t1_t40*MAS[1]

	S += c_t1_t40_in*MAS_in[2]<=c_t1_t40*MAS[2]

	S += c_t1_t40_in*MAS_in[3]<=c_t1_t40*MAS[3]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	c_t1_t40_mem0 += MM_MEM[0]
	S += 27 < c_t1_t40_mem0
	S += c_t1_t40_mem0 <= c_t1_t40

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	c_t1_t40_mem1 += MM_MEM[1]
	S += 36 < c_t1_t40_mem1
	S += c_t1_t40_mem1 <= c_t1_t40

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=4, delay_cost=1)
	c_t1_t4_t5 += alt(MAS)
	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	c_t1_t4_t5_in += alt(MAS_in)
	S += c_t1_t4_t5_in*MAS_in[0]<=c_t1_t4_t5*MAS[0]

	S += c_t1_t4_t5_in*MAS_in[1]<=c_t1_t4_t5*MAS[1]

	S += c_t1_t4_t5_in*MAS_in[2]<=c_t1_t4_t5*MAS[2]

	S += c_t1_t4_t5_in*MAS_in[3]<=c_t1_t4_t5*MAS[3]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	c_t1_t4_t5_mem0 += MM_MEM[0]
	S += 27 < c_t1_t4_t5_mem0
	S += c_t1_t4_t5_mem0 <= c_t1_t4_t5

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	c_t1_t4_t5_mem1 += MM_MEM[1]
	S += 36 < c_t1_t4_t5_mem1
	S += c_t1_t4_t5_mem1 <= c_t1_t4_t5

	c_t1_t50 = S.Task('c_t1_t50', length=4, delay_cost=1)
	c_t1_t50 += alt(MAS)
	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	c_t1_t50_in += alt(MAS_in)
	S += c_t1_t50_in*MAS_in[0]<=c_t1_t50*MAS[0]

	S += c_t1_t50_in*MAS_in[1]<=c_t1_t50*MAS[1]

	S += c_t1_t50_in*MAS_in[2]<=c_t1_t50*MAS[2]

	S += c_t1_t50_in*MAS_in[3]<=c_t1_t50*MAS[3]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	c_t1_t50_mem0 += MAS_MEM[2]
	S += 24 < c_t1_t50_mem0
	S += c_t1_t50_mem0 <= c_t1_t50

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	c_t1_t50_mem1 += MAS_MEM[3]
	S += 36 < c_t1_t50_mem1
	S += c_t1_t50_mem1 <= c_t1_t50

	c_t2_t01 = S.Task('c_t2_t01', length=4, delay_cost=1)
	c_t2_t01 += alt(MAS)
	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	c_t2_t01_in += alt(MAS_in)
	S += c_t2_t01_in*MAS_in[0]<=c_t2_t01*MAS[0]

	S += c_t2_t01_in*MAS_in[1]<=c_t2_t01*MAS[1]

	S += c_t2_t01_in*MAS_in[2]<=c_t2_t01*MAS[2]

	S += c_t2_t01_in*MAS_in[3]<=c_t2_t01*MAS[3]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	c_t2_t01_mem0 += MM_MEM[0]
	S += 42 < c_t2_t01_mem0
	S += c_t2_t01_mem0 <= c_t2_t01

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	c_t2_t01_mem1 += MAS_MEM[3]
	S += 33 < c_t2_t01_mem1
	S += c_t2_t01_mem1 <= c_t2_t01

	c_t2_t11 = S.Task('c_t2_t11', length=4, delay_cost=1)
	c_t2_t11 += alt(MAS)
	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	c_t2_t11_in += alt(MAS_in)
	S += c_t2_t11_in*MAS_in[0]<=c_t2_t11*MAS[0]

	S += c_t2_t11_in*MAS_in[1]<=c_t2_t11*MAS[1]

	S += c_t2_t11_in*MAS_in[2]<=c_t2_t11*MAS[2]

	S += c_t2_t11_in*MAS_in[3]<=c_t2_t11*MAS[3]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	c_t2_t11_mem0 += MM_MEM[0]
	S += 74 < c_t2_t11_mem0
	S += c_t2_t11_mem0 <= c_t2_t11

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	c_t2_t11_mem1 += MAS_MEM[5]
	S += 27 < c_t2_t11_mem1
	S += c_t2_t11_mem1 <= c_t2_t11

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=11, delay_cost=1)
	c_t2_t4_t4 += alt(MM)
	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	c_t2_t4_t4_in += alt(MM_in)
	S += c_t2_t4_t4_in*MM_in[0]<=c_t2_t4_t4*MM[0]
	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	c_t2_t4_t4_mem0 += MAS_MEM[0]
	S += 40 < c_t2_t4_t4_mem0
	S += c_t2_t4_t4_mem0 <= c_t2_t4_t4

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	c_t2_t4_t4_mem1 += MAS_MEM[1]
	S += 45 < c_t2_t4_t4_mem1
	S += c_t2_t4_t4_mem1 <= c_t2_t4_t4

	c_t2_t40 = S.Task('c_t2_t40', length=4, delay_cost=1)
	c_t2_t40 += alt(MAS)
	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	c_t2_t40_in += alt(MAS_in)
	S += c_t2_t40_in*MAS_in[0]<=c_t2_t40*MAS[0]

	S += c_t2_t40_in*MAS_in[1]<=c_t2_t40*MAS[1]

	S += c_t2_t40_in*MAS_in[2]<=c_t2_t40*MAS[2]

	S += c_t2_t40_in*MAS_in[3]<=c_t2_t40*MAS[3]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	c_t2_t40_mem0 += MM_MEM[0]
	S += 52 < c_t2_t40_mem0
	S += c_t2_t40_mem0 <= c_t2_t40

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	c_t2_t40_mem1 += MM_MEM[1]
	S += 46 < c_t2_t40_mem1
	S += c_t2_t40_mem1 <= c_t2_t40

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=4, delay_cost=1)
	c_t2_t4_t5 += alt(MAS)
	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	c_t2_t4_t5_in += alt(MAS_in)
	S += c_t2_t4_t5_in*MAS_in[0]<=c_t2_t4_t5*MAS[0]

	S += c_t2_t4_t5_in*MAS_in[1]<=c_t2_t4_t5*MAS[1]

	S += c_t2_t4_t5_in*MAS_in[2]<=c_t2_t4_t5*MAS[2]

	S += c_t2_t4_t5_in*MAS_in[3]<=c_t2_t4_t5*MAS[3]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	c_t2_t4_t5_mem0 += MM_MEM[0]
	S += 52 < c_t2_t4_t5_mem0
	S += c_t2_t4_t5_mem0 <= c_t2_t4_t5

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	c_t2_t4_t5_mem1 += MM_MEM[1]
	S += 46 < c_t2_t4_t5_mem1
	S += c_t2_t4_t5_mem1 <= c_t2_t4_t5

	c_t2_t50 = S.Task('c_t2_t50', length=4, delay_cost=1)
	c_t2_t50 += alt(MAS)
	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	c_t2_t50_in += alt(MAS_in)
	S += c_t2_t50_in*MAS_in[0]<=c_t2_t50*MAS[0]

	S += c_t2_t50_in*MAS_in[1]<=c_t2_t50*MAS[1]

	S += c_t2_t50_in*MAS_in[2]<=c_t2_t50*MAS[2]

	S += c_t2_t50_in*MAS_in[3]<=c_t2_t50*MAS[3]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	c_t2_t50_mem0 += MAS_MEM[4]
	S += 34 < c_t2_t50_mem0
	S += c_t2_t50_mem0 <= c_t2_t50

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	c_t2_t50_mem1 += MAS_MEM[1]
	S += 26 < c_t2_t50_mem1
	S += c_t2_t50_mem1 <= c_t2_t50

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=11, delay_cost=1)
	c_t3_t0_t4 += alt(MM)
	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	c_t3_t0_t4_in += alt(MM_in)
	S += c_t3_t0_t4_in*MM_in[0]<=c_t3_t0_t4*MM[0]
	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	c_t3_t0_t4_mem0 += MAS_MEM[0]
	S += 67 < c_t3_t0_t4_mem0
	S += c_t3_t0_t4_mem0 <= c_t3_t0_t4

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	c_t3_t0_t4_mem1 += MAS_MEM[5]
	S += 52 < c_t3_t0_t4_mem1
	S += c_t3_t0_t4_mem1 <= c_t3_t0_t4

	c_t3_t00 = S.Task('c_t3_t00', length=4, delay_cost=1)
	c_t3_t00 += alt(MAS)
	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	c_t3_t00_in += alt(MAS_in)
	S += c_t3_t00_in*MAS_in[0]<=c_t3_t00*MAS[0]

	S += c_t3_t00_in*MAS_in[1]<=c_t3_t00*MAS[1]

	S += c_t3_t00_in*MAS_in[2]<=c_t3_t00*MAS[2]

	S += c_t3_t00_in*MAS_in[3]<=c_t3_t00*MAS[3]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	c_t3_t00_mem0 += MM_MEM[0]
	S += 72 < c_t3_t00_mem0
	S += c_t3_t00_mem0 <= c_t3_t00

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	c_t3_t00_mem1 += MM_MEM[1]
	S += 58 < c_t3_t00_mem1
	S += c_t3_t00_mem1 <= c_t3_t00

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=4, delay_cost=1)
	c_t3_t0_t5 += alt(MAS)
	c_t3_t0_t5_in = S.Task('c_t3_t0_t5_in', length=1, delay_cost=1)
	c_t3_t0_t5_in += alt(MAS_in)
	S += c_t3_t0_t5_in*MAS_in[0]<=c_t3_t0_t5*MAS[0]

	S += c_t3_t0_t5_in*MAS_in[1]<=c_t3_t0_t5*MAS[1]

	S += c_t3_t0_t5_in*MAS_in[2]<=c_t3_t0_t5*MAS[2]

	S += c_t3_t0_t5_in*MAS_in[3]<=c_t3_t0_t5*MAS[3]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	c_t3_t0_t5_mem0 += MM_MEM[0]
	S += 72 < c_t3_t0_t5_mem0
	S += c_t3_t0_t5_mem0 <= c_t3_t0_t5

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	c_t3_t0_t5_mem1 += MM_MEM[1]
	S += 58 < c_t3_t0_t5_mem1
	S += c_t3_t0_t5_mem1 <= c_t3_t0_t5

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=11, delay_cost=1)
	c_t3_t1_t4 += alt(MM)
	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	c_t3_t1_t4_in += alt(MM_in)
	S += c_t3_t1_t4_in*MM_in[0]<=c_t3_t1_t4*MM[0]
	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	c_t3_t1_t4_mem0 += MAS_MEM[4]
	S += 51 < c_t3_t1_t4_mem0
	S += c_t3_t1_t4_mem0 <= c_t3_t1_t4

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	c_t3_t1_t4_mem1 += MAS_MEM[3]
	S += 56 < c_t3_t1_t4_mem1
	S += c_t3_t1_t4_mem1 <= c_t3_t1_t4

	c_t3_t10 = S.Task('c_t3_t10', length=4, delay_cost=1)
	c_t3_t10 += alt(MAS)
	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	c_t3_t10_in += alt(MAS_in)
	S += c_t3_t10_in*MAS_in[0]<=c_t3_t10*MAS[0]

	S += c_t3_t10_in*MAS_in[1]<=c_t3_t10*MAS[1]

	S += c_t3_t10_in*MAS_in[2]<=c_t3_t10*MAS[2]

	S += c_t3_t10_in*MAS_in[3]<=c_t3_t10*MAS[3]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	c_t3_t10_mem0 += MM_MEM[0]
	S += 57 < c_t3_t10_mem0
	S += c_t3_t10_mem0 <= c_t3_t10

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	c_t3_t10_mem1 += MM_MEM[1]
	S += 62 < c_t3_t10_mem1
	S += c_t3_t10_mem1 <= c_t3_t10

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=4, delay_cost=1)
	c_t3_t1_t5 += alt(MAS)
	c_t3_t1_t5_in = S.Task('c_t3_t1_t5_in', length=1, delay_cost=1)
	c_t3_t1_t5_in += alt(MAS_in)
	S += c_t3_t1_t5_in*MAS_in[0]<=c_t3_t1_t5*MAS[0]

	S += c_t3_t1_t5_in*MAS_in[1]<=c_t3_t1_t5*MAS[1]

	S += c_t3_t1_t5_in*MAS_in[2]<=c_t3_t1_t5*MAS[2]

	S += c_t3_t1_t5_in*MAS_in[3]<=c_t3_t1_t5*MAS[3]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	c_t3_t1_t5_mem0 += MM_MEM[0]
	S += 57 < c_t3_t1_t5_mem0
	S += c_t3_t1_t5_mem0 <= c_t3_t1_t5

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	c_t3_t1_t5_mem1 += MM_MEM[1]
	S += 62 < c_t3_t1_t5_mem1
	S += c_t3_t1_t5_mem1 <= c_t3_t1_t5

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=11, delay_cost=1)
	c_t3_t4_t0 += alt(MM)
	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	c_t3_t4_t0_in += alt(MM_in)
	S += c_t3_t4_t0_in*MM_in[0]<=c_t3_t4_t0*MM[0]
	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	c_t3_t4_t0_mem0 += MAS_MEM[4]
	S += 66 < c_t3_t4_t0_mem0
	S += c_t3_t4_t0_mem0 <= c_t3_t4_t0

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	c_t3_t4_t0_mem1 += MAS_MEM[1]
	S += 49 < c_t3_t4_t0_mem1
	S += c_t3_t4_t0_mem1 <= c_t3_t4_t0

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=11, delay_cost=1)
	c_t3_t4_t1 += alt(MM)
	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	c_t3_t4_t1_in += alt(MM_in)
	S += c_t3_t4_t1_in*MM_in[0]<=c_t3_t4_t1*MM[0]
	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	c_t3_t4_t1_mem0 += MAS_MEM[0]
	S += 43 < c_t3_t4_t1_mem0
	S += c_t3_t4_t1_mem0 <= c_t3_t4_t1

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	c_t3_t4_t1_mem1 += MAS_MEM[5]
	S += 57 < c_t3_t4_t1_mem1
	S += c_t3_t4_t1_mem1 <= c_t3_t4_t1

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=4, delay_cost=1)
	c_t3_t4_t2 += alt(MAS)
	c_t3_t4_t2_in = S.Task('c_t3_t4_t2_in', length=1, delay_cost=1)
	c_t3_t4_t2_in += alt(MAS_in)
	S += c_t3_t4_t2_in*MAS_in[0]<=c_t3_t4_t2*MAS[0]

	S += c_t3_t4_t2_in*MAS_in[1]<=c_t3_t4_t2*MAS[1]

	S += c_t3_t4_t2_in*MAS_in[2]<=c_t3_t4_t2*MAS[2]

	S += c_t3_t4_t2_in*MAS_in[3]<=c_t3_t4_t2*MAS[3]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	c_t3_t4_t2_mem0 += MAS_MEM[4]
	S += 66 < c_t3_t4_t2_mem0
	S += c_t3_t4_t2_mem0 <= c_t3_t4_t2

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	c_t3_t4_t2_mem1 += MAS_MEM[1]
	S += 43 < c_t3_t4_t2_mem1
	S += c_t3_t4_t2_mem1 <= c_t3_t4_t2

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=4, delay_cost=1)
	c_t3_t4_t3 += alt(MAS)
	c_t3_t4_t3_in = S.Task('c_t3_t4_t3_in', length=1, delay_cost=1)
	c_t3_t4_t3_in += alt(MAS_in)
	S += c_t3_t4_t3_in*MAS_in[0]<=c_t3_t4_t3*MAS[0]

	S += c_t3_t4_t3_in*MAS_in[1]<=c_t3_t4_t3*MAS[1]

	S += c_t3_t4_t3_in*MAS_in[2]<=c_t3_t4_t3*MAS[2]

	S += c_t3_t4_t3_in*MAS_in[3]<=c_t3_t4_t3*MAS[3]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	c_t3_t4_t3_mem0 += MAS_MEM[0]
	S += 49 < c_t3_t4_t3_mem0
	S += c_t3_t4_t3_mem0 <= c_t3_t4_t3

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	c_t3_t4_t3_mem1 += MAS_MEM[5]
	S += 57 < c_t3_t4_t3_mem1
	S += c_t3_t4_t3_mem1 <= c_t3_t4_t3

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=11, delay_cost=1)
	c_t4_t0_t4 += alt(MM)
	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	c_t4_t0_t4_in += alt(MM_in)
	S += c_t4_t0_t4_in*MM_in[0]<=c_t4_t0_t4*MM[0]
	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	c_t4_t0_t4_mem0 += MAS_MEM[4]
	S += 64 < c_t4_t0_t4_mem0
	S += c_t4_t0_t4_mem0 <= c_t4_t0_t4

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	c_t4_t0_t4_mem1 += MAS_MEM[3]
	S += 53 < c_t4_t0_t4_mem1
	S += c_t4_t0_t4_mem1 <= c_t4_t0_t4

	c_t4_t00 = S.Task('c_t4_t00', length=4, delay_cost=1)
	c_t4_t00 += alt(MAS)
	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	c_t4_t00_in += alt(MAS_in)
	S += c_t4_t00_in*MAS_in[0]<=c_t4_t00*MAS[0]

	S += c_t4_t00_in*MAS_in[1]<=c_t4_t00*MAS[1]

	S += c_t4_t00_in*MAS_in[2]<=c_t4_t00*MAS[2]

	S += c_t4_t00_in*MAS_in[3]<=c_t4_t00*MAS[3]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	c_t4_t00_mem0 += MM_MEM[0]
	S += 61 < c_t4_t00_mem0
	S += c_t4_t00_mem0 <= c_t4_t00

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	c_t4_t00_mem1 += MM_MEM[1]
	S += 70 < c_t4_t00_mem1
	S += c_t4_t00_mem1 <= c_t4_t00

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=4, delay_cost=1)
	c_t4_t0_t5 += alt(MAS)
	c_t4_t0_t5_in = S.Task('c_t4_t0_t5_in', length=1, delay_cost=1)
	c_t4_t0_t5_in += alt(MAS_in)
	S += c_t4_t0_t5_in*MAS_in[0]<=c_t4_t0_t5*MAS[0]

	S += c_t4_t0_t5_in*MAS_in[1]<=c_t4_t0_t5*MAS[1]

	S += c_t4_t0_t5_in*MAS_in[2]<=c_t4_t0_t5*MAS[2]

	S += c_t4_t0_t5_in*MAS_in[3]<=c_t4_t0_t5*MAS[3]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	c_t4_t0_t5_mem0 += MM_MEM[0]
	S += 61 < c_t4_t0_t5_mem0
	S += c_t4_t0_t5_mem0 <= c_t4_t0_t5

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	c_t4_t0_t5_mem1 += MM_MEM[1]
	S += 70 < c_t4_t0_t5_mem1
	S += c_t4_t0_t5_mem1 <= c_t4_t0_t5

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=11, delay_cost=1)
	c_t4_t1_t4 += alt(MM)
	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	c_t4_t1_t4_in += alt(MM_in)
	S += c_t4_t1_t4_in*MM_in[0]<=c_t4_t1_t4*MM[0]
	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	c_t4_t1_t4_mem0 += MAS_MEM[4]
	S += 47 < c_t4_t1_t4_mem0
	S += c_t4_t1_t4_mem0 <= c_t4_t1_t4

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	c_t4_t1_t4_mem1 += MAS_MEM[5]
	S += 59 < c_t4_t1_t4_mem1
	S += c_t4_t1_t4_mem1 <= c_t4_t1_t4

	c_t4_t10 = S.Task('c_t4_t10', length=4, delay_cost=1)
	c_t4_t10 += alt(MAS)
	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	c_t4_t10_in += alt(MAS_in)
	S += c_t4_t10_in*MAS_in[0]<=c_t4_t10*MAS[0]

	S += c_t4_t10_in*MAS_in[1]<=c_t4_t10*MAS[1]

	S += c_t4_t10_in*MAS_in[2]<=c_t4_t10*MAS[2]

	S += c_t4_t10_in*MAS_in[3]<=c_t4_t10*MAS[3]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	c_t4_t10_mem0 += MM_MEM[0]
	S += 65 < c_t4_t10_mem0
	S += c_t4_t10_mem0 <= c_t4_t10

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	c_t4_t10_mem1 += MM_MEM[1]
	S += 64 < c_t4_t10_mem1
	S += c_t4_t10_mem1 <= c_t4_t10

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=4, delay_cost=1)
	c_t4_t1_t5 += alt(MAS)
	c_t4_t1_t5_in = S.Task('c_t4_t1_t5_in', length=1, delay_cost=1)
	c_t4_t1_t5_in += alt(MAS_in)
	S += c_t4_t1_t5_in*MAS_in[0]<=c_t4_t1_t5*MAS[0]

	S += c_t4_t1_t5_in*MAS_in[1]<=c_t4_t1_t5*MAS[1]

	S += c_t4_t1_t5_in*MAS_in[2]<=c_t4_t1_t5*MAS[2]

	S += c_t4_t1_t5_in*MAS_in[3]<=c_t4_t1_t5*MAS[3]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	c_t4_t1_t5_mem0 += MM_MEM[0]
	S += 65 < c_t4_t1_t5_mem0
	S += c_t4_t1_t5_mem0 <= c_t4_t1_t5

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	c_t4_t1_t5_mem1 += MM_MEM[1]
	S += 64 < c_t4_t1_t5_mem1
	S += c_t4_t1_t5_mem1 <= c_t4_t1_t5

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=11, delay_cost=1)
	c_t4_t4_t0 += alt(MM)
	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	c_t4_t4_t0_in += alt(MM_in)
	S += c_t4_t4_t0_in*MM_in[0]<=c_t4_t4_t0*MM[0]
	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	c_t4_t4_t0_mem0 += MAS_MEM[6]
	S += 59 < c_t4_t4_t0_mem0
	S += c_t4_t4_t0_mem0 <= c_t4_t4_t0

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	c_t4_t4_t0_mem1 += MAS_MEM[3]
	S += 61 < c_t4_t4_t0_mem1
	S += c_t4_t4_t0_mem1 <= c_t4_t4_t0

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=11, delay_cost=1)
	c_t4_t4_t1 += alt(MM)
	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	c_t4_t4_t1_in += alt(MM_in)
	S += c_t4_t4_t1_in*MM_in[0]<=c_t4_t4_t1*MM[0]
	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	c_t4_t4_t1_mem0 += MAS_MEM[6]
	S += 65 < c_t4_t4_t1_mem0
	S += c_t4_t4_t1_mem0 <= c_t4_t4_t1

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	c_t4_t4_t1_mem1 += MAS_MEM[3]
	S += 60 < c_t4_t4_t1_mem1
	S += c_t4_t4_t1_mem1 <= c_t4_t4_t1

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=4, delay_cost=1)
	c_t4_t4_t2 += alt(MAS)
	c_t4_t4_t2_in = S.Task('c_t4_t4_t2_in', length=1, delay_cost=1)
	c_t4_t4_t2_in += alt(MAS_in)
	S += c_t4_t4_t2_in*MAS_in[0]<=c_t4_t4_t2*MAS[0]

	S += c_t4_t4_t2_in*MAS_in[1]<=c_t4_t4_t2*MAS[1]

	S += c_t4_t4_t2_in*MAS_in[2]<=c_t4_t4_t2*MAS[2]

	S += c_t4_t4_t2_in*MAS_in[3]<=c_t4_t4_t2*MAS[3]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	c_t4_t4_t2_mem0 += MAS_MEM[6]
	S += 59 < c_t4_t4_t2_mem0
	S += c_t4_t4_t2_mem0 <= c_t4_t4_t2

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	c_t4_t4_t2_mem1 += MAS_MEM[7]
	S += 65 < c_t4_t4_t2_mem1
	S += c_t4_t4_t2_mem1 <= c_t4_t4_t2

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=4, delay_cost=1)
	c_t4_t4_t3 += alt(MAS)
	c_t4_t4_t3_in = S.Task('c_t4_t4_t3_in', length=1, delay_cost=1)
	c_t4_t4_t3_in += alt(MAS_in)
	S += c_t4_t4_t3_in*MAS_in[0]<=c_t4_t4_t3*MAS[0]

	S += c_t4_t4_t3_in*MAS_in[1]<=c_t4_t4_t3*MAS[1]

	S += c_t4_t4_t3_in*MAS_in[2]<=c_t4_t4_t3*MAS[2]

	S += c_t4_t4_t3_in*MAS_in[3]<=c_t4_t4_t3*MAS[3]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	c_t4_t4_t3_mem0 += MAS_MEM[2]
	S += 61 < c_t4_t4_t3_mem0
	S += c_t4_t4_t3_mem0 <= c_t4_t4_t3

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	c_t4_t4_t3_mem1 += MAS_MEM[3]
	S += 60 < c_t4_t4_t3_mem1
	S += c_t4_t4_t3_mem1 <= c_t4_t4_t3

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=11, delay_cost=1)
	c_t5_t0_t4 += alt(MM)
	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	c_t5_t0_t4_in += alt(MM_in)
	S += c_t5_t0_t4_in*MM_in[0]<=c_t5_t0_t4*MM[0]
	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	c_t5_t0_t4_mem0 += MAS_MEM[6]
	S += 67 < c_t5_t0_t4_mem0
	S += c_t5_t0_t4_mem0 <= c_t5_t0_t4

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	c_t5_t0_t4_mem1 += MAS_MEM[1]
	S += 58 < c_t5_t0_t4_mem1
	S += c_t5_t0_t4_mem1 <= c_t5_t0_t4

	c_t5_t00 = S.Task('c_t5_t00', length=4, delay_cost=1)
	c_t5_t00 += alt(MAS)
	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	c_t5_t00_in += alt(MAS_in)
	S += c_t5_t00_in*MAS_in[0]<=c_t5_t00*MAS[0]

	S += c_t5_t00_in*MAS_in[1]<=c_t5_t00*MAS[1]

	S += c_t5_t00_in*MAS_in[2]<=c_t5_t00*MAS[2]

	S += c_t5_t00_in*MAS_in[3]<=c_t5_t00*MAS[3]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	c_t5_t00_mem0 += MM_MEM[0]
	S += 68 < c_t5_t00_mem0
	S += c_t5_t00_mem0 <= c_t5_t00

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	c_t5_t00_mem1 += MM_MEM[1]
	S += 67 < c_t5_t00_mem1
	S += c_t5_t00_mem1 <= c_t5_t00

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=4, delay_cost=1)
	c_t5_t0_t5 += alt(MAS)
	c_t5_t0_t5_in = S.Task('c_t5_t0_t5_in', length=1, delay_cost=1)
	c_t5_t0_t5_in += alt(MAS_in)
	S += c_t5_t0_t5_in*MAS_in[0]<=c_t5_t0_t5*MAS[0]

	S += c_t5_t0_t5_in*MAS_in[1]<=c_t5_t0_t5*MAS[1]

	S += c_t5_t0_t5_in*MAS_in[2]<=c_t5_t0_t5*MAS[2]

	S += c_t5_t0_t5_in*MAS_in[3]<=c_t5_t0_t5*MAS[3]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	c_t5_t0_t5_mem0 += MM_MEM[0]
	S += 68 < c_t5_t0_t5_mem0
	S += c_t5_t0_t5_mem0 <= c_t5_t0_t5

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	c_t5_t0_t5_mem1 += MM_MEM[1]
	S += 67 < c_t5_t0_t5_mem1
	S += c_t5_t0_t5_mem1 <= c_t5_t0_t5

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=11, delay_cost=1)
	c_t5_t1_t4 += alt(MM)
	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	c_t5_t1_t4_in += alt(MM_in)
	S += c_t5_t1_t4_in*MM_in[0]<=c_t5_t1_t4*MM[0]
	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	c_t5_t1_t4_mem0 += MAS_MEM[0]
	S += 62 < c_t5_t1_t4_mem0
	S += c_t5_t1_t4_mem0 <= c_t5_t1_t4

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	c_t5_t1_t4_mem1 += MAS_MEM[5]
	S += 68 < c_t5_t1_t4_mem1
	S += c_t5_t1_t4_mem1 <= c_t5_t1_t4

	c_t5_t10 = S.Task('c_t5_t10', length=4, delay_cost=1)
	c_t5_t10 += alt(MAS)
	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	c_t5_t10_in += alt(MAS_in)
	S += c_t5_t10_in*MAS_in[0]<=c_t5_t10*MAS[0]

	S += c_t5_t10_in*MAS_in[1]<=c_t5_t10*MAS[1]

	S += c_t5_t10_in*MAS_in[2]<=c_t5_t10*MAS[2]

	S += c_t5_t10_in*MAS_in[3]<=c_t5_t10*MAS[3]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	c_t5_t10_mem0 += MM_MEM[0]
	S += 75 < c_t5_t10_mem0
	S += c_t5_t10_mem0 <= c_t5_t10

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	c_t5_t10_mem1 += MM_MEM[1]
	S += 71 < c_t5_t10_mem1
	S += c_t5_t10_mem1 <= c_t5_t10

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=4, delay_cost=1)
	c_t5_t1_t5 += alt(MAS)
	c_t5_t1_t5_in = S.Task('c_t5_t1_t5_in', length=1, delay_cost=1)
	c_t5_t1_t5_in += alt(MAS_in)
	S += c_t5_t1_t5_in*MAS_in[0]<=c_t5_t1_t5*MAS[0]

	S += c_t5_t1_t5_in*MAS_in[1]<=c_t5_t1_t5*MAS[1]

	S += c_t5_t1_t5_in*MAS_in[2]<=c_t5_t1_t5*MAS[2]

	S += c_t5_t1_t5_in*MAS_in[3]<=c_t5_t1_t5*MAS[3]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	c_t5_t1_t5_mem0 += MM_MEM[0]
	S += 75 < c_t5_t1_t5_mem0
	S += c_t5_t1_t5_mem0 <= c_t5_t1_t5

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	c_t5_t1_t5_mem1 += MM_MEM[1]
	S += 71 < c_t5_t1_t5_mem1
	S += c_t5_t1_t5_mem1 <= c_t5_t1_t5

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=11, delay_cost=1)
	c_t5_t4_t0 += alt(MM)
	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	c_t5_t4_t0_in += alt(MM_in)
	S += c_t5_t4_t0_in*MM_in[0]<=c_t5_t4_t0*MM[0]
	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	c_t5_t4_t0_mem0 += MAS_MEM[4]
	S += 62 < c_t5_t4_t0_mem0
	S += c_t5_t4_t0_mem0 <= c_t5_t4_t0

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	c_t5_t4_t0_mem1 += MAS_MEM[5]
	S += 69 < c_t5_t4_t0_mem1
	S += c_t5_t4_t0_mem1 <= c_t5_t4_t0

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=11, delay_cost=1)
	c_t5_t4_t1 += alt(MM)
	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	c_t5_t4_t1_in += alt(MM_in)
	S += c_t5_t4_t1_in*MM_in[0]<=c_t5_t4_t1*MM[0]
	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	c_t5_t4_t1_mem0 += MAS_MEM[6]
	S += 70 < c_t5_t4_t1_mem0
	S += c_t5_t4_t1_mem0 <= c_t5_t4_t1

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	c_t5_t4_t1_mem1 += MAS_MEM[7]
	S += 66 < c_t5_t4_t1_mem1
	S += c_t5_t4_t1_mem1 <= c_t5_t4_t1

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=4, delay_cost=1)
	c_t5_t4_t2 += alt(MAS)
	c_t5_t4_t2_in = S.Task('c_t5_t4_t2_in', length=1, delay_cost=1)
	c_t5_t4_t2_in += alt(MAS_in)
	S += c_t5_t4_t2_in*MAS_in[0]<=c_t5_t4_t2*MAS[0]

	S += c_t5_t4_t2_in*MAS_in[1]<=c_t5_t4_t2*MAS[1]

	S += c_t5_t4_t2_in*MAS_in[2]<=c_t5_t4_t2*MAS[2]

	S += c_t5_t4_t2_in*MAS_in[3]<=c_t5_t4_t2*MAS[3]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	c_t5_t4_t2_mem0 += MAS_MEM[4]
	S += 62 < c_t5_t4_t2_mem0
	S += c_t5_t4_t2_mem0 <= c_t5_t4_t2

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	c_t5_t4_t2_mem1 += MAS_MEM[7]
	S += 70 < c_t5_t4_t2_mem1
	S += c_t5_t4_t2_mem1 <= c_t5_t4_t2

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=4, delay_cost=1)
	c_t5_t4_t3 += alt(MAS)
	c_t5_t4_t3_in = S.Task('c_t5_t4_t3_in', length=1, delay_cost=1)
	c_t5_t4_t3_in += alt(MAS_in)
	S += c_t5_t4_t3_in*MAS_in[0]<=c_t5_t4_t3*MAS[0]

	S += c_t5_t4_t3_in*MAS_in[1]<=c_t5_t4_t3*MAS[1]

	S += c_t5_t4_t3_in*MAS_in[2]<=c_t5_t4_t3*MAS[2]

	S += c_t5_t4_t3_in*MAS_in[3]<=c_t5_t4_t3*MAS[3]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	c_t5_t4_t3_mem0 += MAS_MEM[4]
	S += 69 < c_t5_t4_t3_mem0
	S += c_t5_t4_t3_mem0 <= c_t5_t4_t3

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	c_t5_t4_t3_mem1 += MAS_MEM[7]
	S += 66 < c_t5_t4_t3_mem1
	S += c_t5_t4_t3_mem1 <= c_t5_t4_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage4MAS4/MUL/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

