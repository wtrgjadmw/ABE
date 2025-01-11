from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 190
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=9)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=2, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	T11_t2_in = S.Task('T11_t2_in', length=1, delay_cost=1)
	S += T11_t2_in >= 0
	T11_t2_in += MAS_in[0]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	S += T11_t2_mem0 >= 0
	T11_t2_mem0 += MAIN_MEM_r[0]

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	S += T11_t2_mem1 >= 0
	T11_t2_mem1 += MAIN_MEM_r[1]

	T11_t2 = S.Task('T11_t2', length=2, delay_cost=1)
	S += T11_t2 >= 1
	T11_t2 += MAS[0]

	T2_t2_in = S.Task('T2_t2_in', length=1, delay_cost=1)
	S += T2_t2_in >= 1
	T2_t2_in += MAS_in[1]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	S += T2_t2_mem0 >= 1
	T2_t2_mem0 += MAIN_MEM_r[0]

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	S += T2_t2_mem1 >= 1
	T2_t2_mem1 += MAIN_MEM_r[1]

	T2_t2 = S.Task('T2_t2', length=2, delay_cost=1)
	S += T2_t2 >= 2
	T2_t2 += MAS[1]

	T5_t0_in = S.Task('T5_t0_in', length=1, delay_cost=1)
	S += T5_t0_in >= 2
	T5_t0_in += MAS_in[1]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	S += T5_t0_mem0 >= 2
	T5_t0_mem0 += MAIN_MEM_r[0]

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	S += T5_t0_mem1 >= 2
	T5_t0_mem1 += MAIN_MEM_r[1]

	T10_t2_in = S.Task('T10_t2_in', length=1, delay_cost=1)
	S += T10_t2_in >= 3
	T10_t2_in += MAS_in[0]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	S += T10_t2_mem0 >= 3
	T10_t2_mem0 += MAIN_MEM_r[0]

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	S += T10_t2_mem1 >= 3
	T10_t2_mem1 += MAIN_MEM_r[1]

	T5_t0 = S.Task('T5_t0', length=2, delay_cost=1)
	S += T5_t0 >= 3
	T5_t0 += MAS[1]

	T10_t2 = S.Task('T10_t2', length=2, delay_cost=1)
	S += T10_t2 >= 4
	T10_t2 += MAS[0]

	T2_t3_in = S.Task('T2_t3_in', length=1, delay_cost=1)
	S += T2_t3_in >= 4
	T2_t3_in += MAS_in[1]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	S += T2_t3_mem0 >= 4
	T2_t3_mem0 += MAIN_MEM_r[0]

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	S += T2_t3_mem1 >= 4
	T2_t3_mem1 += MAIN_MEM_r[1]

	T2_t3 = S.Task('T2_t3', length=2, delay_cost=1)
	S += T2_t3 >= 5
	T2_t3 += MAS[1]

	T3_t2_in = S.Task('T3_t2_in', length=1, delay_cost=1)
	S += T3_t2_in >= 5
	T3_t2_in += MAS_in[0]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	S += T3_t2_mem0 >= 5
	T3_t2_mem0 += MAIN_MEM_r[0]

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	S += T3_t2_mem1 >= 5
	T3_t2_mem1 += MAIN_MEM_r[1]

	T2_t4_in = S.Task('T2_t4_in', length=1, delay_cost=1)
	S += T2_t4_in >= 6
	T2_t4_in += MM_in[0]

	T2_t4_mem0 = S.Task('T2_t4_mem0', length=1, delay_cost=1)
	S += T2_t4_mem0 >= 6
	T2_t4_mem0 += MAS_MEM[2]

	T2_t4_mem1 = S.Task('T2_t4_mem1', length=1, delay_cost=1)
	S += T2_t4_mem1 >= 6
	T2_t4_mem1 += MAS_MEM[3]

	T3_t2 = S.Task('T3_t2', length=2, delay_cost=1)
	S += T3_t2 >= 6
	T3_t2 += MAS[0]

	T7_t3_in = S.Task('T7_t3_in', length=1, delay_cost=1)
	S += T7_t3_in >= 6
	T7_t3_in += MAS_in[1]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	S += T7_t3_mem0 >= 6
	T7_t3_mem0 += MAIN_MEM_r[0]

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	S += T7_t3_mem1 >= 6
	T7_t3_mem1 += MAIN_MEM_r[1]

	T2_t4 = S.Task('T2_t4', length=9, delay_cost=1)
	S += T2_t4 >= 7
	T2_t4 += MM[0]

	T7_t2_in = S.Task('T7_t2_in', length=1, delay_cost=1)
	S += T7_t2_in >= 7
	T7_t2_in += MAS_in[0]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	S += T7_t2_mem0 >= 7
	T7_t2_mem0 += MAIN_MEM_r[0]

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	S += T7_t2_mem1 >= 7
	T7_t2_mem1 += MAIN_MEM_r[1]

	T7_t3 = S.Task('T7_t3', length=2, delay_cost=1)
	S += T7_t3 >= 7
	T7_t3 += MAS[1]

	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	S += T3_t1_in >= 8
	T3_t1_in += MM_in[0]

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	S += T3_t1_mem0 >= 8
	T3_t1_mem0 += MAIN_MEM_r[0]

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	S += T3_t1_mem1 >= 8
	T3_t1_mem1 += MAIN_MEM_r[1]

	T7_t2 = S.Task('T7_t2', length=2, delay_cost=1)
	S += T7_t2 >= 8
	T7_t2 += MAS[0]

	T3_t1 = S.Task('T3_t1', length=9, delay_cost=1)
	S += T3_t1 >= 9
	T3_t1 += MM[0]

	T4_t2_in = S.Task('T4_t2_in', length=1, delay_cost=1)
	S += T4_t2_in >= 9
	T4_t2_in += MAS_in[0]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	S += T4_t2_mem0 >= 9
	T4_t2_mem0 += MAIN_MEM_r[0]

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	S += T4_t2_mem1 >= 9
	T4_t2_mem1 += MAIN_MEM_r[1]

	T7_t4_in = S.Task('T7_t4_in', length=1, delay_cost=1)
	S += T7_t4_in >= 9
	T7_t4_in += MM_in[0]

	T7_t4_mem0 = S.Task('T7_t4_mem0', length=1, delay_cost=1)
	S += T7_t4_mem0 >= 9
	T7_t4_mem0 += MAS_MEM[0]

	T7_t4_mem1 = S.Task('T7_t4_mem1', length=1, delay_cost=1)
	S += T7_t4_mem1 >= 9
	T7_t4_mem1 += MAS_MEM[3]

	T4_t2 = S.Task('T4_t2', length=2, delay_cost=1)
	S += T4_t2 >= 10
	T4_t2 += MAS[0]

	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	S += T6_t0_in >= 10
	T6_t0_in += MM_in[0]

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	S += T6_t0_mem0 >= 10
	T6_t0_mem0 += MAIN_MEM_r[0]

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	S += T6_t0_mem1 >= 10
	T6_t0_mem1 += MAIN_MEM_r[1]

	T7_t4 = S.Task('T7_t4', length=9, delay_cost=1)
	S += T7_t4 >= 10
	T7_t4 += MM[0]

	T6_t0 = S.Task('T6_t0', length=9, delay_cost=1)
	S += T6_t0 >= 11
	T6_t0 += MM[0]

	T9_t2_in = S.Task('T9_t2_in', length=1, delay_cost=1)
	S += T9_t2_in >= 11
	T9_t2_in += MAS_in[0]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	S += T9_t2_mem0 >= 11
	T9_t2_mem0 += MAIN_MEM_r[0]

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	S += T9_t2_mem1 >= 11
	T9_t2_mem1 += MAIN_MEM_r[1]

	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	S += T7_t0_in >= 12
	T7_t0_in += MM_in[0]

	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	S += T7_t0_mem0 >= 12
	T7_t0_mem0 += MAIN_MEM_r[0]

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	S += T7_t0_mem1 >= 12
	T7_t0_mem1 += MAIN_MEM_r[1]

	T9_t2 = S.Task('T9_t2', length=2, delay_cost=1)
	S += T9_t2 >= 12
	T9_t2 += MAS[0]

	T6_t2_in = S.Task('T6_t2_in', length=1, delay_cost=1)
	S += T6_t2_in >= 13
	T6_t2_in += MAS_in[1]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	S += T6_t2_mem0 >= 13
	T6_t2_mem0 += MAIN_MEM_r[0]

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	S += T6_t2_mem1 >= 13
	T6_t2_mem1 += MAIN_MEM_r[1]

	T7_t0 = S.Task('T7_t0', length=9, delay_cost=1)
	S += T7_t0 >= 13
	T7_t0 += MM[0]

	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	S += T6_t1_in >= 14
	T6_t1_in += MM_in[0]

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	S += T6_t1_mem0 >= 14
	T6_t1_mem0 += MAIN_MEM_r[0]

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	S += T6_t1_mem1 >= 14
	T6_t1_mem1 += MAIN_MEM_r[1]

	T6_t2 = S.Task('T6_t2', length=2, delay_cost=1)
	S += T6_t2 >= 14
	T6_t2 += MAS[1]

	T6_t1 = S.Task('T6_t1', length=9, delay_cost=1)
	S += T6_t1 >= 15
	T6_t1 += MM[0]

	T8_t2_in = S.Task('T8_t2_in', length=1, delay_cost=1)
	S += T8_t2_in >= 15
	T8_t2_in += MAS_in[0]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	S += T8_t2_mem0 >= 15
	T8_t2_mem0 += MAIN_MEM_r[0]

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	S += T8_t2_mem1 >= 15
	T8_t2_mem1 += MAIN_MEM_r[1]

	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	S += T7_t1_in >= 16
	T7_t1_in += MM_in[0]

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	S += T7_t1_mem0 >= 16
	T7_t1_mem0 += MAIN_MEM_r[0]

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	S += T7_t1_mem1 >= 16
	T7_t1_mem1 += MAIN_MEM_r[1]

	T8_t2 = S.Task('T8_t2', length=2, delay_cost=1)
	S += T8_t2 >= 16
	T8_t2 += MAS[0]

	T4_t3_in = S.Task('T4_t3_in', length=1, delay_cost=1)
	S += T4_t3_in >= 17
	T4_t3_in += MAS_in[0]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	S += T4_t3_mem0 >= 17
	T4_t3_mem0 += MAIN_MEM_r[0]

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	S += T4_t3_mem1 >= 17
	T4_t3_mem1 += MAIN_MEM_r[1]

	T7_t1 = S.Task('T7_t1', length=9, delay_cost=1)
	S += T7_t1 >= 17
	T7_t1 += MM[0]

	T4_t3 = S.Task('T4_t3', length=2, delay_cost=1)
	S += T4_t3 >= 18
	T4_t3 += MAS[0]

	T5_t1_in = S.Task('T5_t1_in', length=1, delay_cost=1)
	S += T5_t1_in >= 18
	T5_t1_in += MAS_in[0]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	S += T5_t1_mem0 >= 18
	T5_t1_mem0 += MAIN_MEM_r[0]

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	S += T5_t1_mem1 >= 18
	T5_t1_mem1 += MAIN_MEM_r[1]

	T3_t3_in = S.Task('T3_t3_in', length=1, delay_cost=1)
	S += T3_t3_in >= 19
	T3_t3_in += MAS_in[0]

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	S += T3_t3_mem0 >= 19
	T3_t3_mem0 += MAIN_MEM_r[0]

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	S += T3_t3_mem1 >= 19
	T3_t3_mem1 += MAIN_MEM_r[1]

	T4_t4_in = S.Task('T4_t4_in', length=1, delay_cost=1)
	S += T4_t4_in >= 19
	T4_t4_in += MM_in[0]

	T4_t4_mem0 = S.Task('T4_t4_mem0', length=1, delay_cost=1)
	S += T4_t4_mem0 >= 19
	T4_t4_mem0 += MAS_MEM[0]

	T4_t4_mem1 = S.Task('T4_t4_mem1', length=1, delay_cost=1)
	S += T4_t4_mem1 >= 19
	T4_t4_mem1 += MAS_MEM[1]

	T5_t1 = S.Task('T5_t1', length=2, delay_cost=1)
	S += T5_t1 >= 19
	T5_t1 += MAS[0]

	T1_t0_in = S.Task('T1_t0_in', length=1, delay_cost=1)
	S += T1_t0_in >= 20
	T1_t0_in += MAS_in[1]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	S += T1_t0_mem0 >= 20
	T1_t0_mem0 += MAIN_MEM_r[0]

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	S += T1_t0_mem1 >= 20
	T1_t0_mem1 += MAIN_MEM_r[1]

	T3_t3 = S.Task('T3_t3', length=2, delay_cost=1)
	S += T3_t3 >= 20
	T3_t3 += MAS[0]

	T4_t4 = S.Task('T4_t4', length=9, delay_cost=1)
	S += T4_t4 >= 20
	T4_t4 += MM[0]

	T5_t2_in = S.Task('T5_t2_in', length=1, delay_cost=1)
	S += T5_t2_in >= 20
	T5_t2_in += MM_in[0]

	T5_t2_mem0 = S.Task('T5_t2_mem0', length=1, delay_cost=1)
	S += T5_t2_mem0 >= 20
	T5_t2_mem0 += MAS_MEM[2]

	T5_t2_mem1 = S.Task('T5_t2_mem1', length=1, delay_cost=1)
	S += T5_t2_mem1 >= 20
	T5_t2_mem1 += MAS_MEM[1]

	T1_t0 = S.Task('T1_t0', length=2, delay_cost=1)
	S += T1_t0 >= 21
	T1_t0 += MAS[1]

	T3_t4_in = S.Task('T3_t4_in', length=1, delay_cost=1)
	S += T3_t4_in >= 21
	T3_t4_in += MM_in[0]

	T3_t4_mem0 = S.Task('T3_t4_mem0', length=1, delay_cost=1)
	S += T3_t4_mem0 >= 21
	T3_t4_mem0 += MAS_MEM[0]

	T3_t4_mem1 = S.Task('T3_t4_mem1', length=1, delay_cost=1)
	S += T3_t4_mem1 >= 21
	T3_t4_mem1 += MAS_MEM[1]

	T5_t2 = S.Task('T5_t2', length=9, delay_cost=1)
	S += T5_t2 >= 21
	T5_t2 += MM[0]

	T6_t3_in = S.Task('T6_t3_in', length=1, delay_cost=1)
	S += T6_t3_in >= 21
	T6_t3_in += MAS_in[1]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	S += T6_t3_mem0 >= 21
	T6_t3_mem0 += MAIN_MEM_r[0]

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	S += T6_t3_mem1 >= 21
	T6_t3_mem1 += MAIN_MEM_r[1]

	T3_t4 = S.Task('T3_t4', length=9, delay_cost=1)
	S += T3_t4 >= 22
	T3_t4 += MM[0]

	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	S += T5_t3_in >= 22
	T5_t3_in += MM_in[0]

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	S += T5_t3_mem0 >= 22
	T5_t3_mem0 += MAIN_MEM_r[0]

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	S += T5_t3_mem1 >= 22
	T5_t3_mem1 += MAIN_MEM_r[1]

	T6_t3 = S.Task('T6_t3', length=2, delay_cost=1)
	S += T6_t3 >= 22
	T6_t3 += MAS[1]

	T1_t1_in = S.Task('T1_t1_in', length=1, delay_cost=1)
	S += T1_t1_in >= 23
	T1_t1_in += MAS_in[0]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	S += T1_t1_mem0 >= 23
	T1_t1_mem0 += MAIN_MEM_r[0]

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	S += T1_t1_mem1 >= 23
	T1_t1_mem1 += MAIN_MEM_r[1]

	T5_t3 = S.Task('T5_t3', length=9, delay_cost=1)
	S += T5_t3 >= 23
	T5_t3 += MM[0]

	T6_t4_in = S.Task('T6_t4_in', length=1, delay_cost=1)
	S += T6_t4_in >= 23
	T6_t4_in += MM_in[0]

	T6_t4_mem0 = S.Task('T6_t4_mem0', length=1, delay_cost=1)
	S += T6_t4_mem0 >= 23
	T6_t4_mem0 += MAS_MEM[2]

	T6_t4_mem1 = S.Task('T6_t4_mem1', length=1, delay_cost=1)
	S += T6_t4_mem1 >= 23
	T6_t4_mem1 += MAS_MEM[3]

	T6_t5_in = S.Task('T6_t5_in', length=1, delay_cost=1)
	S += T6_t5_in >= 23
	T6_t5_in += MAS_in[1]

	T6_t5_mem0 = S.Task('T6_t5_mem0', length=1, delay_cost=1)
	S += T6_t5_mem0 >= 23
	T6_t5_mem0 += MM_MEM[0]

	T6_t5_mem1 = S.Task('T6_t5_mem1', length=1, delay_cost=1)
	S += T6_t5_mem1 >= 23
	T6_t5_mem1 += MM_MEM[1]

	T1_t1 = S.Task('T1_t1', length=2, delay_cost=1)
	S += T1_t1 >= 24
	T1_t1 += MAS[0]

	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	S += T4_t1_in >= 24
	T4_t1_in += MM_in[0]

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	S += T4_t1_mem0 >= 24
	T4_t1_mem0 += MAIN_MEM_r[0]

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	S += T4_t1_mem1 >= 24
	T4_t1_mem1 += MAIN_MEM_r[1]

	T60_in = S.Task('T60_in', length=1, delay_cost=1)
	S += T60_in >= 24
	T60_in += MAS_in[1]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 24
	T60_mem0 += MM_MEM[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 24
	T60_mem1 += MM_MEM[1]

	T6_t4 = S.Task('T6_t4', length=9, delay_cost=1)
	S += T6_t4 >= 24
	T6_t4 += MM[0]

	T6_t5 = S.Task('T6_t5', length=2, delay_cost=1)
	S += T6_t5 >= 24
	T6_t5 += MAS[1]

	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	S += T4_t0_in >= 25
	T4_t0_in += MM_in[0]

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	S += T4_t0_mem0 >= 25
	T4_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	S += T4_t0_mem1 >= 25
	T4_t0_mem1 += MAIN_MEM_r[1]

	T4_t1 = S.Task('T4_t1', length=9, delay_cost=1)
	S += T4_t1 >= 25
	T4_t1 += MM[0]

	T60 = S.Task('T60', length=2, delay_cost=1)
	S += T60 >= 25
	T60 += MAS[1]

	T7_t5_in = S.Task('T7_t5_in', length=1, delay_cost=1)
	S += T7_t5_in >= 25
	T7_t5_in += MAS_in[1]

	T7_t5_mem0 = S.Task('T7_t5_mem0', length=1, delay_cost=1)
	S += T7_t5_mem0 >= 25
	T7_t5_mem0 += MM_MEM[0]

	T7_t5_mem1 = S.Task('T7_t5_mem1', length=1, delay_cost=1)
	S += T7_t5_mem1 >= 25
	T7_t5_mem1 += MM_MEM[1]

	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	S += T3_t0_in >= 26
	T3_t0_in += MM_in[0]

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	S += T3_t0_mem0 >= 26
	T3_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	S += T3_t0_mem1 >= 26
	T3_t0_mem1 += MAIN_MEM_r[1]

	T4_t0 = S.Task('T4_t0', length=9, delay_cost=1)
	S += T4_t0 >= 26
	T4_t0 += MM[0]

	T70_in = S.Task('T70_in', length=1, delay_cost=1)
	S += T70_in >= 26
	T70_in += MAS_in[0]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 26
	T70_mem0 += MM_MEM[0]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 26
	T70_mem1 += MM_MEM[1]

	T7_t5 = S.Task('T7_t5', length=2, delay_cost=1)
	S += T7_t5 >= 26
	T7_t5 += MAS[1]

	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	S += T2_t1_in >= 27
	T2_t1_in += MM_in[0]

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	S += T2_t1_mem0 >= 27
	T2_t1_mem0 += MAIN_MEM_r[0]

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	S += T2_t1_mem1 >= 27
	T2_t1_mem1 += MAIN_MEM_r[1]

	T3_t0 = S.Task('T3_t0', length=9, delay_cost=1)
	S += T3_t0 >= 27
	T3_t0 += MM[0]

	T70 = S.Task('T70', length=2, delay_cost=1)
	S += T70 >= 27
	T70 += MAS[0]

	T71_in = S.Task('T71_in', length=1, delay_cost=1)
	S += T71_in >= 27
	T71_in += MAS_in[1]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 27
	T71_mem0 += MM_MEM[0]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 27
	T71_mem1 += MAS_MEM[3]

	T150_in = S.Task('T150_in', length=1, delay_cost=1)
	S += T150_in >= 28
	T150_in += MAS_in[1]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 28
	T150_mem0 += MAS_MEM[0]

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 28
	T150_mem1 += MAS_MEM[1]

	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	S += T2_t0_in >= 28
	T2_t0_in += MM_in[0]

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	S += T2_t0_mem0 >= 28
	T2_t0_mem0 += MAIN_MEM_r[0]

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	S += T2_t0_mem1 >= 28
	T2_t0_mem1 += MAIN_MEM_r[1]

	T2_t1 = S.Task('T2_t1', length=9, delay_cost=1)
	S += T2_t1 >= 28
	T2_t1 += MM[0]

	T71 = S.Task('T71', length=2, delay_cost=1)
	S += T71 >= 28
	T71 += MAS[1]

	T150 = S.Task('T150', length=2, delay_cost=1)
	S += T150 >= 29
	T150 += MAS[1]

	T151_in = S.Task('T151_in', length=1, delay_cost=1)
	S += T151_in >= 29
	T151_in += MAS_in[1]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 29
	T151_mem0 += MAS_MEM[2]

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 29
	T151_mem1 += MAS_MEM[3]

	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	S += T1_t3_in >= 29
	T1_t3_in += MM_in[0]

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	S += T1_t3_mem0 >= 29
	T1_t3_mem0 += MAIN_MEM_r[0]

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	S += T1_t3_mem1 >= 29
	T1_t3_mem1 += MAIN_MEM_r[1]

	T2_t0 = S.Task('T2_t0', length=9, delay_cost=1)
	S += T2_t0 >= 29
	T2_t0 += MM[0]

	T151 = S.Task('T151', length=2, delay_cost=1)
	S += T151 >= 30
	T151 += MAS[1]

	T1_t2_in = S.Task('T1_t2_in', length=1, delay_cost=1)
	S += T1_t2_in >= 30
	T1_t2_in += MM_in[0]

	T1_t2_mem0 = S.Task('T1_t2_mem0', length=1, delay_cost=1)
	S += T1_t2_mem0 >= 30
	T1_t2_mem0 += MAS_MEM[2]

	T1_t2_mem1 = S.Task('T1_t2_mem1', length=1, delay_cost=1)
	S += T1_t2_mem1 >= 30
	T1_t2_mem1 += MAS_MEM[1]

	T1_t3 = S.Task('T1_t3', length=9, delay_cost=1)
	S += T1_t3 >= 30
	T1_t3 += MM[0]

	Z3_t2_in = S.Task('Z3_t2_in', length=1, delay_cost=1)
	S += Z3_t2_in >= 30
	Z3_t2_in += MAS_in[1]

	Z3_t2_mem0 = S.Task('Z3_t2_mem0', length=1, delay_cost=1)
	S += Z3_t2_mem0 >= 30
	Z3_t2_mem0 += MAIN_MEM_r[0]

	Z3_t2_mem1 = S.Task('Z3_t2_mem1', length=1, delay_cost=1)
	S += Z3_t2_mem1 >= 30
	Z3_t2_mem1 += MAIN_MEM_r[1]

	T17_t3_in = S.Task('T17_t3_in', length=1, delay_cost=1)
	S += T17_t3_in >= 31
	T17_t3_in += MAS_in[0]

	T17_t3_mem0 = S.Task('T17_t3_mem0', length=1, delay_cost=1)
	S += T17_t3_mem0 >= 31
	T17_t3_mem0 += MAS_MEM[2]

	T17_t3_mem1 = S.Task('T17_t3_mem1', length=1, delay_cost=1)
	S += T17_t3_mem1 >= 31
	T17_t3_mem1 += MAS_MEM[3]

	T1_t2 = S.Task('T1_t2', length=9, delay_cost=1)
	S += T1_t2 >= 31
	T1_t2 += MM[0]

	T5_t5_in = S.Task('T5_t5_in', length=1, delay_cost=1)
	S += T5_t5_in >= 31
	T5_t5_in += MAS_in[1]

	T5_t5_mem0 = S.Task('T5_t5_mem0', length=1, delay_cost=1)
	S += T5_t5_mem0 >= 31
	T5_t5_mem0 += MM_MEM[0]

	T5_t5_mem1 = S.Task('T5_t5_mem1', length=1, delay_cost=1)
	S += T5_t5_mem1 >= 31
	T5_t5_mem1 += MM_MEM[1]

	Z3_t2 = S.Task('Z3_t2', length=2, delay_cost=1)
	S += Z3_t2 >= 31
	Z3_t2 += MAS[1]

	T17_t3 = S.Task('T17_t3', length=2, delay_cost=1)
	S += T17_t3 >= 32
	T17_t3 += MAS[0]

	T5_t5 = S.Task('T5_t5', length=2, delay_cost=1)
	S += T5_t5 >= 32
	T5_t5 += MAS[1]

	T61_in = S.Task('T61_in', length=1, delay_cost=1)
	S += T61_in >= 32
	T61_in += MAS_in[1]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 32
	T61_mem0 += MM_MEM[0]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 32
	T61_mem1 += MAS_MEM[3]

	T50_in = S.Task('T50_in', length=1, delay_cost=1)
	S += T50_in >= 33
	T50_in += MAS_in[1]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 33
	T50_mem0 += MM_MEM[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 33
	T50_mem1 += MAS_MEM[3]

	T61 = S.Task('T61', length=2, delay_cost=1)
	S += T61 >= 33
	T61 += MAS[1]

	T20_t2_in = S.Task('T20_t2_in', length=1, delay_cost=1)
	S += T20_t2_in >= 34
	T20_t2_in += MAS_in[1]

	T20_t2_mem0 = S.Task('T20_t2_mem0', length=1, delay_cost=1)
	S += T20_t2_mem0 >= 34
	T20_t2_mem0 += MAS_MEM[2]

	T20_t2_mem1 = S.Task('T20_t2_mem1', length=1, delay_cost=1)
	S += T20_t2_mem1 >= 34
	T20_t2_mem1 += MAS_MEM[3]

	T40_in = S.Task('T40_in', length=1, delay_cost=1)
	S += T40_in >= 34
	T40_in += MAS_in[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 34
	T40_mem0 += MM_MEM[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 34
	T40_mem1 += MM_MEM[1]

	T50 = S.Task('T50', length=2, delay_cost=1)
	S += T50 >= 34
	T50 += MAS[1]

	T20_t2 = S.Task('T20_t2', length=2, delay_cost=1)
	S += T20_t2 >= 35
	T20_t2 += MAS[1]

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	S += T30_in >= 35
	T30_in += MAS_in[1]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 35
	T30_mem0 += MM_MEM[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 35
	T30_mem1 += MM_MEM[1]

	T40 = S.Task('T40', length=2, delay_cost=1)
	S += T40 >= 35
	T40 += MAS[0]

	T30 = S.Task('T30', length=2, delay_cost=1)
	S += T30 >= 36
	T30 += MAS[1]

	T3_t5_in = S.Task('T3_t5_in', length=1, delay_cost=1)
	S += T3_t5_in >= 36
	T3_t5_in += MAS_in[0]

	T3_t5_mem0 = S.Task('T3_t5_mem0', length=1, delay_cost=1)
	S += T3_t5_mem0 >= 36
	T3_t5_mem0 += MM_MEM[0]

	T3_t5_mem1 = S.Task('T3_t5_mem1', length=1, delay_cost=1)
	S += T3_t5_mem1 >= 36
	T3_t5_mem1 += MM_MEM[1]

	T11_t0_in = S.Task('T11_t0_in', length=1, delay_cost=1)
	S += T11_t0_in >= 37
	T11_t0_in += MM_in[0]

	T11_t0_mem0 = S.Task('T11_t0_mem0', length=1, delay_cost=1)
	S += T11_t0_mem0 >= 37
	T11_t0_mem0 += MAIN_MEM_r[0]

	T11_t0_mem1 = S.Task('T11_t0_mem1', length=1, delay_cost=1)
	S += T11_t0_mem1 >= 37
	T11_t0_mem1 += MAS_MEM[3]

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	S += T20_in >= 37
	T20_in += MAS_in[0]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 37
	T20_mem0 += MM_MEM[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 37
	T20_mem1 += MM_MEM[1]

	T3_t5 = S.Task('T3_t5', length=2, delay_cost=1)
	S += T3_t5 >= 37
	T3_t5 += MAS[0]

	T10_t0_in = S.Task('T10_t0_in', length=1, delay_cost=1)
	S += T10_t0_in >= 38
	T10_t0_in += MM_in[0]

	T10_t0_mem0 = S.Task('T10_t0_mem0', length=1, delay_cost=1)
	S += T10_t0_mem0 >= 38
	T10_t0_mem0 += MAIN_MEM_r[0]

	T10_t0_mem1 = S.Task('T10_t0_mem1', length=1, delay_cost=1)
	S += T10_t0_mem1 >= 38
	T10_t0_mem1 += MAS_MEM[3]

	T11_t0 = S.Task('T11_t0', length=9, delay_cost=1)
	S += T11_t0 >= 38
	T11_t0 += MM[0]

	T20 = S.Task('T20', length=2, delay_cost=1)
	S += T20 >= 38
	T20 += MAS[0]

	T31_in = S.Task('T31_in', length=1, delay_cost=1)
	S += T31_in >= 38
	T31_in += MAS_in[1]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 38
	T31_mem0 += MM_MEM[0]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 38
	T31_mem1 += MAS_MEM[1]

	T10_t0 = S.Task('T10_t0', length=9, delay_cost=1)
	S += T10_t0 >= 39
	T10_t0 += MM[0]

	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	S += T11_in >= 39
	T11_in += MAS_in[0]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 39
	T11_mem0 += MM_MEM[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 39
	T11_mem1 += MM_MEM[1]

	T120_in = S.Task('T120_in', length=1, delay_cost=1)
	S += T120_in >= 39
	T120_in += MAS_in[1]

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	S += T120_mem0 >= 39
	T120_mem0 += MAS_MEM[0]

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	S += T120_mem1 >= 39
	T120_mem1 += MAS_MEM[1]

	T31 = S.Task('T31', length=2, delay_cost=1)
	S += T31 >= 39
	T31 += MAS[1]

	T10_t1_in = S.Task('T10_t1_in', length=1, delay_cost=1)
	S += T10_t1_in >= 40
	T10_t1_in += MM_in[0]

	T10_t1_mem0 = S.Task('T10_t1_mem0', length=1, delay_cost=1)
	S += T10_t1_mem0 >= 40
	T10_t1_mem0 += MAIN_MEM_r[0]

	T10_t1_mem1 = S.Task('T10_t1_mem1', length=1, delay_cost=1)
	S += T10_t1_mem1 >= 40
	T10_t1_mem1 += MAS_MEM[3]

	T11 = S.Task('T11', length=2, delay_cost=1)
	S += T11 >= 40
	T11 += MAS[0]

	T120 = S.Task('T120', length=2, delay_cost=1)
	S += T120 >= 40
	T120 += MAS[1]

	T130_in = S.Task('T130_in', length=1, delay_cost=1)
	S += T130_in >= 40
	T130_in += MAS_in[0]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 40
	T130_mem0 += MAS_MEM[0]

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 40
	T130_mem1 += MAS_MEM[1]

	T1_t5_in = S.Task('T1_t5_in', length=1, delay_cost=1)
	S += T1_t5_in >= 40
	T1_t5_in += MAS_in[1]

	T1_t5_mem0 = S.Task('T1_t5_mem0', length=1, delay_cost=1)
	S += T1_t5_mem0 >= 40
	T1_t5_mem0 += MM_MEM[0]

	T1_t5_mem1 = S.Task('T1_t5_mem1', length=1, delay_cost=1)
	S += T1_t5_mem1 >= 40
	T1_t5_mem1 += MM_MEM[1]

	T10_t1 = S.Task('T10_t1', length=9, delay_cost=1)
	S += T10_t1 >= 41
	T10_t1 += MM[0]

	T10_t3_in = S.Task('T10_t3_in', length=1, delay_cost=1)
	S += T10_t3_in >= 41
	T10_t3_in += MAS_in[1]

	T10_t3_mem0 = S.Task('T10_t3_mem0', length=1, delay_cost=1)
	S += T10_t3_mem0 >= 41
	T10_t3_mem0 += MAS_MEM[2]

	T10_t3_mem1 = S.Task('T10_t3_mem1', length=1, delay_cost=1)
	S += T10_t3_mem1 >= 41
	T10_t3_mem1 += MAS_MEM[3]

	T130 = S.Task('T130', length=2, delay_cost=1)
	S += T130 >= 41
	T130 += MAS[0]

	T1_t5 = S.Task('T1_t5', length=2, delay_cost=1)
	S += T1_t5 >= 41
	T1_t5 += MAS[1]

	T51_in = S.Task('T51_in', length=1, delay_cost=1)
	S += T51_in >= 41
	T51_in += MAS_in[0]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 41
	T51_mem0 += MM_MEM[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 41
	T51_mem1 += MM_MEM[1]

	T8_t1_in = S.Task('T8_t1_in', length=1, delay_cost=1)
	S += T8_t1_in >= 41
	T8_t1_in += MM_in[0]

	T8_t1_mem0 = S.Task('T8_t1_mem0', length=1, delay_cost=1)
	S += T8_t1_mem0 >= 41
	T8_t1_mem0 += MAIN_MEM_r[0]

	T8_t1_mem1 = S.Task('T8_t1_mem1', length=1, delay_cost=1)
	S += T8_t1_mem1 >= 41
	T8_t1_mem1 += MAS_MEM[1]

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	S += T10_in >= 42
	T10_in += MAS_in[1]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 42
	T10_mem0 += MM_MEM[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 42
	T10_mem1 += MAS_MEM[3]

	T10_t3 = S.Task('T10_t3', length=2, delay_cost=1)
	S += T10_t3 >= 42
	T10_t3 += MAS[1]

	T51 = S.Task('T51', length=2, delay_cost=1)
	S += T51 >= 42
	T51 += MAS[0]

	T8_t1 = S.Task('T8_t1', length=9, delay_cost=1)
	S += T8_t1 >= 42
	T8_t1 += MM[0]

	T9_t1_in = S.Task('T9_t1_in', length=1, delay_cost=1)
	S += T9_t1_in >= 42
	T9_t1_in += MM_in[0]

	T9_t1_mem0 = S.Task('T9_t1_mem0', length=1, delay_cost=1)
	S += T9_t1_mem0 >= 42
	T9_t1_mem0 += MAIN_MEM_r[0]

	T9_t1_mem1 = S.Task('T9_t1_mem1', length=1, delay_cost=1)
	S += T9_t1_mem1 >= 42
	T9_t1_mem1 += MAS_MEM[1]

	T10 = S.Task('T10', length=2, delay_cost=1)
	S += T10 >= 43
	T10 += MAS[1]

	T11_t3_in = S.Task('T11_t3_in', length=1, delay_cost=1)
	S += T11_t3_in >= 43
	T11_t3_in += MAS_in[0]

	T11_t3_mem0 = S.Task('T11_t3_mem0', length=1, delay_cost=1)
	S += T11_t3_mem0 >= 43
	T11_t3_mem0 += MAS_MEM[2]

	T11_t3_mem1 = S.Task('T11_t3_mem1', length=1, delay_cost=1)
	S += T11_t3_mem1 >= 43
	T11_t3_mem1 += MAS_MEM[3]

	T14_t0_in = S.Task('T14_t0_in', length=1, delay_cost=1)
	S += T14_t0_in >= 43
	T14_t0_in += MM_in[0]

	T14_t0_mem0 = S.Task('T14_t0_mem0', length=1, delay_cost=1)
	S += T14_t0_mem0 >= 43
	T14_t0_mem0 += MAS_MEM[0]

	T14_t0_mem1 = S.Task('T14_t0_mem1', length=1, delay_cost=1)
	S += T14_t0_mem1 >= 43
	T14_t0_mem1 += MAS_MEM[1]

	T2_t5_in = S.Task('T2_t5_in', length=1, delay_cost=1)
	S += T2_t5_in >= 43
	T2_t5_in += MAS_in[1]

	T2_t5_mem0 = S.Task('T2_t5_mem0', length=1, delay_cost=1)
	S += T2_t5_mem0 >= 43
	T2_t5_mem0 += MM_MEM[0]

	T2_t5_mem1 = S.Task('T2_t5_mem1', length=1, delay_cost=1)
	S += T2_t5_mem1 >= 43
	T2_t5_mem1 += MM_MEM[1]

	T9_t1 = S.Task('T9_t1', length=9, delay_cost=1)
	S += T9_t1 >= 43
	T9_t1 += MM[0]

	T11_t3 = S.Task('T11_t3', length=2, delay_cost=1)
	S += T11_t3 >= 44
	T11_t3 += MAS[0]

	T14_t0 = S.Task('T14_t0', length=9, delay_cost=1)
	S += T14_t0 >= 44
	T14_t0 += MM[0]

	T2_t5 = S.Task('T2_t5', length=2, delay_cost=1)
	S += T2_t5 >= 44
	T2_t5 += MAS[1]

	T4_t5_in = S.Task('T4_t5_in', length=1, delay_cost=1)
	S += T4_t5_in >= 44
	T4_t5_in += MAS_in[0]

	T4_t5_mem0 = S.Task('T4_t5_mem0', length=1, delay_cost=1)
	S += T4_t5_mem0 >= 44
	T4_t5_mem0 += MM_MEM[0]

	T4_t5_mem1 = S.Task('T4_t5_mem1', length=1, delay_cost=1)
	S += T4_t5_mem1 >= 44
	T4_t5_mem1 += MM_MEM[1]

	T8_t0_in = S.Task('T8_t0_in', length=1, delay_cost=1)
	S += T8_t0_in >= 44
	T8_t0_in += MM_in[0]

	T8_t0_mem0 = S.Task('T8_t0_mem0', length=1, delay_cost=1)
	S += T8_t0_mem0 >= 44
	T8_t0_mem0 += MAIN_MEM_r[0]

	T8_t0_mem1 = S.Task('T8_t0_mem1', length=1, delay_cost=1)
	S += T8_t0_mem1 >= 44
	T8_t0_mem1 += MAS_MEM[3]

	T9_t3_in = S.Task('T9_t3_in', length=1, delay_cost=1)
	S += T9_t3_in >= 44
	T9_t3_in += MAS_in[1]

	T9_t3_mem0 = S.Task('T9_t3_mem0', length=1, delay_cost=1)
	S += T9_t3_mem0 >= 44
	T9_t3_mem0 += MAS_MEM[2]

	T9_t3_mem1 = S.Task('T9_t3_mem1', length=1, delay_cost=1)
	S += T9_t3_mem1 >= 44
	T9_t3_mem1 += MAS_MEM[1]

	T21_in = S.Task('T21_in', length=1, delay_cost=1)
	S += T21_in >= 45
	T21_in += MAS_in[1]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 45
	T21_mem0 += MM_MEM[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 45
	T21_mem1 += MAS_MEM[3]

	T4_t5 = S.Task('T4_t5', length=2, delay_cost=1)
	S += T4_t5 >= 45
	T4_t5 += MAS[0]

	T8_t0 = S.Task('T8_t0', length=9, delay_cost=1)
	S += T8_t0 >= 45
	T8_t0 += MM[0]

	T8_t3_in = S.Task('T8_t3_in', length=1, delay_cost=1)
	S += T8_t3_in >= 45
	T8_t3_in += MAS_in[0]

	T8_t3_mem0 = S.Task('T8_t3_mem0', length=1, delay_cost=1)
	S += T8_t3_mem0 >= 45
	T8_t3_mem0 += MAS_MEM[2]

	T8_t3_mem1 = S.Task('T8_t3_mem1', length=1, delay_cost=1)
	S += T8_t3_mem1 >= 45
	T8_t3_mem1 += MAS_MEM[1]

	T9_t3 = S.Task('T9_t3', length=2, delay_cost=1)
	S += T9_t3 >= 45
	T9_t3 += MAS[1]

	T11_t1_in = S.Task('T11_t1_in', length=1, delay_cost=1)
	S += T11_t1_in >= 46
	T11_t1_in += MM_in[0]

	T11_t1_mem0 = S.Task('T11_t1_mem0', length=1, delay_cost=1)
	S += T11_t1_mem0 >= 46
	T11_t1_mem0 += MAIN_MEM_r[0]

	T11_t1_mem1 = S.Task('T11_t1_mem1', length=1, delay_cost=1)
	S += T11_t1_mem1 >= 46
	T11_t1_mem1 += MAS_MEM[3]

	T21 = S.Task('T21', length=2, delay_cost=1)
	S += T21 >= 46
	T21 += MAS[1]

	T41_in = S.Task('T41_in', length=1, delay_cost=1)
	S += T41_in >= 46
	T41_in += MAS_in[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 46
	T41_mem0 += MM_MEM[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 46
	T41_mem1 += MAS_MEM[1]

	T8_t3 = S.Task('T8_t3', length=2, delay_cost=1)
	S += T8_t3 >= 46
	T8_t3 += MAS[0]

	T11_t1 = S.Task('T11_t1', length=9, delay_cost=1)
	S += T11_t1 >= 47
	T11_t1 += MM[0]

	T16_t2_in = S.Task('T16_t2_in', length=1, delay_cost=1)
	S += T16_t2_in >= 47
	T16_t2_in += MAS_in[0]

	T16_t2_mem0 = S.Task('T16_t2_mem0', length=1, delay_cost=1)
	S += T16_t2_mem0 >= 47
	T16_t2_mem0 += MAS_MEM[2]

	T16_t2_mem1 = S.Task('T16_t2_mem1', length=1, delay_cost=1)
	S += T16_t2_mem1 >= 47
	T16_t2_mem1 += MAS_MEM[1]

	T41 = S.Task('T41', length=2, delay_cost=1)
	S += T41 >= 47
	T41 += MAS[0]

	T9_t0_in = S.Task('T9_t0_in', length=1, delay_cost=1)
	S += T9_t0_in >= 47
	T9_t0_in += MM_in[0]

	T9_t0_mem0 = S.Task('T9_t0_mem0', length=1, delay_cost=1)
	S += T9_t0_mem0 >= 47
	T9_t0_mem0 += MAIN_MEM_r[0]

	T9_t0_mem1 = S.Task('T9_t0_mem1', length=1, delay_cost=1)
	S += T9_t0_mem1 >= 47
	T9_t0_mem1 += MAS_MEM[3]

	T131_in = S.Task('T131_in', length=1, delay_cost=1)
	S += T131_in >= 48
	T131_in += MAS_in[1]

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 48
	T131_mem0 += MAS_MEM[0]

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 48
	T131_mem1 += MAS_MEM[3]

	T16_t2 = S.Task('T16_t2', length=2, delay_cost=1)
	S += T16_t2 >= 48
	T16_t2 += MAS[0]

	T9_t0 = S.Task('T9_t0', length=9, delay_cost=1)
	S += T9_t0 >= 48
	T9_t0 += MM[0]

	T100_in = S.Task('T100_in', length=1, delay_cost=1)
	S += T100_in >= 49
	T100_in += MAS_in[1]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 49
	T100_mem0 += MM_MEM[0]

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 49
	T100_mem1 += MM_MEM[1]

	T121_in = S.Task('T121_in', length=1, delay_cost=1)
	S += T121_in >= 49
	T121_in += MAS_in[0]

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	S += T121_mem0 >= 49
	T121_mem0 += MAS_MEM[0]

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	S += T121_mem1 >= 49
	T121_mem1 += MAS_MEM[3]

	T131 = S.Task('T131', length=2, delay_cost=1)
	S += T131 >= 49
	T131 += MAS[1]

	T100 = S.Task('T100', length=2, delay_cost=1)
	S += T100 >= 50
	T100 += MAS[1]

	T10_t5_in = S.Task('T10_t5_in', length=1, delay_cost=1)
	S += T10_t5_in >= 50
	T10_t5_in += MAS_in[1]

	T10_t5_mem0 = S.Task('T10_t5_mem0', length=1, delay_cost=1)
	S += T10_t5_mem0 >= 50
	T10_t5_mem0 += MM_MEM[0]

	T10_t5_mem1 = S.Task('T10_t5_mem1', length=1, delay_cost=1)
	S += T10_t5_mem1 >= 50
	T10_t5_mem1 += MM_MEM[1]

	T121 = S.Task('T121', length=2, delay_cost=1)
	S += T121 >= 50
	T121 += MAS[0]

	T14_t1_in = S.Task('T14_t1_in', length=1, delay_cost=1)
	S += T14_t1_in >= 50
	T14_t1_in += MM_in[0]

	T14_t1_mem0 = S.Task('T14_t1_mem0', length=1, delay_cost=1)
	S += T14_t1_mem0 >= 50
	T14_t1_mem0 += MAS_MEM[2]

	T14_t1_mem1 = S.Task('T14_t1_mem1', length=1, delay_cost=1)
	S += T14_t1_mem1 >= 50
	T14_t1_mem1 += MAS_MEM[3]

	T10_t5 = S.Task('T10_t5', length=2, delay_cost=1)
	S += T10_t5 >= 51
	T10_t5 += MAS[1]

	T14_t1 = S.Task('T14_t1', length=9, delay_cost=1)
	S += T14_t1 >= 51
	T14_t1 += MM[0]

	T24_t3_in = S.Task('T24_t3_in', length=1, delay_cost=1)
	S += T24_t3_in >= 51
	T24_t3_in += MAS_in[0]

	T24_t3_mem0 = S.Task('T24_t3_mem0', length=1, delay_cost=1)
	S += T24_t3_mem0 >= 51
	T24_t3_mem0 += MAS_MEM[2]

	T24_t3_mem1 = S.Task('T24_t3_mem1', length=1, delay_cost=1)
	S += T24_t3_mem1 >= 51
	T24_t3_mem1 += MAS_MEM[1]

	T9_t4_in = S.Task('T9_t4_in', length=1, delay_cost=1)
	S += T9_t4_in >= 51
	T9_t4_in += MM_in[0]

	T9_t4_mem0 = S.Task('T9_t4_mem0', length=1, delay_cost=1)
	S += T9_t4_mem0 >= 51
	T9_t4_mem0 += MAS_MEM[0]

	T9_t4_mem1 = S.Task('T9_t4_mem1', length=1, delay_cost=1)
	S += T9_t4_mem1 >= 51
	T9_t4_mem1 += MAS_MEM[3]

	T210_in = S.Task('T210_in', length=1, delay_cost=1)
	S += T210_in >= 52
	T210_in += MAS_in[0]

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	S += T210_mem0 >= 52
	T210_mem0 += MAS_MEM[2]

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	S += T210_mem1 >= 52
	T210_mem1 += MAS_MEM[3]

	T24_t3 = S.Task('T24_t3', length=2, delay_cost=1)
	S += T24_t3 >= 52
	T24_t3 += MAS[0]

	T8_t4_in = S.Task('T8_t4_in', length=1, delay_cost=1)
	S += T8_t4_in >= 52
	T8_t4_in += MM_in[0]

	T8_t4_mem0 = S.Task('T8_t4_mem0', length=1, delay_cost=1)
	S += T8_t4_mem0 >= 52
	T8_t4_mem0 += MAS_MEM[0]

	T8_t4_mem1 = S.Task('T8_t4_mem1', length=1, delay_cost=1)
	S += T8_t4_mem1 >= 52
	T8_t4_mem1 += MAS_MEM[1]

	T9_t4 = S.Task('T9_t4', length=9, delay_cost=1)
	S += T9_t4 >= 52
	T9_t4 += MM[0]

	T10_t4_in = S.Task('T10_t4_in', length=1, delay_cost=1)
	S += T10_t4_in >= 53
	T10_t4_in += MM_in[0]

	T10_t4_mem0 = S.Task('T10_t4_mem0', length=1, delay_cost=1)
	S += T10_t4_mem0 >= 53
	T10_t4_mem0 += MAS_MEM[0]

	T10_t4_mem1 = S.Task('T10_t4_mem1', length=1, delay_cost=1)
	S += T10_t4_mem1 >= 53
	T10_t4_mem1 += MAS_MEM[3]

	T210 = S.Task('T210', length=2, delay_cost=1)
	S += T210 >= 53
	T210 += MAS[0]

	T8_t4 = S.Task('T8_t4', length=9, delay_cost=1)
	S += T8_t4 >= 53
	T8_t4 += MM[0]

	T10_t4 = S.Task('T10_t4', length=9, delay_cost=1)
	S += T10_t4 >= 54
	T10_t4 += MM[0]

	T8_t5_in = S.Task('T8_t5_in', length=1, delay_cost=1)
	S += T8_t5_in >= 54
	T8_t5_in += MAS_in[0]

	T8_t5_mem0 = S.Task('T8_t5_mem0', length=1, delay_cost=1)
	S += T8_t5_mem0 >= 54
	T8_t5_mem0 += MM_MEM[0]

	T8_t5_mem1 = S.Task('T8_t5_mem1', length=1, delay_cost=1)
	S += T8_t5_mem1 >= 54
	T8_t5_mem1 += MM_MEM[1]

	T11_t5_in = S.Task('T11_t5_in', length=1, delay_cost=1)
	S += T11_t5_in >= 55
	T11_t5_in += MAS_in[0]

	T11_t5_mem0 = S.Task('T11_t5_mem0', length=1, delay_cost=1)
	S += T11_t5_mem0 >= 55
	T11_t5_mem0 += MM_MEM[0]

	T11_t5_mem1 = S.Task('T11_t5_mem1', length=1, delay_cost=1)
	S += T11_t5_mem1 >= 55
	T11_t5_mem1 += MM_MEM[1]

	T8_t5 = S.Task('T8_t5', length=2, delay_cost=1)
	S += T8_t5 >= 55
	T8_t5 += MAS[0]

	T11_t5 = S.Task('T11_t5', length=2, delay_cost=1)
	S += T11_t5 >= 56
	T11_t5 += MAS[0]

	T90_in = S.Task('T90_in', length=1, delay_cost=1)
	S += T90_in >= 56
	T90_in += MAS_in[0]

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	S += T90_mem0 >= 56
	T90_mem0 += MM_MEM[0]

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	S += T90_mem1 >= 56
	T90_mem1 += MM_MEM[1]

	T110_in = S.Task('T110_in', length=1, delay_cost=1)
	S += T110_in >= 57
	T110_in += MAS_in[0]

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	S += T110_mem0 >= 57
	T110_mem0 += MM_MEM[0]

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	S += T110_mem1 >= 57
	T110_mem1 += MM_MEM[1]

	T90 = S.Task('T90', length=2, delay_cost=1)
	S += T90 >= 57
	T90 += MAS[0]

	T110 = S.Task('T110', length=2, delay_cost=1)
	S += T110 >= 58
	T110 += MAS[0]

	T17_t0_in = S.Task('T17_t0_in', length=1, delay_cost=1)
	S += T17_t0_in >= 58
	T17_t0_in += MM_in[0]

	T17_t0_mem0 = S.Task('T17_t0_mem0', length=1, delay_cost=1)
	S += T17_t0_mem0 >= 58
	T17_t0_mem0 += MAS_MEM[0]

	T17_t0_mem1 = S.Task('T17_t0_mem1', length=1, delay_cost=1)
	S += T17_t0_mem1 >= 58
	T17_t0_mem1 += MAS_MEM[3]

	T180_in = S.Task('T180_in', length=1, delay_cost=1)
	S += T180_in >= 58
	T180_in += MAS_in[0]

	T180_mem0 = S.Task('T180_mem0', length=1, delay_cost=1)
	S += T180_mem0 >= 58
	T180_mem0 += MAS_MEM[2]

	T180_mem1 = S.Task('T180_mem1', length=1, delay_cost=1)
	S += T180_mem1 >= 58
	T180_mem1 += MAS_MEM[1]

	T9_t5_in = S.Task('T9_t5_in', length=1, delay_cost=1)
	S += T9_t5_in >= 58
	T9_t5_in += MAS_in[1]

	T9_t5_mem0 = S.Task('T9_t5_mem0', length=1, delay_cost=1)
	S += T9_t5_mem0 >= 58
	T9_t5_mem0 += MM_MEM[0]

	T9_t5_mem1 = S.Task('T9_t5_mem1', length=1, delay_cost=1)
	S += T9_t5_mem1 >= 58
	T9_t5_mem1 += MM_MEM[1]

	T140_in = S.Task('T140_in', length=1, delay_cost=1)
	S += T140_in >= 59
	T140_in += MAS_in[1]

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 59
	T140_mem0 += MM_MEM[0]

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 59
	T140_mem1 += MM_MEM[1]

	T17_t0 = S.Task('T17_t0', length=9, delay_cost=1)
	S += T17_t0 >= 59
	T17_t0 += MM[0]

	T180 = S.Task('T180', length=2, delay_cost=1)
	S += T180 >= 59
	T180 += MAS[0]

	T190_in = S.Task('T190_in', length=1, delay_cost=1)
	S += T190_in >= 59
	T190_in += MAS_in[0]

	T190_mem0 = S.Task('T190_mem0', length=1, delay_cost=1)
	S += T190_mem0 >= 59
	T190_mem0 += MAS_MEM[2]

	T190_mem1 = S.Task('T190_mem1', length=1, delay_cost=1)
	S += T190_mem1 >= 59
	T190_mem1 += MAS_MEM[1]

	T24_t0_in = S.Task('T24_t0_in', length=1, delay_cost=1)
	S += T24_t0_in >= 59
	T24_t0_in += MM_in[0]

	T24_t0_mem0 = S.Task('T24_t0_mem0', length=1, delay_cost=1)
	S += T24_t0_mem0 >= 59
	T24_t0_mem0 += MAS_MEM[0]

	T24_t0_mem1 = S.Task('T24_t0_mem1', length=1, delay_cost=1)
	S += T24_t0_mem1 >= 59
	T24_t0_mem1 += MAS_MEM[3]

	T9_t5 = S.Task('T9_t5', length=2, delay_cost=1)
	S += T9_t5 >= 59
	T9_t5 += MAS[1]

	T140 = S.Task('T140', length=2, delay_cost=1)
	S += T140 >= 60
	T140 += MAS[1]

	T190 = S.Task('T190', length=2, delay_cost=1)
	S += T190 >= 60
	T190 += MAS[0]

	T20_t0_in = S.Task('T20_t0_in', length=1, delay_cost=1)
	S += T20_t0_in >= 60
	T20_t0_in += MM_in[0]

	T20_t0_mem0 = S.Task('T20_t0_mem0', length=1, delay_cost=1)
	S += T20_t0_mem0 >= 60
	T20_t0_mem0 += MAS_MEM[2]

	T20_t0_mem1 = S.Task('T20_t0_mem1', length=1, delay_cost=1)
	S += T20_t0_mem1 >= 60
	T20_t0_mem1 += MAS_MEM[1]

	T24_t0 = S.Task('T24_t0', length=9, delay_cost=1)
	S += T24_t0 >= 60
	T24_t0 += MM[0]

	T91_in = S.Task('T91_in', length=1, delay_cost=1)
	S += T91_in >= 60
	T91_in += MAS_in[0]

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	S += T91_mem0 >= 60
	T91_mem0 += MM_MEM[0]

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	S += T91_mem1 >= 60
	T91_mem1 += MAS_MEM[3]

	T20_t0 = S.Task('T20_t0', length=9, delay_cost=1)
	S += T20_t0 >= 61
	T20_t0 += MM[0]

	T91 = S.Task('T91', length=2, delay_cost=1)
	S += T91 >= 61
	T91 += MAS[0]

	Z3_t0_in = S.Task('Z3_t0_in', length=1, delay_cost=1)
	S += Z3_t0_in >= 61
	Z3_t0_in += MM_in[0]

	Z3_t0_mem0 = S.Task('Z3_t0_mem0', length=1, delay_cost=1)
	S += Z3_t0_mem0 >= 61
	Z3_t0_mem0 += MAIN_MEM_r[0]

	Z3_t0_mem1 = S.Task('Z3_t0_mem1', length=1, delay_cost=1)
	S += Z3_t0_mem1 >= 61
	Z3_t0_mem1 += MAS_MEM[3]

	T101_in = S.Task('T101_in', length=1, delay_cost=1)
	S += T101_in >= 62
	T101_in += MAS_in[0]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 62
	T101_mem0 += MM_MEM[0]

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 62
	T101_mem1 += MAS_MEM[3]

	T181_in = S.Task('T181_in', length=1, delay_cost=1)
	S += T181_in >= 62
	T181_in += MAS_in[1]

	T181_mem0 = S.Task('T181_mem0', length=1, delay_cost=1)
	S += T181_mem0 >= 62
	T181_mem0 += MAS_MEM[0]

	T181_mem1 = S.Task('T181_mem1', length=1, delay_cost=1)
	S += T181_mem1 >= 62
	T181_mem1 += MAS_MEM[1]

	Z3_t0 = S.Task('Z3_t0', length=9, delay_cost=1)
	S += Z3_t0 >= 62
	Z3_t0 += MM[0]

	T101 = S.Task('T101', length=2, delay_cost=1)
	S += T101 >= 63
	T101 += MAS[0]

	T14_t5_in = S.Task('T14_t5_in', length=1, delay_cost=1)
	S += T14_t5_in >= 63
	T14_t5_in += MAS_in[0]

	T14_t5_mem0 = S.Task('T14_t5_mem0', length=1, delay_cost=1)
	S += T14_t5_mem0 >= 63
	T14_t5_mem0 += MM_MEM[0]

	T14_t5_mem1 = S.Task('T14_t5_mem1', length=1, delay_cost=1)
	S += T14_t5_mem1 >= 63
	T14_t5_mem1 += MM_MEM[1]

	T181 = S.Task('T181', length=2, delay_cost=1)
	S += T181 >= 63
	T181 += MAS[1]

	T14_t5 = S.Task('T14_t5', length=2, delay_cost=1)
	S += T14_t5 >= 64
	T14_t5 += MAS[0]

	T211_in = S.Task('T211_in', length=1, delay_cost=1)
	S += T211_in >= 64
	T211_in += MAS_in[0]

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	S += T211_mem0 >= 64
	T211_mem0 += MAS_MEM[2]

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	S += T211_mem1 >= 64
	T211_mem1 += MAS_MEM[1]

	T111_in = S.Task('T111_in', length=1, delay_cost=1)
	S += T111_in >= 65
	T111_in += MAS_in[1]

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	S += T111_mem0 >= 65
	T111_mem0 += MM_MEM[0]

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	S += T111_mem1 >= 65
	T111_mem1 += MAS_MEM[1]

	T17_t2_in = S.Task('T17_t2_in', length=1, delay_cost=1)
	S += T17_t2_in >= 65
	T17_t2_in += MAS_in[0]

	T17_t2_mem0 = S.Task('T17_t2_mem0', length=1, delay_cost=1)
	S += T17_t2_mem0 >= 65
	T17_t2_mem0 += MAS_MEM[0]

	T17_t2_mem1 = S.Task('T17_t2_mem1', length=1, delay_cost=1)
	S += T17_t2_mem1 >= 65
	T17_t2_mem1 += MAS_MEM[3]

	T211 = S.Task('T211', length=2, delay_cost=1)
	S += T211 >= 65
	T211 += MAS[0]

	T111 = S.Task('T111', length=2, delay_cost=1)
	S += T111 >= 66
	T111 += MAS[1]

	T141_in = S.Task('T141_in', length=1, delay_cost=1)
	S += T141_in >= 66
	T141_in += MAS_in[0]

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 66
	T141_mem0 += MM_MEM[0]

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 66
	T141_mem1 += MAS_MEM[1]

	T16_t3_in = S.Task('T16_t3_in', length=1, delay_cost=1)
	S += T16_t3_in >= 66
	T16_t3_in += MAS_in[1]

	T16_t3_mem0 = S.Task('T16_t3_mem0', length=1, delay_cost=1)
	S += T16_t3_mem0 >= 66
	T16_t3_mem0 += MAS_MEM[0]

	T16_t3_mem1 = S.Task('T16_t3_mem1', length=1, delay_cost=1)
	S += T16_t3_mem1 >= 66
	T16_t3_mem1 += MAS_MEM[3]

	T17_t2 = S.Task('T17_t2', length=2, delay_cost=1)
	S += T17_t2 >= 66
	T17_t2 += MAS[0]

	T141 = S.Task('T141', length=2, delay_cost=1)
	S += T141 >= 67
	T141 += MAS[0]

	T16_t3 = S.Task('T16_t3', length=2, delay_cost=1)
	S += T16_t3 >= 67
	T16_t3 += MAS[1]

	T24_t1_in = S.Task('T24_t1_in', length=1, delay_cost=1)
	S += T24_t1_in >= 67
	T24_t1_in += MM_in[0]

	T24_t1_mem0 = S.Task('T24_t1_mem0', length=1, delay_cost=1)
	S += T24_t1_mem0 >= 67
	T24_t1_mem0 += MAS_MEM[2]

	T24_t1_mem1 = S.Task('T24_t1_mem1', length=1, delay_cost=1)
	S += T24_t1_mem1 >= 67
	T24_t1_mem1 += MAS_MEM[1]

	T24_t2_in = S.Task('T24_t2_in', length=1, delay_cost=1)
	S += T24_t2_in >= 67
	T24_t2_in += MAS_in[0]

	T24_t2_mem0 = S.Task('T24_t2_mem0', length=1, delay_cost=1)
	S += T24_t2_mem0 >= 67
	T24_t2_mem0 += MAS_MEM[0]

	T24_t2_mem1 = S.Task('T24_t2_mem1', length=1, delay_cost=1)
	S += T24_t2_mem1 >= 67
	T24_t2_mem1 += MAS_MEM[3]

	T24_t1 = S.Task('T24_t1', length=9, delay_cost=1)
	S += T24_t1 >= 68
	T24_t1 += MM[0]

	T24_t2 = S.Task('T24_t2', length=2, delay_cost=1)
	S += T24_t2 >= 68
	T24_t2 += MAS[0]


	# new tasks
	T80 = S.Task('T80', length=2, delay_cost=1)
	T80 += alt(MAS)
	T80_in = S.Task('T80_in', length=1, delay_cost=1)
	T80_in += alt(MAS_in)
	S += T80_in*MAS_in[0]<=T80*MAS[0]

	S += T80_in*MAS_in[1]<=T80*MAS[1]

	S += T80<59

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	T80_mem0 += MM_MEM[0]
	S += 53 < T80_mem0
	S += T80_mem0 <= T80

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	T80_mem1 += MM_MEM[1]
	S += 50 < T80_mem1
	S += T80_mem1 <= T80

	T11_t4 = S.Task('T11_t4', length=9, delay_cost=1)
	T11_t4 += alt(MM)
	T11_t4_in = S.Task('T11_t4_in', length=1, delay_cost=1)
	T11_t4_in += alt(MM_in)
	S += T11_t4_in*MM_in[0]<=T11_t4*MM[0]
	S += T11_t4<66

	T11_t4_mem0 = S.Task('T11_t4_mem0', length=1, delay_cost=1)
	T11_t4_mem0 += MAS_MEM[0]
	S += 2 < T11_t4_mem0
	S += T11_t4_mem0 <= T11_t4

	T11_t4_mem1 = S.Task('T11_t4_mem1', length=1, delay_cost=1)
	T11_t4_mem1 += MAS_MEM[1]
	S += 45 < T11_t4_mem1
	S += T11_t4_mem1 <= T11_t4

	T14_t2 = S.Task('T14_t2', length=2, delay_cost=1)
	T14_t2 += alt(MAS)
	T14_t2_in = S.Task('T14_t2_in', length=1, delay_cost=1)
	T14_t2_in += alt(MAS_in)
	S += T14_t2_in*MAS_in[0]<=T14_t2*MAS[0]

	S += T14_t2_in*MAS_in[1]<=T14_t2*MAS[1]

	S += T14_t2<1000

	T14_t2_mem0 = S.Task('T14_t2_mem0', length=1, delay_cost=1)
	T14_t2_mem0 += MAS_MEM[0]
	S += 42 < T14_t2_mem0
	S += T14_t2_mem0 <= T14_t2

	T14_t2_mem1 = S.Task('T14_t2_mem1', length=1, delay_cost=1)
	T14_t2_mem1 += MAS_MEM[3]
	S += 50 < T14_t2_mem1
	S += T14_t2_mem1 <= T14_t2

	T14_t3 = S.Task('T14_t3', length=2, delay_cost=1)
	T14_t3 += alt(MAS)
	T14_t3_in = S.Task('T14_t3_in', length=1, delay_cost=1)
	T14_t3_in += alt(MAS_in)
	S += T14_t3_in*MAS_in[0]<=T14_t3*MAS[0]

	S += T14_t3_in*MAS_in[1]<=T14_t3*MAS[1]

	S += T14_t3<1000

	T14_t3_mem0 = S.Task('T14_t3_mem0', length=1, delay_cost=1)
	T14_t3_mem0 += MAS_MEM[0]
	S += 42 < T14_t3_mem0
	S += T14_t3_mem0 <= T14_t3

	T14_t3_mem1 = S.Task('T14_t3_mem1', length=1, delay_cost=1)
	T14_t3_mem1 += MAS_MEM[3]
	S += 50 < T14_t3_mem1
	S += T14_t3_mem1 <= T14_t3

	T81 = S.Task('T81', length=2, delay_cost=1)
	T81 += alt(MAS)
	T81_in = S.Task('T81_in', length=1, delay_cost=1)
	T81_in += alt(MAS_in)
	S += T81_in*MAS_in[0]<=T81*MAS[0]

	S += T81_in*MAS_in[1]<=T81*MAS[1]

	S += T81<66

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	T81_mem0 += MM_MEM[0]
	S += 61 < T81_mem0
	S += T81_mem0 <= T81

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	T81_mem1 += MAS_MEM[1]
	S += 56 < T81_mem1
	S += T81_mem1 <= T81

	T14_t4 = S.Task('T14_t4', length=9, delay_cost=1)
	T14_t4 += alt(MM)
	T14_t4_in = S.Task('T14_t4_in', length=1, delay_cost=1)
	T14_t4_in += alt(MM_in)
	S += T14_t4_in*MM_in[0]<=T14_t4*MM[0]
	S += T14_t4<67

	T14_t4_mem0 = S.Task('T14_t4_mem0', length=1, delay_cost=1)
	T14_t4_mem0 += alt(MAS_MEM)
	S += (T14_t2*MAS[0])-1 < T14_t4_mem0*MAS_MEM[0]
	S += (T14_t2*MAS[1])-1 < T14_t4_mem0*MAS_MEM[2]
	S += T14_t4_mem0 <= T14_t4

	T14_t4_mem1 = S.Task('T14_t4_mem1', length=1, delay_cost=1)
	T14_t4_mem1 += alt(MAS_MEM)
	S += (T14_t3*MAS[0])-1 < T14_t4_mem1*MAS_MEM[1]
	S += (T14_t3*MAS[1])-1 < T14_t4_mem1*MAS_MEM[3]
	S += T14_t4_mem1 <= T14_t4

	T16_t0 = S.Task('T16_t0', length=9, delay_cost=1)
	T16_t0 += alt(MM)
	T16_t0_in = S.Task('T16_t0_in', length=1, delay_cost=1)
	T16_t0_in += alt(MM_in)
	S += T16_t0_in*MM_in[0]<=T16_t0*MM[0]
	S += T16_t0<1000

	T16_t0_mem0 = S.Task('T16_t0_mem0', length=1, delay_cost=1)
	T16_t0_mem0 += MAS_MEM[2]
	S += 44 < T16_t0_mem0
	S += T16_t0_mem0 <= T16_t0

	T16_t0_mem1 = S.Task('T16_t0_mem1', length=1, delay_cost=1)
	T16_t0_mem1 += alt(MAS_MEM)
	S += (T80*MAS[0])-1 < T16_t0_mem1*MAS_MEM[1]
	S += (T80*MAS[1])-1 < T16_t0_mem1*MAS_MEM[3]
	S += T16_t0_mem1 <= T16_t0

	T16_t1 = S.Task('T16_t1', length=9, delay_cost=1)
	T16_t1 += alt(MM)
	T16_t1_in = S.Task('T16_t1_in', length=1, delay_cost=1)
	T16_t1_in += alt(MM_in)
	S += T16_t1_in*MM_in[0]<=T16_t1*MM[0]
	S += T16_t1<1000

	T16_t1_mem0 = S.Task('T16_t1_mem0', length=1, delay_cost=1)
	T16_t1_mem0 += MAS_MEM[0]
	S += 41 < T16_t1_mem0
	S += T16_t1_mem0 <= T16_t1

	T16_t1_mem1 = S.Task('T16_t1_mem1', length=1, delay_cost=1)
	T16_t1_mem1 += alt(MAS_MEM)
	S += (T81*MAS[0])-1 < T16_t1_mem1*MAS_MEM[1]
	S += (T81*MAS[1])-1 < T16_t1_mem1*MAS_MEM[3]
	S += T16_t1_mem1 <= T16_t1

	T17_t1 = S.Task('T17_t1', length=9, delay_cost=1)
	T17_t1 += alt(MM)
	T17_t1_in = S.Task('T17_t1_in', length=1, delay_cost=1)
	T17_t1_in += alt(MM_in)
	S += T17_t1_in*MM_in[0]<=T17_t1*MM[0]
	S += T17_t1<1000

	T17_t1_mem0 = S.Task('T17_t1_mem0', length=1, delay_cost=1)
	T17_t1_mem0 += alt(MAS_MEM)
	S += (T81*MAS[0])-1 < T17_t1_mem0*MAS_MEM[0]
	S += (T81*MAS[1])-1 < T17_t1_mem0*MAS_MEM[2]
	S += T17_t1_mem0 <= T17_t1

	T17_t1_mem1 = S.Task('T17_t1_mem1', length=1, delay_cost=1)
	T17_t1_mem1 += MAS_MEM[3]
	S += 31 < T17_t1_mem1
	S += T17_t1_mem1 <= T17_t1

	T191 = S.Task('T191', length=2, delay_cost=1)
	T191 += alt(MAS)
	T191_in = S.Task('T191_in', length=1, delay_cost=1)
	T191_in += alt(MAS_in)
	S += T191_in*MAS_in[0]<=T191*MAS[0]

	S += T191_in*MAS_in[1]<=T191*MAS[1]

	S += T191<1000

	T191_mem0 = S.Task('T191_mem0', length=1, delay_cost=1)
	T191_mem0 += MAS_MEM[0]
	S += 43 < T191_mem0
	S += T191_mem0 <= T191

	T191_mem1 = S.Task('T191_mem1', length=1, delay_cost=1)
	T191_mem1 += MAS_MEM[1]
	S += 62 < T191_mem1
	S += T191_mem1 <= T191

	T16_t4 = S.Task('T16_t4', length=9, delay_cost=1)
	T16_t4 += alt(MM)
	T16_t4_in = S.Task('T16_t4_in', length=1, delay_cost=1)
	T16_t4_in += alt(MM_in)
	S += T16_t4_in*MM_in[0]<=T16_t4*MM[0]
	T16_t4_mem0 = S.Task('T16_t4_mem0', length=1, delay_cost=1)
	T16_t4_mem0 += MAS_MEM[0]
	S += 49 < T16_t4_mem0
	S += T16_t4_mem0 <= T16_t4

	T16_t4_mem1 = S.Task('T16_t4_mem1', length=1, delay_cost=1)
	T16_t4_mem1 += MAS_MEM[3]
	S += 68 < T16_t4_mem1
	S += T16_t4_mem1 <= T16_t4

	T160 = S.Task('T160', length=2, delay_cost=1)
	T160 += alt(MAS)
	T160_in = S.Task('T160_in', length=1, delay_cost=1)
	T160_in += alt(MAS_in)
	S += T160_in*MAS_in[0]<=T160*MAS[0]

	S += T160_in*MAS_in[1]<=T160*MAS[1]

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	T160_mem0 += alt(MM_MEM)
	S += (T16_t0*MM[0])-1 < T160_mem0*MM_MEM[0]
	S += T160_mem0 <= T160

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	T160_mem1 += alt(MM_MEM)
	S += (T16_t1*MM[0])-1 < T160_mem1*MM_MEM[1]
	S += T160_mem1 <= T160

	T16_t5 = S.Task('T16_t5', length=2, delay_cost=1)
	T16_t5 += alt(MAS)
	T16_t5_in = S.Task('T16_t5_in', length=1, delay_cost=1)
	T16_t5_in += alt(MAS_in)
	S += T16_t5_in*MAS_in[0]<=T16_t5*MAS[0]

	S += T16_t5_in*MAS_in[1]<=T16_t5*MAS[1]

	T16_t5_mem0 = S.Task('T16_t5_mem0', length=1, delay_cost=1)
	T16_t5_mem0 += alt(MM_MEM)
	S += (T16_t0*MM[0])-1 < T16_t5_mem0*MM_MEM[0]
	S += T16_t5_mem0 <= T16_t5

	T16_t5_mem1 = S.Task('T16_t5_mem1', length=1, delay_cost=1)
	T16_t5_mem1 += alt(MM_MEM)
	S += (T16_t1*MM[0])-1 < T16_t5_mem1*MM_MEM[1]
	S += T16_t5_mem1 <= T16_t5

	T17_t4 = S.Task('T17_t4', length=9, delay_cost=1)
	T17_t4 += alt(MM)
	T17_t4_in = S.Task('T17_t4_in', length=1, delay_cost=1)
	T17_t4_in += alt(MM_in)
	S += T17_t4_in*MM_in[0]<=T17_t4*MM[0]
	T17_t4_mem0 = S.Task('T17_t4_mem0', length=1, delay_cost=1)
	T17_t4_mem0 += MAS_MEM[0]
	S += 67 < T17_t4_mem0
	S += T17_t4_mem0 <= T17_t4

	T17_t4_mem1 = S.Task('T17_t4_mem1', length=1, delay_cost=1)
	T17_t4_mem1 += MAS_MEM[1]
	S += 33 < T17_t4_mem1
	S += T17_t4_mem1 <= T17_t4

	T170 = S.Task('T170', length=2, delay_cost=1)
	T170 += alt(MAS)
	T170_in = S.Task('T170_in', length=1, delay_cost=1)
	T170_in += alt(MAS_in)
	S += T170_in*MAS_in[0]<=T170*MAS[0]

	S += T170_in*MAS_in[1]<=T170*MAS[1]

	T170_mem0 = S.Task('T170_mem0', length=1, delay_cost=1)
	T170_mem0 += MM_MEM[0]
	S += 67 < T170_mem0
	S += T170_mem0 <= T170

	T170_mem1 = S.Task('T170_mem1', length=1, delay_cost=1)
	T170_mem1 += alt(MM_MEM)
	S += (T17_t1*MM[0])-1 < T170_mem1*MM_MEM[1]
	S += T170_mem1 <= T170

	T17_t5 = S.Task('T17_t5', length=2, delay_cost=1)
	T17_t5 += alt(MAS)
	T17_t5_in = S.Task('T17_t5_in', length=1, delay_cost=1)
	T17_t5_in += alt(MAS_in)
	S += T17_t5_in*MAS_in[0]<=T17_t5*MAS[0]

	S += T17_t5_in*MAS_in[1]<=T17_t5*MAS[1]

	T17_t5_mem0 = S.Task('T17_t5_mem0', length=1, delay_cost=1)
	T17_t5_mem0 += MM_MEM[0]
	S += 67 < T17_t5_mem0
	S += T17_t5_mem0 <= T17_t5

	T17_t5_mem1 = S.Task('T17_t5_mem1', length=1, delay_cost=1)
	T17_t5_mem1 += alt(MM_MEM)
	S += (T17_t1*MM[0])-1 < T17_t5_mem1*MM_MEM[1]
	S += T17_t5_mem1 <= T17_t5

	T20_t1 = S.Task('T20_t1', length=9, delay_cost=1)
	T20_t1 += alt(MM)
	T20_t1_in = S.Task('T20_t1_in', length=1, delay_cost=1)
	T20_t1_in += alt(MM_in)
	S += T20_t1_in*MM_in[0]<=T20_t1*MM[0]
	T20_t1_mem0 = S.Task('T20_t1_mem0', length=1, delay_cost=1)
	T20_t1_mem0 += MAS_MEM[2]
	S += 31 < T20_t1_mem0
	S += T20_t1_mem0 <= T20_t1

	T20_t1_mem1 = S.Task('T20_t1_mem1', length=1, delay_cost=1)
	T20_t1_mem1 += MAS_MEM[3]
	S += 64 < T20_t1_mem1
	S += T20_t1_mem1 <= T20_t1

	T20_t3 = S.Task('T20_t3', length=2, delay_cost=1)
	T20_t3 += alt(MAS)
	T20_t3_in = S.Task('T20_t3_in', length=1, delay_cost=1)
	T20_t3_in += alt(MAS_in)
	S += T20_t3_in*MAS_in[0]<=T20_t3*MAS[0]

	S += T20_t3_in*MAS_in[1]<=T20_t3*MAS[1]

	T20_t3_mem0 = S.Task('T20_t3_mem0', length=1, delay_cost=1)
	T20_t3_mem0 += MAS_MEM[0]
	S += 60 < T20_t3_mem0
	S += T20_t3_mem0 <= T20_t3

	T20_t3_mem1 = S.Task('T20_t3_mem1', length=1, delay_cost=1)
	T20_t3_mem1 += MAS_MEM[3]
	S += 64 < T20_t3_mem1
	S += T20_t3_mem1 <= T20_t3

	T22_t0 = S.Task('T22_t0', length=2, delay_cost=1)
	T22_t0 += alt(MAS)
	T22_t0_in = S.Task('T22_t0_in', length=1, delay_cost=1)
	T22_t0_in += alt(MAS_in)
	S += T22_t0_in*MAS_in[0]<=T22_t0*MAS[0]

	S += T22_t0_in*MAS_in[1]<=T22_t0*MAS[1]

	T22_t0_mem0 = S.Task('T22_t0_mem0', length=1, delay_cost=1)
	T22_t0_mem0 += MAS_MEM[0]
	S += 54 < T22_t0_mem0
	S += T22_t0_mem0 <= T22_t0

	T22_t0_mem1 = S.Task('T22_t0_mem1', length=1, delay_cost=1)
	T22_t0_mem1 += MAS_MEM[1]
	S += 66 < T22_t0_mem1
	S += T22_t0_mem1 <= T22_t0

	T22_t1 = S.Task('T22_t1', length=2, delay_cost=1)
	T22_t1 += alt(MAS)
	T22_t1_in = S.Task('T22_t1_in', length=1, delay_cost=1)
	T22_t1_in += alt(MAS_in)
	S += T22_t1_in*MAS_in[0]<=T22_t1*MAS[0]

	S += T22_t1_in*MAS_in[1]<=T22_t1*MAS[1]

	T22_t1_mem0 = S.Task('T22_t1_mem0', length=1, delay_cost=1)
	T22_t1_mem0 += MAS_MEM[0]
	S += 54 < T22_t1_mem0
	S += T22_t1_mem0 <= T22_t1

	T22_t1_mem1 = S.Task('T22_t1_mem1', length=1, delay_cost=1)
	T22_t1_mem1 += MAS_MEM[1]
	S += 66 < T22_t1_mem1
	S += T22_t1_mem1 <= T22_t1

	T22_t3 = S.Task('T22_t3', length=9, delay_cost=1)
	T22_t3 += alt(MM)
	T22_t3_in = S.Task('T22_t3_in', length=1, delay_cost=1)
	T22_t3_in += alt(MM_in)
	S += T22_t3_in*MM_in[0]<=T22_t3*MM[0]
	T22_t3_mem0 = S.Task('T22_t3_mem0', length=1, delay_cost=1)
	T22_t3_mem0 += MAS_MEM[0]
	S += 54 < T22_t3_mem0
	S += T22_t3_mem0 <= T22_t3

	T22_t3_mem1 = S.Task('T22_t3_mem1', length=1, delay_cost=1)
	T22_t3_mem1 += MAS_MEM[1]
	S += 66 < T22_t3_mem1
	S += T22_t3_mem1 <= T22_t3

	T23_t0 = S.Task('T23_t0', length=2, delay_cost=1)
	T23_t0 += alt(MAS)
	T23_t0_in = S.Task('T23_t0_in', length=1, delay_cost=1)
	T23_t0_in += alt(MAS_in)
	S += T23_t0_in*MAS_in[0]<=T23_t0*MAS[0]

	S += T23_t0_in*MAS_in[1]<=T23_t0*MAS[1]

	T23_t0_mem0 = S.Task('T23_t0_mem0', length=1, delay_cost=1)
	T23_t0_mem0 += MAS_MEM[0]
	S += 61 < T23_t0_mem0
	S += T23_t0_mem0 <= T23_t0

	T23_t0_mem1 = S.Task('T23_t0_mem1', length=1, delay_cost=1)
	T23_t0_mem1 += alt(MAS_MEM)
	S += (T191*MAS[0])-1 < T23_t0_mem1*MAS_MEM[1]
	S += (T191*MAS[1])-1 < T23_t0_mem1*MAS_MEM[3]
	S += T23_t0_mem1 <= T23_t0

	T23_t1 = S.Task('T23_t1', length=2, delay_cost=1)
	T23_t1 += alt(MAS)
	T23_t1_in = S.Task('T23_t1_in', length=1, delay_cost=1)
	T23_t1_in += alt(MAS_in)
	S += T23_t1_in*MAS_in[0]<=T23_t1*MAS[0]

	S += T23_t1_in*MAS_in[1]<=T23_t1*MAS[1]

	T23_t1_mem0 = S.Task('T23_t1_mem0', length=1, delay_cost=1)
	T23_t1_mem0 += MAS_MEM[0]
	S += 61 < T23_t1_mem0
	S += T23_t1_mem0 <= T23_t1

	T23_t1_mem1 = S.Task('T23_t1_mem1', length=1, delay_cost=1)
	T23_t1_mem1 += alt(MAS_MEM)
	S += (T191*MAS[0])-1 < T23_t1_mem1*MAS_MEM[1]
	S += (T191*MAS[1])-1 < T23_t1_mem1*MAS_MEM[3]
	S += T23_t1_mem1 <= T23_t1

	T23_t3 = S.Task('T23_t3', length=9, delay_cost=1)
	T23_t3 += alt(MM)
	T23_t3_in = S.Task('T23_t3_in', length=1, delay_cost=1)
	T23_t3_in += alt(MM_in)
	S += T23_t3_in*MM_in[0]<=T23_t3*MM[0]
	T23_t3_mem0 = S.Task('T23_t3_mem0', length=1, delay_cost=1)
	T23_t3_mem0 += MAS_MEM[0]
	S += 61 < T23_t3_mem0
	S += T23_t3_mem0 <= T23_t3

	T23_t3_mem1 = S.Task('T23_t3_mem1', length=1, delay_cost=1)
	T23_t3_mem1 += alt(MAS_MEM)
	S += (T191*MAS[0])-1 < T23_t3_mem1*MAS_MEM[1]
	S += (T191*MAS[1])-1 < T23_t3_mem1*MAS_MEM[3]
	S += T23_t3_mem1 <= T23_t3

	T24_t4 = S.Task('T24_t4', length=9, delay_cost=1)
	T24_t4 += alt(MM)
	T24_t4_in = S.Task('T24_t4_in', length=1, delay_cost=1)
	T24_t4_in += alt(MM_in)
	S += T24_t4_in*MM_in[0]<=T24_t4*MM[0]
	T24_t4_mem0 = S.Task('T24_t4_mem0', length=1, delay_cost=1)
	T24_t4_mem0 += MAS_MEM[0]
	S += 69 < T24_t4_mem0
	S += T24_t4_mem0 <= T24_t4

	T24_t4_mem1 = S.Task('T24_t4_mem1', length=1, delay_cost=1)
	T24_t4_mem1 += MAS_MEM[1]
	S += 53 < T24_t4_mem1
	S += T24_t4_mem1 <= T24_t4

	T240 = S.Task('T240', length=2, delay_cost=1)
	T240 += alt(MAS)
	T240_in = S.Task('T240_in', length=1, delay_cost=1)
	T240_in += alt(MAS_in)
	S += T240_in*MAS_in[0]<=T240*MAS[0]

	S += T240_in*MAS_in[1]<=T240*MAS[1]

	T240_mem0 = S.Task('T240_mem0', length=1, delay_cost=1)
	T240_mem0 += MM_MEM[0]
	S += 68 < T240_mem0
	S += T240_mem0 <= T240

	T240_mem1 = S.Task('T240_mem1', length=1, delay_cost=1)
	T240_mem1 += MM_MEM[1]
	S += 76 < T240_mem1
	S += T240_mem1 <= T240

	T24_t5 = S.Task('T24_t5', length=2, delay_cost=1)
	T24_t5 += alt(MAS)
	T24_t5_in = S.Task('T24_t5_in', length=1, delay_cost=1)
	T24_t5_in += alt(MAS_in)
	S += T24_t5_in*MAS_in[0]<=T24_t5*MAS[0]

	S += T24_t5_in*MAS_in[1]<=T24_t5*MAS[1]

	T24_t5_mem0 = S.Task('T24_t5_mem0', length=1, delay_cost=1)
	T24_t5_mem0 += MM_MEM[0]
	S += 68 < T24_t5_mem0
	S += T24_t5_mem0 <= T24_t5

	T24_t5_mem1 = S.Task('T24_t5_mem1', length=1, delay_cost=1)
	T24_t5_mem1 += MM_MEM[1]
	S += 76 < T24_t5_mem1
	S += T24_t5_mem1 <= T24_t5

	Z3_t1 = S.Task('Z3_t1', length=9, delay_cost=1)
	Z3_t1 += alt(MM)
	Z3_t1_in = S.Task('Z3_t1_in', length=1, delay_cost=1)
	Z3_t1_in += alt(MM_in)
	S += Z3_t1_in*MM_in[0]<=Z3_t1*MM[0]
	Z3_t1_mem0 = S.Task('Z3_t1_mem0', length=1, delay_cost=1)
	Z3_t1_mem0 += MAIN_MEM_r[0]
	S += Z3_t1_mem0 <= Z3_t1

	Z3_t1_mem1 = S.Task('Z3_t1_mem1', length=1, delay_cost=1)
	Z3_t1_mem1 += MAS_MEM[1]
	S += 68 < Z3_t1_mem1
	S += Z3_t1_mem1 <= Z3_t1

	Z3_t3 = S.Task('Z3_t3', length=2, delay_cost=1)
	Z3_t3 += alt(MAS)
	Z3_t3_in = S.Task('Z3_t3_in', length=1, delay_cost=1)
	Z3_t3_in += alt(MAS_in)
	S += Z3_t3_in*MAS_in[0]<=Z3_t3*MAS[0]

	S += Z3_t3_in*MAS_in[1]<=Z3_t3*MAS[1]

	Z3_t3_mem0 = S.Task('Z3_t3_mem0', length=1, delay_cost=1)
	Z3_t3_mem0 += MAS_MEM[2]
	S += 61 < Z3_t3_mem0
	S += Z3_t3_mem0 <= Z3_t3

	Z3_t3_mem1 = S.Task('Z3_t3_mem1', length=1, delay_cost=1)
	Z3_t3_mem1 += MAS_MEM[1]
	S += 68 < Z3_t3_mem1
	S += Z3_t3_mem1 <= Z3_t3

	T161 = S.Task('T161', length=2, delay_cost=1)
	T161 += alt(MAS)
	T161_in = S.Task('T161_in', length=1, delay_cost=1)
	T161_in += alt(MAS_in)
	S += T161_in*MAS_in[0]<=T161*MAS[0]

	S += T161_in*MAS_in[1]<=T161*MAS[1]

	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	T161_mem0 += alt(MM_MEM)
	S += (T16_t4*MM[0])-1 < T161_mem0*MM_MEM[0]
	S += T161_mem0 <= T161

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	T161_mem1 += alt(MAS_MEM)
	S += (T16_t5*MAS[0])-1 < T161_mem1*MAS_MEM[1]
	S += (T16_t5*MAS[1])-1 < T161_mem1*MAS_MEM[3]
	S += T161_mem1 <= T161

	T171 = S.Task('T171', length=2, delay_cost=1)
	T171 += alt(MAS)
	T171_in = S.Task('T171_in', length=1, delay_cost=1)
	T171_in += alt(MAS_in)
	S += T171_in*MAS_in[0]<=T171*MAS[0]

	S += T171_in*MAS_in[1]<=T171*MAS[1]

	T171_mem0 = S.Task('T171_mem0', length=1, delay_cost=1)
	T171_mem0 += alt(MM_MEM)
	S += (T17_t4*MM[0])-1 < T171_mem0*MM_MEM[0]
	S += T171_mem0 <= T171

	T171_mem1 = S.Task('T171_mem1', length=1, delay_cost=1)
	T171_mem1 += alt(MAS_MEM)
	S += (T17_t5*MAS[0])-1 < T171_mem1*MAS_MEM[1]
	S += (T17_t5*MAS[1])-1 < T171_mem1*MAS_MEM[3]
	S += T171_mem1 <= T171

	T20_t4 = S.Task('T20_t4', length=9, delay_cost=1)
	T20_t4 += alt(MM)
	T20_t4_in = S.Task('T20_t4_in', length=1, delay_cost=1)
	T20_t4_in += alt(MM_in)
	S += T20_t4_in*MM_in[0]<=T20_t4*MM[0]
	T20_t4_mem0 = S.Task('T20_t4_mem0', length=1, delay_cost=1)
	T20_t4_mem0 += MAS_MEM[2]
	S += 36 < T20_t4_mem0
	S += T20_t4_mem0 <= T20_t4

	T20_t4_mem1 = S.Task('T20_t4_mem1', length=1, delay_cost=1)
	T20_t4_mem1 += alt(MAS_MEM)
	S += (T20_t3*MAS[0])-1 < T20_t4_mem1*MAS_MEM[1]
	S += (T20_t3*MAS[1])-1 < T20_t4_mem1*MAS_MEM[3]
	S += T20_t4_mem1 <= T20_t4

	T200 = S.Task('T200', length=2, delay_cost=1)
	T200 += alt(MAS)
	T200_in = S.Task('T200_in', length=1, delay_cost=1)
	T200_in += alt(MAS_in)
	S += T200_in*MAS_in[0]<=T200*MAS[0]

	S += T200_in*MAS_in[1]<=T200*MAS[1]

	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	T200_mem0 += MM_MEM[0]
	S += 69 < T200_mem0
	S += T200_mem0 <= T200

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	T200_mem1 += alt(MM_MEM)
	S += (T20_t1*MM[0])-1 < T200_mem1*MM_MEM[1]
	S += T200_mem1 <= T200

	T20_t5 = S.Task('T20_t5', length=2, delay_cost=1)
	T20_t5 += alt(MAS)
	T20_t5_in = S.Task('T20_t5_in', length=1, delay_cost=1)
	T20_t5_in += alt(MAS_in)
	S += T20_t5_in*MAS_in[0]<=T20_t5*MAS[0]

	S += T20_t5_in*MAS_in[1]<=T20_t5*MAS[1]

	T20_t5_mem0 = S.Task('T20_t5_mem0', length=1, delay_cost=1)
	T20_t5_mem0 += MM_MEM[0]
	S += 69 < T20_t5_mem0
	S += T20_t5_mem0 <= T20_t5

	T20_t5_mem1 = S.Task('T20_t5_mem1', length=1, delay_cost=1)
	T20_t5_mem1 += alt(MM_MEM)
	S += (T20_t1*MM[0])-1 < T20_t5_mem1*MM_MEM[1]
	S += T20_t5_mem1 <= T20_t5

	T22_t2 = S.Task('T22_t2', length=9, delay_cost=1)
	T22_t2 += alt(MM)
	T22_t2_in = S.Task('T22_t2_in', length=1, delay_cost=1)
	T22_t2_in += alt(MM_in)
	S += T22_t2_in*MM_in[0]<=T22_t2*MM[0]
	T22_t2_mem0 = S.Task('T22_t2_mem0', length=1, delay_cost=1)
	T22_t2_mem0 += alt(MAS_MEM)
	S += (T22_t0*MAS[0])-1 < T22_t2_mem0*MAS_MEM[0]
	S += (T22_t0*MAS[1])-1 < T22_t2_mem0*MAS_MEM[2]
	S += T22_t2_mem0 <= T22_t2

	T22_t2_mem1 = S.Task('T22_t2_mem1', length=1, delay_cost=1)
	T22_t2_mem1 += alt(MAS_MEM)
	S += (T22_t1*MAS[0])-1 < T22_t2_mem1*MAS_MEM[1]
	S += (T22_t1*MAS[1])-1 < T22_t2_mem1*MAS_MEM[3]
	S += T22_t2_mem1 <= T22_t2

	T22_t5 = S.Task('T22_t5', length=2, delay_cost=1)
	T22_t5 += alt(MAS)
	T22_t5_in = S.Task('T22_t5_in', length=1, delay_cost=1)
	T22_t5_in += alt(MAS_in)
	S += T22_t5_in*MAS_in[0]<=T22_t5*MAS[0]

	S += T22_t5_in*MAS_in[1]<=T22_t5*MAS[1]

	T22_t5_mem0 = S.Task('T22_t5_mem0', length=1, delay_cost=1)
	T22_t5_mem0 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T22_t5_mem0*MM_MEM[0]
	S += T22_t5_mem0 <= T22_t5

	T22_t5_mem1 = S.Task('T22_t5_mem1', length=1, delay_cost=1)
	T22_t5_mem1 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T22_t5_mem1*MM_MEM[1]
	S += T22_t5_mem1 <= T22_t5

	T221 = S.Task('T221', length=2, delay_cost=1)
	T221 += alt(MAS)
	T221_in = S.Task('T221_in', length=1, delay_cost=1)
	T221_in += alt(MAS_in)
	S += T221_in*MAS_in[0]<=T221*MAS[0]

	S += T221_in*MAS_in[1]<=T221*MAS[1]

	T221_mem0 = S.Task('T221_mem0', length=1, delay_cost=1)
	T221_mem0 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T221_mem0*MM_MEM[0]
	S += T221_mem0 <= T221

	T221_mem1 = S.Task('T221_mem1', length=1, delay_cost=1)
	T221_mem1 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T221_mem1*MM_MEM[1]
	S += T221_mem1 <= T221

	T23_t2 = S.Task('T23_t2', length=9, delay_cost=1)
	T23_t2 += alt(MM)
	T23_t2_in = S.Task('T23_t2_in', length=1, delay_cost=1)
	T23_t2_in += alt(MM_in)
	S += T23_t2_in*MM_in[0]<=T23_t2*MM[0]
	T23_t2_mem0 = S.Task('T23_t2_mem0', length=1, delay_cost=1)
	T23_t2_mem0 += alt(MAS_MEM)
	S += (T23_t0*MAS[0])-1 < T23_t2_mem0*MAS_MEM[0]
	S += (T23_t0*MAS[1])-1 < T23_t2_mem0*MAS_MEM[2]
	S += T23_t2_mem0 <= T23_t2

	T23_t2_mem1 = S.Task('T23_t2_mem1', length=1, delay_cost=1)
	T23_t2_mem1 += alt(MAS_MEM)
	S += (T23_t1*MAS[0])-1 < T23_t2_mem1*MAS_MEM[1]
	S += (T23_t1*MAS[1])-1 < T23_t2_mem1*MAS_MEM[3]
	S += T23_t2_mem1 <= T23_t2

	T23_t5 = S.Task('T23_t5', length=2, delay_cost=1)
	T23_t5 += alt(MAS)
	T23_t5_in = S.Task('T23_t5_in', length=1, delay_cost=1)
	T23_t5_in += alt(MAS_in)
	S += T23_t5_in*MAS_in[0]<=T23_t5*MAS[0]

	S += T23_t5_in*MAS_in[1]<=T23_t5*MAS[1]

	T23_t5_mem0 = S.Task('T23_t5_mem0', length=1, delay_cost=1)
	T23_t5_mem0 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T23_t5_mem0*MM_MEM[0]
	S += T23_t5_mem0 <= T23_t5

	T23_t5_mem1 = S.Task('T23_t5_mem1', length=1, delay_cost=1)
	T23_t5_mem1 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T23_t5_mem1*MM_MEM[1]
	S += T23_t5_mem1 <= T23_t5

	T231 = S.Task('T231', length=2, delay_cost=1)
	T231 += alt(MAS)
	T231_in = S.Task('T231_in', length=1, delay_cost=1)
	T231_in += alt(MAS_in)
	S += T231_in*MAS_in[0]<=T231*MAS[0]

	S += T231_in*MAS_in[1]<=T231*MAS[1]

	T231_mem0 = S.Task('T231_mem0', length=1, delay_cost=1)
	T231_mem0 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T231_mem0*MM_MEM[0]
	S += T231_mem0 <= T231

	T231_mem1 = S.Task('T231_mem1', length=1, delay_cost=1)
	T231_mem1 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T231_mem1*MM_MEM[1]
	S += T231_mem1 <= T231

	T241 = S.Task('T241', length=2, delay_cost=1)
	T241 += alt(MAS)
	T241_in = S.Task('T241_in', length=1, delay_cost=1)
	T241_in += alt(MAS_in)
	S += T241_in*MAS_in[0]<=T241*MAS[0]

	S += T241_in*MAS_in[1]<=T241*MAS[1]

	T241_mem0 = S.Task('T241_mem0', length=1, delay_cost=1)
	T241_mem0 += alt(MM_MEM)
	S += (T24_t4*MM[0])-1 < T241_mem0*MM_MEM[0]
	S += T241_mem0 <= T241

	T241_mem1 = S.Task('T241_mem1', length=1, delay_cost=1)
	T241_mem1 += alt(MAS_MEM)
	S += (T24_t5*MAS[0])-1 < T241_mem1*MAS_MEM[1]
	S += (T24_t5*MAS[1])-1 < T241_mem1*MAS_MEM[3]
	S += T241_mem1 <= T241

	Z3_t4 = S.Task('Z3_t4', length=9, delay_cost=1)
	Z3_t4 += alt(MM)
	Z3_t4_in = S.Task('Z3_t4_in', length=1, delay_cost=1)
	Z3_t4_in += alt(MM_in)
	S += Z3_t4_in*MM_in[0]<=Z3_t4*MM[0]
	Z3_t4_mem0 = S.Task('Z3_t4_mem0', length=1, delay_cost=1)
	Z3_t4_mem0 += MAS_MEM[2]
	S += 32 < Z3_t4_mem0
	S += Z3_t4_mem0 <= Z3_t4

	Z3_t4_mem1 = S.Task('Z3_t4_mem1', length=1, delay_cost=1)
	Z3_t4_mem1 += alt(MAS_MEM)
	S += (Z3_t3*MAS[0])-1 < Z3_t4_mem1*MAS_MEM[1]
	S += (Z3_t3*MAS[1])-1 < Z3_t4_mem1*MAS_MEM[3]
	S += Z3_t4_mem1 <= Z3_t4

	Z20_new = S.Task('Z20_new', length=2, delay_cost=1)
	Z20_new += alt(MAS)
	Z20_new_in = S.Task('Z20_new_in', length=1, delay_cost=1)
	Z20_new_in += alt(MAS_in)
	S += Z20_new_in*MAS_in[0]<=Z20_new*MAS[0]

	S += Z20_new_in*MAS_in[1]<=Z20_new*MAS[1]

	S += 0<Z20_new

	Z20_new_w = S.Task('Z20_new_w', length=1, delay_cost=1)
	Z20_new_w += alt(MAIN_MEM_w)
	S += Z20_new <= Z20_new_w

	Z20_new_mem0 = S.Task('Z20_new_mem0', length=1, delay_cost=1)
	Z20_new_mem0 += MM_MEM[0]
	S += 70 < Z20_new_mem0
	S += Z20_new_mem0 <= Z20_new

	Z20_new_mem1 = S.Task('Z20_new_mem1', length=1, delay_cost=1)
	Z20_new_mem1 += alt(MM_MEM)
	S += (Z3_t1*MM[0])-1 < Z20_new_mem1*MM_MEM[1]
	S += Z20_new_mem1 <= Z20_new

	Z3_t5 = S.Task('Z3_t5', length=2, delay_cost=1)
	Z3_t5 += alt(MAS)
	Z3_t5_in = S.Task('Z3_t5_in', length=1, delay_cost=1)
	Z3_t5_in += alt(MAS_in)
	S += Z3_t5_in*MAS_in[0]<=Z3_t5*MAS[0]

	S += Z3_t5_in*MAS_in[1]<=Z3_t5*MAS[1]

	Z3_t5_mem0 = S.Task('Z3_t5_mem0', length=1, delay_cost=1)
	Z3_t5_mem0 += MM_MEM[0]
	S += 70 < Z3_t5_mem0
	S += Z3_t5_mem0 <= Z3_t5

	Z3_t5_mem1 = S.Task('Z3_t5_mem1', length=1, delay_cost=1)
	Z3_t5_mem1 += alt(MM_MEM)
	S += (Z3_t1*MM[0])-1 < Z3_t5_mem1*MM_MEM[1]
	S += Z3_t5_mem1 <= Z3_t5

	T201 = S.Task('T201', length=2, delay_cost=1)
	T201 += alt(MAS)
	T201_in = S.Task('T201_in', length=1, delay_cost=1)
	T201_in += alt(MAS_in)
	S += T201_in*MAS_in[0]<=T201*MAS[0]

	S += T201_in*MAS_in[1]<=T201*MAS[1]

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	T201_mem0 += alt(MM_MEM)
	S += (T20_t4*MM[0])-1 < T201_mem0*MM_MEM[0]
	S += T201_mem0 <= T201

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	T201_mem1 += alt(MAS_MEM)
	S += (T20_t5*MAS[0])-1 < T201_mem1*MAS_MEM[1]
	S += (T20_t5*MAS[1])-1 < T201_mem1*MAS_MEM[3]
	S += T201_mem1 <= T201

	T220 = S.Task('T220', length=2, delay_cost=1)
	T220 += alt(MAS)
	T220_in = S.Task('T220_in', length=1, delay_cost=1)
	T220_in += alt(MAS_in)
	S += T220_in*MAS_in[0]<=T220*MAS[0]

	S += T220_in*MAS_in[1]<=T220*MAS[1]

	T220_mem0 = S.Task('T220_mem0', length=1, delay_cost=1)
	T220_mem0 += alt(MM_MEM)
	S += (T22_t2*MM[0])-1 < T220_mem0*MM_MEM[0]
	S += T220_mem0 <= T220

	T220_mem1 = S.Task('T220_mem1', length=1, delay_cost=1)
	T220_mem1 += alt(MAS_MEM)
	S += (T22_t5*MAS[0])-1 < T220_mem1*MAS_MEM[1]
	S += (T22_t5*MAS[1])-1 < T220_mem1*MAS_MEM[3]
	S += T220_mem1 <= T220

	T230 = S.Task('T230', length=2, delay_cost=1)
	T230 += alt(MAS)
	T230_in = S.Task('T230_in', length=1, delay_cost=1)
	T230_in += alt(MAS_in)
	S += T230_in*MAS_in[0]<=T230*MAS[0]

	S += T230_in*MAS_in[1]<=T230*MAS[1]

	T230_mem0 = S.Task('T230_mem0', length=1, delay_cost=1)
	T230_mem0 += alt(MM_MEM)
	S += (T23_t2*MM[0])-1 < T230_mem0*MM_MEM[0]
	S += T230_mem0 <= T230

	T230_mem1 = S.Task('T230_mem1', length=1, delay_cost=1)
	T230_mem1 += alt(MAS_MEM)
	S += (T23_t5*MAS[0])-1 < T230_mem1*MAS_MEM[1]
	S += (T23_t5*MAS[1])-1 < T230_mem1*MAS_MEM[3]
	S += T230_mem1 <= T230

	T250 = S.Task('T250', length=2, delay_cost=1)
	T250 += alt(MAS)
	T250_in = S.Task('T250_in', length=1, delay_cost=1)
	T250_in += alt(MAS_in)
	S += T250_in*MAS_in[0]<=T250*MAS[0]

	S += T250_in*MAS_in[1]<=T250*MAS[1]

	T250_mem0 = S.Task('T250_mem0', length=1, delay_cost=1)
	T250_mem0 += alt(MAS_MEM)
	S += (T200*MAS[0])-1 < T250_mem0*MAS_MEM[0]
	S += (T200*MAS[1])-1 < T250_mem0*MAS_MEM[2]
	S += T250_mem0 <= T250

	T250_mem1 = S.Task('T250_mem1', length=1, delay_cost=1)
	T250_mem1 += alt(MAS_MEM)
	S += (T200*MAS[0])-1 < T250_mem1*MAS_MEM[1]
	S += (T200*MAS[1])-1 < T250_mem1*MAS_MEM[3]
	S += T250_mem1 <= T250

	Z21_new = S.Task('Z21_new', length=2, delay_cost=1)
	Z21_new += alt(MAS)
	Z21_new_in = S.Task('Z21_new_in', length=1, delay_cost=1)
	Z21_new_in += alt(MAS_in)
	S += Z21_new_in*MAS_in[0]<=Z21_new*MAS[0]

	S += Z21_new_in*MAS_in[1]<=Z21_new*MAS[1]

	S += 0<Z21_new

	Z21_new_w = S.Task('Z21_new_w', length=1, delay_cost=1)
	Z21_new_w += alt(MAIN_MEM_w)
	S += Z21_new <= Z21_new_w

	Z21_new_mem0 = S.Task('Z21_new_mem0', length=1, delay_cost=1)
	Z21_new_mem0 += alt(MM_MEM)
	S += (Z3_t4*MM[0])-1 < Z21_new_mem0*MM_MEM[0]
	S += Z21_new_mem0 <= Z21_new

	Z21_new_mem1 = S.Task('Z21_new_mem1', length=1, delay_cost=1)
	Z21_new_mem1 += alt(MAS_MEM)
	S += (Z3_t5*MAS[0])-1 < Z21_new_mem1*MAS_MEM[1]
	S += (Z3_t5*MAS[1])-1 < Z21_new_mem1*MAS_MEM[3]
	S += Z21_new_mem1 <= Z21_new

	X21_new = S.Task('X21_new', length=2, delay_cost=1)
	X21_new += alt(MAS)
	X21_new_in = S.Task('X21_new_in', length=1, delay_cost=1)
	X21_new_in += alt(MAS_in)
	S += X21_new_in*MAS_in[0]<=X21_new*MAS[0]

	S += X21_new_in*MAS_in[1]<=X21_new*MAS[1]

	S += 0<X21_new

	X21_new_w = S.Task('X21_new_w', length=1, delay_cost=1)
	X21_new_w += alt(MAIN_MEM_w)
	S += X21_new <= X21_new_w

	X21_new_mem0 = S.Task('X21_new_mem0', length=1, delay_cost=1)
	X21_new_mem0 += alt(MAS_MEM)
	S += (T221*MAS[0])-1 < X21_new_mem0*MAS_MEM[0]
	S += (T221*MAS[1])-1 < X21_new_mem0*MAS_MEM[2]
	S += X21_new_mem0 <= X21_new

	X21_new_mem1 = S.Task('X21_new_mem1', length=1, delay_cost=1)
	X21_new_mem1 += alt(MAS_MEM)
	S += (T241*MAS[0])-1 < X21_new_mem1*MAS_MEM[1]
	S += (T241*MAS[1])-1 < X21_new_mem1*MAS_MEM[3]
	S += X21_new_mem1 <= X21_new

	X11_new = S.Task('X11_new', length=2, delay_cost=1)
	X11_new += alt(MAS)
	X11_new_in = S.Task('X11_new_in', length=1, delay_cost=1)
	X11_new_in += alt(MAS_in)
	S += X11_new_in*MAS_in[0]<=X11_new*MAS[0]

	S += X11_new_in*MAS_in[1]<=X11_new*MAS[1]

	S += 0<X11_new

	X11_new_w = S.Task('X11_new_w', length=1, delay_cost=1)
	X11_new_w += alt(MAIN_MEM_w)
	S += X11_new <= X11_new_w

	X11_new_mem0 = S.Task('X11_new_mem0', length=1, delay_cost=1)
	X11_new_mem0 += alt(MAS_MEM)
	S += (T231*MAS[0])-1 < X11_new_mem0*MAS_MEM[0]
	S += (T231*MAS[1])-1 < X11_new_mem0*MAS_MEM[2]
	S += X11_new_mem0 <= X11_new

	X11_new_mem1 = S.Task('X11_new_mem1', length=1, delay_cost=1)
	X11_new_mem1 += alt(MAS_MEM)
	S += (T171*MAS[0])-1 < X11_new_mem1*MAS_MEM[1]
	S += (T171*MAS[1])-1 < X11_new_mem1*MAS_MEM[3]
	S += X11_new_mem1 <= X11_new

	T251 = S.Task('T251', length=2, delay_cost=1)
	T251 += alt(MAS)
	T251_in = S.Task('T251_in', length=1, delay_cost=1)
	T251_in += alt(MAS_in)
	S += T251_in*MAS_in[0]<=T251*MAS[0]

	S += T251_in*MAS_in[1]<=T251*MAS[1]

	T251_mem0 = S.Task('T251_mem0', length=1, delay_cost=1)
	T251_mem0 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem0*MAS_MEM[0]
	S += (T201*MAS[1])-1 < T251_mem0*MAS_MEM[2]
	S += T251_mem0 <= T251

	T251_mem1 = S.Task('T251_mem1', length=1, delay_cost=1)
	T251_mem1 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem1*MAS_MEM[1]
	S += (T201*MAS[1])-1 < T251_mem1*MAS_MEM[3]
	S += T251_mem1 <= T251

	X20_new = S.Task('X20_new', length=2, delay_cost=1)
	X20_new += alt(MAS)
	X20_new_in = S.Task('X20_new_in', length=1, delay_cost=1)
	X20_new_in += alt(MAS_in)
	S += X20_new_in*MAS_in[0]<=X20_new*MAS[0]

	S += X20_new_in*MAS_in[1]<=X20_new*MAS[1]

	S += 0<X20_new

	X20_new_w = S.Task('X20_new_w', length=1, delay_cost=1)
	X20_new_w += alt(MAIN_MEM_w)
	S += X20_new <= X20_new_w

	X20_new_mem0 = S.Task('X20_new_mem0', length=1, delay_cost=1)
	X20_new_mem0 += alt(MAS_MEM)
	S += (T220*MAS[0])-1 < X20_new_mem0*MAS_MEM[0]
	S += (T220*MAS[1])-1 < X20_new_mem0*MAS_MEM[2]
	S += X20_new_mem0 <= X20_new

	X20_new_mem1 = S.Task('X20_new_mem1', length=1, delay_cost=1)
	X20_new_mem1 += alt(MAS_MEM)
	S += (T240*MAS[0])-1 < X20_new_mem1*MAS_MEM[1]
	S += (T240*MAS[1])-1 < X20_new_mem1*MAS_MEM[3]
	S += X20_new_mem1 <= X20_new

	Z10_new = S.Task('Z10_new', length=2, delay_cost=1)
	Z10_new += alt(MAS)
	Z10_new_in = S.Task('Z10_new_in', length=1, delay_cost=1)
	Z10_new_in += alt(MAS_in)
	S += Z10_new_in*MAS_in[0]<=Z10_new*MAS[0]

	S += Z10_new_in*MAS_in[1]<=Z10_new*MAS[1]

	S += 0<Z10_new

	Z10_new_w = S.Task('Z10_new_w', length=1, delay_cost=1)
	Z10_new_w += alt(MAIN_MEM_w)
	S += Z10_new <= Z10_new_w

	Z10_new_mem0 = S.Task('Z10_new_mem0', length=1, delay_cost=1)
	Z10_new_mem0 += alt(MAS_MEM)
	S += (T160*MAS[0])-1 < Z10_new_mem0*MAS_MEM[0]
	S += (T160*MAS[1])-1 < Z10_new_mem0*MAS_MEM[2]
	S += Z10_new_mem0 <= Z10_new

	Z10_new_mem1 = S.Task('Z10_new_mem1', length=1, delay_cost=1)
	Z10_new_mem1 += alt(MAS_MEM)
	S += (T250*MAS[0])-1 < Z10_new_mem1*MAS_MEM[1]
	S += (T250*MAS[1])-1 < Z10_new_mem1*MAS_MEM[3]
	S += Z10_new_mem1 <= Z10_new

	X10_new = S.Task('X10_new', length=2, delay_cost=1)
	X10_new += alt(MAS)
	X10_new_in = S.Task('X10_new_in', length=1, delay_cost=1)
	X10_new_in += alt(MAS_in)
	S += X10_new_in*MAS_in[0]<=X10_new*MAS[0]

	S += X10_new_in*MAS_in[1]<=X10_new*MAS[1]

	S += 0<X10_new

	X10_new_w = S.Task('X10_new_w', length=1, delay_cost=1)
	X10_new_w += alt(MAIN_MEM_w)
	S += X10_new <= X10_new_w

	X10_new_mem0 = S.Task('X10_new_mem0', length=1, delay_cost=1)
	X10_new_mem0 += alt(MAS_MEM)
	S += (T230*MAS[0])-1 < X10_new_mem0*MAS_MEM[0]
	S += (T230*MAS[1])-1 < X10_new_mem0*MAS_MEM[2]
	S += X10_new_mem0 <= X10_new

	X10_new_mem1 = S.Task('X10_new_mem1', length=1, delay_cost=1)
	X10_new_mem1 += alt(MAS_MEM)
	S += (T170*MAS[0])-1 < X10_new_mem1*MAS_MEM[1]
	S += (T170*MAS[1])-1 < X10_new_mem1*MAS_MEM[3]
	S += X10_new_mem1 <= X10_new

	Z11_new = S.Task('Z11_new', length=2, delay_cost=1)
	Z11_new += alt(MAS)
	Z11_new_in = S.Task('Z11_new_in', length=1, delay_cost=1)
	Z11_new_in += alt(MAS_in)
	S += Z11_new_in*MAS_in[0]<=Z11_new*MAS[0]

	S += Z11_new_in*MAS_in[1]<=Z11_new*MAS[1]

	S += 0<Z11_new

	Z11_new_w = S.Task('Z11_new_w', length=1, delay_cost=1)
	Z11_new_w += alt(MAIN_MEM_w)
	S += Z11_new <= Z11_new_w

	Z11_new_mem0 = S.Task('Z11_new_mem0', length=1, delay_cost=1)
	Z11_new_mem0 += alt(MAS_MEM)
	S += (T161*MAS[0])-1 < Z11_new_mem0*MAS_MEM[0]
	S += (T161*MAS[1])-1 < Z11_new_mem0*MAS_MEM[2]
	S += Z11_new_mem0 <= Z11_new

	Z11_new_mem1 = S.Task('Z11_new_mem1', length=1, delay_cost=1)
	Z11_new_mem1 += alt(MAS_MEM)
	S += (T251*MAS[0])-1 < Z11_new_mem1*MAS_MEM[1]
	S += (T251*MAS[1])-1 < Z11_new_mem1*MAS_MEM[3]
	S += Z11_new_mem1 <= Z11_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM1_stage2MAS2/EP2_LADDERMUL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution

