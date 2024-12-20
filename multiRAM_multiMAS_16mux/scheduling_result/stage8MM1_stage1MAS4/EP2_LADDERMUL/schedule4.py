from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 201
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	S += T7_t0_in >= 0
	T7_t0_in += MM_in[0]

	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	S += T7_t0_mem0 >= 0
	T7_t0_mem0 += MAIN_MEM_r[0]

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	S += T7_t0_mem1 >= 0
	T7_t0_mem1 += MAIN_MEM_r[1]

	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	S += T5_t3_in >= 1
	T5_t3_in += MM_in[0]

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	S += T5_t3_mem0 >= 1
	T5_t3_mem0 += MAIN_MEM_r[0]

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	S += T5_t3_mem1 >= 1
	T5_t3_mem1 += MAIN_MEM_r[1]

	T7_t0 = S.Task('T7_t0', length=8, delay_cost=1)
	S += T7_t0 >= 1
	T7_t0 += MM[0]

	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	S += T4_t0_in >= 2
	T4_t0_in += MM_in[0]

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	S += T4_t0_mem0 >= 2
	T4_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	S += T4_t0_mem1 >= 2
	T4_t0_mem1 += MAIN_MEM_r[1]

	T5_t3 = S.Task('T5_t3', length=8, delay_cost=1)
	S += T5_t3 >= 2
	T5_t3 += MM[0]

	T4_t0 = S.Task('T4_t0', length=8, delay_cost=1)
	S += T4_t0 >= 3
	T4_t0 += MM[0]

	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	S += T6_t0_in >= 3
	T6_t0_in += MM_in[0]

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	S += T6_t0_mem0 >= 3
	T6_t0_mem0 += MAIN_MEM_r[0]

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	S += T6_t0_mem1 >= 3
	T6_t0_mem1 += MAIN_MEM_r[1]

	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	S += T3_t1_in >= 4
	T3_t1_in += MM_in[0]

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	S += T3_t1_mem0 >= 4
	T3_t1_mem0 += MAIN_MEM_r[0]

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	S += T3_t1_mem1 >= 4
	T3_t1_mem1 += MAIN_MEM_r[1]

	T6_t0 = S.Task('T6_t0', length=8, delay_cost=1)
	S += T6_t0 >= 4
	T6_t0 += MM[0]

	T3_t1 = S.Task('T3_t1', length=8, delay_cost=1)
	S += T3_t1 >= 5
	T3_t1 += MM[0]

	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	S += T6_t1_in >= 5
	T6_t1_in += MM_in[0]

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	S += T6_t1_mem0 >= 5
	T6_t1_mem0 += MAIN_MEM_r[0]

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	S += T6_t1_mem1 >= 5
	T6_t1_mem1 += MAIN_MEM_r[1]

	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	S += T3_t0_in >= 6
	T3_t0_in += MM_in[0]

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	S += T3_t0_mem0 >= 6
	T3_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	S += T3_t0_mem1 >= 6
	T3_t0_mem1 += MAIN_MEM_r[1]

	T6_t1 = S.Task('T6_t1', length=8, delay_cost=1)
	S += T6_t1 >= 6
	T6_t1 += MM[0]

	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	S += T2_t1_in >= 7
	T2_t1_in += MM_in[0]

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	S += T2_t1_mem0 >= 7
	T2_t1_mem0 += MAIN_MEM_r[0]

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	S += T2_t1_mem1 >= 7
	T2_t1_mem1 += MAIN_MEM_r[1]

	T3_t0 = S.Task('T3_t0', length=8, delay_cost=1)
	S += T3_t0 >= 7
	T3_t0 += MM[0]

	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	S += T2_t0_in >= 8
	T2_t0_in += MM_in[0]

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	S += T2_t0_mem0 >= 8
	T2_t0_mem0 += MAIN_MEM_r[0]

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	S += T2_t0_mem1 >= 8
	T2_t0_mem1 += MAIN_MEM_r[1]

	T2_t1 = S.Task('T2_t1', length=8, delay_cost=1)
	S += T2_t1 >= 8
	T2_t1 += MM[0]

	T2_t0 = S.Task('T2_t0', length=8, delay_cost=1)
	S += T2_t0 >= 9
	T2_t0 += MM[0]

	T5_t5_mem0 = S.Task('T5_t5_mem0', length=1, delay_cost=1)
	S += T5_t5_mem0 >= 9
	T5_t5_mem0 += MM_MEM[0]

	T5_t5_mem1 = S.Task('T5_t5_mem1', length=1, delay_cost=1)
	S += T5_t5_mem1 >= 9
	T5_t5_mem1 += MM_MEM[1]

	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	S += T7_t1_in >= 9
	T7_t1_in += MM_in[0]

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	S += T7_t1_mem0 >= 9
	T7_t1_mem0 += MAIN_MEM_r[0]

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	S += T7_t1_mem1 >= 9
	T7_t1_mem1 += MAIN_MEM_r[1]

	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	S += T4_t1_in >= 10
	T4_t1_in += MM_in[0]

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	S += T4_t1_mem0 >= 10
	T4_t1_mem0 += MAIN_MEM_r[0]

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	S += T4_t1_mem1 >= 10
	T4_t1_mem1 += MAIN_MEM_r[1]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 10
	T51_mem0 += MM_MEM[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 10
	T51_mem1 += MM_MEM[1]

	T5_t5 = S.Task('T5_t5', length=1, delay_cost=1)
	S += T5_t5 >= 10
	T5_t5 += MAS[3]

	T7_t1 = S.Task('T7_t1', length=8, delay_cost=1)
	S += T7_t1 >= 10
	T7_t1 += MM[0]

	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	S += T1_t3_in >= 11
	T1_t3_in += MM_in[0]

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	S += T1_t3_mem0 >= 11
	T1_t3_mem0 += MAIN_MEM_r[0]

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	S += T1_t3_mem1 >= 11
	T1_t3_mem1 += MAIN_MEM_r[1]

	T4_t1 = S.Task('T4_t1', length=8, delay_cost=1)
	S += T4_t1 >= 11
	T4_t1 += MM[0]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 11
	T51 += MAS[0]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	S += T11_t2_mem0 >= 12
	T11_t2_mem0 += MAIN_MEM_r[0]

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	S += T11_t2_mem1 >= 12
	T11_t2_mem1 += MAIN_MEM_r[1]

	T1_t3 = S.Task('T1_t3', length=8, delay_cost=1)
	S += T1_t3 >= 12
	T1_t3 += MM[0]

	T11_t2 = S.Task('T11_t2', length=1, delay_cost=1)
	S += T11_t2 >= 13
	T11_t2 += MAS[3]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	S += T4_t2_mem0 >= 13
	T4_t2_mem0 += MAIN_MEM_r[0]

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	S += T4_t2_mem1 >= 13
	T4_t2_mem1 += MAIN_MEM_r[1]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 13
	T60_mem0 += MM_MEM[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 13
	T60_mem1 += MM_MEM[1]

	T3_t5_mem0 = S.Task('T3_t5_mem0', length=1, delay_cost=1)
	S += T3_t5_mem0 >= 14
	T3_t5_mem0 += MM_MEM[0]

	T3_t5_mem1 = S.Task('T3_t5_mem1', length=1, delay_cost=1)
	S += T3_t5_mem1 >= 14
	T3_t5_mem1 += MM_MEM[1]

	T4_t2 = S.Task('T4_t2', length=1, delay_cost=1)
	S += T4_t2 >= 14
	T4_t2 += MAS[0]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	S += T4_t3_mem0 >= 14
	T4_t3_mem0 += MAIN_MEM_r[0]

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	S += T4_t3_mem1 >= 14
	T4_t3_mem1 += MAIN_MEM_r[1]

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 14
	T60 += MAS[2]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 15
	T30_mem0 += MM_MEM[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 15
	T30_mem1 += MM_MEM[1]

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	S += T3_t3_mem0 >= 15
	T3_t3_mem0 += MAIN_MEM_r[0]

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	S += T3_t3_mem1 >= 15
	T3_t3_mem1 += MAIN_MEM_r[1]

	T3_t5 = S.Task('T3_t5', length=1, delay_cost=1)
	S += T3_t5 >= 15
	T3_t5 += MAS[2]

	T4_t3 = S.Task('T4_t3', length=1, delay_cost=1)
	S += T4_t3 >= 15
	T4_t3 += MAS[0]

	T4_t4_in = S.Task('T4_t4_in', length=1, delay_cost=1)
	S += T4_t4_in >= 15
	T4_t4_in += MM_in[0]

	T4_t4_mem0 = S.Task('T4_t4_mem0', length=1, delay_cost=1)
	S += T4_t4_mem0 >= 15
	T4_t4_mem0 += MAS_MEM[0]

	T4_t4_mem1 = S.Task('T4_t4_mem1', length=1, delay_cost=1)
	S += T4_t4_mem1 >= 15
	T4_t4_mem1 += MAS_MEM[1]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	S += T1_t0_mem0 >= 16
	T1_t0_mem0 += MAIN_MEM_r[0]

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	S += T1_t0_mem1 >= 16
	T1_t0_mem1 += MAIN_MEM_r[1]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 16
	T20_mem0 += MM_MEM[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 16
	T20_mem1 += MM_MEM[1]

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 16
	T30 += MAS[1]

	T3_t3 = S.Task('T3_t3', length=1, delay_cost=1)
	S += T3_t3 >= 16
	T3_t3 += MAS[0]

	T4_t4 = S.Task('T4_t4', length=8, delay_cost=1)
	S += T4_t4 >= 16
	T4_t4 += MM[0]

	T1_t0 = S.Task('T1_t0', length=1, delay_cost=1)
	S += T1_t0 >= 17
	T1_t0 += MAS[3]

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 17
	T20 += MAS[0]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	S += T2_t3_mem0 >= 17
	T2_t3_mem0 += MAIN_MEM_r[0]

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	S += T2_t3_mem1 >= 17
	T2_t3_mem1 += MAIN_MEM_r[1]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 17
	T70_mem0 += MM_MEM[0]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 17
	T70_mem1 += MM_MEM[1]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	S += T10_t2_mem0 >= 18
	T10_t2_mem0 += MAIN_MEM_r[0]

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	S += T10_t2_mem1 >= 18
	T10_t2_mem1 += MAIN_MEM_r[1]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 18
	T150_mem0 += MAS_MEM[2]

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 18
	T150_mem1 += MAS_MEM[3]

	T2_t3 = S.Task('T2_t3', length=1, delay_cost=1)
	S += T2_t3 >= 18
	T2_t3 += MAS[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 18
	T40_mem0 += MM_MEM[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 18
	T40_mem1 += MM_MEM[1]

	T70 = S.Task('T70', length=1, delay_cost=1)
	S += T70 >= 18
	T70 += MAS[1]

	T10_t2 = S.Task('T10_t2', length=1, delay_cost=1)
	S += T10_t2 >= 19
	T10_t2 += MAS[0]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 19
	T130_mem0 += MAS_MEM[6]

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 19
	T130_mem1 += MAS_MEM[1]

	T150 = S.Task('T150', length=1, delay_cost=1)
	S += T150 >= 19
	T150 += MAS[1]

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 19
	T40 += MAS[3]

	T4_t5_mem0 = S.Task('T4_t5_mem0', length=1, delay_cost=1)
	S += T4_t5_mem0 >= 19
	T4_t5_mem0 += MM_MEM[0]

	T4_t5_mem1 = S.Task('T4_t5_mem1', length=1, delay_cost=1)
	S += T4_t5_mem1 >= 19
	T4_t5_mem1 += MM_MEM[1]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	S += T9_t2_mem0 >= 19
	T9_t2_mem0 += MAIN_MEM_r[0]

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	S += T9_t2_mem1 >= 19
	T9_t2_mem1 += MAIN_MEM_r[1]

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	S += T120_mem0 >= 20
	T120_mem0 += MAS_MEM[6]

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	S += T120_mem1 >= 20
	T120_mem1 += MAS_MEM[1]

	T130 = S.Task('T130', length=1, delay_cost=1)
	S += T130 >= 20
	T130 += MAS[2]

	T14_t0_in = S.Task('T14_t0_in', length=1, delay_cost=1)
	S += T14_t0_in >= 20
	T14_t0_in += MM_in[0]

	T14_t0_mem0 = S.Task('T14_t0_mem0', length=1, delay_cost=1)
	S += T14_t0_mem0 >= 20
	T14_t0_mem0 += MAS_MEM[4]

	T14_t0_mem1 = S.Task('T14_t0_mem1', length=1, delay_cost=1)
	S += T14_t0_mem1 >= 20
	T14_t0_mem1 += MAS_MEM[5]

	T1_t5_mem0 = S.Task('T1_t5_mem0', length=1, delay_cost=1)
	S += T1_t5_mem0 >= 20
	T1_t5_mem0 += MM_MEM[0]

	T1_t5_mem1 = S.Task('T1_t5_mem1', length=1, delay_cost=1)
	S += T1_t5_mem1 >= 20
	T1_t5_mem1 += MM_MEM[1]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	S += T2_t2_mem0 >= 20
	T2_t2_mem0 += MAIN_MEM_r[0]

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	S += T2_t2_mem1 >= 20
	T2_t2_mem1 += MAIN_MEM_r[1]

	T4_t5 = S.Task('T4_t5', length=1, delay_cost=1)
	S += T4_t5 >= 20
	T4_t5 += MAS[0]

	T9_t2 = S.Task('T9_t2', length=1, delay_cost=1)
	S += T9_t2 >= 20
	T9_t2 += MAS[1]

	T120 = S.Task('T120', length=1, delay_cost=1)
	S += T120 >= 21
	T120 += MAS[1]

	T14_t0 = S.Task('T14_t0', length=8, delay_cost=1)
	S += T14_t0 >= 21
	T14_t0 += MM[0]

	T1_t5 = S.Task('T1_t5', length=1, delay_cost=1)
	S += T1_t5 >= 21
	T1_t5 += MAS[0]

	T2_t2 = S.Task('T2_t2', length=1, delay_cost=1)
	S += T2_t2 >= 21
	T2_t2 += MAS[2]

	T2_t4_in = S.Task('T2_t4_in', length=1, delay_cost=1)
	S += T2_t4_in >= 21
	T2_t4_in += MM_in[0]

	T2_t4_mem0 = S.Task('T2_t4_mem0', length=1, delay_cost=1)
	S += T2_t4_mem0 >= 21
	T2_t4_mem0 += MAS_MEM[4]

	T2_t4_mem1 = S.Task('T2_t4_mem1', length=1, delay_cost=1)
	S += T2_t4_mem1 >= 21
	T2_t4_mem1 += MAS_MEM[1]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	S += T3_t2_mem0 >= 21
	T3_t2_mem0 += MAIN_MEM_r[0]

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	S += T3_t2_mem1 >= 21
	T3_t2_mem1 += MAIN_MEM_r[1]

	T6_t5_mem0 = S.Task('T6_t5_mem0', length=1, delay_cost=1)
	S += T6_t5_mem0 >= 21
	T6_t5_mem0 += MM_MEM[0]

	T6_t5_mem1 = S.Task('T6_t5_mem1', length=1, delay_cost=1)
	S += T6_t5_mem1 >= 21
	T6_t5_mem1 += MM_MEM[1]

	T2_t4 = S.Task('T2_t4', length=8, delay_cost=1)
	S += T2_t4 >= 22
	T2_t4 += MM[0]

	T3_t2 = S.Task('T3_t2', length=1, delay_cost=1)
	S += T3_t2 >= 22
	T3_t2 += MAS[1]

	T3_t4_in = S.Task('T3_t4_in', length=1, delay_cost=1)
	S += T3_t4_in >= 22
	T3_t4_in += MM_in[0]

	T3_t4_mem0 = S.Task('T3_t4_mem0', length=1, delay_cost=1)
	S += T3_t4_mem0 >= 22
	T3_t4_mem0 += MAS_MEM[2]

	T3_t4_mem1 = S.Task('T3_t4_mem1', length=1, delay_cost=1)
	S += T3_t4_mem1 >= 22
	T3_t4_mem1 += MAS_MEM[1]

	T6_t5 = S.Task('T6_t5', length=1, delay_cost=1)
	S += T6_t5 >= 22
	T6_t5 += MAS[0]

	T7_t5_mem0 = S.Task('T7_t5_mem0', length=1, delay_cost=1)
	S += T7_t5_mem0 >= 22
	T7_t5_mem0 += MM_MEM[0]

	T7_t5_mem1 = S.Task('T7_t5_mem1', length=1, delay_cost=1)
	S += T7_t5_mem1 >= 22
	T7_t5_mem1 += MM_MEM[1]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	S += T8_t2_mem0 >= 22
	T8_t2_mem0 += MAIN_MEM_r[0]

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	S += T8_t2_mem1 >= 22
	T8_t2_mem1 += MAIN_MEM_r[1]

	T3_t4 = S.Task('T3_t4', length=8, delay_cost=1)
	S += T3_t4 >= 23
	T3_t4 += MM[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 23
	T41_mem0 += MM_MEM[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 23
	T41_mem1 += MAS_MEM[1]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	S += T7_t3_mem0 >= 23
	T7_t3_mem0 += MAIN_MEM_r[0]

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	S += T7_t3_mem1 >= 23
	T7_t3_mem1 += MAIN_MEM_r[1]

	T7_t5 = S.Task('T7_t5', length=1, delay_cost=1)
	S += T7_t5 >= 23
	T7_t5 += MAS[2]

	T8_t2 = S.Task('T8_t2', length=1, delay_cost=1)
	S += T8_t2 >= 23
	T8_t2 += MAS[0]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 24
	T11_mem0 += MM_MEM[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 24
	T11_mem1 += MM_MEM[1]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 24
	T41 += MAS[3]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	S += T7_t2_mem0 >= 24
	T7_t2_mem0 += MAIN_MEM_r[0]

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	S += T7_t2_mem1 >= 24
	T7_t2_mem1 += MAIN_MEM_r[1]

	T7_t3 = S.Task('T7_t3', length=1, delay_cost=1)
	S += T7_t3 >= 24
	T7_t3 += MAS[0]

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 25
	T11 += MAS[2]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	S += T1_t1_mem0 >= 25
	T1_t1_mem0 += MAIN_MEM_r[0]

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	S += T1_t1_mem1 >= 25
	T1_t1_mem1 += MAIN_MEM_r[1]

	T2_t5_mem0 = S.Task('T2_t5_mem0', length=1, delay_cost=1)
	S += T2_t5_mem0 >= 25
	T2_t5_mem0 += MM_MEM[0]

	T2_t5_mem1 = S.Task('T2_t5_mem1', length=1, delay_cost=1)
	S += T2_t5_mem1 >= 25
	T2_t5_mem1 += MM_MEM[1]

	T7_t2 = S.Task('T7_t2', length=1, delay_cost=1)
	S += T7_t2 >= 25
	T7_t2 += MAS[0]

	T7_t4_in = S.Task('T7_t4_in', length=1, delay_cost=1)
	S += T7_t4_in >= 25
	T7_t4_in += MM_in[0]

	T7_t4_mem0 = S.Task('T7_t4_mem0', length=1, delay_cost=1)
	S += T7_t4_mem0 >= 25
	T7_t4_mem0 += MAS_MEM[0]

	T7_t4_mem1 = S.Task('T7_t4_mem1', length=1, delay_cost=1)
	S += T7_t4_mem1 >= 25
	T7_t4_mem1 += MAS_MEM[1]

	T1_t1 = S.Task('T1_t1', length=1, delay_cost=1)
	S += T1_t1 >= 26
	T1_t1 += MAS[3]

	T1_t2_in = S.Task('T1_t2_in', length=1, delay_cost=1)
	S += T1_t2_in >= 26
	T1_t2_in += MM_in[0]

	T1_t2_mem0 = S.Task('T1_t2_mem0', length=1, delay_cost=1)
	S += T1_t2_mem0 >= 26
	T1_t2_mem0 += MAS_MEM[6]

	T1_t2_mem1 = S.Task('T1_t2_mem1', length=1, delay_cost=1)
	S += T1_t2_mem1 >= 26
	T1_t2_mem1 += MAS_MEM[7]

	T2_t5 = S.Task('T2_t5', length=1, delay_cost=1)
	S += T2_t5 >= 26
	T2_t5 += MAS[1]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	S += T6_t3_mem0 >= 26
	T6_t3_mem0 += MAIN_MEM_r[0]

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	S += T6_t3_mem1 >= 26
	T6_t3_mem1 += MAIN_MEM_r[1]

	T7_t4 = S.Task('T7_t4', length=8, delay_cost=1)
	S += T7_t4 >= 26
	T7_t4 += MM[0]

	T1_t2 = S.Task('T1_t2', length=8, delay_cost=1)
	S += T1_t2 >= 27
	T1_t2 += MM[0]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	S += T6_t2_mem0 >= 27
	T6_t2_mem0 += MAIN_MEM_r[0]

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	S += T6_t2_mem1 >= 27
	T6_t2_mem1 += MAIN_MEM_r[1]

	T6_t3 = S.Task('T6_t3', length=1, delay_cost=1)
	S += T6_t3 >= 27
	T6_t3 += MAS[0]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	S += T5_t1_mem0 >= 28
	T5_t1_mem0 += MAIN_MEM_r[0]

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	S += T5_t1_mem1 >= 28
	T5_t1_mem1 += MAIN_MEM_r[1]

	T6_t2 = S.Task('T6_t2', length=1, delay_cost=1)
	S += T6_t2 >= 28
	T6_t2 += MAS[0]

	T6_t4_in = S.Task('T6_t4_in', length=1, delay_cost=1)
	S += T6_t4_in >= 28
	T6_t4_in += MM_in[0]

	T6_t4_mem0 = S.Task('T6_t4_mem0', length=1, delay_cost=1)
	S += T6_t4_mem0 >= 28
	T6_t4_mem0 += MAS_MEM[0]

	T6_t4_mem1 = S.Task('T6_t4_mem1', length=1, delay_cost=1)
	S += T6_t4_mem1 >= 28
	T6_t4_mem1 += MAS_MEM[1]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 29
	T21_mem0 += MM_MEM[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 29
	T21_mem1 += MAS_MEM[3]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	S += T5_t0_mem0 >= 29
	T5_t0_mem0 += MAIN_MEM_r[0]

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	S += T5_t0_mem1 >= 29
	T5_t0_mem1 += MAIN_MEM_r[1]

	T5_t1 = S.Task('T5_t1', length=1, delay_cost=1)
	S += T5_t1 >= 29
	T5_t1 += MAS[1]

	T6_t4 = S.Task('T6_t4', length=8, delay_cost=1)
	S += T6_t4 >= 29
	T6_t4 += MM[0]

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 30
	T131_mem0 += MAS_MEM[6]

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 30
	T131_mem1 += MAS_MEM[7]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 30
	T21 += MAS[3]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 30
	T31_mem0 += MM_MEM[0]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 30
	T31_mem1 += MAS_MEM[5]

	T5_t0 = S.Task('T5_t0', length=1, delay_cost=1)
	S += T5_t0 >= 30
	T5_t0 += MAS[0]

	T5_t2_in = S.Task('T5_t2_in', length=1, delay_cost=1)
	S += T5_t2_in >= 30
	T5_t2_in += MM_in[0]

	T5_t2_mem0 = S.Task('T5_t2_mem0', length=1, delay_cost=1)
	S += T5_t2_mem0 >= 30
	T5_t2_mem0 += MAS_MEM[0]

	T5_t2_mem1 = S.Task('T5_t2_mem1', length=1, delay_cost=1)
	S += T5_t2_mem1 >= 30
	T5_t2_mem1 += MAS_MEM[3]

	Z3_t2_mem0 = S.Task('Z3_t2_mem0', length=1, delay_cost=1)
	S += Z3_t2_mem0 >= 30
	Z3_t2_mem0 += MAIN_MEM_r[0]

	Z3_t2_mem1 = S.Task('Z3_t2_mem1', length=1, delay_cost=1)
	S += Z3_t2_mem1 >= 30
	Z3_t2_mem1 += MAIN_MEM_r[1]

	T11_t3_mem0 = S.Task('T11_t3_mem0', length=1, delay_cost=1)
	S += T11_t3_mem0 >= 31
	T11_t3_mem0 += MAS_MEM[2]

	T11_t3_mem1 = S.Task('T11_t3_mem1', length=1, delay_cost=1)
	S += T11_t3_mem1 >= 31
	T11_t3_mem1 += MAS_MEM[3]

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	S += T121_mem0 >= 31
	T121_mem0 += MAS_MEM[6]

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	S += T121_mem1 >= 31
	T121_mem1 += MAS_MEM[7]

	T131 = S.Task('T131', length=1, delay_cost=1)
	S += T131 >= 31
	T131 += MAS[0]

	T14_t2_mem0 = S.Task('T14_t2_mem0', length=1, delay_cost=1)
	S += T14_t2_mem0 >= 31
	T14_t2_mem0 += MAS_MEM[4]

	T14_t2_mem1 = S.Task('T14_t2_mem1', length=1, delay_cost=1)
	S += T14_t2_mem1 >= 31
	T14_t2_mem1 += MAS_MEM[1]

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 31
	T31 += MAS[1]

	T5_t2 = S.Task('T5_t2', length=8, delay_cost=1)
	S += T5_t2 >= 31
	T5_t2 += MM[0]

	T9_t1_in = S.Task('T9_t1_in', length=1, delay_cost=1)
	S += T9_t1_in >= 31
	T9_t1_in += MM_in[0]

	T9_t1_mem0 = S.Task('T9_t1_mem0', length=1, delay_cost=1)
	S += T9_t1_mem0 >= 31
	T9_t1_mem0 += MAIN_MEM_r[0]

	T9_t1_mem1 = S.Task('T9_t1_mem1', length=1, delay_cost=1)
	S += T9_t1_mem1 >= 31
	T9_t1_mem1 += MAS_MEM[5]

	Z3_t2 = S.Task('Z3_t2', length=1, delay_cost=1)
	S += Z3_t2 >= 31
	Z3_t2 += MAS[3]

	T10_t3_mem0 = S.Task('T10_t3_mem0', length=1, delay_cost=1)
	S += T10_t3_mem0 >= 32
	T10_t3_mem0 += MAS_MEM[2]

	T10_t3_mem1 = S.Task('T10_t3_mem1', length=1, delay_cost=1)
	S += T10_t3_mem1 >= 32
	T10_t3_mem1 += MAS_MEM[3]

	T11_t3 = S.Task('T11_t3', length=1, delay_cost=1)
	S += T11_t3 >= 32
	T11_t3 += MAS[0]

	T121 = S.Task('T121', length=1, delay_cost=1)
	S += T121 >= 32
	T121 += MAS[1]

	T14_t2 = S.Task('T14_t2', length=1, delay_cost=1)
	S += T14_t2 >= 32
	T14_t2 += MAS[3]

	T14_t3_mem0 = S.Task('T14_t3_mem0', length=1, delay_cost=1)
	S += T14_t3_mem0 >= 32
	T14_t3_mem0 += MAS_MEM[4]

	T14_t3_mem1 = S.Task('T14_t3_mem1', length=1, delay_cost=1)
	S += T14_t3_mem1 >= 32
	T14_t3_mem1 += MAS_MEM[1]

	T8_t1_in = S.Task('T8_t1_in', length=1, delay_cost=1)
	S += T8_t1_in >= 32
	T8_t1_in += MM_in[0]

	T8_t1_mem0 = S.Task('T8_t1_mem0', length=1, delay_cost=1)
	S += T8_t1_mem0 >= 32
	T8_t1_mem0 += MAIN_MEM_r[0]

	T8_t1_mem1 = S.Task('T8_t1_mem1', length=1, delay_cost=1)
	S += T8_t1_mem1 >= 32
	T8_t1_mem1 += MAS_MEM[5]

	T9_t1 = S.Task('T9_t1', length=8, delay_cost=1)
	S += T9_t1 >= 32
	T9_t1 += MM[0]

	T10_t3 = S.Task('T10_t3', length=1, delay_cost=1)
	S += T10_t3 >= 33
	T10_t3 += MAS[3]

	T11_t1_in = S.Task('T11_t1_in', length=1, delay_cost=1)
	S += T11_t1_in >= 33
	T11_t1_in += MM_in[0]

	T11_t1_mem0 = S.Task('T11_t1_mem0', length=1, delay_cost=1)
	S += T11_t1_mem0 >= 33
	T11_t1_mem0 += MAIN_MEM_r[0]

	T11_t1_mem1 = S.Task('T11_t1_mem1', length=1, delay_cost=1)
	S += T11_t1_mem1 >= 33
	T11_t1_mem1 += MAS_MEM[3]

	T14_t3 = S.Task('T14_t3', length=1, delay_cost=1)
	S += T14_t3 >= 33
	T14_t3 += MAS[1]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 33
	T71_mem0 += MM_MEM[0]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 33
	T71_mem1 += MAS_MEM[5]

	T8_t1 = S.Task('T8_t1', length=8, delay_cost=1)
	S += T8_t1 >= 33
	T8_t1 += MM[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 34
	T10_mem0 += MM_MEM[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 34
	T10_mem1 += MAS_MEM[1]

	T10_t1_in = S.Task('T10_t1_in', length=1, delay_cost=1)
	S += T10_t1_in >= 34
	T10_t1_in += MM_in[0]

	T10_t1_mem0 = S.Task('T10_t1_mem0', length=1, delay_cost=1)
	S += T10_t1_mem0 >= 34
	T10_t1_mem0 += MAIN_MEM_r[0]

	T10_t1_mem1 = S.Task('T10_t1_mem1', length=1, delay_cost=1)
	S += T10_t1_mem1 >= 34
	T10_t1_mem1 += MAS_MEM[3]

	T11_t1 = S.Task('T11_t1', length=8, delay_cost=1)
	S += T11_t1 >= 34
	T11_t1 += MM[0]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 34
	T151_mem0 += MAS_MEM[6]

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 34
	T151_mem1 += MAS_MEM[7]

	T71 = S.Task('T71', length=1, delay_cost=1)
	S += T71 >= 34
	T71 += MAS[3]

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 35
	T10 += MAS[0]

	T10_t1 = S.Task('T10_t1', length=8, delay_cost=1)
	S += T10_t1 >= 35
	T10_t1 += MM[0]

	T151 = S.Task('T151', length=1, delay_cost=1)
	S += T151 >= 35
	T151 += MAS[3]

	T16_t2_mem0 = S.Task('T16_t2_mem0', length=1, delay_cost=1)
	S += T16_t2_mem0 >= 35
	T16_t2_mem0 += MAS_MEM[0]

	T16_t2_mem1 = S.Task('T16_t2_mem1', length=1, delay_cost=1)
	S += T16_t2_mem1 >= 35
	T16_t2_mem1 += MAS_MEM[5]

	T24_t3_mem0 = S.Task('T24_t3_mem0', length=1, delay_cost=1)
	S += T24_t3_mem0 >= 35
	T24_t3_mem0 += MAS_MEM[2]

	T24_t3_mem1 = S.Task('T24_t3_mem1', length=1, delay_cost=1)
	S += T24_t3_mem1 >= 35
	T24_t3_mem1 += MAS_MEM[3]

	T8_t0_in = S.Task('T8_t0_in', length=1, delay_cost=1)
	S += T8_t0_in >= 35
	T8_t0_in += MM_in[0]

	T8_t0_mem0 = S.Task('T8_t0_mem0', length=1, delay_cost=1)
	S += T8_t0_mem0 >= 35
	T8_t0_mem0 += MAIN_MEM_r[0]

	T8_t0_mem1 = S.Task('T8_t0_mem1', length=1, delay_cost=1)
	S += T8_t0_mem1 >= 35
	T8_t0_mem1 += MAS_MEM[1]

	T10_t0_in = S.Task('T10_t0_in', length=1, delay_cost=1)
	S += T10_t0_in >= 36
	T10_t0_in += MM_in[0]

	T10_t0_mem0 = S.Task('T10_t0_mem0', length=1, delay_cost=1)
	S += T10_t0_mem0 >= 36
	T10_t0_mem0 += MAIN_MEM_r[0]

	T10_t0_mem1 = S.Task('T10_t0_mem1', length=1, delay_cost=1)
	S += T10_t0_mem1 >= 36
	T10_t0_mem1 += MAS_MEM[3]

	T16_t2 = S.Task('T16_t2', length=1, delay_cost=1)
	S += T16_t2 >= 36
	T16_t2 += MAS[3]

	T17_t3_mem0 = S.Task('T17_t3_mem0', length=1, delay_cost=1)
	S += T17_t3_mem0 >= 36
	T17_t3_mem0 += MAS_MEM[2]

	T17_t3_mem1 = S.Task('T17_t3_mem1', length=1, delay_cost=1)
	S += T17_t3_mem1 >= 36
	T17_t3_mem1 += MAS_MEM[7]

	T24_t3 = S.Task('T24_t3', length=1, delay_cost=1)
	S += T24_t3 >= 36
	T24_t3 += MAS[0]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 36
	T61_mem0 += MM_MEM[0]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 36
	T61_mem1 += MAS_MEM[1]

	T8_t0 = S.Task('T8_t0', length=8, delay_cost=1)
	S += T8_t0 >= 36
	T8_t0 += MM[0]

	T8_t3_mem0 = S.Task('T8_t3_mem0', length=1, delay_cost=1)
	S += T8_t3_mem0 >= 36
	T8_t3_mem0 += MAS_MEM[0]

	T8_t3_mem1 = S.Task('T8_t3_mem1', length=1, delay_cost=1)
	S += T8_t3_mem1 >= 36
	T8_t3_mem1 += MAS_MEM[5]

	T10_t0 = S.Task('T10_t0', length=8, delay_cost=1)
	S += T10_t0 >= 37
	T10_t0 += MM[0]

	T17_t3 = S.Task('T17_t3', length=1, delay_cost=1)
	S += T17_t3 >= 37
	T17_t3 += MAS[0]

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 37
	T61 += MAS[3]

	T8_t3 = S.Task('T8_t3', length=1, delay_cost=1)
	S += T8_t3 >= 37
	T8_t3 += MAS[1]

	T9_t0_in = S.Task('T9_t0_in', length=1, delay_cost=1)
	S += T9_t0_in >= 37
	T9_t0_in += MM_in[0]

	T9_t0_mem0 = S.Task('T9_t0_mem0', length=1, delay_cost=1)
	S += T9_t0_mem0 >= 37
	T9_t0_mem0 += MAIN_MEM_r[0]

	T9_t0_mem1 = S.Task('T9_t0_mem1', length=1, delay_cost=1)
	S += T9_t0_mem1 >= 37
	T9_t0_mem1 += MAS_MEM[1]

	T9_t3_mem0 = S.Task('T9_t3_mem0', length=1, delay_cost=1)
	S += T9_t3_mem0 >= 37
	T9_t3_mem0 += MAS_MEM[0]

	T9_t3_mem1 = S.Task('T9_t3_mem1', length=1, delay_cost=1)
	S += T9_t3_mem1 >= 37
	T9_t3_mem1 += MAS_MEM[5]

	T11_t0_in = S.Task('T11_t0_in', length=1, delay_cost=1)
	S += T11_t0_in >= 38
	T11_t0_in += MM_in[0]

	T11_t0_mem0 = S.Task('T11_t0_mem0', length=1, delay_cost=1)
	S += T11_t0_mem0 >= 38
	T11_t0_mem0 += MAIN_MEM_r[0]

	T11_t0_mem1 = S.Task('T11_t0_mem1', length=1, delay_cost=1)
	S += T11_t0_mem1 >= 38
	T11_t0_mem1 += MAS_MEM[3]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 38
	T50_mem0 += MM_MEM[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 38
	T50_mem1 += MAS_MEM[7]

	T9_t0 = S.Task('T9_t0', length=8, delay_cost=1)
	S += T9_t0 >= 38
	T9_t0 += MM[0]

	T9_t3 = S.Task('T9_t3', length=1, delay_cost=1)
	S += T9_t3 >= 38
	T9_t3 += MAS[1]

	T11_t0 = S.Task('T11_t0', length=8, delay_cost=1)
	S += T11_t0 >= 39
	T11_t0 += MM[0]

	T14_t4_in = S.Task('T14_t4_in', length=1, delay_cost=1)
	S += T14_t4_in >= 39
	T14_t4_in += MM_in[0]

	T14_t4_mem0 = S.Task('T14_t4_mem0', length=1, delay_cost=1)
	S += T14_t4_mem0 >= 39
	T14_t4_mem0 += MAS_MEM[6]

	T14_t4_mem1 = S.Task('T14_t4_mem1', length=1, delay_cost=1)
	S += T14_t4_mem1 >= 39
	T14_t4_mem1 += MAS_MEM[3]

	T20_t2_mem0 = S.Task('T20_t2_mem0', length=1, delay_cost=1)
	S += T20_t2_mem0 >= 39
	T20_t2_mem0 += MAS_MEM[0]

	T20_t2_mem1 = S.Task('T20_t2_mem1', length=1, delay_cost=1)
	S += T20_t2_mem1 >= 39
	T20_t2_mem1 += MAS_MEM[1]

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 39
	T50 += MAS[0]

	T14_t4 = S.Task('T14_t4', length=8, delay_cost=1)
	S += T14_t4 >= 40
	T14_t4 += MM[0]

	T20_t2 = S.Task('T20_t2', length=1, delay_cost=1)
	S += T20_t2 >= 40
	T20_t2 += MAS[0]

	T8_t4_in = S.Task('T8_t4_in', length=1, delay_cost=1)
	S += T8_t4_in >= 40
	T8_t4_in += MM_in[0]

	T8_t4_mem0 = S.Task('T8_t4_mem0', length=1, delay_cost=1)
	S += T8_t4_mem0 >= 40
	T8_t4_mem0 += MAS_MEM[0]

	T8_t4_mem1 = S.Task('T8_t4_mem1', length=1, delay_cost=1)
	S += T8_t4_mem1 >= 40
	T8_t4_mem1 += MAS_MEM[3]

	T11_t4_in = S.Task('T11_t4_in', length=1, delay_cost=1)
	S += T11_t4_in >= 41
	T11_t4_in += MM_in[0]

	T11_t4_mem0 = S.Task('T11_t4_mem0', length=1, delay_cost=1)
	S += T11_t4_mem0 >= 41
	T11_t4_mem0 += MAS_MEM[6]

	T11_t4_mem1 = S.Task('T11_t4_mem1', length=1, delay_cost=1)
	S += T11_t4_mem1 >= 41
	T11_t4_mem1 += MAS_MEM[1]

	T8_t4 = S.Task('T8_t4', length=8, delay_cost=1)
	S += T8_t4 >= 41
	T8_t4 += MM[0]

	T11_t4 = S.Task('T11_t4', length=8, delay_cost=1)
	S += T11_t4 >= 42
	T11_t4 += MM[0]

	T14_t1_in = S.Task('T14_t1_in', length=1, delay_cost=1)
	S += T14_t1_in >= 42
	T14_t1_in += MM_in[0]

	T14_t1_mem0 = S.Task('T14_t1_mem0', length=1, delay_cost=1)
	S += T14_t1_mem0 >= 42
	T14_t1_mem0 += MAS_MEM[0]

	T14_t1_mem1 = S.Task('T14_t1_mem1', length=1, delay_cost=1)
	S += T14_t1_mem1 >= 42
	T14_t1_mem1 += MAS_MEM[1]

	T14_t1 = S.Task('T14_t1', length=8, delay_cost=1)
	S += T14_t1 >= 43
	T14_t1 += MM[0]

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	S += T80_mem0 >= 43
	T80_mem0 += MM_MEM[0]

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	S += T80_mem1 >= 43
	T80_mem1 += MM_MEM[1]

	T9_t4_in = S.Task('T9_t4_in', length=1, delay_cost=1)
	S += T9_t4_in >= 43
	T9_t4_in += MM_in[0]

	T9_t4_mem0 = S.Task('T9_t4_mem0', length=1, delay_cost=1)
	S += T9_t4_mem0 >= 43
	T9_t4_mem0 += MAS_MEM[2]

	T9_t4_mem1 = S.Task('T9_t4_mem1', length=1, delay_cost=1)
	S += T9_t4_mem1 >= 43
	T9_t4_mem1 += MAS_MEM[3]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 44
	T100_mem0 += MM_MEM[0]

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 44
	T100_mem1 += MM_MEM[1]

	T16_t0_in = S.Task('T16_t0_in', length=1, delay_cost=1)
	S += T16_t0_in >= 44
	T16_t0_in += MM_in[0]

	T16_t0_mem0 = S.Task('T16_t0_mem0', length=1, delay_cost=1)
	S += T16_t0_mem0 >= 44
	T16_t0_mem0 += MAS_MEM[0]

	T16_t0_mem1 = S.Task('T16_t0_mem1', length=1, delay_cost=1)
	S += T16_t0_mem1 >= 44
	T16_t0_mem1 += MAS_MEM[3]

	T80 = S.Task('T80', length=1, delay_cost=1)
	S += T80 >= 44
	T80 += MAS[1]

	T9_t4 = S.Task('T9_t4', length=8, delay_cost=1)
	S += T9_t4 >= 44
	T9_t4 += MM[0]

	T100 = S.Task('T100', length=1, delay_cost=1)
	S += T100 >= 45
	T100 += MAS[2]

	T10_t4_in = S.Task('T10_t4_in', length=1, delay_cost=1)
	S += T10_t4_in >= 45
	T10_t4_in += MM_in[0]

	T10_t4_mem0 = S.Task('T10_t4_mem0', length=1, delay_cost=1)
	S += T10_t4_mem0 >= 45
	T10_t4_mem0 += MAS_MEM[0]

	T10_t4_mem1 = S.Task('T10_t4_mem1', length=1, delay_cost=1)
	S += T10_t4_mem1 >= 45
	T10_t4_mem1 += MAS_MEM[7]

	T16_t0 = S.Task('T16_t0', length=8, delay_cost=1)
	S += T16_t0 >= 45
	T16_t0 += MM[0]

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	S += T210_mem0 >= 45
	T210_mem0 += MAS_MEM[4]

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	S += T210_mem1 >= 45
	T210_mem1 += MAS_MEM[5]

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	S += T90_mem0 >= 45
	T90_mem0 += MM_MEM[0]

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	S += T90_mem1 >= 45
	T90_mem1 += MM_MEM[1]

	T10_t4 = S.Task('T10_t4', length=8, delay_cost=1)
	S += T10_t4 >= 46
	T10_t4 += MM[0]

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	S += T110_mem0 >= 46
	T110_mem0 += MM_MEM[0]

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	S += T110_mem1 >= 46
	T110_mem1 += MM_MEM[1]

	T17_t0_in = S.Task('T17_t0_in', length=1, delay_cost=1)
	S += T17_t0_in >= 46
	T17_t0_in += MM_in[0]

	T17_t0_mem0 = S.Task('T17_t0_mem0', length=1, delay_cost=1)
	S += T17_t0_mem0 >= 46
	T17_t0_mem0 += MAS_MEM[2]

	T17_t0_mem1 = S.Task('T17_t0_mem1', length=1, delay_cost=1)
	S += T17_t0_mem1 >= 46
	T17_t0_mem1 += MAS_MEM[3]

	T190_mem0 = S.Task('T190_mem0', length=1, delay_cost=1)
	S += T190_mem0 >= 46
	T190_mem0 += MAS_MEM[0]

	T190_mem1 = S.Task('T190_mem1', length=1, delay_cost=1)
	S += T190_mem1 >= 46
	T190_mem1 += MAS_MEM[5]

	T210 = S.Task('T210', length=1, delay_cost=1)
	S += T210 >= 46
	T210 += MAS[1]

	T90 = S.Task('T90', length=1, delay_cost=1)
	S += T90 >= 46
	T90 += MAS[2]

	T110 = S.Task('T110', length=1, delay_cost=1)
	S += T110 >= 47
	T110 += MAS[3]

	T17_t0 = S.Task('T17_t0', length=8, delay_cost=1)
	S += T17_t0 >= 47
	T17_t0 += MM[0]

	T180_mem0 = S.Task('T180_mem0', length=1, delay_cost=1)
	S += T180_mem0 >= 47
	T180_mem0 += MAS_MEM[0]

	T180_mem1 = S.Task('T180_mem1', length=1, delay_cost=1)
	S += T180_mem1 >= 47
	T180_mem1 += MAS_MEM[5]

	T190 = S.Task('T190', length=1, delay_cost=1)
	S += T190 >= 47
	T190 += MAS[1]

	T24_t0_in = S.Task('T24_t0_in', length=1, delay_cost=1)
	S += T24_t0_in >= 47
	T24_t0_in += MM_in[0]

	T24_t0_mem0 = S.Task('T24_t0_mem0', length=1, delay_cost=1)
	S += T24_t0_mem0 >= 47
	T24_t0_mem0 += MAS_MEM[6]

	T24_t0_mem1 = S.Task('T24_t0_mem1', length=1, delay_cost=1)
	S += T24_t0_mem1 >= 47
	T24_t0_mem1 += MAS_MEM[3]

	T8_t5_mem0 = S.Task('T8_t5_mem0', length=1, delay_cost=1)
	S += T8_t5_mem0 >= 47
	T8_t5_mem0 += MM_MEM[0]

	T8_t5_mem1 = S.Task('T8_t5_mem1', length=1, delay_cost=1)
	S += T8_t5_mem1 >= 47
	T8_t5_mem1 += MM_MEM[1]

	T180 = S.Task('T180', length=1, delay_cost=1)
	S += T180 >= 48
	T180 += MAS[2]

	T20_t0_in = S.Task('T20_t0_in', length=1, delay_cost=1)
	S += T20_t0_in >= 48
	T20_t0_in += MM_in[0]

	T20_t0_mem0 = S.Task('T20_t0_mem0', length=1, delay_cost=1)
	S += T20_t0_mem0 >= 48
	T20_t0_mem0 += MAS_MEM[0]

	T20_t0_mem1 = S.Task('T20_t0_mem1', length=1, delay_cost=1)
	S += T20_t0_mem1 >= 48
	T20_t0_mem1 += MAS_MEM[5]

	T24_t0 = S.Task('T24_t0', length=8, delay_cost=1)
	S += T24_t0 >= 48
	T24_t0 += MM[0]

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	S += T81_mem0 >= 48
	T81_mem0 += MM_MEM[0]

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	S += T81_mem1 >= 48
	T81_mem1 += MAS_MEM[7]

	T8_t5 = S.Task('T8_t5', length=1, delay_cost=1)
	S += T8_t5 >= 48
	T8_t5 += MAS[3]

	T11_t5_mem0 = S.Task('T11_t5_mem0', length=1, delay_cost=1)
	S += T11_t5_mem0 >= 49
	T11_t5_mem0 += MM_MEM[0]

	T11_t5_mem1 = S.Task('T11_t5_mem1', length=1, delay_cost=1)
	S += T11_t5_mem1 >= 49
	T11_t5_mem1 += MM_MEM[1]

	T16_t3_mem0 = S.Task('T16_t3_mem0', length=1, delay_cost=1)
	S += T16_t3_mem0 >= 49
	T16_t3_mem0 += MAS_MEM[2]

	T16_t3_mem1 = S.Task('T16_t3_mem1', length=1, delay_cost=1)
	S += T16_t3_mem1 >= 49
	T16_t3_mem1 += MAS_MEM[1]

	T17_t1_in = S.Task('T17_t1_in', length=1, delay_cost=1)
	S += T17_t1_in >= 49
	T17_t1_in += MM_in[0]

	T17_t1_mem0 = S.Task('T17_t1_mem0', length=1, delay_cost=1)
	S += T17_t1_mem0 >= 49
	T17_t1_mem0 += MAS_MEM[0]

	T17_t1_mem1 = S.Task('T17_t1_mem1', length=1, delay_cost=1)
	S += T17_t1_mem1 >= 49
	T17_t1_mem1 += MAS_MEM[7]

	T20_t0 = S.Task('T20_t0', length=8, delay_cost=1)
	S += T20_t0 >= 49
	T20_t0 += MM[0]

	T81 = S.Task('T81', length=1, delay_cost=1)
	S += T81 >= 49
	T81 += MAS[0]

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	S += T111_mem0 >= 50
	T111_mem0 += MM_MEM[0]

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	S += T111_mem1 >= 50
	T111_mem1 += MAS_MEM[3]

	T11_t5 = S.Task('T11_t5', length=1, delay_cost=1)
	S += T11_t5 >= 50
	T11_t5 += MAS[1]

	T16_t1_in = S.Task('T16_t1_in', length=1, delay_cost=1)
	S += T16_t1_in >= 50
	T16_t1_in += MM_in[0]

	T16_t1_mem0 = S.Task('T16_t1_mem0', length=1, delay_cost=1)
	S += T16_t1_mem0 >= 50
	T16_t1_mem0 += MAS_MEM[4]

	T16_t1_mem1 = S.Task('T16_t1_mem1', length=1, delay_cost=1)
	S += T16_t1_mem1 >= 50
	T16_t1_mem1 += MAS_MEM[1]

	T16_t3 = S.Task('T16_t3', length=1, delay_cost=1)
	S += T16_t3 >= 50
	T16_t3 += MAS[3]

	T17_t1 = S.Task('T17_t1', length=8, delay_cost=1)
	S += T17_t1 >= 50
	T17_t1 += MM[0]

	T111 = S.Task('T111', length=1, delay_cost=1)
	S += T111 >= 51
	T111 += MAS[2]

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 51
	T140_mem0 += MM_MEM[0]

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 51
	T140_mem1 += MM_MEM[1]

	T16_t1 = S.Task('T16_t1', length=8, delay_cost=1)
	S += T16_t1 >= 51
	T16_t1 += MM[0]

	T17_t2_mem0 = S.Task('T17_t2_mem0', length=1, delay_cost=1)
	S += T17_t2_mem0 >= 51
	T17_t2_mem0 += MAS_MEM[2]

	T17_t2_mem1 = S.Task('T17_t2_mem1', length=1, delay_cost=1)
	S += T17_t2_mem1 >= 51
	T17_t2_mem1 += MAS_MEM[1]

	T24_t1_in = S.Task('T24_t1_in', length=1, delay_cost=1)
	S += T24_t1_in >= 51
	T24_t1_in += MM_in[0]

	T24_t1_mem0 = S.Task('T24_t1_mem0', length=1, delay_cost=1)
	S += T24_t1_mem0 >= 51
	T24_t1_mem0 += MAS_MEM[4]

	T24_t1_mem1 = S.Task('T24_t1_mem1', length=1, delay_cost=1)
	S += T24_t1_mem1 >= 51
	T24_t1_mem1 += MAS_MEM[3]

	T24_t2_mem0 = S.Task('T24_t2_mem0', length=1, delay_cost=1)
	S += T24_t2_mem0 >= 51
	T24_t2_mem0 += MAS_MEM[6]

	T24_t2_mem1 = S.Task('T24_t2_mem1', length=1, delay_cost=1)
	S += T24_t2_mem1 >= 51
	T24_t2_mem1 += MAS_MEM[5]

	T140 = S.Task('T140', length=1, delay_cost=1)
	S += T140 >= 52
	T140 += MAS[0]

	T17_t2 = S.Task('T17_t2', length=1, delay_cost=1)
	S += T17_t2 >= 52
	T17_t2 += MAS[2]

	T24_t1 = S.Task('T24_t1', length=8, delay_cost=1)
	S += T24_t1 >= 52
	T24_t1 += MM[0]

	T24_t2 = S.Task('T24_t2', length=1, delay_cost=1)
	S += T24_t2 >= 52
	T24_t2 += MAS[3]

	T9_t5_mem0 = S.Task('T9_t5_mem0', length=1, delay_cost=1)
	S += T9_t5_mem0 >= 52
	T9_t5_mem0 += MM_MEM[0]

	T9_t5_mem1 = S.Task('T9_t5_mem1', length=1, delay_cost=1)
	S += T9_t5_mem1 >= 52
	T9_t5_mem1 += MM_MEM[1]

	Z3_t0_in = S.Task('Z3_t0_in', length=1, delay_cost=1)
	S += Z3_t0_in >= 52
	Z3_t0_in += MM_in[0]

	Z3_t0_mem0 = S.Task('Z3_t0_mem0', length=1, delay_cost=1)
	S += Z3_t0_mem0 >= 52
	Z3_t0_mem0 += MAIN_MEM_r[0]

	Z3_t0_mem1 = S.Task('Z3_t0_mem1', length=1, delay_cost=1)
	S += Z3_t0_mem1 >= 52
	Z3_t0_mem1 += MAS_MEM[1]

	T16_t4_in = S.Task('T16_t4_in', length=1, delay_cost=1)
	S += T16_t4_in >= 53
	T16_t4_in += MM_in[0]

	T16_t4_mem0 = S.Task('T16_t4_mem0', length=1, delay_cost=1)
	S += T16_t4_mem0 >= 53
	T16_t4_mem0 += MAS_MEM[6]

	T16_t4_mem1 = S.Task('T16_t4_mem1', length=1, delay_cost=1)
	S += T16_t4_mem1 >= 53
	T16_t4_mem1 += MAS_MEM[7]

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	S += T91_mem0 >= 53
	T91_mem0 += MM_MEM[0]

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	S += T91_mem1 >= 53
	T91_mem1 += MAS_MEM[1]

	T9_t5 = S.Task('T9_t5', length=1, delay_cost=1)
	S += T9_t5 >= 53
	T9_t5 += MAS[0]

	Z3_t0 = S.Task('Z3_t0', length=8, delay_cost=1)
	S += Z3_t0 >= 53
	Z3_t0 += MM[0]

	T10_t5_mem0 = S.Task('T10_t5_mem0', length=1, delay_cost=1)
	S += T10_t5_mem0 >= 54
	T10_t5_mem0 += MM_MEM[0]

	T10_t5_mem1 = S.Task('T10_t5_mem1', length=1, delay_cost=1)
	S += T10_t5_mem1 >= 54
	T10_t5_mem1 += MM_MEM[1]

	T16_t4 = S.Task('T16_t4', length=8, delay_cost=1)
	S += T16_t4 >= 54
	T16_t4 += MM[0]

	T17_t4_in = S.Task('T17_t4_in', length=1, delay_cost=1)
	S += T17_t4_in >= 54
	T17_t4_in += MM_in[0]

	T17_t4_mem0 = S.Task('T17_t4_mem0', length=1, delay_cost=1)
	S += T17_t4_mem0 >= 54
	T17_t4_mem0 += MAS_MEM[4]

	T17_t4_mem1 = S.Task('T17_t4_mem1', length=1, delay_cost=1)
	S += T17_t4_mem1 >= 54
	T17_t4_mem1 += MAS_MEM[1]

	T181_mem0 = S.Task('T181_mem0', length=1, delay_cost=1)
	S += T181_mem0 >= 54
	T181_mem0 += MAS_MEM[0]

	T181_mem1 = S.Task('T181_mem1', length=1, delay_cost=1)
	S += T181_mem1 >= 54
	T181_mem1 += MAS_MEM[7]

	T91 = S.Task('T91', length=1, delay_cost=1)
	S += T91 >= 54
	T91 += MAS[3]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 55
	T101_mem0 += MM_MEM[0]

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 55
	T101_mem1 += MAS_MEM[1]

	T10_t5 = S.Task('T10_t5', length=1, delay_cost=1)
	S += T10_t5 >= 55
	T10_t5 += MAS[0]

	T17_t4 = S.Task('T17_t4', length=8, delay_cost=1)
	S += T17_t4 >= 55
	T17_t4 += MM[0]

	T181 = S.Task('T181', length=1, delay_cost=1)
	S += T181 >= 55
	T181 += MAS[3]

	T191_mem0 = S.Task('T191_mem0', length=1, delay_cost=1)
	S += T191_mem0 >= 55
	T191_mem0 += MAS_MEM[0]

	T191_mem1 = S.Task('T191_mem1', length=1, delay_cost=1)
	S += T191_mem1 >= 55
	T191_mem1 += MAS_MEM[7]

	T101 = S.Task('T101', length=1, delay_cost=1)
	S += T101 >= 56
	T101 += MAS[2]

	T14_t5_mem0 = S.Task('T14_t5_mem0', length=1, delay_cost=1)
	S += T14_t5_mem0 >= 56
	T14_t5_mem0 += MM_MEM[0]

	T14_t5_mem1 = S.Task('T14_t5_mem1', length=1, delay_cost=1)
	S += T14_t5_mem1 >= 56
	T14_t5_mem1 += MM_MEM[1]

	T191 = S.Task('T191', length=1, delay_cost=1)
	S += T191 >= 56
	T191 += MAS[0]

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	S += T211_mem0 >= 56
	T211_mem0 += MAS_MEM[6]

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	S += T211_mem1 >= 56
	T211_mem1 += MAS_MEM[5]

	T23_t3_in = S.Task('T23_t3_in', length=1, delay_cost=1)
	S += T23_t3_in >= 56
	T23_t3_in += MM_in[0]

	T23_t3_mem0 = S.Task('T23_t3_mem0', length=1, delay_cost=1)
	S += T23_t3_mem0 >= 56
	T23_t3_mem0 += MAS_MEM[2]

	T23_t3_mem1 = S.Task('T23_t3_mem1', length=1, delay_cost=1)
	S += T23_t3_mem1 >= 56
	T23_t3_mem1 += MAS_MEM[1]

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 57
	T141_mem0 += MM_MEM[0]

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 57
	T141_mem1 += MAS_MEM[3]

	T14_t5 = S.Task('T14_t5', length=1, delay_cost=1)
	S += T14_t5 >= 57
	T14_t5 += MAS[1]

	T20_t1_in = S.Task('T20_t1_in', length=1, delay_cost=1)
	S += T20_t1_in >= 57
	T20_t1_in += MM_in[0]

	T20_t1_mem0 = S.Task('T20_t1_mem0', length=1, delay_cost=1)
	S += T20_t1_mem0 >= 57
	T20_t1_mem0 += MAS_MEM[0]

	T20_t1_mem1 = S.Task('T20_t1_mem1', length=1, delay_cost=1)
	S += T20_t1_mem1 >= 57
	T20_t1_mem1 += MAS_MEM[7]

	T211 = S.Task('T211', length=1, delay_cost=1)
	S += T211 >= 57
	T211 += MAS[0]

	T23_t0_mem0 = S.Task('T23_t0_mem0', length=1, delay_cost=1)
	S += T23_t0_mem0 >= 57
	T23_t0_mem0 += MAS_MEM[2]

	T23_t0_mem1 = S.Task('T23_t0_mem1', length=1, delay_cost=1)
	S += T23_t0_mem1 >= 57
	T23_t0_mem1 += MAS_MEM[1]

	T23_t3 = S.Task('T23_t3', length=8, delay_cost=1)
	S += T23_t3 >= 57
	T23_t3 += MM[0]

	T141 = S.Task('T141', length=1, delay_cost=1)
	S += T141 >= 58
	T141 += MAS[1]

	T170_mem0 = S.Task('T170_mem0', length=1, delay_cost=1)
	S += T170_mem0 >= 58
	T170_mem0 += MM_MEM[0]

	T170_mem1 = S.Task('T170_mem1', length=1, delay_cost=1)
	S += T170_mem1 >= 58
	T170_mem1 += MM_MEM[1]

	T20_t1 = S.Task('T20_t1', length=8, delay_cost=1)
	S += T20_t1 >= 58
	T20_t1 += MM[0]

	T23_t0 = S.Task('T23_t0', length=1, delay_cost=1)
	S += T23_t0 >= 58
	T23_t0 += MAS[2]

	T23_t1_mem0 = S.Task('T23_t1_mem0', length=1, delay_cost=1)
	S += T23_t1_mem0 >= 58
	T23_t1_mem0 += MAS_MEM[2]

	T23_t1_mem1 = S.Task('T23_t1_mem1', length=1, delay_cost=1)
	S += T23_t1_mem1 >= 58
	T23_t1_mem1 += MAS_MEM[1]

	T16_t5_mem0 = S.Task('T16_t5_mem0', length=1, delay_cost=1)
	S += T16_t5_mem0 >= 59
	T16_t5_mem0 += MM_MEM[0]

	T16_t5_mem1 = S.Task('T16_t5_mem1', length=1, delay_cost=1)
	S += T16_t5_mem1 >= 59
	T16_t5_mem1 += MM_MEM[1]

	T170 = S.Task('T170', length=1, delay_cost=1)
	S += T170 >= 59
	T170 += MAS[0]

	T22_t0_mem0 = S.Task('T22_t0_mem0', length=1, delay_cost=1)
	S += T22_t0_mem0 >= 59
	T22_t0_mem0 += MAS_MEM[2]

	T22_t0_mem1 = S.Task('T22_t0_mem1', length=1, delay_cost=1)
	S += T22_t0_mem1 >= 59
	T22_t0_mem1 += MAS_MEM[1]

	T23_t1 = S.Task('T23_t1', length=1, delay_cost=1)
	S += T23_t1 >= 59
	T23_t1 += MAS[2]

	Z3_t3_mem0 = S.Task('Z3_t3_mem0', length=1, delay_cost=1)
	S += Z3_t3_mem0 >= 59
	Z3_t3_mem0 += MAS_MEM[0]

	Z3_t3_mem1 = S.Task('Z3_t3_mem1', length=1, delay_cost=1)
	S += Z3_t3_mem1 >= 59
	Z3_t3_mem1 += MAS_MEM[3]

	T16_t5 = S.Task('T16_t5', length=1, delay_cost=1)
	S += T16_t5 >= 60
	T16_t5 += MAS[3]

	T17_t5_mem0 = S.Task('T17_t5_mem0', length=1, delay_cost=1)
	S += T17_t5_mem0 >= 60
	T17_t5_mem0 += MM_MEM[0]

	T17_t5_mem1 = S.Task('T17_t5_mem1', length=1, delay_cost=1)
	S += T17_t5_mem1 >= 60
	T17_t5_mem1 += MM_MEM[1]

	T22_t0 = S.Task('T22_t0', length=1, delay_cost=1)
	S += T22_t0 >= 60
	T22_t0 += MAS[0]

	T22_t1_mem0 = S.Task('T22_t1_mem0', length=1, delay_cost=1)
	S += T22_t1_mem0 >= 60
	T22_t1_mem0 += MAS_MEM[2]

	T22_t1_mem1 = S.Task('T22_t1_mem1', length=1, delay_cost=1)
	S += T22_t1_mem1 >= 60
	T22_t1_mem1 += MAS_MEM[1]

	Z3_t3 = S.Task('Z3_t3', length=1, delay_cost=1)
	S += Z3_t3 >= 60
	Z3_t3 += MAS[1]

	Z3_t4_in = S.Task('Z3_t4_in', length=1, delay_cost=1)
	S += Z3_t4_in >= 60
	Z3_t4_in += MM_in[0]

	Z3_t4_mem0 = S.Task('Z3_t4_mem0', length=1, delay_cost=1)
	S += Z3_t4_mem0 >= 60
	Z3_t4_mem0 += MAS_MEM[6]

	Z3_t4_mem1 = S.Task('Z3_t4_mem1', length=1, delay_cost=1)
	S += Z3_t4_mem1 >= 60
	Z3_t4_mem1 += MAS_MEM[3]

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	S += T160_mem0 >= 61
	T160_mem0 += MM_MEM[0]

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	S += T160_mem1 >= 61
	T160_mem1 += MM_MEM[1]

	T17_t5 = S.Task('T17_t5', length=1, delay_cost=1)
	S += T17_t5 >= 61
	T17_t5 += MAS[1]

	T22_t1 = S.Task('T22_t1', length=1, delay_cost=1)
	S += T22_t1 >= 61
	T22_t1 += MAS[0]

	T22_t3_in = S.Task('T22_t3_in', length=1, delay_cost=1)
	S += T22_t3_in >= 61
	T22_t3_in += MM_in[0]

	T22_t3_mem0 = S.Task('T22_t3_mem0', length=1, delay_cost=1)
	S += T22_t3_mem0 >= 61
	T22_t3_mem0 += MAS_MEM[2]

	T22_t3_mem1 = S.Task('T22_t3_mem1', length=1, delay_cost=1)
	S += T22_t3_mem1 >= 61
	T22_t3_mem1 += MAS_MEM[1]

	Z3_t4 = S.Task('Z3_t4', length=8, delay_cost=1)
	S += Z3_t4 >= 61
	Z3_t4 += MM[0]

	T160 = S.Task('T160', length=1, delay_cost=1)
	S += T160 >= 62
	T160 += MAS[0]

	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	S += T161_mem0 >= 62
	T161_mem0 += MM_MEM[0]

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	S += T161_mem1 >= 62
	T161_mem1 += MAS_MEM[7]

	T22_t2_in = S.Task('T22_t2_in', length=1, delay_cost=1)
	S += T22_t2_in >= 62
	T22_t2_in += MM_in[0]

	T22_t2_mem0 = S.Task('T22_t2_mem0', length=1, delay_cost=1)
	S += T22_t2_mem0 >= 62
	T22_t2_mem0 += MAS_MEM[0]

	T22_t2_mem1 = S.Task('T22_t2_mem1', length=1, delay_cost=1)
	S += T22_t2_mem1 >= 62
	T22_t2_mem1 += MAS_MEM[1]

	T22_t3 = S.Task('T22_t3', length=8, delay_cost=1)
	S += T22_t3 >= 62
	T22_t3 += MM[0]

	T161 = S.Task('T161', length=1, delay_cost=1)
	S += T161 >= 63
	T161 += MAS[2]

	T171_mem0 = S.Task('T171_mem0', length=1, delay_cost=1)
	S += T171_mem0 >= 63
	T171_mem0 += MM_MEM[0]

	T171_mem1 = S.Task('T171_mem1', length=1, delay_cost=1)
	S += T171_mem1 >= 63
	T171_mem1 += MAS_MEM[3]

	T22_t2 = S.Task('T22_t2', length=8, delay_cost=1)
	S += T22_t2 >= 63
	T22_t2 += MM[0]

	T24_t4_in = S.Task('T24_t4_in', length=1, delay_cost=1)
	S += T24_t4_in >= 63
	T24_t4_in += MM_in[0]

	T24_t4_mem0 = S.Task('T24_t4_mem0', length=1, delay_cost=1)
	S += T24_t4_mem0 >= 63
	T24_t4_mem0 += MAS_MEM[6]

	T24_t4_mem1 = S.Task('T24_t4_mem1', length=1, delay_cost=1)
	S += T24_t4_mem1 >= 63
	T24_t4_mem1 += MAS_MEM[1]

	T171 = S.Task('T171', length=1, delay_cost=1)
	S += T171 >= 64
	T171 += MAS[2]

	T231_mem0 = S.Task('T231_mem0', length=1, delay_cost=1)
	S += T231_mem0 >= 64
	T231_mem0 += MM_MEM[0]

	T231_mem1 = S.Task('T231_mem1', length=1, delay_cost=1)
	S += T231_mem1 >= 64
	T231_mem1 += MM_MEM[1]

	T24_t4 = S.Task('T24_t4', length=8, delay_cost=1)
	S += T24_t4 >= 64
	T24_t4 += MM[0]

	Z3_t1_in = S.Task('Z3_t1_in', length=1, delay_cost=1)
	S += Z3_t1_in >= 64
	Z3_t1_in += MM_in[0]

	Z3_t1_mem0 = S.Task('Z3_t1_mem0', length=1, delay_cost=1)
	S += Z3_t1_mem0 >= 64
	Z3_t1_mem0 += MAIN_MEM_r[0]

	Z3_t1_mem1 = S.Task('Z3_t1_mem1', length=1, delay_cost=1)
	S += Z3_t1_mem1 >= 64
	Z3_t1_mem1 += MAS_MEM[3]

	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	S += T200_mem0 >= 65
	T200_mem0 += MM_MEM[0]

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	S += T200_mem1 >= 65
	T200_mem1 += MM_MEM[1]

	T231 = S.Task('T231', length=1, delay_cost=1)
	S += T231 >= 65
	T231 += MAS[0]

	X41_mem0 = S.Task('X41_mem0', length=1, delay_cost=1)
	S += X41_mem0 >= 65
	X41_mem0 += MAS_MEM[0]

	X41_mem1 = S.Task('X41_mem1', length=1, delay_cost=1)
	S += X41_mem1 >= 65
	X41_mem1 += MAS_MEM[5]

	Z3_t1 = S.Task('Z3_t1', length=8, delay_cost=1)
	S += Z3_t1 >= 65
	Z3_t1 += MM[0]

	T200 = S.Task('T200', length=1, delay_cost=1)
	S += T200 >= 66
	T200 += MAS[0]

	T250_mem0 = S.Task('T250_mem0', length=1, delay_cost=1)
	S += T250_mem0 >= 66
	T250_mem0 += MAS_MEM[0]

	T250_mem1 = S.Task('T250_mem1', length=1, delay_cost=1)
	S += T250_mem1 >= 66
	T250_mem1 += MAS_MEM[1]

	X41 = S.Task('X41', length=1, delay_cost=1)
	S += X41 >= 66
	X41 += MAS[1]

	T250 = S.Task('T250', length=1, delay_cost=1)
	S += T250 >= 67
	T250 += MAS[1]

	X41_w = S.Task('X41_w', length=1, delay_cost=1)
	S += X41_w >= 67
	X41_w += MAIN_MEM_w

	Z40_mem0 = S.Task('Z40_mem0', length=1, delay_cost=1)
	S += Z40_mem0 >= 67
	Z40_mem0 += MAS_MEM[0]

	Z40_mem1 = S.Task('Z40_mem1', length=1, delay_cost=1)
	S += Z40_mem1 >= 67
	Z40_mem1 += MAS_MEM[3]

	T23_t5_mem0 = S.Task('T23_t5_mem0', length=1, delay_cost=1)
	S += T23_t5_mem0 >= 68
	T23_t5_mem0 += MM_MEM[0]

	T23_t5_mem1 = S.Task('T23_t5_mem1', length=1, delay_cost=1)
	S += T23_t5_mem1 >= 68
	T23_t5_mem1 += MM_MEM[1]

	Z40 = S.Task('Z40', length=1, delay_cost=1)
	S += Z40 >= 68
	Z40 += MAS[2]

	T230_mem0 = S.Task('T230_mem0', length=1, delay_cost=1)
	S += T230_mem0 >= 69
	T230_mem0 += MM_MEM[0]

	T230_mem1 = S.Task('T230_mem1', length=1, delay_cost=1)
	S += T230_mem1 >= 69
	T230_mem1 += MAS_MEM[3]

	T23_t5 = S.Task('T23_t5', length=1, delay_cost=1)
	S += T23_t5 >= 69
	T23_t5 += MAS[1]

	Z40_w = S.Task('Z40_w', length=1, delay_cost=1)
	S += Z40_w >= 69
	Z40_w += MAIN_MEM_w

	T230 = S.Task('T230', length=1, delay_cost=1)
	S += T230 >= 70
	T230 += MAS[1]

	T240_mem0 = S.Task('T240_mem0', length=1, delay_cost=1)
	S += T240_mem0 >= 70
	T240_mem0 += MM_MEM[0]

	T240_mem1 = S.Task('T240_mem1', length=1, delay_cost=1)
	S += T240_mem1 >= 70
	T240_mem1 += MM_MEM[1]

	X40_mem0 = S.Task('X40_mem0', length=1, delay_cost=1)
	S += X40_mem0 >= 70
	X40_mem0 += MAS_MEM[2]

	X40_mem1 = S.Task('X40_mem1', length=1, delay_cost=1)
	S += X40_mem1 >= 70
	X40_mem1 += MAS_MEM[1]

	T22_t5_mem0 = S.Task('T22_t5_mem0', length=1, delay_cost=1)
	S += T22_t5_mem0 >= 71
	T22_t5_mem0 += MM_MEM[0]

	T22_t5_mem1 = S.Task('T22_t5_mem1', length=1, delay_cost=1)
	S += T22_t5_mem1 >= 71
	T22_t5_mem1 += MM_MEM[1]

	T240 = S.Task('T240', length=1, delay_cost=1)
	S += T240 >= 71
	T240 += MAS[0]

	X40 = S.Task('X40', length=1, delay_cost=1)
	S += X40 >= 71
	X40 += MAS[1]

	T220_mem0 = S.Task('T220_mem0', length=1, delay_cost=1)
	S += T220_mem0 >= 72
	T220_mem0 += MM_MEM[0]

	T220_mem1 = S.Task('T220_mem1', length=1, delay_cost=1)
	S += T220_mem1 >= 72
	T220_mem1 += MAS_MEM[1]

	T22_t5 = S.Task('T22_t5', length=1, delay_cost=1)
	S += T22_t5 >= 72
	T22_t5 += MAS[0]

	X40_w = S.Task('X40_w', length=1, delay_cost=1)
	S += X40_w >= 72
	X40_w += MAIN_MEM_w

	T220 = S.Task('T220', length=1, delay_cost=1)
	S += T220 >= 73
	T220 += MAS[1]

	T24_t5_mem0 = S.Task('T24_t5_mem0', length=1, delay_cost=1)
	S += T24_t5_mem0 >= 73
	T24_t5_mem0 += MM_MEM[0]

	T24_t5_mem1 = S.Task('T24_t5_mem1', length=1, delay_cost=1)
	S += T24_t5_mem1 >= 73
	T24_t5_mem1 += MM_MEM[1]

	X30_mem0 = S.Task('X30_mem0', length=1, delay_cost=1)
	S += X30_mem0 >= 73
	X30_mem0 += MAS_MEM[2]

	X30_mem1 = S.Task('X30_mem1', length=1, delay_cost=1)
	S += X30_mem1 >= 73
	X30_mem1 += MAS_MEM[1]

	T221_mem0 = S.Task('T221_mem0', length=1, delay_cost=1)
	S += T221_mem0 >= 74
	T221_mem0 += MM_MEM[0]

	T221_mem1 = S.Task('T221_mem1', length=1, delay_cost=1)
	S += T221_mem1 >= 74
	T221_mem1 += MM_MEM[1]

	T24_t5 = S.Task('T24_t5', length=1, delay_cost=1)
	S += T24_t5 >= 74
	T24_t5 += MAS[1]

	X30 = S.Task('X30', length=1, delay_cost=1)
	S += X30 >= 74
	X30 += MAS[0]

	T221 = S.Task('T221', length=1, delay_cost=1)
	S += T221 >= 75
	T221 += MAS[0]

	T241_mem0 = S.Task('T241_mem0', length=1, delay_cost=1)
	S += T241_mem0 >= 75
	T241_mem0 += MM_MEM[0]

	T241_mem1 = S.Task('T241_mem1', length=1, delay_cost=1)
	S += T241_mem1 >= 75
	T241_mem1 += MAS_MEM[3]

	X30_w = S.Task('X30_w', length=1, delay_cost=1)
	S += X30_w >= 75
	X30_w += MAIN_MEM_w

	T241 = S.Task('T241', length=1, delay_cost=1)
	S += T241 >= 76
	T241 += MAS[3]

	X31_mem0 = S.Task('X31_mem0', length=1, delay_cost=1)
	S += X31_mem0 >= 76
	X31_mem0 += MAS_MEM[0]

	X31_mem1 = S.Task('X31_mem1', length=1, delay_cost=1)
	S += X31_mem1 >= 76
	X31_mem1 += MAS_MEM[7]

	Z3_t5_mem0 = S.Task('Z3_t5_mem0', length=1, delay_cost=1)
	S += Z3_t5_mem0 >= 76
	Z3_t5_mem0 += MM_MEM[0]

	Z3_t5_mem1 = S.Task('Z3_t5_mem1', length=1, delay_cost=1)
	S += Z3_t5_mem1 >= 76
	Z3_t5_mem1 += MM_MEM[1]

	X31 = S.Task('X31', length=1, delay_cost=1)
	S += X31 >= 77
	X31 += MAS[1]

	Z30_mem0 = S.Task('Z30_mem0', length=1, delay_cost=1)
	S += Z30_mem0 >= 77
	Z30_mem0 += MM_MEM[0]

	Z30_mem1 = S.Task('Z30_mem1', length=1, delay_cost=1)
	S += Z30_mem1 >= 77
	Z30_mem1 += MM_MEM[1]

	Z3_t5 = S.Task('Z3_t5', length=1, delay_cost=1)
	S += Z3_t5 >= 77
	Z3_t5 += MAS[0]

	X31_w = S.Task('X31_w', length=1, delay_cost=1)
	S += X31_w >= 78
	X31_w += MAIN_MEM_w

	Z30 = S.Task('Z30', length=1, delay_cost=1)
	S += Z30 >= 78
	Z30 += MAS[2]

	Z31_mem0 = S.Task('Z31_mem0', length=1, delay_cost=1)
	S += Z31_mem0 >= 78
	Z31_mem0 += MM_MEM[0]

	Z31_mem1 = S.Task('Z31_mem1', length=1, delay_cost=1)
	S += Z31_mem1 >= 78
	Z31_mem1 += MAS_MEM[1]

	Z30_w = S.Task('Z30_w', length=1, delay_cost=1)
	S += Z30_w >= 79
	Z30_w += MAIN_MEM_w

	Z31 = S.Task('Z31', length=1, delay_cost=1)
	S += Z31 >= 79
	Z31 += MAS[0]

	Z31_w = S.Task('Z31_w', length=1, delay_cost=1)
	S += Z31_w >= 80
	Z31_w += MAIN_MEM_w


	# new tasks
	T20_t3 = S.Task('T20_t3', length=1, delay_cost=1)
	T20_t3 += alt(MAS)
	S += T20_t3<1000

	T20_t3_mem0 = S.Task('T20_t3_mem0', length=1, delay_cost=1)
	T20_t3_mem0 += MAS_MEM[4]
	S += 48 < T20_t3_mem0
	S += T20_t3_mem0 <= T20_t3

	T20_t3_mem1 = S.Task('T20_t3_mem1', length=1, delay_cost=1)
	T20_t3_mem1 += MAS_MEM[7]
	S += 55 < T20_t3_mem1
	S += T20_t3_mem1 <= T20_t3

	T20_t4 = S.Task('T20_t4', length=8, delay_cost=1)
	T20_t4 += alt(MM)
	T20_t4_in = S.Task('T20_t4_in', length=1, delay_cost=1)
	T20_t4_in += alt(MM_in)
	S += T20_t4_in*MM_in[0]<=T20_t4*MM[0]
	S += T20_t4<1000

	T20_t4_mem0 = S.Task('T20_t4_mem0', length=1, delay_cost=1)
	T20_t4_mem0 += MAS_MEM[0]
	S += 40 < T20_t4_mem0
	S += T20_t4_mem0 <= T20_t4

	T20_t4_mem1 = S.Task('T20_t4_mem1', length=1, delay_cost=1)
	T20_t4_mem1 += alt(MAS_MEM)
	S += (T20_t3*MAS[0])-1 < T20_t4_mem1*MAS_MEM[1]
	S += (T20_t3*MAS[1])-1 < T20_t4_mem1*MAS_MEM[3]
	S += (T20_t3*MAS[2])-1 < T20_t4_mem1*MAS_MEM[5]
	S += (T20_t3*MAS[3])-1 < T20_t4_mem1*MAS_MEM[7]
	S += T20_t4_mem1 <= T20_t4

	T20_t5 = S.Task('T20_t5', length=1, delay_cost=1)
	T20_t5 += alt(MAS)
	S += T20_t5<1000

	T20_t5_mem0 = S.Task('T20_t5_mem0', length=1, delay_cost=1)
	T20_t5_mem0 += MM_MEM[0]
	S += 56 < T20_t5_mem0
	S += T20_t5_mem0 <= T20_t5

	T20_t5_mem1 = S.Task('T20_t5_mem1', length=1, delay_cost=1)
	T20_t5_mem1 += MM_MEM[1]
	S += 65 < T20_t5_mem1
	S += T20_t5_mem1 <= T20_t5

	T23_t2 = S.Task('T23_t2', length=8, delay_cost=1)
	T23_t2 += alt(MM)
	T23_t2_in = S.Task('T23_t2_in', length=1, delay_cost=1)
	T23_t2_in += alt(MM_in)
	S += T23_t2_in*MM_in[0]<=T23_t2*MM[0]
	S += T23_t2<70

	T23_t2_mem0 = S.Task('T23_t2_mem0', length=1, delay_cost=1)
	T23_t2_mem0 += MAS_MEM[4]
	S += 58 < T23_t2_mem0
	S += T23_t2_mem0 <= T23_t2

	T23_t2_mem1 = S.Task('T23_t2_mem1', length=1, delay_cost=1)
	T23_t2_mem1 += MAS_MEM[5]
	S += 59 < T23_t2_mem1
	S += T23_t2_mem1 <= T23_t2

	T201 = S.Task('T201', length=1, delay_cost=1)
	T201 += alt(MAS)
	S += T201<1000

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	T201_mem0 += alt(MM_MEM)
	S += (T20_t4*MM[0])-1 < T201_mem0*MM_MEM[0]
	S += T201_mem0 <= T201

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	T201_mem1 += alt(MAS_MEM)
	S += (T20_t5*MAS[0])-1 < T201_mem1*MAS_MEM[1]
	S += (T20_t5*MAS[1])-1 < T201_mem1*MAS_MEM[3]
	S += (T20_t5*MAS[2])-1 < T201_mem1*MAS_MEM[5]
	S += (T20_t5*MAS[3])-1 < T201_mem1*MAS_MEM[7]
	S += T201_mem1 <= T201

	T251 = S.Task('T251', length=1, delay_cost=1)
	T251 += alt(MAS)
	S += T251<1000

	T251_mem0 = S.Task('T251_mem0', length=1, delay_cost=1)
	T251_mem0 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem0*MAS_MEM[0]
	S += (T201*MAS[1])-1 < T251_mem0*MAS_MEM[2]
	S += (T201*MAS[2])-1 < T251_mem0*MAS_MEM[4]
	S += (T201*MAS[3])-1 < T251_mem0*MAS_MEM[6]
	S += T251_mem0 <= T251

	T251_mem1 = S.Task('T251_mem1', length=1, delay_cost=1)
	T251_mem1 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem1*MAS_MEM[1]
	S += (T201*MAS[1])-1 < T251_mem1*MAS_MEM[3]
	S += (T201*MAS[2])-1 < T251_mem1*MAS_MEM[5]
	S += (T201*MAS[3])-1 < T251_mem1*MAS_MEM[7]
	S += T251_mem1 <= T251

	Z41 = S.Task('Z41', length=1, delay_cost=1)
	Z41 += alt(MAS)
	S += 0<Z41

	Z41_w = S.Task('Z41_w', length=1, delay_cost=1)
	Z41_w += alt(MAIN_MEM_w)
	S += Z41 <= Z41_w

	S += Z41<1000

	Z41_mem0 = S.Task('Z41_mem0', length=1, delay_cost=1)
	Z41_mem0 += MAS_MEM[4]
	S += 63 < Z41_mem0
	S += Z41_mem0 <= Z41

	Z41_mem1 = S.Task('Z41_mem1', length=1, delay_cost=1)
	Z41_mem1 += alt(MAS_MEM)
	S += (T251*MAS[0])-1 < Z41_mem1*MAS_MEM[1]
	S += (T251*MAS[1])-1 < Z41_mem1*MAS_MEM[3]
	S += (T251*MAS[2])-1 < Z41_mem1*MAS_MEM[5]
	S += (T251*MAS[3])-1 < Z41_mem1*MAS_MEM[7]
	S += Z41_mem1 <= Z41

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage1MAS4/EP2_LADDERMUL/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

