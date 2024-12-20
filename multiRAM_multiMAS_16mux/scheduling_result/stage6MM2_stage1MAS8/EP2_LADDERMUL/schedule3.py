from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 172
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=6)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	S += T7_t0_in >= 0
	T7_t0_in += MM_in[1]

	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	S += T7_t0_mem0 >= 0
	T7_t0_mem0 += MAIN_MEM_r[0]

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	S += T7_t0_mem1 >= 0
	T7_t0_mem1 += MAIN_MEM_r[1]

	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	S += T6_t0_in >= 1
	T6_t0_in += MM_in[0]

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	S += T6_t0_mem0 >= 1
	T6_t0_mem0 += MAIN_MEM_r[0]

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	S += T6_t0_mem1 >= 1
	T6_t0_mem1 += MAIN_MEM_r[1]

	T7_t0 = S.Task('T7_t0', length=6, delay_cost=1)
	S += T7_t0 >= 1
	T7_t0 += MM[1]

	T6_t0 = S.Task('T6_t0', length=6, delay_cost=1)
	S += T6_t0 >= 2
	T6_t0 += MM[0]

	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	S += T6_t1_in >= 2
	T6_t1_in += MM_in[0]

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	S += T6_t1_mem0 >= 2
	T6_t1_mem0 += MAIN_MEM_r[0]

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	S += T6_t1_mem1 >= 2
	T6_t1_mem1 += MAIN_MEM_r[1]

	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	S += T4_t1_in >= 3
	T4_t1_in += MM_in[0]

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	S += T4_t1_mem0 >= 3
	T4_t1_mem0 += MAIN_MEM_r[0]

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	S += T4_t1_mem1 >= 3
	T4_t1_mem1 += MAIN_MEM_r[1]

	T6_t1 = S.Task('T6_t1', length=6, delay_cost=1)
	S += T6_t1 >= 3
	T6_t1 += MM[0]

	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	S += T4_t0_in >= 4
	T4_t0_in += MM_in[1]

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	S += T4_t0_mem0 >= 4
	T4_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	S += T4_t0_mem1 >= 4
	T4_t0_mem1 += MAIN_MEM_r[1]

	T4_t1 = S.Task('T4_t1', length=6, delay_cost=1)
	S += T4_t1 >= 4
	T4_t1 += MM[0]

	T4_t0 = S.Task('T4_t0', length=6, delay_cost=1)
	S += T4_t0 >= 5
	T4_t0 += MM[1]

	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	S += T7_t1_in >= 5
	T7_t1_in += MM_in[0]

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	S += T7_t1_mem0 >= 5
	T7_t1_mem0 += MAIN_MEM_r[0]

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	S += T7_t1_mem1 >= 5
	T7_t1_mem1 += MAIN_MEM_r[1]

	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	S += T5_t3_in >= 6
	T5_t3_in += MM_in[0]

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	S += T5_t3_mem0 >= 6
	T5_t3_mem0 += MAIN_MEM_r[0]

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	S += T5_t3_mem1 >= 6
	T5_t3_mem1 += MAIN_MEM_r[1]

	T7_t1 = S.Task('T7_t1', length=6, delay_cost=1)
	S += T7_t1 >= 6
	T7_t1 += MM[0]

	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	S += T3_t1_in >= 7
	T3_t1_in += MM_in[0]

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	S += T3_t1_mem0 >= 7
	T3_t1_mem0 += MAIN_MEM_r[0]

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	S += T3_t1_mem1 >= 7
	T3_t1_mem1 += MAIN_MEM_r[1]

	T5_t3 = S.Task('T5_t3', length=6, delay_cost=1)
	S += T5_t3 >= 7
	T5_t3 += MM[0]

	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	S += T3_t0_in >= 8
	T3_t0_in += MM_in[0]

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	S += T3_t0_mem0 >= 8
	T3_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	S += T3_t0_mem1 >= 8
	T3_t0_mem1 += MAIN_MEM_r[1]

	T3_t1 = S.Task('T3_t1', length=6, delay_cost=1)
	S += T3_t1 >= 8
	T3_t1 += MM[0]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 8
	T60_mem0 += MM_MEM[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 8
	T60_mem1 += MM_MEM[1]

	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	S += T1_t3_in >= 9
	T1_t3_in += MM_in[1]

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	S += T1_t3_mem0 >= 9
	T1_t3_mem0 += MAIN_MEM_r[0]

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	S += T1_t3_mem1 >= 9
	T1_t3_mem1 += MAIN_MEM_r[1]

	T3_t0 = S.Task('T3_t0', length=6, delay_cost=1)
	S += T3_t0 >= 9
	T3_t0 += MM[0]

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 9
	T60 += MAS[6]

	T6_t5_mem0 = S.Task('T6_t5_mem0', length=1, delay_cost=1)
	S += T6_t5_mem0 >= 9
	T6_t5_mem0 += MM_MEM[0]

	T6_t5_mem1 = S.Task('T6_t5_mem1', length=1, delay_cost=1)
	S += T6_t5_mem1 >= 9
	T6_t5_mem1 += MM_MEM[1]

	T1_t3 = S.Task('T1_t3', length=6, delay_cost=1)
	S += T1_t3 >= 10
	T1_t3 += MM[1]

	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	S += T2_t1_in >= 10
	T2_t1_in += MM_in[1]

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	S += T2_t1_mem0 >= 10
	T2_t1_mem0 += MAIN_MEM_r[0]

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	S += T2_t1_mem1 >= 10
	T2_t1_mem1 += MAIN_MEM_r[1]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 10
	T40_mem0 += MM_MEM[2]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 10
	T40_mem1 += MM_MEM[1]

	T6_t5 = S.Task('T6_t5', length=1, delay_cost=1)
	S += T6_t5 >= 10
	T6_t5 += MAS[2]

	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	S += T2_t0_in >= 11
	T2_t0_in += MM_in[1]

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	S += T2_t0_mem0 >= 11
	T2_t0_mem0 += MAIN_MEM_r[0]

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	S += T2_t0_mem1 >= 11
	T2_t0_mem1 += MAIN_MEM_r[1]

	T2_t1 = S.Task('T2_t1', length=6, delay_cost=1)
	S += T2_t1 >= 11
	T2_t1 += MM[1]

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 11
	T40 += MAS[4]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 11
	T70_mem0 += MM_MEM[2]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 11
	T70_mem1 += MM_MEM[1]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	S += T11_t2_mem0 >= 12
	T11_t2_mem0 += MAIN_MEM_r[0]

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	S += T11_t2_mem1 >= 12
	T11_t2_mem1 += MAIN_MEM_r[1]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 12
	T150_mem0 += MAS_MEM[10]

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 12
	T150_mem1 += MAS_MEM[11]

	T2_t0 = S.Task('T2_t0', length=6, delay_cost=1)
	S += T2_t0 >= 12
	T2_t0 += MM[1]

	T4_t5_mem0 = S.Task('T4_t5_mem0', length=1, delay_cost=1)
	S += T4_t5_mem0 >= 12
	T4_t5_mem0 += MM_MEM[2]

	T4_t5_mem1 = S.Task('T4_t5_mem1', length=1, delay_cost=1)
	S += T4_t5_mem1 >= 12
	T4_t5_mem1 += MM_MEM[1]

	T70 = S.Task('T70', length=1, delay_cost=1)
	S += T70 >= 12
	T70 += MAS[5]

	T11_t2 = S.Task('T11_t2', length=1, delay_cost=1)
	S += T11_t2 >= 13
	T11_t2 += MAS[5]

	T150 = S.Task('T150', length=1, delay_cost=1)
	S += T150 >= 13
	T150 += MAS[6]

	T4_t5 = S.Task('T4_t5', length=1, delay_cost=1)
	S += T4_t5 >= 13
	T4_t5 += MAS[1]

	T7_t5_mem0 = S.Task('T7_t5_mem0', length=1, delay_cost=1)
	S += T7_t5_mem0 >= 13
	T7_t5_mem0 += MM_MEM[2]

	T7_t5_mem1 = S.Task('T7_t5_mem1', length=1, delay_cost=1)
	S += T7_t5_mem1 >= 13
	T7_t5_mem1 += MM_MEM[1]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	S += T9_t2_mem0 >= 13
	T9_t2_mem0 += MAIN_MEM_r[0]

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	S += T9_t2_mem1 >= 13
	T9_t2_mem1 += MAIN_MEM_r[1]

	T5_t5_mem0 = S.Task('T5_t5_mem0', length=1, delay_cost=1)
	S += T5_t5_mem0 >= 14
	T5_t5_mem0 += MM_MEM[0]

	T5_t5_mem1 = S.Task('T5_t5_mem1', length=1, delay_cost=1)
	S += T5_t5_mem1 >= 14
	T5_t5_mem1 += MM_MEM[1]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	S += T7_t3_mem0 >= 14
	T7_t3_mem0 += MAIN_MEM_r[0]

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	S += T7_t3_mem1 >= 14
	T7_t3_mem1 += MAIN_MEM_r[1]

	T7_t5 = S.Task('T7_t5', length=1, delay_cost=1)
	S += T7_t5 >= 14
	T7_t5 += MAS[7]

	T9_t2 = S.Task('T9_t2', length=1, delay_cost=1)
	S += T9_t2 >= 14
	T9_t2 += MAS[0]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	S += T10_t2_mem0 >= 15
	T10_t2_mem0 += MAIN_MEM_r[0]

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	S += T10_t2_mem1 >= 15
	T10_t2_mem1 += MAIN_MEM_r[1]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 15
	T11_mem0 += MM_MEM[2]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 15
	T11_mem1 += MM_MEM[3]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 15
	T51_mem0 += MM_MEM[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 15
	T51_mem1 += MM_MEM[1]

	T5_t5 = S.Task('T5_t5', length=1, delay_cost=1)
	S += T5_t5 >= 15
	T5_t5 += MAS[0]

	T7_t3 = S.Task('T7_t3', length=1, delay_cost=1)
	S += T7_t3 >= 15
	T7_t3 += MAS[4]

	T10_t2 = S.Task('T10_t2', length=1, delay_cost=1)
	S += T10_t2 >= 16
	T10_t2 += MAS[5]

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 16
	T11 += MAS[0]

	T1_t5_mem0 = S.Task('T1_t5_mem0', length=1, delay_cost=1)
	S += T1_t5_mem0 >= 16
	T1_t5_mem0 += MM_MEM[2]

	T1_t5_mem1 = S.Task('T1_t5_mem1', length=1, delay_cost=1)
	S += T1_t5_mem1 >= 16
	T1_t5_mem1 += MM_MEM[3]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 16
	T30_mem0 += MM_MEM[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 16
	T30_mem1 += MM_MEM[1]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 16
	T51 += MAS[3]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	S += T5_t1_mem0 >= 16
	T5_t1_mem0 += MAIN_MEM_r[0]

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	S += T5_t1_mem1 >= 16
	T5_t1_mem1 += MAIN_MEM_r[1]

	T1_t5 = S.Task('T1_t5', length=1, delay_cost=1)
	S += T1_t5 >= 17
	T1_t5 += MAS[3]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 17
	T20_mem0 += MM_MEM[2]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 17
	T20_mem1 += MM_MEM[3]

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 17
	T30 += MAS[7]

	T3_t5_mem0 = S.Task('T3_t5_mem0', length=1, delay_cost=1)
	S += T3_t5_mem0 >= 17
	T3_t5_mem0 += MM_MEM[0]

	T3_t5_mem1 = S.Task('T3_t5_mem1', length=1, delay_cost=1)
	S += T3_t5_mem1 >= 17
	T3_t5_mem1 += MM_MEM[1]

	T5_t1 = S.Task('T5_t1', length=1, delay_cost=1)
	S += T5_t1 >= 17
	T5_t1 += MAS[0]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	S += T6_t3_mem0 >= 17
	T6_t3_mem0 += MAIN_MEM_r[0]

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	S += T6_t3_mem1 >= 17
	T6_t3_mem1 += MAIN_MEM_r[1]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 18
	T130_mem0 += MAS_MEM[8]

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 18
	T130_mem1 += MAS_MEM[15]

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 18
	T20 += MAS[7]

	T2_t5_mem0 = S.Task('T2_t5_mem0', length=1, delay_cost=1)
	S += T2_t5_mem0 >= 18
	T2_t5_mem0 += MM_MEM[2]

	T2_t5_mem1 = S.Task('T2_t5_mem1', length=1, delay_cost=1)
	S += T2_t5_mem1 >= 18
	T2_t5_mem1 += MM_MEM[3]

	T3_t5 = S.Task('T3_t5', length=1, delay_cost=1)
	S += T3_t5 >= 18
	T3_t5 += MAS[4]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	S += T5_t0_mem0 >= 18
	T5_t0_mem0 += MAIN_MEM_r[0]

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	S += T5_t0_mem1 >= 18
	T5_t0_mem1 += MAIN_MEM_r[1]

	T6_t3 = S.Task('T6_t3', length=1, delay_cost=1)
	S += T6_t3 >= 18
	T6_t3 += MAS[1]

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	S += T120_mem0 >= 19
	T120_mem0 += MAS_MEM[8]

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	S += T120_mem1 >= 19
	T120_mem1 += MAS_MEM[15]

	T130 = S.Task('T130', length=1, delay_cost=1)
	S += T130 >= 19
	T130 += MAS[1]

	T14_t0_in = S.Task('T14_t0_in', length=1, delay_cost=1)
	S += T14_t0_in >= 19
	T14_t0_in += MM_in[0]

	T14_t0_mem0 = S.Task('T14_t0_mem0', length=1, delay_cost=1)
	S += T14_t0_mem0 >= 19
	T14_t0_mem0 += MAS_MEM[2]

	T14_t0_mem1 = S.Task('T14_t0_mem1', length=1, delay_cost=1)
	S += T14_t0_mem1 >= 19
	T14_t0_mem1 += MAS_MEM[3]

	T2_t5 = S.Task('T2_t5', length=1, delay_cost=1)
	S += T2_t5 >= 19
	T2_t5 += MAS[5]

	T5_t0 = S.Task('T5_t0', length=1, delay_cost=1)
	S += T5_t0 >= 19
	T5_t0 += MAS[0]

	T5_t2_in = S.Task('T5_t2_in', length=1, delay_cost=1)
	S += T5_t2_in >= 19
	T5_t2_in += MM_in[1]

	T5_t2_mem0 = S.Task('T5_t2_mem0', length=1, delay_cost=1)
	S += T5_t2_mem0 >= 19
	T5_t2_mem0 += MAS_MEM[0]

	T5_t2_mem1 = S.Task('T5_t2_mem1', length=1, delay_cost=1)
	S += T5_t2_mem1 >= 19
	T5_t2_mem1 += MAS_MEM[1]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	S += T8_t2_mem0 >= 19
	T8_t2_mem0 += MAIN_MEM_r[0]

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	S += T8_t2_mem1 >= 19
	T8_t2_mem1 += MAIN_MEM_r[1]

	T120 = S.Task('T120', length=1, delay_cost=1)
	S += T120 >= 20
	T120 += MAS[7]

	T14_t0 = S.Task('T14_t0', length=6, delay_cost=1)
	S += T14_t0 >= 20
	T14_t0 += MM[0]

	T5_t2 = S.Task('T5_t2', length=6, delay_cost=1)
	S += T5_t2 >= 20
	T5_t2 += MM[1]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	S += T6_t2_mem0 >= 20
	T6_t2_mem0 += MAIN_MEM_r[0]

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	S += T6_t2_mem1 >= 20
	T6_t2_mem1 += MAIN_MEM_r[1]

	T8_t2 = S.Task('T8_t2', length=1, delay_cost=1)
	S += T8_t2 >= 20
	T8_t2 += MAS[1]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	S += T1_t0_mem0 >= 21
	T1_t0_mem0 += MAIN_MEM_r[0]

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	S += T1_t0_mem1 >= 21
	T1_t0_mem1 += MAIN_MEM_r[1]

	T6_t2 = S.Task('T6_t2', length=1, delay_cost=1)
	S += T6_t2 >= 21
	T6_t2 += MAS[1]

	T6_t4_in = S.Task('T6_t4_in', length=1, delay_cost=1)
	S += T6_t4_in >= 21
	T6_t4_in += MM_in[1]

	T6_t4_mem0 = S.Task('T6_t4_mem0', length=1, delay_cost=1)
	S += T6_t4_mem0 >= 21
	T6_t4_mem0 += MAS_MEM[2]

	T6_t4_mem1 = S.Task('T6_t4_mem1', length=1, delay_cost=1)
	S += T6_t4_mem1 >= 21
	T6_t4_mem1 += MAS_MEM[3]

	T1_t0 = S.Task('T1_t0', length=1, delay_cost=1)
	S += T1_t0 >= 22
	T1_t0 += MAS[5]

	T6_t4 = S.Task('T6_t4', length=6, delay_cost=1)
	S += T6_t4 >= 22
	T6_t4 += MM[1]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	S += T7_t2_mem0 >= 22
	T7_t2_mem0 += MAIN_MEM_r[0]

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	S += T7_t2_mem1 >= 22
	T7_t2_mem1 += MAIN_MEM_r[1]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	S += T4_t3_mem0 >= 23
	T4_t3_mem0 += MAIN_MEM_r[0]

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	S += T4_t3_mem1 >= 23
	T4_t3_mem1 += MAIN_MEM_r[1]

	T7_t2 = S.Task('T7_t2', length=1, delay_cost=1)
	S += T7_t2 >= 23
	T7_t2 += MAS[7]

	T7_t4_in = S.Task('T7_t4_in', length=1, delay_cost=1)
	S += T7_t4_in >= 23
	T7_t4_in += MM_in[0]

	T7_t4_mem0 = S.Task('T7_t4_mem0', length=1, delay_cost=1)
	S += T7_t4_mem0 >= 23
	T7_t4_mem0 += MAS_MEM[14]

	T7_t4_mem1 = S.Task('T7_t4_mem1', length=1, delay_cost=1)
	S += T7_t4_mem1 >= 23
	T7_t4_mem1 += MAS_MEM[9]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	S += T4_t2_mem0 >= 24
	T4_t2_mem0 += MAIN_MEM_r[0]

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	S += T4_t2_mem1 >= 24
	T4_t2_mem1 += MAIN_MEM_r[1]

	T4_t3 = S.Task('T4_t3', length=1, delay_cost=1)
	S += T4_t3 >= 24
	T4_t3 += MAS[3]

	T7_t4 = S.Task('T7_t4', length=6, delay_cost=1)
	S += T7_t4 >= 24
	T7_t4 += MM[0]

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	S += T3_t3_mem0 >= 25
	T3_t3_mem0 += MAIN_MEM_r[0]

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	S += T3_t3_mem1 >= 25
	T3_t3_mem1 += MAIN_MEM_r[1]

	T4_t2 = S.Task('T4_t2', length=1, delay_cost=1)
	S += T4_t2 >= 25
	T4_t2 += MAS[3]

	T4_t4_in = S.Task('T4_t4_in', length=1, delay_cost=1)
	S += T4_t4_in >= 25
	T4_t4_in += MM_in[1]

	T4_t4_mem0 = S.Task('T4_t4_mem0', length=1, delay_cost=1)
	S += T4_t4_mem0 >= 25
	T4_t4_mem0 += MAS_MEM[6]

	T4_t4_mem1 = S.Task('T4_t4_mem1', length=1, delay_cost=1)
	S += T4_t4_mem1 >= 25
	T4_t4_mem1 += MAS_MEM[7]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 25
	T50_mem0 += MM_MEM[2]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 25
	T50_mem1 += MAS_MEM[1]

	T20_t2_mem0 = S.Task('T20_t2_mem0', length=1, delay_cost=1)
	S += T20_t2_mem0 >= 26
	T20_t2_mem0 += MAS_MEM[2]

	T20_t2_mem1 = S.Task('T20_t2_mem1', length=1, delay_cost=1)
	S += T20_t2_mem1 >= 26
	T20_t2_mem1 += MAS_MEM[7]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	S += T3_t2_mem0 >= 26
	T3_t2_mem0 += MAIN_MEM_r[0]

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	S += T3_t2_mem1 >= 26
	T3_t2_mem1 += MAIN_MEM_r[1]

	T3_t3 = S.Task('T3_t3', length=1, delay_cost=1)
	S += T3_t3 >= 26
	T3_t3 += MAS[0]

	T4_t4 = S.Task('T4_t4', length=6, delay_cost=1)
	S += T4_t4 >= 26
	T4_t4 += MM[1]

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 26
	T50 += MAS[1]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	S += T1_t1_mem0 >= 27
	T1_t1_mem0 += MAIN_MEM_r[0]

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	S += T1_t1_mem1 >= 27
	T1_t1_mem1 += MAIN_MEM_r[1]

	T20_t2 = S.Task('T20_t2', length=1, delay_cost=1)
	S += T20_t2 >= 27
	T20_t2 += MAS[7]

	T3_t2 = S.Task('T3_t2', length=1, delay_cost=1)
	S += T3_t2 >= 27
	T3_t2 += MAS[0]

	T3_t4_in = S.Task('T3_t4_in', length=1, delay_cost=1)
	S += T3_t4_in >= 27
	T3_t4_in += MM_in[1]

	T3_t4_mem0 = S.Task('T3_t4_mem0', length=1, delay_cost=1)
	S += T3_t4_mem0 >= 27
	T3_t4_mem0 += MAS_MEM[0]

	T3_t4_mem1 = S.Task('T3_t4_mem1', length=1, delay_cost=1)
	S += T3_t4_mem1 >= 27
	T3_t4_mem1 += MAS_MEM[1]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 27
	T61_mem0 += MM_MEM[2]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 27
	T61_mem1 += MAS_MEM[5]

	T1_t1 = S.Task('T1_t1', length=1, delay_cost=1)
	S += T1_t1 >= 28
	T1_t1 += MAS[0]

	T1_t2_in = S.Task('T1_t2_in', length=1, delay_cost=1)
	S += T1_t2_in >= 28
	T1_t2_in += MM_in[0]

	T1_t2_mem0 = S.Task('T1_t2_mem0', length=1, delay_cost=1)
	S += T1_t2_mem0 >= 28
	T1_t2_mem0 += MAS_MEM[10]

	T1_t2_mem1 = S.Task('T1_t2_mem1', length=1, delay_cost=1)
	S += T1_t2_mem1 >= 28
	T1_t2_mem1 += MAS_MEM[1]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	S += T2_t3_mem0 >= 28
	T2_t3_mem0 += MAIN_MEM_r[0]

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	S += T2_t3_mem1 >= 28
	T2_t3_mem1 += MAIN_MEM_r[1]

	T3_t4 = S.Task('T3_t4', length=6, delay_cost=1)
	S += T3_t4 >= 28
	T3_t4 += MM[1]

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 28
	T61 += MAS[6]

	T1_t2 = S.Task('T1_t2', length=6, delay_cost=1)
	S += T1_t2 >= 29
	T1_t2 += MM[0]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	S += T2_t2_mem0 >= 29
	T2_t2_mem0 += MAIN_MEM_r[0]

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	S += T2_t2_mem1 >= 29
	T2_t2_mem1 += MAIN_MEM_r[1]

	T2_t3 = S.Task('T2_t3', length=1, delay_cost=1)
	S += T2_t3 >= 29
	T2_t3 += MAS[2]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 29
	T71_mem0 += MM_MEM[0]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 29
	T71_mem1 += MAS_MEM[15]

	T10_t0_in = S.Task('T10_t0_in', length=1, delay_cost=1)
	S += T10_t0_in >= 30
	T10_t0_in += MM_in[1]

	T10_t0_mem0 = S.Task('T10_t0_mem0', length=1, delay_cost=1)
	S += T10_t0_mem0 >= 30
	T10_t0_mem0 += MAIN_MEM_r[0]

	T10_t0_mem1 = S.Task('T10_t0_mem1', length=1, delay_cost=1)
	S += T10_t0_mem1 >= 30
	T10_t0_mem1 += MAS_MEM[15]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 30
	T151_mem0 += MAS_MEM[0]

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 30
	T151_mem1 += MAS_MEM[1]

	T2_t2 = S.Task('T2_t2', length=1, delay_cost=1)
	S += T2_t2 >= 30
	T2_t2 += MAS[2]

	T2_t4_in = S.Task('T2_t4_in', length=1, delay_cost=1)
	S += T2_t4_in >= 30
	T2_t4_in += MM_in[0]

	T2_t4_mem0 = S.Task('T2_t4_mem0', length=1, delay_cost=1)
	S += T2_t4_mem0 >= 30
	T2_t4_mem0 += MAS_MEM[4]

	T2_t4_mem1 = S.Task('T2_t4_mem1', length=1, delay_cost=1)
	S += T2_t4_mem1 >= 30
	T2_t4_mem1 += MAS_MEM[5]

	T71 = S.Task('T71', length=1, delay_cost=1)
	S += T71 >= 30
	T71 += MAS[0]

	T10_t0 = S.Task('T10_t0', length=6, delay_cost=1)
	S += T10_t0 >= 31
	T10_t0 += MM[1]

	T151 = S.Task('T151', length=1, delay_cost=1)
	S += T151 >= 31
	T151 += MAS[6]

	T17_t3_mem0 = S.Task('T17_t3_mem0', length=1, delay_cost=1)
	S += T17_t3_mem0 >= 31
	T17_t3_mem0 += MAS_MEM[12]

	T17_t3_mem1 = S.Task('T17_t3_mem1', length=1, delay_cost=1)
	S += T17_t3_mem1 >= 31
	T17_t3_mem1 += MAS_MEM[13]

	T2_t4 = S.Task('T2_t4', length=6, delay_cost=1)
	S += T2_t4 >= 31
	T2_t4 += MM[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 31
	T41_mem0 += MM_MEM[2]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 31
	T41_mem1 += MAS_MEM[3]

	T9_t1_in = S.Task('T9_t1_in', length=1, delay_cost=1)
	S += T9_t1_in >= 31
	T9_t1_in += MM_in[1]

	T9_t1_mem0 = S.Task('T9_t1_mem0', length=1, delay_cost=1)
	S += T9_t1_mem0 >= 31
	T9_t1_mem0 += MAIN_MEM_r[0]

	T9_t1_mem1 = S.Task('T9_t1_mem1', length=1, delay_cost=1)
	S += T9_t1_mem1 >= 31
	T9_t1_mem1 += MAS_MEM[1]

	T17_t3 = S.Task('T17_t3', length=1, delay_cost=1)
	S += T17_t3 >= 32
	T17_t3 += MAS[0]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 32
	T41 += MAS[1]

	T8_t1_in = S.Task('T8_t1_in', length=1, delay_cost=1)
	S += T8_t1_in >= 32
	T8_t1_in += MM_in[0]

	T8_t1_mem0 = S.Task('T8_t1_mem0', length=1, delay_cost=1)
	S += T8_t1_mem0 >= 32
	T8_t1_mem0 += MAIN_MEM_r[0]

	T8_t1_mem1 = S.Task('T8_t1_mem1', length=1, delay_cost=1)
	S += T8_t1_mem1 >= 32
	T8_t1_mem1 += MAS_MEM[1]

	T9_t1 = S.Task('T9_t1', length=6, delay_cost=1)
	S += T9_t1 >= 32
	T9_t1 += MM[1]

	T11_t0_in = S.Task('T11_t0_in', length=1, delay_cost=1)
	S += T11_t0_in >= 33
	T11_t0_in += MM_in[0]

	T11_t0_mem0 = S.Task('T11_t0_mem0', length=1, delay_cost=1)
	S += T11_t0_mem0 >= 33
	T11_t0_mem0 += MAIN_MEM_r[0]

	T11_t0_mem1 = S.Task('T11_t0_mem1', length=1, delay_cost=1)
	S += T11_t0_mem1 >= 33
	T11_t0_mem1 += MAS_MEM[15]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 33
	T31_mem0 += MM_MEM[2]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 33
	T31_mem1 += MAS_MEM[9]

	T8_t1 = S.Task('T8_t1', length=6, delay_cost=1)
	S += T8_t1 >= 33
	T8_t1 += MM[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 34
	T10_mem0 += MM_MEM[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 34
	T10_mem1 += MAS_MEM[7]

	T11_t0 = S.Task('T11_t0', length=6, delay_cost=1)
	S += T11_t0 >= 34
	T11_t0 += MM[0]

	T11_t3_mem0 = S.Task('T11_t3_mem0', length=1, delay_cost=1)
	S += T11_t3_mem0 >= 34
	T11_t3_mem0 += MAS_MEM[14]

	T11_t3_mem1 = S.Task('T11_t3_mem1', length=1, delay_cost=1)
	S += T11_t3_mem1 >= 34
	T11_t3_mem1 += MAS_MEM[13]

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 34
	T31 += MAS[6]

	Z3_t2_mem0 = S.Task('Z3_t2_mem0', length=1, delay_cost=1)
	S += Z3_t2_mem0 >= 34
	Z3_t2_mem0 += MAIN_MEM_r[0]

	Z3_t2_mem1 = S.Task('Z3_t2_mem1', length=1, delay_cost=1)
	S += Z3_t2_mem1 >= 34
	Z3_t2_mem1 += MAIN_MEM_r[1]

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 35
	T10 += MAS[2]

	T10_t3_mem0 = S.Task('T10_t3_mem0', length=1, delay_cost=1)
	S += T10_t3_mem0 >= 35
	T10_t3_mem0 += MAS_MEM[14]

	T10_t3_mem1 = S.Task('T10_t3_mem1', length=1, delay_cost=1)
	S += T10_t3_mem1 >= 35
	T10_t3_mem1 += MAS_MEM[13]

	T11_t3 = S.Task('T11_t3', length=1, delay_cost=1)
	S += T11_t3 >= 35
	T11_t3 += MAS[0]

	T9_t0_in = S.Task('T9_t0_in', length=1, delay_cost=1)
	S += T9_t0_in >= 35
	T9_t0_in += MM_in[0]

	T9_t0_mem0 = S.Task('T9_t0_mem0', length=1, delay_cost=1)
	S += T9_t0_mem0 >= 35
	T9_t0_mem0 += MAIN_MEM_r[0]

	T9_t0_mem1 = S.Task('T9_t0_mem1', length=1, delay_cost=1)
	S += T9_t0_mem1 >= 35
	T9_t0_mem1 += MAS_MEM[5]

	T9_t3_mem0 = S.Task('T9_t3_mem0', length=1, delay_cost=1)
	S += T9_t3_mem0 >= 35
	T9_t3_mem0 += MAS_MEM[4]

	T9_t3_mem1 = S.Task('T9_t3_mem1', length=1, delay_cost=1)
	S += T9_t3_mem1 >= 35
	T9_t3_mem1 += MAS_MEM[1]

	Z3_t2 = S.Task('Z3_t2', length=1, delay_cost=1)
	S += Z3_t2 >= 35
	Z3_t2 += MAS[4]

	T10_t1_in = S.Task('T10_t1_in', length=1, delay_cost=1)
	S += T10_t1_in >= 36
	T10_t1_in += MM_in[0]

	T10_t1_mem0 = S.Task('T10_t1_mem0', length=1, delay_cost=1)
	S += T10_t1_mem0 >= 36
	T10_t1_mem0 += MAIN_MEM_r[0]

	T10_t1_mem1 = S.Task('T10_t1_mem1', length=1, delay_cost=1)
	S += T10_t1_mem1 >= 36
	T10_t1_mem1 += MAS_MEM[13]

	T10_t3 = S.Task('T10_t3', length=1, delay_cost=1)
	S += T10_t3 >= 36
	T10_t3 += MAS[4]

	T16_t2_mem0 = S.Task('T16_t2_mem0', length=1, delay_cost=1)
	S += T16_t2_mem0 >= 36
	T16_t2_mem0 += MAS_MEM[4]

	T16_t2_mem1 = S.Task('T16_t2_mem1', length=1, delay_cost=1)
	S += T16_t2_mem1 >= 36
	T16_t2_mem1 += MAS_MEM[1]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 36
	T21_mem0 += MM_MEM[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 36
	T21_mem1 += MAS_MEM[11]

	T9_t0 = S.Task('T9_t0', length=6, delay_cost=1)
	S += T9_t0 >= 36
	T9_t0 += MM[0]

	T9_t3 = S.Task('T9_t3', length=1, delay_cost=1)
	S += T9_t3 >= 36
	T9_t3 += MAS[3]

	T9_t4_in = S.Task('T9_t4_in', length=1, delay_cost=1)
	S += T9_t4_in >= 36
	T9_t4_in += MM_in[1]

	T9_t4_mem0 = S.Task('T9_t4_mem0', length=1, delay_cost=1)
	S += T9_t4_mem0 >= 36
	T9_t4_mem0 += MAS_MEM[0]

	T9_t4_mem1 = S.Task('T9_t4_mem1', length=1, delay_cost=1)
	S += T9_t4_mem1 >= 36
	T9_t4_mem1 += MAS_MEM[7]

	T10_t1 = S.Task('T10_t1', length=6, delay_cost=1)
	S += T10_t1 >= 37
	T10_t1 += MM[0]

	T10_t4_in = S.Task('T10_t4_in', length=1, delay_cost=1)
	S += T10_t4_in >= 37
	T10_t4_in += MM_in[1]

	T10_t4_mem0 = S.Task('T10_t4_mem0', length=1, delay_cost=1)
	S += T10_t4_mem0 >= 37
	T10_t4_mem0 += MAS_MEM[10]

	T10_t4_mem1 = S.Task('T10_t4_mem1', length=1, delay_cost=1)
	S += T10_t4_mem1 >= 37
	T10_t4_mem1 += MAS_MEM[9]

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	S += T121_mem0 >= 37
	T121_mem0 += MAS_MEM[2]

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	S += T121_mem1 >= 37
	T121_mem1 += MAS_MEM[3]

	T16_t2 = S.Task('T16_t2', length=1, delay_cost=1)
	S += T16_t2 >= 37
	T16_t2 += MAS[0]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 37
	T21 += MAS[1]

	T8_t0_in = S.Task('T8_t0_in', length=1, delay_cost=1)
	S += T8_t0_in >= 37
	T8_t0_in += MM_in[0]

	T8_t0_mem0 = S.Task('T8_t0_mem0', length=1, delay_cost=1)
	S += T8_t0_mem0 >= 37
	T8_t0_mem0 += MAIN_MEM_r[0]

	T8_t0_mem1 = S.Task('T8_t0_mem1', length=1, delay_cost=1)
	S += T8_t0_mem1 >= 37
	T8_t0_mem1 += MAS_MEM[5]

	T8_t3_mem0 = S.Task('T8_t3_mem0', length=1, delay_cost=1)
	S += T8_t3_mem0 >= 37
	T8_t3_mem0 += MAS_MEM[4]

	T8_t3_mem1 = S.Task('T8_t3_mem1', length=1, delay_cost=1)
	S += T8_t3_mem1 >= 37
	T8_t3_mem1 += MAS_MEM[1]

	T9_t4 = S.Task('T9_t4', length=6, delay_cost=1)
	S += T9_t4 >= 37
	T9_t4 += MM[1]

	T10_t4 = S.Task('T10_t4', length=6, delay_cost=1)
	S += T10_t4 >= 38
	T10_t4 += MM[1]

	T11_t1_in = S.Task('T11_t1_in', length=1, delay_cost=1)
	S += T11_t1_in >= 38
	T11_t1_in += MM_in[0]

	T11_t1_mem0 = S.Task('T11_t1_mem0', length=1, delay_cost=1)
	S += T11_t1_mem0 >= 38
	T11_t1_mem0 += MAIN_MEM_r[0]

	T11_t1_mem1 = S.Task('T11_t1_mem1', length=1, delay_cost=1)
	S += T11_t1_mem1 >= 38
	T11_t1_mem1 += MAS_MEM[13]

	T11_t4_in = S.Task('T11_t4_in', length=1, delay_cost=1)
	S += T11_t4_in >= 38
	T11_t4_in += MM_in[1]

	T11_t4_mem0 = S.Task('T11_t4_mem0', length=1, delay_cost=1)
	S += T11_t4_mem0 >= 38
	T11_t4_mem0 += MAS_MEM[10]

	T11_t4_mem1 = S.Task('T11_t4_mem1', length=1, delay_cost=1)
	S += T11_t4_mem1 >= 38
	T11_t4_mem1 += MAS_MEM[1]

	T121 = S.Task('T121', length=1, delay_cost=1)
	S += T121 >= 38
	T121 += MAS[5]

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 38
	T131_mem0 += MAS_MEM[2]

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 38
	T131_mem1 += MAS_MEM[3]

	T24_t3_mem0 = S.Task('T24_t3_mem0', length=1, delay_cost=1)
	S += T24_t3_mem0 >= 38
	T24_t3_mem0 += MAS_MEM[14]

	T24_t3_mem1 = S.Task('T24_t3_mem1', length=1, delay_cost=1)
	S += T24_t3_mem1 >= 38
	T24_t3_mem1 += MAS_MEM[11]

	T8_t0 = S.Task('T8_t0', length=6, delay_cost=1)
	S += T8_t0 >= 38
	T8_t0 += MM[0]

	T8_t3 = S.Task('T8_t3', length=1, delay_cost=1)
	S += T8_t3 >= 38
	T8_t3 += MAS[2]

	T11_t1 = S.Task('T11_t1', length=6, delay_cost=1)
	S += T11_t1 >= 39
	T11_t1 += MM[0]

	T11_t4 = S.Task('T11_t4', length=6, delay_cost=1)
	S += T11_t4 >= 39
	T11_t4 += MM[1]

	T131 = S.Task('T131', length=1, delay_cost=1)
	S += T131 >= 39
	T131 += MAS[7]

	T14_t1_in = S.Task('T14_t1_in', length=1, delay_cost=1)
	S += T14_t1_in >= 39
	T14_t1_in += MM_in[0]

	T14_t1_mem0 = S.Task('T14_t1_mem0', length=1, delay_cost=1)
	S += T14_t1_mem0 >= 39
	T14_t1_mem0 += MAS_MEM[14]

	T14_t1_mem1 = S.Task('T14_t1_mem1', length=1, delay_cost=1)
	S += T14_t1_mem1 >= 39
	T14_t1_mem1 += MAS_MEM[15]

	T24_t3 = S.Task('T24_t3', length=1, delay_cost=1)
	S += T24_t3 >= 39
	T24_t3 += MAS[4]

	T8_t4_in = S.Task('T8_t4_in', length=1, delay_cost=1)
	S += T8_t4_in >= 39
	T8_t4_in += MM_in[1]

	T8_t4_mem0 = S.Task('T8_t4_mem0', length=1, delay_cost=1)
	S += T8_t4_mem0 >= 39
	T8_t4_mem0 += MAS_MEM[2]

	T8_t4_mem1 = S.Task('T8_t4_mem1', length=1, delay_cost=1)
	S += T8_t4_mem1 >= 39
	T8_t4_mem1 += MAS_MEM[5]

	T14_t1 = S.Task('T14_t1', length=6, delay_cost=1)
	S += T14_t1 >= 40
	T14_t1 += MM[0]

	T14_t3_mem0 = S.Task('T14_t3_mem0', length=1, delay_cost=1)
	S += T14_t3_mem0 >= 40
	T14_t3_mem0 += MAS_MEM[2]

	T14_t3_mem1 = S.Task('T14_t3_mem1', length=1, delay_cost=1)
	S += T14_t3_mem1 >= 40
	T14_t3_mem1 += MAS_MEM[15]

	T8_t4 = S.Task('T8_t4', length=6, delay_cost=1)
	S += T8_t4 >= 40
	T8_t4 += MM[1]

	T14_t2_mem0 = S.Task('T14_t2_mem0', length=1, delay_cost=1)
	S += T14_t2_mem0 >= 41
	T14_t2_mem0 += MAS_MEM[2]

	T14_t2_mem1 = S.Task('T14_t2_mem1', length=1, delay_cost=1)
	S += T14_t2_mem1 >= 41
	T14_t2_mem1 += MAS_MEM[15]

	T14_t3 = S.Task('T14_t3', length=1, delay_cost=1)
	S += T14_t3 >= 41
	T14_t3 += MAS[6]

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	S += T90_mem0 >= 41
	T90_mem0 += MM_MEM[0]

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	S += T90_mem1 >= 41
	T90_mem1 += MM_MEM[3]

	T10_t5_mem0 = S.Task('T10_t5_mem0', length=1, delay_cost=1)
	S += T10_t5_mem0 >= 42
	T10_t5_mem0 += MM_MEM[2]

	T10_t5_mem1 = S.Task('T10_t5_mem1', length=1, delay_cost=1)
	S += T10_t5_mem1 >= 42
	T10_t5_mem1 += MM_MEM[1]

	T14_t2 = S.Task('T14_t2', length=1, delay_cost=1)
	S += T14_t2 >= 42
	T14_t2 += MAS[6]

	T14_t4_in = S.Task('T14_t4_in', length=1, delay_cost=1)
	S += T14_t4_in >= 42
	T14_t4_in += MM_in[0]

	T14_t4_mem0 = S.Task('T14_t4_mem0', length=1, delay_cost=1)
	S += T14_t4_mem0 >= 42
	T14_t4_mem0 += MAS_MEM[12]

	T14_t4_mem1 = S.Task('T14_t4_mem1', length=1, delay_cost=1)
	S += T14_t4_mem1 >= 42
	T14_t4_mem1 += MAS_MEM[13]

	T180_mem0 = S.Task('T180_mem0', length=1, delay_cost=1)
	S += T180_mem0 >= 42
	T180_mem0 += MAS_MEM[2]

	T180_mem1 = S.Task('T180_mem1', length=1, delay_cost=1)
	S += T180_mem1 >= 42
	T180_mem1 += MAS_MEM[3]

	T90 = S.Task('T90', length=1, delay_cost=1)
	S += T90 >= 42
	T90 += MAS[1]

	T9_t5_mem0 = S.Task('T9_t5_mem0', length=1, delay_cost=1)
	S += T9_t5_mem0 >= 42
	T9_t5_mem0 += MM_MEM[0]

	T9_t5_mem1 = S.Task('T9_t5_mem1', length=1, delay_cost=1)
	S += T9_t5_mem1 >= 42
	T9_t5_mem1 += MM_MEM[3]

	T10_t5 = S.Task('T10_t5', length=1, delay_cost=1)
	S += T10_t5 >= 43
	T10_t5 += MAS[3]

	T14_t4 = S.Task('T14_t4', length=6, delay_cost=1)
	S += T14_t4 >= 43
	T14_t4 += MM[0]

	T180 = S.Task('T180', length=1, delay_cost=1)
	S += T180 >= 43
	T180 += MAS[2]

	T20_t0_in = S.Task('T20_t0_in', length=1, delay_cost=1)
	S += T20_t0_in >= 43
	T20_t0_in += MM_in[1]

	T20_t0_mem0 = S.Task('T20_t0_mem0', length=1, delay_cost=1)
	S += T20_t0_mem0 >= 43
	T20_t0_mem0 += MAS_MEM[2]

	T20_t0_mem1 = S.Task('T20_t0_mem1', length=1, delay_cost=1)
	S += T20_t0_mem1 >= 43
	T20_t0_mem1 += MAS_MEM[5]

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	S += T80_mem0 >= 43
	T80_mem0 += MM_MEM[0]

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	S += T80_mem1 >= 43
	T80_mem1 += MM_MEM[1]

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	S += T91_mem0 >= 43
	T91_mem0 += MM_MEM[2]

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	S += T91_mem1 >= 43
	T91_mem1 += MAS_MEM[15]

	T9_t5 = S.Task('T9_t5', length=1, delay_cost=1)
	S += T9_t5 >= 43
	T9_t5 += MAS[7]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 44
	T101_mem0 += MM_MEM[2]

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 44
	T101_mem1 += MAS_MEM[7]

	T16_t0_in = S.Task('T16_t0_in', length=1, delay_cost=1)
	S += T16_t0_in >= 44
	T16_t0_in += MM_in[1]

	T16_t0_mem0 = S.Task('T16_t0_mem0', length=1, delay_cost=1)
	S += T16_t0_mem0 >= 44
	T16_t0_mem0 += MAS_MEM[4]

	T16_t0_mem1 = S.Task('T16_t0_mem1', length=1, delay_cost=1)
	S += T16_t0_mem1 >= 44
	T16_t0_mem1 += MAS_MEM[15]

	T17_t0_in = S.Task('T17_t0_in', length=1, delay_cost=1)
	S += T17_t0_in >= 44
	T17_t0_in += MM_in[0]

	T17_t0_mem0 = S.Task('T17_t0_mem0', length=1, delay_cost=1)
	S += T17_t0_mem0 >= 44
	T17_t0_mem0 += MAS_MEM[14]

	T17_t0_mem1 = S.Task('T17_t0_mem1', length=1, delay_cost=1)
	S += T17_t0_mem1 >= 44
	T17_t0_mem1 += MAS_MEM[13]

	T190_mem0 = S.Task('T190_mem0', length=1, delay_cost=1)
	S += T190_mem0 >= 44
	T190_mem0 += MAS_MEM[2]

	T190_mem1 = S.Task('T190_mem1', length=1, delay_cost=1)
	S += T190_mem1 >= 44
	T190_mem1 += MAS_MEM[3]

	T191_mem0 = S.Task('T191_mem0', length=1, delay_cost=1)
	S += T191_mem0 >= 44
	T191_mem0 += MAS_MEM[6]

	T191_mem1 = S.Task('T191_mem1', length=1, delay_cost=1)
	S += T191_mem1 >= 44
	T191_mem1 += MAS_MEM[1]

	T20_t0 = S.Task('T20_t0', length=6, delay_cost=1)
	S += T20_t0 >= 44
	T20_t0 += MM[1]

	T80 = S.Task('T80', length=1, delay_cost=1)
	S += T80 >= 44
	T80 += MAS[7]

	T8_t5_mem0 = S.Task('T8_t5_mem0', length=1, delay_cost=1)
	S += T8_t5_mem0 >= 44
	T8_t5_mem0 += MM_MEM[0]

	T8_t5_mem1 = S.Task('T8_t5_mem1', length=1, delay_cost=1)
	S += T8_t5_mem1 >= 44
	T8_t5_mem1 += MM_MEM[1]

	T91 = S.Task('T91', length=1, delay_cost=1)
	S += T91 >= 44
	T91 += MAS[0]

	T101 = S.Task('T101', length=1, delay_cost=1)
	S += T101 >= 45
	T101 += MAS[4]

	T11_t5_mem0 = S.Task('T11_t5_mem0', length=1, delay_cost=1)
	S += T11_t5_mem0 >= 45
	T11_t5_mem0 += MM_MEM[0]

	T11_t5_mem1 = S.Task('T11_t5_mem1', length=1, delay_cost=1)
	S += T11_t5_mem1 >= 45
	T11_t5_mem1 += MM_MEM[1]

	T16_t0 = S.Task('T16_t0', length=6, delay_cost=1)
	S += T16_t0 >= 45
	T16_t0 += MM[1]

	T17_t0 = S.Task('T17_t0', length=6, delay_cost=1)
	S += T17_t0 >= 45
	T17_t0 += MM[0]

	T181_mem0 = S.Task('T181_mem0', length=1, delay_cost=1)
	S += T181_mem0 >= 45
	T181_mem0 += MAS_MEM[6]

	T181_mem1 = S.Task('T181_mem1', length=1, delay_cost=1)
	S += T181_mem1 >= 45
	T181_mem1 += MAS_MEM[1]

	T190 = S.Task('T190', length=1, delay_cost=1)
	S += T190 >= 45
	T190 += MAS[1]

	T191 = S.Task('T191', length=1, delay_cost=1)
	S += T191 >= 45
	T191 += MAS[0]

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	S += T211_mem0 >= 45
	T211_mem0 += MAS_MEM[12]

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	S += T211_mem1 >= 45
	T211_mem1 += MAS_MEM[9]

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	S += T81_mem0 >= 45
	T81_mem0 += MM_MEM[2]

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	S += T81_mem1 >= 45
	T81_mem1 += MAS_MEM[11]

	T8_t5 = S.Task('T8_t5', length=1, delay_cost=1)
	S += T8_t5 >= 45
	T8_t5 += MAS[5]

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	S += T110_mem0 >= 46
	T110_mem0 += MM_MEM[0]

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	S += T110_mem1 >= 46
	T110_mem1 += MM_MEM[1]

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	S += T111_mem0 >= 46
	T111_mem0 += MM_MEM[2]

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	S += T111_mem1 >= 46
	T111_mem1 += MAS_MEM[3]

	T11_t5 = S.Task('T11_t5', length=1, delay_cost=1)
	S += T11_t5 >= 46
	T11_t5 += MAS[1]

	T16_t1_in = S.Task('T16_t1_in', length=1, delay_cost=1)
	S += T16_t1_in >= 46
	T16_t1_in += MM_in[1]

	T16_t1_mem0 = S.Task('T16_t1_mem0', length=1, delay_cost=1)
	S += T16_t1_mem0 >= 46
	T16_t1_mem0 += MAS_MEM[0]

	T16_t1_mem1 = S.Task('T16_t1_mem1', length=1, delay_cost=1)
	S += T16_t1_mem1 >= 46
	T16_t1_mem1 += MAS_MEM[7]

	T17_t1_in = S.Task('T17_t1_in', length=1, delay_cost=1)
	S += T17_t1_in >= 46
	T17_t1_in += MM_in[0]

	T17_t1_mem0 = S.Task('T17_t1_mem0', length=1, delay_cost=1)
	S += T17_t1_mem0 >= 46
	T17_t1_mem0 += MAS_MEM[6]

	T17_t1_mem1 = S.Task('T17_t1_mem1', length=1, delay_cost=1)
	S += T17_t1_mem1 >= 46
	T17_t1_mem1 += MAS_MEM[13]

	T181 = S.Task('T181', length=1, delay_cost=1)
	S += T181 >= 46
	T181 += MAS[5]

	T211 = S.Task('T211', length=1, delay_cost=1)
	S += T211 >= 46
	T211 += MAS[2]

	T81 = S.Task('T81', length=1, delay_cost=1)
	S += T81 >= 46
	T81 += MAS[3]

	T110 = S.Task('T110', length=1, delay_cost=1)
	S += T110 >= 47
	T110 += MAS[0]

	T111 = S.Task('T111', length=1, delay_cost=1)
	S += T111 >= 47
	T111 += MAS[5]

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 47
	T140_mem0 += MM_MEM[0]

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 47
	T140_mem1 += MM_MEM[1]

	T16_t1 = S.Task('T16_t1', length=6, delay_cost=1)
	S += T16_t1 >= 47
	T16_t1 += MM[1]

	T16_t3_mem0 = S.Task('T16_t3_mem0', length=1, delay_cost=1)
	S += T16_t3_mem0 >= 47
	T16_t3_mem0 += MAS_MEM[14]

	T16_t3_mem1 = S.Task('T16_t3_mem1', length=1, delay_cost=1)
	S += T16_t3_mem1 >= 47
	T16_t3_mem1 += MAS_MEM[7]

	T17_t1 = S.Task('T17_t1', length=6, delay_cost=1)
	S += T17_t1 >= 47
	T17_t1 += MM[0]

	T24_t0_in = S.Task('T24_t0_in', length=1, delay_cost=1)
	S += T24_t0_in >= 47
	T24_t0_in += MM_in[1]

	T24_t0_mem0 = S.Task('T24_t0_mem0', length=1, delay_cost=1)
	S += T24_t0_mem0 >= 47
	T24_t0_mem0 += MAS_MEM[0]

	T24_t0_mem1 = S.Task('T24_t0_mem1', length=1, delay_cost=1)
	S += T24_t0_mem1 >= 47
	T24_t0_mem1 += MAS_MEM[15]

	T24_t1_in = S.Task('T24_t1_in', length=1, delay_cost=1)
	S += T24_t1_in >= 47
	T24_t1_in += MM_in[0]

	T24_t1_mem0 = S.Task('T24_t1_mem0', length=1, delay_cost=1)
	S += T24_t1_mem0 >= 47
	T24_t1_mem0 += MAS_MEM[10]

	T24_t1_mem1 = S.Task('T24_t1_mem1', length=1, delay_cost=1)
	S += T24_t1_mem1 >= 47
	T24_t1_mem1 += MAS_MEM[11]

	T140 = S.Task('T140', length=1, delay_cost=1)
	S += T140 >= 48
	T140 += MAS[4]

	T14_t5_mem0 = S.Task('T14_t5_mem0', length=1, delay_cost=1)
	S += T14_t5_mem0 >= 48
	T14_t5_mem0 += MM_MEM[0]

	T14_t5_mem1 = S.Task('T14_t5_mem1', length=1, delay_cost=1)
	S += T14_t5_mem1 >= 48
	T14_t5_mem1 += MM_MEM[1]

	T16_t3 = S.Task('T16_t3', length=1, delay_cost=1)
	S += T16_t3 >= 48
	T16_t3 += MAS[1]

	T17_t2_mem0 = S.Task('T17_t2_mem0', length=1, delay_cost=1)
	S += T17_t2_mem0 >= 48
	T17_t2_mem0 += MAS_MEM[14]

	T17_t2_mem1 = S.Task('T17_t2_mem1', length=1, delay_cost=1)
	S += T17_t2_mem1 >= 48
	T17_t2_mem1 += MAS_MEM[7]

	T24_t0 = S.Task('T24_t0', length=6, delay_cost=1)
	S += T24_t0 >= 48
	T24_t0 += MM[1]

	T24_t1 = S.Task('T24_t1', length=6, delay_cost=1)
	S += T24_t1 >= 48
	T24_t1 += MM[0]

	T24_t2_mem0 = S.Task('T24_t2_mem0', length=1, delay_cost=1)
	S += T24_t2_mem0 >= 48
	T24_t2_mem0 += MAS_MEM[0]

	T24_t2_mem1 = S.Task('T24_t2_mem1', length=1, delay_cost=1)
	S += T24_t2_mem1 >= 48
	T24_t2_mem1 += MAS_MEM[11]

	Z3_t0_in = S.Task('Z3_t0_in', length=1, delay_cost=1)
	S += Z3_t0_in >= 48
	Z3_t0_in += MM_in[1]

	Z3_t0_mem0 = S.Task('Z3_t0_mem0', length=1, delay_cost=1)
	S += Z3_t0_mem0 >= 48
	Z3_t0_mem0 += MAIN_MEM_r[0]

	Z3_t0_mem1 = S.Task('Z3_t0_mem1', length=1, delay_cost=1)
	S += Z3_t0_mem1 >= 48
	Z3_t0_mem1 += MAS_MEM[9]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 49
	T100_mem0 += MM_MEM[2]

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 49
	T100_mem1 += MM_MEM[1]

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 49
	T141_mem0 += MM_MEM[0]

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 49
	T141_mem1 += MAS_MEM[3]

	T14_t5 = S.Task('T14_t5', length=1, delay_cost=1)
	S += T14_t5 >= 49
	T14_t5 += MAS[1]

	T17_t2 = S.Task('T17_t2', length=1, delay_cost=1)
	S += T17_t2 >= 49
	T17_t2 += MAS[0]

	T24_t2 = S.Task('T24_t2', length=1, delay_cost=1)
	S += T24_t2 >= 49
	T24_t2 += MAS[2]

	Z3_t0 = S.Task('Z3_t0', length=6, delay_cost=1)
	S += Z3_t0 >= 49
	Z3_t0 += MM[1]

	T100 = S.Task('T100', length=1, delay_cost=1)
	S += T100 >= 50
	T100 += MAS[7]

	T141 = S.Task('T141', length=1, delay_cost=1)
	S += T141 >= 50
	T141 += MAS[0]

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	S += T210_mem0 >= 50
	T210_mem0 += MAS_MEM[12]

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	S += T210_mem1 >= 50
	T210_mem1 += MAS_MEM[15]

	T210 = S.Task('T210', length=1, delay_cost=1)
	S += T210 >= 51
	T210 += MAS[7]


	# new tasks
	T16_t4 = S.Task('T16_t4', length=6, delay_cost=1)
	T16_t4 += alt(MM)
	T16_t4_in = S.Task('T16_t4_in', length=1, delay_cost=1)
	T16_t4_in += alt(MM_in)
	S += T16_t4_in*MM_in[0]<=T16_t4*MM[0]
	S += T16_t4_in*MM_in[1]<=T16_t4*MM[1]
	T16_t4_mem0 = S.Task('T16_t4_mem0', length=1, delay_cost=1)
	T16_t4_mem0 += MAS_MEM[0]
	S += 37 < T16_t4_mem0
	S += T16_t4_mem0 <= T16_t4

	T16_t4_mem1 = S.Task('T16_t4_mem1', length=1, delay_cost=1)
	T16_t4_mem1 += MAS_MEM[3]
	S += 48 < T16_t4_mem1
	S += T16_t4_mem1 <= T16_t4

	T160 = S.Task('T160', length=1, delay_cost=1)
	T160 += alt(MAS)
	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	T160_mem0 += MM_MEM[2]
	S += 50 < T160_mem0
	S += T160_mem0 <= T160

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	T160_mem1 += MM_MEM[3]
	S += 52 < T160_mem1
	S += T160_mem1 <= T160

	T16_t5 = S.Task('T16_t5', length=1, delay_cost=1)
	T16_t5 += alt(MAS)
	T16_t5_mem0 = S.Task('T16_t5_mem0', length=1, delay_cost=1)
	T16_t5_mem0 += MM_MEM[2]
	S += 50 < T16_t5_mem0
	S += T16_t5_mem0 <= T16_t5

	T16_t5_mem1 = S.Task('T16_t5_mem1', length=1, delay_cost=1)
	T16_t5_mem1 += MM_MEM[3]
	S += 52 < T16_t5_mem1
	S += T16_t5_mem1 <= T16_t5

	T17_t4 = S.Task('T17_t4', length=6, delay_cost=1)
	T17_t4 += alt(MM)
	T17_t4_in = S.Task('T17_t4_in', length=1, delay_cost=1)
	T17_t4_in += alt(MM_in)
	S += T17_t4_in*MM_in[0]<=T17_t4*MM[0]
	S += T17_t4_in*MM_in[1]<=T17_t4*MM[1]
	T17_t4_mem0 = S.Task('T17_t4_mem0', length=1, delay_cost=1)
	T17_t4_mem0 += MAS_MEM[0]
	S += 49 < T17_t4_mem0
	S += T17_t4_mem0 <= T17_t4

	T17_t4_mem1 = S.Task('T17_t4_mem1', length=1, delay_cost=1)
	T17_t4_mem1 += MAS_MEM[1]
	S += 32 < T17_t4_mem1
	S += T17_t4_mem1 <= T17_t4

	T170 = S.Task('T170', length=1, delay_cost=1)
	T170 += alt(MAS)
	T170_mem0 = S.Task('T170_mem0', length=1, delay_cost=1)
	T170_mem0 += MM_MEM[0]
	S += 50 < T170_mem0
	S += T170_mem0 <= T170

	T170_mem1 = S.Task('T170_mem1', length=1, delay_cost=1)
	T170_mem1 += MM_MEM[1]
	S += 52 < T170_mem1
	S += T170_mem1 <= T170

	T17_t5 = S.Task('T17_t5', length=1, delay_cost=1)
	T17_t5 += alt(MAS)
	T17_t5_mem0 = S.Task('T17_t5_mem0', length=1, delay_cost=1)
	T17_t5_mem0 += MM_MEM[0]
	S += 50 < T17_t5_mem0
	S += T17_t5_mem0 <= T17_t5

	T17_t5_mem1 = S.Task('T17_t5_mem1', length=1, delay_cost=1)
	T17_t5_mem1 += MM_MEM[1]
	S += 52 < T17_t5_mem1
	S += T17_t5_mem1 <= T17_t5

	T20_t1 = S.Task('T20_t1', length=6, delay_cost=1)
	T20_t1 += alt(MM)
	T20_t1_in = S.Task('T20_t1_in', length=1, delay_cost=1)
	T20_t1_in += alt(MM_in)
	S += T20_t1_in*MM_in[0]<=T20_t1*MM[0]
	S += T20_t1_in*MM_in[1]<=T20_t1*MM[1]
	T20_t1_mem0 = S.Task('T20_t1_mem0', length=1, delay_cost=1)
	T20_t1_mem0 += MAS_MEM[6]
	S += 16 < T20_t1_mem0
	S += T20_t1_mem0 <= T20_t1

	T20_t1_mem1 = S.Task('T20_t1_mem1', length=1, delay_cost=1)
	T20_t1_mem1 += MAS_MEM[11]
	S += 46 < T20_t1_mem1
	S += T20_t1_mem1 <= T20_t1

	T20_t3 = S.Task('T20_t3', length=1, delay_cost=1)
	T20_t3 += alt(MAS)
	T20_t3_mem0 = S.Task('T20_t3_mem0', length=1, delay_cost=1)
	T20_t3_mem0 += MAS_MEM[4]
	S += 43 < T20_t3_mem0
	S += T20_t3_mem0 <= T20_t3

	T20_t3_mem1 = S.Task('T20_t3_mem1', length=1, delay_cost=1)
	T20_t3_mem1 += MAS_MEM[11]
	S += 46 < T20_t3_mem1
	S += T20_t3_mem1 <= T20_t3

	T22_t0 = S.Task('T22_t0', length=1, delay_cost=1)
	T22_t0 += alt(MAS)
	T22_t0_mem0 = S.Task('T22_t0_mem0', length=1, delay_cost=1)
	T22_t0_mem0 += MAS_MEM[14]
	S += 51 < T22_t0_mem0
	S += T22_t0_mem0 <= T22_t0

	T22_t0_mem1 = S.Task('T22_t0_mem1', length=1, delay_cost=1)
	T22_t0_mem1 += MAS_MEM[5]
	S += 46 < T22_t0_mem1
	S += T22_t0_mem1 <= T22_t0

	T22_t1 = S.Task('T22_t1', length=1, delay_cost=1)
	T22_t1 += alt(MAS)
	T22_t1_mem0 = S.Task('T22_t1_mem0', length=1, delay_cost=1)
	T22_t1_mem0 += MAS_MEM[14]
	S += 51 < T22_t1_mem0
	S += T22_t1_mem0 <= T22_t1

	T22_t1_mem1 = S.Task('T22_t1_mem1', length=1, delay_cost=1)
	T22_t1_mem1 += MAS_MEM[5]
	S += 46 < T22_t1_mem1
	S += T22_t1_mem1 <= T22_t1

	T22_t3 = S.Task('T22_t3', length=6, delay_cost=1)
	T22_t3 += alt(MM)
	T22_t3_in = S.Task('T22_t3_in', length=1, delay_cost=1)
	T22_t3_in += alt(MM_in)
	S += T22_t3_in*MM_in[0]<=T22_t3*MM[0]
	S += T22_t3_in*MM_in[1]<=T22_t3*MM[1]
	T22_t3_mem0 = S.Task('T22_t3_mem0', length=1, delay_cost=1)
	T22_t3_mem0 += MAS_MEM[14]
	S += 51 < T22_t3_mem0
	S += T22_t3_mem0 <= T22_t3

	T22_t3_mem1 = S.Task('T22_t3_mem1', length=1, delay_cost=1)
	T22_t3_mem1 += MAS_MEM[5]
	S += 46 < T22_t3_mem1
	S += T22_t3_mem1 <= T22_t3

	T23_t0 = S.Task('T23_t0', length=1, delay_cost=1)
	T23_t0 += alt(MAS)
	T23_t0_mem0 = S.Task('T23_t0_mem0', length=1, delay_cost=1)
	T23_t0_mem0 += MAS_MEM[2]
	S += 45 < T23_t0_mem0
	S += T23_t0_mem0 <= T23_t0

	T23_t0_mem1 = S.Task('T23_t0_mem1', length=1, delay_cost=1)
	T23_t0_mem1 += MAS_MEM[1]
	S += 45 < T23_t0_mem1
	S += T23_t0_mem1 <= T23_t0

	T23_t1 = S.Task('T23_t1', length=1, delay_cost=1)
	T23_t1 += alt(MAS)
	T23_t1_mem0 = S.Task('T23_t1_mem0', length=1, delay_cost=1)
	T23_t1_mem0 += MAS_MEM[2]
	S += 45 < T23_t1_mem0
	S += T23_t1_mem0 <= T23_t1

	T23_t1_mem1 = S.Task('T23_t1_mem1', length=1, delay_cost=1)
	T23_t1_mem1 += MAS_MEM[1]
	S += 45 < T23_t1_mem1
	S += T23_t1_mem1 <= T23_t1

	T23_t3 = S.Task('T23_t3', length=6, delay_cost=1)
	T23_t3 += alt(MM)
	T23_t3_in = S.Task('T23_t3_in', length=1, delay_cost=1)
	T23_t3_in += alt(MM_in)
	S += T23_t3_in*MM_in[0]<=T23_t3*MM[0]
	S += T23_t3_in*MM_in[1]<=T23_t3*MM[1]
	T23_t3_mem0 = S.Task('T23_t3_mem0', length=1, delay_cost=1)
	T23_t3_mem0 += MAS_MEM[2]
	S += 45 < T23_t3_mem0
	S += T23_t3_mem0 <= T23_t3

	T23_t3_mem1 = S.Task('T23_t3_mem1', length=1, delay_cost=1)
	T23_t3_mem1 += MAS_MEM[1]
	S += 45 < T23_t3_mem1
	S += T23_t3_mem1 <= T23_t3

	T24_t4 = S.Task('T24_t4', length=6, delay_cost=1)
	T24_t4 += alt(MM)
	T24_t4_in = S.Task('T24_t4_in', length=1, delay_cost=1)
	T24_t4_in += alt(MM_in)
	S += T24_t4_in*MM_in[0]<=T24_t4*MM[0]
	S += T24_t4_in*MM_in[1]<=T24_t4*MM[1]
	T24_t4_mem0 = S.Task('T24_t4_mem0', length=1, delay_cost=1)
	T24_t4_mem0 += MAS_MEM[4]
	S += 49 < T24_t4_mem0
	S += T24_t4_mem0 <= T24_t4

	T24_t4_mem1 = S.Task('T24_t4_mem1', length=1, delay_cost=1)
	T24_t4_mem1 += MAS_MEM[9]
	S += 39 < T24_t4_mem1
	S += T24_t4_mem1 <= T24_t4

	T240 = S.Task('T240', length=1, delay_cost=1)
	T240 += alt(MAS)
	T240_mem0 = S.Task('T240_mem0', length=1, delay_cost=1)
	T240_mem0 += MM_MEM[2]
	S += 53 < T240_mem0
	S += T240_mem0 <= T240

	T240_mem1 = S.Task('T240_mem1', length=1, delay_cost=1)
	T240_mem1 += MM_MEM[1]
	S += 53 < T240_mem1
	S += T240_mem1 <= T240

	T24_t5 = S.Task('T24_t5', length=1, delay_cost=1)
	T24_t5 += alt(MAS)
	T24_t5_mem0 = S.Task('T24_t5_mem0', length=1, delay_cost=1)
	T24_t5_mem0 += MM_MEM[2]
	S += 53 < T24_t5_mem0
	S += T24_t5_mem0 <= T24_t5

	T24_t5_mem1 = S.Task('T24_t5_mem1', length=1, delay_cost=1)
	T24_t5_mem1 += MM_MEM[1]
	S += 53 < T24_t5_mem1
	S += T24_t5_mem1 <= T24_t5

	Z3_t1 = S.Task('Z3_t1', length=6, delay_cost=1)
	Z3_t1 += alt(MM)
	Z3_t1_in = S.Task('Z3_t1_in', length=1, delay_cost=1)
	Z3_t1_in += alt(MM_in)
	S += Z3_t1_in*MM_in[0]<=Z3_t1*MM[0]
	S += Z3_t1_in*MM_in[1]<=Z3_t1*MM[1]
	Z3_t1_mem0 = S.Task('Z3_t1_mem0', length=1, delay_cost=1)
	Z3_t1_mem0 += MAIN_MEM_r[0]
	S += Z3_t1_mem0 <= Z3_t1

	Z3_t1_mem1 = S.Task('Z3_t1_mem1', length=1, delay_cost=1)
	Z3_t1_mem1 += MAS_MEM[1]
	S += 50 < Z3_t1_mem1
	S += Z3_t1_mem1 <= Z3_t1

	Z3_t3 = S.Task('Z3_t3', length=1, delay_cost=1)
	Z3_t3 += alt(MAS)
	Z3_t3_mem0 = S.Task('Z3_t3_mem0', length=1, delay_cost=1)
	Z3_t3_mem0 += MAS_MEM[8]
	S += 48 < Z3_t3_mem0
	S += Z3_t3_mem0 <= Z3_t3

	Z3_t3_mem1 = S.Task('Z3_t3_mem1', length=1, delay_cost=1)
	Z3_t3_mem1 += MAS_MEM[1]
	S += 50 < Z3_t3_mem1
	S += Z3_t3_mem1 <= Z3_t3

	T161 = S.Task('T161', length=1, delay_cost=1)
	T161 += alt(MAS)
	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	T161_mem0 += alt(MM_MEM)
	S += (T16_t4*MM[0])-1 < T161_mem0*MM_MEM[0]
	S += (T16_t4*MM[1])-1 < T161_mem0*MM_MEM[2]
	S += T161_mem0 <= T161

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	T161_mem1 += alt(MAS_MEM)
	S += (T16_t5*MAS[0])-1 < T161_mem1*MAS_MEM[1]
	S += (T16_t5*MAS[1])-1 < T161_mem1*MAS_MEM[3]
	S += (T16_t5*MAS[2])-1 < T161_mem1*MAS_MEM[5]
	S += (T16_t5*MAS[3])-1 < T161_mem1*MAS_MEM[7]
	S += (T16_t5*MAS[4])-1 < T161_mem1*MAS_MEM[9]
	S += (T16_t5*MAS[5])-1 < T161_mem1*MAS_MEM[11]
	S += (T16_t5*MAS[6])-1 < T161_mem1*MAS_MEM[13]
	S += (T16_t5*MAS[7])-1 < T161_mem1*MAS_MEM[15]
	S += T161_mem1 <= T161

	T171 = S.Task('T171', length=1, delay_cost=1)
	T171 += alt(MAS)
	T171_mem0 = S.Task('T171_mem0', length=1, delay_cost=1)
	T171_mem0 += alt(MM_MEM)
	S += (T17_t4*MM[0])-1 < T171_mem0*MM_MEM[0]
	S += (T17_t4*MM[1])-1 < T171_mem0*MM_MEM[2]
	S += T171_mem0 <= T171

	T171_mem1 = S.Task('T171_mem1', length=1, delay_cost=1)
	T171_mem1 += alt(MAS_MEM)
	S += (T17_t5*MAS[0])-1 < T171_mem1*MAS_MEM[1]
	S += (T17_t5*MAS[1])-1 < T171_mem1*MAS_MEM[3]
	S += (T17_t5*MAS[2])-1 < T171_mem1*MAS_MEM[5]
	S += (T17_t5*MAS[3])-1 < T171_mem1*MAS_MEM[7]
	S += (T17_t5*MAS[4])-1 < T171_mem1*MAS_MEM[9]
	S += (T17_t5*MAS[5])-1 < T171_mem1*MAS_MEM[11]
	S += (T17_t5*MAS[6])-1 < T171_mem1*MAS_MEM[13]
	S += (T17_t5*MAS[7])-1 < T171_mem1*MAS_MEM[15]
	S += T171_mem1 <= T171

	T20_t4 = S.Task('T20_t4', length=6, delay_cost=1)
	T20_t4 += alt(MM)
	T20_t4_in = S.Task('T20_t4_in', length=1, delay_cost=1)
	T20_t4_in += alt(MM_in)
	S += T20_t4_in*MM_in[0]<=T20_t4*MM[0]
	S += T20_t4_in*MM_in[1]<=T20_t4*MM[1]
	T20_t4_mem0 = S.Task('T20_t4_mem0', length=1, delay_cost=1)
	T20_t4_mem0 += MAS_MEM[14]
	S += 27 < T20_t4_mem0
	S += T20_t4_mem0 <= T20_t4

	T20_t4_mem1 = S.Task('T20_t4_mem1', length=1, delay_cost=1)
	T20_t4_mem1 += alt(MAS_MEM)
	S += (T20_t3*MAS[0])-1 < T20_t4_mem1*MAS_MEM[1]
	S += (T20_t3*MAS[1])-1 < T20_t4_mem1*MAS_MEM[3]
	S += (T20_t3*MAS[2])-1 < T20_t4_mem1*MAS_MEM[5]
	S += (T20_t3*MAS[3])-1 < T20_t4_mem1*MAS_MEM[7]
	S += (T20_t3*MAS[4])-1 < T20_t4_mem1*MAS_MEM[9]
	S += (T20_t3*MAS[5])-1 < T20_t4_mem1*MAS_MEM[11]
	S += (T20_t3*MAS[6])-1 < T20_t4_mem1*MAS_MEM[13]
	S += (T20_t3*MAS[7])-1 < T20_t4_mem1*MAS_MEM[15]
	S += T20_t4_mem1 <= T20_t4

	T200 = S.Task('T200', length=1, delay_cost=1)
	T200 += alt(MAS)
	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	T200_mem0 += MM_MEM[2]
	S += 49 < T200_mem0
	S += T200_mem0 <= T200

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	T200_mem1 += alt(MM_MEM)
	S += (T20_t1*MM[0])-1 < T200_mem1*MM_MEM[1]
	S += (T20_t1*MM[1])-1 < T200_mem1*MM_MEM[3]
	S += T200_mem1 <= T200

	T20_t5 = S.Task('T20_t5', length=1, delay_cost=1)
	T20_t5 += alt(MAS)
	T20_t5_mem0 = S.Task('T20_t5_mem0', length=1, delay_cost=1)
	T20_t5_mem0 += MM_MEM[2]
	S += 49 < T20_t5_mem0
	S += T20_t5_mem0 <= T20_t5

	T20_t5_mem1 = S.Task('T20_t5_mem1', length=1, delay_cost=1)
	T20_t5_mem1 += alt(MM_MEM)
	S += (T20_t1*MM[0])-1 < T20_t5_mem1*MM_MEM[1]
	S += (T20_t1*MM[1])-1 < T20_t5_mem1*MM_MEM[3]
	S += T20_t5_mem1 <= T20_t5

	T22_t2 = S.Task('T22_t2', length=6, delay_cost=1)
	T22_t2 += alt(MM)
	T22_t2_in = S.Task('T22_t2_in', length=1, delay_cost=1)
	T22_t2_in += alt(MM_in)
	S += T22_t2_in*MM_in[0]<=T22_t2*MM[0]
	S += T22_t2_in*MM_in[1]<=T22_t2*MM[1]
	T22_t2_mem0 = S.Task('T22_t2_mem0', length=1, delay_cost=1)
	T22_t2_mem0 += alt(MAS_MEM)
	S += (T22_t0*MAS[0])-1 < T22_t2_mem0*MAS_MEM[0]
	S += (T22_t0*MAS[1])-1 < T22_t2_mem0*MAS_MEM[2]
	S += (T22_t0*MAS[2])-1 < T22_t2_mem0*MAS_MEM[4]
	S += (T22_t0*MAS[3])-1 < T22_t2_mem0*MAS_MEM[6]
	S += (T22_t0*MAS[4])-1 < T22_t2_mem0*MAS_MEM[8]
	S += (T22_t0*MAS[5])-1 < T22_t2_mem0*MAS_MEM[10]
	S += (T22_t0*MAS[6])-1 < T22_t2_mem0*MAS_MEM[12]
	S += (T22_t0*MAS[7])-1 < T22_t2_mem0*MAS_MEM[14]
	S += T22_t2_mem0 <= T22_t2

	T22_t2_mem1 = S.Task('T22_t2_mem1', length=1, delay_cost=1)
	T22_t2_mem1 += alt(MAS_MEM)
	S += (T22_t1*MAS[0])-1 < T22_t2_mem1*MAS_MEM[1]
	S += (T22_t1*MAS[1])-1 < T22_t2_mem1*MAS_MEM[3]
	S += (T22_t1*MAS[2])-1 < T22_t2_mem1*MAS_MEM[5]
	S += (T22_t1*MAS[3])-1 < T22_t2_mem1*MAS_MEM[7]
	S += (T22_t1*MAS[4])-1 < T22_t2_mem1*MAS_MEM[9]
	S += (T22_t1*MAS[5])-1 < T22_t2_mem1*MAS_MEM[11]
	S += (T22_t1*MAS[6])-1 < T22_t2_mem1*MAS_MEM[13]
	S += (T22_t1*MAS[7])-1 < T22_t2_mem1*MAS_MEM[15]
	S += T22_t2_mem1 <= T22_t2

	T22_t5 = S.Task('T22_t5', length=1, delay_cost=1)
	T22_t5 += alt(MAS)
	T22_t5_mem0 = S.Task('T22_t5_mem0', length=1, delay_cost=1)
	T22_t5_mem0 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T22_t5_mem0*MM_MEM[0]
	S += (T22_t3*MM[1])-1 < T22_t5_mem0*MM_MEM[2]
	S += T22_t5_mem0 <= T22_t5

	T22_t5_mem1 = S.Task('T22_t5_mem1', length=1, delay_cost=1)
	T22_t5_mem1 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T22_t5_mem1*MM_MEM[1]
	S += (T22_t3*MM[1])-1 < T22_t5_mem1*MM_MEM[3]
	S += T22_t5_mem1 <= T22_t5

	T221 = S.Task('T221', length=1, delay_cost=1)
	T221 += alt(MAS)
	T221_mem0 = S.Task('T221_mem0', length=1, delay_cost=1)
	T221_mem0 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T221_mem0*MM_MEM[0]
	S += (T22_t3*MM[1])-1 < T221_mem0*MM_MEM[2]
	S += T221_mem0 <= T221

	T221_mem1 = S.Task('T221_mem1', length=1, delay_cost=1)
	T221_mem1 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T221_mem1*MM_MEM[1]
	S += (T22_t3*MM[1])-1 < T221_mem1*MM_MEM[3]
	S += T221_mem1 <= T221

	T23_t2 = S.Task('T23_t2', length=6, delay_cost=1)
	T23_t2 += alt(MM)
	T23_t2_in = S.Task('T23_t2_in', length=1, delay_cost=1)
	T23_t2_in += alt(MM_in)
	S += T23_t2_in*MM_in[0]<=T23_t2*MM[0]
	S += T23_t2_in*MM_in[1]<=T23_t2*MM[1]
	T23_t2_mem0 = S.Task('T23_t2_mem0', length=1, delay_cost=1)
	T23_t2_mem0 += alt(MAS_MEM)
	S += (T23_t0*MAS[0])-1 < T23_t2_mem0*MAS_MEM[0]
	S += (T23_t0*MAS[1])-1 < T23_t2_mem0*MAS_MEM[2]
	S += (T23_t0*MAS[2])-1 < T23_t2_mem0*MAS_MEM[4]
	S += (T23_t0*MAS[3])-1 < T23_t2_mem0*MAS_MEM[6]
	S += (T23_t0*MAS[4])-1 < T23_t2_mem0*MAS_MEM[8]
	S += (T23_t0*MAS[5])-1 < T23_t2_mem0*MAS_MEM[10]
	S += (T23_t0*MAS[6])-1 < T23_t2_mem0*MAS_MEM[12]
	S += (T23_t0*MAS[7])-1 < T23_t2_mem0*MAS_MEM[14]
	S += T23_t2_mem0 <= T23_t2

	T23_t2_mem1 = S.Task('T23_t2_mem1', length=1, delay_cost=1)
	T23_t2_mem1 += alt(MAS_MEM)
	S += (T23_t1*MAS[0])-1 < T23_t2_mem1*MAS_MEM[1]
	S += (T23_t1*MAS[1])-1 < T23_t2_mem1*MAS_MEM[3]
	S += (T23_t1*MAS[2])-1 < T23_t2_mem1*MAS_MEM[5]
	S += (T23_t1*MAS[3])-1 < T23_t2_mem1*MAS_MEM[7]
	S += (T23_t1*MAS[4])-1 < T23_t2_mem1*MAS_MEM[9]
	S += (T23_t1*MAS[5])-1 < T23_t2_mem1*MAS_MEM[11]
	S += (T23_t1*MAS[6])-1 < T23_t2_mem1*MAS_MEM[13]
	S += (T23_t1*MAS[7])-1 < T23_t2_mem1*MAS_MEM[15]
	S += T23_t2_mem1 <= T23_t2

	T23_t5 = S.Task('T23_t5', length=1, delay_cost=1)
	T23_t5 += alt(MAS)
	T23_t5_mem0 = S.Task('T23_t5_mem0', length=1, delay_cost=1)
	T23_t5_mem0 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T23_t5_mem0*MM_MEM[0]
	S += (T23_t3*MM[1])-1 < T23_t5_mem0*MM_MEM[2]
	S += T23_t5_mem0 <= T23_t5

	T23_t5_mem1 = S.Task('T23_t5_mem1', length=1, delay_cost=1)
	T23_t5_mem1 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T23_t5_mem1*MM_MEM[1]
	S += (T23_t3*MM[1])-1 < T23_t5_mem1*MM_MEM[3]
	S += T23_t5_mem1 <= T23_t5

	T231 = S.Task('T231', length=1, delay_cost=1)
	T231 += alt(MAS)
	T231_mem0 = S.Task('T231_mem0', length=1, delay_cost=1)
	T231_mem0 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T231_mem0*MM_MEM[0]
	S += (T23_t3*MM[1])-1 < T231_mem0*MM_MEM[2]
	S += T231_mem0 <= T231

	T231_mem1 = S.Task('T231_mem1', length=1, delay_cost=1)
	T231_mem1 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T231_mem1*MM_MEM[1]
	S += (T23_t3*MM[1])-1 < T231_mem1*MM_MEM[3]
	S += T231_mem1 <= T231

	T241 = S.Task('T241', length=1, delay_cost=1)
	T241 += alt(MAS)
	T241_mem0 = S.Task('T241_mem0', length=1, delay_cost=1)
	T241_mem0 += alt(MM_MEM)
	S += (T24_t4*MM[0])-1 < T241_mem0*MM_MEM[0]
	S += (T24_t4*MM[1])-1 < T241_mem0*MM_MEM[2]
	S += T241_mem0 <= T241

	T241_mem1 = S.Task('T241_mem1', length=1, delay_cost=1)
	T241_mem1 += alt(MAS_MEM)
	S += (T24_t5*MAS[0])-1 < T241_mem1*MAS_MEM[1]
	S += (T24_t5*MAS[1])-1 < T241_mem1*MAS_MEM[3]
	S += (T24_t5*MAS[2])-1 < T241_mem1*MAS_MEM[5]
	S += (T24_t5*MAS[3])-1 < T241_mem1*MAS_MEM[7]
	S += (T24_t5*MAS[4])-1 < T241_mem1*MAS_MEM[9]
	S += (T24_t5*MAS[5])-1 < T241_mem1*MAS_MEM[11]
	S += (T24_t5*MAS[6])-1 < T241_mem1*MAS_MEM[13]
	S += (T24_t5*MAS[7])-1 < T241_mem1*MAS_MEM[15]
	S += T241_mem1 <= T241

	Z3_t4 = S.Task('Z3_t4', length=6, delay_cost=1)
	Z3_t4 += alt(MM)
	Z3_t4_in = S.Task('Z3_t4_in', length=1, delay_cost=1)
	Z3_t4_in += alt(MM_in)
	S += Z3_t4_in*MM_in[0]<=Z3_t4*MM[0]
	S += Z3_t4_in*MM_in[1]<=Z3_t4*MM[1]
	Z3_t4_mem0 = S.Task('Z3_t4_mem0', length=1, delay_cost=1)
	Z3_t4_mem0 += MAS_MEM[8]
	S += 35 < Z3_t4_mem0
	S += Z3_t4_mem0 <= Z3_t4

	Z3_t4_mem1 = S.Task('Z3_t4_mem1', length=1, delay_cost=1)
	Z3_t4_mem1 += alt(MAS_MEM)
	S += (Z3_t3*MAS[0])-1 < Z3_t4_mem1*MAS_MEM[1]
	S += (Z3_t3*MAS[1])-1 < Z3_t4_mem1*MAS_MEM[3]
	S += (Z3_t3*MAS[2])-1 < Z3_t4_mem1*MAS_MEM[5]
	S += (Z3_t3*MAS[3])-1 < Z3_t4_mem1*MAS_MEM[7]
	S += (Z3_t3*MAS[4])-1 < Z3_t4_mem1*MAS_MEM[9]
	S += (Z3_t3*MAS[5])-1 < Z3_t4_mem1*MAS_MEM[11]
	S += (Z3_t3*MAS[6])-1 < Z3_t4_mem1*MAS_MEM[13]
	S += (Z3_t3*MAS[7])-1 < Z3_t4_mem1*MAS_MEM[15]
	S += Z3_t4_mem1 <= Z3_t4

	Z30 = S.Task('Z30', length=1, delay_cost=1)
	Z30 += alt(MAS)
	S += 0<Z30

	Z30_w = S.Task('Z30_w', length=1, delay_cost=1)
	Z30_w += alt(MAIN_MEM_w)
	S += Z30 <= Z30_w

	Z30_mem0 = S.Task('Z30_mem0', length=1, delay_cost=1)
	Z30_mem0 += MM_MEM[2]
	S += 54 < Z30_mem0
	S += Z30_mem0 <= Z30

	Z30_mem1 = S.Task('Z30_mem1', length=1, delay_cost=1)
	Z30_mem1 += alt(MM_MEM)
	S += (Z3_t1*MM[0])-1 < Z30_mem1*MM_MEM[1]
	S += (Z3_t1*MM[1])-1 < Z30_mem1*MM_MEM[3]
	S += Z30_mem1 <= Z30

	Z3_t5 = S.Task('Z3_t5', length=1, delay_cost=1)
	Z3_t5 += alt(MAS)
	Z3_t5_mem0 = S.Task('Z3_t5_mem0', length=1, delay_cost=1)
	Z3_t5_mem0 += MM_MEM[2]
	S += 54 < Z3_t5_mem0
	S += Z3_t5_mem0 <= Z3_t5

	Z3_t5_mem1 = S.Task('Z3_t5_mem1', length=1, delay_cost=1)
	Z3_t5_mem1 += alt(MM_MEM)
	S += (Z3_t1*MM[0])-1 < Z3_t5_mem1*MM_MEM[1]
	S += (Z3_t1*MM[1])-1 < Z3_t5_mem1*MM_MEM[3]
	S += Z3_t5_mem1 <= Z3_t5

	T201 = S.Task('T201', length=1, delay_cost=1)
	T201 += alt(MAS)
	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	T201_mem0 += alt(MM_MEM)
	S += (T20_t4*MM[0])-1 < T201_mem0*MM_MEM[0]
	S += (T20_t4*MM[1])-1 < T201_mem0*MM_MEM[2]
	S += T201_mem0 <= T201

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	T201_mem1 += alt(MAS_MEM)
	S += (T20_t5*MAS[0])-1 < T201_mem1*MAS_MEM[1]
	S += (T20_t5*MAS[1])-1 < T201_mem1*MAS_MEM[3]
	S += (T20_t5*MAS[2])-1 < T201_mem1*MAS_MEM[5]
	S += (T20_t5*MAS[3])-1 < T201_mem1*MAS_MEM[7]
	S += (T20_t5*MAS[4])-1 < T201_mem1*MAS_MEM[9]
	S += (T20_t5*MAS[5])-1 < T201_mem1*MAS_MEM[11]
	S += (T20_t5*MAS[6])-1 < T201_mem1*MAS_MEM[13]
	S += (T20_t5*MAS[7])-1 < T201_mem1*MAS_MEM[15]
	S += T201_mem1 <= T201

	T220 = S.Task('T220', length=1, delay_cost=1)
	T220 += alt(MAS)
	T220_mem0 = S.Task('T220_mem0', length=1, delay_cost=1)
	T220_mem0 += alt(MM_MEM)
	S += (T22_t2*MM[0])-1 < T220_mem0*MM_MEM[0]
	S += (T22_t2*MM[1])-1 < T220_mem0*MM_MEM[2]
	S += T220_mem0 <= T220

	T220_mem1 = S.Task('T220_mem1', length=1, delay_cost=1)
	T220_mem1 += alt(MAS_MEM)
	S += (T22_t5*MAS[0])-1 < T220_mem1*MAS_MEM[1]
	S += (T22_t5*MAS[1])-1 < T220_mem1*MAS_MEM[3]
	S += (T22_t5*MAS[2])-1 < T220_mem1*MAS_MEM[5]
	S += (T22_t5*MAS[3])-1 < T220_mem1*MAS_MEM[7]
	S += (T22_t5*MAS[4])-1 < T220_mem1*MAS_MEM[9]
	S += (T22_t5*MAS[5])-1 < T220_mem1*MAS_MEM[11]
	S += (T22_t5*MAS[6])-1 < T220_mem1*MAS_MEM[13]
	S += (T22_t5*MAS[7])-1 < T220_mem1*MAS_MEM[15]
	S += T220_mem1 <= T220

	T230 = S.Task('T230', length=1, delay_cost=1)
	T230 += alt(MAS)
	T230_mem0 = S.Task('T230_mem0', length=1, delay_cost=1)
	T230_mem0 += alt(MM_MEM)
	S += (T23_t2*MM[0])-1 < T230_mem0*MM_MEM[0]
	S += (T23_t2*MM[1])-1 < T230_mem0*MM_MEM[2]
	S += T230_mem0 <= T230

	T230_mem1 = S.Task('T230_mem1', length=1, delay_cost=1)
	T230_mem1 += alt(MAS_MEM)
	S += (T23_t5*MAS[0])-1 < T230_mem1*MAS_MEM[1]
	S += (T23_t5*MAS[1])-1 < T230_mem1*MAS_MEM[3]
	S += (T23_t5*MAS[2])-1 < T230_mem1*MAS_MEM[5]
	S += (T23_t5*MAS[3])-1 < T230_mem1*MAS_MEM[7]
	S += (T23_t5*MAS[4])-1 < T230_mem1*MAS_MEM[9]
	S += (T23_t5*MAS[5])-1 < T230_mem1*MAS_MEM[11]
	S += (T23_t5*MAS[6])-1 < T230_mem1*MAS_MEM[13]
	S += (T23_t5*MAS[7])-1 < T230_mem1*MAS_MEM[15]
	S += T230_mem1 <= T230

	T250 = S.Task('T250', length=1, delay_cost=1)
	T250 += alt(MAS)
	T250_mem0 = S.Task('T250_mem0', length=1, delay_cost=1)
	T250_mem0 += alt(MAS_MEM)
	S += (T200*MAS[0])-1 < T250_mem0*MAS_MEM[0]
	S += (T200*MAS[1])-1 < T250_mem0*MAS_MEM[2]
	S += (T200*MAS[2])-1 < T250_mem0*MAS_MEM[4]
	S += (T200*MAS[3])-1 < T250_mem0*MAS_MEM[6]
	S += (T200*MAS[4])-1 < T250_mem0*MAS_MEM[8]
	S += (T200*MAS[5])-1 < T250_mem0*MAS_MEM[10]
	S += (T200*MAS[6])-1 < T250_mem0*MAS_MEM[12]
	S += (T200*MAS[7])-1 < T250_mem0*MAS_MEM[14]
	S += T250_mem0 <= T250

	T250_mem1 = S.Task('T250_mem1', length=1, delay_cost=1)
	T250_mem1 += alt(MAS_MEM)
	S += (T200*MAS[0])-1 < T250_mem1*MAS_MEM[1]
	S += (T200*MAS[1])-1 < T250_mem1*MAS_MEM[3]
	S += (T200*MAS[2])-1 < T250_mem1*MAS_MEM[5]
	S += (T200*MAS[3])-1 < T250_mem1*MAS_MEM[7]
	S += (T200*MAS[4])-1 < T250_mem1*MAS_MEM[9]
	S += (T200*MAS[5])-1 < T250_mem1*MAS_MEM[11]
	S += (T200*MAS[6])-1 < T250_mem1*MAS_MEM[13]
	S += (T200*MAS[7])-1 < T250_mem1*MAS_MEM[15]
	S += T250_mem1 <= T250

	Z31 = S.Task('Z31', length=1, delay_cost=1)
	Z31 += alt(MAS)
	S += 0<Z31

	Z31_w = S.Task('Z31_w', length=1, delay_cost=1)
	Z31_w += alt(MAIN_MEM_w)
	S += Z31 <= Z31_w

	Z31_mem0 = S.Task('Z31_mem0', length=1, delay_cost=1)
	Z31_mem0 += alt(MM_MEM)
	S += (Z3_t4*MM[0])-1 < Z31_mem0*MM_MEM[0]
	S += (Z3_t4*MM[1])-1 < Z31_mem0*MM_MEM[2]
	S += Z31_mem0 <= Z31

	Z31_mem1 = S.Task('Z31_mem1', length=1, delay_cost=1)
	Z31_mem1 += alt(MAS_MEM)
	S += (Z3_t5*MAS[0])-1 < Z31_mem1*MAS_MEM[1]
	S += (Z3_t5*MAS[1])-1 < Z31_mem1*MAS_MEM[3]
	S += (Z3_t5*MAS[2])-1 < Z31_mem1*MAS_MEM[5]
	S += (Z3_t5*MAS[3])-1 < Z31_mem1*MAS_MEM[7]
	S += (Z3_t5*MAS[4])-1 < Z31_mem1*MAS_MEM[9]
	S += (Z3_t5*MAS[5])-1 < Z31_mem1*MAS_MEM[11]
	S += (Z3_t5*MAS[6])-1 < Z31_mem1*MAS_MEM[13]
	S += (Z3_t5*MAS[7])-1 < Z31_mem1*MAS_MEM[15]
	S += Z31_mem1 <= Z31

	X31 = S.Task('X31', length=1, delay_cost=1)
	X31 += alt(MAS)
	S += 0<X31

	X31_w = S.Task('X31_w', length=1, delay_cost=1)
	X31_w += alt(MAIN_MEM_w)
	S += X31 <= X31_w

	X31_mem0 = S.Task('X31_mem0', length=1, delay_cost=1)
	X31_mem0 += alt(MAS_MEM)
	S += (T221*MAS[0])-1 < X31_mem0*MAS_MEM[0]
	S += (T221*MAS[1])-1 < X31_mem0*MAS_MEM[2]
	S += (T221*MAS[2])-1 < X31_mem0*MAS_MEM[4]
	S += (T221*MAS[3])-1 < X31_mem0*MAS_MEM[6]
	S += (T221*MAS[4])-1 < X31_mem0*MAS_MEM[8]
	S += (T221*MAS[5])-1 < X31_mem0*MAS_MEM[10]
	S += (T221*MAS[6])-1 < X31_mem0*MAS_MEM[12]
	S += (T221*MAS[7])-1 < X31_mem0*MAS_MEM[14]
	S += X31_mem0 <= X31

	X31_mem1 = S.Task('X31_mem1', length=1, delay_cost=1)
	X31_mem1 += alt(MAS_MEM)
	S += (T241*MAS[0])-1 < X31_mem1*MAS_MEM[1]
	S += (T241*MAS[1])-1 < X31_mem1*MAS_MEM[3]
	S += (T241*MAS[2])-1 < X31_mem1*MAS_MEM[5]
	S += (T241*MAS[3])-1 < X31_mem1*MAS_MEM[7]
	S += (T241*MAS[4])-1 < X31_mem1*MAS_MEM[9]
	S += (T241*MAS[5])-1 < X31_mem1*MAS_MEM[11]
	S += (T241*MAS[6])-1 < X31_mem1*MAS_MEM[13]
	S += (T241*MAS[7])-1 < X31_mem1*MAS_MEM[15]
	S += X31_mem1 <= X31

	X41 = S.Task('X41', length=1, delay_cost=1)
	X41 += alt(MAS)
	S += 0<X41

	X41_w = S.Task('X41_w', length=1, delay_cost=1)
	X41_w += alt(MAIN_MEM_w)
	S += X41 <= X41_w

	X41_mem0 = S.Task('X41_mem0', length=1, delay_cost=1)
	X41_mem0 += alt(MAS_MEM)
	S += (T231*MAS[0])-1 < X41_mem0*MAS_MEM[0]
	S += (T231*MAS[1])-1 < X41_mem0*MAS_MEM[2]
	S += (T231*MAS[2])-1 < X41_mem0*MAS_MEM[4]
	S += (T231*MAS[3])-1 < X41_mem0*MAS_MEM[6]
	S += (T231*MAS[4])-1 < X41_mem0*MAS_MEM[8]
	S += (T231*MAS[5])-1 < X41_mem0*MAS_MEM[10]
	S += (T231*MAS[6])-1 < X41_mem0*MAS_MEM[12]
	S += (T231*MAS[7])-1 < X41_mem0*MAS_MEM[14]
	S += X41_mem0 <= X41

	X41_mem1 = S.Task('X41_mem1', length=1, delay_cost=1)
	X41_mem1 += alt(MAS_MEM)
	S += (T171*MAS[0])-1 < X41_mem1*MAS_MEM[1]
	S += (T171*MAS[1])-1 < X41_mem1*MAS_MEM[3]
	S += (T171*MAS[2])-1 < X41_mem1*MAS_MEM[5]
	S += (T171*MAS[3])-1 < X41_mem1*MAS_MEM[7]
	S += (T171*MAS[4])-1 < X41_mem1*MAS_MEM[9]
	S += (T171*MAS[5])-1 < X41_mem1*MAS_MEM[11]
	S += (T171*MAS[6])-1 < X41_mem1*MAS_MEM[13]
	S += (T171*MAS[7])-1 < X41_mem1*MAS_MEM[15]
	S += X41_mem1 <= X41

	T251 = S.Task('T251', length=1, delay_cost=1)
	T251 += alt(MAS)
	T251_mem0 = S.Task('T251_mem0', length=1, delay_cost=1)
	T251_mem0 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem0*MAS_MEM[0]
	S += (T201*MAS[1])-1 < T251_mem0*MAS_MEM[2]
	S += (T201*MAS[2])-1 < T251_mem0*MAS_MEM[4]
	S += (T201*MAS[3])-1 < T251_mem0*MAS_MEM[6]
	S += (T201*MAS[4])-1 < T251_mem0*MAS_MEM[8]
	S += (T201*MAS[5])-1 < T251_mem0*MAS_MEM[10]
	S += (T201*MAS[6])-1 < T251_mem0*MAS_MEM[12]
	S += (T201*MAS[7])-1 < T251_mem0*MAS_MEM[14]
	S += T251_mem0 <= T251

	T251_mem1 = S.Task('T251_mem1', length=1, delay_cost=1)
	T251_mem1 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem1*MAS_MEM[1]
	S += (T201*MAS[1])-1 < T251_mem1*MAS_MEM[3]
	S += (T201*MAS[2])-1 < T251_mem1*MAS_MEM[5]
	S += (T201*MAS[3])-1 < T251_mem1*MAS_MEM[7]
	S += (T201*MAS[4])-1 < T251_mem1*MAS_MEM[9]
	S += (T201*MAS[5])-1 < T251_mem1*MAS_MEM[11]
	S += (T201*MAS[6])-1 < T251_mem1*MAS_MEM[13]
	S += (T201*MAS[7])-1 < T251_mem1*MAS_MEM[15]
	S += T251_mem1 <= T251

	X30 = S.Task('X30', length=1, delay_cost=1)
	X30 += alt(MAS)
	S += 0<X30

	X30_w = S.Task('X30_w', length=1, delay_cost=1)
	X30_w += alt(MAIN_MEM_w)
	S += X30 <= X30_w

	X30_mem0 = S.Task('X30_mem0', length=1, delay_cost=1)
	X30_mem0 += alt(MAS_MEM)
	S += (T220*MAS[0])-1 < X30_mem0*MAS_MEM[0]
	S += (T220*MAS[1])-1 < X30_mem0*MAS_MEM[2]
	S += (T220*MAS[2])-1 < X30_mem0*MAS_MEM[4]
	S += (T220*MAS[3])-1 < X30_mem0*MAS_MEM[6]
	S += (T220*MAS[4])-1 < X30_mem0*MAS_MEM[8]
	S += (T220*MAS[5])-1 < X30_mem0*MAS_MEM[10]
	S += (T220*MAS[6])-1 < X30_mem0*MAS_MEM[12]
	S += (T220*MAS[7])-1 < X30_mem0*MAS_MEM[14]
	S += X30_mem0 <= X30

	X30_mem1 = S.Task('X30_mem1', length=1, delay_cost=1)
	X30_mem1 += alt(MAS_MEM)
	S += (T240*MAS[0])-1 < X30_mem1*MAS_MEM[1]
	S += (T240*MAS[1])-1 < X30_mem1*MAS_MEM[3]
	S += (T240*MAS[2])-1 < X30_mem1*MAS_MEM[5]
	S += (T240*MAS[3])-1 < X30_mem1*MAS_MEM[7]
	S += (T240*MAS[4])-1 < X30_mem1*MAS_MEM[9]
	S += (T240*MAS[5])-1 < X30_mem1*MAS_MEM[11]
	S += (T240*MAS[6])-1 < X30_mem1*MAS_MEM[13]
	S += (T240*MAS[7])-1 < X30_mem1*MAS_MEM[15]
	S += X30_mem1 <= X30

	Z40 = S.Task('Z40', length=1, delay_cost=1)
	Z40 += alt(MAS)
	S += 0<Z40

	Z40_w = S.Task('Z40_w', length=1, delay_cost=1)
	Z40_w += alt(MAIN_MEM_w)
	S += Z40 <= Z40_w

	Z40_mem0 = S.Task('Z40_mem0', length=1, delay_cost=1)
	Z40_mem0 += alt(MAS_MEM)
	S += (T160*MAS[0])-1 < Z40_mem0*MAS_MEM[0]
	S += (T160*MAS[1])-1 < Z40_mem0*MAS_MEM[2]
	S += (T160*MAS[2])-1 < Z40_mem0*MAS_MEM[4]
	S += (T160*MAS[3])-1 < Z40_mem0*MAS_MEM[6]
	S += (T160*MAS[4])-1 < Z40_mem0*MAS_MEM[8]
	S += (T160*MAS[5])-1 < Z40_mem0*MAS_MEM[10]
	S += (T160*MAS[6])-1 < Z40_mem0*MAS_MEM[12]
	S += (T160*MAS[7])-1 < Z40_mem0*MAS_MEM[14]
	S += Z40_mem0 <= Z40

	Z40_mem1 = S.Task('Z40_mem1', length=1, delay_cost=1)
	Z40_mem1 += alt(MAS_MEM)
	S += (T250*MAS[0])-1 < Z40_mem1*MAS_MEM[1]
	S += (T250*MAS[1])-1 < Z40_mem1*MAS_MEM[3]
	S += (T250*MAS[2])-1 < Z40_mem1*MAS_MEM[5]
	S += (T250*MAS[3])-1 < Z40_mem1*MAS_MEM[7]
	S += (T250*MAS[4])-1 < Z40_mem1*MAS_MEM[9]
	S += (T250*MAS[5])-1 < Z40_mem1*MAS_MEM[11]
	S += (T250*MAS[6])-1 < Z40_mem1*MAS_MEM[13]
	S += (T250*MAS[7])-1 < Z40_mem1*MAS_MEM[15]
	S += Z40_mem1 <= Z40

	X40 = S.Task('X40', length=1, delay_cost=1)
	X40 += alt(MAS)
	S += 0<X40

	X40_w = S.Task('X40_w', length=1, delay_cost=1)
	X40_w += alt(MAIN_MEM_w)
	S += X40 <= X40_w

	X40_mem0 = S.Task('X40_mem0', length=1, delay_cost=1)
	X40_mem0 += alt(MAS_MEM)
	S += (T230*MAS[0])-1 < X40_mem0*MAS_MEM[0]
	S += (T230*MAS[1])-1 < X40_mem0*MAS_MEM[2]
	S += (T230*MAS[2])-1 < X40_mem0*MAS_MEM[4]
	S += (T230*MAS[3])-1 < X40_mem0*MAS_MEM[6]
	S += (T230*MAS[4])-1 < X40_mem0*MAS_MEM[8]
	S += (T230*MAS[5])-1 < X40_mem0*MAS_MEM[10]
	S += (T230*MAS[6])-1 < X40_mem0*MAS_MEM[12]
	S += (T230*MAS[7])-1 < X40_mem0*MAS_MEM[14]
	S += X40_mem0 <= X40

	X40_mem1 = S.Task('X40_mem1', length=1, delay_cost=1)
	X40_mem1 += alt(MAS_MEM)
	S += (T170*MAS[0])-1 < X40_mem1*MAS_MEM[1]
	S += (T170*MAS[1])-1 < X40_mem1*MAS_MEM[3]
	S += (T170*MAS[2])-1 < X40_mem1*MAS_MEM[5]
	S += (T170*MAS[3])-1 < X40_mem1*MAS_MEM[7]
	S += (T170*MAS[4])-1 < X40_mem1*MAS_MEM[9]
	S += (T170*MAS[5])-1 < X40_mem1*MAS_MEM[11]
	S += (T170*MAS[6])-1 < X40_mem1*MAS_MEM[13]
	S += (T170*MAS[7])-1 < X40_mem1*MAS_MEM[15]
	S += X40_mem1 <= X40

	Z41 = S.Task('Z41', length=1, delay_cost=1)
	Z41 += alt(MAS)
	S += 0<Z41

	Z41_w = S.Task('Z41_w', length=1, delay_cost=1)
	Z41_w += alt(MAIN_MEM_w)
	S += Z41 <= Z41_w

	Z41_mem0 = S.Task('Z41_mem0', length=1, delay_cost=1)
	Z41_mem0 += alt(MAS_MEM)
	S += (T161*MAS[0])-1 < Z41_mem0*MAS_MEM[0]
	S += (T161*MAS[1])-1 < Z41_mem0*MAS_MEM[2]
	S += (T161*MAS[2])-1 < Z41_mem0*MAS_MEM[4]
	S += (T161*MAS[3])-1 < Z41_mem0*MAS_MEM[6]
	S += (T161*MAS[4])-1 < Z41_mem0*MAS_MEM[8]
	S += (T161*MAS[5])-1 < Z41_mem0*MAS_MEM[10]
	S += (T161*MAS[6])-1 < Z41_mem0*MAS_MEM[12]
	S += (T161*MAS[7])-1 < Z41_mem0*MAS_MEM[14]
	S += Z41_mem0 <= Z41

	Z41_mem1 = S.Task('Z41_mem1', length=1, delay_cost=1)
	Z41_mem1 += alt(MAS_MEM)
	S += (T251*MAS[0])-1 < Z41_mem1*MAS_MEM[1]
	S += (T251*MAS[1])-1 < Z41_mem1*MAS_MEM[3]
	S += (T251*MAS[2])-1 < Z41_mem1*MAS_MEM[5]
	S += (T251*MAS[3])-1 < Z41_mem1*MAS_MEM[7]
	S += (T251*MAS[4])-1 < Z41_mem1*MAS_MEM[9]
	S += (T251*MAS[5])-1 < Z41_mem1*MAS_MEM[11]
	S += (T251*MAS[6])-1 < Z41_mem1*MAS_MEM[13]
	S += (T251*MAS[7])-1 < Z41_mem1*MAS_MEM[15]
	S += Z41_mem1 <= Z41

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM2_stage1MAS8/EP2_LADDERMUL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

