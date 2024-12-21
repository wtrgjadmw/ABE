from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 122
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 0
	t11_in += MAS_in[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 0
	t11_mem0 += MAIN_MEM_r[0]

	t3_t2_in = S.Task('t3_t2_in', length=1, delay_cost=1)
	S += t3_t2_in >= 0
	t3_t2_in += MAS_in[3]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 0
	t5_t2_in += MAS_in[2]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 0
	t6_t1_mem1 += MAIN_MEM_r[1]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 0
	t7_t1_in += MM_in[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 0
	t7_t2_in += MAS_in[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 1
	t0_t0_in += MAS_in[1]

	t11 = S.Task('t11', length=2, delay_cost=1)
	S += t11 >= 1
	t11 += MAS[1]

	t3_t2 = S.Task('t3_t2', length=2, delay_cost=1)
	S += t3_t2 >= 1
	t3_t2 += MAS[3]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 1
	t4_t0_in += MAS_in[0]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 1
	t4_t1_in += MAS_in[2]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 1
	t5_t1_mem1 += MAIN_MEM_r[1]

	t5_t2 = S.Task('t5_t2', length=2, delay_cost=1)
	S += t5_t2 >= 1
	t5_t2 += MAS[2]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 1
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 1
	t6_t0_mem0 += MAIN_MEM_r[0]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 1
	t6_t2_in += MAS_in[3]

	t7_t1 = S.Task('t7_t1', length=4, delay_cost=1)
	S += t7_t1 >= 1
	t7_t1 += MM[0]

	t7_t2 = S.Task('t7_t2', length=2, delay_cost=1)
	S += t7_t2 >= 1
	t7_t2 += MAS[0]

	t0_t0 = S.Task('t0_t0', length=2, delay_cost=1)
	S += t0_t0 >= 2
	t0_t0 += MAS[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 2
	t0_t1_mem0 += MAIN_MEM_r[0]

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	S += t3_t2_mem1 >= 2
	t3_t2_mem1 += MAIN_MEM_r[1]

	t3_t3_in = S.Task('t3_t3_in', length=1, delay_cost=1)
	S += t3_t3_in >= 2
	t3_t3_in += MAS_in[0]

	t4_t0 = S.Task('t4_t0', length=2, delay_cost=1)
	S += t4_t0 >= 2
	t4_t0 += MAS[0]

	t4_t1 = S.Task('t4_t1', length=2, delay_cost=1)
	S += t4_t1 >= 2
	t4_t1 += MAS[2]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 2
	t5_t3_in += MAS_in[2]

	t6_t0 = S.Task('t6_t0', length=4, delay_cost=1)
	S += t6_t0 >= 2
	t6_t0 += MM[0]

	t6_t2 = S.Task('t6_t2', length=2, delay_cost=1)
	S += t6_t2 >= 2
	t6_t2 += MAS[3]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 2
	t6_t3_in += MAS_in[3]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 2
	t7_t0_in += MM_in[0]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 2
	t7_t3_in += MAS_in[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 3
	t0_t1_in += MAS_in[0]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 3
	t10_in += MAS_in[1]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 3
	t21_in += MAS_in[3]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 3
	t21_mem0 += MAS_MEM[2]

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	S += t3_t0_in >= 3
	t3_t0_in += MM_in[0]

	t3_t3 = S.Task('t3_t3', length=2, delay_cost=1)
	S += t3_t3 >= 3
	t3_t3 += MAS[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 3
	t4_t0_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=2, delay_cost=1)
	S += t5_t3 >= 3
	t5_t3 += MAS[2]

	t6_t3 = S.Task('t6_t3', length=2, delay_cost=1)
	S += t6_t3 >= 3
	t6_t3 += MAS[3]

	t7_t0 = S.Task('t7_t0', length=4, delay_cost=1)
	S += t7_t0 >= 3
	t7_t0 += MM[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 3
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t3 = S.Task('t7_t3', length=2, delay_cost=1)
	S += t7_t3 >= 3
	t7_t3 += MAS[1]

	t0_t1 = S.Task('t0_t1', length=2, delay_cost=1)
	S += t0_t1 >= 4
	t0_t1 += MAS[0]

	t10 = S.Task('t10', length=2, delay_cost=1)
	S += t10 >= 4
	t10 += MAS[1]

	t21 = S.Task('t21', length=2, delay_cost=1)
	S += t21 >= 4
	t21 += MAS[3]

	t3_t0 = S.Task('t3_t0', length=4, delay_cost=1)
	S += t3_t0 >= 4
	t3_t0 += MM[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 4
	t5_t0_mem1 += MAIN_MEM_r[1]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 4
	t5_t2_mem0 += MAIN_MEM_r[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 4
	t6_t1_in += MM_in[0]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 4
	t81_in += MAS_in[1]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 4
	t81_mem0 += MAS_MEM[2]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 5
	t20_in += MAS_in[2]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 5
	t20_mem0 += MAS_MEM[2]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 5
	t4_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 5
	t5_t0_in += MM_in[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 5
	t5_t2_mem1 += MAIN_MEM_r[1]

	t6_t1 = S.Task('t6_t1', length=4, delay_cost=1)
	S += t6_t1 >= 5
	t6_t1 += MM[0]

	t81 = S.Task('t81', length=2, delay_cost=1)
	S += t81 >= 5
	t81 += MAS[1]

	t20 = S.Task('t20', length=2, delay_cost=1)
	S += t20 >= 6
	t20 += MAS[2]

	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	S += t3_t1_in >= 6
	t3_t1_in += MM_in[0]

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	S += t3_t3_mem1 >= 6
	t3_t3_mem1 += MAIN_MEM_r[1]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 6
	t4_t1_mem0 += MAIN_MEM_r[0]

	t5_t0 = S.Task('t5_t0', length=4, delay_cost=1)
	S += t5_t0 >= 6
	t5_t0 += MM[0]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 6
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 6
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 6
	t70_mem1 += MM_MEM[1]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 6
	t80_in += MAS_in[3]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 6
	t80_mem0 += MAS_MEM[2]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 7
	t0_t0_mem0 += MAIN_MEM_r[0]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 7
	t10_t1_in += MAS_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 7
	t10_t1_mem0 += MAS_MEM[4]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 7
	t10_t1_mem1 += MAS_MEM[7]

	t3_t1 = S.Task('t3_t1', length=4, delay_cost=1)
	S += t3_t1 >= 7
	t3_t1 += MM[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 7
	t4_t3_in += MM_in[0]

	t70 = S.Task('t70', length=2, delay_cost=1)
	S += t70 >= 7
	t70 += MAS[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 7
	t7_t1_mem1 += MAIN_MEM_r[1]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 7
	t7_t5_in += MAS_in[1]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 7
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 7
	t7_t5_mem1 += MM_MEM[1]

	t80 = S.Task('t80', length=2, delay_cost=1)
	S += t80 >= 7
	t80 += MAS[3]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 8
	t0_t3_in += MM_in[0]

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 8
	t10_t0_in += MAS_in[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 8
	t10_t0_mem0 += MAS_MEM[4]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 8
	t10_t0_mem1 += MAS_MEM[7]

	t10_t1 = S.Task('t10_t1', length=2, delay_cost=1)
	S += t10_t1 >= 8
	t10_t1 += MAS[0]

	t260_in = S.Task('t260_in', length=1, delay_cost=1)
	S += t260_in >= 8
	t260_in += MAS_in[2]

	t260_mem0 = S.Task('t260_mem0', length=1, delay_cost=1)
	S += t260_mem0 >= 8
	t260_mem0 += MAS_MEM[0]

	t4_t3 = S.Task('t4_t3', length=4, delay_cost=1)
	S += t4_t3 >= 8
	t4_t3 += MM[0]

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 8
	t60_in += MAS_in[3]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 8
	t60_mem0 += MM_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 8
	t60_mem1 += MM_MEM[1]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 8
	t6_t0_mem1 += MAIN_MEM_r[1]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 8
	t6_t3_mem0 += MAIN_MEM_r[0]

	t7_t5 = S.Task('t7_t5', length=2, delay_cost=1)
	S += t7_t5 >= 8
	t7_t5 += MAS[1]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 8
	t9_t1_in += MAS_in[1]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 8
	t9_t1_mem0 += MAS_MEM[6]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 8
	t9_t1_mem1 += MAS_MEM[3]

	t0_t3 = S.Task('t0_t3', length=4, delay_cost=1)
	S += t0_t3 >= 9
	t0_t3 += MM[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 9
	t10_mem0 += MAIN_MEM_r[0]

	t10_t0 = S.Task('t10_t0', length=2, delay_cost=1)
	S += t10_t0 >= 9
	t10_t0 += MAS[0]

	t260 = S.Task('t260', length=2, delay_cost=1)
	S += t260 >= 9
	t260 += MAS[2]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 9
	t4_t3_mem1 += MAIN_MEM_r[1]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 9
	t5_t1_in += MM_in[0]

	t60 = S.Task('t60', length=2, delay_cost=1)
	S += t60 >= 9
	t60 += MAS[3]

	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	S += t6_t5_in >= 9
	t6_t5_in += MAS_in[2]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 9
	t6_t5_mem0 += MM_MEM[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 9
	t6_t5_mem1 += MM_MEM[1]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 9
	t9_t0_in += MAS_in[3]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 9
	t9_t0_mem0 += MAS_MEM[6]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 9
	t9_t0_mem1 += MAS_MEM[3]

	t9_t1 = S.Task('t9_t1', length=2, delay_cost=1)
	S += t9_t1 >= 9
	t9_t1 += MAS[1]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 10
	t0_t3_mem1 += MAIN_MEM_r[1]

	t220_in = S.Task('t220_in', length=1, delay_cost=1)
	S += t220_in >= 10
	t220_in += MAS_in[2]

	t220_mem0 = S.Task('t220_mem0', length=1, delay_cost=1)
	S += t220_mem0 >= 10
	t220_mem0 += MAS_MEM[6]

	t270_in = S.Task('t270_in', length=1, delay_cost=1)
	S += t270_in >= 10
	t270_in += MAS_in[1]

	t270_mem0 = S.Task('t270_mem0', length=1, delay_cost=1)
	S += t270_mem0 >= 10
	t270_mem0 += MAS_MEM[4]

	t270_mem1 = S.Task('t270_mem1', length=1, delay_cost=1)
	S += t270_mem1 >= 10
	t270_mem1 += MAS_MEM[1]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 10
	t30_in += MAS_in[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 10
	t30_mem0 += MM_MEM[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 10
	t30_mem1 += MM_MEM[1]

	t5_t1 = S.Task('t5_t1', length=4, delay_cost=1)
	S += t5_t1 >= 10
	t5_t1 += MM[0]

	t6_t5 = S.Task('t6_t5', length=2, delay_cost=1)
	S += t6_t5 >= 10
	t6_t5 += MAS[2]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 10
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 10
	t7_t4_in += MM_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 10
	t7_t4_mem0 += MAS_MEM[0]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 10
	t7_t4_mem1 += MAS_MEM[3]

	t9_t0 = S.Task('t9_t0', length=2, delay_cost=1)
	S += t9_t0 >= 10
	t9_t0 += MAS[3]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 11
	t11_mem1 += MAIN_MEM_r[1]

	t220 = S.Task('t220', length=2, delay_cost=1)
	S += t220 >= 11
	t220 += MAS[2]

	t270 = S.Task('t270', length=2, delay_cost=1)
	S += t270 >= 11
	t270 += MAS[1]

	t30 = S.Task('t30', length=2, delay_cost=1)
	S += t30 >= 11
	t30 += MAS[0]

	t3_t4_in = S.Task('t3_t4_in', length=1, delay_cost=1)
	S += t3_t4_in >= 11
	t3_t4_in += MM_in[0]

	t3_t4_mem0 = S.Task('t3_t4_mem0', length=1, delay_cost=1)
	S += t3_t4_mem0 >= 11
	t3_t4_mem0 += MAS_MEM[6]

	t3_t4_mem1 = S.Task('t3_t4_mem1', length=1, delay_cost=1)
	S += t3_t4_mem1 >= 11
	t3_t4_mem1 += MAS_MEM[1]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 11
	t41_in += MAS_in[2]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 11
	t41_mem0 += MM_MEM[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 11
	t5_t1_mem0 += MAIN_MEM_r[0]

	t7_t4 = S.Task('t7_t4', length=4, delay_cost=1)
	S += t7_t4 >= 11
	t7_t4 += MM[0]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 12
	t01_in += MAS_in[1]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 12
	t01_mem0 += MM_MEM[0]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 12
	t110_in += MAS_in[2]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 12
	t110_mem0 += MAS_MEM[0]

	t280_in = S.Task('t280_in', length=1, delay_cost=1)
	S += t280_in >= 12
	t280_in += MAS_in[0]

	t280_mem0 = S.Task('t280_mem0', length=1, delay_cost=1)
	S += t280_mem0 >= 12
	t280_mem0 += MAS_MEM[2]

	t3_t4 = S.Task('t3_t4', length=4, delay_cost=1)
	S += t3_t4 >= 12
	t3_t4 += MM[0]

	t41 = S.Task('t41', length=2, delay_cost=1)
	S += t41 >= 12
	t41 += MAS[2]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 12
	t5_t4_in += MM_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 12
	t5_t4_mem0 += MAS_MEM[4]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 12
	t5_t4_mem1 += MAS_MEM[5]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 12
	t6_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 12
	t7_t2_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=2, delay_cost=1)
	S += t01 >= 13
	t01 += MAS[1]

	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	S += t10_t3_in >= 13
	t10_t3_in += MM_in[0]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 13
	t10_t3_mem0 += MAS_MEM[4]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 13
	t10_t3_mem1 += MAS_MEM[7]

	t110 = S.Task('t110', length=2, delay_cost=1)
	S += t110 >= 13
	t110 += MAS[2]

	t280 = S.Task('t280', length=2, delay_cost=1)
	S += t280 >= 13
	t280 += MAS[0]

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_mem1 >= 13
	t3_t0_mem1 += MAIN_MEM_r[1]

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_mem0 >= 13
	t3_t1_mem0 += MAIN_MEM_r[0]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 13
	t50_in += MAS_in[2]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 13
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 13
	t50_mem1 += MM_MEM[1]

	t5_t4 = S.Task('t5_t4', length=4, delay_cost=1)
	S += t5_t4 >= 13
	t5_t4 += MM[0]

	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	S += c210_in >= 14
	c210_in += MAS_in[1]

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	S += c210_mem0 >= 14
	c210_mem0 += MAS_MEM[0]

	t10_t3 = S.Task('t10_t3', length=4, delay_cost=1)
	S += t10_t3 >= 14
	t10_t3 += MM[0]

	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	S += t151_in >= 14
	t151_in += MAS_in[2]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 14
	t151_mem0 += MAS_MEM[2]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 14
	t151_mem1 += MAS_MEM[5]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 14
	t4_t1_mem1 += MAIN_MEM_r[1]

	t50 = S.Task('t50', length=2, delay_cost=1)
	S += t50 >= 14
	t50 += MAS[2]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 14
	t6_t1_mem0 += MAIN_MEM_r[0]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 14
	t6_t4_in += MM_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 14
	t6_t4_mem0 += MAS_MEM[6]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 14
	t6_t4_mem1 += MAS_MEM[7]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 14
	t71_in += MAS_in[3]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 14
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 14
	t71_mem1 += MAS_MEM[3]

	c210 = S.Task('c210', length=2, delay_cost=1)
	S += c210 >= 15
	c210 += MAS[1]

	t151 = S.Task('t151', length=2, delay_cost=1)
	S += t151 >= 15
	t151 += MAS[2]

	t290_in = S.Task('t290_in', length=1, delay_cost=1)
	S += t290_in >= 15
	t290_in += MAS_in[2]

	t290_mem0 = S.Task('t290_mem0', length=1, delay_cost=1)
	S += t290_mem0 >= 15
	t290_mem0 += MAS_MEM[4]

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_mem0 >= 15
	t3_t0_mem0 += MAIN_MEM_r[0]

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_mem1 >= 15
	t3_t1_mem1 += MAIN_MEM_r[1]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 15
	t5_t5_in += MAS_in[1]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 15
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 15
	t5_t5_mem1 += MM_MEM[1]

	t6_t4 = S.Task('t6_t4', length=4, delay_cost=1)
	S += t6_t4 >= 15
	t6_t4 += MM[0]

	t71 = S.Task('t71', length=2, delay_cost=1)
	S += t71 >= 15
	t71 += MAS[3]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 15
	t9_t3_in += MM_in[0]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 15
	t9_t3_mem0 += MAS_MEM[6]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 15
	t9_t3_mem1 += MAS_MEM[3]

	t230_in = S.Task('t230_in', length=1, delay_cost=1)
	S += t230_in >= 16
	t230_in += MAS_in[0]

	t230_mem0 = S.Task('t230_mem0', length=1, delay_cost=1)
	S += t230_mem0 >= 16
	t230_mem0 += MAS_MEM[4]

	t230_mem1 = S.Task('t230_mem1', length=1, delay_cost=1)
	S += t230_mem1 >= 16
	t230_mem1 += MAS_MEM[7]

	t261_in = S.Task('t261_in', length=1, delay_cost=1)
	S += t261_in >= 16
	t261_in += MAS_in[2]

	t261_mem0 = S.Task('t261_mem0', length=1, delay_cost=1)
	S += t261_mem0 >= 16
	t261_mem0 += MAS_MEM[6]

	t290 = S.Task('t290', length=2, delay_cost=1)
	S += t290 >= 16
	t290 += MAS[2]

	t3_t5_in = S.Task('t3_t5_in', length=1, delay_cost=1)
	S += t3_t5_in >= 16
	t3_t5_in += MAS_in[3]

	t3_t5_mem0 = S.Task('t3_t5_mem0', length=1, delay_cost=1)
	S += t3_t5_mem0 >= 16
	t3_t5_mem0 += MM_MEM[0]

	t3_t5_mem1 = S.Task('t3_t5_mem1', length=1, delay_cost=1)
	S += t3_t5_mem1 >= 16
	t3_t5_mem1 += MM_MEM[1]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 16
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 16
	t4_t2_mem0 += MAS_MEM[0]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 16
	t4_t2_mem1 += MAS_MEM[5]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 16
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 16
	t5_t3_mem1 += MAIN_MEM_r[1]

	t5_t5 = S.Task('t5_t5', length=2, delay_cost=1)
	S += t5_t5 >= 16
	t5_t5 += MAS[1]

	t9_t3 = S.Task('t9_t3', length=4, delay_cost=1)
	S += t9_t3 >= 16
	t9_t3 += MM[0]

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	S += c210_w >= 17
	c210_w += MAIN_MEM_w

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 17
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 17
	t0_t2_in += MM_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 17
	t0_t2_mem0 += MAS_MEM[2]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 17
	t0_t2_mem1 += MAS_MEM[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 17
	t0_t3_mem0 += MAIN_MEM_r[0]

	t230 = S.Task('t230', length=2, delay_cost=1)
	S += t230 >= 17
	t230 += MAS[0]

	t261 = S.Task('t261', length=2, delay_cost=1)
	S += t261 >= 17
	t261 += MAS[2]

	t300_in = S.Task('t300_in', length=1, delay_cost=1)
	S += t300_in >= 17
	t300_in += MAS_in[1]

	t300_mem0 = S.Task('t300_mem0', length=1, delay_cost=1)
	S += t300_mem0 >= 17
	t300_mem0 += MAS_MEM[4]

	t300_mem1 = S.Task('t300_mem1', length=1, delay_cost=1)
	S += t300_mem1 >= 17
	t300_mem1 += MAS_MEM[5]

	t3_t5 = S.Task('t3_t5', length=2, delay_cost=1)
	S += t3_t5 >= 17
	t3_t5 += MAS[3]

	t4_t2 = S.Task('t4_t2', length=4, delay_cost=1)
	S += t4_t2 >= 17
	t4_t2 += MM[0]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 17
	t51_in += MAS_in[0]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 17
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 17
	t51_mem1 += MAS_MEM[3]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 18
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t2 = S.Task('t0_t2', length=4, delay_cost=1)
	S += t0_t2 >= 18
	t0_t2 += MM[0]

	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	S += t10_t2_in >= 18
	t10_t2_in += MM_in[0]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 18
	t10_t2_mem0 += MAS_MEM[0]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 18
	t10_t2_mem1 += MAS_MEM[1]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 18
	t161_in += MAS_in[0]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 18
	t161_mem0 += MAS_MEM[4]

	t300 = S.Task('t300', length=2, delay_cost=1)
	S += t300 >= 18
	t300 += MAS[1]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 18
	t31_in += MAS_in[3]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 18
	t31_mem0 += MM_MEM[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 18
	t31_mem1 += MAS_MEM[7]

	t51 = S.Task('t51', length=2, delay_cost=1)
	S += t51 >= 18
	t51 += MAS[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 18
	t7_t1_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 19
	t10_mem1 += MAIN_MEM_r[1]

	t10_t2 = S.Task('t10_t2', length=4, delay_cost=1)
	S += t10_t2 >= 19
	t10_t2 += MM[0]

	t161 = S.Task('t161', length=2, delay_cost=1)
	S += t161 >= 19
	t161 += MAS[0]

	t271_in = S.Task('t271_in', length=1, delay_cost=1)
	S += t271_in >= 19
	t271_in += MAS_in[1]

	t271_mem0 = S.Task('t271_mem0', length=1, delay_cost=1)
	S += t271_mem0 >= 19
	t271_mem0 += MAS_MEM[4]

	t271_mem1 = S.Task('t271_mem1', length=1, delay_cost=1)
	S += t271_mem1 >= 19
	t271_mem1 += MAS_MEM[7]

	t291_in = S.Task('t291_in', length=1, delay_cost=1)
	S += t291_in >= 19
	t291_in += MAS_in[2]

	t291_mem0 = S.Task('t291_mem0', length=1, delay_cost=1)
	S += t291_mem0 >= 19
	t291_mem0 += MAS_MEM[0]

	t31 = S.Task('t31', length=2, delay_cost=1)
	S += t31 >= 19
	t31 += MAS[3]

	t310_in = S.Task('t310_in', length=1, delay_cost=1)
	S += t310_in >= 19
	t310_in += MAS_in[0]

	t310_mem0 = S.Task('t310_mem0', length=1, delay_cost=1)
	S += t310_mem0 >= 19
	t310_mem0 += MAS_MEM[2]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 19
	t4_t3_mem0 += MAIN_MEM_r[0]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 19
	t61_in += MAS_in[3]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 19
	t61_mem0 += MM_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 19
	t61_mem1 += MAS_MEM[5]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 19
	t9_t2_in += MM_in[0]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 19
	t9_t2_mem0 += MAS_MEM[6]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 19
	t9_t2_mem1 += MAS_MEM[3]

	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	S += t111_in >= 20
	t111_in += MAS_in[3]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 20
	t111_mem0 += MAS_MEM[6]

	t271 = S.Task('t271', length=2, delay_cost=1)
	S += t271 >= 20
	t271 += MAS[1]

	t291 = S.Task('t291', length=2, delay_cost=1)
	S += t291 >= 20
	t291 += MAS[2]

	t310 = S.Task('t310', length=2, delay_cost=1)
	S += t310 >= 20
	t310 += MAS[0]

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	S += t3_t3_mem0 >= 20
	t3_t3_mem0 += MAIN_MEM_r[0]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 20
	t4_t5_in += MAS_in[1]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 20
	t4_t5_mem0 += MM_MEM[0]

	t61 = S.Task('t61', length=2, delay_cost=1)
	S += t61 >= 20
	t61 += MAS[3]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 20
	t6_t3_mem1 += MAIN_MEM_r[1]

	t9_t2 = S.Task('t9_t2', length=4, delay_cost=1)
	S += t9_t2 >= 20
	t9_t2 += MM[0]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 21
	c010_in += MAS_in[2]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 21
	c010_mem0 += MAS_MEM[0]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 21
	t0_t5_in += MAS_in[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 21
	t0_t5_mem0 += MM_MEM[0]

	t111 = S.Task('t111', length=2, delay_cost=1)
	S += t111 >= 21
	t111 += MAS[3]

	t221_in = S.Task('t221_in', length=1, delay_cost=1)
	S += t221_in >= 21
	t221_in += MAS_in[1]

	t221_mem0 = S.Task('t221_mem0', length=1, delay_cost=1)
	S += t221_mem0 >= 21
	t221_mem0 += MAS_MEM[6]

	t301_in = S.Task('t301_in', length=1, delay_cost=1)
	S += t301_in >= 21
	t301_in += MAS_in[3]

	t301_mem0 = S.Task('t301_mem0', length=1, delay_cost=1)
	S += t301_mem0 >= 21
	t301_mem0 += MAS_MEM[4]

	t301_mem1 = S.Task('t301_mem1', length=1, delay_cost=1)
	S += t301_mem1 >= 21
	t301_mem1 += MAS_MEM[1]

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	S += t3_t2_mem0 >= 21
	t3_t2_mem0 += MAIN_MEM_r[0]

	t4_t5 = S.Task('t4_t5', length=2, delay_cost=1)
	S += t4_t5 >= 21
	t4_t5 += MAS[1]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 21
	t7_t3_mem1 += MAIN_MEM_r[1]

	c010 = S.Task('c010', length=2, delay_cost=1)
	S += c010 >= 22
	c010 += MAS[2]

	t0_t5 = S.Task('t0_t5', length=2, delay_cost=1)
	S += t0_t5 >= 22
	t0_t5 += MAS[0]

	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	S += t120_in >= 22
	t120_in += MAS_in[1]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 22
	t120_mem0 += MAS_MEM[4]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 22
	t120_mem1 += MAS_MEM[7]

	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	S += t121_in >= 22
	t121_in += MAS_in[0]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 22
	t121_mem0 += MAS_MEM[6]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 22
	t121_mem1 += MAS_MEM[5]

	t221 = S.Task('t221', length=2, delay_cost=1)
	S += t221 >= 22
	t221 += MAS[1]

	t281_in = S.Task('t281_in', length=1, delay_cost=1)
	S += t281_in >= 22
	t281_in += MAS_in[3]

	t281_mem0 = S.Task('t281_mem0', length=1, delay_cost=1)
	S += t281_mem0 >= 22
	t281_mem0 += MAS_MEM[2]

	t301 = S.Task('t301', length=2, delay_cost=1)
	S += t301 >= 22
	t301 += MAS[3]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 22
	t40_in += MAS_in[2]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 22
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 22
	t40_mem1 += MAS_MEM[3]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 22
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 22
	t7_t0_mem1 += MAIN_MEM_r[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 23
	t00_in += MAS_in[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 23
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 23
	t00_mem1 += MAS_MEM[1]

	t120 = S.Task('t120', length=2, delay_cost=1)
	S += t120 >= 23
	t120 += MAS[1]

	t121 = S.Task('t121', length=2, delay_cost=1)
	S += t121 >= 23
	t121 += MAS[0]

	t231_in = S.Task('t231_in', length=1, delay_cost=1)
	S += t231_in >= 23
	t231_in += MAS_in[3]

	t231_mem0 = S.Task('t231_mem0', length=1, delay_cost=1)
	S += t231_mem0 >= 23
	t231_mem0 += MAS_MEM[2]

	t231_mem1 = S.Task('t231_mem1', length=1, delay_cost=1)
	S += t231_mem1 >= 23
	t231_mem1 += MAS_MEM[7]

	t281 = S.Task('t281', length=2, delay_cost=1)
	S += t281 >= 23
	t281 += MAS[3]

	t311_in = S.Task('t311_in', length=1, delay_cost=1)
	S += t311_in >= 23
	t311_in += MAS_in[2]

	t311_mem0 = S.Task('t311_mem0', length=1, delay_cost=1)
	S += t311_mem0 >= 23
	t311_mem0 += MAS_MEM[6]

	t40 = S.Task('t40', length=2, delay_cost=1)
	S += t40 >= 23
	t40 += MAS[2]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 23
	t5_t3_mem0 += MAIN_MEM_r[0]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 23
	t6_t2_mem1 += MAIN_MEM_r[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 24
	c010_w += MAIN_MEM_w

	t00 = S.Task('t00', length=2, delay_cost=1)
	S += t00 >= 24
	t00 += MAS[1]

	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	S += t131_in >= 24
	t131_in += MAS_in[1]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 24
	t131_mem0 += MAS_MEM[2]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 24
	t131_mem1 += MAS_MEM[1]

	t181_in = S.Task('t181_in', length=1, delay_cost=1)
	S += t181_in >= 24
	t181_in += MAS_in[2]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 24
	t181_mem0 += MAS_MEM[4]

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	S += t181_mem1 >= 24
	t181_mem1 += MAS_MEM[5]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 24
	t21_mem1 += MAIN_MEM_r[1]

	t231 = S.Task('t231', length=2, delay_cost=1)
	S += t231 >= 24
	t231 += MAS[3]

	t311 = S.Task('t311', length=2, delay_cost=1)
	S += t311 >= 24
	t311 += MAS[2]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 24
	t91_in += MAS_in[3]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 24
	t91_mem0 += MM_MEM[0]

	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	S += t130_in >= 25
	t130_in += MAS_in[3]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 25
	t130_mem0 += MAS_MEM[2]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 25
	t130_mem1 += MAS_MEM[3]

	t131 = S.Task('t131', length=2, delay_cost=1)
	S += t131 >= 25
	t131 += MAS[1]

	t180_in = S.Task('t180_in', length=1, delay_cost=1)
	S += t180_in >= 25
	t180_in += MAS_in[2]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 25
	t180_mem0 += MAS_MEM[4]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 25
	t180_mem1 += MAS_MEM[5]

	t181 = S.Task('t181', length=2, delay_cost=1)
	S += t181 >= 25
	t181 += MAS[2]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 25
	t20_mem1 += MAIN_MEM_r[1]

	t241_in = S.Task('t241_in', length=1, delay_cost=1)
	S += t241_in >= 25
	t241_in += MAS_in[0]

	t241_mem0 = S.Task('t241_mem0', length=1, delay_cost=1)
	S += t241_mem0 >= 25
	t241_mem0 += MAS_MEM[6]

	t241_mem1 = S.Task('t241_mem1', length=1, delay_cost=1)
	S += t241_mem1 >= 25
	t241_mem1 += MAS_MEM[1]

	t91 = S.Task('t91', length=2, delay_cost=1)
	S += t91 >= 25
	t91 += MAS[3]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 26
	t101_in += MAS_in[3]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 26
	t101_mem0 += MM_MEM[0]

	t130 = S.Task('t130', length=2, delay_cost=1)
	S += t130 >= 26
	t130 += MAS[3]

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 26
	t150_in += MAS_in[2]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 26
	t150_mem0 += MAS_MEM[2]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 26
	t150_mem1 += MAS_MEM[5]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 26
	t171_in += MAS_in[0]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 26
	t171_mem0 += MAS_MEM[6]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 26
	t171_mem1 += MAS_MEM[1]

	t180 = S.Task('t180', length=2, delay_cost=1)
	S += t180 >= 26
	t180 += MAS[2]

	t191_in = S.Task('t191_in', length=1, delay_cost=1)
	S += t191_in >= 26
	t191_in += MAS_in[1]

	t191_mem0 = S.Task('t191_mem0', length=1, delay_cost=1)
	S += t191_mem0 >= 26
	t191_mem0 += MAS_MEM[4]

	t191_mem1 = S.Task('t191_mem1', length=1, delay_cost=1)
	S += t191_mem1 >= 26
	t191_mem1 += MAS_MEM[7]

	t241 = S.Task('t241', length=2, delay_cost=1)
	S += t241 >= 26
	t241 += MAS[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 26
	t81_mem1 += MAIN_MEM_r[1]

	t101 = S.Task('t101', length=2, delay_cost=1)
	S += t101 >= 27
	t101 += MAS[3]

	t10_t5_in = S.Task('t10_t5_in', length=1, delay_cost=1)
	S += t10_t5_in >= 27
	t10_t5_in += MAS_in[1]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 27
	t10_t5_mem0 += MM_MEM[0]

	t150 = S.Task('t150', length=2, delay_cost=1)
	S += t150 >= 27
	t150 += MAS[2]

	t171 = S.Task('t171', length=2, delay_cost=1)
	S += t171 >= 27
	t171 += MAS[0]

	t190_in = S.Task('t190_in', length=1, delay_cost=1)
	S += t190_in >= 27
	t190_in += MAS_in[2]

	t190_mem0 = S.Task('t190_mem0', length=1, delay_cost=1)
	S += t190_mem0 >= 27
	t190_mem0 += MAS_MEM[4]

	t190_mem1 = S.Task('t190_mem1', length=1, delay_cost=1)
	S += t190_mem1 >= 27
	t190_mem1 += MAS_MEM[5]

	t191 = S.Task('t191', length=2, delay_cost=1)
	S += t191 >= 27
	t191 += MAS[1]

	t240_in = S.Task('t240_in', length=1, delay_cost=1)
	S += t240_in >= 27
	t240_in += MAS_in[0]

	t240_mem0 = S.Task('t240_mem0', length=1, delay_cost=1)
	S += t240_mem0 >= 27
	t240_mem0 += MAS_MEM[0]

	t240_mem1 = S.Task('t240_mem1', length=1, delay_cost=1)
	S += t240_mem1 >= 27
	t240_mem1 += MAS_MEM[7]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 27
	t80_mem1 += MAIN_MEM_r[1]

	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	S += c111_in >= 28
	c111_in += MAS_in[3]

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	S += c111_mem0 >= 28
	c111_mem0 += MAS_MEM[6]

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	S += c111_mem1 >= 28
	c111_mem1 += MAS_MEM[1]

	t10_t5 = S.Task('t10_t5', length=2, delay_cost=1)
	S += t10_t5 >= 28
	t10_t5 += MAS[1]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 28
	t160_in += MAS_in[1]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 28
	t160_mem0 += MAS_MEM[4]

	t190 = S.Task('t190', length=2, delay_cost=1)
	S += t190 >= 28
	t190 += MAS[2]

	t201_in = S.Task('t201_in', length=1, delay_cost=1)
	S += t201_in >= 28
	t201_in += MAS_in[0]

	t201_mem0 = S.Task('t201_mem0', length=1, delay_cost=1)
	S += t201_mem0 >= 28
	t201_mem0 += MAS_MEM[2]

	t240 = S.Task('t240', length=2, delay_cost=1)
	S += t240 >= 28
	t240 += MAS[0]

	t311_mem1 = S.Task('t311_mem1', length=1, delay_cost=1)
	S += t311_mem1 >= 28
	t311_mem1 += MAIN_MEM_r[1]

	c111 = S.Task('c111', length=2, delay_cost=1)
	S += c111 >= 29
	c111 += MAS[3]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 29
	t100_in += MAS_in[1]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 29
	t100_mem0 += MM_MEM[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 29
	t100_mem1 += MAS_MEM[3]

	t160 = S.Task('t160', length=2, delay_cost=1)
	S += t160 >= 29
	t160 += MAS[1]

	t200_in = S.Task('t200_in', length=1, delay_cost=1)
	S += t200_in >= 29
	t200_in += MAS_in[3]

	t200_mem0 = S.Task('t200_mem0', length=1, delay_cost=1)
	S += t200_mem0 >= 29
	t200_mem0 += MAS_MEM[4]

	t201 = S.Task('t201', length=2, delay_cost=1)
	S += t201 >= 29
	t201 += MAS[0]

	t280_mem1 = S.Task('t280_mem1', length=1, delay_cost=1)
	S += t280_mem1 >= 29
	t280_mem1 += MAIN_MEM_r[1]

	t100 = S.Task('t100', length=2, delay_cost=1)
	S += t100 >= 30
	t100 += MAS[1]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 30
	t170_in += MAS_in[2]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 30
	t170_mem0 += MAS_MEM[4]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 30
	t170_mem1 += MAS_MEM[3]

	t200 = S.Task('t200', length=2, delay_cost=1)
	S += t200 >= 30
	t200 += MAS[3]

	t281_mem1 = S.Task('t281_mem1', length=1, delay_cost=1)
	S += t281_mem1 >= 30
	t281_mem1 += MAIN_MEM_r[1]

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	S += c111_w >= 31
	c111_w += MAIN_MEM_w

	t170 = S.Task('t170', length=2, delay_cost=1)
	S += t170 >= 31
	t170 += MAS[2]

	t310_mem1 = S.Task('t310_mem1', length=1, delay_cost=1)
	S += t310_mem1 >= 31
	t310_mem1 += MAIN_MEM_r[1]


	# new tasks
	t9_t5 = S.Task('t9_t5', length=2, delay_cost=1)
	t9_t5 += alt(MAS)
	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	t9_t5_in += alt(MAS_in)
	S += t9_t5_in*MAS_in[0]<=t9_t5*MAS[0]

	S += t9_t5_in*MAS_in[1]<=t9_t5*MAS[1]

	S += t9_t5_in*MAS_in[2]<=t9_t5*MAS[2]

	S += t9_t5_in*MAS_in[3]<=t9_t5*MAS[3]

	S += t9_t5<29

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	t9_t5_mem0 += MM_MEM[0]
	S += 19 < t9_t5_mem0
	S += t9_t5_mem0 <= t9_t5

	t90 = S.Task('t90', length=2, delay_cost=1)
	t90 += alt(MAS)
	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	t90_in += alt(MAS_in)
	S += t90_in*MAS_in[0]<=t90*MAS[0]

	S += t90_in*MAS_in[1]<=t90*MAS[1]

	S += t90_in*MAS_in[2]<=t90*MAS[2]

	S += t90_in*MAS_in[3]<=t90*MAS[3]

	S += t90<31

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += MM_MEM[0]
	S += 23 < t90_mem0
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += alt(MAS_MEM)
	S += (t9_t5*MAS[0])-1 < t90_mem1*MAS_MEM[1]
	S += (t9_t5*MAS[1])-1 < t90_mem1*MAS_MEM[3]
	S += (t9_t5*MAS[2])-1 < t90_mem1*MAS_MEM[5]
	S += (t9_t5*MAS[3])-1 < t90_mem1*MAS_MEM[7]
	S += t90_mem1 <= t90

	t140 = S.Task('t140', length=2, delay_cost=1)
	t140 += alt(MAS)
	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	t140_in += alt(MAS_in)
	S += t140_in*MAS_in[0]<=t140*MAS[0]

	S += t140_in*MAS_in[1]<=t140*MAS[1]

	S += t140_in*MAS_in[2]<=t140*MAS[2]

	S += t140_in*MAS_in[3]<=t140*MAS[3]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += MAS_MEM[6]
	S += 27 < t140_mem0
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += MAIN_MEM_r[1]
	c001 = S.Task('c001', length=2, delay_cost=1)
	c001 += alt(MAS)
	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	c001_in += alt(MAS_in)
	S += c001_in*MAS_in[0]<=c001*MAS[0]

	S += c001_in*MAS_in[1]<=c001*MAS[1]

	S += c001_in*MAS_in[2]<=c001*MAS[2]

	S += c001_in*MAS_in[3]<=c001*MAS[3]

	S += 10<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[2]
	S += 26 < c001_mem0
	S += c001_mem0 <= c001

	c011 = S.Task('c011', length=2, delay_cost=1)
	c011 += alt(MAS)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MAS_in)
	S += c011_in*MAS_in[0]<=c011*MAS[0]

	S += c011_in*MAS_in[1]<=c011*MAS[1]

	S += c011_in*MAS_in[2]<=c011*MAS[2]

	S += c011_in*MAS_in[3]<=c011*MAS[3]

	S += 24<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MAS_MEM[4]
	S += 25 < c011_mem0
	S += c011_mem0 <= c011

	c110 = S.Task('c110', length=2, delay_cost=1)
	c110 += alt(MAS)
	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	c110_in += alt(MAS_in)
	S += c110_in*MAS_in[0]<=c110*MAS[0]

	S += c110_in*MAS_in[1]<=c110*MAS[1]

	S += c110_in*MAS_in[2]<=c110*MAS[2]

	S += c110_in*MAS_in[3]<=c110*MAS[3]

	S += 8<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[2]
	S += 31 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MAS_MEM[5]
	S += 32 < c110_mem1
	S += c110_mem1 <= c110

	t210 = S.Task('t210', length=2, delay_cost=1)
	t210 += alt(MAS)
	t210_in = S.Task('t210_in', length=1, delay_cost=1)
	t210_in += alt(MAS_in)
	S += t210_in*MAS_in[0]<=t210*MAS[0]

	S += t210_in*MAS_in[1]<=t210*MAS[1]

	S += t210_in*MAS_in[2]<=t210*MAS[2]

	S += t210_in*MAS_in[3]<=t210*MAS[3]

	t210_mem0 = S.Task('t210_mem0', length=1, delay_cost=1)
	t210_mem0 += MAS_MEM[6]
	S += 31 < t210_mem0
	S += t210_mem0 <= t210

	t210_mem1 = S.Task('t210_mem1', length=1, delay_cost=1)
	t210_mem1 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t210_mem1*MAS_MEM[1]
	S += (t90*MAS[1])-1 < t210_mem1*MAS_MEM[3]
	S += (t90*MAS[2])-1 < t210_mem1*MAS_MEM[5]
	S += (t90*MAS[3])-1 < t210_mem1*MAS_MEM[7]
	S += t210_mem1 <= t210

	t211 = S.Task('t211', length=2, delay_cost=1)
	t211 += alt(MAS)
	t211_in = S.Task('t211_in', length=1, delay_cost=1)
	t211_in += alt(MAS_in)
	S += t211_in*MAS_in[0]<=t211*MAS[0]

	S += t211_in*MAS_in[1]<=t211*MAS[1]

	S += t211_in*MAS_in[2]<=t211*MAS[2]

	S += t211_in*MAS_in[3]<=t211*MAS[3]

	t211_mem0 = S.Task('t211_mem0', length=1, delay_cost=1)
	t211_mem0 += MAS_MEM[0]
	S += 30 < t211_mem0
	S += t211_mem0 <= t211

	t211_mem1 = S.Task('t211_mem1', length=1, delay_cost=1)
	t211_mem1 += MAS_MEM[7]
	S += 26 < t211_mem1
	S += t211_mem1 <= t211

	t250 = S.Task('t250', length=2, delay_cost=1)
	t250 += alt(MAS)
	t250_in = S.Task('t250_in', length=1, delay_cost=1)
	t250_in += alt(MAS_in)
	S += t250_in*MAS_in[0]<=t250*MAS[0]

	S += t250_in*MAS_in[1]<=t250*MAS[1]

	S += t250_in*MAS_in[2]<=t250*MAS[2]

	S += t250_in*MAS_in[3]<=t250*MAS[3]

	t250_mem0 = S.Task('t250_mem0', length=1, delay_cost=1)
	t250_mem0 += MAIN_MEM_r[0]
	t250_mem1 = S.Task('t250_mem1', length=1, delay_cost=1)
	t250_mem1 += MAS_MEM[1]
	S += 29 < t250_mem1
	S += t250_mem1 <= t250

	t251 = S.Task('t251', length=2, delay_cost=1)
	t251 += alt(MAS)
	t251_in = S.Task('t251_in', length=1, delay_cost=1)
	t251_in += alt(MAS_in)
	S += t251_in*MAS_in[0]<=t251*MAS[0]

	S += t251_in*MAS_in[1]<=t251*MAS[1]

	S += t251_in*MAS_in[2]<=t251*MAS[2]

	S += t251_in*MAS_in[3]<=t251*MAS[3]

	t251_mem0 = S.Task('t251_mem0', length=1, delay_cost=1)
	t251_mem0 += MAIN_MEM_r[0]
	t251_mem1 = S.Task('t251_mem1', length=1, delay_cost=1)
	t251_mem1 += MAS_MEM[1]
	S += 27 < t251_mem1
	S += t251_mem1 <= t251

	c211 = S.Task('c211', length=2, delay_cost=1)
	c211 += alt(MAS)
	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	c211_in += alt(MAS_in)
	S += c211_in*MAS_in[0]<=c211*MAS[0]

	S += c211_in*MAS_in[1]<=c211*MAS[1]

	S += c211_in*MAS_in[2]<=c211*MAS[2]

	S += c211_in*MAS_in[3]<=c211*MAS[3]

	S += 23<c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += MAS_MEM[6]
	S += 24 < c211_mem0
	S += c211_mem0 <= c211

	c000 = S.Task('c000', length=2, delay_cost=1)
	c000 += alt(MAS)
	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	c000_in += alt(MAS_in)
	S += c000_in*MAS_in[0]<=c000*MAS[0]

	S += c000_in*MAS_in[1]<=c000*MAS[1]

	S += c000_in*MAS_in[2]<=c000*MAS[2]

	S += c000_in*MAS_in[3]<=c000*MAS[3]

	S += 9<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[6]
	S += 27 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (t140*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (t140*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (t140*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += c000_mem1 <= c000

	c200 = S.Task('c200', length=2, delay_cost=1)
	c200 += alt(MAS)
	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MAS_in)
	S += c200_in*MAS_in[0]<=c200*MAS[0]

	S += c200_in*MAS_in[1]<=c200*MAS[1]

	S += c200_in*MAS_in[2]<=c200*MAS[2]

	S += c200_in*MAS_in[3]<=c200*MAS[3]

	S += 7<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(MAS_MEM)
	S += (t210*MAS[0])-1 < c200_mem0*MAS_MEM[0]
	S += (t210*MAS[1])-1 < c200_mem0*MAS_MEM[2]
	S += (t210*MAS[2])-1 < c200_mem0*MAS_MEM[4]
	S += (t210*MAS[3])-1 < c200_mem0*MAS_MEM[6]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAS_MEM[3]
	S += 31 < c200_mem1
	S += c200_mem1 <= c200

	c201 = S.Task('c201', length=2, delay_cost=1)
	c201 += alt(MAS)
	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MAS_in)
	S += c201_in*MAS_in[0]<=c201*MAS[0]

	S += c201_in*MAS_in[1]<=c201*MAS[1]

	S += c201_in*MAS_in[2]<=c201*MAS[2]

	S += c201_in*MAS_in[3]<=c201*MAS[3]

	S += 7<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MAS_MEM)
	S += (t211*MAS[0])-1 < c201_mem0*MAS_MEM[0]
	S += (t211*MAS[1])-1 < c201_mem0*MAS_MEM[2]
	S += (t211*MAS[2])-1 < c201_mem0*MAS_MEM[4]
	S += (t211*MAS[3])-1 < c201_mem0*MAS_MEM[6]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += MAS_MEM[7]
	S += 28 < c201_mem1
	S += c201_mem1 <= c201

	c100 = S.Task('c100', length=2, delay_cost=1)
	c100 += alt(MAS)
	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	c100_in += alt(MAS_in)
	S += c100_in*MAS_in[0]<=c100*MAS[0]

	S += c100_in*MAS_in[1]<=c100*MAS[1]

	S += c100_in*MAS_in[2]<=c100*MAS[2]

	S += c100_in*MAS_in[3]<=c100*MAS[3]

	S += 3<c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(MAS_MEM)
	S += (t250*MAS[0])-1 < c100_mem0*MAS_MEM[0]
	S += (t250*MAS[1])-1 < c100_mem0*MAS_MEM[2]
	S += (t250*MAS[2])-1 < c100_mem0*MAS_MEM[4]
	S += (t250*MAS[3])-1 < c100_mem0*MAS_MEM[6]
	S += c100_mem0 <= c100

	c101 = S.Task('c101', length=2, delay_cost=1)
	c101 += alt(MAS)
	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	c101_in += alt(MAS_in)
	S += c101_in*MAS_in[0]<=c101*MAS[0]

	S += c101_in*MAS_in[1]<=c101*MAS[1]

	S += c101_in*MAS_in[2]<=c101*MAS[2]

	S += c101_in*MAS_in[3]<=c101*MAS[3]

	S += 1<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MAS_MEM)
	S += (t251*MAS[0])-1 < c101_mem0*MAS_MEM[0]
	S += (t251*MAS[1])-1 < c101_mem0*MAS_MEM[2]
	S += (t251*MAS[2])-1 < c101_mem0*MAS_MEM[4]
	S += (t251*MAS[3])-1 < c101_mem0*MAS_MEM[6]
	S += c101_mem0 <= c101

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage2MAS4/SQR012345/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

