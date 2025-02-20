from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 195
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	T9_t2_in = S.Task('T9_t2_in', length=1, delay_cost=1)
	S += T9_t2_in >= 0
	T9_t2_in += MAS_in[1]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	S += T9_t2_mem0 >= 0
	T9_t2_mem0 += MAIN_MEM_r[0]

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	S += T9_t2_mem1 >= 0
	T9_t2_mem1 += MAIN_MEM_r[1]

	T6_t2_in = S.Task('T6_t2_in', length=1, delay_cost=1)
	S += T6_t2_in >= 1
	T6_t2_in += MAS_in[4]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	S += T6_t2_mem0 >= 1
	T6_t2_mem0 += MAIN_MEM_r[0]

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	S += T6_t2_mem1 >= 1
	T6_t2_mem1 += MAIN_MEM_r[1]

	T9_t2 = S.Task('T9_t2', length=4, delay_cost=1)
	S += T9_t2 >= 1
	T9_t2 += MAS[1]

	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	S += T3_t0_in >= 2
	T3_t0_in += MM_in[0]

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	S += T3_t0_mem0 >= 2
	T3_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	S += T3_t0_mem1 >= 2
	T3_t0_mem1 += MAIN_MEM_r[1]

	T6_t2 = S.Task('T6_t2', length=4, delay_cost=1)
	S += T6_t2 >= 2
	T6_t2 += MAS[4]

	T3_t0 = S.Task('T3_t0', length=11, delay_cost=1)
	S += T3_t0 >= 3
	T3_t0 += MM[0]

	T7_t3_in = S.Task('T7_t3_in', length=1, delay_cost=1)
	S += T7_t3_in >= 3
	T7_t3_in += MAS_in[2]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	S += T7_t3_mem0 >= 3
	T7_t3_mem0 += MAIN_MEM_r[0]

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	S += T7_t3_mem1 >= 3
	T7_t3_mem1 += MAIN_MEM_r[1]

	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	S += T4_t0_in >= 4
	T4_t0_in += MM_in[0]

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	S += T4_t0_mem0 >= 4
	T4_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	S += T4_t0_mem1 >= 4
	T4_t0_mem1 += MAIN_MEM_r[1]

	T7_t3 = S.Task('T7_t3', length=4, delay_cost=1)
	S += T7_t3 >= 4
	T7_t3 += MAS[2]

	T4_t0 = S.Task('T4_t0', length=11, delay_cost=1)
	S += T4_t0 >= 5
	T4_t0 += MM[0]

	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	S += T7_t0_in >= 5
	T7_t0_in += MM_in[0]

	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	S += T7_t0_mem0 >= 5
	T7_t0_mem0 += MAIN_MEM_r[0]

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	S += T7_t0_mem1 >= 5
	T7_t0_mem1 += MAIN_MEM_r[1]

	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	S += T5_t3_in >= 6
	T5_t3_in += MM_in[1]

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	S += T5_t3_mem0 >= 6
	T5_t3_mem0 += MAIN_MEM_r[0]

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	S += T5_t3_mem1 >= 6
	T5_t3_mem1 += MAIN_MEM_r[1]

	T7_t0 = S.Task('T7_t0', length=11, delay_cost=1)
	S += T7_t0 >= 6
	T7_t0 += MM[0]

	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	S += T3_t1_in >= 7
	T3_t1_in += MM_in[1]

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	S += T3_t1_mem0 >= 7
	T3_t1_mem0 += MAIN_MEM_r[0]

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	S += T3_t1_mem1 >= 7
	T3_t1_mem1 += MAIN_MEM_r[1]

	T5_t3 = S.Task('T5_t3', length=11, delay_cost=1)
	S += T5_t3 >= 7
	T5_t3 += MM[1]

	T11_t2_in = S.Task('T11_t2_in', length=1, delay_cost=1)
	S += T11_t2_in >= 8
	T11_t2_in += MAS_in[0]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	S += T11_t2_mem0 >= 8
	T11_t2_mem0 += MAIN_MEM_r[0]

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	S += T11_t2_mem1 >= 8
	T11_t2_mem1 += MAIN_MEM_r[1]

	T3_t1 = S.Task('T3_t1', length=11, delay_cost=1)
	S += T3_t1 >= 8
	T3_t1 += MM[1]

	T11_t2 = S.Task('T11_t2', length=4, delay_cost=1)
	S += T11_t2 >= 9
	T11_t2 += MAS[0]

	T5_t1_in = S.Task('T5_t1_in', length=1, delay_cost=1)
	S += T5_t1_in >= 9
	T5_t1_in += MAS_in[0]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	S += T5_t1_mem0 >= 9
	T5_t1_mem0 += MAIN_MEM_r[0]

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	S += T5_t1_mem1 >= 9
	T5_t1_mem1 += MAIN_MEM_r[1]

	T4_t2_in = S.Task('T4_t2_in', length=1, delay_cost=1)
	S += T4_t2_in >= 10
	T4_t2_in += MAS_in[0]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	S += T4_t2_mem0 >= 10
	T4_t2_mem0 += MAIN_MEM_r[0]

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	S += T4_t2_mem1 >= 10
	T4_t2_mem1 += MAIN_MEM_r[1]

	T5_t1 = S.Task('T5_t1', length=4, delay_cost=1)
	S += T5_t1 >= 10
	T5_t1 += MAS[0]

	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	S += T1_t3_in >= 11
	T1_t3_in += MM_in[0]

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	S += T1_t3_mem0 >= 11
	T1_t3_mem0 += MAIN_MEM_r[0]

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	S += T1_t3_mem1 >= 11
	T1_t3_mem1 += MAIN_MEM_r[1]

	T4_t2 = S.Task('T4_t2', length=4, delay_cost=1)
	S += T4_t2 >= 11
	T4_t2 += MAS[0]

	T1_t3 = S.Task('T1_t3', length=11, delay_cost=1)
	S += T1_t3 >= 12
	T1_t3 += MM[0]

	T5_t0_in = S.Task('T5_t0_in', length=1, delay_cost=1)
	S += T5_t0_in >= 12
	T5_t0_in += MAS_in[0]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	S += T5_t0_mem0 >= 12
	T5_t0_mem0 += MAIN_MEM_r[0]

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	S += T5_t0_mem1 >= 12
	T5_t0_mem1 += MAIN_MEM_r[1]

	T3_t2_in = S.Task('T3_t2_in', length=1, delay_cost=1)
	S += T3_t2_in >= 13
	T3_t2_in += MAS_in[4]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	S += T3_t2_mem0 >= 13
	T3_t2_mem0 += MAIN_MEM_r[0]

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	S += T3_t2_mem1 >= 13
	T3_t2_mem1 += MAIN_MEM_r[1]

	T5_t0 = S.Task('T5_t0', length=4, delay_cost=1)
	S += T5_t0 >= 13
	T5_t0 += MAS[0]

	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	S += T2_t0_in >= 14
	T2_t0_in += MM_in[1]

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	S += T2_t0_mem0 >= 14
	T2_t0_mem0 += MAIN_MEM_r[0]

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	S += T2_t0_mem1 >= 14
	T2_t0_mem1 += MAIN_MEM_r[1]

	T3_t2 = S.Task('T3_t2', length=4, delay_cost=1)
	S += T3_t2 >= 14
	T3_t2 += MAS[4]

	T2_t0 = S.Task('T2_t0', length=11, delay_cost=1)
	S += T2_t0 >= 15
	T2_t0 += MM[1]

	T2_t3_in = S.Task('T2_t3_in', length=1, delay_cost=1)
	S += T2_t3_in >= 15
	T2_t3_in += MAS_in[1]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	S += T2_t3_mem0 >= 15
	T2_t3_mem0 += MAIN_MEM_r[0]

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	S += T2_t3_mem1 >= 15
	T2_t3_mem1 += MAIN_MEM_r[1]

	T2_t3 = S.Task('T2_t3', length=4, delay_cost=1)
	S += T2_t3 >= 16
	T2_t3 += MAS[1]

	T5_t2_in = S.Task('T5_t2_in', length=1, delay_cost=1)
	S += T5_t2_in >= 16
	T5_t2_in += MM_in[0]

	T5_t2_mem0 = S.Task('T5_t2_mem0', length=1, delay_cost=1)
	S += T5_t2_mem0 >= 16
	T5_t2_mem0 += MAS_MEM[0]

	T5_t2_mem1 = S.Task('T5_t2_mem1', length=1, delay_cost=1)
	S += T5_t2_mem1 >= 16
	T5_t2_mem1 += MAS_MEM[1]

	T6_t3_in = S.Task('T6_t3_in', length=1, delay_cost=1)
	S += T6_t3_in >= 16
	T6_t3_in += MAS_in[1]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	S += T6_t3_mem0 >= 16
	T6_t3_mem0 += MAIN_MEM_r[0]

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	S += T6_t3_mem1 >= 16
	T6_t3_mem1 += MAIN_MEM_r[1]

	T51_in = S.Task('T51_in', length=1, delay_cost=1)
	S += T51_in >= 17
	T51_in += MAS_in[4]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 17
	T51_mem0 += MM_MEM[2]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 17
	T51_mem1 += MM_MEM[3]

	T5_t2 = S.Task('T5_t2', length=11, delay_cost=1)
	S += T5_t2 >= 17
	T5_t2 += MM[0]

	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	S += T6_t0_in >= 17
	T6_t0_in += MM_in[0]

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	S += T6_t0_mem0 >= 17
	T6_t0_mem0 += MAIN_MEM_r[0]

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	S += T6_t0_mem1 >= 17
	T6_t0_mem1 += MAIN_MEM_r[1]

	T6_t3 = S.Task('T6_t3', length=4, delay_cost=1)
	S += T6_t3 >= 17
	T6_t3 += MAS[1]

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	S += T30_in >= 18
	T30_in += MAS_in[1]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 18
	T30_mem0 += MM_MEM[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 18
	T30_mem1 += MM_MEM[3]

	T51 = S.Task('T51', length=4, delay_cost=1)
	S += T51 >= 18
	T51 += MAS[4]

	T6_t0 = S.Task('T6_t0', length=11, delay_cost=1)
	S += T6_t0 >= 18
	T6_t0 += MM[0]

	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	S += T7_t1_in >= 18
	T7_t1_in += MM_in[1]

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	S += T7_t1_mem0 >= 18
	T7_t1_mem0 += MAIN_MEM_r[0]

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	S += T7_t1_mem1 >= 18
	T7_t1_mem1 += MAIN_MEM_r[1]

	T30 = S.Task('T30', length=4, delay_cost=1)
	S += T30 >= 19
	T30 += MAS[1]

	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	S += T4_t1_in >= 19
	T4_t1_in += MM_in[0]

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	S += T4_t1_mem0 >= 19
	T4_t1_mem0 += MAIN_MEM_r[0]

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	S += T4_t1_mem1 >= 19
	T4_t1_mem1 += MAIN_MEM_r[1]

	T5_t5_in = S.Task('T5_t5_in', length=1, delay_cost=1)
	S += T5_t5_in >= 19
	T5_t5_in += MAS_in[1]

	T5_t5_mem0 = S.Task('T5_t5_mem0', length=1, delay_cost=1)
	S += T5_t5_mem0 >= 19
	T5_t5_mem0 += MM_MEM[2]

	T5_t5_mem1 = S.Task('T5_t5_mem1', length=1, delay_cost=1)
	S += T5_t5_mem1 >= 19
	T5_t5_mem1 += MM_MEM[3]

	T7_t1 = S.Task('T7_t1', length=11, delay_cost=1)
	S += T7_t1 >= 19
	T7_t1 += MM[1]

	T1_t1_in = S.Task('T1_t1_in', length=1, delay_cost=1)
	S += T1_t1_in >= 20
	T1_t1_in += MAS_in[0]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	S += T1_t1_mem0 >= 20
	T1_t1_mem0 += MAIN_MEM_r[0]

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	S += T1_t1_mem1 >= 20
	T1_t1_mem1 += MAIN_MEM_r[1]

	T3_t5_in = S.Task('T3_t5_in', length=1, delay_cost=1)
	S += T3_t5_in >= 20
	T3_t5_in += MAS_in[2]

	T3_t5_mem0 = S.Task('T3_t5_mem0', length=1, delay_cost=1)
	S += T3_t5_mem0 >= 20
	T3_t5_mem0 += MM_MEM[0]

	T3_t5_mem1 = S.Task('T3_t5_mem1', length=1, delay_cost=1)
	S += T3_t5_mem1 >= 20
	T3_t5_mem1 += MM_MEM[3]

	T4_t1 = S.Task('T4_t1', length=11, delay_cost=1)
	S += T4_t1 >= 20
	T4_t1 += MM[0]

	T5_t5 = S.Task('T5_t5', length=4, delay_cost=1)
	S += T5_t5 >= 20
	T5_t5 += MAS[1]

	T6_t4_in = S.Task('T6_t4_in', length=1, delay_cost=1)
	S += T6_t4_in >= 20
	T6_t4_in += MM_in[0]

	T6_t4_mem0 = S.Task('T6_t4_mem0', length=1, delay_cost=1)
	S += T6_t4_mem0 >= 20
	T6_t4_mem0 += MAS_MEM[8]

	T6_t4_mem1 = S.Task('T6_t4_mem1', length=1, delay_cost=1)
	S += T6_t4_mem1 >= 20
	T6_t4_mem1 += MAS_MEM[3]

	T1_t1 = S.Task('T1_t1', length=4, delay_cost=1)
	S += T1_t1 >= 21
	T1_t1 += MAS[0]

	T3_t5 = S.Task('T3_t5', length=4, delay_cost=1)
	S += T3_t5 >= 21
	T3_t5 += MAS[2]

	T4_t3_in = S.Task('T4_t3_in', length=1, delay_cost=1)
	S += T4_t3_in >= 21
	T4_t3_in += MAS_in[4]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	S += T4_t3_mem0 >= 21
	T4_t3_mem0 += MAIN_MEM_r[0]

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	S += T4_t3_mem1 >= 21
	T4_t3_mem1 += MAIN_MEM_r[1]

	T6_t4 = S.Task('T6_t4', length=11, delay_cost=1)
	S += T6_t4 >= 21
	T6_t4 += MM[0]

	T10_t2_in = S.Task('T10_t2_in', length=1, delay_cost=1)
	S += T10_t2_in >= 22
	T10_t2_in += MAS_in[4]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	S += T10_t2_mem0 >= 22
	T10_t2_mem0 += MAIN_MEM_r[0]

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	S += T10_t2_mem1 >= 22
	T10_t2_mem1 += MAIN_MEM_r[1]

	T1_t5_in = S.Task('T1_t5_in', length=1, delay_cost=1)
	S += T1_t5_in >= 22
	T1_t5_in += MAS_in[3]

	T1_t5_mem0 = S.Task('T1_t5_mem0', length=1, delay_cost=1)
	S += T1_t5_mem0 >= 22
	T1_t5_mem0 += MM_MEM[0]

	T1_t5_mem1 = S.Task('T1_t5_mem1', length=1, delay_cost=1)
	S += T1_t5_mem1 >= 22
	T1_t5_mem1 += MM_MEM[1]

	T4_t3 = S.Task('T4_t3', length=4, delay_cost=1)
	S += T4_t3 >= 22
	T4_t3 += MAS[4]

	T10_t2 = S.Task('T10_t2', length=4, delay_cost=1)
	S += T10_t2 >= 23
	T10_t2 += MAS[4]

	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	S += T11_in >= 23
	T11_in += MAS_in[0]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 23
	T11_mem0 += MM_MEM[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 23
	T11_mem1 += MM_MEM[1]

	T1_t5 = S.Task('T1_t5', length=4, delay_cost=1)
	S += T1_t5 >= 23
	T1_t5 += MAS[3]

	T3_t3_in = S.Task('T3_t3_in', length=1, delay_cost=1)
	S += T3_t3_in >= 23
	T3_t3_in += MAS_in[2]

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	S += T3_t3_mem0 >= 23
	T3_t3_mem0 += MAIN_MEM_r[0]

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	S += T3_t3_mem1 >= 23
	T3_t3_mem1 += MAIN_MEM_r[1]

	T11 = S.Task('T11', length=4, delay_cost=1)
	S += T11 >= 24
	T11 += MAS[0]

	T3_t3 = S.Task('T3_t3', length=4, delay_cost=1)
	S += T3_t3 >= 24
	T3_t3 += MAS[2]

	T7_t2_in = S.Task('T7_t2_in', length=1, delay_cost=1)
	S += T7_t2_in >= 24
	T7_t2_in += MAS_in[4]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	S += T7_t2_mem0 >= 24
	T7_t2_mem0 += MAIN_MEM_r[0]

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	S += T7_t2_mem1 >= 24
	T7_t2_mem1 += MAIN_MEM_r[1]

	T4_t4_in = S.Task('T4_t4_in', length=1, delay_cost=1)
	S += T4_t4_in >= 25
	T4_t4_in += MM_in[0]

	T4_t4_mem0 = S.Task('T4_t4_mem0', length=1, delay_cost=1)
	S += T4_t4_mem0 >= 25
	T4_t4_mem0 += MAS_MEM[0]

	T4_t4_mem1 = S.Task('T4_t4_mem1', length=1, delay_cost=1)
	S += T4_t4_mem1 >= 25
	T4_t4_mem1 += MAS_MEM[9]

	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	S += T6_t1_in >= 25
	T6_t1_in += MM_in[1]

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	S += T6_t1_mem0 >= 25
	T6_t1_mem0 += MAIN_MEM_r[0]

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	S += T6_t1_mem1 >= 25
	T6_t1_mem1 += MAIN_MEM_r[1]

	T7_t2 = S.Task('T7_t2', length=4, delay_cost=1)
	S += T7_t2 >= 25
	T7_t2 += MAS[4]

	T4_t4 = S.Task('T4_t4', length=11, delay_cost=1)
	S += T4_t4 >= 26
	T4_t4 += MM[0]

	T6_t1 = S.Task('T6_t1', length=11, delay_cost=1)
	S += T6_t1 >= 26
	T6_t1 += MM[1]

	T8_t2_in = S.Task('T8_t2_in', length=1, delay_cost=1)
	S += T8_t2_in >= 26
	T8_t2_in += MAS_in[4]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	S += T8_t2_mem0 >= 26
	T8_t2_mem0 += MAIN_MEM_r[0]

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	S += T8_t2_mem1 >= 26
	T8_t2_mem1 += MAIN_MEM_r[1]

	T2_t2_in = S.Task('T2_t2_in', length=1, delay_cost=1)
	S += T2_t2_in >= 27
	T2_t2_in += MAS_in[3]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	S += T2_t2_mem0 >= 27
	T2_t2_mem0 += MAIN_MEM_r[0]

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	S += T2_t2_mem1 >= 27
	T2_t2_mem1 += MAIN_MEM_r[1]

	T3_t4_in = S.Task('T3_t4_in', length=1, delay_cost=1)
	S += T3_t4_in >= 27
	T3_t4_in += MM_in[1]

	T3_t4_mem0 = S.Task('T3_t4_mem0', length=1, delay_cost=1)
	S += T3_t4_mem0 >= 27
	T3_t4_mem0 += MAS_MEM[8]

	T3_t4_mem1 = S.Task('T3_t4_mem1', length=1, delay_cost=1)
	S += T3_t4_mem1 >= 27
	T3_t4_mem1 += MAS_MEM[5]

	T50_in = S.Task('T50_in', length=1, delay_cost=1)
	S += T50_in >= 27
	T50_in += MAS_in[4]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 27
	T50_mem0 += MM_MEM[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 27
	T50_mem1 += MAS_MEM[3]

	T8_t2 = S.Task('T8_t2', length=4, delay_cost=1)
	S += T8_t2 >= 27
	T8_t2 += MAS[4]

	T1_t0_in = S.Task('T1_t0_in', length=1, delay_cost=1)
	S += T1_t0_in >= 28
	T1_t0_in += MAS_in[5]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	S += T1_t0_mem0 >= 28
	T1_t0_mem0 += MAIN_MEM_r[0]

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	S += T1_t0_mem1 >= 28
	T1_t0_mem1 += MAIN_MEM_r[1]

	T2_t2 = S.Task('T2_t2', length=4, delay_cost=1)
	S += T2_t2 >= 28
	T2_t2 += MAS[3]

	T3_t4 = S.Task('T3_t4', length=11, delay_cost=1)
	S += T3_t4 >= 28
	T3_t4 += MM[1]

	T50 = S.Task('T50', length=4, delay_cost=1)
	S += T50 >= 28
	T50 += MAS[4]

	T7_t4_in = S.Task('T7_t4_in', length=1, delay_cost=1)
	S += T7_t4_in >= 28
	T7_t4_in += MM_in[0]

	T7_t4_mem0 = S.Task('T7_t4_mem0', length=1, delay_cost=1)
	S += T7_t4_mem0 >= 28
	T7_t4_mem0 += MAS_MEM[8]

	T7_t4_mem1 = S.Task('T7_t4_mem1', length=1, delay_cost=1)
	S += T7_t4_mem1 >= 28
	T7_t4_mem1 += MAS_MEM[5]

	T1_t0 = S.Task('T1_t0', length=4, delay_cost=1)
	S += T1_t0 >= 29
	T1_t0 += MAS[5]

	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	S += T2_t1_in >= 29
	T2_t1_in += MM_in[0]

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	S += T2_t1_mem0 >= 29
	T2_t1_mem0 += MAIN_MEM_r[0]

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	S += T2_t1_mem1 >= 29
	T2_t1_mem1 += MAIN_MEM_r[1]

	T70_in = S.Task('T70_in', length=1, delay_cost=1)
	S += T70_in >= 29
	T70_in += MAS_in[5]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 29
	T70_mem0 += MM_MEM[0]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 29
	T70_mem1 += MM_MEM[3]

	T7_t4 = S.Task('T7_t4', length=11, delay_cost=1)
	S += T7_t4 >= 29
	T7_t4 += MM[0]

	T2_t1 = S.Task('T2_t1', length=11, delay_cost=1)
	S += T2_t1 >= 30
	T2_t1 += MM[0]

	T70 = S.Task('T70', length=4, delay_cost=1)
	S += T70 >= 30
	T70 += MAS[5]

	T7_t5_in = S.Task('T7_t5_in', length=1, delay_cost=1)
	S += T7_t5_in >= 30
	T7_t5_in += MAS_in[2]

	T7_t5_mem0 = S.Task('T7_t5_mem0', length=1, delay_cost=1)
	S += T7_t5_mem0 >= 30
	T7_t5_mem0 += MM_MEM[0]

	T7_t5_mem1 = S.Task('T7_t5_mem1', length=1, delay_cost=1)
	S += T7_t5_mem1 >= 30
	T7_t5_mem1 += MM_MEM[3]

	T9_t1_in = S.Task('T9_t1_in', length=1, delay_cost=1)
	S += T9_t1_in >= 30
	T9_t1_in += MM_in[1]

	T9_t1_mem0 = S.Task('T9_t1_mem0', length=1, delay_cost=1)
	S += T9_t1_mem0 >= 30
	T9_t1_mem0 += MAIN_MEM_r[0]

	T9_t1_mem1 = S.Task('T9_t1_mem1', length=1, delay_cost=1)
	S += T9_t1_mem1 >= 30
	T9_t1_mem1 += MAS_MEM[1]

	T20_t2_in = S.Task('T20_t2_in', length=1, delay_cost=1)
	S += T20_t2_in >= 31
	T20_t2_in += MAS_in[2]

	T20_t2_mem0 = S.Task('T20_t2_mem0', length=1, delay_cost=1)
	S += T20_t2_mem0 >= 31
	T20_t2_mem0 += MAS_MEM[8]

	T20_t2_mem1 = S.Task('T20_t2_mem1', length=1, delay_cost=1)
	S += T20_t2_mem1 >= 31
	T20_t2_mem1 += MAS_MEM[9]

	T2_t4_in = S.Task('T2_t4_in', length=1, delay_cost=1)
	S += T2_t4_in >= 31
	T2_t4_in += MM_in[1]

	T2_t4_mem0 = S.Task('T2_t4_mem0', length=1, delay_cost=1)
	S += T2_t4_mem0 >= 31
	T2_t4_mem0 += MAS_MEM[6]

	T2_t4_mem1 = S.Task('T2_t4_mem1', length=1, delay_cost=1)
	S += T2_t4_mem1 >= 31
	T2_t4_mem1 += MAS_MEM[3]

	T40_in = S.Task('T40_in', length=1, delay_cost=1)
	S += T40_in >= 31
	T40_in += MAS_in[5]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 31
	T40_mem0 += MM_MEM[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 31
	T40_mem1 += MM_MEM[1]

	T7_t5 = S.Task('T7_t5', length=4, delay_cost=1)
	S += T7_t5 >= 31
	T7_t5 += MAS[2]

	T9_t1 = S.Task('T9_t1', length=11, delay_cost=1)
	S += T9_t1 >= 31
	T9_t1 += MM[1]

	Z3_t2_in = S.Task('Z3_t2_in', length=1, delay_cost=1)
	S += Z3_t2_in >= 31
	Z3_t2_in += MAS_in[4]

	Z3_t2_mem0 = S.Task('Z3_t2_mem0', length=1, delay_cost=1)
	S += Z3_t2_mem0 >= 31
	Z3_t2_mem0 += MAIN_MEM_r[0]

	Z3_t2_mem1 = S.Task('Z3_t2_mem1', length=1, delay_cost=1)
	S += Z3_t2_mem1 >= 31
	Z3_t2_mem1 += MAIN_MEM_r[1]

	T11_t0_in = S.Task('T11_t0_in', length=1, delay_cost=1)
	S += T11_t0_in >= 32
	T11_t0_in += MM_in[1]

	T11_t0_mem0 = S.Task('T11_t0_mem0', length=1, delay_cost=1)
	S += T11_t0_mem0 >= 32
	T11_t0_mem0 += MAIN_MEM_r[0]

	T11_t0_mem1 = S.Task('T11_t0_mem1', length=1, delay_cost=1)
	S += T11_t0_mem1 >= 32
	T11_t0_mem1 += MAS_MEM[3]

	T1_t2_in = S.Task('T1_t2_in', length=1, delay_cost=1)
	S += T1_t2_in >= 32
	T1_t2_in += MM_in[0]

	T1_t2_mem0 = S.Task('T1_t2_mem0', length=1, delay_cost=1)
	S += T1_t2_mem0 >= 32
	T1_t2_mem0 += MAS_MEM[10]

	T1_t2_mem1 = S.Task('T1_t2_mem1', length=1, delay_cost=1)
	S += T1_t2_mem1 >= 32
	T1_t2_mem1 += MAS_MEM[1]

	T20_t2 = S.Task('T20_t2', length=4, delay_cost=1)
	S += T20_t2 >= 32
	T20_t2 += MAS[2]

	T2_t4 = S.Task('T2_t4', length=11, delay_cost=1)
	S += T2_t4 >= 32
	T2_t4 += MM[1]

	T40 = S.Task('T40', length=4, delay_cost=1)
	S += T40 >= 32
	T40 += MAS[5]

	T4_t5_in = S.Task('T4_t5_in', length=1, delay_cost=1)
	S += T4_t5_in >= 32
	T4_t5_in += MAS_in[3]

	T4_t5_mem0 = S.Task('T4_t5_mem0', length=1, delay_cost=1)
	S += T4_t5_mem0 >= 32
	T4_t5_mem0 += MM_MEM[0]

	T4_t5_mem1 = S.Task('T4_t5_mem1', length=1, delay_cost=1)
	S += T4_t5_mem1 >= 32
	T4_t5_mem1 += MM_MEM[1]

	Z3_t2 = S.Task('Z3_t2', length=4, delay_cost=1)
	S += Z3_t2 >= 32
	Z3_t2 += MAS[4]

	T11_t0 = S.Task('T11_t0', length=11, delay_cost=1)
	S += T11_t0 >= 33
	T11_t0 += MM[1]

	T150_in = S.Task('T150_in', length=1, delay_cost=1)
	S += T150_in >= 33
	T150_in += MAS_in[4]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 33
	T150_mem0 += MAS_MEM[10]

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 33
	T150_mem1 += MAS_MEM[11]

	T1_t2 = S.Task('T1_t2', length=11, delay_cost=1)
	S += T1_t2 >= 33
	T1_t2 += MM[0]

	T4_t5 = S.Task('T4_t5', length=4, delay_cost=1)
	S += T4_t5 >= 33
	T4_t5 += MAS[3]

	T8_t1_in = S.Task('T8_t1_in', length=1, delay_cost=1)
	S += T8_t1_in >= 33
	T8_t1_in += MM_in[1]

	T8_t1_mem0 = S.Task('T8_t1_mem0', length=1, delay_cost=1)
	S += T8_t1_mem0 >= 33
	T8_t1_mem0 += MAIN_MEM_r[0]

	T8_t1_mem1 = S.Task('T8_t1_mem1', length=1, delay_cost=1)
	S += T8_t1_mem1 >= 33
	T8_t1_mem1 += MAS_MEM[1]

	T10_t0_in = S.Task('T10_t0_in', length=1, delay_cost=1)
	S += T10_t0_in >= 34
	T10_t0_in += MM_in[1]

	T10_t0_mem0 = S.Task('T10_t0_mem0', length=1, delay_cost=1)
	S += T10_t0_mem0 >= 34
	T10_t0_mem0 += MAIN_MEM_r[0]

	T10_t0_mem1 = S.Task('T10_t0_mem1', length=1, delay_cost=1)
	S += T10_t0_mem1 >= 34
	T10_t0_mem1 += MAS_MEM[3]

	T150 = S.Task('T150', length=4, delay_cost=1)
	S += T150 >= 34
	T150 += MAS[4]

	T8_t1 = S.Task('T8_t1', length=11, delay_cost=1)
	S += T8_t1 >= 34
	T8_t1 += MM[1]

	T10_t0 = S.Task('T10_t0', length=11, delay_cost=1)
	S += T10_t0 >= 35
	T10_t0 += MM[1]

	T6_t5_in = S.Task('T6_t5_in', length=1, delay_cost=1)
	S += T6_t5_in >= 36
	T6_t5_in += MAS_in[2]

	T6_t5_mem0 = S.Task('T6_t5_mem0', length=1, delay_cost=1)
	S += T6_t5_mem0 >= 36
	T6_t5_mem0 += MM_MEM[0]

	T6_t5_mem1 = S.Task('T6_t5_mem1', length=1, delay_cost=1)
	S += T6_t5_mem1 >= 36
	T6_t5_mem1 += MM_MEM[3]

	T41_in = S.Task('T41_in', length=1, delay_cost=1)
	S += T41_in >= 37
	T41_in += MAS_in[2]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 37
	T41_mem0 += MM_MEM[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 37
	T41_mem1 += MAS_MEM[7]

	T6_t5 = S.Task('T6_t5', length=4, delay_cost=1)
	S += T6_t5 >= 37
	T6_t5 += MAS[2]

	T31_in = S.Task('T31_in', length=1, delay_cost=1)
	S += T31_in >= 38
	T31_in += MAS_in[0]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 38
	T31_mem0 += MM_MEM[2]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 38
	T31_mem1 += MAS_MEM[5]

	T41 = S.Task('T41', length=4, delay_cost=1)
	S += T41 >= 38
	T41 += MAS[2]

	T60_in = S.Task('T60_in', length=1, delay_cost=1)
	S += T60_in >= 38
	T60_in += MAS_in[4]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 38
	T60_mem0 += MM_MEM[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 38
	T60_mem1 += MM_MEM[3]

	T31 = S.Task('T31', length=4, delay_cost=1)
	S += T31 >= 39
	T31 += MAS[0]

	T60 = S.Task('T60', length=4, delay_cost=1)
	S += T60 >= 39
	T60 += MAS[4]

	T71_in = S.Task('T71_in', length=1, delay_cost=1)
	S += T71_in >= 39
	T71_in += MAS_in[4]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 39
	T71_mem0 += MM_MEM[0]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 39
	T71_mem1 += MAS_MEM[5]

	T2_t5_in = S.Task('T2_t5_in', length=1, delay_cost=1)
	S += T2_t5_in >= 40
	T2_t5_in += MAS_in[2]

	T2_t5_mem0 = S.Task('T2_t5_mem0', length=1, delay_cost=1)
	S += T2_t5_mem0 >= 40
	T2_t5_mem0 += MM_MEM[2]

	T2_t5_mem1 = S.Task('T2_t5_mem1', length=1, delay_cost=1)
	S += T2_t5_mem1 >= 40
	T2_t5_mem1 += MM_MEM[1]

	T61_in = S.Task('T61_in', length=1, delay_cost=1)
	S += T61_in >= 40
	T61_in += MAS_in[4]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 40
	T61_mem0 += MM_MEM[0]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 40
	T61_mem1 += MAS_MEM[5]

	T71 = S.Task('T71', length=4, delay_cost=1)
	S += T71 >= 40
	T71 += MAS[4]

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	S += T20_in >= 41
	T20_in += MAS_in[4]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 41
	T20_mem0 += MM_MEM[2]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 41
	T20_mem1 += MM_MEM[1]

	T2_t5 = S.Task('T2_t5', length=4, delay_cost=1)
	S += T2_t5 >= 41
	T2_t5 += MAS[2]

	T61 = S.Task('T61', length=4, delay_cost=1)
	S += T61 >= 41
	T61 += MAS[4]

	T11_t3_in = S.Task('T11_t3_in', length=1, delay_cost=1)
	S += T11_t3_in >= 42
	T11_t3_in += MAS_in[2]

	T11_t3_mem0 = S.Task('T11_t3_mem0', length=1, delay_cost=1)
	S += T11_t3_mem0 >= 42
	T11_t3_mem0 += MAS_MEM[2]

	T11_t3_mem1 = S.Task('T11_t3_mem1', length=1, delay_cost=1)
	S += T11_t3_mem1 >= 42
	T11_t3_mem1 += MAS_MEM[1]

	T20 = S.Task('T20', length=4, delay_cost=1)
	S += T20 >= 42
	T20 += MAS[4]

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	S += T10_in >= 43
	T10_in += MAS_in[5]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 43
	T10_mem0 += MM_MEM[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 43
	T10_mem1 += MAS_MEM[7]

	T10_t3_in = S.Task('T10_t3_in', length=1, delay_cost=1)
	S += T10_t3_in >= 43
	T10_t3_in += MAS_in[4]

	T10_t3_mem0 = S.Task('T10_t3_mem0', length=1, delay_cost=1)
	S += T10_t3_mem0 >= 43
	T10_t3_mem0 += MAS_MEM[2]

	T10_t3_mem1 = S.Task('T10_t3_mem1', length=1, delay_cost=1)
	S += T10_t3_mem1 >= 43
	T10_t3_mem1 += MAS_MEM[1]

	T11_t3 = S.Task('T11_t3', length=4, delay_cost=1)
	S += T11_t3 >= 43
	T11_t3 += MAS[2]

	T151_in = S.Task('T151_in', length=1, delay_cost=1)
	S += T151_in >= 43
	T151_in += MAS_in[2]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 43
	T151_mem0 += MAS_MEM[8]

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 43
	T151_mem1 += MAS_MEM[9]

	T10 = S.Task('T10', length=4, delay_cost=1)
	S += T10 >= 44
	T10 += MAS[5]

	T10_t1_in = S.Task('T10_t1_in', length=1, delay_cost=1)
	S += T10_t1_in >= 44
	T10_t1_in += MM_in[1]

	T10_t1_mem0 = S.Task('T10_t1_mem0', length=1, delay_cost=1)
	S += T10_t1_mem0 >= 44
	T10_t1_mem0 += MAIN_MEM_r[0]

	T10_t1_mem1 = S.Task('T10_t1_mem1', length=1, delay_cost=1)
	S += T10_t1_mem1 >= 44
	T10_t1_mem1 += MAS_MEM[1]

	T10_t3 = S.Task('T10_t3', length=4, delay_cost=1)
	S += T10_t3 >= 44
	T10_t3 += MAS[4]

	T151 = S.Task('T151', length=4, delay_cost=1)
	S += T151 >= 44
	T151 += MAS[2]

	T21_in = S.Task('T21_in', length=1, delay_cost=1)
	S += T21_in >= 44
	T21_in += MAS_in[4]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 44
	T21_mem0 += MM_MEM[2]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 44
	T21_mem1 += MAS_MEM[5]

	T10_t1 = S.Task('T10_t1', length=11, delay_cost=1)
	S += T10_t1 >= 45
	T10_t1 += MM[1]

	T11_t1_in = S.Task('T11_t1_in', length=1, delay_cost=1)
	S += T11_t1_in >= 45
	T11_t1_in += MM_in[0]

	T11_t1_mem0 = S.Task('T11_t1_mem0', length=1, delay_cost=1)
	S += T11_t1_mem0 >= 45
	T11_t1_mem0 += MAIN_MEM_r[0]

	T11_t1_mem1 = S.Task('T11_t1_mem1', length=1, delay_cost=1)
	S += T11_t1_mem1 >= 45
	T11_t1_mem1 += MAS_MEM[1]

	T130_in = S.Task('T130_in', length=1, delay_cost=1)
	S += T130_in >= 45
	T130_in += MAS_in[1]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 45
	T130_mem0 += MAS_MEM[10]

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 45
	T130_mem1 += MAS_MEM[9]

	T21 = S.Task('T21', length=4, delay_cost=1)
	S += T21 >= 45
	T21 += MAS[4]

	T11_t1 = S.Task('T11_t1', length=11, delay_cost=1)
	S += T11_t1 >= 46
	T11_t1 += MM[0]

	T11_t4_in = S.Task('T11_t4_in', length=1, delay_cost=1)
	S += T11_t4_in >= 46
	T11_t4_in += MM_in[0]

	T11_t4_mem0 = S.Task('T11_t4_mem0', length=1, delay_cost=1)
	S += T11_t4_mem0 >= 46
	T11_t4_mem0 += MAS_MEM[0]

	T11_t4_mem1 = S.Task('T11_t4_mem1', length=1, delay_cost=1)
	S += T11_t4_mem1 >= 46
	T11_t4_mem1 += MAS_MEM[5]

	T120_in = S.Task('T120_in', length=1, delay_cost=1)
	S += T120_in >= 46
	T120_in += MAS_in[5]

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	S += T120_mem0 >= 46
	T120_mem0 += MAS_MEM[10]

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	S += T120_mem1 >= 46
	T120_mem1 += MAS_MEM[9]

	T130 = S.Task('T130', length=4, delay_cost=1)
	S += T130 >= 46
	T130 += MAS[1]

	T10_t4_in = S.Task('T10_t4_in', length=1, delay_cost=1)
	S += T10_t4_in >= 47
	T10_t4_in += MM_in[0]

	T10_t4_mem0 = S.Task('T10_t4_mem0', length=1, delay_cost=1)
	S += T10_t4_mem0 >= 47
	T10_t4_mem0 += MAS_MEM[8]

	T10_t4_mem1 = S.Task('T10_t4_mem1', length=1, delay_cost=1)
	S += T10_t4_mem1 >= 47
	T10_t4_mem1 += MAS_MEM[9]

	T11_t4 = S.Task('T11_t4', length=11, delay_cost=1)
	S += T11_t4 >= 47
	T11_t4 += MM[0]

	T120 = S.Task('T120', length=4, delay_cost=1)
	S += T120 >= 47
	T120 += MAS[5]

	T8_t0_in = S.Task('T8_t0_in', length=1, delay_cost=1)
	S += T8_t0_in >= 47
	T8_t0_in += MM_in[1]

	T8_t0_mem0 = S.Task('T8_t0_mem0', length=1, delay_cost=1)
	S += T8_t0_mem0 >= 47
	T8_t0_mem0 += MAIN_MEM_r[0]

	T8_t0_mem1 = S.Task('T8_t0_mem1', length=1, delay_cost=1)
	S += T8_t0_mem1 >= 47
	T8_t0_mem1 += MAS_MEM[11]

	T8_t3_in = S.Task('T8_t3_in', length=1, delay_cost=1)
	S += T8_t3_in >= 47
	T8_t3_in += MAS_in[2]

	T8_t3_mem0 = S.Task('T8_t3_mem0', length=1, delay_cost=1)
	S += T8_t3_mem0 >= 47
	T8_t3_mem0 += MAS_MEM[10]

	T8_t3_mem1 = S.Task('T8_t3_mem1', length=1, delay_cost=1)
	S += T8_t3_mem1 >= 47
	T8_t3_mem1 += MAS_MEM[1]

	T10_t4 = S.Task('T10_t4', length=11, delay_cost=1)
	S += T10_t4 >= 48
	T10_t4 += MM[0]

	T121_in = S.Task('T121_in', length=1, delay_cost=1)
	S += T121_in >= 48
	T121_in += MAS_in[2]

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	S += T121_mem0 >= 48
	T121_mem0 += MAS_MEM[4]

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	S += T121_mem1 >= 48
	T121_mem1 += MAS_MEM[9]

	T16_t2_in = S.Task('T16_t2_in', length=1, delay_cost=1)
	S += T16_t2_in >= 48
	T16_t2_in += MAS_in[5]

	T16_t2_mem0 = S.Task('T16_t2_mem0', length=1, delay_cost=1)
	S += T16_t2_mem0 >= 48
	T16_t2_mem0 += MAS_MEM[10]

	T16_t2_mem1 = S.Task('T16_t2_mem1', length=1, delay_cost=1)
	S += T16_t2_mem1 >= 48
	T16_t2_mem1 += MAS_MEM[1]

	T17_t3_in = S.Task('T17_t3_in', length=1, delay_cost=1)
	S += T17_t3_in >= 48
	T17_t3_in += MAS_in[4]

	T17_t3_mem0 = S.Task('T17_t3_mem0', length=1, delay_cost=1)
	S += T17_t3_mem0 >= 48
	T17_t3_mem0 += MAS_MEM[8]

	T17_t3_mem1 = S.Task('T17_t3_mem1', length=1, delay_cost=1)
	S += T17_t3_mem1 >= 48
	T17_t3_mem1 += MAS_MEM[5]

	T8_t0 = S.Task('T8_t0', length=11, delay_cost=1)
	S += T8_t0 >= 48
	T8_t0 += MM[1]

	T8_t3 = S.Task('T8_t3', length=4, delay_cost=1)
	S += T8_t3 >= 48
	T8_t3 += MAS[2]

	T9_t0_in = S.Task('T9_t0_in', length=1, delay_cost=1)
	S += T9_t0_in >= 48
	T9_t0_in += MM_in[1]

	T9_t0_mem0 = S.Task('T9_t0_mem0', length=1, delay_cost=1)
	S += T9_t0_mem0 >= 48
	T9_t0_mem0 += MAIN_MEM_r[0]

	T9_t0_mem1 = S.Task('T9_t0_mem1', length=1, delay_cost=1)
	S += T9_t0_mem1 >= 48
	T9_t0_mem1 += MAS_MEM[11]

	T121 = S.Task('T121', length=4, delay_cost=1)
	S += T121 >= 49
	T121 += MAS[2]

	T131_in = S.Task('T131_in', length=1, delay_cost=1)
	S += T131_in >= 49
	T131_in += MAS_in[3]

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 49
	T131_mem0 += MAS_MEM[4]

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 49
	T131_mem1 += MAS_MEM[9]

	T14_t0_in = S.Task('T14_t0_in', length=1, delay_cost=1)
	S += T14_t0_in >= 49
	T14_t0_in += MM_in[0]

	T14_t0_mem0 = S.Task('T14_t0_mem0', length=1, delay_cost=1)
	S += T14_t0_mem0 >= 49
	T14_t0_mem0 += MAS_MEM[2]

	T14_t0_mem1 = S.Task('T14_t0_mem1', length=1, delay_cost=1)
	S += T14_t0_mem1 >= 49
	T14_t0_mem1 += MAS_MEM[3]

	T16_t2 = S.Task('T16_t2', length=4, delay_cost=1)
	S += T16_t2 >= 49
	T16_t2 += MAS[5]

	T17_t3 = S.Task('T17_t3', length=4, delay_cost=1)
	S += T17_t3 >= 49
	T17_t3 += MAS[4]

	T9_t0 = S.Task('T9_t0', length=11, delay_cost=1)
	S += T9_t0 >= 49
	T9_t0 += MM[1]

	T9_t3_in = S.Task('T9_t3_in', length=1, delay_cost=1)
	S += T9_t3_in >= 49
	T9_t3_in += MAS_in[5]

	T9_t3_mem0 = S.Task('T9_t3_mem0', length=1, delay_cost=1)
	S += T9_t3_mem0 >= 49
	T9_t3_mem0 += MAS_MEM[10]

	T9_t3_mem1 = S.Task('T9_t3_mem1', length=1, delay_cost=1)
	S += T9_t3_mem1 >= 49
	T9_t3_mem1 += MAS_MEM[1]

	T131 = S.Task('T131', length=4, delay_cost=1)
	S += T131 >= 50
	T131 += MAS[3]

	T14_t0 = S.Task('T14_t0', length=11, delay_cost=1)
	S += T14_t0 >= 50
	T14_t0 += MM[0]

	T9_t3 = S.Task('T9_t3', length=4, delay_cost=1)
	S += T9_t3 >= 50
	T9_t3 += MAS[5]

	T8_t4_in = S.Task('T8_t4_in', length=1, delay_cost=1)
	S += T8_t4_in >= 51
	T8_t4_in += MM_in[0]

	T8_t4_mem0 = S.Task('T8_t4_mem0', length=1, delay_cost=1)
	S += T8_t4_mem0 >= 51
	T8_t4_mem0 += MAS_MEM[8]

	T8_t4_mem1 = S.Task('T8_t4_mem1', length=1, delay_cost=1)
	S += T8_t4_mem1 >= 51
	T8_t4_mem1 += MAS_MEM[5]

	T24_t3_in = S.Task('T24_t3_in', length=1, delay_cost=1)
	S += T24_t3_in >= 52
	T24_t3_in += MAS_in[4]

	T24_t3_mem0 = S.Task('T24_t3_mem0', length=1, delay_cost=1)
	S += T24_t3_mem0 >= 52
	T24_t3_mem0 += MAS_MEM[10]

	T24_t3_mem1 = S.Task('T24_t3_mem1', length=1, delay_cost=1)
	S += T24_t3_mem1 >= 52
	T24_t3_mem1 += MAS_MEM[5]

	T8_t4 = S.Task('T8_t4', length=11, delay_cost=1)
	S += T8_t4 >= 52
	T8_t4 += MM[0]

	T14_t1_in = S.Task('T14_t1_in', length=1, delay_cost=1)
	S += T14_t1_in >= 53
	T14_t1_in += MM_in[0]

	T14_t1_mem0 = S.Task('T14_t1_mem0', length=1, delay_cost=1)
	S += T14_t1_mem0 >= 53
	T14_t1_mem0 += MAS_MEM[6]

	T14_t1_mem1 = S.Task('T14_t1_mem1', length=1, delay_cost=1)
	S += T14_t1_mem1 >= 53
	T14_t1_mem1 += MAS_MEM[7]

	T24_t3 = S.Task('T24_t3', length=4, delay_cost=1)
	S += T24_t3 >= 53
	T24_t3 += MAS[4]

	T9_t4_in = S.Task('T9_t4_in', length=1, delay_cost=1)
	S += T9_t4_in >= 53
	T9_t4_in += MM_in[1]

	T9_t4_mem0 = S.Task('T9_t4_mem0', length=1, delay_cost=1)
	S += T9_t4_mem0 >= 53
	T9_t4_mem0 += MAS_MEM[2]

	T9_t4_mem1 = S.Task('T9_t4_mem1', length=1, delay_cost=1)
	S += T9_t4_mem1 >= 53
	T9_t4_mem1 += MAS_MEM[11]

	T14_t1 = S.Task('T14_t1', length=11, delay_cost=1)
	S += T14_t1 >= 54
	T14_t1 += MM[0]

	T14_t3_in = S.Task('T14_t3_in', length=1, delay_cost=1)
	S += T14_t3_in >= 54
	T14_t3_in += MAS_in[2]

	T14_t3_mem0 = S.Task('T14_t3_mem0', length=1, delay_cost=1)
	S += T14_t3_mem0 >= 54
	T14_t3_mem0 += MAS_MEM[2]

	T14_t3_mem1 = S.Task('T14_t3_mem1', length=1, delay_cost=1)
	S += T14_t3_mem1 >= 54
	T14_t3_mem1 += MAS_MEM[7]

	T9_t4 = S.Task('T9_t4', length=11, delay_cost=1)
	S += T9_t4 >= 54
	T9_t4 += MM[1]

	T10_t5_in = S.Task('T10_t5_in', length=1, delay_cost=1)
	S += T10_t5_in >= 55
	T10_t5_in += MAS_in[0]

	T10_t5_mem0 = S.Task('T10_t5_mem0', length=1, delay_cost=1)
	S += T10_t5_mem0 >= 55
	T10_t5_mem0 += MM_MEM[2]

	T10_t5_mem1 = S.Task('T10_t5_mem1', length=1, delay_cost=1)
	S += T10_t5_mem1 >= 55
	T10_t5_mem1 += MM_MEM[3]

	T14_t2_in = S.Task('T14_t2_in', length=1, delay_cost=1)
	S += T14_t2_in >= 55
	T14_t2_in += MAS_in[2]

	T14_t2_mem0 = S.Task('T14_t2_mem0', length=1, delay_cost=1)
	S += T14_t2_mem0 >= 55
	T14_t2_mem0 += MAS_MEM[2]

	T14_t2_mem1 = S.Task('T14_t2_mem1', length=1, delay_cost=1)
	S += T14_t2_mem1 >= 55
	T14_t2_mem1 += MAS_MEM[7]

	T14_t3 = S.Task('T14_t3', length=4, delay_cost=1)
	S += T14_t3 >= 55
	T14_t3 += MAS[2]

	T10_t5 = S.Task('T10_t5', length=4, delay_cost=1)
	S += T10_t5 >= 56
	T10_t5 += MAS[0]

	T11_t5_in = S.Task('T11_t5_in', length=1, delay_cost=1)
	S += T11_t5_in >= 56
	T11_t5_in += MAS_in[2]

	T11_t5_mem0 = S.Task('T11_t5_mem0', length=1, delay_cost=1)
	S += T11_t5_mem0 >= 56
	T11_t5_mem0 += MM_MEM[2]

	T11_t5_mem1 = S.Task('T11_t5_mem1', length=1, delay_cost=1)
	S += T11_t5_mem1 >= 56
	T11_t5_mem1 += MM_MEM[1]

	T14_t2 = S.Task('T14_t2', length=4, delay_cost=1)
	S += T14_t2 >= 56
	T14_t2 += MAS[2]

	T110_in = S.Task('T110_in', length=1, delay_cost=1)
	S += T110_in >= 57
	T110_in += MAS_in[1]

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	S += T110_mem0 >= 57
	T110_mem0 += MM_MEM[2]

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	S += T110_mem1 >= 57
	T110_mem1 += MM_MEM[1]

	T11_t5 = S.Task('T11_t5', length=4, delay_cost=1)
	S += T11_t5 >= 57
	T11_t5 += MAS[2]

	T110 = S.Task('T110', length=4, delay_cost=1)
	S += T110 >= 58
	T110 += MAS[1]

	T8_t5_in = S.Task('T8_t5_in', length=1, delay_cost=1)
	S += T8_t5_in >= 58
	T8_t5_in += MAS_in[0]

	T8_t5_mem0 = S.Task('T8_t5_mem0', length=1, delay_cost=1)
	S += T8_t5_mem0 >= 58
	T8_t5_mem0 += MM_MEM[2]

	T8_t5_mem1 = S.Task('T8_t5_mem1', length=1, delay_cost=1)
	S += T8_t5_mem1 >= 58
	T8_t5_mem1 += MM_MEM[3]

	T101_in = S.Task('T101_in', length=1, delay_cost=1)
	S += T101_in >= 59
	T101_in += MAS_in[1]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 59
	T101_mem0 += MM_MEM[0]

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 59
	T101_mem1 += MAS_MEM[1]

	T14_t4_in = S.Task('T14_t4_in', length=1, delay_cost=1)
	S += T14_t4_in >= 59
	T14_t4_in += MM_in[1]

	T14_t4_mem0 = S.Task('T14_t4_mem0', length=1, delay_cost=1)
	S += T14_t4_mem0 >= 59
	T14_t4_mem0 += MAS_MEM[4]

	T14_t4_mem1 = S.Task('T14_t4_mem1', length=1, delay_cost=1)
	S += T14_t4_mem1 >= 59
	T14_t4_mem1 += MAS_MEM[5]

	T8_t5 = S.Task('T8_t5', length=4, delay_cost=1)
	S += T8_t5 >= 59
	T8_t5 += MAS[0]

	T90_in = S.Task('T90_in', length=1, delay_cost=1)
	S += T90_in >= 59
	T90_in += MAS_in[3]

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	S += T90_mem0 >= 59
	T90_mem0 += MM_MEM[2]

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	S += T90_mem1 >= 59
	T90_mem1 += MM_MEM[3]

	T101 = S.Task('T101', length=4, delay_cost=1)
	S += T101 >= 60
	T101 += MAS[1]

	T111_in = S.Task('T111_in', length=1, delay_cost=1)
	S += T111_in >= 60
	T111_in += MAS_in[5]

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	S += T111_mem0 >= 60
	T111_mem0 += MM_MEM[0]

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	S += T111_mem1 >= 60
	T111_mem1 += MAS_MEM[5]

	T14_t4 = S.Task('T14_t4', length=11, delay_cost=1)
	S += T14_t4 >= 60
	T14_t4 += MM[1]

	T90 = S.Task('T90', length=4, delay_cost=1)
	S += T90 >= 60
	T90 += MAS[3]

	T9_t5_in = S.Task('T9_t5_in', length=1, delay_cost=1)
	S += T9_t5_in >= 60
	T9_t5_in += MAS_in[4]

	T9_t5_mem0 = S.Task('T9_t5_mem0', length=1, delay_cost=1)
	S += T9_t5_mem0 >= 60
	T9_t5_mem0 += MM_MEM[2]

	T9_t5_mem1 = S.Task('T9_t5_mem1', length=1, delay_cost=1)
	S += T9_t5_mem1 >= 60
	T9_t5_mem1 += MM_MEM[3]

	T111 = S.Task('T111', length=4, delay_cost=1)
	S += T111 >= 61
	T111 += MAS[5]

	T24_t0_in = S.Task('T24_t0_in', length=1, delay_cost=1)
	S += T24_t0_in >= 61
	T24_t0_in += MM_in[0]

	T24_t0_mem0 = S.Task('T24_t0_mem0', length=1, delay_cost=1)
	S += T24_t0_mem0 >= 61
	T24_t0_mem0 += MAS_MEM[2]

	T24_t0_mem1 = S.Task('T24_t0_mem1', length=1, delay_cost=1)
	S += T24_t0_mem1 >= 61
	T24_t0_mem1 += MAS_MEM[11]

	T80_in = S.Task('T80_in', length=1, delay_cost=1)
	S += T80_in >= 61
	T80_in += MAS_in[1]

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	S += T80_mem0 >= 61
	T80_mem0 += MM_MEM[2]

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	S += T80_mem1 >= 61
	T80_mem1 += MM_MEM[3]

	T9_t5 = S.Task('T9_t5', length=4, delay_cost=1)
	S += T9_t5 >= 61
	T9_t5 += MAS[4]

	T100_in = S.Task('T100_in', length=1, delay_cost=1)
	S += T100_in >= 62
	T100_in += MAS_in[1]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 62
	T100_mem0 += MM_MEM[2]

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 62
	T100_mem1 += MM_MEM[3]

	T24_t0 = S.Task('T24_t0', length=11, delay_cost=1)
	S += T24_t0 >= 62
	T24_t0 += MM[0]

	T80 = S.Task('T80', length=4, delay_cost=1)
	S += T80 >= 62
	T80 += MAS[1]

	T81_in = S.Task('T81_in', length=1, delay_cost=1)
	S += T81_in >= 62
	T81_in += MAS_in[5]

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	S += T81_mem0 >= 62
	T81_mem0 += MM_MEM[0]

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	S += T81_mem1 >= 62
	T81_mem1 += MAS_MEM[1]

	T100 = S.Task('T100', length=4, delay_cost=1)
	S += T100 >= 63
	T100 += MAS[1]

	T180_in = S.Task('T180_in', length=1, delay_cost=1)
	S += T180_in >= 63
	T180_in += MAS_in[0]

	T180_mem0 = S.Task('T180_mem0', length=1, delay_cost=1)
	S += T180_mem0 >= 63
	T180_mem0 += MAS_MEM[8]

	T180_mem1 = S.Task('T180_mem1', length=1, delay_cost=1)
	S += T180_mem1 >= 63
	T180_mem1 += MAS_MEM[7]

	T81 = S.Task('T81', length=4, delay_cost=1)
	S += T81 >= 63
	T81 += MAS[5]

	T140_in = S.Task('T140_in', length=1, delay_cost=1)
	S += T140_in >= 64
	T140_in += MAS_in[0]

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 64
	T140_mem0 += MM_MEM[0]

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 64
	T140_mem1 += MM_MEM[1]

	T180 = S.Task('T180', length=4, delay_cost=1)
	S += T180 >= 64
	T180 += MAS[0]

	T211_in = S.Task('T211_in', length=1, delay_cost=1)
	S += T211_in >= 64
	T211_in += MAS_in[2]

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	S += T211_mem0 >= 64
	T211_mem0 += MAS_MEM[8]

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	S += T211_mem1 >= 64
	T211_mem1 += MAS_MEM[3]

	T24_t1_in = S.Task('T24_t1_in', length=1, delay_cost=1)
	S += T24_t1_in >= 64
	T24_t1_in += MM_in[1]

	T24_t1_mem0 = S.Task('T24_t1_mem0', length=1, delay_cost=1)
	S += T24_t1_mem0 >= 64
	T24_t1_mem0 += MAS_MEM[10]

	T24_t1_mem1 = S.Task('T24_t1_mem1', length=1, delay_cost=1)
	S += T24_t1_mem1 >= 64
	T24_t1_mem1 += MAS_MEM[5]

	T24_t2_in = S.Task('T24_t2_in', length=1, delay_cost=1)
	S += T24_t2_in >= 64
	T24_t2_in += MAS_in[1]

	T24_t2_mem0 = S.Task('T24_t2_mem0', length=1, delay_cost=1)
	S += T24_t2_mem0 >= 64
	T24_t2_mem0 += MAS_MEM[2]

	T24_t2_mem1 = S.Task('T24_t2_mem1', length=1, delay_cost=1)
	S += T24_t2_mem1 >= 64
	T24_t2_mem1 += MAS_MEM[11]

	T91_in = S.Task('T91_in', length=1, delay_cost=1)
	S += T91_in >= 64
	T91_in += MAS_in[3]

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	S += T91_mem0 >= 64
	T91_mem0 += MM_MEM[2]

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	S += T91_mem1 >= 64
	T91_mem1 += MAS_MEM[9]

	T140 = S.Task('T140', length=4, delay_cost=1)
	S += T140 >= 65
	T140 += MAS[0]

	T14_t5_in = S.Task('T14_t5_in', length=1, delay_cost=1)
	S += T14_t5_in >= 65
	T14_t5_in += MAS_in[4]

	T14_t5_mem0 = S.Task('T14_t5_mem0', length=1, delay_cost=1)
	S += T14_t5_mem0 >= 65
	T14_t5_mem0 += MM_MEM[0]

	T14_t5_mem1 = S.Task('T14_t5_mem1', length=1, delay_cost=1)
	S += T14_t5_mem1 >= 65
	T14_t5_mem1 += MM_MEM[1]

	T16_t0_in = S.Task('T16_t0_in', length=1, delay_cost=1)
	S += T16_t0_in >= 65
	T16_t0_in += MM_in[1]

	T16_t0_mem0 = S.Task('T16_t0_mem0', length=1, delay_cost=1)
	S += T16_t0_mem0 >= 65
	T16_t0_mem0 += MAS_MEM[10]

	T16_t0_mem1 = S.Task('T16_t0_mem1', length=1, delay_cost=1)
	S += T16_t0_mem1 >= 65
	T16_t0_mem1 += MAS_MEM[3]

	T17_t0_in = S.Task('T17_t0_in', length=1, delay_cost=1)
	S += T17_t0_in >= 65
	T17_t0_in += MM_in[0]

	T17_t0_mem0 = S.Task('T17_t0_mem0', length=1, delay_cost=1)
	S += T17_t0_mem0 >= 65
	T17_t0_mem0 += MAS_MEM[2]

	T17_t0_mem1 = S.Task('T17_t0_mem1', length=1, delay_cost=1)
	S += T17_t0_mem1 >= 65
	T17_t0_mem1 += MAS_MEM[9]

	T190_in = S.Task('T190_in', length=1, delay_cost=1)
	S += T190_in >= 65
	T190_in += MAS_in[0]

	T190_mem0 = S.Task('T190_mem0', length=1, delay_cost=1)
	S += T190_mem0 >= 65
	T190_mem0 += MAS_MEM[8]

	T190_mem1 = S.Task('T190_mem1', length=1, delay_cost=1)
	S += T190_mem1 >= 65
	T190_mem1 += MAS_MEM[7]

	T211 = S.Task('T211', length=4, delay_cost=1)
	S += T211 >= 65
	T211 += MAS[2]

	T24_t1 = S.Task('T24_t1', length=11, delay_cost=1)
	S += T24_t1 >= 65
	T24_t1 += MM[1]

	T24_t2 = S.Task('T24_t2', length=4, delay_cost=1)
	S += T24_t2 >= 65
	T24_t2 += MAS[1]

	T91 = S.Task('T91', length=4, delay_cost=1)
	S += T91 >= 65
	T91 += MAS[3]

	T14_t5 = S.Task('T14_t5', length=4, delay_cost=1)
	S += T14_t5 >= 66
	T14_t5 += MAS[4]

	T16_t0 = S.Task('T16_t0', length=11, delay_cost=1)
	S += T16_t0 >= 66
	T16_t0 += MM[1]

	T17_t0 = S.Task('T17_t0', length=11, delay_cost=1)
	S += T17_t0 >= 66
	T17_t0 += MM[0]

	T17_t1_in = S.Task('T17_t1_in', length=1, delay_cost=1)
	S += T17_t1_in >= 66
	T17_t1_in += MM_in[1]

	T17_t1_mem0 = S.Task('T17_t1_mem0', length=1, delay_cost=1)
	S += T17_t1_mem0 >= 66
	T17_t1_mem0 += MAS_MEM[10]

	T17_t1_mem1 = S.Task('T17_t1_mem1', length=1, delay_cost=1)
	S += T17_t1_mem1 >= 66
	T17_t1_mem1 += MAS_MEM[5]

	T17_t2_in = S.Task('T17_t2_in', length=1, delay_cost=1)
	S += T17_t2_in >= 66
	T17_t2_in += MAS_in[2]

	T17_t2_mem0 = S.Task('T17_t2_mem0', length=1, delay_cost=1)
	S += T17_t2_mem0 >= 66
	T17_t2_mem0 += MAS_MEM[2]

	T17_t2_mem1 = S.Task('T17_t2_mem1', length=1, delay_cost=1)
	S += T17_t2_mem1 >= 66
	T17_t2_mem1 += MAS_MEM[11]

	T190 = S.Task('T190', length=4, delay_cost=1)
	S += T190 >= 66
	T190 += MAS[0]

	T210_in = S.Task('T210_in', length=1, delay_cost=1)
	S += T210_in >= 66
	T210_in += MAS_in[0]

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	S += T210_mem0 >= 66
	T210_mem0 += MAS_MEM[8]

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	S += T210_mem1 >= 66
	T210_mem1 += MAS_MEM[3]

	T16_t3_in = S.Task('T16_t3_in', length=1, delay_cost=1)
	S += T16_t3_in >= 67
	T16_t3_in += MAS_in[1]

	T16_t3_mem0 = S.Task('T16_t3_mem0', length=1, delay_cost=1)
	S += T16_t3_mem0 >= 67
	T16_t3_mem0 += MAS_MEM[2]

	T16_t3_mem1 = S.Task('T16_t3_mem1', length=1, delay_cost=1)
	S += T16_t3_mem1 >= 67
	T16_t3_mem1 += MAS_MEM[11]

	T17_t1 = S.Task('T17_t1', length=11, delay_cost=1)
	S += T17_t1 >= 67
	T17_t1 += MM[1]

	T17_t2 = S.Task('T17_t2', length=4, delay_cost=1)
	S += T17_t2 >= 67
	T17_t2 += MAS[2]

	T20_t0_in = S.Task('T20_t0_in', length=1, delay_cost=1)
	S += T20_t0_in >= 67
	T20_t0_in += MM_in[1]

	T20_t0_mem0 = S.Task('T20_t0_mem0', length=1, delay_cost=1)
	S += T20_t0_mem0 >= 67
	T20_t0_mem0 += MAS_MEM[8]

	T20_t0_mem1 = S.Task('T20_t0_mem1', length=1, delay_cost=1)
	S += T20_t0_mem1 >= 67
	T20_t0_mem1 += MAS_MEM[1]

	T210 = S.Task('T210', length=4, delay_cost=1)
	S += T210 >= 67
	T210 += MAS[0]

	T16_t1_in = S.Task('T16_t1_in', length=1, delay_cost=1)
	S += T16_t1_in >= 68
	T16_t1_in += MM_in[1]

	T16_t1_mem0 = S.Task('T16_t1_mem0', length=1, delay_cost=1)
	S += T16_t1_mem0 >= 68
	T16_t1_mem0 += MAS_MEM[0]

	T16_t1_mem1 = S.Task('T16_t1_mem1', length=1, delay_cost=1)
	S += T16_t1_mem1 >= 68
	T16_t1_mem1 += MAS_MEM[11]

	T16_t3 = S.Task('T16_t3', length=4, delay_cost=1)
	S += T16_t3 >= 68
	T16_t3 += MAS[1]

	T181_in = S.Task('T181_in', length=1, delay_cost=1)
	S += T181_in >= 68
	T181_in += MAS_in[2]

	T181_mem0 = S.Task('T181_mem0', length=1, delay_cost=1)
	S += T181_mem0 >= 68
	T181_mem0 += MAS_MEM[8]

	T181_mem1 = S.Task('T181_mem1', length=1, delay_cost=1)
	S += T181_mem1 >= 68
	T181_mem1 += MAS_MEM[7]

	T20_t0 = S.Task('T20_t0', length=11, delay_cost=1)
	S += T20_t0 >= 68
	T20_t0 += MM[1]

	Z3_t0_in = S.Task('Z3_t0_in', length=1, delay_cost=1)
	S += Z3_t0_in >= 68
	Z3_t0_in += MM_in[0]

	Z3_t0_mem0 = S.Task('Z3_t0_mem0', length=1, delay_cost=1)
	S += Z3_t0_mem0 >= 68
	Z3_t0_mem0 += MAIN_MEM_r[0]

	Z3_t0_mem1 = S.Task('Z3_t0_mem1', length=1, delay_cost=1)
	S += Z3_t0_mem1 >= 68
	Z3_t0_mem1 += MAS_MEM[1]

	T16_t1 = S.Task('T16_t1', length=11, delay_cost=1)
	S += T16_t1 >= 69
	T16_t1 += MM[1]

	T181 = S.Task('T181', length=4, delay_cost=1)
	S += T181 >= 69
	T181 += MAS[2]

	T191_in = S.Task('T191_in', length=1, delay_cost=1)
	S += T191_in >= 69
	T191_in += MAS_in[0]

	T191_mem0 = S.Task('T191_mem0', length=1, delay_cost=1)
	S += T191_mem0 >= 69
	T191_mem0 += MAS_MEM[8]

	T191_mem1 = S.Task('T191_mem1', length=1, delay_cost=1)
	S += T191_mem1 >= 69
	T191_mem1 += MAS_MEM[7]

	Z3_t0 = S.Task('Z3_t0', length=11, delay_cost=1)
	S += Z3_t0 >= 69
	Z3_t0 += MM[0]

	T141_in = S.Task('T141_in', length=1, delay_cost=1)
	S += T141_in >= 70
	T141_in += MAS_in[2]

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 70
	T141_mem0 += MM_MEM[2]

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 70
	T141_mem1 += MAS_MEM[9]

	T191 = S.Task('T191', length=4, delay_cost=1)
	S += T191 >= 70
	T191 += MAS[0]

	T141 = S.Task('T141', length=4, delay_cost=1)
	S += T141 >= 71
	T141 += MAS[2]


	# new tasks
	T16_t4 = S.Task('T16_t4', length=11, delay_cost=1)
	T16_t4 += alt(MM)
	T16_t4_in = S.Task('T16_t4_in', length=1, delay_cost=1)
	T16_t4_in += alt(MM_in)
	S += T16_t4_in*MM_in[0]<=T16_t4*MM[0]
	S += T16_t4_in*MM_in[1]<=T16_t4*MM[1]
	T16_t4_mem0 = S.Task('T16_t4_mem0', length=1, delay_cost=1)
	T16_t4_mem0 += MAS_MEM[10]
	S += 52 < T16_t4_mem0
	S += T16_t4_mem0 <= T16_t4

	T16_t4_mem1 = S.Task('T16_t4_mem1', length=1, delay_cost=1)
	T16_t4_mem1 += MAS_MEM[3]
	S += 71 < T16_t4_mem1
	S += T16_t4_mem1 <= T16_t4

	T160 = S.Task('T160', length=4, delay_cost=1)
	T160 += alt(MAS)
	T160_in = S.Task('T160_in', length=1, delay_cost=1)
	T160_in += alt(MAS_in)
	S += T160_in*MAS_in[0]<=T160*MAS[0]

	S += T160_in*MAS_in[1]<=T160*MAS[1]

	S += T160_in*MAS_in[2]<=T160*MAS[2]

	S += T160_in*MAS_in[3]<=T160*MAS[3]

	S += T160_in*MAS_in[4]<=T160*MAS[4]

	S += T160_in*MAS_in[5]<=T160*MAS[5]

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	T160_mem0 += MM_MEM[2]
	S += 76 < T160_mem0
	S += T160_mem0 <= T160

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	T160_mem1 += MM_MEM[3]
	S += 79 < T160_mem1
	S += T160_mem1 <= T160

	T16_t5 = S.Task('T16_t5', length=4, delay_cost=1)
	T16_t5 += alt(MAS)
	T16_t5_in = S.Task('T16_t5_in', length=1, delay_cost=1)
	T16_t5_in += alt(MAS_in)
	S += T16_t5_in*MAS_in[0]<=T16_t5*MAS[0]

	S += T16_t5_in*MAS_in[1]<=T16_t5*MAS[1]

	S += T16_t5_in*MAS_in[2]<=T16_t5*MAS[2]

	S += T16_t5_in*MAS_in[3]<=T16_t5*MAS[3]

	S += T16_t5_in*MAS_in[4]<=T16_t5*MAS[4]

	S += T16_t5_in*MAS_in[5]<=T16_t5*MAS[5]

	T16_t5_mem0 = S.Task('T16_t5_mem0', length=1, delay_cost=1)
	T16_t5_mem0 += MM_MEM[2]
	S += 76 < T16_t5_mem0
	S += T16_t5_mem0 <= T16_t5

	T16_t5_mem1 = S.Task('T16_t5_mem1', length=1, delay_cost=1)
	T16_t5_mem1 += MM_MEM[3]
	S += 79 < T16_t5_mem1
	S += T16_t5_mem1 <= T16_t5

	T17_t4 = S.Task('T17_t4', length=11, delay_cost=1)
	T17_t4 += alt(MM)
	T17_t4_in = S.Task('T17_t4_in', length=1, delay_cost=1)
	T17_t4_in += alt(MM_in)
	S += T17_t4_in*MM_in[0]<=T17_t4*MM[0]
	S += T17_t4_in*MM_in[1]<=T17_t4*MM[1]
	T17_t4_mem0 = S.Task('T17_t4_mem0', length=1, delay_cost=1)
	T17_t4_mem0 += MAS_MEM[4]
	S += 70 < T17_t4_mem0
	S += T17_t4_mem0 <= T17_t4

	T17_t4_mem1 = S.Task('T17_t4_mem1', length=1, delay_cost=1)
	T17_t4_mem1 += MAS_MEM[9]
	S += 52 < T17_t4_mem1
	S += T17_t4_mem1 <= T17_t4

	T170 = S.Task('T170', length=4, delay_cost=1)
	T170 += alt(MAS)
	T170_in = S.Task('T170_in', length=1, delay_cost=1)
	T170_in += alt(MAS_in)
	S += T170_in*MAS_in[0]<=T170*MAS[0]

	S += T170_in*MAS_in[1]<=T170*MAS[1]

	S += T170_in*MAS_in[2]<=T170*MAS[2]

	S += T170_in*MAS_in[3]<=T170*MAS[3]

	S += T170_in*MAS_in[4]<=T170*MAS[4]

	S += T170_in*MAS_in[5]<=T170*MAS[5]

	T170_mem0 = S.Task('T170_mem0', length=1, delay_cost=1)
	T170_mem0 += MM_MEM[0]
	S += 76 < T170_mem0
	S += T170_mem0 <= T170

	T170_mem1 = S.Task('T170_mem1', length=1, delay_cost=1)
	T170_mem1 += MM_MEM[3]
	S += 77 < T170_mem1
	S += T170_mem1 <= T170

	T17_t5 = S.Task('T17_t5', length=4, delay_cost=1)
	T17_t5 += alt(MAS)
	T17_t5_in = S.Task('T17_t5_in', length=1, delay_cost=1)
	T17_t5_in += alt(MAS_in)
	S += T17_t5_in*MAS_in[0]<=T17_t5*MAS[0]

	S += T17_t5_in*MAS_in[1]<=T17_t5*MAS[1]

	S += T17_t5_in*MAS_in[2]<=T17_t5*MAS[2]

	S += T17_t5_in*MAS_in[3]<=T17_t5*MAS[3]

	S += T17_t5_in*MAS_in[4]<=T17_t5*MAS[4]

	S += T17_t5_in*MAS_in[5]<=T17_t5*MAS[5]

	T17_t5_mem0 = S.Task('T17_t5_mem0', length=1, delay_cost=1)
	T17_t5_mem0 += MM_MEM[0]
	S += 76 < T17_t5_mem0
	S += T17_t5_mem0 <= T17_t5

	T17_t5_mem1 = S.Task('T17_t5_mem1', length=1, delay_cost=1)
	T17_t5_mem1 += MM_MEM[3]
	S += 77 < T17_t5_mem1
	S += T17_t5_mem1 <= T17_t5

	T20_t1 = S.Task('T20_t1', length=11, delay_cost=1)
	T20_t1 += alt(MM)
	T20_t1_in = S.Task('T20_t1_in', length=1, delay_cost=1)
	T20_t1_in += alt(MM_in)
	S += T20_t1_in*MM_in[0]<=T20_t1*MM[0]
	S += T20_t1_in*MM_in[1]<=T20_t1*MM[1]
	T20_t1_mem0 = S.Task('T20_t1_mem0', length=1, delay_cost=1)
	T20_t1_mem0 += MAS_MEM[8]
	S += 21 < T20_t1_mem0
	S += T20_t1_mem0 <= T20_t1

	T20_t1_mem1 = S.Task('T20_t1_mem1', length=1, delay_cost=1)
	T20_t1_mem1 += MAS_MEM[5]
	S += 72 < T20_t1_mem1
	S += T20_t1_mem1 <= T20_t1

	T20_t3 = S.Task('T20_t3', length=4, delay_cost=1)
	T20_t3 += alt(MAS)
	T20_t3_in = S.Task('T20_t3_in', length=1, delay_cost=1)
	T20_t3_in += alt(MAS_in)
	S += T20_t3_in*MAS_in[0]<=T20_t3*MAS[0]

	S += T20_t3_in*MAS_in[1]<=T20_t3*MAS[1]

	S += T20_t3_in*MAS_in[2]<=T20_t3*MAS[2]

	S += T20_t3_in*MAS_in[3]<=T20_t3*MAS[3]

	S += T20_t3_in*MAS_in[4]<=T20_t3*MAS[4]

	S += T20_t3_in*MAS_in[5]<=T20_t3*MAS[5]

	T20_t3_mem0 = S.Task('T20_t3_mem0', length=1, delay_cost=1)
	T20_t3_mem0 += MAS_MEM[0]
	S += 67 < T20_t3_mem0
	S += T20_t3_mem0 <= T20_t3

	T20_t3_mem1 = S.Task('T20_t3_mem1', length=1, delay_cost=1)
	T20_t3_mem1 += MAS_MEM[5]
	S += 72 < T20_t3_mem1
	S += T20_t3_mem1 <= T20_t3

	T22_t0 = S.Task('T22_t0', length=4, delay_cost=1)
	T22_t0 += alt(MAS)
	T22_t0_in = S.Task('T22_t0_in', length=1, delay_cost=1)
	T22_t0_in += alt(MAS_in)
	S += T22_t0_in*MAS_in[0]<=T22_t0*MAS[0]

	S += T22_t0_in*MAS_in[1]<=T22_t0*MAS[1]

	S += T22_t0_in*MAS_in[2]<=T22_t0*MAS[2]

	S += T22_t0_in*MAS_in[3]<=T22_t0*MAS[3]

	S += T22_t0_in*MAS_in[4]<=T22_t0*MAS[4]

	S += T22_t0_in*MAS_in[5]<=T22_t0*MAS[5]

	T22_t0_mem0 = S.Task('T22_t0_mem0', length=1, delay_cost=1)
	T22_t0_mem0 += MAS_MEM[0]
	S += 70 < T22_t0_mem0
	S += T22_t0_mem0 <= T22_t0

	T22_t0_mem1 = S.Task('T22_t0_mem1', length=1, delay_cost=1)
	T22_t0_mem1 += MAS_MEM[5]
	S += 68 < T22_t0_mem1
	S += T22_t0_mem1 <= T22_t0

	T22_t1 = S.Task('T22_t1', length=4, delay_cost=1)
	T22_t1 += alt(MAS)
	T22_t1_in = S.Task('T22_t1_in', length=1, delay_cost=1)
	T22_t1_in += alt(MAS_in)
	S += T22_t1_in*MAS_in[0]<=T22_t1*MAS[0]

	S += T22_t1_in*MAS_in[1]<=T22_t1*MAS[1]

	S += T22_t1_in*MAS_in[2]<=T22_t1*MAS[2]

	S += T22_t1_in*MAS_in[3]<=T22_t1*MAS[3]

	S += T22_t1_in*MAS_in[4]<=T22_t1*MAS[4]

	S += T22_t1_in*MAS_in[5]<=T22_t1*MAS[5]

	T22_t1_mem0 = S.Task('T22_t1_mem0', length=1, delay_cost=1)
	T22_t1_mem0 += MAS_MEM[0]
	S += 70 < T22_t1_mem0
	S += T22_t1_mem0 <= T22_t1

	T22_t1_mem1 = S.Task('T22_t1_mem1', length=1, delay_cost=1)
	T22_t1_mem1 += MAS_MEM[5]
	S += 68 < T22_t1_mem1
	S += T22_t1_mem1 <= T22_t1

	T22_t3 = S.Task('T22_t3', length=11, delay_cost=1)
	T22_t3 += alt(MM)
	T22_t3_in = S.Task('T22_t3_in', length=1, delay_cost=1)
	T22_t3_in += alt(MM_in)
	S += T22_t3_in*MM_in[0]<=T22_t3*MM[0]
	S += T22_t3_in*MM_in[1]<=T22_t3*MM[1]
	T22_t3_mem0 = S.Task('T22_t3_mem0', length=1, delay_cost=1)
	T22_t3_mem0 += MAS_MEM[0]
	S += 70 < T22_t3_mem0
	S += T22_t3_mem0 <= T22_t3

	T22_t3_mem1 = S.Task('T22_t3_mem1', length=1, delay_cost=1)
	T22_t3_mem1 += MAS_MEM[5]
	S += 68 < T22_t3_mem1
	S += T22_t3_mem1 <= T22_t3

	T23_t0 = S.Task('T23_t0', length=4, delay_cost=1)
	T23_t0 += alt(MAS)
	T23_t0_in = S.Task('T23_t0_in', length=1, delay_cost=1)
	T23_t0_in += alt(MAS_in)
	S += T23_t0_in*MAS_in[0]<=T23_t0*MAS[0]

	S += T23_t0_in*MAS_in[1]<=T23_t0*MAS[1]

	S += T23_t0_in*MAS_in[2]<=T23_t0*MAS[2]

	S += T23_t0_in*MAS_in[3]<=T23_t0*MAS[3]

	S += T23_t0_in*MAS_in[4]<=T23_t0*MAS[4]

	S += T23_t0_in*MAS_in[5]<=T23_t0*MAS[5]

	T23_t0_mem0 = S.Task('T23_t0_mem0', length=1, delay_cost=1)
	T23_t0_mem0 += MAS_MEM[0]
	S += 69 < T23_t0_mem0
	S += T23_t0_mem0 <= T23_t0

	T23_t0_mem1 = S.Task('T23_t0_mem1', length=1, delay_cost=1)
	T23_t0_mem1 += MAS_MEM[1]
	S += 73 < T23_t0_mem1
	S += T23_t0_mem1 <= T23_t0

	T23_t1 = S.Task('T23_t1', length=4, delay_cost=1)
	T23_t1 += alt(MAS)
	T23_t1_in = S.Task('T23_t1_in', length=1, delay_cost=1)
	T23_t1_in += alt(MAS_in)
	S += T23_t1_in*MAS_in[0]<=T23_t1*MAS[0]

	S += T23_t1_in*MAS_in[1]<=T23_t1*MAS[1]

	S += T23_t1_in*MAS_in[2]<=T23_t1*MAS[2]

	S += T23_t1_in*MAS_in[3]<=T23_t1*MAS[3]

	S += T23_t1_in*MAS_in[4]<=T23_t1*MAS[4]

	S += T23_t1_in*MAS_in[5]<=T23_t1*MAS[5]

	T23_t1_mem0 = S.Task('T23_t1_mem0', length=1, delay_cost=1)
	T23_t1_mem0 += MAS_MEM[0]
	S += 69 < T23_t1_mem0
	S += T23_t1_mem0 <= T23_t1

	T23_t1_mem1 = S.Task('T23_t1_mem1', length=1, delay_cost=1)
	T23_t1_mem1 += MAS_MEM[1]
	S += 73 < T23_t1_mem1
	S += T23_t1_mem1 <= T23_t1

	T23_t3 = S.Task('T23_t3', length=11, delay_cost=1)
	T23_t3 += alt(MM)
	T23_t3_in = S.Task('T23_t3_in', length=1, delay_cost=1)
	T23_t3_in += alt(MM_in)
	S += T23_t3_in*MM_in[0]<=T23_t3*MM[0]
	S += T23_t3_in*MM_in[1]<=T23_t3*MM[1]
	T23_t3_mem0 = S.Task('T23_t3_mem0', length=1, delay_cost=1)
	T23_t3_mem0 += MAS_MEM[0]
	S += 69 < T23_t3_mem0
	S += T23_t3_mem0 <= T23_t3

	T23_t3_mem1 = S.Task('T23_t3_mem1', length=1, delay_cost=1)
	T23_t3_mem1 += MAS_MEM[1]
	S += 73 < T23_t3_mem1
	S += T23_t3_mem1 <= T23_t3

	T24_t4 = S.Task('T24_t4', length=11, delay_cost=1)
	T24_t4 += alt(MM)
	T24_t4_in = S.Task('T24_t4_in', length=1, delay_cost=1)
	T24_t4_in += alt(MM_in)
	S += T24_t4_in*MM_in[0]<=T24_t4*MM[0]
	S += T24_t4_in*MM_in[1]<=T24_t4*MM[1]
	T24_t4_mem0 = S.Task('T24_t4_mem0', length=1, delay_cost=1)
	T24_t4_mem0 += MAS_MEM[2]
	S += 68 < T24_t4_mem0
	S += T24_t4_mem0 <= T24_t4

	T24_t4_mem1 = S.Task('T24_t4_mem1', length=1, delay_cost=1)
	T24_t4_mem1 += MAS_MEM[9]
	S += 56 < T24_t4_mem1
	S += T24_t4_mem1 <= T24_t4

	T240 = S.Task('T240', length=4, delay_cost=1)
	T240 += alt(MAS)
	T240_in = S.Task('T240_in', length=1, delay_cost=1)
	T240_in += alt(MAS_in)
	S += T240_in*MAS_in[0]<=T240*MAS[0]

	S += T240_in*MAS_in[1]<=T240*MAS[1]

	S += T240_in*MAS_in[2]<=T240*MAS[2]

	S += T240_in*MAS_in[3]<=T240*MAS[3]

	S += T240_in*MAS_in[4]<=T240*MAS[4]

	S += T240_in*MAS_in[5]<=T240*MAS[5]

	T240_mem0 = S.Task('T240_mem0', length=1, delay_cost=1)
	T240_mem0 += MM_MEM[0]
	S += 72 < T240_mem0
	S += T240_mem0 <= T240

	T240_mem1 = S.Task('T240_mem1', length=1, delay_cost=1)
	T240_mem1 += MM_MEM[3]
	S += 75 < T240_mem1
	S += T240_mem1 <= T240

	T24_t5 = S.Task('T24_t5', length=4, delay_cost=1)
	T24_t5 += alt(MAS)
	T24_t5_in = S.Task('T24_t5_in', length=1, delay_cost=1)
	T24_t5_in += alt(MAS_in)
	S += T24_t5_in*MAS_in[0]<=T24_t5*MAS[0]

	S += T24_t5_in*MAS_in[1]<=T24_t5*MAS[1]

	S += T24_t5_in*MAS_in[2]<=T24_t5*MAS[2]

	S += T24_t5_in*MAS_in[3]<=T24_t5*MAS[3]

	S += T24_t5_in*MAS_in[4]<=T24_t5*MAS[4]

	S += T24_t5_in*MAS_in[5]<=T24_t5*MAS[5]

	T24_t5_mem0 = S.Task('T24_t5_mem0', length=1, delay_cost=1)
	T24_t5_mem0 += MM_MEM[0]
	S += 72 < T24_t5_mem0
	S += T24_t5_mem0 <= T24_t5

	T24_t5_mem1 = S.Task('T24_t5_mem1', length=1, delay_cost=1)
	T24_t5_mem1 += MM_MEM[3]
	S += 75 < T24_t5_mem1
	S += T24_t5_mem1 <= T24_t5

	Z3_t1 = S.Task('Z3_t1', length=11, delay_cost=1)
	Z3_t1 += alt(MM)
	Z3_t1_in = S.Task('Z3_t1_in', length=1, delay_cost=1)
	Z3_t1_in += alt(MM_in)
	S += Z3_t1_in*MM_in[0]<=Z3_t1*MM[0]
	S += Z3_t1_in*MM_in[1]<=Z3_t1*MM[1]
	Z3_t1_mem0 = S.Task('Z3_t1_mem0', length=1, delay_cost=1)
	Z3_t1_mem0 += MAIN_MEM_r[0]
	S += Z3_t1_mem0 <= Z3_t1

	Z3_t1_mem1 = S.Task('Z3_t1_mem1', length=1, delay_cost=1)
	Z3_t1_mem1 += MAS_MEM[5]
	S += 74 < Z3_t1_mem1
	S += Z3_t1_mem1 <= Z3_t1

	Z3_t3 = S.Task('Z3_t3', length=4, delay_cost=1)
	Z3_t3 += alt(MAS)
	Z3_t3_in = S.Task('Z3_t3_in', length=1, delay_cost=1)
	Z3_t3_in += alt(MAS_in)
	S += Z3_t3_in*MAS_in[0]<=Z3_t3*MAS[0]

	S += Z3_t3_in*MAS_in[1]<=Z3_t3*MAS[1]

	S += Z3_t3_in*MAS_in[2]<=Z3_t3*MAS[2]

	S += Z3_t3_in*MAS_in[3]<=Z3_t3*MAS[3]

	S += Z3_t3_in*MAS_in[4]<=Z3_t3*MAS[4]

	S += Z3_t3_in*MAS_in[5]<=Z3_t3*MAS[5]

	Z3_t3_mem0 = S.Task('Z3_t3_mem0', length=1, delay_cost=1)
	Z3_t3_mem0 += MAS_MEM[0]
	S += 68 < Z3_t3_mem0
	S += Z3_t3_mem0 <= Z3_t3

	Z3_t3_mem1 = S.Task('Z3_t3_mem1', length=1, delay_cost=1)
	Z3_t3_mem1 += MAS_MEM[5]
	S += 74 < Z3_t3_mem1
	S += Z3_t3_mem1 <= Z3_t3

	T161 = S.Task('T161', length=4, delay_cost=1)
	T161 += alt(MAS)
	T161_in = S.Task('T161_in', length=1, delay_cost=1)
	T161_in += alt(MAS_in)
	S += T161_in*MAS_in[0]<=T161*MAS[0]

	S += T161_in*MAS_in[1]<=T161*MAS[1]

	S += T161_in*MAS_in[2]<=T161*MAS[2]

	S += T161_in*MAS_in[3]<=T161*MAS[3]

	S += T161_in*MAS_in[4]<=T161*MAS[4]

	S += T161_in*MAS_in[5]<=T161*MAS[5]

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
	S += T161_mem1 <= T161

	T171 = S.Task('T171', length=4, delay_cost=1)
	T171 += alt(MAS)
	T171_in = S.Task('T171_in', length=1, delay_cost=1)
	T171_in += alt(MAS_in)
	S += T171_in*MAS_in[0]<=T171*MAS[0]

	S += T171_in*MAS_in[1]<=T171*MAS[1]

	S += T171_in*MAS_in[2]<=T171*MAS[2]

	S += T171_in*MAS_in[3]<=T171*MAS[3]

	S += T171_in*MAS_in[4]<=T171*MAS[4]

	S += T171_in*MAS_in[5]<=T171*MAS[5]

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
	S += T171_mem1 <= T171

	T20_t4 = S.Task('T20_t4', length=11, delay_cost=1)
	T20_t4 += alt(MM)
	T20_t4_in = S.Task('T20_t4_in', length=1, delay_cost=1)
	T20_t4_in += alt(MM_in)
	S += T20_t4_in*MM_in[0]<=T20_t4*MM[0]
	S += T20_t4_in*MM_in[1]<=T20_t4*MM[1]
	T20_t4_mem0 = S.Task('T20_t4_mem0', length=1, delay_cost=1)
	T20_t4_mem0 += MAS_MEM[4]
	S += 35 < T20_t4_mem0
	S += T20_t4_mem0 <= T20_t4

	T20_t4_mem1 = S.Task('T20_t4_mem1', length=1, delay_cost=1)
	T20_t4_mem1 += alt(MAS_MEM)
	S += (T20_t3*MAS[0])-1 < T20_t4_mem1*MAS_MEM[1]
	S += (T20_t3*MAS[1])-1 < T20_t4_mem1*MAS_MEM[3]
	S += (T20_t3*MAS[2])-1 < T20_t4_mem1*MAS_MEM[5]
	S += (T20_t3*MAS[3])-1 < T20_t4_mem1*MAS_MEM[7]
	S += (T20_t3*MAS[4])-1 < T20_t4_mem1*MAS_MEM[9]
	S += (T20_t3*MAS[5])-1 < T20_t4_mem1*MAS_MEM[11]
	S += T20_t4_mem1 <= T20_t4

	T200 = S.Task('T200', length=4, delay_cost=1)
	T200 += alt(MAS)
	T200_in = S.Task('T200_in', length=1, delay_cost=1)
	T200_in += alt(MAS_in)
	S += T200_in*MAS_in[0]<=T200*MAS[0]

	S += T200_in*MAS_in[1]<=T200*MAS[1]

	S += T200_in*MAS_in[2]<=T200*MAS[2]

	S += T200_in*MAS_in[3]<=T200*MAS[3]

	S += T200_in*MAS_in[4]<=T200*MAS[4]

	S += T200_in*MAS_in[5]<=T200*MAS[5]

	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	T200_mem0 += MM_MEM[2]
	S += 78 < T200_mem0
	S += T200_mem0 <= T200

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	T200_mem1 += alt(MM_MEM)
	S += (T20_t1*MM[0])-1 < T200_mem1*MM_MEM[1]
	S += (T20_t1*MM[1])-1 < T200_mem1*MM_MEM[3]
	S += T200_mem1 <= T200

	T20_t5 = S.Task('T20_t5', length=4, delay_cost=1)
	T20_t5 += alt(MAS)
	T20_t5_in = S.Task('T20_t5_in', length=1, delay_cost=1)
	T20_t5_in += alt(MAS_in)
	S += T20_t5_in*MAS_in[0]<=T20_t5*MAS[0]

	S += T20_t5_in*MAS_in[1]<=T20_t5*MAS[1]

	S += T20_t5_in*MAS_in[2]<=T20_t5*MAS[2]

	S += T20_t5_in*MAS_in[3]<=T20_t5*MAS[3]

	S += T20_t5_in*MAS_in[4]<=T20_t5*MAS[4]

	S += T20_t5_in*MAS_in[5]<=T20_t5*MAS[5]

	T20_t5_mem0 = S.Task('T20_t5_mem0', length=1, delay_cost=1)
	T20_t5_mem0 += MM_MEM[2]
	S += 78 < T20_t5_mem0
	S += T20_t5_mem0 <= T20_t5

	T20_t5_mem1 = S.Task('T20_t5_mem1', length=1, delay_cost=1)
	T20_t5_mem1 += alt(MM_MEM)
	S += (T20_t1*MM[0])-1 < T20_t5_mem1*MM_MEM[1]
	S += (T20_t1*MM[1])-1 < T20_t5_mem1*MM_MEM[3]
	S += T20_t5_mem1 <= T20_t5

	T22_t2 = S.Task('T22_t2', length=11, delay_cost=1)
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
	S += T22_t2_mem0 <= T22_t2

	T22_t2_mem1 = S.Task('T22_t2_mem1', length=1, delay_cost=1)
	T22_t2_mem1 += alt(MAS_MEM)
	S += (T22_t1*MAS[0])-1 < T22_t2_mem1*MAS_MEM[1]
	S += (T22_t1*MAS[1])-1 < T22_t2_mem1*MAS_MEM[3]
	S += (T22_t1*MAS[2])-1 < T22_t2_mem1*MAS_MEM[5]
	S += (T22_t1*MAS[3])-1 < T22_t2_mem1*MAS_MEM[7]
	S += (T22_t1*MAS[4])-1 < T22_t2_mem1*MAS_MEM[9]
	S += (T22_t1*MAS[5])-1 < T22_t2_mem1*MAS_MEM[11]
	S += T22_t2_mem1 <= T22_t2

	T22_t5 = S.Task('T22_t5', length=4, delay_cost=1)
	T22_t5 += alt(MAS)
	T22_t5_in = S.Task('T22_t5_in', length=1, delay_cost=1)
	T22_t5_in += alt(MAS_in)
	S += T22_t5_in*MAS_in[0]<=T22_t5*MAS[0]

	S += T22_t5_in*MAS_in[1]<=T22_t5*MAS[1]

	S += T22_t5_in*MAS_in[2]<=T22_t5*MAS[2]

	S += T22_t5_in*MAS_in[3]<=T22_t5*MAS[3]

	S += T22_t5_in*MAS_in[4]<=T22_t5*MAS[4]

	S += T22_t5_in*MAS_in[5]<=T22_t5*MAS[5]

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

	T221 = S.Task('T221', length=4, delay_cost=1)
	T221 += alt(MAS)
	T221_in = S.Task('T221_in', length=1, delay_cost=1)
	T221_in += alt(MAS_in)
	S += T221_in*MAS_in[0]<=T221*MAS[0]

	S += T221_in*MAS_in[1]<=T221*MAS[1]

	S += T221_in*MAS_in[2]<=T221*MAS[2]

	S += T221_in*MAS_in[3]<=T221*MAS[3]

	S += T221_in*MAS_in[4]<=T221*MAS[4]

	S += T221_in*MAS_in[5]<=T221*MAS[5]

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

	T23_t2 = S.Task('T23_t2', length=11, delay_cost=1)
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
	S += T23_t2_mem0 <= T23_t2

	T23_t2_mem1 = S.Task('T23_t2_mem1', length=1, delay_cost=1)
	T23_t2_mem1 += alt(MAS_MEM)
	S += (T23_t1*MAS[0])-1 < T23_t2_mem1*MAS_MEM[1]
	S += (T23_t1*MAS[1])-1 < T23_t2_mem1*MAS_MEM[3]
	S += (T23_t1*MAS[2])-1 < T23_t2_mem1*MAS_MEM[5]
	S += (T23_t1*MAS[3])-1 < T23_t2_mem1*MAS_MEM[7]
	S += (T23_t1*MAS[4])-1 < T23_t2_mem1*MAS_MEM[9]
	S += (T23_t1*MAS[5])-1 < T23_t2_mem1*MAS_MEM[11]
	S += T23_t2_mem1 <= T23_t2

	T23_t5 = S.Task('T23_t5', length=4, delay_cost=1)
	T23_t5 += alt(MAS)
	T23_t5_in = S.Task('T23_t5_in', length=1, delay_cost=1)
	T23_t5_in += alt(MAS_in)
	S += T23_t5_in*MAS_in[0]<=T23_t5*MAS[0]

	S += T23_t5_in*MAS_in[1]<=T23_t5*MAS[1]

	S += T23_t5_in*MAS_in[2]<=T23_t5*MAS[2]

	S += T23_t5_in*MAS_in[3]<=T23_t5*MAS[3]

	S += T23_t5_in*MAS_in[4]<=T23_t5*MAS[4]

	S += T23_t5_in*MAS_in[5]<=T23_t5*MAS[5]

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

	T231 = S.Task('T231', length=4, delay_cost=1)
	T231 += alt(MAS)
	T231_in = S.Task('T231_in', length=1, delay_cost=1)
	T231_in += alt(MAS_in)
	S += T231_in*MAS_in[0]<=T231*MAS[0]

	S += T231_in*MAS_in[1]<=T231*MAS[1]

	S += T231_in*MAS_in[2]<=T231*MAS[2]

	S += T231_in*MAS_in[3]<=T231*MAS[3]

	S += T231_in*MAS_in[4]<=T231*MAS[4]

	S += T231_in*MAS_in[5]<=T231*MAS[5]

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

	T241 = S.Task('T241', length=4, delay_cost=1)
	T241 += alt(MAS)
	T241_in = S.Task('T241_in', length=1, delay_cost=1)
	T241_in += alt(MAS_in)
	S += T241_in*MAS_in[0]<=T241*MAS[0]

	S += T241_in*MAS_in[1]<=T241*MAS[1]

	S += T241_in*MAS_in[2]<=T241*MAS[2]

	S += T241_in*MAS_in[3]<=T241*MAS[3]

	S += T241_in*MAS_in[4]<=T241*MAS[4]

	S += T241_in*MAS_in[5]<=T241*MAS[5]

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
	S += T241_mem1 <= T241

	Z3_t4 = S.Task('Z3_t4', length=11, delay_cost=1)
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
	S += Z3_t4_mem1 <= Z3_t4

	Z30 = S.Task('Z30', length=4, delay_cost=1)
	Z30 += alt(MAS)
	Z30_in = S.Task('Z30_in', length=1, delay_cost=1)
	Z30_in += alt(MAS_in)
	S += Z30_in*MAS_in[0]<=Z30*MAS[0]

	S += Z30_in*MAS_in[1]<=Z30*MAS[1]

	S += Z30_in*MAS_in[2]<=Z30*MAS[2]

	S += Z30_in*MAS_in[3]<=Z30*MAS[3]

	S += Z30_in*MAS_in[4]<=Z30*MAS[4]

	S += Z30_in*MAS_in[5]<=Z30*MAS[5]

	S += 0<Z30

	Z30_w = S.Task('Z30_w', length=1, delay_cost=1)
	Z30_w += alt(MAIN_MEM_w)
	S += Z30 <= Z30_w

	Z30_mem0 = S.Task('Z30_mem0', length=1, delay_cost=1)
	Z30_mem0 += MM_MEM[0]
	S += 79 < Z30_mem0
	S += Z30_mem0 <= Z30

	Z30_mem1 = S.Task('Z30_mem1', length=1, delay_cost=1)
	Z30_mem1 += alt(MM_MEM)
	S += (Z3_t1*MM[0])-1 < Z30_mem1*MM_MEM[1]
	S += (Z3_t1*MM[1])-1 < Z30_mem1*MM_MEM[3]
	S += Z30_mem1 <= Z30

	Z3_t5 = S.Task('Z3_t5', length=4, delay_cost=1)
	Z3_t5 += alt(MAS)
	Z3_t5_in = S.Task('Z3_t5_in', length=1, delay_cost=1)
	Z3_t5_in += alt(MAS_in)
	S += Z3_t5_in*MAS_in[0]<=Z3_t5*MAS[0]

	S += Z3_t5_in*MAS_in[1]<=Z3_t5*MAS[1]

	S += Z3_t5_in*MAS_in[2]<=Z3_t5*MAS[2]

	S += Z3_t5_in*MAS_in[3]<=Z3_t5*MAS[3]

	S += Z3_t5_in*MAS_in[4]<=Z3_t5*MAS[4]

	S += Z3_t5_in*MAS_in[5]<=Z3_t5*MAS[5]

	Z3_t5_mem0 = S.Task('Z3_t5_mem0', length=1, delay_cost=1)
	Z3_t5_mem0 += MM_MEM[0]
	S += 79 < Z3_t5_mem0
	S += Z3_t5_mem0 <= Z3_t5

	Z3_t5_mem1 = S.Task('Z3_t5_mem1', length=1, delay_cost=1)
	Z3_t5_mem1 += alt(MM_MEM)
	S += (Z3_t1*MM[0])-1 < Z3_t5_mem1*MM_MEM[1]
	S += (Z3_t1*MM[1])-1 < Z3_t5_mem1*MM_MEM[3]
	S += Z3_t5_mem1 <= Z3_t5

	T201 = S.Task('T201', length=4, delay_cost=1)
	T201 += alt(MAS)
	T201_in = S.Task('T201_in', length=1, delay_cost=1)
	T201_in += alt(MAS_in)
	S += T201_in*MAS_in[0]<=T201*MAS[0]

	S += T201_in*MAS_in[1]<=T201*MAS[1]

	S += T201_in*MAS_in[2]<=T201*MAS[2]

	S += T201_in*MAS_in[3]<=T201*MAS[3]

	S += T201_in*MAS_in[4]<=T201*MAS[4]

	S += T201_in*MAS_in[5]<=T201*MAS[5]

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
	S += T201_mem1 <= T201

	T220 = S.Task('T220', length=4, delay_cost=1)
	T220 += alt(MAS)
	T220_in = S.Task('T220_in', length=1, delay_cost=1)
	T220_in += alt(MAS_in)
	S += T220_in*MAS_in[0]<=T220*MAS[0]

	S += T220_in*MAS_in[1]<=T220*MAS[1]

	S += T220_in*MAS_in[2]<=T220*MAS[2]

	S += T220_in*MAS_in[3]<=T220*MAS[3]

	S += T220_in*MAS_in[4]<=T220*MAS[4]

	S += T220_in*MAS_in[5]<=T220*MAS[5]

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
	S += T220_mem1 <= T220

	T230 = S.Task('T230', length=4, delay_cost=1)
	T230 += alt(MAS)
	T230_in = S.Task('T230_in', length=1, delay_cost=1)
	T230_in += alt(MAS_in)
	S += T230_in*MAS_in[0]<=T230*MAS[0]

	S += T230_in*MAS_in[1]<=T230*MAS[1]

	S += T230_in*MAS_in[2]<=T230*MAS[2]

	S += T230_in*MAS_in[3]<=T230*MAS[3]

	S += T230_in*MAS_in[4]<=T230*MAS[4]

	S += T230_in*MAS_in[5]<=T230*MAS[5]

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
	S += T230_mem1 <= T230

	T250 = S.Task('T250', length=4, delay_cost=1)
	T250 += alt(MAS)
	T250_in = S.Task('T250_in', length=1, delay_cost=1)
	T250_in += alt(MAS_in)
	S += T250_in*MAS_in[0]<=T250*MAS[0]

	S += T250_in*MAS_in[1]<=T250*MAS[1]

	S += T250_in*MAS_in[2]<=T250*MAS[2]

	S += T250_in*MAS_in[3]<=T250*MAS[3]

	S += T250_in*MAS_in[4]<=T250*MAS[4]

	S += T250_in*MAS_in[5]<=T250*MAS[5]

	T250_mem0 = S.Task('T250_mem0', length=1, delay_cost=1)
	T250_mem0 += alt(MAS_MEM)
	S += (T200*MAS[0])-1 < T250_mem0*MAS_MEM[0]
	S += (T200*MAS[1])-1 < T250_mem0*MAS_MEM[2]
	S += (T200*MAS[2])-1 < T250_mem0*MAS_MEM[4]
	S += (T200*MAS[3])-1 < T250_mem0*MAS_MEM[6]
	S += (T200*MAS[4])-1 < T250_mem0*MAS_MEM[8]
	S += (T200*MAS[5])-1 < T250_mem0*MAS_MEM[10]
	S += T250_mem0 <= T250

	T250_mem1 = S.Task('T250_mem1', length=1, delay_cost=1)
	T250_mem1 += alt(MAS_MEM)
	S += (T200*MAS[0])-1 < T250_mem1*MAS_MEM[1]
	S += (T200*MAS[1])-1 < T250_mem1*MAS_MEM[3]
	S += (T200*MAS[2])-1 < T250_mem1*MAS_MEM[5]
	S += (T200*MAS[3])-1 < T250_mem1*MAS_MEM[7]
	S += (T200*MAS[4])-1 < T250_mem1*MAS_MEM[9]
	S += (T200*MAS[5])-1 < T250_mem1*MAS_MEM[11]
	S += T250_mem1 <= T250

	Z31 = S.Task('Z31', length=4, delay_cost=1)
	Z31 += alt(MAS)
	Z31_in = S.Task('Z31_in', length=1, delay_cost=1)
	Z31_in += alt(MAS_in)
	S += Z31_in*MAS_in[0]<=Z31*MAS[0]

	S += Z31_in*MAS_in[1]<=Z31*MAS[1]

	S += Z31_in*MAS_in[2]<=Z31*MAS[2]

	S += Z31_in*MAS_in[3]<=Z31*MAS[3]

	S += Z31_in*MAS_in[4]<=Z31*MAS[4]

	S += Z31_in*MAS_in[5]<=Z31*MAS[5]

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
	S += Z31_mem1 <= Z31

	X31 = S.Task('X31', length=4, delay_cost=1)
	X31 += alt(MAS)
	X31_in = S.Task('X31_in', length=1, delay_cost=1)
	X31_in += alt(MAS_in)
	S += X31_in*MAS_in[0]<=X31*MAS[0]

	S += X31_in*MAS_in[1]<=X31*MAS[1]

	S += X31_in*MAS_in[2]<=X31*MAS[2]

	S += X31_in*MAS_in[3]<=X31*MAS[3]

	S += X31_in*MAS_in[4]<=X31*MAS[4]

	S += X31_in*MAS_in[5]<=X31*MAS[5]

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
	S += X31_mem0 <= X31

	X31_mem1 = S.Task('X31_mem1', length=1, delay_cost=1)
	X31_mem1 += alt(MAS_MEM)
	S += (T241*MAS[0])-1 < X31_mem1*MAS_MEM[1]
	S += (T241*MAS[1])-1 < X31_mem1*MAS_MEM[3]
	S += (T241*MAS[2])-1 < X31_mem1*MAS_MEM[5]
	S += (T241*MAS[3])-1 < X31_mem1*MAS_MEM[7]
	S += (T241*MAS[4])-1 < X31_mem1*MAS_MEM[9]
	S += (T241*MAS[5])-1 < X31_mem1*MAS_MEM[11]
	S += X31_mem1 <= X31

	X41 = S.Task('X41', length=4, delay_cost=1)
	X41 += alt(MAS)
	X41_in = S.Task('X41_in', length=1, delay_cost=1)
	X41_in += alt(MAS_in)
	S += X41_in*MAS_in[0]<=X41*MAS[0]

	S += X41_in*MAS_in[1]<=X41*MAS[1]

	S += X41_in*MAS_in[2]<=X41*MAS[2]

	S += X41_in*MAS_in[3]<=X41*MAS[3]

	S += X41_in*MAS_in[4]<=X41*MAS[4]

	S += X41_in*MAS_in[5]<=X41*MAS[5]

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
	S += X41_mem0 <= X41

	X41_mem1 = S.Task('X41_mem1', length=1, delay_cost=1)
	X41_mem1 += alt(MAS_MEM)
	S += (T171*MAS[0])-1 < X41_mem1*MAS_MEM[1]
	S += (T171*MAS[1])-1 < X41_mem1*MAS_MEM[3]
	S += (T171*MAS[2])-1 < X41_mem1*MAS_MEM[5]
	S += (T171*MAS[3])-1 < X41_mem1*MAS_MEM[7]
	S += (T171*MAS[4])-1 < X41_mem1*MAS_MEM[9]
	S += (T171*MAS[5])-1 < X41_mem1*MAS_MEM[11]
	S += X41_mem1 <= X41

	T251 = S.Task('T251', length=4, delay_cost=1)
	T251 += alt(MAS)
	T251_in = S.Task('T251_in', length=1, delay_cost=1)
	T251_in += alt(MAS_in)
	S += T251_in*MAS_in[0]<=T251*MAS[0]

	S += T251_in*MAS_in[1]<=T251*MAS[1]

	S += T251_in*MAS_in[2]<=T251*MAS[2]

	S += T251_in*MAS_in[3]<=T251*MAS[3]

	S += T251_in*MAS_in[4]<=T251*MAS[4]

	S += T251_in*MAS_in[5]<=T251*MAS[5]

	T251_mem0 = S.Task('T251_mem0', length=1, delay_cost=1)
	T251_mem0 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem0*MAS_MEM[0]
	S += (T201*MAS[1])-1 < T251_mem0*MAS_MEM[2]
	S += (T201*MAS[2])-1 < T251_mem0*MAS_MEM[4]
	S += (T201*MAS[3])-1 < T251_mem0*MAS_MEM[6]
	S += (T201*MAS[4])-1 < T251_mem0*MAS_MEM[8]
	S += (T201*MAS[5])-1 < T251_mem0*MAS_MEM[10]
	S += T251_mem0 <= T251

	T251_mem1 = S.Task('T251_mem1', length=1, delay_cost=1)
	T251_mem1 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem1*MAS_MEM[1]
	S += (T201*MAS[1])-1 < T251_mem1*MAS_MEM[3]
	S += (T201*MAS[2])-1 < T251_mem1*MAS_MEM[5]
	S += (T201*MAS[3])-1 < T251_mem1*MAS_MEM[7]
	S += (T201*MAS[4])-1 < T251_mem1*MAS_MEM[9]
	S += (T201*MAS[5])-1 < T251_mem1*MAS_MEM[11]
	S += T251_mem1 <= T251

	X30 = S.Task('X30', length=4, delay_cost=1)
	X30 += alt(MAS)
	X30_in = S.Task('X30_in', length=1, delay_cost=1)
	X30_in += alt(MAS_in)
	S += X30_in*MAS_in[0]<=X30*MAS[0]

	S += X30_in*MAS_in[1]<=X30*MAS[1]

	S += X30_in*MAS_in[2]<=X30*MAS[2]

	S += X30_in*MAS_in[3]<=X30*MAS[3]

	S += X30_in*MAS_in[4]<=X30*MAS[4]

	S += X30_in*MAS_in[5]<=X30*MAS[5]

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
	S += X30_mem0 <= X30

	X30_mem1 = S.Task('X30_mem1', length=1, delay_cost=1)
	X30_mem1 += alt(MAS_MEM)
	S += (T240*MAS[0])-1 < X30_mem1*MAS_MEM[1]
	S += (T240*MAS[1])-1 < X30_mem1*MAS_MEM[3]
	S += (T240*MAS[2])-1 < X30_mem1*MAS_MEM[5]
	S += (T240*MAS[3])-1 < X30_mem1*MAS_MEM[7]
	S += (T240*MAS[4])-1 < X30_mem1*MAS_MEM[9]
	S += (T240*MAS[5])-1 < X30_mem1*MAS_MEM[11]
	S += X30_mem1 <= X30

	Z40 = S.Task('Z40', length=4, delay_cost=1)
	Z40 += alt(MAS)
	Z40_in = S.Task('Z40_in', length=1, delay_cost=1)
	Z40_in += alt(MAS_in)
	S += Z40_in*MAS_in[0]<=Z40*MAS[0]

	S += Z40_in*MAS_in[1]<=Z40*MAS[1]

	S += Z40_in*MAS_in[2]<=Z40*MAS[2]

	S += Z40_in*MAS_in[3]<=Z40*MAS[3]

	S += Z40_in*MAS_in[4]<=Z40*MAS[4]

	S += Z40_in*MAS_in[5]<=Z40*MAS[5]

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
	S += Z40_mem0 <= Z40

	Z40_mem1 = S.Task('Z40_mem1', length=1, delay_cost=1)
	Z40_mem1 += alt(MAS_MEM)
	S += (T250*MAS[0])-1 < Z40_mem1*MAS_MEM[1]
	S += (T250*MAS[1])-1 < Z40_mem1*MAS_MEM[3]
	S += (T250*MAS[2])-1 < Z40_mem1*MAS_MEM[5]
	S += (T250*MAS[3])-1 < Z40_mem1*MAS_MEM[7]
	S += (T250*MAS[4])-1 < Z40_mem1*MAS_MEM[9]
	S += (T250*MAS[5])-1 < Z40_mem1*MAS_MEM[11]
	S += Z40_mem1 <= Z40

	X40 = S.Task('X40', length=4, delay_cost=1)
	X40 += alt(MAS)
	X40_in = S.Task('X40_in', length=1, delay_cost=1)
	X40_in += alt(MAS_in)
	S += X40_in*MAS_in[0]<=X40*MAS[0]

	S += X40_in*MAS_in[1]<=X40*MAS[1]

	S += X40_in*MAS_in[2]<=X40*MAS[2]

	S += X40_in*MAS_in[3]<=X40*MAS[3]

	S += X40_in*MAS_in[4]<=X40*MAS[4]

	S += X40_in*MAS_in[5]<=X40*MAS[5]

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
	S += X40_mem0 <= X40

	X40_mem1 = S.Task('X40_mem1', length=1, delay_cost=1)
	X40_mem1 += alt(MAS_MEM)
	S += (T170*MAS[0])-1 < X40_mem1*MAS_MEM[1]
	S += (T170*MAS[1])-1 < X40_mem1*MAS_MEM[3]
	S += (T170*MAS[2])-1 < X40_mem1*MAS_MEM[5]
	S += (T170*MAS[3])-1 < X40_mem1*MAS_MEM[7]
	S += (T170*MAS[4])-1 < X40_mem1*MAS_MEM[9]
	S += (T170*MAS[5])-1 < X40_mem1*MAS_MEM[11]
	S += X40_mem1 <= X40

	Z41 = S.Task('Z41', length=4, delay_cost=1)
	Z41 += alt(MAS)
	Z41_in = S.Task('Z41_in', length=1, delay_cost=1)
	Z41_in += alt(MAS_in)
	S += Z41_in*MAS_in[0]<=Z41*MAS[0]

	S += Z41_in*MAS_in[1]<=Z41*MAS[1]

	S += Z41_in*MAS_in[2]<=Z41*MAS[2]

	S += Z41_in*MAS_in[3]<=Z41*MAS[3]

	S += Z41_in*MAS_in[4]<=Z41*MAS[4]

	S += Z41_in*MAS_in[5]<=Z41*MAS[5]

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
	S += Z41_mem0 <= Z41

	Z41_mem1 = S.Task('Z41_mem1', length=1, delay_cost=1)
	Z41_mem1 += alt(MAS_MEM)
	S += (T251*MAS[0])-1 < Z41_mem1*MAS_MEM[1]
	S += (T251*MAS[1])-1 < Z41_mem1*MAS_MEM[3]
	S += (T251*MAS[2])-1 < Z41_mem1*MAS_MEM[5]
	S += (T251*MAS[3])-1 < Z41_mem1*MAS_MEM[7]
	S += (T251*MAS[4])-1 < Z41_mem1*MAS_MEM[9]
	S += (T251*MAS[5])-1 < Z41_mem1*MAS_MEM[11]
	S += Z41_mem1 <= Z41

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage4MAS6/EP2_LADDERMUL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

