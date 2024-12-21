from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 202
	S = Scenario("schedule4", horizon=horizon)

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
	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	S += T1_t3_in >= 0
	T1_t3_in += MM_in[0]

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	S += T1_t3_mem0 >= 0
	T1_t3_mem0 += MAIN_MEM_r[0]

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	S += T1_t3_mem1 >= 0
	T1_t3_mem1 += MAIN_MEM_r[1]

	T1_t3 = S.Task('T1_t3', length=4, delay_cost=1)
	S += T1_t3 >= 1
	T1_t3 += MM[0]

	T3_t2_in = S.Task('T3_t2_in', length=1, delay_cost=1)
	S += T3_t2_in >= 1
	T3_t2_in += MAS_in[3]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	S += T3_t2_mem0 >= 1
	T3_t2_mem0 += MAIN_MEM_r[0]

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	S += T3_t2_mem1 >= 1
	T3_t2_mem1 += MAIN_MEM_r[1]

	T3_t2 = S.Task('T3_t2', length=2, delay_cost=1)
	S += T3_t2 >= 2
	T3_t2 += MAS[3]

	T3_t3_in = S.Task('T3_t3_in', length=1, delay_cost=1)
	S += T3_t3_in >= 2
	T3_t3_in += MAS_in[2]

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	S += T3_t3_mem0 >= 2
	T3_t3_mem0 += MAIN_MEM_r[0]

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	S += T3_t3_mem1 >= 2
	T3_t3_mem1 += MAIN_MEM_r[1]

	T3_t3 = S.Task('T3_t3', length=2, delay_cost=1)
	S += T3_t3 >= 3
	T3_t3 += MAS[2]

	T5_t1_in = S.Task('T5_t1_in', length=1, delay_cost=1)
	S += T5_t1_in >= 3
	T5_t1_in += MAS_in[0]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	S += T5_t1_mem0 >= 3
	T5_t1_mem0 += MAIN_MEM_r[0]

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	S += T5_t1_mem1 >= 3
	T5_t1_mem1 += MAIN_MEM_r[1]

	T1_t5_in = S.Task('T1_t5_in', length=1, delay_cost=1)
	S += T1_t5_in >= 4
	T1_t5_in += MAS_in[1]

	T1_t5_mem0 = S.Task('T1_t5_mem0', length=1, delay_cost=1)
	S += T1_t5_mem0 >= 4
	T1_t5_mem0 += MM_MEM[0]

	T1_t5_mem1 = S.Task('T1_t5_mem1', length=1, delay_cost=1)
	S += T1_t5_mem1 >= 4
	T1_t5_mem1 += MM_MEM[1]

	T3_t4_in = S.Task('T3_t4_in', length=1, delay_cost=1)
	S += T3_t4_in >= 4
	T3_t4_in += MM_in[0]

	T3_t4_mem0 = S.Task('T3_t4_mem0', length=1, delay_cost=1)
	S += T3_t4_mem0 >= 4
	T3_t4_mem0 += MAS_MEM[6]

	T3_t4_mem1 = S.Task('T3_t4_mem1', length=1, delay_cost=1)
	S += T3_t4_mem1 >= 4
	T3_t4_mem1 += MAS_MEM[5]

	T5_t1 = S.Task('T5_t1', length=2, delay_cost=1)
	S += T5_t1 >= 4
	T5_t1 += MAS[0]

	T7_t3_in = S.Task('T7_t3_in', length=1, delay_cost=1)
	S += T7_t3_in >= 4
	T7_t3_in += MAS_in[0]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	S += T7_t3_mem0 >= 4
	T7_t3_mem0 += MAIN_MEM_r[0]

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	S += T7_t3_mem1 >= 4
	T7_t3_mem1 += MAIN_MEM_r[1]

	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	S += T11_in >= 5
	T11_in += MAS_in[2]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 5
	T11_mem0 += MM_MEM[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 5
	T11_mem1 += MM_MEM[1]

	T1_t5 = S.Task('T1_t5', length=2, delay_cost=1)
	S += T1_t5 >= 5
	T1_t5 += MAS[1]

	T2_t3_in = S.Task('T2_t3_in', length=1, delay_cost=1)
	S += T2_t3_in >= 5
	T2_t3_in += MAS_in[0]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	S += T2_t3_mem0 >= 5
	T2_t3_mem0 += MAIN_MEM_r[0]

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	S += T2_t3_mem1 >= 5
	T2_t3_mem1 += MAIN_MEM_r[1]

	T3_t4 = S.Task('T3_t4', length=4, delay_cost=1)
	S += T3_t4 >= 5
	T3_t4 += MM[0]

	T7_t3 = S.Task('T7_t3', length=2, delay_cost=1)
	S += T7_t3 >= 5
	T7_t3 += MAS[0]

	T11 = S.Task('T11', length=2, delay_cost=1)
	S += T11 >= 6
	T11 += MAS[2]

	T2_t3 = S.Task('T2_t3', length=2, delay_cost=1)
	S += T2_t3 >= 6
	T2_t3 += MAS[0]

	T9_t2_in = S.Task('T9_t2_in', length=1, delay_cost=1)
	S += T9_t2_in >= 6
	T9_t2_in += MAS_in[0]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	S += T9_t2_mem0 >= 6
	T9_t2_mem0 += MAIN_MEM_r[0]

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	S += T9_t2_mem1 >= 6
	T9_t2_mem1 += MAIN_MEM_r[1]

	T1_t0_in = S.Task('T1_t0_in', length=1, delay_cost=1)
	S += T1_t0_in >= 7
	T1_t0_in += MAS_in[2]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	S += T1_t0_mem0 >= 7
	T1_t0_mem0 += MAIN_MEM_r[0]

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	S += T1_t0_mem1 >= 7
	T1_t0_mem1 += MAIN_MEM_r[1]

	T9_t2 = S.Task('T9_t2', length=2, delay_cost=1)
	S += T9_t2 >= 7
	T9_t2 += MAS[0]

	T1_t0 = S.Task('T1_t0', length=2, delay_cost=1)
	S += T1_t0 >= 8
	T1_t0 += MAS[2]

	T1_t1_in = S.Task('T1_t1_in', length=1, delay_cost=1)
	S += T1_t1_in >= 8
	T1_t1_in += MAS_in[0]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	S += T1_t1_mem0 >= 8
	T1_t1_mem0 += MAIN_MEM_r[0]

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	S += T1_t1_mem1 >= 8
	T1_t1_mem1 += MAIN_MEM_r[1]

	T1_t1 = S.Task('T1_t1', length=2, delay_cost=1)
	S += T1_t1 >= 9
	T1_t1 += MAS[0]

	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	S += T2_t0_in >= 9
	T2_t0_in += MM_in[0]

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	S += T2_t0_mem0 >= 9
	T2_t0_mem0 += MAIN_MEM_r[0]

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	S += T2_t0_mem1 >= 9
	T2_t0_mem1 += MAIN_MEM_r[1]

	T1_t2_in = S.Task('T1_t2_in', length=1, delay_cost=1)
	S += T1_t2_in >= 10
	T1_t2_in += MM_in[0]

	T1_t2_mem0 = S.Task('T1_t2_mem0', length=1, delay_cost=1)
	S += T1_t2_mem0 >= 10
	T1_t2_mem0 += MAS_MEM[4]

	T1_t2_mem1 = S.Task('T1_t2_mem1', length=1, delay_cost=1)
	S += T1_t2_mem1 >= 10
	T1_t2_mem1 += MAS_MEM[1]

	T2_t0 = S.Task('T2_t0', length=4, delay_cost=1)
	S += T2_t0 >= 10
	T2_t0 += MM[0]

	T4_t2_in = S.Task('T4_t2_in', length=1, delay_cost=1)
	S += T4_t2_in >= 10
	T4_t2_in += MAS_in[3]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	S += T4_t2_mem0 >= 10
	T4_t2_mem0 += MAIN_MEM_r[0]

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	S += T4_t2_mem1 >= 10
	T4_t2_mem1 += MAIN_MEM_r[1]

	T1_t2 = S.Task('T1_t2', length=4, delay_cost=1)
	S += T1_t2 >= 11
	T1_t2 += MM[0]

	T4_t2 = S.Task('T4_t2', length=2, delay_cost=1)
	S += T4_t2 >= 11
	T4_t2 += MAS[3]

	T4_t3_in = S.Task('T4_t3_in', length=1, delay_cost=1)
	S += T4_t3_in >= 11
	T4_t3_in += MAS_in[3]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	S += T4_t3_mem0 >= 11
	T4_t3_mem0 += MAIN_MEM_r[0]

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	S += T4_t3_mem1 >= 11
	T4_t3_mem1 += MAIN_MEM_r[1]

	T4_t3 = S.Task('T4_t3', length=2, delay_cost=1)
	S += T4_t3 >= 12
	T4_t3 += MAS[3]

	T5_t0_in = S.Task('T5_t0_in', length=1, delay_cost=1)
	S += T5_t0_in >= 12
	T5_t0_in += MAS_in[2]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	S += T5_t0_mem0 >= 12
	T5_t0_mem0 += MAIN_MEM_r[0]

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	S += T5_t0_mem1 >= 12
	T5_t0_mem1 += MAIN_MEM_r[1]

	T10_t2_in = S.Task('T10_t2_in', length=1, delay_cost=1)
	S += T10_t2_in >= 13
	T10_t2_in += MAS_in[3]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	S += T10_t2_mem0 >= 13
	T10_t2_mem0 += MAIN_MEM_r[0]

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	S += T10_t2_mem1 >= 13
	T10_t2_mem1 += MAIN_MEM_r[1]

	T4_t4_in = S.Task('T4_t4_in', length=1, delay_cost=1)
	S += T4_t4_in >= 13
	T4_t4_in += MM_in[0]

	T4_t4_mem0 = S.Task('T4_t4_mem0', length=1, delay_cost=1)
	S += T4_t4_mem0 >= 13
	T4_t4_mem0 += MAS_MEM[6]

	T4_t4_mem1 = S.Task('T4_t4_mem1', length=1, delay_cost=1)
	S += T4_t4_mem1 >= 13
	T4_t4_mem1 += MAS_MEM[7]

	T5_t0 = S.Task('T5_t0', length=2, delay_cost=1)
	S += T5_t0 >= 13
	T5_t0 += MAS[2]

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	S += T10_in >= 14
	T10_in += MAS_in[1]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 14
	T10_mem0 += MM_MEM[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 14
	T10_mem1 += MAS_MEM[3]

	T10_t2 = S.Task('T10_t2', length=2, delay_cost=1)
	S += T10_t2 >= 14
	T10_t2 += MAS[3]

	T4_t4 = S.Task('T4_t4', length=4, delay_cost=1)
	S += T4_t4 >= 14
	T4_t4 += MM[0]

	T5_t2_in = S.Task('T5_t2_in', length=1, delay_cost=1)
	S += T5_t2_in >= 14
	T5_t2_in += MM_in[0]

	T5_t2_mem0 = S.Task('T5_t2_mem0', length=1, delay_cost=1)
	S += T5_t2_mem0 >= 14
	T5_t2_mem0 += MAS_MEM[4]

	T5_t2_mem1 = S.Task('T5_t2_mem1', length=1, delay_cost=1)
	S += T5_t2_mem1 >= 14
	T5_t2_mem1 += MAS_MEM[1]

	T7_t2_in = S.Task('T7_t2_in', length=1, delay_cost=1)
	S += T7_t2_in >= 14
	T7_t2_in += MAS_in[3]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	S += T7_t2_mem0 >= 14
	T7_t2_mem0 += MAIN_MEM_r[0]

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	S += T7_t2_mem1 >= 14
	T7_t2_mem1 += MAIN_MEM_r[1]

	T10 = S.Task('T10', length=2, delay_cost=1)
	S += T10 >= 15
	T10 += MAS[1]

	T11_t2_in = S.Task('T11_t2_in', length=1, delay_cost=1)
	S += T11_t2_in >= 15
	T11_t2_in += MAS_in[3]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	S += T11_t2_mem0 >= 15
	T11_t2_mem0 += MAIN_MEM_r[0]

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	S += T11_t2_mem1 >= 15
	T11_t2_mem1 += MAIN_MEM_r[1]

	T5_t2 = S.Task('T5_t2', length=4, delay_cost=1)
	S += T5_t2 >= 15
	T5_t2 += MM[0]

	T7_t2 = S.Task('T7_t2', length=2, delay_cost=1)
	S += T7_t2 >= 15
	T7_t2 += MAS[3]

	T11_t2 = S.Task('T11_t2', length=2, delay_cost=1)
	S += T11_t2 >= 16
	T11_t2 += MAS[3]

	T16_t2_in = S.Task('T16_t2_in', length=1, delay_cost=1)
	S += T16_t2_in >= 16
	T16_t2_in += MAS_in[1]

	T16_t2_mem0 = S.Task('T16_t2_mem0', length=1, delay_cost=1)
	S += T16_t2_mem0 >= 16
	T16_t2_mem0 += MAS_MEM[2]

	T16_t2_mem1 = S.Task('T16_t2_mem1', length=1, delay_cost=1)
	S += T16_t2_mem1 >= 16
	T16_t2_mem1 += MAS_MEM[5]

	T6_t2_in = S.Task('T6_t2_in', length=1, delay_cost=1)
	S += T6_t2_in >= 16
	T6_t2_in += MAS_in[2]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	S += T6_t2_mem0 >= 16
	T6_t2_mem0 += MAIN_MEM_r[0]

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	S += T6_t2_mem1 >= 16
	T6_t2_mem1 += MAIN_MEM_r[1]

	T7_t4_in = S.Task('T7_t4_in', length=1, delay_cost=1)
	S += T7_t4_in >= 16
	T7_t4_in += MM_in[0]

	T7_t4_mem0 = S.Task('T7_t4_mem0', length=1, delay_cost=1)
	S += T7_t4_mem0 >= 16
	T7_t4_mem0 += MAS_MEM[6]

	T7_t4_mem1 = S.Task('T7_t4_mem1', length=1, delay_cost=1)
	S += T7_t4_mem1 >= 16
	T7_t4_mem1 += MAS_MEM[1]

	T16_t2 = S.Task('T16_t2', length=2, delay_cost=1)
	S += T16_t2 >= 17
	T16_t2 += MAS[1]

	T6_t2 = S.Task('T6_t2', length=2, delay_cost=1)
	S += T6_t2 >= 17
	T6_t2 += MAS[2]

	T6_t3_in = S.Task('T6_t3_in', length=1, delay_cost=1)
	S += T6_t3_in >= 17
	T6_t3_in += MAS_in[2]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	S += T6_t3_mem0 >= 17
	T6_t3_mem0 += MAIN_MEM_r[0]

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	S += T6_t3_mem1 >= 17
	T6_t3_mem1 += MAIN_MEM_r[1]

	T7_t4 = S.Task('T7_t4', length=4, delay_cost=1)
	S += T7_t4 >= 17
	T7_t4 += MM[0]

	T9_t3_in = S.Task('T9_t3_in', length=1, delay_cost=1)
	S += T9_t3_in >= 17
	T9_t3_in += MAS_in[3]

	T9_t3_mem0 = S.Task('T9_t3_mem0', length=1, delay_cost=1)
	S += T9_t3_mem0 >= 17
	T9_t3_mem0 += MAS_MEM[2]

	T9_t3_mem1 = S.Task('T9_t3_mem1', length=1, delay_cost=1)
	S += T9_t3_mem1 >= 17
	T9_t3_mem1 += MAS_MEM[5]

	T2_t2_in = S.Task('T2_t2_in', length=1, delay_cost=1)
	S += T2_t2_in >= 18
	T2_t2_in += MAS_in[0]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	S += T2_t2_mem0 >= 18
	T2_t2_mem0 += MAIN_MEM_r[0]

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	S += T2_t2_mem1 >= 18
	T2_t2_mem1 += MAIN_MEM_r[1]

	T6_t3 = S.Task('T6_t3', length=2, delay_cost=1)
	S += T6_t3 >= 18
	T6_t3 += MAS[2]

	T8_t3_in = S.Task('T8_t3_in', length=1, delay_cost=1)
	S += T8_t3_in >= 18
	T8_t3_in += MAS_in[3]

	T8_t3_mem0 = S.Task('T8_t3_mem0', length=1, delay_cost=1)
	S += T8_t3_mem0 >= 18
	T8_t3_mem0 += MAS_MEM[2]

	T8_t3_mem1 = S.Task('T8_t3_mem1', length=1, delay_cost=1)
	S += T8_t3_mem1 >= 18
	T8_t3_mem1 += MAS_MEM[5]

	T9_t3 = S.Task('T9_t3', length=2, delay_cost=1)
	S += T9_t3 >= 18
	T9_t3 += MAS[3]

	T2_t2 = S.Task('T2_t2', length=2, delay_cost=1)
	S += T2_t2 >= 19
	T2_t2 += MAS[0]

	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	S += T6_t1_in >= 19
	T6_t1_in += MM_in[0]

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	S += T6_t1_mem0 >= 19
	T6_t1_mem0 += MAIN_MEM_r[0]

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	S += T6_t1_mem1 >= 19
	T6_t1_mem1 += MAIN_MEM_r[1]

	T8_t3 = S.Task('T8_t3', length=2, delay_cost=1)
	S += T8_t3 >= 19
	T8_t3 += MAS[3]

	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	S += T6_t0_in >= 20
	T6_t0_in += MM_in[0]

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	S += T6_t0_mem0 >= 20
	T6_t0_mem0 += MAIN_MEM_r[0]

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	S += T6_t0_mem1 >= 20
	T6_t0_mem1 += MAIN_MEM_r[1]

	T6_t1 = S.Task('T6_t1', length=4, delay_cost=1)
	S += T6_t1 >= 20
	T6_t1 += MM[0]

	T2_t4_in = S.Task('T2_t4_in', length=1, delay_cost=1)
	S += T2_t4_in >= 21
	T2_t4_in += MM_in[0]

	T2_t4_mem0 = S.Task('T2_t4_mem0', length=1, delay_cost=1)
	S += T2_t4_mem0 >= 21
	T2_t4_mem0 += MAS_MEM[0]

	T2_t4_mem1 = S.Task('T2_t4_mem1', length=1, delay_cost=1)
	S += T2_t4_mem1 >= 21
	T2_t4_mem1 += MAS_MEM[1]

	T6_t0 = S.Task('T6_t0', length=4, delay_cost=1)
	S += T6_t0 >= 21
	T6_t0 += MM[0]

	T8_t2_in = S.Task('T8_t2_in', length=1, delay_cost=1)
	S += T8_t2_in >= 21
	T8_t2_in += MAS_in[3]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	S += T8_t2_mem0 >= 21
	T8_t2_mem0 += MAIN_MEM_r[0]

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	S += T8_t2_mem1 >= 21
	T8_t2_mem1 += MAIN_MEM_r[1]

	T2_t4 = S.Task('T2_t4', length=4, delay_cost=1)
	S += T2_t4 >= 22
	T2_t4 += MM[0]

	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	S += T5_t3_in >= 22
	T5_t3_in += MM_in[0]

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	S += T5_t3_mem0 >= 22
	T5_t3_mem0 += MAIN_MEM_r[0]

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	S += T5_t3_mem1 >= 22
	T5_t3_mem1 += MAIN_MEM_r[1]

	T8_t2 = S.Task('T8_t2', length=2, delay_cost=1)
	S += T8_t2 >= 22
	T8_t2 += MAS[3]

	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	S += T4_t1_in >= 23
	T4_t1_in += MM_in[0]

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	S += T4_t1_mem0 >= 23
	T4_t1_mem0 += MAIN_MEM_r[0]

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	S += T4_t1_mem1 >= 23
	T4_t1_mem1 += MAIN_MEM_r[1]

	T5_t3 = S.Task('T5_t3', length=4, delay_cost=1)
	S += T5_t3 >= 23
	T5_t3 += MM[0]

	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	S += T4_t0_in >= 24
	T4_t0_in += MM_in[0]

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	S += T4_t0_mem0 >= 24
	T4_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	S += T4_t0_mem1 >= 24
	T4_t0_mem1 += MAIN_MEM_r[1]

	T4_t1 = S.Task('T4_t1', length=4, delay_cost=1)
	S += T4_t1 >= 24
	T4_t1 += MM[0]

	T6_t5_in = S.Task('T6_t5_in', length=1, delay_cost=1)
	S += T6_t5_in >= 24
	T6_t5_in += MAS_in[2]

	T6_t5_mem0 = S.Task('T6_t5_mem0', length=1, delay_cost=1)
	S += T6_t5_mem0 >= 24
	T6_t5_mem0 += MM_MEM[0]

	T6_t5_mem1 = S.Task('T6_t5_mem1', length=1, delay_cost=1)
	S += T6_t5_mem1 >= 24
	T6_t5_mem1 += MM_MEM[1]

	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	S += T3_t1_in >= 25
	T3_t1_in += MM_in[0]

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	S += T3_t1_mem0 >= 25
	T3_t1_mem0 += MAIN_MEM_r[0]

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	S += T3_t1_mem1 >= 25
	T3_t1_mem1 += MAIN_MEM_r[1]

	T4_t0 = S.Task('T4_t0', length=4, delay_cost=1)
	S += T4_t0 >= 25
	T4_t0 += MM[0]

	T60_in = S.Task('T60_in', length=1, delay_cost=1)
	S += T60_in >= 25
	T60_in += MAS_in[0]

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	S += T60_mem0 >= 25
	T60_mem0 += MM_MEM[0]

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	S += T60_mem1 >= 25
	T60_mem1 += MM_MEM[1]

	T6_t5 = S.Task('T6_t5', length=2, delay_cost=1)
	S += T6_t5 >= 25
	T6_t5 += MAS[2]

	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	S += T3_t0_in >= 26
	T3_t0_in += MM_in[0]

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	S += T3_t0_mem0 >= 26
	T3_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	S += T3_t0_mem1 >= 26
	T3_t0_mem1 += MAIN_MEM_r[1]

	T3_t1 = S.Task('T3_t1', length=4, delay_cost=1)
	S += T3_t1 >= 26
	T3_t1 += MM[0]

	T5_t5_in = S.Task('T5_t5_in', length=1, delay_cost=1)
	S += T5_t5_in >= 26
	T5_t5_in += MAS_in[0]

	T5_t5_mem0 = S.Task('T5_t5_mem0', length=1, delay_cost=1)
	S += T5_t5_mem0 >= 26
	T5_t5_mem0 += MM_MEM[0]

	T5_t5_mem1 = S.Task('T5_t5_mem1', length=1, delay_cost=1)
	S += T5_t5_mem1 >= 26
	T5_t5_mem1 += MM_MEM[1]

	T60 = S.Task('T60', length=2, delay_cost=1)
	S += T60 >= 26
	T60 += MAS[0]

	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	S += T2_t1_in >= 27
	T2_t1_in += MM_in[0]

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	S += T2_t1_mem0 >= 27
	T2_t1_mem0 += MAIN_MEM_r[0]

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	S += T2_t1_mem1 >= 27
	T2_t1_mem1 += MAIN_MEM_r[1]

	T3_t0 = S.Task('T3_t0', length=4, delay_cost=1)
	S += T3_t0 >= 27
	T3_t0 += MM[0]

	T51_in = S.Task('T51_in', length=1, delay_cost=1)
	S += T51_in >= 27
	T51_in += MAS_in[0]

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	S += T51_mem0 >= 27
	T51_mem0 += MM_MEM[0]

	T51_mem1 = S.Task('T51_mem1', length=1, delay_cost=1)
	S += T51_mem1 >= 27
	T51_mem1 += MM_MEM[1]

	T5_t5 = S.Task('T5_t5', length=2, delay_cost=1)
	S += T5_t5 >= 27
	T5_t5 += MAS[0]

	T2_t1 = S.Task('T2_t1', length=4, delay_cost=1)
	S += T2_t1 >= 28
	T2_t1 += MM[0]

	T50_in = S.Task('T50_in', length=1, delay_cost=1)
	S += T50_in >= 28
	T50_in += MAS_in[0]

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	S += T50_mem0 >= 28
	T50_mem0 += MM_MEM[0]

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	S += T50_mem1 >= 28
	T50_mem1 += MAS_MEM[1]

	T51 = S.Task('T51', length=2, delay_cost=1)
	S += T51 >= 28
	T51 += MAS[0]

	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	S += T7_t1_in >= 28
	T7_t1_in += MM_in[0]

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	S += T7_t1_mem0 >= 28
	T7_t1_mem0 += MAIN_MEM_r[0]

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	S += T7_t1_mem1 >= 28
	T7_t1_mem1 += MAIN_MEM_r[1]

	T40_in = S.Task('T40_in', length=1, delay_cost=1)
	S += T40_in >= 29
	T40_in += MAS_in[1]

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	S += T40_mem0 >= 29
	T40_mem0 += MM_MEM[0]

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	S += T40_mem1 >= 29
	T40_mem1 += MM_MEM[1]

	T50 = S.Task('T50', length=2, delay_cost=1)
	S += T50 >= 29
	T50 += MAS[0]

	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	S += T7_t0_in >= 29
	T7_t0_in += MM_in[0]

	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	S += T7_t0_mem0 >= 29
	T7_t0_mem0 += MAIN_MEM_r[0]

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	S += T7_t0_mem1 >= 29
	T7_t0_mem1 += MAIN_MEM_r[1]

	T7_t1 = S.Task('T7_t1', length=4, delay_cost=1)
	S += T7_t1 >= 29
	T7_t1 += MM[0]

	T20_t2_in = S.Task('T20_t2_in', length=1, delay_cost=1)
	S += T20_t2_in >= 30
	T20_t2_in += MAS_in[1]

	T20_t2_mem0 = S.Task('T20_t2_mem0', length=1, delay_cost=1)
	S += T20_t2_mem0 >= 30
	T20_t2_mem0 += MAS_MEM[0]

	T20_t2_mem1 = S.Task('T20_t2_mem1', length=1, delay_cost=1)
	S += T20_t2_mem1 >= 30
	T20_t2_mem1 += MAS_MEM[1]

	T3_t5_in = S.Task('T3_t5_in', length=1, delay_cost=1)
	S += T3_t5_in >= 30
	T3_t5_in += MAS_in[3]

	T3_t5_mem0 = S.Task('T3_t5_mem0', length=1, delay_cost=1)
	S += T3_t5_mem0 >= 30
	T3_t5_mem0 += MM_MEM[0]

	T3_t5_mem1 = S.Task('T3_t5_mem1', length=1, delay_cost=1)
	S += T3_t5_mem1 >= 30
	T3_t5_mem1 += MM_MEM[1]

	T40 = S.Task('T40', length=2, delay_cost=1)
	S += T40 >= 30
	T40 += MAS[1]

	T6_t4_in = S.Task('T6_t4_in', length=1, delay_cost=1)
	S += T6_t4_in >= 30
	T6_t4_in += MM_in[0]

	T6_t4_mem0 = S.Task('T6_t4_mem0', length=1, delay_cost=1)
	S += T6_t4_mem0 >= 30
	T6_t4_mem0 += MAS_MEM[4]

	T6_t4_mem1 = S.Task('T6_t4_mem1', length=1, delay_cost=1)
	S += T6_t4_mem1 >= 30
	T6_t4_mem1 += MAS_MEM[5]

	T7_t0 = S.Task('T7_t0', length=4, delay_cost=1)
	S += T7_t0 >= 30
	T7_t0 += MM[0]

	Z3_t2_in = S.Task('Z3_t2_in', length=1, delay_cost=1)
	S += Z3_t2_in >= 30
	Z3_t2_in += MAS_in[2]

	Z3_t2_mem0 = S.Task('Z3_t2_mem0', length=1, delay_cost=1)
	S += Z3_t2_mem0 >= 30
	Z3_t2_mem0 += MAIN_MEM_r[0]

	Z3_t2_mem1 = S.Task('Z3_t2_mem1', length=1, delay_cost=1)
	S += Z3_t2_mem1 >= 30
	Z3_t2_mem1 += MAIN_MEM_r[1]

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	S += T20_in >= 31
	T20_in += MAS_in[0]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 31
	T20_mem0 += MM_MEM[0]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 31
	T20_mem1 += MM_MEM[1]

	T20_t2 = S.Task('T20_t2', length=2, delay_cost=1)
	S += T20_t2 >= 31
	T20_t2 += MAS[1]

	T3_t5 = S.Task('T3_t5', length=2, delay_cost=1)
	S += T3_t5 >= 31
	T3_t5 += MAS[3]

	T6_t4 = S.Task('T6_t4', length=4, delay_cost=1)
	S += T6_t4 >= 31
	T6_t4 += MM[0]

	T9_t1_in = S.Task('T9_t1_in', length=1, delay_cost=1)
	S += T9_t1_in >= 31
	T9_t1_in += MM_in[0]

	T9_t1_mem0 = S.Task('T9_t1_mem0', length=1, delay_cost=1)
	S += T9_t1_mem0 >= 31
	T9_t1_mem0 += MAIN_MEM_r[0]

	T9_t1_mem1 = S.Task('T9_t1_mem1', length=1, delay_cost=1)
	S += T9_t1_mem1 >= 31
	T9_t1_mem1 += MAS_MEM[5]

	Z3_t2 = S.Task('Z3_t2', length=2, delay_cost=1)
	S += Z3_t2 >= 31
	Z3_t2 += MAS[2]

	T20 = S.Task('T20', length=2, delay_cost=1)
	S += T20 >= 32
	T20 += MAS[0]

	T30_in = S.Task('T30_in', length=1, delay_cost=1)
	S += T30_in >= 32
	T30_in += MAS_in[2]

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	S += T30_mem0 >= 32
	T30_mem0 += MM_MEM[0]

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	S += T30_mem1 >= 32
	T30_mem1 += MM_MEM[1]

	T8_t1_in = S.Task('T8_t1_in', length=1, delay_cost=1)
	S += T8_t1_in >= 32
	T8_t1_in += MM_in[0]

	T8_t1_mem0 = S.Task('T8_t1_mem0', length=1, delay_cost=1)
	S += T8_t1_mem0 >= 32
	T8_t1_mem0 += MAIN_MEM_r[0]

	T8_t1_mem1 = S.Task('T8_t1_mem1', length=1, delay_cost=1)
	S += T8_t1_mem1 >= 32
	T8_t1_mem1 += MAS_MEM[5]

	T9_t1 = S.Task('T9_t1', length=4, delay_cost=1)
	S += T9_t1 >= 32
	T9_t1 += MM[0]

	T120_in = S.Task('T120_in', length=1, delay_cost=1)
	S += T120_in >= 33
	T120_in += MAS_in[3]

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	S += T120_mem0 >= 33
	T120_mem0 += MAS_MEM[2]

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	S += T120_mem1 >= 33
	T120_mem1 += MAS_MEM[1]

	T30 = S.Task('T30', length=2, delay_cost=1)
	S += T30 >= 33
	T30 += MAS[2]

	T31_in = S.Task('T31_in', length=1, delay_cost=1)
	S += T31_in >= 33
	T31_in += MAS_in[0]

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	S += T31_mem0 >= 33
	T31_mem0 += MM_MEM[0]

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	S += T31_mem1 >= 33
	T31_mem1 += MAS_MEM[7]

	T8_t1 = S.Task('T8_t1', length=4, delay_cost=1)
	S += T8_t1 >= 33
	T8_t1 += MM[0]

	T9_t0_in = S.Task('T9_t0_in', length=1, delay_cost=1)
	S += T9_t0_in >= 33
	T9_t0_in += MM_in[0]

	T9_t0_mem0 = S.Task('T9_t0_mem0', length=1, delay_cost=1)
	S += T9_t0_mem0 >= 33
	T9_t0_mem0 += MAIN_MEM_r[0]

	T9_t0_mem1 = S.Task('T9_t0_mem1', length=1, delay_cost=1)
	S += T9_t0_mem1 >= 33
	T9_t0_mem1 += MAS_MEM[3]

	T11_t0_in = S.Task('T11_t0_in', length=1, delay_cost=1)
	S += T11_t0_in >= 34
	T11_t0_in += MM_in[0]

	T11_t0_mem0 = S.Task('T11_t0_mem0', length=1, delay_cost=1)
	S += T11_t0_mem0 >= 34
	T11_t0_mem0 += MAIN_MEM_r[0]

	T11_t0_mem1 = S.Task('T11_t0_mem1', length=1, delay_cost=1)
	S += T11_t0_mem1 >= 34
	T11_t0_mem1 += MAS_MEM[5]

	T120 = S.Task('T120', length=2, delay_cost=1)
	S += T120 >= 34
	T120 += MAS[3]

	T130_in = S.Task('T130_in', length=1, delay_cost=1)
	S += T130_in >= 34
	T130_in += MAS_in[2]

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	S += T130_mem0 >= 34
	T130_mem0 += MAS_MEM[2]

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	S += T130_mem1 >= 34
	T130_mem1 += MAS_MEM[1]

	T31 = S.Task('T31', length=2, delay_cost=1)
	S += T31 >= 34
	T31 += MAS[0]

	T70_in = S.Task('T70_in', length=1, delay_cost=1)
	S += T70_in >= 34
	T70_in += MAS_in[3]

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	S += T70_mem0 >= 34
	T70_mem0 += MM_MEM[0]

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	S += T70_mem1 >= 34
	T70_mem1 += MM_MEM[1]

	T9_t0 = S.Task('T9_t0', length=4, delay_cost=1)
	S += T9_t0 >= 34
	T9_t0 += MM[0]

	T11_t0 = S.Task('T11_t0', length=4, delay_cost=1)
	S += T11_t0 >= 35
	T11_t0 += MM[0]

	T11_t3_in = S.Task('T11_t3_in', length=1, delay_cost=1)
	S += T11_t3_in >= 35
	T11_t3_in += MAS_in[1]

	T11_t3_mem0 = S.Task('T11_t3_mem0', length=1, delay_cost=1)
	S += T11_t3_mem0 >= 35
	T11_t3_mem0 += MAS_MEM[4]

	T11_t3_mem1 = S.Task('T11_t3_mem1', length=1, delay_cost=1)
	S += T11_t3_mem1 >= 35
	T11_t3_mem1 += MAS_MEM[1]

	T130 = S.Task('T130', length=2, delay_cost=1)
	S += T130 >= 35
	T130 += MAS[2]

	T4_t5_in = S.Task('T4_t5_in', length=1, delay_cost=1)
	S += T4_t5_in >= 35
	T4_t5_in += MAS_in[0]

	T4_t5_mem0 = S.Task('T4_t5_mem0', length=1, delay_cost=1)
	S += T4_t5_mem0 >= 35
	T4_t5_mem0 += MM_MEM[0]

	T4_t5_mem1 = S.Task('T4_t5_mem1', length=1, delay_cost=1)
	S += T4_t5_mem1 >= 35
	T4_t5_mem1 += MM_MEM[1]

	T70 = S.Task('T70', length=2, delay_cost=1)
	S += T70 >= 35
	T70 += MAS[3]

	T8_t0_in = S.Task('T8_t0_in', length=1, delay_cost=1)
	S += T8_t0_in >= 35
	T8_t0_in += MM_in[0]

	T8_t0_mem0 = S.Task('T8_t0_mem0', length=1, delay_cost=1)
	S += T8_t0_mem0 >= 35
	T8_t0_mem0 += MAIN_MEM_r[0]

	T8_t0_mem1 = S.Task('T8_t0_mem1', length=1, delay_cost=1)
	S += T8_t0_mem1 >= 35
	T8_t0_mem1 += MAS_MEM[3]

	T10_t0_in = S.Task('T10_t0_in', length=1, delay_cost=1)
	S += T10_t0_in >= 36
	T10_t0_in += MM_in[0]

	T10_t0_mem0 = S.Task('T10_t0_mem0', length=1, delay_cost=1)
	S += T10_t0_mem0 >= 36
	T10_t0_mem0 += MAIN_MEM_r[0]

	T10_t0_mem1 = S.Task('T10_t0_mem1', length=1, delay_cost=1)
	S += T10_t0_mem1 >= 36
	T10_t0_mem1 += MAS_MEM[5]

	T10_t3_in = S.Task('T10_t3_in', length=1, delay_cost=1)
	S += T10_t3_in >= 36
	T10_t3_in += MAS_in[1]

	T10_t3_mem0 = S.Task('T10_t3_mem0', length=1, delay_cost=1)
	S += T10_t3_mem0 >= 36
	T10_t3_mem0 += MAS_MEM[4]

	T10_t3_mem1 = S.Task('T10_t3_mem1', length=1, delay_cost=1)
	S += T10_t3_mem1 >= 36
	T10_t3_mem1 += MAS_MEM[1]

	T11_t3 = S.Task('T11_t3', length=2, delay_cost=1)
	S += T11_t3 >= 36
	T11_t3 += MAS[1]

	T150_in = S.Task('T150_in', length=1, delay_cost=1)
	S += T150_in >= 36
	T150_in += MAS_in[3]

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	S += T150_mem0 >= 36
	T150_mem0 += MAS_MEM[6]

	T150_mem1 = S.Task('T150_mem1', length=1, delay_cost=1)
	S += T150_mem1 >= 36
	T150_mem1 += MAS_MEM[7]

	T2_t5_in = S.Task('T2_t5_in', length=1, delay_cost=1)
	S += T2_t5_in >= 36
	T2_t5_in += MAS_in[2]

	T2_t5_mem0 = S.Task('T2_t5_mem0', length=1, delay_cost=1)
	S += T2_t5_mem0 >= 36
	T2_t5_mem0 += MM_MEM[0]

	T2_t5_mem1 = S.Task('T2_t5_mem1', length=1, delay_cost=1)
	S += T2_t5_mem1 >= 36
	T2_t5_mem1 += MM_MEM[1]

	T4_t5 = S.Task('T4_t5', length=2, delay_cost=1)
	S += T4_t5 >= 36
	T4_t5 += MAS[0]

	T8_t0 = S.Task('T8_t0', length=4, delay_cost=1)
	S += T8_t0 >= 36
	T8_t0 += MM[0]

	T10_t0 = S.Task('T10_t0', length=4, delay_cost=1)
	S += T10_t0 >= 37
	T10_t0 += MM[0]

	T10_t3 = S.Task('T10_t3', length=2, delay_cost=1)
	S += T10_t3 >= 37
	T10_t3 += MAS[1]

	T14_t0_in = S.Task('T14_t0_in', length=1, delay_cost=1)
	S += T14_t0_in >= 37
	T14_t0_in += MM_in[0]

	T14_t0_mem0 = S.Task('T14_t0_mem0', length=1, delay_cost=1)
	S += T14_t0_mem0 >= 37
	T14_t0_mem0 += MAS_MEM[4]

	T14_t0_mem1 = S.Task('T14_t0_mem1', length=1, delay_cost=1)
	S += T14_t0_mem1 >= 37
	T14_t0_mem1 += MAS_MEM[5]

	T150 = S.Task('T150', length=2, delay_cost=1)
	S += T150 >= 37
	T150 += MAS[3]

	T2_t5 = S.Task('T2_t5', length=2, delay_cost=1)
	S += T2_t5 >= 37
	T2_t5 += MAS[2]

	T41_in = S.Task('T41_in', length=1, delay_cost=1)
	S += T41_in >= 37
	T41_in += MAS_in[1]

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	S += T41_mem0 >= 37
	T41_mem0 += MM_MEM[0]

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	S += T41_mem1 >= 37
	T41_mem1 += MAS_MEM[1]

	T11_t1_in = S.Task('T11_t1_in', length=1, delay_cost=1)
	S += T11_t1_in >= 38
	T11_t1_in += MM_in[0]

	T11_t1_mem0 = S.Task('T11_t1_mem0', length=1, delay_cost=1)
	S += T11_t1_mem0 >= 38
	T11_t1_mem0 += MAIN_MEM_r[0]

	T11_t1_mem1 = S.Task('T11_t1_mem1', length=1, delay_cost=1)
	S += T11_t1_mem1 >= 38
	T11_t1_mem1 += MAS_MEM[1]

	T14_t0 = S.Task('T14_t0', length=4, delay_cost=1)
	S += T14_t0 >= 38
	T14_t0 += MM[0]

	T21_in = S.Task('T21_in', length=1, delay_cost=1)
	S += T21_in >= 38
	T21_in += MAS_in[1]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 38
	T21_mem0 += MM_MEM[0]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 38
	T21_mem1 += MAS_MEM[5]

	T41 = S.Task('T41', length=2, delay_cost=1)
	S += T41 >= 38
	T41 += MAS[1]

	T10_t1_in = S.Task('T10_t1_in', length=1, delay_cost=1)
	S += T10_t1_in >= 39
	T10_t1_in += MM_in[0]

	T10_t1_mem0 = S.Task('T10_t1_mem0', length=1, delay_cost=1)
	S += T10_t1_mem0 >= 39
	T10_t1_mem0 += MAIN_MEM_r[0]

	T10_t1_mem1 = S.Task('T10_t1_mem1', length=1, delay_cost=1)
	S += T10_t1_mem1 >= 39
	T10_t1_mem1 += MAS_MEM[1]

	T11_t1 = S.Task('T11_t1', length=4, delay_cost=1)
	S += T11_t1 >= 39
	T11_t1 += MM[0]

	T21 = S.Task('T21', length=2, delay_cost=1)
	S += T21 >= 39
	T21 += MAS[1]

	T7_t5_in = S.Task('T7_t5_in', length=1, delay_cost=1)
	S += T7_t5_in >= 39
	T7_t5_in += MAS_in[3]

	T7_t5_mem0 = S.Task('T7_t5_mem0', length=1, delay_cost=1)
	S += T7_t5_mem0 >= 39
	T7_t5_mem0 += MM_MEM[0]

	T7_t5_mem1 = S.Task('T7_t5_mem1', length=1, delay_cost=1)
	S += T7_t5_mem1 >= 39
	T7_t5_mem1 += MM_MEM[1]

	T10_t1 = S.Task('T10_t1', length=4, delay_cost=1)
	S += T10_t1 >= 40
	T10_t1 += MM[0]

	T131_in = S.Task('T131_in', length=1, delay_cost=1)
	S += T131_in >= 40
	T131_in += MAS_in[0]

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	S += T131_mem0 >= 40
	T131_mem0 += MAS_MEM[2]

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	S += T131_mem1 >= 40
	T131_mem1 += MAS_MEM[3]

	T61_in = S.Task('T61_in', length=1, delay_cost=1)
	S += T61_in >= 40
	T61_in += MAS_in[2]

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	S += T61_mem0 >= 40
	T61_mem0 += MM_MEM[0]

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	S += T61_mem1 >= 40
	T61_mem1 += MAS_MEM[5]

	T7_t5 = S.Task('T7_t5', length=2, delay_cost=1)
	S += T7_t5 >= 40
	T7_t5 += MAS[3]

	T9_t4_in = S.Task('T9_t4_in', length=1, delay_cost=1)
	S += T9_t4_in >= 40
	T9_t4_in += MM_in[0]

	T9_t4_mem0 = S.Task('T9_t4_mem0', length=1, delay_cost=1)
	S += T9_t4_mem0 >= 40
	T9_t4_mem0 += MAS_MEM[0]

	T9_t4_mem1 = S.Task('T9_t4_mem1', length=1, delay_cost=1)
	S += T9_t4_mem1 >= 40
	T9_t4_mem1 += MAS_MEM[7]

	T121_in = S.Task('T121_in', length=1, delay_cost=1)
	S += T121_in >= 41
	T121_in += MAS_in[3]

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	S += T121_mem0 >= 41
	T121_mem0 += MAS_MEM[2]

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	S += T121_mem1 >= 41
	T121_mem1 += MAS_MEM[3]

	T131 = S.Task('T131', length=2, delay_cost=1)
	S += T131 >= 41
	T131 += MAS[0]

	T61 = S.Task('T61', length=2, delay_cost=1)
	S += T61 >= 41
	T61 += MAS[2]

	T71_in = S.Task('T71_in', length=1, delay_cost=1)
	S += T71_in >= 41
	T71_in += MAS_in[0]

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	S += T71_mem0 >= 41
	T71_mem0 += MM_MEM[0]

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	S += T71_mem1 >= 41
	T71_mem1 += MAS_MEM[7]

	T9_t4 = S.Task('T9_t4', length=4, delay_cost=1)
	S += T9_t4 >= 41
	T9_t4 += MM[0]

	T121 = S.Task('T121', length=2, delay_cost=1)
	S += T121 >= 42
	T121 += MAS[3]

	T14_t2_in = S.Task('T14_t2_in', length=1, delay_cost=1)
	S += T14_t2_in >= 42
	T14_t2_in += MAS_in[2]

	T14_t2_mem0 = S.Task('T14_t2_mem0', length=1, delay_cost=1)
	S += T14_t2_mem0 >= 42
	T14_t2_mem0 += MAS_MEM[4]

	T14_t2_mem1 = S.Task('T14_t2_mem1', length=1, delay_cost=1)
	S += T14_t2_mem1 >= 42
	T14_t2_mem1 += MAS_MEM[1]

	T71 = S.Task('T71', length=2, delay_cost=1)
	S += T71 >= 42
	T71 += MAS[0]

	T8_t4_in = S.Task('T8_t4_in', length=1, delay_cost=1)
	S += T8_t4_in >= 42
	T8_t4_in += MM_in[0]

	T8_t4_mem0 = S.Task('T8_t4_mem0', length=1, delay_cost=1)
	S += T8_t4_mem0 >= 42
	T8_t4_mem0 += MAS_MEM[6]

	T8_t4_mem1 = S.Task('T8_t4_mem1', length=1, delay_cost=1)
	S += T8_t4_mem1 >= 42
	T8_t4_mem1 += MAS_MEM[7]

	T90_in = S.Task('T90_in', length=1, delay_cost=1)
	S += T90_in >= 42
	T90_in += MAS_in[3]

	T90_mem0 = S.Task('T90_mem0', length=1, delay_cost=1)
	S += T90_mem0 >= 42
	T90_mem0 += MM_MEM[0]

	T90_mem1 = S.Task('T90_mem1', length=1, delay_cost=1)
	S += T90_mem1 >= 42
	T90_mem1 += MM_MEM[1]

	T10_t4_in = S.Task('T10_t4_in', length=1, delay_cost=1)
	S += T10_t4_in >= 43
	T10_t4_in += MM_in[0]

	T10_t4_mem0 = S.Task('T10_t4_mem0', length=1, delay_cost=1)
	S += T10_t4_mem0 >= 43
	T10_t4_mem0 += MAS_MEM[6]

	T10_t4_mem1 = S.Task('T10_t4_mem1', length=1, delay_cost=1)
	S += T10_t4_mem1 >= 43
	T10_t4_mem1 += MAS_MEM[3]

	T14_t2 = S.Task('T14_t2', length=2, delay_cost=1)
	S += T14_t2 >= 43
	T14_t2 += MAS[2]

	T151_in = S.Task('T151_in', length=1, delay_cost=1)
	S += T151_in >= 43
	T151_in += MAS_in[2]

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	S += T151_mem0 >= 43
	T151_mem0 += MAS_MEM[0]

	T151_mem1 = S.Task('T151_mem1', length=1, delay_cost=1)
	S += T151_mem1 >= 43
	T151_mem1 += MAS_MEM[1]

	T80_in = S.Task('T80_in', length=1, delay_cost=1)
	S += T80_in >= 43
	T80_in += MAS_in[1]

	T80_mem0 = S.Task('T80_mem0', length=1, delay_cost=1)
	S += T80_mem0 >= 43
	T80_mem0 += MM_MEM[0]

	T80_mem1 = S.Task('T80_mem1', length=1, delay_cost=1)
	S += T80_mem1 >= 43
	T80_mem1 += MM_MEM[1]

	T8_t4 = S.Task('T8_t4', length=4, delay_cost=1)
	S += T8_t4 >= 43
	T8_t4 += MM[0]

	T90 = S.Task('T90', length=2, delay_cost=1)
	S += T90 >= 43
	T90 += MAS[3]

	T100_in = S.Task('T100_in', length=1, delay_cost=1)
	S += T100_in >= 44
	T100_in += MAS_in[0]

	T100_mem0 = S.Task('T100_mem0', length=1, delay_cost=1)
	S += T100_mem0 >= 44
	T100_mem0 += MM_MEM[0]

	T100_mem1 = S.Task('T100_mem1', length=1, delay_cost=1)
	S += T100_mem1 >= 44
	T100_mem1 += MM_MEM[1]

	T10_t4 = S.Task('T10_t4', length=4, delay_cost=1)
	S += T10_t4 >= 44
	T10_t4 += MM[0]

	T11_t4_in = S.Task('T11_t4_in', length=1, delay_cost=1)
	S += T11_t4_in >= 44
	T11_t4_in += MM_in[0]

	T11_t4_mem0 = S.Task('T11_t4_mem0', length=1, delay_cost=1)
	S += T11_t4_mem0 >= 44
	T11_t4_mem0 += MAS_MEM[6]

	T11_t4_mem1 = S.Task('T11_t4_mem1', length=1, delay_cost=1)
	S += T11_t4_mem1 >= 44
	T11_t4_mem1 += MAS_MEM[3]

	T14_t3_in = S.Task('T14_t3_in', length=1, delay_cost=1)
	S += T14_t3_in >= 44
	T14_t3_in += MAS_in[1]

	T14_t3_mem0 = S.Task('T14_t3_mem0', length=1, delay_cost=1)
	S += T14_t3_mem0 >= 44
	T14_t3_mem0 += MAS_MEM[4]

	T14_t3_mem1 = S.Task('T14_t3_mem1', length=1, delay_cost=1)
	S += T14_t3_mem1 >= 44
	T14_t3_mem1 += MAS_MEM[1]

	T151 = S.Task('T151', length=2, delay_cost=1)
	S += T151 >= 44
	T151 += MAS[2]

	T180_in = S.Task('T180_in', length=1, delay_cost=1)
	S += T180_in >= 44
	T180_in += MAS_in[2]

	T180_mem0 = S.Task('T180_mem0', length=1, delay_cost=1)
	S += T180_mem0 >= 44
	T180_mem0 += MAS_MEM[0]

	T180_mem1 = S.Task('T180_mem1', length=1, delay_cost=1)
	S += T180_mem1 >= 44
	T180_mem1 += MAS_MEM[7]

	T80 = S.Task('T80', length=2, delay_cost=1)
	S += T80 >= 44
	T80 += MAS[1]

	T100 = S.Task('T100', length=2, delay_cost=1)
	S += T100 >= 45
	T100 += MAS[0]

	T11_t4 = S.Task('T11_t4', length=4, delay_cost=1)
	S += T11_t4 >= 45
	T11_t4 += MM[0]

	T14_t3 = S.Task('T14_t3', length=2, delay_cost=1)
	S += T14_t3 >= 45
	T14_t3 += MAS[1]

	T16_t0_in = S.Task('T16_t0_in', length=1, delay_cost=1)
	S += T16_t0_in >= 45
	T16_t0_in += MM_in[0]

	T16_t0_mem0 = S.Task('T16_t0_mem0', length=1, delay_cost=1)
	S += T16_t0_mem0 >= 45
	T16_t0_mem0 += MAS_MEM[2]

	T16_t0_mem1 = S.Task('T16_t0_mem1', length=1, delay_cost=1)
	S += T16_t0_mem1 >= 45
	T16_t0_mem1 += MAS_MEM[3]

	T17_t3_in = S.Task('T17_t3_in', length=1, delay_cost=1)
	S += T17_t3_in >= 45
	T17_t3_in += MAS_in[2]

	T17_t3_mem0 = S.Task('T17_t3_mem0', length=1, delay_cost=1)
	S += T17_t3_mem0 >= 45
	T17_t3_mem0 += MAS_MEM[6]

	T17_t3_mem1 = S.Task('T17_t3_mem1', length=1, delay_cost=1)
	S += T17_t3_mem1 >= 45
	T17_t3_mem1 += MAS_MEM[5]

	T180 = S.Task('T180', length=2, delay_cost=1)
	S += T180 >= 45
	T180 += MAS[2]

	T190_in = S.Task('T190_in', length=1, delay_cost=1)
	S += T190_in >= 45
	T190_in += MAS_in[1]

	T190_mem0 = S.Task('T190_mem0', length=1, delay_cost=1)
	S += T190_mem0 >= 45
	T190_mem0 += MAS_MEM[0]

	T190_mem1 = S.Task('T190_mem1', length=1, delay_cost=1)
	S += T190_mem1 >= 45
	T190_mem1 += MAS_MEM[7]

	T8_t5_in = S.Task('T8_t5_in', length=1, delay_cost=1)
	S += T8_t5_in >= 45
	T8_t5_in += MAS_in[0]

	T8_t5_mem0 = S.Task('T8_t5_mem0', length=1, delay_cost=1)
	S += T8_t5_mem0 >= 45
	T8_t5_mem0 += MM_MEM[0]

	T8_t5_mem1 = S.Task('T8_t5_mem1', length=1, delay_cost=1)
	S += T8_t5_mem1 >= 45
	T8_t5_mem1 += MM_MEM[1]

	T14_t4_in = S.Task('T14_t4_in', length=1, delay_cost=1)
	S += T14_t4_in >= 46
	T14_t4_in += MM_in[0]

	T14_t4_mem0 = S.Task('T14_t4_mem0', length=1, delay_cost=1)
	S += T14_t4_mem0 >= 46
	T14_t4_mem0 += MAS_MEM[4]

	T14_t4_mem1 = S.Task('T14_t4_mem1', length=1, delay_cost=1)
	S += T14_t4_mem1 >= 46
	T14_t4_mem1 += MAS_MEM[3]

	T16_t0 = S.Task('T16_t0', length=4, delay_cost=1)
	S += T16_t0 >= 46
	T16_t0 += MM[0]

	T17_t3 = S.Task('T17_t3', length=2, delay_cost=1)
	S += T17_t3 >= 46
	T17_t3 += MAS[2]

	T190 = S.Task('T190', length=2, delay_cost=1)
	S += T190 >= 46
	T190 += MAS[1]

	T210_in = S.Task('T210_in', length=1, delay_cost=1)
	S += T210_in >= 46
	T210_in += MAS_in[0]

	T210_mem0 = S.Task('T210_mem0', length=1, delay_cost=1)
	S += T210_mem0 >= 46
	T210_mem0 += MAS_MEM[0]

	T210_mem1 = S.Task('T210_mem1', length=1, delay_cost=1)
	S += T210_mem1 >= 46
	T210_mem1 += MAS_MEM[1]

	T24_t3_in = S.Task('T24_t3_in', length=1, delay_cost=1)
	S += T24_t3_in >= 46
	T24_t3_in += MAS_in[2]

	T24_t3_mem0 = S.Task('T24_t3_mem0', length=1, delay_cost=1)
	S += T24_t3_mem0 >= 46
	T24_t3_mem0 += MAS_MEM[6]

	T24_t3_mem1 = S.Task('T24_t3_mem1', length=1, delay_cost=1)
	S += T24_t3_mem1 >= 46
	T24_t3_mem1 += MAS_MEM[7]

	T8_t5 = S.Task('T8_t5', length=2, delay_cost=1)
	S += T8_t5 >= 46
	T8_t5 += MAS[0]

	T9_t5_in = S.Task('T9_t5_in', length=1, delay_cost=1)
	S += T9_t5_in >= 46
	T9_t5_in += MAS_in[1]

	T9_t5_mem0 = S.Task('T9_t5_mem0', length=1, delay_cost=1)
	S += T9_t5_mem0 >= 46
	T9_t5_mem0 += MM_MEM[0]

	T9_t5_mem1 = S.Task('T9_t5_mem1', length=1, delay_cost=1)
	S += T9_t5_mem1 >= 46
	T9_t5_mem1 += MM_MEM[1]

	T14_t4 = S.Task('T14_t4', length=4, delay_cost=1)
	S += T14_t4 >= 47
	T14_t4 += MM[0]

	T17_t0_in = S.Task('T17_t0_in', length=1, delay_cost=1)
	S += T17_t0_in >= 47
	T17_t0_in += MM_in[0]

	T17_t0_mem0 = S.Task('T17_t0_mem0', length=1, delay_cost=1)
	S += T17_t0_mem0 >= 47
	T17_t0_mem0 += MAS_MEM[2]

	T17_t0_mem1 = S.Task('T17_t0_mem1', length=1, delay_cost=1)
	S += T17_t0_mem1 >= 47
	T17_t0_mem1 += MAS_MEM[7]

	T210 = S.Task('T210', length=2, delay_cost=1)
	S += T210 >= 47
	T210 += MAS[0]

	T24_t3 = S.Task('T24_t3', length=2, delay_cost=1)
	S += T24_t3 >= 47
	T24_t3 += MAS[2]

	T81_in = S.Task('T81_in', length=1, delay_cost=1)
	S += T81_in >= 47
	T81_in += MAS_in[3]

	T81_mem0 = S.Task('T81_mem0', length=1, delay_cost=1)
	S += T81_mem0 >= 47
	T81_mem0 += MM_MEM[0]

	T81_mem1 = S.Task('T81_mem1', length=1, delay_cost=1)
	S += T81_mem1 >= 47
	T81_mem1 += MAS_MEM[1]

	T9_t5 = S.Task('T9_t5', length=2, delay_cost=1)
	S += T9_t5 >= 47
	T9_t5 += MAS[1]

	T14_t1_in = S.Task('T14_t1_in', length=1, delay_cost=1)
	S += T14_t1_in >= 48
	T14_t1_in += MM_in[0]

	T14_t1_mem0 = S.Task('T14_t1_mem0', length=1, delay_cost=1)
	S += T14_t1_mem0 >= 48
	T14_t1_mem0 += MAS_MEM[0]

	T14_t1_mem1 = S.Task('T14_t1_mem1', length=1, delay_cost=1)
	S += T14_t1_mem1 >= 48
	T14_t1_mem1 += MAS_MEM[1]

	T17_t0 = S.Task('T17_t0', length=4, delay_cost=1)
	S += T17_t0 >= 48
	T17_t0 += MM[0]

	T81 = S.Task('T81', length=2, delay_cost=1)
	S += T81 >= 48
	T81 += MAS[3]

	T91_in = S.Task('T91_in', length=1, delay_cost=1)
	S += T91_in >= 48
	T91_in += MAS_in[1]

	T91_mem0 = S.Task('T91_mem0', length=1, delay_cost=1)
	S += T91_mem0 >= 48
	T91_mem0 += MM_MEM[0]

	T91_mem1 = S.Task('T91_mem1', length=1, delay_cost=1)
	S += T91_mem1 >= 48
	T91_mem1 += MAS_MEM[3]

	T11_t5_in = S.Task('T11_t5_in', length=1, delay_cost=1)
	S += T11_t5_in >= 49
	T11_t5_in += MAS_in[0]

	T11_t5_mem0 = S.Task('T11_t5_mem0', length=1, delay_cost=1)
	S += T11_t5_mem0 >= 49
	T11_t5_mem0 += MM_MEM[0]

	T11_t5_mem1 = S.Task('T11_t5_mem1', length=1, delay_cost=1)
	S += T11_t5_mem1 >= 49
	T11_t5_mem1 += MM_MEM[1]

	T14_t1 = S.Task('T14_t1', length=4, delay_cost=1)
	S += T14_t1 >= 49
	T14_t1 += MM[0]

	T17_t2_in = S.Task('T17_t2_in', length=1, delay_cost=1)
	S += T17_t2_in >= 49
	T17_t2_in += MAS_in[1]

	T17_t2_mem0 = S.Task('T17_t2_mem0', length=1, delay_cost=1)
	S += T17_t2_mem0 >= 49
	T17_t2_mem0 += MAS_MEM[2]

	T17_t2_mem1 = S.Task('T17_t2_mem1', length=1, delay_cost=1)
	S += T17_t2_mem1 >= 49
	T17_t2_mem1 += MAS_MEM[7]

	T20_t0_in = S.Task('T20_t0_in', length=1, delay_cost=1)
	S += T20_t0_in >= 49
	T20_t0_in += MM_in[0]

	T20_t0_mem0 = S.Task('T20_t0_mem0', length=1, delay_cost=1)
	S += T20_t0_mem0 >= 49
	T20_t0_mem0 += MAS_MEM[0]

	T20_t0_mem1 = S.Task('T20_t0_mem1', length=1, delay_cost=1)
	S += T20_t0_mem1 >= 49
	T20_t0_mem1 += MAS_MEM[5]

	T91 = S.Task('T91', length=2, delay_cost=1)
	S += T91 >= 49
	T91 += MAS[1]

	T110_in = S.Task('T110_in', length=1, delay_cost=1)
	S += T110_in >= 50
	T110_in += MAS_in[2]

	T110_mem0 = S.Task('T110_mem0', length=1, delay_cost=1)
	S += T110_mem0 >= 50
	T110_mem0 += MM_MEM[0]

	T110_mem1 = S.Task('T110_mem1', length=1, delay_cost=1)
	S += T110_mem1 >= 50
	T110_mem1 += MM_MEM[1]

	T11_t5 = S.Task('T11_t5', length=2, delay_cost=1)
	S += T11_t5 >= 50
	T11_t5 += MAS[0]

	T16_t3_in = S.Task('T16_t3_in', length=1, delay_cost=1)
	S += T16_t3_in >= 50
	T16_t3_in += MAS_in[1]

	T16_t3_mem0 = S.Task('T16_t3_mem0', length=1, delay_cost=1)
	S += T16_t3_mem0 >= 50
	T16_t3_mem0 += MAS_MEM[2]

	T16_t3_mem1 = S.Task('T16_t3_mem1', length=1, delay_cost=1)
	S += T16_t3_mem1 >= 50
	T16_t3_mem1 += MAS_MEM[7]

	T17_t1_in = S.Task('T17_t1_in', length=1, delay_cost=1)
	S += T17_t1_in >= 50
	T17_t1_in += MM_in[0]

	T17_t1_mem0 = S.Task('T17_t1_mem0', length=1, delay_cost=1)
	S += T17_t1_mem0 >= 50
	T17_t1_mem0 += MAS_MEM[6]

	T17_t1_mem1 = S.Task('T17_t1_mem1', length=1, delay_cost=1)
	S += T17_t1_mem1 >= 50
	T17_t1_mem1 += MAS_MEM[5]

	T17_t2 = S.Task('T17_t2', length=2, delay_cost=1)
	S += T17_t2 >= 50
	T17_t2 += MAS[1]

	T191_in = S.Task('T191_in', length=1, delay_cost=1)
	S += T191_in >= 50
	T191_in += MAS_in[0]

	T191_mem0 = S.Task('T191_mem0', length=1, delay_cost=1)
	S += T191_mem0 >= 50
	T191_mem0 += MAS_MEM[0]

	T191_mem1 = S.Task('T191_mem1', length=1, delay_cost=1)
	S += T191_mem1 >= 50
	T191_mem1 += MAS_MEM[3]

	T20_t0 = S.Task('T20_t0', length=4, delay_cost=1)
	S += T20_t0 >= 50
	T20_t0 += MM[0]

	T110 = S.Task('T110', length=2, delay_cost=1)
	S += T110 >= 51
	T110 += MAS[2]

	T111_in = S.Task('T111_in', length=1, delay_cost=1)
	S += T111_in >= 51
	T111_in += MAS_in[0]

	T111_mem0 = S.Task('T111_mem0', length=1, delay_cost=1)
	S += T111_mem0 >= 51
	T111_mem0 += MM_MEM[0]

	T111_mem1 = S.Task('T111_mem1', length=1, delay_cost=1)
	S += T111_mem1 >= 51
	T111_mem1 += MAS_MEM[1]

	T16_t1_in = S.Task('T16_t1_in', length=1, delay_cost=1)
	S += T16_t1_in >= 51
	T16_t1_in += MM_in[0]

	T16_t1_mem0 = S.Task('T16_t1_mem0', length=1, delay_cost=1)
	S += T16_t1_mem0 >= 51
	T16_t1_mem0 += MAS_MEM[4]

	T16_t1_mem1 = S.Task('T16_t1_mem1', length=1, delay_cost=1)
	S += T16_t1_mem1 >= 51
	T16_t1_mem1 += MAS_MEM[7]

	T16_t3 = S.Task('T16_t3', length=2, delay_cost=1)
	S += T16_t3 >= 51
	T16_t3 += MAS[1]

	T17_t1 = S.Task('T17_t1', length=4, delay_cost=1)
	S += T17_t1 >= 51
	T17_t1 += MM[0]

	T181_in = S.Task('T181_in', length=1, delay_cost=1)
	S += T181_in >= 51
	T181_in += MAS_in[3]

	T181_mem0 = S.Task('T181_mem0', length=1, delay_cost=1)
	S += T181_mem0 >= 51
	T181_mem0 += MAS_MEM[0]

	T181_mem1 = S.Task('T181_mem1', length=1, delay_cost=1)
	S += T181_mem1 >= 51
	T181_mem1 += MAS_MEM[3]

	T191 = S.Task('T191', length=2, delay_cost=1)
	S += T191 >= 51
	T191 += MAS[0]

	T111 = S.Task('T111', length=2, delay_cost=1)
	S += T111 >= 52
	T111 += MAS[0]

	T140_in = S.Task('T140_in', length=1, delay_cost=1)
	S += T140_in >= 52
	T140_in += MAS_in[0]

	T140_mem0 = S.Task('T140_mem0', length=1, delay_cost=1)
	S += T140_mem0 >= 52
	T140_mem0 += MM_MEM[0]

	T140_mem1 = S.Task('T140_mem1', length=1, delay_cost=1)
	S += T140_mem1 >= 52
	T140_mem1 += MM_MEM[1]

	T16_t1 = S.Task('T16_t1', length=4, delay_cost=1)
	S += T16_t1 >= 52
	T16_t1 += MM[0]

	T181 = S.Task('T181', length=2, delay_cost=1)
	S += T181 >= 52
	T181 += MAS[3]

	T23_t0_in = S.Task('T23_t0_in', length=1, delay_cost=1)
	S += T23_t0_in >= 52
	T23_t0_in += MAS_in[1]

	T23_t0_mem0 = S.Task('T23_t0_mem0', length=1, delay_cost=1)
	S += T23_t0_mem0 >= 52
	T23_t0_mem0 += MAS_MEM[2]

	T23_t0_mem1 = S.Task('T23_t0_mem1', length=1, delay_cost=1)
	S += T23_t0_mem1 >= 52
	T23_t0_mem1 += MAS_MEM[1]

	T24_t0_in = S.Task('T24_t0_in', length=1, delay_cost=1)
	S += T24_t0_in >= 52
	T24_t0_in += MM_in[0]

	T24_t0_mem0 = S.Task('T24_t0_mem0', length=1, delay_cost=1)
	S += T24_t0_mem0 >= 52
	T24_t0_mem0 += MAS_MEM[4]

	T24_t0_mem1 = S.Task('T24_t0_mem1', length=1, delay_cost=1)
	S += T24_t0_mem1 >= 52
	T24_t0_mem1 += MAS_MEM[7]

	T10_t5_in = S.Task('T10_t5_in', length=1, delay_cost=1)
	S += T10_t5_in >= 53
	T10_t5_in += MAS_in[0]

	T10_t5_mem0 = S.Task('T10_t5_mem0', length=1, delay_cost=1)
	S += T10_t5_mem0 >= 53
	T10_t5_mem0 += MM_MEM[0]

	T10_t5_mem1 = S.Task('T10_t5_mem1', length=1, delay_cost=1)
	S += T10_t5_mem1 >= 53
	T10_t5_mem1 += MM_MEM[1]

	T140 = S.Task('T140', length=2, delay_cost=1)
	S += T140 >= 53
	T140 += MAS[0]

	T23_t0 = S.Task('T23_t0', length=2, delay_cost=1)
	S += T23_t0 >= 53
	T23_t0 += MAS[1]

	T24_t0 = S.Task('T24_t0', length=4, delay_cost=1)
	S += T24_t0 >= 53
	T24_t0 += MM[0]

	T24_t1_in = S.Task('T24_t1_in', length=1, delay_cost=1)
	S += T24_t1_in >= 53
	T24_t1_in += MM_in[0]

	T24_t1_mem0 = S.Task('T24_t1_mem0', length=1, delay_cost=1)
	S += T24_t1_mem0 >= 53
	T24_t1_mem0 += MAS_MEM[0]

	T24_t1_mem1 = S.Task('T24_t1_mem1', length=1, delay_cost=1)
	S += T24_t1_mem1 >= 53
	T24_t1_mem1 += MAS_MEM[7]

	T24_t2_in = S.Task('T24_t2_in', length=1, delay_cost=1)
	S += T24_t2_in >= 53
	T24_t2_in += MAS_in[3]

	T24_t2_mem0 = S.Task('T24_t2_mem0', length=1, delay_cost=1)
	S += T24_t2_mem0 >= 53
	T24_t2_mem0 += MAS_MEM[4]

	T24_t2_mem1 = S.Task('T24_t2_mem1', length=1, delay_cost=1)
	S += T24_t2_mem1 >= 53
	T24_t2_mem1 += MAS_MEM[1]

	T10_t5 = S.Task('T10_t5', length=2, delay_cost=1)
	S += T10_t5 >= 54
	T10_t5 += MAS[0]

	T14_t5_in = S.Task('T14_t5_in', length=1, delay_cost=1)
	S += T14_t5_in >= 54
	T14_t5_in += MAS_in[0]

	T14_t5_mem0 = S.Task('T14_t5_mem0', length=1, delay_cost=1)
	S += T14_t5_mem0 >= 54
	T14_t5_mem0 += MM_MEM[0]

	T14_t5_mem1 = S.Task('T14_t5_mem1', length=1, delay_cost=1)
	S += T14_t5_mem1 >= 54
	T14_t5_mem1 += MM_MEM[1]

	T20_t3_in = S.Task('T20_t3_in', length=1, delay_cost=1)
	S += T20_t3_in >= 54
	T20_t3_in += MAS_in[3]

	T20_t3_mem0 = S.Task('T20_t3_mem0', length=1, delay_cost=1)
	S += T20_t3_mem0 >= 54
	T20_t3_mem0 += MAS_MEM[4]

	T20_t3_mem1 = S.Task('T20_t3_mem1', length=1, delay_cost=1)
	S += T20_t3_mem1 >= 54
	T20_t3_mem1 += MAS_MEM[7]

	T24_t1 = S.Task('T24_t1', length=4, delay_cost=1)
	S += T24_t1 >= 54
	T24_t1 += MM[0]

	T24_t2 = S.Task('T24_t2', length=2, delay_cost=1)
	S += T24_t2 >= 54
	T24_t2 += MAS[3]

	Z3_t0_in = S.Task('Z3_t0_in', length=1, delay_cost=1)
	S += Z3_t0_in >= 54
	Z3_t0_in += MM_in[0]

	Z3_t0_mem0 = S.Task('Z3_t0_mem0', length=1, delay_cost=1)
	S += Z3_t0_mem0 >= 54
	Z3_t0_mem0 += MAIN_MEM_r[0]

	Z3_t0_mem1 = S.Task('Z3_t0_mem1', length=1, delay_cost=1)
	S += Z3_t0_mem1 >= 54
	Z3_t0_mem1 += MAS_MEM[1]

	T101_in = S.Task('T101_in', length=1, delay_cost=1)
	S += T101_in >= 55
	T101_in += MAS_in[0]

	T101_mem0 = S.Task('T101_mem0', length=1, delay_cost=1)
	S += T101_mem0 >= 55
	T101_mem0 += MM_MEM[0]

	T101_mem1 = S.Task('T101_mem1', length=1, delay_cost=1)
	S += T101_mem1 >= 55
	T101_mem1 += MAS_MEM[1]

	T14_t5 = S.Task('T14_t5', length=2, delay_cost=1)
	S += T14_t5 >= 55
	T14_t5 += MAS[0]

	T20_t1_in = S.Task('T20_t1_in', length=1, delay_cost=1)
	S += T20_t1_in >= 55
	T20_t1_in += MM_in[0]

	T20_t1_mem0 = S.Task('T20_t1_mem0', length=1, delay_cost=1)
	S += T20_t1_mem0 >= 55
	T20_t1_mem0 += MAS_MEM[0]

	T20_t1_mem1 = S.Task('T20_t1_mem1', length=1, delay_cost=1)
	S += T20_t1_mem1 >= 55
	T20_t1_mem1 += MAS_MEM[7]

	T20_t3 = S.Task('T20_t3', length=2, delay_cost=1)
	S += T20_t3 >= 55
	T20_t3 += MAS[3]

	Z3_t0 = S.Task('Z3_t0', length=4, delay_cost=1)
	S += Z3_t0 >= 55
	Z3_t0 += MM[0]

	T101 = S.Task('T101', length=2, delay_cost=1)
	S += T101 >= 56
	T101 += MAS[0]

	T141_in = S.Task('T141_in', length=1, delay_cost=1)
	S += T141_in >= 56
	T141_in += MAS_in[3]

	T141_mem0 = S.Task('T141_mem0', length=1, delay_cost=1)
	S += T141_mem0 >= 56
	T141_mem0 += MM_MEM[0]

	T141_mem1 = S.Task('T141_mem1', length=1, delay_cost=1)
	S += T141_mem1 >= 56
	T141_mem1 += MAS_MEM[1]

	T20_t1 = S.Task('T20_t1', length=4, delay_cost=1)
	S += T20_t1 >= 56
	T20_t1 += MM[0]

	T20_t4_in = S.Task('T20_t4_in', length=1, delay_cost=1)
	S += T20_t4_in >= 56
	T20_t4_in += MM_in[0]

	T20_t4_mem0 = S.Task('T20_t4_mem0', length=1, delay_cost=1)
	S += T20_t4_mem0 >= 56
	T20_t4_mem0 += MAS_MEM[2]

	T20_t4_mem1 = S.Task('T20_t4_mem1', length=1, delay_cost=1)
	S += T20_t4_mem1 >= 56
	T20_t4_mem1 += MAS_MEM[7]

	T141 = S.Task('T141', length=2, delay_cost=1)
	S += T141 >= 57
	T141 += MAS[3]

	T17_t4_in = S.Task('T17_t4_in', length=1, delay_cost=1)
	S += T17_t4_in >= 57
	T17_t4_in += MM_in[0]

	T17_t4_mem0 = S.Task('T17_t4_mem0', length=1, delay_cost=1)
	S += T17_t4_mem0 >= 57
	T17_t4_mem0 += MAS_MEM[2]

	T17_t4_mem1 = S.Task('T17_t4_mem1', length=1, delay_cost=1)
	S += T17_t4_mem1 >= 57
	T17_t4_mem1 += MAS_MEM[5]

	T20_t4 = S.Task('T20_t4', length=4, delay_cost=1)
	S += T20_t4 >= 57
	T20_t4 += MM[0]

	T211_in = S.Task('T211_in', length=1, delay_cost=1)
	S += T211_in >= 57
	T211_in += MAS_in[3]

	T211_mem0 = S.Task('T211_mem0', length=1, delay_cost=1)
	S += T211_mem0 >= 57
	T211_mem0 += MAS_MEM[4]

	T211_mem1 = S.Task('T211_mem1', length=1, delay_cost=1)
	S += T211_mem1 >= 57
	T211_mem1 += MAS_MEM[1]

	T24_t5_in = S.Task('T24_t5_in', length=1, delay_cost=1)
	S += T24_t5_in >= 57
	T24_t5_in += MAS_in[0]

	T24_t5_mem0 = S.Task('T24_t5_mem0', length=1, delay_cost=1)
	S += T24_t5_mem0 >= 57
	T24_t5_mem0 += MM_MEM[0]

	T24_t5_mem1 = S.Task('T24_t5_mem1', length=1, delay_cost=1)
	S += T24_t5_mem1 >= 57
	T24_t5_mem1 += MM_MEM[1]

	T16_t5_in = S.Task('T16_t5_in', length=1, delay_cost=1)
	S += T16_t5_in >= 58
	T16_t5_in += MAS_in[3]

	T16_t5_mem0 = S.Task('T16_t5_mem0', length=1, delay_cost=1)
	S += T16_t5_mem0 >= 58
	T16_t5_mem0 += MM_MEM[0]

	T16_t5_mem1 = S.Task('T16_t5_mem1', length=1, delay_cost=1)
	S += T16_t5_mem1 >= 58
	T16_t5_mem1 += MM_MEM[1]

	T17_t4 = S.Task('T17_t4', length=4, delay_cost=1)
	S += T17_t4 >= 58
	T17_t4 += MM[0]

	T211 = S.Task('T211', length=2, delay_cost=1)
	S += T211 >= 58
	T211 += MAS[3]

	T23_t1_in = S.Task('T23_t1_in', length=1, delay_cost=1)
	S += T23_t1_in >= 58
	T23_t1_in += MAS_in[1]

	T23_t1_mem0 = S.Task('T23_t1_mem0', length=1, delay_cost=1)
	S += T23_t1_mem0 >= 58
	T23_t1_mem0 += MAS_MEM[2]

	T23_t1_mem1 = S.Task('T23_t1_mem1', length=1, delay_cost=1)
	S += T23_t1_mem1 >= 58
	T23_t1_mem1 += MAS_MEM[1]

	T24_t4_in = S.Task('T24_t4_in', length=1, delay_cost=1)
	S += T24_t4_in >= 58
	T24_t4_in += MM_in[0]

	T24_t4_mem0 = S.Task('T24_t4_mem0', length=1, delay_cost=1)
	S += T24_t4_mem0 >= 58
	T24_t4_mem0 += MAS_MEM[6]

	T24_t4_mem1 = S.Task('T24_t4_mem1', length=1, delay_cost=1)
	S += T24_t4_mem1 >= 58
	T24_t4_mem1 += MAS_MEM[5]

	T24_t5 = S.Task('T24_t5', length=2, delay_cost=1)
	S += T24_t5 >= 58
	T24_t5 += MAS[0]

	Z3_t3_in = S.Task('Z3_t3_in', length=1, delay_cost=1)
	S += Z3_t3_in >= 58
	Z3_t3_in += MAS_in[2]

	Z3_t3_mem0 = S.Task('Z3_t3_mem0', length=1, delay_cost=1)
	S += Z3_t3_mem0 >= 58
	Z3_t3_mem0 += MAS_MEM[0]

	Z3_t3_mem1 = S.Task('Z3_t3_mem1', length=1, delay_cost=1)
	S += Z3_t3_mem1 >= 58
	Z3_t3_mem1 += MAS_MEM[7]

	T16_t4_in = S.Task('T16_t4_in', length=1, delay_cost=1)
	S += T16_t4_in >= 59
	T16_t4_in += MM_in[0]

	T16_t4_mem0 = S.Task('T16_t4_mem0', length=1, delay_cost=1)
	S += T16_t4_mem0 >= 59
	T16_t4_mem0 += MAS_MEM[2]

	T16_t4_mem1 = S.Task('T16_t4_mem1', length=1, delay_cost=1)
	S += T16_t4_mem1 >= 59
	T16_t4_mem1 += MAS_MEM[3]

	T16_t5 = S.Task('T16_t5', length=2, delay_cost=1)
	S += T16_t5 >= 59
	T16_t5 += MAS[3]

	T200_in = S.Task('T200_in', length=1, delay_cost=1)
	S += T200_in >= 59
	T200_in += MAS_in[1]

	T200_mem0 = S.Task('T200_mem0', length=1, delay_cost=1)
	S += T200_mem0 >= 59
	T200_mem0 += MM_MEM[0]

	T200_mem1 = S.Task('T200_mem1', length=1, delay_cost=1)
	S += T200_mem1 >= 59
	T200_mem1 += MM_MEM[1]

	T22_t0_in = S.Task('T22_t0_in', length=1, delay_cost=1)
	S += T22_t0_in >= 59
	T22_t0_in += MAS_in[3]

	T22_t0_mem0 = S.Task('T22_t0_mem0', length=1, delay_cost=1)
	S += T22_t0_mem0 >= 59
	T22_t0_mem0 += MAS_MEM[0]

	T22_t0_mem1 = S.Task('T22_t0_mem1', length=1, delay_cost=1)
	S += T22_t0_mem1 >= 59
	T22_t0_mem1 += MAS_MEM[7]

	T23_t1 = S.Task('T23_t1', length=2, delay_cost=1)
	S += T23_t1 >= 59
	T23_t1 += MAS[1]

	T24_t4 = S.Task('T24_t4', length=4, delay_cost=1)
	S += T24_t4 >= 59
	T24_t4 += MM[0]

	Z3_t3 = S.Task('Z3_t3', length=2, delay_cost=1)
	S += Z3_t3 >= 59
	Z3_t3 += MAS[2]

	T16_t4 = S.Task('T16_t4', length=4, delay_cost=1)
	S += T16_t4 >= 60
	T16_t4 += MM[0]

	T200 = S.Task('T200', length=2, delay_cost=1)
	S += T200 >= 60
	T200 += MAS[1]

	T20_t5_in = S.Task('T20_t5_in', length=1, delay_cost=1)
	S += T20_t5_in >= 60
	T20_t5_in += MAS_in[0]

	T20_t5_mem0 = S.Task('T20_t5_mem0', length=1, delay_cost=1)
	S += T20_t5_mem0 >= 60
	T20_t5_mem0 += MM_MEM[0]

	T20_t5_mem1 = S.Task('T20_t5_mem1', length=1, delay_cost=1)
	S += T20_t5_mem1 >= 60
	T20_t5_mem1 += MM_MEM[1]

	T22_t0 = S.Task('T22_t0', length=2, delay_cost=1)
	S += T22_t0 >= 60
	T22_t0 += MAS[3]

	T22_t1_in = S.Task('T22_t1_in', length=1, delay_cost=1)
	S += T22_t1_in >= 60
	T22_t1_in += MAS_in[1]

	T22_t1_mem0 = S.Task('T22_t1_mem0', length=1, delay_cost=1)
	S += T22_t1_mem0 >= 60
	T22_t1_mem0 += MAS_MEM[0]

	T22_t1_mem1 = S.Task('T22_t1_mem1', length=1, delay_cost=1)
	S += T22_t1_mem1 >= 60
	T22_t1_mem1 += MAS_MEM[7]

	T23_t3_in = S.Task('T23_t3_in', length=1, delay_cost=1)
	S += T23_t3_in >= 60
	T23_t3_in += MM_in[0]

	T23_t3_mem0 = S.Task('T23_t3_mem0', length=1, delay_cost=1)
	S += T23_t3_mem0 >= 60
	T23_t3_mem0 += MAS_MEM[2]

	T23_t3_mem1 = S.Task('T23_t3_mem1', length=1, delay_cost=1)
	S += T23_t3_mem1 >= 60
	T23_t3_mem1 += MAS_MEM[1]

	T160_in = S.Task('T160_in', length=1, delay_cost=1)
	S += T160_in >= 61
	T160_in += MAS_in[3]

	T160_mem0 = S.Task('T160_mem0', length=1, delay_cost=1)
	S += T160_mem0 >= 61
	T160_mem0 += MM_MEM[0]

	T160_mem1 = S.Task('T160_mem1', length=1, delay_cost=1)
	S += T160_mem1 >= 61
	T160_mem1 += MM_MEM[1]

	T20_t5 = S.Task('T20_t5', length=2, delay_cost=1)
	S += T20_t5 >= 61
	T20_t5 += MAS[0]

	T22_t1 = S.Task('T22_t1', length=2, delay_cost=1)
	S += T22_t1 >= 61
	T22_t1 += MAS[1]

	T22_t3_in = S.Task('T22_t3_in', length=1, delay_cost=1)
	S += T22_t3_in >= 61
	T22_t3_in += MM_in[0]

	T22_t3_mem0 = S.Task('T22_t3_mem0', length=1, delay_cost=1)
	S += T22_t3_mem0 >= 61
	T22_t3_mem0 += MAS_MEM[0]

	T22_t3_mem1 = S.Task('T22_t3_mem1', length=1, delay_cost=1)
	S += T22_t3_mem1 >= 61
	T22_t3_mem1 += MAS_MEM[7]

	T23_t3 = S.Task('T23_t3', length=4, delay_cost=1)
	S += T23_t3 >= 61
	T23_t3 += MM[0]

	T250_in = S.Task('T250_in', length=1, delay_cost=1)
	S += T250_in >= 61
	T250_in += MAS_in[1]

	T250_mem0 = S.Task('T250_mem0', length=1, delay_cost=1)
	S += T250_mem0 >= 61
	T250_mem0 += MAS_MEM[2]

	T250_mem1 = S.Task('T250_mem1', length=1, delay_cost=1)
	S += T250_mem1 >= 61
	T250_mem1 += MAS_MEM[3]

	T160 = S.Task('T160', length=2, delay_cost=1)
	S += T160 >= 62
	T160 += MAS[3]

	T201_in = S.Task('T201_in', length=1, delay_cost=1)
	S += T201_in >= 62
	T201_in += MAS_in[0]

	T201_mem0 = S.Task('T201_mem0', length=1, delay_cost=1)
	S += T201_mem0 >= 62
	T201_mem0 += MM_MEM[0]

	T201_mem1 = S.Task('T201_mem1', length=1, delay_cost=1)
	S += T201_mem1 >= 62
	T201_mem1 += MAS_MEM[1]

	T22_t2_in = S.Task('T22_t2_in', length=1, delay_cost=1)
	S += T22_t2_in >= 62
	T22_t2_in += MM_in[0]

	T22_t2_mem0 = S.Task('T22_t2_mem0', length=1, delay_cost=1)
	S += T22_t2_mem0 >= 62
	T22_t2_mem0 += MAS_MEM[6]

	T22_t2_mem1 = S.Task('T22_t2_mem1', length=1, delay_cost=1)
	S += T22_t2_mem1 >= 62
	T22_t2_mem1 += MAS_MEM[3]

	T22_t3 = S.Task('T22_t3', length=4, delay_cost=1)
	S += T22_t3 >= 62
	T22_t3 += MM[0]

	T250 = S.Task('T250', length=2, delay_cost=1)
	S += T250 >= 62
	T250 += MAS[1]

	T201 = S.Task('T201', length=2, delay_cost=1)
	S += T201 >= 63
	T201 += MAS[0]

	T22_t2 = S.Task('T22_t2', length=4, delay_cost=1)
	S += T22_t2 >= 63
	T22_t2 += MM[0]

	T241_in = S.Task('T241_in', length=1, delay_cost=1)
	S += T241_in >= 63
	T241_in += MAS_in[2]

	T241_mem0 = S.Task('T241_mem0', length=1, delay_cost=1)
	S += T241_mem0 >= 63
	T241_mem0 += MM_MEM[0]

	T241_mem1 = S.Task('T241_mem1', length=1, delay_cost=1)
	S += T241_mem1 >= 63
	T241_mem1 += MAS_MEM[1]

	Z3_t1_in = S.Task('Z3_t1_in', length=1, delay_cost=1)
	S += Z3_t1_in >= 63
	Z3_t1_in += MM_in[0]

	Z3_t1_mem0 = S.Task('Z3_t1_mem0', length=1, delay_cost=1)
	S += Z3_t1_mem0 >= 63
	Z3_t1_mem0 += MAIN_MEM_r[0]

	Z3_t1_mem1 = S.Task('Z3_t1_mem1', length=1, delay_cost=1)
	S += Z3_t1_mem1 >= 63
	Z3_t1_mem1 += MAS_MEM[7]

	Z40_in = S.Task('Z40_in', length=1, delay_cost=1)
	S += Z40_in >= 63
	Z40_in += MAS_in[3]

	Z40_mem0 = S.Task('Z40_mem0', length=1, delay_cost=1)
	S += Z40_mem0 >= 63
	Z40_mem0 += MAS_MEM[6]

	Z40_mem1 = S.Task('Z40_mem1', length=1, delay_cost=1)
	S += Z40_mem1 >= 63
	Z40_mem1 += MAS_MEM[3]

	T161_in = S.Task('T161_in', length=1, delay_cost=1)
	S += T161_in >= 64
	T161_in += MAS_in[0]

	T161_mem0 = S.Task('T161_mem0', length=1, delay_cost=1)
	S += T161_mem0 >= 64
	T161_mem0 += MM_MEM[0]

	T161_mem1 = S.Task('T161_mem1', length=1, delay_cost=1)
	S += T161_mem1 >= 64
	T161_mem1 += MAS_MEM[7]

	T23_t2_in = S.Task('T23_t2_in', length=1, delay_cost=1)
	S += T23_t2_in >= 64
	T23_t2_in += MM_in[0]

	T23_t2_mem0 = S.Task('T23_t2_mem0', length=1, delay_cost=1)
	S += T23_t2_mem0 >= 64
	T23_t2_mem0 += MAS_MEM[2]

	T23_t2_mem1 = S.Task('T23_t2_mem1', length=1, delay_cost=1)
	S += T23_t2_mem1 >= 64
	T23_t2_mem1 += MAS_MEM[3]

	T241 = S.Task('T241', length=2, delay_cost=1)
	S += T241 >= 64
	T241 += MAS[2]

	Z3_t1 = S.Task('Z3_t1', length=4, delay_cost=1)
	S += Z3_t1 >= 64
	Z3_t1 += MM[0]

	Z40 = S.Task('Z40', length=2, delay_cost=1)
	S += Z40 >= 64
	Z40 += MAS[3]

	T161 = S.Task('T161', length=2, delay_cost=1)
	S += T161 >= 65
	T161 += MAS[0]

	T221_in = S.Task('T221_in', length=1, delay_cost=1)
	S += T221_in >= 65
	T221_in += MAS_in[0]

	T221_mem0 = S.Task('T221_mem0', length=1, delay_cost=1)
	S += T221_mem0 >= 65
	T221_mem0 += MM_MEM[0]

	T221_mem1 = S.Task('T221_mem1', length=1, delay_cost=1)
	S += T221_mem1 >= 65
	T221_mem1 += MM_MEM[1]

	T23_t2 = S.Task('T23_t2', length=4, delay_cost=1)
	S += T23_t2 >= 65
	T23_t2 += MM[0]

	Z3_t4_in = S.Task('Z3_t4_in', length=1, delay_cost=1)
	S += Z3_t4_in >= 65
	Z3_t4_in += MM_in[0]

	Z3_t4_mem0 = S.Task('Z3_t4_mem0', length=1, delay_cost=1)
	S += Z3_t4_mem0 >= 65
	Z3_t4_mem0 += MAS_MEM[4]

	Z3_t4_mem1 = S.Task('Z3_t4_mem1', length=1, delay_cost=1)
	S += Z3_t4_mem1 >= 65
	Z3_t4_mem1 += MAS_MEM[5]

	T221 = S.Task('T221', length=2, delay_cost=1)
	S += T221 >= 66
	T221 += MAS[0]

	T23_t5_in = S.Task('T23_t5_in', length=1, delay_cost=1)
	S += T23_t5_in >= 66
	T23_t5_in += MAS_in[0]

	T23_t5_mem0 = S.Task('T23_t5_mem0', length=1, delay_cost=1)
	S += T23_t5_mem0 >= 66
	T23_t5_mem0 += MM_MEM[0]

	T23_t5_mem1 = S.Task('T23_t5_mem1', length=1, delay_cost=1)
	S += T23_t5_mem1 >= 66
	T23_t5_mem1 += MM_MEM[1]

	Z3_t4 = S.Task('Z3_t4', length=4, delay_cost=1)
	S += Z3_t4 >= 66
	Z3_t4 += MM[0]

	Z40_w = S.Task('Z40_w', length=1, delay_cost=1)
	S += Z40_w >= 66
	Z40_w += MAIN_MEM_w

	T170_in = S.Task('T170_in', length=1, delay_cost=1)
	S += T170_in >= 67
	T170_in += MAS_in[1]

	T170_mem0 = S.Task('T170_mem0', length=1, delay_cost=1)
	S += T170_mem0 >= 67
	T170_mem0 += MM_MEM[0]

	T170_mem1 = S.Task('T170_mem1', length=1, delay_cost=1)
	S += T170_mem1 >= 67
	T170_mem1 += MM_MEM[1]

	T23_t5 = S.Task('T23_t5', length=2, delay_cost=1)
	S += T23_t5 >= 67
	T23_t5 += MAS[0]

	X31_in = S.Task('X31_in', length=1, delay_cost=1)
	S += X31_in >= 67
	X31_in += MAS_in[3]

	X31_mem0 = S.Task('X31_mem0', length=1, delay_cost=1)
	S += X31_mem0 >= 67
	X31_mem0 += MAS_MEM[0]

	X31_mem1 = S.Task('X31_mem1', length=1, delay_cost=1)
	S += X31_mem1 >= 67
	X31_mem1 += MAS_MEM[5]

	T170 = S.Task('T170', length=2, delay_cost=1)
	S += T170 >= 68
	T170 += MAS[1]

	T230_in = S.Task('T230_in', length=1, delay_cost=1)
	S += T230_in >= 68
	T230_in += MAS_in[0]

	T230_mem0 = S.Task('T230_mem0', length=1, delay_cost=1)
	S += T230_mem0 >= 68
	T230_mem0 += MM_MEM[0]

	T230_mem1 = S.Task('T230_mem1', length=1, delay_cost=1)
	S += T230_mem1 >= 68
	T230_mem1 += MAS_MEM[1]

	X31 = S.Task('X31', length=2, delay_cost=1)
	S += X31 >= 68
	X31 += MAS[3]

	T17_t5_in = S.Task('T17_t5_in', length=1, delay_cost=1)
	S += T17_t5_in >= 69
	T17_t5_in += MAS_in[3]

	T17_t5_mem0 = S.Task('T17_t5_mem0', length=1, delay_cost=1)
	S += T17_t5_mem0 >= 69
	T17_t5_mem0 += MM_MEM[0]

	T17_t5_mem1 = S.Task('T17_t5_mem1', length=1, delay_cost=1)
	S += T17_t5_mem1 >= 69
	T17_t5_mem1 += MM_MEM[1]

	T230 = S.Task('T230', length=2, delay_cost=1)
	S += T230 >= 69
	T230 += MAS[0]

	T17_t5 = S.Task('T17_t5', length=2, delay_cost=1)
	S += T17_t5 >= 70
	T17_t5 += MAS[3]

	T231_in = S.Task('T231_in', length=1, delay_cost=1)
	S += T231_in >= 70
	T231_in += MAS_in[0]

	T231_mem0 = S.Task('T231_mem0', length=1, delay_cost=1)
	S += T231_mem0 >= 70
	T231_mem0 += MM_MEM[0]

	T231_mem1 = S.Task('T231_mem1', length=1, delay_cost=1)
	S += T231_mem1 >= 70
	T231_mem1 += MM_MEM[1]

	X31_w = S.Task('X31_w', length=1, delay_cost=1)
	S += X31_w >= 70
	X31_w += MAIN_MEM_w

	X40_in = S.Task('X40_in', length=1, delay_cost=1)
	S += X40_in >= 70
	X40_in += MAS_in[3]

	X40_mem0 = S.Task('X40_mem0', length=1, delay_cost=1)
	S += X40_mem0 >= 70
	X40_mem0 += MAS_MEM[0]

	X40_mem1 = S.Task('X40_mem1', length=1, delay_cost=1)
	S += X40_mem1 >= 70
	X40_mem1 += MAS_MEM[3]

	T171_in = S.Task('T171_in', length=1, delay_cost=1)
	S += T171_in >= 71
	T171_in += MAS_in[1]

	T171_mem0 = S.Task('T171_mem0', length=1, delay_cost=1)
	S += T171_mem0 >= 71
	T171_mem0 += MM_MEM[0]

	T171_mem1 = S.Task('T171_mem1', length=1, delay_cost=1)
	S += T171_mem1 >= 71
	T171_mem1 += MAS_MEM[7]

	T231 = S.Task('T231', length=2, delay_cost=1)
	S += T231 >= 71
	T231 += MAS[0]

	X40 = S.Task('X40', length=2, delay_cost=1)
	S += X40 >= 71
	X40 += MAS[3]

	T171 = S.Task('T171', length=2, delay_cost=1)
	S += T171 >= 72
	T171 += MAS[1]

	T22_t5_in = S.Task('T22_t5_in', length=1, delay_cost=1)
	S += T22_t5_in >= 72
	T22_t5_in += MAS_in[0]

	T22_t5_mem0 = S.Task('T22_t5_mem0', length=1, delay_cost=1)
	S += T22_t5_mem0 >= 72
	T22_t5_mem0 += MM_MEM[0]

	T22_t5_mem1 = S.Task('T22_t5_mem1', length=1, delay_cost=1)
	S += T22_t5_mem1 >= 72
	T22_t5_mem1 += MM_MEM[1]

	T22_t5 = S.Task('T22_t5', length=2, delay_cost=1)
	S += T22_t5 >= 73
	T22_t5 += MAS[0]

	T240_in = S.Task('T240_in', length=1, delay_cost=1)
	S += T240_in >= 73
	T240_in += MAS_in[0]

	T240_mem0 = S.Task('T240_mem0', length=1, delay_cost=1)
	S += T240_mem0 >= 73
	T240_mem0 += MM_MEM[0]

	T240_mem1 = S.Task('T240_mem1', length=1, delay_cost=1)
	S += T240_mem1 >= 73
	T240_mem1 += MM_MEM[1]

	X40_w = S.Task('X40_w', length=1, delay_cost=1)
	S += X40_w >= 73
	X40_w += MAIN_MEM_w

	X41_in = S.Task('X41_in', length=1, delay_cost=1)
	S += X41_in >= 73
	X41_in += MAS_in[1]

	X41_mem0 = S.Task('X41_mem0', length=1, delay_cost=1)
	S += X41_mem0 >= 73
	X41_mem0 += MAS_MEM[0]

	X41_mem1 = S.Task('X41_mem1', length=1, delay_cost=1)
	S += X41_mem1 >= 73
	X41_mem1 += MAS_MEM[3]

	T220_in = S.Task('T220_in', length=1, delay_cost=1)
	S += T220_in >= 74
	T220_in += MAS_in[2]

	T220_mem0 = S.Task('T220_mem0', length=1, delay_cost=1)
	S += T220_mem0 >= 74
	T220_mem0 += MM_MEM[0]

	T220_mem1 = S.Task('T220_mem1', length=1, delay_cost=1)
	S += T220_mem1 >= 74
	T220_mem1 += MAS_MEM[1]

	T240 = S.Task('T240', length=2, delay_cost=1)
	S += T240 >= 74
	T240 += MAS[0]

	X41 = S.Task('X41', length=2, delay_cost=1)
	S += X41 >= 74
	X41 += MAS[1]

	T220 = S.Task('T220', length=2, delay_cost=1)
	S += T220 >= 75
	T220 += MAS[2]

	Z30_in = S.Task('Z30_in', length=1, delay_cost=1)
	S += Z30_in >= 75
	Z30_in += MAS_in[0]

	Z30_mem0 = S.Task('Z30_mem0', length=1, delay_cost=1)
	S += Z30_mem0 >= 75
	Z30_mem0 += MM_MEM[0]

	Z30_mem1 = S.Task('Z30_mem1', length=1, delay_cost=1)
	S += Z30_mem1 >= 75
	Z30_mem1 += MM_MEM[1]

	X30_in = S.Task('X30_in', length=1, delay_cost=1)
	S += X30_in >= 76
	X30_in += MAS_in[2]

	X30_mem0 = S.Task('X30_mem0', length=1, delay_cost=1)
	S += X30_mem0 >= 76
	X30_mem0 += MAS_MEM[4]

	X30_mem1 = S.Task('X30_mem1', length=1, delay_cost=1)
	S += X30_mem1 >= 76
	X30_mem1 += MAS_MEM[1]

	X41_w = S.Task('X41_w', length=1, delay_cost=1)
	S += X41_w >= 76
	X41_w += MAIN_MEM_w

	Z30 = S.Task('Z30', length=2, delay_cost=1)
	S += Z30 >= 76
	Z30 += MAS[0]

	Z3_t5_in = S.Task('Z3_t5_in', length=1, delay_cost=1)
	S += Z3_t5_in >= 76
	Z3_t5_in += MAS_in[1]

	Z3_t5_mem0 = S.Task('Z3_t5_mem0', length=1, delay_cost=1)
	S += Z3_t5_mem0 >= 76
	Z3_t5_mem0 += MM_MEM[0]

	Z3_t5_mem1 = S.Task('Z3_t5_mem1', length=1, delay_cost=1)
	S += Z3_t5_mem1 >= 76
	Z3_t5_mem1 += MM_MEM[1]

	X30 = S.Task('X30', length=2, delay_cost=1)
	S += X30 >= 77
	X30 += MAS[2]

	Z3_t5 = S.Task('Z3_t5', length=2, delay_cost=1)
	S += Z3_t5 >= 77
	Z3_t5 += MAS[1]

	Z30_w = S.Task('Z30_w', length=1, delay_cost=1)
	S += Z30_w >= 78
	Z30_w += MAIN_MEM_w

	Z31_in = S.Task('Z31_in', length=1, delay_cost=1)
	S += Z31_in >= 78
	Z31_in += MAS_in[0]

	Z31_mem0 = S.Task('Z31_mem0', length=1, delay_cost=1)
	S += Z31_mem0 >= 78
	Z31_mem0 += MM_MEM[0]

	Z31_mem1 = S.Task('Z31_mem1', length=1, delay_cost=1)
	S += Z31_mem1 >= 78
	Z31_mem1 += MAS_MEM[3]

	X30_w = S.Task('X30_w', length=1, delay_cost=1)
	S += X30_w >= 79
	X30_w += MAIN_MEM_w

	Z31 = S.Task('Z31', length=2, delay_cost=1)
	S += Z31 >= 79
	Z31 += MAS[0]

	Z31_w = S.Task('Z31_w', length=1, delay_cost=1)
	S += Z31_w >= 81
	Z31_w += MAIN_MEM_w


	# new tasks
	T251 = S.Task('T251', length=2, delay_cost=1)
	T251 += alt(MAS)
	T251_in = S.Task('T251_in', length=1, delay_cost=1)
	T251_in += alt(MAS_in)
	S += T251_in*MAS_in[0]<=T251*MAS[0]

	S += T251_in*MAS_in[1]<=T251*MAS[1]

	S += T251_in*MAS_in[2]<=T251*MAS[2]

	S += T251_in*MAS_in[3]<=T251*MAS[3]

	S += T251<67

	T251_mem0 = S.Task('T251_mem0', length=1, delay_cost=1)
	T251_mem0 += MAS_MEM[0]
	S += 64 < T251_mem0
	S += T251_mem0 <= T251

	T251_mem1 = S.Task('T251_mem1', length=1, delay_cost=1)
	T251_mem1 += MAS_MEM[1]
	S += 64 < T251_mem1
	S += T251_mem1 <= T251

	Z41 = S.Task('Z41', length=2, delay_cost=1)
	Z41 += alt(MAS)
	Z41_in = S.Task('Z41_in', length=1, delay_cost=1)
	Z41_in += alt(MAS_in)
	S += Z41_in*MAS_in[0]<=Z41*MAS[0]

	S += Z41_in*MAS_in[1]<=Z41*MAS[1]

	S += Z41_in*MAS_in[2]<=Z41*MAS[2]

	S += Z41_in*MAS_in[3]<=Z41*MAS[3]

	S += 0<Z41

	Z41_w = S.Task('Z41_w', length=1, delay_cost=1)
	Z41_w += alt(MAIN_MEM_w)
	S += Z41 <= Z41_w

	S += Z41<1000

	Z41_mem0 = S.Task('Z41_mem0', length=1, delay_cost=1)
	Z41_mem0 += MAS_MEM[0]
	S += 66 < Z41_mem0
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

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage2MAS4/EP2_LADDERMUL/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

