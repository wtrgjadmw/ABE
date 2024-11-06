from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 171
	S = Scenario("schedule7", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	S += c_t0_t3_t1_in >= 0
	c_t0_t3_t1_in += MM_in[0]

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem0 >= 0
	c_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem1 >= 0
	c_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=7, delay_cost=1)
	S += c_t0_t3_t1 >= 1
	c_t0_t3_t1 += MM[0]

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	S += c_t1_t3_t1_in >= 1
	c_t1_t3_t1_in += MM_in[0]

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem0 >= 1
	c_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem1 >= 1
	c_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	S += c_t1_t3_t0_in >= 2
	c_t1_t3_t0_in += MM_in[0]

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem0 >= 2
	c_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem1 >= 2
	c_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=7, delay_cost=1)
	S += c_t1_t3_t1 >= 2
	c_t1_t3_t1 += MM[0]

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	S += c_t0_t3_t0_in >= 3
	c_t0_t3_t0_in += MM_in[0]

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem0 >= 3
	c_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem1 >= 3
	c_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=7, delay_cost=1)
	S += c_t1_t3_t0 >= 3
	c_t1_t3_t0 += MM[0]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 4
	c_t0_t11_mem0 += MAIN_MEM_r[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 4
	c_t0_t11_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=7, delay_cost=1)
	S += c_t0_t3_t0 >= 4
	c_t0_t3_t0 += MM[0]

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	S += c_t0_t11 >= 5
	c_t0_t11 += MAS[0]

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem0 >= 5
	c_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem1 >= 5
	c_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	S += c_t1_a1_1_mem0 >= 6
	c_t1_a1_1_mem0 += MAIN_MEM_r[0]

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	S += c_t1_a1_1_mem1 >= 6
	c_t1_a1_1_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=1, delay_cost=1)
	S += c_t1_t3_t2 >= 6
	c_t1_t3_t2 += MAS[1]

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=1, delay_cost=1)
	S += c_t1_a1_1 >= 7
	c_t1_a1_1 += MAS[1]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 7
	c_t2_t11_mem0 += MAIN_MEM_r[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 7
	c_t2_t11_mem1 += MAIN_MEM_r[1]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 8
	c_t2_t10_mem0 += MAIN_MEM_r[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 8
	c_t2_t10_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	S += c_t2_t11 >= 8
	c_t2_t11 += MAS[0]

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem0 >= 9
	c_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem1 >= 9
	c_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t5_mem0 = S.Task('c_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem0 >= 9
	c_t1_t3_t5_mem0 += MM_MEM[0]

	c_t1_t3_t5_mem1 = S.Task('c_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem1 >= 9
	c_t1_t3_t5_mem1 += MM_MEM[1]

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	S += c_t2_t10 >= 9
	c_t2_t10 += MAS[1]

	c_t2_t2_t3_mem0 = S.Task('c_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem0 >= 9
	c_t2_t2_t3_mem0 += MAS_MEM[2]

	c_t2_t2_t3_mem1 = S.Task('c_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem1 >= 9
	c_t2_t2_t3_mem1 += MAS_MEM[1]

	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	S += c_t0_a1_0_mem0 >= 10
	c_t0_a1_0_mem0 += MAIN_MEM_r[0]

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	S += c_t0_a1_0_mem1 >= 10
	c_t0_a1_0_mem1 += MAIN_MEM_r[1]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 10
	c_t0_t30_mem0 += MM_MEM[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 10
	c_t0_t30_mem1 += MM_MEM[1]

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=1, delay_cost=1)
	S += c_t0_t3_t2 >= 10
	c_t0_t3_t2 += MAS[2]

	c_t1_t3_t5 = S.Task('c_t1_t3_t5', length=1, delay_cost=1)
	S += c_t1_t3_t5 >= 10
	c_t1_t3_t5 += MAS[0]

	c_t2_t2_t3 = S.Task('c_t2_t2_t3', length=1, delay_cost=1)
	S += c_t2_t2_t3 >= 10
	c_t2_t2_t3 += MAS[3]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 11
	c_t010_mem0 += MAS_MEM[2]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 11
	c_t010_mem1 += MAS_MEM[3]

	c_t0_a1_0 = S.Task('c_t0_a1_0', length=1, delay_cost=1)
	S += c_t0_a1_0 >= 11
	c_t0_a1_0 += MAS[0]

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 11
	c_t0_t30 += MAS[1]

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem0 >= 11
	c_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem1 >= 11
	c_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t5_mem0 = S.Task('c_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem0 >= 11
	c_t0_t3_t5_mem0 += MM_MEM[0]

	c_t0_t3_t5_mem1 = S.Task('c_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem1 >= 11
	c_t0_t3_t5_mem1 += MM_MEM[1]

	c_t010 = S.Task('c_t010', length=1, delay_cost=1)
	S += c_t010 >= 12
	c_t010 += MAS[2]

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=1, delay_cost=1)
	S += c_t0_t3_t3 >= 12
	c_t0_t3_t3 += MAS[0]

	c_t0_t3_t4_in = S.Task('c_t0_t3_t4_in', length=1, delay_cost=1)
	S += c_t0_t3_t4_in >= 12
	c_t0_t3_t4_in += MM_in[0]

	c_t0_t3_t4_mem0 = S.Task('c_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem0 >= 12
	c_t0_t3_t4_mem0 += MAS_MEM[4]

	c_t0_t3_t4_mem1 = S.Task('c_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem1 >= 12
	c_t0_t3_t4_mem1 += MAS_MEM[1]

	c_t0_t3_t5 = S.Task('c_t0_t3_t5', length=1, delay_cost=1)
	S += c_t0_t3_t5 >= 12
	c_t0_t3_t5 += MAS[3]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 12
	c_t1_t30_mem0 += MM_MEM[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 12
	c_t1_t30_mem1 += MM_MEM[1]

	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	S += c_t2_a1_1_mem0 >= 12
	c_t2_a1_1_mem0 += MAIN_MEM_r[0]

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	S += c_t2_a1_1_mem1 >= 12
	c_t2_a1_1_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t4 = S.Task('c_t0_t3_t4', length=7, delay_cost=1)
	S += c_t0_t3_t4 >= 13
	c_t0_t3_t4 += MM[0]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 13
	c_t110_mem0 += MAS_MEM[0]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 13
	c_t110_mem1 += MAS_MEM[1]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 13
	c_t1_t11_mem0 += MAIN_MEM_r[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 13
	c_t1_t11_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 13
	c_t1_t30 += MAS[0]

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=1, delay_cost=1)
	S += c_t2_a1_1 >= 13
	c_t2_a1_1 += MAS[3]

	c_s0010_mem0 = S.Task('c_s0010_mem0', length=1, delay_cost=1)
	S += c_s0010_mem0 >= 14
	c_s0010_mem0 += MAS_MEM[4]

	c_s0010_mem1 = S.Task('c_s0010_mem1', length=1, delay_cost=1)
	S += c_s0010_mem1 >= 14
	c_s0010_mem1 += MAS_MEM[7]

	c_t110 = S.Task('c_t110', length=1, delay_cost=1)
	S += c_t110 >= 14
	c_t110 += MAS[3]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 14
	c_t1_t10_mem0 += MAIN_MEM_r[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 14
	c_t1_t10_mem1 += MAIN_MEM_r[1]

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	S += c_t1_t11 >= 14
	c_t1_t11 += MAS[0]

	c_s0010 = S.Task('c_s0010', length=1, delay_cost=1)
	S += c_s0010 >= 15
	c_s0010 += MAS[0]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 15
	c_t0_t10_mem0 += MAIN_MEM_r[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 15
	c_t0_t10_mem1 += MAIN_MEM_r[1]

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	S += c_t1_t10 >= 15
	c_t1_t10 += MAS[2]

	c_t1_t2_t3_mem0 = S.Task('c_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem0 >= 15
	c_t1_t2_t3_mem0 += MAS_MEM[4]

	c_t1_t2_t3_mem1 = S.Task('c_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem1 >= 15
	c_t1_t2_t3_mem1 += MAS_MEM[1]

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	S += c_t0_t10 >= 16
	c_t0_t10 += MAS[0]

	c_t0_t2_t3_mem0 = S.Task('c_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem0 >= 16
	c_t0_t2_t3_mem0 += MAS_MEM[0]

	c_t0_t2_t3_mem1 = S.Task('c_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem1 >= 16
	c_t0_t2_t3_mem1 += MAS_MEM[1]

	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	S += c_t1_a1_0_mem0 >= 16
	c_t1_a1_0_mem0 += MAIN_MEM_r[0]

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	S += c_t1_a1_0_mem1 >= 16
	c_t1_a1_0_mem1 += MAIN_MEM_r[1]

	c_t1_t2_t3 = S.Task('c_t1_t2_t3', length=1, delay_cost=1)
	S += c_t1_t2_t3 >= 16
	c_t1_t2_t3 += MAS[1]

	c_t0_t2_t3 = S.Task('c_t0_t2_t3', length=1, delay_cost=1)
	S += c_t0_t2_t3 >= 17
	c_t0_t2_t3 += MAS[0]

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=1, delay_cost=1)
	S += c_t1_a1_0 >= 17
	c_t1_a1_0 += MAS[2]

	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	S += c_t2_a1_0_mem0 >= 17
	c_t2_a1_0_mem0 += MAIN_MEM_r[0]

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	S += c_t2_a1_0_mem1 >= 17
	c_t2_a1_0_mem1 += MAIN_MEM_r[1]

	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	S += c_t0_a1_1_mem0 >= 18
	c_t0_a1_1_mem0 += MAIN_MEM_r[0]

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	S += c_t0_a1_1_mem1 >= 18
	c_t0_a1_1_mem1 += MAIN_MEM_r[1]

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=1, delay_cost=1)
	S += c_t2_a1_0 >= 18
	c_t2_a1_0 += MAS[3]

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=1, delay_cost=1)
	S += c_t0_a1_1 >= 19
	c_t0_a1_1 += MAS[3]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 19
	c_t0_t31_mem0 += MM_MEM[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 19
	c_t0_t31_mem1 += MAS_MEM[7]

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem0 >= 19
	c_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem1 >= 19
	c_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 20
	c_t011_mem0 += MAS_MEM[2]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 20
	c_t011_mem1 += MAS_MEM[3]

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	S += c_t0_t31 >= 20
	c_t0_t31 += MAS[1]

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=1, delay_cost=1)
	S += c_t1_t3_t3 >= 20
	c_t1_t3_t3 += MAS[3]

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	S += c_t2_t3_t0_in >= 20
	c_t2_t3_t0_in += MM_in[0]

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem0 >= 20
	c_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem1 >= 20
	c_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t011 = S.Task('c_t011', length=1, delay_cost=1)
	S += c_t011 >= 21
	c_t011 += MAS[0]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 21
	c_t0_t40_mem0 += MAS_MEM[2]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 21
	c_t0_t40_mem1 += MAS_MEM[3]

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=7, delay_cost=1)
	S += c_t2_t3_t0 >= 21
	c_t2_t3_t0 += MM[0]

	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	S += c_t2_t3_t1_in >= 21
	c_t2_t3_t1_in += MM_in[0]

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem0 >= 21
	c_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem1 >= 21
	c_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t40 = S.Task('c_t0_t40', length=1, delay_cost=1)
	S += c_t0_t40 >= 22
	c_t0_t40 += MAS[1]

	c_t1_t3_t4_in = S.Task('c_t1_t3_t4_in', length=1, delay_cost=1)
	S += c_t1_t3_t4_in >= 22
	c_t1_t3_t4_in += MM_in[0]

	c_t1_t3_t4_mem0 = S.Task('c_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem0 >= 22
	c_t1_t3_t4_mem0 += MAS_MEM[2]

	c_t1_t3_t4_mem1 = S.Task('c_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem1 >= 22
	c_t1_t3_t4_mem1 += MAS_MEM[7]

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=7, delay_cost=1)
	S += c_t2_t3_t1 >= 22
	c_t2_t3_t1 += MM[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 22
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 22
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 23
	c_t0_t41_mem0 += MAS_MEM[2]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 23
	c_t0_t41_mem1 += MAS_MEM[3]

	c_t1_t3_t4 = S.Task('c_t1_t3_t4', length=7, delay_cost=1)
	S += c_t1_t3_t4 >= 23
	c_t1_t3_t4 += MM[0]

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	S += c_t3010 >= 23
	c_t3010 += MAS[2]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 23
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 23
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t0_t41 = S.Task('c_t0_t41', length=1, delay_cost=1)
	S += c_t0_t41 >= 24
	c_t0_t41 += MAS[2]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 24
	c_t0_t50_mem0 += MAS_MEM[2]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 24
	c_t0_t50_mem1 += MAS_MEM[3]

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem0 >= 24
	c_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem1 >= 24
	c_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	S += c_t5001 >= 24
	c_t5001 += MAS[3]

	c_t0_t50 = S.Task('c_t0_t50', length=1, delay_cost=1)
	S += c_t0_t50 >= 25
	c_t0_t50 += MAS[0]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	S += c_t0_t51_mem0 >= 25
	c_t0_t51_mem0 += MAS_MEM[2]

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	S += c_t0_t51_mem1 >= 25
	c_t0_t51_mem1 += MAS_MEM[5]

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=1, delay_cost=1)
	S += c_t2_t3_t3 >= 25
	c_t2_t3_t3 += MAS[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 25
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 25
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t0_t51 = S.Task('c_t0_t51', length=1, delay_cost=1)
	S += c_t0_t51 >= 26
	c_t0_t51 += MAS[2]

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	S += c_t3000 >= 26
	c_t3000 += MAS[3]

	c_t3_t3_t0_in = S.Task('c_t3_t3_t0_in', length=1, delay_cost=1)
	S += c_t3_t3_t0_in >= 26
	c_t3_t3_t0_in += MM_in[0]

	c_t3_t3_t0_mem0 = S.Task('c_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem0 >= 26
	c_t3_t3_t0_mem0 += MAS_MEM[6]

	c_t3_t3_t0_mem1 = S.Task('c_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem1 >= 26
	c_t3_t3_t0_mem1 += MAS_MEM[5]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 26
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 26
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 27
	c_t3_t10_mem0 += MAS_MEM[6]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 27
	c_t3_t10_mem1 += MAS_MEM[5]

	c_t3_t3_t0 = S.Task('c_t3_t3_t0', length=7, delay_cost=1)
	S += c_t3_t3_t0 >= 27
	c_t3_t3_t0 += MM[0]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 27
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 27
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	S += c_t5000 >= 27
	c_t5000 += MAS[1]

	c_t5_t3_t2_mem0 = S.Task('c_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem0 >= 27
	c_t5_t3_t2_mem0 += MAS_MEM[2]

	c_t5_t3_t2_mem1 = S.Task('c_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem1 >= 27
	c_t5_t3_t2_mem1 += MAS_MEM[7]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 28
	c_t2_t30_mem0 += MM_MEM[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 28
	c_t2_t30_mem1 += MM_MEM[1]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 28
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 28
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3_t10 = S.Task('c_t3_t10', length=1, delay_cost=1)
	S += c_t3_t10 >= 28
	c_t3_t10 += MAS[1]

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	S += c_t4000 >= 28
	c_t4000 += MAS[3]

	c_t5_t3_t2 = S.Task('c_t5_t3_t2', length=1, delay_cost=1)
	S += c_t5_t3_t2 >= 28
	c_t5_t3_t2 += MAS[0]

	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	S += c_t2_t30 >= 29
	c_t2_t30 += MAS[1]

	c_t2_t3_t5_mem0 = S.Task('c_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem0 >= 29
	c_t2_t3_t5_mem0 += MM_MEM[0]

	c_t2_t3_t5_mem1 = S.Task('c_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem1 >= 29
	c_t2_t3_t5_mem1 += MM_MEM[1]

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	S += c_t3011 >= 29
	c_t3011 += MAS[0]

	c_t3_a1_0_mem0 = S.Task('c_t3_a1_0_mem0', length=1, delay_cost=1)
	S += c_t3_a1_0_mem0 >= 29
	c_t3_a1_0_mem0 += MAS_MEM[4]

	c_t3_a1_0_mem1 = S.Task('c_t3_a1_0_mem1', length=1, delay_cost=1)
	S += c_t3_a1_0_mem1 >= 29
	c_t3_a1_0_mem1 += MAS_MEM[1]

	c_t3_a1_1_mem0 = S.Task('c_t3_a1_1_mem0', length=1, delay_cost=1)
	S += c_t3_a1_1_mem0 >= 29
	c_t3_a1_1_mem0 += MAS_MEM[0]

	c_t3_a1_1_mem1 = S.Task('c_t3_a1_1_mem1', length=1, delay_cost=1)
	S += c_t3_a1_1_mem1 >= 29
	c_t3_a1_1_mem1 += MAS_MEM[5]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 29
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 29
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 30
	c_t210_mem0 += MAS_MEM[2]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 30
	c_t210_mem1 += MAS_MEM[3]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem0 >= 30
	c_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem1 >= 30
	c_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t5 = S.Task('c_t2_t3_t5', length=1, delay_cost=1)
	S += c_t2_t3_t5 >= 30
	c_t2_t3_t5 += MAS[1]

	c_t3_a1_0 = S.Task('c_t3_a1_0', length=1, delay_cost=1)
	S += c_t3_a1_0 >= 30
	c_t3_a1_0 += MAS[2]

	c_t3_a1_1 = S.Task('c_t3_a1_1', length=1, delay_cost=1)
	S += c_t3_a1_1 >= 30
	c_t3_a1_1 += MAS[0]

	c_t3_t3_t3_mem0 = S.Task('c_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem0 >= 30
	c_t3_t3_t3_mem0 += MAS_MEM[4]

	c_t3_t3_t3_mem1 = S.Task('c_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem1 >= 30
	c_t3_t3_t3_mem1 += MAS_MEM[1]

	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	S += c_t4010 >= 30
	c_t4010 += MAS[3]

	c_t4_t3_t0_in = S.Task('c_t4_t3_t0_in', length=1, delay_cost=1)
	S += c_t4_t3_t0_in >= 30
	c_t4_t3_t0_in += MM_in[0]

	c_t4_t3_t0_mem0 = S.Task('c_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem0 >= 30
	c_t4_t3_t0_mem0 += MAS_MEM[6]

	c_t4_t3_t0_mem1 = S.Task('c_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem1 >= 30
	c_t4_t3_t0_mem1 += MAS_MEM[7]

	c_s2010_mem0 = S.Task('c_s2010_mem0', length=1, delay_cost=1)
	S += c_s2010_mem0 >= 31
	c_s2010_mem0 += MAS_MEM[0]

	c_s2010_mem1 = S.Task('c_s2010_mem1', length=1, delay_cost=1)
	S += c_s2010_mem1 >= 31
	c_s2010_mem1 += MAS_MEM[5]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 31
	c_t1_t31_mem0 += MM_MEM[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 31
	c_t1_t31_mem1 += MAS_MEM[1]

	c_t210 = S.Task('c_t210', length=1, delay_cost=1)
	S += c_t210 >= 31
	c_t210 += MAS[0]

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=1, delay_cost=1)
	S += c_t2_t3_t2 >= 31
	c_t2_t3_t2 += MAS[1]

	c_t3_t3_t3 = S.Task('c_t3_t3_t3', length=1, delay_cost=1)
	S += c_t3_t3_t3 >= 31
	c_t3_t3_t3 += MAS[2]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 31
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 31
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 31
	c_t4_t10_mem0 += MAS_MEM[6]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 31
	c_t4_t10_mem1 += MAS_MEM[7]

	c_t4_t3_t0 = S.Task('c_t4_t3_t0', length=7, delay_cost=1)
	S += c_t4_t3_t0 >= 31
	c_t4_t3_t0 += MM[0]

	c_s2010 = S.Task('c_s2010', length=1, delay_cost=1)
	S += c_s2010 >= 32
	c_s2010 += MAS[3]

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	S += c_t1_t31 >= 32
	c_t1_t31 += MAS[2]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 32
	c_t1_t40_mem0 += MAS_MEM[0]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 32
	c_t1_t40_mem1 += MAS_MEM[5]

	c_t2_t3_t4_in = S.Task('c_t2_t3_t4_in', length=1, delay_cost=1)
	S += c_t2_t3_t4_in >= 32
	c_t2_t3_t4_in += MM_in[0]

	c_t2_t3_t4_mem0 = S.Task('c_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem0 >= 32
	c_t2_t3_t4_mem0 += MAS_MEM[2]

	c_t2_t3_t4_mem1 = S.Task('c_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem1 >= 32
	c_t2_t3_t4_mem1 += MAS_MEM[7]

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	S += c_t4011 >= 32
	c_t4011 += MAS[0]

	c_t4_t10 = S.Task('c_t4_t10', length=1, delay_cost=1)
	S += c_t4_t10 >= 32
	c_t4_t10 += MAS[1]

	c_t4_t3_t3_mem0 = S.Task('c_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem0 >= 32
	c_t4_t3_t3_mem0 += MAS_MEM[6]

	c_t4_t3_t3_mem1 = S.Task('c_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem1 >= 32
	c_t4_t3_t3_mem1 += MAS_MEM[1]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 32
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 32
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 33
	c_t111_mem0 += MAS_MEM[4]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 33
	c_t111_mem1 += MAS_MEM[5]

	c_t1_t40 = S.Task('c_t1_t40', length=1, delay_cost=1)
	S += c_t1_t40 >= 33
	c_t1_t40 += MAS[1]

	c_t2_t3_t4 = S.Task('c_t2_t3_t4', length=7, delay_cost=1)
	S += c_t2_t3_t4 >= 33
	c_t2_t3_t4 += MM[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 33
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 33
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4_a1_1_mem0 = S.Task('c_t4_a1_1_mem0', length=1, delay_cost=1)
	S += c_t4_a1_1_mem0 >= 33
	c_t4_a1_1_mem0 += MAS_MEM[0]

	c_t4_a1_1_mem1 = S.Task('c_t4_a1_1_mem1', length=1, delay_cost=1)
	S += c_t4_a1_1_mem1 >= 33
	c_t4_a1_1_mem1 += MAS_MEM[7]

	c_t4_t3_t3 = S.Task('c_t4_t3_t3', length=1, delay_cost=1)
	S += c_t4_t3_t3 >= 33
	c_t4_t3_t3 += MAS[2]

	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	S += c_t5011 >= 33
	c_t5011 += MAS[0]

	c_t5_t3_t1_in = S.Task('c_t5_t3_t1_in', length=1, delay_cost=1)
	S += c_t5_t3_t1_in >= 33
	c_t5_t3_t1_in += MM_in[0]

	c_t5_t3_t1_mem0 = S.Task('c_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem0 >= 33
	c_t5_t3_t1_mem0 += MAS_MEM[6]

	c_t5_t3_t1_mem1 = S.Task('c_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem1 >= 33
	c_t5_t3_t1_mem1 += MAS_MEM[1]

	c_t111 = S.Task('c_t111', length=1, delay_cost=1)
	S += c_t111 >= 34
	c_t111 += MAS[1]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 34
	c_t3_t00_mem0 += MAS_MEM[6]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 34
	c_t3_t00_mem1 += MAS_MEM[5]

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	S += c_t4001 >= 34
	c_t4001 += MAS[0]

	c_t4_a1_1 = S.Task('c_t4_a1_1', length=1, delay_cost=1)
	S += c_t4_a1_1 >= 34
	c_t4_a1_1 += MAS[2]

	c_t4_t3_t1_in = S.Task('c_t4_t3_t1_in', length=1, delay_cost=1)
	S += c_t4_t3_t1_in >= 34
	c_t4_t3_t1_in += MM_in[0]

	c_t4_t3_t1_mem0 = S.Task('c_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem0 >= 34
	c_t4_t3_t1_mem0 += MAS_MEM[0]

	c_t4_t3_t1_mem1 = S.Task('c_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem1 >= 34
	c_t4_t3_t1_mem1 += MAS_MEM[1]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 34
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 34
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5_t3_t1 = S.Task('c_t5_t3_t1', length=7, delay_cost=1)
	S += c_t5_t3_t1 >= 34
	c_t5_t3_t1 += MM[0]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 35
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 35
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3_t00 = S.Task('c_t3_t00', length=1, delay_cost=1)
	S += c_t3_t00 >= 35
	c_t3_t00 += MAS[0]

	c_t4_a1_0_mem0 = S.Task('c_t4_a1_0_mem0', length=1, delay_cost=1)
	S += c_t4_a1_0_mem0 >= 35
	c_t4_a1_0_mem0 += MAS_MEM[6]

	c_t4_a1_0_mem1 = S.Task('c_t4_a1_0_mem1', length=1, delay_cost=1)
	S += c_t4_a1_0_mem1 >= 35
	c_t4_a1_0_mem1 += MAS_MEM[1]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 35
	c_t4_t01_mem0 += MAS_MEM[0]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 35
	c_t4_t01_mem1 += MAS_MEM[5]

	c_t4_t3_t1 = S.Task('c_t4_t3_t1', length=7, delay_cost=1)
	S += c_t4_t3_t1 >= 35
	c_t4_t3_t1 += MM[0]

	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	S += c_t5010 >= 35
	c_t5010 += MAS[1]

	c_t5_t3_t0_in = S.Task('c_t5_t3_t0_in', length=1, delay_cost=1)
	S += c_t5_t3_t0_in >= 35
	c_t5_t3_t0_in += MM_in[0]

	c_t5_t3_t0_mem0 = S.Task('c_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem0 >= 35
	c_t5_t3_t0_mem0 += MAS_MEM[2]

	c_t5_t3_t0_mem1 = S.Task('c_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem1 >= 35
	c_t5_t3_t0_mem1 += MAS_MEM[3]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 36
	c_t1_t00_mem0 += MAIN_MEM_r[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 36
	c_t1_t00_mem1 += MAS_MEM[5]

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	S += c_t3001 >= 36
	c_t3001 += MAS[3]

	c_t3_t3_t2_mem0 = S.Task('c_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem0 >= 36
	c_t3_t3_t2_mem0 += MAS_MEM[6]

	c_t3_t3_t2_mem1 = S.Task('c_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem1 >= 36
	c_t3_t3_t2_mem1 += MAS_MEM[7]

	c_t4_a1_0 = S.Task('c_t4_a1_0', length=1, delay_cost=1)
	S += c_t4_a1_0 >= 36
	c_t4_a1_0 += MAS[1]

	c_t4_t01 = S.Task('c_t4_t01', length=1, delay_cost=1)
	S += c_t4_t01 >= 36
	c_t4_t01 += MAS[0]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 36
	c_t4_t11_mem0 += MAS_MEM[0]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 36
	c_t4_t11_mem1 += MAS_MEM[1]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 36
	c_t5_t10_mem0 += MAS_MEM[2]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 36
	c_t5_t10_mem1 += MAS_MEM[3]

	c_t5_t3_t0 = S.Task('c_t5_t3_t0', length=7, delay_cost=1)
	S += c_t5_t3_t0 >= 36
	c_t5_t3_t0 += MM[0]

	c_t1_t00 = S.Task('c_t1_t00', length=1, delay_cost=1)
	S += c_t1_t00 >= 37
	c_t1_t00 += MAS[2]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 37
	c_t2_t01_mem0 += MAIN_MEM_r[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 37
	c_t2_t01_mem1 += MAS_MEM[7]

	c_t3_t3_t1_in = S.Task('c_t3_t3_t1_in', length=1, delay_cost=1)
	S += c_t3_t3_t1_in >= 37
	c_t3_t3_t1_in += MM_in[0]

	c_t3_t3_t1_mem0 = S.Task('c_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem0 >= 37
	c_t3_t3_t1_mem0 += MAS_MEM[6]

	c_t3_t3_t1_mem1 = S.Task('c_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem1 >= 37
	c_t3_t3_t1_mem1 += MAS_MEM[1]

	c_t3_t3_t2 = S.Task('c_t3_t3_t2', length=1, delay_cost=1)
	S += c_t3_t3_t2 >= 37
	c_t3_t3_t2 += MAS[0]

	c_t4_t11 = S.Task('c_t4_t11', length=1, delay_cost=1)
	S += c_t4_t11 >= 37
	c_t4_t11 += MAS[1]

	c_t5_a1_1_mem0 = S.Task('c_t5_a1_1_mem0', length=1, delay_cost=1)
	S += c_t5_a1_1_mem0 >= 37
	c_t5_a1_1_mem0 += MAS_MEM[0]

	c_t5_a1_1_mem1 = S.Task('c_t5_a1_1_mem1', length=1, delay_cost=1)
	S += c_t5_a1_1_mem1 >= 37
	c_t5_a1_1_mem1 += MAS_MEM[3]

	c_t5_t10 = S.Task('c_t5_t10', length=1, delay_cost=1)
	S += c_t5_t10 >= 37
	c_t5_t10 += MAS[3]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 38
	c_t0_t01_mem0 += MAIN_MEM_r[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 38
	c_t0_t01_mem1 += MAS_MEM[7]

	c_t2_t01 = S.Task('c_t2_t01', length=1, delay_cost=1)
	S += c_t2_t01 >= 38
	c_t2_t01 += MAS[0]

	c_t3_t3_t1 = S.Task('c_t3_t3_t1', length=7, delay_cost=1)
	S += c_t3_t3_t1 >= 38
	c_t3_t3_t1 += MM[0]

	c_t3_t3_t4_in = S.Task('c_t3_t3_t4_in', length=1, delay_cost=1)
	S += c_t3_t3_t4_in >= 38
	c_t3_t3_t4_in += MM_in[0]

	c_t3_t3_t4_mem0 = S.Task('c_t3_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t4_mem0 >= 38
	c_t3_t3_t4_mem0 += MAS_MEM[0]

	c_t3_t3_t4_mem1 = S.Task('c_t3_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t4_mem1 >= 38
	c_t3_t3_t4_mem1 += MAS_MEM[5]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 38
	c_t4_t00_mem0 += MAS_MEM[6]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 38
	c_t4_t00_mem1 += MAS_MEM[3]

	c_t5_a1_0_mem0 = S.Task('c_t5_a1_0_mem0', length=1, delay_cost=1)
	S += c_t5_a1_0_mem0 >= 38
	c_t5_a1_0_mem0 += MAS_MEM[2]

	c_t5_a1_0_mem1 = S.Task('c_t5_a1_0_mem1', length=1, delay_cost=1)
	S += c_t5_a1_0_mem1 >= 38
	c_t5_a1_0_mem1 += MAS_MEM[1]

	c_t5_a1_1 = S.Task('c_t5_a1_1', length=1, delay_cost=1)
	S += c_t5_a1_1 >= 38
	c_t5_a1_1 += MAS[3]

	c_t0_t01 = S.Task('c_t0_t01', length=1, delay_cost=1)
	S += c_t0_t01 >= 39
	c_t0_t01 += MAS[2]

	c_t1_t2_t0_in = S.Task('c_t1_t2_t0_in', length=1, delay_cost=1)
	S += c_t1_t2_t0_in >= 39
	c_t1_t2_t0_in += MM_in[0]

	c_t1_t2_t0_mem0 = S.Task('c_t1_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t0_mem0 >= 39
	c_t1_t2_t0_mem0 += MAS_MEM[4]

	c_t1_t2_t0_mem1 = S.Task('c_t1_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t0_mem1 >= 39
	c_t1_t2_t0_mem1 += MAS_MEM[5]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 39
	c_t2_t00_mem0 += MAIN_MEM_r[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 39
	c_t2_t00_mem1 += MAS_MEM[7]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 39
	c_t2_t31_mem0 += MM_MEM[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 39
	c_t2_t31_mem1 += MAS_MEM[3]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 39
	c_t3_t11_mem0 += MAS_MEM[6]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 39
	c_t3_t11_mem1 += MAS_MEM[1]

	c_t3_t3_t4 = S.Task('c_t3_t3_t4', length=7, delay_cost=1)
	S += c_t3_t3_t4 >= 39
	c_t3_t3_t4 += MM[0]

	c_t4_t00 = S.Task('c_t4_t00', length=1, delay_cost=1)
	S += c_t4_t00 >= 39
	c_t4_t00 += MAS[1]

	c_t5_a1_0 = S.Task('c_t5_a1_0', length=1, delay_cost=1)
	S += c_t5_a1_0 >= 39
	c_t5_a1_0 += MAS[0]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 40
	c_t1_t01_mem0 += MAIN_MEM_r[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 40
	c_t1_t01_mem1 += MAS_MEM[3]

	c_t1_t2_t0 = S.Task('c_t1_t2_t0', length=7, delay_cost=1)
	S += c_t1_t2_t0 >= 40
	c_t1_t2_t0 += MM[0]

	c_t2_t00 = S.Task('c_t2_t00', length=1, delay_cost=1)
	S += c_t2_t00 >= 40
	c_t2_t00 += MAS[1]

	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	S += c_t2_t31 >= 40
	c_t2_t31 += MAS[2]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 40
	c_t2_t40_mem0 += MAS_MEM[2]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 40
	c_t2_t40_mem1 += MAS_MEM[5]

	c_t3_t11 = S.Task('c_t3_t11', length=1, delay_cost=1)
	S += c_t3_t11 >= 40
	c_t3_t11 += MAS[0]

	c_t4_t3_t2_mem0 = S.Task('c_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem0 >= 40
	c_t4_t3_t2_mem0 += MAS_MEM[6]

	c_t4_t3_t2_mem1 = S.Task('c_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem1 >= 40
	c_t4_t3_t2_mem1 += MAS_MEM[1]

	c_t1_t01 = S.Task('c_t1_t01', length=1, delay_cost=1)
	S += c_t1_t01 >= 41
	c_t1_t01 += MAS[0]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 41
	c_t211_mem0 += MAS_MEM[4]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 41
	c_t211_mem1 += MAS_MEM[5]

	c_t2_t40 = S.Task('c_t2_t40', length=1, delay_cost=1)
	S += c_t2_t40 >= 41
	c_t2_t40 += MAS[2]

	c_t3_t2_t0_in = S.Task('c_t3_t2_t0_in', length=1, delay_cost=1)
	S += c_t3_t2_t0_in >= 41
	c_t3_t2_t0_in += MM_in[0]

	c_t3_t2_t0_mem0 = S.Task('c_t3_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t0_mem0 >= 41
	c_t3_t2_t0_mem0 += MAS_MEM[0]

	c_t3_t2_t0_mem1 = S.Task('c_t3_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t0_mem1 >= 41
	c_t3_t2_t0_mem1 += MAS_MEM[3]

	c_t4_t3_t2 = S.Task('c_t4_t3_t2', length=1, delay_cost=1)
	S += c_t4_t3_t2 >= 41
	c_t4_t3_t2 += MAS[1]

	c_t4_t3_t5_mem0 = S.Task('c_t4_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t5_mem0 >= 41
	c_t4_t3_t5_mem0 += MM_MEM[0]

	c_t4_t3_t5_mem1 = S.Task('c_t4_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t5_mem1 >= 41
	c_t4_t3_t5_mem1 += MM_MEM[1]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 41
	c_t5_t01_mem0 += MAS_MEM[6]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 41
	c_t5_t01_mem1 += MAS_MEM[7]

	c_t5_t3_t3_mem0 = S.Task('c_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem0 >= 41
	c_t5_t3_t3_mem0 += MAS_MEM[2]

	c_t5_t3_t3_mem1 = S.Task('c_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem1 >= 41
	c_t5_t3_t3_mem1 += MAS_MEM[1]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 42
	c_t0_t00_mem0 += MAIN_MEM_r[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 42
	c_t0_t00_mem1 += MAS_MEM[1]

	c_t211 = S.Task('c_t211', length=1, delay_cost=1)
	S += c_t211 >= 42
	c_t211 += MAS[1]

	c_t3_t2_t0 = S.Task('c_t3_t2_t0', length=7, delay_cost=1)
	S += c_t3_t2_t0 >= 42
	c_t3_t2_t0 += MM[0]

	c_t4_t2_t3_mem0 = S.Task('c_t4_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t3_mem0 >= 42
	c_t4_t2_t3_mem0 += MAS_MEM[2]

	c_t4_t2_t3_mem1 = S.Task('c_t4_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t3_mem1 >= 42
	c_t4_t2_t3_mem1 += MAS_MEM[3]

	c_t4_t3_t5 = S.Task('c_t4_t3_t5', length=1, delay_cost=1)
	S += c_t4_t3_t5 >= 42
	c_t4_t3_t5 += MAS[0]

	c_t5_t01 = S.Task('c_t5_t01', length=1, delay_cost=1)
	S += c_t5_t01 >= 42
	c_t5_t01 += MAS[2]

	c_t5_t3_t3 = S.Task('c_t5_t3_t3', length=1, delay_cost=1)
	S += c_t5_t3_t3 >= 42
	c_t5_t3_t3 += MAS[3]

	c_t5_t3_t4_in = S.Task('c_t5_t3_t4_in', length=1, delay_cost=1)
	S += c_t5_t3_t4_in >= 42
	c_t5_t3_t4_in += MM_in[0]

	c_t5_t3_t4_mem0 = S.Task('c_t5_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t4_mem0 >= 42
	c_t5_t3_t4_mem0 += MAS_MEM[0]

	c_t5_t3_t4_mem1 = S.Task('c_t5_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t4_mem1 >= 42
	c_t5_t3_t4_mem1 += MAS_MEM[7]

	c_t5_t3_t5_mem0 = S.Task('c_t5_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t5_mem0 >= 42
	c_t5_t3_t5_mem0 += MM_MEM[0]

	c_t5_t3_t5_mem1 = S.Task('c_t5_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t5_mem1 >= 42
	c_t5_t3_t5_mem1 += MM_MEM[1]

	c_t0_t00 = S.Task('c_t0_t00', length=1, delay_cost=1)
	S += c_t0_t00 >= 43
	c_t0_t00 += MAS[0]

	c_t0_t2_t2_mem0 = S.Task('c_t0_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t2_mem0 >= 43
	c_t0_t2_t2_mem0 += MAS_MEM[0]

	c_t0_t2_t2_mem1 = S.Task('c_t0_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t2_mem1 >= 43
	c_t0_t2_t2_mem1 += MAS_MEM[5]

	c_t2_t2_t0_in = S.Task('c_t2_t2_t0_in', length=1, delay_cost=1)
	S += c_t2_t2_t0_in >= 43
	c_t2_t2_t0_in += MM_in[0]

	c_t2_t2_t0_mem0 = S.Task('c_t2_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t0_mem0 >= 43
	c_t2_t2_t0_mem0 += MAS_MEM[2]

	c_t2_t2_t0_mem1 = S.Task('c_t2_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t0_mem1 >= 43
	c_t2_t2_t0_mem1 += MAS_MEM[3]

	c_t4_t2_t3 = S.Task('c_t4_t2_t3', length=1, delay_cost=1)
	S += c_t4_t2_t3 >= 43
	c_t4_t2_t3 += MAS[3]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 43
	c_t5_t11_mem0 += MAS_MEM[6]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 43
	c_t5_t11_mem1 += MAS_MEM[1]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 43
	c_t5_t30_mem0 += MM_MEM[0]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 43
	c_t5_t30_mem1 += MM_MEM[1]

	c_t5_t3_t4 = S.Task('c_t5_t3_t4', length=7, delay_cost=1)
	S += c_t5_t3_t4 >= 43
	c_t5_t3_t4 += MM[0]

	c_t5_t3_t5 = S.Task('c_t5_t3_t5', length=1, delay_cost=1)
	S += c_t5_t3_t5 >= 43
	c_t5_t3_t5 += MAS[1]

	c_t0_t2_t2 = S.Task('c_t0_t2_t2', length=1, delay_cost=1)
	S += c_t0_t2_t2 >= 44
	c_t0_t2_t2 += MAS[0]

	c_t1_t2_t2_mem0 = S.Task('c_t1_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t2_mem0 >= 44
	c_t1_t2_t2_mem0 += MAS_MEM[4]

	c_t1_t2_t2_mem1 = S.Task('c_t1_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t2_mem1 >= 44
	c_t1_t2_t2_mem1 += MAS_MEM[1]

	c_t2_t2_t0 = S.Task('c_t2_t2_t0', length=7, delay_cost=1)
	S += c_t2_t2_t0 >= 44
	c_t2_t2_t0 += MM[0]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 44
	c_t3_t30_mem0 += MM_MEM[0]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 44
	c_t3_t30_mem1 += MM_MEM[1]

	c_t4_t3_t4_in = S.Task('c_t4_t3_t4_in', length=1, delay_cost=1)
	S += c_t4_t3_t4_in >= 44
	c_t4_t3_t4_in += MM_in[0]

	c_t4_t3_t4_mem0 = S.Task('c_t4_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t4_mem0 >= 44
	c_t4_t3_t4_mem0 += MAS_MEM[2]

	c_t4_t3_t4_mem1 = S.Task('c_t4_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t4_mem1 >= 44
	c_t4_t3_t4_mem1 += MAS_MEM[5]

	c_t5_t11 = S.Task('c_t5_t11', length=1, delay_cost=1)
	S += c_t5_t11 >= 44
	c_t5_t11 += MAS[1]

	c_t5_t2_t3_mem0 = S.Task('c_t5_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t3_mem0 >= 44
	c_t5_t2_t3_mem0 += MAS_MEM[6]

	c_t5_t2_t3_mem1 = S.Task('c_t5_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t3_mem1 >= 44
	c_t5_t2_t3_mem1 += MAS_MEM[3]

	c_t5_t30 = S.Task('c_t5_t30', length=1, delay_cost=1)
	S += c_t5_t30 >= 44
	c_t5_t30 += MAS[3]

	c_t1_t2_t1_in = S.Task('c_t1_t2_t1_in', length=1, delay_cost=1)
	S += c_t1_t2_t1_in >= 45
	c_t1_t2_t1_in += MM_in[0]

	c_t1_t2_t1_mem0 = S.Task('c_t1_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t1_mem0 >= 45
	c_t1_t2_t1_mem0 += MAS_MEM[0]

	c_t1_t2_t1_mem1 = S.Task('c_t1_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t1_mem1 >= 45
	c_t1_t2_t1_mem1 += MAS_MEM[1]

	c_t1_t2_t2 = S.Task('c_t1_t2_t2', length=1, delay_cost=1)
	S += c_t1_t2_t2 >= 45
	c_t1_t2_t2 += MAS[1]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 45
	c_t2_t41_mem0 += MAS_MEM[4]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 45
	c_t2_t41_mem1 += MAS_MEM[3]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 45
	c_t2_t50_mem0 += MAS_MEM[2]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 45
	c_t2_t50_mem1 += MAS_MEM[5]

	c_t3_t30 = S.Task('c_t3_t30', length=1, delay_cost=1)
	S += c_t3_t30 >= 45
	c_t3_t30 += MAS[0]

	c_t3_t3_t5_mem0 = S.Task('c_t3_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t5_mem0 >= 45
	c_t3_t3_t5_mem0 += MM_MEM[0]

	c_t3_t3_t5_mem1 = S.Task('c_t3_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t5_mem1 >= 45
	c_t3_t3_t5_mem1 += MM_MEM[1]

	c_t4_t3_t4 = S.Task('c_t4_t3_t4', length=7, delay_cost=1)
	S += c_t4_t3_t4 >= 45
	c_t4_t3_t4 += MM[0]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	S += c_t510_mem0 >= 45
	c_t510_mem0 += MAS_MEM[6]

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	S += c_t510_mem1 >= 45
	c_t510_mem1 += MAS_MEM[7]

	c_t5_t2_t3 = S.Task('c_t5_t2_t3', length=1, delay_cost=1)
	S += c_t5_t2_t3 >= 45
	c_t5_t2_t3 += MAS[3]

	c_s1011_mem0 = S.Task('c_s1011_mem0', length=1, delay_cost=1)
	S += c_s1011_mem0 >= 46
	c_s1011_mem0 += MAS_MEM[2]

	c_s1011_mem1 = S.Task('c_s1011_mem1', length=1, delay_cost=1)
	S += c_s1011_mem1 >= 46
	c_s1011_mem1 += MAS_MEM[3]

	c_t0_t2_t0_in = S.Task('c_t0_t2_t0_in', length=1, delay_cost=1)
	S += c_t0_t2_t0_in >= 46
	c_t0_t2_t0_in += MM_in[0]

	c_t0_t2_t0_mem0 = S.Task('c_t0_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t0_mem0 >= 46
	c_t0_t2_t0_mem0 += MAS_MEM[0]

	c_t0_t2_t0_mem1 = S.Task('c_t0_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t0_mem1 >= 46
	c_t0_t2_t0_mem1 += MAS_MEM[1]

	c_t1_t2_t1 = S.Task('c_t1_t2_t1', length=7, delay_cost=1)
	S += c_t1_t2_t1 >= 46
	c_t1_t2_t1 += MM[0]

	c_t2_t41 = S.Task('c_t2_t41', length=1, delay_cost=1)
	S += c_t2_t41 >= 46
	c_t2_t41 += MAS[3]

	c_t2_t50 = S.Task('c_t2_t50', length=1, delay_cost=1)
	S += c_t2_t50 >= 46
	c_t2_t50 += MAS[2]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	S += c_t2_t51_mem0 >= 46
	c_t2_t51_mem0 += MAS_MEM[4]

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	S += c_t2_t51_mem1 >= 46
	c_t2_t51_mem1 += MAS_MEM[7]

	c_t3_t3_t5 = S.Task('c_t3_t3_t5', length=1, delay_cost=1)
	S += c_t3_t3_t5 >= 46
	c_t3_t3_t5 += MAS[1]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 46
	c_t4_t30_mem0 += MM_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 46
	c_t4_t30_mem1 += MM_MEM[1]

	c_t510 = S.Task('c_t510', length=1, delay_cost=1)
	S += c_t510 >= 46
	c_t510 += MAS[0]

	c_s1011 = S.Task('c_s1011', length=1, delay_cost=1)
	S += c_s1011 >= 47
	c_s1011 += MAS[0]

	c_t0_t2_t0 = S.Task('c_t0_t2_t0', length=7, delay_cost=1)
	S += c_t0_t2_t0 >= 47
	c_t0_t2_t0 += MM[0]

	c_t2_t2_t1_in = S.Task('c_t2_t2_t1_in', length=1, delay_cost=1)
	S += c_t2_t2_t1_in >= 47
	c_t2_t2_t1_in += MM_in[0]

	c_t2_t2_t1_mem0 = S.Task('c_t2_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t1_mem0 >= 47
	c_t2_t2_t1_mem0 += MAS_MEM[0]

	c_t2_t2_t1_mem1 = S.Task('c_t2_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t1_mem1 >= 47
	c_t2_t2_t1_mem1 += MAS_MEM[1]

	c_t2_t51 = S.Task('c_t2_t51', length=1, delay_cost=1)
	S += c_t2_t51 >= 47
	c_t2_t51 += MAS[3]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 47
	c_t3_t31_mem0 += MM_MEM[0]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 47
	c_t3_t31_mem1 += MAS_MEM[3]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	S += c_t410_mem0 >= 47
	c_t410_mem0 += MAS_MEM[4]

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	S += c_t410_mem1 >= 47
	c_t410_mem1 += MAS_MEM[5]

	c_t4_t30 = S.Task('c_t4_t30', length=1, delay_cost=1)
	S += c_t4_t30 >= 47
	c_t4_t30 += MAS[2]

	c_s0011_mem0 = S.Task('c_s0011_mem0', length=1, delay_cost=1)
	S += c_s0011_mem0 >= 48
	c_s0011_mem0 += MAS_MEM[0]

	c_s0011_mem1 = S.Task('c_s0011_mem1', length=1, delay_cost=1)
	S += c_s0011_mem1 >= 48
	c_s0011_mem1 += MAS_MEM[3]

	c_t0_t2_t1_in = S.Task('c_t0_t2_t1_in', length=1, delay_cost=1)
	S += c_t0_t2_t1_in >= 48
	c_t0_t2_t1_in += MM_in[0]

	c_t0_t2_t1_mem0 = S.Task('c_t0_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t1_mem0 >= 48
	c_t0_t2_t1_mem0 += MAS_MEM[4]

	c_t0_t2_t1_mem1 = S.Task('c_t0_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t1_mem1 >= 48
	c_t0_t2_t1_mem1 += MAS_MEM[1]

	c_t2_t2_t1 = S.Task('c_t2_t2_t1', length=7, delay_cost=1)
	S += c_t2_t2_t1 >= 48
	c_t2_t2_t1 += MM[0]

	c_t3_t31 = S.Task('c_t3_t31', length=1, delay_cost=1)
	S += c_t3_t31 >= 48
	c_t3_t31 += MAS[0]

	c_t410 = S.Task('c_t410', length=1, delay_cost=1)
	S += c_t410 >= 48
	c_t410 += MAS[3]

	c_s0011 = S.Task('c_s0011', length=1, delay_cost=1)
	S += c_s0011 >= 49
	c_s0011 += MAS[2]

	c_t0_t2_t1 = S.Task('c_t0_t2_t1', length=7, delay_cost=1)
	S += c_t0_t2_t1 >= 49
	c_t0_t2_t1 += MM[0]

	c_t3_t2_t3_mem0 = S.Task('c_t3_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t3_mem0 >= 49
	c_t3_t2_t3_mem0 += MAS_MEM[2]

	c_t3_t2_t3_mem1 = S.Task('c_t3_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t3_mem1 >= 49
	c_t3_t2_t3_mem1 += MAS_MEM[1]

	c_t4_t2_t1_in = S.Task('c_t4_t2_t1_in', length=1, delay_cost=1)
	S += c_t4_t2_t1_in >= 49
	c_t4_t2_t1_in += MM_in[0]

	c_t4_t2_t1_mem0 = S.Task('c_t4_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t1_mem0 >= 49
	c_t4_t2_t1_mem0 += MAS_MEM[0]

	c_t4_t2_t1_mem1 = S.Task('c_t4_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t1_mem1 >= 49
	c_t4_t2_t1_mem1 += MAS_MEM[3]

	c_s210_mem0 = S.Task('c_s210_mem0', length=1, delay_cost=1)
	S += c_s210_mem0 >= 50
	c_s210_mem0 += MAS_MEM[0]

	c_s210_mem1 = S.Task('c_s210_mem1', length=1, delay_cost=1)
	S += c_s210_mem1 >= 50
	c_s210_mem1 += MAS_MEM[7]

	c_t3_t2_t3 = S.Task('c_t3_t2_t3', length=1, delay_cost=1)
	S += c_t3_t2_t3 >= 50
	c_t3_t2_t3 += MAS[2]

	c_t4_t2_t1 = S.Task('c_t4_t2_t1', length=7, delay_cost=1)
	S += c_t4_t2_t1 >= 50
	c_t4_t2_t1 += MM[0]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 50
	c_t5_t00_mem0 += MAS_MEM[2]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 50
	c_t5_t00_mem1 += MAS_MEM[1]

	c_t5_t2_t1_in = S.Task('c_t5_t2_t1_in', length=1, delay_cost=1)
	S += c_t5_t2_t1_in >= 50
	c_t5_t2_t1_in += MM_in[0]

	c_t5_t2_t1_mem0 = S.Task('c_t5_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t1_mem0 >= 50
	c_t5_t2_t1_mem0 += MAS_MEM[4]

	c_t5_t2_t1_mem1 = S.Task('c_t5_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t1_mem1 >= 50
	c_t5_t2_t1_mem1 += MAS_MEM[3]

	c_s210 = S.Task('c_s210', length=1, delay_cost=1)
	S += c_s210 >= 51
	c_s210 += MAS[1]

	c_t2_t2_t2_mem0 = S.Task('c_t2_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t2_mem0 >= 51
	c_t2_t2_t2_mem0 += MAS_MEM[2]

	c_t2_t2_t2_mem1 = S.Task('c_t2_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t2_mem1 >= 51
	c_t2_t2_t2_mem1 += MAS_MEM[1]

	c_t5_t00 = S.Task('c_t5_t00', length=1, delay_cost=1)
	S += c_t5_t00 >= 51
	c_t5_t00 += MAS[0]

	c_t5_t2_t0_in = S.Task('c_t5_t2_t0_in', length=1, delay_cost=1)
	S += c_t5_t2_t0_in >= 51
	c_t5_t2_t0_in += MM_in[0]

	c_t5_t2_t0_mem0 = S.Task('c_t5_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t0_mem0 >= 51
	c_t5_t2_t0_mem0 += MAS_MEM[0]

	c_t5_t2_t0_mem1 = S.Task('c_t5_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t0_mem1 >= 51
	c_t5_t2_t0_mem1 += MAS_MEM[7]

	c_t5_t2_t1 = S.Task('c_t5_t2_t1', length=7, delay_cost=1)
	S += c_t5_t2_t1 >= 51
	c_t5_t2_t1 += MM[0]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 51
	c_t5_t31_mem0 += MM_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 51
	c_t5_t31_mem1 += MAS_MEM[3]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 52
	c_t1_t20_mem0 += MM_MEM[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 52
	c_t1_t20_mem1 += MM_MEM[1]

	c_t1_t2_t4_in = S.Task('c_t1_t2_t4_in', length=1, delay_cost=1)
	S += c_t1_t2_t4_in >= 52
	c_t1_t2_t4_in += MM_in[0]

	c_t1_t2_t4_mem0 = S.Task('c_t1_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t4_mem0 >= 52
	c_t1_t2_t4_mem0 += MAS_MEM[2]

	c_t1_t2_t4_mem1 = S.Task('c_t1_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t4_mem1 >= 52
	c_t1_t2_t4_mem1 += MAS_MEM[3]

	c_t2_t2_t2 = S.Task('c_t2_t2_t2', length=1, delay_cost=1)
	S += c_t2_t2_t2 >= 52
	c_t2_t2_t2 += MAS[0]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 52
	c_t3_t01_mem0 += MAS_MEM[6]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 52
	c_t3_t01_mem1 += MAS_MEM[1]

	c_t5_t2_t0 = S.Task('c_t5_t2_t0', length=7, delay_cost=1)
	S += c_t5_t2_t0 >= 52
	c_t5_t2_t0 += MM[0]

	c_t5_t2_t2_mem0 = S.Task('c_t5_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t2_mem0 >= 52
	c_t5_t2_t2_mem0 += MAS_MEM[0]

	c_t5_t2_t2_mem1 = S.Task('c_t5_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t2_mem1 >= 52
	c_t5_t2_t2_mem1 += MAS_MEM[5]

	c_t5_t31 = S.Task('c_t5_t31', length=1, delay_cost=1)
	S += c_t5_t31 >= 52
	c_t5_t31 += MAS[1]

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	S += c_t1_t20 >= 53
	c_t1_t20 += MAS[1]

	c_t1_t2_t4 = S.Task('c_t1_t2_t4', length=7, delay_cost=1)
	S += c_t1_t2_t4 >= 53
	c_t1_t2_t4 += MM[0]

	c_t1_t2_t5_mem0 = S.Task('c_t1_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t5_mem0 >= 53
	c_t1_t2_t5_mem0 += MM_MEM[0]

	c_t1_t2_t5_mem1 = S.Task('c_t1_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t5_mem1 >= 53
	c_t1_t2_t5_mem1 += MM_MEM[1]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 53
	c_t310_mem0 += MAS_MEM[0]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 53
	c_t310_mem1 += MAS_MEM[1]

	c_t3_t01 = S.Task('c_t3_t01', length=1, delay_cost=1)
	S += c_t3_t01 >= 53
	c_t3_t01 += MAS[0]

	c_t4_t2_t0_in = S.Task('c_t4_t2_t0_in', length=1, delay_cost=1)
	S += c_t4_t2_t0_in >= 53
	c_t4_t2_t0_in += MM_in[0]

	c_t4_t2_t0_mem0 = S.Task('c_t4_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t0_mem0 >= 53
	c_t4_t2_t0_mem0 += MAS_MEM[2]

	c_t4_t2_t0_mem1 = S.Task('c_t4_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t0_mem1 >= 53
	c_t4_t2_t0_mem1 += MAS_MEM[3]

	c_t5_t2_t2 = S.Task('c_t5_t2_t2', length=1, delay_cost=1)
	S += c_t5_t2_t2 >= 53
	c_t5_t2_t2 += MAS[2]

	c_t1_t2_t5 = S.Task('c_t1_t2_t5', length=1, delay_cost=1)
	S += c_t1_t2_t5 >= 54
	c_t1_t2_t5 += MAS[1]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 54
	c_t1_t41_mem0 += MAS_MEM[4]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 54
	c_t1_t41_mem1 += MAS_MEM[1]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 54
	c_t2_t20_mem0 += MM_MEM[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 54
	c_t2_t20_mem1 += MM_MEM[1]

	c_t2_t2_t4_in = S.Task('c_t2_t2_t4_in', length=1, delay_cost=1)
	S += c_t2_t2_t4_in >= 54
	c_t2_t2_t4_in += MM_in[0]

	c_t2_t2_t4_mem0 = S.Task('c_t2_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t4_mem0 >= 54
	c_t2_t2_t4_mem0 += MAS_MEM[0]

	c_t2_t2_t4_mem1 = S.Task('c_t2_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t4_mem1 >= 54
	c_t2_t2_t4_mem1 += MAS_MEM[7]

	c_t310 = S.Task('c_t310', length=1, delay_cost=1)
	S += c_t310 >= 54
	c_t310 += MAS[0]

	c_t4_t2_t0 = S.Task('c_t4_t2_t0', length=7, delay_cost=1)
	S += c_t4_t2_t0 >= 54
	c_t4_t2_t0 += MM[0]

	c_t511_mem0 = S.Task('c_t511_mem0', length=1, delay_cost=1)
	S += c_t511_mem0 >= 54
	c_t511_mem0 += MAS_MEM[2]

	c_t511_mem1 = S.Task('c_t511_mem1', length=1, delay_cost=1)
	S += c_t511_mem1 >= 54
	c_t511_mem1 += MAS_MEM[3]

	c_t0_t2_t4_in = S.Task('c_t0_t2_t4_in', length=1, delay_cost=1)
	S += c_t0_t2_t4_in >= 55
	c_t0_t2_t4_in += MM_in[0]

	c_t0_t2_t4_mem0 = S.Task('c_t0_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t4_mem0 >= 55
	c_t0_t2_t4_mem0 += MAS_MEM[0]

	c_t0_t2_t4_mem1 = S.Task('c_t0_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t4_mem1 >= 55
	c_t0_t2_t4_mem1 += MAS_MEM[1]

	c_t1_t41 = S.Task('c_t1_t41', length=1, delay_cost=1)
	S += c_t1_t41 >= 55
	c_t1_t41 += MAS[2]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	S += c_t1_t51_mem0 >= 55
	c_t1_t51_mem0 += MAS_MEM[4]

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	S += c_t1_t51_mem1 >= 55
	c_t1_t51_mem1 += MAS_MEM[5]

	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	S += c_t2_t20 >= 55
	c_t2_t20 += MAS[0]

	c_t2_t2_t4 = S.Task('c_t2_t2_t4', length=7, delay_cost=1)
	S += c_t2_t2_t4 >= 55
	c_t2_t2_t4 += MM[0]

	c_t2_t2_t5_mem0 = S.Task('c_t2_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t5_mem0 >= 55
	c_t2_t2_t5_mem0 += MM_MEM[0]

	c_t2_t2_t5_mem1 = S.Task('c_t2_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t5_mem1 >= 55
	c_t2_t2_t5_mem1 += MM_MEM[1]

	c_t511 = S.Task('c_t511', length=1, delay_cost=1)
	S += c_t511 >= 55
	c_t511 += MAS[1]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	S += c_t5_t40_mem0 >= 55
	c_t5_t40_mem0 += MAS_MEM[6]

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	S += c_t5_t40_mem1 >= 55
	c_t5_t40_mem1 += MAS_MEM[3]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	S += c_t5_t41_mem0 >= 55
	c_t5_t41_mem0 += MAS_MEM[2]

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	S += c_t5_t41_mem1 >= 55
	c_t5_t41_mem1 += MAS_MEM[7]

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	S += c210_mem0 >= 56
	c210_mem0 += MAS_MEM[6]

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	S += c210_mem1 >= 56
	c210_mem1 += MAS_MEM[3]

	c_t0_t2_t4 = S.Task('c_t0_t2_t4', length=7, delay_cost=1)
	S += c_t0_t2_t4 >= 56
	c_t0_t2_t4 += MM[0]

	c_t0_t2_t5_mem0 = S.Task('c_t0_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t5_mem0 >= 56
	c_t0_t2_t5_mem0 += MM_MEM[0]

	c_t0_t2_t5_mem1 = S.Task('c_t0_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t5_mem1 >= 56
	c_t0_t2_t5_mem1 += MM_MEM[1]

	c_t1_t51 = S.Task('c_t1_t51', length=1, delay_cost=1)
	S += c_t1_t51 >= 56
	c_t1_t51 += MAS[1]

	c_t2_t2_t5 = S.Task('c_t2_t2_t5', length=1, delay_cost=1)
	S += c_t2_t2_t5 >= 56
	c_t2_t2_t5 += MAS[2]

	c_t3_t2_t1_in = S.Task('c_t3_t2_t1_in', length=1, delay_cost=1)
	S += c_t3_t2_t1_in >= 56
	c_t3_t2_t1_in += MM_in[0]

	c_t3_t2_t1_mem0 = S.Task('c_t3_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t1_mem0 >= 56
	c_t3_t2_t1_mem0 += MAS_MEM[0]

	c_t3_t2_t1_mem1 = S.Task('c_t3_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t1_mem1 >= 56
	c_t3_t2_t1_mem1 += MAS_MEM[1]

	c_t5_t40 = S.Task('c_t5_t40', length=1, delay_cost=1)
	S += c_t5_t40 >= 56
	c_t5_t40 += MAS[0]

	c_t5_t41 = S.Task('c_t5_t41', length=1, delay_cost=1)
	S += c_t5_t41 >= 56
	c_t5_t41 += MAS[3]

	c_t5_t51_mem0 = S.Task('c_t5_t51_mem0', length=1, delay_cost=1)
	S += c_t5_t51_mem0 >= 56
	c_t5_t51_mem0 += MAS_MEM[2]

	c_t5_t51_mem1 = S.Task('c_t5_t51_mem1', length=1, delay_cost=1)
	S += c_t5_t51_mem1 >= 56
	c_t5_t51_mem1 += MAS_MEM[7]

	c210 = S.Task('c210', length=1, delay_cost=1)
	S += c210 >= 57
	c210 += MAS[3]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 57
	c_t0_t20_mem0 += MM_MEM[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 57
	c_t0_t20_mem1 += MM_MEM[1]

	c_t0_t2_t5 = S.Task('c_t0_t2_t5', length=1, delay_cost=1)
	S += c_t0_t2_t5 >= 57
	c_t0_t2_t5 += MAS[1]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 57
	c_t1_t50_mem0 += MAS_MEM[0]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 57
	c_t1_t50_mem1 += MAS_MEM[3]

	c_t3_t2_t1 = S.Task('c_t3_t2_t1', length=7, delay_cost=1)
	S += c_t3_t2_t1 >= 57
	c_t3_t2_t1 += MM[0]

	c_t4_t2_t2_mem0 = S.Task('c_t4_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t2_mem0 >= 57
	c_t4_t2_t2_mem0 += MAS_MEM[2]

	c_t4_t2_t2_mem1 = S.Task('c_t4_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t2_mem1 >= 57
	c_t4_t2_t2_mem1 += MAS_MEM[1]

	c_t5_t2_t4_in = S.Task('c_t5_t2_t4_in', length=1, delay_cost=1)
	S += c_t5_t2_t4_in >= 57
	c_t5_t2_t4_in += MM_in[0]

	c_t5_t2_t4_mem0 = S.Task('c_t5_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t4_mem0 >= 57
	c_t5_t2_t4_mem0 += MAS_MEM[4]

	c_t5_t2_t4_mem1 = S.Task('c_t5_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t4_mem1 >= 57
	c_t5_t2_t4_mem1 += MAS_MEM[7]

	c_t5_t51 = S.Task('c_t5_t51', length=1, delay_cost=1)
	S += c_t5_t51 >= 57
	c_t5_t51 += MAS[2]

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	S += c210_w >= 58
	c210_w += MAIN_MEM_w

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	S += c_t0_t20 >= 58
	c_t0_t20 += MAS[0]

	c_t100_mem0 = S.Task('c_t100_mem0', length=1, delay_cost=1)
	S += c_t100_mem0 >= 58
	c_t100_mem0 += MAS_MEM[2]

	c_t100_mem1 = S.Task('c_t100_mem1', length=1, delay_cost=1)
	S += c_t100_mem1 >= 58
	c_t100_mem1 += MAS_MEM[3]

	c_t1_t50 = S.Task('c_t1_t50', length=1, delay_cost=1)
	S += c_t1_t50 >= 58
	c_t1_t50 += MAS[1]

	c_t3_t2_t2_mem0 = S.Task('c_t3_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t2_mem0 >= 58
	c_t3_t2_t2_mem0 += MAS_MEM[0]

	c_t3_t2_t2_mem1 = S.Task('c_t3_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t2_mem1 >= 58
	c_t3_t2_t2_mem1 += MAS_MEM[1]

	c_t4_t2_t2 = S.Task('c_t4_t2_t2', length=1, delay_cost=1)
	S += c_t4_t2_t2 >= 58
	c_t4_t2_t2 += MAS[3]

	c_t4_t2_t4_in = S.Task('c_t4_t2_t4_in', length=1, delay_cost=1)
	S += c_t4_t2_t4_in >= 58
	c_t4_t2_t4_in += MM_in[0]

	c_t4_t2_t4_mem0 = S.Task('c_t4_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t4_mem0 >= 58
	c_t4_t2_t4_mem0 += MAS_MEM[6]

	c_t4_t2_t4_mem1 = S.Task('c_t4_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t4_mem1 >= 58
	c_t4_t2_t4_mem1 += MAS_MEM[7]

	c_t5_t2_t4 = S.Task('c_t5_t2_t4', length=7, delay_cost=1)
	S += c_t5_t2_t4 >= 58
	c_t5_t2_t4 += MM[0]

	c_t5_t2_t5_mem0 = S.Task('c_t5_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t5_mem0 >= 58
	c_t5_t2_t5_mem0 += MM_MEM[0]

	c_t5_t2_t5_mem1 = S.Task('c_t5_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t5_mem1 >= 58
	c_t5_t2_t5_mem1 += MM_MEM[1]

	c_s1010_mem0 = S.Task('c_s1010_mem0', length=1, delay_cost=1)
	S += c_s1010_mem0 >= 59
	c_s1010_mem0 += MAS_MEM[6]

	c_s1010_mem1 = S.Task('c_s1010_mem1', length=1, delay_cost=1)
	S += c_s1010_mem1 >= 59
	c_s1010_mem1 += MAS_MEM[1]

	c_t100 = S.Task('c_t100', length=1, delay_cost=1)
	S += c_t100 >= 59
	c_t100 += MAS[3]

	c_t3_t2_t2 = S.Task('c_t3_t2_t2', length=1, delay_cost=1)
	S += c_t3_t2_t2 >= 59
	c_t3_t2_t2 += MAS[0]

	c_t4_t2_t4 = S.Task('c_t4_t2_t4', length=7, delay_cost=1)
	S += c_t4_t2_t4 >= 59
	c_t4_t2_t4 += MM[0]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 59
	c_t5_t20_mem0 += MM_MEM[0]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 59
	c_t5_t20_mem1 += MM_MEM[1]

	c_t5_t2_t5 = S.Task('c_t5_t2_t5', length=1, delay_cost=1)
	S += c_t5_t2_t5 >= 59
	c_t5_t2_t5 += MAS[1]

	c_t6_y1_0_mem0 = S.Task('c_t6_y1_0_mem0', length=1, delay_cost=1)
	S += c_t6_y1_0_mem0 >= 59
	c_t6_y1_0_mem0 += MAS_MEM[0]

	c_t6_y1_0_mem1 = S.Task('c_t6_y1_0_mem1', length=1, delay_cost=1)
	S += c_t6_y1_0_mem1 >= 59
	c_t6_y1_0_mem1 += MAS_MEM[3]

	c_s1010 = S.Task('c_s1010', length=1, delay_cost=1)
	S += c_s1010 >= 60
	c_s1010 += MAS[1]

	c_s1110_mem0 = S.Task('c_s1110_mem0', length=1, delay_cost=1)
	S += c_s1110_mem0 >= 60
	c_s1110_mem0 += MAS_MEM[6]

	c_s1110_mem1 = S.Task('c_s1110_mem1', length=1, delay_cost=1)
	S += c_s1110_mem1 >= 60
	c_s1110_mem1 += MAS_MEM[3]

	c_t3_t2_t4_in = S.Task('c_t3_t2_t4_in', length=1, delay_cost=1)
	S += c_t3_t2_t4_in >= 60
	c_t3_t2_t4_in += MM_in[0]

	c_t3_t2_t4_mem0 = S.Task('c_t3_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t4_mem0 >= 60
	c_t3_t2_t4_mem0 += MAS_MEM[0]

	c_t3_t2_t4_mem1 = S.Task('c_t3_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t4_mem1 >= 60
	c_t3_t2_t4_mem1 += MAS_MEM[5]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 60
	c_t4_t31_mem0 += MM_MEM[0]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 60
	c_t4_t31_mem1 += MAS_MEM[1]

	c_t5_t20 = S.Task('c_t5_t20', length=1, delay_cost=1)
	S += c_t5_t20 >= 60
	c_t5_t20 += MAS[2]

	c_t6_y1_0 = S.Task('c_t6_y1_0', length=1, delay_cost=1)
	S += c_t6_y1_0 >= 60
	c_t6_y1_0 += MAS[0]

	c_s1110 = S.Task('c_s1110', length=1, delay_cost=1)
	S += c_s1110 >= 61
	c_s1110 += MAS[2]

	c_t3_t2_t4 = S.Task('c_t3_t2_t4', length=7, delay_cost=1)
	S += c_t3_t2_t4 >= 61
	c_t3_t2_t4 += MM[0]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	S += c_t3_t41_mem0 >= 61
	c_t3_t41_mem0 += MAS_MEM[0]

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	S += c_t3_t41_mem1 >= 61
	c_t3_t41_mem1 += MAS_MEM[1]

	c_t4_t2_t5_mem0 = S.Task('c_t4_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t5_mem0 >= 61
	c_t4_t2_t5_mem0 += MM_MEM[0]

	c_t4_t2_t5_mem1 = S.Task('c_t4_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t5_mem1 >= 61
	c_t4_t2_t5_mem1 += MM_MEM[1]

	c_t4_t31 = S.Task('c_t4_t31', length=1, delay_cost=1)
	S += c_t4_t31 >= 61
	c_t4_t31 += MAS[1]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	S += c_t4_t40_mem0 >= 61
	c_t4_t40_mem0 += MAS_MEM[4]

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	S += c_t4_t40_mem1 >= 61
	c_t4_t40_mem1 += MAS_MEM[3]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	S += c_t4_t41_mem0 >= 61
	c_t4_t41_mem0 += MAS_MEM[2]

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	S += c_t4_t41_mem1 >= 61
	c_t4_t41_mem1 += MAS_MEM[5]

	c_t311_mem0 = S.Task('c_t311_mem0', length=1, delay_cost=1)
	S += c_t311_mem0 >= 62
	c_t311_mem0 += MAS_MEM[0]

	c_t311_mem1 = S.Task('c_t311_mem1', length=1, delay_cost=1)
	S += c_t311_mem1 >= 62
	c_t311_mem1 += MAS_MEM[1]

	c_t3_t41 = S.Task('c_t3_t41', length=1, delay_cost=1)
	S += c_t3_t41 >= 62
	c_t3_t41 += MAS[2]

	c_t411_mem0 = S.Task('c_t411_mem0', length=1, delay_cost=1)
	S += c_t411_mem0 >= 62
	c_t411_mem0 += MAS_MEM[2]

	c_t411_mem1 = S.Task('c_t411_mem1', length=1, delay_cost=1)
	S += c_t411_mem1 >= 62
	c_t411_mem1 += MAS_MEM[3]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 62
	c_t4_t20_mem0 += MM_MEM[0]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 62
	c_t4_t20_mem1 += MM_MEM[1]

	c_t4_t2_t5 = S.Task('c_t4_t2_t5', length=1, delay_cost=1)
	S += c_t4_t2_t5 >= 62
	c_t4_t2_t5 += MAS[3]

	c_t4_t40 = S.Task('c_t4_t40', length=1, delay_cost=1)
	S += c_t4_t40 >= 62
	c_t4_t40 += MAS[1]

	c_t4_t41 = S.Task('c_t4_t41', length=1, delay_cost=1)
	S += c_t4_t41 >= 62
	c_t4_t41 += MAS[0]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 63
	c_t2_t21_mem0 += MM_MEM[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 63
	c_t2_t21_mem1 += MAS_MEM[5]

	c_t311 = S.Task('c_t311', length=1, delay_cost=1)
	S += c_t311 >= 63
	c_t311 += MAS[3]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	S += c_t3_t40_mem0 >= 63
	c_t3_t40_mem0 += MAS_MEM[0]

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	S += c_t3_t40_mem1 >= 63
	c_t3_t40_mem1 += MAS_MEM[1]

	c_t411 = S.Task('c_t411', length=1, delay_cost=1)
	S += c_t411 >= 63
	c_t411 += MAS[0]

	c_t4_t20 = S.Task('c_t4_t20', length=1, delay_cost=1)
	S += c_t4_t20 >= 63
	c_t4_t20 += MAS[1]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	S += c_t4_t50_mem0 >= 63
	c_t4_t50_mem0 += MAS_MEM[4]

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	S += c_t4_t50_mem1 >= 63
	c_t4_t50_mem1 += MAS_MEM[3]

	c_s011_mem0 = S.Task('c_s011_mem0', length=1, delay_cost=1)
	S += c_s011_mem0 >= 64
	c_s011_mem0 += MAS_MEM[6]

	c_s011_mem1 = S.Task('c_s011_mem1', length=1, delay_cost=1)
	S += c_s011_mem1 >= 64
	c_s011_mem1 += MAS_MEM[5]

	c_s2011_mem0 = S.Task('c_s2011_mem0', length=1, delay_cost=1)
	S += c_s2011_mem0 >= 64
	c_s2011_mem0 += MAS_MEM[2]

	c_s2011_mem1 = S.Task('c_s2011_mem1', length=1, delay_cost=1)
	S += c_s2011_mem1 >= 64
	c_s2011_mem1 += MAS_MEM[1]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 64
	c_t1_t21_mem0 += MM_MEM[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 64
	c_t1_t21_mem1 += MAS_MEM[3]

	c_t201_mem0 = S.Task('c_t201_mem0', length=1, delay_cost=1)
	S += c_t201_mem0 >= 64
	c_t201_mem0 += MAS_MEM[0]

	c_t201_mem1 = S.Task('c_t201_mem1', length=1, delay_cost=1)
	S += c_t201_mem1 >= 64
	c_t201_mem1 += MAS_MEM[7]

	c_t2_t21 = S.Task('c_t2_t21', length=1, delay_cost=1)
	S += c_t2_t21 >= 64
	c_t2_t21 += MAS[0]

	c_t3_t40 = S.Task('c_t3_t40', length=1, delay_cost=1)
	S += c_t3_t40 >= 64
	c_t3_t40 += MAS[2]

	c_t4_t50 = S.Task('c_t4_t50', length=1, delay_cost=1)
	S += c_t4_t50 >= 64
	c_t4_t50 += MAS[1]

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	S += c111_mem0 >= 65
	c111_mem0 += MAS_MEM[4]

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	S += c111_mem1 >= 65
	c111_mem1 += MAS_MEM[7]

	c_s011 = S.Task('c_s011', length=1, delay_cost=1)
	S += c_s011 >= 65
	c_s011 += MAS[2]

	c_s2011 = S.Task('c_s2011', length=1, delay_cost=1)
	S += c_s2011 >= 65
	c_s2011 += MAS[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 65
	c_t0_t21_mem0 += MM_MEM[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 65
	c_t0_t21_mem1 += MAS_MEM[3]

	c_t1_t21 = S.Task('c_t1_t21', length=1, delay_cost=1)
	S += c_t1_t21 >= 65
	c_t1_t21 += MAS[0]

	c_t200_mem0 = S.Task('c_t200_mem0', length=1, delay_cost=1)
	S += c_t200_mem0 >= 65
	c_t200_mem0 += MAS_MEM[0]

	c_t200_mem1 = S.Task('c_t200_mem1', length=1, delay_cost=1)
	S += c_t200_mem1 >= 65
	c_t200_mem1 += MAS_MEM[5]

	c_t201 = S.Task('c_t201', length=1, delay_cost=1)
	S += c_t201 >= 65
	c_t201 += MAS[3]

	c_t6_y1_1_mem0 = S.Task('c_t6_y1_1_mem0', length=1, delay_cost=1)
	S += c_t6_y1_1_mem0 >= 65
	c_t6_y1_1_mem0 += MAS_MEM[2]

	c_t6_y1_1_mem1 = S.Task('c_t6_y1_1_mem1', length=1, delay_cost=1)
	S += c_t6_y1_1_mem1 >= 65
	c_t6_y1_1_mem1 += MAS_MEM[1]

	c111 = S.Task('c111', length=1, delay_cost=1)
	S += c111 >= 66
	c111 += MAS[2]

	c_s010_mem0 = S.Task('c_s010_mem0', length=1, delay_cost=1)
	S += c_s010_mem0 >= 66
	c_s010_mem0 += MAS_MEM[0]

	c_s010_mem1 = S.Task('c_s010_mem1', length=1, delay_cost=1)
	S += c_s010_mem1 >= 66
	c_s010_mem1 += MAS_MEM[1]

	c_s1000_mem0 = S.Task('c_s1000_mem0', length=1, delay_cost=1)
	S += c_s1000_mem0 >= 66
	c_s1000_mem0 += MAS_MEM[6]

	c_s1000_mem1 = S.Task('c_s1000_mem1', length=1, delay_cost=1)
	S += c_s1000_mem1 >= 66
	c_s1000_mem1 += MAS_MEM[7]

	c_t001_mem0 = S.Task('c_t001_mem0', length=1, delay_cost=1)
	S += c_t001_mem0 >= 66
	c_t001_mem0 += MAS_MEM[2]

	c_t001_mem1 = S.Task('c_t001_mem1', length=1, delay_cost=1)
	S += c_t001_mem1 >= 66
	c_t001_mem1 += MAS_MEM[5]

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	S += c_t0_t21 >= 66
	c_t0_t21 += MAS[1]

	c_t200 = S.Task('c_t200', length=1, delay_cost=1)
	S += c_t200 >= 66
	c_t200 += MAS[3]

	c_t3_t2_t5_mem0 = S.Task('c_t3_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t5_mem0 >= 66
	c_t3_t2_t5_mem0 += MM_MEM[0]

	c_t3_t2_t5_mem1 = S.Task('c_t3_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t5_mem1 >= 66
	c_t3_t2_t5_mem1 += MM_MEM[1]

	c_t6_y1_1 = S.Task('c_t6_y1_1', length=1, delay_cost=1)
	S += c_t6_y1_1 >= 66
	c_t6_y1_1 += MAS[0]

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	S += c110_mem0 >= 67
	c110_mem0 += MAS_MEM[4]

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	S += c110_mem1 >= 67
	c110_mem1 += MAS_MEM[7]

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	S += c111_w >= 67
	c111_w += MAIN_MEM_w

	c_s010 = S.Task('c_s010', length=1, delay_cost=1)
	S += c_s010 >= 67
	c_s010 += MAS[2]

	c_s1000 = S.Task('c_s1000', length=1, delay_cost=1)
	S += c_s1000 >= 67
	c_s1000 += MAS[0]

	c_s1111_mem0 = S.Task('c_s1111_mem0', length=1, delay_cost=1)
	S += c_s1111_mem0 >= 67
	c_s1111_mem0 += MAS_MEM[0]

	c_s1111_mem1 = S.Task('c_s1111_mem1', length=1, delay_cost=1)
	S += c_s1111_mem1 >= 67
	c_s1111_mem1 += MAS_MEM[1]

	c_s211_mem0 = S.Task('c_s211_mem0', length=1, delay_cost=1)
	S += c_s211_mem0 >= 67
	c_s211_mem0 += MAS_MEM[2]

	c_s211_mem1 = S.Task('c_s211_mem1', length=1, delay_cost=1)
	S += c_s211_mem1 >= 67
	c_s211_mem1 += MAS_MEM[3]

	c_t001 = S.Task('c_t001', length=1, delay_cost=1)
	S += c_t001 >= 67
	c_t001 += MAS[3]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 67
	c_t3_t20_mem0 += MM_MEM[0]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 67
	c_t3_t20_mem1 += MM_MEM[1]

	c_t3_t2_t5 = S.Task('c_t3_t2_t5', length=1, delay_cost=1)
	S += c_t3_t2_t5 >= 67
	c_t3_t2_t5 += MAS[1]

	c110 = S.Task('c110', length=1, delay_cost=1)
	S += c110 >= 68
	c110 += MAS[2]

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	S += c211_mem0 >= 68
	c211_mem0 += MAS_MEM[2]

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	S += c211_mem1 >= 68
	c211_mem1 += MAS_MEM[3]

	c_s1111 = S.Task('c_s1111', length=1, delay_cost=1)
	S += c_s1111 >= 68
	c_s1111 += MAS[3]

	c_s1_y1_0_mem0 = S.Task('c_s1_y1_0_mem0', length=1, delay_cost=1)
	S += c_s1_y1_0_mem0 >= 68
	c_s1_y1_0_mem0 += MAS_MEM[4]

	c_s1_y1_0_mem1 = S.Task('c_s1_y1_0_mem1', length=1, delay_cost=1)
	S += c_s1_y1_0_mem1 >= 68
	c_s1_y1_0_mem1 += MAS_MEM[7]

	c_s1_y1_1_mem0 = S.Task('c_s1_y1_1_mem0', length=1, delay_cost=1)
	S += c_s1_y1_1_mem0 >= 68
	c_s1_y1_1_mem0 += MAS_MEM[6]

	c_s1_y1_1_mem1 = S.Task('c_s1_y1_1_mem1', length=1, delay_cost=1)
	S += c_s1_y1_1_mem1 >= 68
	c_s1_y1_1_mem1 += MAS_MEM[5]

	c_s211 = S.Task('c_s211', length=1, delay_cost=1)
	S += c_s211 >= 68
	c_s211 += MAS[1]

	c_t000_mem0 = S.Task('c_t000_mem0', length=1, delay_cost=1)
	S += c_t000_mem0 >= 68
	c_t000_mem0 += MAS_MEM[0]

	c_t000_mem1 = S.Task('c_t000_mem1', length=1, delay_cost=1)
	S += c_t000_mem1 >= 68
	c_t000_mem1 += MAS_MEM[1]

	c_t3_t20 = S.Task('c_t3_t20', length=1, delay_cost=1)
	S += c_t3_t20 >= 68
	c_t3_t20 += MAS[0]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 69
	c000_mem0 += MAS_MEM[4]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 69
	c000_mem1 += MAS_MEM[7]

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	S += c110_w >= 69
	c110_w += MAIN_MEM_w

	c211 = S.Task('c211', length=1, delay_cost=1)
	S += c211 >= 69
	c211 += MAS[0]

	c_s1_y1_0 = S.Task('c_s1_y1_0', length=1, delay_cost=1)
	S += c_s1_y1_0 >= 69
	c_s1_y1_0 += MAS[3]

	c_s1_y1_1 = S.Task('c_s1_y1_1', length=1, delay_cost=1)
	S += c_s1_y1_1 >= 69
	c_s1_y1_1 += MAS[1]

	c_t000 = S.Task('c_t000', length=1, delay_cost=1)
	S += c_t000 >= 69
	c_t000 += MAS[2]

	c_t400_mem0 = S.Task('c_t400_mem0', length=1, delay_cost=1)
	S += c_t400_mem0 >= 69
	c_t400_mem0 += MAS_MEM[2]

	c_t400_mem1 = S.Task('c_t400_mem1', length=1, delay_cost=1)
	S += c_t400_mem1 >= 69
	c_t400_mem1 += MAS_MEM[3]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	S += c_t5_t50_mem0 >= 69
	c_t5_t50_mem0 += MAS_MEM[6]

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	S += c_t5_t50_mem1 >= 69
	c_t5_t50_mem1 += MAS_MEM[1]

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 70
	c000 += MAS[0]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 70
	c001_mem0 += MAS_MEM[6]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 70
	c001_mem1 += MAS_MEM[3]

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	S += c211_w >= 70
	c211_w += MAIN_MEM_w

	c_s0000_mem0 = S.Task('c_s0000_mem0', length=1, delay_cost=1)
	S += c_s0000_mem0 >= 70
	c_s0000_mem0 += MAS_MEM[4]

	c_s0000_mem1 = S.Task('c_s0000_mem1', length=1, delay_cost=1)
	S += c_s0000_mem1 >= 70
	c_s0000_mem1 += MAS_MEM[7]

	c_s1100_mem0 = S.Task('c_s1100_mem0', length=1, delay_cost=1)
	S += c_s1100_mem0 >= 70
	c_s1100_mem0 += MAS_MEM[2]

	c_s1100_mem1 = S.Task('c_s1100_mem1', length=1, delay_cost=1)
	S += c_s1100_mem1 >= 70
	c_s1100_mem1 += MAS_MEM[1]

	c_t400 = S.Task('c_t400', length=1, delay_cost=1)
	S += c_t400 >= 70
	c_t400 += MAS[1]

	c_t5_t50 = S.Task('c_t5_t50', length=1, delay_cost=1)
	S += c_t5_t50 >= 70
	c_t5_t50 += MAS[3]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 71
	c000_w += MAIN_MEM_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 71
	c001 += MAS[2]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 71
	c010_mem0 += MAS_MEM[4]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 71
	c010_mem1 += MAS_MEM[7]

	c_s0000 = S.Task('c_s0000', length=1, delay_cost=1)
	S += c_s0000 >= 71
	c_s0000 += MAS[0]

	c_s000_mem0 = S.Task('c_s000_mem0', length=1, delay_cost=1)
	S += c_s000_mem0 >= 71
	c_s000_mem0 += MAS_MEM[2]

	c_s000_mem1 = S.Task('c_s000_mem1', length=1, delay_cost=1)
	S += c_s000_mem1 >= 71
	c_s000_mem1 += MAS_MEM[1]

	c_s1100 = S.Task('c_s1100', length=1, delay_cost=1)
	S += c_s1100 >= 71
	c_s1100 += MAS[3]

	c_t3_t51_mem0 = S.Task('c_t3_t51_mem0', length=1, delay_cost=1)
	S += c_t3_t51_mem0 >= 71
	c_t3_t51_mem0 += MAS_MEM[0]

	c_t3_t51_mem1 = S.Task('c_t3_t51_mem1', length=1, delay_cost=1)
	S += c_t3_t51_mem1 >= 71
	c_t3_t51_mem1 += MAS_MEM[5]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 71
	c_t5_t21_mem0 += MM_MEM[0]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 71
	c_t5_t21_mem1 += MAS_MEM[3]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 72
	c001_w += MAIN_MEM_w

	c010 = S.Task('c010', length=1, delay_cost=1)
	S += c010 >= 72
	c010 += MAS[3]

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	S += c100_mem0 >= 72
	c100_mem0 += MAS_MEM[4]

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	S += c100_mem1 >= 72
	c100_mem1 += MAS_MEM[1]

	c_s000 = S.Task('c_s000', length=1, delay_cost=1)
	S += c_s000 >= 72
	c_s000 += MAS[2]

	c_s2001_mem0 = S.Task('c_s2001_mem0', length=1, delay_cost=1)
	S += c_s2001_mem0 >= 72
	c_s2001_mem0 += MAS_MEM[6]

	c_s2001_mem1 = S.Task('c_s2001_mem1', length=1, delay_cost=1)
	S += c_s2001_mem1 >= 72
	c_s2001_mem1 += MAS_MEM[7]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 72
	c_t3_t21_mem0 += MM_MEM[0]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 72
	c_t3_t21_mem1 += MAS_MEM[3]

	c_t3_t51 = S.Task('c_t3_t51', length=1, delay_cost=1)
	S += c_t3_t51 >= 72
	c_t3_t51 += MAS[0]

	c_t501_mem0 = S.Task('c_t501_mem0', length=1, delay_cost=1)
	S += c_t501_mem0 >= 72
	c_t501_mem0 += MAS_MEM[2]

	c_t501_mem1 = S.Task('c_t501_mem1', length=1, delay_cost=1)
	S += c_t501_mem1 >= 72
	c_t501_mem1 += MAS_MEM[5]

	c_t5_t21 = S.Task('c_t5_t21', length=1, delay_cost=1)
	S += c_t5_t21 >= 72
	c_t5_t21 += MAS[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 73
	c010_w += MAIN_MEM_w

	c100 = S.Task('c100', length=1, delay_cost=1)
	S += c100 >= 73
	c100 += MAS[3]

	c_s2000_mem0 = S.Task('c_s2000_mem0', length=1, delay_cost=1)
	S += c_s2000_mem0 >= 73
	c_s2000_mem0 += MAS_MEM[6]

	c_s2000_mem1 = S.Task('c_s2000_mem1', length=1, delay_cost=1)
	S += c_s2000_mem1 >= 73
	c_s2000_mem1 += MAS_MEM[5]

	c_s2001 = S.Task('c_s2001', length=1, delay_cost=1)
	S += c_s2001 >= 73
	c_s2001 += MAS[0]

	c_s201_mem0 = S.Task('c_s201_mem0', length=1, delay_cost=1)
	S += c_s201_mem0 >= 73
	c_s201_mem0 += MAS_MEM[2]

	c_s201_mem1 = S.Task('c_s201_mem1', length=1, delay_cost=1)
	S += c_s201_mem1 >= 73
	c_s201_mem1 += MAS_MEM[1]

	c_t101_mem0 = S.Task('c_t101_mem0', length=1, delay_cost=1)
	S += c_t101_mem0 >= 73
	c_t101_mem0 += MAS_MEM[0]

	c_t101_mem1 = S.Task('c_t101_mem1', length=1, delay_cost=1)
	S += c_t101_mem1 >= 73
	c_t101_mem1 += MAS_MEM[3]

	c_t3_t21 = S.Task('c_t3_t21', length=1, delay_cost=1)
	S += c_t3_t21 >= 73
	c_t3_t21 += MAS[2]

	c_t500_mem0 = S.Task('c_t500_mem0', length=1, delay_cost=1)
	S += c_t500_mem0 >= 73
	c_t500_mem0 += MAS_MEM[4]

	c_t500_mem1 = S.Task('c_t500_mem1', length=1, delay_cost=1)
	S += c_t500_mem1 >= 73
	c_t500_mem1 += MAS_MEM[7]

	c_t501 = S.Task('c_t501', length=1, delay_cost=1)
	S += c_t501 >= 73
	c_t501 += MAS[1]

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	S += c100_w >= 74
	c100_w += MAIN_MEM_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 74
	c201_mem0 += MAS_MEM[2]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 74
	c201_mem1 += MAS_MEM[5]

	c_s0001_mem0 = S.Task('c_s0001_mem0', length=1, delay_cost=1)
	S += c_s0001_mem0 >= 74
	c_s0001_mem0 += MAS_MEM[6]

	c_s0001_mem1 = S.Task('c_s0001_mem1', length=1, delay_cost=1)
	S += c_s0001_mem1 >= 74
	c_s0001_mem1 += MAS_MEM[3]

	c_s2000 = S.Task('c_s2000', length=1, delay_cost=1)
	S += c_s2000 >= 74
	c_s2000 += MAS[3]

	c_s200_mem0 = S.Task('c_s200_mem0', length=1, delay_cost=1)
	S += c_s200_mem0 >= 74
	c_s200_mem0 += MAS_MEM[0]

	c_s200_mem1 = S.Task('c_s200_mem1', length=1, delay_cost=1)
	S += c_s200_mem1 >= 74
	c_s200_mem1 += MAS_MEM[7]

	c_s201 = S.Task('c_s201', length=1, delay_cost=1)
	S += c_s201 >= 74
	c_s201 += MAS[2]

	c_t101 = S.Task('c_t101', length=1, delay_cost=1)
	S += c_t101 >= 74
	c_t101 += MAS[1]

	c_t301_mem0 = S.Task('c_t301_mem0', length=1, delay_cost=1)
	S += c_t301_mem0 >= 74
	c_t301_mem0 += MAS_MEM[4]

	c_t301_mem1 = S.Task('c_t301_mem1', length=1, delay_cost=1)
	S += c_t301_mem1 >= 74
	c_t301_mem1 += MAS_MEM[1]

	c_t500 = S.Task('c_t500', length=1, delay_cost=1)
	S += c_t500 >= 74
	c_t500 += MAS[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 75
	c200_mem0 += MAS_MEM[6]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 75
	c200_mem1 += MAS_MEM[3]

	c201 = S.Task('c201', length=1, delay_cost=1)
	S += c201 >= 75
	c201 += MAS[3]

	c_s0001 = S.Task('c_s0001', length=1, delay_cost=1)
	S += c_s0001 >= 75
	c_s0001 += MAS[2]

	c_s001_mem0 = S.Task('c_s001_mem0', length=1, delay_cost=1)
	S += c_s001_mem0 >= 75
	c_s001_mem0 += MAS_MEM[0]

	c_s001_mem1 = S.Task('c_s001_mem1', length=1, delay_cost=1)
	S += c_s001_mem1 >= 75
	c_s001_mem1 += MAS_MEM[5]

	c_s200 = S.Task('c_s200', length=1, delay_cost=1)
	S += c_s200 >= 75
	c_s200 += MAS[1]

	c_t301 = S.Task('c_t301', length=1, delay_cost=1)
	S += c_t301 >= 75
	c_t301 += MAS[0]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 75
	c_t4_t21_mem0 += MM_MEM[0]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 75
	c_t4_t21_mem1 += MAS_MEM[7]

	c_t4_t51_mem0 = S.Task('c_t4_t51_mem0', length=1, delay_cost=1)
	S += c_t4_t51_mem0 >= 75
	c_t4_t51_mem0 += MAS_MEM[2]

	c_t4_t51_mem1 = S.Task('c_t4_t51_mem1', length=1, delay_cost=1)
	S += c_t4_t51_mem1 >= 75
	c_t4_t51_mem1 += MAS_MEM[1]

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	S += c101_mem0 >= 76
	c101_mem0 += MAS_MEM[0]

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	S += c101_mem1 >= 76
	c101_mem1 += MAS_MEM[1]

	c200 = S.Task('c200', length=1, delay_cost=1)
	S += c200 >= 76
	c200 += MAS[2]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 76
	c201_w += MAIN_MEM_w

	c_s001 = S.Task('c_s001', length=1, delay_cost=1)
	S += c_s001 >= 76
	c_s001 += MAS[0]

	c_s1001_mem0 = S.Task('c_s1001_mem0', length=1, delay_cost=1)
	S += c_s1001_mem0 >= 76
	c_s1001_mem0 += MAS_MEM[2]

	c_s1001_mem1 = S.Task('c_s1001_mem1', length=1, delay_cost=1)
	S += c_s1001_mem1 >= 76
	c_s1001_mem1 += MAS_MEM[7]

	c_t401_mem0 = S.Task('c_t401_mem0', length=1, delay_cost=1)
	S += c_t401_mem0 >= 76
	c_t401_mem0 += MAS_MEM[6]

	c_t401_mem1 = S.Task('c_t401_mem1', length=1, delay_cost=1)
	S += c_t401_mem1 >= 76
	c_t401_mem1 += MAS_MEM[3]

	c_t4_t21 = S.Task('c_t4_t21', length=1, delay_cost=1)
	S += c_t4_t21 >= 76
	c_t4_t21 += MAS[3]

	c_t4_t51 = S.Task('c_t4_t51', length=1, delay_cost=1)
	S += c_t4_t51 >= 76
	c_t4_t51 += MAS[1]

	c101 = S.Task('c101', length=1, delay_cost=1)
	S += c101 >= 77
	c101 += MAS[2]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 77
	c200_w += MAIN_MEM_w

	c_s1001 = S.Task('c_s1001', length=1, delay_cost=1)
	S += c_s1001 >= 77
	c_s1001 += MAS[3]

	c_s1101_mem0 = S.Task('c_s1101_mem0', length=1, delay_cost=1)
	S += c_s1101_mem0 >= 77
	c_s1101_mem0 += MAS_MEM[2]

	c_s1101_mem1 = S.Task('c_s1101_mem1', length=1, delay_cost=1)
	S += c_s1101_mem1 >= 77
	c_s1101_mem1 += MAS_MEM[7]

	c_t401 = S.Task('c_t401', length=1, delay_cost=1)
	S += c_t401 >= 77
	c_t401 += MAS[1]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 78
	c011_mem0 += MAS_MEM[0]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 78
	c011_mem1 += MAS_MEM[1]

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	S += c101_w >= 78
	c101_w += MAIN_MEM_w

	c_s1101 = S.Task('c_s1101', length=1, delay_cost=1)
	S += c_s1101 >= 78
	c_s1101 += MAS[0]

	c011 = S.Task('c011', length=1, delay_cost=1)
	S += c011 >= 79
	c011 += MAS[1]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 80
	c011_w += MAIN_MEM_w


	# new tasks
	c_t3_t50 = S.Task('c_t3_t50', length=1, delay_cost=1)
	c_t3_t50 += alt(MAS)

	S += c_t3_t50<71

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	c_t3_t50_mem0 += MAS_MEM[0]
	S += 45 < c_t3_t50_mem0
	S += c_t3_t50_mem0 <= c_t3_t50

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	c_t3_t50_mem1 += MAS_MEM[5]
	S += 64 < c_t3_t50_mem1
	S += c_t3_t50_mem1 <= c_t3_t50

	c_t300 = S.Task('c_t300', length=1, delay_cost=1)
	c_t300 += alt(MAS)

	S += c_t300<72

	c_t300_mem0 = S.Task('c_t300_mem0', length=1, delay_cost=1)
	c_t300_mem0 += MAS_MEM[0]
	S += 68 < c_t300_mem0
	S += c_t300_mem0 <= c_t300

	c_t300_mem1 = S.Task('c_t300_mem1', length=1, delay_cost=1)
	c_t300_mem1 += alt(MAS_MEM)
	S += (c_t3_t50*MAS[0])-1 < c_t300_mem1*MAS_MEM[1]
	S += (c_t3_t50*MAS[1])-1 < c_t300_mem1*MAS_MEM[3]
	S += (c_t3_t50*MAS[2])-1 < c_t300_mem1*MAS_MEM[5]
	S += (c_t3_t50*MAS[3])-1 < c_t300_mem1*MAS_MEM[7]
	S += c_t300_mem1 <= c_t300

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage7MM1_stage1MAS4/SQR/schedule7.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

