from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 141
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling
	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 0
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 0
	t5_t1_mem0 += MAIN_MEM_r

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 0
	t5_t1_mem1 += MAIN_MEM_r

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 1
	t5_t0_in += MM_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 1
	t5_t0_mem0 += MAIN_MEM_r

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 1
	t5_t0_mem1 += MAIN_MEM_r

	t5_t1 = S.Task('t5_t1', length=5, delay_cost=1)
	S += t5_t1 >= 1
	t5_t1 += MM[0]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 2
	t1_t3_in += MM_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 2
	t1_t3_mem0 += MAIN_MEM_r

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 2
	t1_t3_mem1 += MAIN_MEM_r

	t5_t0 = S.Task('t5_t0', length=5, delay_cost=1)
	S += t5_t0 >= 2
	t5_t0 += MM[0]

	t1_t3 = S.Task('t1_t3', length=5, delay_cost=1)
	S += t1_t3 >= 3
	t1_t3 += MM[0]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 3
	t7_t3_in += MM_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 3
	t7_t3_mem0 += MAIN_MEM_r

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 3
	t7_t3_mem1 += MAIN_MEM_r

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 4
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 4
	t0_t3_mem0 += MAIN_MEM_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 4
	t0_t3_mem1 += MAIN_MEM_r

	t7_t3 = S.Task('t7_t3', length=5, delay_cost=1)
	S += t7_t3 >= 4
	t7_t3 += MM[0]

	t0_t3 = S.Task('t0_t3', length=5, delay_cost=1)
	S += t0_t3 >= 5
	t0_t3 += MM[0]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 5
	t10_t1_in += MM_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 5
	t10_t1_mem0 += MAIN_MEM_r

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 5
	t10_t1_mem1 += MAIN_MEM_r

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 6
	t10_t0_in += MM_in[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 6
	t10_t0_mem0 += MAIN_MEM_r

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 6
	t10_t0_mem1 += MAIN_MEM_r

	t10_t1 = S.Task('t10_t1', length=5, delay_cost=1)
	S += t10_t1 >= 6
	t10_t1 += MM[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 6
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 6
	t50_mem1 += MM_MEM[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 7
	t0_t0_mem0 += MAIN_MEM_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 7
	t0_t0_mem1 += MAIN_MEM_r

	t10_t0 = S.Task('t10_t0', length=5, delay_cost=1)
	S += t10_t0 >= 7
	t10_t0 += MM[0]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 7
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 7
	t1_t5_mem1 += MM_MEM[0]

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 7
	t50 += MAS[2]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 7
	t60_mem0 += MAS_MEM[2]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 7
	t60_mem1 += MAS_MEM[2]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 8
	t0_t0 += MAS[3]

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	S += t1_t5 >= 8
	t1_t5 += MAS[2]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 8
	t5_t2_mem0 += MAIN_MEM_r

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 8
	t5_t2_mem1 += MAIN_MEM_r

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 8
	t60 += MAS[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 8
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 8
	t71_mem1 += MM_MEM[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 9
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 9
	t01_mem1 += MM_MEM[0]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 9
	t5_t2 += MAS[0]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 9
	t71 += MAS[2]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 9
	t7_t1_mem0 += MAIN_MEM_r

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 9
	t7_t1_mem1 += MAIN_MEM_r

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 9
	t81_mem0 += MAS_MEM[2]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 9
	t81_mem1 += MAS_MEM[2]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 10
	t01 += MAS[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 10
	t0_t1_mem0 += MAIN_MEM_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 10
	t0_t1_mem1 += MAIN_MEM_r

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 10
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 10
	t5_t5_mem1 += MM_MEM[0]

	t7_t1 = S.Task('t7_t1', length=1, delay_cost=1)
	S += t7_t1 >= 10
	t7_t1 += MAS[2]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 10
	t81 += MAS[3]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 10
	t91_mem0 += MAS_MEM[3]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 10
	t91_mem1 += MAS_MEM[2]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 11
	t0_t1 += MAS[0]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 11
	t0_t2_in += MM_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 11
	t0_t2_mem0 += MAS_MEM[3]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 11
	t0_t2_mem1 += MAS_MEM[0]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 11
	t100_mem0 += MM_MEM[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 11
	t100_mem1 += MM_MEM[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 11
	t5_t3_mem0 += MAIN_MEM_r

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 11
	t5_t3_mem1 += MAIN_MEM_r

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 11
	t5_t5 += MAS[2]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 11
	t91 += MAS[3]

	t0_t2 = S.Task('t0_t2', length=5, delay_cost=1)
	S += t0_t2 >= 12
	t0_t2 += MM[0]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 12
	t100 += MAS[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 12
	t110_mem0 += MAS_MEM[1]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 12
	t110_mem1 += MAS_MEM[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 12
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 12
	t11_mem1 += MM_MEM[0]

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 12
	t5_t3 += MAS[0]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 12
	t5_t4_in += MM_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 12
	t5_t4_mem0 += MAS_MEM[0]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 12
	t5_t4_mem1 += MAS_MEM[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 12
	t7_t0_mem0 += MAIN_MEM_r

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 12
	t7_t0_mem1 += MAIN_MEM_r

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 13
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 13
	t0_t5_mem1 += MM_MEM[0]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 13
	t11 += MAS[2]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 13
	t110 += MAS[1]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 13
	t1_t0_mem0 += MAIN_MEM_r

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 13
	t1_t0_mem1 += MAIN_MEM_r

	t5_t4 = S.Task('t5_t4', length=5, delay_cost=1)
	S += t5_t4 >= 13
	t5_t4 += MM[0]

	t7_t0 = S.Task('t7_t0', length=1, delay_cost=1)
	S += t7_t0 >= 13
	t7_t0 += MAS[3]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 13
	t7_t2_in += MM_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 13
	t7_t2_mem0 += MAS_MEM[3]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 13
	t7_t2_mem1 += MAS_MEM[2]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 14
	t0_t5 += MAS[0]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 14
	t10_t3_mem0 += MAIN_MEM_r

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 14
	t10_t3_mem1 += MAIN_MEM_r

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 14
	t10_t5_mem0 += MM_MEM[0]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 14
	t10_t5_mem1 += MM_MEM[0]

	t1_t0 = S.Task('t1_t0', length=1, delay_cost=1)
	S += t1_t0 >= 14
	t1_t0 += MAS[3]

	t7_t2 = S.Task('t7_t2', length=5, delay_cost=1)
	S += t7_t2 >= 14
	t7_t2 += MM[0]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 15
	t10_t2_mem0 += MAIN_MEM_r

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 15
	t10_t2_mem1 += MAIN_MEM_r

	t10_t3 = S.Task('t10_t3', length=1, delay_cost=1)
	S += t10_t3 >= 15
	t10_t3 += MAS[0]

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	S += t10_t5 >= 15
	t10_t5 += MAS[1]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 15
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 15
	t7_t5_mem1 += MM_MEM[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 16
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 16
	t00_mem1 += MAS_MEM[0]

	t10_t2 = S.Task('t10_t2', length=1, delay_cost=1)
	S += t10_t2 >= 16
	t10_t2 += MAS[3]

	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	S += t10_t4_in >= 16
	t10_t4_in += MM_in[0]

	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	S += t10_t4_mem0 >= 16
	t10_t4_mem0 += MAS_MEM[3]

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	S += t10_t4_mem1 >= 16
	t10_t4_mem1 += MAS_MEM[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 16
	t2_t2_mem0 += MAIN_MEM_r

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 16
	t2_t2_mem1 += MAIN_MEM_r

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 16
	t7_t5 += MAS[2]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 17
	t00 += MAS[3]

	t10_t4 = S.Task('t10_t4', length=5, delay_cost=1)
	S += t10_t4 >= 17
	t10_t4 += MM[0]

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	S += t18_t0_mem0 >= 17
	t18_t0_mem0 += MAS_MEM[3]

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	S += t18_t0_mem1 >= 17
	t18_t0_mem1 += MAS_MEM[0]

	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	S += t18_t3_in >= 17
	t18_t3_in += MM_in[0]

	t18_t3_mem0 = S.Task('t18_t3_mem0', length=1, delay_cost=1)
	S += t18_t3_mem0 >= 17
	t18_t3_mem0 += MAS_MEM[3]

	t18_t3_mem1 = S.Task('t18_t3_mem1', length=1, delay_cost=1)
	S += t18_t3_mem1 >= 17
	t18_t3_mem1 += MAS_MEM[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 17
	t1_t1_mem0 += MAIN_MEM_r

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 17
	t1_t1_mem1 += MAIN_MEM_r

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 17
	t2_t2 += MAS[2]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 17
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 17
	t51_mem1 += MAS_MEM[2]

	t12_t2_mem0 = S.Task('t12_t2_mem0', length=1, delay_cost=1)
	S += t12_t2_mem0 >= 18
	t12_t2_mem0 += MAS_MEM[3]

	t12_t2_mem1 = S.Task('t12_t2_mem1', length=1, delay_cost=1)
	S += t12_t2_mem1 >= 18
	t12_t2_mem1 += MAS_MEM[0]

	t18_t0 = S.Task('t18_t0', length=1, delay_cost=1)
	S += t18_t0 >= 18
	t18_t0 += MAS[3]

	t18_t3 = S.Task('t18_t3', length=5, delay_cost=1)
	S += t18_t3 >= 18
	t18_t3 += MM[0]

	t1_t1 = S.Task('t1_t1', length=1, delay_cost=1)
	S += t1_t1 >= 18
	t1_t1 += MAS[2]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 18
	t1_t2_in += MM_in[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 18
	t1_t2_mem0 += MAS_MEM[3]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 18
	t1_t2_mem1 += MAS_MEM[2]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 18
	t51 += MAS[1]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 18
	t61_mem0 += MAS_MEM[1]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 18
	t61_mem1 += MAS_MEM[1]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 18
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 18
	t70_mem1 += MAS_MEM[2]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 19
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 19
	c201_mem0 += MAS_MEM[3]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 19
	c201_mem1 += MAIN_MEM_r

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 19
	new_TX_t3_mem0 += MAS_MEM[0]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 19
	new_TX_t3_mem1 += MAS_MEM[1]

	t12_t2 = S.Task('t12_t2', length=1, delay_cost=1)
	S += t12_t2 >= 19
	t12_t2 += MAS[3]

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	S += t18_t1_mem0 >= 19
	t18_t1_mem0 += MAS_MEM[3]

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	S += t18_t1_mem1 >= 19
	t18_t1_mem1 += MAS_MEM[0]

	t1_t2 = S.Task('t1_t2', length=5, delay_cost=1)
	S += t1_t2 >= 19
	t1_t2 += MM[0]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 19
	t61 += MAS[1]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 19
	t70 += MAS[2]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 19
	t80_mem0 += MAS_MEM[2]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 19
	t80_mem1 += MAS_MEM[2]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 20
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 20
	c010_mem0 += MAS_MEM[1]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 20
	c010_mem1 += MAIN_MEM_r

	c201 = S.Task('c201', length=5, delay_cost=1)
	S += c201 >= 20
	c201 += MM[0]

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	S += new_TX_t3 >= 20
	new_TX_t3 += MAS[3]

	t18_t1 = S.Task('t18_t1', length=1, delay_cost=1)
	S += t18_t1 >= 20
	t18_t1 += MAS[0]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 20
	t80 += MAS[1]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 20
	t90_mem0 += MAS_MEM[1]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 20
	t90_mem1 += MAS_MEM[2]

	c010 = S.Task('c010', length=5, delay_cost=1)
	S += c010 >= 21
	c010 += MM[0]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 21
	t101_mem0 += MM_MEM[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 21
	t101_mem1 += MAS_MEM[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 21
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 21
	t2_t1_mem0 += MAIN_MEM_r

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 21
	t2_t1_mem1 += MAS_MEM[2]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 21
	t90 += MAS[3]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 22
	t101 += MAS[0]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 22
	t111_mem0 += MAS_MEM[0]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 22
	t111_mem1 += MAS_MEM[0]

	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	S += t12_t0_in >= 22
	t12_t0_in += MM_in[0]

	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	S += t12_t0_mem0 >= 22
	t12_t0_mem0 += MAS_MEM[3]

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	S += t12_t0_mem1 >= 22
	t12_t0_mem1 += MAS_MEM[1]

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	S += t18_t5_mem0 >= 22
	t18_t5_mem0 += MM_MEM[0]

	t18_t5_mem1 = S.Task('t18_t5_mem1', length=1, delay_cost=1)
	S += t18_t5_mem1 >= 22
	t18_t5_mem1 += MM_MEM[0]

	t2_t1 = S.Task('t2_t1', length=5, delay_cost=1)
	S += t2_t1 >= 22
	t2_t1 += MM[0]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 23
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 23
	c011_mem0 += MAS_MEM[3]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 23
	c011_mem1 += MAIN_MEM_r

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 23
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 23
	t10_mem1 += MAS_MEM[2]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 23
	t111 += MAS[3]

	t12_t0 = S.Task('t12_t0', length=5, delay_cost=1)
	S += t12_t0 >= 23
	t12_t0 += MM[0]

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	S += t12_t3_mem0 >= 23
	t12_t3_mem0 += MAS_MEM[1]

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	S += t12_t3_mem1 >= 23
	t12_t3_mem1 += MAS_MEM[3]

	t18_t5 = S.Task('t18_t5', length=1, delay_cost=1)
	S += t18_t5 >= 23
	t18_t5 += MAS[0]

	c011 = S.Task('c011', length=5, delay_cost=1)
	S += c011 >= 24
	c011 += MM[0]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 24
	t10 += MAS[0]

	t12_t3 = S.Task('t12_t3', length=1, delay_cost=1)
	S += t12_t3 >= 24
	t12_t3 += MAS[3]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 24
	t181_mem0 += MM_MEM[0]

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	S += t181_mem1 >= 24
	t181_mem1 += MM_MEM[0]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 24
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 24
	t2_t0_mem0 += MAIN_MEM_r

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 24
	t2_t0_mem1 += MAS_MEM[0]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 24
	t2_t3_mem0 += MAS_MEM[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 24
	t2_t3_mem1 += MAS_MEM[2]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 25
	c201_w += MAIN_MEM_w

	t181 = S.Task('t181', length=1, delay_cost=1)
	S += t181 >= 25
	t181 += MAS[3]

	t2_t0 = S.Task('t2_t0', length=5, delay_cost=1)
	S += t2_t0 >= 25
	t2_t0 += MM[0]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 25
	t2_t3 += MAS[2]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 25
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 25
	t2_t4_mem0 += MAS_MEM[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 25
	t2_t4_mem1 += MAS_MEM[2]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 26
	c010_w += MAIN_MEM_w

	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	S += t18_t2_in >= 26
	t18_t2_in += MM_in[0]

	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	S += t18_t2_mem0 >= 26
	t18_t2_mem0 += MAS_MEM[3]

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	S += t18_t2_mem1 >= 26
	t18_t2_mem1 += MAS_MEM[0]

	t2_t4 = S.Task('t2_t4', length=5, delay_cost=1)
	S += t2_t4 >= 26
	t2_t4 += MM[0]

	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	S += t12_t1_in >= 27
	t12_t1_in += MM_in[0]

	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	S += t12_t1_mem0 >= 27
	t12_t1_mem0 += MAS_MEM[0]

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	S += t12_t1_mem1 >= 27
	t12_t1_mem1 += MAS_MEM[3]

	t18_t2 = S.Task('t18_t2', length=5, delay_cost=1)
	S += t18_t2 >= 27
	t18_t2 += MM[0]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 28
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 28
	c200_mem0 += MAS_MEM[3]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 28
	c200_mem1 += MAIN_MEM_r

	t12_t1 = S.Task('t12_t1', length=5, delay_cost=1)
	S += t12_t1 >= 28
	t12_t1 += MM[0]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 29
	c011_w += MAIN_MEM_w

	c200 = S.Task('c200', length=5, delay_cost=1)
	S += c200 >= 29
	c200 += MM[0]

	t12_t4_in = S.Task('t12_t4_in', length=1, delay_cost=1)
	S += t12_t4_in >= 29
	t12_t4_in += MM_in[0]

	t12_t4_mem0 = S.Task('t12_t4_mem0', length=1, delay_cost=1)
	S += t12_t4_mem0 >= 29
	t12_t4_mem0 += MAS_MEM[3]

	t12_t4_mem1 = S.Task('t12_t4_mem1', length=1, delay_cost=1)
	S += t12_t4_mem1 >= 29
	t12_t4_mem1 += MAS_MEM[3]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 29
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 29
	t2_t5_mem1 += MM_MEM[0]

	t12_t4 = S.Task('t12_t4', length=5, delay_cost=1)
	S += t12_t4 >= 30
	t12_t4 += MM[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 30
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 30
	t20_mem1 += MM_MEM[0]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 30
	t2_t5 += MAS[3]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 31
	t180_mem0 += MM_MEM[0]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 31
	t180_mem1 += MAS_MEM[0]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 31
	t20 += MAS[3]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 31
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 31
	t21_mem1 += MAS_MEM[3]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 32
	t120_mem0 += MM_MEM[0]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 32
	t120_mem1 += MM_MEM[0]

	t180 = S.Task('t180', length=1, delay_cost=1)
	S += t180 >= 32
	t180 += MAS[3]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 32
	t21 += MAS[2]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 32
	t30_mem0 += MAS_MEM[3]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 32
	t30_mem1 += MAS_MEM[3]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 32
	t31_mem0 += MAS_MEM[2]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 32
	t31_mem1 += MAS_MEM[2]

	t120 = S.Task('t120', length=1, delay_cost=1)
	S += t120 >= 33
	t120 += MAS[0]

	t12_t5_mem0 = S.Task('t12_t5_mem0', length=1, delay_cost=1)
	S += t12_t5_mem0 >= 33
	t12_t5_mem0 += MM_MEM[0]

	t12_t5_mem1 = S.Task('t12_t5_mem1', length=1, delay_cost=1)
	S += t12_t5_mem1 >= 33
	t12_t5_mem1 += MM_MEM[0]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 33
	t130_mem0 += MAS_MEM[0]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 33
	t130_mem1 += MAS_MEM[0]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 33
	t30 += MAS[3]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 33
	t31 += MAS[1]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 33
	t40_mem0 += MAS_MEM[3]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 33
	t40_mem1 += MAS_MEM[3]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 33
	t41_mem0 += MAS_MEM[1]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 33
	t41_mem1 += MAS_MEM[2]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 34
	c200_w += MAIN_MEM_w

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 34
	new_TZ0_mem0 += MAS_MEM[1]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 34
	new_TZ0_mem1 += MAS_MEM[1]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 34
	t121_mem0 += MM_MEM[0]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 34
	t121_mem1 += MAS_MEM[3]

	t12_t5 = S.Task('t12_t5', length=1, delay_cost=1)
	S += t12_t5 >= 34
	t12_t5 += MAS[3]

	t130 = S.Task('t130', length=1, delay_cost=1)
	S += t130 >= 34
	t130 += MAS[1]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 34
	t140_mem0 += MAS_MEM[0]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 34
	t140_mem1 += MAS_MEM[0]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 34
	t141_mem0 += MAS_MEM[2]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 34
	t141_mem1 += MAS_MEM[2]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 34
	t40 += MAS[0]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 34
	t41 += MAS[2]

	b31_mem0 = S.Task('b31_mem0', length=1, delay_cost=1)
	S += b31_mem0 >= 35
	b31_mem0 += MAS_MEM[2]

	b31_mem1 = S.Task('b31_mem1', length=1, delay_cost=1)
	S += b31_mem1 >= 35
	b31_mem1 += MAS_MEM[2]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 35
	c000_mem0 += MAS_MEM[3]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 35
	c000_mem1 += MAS_MEM[0]

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	S += new_TZ0 >= 35
	new_TZ0 += MAS[0]

	t121 = S.Task('t121', length=1, delay_cost=1)
	S += t121 >= 35
	t121 += MAS[1]

	t140 = S.Task('t140', length=1, delay_cost=1)
	S += t140 >= 35
	t140 += MAS[3]

	t141 = S.Task('t141', length=1, delay_cost=1)
	S += t141 >= 35
	t141 += MAS[2]

	b31 = S.Task('b31', length=1, delay_cost=1)
	S += b31 >= 36
	b31 += MAS[0]

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 36
	c000 += MAS[1]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 36
	c001_mem0 += MAS_MEM[0]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 36
	c001_mem1 += MAS_MEM[2]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 36
	new_TZ0_w += MAIN_MEM_w

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 36
	t150_mem0 += MAS_MEM[1]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 36
	t150_mem1 += MAS_MEM[3]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 36
	t160_mem0 += MAS_MEM[3]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 36
	t160_mem1 += MAS_MEM[1]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 36
	t17_t2_mem0 += MAS_MEM[2]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 36
	t17_t2_mem1 += MAS_MEM[0]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 37
	c000_w += MAIN_MEM_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 37
	c001 += MAS[1]

	t150 = S.Task('t150', length=1, delay_cost=1)
	S += t150 >= 37
	t150 += MAS[2]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 37
	t151_mem0 += MAS_MEM[1]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 37
	t151_mem1 += MAS_MEM[2]

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 37
	t160 += MAS[0]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 37
	t161_mem0 += MAS_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 37
	t161_mem1 += MAS_MEM[1]

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	S += t17_t2 >= 37
	t17_t2 += MAS[3]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 38
	c001_w += MAIN_MEM_w

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 38
	new_TX_t2_mem0 += MAS_MEM[2]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 38
	new_TX_t2_mem1 += MAS_MEM[2]

	t151 = S.Task('t151', length=1, delay_cost=1)
	S += t151 >= 38
	t151 += MAS[2]

	t161 = S.Task('t161', length=1, delay_cost=1)
	S += t161 >= 38
	t161 += MAS[1]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 38
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 38
	t17_t1_mem0 += MAS_MEM[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 38
	t17_t1_mem1 += MAS_MEM[1]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 38
	t17_t3_mem0 += MAS_MEM[0]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 38
	t17_t3_mem1 += MAS_MEM[1]

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	S += new_TX_t2 >= 39
	new_TX_t2 += MAS[0]

	t17_t1 = S.Task('t17_t1', length=5, delay_cost=1)
	S += t17_t1 >= 39
	t17_t1 += MM[0]

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	S += t17_t3 >= 39
	t17_t3 += MAS[1]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 39
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 39
	t17_t4_mem0 += MAS_MEM[3]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 39
	t17_t4_mem1 += MAS_MEM[1]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 40
	new_TX_t1_in += MM_in[0]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 40
	new_TX_t1_mem0 += MAS_MEM[2]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 40
	new_TX_t1_mem1 += MAS_MEM[1]

	t17_t4 = S.Task('t17_t4', length=5, delay_cost=1)
	S += t17_t4 >= 40
	t17_t4 += MM[0]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 41
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 41
	new_TX_t0_mem0 += MAS_MEM[2]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 41
	new_TX_t0_mem1 += MAS_MEM[0]

	new_TX_t1 = S.Task('new_TX_t1', length=5, delay_cost=1)
	S += new_TX_t1 >= 41
	new_TX_t1 += MM[0]

	new_TX_t0 = S.Task('new_TX_t0', length=5, delay_cost=1)
	S += new_TX_t0 >= 42
	new_TX_t0 += MM[0]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 42
	new_TX_t4_in += MM_in[0]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 42
	new_TX_t4_mem0 += MAS_MEM[0]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 42
	new_TX_t4_mem1 += MAS_MEM[3]

	new_TX_t4 = S.Task('new_TX_t4', length=5, delay_cost=1)
	S += new_TX_t4 >= 43
	new_TX_t4 += MM[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 43
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 43
	t170_mem1 += MM_MEM[0]

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	S += new_TY0_mem0 >= 44
	new_TY0_mem0 += MAS_MEM[1]

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	S += new_TY0_mem1 >= 44
	new_TY0_mem1 += MAS_MEM[3]

	t170 = S.Task('t170', length=1, delay_cost=1)
	S += t170 >= 44
	t170 += MAS[1]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 44
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 44
	t17_t5_mem1 += MM_MEM[0]

	new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
	S += new_TY0 >= 45
	new_TY0 += MAS[3]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 45
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 45
	t171_mem1 += MAS_MEM[1]

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	S += t17_t5 >= 45
	t17_t5 += MAS[1]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 46
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 46
	new_TX_t5_mem1 += MM_MEM[0]

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	S += new_TY0_w >= 46
	new_TY0_w += MAIN_MEM_w

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	S += new_TY1_mem0 >= 46
	new_TY1_mem0 += MAS_MEM[0]

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	S += new_TY1_mem1 >= 46
	new_TY1_mem1 += MAS_MEM[3]

	t171 = S.Task('t171', length=1, delay_cost=1)
	S += t171 >= 46
	t171 += MAS[0]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 47
	new_TX1_mem0 += MM_MEM[0]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 47
	new_TX1_mem1 += MAS_MEM[0]

	new_TX_t5 = S.Task('new_TX_t5', length=1, delay_cost=1)
	S += new_TX_t5 >= 47
	new_TX_t5 += MAS[0]

	new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
	S += new_TY1 >= 47
	new_TY1 += MAS[2]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 48
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 48
	new_TX0_mem1 += MM_MEM[0]

	new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
	S += new_TX1 >= 48
	new_TX1 += MAS[0]

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	S += new_TY1_w >= 48
	new_TY1_w += MAIN_MEM_w

	new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
	S += new_TX0 >= 49
	new_TX0 += MAS[3]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 49
	new_TX1_w += MAIN_MEM_w

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 50
	new_TX0_w += MAIN_MEM_w


	# new tasks
	t131 = S.Task('t131', length=1, delay_cost=1)
	t131 += alt(MAS)

	S += t131<38

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += MAS_MEM[1]
	S += 35 < t131_mem0
	S += t131_mem0 <= t131

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	t131_mem1 += MAS_MEM[1]
	S += 35 < t131_mem1
	S += t131_mem1 <= t131

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	new_TZ1 += alt(MAS)

	S += 18<new_TZ1

	S += new_TZ1<1000

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	new_TZ1_mem0 += alt(MAS_MEM)
	S += (t131*MAS[0])-1 < new_TZ1_mem0*MAS_MEM[0]
	S += (t131*MAS[1])-1 < new_TZ1_mem0*MAS_MEM[1]
	S += (t131*MAS[2])-1 < new_TZ1_mem0*MAS_MEM[2]
	S += (t131*MAS[3])-1 < new_TZ1_mem0*MAS_MEM[3]
	S += new_TZ1_mem0 <= new_TZ1

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	new_TZ1_mem1 += alt(MAS_MEM)
	S += (t131*MAS[0])-1 < new_TZ1_mem1*MAS_MEM[0]
	S += (t131*MAS[1])-1 < new_TZ1_mem1*MAS_MEM[1]
	S += (t131*MAS[2])-1 < new_TZ1_mem1*MAS_MEM[2]
	S += (t131*MAS[3])-1 < new_TZ1_mem1*MAS_MEM[3]
	S += new_TZ1_mem1 <= new_TZ1

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	new_TZ1_w += alt(MAIN_MEM_w)
	S += new_TZ1 <= new_TZ1_w

	b30 = S.Task('b30', length=1, delay_cost=1)
	b30 += alt(MAS)

	S += b30<37

	b30_mem0 = S.Task('b30_mem0', length=1, delay_cost=1)
	b30_mem0 += MAS_MEM[3]
	S += 35 < b30_mem0
	S += b30_mem0 <= b30

	b30_mem1 = S.Task('b30_mem1', length=1, delay_cost=1)
	b30_mem1 += MAS_MEM[0]
	S += 34 < b30_mem1
	S += b30_mem1 <= b30

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	t17_t0_in += alt(MM_in)
	t17_t0 = S.Task('t17_t0', length=5, delay_cost=1)
	t17_t0 += alt(MM)
	S += t17_t0>=t17_t0_in

	S += t17_t0<44

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	t17_t0_mem0 += alt(MAS_MEM)
	S += (b30*MAS[0])-1 < t17_t0_mem0*MAS_MEM[0]
	S += (b30*MAS[1])-1 < t17_t0_mem0*MAS_MEM[1]
	S += (b30*MAS[2])-1 < t17_t0_mem0*MAS_MEM[2]
	S += (b30*MAS[3])-1 < t17_t0_mem0*MAS_MEM[3]
	S += t17_t0_mem0 <= t17_t0

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	t17_t0_mem1 += MAS_MEM[0]
	S += 37 < t17_t0_mem1
	S += t17_t0_mem1 <= t17_t0

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/PDBL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

