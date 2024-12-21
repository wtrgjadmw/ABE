from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 130
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 0
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 0
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 0
	t5_t1_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=5, delay_cost=1)
	S += t5_t1 >= 1
	t5_t1 += MM[0]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 1
	t7_t3_in += MM_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 1
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 1
	t7_t3_mem1 += MAIN_MEM_r[1]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 2
	t10_t1_in += MM_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 2
	t10_t1_mem0 += MAIN_MEM_r[0]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 2
	t10_t1_mem1 += MAIN_MEM_r[1]

	t7_t3 = S.Task('t7_t3', length=5, delay_cost=1)
	S += t7_t3 >= 2
	t7_t3 += MM[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 3
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 3
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 3
	t0_t3_mem1 += MAIN_MEM_r[1]

	t10_t1 = S.Task('t10_t1', length=5, delay_cost=1)
	S += t10_t1 >= 3
	t10_t1 += MM[0]

	t0_t3 = S.Task('t0_t3', length=5, delay_cost=1)
	S += t0_t3 >= 4
	t0_t3 += MM[0]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 4
	t5_t0_in += MM_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 4
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 4
	t5_t0_mem1 += MAIN_MEM_r[1]

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 5
	t10_t0_in += MM_in[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 5
	t10_t0_mem0 += MAIN_MEM_r[0]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 5
	t10_t0_mem1 += MAIN_MEM_r[1]

	t5_t0 = S.Task('t5_t0', length=5, delay_cost=1)
	S += t5_t0 >= 5
	t5_t0 += MM[0]

	t10_t0 = S.Task('t10_t0', length=5, delay_cost=1)
	S += t10_t0 >= 6
	t10_t0 += MM[0]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 6
	t1_t3_in += MM_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 6
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 6
	t1_t3_mem1 += MAIN_MEM_r[1]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 6
	t71_mem0 += MM_MEM[0]

	t1_t3 = S.Task('t1_t3', length=5, delay_cost=1)
	S += t1_t3 >= 7
	t1_t3 += MM[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 7
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 7
	t5_t2_mem1 += MAIN_MEM_r[1]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 7
	t71 += MAS[0]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 7
	t7_t5_mem0 += MM_MEM[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 7
	t81_mem0 += MAS_MEM[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 8
	t0_t5_mem0 += MM_MEM[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 8
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 8
	t1_t1_mem1 += MAIN_MEM_r[1]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 8
	t5_t2 += MAS[3]

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 8
	t7_t5 += MAS[1]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 8
	t81 += MAS[0]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 8
	t91_mem0 += MAS_MEM[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 8
	t91_mem1 += MAS_MEM[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 9
	t0_t5 += MAS[3]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 9
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 9
	t1_t0_mem1 += MAIN_MEM_r[1]

	t1_t1 = S.Task('t1_t1', length=1, delay_cost=1)
	S += t1_t1 >= 9
	t1_t1 += MAS[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 9
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 9
	t50_mem1 += MM_MEM[1]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 9
	t91 += MAS[2]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 10
	t100_mem0 += MM_MEM[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 10
	t100_mem1 += MM_MEM[1]

	t1_t0 = S.Task('t1_t0', length=1, delay_cost=1)
	S += t1_t0 >= 10
	t1_t0 += MAS[1]

	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	S += t1_t2_in >= 10
	t1_t2_in += MM_in[0]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	S += t1_t2_mem0 >= 10
	t1_t2_mem0 += MAS_MEM[2]

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	S += t1_t2_mem1 >= 10
	t1_t2_mem1 += MAS_MEM[1]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 10
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 10
	t2_t2_mem1 += MAIN_MEM_r[1]

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 10
	t50 += MAS[2]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 10
	t60_mem0 += MAS_MEM[4]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 11
	t100 += MAS[1]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 11
	t10_t3_mem0 += MAIN_MEM_r[0]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 11
	t10_t3_mem1 += MAIN_MEM_r[1]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 11
	t10_t5_mem0 += MM_MEM[0]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 11
	t10_t5_mem1 += MM_MEM[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 11
	t110_mem0 += MAS_MEM[2]

	t1_t2 = S.Task('t1_t2', length=5, delay_cost=1)
	S += t1_t2 >= 11
	t1_t2 += MM[0]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 11
	t2_t2 += MAS[0]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 11
	t60 += MAS[2]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 12
	t10_t2_mem0 += MAIN_MEM_r[0]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 12
	t10_t2_mem1 += MAIN_MEM_r[1]

	t10_t3 = S.Task('t10_t3', length=1, delay_cost=1)
	S += t10_t3 >= 12
	t10_t3 += MAS[0]

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	S += t10_t5 >= 12
	t10_t5 += MAS[3]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 12
	t110 += MAS[1]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 12
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 12
	t5_t5_mem1 += MM_MEM[1]

	t10_t2 = S.Task('t10_t2', length=1, delay_cost=1)
	S += t10_t2 >= 13
	t10_t2 += MAS[0]

	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	S += t10_t4_in >= 13
	t10_t4_in += MM_in[0]

	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	S += t10_t4_mem0 >= 13
	t10_t4_mem0 += MAS_MEM[0]

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	S += t10_t4_mem1 >= 13
	t10_t4_mem1 += MAS_MEM[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 13
	t11_mem0 += MM_MEM[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 13
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 13
	t5_t3_mem1 += MAIN_MEM_r[1]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 13
	t5_t5 += MAS[2]

	t10_t4 = S.Task('t10_t4', length=5, delay_cost=1)
	S += t10_t4 >= 14
	t10_t4 += MM[0]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 14
	t11 += MAS[1]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	S += t1_t5_mem0 >= 14
	t1_t5_mem0 += MM_MEM[0]

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 14
	t5_t3 += MAS[0]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 14
	t5_t4_in += MM_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 14
	t5_t4_mem0 += MAS_MEM[6]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 14
	t5_t4_mem1 += MAS_MEM[1]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 14
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 14
	t7_t0_mem1 += MAIN_MEM_r[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 15
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 15
	t10_mem1 += MAS_MEM[3]

	t1_t5 = S.Task('t1_t5', length=1, delay_cost=1)
	S += t1_t5 >= 15
	t1_t5 += MAS[1]

	t5_t4 = S.Task('t5_t4', length=5, delay_cost=1)
	S += t5_t4 >= 15
	t5_t4 += MM[0]

	t7_t0 = S.Task('t7_t0', length=1, delay_cost=1)
	S += t7_t0 >= 15
	t7_t0 += MAS[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 15
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 15
	t7_t1_mem1 += MAIN_MEM_r[1]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 16
	t01_mem0 += MM_MEM[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 16
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 16
	t0_t0_mem1 += MAIN_MEM_r[1]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 16
	t10 += MAS[3]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 16
	t2_t3_mem0 += MAS_MEM[6]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 16
	t2_t3_mem1 += MAS_MEM[3]

	t7_t1 = S.Task('t7_t1', length=1, delay_cost=1)
	S += t7_t1 >= 16
	t7_t1 += MAS[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 16
	t7_t2_in += MM_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 16
	t7_t2_mem0 += MAS_MEM[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 16
	t7_t2_mem1 += MAS_MEM[1]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 17
	t01 += MAS[2]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 17
	t0_t0 += MAS[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 17
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 17
	t0_t1_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 17
	t2_t3 += MAS[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 17
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 17
	t2_t4_mem0 += MAS_MEM[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 17
	t2_t4_mem1 += MAS_MEM[3]

	t7_t2 = S.Task('t7_t2', length=5, delay_cost=1)
	S += t7_t2 >= 17
	t7_t2 += MM[0]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 18
	t0_t1 += MAS[0]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 18
	t0_t2_in += MM_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 18
	t0_t2_mem0 += MAS_MEM[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 18
	t0_t2_mem1 += MAS_MEM[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 18
	t101_mem0 += MM_MEM[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 18
	t101_mem1 += MAS_MEM[7]

	t2_t4 = S.Task('t2_t4', length=5, delay_cost=1)
	S += t2_t4 >= 18
	t2_t4 += MM[0]

	t0_t2 = S.Task('t0_t2', length=5, delay_cost=1)
	S += t0_t2 >= 19
	t0_t2 += MM[0]

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 19
	t101 += MAS[0]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 19
	t111_mem0 += MAS_MEM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 19
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 19
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 19
	t2_t1_mem1 += MAS_MEM[3]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 19
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 19
	t51_mem1 += MAS_MEM[5]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 20
	t111 += MAS[0]

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	S += t12_t3_mem0 >= 20
	t12_t3_mem0 += MAS_MEM[2]

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	S += t12_t3_mem1 >= 20
	t12_t3_mem1 += MAS_MEM[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 20
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 20
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 20
	t2_t0_mem1 += MAS_MEM[7]

	t2_t1 = S.Task('t2_t1', length=5, delay_cost=1)
	S += t2_t1 >= 20
	t2_t1 += MM[0]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 20
	t51 += MAS[2]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 20
	t61_mem0 += MAS_MEM[4]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 21
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 21
	c010_mem0 += MAS_MEM[2]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 21
	c010_mem1 += MAIN_MEM_r[1]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 21
	new_TX_t3_mem0 += MAS_MEM[4]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 21
	new_TX_t3_mem1 += MAS_MEM[5]

	t12_t3 = S.Task('t12_t3', length=1, delay_cost=1)
	S += t12_t3 >= 21
	t12_t3 += MAS[0]

	t2_t0 = S.Task('t2_t0', length=5, delay_cost=1)
	S += t2_t0 >= 21
	t2_t0 += MM[0]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 21
	t61 += MAS[2]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 21
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 21
	t70_mem1 += MAS_MEM[3]

	c010 = S.Task('c010', length=5, delay_cost=1)
	S += c010 >= 22
	c010 += MM[0]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 22
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 22
	c011_mem0 += MAS_MEM[0]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 22
	c011_mem1 += MAIN_MEM_r[1]

	new_TX_t3 = S.Task('new_TX_t3', length=1, delay_cost=1)
	S += new_TX_t3 >= 22
	new_TX_t3 += MAS[1]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 22
	t70 += MAS[2]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 22
	t80_mem0 += MAS_MEM[4]

	c011 = S.Task('c011', length=5, delay_cost=1)
	S += c011 >= 23
	c011 += MM[0]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 23
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 23
	c201_mem0 += MAS_MEM[4]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 23
	c201_mem1 += MAIN_MEM_r[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 23
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 23
	t00_mem1 += MAS_MEM[7]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 23
	t80 += MAS[3]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 23
	t90_mem0 += MAS_MEM[6]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 23
	t90_mem1 += MAS_MEM[5]

	c201 = S.Task('c201', length=5, delay_cost=1)
	S += c201 >= 24
	c201 += MM[0]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 24
	t00 += MAS[1]

	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	S += t12_t1_in >= 24
	t12_t1_in += MM_in[0]

	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	S += t12_t1_mem0 >= 24
	t12_t1_mem0 += MAS_MEM[4]

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	S += t12_t1_mem1 >= 24
	t12_t1_mem1 += MAS_MEM[1]

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	S += t18_t0_mem0 >= 24
	t18_t0_mem0 += MAS_MEM[2]

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	S += t18_t0_mem1 >= 24
	t18_t0_mem1 += MAS_MEM[5]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 24
	t90 += MAS[0]

	t12_t1 = S.Task('t12_t1', length=5, delay_cost=1)
	S += t12_t1 >= 25
	t12_t1 += MM[0]

	t18_t0 = S.Task('t18_t0', length=1, delay_cost=1)
	S += t18_t0 >= 25
	t18_t0 += MAS[3]

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	S += t18_t1_mem0 >= 25
	t18_t1_mem0 += MAS_MEM[2]

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	S += t18_t1_mem1 >= 25
	t18_t1_mem1 += MAS_MEM[5]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 25
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 25
	t20_mem1 += MM_MEM[1]

	t18_t1 = S.Task('t18_t1', length=1, delay_cost=1)
	S += t18_t1 >= 26
	t18_t1 += MAS[2]

	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	S += t18_t3_in >= 26
	t18_t3_in += MM_in[0]

	t18_t3_mem0 = S.Task('t18_t3_mem0', length=1, delay_cost=1)
	S += t18_t3_mem0 >= 26
	t18_t3_mem0 += MAS_MEM[2]

	t18_t3_mem1 = S.Task('t18_t3_mem1', length=1, delay_cost=1)
	S += t18_t3_mem1 >= 26
	t18_t3_mem1 += MAS_MEM[5]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 26
	t20 += MAS[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 26
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 26
	t2_t5_mem1 += MM_MEM[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 27
	c010_w += MAIN_MEM_w

	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	S += t18_t2_in >= 27
	t18_t2_in += MM_in[0]

	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	S += t18_t2_mem0 >= 27
	t18_t2_mem0 += MAS_MEM[6]

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	S += t18_t2_mem1 >= 27
	t18_t2_mem1 += MAS_MEM[5]

	t18_t3 = S.Task('t18_t3', length=5, delay_cost=1)
	S += t18_t3 >= 27
	t18_t3 += MM[0]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 27
	t2_t5 += MAS[2]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 28
	c011_w += MAIN_MEM_w

	t12_t2_mem0 = S.Task('t12_t2_mem0', length=1, delay_cost=1)
	S += t12_t2_mem0 >= 28
	t12_t2_mem0 += MAS_MEM[2]

	t12_t2_mem1 = S.Task('t12_t2_mem1', length=1, delay_cost=1)
	S += t12_t2_mem1 >= 28
	t12_t2_mem1 += MAS_MEM[5]

	t18_t2 = S.Task('t18_t2', length=5, delay_cost=1)
	S += t18_t2 >= 28
	t18_t2 += MM[0]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 29
	c201_w += MAIN_MEM_w

	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	S += t12_t0_in >= 29
	t12_t0_in += MM_in[0]

	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	S += t12_t0_mem0 >= 29
	t12_t0_mem0 += MAS_MEM[2]

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	S += t12_t0_mem1 >= 29
	t12_t0_mem1 += MAS_MEM[3]

	t12_t2 = S.Task('t12_t2', length=1, delay_cost=1)
	S += t12_t2 >= 29
	t12_t2 += MAS[3]

	t12_t0 = S.Task('t12_t0', length=5, delay_cost=1)
	S += t12_t0 >= 30
	t12_t0 += MM[0]

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	S += t18_t5_mem0 >= 33
	t18_t5_mem0 += MM_MEM[0]

	t18_t5 = S.Task('t18_t5', length=1, delay_cost=1)
	S += t18_t5 >= 34
	t18_t5 += MAS[3]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 38
	t181_mem0 += MM_MEM[0]

	t181 = S.Task('t181', length=1, delay_cost=1)
	S += t181 >= 39
	t181 += MAS[1]


	# new tasks
	t21 = S.Task('t21', length=1, delay_cost=1)
	t21 += alt(MAS)

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MM_MEM[0]
	S += 22 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAS_MEM[5]
	S += 27 < t21_mem1
	S += t21_mem1 <= t21

	t30 = S.Task('t30', length=1, delay_cost=1)
	t30 += alt(MAS)

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MAS_MEM[0]
	S += 26 < t30_mem0
	S += t30_mem0 <= t30

	t12_t4_in = S.Task('t12_t4_in', length=1, delay_cost=1)
	t12_t4_in += alt(MM_in)
	t12_t4 = S.Task('t12_t4', length=5, delay_cost=1)
	t12_t4 += alt(MM)
	S += t12_t4>=t12_t4_in

	t12_t4_mem0 = S.Task('t12_t4_mem0', length=1, delay_cost=1)
	t12_t4_mem0 += MAS_MEM[6]
	S += 29 < t12_t4_mem0
	S += t12_t4_mem0 <= t12_t4

	t12_t4_mem1 = S.Task('t12_t4_mem1', length=1, delay_cost=1)
	t12_t4_mem1 += MAS_MEM[1]
	S += 21 < t12_t4_mem1
	S += t12_t4_mem1 <= t12_t4

	t120 = S.Task('t120', length=1, delay_cost=1)
	t120 += alt(MAS)

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += MM_MEM[0]
	S += 34 < t120_mem0
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += MM_MEM[1]
	S += 29 < t120_mem1
	S += t120_mem1 <= t120

	t12_t5 = S.Task('t12_t5', length=1, delay_cost=1)
	t12_t5 += alt(MAS)

	t12_t5_mem0 = S.Task('t12_t5_mem0', length=1, delay_cost=1)
	t12_t5_mem0 += MM_MEM[0]
	S += 34 < t12_t5_mem0
	S += t12_t5_mem0 <= t12_t5

	t12_t5_mem1 = S.Task('t12_t5_mem1', length=1, delay_cost=1)
	t12_t5_mem1 += MM_MEM[1]
	S += 29 < t12_t5_mem1
	S += t12_t5_mem1 <= t12_t5

	t180 = S.Task('t180', length=1, delay_cost=1)
	t180 += alt(MAS)

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	t180_mem0 += MM_MEM[0]
	S += 32 < t180_mem0
	S += t180_mem0 <= t180

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	t180_mem1 += MAS_MEM[7]
	S += 34 < t180_mem1
	S += t180_mem1 <= t180

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MM_in)
	c200 = S.Task('c200', length=5, delay_cost=1)
	c200 += alt(MM)
	S += c200>=c200_in

	S += 0<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += MAS_MEM[0]
	S += 24 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAIN_MEM_r[1]
	S += c200_mem1 <= c200

	t31 = S.Task('t31', length=1, delay_cost=1)
	t31 += alt(MAS)

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t31_mem0*MAS_MEM[0]
	S += (t21*MAS[1])-1 < t31_mem0*MAS_MEM[2]
	S += (t21*MAS[2])-1 < t31_mem0*MAS_MEM[4]
	S += (t21*MAS[3])-1 < t31_mem0*MAS_MEM[6]
	S += t31_mem0 <= t31

	t40 = S.Task('t40', length=1, delay_cost=1)
	t40 += alt(MAS)

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	t40_mem0 += alt(MAS_MEM)
	S += (t30*MAS[0])-1 < t40_mem0*MAS_MEM[0]
	S += (t30*MAS[1])-1 < t40_mem0*MAS_MEM[2]
	S += (t30*MAS[2])-1 < t40_mem0*MAS_MEM[4]
	S += (t30*MAS[3])-1 < t40_mem0*MAS_MEM[6]
	S += t40_mem0 <= t40

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	t40_mem1 += MAS_MEM[1]
	S += 26 < t40_mem1
	S += t40_mem1 <= t40

	t121 = S.Task('t121', length=1, delay_cost=1)
	t121 += alt(MAS)

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	t121_mem0 += alt(MM_MEM)
	S += (t12_t4*MM[0])-1 < t121_mem0*MM_MEM[0]
	S += t121_mem0 <= t121

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	t121_mem1 += alt(MAS_MEM)
	S += (t12_t5*MAS[0])-1 < t121_mem1*MAS_MEM[1]
	S += (t12_t5*MAS[1])-1 < t121_mem1*MAS_MEM[3]
	S += (t12_t5*MAS[2])-1 < t121_mem1*MAS_MEM[5]
	S += (t12_t5*MAS[3])-1 < t121_mem1*MAS_MEM[7]
	S += t121_mem1 <= t121

	t130 = S.Task('t130', length=1, delay_cost=1)
	t130 += alt(MAS)

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	t130_mem0 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t130_mem0*MAS_MEM[0]
	S += (t120*MAS[1])-1 < t130_mem0*MAS_MEM[2]
	S += (t120*MAS[2])-1 < t130_mem0*MAS_MEM[4]
	S += (t120*MAS[3])-1 < t130_mem0*MAS_MEM[6]
	S += t130_mem0 <= t130

	t41 = S.Task('t41', length=1, delay_cost=1)
	t41 += alt(MAS)

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	t41_mem0 += alt(MAS_MEM)
	S += (t31*MAS[0])-1 < t41_mem0*MAS_MEM[0]
	S += (t31*MAS[1])-1 < t41_mem0*MAS_MEM[2]
	S += (t31*MAS[2])-1 < t41_mem0*MAS_MEM[4]
	S += (t31*MAS[3])-1 < t41_mem0*MAS_MEM[6]
	S += t41_mem0 <= t41

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	t41_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t41_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t41_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t41_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t41_mem1*MAS_MEM[7]
	S += t41_mem1 <= t41

	t131 = S.Task('t131', length=1, delay_cost=1)
	t131 += alt(MAS)

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += alt(MAS_MEM)
	S += (t121*MAS[0])-1 < t131_mem0*MAS_MEM[0]
	S += (t121*MAS[1])-1 < t131_mem0*MAS_MEM[2]
	S += (t121*MAS[2])-1 < t131_mem0*MAS_MEM[4]
	S += (t121*MAS[3])-1 < t131_mem0*MAS_MEM[6]
	S += t131_mem0 <= t131

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	new_TZ0 += alt(MAS)

	S += 12<new_TZ0

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	new_TZ0_w += alt(MAIN_MEM_w)
	S += new_TZ0 <= new_TZ0_w

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	new_TZ0_mem0 += alt(MAS_MEM)
	S += (t130*MAS[0])-1 < new_TZ0_mem0*MAS_MEM[0]
	S += (t130*MAS[1])-1 < new_TZ0_mem0*MAS_MEM[2]
	S += (t130*MAS[2])-1 < new_TZ0_mem0*MAS_MEM[4]
	S += (t130*MAS[3])-1 < new_TZ0_mem0*MAS_MEM[6]
	S += new_TZ0_mem0 <= new_TZ0

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)

	S += 0<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[2]
	S += 24 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (t40*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (t40*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (t40*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += c000_mem1 <= c000

	t140 = S.Task('t140', length=1, delay_cost=1)
	t140 += alt(MAS)

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < t140_mem0*MAS_MEM[0]
	S += (t40*MAS[1])-1 < t140_mem0*MAS_MEM[2]
	S += (t40*MAS[2])-1 < t140_mem0*MAS_MEM[4]
	S += (t40*MAS[3])-1 < t140_mem0*MAS_MEM[6]
	S += t140_mem0 <= t140

	new_TZ1 = S.Task('new_TZ1', length=1, delay_cost=1)
	new_TZ1 += alt(MAS)

	S += 12<new_TZ1

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	new_TZ1_w += alt(MAIN_MEM_w)
	S += new_TZ1 <= new_TZ1_w

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	new_TZ1_mem0 += alt(MAS_MEM)
	S += (t131*MAS[0])-1 < new_TZ1_mem0*MAS_MEM[0]
	S += (t131*MAS[1])-1 < new_TZ1_mem0*MAS_MEM[2]
	S += (t131*MAS[2])-1 < new_TZ1_mem0*MAS_MEM[4]
	S += (t131*MAS[3])-1 < new_TZ1_mem0*MAS_MEM[6]
	S += new_TZ1_mem0 <= new_TZ1

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)

	S += 0<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[4]
	S += 17 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += (t41*MAS[1])-1 < c001_mem1*MAS_MEM[3]
	S += (t41*MAS[2])-1 < c001_mem1*MAS_MEM[5]
	S += (t41*MAS[3])-1 < c001_mem1*MAS_MEM[7]
	S += c001_mem1 <= c001

	t141 = S.Task('t141', length=1, delay_cost=1)
	t141 += alt(MAS)

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < t141_mem0*MAS_MEM[0]
	S += (t41*MAS[1])-1 < t141_mem0*MAS_MEM[2]
	S += (t41*MAS[2])-1 < t141_mem0*MAS_MEM[4]
	S += (t41*MAS[3])-1 < t141_mem0*MAS_MEM[6]
	S += t141_mem0 <= t141

	t150 = S.Task('t150', length=1, delay_cost=1)
	t150 += alt(MAS)

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += alt(MAS_MEM)
	S += (c000*MAS[0])-1 < t150_mem0*MAS_MEM[0]
	S += (c000*MAS[1])-1 < t150_mem0*MAS_MEM[2]
	S += (c000*MAS[2])-1 < t150_mem0*MAS_MEM[4]
	S += (c000*MAS[3])-1 < t150_mem0*MAS_MEM[6]
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < t150_mem1*MAS_MEM[1]
	S += (t140*MAS[1])-1 < t150_mem1*MAS_MEM[3]
	S += (t140*MAS[2])-1 < t150_mem1*MAS_MEM[5]
	S += (t140*MAS[3])-1 < t150_mem1*MAS_MEM[7]
	S += t150_mem1 <= t150

	t160 = S.Task('t160', length=1, delay_cost=1)
	t160 += alt(MAS)

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += MAS_MEM[2]
	S += 24 < t160_mem0
	S += t160_mem0 <= t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(MAS_MEM)
	S += (c000*MAS[0])-1 < t160_mem1*MAS_MEM[1]
	S += (c000*MAS[1])-1 < t160_mem1*MAS_MEM[3]
	S += (c000*MAS[2])-1 < t160_mem1*MAS_MEM[5]
	S += (c000*MAS[3])-1 < t160_mem1*MAS_MEM[7]
	S += t160_mem1 <= t160

	b30 = S.Task('b30', length=1, delay_cost=1)
	b30 += alt(MAS)

	b30_mem0 = S.Task('b30_mem0', length=1, delay_cost=1)
	b30_mem0 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < b30_mem0*MAS_MEM[0]
	S += (t140*MAS[1])-1 < b30_mem0*MAS_MEM[2]
	S += (t140*MAS[2])-1 < b30_mem0*MAS_MEM[4]
	S += (t140*MAS[3])-1 < b30_mem0*MAS_MEM[6]
	S += b30_mem0 <= b30

	b30_mem1 = S.Task('b30_mem1', length=1, delay_cost=1)
	b30_mem1 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < b30_mem1*MAS_MEM[1]
	S += (t40*MAS[1])-1 < b30_mem1*MAS_MEM[3]
	S += (t40*MAS[2])-1 < b30_mem1*MAS_MEM[5]
	S += (t40*MAS[3])-1 < b30_mem1*MAS_MEM[7]
	S += b30_mem1 <= b30

	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(MAS)

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += alt(MAS_MEM)
	S += (c001*MAS[0])-1 < t151_mem0*MAS_MEM[0]
	S += (c001*MAS[1])-1 < t151_mem0*MAS_MEM[2]
	S += (c001*MAS[2])-1 < t151_mem0*MAS_MEM[4]
	S += (c001*MAS[3])-1 < t151_mem0*MAS_MEM[6]
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < t151_mem1*MAS_MEM[1]
	S += (t141*MAS[1])-1 < t151_mem1*MAS_MEM[3]
	S += (t141*MAS[2])-1 < t151_mem1*MAS_MEM[5]
	S += (t141*MAS[3])-1 < t151_mem1*MAS_MEM[7]
	S += t151_mem1 <= t151

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	new_TX_t0_in += alt(MM_in)
	new_TX_t0 = S.Task('new_TX_t0', length=5, delay_cost=1)
	new_TX_t0 += alt(MM)
	S += new_TX_t0>=new_TX_t0_in

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	new_TX_t0_mem0 += alt(MAS_MEM)
	S += (t150*MAS[0])-1 < new_TX_t0_mem0*MAS_MEM[0]
	S += (t150*MAS[1])-1 < new_TX_t0_mem0*MAS_MEM[2]
	S += (t150*MAS[2])-1 < new_TX_t0_mem0*MAS_MEM[4]
	S += (t150*MAS[3])-1 < new_TX_t0_mem0*MAS_MEM[6]
	S += new_TX_t0_mem0 <= new_TX_t0

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	new_TX_t0_mem1 += MAS_MEM[5]
	S += 11 < new_TX_t0_mem1
	S += new_TX_t0_mem1 <= new_TX_t0

	t161 = S.Task('t161', length=1, delay_cost=1)
	t161 += alt(MAS)

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += MAS_MEM[4]
	S += 17 < t161_mem0
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += alt(MAS_MEM)
	S += (c001*MAS[0])-1 < t161_mem1*MAS_MEM[1]
	S += (c001*MAS[1])-1 < t161_mem1*MAS_MEM[3]
	S += (c001*MAS[2])-1 < t161_mem1*MAS_MEM[5]
	S += (c001*MAS[3])-1 < t161_mem1*MAS_MEM[7]
	S += t161_mem1 <= t161

	b31 = S.Task('b31', length=1, delay_cost=1)
	b31 += alt(MAS)

	b31_mem0 = S.Task('b31_mem0', length=1, delay_cost=1)
	b31_mem0 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < b31_mem0*MAS_MEM[0]
	S += (t141*MAS[1])-1 < b31_mem0*MAS_MEM[2]
	S += (t141*MAS[2])-1 < b31_mem0*MAS_MEM[4]
	S += (t141*MAS[3])-1 < b31_mem0*MAS_MEM[6]
	S += b31_mem0 <= b31

	b31_mem1 = S.Task('b31_mem1', length=1, delay_cost=1)
	b31_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < b31_mem1*MAS_MEM[1]
	S += (t41*MAS[1])-1 < b31_mem1*MAS_MEM[3]
	S += (t41*MAS[2])-1 < b31_mem1*MAS_MEM[5]
	S += (t41*MAS[3])-1 < b31_mem1*MAS_MEM[7]
	S += b31_mem1 <= b31

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	t17_t0_in += alt(MM_in)
	t17_t0 = S.Task('t17_t0', length=5, delay_cost=1)
	t17_t0 += alt(MM)
	S += t17_t0>=t17_t0_in

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	t17_t0_mem0 += alt(MAS_MEM)
	S += (b30*MAS[0])-1 < t17_t0_mem0*MAS_MEM[0]
	S += (b30*MAS[1])-1 < t17_t0_mem0*MAS_MEM[2]
	S += (b30*MAS[2])-1 < t17_t0_mem0*MAS_MEM[4]
	S += (b30*MAS[3])-1 < t17_t0_mem0*MAS_MEM[6]
	S += t17_t0_mem0 <= t17_t0

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	t17_t0_mem1 += alt(MAS_MEM)
	S += (t160*MAS[0])-1 < t17_t0_mem1*MAS_MEM[1]
	S += (t160*MAS[1])-1 < t17_t0_mem1*MAS_MEM[3]
	S += (t160*MAS[2])-1 < t17_t0_mem1*MAS_MEM[5]
	S += (t160*MAS[3])-1 < t17_t0_mem1*MAS_MEM[7]
	S += t17_t0_mem1 <= t17_t0

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	new_TX_t1_in += alt(MM_in)
	new_TX_t1 = S.Task('new_TX_t1', length=5, delay_cost=1)
	new_TX_t1 += alt(MM)
	S += new_TX_t1>=new_TX_t1_in

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	new_TX_t1_mem0 += alt(MAS_MEM)
	S += (t151*MAS[0])-1 < new_TX_t1_mem0*MAS_MEM[0]
	S += (t151*MAS[1])-1 < new_TX_t1_mem0*MAS_MEM[2]
	S += (t151*MAS[2])-1 < new_TX_t1_mem0*MAS_MEM[4]
	S += (t151*MAS[3])-1 < new_TX_t1_mem0*MAS_MEM[6]
	S += new_TX_t1_mem0 <= new_TX_t1

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	new_TX_t1_mem1 += MAS_MEM[5]
	S += 21 < new_TX_t1_mem1
	S += new_TX_t1_mem1 <= new_TX_t1

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	new_TX_t2 += alt(MAS)

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	new_TX_t2_mem0 += alt(MAS_MEM)
	S += (t150*MAS[0])-1 < new_TX_t2_mem0*MAS_MEM[0]
	S += (t150*MAS[1])-1 < new_TX_t2_mem0*MAS_MEM[2]
	S += (t150*MAS[2])-1 < new_TX_t2_mem0*MAS_MEM[4]
	S += (t150*MAS[3])-1 < new_TX_t2_mem0*MAS_MEM[6]
	S += new_TX_t2_mem0 <= new_TX_t2

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	new_TX_t2_mem1 += alt(MAS_MEM)
	S += (t151*MAS[0])-1 < new_TX_t2_mem1*MAS_MEM[1]
	S += (t151*MAS[1])-1 < new_TX_t2_mem1*MAS_MEM[3]
	S += (t151*MAS[2])-1 < new_TX_t2_mem1*MAS_MEM[5]
	S += (t151*MAS[3])-1 < new_TX_t2_mem1*MAS_MEM[7]
	S += new_TX_t2_mem1 <= new_TX_t2

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	t17_t1_in += alt(MM_in)
	t17_t1 = S.Task('t17_t1', length=5, delay_cost=1)
	t17_t1 += alt(MM)
	S += t17_t1>=t17_t1_in

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	t17_t1_mem0 += alt(MAS_MEM)
	S += (b31*MAS[0])-1 < t17_t1_mem0*MAS_MEM[0]
	S += (b31*MAS[1])-1 < t17_t1_mem0*MAS_MEM[2]
	S += (b31*MAS[2])-1 < t17_t1_mem0*MAS_MEM[4]
	S += (b31*MAS[3])-1 < t17_t1_mem0*MAS_MEM[6]
	S += t17_t1_mem0 <= t17_t1

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	t17_t1_mem1 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < t17_t1_mem1*MAS_MEM[1]
	S += (t161*MAS[1])-1 < t17_t1_mem1*MAS_MEM[3]
	S += (t161*MAS[2])-1 < t17_t1_mem1*MAS_MEM[5]
	S += (t161*MAS[3])-1 < t17_t1_mem1*MAS_MEM[7]
	S += t17_t1_mem1 <= t17_t1

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	t17_t2 += alt(MAS)

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	t17_t2_mem0 += alt(MAS_MEM)
	S += (b30*MAS[0])-1 < t17_t2_mem0*MAS_MEM[0]
	S += (b30*MAS[1])-1 < t17_t2_mem0*MAS_MEM[2]
	S += (b30*MAS[2])-1 < t17_t2_mem0*MAS_MEM[4]
	S += (b30*MAS[3])-1 < t17_t2_mem0*MAS_MEM[6]
	S += t17_t2_mem0 <= t17_t2

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	t17_t2_mem1 += alt(MAS_MEM)
	S += (b31*MAS[0])-1 < t17_t2_mem1*MAS_MEM[1]
	S += (b31*MAS[1])-1 < t17_t2_mem1*MAS_MEM[3]
	S += (b31*MAS[2])-1 < t17_t2_mem1*MAS_MEM[5]
	S += (b31*MAS[3])-1 < t17_t2_mem1*MAS_MEM[7]
	S += t17_t2_mem1 <= t17_t2

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	t17_t3 += alt(MAS)

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	t17_t3_mem0 += alt(MAS_MEM)
	S += (t160*MAS[0])-1 < t17_t3_mem0*MAS_MEM[0]
	S += (t160*MAS[1])-1 < t17_t3_mem0*MAS_MEM[2]
	S += (t160*MAS[2])-1 < t17_t3_mem0*MAS_MEM[4]
	S += (t160*MAS[3])-1 < t17_t3_mem0*MAS_MEM[6]
	S += t17_t3_mem0 <= t17_t3

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	t17_t3_mem1 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < t17_t3_mem1*MAS_MEM[1]
	S += (t161*MAS[1])-1 < t17_t3_mem1*MAS_MEM[3]
	S += (t161*MAS[2])-1 < t17_t3_mem1*MAS_MEM[5]
	S += (t161*MAS[3])-1 < t17_t3_mem1*MAS_MEM[7]
	S += t17_t3_mem1 <= t17_t3

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	new_TX_t4_in += alt(MM_in)
	new_TX_t4 = S.Task('new_TX_t4', length=5, delay_cost=1)
	new_TX_t4 += alt(MM)
	S += new_TX_t4>=new_TX_t4_in

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	new_TX_t4_mem0 += alt(MAS_MEM)
	S += (new_TX_t2*MAS[0])-1 < new_TX_t4_mem0*MAS_MEM[0]
	S += (new_TX_t2*MAS[1])-1 < new_TX_t4_mem0*MAS_MEM[2]
	S += (new_TX_t2*MAS[2])-1 < new_TX_t4_mem0*MAS_MEM[4]
	S += (new_TX_t2*MAS[3])-1 < new_TX_t4_mem0*MAS_MEM[6]
	S += new_TX_t4_mem0 <= new_TX_t4

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	new_TX_t4_mem1 += MAS_MEM[3]
	S += 22 < new_TX_t4_mem1
	S += new_TX_t4_mem1 <= new_TX_t4

	new_TX0 = S.Task('new_TX0', length=1, delay_cost=1)
	new_TX0 += alt(MAS)

	S += 16<new_TX0

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	new_TX0_w += alt(MAIN_MEM_w)
	S += new_TX0 <= new_TX0_w

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	new_TX0_mem0 += alt(MM_MEM)
	S += (new_TX_t0*MM[0])-1 < new_TX0_mem0*MM_MEM[0]
	S += new_TX0_mem0 <= new_TX0

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	new_TX0_mem1 += alt(MM_MEM)
	S += (new_TX_t1*MM[0])-1 < new_TX0_mem1*MM_MEM[1]
	S += new_TX0_mem1 <= new_TX0

	new_TX_t5 = S.Task('new_TX_t5', length=1, delay_cost=1)
	new_TX_t5 += alt(MAS)

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	new_TX_t5_mem0 += alt(MM_MEM)
	S += (new_TX_t0*MM[0])-1 < new_TX_t5_mem0*MM_MEM[0]
	S += new_TX_t5_mem0 <= new_TX_t5

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	new_TX_t5_mem1 += alt(MM_MEM)
	S += (new_TX_t1*MM[0])-1 < new_TX_t5_mem1*MM_MEM[1]
	S += new_TX_t5_mem1 <= new_TX_t5

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	t17_t4_in += alt(MM_in)
	t17_t4 = S.Task('t17_t4', length=5, delay_cost=1)
	t17_t4 += alt(MM)
	S += t17_t4>=t17_t4_in

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	t17_t4_mem0 += alt(MAS_MEM)
	S += (t17_t2*MAS[0])-1 < t17_t4_mem0*MAS_MEM[0]
	S += (t17_t2*MAS[1])-1 < t17_t4_mem0*MAS_MEM[2]
	S += (t17_t2*MAS[2])-1 < t17_t4_mem0*MAS_MEM[4]
	S += (t17_t2*MAS[3])-1 < t17_t4_mem0*MAS_MEM[6]
	S += t17_t4_mem0 <= t17_t4

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	t17_t4_mem1 += alt(MAS_MEM)
	S += (t17_t3*MAS[0])-1 < t17_t4_mem1*MAS_MEM[1]
	S += (t17_t3*MAS[1])-1 < t17_t4_mem1*MAS_MEM[3]
	S += (t17_t3*MAS[2])-1 < t17_t4_mem1*MAS_MEM[5]
	S += (t17_t3*MAS[3])-1 < t17_t4_mem1*MAS_MEM[7]
	S += t17_t4_mem1 <= t17_t4

	t170 = S.Task('t170', length=1, delay_cost=1)
	t170 += alt(MAS)

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += alt(MM_MEM)
	S += (t17_t0*MM[0])-1 < t170_mem0*MM_MEM[0]
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(MM_MEM)
	S += (t17_t1*MM[0])-1 < t170_mem1*MM_MEM[1]
	S += t170_mem1 <= t170

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	t17_t5 += alt(MAS)

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	t17_t5_mem0 += alt(MM_MEM)
	S += (t17_t0*MM[0])-1 < t17_t5_mem0*MM_MEM[0]
	S += t17_t5_mem0 <= t17_t5

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	t17_t5_mem1 += alt(MM_MEM)
	S += (t17_t1*MM[0])-1 < t17_t5_mem1*MM_MEM[1]
	S += t17_t5_mem1 <= t17_t5

	new_TX1 = S.Task('new_TX1', length=1, delay_cost=1)
	new_TX1 += alt(MAS)

	S += 16<new_TX1

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	new_TX1_w += alt(MAIN_MEM_w)
	S += new_TX1 <= new_TX1_w

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	new_TX1_mem0 += alt(MM_MEM)
	S += (new_TX_t4*MM[0])-1 < new_TX1_mem0*MM_MEM[0]
	S += new_TX1_mem0 <= new_TX1

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	new_TX1_mem1 += alt(MAS_MEM)
	S += (new_TX_t5*MAS[0])-1 < new_TX1_mem1*MAS_MEM[1]
	S += (new_TX_t5*MAS[1])-1 < new_TX1_mem1*MAS_MEM[3]
	S += (new_TX_t5*MAS[2])-1 < new_TX1_mem1*MAS_MEM[5]
	S += (new_TX_t5*MAS[3])-1 < new_TX1_mem1*MAS_MEM[7]
	S += new_TX1_mem1 <= new_TX1

	t171 = S.Task('t171', length=1, delay_cost=1)
	t171 += alt(MAS)

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(MM_MEM)
	S += (t17_t4*MM[0])-1 < t171_mem0*MM_MEM[0]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += alt(MAS_MEM)
	S += (t17_t5*MAS[0])-1 < t171_mem1*MAS_MEM[1]
	S += (t17_t5*MAS[1])-1 < t171_mem1*MAS_MEM[3]
	S += (t17_t5*MAS[2])-1 < t171_mem1*MAS_MEM[5]
	S += (t17_t5*MAS[3])-1 < t171_mem1*MAS_MEM[7]
	S += t171_mem1 <= t171

	new_TY0 = S.Task('new_TY0', length=1, delay_cost=1)
	new_TY0 += alt(MAS)

	S += 18<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += alt(MAS_MEM)
	S += (t170*MAS[0])-1 < new_TY0_mem0*MAS_MEM[0]
	S += (t170*MAS[1])-1 < new_TY0_mem0*MAS_MEM[2]
	S += (t170*MAS[2])-1 < new_TY0_mem0*MAS_MEM[4]
	S += (t170*MAS[3])-1 < new_TY0_mem0*MAS_MEM[6]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += alt(MAS_MEM)
	S += (t180*MAS[0])-1 < new_TY0_mem1*MAS_MEM[1]
	S += (t180*MAS[1])-1 < new_TY0_mem1*MAS_MEM[3]
	S += (t180*MAS[2])-1 < new_TY0_mem1*MAS_MEM[5]
	S += (t180*MAS[3])-1 < new_TY0_mem1*MAS_MEM[7]
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=1, delay_cost=1)
	new_TY1 += alt(MAS)

	S += 18<new_TY1

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	new_TY1_w += alt(MAIN_MEM_w)
	S += new_TY1 <= new_TY1_w

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	new_TY1_mem0 += alt(MAS_MEM)
	S += (t171*MAS[0])-1 < new_TY1_mem0*MAS_MEM[0]
	S += (t171*MAS[1])-1 < new_TY1_mem0*MAS_MEM[2]
	S += (t171*MAS[2])-1 < new_TY1_mem0*MAS_MEM[4]
	S += (t171*MAS[3])-1 < new_TY1_mem0*MAS_MEM[6]
	S += new_TY1_mem0 <= new_TY1

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	new_TY1_mem1 += MAS_MEM[3]
	S += 39 < new_TY1_mem1
	S += new_TY1_mem1 <= new_TY1

	solvers.mip.solve(S,msg=1,ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage1MAS4/EP2_DBL_w_EVAL/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

