from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 139
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 0
	t7_t3_in += MM_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 0
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 0
	t7_t3_mem1 += MAIN_MEM_r[1]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 1
	t1_t3_in += MM_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 1
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 1
	t1_t3_mem1 += MAIN_MEM_r[1]

	t7_t3 = S.Task('t7_t3', length=5, delay_cost=1)
	S += t7_t3 >= 1
	t7_t3 += MM[0]

	t1_t3 = S.Task('t1_t3', length=5, delay_cost=1)
	S += t1_t3 >= 2
	t1_t3 += MM[0]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 2
	t5_t0_in += MM_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 2
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 2
	t5_t0_mem1 += MAIN_MEM_r[1]

	t5_t0 = S.Task('t5_t0', length=5, delay_cost=1)
	S += t5_t0 >= 3
	t5_t0 += MM[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 3
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 3
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 3
	t5_t1_mem1 += MAIN_MEM_r[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 4
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 4
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 4
	t0_t3_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=5, delay_cost=1)
	S += t5_t1 >= 4
	t5_t1 += MM[0]

	t0_t3 = S.Task('t0_t3', length=5, delay_cost=1)
	S += t0_t3 >= 5
	t0_t3 += MM[0]

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 5
	t10_t0_in += MM_in[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 5
	t10_t0_mem0 += MAIN_MEM_r[0]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 5
	t10_t0_mem1 += MAIN_MEM_r[1]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 5
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 5
	t71_mem1 += MM_MEM[1]

	t10_t0 = S.Task('t10_t0', length=5, delay_cost=1)
	S += t10_t0 >= 6
	t10_t0 += MM[0]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 6
	t10_t1_in += MM_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 6
	t10_t1_mem0 += MAIN_MEM_r[0]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 6
	t10_t1_mem1 += MAIN_MEM_r[1]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 6
	t71 += MAS[4]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 6
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 6
	t7_t5_mem1 += MM_MEM[1]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 6
	t81_mem0 += MAS_MEM[8]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 6
	t81_mem1 += MAS_MEM[9]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 7
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 7
	t0_t0_mem1 += MAIN_MEM_r[1]

	t10_t1 = S.Task('t10_t1', length=5, delay_cost=1)
	S += t10_t1 >= 7
	t10_t1 += MM[0]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 7
	t1_t5_mem0 += MM_MEM[0]

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	S += t1_t5_mem1 >= 7
	t1_t5_mem1 += MM_MEM[1]

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 7
	t7_t5 += MAS[4]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 7
	t81 += MAS[2]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 7
	t91_mem0 += MAS_MEM[4]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 7
	t91_mem1 += MAS_MEM[9]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 8
	t0_t0 += MAS[2]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 8
	t10_t2_mem0 += MAIN_MEM_r[0]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 8
	t10_t2_mem1 += MAIN_MEM_r[1]

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	S += t1_t5 >= 8
	t1_t5 += MAS[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 8
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 8
	t50_mem1 += MM_MEM[1]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 8
	t91 += MAS[4]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 9
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 9
	t01_mem1 += MM_MEM[1]

	t10_t2 = S.Task('t10_t2', length=1, delay_cost=1)
	S += t10_t2 >= 9
	t10_t2 += MAS[1]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 9
	t10_t3_mem0 += MAIN_MEM_r[0]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 9
	t10_t3_mem1 += MAIN_MEM_r[1]

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 9
	t50 += MAS[3]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 9
	t60_mem0 += MAS_MEM[6]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 9
	t60_mem1 += MAS_MEM[7]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 10
	t01 += MAS[1]

	t10_t3 = S.Task('t10_t3', length=1, delay_cost=1)
	S += t10_t3 >= 10
	t10_t3 += MAS[3]

	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	S += t10_t4_in >= 10
	t10_t4_in += MM_in[0]

	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	S += t10_t4_mem0 >= 10
	t10_t4_mem0 += MAS_MEM[2]

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	S += t10_t4_mem1 >= 10
	t10_t4_mem1 += MAS_MEM[7]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 10
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 10
	t2_t2_mem1 += MAIN_MEM_r[1]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 10
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 10
	t5_t5_mem1 += MM_MEM[1]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 10
	t60 += MAS[4]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 11
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 11
	t0_t1_mem1 += MAIN_MEM_r[1]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 11
	t100_mem0 += MM_MEM[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 11
	t100_mem1 += MM_MEM[1]

	t10_t4 = S.Task('t10_t4', length=5, delay_cost=1)
	S += t10_t4 >= 11
	t10_t4 += MM[0]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 11
	t2_t2 += MAS[2]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 11
	t5_t5 += MAS[3]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 12
	t0_t1 += MAS[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 12
	t0_t2_in += MM_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 12
	t0_t2_mem0 += MAS_MEM[4]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 12
	t0_t2_mem1 += MAS_MEM[3]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 12
	t100 += MAS[3]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 12
	t10_t5_mem0 += MM_MEM[0]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 12
	t10_t5_mem1 += MM_MEM[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 12
	t110_mem0 += MAS_MEM[6]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 12
	t110_mem1 += MAS_MEM[7]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 12
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 12
	t1_t1_mem1 += MAIN_MEM_r[1]

	t0_t2 = S.Task('t0_t2', length=5, delay_cost=1)
	S += t0_t2 >= 13
	t0_t2 += MM[0]

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	S += t10_t5 >= 13
	t10_t5 += MAS[3]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 13
	t110 += MAS[2]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 13
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 13
	t11_mem1 += MM_MEM[1]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 13
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 13
	t1_t0_mem1 += MAIN_MEM_r[1]

	t1_t1 = S.Task('t1_t1', length=1, delay_cost=1)
	S += t1_t1 >= 13
	t1_t1 += MAS[4]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 14
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 14
	t0_t5_mem1 += MM_MEM[1]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 14
	t11 += MAS[2]

	t1_t0 = S.Task('t1_t0', length=1, delay_cost=1)
	S += t1_t0 >= 14
	t1_t0 += MAS[0]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 14
	t1_t2_in += MM_in[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 14
	t1_t2_mem0 += MAS_MEM[0]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 14
	t1_t2_mem1 += MAS_MEM[9]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 14
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 14
	t7_t1_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 15
	t0_t5 += MAS[0]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 15
	t101_mem0 += MM_MEM[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 15
	t101_mem1 += MAS_MEM[7]

	t1_t2 = S.Task('t1_t2', length=5, delay_cost=1)
	S += t1_t2 >= 15
	t1_t2 += MM[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 15
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 15
	t7_t0_mem1 += MAIN_MEM_r[1]

	t7_t1 = S.Task('t7_t1', length=1, delay_cost=1)
	S += t7_t1 >= 15
	t7_t1 += MAS[4]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 16
	t101 += MAS[2]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 16
	t111_mem0 += MAS_MEM[4]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 16
	t111_mem1 += MAS_MEM[5]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 16
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 16
	t5_t3_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=1, delay_cost=1)
	S += t7_t0 >= 16
	t7_t0 += MAS[3]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 16
	t7_t2_in += MM_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 16
	t7_t2_mem0 += MAS_MEM[6]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 16
	t7_t2_mem1 += MAS_MEM[9]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 17
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 17
	t00_mem1 += MAS_MEM[1]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 17
	t111 += MAS[3]

	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	S += t12_t1_in >= 17
	t12_t1_in += MM_in[0]

	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	S += t12_t1_mem0 >= 17
	t12_t1_mem0 += MAS_MEM[2]

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	S += t12_t1_mem1 >= 17
	t12_t1_mem1 += MAS_MEM[7]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 17
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 17
	t5_t2_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 17
	t5_t3 += MAS[0]

	t7_t2 = S.Task('t7_t2', length=5, delay_cost=1)
	S += t7_t2 >= 17
	t7_t2 += MM[0]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 18
	t00 += MAS[1]

	t12_t1 = S.Task('t12_t1', length=5, delay_cost=1)
	S += t12_t1 >= 18
	t12_t1 += MM[0]

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	S += t12_t3_mem0 >= 18
	t12_t3_mem0 += MAS_MEM[4]

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	S += t12_t3_mem1 >= 18
	t12_t3_mem1 += MAS_MEM[7]

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	S += t18_t1_mem0 >= 18
	t18_t1_mem0 += MAS_MEM[2]

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	S += t18_t1_mem1 >= 18
	t18_t1_mem1 += MAS_MEM[3]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 18
	t5_t2 += MAS[3]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 18
	t5_t4_in += MM_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 18
	t5_t4_mem0 += MAS_MEM[6]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 18
	t5_t4_mem1 += MAS_MEM[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 19
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 19
	t10_mem1 += MAS_MEM[1]

	t12_t3 = S.Task('t12_t3', length=1, delay_cost=1)
	S += t12_t3 >= 19
	t12_t3 += MAS[3]

	t18_t1 = S.Task('t18_t1', length=1, delay_cost=1)
	S += t18_t1 >= 19
	t18_t1 += MAS[2]

	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	S += t18_t3_in >= 19
	t18_t3_in += MM_in[0]

	t18_t3_mem0 = S.Task('t18_t3_mem0', length=1, delay_cost=1)
	S += t18_t3_mem0 >= 19
	t18_t3_mem0 += MAS_MEM[2]

	t18_t3_mem1 = S.Task('t18_t3_mem1', length=1, delay_cost=1)
	S += t18_t3_mem1 >= 19
	t18_t3_mem1 += MAS_MEM[3]

	t5_t4 = S.Task('t5_t4', length=5, delay_cost=1)
	S += t5_t4 >= 19
	t5_t4 += MM[0]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 20
	t10 += MAS[0]

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	S += t18_t0_mem0 >= 20
	t18_t0_mem0 += MAS_MEM[2]

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	S += t18_t0_mem1 >= 20
	t18_t0_mem1 += MAS_MEM[3]

	t18_t3 = S.Task('t18_t3', length=5, delay_cost=1)
	S += t18_t3 >= 20
	t18_t3 += MM[0]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 20
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 20
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 20
	t2_t0_mem1 += MAS_MEM[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 20
	t2_t3_mem0 += MAS_MEM[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 20
	t2_t3_mem1 += MAS_MEM[5]

	t12_t2_mem0 = S.Task('t12_t2_mem0', length=1, delay_cost=1)
	S += t12_t2_mem0 >= 21
	t12_t2_mem0 += MAS_MEM[2]

	t12_t2_mem1 = S.Task('t12_t2_mem1', length=1, delay_cost=1)
	S += t12_t2_mem1 >= 21
	t12_t2_mem1 += MAS_MEM[3]

	t18_t0 = S.Task('t18_t0', length=1, delay_cost=1)
	S += t18_t0 >= 21
	t18_t0 += MAS[1]

	t2_t0 = S.Task('t2_t0', length=5, delay_cost=1)
	S += t2_t0 >= 21
	t2_t0 += MM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 21
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 21
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 21
	t2_t1_mem1 += MAS_MEM[5]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 21
	t2_t3 += MAS[2]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 21
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 21
	t70_mem1 += MAS_MEM[9]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 22
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 22
	c010_mem0 += MAS_MEM[4]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 22
	c010_mem1 += MAIN_MEM_r[1]

	t12_t2 = S.Task('t12_t2', length=1, delay_cost=1)
	S += t12_t2 >= 22
	t12_t2 += MAS[4]

	t2_t1 = S.Task('t2_t1', length=5, delay_cost=1)
	S += t2_t1 >= 22
	t2_t1 += MM[0]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 22
	t70 += MAS[1]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 22
	t80_mem0 += MAS_MEM[2]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 22
	t80_mem1 += MAS_MEM[3]

	c010 = S.Task('c010', length=5, delay_cost=1)
	S += c010 >= 23
	c010 += MM[0]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 23
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 23
	c011_mem0 += MAS_MEM[6]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 23
	c011_mem1 += MAIN_MEM_r[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 23
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 23
	t51_mem1 += MAS_MEM[7]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 23
	t80 += MAS[2]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 23
	t90_mem0 += MAS_MEM[4]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 23
	t90_mem1 += MAS_MEM[3]

	c011 = S.Task('c011', length=5, delay_cost=1)
	S += c011 >= 24
	c011 += MM[0]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 24
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 24
	c201_mem0 += MAS_MEM[8]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 24
	c201_mem1 += MAIN_MEM_r[1]

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	S += t18_t5_mem0 >= 24
	t18_t5_mem0 += MM_MEM[0]

	t18_t5_mem1 = S.Task('t18_t5_mem1', length=1, delay_cost=1)
	S += t18_t5_mem1 >= 24
	t18_t5_mem1 += MM_MEM[1]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 24
	t51 += MAS[2]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 24
	t61_mem0 += MAS_MEM[4]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 24
	t61_mem1 += MAS_MEM[5]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 24
	t90 += MAS[3]

	c201 = S.Task('c201', length=5, delay_cost=1)
	S += c201 >= 25
	c201 += MM[0]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 25
	new_TX_t3_mem0 += MAS_MEM[8]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 25
	new_TX_t3_mem1 += MAS_MEM[7]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 25
	t181_mem0 += MM_MEM[0]

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	S += t181_mem1 >= 25
	t181_mem1 += MM_MEM[1]

	t18_t5 = S.Task('t18_t5', length=1, delay_cost=1)
	S += t18_t5 >= 25
	t18_t5 += MAS[2]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 25
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 25
	t2_t4_mem0 += MAS_MEM[4]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 25
	t2_t4_mem1 += MAS_MEM[5]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 25
	t61 += MAS[3]

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	S += new_TX_t3 >= 26
	new_TX_t3 += MAS[2]

	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	S += t12_t0_in >= 26
	t12_t0_in += MM_in[0]

	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	S += t12_t0_mem0 >= 26
	t12_t0_mem0 += MAS_MEM[2]

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	S += t12_t0_mem1 >= 26
	t12_t0_mem1 += MAS_MEM[5]

	t181 = S.Task('t181', length=1, delay_cost=1)
	S += t181 >= 26
	t181 += MAS[3]

	t2_t4 = S.Task('t2_t4', length=5, delay_cost=1)
	S += t2_t4 >= 26
	t2_t4 += MM[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 26
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 26
	t2_t5_mem1 += MM_MEM[1]

	t12_t0 = S.Task('t12_t0', length=5, delay_cost=1)
	S += t12_t0 >= 27
	t12_t0 += MM[0]

	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	S += t18_t2_in >= 27
	t18_t2_in += MM_in[0]

	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	S += t18_t2_mem0 >= 27
	t18_t2_mem0 += MAS_MEM[2]

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	S += t18_t2_mem1 >= 27
	t18_t2_mem1 += MAS_MEM[5]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 27
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 27
	t20_mem1 += MM_MEM[1]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 27
	t2_t5 += MAS[2]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 28
	c010_w += MAIN_MEM_w

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 28
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 28
	c200_mem0 += MAS_MEM[6]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 28
	c200_mem1 += MAIN_MEM_r[1]

	t18_t2 = S.Task('t18_t2', length=5, delay_cost=1)
	S += t18_t2 >= 28
	t18_t2 += MM[0]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 28
	t20 += MAS[4]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 28
	t30_mem0 += MAS_MEM[8]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 28
	t30_mem1 += MAS_MEM[9]

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
	t12_t4_mem0 += MAS_MEM[8]

	t12_t4_mem1 = S.Task('t12_t4_mem1', length=1, delay_cost=1)
	S += t12_t4_mem1 >= 29
	t12_t4_mem1 += MAS_MEM[7]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 29
	t30 += MAS[1]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 29
	t40_mem0 += MAS_MEM[2]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 29
	t40_mem1 += MAS_MEM[9]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 30
	c000_mem0 += MAS_MEM[2]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 30
	c000_mem1 += MAS_MEM[7]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 30
	c201_w += MAIN_MEM_w

	t12_t4 = S.Task('t12_t4', length=5, delay_cost=1)
	S += t12_t4 >= 30
	t12_t4 += MM[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 30
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 30
	t21_mem1 += MAS_MEM[5]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 30
	t40 += MAS[3]

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 31
	c000 += MAS[1]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 31
	t120_mem0 += MM_MEM[0]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 31
	t120_mem1 += MM_MEM[1]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 31
	t140_mem0 += MAS_MEM[6]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 31
	t140_mem1 += MAS_MEM[7]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 31
	t160_mem0 += MAS_MEM[2]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 31
	t160_mem1 += MAS_MEM[3]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 31
	t21 += MAS[4]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 31
	t31_mem0 += MAS_MEM[8]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 31
	t31_mem1 += MAS_MEM[9]

	b30_mem0 = S.Task('b30_mem0', length=1, delay_cost=1)
	S += b30_mem0 >= 32
	b30_mem0 += MAS_MEM[4]

	b30_mem1 = S.Task('b30_mem1', length=1, delay_cost=1)
	S += b30_mem1 >= 32
	b30_mem1 += MAS_MEM[7]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 32
	c000_w += MAIN_MEM_w

	t120 = S.Task('t120', length=1, delay_cost=1)
	S += t120 >= 32
	t120 += MAS[0]

	t12_t5_mem0 = S.Task('t12_t5_mem0', length=1, delay_cost=1)
	S += t12_t5_mem0 >= 32
	t12_t5_mem0 += MM_MEM[0]

	t12_t5_mem1 = S.Task('t12_t5_mem1', length=1, delay_cost=1)
	S += t12_t5_mem1 >= 32
	t12_t5_mem1 += MM_MEM[1]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 32
	t130_mem0 += MAS_MEM[0]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 32
	t130_mem1 += MAS_MEM[1]

	t140 = S.Task('t140', length=1, delay_cost=1)
	S += t140 >= 32
	t140 += MAS[2]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 32
	t150_mem0 += MAS_MEM[2]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 32
	t150_mem1 += MAS_MEM[5]

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 32
	t160 += MAS[4]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 32
	t31 += MAS[3]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 32
	t41_mem0 += MAS_MEM[6]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 32
	t41_mem1 += MAS_MEM[9]

	b30 = S.Task('b30', length=1, delay_cost=1)
	S += b30 >= 33
	b30 += MAS[4]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 33
	c001_mem0 += MAS_MEM[2]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 33
	c001_mem1 += MAS_MEM[1]

	t12_t5 = S.Task('t12_t5', length=1, delay_cost=1)
	S += t12_t5 >= 33
	t12_t5 += MAS[1]

	t130 = S.Task('t130', length=1, delay_cost=1)
	S += t130 >= 33
	t130 += MAS[2]

	t150 = S.Task('t150', length=1, delay_cost=1)
	S += t150 >= 33
	t150 += MAS[3]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 33
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 33
	t17_t0_mem0 += MAS_MEM[8]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 33
	t17_t0_mem1 += MAS_MEM[9]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 33
	t180_mem0 += MM_MEM[0]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 33
	t180_mem1 += MAS_MEM[5]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 33
	t41 += MAS[0]

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 34
	c001 += MAS[3]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 34
	c200_w += MAIN_MEM_w

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 34
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 34
	new_TX_t0_mem0 += MAS_MEM[6]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 34
	new_TX_t0_mem1 += MAS_MEM[9]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 34
	new_TZ0_mem0 += MAS_MEM[4]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 34
	new_TZ0_mem1 += MAS_MEM[5]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 34
	t121_mem0 += MM_MEM[0]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 34
	t121_mem1 += MAS_MEM[3]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 34
	t161_mem0 += MAS_MEM[2]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 34
	t161_mem1 += MAS_MEM[7]

	t17_t0 = S.Task('t17_t0', length=5, delay_cost=1)
	S += t17_t0 >= 34
	t17_t0 += MM[0]

	t180 = S.Task('t180', length=1, delay_cost=1)
	S += t180 >= 34
	t180 += MAS[2]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 35
	c001_w += MAIN_MEM_w

	new_TX_t0 = S.Task('new_TX_t0', length=5, delay_cost=1)
	S += new_TX_t0 >= 35
	new_TX_t0 += MM[0]

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	S += new_TZ0 >= 35
	new_TZ0 += MAS[0]

	t121 = S.Task('t121', length=1, delay_cost=1)
	S += t121 >= 35
	t121 += MAS[2]

	t161 = S.Task('t161', length=1, delay_cost=1)
	S += t161 >= 35
	t161 += MAS[4]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 35
	t17_t3_mem0 += MAS_MEM[8]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 35
	t17_t3_mem1 += MAS_MEM[9]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 36
	new_TX_t2_mem0 += MAS_MEM[6]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 36
	new_TX_t2_mem1 += MAS_MEM[5]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 36
	new_TZ0_w += MAIN_MEM_w

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 36
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 36
	t17_t1_mem0 += MAS_MEM[2]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 36
	t17_t1_mem1 += MAS_MEM[9]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 36
	t17_t2_mem0 += MAS_MEM[8]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 36
	t17_t2_mem1 += MAS_MEM[3]

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	S += t17_t3 >= 36
	t17_t3 += MAS[4]

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	S += new_TX_t2 >= 37
	new_TX_t2 += MAS[3]

	t17_t1 = S.Task('t17_t1', length=5, delay_cost=1)
	S += t17_t1 >= 37
	t17_t1 += MM[0]

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	S += t17_t2 >= 37
	t17_t2 += MAS[2]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 37
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 37
	t17_t4_mem0 += MAS_MEM[4]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 37
	t17_t4_mem1 += MAS_MEM[9]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 38
	new_TX_t1_in += MM_in[0]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 38
	new_TX_t1_mem0 += MAS_MEM[4]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 38
	new_TX_t1_mem1 += MAS_MEM[7]

	t17_t4 = S.Task('t17_t4', length=5, delay_cost=1)
	S += t17_t4 >= 38
	t17_t4 += MM[0]

	new_TX_t1 = S.Task('new_TX_t1', length=5, delay_cost=1)
	S += new_TX_t1 >= 39
	new_TX_t1 += MM[0]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 39
	new_TX_t4_in += MM_in[0]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 39
	new_TX_t4_mem0 += MAS_MEM[6]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 39
	new_TX_t4_mem1 += MAS_MEM[5]

	new_TX_t4 = S.Task('new_TX_t4', length=5, delay_cost=1)
	S += new_TX_t4 >= 40
	new_TX_t4 += MM[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 41
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 41
	t170_mem1 += MM_MEM[1]

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	S += new_TY0_mem0 >= 42
	new_TY0_mem0 += MAS_MEM[4]

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	S += new_TY0_mem1 >= 42
	new_TY0_mem1 += MAS_MEM[5]

	t170 = S.Task('t170', length=1, delay_cost=1)
	S += t170 >= 42
	t170 += MAS[2]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 42
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 42
	t17_t5_mem1 += MM_MEM[1]

	new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
	S += new_TY0 >= 43
	new_TY0 += MAS[3]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 43
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 43
	t171_mem1 += MAS_MEM[5]

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	S += t17_t5 >= 43
	t17_t5 += MAS[2]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 44
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 44
	new_TX_t5_mem1 += MM_MEM[1]

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	S += new_TY0_w >= 44
	new_TY0_w += MAIN_MEM_w

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	S += new_TY1_mem0 >= 44
	new_TY1_mem0 += MAS_MEM[6]

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	S += new_TY1_mem1 >= 44
	new_TY1_mem1 += MAS_MEM[7]

	t171 = S.Task('t171', length=1, delay_cost=1)
	S += t171 >= 44
	t171 += MAS[3]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 45
	new_TX1_mem0 += MM_MEM[0]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 45
	new_TX1_mem1 += MAS_MEM[1]

	new_TX_t5 = S.Task('new_TX_t5', length=1, delay_cost=1)
	S += new_TX_t5 >= 45
	new_TX_t5 += MAS[0]

	new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
	S += new_TY1 >= 45
	new_TY1 += MAS[4]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 46
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 46
	new_TX0_mem1 += MM_MEM[1]

	new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
	S += new_TX1 >= 46
	new_TX1 += MAS[3]

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	S += new_TY1_w >= 46
	new_TY1_w += MAIN_MEM_w

	new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
	S += new_TX0 >= 47
	new_TX0 += MAS[1]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 47
	new_TX1_w += MAIN_MEM_w

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 48
	new_TX0_w += MAIN_MEM_w


	# new tasks
	t131 = S.Task('t131', length=1, delay_cost=1)
	t131 += alt(MAS)

	S += t131<37

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += MAS_MEM[4]
	S += 35 < t131_mem0
	S += t131_mem0 <= t131

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	t131_mem1 += MAS_MEM[5]
	S += 35 < t131_mem1
	S += t131_mem1 <= t131

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	new_TZ1 += alt(MAS)

	S += 14<new_TZ1

	S += new_TZ1<1000

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	new_TZ1_mem0 += alt(MAS_MEM)
	S += (t131*MAS[0])-1 < new_TZ1_mem0*MAS_MEM[0]
	S += (t131*MAS[1])-1 < new_TZ1_mem0*MAS_MEM[2]
	S += (t131*MAS[2])-1 < new_TZ1_mem0*MAS_MEM[4]
	S += (t131*MAS[3])-1 < new_TZ1_mem0*MAS_MEM[6]
	S += (t131*MAS[4])-1 < new_TZ1_mem0*MAS_MEM[8]
	S += new_TZ1_mem0 <= new_TZ1

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	new_TZ1_mem1 += alt(MAS_MEM)
	S += (t131*MAS[0])-1 < new_TZ1_mem1*MAS_MEM[1]
	S += (t131*MAS[1])-1 < new_TZ1_mem1*MAS_MEM[3]
	S += (t131*MAS[2])-1 < new_TZ1_mem1*MAS_MEM[5]
	S += (t131*MAS[3])-1 < new_TZ1_mem1*MAS_MEM[7]
	S += (t131*MAS[4])-1 < new_TZ1_mem1*MAS_MEM[9]
	S += new_TZ1_mem1 <= new_TZ1

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	new_TZ1_w += alt(MAIN_MEM_w)
	S += new_TZ1 <= new_TZ1_w

	t141 = S.Task('t141', length=1, delay_cost=1)
	t141 += alt(MAS)

	S += t141<36

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += MAS_MEM[0]
	S += 33 < t141_mem0
	S += t141_mem0 <= t141

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	t141_mem1 += MAS_MEM[1]
	S += 33 < t141_mem1
	S += t141_mem1 <= t141

	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(MAS)

	S += t151<37

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[6]
	S += 34 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < t151_mem1*MAS_MEM[1]
	S += (t141*MAS[1])-1 < t151_mem1*MAS_MEM[3]
	S += (t141*MAS[2])-1 < t151_mem1*MAS_MEM[5]
	S += (t141*MAS[3])-1 < t151_mem1*MAS_MEM[7]
	S += (t141*MAS[4])-1 < t151_mem1*MAS_MEM[9]
	S += t151_mem1 <= t151

	b31 = S.Task('b31', length=1, delay_cost=1)
	b31 += alt(MAS)

	S += b31<37

	b31_mem0 = S.Task('b31_mem0', length=1, delay_cost=1)
	b31_mem0 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < b31_mem0*MAS_MEM[0]
	S += (t141*MAS[1])-1 < b31_mem0*MAS_MEM[2]
	S += (t141*MAS[2])-1 < b31_mem0*MAS_MEM[4]
	S += (t141*MAS[3])-1 < b31_mem0*MAS_MEM[6]
	S += (t141*MAS[4])-1 < b31_mem0*MAS_MEM[8]
	S += b31_mem0 <= b31

	b31_mem1 = S.Task('b31_mem1', length=1, delay_cost=1)
	b31_mem1 += MAS_MEM[1]
	S += 33 < b31_mem1
	S += b31_mem1 <= b31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS5/PDBL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

