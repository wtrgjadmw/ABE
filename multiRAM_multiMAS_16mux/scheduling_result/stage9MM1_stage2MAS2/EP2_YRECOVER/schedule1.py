from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 159
	S = Scenario("schedule1", horizon=horizon)

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
	r3_t3_in = S.Task('r3_t3_in', length=1, delay_cost=1)
	S += r3_t3_in >= 0
	r3_t3_in += MAS_in[0]

	r3_t3_mem0 = S.Task('r3_t3_mem0', length=1, delay_cost=1)
	S += r3_t3_mem0 >= 0
	r3_t3_mem0 += MAIN_MEM_r[0]

	r3_t3_mem1 = S.Task('r3_t3_mem1', length=1, delay_cost=1)
	S += r3_t3_mem1 >= 0
	r3_t3_mem1 += MAIN_MEM_r[1]

	r3_t3 = S.Task('r3_t3', length=2, delay_cost=1)
	S += r3_t3 >= 1
	r3_t3 += MAS[0]

	r9_t2_in = S.Task('r9_t2_in', length=1, delay_cost=1)
	S += r9_t2_in >= 1
	r9_t2_in += MAS_in[0]

	r9_t2_mem0 = S.Task('r9_t2_mem0', length=1, delay_cost=1)
	S += r9_t2_mem0 >= 1
	r9_t2_mem0 += MAIN_MEM_r[0]

	r9_t2_mem1 = S.Task('r9_t2_mem1', length=1, delay_cost=1)
	S += r9_t2_mem1 >= 1
	r9_t2_mem1 += MAIN_MEM_r[1]

	r12_t1_in = S.Task('r12_t1_in', length=1, delay_cost=1)
	S += r12_t1_in >= 2
	r12_t1_in += MM_in[0]

	r12_t1_mem0 = S.Task('r12_t1_mem0', length=1, delay_cost=1)
	S += r12_t1_mem0 >= 2
	r12_t1_mem0 += MAIN_MEM_r[0]

	r12_t1_mem1 = S.Task('r12_t1_mem1', length=1, delay_cost=1)
	S += r12_t1_mem1 >= 2
	r12_t1_mem1 += MAIN_MEM_r[1]

	r9_t2 = S.Task('r9_t2', length=2, delay_cost=1)
	S += r9_t2 >= 2
	r9_t2 += MAS[0]

	r12_t1 = S.Task('r12_t1', length=9, delay_cost=1)
	S += r12_t1 >= 3
	r12_t1 += MM[0]

	r5_t0_in = S.Task('r5_t0_in', length=1, delay_cost=1)
	S += r5_t0_in >= 3
	r5_t0_in += MM_in[0]

	r5_t0_mem0 = S.Task('r5_t0_mem0', length=1, delay_cost=1)
	S += r5_t0_mem0 >= 3
	r5_t0_mem0 += MAIN_MEM_r[0]

	r5_t0_mem1 = S.Task('r5_t0_mem1', length=1, delay_cost=1)
	S += r5_t0_mem1 >= 3
	r5_t0_mem1 += MAIN_MEM_r[1]

	r4_t3_in = S.Task('r4_t3_in', length=1, delay_cost=1)
	S += r4_t3_in >= 4
	r4_t3_in += MAS_in[0]

	r4_t3_mem0 = S.Task('r4_t3_mem0', length=1, delay_cost=1)
	S += r4_t3_mem0 >= 4
	r4_t3_mem0 += MAIN_MEM_r[0]

	r4_t3_mem1 = S.Task('r4_t3_mem1', length=1, delay_cost=1)
	S += r4_t3_mem1 >= 4
	r4_t3_mem1 += MAIN_MEM_r[1]

	r5_t0 = S.Task('r5_t0', length=9, delay_cost=1)
	S += r5_t0 >= 4
	r5_t0 += MM[0]

	r1_t2_in = S.Task('r1_t2_in', length=1, delay_cost=1)
	S += r1_t2_in >= 5
	r1_t2_in += MAS_in[0]

	r1_t2_mem0 = S.Task('r1_t2_mem0', length=1, delay_cost=1)
	S += r1_t2_mem0 >= 5
	r1_t2_mem0 += MAIN_MEM_r[0]

	r1_t2_mem1 = S.Task('r1_t2_mem1', length=1, delay_cost=1)
	S += r1_t2_mem1 >= 5
	r1_t2_mem1 += MAIN_MEM_r[1]

	r4_t3 = S.Task('r4_t3', length=2, delay_cost=1)
	S += r4_t3 >= 5
	r4_t3 += MAS[0]

	r1_t2 = S.Task('r1_t2', length=2, delay_cost=1)
	S += r1_t2 >= 6
	r1_t2 += MAS[0]

	r6_t3_in = S.Task('r6_t3_in', length=1, delay_cost=1)
	S += r6_t3_in >= 6
	r6_t3_in += MAS_in[0]

	r6_t3_mem0 = S.Task('r6_t3_mem0', length=1, delay_cost=1)
	S += r6_t3_mem0 >= 6
	r6_t3_mem0 += MAIN_MEM_r[0]

	r6_t3_mem1 = S.Task('r6_t3_mem1', length=1, delay_cost=1)
	S += r6_t3_mem1 >= 6
	r6_t3_mem1 += MAIN_MEM_r[1]

	r13_t2_in = S.Task('r13_t2_in', length=1, delay_cost=1)
	S += r13_t2_in >= 7
	r13_t2_in += MAS_in[0]

	r13_t2_mem0 = S.Task('r13_t2_mem0', length=1, delay_cost=1)
	S += r13_t2_mem0 >= 7
	r13_t2_mem0 += MAIN_MEM_r[0]

	r13_t2_mem1 = S.Task('r13_t2_mem1', length=1, delay_cost=1)
	S += r13_t2_mem1 >= 7
	r13_t2_mem1 += MAIN_MEM_r[1]

	r6_t3 = S.Task('r6_t3', length=2, delay_cost=1)
	S += r6_t3 >= 7
	r6_t3 += MAS[0]

	r13_t2 = S.Task('r13_t2', length=2, delay_cost=1)
	S += r13_t2 >= 8
	r13_t2 += MAS[0]

	r4_t2_in = S.Task('r4_t2_in', length=1, delay_cost=1)
	S += r4_t2_in >= 8
	r4_t2_in += MAS_in[1]

	r4_t2_mem0 = S.Task('r4_t2_mem0', length=1, delay_cost=1)
	S += r4_t2_mem0 >= 8
	r4_t2_mem0 += MAIN_MEM_r[0]

	r4_t2_mem1 = S.Task('r4_t2_mem1', length=1, delay_cost=1)
	S += r4_t2_mem1 >= 8
	r4_t2_mem1 += MAIN_MEM_r[1]

	r4_t2 = S.Task('r4_t2', length=2, delay_cost=1)
	S += r4_t2 >= 9
	r4_t2 += MAS[1]

	r6_t1_in = S.Task('r6_t1_in', length=1, delay_cost=1)
	S += r6_t1_in >= 9
	r6_t1_in += MM_in[0]

	r6_t1_mem0 = S.Task('r6_t1_mem0', length=1, delay_cost=1)
	S += r6_t1_mem0 >= 9
	r6_t1_mem0 += MAIN_MEM_r[0]

	r6_t1_mem1 = S.Task('r6_t1_mem1', length=1, delay_cost=1)
	S += r6_t1_mem1 >= 9
	r6_t1_mem1 += MAIN_MEM_r[1]

	r12_t3_in = S.Task('r12_t3_in', length=1, delay_cost=1)
	S += r12_t3_in >= 10
	r12_t3_in += MAS_in[1]

	r12_t3_mem0 = S.Task('r12_t3_mem0', length=1, delay_cost=1)
	S += r12_t3_mem0 >= 10
	r12_t3_mem0 += MAIN_MEM_r[0]

	r12_t3_mem1 = S.Task('r12_t3_mem1', length=1, delay_cost=1)
	S += r12_t3_mem1 >= 10
	r12_t3_mem1 += MAIN_MEM_r[1]

	r6_t1 = S.Task('r6_t1', length=9, delay_cost=1)
	S += r6_t1 >= 10
	r6_t1 += MM[0]

	r12_t3 = S.Task('r12_t3', length=2, delay_cost=1)
	S += r12_t3 >= 11
	r12_t3 += MAS[1]

	r13_t3_in = S.Task('r13_t3_in', length=1, delay_cost=1)
	S += r13_t3_in >= 11
	r13_t3_in += MAS_in[1]

	r13_t3_mem0 = S.Task('r13_t3_mem0', length=1, delay_cost=1)
	S += r13_t3_mem0 >= 11
	r13_t3_mem0 += MAIN_MEM_r[0]

	r13_t3_mem1 = S.Task('r13_t3_mem1', length=1, delay_cost=1)
	S += r13_t3_mem1 >= 11
	r13_t3_mem1 += MAIN_MEM_r[1]

	r13_t3 = S.Task('r13_t3', length=2, delay_cost=1)
	S += r13_t3 >= 12
	r13_t3 += MAS[1]

	r3_t0_in = S.Task('r3_t0_in', length=1, delay_cost=1)
	S += r3_t0_in >= 12
	r3_t0_in += MM_in[0]

	r3_t0_mem0 = S.Task('r3_t0_mem0', length=1, delay_cost=1)
	S += r3_t0_mem0 >= 12
	r3_t0_mem0 += MAIN_MEM_r[0]

	r3_t0_mem1 = S.Task('r3_t0_mem1', length=1, delay_cost=1)
	S += r3_t0_mem1 >= 12
	r3_t0_mem1 += MAIN_MEM_r[1]

	r16_t3_in = S.Task('r16_t3_in', length=1, delay_cost=1)
	S += r16_t3_in >= 13
	r16_t3_in += MAS_in[0]

	r16_t3_mem0 = S.Task('r16_t3_mem0', length=1, delay_cost=1)
	S += r16_t3_mem0 >= 13
	r16_t3_mem0 += MAIN_MEM_r[0]

	r16_t3_mem1 = S.Task('r16_t3_mem1', length=1, delay_cost=1)
	S += r16_t3_mem1 >= 13
	r16_t3_mem1 += MAIN_MEM_r[1]

	r3_t0 = S.Task('r3_t0', length=9, delay_cost=1)
	S += r3_t0 >= 13
	r3_t0 += MM[0]

	r16_t3 = S.Task('r16_t3', length=2, delay_cost=1)
	S += r16_t3 >= 14
	r16_t3 += MAS[0]

	r4_t0_in = S.Task('r4_t0_in', length=1, delay_cost=1)
	S += r4_t0_in >= 14
	r4_t0_in += MM_in[0]

	r4_t0_mem0 = S.Task('r4_t0_mem0', length=1, delay_cost=1)
	S += r4_t0_mem0 >= 14
	r4_t0_mem0 += MAIN_MEM_r[0]

	r4_t0_mem1 = S.Task('r4_t0_mem1', length=1, delay_cost=1)
	S += r4_t0_mem1 >= 14
	r4_t0_mem1 += MAIN_MEM_r[1]

	r3_t2_in = S.Task('r3_t2_in', length=1, delay_cost=1)
	S += r3_t2_in >= 15
	r3_t2_in += MAS_in[1]

	r3_t2_mem0 = S.Task('r3_t2_mem0', length=1, delay_cost=1)
	S += r3_t2_mem0 >= 15
	r3_t2_mem0 += MAIN_MEM_r[0]

	r3_t2_mem1 = S.Task('r3_t2_mem1', length=1, delay_cost=1)
	S += r3_t2_mem1 >= 15
	r3_t2_mem1 += MAIN_MEM_r[1]

	r4_t0 = S.Task('r4_t0', length=9, delay_cost=1)
	S += r4_t0 >= 15
	r4_t0 += MM[0]

	r1_t1_in = S.Task('r1_t1_in', length=1, delay_cost=1)
	S += r1_t1_in >= 16
	r1_t1_in += MM_in[0]

	r1_t1_mem0 = S.Task('r1_t1_mem0', length=1, delay_cost=1)
	S += r1_t1_mem0 >= 16
	r1_t1_mem0 += MAIN_MEM_r[0]

	r1_t1_mem1 = S.Task('r1_t1_mem1', length=1, delay_cost=1)
	S += r1_t1_mem1 >= 16
	r1_t1_mem1 += MAIN_MEM_r[1]

	r3_t2 = S.Task('r3_t2', length=2, delay_cost=1)
	S += r3_t2 >= 16
	r3_t2 += MAS[1]

	r12_t2_in = S.Task('r12_t2_in', length=1, delay_cost=1)
	S += r12_t2_in >= 17
	r12_t2_in += MAS_in[0]

	r12_t2_mem0 = S.Task('r12_t2_mem0', length=1, delay_cost=1)
	S += r12_t2_mem0 >= 17
	r12_t2_mem0 += MAIN_MEM_r[0]

	r12_t2_mem1 = S.Task('r12_t2_mem1', length=1, delay_cost=1)
	S += r12_t2_mem1 >= 17
	r12_t2_mem1 += MAIN_MEM_r[1]

	r1_t1 = S.Task('r1_t1', length=9, delay_cost=1)
	S += r1_t1 >= 17
	r1_t1 += MM[0]

	r12_t2 = S.Task('r12_t2', length=2, delay_cost=1)
	S += r12_t2 >= 18
	r12_t2 += MAS[0]

	r1_t3_in = S.Task('r1_t3_in', length=1, delay_cost=1)
	S += r1_t3_in >= 18
	r1_t3_in += MAS_in[0]

	r1_t3_mem0 = S.Task('r1_t3_mem0', length=1, delay_cost=1)
	S += r1_t3_mem0 >= 18
	r1_t3_mem0 += MAIN_MEM_r[0]

	r1_t3_mem1 = S.Task('r1_t3_mem1', length=1, delay_cost=1)
	S += r1_t3_mem1 >= 18
	r1_t3_mem1 += MAIN_MEM_r[1]

	r1_t3 = S.Task('r1_t3', length=2, delay_cost=1)
	S += r1_t3 >= 19
	r1_t3 += MAS[0]

	r5_t1_in = S.Task('r5_t1_in', length=1, delay_cost=1)
	S += r5_t1_in >= 19
	r5_t1_in += MM_in[0]

	r5_t1_mem0 = S.Task('r5_t1_mem0', length=1, delay_cost=1)
	S += r5_t1_mem0 >= 19
	r5_t1_mem0 += MAIN_MEM_r[0]

	r5_t1_mem1 = S.Task('r5_t1_mem1', length=1, delay_cost=1)
	S += r5_t1_mem1 >= 19
	r5_t1_mem1 += MAIN_MEM_r[1]

	r4_t1_in = S.Task('r4_t1_in', length=1, delay_cost=1)
	S += r4_t1_in >= 20
	r4_t1_in += MM_in[0]

	r4_t1_mem0 = S.Task('r4_t1_mem0', length=1, delay_cost=1)
	S += r4_t1_mem0 >= 20
	r4_t1_mem0 += MAIN_MEM_r[0]

	r4_t1_mem1 = S.Task('r4_t1_mem1', length=1, delay_cost=1)
	S += r4_t1_mem1 >= 20
	r4_t1_mem1 += MAIN_MEM_r[1]

	r5_t1 = S.Task('r5_t1', length=9, delay_cost=1)
	S += r5_t1 >= 20
	r5_t1 += MM[0]

	r1_t0_in = S.Task('r1_t0_in', length=1, delay_cost=1)
	S += r1_t0_in >= 21
	r1_t0_in += MM_in[0]

	r1_t0_mem0 = S.Task('r1_t0_mem0', length=1, delay_cost=1)
	S += r1_t0_mem0 >= 21
	r1_t0_mem0 += MAIN_MEM_r[0]

	r1_t0_mem1 = S.Task('r1_t0_mem1', length=1, delay_cost=1)
	S += r1_t0_mem1 >= 21
	r1_t0_mem1 += MAIN_MEM_r[1]

	r4_t1 = S.Task('r4_t1', length=9, delay_cost=1)
	S += r4_t1 >= 21
	r4_t1 += MM[0]

	r1_t0 = S.Task('r1_t0', length=9, delay_cost=1)
	S += r1_t0 >= 22
	r1_t0 += MM[0]

	r6_t2_in = S.Task('r6_t2_in', length=1, delay_cost=1)
	S += r6_t2_in >= 22
	r6_t2_in += MAS_in[0]

	r6_t2_mem0 = S.Task('r6_t2_mem0', length=1, delay_cost=1)
	S += r6_t2_mem0 >= 22
	r6_t2_mem0 += MAIN_MEM_r[0]

	r6_t2_mem1 = S.Task('r6_t2_mem1', length=1, delay_cost=1)
	S += r6_t2_mem1 >= 22
	r6_t2_mem1 += MAIN_MEM_r[1]

	r6_t0_in = S.Task('r6_t0_in', length=1, delay_cost=1)
	S += r6_t0_in >= 23
	r6_t0_in += MM_in[0]

	r6_t0_mem0 = S.Task('r6_t0_mem0', length=1, delay_cost=1)
	S += r6_t0_mem0 >= 23
	r6_t0_mem0 += MAIN_MEM_r[0]

	r6_t0_mem1 = S.Task('r6_t0_mem1', length=1, delay_cost=1)
	S += r6_t0_mem1 >= 23
	r6_t0_mem1 += MAIN_MEM_r[1]

	r6_t2 = S.Task('r6_t2', length=2, delay_cost=1)
	S += r6_t2 >= 23
	r6_t2 += MAS[0]

	r5_t2_in = S.Task('r5_t2_in', length=1, delay_cost=1)
	S += r5_t2_in >= 24
	r5_t2_in += MAS_in[1]

	r5_t2_mem0 = S.Task('r5_t2_mem0', length=1, delay_cost=1)
	S += r5_t2_mem0 >= 24
	r5_t2_mem0 += MAIN_MEM_r[0]

	r5_t2_mem1 = S.Task('r5_t2_mem1', length=1, delay_cost=1)
	S += r5_t2_mem1 >= 24
	r5_t2_mem1 += MAIN_MEM_r[1]

	r6_t0 = S.Task('r6_t0', length=9, delay_cost=1)
	S += r6_t0 >= 24
	r6_t0 += MM[0]

	r3_t1_in = S.Task('r3_t1_in', length=1, delay_cost=1)
	S += r3_t1_in >= 25
	r3_t1_in += MM_in[0]

	r3_t1_mem0 = S.Task('r3_t1_mem0', length=1, delay_cost=1)
	S += r3_t1_mem0 >= 25
	r3_t1_mem0 += MAIN_MEM_r[0]

	r3_t1_mem1 = S.Task('r3_t1_mem1', length=1, delay_cost=1)
	S += r3_t1_mem1 >= 25
	r3_t1_mem1 += MAIN_MEM_r[1]

	r5_t2 = S.Task('r5_t2', length=2, delay_cost=1)
	S += r5_t2 >= 25
	r5_t2 += MAS[1]

	r3_t1 = S.Task('r3_t1', length=9, delay_cost=1)
	S += r3_t1 >= 26
	r3_t1 += MM[0]

	r5_t3_in = S.Task('r5_t3_in', length=1, delay_cost=1)
	S += r5_t3_in >= 26
	r5_t3_in += MAS_in[0]

	r5_t3_mem0 = S.Task('r5_t3_mem0', length=1, delay_cost=1)
	S += r5_t3_mem0 >= 26
	r5_t3_mem0 += MAIN_MEM_r[0]

	r5_t3_mem1 = S.Task('r5_t3_mem1', length=1, delay_cost=1)
	S += r5_t3_mem1 >= 26
	r5_t3_mem1 += MAIN_MEM_r[1]

	r13_t1_in = S.Task('r13_t1_in', length=1, delay_cost=1)
	S += r13_t1_in >= 27
	r13_t1_in += MM_in[0]

	r13_t1_mem0 = S.Task('r13_t1_mem0', length=1, delay_cost=1)
	S += r13_t1_mem0 >= 27
	r13_t1_mem0 += MAIN_MEM_r[0]

	r13_t1_mem1 = S.Task('r13_t1_mem1', length=1, delay_cost=1)
	S += r13_t1_mem1 >= 27
	r13_t1_mem1 += MAIN_MEM_r[1]

	r5_t3 = S.Task('r5_t3', length=2, delay_cost=1)
	S += r5_t3 >= 27
	r5_t3 += MAS[0]

	r13_t0_in = S.Task('r13_t0_in', length=1, delay_cost=1)
	S += r13_t0_in >= 28
	r13_t0_in += MM_in[0]

	r13_t0_mem0 = S.Task('r13_t0_mem0', length=1, delay_cost=1)
	S += r13_t0_mem0 >= 28
	r13_t0_mem0 += MAIN_MEM_r[0]

	r13_t0_mem1 = S.Task('r13_t0_mem1', length=1, delay_cost=1)
	S += r13_t0_mem1 >= 28
	r13_t0_mem1 += MAIN_MEM_r[1]

	r13_t1 = S.Task('r13_t1', length=9, delay_cost=1)
	S += r13_t1 >= 28
	r13_t1 += MM[0]

	r12_t0_in = S.Task('r12_t0_in', length=1, delay_cost=1)
	S += r12_t0_in >= 29
	r12_t0_in += MM_in[0]

	r12_t0_mem0 = S.Task('r12_t0_mem0', length=1, delay_cost=1)
	S += r12_t0_mem0 >= 29
	r12_t0_mem0 += MAIN_MEM_r[0]

	r12_t0_mem1 = S.Task('r12_t0_mem1', length=1, delay_cost=1)
	S += r12_t0_mem1 >= 29
	r12_t0_mem1 += MAIN_MEM_r[1]

	r13_t0 = S.Task('r13_t0', length=9, delay_cost=1)
	S += r13_t0 >= 29
	r13_t0 += MM[0]

	r12_t0 = S.Task('r12_t0', length=9, delay_cost=1)
	S += r12_t0 >= 30
	r12_t0 += MM[0]


	# new tasks
	r1_t4 = S.Task('r1_t4', length=9, delay_cost=1)
	r1_t4 += alt(MM)
	r1_t4_in = S.Task('r1_t4_in', length=1, delay_cost=1)
	r1_t4_in += alt(MM_in)
	S += r1_t4_in*MM_in[0]<=r1_t4*MM[0]
	r1_t4_mem0 = S.Task('r1_t4_mem0', length=1, delay_cost=1)
	r1_t4_mem0 += MAS_MEM[0]
	S += 7 < r1_t4_mem0
	S += r1_t4_mem0 <= r1_t4

	r1_t4_mem1 = S.Task('r1_t4_mem1', length=1, delay_cost=1)
	r1_t4_mem1 += MAS_MEM[1]
	S += 20 < r1_t4_mem1
	S += r1_t4_mem1 <= r1_t4

	r10 = S.Task('r10', length=2, delay_cost=1)
	r10 += alt(MAS)
	r10_in = S.Task('r10_in', length=1, delay_cost=1)
	r10_in += alt(MAS_in)
	S += r10_in*MAS_in[0]<=r10*MAS[0]

	S += r10_in*MAS_in[1]<=r10*MAS[1]

	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	r10_mem0 += MM_MEM[0]
	S += 30 < r10_mem0
	S += r10_mem0 <= r10

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	r10_mem1 += MM_MEM[1]
	S += 25 < r10_mem1
	S += r10_mem1 <= r10

	r1_t5 = S.Task('r1_t5', length=2, delay_cost=1)
	r1_t5 += alt(MAS)
	r1_t5_in = S.Task('r1_t5_in', length=1, delay_cost=1)
	r1_t5_in += alt(MAS_in)
	S += r1_t5_in*MAS_in[0]<=r1_t5*MAS[0]

	S += r1_t5_in*MAS_in[1]<=r1_t5*MAS[1]

	r1_t5_mem0 = S.Task('r1_t5_mem0', length=1, delay_cost=1)
	r1_t5_mem0 += MM_MEM[0]
	S += 30 < r1_t5_mem0
	S += r1_t5_mem0 <= r1_t5

	r1_t5_mem1 = S.Task('r1_t5_mem1', length=1, delay_cost=1)
	r1_t5_mem1 += MM_MEM[1]
	S += 25 < r1_t5_mem1
	S += r1_t5_mem1 <= r1_t5

	r3_t4 = S.Task('r3_t4', length=9, delay_cost=1)
	r3_t4 += alt(MM)
	r3_t4_in = S.Task('r3_t4_in', length=1, delay_cost=1)
	r3_t4_in += alt(MM_in)
	S += r3_t4_in*MM_in[0]<=r3_t4*MM[0]
	r3_t4_mem0 = S.Task('r3_t4_mem0', length=1, delay_cost=1)
	r3_t4_mem0 += MAS_MEM[2]
	S += 17 < r3_t4_mem0
	S += r3_t4_mem0 <= r3_t4

	r3_t4_mem1 = S.Task('r3_t4_mem1', length=1, delay_cost=1)
	r3_t4_mem1 += MAS_MEM[1]
	S += 2 < r3_t4_mem1
	S += r3_t4_mem1 <= r3_t4

	r30 = S.Task('r30', length=2, delay_cost=1)
	r30 += alt(MAS)
	r30_in = S.Task('r30_in', length=1, delay_cost=1)
	r30_in += alt(MAS_in)
	S += r30_in*MAS_in[0]<=r30*MAS[0]

	S += r30_in*MAS_in[1]<=r30*MAS[1]

	r30_mem0 = S.Task('r30_mem0', length=1, delay_cost=1)
	r30_mem0 += MM_MEM[0]
	S += 21 < r30_mem0
	S += r30_mem0 <= r30

	r30_mem1 = S.Task('r30_mem1', length=1, delay_cost=1)
	r30_mem1 += MM_MEM[1]
	S += 34 < r30_mem1
	S += r30_mem1 <= r30

	r3_t5 = S.Task('r3_t5', length=2, delay_cost=1)
	r3_t5 += alt(MAS)
	r3_t5_in = S.Task('r3_t5_in', length=1, delay_cost=1)
	r3_t5_in += alt(MAS_in)
	S += r3_t5_in*MAS_in[0]<=r3_t5*MAS[0]

	S += r3_t5_in*MAS_in[1]<=r3_t5*MAS[1]

	r3_t5_mem0 = S.Task('r3_t5_mem0', length=1, delay_cost=1)
	r3_t5_mem0 += MM_MEM[0]
	S += 21 < r3_t5_mem0
	S += r3_t5_mem0 <= r3_t5

	r3_t5_mem1 = S.Task('r3_t5_mem1', length=1, delay_cost=1)
	r3_t5_mem1 += MM_MEM[1]
	S += 34 < r3_t5_mem1
	S += r3_t5_mem1 <= r3_t5

	r4_t4 = S.Task('r4_t4', length=9, delay_cost=1)
	r4_t4 += alt(MM)
	r4_t4_in = S.Task('r4_t4_in', length=1, delay_cost=1)
	r4_t4_in += alt(MM_in)
	S += r4_t4_in*MM_in[0]<=r4_t4*MM[0]
	r4_t4_mem0 = S.Task('r4_t4_mem0', length=1, delay_cost=1)
	r4_t4_mem0 += MAS_MEM[2]
	S += 10 < r4_t4_mem0
	S += r4_t4_mem0 <= r4_t4

	r4_t4_mem1 = S.Task('r4_t4_mem1', length=1, delay_cost=1)
	r4_t4_mem1 += MAS_MEM[1]
	S += 6 < r4_t4_mem1
	S += r4_t4_mem1 <= r4_t4

	r40 = S.Task('r40', length=2, delay_cost=1)
	r40 += alt(MAS)
	r40_in = S.Task('r40_in', length=1, delay_cost=1)
	r40_in += alt(MAS_in)
	S += r40_in*MAS_in[0]<=r40*MAS[0]

	S += r40_in*MAS_in[1]<=r40*MAS[1]

	r40_mem0 = S.Task('r40_mem0', length=1, delay_cost=1)
	r40_mem0 += MM_MEM[0]
	S += 23 < r40_mem0
	S += r40_mem0 <= r40

	r40_mem1 = S.Task('r40_mem1', length=1, delay_cost=1)
	r40_mem1 += MM_MEM[1]
	S += 29 < r40_mem1
	S += r40_mem1 <= r40

	r4_t5 = S.Task('r4_t5', length=2, delay_cost=1)
	r4_t5 += alt(MAS)
	r4_t5_in = S.Task('r4_t5_in', length=1, delay_cost=1)
	r4_t5_in += alt(MAS_in)
	S += r4_t5_in*MAS_in[0]<=r4_t5*MAS[0]

	S += r4_t5_in*MAS_in[1]<=r4_t5*MAS[1]

	r4_t5_mem0 = S.Task('r4_t5_mem0', length=1, delay_cost=1)
	r4_t5_mem0 += MM_MEM[0]
	S += 23 < r4_t5_mem0
	S += r4_t5_mem0 <= r4_t5

	r4_t5_mem1 = S.Task('r4_t5_mem1', length=1, delay_cost=1)
	r4_t5_mem1 += MM_MEM[1]
	S += 29 < r4_t5_mem1
	S += r4_t5_mem1 <= r4_t5

	r5_t4 = S.Task('r5_t4', length=9, delay_cost=1)
	r5_t4 += alt(MM)
	r5_t4_in = S.Task('r5_t4_in', length=1, delay_cost=1)
	r5_t4_in += alt(MM_in)
	S += r5_t4_in*MM_in[0]<=r5_t4*MM[0]
	r5_t4_mem0 = S.Task('r5_t4_mem0', length=1, delay_cost=1)
	r5_t4_mem0 += MAS_MEM[2]
	S += 26 < r5_t4_mem0
	S += r5_t4_mem0 <= r5_t4

	r5_t4_mem1 = S.Task('r5_t4_mem1', length=1, delay_cost=1)
	r5_t4_mem1 += MAS_MEM[1]
	S += 28 < r5_t4_mem1
	S += r5_t4_mem1 <= r5_t4

	r50 = S.Task('r50', length=2, delay_cost=1)
	r50 += alt(MAS)
	r50_in = S.Task('r50_in', length=1, delay_cost=1)
	r50_in += alt(MAS_in)
	S += r50_in*MAS_in[0]<=r50*MAS[0]

	S += r50_in*MAS_in[1]<=r50*MAS[1]

	r50_mem0 = S.Task('r50_mem0', length=1, delay_cost=1)
	r50_mem0 += MM_MEM[0]
	S += 12 < r50_mem0
	S += r50_mem0 <= r50

	r50_mem1 = S.Task('r50_mem1', length=1, delay_cost=1)
	r50_mem1 += MM_MEM[1]
	S += 28 < r50_mem1
	S += r50_mem1 <= r50

	r5_t5 = S.Task('r5_t5', length=2, delay_cost=1)
	r5_t5 += alt(MAS)
	r5_t5_in = S.Task('r5_t5_in', length=1, delay_cost=1)
	r5_t5_in += alt(MAS_in)
	S += r5_t5_in*MAS_in[0]<=r5_t5*MAS[0]

	S += r5_t5_in*MAS_in[1]<=r5_t5*MAS[1]

	r5_t5_mem0 = S.Task('r5_t5_mem0', length=1, delay_cost=1)
	r5_t5_mem0 += MM_MEM[0]
	S += 12 < r5_t5_mem0
	S += r5_t5_mem0 <= r5_t5

	r5_t5_mem1 = S.Task('r5_t5_mem1', length=1, delay_cost=1)
	r5_t5_mem1 += MM_MEM[1]
	S += 28 < r5_t5_mem1
	S += r5_t5_mem1 <= r5_t5

	r6_t4 = S.Task('r6_t4', length=9, delay_cost=1)
	r6_t4 += alt(MM)
	r6_t4_in = S.Task('r6_t4_in', length=1, delay_cost=1)
	r6_t4_in += alt(MM_in)
	S += r6_t4_in*MM_in[0]<=r6_t4*MM[0]
	r6_t4_mem0 = S.Task('r6_t4_mem0', length=1, delay_cost=1)
	r6_t4_mem0 += MAS_MEM[0]
	S += 24 < r6_t4_mem0
	S += r6_t4_mem0 <= r6_t4

	r6_t4_mem1 = S.Task('r6_t4_mem1', length=1, delay_cost=1)
	r6_t4_mem1 += MAS_MEM[1]
	S += 8 < r6_t4_mem1
	S += r6_t4_mem1 <= r6_t4

	r60 = S.Task('r60', length=2, delay_cost=1)
	r60 += alt(MAS)
	r60_in = S.Task('r60_in', length=1, delay_cost=1)
	r60_in += alt(MAS_in)
	S += r60_in*MAS_in[0]<=r60*MAS[0]

	S += r60_in*MAS_in[1]<=r60*MAS[1]

	r60_mem0 = S.Task('r60_mem0', length=1, delay_cost=1)
	r60_mem0 += MM_MEM[0]
	S += 32 < r60_mem0
	S += r60_mem0 <= r60

	r60_mem1 = S.Task('r60_mem1', length=1, delay_cost=1)
	r60_mem1 += MM_MEM[1]
	S += 18 < r60_mem1
	S += r60_mem1 <= r60

	r6_t5 = S.Task('r6_t5', length=2, delay_cost=1)
	r6_t5 += alt(MAS)
	r6_t5_in = S.Task('r6_t5_in', length=1, delay_cost=1)
	r6_t5_in += alt(MAS_in)
	S += r6_t5_in*MAS_in[0]<=r6_t5*MAS[0]

	S += r6_t5_in*MAS_in[1]<=r6_t5*MAS[1]

	r6_t5_mem0 = S.Task('r6_t5_mem0', length=1, delay_cost=1)
	r6_t5_mem0 += MM_MEM[0]
	S += 32 < r6_t5_mem0
	S += r6_t5_mem0 <= r6_t5

	r6_t5_mem1 = S.Task('r6_t5_mem1', length=1, delay_cost=1)
	r6_t5_mem1 += MM_MEM[1]
	S += 18 < r6_t5_mem1
	S += r6_t5_mem1 <= r6_t5

	r12_t4 = S.Task('r12_t4', length=9, delay_cost=1)
	r12_t4 += alt(MM)
	r12_t4_in = S.Task('r12_t4_in', length=1, delay_cost=1)
	r12_t4_in += alt(MM_in)
	S += r12_t4_in*MM_in[0]<=r12_t4*MM[0]
	r12_t4_mem0 = S.Task('r12_t4_mem0', length=1, delay_cost=1)
	r12_t4_mem0 += MAS_MEM[0]
	S += 19 < r12_t4_mem0
	S += r12_t4_mem0 <= r12_t4

	r12_t4_mem1 = S.Task('r12_t4_mem1', length=1, delay_cost=1)
	r12_t4_mem1 += MAS_MEM[3]
	S += 12 < r12_t4_mem1
	S += r12_t4_mem1 <= r12_t4

	r120 = S.Task('r120', length=2, delay_cost=1)
	r120 += alt(MAS)
	r120_in = S.Task('r120_in', length=1, delay_cost=1)
	r120_in += alt(MAS_in)
	S += r120_in*MAS_in[0]<=r120*MAS[0]

	S += r120_in*MAS_in[1]<=r120*MAS[1]

	r120_mem0 = S.Task('r120_mem0', length=1, delay_cost=1)
	r120_mem0 += MM_MEM[0]
	S += 38 < r120_mem0
	S += r120_mem0 <= r120

	r120_mem1 = S.Task('r120_mem1', length=1, delay_cost=1)
	r120_mem1 += MM_MEM[1]
	S += 11 < r120_mem1
	S += r120_mem1 <= r120

	r12_t5 = S.Task('r12_t5', length=2, delay_cost=1)
	r12_t5 += alt(MAS)
	r12_t5_in = S.Task('r12_t5_in', length=1, delay_cost=1)
	r12_t5_in += alt(MAS_in)
	S += r12_t5_in*MAS_in[0]<=r12_t5*MAS[0]

	S += r12_t5_in*MAS_in[1]<=r12_t5*MAS[1]

	r12_t5_mem0 = S.Task('r12_t5_mem0', length=1, delay_cost=1)
	r12_t5_mem0 += MM_MEM[0]
	S += 38 < r12_t5_mem0
	S += r12_t5_mem0 <= r12_t5

	r12_t5_mem1 = S.Task('r12_t5_mem1', length=1, delay_cost=1)
	r12_t5_mem1 += MM_MEM[1]
	S += 11 < r12_t5_mem1
	S += r12_t5_mem1 <= r12_t5

	r13_t4 = S.Task('r13_t4', length=9, delay_cost=1)
	r13_t4 += alt(MM)
	r13_t4_in = S.Task('r13_t4_in', length=1, delay_cost=1)
	r13_t4_in += alt(MM_in)
	S += r13_t4_in*MM_in[0]<=r13_t4*MM[0]
	r13_t4_mem0 = S.Task('r13_t4_mem0', length=1, delay_cost=1)
	r13_t4_mem0 += MAS_MEM[0]
	S += 9 < r13_t4_mem0
	S += r13_t4_mem0 <= r13_t4

	r13_t4_mem1 = S.Task('r13_t4_mem1', length=1, delay_cost=1)
	r13_t4_mem1 += MAS_MEM[3]
	S += 13 < r13_t4_mem1
	S += r13_t4_mem1 <= r13_t4

	r130 = S.Task('r130', length=2, delay_cost=1)
	r130 += alt(MAS)
	r130_in = S.Task('r130_in', length=1, delay_cost=1)
	r130_in += alt(MAS_in)
	S += r130_in*MAS_in[0]<=r130*MAS[0]

	S += r130_in*MAS_in[1]<=r130*MAS[1]

	r130_mem0 = S.Task('r130_mem0', length=1, delay_cost=1)
	r130_mem0 += MM_MEM[0]
	S += 37 < r130_mem0
	S += r130_mem0 <= r130

	r130_mem1 = S.Task('r130_mem1', length=1, delay_cost=1)
	r130_mem1 += MM_MEM[1]
	S += 36 < r130_mem1
	S += r130_mem1 <= r130

	r13_t5 = S.Task('r13_t5', length=2, delay_cost=1)
	r13_t5 += alt(MAS)
	r13_t5_in = S.Task('r13_t5_in', length=1, delay_cost=1)
	r13_t5_in += alt(MAS_in)
	S += r13_t5_in*MAS_in[0]<=r13_t5*MAS[0]

	S += r13_t5_in*MAS_in[1]<=r13_t5*MAS[1]

	r13_t5_mem0 = S.Task('r13_t5_mem0', length=1, delay_cost=1)
	r13_t5_mem0 += MM_MEM[0]
	S += 37 < r13_t5_mem0
	S += r13_t5_mem0 <= r13_t5

	r13_t5_mem1 = S.Task('r13_t5_mem1', length=1, delay_cost=1)
	r13_t5_mem1 += MM_MEM[1]
	S += 36 < r13_t5_mem1
	S += r13_t5_mem1 <= r13_t5

	r11 = S.Task('r11', length=2, delay_cost=1)
	r11 += alt(MAS)
	r11_in = S.Task('r11_in', length=1, delay_cost=1)
	r11_in += alt(MAS_in)
	S += r11_in*MAS_in[0]<=r11*MAS[0]

	S += r11_in*MAS_in[1]<=r11*MAS[1]

	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	r11_mem0 += alt(MM_MEM)
	S += (r1_t4*MM[0])-1 < r11_mem0*MM_MEM[0]
	S += r11_mem0 <= r11

	r11_mem1 = S.Task('r11_mem1', length=1, delay_cost=1)
	r11_mem1 += alt(MAS_MEM)
	S += (r1_t5*MAS[0])-1 < r11_mem1*MAS_MEM[1]
	S += (r1_t5*MAS[1])-1 < r11_mem1*MAS_MEM[3]
	S += r11_mem1 <= r11

	r20 = S.Task('r20', length=2, delay_cost=1)
	r20 += alt(MAS)
	r20_in = S.Task('r20_in', length=1, delay_cost=1)
	r20_in += alt(MAS_in)
	S += r20_in*MAS_in[0]<=r20*MAS[0]

	S += r20_in*MAS_in[1]<=r20*MAS[1]

	r20_mem0 = S.Task('r20_mem0', length=1, delay_cost=1)
	r20_mem0 += alt(MAS_MEM)
	S += (r10*MAS[0])-1 < r20_mem0*MAS_MEM[0]
	S += (r10*MAS[1])-1 < r20_mem0*MAS_MEM[2]
	S += r20_mem0 <= r20

	r20_mem1 = S.Task('r20_mem1', length=1, delay_cost=1)
	r20_mem1 += alt(MAS_MEM)
	S += (r10*MAS[0])-1 < r20_mem1*MAS_MEM[1]
	S += (r10*MAS[1])-1 < r20_mem1*MAS_MEM[3]
	S += r20_mem1 <= r20

	r31 = S.Task('r31', length=2, delay_cost=1)
	r31 += alt(MAS)
	r31_in = S.Task('r31_in', length=1, delay_cost=1)
	r31_in += alt(MAS_in)
	S += r31_in*MAS_in[0]<=r31*MAS[0]

	S += r31_in*MAS_in[1]<=r31*MAS[1]

	r31_mem0 = S.Task('r31_mem0', length=1, delay_cost=1)
	r31_mem0 += alt(MM_MEM)
	S += (r3_t4*MM[0])-1 < r31_mem0*MM_MEM[0]
	S += r31_mem0 <= r31

	r31_mem1 = S.Task('r31_mem1', length=1, delay_cost=1)
	r31_mem1 += alt(MAS_MEM)
	S += (r3_t5*MAS[0])-1 < r31_mem1*MAS_MEM[1]
	S += (r3_t5*MAS[1])-1 < r31_mem1*MAS_MEM[3]
	S += r31_mem1 <= r31

	r41 = S.Task('r41', length=2, delay_cost=1)
	r41 += alt(MAS)
	r41_in = S.Task('r41_in', length=1, delay_cost=1)
	r41_in += alt(MAS_in)
	S += r41_in*MAS_in[0]<=r41*MAS[0]

	S += r41_in*MAS_in[1]<=r41*MAS[1]

	r41_mem0 = S.Task('r41_mem0', length=1, delay_cost=1)
	r41_mem0 += alt(MM_MEM)
	S += (r4_t4*MM[0])-1 < r41_mem0*MM_MEM[0]
	S += r41_mem0 <= r41

	r41_mem1 = S.Task('r41_mem1', length=1, delay_cost=1)
	r41_mem1 += alt(MAS_MEM)
	S += (r4_t5*MAS[0])-1 < r41_mem1*MAS_MEM[1]
	S += (r4_t5*MAS[1])-1 < r41_mem1*MAS_MEM[3]
	S += r41_mem1 <= r41

	r51 = S.Task('r51', length=2, delay_cost=1)
	r51 += alt(MAS)
	r51_in = S.Task('r51_in', length=1, delay_cost=1)
	r51_in += alt(MAS_in)
	S += r51_in*MAS_in[0]<=r51*MAS[0]

	S += r51_in*MAS_in[1]<=r51*MAS[1]

	r51_mem0 = S.Task('r51_mem0', length=1, delay_cost=1)
	r51_mem0 += alt(MM_MEM)
	S += (r5_t4*MM[0])-1 < r51_mem0*MM_MEM[0]
	S += r51_mem0 <= r51

	r51_mem1 = S.Task('r51_mem1', length=1, delay_cost=1)
	r51_mem1 += alt(MAS_MEM)
	S += (r5_t5*MAS[0])-1 < r51_mem1*MAS_MEM[1]
	S += (r5_t5*MAS[1])-1 < r51_mem1*MAS_MEM[3]
	S += r51_mem1 <= r51

	r61 = S.Task('r61', length=2, delay_cost=1)
	r61 += alt(MAS)
	r61_in = S.Task('r61_in', length=1, delay_cost=1)
	r61_in += alt(MAS_in)
	S += r61_in*MAS_in[0]<=r61*MAS[0]

	S += r61_in*MAS_in[1]<=r61*MAS[1]

	r61_mem0 = S.Task('r61_mem0', length=1, delay_cost=1)
	r61_mem0 += alt(MM_MEM)
	S += (r6_t4*MM[0])-1 < r61_mem0*MM_MEM[0]
	S += r61_mem0 <= r61

	r61_mem1 = S.Task('r61_mem1', length=1, delay_cost=1)
	r61_mem1 += alt(MAS_MEM)
	S += (r6_t5*MAS[0])-1 < r61_mem1*MAS_MEM[1]
	S += (r6_t5*MAS[1])-1 < r61_mem1*MAS_MEM[3]
	S += r61_mem1 <= r61

	r70 = S.Task('r70', length=2, delay_cost=1)
	r70 += alt(MAS)
	r70_in = S.Task('r70_in', length=1, delay_cost=1)
	r70_in += alt(MAS_in)
	S += r70_in*MAS_in[0]<=r70*MAS[0]

	S += r70_in*MAS_in[1]<=r70*MAS[1]

	r70_mem0 = S.Task('r70_mem0', length=1, delay_cost=1)
	r70_mem0 += alt(MAS_MEM)
	S += (r50*MAS[0])-1 < r70_mem0*MAS_MEM[0]
	S += (r50*MAS[1])-1 < r70_mem0*MAS_MEM[2]
	S += r70_mem0 <= r70

	r70_mem1 = S.Task('r70_mem1', length=1, delay_cost=1)
	r70_mem1 += alt(MAS_MEM)
	S += (r60*MAS[0])-1 < r70_mem1*MAS_MEM[1]
	S += (r60*MAS[1])-1 < r70_mem1*MAS_MEM[3]
	S += r70_mem1 <= r70

	r80 = S.Task('r80', length=2, delay_cost=1)
	r80 += alt(MAS)
	r80_in = S.Task('r80_in', length=1, delay_cost=1)
	r80_in += alt(MAS_in)
	S += r80_in*MAS_in[0]<=r80*MAS[0]

	S += r80_in*MAS_in[1]<=r80*MAS[1]

	r80_mem0 = S.Task('r80_mem0', length=1, delay_cost=1)
	r80_mem0 += MAIN_MEM_r[0]
	S += r80_mem0 <= r80

	r80_mem1 = S.Task('r80_mem1', length=1, delay_cost=1)
	r80_mem1 += alt(MAS_MEM)
	S += (r40*MAS[0])-1 < r80_mem1*MAS_MEM[1]
	S += (r40*MAS[1])-1 < r80_mem1*MAS_MEM[3]
	S += r80_mem1 <= r80

	r100 = S.Task('r100', length=2, delay_cost=1)
	r100 += alt(MAS)
	r100_in = S.Task('r100_in', length=1, delay_cost=1)
	r100_in += alt(MAS_in)
	S += r100_in*MAS_in[0]<=r100*MAS[0]

	S += r100_in*MAS_in[1]<=r100*MAS[1]

	r100_mem0 = S.Task('r100_mem0', length=1, delay_cost=1)
	r100_mem0 += MAIN_MEM_r[0]
	S += r100_mem0 <= r100

	r100_mem1 = S.Task('r100_mem1', length=1, delay_cost=1)
	r100_mem1 += alt(MAS_MEM)
	S += (r40*MAS[0])-1 < r100_mem1*MAS_MEM[1]
	S += (r40*MAS[1])-1 < r100_mem1*MAS_MEM[3]
	S += r100_mem1 <= r100

	r121 = S.Task('r121', length=2, delay_cost=1)
	r121 += alt(MAS)
	r121_in = S.Task('r121_in', length=1, delay_cost=1)
	r121_in += alt(MAS_in)
	S += r121_in*MAS_in[0]<=r121*MAS[0]

	S += r121_in*MAS_in[1]<=r121*MAS[1]

	r121_mem0 = S.Task('r121_mem0', length=1, delay_cost=1)
	r121_mem0 += alt(MM_MEM)
	S += (r12_t4*MM[0])-1 < r121_mem0*MM_MEM[0]
	S += r121_mem0 <= r121

	r121_mem1 = S.Task('r121_mem1', length=1, delay_cost=1)
	r121_mem1 += alt(MAS_MEM)
	S += (r12_t5*MAS[0])-1 < r121_mem1*MAS_MEM[1]
	S += (r12_t5*MAS[1])-1 < r121_mem1*MAS_MEM[3]
	S += r121_mem1 <= r121

	r131 = S.Task('r131', length=2, delay_cost=1)
	r131 += alt(MAS)
	r131_in = S.Task('r131_in', length=1, delay_cost=1)
	r131_in += alt(MAS_in)
	S += r131_in*MAS_in[0]<=r131*MAS[0]

	S += r131_in*MAS_in[1]<=r131*MAS[1]

	r131_mem0 = S.Task('r131_mem0', length=1, delay_cost=1)
	r131_mem0 += alt(MM_MEM)
	S += (r13_t4*MM[0])-1 < r131_mem0*MM_MEM[0]
	S += r131_mem0 <= r131

	r131_mem1 = S.Task('r131_mem1', length=1, delay_cost=1)
	r131_mem1 += alt(MAS_MEM)
	S += (r13_t5*MAS[0])-1 < r131_mem1*MAS_MEM[1]
	S += (r13_t5*MAS[1])-1 < r131_mem1*MAS_MEM[3]
	S += r131_mem1 <= r131

	r21 = S.Task('r21', length=2, delay_cost=1)
	r21 += alt(MAS)
	r21_in = S.Task('r21_in', length=1, delay_cost=1)
	r21_in += alt(MAS_in)
	S += r21_in*MAS_in[0]<=r21*MAS[0]

	S += r21_in*MAS_in[1]<=r21*MAS[1]

	r21_mem0 = S.Task('r21_mem0', length=1, delay_cost=1)
	r21_mem0 += alt(MAS_MEM)
	S += (r11*MAS[0])-1 < r21_mem0*MAS_MEM[0]
	S += (r11*MAS[1])-1 < r21_mem0*MAS_MEM[2]
	S += r21_mem0 <= r21

	r21_mem1 = S.Task('r21_mem1', length=1, delay_cost=1)
	r21_mem1 += alt(MAS_MEM)
	S += (r11*MAS[0])-1 < r21_mem1*MAS_MEM[1]
	S += (r11*MAS[1])-1 < r21_mem1*MAS_MEM[3]
	S += r21_mem1 <= r21

	r71 = S.Task('r71', length=2, delay_cost=1)
	r71 += alt(MAS)
	r71_in = S.Task('r71_in', length=1, delay_cost=1)
	r71_in += alt(MAS_in)
	S += r71_in*MAS_in[0]<=r71*MAS[0]

	S += r71_in*MAS_in[1]<=r71*MAS[1]

	r71_mem0 = S.Task('r71_mem0', length=1, delay_cost=1)
	r71_mem0 += alt(MAS_MEM)
	S += (r51*MAS[0])-1 < r71_mem0*MAS_MEM[0]
	S += (r51*MAS[1])-1 < r71_mem0*MAS_MEM[2]
	S += r71_mem0 <= r71

	r71_mem1 = S.Task('r71_mem1', length=1, delay_cost=1)
	r71_mem1 += alt(MAS_MEM)
	S += (r61*MAS[0])-1 < r71_mem1*MAS_MEM[1]
	S += (r61*MAS[1])-1 < r71_mem1*MAS_MEM[3]
	S += r71_mem1 <= r71

	r81 = S.Task('r81', length=2, delay_cost=1)
	r81 += alt(MAS)
	r81_in = S.Task('r81_in', length=1, delay_cost=1)
	r81_in += alt(MAS_in)
	S += r81_in*MAS_in[0]<=r81*MAS[0]

	S += r81_in*MAS_in[1]<=r81*MAS[1]

	r81_mem0 = S.Task('r81_mem0', length=1, delay_cost=1)
	r81_mem0 += MAIN_MEM_r[0]
	S += r81_mem0 <= r81

	r81_mem1 = S.Task('r81_mem1', length=1, delay_cost=1)
	r81_mem1 += alt(MAS_MEM)
	S += (r41*MAS[0])-1 < r81_mem1*MAS_MEM[1]
	S += (r41*MAS[1])-1 < r81_mem1*MAS_MEM[3]
	S += r81_mem1 <= r81

	r9_t0 = S.Task('r9_t0', length=9, delay_cost=1)
	r9_t0 += alt(MM)
	r9_t0_in = S.Task('r9_t0_in', length=1, delay_cost=1)
	r9_t0_in += alt(MM_in)
	S += r9_t0_in*MM_in[0]<=r9_t0*MM[0]
	r9_t0_mem0 = S.Task('r9_t0_mem0', length=1, delay_cost=1)
	r9_t0_mem0 += MAIN_MEM_r[0]
	S += r9_t0_mem0 <= r9_t0

	r9_t0_mem1 = S.Task('r9_t0_mem1', length=1, delay_cost=1)
	r9_t0_mem1 += alt(MAS_MEM)
	S += (r70*MAS[0])-1 < r9_t0_mem1*MAS_MEM[1]
	S += (r70*MAS[1])-1 < r9_t0_mem1*MAS_MEM[3]
	S += r9_t0_mem1 <= r9_t0

	r101 = S.Task('r101', length=2, delay_cost=1)
	r101 += alt(MAS)
	r101_in = S.Task('r101_in', length=1, delay_cost=1)
	r101_in += alt(MAS_in)
	S += r101_in*MAS_in[0]<=r101*MAS[0]

	S += r101_in*MAS_in[1]<=r101*MAS[1]

	r101_mem0 = S.Task('r101_mem0', length=1, delay_cost=1)
	r101_mem0 += MAIN_MEM_r[0]
	S += r101_mem0 <= r101

	r101_mem1 = S.Task('r101_mem1', length=1, delay_cost=1)
	r101_mem1 += alt(MAS_MEM)
	S += (r41*MAS[0])-1 < r101_mem1*MAS_MEM[1]
	S += (r41*MAS[1])-1 < r101_mem1*MAS_MEM[3]
	S += r101_mem1 <= r101

	X_new_t0 = S.Task('X_new_t0', length=9, delay_cost=1)
	X_new_t0 += alt(MM)
	X_new_t0_in = S.Task('X_new_t0_in', length=1, delay_cost=1)
	X_new_t0_in += alt(MM_in)
	S += X_new_t0_in*MM_in[0]<=X_new_t0*MM[0]
	X_new_t0_mem0 = S.Task('X_new_t0_mem0', length=1, delay_cost=1)
	X_new_t0_mem0 += alt(MAS_MEM)
	S += (r20*MAS[0])-1 < X_new_t0_mem0*MAS_MEM[0]
	S += (r20*MAS[1])-1 < X_new_t0_mem0*MAS_MEM[2]
	S += X_new_t0_mem0 <= X_new_t0

	X_new_t0_mem1 = S.Task('X_new_t0_mem1', length=1, delay_cost=1)
	X_new_t0_mem1 += alt(MAS_MEM)
	S += (r120*MAS[0])-1 < X_new_t0_mem1*MAS_MEM[1]
	S += (r120*MAS[1])-1 < X_new_t0_mem1*MAS_MEM[3]
	S += X_new_t0_mem1 <= X_new_t0

	X_new_t3 = S.Task('X_new_t3', length=2, delay_cost=1)
	X_new_t3 += alt(MAS)
	X_new_t3_in = S.Task('X_new_t3_in', length=1, delay_cost=1)
	X_new_t3_in += alt(MAS_in)
	S += X_new_t3_in*MAS_in[0]<=X_new_t3*MAS[0]

	S += X_new_t3_in*MAS_in[1]<=X_new_t3*MAS[1]

	X_new_t3_mem0 = S.Task('X_new_t3_mem0', length=1, delay_cost=1)
	X_new_t3_mem0 += alt(MAS_MEM)
	S += (r120*MAS[0])-1 < X_new_t3_mem0*MAS_MEM[0]
	S += (r120*MAS[1])-1 < X_new_t3_mem0*MAS_MEM[2]
	S += X_new_t3_mem0 <= X_new_t3

	X_new_t3_mem1 = S.Task('X_new_t3_mem1', length=1, delay_cost=1)
	X_new_t3_mem1 += alt(MAS_MEM)
	S += (r121*MAS[0])-1 < X_new_t3_mem1*MAS_MEM[1]
	S += (r121*MAS[1])-1 < X_new_t3_mem1*MAS_MEM[3]
	S += X_new_t3_mem1 <= X_new_t3

	r14_t0 = S.Task('r14_t0', length=9, delay_cost=1)
	r14_t0 += alt(MM)
	r14_t0_in = S.Task('r14_t0_in', length=1, delay_cost=1)
	r14_t0_in += alt(MM_in)
	S += r14_t0_in*MM_in[0]<=r14_t0*MM[0]
	r14_t0_mem0 = S.Task('r14_t0_mem0', length=1, delay_cost=1)
	r14_t0_mem0 += alt(MAS_MEM)
	S += (r20*MAS[0])-1 < r14_t0_mem0*MAS_MEM[0]
	S += (r20*MAS[1])-1 < r14_t0_mem0*MAS_MEM[2]
	S += r14_t0_mem0 <= r14_t0

	r14_t0_mem1 = S.Task('r14_t0_mem1', length=1, delay_cost=1)
	r14_t0_mem1 += alt(MAS_MEM)
	S += (r30*MAS[0])-1 < r14_t0_mem1*MAS_MEM[1]
	S += (r30*MAS[1])-1 < r14_t0_mem1*MAS_MEM[3]
	S += r14_t0_mem1 <= r14_t0

	r14_t3 = S.Task('r14_t3', length=2, delay_cost=1)
	r14_t3 += alt(MAS)
	r14_t3_in = S.Task('r14_t3_in', length=1, delay_cost=1)
	r14_t3_in += alt(MAS_in)
	S += r14_t3_in*MAS_in[0]<=r14_t3*MAS[0]

	S += r14_t3_in*MAS_in[1]<=r14_t3*MAS[1]

	r14_t3_mem0 = S.Task('r14_t3_mem0', length=1, delay_cost=1)
	r14_t3_mem0 += alt(MAS_MEM)
	S += (r30*MAS[0])-1 < r14_t3_mem0*MAS_MEM[0]
	S += (r30*MAS[1])-1 < r14_t3_mem0*MAS_MEM[2]
	S += r14_t3_mem0 <= r14_t3

	r14_t3_mem1 = S.Task('r14_t3_mem1', length=1, delay_cost=1)
	r14_t3_mem1 += alt(MAS_MEM)
	S += (r31*MAS[0])-1 < r14_t3_mem1*MAS_MEM[1]
	S += (r31*MAS[1])-1 < r14_t3_mem1*MAS_MEM[3]
	S += r14_t3_mem1 <= r14_t3

	Z_new_t0 = S.Task('Z_new_t0', length=9, delay_cost=1)
	Z_new_t0 += alt(MM)
	Z_new_t0_in = S.Task('Z_new_t0_in', length=1, delay_cost=1)
	Z_new_t0_in += alt(MM_in)
	S += Z_new_t0_in*MM_in[0]<=Z_new_t0*MM[0]
	Z_new_t0_mem0 = S.Task('Z_new_t0_mem0', length=1, delay_cost=1)
	Z_new_t0_mem0 += alt(MAS_MEM)
	S += (r20*MAS[0])-1 < Z_new_t0_mem0*MAS_MEM[0]
	S += (r20*MAS[1])-1 < Z_new_t0_mem0*MAS_MEM[2]
	S += Z_new_t0_mem0 <= Z_new_t0

	Z_new_t0_mem1 = S.Task('Z_new_t0_mem1', length=1, delay_cost=1)
	Z_new_t0_mem1 += alt(MAS_MEM)
	S += (r130*MAS[0])-1 < Z_new_t0_mem1*MAS_MEM[1]
	S += (r130*MAS[1])-1 < Z_new_t0_mem1*MAS_MEM[3]
	S += Z_new_t0_mem1 <= Z_new_t0

	Z_new_t3 = S.Task('Z_new_t3', length=2, delay_cost=1)
	Z_new_t3 += alt(MAS)
	Z_new_t3_in = S.Task('Z_new_t3_in', length=1, delay_cost=1)
	Z_new_t3_in += alt(MAS_in)
	S += Z_new_t3_in*MAS_in[0]<=Z_new_t3*MAS[0]

	S += Z_new_t3_in*MAS_in[1]<=Z_new_t3*MAS[1]

	Z_new_t3_mem0 = S.Task('Z_new_t3_mem0', length=1, delay_cost=1)
	Z_new_t3_mem0 += alt(MAS_MEM)
	S += (r130*MAS[0])-1 < Z_new_t3_mem0*MAS_MEM[0]
	S += (r130*MAS[1])-1 < Z_new_t3_mem0*MAS_MEM[2]
	S += Z_new_t3_mem0 <= Z_new_t3

	Z_new_t3_mem1 = S.Task('Z_new_t3_mem1', length=1, delay_cost=1)
	Z_new_t3_mem1 += alt(MAS_MEM)
	S += (r131*MAS[0])-1 < Z_new_t3_mem1*MAS_MEM[1]
	S += (r131*MAS[1])-1 < Z_new_t3_mem1*MAS_MEM[3]
	S += Z_new_t3_mem1 <= Z_new_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM1_stage2MAS2/EP2_YRECOVER/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution
