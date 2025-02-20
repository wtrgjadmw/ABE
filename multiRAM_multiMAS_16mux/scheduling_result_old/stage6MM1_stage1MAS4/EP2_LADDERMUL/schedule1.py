from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	S += T1_t3_in >= 0
	T1_t3_in += MM_in[0]

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	S += T6_t1_mem0 >= 0
	T6_t1_mem0 += MAIN_MEM_r[0]

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	S += T7_t2_mem1 >= 0
	T7_t2_mem1 += MAIN_MEM_r[1]

	T10_t2 = S.Task('T10_t2', length=1, delay_cost=1)
	S += T10_t2 >= 1
	T10_t2 += MAS[0]

	T1_t1 = S.Task('T1_t1', length=1, delay_cost=1)
	S += T1_t1 >= 1
	T1_t1 += MAS[3]

	T1_t3 = S.Task('T1_t3', length=6, delay_cost=1)
	S += T1_t3 >= 1
	T1_t3 += MM[0]

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	S += T2_t0_mem1 >= 1
	T2_t0_mem1 += MAIN_MEM_r[1]

	T2_t3 = S.Task('T2_t3', length=1, delay_cost=1)
	S += T2_t3 >= 1
	T2_t3 += MAS[1]

	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	S += T4_t1_in >= 1
	T4_t1_in += MM_in[0]

	T6_t2 = S.Task('T6_t2', length=1, delay_cost=1)
	S += T6_t2 >= 1
	T6_t2 += MAS[2]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	S += T6_t2_mem0 >= 1
	T6_t2_mem0 += MAIN_MEM_r[0]

	T2_t2 = S.Task('T2_t2', length=1, delay_cost=1)
	S += T2_t2 >= 2
	T2_t2 += MAS[1]

	T3_t2 = S.Task('T3_t2', length=1, delay_cost=1)
	S += T3_t2 >= 2
	T3_t2 += MAS[2]

	T4_t1 = S.Task('T4_t1', length=6, delay_cost=1)
	S += T4_t1 >= 2
	T4_t1 += MM[0]

	T5_t0 = S.Task('T5_t0', length=1, delay_cost=1)
	S += T5_t0 >= 2
	T5_t0 += MAS[3]

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	S += T5_t0_mem1 >= 2
	T5_t0_mem1 += MAIN_MEM_r[1]

	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	S += T6_t0_in >= 2
	T6_t0_in += MM_in[0]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	S += T7_t2_mem0 >= 2
	T7_t2_mem0 += MAIN_MEM_r[0]

	T9_t2 = S.Task('T9_t2', length=1, delay_cost=1)
	S += T9_t2 >= 2
	T9_t2 += MAS[0]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	S += T11_t2_mem0 >= 3
	T11_t2_mem0 += MAIN_MEM_r[0]

	T1_t0 = S.Task('T1_t0', length=1, delay_cost=1)
	S += T1_t0 >= 3
	T1_t0 += MAS[3]

	T3_t3 = S.Task('T3_t3', length=1, delay_cost=1)
	S += T3_t3 >= 3
	T3_t3 += MAS[2]

	T6_t0 = S.Task('T6_t0', length=6, delay_cost=1)
	S += T6_t0 >= 3
	T6_t0 += MM[0]

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	S += T6_t3_mem1 >= 3
	T6_t3_mem1 += MAIN_MEM_r[1]

	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	S += T7_t0_in >= 3
	T7_t0_in += MM_in[0]

	T7_t2 = S.Task('T7_t2', length=1, delay_cost=1)
	S += T7_t2 >= 3
	T7_t2 += MAS[0]

	T7_t3 = S.Task('T7_t3', length=1, delay_cost=1)
	S += T7_t3 >= 3
	T7_t3 += MAS[1]

	T11_t2 = S.Task('T11_t2', length=1, delay_cost=1)
	S += T11_t2 >= 4
	T11_t2 += MAS[0]

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	S += T1_t1_mem1 >= 4
	T1_t1_mem1 += MAIN_MEM_r[1]

	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	S += T2_t1_in >= 4
	T2_t1_in += MM_in[0]

	T4_t2 = S.Task('T4_t2', length=1, delay_cost=1)
	S += T4_t2 >= 4
	T4_t2 += MAS[3]

	T5_t1 = S.Task('T5_t1', length=1, delay_cost=1)
	S += T5_t1 >= 4
	T5_t1 += MAS[2]

	T6_t3 = S.Task('T6_t3', length=1, delay_cost=1)
	S += T6_t3 >= 4
	T6_t3 += MAS[1]

	T7_t0 = S.Task('T7_t0', length=6, delay_cost=1)
	S += T7_t0 >= 4
	T7_t0 += MM[0]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	S += T7_t3_mem0 >= 4
	T7_t3_mem0 += MAIN_MEM_r[0]

	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	S += T2_t0_in >= 5
	T2_t0_in += MM_in[0]

	T2_t1 = S.Task('T2_t1', length=6, delay_cost=1)
	S += T2_t1 >= 5
	T2_t1 += MM[0]

	T4_t3 = S.Task('T4_t3', length=1, delay_cost=1)
	S += T4_t3 >= 5
	T4_t3 += MAS[0]

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	S += T5_t3_mem0 >= 5
	T5_t3_mem0 += MAIN_MEM_r[0]

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	S += T7_t1_mem1 >= 5
	T7_t1_mem1 += MAIN_MEM_r[1]

	T8_t2 = S.Task('T8_t2', length=1, delay_cost=1)
	S += T8_t2 >= 5
	T8_t2 += MAS[1]

	T2_t0 = S.Task('T2_t0', length=6, delay_cost=1)
	S += T2_t0 >= 6
	T2_t0 += MM[0]

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	S += T2_t0_mem0 >= 6
	T2_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	S += T3_t0_in >= 6
	T3_t0_in += MM_in[0]

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	S += T6_t2_mem1 >= 6
	T6_t2_mem1 += MAIN_MEM_r[1]

	T3_t0 = S.Task('T3_t0', length=6, delay_cost=1)
	S += T3_t0 >= 7
	T3_t0 += MM[0]

	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	S += T5_t3_in >= 7
	T5_t3_in += MM_in[0]

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	S += T6_t1_mem1 >= 7
	T6_t1_mem1 += MAIN_MEM_r[1]

	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	S += T7_t0_mem0 >= 7
	T7_t0_mem0 += MAIN_MEM_r[0]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	S += T1_t0_mem0 >= 8
	T1_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	S += T4_t0_in >= 8
	T4_t0_in += MM_in[0]

	T5_t3 = S.Task('T5_t3', length=6, delay_cost=1)
	S += T5_t3 >= 8
	T5_t3 += MM[0]

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	S += T7_t3_mem1 >= 8
	T7_t3_mem1 += MAIN_MEM_r[1]

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	S += T2_t2_mem1 >= 9
	T2_t2_mem1 += MAIN_MEM_r[1]

	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	S += T3_t1_in >= 9
	T3_t1_in += MM_in[0]

	T4_t0 = S.Task('T4_t0', length=6, delay_cost=1)
	S += T4_t0 >= 9
	T4_t0 += MM[0]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	S += T8_t2_mem0 >= 9
	T8_t2_mem0 += MAIN_MEM_r[0]

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	S += T1_t3_mem0 >= 10
	T1_t3_mem0 += MAIN_MEM_r[0]

	T3_t1 = S.Task('T3_t1', length=6, delay_cost=1)
	S += T3_t1 >= 10
	T3_t1 += MM[0]

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	S += T3_t3_mem1 >= 10
	T3_t3_mem1 += MAIN_MEM_r[1]

	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	S += T6_t1_in >= 10
	T6_t1_in += MM_in[0]

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	S += T4_t3_mem1 >= 11
	T4_t3_mem1 += MAIN_MEM_r[1]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	S += T5_t1_mem0 >= 11
	T5_t1_mem0 += MAIN_MEM_r[0]

	T6_t1 = S.Task('T6_t1', length=6, delay_cost=1)
	S += T6_t1 >= 11
	T6_t1 += MM[0]

	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	S += T7_t1_in >= 11
	T7_t1_in += MM_in[0]

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	S += T1_t0_mem1 >= 12
	T1_t0_mem1 += MAIN_MEM_r[1]

	T7_t1 = S.Task('T7_t1', length=6, delay_cost=1)
	S += T7_t1 >= 12
	T7_t1 += MM[0]

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	S += T7_t1_mem0 >= 12
	T7_t1_mem0 += MAIN_MEM_r[0]

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	S += T2_t1_mem0 >= 13
	T2_t1_mem0 += MAIN_MEM_r[0]

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	S += T4_t2_mem1 >= 13
	T4_t2_mem1 += MAIN_MEM_r[1]

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	S += T10_t2_mem1 >= 14
	T10_t2_mem1 += MAIN_MEM_r[1]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	S += T9_t2_mem0 >= 14
	T9_t2_mem0 += MAIN_MEM_r[0]

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	S += T1_t3_mem1 >= 15
	T1_t3_mem1 += MAIN_MEM_r[1]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	S += T2_t2_mem0 >= 15
	T2_t2_mem0 += MAIN_MEM_r[0]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	S += T10_t2_mem0 >= 16
	T10_t2_mem0 += MAIN_MEM_r[0]

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	S += T6_t0_mem1 >= 16
	T6_t0_mem1 += MAIN_MEM_r[1]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	S += T5_t0_mem0 >= 17
	T5_t0_mem0 += MAIN_MEM_r[0]

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	S += T9_t2_mem1 >= 17
	T9_t2_mem1 += MAIN_MEM_r[1]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	S += T6_t3_mem0 >= 18
	T6_t3_mem0 += MAIN_MEM_r[0]

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	S += T7_t0_mem1 >= 18
	T7_t0_mem1 += MAIN_MEM_r[1]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	S += T4_t3_mem0 >= 19
	T4_t3_mem0 += MAIN_MEM_r[0]

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	S += T5_t3_mem1 >= 19
	T5_t3_mem1 += MAIN_MEM_r[1]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	S += T1_t1_mem0 >= 20
	T1_t1_mem0 += MAIN_MEM_r[0]

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	S += T4_t1_mem1 >= 20
	T4_t1_mem1 += MAIN_MEM_r[1]

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	S += T3_t3_mem0 >= 21
	T3_t3_mem0 += MAIN_MEM_r[0]

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	S += T8_t2_mem1 >= 21
	T8_t2_mem1 += MAIN_MEM_r[1]

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	S += T3_t1_mem1 >= 22
	T3_t1_mem1 += MAIN_MEM_r[1]

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	S += T6_t0_mem0 >= 22
	T6_t0_mem0 += MAIN_MEM_r[0]

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	S += T11_t2_mem1 >= 23
	T11_t2_mem1 += MAIN_MEM_r[1]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	S += T4_t2_mem0 >= 23
	T4_t2_mem0 += MAIN_MEM_r[0]

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	S += T4_t0_mem0 >= 24
	T4_t0_mem0 += MAIN_MEM_r[0]

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	S += T4_t0_mem1 >= 24
	T4_t0_mem1 += MAIN_MEM_r[1]

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	S += T2_t1_mem1 >= 25
	T2_t1_mem1 += MAIN_MEM_r[1]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	S += T3_t2_mem0 >= 25
	T3_t2_mem0 += MAIN_MEM_r[0]

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	S += T2_t3_mem1 >= 26
	T2_t3_mem1 += MAIN_MEM_r[1]

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	S += T4_t1_mem0 >= 26
	T4_t1_mem0 += MAIN_MEM_r[0]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	S += T2_t3_mem0 >= 27
	T2_t3_mem0 += MAIN_MEM_r[0]

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	S += T5_t1_mem1 >= 27
	T5_t1_mem1 += MAIN_MEM_r[1]

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	S += T3_t0_mem0 >= 28
	T3_t0_mem0 += MAIN_MEM_r[0]

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	S += T3_t0_mem1 >= 28
	T3_t0_mem1 += MAIN_MEM_r[1]

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	S += T3_t1_mem0 >= 29
	T3_t1_mem0 += MAIN_MEM_r[0]

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	S += T3_t2_mem1 >= 29
	T3_t2_mem1 += MAIN_MEM_r[1]


	# new tasks
	Z3_t2 = S.Task('Z3_t2', length=1, delay_cost=1)
	Z3_t2 += alt(MAS)

	Z3_t2_mem0 = S.Task('Z3_t2_mem0', length=1, delay_cost=1)
	Z3_t2_mem0 += MAIN_MEM_r[0]
	Z3_t2_mem1 = S.Task('Z3_t2_mem1', length=1, delay_cost=1)
	Z3_t2_mem1 += MAIN_MEM_r[1]
	T1_t2_in = S.Task('T1_t2_in', length=1, delay_cost=1)
	T1_t2_in += alt(MM_in)
	T1_t2 = S.Task('T1_t2', length=6, delay_cost=1)
	T1_t2 += alt(MM)
	S += T1_t2>=T1_t2_in

	T1_t2_mem0 = S.Task('T1_t2_mem0', length=1, delay_cost=1)
	T1_t2_mem0 += MAS_MEM[6]
	S += 3 < T1_t2_mem0
	S += T1_t2_mem0 <= T1_t2

	T1_t2_mem1 = S.Task('T1_t2_mem1', length=1, delay_cost=1)
	T1_t2_mem1 += MAS_MEM[7]
	S += 1 < T1_t2_mem1
	S += T1_t2_mem1 <= T1_t2

	T1_t5 = S.Task('T1_t5', length=1, delay_cost=1)
	T1_t5 += alt(MAS)

	T1_t5_mem0 = S.Task('T1_t5_mem0', length=1, delay_cost=1)
	T1_t5_mem0 += MM_MEM[0]
	S += 6 < T1_t5_mem0
	S += T1_t5_mem0 <= T1_t5

	T11 = S.Task('T11', length=1, delay_cost=1)
	T11 += alt(MAS)

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += MM_MEM[0]
	S += 6 < T11_mem0
	S += T11_mem0 <= T11

	T2_t4_in = S.Task('T2_t4_in', length=1, delay_cost=1)
	T2_t4_in += alt(MM_in)
	T2_t4 = S.Task('T2_t4', length=6, delay_cost=1)
	T2_t4 += alt(MM)
	S += T2_t4>=T2_t4_in

	T2_t4_mem0 = S.Task('T2_t4_mem0', length=1, delay_cost=1)
	T2_t4_mem0 += MAS_MEM[2]
	S += 2 < T2_t4_mem0
	S += T2_t4_mem0 <= T2_t4

	T2_t4_mem1 = S.Task('T2_t4_mem1', length=1, delay_cost=1)
	T2_t4_mem1 += MAS_MEM[3]
	S += 1 < T2_t4_mem1
	S += T2_t4_mem1 <= T2_t4

	T20 = S.Task('T20', length=1, delay_cost=1)
	T20 += alt(MAS)

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += MM_MEM[0]
	S += 11 < T20_mem0
	S += T20_mem0 <= T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += MM_MEM[1]
	S += 10 < T20_mem1
	S += T20_mem1 <= T20

	T2_t5 = S.Task('T2_t5', length=1, delay_cost=1)
	T2_t5 += alt(MAS)

	T2_t5_mem0 = S.Task('T2_t5_mem0', length=1, delay_cost=1)
	T2_t5_mem0 += MM_MEM[0]
	S += 11 < T2_t5_mem0
	S += T2_t5_mem0 <= T2_t5

	T2_t5_mem1 = S.Task('T2_t5_mem1', length=1, delay_cost=1)
	T2_t5_mem1 += MM_MEM[1]
	S += 10 < T2_t5_mem1
	S += T2_t5_mem1 <= T2_t5

	T3_t4_in = S.Task('T3_t4_in', length=1, delay_cost=1)
	T3_t4_in += alt(MM_in)
	T3_t4 = S.Task('T3_t4', length=6, delay_cost=1)
	T3_t4 += alt(MM)
	S += T3_t4>=T3_t4_in

	T3_t4_mem0 = S.Task('T3_t4_mem0', length=1, delay_cost=1)
	T3_t4_mem0 += MAS_MEM[4]
	S += 2 < T3_t4_mem0
	S += T3_t4_mem0 <= T3_t4

	T3_t4_mem1 = S.Task('T3_t4_mem1', length=1, delay_cost=1)
	T3_t4_mem1 += MAS_MEM[5]
	S += 3 < T3_t4_mem1
	S += T3_t4_mem1 <= T3_t4

	T30 = S.Task('T30', length=1, delay_cost=1)
	T30 += alt(MAS)

	T30_mem0 = S.Task('T30_mem0', length=1, delay_cost=1)
	T30_mem0 += MM_MEM[0]
	S += 12 < T30_mem0
	S += T30_mem0 <= T30

	T30_mem1 = S.Task('T30_mem1', length=1, delay_cost=1)
	T30_mem1 += MM_MEM[1]
	S += 15 < T30_mem1
	S += T30_mem1 <= T30

	T3_t5 = S.Task('T3_t5', length=1, delay_cost=1)
	T3_t5 += alt(MAS)

	T3_t5_mem0 = S.Task('T3_t5_mem0', length=1, delay_cost=1)
	T3_t5_mem0 += MM_MEM[0]
	S += 12 < T3_t5_mem0
	S += T3_t5_mem0 <= T3_t5

	T3_t5_mem1 = S.Task('T3_t5_mem1', length=1, delay_cost=1)
	T3_t5_mem1 += MM_MEM[1]
	S += 15 < T3_t5_mem1
	S += T3_t5_mem1 <= T3_t5

	T4_t4_in = S.Task('T4_t4_in', length=1, delay_cost=1)
	T4_t4_in += alt(MM_in)
	T4_t4 = S.Task('T4_t4', length=6, delay_cost=1)
	T4_t4 += alt(MM)
	S += T4_t4>=T4_t4_in

	T4_t4_mem0 = S.Task('T4_t4_mem0', length=1, delay_cost=1)
	T4_t4_mem0 += MAS_MEM[6]
	S += 4 < T4_t4_mem0
	S += T4_t4_mem0 <= T4_t4

	T4_t4_mem1 = S.Task('T4_t4_mem1', length=1, delay_cost=1)
	T4_t4_mem1 += MAS_MEM[1]
	S += 5 < T4_t4_mem1
	S += T4_t4_mem1 <= T4_t4

	T40 = S.Task('T40', length=1, delay_cost=1)
	T40 += alt(MAS)

	T40_mem0 = S.Task('T40_mem0', length=1, delay_cost=1)
	T40_mem0 += MM_MEM[0]
	S += 14 < T40_mem0
	S += T40_mem0 <= T40

	T40_mem1 = S.Task('T40_mem1', length=1, delay_cost=1)
	T40_mem1 += MM_MEM[1]
	S += 7 < T40_mem1
	S += T40_mem1 <= T40

	T4_t5 = S.Task('T4_t5', length=1, delay_cost=1)
	T4_t5 += alt(MAS)

	T4_t5_mem0 = S.Task('T4_t5_mem0', length=1, delay_cost=1)
	T4_t5_mem0 += MM_MEM[0]
	S += 14 < T4_t5_mem0
	S += T4_t5_mem0 <= T4_t5

	T4_t5_mem1 = S.Task('T4_t5_mem1', length=1, delay_cost=1)
	T4_t5_mem1 += MM_MEM[1]
	S += 7 < T4_t5_mem1
	S += T4_t5_mem1 <= T4_t5

	T5_t2_in = S.Task('T5_t2_in', length=1, delay_cost=1)
	T5_t2_in += alt(MM_in)
	T5_t2 = S.Task('T5_t2', length=6, delay_cost=1)
	T5_t2 += alt(MM)
	S += T5_t2>=T5_t2_in

	T5_t2_mem0 = S.Task('T5_t2_mem0', length=1, delay_cost=1)
	T5_t2_mem0 += MAS_MEM[6]
	S += 2 < T5_t2_mem0
	S += T5_t2_mem0 <= T5_t2

	T5_t2_mem1 = S.Task('T5_t2_mem1', length=1, delay_cost=1)
	T5_t2_mem1 += MAS_MEM[5]
	S += 4 < T5_t2_mem1
	S += T5_t2_mem1 <= T5_t2

	T5_t5 = S.Task('T5_t5', length=1, delay_cost=1)
	T5_t5 += alt(MAS)

	T5_t5_mem0 = S.Task('T5_t5_mem0', length=1, delay_cost=1)
	T5_t5_mem0 += MM_MEM[0]
	S += 13 < T5_t5_mem0
	S += T5_t5_mem0 <= T5_t5

	T51 = S.Task('T51', length=1, delay_cost=1)
	T51 += alt(MAS)

	T51_mem0 = S.Task('T51_mem0', length=1, delay_cost=1)
	T51_mem0 += MM_MEM[0]
	S += 13 < T51_mem0
	S += T51_mem0 <= T51

	T6_t4_in = S.Task('T6_t4_in', length=1, delay_cost=1)
	T6_t4_in += alt(MM_in)
	T6_t4 = S.Task('T6_t4', length=6, delay_cost=1)
	T6_t4 += alt(MM)
	S += T6_t4>=T6_t4_in

	T6_t4_mem0 = S.Task('T6_t4_mem0', length=1, delay_cost=1)
	T6_t4_mem0 += MAS_MEM[4]
	S += 1 < T6_t4_mem0
	S += T6_t4_mem0 <= T6_t4

	T6_t4_mem1 = S.Task('T6_t4_mem1', length=1, delay_cost=1)
	T6_t4_mem1 += MAS_MEM[3]
	S += 4 < T6_t4_mem1
	S += T6_t4_mem1 <= T6_t4

	T60 = S.Task('T60', length=1, delay_cost=1)
	T60 += alt(MAS)

	T60_mem0 = S.Task('T60_mem0', length=1, delay_cost=1)
	T60_mem0 += MM_MEM[0]
	S += 8 < T60_mem0
	S += T60_mem0 <= T60

	T60_mem1 = S.Task('T60_mem1', length=1, delay_cost=1)
	T60_mem1 += MM_MEM[1]
	S += 16 < T60_mem1
	S += T60_mem1 <= T60

	T6_t5 = S.Task('T6_t5', length=1, delay_cost=1)
	T6_t5 += alt(MAS)

	T6_t5_mem0 = S.Task('T6_t5_mem0', length=1, delay_cost=1)
	T6_t5_mem0 += MM_MEM[0]
	S += 8 < T6_t5_mem0
	S += T6_t5_mem0 <= T6_t5

	T6_t5_mem1 = S.Task('T6_t5_mem1', length=1, delay_cost=1)
	T6_t5_mem1 += MM_MEM[1]
	S += 16 < T6_t5_mem1
	S += T6_t5_mem1 <= T6_t5

	T7_t4_in = S.Task('T7_t4_in', length=1, delay_cost=1)
	T7_t4_in += alt(MM_in)
	T7_t4 = S.Task('T7_t4', length=6, delay_cost=1)
	T7_t4 += alt(MM)
	S += T7_t4>=T7_t4_in

	T7_t4_mem0 = S.Task('T7_t4_mem0', length=1, delay_cost=1)
	T7_t4_mem0 += MAS_MEM[0]
	S += 3 < T7_t4_mem0
	S += T7_t4_mem0 <= T7_t4

	T7_t4_mem1 = S.Task('T7_t4_mem1', length=1, delay_cost=1)
	T7_t4_mem1 += MAS_MEM[3]
	S += 3 < T7_t4_mem1
	S += T7_t4_mem1 <= T7_t4

	T70 = S.Task('T70', length=1, delay_cost=1)
	T70 += alt(MAS)

	T70_mem0 = S.Task('T70_mem0', length=1, delay_cost=1)
	T70_mem0 += MM_MEM[0]
	S += 9 < T70_mem0
	S += T70_mem0 <= T70

	T70_mem1 = S.Task('T70_mem1', length=1, delay_cost=1)
	T70_mem1 += MM_MEM[1]
	S += 17 < T70_mem1
	S += T70_mem1 <= T70

	T7_t5 = S.Task('T7_t5', length=1, delay_cost=1)
	T7_t5 += alt(MAS)

	T7_t5_mem0 = S.Task('T7_t5_mem0', length=1, delay_cost=1)
	T7_t5_mem0 += MM_MEM[0]
	S += 9 < T7_t5_mem0
	S += T7_t5_mem0 <= T7_t5

	T7_t5_mem1 = S.Task('T7_t5_mem1', length=1, delay_cost=1)
	T7_t5_mem1 += MM_MEM[1]
	S += 17 < T7_t5_mem1
	S += T7_t5_mem1 <= T7_t5

	T10 = S.Task('T10', length=1, delay_cost=1)
	T10 += alt(MAS)

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += alt(MM_MEM)
	S += (T1_t2*MM[0])-1 < T10_mem0*MM_MEM[0]
	S += T10_mem0 <= T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += alt(MAS_MEM)
	S += (T1_t5*MAS[0])-1 < T10_mem1*MAS_MEM[1]
	S += (T1_t5*MAS[1])-1 < T10_mem1*MAS_MEM[3]
	S += (T1_t5*MAS[2])-1 < T10_mem1*MAS_MEM[5]
	S += (T1_t5*MAS[3])-1 < T10_mem1*MAS_MEM[7]
	S += T10_mem1 <= T10

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(MAS)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += alt(MM_MEM)
	S += (T2_t4*MM[0])-1 < T21_mem0*MM_MEM[0]
	S += T21_mem0 <= T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += alt(MAS_MEM)
	S += (T2_t5*MAS[0])-1 < T21_mem1*MAS_MEM[1]
	S += (T2_t5*MAS[1])-1 < T21_mem1*MAS_MEM[3]
	S += (T2_t5*MAS[2])-1 < T21_mem1*MAS_MEM[5]
	S += (T2_t5*MAS[3])-1 < T21_mem1*MAS_MEM[7]
	S += T21_mem1 <= T21

	T31 = S.Task('T31', length=1, delay_cost=1)
	T31 += alt(MAS)

	T31_mem0 = S.Task('T31_mem0', length=1, delay_cost=1)
	T31_mem0 += alt(MM_MEM)
	S += (T3_t4*MM[0])-1 < T31_mem0*MM_MEM[0]
	S += T31_mem0 <= T31

	T31_mem1 = S.Task('T31_mem1', length=1, delay_cost=1)
	T31_mem1 += alt(MAS_MEM)
	S += (T3_t5*MAS[0])-1 < T31_mem1*MAS_MEM[1]
	S += (T3_t5*MAS[1])-1 < T31_mem1*MAS_MEM[3]
	S += (T3_t5*MAS[2])-1 < T31_mem1*MAS_MEM[5]
	S += (T3_t5*MAS[3])-1 < T31_mem1*MAS_MEM[7]
	S += T31_mem1 <= T31

	T41 = S.Task('T41', length=1, delay_cost=1)
	T41 += alt(MAS)

	T41_mem0 = S.Task('T41_mem0', length=1, delay_cost=1)
	T41_mem0 += alt(MM_MEM)
	S += (T4_t4*MM[0])-1 < T41_mem0*MM_MEM[0]
	S += T41_mem0 <= T41

	T41_mem1 = S.Task('T41_mem1', length=1, delay_cost=1)
	T41_mem1 += alt(MAS_MEM)
	S += (T4_t5*MAS[0])-1 < T41_mem1*MAS_MEM[1]
	S += (T4_t5*MAS[1])-1 < T41_mem1*MAS_MEM[3]
	S += (T4_t5*MAS[2])-1 < T41_mem1*MAS_MEM[5]
	S += (T4_t5*MAS[3])-1 < T41_mem1*MAS_MEM[7]
	S += T41_mem1 <= T41

	T50 = S.Task('T50', length=1, delay_cost=1)
	T50 += alt(MAS)

	T50_mem0 = S.Task('T50_mem0', length=1, delay_cost=1)
	T50_mem0 += alt(MM_MEM)
	S += (T5_t2*MM[0])-1 < T50_mem0*MM_MEM[0]
	S += T50_mem0 <= T50

	T50_mem1 = S.Task('T50_mem1', length=1, delay_cost=1)
	T50_mem1 += alt(MAS_MEM)
	S += (T5_t5*MAS[0])-1 < T50_mem1*MAS_MEM[1]
	S += (T5_t5*MAS[1])-1 < T50_mem1*MAS_MEM[3]
	S += (T5_t5*MAS[2])-1 < T50_mem1*MAS_MEM[5]
	S += (T5_t5*MAS[3])-1 < T50_mem1*MAS_MEM[7]
	S += T50_mem1 <= T50

	T61 = S.Task('T61', length=1, delay_cost=1)
	T61 += alt(MAS)

	T61_mem0 = S.Task('T61_mem0', length=1, delay_cost=1)
	T61_mem0 += alt(MM_MEM)
	S += (T6_t4*MM[0])-1 < T61_mem0*MM_MEM[0]
	S += T61_mem0 <= T61

	T61_mem1 = S.Task('T61_mem1', length=1, delay_cost=1)
	T61_mem1 += alt(MAS_MEM)
	S += (T6_t5*MAS[0])-1 < T61_mem1*MAS_MEM[1]
	S += (T6_t5*MAS[1])-1 < T61_mem1*MAS_MEM[3]
	S += (T6_t5*MAS[2])-1 < T61_mem1*MAS_MEM[5]
	S += (T6_t5*MAS[3])-1 < T61_mem1*MAS_MEM[7]
	S += T61_mem1 <= T61

	T71 = S.Task('T71', length=1, delay_cost=1)
	T71 += alt(MAS)

	T71_mem0 = S.Task('T71_mem0', length=1, delay_cost=1)
	T71_mem0 += alt(MM_MEM)
	S += (T7_t4*MM[0])-1 < T71_mem0*MM_MEM[0]
	S += T71_mem0 <= T71

	T71_mem1 = S.Task('T71_mem1', length=1, delay_cost=1)
	T71_mem1 += alt(MAS_MEM)
	S += (T7_t5*MAS[0])-1 < T71_mem1*MAS_MEM[1]
	S += (T7_t5*MAS[1])-1 < T71_mem1*MAS_MEM[3]
	S += (T7_t5*MAS[2])-1 < T71_mem1*MAS_MEM[5]
	S += (T7_t5*MAS[3])-1 < T71_mem1*MAS_MEM[7]
	S += T71_mem1 <= T71

	T8_t1_in = S.Task('T8_t1_in', length=1, delay_cost=1)
	T8_t1_in += alt(MM_in)
	T8_t1 = S.Task('T8_t1', length=6, delay_cost=1)
	T8_t1 += alt(MM)
	S += T8_t1>=T8_t1_in

	T8_t1_mem0 = S.Task('T8_t1_mem0', length=1, delay_cost=1)
	T8_t1_mem0 += MAIN_MEM_r[0]
	T8_t1_mem1 = S.Task('T8_t1_mem1', length=1, delay_cost=1)
	T8_t1_mem1 += alt(MAS_MEM)
	S += (T11*MAS[0])-1 < T8_t1_mem1*MAS_MEM[1]
	S += (T11*MAS[1])-1 < T8_t1_mem1*MAS_MEM[3]
	S += (T11*MAS[2])-1 < T8_t1_mem1*MAS_MEM[5]
	S += (T11*MAS[3])-1 < T8_t1_mem1*MAS_MEM[7]
	S += T8_t1_mem1 <= T8_t1

	T9_t1_in = S.Task('T9_t1_in', length=1, delay_cost=1)
	T9_t1_in += alt(MM_in)
	T9_t1 = S.Task('T9_t1', length=6, delay_cost=1)
	T9_t1 += alt(MM)
	S += T9_t1>=T9_t1_in

	T9_t1_mem0 = S.Task('T9_t1_mem0', length=1, delay_cost=1)
	T9_t1_mem0 += MAIN_MEM_r[0]
	T9_t1_mem1 = S.Task('T9_t1_mem1', length=1, delay_cost=1)
	T9_t1_mem1 += alt(MAS_MEM)
	S += (T11*MAS[0])-1 < T9_t1_mem1*MAS_MEM[1]
	S += (T11*MAS[1])-1 < T9_t1_mem1*MAS_MEM[3]
	S += (T11*MAS[2])-1 < T9_t1_mem1*MAS_MEM[5]
	S += (T11*MAS[3])-1 < T9_t1_mem1*MAS_MEM[7]
	S += T9_t1_mem1 <= T9_t1

	T10_t0_in = S.Task('T10_t0_in', length=1, delay_cost=1)
	T10_t0_in += alt(MM_in)
	T10_t0 = S.Task('T10_t0', length=6, delay_cost=1)
	T10_t0 += alt(MM)
	S += T10_t0>=T10_t0_in

	T10_t0_mem0 = S.Task('T10_t0_mem0', length=1, delay_cost=1)
	T10_t0_mem0 += MAIN_MEM_r[0]
	T10_t0_mem1 = S.Task('T10_t0_mem1', length=1, delay_cost=1)
	T10_t0_mem1 += alt(MAS_MEM)
	S += (T30*MAS[0])-1 < T10_t0_mem1*MAS_MEM[1]
	S += (T30*MAS[1])-1 < T10_t0_mem1*MAS_MEM[3]
	S += (T30*MAS[2])-1 < T10_t0_mem1*MAS_MEM[5]
	S += (T30*MAS[3])-1 < T10_t0_mem1*MAS_MEM[7]
	S += T10_t0_mem1 <= T10_t0

	T11_t0_in = S.Task('T11_t0_in', length=1, delay_cost=1)
	T11_t0_in += alt(MM_in)
	T11_t0 = S.Task('T11_t0', length=6, delay_cost=1)
	T11_t0 += alt(MM)
	S += T11_t0>=T11_t0_in

	T11_t0_mem0 = S.Task('T11_t0_mem0', length=1, delay_cost=1)
	T11_t0_mem0 += MAIN_MEM_r[0]
	T11_t0_mem1 = S.Task('T11_t0_mem1', length=1, delay_cost=1)
	T11_t0_mem1 += alt(MAS_MEM)
	S += (T30*MAS[0])-1 < T11_t0_mem1*MAS_MEM[1]
	S += (T30*MAS[1])-1 < T11_t0_mem1*MAS_MEM[3]
	S += (T30*MAS[2])-1 < T11_t0_mem1*MAS_MEM[5]
	S += (T30*MAS[3])-1 < T11_t0_mem1*MAS_MEM[7]
	S += T11_t0_mem1 <= T11_t0

	T120 = S.Task('T120', length=1, delay_cost=1)
	T120 += alt(MAS)

	T120_mem0 = S.Task('T120_mem0', length=1, delay_cost=1)
	T120_mem0 += alt(MAS_MEM)
	S += (T40*MAS[0])-1 < T120_mem0*MAS_MEM[0]
	S += (T40*MAS[1])-1 < T120_mem0*MAS_MEM[2]
	S += (T40*MAS[2])-1 < T120_mem0*MAS_MEM[4]
	S += (T40*MAS[3])-1 < T120_mem0*MAS_MEM[6]
	S += T120_mem0 <= T120

	T120_mem1 = S.Task('T120_mem1', length=1, delay_cost=1)
	T120_mem1 += alt(MAS_MEM)
	S += (T20*MAS[0])-1 < T120_mem1*MAS_MEM[1]
	S += (T20*MAS[1])-1 < T120_mem1*MAS_MEM[3]
	S += (T20*MAS[2])-1 < T120_mem1*MAS_MEM[5]
	S += (T20*MAS[3])-1 < T120_mem1*MAS_MEM[7]
	S += T120_mem1 <= T120

	T130 = S.Task('T130', length=1, delay_cost=1)
	T130 += alt(MAS)

	T130_mem0 = S.Task('T130_mem0', length=1, delay_cost=1)
	T130_mem0 += alt(MAS_MEM)
	S += (T40*MAS[0])-1 < T130_mem0*MAS_MEM[0]
	S += (T40*MAS[1])-1 < T130_mem0*MAS_MEM[2]
	S += (T40*MAS[2])-1 < T130_mem0*MAS_MEM[4]
	S += (T40*MAS[3])-1 < T130_mem0*MAS_MEM[6]
	S += T130_mem0 <= T130

	T130_mem1 = S.Task('T130_mem1', length=1, delay_cost=1)
	T130_mem1 += alt(MAS_MEM)
	S += (T20*MAS[0])-1 < T130_mem1*MAS_MEM[1]
	S += (T20*MAS[1])-1 < T130_mem1*MAS_MEM[3]
	S += (T20*MAS[2])-1 < T130_mem1*MAS_MEM[5]
	S += (T20*MAS[3])-1 < T130_mem1*MAS_MEM[7]
	S += T130_mem1 <= T130

	T150 = S.Task('T150', length=1, delay_cost=1)
	T150 += alt(MAS)

	T150_mem0 = S.Task('T150_mem0', length=1, delay_cost=1)
	T150_mem0 += alt(MAS_MEM)
	S += (T70*MAS[0])-1 < T150_mem0*MAS_MEM[0]
	S += (T70*MAS[1])-1 < T150_mem0*MAS_MEM[2]
	S += (T70*MAS[2])-1 < T150_mem0*MAS_MEM[4]
	S += (T70*MAS[3])-1 < T150_mem0*MAS_MEM[6]
	S += T150_mem0 <= T150

	T8_t0_in = S.Task('T8_t0_in', length=1, delay_cost=1)
	T8_t0_in += alt(MM_in)
	T8_t0 = S.Task('T8_t0', length=6, delay_cost=1)
	T8_t0 += alt(MM)
	S += T8_t0>=T8_t0_in

	T8_t0_mem0 = S.Task('T8_t0_mem0', length=1, delay_cost=1)
	T8_t0_mem0 += MAIN_MEM_r[0]
	T8_t0_mem1 = S.Task('T8_t0_mem1', length=1, delay_cost=1)
	T8_t0_mem1 += alt(MAS_MEM)
	S += (T10*MAS[0])-1 < T8_t0_mem1*MAS_MEM[1]
	S += (T10*MAS[1])-1 < T8_t0_mem1*MAS_MEM[3]
	S += (T10*MAS[2])-1 < T8_t0_mem1*MAS_MEM[5]
	S += (T10*MAS[3])-1 < T8_t0_mem1*MAS_MEM[7]
	S += T8_t0_mem1 <= T8_t0

	T8_t3 = S.Task('T8_t3', length=1, delay_cost=1)
	T8_t3 += alt(MAS)

	T8_t3_mem0 = S.Task('T8_t3_mem0', length=1, delay_cost=1)
	T8_t3_mem0 += alt(MAS_MEM)
	S += (T10*MAS[0])-1 < T8_t3_mem0*MAS_MEM[0]
	S += (T10*MAS[1])-1 < T8_t3_mem0*MAS_MEM[2]
	S += (T10*MAS[2])-1 < T8_t3_mem0*MAS_MEM[4]
	S += (T10*MAS[3])-1 < T8_t3_mem0*MAS_MEM[6]
	S += T8_t3_mem0 <= T8_t3

	T8_t3_mem1 = S.Task('T8_t3_mem1', length=1, delay_cost=1)
	T8_t3_mem1 += alt(MAS_MEM)
	S += (T11*MAS[0])-1 < T8_t3_mem1*MAS_MEM[1]
	S += (T11*MAS[1])-1 < T8_t3_mem1*MAS_MEM[3]
	S += (T11*MAS[2])-1 < T8_t3_mem1*MAS_MEM[5]
	S += (T11*MAS[3])-1 < T8_t3_mem1*MAS_MEM[7]
	S += T8_t3_mem1 <= T8_t3

	T9_t0_in = S.Task('T9_t0_in', length=1, delay_cost=1)
	T9_t0_in += alt(MM_in)
	T9_t0 = S.Task('T9_t0', length=6, delay_cost=1)
	T9_t0 += alt(MM)
	S += T9_t0>=T9_t0_in

	T9_t0_mem0 = S.Task('T9_t0_mem0', length=1, delay_cost=1)
	T9_t0_mem0 += MAIN_MEM_r[0]
	T9_t0_mem1 = S.Task('T9_t0_mem1', length=1, delay_cost=1)
	T9_t0_mem1 += alt(MAS_MEM)
	S += (T10*MAS[0])-1 < T9_t0_mem1*MAS_MEM[1]
	S += (T10*MAS[1])-1 < T9_t0_mem1*MAS_MEM[3]
	S += (T10*MAS[2])-1 < T9_t0_mem1*MAS_MEM[5]
	S += (T10*MAS[3])-1 < T9_t0_mem1*MAS_MEM[7]
	S += T9_t0_mem1 <= T9_t0

	T9_t3 = S.Task('T9_t3', length=1, delay_cost=1)
	T9_t3 += alt(MAS)

	T9_t3_mem0 = S.Task('T9_t3_mem0', length=1, delay_cost=1)
	T9_t3_mem0 += alt(MAS_MEM)
	S += (T10*MAS[0])-1 < T9_t3_mem0*MAS_MEM[0]
	S += (T10*MAS[1])-1 < T9_t3_mem0*MAS_MEM[2]
	S += (T10*MAS[2])-1 < T9_t3_mem0*MAS_MEM[4]
	S += (T10*MAS[3])-1 < T9_t3_mem0*MAS_MEM[6]
	S += T9_t3_mem0 <= T9_t3

	T9_t3_mem1 = S.Task('T9_t3_mem1', length=1, delay_cost=1)
	T9_t3_mem1 += alt(MAS_MEM)
	S += (T11*MAS[0])-1 < T9_t3_mem1*MAS_MEM[1]
	S += (T11*MAS[1])-1 < T9_t3_mem1*MAS_MEM[3]
	S += (T11*MAS[2])-1 < T9_t3_mem1*MAS_MEM[5]
	S += (T11*MAS[3])-1 < T9_t3_mem1*MAS_MEM[7]
	S += T9_t3_mem1 <= T9_t3

	T10_t1_in = S.Task('T10_t1_in', length=1, delay_cost=1)
	T10_t1_in += alt(MM_in)
	T10_t1 = S.Task('T10_t1', length=6, delay_cost=1)
	T10_t1 += alt(MM)
	S += T10_t1>=T10_t1_in

	T10_t1_mem0 = S.Task('T10_t1_mem0', length=1, delay_cost=1)
	T10_t1_mem0 += MAIN_MEM_r[0]
	T10_t1_mem1 = S.Task('T10_t1_mem1', length=1, delay_cost=1)
	T10_t1_mem1 += alt(MAS_MEM)
	S += (T31*MAS[0])-1 < T10_t1_mem1*MAS_MEM[1]
	S += (T31*MAS[1])-1 < T10_t1_mem1*MAS_MEM[3]
	S += (T31*MAS[2])-1 < T10_t1_mem1*MAS_MEM[5]
	S += (T31*MAS[3])-1 < T10_t1_mem1*MAS_MEM[7]
	S += T10_t1_mem1 <= T10_t1

	T10_t3 = S.Task('T10_t3', length=1, delay_cost=1)
	T10_t3 += alt(MAS)

	T10_t3_mem0 = S.Task('T10_t3_mem0', length=1, delay_cost=1)
	T10_t3_mem0 += alt(MAS_MEM)
	S += (T30*MAS[0])-1 < T10_t3_mem0*MAS_MEM[0]
	S += (T30*MAS[1])-1 < T10_t3_mem0*MAS_MEM[2]
	S += (T30*MAS[2])-1 < T10_t3_mem0*MAS_MEM[4]
	S += (T30*MAS[3])-1 < T10_t3_mem0*MAS_MEM[6]
	S += T10_t3_mem0 <= T10_t3

	T10_t3_mem1 = S.Task('T10_t3_mem1', length=1, delay_cost=1)
	T10_t3_mem1 += alt(MAS_MEM)
	S += (T31*MAS[0])-1 < T10_t3_mem1*MAS_MEM[1]
	S += (T31*MAS[1])-1 < T10_t3_mem1*MAS_MEM[3]
	S += (T31*MAS[2])-1 < T10_t3_mem1*MAS_MEM[5]
	S += (T31*MAS[3])-1 < T10_t3_mem1*MAS_MEM[7]
	S += T10_t3_mem1 <= T10_t3

	T11_t1_in = S.Task('T11_t1_in', length=1, delay_cost=1)
	T11_t1_in += alt(MM_in)
	T11_t1 = S.Task('T11_t1', length=6, delay_cost=1)
	T11_t1 += alt(MM)
	S += T11_t1>=T11_t1_in

	T11_t1_mem0 = S.Task('T11_t1_mem0', length=1, delay_cost=1)
	T11_t1_mem0 += MAIN_MEM_r[0]
	T11_t1_mem1 = S.Task('T11_t1_mem1', length=1, delay_cost=1)
	T11_t1_mem1 += alt(MAS_MEM)
	S += (T31*MAS[0])-1 < T11_t1_mem1*MAS_MEM[1]
	S += (T31*MAS[1])-1 < T11_t1_mem1*MAS_MEM[3]
	S += (T31*MAS[2])-1 < T11_t1_mem1*MAS_MEM[5]
	S += (T31*MAS[3])-1 < T11_t1_mem1*MAS_MEM[7]
	S += T11_t1_mem1 <= T11_t1

	T11_t3 = S.Task('T11_t3', length=1, delay_cost=1)
	T11_t3 += alt(MAS)

	T11_t3_mem0 = S.Task('T11_t3_mem0', length=1, delay_cost=1)
	T11_t3_mem0 += alt(MAS_MEM)
	S += (T30*MAS[0])-1 < T11_t3_mem0*MAS_MEM[0]
	S += (T30*MAS[1])-1 < T11_t3_mem0*MAS_MEM[2]
	S += (T30*MAS[2])-1 < T11_t3_mem0*MAS_MEM[4]
	S += (T30*MAS[3])-1 < T11_t3_mem0*MAS_MEM[6]
	S += T11_t3_mem0 <= T11_t3

	T11_t3_mem1 = S.Task('T11_t3_mem1', length=1, delay_cost=1)
	T11_t3_mem1 += alt(MAS_MEM)
	S += (T31*MAS[0])-1 < T11_t3_mem1*MAS_MEM[1]
	S += (T31*MAS[1])-1 < T11_t3_mem1*MAS_MEM[3]
	S += (T31*MAS[2])-1 < T11_t3_mem1*MAS_MEM[5]
	S += (T31*MAS[3])-1 < T11_t3_mem1*MAS_MEM[7]
	S += T11_t3_mem1 <= T11_t3

	T121 = S.Task('T121', length=1, delay_cost=1)
	T121 += alt(MAS)

	T121_mem0 = S.Task('T121_mem0', length=1, delay_cost=1)
	T121_mem0 += alt(MAS_MEM)
	S += (T41*MAS[0])-1 < T121_mem0*MAS_MEM[0]
	S += (T41*MAS[1])-1 < T121_mem0*MAS_MEM[2]
	S += (T41*MAS[2])-1 < T121_mem0*MAS_MEM[4]
	S += (T41*MAS[3])-1 < T121_mem0*MAS_MEM[6]
	S += T121_mem0 <= T121

	T121_mem1 = S.Task('T121_mem1', length=1, delay_cost=1)
	T121_mem1 += alt(MAS_MEM)
	S += (T21*MAS[0])-1 < T121_mem1*MAS_MEM[1]
	S += (T21*MAS[1])-1 < T121_mem1*MAS_MEM[3]
	S += (T21*MAS[2])-1 < T121_mem1*MAS_MEM[5]
	S += (T21*MAS[3])-1 < T121_mem1*MAS_MEM[7]
	S += T121_mem1 <= T121

	T131 = S.Task('T131', length=1, delay_cost=1)
	T131 += alt(MAS)

	T131_mem0 = S.Task('T131_mem0', length=1, delay_cost=1)
	T131_mem0 += alt(MAS_MEM)
	S += (T41*MAS[0])-1 < T131_mem0*MAS_MEM[0]
	S += (T41*MAS[1])-1 < T131_mem0*MAS_MEM[2]
	S += (T41*MAS[2])-1 < T131_mem0*MAS_MEM[4]
	S += (T41*MAS[3])-1 < T131_mem0*MAS_MEM[6]
	S += T131_mem0 <= T131

	T131_mem1 = S.Task('T131_mem1', length=1, delay_cost=1)
	T131_mem1 += alt(MAS_MEM)
	S += (T21*MAS[0])-1 < T131_mem1*MAS_MEM[1]
	S += (T21*MAS[1])-1 < T131_mem1*MAS_MEM[3]
	S += (T21*MAS[2])-1 < T131_mem1*MAS_MEM[5]
	S += (T21*MAS[3])-1 < T131_mem1*MAS_MEM[7]
	S += T131_mem1 <= T131

	T14_t0_in = S.Task('T14_t0_in', length=1, delay_cost=1)
	T14_t0_in += alt(MM_in)
	T14_t0 = S.Task('T14_t0', length=6, delay_cost=1)
	T14_t0 += alt(MM)
	S += T14_t0>=T14_t0_in

	T14_t0_mem0 = S.Task('T14_t0_mem0', length=1, delay_cost=1)
	T14_t0_mem0 += alt(MAS_MEM)
	S += (T130*MAS[0])-1 < T14_t0_mem0*MAS_MEM[0]
	S += (T130*MAS[1])-1 < T14_t0_mem0*MAS_MEM[2]
	S += (T130*MAS[2])-1 < T14_t0_mem0*MAS_MEM[4]
	S += (T130*MAS[3])-1 < T14_t0_mem0*MAS_MEM[6]
	S += T14_t0_mem0 <= T14_t0

	T151 = S.Task('T151', length=1, delay_cost=1)
	T151 += alt(MAS)

	T151_mem0 = S.Task('T151_mem0', length=1, delay_cost=1)
	T151_mem0 += alt(MAS_MEM)
	S += (T71*MAS[0])-1 < T151_mem0*MAS_MEM[0]
	S += (T71*MAS[1])-1 < T151_mem0*MAS_MEM[2]
	S += (T71*MAS[2])-1 < T151_mem0*MAS_MEM[4]
	S += (T71*MAS[3])-1 < T151_mem0*MAS_MEM[6]
	S += T151_mem0 <= T151

	T16_t2 = S.Task('T16_t2', length=1, delay_cost=1)
	T16_t2 += alt(MAS)

	T16_t2_mem0 = S.Task('T16_t2_mem0', length=1, delay_cost=1)
	T16_t2_mem0 += alt(MAS_MEM)
	S += (T10*MAS[0])-1 < T16_t2_mem0*MAS_MEM[0]
	S += (T10*MAS[1])-1 < T16_t2_mem0*MAS_MEM[2]
	S += (T10*MAS[2])-1 < T16_t2_mem0*MAS_MEM[4]
	S += (T10*MAS[3])-1 < T16_t2_mem0*MAS_MEM[6]
	S += T16_t2_mem0 <= T16_t2

	T16_t2_mem1 = S.Task('T16_t2_mem1', length=1, delay_cost=1)
	T16_t2_mem1 += alt(MAS_MEM)
	S += (T11*MAS[0])-1 < T16_t2_mem1*MAS_MEM[1]
	S += (T11*MAS[1])-1 < T16_t2_mem1*MAS_MEM[3]
	S += (T11*MAS[2])-1 < T16_t2_mem1*MAS_MEM[5]
	S += (T11*MAS[3])-1 < T16_t2_mem1*MAS_MEM[7]
	S += T16_t2_mem1 <= T16_t2

	T20_t2 = S.Task('T20_t2', length=1, delay_cost=1)
	T20_t2 += alt(MAS)

	T20_t2_mem0 = S.Task('T20_t2_mem0', length=1, delay_cost=1)
	T20_t2_mem0 += alt(MAS_MEM)
	S += (T50*MAS[0])-1 < T20_t2_mem0*MAS_MEM[0]
	S += (T50*MAS[1])-1 < T20_t2_mem0*MAS_MEM[2]
	S += (T50*MAS[2])-1 < T20_t2_mem0*MAS_MEM[4]
	S += (T50*MAS[3])-1 < T20_t2_mem0*MAS_MEM[6]
	S += T20_t2_mem0 <= T20_t2

	T20_t2_mem1 = S.Task('T20_t2_mem1', length=1, delay_cost=1)
	T20_t2_mem1 += alt(MAS_MEM)
	S += (T51*MAS[0])-1 < T20_t2_mem1*MAS_MEM[1]
	S += (T51*MAS[1])-1 < T20_t2_mem1*MAS_MEM[3]
	S += (T51*MAS[2])-1 < T20_t2_mem1*MAS_MEM[5]
	S += (T51*MAS[3])-1 < T20_t2_mem1*MAS_MEM[7]
	S += T20_t2_mem1 <= T20_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS4/EP2_LADDERMUL/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

