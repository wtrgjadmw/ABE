from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 214
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=11)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=1, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	T7_t2_in = S.Task('T7_t2_in', length=1, delay_cost=1)
	S += T7_t2_in >= 0
	T7_t2_in += MAS_in[0]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	S += T7_t2_mem0 >= 0
	T7_t2_mem0 += MAIN_MEM_r[0]

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	S += T7_t2_mem1 >= 0
	T7_t2_mem1 += MAIN_MEM_r[1]

	T2_t2_in = S.Task('T2_t2_in', length=1, delay_cost=1)
	S += T2_t2_in >= 1
	T2_t2_in += MAS_in[0]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	S += T2_t2_mem0 >= 1
	T2_t2_mem0 += MAIN_MEM_r[0]

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	S += T2_t2_mem1 >= 1
	T2_t2_mem1 += MAIN_MEM_r[1]

	T7_t2 = S.Task('T7_t2', length=3, delay_cost=1)
	S += T7_t2 >= 1
	T7_t2 += MAS[0]

	T2_t2 = S.Task('T2_t2', length=3, delay_cost=1)
	S += T2_t2 >= 2
	T2_t2 += MAS[0]

	T6_t3_in = S.Task('T6_t3_in', length=1, delay_cost=1)
	S += T6_t3_in >= 2
	T6_t3_in += MAS_in[0]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	S += T6_t3_mem0 >= 2
	T6_t3_mem0 += MAIN_MEM_r[0]

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	S += T6_t3_mem1 >= 2
	T6_t3_mem1 += MAIN_MEM_r[1]

	T6_t3 = S.Task('T6_t3', length=3, delay_cost=1)
	S += T6_t3 >= 3
	T6_t3 += MAS[0]

	T7_t3_in = S.Task('T7_t3_in', length=1, delay_cost=1)
	S += T7_t3_in >= 3
	T7_t3_in += MAS_in[0]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	S += T7_t3_mem0 >= 3
	T7_t3_mem0 += MAIN_MEM_r[0]

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	S += T7_t3_mem1 >= 3
	T7_t3_mem1 += MAIN_MEM_r[1]

	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	S += T6_t0_in >= 4
	T6_t0_in += MM_in[0]

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	S += T6_t0_mem0 >= 4
	T6_t0_mem0 += MAIN_MEM_r[0]

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	S += T6_t0_mem1 >= 4
	T6_t0_mem1 += MAIN_MEM_r[1]

	T7_t3 = S.Task('T7_t3', length=3, delay_cost=1)
	S += T7_t3 >= 4
	T7_t3 += MAS[0]

	T3_t3_in = S.Task('T3_t3_in', length=1, delay_cost=1)
	S += T3_t3_in >= 5
	T3_t3_in += MAS_in[0]

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	S += T3_t3_mem0 >= 5
	T3_t3_mem0 += MAIN_MEM_r[0]

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	S += T3_t3_mem1 >= 5
	T3_t3_mem1 += MAIN_MEM_r[1]

	T6_t0 = S.Task('T6_t0', length=11, delay_cost=1)
	S += T6_t0 >= 5
	T6_t0 += MM[0]

	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	S += T3_t0_in >= 6
	T3_t0_in += MM_in[0]

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	S += T3_t0_mem0 >= 6
	T3_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	S += T3_t0_mem1 >= 6
	T3_t0_mem1 += MAIN_MEM_r[1]

	T3_t3 = S.Task('T3_t3', length=3, delay_cost=1)
	S += T3_t3 >= 6
	T3_t3 += MAS[0]

	T3_t0 = S.Task('T3_t0', length=11, delay_cost=1)
	S += T3_t0 >= 7
	T3_t0 += MM[0]

	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	S += T5_t3_in >= 7
	T5_t3_in += MM_in[0]

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	S += T5_t3_mem0 >= 7
	T5_t3_mem0 += MAIN_MEM_r[0]

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	S += T5_t3_mem1 >= 7
	T5_t3_mem1 += MAIN_MEM_r[1]

	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	S += T2_t0_in >= 8
	T2_t0_in += MM_in[0]

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	S += T2_t0_mem0 >= 8
	T2_t0_mem0 += MAIN_MEM_r[0]

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	S += T2_t0_mem1 >= 8
	T2_t0_mem1 += MAIN_MEM_r[1]

	T5_t3 = S.Task('T5_t3', length=11, delay_cost=1)
	S += T5_t3 >= 8
	T5_t3 += MM[0]

	T2_t0 = S.Task('T2_t0', length=11, delay_cost=1)
	S += T2_t0 >= 9
	T2_t0 += MM[0]

	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	S += T4_t1_in >= 9
	T4_t1_in += MM_in[0]

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	S += T4_t1_mem0 >= 9
	T4_t1_mem0 += MAIN_MEM_r[0]

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	S += T4_t1_mem1 >= 9
	T4_t1_mem1 += MAIN_MEM_r[1]

	T2_t3_in = S.Task('T2_t3_in', length=1, delay_cost=1)
	S += T2_t3_in >= 10
	T2_t3_in += MAS_in[0]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	S += T2_t3_mem0 >= 10
	T2_t3_mem0 += MAIN_MEM_r[0]

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	S += T2_t3_mem1 >= 10
	T2_t3_mem1 += MAIN_MEM_r[1]

	T4_t1 = S.Task('T4_t1', length=11, delay_cost=1)
	S += T4_t1 >= 10
	T4_t1 += MM[0]

	T7_t4_in = S.Task('T7_t4_in', length=1, delay_cost=1)
	S += T7_t4_in >= 10
	T7_t4_in += MM_in[0]

	T7_t4_mem0 = S.Task('T7_t4_mem0', length=1, delay_cost=1)
	S += T7_t4_mem0 >= 10
	T7_t4_mem0 += MAS_MEM[0]

	T7_t4_mem1 = S.Task('T7_t4_mem1', length=1, delay_cost=1)
	S += T7_t4_mem1 >= 10
	T7_t4_mem1 += MAS_MEM[1]

	T2_t3 = S.Task('T2_t3', length=3, delay_cost=1)
	S += T2_t3 >= 11
	T2_t3 += MAS[0]

	T7_t4 = S.Task('T7_t4', length=11, delay_cost=1)
	S += T7_t4 >= 11
	T7_t4 += MM[0]

	T9_t2_in = S.Task('T9_t2_in', length=1, delay_cost=1)
	S += T9_t2_in >= 11
	T9_t2_in += MAS_in[0]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	S += T9_t2_mem0 >= 11
	T9_t2_mem0 += MAIN_MEM_r[0]

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	S += T9_t2_mem1 >= 11
	T9_t2_mem1 += MAIN_MEM_r[1]

	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	S += T2_t1_in >= 12
	T2_t1_in += MM_in[0]

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	S += T2_t1_mem0 >= 12
	T2_t1_mem0 += MAIN_MEM_r[0]

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	S += T2_t1_mem1 >= 12
	T2_t1_mem1 += MAIN_MEM_r[1]

	T9_t2 = S.Task('T9_t2', length=3, delay_cost=1)
	S += T9_t2 >= 12
	T9_t2 += MAS[0]

	T2_t1 = S.Task('T2_t1', length=11, delay_cost=1)
	S += T2_t1 >= 13
	T2_t1 += MM[0]

	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	S += T3_t1_in >= 13
	T3_t1_in += MM_in[0]

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	S += T3_t1_mem0 >= 13
	T3_t1_mem0 += MAIN_MEM_r[0]

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	S += T3_t1_mem1 >= 13
	T3_t1_mem1 += MAIN_MEM_r[1]

	T2_t4_in = S.Task('T2_t4_in', length=1, delay_cost=1)
	S += T2_t4_in >= 14
	T2_t4_in += MM_in[0]

	T2_t4_mem0 = S.Task('T2_t4_mem0', length=1, delay_cost=1)
	S += T2_t4_mem0 >= 14
	T2_t4_mem0 += MAS_MEM[0]

	T2_t4_mem1 = S.Task('T2_t4_mem1', length=1, delay_cost=1)
	S += T2_t4_mem1 >= 14
	T2_t4_mem1 += MAS_MEM[1]

	T3_t1 = S.Task('T3_t1', length=11, delay_cost=1)
	S += T3_t1 >= 14
	T3_t1 += MM[0]

	T4_t2_in = S.Task('T4_t2_in', length=1, delay_cost=1)
	S += T4_t2_in >= 14
	T4_t2_in += MAS_in[0]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	S += T4_t2_mem0 >= 14
	T4_t2_mem0 += MAIN_MEM_r[0]

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	S += T4_t2_mem1 >= 14
	T4_t2_mem1 += MAIN_MEM_r[1]

	T2_t4 = S.Task('T2_t4', length=11, delay_cost=1)
	S += T2_t4 >= 15
	T2_t4 += MM[0]

	T4_t2 = S.Task('T4_t2', length=3, delay_cost=1)
	S += T4_t2 >= 15
	T4_t2 += MAS[0]

	T4_t3_in = S.Task('T4_t3_in', length=1, delay_cost=1)
	S += T4_t3_in >= 15
	T4_t3_in += MAS_in[0]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	S += T4_t3_mem0 >= 15
	T4_t3_mem0 += MAIN_MEM_r[0]

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	S += T4_t3_mem1 >= 15
	T4_t3_mem1 += MAIN_MEM_r[1]

	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	S += T1_t3_in >= 16
	T1_t3_in += MM_in[0]

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	S += T1_t3_mem0 >= 16
	T1_t3_mem0 += MAIN_MEM_r[0]

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	S += T1_t3_mem1 >= 16
	T1_t3_mem1 += MAIN_MEM_r[1]

	T4_t3 = S.Task('T4_t3', length=3, delay_cost=1)
	S += T4_t3 >= 16
	T4_t3 += MAS[0]

	T1_t3 = S.Task('T1_t3', length=11, delay_cost=1)
	S += T1_t3 >= 17
	T1_t3 += MM[0]

	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	S += T6_t1_in >= 17
	T6_t1_in += MM_in[0]

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	S += T6_t1_mem0 >= 17
	T6_t1_mem0 += MAIN_MEM_r[0]

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	S += T6_t1_mem1 >= 17
	T6_t1_mem1 += MAIN_MEM_r[1]

	T3_t2_in = S.Task('T3_t2_in', length=1, delay_cost=1)
	S += T3_t2_in >= 18
	T3_t2_in += MAS_in[0]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	S += T3_t2_mem0 >= 18
	T3_t2_mem0 += MAIN_MEM_r[0]

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	S += T3_t2_mem1 >= 18
	T3_t2_mem1 += MAIN_MEM_r[1]

	T4_t4_in = S.Task('T4_t4_in', length=1, delay_cost=1)
	S += T4_t4_in >= 18
	T4_t4_in += MM_in[0]

	T4_t4_mem0 = S.Task('T4_t4_mem0', length=1, delay_cost=1)
	S += T4_t4_mem0 >= 18
	T4_t4_mem0 += MAS_MEM[0]

	T4_t4_mem1 = S.Task('T4_t4_mem1', length=1, delay_cost=1)
	S += T4_t4_mem1 >= 18
	T4_t4_mem1 += MAS_MEM[1]

	T6_t1 = S.Task('T6_t1', length=11, delay_cost=1)
	S += T6_t1 >= 18
	T6_t1 += MM[0]

	T3_t2 = S.Task('T3_t2', length=3, delay_cost=1)
	S += T3_t2 >= 19
	T3_t2 += MAS[0]

	T4_t4 = S.Task('T4_t4', length=11, delay_cost=1)
	S += T4_t4 >= 19
	T4_t4 += MM[0]

	T8_t2_in = S.Task('T8_t2_in', length=1, delay_cost=1)
	S += T8_t2_in >= 19
	T8_t2_in += MAS_in[0]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	S += T8_t2_mem0 >= 19
	T8_t2_mem0 += MAIN_MEM_r[0]

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	S += T8_t2_mem1 >= 19
	T8_t2_mem1 += MAIN_MEM_r[1]

	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	S += T4_t0_in >= 20
	T4_t0_in += MM_in[0]

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	S += T4_t0_mem0 >= 20
	T4_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	S += T4_t0_mem1 >= 20
	T4_t0_mem1 += MAIN_MEM_r[1]

	T5_t5_in = S.Task('T5_t5_in', length=1, delay_cost=1)
	S += T5_t5_in >= 20
	T5_t5_in += MAS_in[0]

	T5_t5_mem0 = S.Task('T5_t5_mem0', length=1, delay_cost=1)
	S += T5_t5_mem0 >= 20
	T5_t5_mem0 += MM_MEM[0]

	T5_t5_mem1 = S.Task('T5_t5_mem1', length=1, delay_cost=1)
	S += T5_t5_mem1 >= 20
	T5_t5_mem1 += MM_MEM[1]

	T8_t2 = S.Task('T8_t2', length=3, delay_cost=1)
	S += T8_t2 >= 20
	T8_t2 += MAS[0]

	T3_t4_in = S.Task('T3_t4_in', length=1, delay_cost=1)
	S += T3_t4_in >= 21
	T3_t4_in += MM_in[0]

	T3_t4_mem0 = S.Task('T3_t4_mem0', length=1, delay_cost=1)
	S += T3_t4_mem0 >= 21
	T3_t4_mem0 += MAS_MEM[0]

	T3_t4_mem1 = S.Task('T3_t4_mem1', length=1, delay_cost=1)
	S += T3_t4_mem1 >= 21
	T3_t4_mem1 += MAS_MEM[1]

	T4_t0 = S.Task('T4_t0', length=11, delay_cost=1)
	S += T4_t0 >= 21
	T4_t0 += MM[0]

	T5_t5 = S.Task('T5_t5', length=3, delay_cost=1)
	S += T5_t5 >= 21
	T5_t5 += MAS[0]

	T6_t2_in = S.Task('T6_t2_in', length=1, delay_cost=1)
	S += T6_t2_in >= 21
	T6_t2_in += MAS_in[0]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	S += T6_t2_mem0 >= 21
	T6_t2_mem0 += MAIN_MEM_r[0]

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	S += T6_t2_mem1 >= 21
	T6_t2_mem1 += MAIN_MEM_r[1]

	T3_t4 = S.Task('T3_t4', length=11, delay_cost=1)
	S += T3_t4 >= 22
	T3_t4 += MM[0]

	T5_t0_in = S.Task('T5_t0_in', length=1, delay_cost=1)
	S += T5_t0_in >= 22
	T5_t0_in += MAS_in[0]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	S += T5_t0_mem0 >= 22
	T5_t0_mem0 += MAIN_MEM_r[0]

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	S += T5_t0_mem1 >= 22
	T5_t0_mem1 += MAIN_MEM_r[1]

	T6_t2 = S.Task('T6_t2', length=3, delay_cost=1)
	S += T6_t2 >= 22
	T6_t2 += MAS[0]

	T5_t0 = S.Task('T5_t0', length=3, delay_cost=1)
	S += T5_t0 >= 23
	T5_t0 += MAS[0]

	T5_t1_in = S.Task('T5_t1_in', length=1, delay_cost=1)
	S += T5_t1_in >= 23
	T5_t1_in += MAS_in[0]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	S += T5_t1_mem0 >= 23
	T5_t1_mem0 += MAIN_MEM_r[0]

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	S += T5_t1_mem1 >= 23
	T5_t1_mem1 += MAIN_MEM_r[1]

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	S += T30_in >= 24
	T30_in += MAS_in[0]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 24
	T30_mem0 += MM_MEM[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 24
	T30_mem1 += MM_MEM[1]

	T5_t1 = S.Task('T5_t1', length=3, delay_cost=1)
	S += T5_t1 >= 24
	T5_t1 += MAS[0]

	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	S += T7_t0_in >= 24
	T7_t0_in += MM_in[0]

	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	S += T7_t0_mem0 >= 24
	T7_t0_mem0 += MAIN_MEM_r[0]

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	S += T7_t0_mem1 >= 24
	T7_t0_mem1 += MAIN_MEM_r[1]

	T30 = S.Task('T30', length=3, delay_cost=1)
	S += T30 >= 25
	T30 += MAS[0]

	T3_t5_in = S.Task('T3_t5_in', length=1, delay_cost=1)
	S += T3_t5_in >= 25
	T3_t5_in += MAS_in[0]

	T3_t5_mem0 = S.Task('T3_t5_mem0', length=1, delay_cost=1)
	S += T3_t5_mem0 >= 25
	T3_t5_mem0 += MM_MEM[0]

	T3_t5_mem1 = S.Task('T3_t5_mem1', length=1, delay_cost=1)
	S += T3_t5_mem1 >= 25
	T3_t5_mem1 += MM_MEM[1]

	T7_t0 = S.Task('T7_t0', length=11, delay_cost=1)
	S += T7_t0 >= 25
	T7_t0 += MM[0]

	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	S += T7_t1_in >= 25
	T7_t1_in += MM_in[0]

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	S += T7_t1_mem0 >= 25
	T7_t1_mem0 += MAIN_MEM_r[0]

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	S += T7_t1_mem1 >= 25
	T7_t1_mem1 += MAIN_MEM_r[1]

	T1_t1_in = S.Task('T1_t1_in', length=1, delay_cost=1)
	S += T1_t1_in >= 26
	T1_t1_in += MAS_in[0]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	S += T1_t1_mem0 >= 26
	T1_t1_mem0 += MAIN_MEM_r[0]

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	S += T1_t1_mem1 >= 26
	T1_t1_mem1 += MAIN_MEM_r[1]

	T3_t5 = S.Task('T3_t5', length=3, delay_cost=1)
	S += T3_t5 >= 26
	T3_t5 += MAS[0]

	T5_t2_in = S.Task('T5_t2_in', length=1, delay_cost=1)
	S += T5_t2_in >= 26
	T5_t2_in += MM_in[0]

	T5_t2_mem0 = S.Task('T5_t2_mem0', length=1, delay_cost=1)
	S += T5_t2_mem0 >= 26
	T5_t2_mem0 += MAS_MEM[0]

	T5_t2_mem1 = S.Task('T5_t2_mem1', length=1, delay_cost=1)
	S += T5_t2_mem1 >= 26
	T5_t2_mem1 += MAS_MEM[1]

	T7_t1 = S.Task('T7_t1', length=11, delay_cost=1)
	S += T7_t1 >= 26
	T7_t1 += MM[0]

	T1_t0_in = S.Task('T1_t0_in', length=1, delay_cost=1)
	S += T1_t0_in >= 27
	T1_t0_in += MAS_in[0]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	S += T1_t0_mem0 >= 27
	T1_t0_mem0 += MAIN_MEM_r[0]

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	S += T1_t0_mem1 >= 27
	T1_t0_mem1 += MAIN_MEM_r[1]

	T1_t1 = S.Task('T1_t1', length=3, delay_cost=1)
	S += T1_t1 >= 27
	T1_t1 += MAS[0]

	T5_t2 = S.Task('T5_t2', length=11, delay_cost=1)
	S += T5_t2 >= 27
	T5_t2 += MM[0]

	T6_t4_in = S.Task('T6_t4_in', length=1, delay_cost=1)
	S += T6_t4_in >= 27
	T6_t4_in += MM_in[0]

	T6_t4_mem0 = S.Task('T6_t4_mem0', length=1, delay_cost=1)
	S += T6_t4_mem0 >= 27
	T6_t4_mem0 += MAS_MEM[0]

	T6_t4_mem1 = S.Task('T6_t4_mem1', length=1, delay_cost=1)
	S += T6_t4_mem1 >= 27
	T6_t4_mem1 += MAS_MEM[1]

	T11_t2_in = S.Task('T11_t2_in', length=1, delay_cost=1)
	S += T11_t2_in >= 28
	T11_t2_in += MAS_in[0]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	S += T11_t2_mem0 >= 28
	T11_t2_mem0 += MAIN_MEM_r[0]

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	S += T11_t2_mem1 >= 28
	T11_t2_mem1 += MAIN_MEM_r[1]

	T1_t0 = S.Task('T1_t0', length=3, delay_cost=1)
	S += T1_t0 >= 28
	T1_t0 += MAS[0]

	T6_t4 = S.Task('T6_t4', length=11, delay_cost=1)
	S += T6_t4 >= 28
	T6_t4 += MM[0]

	T10_t2_in = S.Task('T10_t2_in', length=1, delay_cost=1)
	S += T10_t2_in >= 29
	T10_t2_in += MAS_in[0]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	S += T10_t2_mem0 >= 29
	T10_t2_mem0 += MAIN_MEM_r[0]

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	S += T10_t2_mem1 >= 29
	T10_t2_mem1 += MAIN_MEM_r[1]

	T11_t2 = S.Task('T11_t2', length=3, delay_cost=1)
	S += T11_t2 >= 29
	T11_t2 += MAS[0]

	T10_t2 = S.Task('T10_t2', length=3, delay_cost=1)
	S += T10_t2 >= 30
	T10_t2 += MAS[0]

	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	S += T11_in >= 30
	T11_in += MAS_in[0]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 30
	T11_mem0 += MM_MEM[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 30
	T11_mem1 += MM_MEM[1]

	T1_t2_in = S.Task('T1_t2_in', length=1, delay_cost=1)
	S += T1_t2_in >= 30
	T1_t2_in += MM_in[0]

	T1_t2_mem0 = S.Task('T1_t2_mem0', length=1, delay_cost=1)
	S += T1_t2_mem0 >= 30
	T1_t2_mem0 += MAS_MEM[0]

	T1_t2_mem1 = S.Task('T1_t2_mem1', length=1, delay_cost=1)
	S += T1_t2_mem1 >= 30
	T1_t2_mem1 += MAS_MEM[1]

	T10_t0_in = S.Task('T10_t0_in', length=1, delay_cost=1)
	S += T10_t0_in >= 31
	T10_t0_in += MM_in[0]

	T10_t0_mem0 = S.Task('T10_t0_mem0', length=1, delay_cost=1)
	S += T10_t0_mem0 >= 31
	T10_t0_mem0 += MAIN_MEM_r[0]

	T10_t0_mem1 = S.Task('T10_t0_mem1', length=1, delay_cost=1)
	S += T10_t0_mem1 >= 31
	T10_t0_mem1 += MAS_MEM[1]

	T11 = S.Task('T11', length=3, delay_cost=1)
	S += T11 >= 31
	T11 += MAS[0]

	T1_t2 = S.Task('T1_t2', length=11, delay_cost=1)
	S += T1_t2 >= 31
	T1_t2 += MM[0]

	T40_in = S.Task('T40_in', length=1, delay_cost=1)
	S += T40_in >= 31
	T40_in += MAS_in[0]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 31
	T40_mem0 += MM_MEM[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 31
	T40_mem1 += MM_MEM[1]

	T10_t0 = S.Task('T10_t0', length=11, delay_cost=1)
	S += T10_t0 >= 32
	T10_t0 += MM[0]

	T11_t0_in = S.Task('T11_t0_in', length=1, delay_cost=1)
	S += T11_t0_in >= 32
	T11_t0_in += MM_in[0]

	T11_t0_mem0 = S.Task('T11_t0_mem0', length=1, delay_cost=1)
	S += T11_t0_mem0 >= 32
	T11_t0_mem0 += MAIN_MEM_r[0]

	T11_t0_mem1 = S.Task('T11_t0_mem1', length=1, delay_cost=1)
	S += T11_t0_mem1 >= 32
	T11_t0_mem1 += MAS_MEM[1]

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	S += T20_in >= 32
	T20_in += MAS_in[0]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 32
	T20_mem0 += MM_MEM[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 32
	T20_mem1 += MM_MEM[1]

	T40 = S.Task('T40', length=3, delay_cost=1)
	S += T40 >= 32
	T40 += MAS[0]

	T11_t0 = S.Task('T11_t0', length=11, delay_cost=1)
	S += T11_t0 >= 33
	T11_t0 += MM[0]

	T20 = S.Task('T20', length=3, delay_cost=1)
	S += T20 >= 33
	T20 += MAS[0]

	T2_t5_in = S.Task('T2_t5_in', length=1, delay_cost=1)
	S += T2_t5_in >= 33
	T2_t5_in += MAS_in[0]

	T2_t5_mem0 = S.Task('T2_t5_mem0', length=1, delay_cost=1)
	S += T2_t5_mem0 >= 33
	T2_t5_mem0 += MM_MEM[0]

	T2_t5_mem1 = S.Task('T2_t5_mem1', length=1, delay_cost=1)
	S += T2_t5_mem1 >= 33
	T2_t5_mem1 += MM_MEM[1]

	T8_t1_in = S.Task('T8_t1_in', length=1, delay_cost=1)
	S += T8_t1_in >= 33
	T8_t1_in += MM_in[0]

	T8_t1_mem0 = S.Task('T8_t1_mem0', length=1, delay_cost=1)
	S += T8_t1_mem0 >= 33
	T8_t1_mem0 += MAIN_MEM_r[0]

	T8_t1_mem1 = S.Task('T8_t1_mem1', length=1, delay_cost=1)
	S += T8_t1_mem1 >= 33
	T8_t1_mem1 += MAS_MEM[1]

	T2_t5 = S.Task('T2_t5', length=3, delay_cost=1)
	S += T2_t5 >= 34
	T2_t5 += MAS[0]

	T31_in = S.Task('T31_in', length=1, delay_cost=1)
	S += T31_in >= 34
	T31_in += MAS_in[0]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 34
	T31_mem0 += MM_MEM[0]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 34
	T31_mem1 += MAS_MEM[1]

	T8_t1 = S.Task('T8_t1', length=11, delay_cost=1)
	S += T8_t1 >= 34
	T8_t1 += MM[0]

	T1_t5_in = S.Task('T1_t5_in', length=1, delay_cost=1)
	S += T1_t5_in >= 35
	T1_t5_in += MAS_in[0]

	T1_t5_mem0 = S.Task('T1_t5_mem0', length=1, delay_cost=1)
	S += T1_t5_mem0 >= 35
	T1_t5_mem0 += MM_MEM[0]

	T1_t5_mem1 = S.Task('T1_t5_mem1', length=1, delay_cost=1)
	S += T1_t5_mem1 >= 35
	T1_t5_mem1 += MM_MEM[1]

	T31 = S.Task('T31', length=3, delay_cost=1)
	S += T31 >= 35
	T31 += MAS[0]

	T9_t1_in = S.Task('T9_t1_in', length=1, delay_cost=1)
	S += T9_t1_in >= 35
	T9_t1_in += MM_in[0]

	T9_t1_mem0 = S.Task('T9_t1_mem0', length=1, delay_cost=1)
	S += T9_t1_mem0 >= 35
	T9_t1_mem0 += MAIN_MEM_r[0]

	T9_t1_mem1 = S.Task('T9_t1_mem1', length=1, delay_cost=1)
	S += T9_t1_mem1 >= 35
	T9_t1_mem1 += MAS_MEM[1]

	T130_in = S.Task('T130_in', length=1, delay_cost=1)
	S += T130_in >= 36
	T130_in += MAS_in[0]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 36
	T130_mem0 += MAS_MEM[0]

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 36
	T130_mem1 += MAS_MEM[1]

	T1_t5 = S.Task('T1_t5', length=3, delay_cost=1)
	S += T1_t5 >= 36
	T1_t5 += MAS[0]

	T9_t1 = S.Task('T9_t1', length=11, delay_cost=1)
	S += T9_t1 >= 36
	T9_t1 += MM[0]

	T11_t1_in = S.Task('T11_t1_in', length=1, delay_cost=1)
	S += T11_t1_in >= 37
	T11_t1_in += MM_in[0]

	T11_t1_mem0 = S.Task('T11_t1_mem0', length=1, delay_cost=1)
	S += T11_t1_mem0 >= 37
	T11_t1_mem0 += MAIN_MEM_r[0]

	T11_t1_mem1 = S.Task('T11_t1_mem1', length=1, delay_cost=1)
	S += T11_t1_mem1 >= 37
	T11_t1_mem1 += MAS_MEM[1]

	T130 = S.Task('T130', length=3, delay_cost=1)
	S += T130 >= 37
	T130 += MAS[0]

	T6_t5_in = S.Task('T6_t5_in', length=1, delay_cost=1)
	S += T6_t5_in >= 37
	T6_t5_in += MAS_in[0]

	T6_t5_mem0 = S.Task('T6_t5_mem0', length=1, delay_cost=1)
	S += T6_t5_mem0 >= 37
	T6_t5_mem0 += MM_MEM[0]

	T6_t5_mem1 = S.Task('T6_t5_mem1', length=1, delay_cost=1)
	S += T6_t5_mem1 >= 37
	T6_t5_mem1 += MM_MEM[1]

	T10_t1_in = S.Task('T10_t1_in', length=1, delay_cost=1)
	S += T10_t1_in >= 38
	T10_t1_in += MM_in[0]

	T10_t1_mem0 = S.Task('T10_t1_mem0', length=1, delay_cost=1)
	S += T10_t1_mem0 >= 38
	T10_t1_mem0 += MAIN_MEM_r[0]

	T10_t1_mem1 = S.Task('T10_t1_mem1', length=1, delay_cost=1)
	S += T10_t1_mem1 >= 38
	T10_t1_mem1 += MAS_MEM[1]

	T11_t1 = S.Task('T11_t1', length=11, delay_cost=1)
	S += T11_t1 >= 38
	T11_t1 += MM[0]

	T6_t5 = S.Task('T6_t5', length=3, delay_cost=1)
	S += T6_t5 >= 38
	T6_t5 += MAS[0]

	T70_in = S.Task('T70_in', length=1, delay_cost=1)
	S += T70_in >= 38
	T70_in += MAS_in[0]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 38
	T70_mem0 += MM_MEM[0]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 38
	T70_mem1 += MM_MEM[1]

	T10_t1 = S.Task('T10_t1', length=11, delay_cost=1)
	S += T10_t1 >= 39
	T10_t1 += MM[0]

	T14_t0_in = S.Task('T14_t0_in', length=1, delay_cost=1)
	S += T14_t0_in >= 39
	T14_t0_in += MM_in[0]

	T14_t0_mem0 = S.Task('T14_t0_mem0', length=1, delay_cost=1)
	S += T14_t0_mem0 >= 39
	T14_t0_mem0 += MAS_MEM[0]

	T14_t0_mem1 = S.Task('T14_t0_mem1', length=1, delay_cost=1)
	S += T14_t0_mem1 >= 39
	T14_t0_mem1 += MAS_MEM[1]

	T70 = S.Task('T70', length=3, delay_cost=1)
	S += T70 >= 39
	T70 += MAS[0]

	T7_t5_in = S.Task('T7_t5_in', length=1, delay_cost=1)
	S += T7_t5_in >= 39
	T7_t5_in += MAS_in[0]

	T7_t5_mem0 = S.Task('T7_t5_mem0', length=1, delay_cost=1)
	S += T7_t5_mem0 >= 39
	T7_t5_mem0 += MM_MEM[0]

	T7_t5_mem1 = S.Task('T7_t5_mem1', length=1, delay_cost=1)
	S += T7_t5_mem1 >= 39
	T7_t5_mem1 += MM_MEM[1]

	T14_t0 = S.Task('T14_t0', length=11, delay_cost=1)
	S += T14_t0 >= 40
	T14_t0 += MM[0]

	T50_in = S.Task('T50_in', length=1, delay_cost=1)
	S += T50_in >= 40
	T50_in += MAS_in[0]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 40
	T50_mem0 += MM_MEM[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 40
	T50_mem1 += MAS_MEM[1]

	T7_t5 = S.Task('T7_t5', length=3, delay_cost=1)
	S += T7_t5 >= 40
	T7_t5 += MAS[0]

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	S += T10_in >= 41
	T10_in += MAS_in[0]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 41
	T10_mem0 += MM_MEM[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 41
	T10_mem1 += MAS_MEM[1]

	T50 = S.Task('T50', length=3, delay_cost=1)
	S += T50 >= 41
	T50 += MAS[0]

	T10 = S.Task('T10', length=3, delay_cost=1)
	S += T10 >= 42
	T10 += MAS[0]

	T120_in = S.Task('T120_in', length=1, delay_cost=1)
	S += T120_in >= 42
	T120_in += MAS_in[0]

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	S += T120_mem0 >= 42
	T120_mem0 += MAS_MEM[0]

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	S += T120_mem1 >= 42
	T120_mem1 += MAS_MEM[1]

	T120 = S.Task('T120', length=3, delay_cost=1)
	S += T120 >= 43
	T120 += MAS[0]

	T21_in = S.Task('T21_in', length=1, delay_cost=1)
	S += T21_in >= 43
	T21_in += MAS_in[0]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 43
	T21_mem0 += MM_MEM[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 43
	T21_mem1 += MAS_MEM[1]

	T21 = S.Task('T21', length=3, delay_cost=1)
	S += T21 >= 44
	T21 += MAS[0]

	T4_t5_in = S.Task('T4_t5_in', length=1, delay_cost=1)
	S += T4_t5_in >= 44
	T4_t5_in += MAS_in[0]

	T4_t5_mem0 = S.Task('T4_t5_mem0', length=1, delay_cost=1)
	S += T4_t5_mem0 >= 44
	T4_t5_mem0 += MM_MEM[0]

	T4_t5_mem1 = S.Task('T4_t5_mem1', length=1, delay_cost=1)
	S += T4_t5_mem1 >= 44
	T4_t5_mem1 += MM_MEM[1]

	T9_t0_in = S.Task('T9_t0_in', length=1, delay_cost=1)
	S += T9_t0_in >= 44
	T9_t0_in += MM_in[0]

	T9_t0_mem0 = S.Task('T9_t0_mem0', length=1, delay_cost=1)
	S += T9_t0_mem0 >= 44
	T9_t0_mem0 += MAIN_MEM_r[0]

	T9_t0_mem1 = S.Task('T9_t0_mem1', length=1, delay_cost=1)
	S += T9_t0_mem1 >= 44
	T9_t0_mem1 += MAS_MEM[1]

	T4_t5 = S.Task('T4_t5', length=3, delay_cost=1)
	S += T4_t5 >= 45
	T4_t5 += MAS[0]

	T60_in = S.Task('T60_in', length=1, delay_cost=1)
	S += T60_in >= 45
	T60_in += MAS_in[0]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 45
	T60_mem0 += MM_MEM[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 45
	T60_mem1 += MM_MEM[1]

	T8_t0_in = S.Task('T8_t0_in', length=1, delay_cost=1)
	S += T8_t0_in >= 45
	T8_t0_in += MM_in[0]

	T8_t0_mem0 = S.Task('T8_t0_mem0', length=1, delay_cost=1)
	S += T8_t0_mem0 >= 45
	T8_t0_mem0 += MAIN_MEM_r[0]

	T8_t0_mem1 = S.Task('T8_t0_mem1', length=1, delay_cost=1)
	S += T8_t0_mem1 >= 45
	T8_t0_mem1 += MAS_MEM[1]

	T9_t0 = S.Task('T9_t0', length=11, delay_cost=1)
	S += T9_t0 >= 45
	T9_t0 += MM[0]

	T60 = S.Task('T60', length=3, delay_cost=1)
	S += T60 >= 46
	T60 += MAS[0]

	T8_t0 = S.Task('T8_t0', length=11, delay_cost=1)
	S += T8_t0 >= 46
	T8_t0 += MM[0]

	T9_t3_in = S.Task('T9_t3_in', length=1, delay_cost=1)
	S += T9_t3_in >= 46
	T9_t3_in += MAS_in[0]

	T9_t3_mem0 = S.Task('T9_t3_mem0', length=1, delay_cost=1)
	S += T9_t3_mem0 >= 46
	T9_t3_mem0 += MAS_MEM[0]

	T9_t3_mem1 = S.Task('T9_t3_mem1', length=1, delay_cost=1)
	S += T9_t3_mem1 >= 46
	T9_t3_mem1 += MAS_MEM[1]

	T71_in = S.Task('T71_in', length=1, delay_cost=1)
	S += T71_in >= 47
	T71_in += MAS_in[0]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 47
	T71_mem0 += MM_MEM[0]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 47
	T71_mem1 += MAS_MEM[1]

	T9_t3 = S.Task('T9_t3', length=3, delay_cost=1)
	S += T9_t3 >= 47
	T9_t3 += MAS[0]

	T41_in = S.Task('T41_in', length=1, delay_cost=1)
	S += T41_in >= 48
	T41_in += MAS_in[0]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 48
	T41_mem0 += MM_MEM[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 48
	T41_mem1 += MAS_MEM[1]

	T71 = S.Task('T71', length=3, delay_cost=1)
	S += T71 >= 48
	T71 += MAS[0]

	T150_in = S.Task('T150_in', length=1, delay_cost=1)
	S += T150_in >= 49
	T150_in += MAS_in[0]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 49
	T150_mem0 += MAS_MEM[0]

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 49
	T150_mem1 += MAS_MEM[1]

	T41 = S.Task('T41', length=3, delay_cost=1)
	S += T41 >= 49
	T41 += MAS[0]

	T150 = S.Task('T150', length=3, delay_cost=1)
	S += T150 >= 50
	T150 += MAS[0]

	T8_t3_in = S.Task('T8_t3_in', length=1, delay_cost=1)
	S += T8_t3_in >= 50
	T8_t3_in += MAS_in[0]

	T8_t3_mem0 = S.Task('T8_t3_mem0', length=1, delay_cost=1)
	S += T8_t3_mem0 >= 50
	T8_t3_mem0 += MAS_MEM[0]

	T8_t3_mem1 = S.Task('T8_t3_mem1', length=1, delay_cost=1)
	S += T8_t3_mem1 >= 50
	T8_t3_mem1 += MAS_MEM[1]

	T131_in = S.Task('T131_in', length=1, delay_cost=1)
	S += T131_in >= 51
	T131_in += MAS_in[0]

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 51
	T131_mem0 += MAS_MEM[0]

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 51
	T131_mem1 += MAS_MEM[1]

	T8_t3 = S.Task('T8_t3', length=3, delay_cost=1)
	S += T8_t3 >= 51
	T8_t3 += MAS[0]

	T131 = S.Task('T131', length=3, delay_cost=1)
	S += T131 >= 52
	T131 += MAS[0]

	T151_in = S.Task('T151_in', length=1, delay_cost=1)
	S += T151_in >= 52
	T151_in += MAS_in[0]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 52
	T151_mem0 += MAS_MEM[0]

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 52
	T151_mem1 += MAS_MEM[1]

	T151 = S.Task('T151', length=3, delay_cost=1)
	S += T151 >= 53
	T151 += MAS[0]

	T16_t2_in = S.Task('T16_t2_in', length=1, delay_cost=1)
	S += T16_t2_in >= 53
	T16_t2_in += MAS_in[0]

	T16_t2_mem0 = S.Task('T16_t2_mem0', length=1, delay_cost=1)
	S += T16_t2_mem0 >= 53
	T16_t2_mem0 += MAS_MEM[0]

	T16_t2_mem1 = S.Task('T16_t2_mem1', length=1, delay_cost=1)
	S += T16_t2_mem1 >= 53
	T16_t2_mem1 += MAS_MEM[1]

	T16_t2 = S.Task('T16_t2', length=3, delay_cost=1)
	S += T16_t2 >= 54
	T16_t2 += MAS[0]

	T61_in = S.Task('T61_in', length=1, delay_cost=1)
	S += T61_in >= 54
	T61_in += MAS_in[0]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 54
	T61_mem0 += MM_MEM[0]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 54
	T61_mem1 += MAS_MEM[1]

	T11_t3_in = S.Task('T11_t3_in', length=1, delay_cost=1)
	S += T11_t3_in >= 55
	T11_t3_in += MAS_in[0]

	T11_t3_mem0 = S.Task('T11_t3_mem0', length=1, delay_cost=1)
	S += T11_t3_mem0 >= 55
	T11_t3_mem0 += MAS_MEM[0]

	T11_t3_mem1 = S.Task('T11_t3_mem1', length=1, delay_cost=1)
	S += T11_t3_mem1 >= 55
	T11_t3_mem1 += MAS_MEM[1]

	T61 = S.Task('T61', length=3, delay_cost=1)
	S += T61 >= 55
	T61 += MAS[0]

	T10_t3_in = S.Task('T10_t3_in', length=1, delay_cost=1)
	S += T10_t3_in >= 56
	T10_t3_in += MAS_in[0]

	T10_t3_mem0 = S.Task('T10_t3_mem0', length=1, delay_cost=1)
	S += T10_t3_mem0 >= 56
	T10_t3_mem0 += MAS_MEM[0]

	T10_t3_mem1 = S.Task('T10_t3_mem1', length=1, delay_cost=1)
	S += T10_t3_mem1 >= 56
	T10_t3_mem1 += MAS_MEM[1]

	T11_t3 = S.Task('T11_t3', length=3, delay_cost=1)
	S += T11_t3 >= 56
	T11_t3 += MAS[0]

	T10_t3 = S.Task('T10_t3', length=3, delay_cost=1)
	S += T10_t3 >= 57
	T10_t3 += MAS[0]

	T121_in = S.Task('T121_in', length=1, delay_cost=1)
	S += T121_in >= 57
	T121_in += MAS_in[0]

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	S += T121_mem0 >= 57
	T121_mem0 += MAS_MEM[0]

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	S += T121_mem1 >= 57
	T121_mem1 += MAS_MEM[1]

	T121 = S.Task('T121', length=3, delay_cost=1)
	S += T121 >= 58
	T121 += MAS[0]

	T14_t1_in = S.Task('T14_t1_in', length=1, delay_cost=1)
	S += T14_t1_in >= 58
	T14_t1_in += MM_in[0]

	T14_t1_mem0 = S.Task('T14_t1_mem0', length=1, delay_cost=1)
	S += T14_t1_mem0 >= 58
	T14_t1_mem0 += MAS_MEM[0]

	T14_t1_mem1 = S.Task('T14_t1_mem1', length=1, delay_cost=1)
	S += T14_t1_mem1 >= 58
	T14_t1_mem1 += MAS_MEM[1]

	Z3_t2_in = S.Task('Z3_t2_in', length=1, delay_cost=1)
	S += Z3_t2_in >= 58
	Z3_t2_in += MAS_in[0]

	Z3_t2_mem0 = S.Task('Z3_t2_mem0', length=1, delay_cost=1)
	S += Z3_t2_mem0 >= 58
	Z3_t2_mem0 += MAIN_MEM_r[0]

	Z3_t2_mem1 = S.Task('Z3_t2_mem1', length=1, delay_cost=1)
	S += Z3_t2_mem1 >= 58
	Z3_t2_mem1 += MAIN_MEM_r[1]

	T14_t1 = S.Task('T14_t1', length=11, delay_cost=1)
	S += T14_t1 >= 59
	T14_t1 += MM[0]

	T51_in = S.Task('T51_in', length=1, delay_cost=1)
	S += T51_in >= 59
	T51_in += MAS_in[0]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 59
	T51_mem0 += MM_MEM[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 59
	T51_mem1 += MM_MEM[1]

	T8_t4_in = S.Task('T8_t4_in', length=1, delay_cost=1)
	S += T8_t4_in >= 59
	T8_t4_in += MM_in[0]

	T8_t4_mem0 = S.Task('T8_t4_mem0', length=1, delay_cost=1)
	S += T8_t4_mem0 >= 59
	T8_t4_mem0 += MAS_MEM[0]

	T8_t4_mem1 = S.Task('T8_t4_mem1', length=1, delay_cost=1)
	S += T8_t4_mem1 >= 59
	T8_t4_mem1 += MAS_MEM[1]

	Z3_t2 = S.Task('Z3_t2', length=3, delay_cost=1)
	S += Z3_t2 >= 59
	Z3_t2 += MAS[0]

	T11_t4_in = S.Task('T11_t4_in', length=1, delay_cost=1)
	S += T11_t4_in >= 60
	T11_t4_in += MM_in[0]

	T11_t4_mem0 = S.Task('T11_t4_mem0', length=1, delay_cost=1)
	S += T11_t4_mem0 >= 60
	T11_t4_mem0 += MAS_MEM[0]

	T11_t4_mem1 = S.Task('T11_t4_mem1', length=1, delay_cost=1)
	S += T11_t4_mem1 >= 60
	T11_t4_mem1 += MAS_MEM[1]

	T51 = S.Task('T51', length=3, delay_cost=1)
	S += T51 >= 60
	T51 += MAS[0]

	T80_in = S.Task('T80_in', length=1, delay_cost=1)
	S += T80_in >= 60
	T80_in += MAS_in[0]

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	S += T80_mem0 >= 60
	T80_mem0 += MM_MEM[0]

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	S += T80_mem1 >= 60
	T80_mem1 += MM_MEM[1]

	T8_t4 = S.Task('T8_t4', length=11, delay_cost=1)
	S += T8_t4 >= 60
	T8_t4 += MM[0]

	T110_in = S.Task('T110_in', length=1, delay_cost=1)
	S += T110_in >= 61
	T110_in += MAS_in[0]

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	S += T110_mem0 >= 61
	T110_mem0 += MM_MEM[0]

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	S += T110_mem1 >= 61
	T110_mem1 += MM_MEM[1]

	T11_t4 = S.Task('T11_t4', length=11, delay_cost=1)
	S += T11_t4 >= 61
	T11_t4 += MM[0]

	T80 = S.Task('T80', length=3, delay_cost=1)
	S += T80 >= 61
	T80 += MAS[0]

	T9_t4_in = S.Task('T9_t4_in', length=1, delay_cost=1)
	S += T9_t4_in >= 61
	T9_t4_in += MM_in[0]

	T9_t4_mem0 = S.Task('T9_t4_mem0', length=1, delay_cost=1)
	S += T9_t4_mem0 >= 61
	T9_t4_mem0 += MAS_MEM[0]

	T9_t4_mem1 = S.Task('T9_t4_mem1', length=1, delay_cost=1)
	S += T9_t4_mem1 >= 61
	T9_t4_mem1 += MAS_MEM[1]

	T10_t4_in = S.Task('T10_t4_in', length=1, delay_cost=1)
	S += T10_t4_in >= 62
	T10_t4_in += MM_in[0]

	T10_t4_mem0 = S.Task('T10_t4_mem0', length=1, delay_cost=1)
	S += T10_t4_mem0 >= 62
	T10_t4_mem0 += MAS_MEM[0]

	T10_t4_mem1 = S.Task('T10_t4_mem1', length=1, delay_cost=1)
	S += T10_t4_mem1 >= 62
	T10_t4_mem1 += MAS_MEM[1]

	T110 = S.Task('T110', length=3, delay_cost=1)
	S += T110 >= 62
	T110 += MAS[0]

	T90_in = S.Task('T90_in', length=1, delay_cost=1)
	S += T90_in >= 62
	T90_in += MAS_in[0]

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	S += T90_mem0 >= 62
	T90_mem0 += MM_MEM[0]

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	S += T90_mem1 >= 62
	T90_mem1 += MM_MEM[1]

	T9_t4 = S.Task('T9_t4', length=11, delay_cost=1)
	S += T9_t4 >= 62
	T9_t4 += MM[0]

	T10_t4 = S.Task('T10_t4', length=11, delay_cost=1)
	S += T10_t4 >= 63
	T10_t4 += MM[0]

	T11_t5_in = S.Task('T11_t5_in', length=1, delay_cost=1)
	S += T11_t5_in >= 63
	T11_t5_in += MAS_in[0]

	T11_t5_mem0 = S.Task('T11_t5_mem0', length=1, delay_cost=1)
	S += T11_t5_mem0 >= 63
	T11_t5_mem0 += MM_MEM[0]

	T11_t5_mem1 = S.Task('T11_t5_mem1', length=1, delay_cost=1)
	S += T11_t5_mem1 >= 63
	T11_t5_mem1 += MM_MEM[1]

	T16_t0_in = S.Task('T16_t0_in', length=1, delay_cost=1)
	S += T16_t0_in >= 63
	T16_t0_in += MM_in[0]

	T16_t0_mem0 = S.Task('T16_t0_mem0', length=1, delay_cost=1)
	S += T16_t0_mem0 >= 63
	T16_t0_mem0 += MAS_MEM[0]

	T16_t0_mem1 = S.Task('T16_t0_mem1', length=1, delay_cost=1)
	S += T16_t0_mem1 >= 63
	T16_t0_mem1 += MAS_MEM[1]

	T90 = S.Task('T90', length=3, delay_cost=1)
	S += T90 >= 63
	T90 += MAS[0]

	T11_t5 = S.Task('T11_t5', length=3, delay_cost=1)
	S += T11_t5 >= 64
	T11_t5 += MAS[0]

	T16_t0 = S.Task('T16_t0', length=11, delay_cost=1)
	S += T16_t0 >= 64
	T16_t0 += MM[0]

	T24_t0_in = S.Task('T24_t0_in', length=1, delay_cost=1)
	S += T24_t0_in >= 64
	T24_t0_in += MM_in[0]

	T24_t0_mem0 = S.Task('T24_t0_mem0', length=1, delay_cost=1)
	S += T24_t0_mem0 >= 64
	T24_t0_mem0 += MAS_MEM[0]

	T24_t0_mem1 = S.Task('T24_t0_mem1', length=1, delay_cost=1)
	S += T24_t0_mem1 >= 64
	T24_t0_mem1 += MAS_MEM[1]

	T9_t5_in = S.Task('T9_t5_in', length=1, delay_cost=1)
	S += T9_t5_in >= 64
	T9_t5_in += MAS_in[0]

	T9_t5_mem0 = S.Task('T9_t5_mem0', length=1, delay_cost=1)
	S += T9_t5_mem0 >= 64
	T9_t5_mem0 += MM_MEM[0]

	T9_t5_mem1 = S.Task('T9_t5_mem1', length=1, delay_cost=1)
	S += T9_t5_mem1 >= 64
	T9_t5_mem1 += MM_MEM[1]

	T17_t0_in = S.Task('T17_t0_in', length=1, delay_cost=1)
	S += T17_t0_in >= 65
	T17_t0_in += MM_in[0]

	T17_t0_mem0 = S.Task('T17_t0_mem0', length=1, delay_cost=1)
	S += T17_t0_mem0 >= 65
	T17_t0_mem0 += MAS_MEM[0]

	T17_t0_mem1 = S.Task('T17_t0_mem1', length=1, delay_cost=1)
	S += T17_t0_mem1 >= 65
	T17_t0_mem1 += MAS_MEM[1]

	T24_t0 = S.Task('T24_t0', length=11, delay_cost=1)
	S += T24_t0 >= 65
	T24_t0 += MM[0]

	T8_t5_in = S.Task('T8_t5_in', length=1, delay_cost=1)
	S += T8_t5_in >= 65
	T8_t5_in += MAS_in[0]

	T8_t5_mem0 = S.Task('T8_t5_mem0', length=1, delay_cost=1)
	S += T8_t5_mem0 >= 65
	T8_t5_mem0 += MM_MEM[0]

	T8_t5_mem1 = S.Task('T8_t5_mem1', length=1, delay_cost=1)
	S += T8_t5_mem1 >= 65
	T8_t5_mem1 += MM_MEM[1]

	T9_t5 = S.Task('T9_t5', length=3, delay_cost=1)
	S += T9_t5 >= 65
	T9_t5 += MAS[0]

	T17_t0 = S.Task('T17_t0', length=11, delay_cost=1)
	S += T17_t0 >= 66
	T17_t0 += MM[0]

	T180_in = S.Task('T180_in', length=1, delay_cost=1)
	S += T180_in >= 66
	T180_in += MAS_in[0]

	T180_mem0 = S.Task('T180_mem0', length=1, delay_cost=1)
	S += T180_mem0 >= 66
	T180_mem0 += MAS_MEM[0]

	T180_mem1 = S.Task('T180_mem1', length=1, delay_cost=1)
	S += T180_mem1 >= 66
	T180_mem1 += MAS_MEM[1]

	T8_t5 = S.Task('T8_t5', length=3, delay_cost=1)
	S += T8_t5 >= 66
	T8_t5 += MAS[0]

	T14_t2_in = S.Task('T14_t2_in', length=1, delay_cost=1)
	S += T14_t2_in >= 67
	T14_t2_in += MAS_in[0]

	T14_t2_mem0 = S.Task('T14_t2_mem0', length=1, delay_cost=1)
	S += T14_t2_mem0 >= 67
	T14_t2_mem0 += MAS_MEM[0]

	T14_t2_mem1 = S.Task('T14_t2_mem1', length=1, delay_cost=1)
	S += T14_t2_mem1 >= 67
	T14_t2_mem1 += MAS_MEM[1]

	T180 = S.Task('T180', length=3, delay_cost=1)
	S += T180 >= 67
	T180 += MAS[0]

	T14_t2 = S.Task('T14_t2', length=3, delay_cost=1)
	S += T14_t2 >= 68
	T14_t2 += MAS[0]

	T14_t3_in = S.Task('T14_t3_in', length=1, delay_cost=1)
	S += T14_t3_in >= 68
	T14_t3_in += MAS_in[0]

	T14_t3_mem0 = S.Task('T14_t3_mem0', length=1, delay_cost=1)
	S += T14_t3_mem0 >= 68
	T14_t3_mem0 += MAS_MEM[0]

	T14_t3_mem1 = S.Task('T14_t3_mem1', length=1, delay_cost=1)
	S += T14_t3_mem1 >= 68
	T14_t3_mem1 += MAS_MEM[1]

	T140_in = S.Task('T140_in', length=1, delay_cost=1)
	S += T140_in >= 69
	T140_in += MAS_in[0]

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 69
	T140_mem0 += MM_MEM[0]

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 69
	T140_mem1 += MM_MEM[1]

	T14_t3 = S.Task('T14_t3', length=3, delay_cost=1)
	S += T14_t3 >= 69
	T14_t3 += MAS[0]

	T20_t0_in = S.Task('T20_t0_in', length=1, delay_cost=1)
	S += T20_t0_in >= 69
	T20_t0_in += MM_in[0]

	T20_t0_mem0 = S.Task('T20_t0_mem0', length=1, delay_cost=1)
	S += T20_t0_mem0 >= 69
	T20_t0_mem0 += MAS_MEM[0]

	T20_t0_mem1 = S.Task('T20_t0_mem1', length=1, delay_cost=1)
	S += T20_t0_mem1 >= 69
	T20_t0_mem1 += MAS_MEM[1]

	T140 = S.Task('T140', length=3, delay_cost=1)
	S += T140 >= 70
	T140 += MAS[0]

	T20_t0 = S.Task('T20_t0', length=11, delay_cost=1)
	S += T20_t0 >= 70
	T20_t0 += MM[0]

	T81_in = S.Task('T81_in', length=1, delay_cost=1)
	S += T81_in >= 70
	T81_in += MAS_in[0]

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	S += T81_mem0 >= 70
	T81_mem0 += MM_MEM[0]

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	S += T81_mem1 >= 70
	T81_mem1 += MAS_MEM[1]

	T100_in = S.Task('T100_in', length=1, delay_cost=1)
	S += T100_in >= 71
	T100_in += MAS_in[0]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 71
	T100_mem0 += MM_MEM[0]

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 71
	T100_mem1 += MM_MEM[1]

	T14_t4_in = S.Task('T14_t4_in', length=1, delay_cost=1)
	S += T14_t4_in >= 71
	T14_t4_in += MM_in[0]

	T14_t4_mem0 = S.Task('T14_t4_mem0', length=1, delay_cost=1)
	S += T14_t4_mem0 >= 71
	T14_t4_mem0 += MAS_MEM[0]

	T14_t4_mem1 = S.Task('T14_t4_mem1', length=1, delay_cost=1)
	S += T14_t4_mem1 >= 71
	T14_t4_mem1 += MAS_MEM[1]

	T81 = S.Task('T81', length=3, delay_cost=1)
	S += T81 >= 71
	T81 += MAS[0]

	T100 = S.Task('T100', length=3, delay_cost=1)
	S += T100 >= 72
	T100 += MAS[0]

	T10_t5_in = S.Task('T10_t5_in', length=1, delay_cost=1)
	S += T10_t5_in >= 72
	T10_t5_in += MAS_in[0]

	T10_t5_mem0 = S.Task('T10_t5_mem0', length=1, delay_cost=1)
	S += T10_t5_mem0 >= 72
	T10_t5_mem0 += MM_MEM[0]

	T10_t5_mem1 = S.Task('T10_t5_mem1', length=1, delay_cost=1)
	S += T10_t5_mem1 >= 72
	T10_t5_mem1 += MM_MEM[1]

	T14_t4 = S.Task('T14_t4', length=11, delay_cost=1)
	S += T14_t4 >= 72
	T14_t4 += MM[0]

	Z3_t0_in = S.Task('Z3_t0_in', length=1, delay_cost=1)
	S += Z3_t0_in >= 72
	Z3_t0_in += MM_in[0]

	Z3_t0_mem0 = S.Task('Z3_t0_mem0', length=1, delay_cost=1)
	S += Z3_t0_mem0 >= 72
	Z3_t0_mem0 += MAIN_MEM_r[0]

	Z3_t0_mem1 = S.Task('Z3_t0_mem1', length=1, delay_cost=1)
	S += Z3_t0_mem1 >= 72
	Z3_t0_mem1 += MAS_MEM[1]

	T10_t5 = S.Task('T10_t5', length=3, delay_cost=1)
	S += T10_t5 >= 73
	T10_t5 += MAS[0]

	T14_t5_in = S.Task('T14_t5_in', length=1, delay_cost=1)
	S += T14_t5_in >= 73
	T14_t5_in += MAS_in[0]

	T14_t5_mem0 = S.Task('T14_t5_mem0', length=1, delay_cost=1)
	S += T14_t5_mem0 >= 73
	T14_t5_mem0 += MM_MEM[0]

	T14_t5_mem1 = S.Task('T14_t5_mem1', length=1, delay_cost=1)
	S += T14_t5_mem1 >= 73
	T14_t5_mem1 += MM_MEM[1]

	T17_t1_in = S.Task('T17_t1_in', length=1, delay_cost=1)
	S += T17_t1_in >= 73
	T17_t1_in += MM_in[0]

	T17_t1_mem0 = S.Task('T17_t1_mem0', length=1, delay_cost=1)
	S += T17_t1_mem0 >= 73
	T17_t1_mem0 += MAS_MEM[0]

	T17_t1_mem1 = S.Task('T17_t1_mem1', length=1, delay_cost=1)
	S += T17_t1_mem1 >= 73
	T17_t1_mem1 += MAS_MEM[1]

	Z3_t0 = S.Task('Z3_t0', length=11, delay_cost=1)
	S += Z3_t0 >= 73
	Z3_t0 += MM[0]

	T111_in = S.Task('T111_in', length=1, delay_cost=1)
	S += T111_in >= 74
	T111_in += MAS_in[0]

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	S += T111_mem0 >= 74
	T111_mem0 += MM_MEM[0]

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	S += T111_mem1 >= 74
	T111_mem1 += MAS_MEM[1]

	T14_t5 = S.Task('T14_t5', length=3, delay_cost=1)
	S += T14_t5 >= 74
	T14_t5 += MAS[0]

	T17_t1 = S.Task('T17_t1', length=11, delay_cost=1)
	S += T17_t1 >= 74
	T17_t1 += MM[0]

	T111 = S.Task('T111', length=3, delay_cost=1)
	S += T111 >= 75
	T111 += MAS[0]

	T16_t3_in = S.Task('T16_t3_in', length=1, delay_cost=1)
	S += T16_t3_in >= 75
	T16_t3_in += MAS_in[0]

	T16_t3_mem0 = S.Task('T16_t3_mem0', length=1, delay_cost=1)
	S += T16_t3_mem0 >= 75
	T16_t3_mem0 += MAS_MEM[0]

	T16_t3_mem1 = S.Task('T16_t3_mem1', length=1, delay_cost=1)
	S += T16_t3_mem1 >= 75
	T16_t3_mem1 += MAS_MEM[1]

	T16_t3 = S.Task('T16_t3', length=3, delay_cost=1)
	S += T16_t3 >= 76
	T16_t3 += MAS[0]

	T190_in = S.Task('T190_in', length=1, delay_cost=1)
	S += T190_in >= 76
	T190_in += MAS_in[0]

	T190_mem0 = S.Task('T190_mem0', length=1, delay_cost=1)
	S += T190_mem0 >= 76
	T190_mem0 += MAS_MEM[0]

	T190_mem1 = S.Task('T190_mem1', length=1, delay_cost=1)
	S += T190_mem1 >= 76
	T190_mem1 += MAS_MEM[1]

	T17_t2_in = S.Task('T17_t2_in', length=1, delay_cost=1)
	S += T17_t2_in >= 77
	T17_t2_in += MAS_in[0]

	T17_t2_mem0 = S.Task('T17_t2_mem0', length=1, delay_cost=1)
	S += T17_t2_mem0 >= 77
	T17_t2_mem0 += MAS_MEM[0]

	T17_t2_mem1 = S.Task('T17_t2_mem1', length=1, delay_cost=1)
	S += T17_t2_mem1 >= 77
	T17_t2_mem1 += MAS_MEM[1]

	T190 = S.Task('T190', length=3, delay_cost=1)
	S += T190 >= 77
	T190 += MAS[0]

	T17_t2 = S.Task('T17_t2', length=3, delay_cost=1)
	S += T17_t2 >= 78
	T17_t2 += MAS[0]

	T91_in = S.Task('T91_in', length=1, delay_cost=1)
	S += T91_in >= 78
	T91_in += MAS_in[0]

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	S += T91_mem0 >= 78
	T91_mem0 += MM_MEM[0]

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	S += T91_mem1 >= 78
	T91_mem1 += MAS_MEM[1]

	T16_t1_in = S.Task('T16_t1_in', length=1, delay_cost=1)
	S += T16_t1_in >= 79
	T16_t1_in += MM_in[0]

	T16_t1_mem0 = S.Task('T16_t1_mem0', length=1, delay_cost=1)
	S += T16_t1_mem0 >= 79
	T16_t1_mem0 += MAS_MEM[0]

	T16_t1_mem1 = S.Task('T16_t1_mem1', length=1, delay_cost=1)
	S += T16_t1_mem1 >= 79
	T16_t1_mem1 += MAS_MEM[1]

	T91 = S.Task('T91', length=3, delay_cost=1)
	S += T91 >= 79
	T91 += MAS[0]

	T101_in = S.Task('T101_in', length=1, delay_cost=1)
	S += T101_in >= 80
	T101_in += MAS_in[0]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 80
	T101_mem0 += MM_MEM[0]

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 80
	T101_mem1 += MAS_MEM[1]

	T16_t1 = S.Task('T16_t1', length=11, delay_cost=1)
	S += T16_t1 >= 80
	T16_t1 += MM[0]

	T101 = S.Task('T101', length=3, delay_cost=1)
	S += T101 >= 81
	T101 += MAS[0]

	T24_t2_in = S.Task('T24_t2_in', length=1, delay_cost=1)
	S += T24_t2_in >= 81
	T24_t2_in += MAS_in[0]

	T24_t2_mem0 = S.Task('T24_t2_mem0', length=1, delay_cost=1)
	S += T24_t2_mem0 >= 81
	T24_t2_mem0 += MAS_MEM[0]

	T24_t2_mem1 = S.Task('T24_t2_mem1', length=1, delay_cost=1)
	S += T24_t2_mem1 >= 81
	T24_t2_mem1 += MAS_MEM[1]

	T191_in = S.Task('T191_in', length=1, delay_cost=1)
	S += T191_in >= 82
	T191_in += MAS_in[0]

	T191_mem0 = S.Task('T191_mem0', length=1, delay_cost=1)
	S += T191_mem0 >= 82
	T191_mem0 += MAS_MEM[0]

	T191_mem1 = S.Task('T191_mem1', length=1, delay_cost=1)
	S += T191_mem1 >= 82
	T191_mem1 += MAS_MEM[1]

	T24_t2 = S.Task('T24_t2', length=3, delay_cost=1)
	S += T24_t2 >= 82
	T24_t2 += MAS[0]

	T191 = S.Task('T191', length=3, delay_cost=1)
	S += T191 >= 83
	T191 += MAS[0]

	T24_t1_in = S.Task('T24_t1_in', length=1, delay_cost=1)
	S += T24_t1_in >= 83
	T24_t1_in += MM_in[0]

	T24_t1_mem0 = S.Task('T24_t1_mem0', length=1, delay_cost=1)
	S += T24_t1_mem0 >= 83
	T24_t1_mem0 += MAS_MEM[0]

	T24_t1_mem1 = S.Task('T24_t1_mem1', length=1, delay_cost=1)
	S += T24_t1_mem1 >= 83
	T24_t1_mem1 += MAS_MEM[1]

	T24_t1 = S.Task('T24_t1', length=11, delay_cost=1)
	S += T24_t1 >= 84
	T24_t1 += MM[0]

	T24_t3_in = S.Task('T24_t3_in', length=1, delay_cost=1)
	S += T24_t3_in >= 84
	T24_t3_in += MAS_in[0]

	T24_t3_mem0 = S.Task('T24_t3_mem0', length=1, delay_cost=1)
	S += T24_t3_mem0 >= 84
	T24_t3_mem0 += MAS_MEM[0]

	T24_t3_mem1 = S.Task('T24_t3_mem1', length=1, delay_cost=1)
	S += T24_t3_mem1 >= 84
	T24_t3_mem1 += MAS_MEM[1]

	T210_in = S.Task('T210_in', length=1, delay_cost=1)
	S += T210_in >= 85
	T210_in += MAS_in[0]

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	S += T210_mem0 >= 85
	T210_mem0 += MAS_MEM[0]

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	S += T210_mem1 >= 85
	T210_mem1 += MAS_MEM[1]

	T24_t3 = S.Task('T24_t3', length=3, delay_cost=1)
	S += T24_t3 >= 85
	T24_t3 += MAS[0]

	T141_in = S.Task('T141_in', length=1, delay_cost=1)
	S += T141_in >= 86
	T141_in += MAS_in[0]

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 86
	T141_mem0 += MM_MEM[0]

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 86
	T141_mem1 += MAS_MEM[1]

	T210 = S.Task('T210', length=3, delay_cost=1)
	S += T210 >= 86
	T210 += MAS[0]

	T141 = S.Task('T141', length=3, delay_cost=1)
	S += T141 >= 87
	T141 += MAS[0]

	T181_in = S.Task('T181_in', length=1, delay_cost=1)
	S += T181_in >= 87
	T181_in += MAS_in[0]

	T181_mem0 = S.Task('T181_mem0', length=1, delay_cost=1)
	S += T181_mem0 >= 87
	T181_mem0 += MAS_MEM[0]

	T181_mem1 = S.Task('T181_mem1', length=1, delay_cost=1)
	S += T181_mem1 >= 87
	T181_mem1 += MAS_MEM[1]

	T181 = S.Task('T181', length=3, delay_cost=1)
	S += T181 >= 88
	T181 += MAS[0]

	T211_in = S.Task('T211_in', length=1, delay_cost=1)
	S += T211_in >= 88
	T211_in += MAS_in[0]

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	S += T211_mem0 >= 88
	T211_mem0 += MAS_MEM[0]

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	S += T211_mem1 >= 88
	T211_mem1 += MAS_MEM[1]

	T20_t2_in = S.Task('T20_t2_in', length=1, delay_cost=1)
	S += T20_t2_in >= 89
	T20_t2_in += MAS_in[0]

	T20_t2_mem0 = S.Task('T20_t2_mem0', length=1, delay_cost=1)
	S += T20_t2_mem0 >= 89
	T20_t2_mem0 += MAS_MEM[0]

	T20_t2_mem1 = S.Task('T20_t2_mem1', length=1, delay_cost=1)
	S += T20_t2_mem1 >= 89
	T20_t2_mem1 += MAS_MEM[1]

	T211 = S.Task('T211', length=3, delay_cost=1)
	S += T211 >= 89
	T211 += MAS[0]

	T17_t3_in = S.Task('T17_t3_in', length=1, delay_cost=1)
	S += T17_t3_in >= 90
	T17_t3_in += MAS_in[0]

	T17_t3_mem0 = S.Task('T17_t3_mem0', length=1, delay_cost=1)
	S += T17_t3_mem0 >= 90
	T17_t3_mem0 += MAS_MEM[0]

	T17_t3_mem1 = S.Task('T17_t3_mem1', length=1, delay_cost=1)
	S += T17_t3_mem1 >= 90
	T17_t3_mem1 += MAS_MEM[1]

	T20_t2 = S.Task('T20_t2', length=3, delay_cost=1)
	S += T20_t2 >= 90
	T20_t2 += MAS[0]

	T17_t3 = S.Task('T17_t3', length=3, delay_cost=1)
	S += T17_t3 >= 91
	T17_t3 += MAS[0]


	# new tasks
	T16_t4 = S.Task('T16_t4', length=11, delay_cost=1)
	T16_t4 += alt(MM)
	T16_t4_in = S.Task('T16_t4_in', length=1, delay_cost=1)
	T16_t4_in += alt(MM_in)
	S += T16_t4_in*MM_in[0]<=T16_t4*MM[0]
	T16_t4_mem0 = S.Task('T16_t4_mem0', length=1, delay_cost=1)
	T16_t4_mem0 += MAS_MEM[0]
	S += 56 < T16_t4_mem0
	S += T16_t4_mem0 <= T16_t4

	T16_t4_mem1 = S.Task('T16_t4_mem1', length=1, delay_cost=1)
	T16_t4_mem1 += MAS_MEM[1]
	S += 78 < T16_t4_mem1
	S += T16_t4_mem1 <= T16_t4

	T160 = S.Task('T160', length=3, delay_cost=1)
	T160 += alt(MAS)
	T160_in = S.Task('T160_in', length=1, delay_cost=1)
	T160_in += alt(MAS_in)
	S += T160_in*MAS_in[0]<=T160*MAS[0]

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	T160_mem0 += MM_MEM[0]
	S += 74 < T160_mem0
	S += T160_mem0 <= T160

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	T160_mem1 += MM_MEM[1]
	S += 90 < T160_mem1
	S += T160_mem1 <= T160

	T16_t5 = S.Task('T16_t5', length=3, delay_cost=1)
	T16_t5 += alt(MAS)
	T16_t5_in = S.Task('T16_t5_in', length=1, delay_cost=1)
	T16_t5_in += alt(MAS_in)
	S += T16_t5_in*MAS_in[0]<=T16_t5*MAS[0]

	T16_t5_mem0 = S.Task('T16_t5_mem0', length=1, delay_cost=1)
	T16_t5_mem0 += MM_MEM[0]
	S += 74 < T16_t5_mem0
	S += T16_t5_mem0 <= T16_t5

	T16_t5_mem1 = S.Task('T16_t5_mem1', length=1, delay_cost=1)
	T16_t5_mem1 += MM_MEM[1]
	S += 90 < T16_t5_mem1
	S += T16_t5_mem1 <= T16_t5

	T17_t4 = S.Task('T17_t4', length=11, delay_cost=1)
	T17_t4 += alt(MM)
	T17_t4_in = S.Task('T17_t4_in', length=1, delay_cost=1)
	T17_t4_in += alt(MM_in)
	S += T17_t4_in*MM_in[0]<=T17_t4*MM[0]
	T17_t4_mem0 = S.Task('T17_t4_mem0', length=1, delay_cost=1)
	T17_t4_mem0 += MAS_MEM[0]
	S += 80 < T17_t4_mem0
	S += T17_t4_mem0 <= T17_t4

	T17_t4_mem1 = S.Task('T17_t4_mem1', length=1, delay_cost=1)
	T17_t4_mem1 += MAS_MEM[1]
	S += 93 < T17_t4_mem1
	S += T17_t4_mem1 <= T17_t4

	T170 = S.Task('T170', length=3, delay_cost=1)
	T170 += alt(MAS)
	T170_in = S.Task('T170_in', length=1, delay_cost=1)
	T170_in += alt(MAS_in)
	S += T170_in*MAS_in[0]<=T170*MAS[0]

	T170_mem0 = S.Task('T170_mem0', length=1, delay_cost=1)
	T170_mem0 += MM_MEM[0]
	S += 76 < T170_mem0
	S += T170_mem0 <= T170

	T170_mem1 = S.Task('T170_mem1', length=1, delay_cost=1)
	T170_mem1 += MM_MEM[1]
	S += 84 < T170_mem1
	S += T170_mem1 <= T170

	T17_t5 = S.Task('T17_t5', length=3, delay_cost=1)
	T17_t5 += alt(MAS)
	T17_t5_in = S.Task('T17_t5_in', length=1, delay_cost=1)
	T17_t5_in += alt(MAS_in)
	S += T17_t5_in*MAS_in[0]<=T17_t5*MAS[0]

	T17_t5_mem0 = S.Task('T17_t5_mem0', length=1, delay_cost=1)
	T17_t5_mem0 += MM_MEM[0]
	S += 76 < T17_t5_mem0
	S += T17_t5_mem0 <= T17_t5

	T17_t5_mem1 = S.Task('T17_t5_mem1', length=1, delay_cost=1)
	T17_t5_mem1 += MM_MEM[1]
	S += 84 < T17_t5_mem1
	S += T17_t5_mem1 <= T17_t5

	T20_t1 = S.Task('T20_t1', length=11, delay_cost=1)
	T20_t1 += alt(MM)
	T20_t1_in = S.Task('T20_t1_in', length=1, delay_cost=1)
	T20_t1_in += alt(MM_in)
	S += T20_t1_in*MM_in[0]<=T20_t1*MM[0]
	T20_t1_mem0 = S.Task('T20_t1_mem0', length=1, delay_cost=1)
	T20_t1_mem0 += MAS_MEM[0]
	S += 55 < T20_t1_mem0
	S += T20_t1_mem0 <= T20_t1

	T20_t1_mem1 = S.Task('T20_t1_mem1', length=1, delay_cost=1)
	T20_t1_mem1 += MAS_MEM[1]
	S += 90 < T20_t1_mem1
	S += T20_t1_mem1 <= T20_t1

	T20_t3 = S.Task('T20_t3', length=3, delay_cost=1)
	T20_t3 += alt(MAS)
	T20_t3_in = S.Task('T20_t3_in', length=1, delay_cost=1)
	T20_t3_in += alt(MAS_in)
	S += T20_t3_in*MAS_in[0]<=T20_t3*MAS[0]

	T20_t3_mem0 = S.Task('T20_t3_mem0', length=1, delay_cost=1)
	T20_t3_mem0 += MAS_MEM[0]
	S += 69 < T20_t3_mem0
	S += T20_t3_mem0 <= T20_t3

	T20_t3_mem1 = S.Task('T20_t3_mem1', length=1, delay_cost=1)
	T20_t3_mem1 += MAS_MEM[1]
	S += 90 < T20_t3_mem1
	S += T20_t3_mem1 <= T20_t3

	T22_t0 = S.Task('T22_t0', length=3, delay_cost=1)
	T22_t0 += alt(MAS)
	T22_t0_in = S.Task('T22_t0_in', length=1, delay_cost=1)
	T22_t0_in += alt(MAS_in)
	S += T22_t0_in*MAS_in[0]<=T22_t0*MAS[0]

	T22_t0_mem0 = S.Task('T22_t0_mem0', length=1, delay_cost=1)
	T22_t0_mem0 += MAS_MEM[0]
	S += 88 < T22_t0_mem0
	S += T22_t0_mem0 <= T22_t0

	T22_t0_mem1 = S.Task('T22_t0_mem1', length=1, delay_cost=1)
	T22_t0_mem1 += MAS_MEM[1]
	S += 91 < T22_t0_mem1
	S += T22_t0_mem1 <= T22_t0

	T22_t1 = S.Task('T22_t1', length=3, delay_cost=1)
	T22_t1 += alt(MAS)
	T22_t1_in = S.Task('T22_t1_in', length=1, delay_cost=1)
	T22_t1_in += alt(MAS_in)
	S += T22_t1_in*MAS_in[0]<=T22_t1*MAS[0]

	T22_t1_mem0 = S.Task('T22_t1_mem0', length=1, delay_cost=1)
	T22_t1_mem0 += MAS_MEM[0]
	S += 88 < T22_t1_mem0
	S += T22_t1_mem0 <= T22_t1

	T22_t1_mem1 = S.Task('T22_t1_mem1', length=1, delay_cost=1)
	T22_t1_mem1 += MAS_MEM[1]
	S += 91 < T22_t1_mem1
	S += T22_t1_mem1 <= T22_t1

	T22_t3 = S.Task('T22_t3', length=11, delay_cost=1)
	T22_t3 += alt(MM)
	T22_t3_in = S.Task('T22_t3_in', length=1, delay_cost=1)
	T22_t3_in += alt(MM_in)
	S += T22_t3_in*MM_in[0]<=T22_t3*MM[0]
	T22_t3_mem0 = S.Task('T22_t3_mem0', length=1, delay_cost=1)
	T22_t3_mem0 += MAS_MEM[0]
	S += 88 < T22_t3_mem0
	S += T22_t3_mem0 <= T22_t3

	T22_t3_mem1 = S.Task('T22_t3_mem1', length=1, delay_cost=1)
	T22_t3_mem1 += MAS_MEM[1]
	S += 91 < T22_t3_mem1
	S += T22_t3_mem1 <= T22_t3

	T23_t0 = S.Task('T23_t0', length=3, delay_cost=1)
	T23_t0 += alt(MAS)
	T23_t0_in = S.Task('T23_t0_in', length=1, delay_cost=1)
	T23_t0_in += alt(MAS_in)
	S += T23_t0_in*MAS_in[0]<=T23_t0*MAS[0]

	T23_t0_mem0 = S.Task('T23_t0_mem0', length=1, delay_cost=1)
	T23_t0_mem0 += MAS_MEM[0]
	S += 79 < T23_t0_mem0
	S += T23_t0_mem0 <= T23_t0

	T23_t0_mem1 = S.Task('T23_t0_mem1', length=1, delay_cost=1)
	T23_t0_mem1 += MAS_MEM[1]
	S += 85 < T23_t0_mem1
	S += T23_t0_mem1 <= T23_t0

	T23_t1 = S.Task('T23_t1', length=3, delay_cost=1)
	T23_t1 += alt(MAS)
	T23_t1_in = S.Task('T23_t1_in', length=1, delay_cost=1)
	T23_t1_in += alt(MAS_in)
	S += T23_t1_in*MAS_in[0]<=T23_t1*MAS[0]

	T23_t1_mem0 = S.Task('T23_t1_mem0', length=1, delay_cost=1)
	T23_t1_mem0 += MAS_MEM[0]
	S += 79 < T23_t1_mem0
	S += T23_t1_mem0 <= T23_t1

	T23_t1_mem1 = S.Task('T23_t1_mem1', length=1, delay_cost=1)
	T23_t1_mem1 += MAS_MEM[1]
	S += 85 < T23_t1_mem1
	S += T23_t1_mem1 <= T23_t1

	T23_t3 = S.Task('T23_t3', length=11, delay_cost=1)
	T23_t3 += alt(MM)
	T23_t3_in = S.Task('T23_t3_in', length=1, delay_cost=1)
	T23_t3_in += alt(MM_in)
	S += T23_t3_in*MM_in[0]<=T23_t3*MM[0]
	T23_t3_mem0 = S.Task('T23_t3_mem0', length=1, delay_cost=1)
	T23_t3_mem0 += MAS_MEM[0]
	S += 79 < T23_t3_mem0
	S += T23_t3_mem0 <= T23_t3

	T23_t3_mem1 = S.Task('T23_t3_mem1', length=1, delay_cost=1)
	T23_t3_mem1 += MAS_MEM[1]
	S += 85 < T23_t3_mem1
	S += T23_t3_mem1 <= T23_t3

	T24_t4 = S.Task('T24_t4', length=11, delay_cost=1)
	T24_t4 += alt(MM)
	T24_t4_in = S.Task('T24_t4_in', length=1, delay_cost=1)
	T24_t4_in += alt(MM_in)
	S += T24_t4_in*MM_in[0]<=T24_t4*MM[0]
	T24_t4_mem0 = S.Task('T24_t4_mem0', length=1, delay_cost=1)
	T24_t4_mem0 += MAS_MEM[0]
	S += 84 < T24_t4_mem0
	S += T24_t4_mem0 <= T24_t4

	T24_t4_mem1 = S.Task('T24_t4_mem1', length=1, delay_cost=1)
	T24_t4_mem1 += MAS_MEM[1]
	S += 87 < T24_t4_mem1
	S += T24_t4_mem1 <= T24_t4

	T240 = S.Task('T240', length=3, delay_cost=1)
	T240 += alt(MAS)
	T240_in = S.Task('T240_in', length=1, delay_cost=1)
	T240_in += alt(MAS_in)
	S += T240_in*MAS_in[0]<=T240*MAS[0]

	T240_mem0 = S.Task('T240_mem0', length=1, delay_cost=1)
	T240_mem0 += MM_MEM[0]
	S += 75 < T240_mem0
	S += T240_mem0 <= T240

	T240_mem1 = S.Task('T240_mem1', length=1, delay_cost=1)
	T240_mem1 += MM_MEM[1]
	S += 94 < T240_mem1
	S += T240_mem1 <= T240

	T24_t5 = S.Task('T24_t5', length=3, delay_cost=1)
	T24_t5 += alt(MAS)
	T24_t5_in = S.Task('T24_t5_in', length=1, delay_cost=1)
	T24_t5_in += alt(MAS_in)
	S += T24_t5_in*MAS_in[0]<=T24_t5*MAS[0]

	T24_t5_mem0 = S.Task('T24_t5_mem0', length=1, delay_cost=1)
	T24_t5_mem0 += MM_MEM[0]
	S += 75 < T24_t5_mem0
	S += T24_t5_mem0 <= T24_t5

	T24_t5_mem1 = S.Task('T24_t5_mem1', length=1, delay_cost=1)
	T24_t5_mem1 += MM_MEM[1]
	S += 94 < T24_t5_mem1
	S += T24_t5_mem1 <= T24_t5

	Z3_t1 = S.Task('Z3_t1', length=11, delay_cost=1)
	Z3_t1 += alt(MM)
	Z3_t1_in = S.Task('Z3_t1_in', length=1, delay_cost=1)
	Z3_t1_in += alt(MM_in)
	S += Z3_t1_in*MM_in[0]<=Z3_t1*MM[0]
	Z3_t1_mem0 = S.Task('Z3_t1_mem0', length=1, delay_cost=1)
	Z3_t1_mem0 += MAIN_MEM_r[0]
	S += Z3_t1_mem0 <= Z3_t1

	Z3_t1_mem1 = S.Task('Z3_t1_mem1', length=1, delay_cost=1)
	Z3_t1_mem1 += MAS_MEM[1]
	S += 89 < Z3_t1_mem1
	S += Z3_t1_mem1 <= Z3_t1

	Z3_t3 = S.Task('Z3_t3', length=3, delay_cost=1)
	Z3_t3 += alt(MAS)
	Z3_t3_in = S.Task('Z3_t3_in', length=1, delay_cost=1)
	Z3_t3_in += alt(MAS_in)
	S += Z3_t3_in*MAS_in[0]<=Z3_t3*MAS[0]

	Z3_t3_mem0 = S.Task('Z3_t3_mem0', length=1, delay_cost=1)
	Z3_t3_mem0 += MAS_MEM[0]
	S += 72 < Z3_t3_mem0
	S += Z3_t3_mem0 <= Z3_t3

	Z3_t3_mem1 = S.Task('Z3_t3_mem1', length=1, delay_cost=1)
	Z3_t3_mem1 += MAS_MEM[1]
	S += 89 < Z3_t3_mem1
	S += Z3_t3_mem1 <= Z3_t3

	T161 = S.Task('T161', length=3, delay_cost=1)
	T161 += alt(MAS)
	T161_in = S.Task('T161_in', length=1, delay_cost=1)
	T161_in += alt(MAS_in)
	S += T161_in*MAS_in[0]<=T161*MAS[0]

	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	T161_mem0 += alt(MM_MEM)
	S += (T16_t4*MM[0])-1 < T161_mem0*MM_MEM[0]
	S += T161_mem0 <= T161

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	T161_mem1 += alt(MAS_MEM)
	S += (T16_t5*MAS[0])-1 < T161_mem1*MAS_MEM[1]
	S += T161_mem1 <= T161

	T171 = S.Task('T171', length=3, delay_cost=1)
	T171 += alt(MAS)
	T171_in = S.Task('T171_in', length=1, delay_cost=1)
	T171_in += alt(MAS_in)
	S += T171_in*MAS_in[0]<=T171*MAS[0]

	T171_mem0 = S.Task('T171_mem0', length=1, delay_cost=1)
	T171_mem0 += alt(MM_MEM)
	S += (T17_t4*MM[0])-1 < T171_mem0*MM_MEM[0]
	S += T171_mem0 <= T171

	T171_mem1 = S.Task('T171_mem1', length=1, delay_cost=1)
	T171_mem1 += alt(MAS_MEM)
	S += (T17_t5*MAS[0])-1 < T171_mem1*MAS_MEM[1]
	S += T171_mem1 <= T171

	T20_t4 = S.Task('T20_t4', length=11, delay_cost=1)
	T20_t4 += alt(MM)
	T20_t4_in = S.Task('T20_t4_in', length=1, delay_cost=1)
	T20_t4_in += alt(MM_in)
	S += T20_t4_in*MM_in[0]<=T20_t4*MM[0]
	T20_t4_mem0 = S.Task('T20_t4_mem0', length=1, delay_cost=1)
	T20_t4_mem0 += MAS_MEM[0]
	S += 92 < T20_t4_mem0
	S += T20_t4_mem0 <= T20_t4

	T20_t4_mem1 = S.Task('T20_t4_mem1', length=1, delay_cost=1)
	T20_t4_mem1 += alt(MAS_MEM)
	S += (T20_t3*MAS[0])-1 < T20_t4_mem1*MAS_MEM[1]
	S += T20_t4_mem1 <= T20_t4

	T200 = S.Task('T200', length=3, delay_cost=1)
	T200 += alt(MAS)
	T200_in = S.Task('T200_in', length=1, delay_cost=1)
	T200_in += alt(MAS_in)
	S += T200_in*MAS_in[0]<=T200*MAS[0]

	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	T200_mem0 += MM_MEM[0]
	S += 80 < T200_mem0
	S += T200_mem0 <= T200

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	T200_mem1 += alt(MM_MEM)
	S += (T20_t1*MM[0])-1 < T200_mem1*MM_MEM[1]
	S += T200_mem1 <= T200

	T20_t5 = S.Task('T20_t5', length=3, delay_cost=1)
	T20_t5 += alt(MAS)
	T20_t5_in = S.Task('T20_t5_in', length=1, delay_cost=1)
	T20_t5_in += alt(MAS_in)
	S += T20_t5_in*MAS_in[0]<=T20_t5*MAS[0]

	T20_t5_mem0 = S.Task('T20_t5_mem0', length=1, delay_cost=1)
	T20_t5_mem0 += MM_MEM[0]
	S += 80 < T20_t5_mem0
	S += T20_t5_mem0 <= T20_t5

	T20_t5_mem1 = S.Task('T20_t5_mem1', length=1, delay_cost=1)
	T20_t5_mem1 += alt(MM_MEM)
	S += (T20_t1*MM[0])-1 < T20_t5_mem1*MM_MEM[1]
	S += T20_t5_mem1 <= T20_t5

	T22_t2 = S.Task('T22_t2', length=11, delay_cost=1)
	T22_t2 += alt(MM)
	T22_t2_in = S.Task('T22_t2_in', length=1, delay_cost=1)
	T22_t2_in += alt(MM_in)
	S += T22_t2_in*MM_in[0]<=T22_t2*MM[0]
	T22_t2_mem0 = S.Task('T22_t2_mem0', length=1, delay_cost=1)
	T22_t2_mem0 += alt(MAS_MEM)
	S += (T22_t0*MAS[0])-1 < T22_t2_mem0*MAS_MEM[0]
	S += T22_t2_mem0 <= T22_t2

	T22_t2_mem1 = S.Task('T22_t2_mem1', length=1, delay_cost=1)
	T22_t2_mem1 += alt(MAS_MEM)
	S += (T22_t1*MAS[0])-1 < T22_t2_mem1*MAS_MEM[1]
	S += T22_t2_mem1 <= T22_t2

	T22_t5 = S.Task('T22_t5', length=3, delay_cost=1)
	T22_t5 += alt(MAS)
	T22_t5_in = S.Task('T22_t5_in', length=1, delay_cost=1)
	T22_t5_in += alt(MAS_in)
	S += T22_t5_in*MAS_in[0]<=T22_t5*MAS[0]

	T22_t5_mem0 = S.Task('T22_t5_mem0', length=1, delay_cost=1)
	T22_t5_mem0 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T22_t5_mem0*MM_MEM[0]
	S += T22_t5_mem0 <= T22_t5

	T22_t5_mem1 = S.Task('T22_t5_mem1', length=1, delay_cost=1)
	T22_t5_mem1 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T22_t5_mem1*MM_MEM[1]
	S += T22_t5_mem1 <= T22_t5

	T221 = S.Task('T221', length=3, delay_cost=1)
	T221 += alt(MAS)
	T221_in = S.Task('T221_in', length=1, delay_cost=1)
	T221_in += alt(MAS_in)
	S += T221_in*MAS_in[0]<=T221*MAS[0]

	T221_mem0 = S.Task('T221_mem0', length=1, delay_cost=1)
	T221_mem0 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T221_mem0*MM_MEM[0]
	S += T221_mem0 <= T221

	T221_mem1 = S.Task('T221_mem1', length=1, delay_cost=1)
	T221_mem1 += alt(MM_MEM)
	S += (T22_t3*MM[0])-1 < T221_mem1*MM_MEM[1]
	S += T221_mem1 <= T221

	T23_t2 = S.Task('T23_t2', length=11, delay_cost=1)
	T23_t2 += alt(MM)
	T23_t2_in = S.Task('T23_t2_in', length=1, delay_cost=1)
	T23_t2_in += alt(MM_in)
	S += T23_t2_in*MM_in[0]<=T23_t2*MM[0]
	T23_t2_mem0 = S.Task('T23_t2_mem0', length=1, delay_cost=1)
	T23_t2_mem0 += alt(MAS_MEM)
	S += (T23_t0*MAS[0])-1 < T23_t2_mem0*MAS_MEM[0]
	S += T23_t2_mem0 <= T23_t2

	T23_t2_mem1 = S.Task('T23_t2_mem1', length=1, delay_cost=1)
	T23_t2_mem1 += alt(MAS_MEM)
	S += (T23_t1*MAS[0])-1 < T23_t2_mem1*MAS_MEM[1]
	S += T23_t2_mem1 <= T23_t2

	T23_t5 = S.Task('T23_t5', length=3, delay_cost=1)
	T23_t5 += alt(MAS)
	T23_t5_in = S.Task('T23_t5_in', length=1, delay_cost=1)
	T23_t5_in += alt(MAS_in)
	S += T23_t5_in*MAS_in[0]<=T23_t5*MAS[0]

	T23_t5_mem0 = S.Task('T23_t5_mem0', length=1, delay_cost=1)
	T23_t5_mem0 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T23_t5_mem0*MM_MEM[0]
	S += T23_t5_mem0 <= T23_t5

	T23_t5_mem1 = S.Task('T23_t5_mem1', length=1, delay_cost=1)
	T23_t5_mem1 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T23_t5_mem1*MM_MEM[1]
	S += T23_t5_mem1 <= T23_t5

	T231 = S.Task('T231', length=3, delay_cost=1)
	T231 += alt(MAS)
	T231_in = S.Task('T231_in', length=1, delay_cost=1)
	T231_in += alt(MAS_in)
	S += T231_in*MAS_in[0]<=T231*MAS[0]

	T231_mem0 = S.Task('T231_mem0', length=1, delay_cost=1)
	T231_mem0 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T231_mem0*MM_MEM[0]
	S += T231_mem0 <= T231

	T231_mem1 = S.Task('T231_mem1', length=1, delay_cost=1)
	T231_mem1 += alt(MM_MEM)
	S += (T23_t3*MM[0])-1 < T231_mem1*MM_MEM[1]
	S += T231_mem1 <= T231

	T241 = S.Task('T241', length=3, delay_cost=1)
	T241 += alt(MAS)
	T241_in = S.Task('T241_in', length=1, delay_cost=1)
	T241_in += alt(MAS_in)
	S += T241_in*MAS_in[0]<=T241*MAS[0]

	T241_mem0 = S.Task('T241_mem0', length=1, delay_cost=1)
	T241_mem0 += alt(MM_MEM)
	S += (T24_t4*MM[0])-1 < T241_mem0*MM_MEM[0]
	S += T241_mem0 <= T241

	T241_mem1 = S.Task('T241_mem1', length=1, delay_cost=1)
	T241_mem1 += alt(MAS_MEM)
	S += (T24_t5*MAS[0])-1 < T241_mem1*MAS_MEM[1]
	S += T241_mem1 <= T241

	Z3_t4 = S.Task('Z3_t4', length=11, delay_cost=1)
	Z3_t4 += alt(MM)
	Z3_t4_in = S.Task('Z3_t4_in', length=1, delay_cost=1)
	Z3_t4_in += alt(MM_in)
	S += Z3_t4_in*MM_in[0]<=Z3_t4*MM[0]
	Z3_t4_mem0 = S.Task('Z3_t4_mem0', length=1, delay_cost=1)
	Z3_t4_mem0 += MAS_MEM[0]
	S += 61 < Z3_t4_mem0
	S += Z3_t4_mem0 <= Z3_t4

	Z3_t4_mem1 = S.Task('Z3_t4_mem1', length=1, delay_cost=1)
	Z3_t4_mem1 += alt(MAS_MEM)
	S += (Z3_t3*MAS[0])-1 < Z3_t4_mem1*MAS_MEM[1]
	S += Z3_t4_mem1 <= Z3_t4

	Z20_new = S.Task('Z20_new', length=3, delay_cost=1)
	Z20_new += alt(MAS)
	Z20_new_in = S.Task('Z20_new_in', length=1, delay_cost=1)
	Z20_new_in += alt(MAS_in)
	S += Z20_new_in*MAS_in[0]<=Z20_new*MAS[0]

	S += 0<Z20_new

	Z20_new_w = S.Task('Z20_new_w', length=1, delay_cost=1)
	Z20_new_w += alt(MAIN_MEM_w)
	S += Z20_new <= Z20_new_w

	Z20_new_mem0 = S.Task('Z20_new_mem0', length=1, delay_cost=1)
	Z20_new_mem0 += MM_MEM[0]
	S += 83 < Z20_new_mem0
	S += Z20_new_mem0 <= Z20_new

	Z20_new_mem1 = S.Task('Z20_new_mem1', length=1, delay_cost=1)
	Z20_new_mem1 += alt(MM_MEM)
	S += (Z3_t1*MM[0])-1 < Z20_new_mem1*MM_MEM[1]
	S += Z20_new_mem1 <= Z20_new

	Z3_t5 = S.Task('Z3_t5', length=3, delay_cost=1)
	Z3_t5 += alt(MAS)
	Z3_t5_in = S.Task('Z3_t5_in', length=1, delay_cost=1)
	Z3_t5_in += alt(MAS_in)
	S += Z3_t5_in*MAS_in[0]<=Z3_t5*MAS[0]

	Z3_t5_mem0 = S.Task('Z3_t5_mem0', length=1, delay_cost=1)
	Z3_t5_mem0 += MM_MEM[0]
	S += 83 < Z3_t5_mem0
	S += Z3_t5_mem0 <= Z3_t5

	Z3_t5_mem1 = S.Task('Z3_t5_mem1', length=1, delay_cost=1)
	Z3_t5_mem1 += alt(MM_MEM)
	S += (Z3_t1*MM[0])-1 < Z3_t5_mem1*MM_MEM[1]
	S += Z3_t5_mem1 <= Z3_t5

	T201 = S.Task('T201', length=3, delay_cost=1)
	T201 += alt(MAS)
	T201_in = S.Task('T201_in', length=1, delay_cost=1)
	T201_in += alt(MAS_in)
	S += T201_in*MAS_in[0]<=T201*MAS[0]

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	T201_mem0 += alt(MM_MEM)
	S += (T20_t4*MM[0])-1 < T201_mem0*MM_MEM[0]
	S += T201_mem0 <= T201

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	T201_mem1 += alt(MAS_MEM)
	S += (T20_t5*MAS[0])-1 < T201_mem1*MAS_MEM[1]
	S += T201_mem1 <= T201

	T220 = S.Task('T220', length=3, delay_cost=1)
	T220 += alt(MAS)
	T220_in = S.Task('T220_in', length=1, delay_cost=1)
	T220_in += alt(MAS_in)
	S += T220_in*MAS_in[0]<=T220*MAS[0]

	T220_mem0 = S.Task('T220_mem0', length=1, delay_cost=1)
	T220_mem0 += alt(MM_MEM)
	S += (T22_t2*MM[0])-1 < T220_mem0*MM_MEM[0]
	S += T220_mem0 <= T220

	T220_mem1 = S.Task('T220_mem1', length=1, delay_cost=1)
	T220_mem1 += alt(MAS_MEM)
	S += (T22_t5*MAS[0])-1 < T220_mem1*MAS_MEM[1]
	S += T220_mem1 <= T220

	T230 = S.Task('T230', length=3, delay_cost=1)
	T230 += alt(MAS)
	T230_in = S.Task('T230_in', length=1, delay_cost=1)
	T230_in += alt(MAS_in)
	S += T230_in*MAS_in[0]<=T230*MAS[0]

	T230_mem0 = S.Task('T230_mem0', length=1, delay_cost=1)
	T230_mem0 += alt(MM_MEM)
	S += (T23_t2*MM[0])-1 < T230_mem0*MM_MEM[0]
	S += T230_mem0 <= T230

	T230_mem1 = S.Task('T230_mem1', length=1, delay_cost=1)
	T230_mem1 += alt(MAS_MEM)
	S += (T23_t5*MAS[0])-1 < T230_mem1*MAS_MEM[1]
	S += T230_mem1 <= T230

	T250 = S.Task('T250', length=3, delay_cost=1)
	T250 += alt(MAS)
	T250_in = S.Task('T250_in', length=1, delay_cost=1)
	T250_in += alt(MAS_in)
	S += T250_in*MAS_in[0]<=T250*MAS[0]

	T250_mem0 = S.Task('T250_mem0', length=1, delay_cost=1)
	T250_mem0 += alt(MAS_MEM)
	S += (T200*MAS[0])-1 < T250_mem0*MAS_MEM[0]
	S += T250_mem0 <= T250

	T250_mem1 = S.Task('T250_mem1', length=1, delay_cost=1)
	T250_mem1 += alt(MAS_MEM)
	S += (T200*MAS[0])-1 < T250_mem1*MAS_MEM[1]
	S += T250_mem1 <= T250

	Z21_new = S.Task('Z21_new', length=3, delay_cost=1)
	Z21_new += alt(MAS)
	Z21_new_in = S.Task('Z21_new_in', length=1, delay_cost=1)
	Z21_new_in += alt(MAS_in)
	S += Z21_new_in*MAS_in[0]<=Z21_new*MAS[0]

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
	S += Z21_new_mem1 <= Z21_new

	X21_new = S.Task('X21_new', length=3, delay_cost=1)
	X21_new += alt(MAS)
	X21_new_in = S.Task('X21_new_in', length=1, delay_cost=1)
	X21_new_in += alt(MAS_in)
	S += X21_new_in*MAS_in[0]<=X21_new*MAS[0]

	S += 0<X21_new

	X21_new_w = S.Task('X21_new_w', length=1, delay_cost=1)
	X21_new_w += alt(MAIN_MEM_w)
	S += X21_new <= X21_new_w

	X21_new_mem0 = S.Task('X21_new_mem0', length=1, delay_cost=1)
	X21_new_mem0 += alt(MAS_MEM)
	S += (T221*MAS[0])-1 < X21_new_mem0*MAS_MEM[0]
	S += X21_new_mem0 <= X21_new

	X21_new_mem1 = S.Task('X21_new_mem1', length=1, delay_cost=1)
	X21_new_mem1 += alt(MAS_MEM)
	S += (T241*MAS[0])-1 < X21_new_mem1*MAS_MEM[1]
	S += X21_new_mem1 <= X21_new

	X11_new = S.Task('X11_new', length=3, delay_cost=1)
	X11_new += alt(MAS)
	X11_new_in = S.Task('X11_new_in', length=1, delay_cost=1)
	X11_new_in += alt(MAS_in)
	S += X11_new_in*MAS_in[0]<=X11_new*MAS[0]

	S += 0<X11_new

	X11_new_w = S.Task('X11_new_w', length=1, delay_cost=1)
	X11_new_w += alt(MAIN_MEM_w)
	S += X11_new <= X11_new_w

	X11_new_mem0 = S.Task('X11_new_mem0', length=1, delay_cost=1)
	X11_new_mem0 += alt(MAS_MEM)
	S += (T231*MAS[0])-1 < X11_new_mem0*MAS_MEM[0]
	S += X11_new_mem0 <= X11_new

	X11_new_mem1 = S.Task('X11_new_mem1', length=1, delay_cost=1)
	X11_new_mem1 += alt(MAS_MEM)
	S += (T171*MAS[0])-1 < X11_new_mem1*MAS_MEM[1]
	S += X11_new_mem1 <= X11_new

	T251 = S.Task('T251', length=3, delay_cost=1)
	T251 += alt(MAS)
	T251_in = S.Task('T251_in', length=1, delay_cost=1)
	T251_in += alt(MAS_in)
	S += T251_in*MAS_in[0]<=T251*MAS[0]

	T251_mem0 = S.Task('T251_mem0', length=1, delay_cost=1)
	T251_mem0 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem0*MAS_MEM[0]
	S += T251_mem0 <= T251

	T251_mem1 = S.Task('T251_mem1', length=1, delay_cost=1)
	T251_mem1 += alt(MAS_MEM)
	S += (T201*MAS[0])-1 < T251_mem1*MAS_MEM[1]
	S += T251_mem1 <= T251

	X20_new = S.Task('X20_new', length=3, delay_cost=1)
	X20_new += alt(MAS)
	X20_new_in = S.Task('X20_new_in', length=1, delay_cost=1)
	X20_new_in += alt(MAS_in)
	S += X20_new_in*MAS_in[0]<=X20_new*MAS[0]

	S += 0<X20_new

	X20_new_w = S.Task('X20_new_w', length=1, delay_cost=1)
	X20_new_w += alt(MAIN_MEM_w)
	S += X20_new <= X20_new_w

	X20_new_mem0 = S.Task('X20_new_mem0', length=1, delay_cost=1)
	X20_new_mem0 += alt(MAS_MEM)
	S += (T220*MAS[0])-1 < X20_new_mem0*MAS_MEM[0]
	S += X20_new_mem0 <= X20_new

	X20_new_mem1 = S.Task('X20_new_mem1', length=1, delay_cost=1)
	X20_new_mem1 += alt(MAS_MEM)
	S += (T240*MAS[0])-1 < X20_new_mem1*MAS_MEM[1]
	S += X20_new_mem1 <= X20_new

	Z10_new = S.Task('Z10_new', length=3, delay_cost=1)
	Z10_new += alt(MAS)
	Z10_new_in = S.Task('Z10_new_in', length=1, delay_cost=1)
	Z10_new_in += alt(MAS_in)
	S += Z10_new_in*MAS_in[0]<=Z10_new*MAS[0]

	S += 0<Z10_new

	Z10_new_w = S.Task('Z10_new_w', length=1, delay_cost=1)
	Z10_new_w += alt(MAIN_MEM_w)
	S += Z10_new <= Z10_new_w

	Z10_new_mem0 = S.Task('Z10_new_mem0', length=1, delay_cost=1)
	Z10_new_mem0 += alt(MAS_MEM)
	S += (T160*MAS[0])-1 < Z10_new_mem0*MAS_MEM[0]
	S += Z10_new_mem0 <= Z10_new

	Z10_new_mem1 = S.Task('Z10_new_mem1', length=1, delay_cost=1)
	Z10_new_mem1 += alt(MAS_MEM)
	S += (T250*MAS[0])-1 < Z10_new_mem1*MAS_MEM[1]
	S += Z10_new_mem1 <= Z10_new

	X10_new = S.Task('X10_new', length=3, delay_cost=1)
	X10_new += alt(MAS)
	X10_new_in = S.Task('X10_new_in', length=1, delay_cost=1)
	X10_new_in += alt(MAS_in)
	S += X10_new_in*MAS_in[0]<=X10_new*MAS[0]

	S += 0<X10_new

	X10_new_w = S.Task('X10_new_w', length=1, delay_cost=1)
	X10_new_w += alt(MAIN_MEM_w)
	S += X10_new <= X10_new_w

	X10_new_mem0 = S.Task('X10_new_mem0', length=1, delay_cost=1)
	X10_new_mem0 += alt(MAS_MEM)
	S += (T230*MAS[0])-1 < X10_new_mem0*MAS_MEM[0]
	S += X10_new_mem0 <= X10_new

	X10_new_mem1 = S.Task('X10_new_mem1', length=1, delay_cost=1)
	X10_new_mem1 += alt(MAS_MEM)
	S += (T170*MAS[0])-1 < X10_new_mem1*MAS_MEM[1]
	S += X10_new_mem1 <= X10_new

	Z11_new = S.Task('Z11_new', length=3, delay_cost=1)
	Z11_new += alt(MAS)
	Z11_new_in = S.Task('Z11_new_in', length=1, delay_cost=1)
	Z11_new_in += alt(MAS_in)
	S += Z11_new_in*MAS_in[0]<=Z11_new*MAS[0]

	S += 0<Z11_new

	Z11_new_w = S.Task('Z11_new_w', length=1, delay_cost=1)
	Z11_new_w += alt(MAIN_MEM_w)
	S += Z11_new <= Z11_new_w

	Z11_new_mem0 = S.Task('Z11_new_mem0', length=1, delay_cost=1)
	Z11_new_mem0 += alt(MAS_MEM)
	S += (T161*MAS[0])-1 < Z11_new_mem0*MAS_MEM[0]
	S += Z11_new_mem0 <= Z11_new

	Z11_new_mem1 = S.Task('Z11_new_mem1', length=1, delay_cost=1)
	Z11_new_mem1 += alt(MAS_MEM)
	S += (T251*MAS[0])-1 < Z11_new_mem1*MAS_MEM[1]
	S += Z11_new_mem1 <= Z11_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS1/EP2_LADDERMUL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution

