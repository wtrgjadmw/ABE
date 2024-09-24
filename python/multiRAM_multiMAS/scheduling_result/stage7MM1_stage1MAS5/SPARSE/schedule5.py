from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 153
	S = Scenario("schedule5", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	S += t4_t1_t0_in >= 0
	t4_t1_t0_in += MM_in[0]

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	S += t4_t1_t0_mem0 >= 0
	t4_t1_t0_mem0 += MAIN_MEM_r[0]

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	S += t4_t1_t0_mem1 >= 0
	t4_t1_t0_mem1 += MAIN_MEM_r[1]

	t4_t1_t0 = S.Task('t4_t1_t0', length=7, delay_cost=1)
	S += t4_t1_t0 >= 1
	t4_t1_t0 += MM[0]

	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	S += t4_t1_t1_in >= 1
	t4_t1_t1_in += MM_in[0]

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_t1_mem0 >= 1
	t4_t1_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_t1_mem1 >= 1
	t4_t1_t1_mem1 += MAIN_MEM_r[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 2
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 2
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 2
	t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t1_t1 = S.Task('t4_t1_t1', length=7, delay_cost=1)
	S += t4_t1_t1 >= 2
	t4_t1_t1 += MM[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 3
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 3
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 3
	t0_t0_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	S += t2_t1 >= 3
	t2_t1 += MM[0]

	t0_t0 = S.Task('t0_t0', length=7, delay_cost=1)
	S += t0_t0 >= 4
	t0_t0 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 4
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 4
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 4
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=7, delay_cost=1)
	S += t0_t1 >= 5
	t0_t1 += MM[0]

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	S += t4_t0_t0_in >= 5
	t4_t0_t0_in += MM_in[0]

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_t0_mem0 >= 5
	t4_t0_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_t0_mem1 >= 5
	t4_t0_t0_mem1 += MAIN_MEM_r[1]

	t4_t0_t0 = S.Task('t4_t0_t0', length=7, delay_cost=1)
	S += t4_t0_t0 >= 6
	t4_t0_t0 += MM[0]

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	S += t4_t0_t1_in >= 6
	t4_t0_t1_in += MM_in[0]

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	S += t4_t0_t1_mem0 >= 6
	t4_t0_t1_mem0 += MAIN_MEM_r[0]

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	S += t4_t0_t1_mem1 >= 6
	t4_t0_t1_mem1 += MAIN_MEM_r[1]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 7
	t1_t1_in += MM_in[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 7
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 7
	t1_t1_mem1 += MAIN_MEM_r[1]

	t4_t0_t1 = S.Task('t4_t0_t1', length=7, delay_cost=1)
	S += t4_t0_t1 >= 7
	t4_t0_t1 += MM[0]

	t1_t1 = S.Task('t1_t1', length=7, delay_cost=1)
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

	t4_t1_t5_mem0 = S.Task('t4_t1_t5_mem0', length=1, delay_cost=1)
	S += t4_t1_t5_mem0 >= 8
	t4_t1_t5_mem0 += MM_MEM[0]

	t4_t1_t5_mem1 = S.Task('t4_t1_t5_mem1', length=1, delay_cost=1)
	S += t4_t1_t5_mem1 >= 8
	t4_t1_t5_mem1 += MM_MEM[1]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 9
	t1_t0_in += MM_in[0]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 9
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 9
	t1_t0_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	S += t2_t0 >= 9
	t2_t0 += MM[0]

	t4_t10_mem0 = S.Task('t4_t10_mem0', length=1, delay_cost=1)
	S += t4_t10_mem0 >= 9
	t4_t10_mem0 += MM_MEM[0]

	t4_t10_mem1 = S.Task('t4_t10_mem1', length=1, delay_cost=1)
	S += t4_t10_mem1 >= 9
	t4_t10_mem1 += MM_MEM[1]

	t4_t1_t5 = S.Task('t4_t1_t5', length=1, delay_cost=1)
	S += t4_t1_t5 >= 9
	t4_t1_t5 += MAS[2]

	t1_t0 = S.Task('t1_t0', length=7, delay_cost=1)
	S += t1_t0 >= 10
	t1_t0 += MM[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 10
	t1_t2_mem0 += MAIN_MEM_r[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 10
	t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t10 = S.Task('t4_t10', length=1, delay_cost=1)
	S += t4_t10 >= 10
	t4_t10 += MAS[2]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 11
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 11
	t00_mem1 += MM_MEM[1]

	t1_t2 = S.Task('t1_t2', length=1, delay_cost=1)
	S += t1_t2 >= 11
	t1_t2 += MAS[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 11
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 11
	t2_t3_mem1 += MAIN_MEM_r[1]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 12
	t00 += MAS[1]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 12
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 12
	t0_t5_mem1 += MM_MEM[1]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 12
	t2_t3 += MAS[0]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	S += t4_t0_t2_mem0 >= 12
	t4_t0_t2_mem0 += MAIN_MEM_r[0]

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	S += t4_t0_t2_mem1 >= 12
	t4_t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 13
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 13
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 13
	t0_t5 += MAS[2]

	t4_t0_t2 = S.Task('t4_t0_t2', length=1, delay_cost=1)
	S += t4_t0_t2 >= 13
	t4_t0_t2 += MAS[1]

	t4_t0_t5_mem0 = S.Task('t4_t0_t5_mem0', length=1, delay_cost=1)
	S += t4_t0_t5_mem0 >= 13
	t4_t0_t5_mem0 += MM_MEM[0]

	t4_t0_t5_mem1 = S.Task('t4_t0_t5_mem1', length=1, delay_cost=1)
	S += t4_t0_t5_mem1 >= 13
	t4_t0_t5_mem1 += MM_MEM[1]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 14
	t0_t2 += MAS[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 14
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 14
	t2_t2_mem1 += MAIN_MEM_r[1]

	t4_t00_mem0 = S.Task('t4_t00_mem0', length=1, delay_cost=1)
	S += t4_t00_mem0 >= 14
	t4_t00_mem0 += MM_MEM[0]

	t4_t00_mem1 = S.Task('t4_t00_mem1', length=1, delay_cost=1)
	S += t4_t00_mem1 >= 14
	t4_t00_mem1 += MM_MEM[1]

	t4_t0_t5 = S.Task('t4_t0_t5', length=1, delay_cost=1)
	S += t4_t0_t5 >= 14
	t4_t0_t5 += MAS[1]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 15
	t2_t2 += MAS[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 15
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 15
	t2_t4_mem0 += MAS_MEM[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 15
	t2_t4_mem1 += MAS_MEM[1]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 15
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 15
	t2_t5_mem1 += MM_MEM[1]

	t4_t00 = S.Task('t4_t00', length=1, delay_cost=1)
	S += t4_t00 >= 15
	t4_t00 += MAS[2]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	S += t4_t0_t3_mem0 >= 15
	t4_t0_t3_mem0 += MAIN_MEM_r[0]

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	S += t4_t0_t3_mem1 >= 15
	t4_t0_t3_mem1 += MAIN_MEM_r[1]

	t4_t70_mem0 = S.Task('t4_t70_mem0', length=1, delay_cost=1)
	S += t4_t70_mem0 >= 15
	t4_t70_mem0 += MAS_MEM[4]

	t4_t70_mem1 = S.Task('t4_t70_mem1', length=1, delay_cost=1)
	S += t4_t70_mem1 >= 15
	t4_t70_mem1 += MAS_MEM[5]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 16
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 16
	t0_t3_mem1 += MAIN_MEM_r[1]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 16
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 16
	t1_t5_mem1 += MM_MEM[1]

	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	S += t2_t4 >= 16
	t2_t4 += MM[0]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 16
	t2_t5 += MAS[1]

	t4_t0_t3 = S.Task('t4_t0_t3', length=1, delay_cost=1)
	S += t4_t0_t3 >= 16
	t4_t0_t3 += MAS[0]

	t4_t0_t4_in = S.Task('t4_t0_t4_in', length=1, delay_cost=1)
	S += t4_t0_t4_in >= 16
	t4_t0_t4_in += MM_in[0]

	t4_t0_t4_mem0 = S.Task('t4_t0_t4_mem0', length=1, delay_cost=1)
	S += t4_t0_t4_mem0 >= 16
	t4_t0_t4_mem0 += MAS_MEM[2]

	t4_t0_t4_mem1 = S.Task('t4_t0_t4_mem1', length=1, delay_cost=1)
	S += t4_t0_t4_mem1 >= 16
	t4_t0_t4_mem1 += MAS_MEM[1]

	t4_t70 = S.Task('t4_t70', length=1, delay_cost=1)
	S += t4_t70 >= 16
	t4_t70 += MAS[2]

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 17
	t0_t3 += MAS[3]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 17
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 17
	t0_t4_mem0 += MAS_MEM[0]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 17
	t0_t4_mem1 += MAS_MEM[7]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 17
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 17
	t10_mem1 += MM_MEM[1]

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	S += t1_t5 >= 17
	t1_t5 += MAS[4]

	t4_t0_t4 = S.Task('t4_t0_t4', length=7, delay_cost=1)
	S += t4_t0_t4 >= 17
	t4_t0_t4 += MM[0]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	S += t4_t1_t3_mem0 >= 17
	t4_t1_t3_mem0 += MAIN_MEM_r[0]

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	S += t4_t1_t3_mem1 >= 17
	t4_t1_t3_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=7, delay_cost=1)
	S += t0_t4 >= 18
	t0_t4 += MM[0]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 18
	t10 += MAS[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 18
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 18
	t20_mem1 += MM_MEM[1]

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	S += t4_t1_t2_mem0 >= 18
	t4_t1_t2_mem0 += MAIN_MEM_r[0]

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	S += t4_t1_t2_mem1 >= 18
	t4_t1_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_t3 = S.Task('t4_t1_t3', length=1, delay_cost=1)
	S += t4_t1_t3 >= 18
	t4_t1_t3 += MAS[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 19
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 19
	t1_t3_mem1 += MAIN_MEM_r[1]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 19
	t20 += MAS[1]

	t4_t1_t2 = S.Task('t4_t1_t2', length=1, delay_cost=1)
	S += t4_t1_t2 >= 19
	t4_t1_t2 += MAS[0]

	t4_t1_t4_in = S.Task('t4_t1_t4_in', length=1, delay_cost=1)
	S += t4_t1_t4_in >= 19
	t4_t1_t4_in += MM_in[0]

	t4_t1_t4_mem0 = S.Task('t4_t1_t4_mem0', length=1, delay_cost=1)
	S += t4_t1_t4_mem0 >= 19
	t4_t1_t4_mem0 += MAS_MEM[0]

	t4_t1_t4_mem1 = S.Task('t4_t1_t4_mem1', length=1, delay_cost=1)
	S += t4_t1_t4_mem1 >= 19
	t4_t1_t4_mem1 += MAS_MEM[1]

	t1_t3 = S.Task('t1_t3', length=1, delay_cost=1)
	S += t1_t3 >= 20
	t1_t3 += MAS[1]

	t4_t1_t4 = S.Task('t4_t1_t4', length=7, delay_cost=1)
	S += t4_t1_t4 >= 20
	t4_t1_t4 += MM[0]

	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	S += t4_t2_t0_in >= 20
	t4_t2_t0_in += MM_in[0]

	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	S += t4_t2_t0_mem0 >= 20
	t4_t2_t0_mem0 += MAIN_MEM_r[0]

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	S += t4_t2_t0_mem1 >= 20
	t4_t2_t0_mem1 += MAIN_MEM_r[1]

	t4_t2_t0 = S.Task('t4_t2_t0', length=7, delay_cost=1)
	S += t4_t2_t0 >= 21
	t4_t2_t0 += MM[0]

	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	S += t4_t8_t0_in >= 21
	t4_t8_t0_in += MM_in[0]

	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	S += t4_t8_t0_mem0 >= 21
	t4_t8_t0_mem0 += MAIN_MEM_r[0]

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	S += t4_t8_t0_mem1 >= 21
	t4_t8_t0_mem1 += MAIN_MEM_r[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 22
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 22
	t21_mem1 += MAS_MEM[3]

	t4_t8_t0 = S.Task('t4_t8_t0', length=7, delay_cost=1)
	S += t4_t8_t0 >= 22
	t4_t8_t0 += MM[0]

	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	S += t4_t8_t1_in >= 22
	t4_t8_t1_in += MM_in[0]

	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	S += t4_t8_t1_mem0 >= 22
	t4_t8_t1_mem0 += MAIN_MEM_r[0]

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	S += t4_t8_t1_mem1 >= 22
	t4_t8_t1_mem1 += MAIN_MEM_r[1]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 23
	t170_mem0 += MAS_MEM[2]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 23
	t170_mem1 += MAS_MEM[9]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 23
	t171_mem0 += MAS_MEM[8]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 23
	t171_mem1 += MAS_MEM[3]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 23
	t21 += MAS[4]

	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	S += t4_t2_t1_in >= 23
	t4_t2_t1_in += MM_in[0]

	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	S += t4_t2_t1_mem0 >= 23
	t4_t2_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	S += t4_t2_t1_mem1 >= 23
	t4_t2_t1_mem1 += MAIN_MEM_r[1]

	t4_t8_t1 = S.Task('t4_t8_t1', length=7, delay_cost=1)
	S += t4_t8_t1 >= 23
	t4_t8_t1 += MM[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 24
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 24
	t01_mem1 += MAS_MEM[5]

	t170 = S.Task('t170', length=1, delay_cost=1)
	S += t170 >= 24
	t170 += MAS[2]

	t171 = S.Task('t171', length=1, delay_cost=1)
	S += t171 >= 24
	t171 += MAS[3]

	t1_t4_in = S.Task('t1_t4_in', length=1, delay_cost=1)
	S += t1_t4_in >= 24
	t1_t4_in += MM_in[0]

	t1_t4_mem0 = S.Task('t1_t4_mem0', length=1, delay_cost=1)
	S += t1_t4_mem0 >= 24
	t1_t4_mem0 += MAS_MEM[2]

	t1_t4_mem1 = S.Task('t1_t4_mem1', length=1, delay_cost=1)
	S += t1_t4_mem1 >= 24
	t1_t4_mem1 += MAS_MEM[3]

	t4_t2_t1 = S.Task('t4_t2_t1', length=7, delay_cost=1)
	S += t4_t2_t1 >= 24
	t4_t2_t1 += MM[0]

	t4_t8_t2_mem0 = S.Task('t4_t8_t2_mem0', length=1, delay_cost=1)
	S += t4_t8_t2_mem0 >= 24
	t4_t8_t2_mem0 += MAIN_MEM_r[0]

	t4_t8_t2_mem1 = S.Task('t4_t8_t2_mem1', length=1, delay_cost=1)
	S += t4_t8_t2_mem1 >= 24
	t4_t8_t2_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 25
	t01 += MAS[0]

	t1_t4 = S.Task('t1_t4', length=7, delay_cost=1)
	S += t1_t4 >= 25
	t1_t4 += MM[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 25
	t30_mem0 += MAS_MEM[2]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 25
	t30_mem1 += MAS_MEM[1]

	t4_t01_mem0 = S.Task('t4_t01_mem0', length=1, delay_cost=1)
	S += t4_t01_mem0 >= 25
	t4_t01_mem0 += MM_MEM[0]

	t4_t01_mem1 = S.Task('t4_t01_mem1', length=1, delay_cost=1)
	S += t4_t01_mem1 >= 25
	t4_t01_mem1 += MAS_MEM[3]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	S += t4_t51_mem0 >= 25
	t4_t51_mem0 += MAIN_MEM_r[0]

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	S += t4_t51_mem1 >= 25
	t4_t51_mem1 += MAIN_MEM_r[1]

	t4_t8_t2 = S.Task('t4_t8_t2', length=1, delay_cost=1)
	S += t4_t8_t2 >= 25
	t4_t8_t2 += MAS[4]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 26
	t30 += MAS[2]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 26
	t31_mem0 += MAS_MEM[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 26
	t31_mem1 += MAS_MEM[3]

	t4_t01 = S.Task('t4_t01', length=1, delay_cost=1)
	S += t4_t01 >= 26
	t4_t01 += MAS[1]

	t4_t11_mem0 = S.Task('t4_t11_mem0', length=1, delay_cost=1)
	S += t4_t11_mem0 >= 26
	t4_t11_mem0 += MM_MEM[0]

	t4_t11_mem1 = S.Task('t4_t11_mem1', length=1, delay_cost=1)
	S += t4_t11_mem1 >= 26
	t4_t11_mem1 += MAS_MEM[5]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	S += t4_t40_mem0 >= 26
	t4_t40_mem0 += MAIN_MEM_r[0]

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	S += t4_t40_mem1 >= 26
	t4_t40_mem1 += MAIN_MEM_r[1]

	t4_t51 = S.Task('t4_t51', length=1, delay_cost=1)
	S += t4_t51 >= 26
	t4_t51 += MAS[4]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 27
	t31 += MAS[1]

	t4_t11 = S.Task('t4_t11', length=1, delay_cost=1)
	S += t4_t11 >= 27
	t4_t11 += MAS[4]

	t4_t40 = S.Task('t4_t40', length=1, delay_cost=1)
	S += t4_t40 >= 27
	t4_t40 += MAS[2]

	t4_t71_mem0 = S.Task('t4_t71_mem0', length=1, delay_cost=1)
	S += t4_t71_mem0 >= 27
	t4_t71_mem0 += MAS_MEM[2]

	t4_t71_mem1 = S.Task('t4_t71_mem1', length=1, delay_cost=1)
	S += t4_t71_mem1 >= 27
	t4_t71_mem1 += MAS_MEM[9]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 27
	t81_mem0 += MAIN_MEM_r[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 27
	t81_mem1 += MAIN_MEM_r[1]

	t4_t71 = S.Task('t4_t71', length=1, delay_cost=1)
	S += t4_t71 >= 28
	t4_t71 += MAS[1]

	t4_t8_t3_mem0 = S.Task('t4_t8_t3_mem0', length=1, delay_cost=1)
	S += t4_t8_t3_mem0 >= 28
	t4_t8_t3_mem0 += MAIN_MEM_r[0]

	t4_t8_t3_mem1 = S.Task('t4_t8_t3_mem1', length=1, delay_cost=1)
	S += t4_t8_t3_mem1 >= 28
	t4_t8_t3_mem1 += MAIN_MEM_r[1]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 28
	t81 += MAS[3]

	t4_t80_mem0 = S.Task('t4_t80_mem0', length=1, delay_cost=1)
	S += t4_t80_mem0 >= 29
	t4_t80_mem0 += MM_MEM[0]

	t4_t80_mem1 = S.Task('t4_t80_mem1', length=1, delay_cost=1)
	S += t4_t80_mem1 >= 29
	t4_t80_mem1 += MM_MEM[1]

	t4_t8_t3 = S.Task('t4_t8_t3', length=1, delay_cost=1)
	S += t4_t8_t3 >= 29
	t4_t8_t3 += MAS[3]

	t4_t8_t4_in = S.Task('t4_t8_t4_in', length=1, delay_cost=1)
	S += t4_t8_t4_in >= 29
	t4_t8_t4_in += MM_in[0]

	t4_t8_t4_mem0 = S.Task('t4_t8_t4_mem0', length=1, delay_cost=1)
	S += t4_t8_t4_mem0 >= 29
	t4_t8_t4_mem0 += MAS_MEM[8]

	t4_t8_t4_mem1 = S.Task('t4_t8_t4_mem1', length=1, delay_cost=1)
	S += t4_t8_t4_mem1 >= 29
	t4_t8_t4_mem1 += MAS_MEM[7]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 29
	t71_mem0 += MAIN_MEM_r[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 29
	t71_mem1 += MAIN_MEM_r[1]

	t420_mem0 = S.Task('t420_mem0', length=1, delay_cost=1)
	S += t420_mem0 >= 30
	t420_mem0 += MAS_MEM[0]

	t420_mem1 = S.Task('t420_mem1', length=1, delay_cost=1)
	S += t420_mem1 >= 30
	t420_mem1 += MAS_MEM[5]

	t4_t2_t5_mem0 = S.Task('t4_t2_t5_mem0', length=1, delay_cost=1)
	S += t4_t2_t5_mem0 >= 30
	t4_t2_t5_mem0 += MM_MEM[0]

	t4_t2_t5_mem1 = S.Task('t4_t2_t5_mem1', length=1, delay_cost=1)
	S += t4_t2_t5_mem1 >= 30
	t4_t2_t5_mem1 += MM_MEM[1]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	S += t4_t41_mem0 >= 30
	t4_t41_mem0 += MAIN_MEM_r[0]

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	S += t4_t41_mem1 >= 30
	t4_t41_mem1 += MAIN_MEM_r[1]

	t4_t80 = S.Task('t4_t80', length=1, delay_cost=1)
	S += t4_t80 >= 30
	t4_t80 += MAS[0]

	t4_t8_t4 = S.Task('t4_t8_t4', length=7, delay_cost=1)
	S += t4_t8_t4 >= 30
	t4_t8_t4 += MM[0]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 30
	t71 += MAS[3]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 31
	t160_mem0 += MAS_MEM[2]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 31
	t160_mem1 += MAS_MEM[3]

	t420 = S.Task('t420', length=1, delay_cost=1)
	S += t420 >= 31
	t420 += MAS[1]

	t4_t2_t5 = S.Task('t4_t2_t5', length=1, delay_cost=1)
	S += t4_t2_t5 >= 31
	t4_t2_t5 += MAS[0]

	t4_t41 = S.Task('t4_t41', length=1, delay_cost=1)
	S += t4_t41 >= 31
	t4_t41 += MAS[3]

	t4_t6_t1_in = S.Task('t4_t6_t1_in', length=1, delay_cost=1)
	S += t4_t6_t1_in >= 31
	t4_t6_t1_in += MM_in[0]

	t4_t6_t1_mem0 = S.Task('t4_t6_t1_mem0', length=1, delay_cost=1)
	S += t4_t6_t1_mem0 >= 31
	t4_t6_t1_mem0 += MAS_MEM[6]

	t4_t6_t1_mem1 = S.Task('t4_t6_t1_mem1', length=1, delay_cost=1)
	S += t4_t6_t1_mem1 >= 31
	t4_t6_t1_mem1 += MAS_MEM[9]

	t4_t6_t2_mem0 = S.Task('t4_t6_t2_mem0', length=1, delay_cost=1)
	S += t4_t6_t2_mem0 >= 31
	t4_t6_t2_mem0 += MAS_MEM[4]

	t4_t6_t2_mem1 = S.Task('t4_t6_t2_mem1', length=1, delay_cost=1)
	S += t4_t6_t2_mem1 >= 31
	t4_t6_t2_mem1 += MAS_MEM[7]

	t4_t8_t5_mem0 = S.Task('t4_t8_t5_mem0', length=1, delay_cost=1)
	S += t4_t8_t5_mem0 >= 31
	t4_t8_t5_mem0 += MM_MEM[0]

	t4_t8_t5_mem1 = S.Task('t4_t8_t5_mem1', length=1, delay_cost=1)
	S += t4_t8_t5_mem1 >= 31
	t4_t8_t5_mem1 += MM_MEM[1]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 31
	t91_mem0 += MAIN_MEM_r[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 31
	t91_mem1 += MAIN_MEM_r[1]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 32
	t100_mem0 += MAIN_MEM_r[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 32
	t100_mem1 += MAIN_MEM_r[1]

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 32
	t160 += MAS[2]

	t4_t20_mem0 = S.Task('t4_t20_mem0', length=1, delay_cost=1)
	S += t4_t20_mem0 >= 32
	t4_t20_mem0 += MM_MEM[0]

	t4_t20_mem1 = S.Task('t4_t20_mem1', length=1, delay_cost=1)
	S += t4_t20_mem1 >= 32
	t4_t20_mem1 += MM_MEM[1]

	t4_t6_t1 = S.Task('t4_t6_t1', length=7, delay_cost=1)
	S += t4_t6_t1 >= 32
	t4_t6_t1 += MM[0]

	t4_t6_t2 = S.Task('t4_t6_t2', length=1, delay_cost=1)
	S += t4_t6_t2 >= 32
	t4_t6_t2 += MAS[3]

	t4_t8_t5 = S.Task('t4_t8_t5', length=1, delay_cost=1)
	S += t4_t8_t5 >= 32
	t4_t8_t5 += MAS[1]

	t5_t1_t1_in = S.Task('t5_t1_t1_in', length=1, delay_cost=1)
	S += t5_t1_t1_in >= 32
	t5_t1_t1_in += MM_in[0]

	t5_t1_t1_mem0 = S.Task('t5_t1_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_t1_mem0 >= 32
	t5_t1_t1_mem0 += MAS_MEM[6]

	t5_t1_t1_mem1 = S.Task('t5_t1_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_t1_mem1 >= 32
	t5_t1_t1_mem1 += MAS_MEM[1]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 32
	t91 += MAS[0]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 33
	t100 += MAS[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 33
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 33
	t11_mem1 += MAS_MEM[9]

	t4_t20 = S.Task('t4_t20', length=1, delay_cost=1)
	S += t4_t20 >= 33
	t4_t20 += MAS[0]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_t2_mem0 >= 33
	t4_t2_t2_mem0 += MAIN_MEM_r[0]

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_t2_mem1 >= 33
	t4_t2_t2_mem1 += MAIN_MEM_r[1]

	t5_t1_t1 = S.Task('t5_t1_t1', length=7, delay_cost=1)
	S += t5_t1_t1 >= 33
	t5_t1_t1 += MM[0]

	t5_t51_mem0 = S.Task('t5_t51_mem0', length=1, delay_cost=1)
	S += t5_t51_mem0 >= 33
	t5_t51_mem0 += MAS_MEM[6]

	t5_t51_mem1 = S.Task('t5_t51_mem1', length=1, delay_cost=1)
	S += t5_t51_mem1 >= 33
	t5_t51_mem1 += MAS_MEM[1]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 34
	t11 += MAS[1]

	t4_t2_t2 = S.Task('t4_t2_t2', length=1, delay_cost=1)
	S += t4_t2_t2 >= 34
	t4_t2_t2 += MAS[0]

	t5_t51 = S.Task('t5_t51', length=1, delay_cost=1)
	S += t5_t51 >= 34
	t5_t51 += MAS[2]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 34
	t90_mem0 += MAIN_MEM_r[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 34
	t90_mem1 += MAIN_MEM_r[1]

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	S += c110_mem0 >= 35
	c110_mem0 += MAS_MEM[2]

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	S += c110_mem1 >= 35
	c110_mem1 += MAS_MEM[3]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	S += t4_t2_t3_mem0 >= 35
	t4_t2_t3_mem0 += MAIN_MEM_r[0]

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	S += t4_t2_t3_mem1 >= 35
	t4_t2_t3_mem1 += MAIN_MEM_r[1]

	t5_t1_t3_mem0 = S.Task('t5_t1_t3_mem0', length=1, delay_cost=1)
	S += t5_t1_t3_mem0 >= 35
	t5_t1_t3_mem0 += MAS_MEM[0]

	t5_t1_t3_mem1 = S.Task('t5_t1_t3_mem1', length=1, delay_cost=1)
	S += t5_t1_t3_mem1 >= 35
	t5_t1_t3_mem1 += MAS_MEM[1]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 35
	t90 += MAS[0]

	c110 = S.Task('c110', length=1, delay_cost=1)
	S += c110 >= 36
	c110 += MAS[1]

	t4_t2_t3 = S.Task('t4_t2_t3', length=1, delay_cost=1)
	S += t4_t2_t3 >= 36
	t4_t2_t3 += MAS[3]

	t4_t2_t4_in = S.Task('t4_t2_t4_in', length=1, delay_cost=1)
	S += t4_t2_t4_in >= 36
	t4_t2_t4_in += MM_in[0]

	t4_t2_t4_mem0 = S.Task('t4_t2_t4_mem0', length=1, delay_cost=1)
	S += t4_t2_t4_mem0 >= 36
	t4_t2_t4_mem0 += MAS_MEM[0]

	t4_t2_t4_mem1 = S.Task('t4_t2_t4_mem1', length=1, delay_cost=1)
	S += t4_t2_t4_mem1 >= 36
	t4_t2_t4_mem1 += MAS_MEM[7]

	t4_t81_mem0 = S.Task('t4_t81_mem0', length=1, delay_cost=1)
	S += t4_t81_mem0 >= 36
	t4_t81_mem0 += MM_MEM[0]

	t4_t81_mem1 = S.Task('t4_t81_mem1', length=1, delay_cost=1)
	S += t4_t81_mem1 >= 36
	t4_t81_mem1 += MAS_MEM[3]

	t5_t1_t3 = S.Task('t5_t1_t3', length=1, delay_cost=1)
	S += t5_t1_t3 >= 36
	t5_t1_t3 += MAS[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 36
	t80_mem0 += MAIN_MEM_r[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 36
	t80_mem1 += MAIN_MEM_r[1]

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	S += c110_w >= 37
	c110_w += MAIN_MEM_w

	t421_mem0 = S.Task('t421_mem0', length=1, delay_cost=1)
	S += t421_mem0 >= 37
	t421_mem0 += MAS_MEM[4]

	t421_mem1 = S.Task('t421_mem1', length=1, delay_cost=1)
	S += t421_mem1 >= 37
	t421_mem1 += MAS_MEM[9]

	t4_t2_t4 = S.Task('t4_t2_t4', length=7, delay_cost=1)
	S += t4_t2_t4 >= 37
	t4_t2_t4 += MM[0]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	S += t4_t50_mem0 >= 37
	t4_t50_mem0 += MAIN_MEM_r[0]

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	S += t4_t50_mem1 >= 37
	t4_t50_mem1 += MAIN_MEM_r[1]

	t4_t81 = S.Task('t4_t81', length=1, delay_cost=1)
	S += t4_t81 >= 37
	t4_t81 += MAS[2]

	t5_t0_t3_mem0 = S.Task('t5_t0_t3_mem0', length=1, delay_cost=1)
	S += t5_t0_t3_mem0 >= 37
	t5_t0_t3_mem0 += MAS_MEM[2]

	t5_t0_t3_mem1 = S.Task('t5_t0_t3_mem1', length=1, delay_cost=1)
	S += t5_t0_t3_mem1 >= 37
	t5_t0_t3_mem1 += MAS_MEM[7]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 37
	t80 += MAS[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 38
	t101_mem0 += MAIN_MEM_r[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 38
	t101_mem1 += MAIN_MEM_r[1]

	t421 = S.Task('t421', length=1, delay_cost=1)
	S += t421 >= 38
	t421 += MAS[0]

	t4_t50 = S.Task('t4_t50', length=1, delay_cost=1)
	S += t4_t50 >= 38
	t4_t50 += MAS[3]

	t4_t6_t0_in = S.Task('t4_t6_t0_in', length=1, delay_cost=1)
	S += t4_t6_t0_in >= 38
	t4_t6_t0_in += MM_in[0]

	t4_t6_t0_mem0 = S.Task('t4_t6_t0_mem0', length=1, delay_cost=1)
	S += t4_t6_t0_mem0 >= 38
	t4_t6_t0_mem0 += MAS_MEM[4]

	t4_t6_t0_mem1 = S.Task('t4_t6_t0_mem1', length=1, delay_cost=1)
	S += t4_t6_t0_mem1 >= 38
	t4_t6_t0_mem1 += MAS_MEM[7]

	t4_t6_t3_mem0 = S.Task('t4_t6_t3_mem0', length=1, delay_cost=1)
	S += t4_t6_t3_mem0 >= 38
	t4_t6_t3_mem0 += MAS_MEM[6]

	t4_t6_t3_mem1 = S.Task('t4_t6_t3_mem1', length=1, delay_cost=1)
	S += t4_t6_t3_mem1 >= 38
	t4_t6_t3_mem1 += MAS_MEM[9]

	t5_t0_t3 = S.Task('t5_t0_t3', length=1, delay_cost=1)
	S += t5_t0_t3 >= 38
	t5_t0_t3 += MAS[2]

	t5_t50_mem0 = S.Task('t5_t50_mem0', length=1, delay_cost=1)
	S += t5_t50_mem0 >= 38
	t5_t50_mem0 += MAS_MEM[2]

	t5_t50_mem1 = S.Task('t5_t50_mem1', length=1, delay_cost=1)
	S += t5_t50_mem1 >= 38
	t5_t50_mem1 += MAS_MEM[1]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 39
	t101 += MAS[3]

	t4_t6_t0 = S.Task('t4_t6_t0', length=7, delay_cost=1)
	S += t4_t6_t0 >= 39
	t4_t6_t0 += MM[0]

	t4_t6_t3 = S.Task('t4_t6_t3', length=1, delay_cost=1)
	S += t4_t6_t3 >= 39
	t4_t6_t3 += MAS[0]

	t5_t2_t1_in = S.Task('t5_t2_t1_in', length=1, delay_cost=1)
	S += t5_t2_t1_in >= 39
	t5_t2_t1_in += MM_in[0]

	t5_t2_t1_mem0 = S.Task('t5_t2_t1_mem0', length=1, delay_cost=1)
	S += t5_t2_t1_mem0 >= 39
	t5_t2_t1_mem0 += MAS_MEM[6]

	t5_t2_t1_mem1 = S.Task('t5_t2_t1_mem1', length=1, delay_cost=1)
	S += t5_t2_t1_mem1 >= 39
	t5_t2_t1_mem1 += MAS_MEM[7]

	t5_t50 = S.Task('t5_t50', length=1, delay_cost=1)
	S += t5_t50 >= 39
	t5_t50 += MAS[1]

	t5_t6_t3_mem0 = S.Task('t5_t6_t3_mem0', length=1, delay_cost=1)
	S += t5_t6_t3_mem0 >= 39
	t5_t6_t3_mem0 += MAS_MEM[2]

	t5_t6_t3_mem1 = S.Task('t5_t6_t3_mem1', length=1, delay_cost=1)
	S += t5_t6_t3_mem1 >= 39
	t5_t6_t3_mem1 += MAS_MEM[5]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 39
	t70_mem0 += MAIN_MEM_r[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 39
	t70_mem1 += MAIN_MEM_r[1]

	t5_t1_t0_in = S.Task('t5_t1_t0_in', length=1, delay_cost=1)
	S += t5_t1_t0_in >= 40
	t5_t1_t0_in += MM_in[0]

	t5_t1_t0_mem0 = S.Task('t5_t1_t0_mem0', length=1, delay_cost=1)
	S += t5_t1_t0_mem0 >= 40
	t5_t1_t0_mem0 += MAS_MEM[0]

	t5_t1_t0_mem1 = S.Task('t5_t1_t0_mem1', length=1, delay_cost=1)
	S += t5_t1_t0_mem1 >= 40
	t5_t1_t0_mem1 += MAS_MEM[1]

	t5_t2_t1 = S.Task('t5_t2_t1', length=7, delay_cost=1)
	S += t5_t2_t1 >= 40
	t5_t2_t1 += MM[0]

	t5_t2_t3_mem0 = S.Task('t5_t2_t3_mem0', length=1, delay_cost=1)
	S += t5_t2_t3_mem0 >= 40
	t5_t2_t3_mem0 += MAS_MEM[2]

	t5_t2_t3_mem1 = S.Task('t5_t2_t3_mem1', length=1, delay_cost=1)
	S += t5_t2_t3_mem1 >= 40
	t5_t2_t3_mem1 += MAS_MEM[7]

	t5_t6_t3 = S.Task('t5_t6_t3', length=1, delay_cost=1)
	S += t5_t6_t3 >= 40
	t5_t6_t3 += MAS[2]

	t5_t8_t2_mem0 = S.Task('t5_t8_t2_mem0', length=1, delay_cost=1)
	S += t5_t8_t2_mem0 >= 40
	t5_t8_t2_mem0 += MAIN_MEM_r[0]

	t5_t8_t2_mem1 = S.Task('t5_t8_t2_mem1', length=1, delay_cost=1)
	S += t5_t8_t2_mem1 >= 40
	t5_t8_t2_mem1 += MAIN_MEM_r[1]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 40
	t70 += MAS[0]

	t5_t0_t2_mem0 = S.Task('t5_t0_t2_mem0', length=1, delay_cost=1)
	S += t5_t0_t2_mem0 >= 41
	t5_t0_t2_mem0 += MAIN_MEM_r[0]

	t5_t0_t2_mem1 = S.Task('t5_t0_t2_mem1', length=1, delay_cost=1)
	S += t5_t0_t2_mem1 >= 41
	t5_t0_t2_mem1 += MAIN_MEM_r[1]

	t5_t1_t0 = S.Task('t5_t1_t0', length=7, delay_cost=1)
	S += t5_t1_t0 >= 41
	t5_t1_t0 += MM[0]

	t5_t2_t0_in = S.Task('t5_t2_t0_in', length=1, delay_cost=1)
	S += t5_t2_t0_in >= 41
	t5_t2_t0_in += MM_in[0]

	t5_t2_t0_mem0 = S.Task('t5_t2_t0_mem0', length=1, delay_cost=1)
	S += t5_t2_t0_mem0 >= 41
	t5_t2_t0_mem0 += MAS_MEM[0]

	t5_t2_t0_mem1 = S.Task('t5_t2_t0_mem1', length=1, delay_cost=1)
	S += t5_t2_t0_mem1 >= 41
	t5_t2_t0_mem1 += MAS_MEM[3]

	t5_t2_t3 = S.Task('t5_t2_t3', length=1, delay_cost=1)
	S += t5_t2_t3 >= 41
	t5_t2_t3 += MAS[2]

	t5_t8_t2 = S.Task('t5_t8_t2', length=1, delay_cost=1)
	S += t5_t8_t2 >= 41
	t5_t8_t2 += MAS[3]

	t5_t8_t3_mem0 = S.Task('t5_t8_t3_mem0', length=1, delay_cost=1)
	S += t5_t8_t3_mem0 >= 41
	t5_t8_t3_mem0 += MAS_MEM[2]

	t5_t8_t3_mem1 = S.Task('t5_t8_t3_mem1', length=1, delay_cost=1)
	S += t5_t8_t3_mem1 >= 41
	t5_t8_t3_mem1 += MAS_MEM[7]

	t5_t0_t2 = S.Task('t5_t0_t2', length=1, delay_cost=1)
	S += t5_t0_t2 >= 42
	t5_t0_t2 += MAS[3]

	t5_t1_t2_mem0 = S.Task('t5_t1_t2_mem0', length=1, delay_cost=1)
	S += t5_t1_t2_mem0 >= 42
	t5_t1_t2_mem0 += MAS_MEM[0]

	t5_t1_t2_mem1 = S.Task('t5_t1_t2_mem1', length=1, delay_cost=1)
	S += t5_t1_t2_mem1 >= 42
	t5_t1_t2_mem1 += MAS_MEM[7]

	t5_t2_t0 = S.Task('t5_t2_t0', length=7, delay_cost=1)
	S += t5_t2_t0 >= 42
	t5_t2_t0 += MM[0]

	t5_t8_t0_in = S.Task('t5_t8_t0_in', length=1, delay_cost=1)
	S += t5_t8_t0_in >= 42
	t5_t8_t0_in += MM_in[0]

	t5_t8_t0_mem0 = S.Task('t5_t8_t0_mem0', length=1, delay_cost=1)
	S += t5_t8_t0_mem0 >= 42
	t5_t8_t0_mem0 += MAIN_MEM_r[0]

	t5_t8_t0_mem1 = S.Task('t5_t8_t0_mem1', length=1, delay_cost=1)
	S += t5_t8_t0_mem1 >= 42
	t5_t8_t0_mem1 += MAS_MEM[3]

	t5_t8_t3 = S.Task('t5_t8_t3', length=1, delay_cost=1)
	S += t5_t8_t3 >= 42
	t5_t8_t3 += MAS[1]

	t4_t21_mem0 = S.Task('t4_t21_mem0', length=1, delay_cost=1)
	S += t4_t21_mem0 >= 43
	t4_t21_mem0 += MM_MEM[0]

	t4_t21_mem1 = S.Task('t4_t21_mem1', length=1, delay_cost=1)
	S += t4_t21_mem1 >= 43
	t4_t21_mem1 += MAS_MEM[1]

	t5_t0_t0_in = S.Task('t5_t0_t0_in', length=1, delay_cost=1)
	S += t5_t0_t0_in >= 43
	t5_t0_t0_in += MM_in[0]

	t5_t0_t0_mem0 = S.Task('t5_t0_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_t0_mem0 >= 43
	t5_t0_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_t0_mem1 = S.Task('t5_t0_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_t0_mem1 >= 43
	t5_t0_t0_mem1 += MAS_MEM[3]

	t5_t1_t2 = S.Task('t5_t1_t2', length=1, delay_cost=1)
	S += t5_t1_t2 >= 43
	t5_t1_t2 += MAS[1]

	t5_t2_t2_mem0 = S.Task('t5_t2_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_t2_mem0 >= 43
	t5_t2_t2_mem0 += MAS_MEM[0]

	t5_t2_t2_mem1 = S.Task('t5_t2_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_t2_mem1 >= 43
	t5_t2_t2_mem1 += MAS_MEM[7]

	t5_t8_t0 = S.Task('t5_t8_t0', length=7, delay_cost=1)
	S += t5_t8_t0 >= 43
	t5_t8_t0 += MM[0]

	t4_t100_mem0 = S.Task('t4_t100_mem0', length=1, delay_cost=1)
	S += t4_t100_mem0 >= 44
	t4_t100_mem0 += MAS_MEM[0]

	t4_t100_mem1 = S.Task('t4_t100_mem1', length=1, delay_cost=1)
	S += t4_t100_mem1 >= 44
	t4_t100_mem1 += MAS_MEM[5]

	t4_t101_mem0 = S.Task('t4_t101_mem0', length=1, delay_cost=1)
	S += t4_t101_mem0 >= 44
	t4_t101_mem0 += MAS_MEM[4]

	t4_t101_mem1 = S.Task('t4_t101_mem1', length=1, delay_cost=1)
	S += t4_t101_mem1 >= 44
	t4_t101_mem1 += MAS_MEM[1]

	t4_t21 = S.Task('t4_t21', length=1, delay_cost=1)
	S += t4_t21 >= 44
	t4_t21 += MAS[2]

	t5_t0_t0 = S.Task('t5_t0_t0', length=7, delay_cost=1)
	S += t5_t0_t0 >= 44
	t5_t0_t0 += MM[0]

	t5_t2_t2 = S.Task('t5_t2_t2', length=1, delay_cost=1)
	S += t5_t2_t2 >= 44
	t5_t2_t2 += MAS[0]

	t5_t8_t1_in = S.Task('t5_t8_t1_in', length=1, delay_cost=1)
	S += t5_t8_t1_in >= 44
	t5_t8_t1_in += MM_in[0]

	t5_t8_t1_mem0 = S.Task('t5_t8_t1_mem0', length=1, delay_cost=1)
	S += t5_t8_t1_mem0 >= 44
	t5_t8_t1_mem0 += MAIN_MEM_r[0]

	t5_t8_t1_mem1 = S.Task('t5_t8_t1_mem1', length=1, delay_cost=1)
	S += t5_t8_t1_mem1 >= 44
	t5_t8_t1_mem1 += MAS_MEM[7]

	t4_t100 = S.Task('t4_t100', length=1, delay_cost=1)
	S += t4_t100 >= 45
	t4_t100 += MAS[2]

	t4_t101 = S.Task('t4_t101', length=1, delay_cost=1)
	S += t4_t101 >= 45
	t4_t101 += MAS[0]

	t4_t60_mem0 = S.Task('t4_t60_mem0', length=1, delay_cost=1)
	S += t4_t60_mem0 >= 45
	t4_t60_mem0 += MM_MEM[0]

	t4_t60_mem1 = S.Task('t4_t60_mem1', length=1, delay_cost=1)
	S += t4_t60_mem1 >= 45
	t4_t60_mem1 += MM_MEM[1]

	t5_t0_t1_in = S.Task('t5_t0_t1_in', length=1, delay_cost=1)
	S += t5_t0_t1_in >= 45
	t5_t0_t1_in += MM_in[0]

	t5_t0_t1_mem0 = S.Task('t5_t0_t1_mem0', length=1, delay_cost=1)
	S += t5_t0_t1_mem0 >= 45
	t5_t0_t1_mem0 += MAIN_MEM_r[0]

	t5_t0_t1_mem1 = S.Task('t5_t0_t1_mem1', length=1, delay_cost=1)
	S += t5_t0_t1_mem1 >= 45
	t5_t0_t1_mem1 += MAS_MEM[7]

	t5_t8_t1 = S.Task('t5_t8_t1', length=7, delay_cost=1)
	S += t5_t8_t1 >= 45
	t5_t8_t1 += MM[0]

	t410_mem0 = S.Task('t410_mem0', length=1, delay_cost=1)
	S += t410_mem0 >= 46
	t410_mem0 += MAS_MEM[8]

	t410_mem1 = S.Task('t410_mem1', length=1, delay_cost=1)
	S += t410_mem1 >= 46
	t410_mem1 += MAS_MEM[5]

	t4_t60 = S.Task('t4_t60', length=1, delay_cost=1)
	S += t4_t60 >= 46
	t4_t60 += MAS[4]

	t4_t6_t5_mem0 = S.Task('t4_t6_t5_mem0', length=1, delay_cost=1)
	S += t4_t6_t5_mem0 >= 46
	t4_t6_t5_mem0 += MM_MEM[0]

	t4_t6_t5_mem1 = S.Task('t4_t6_t5_mem1', length=1, delay_cost=1)
	S += t4_t6_t5_mem1 >= 46
	t4_t6_t5_mem1 += MM_MEM[1]

	t5_t0_t1 = S.Task('t5_t0_t1', length=7, delay_cost=1)
	S += t5_t0_t1 >= 46
	t5_t0_t1 += MM[0]

	t5_t41_mem0 = S.Task('t5_t41_mem0', length=1, delay_cost=1)
	S += t5_t41_mem0 >= 46
	t5_t41_mem0 += MAIN_MEM_r[0]

	t5_t41_mem1 = S.Task('t5_t41_mem1', length=1, delay_cost=1)
	S += t5_t41_mem1 >= 46
	t5_t41_mem1 += MAS_MEM[7]

	t5_t8_t4_in = S.Task('t5_t8_t4_in', length=1, delay_cost=1)
	S += t5_t8_t4_in >= 46
	t5_t8_t4_in += MM_in[0]

	t5_t8_t4_mem0 = S.Task('t5_t8_t4_mem0', length=1, delay_cost=1)
	S += t5_t8_t4_mem0 >= 46
	t5_t8_t4_mem0 += MAS_MEM[6]

	t5_t8_t4_mem1 = S.Task('t5_t8_t4_mem1', length=1, delay_cost=1)
	S += t5_t8_t4_mem1 >= 46
	t5_t8_t4_mem1 += MAS_MEM[3]

	t410 = S.Task('t410', length=1, delay_cost=1)
	S += t410 >= 47
	t410 += MAS[2]

	t4_t6_t5 = S.Task('t4_t6_t5', length=1, delay_cost=1)
	S += t4_t6_t5 >= 47
	t4_t6_t5 += MAS[1]

	t5_t1_t5_mem0 = S.Task('t5_t1_t5_mem0', length=1, delay_cost=1)
	S += t5_t1_t5_mem0 >= 47
	t5_t1_t5_mem0 += MM_MEM[0]

	t5_t1_t5_mem1 = S.Task('t5_t1_t5_mem1', length=1, delay_cost=1)
	S += t5_t1_t5_mem1 >= 47
	t5_t1_t5_mem1 += MM_MEM[1]

	t5_t2_t4_in = S.Task('t5_t2_t4_in', length=1, delay_cost=1)
	S += t5_t2_t4_in >= 47
	t5_t2_t4_in += MM_in[0]

	t5_t2_t4_mem0 = S.Task('t5_t2_t4_mem0', length=1, delay_cost=1)
	S += t5_t2_t4_mem0 >= 47
	t5_t2_t4_mem0 += MAS_MEM[0]

	t5_t2_t4_mem1 = S.Task('t5_t2_t4_mem1', length=1, delay_cost=1)
	S += t5_t2_t4_mem1 >= 47
	t5_t2_t4_mem1 += MAS_MEM[5]

	t5_t40_mem0 = S.Task('t5_t40_mem0', length=1, delay_cost=1)
	S += t5_t40_mem0 >= 47
	t5_t40_mem0 += MAIN_MEM_r[0]

	t5_t40_mem1 = S.Task('t5_t40_mem1', length=1, delay_cost=1)
	S += t5_t40_mem1 >= 47
	t5_t40_mem1 += MAS_MEM[1]

	t5_t41 = S.Task('t5_t41', length=1, delay_cost=1)
	S += t5_t41 >= 47
	t5_t41 += MAS[0]

	t5_t8_t4 = S.Task('t5_t8_t4', length=7, delay_cost=1)
	S += t5_t8_t4 >= 47
	t5_t8_t4 += MM[0]

	t5_t0_t4_in = S.Task('t5_t0_t4_in', length=1, delay_cost=1)
	S += t5_t0_t4_in >= 48
	t5_t0_t4_in += MM_in[0]

	t5_t0_t4_mem0 = S.Task('t5_t0_t4_mem0', length=1, delay_cost=1)
	S += t5_t0_t4_mem0 >= 48
	t5_t0_t4_mem0 += MAS_MEM[6]

	t5_t0_t4_mem1 = S.Task('t5_t0_t4_mem1', length=1, delay_cost=1)
	S += t5_t0_t4_mem1 >= 48
	t5_t0_t4_mem1 += MAS_MEM[5]

	t5_t1_t5 = S.Task('t5_t1_t5', length=1, delay_cost=1)
	S += t5_t1_t5 >= 48
	t5_t1_t5 += MAS[2]

	t5_t20_mem0 = S.Task('t5_t20_mem0', length=1, delay_cost=1)
	S += t5_t20_mem0 >= 48
	t5_t20_mem0 += MM_MEM[0]

	t5_t20_mem1 = S.Task('t5_t20_mem1', length=1, delay_cost=1)
	S += t5_t20_mem1 >= 48
	t5_t20_mem1 += MM_MEM[1]

	t5_t2_t4 = S.Task('t5_t2_t4', length=7, delay_cost=1)
	S += t5_t2_t4 >= 48
	t5_t2_t4 += MM[0]

	t5_t40 = S.Task('t5_t40', length=1, delay_cost=1)
	S += t5_t40 >= 48
	t5_t40 += MAS[0]

	t5_t6_t2_mem0 = S.Task('t5_t6_t2_mem0', length=1, delay_cost=1)
	S += t5_t6_t2_mem0 >= 48
	t5_t6_t2_mem0 += MAS_MEM[0]

	t5_t6_t2_mem1 = S.Task('t5_t6_t2_mem1', length=1, delay_cost=1)
	S += t5_t6_t2_mem1 >= 48
	t5_t6_t2_mem1 += MAS_MEM[1]

	t5_t0_t4 = S.Task('t5_t0_t4', length=7, delay_cost=1)
	S += t5_t0_t4 >= 49
	t5_t0_t4 += MM[0]

	t5_t10_mem0 = S.Task('t5_t10_mem0', length=1, delay_cost=1)
	S += t5_t10_mem0 >= 49
	t5_t10_mem0 += MM_MEM[0]

	t5_t10_mem1 = S.Task('t5_t10_mem1', length=1, delay_cost=1)
	S += t5_t10_mem1 >= 49
	t5_t10_mem1 += MM_MEM[1]

	t5_t20 = S.Task('t5_t20', length=1, delay_cost=1)
	S += t5_t20 >= 49
	t5_t20 += MAS[4]

	t5_t6_t0_in = S.Task('t5_t6_t0_in', length=1, delay_cost=1)
	S += t5_t6_t0_in >= 49
	t5_t6_t0_in += MM_in[0]

	t5_t6_t0_mem0 = S.Task('t5_t6_t0_mem0', length=1, delay_cost=1)
	S += t5_t6_t0_mem0 >= 49
	t5_t6_t0_mem0 += MAS_MEM[0]

	t5_t6_t0_mem1 = S.Task('t5_t6_t0_mem1', length=1, delay_cost=1)
	S += t5_t6_t0_mem1 >= 49
	t5_t6_t0_mem1 += MAS_MEM[3]

	t5_t6_t2 = S.Task('t5_t6_t2', length=1, delay_cost=1)
	S += t5_t6_t2 >= 49
	t5_t6_t2 += MAS[3]

	t5_t10 = S.Task('t5_t10', length=1, delay_cost=1)
	S += t5_t10 >= 50
	t5_t10 += MAS[4]

	t5_t1_t4_in = S.Task('t5_t1_t4_in', length=1, delay_cost=1)
	S += t5_t1_t4_in >= 50
	t5_t1_t4_in += MM_in[0]

	t5_t1_t4_mem0 = S.Task('t5_t1_t4_mem0', length=1, delay_cost=1)
	S += t5_t1_t4_mem0 >= 50
	t5_t1_t4_mem0 += MAS_MEM[2]

	t5_t1_t4_mem1 = S.Task('t5_t1_t4_mem1', length=1, delay_cost=1)
	S += t5_t1_t4_mem1 >= 50
	t5_t1_t4_mem1 += MAS_MEM[1]

	t5_t2_t5_mem0 = S.Task('t5_t2_t5_mem0', length=1, delay_cost=1)
	S += t5_t2_t5_mem0 >= 50
	t5_t2_t5_mem0 += MM_MEM[0]

	t5_t2_t5_mem1 = S.Task('t5_t2_t5_mem1', length=1, delay_cost=1)
	S += t5_t2_t5_mem1 >= 50
	t5_t2_t5_mem1 += MM_MEM[1]

	t5_t6_t0 = S.Task('t5_t6_t0', length=7, delay_cost=1)
	S += t5_t6_t0 >= 50
	t5_t6_t0 += MM[0]

	t4_t6_t4_in = S.Task('t4_t6_t4_in', length=1, delay_cost=1)
	S += t4_t6_t4_in >= 51
	t4_t6_t4_in += MM_in[0]

	t4_t6_t4_mem0 = S.Task('t4_t6_t4_mem0', length=1, delay_cost=1)
	S += t4_t6_t4_mem0 >= 51
	t4_t6_t4_mem0 += MAS_MEM[6]

	t4_t6_t4_mem1 = S.Task('t4_t6_t4_mem1', length=1, delay_cost=1)
	S += t4_t6_t4_mem1 >= 51
	t4_t6_t4_mem1 += MAS_MEM[1]

	t5_t1_t4 = S.Task('t5_t1_t4', length=7, delay_cost=1)
	S += t5_t1_t4 >= 51
	t5_t1_t4 += MM[0]

	t5_t2_t5 = S.Task('t5_t2_t5', length=1, delay_cost=1)
	S += t5_t2_t5 >= 51
	t5_t2_t5 += MAS[4]

	t5_t80_mem0 = S.Task('t5_t80_mem0', length=1, delay_cost=1)
	S += t5_t80_mem0 >= 51
	t5_t80_mem0 += MM_MEM[0]

	t5_t80_mem1 = S.Task('t5_t80_mem1', length=1, delay_cost=1)
	S += t5_t80_mem1 >= 51
	t5_t80_mem1 += MM_MEM[1]

	t4_t6_t4 = S.Task('t4_t6_t4', length=7, delay_cost=1)
	S += t4_t6_t4 >= 52
	t4_t6_t4 += MM[0]

	t520_mem0 = S.Task('t520_mem0', length=1, delay_cost=1)
	S += t520_mem0 >= 52
	t520_mem0 += MAS_MEM[2]

	t520_mem1 = S.Task('t520_mem1', length=1, delay_cost=1)
	S += t520_mem1 >= 52
	t520_mem1 += MAS_MEM[9]

	t5_t00_mem0 = S.Task('t5_t00_mem0', length=1, delay_cost=1)
	S += t5_t00_mem0 >= 52
	t5_t00_mem0 += MM_MEM[0]

	t5_t00_mem1 = S.Task('t5_t00_mem1', length=1, delay_cost=1)
	S += t5_t00_mem1 >= 52
	t5_t00_mem1 += MM_MEM[1]

	t5_t6_t4_in = S.Task('t5_t6_t4_in', length=1, delay_cost=1)
	S += t5_t6_t4_in >= 52
	t5_t6_t4_in += MM_in[0]

	t5_t6_t4_mem0 = S.Task('t5_t6_t4_mem0', length=1, delay_cost=1)
	S += t5_t6_t4_mem0 >= 52
	t5_t6_t4_mem0 += MAS_MEM[6]

	t5_t6_t4_mem1 = S.Task('t5_t6_t4_mem1', length=1, delay_cost=1)
	S += t5_t6_t4_mem1 >= 52
	t5_t6_t4_mem1 += MAS_MEM[5]

	t5_t80 = S.Task('t5_t80', length=1, delay_cost=1)
	S += t5_t80 >= 52
	t5_t80 += MAS[1]

	t520 = S.Task('t520', length=1, delay_cost=1)
	S += t520 >= 53
	t520 += MAS[1]

	t5_t00 = S.Task('t5_t00', length=1, delay_cost=1)
	S += t5_t00 >= 53
	t5_t00 += MAS[2]

	t5_t0_t5_mem0 = S.Task('t5_t0_t5_mem0', length=1, delay_cost=1)
	S += t5_t0_t5_mem0 >= 53
	t5_t0_t5_mem0 += MM_MEM[0]

	t5_t0_t5_mem1 = S.Task('t5_t0_t5_mem1', length=1, delay_cost=1)
	S += t5_t0_t5_mem1 >= 53
	t5_t0_t5_mem1 += MM_MEM[1]

	t5_t6_t1_in = S.Task('t5_t6_t1_in', length=1, delay_cost=1)
	S += t5_t6_t1_in >= 53
	t5_t6_t1_in += MM_in[0]

	t5_t6_t1_mem0 = S.Task('t5_t6_t1_mem0', length=1, delay_cost=1)
	S += t5_t6_t1_mem0 >= 53
	t5_t6_t1_mem0 += MAS_MEM[0]

	t5_t6_t1_mem1 = S.Task('t5_t6_t1_mem1', length=1, delay_cost=1)
	S += t5_t6_t1_mem1 >= 53
	t5_t6_t1_mem1 += MAS_MEM[5]

	t5_t6_t4 = S.Task('t5_t6_t4', length=7, delay_cost=1)
	S += t5_t6_t4 >= 53
	t5_t6_t4 += MM[0]

	t5_t70_mem0 = S.Task('t5_t70_mem0', length=1, delay_cost=1)
	S += t5_t70_mem0 >= 53
	t5_t70_mem0 += MAS_MEM[4]

	t5_t70_mem1 = S.Task('t5_t70_mem1', length=1, delay_cost=1)
	S += t5_t70_mem1 >= 53
	t5_t70_mem1 += MAS_MEM[9]

	t5_t0_t5 = S.Task('t5_t0_t5', length=1, delay_cost=1)
	S += t5_t0_t5 >= 54
	t5_t0_t5 += MAS[1]

	t5_t6_t1 = S.Task('t5_t6_t1', length=7, delay_cost=1)
	S += t5_t6_t1 >= 54
	t5_t6_t1 += MM[0]

	t5_t70 = S.Task('t5_t70', length=1, delay_cost=1)
	S += t5_t70 >= 54
	t5_t70 += MAS[2]

	t5_t8_t5_mem0 = S.Task('t5_t8_t5_mem0', length=1, delay_cost=1)
	S += t5_t8_t5_mem0 >= 54
	t5_t8_t5_mem0 += MM_MEM[0]

	t5_t8_t5_mem1 = S.Task('t5_t8_t5_mem1', length=1, delay_cost=1)
	S += t5_t8_t5_mem1 >= 54
	t5_t8_t5_mem1 += MM_MEM[1]

	t5_t01_mem0 = S.Task('t5_t01_mem0', length=1, delay_cost=1)
	S += t5_t01_mem0 >= 55
	t5_t01_mem0 += MM_MEM[0]

	t5_t01_mem1 = S.Task('t5_t01_mem1', length=1, delay_cost=1)
	S += t5_t01_mem1 >= 55
	t5_t01_mem1 += MAS_MEM[3]

	t5_t8_t5 = S.Task('t5_t8_t5', length=1, delay_cost=1)
	S += t5_t8_t5 >= 55
	t5_t8_t5 += MAS[0]

	t5_t01 = S.Task('t5_t01', length=1, delay_cost=1)
	S += t5_t01 >= 56
	t5_t01 += MAS[0]

	t5_t21_mem0 = S.Task('t5_t21_mem0', length=1, delay_cost=1)
	S += t5_t21_mem0 >= 56
	t5_t21_mem0 += MM_MEM[0]

	t5_t21_mem1 = S.Task('t5_t21_mem1', length=1, delay_cost=1)
	S += t5_t21_mem1 >= 56
	t5_t21_mem1 += MAS_MEM[9]

	t5_t11_mem0 = S.Task('t5_t11_mem0', length=1, delay_cost=1)
	S += t5_t11_mem0 >= 57
	t5_t11_mem0 += MM_MEM[0]

	t5_t11_mem1 = S.Task('t5_t11_mem1', length=1, delay_cost=1)
	S += t5_t11_mem1 >= 57
	t5_t11_mem1 += MAS_MEM[5]

	t5_t21 = S.Task('t5_t21', length=1, delay_cost=1)
	S += t5_t21 >= 57
	t5_t21 += MAS[3]

	t4_t61_mem0 = S.Task('t4_t61_mem0', length=1, delay_cost=1)
	S += t4_t61_mem0 >= 58
	t4_t61_mem0 += MM_MEM[0]

	t4_t61_mem1 = S.Task('t4_t61_mem1', length=1, delay_cost=1)
	S += t4_t61_mem1 >= 58
	t4_t61_mem1 += MAS_MEM[3]

	t5_t11 = S.Task('t5_t11', length=1, delay_cost=1)
	S += t5_t11 >= 58
	t5_t11 += MAS[2]

	t4_t61 = S.Task('t4_t61', length=1, delay_cost=1)
	S += t4_t61 >= 59
	t4_t61 += MAS[3]

	t5_t81_mem0 = S.Task('t5_t81_mem0', length=1, delay_cost=1)
	S += t5_t81_mem0 >= 59
	t5_t81_mem0 += MM_MEM[0]

	t5_t81_mem1 = S.Task('t5_t81_mem1', length=1, delay_cost=1)
	S += t5_t81_mem1 >= 59
	t5_t81_mem1 += MAS_MEM[1]

	t5_t60_mem0 = S.Task('t5_t60_mem0', length=1, delay_cost=1)
	S += t5_t60_mem0 >= 60
	t5_t60_mem0 += MM_MEM[0]

	t5_t60_mem1 = S.Task('t5_t60_mem1', length=1, delay_cost=1)
	S += t5_t60_mem1 >= 60
	t5_t60_mem1 += MM_MEM[1]

	t5_t81 = S.Task('t5_t81', length=1, delay_cost=1)
	S += t5_t81 >= 60
	t5_t81 += MAS[0]

	t5_t60 = S.Task('t5_t60', length=1, delay_cost=1)
	S += t5_t60 >= 61
	t5_t60 += MAS[1]

	t5_t6_t5_mem0 = S.Task('t5_t6_t5_mem0', length=1, delay_cost=1)
	S += t5_t6_t5_mem0 >= 61
	t5_t6_t5_mem0 += MM_MEM[0]

	t5_t6_t5_mem1 = S.Task('t5_t6_t5_mem1', length=1, delay_cost=1)
	S += t5_t6_t5_mem1 >= 61
	t5_t6_t5_mem1 += MM_MEM[1]

	t5_t6_t5 = S.Task('t5_t6_t5', length=1, delay_cost=1)
	S += t5_t6_t5 >= 62
	t5_t6_t5 += MAS[2]


	# new tasks
	t400 = S.Task('t400', length=1, delay_cost=1)
	t400 += alt(MAS)

	t400_mem0 = S.Task('t400_mem0', length=1, delay_cost=1)
	t400_mem0 += MAS_MEM[4]
	S += 15 < t400_mem0
	S += t400_mem0 <= t400

	t400_mem1 = S.Task('t400_mem1', length=1, delay_cost=1)
	t400_mem1 += MAS_MEM[5]
	S += 45 < t400_mem1
	S += t400_mem1 <= t400

	t401 = S.Task('t401', length=1, delay_cost=1)
	t401 += alt(MAS)

	t401_mem0 = S.Task('t401_mem0', length=1, delay_cost=1)
	t401_mem0 += MAS_MEM[2]
	S += 26 < t401_mem0
	S += t401_mem0 <= t401

	t401_mem1 = S.Task('t401_mem1', length=1, delay_cost=1)
	t401_mem1 += MAS_MEM[1]
	S += 45 < t401_mem1
	S += t401_mem1 <= t401

	t411 = S.Task('t411', length=1, delay_cost=1)
	t411 += alt(MAS)

	t411_mem0 = S.Task('t411_mem0', length=1, delay_cost=1)
	t411_mem0 += MAS_MEM[6]
	S += 59 < t411_mem0
	S += t411_mem0 <= t411

	t411_mem1 = S.Task('t411_mem1', length=1, delay_cost=1)
	t411_mem1 += MAS_MEM[3]
	S += 28 < t411_mem1
	S += t411_mem1 <= t411

	t5_t100 = S.Task('t5_t100', length=1, delay_cost=1)
	t5_t100 += alt(MAS)

	t5_t100_mem0 = S.Task('t5_t100_mem0', length=1, delay_cost=1)
	t5_t100_mem0 += MAS_MEM[8]
	S += 49 < t5_t100_mem0
	S += t5_t100_mem0 <= t5_t100

	t5_t100_mem1 = S.Task('t5_t100_mem1', length=1, delay_cost=1)
	t5_t100_mem1 += MAS_MEM[7]
	S += 57 < t5_t100_mem1
	S += t5_t100_mem1 <= t5_t100

	t5_t101 = S.Task('t5_t101', length=1, delay_cost=1)
	t5_t101 += alt(MAS)

	t5_t101_mem0 = S.Task('t5_t101_mem0', length=1, delay_cost=1)
	t5_t101_mem0 += MAS_MEM[6]
	S += 57 < t5_t101_mem0
	S += t5_t101_mem0 <= t5_t101

	t5_t101_mem1 = S.Task('t5_t101_mem1', length=1, delay_cost=1)
	t5_t101_mem1 += MAS_MEM[9]
	S += 49 < t5_t101_mem1
	S += t5_t101_mem1 <= t5_t101

	t5_t61 = S.Task('t5_t61', length=1, delay_cost=1)
	t5_t61 += alt(MAS)

	t5_t61_mem0 = S.Task('t5_t61_mem0', length=1, delay_cost=1)
	t5_t61_mem0 += MM_MEM[0]
	S += 59 < t5_t61_mem0
	S += t5_t61_mem0 <= t5_t61

	t5_t61_mem1 = S.Task('t5_t61_mem1', length=1, delay_cost=1)
	t5_t61_mem1 += MAS_MEM[5]
	S += 62 < t5_t61_mem1
	S += t5_t61_mem1 <= t5_t61

	t5_t71 = S.Task('t5_t71', length=1, delay_cost=1)
	t5_t71 += alt(MAS)

	t5_t71_mem0 = S.Task('t5_t71_mem0', length=1, delay_cost=1)
	t5_t71_mem0 += MAS_MEM[0]
	S += 56 < t5_t71_mem0
	S += t5_t71_mem0 <= t5_t71

	t5_t71_mem1 = S.Task('t5_t71_mem1', length=1, delay_cost=1)
	t5_t71_mem1 += MAS_MEM[5]
	S += 58 < t5_t71_mem1
	S += t5_t71_mem1 <= t5_t71

	t510 = S.Task('t510', length=1, delay_cost=1)
	t510 += alt(MAS)

	t510_mem0 = S.Task('t510_mem0', length=1, delay_cost=1)
	t510_mem0 += MAS_MEM[2]
	S += 61 < t510_mem0
	S += t510_mem0 <= t510

	t510_mem1 = S.Task('t510_mem1', length=1, delay_cost=1)
	t510_mem1 += MAS_MEM[5]
	S += 54 < t510_mem1
	S += t510_mem1 <= t510

	t521 = S.Task('t521', length=1, delay_cost=1)
	t521 += alt(MAS)

	t521_mem0 = S.Task('t521_mem0', length=1, delay_cost=1)
	t521_mem0 += MAS_MEM[0]
	S += 60 < t521_mem0
	S += t521_mem0 <= t521

	t521_mem1 = S.Task('t521_mem1', length=1, delay_cost=1)
	t521_mem1 += MAS_MEM[5]
	S += 58 < t521_mem1
	S += t521_mem1 <= t521

	t150 = S.Task('t150', length=1, delay_cost=1)
	t150 += alt(MAS)

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += MAS_MEM[2]
	S += 18 < t150_mem0
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += MAS_MEM[5]
	S += 47 < t150_mem1
	S += t150_mem1 <= t150

	t161 = S.Task('t161', length=1, delay_cost=1)
	t161 += alt(MAS)

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += MAS_MEM[8]
	S += 23 < t161_mem0
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += MAS_MEM[1]
	S += 38 < t161_mem1
	S += t161_mem1 <= t161

	c210 = S.Task('c210', length=1, delay_cost=1)
	c210 += alt(MAS)

	S += 33<c210

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MAS_MEM[2]
	S += 53 < c210_mem0
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MAS_MEM[5]
	S += 32 < c210_mem1
	S += c210_mem1 <= c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(MAS)

	S += 40<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += MAS_MEM[4]
	S += 26 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAS_MEM[5]
	S += 47 < c200_mem1
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c111 = S.Task('c111', length=1, delay_cost=1)
	c111 += alt(MAS)

	S += 39<c111

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += MAS_MEM[2]
	S += 34 < c111_mem0
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += MAS_MEM[1]
	S += 38 < c111_mem1
	S += c111_mem1 <= c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	t500 = S.Task('t500', length=1, delay_cost=1)
	t500 += alt(MAS)

	t500_mem0 = S.Task('t500_mem0', length=1, delay_cost=1)
	t500_mem0 += MAS_MEM[4]
	S += 53 < t500_mem0
	S += t500_mem0 <= t500

	t500_mem1 = S.Task('t500_mem1', length=1, delay_cost=1)
	t500_mem1 += alt(MAS_MEM)
	S += (t5_t100*MAS[0])-1 < t500_mem1*MAS_MEM[1]
	S += (t5_t100*MAS[1])-1 < t500_mem1*MAS_MEM[3]
	S += (t5_t100*MAS[2])-1 < t500_mem1*MAS_MEM[5]
	S += (t5_t100*MAS[3])-1 < t500_mem1*MAS_MEM[7]
	S += (t5_t100*MAS[4])-1 < t500_mem1*MAS_MEM[9]
	S += t500_mem1 <= t500

	t501 = S.Task('t501', length=1, delay_cost=1)
	t501 += alt(MAS)

	t501_mem0 = S.Task('t501_mem0', length=1, delay_cost=1)
	t501_mem0 += MAS_MEM[0]
	S += 56 < t501_mem0
	S += t501_mem0 <= t501

	t501_mem1 = S.Task('t501_mem1', length=1, delay_cost=1)
	t501_mem1 += alt(MAS_MEM)
	S += (t5_t101*MAS[0])-1 < t501_mem1*MAS_MEM[1]
	S += (t5_t101*MAS[1])-1 < t501_mem1*MAS_MEM[3]
	S += (t5_t101*MAS[2])-1 < t501_mem1*MAS_MEM[5]
	S += (t5_t101*MAS[3])-1 < t501_mem1*MAS_MEM[7]
	S += (t5_t101*MAS[4])-1 < t501_mem1*MAS_MEM[9]
	S += t501_mem1 <= t501

	t511 = S.Task('t511', length=1, delay_cost=1)
	t511 += alt(MAS)

	t511_mem0 = S.Task('t511_mem0', length=1, delay_cost=1)
	t511_mem0 += alt(MAS_MEM)
	S += (t5_t61*MAS[0])-1 < t511_mem0*MAS_MEM[0]
	S += (t5_t61*MAS[1])-1 < t511_mem0*MAS_MEM[2]
	S += (t5_t61*MAS[2])-1 < t511_mem0*MAS_MEM[4]
	S += (t5_t61*MAS[3])-1 < t511_mem0*MAS_MEM[6]
	S += (t5_t61*MAS[4])-1 < t511_mem0*MAS_MEM[8]
	S += t511_mem0 <= t511

	t511_mem1 = S.Task('t511_mem1', length=1, delay_cost=1)
	t511_mem1 += alt(MAS_MEM)
	S += (t5_t71*MAS[0])-1 < t511_mem1*MAS_MEM[1]
	S += (t5_t71*MAS[1])-1 < t511_mem1*MAS_MEM[3]
	S += (t5_t71*MAS[2])-1 < t511_mem1*MAS_MEM[5]
	S += (t5_t71*MAS[3])-1 < t511_mem1*MAS_MEM[7]
	S += (t5_t71*MAS[4])-1 < t511_mem1*MAS_MEM[9]
	S += t511_mem1 <= t511

	t140 = S.Task('t140', length=1, delay_cost=1)
	t140 += alt(MAS)

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += MAS_MEM[4]
	S += 26 < t140_mem0
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += alt(MAS_MEM)
	S += (t400*MAS[0])-1 < t140_mem1*MAS_MEM[1]
	S += (t400*MAS[1])-1 < t140_mem1*MAS_MEM[3]
	S += (t400*MAS[2])-1 < t140_mem1*MAS_MEM[5]
	S += (t400*MAS[3])-1 < t140_mem1*MAS_MEM[7]
	S += (t400*MAS[4])-1 < t140_mem1*MAS_MEM[9]
	S += t140_mem1 <= t140

	t141 = S.Task('t141', length=1, delay_cost=1)
	t141 += alt(MAS)

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += MAS_MEM[2]
	S += 27 < t141_mem0
	S += t141_mem0 <= t141

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	t141_mem1 += alt(MAS_MEM)
	S += (t401*MAS[0])-1 < t141_mem1*MAS_MEM[1]
	S += (t401*MAS[1])-1 < t141_mem1*MAS_MEM[3]
	S += (t401*MAS[2])-1 < t141_mem1*MAS_MEM[5]
	S += (t401*MAS[3])-1 < t141_mem1*MAS_MEM[7]
	S += (t401*MAS[4])-1 < t141_mem1*MAS_MEM[9]
	S += t141_mem1 <= t141

	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(MAS)

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[2]
	S += 34 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(MAS_MEM)
	S += (t411*MAS[0])-1 < t151_mem1*MAS_MEM[1]
	S += (t411*MAS[1])-1 < t151_mem1*MAS_MEM[3]
	S += (t411*MAS[2])-1 < t151_mem1*MAS_MEM[5]
	S += (t411*MAS[3])-1 < t151_mem1*MAS_MEM[7]
	S += (t411*MAS[4])-1 < t151_mem1*MAS_MEM[9]
	S += t151_mem1 <= t151

	c010 = S.Task('c010', length=1, delay_cost=1)
	c010 += alt(MAS)

	S += 40<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += alt(MAS_MEM)
	S += (t510*MAS[0])-1 < c010_mem0*MAS_MEM[0]
	S += (t510*MAS[1])-1 < c010_mem0*MAS_MEM[2]
	S += (t510*MAS[2])-1 < c010_mem0*MAS_MEM[4]
	S += (t510*MAS[3])-1 < c010_mem0*MAS_MEM[6]
	S += (t510*MAS[4])-1 < c010_mem0*MAS_MEM[8]
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += alt(MAS_MEM)
	S += (t150*MAS[0])-1 < c010_mem1*MAS_MEM[1]
	S += (t150*MAS[1])-1 < c010_mem1*MAS_MEM[3]
	S += (t150*MAS[2])-1 < c010_mem1*MAS_MEM[5]
	S += (t150*MAS[3])-1 < c010_mem1*MAS_MEM[7]
	S += (t150*MAS[4])-1 < c010_mem1*MAS_MEM[9]
	S += c010_mem1 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(MAS)

	S += 39<c211

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(MAS_MEM)
	S += (t521*MAS[0])-1 < c211_mem0*MAS_MEM[0]
	S += (t521*MAS[1])-1 < c211_mem0*MAS_MEM[2]
	S += (t521*MAS[2])-1 < c211_mem0*MAS_MEM[4]
	S += (t521*MAS[3])-1 < c211_mem0*MAS_MEM[6]
	S += (t521*MAS[4])-1 < c211_mem0*MAS_MEM[8]
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < c211_mem1*MAS_MEM[1]
	S += (t161*MAS[1])-1 < c211_mem1*MAS_MEM[3]
	S += (t161*MAS[2])-1 < c211_mem1*MAS_MEM[5]
	S += (t161*MAS[3])-1 < c211_mem1*MAS_MEM[7]
	S += (t161*MAS[4])-1 < c211_mem1*MAS_MEM[9]
	S += c211_mem1 <= c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)

	S += 48<c000

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[4]
	S += 24 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (t400*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (t400*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (t400*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (t400*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += (t400*MAS[4])-1 < c000_mem1*MAS_MEM[9]
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)

	S += 47<c001

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[6]
	S += 24 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (t401*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += (t401*MAS[1])-1 < c001_mem1*MAS_MEM[3]
	S += (t401*MAS[2])-1 < c001_mem1*MAS_MEM[5]
	S += (t401*MAS[3])-1 < c001_mem1*MAS_MEM[7]
	S += (t401*MAS[4])-1 < c001_mem1*MAS_MEM[9]
	S += c001_mem1 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(MAS)

	S += 34<c201

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += MAS_MEM[2]
	S += 27 < c201_mem0
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += alt(MAS_MEM)
	S += (t411*MAS[0])-1 < c201_mem1*MAS_MEM[1]
	S += (t411*MAS[1])-1 < c201_mem1*MAS_MEM[3]
	S += (t411*MAS[2])-1 < c201_mem1*MAS_MEM[5]
	S += (t411*MAS[3])-1 < c201_mem1*MAS_MEM[7]
	S += (t411*MAS[4])-1 < c201_mem1*MAS_MEM[9]
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(MAS)

	S += 37<c100

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(MAS_MEM)
	S += (t500*MAS[0])-1 < c100_mem0*MAS_MEM[0]
	S += (t500*MAS[1])-1 < c100_mem0*MAS_MEM[2]
	S += (t500*MAS[2])-1 < c100_mem0*MAS_MEM[4]
	S += (t500*MAS[3])-1 < c100_mem0*MAS_MEM[6]
	S += (t500*MAS[4])-1 < c100_mem0*MAS_MEM[8]
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < c100_mem1*MAS_MEM[1]
	S += (t140*MAS[1])-1 < c100_mem1*MAS_MEM[3]
	S += (t140*MAS[2])-1 < c100_mem1*MAS_MEM[5]
	S += (t140*MAS[3])-1 < c100_mem1*MAS_MEM[7]
	S += (t140*MAS[4])-1 < c100_mem1*MAS_MEM[9]
	S += c100_mem1 <= c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(MAS)

	S += 28<c101

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MAS_MEM)
	S += (t501*MAS[0])-1 < c101_mem0*MAS_MEM[0]
	S += (t501*MAS[1])-1 < c101_mem0*MAS_MEM[2]
	S += (t501*MAS[2])-1 < c101_mem0*MAS_MEM[4]
	S += (t501*MAS[3])-1 < c101_mem0*MAS_MEM[6]
	S += (t501*MAS[4])-1 < c101_mem0*MAS_MEM[8]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < c101_mem1*MAS_MEM[1]
	S += (t141*MAS[1])-1 < c101_mem1*MAS_MEM[3]
	S += (t141*MAS[2])-1 < c101_mem1*MAS_MEM[5]
	S += (t141*MAS[3])-1 < c101_mem1*MAS_MEM[7]
	S += (t141*MAS[4])-1 < c101_mem1*MAS_MEM[9]
	S += c101_mem1 <= c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(MAS)

	S += 32<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(MAS_MEM)
	S += (t511*MAS[0])-1 < c011_mem0*MAS_MEM[0]
	S += (t511*MAS[1])-1 < c011_mem0*MAS_MEM[2]
	S += (t511*MAS[2])-1 < c011_mem0*MAS_MEM[4]
	S += (t511*MAS[3])-1 < c011_mem0*MAS_MEM[6]
	S += (t511*MAS[4])-1 < c011_mem0*MAS_MEM[8]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(MAS_MEM)
	S += (t151*MAS[0])-1 < c011_mem1*MAS_MEM[1]
	S += (t151*MAS[1])-1 < c011_mem1*MAS_MEM[3]
	S += (t151*MAS[2])-1 < c011_mem1*MAS_MEM[5]
	S += (t151*MAS[3])-1 < c011_mem1*MAS_MEM[7]
	S += (t151*MAS[4])-1 < c011_mem1*MAS_MEM[9]
	S += c011_mem1 <= c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage7MM1_stage1MAS5/SPARSE/schedule5.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

