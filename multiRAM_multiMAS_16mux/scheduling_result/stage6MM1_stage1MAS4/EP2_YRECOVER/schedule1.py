from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 151
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
	r6_t1_in = S.Task('r6_t1_in', length=1, delay_cost=1)
	S += r6_t1_in >= 0
	r6_t1_in += MM_in[0]

	r6_t1_mem0 = S.Task('r6_t1_mem0', length=1, delay_cost=1)
	S += r6_t1_mem0 >= 0
	r6_t1_mem0 += MAIN_MEM_r[0]

	r6_t1_mem1 = S.Task('r6_t1_mem1', length=1, delay_cost=1)
	S += r6_t1_mem1 >= 0
	r6_t1_mem1 += MAIN_MEM_r[1]

	r1_t0_in = S.Task('r1_t0_in', length=1, delay_cost=1)
	S += r1_t0_in >= 1
	r1_t0_in += MM_in[0]

	r1_t0_mem0 = S.Task('r1_t0_mem0', length=1, delay_cost=1)
	S += r1_t0_mem0 >= 1
	r1_t0_mem0 += MAIN_MEM_r[0]

	r1_t0_mem1 = S.Task('r1_t0_mem1', length=1, delay_cost=1)
	S += r1_t0_mem1 >= 1
	r1_t0_mem1 += MAIN_MEM_r[1]

	r6_t1 = S.Task('r6_t1', length=6, delay_cost=1)
	S += r6_t1 >= 1
	r6_t1 += MM[0]

	r1_t0 = S.Task('r1_t0', length=6, delay_cost=1)
	S += r1_t0 >= 2
	r1_t0 += MM[0]

	r1_t1_in = S.Task('r1_t1_in', length=1, delay_cost=1)
	S += r1_t1_in >= 2
	r1_t1_in += MM_in[0]

	r1_t1_mem0 = S.Task('r1_t1_mem0', length=1, delay_cost=1)
	S += r1_t1_mem0 >= 2
	r1_t1_mem0 += MAIN_MEM_r[0]

	r1_t1_mem1 = S.Task('r1_t1_mem1', length=1, delay_cost=1)
	S += r1_t1_mem1 >= 2
	r1_t1_mem1 += MAIN_MEM_r[1]

	r1_t1 = S.Task('r1_t1', length=6, delay_cost=1)
	S += r1_t1 >= 3
	r1_t1 += MM[0]

	r3_t1_in = S.Task('r3_t1_in', length=1, delay_cost=1)
	S += r3_t1_in >= 3
	r3_t1_in += MM_in[0]

	r3_t1_mem0 = S.Task('r3_t1_mem0', length=1, delay_cost=1)
	S += r3_t1_mem0 >= 3
	r3_t1_mem0 += MAIN_MEM_r[0]

	r3_t1_mem1 = S.Task('r3_t1_mem1', length=1, delay_cost=1)
	S += r3_t1_mem1 >= 3
	r3_t1_mem1 += MAIN_MEM_r[1]

	r13_t1_in = S.Task('r13_t1_in', length=1, delay_cost=1)
	S += r13_t1_in >= 4
	r13_t1_in += MM_in[0]

	r13_t1_mem0 = S.Task('r13_t1_mem0', length=1, delay_cost=1)
	S += r13_t1_mem0 >= 4
	r13_t1_mem0 += MAIN_MEM_r[0]

	r13_t1_mem1 = S.Task('r13_t1_mem1', length=1, delay_cost=1)
	S += r13_t1_mem1 >= 4
	r13_t1_mem1 += MAIN_MEM_r[1]

	r3_t1 = S.Task('r3_t1', length=6, delay_cost=1)
	S += r3_t1 >= 4
	r3_t1 += MM[0]

	r13_t1 = S.Task('r13_t1', length=6, delay_cost=1)
	S += r13_t1 >= 5
	r13_t1 += MM[0]

	r3_t0_in = S.Task('r3_t0_in', length=1, delay_cost=1)
	S += r3_t0_in >= 5
	r3_t0_in += MM_in[0]

	r3_t0_mem0 = S.Task('r3_t0_mem0', length=1, delay_cost=1)
	S += r3_t0_mem0 >= 5
	r3_t0_mem0 += MAIN_MEM_r[0]

	r3_t0_mem1 = S.Task('r3_t0_mem1', length=1, delay_cost=1)
	S += r3_t0_mem1 >= 5
	r3_t0_mem1 += MAIN_MEM_r[1]

	r3_t0 = S.Task('r3_t0', length=6, delay_cost=1)
	S += r3_t0 >= 6
	r3_t0 += MM[0]

	r5_t1_in = S.Task('r5_t1_in', length=1, delay_cost=1)
	S += r5_t1_in >= 6
	r5_t1_in += MM_in[0]

	r5_t1_mem0 = S.Task('r5_t1_mem0', length=1, delay_cost=1)
	S += r5_t1_mem0 >= 6
	r5_t1_mem0 += MAIN_MEM_r[0]

	r5_t1_mem1 = S.Task('r5_t1_mem1', length=1, delay_cost=1)
	S += r5_t1_mem1 >= 6
	r5_t1_mem1 += MAIN_MEM_r[1]

	r12_t1_in = S.Task('r12_t1_in', length=1, delay_cost=1)
	S += r12_t1_in >= 7
	r12_t1_in += MM_in[0]

	r12_t1_mem0 = S.Task('r12_t1_mem0', length=1, delay_cost=1)
	S += r12_t1_mem0 >= 7
	r12_t1_mem0 += MAIN_MEM_r[0]

	r12_t1_mem1 = S.Task('r12_t1_mem1', length=1, delay_cost=1)
	S += r12_t1_mem1 >= 7
	r12_t1_mem1 += MAIN_MEM_r[1]

	r5_t1 = S.Task('r5_t1', length=6, delay_cost=1)
	S += r5_t1 >= 7
	r5_t1 += MM[0]

	r12_t0_in = S.Task('r12_t0_in', length=1, delay_cost=1)
	S += r12_t0_in >= 8
	r12_t0_in += MM_in[0]

	r12_t0_mem0 = S.Task('r12_t0_mem0', length=1, delay_cost=1)
	S += r12_t0_mem0 >= 8
	r12_t0_mem0 += MAIN_MEM_r[0]

	r12_t0_mem1 = S.Task('r12_t0_mem1', length=1, delay_cost=1)
	S += r12_t0_mem1 >= 8
	r12_t0_mem1 += MAIN_MEM_r[1]

	r12_t1 = S.Task('r12_t1', length=6, delay_cost=1)
	S += r12_t1 >= 8
	r12_t1 += MM[0]

	r12_t0 = S.Task('r12_t0', length=6, delay_cost=1)
	S += r12_t0 >= 9
	r12_t0 += MM[0]

	r6_t0_in = S.Task('r6_t0_in', length=1, delay_cost=1)
	S += r6_t0_in >= 9
	r6_t0_in += MM_in[0]

	r6_t0_mem0 = S.Task('r6_t0_mem0', length=1, delay_cost=1)
	S += r6_t0_mem0 >= 9
	r6_t0_mem0 += MAIN_MEM_r[0]

	r6_t0_mem1 = S.Task('r6_t0_mem1', length=1, delay_cost=1)
	S += r6_t0_mem1 >= 9
	r6_t0_mem1 += MAIN_MEM_r[1]

	r5_t0_in = S.Task('r5_t0_in', length=1, delay_cost=1)
	S += r5_t0_in >= 10
	r5_t0_in += MM_in[0]

	r5_t0_mem0 = S.Task('r5_t0_mem0', length=1, delay_cost=1)
	S += r5_t0_mem0 >= 10
	r5_t0_mem0 += MAIN_MEM_r[0]

	r5_t0_mem1 = S.Task('r5_t0_mem1', length=1, delay_cost=1)
	S += r5_t0_mem1 >= 10
	r5_t0_mem1 += MAIN_MEM_r[1]

	r6_t0 = S.Task('r6_t0', length=6, delay_cost=1)
	S += r6_t0 >= 10
	r6_t0 += MM[0]

	r4_t1_in = S.Task('r4_t1_in', length=1, delay_cost=1)
	S += r4_t1_in >= 11
	r4_t1_in += MM_in[0]

	r4_t1_mem0 = S.Task('r4_t1_mem0', length=1, delay_cost=1)
	S += r4_t1_mem0 >= 11
	r4_t1_mem0 += MAIN_MEM_r[0]

	r4_t1_mem1 = S.Task('r4_t1_mem1', length=1, delay_cost=1)
	S += r4_t1_mem1 >= 11
	r4_t1_mem1 += MAIN_MEM_r[1]

	r5_t0 = S.Task('r5_t0', length=6, delay_cost=1)
	S += r5_t0 >= 11
	r5_t0 += MM[0]

	r4_t0_in = S.Task('r4_t0_in', length=1, delay_cost=1)
	S += r4_t0_in >= 12
	r4_t0_in += MM_in[0]

	r4_t0_mem0 = S.Task('r4_t0_mem0', length=1, delay_cost=1)
	S += r4_t0_mem0 >= 12
	r4_t0_mem0 += MAIN_MEM_r[0]

	r4_t0_mem1 = S.Task('r4_t0_mem1', length=1, delay_cost=1)
	S += r4_t0_mem1 >= 12
	r4_t0_mem1 += MAIN_MEM_r[1]

	r4_t1 = S.Task('r4_t1', length=6, delay_cost=1)
	S += r4_t1 >= 12
	r4_t1 += MM[0]

	r13_t0_in = S.Task('r13_t0_in', length=1, delay_cost=1)
	S += r13_t0_in >= 13
	r13_t0_in += MM_in[0]

	r13_t0_mem0 = S.Task('r13_t0_mem0', length=1, delay_cost=1)
	S += r13_t0_mem0 >= 13
	r13_t0_mem0 += MAIN_MEM_r[0]

	r13_t0_mem1 = S.Task('r13_t0_mem1', length=1, delay_cost=1)
	S += r13_t0_mem1 >= 13
	r13_t0_mem1 += MAIN_MEM_r[1]

	r4_t0 = S.Task('r4_t0', length=6, delay_cost=1)
	S += r4_t0 >= 13
	r4_t0 += MM[0]

	r13_t0 = S.Task('r13_t0', length=6, delay_cost=1)
	S += r13_t0 >= 14
	r13_t0 += MM[0]

	r3_t2_mem0 = S.Task('r3_t2_mem0', length=1, delay_cost=1)
	S += r3_t2_mem0 >= 14
	r3_t2_mem0 += MAIN_MEM_r[0]

	r3_t2_mem1 = S.Task('r3_t2_mem1', length=1, delay_cost=1)
	S += r3_t2_mem1 >= 14
	r3_t2_mem1 += MAIN_MEM_r[1]

	r3_t2 = S.Task('r3_t2', length=1, delay_cost=1)
	S += r3_t2 >= 15
	r3_t2 += MAS[0]

	r5_t3_mem0 = S.Task('r5_t3_mem0', length=1, delay_cost=1)
	S += r5_t3_mem0 >= 15
	r5_t3_mem0 += MAIN_MEM_r[0]

	r5_t3_mem1 = S.Task('r5_t3_mem1', length=1, delay_cost=1)
	S += r5_t3_mem1 >= 15
	r5_t3_mem1 += MAIN_MEM_r[1]

	r5_t2_mem0 = S.Task('r5_t2_mem0', length=1, delay_cost=1)
	S += r5_t2_mem0 >= 16
	r5_t2_mem0 += MAIN_MEM_r[0]

	r5_t2_mem1 = S.Task('r5_t2_mem1', length=1, delay_cost=1)
	S += r5_t2_mem1 >= 16
	r5_t2_mem1 += MAIN_MEM_r[1]

	r5_t3 = S.Task('r5_t3', length=1, delay_cost=1)
	S += r5_t3 >= 16
	r5_t3 += MAS[0]

	r3_t3_mem0 = S.Task('r3_t3_mem0', length=1, delay_cost=1)
	S += r3_t3_mem0 >= 17
	r3_t3_mem0 += MAIN_MEM_r[0]

	r3_t3_mem1 = S.Task('r3_t3_mem1', length=1, delay_cost=1)
	S += r3_t3_mem1 >= 17
	r3_t3_mem1 += MAIN_MEM_r[1]

	r5_t2 = S.Task('r5_t2', length=1, delay_cost=1)
	S += r5_t2 >= 17
	r5_t2 += MAS[2]

	r3_t3 = S.Task('r3_t3', length=1, delay_cost=1)
	S += r3_t3 >= 18
	r3_t3 += MAS[0]

	r4_t2_mem0 = S.Task('r4_t2_mem0', length=1, delay_cost=1)
	S += r4_t2_mem0 >= 18
	r4_t2_mem0 += MAIN_MEM_r[0]

	r4_t2_mem1 = S.Task('r4_t2_mem1', length=1, delay_cost=1)
	S += r4_t2_mem1 >= 18
	r4_t2_mem1 += MAIN_MEM_r[1]

	r4_t2 = S.Task('r4_t2', length=1, delay_cost=1)
	S += r4_t2 >= 19
	r4_t2 += MAS[3]

	r4_t3_mem0 = S.Task('r4_t3_mem0', length=1, delay_cost=1)
	S += r4_t3_mem0 >= 19
	r4_t3_mem0 += MAIN_MEM_r[0]

	r4_t3_mem1 = S.Task('r4_t3_mem1', length=1, delay_cost=1)
	S += r4_t3_mem1 >= 19
	r4_t3_mem1 += MAIN_MEM_r[1]

	r1_t2_mem0 = S.Task('r1_t2_mem0', length=1, delay_cost=1)
	S += r1_t2_mem0 >= 20
	r1_t2_mem0 += MAIN_MEM_r[0]

	r1_t2_mem1 = S.Task('r1_t2_mem1', length=1, delay_cost=1)
	S += r1_t2_mem1 >= 20
	r1_t2_mem1 += MAIN_MEM_r[1]

	r4_t3 = S.Task('r4_t3', length=1, delay_cost=1)
	S += r4_t3 >= 20
	r4_t3 += MAS[0]

	r16_t3_mem0 = S.Task('r16_t3_mem0', length=1, delay_cost=1)
	S += r16_t3_mem0 >= 21
	r16_t3_mem0 += MAIN_MEM_r[0]

	r16_t3_mem1 = S.Task('r16_t3_mem1', length=1, delay_cost=1)
	S += r16_t3_mem1 >= 21
	r16_t3_mem1 += MAIN_MEM_r[1]

	r1_t2 = S.Task('r1_t2', length=1, delay_cost=1)
	S += r1_t2 >= 21
	r1_t2 += MAS[1]

	r13_t3_mem0 = S.Task('r13_t3_mem0', length=1, delay_cost=1)
	S += r13_t3_mem0 >= 22
	r13_t3_mem0 += MAIN_MEM_r[0]

	r13_t3_mem1 = S.Task('r13_t3_mem1', length=1, delay_cost=1)
	S += r13_t3_mem1 >= 22
	r13_t3_mem1 += MAIN_MEM_r[1]

	r16_t3 = S.Task('r16_t3', length=1, delay_cost=1)
	S += r16_t3 >= 22
	r16_t3 += MAS[0]

	r13_t2_mem0 = S.Task('r13_t2_mem0', length=1, delay_cost=1)
	S += r13_t2_mem0 >= 23
	r13_t2_mem0 += MAIN_MEM_r[0]

	r13_t2_mem1 = S.Task('r13_t2_mem1', length=1, delay_cost=1)
	S += r13_t2_mem1 >= 23
	r13_t2_mem1 += MAIN_MEM_r[1]

	r13_t3 = S.Task('r13_t3', length=1, delay_cost=1)
	S += r13_t3 >= 23
	r13_t3 += MAS[0]

	r13_t2 = S.Task('r13_t2', length=1, delay_cost=1)
	S += r13_t2 >= 24
	r13_t2 += MAS[0]

	r1_t3_mem0 = S.Task('r1_t3_mem0', length=1, delay_cost=1)
	S += r1_t3_mem0 >= 24
	r1_t3_mem0 += MAIN_MEM_r[0]

	r1_t3_mem1 = S.Task('r1_t3_mem1', length=1, delay_cost=1)
	S += r1_t3_mem1 >= 24
	r1_t3_mem1 += MAIN_MEM_r[1]

	r12_t3_mem0 = S.Task('r12_t3_mem0', length=1, delay_cost=1)
	S += r12_t3_mem0 >= 25
	r12_t3_mem0 += MAIN_MEM_r[0]

	r12_t3_mem1 = S.Task('r12_t3_mem1', length=1, delay_cost=1)
	S += r12_t3_mem1 >= 25
	r12_t3_mem1 += MAIN_MEM_r[1]

	r1_t3 = S.Task('r1_t3', length=1, delay_cost=1)
	S += r1_t3 >= 25
	r1_t3 += MAS[0]

	r12_t2_mem0 = S.Task('r12_t2_mem0', length=1, delay_cost=1)
	S += r12_t2_mem0 >= 26
	r12_t2_mem0 += MAIN_MEM_r[0]

	r12_t2_mem1 = S.Task('r12_t2_mem1', length=1, delay_cost=1)
	S += r12_t2_mem1 >= 26
	r12_t2_mem1 += MAIN_MEM_r[1]

	r12_t3 = S.Task('r12_t3', length=1, delay_cost=1)
	S += r12_t3 >= 26
	r12_t3 += MAS[0]

	r12_t2 = S.Task('r12_t2', length=1, delay_cost=1)
	S += r12_t2 >= 27
	r12_t2 += MAS[0]

	r9_t2_mem0 = S.Task('r9_t2_mem0', length=1, delay_cost=1)
	S += r9_t2_mem0 >= 27
	r9_t2_mem0 += MAIN_MEM_r[0]

	r9_t2_mem1 = S.Task('r9_t2_mem1', length=1, delay_cost=1)
	S += r9_t2_mem1 >= 27
	r9_t2_mem1 += MAIN_MEM_r[1]

	r6_t3_mem0 = S.Task('r6_t3_mem0', length=1, delay_cost=1)
	S += r6_t3_mem0 >= 28
	r6_t3_mem0 += MAIN_MEM_r[0]

	r6_t3_mem1 = S.Task('r6_t3_mem1', length=1, delay_cost=1)
	S += r6_t3_mem1 >= 28
	r6_t3_mem1 += MAIN_MEM_r[1]

	r9_t2 = S.Task('r9_t2', length=1, delay_cost=1)
	S += r9_t2 >= 28
	r9_t2 += MAS[0]

	r6_t2_mem0 = S.Task('r6_t2_mem0', length=1, delay_cost=1)
	S += r6_t2_mem0 >= 29
	r6_t2_mem0 += MAIN_MEM_r[0]

	r6_t2_mem1 = S.Task('r6_t2_mem1', length=1, delay_cost=1)
	S += r6_t2_mem1 >= 29
	r6_t2_mem1 += MAIN_MEM_r[1]

	r6_t3 = S.Task('r6_t3', length=1, delay_cost=1)
	S += r6_t3 >= 29
	r6_t3 += MAS[1]

	r6_t2 = S.Task('r6_t2', length=1, delay_cost=1)
	S += r6_t2 >= 30
	r6_t2 += MAS[0]


	# new tasks
	r1_t4 = S.Task('r1_t4', length=6, delay_cost=1)
	r1_t4 += alt(MM)
	r1_t4_in = S.Task('r1_t4_in', length=1, delay_cost=1)
	r1_t4_in += alt(MM_in)
	S += r1_t4_in*MM_in[0]<=r1_t4*MM[0]
	r1_t4_mem0 = S.Task('r1_t4_mem0', length=1, delay_cost=1)
	r1_t4_mem0 += MAS_MEM[2]
	S += 21 < r1_t4_mem0
	S += r1_t4_mem0 <= r1_t4

	r1_t4_mem1 = S.Task('r1_t4_mem1', length=1, delay_cost=1)
	r1_t4_mem1 += MAS_MEM[1]
	S += 25 < r1_t4_mem1
	S += r1_t4_mem1 <= r1_t4

	r10 = S.Task('r10', length=1, delay_cost=1)
	r10 += alt(MAS)
	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	r10_mem0 += MM_MEM[0]
	S += 7 < r10_mem0
	S += r10_mem0 <= r10

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	r10_mem1 += MM_MEM[1]
	S += 8 < r10_mem1
	S += r10_mem1 <= r10

	r1_t5 = S.Task('r1_t5', length=1, delay_cost=1)
	r1_t5 += alt(MAS)
	r1_t5_mem0 = S.Task('r1_t5_mem0', length=1, delay_cost=1)
	r1_t5_mem0 += MM_MEM[0]
	S += 7 < r1_t5_mem0
	S += r1_t5_mem0 <= r1_t5

	r1_t5_mem1 = S.Task('r1_t5_mem1', length=1, delay_cost=1)
	r1_t5_mem1 += MM_MEM[1]
	S += 8 < r1_t5_mem1
	S += r1_t5_mem1 <= r1_t5

	r3_t4 = S.Task('r3_t4', length=6, delay_cost=1)
	r3_t4 += alt(MM)
	r3_t4_in = S.Task('r3_t4_in', length=1, delay_cost=1)
	r3_t4_in += alt(MM_in)
	S += r3_t4_in*MM_in[0]<=r3_t4*MM[0]
	r3_t4_mem0 = S.Task('r3_t4_mem0', length=1, delay_cost=1)
	r3_t4_mem0 += MAS_MEM[0]
	S += 15 < r3_t4_mem0
	S += r3_t4_mem0 <= r3_t4

	r3_t4_mem1 = S.Task('r3_t4_mem1', length=1, delay_cost=1)
	r3_t4_mem1 += MAS_MEM[1]
	S += 18 < r3_t4_mem1
	S += r3_t4_mem1 <= r3_t4

	r30 = S.Task('r30', length=1, delay_cost=1)
	r30 += alt(MAS)
	r30_mem0 = S.Task('r30_mem0', length=1, delay_cost=1)
	r30_mem0 += MM_MEM[0]
	S += 11 < r30_mem0
	S += r30_mem0 <= r30

	r30_mem1 = S.Task('r30_mem1', length=1, delay_cost=1)
	r30_mem1 += MM_MEM[1]
	S += 9 < r30_mem1
	S += r30_mem1 <= r30

	r3_t5 = S.Task('r3_t5', length=1, delay_cost=1)
	r3_t5 += alt(MAS)
	r3_t5_mem0 = S.Task('r3_t5_mem0', length=1, delay_cost=1)
	r3_t5_mem0 += MM_MEM[0]
	S += 11 < r3_t5_mem0
	S += r3_t5_mem0 <= r3_t5

	r3_t5_mem1 = S.Task('r3_t5_mem1', length=1, delay_cost=1)
	r3_t5_mem1 += MM_MEM[1]
	S += 9 < r3_t5_mem1
	S += r3_t5_mem1 <= r3_t5

	r4_t4 = S.Task('r4_t4', length=6, delay_cost=1)
	r4_t4 += alt(MM)
	r4_t4_in = S.Task('r4_t4_in', length=1, delay_cost=1)
	r4_t4_in += alt(MM_in)
	S += r4_t4_in*MM_in[0]<=r4_t4*MM[0]
	r4_t4_mem0 = S.Task('r4_t4_mem0', length=1, delay_cost=1)
	r4_t4_mem0 += MAS_MEM[6]
	S += 19 < r4_t4_mem0
	S += r4_t4_mem0 <= r4_t4

	r4_t4_mem1 = S.Task('r4_t4_mem1', length=1, delay_cost=1)
	r4_t4_mem1 += MAS_MEM[1]
	S += 20 < r4_t4_mem1
	S += r4_t4_mem1 <= r4_t4

	r40 = S.Task('r40', length=1, delay_cost=1)
	r40 += alt(MAS)
	r40_mem0 = S.Task('r40_mem0', length=1, delay_cost=1)
	r40_mem0 += MM_MEM[0]
	S += 18 < r40_mem0
	S += r40_mem0 <= r40

	r40_mem1 = S.Task('r40_mem1', length=1, delay_cost=1)
	r40_mem1 += MM_MEM[1]
	S += 17 < r40_mem1
	S += r40_mem1 <= r40

	r4_t5 = S.Task('r4_t5', length=1, delay_cost=1)
	r4_t5 += alt(MAS)
	r4_t5_mem0 = S.Task('r4_t5_mem0', length=1, delay_cost=1)
	r4_t5_mem0 += MM_MEM[0]
	S += 18 < r4_t5_mem0
	S += r4_t5_mem0 <= r4_t5

	r4_t5_mem1 = S.Task('r4_t5_mem1', length=1, delay_cost=1)
	r4_t5_mem1 += MM_MEM[1]
	S += 17 < r4_t5_mem1
	S += r4_t5_mem1 <= r4_t5

	r5_t4 = S.Task('r5_t4', length=6, delay_cost=1)
	r5_t4 += alt(MM)
	r5_t4_in = S.Task('r5_t4_in', length=1, delay_cost=1)
	r5_t4_in += alt(MM_in)
	S += r5_t4_in*MM_in[0]<=r5_t4*MM[0]
	r5_t4_mem0 = S.Task('r5_t4_mem0', length=1, delay_cost=1)
	r5_t4_mem0 += MAS_MEM[4]
	S += 17 < r5_t4_mem0
	S += r5_t4_mem0 <= r5_t4

	r5_t4_mem1 = S.Task('r5_t4_mem1', length=1, delay_cost=1)
	r5_t4_mem1 += MAS_MEM[1]
	S += 16 < r5_t4_mem1
	S += r5_t4_mem1 <= r5_t4

	r50 = S.Task('r50', length=1, delay_cost=1)
	r50 += alt(MAS)
	r50_mem0 = S.Task('r50_mem0', length=1, delay_cost=1)
	r50_mem0 += MM_MEM[0]
	S += 16 < r50_mem0
	S += r50_mem0 <= r50

	r50_mem1 = S.Task('r50_mem1', length=1, delay_cost=1)
	r50_mem1 += MM_MEM[1]
	S += 12 < r50_mem1
	S += r50_mem1 <= r50

	r5_t5 = S.Task('r5_t5', length=1, delay_cost=1)
	r5_t5 += alt(MAS)
	r5_t5_mem0 = S.Task('r5_t5_mem0', length=1, delay_cost=1)
	r5_t5_mem0 += MM_MEM[0]
	S += 16 < r5_t5_mem0
	S += r5_t5_mem0 <= r5_t5

	r5_t5_mem1 = S.Task('r5_t5_mem1', length=1, delay_cost=1)
	r5_t5_mem1 += MM_MEM[1]
	S += 12 < r5_t5_mem1
	S += r5_t5_mem1 <= r5_t5

	r6_t4 = S.Task('r6_t4', length=6, delay_cost=1)
	r6_t4 += alt(MM)
	r6_t4_in = S.Task('r6_t4_in', length=1, delay_cost=1)
	r6_t4_in += alt(MM_in)
	S += r6_t4_in*MM_in[0]<=r6_t4*MM[0]
	r6_t4_mem0 = S.Task('r6_t4_mem0', length=1, delay_cost=1)
	r6_t4_mem0 += MAS_MEM[0]
	S += 30 < r6_t4_mem0
	S += r6_t4_mem0 <= r6_t4

	r6_t4_mem1 = S.Task('r6_t4_mem1', length=1, delay_cost=1)
	r6_t4_mem1 += MAS_MEM[3]
	S += 29 < r6_t4_mem1
	S += r6_t4_mem1 <= r6_t4

	r60 = S.Task('r60', length=1, delay_cost=1)
	r60 += alt(MAS)
	r60_mem0 = S.Task('r60_mem0', length=1, delay_cost=1)
	r60_mem0 += MM_MEM[0]
	S += 15 < r60_mem0
	S += r60_mem0 <= r60

	r60_mem1 = S.Task('r60_mem1', length=1, delay_cost=1)
	r60_mem1 += MM_MEM[1]
	S += 6 < r60_mem1
	S += r60_mem1 <= r60

	r6_t5 = S.Task('r6_t5', length=1, delay_cost=1)
	r6_t5 += alt(MAS)
	r6_t5_mem0 = S.Task('r6_t5_mem0', length=1, delay_cost=1)
	r6_t5_mem0 += MM_MEM[0]
	S += 15 < r6_t5_mem0
	S += r6_t5_mem0 <= r6_t5

	r6_t5_mem1 = S.Task('r6_t5_mem1', length=1, delay_cost=1)
	r6_t5_mem1 += MM_MEM[1]
	S += 6 < r6_t5_mem1
	S += r6_t5_mem1 <= r6_t5

	r12_t4 = S.Task('r12_t4', length=6, delay_cost=1)
	r12_t4 += alt(MM)
	r12_t4_in = S.Task('r12_t4_in', length=1, delay_cost=1)
	r12_t4_in += alt(MM_in)
	S += r12_t4_in*MM_in[0]<=r12_t4*MM[0]
	r12_t4_mem0 = S.Task('r12_t4_mem0', length=1, delay_cost=1)
	r12_t4_mem0 += MAS_MEM[0]
	S += 27 < r12_t4_mem0
	S += r12_t4_mem0 <= r12_t4

	r12_t4_mem1 = S.Task('r12_t4_mem1', length=1, delay_cost=1)
	r12_t4_mem1 += MAS_MEM[1]
	S += 26 < r12_t4_mem1
	S += r12_t4_mem1 <= r12_t4

	r120 = S.Task('r120', length=1, delay_cost=1)
	r120 += alt(MAS)
	r120_mem0 = S.Task('r120_mem0', length=1, delay_cost=1)
	r120_mem0 += MM_MEM[0]
	S += 14 < r120_mem0
	S += r120_mem0 <= r120

	r120_mem1 = S.Task('r120_mem1', length=1, delay_cost=1)
	r120_mem1 += MM_MEM[1]
	S += 13 < r120_mem1
	S += r120_mem1 <= r120

	r12_t5 = S.Task('r12_t5', length=1, delay_cost=1)
	r12_t5 += alt(MAS)
	r12_t5_mem0 = S.Task('r12_t5_mem0', length=1, delay_cost=1)
	r12_t5_mem0 += MM_MEM[0]
	S += 14 < r12_t5_mem0
	S += r12_t5_mem0 <= r12_t5

	r12_t5_mem1 = S.Task('r12_t5_mem1', length=1, delay_cost=1)
	r12_t5_mem1 += MM_MEM[1]
	S += 13 < r12_t5_mem1
	S += r12_t5_mem1 <= r12_t5

	r13_t4 = S.Task('r13_t4', length=6, delay_cost=1)
	r13_t4 += alt(MM)
	r13_t4_in = S.Task('r13_t4_in', length=1, delay_cost=1)
	r13_t4_in += alt(MM_in)
	S += r13_t4_in*MM_in[0]<=r13_t4*MM[0]
	r13_t4_mem0 = S.Task('r13_t4_mem0', length=1, delay_cost=1)
	r13_t4_mem0 += MAS_MEM[0]
	S += 24 < r13_t4_mem0
	S += r13_t4_mem0 <= r13_t4

	r13_t4_mem1 = S.Task('r13_t4_mem1', length=1, delay_cost=1)
	r13_t4_mem1 += MAS_MEM[1]
	S += 23 < r13_t4_mem1
	S += r13_t4_mem1 <= r13_t4

	r130 = S.Task('r130', length=1, delay_cost=1)
	r130 += alt(MAS)
	r130_mem0 = S.Task('r130_mem0', length=1, delay_cost=1)
	r130_mem0 += MM_MEM[0]
	S += 19 < r130_mem0
	S += r130_mem0 <= r130

	r130_mem1 = S.Task('r130_mem1', length=1, delay_cost=1)
	r130_mem1 += MM_MEM[1]
	S += 10 < r130_mem1
	S += r130_mem1 <= r130

	r13_t5 = S.Task('r13_t5', length=1, delay_cost=1)
	r13_t5 += alt(MAS)
	r13_t5_mem0 = S.Task('r13_t5_mem0', length=1, delay_cost=1)
	r13_t5_mem0 += MM_MEM[0]
	S += 19 < r13_t5_mem0
	S += r13_t5_mem0 <= r13_t5

	r13_t5_mem1 = S.Task('r13_t5_mem1', length=1, delay_cost=1)
	r13_t5_mem1 += MM_MEM[1]
	S += 10 < r13_t5_mem1
	S += r13_t5_mem1 <= r13_t5

	r11 = S.Task('r11', length=1, delay_cost=1)
	r11 += alt(MAS)
	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	r11_mem0 += alt(MM_MEM)
	S += (r1_t4*MM[0])-1 < r11_mem0*MM_MEM[0]
	S += r11_mem0 <= r11

	r11_mem1 = S.Task('r11_mem1', length=1, delay_cost=1)
	r11_mem1 += alt(MAS_MEM)
	S += (r1_t5*MAS[0])-1 < r11_mem1*MAS_MEM[1]
	S += (r1_t5*MAS[1])-1 < r11_mem1*MAS_MEM[3]
	S += (r1_t5*MAS[2])-1 < r11_mem1*MAS_MEM[5]
	S += (r1_t5*MAS[3])-1 < r11_mem1*MAS_MEM[7]
	S += r11_mem1 <= r11

	r20 = S.Task('r20', length=1, delay_cost=1)
	r20 += alt(MAS)
	r20_mem0 = S.Task('r20_mem0', length=1, delay_cost=1)
	r20_mem0 += alt(MAS_MEM)
	S += (r10*MAS[0])-1 < r20_mem0*MAS_MEM[0]
	S += (r10*MAS[1])-1 < r20_mem0*MAS_MEM[2]
	S += (r10*MAS[2])-1 < r20_mem0*MAS_MEM[4]
	S += (r10*MAS[3])-1 < r20_mem0*MAS_MEM[6]
	S += r20_mem0 <= r20

	r20_mem1 = S.Task('r20_mem1', length=1, delay_cost=1)
	r20_mem1 += alt(MAS_MEM)
	S += (r10*MAS[0])-1 < r20_mem1*MAS_MEM[1]
	S += (r10*MAS[1])-1 < r20_mem1*MAS_MEM[3]
	S += (r10*MAS[2])-1 < r20_mem1*MAS_MEM[5]
	S += (r10*MAS[3])-1 < r20_mem1*MAS_MEM[7]
	S += r20_mem1 <= r20

	r31 = S.Task('r31', length=1, delay_cost=1)
	r31 += alt(MAS)
	r31_mem0 = S.Task('r31_mem0', length=1, delay_cost=1)
	r31_mem0 += alt(MM_MEM)
	S += (r3_t4*MM[0])-1 < r31_mem0*MM_MEM[0]
	S += r31_mem0 <= r31

	r31_mem1 = S.Task('r31_mem1', length=1, delay_cost=1)
	r31_mem1 += alt(MAS_MEM)
	S += (r3_t5*MAS[0])-1 < r31_mem1*MAS_MEM[1]
	S += (r3_t5*MAS[1])-1 < r31_mem1*MAS_MEM[3]
	S += (r3_t5*MAS[2])-1 < r31_mem1*MAS_MEM[5]
	S += (r3_t5*MAS[3])-1 < r31_mem1*MAS_MEM[7]
	S += r31_mem1 <= r31

	r41 = S.Task('r41', length=1, delay_cost=1)
	r41 += alt(MAS)
	r41_mem0 = S.Task('r41_mem0', length=1, delay_cost=1)
	r41_mem0 += alt(MM_MEM)
	S += (r4_t4*MM[0])-1 < r41_mem0*MM_MEM[0]
	S += r41_mem0 <= r41

	r41_mem1 = S.Task('r41_mem1', length=1, delay_cost=1)
	r41_mem1 += alt(MAS_MEM)
	S += (r4_t5*MAS[0])-1 < r41_mem1*MAS_MEM[1]
	S += (r4_t5*MAS[1])-1 < r41_mem1*MAS_MEM[3]
	S += (r4_t5*MAS[2])-1 < r41_mem1*MAS_MEM[5]
	S += (r4_t5*MAS[3])-1 < r41_mem1*MAS_MEM[7]
	S += r41_mem1 <= r41

	r51 = S.Task('r51', length=1, delay_cost=1)
	r51 += alt(MAS)
	r51_mem0 = S.Task('r51_mem0', length=1, delay_cost=1)
	r51_mem0 += alt(MM_MEM)
	S += (r5_t4*MM[0])-1 < r51_mem0*MM_MEM[0]
	S += r51_mem0 <= r51

	r51_mem1 = S.Task('r51_mem1', length=1, delay_cost=1)
	r51_mem1 += alt(MAS_MEM)
	S += (r5_t5*MAS[0])-1 < r51_mem1*MAS_MEM[1]
	S += (r5_t5*MAS[1])-1 < r51_mem1*MAS_MEM[3]
	S += (r5_t5*MAS[2])-1 < r51_mem1*MAS_MEM[5]
	S += (r5_t5*MAS[3])-1 < r51_mem1*MAS_MEM[7]
	S += r51_mem1 <= r51

	r61 = S.Task('r61', length=1, delay_cost=1)
	r61 += alt(MAS)
	r61_mem0 = S.Task('r61_mem0', length=1, delay_cost=1)
	r61_mem0 += alt(MM_MEM)
	S += (r6_t4*MM[0])-1 < r61_mem0*MM_MEM[0]
	S += r61_mem0 <= r61

	r61_mem1 = S.Task('r61_mem1', length=1, delay_cost=1)
	r61_mem1 += alt(MAS_MEM)
	S += (r6_t5*MAS[0])-1 < r61_mem1*MAS_MEM[1]
	S += (r6_t5*MAS[1])-1 < r61_mem1*MAS_MEM[3]
	S += (r6_t5*MAS[2])-1 < r61_mem1*MAS_MEM[5]
	S += (r6_t5*MAS[3])-1 < r61_mem1*MAS_MEM[7]
	S += r61_mem1 <= r61

	r70 = S.Task('r70', length=1, delay_cost=1)
	r70 += alt(MAS)
	r70_mem0 = S.Task('r70_mem0', length=1, delay_cost=1)
	r70_mem0 += alt(MAS_MEM)
	S += (r50*MAS[0])-1 < r70_mem0*MAS_MEM[0]
	S += (r50*MAS[1])-1 < r70_mem0*MAS_MEM[2]
	S += (r50*MAS[2])-1 < r70_mem0*MAS_MEM[4]
	S += (r50*MAS[3])-1 < r70_mem0*MAS_MEM[6]
	S += r70_mem0 <= r70

	r70_mem1 = S.Task('r70_mem1', length=1, delay_cost=1)
	r70_mem1 += alt(MAS_MEM)
	S += (r60*MAS[0])-1 < r70_mem1*MAS_MEM[1]
	S += (r60*MAS[1])-1 < r70_mem1*MAS_MEM[3]
	S += (r60*MAS[2])-1 < r70_mem1*MAS_MEM[5]
	S += (r60*MAS[3])-1 < r70_mem1*MAS_MEM[7]
	S += r70_mem1 <= r70

	r80 = S.Task('r80', length=1, delay_cost=1)
	r80 += alt(MAS)
	r80_mem0 = S.Task('r80_mem0', length=1, delay_cost=1)
	r80_mem0 += MAIN_MEM_r[0]
	S += r80_mem0 <= r80

	r80_mem1 = S.Task('r80_mem1', length=1, delay_cost=1)
	r80_mem1 += alt(MAS_MEM)
	S += (r40*MAS[0])-1 < r80_mem1*MAS_MEM[1]
	S += (r40*MAS[1])-1 < r80_mem1*MAS_MEM[3]
	S += (r40*MAS[2])-1 < r80_mem1*MAS_MEM[5]
	S += (r40*MAS[3])-1 < r80_mem1*MAS_MEM[7]
	S += r80_mem1 <= r80

	r100 = S.Task('r100', length=1, delay_cost=1)
	r100 += alt(MAS)
	r100_mem0 = S.Task('r100_mem0', length=1, delay_cost=1)
	r100_mem0 += MAIN_MEM_r[0]
	S += r100_mem0 <= r100

	r100_mem1 = S.Task('r100_mem1', length=1, delay_cost=1)
	r100_mem1 += alt(MAS_MEM)
	S += (r40*MAS[0])-1 < r100_mem1*MAS_MEM[1]
	S += (r40*MAS[1])-1 < r100_mem1*MAS_MEM[3]
	S += (r40*MAS[2])-1 < r100_mem1*MAS_MEM[5]
	S += (r40*MAS[3])-1 < r100_mem1*MAS_MEM[7]
	S += r100_mem1 <= r100

	r121 = S.Task('r121', length=1, delay_cost=1)
	r121 += alt(MAS)
	r121_mem0 = S.Task('r121_mem0', length=1, delay_cost=1)
	r121_mem0 += alt(MM_MEM)
	S += (r12_t4*MM[0])-1 < r121_mem0*MM_MEM[0]
	S += r121_mem0 <= r121

	r121_mem1 = S.Task('r121_mem1', length=1, delay_cost=1)
	r121_mem1 += alt(MAS_MEM)
	S += (r12_t5*MAS[0])-1 < r121_mem1*MAS_MEM[1]
	S += (r12_t5*MAS[1])-1 < r121_mem1*MAS_MEM[3]
	S += (r12_t5*MAS[2])-1 < r121_mem1*MAS_MEM[5]
	S += (r12_t5*MAS[3])-1 < r121_mem1*MAS_MEM[7]
	S += r121_mem1 <= r121

	r131 = S.Task('r131', length=1, delay_cost=1)
	r131 += alt(MAS)
	r131_mem0 = S.Task('r131_mem0', length=1, delay_cost=1)
	r131_mem0 += alt(MM_MEM)
	S += (r13_t4*MM[0])-1 < r131_mem0*MM_MEM[0]
	S += r131_mem0 <= r131

	r131_mem1 = S.Task('r131_mem1', length=1, delay_cost=1)
	r131_mem1 += alt(MAS_MEM)
	S += (r13_t5*MAS[0])-1 < r131_mem1*MAS_MEM[1]
	S += (r13_t5*MAS[1])-1 < r131_mem1*MAS_MEM[3]
	S += (r13_t5*MAS[2])-1 < r131_mem1*MAS_MEM[5]
	S += (r13_t5*MAS[3])-1 < r131_mem1*MAS_MEM[7]
	S += r131_mem1 <= r131

	r21 = S.Task('r21', length=1, delay_cost=1)
	r21 += alt(MAS)
	r21_mem0 = S.Task('r21_mem0', length=1, delay_cost=1)
	r21_mem0 += alt(MAS_MEM)
	S += (r11*MAS[0])-1 < r21_mem0*MAS_MEM[0]
	S += (r11*MAS[1])-1 < r21_mem0*MAS_MEM[2]
	S += (r11*MAS[2])-1 < r21_mem0*MAS_MEM[4]
	S += (r11*MAS[3])-1 < r21_mem0*MAS_MEM[6]
	S += r21_mem0 <= r21

	r21_mem1 = S.Task('r21_mem1', length=1, delay_cost=1)
	r21_mem1 += alt(MAS_MEM)
	S += (r11*MAS[0])-1 < r21_mem1*MAS_MEM[1]
	S += (r11*MAS[1])-1 < r21_mem1*MAS_MEM[3]
	S += (r11*MAS[2])-1 < r21_mem1*MAS_MEM[5]
	S += (r11*MAS[3])-1 < r21_mem1*MAS_MEM[7]
	S += r21_mem1 <= r21

	r71 = S.Task('r71', length=1, delay_cost=1)
	r71 += alt(MAS)
	r71_mem0 = S.Task('r71_mem0', length=1, delay_cost=1)
	r71_mem0 += alt(MAS_MEM)
	S += (r51*MAS[0])-1 < r71_mem0*MAS_MEM[0]
	S += (r51*MAS[1])-1 < r71_mem0*MAS_MEM[2]
	S += (r51*MAS[2])-1 < r71_mem0*MAS_MEM[4]
	S += (r51*MAS[3])-1 < r71_mem0*MAS_MEM[6]
	S += r71_mem0 <= r71

	r71_mem1 = S.Task('r71_mem1', length=1, delay_cost=1)
	r71_mem1 += alt(MAS_MEM)
	S += (r61*MAS[0])-1 < r71_mem1*MAS_MEM[1]
	S += (r61*MAS[1])-1 < r71_mem1*MAS_MEM[3]
	S += (r61*MAS[2])-1 < r71_mem1*MAS_MEM[5]
	S += (r61*MAS[3])-1 < r71_mem1*MAS_MEM[7]
	S += r71_mem1 <= r71

	r81 = S.Task('r81', length=1, delay_cost=1)
	r81 += alt(MAS)
	r81_mem0 = S.Task('r81_mem0', length=1, delay_cost=1)
	r81_mem0 += MAIN_MEM_r[0]
	S += r81_mem0 <= r81

	r81_mem1 = S.Task('r81_mem1', length=1, delay_cost=1)
	r81_mem1 += alt(MAS_MEM)
	S += (r41*MAS[0])-1 < r81_mem1*MAS_MEM[1]
	S += (r41*MAS[1])-1 < r81_mem1*MAS_MEM[3]
	S += (r41*MAS[2])-1 < r81_mem1*MAS_MEM[5]
	S += (r41*MAS[3])-1 < r81_mem1*MAS_MEM[7]
	S += r81_mem1 <= r81

	r9_t0 = S.Task('r9_t0', length=6, delay_cost=1)
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
	S += (r70*MAS[2])-1 < r9_t0_mem1*MAS_MEM[5]
	S += (r70*MAS[3])-1 < r9_t0_mem1*MAS_MEM[7]
	S += r9_t0_mem1 <= r9_t0

	r101 = S.Task('r101', length=1, delay_cost=1)
	r101 += alt(MAS)
	r101_mem0 = S.Task('r101_mem0', length=1, delay_cost=1)
	r101_mem0 += MAIN_MEM_r[0]
	S += r101_mem0 <= r101

	r101_mem1 = S.Task('r101_mem1', length=1, delay_cost=1)
	r101_mem1 += alt(MAS_MEM)
	S += (r41*MAS[0])-1 < r101_mem1*MAS_MEM[1]
	S += (r41*MAS[1])-1 < r101_mem1*MAS_MEM[3]
	S += (r41*MAS[2])-1 < r101_mem1*MAS_MEM[5]
	S += (r41*MAS[3])-1 < r101_mem1*MAS_MEM[7]
	S += r101_mem1 <= r101

	X_new_t0 = S.Task('X_new_t0', length=6, delay_cost=1)
	X_new_t0 += alt(MM)
	X_new_t0_in = S.Task('X_new_t0_in', length=1, delay_cost=1)
	X_new_t0_in += alt(MM_in)
	S += X_new_t0_in*MM_in[0]<=X_new_t0*MM[0]
	X_new_t0_mem0 = S.Task('X_new_t0_mem0', length=1, delay_cost=1)
	X_new_t0_mem0 += alt(MAS_MEM)
	S += (r20*MAS[0])-1 < X_new_t0_mem0*MAS_MEM[0]
	S += (r20*MAS[1])-1 < X_new_t0_mem0*MAS_MEM[2]
	S += (r20*MAS[2])-1 < X_new_t0_mem0*MAS_MEM[4]
	S += (r20*MAS[3])-1 < X_new_t0_mem0*MAS_MEM[6]
	S += X_new_t0_mem0 <= X_new_t0

	X_new_t0_mem1 = S.Task('X_new_t0_mem1', length=1, delay_cost=1)
	X_new_t0_mem1 += alt(MAS_MEM)
	S += (r120*MAS[0])-1 < X_new_t0_mem1*MAS_MEM[1]
	S += (r120*MAS[1])-1 < X_new_t0_mem1*MAS_MEM[3]
	S += (r120*MAS[2])-1 < X_new_t0_mem1*MAS_MEM[5]
	S += (r120*MAS[3])-1 < X_new_t0_mem1*MAS_MEM[7]
	S += X_new_t0_mem1 <= X_new_t0

	X_new_t3 = S.Task('X_new_t3', length=1, delay_cost=1)
	X_new_t3 += alt(MAS)
	X_new_t3_mem0 = S.Task('X_new_t3_mem0', length=1, delay_cost=1)
	X_new_t3_mem0 += alt(MAS_MEM)
	S += (r120*MAS[0])-1 < X_new_t3_mem0*MAS_MEM[0]
	S += (r120*MAS[1])-1 < X_new_t3_mem0*MAS_MEM[2]
	S += (r120*MAS[2])-1 < X_new_t3_mem0*MAS_MEM[4]
	S += (r120*MAS[3])-1 < X_new_t3_mem0*MAS_MEM[6]
	S += X_new_t3_mem0 <= X_new_t3

	X_new_t3_mem1 = S.Task('X_new_t3_mem1', length=1, delay_cost=1)
	X_new_t3_mem1 += alt(MAS_MEM)
	S += (r121*MAS[0])-1 < X_new_t3_mem1*MAS_MEM[1]
	S += (r121*MAS[1])-1 < X_new_t3_mem1*MAS_MEM[3]
	S += (r121*MAS[2])-1 < X_new_t3_mem1*MAS_MEM[5]
	S += (r121*MAS[3])-1 < X_new_t3_mem1*MAS_MEM[7]
	S += X_new_t3_mem1 <= X_new_t3

	r14_t0 = S.Task('r14_t0', length=6, delay_cost=1)
	r14_t0 += alt(MM)
	r14_t0_in = S.Task('r14_t0_in', length=1, delay_cost=1)
	r14_t0_in += alt(MM_in)
	S += r14_t0_in*MM_in[0]<=r14_t0*MM[0]
	r14_t0_mem0 = S.Task('r14_t0_mem0', length=1, delay_cost=1)
	r14_t0_mem0 += alt(MAS_MEM)
	S += (r20*MAS[0])-1 < r14_t0_mem0*MAS_MEM[0]
	S += (r20*MAS[1])-1 < r14_t0_mem0*MAS_MEM[2]
	S += (r20*MAS[2])-1 < r14_t0_mem0*MAS_MEM[4]
	S += (r20*MAS[3])-1 < r14_t0_mem0*MAS_MEM[6]
	S += r14_t0_mem0 <= r14_t0

	r14_t0_mem1 = S.Task('r14_t0_mem1', length=1, delay_cost=1)
	r14_t0_mem1 += alt(MAS_MEM)
	S += (r30*MAS[0])-1 < r14_t0_mem1*MAS_MEM[1]
	S += (r30*MAS[1])-1 < r14_t0_mem1*MAS_MEM[3]
	S += (r30*MAS[2])-1 < r14_t0_mem1*MAS_MEM[5]
	S += (r30*MAS[3])-1 < r14_t0_mem1*MAS_MEM[7]
	S += r14_t0_mem1 <= r14_t0

	r14_t3 = S.Task('r14_t3', length=1, delay_cost=1)
	r14_t3 += alt(MAS)
	r14_t3_mem0 = S.Task('r14_t3_mem0', length=1, delay_cost=1)
	r14_t3_mem0 += alt(MAS_MEM)
	S += (r30*MAS[0])-1 < r14_t3_mem0*MAS_MEM[0]
	S += (r30*MAS[1])-1 < r14_t3_mem0*MAS_MEM[2]
	S += (r30*MAS[2])-1 < r14_t3_mem0*MAS_MEM[4]
	S += (r30*MAS[3])-1 < r14_t3_mem0*MAS_MEM[6]
	S += r14_t3_mem0 <= r14_t3

	r14_t3_mem1 = S.Task('r14_t3_mem1', length=1, delay_cost=1)
	r14_t3_mem1 += alt(MAS_MEM)
	S += (r31*MAS[0])-1 < r14_t3_mem1*MAS_MEM[1]
	S += (r31*MAS[1])-1 < r14_t3_mem1*MAS_MEM[3]
	S += (r31*MAS[2])-1 < r14_t3_mem1*MAS_MEM[5]
	S += (r31*MAS[3])-1 < r14_t3_mem1*MAS_MEM[7]
	S += r14_t3_mem1 <= r14_t3

	Z_new_t0 = S.Task('Z_new_t0', length=6, delay_cost=1)
	Z_new_t0 += alt(MM)
	Z_new_t0_in = S.Task('Z_new_t0_in', length=1, delay_cost=1)
	Z_new_t0_in += alt(MM_in)
	S += Z_new_t0_in*MM_in[0]<=Z_new_t0*MM[0]
	Z_new_t0_mem0 = S.Task('Z_new_t0_mem0', length=1, delay_cost=1)
	Z_new_t0_mem0 += alt(MAS_MEM)
	S += (r20*MAS[0])-1 < Z_new_t0_mem0*MAS_MEM[0]
	S += (r20*MAS[1])-1 < Z_new_t0_mem0*MAS_MEM[2]
	S += (r20*MAS[2])-1 < Z_new_t0_mem0*MAS_MEM[4]
	S += (r20*MAS[3])-1 < Z_new_t0_mem0*MAS_MEM[6]
	S += Z_new_t0_mem0 <= Z_new_t0

	Z_new_t0_mem1 = S.Task('Z_new_t0_mem1', length=1, delay_cost=1)
	Z_new_t0_mem1 += alt(MAS_MEM)
	S += (r130*MAS[0])-1 < Z_new_t0_mem1*MAS_MEM[1]
	S += (r130*MAS[1])-1 < Z_new_t0_mem1*MAS_MEM[3]
	S += (r130*MAS[2])-1 < Z_new_t0_mem1*MAS_MEM[5]
	S += (r130*MAS[3])-1 < Z_new_t0_mem1*MAS_MEM[7]
	S += Z_new_t0_mem1 <= Z_new_t0

	Z_new_t3 = S.Task('Z_new_t3', length=1, delay_cost=1)
	Z_new_t3 += alt(MAS)
	Z_new_t3_mem0 = S.Task('Z_new_t3_mem0', length=1, delay_cost=1)
	Z_new_t3_mem0 += alt(MAS_MEM)
	S += (r130*MAS[0])-1 < Z_new_t3_mem0*MAS_MEM[0]
	S += (r130*MAS[1])-1 < Z_new_t3_mem0*MAS_MEM[2]
	S += (r130*MAS[2])-1 < Z_new_t3_mem0*MAS_MEM[4]
	S += (r130*MAS[3])-1 < Z_new_t3_mem0*MAS_MEM[6]
	S += Z_new_t3_mem0 <= Z_new_t3

	Z_new_t3_mem1 = S.Task('Z_new_t3_mem1', length=1, delay_cost=1)
	Z_new_t3_mem1 += alt(MAS_MEM)
	S += (r131*MAS[0])-1 < Z_new_t3_mem1*MAS_MEM[1]
	S += (r131*MAS[1])-1 < Z_new_t3_mem1*MAS_MEM[3]
	S += (r131*MAS[2])-1 < Z_new_t3_mem1*MAS_MEM[5]
	S += (r131*MAS[3])-1 < Z_new_t3_mem1*MAS_MEM[7]
	S += Z_new_t3_mem1 <= Z_new_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS4/EP2_YRECOVER/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

