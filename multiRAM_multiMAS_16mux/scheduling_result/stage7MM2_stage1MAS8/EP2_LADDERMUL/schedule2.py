from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 161
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=7)
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

	T7_t0 = S.Task('T7_t0', length=7, delay_cost=1)
	S += T7_t0 >= 1
	T7_t0 += MM[1]

	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	S += T7_t1_in >= 1
	T7_t1_in += MM_in[0]

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	S += T7_t1_mem0 >= 1
	T7_t1_mem0 += MAIN_MEM_r[0]

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	S += T7_t1_mem1 >= 1
	T7_t1_mem1 += MAIN_MEM_r[1]

	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	S += T6_t0_in >= 2
	T6_t0_in += MM_in[1]

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	S += T6_t0_mem0 >= 2
	T6_t0_mem0 += MAIN_MEM_r[0]

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	S += T6_t0_mem1 >= 2
	T6_t0_mem1 += MAIN_MEM_r[1]

	T7_t1 = S.Task('T7_t1', length=7, delay_cost=1)
	S += T7_t1 >= 2
	T7_t1 += MM[0]

	T6_t0 = S.Task('T6_t0', length=7, delay_cost=1)
	S += T6_t0 >= 3
	T6_t0 += MM[1]

	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	S += T6_t1_in >= 3
	T6_t1_in += MM_in[0]

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	S += T6_t1_mem0 >= 3
	T6_t1_mem0 += MAIN_MEM_r[0]

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	S += T6_t1_mem1 >= 3
	T6_t1_mem1 += MAIN_MEM_r[1]

	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	S += T4_t0_in >= 4
	T4_t0_in += MM_in[0]

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	S += T4_t0_mem0 >= 4
	T4_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	S += T4_t0_mem1 >= 4
	T4_t0_mem1 += MAIN_MEM_r[1]

	T6_t1 = S.Task('T6_t1', length=7, delay_cost=1)
	S += T6_t1 >= 4
	T6_t1 += MM[0]

	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	S += T1_t3_in >= 5
	T1_t3_in += MM_in[0]

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	S += T1_t3_mem0 >= 5
	T1_t3_mem0 += MAIN_MEM_r[0]

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	S += T1_t3_mem1 >= 5
	T1_t3_mem1 += MAIN_MEM_r[1]

	T4_t0 = S.Task('T4_t0', length=7, delay_cost=1)
	S += T4_t0 >= 5
	T4_t0 += MM[0]

	T1_t3 = S.Task('T1_t3', length=7, delay_cost=1)
	S += T1_t3 >= 6
	T1_t3 += MM[0]

	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	S += T5_t3_in >= 6
	T5_t3_in += MM_in[0]

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	S += T5_t3_mem0 >= 6
	T5_t3_mem0 += MAIN_MEM_r[0]

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	S += T5_t3_mem1 >= 6
	T5_t3_mem1 += MAIN_MEM_r[1]

	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	S += T3_t1_in >= 7
	T3_t1_in += MM_in[0]

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	S += T3_t1_mem0 >= 7
	T3_t1_mem0 += MAIN_MEM_r[0]

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	S += T3_t1_mem1 >= 7
	T3_t1_mem1 += MAIN_MEM_r[1]

	T5_t3 = S.Task('T5_t3', length=7, delay_cost=1)
	S += T5_t3 >= 7
	T5_t3 += MM[0]

	T3_t1 = S.Task('T3_t1', length=7, delay_cost=1)
	S += T3_t1 >= 8
	T3_t1 += MM[0]

	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	S += T4_t1_in >= 8
	T4_t1_in += MM_in[0]

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	S += T4_t1_mem0 >= 8
	T4_t1_mem0 += MAIN_MEM_r[0]

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	S += T4_t1_mem1 >= 8
	T4_t1_mem1 += MAIN_MEM_r[1]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 8
	T70_mem0 += MM_MEM[2]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 8
	T70_mem1 += MM_MEM[1]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 9
	T150_mem0 += MAS_MEM[0]

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 9
	T150_mem1 += MAS_MEM[1]

	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	S += T2_t1_in >= 9
	T2_t1_in += MM_in[0]

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	S += T2_t1_mem0 >= 9
	T2_t1_mem0 += MAIN_MEM_r[0]

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	S += T2_t1_mem1 >= 9
	T2_t1_mem1 += MAIN_MEM_r[1]

	T4_t1 = S.Task('T4_t1', length=7, delay_cost=1)
	S += T4_t1 >= 9
	T4_t1 += MM[0]

	T70 = S.Task('T70', length=1, delay_cost=1)
	S += T70 >= 9
	T70 += MAS[0]

	T7_t5_mem0 = S.Task('T7_t5_mem0', length=1, delay_cost=1)
	S += T7_t5_mem0 >= 9
	T7_t5_mem0 += MM_MEM[2]

	T7_t5_mem1 = S.Task('T7_t5_mem1', length=1, delay_cost=1)
	S += T7_t5_mem1 >= 9
	T7_t5_mem1 += MM_MEM[1]

	T150 = S.Task('T150', length=1, delay_cost=1)
	S += T150 >= 10
	T150 += MAS[4]

	T2_t1 = S.Task('T2_t1', length=7, delay_cost=1)
	S += T2_t1 >= 10
	T2_t1 += MM[0]

	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	S += T3_t0_in >= 10
	T3_t0_in += MM_in[0]

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	S += T3_t0_mem0 >= 10
	T3_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	S += T3_t0_mem1 >= 10
	T3_t0_mem1 += MAIN_MEM_r[1]

	T6_t5_mem0 = S.Task('T6_t5_mem0', length=1, delay_cost=1)
	S += T6_t5_mem0 >= 10
	T6_t5_mem0 += MM_MEM[2]

	T6_t5_mem1 = S.Task('T6_t5_mem1', length=1, delay_cost=1)
	S += T6_t5_mem1 >= 10
	T6_t5_mem1 += MM_MEM[1]

	T7_t5 = S.Task('T7_t5', length=1, delay_cost=1)
	S += T7_t5 >= 10
	T7_t5 += MAS[0]

	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	S += T2_t0_in >= 11
	T2_t0_in += MM_in[1]

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	S += T2_t0_mem0 >= 11
	T2_t0_mem0 += MAIN_MEM_r[0]

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	S += T2_t0_mem1 >= 11
	T2_t0_mem1 += MAIN_MEM_r[1]

	T3_t0 = S.Task('T3_t0', length=7, delay_cost=1)
	S += T3_t0 >= 11
	T3_t0 += MM[0]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 11
	T60_mem0 += MM_MEM[2]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 11
	T60_mem1 += MM_MEM[1]

	T6_t5 = S.Task('T6_t5', length=1, delay_cost=1)
	S += T6_t5 >= 11
	T6_t5 += MAS[5]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	S += T10_t2_mem0 >= 12
	T10_t2_mem0 += MAIN_MEM_r[0]

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	S += T10_t2_mem1 >= 12
	T10_t2_mem1 += MAIN_MEM_r[1]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 12
	T11_mem0 += MM_MEM[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 12
	T11_mem1 += MM_MEM[1]

	T2_t0 = S.Task('T2_t0', length=7, delay_cost=1)
	S += T2_t0 >= 12
	T2_t0 += MM[1]

	T60 = S.Task('T60', length=1, delay_cost=1)
	S += T60 >= 12
	T60 += MAS[5]

	T10_t2 = S.Task('T10_t2', length=1, delay_cost=1)
	S += T10_t2 >= 13
	T10_t2 += MAS[0]

	T11 = S.Task('T11', length=1, delay_cost=1)
	S += T11 >= 13
	T11 += MAS[1]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 13
	T51_mem0 += MM_MEM[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 13
	T51_mem1 += MM_MEM[1]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	S += T7_t2_mem0 >= 13
	T7_t2_mem0 += MAIN_MEM_r[0]

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	S += T7_t2_mem1 >= 13
	T7_t2_mem1 += MAIN_MEM_r[1]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	S += T11_t2_mem0 >= 14
	T11_t2_mem0 += MAIN_MEM_r[0]

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	S += T11_t2_mem1 >= 14
	T11_t2_mem1 += MAIN_MEM_r[1]

	T51 = S.Task('T51', length=1, delay_cost=1)
	S += T51 >= 14
	T51 += MAS[5]

	T5_t5_mem0 = S.Task('T5_t5_mem0', length=1, delay_cost=1)
	S += T5_t5_mem0 >= 14
	T5_t5_mem0 += MM_MEM[0]

	T5_t5_mem1 = S.Task('T5_t5_mem1', length=1, delay_cost=1)
	S += T5_t5_mem1 >= 14
	T5_t5_mem1 += MM_MEM[1]

	T7_t2 = S.Task('T7_t2', length=1, delay_cost=1)
	S += T7_t2 >= 14
	T7_t2 += MAS[2]

	T11_t2 = S.Task('T11_t2', length=1, delay_cost=1)
	S += T11_t2 >= 15
	T11_t2 += MAS[0]

	T1_t5_mem0 = S.Task('T1_t5_mem0', length=1, delay_cost=1)
	S += T1_t5_mem0 >= 15
	T1_t5_mem0 += MM_MEM[0]

	T1_t5_mem1 = S.Task('T1_t5_mem1', length=1, delay_cost=1)
	S += T1_t5_mem1 >= 15
	T1_t5_mem1 += MM_MEM[1]

	T5_t5 = S.Task('T5_t5', length=1, delay_cost=1)
	S += T5_t5 >= 15
	T5_t5 += MAS[6]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	S += T6_t3_mem0 >= 15
	T6_t3_mem0 += MAIN_MEM_r[0]

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	S += T6_t3_mem1 >= 15
	T6_t3_mem1 += MAIN_MEM_r[1]

	T1_t5 = S.Task('T1_t5', length=1, delay_cost=1)
	S += T1_t5 >= 16
	T1_t5 += MAS[6]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 16
	T40_mem0 += MM_MEM[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 16
	T40_mem1 += MM_MEM[1]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	S += T6_t2_mem0 >= 16
	T6_t2_mem0 += MAIN_MEM_r[0]

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	S += T6_t2_mem1 >= 16
	T6_t2_mem1 += MAIN_MEM_r[1]

	T6_t3 = S.Task('T6_t3', length=1, delay_cost=1)
	S += T6_t3 >= 16
	T6_t3 += MAS[1]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 17
	T30_mem0 += MM_MEM[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 17
	T30_mem1 += MM_MEM[1]

	T40 = S.Task('T40', length=1, delay_cost=1)
	S += T40 >= 17
	T40 += MAS[5]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	S += T5_t1_mem0 >= 17
	T5_t1_mem0 += MAIN_MEM_r[0]

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	S += T5_t1_mem1 >= 17
	T5_t1_mem1 += MAIN_MEM_r[1]

	T6_t2 = S.Task('T6_t2', length=1, delay_cost=1)
	S += T6_t2 >= 17
	T6_t2 += MAS[0]

	T6_t4_in = S.Task('T6_t4_in', length=1, delay_cost=1)
	S += T6_t4_in >= 17
	T6_t4_in += MM_in[0]

	T6_t4_mem0 = S.Task('T6_t4_mem0', length=1, delay_cost=1)
	S += T6_t4_mem0 >= 17
	T6_t4_mem0 += MAS_MEM[0]

	T6_t4_mem1 = S.Task('T6_t4_mem1', length=1, delay_cost=1)
	S += T6_t4_mem1 >= 17
	T6_t4_mem1 += MAS_MEM[3]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 18
	T20_mem0 += MM_MEM[2]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 18
	T20_mem1 += MM_MEM[1]

	T30 = S.Task('T30', length=1, delay_cost=1)
	S += T30 >= 18
	T30 += MAS[1]

	T5_t1 = S.Task('T5_t1', length=1, delay_cost=1)
	S += T5_t1 >= 18
	T5_t1 += MAS[3]

	T6_t4 = S.Task('T6_t4', length=7, delay_cost=1)
	S += T6_t4 >= 18
	T6_t4 += MM[0]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	S += T9_t2_mem0 >= 18
	T9_t2_mem0 += MAIN_MEM_r[0]

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	S += T9_t2_mem1 >= 18
	T9_t2_mem1 += MAIN_MEM_r[1]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 19
	T130_mem0 += MAS_MEM[10]

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 19
	T130_mem1 += MAS_MEM[11]

	T20 = S.Task('T20', length=1, delay_cost=1)
	S += T20 >= 19
	T20 += MAS[5]

	T2_t5_mem0 = S.Task('T2_t5_mem0', length=1, delay_cost=1)
	S += T2_t5_mem0 >= 19
	T2_t5_mem0 += MM_MEM[2]

	T2_t5_mem1 = S.Task('T2_t5_mem1', length=1, delay_cost=1)
	S += T2_t5_mem1 >= 19
	T2_t5_mem1 += MM_MEM[1]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	S += T4_t3_mem0 >= 19
	T4_t3_mem0 += MAIN_MEM_r[0]

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	S += T4_t3_mem1 >= 19
	T4_t3_mem1 += MAIN_MEM_r[1]

	T9_t2 = S.Task('T9_t2', length=1, delay_cost=1)
	S += T9_t2 >= 19
	T9_t2 += MAS[0]

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	S += T120_mem0 >= 20
	T120_mem0 += MAS_MEM[10]

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	S += T120_mem1 >= 20
	T120_mem1 += MAS_MEM[11]

	T130 = S.Task('T130', length=1, delay_cost=1)
	S += T130 >= 20
	T130 += MAS[0]

	T14_t0_in = S.Task('T14_t0_in', length=1, delay_cost=1)
	S += T14_t0_in >= 20
	T14_t0_in += MM_in[0]

	T14_t0_mem0 = S.Task('T14_t0_mem0', length=1, delay_cost=1)
	S += T14_t0_mem0 >= 20
	T14_t0_mem0 += MAS_MEM[0]

	T14_t0_mem1 = S.Task('T14_t0_mem1', length=1, delay_cost=1)
	S += T14_t0_mem1 >= 20
	T14_t0_mem1 += MAS_MEM[1]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	S += T1_t0_mem0 >= 20
	T1_t0_mem0 += MAIN_MEM_r[0]

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	S += T1_t0_mem1 >= 20
	T1_t0_mem1 += MAIN_MEM_r[1]

	T2_t5 = S.Task('T2_t5', length=1, delay_cost=1)
	S += T2_t5 >= 20
	T2_t5 += MAS[6]

	T4_t3 = S.Task('T4_t3', length=1, delay_cost=1)
	S += T4_t3 >= 20
	T4_t3 += MAS[3]

	T4_t5_mem0 = S.Task('T4_t5_mem0', length=1, delay_cost=1)
	S += T4_t5_mem0 >= 20
	T4_t5_mem0 += MM_MEM[0]

	T4_t5_mem1 = S.Task('T4_t5_mem1', length=1, delay_cost=1)
	S += T4_t5_mem1 >= 20
	T4_t5_mem1 += MM_MEM[1]

	T120 = S.Task('T120', length=1, delay_cost=1)
	S += T120 >= 21
	T120 += MAS[7]

	T14_t0 = S.Task('T14_t0', length=7, delay_cost=1)
	S += T14_t0 >= 21
	T14_t0 += MM[0]

	T1_t0 = S.Task('T1_t0', length=1, delay_cost=1)
	S += T1_t0 >= 21
	T1_t0 += MAS[0]

	T3_t5_mem0 = S.Task('T3_t5_mem0', length=1, delay_cost=1)
	S += T3_t5_mem0 >= 21
	T3_t5_mem0 += MM_MEM[0]

	T3_t5_mem1 = S.Task('T3_t5_mem1', length=1, delay_cost=1)
	S += T3_t5_mem1 >= 21
	T3_t5_mem1 += MM_MEM[1]

	T4_t5 = S.Task('T4_t5', length=1, delay_cost=1)
	S += T4_t5 >= 21
	T4_t5 += MAS[3]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	S += T5_t0_mem0 >= 21
	T5_t0_mem0 += MAIN_MEM_r[0]

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	S += T5_t0_mem1 >= 21
	T5_t0_mem1 += MAIN_MEM_r[1]

	T3_t5 = S.Task('T3_t5', length=1, delay_cost=1)
	S += T3_t5 >= 22
	T3_t5 += MAS[1]

	T5_t0 = S.Task('T5_t0', length=1, delay_cost=1)
	S += T5_t0 >= 22
	T5_t0 += MAS[0]

	T5_t2_in = S.Task('T5_t2_in', length=1, delay_cost=1)
	S += T5_t2_in >= 22
	T5_t2_in += MM_in[1]

	T5_t2_mem0 = S.Task('T5_t2_mem0', length=1, delay_cost=1)
	S += T5_t2_mem0 >= 22
	T5_t2_mem0 += MAS_MEM[0]

	T5_t2_mem1 = S.Task('T5_t2_mem1', length=1, delay_cost=1)
	S += T5_t2_mem1 >= 22
	T5_t2_mem1 += MAS_MEM[7]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	S += T7_t3_mem0 >= 22
	T7_t3_mem0 += MAIN_MEM_r[0]

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	S += T7_t3_mem1 >= 22
	T7_t3_mem1 += MAIN_MEM_r[1]

	T5_t2 = S.Task('T5_t2', length=7, delay_cost=1)
	S += T5_t2 >= 23
	T5_t2 += MM[1]

	T7_t3 = S.Task('T7_t3', length=1, delay_cost=1)
	S += T7_t3 >= 23
	T7_t3 += MAS[0]

	T7_t4_in = S.Task('T7_t4_in', length=1, delay_cost=1)
	S += T7_t4_in >= 23
	T7_t4_in += MM_in[1]

	T7_t4_mem0 = S.Task('T7_t4_mem0', length=1, delay_cost=1)
	S += T7_t4_mem0 >= 23
	T7_t4_mem0 += MAS_MEM[4]

	T7_t4_mem1 = S.Task('T7_t4_mem1', length=1, delay_cost=1)
	S += T7_t4_mem1 >= 23
	T7_t4_mem1 += MAS_MEM[1]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	S += T8_t2_mem0 >= 23
	T8_t2_mem0 += MAIN_MEM_r[0]

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	S += T8_t2_mem1 >= 23
	T8_t2_mem1 += MAIN_MEM_r[1]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	S += T4_t2_mem0 >= 24
	T4_t2_mem0 += MAIN_MEM_r[0]

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	S += T4_t2_mem1 >= 24
	T4_t2_mem1 += MAIN_MEM_r[1]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 24
	T61_mem0 += MM_MEM[0]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 24
	T61_mem1 += MAS_MEM[11]

	T7_t4 = S.Task('T7_t4', length=7, delay_cost=1)
	S += T7_t4 >= 24
	T7_t4 += MM[1]

	T8_t2 = S.Task('T8_t2', length=1, delay_cost=1)
	S += T8_t2 >= 24
	T8_t2 += MAS[0]

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
	T4_t4_in += MM_in[0]

	T4_t4_mem0 = S.Task('T4_t4_mem0', length=1, delay_cost=1)
	S += T4_t4_mem0 >= 25
	T4_t4_mem0 += MAS_MEM[6]

	T4_t4_mem1 = S.Task('T4_t4_mem1', length=1, delay_cost=1)
	S += T4_t4_mem1 >= 25
	T4_t4_mem1 += MAS_MEM[7]

	T61 = S.Task('T61', length=1, delay_cost=1)
	S += T61 >= 25
	T61 += MAS[6]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	S += T3_t2_mem0 >= 26
	T3_t2_mem0 += MAIN_MEM_r[0]

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	S += T3_t2_mem1 >= 26
	T3_t2_mem1 += MAIN_MEM_r[1]

	T3_t3 = S.Task('T3_t3', length=1, delay_cost=1)
	S += T3_t3 >= 26
	T3_t3 += MAS[0]

	T4_t4 = S.Task('T4_t4', length=7, delay_cost=1)
	S += T4_t4 >= 26
	T4_t4 += MM[0]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	S += T1_t1_mem0 >= 27
	T1_t1_mem0 += MAIN_MEM_r[0]

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	S += T1_t1_mem1 >= 27
	T1_t1_mem1 += MAIN_MEM_r[1]

	T3_t2 = S.Task('T3_t2', length=1, delay_cost=1)
	S += T3_t2 >= 27
	T3_t2 += MAS[0]

	T3_t4_in = S.Task('T3_t4_in', length=1, delay_cost=1)
	S += T3_t4_in >= 27
	T3_t4_in += MM_in[0]

	T3_t4_mem0 = S.Task('T3_t4_mem0', length=1, delay_cost=1)
	S += T3_t4_mem0 >= 27
	T3_t4_mem0 += MAS_MEM[0]

	T3_t4_mem1 = S.Task('T3_t4_mem1', length=1, delay_cost=1)
	S += T3_t4_mem1 >= 27
	T3_t4_mem1 += MAS_MEM[1]

	T1_t1 = S.Task('T1_t1', length=1, delay_cost=1)
	S += T1_t1 >= 28
	T1_t1 += MAS[0]

	T1_t2_in = S.Task('T1_t2_in', length=1, delay_cost=1)
	S += T1_t2_in >= 28
	T1_t2_in += MM_in[1]

	T1_t2_mem0 = S.Task('T1_t2_mem0', length=1, delay_cost=1)
	S += T1_t2_mem0 >= 28
	T1_t2_mem0 += MAS_MEM[0]

	T1_t2_mem1 = S.Task('T1_t2_mem1', length=1, delay_cost=1)
	S += T1_t2_mem1 >= 28
	T1_t2_mem1 += MAS_MEM[1]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	S += T2_t3_mem0 >= 28
	T2_t3_mem0 += MAIN_MEM_r[0]

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	S += T2_t3_mem1 >= 28
	T2_t3_mem1 += MAIN_MEM_r[1]

	T3_t4 = S.Task('T3_t4', length=7, delay_cost=1)
	S += T3_t4 >= 28
	T3_t4 += MM[0]

	T1_t2 = S.Task('T1_t2', length=7, delay_cost=1)
	S += T1_t2 >= 29
	T1_t2 += MM[1]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	S += T2_t2_mem0 >= 29
	T2_t2_mem0 += MAIN_MEM_r[0]

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	S += T2_t2_mem1 >= 29
	T2_t2_mem1 += MAIN_MEM_r[1]

	T2_t3 = S.Task('T2_t3', length=1, delay_cost=1)
	S += T2_t3 >= 29
	T2_t3 += MAS[3]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 29
	T50_mem0 += MM_MEM[2]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 29
	T50_mem1 += MAS_MEM[13]

	T20_t2_mem0 = S.Task('T20_t2_mem0', length=1, delay_cost=1)
	S += T20_t2_mem0 >= 30
	T20_t2_mem0 += MAS_MEM[8]

	T20_t2_mem1 = S.Task('T20_t2_mem1', length=1, delay_cost=1)
	S += T20_t2_mem1 >= 30
	T20_t2_mem1 += MAS_MEM[11]

	T2_t2 = S.Task('T2_t2', length=1, delay_cost=1)
	S += T2_t2 >= 30
	T2_t2 += MAS[6]

	T2_t4_in = S.Task('T2_t4_in', length=1, delay_cost=1)
	S += T2_t4_in >= 30
	T2_t4_in += MM_in[1]

	T2_t4_mem0 = S.Task('T2_t4_mem0', length=1, delay_cost=1)
	S += T2_t4_mem0 >= 30
	T2_t4_mem0 += MAS_MEM[12]

	T2_t4_mem1 = S.Task('T2_t4_mem1', length=1, delay_cost=1)
	S += T2_t4_mem1 >= 30
	T2_t4_mem1 += MAS_MEM[7]

	T50 = S.Task('T50', length=1, delay_cost=1)
	S += T50 >= 30
	T50 += MAS[4]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 30
	T71_mem0 += MM_MEM[2]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 30
	T71_mem1 += MAS_MEM[1]

	T9_t1_in = S.Task('T9_t1_in', length=1, delay_cost=1)
	S += T9_t1_in >= 30
	T9_t1_in += MM_in[0]

	T9_t1_mem0 = S.Task('T9_t1_mem0', length=1, delay_cost=1)
	S += T9_t1_mem0 >= 30
	T9_t1_mem0 += MAIN_MEM_r[0]

	T9_t1_mem1 = S.Task('T9_t1_mem1', length=1, delay_cost=1)
	S += T9_t1_mem1 >= 30
	T9_t1_mem1 += MAS_MEM[3]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 31
	T151_mem0 += MAS_MEM[8]

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 31
	T151_mem1 += MAS_MEM[9]

	T20_t2 = S.Task('T20_t2', length=1, delay_cost=1)
	S += T20_t2 >= 31
	T20_t2 += MAS[3]

	T2_t4 = S.Task('T2_t4', length=7, delay_cost=1)
	S += T2_t4 >= 31
	T2_t4 += MM[1]

	T71 = S.Task('T71', length=1, delay_cost=1)
	S += T71 >= 31
	T71 += MAS[4]

	T8_t1_in = S.Task('T8_t1_in', length=1, delay_cost=1)
	S += T8_t1_in >= 31
	T8_t1_in += MM_in[1]

	T8_t1_mem0 = S.Task('T8_t1_mem0', length=1, delay_cost=1)
	S += T8_t1_mem0 >= 31
	T8_t1_mem0 += MAIN_MEM_r[0]

	T8_t1_mem1 = S.Task('T8_t1_mem1', length=1, delay_cost=1)
	S += T8_t1_mem1 >= 31
	T8_t1_mem1 += MAS_MEM[3]

	T9_t1 = S.Task('T9_t1', length=7, delay_cost=1)
	S += T9_t1 >= 31
	T9_t1 += MM[0]

	T11_t0_in = S.Task('T11_t0_in', length=1, delay_cost=1)
	S += T11_t0_in >= 32
	T11_t0_in += MM_in[0]

	T11_t0_mem0 = S.Task('T11_t0_mem0', length=1, delay_cost=1)
	S += T11_t0_mem0 >= 32
	T11_t0_mem0 += MAIN_MEM_r[0]

	T11_t0_mem1 = S.Task('T11_t0_mem1', length=1, delay_cost=1)
	S += T11_t0_mem1 >= 32
	T11_t0_mem1 += MAS_MEM[3]

	T151 = S.Task('T151', length=1, delay_cost=1)
	S += T151 >= 32
	T151 += MAS[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 32
	T41_mem0 += MM_MEM[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 32
	T41_mem1 += MAS_MEM[7]

	T8_t1 = S.Task('T8_t1', length=7, delay_cost=1)
	S += T8_t1 >= 32
	T8_t1 += MM[1]

	T10_t0_in = S.Task('T10_t0_in', length=1, delay_cost=1)
	S += T10_t0_in >= 33
	T10_t0_in += MM_in[1]

	T10_t0_mem0 = S.Task('T10_t0_mem0', length=1, delay_cost=1)
	S += T10_t0_mem0 >= 33
	T10_t0_mem0 += MAIN_MEM_r[0]

	T10_t0_mem1 = S.Task('T10_t0_mem1', length=1, delay_cost=1)
	S += T10_t0_mem1 >= 33
	T10_t0_mem1 += MAS_MEM[3]

	T11_t0 = S.Task('T11_t0', length=7, delay_cost=1)
	S += T11_t0 >= 33
	T11_t0 += MM[0]

	T41 = S.Task('T41', length=1, delay_cost=1)
	S += T41 >= 33
	T41 += MAS[4]

	T10_t0 = S.Task('T10_t0', length=7, delay_cost=1)
	S += T10_t0 >= 34
	T10_t0 += MM[1]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 34
	T31_mem0 += MM_MEM[0]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 34
	T31_mem1 += MAS_MEM[3]

	Z3_t2_mem0 = S.Task('Z3_t2_mem0', length=1, delay_cost=1)
	S += Z3_t2_mem0 >= 34
	Z3_t2_mem0 += MAIN_MEM_r[0]

	Z3_t2_mem1 = S.Task('Z3_t2_mem1', length=1, delay_cost=1)
	S += Z3_t2_mem1 >= 34
	Z3_t2_mem1 += MAIN_MEM_r[1]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 35
	T10_mem0 += MM_MEM[2]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 35
	T10_mem1 += MAS_MEM[13]

	T10_t1_in = S.Task('T10_t1_in', length=1, delay_cost=1)
	S += T10_t1_in >= 35
	T10_t1_in += MM_in[0]

	T10_t1_mem0 = S.Task('T10_t1_mem0', length=1, delay_cost=1)
	S += T10_t1_mem0 >= 35
	T10_t1_mem0 += MAIN_MEM_r[0]

	T10_t1_mem1 = S.Task('T10_t1_mem1', length=1, delay_cost=1)
	S += T10_t1_mem1 >= 35
	T10_t1_mem1 += MAS_MEM[1]

	T31 = S.Task('T31', length=1, delay_cost=1)
	S += T31 >= 35
	T31 += MAS[0]

	Z3_t2 = S.Task('Z3_t2', length=1, delay_cost=1)
	S += Z3_t2 >= 35
	Z3_t2 += MAS[1]

	T10 = S.Task('T10', length=1, delay_cost=1)
	S += T10 >= 36
	T10 += MAS[5]

	T10_t1 = S.Task('T10_t1', length=7, delay_cost=1)
	S += T10_t1 >= 36
	T10_t1 += MM[0]

	T11_t3_mem0 = S.Task('T11_t3_mem0', length=1, delay_cost=1)
	S += T11_t3_mem0 >= 36
	T11_t3_mem0 += MAS_MEM[2]

	T11_t3_mem1 = S.Task('T11_t3_mem1', length=1, delay_cost=1)
	S += T11_t3_mem1 >= 36
	T11_t3_mem1 += MAS_MEM[1]

	T9_t0_in = S.Task('T9_t0_in', length=1, delay_cost=1)
	S += T9_t0_in >= 36
	T9_t0_in += MM_in[0]

	T9_t0_mem0 = S.Task('T9_t0_mem0', length=1, delay_cost=1)
	S += T9_t0_mem0 >= 36
	T9_t0_mem0 += MAIN_MEM_r[0]

	T9_t0_mem1 = S.Task('T9_t0_mem1', length=1, delay_cost=1)
	S += T9_t0_mem1 >= 36
	T9_t0_mem1 += MAS_MEM[11]

	T9_t3_mem0 = S.Task('T9_t3_mem0', length=1, delay_cost=1)
	S += T9_t3_mem0 >= 36
	T9_t3_mem0 += MAS_MEM[10]

	T9_t3_mem1 = S.Task('T9_t3_mem1', length=1, delay_cost=1)
	S += T9_t3_mem1 >= 36
	T9_t3_mem1 += MAS_MEM[3]

	T10_t3_mem0 = S.Task('T10_t3_mem0', length=1, delay_cost=1)
	S += T10_t3_mem0 >= 37
	T10_t3_mem0 += MAS_MEM[2]

	T10_t3_mem1 = S.Task('T10_t3_mem1', length=1, delay_cost=1)
	S += T10_t3_mem1 >= 37
	T10_t3_mem1 += MAS_MEM[1]

	T11_t3 = S.Task('T11_t3', length=1, delay_cost=1)
	S += T11_t3 >= 37
	T11_t3 += MAS[6]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 37
	T21_mem0 += MM_MEM[2]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 37
	T21_mem1 += MAS_MEM[13]

	T8_t0_in = S.Task('T8_t0_in', length=1, delay_cost=1)
	S += T8_t0_in >= 37
	T8_t0_in += MM_in[0]

	T8_t0_mem0 = S.Task('T8_t0_mem0', length=1, delay_cost=1)
	S += T8_t0_mem0 >= 37
	T8_t0_mem0 += MAIN_MEM_r[0]

	T8_t0_mem1 = S.Task('T8_t0_mem1', length=1, delay_cost=1)
	S += T8_t0_mem1 >= 37
	T8_t0_mem1 += MAS_MEM[11]

	T8_t3_mem0 = S.Task('T8_t3_mem0', length=1, delay_cost=1)
	S += T8_t3_mem0 >= 37
	T8_t3_mem0 += MAS_MEM[10]

	T8_t3_mem1 = S.Task('T8_t3_mem1', length=1, delay_cost=1)
	S += T8_t3_mem1 >= 37
	T8_t3_mem1 += MAS_MEM[3]

	T9_t0 = S.Task('T9_t0', length=7, delay_cost=1)
	S += T9_t0 >= 37
	T9_t0 += MM[0]

	T9_t3 = S.Task('T9_t3', length=1, delay_cost=1)
	S += T9_t3 >= 37
	T9_t3 += MAS[5]

	T10_t3 = S.Task('T10_t3', length=1, delay_cost=1)
	S += T10_t3 >= 38
	T10_t3 += MAS[0]

	T11_t1_in = S.Task('T11_t1_in', length=1, delay_cost=1)
	S += T11_t1_in >= 38
	T11_t1_in += MM_in[0]

	T11_t1_mem0 = S.Task('T11_t1_mem0', length=1, delay_cost=1)
	S += T11_t1_mem0 >= 38
	T11_t1_mem0 += MAIN_MEM_r[0]

	T11_t1_mem1 = S.Task('T11_t1_mem1', length=1, delay_cost=1)
	S += T11_t1_mem1 >= 38
	T11_t1_mem1 += MAS_MEM[1]

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 38
	T131_mem0 += MAS_MEM[8]

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 38
	T131_mem1 += MAS_MEM[13]

	T16_t2_mem0 = S.Task('T16_t2_mem0', length=1, delay_cost=1)
	S += T16_t2_mem0 >= 38
	T16_t2_mem0 += MAS_MEM[10]

	T16_t2_mem1 = S.Task('T16_t2_mem1', length=1, delay_cost=1)
	S += T16_t2_mem1 >= 38
	T16_t2_mem1 += MAS_MEM[3]

	T21 = S.Task('T21', length=1, delay_cost=1)
	S += T21 >= 38
	T21 += MAS[6]

	T8_t0 = S.Task('T8_t0', length=7, delay_cost=1)
	S += T8_t0 >= 38
	T8_t0 += MM[0]

	T8_t3 = S.Task('T8_t3', length=1, delay_cost=1)
	S += T8_t3 >= 38
	T8_t3 += MAS[2]

	T11_t1 = S.Task('T11_t1', length=7, delay_cost=1)
	S += T11_t1 >= 39
	T11_t1 += MM[0]

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	S += T121_mem0 >= 39
	T121_mem0 += MAS_MEM[8]

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	S += T121_mem1 >= 39
	T121_mem1 += MAS_MEM[13]

	T131 = S.Task('T131', length=1, delay_cost=1)
	S += T131 >= 39
	T131 += MAS[7]

	T16_t2 = S.Task('T16_t2', length=1, delay_cost=1)
	S += T16_t2 >= 39
	T16_t2 += MAS[6]

	T121 = S.Task('T121', length=1, delay_cost=1)
	S += T121 >= 40
	T121 += MAS[0]


	# new tasks
	T8_t4 = S.Task('T8_t4', length=7, delay_cost=1)
	T8_t4 += alt(MM)
	T8_t4_in = S.Task('T8_t4_in', length=1, delay_cost=1)
	T8_t4_in += alt(MM_in)
	S += T8_t4_in*MM_in[0]<=T8_t4*MM[0]
	S += T8_t4_in*MM_in[1]<=T8_t4*MM[1]
	T8_t4_mem0 = S.Task('T8_t4_mem0', length=1, delay_cost=1)
	T8_t4_mem0 += MAS_MEM[0]
	S += 24 < T8_t4_mem0
	S += T8_t4_mem0 <= T8_t4

	T8_t4_mem1 = S.Task('T8_t4_mem1', length=1, delay_cost=1)
	T8_t4_mem1 += MAS_MEM[5]
	S += 38 < T8_t4_mem1
	S += T8_t4_mem1 <= T8_t4

	T80 = S.Task('T80', length=1, delay_cost=1)
	T80 += alt(MAS)
	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	T80_mem0 += MM_MEM[0]
	S += 44 < T80_mem0
	S += T80_mem0 <= T80

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	T80_mem1 += MM_MEM[3]
	S += 38 < T80_mem1
	S += T80_mem1 <= T80

	T8_t5 = S.Task('T8_t5', length=1, delay_cost=1)
	T8_t5 += alt(MAS)
	T8_t5_mem0 = S.Task('T8_t5_mem0', length=1, delay_cost=1)
	T8_t5_mem0 += MM_MEM[0]
	S += 44 < T8_t5_mem0
	S += T8_t5_mem0 <= T8_t5

	T8_t5_mem1 = S.Task('T8_t5_mem1', length=1, delay_cost=1)
	T8_t5_mem1 += MM_MEM[3]
	S += 38 < T8_t5_mem1
	S += T8_t5_mem1 <= T8_t5

	T9_t4 = S.Task('T9_t4', length=7, delay_cost=1)
	T9_t4 += alt(MM)
	T9_t4_in = S.Task('T9_t4_in', length=1, delay_cost=1)
	T9_t4_in += alt(MM_in)
	S += T9_t4_in*MM_in[0]<=T9_t4*MM[0]
	S += T9_t4_in*MM_in[1]<=T9_t4*MM[1]
	T9_t4_mem0 = S.Task('T9_t4_mem0', length=1, delay_cost=1)
	T9_t4_mem0 += MAS_MEM[0]
	S += 19 < T9_t4_mem0
	S += T9_t4_mem0 <= T9_t4

	T9_t4_mem1 = S.Task('T9_t4_mem1', length=1, delay_cost=1)
	T9_t4_mem1 += MAS_MEM[11]
	S += 37 < T9_t4_mem1
	S += T9_t4_mem1 <= T9_t4

	T90 = S.Task('T90', length=1, delay_cost=1)
	T90 += alt(MAS)
	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	T90_mem0 += MM_MEM[0]
	S += 43 < T90_mem0
	S += T90_mem0 <= T90

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	T90_mem1 += MM_MEM[1]
	S += 37 < T90_mem1
	S += T90_mem1 <= T90

	T9_t5 = S.Task('T9_t5', length=1, delay_cost=1)
	T9_t5 += alt(MAS)
	T9_t5_mem0 = S.Task('T9_t5_mem0', length=1, delay_cost=1)
	T9_t5_mem0 += MM_MEM[0]
	S += 43 < T9_t5_mem0
	S += T9_t5_mem0 <= T9_t5

	T9_t5_mem1 = S.Task('T9_t5_mem1', length=1, delay_cost=1)
	T9_t5_mem1 += MM_MEM[1]
	S += 37 < T9_t5_mem1
	S += T9_t5_mem1 <= T9_t5

	T10_t4 = S.Task('T10_t4', length=7, delay_cost=1)
	T10_t4 += alt(MM)
	T10_t4_in = S.Task('T10_t4_in', length=1, delay_cost=1)
	T10_t4_in += alt(MM_in)
	S += T10_t4_in*MM_in[0]<=T10_t4*MM[0]
	S += T10_t4_in*MM_in[1]<=T10_t4*MM[1]
	T10_t4_mem0 = S.Task('T10_t4_mem0', length=1, delay_cost=1)
	T10_t4_mem0 += MAS_MEM[0]
	S += 13 < T10_t4_mem0
	S += T10_t4_mem0 <= T10_t4

	T10_t4_mem1 = S.Task('T10_t4_mem1', length=1, delay_cost=1)
	T10_t4_mem1 += MAS_MEM[1]
	S += 38 < T10_t4_mem1
	S += T10_t4_mem1 <= T10_t4

	T100 = S.Task('T100', length=1, delay_cost=1)
	T100 += alt(MAS)
	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	T100_mem0 += MM_MEM[2]
	S += 40 < T100_mem0
	S += T100_mem0 <= T100

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	T100_mem1 += MM_MEM[1]
	S += 42 < T100_mem1
	S += T100_mem1 <= T100

	T10_t5 = S.Task('T10_t5', length=1, delay_cost=1)
	T10_t5 += alt(MAS)
	T10_t5_mem0 = S.Task('T10_t5_mem0', length=1, delay_cost=1)
	T10_t5_mem0 += MM_MEM[2]
	S += 40 < T10_t5_mem0
	S += T10_t5_mem0 <= T10_t5

	T10_t5_mem1 = S.Task('T10_t5_mem1', length=1, delay_cost=1)
	T10_t5_mem1 += MM_MEM[1]
	S += 42 < T10_t5_mem1
	S += T10_t5_mem1 <= T10_t5

	T11_t4 = S.Task('T11_t4', length=7, delay_cost=1)
	T11_t4 += alt(MM)
	T11_t4_in = S.Task('T11_t4_in', length=1, delay_cost=1)
	T11_t4_in += alt(MM_in)
	S += T11_t4_in*MM_in[0]<=T11_t4*MM[0]
	S += T11_t4_in*MM_in[1]<=T11_t4*MM[1]
	T11_t4_mem0 = S.Task('T11_t4_mem0', length=1, delay_cost=1)
	T11_t4_mem0 += MAS_MEM[0]
	S += 15 < T11_t4_mem0
	S += T11_t4_mem0 <= T11_t4

	T11_t4_mem1 = S.Task('T11_t4_mem1', length=1, delay_cost=1)
	T11_t4_mem1 += MAS_MEM[13]
	S += 37 < T11_t4_mem1
	S += T11_t4_mem1 <= T11_t4

	T110 = S.Task('T110', length=1, delay_cost=1)
	T110 += alt(MAS)
	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	T110_mem0 += MM_MEM[0]
	S += 39 < T110_mem0
	S += T110_mem0 <= T110

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	T110_mem1 += MM_MEM[1]
	S += 45 < T110_mem1
	S += T110_mem1 <= T110

	T11_t5 = S.Task('T11_t5', length=1, delay_cost=1)
	T11_t5 += alt(MAS)
	T11_t5_mem0 = S.Task('T11_t5_mem0', length=1, delay_cost=1)
	T11_t5_mem0 += MM_MEM[0]
	S += 39 < T11_t5_mem0
	S += T11_t5_mem0 <= T11_t5

	T11_t5_mem1 = S.Task('T11_t5_mem1', length=1, delay_cost=1)
	T11_t5_mem1 += MM_MEM[1]
	S += 45 < T11_t5_mem1
	S += T11_t5_mem1 <= T11_t5

	T14_t1 = S.Task('T14_t1', length=7, delay_cost=1)
	T14_t1 += alt(MM)
	T14_t1_in = S.Task('T14_t1_in', length=1, delay_cost=1)
	T14_t1_in += alt(MM_in)
	S += T14_t1_in*MM_in[0]<=T14_t1*MM[0]
	S += T14_t1_in*MM_in[1]<=T14_t1*MM[1]
	T14_t1_mem0 = S.Task('T14_t1_mem0', length=1, delay_cost=1)
	T14_t1_mem0 += MAS_MEM[14]
	S += 39 < T14_t1_mem0
	S += T14_t1_mem0 <= T14_t1

	T14_t1_mem1 = S.Task('T14_t1_mem1', length=1, delay_cost=1)
	T14_t1_mem1 += MAS_MEM[15]
	S += 39 < T14_t1_mem1
	S += T14_t1_mem1 <= T14_t1

	T14_t2 = S.Task('T14_t2', length=1, delay_cost=1)
	T14_t2 += alt(MAS)
	T14_t2_mem0 = S.Task('T14_t2_mem0', length=1, delay_cost=1)
	T14_t2_mem0 += MAS_MEM[0]
	S += 20 < T14_t2_mem0
	S += T14_t2_mem0 <= T14_t2

	T14_t2_mem1 = S.Task('T14_t2_mem1', length=1, delay_cost=1)
	T14_t2_mem1 += MAS_MEM[15]
	S += 39 < T14_t2_mem1
	S += T14_t2_mem1 <= T14_t2

	T14_t3 = S.Task('T14_t3', length=1, delay_cost=1)
	T14_t3 += alt(MAS)
	T14_t3_mem0 = S.Task('T14_t3_mem0', length=1, delay_cost=1)
	T14_t3_mem0 += MAS_MEM[0]
	S += 20 < T14_t3_mem0
	S += T14_t3_mem0 <= T14_t3

	T14_t3_mem1 = S.Task('T14_t3_mem1', length=1, delay_cost=1)
	T14_t3_mem1 += MAS_MEM[15]
	S += 39 < T14_t3_mem1
	S += T14_t3_mem1 <= T14_t3

	T17_t3 = S.Task('T17_t3', length=1, delay_cost=1)
	T17_t3 += alt(MAS)
	T17_t3_mem0 = S.Task('T17_t3_mem0', length=1, delay_cost=1)
	T17_t3_mem0 += MAS_MEM[8]
	S += 10 < T17_t3_mem0
	S += T17_t3_mem0 <= T17_t3

	T17_t3_mem1 = S.Task('T17_t3_mem1', length=1, delay_cost=1)
	T17_t3_mem1 += MAS_MEM[1]
	S += 32 < T17_t3_mem1
	S += T17_t3_mem1 <= T17_t3

	T24_t3 = S.Task('T24_t3', length=1, delay_cost=1)
	T24_t3 += alt(MAS)
	T24_t3_mem0 = S.Task('T24_t3_mem0', length=1, delay_cost=1)
	T24_t3_mem0 += MAS_MEM[14]
	S += 21 < T24_t3_mem0
	S += T24_t3_mem0 <= T24_t3

	T24_t3_mem1 = S.Task('T24_t3_mem1', length=1, delay_cost=1)
	T24_t3_mem1 += MAS_MEM[1]
	S += 40 < T24_t3_mem1
	S += T24_t3_mem1 <= T24_t3

	T81 = S.Task('T81', length=1, delay_cost=1)
	T81 += alt(MAS)
	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	T81_mem0 += alt(MM_MEM)
	S += (T8_t4*MM[0])-1 < T81_mem0*MM_MEM[0]
	S += (T8_t4*MM[1])-1 < T81_mem0*MM_MEM[2]
	S += T81_mem0 <= T81

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	T81_mem1 += alt(MAS_MEM)
	S += (T8_t5*MAS[0])-1 < T81_mem1*MAS_MEM[1]
	S += (T8_t5*MAS[1])-1 < T81_mem1*MAS_MEM[3]
	S += (T8_t5*MAS[2])-1 < T81_mem1*MAS_MEM[5]
	S += (T8_t5*MAS[3])-1 < T81_mem1*MAS_MEM[7]
	S += (T8_t5*MAS[4])-1 < T81_mem1*MAS_MEM[9]
	S += (T8_t5*MAS[5])-1 < T81_mem1*MAS_MEM[11]
	S += (T8_t5*MAS[6])-1 < T81_mem1*MAS_MEM[13]
	S += (T8_t5*MAS[7])-1 < T81_mem1*MAS_MEM[15]
	S += T81_mem1 <= T81

	T91 = S.Task('T91', length=1, delay_cost=1)
	T91 += alt(MAS)
	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	T91_mem0 += alt(MM_MEM)
	S += (T9_t4*MM[0])-1 < T91_mem0*MM_MEM[0]
	S += (T9_t4*MM[1])-1 < T91_mem0*MM_MEM[2]
	S += T91_mem0 <= T91

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	T91_mem1 += alt(MAS_MEM)
	S += (T9_t5*MAS[0])-1 < T91_mem1*MAS_MEM[1]
	S += (T9_t5*MAS[1])-1 < T91_mem1*MAS_MEM[3]
	S += (T9_t5*MAS[2])-1 < T91_mem1*MAS_MEM[5]
	S += (T9_t5*MAS[3])-1 < T91_mem1*MAS_MEM[7]
	S += (T9_t5*MAS[4])-1 < T91_mem1*MAS_MEM[9]
	S += (T9_t5*MAS[5])-1 < T91_mem1*MAS_MEM[11]
	S += (T9_t5*MAS[6])-1 < T91_mem1*MAS_MEM[13]
	S += (T9_t5*MAS[7])-1 < T91_mem1*MAS_MEM[15]
	S += T91_mem1 <= T91

	T101 = S.Task('T101', length=1, delay_cost=1)
	T101 += alt(MAS)
	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	T101_mem0 += alt(MM_MEM)
	S += (T10_t4*MM[0])-1 < T101_mem0*MM_MEM[0]
	S += (T10_t4*MM[1])-1 < T101_mem0*MM_MEM[2]
	S += T101_mem0 <= T101

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	T101_mem1 += alt(MAS_MEM)
	S += (T10_t5*MAS[0])-1 < T101_mem1*MAS_MEM[1]
	S += (T10_t5*MAS[1])-1 < T101_mem1*MAS_MEM[3]
	S += (T10_t5*MAS[2])-1 < T101_mem1*MAS_MEM[5]
	S += (T10_t5*MAS[3])-1 < T101_mem1*MAS_MEM[7]
	S += (T10_t5*MAS[4])-1 < T101_mem1*MAS_MEM[9]
	S += (T10_t5*MAS[5])-1 < T101_mem1*MAS_MEM[11]
	S += (T10_t5*MAS[6])-1 < T101_mem1*MAS_MEM[13]
	S += (T10_t5*MAS[7])-1 < T101_mem1*MAS_MEM[15]
	S += T101_mem1 <= T101

	T111 = S.Task('T111', length=1, delay_cost=1)
	T111 += alt(MAS)
	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	T111_mem0 += alt(MM_MEM)
	S += (T11_t4*MM[0])-1 < T111_mem0*MM_MEM[0]
	S += (T11_t4*MM[1])-1 < T111_mem0*MM_MEM[2]
	S += T111_mem0 <= T111

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	T111_mem1 += alt(MAS_MEM)
	S += (T11_t5*MAS[0])-1 < T111_mem1*MAS_MEM[1]
	S += (T11_t5*MAS[1])-1 < T111_mem1*MAS_MEM[3]
	S += (T11_t5*MAS[2])-1 < T111_mem1*MAS_MEM[5]
	S += (T11_t5*MAS[3])-1 < T111_mem1*MAS_MEM[7]
	S += (T11_t5*MAS[4])-1 < T111_mem1*MAS_MEM[9]
	S += (T11_t5*MAS[5])-1 < T111_mem1*MAS_MEM[11]
	S += (T11_t5*MAS[6])-1 < T111_mem1*MAS_MEM[13]
	S += (T11_t5*MAS[7])-1 < T111_mem1*MAS_MEM[15]
	S += T111_mem1 <= T111

	T14_t4 = S.Task('T14_t4', length=7, delay_cost=1)
	T14_t4 += alt(MM)
	T14_t4_in = S.Task('T14_t4_in', length=1, delay_cost=1)
	T14_t4_in += alt(MM_in)
	S += T14_t4_in*MM_in[0]<=T14_t4*MM[0]
	S += T14_t4_in*MM_in[1]<=T14_t4*MM[1]
	T14_t4_mem0 = S.Task('T14_t4_mem0', length=1, delay_cost=1)
	T14_t4_mem0 += alt(MAS_MEM)
	S += (T14_t2*MAS[0])-1 < T14_t4_mem0*MAS_MEM[0]
	S += (T14_t2*MAS[1])-1 < T14_t4_mem0*MAS_MEM[2]
	S += (T14_t2*MAS[2])-1 < T14_t4_mem0*MAS_MEM[4]
	S += (T14_t2*MAS[3])-1 < T14_t4_mem0*MAS_MEM[6]
	S += (T14_t2*MAS[4])-1 < T14_t4_mem0*MAS_MEM[8]
	S += (T14_t2*MAS[5])-1 < T14_t4_mem0*MAS_MEM[10]
	S += (T14_t2*MAS[6])-1 < T14_t4_mem0*MAS_MEM[12]
	S += (T14_t2*MAS[7])-1 < T14_t4_mem0*MAS_MEM[14]
	S += T14_t4_mem0 <= T14_t4

	T14_t4_mem1 = S.Task('T14_t4_mem1', length=1, delay_cost=1)
	T14_t4_mem1 += alt(MAS_MEM)
	S += (T14_t3*MAS[0])-1 < T14_t4_mem1*MAS_MEM[1]
	S += (T14_t3*MAS[1])-1 < T14_t4_mem1*MAS_MEM[3]
	S += (T14_t3*MAS[2])-1 < T14_t4_mem1*MAS_MEM[5]
	S += (T14_t3*MAS[3])-1 < T14_t4_mem1*MAS_MEM[7]
	S += (T14_t3*MAS[4])-1 < T14_t4_mem1*MAS_MEM[9]
	S += (T14_t3*MAS[5])-1 < T14_t4_mem1*MAS_MEM[11]
	S += (T14_t3*MAS[6])-1 < T14_t4_mem1*MAS_MEM[13]
	S += (T14_t3*MAS[7])-1 < T14_t4_mem1*MAS_MEM[15]
	S += T14_t4_mem1 <= T14_t4

	T140 = S.Task('T140', length=1, delay_cost=1)
	T140 += alt(MAS)
	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	T140_mem0 += MM_MEM[0]
	S += 27 < T140_mem0
	S += T140_mem0 <= T140

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	T140_mem1 += alt(MM_MEM)
	S += (T14_t1*MM[0])-1 < T140_mem1*MM_MEM[1]
	S += (T14_t1*MM[1])-1 < T140_mem1*MM_MEM[3]
	S += T140_mem1 <= T140

	T14_t5 = S.Task('T14_t5', length=1, delay_cost=1)
	T14_t5 += alt(MAS)
	T14_t5_mem0 = S.Task('T14_t5_mem0', length=1, delay_cost=1)
	T14_t5_mem0 += MM_MEM[0]
	S += 27 < T14_t5_mem0
	S += T14_t5_mem0 <= T14_t5

	T14_t5_mem1 = S.Task('T14_t5_mem1', length=1, delay_cost=1)
	T14_t5_mem1 += alt(MM_MEM)
	S += (T14_t1*MM[0])-1 < T14_t5_mem1*MM_MEM[1]
	S += (T14_t1*MM[1])-1 < T14_t5_mem1*MM_MEM[3]
	S += T14_t5_mem1 <= T14_t5

	T16_t0 = S.Task('T16_t0', length=7, delay_cost=1)
	T16_t0 += alt(MM)
	T16_t0_in = S.Task('T16_t0_in', length=1, delay_cost=1)
	T16_t0_in += alt(MM_in)
	S += T16_t0_in*MM_in[0]<=T16_t0*MM[0]
	S += T16_t0_in*MM_in[1]<=T16_t0*MM[1]
	T16_t0_mem0 = S.Task('T16_t0_mem0', length=1, delay_cost=1)
	T16_t0_mem0 += MAS_MEM[10]
	S += 36 < T16_t0_mem0
	S += T16_t0_mem0 <= T16_t0

	T16_t0_mem1 = S.Task('T16_t0_mem1', length=1, delay_cost=1)
	T16_t0_mem1 += alt(MAS_MEM)
	S += (T80*MAS[0])-1 < T16_t0_mem1*MAS_MEM[1]
	S += (T80*MAS[1])-1 < T16_t0_mem1*MAS_MEM[3]
	S += (T80*MAS[2])-1 < T16_t0_mem1*MAS_MEM[5]
	S += (T80*MAS[3])-1 < T16_t0_mem1*MAS_MEM[7]
	S += (T80*MAS[4])-1 < T16_t0_mem1*MAS_MEM[9]
	S += (T80*MAS[5])-1 < T16_t0_mem1*MAS_MEM[11]
	S += (T80*MAS[6])-1 < T16_t0_mem1*MAS_MEM[13]
	S += (T80*MAS[7])-1 < T16_t0_mem1*MAS_MEM[15]
	S += T16_t0_mem1 <= T16_t0

	T17_t0 = S.Task('T17_t0', length=7, delay_cost=1)
	T17_t0 += alt(MM)
	T17_t0_in = S.Task('T17_t0_in', length=1, delay_cost=1)
	T17_t0_in += alt(MM_in)
	S += T17_t0_in*MM_in[0]<=T17_t0*MM[0]
	S += T17_t0_in*MM_in[1]<=T17_t0*MM[1]
	T17_t0_mem0 = S.Task('T17_t0_mem0', length=1, delay_cost=1)
	T17_t0_mem0 += alt(MAS_MEM)
	S += (T80*MAS[0])-1 < T17_t0_mem0*MAS_MEM[0]
	S += (T80*MAS[1])-1 < T17_t0_mem0*MAS_MEM[2]
	S += (T80*MAS[2])-1 < T17_t0_mem0*MAS_MEM[4]
	S += (T80*MAS[3])-1 < T17_t0_mem0*MAS_MEM[6]
	S += (T80*MAS[4])-1 < T17_t0_mem0*MAS_MEM[8]
	S += (T80*MAS[5])-1 < T17_t0_mem0*MAS_MEM[10]
	S += (T80*MAS[6])-1 < T17_t0_mem0*MAS_MEM[12]
	S += (T80*MAS[7])-1 < T17_t0_mem0*MAS_MEM[14]
	S += T17_t0_mem0 <= T17_t0

	T17_t0_mem1 = S.Task('T17_t0_mem1', length=1, delay_cost=1)
	T17_t0_mem1 += MAS_MEM[9]
	S += 10 < T17_t0_mem1
	S += T17_t0_mem1 <= T17_t0

	T180 = S.Task('T180', length=1, delay_cost=1)
	T180 += alt(MAS)
	T180_mem0 = S.Task('T180_mem0', length=1, delay_cost=1)
	T180_mem0 += MAS_MEM[8]
	S += 30 < T180_mem0
	S += T180_mem0 <= T180

	T180_mem1 = S.Task('T180_mem1', length=1, delay_cost=1)
	T180_mem1 += alt(MAS_MEM)
	S += (T90*MAS[0])-1 < T180_mem1*MAS_MEM[1]
	S += (T90*MAS[1])-1 < T180_mem1*MAS_MEM[3]
	S += (T90*MAS[2])-1 < T180_mem1*MAS_MEM[5]
	S += (T90*MAS[3])-1 < T180_mem1*MAS_MEM[7]
	S += (T90*MAS[4])-1 < T180_mem1*MAS_MEM[9]
	S += (T90*MAS[5])-1 < T180_mem1*MAS_MEM[11]
	S += (T90*MAS[6])-1 < T180_mem1*MAS_MEM[13]
	S += (T90*MAS[7])-1 < T180_mem1*MAS_MEM[15]
	S += T180_mem1 <= T180

	T190 = S.Task('T190', length=1, delay_cost=1)
	T190 += alt(MAS)
	T190_mem0 = S.Task('T190_mem0', length=1, delay_cost=1)
	T190_mem0 += MAS_MEM[8]
	S += 30 < T190_mem0
	S += T190_mem0 <= T190

	T190_mem1 = S.Task('T190_mem1', length=1, delay_cost=1)
	T190_mem1 += alt(MAS_MEM)
	S += (T90*MAS[0])-1 < T190_mem1*MAS_MEM[1]
	S += (T90*MAS[1])-1 < T190_mem1*MAS_MEM[3]
	S += (T90*MAS[2])-1 < T190_mem1*MAS_MEM[5]
	S += (T90*MAS[3])-1 < T190_mem1*MAS_MEM[7]
	S += (T90*MAS[4])-1 < T190_mem1*MAS_MEM[9]
	S += (T90*MAS[5])-1 < T190_mem1*MAS_MEM[11]
	S += (T90*MAS[6])-1 < T190_mem1*MAS_MEM[13]
	S += (T90*MAS[7])-1 < T190_mem1*MAS_MEM[15]
	S += T190_mem1 <= T190

	T210 = S.Task('T210', length=1, delay_cost=1)
	T210 += alt(MAS)
	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	T210_mem0 += MAS_MEM[10]
	S += 12 < T210_mem0
	S += T210_mem0 <= T210

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	T210_mem1 += alt(MAS_MEM)
	S += (T100*MAS[0])-1 < T210_mem1*MAS_MEM[1]
	S += (T100*MAS[1])-1 < T210_mem1*MAS_MEM[3]
	S += (T100*MAS[2])-1 < T210_mem1*MAS_MEM[5]
	S += (T100*MAS[3])-1 < T210_mem1*MAS_MEM[7]
	S += (T100*MAS[4])-1 < T210_mem1*MAS_MEM[9]
	S += (T100*MAS[5])-1 < T210_mem1*MAS_MEM[11]
	S += (T100*MAS[6])-1 < T210_mem1*MAS_MEM[13]
	S += (T100*MAS[7])-1 < T210_mem1*MAS_MEM[15]
	S += T210_mem1 <= T210

	T24_t0 = S.Task('T24_t0', length=7, delay_cost=1)
	T24_t0 += alt(MM)
	T24_t0_in = S.Task('T24_t0_in', length=1, delay_cost=1)
	T24_t0_in += alt(MM_in)
	S += T24_t0_in*MM_in[0]<=T24_t0*MM[0]
	S += T24_t0_in*MM_in[1]<=T24_t0*MM[1]
	T24_t0_mem0 = S.Task('T24_t0_mem0', length=1, delay_cost=1)
	T24_t0_mem0 += alt(MAS_MEM)
	S += (T110*MAS[0])-1 < T24_t0_mem0*MAS_MEM[0]
	S += (T110*MAS[1])-1 < T24_t0_mem0*MAS_MEM[2]
	S += (T110*MAS[2])-1 < T24_t0_mem0*MAS_MEM[4]
	S += (T110*MAS[3])-1 < T24_t0_mem0*MAS_MEM[6]
	S += (T110*MAS[4])-1 < T24_t0_mem0*MAS_MEM[8]
	S += (T110*MAS[5])-1 < T24_t0_mem0*MAS_MEM[10]
	S += (T110*MAS[6])-1 < T24_t0_mem0*MAS_MEM[12]
	S += (T110*MAS[7])-1 < T24_t0_mem0*MAS_MEM[14]
	S += T24_t0_mem0 <= T24_t0

	T24_t0_mem1 = S.Task('T24_t0_mem1', length=1, delay_cost=1)
	T24_t0_mem1 += MAS_MEM[15]
	S += 21 < T24_t0_mem1
	S += T24_t0_mem1 <= T24_t0

	T141 = S.Task('T141', length=1, delay_cost=1)
	T141 += alt(MAS)
	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	T141_mem0 += alt(MM_MEM)
	S += (T14_t4*MM[0])-1 < T141_mem0*MM_MEM[0]
	S += (T14_t4*MM[1])-1 < T141_mem0*MM_MEM[2]
	S += T141_mem0 <= T141

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	T141_mem1 += alt(MAS_MEM)
	S += (T14_t5*MAS[0])-1 < T141_mem1*MAS_MEM[1]
	S += (T14_t5*MAS[1])-1 < T141_mem1*MAS_MEM[3]
	S += (T14_t5*MAS[2])-1 < T141_mem1*MAS_MEM[5]
	S += (T14_t5*MAS[3])-1 < T141_mem1*MAS_MEM[7]
	S += (T14_t5*MAS[4])-1 < T141_mem1*MAS_MEM[9]
	S += (T14_t5*MAS[5])-1 < T141_mem1*MAS_MEM[11]
	S += (T14_t5*MAS[6])-1 < T141_mem1*MAS_MEM[13]
	S += (T14_t5*MAS[7])-1 < T141_mem1*MAS_MEM[15]
	S += T141_mem1 <= T141

	T16_t1 = S.Task('T16_t1', length=7, delay_cost=1)
	T16_t1 += alt(MM)
	T16_t1_in = S.Task('T16_t1_in', length=1, delay_cost=1)
	T16_t1_in += alt(MM_in)
	S += T16_t1_in*MM_in[0]<=T16_t1*MM[0]
	S += T16_t1_in*MM_in[1]<=T16_t1*MM[1]
	T16_t1_mem0 = S.Task('T16_t1_mem0', length=1, delay_cost=1)
	T16_t1_mem0 += MAS_MEM[2]
	S += 13 < T16_t1_mem0
	S += T16_t1_mem0 <= T16_t1

	T16_t1_mem1 = S.Task('T16_t1_mem1', length=1, delay_cost=1)
	T16_t1_mem1 += alt(MAS_MEM)
	S += (T81*MAS[0])-1 < T16_t1_mem1*MAS_MEM[1]
	S += (T81*MAS[1])-1 < T16_t1_mem1*MAS_MEM[3]
	S += (T81*MAS[2])-1 < T16_t1_mem1*MAS_MEM[5]
	S += (T81*MAS[3])-1 < T16_t1_mem1*MAS_MEM[7]
	S += (T81*MAS[4])-1 < T16_t1_mem1*MAS_MEM[9]
	S += (T81*MAS[5])-1 < T16_t1_mem1*MAS_MEM[11]
	S += (T81*MAS[6])-1 < T16_t1_mem1*MAS_MEM[13]
	S += (T81*MAS[7])-1 < T16_t1_mem1*MAS_MEM[15]
	S += T16_t1_mem1 <= T16_t1

	T16_t3 = S.Task('T16_t3', length=1, delay_cost=1)
	T16_t3 += alt(MAS)
	T16_t3_mem0 = S.Task('T16_t3_mem0', length=1, delay_cost=1)
	T16_t3_mem0 += alt(MAS_MEM)
	S += (T80*MAS[0])-1 < T16_t3_mem0*MAS_MEM[0]
	S += (T80*MAS[1])-1 < T16_t3_mem0*MAS_MEM[2]
	S += (T80*MAS[2])-1 < T16_t3_mem0*MAS_MEM[4]
	S += (T80*MAS[3])-1 < T16_t3_mem0*MAS_MEM[6]
	S += (T80*MAS[4])-1 < T16_t3_mem0*MAS_MEM[8]
	S += (T80*MAS[5])-1 < T16_t3_mem0*MAS_MEM[10]
	S += (T80*MAS[6])-1 < T16_t3_mem0*MAS_MEM[12]
	S += (T80*MAS[7])-1 < T16_t3_mem0*MAS_MEM[14]
	S += T16_t3_mem0 <= T16_t3

	T16_t3_mem1 = S.Task('T16_t3_mem1', length=1, delay_cost=1)
	T16_t3_mem1 += alt(MAS_MEM)
	S += (T81*MAS[0])-1 < T16_t3_mem1*MAS_MEM[1]
	S += (T81*MAS[1])-1 < T16_t3_mem1*MAS_MEM[3]
	S += (T81*MAS[2])-1 < T16_t3_mem1*MAS_MEM[5]
	S += (T81*MAS[3])-1 < T16_t3_mem1*MAS_MEM[7]
	S += (T81*MAS[4])-1 < T16_t3_mem1*MAS_MEM[9]
	S += (T81*MAS[5])-1 < T16_t3_mem1*MAS_MEM[11]
	S += (T81*MAS[6])-1 < T16_t3_mem1*MAS_MEM[13]
	S += (T81*MAS[7])-1 < T16_t3_mem1*MAS_MEM[15]
	S += T16_t3_mem1 <= T16_t3

	T17_t1 = S.Task('T17_t1', length=7, delay_cost=1)
	T17_t1 += alt(MM)
	T17_t1_in = S.Task('T17_t1_in', length=1, delay_cost=1)
	T17_t1_in += alt(MM_in)
	S += T17_t1_in*MM_in[0]<=T17_t1*MM[0]
	S += T17_t1_in*MM_in[1]<=T17_t1*MM[1]
	T17_t1_mem0 = S.Task('T17_t1_mem0', length=1, delay_cost=1)
	T17_t1_mem0 += alt(MAS_MEM)
	S += (T81*MAS[0])-1 < T17_t1_mem0*MAS_MEM[0]
	S += (T81*MAS[1])-1 < T17_t1_mem0*MAS_MEM[2]
	S += (T81*MAS[2])-1 < T17_t1_mem0*MAS_MEM[4]
	S += (T81*MAS[3])-1 < T17_t1_mem0*MAS_MEM[6]
	S += (T81*MAS[4])-1 < T17_t1_mem0*MAS_MEM[8]
	S += (T81*MAS[5])-1 < T17_t1_mem0*MAS_MEM[10]
	S += (T81*MAS[6])-1 < T17_t1_mem0*MAS_MEM[12]
	S += (T81*MAS[7])-1 < T17_t1_mem0*MAS_MEM[14]
	S += T17_t1_mem0 <= T17_t1

	T17_t1_mem1 = S.Task('T17_t1_mem1', length=1, delay_cost=1)
	T17_t1_mem1 += MAS_MEM[1]
	S += 32 < T17_t1_mem1
	S += T17_t1_mem1 <= T17_t1

	T17_t2 = S.Task('T17_t2', length=1, delay_cost=1)
	T17_t2 += alt(MAS)
	T17_t2_mem0 = S.Task('T17_t2_mem0', length=1, delay_cost=1)
	T17_t2_mem0 += alt(MAS_MEM)
	S += (T80*MAS[0])-1 < T17_t2_mem0*MAS_MEM[0]
	S += (T80*MAS[1])-1 < T17_t2_mem0*MAS_MEM[2]
	S += (T80*MAS[2])-1 < T17_t2_mem0*MAS_MEM[4]
	S += (T80*MAS[3])-1 < T17_t2_mem0*MAS_MEM[6]
	S += (T80*MAS[4])-1 < T17_t2_mem0*MAS_MEM[8]
	S += (T80*MAS[5])-1 < T17_t2_mem0*MAS_MEM[10]
	S += (T80*MAS[6])-1 < T17_t2_mem0*MAS_MEM[12]
	S += (T80*MAS[7])-1 < T17_t2_mem0*MAS_MEM[14]
	S += T17_t2_mem0 <= T17_t2

	T17_t2_mem1 = S.Task('T17_t2_mem1', length=1, delay_cost=1)
	T17_t2_mem1 += alt(MAS_MEM)
	S += (T81*MAS[0])-1 < T17_t2_mem1*MAS_MEM[1]
	S += (T81*MAS[1])-1 < T17_t2_mem1*MAS_MEM[3]
	S += (T81*MAS[2])-1 < T17_t2_mem1*MAS_MEM[5]
	S += (T81*MAS[3])-1 < T17_t2_mem1*MAS_MEM[7]
	S += (T81*MAS[4])-1 < T17_t2_mem1*MAS_MEM[9]
	S += (T81*MAS[5])-1 < T17_t2_mem1*MAS_MEM[11]
	S += (T81*MAS[6])-1 < T17_t2_mem1*MAS_MEM[13]
	S += (T81*MAS[7])-1 < T17_t2_mem1*MAS_MEM[15]
	S += T17_t2_mem1 <= T17_t2

	T181 = S.Task('T181', length=1, delay_cost=1)
	T181 += alt(MAS)
	T181_mem0 = S.Task('T181_mem0', length=1, delay_cost=1)
	T181_mem0 += MAS_MEM[10]
	S += 14 < T181_mem0
	S += T181_mem0 <= T181

	T181_mem1 = S.Task('T181_mem1', length=1, delay_cost=1)
	T181_mem1 += alt(MAS_MEM)
	S += (T91*MAS[0])-1 < T181_mem1*MAS_MEM[1]
	S += (T91*MAS[1])-1 < T181_mem1*MAS_MEM[3]
	S += (T91*MAS[2])-1 < T181_mem1*MAS_MEM[5]
	S += (T91*MAS[3])-1 < T181_mem1*MAS_MEM[7]
	S += (T91*MAS[4])-1 < T181_mem1*MAS_MEM[9]
	S += (T91*MAS[5])-1 < T181_mem1*MAS_MEM[11]
	S += (T91*MAS[6])-1 < T181_mem1*MAS_MEM[13]
	S += (T91*MAS[7])-1 < T181_mem1*MAS_MEM[15]
	S += T181_mem1 <= T181

	T191 = S.Task('T191', length=1, delay_cost=1)
	T191 += alt(MAS)
	T191_mem0 = S.Task('T191_mem0', length=1, delay_cost=1)
	T191_mem0 += MAS_MEM[10]
	S += 14 < T191_mem0
	S += T191_mem0 <= T191

	T191_mem1 = S.Task('T191_mem1', length=1, delay_cost=1)
	T191_mem1 += alt(MAS_MEM)
	S += (T91*MAS[0])-1 < T191_mem1*MAS_MEM[1]
	S += (T91*MAS[1])-1 < T191_mem1*MAS_MEM[3]
	S += (T91*MAS[2])-1 < T191_mem1*MAS_MEM[5]
	S += (T91*MAS[3])-1 < T191_mem1*MAS_MEM[7]
	S += (T91*MAS[4])-1 < T191_mem1*MAS_MEM[9]
	S += (T91*MAS[5])-1 < T191_mem1*MAS_MEM[11]
	S += (T91*MAS[6])-1 < T191_mem1*MAS_MEM[13]
	S += (T91*MAS[7])-1 < T191_mem1*MAS_MEM[15]
	S += T191_mem1 <= T191

	T20_t0 = S.Task('T20_t0', length=7, delay_cost=1)
	T20_t0 += alt(MM)
	T20_t0_in = S.Task('T20_t0_in', length=1, delay_cost=1)
	T20_t0_in += alt(MM_in)
	S += T20_t0_in*MM_in[0]<=T20_t0*MM[0]
	S += T20_t0_in*MM_in[1]<=T20_t0*MM[1]
	T20_t0_mem0 = S.Task('T20_t0_mem0', length=1, delay_cost=1)
	T20_t0_mem0 += MAS_MEM[8]
	S += 30 < T20_t0_mem0
	S += T20_t0_mem0 <= T20_t0

	T20_t0_mem1 = S.Task('T20_t0_mem1', length=1, delay_cost=1)
	T20_t0_mem1 += alt(MAS_MEM)
	S += (T180*MAS[0])-1 < T20_t0_mem1*MAS_MEM[1]
	S += (T180*MAS[1])-1 < T20_t0_mem1*MAS_MEM[3]
	S += (T180*MAS[2])-1 < T20_t0_mem1*MAS_MEM[5]
	S += (T180*MAS[3])-1 < T20_t0_mem1*MAS_MEM[7]
	S += (T180*MAS[4])-1 < T20_t0_mem1*MAS_MEM[9]
	S += (T180*MAS[5])-1 < T20_t0_mem1*MAS_MEM[11]
	S += (T180*MAS[6])-1 < T20_t0_mem1*MAS_MEM[13]
	S += (T180*MAS[7])-1 < T20_t0_mem1*MAS_MEM[15]
	S += T20_t0_mem1 <= T20_t0

	T211 = S.Task('T211', length=1, delay_cost=1)
	T211 += alt(MAS)
	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	T211_mem0 += MAS_MEM[12]
	S += 25 < T211_mem0
	S += T211_mem0 <= T211

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	T211_mem1 += alt(MAS_MEM)
	S += (T101*MAS[0])-1 < T211_mem1*MAS_MEM[1]
	S += (T101*MAS[1])-1 < T211_mem1*MAS_MEM[3]
	S += (T101*MAS[2])-1 < T211_mem1*MAS_MEM[5]
	S += (T101*MAS[3])-1 < T211_mem1*MAS_MEM[7]
	S += (T101*MAS[4])-1 < T211_mem1*MAS_MEM[9]
	S += (T101*MAS[5])-1 < T211_mem1*MAS_MEM[11]
	S += (T101*MAS[6])-1 < T211_mem1*MAS_MEM[13]
	S += (T101*MAS[7])-1 < T211_mem1*MAS_MEM[15]
	S += T211_mem1 <= T211

	T24_t1 = S.Task('T24_t1', length=7, delay_cost=1)
	T24_t1 += alt(MM)
	T24_t1_in = S.Task('T24_t1_in', length=1, delay_cost=1)
	T24_t1_in += alt(MM_in)
	S += T24_t1_in*MM_in[0]<=T24_t1*MM[0]
	S += T24_t1_in*MM_in[1]<=T24_t1*MM[1]
	T24_t1_mem0 = S.Task('T24_t1_mem0', length=1, delay_cost=1)
	T24_t1_mem0 += alt(MAS_MEM)
	S += (T111*MAS[0])-1 < T24_t1_mem0*MAS_MEM[0]
	S += (T111*MAS[1])-1 < T24_t1_mem0*MAS_MEM[2]
	S += (T111*MAS[2])-1 < T24_t1_mem0*MAS_MEM[4]
	S += (T111*MAS[3])-1 < T24_t1_mem0*MAS_MEM[6]
	S += (T111*MAS[4])-1 < T24_t1_mem0*MAS_MEM[8]
	S += (T111*MAS[5])-1 < T24_t1_mem0*MAS_MEM[10]
	S += (T111*MAS[6])-1 < T24_t1_mem0*MAS_MEM[12]
	S += (T111*MAS[7])-1 < T24_t1_mem0*MAS_MEM[14]
	S += T24_t1_mem0 <= T24_t1

	T24_t1_mem1 = S.Task('T24_t1_mem1', length=1, delay_cost=1)
	T24_t1_mem1 += MAS_MEM[1]
	S += 40 < T24_t1_mem1
	S += T24_t1_mem1 <= T24_t1

	T24_t2 = S.Task('T24_t2', length=1, delay_cost=1)
	T24_t2 += alt(MAS)
	T24_t2_mem0 = S.Task('T24_t2_mem0', length=1, delay_cost=1)
	T24_t2_mem0 += alt(MAS_MEM)
	S += (T110*MAS[0])-1 < T24_t2_mem0*MAS_MEM[0]
	S += (T110*MAS[1])-1 < T24_t2_mem0*MAS_MEM[2]
	S += (T110*MAS[2])-1 < T24_t2_mem0*MAS_MEM[4]
	S += (T110*MAS[3])-1 < T24_t2_mem0*MAS_MEM[6]
	S += (T110*MAS[4])-1 < T24_t2_mem0*MAS_MEM[8]
	S += (T110*MAS[5])-1 < T24_t2_mem0*MAS_MEM[10]
	S += (T110*MAS[6])-1 < T24_t2_mem0*MAS_MEM[12]
	S += (T110*MAS[7])-1 < T24_t2_mem0*MAS_MEM[14]
	S += T24_t2_mem0 <= T24_t2

	T24_t2_mem1 = S.Task('T24_t2_mem1', length=1, delay_cost=1)
	T24_t2_mem1 += alt(MAS_MEM)
	S += (T111*MAS[0])-1 < T24_t2_mem1*MAS_MEM[1]
	S += (T111*MAS[1])-1 < T24_t2_mem1*MAS_MEM[3]
	S += (T111*MAS[2])-1 < T24_t2_mem1*MAS_MEM[5]
	S += (T111*MAS[3])-1 < T24_t2_mem1*MAS_MEM[7]
	S += (T111*MAS[4])-1 < T24_t2_mem1*MAS_MEM[9]
	S += (T111*MAS[5])-1 < T24_t2_mem1*MAS_MEM[11]
	S += (T111*MAS[6])-1 < T24_t2_mem1*MAS_MEM[13]
	S += (T111*MAS[7])-1 < T24_t2_mem1*MAS_MEM[15]
	S += T24_t2_mem1 <= T24_t2

	Z3_t0 = S.Task('Z3_t0', length=7, delay_cost=1)
	Z3_t0 += alt(MM)
	Z3_t0_in = S.Task('Z3_t0_in', length=1, delay_cost=1)
	Z3_t0_in += alt(MM_in)
	S += Z3_t0_in*MM_in[0]<=Z3_t0*MM[0]
	S += Z3_t0_in*MM_in[1]<=Z3_t0*MM[1]
	Z3_t0_mem0 = S.Task('Z3_t0_mem0', length=1, delay_cost=1)
	Z3_t0_mem0 += MAIN_MEM_r[0]
	S += Z3_t0_mem0 <= Z3_t0

	Z3_t0_mem1 = S.Task('Z3_t0_mem1', length=1, delay_cost=1)
	Z3_t0_mem1 += alt(MAS_MEM)
	S += (T140*MAS[0])-1 < Z3_t0_mem1*MAS_MEM[1]
	S += (T140*MAS[1])-1 < Z3_t0_mem1*MAS_MEM[3]
	S += (T140*MAS[2])-1 < Z3_t0_mem1*MAS_MEM[5]
	S += (T140*MAS[3])-1 < Z3_t0_mem1*MAS_MEM[7]
	S += (T140*MAS[4])-1 < Z3_t0_mem1*MAS_MEM[9]
	S += (T140*MAS[5])-1 < Z3_t0_mem1*MAS_MEM[11]
	S += (T140*MAS[6])-1 < Z3_t0_mem1*MAS_MEM[13]
	S += (T140*MAS[7])-1 < Z3_t0_mem1*MAS_MEM[15]
	S += Z3_t0_mem1 <= Z3_t0

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM2_stage1MAS8/EP2_LADDERMUL/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

