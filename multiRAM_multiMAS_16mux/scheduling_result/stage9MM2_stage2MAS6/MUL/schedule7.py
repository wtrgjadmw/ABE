from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 207
	S = Scenario("schedule7", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=9)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 0
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 0
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 0
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 1
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 1
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 1
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=9, delay_cost=1)
	S += c_t0_t1_t1 >= 1
	c_t0_t1_t1 += MM[0]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=9, delay_cost=1)
	S += c_t0_t0_t1 >= 2
	c_t0_t0_t1 += MM[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 2
	c_t0_t1_t2_in += MAS_in[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 2
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 2
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=2, delay_cost=1)
	S += c_t0_t1_t2 >= 3
	c_t0_t1_t2 += MAS[0]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 3
	c_t0_t20_in += MAS_in[0]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 3
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 3
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t20 = S.Task('c_t0_t20', length=2, delay_cost=1)
	S += c_t0_t20 >= 4
	c_t0_t20 += MAS[0]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 4
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 4
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 4
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=9, delay_cost=1)
	S += c_t1_t0_t0 >= 5
	c_t1_t0_t0 += MM[0]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 5
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 5
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 5
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=2, delay_cost=1)
	S += c_t1_t0_t2 >= 6
	c_t1_t0_t2 += MAS[0]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 6
	c_t1_t30_in += MAS_in[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 6
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 6
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 7
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 7
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 7
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=2, delay_cost=1)
	S += c_t1_t30 >= 7
	c_t1_t30 += MAS[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=9, delay_cost=1)
	S += c_t0_t0_t0 >= 8
	c_t0_t0_t0 += MM[0]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 8
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 8
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 8
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=9, delay_cost=1)
	S += c_t2_t0_t0 >= 9
	c_t2_t0_t0 += MM[0]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 9
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 9
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 9
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 10
	c_t1_t20_in += MAS_in[0]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 10
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 10
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=9, delay_cost=1)
	S += c_t2_t0_t1 >= 10
	c_t2_t0_t1 += MM[0]

	c_t1_t20 = S.Task('c_t1_t20', length=2, delay_cost=1)
	S += c_t1_t20 >= 11
	c_t1_t20 += MAS[0]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 11
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 11
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 11
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 12
	c_t0_t0_t2_in += MAS_in[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 12
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 12
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 12
	c_t1_t4_t0_in += MM_in[1]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 12
	c_t1_t4_t0_mem0 += MAS_MEM[0]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 12
	c_t1_t4_t0_mem1 += MAS_MEM[1]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=9, delay_cost=1)
	S += c_t2_t1_t0 >= 12
	c_t2_t1_t0 += MM[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=2, delay_cost=1)
	S += c_t0_t0_t2 >= 13
	c_t0_t0_t2 += MAS[0]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 13
	c_t0_t0_t3_in += MAS_in[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 13
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 13
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=9, delay_cost=1)
	S += c_t1_t4_t0 >= 13
	c_t1_t4_t0 += MM[1]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=2, delay_cost=1)
	S += c_t0_t0_t3 >= 14
	c_t0_t0_t3 += MAS[0]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 14
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 14
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 14
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 15
	c_t0_t0_t4_in += MM_in[1]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 15
	c_t0_t0_t4_mem0 += MAS_MEM[0]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 15
	c_t0_t0_t4_mem1 += MAS_MEM[1]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=2, delay_cost=1)
	S += c_t0_t1_t3 >= 15
	c_t0_t1_t3 += MAS[0]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 15
	c_t1_t1_t2_in += MAS_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 15
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 15
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 16
	c_t0_t00_in += MAS_in[4]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 16
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 16
	c_t0_t00_mem1 += MM_MEM[1]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=9, delay_cost=1)
	S += c_t0_t0_t4 >= 16
	c_t0_t0_t4 += MM[1]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 16
	c_t0_t1_t4_in += MM_in[1]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 16
	c_t0_t1_t4_mem0 += MAS_MEM[0]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 16
	c_t0_t1_t4_mem1 += MAS_MEM[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 16
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 16
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 16
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=2, delay_cost=1)
	S += c_t1_t1_t2 >= 16
	c_t1_t1_t2 += MAS[0]

	c_t0_t00 = S.Task('c_t0_t00', length=2, delay_cost=1)
	S += c_t0_t00 >= 17
	c_t0_t00 += MAS[4]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 17
	c_t0_t0_t5_in += MAS_in[1]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 17
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 17
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=9, delay_cost=1)
	S += c_t0_t1_t4 >= 17
	c_t0_t1_t4 += MM[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=9, delay_cost=1)
	S += c_t1_t0_t1 >= 17
	c_t1_t0_t1 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 17
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 17
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 17
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=2, delay_cost=1)
	S += c_t0_t0_t5 >= 18
	c_t0_t0_t5 += MAS[1]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 18
	c_t0_t30_in += MAS_in[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 18
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 18
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 18
	c_t2_t0_t5_in += MAS_in[1]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 18
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 18
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=9, delay_cost=1)
	S += c_t2_t1_t1 >= 18
	c_t2_t1_t1 += MM[0]

	c_t0_t30 = S.Task('c_t0_t30', length=2, delay_cost=1)
	S += c_t0_t30 >= 19
	c_t0_t30 += MAS[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 19
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 19
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 19
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 19
	c_t2_t00_in += MAS_in[0]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 19
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 19
	c_t2_t00_mem1 += MM_MEM[1]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=2, delay_cost=1)
	S += c_t2_t0_t5 >= 19
	c_t2_t0_t5 += MAS[1]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 20
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 20
	c_t0_t4_t0_mem0 += MAS_MEM[0]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 20
	c_t0_t4_t0_mem1 += MAS_MEM[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=9, delay_cost=1)
	S += c_t1_t1_t1 >= 20
	c_t1_t1_t1 += MM[0]

	c_t2_t00 = S.Task('c_t2_t00', length=2, delay_cost=1)
	S += c_t2_t00 >= 20
	c_t2_t00 += MAS[0]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 20
	c_t2_t0_t2_in += MAS_in[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 20
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 20
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 21
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 21
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 21
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=9, delay_cost=1)
	S += c_t0_t4_t0 >= 21
	c_t0_t4_t0 += MM[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=2, delay_cost=1)
	S += c_t2_t0_t2 >= 21
	c_t2_t0_t2 += MAS[0]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=9, delay_cost=1)
	S += c_t0_t1_t0 >= 22
	c_t0_t1_t0 += MM[0]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 22
	c_t1_t1_t3_in += MAS_in[0]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 22
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 22
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 23
	c_t0_t31_in += MAS_in[2]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 23
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 23
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=2, delay_cost=1)
	S += c_t1_t1_t3 >= 23
	c_t1_t1_t3 += MAS[0]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 24
	c_t0_t01_in += MAS_in[0]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 24
	c_t0_t01_mem0 += MM_MEM[2]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 24
	c_t0_t01_mem1 += MAS_MEM[3]

	c_t0_t31 = S.Task('c_t0_t31', length=2, delay_cost=1)
	S += c_t0_t31 >= 24
	c_t0_t31 += MAS[2]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 24
	c_t1_t0_t3_in += MAS_in[4]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 24
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 24
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 24
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 24
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 24
	c_t1_t1_t4_mem1 += MAS_MEM[1]

	c_t0_t01 = S.Task('c_t0_t01', length=2, delay_cost=1)
	S += c_t0_t01 >= 25
	c_t0_t01 += MAS[0]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 25
	c_t0_t4_t3_in += MAS_in[5]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 25
	c_t0_t4_t3_mem0 += MAS_MEM[0]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 25
	c_t0_t4_t3_mem1 += MAS_MEM[5]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 25
	c_t1_t00_in += MAS_in[3]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 25
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 25
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=2, delay_cost=1)
	S += c_t1_t0_t3 >= 25
	c_t1_t0_t3 += MAS[4]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=9, delay_cost=1)
	S += c_t1_t1_t4 >= 25
	c_t1_t1_t4 += MM[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 25
	c_t2_t0_t3_in += MAS_in[2]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 25
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 25
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 26
	c_t0_t21_in += MAS_in[5]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 26
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 26
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=2, delay_cost=1)
	S += c_t0_t4_t3 >= 26
	c_t0_t4_t3 += MAS[5]

	c_t1_t00 = S.Task('c_t1_t00', length=2, delay_cost=1)
	S += c_t1_t00 >= 26
	c_t1_t00 += MAS[3]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 26
	c_t1_t0_t4_in += MM_in[1]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 26
	c_t1_t0_t4_mem0 += MAS_MEM[0]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 26
	c_t1_t0_t4_mem1 += MAS_MEM[9]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 26
	c_t1_t0_t5_in += MAS_in[0]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 26
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 26
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=2, delay_cost=1)
	S += c_t2_t0_t3 >= 26
	c_t2_t0_t3 += MAS[2]

	c_t0_t21 = S.Task('c_t0_t21', length=2, delay_cost=1)
	S += c_t0_t21 >= 27
	c_t0_t21 += MAS[5]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=9, delay_cost=1)
	S += c_t1_t0_t4 >= 27
	c_t1_t0_t4 += MM[1]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=2, delay_cost=1)
	S += c_t1_t0_t5 >= 27
	c_t1_t0_t5 += MAS[0]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 27
	c_t1_t21_in += MAS_in[5]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 27
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 27
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 27
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 27
	c_t2_t0_t4_mem0 += MAS_MEM[0]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 27
	c_t2_t0_t4_mem1 += MAS_MEM[5]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 27
	c_t2_t10_in += MAS_in[3]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 27
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 27
	c_t2_t10_mem1 += MM_MEM[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 28
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 28
	c_t0_t4_t1_mem0 += MAS_MEM[10]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 28
	c_t0_t4_t1_mem1 += MAS_MEM[5]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 28
	c_t0_t4_t2_in += MAS_in[5]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 28
	c_t0_t4_t2_mem0 += MAS_MEM[0]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 28
	c_t0_t4_t2_mem1 += MAS_MEM[11]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 28
	c_t1_t1_t0_in += MM_in[1]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 28
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 28
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t21 = S.Task('c_t1_t21', length=2, delay_cost=1)
	S += c_t1_t21 >= 28
	c_t1_t21 += MAS[5]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=9, delay_cost=1)
	S += c_t2_t0_t4 >= 28
	c_t2_t0_t4 += MM[0]

	c_t2_t10 = S.Task('c_t2_t10', length=2, delay_cost=1)
	S += c_t2_t10 >= 28
	c_t2_t10 += MAS[3]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 28
	c_t2_t1_t5_in += MAS_in[1]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 28
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 28
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=9, delay_cost=1)
	S += c_t0_t4_t1 >= 29
	c_t0_t4_t1 += MM[0]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=2, delay_cost=1)
	S += c_t0_t4_t2 >= 29
	c_t0_t4_t2 += MAS[5]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=9, delay_cost=1)
	S += c_t1_t1_t0 >= 29
	c_t1_t1_t0 += MM[1]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 29
	c_t1_t31_in += MAS_in[5]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 29
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 29
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 29
	c_t1_t4_t2_in += MAS_in[4]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 29
	c_t1_t4_t2_mem0 += MAS_MEM[0]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 29
	c_t1_t4_t2_mem1 += MAS_MEM[11]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=2, delay_cost=1)
	S += c_t2_t1_t5 >= 29
	c_t2_t1_t5 += MAS[1]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 30
	c_t0_t10_in += MAS_in[3]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 30
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 30
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	S += c_t0_t4_t4_in >= 30
	c_t0_t4_t4_in += MM_in[0]

	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem0 >= 30
	c_t0_t4_t4_mem0 += MAS_MEM[10]

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem1 >= 30
	c_t0_t4_t4_mem1 += MAS_MEM[11]

	c_t1_t31 = S.Task('c_t1_t31', length=2, delay_cost=1)
	S += c_t1_t31 >= 30
	c_t1_t31 += MAS[5]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=2, delay_cost=1)
	S += c_t1_t4_t2 >= 30
	c_t1_t4_t2 += MAS[4]

	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	S += c_t2_t50_in >= 30
	c_t2_t50_in += MAS_in[1]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 30
	c_t2_t50_mem0 += MAS_MEM[0]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 30
	c_t2_t50_mem1 += MAS_MEM[7]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 30
	c_t3010_in += MAS_in[2]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 30
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 30
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t0_t10 = S.Task('c_t0_t10', length=2, delay_cost=1)
	S += c_t0_t10 >= 31
	c_t0_t10 += MAS[3]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 31
	c_t0_t1_t5_in += MAS_in[1]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 31
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 31
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=9, delay_cost=1)
	S += c_t0_t4_t4 >= 31
	c_t0_t4_t4 += MM[0]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 31
	c_t1_t4_t1_in += MM_in[1]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 31
	c_t1_t4_t1_mem0 += MAS_MEM[10]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 31
	c_t1_t4_t1_mem1 += MAS_MEM[11]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 31
	c_t2_t1_t2_in += MAS_in[4]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 31
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 31
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t50 = S.Task('c_t2_t50', length=2, delay_cost=1)
	S += c_t2_t50 >= 31
	c_t2_t50 += MAS[1]

	c_t3010 = S.Task('c_t3010', length=2, delay_cost=1)
	S += c_t3010 >= 31
	c_t3010 += MAS[2]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=2, delay_cost=1)
	S += c_t0_t1_t5 >= 32
	c_t0_t1_t5 += MAS[1]

	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	S += c_t0_t50_in >= 32
	c_t0_t50_in += MAS_in[5]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 32
	c_t0_t50_mem0 += MAS_MEM[8]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 32
	c_t0_t50_mem1 += MAS_MEM[7]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=9, delay_cost=1)
	S += c_t1_t4_t1 >= 32
	c_t1_t4_t1 += MM[1]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 32
	c_t1_t4_t3_in += MAS_in[4]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 32
	c_t1_t4_t3_mem0 += MAS_MEM[0]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 32
	c_t1_t4_t3_mem1 += MAS_MEM[11]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=2, delay_cost=1)
	S += c_t2_t1_t2 >= 32
	c_t2_t1_t2 += MAS[4]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 32
	c_t3001_in += MAS_in[0]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 32
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 32
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 33
	c_t0_t11_in += MAS_in[1]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 33
	c_t0_t11_mem0 += MM_MEM[2]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 33
	c_t0_t11_mem1 += MAS_MEM[3]

	c_t0_t50 = S.Task('c_t0_t50', length=2, delay_cost=1)
	S += c_t0_t50 >= 33
	c_t0_t50 += MAS[5]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=2, delay_cost=1)
	S += c_t1_t4_t3 >= 33
	c_t1_t4_t3 += MAS[4]

	c_t3001 = S.Task('c_t3001', length=2, delay_cost=1)
	S += c_t3001 >= 33
	c_t3001 += MAS[0]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 33
	c_t3101_in += MAS_in[5]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 33
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 33
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t0_t11 = S.Task('c_t0_t11', length=2, delay_cost=1)
	S += c_t0_t11 >= 34
	c_t0_t11 += MAS[1]

	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	S += c_t1_t4_t4_in >= 34
	c_t1_t4_t4_in += MM_in[0]

	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem0 >= 34
	c_t1_t4_t4_mem0 += MAS_MEM[8]

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem1 >= 34
	c_t1_t4_t4_mem1 += MAS_MEM[9]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 34
	c_t2_t31_in += MAS_in[2]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 34
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 34
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t3101 = S.Task('c_t3101', length=2, delay_cost=1)
	S += c_t3101 >= 34
	c_t3101 += MAS[5]

	c_t0_s00_in = S.Task('c_t0_s00_in', length=1, delay_cost=1)
	S += c_t0_s00_in >= 35
	c_t0_s00_in += MAS_in[4]

	c_t0_s00_mem0 = S.Task('c_t0_s00_mem0', length=1, delay_cost=1)
	S += c_t0_s00_mem0 >= 35
	c_t0_s00_mem0 += MAS_MEM[6]

	c_t0_s00_mem1 = S.Task('c_t0_s00_mem1', length=1, delay_cost=1)
	S += c_t0_s00_mem1 >= 35
	c_t0_s00_mem1 += MAS_MEM[3]

	c_t0_s01_in = S.Task('c_t0_s01_in', length=1, delay_cost=1)
	S += c_t0_s01_in >= 35
	c_t0_s01_in += MAS_in[2]

	c_t0_s01_mem0 = S.Task('c_t0_s01_mem0', length=1, delay_cost=1)
	S += c_t0_s01_mem0 >= 35
	c_t0_s01_mem0 += MAS_MEM[2]

	c_t0_s01_mem1 = S.Task('c_t0_s01_mem1', length=1, delay_cost=1)
	S += c_t0_s01_mem1 >= 35
	c_t0_s01_mem1 += MAS_MEM[7]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 35
	c_t1_t01_in += MAS_in[3]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 35
	c_t1_t01_mem0 += MM_MEM[2]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 35
	c_t1_t01_mem1 += MAS_MEM[1]

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=9, delay_cost=1)
	S += c_t1_t4_t4 >= 35
	c_t1_t4_t4 += MM[0]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 35
	c_t2_t1_t3_in += MAS_in[1]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 35
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 35
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t31 = S.Task('c_t2_t31', length=2, delay_cost=1)
	S += c_t2_t31 >= 35
	c_t2_t31 += MAS[2]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 35
	c_t3_t0_t1_in += MM_in[1]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 35
	c_t3_t0_t1_mem0 += MAS_MEM[0]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 35
	c_t3_t0_t1_mem1 += MAS_MEM[11]

	c_t0_s00 = S.Task('c_t0_s00', length=2, delay_cost=1)
	S += c_t0_s00 >= 36
	c_t0_s00 += MAS[4]

	c_t0_s01 = S.Task('c_t0_s01', length=2, delay_cost=1)
	S += c_t0_s01 >= 36
	c_t0_s01 += MAS[2]

	c_t1_t01 = S.Task('c_t1_t01', length=2, delay_cost=1)
	S += c_t1_t01 >= 36
	c_t1_t01 += MAS[3]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 36
	c_t2_t01_in += MAS_in[2]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 36
	c_t2_t01_mem0 += MM_MEM[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 36
	c_t2_t01_mem1 += MAS_MEM[3]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=2, delay_cost=1)
	S += c_t2_t1_t3 >= 36
	c_t2_t1_t3 += MAS[1]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 36
	c_t3000_in += MAS_in[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 36
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 36
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=9, delay_cost=1)
	S += c_t3_t0_t1 >= 36
	c_t3_t0_t1 += MM[1]

	c_t001_in = S.Task('c_t001_in', length=1, delay_cost=1)
	S += c_t001_in >= 37
	c_t001_in += MAS_in[0]

	c_t001_mem0 = S.Task('c_t001_mem0', length=1, delay_cost=1)
	S += c_t001_mem0 >= 37
	c_t001_mem0 += MAS_MEM[0]

	c_t001_mem1 = S.Task('c_t001_mem1', length=1, delay_cost=1)
	S += c_t001_mem1 >= 37
	c_t001_mem1 += MAS_MEM[5]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 37
	c_t1_t1_t5_in += MAS_in[4]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 37
	c_t1_t1_t5_mem0 += MM_MEM[2]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 37
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t2_t01 = S.Task('c_t2_t01', length=2, delay_cost=1)
	S += c_t2_t01 >= 37
	c_t2_t01 += MAS[2]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 37
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 37
	c_t2_t1_t4_mem0 += MAS_MEM[8]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 37
	c_t2_t1_t4_mem1 += MAS_MEM[3]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 37
	c_t2_t21_in += MAS_in[3]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 37
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 37
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t3000 = S.Task('c_t3000', length=2, delay_cost=1)
	S += c_t3000 >= 37
	c_t3000 += MAS[3]

	c_t000_in = S.Task('c_t000_in', length=1, delay_cost=1)
	S += c_t000_in >= 38
	c_t000_in += MAS_in[1]

	c_t000_mem0 = S.Task('c_t000_mem0', length=1, delay_cost=1)
	S += c_t000_mem0 >= 38
	c_t000_mem0 += MAS_MEM[8]

	c_t000_mem1 = S.Task('c_t000_mem1', length=1, delay_cost=1)
	S += c_t000_mem1 >= 38
	c_t000_mem1 += MAS_MEM[9]

	c_t001 = S.Task('c_t001', length=2, delay_cost=1)
	S += c_t001 >= 38
	c_t001 += MAS[0]

	c_t0_t51_in = S.Task('c_t0_t51_in', length=1, delay_cost=1)
	S += c_t0_t51_in >= 38
	c_t0_t51_in += MAS_in[2]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	S += c_t0_t51_mem0 >= 38
	c_t0_t51_mem0 += MAS_MEM[0]

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	S += c_t0_t51_mem1 >= 38
	c_t0_t51_mem1 += MAS_MEM[3]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 38
	c_t1_t10_in += MAS_in[3]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 38
	c_t1_t10_mem0 += MM_MEM[2]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 38
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=2, delay_cost=1)
	S += c_t1_t1_t5 >= 38
	c_t1_t1_t5 += MAS[4]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=9, delay_cost=1)
	S += c_t2_t1_t4 >= 38
	c_t2_t1_t4 += MM[0]

	c_t2_t21 = S.Task('c_t2_t21', length=2, delay_cost=1)
	S += c_t2_t21 >= 38
	c_t2_t21 += MAS[3]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 38
	c_t2_t30_in += MAS_in[0]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 38
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 38
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 38
	c_t3_t20_in += MAS_in[4]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 38
	c_t3_t20_mem0 += MAS_MEM[6]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 38
	c_t3_t20_mem1 += MAS_MEM[5]

	c_t000 = S.Task('c_t000', length=2, delay_cost=1)
	S += c_t000 >= 39
	c_t000 += MAS[1]

	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	S += c_t0_t40_in >= 39
	c_t0_t40_in += MAS_in[3]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 39
	c_t0_t40_mem0 += MM_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 39
	c_t0_t40_mem1 += MM_MEM[1]

	c_t0_t51 = S.Task('c_t0_t51', length=2, delay_cost=1)
	S += c_t0_t51 >= 39
	c_t0_t51 += MAS[2]

	c_t1_t10 = S.Task('c_t1_t10', length=2, delay_cost=1)
	S += c_t1_t10 >= 39
	c_t1_t10 += MAS[3]

	c_t2_t30 = S.Task('c_t2_t30', length=2, delay_cost=1)
	S += c_t2_t30 >= 39
	c_t2_t30 += MAS[0]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 39
	c_t2_t4_t1_in += MM_in[1]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 39
	c_t2_t4_t1_mem0 += MAS_MEM[6]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 39
	c_t2_t4_t1_mem1 += MAS_MEM[5]

	c_t3_t20 = S.Task('c_t3_t20', length=2, delay_cost=1)
	S += c_t3_t20 >= 39
	c_t3_t20 += MAS[4]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 39
	c_t4010_in += MAS_in[0]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 39
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 39
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t0_t40 = S.Task('c_t0_t40', length=2, delay_cost=1)
	S += c_t0_t40 >= 40
	c_t0_t40 += MAS[3]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 40
	c_t1_t11_in += MAS_in[1]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 40
	c_t1_t11_mem0 += MM_MEM[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 40
	c_t1_t11_mem1 += MAS_MEM[9]

	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	S += c_t1_t4_t5_in >= 40
	c_t1_t4_t5_in += MAS_in[0]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem0 >= 40
	c_t1_t4_t5_mem0 += MM_MEM[2]

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem1 >= 40
	c_t1_t4_t5_mem1 += MM_MEM[3]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=9, delay_cost=1)
	S += c_t2_t4_t1 >= 40
	c_t2_t4_t1 += MM[1]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 40
	c_t2_t4_t3_in += MAS_in[3]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 40
	c_t2_t4_t3_mem0 += MAS_MEM[0]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 40
	c_t2_t4_t3_mem1 += MAS_MEM[5]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 40
	c_t3100_in += MAS_in[4]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 40
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 40
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 40
	c_t3_t0_t2_in += MAS_in[2]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 40
	c_t3_t0_t2_mem0 += MAS_MEM[6]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 40
	c_t3_t0_t2_mem1 += MAS_MEM[1]

	c_t4010 = S.Task('c_t4010', length=2, delay_cost=1)
	S += c_t4010 >= 40
	c_t4010 += MAS[0]

	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	S += c_t0_t4_t5_in >= 41
	c_t0_t4_t5_in += MAS_in[4]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem0 >= 41
	c_t0_t4_t5_mem0 += MM_MEM[0]

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem1 >= 41
	c_t0_t4_t5_mem1 += MM_MEM[1]

	c_t1_t11 = S.Task('c_t1_t11', length=2, delay_cost=1)
	S += c_t1_t11 >= 41
	c_t1_t11 += MAS[1]

	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	S += c_t1_t40_in >= 41
	c_t1_t40_in += MAS_in[1]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 41
	c_t1_t40_mem0 += MM_MEM[2]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 41
	c_t1_t40_mem1 += MM_MEM[3]

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=2, delay_cost=1)
	S += c_t1_t4_t5 >= 41
	c_t1_t4_t5 += MAS[0]

	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	S += c_t1_t50_in >= 41
	c_t1_t50_in += MAS_in[0]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 41
	c_t1_t50_mem0 += MAS_MEM[6]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 41
	c_t1_t50_mem1 += MAS_MEM[7]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=2, delay_cost=1)
	S += c_t2_t4_t3 >= 41
	c_t2_t4_t3 += MAS[3]

	c_t3100 = S.Task('c_t3100', length=2, delay_cost=1)
	S += c_t3100 >= 41
	c_t3100 += MAS[4]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 41
	c_t3111_in += MAS_in[3]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 41
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 41
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=2, delay_cost=1)
	S += c_t3_t0_t2 >= 41
	c_t3_t0_t2 += MAS[2]

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=2, delay_cost=1)
	S += c_t0_t4_t5 >= 42
	c_t0_t4_t5 += MAS[4]

	c_t1_s01_in = S.Task('c_t1_s01_in', length=1, delay_cost=1)
	S += c_t1_s01_in >= 42
	c_t1_s01_in += MAS_in[3]

	c_t1_s01_mem0 = S.Task('c_t1_s01_mem0', length=1, delay_cost=1)
	S += c_t1_s01_mem0 >= 42
	c_t1_s01_mem0 += MAS_MEM[2]

	c_t1_s01_mem1 = S.Task('c_t1_s01_mem1', length=1, delay_cost=1)
	S += c_t1_s01_mem1 >= 42
	c_t1_s01_mem1 += MAS_MEM[7]

	c_t1_t40 = S.Task('c_t1_t40', length=2, delay_cost=1)
	S += c_t1_t40 >= 42
	c_t1_t40 += MAS[1]

	c_t1_t50 = S.Task('c_t1_t50', length=2, delay_cost=1)
	S += c_t1_t50 >= 42
	c_t1_t50 += MAS[0]

	c_t3111 = S.Task('c_t3111', length=2, delay_cost=1)
	S += c_t3111 >= 42
	c_t3111 += MAS[3]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 42
	c_t3_t0_t0_in += MM_in[1]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 42
	c_t3_t0_t0_mem0 += MAS_MEM[6]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 42
	c_t3_t0_t0_mem1 += MAS_MEM[9]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 42
	c_t3_t0_t3_in += MAS_in[4]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 42
	c_t3_t0_t3_mem0 += MAS_MEM[8]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 42
	c_t3_t0_t3_mem1 += MAS_MEM[11]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 42
	c_t4000_in += MAS_in[5]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 42
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 42
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t0_t41_in = S.Task('c_t0_t41_in', length=1, delay_cost=1)
	S += c_t0_t41_in >= 43
	c_t0_t41_in += MAS_in[1]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 43
	c_t0_t41_mem0 += MM_MEM[0]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 43
	c_t0_t41_mem1 += MAS_MEM[9]

	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	S += c_t110_in >= 43
	c_t110_in += MAS_in[5]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 43
	c_t110_mem0 += MAS_MEM[2]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 43
	c_t110_mem1 += MAS_MEM[1]

	c_t1_s01 = S.Task('c_t1_s01', length=2, delay_cost=1)
	S += c_t1_s01 >= 43
	c_t1_s01 += MAS[3]

	c_t1_t51_in = S.Task('c_t1_t51_in', length=1, delay_cost=1)
	S += c_t1_t51_in >= 43
	c_t1_t51_in += MAS_in[2]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	S += c_t1_t51_mem0 >= 43
	c_t1_t51_mem0 += MAS_MEM[6]

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	S += c_t1_t51_mem1 >= 43
	c_t1_t51_mem1 += MAS_MEM[3]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=9, delay_cost=1)
	S += c_t3_t0_t0 >= 43
	c_t3_t0_t0 += MM[1]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=2, delay_cost=1)
	S += c_t3_t0_t3 >= 43
	c_t3_t0_t3 += MAS[4]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 43
	c_t3_t31_in += MAS_in[3]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 43
	c_t3_t31_mem0 += MAS_MEM[10]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 43
	c_t3_t31_mem1 += MAS_MEM[7]

	c_t4000 = S.Task('c_t4000', length=2, delay_cost=1)
	S += c_t4000 >= 43
	c_t4000 += MAS[5]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 43
	c_t5000_in += MAS_in[4]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 43
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 43
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	S += c_t010_in >= 44
	c_t010_in += MAS_in[4]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 44
	c_t010_mem0 += MAS_MEM[6]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 44
	c_t010_mem1 += MAS_MEM[11]

	c_t0_t41 = S.Task('c_t0_t41', length=2, delay_cost=1)
	S += c_t0_t41 >= 44
	c_t0_t41 += MAS[1]

	c_t110 = S.Task('c_t110', length=2, delay_cost=1)
	S += c_t110 >= 44
	c_t110 += MAS[5]

	c_t1_t51 = S.Task('c_t1_t51', length=2, delay_cost=1)
	S += c_t1_t51 >= 44
	c_t1_t51 += MAS[2]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 44
	c_t3011_in += MAS_in[5]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 44
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 44
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	S += c_t3_t0_t4_in >= 44
	c_t3_t0_t4_in += MM_in[1]

	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem0 >= 44
	c_t3_t0_t4_mem0 += MAS_MEM[4]

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem1 >= 44
	c_t3_t0_t4_mem1 += MAS_MEM[9]

	c_t3_t31 = S.Task('c_t3_t31', length=2, delay_cost=1)
	S += c_t3_t31 >= 44
	c_t3_t31 += MAS[3]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 44
	c_t4_t20_in += MAS_in[1]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 44
	c_t4_t20_mem0 += MAS_MEM[10]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 44
	c_t4_t20_mem1 += MAS_MEM[1]

	c_t5000 = S.Task('c_t5000', length=2, delay_cost=1)
	S += c_t5000 >= 44
	c_t5000 += MAS[4]

	c_t010 = S.Task('c_t010', length=2, delay_cost=1)
	S += c_t010 >= 45
	c_t010 += MAS[4]

	c_t011_in = S.Task('c_t011_in', length=1, delay_cost=1)
	S += c_t011_in >= 45
	c_t011_in += MAS_in[0]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 45
	c_t011_mem0 += MAS_MEM[2]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 45
	c_t011_mem1 += MAS_MEM[5]

	c_t1_s00_in = S.Task('c_t1_s00_in', length=1, delay_cost=1)
	S += c_t1_s00_in >= 45
	c_t1_s00_in += MAS_in[2]

	c_t1_s00_mem0 = S.Task('c_t1_s00_mem0', length=1, delay_cost=1)
	S += c_t1_s00_mem0 >= 45
	c_t1_s00_mem0 += MAS_MEM[6]

	c_t1_s00_mem1 = S.Task('c_t1_s00_mem1', length=1, delay_cost=1)
	S += c_t1_s00_mem1 >= 45
	c_t1_s00_mem1 += MAS_MEM[3]

	c_t1_t41_in = S.Task('c_t1_t41_in', length=1, delay_cost=1)
	S += c_t1_t41_in >= 45
	c_t1_t41_in += MAS_in[4]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 45
	c_t1_t41_mem0 += MM_MEM[0]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 45
	c_t1_t41_mem1 += MAS_MEM[1]

	c_t3011 = S.Task('c_t3011', length=2, delay_cost=1)
	S += c_t3011 >= 45
	c_t3011 += MAS[5]

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=9, delay_cost=1)
	S += c_t3_t0_t4 >= 45
	c_t3_t0_t4 += MM[1]

	c_t4_t20 = S.Task('c_t4_t20', length=2, delay_cost=1)
	S += c_t4_t20 >= 45
	c_t4_t20 += MAS[1]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 45
	c_t5001_in += MAS_in[1]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 45
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 45
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t011 = S.Task('c_t011', length=2, delay_cost=1)
	S += c_t011 >= 46
	c_t011 += MAS[0]

	c_t1_s00 = S.Task('c_t1_s00', length=2, delay_cost=1)
	S += c_t1_s00 >= 46
	c_t1_s00 += MAS[2]

	c_t1_t41 = S.Task('c_t1_t41', length=2, delay_cost=1)
	S += c_t1_t41 >= 46
	c_t1_t41 += MAS[4]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 46
	c_t2_t11_in += MAS_in[1]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 46
	c_t2_t11_mem0 += MM_MEM[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 46
	c_t2_t11_mem1 += MAS_MEM[3]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 46
	c_t3_t1_t1_in += MM_in[1]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 46
	c_t3_t1_t1_mem0 += MAS_MEM[10]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 46
	c_t3_t1_t1_mem1 += MAS_MEM[7]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 46
	c_t3_t21_in += MAS_in[5]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 46
	c_t3_t21_mem0 += MAS_MEM[0]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 46
	c_t3_t21_mem1 += MAS_MEM[11]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 46
	c_t4101_in += MAS_in[4]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 46
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 46
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t5001 = S.Task('c_t5001', length=2, delay_cost=1)
	S += c_t5001 >= 46
	c_t5001 += MAS[1]

	c_t101_in = S.Task('c_t101_in', length=1, delay_cost=1)
	S += c_t101_in >= 47
	c_t101_in += MAS_in[0]

	c_t101_mem0 = S.Task('c_t101_mem0', length=1, delay_cost=1)
	S += c_t101_mem0 >= 47
	c_t101_mem0 += MAS_MEM[6]

	c_t101_mem1 = S.Task('c_t101_mem1', length=1, delay_cost=1)
	S += c_t101_mem1 >= 47
	c_t101_mem1 += MAS_MEM[7]

	c_t2_t11 = S.Task('c_t2_t11', length=2, delay_cost=1)
	S += c_t2_t11 >= 47
	c_t2_t11 += MAS[1]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=9, delay_cost=1)
	S += c_t3_t1_t1 >= 47
	c_t3_t1_t1 += MM[1]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 47
	c_t3_t1_t2_in += MAS_in[4]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 47
	c_t3_t1_t2_mem0 += MAS_MEM[4]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 47
	c_t3_t1_t2_mem1 += MAS_MEM[11]

	c_t3_t21 = S.Task('c_t3_t21', length=2, delay_cost=1)
	S += c_t3_t21 >= 47
	c_t3_t21 += MAS[5]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 47
	c_t4001_in += MAS_in[5]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 47
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 47
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4101 = S.Task('c_t4101', length=2, delay_cost=1)
	S += c_t4101 >= 47
	c_t4101 += MAS[4]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 47
	c_t5_t0_t2_in += MAS_in[2]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 47
	c_t5_t0_t2_mem0 += MAS_MEM[8]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 47
	c_t5_t0_t2_mem1 += MAS_MEM[3]

	c_t101 = S.Task('c_t101', length=2, delay_cost=1)
	S += c_t101 >= 48
	c_t101 += MAS[0]

	c_t2_s00_in = S.Task('c_t2_s00_in', length=1, delay_cost=1)
	S += c_t2_s00_in >= 48
	c_t2_s00_in += MAS_in[5]

	c_t2_s00_mem0 = S.Task('c_t2_s00_mem0', length=1, delay_cost=1)
	S += c_t2_s00_mem0 >= 48
	c_t2_s00_mem0 += MAS_MEM[6]

	c_t2_s00_mem1 = S.Task('c_t2_s00_mem1', length=1, delay_cost=1)
	S += c_t2_s00_mem1 >= 48
	c_t2_s00_mem1 += MAS_MEM[3]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=2, delay_cost=1)
	S += c_t3_t1_t2 >= 48
	c_t3_t1_t2 += MAS[4]

	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	S += c_t3_t4_t1_in >= 48
	c_t3_t4_t1_in += MM_in[0]

	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem0 >= 48
	c_t3_t4_t1_mem0 += MAS_MEM[10]

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem1 >= 48
	c_t3_t4_t1_mem1 += MAS_MEM[7]

	c_t3_t4_t2_in = S.Task('c_t3_t4_t2_in', length=1, delay_cost=1)
	S += c_t3_t4_t2_in >= 48
	c_t3_t4_t2_in += MAS_in[2]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem0 >= 48
	c_t3_t4_t2_mem0 += MAS_MEM[8]

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem1 >= 48
	c_t3_t4_t2_mem1 += MAS_MEM[11]

	c_t4001 = S.Task('c_t4001', length=2, delay_cost=1)
	S += c_t4001 >= 48
	c_t4001 += MAS[5]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 48
	c_t4100_in += MAS_in[4]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 48
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 48
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=2, delay_cost=1)
	S += c_t5_t0_t2 >= 48
	c_t5_t0_t2 += MAS[2]

	c_t111_in = S.Task('c_t111_in', length=1, delay_cost=1)
	S += c_t111_in >= 49
	c_t111_in += MAS_in[0]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 49
	c_t111_mem0 += MAS_MEM[8]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 49
	c_t111_mem1 += MAS_MEM[5]

	c_t2_s00 = S.Task('c_t2_s00', length=2, delay_cost=1)
	S += c_t2_s00 >= 49
	c_t2_s00 += MAS[5]

	c_t2_s01_in = S.Task('c_t2_s01_in', length=1, delay_cost=1)
	S += c_t2_s01_in >= 49
	c_t2_s01_in += MAS_in[5]

	c_t2_s01_mem0 = S.Task('c_t2_s01_mem0', length=1, delay_cost=1)
	S += c_t2_s01_mem0 >= 49
	c_t2_s01_mem0 += MAS_MEM[2]

	c_t2_s01_mem1 = S.Task('c_t2_s01_mem1', length=1, delay_cost=1)
	S += c_t2_s01_mem1 >= 49
	c_t2_s01_mem1 += MAS_MEM[7]

	c_t2_t51_in = S.Task('c_t2_t51_in', length=1, delay_cost=1)
	S += c_t2_t51_in >= 49
	c_t2_t51_in += MAS_in[2]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	S += c_t2_t51_mem0 >= 49
	c_t2_t51_mem0 += MAS_MEM[4]

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	S += c_t2_t51_mem1 >= 49
	c_t2_t51_mem1 += MAS_MEM[3]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 49
	c_t3110_in += MAS_in[4]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 49
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 49
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=9, delay_cost=1)
	S += c_t3_t4_t1 >= 49
	c_t3_t4_t1 += MM[0]

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=2, delay_cost=1)
	S += c_t3_t4_t2 >= 49
	c_t3_t4_t2 += MAS[2]

	c_t4100 = S.Task('c_t4100', length=2, delay_cost=1)
	S += c_t4100 >= 49
	c_t4100 += MAS[4]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 49
	c_t4_t0_t1_in += MM_in[1]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 49
	c_t4_t0_t1_mem0 += MAS_MEM[10]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 49
	c_t4_t0_t1_mem1 += MAS_MEM[9]

	c_t6001_in = S.Task('c_t6001_in', length=1, delay_cost=1)
	S += c_t6001_in >= 49
	c_t6001_in += MAS_in[3]

	c_t6001_mem0 = S.Task('c_t6001_mem0', length=1, delay_cost=1)
	S += c_t6001_mem0 >= 49
	c_t6001_mem0 += MAS_MEM[0]

	c_t6001_mem1 = S.Task('c_t6001_mem1', length=1, delay_cost=1)
	S += c_t6001_mem1 >= 49
	c_t6001_mem1 += MAS_MEM[1]

	c_t100_in = S.Task('c_t100_in', length=1, delay_cost=1)
	S += c_t100_in >= 50
	c_t100_in += MAS_in[1]

	c_t100_mem0 = S.Task('c_t100_mem0', length=1, delay_cost=1)
	S += c_t100_mem0 >= 50
	c_t100_mem0 += MAS_MEM[6]

	c_t100_mem1 = S.Task('c_t100_mem1', length=1, delay_cost=1)
	S += c_t100_mem1 >= 50
	c_t100_mem1 += MAS_MEM[5]

	c_t111 = S.Task('c_t111', length=2, delay_cost=1)
	S += c_t111 >= 50
	c_t111 += MAS[0]

	c_t2_s01 = S.Task('c_t2_s01', length=2, delay_cost=1)
	S += c_t2_s01 >= 50
	c_t2_s01 += MAS[5]

	c_t2_t51 = S.Task('c_t2_t51', length=2, delay_cost=1)
	S += c_t2_t51 >= 50
	c_t2_t51 += MAS[2]

	c_t3110 = S.Task('c_t3110', length=2, delay_cost=1)
	S += c_t3110 >= 50
	c_t3110 += MAS[4]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=9, delay_cost=1)
	S += c_t4_t0_t1 >= 50
	c_t4_t0_t1 += MM[1]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 50
	c_t4_t0_t2_in += MAS_in[2]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 50
	c_t4_t0_t2_mem0 += MAS_MEM[10]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 50
	c_t4_t0_t2_mem1 += MAS_MEM[11]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 50
	c_t4_t0_t3_in += MAS_in[3]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 50
	c_t4_t0_t3_mem0 += MAS_MEM[8]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 50
	c_t4_t0_t3_mem1 += MAS_MEM[9]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 50
	c_t5111_in += MAS_in[5]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 50
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 50
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t6001 = S.Task('c_t6001', length=2, delay_cost=1)
	S += c_t6001 >= 50
	c_t6001 += MAS[3]

	c_t100 = S.Task('c_t100', length=2, delay_cost=1)
	S += c_t100 >= 51
	c_t100 += MAS[1]

	c_t200_in = S.Task('c_t200_in', length=1, delay_cost=1)
	S += c_t200_in >= 51
	c_t200_in += MAS_in[1]

	c_t200_mem0 = S.Task('c_t200_mem0', length=1, delay_cost=1)
	S += c_t200_mem0 >= 51
	c_t200_mem0 += MAS_MEM[0]

	c_t200_mem1 = S.Task('c_t200_mem1', length=1, delay_cost=1)
	S += c_t200_mem1 >= 51
	c_t200_mem1 += MAS_MEM[11]

	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	S += c_t3_t00_in >= 51
	c_t3_t00_in += MAS_in[2]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 51
	c_t3_t00_mem0 += MM_MEM[2]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 51
	c_t3_t00_mem1 += MM_MEM[3]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 51
	c_t3_t1_t0_in += MM_in[1]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 51
	c_t3_t1_t0_mem0 += MAS_MEM[4]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 51
	c_t3_t1_t0_mem1 += MAS_MEM[9]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 51
	c_t3_t1_t3_in += MAS_in[5]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 51
	c_t3_t1_t3_mem0 += MAS_MEM[8]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 51
	c_t3_t1_t3_mem1 += MAS_MEM[7]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 51
	c_t4110_in += MAS_in[3]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 51
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 51
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=2, delay_cost=1)
	S += c_t4_t0_t2 >= 51
	c_t4_t0_t2 += MAS[2]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=2, delay_cost=1)
	S += c_t4_t0_t3 >= 51
	c_t4_t0_t3 += MAS[3]

	c_t5111 = S.Task('c_t5111', length=2, delay_cost=1)
	S += c_t5111 >= 51
	c_t5111 += MAS[5]

	c_t200 = S.Task('c_t200', length=2, delay_cost=1)
	S += c_t200 >= 52
	c_t200 += MAS[1]

	c_t3_t00 = S.Task('c_t3_t00', length=2, delay_cost=1)
	S += c_t3_t00 >= 52
	c_t3_t00 += MAS[2]

	c_t3_t0_t5_in = S.Task('c_t3_t0_t5_in', length=1, delay_cost=1)
	S += c_t3_t0_t5_in >= 52
	c_t3_t0_t5_in += MAS_in[2]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem0 >= 52
	c_t3_t0_t5_mem0 += MM_MEM[2]

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem1 >= 52
	c_t3_t0_t5_mem1 += MM_MEM[3]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=9, delay_cost=1)
	S += c_t3_t1_t0 >= 52
	c_t3_t1_t0 += MM[1]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=2, delay_cost=1)
	S += c_t3_t1_t3 >= 52
	c_t3_t1_t3 += MAS[5]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 52
	c_t4011_in += MAS_in[5]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 52
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 52
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4110 = S.Task('c_t4110', length=2, delay_cost=1)
	S += c_t4110 >= 52
	c_t4110 += MAS[3]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 52
	c_t4_t0_t0_in += MM_in[1]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 52
	c_t4_t0_t0_mem0 += MAS_MEM[10]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 52
	c_t4_t0_t0_mem1 += MAS_MEM[9]

	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	S += c_t4_t0_t4_in >= 52
	c_t4_t0_t4_in += MM_in[0]

	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem0 >= 52
	c_t4_t0_t4_mem0 += MAS_MEM[4]

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem1 >= 52
	c_t4_t0_t4_mem1 += MAS_MEM[7]

	c_t6000_in = S.Task('c_t6000_in', length=1, delay_cost=1)
	S += c_t6000_in >= 52
	c_t6000_in += MAS_in[3]

	c_t6000_mem0 = S.Task('c_t6000_mem0', length=1, delay_cost=1)
	S += c_t6000_mem0 >= 52
	c_t6000_mem0 += MAS_MEM[2]

	c_t6000_mem1 = S.Task('c_t6000_mem1', length=1, delay_cost=1)
	S += c_t6000_mem1 >= 52
	c_t6000_mem1 += MAS_MEM[3]

	c_t6010_in = S.Task('c_t6010_in', length=1, delay_cost=1)
	S += c_t6010_in >= 52
	c_t6010_in += MAS_in[1]

	c_t6010_mem0 = S.Task('c_t6010_mem0', length=1, delay_cost=1)
	S += c_t6010_mem0 >= 52
	c_t6010_mem0 += MAS_MEM[8]

	c_t6010_mem1 = S.Task('c_t6010_mem1', length=1, delay_cost=1)
	S += c_t6010_mem1 >= 52
	c_t6010_mem1 += MAS_MEM[11]

	c_t6011_in = S.Task('c_t6011_in', length=1, delay_cost=1)
	S += c_t6011_in >= 52
	c_t6011_in += MAS_in[0]

	c_t6011_mem0 = S.Task('c_t6011_mem0', length=1, delay_cost=1)
	S += c_t6011_mem0 >= 52
	c_t6011_mem0 += MAS_MEM[0]

	c_t6011_mem1 = S.Task('c_t6011_mem1', length=1, delay_cost=1)
	S += c_t6011_mem1 >= 52
	c_t6011_mem1 += MAS_MEM[1]

	c_t201_in = S.Task('c_t201_in', length=1, delay_cost=1)
	S += c_t201_in >= 53
	c_t201_in += MAS_in[1]

	c_t201_mem0 = S.Task('c_t201_mem0', length=1, delay_cost=1)
	S += c_t201_mem0 >= 53
	c_t201_mem0 += MAS_MEM[4]

	c_t201_mem1 = S.Task('c_t201_mem1', length=1, delay_cost=1)
	S += c_t201_mem1 >= 53
	c_t201_mem1 += MAS_MEM[11]

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=2, delay_cost=1)
	S += c_t3_t0_t5 >= 53
	c_t3_t0_t5 += MAS[2]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 53
	c_t3_t30_in += MAS_in[2]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 53
	c_t3_t30_mem0 += MAS_MEM[8]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 53
	c_t3_t30_mem1 += MAS_MEM[9]

	c_t4011 = S.Task('c_t4011', length=2, delay_cost=1)
	S += c_t4011 >= 53
	c_t4011 += MAS[5]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 53
	c_t4111_in += MAS_in[5]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 53
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 53
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=9, delay_cost=1)
	S += c_t4_t0_t0 >= 53
	c_t4_t0_t0 += MM[1]

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=9, delay_cost=1)
	S += c_t4_t0_t4 >= 53
	c_t4_t0_t4 += MM[0]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 53
	c_t4_t1_t0_in += MM_in[1]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 53
	c_t4_t1_t0_mem0 += MAS_MEM[0]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 53
	c_t4_t1_t0_mem1 += MAS_MEM[7]

	c_t6000 = S.Task('c_t6000', length=2, delay_cost=1)
	S += c_t6000 >= 53
	c_t6000 += MAS[3]

	c_t6010 = S.Task('c_t6010', length=2, delay_cost=1)
	S += c_t6010 >= 53
	c_t6010 += MAS[1]

	c_t6011 = S.Task('c_t6011', length=2, delay_cost=1)
	S += c_t6011 >= 53
	c_t6011 += MAS[0]

	c_t8000_in = S.Task('c_t8000_in', length=1, delay_cost=1)
	S += c_t8000_in >= 53
	c_t8000_in += MAS_in[3]

	c_t8000_mem0 = S.Task('c_t8000_mem0', length=1, delay_cost=1)
	S += c_t8000_mem0 >= 53
	c_t8000_mem0 += MAS_MEM[2]

	c_t8000_mem1 = S.Task('c_t8000_mem1', length=1, delay_cost=1)
	S += c_t8000_mem1 >= 53
	c_t8000_mem1 += MAS_MEM[3]

	c_t201 = S.Task('c_t201', length=2, delay_cost=1)
	S += c_t201 >= 54
	c_t201 += MAS[1]

	c_t3_t01_in = S.Task('c_t3_t01_in', length=1, delay_cost=1)
	S += c_t3_t01_in >= 54
	c_t3_t01_in += MAS_in[0]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 54
	c_t3_t01_mem0 += MM_MEM[2]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 54
	c_t3_t01_mem1 += MAS_MEM[5]

	c_t3_t30 = S.Task('c_t3_t30', length=2, delay_cost=1)
	S += c_t3_t30 >= 54
	c_t3_t30 += MAS[2]

	c_t4111 = S.Task('c_t4111', length=2, delay_cost=1)
	S += c_t4111 >= 54
	c_t4111 += MAS[5]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=9, delay_cost=1)
	S += c_t4_t1_t0 >= 54
	c_t4_t1_t0 += MM[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 54
	c_t4_t1_t2_in += MAS_in[5]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 54
	c_t4_t1_t2_mem0 += MAS_MEM[0]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 54
	c_t4_t1_t2_mem1 += MAS_MEM[11]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 54
	c_t4_t30_in += MAS_in[1]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 54
	c_t4_t30_mem0 += MAS_MEM[8]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 54
	c_t4_t30_mem1 += MAS_MEM[7]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 54
	c_t5101_in += MAS_in[4]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 54
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 54
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t7000_in = S.Task('c_t7000_in', length=1, delay_cost=1)
	S += c_t7000_in >= 54
	c_t7000_in += MAS_in[3]

	c_t7000_mem0 = S.Task('c_t7000_mem0', length=1, delay_cost=1)
	S += c_t7000_mem0 >= 54
	c_t7000_mem0 += MAS_MEM[2]

	c_t7000_mem1 = S.Task('c_t7000_mem1', length=1, delay_cost=1)
	S += c_t7000_mem1 >= 54
	c_t7000_mem1 += MAS_MEM[3]

	c_t8000 = S.Task('c_t8000', length=2, delay_cost=1)
	S += c_t8000 >= 54
	c_t8000 += MAS[3]

	c_t3_t01 = S.Task('c_t3_t01', length=2, delay_cost=1)
	S += c_t3_t01 >= 55
	c_t3_t01 += MAS[0]

	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	S += c_t3_t4_t0_in >= 55
	c_t3_t4_t0_in += MM_in[0]

	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem0 >= 55
	c_t3_t4_t0_mem0 += MAS_MEM[8]

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem1 >= 55
	c_t3_t4_t0_mem1 += MAS_MEM[5]

	c_t3_t4_t3_in = S.Task('c_t3_t4_t3_in', length=1, delay_cost=1)
	S += c_t3_t4_t3_in >= 55
	c_t3_t4_t3_in += MAS_in[5]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem0 >= 55
	c_t3_t4_t3_mem0 += MAS_MEM[4]

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem1 >= 55
	c_t3_t4_t3_mem1 += MAS_MEM[7]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 55
	c_t4_t1_t1_in += MM_in[1]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 55
	c_t4_t1_t1_mem0 += MAS_MEM[10]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 55
	c_t4_t1_t1_mem1 += MAS_MEM[11]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=2, delay_cost=1)
	S += c_t4_t1_t2 >= 55
	c_t4_t1_t2 += MAS[5]

	c_t4_t30 = S.Task('c_t4_t30', length=2, delay_cost=1)
	S += c_t4_t30 >= 55
	c_t4_t30 += MAS[1]

	c_t5101 = S.Task('c_t5101', length=2, delay_cost=1)
	S += c_t5101 >= 55
	c_t5101 += MAS[4]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 55
	c_t5110_in += MAS_in[1]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 55
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 55
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t7000 = S.Task('c_t7000', length=2, delay_cost=1)
	S += c_t7000 >= 55
	c_t7000 += MAS[3]

	c_t7001_in = S.Task('c_t7001_in', length=1, delay_cost=1)
	S += c_t7001_in >= 55
	c_t7001_in += MAS_in[3]

	c_t7001_mem0 = S.Task('c_t7001_mem0', length=1, delay_cost=1)
	S += c_t7001_mem0 >= 55
	c_t7001_mem0 += MAS_MEM[0]

	c_t7001_mem1 = S.Task('c_t7001_mem1', length=1, delay_cost=1)
	S += c_t7001_mem1 >= 55
	c_t7001_mem1 += MAS_MEM[3]

	c_t8001_in = S.Task('c_t8001_in', length=1, delay_cost=1)
	S += c_t8001_in >= 55
	c_t8001_in += MAS_in[4]

	c_t8001_mem0 = S.Task('c_t8001_mem0', length=1, delay_cost=1)
	S += c_t8001_mem0 >= 55
	c_t8001_mem0 += MAS_MEM[2]

	c_t8001_mem1 = S.Task('c_t8001_mem1', length=1, delay_cost=1)
	S += c_t8001_mem1 >= 55
	c_t8001_mem1 += MAS_MEM[1]

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=9, delay_cost=1)
	S += c_t3_t4_t0 >= 56
	c_t3_t4_t0 += MM[0]

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=2, delay_cost=1)
	S += c_t3_t4_t3 >= 56
	c_t3_t4_t3 += MAS[5]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=9, delay_cost=1)
	S += c_t4_t1_t1 >= 56
	c_t4_t1_t1 += MM[1]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 56
	c_t4_t1_t3_in += MAS_in[1]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 56
	c_t4_t1_t3_mem0 += MAS_MEM[6]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 56
	c_t4_t1_t3_mem1 += MAS_MEM[11]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 56
	c_t5100_in += MAS_in[5]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 56
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 56
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5110 = S.Task('c_t5110', length=2, delay_cost=1)
	S += c_t5110 >= 56
	c_t5110 += MAS[1]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 56
	c_t5_t0_t1_in += MM_in[1]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 56
	c_t5_t0_t1_mem0 += MAS_MEM[2]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 56
	c_t5_t0_t1_mem1 += MAS_MEM[9]

	c_t7001 = S.Task('c_t7001', length=2, delay_cost=1)
	S += c_t7001 >= 56
	c_t7001 += MAS[3]

	c_t8001 = S.Task('c_t8001', length=2, delay_cost=1)
	S += c_t8001 >= 56
	c_t8001 += MAS[4]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=2, delay_cost=1)
	S += c_t4_t1_t3 >= 57
	c_t4_t1_t3 += MAS[1]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 57
	c_t5010_in += MAS_in[5]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 57
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 57
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5100 = S.Task('c_t5100', length=2, delay_cost=1)
	S += c_t5100 >= 57
	c_t5100 += MAS[5]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=9, delay_cost=1)
	S += c_t5_t0_t1 >= 57
	c_t5_t0_t1 += MM[1]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 57
	c_t5_t1_t3_in += MAS_in[1]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 57
	c_t5_t1_t3_mem0 += MAS_MEM[2]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 57
	c_t5_t1_t3_mem1 += MAS_MEM[11]

	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	S += c_t4_t4_t0_in >= 58
	c_t4_t4_t0_in += MM_in[1]

	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem0 >= 58
	c_t4_t4_t0_mem0 += MAS_MEM[2]

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem1 >= 58
	c_t4_t4_t0_mem1 += MAS_MEM[3]

	c_t5010 = S.Task('c_t5010', length=2, delay_cost=1)
	S += c_t5010 >= 58
	c_t5010 += MAS[5]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 58
	c_t5011_in += MAS_in[5]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 58
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 58
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 58
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 58
	c_t5_t0_t0_mem0 += MAS_MEM[8]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 58
	c_t5_t0_t0_mem1 += MAS_MEM[11]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 58
	c_t5_t0_t3_in += MAS_in[3]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 58
	c_t5_t0_t3_mem0 += MAS_MEM[10]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 58
	c_t5_t0_t3_mem1 += MAS_MEM[9]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=2, delay_cost=1)
	S += c_t5_t1_t3 >= 58
	c_t5_t1_t3 += MAS[1]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 59
	c_t2_t20_in += MAS_in[2]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 59
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 59
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=9, delay_cost=1)
	S += c_t4_t4_t0 >= 59
	c_t4_t4_t0 += MM[1]

	c_t5011 = S.Task('c_t5011', length=2, delay_cost=1)
	S += c_t5011 >= 59
	c_t5011 += MAS[5]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=9, delay_cost=1)
	S += c_t5_t0_t0 >= 59
	c_t5_t0_t0 += MM[0]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=2, delay_cost=1)
	S += c_t5_t0_t3 >= 59
	c_t5_t0_t3 += MAS[3]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 59
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 59
	c_t5_t1_t0_mem0 += MAS_MEM[10]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 59
	c_t5_t1_t0_mem1 += MAS_MEM[3]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 59
	c_t5_t20_in += MAS_in[3]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 59
	c_t5_t20_mem0 += MAS_MEM[8]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 59
	c_t5_t20_mem1 += MAS_MEM[11]

	c_t2_t20 = S.Task('c_t2_t20', length=2, delay_cost=1)
	S += c_t2_t20 >= 60
	c_t2_t20 += MAS[2]

	c_t3_t1_t5_in = S.Task('c_t3_t1_t5_in', length=1, delay_cost=1)
	S += c_t3_t1_t5_in >= 60
	c_t3_t1_t5_in += MAS_in[4]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem0 >= 60
	c_t3_t1_t5_mem0 += MM_MEM[2]

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem1 >= 60
	c_t3_t1_t5_mem1 += MM_MEM[3]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 60
	c_t4_t31_in += MAS_in[3]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 60
	c_t4_t31_mem0 += MAS_MEM[8]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 60
	c_t4_t31_mem1 += MAS_MEM[11]

	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	S += c_t5_t0_t4_in >= 60
	c_t5_t0_t4_in += MM_in[0]

	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem0 >= 60
	c_t5_t0_t4_mem0 += MAS_MEM[4]

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem1 >= 60
	c_t5_t0_t4_mem1 += MAS_MEM[7]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=9, delay_cost=1)
	S += c_t5_t1_t0 >= 60
	c_t5_t1_t0 += MM[0]

	c_t5_t20 = S.Task('c_t5_t20', length=2, delay_cost=1)
	S += c_t5_t20 >= 60
	c_t5_t20 += MAS[3]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 60
	c_t5_t30_in += MAS_in[0]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 60
	c_t5_t30_mem0 += MAS_MEM[10]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 60
	c_t5_t30_mem1 += MAS_MEM[3]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 61
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 61
	c_t2_t4_t0_mem0 += MAS_MEM[4]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 61
	c_t2_t4_t0_mem1 += MAS_MEM[1]

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=2, delay_cost=1)
	S += c_t3_t1_t5 >= 61
	c_t3_t1_t5 += MAS[4]

	c_t4_t0_t5_in = S.Task('c_t4_t0_t5_in', length=1, delay_cost=1)
	S += c_t4_t0_t5_in >= 61
	c_t4_t0_t5_in += MAS_in[4]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem0 >= 61
	c_t4_t0_t5_mem0 += MM_MEM[2]

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem1 >= 61
	c_t4_t0_t5_mem1 += MM_MEM[3]

	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	S += c_t4_t1_t4_in >= 61
	c_t4_t1_t4_in += MM_in[1]

	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem0 >= 61
	c_t4_t1_t4_mem0 += MAS_MEM[10]

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem1 >= 61
	c_t4_t1_t4_mem1 += MAS_MEM[3]

	c_t4_t31 = S.Task('c_t4_t31', length=2, delay_cost=1)
	S += c_t4_t31 >= 61
	c_t4_t31 += MAS[3]

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=9, delay_cost=1)
	S += c_t5_t0_t4 >= 61
	c_t5_t0_t4 += MM[0]

	c_t5_t30 = S.Task('c_t5_t30', length=2, delay_cost=1)
	S += c_t5_t30 >= 61
	c_t5_t30 += MAS[0]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 61
	c_t5_t31_in += MAS_in[2]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 61
	c_t5_t31_mem0 += MAS_MEM[8]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 61
	c_t5_t31_mem1 += MAS_MEM[11]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=9, delay_cost=1)
	S += c_t2_t4_t0 >= 62
	c_t2_t4_t0 += MM[0]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 62
	c_t2_t4_t2_in += MAS_in[4]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 62
	c_t2_t4_t2_mem0 += MAS_MEM[4]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 62
	c_t2_t4_t2_mem1 += MAS_MEM[7]

	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	S += c_t4_t00_in >= 62
	c_t4_t00_in += MAS_in[2]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 62
	c_t4_t00_mem0 += MM_MEM[2]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 62
	c_t4_t00_mem1 += MM_MEM[3]

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=2, delay_cost=1)
	S += c_t4_t0_t5 >= 62
	c_t4_t0_t5 += MAS[4]

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=9, delay_cost=1)
	S += c_t4_t1_t4 >= 62
	c_t4_t1_t4 += MM[1]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 62
	c_t5_t1_t2_in += MAS_in[1]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 62
	c_t5_t1_t2_mem0 += MAS_MEM[10]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 62
	c_t5_t1_t2_mem1 += MAS_MEM[11]

	c_t5_t31 = S.Task('c_t5_t31', length=2, delay_cost=1)
	S += c_t5_t31 >= 62
	c_t5_t31 += MAS[2]

	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	S += c_t5_t4_t0_in >= 62
	c_t5_t4_t0_in += MM_in[0]

	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem0 >= 62
	c_t5_t4_t0_mem0 += MAS_MEM[6]

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem1 >= 62
	c_t5_t4_t0_mem1 += MAS_MEM[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=2, delay_cost=1)
	S += c_t2_t4_t2 >= 63
	c_t2_t4_t2 += MAS[4]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 63
	c_t3_t10_in += MAS_in[0]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 63
	c_t3_t10_mem0 += MM_MEM[2]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 63
	c_t3_t10_mem1 += MM_MEM[3]

	c_t4_t00 = S.Task('c_t4_t00', length=2, delay_cost=1)
	S += c_t4_t00 >= 63
	c_t4_t00 += MAS[2]

	c_t4_t01_in = S.Task('c_t4_t01_in', length=1, delay_cost=1)
	S += c_t4_t01_in >= 63
	c_t4_t01_in += MAS_in[2]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 63
	c_t4_t01_mem0 += MM_MEM[0]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 63
	c_t4_t01_mem1 += MAS_MEM[9]

	c_t4_t4_t3_in = S.Task('c_t4_t4_t3_in', length=1, delay_cost=1)
	S += c_t4_t4_t3_in >= 63
	c_t4_t4_t3_in += MAS_in[4]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem0 >= 63
	c_t4_t4_t3_mem0 += MAS_MEM[2]

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem1 >= 63
	c_t4_t4_t3_mem1 += MAS_MEM[7]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 63
	c_t5_t1_t1_in += MM_in[1]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 63
	c_t5_t1_t1_mem0 += MAS_MEM[10]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 63
	c_t5_t1_t1_mem1 += MAS_MEM[11]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=2, delay_cost=1)
	S += c_t5_t1_t2 >= 63
	c_t5_t1_t2 += MAS[1]

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=9, delay_cost=1)
	S += c_t5_t4_t0 >= 63
	c_t5_t4_t0 += MM[0]

	c_t5_t4_t3_in = S.Task('c_t5_t4_t3_in', length=1, delay_cost=1)
	S += c_t5_t4_t3_in >= 63
	c_t5_t4_t3_in += MAS_in[5]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem0 >= 63
	c_t5_t4_t3_mem0 += MAS_MEM[0]

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem1 >= 63
	c_t5_t4_t3_mem1 += MAS_MEM[5]

	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	S += c_t2_t4_t4_in >= 64
	c_t2_t4_t4_in += MM_in[0]

	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem0 >= 64
	c_t2_t4_t4_mem0 += MAS_MEM[8]

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem1 >= 64
	c_t2_t4_t4_mem1 += MAS_MEM[7]

	c_t3_t10 = S.Task('c_t3_t10', length=2, delay_cost=1)
	S += c_t3_t10 >= 64
	c_t3_t10 += MAS[0]

	c_t3_t4_t5_in = S.Task('c_t3_t4_t5_in', length=1, delay_cost=1)
	S += c_t3_t4_t5_in >= 64
	c_t3_t4_t5_in += MAS_in[2]

	c_t3_t4_t5_mem0 = S.Task('c_t3_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem0 >= 64
	c_t3_t4_t5_mem0 += MM_MEM[0]

	c_t3_t4_t5_mem1 = S.Task('c_t3_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem1 >= 64
	c_t3_t4_t5_mem1 += MM_MEM[1]

	c_t4_t01 = S.Task('c_t4_t01', length=2, delay_cost=1)
	S += c_t4_t01 >= 64
	c_t4_t01 += MAS[2]

	c_t4_t1_t5_in = S.Task('c_t4_t1_t5_in', length=1, delay_cost=1)
	S += c_t4_t1_t5_in >= 64
	c_t4_t1_t5_in += MAS_in[4]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem0 >= 64
	c_t4_t1_t5_mem0 += MM_MEM[2]

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem1 >= 64
	c_t4_t1_t5_mem1 += MM_MEM[3]

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=2, delay_cost=1)
	S += c_t4_t4_t3 >= 64
	c_t4_t4_t3 += MAS[4]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=9, delay_cost=1)
	S += c_t5_t1_t1 >= 64
	c_t5_t1_t1 += MM[1]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 64
	c_t5_t21_in += MAS_in[3]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 64
	c_t5_t21_mem0 += MAS_MEM[2]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 64
	c_t5_t21_mem1 += MAS_MEM[11]

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=2, delay_cost=1)
	S += c_t5_t4_t3 >= 64
	c_t5_t4_t3 += MAS[5]

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=9, delay_cost=1)
	S += c_t2_t4_t4 >= 65
	c_t2_t4_t4 += MM[0]

	c_t3_t40_in = S.Task('c_t3_t40_in', length=1, delay_cost=1)
	S += c_t3_t40_in >= 65
	c_t3_t40_in += MAS_in[5]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	S += c_t3_t40_mem0 >= 65
	c_t3_t40_mem0 += MM_MEM[0]

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	S += c_t3_t40_mem1 >= 65
	c_t3_t40_mem1 += MM_MEM[1]

	c_t3_t4_t5 = S.Task('c_t3_t4_t5', length=2, delay_cost=1)
	S += c_t3_t4_t5 >= 65
	c_t3_t4_t5 += MAS[2]

	c_t3_t50_in = S.Task('c_t3_t50_in', length=1, delay_cost=1)
	S += c_t3_t50_in >= 65
	c_t3_t50_in += MAS_in[0]

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	S += c_t3_t50_mem0 >= 65
	c_t3_t50_mem0 += MAS_MEM[4]

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	S += c_t3_t50_mem1 >= 65
	c_t3_t50_mem1 += MAS_MEM[1]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 65
	c_t4_t10_in += MAS_in[4]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 65
	c_t4_t10_mem0 += MM_MEM[2]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 65
	c_t4_t10_mem1 += MM_MEM[3]

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=2, delay_cost=1)
	S += c_t4_t1_t5 >= 65
	c_t4_t1_t5 += MAS[4]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 65
	c_t4_t21_in += MAS_in[2]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 65
	c_t4_t21_mem0 += MAS_MEM[10]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 65
	c_t4_t21_mem1 += MAS_MEM[11]

	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	S += c_t5_t1_t4_in >= 65
	c_t5_t1_t4_in += MM_in[0]

	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem0 >= 65
	c_t5_t1_t4_mem0 += MAS_MEM[2]

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem1 >= 65
	c_t5_t1_t4_mem1 += MAS_MEM[3]

	c_t5_t21 = S.Task('c_t5_t21', length=2, delay_cost=1)
	S += c_t5_t21 >= 65
	c_t5_t21 += MAS[3]

	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	S += c_t3_t1_t4_in >= 66
	c_t3_t1_t4_in += MM_in[0]

	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem0 >= 66
	c_t3_t1_t4_mem0 += MAS_MEM[8]

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem1 >= 66
	c_t3_t1_t4_mem1 += MAS_MEM[11]

	c_t3_t40 = S.Task('c_t3_t40', length=2, delay_cost=1)
	S += c_t3_t40 >= 66
	c_t3_t40 += MAS[5]

	c_t3_t50 = S.Task('c_t3_t50', length=2, delay_cost=1)
	S += c_t3_t50 >= 66
	c_t3_t50 += MAS[0]

	c_t4_t10 = S.Task('c_t4_t10', length=2, delay_cost=1)
	S += c_t4_t10 >= 66
	c_t4_t10 += MAS[4]

	c_t4_t21 = S.Task('c_t4_t21', length=2, delay_cost=1)
	S += c_t4_t21 >= 66
	c_t4_t21 += MAS[2]

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=9, delay_cost=1)
	S += c_t5_t1_t4 >= 66
	c_t5_t1_t4 += MM[0]

	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	S += c_t5_t4_t1_in >= 66
	c_t5_t4_t1_in += MM_in[1]

	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem0 >= 66
	c_t5_t4_t1_mem0 += MAS_MEM[6]

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem1 >= 66
	c_t5_t4_t1_mem1 += MAS_MEM[5]

	c_t310_in = S.Task('c_t310_in', length=1, delay_cost=1)
	S += c_t310_in >= 67
	c_t310_in += MAS_in[3]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 67
	c_t310_mem0 += MAS_MEM[10]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 67
	c_t310_mem1 += MAS_MEM[1]

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=9, delay_cost=1)
	S += c_t3_t1_t4 >= 67
	c_t3_t1_t4 += MM[0]

	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	S += c_t4_t4_t1_in >= 67
	c_t4_t4_t1_in += MM_in[1]

	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem0 >= 67
	c_t4_t4_t1_mem0 += MAS_MEM[4]

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem1 >= 67
	c_t4_t4_t1_mem1 += MAS_MEM[7]

	c_t4_t4_t2_in = S.Task('c_t4_t4_t2_in', length=1, delay_cost=1)
	S += c_t4_t4_t2_in >= 67
	c_t4_t4_t2_in += MAS_in[4]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem0 >= 67
	c_t4_t4_t2_mem0 += MAS_MEM[2]

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem1 >= 67
	c_t4_t4_t2_mem1 += MAS_MEM[5]

	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	S += c_t5_t00_in >= 67
	c_t5_t00_in += MAS_in[1]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 67
	c_t5_t00_mem0 += MM_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 67
	c_t5_t00_mem1 += MM_MEM[3]

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=9, delay_cost=1)
	S += c_t5_t4_t1 >= 67
	c_t5_t4_t1 += MM[1]

	c_t310 = S.Task('c_t310', length=2, delay_cost=1)
	S += c_t310 >= 68
	c_t310 += MAS[3]

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=9, delay_cost=1)
	S += c_t4_t4_t1 >= 68
	c_t4_t4_t1 += MM[1]

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=2, delay_cost=1)
	S += c_t4_t4_t2 >= 68
	c_t4_t4_t2 += MAS[4]

	c_t4_t50_in = S.Task('c_t4_t50_in', length=1, delay_cost=1)
	S += c_t4_t50_in >= 68
	c_t4_t50_in += MAS_in[4]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	S += c_t4_t50_mem0 >= 68
	c_t4_t50_mem0 += MAS_MEM[4]

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	S += c_t4_t50_mem1 >= 68
	c_t4_t50_mem1 += MAS_MEM[9]

	c_t5_t00 = S.Task('c_t5_t00', length=2, delay_cost=1)
	S += c_t5_t00 >= 68
	c_t5_t00 += MAS[1]

	c_t5_t0_t5_in = S.Task('c_t5_t0_t5_in', length=1, delay_cost=1)
	S += c_t5_t0_t5_in >= 68
	c_t5_t0_t5_in += MAS_in[0]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem0 >= 68
	c_t5_t0_t5_mem0 += MM_MEM[0]

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem1 >= 68
	c_t5_t0_t5_mem1 += MM_MEM[3]

	c_t5_t4_t2_in = S.Task('c_t5_t4_t2_in', length=1, delay_cost=1)
	S += c_t5_t4_t2_in >= 68
	c_t5_t4_t2_in += MAS_in[1]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem0 >= 68
	c_t5_t4_t2_mem0 += MAS_MEM[6]

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem1 >= 68
	c_t5_t4_t2_mem1 += MAS_MEM[7]

	c_t3_t4_t4_in = S.Task('c_t3_t4_t4_in', length=1, delay_cost=1)
	S += c_t3_t4_t4_in >= 69
	c_t3_t4_t4_in += MM_in[1]

	c_t3_t4_t4_mem0 = S.Task('c_t3_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem0 >= 69
	c_t3_t4_t4_mem0 += MAS_MEM[4]

	c_t3_t4_t4_mem1 = S.Task('c_t3_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem1 >= 69
	c_t3_t4_t4_mem1 += MAS_MEM[11]

	c_t4_t4_t4_in = S.Task('c_t4_t4_t4_in', length=1, delay_cost=1)
	S += c_t4_t4_t4_in >= 69
	c_t4_t4_t4_in += MM_in[0]

	c_t4_t4_t4_mem0 = S.Task('c_t4_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem0 >= 69
	c_t4_t4_t4_mem0 += MAS_MEM[8]

	c_t4_t4_t4_mem1 = S.Task('c_t4_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem1 >= 69
	c_t4_t4_t4_mem1 += MAS_MEM[9]

	c_t4_t50 = S.Task('c_t4_t50', length=2, delay_cost=1)
	S += c_t4_t50 >= 69
	c_t4_t50 += MAS[4]

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=2, delay_cost=1)
	S += c_t5_t0_t5 >= 69
	c_t5_t0_t5 += MAS[0]

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=2, delay_cost=1)
	S += c_t5_t4_t2 >= 69
	c_t5_t4_t2 += MAS[1]

	c_t610_in = S.Task('c_t610_in', length=1, delay_cost=1)
	S += c_t610_in >= 69
	c_t610_in += MAS_in[2]

	c_t610_mem0 = S.Task('c_t610_mem0', length=1, delay_cost=1)
	S += c_t610_mem0 >= 69
	c_t610_mem0 += MAS_MEM[6]

	c_t610_mem1 = S.Task('c_t610_mem1', length=1, delay_cost=1)
	S += c_t610_mem1 >= 69
	c_t610_mem1 += MAS_MEM[3]

	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	S += c_t2_t40_in >= 70
	c_t2_t40_in += MAS_in[1]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 70
	c_t2_t40_mem0 += MM_MEM[0]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 70
	c_t2_t40_mem1 += MM_MEM[3]

	c_t3_t4_t4 = S.Task('c_t3_t4_t4', length=9, delay_cost=1)
	S += c_t3_t4_t4 >= 70
	c_t3_t4_t4 += MM[1]

	c_t4_t11_in = S.Task('c_t4_t11_in', length=1, delay_cost=1)
	S += c_t4_t11_in >= 70
	c_t4_t11_in += MAS_in[0]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 70
	c_t4_t11_mem0 += MM_MEM[2]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 70
	c_t4_t11_mem1 += MAS_MEM[9]

	c_t4_t4_t4 = S.Task('c_t4_t4_t4', length=9, delay_cost=1)
	S += c_t4_t4_t4 >= 70
	c_t4_t4_t4 += MM[0]

	c_t5_t4_t4_in = S.Task('c_t5_t4_t4_in', length=1, delay_cost=1)
	S += c_t5_t4_t4_in >= 70
	c_t5_t4_t4_in += MM_in[1]

	c_t5_t4_t4_mem0 = S.Task('c_t5_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem0 >= 70
	c_t5_t4_t4_mem0 += MAS_MEM[2]

	c_t5_t4_t4_mem1 = S.Task('c_t5_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem1 >= 70
	c_t5_t4_t4_mem1 += MAS_MEM[11]

	c_t610 = S.Task('c_t610', length=2, delay_cost=1)
	S += c_t610 >= 70
	c_t610 += MAS[2]

	c_t2_t40 = S.Task('c_t2_t40', length=2, delay_cost=1)
	S += c_t2_t40 >= 71
	c_t2_t40 += MAS[1]

	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	S += c_t2_t4_t5_in >= 71
	c_t2_t4_t5_in += MAS_in[0]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem0 >= 71
	c_t2_t4_t5_mem0 += MM_MEM[0]

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem1 >= 71
	c_t2_t4_t5_mem1 += MM_MEM[3]

	c_t4_t11 = S.Task('c_t4_t11', length=2, delay_cost=1)
	S += c_t4_t11 >= 71
	c_t4_t11 += MAS[0]

	c_t5_t4_t4 = S.Task('c_t5_t4_t4', length=9, delay_cost=1)
	S += c_t5_t4_t4 >= 71
	c_t5_t4_t4 += MM[1]

	c_t210_in = S.Task('c_t210_in', length=1, delay_cost=1)
	S += c_t210_in >= 72
	c_t210_in += MAS_in[2]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 72
	c_t210_mem0 += MAS_MEM[2]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 72
	c_t210_mem1 += MAS_MEM[3]

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=2, delay_cost=1)
	S += c_t2_t4_t5 >= 72
	c_t2_t4_t5 += MAS[0]

	c_t4_s01_in = S.Task('c_t4_s01_in', length=1, delay_cost=1)
	S += c_t4_s01_in >= 72
	c_t4_s01_in += MAS_in[1]

	c_t4_s01_mem0 = S.Task('c_t4_s01_mem0', length=1, delay_cost=1)
	S += c_t4_s01_mem0 >= 72
	c_t4_s01_mem0 += MAS_MEM[0]

	c_t4_s01_mem1 = S.Task('c_t4_s01_mem1', length=1, delay_cost=1)
	S += c_t4_s01_mem1 >= 72
	c_t4_s01_mem1 += MAS_MEM[9]

	c_t4_t51_in = S.Task('c_t4_t51_in', length=1, delay_cost=1)
	S += c_t4_t51_in >= 72
	c_t4_t51_in += MAS_in[0]

	c_t4_t51_mem0 = S.Task('c_t4_t51_mem0', length=1, delay_cost=1)
	S += c_t4_t51_mem0 >= 72
	c_t4_t51_mem0 += MAS_MEM[4]

	c_t4_t51_mem1 = S.Task('c_t4_t51_mem1', length=1, delay_cost=1)
	S += c_t4_t51_mem1 >= 72
	c_t4_t51_mem1 += MAS_MEM[1]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 72
	c_t5_t10_in += MAS_in[4]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 72
	c_t5_t10_mem0 += MM_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 72
	c_t5_t10_mem1 += MM_MEM[3]

	c_t210 = S.Task('c_t210', length=2, delay_cost=1)
	S += c_t210 >= 73
	c_t210 += MAS[2]

	c_t4_s00_in = S.Task('c_t4_s00_in', length=1, delay_cost=1)
	S += c_t4_s00_in >= 73
	c_t4_s00_in += MAS_in[1]

	c_t4_s00_mem0 = S.Task('c_t4_s00_mem0', length=1, delay_cost=1)
	S += c_t4_s00_mem0 >= 73
	c_t4_s00_mem0 += MAS_MEM[8]

	c_t4_s00_mem1 = S.Task('c_t4_s00_mem1', length=1, delay_cost=1)
	S += c_t4_s00_mem1 >= 73
	c_t4_s00_mem1 += MAS_MEM[1]

	c_t4_s01 = S.Task('c_t4_s01', length=2, delay_cost=1)
	S += c_t4_s01 >= 73
	c_t4_s01 += MAS[1]

	c_t4_t51 = S.Task('c_t4_t51', length=2, delay_cost=1)
	S += c_t4_t51 >= 73
	c_t4_t51 += MAS[0]

	c_t5_t10 = S.Task('c_t5_t10', length=2, delay_cost=1)
	S += c_t5_t10 >= 73
	c_t5_t10 += MAS[4]

	c_t5_t1_t5_in = S.Task('c_t5_t1_t5_in', length=1, delay_cost=1)
	S += c_t5_t1_t5_in >= 73
	c_t5_t1_t5_in += MAS_in[0]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem0 >= 73
	c_t5_t1_t5_mem0 += MM_MEM[0]

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem1 >= 73
	c_t5_t1_t5_mem1 += MM_MEM[3]

	c_t401_in = S.Task('c_t401_in', length=1, delay_cost=1)
	S += c_t401_in >= 74
	c_t401_in += MAS_in[2]

	c_t401_mem0 = S.Task('c_t401_mem0', length=1, delay_cost=1)
	S += c_t401_mem0 >= 74
	c_t401_mem0 += MAS_MEM[4]

	c_t401_mem1 = S.Task('c_t401_mem1', length=1, delay_cost=1)
	S += c_t401_mem1 >= 74
	c_t401_mem1 += MAS_MEM[3]

	c_t4_s00 = S.Task('c_t4_s00', length=2, delay_cost=1)
	S += c_t4_s00 >= 74
	c_t4_s00 += MAS[1]

	c_t5_t01_in = S.Task('c_t5_t01_in', length=1, delay_cost=1)
	S += c_t5_t01_in >= 74
	c_t5_t01_in += MAS_in[4]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 74
	c_t5_t01_mem0 += MM_MEM[0]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 74
	c_t5_t01_mem1 += MAS_MEM[1]

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=2, delay_cost=1)
	S += c_t5_t1_t5 >= 74
	c_t5_t1_t5 += MAS[0]

	c_t5_t50_in = S.Task('c_t5_t50_in', length=1, delay_cost=1)
	S += c_t5_t50_in >= 74
	c_t5_t50_in += MAS_in[5]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	S += c_t5_t50_mem0 >= 74
	c_t5_t50_mem0 += MAS_MEM[2]

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	S += c_t5_t50_mem1 >= 74
	c_t5_t50_mem1 += MAS_MEM[9]

	c_t7010_in = S.Task('c_t7010_in', length=1, delay_cost=1)
	S += c_t7010_in >= 74
	c_t7010_in += MAS_in[1]

	c_t7010_mem0 = S.Task('c_t7010_mem0', length=1, delay_cost=1)
	S += c_t7010_mem0 >= 74
	c_t7010_mem0 += MAS_MEM[10]

	c_t7010_mem1 = S.Task('c_t7010_mem1', length=1, delay_cost=1)
	S += c_t7010_mem1 >= 74
	c_t7010_mem1 += MAS_MEM[5]

	c_t401 = S.Task('c_t401', length=2, delay_cost=1)
	S += c_t401 >= 75
	c_t401 += MAS[2]

	c_t5_t01 = S.Task('c_t5_t01', length=2, delay_cost=1)
	S += c_t5_t01 >= 75
	c_t5_t01 += MAS[4]

	c_t5_t40_in = S.Task('c_t5_t40_in', length=1, delay_cost=1)
	S += c_t5_t40_in >= 75
	c_t5_t40_in += MAS_in[4]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	S += c_t5_t40_mem0 >= 75
	c_t5_t40_mem0 += MM_MEM[0]

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	S += c_t5_t40_mem1 >= 75
	c_t5_t40_mem1 += MM_MEM[3]

	c_t5_t50 = S.Task('c_t5_t50', length=2, delay_cost=1)
	S += c_t5_t50 >= 75
	c_t5_t50 += MAS[5]

	c_t7010 = S.Task('c_t7010', length=2, delay_cost=1)
	S += c_t7010 >= 75
	c_t7010 += MAS[1]

	c_t8010_in = S.Task('c_t8010_in', length=1, delay_cost=1)
	S += c_t8010_in >= 75
	c_t8010_in += MAS_in[3]

	c_t8010_mem0 = S.Task('c_t8010_mem0', length=1, delay_cost=1)
	S += c_t8010_mem0 >= 75
	c_t8010_mem0 += MAS_MEM[4]

	c_t8010_mem1 = S.Task('c_t8010_mem1', length=1, delay_cost=1)
	S += c_t8010_mem1 >= 75
	c_t8010_mem1 += MAS_MEM[9]

	c_t3_t11_in = S.Task('c_t3_t11_in', length=1, delay_cost=1)
	S += c_t3_t11_in >= 76
	c_t3_t11_in += MAS_in[1]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 76
	c_t3_t11_mem0 += MM_MEM[0]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 76
	c_t3_t11_mem1 += MAS_MEM[9]

	c_t400_in = S.Task('c_t400_in', length=1, delay_cost=1)
	S += c_t400_in >= 76
	c_t400_in += MAS_in[4]

	c_t400_mem0 = S.Task('c_t400_mem0', length=1, delay_cost=1)
	S += c_t400_mem0 >= 76
	c_t400_mem0 += MAS_MEM[4]

	c_t400_mem1 = S.Task('c_t400_mem1', length=1, delay_cost=1)
	S += c_t400_mem1 >= 76
	c_t400_mem1 += MAS_MEM[3]

	c_t4_t40_in = S.Task('c_t4_t40_in', length=1, delay_cost=1)
	S += c_t4_t40_in >= 76
	c_t4_t40_in += MAS_in[5]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	S += c_t4_t40_mem0 >= 76
	c_t4_t40_mem0 += MM_MEM[2]

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	S += c_t4_t40_mem1 >= 76
	c_t4_t40_mem1 += MM_MEM[3]

	c_t5_t40 = S.Task('c_t5_t40', length=2, delay_cost=1)
	S += c_t5_t40 >= 76
	c_t5_t40 += MAS[4]

	c_t8010 = S.Task('c_t8010', length=2, delay_cost=1)
	S += c_t8010 >= 76
	c_t8010 += MAS[3]

	c_t2_t41_in = S.Task('c_t2_t41_in', length=1, delay_cost=1)
	S += c_t2_t41_in >= 77
	c_t2_t41_in += MAS_in[1]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 77
	c_t2_t41_mem0 += MM_MEM[0]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 77
	c_t2_t41_mem1 += MAS_MEM[1]

	c_t3_t11 = S.Task('c_t3_t11', length=2, delay_cost=1)
	S += c_t3_t11 >= 77
	c_t3_t11 += MAS[1]

	c_t400 = S.Task('c_t400', length=2, delay_cost=1)
	S += c_t400 >= 77
	c_t400 += MAS[4]

	c_t4_t40 = S.Task('c_t4_t40', length=2, delay_cost=1)
	S += c_t4_t40 >= 77
	c_t4_t40 += MAS[5]

	c_t4_t4_t5_in = S.Task('c_t4_t4_t5_in', length=1, delay_cost=1)
	S += c_t4_t4_t5_in >= 77
	c_t4_t4_t5_in += MAS_in[2]

	c_t4_t4_t5_mem0 = S.Task('c_t4_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem0 >= 77
	c_t4_t4_t5_mem0 += MM_MEM[2]

	c_t4_t4_t5_mem1 = S.Task('c_t4_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem1 >= 77
	c_t4_t4_t5_mem1 += MM_MEM[3]

	c_t510_in = S.Task('c_t510_in', length=1, delay_cost=1)
	S += c_t510_in >= 77
	c_t510_in += MAS_in[4]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	S += c_t510_mem0 >= 77
	c_t510_mem0 += MAS_MEM[8]

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	S += c_t510_mem1 >= 77
	c_t510_mem1 += MAS_MEM[11]

	c_t2_t41 = S.Task('c_t2_t41', length=2, delay_cost=1)
	S += c_t2_t41 >= 78
	c_t2_t41 += MAS[1]

	c_t3_s00_in = S.Task('c_t3_s00_in', length=1, delay_cost=1)
	S += c_t3_s00_in >= 78
	c_t3_s00_in += MAS_in[0]

	c_t3_s00_mem0 = S.Task('c_t3_s00_mem0', length=1, delay_cost=1)
	S += c_t3_s00_mem0 >= 78
	c_t3_s00_mem0 += MAS_MEM[0]

	c_t3_s00_mem1 = S.Task('c_t3_s00_mem1', length=1, delay_cost=1)
	S += c_t3_s00_mem1 >= 78
	c_t3_s00_mem1 += MAS_MEM[3]

	c_t3_s01_in = S.Task('c_t3_s01_in', length=1, delay_cost=1)
	S += c_t3_s01_in >= 78
	c_t3_s01_in += MAS_in[3]

	c_t3_s01_mem0 = S.Task('c_t3_s01_mem0', length=1, delay_cost=1)
	S += c_t3_s01_mem0 >= 78
	c_t3_s01_mem0 += MAS_MEM[2]

	c_t3_s01_mem1 = S.Task('c_t3_s01_mem1', length=1, delay_cost=1)
	S += c_t3_s01_mem1 >= 78
	c_t3_s01_mem1 += MAS_MEM[1]

	c_t3_t41_in = S.Task('c_t3_t41_in', length=1, delay_cost=1)
	S += c_t3_t41_in >= 78
	c_t3_t41_in += MAS_in[1]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	S += c_t3_t41_mem0 >= 78
	c_t3_t41_mem0 += MM_MEM[2]

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	S += c_t3_t41_mem1 >= 78
	c_t3_t41_mem1 += MAS_MEM[5]

	c_t410_in = S.Task('c_t410_in', length=1, delay_cost=1)
	S += c_t410_in >= 78
	c_t410_in += MAS_in[5]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	S += c_t410_mem0 >= 78
	c_t410_mem0 += MAS_MEM[10]

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	S += c_t410_mem1 >= 78
	c_t410_mem1 += MAS_MEM[9]

	c_t4_t4_t5 = S.Task('c_t4_t4_t5', length=2, delay_cost=1)
	S += c_t4_t4_t5 >= 78
	c_t4_t4_t5 += MAS[2]

	c_t510 = S.Task('c_t510', length=2, delay_cost=1)
	S += c_t510 >= 78
	c_t510 += MAS[4]

	c_t5_t4_t5_in = S.Task('c_t5_t4_t5_in', length=1, delay_cost=1)
	S += c_t5_t4_t5_in >= 78
	c_t5_t4_t5_in += MAS_in[4]

	c_t5_t4_t5_mem0 = S.Task('c_t5_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem0 >= 78
	c_t5_t4_t5_mem0 += MM_MEM[0]

	c_t5_t4_t5_mem1 = S.Task('c_t5_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem1 >= 78
	c_t5_t4_t5_mem1 += MM_MEM[3]

	c_t211_in = S.Task('c_t211_in', length=1, delay_cost=1)
	S += c_t211_in >= 79
	c_t211_in += MAS_in[3]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 79
	c_t211_mem0 += MAS_MEM[2]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 79
	c_t211_mem1 += MAS_MEM[5]

	c_t3_s00 = S.Task('c_t3_s00', length=2, delay_cost=1)
	S += c_t3_s00 >= 79
	c_t3_s00 += MAS[0]

	c_t3_s01 = S.Task('c_t3_s01', length=2, delay_cost=1)
	S += c_t3_s01 >= 79
	c_t3_s01 += MAS[3]

	c_t3_t41 = S.Task('c_t3_t41', length=2, delay_cost=1)
	S += c_t3_t41 >= 79
	c_t3_t41 += MAS[1]

	c_t3_t51_in = S.Task('c_t3_t51_in', length=1, delay_cost=1)
	S += c_t3_t51_in >= 79
	c_t3_t51_in += MAS_in[1]

	c_t3_t51_mem0 = S.Task('c_t3_t51_mem0', length=1, delay_cost=1)
	S += c_t3_t51_mem0 >= 79
	c_t3_t51_mem0 += MAS_MEM[0]

	c_t3_t51_mem1 = S.Task('c_t3_t51_mem1', length=1, delay_cost=1)
	S += c_t3_t51_mem1 >= 79
	c_t3_t51_mem1 += MAS_MEM[3]

	c_t410 = S.Task('c_t410', length=2, delay_cost=1)
	S += c_t410 >= 79
	c_t410 += MAS[5]

	c_t5_t11_in = S.Task('c_t5_t11_in', length=1, delay_cost=1)
	S += c_t5_t11_in >= 79
	c_t5_t11_in += MAS_in[5]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 79
	c_t5_t11_mem0 += MM_MEM[0]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 79
	c_t5_t11_mem1 += MAS_MEM[1]

	c_t5_t4_t5 = S.Task('c_t5_t4_t5', length=2, delay_cost=1)
	S += c_t5_t4_t5 >= 79
	c_t5_t4_t5 += MAS[4]

	c_t810_in = S.Task('c_t810_in', length=1, delay_cost=1)
	S += c_t810_in >= 79
	c_t810_in += MAS_in[2]

	c_t810_mem0 = S.Task('c_t810_mem0', length=1, delay_cost=1)
	S += c_t810_mem0 >= 79
	c_t810_mem0 += MAS_MEM[8]

	c_t810_mem1 = S.Task('c_t810_mem1', length=1, delay_cost=1)
	S += c_t810_mem1 >= 79
	c_t810_mem1 += MAS_MEM[7]

	c_t211 = S.Task('c_t211', length=2, delay_cost=1)
	S += c_t211 >= 80
	c_t211 += MAS[3]

	c_t300_in = S.Task('c_t300_in', length=1, delay_cost=1)
	S += c_t300_in >= 80
	c_t300_in += MAS_in[4]

	c_t300_mem0 = S.Task('c_t300_mem0', length=1, delay_cost=1)
	S += c_t300_mem0 >= 80
	c_t300_mem0 += MAS_MEM[4]

	c_t300_mem1 = S.Task('c_t300_mem1', length=1, delay_cost=1)
	S += c_t300_mem1 >= 80
	c_t300_mem1 += MAS_MEM[1]

	c_t301_in = S.Task('c_t301_in', length=1, delay_cost=1)
	S += c_t301_in >= 80
	c_t301_in += MAS_in[3]

	c_t301_mem0 = S.Task('c_t301_mem0', length=1, delay_cost=1)
	S += c_t301_mem0 >= 80
	c_t301_mem0 += MAS_MEM[0]

	c_t301_mem1 = S.Task('c_t301_mem1', length=1, delay_cost=1)
	S += c_t301_mem1 >= 80
	c_t301_mem1 += MAS_MEM[7]

	c_t3_t51 = S.Task('c_t3_t51', length=2, delay_cost=1)
	S += c_t3_t51 >= 80
	c_t3_t51 += MAS[1]

	c_t4_t41_in = S.Task('c_t4_t41_in', length=1, delay_cost=1)
	S += c_t4_t41_in >= 80
	c_t4_t41_in += MAS_in[5]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	S += c_t4_t41_mem0 >= 80
	c_t4_t41_mem0 += MM_MEM[0]

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	S += c_t4_t41_mem1 >= 80
	c_t4_t41_mem1 += MAS_MEM[5]

	c_t5_t11 = S.Task('c_t5_t11', length=2, delay_cost=1)
	S += c_t5_t11 >= 80
	c_t5_t11 += MAS[5]

	c_t5_t41_in = S.Task('c_t5_t41_in', length=1, delay_cost=1)
	S += c_t5_t41_in >= 80
	c_t5_t41_in += MAS_in[2]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	S += c_t5_t41_mem0 >= 80
	c_t5_t41_mem0 += MM_MEM[2]

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	S += c_t5_t41_mem1 >= 80
	c_t5_t41_mem1 += MAS_MEM[9]

	c_t7110_in = S.Task('c_t7110_in', length=1, delay_cost=1)
	S += c_t7110_in >= 80
	c_t7110_in += MAS_in[0]

	c_t7110_mem0 = S.Task('c_t7110_mem0', length=1, delay_cost=1)
	S += c_t7110_mem0 >= 80
	c_t7110_mem0 += MAS_MEM[10]

	c_t7110_mem1 = S.Task('c_t7110_mem1', length=1, delay_cost=1)
	S += c_t7110_mem1 >= 80
	c_t7110_mem1 += MAS_MEM[3]

	c_t810 = S.Task('c_t810', length=2, delay_cost=1)
	S += c_t810 >= 80
	c_t810 += MAS[2]

	c_t300 = S.Task('c_t300', length=2, delay_cost=1)
	S += c_t300 >= 81
	c_t300 += MAS[4]

	c_t301 = S.Task('c_t301', length=2, delay_cost=1)
	S += c_t301 >= 81
	c_t301 += MAS[3]

	c_t311_in = S.Task('c_t311_in', length=1, delay_cost=1)
	S += c_t311_in >= 81
	c_t311_in += MAS_in[4]

	c_t311_mem0 = S.Task('c_t311_mem0', length=1, delay_cost=1)
	S += c_t311_mem0 >= 81
	c_t311_mem0 += MAS_MEM[2]

	c_t311_mem1 = S.Task('c_t311_mem1', length=1, delay_cost=1)
	S += c_t311_mem1 >= 81
	c_t311_mem1 += MAS_MEM[3]

	c_t4_t41 = S.Task('c_t4_t41', length=2, delay_cost=1)
	S += c_t4_t41 >= 81
	c_t4_t41 += MAS[5]

	c_t5_s00_in = S.Task('c_t5_s00_in', length=1, delay_cost=1)
	S += c_t5_s00_in >= 81
	c_t5_s00_in += MAS_in[0]

	c_t5_s00_mem0 = S.Task('c_t5_s00_mem0', length=1, delay_cost=1)
	S += c_t5_s00_mem0 >= 81
	c_t5_s00_mem0 += MAS_MEM[8]

	c_t5_s00_mem1 = S.Task('c_t5_s00_mem1', length=1, delay_cost=1)
	S += c_t5_s00_mem1 >= 81
	c_t5_s00_mem1 += MAS_MEM[11]

	c_t5_s01_in = S.Task('c_t5_s01_in', length=1, delay_cost=1)
	S += c_t5_s01_in >= 81
	c_t5_s01_in += MAS_in[2]

	c_t5_s01_mem0 = S.Task('c_t5_s01_mem0', length=1, delay_cost=1)
	S += c_t5_s01_mem0 >= 81
	c_t5_s01_mem0 += MAS_MEM[10]

	c_t5_s01_mem1 = S.Task('c_t5_s01_mem1', length=1, delay_cost=1)
	S += c_t5_s01_mem1 >= 81
	c_t5_s01_mem1 += MAS_MEM[9]

	c_t5_t41 = S.Task('c_t5_t41', length=2, delay_cost=1)
	S += c_t5_t41 >= 81
	c_t5_t41 += MAS[2]

	c_t7011_in = S.Task('c_t7011_in', length=1, delay_cost=1)
	S += c_t7011_in >= 81
	c_t7011_in += MAS_in[5]

	c_t7011_mem0 = S.Task('c_t7011_mem0', length=1, delay_cost=1)
	S += c_t7011_mem0 >= 81
	c_t7011_mem0 += MAS_MEM[0]

	c_t7011_mem1 = S.Task('c_t7011_mem1', length=1, delay_cost=1)
	S += c_t7011_mem1 >= 81
	c_t7011_mem1 += MAS_MEM[7]

	c_t7110 = S.Task('c_t7110', length=2, delay_cost=1)
	S += c_t7110 >= 81
	c_t7110 += MAS[0]

	c_t8011_in = S.Task('c_t8011_in', length=1, delay_cost=1)
	S += c_t8011_in >= 81
	c_t8011_in += MAS_in[1]

	c_t8011_mem0 = S.Task('c_t8011_mem0', length=1, delay_cost=1)
	S += c_t8011_mem0 >= 81
	c_t8011_mem0 += MAS_MEM[6]

	c_t8011_mem1 = S.Task('c_t8011_mem1', length=1, delay_cost=1)
	S += c_t8011_mem1 >= 81
	c_t8011_mem1 += MAS_MEM[1]

	c_t311 = S.Task('c_t311', length=2, delay_cost=1)
	S += c_t311 >= 82
	c_t311 += MAS[4]

	c_t411_in = S.Task('c_t411_in', length=1, delay_cost=1)
	S += c_t411_in >= 82
	c_t411_in += MAS_in[5]

	c_t411_mem0 = S.Task('c_t411_mem0', length=1, delay_cost=1)
	S += c_t411_mem0 >= 82
	c_t411_mem0 += MAS_MEM[10]

	c_t411_mem1 = S.Task('c_t411_mem1', length=1, delay_cost=1)
	S += c_t411_mem1 >= 82
	c_t411_mem1 += MAS_MEM[1]

	c_t5_s00 = S.Task('c_t5_s00', length=2, delay_cost=1)
	S += c_t5_s00 >= 82
	c_t5_s00 += MAS[0]

	c_t5_s01 = S.Task('c_t5_s01', length=2, delay_cost=1)
	S += c_t5_s01 >= 82
	c_t5_s01 += MAS[2]

	c_t5_t51_in = S.Task('c_t5_t51_in', length=1, delay_cost=1)
	S += c_t5_t51_in >= 82
	c_t5_t51_in += MAS_in[2]

	c_t5_t51_mem0 = S.Task('c_t5_t51_mem0', length=1, delay_cost=1)
	S += c_t5_t51_mem0 >= 82
	c_t5_t51_mem0 += MAS_MEM[8]

	c_t5_t51_mem1 = S.Task('c_t5_t51_mem1', length=1, delay_cost=1)
	S += c_t5_t51_mem1 >= 82
	c_t5_t51_mem1 += MAS_MEM[11]

	c_t7011 = S.Task('c_t7011', length=2, delay_cost=1)
	S += c_t7011 >= 82
	c_t7011 += MAS[5]

	c_t8011 = S.Task('c_t8011', length=2, delay_cost=1)
	S += c_t8011 >= 82
	c_t8011 += MAS[1]

	c_t9_y1_0_in = S.Task('c_t9_y1_0_in', length=1, delay_cost=1)
	S += c_t9_y1_0_in >= 82
	c_t9_y1_0_in += MAS_in[3]

	c_t9_y1_0_mem0 = S.Task('c_t9_y1_0_mem0', length=1, delay_cost=1)
	S += c_t9_y1_0_mem0 >= 82
	c_t9_y1_0_mem0 += MAS_MEM[4]

	c_t9_y1_0_mem1 = S.Task('c_t9_y1_0_mem1', length=1, delay_cost=1)
	S += c_t9_y1_0_mem1 >= 82
	c_t9_y1_0_mem1 += MAS_MEM[7]

	c_t9_y1_1_in = S.Task('c_t9_y1_1_in', length=1, delay_cost=1)
	S += c_t9_y1_1_in >= 82
	c_t9_y1_1_in += MAS_in[4]

	c_t9_y1_1_mem0 = S.Task('c_t9_y1_1_mem0', length=1, delay_cost=1)
	S += c_t9_y1_1_mem0 >= 82
	c_t9_y1_1_mem0 += MAS_MEM[6]

	c_t9_y1_1_mem1 = S.Task('c_t9_y1_1_mem1', length=1, delay_cost=1)
	S += c_t9_y1_1_mem1 >= 82
	c_t9_y1_1_mem1 += MAS_MEM[5]

	c_t411 = S.Task('c_t411', length=2, delay_cost=1)
	S += c_t411 >= 83
	c_t411 += MAS[5]

	c_t500_in = S.Task('c_t500_in', length=1, delay_cost=1)
	S += c_t500_in >= 83
	c_t500_in += MAS_in[4]

	c_t500_mem0 = S.Task('c_t500_mem0', length=1, delay_cost=1)
	S += c_t500_mem0 >= 83
	c_t500_mem0 += MAS_MEM[2]

	c_t500_mem1 = S.Task('c_t500_mem1', length=1, delay_cost=1)
	S += c_t500_mem1 >= 83
	c_t500_mem1 += MAS_MEM[1]

	c_t501_in = S.Task('c_t501_in', length=1, delay_cost=1)
	S += c_t501_in >= 83
	c_t501_in += MAS_in[3]

	c_t501_mem0 = S.Task('c_t501_mem0', length=1, delay_cost=1)
	S += c_t501_mem0 >= 83
	c_t501_mem0 += MAS_MEM[8]

	c_t501_mem1 = S.Task('c_t501_mem1', length=1, delay_cost=1)
	S += c_t501_mem1 >= 83
	c_t501_mem1 += MAS_MEM[5]

	c_t5_t51 = S.Task('c_t5_t51', length=2, delay_cost=1)
	S += c_t5_t51 >= 83
	c_t5_t51 += MAS[2]

	c_t9_y1_0 = S.Task('c_t9_y1_0', length=2, delay_cost=1)
	S += c_t9_y1_0 >= 83
	c_t9_y1_0 += MAS[3]

	c_t9_y1_1 = S.Task('c_t9_y1_1', length=2, delay_cost=1)
	S += c_t9_y1_1 >= 83
	c_t9_y1_1 += MAS[4]

	c_t500 = S.Task('c_t500', length=2, delay_cost=1)
	S += c_t500 >= 84
	c_t500 += MAS[4]

	c_t501 = S.Task('c_t501', length=2, delay_cost=1)
	S += c_t501 >= 84
	c_t501 += MAS[3]

	c_t511_in = S.Task('c_t511_in', length=1, delay_cost=1)
	S += c_t511_in >= 84
	c_t511_in += MAS_in[0]

	c_t511_mem0 = S.Task('c_t511_mem0', length=1, delay_cost=1)
	S += c_t511_mem0 >= 84
	c_t511_mem0 += MAS_MEM[4]

	c_t511_mem1 = S.Task('c_t511_mem1', length=1, delay_cost=1)
	S += c_t511_mem1 >= 84
	c_t511_mem1 += MAS_MEM[5]

	c_t511 = S.Task('c_t511', length=2, delay_cost=1)
	S += c_t511 >= 85
	c_t511 += MAS[0]


	# new tasks
	c_t600 = S.Task('c_t600', length=2, delay_cost=1)
	c_t600 += alt(MAS)
	c_t600_in = S.Task('c_t600_in', length=1, delay_cost=1)
	c_t600_in += alt(MAS_in)
	S += c_t600_in*MAS_in[0]<=c_t600*MAS[0]

	S += c_t600_in*MAS_in[1]<=c_t600*MAS[1]

	S += c_t600_in*MAS_in[2]<=c_t600*MAS[2]

	S += c_t600_in*MAS_in[3]<=c_t600*MAS[3]

	S += c_t600_in*MAS_in[4]<=c_t600*MAS[4]

	S += c_t600_in*MAS_in[5]<=c_t600*MAS[5]

	c_t600_mem0 = S.Task('c_t600_mem0', length=1, delay_cost=1)
	c_t600_mem0 += MAS_MEM[8]
	S += 82 < c_t600_mem0
	S += c_t600_mem0 <= c_t600

	c_t600_mem1 = S.Task('c_t600_mem1', length=1, delay_cost=1)
	c_t600_mem1 += MAS_MEM[7]
	S += 54 < c_t600_mem1
	S += c_t600_mem1 <= c_t600

	c_t601 = S.Task('c_t601', length=2, delay_cost=1)
	c_t601 += alt(MAS)
	c_t601_in = S.Task('c_t601_in', length=1, delay_cost=1)
	c_t601_in += alt(MAS_in)
	S += c_t601_in*MAS_in[0]<=c_t601*MAS[0]

	S += c_t601_in*MAS_in[1]<=c_t601*MAS[1]

	S += c_t601_in*MAS_in[2]<=c_t601*MAS[2]

	S += c_t601_in*MAS_in[3]<=c_t601*MAS[3]

	S += c_t601_in*MAS_in[4]<=c_t601*MAS[4]

	S += c_t601_in*MAS_in[5]<=c_t601*MAS[5]

	c_t601_mem0 = S.Task('c_t601_mem0', length=1, delay_cost=1)
	c_t601_mem0 += MAS_MEM[6]
	S += 82 < c_t601_mem0
	S += c_t601_mem0 <= c_t601

	c_t601_mem1 = S.Task('c_t601_mem1', length=1, delay_cost=1)
	c_t601_mem1 += MAS_MEM[7]
	S += 51 < c_t601_mem1
	S += c_t601_mem1 <= c_t601

	c_t611 = S.Task('c_t611', length=2, delay_cost=1)
	c_t611 += alt(MAS)
	c_t611_in = S.Task('c_t611_in', length=1, delay_cost=1)
	c_t611_in += alt(MAS_in)
	S += c_t611_in*MAS_in[0]<=c_t611*MAS[0]

	S += c_t611_in*MAS_in[1]<=c_t611*MAS[1]

	S += c_t611_in*MAS_in[2]<=c_t611*MAS[2]

	S += c_t611_in*MAS_in[3]<=c_t611*MAS[3]

	S += c_t611_in*MAS_in[4]<=c_t611*MAS[4]

	S += c_t611_in*MAS_in[5]<=c_t611*MAS[5]

	c_t611_mem0 = S.Task('c_t611_mem0', length=1, delay_cost=1)
	c_t611_mem0 += MAS_MEM[8]
	S += 83 < c_t611_mem0
	S += c_t611_mem0 <= c_t611

	c_t611_mem1 = S.Task('c_t611_mem1', length=1, delay_cost=1)
	c_t611_mem1 += MAS_MEM[1]
	S += 54 < c_t611_mem1
	S += c_t611_mem1 <= c_t611

	c110 = S.Task('c110', length=2, delay_cost=1)
	c110 += alt(MAS)
	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	c110_in += alt(MAS_in)
	S += c110_in*MAS_in[0]<=c110*MAS[0]

	S += c110_in*MAS_in[1]<=c110*MAS[1]

	S += c110_in*MAS_in[2]<=c110*MAS[2]

	S += c110_in*MAS_in[3]<=c110*MAS[3]

	S += c110_in*MAS_in[4]<=c110*MAS[4]

	S += c110_in*MAS_in[5]<=c110*MAS[5]

	S += 52<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[4]
	S += 71 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MAS_MEM[3]
	S += 53 < c110_mem1
	S += c110_mem1 <= c110

	c_t7100 = S.Task('c_t7100', length=2, delay_cost=1)
	c_t7100 += alt(MAS)
	c_t7100_in = S.Task('c_t7100_in', length=1, delay_cost=1)
	c_t7100_in += alt(MAS_in)
	S += c_t7100_in*MAS_in[0]<=c_t7100*MAS[0]

	S += c_t7100_in*MAS_in[1]<=c_t7100*MAS[1]

	S += c_t7100_in*MAS_in[2]<=c_t7100*MAS[2]

	S += c_t7100_in*MAS_in[3]<=c_t7100*MAS[3]

	S += c_t7100_in*MAS_in[4]<=c_t7100*MAS[4]

	S += c_t7100_in*MAS_in[5]<=c_t7100*MAS[5]

	c_t7100_mem0 = S.Task('c_t7100_mem0', length=1, delay_cost=1)
	c_t7100_mem0 += MAS_MEM[8]
	S += 78 < c_t7100_mem0
	S += c_t7100_mem0 <= c_t7100

	c_t7100_mem1 = S.Task('c_t7100_mem1', length=1, delay_cost=1)
	c_t7100_mem1 += MAS_MEM[7]
	S += 56 < c_t7100_mem1
	S += c_t7100_mem1 <= c_t7100

	c_t7101 = S.Task('c_t7101', length=2, delay_cost=1)
	c_t7101 += alt(MAS)
	c_t7101_in = S.Task('c_t7101_in', length=1, delay_cost=1)
	c_t7101_in += alt(MAS_in)
	S += c_t7101_in*MAS_in[0]<=c_t7101*MAS[0]

	S += c_t7101_in*MAS_in[1]<=c_t7101*MAS[1]

	S += c_t7101_in*MAS_in[2]<=c_t7101*MAS[2]

	S += c_t7101_in*MAS_in[3]<=c_t7101*MAS[3]

	S += c_t7101_in*MAS_in[4]<=c_t7101*MAS[4]

	S += c_t7101_in*MAS_in[5]<=c_t7101*MAS[5]

	c_t7101_mem0 = S.Task('c_t7101_mem0', length=1, delay_cost=1)
	c_t7101_mem0 += MAS_MEM[4]
	S += 76 < c_t7101_mem0
	S += c_t7101_mem0 <= c_t7101

	c_t7101_mem1 = S.Task('c_t7101_mem1', length=1, delay_cost=1)
	c_t7101_mem1 += MAS_MEM[7]
	S += 57 < c_t7101_mem1
	S += c_t7101_mem1 <= c_t7101

	c_t7111 = S.Task('c_t7111', length=2, delay_cost=1)
	c_t7111 += alt(MAS)
	c_t7111_in = S.Task('c_t7111_in', length=1, delay_cost=1)
	c_t7111_in += alt(MAS_in)
	S += c_t7111_in*MAS_in[0]<=c_t7111*MAS[0]

	S += c_t7111_in*MAS_in[1]<=c_t7111*MAS[1]

	S += c_t7111_in*MAS_in[2]<=c_t7111*MAS[2]

	S += c_t7111_in*MAS_in[3]<=c_t7111*MAS[3]

	S += c_t7111_in*MAS_in[4]<=c_t7111*MAS[4]

	S += c_t7111_in*MAS_in[5]<=c_t7111*MAS[5]

	c_t7111_mem0 = S.Task('c_t7111_mem0', length=1, delay_cost=1)
	c_t7111_mem0 += MAS_MEM[10]
	S += 84 < c_t7111_mem0
	S += c_t7111_mem0 <= c_t7111

	c_t7111_mem1 = S.Task('c_t7111_mem1', length=1, delay_cost=1)
	c_t7111_mem1 += MAS_MEM[11]
	S += 83 < c_t7111_mem1
	S += c_t7111_mem1 <= c_t7111

	c_t800 = S.Task('c_t800', length=2, delay_cost=1)
	c_t800 += alt(MAS)
	c_t800_in = S.Task('c_t800_in', length=1, delay_cost=1)
	c_t800_in += alt(MAS_in)
	S += c_t800_in*MAS_in[0]<=c_t800*MAS[0]

	S += c_t800_in*MAS_in[1]<=c_t800*MAS[1]

	S += c_t800_in*MAS_in[2]<=c_t800*MAS[2]

	S += c_t800_in*MAS_in[3]<=c_t800*MAS[3]

	S += c_t800_in*MAS_in[4]<=c_t800*MAS[4]

	S += c_t800_in*MAS_in[5]<=c_t800*MAS[5]

	c_t800_mem0 = S.Task('c_t800_mem0', length=1, delay_cost=1)
	c_t800_mem0 += MAS_MEM[8]
	S += 85 < c_t800_mem0
	S += c_t800_mem0 <= c_t800

	c_t800_mem1 = S.Task('c_t800_mem1', length=1, delay_cost=1)
	c_t800_mem1 += MAS_MEM[7]
	S += 55 < c_t800_mem1
	S += c_t800_mem1 <= c_t800

	c_t801 = S.Task('c_t801', length=2, delay_cost=1)
	c_t801 += alt(MAS)
	c_t801_in = S.Task('c_t801_in', length=1, delay_cost=1)
	c_t801_in += alt(MAS_in)
	S += c_t801_in*MAS_in[0]<=c_t801*MAS[0]

	S += c_t801_in*MAS_in[1]<=c_t801*MAS[1]

	S += c_t801_in*MAS_in[2]<=c_t801*MAS[2]

	S += c_t801_in*MAS_in[3]<=c_t801*MAS[3]

	S += c_t801_in*MAS_in[4]<=c_t801*MAS[4]

	S += c_t801_in*MAS_in[5]<=c_t801*MAS[5]

	c_t801_mem0 = S.Task('c_t801_mem0', length=1, delay_cost=1)
	c_t801_mem0 += MAS_MEM[6]
	S += 85 < c_t801_mem0
	S += c_t801_mem0 <= c_t801

	c_t801_mem1 = S.Task('c_t801_mem1', length=1, delay_cost=1)
	c_t801_mem1 += MAS_MEM[9]
	S += 57 < c_t801_mem1
	S += c_t801_mem1 <= c_t801

	c_t811 = S.Task('c_t811', length=2, delay_cost=1)
	c_t811 += alt(MAS)
	c_t811_in = S.Task('c_t811_in', length=1, delay_cost=1)
	c_t811_in += alt(MAS_in)
	S += c_t811_in*MAS_in[0]<=c_t811*MAS[0]

	S += c_t811_in*MAS_in[1]<=c_t811*MAS[1]

	S += c_t811_in*MAS_in[2]<=c_t811*MAS[2]

	S += c_t811_in*MAS_in[3]<=c_t811*MAS[3]

	S += c_t811_in*MAS_in[4]<=c_t811*MAS[4]

	S += c_t811_in*MAS_in[5]<=c_t811*MAS[5]

	c_t811_mem0 = S.Task('c_t811_mem0', length=1, delay_cost=1)
	c_t811_mem0 += MAS_MEM[0]
	S += 86 < c_t811_mem0
	S += c_t811_mem0 <= c_t811

	c_t811_mem1 = S.Task('c_t811_mem1', length=1, delay_cost=1)
	c_t811_mem1 += MAS_MEM[3]
	S += 83 < c_t811_mem1
	S += c_t811_mem1 <= c_t811

	c210 = S.Task('c210', length=2, delay_cost=1)
	c210 += alt(MAS)
	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	c210_in += alt(MAS_in)
	S += c210_in*MAS_in[0]<=c210*MAS[0]

	S += c210_in*MAS_in[1]<=c210*MAS[1]

	S += c210_in*MAS_in[2]<=c210*MAS[2]

	S += c210_in*MAS_in[3]<=c210*MAS[3]

	S += c210_in*MAS_in[4]<=c210*MAS[4]

	S += c210_in*MAS_in[5]<=c210*MAS[5]

	S += 60<c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MAS_MEM[4]
	S += 81 < c210_mem0
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MAS_MEM[11]
	S += 45 < c210_mem1
	S += c210_mem1 <= c210

	c100 = S.Task('c100', length=2, delay_cost=1)
	c100 += alt(MAS)
	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	c100_in += alt(MAS_in)
	S += c100_in*MAS_in[0]<=c100*MAS[0]

	S += c100_in*MAS_in[1]<=c100*MAS[1]

	S += c100_in*MAS_in[2]<=c100*MAS[2]

	S += c100_in*MAS_in[3]<=c100*MAS[3]

	S += c100_in*MAS_in[4]<=c100*MAS[4]

	S += c100_in*MAS_in[5]<=c100*MAS[5]

	S += 49<c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(MAS_MEM)
	S += (c_t600*MAS[0])-1 < c100_mem0*MAS_MEM[0]
	S += (c_t600*MAS[1])-1 < c100_mem0*MAS_MEM[2]
	S += (c_t600*MAS[2])-1 < c100_mem0*MAS_MEM[4]
	S += (c_t600*MAS[3])-1 < c100_mem0*MAS_MEM[6]
	S += (c_t600*MAS[4])-1 < c100_mem0*MAS_MEM[8]
	S += (c_t600*MAS[5])-1 < c100_mem0*MAS_MEM[10]
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += MAS_MEM[7]
	S += 84 < c100_mem1
	S += c100_mem1 <= c100

	c101 = S.Task('c101', length=2, delay_cost=1)
	c101 += alt(MAS)
	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	c101_in += alt(MAS_in)
	S += c101_in*MAS_in[0]<=c101*MAS[0]

	S += c101_in*MAS_in[1]<=c101*MAS[1]

	S += c101_in*MAS_in[2]<=c101*MAS[2]

	S += c101_in*MAS_in[3]<=c101*MAS[3]

	S += c101_in*MAS_in[4]<=c101*MAS[4]

	S += c101_in*MAS_in[5]<=c101*MAS[5]

	S += 48<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MAS_MEM)
	S += (c_t601*MAS[0])-1 < c101_mem0*MAS_MEM[0]
	S += (c_t601*MAS[1])-1 < c101_mem0*MAS_MEM[2]
	S += (c_t601*MAS[2])-1 < c101_mem0*MAS_MEM[4]
	S += (c_t601*MAS[3])-1 < c101_mem0*MAS_MEM[6]
	S += (c_t601*MAS[4])-1 < c101_mem0*MAS_MEM[8]
	S += (c_t601*MAS[5])-1 < c101_mem0*MAS_MEM[10]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += MAS_MEM[9]
	S += 84 < c101_mem1
	S += c101_mem1 <= c101

	c111 = S.Task('c111', length=2, delay_cost=1)
	c111 += alt(MAS)
	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	c111_in += alt(MAS_in)
	S += c111_in*MAS_in[0]<=c111*MAS[0]

	S += c111_in*MAS_in[1]<=c111*MAS[1]

	S += c111_in*MAS_in[2]<=c111*MAS[2]

	S += c111_in*MAS_in[3]<=c111*MAS[3]

	S += c111_in*MAS_in[4]<=c111*MAS[4]

	S += c111_in*MAS_in[5]<=c111*MAS[5]

	S += 54<c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += alt(MAS_MEM)
	S += (c_t611*MAS[0])-1 < c111_mem0*MAS_MEM[0]
	S += (c_t611*MAS[1])-1 < c111_mem0*MAS_MEM[2]
	S += (c_t611*MAS[2])-1 < c111_mem0*MAS_MEM[4]
	S += (c_t611*MAS[3])-1 < c111_mem0*MAS_MEM[6]
	S += (c_t611*MAS[4])-1 < c111_mem0*MAS_MEM[8]
	S += (c_t611*MAS[5])-1 < c111_mem0*MAS_MEM[10]
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += MAS_MEM[3]
	S += 55 < c111_mem1
	S += c111_mem1 <= c111

	c_t7_y1_0 = S.Task('c_t7_y1_0', length=2, delay_cost=1)
	c_t7_y1_0 += alt(MAS)
	c_t7_y1_0_in = S.Task('c_t7_y1_0_in', length=1, delay_cost=1)
	c_t7_y1_0_in += alt(MAS_in)
	S += c_t7_y1_0_in*MAS_in[0]<=c_t7_y1_0*MAS[0]

	S += c_t7_y1_0_in*MAS_in[1]<=c_t7_y1_0*MAS[1]

	S += c_t7_y1_0_in*MAS_in[2]<=c_t7_y1_0*MAS[2]

	S += c_t7_y1_0_in*MAS_in[3]<=c_t7_y1_0*MAS[3]

	S += c_t7_y1_0_in*MAS_in[4]<=c_t7_y1_0*MAS[4]

	S += c_t7_y1_0_in*MAS_in[5]<=c_t7_y1_0*MAS[5]

	c_t7_y1_0_mem0 = S.Task('c_t7_y1_0_mem0', length=1, delay_cost=1)
	c_t7_y1_0_mem0 += MAS_MEM[0]
	S += 82 < c_t7_y1_0_mem0
	S += c_t7_y1_0_mem0 <= c_t7_y1_0

	c_t7_y1_0_mem1 = S.Task('c_t7_y1_0_mem1', length=1, delay_cost=1)
	c_t7_y1_0_mem1 += alt(MAS_MEM)
	S += (c_t7111*MAS[0])-1 < c_t7_y1_0_mem1*MAS_MEM[1]
	S += (c_t7111*MAS[1])-1 < c_t7_y1_0_mem1*MAS_MEM[3]
	S += (c_t7111*MAS[2])-1 < c_t7_y1_0_mem1*MAS_MEM[5]
	S += (c_t7111*MAS[3])-1 < c_t7_y1_0_mem1*MAS_MEM[7]
	S += (c_t7111*MAS[4])-1 < c_t7_y1_0_mem1*MAS_MEM[9]
	S += (c_t7111*MAS[5])-1 < c_t7_y1_0_mem1*MAS_MEM[11]
	S += c_t7_y1_0_mem1 <= c_t7_y1_0

	c_t7_y1_1 = S.Task('c_t7_y1_1', length=2, delay_cost=1)
	c_t7_y1_1 += alt(MAS)
	c_t7_y1_1_in = S.Task('c_t7_y1_1_in', length=1, delay_cost=1)
	c_t7_y1_1_in += alt(MAS_in)
	S += c_t7_y1_1_in*MAS_in[0]<=c_t7_y1_1*MAS[0]

	S += c_t7_y1_1_in*MAS_in[1]<=c_t7_y1_1*MAS[1]

	S += c_t7_y1_1_in*MAS_in[2]<=c_t7_y1_1*MAS[2]

	S += c_t7_y1_1_in*MAS_in[3]<=c_t7_y1_1*MAS[3]

	S += c_t7_y1_1_in*MAS_in[4]<=c_t7_y1_1*MAS[4]

	S += c_t7_y1_1_in*MAS_in[5]<=c_t7_y1_1*MAS[5]

	c_t7_y1_1_mem0 = S.Task('c_t7_y1_1_mem0', length=1, delay_cost=1)
	c_t7_y1_1_mem0 += alt(MAS_MEM)
	S += (c_t7111*MAS[0])-1 < c_t7_y1_1_mem0*MAS_MEM[0]
	S += (c_t7111*MAS[1])-1 < c_t7_y1_1_mem0*MAS_MEM[2]
	S += (c_t7111*MAS[2])-1 < c_t7_y1_1_mem0*MAS_MEM[4]
	S += (c_t7111*MAS[3])-1 < c_t7_y1_1_mem0*MAS_MEM[6]
	S += (c_t7111*MAS[4])-1 < c_t7_y1_1_mem0*MAS_MEM[8]
	S += (c_t7111*MAS[5])-1 < c_t7_y1_1_mem0*MAS_MEM[10]
	S += c_t7_y1_1_mem0 <= c_t7_y1_1

	c_t7_y1_1_mem1 = S.Task('c_t7_y1_1_mem1', length=1, delay_cost=1)
	c_t7_y1_1_mem1 += MAS_MEM[1]
	S += 82 < c_t7_y1_1_mem1
	S += c_t7_y1_1_mem1 <= c_t7_y1_1

	c010 = S.Task('c010', length=2, delay_cost=1)
	c010 += alt(MAS)
	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MAS_in)
	S += c010_in*MAS_in[0]<=c010*MAS[0]

	S += c010_in*MAS_in[1]<=c010*MAS[1]

	S += c010_in*MAS_in[2]<=c010*MAS[2]

	S += c010_in*MAS_in[3]<=c010*MAS[3]

	S += c010_in*MAS_in[4]<=c010*MAS[4]

	S += c010_in*MAS_in[5]<=c010*MAS[5]

	S += 58<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += MAS_MEM[8]
	S += 46 < c010_mem0
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += alt(MAS_MEM)
	S += (c_t7100*MAS[0])-1 < c010_mem1*MAS_MEM[1]
	S += (c_t7100*MAS[1])-1 < c010_mem1*MAS_MEM[3]
	S += (c_t7100*MAS[2])-1 < c010_mem1*MAS_MEM[5]
	S += (c_t7100*MAS[3])-1 < c010_mem1*MAS_MEM[7]
	S += (c_t7100*MAS[4])-1 < c010_mem1*MAS_MEM[9]
	S += (c_t7100*MAS[5])-1 < c010_mem1*MAS_MEM[11]
	S += c010_mem1 <= c010

	c011 = S.Task('c011', length=2, delay_cost=1)
	c011 += alt(MAS)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MAS_in)
	S += c011_in*MAS_in[0]<=c011*MAS[0]

	S += c011_in*MAS_in[1]<=c011*MAS[1]

	S += c011_in*MAS_in[2]<=c011*MAS[2]

	S += c011_in*MAS_in[3]<=c011*MAS[3]

	S += c011_in*MAS_in[4]<=c011*MAS[4]

	S += c011_in*MAS_in[5]<=c011*MAS[5]

	S += 59<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MAS_MEM[0]
	S += 47 < c011_mem0
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(MAS_MEM)
	S += (c_t7101*MAS[0])-1 < c011_mem1*MAS_MEM[1]
	S += (c_t7101*MAS[1])-1 < c011_mem1*MAS_MEM[3]
	S += (c_t7101*MAS[2])-1 < c011_mem1*MAS_MEM[5]
	S += (c_t7101*MAS[3])-1 < c011_mem1*MAS_MEM[7]
	S += (c_t7101*MAS[4])-1 < c011_mem1*MAS_MEM[9]
	S += (c_t7101*MAS[5])-1 < c011_mem1*MAS_MEM[11]
	S += c011_mem1 <= c011

	c200 = S.Task('c200', length=2, delay_cost=1)
	c200 += alt(MAS)
	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MAS_in)
	S += c200_in*MAS_in[0]<=c200*MAS[0]

	S += c200_in*MAS_in[1]<=c200*MAS[1]

	S += c200_in*MAS_in[2]<=c200*MAS[2]

	S += c200_in*MAS_in[3]<=c200*MAS[3]

	S += c200_in*MAS_in[4]<=c200*MAS[4]

	S += c200_in*MAS_in[5]<=c200*MAS[5]

	S += 60<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(MAS_MEM)
	S += (c_t800*MAS[0])-1 < c200_mem0*MAS_MEM[0]
	S += (c_t800*MAS[1])-1 < c200_mem0*MAS_MEM[2]
	S += (c_t800*MAS[2])-1 < c200_mem0*MAS_MEM[4]
	S += (c_t800*MAS[3])-1 < c200_mem0*MAS_MEM[6]
	S += (c_t800*MAS[4])-1 < c200_mem0*MAS_MEM[8]
	S += (c_t800*MAS[5])-1 < c200_mem0*MAS_MEM[10]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAS_MEM[3]
	S += 52 < c200_mem1
	S += c200_mem1 <= c200

	c201 = S.Task('c201', length=2, delay_cost=1)
	c201 += alt(MAS)
	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MAS_in)
	S += c201_in*MAS_in[0]<=c201*MAS[0]

	S += c201_in*MAS_in[1]<=c201*MAS[1]

	S += c201_in*MAS_in[2]<=c201*MAS[2]

	S += c201_in*MAS_in[3]<=c201*MAS[3]

	S += c201_in*MAS_in[4]<=c201*MAS[4]

	S += c201_in*MAS_in[5]<=c201*MAS[5]

	S += 55<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MAS_MEM)
	S += (c_t801*MAS[0])-1 < c201_mem0*MAS_MEM[0]
	S += (c_t801*MAS[1])-1 < c201_mem0*MAS_MEM[2]
	S += (c_t801*MAS[2])-1 < c201_mem0*MAS_MEM[4]
	S += (c_t801*MAS[3])-1 < c201_mem0*MAS_MEM[6]
	S += (c_t801*MAS[4])-1 < c201_mem0*MAS_MEM[8]
	S += (c_t801*MAS[5])-1 < c201_mem0*MAS_MEM[10]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += MAS_MEM[1]
	S += 49 < c201_mem1
	S += c201_mem1 <= c201

	c211 = S.Task('c211', length=2, delay_cost=1)
	c211 += alt(MAS)
	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	c211_in += alt(MAS_in)
	S += c211_in*MAS_in[0]<=c211*MAS[0]

	S += c211_in*MAS_in[1]<=c211*MAS[1]

	S += c211_in*MAS_in[2]<=c211*MAS[2]

	S += c211_in*MAS_in[3]<=c211*MAS[3]

	S += c211_in*MAS_in[4]<=c211*MAS[4]

	S += c211_in*MAS_in[5]<=c211*MAS[5]

	S += 59<c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(MAS_MEM)
	S += (c_t811*MAS[0])-1 < c211_mem0*MAS_MEM[0]
	S += (c_t811*MAS[1])-1 < c211_mem0*MAS_MEM[2]
	S += (c_t811*MAS[2])-1 < c211_mem0*MAS_MEM[4]
	S += (c_t811*MAS[3])-1 < c211_mem0*MAS_MEM[6]
	S += (c_t811*MAS[4])-1 < c211_mem0*MAS_MEM[8]
	S += (c_t811*MAS[5])-1 < c211_mem0*MAS_MEM[10]
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += MAS_MEM[1]
	S += 51 < c211_mem1
	S += c211_mem1 <= c211

	c000 = S.Task('c000', length=2, delay_cost=1)
	c000 += alt(MAS)
	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	c000_in += alt(MAS_in)
	S += c000_in*MAS_in[0]<=c000*MAS[0]

	S += c000_in*MAS_in[1]<=c000*MAS[1]

	S += c000_in*MAS_in[2]<=c000*MAS[2]

	S += c000_in*MAS_in[3]<=c000*MAS[3]

	S += c000_in*MAS_in[4]<=c000*MAS[4]

	S += c000_in*MAS_in[5]<=c000*MAS[5]

	S += 57<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[2]
	S += 40 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (c_t7_y1_0*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (c_t7_y1_0*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (c_t7_y1_0*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (c_t7_y1_0*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += (c_t7_y1_0*MAS[4])-1 < c000_mem1*MAS_MEM[9]
	S += (c_t7_y1_0*MAS[5])-1 < c000_mem1*MAS_MEM[11]
	S += c000_mem1 <= c000

	c001 = S.Task('c001', length=2, delay_cost=1)
	c001 += alt(MAS)
	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	c001_in += alt(MAS_in)
	S += c001_in*MAS_in[0]<=c001*MAS[0]

	S += c001_in*MAS_in[1]<=c001*MAS[1]

	S += c001_in*MAS_in[2]<=c001*MAS[2]

	S += c001_in*MAS_in[3]<=c001*MAS[3]

	S += c001_in*MAS_in[4]<=c001*MAS[4]

	S += c001_in*MAS_in[5]<=c001*MAS[5]

	S += 55<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[0]
	S += 39 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (c_t7_y1_1*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += (c_t7_y1_1*MAS[1])-1 < c001_mem1*MAS_MEM[3]
	S += (c_t7_y1_1*MAS[2])-1 < c001_mem1*MAS_MEM[5]
	S += (c_t7_y1_1*MAS[3])-1 < c001_mem1*MAS_MEM[7]
	S += (c_t7_y1_1*MAS[4])-1 < c001_mem1*MAS_MEM[9]
	S += (c_t7_y1_1*MAS[5])-1 < c001_mem1*MAS_MEM[11]
	S += c001_mem1 <= c001

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM2_stage2MAS6/MUL/schedule7.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

