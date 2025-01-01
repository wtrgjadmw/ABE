from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 213
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=1, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=2)
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

	r13_t1_in = S.Task('r13_t1_in', length=1, delay_cost=1)
	S += r13_t1_in >= 1
	r13_t1_in += MM_in[0]

	r13_t1_mem0 = S.Task('r13_t1_mem0', length=1, delay_cost=1)
	S += r13_t1_mem0 >= 1
	r13_t1_mem0 += MAIN_MEM_r[0]

	r13_t1_mem1 = S.Task('r13_t1_mem1', length=1, delay_cost=1)
	S += r13_t1_mem1 >= 1
	r13_t1_mem1 += MAIN_MEM_r[1]

	r6_t1 = S.Task('r6_t1', length=6, delay_cost=1)
	S += r6_t1 >= 1
	r6_t1 += MM[0]

	r13_t1 = S.Task('r13_t1', length=6, delay_cost=1)
	S += r13_t1 >= 2
	r13_t1 += MM[0]

	r5_t2_in = S.Task('r5_t2_in', length=1, delay_cost=1)
	S += r5_t2_in >= 2
	r5_t2_in += MAS_in[0]

	r5_t2_mem0 = S.Task('r5_t2_mem0', length=1, delay_cost=1)
	S += r5_t2_mem0 >= 2
	r5_t2_mem0 += MAIN_MEM_r[0]

	r5_t2_mem1 = S.Task('r5_t2_mem1', length=1, delay_cost=1)
	S += r5_t2_mem1 >= 2
	r5_t2_mem1 += MAIN_MEM_r[1]

	r5_t0_in = S.Task('r5_t0_in', length=1, delay_cost=1)
	S += r5_t0_in >= 3
	r5_t0_in += MM_in[0]

	r5_t0_mem0 = S.Task('r5_t0_mem0', length=1, delay_cost=1)
	S += r5_t0_mem0 >= 3
	r5_t0_mem0 += MAIN_MEM_r[0]

	r5_t0_mem1 = S.Task('r5_t0_mem1', length=1, delay_cost=1)
	S += r5_t0_mem1 >= 3
	r5_t0_mem1 += MAIN_MEM_r[1]

	r5_t2 = S.Task('r5_t2', length=2, delay_cost=1)
	S += r5_t2 >= 3
	r5_t2 += MAS[0]

	r4_t1_in = S.Task('r4_t1_in', length=1, delay_cost=1)
	S += r4_t1_in >= 4
	r4_t1_in += MM_in[0]

	r4_t1_mem0 = S.Task('r4_t1_mem0', length=1, delay_cost=1)
	S += r4_t1_mem0 >= 4
	r4_t1_mem0 += MAIN_MEM_r[0]

	r4_t1_mem1 = S.Task('r4_t1_mem1', length=1, delay_cost=1)
	S += r4_t1_mem1 >= 4
	r4_t1_mem1 += MAIN_MEM_r[1]

	r5_t0 = S.Task('r5_t0', length=6, delay_cost=1)
	S += r5_t0 >= 4
	r5_t0 += MM[0]

	r1_t0_in = S.Task('r1_t0_in', length=1, delay_cost=1)
	S += r1_t0_in >= 5
	r1_t0_in += MM_in[0]

	r1_t0_mem0 = S.Task('r1_t0_mem0', length=1, delay_cost=1)
	S += r1_t0_mem0 >= 5
	r1_t0_mem0 += MAIN_MEM_r[0]

	r1_t0_mem1 = S.Task('r1_t0_mem1', length=1, delay_cost=1)
	S += r1_t0_mem1 >= 5
	r1_t0_mem1 += MAIN_MEM_r[1]

	r4_t1 = S.Task('r4_t1', length=6, delay_cost=1)
	S += r4_t1 >= 5
	r4_t1 += MM[0]

	r13_t0_in = S.Task('r13_t0_in', length=1, delay_cost=1)
	S += r13_t0_in >= 6
	r13_t0_in += MM_in[0]

	r13_t0_mem0 = S.Task('r13_t0_mem0', length=1, delay_cost=1)
	S += r13_t0_mem0 >= 6
	r13_t0_mem0 += MAIN_MEM_r[0]

	r13_t0_mem1 = S.Task('r13_t0_mem1', length=1, delay_cost=1)
	S += r13_t0_mem1 >= 6
	r13_t0_mem1 += MAIN_MEM_r[1]

	r1_t0 = S.Task('r1_t0', length=6, delay_cost=1)
	S += r1_t0 >= 6
	r1_t0 += MM[0]

	r13_t0 = S.Task('r13_t0', length=6, delay_cost=1)
	S += r13_t0 >= 7
	r13_t0 += MM[0]

	r1_t2_in = S.Task('r1_t2_in', length=1, delay_cost=1)
	S += r1_t2_in >= 7
	r1_t2_in += MAS_in[0]

	r1_t2_mem0 = S.Task('r1_t2_mem0', length=1, delay_cost=1)
	S += r1_t2_mem0 >= 7
	r1_t2_mem0 += MAIN_MEM_r[0]

	r1_t2_mem1 = S.Task('r1_t2_mem1', length=1, delay_cost=1)
	S += r1_t2_mem1 >= 7
	r1_t2_mem1 += MAIN_MEM_r[1]

	r1_t2 = S.Task('r1_t2', length=2, delay_cost=1)
	S += r1_t2 >= 8
	r1_t2 += MAS[0]

	r4_t2_in = S.Task('r4_t2_in', length=1, delay_cost=1)
	S += r4_t2_in >= 8
	r4_t2_in += MAS_in[0]

	r4_t2_mem0 = S.Task('r4_t2_mem0', length=1, delay_cost=1)
	S += r4_t2_mem0 >= 8
	r4_t2_mem0 += MAIN_MEM_r[0]

	r4_t2_mem1 = S.Task('r4_t2_mem1', length=1, delay_cost=1)
	S += r4_t2_mem1 >= 8
	r4_t2_mem1 += MAIN_MEM_r[1]

	r4_t2 = S.Task('r4_t2', length=2, delay_cost=1)
	S += r4_t2 >= 9
	r4_t2 += MAS[0]

	r6_t3_in = S.Task('r6_t3_in', length=1, delay_cost=1)
	S += r6_t3_in >= 9
	r6_t3_in += MAS_in[0]

	r6_t3_mem0 = S.Task('r6_t3_mem0', length=1, delay_cost=1)
	S += r6_t3_mem0 >= 9
	r6_t3_mem0 += MAIN_MEM_r[0]

	r6_t3_mem1 = S.Task('r6_t3_mem1', length=1, delay_cost=1)
	S += r6_t3_mem1 >= 9
	r6_t3_mem1 += MAIN_MEM_r[1]

	r3_t1_in = S.Task('r3_t1_in', length=1, delay_cost=1)
	S += r3_t1_in >= 10
	r3_t1_in += MM_in[0]

	r3_t1_mem0 = S.Task('r3_t1_mem0', length=1, delay_cost=1)
	S += r3_t1_mem0 >= 10
	r3_t1_mem0 += MAIN_MEM_r[0]

	r3_t1_mem1 = S.Task('r3_t1_mem1', length=1, delay_cost=1)
	S += r3_t1_mem1 >= 10
	r3_t1_mem1 += MAIN_MEM_r[1]

	r6_t3 = S.Task('r6_t3', length=2, delay_cost=1)
	S += r6_t3 >= 10
	r6_t3 += MAS[0]

	r3_t1 = S.Task('r3_t1', length=6, delay_cost=1)
	S += r3_t1 >= 11
	r3_t1 += MM[0]

	r4_t0_in = S.Task('r4_t0_in', length=1, delay_cost=1)
	S += r4_t0_in >= 11
	r4_t0_in += MM_in[0]

	r4_t0_mem0 = S.Task('r4_t0_mem0', length=1, delay_cost=1)
	S += r4_t0_mem0 >= 11
	r4_t0_mem0 += MAIN_MEM_r[0]

	r4_t0_mem1 = S.Task('r4_t0_mem1', length=1, delay_cost=1)
	S += r4_t0_mem1 >= 11
	r4_t0_mem1 += MAIN_MEM_r[1]

	r1_t3_in = S.Task('r1_t3_in', length=1, delay_cost=1)
	S += r1_t3_in >= 12
	r1_t3_in += MAS_in[0]

	r1_t3_mem0 = S.Task('r1_t3_mem0', length=1, delay_cost=1)
	S += r1_t3_mem0 >= 12
	r1_t3_mem0 += MAIN_MEM_r[0]

	r1_t3_mem1 = S.Task('r1_t3_mem1', length=1, delay_cost=1)
	S += r1_t3_mem1 >= 12
	r1_t3_mem1 += MAIN_MEM_r[1]

	r4_t0 = S.Task('r4_t0', length=6, delay_cost=1)
	S += r4_t0 >= 12
	r4_t0 += MM[0]

	r1_t3 = S.Task('r1_t3', length=2, delay_cost=1)
	S += r1_t3 >= 13
	r1_t3 += MAS[0]

	r4_t3_in = S.Task('r4_t3_in', length=1, delay_cost=1)
	S += r4_t3_in >= 13
	r4_t3_in += MAS_in[0]

	r4_t3_mem0 = S.Task('r4_t3_mem0', length=1, delay_cost=1)
	S += r4_t3_mem0 >= 13
	r4_t3_mem0 += MAIN_MEM_r[0]

	r4_t3_mem1 = S.Task('r4_t3_mem1', length=1, delay_cost=1)
	S += r4_t3_mem1 >= 13
	r4_t3_mem1 += MAIN_MEM_r[1]

	r16_t3_in = S.Task('r16_t3_in', length=1, delay_cost=1)
	S += r16_t3_in >= 14
	r16_t3_in += MAS_in[0]

	r16_t3_mem0 = S.Task('r16_t3_mem0', length=1, delay_cost=1)
	S += r16_t3_mem0 >= 14
	r16_t3_mem0 += MAIN_MEM_r[0]

	r16_t3_mem1 = S.Task('r16_t3_mem1', length=1, delay_cost=1)
	S += r16_t3_mem1 >= 14
	r16_t3_mem1 += MAIN_MEM_r[1]

	r1_t4_in = S.Task('r1_t4_in', length=1, delay_cost=1)
	S += r1_t4_in >= 14
	r1_t4_in += MM_in[0]

	r1_t4_mem0 = S.Task('r1_t4_mem0', length=1, delay_cost=1)
	S += r1_t4_mem0 >= 14
	r1_t4_mem0 += MAS_MEM[0]

	r1_t4_mem1 = S.Task('r1_t4_mem1', length=1, delay_cost=1)
	S += r1_t4_mem1 >= 14
	r1_t4_mem1 += MAS_MEM[1]

	r4_t3 = S.Task('r4_t3', length=2, delay_cost=1)
	S += r4_t3 >= 14
	r4_t3 += MAS[0]

	r13_t2_in = S.Task('r13_t2_in', length=1, delay_cost=1)
	S += r13_t2_in >= 15
	r13_t2_in += MAS_in[0]

	r13_t2_mem0 = S.Task('r13_t2_mem0', length=1, delay_cost=1)
	S += r13_t2_mem0 >= 15
	r13_t2_mem0 += MAIN_MEM_r[0]

	r13_t2_mem1 = S.Task('r13_t2_mem1', length=1, delay_cost=1)
	S += r13_t2_mem1 >= 15
	r13_t2_mem1 += MAIN_MEM_r[1]

	r16_t3 = S.Task('r16_t3', length=2, delay_cost=1)
	S += r16_t3 >= 15
	r16_t3 += MAS[0]

	r1_t4 = S.Task('r1_t4', length=6, delay_cost=1)
	S += r1_t4 >= 15
	r1_t4 += MM[0]

	r4_t4_in = S.Task('r4_t4_in', length=1, delay_cost=1)
	S += r4_t4_in >= 15
	r4_t4_in += MM_in[0]

	r4_t4_mem0 = S.Task('r4_t4_mem0', length=1, delay_cost=1)
	S += r4_t4_mem0 >= 15
	r4_t4_mem0 += MAS_MEM[0]

	r4_t4_mem1 = S.Task('r4_t4_mem1', length=1, delay_cost=1)
	S += r4_t4_mem1 >= 15
	r4_t4_mem1 += MAS_MEM[1]

	r130_in = S.Task('r130_in', length=1, delay_cost=1)
	S += r130_in >= 16
	r130_in += MAS_in[0]

	r130_mem0 = S.Task('r130_mem0', length=1, delay_cost=1)
	S += r130_mem0 >= 16
	r130_mem0 += MM_MEM[0]

	r130_mem1 = S.Task('r130_mem1', length=1, delay_cost=1)
	S += r130_mem1 >= 16
	r130_mem1 += MM_MEM[1]

	r13_t2 = S.Task('r13_t2', length=2, delay_cost=1)
	S += r13_t2 >= 16
	r13_t2 += MAS[0]

	r4_t4 = S.Task('r4_t4', length=6, delay_cost=1)
	S += r4_t4 >= 16
	r4_t4 += MM[0]

	r6_t0_in = S.Task('r6_t0_in', length=1, delay_cost=1)
	S += r6_t0_in >= 16
	r6_t0_in += MM_in[0]

	r6_t0_mem0 = S.Task('r6_t0_mem0', length=1, delay_cost=1)
	S += r6_t0_mem0 >= 16
	r6_t0_mem0 += MAIN_MEM_r[0]

	r6_t0_mem1 = S.Task('r6_t0_mem1', length=1, delay_cost=1)
	S += r6_t0_mem1 >= 16
	r6_t0_mem1 += MAIN_MEM_r[1]

	r130 = S.Task('r130', length=2, delay_cost=1)
	S += r130 >= 17
	r130 += MAS[0]

	r6_t0 = S.Task('r6_t0', length=6, delay_cost=1)
	S += r6_t0 >= 17
	r6_t0 += MM[0]

	r9_t2_in = S.Task('r9_t2_in', length=1, delay_cost=1)
	S += r9_t2_in >= 17
	r9_t2_in += MAS_in[0]

	r9_t2_mem0 = S.Task('r9_t2_mem0', length=1, delay_cost=1)
	S += r9_t2_mem0 >= 17
	r9_t2_mem0 += MAIN_MEM_r[0]

	r9_t2_mem1 = S.Task('r9_t2_mem1', length=1, delay_cost=1)
	S += r9_t2_mem1 >= 17
	r9_t2_mem1 += MAIN_MEM_r[1]

	r3_t0_in = S.Task('r3_t0_in', length=1, delay_cost=1)
	S += r3_t0_in >= 18
	r3_t0_in += MM_in[0]

	r3_t0_mem0 = S.Task('r3_t0_mem0', length=1, delay_cost=1)
	S += r3_t0_mem0 >= 18
	r3_t0_mem0 += MAIN_MEM_r[0]

	r3_t0_mem1 = S.Task('r3_t0_mem1', length=1, delay_cost=1)
	S += r3_t0_mem1 >= 18
	r3_t0_mem1 += MAIN_MEM_r[1]

	r4_t5_in = S.Task('r4_t5_in', length=1, delay_cost=1)
	S += r4_t5_in >= 18
	r4_t5_in += MAS_in[0]

	r4_t5_mem0 = S.Task('r4_t5_mem0', length=1, delay_cost=1)
	S += r4_t5_mem0 >= 18
	r4_t5_mem0 += MM_MEM[0]

	r4_t5_mem1 = S.Task('r4_t5_mem1', length=1, delay_cost=1)
	S += r4_t5_mem1 >= 18
	r4_t5_mem1 += MM_MEM[1]

	r9_t2 = S.Task('r9_t2', length=2, delay_cost=1)
	S += r9_t2 >= 18
	r9_t2 += MAS[0]

	r13_t3_in = S.Task('r13_t3_in', length=1, delay_cost=1)
	S += r13_t3_in >= 19
	r13_t3_in += MAS_in[0]

	r13_t3_mem0 = S.Task('r13_t3_mem0', length=1, delay_cost=1)
	S += r13_t3_mem0 >= 19
	r13_t3_mem0 += MAIN_MEM_r[0]

	r13_t3_mem1 = S.Task('r13_t3_mem1', length=1, delay_cost=1)
	S += r13_t3_mem1 >= 19
	r13_t3_mem1 += MAIN_MEM_r[1]

	r3_t0 = S.Task('r3_t0', length=6, delay_cost=1)
	S += r3_t0 >= 19
	r3_t0 += MM[0]

	r4_t5 = S.Task('r4_t5', length=2, delay_cost=1)
	S += r4_t5 >= 19
	r4_t5 += MAS[0]

	r13_t3 = S.Task('r13_t3', length=2, delay_cost=1)
	S += r13_t3 >= 20
	r13_t3 += MAS[0]

	r3_t2_in = S.Task('r3_t2_in', length=1, delay_cost=1)
	S += r3_t2_in >= 20
	r3_t2_in += MAS_in[0]

	r3_t2_mem0 = S.Task('r3_t2_mem0', length=1, delay_cost=1)
	S += r3_t2_mem0 >= 20
	r3_t2_mem0 += MAIN_MEM_r[0]

	r3_t2_mem1 = S.Task('r3_t2_mem1', length=1, delay_cost=1)
	S += r3_t2_mem1 >= 20
	r3_t2_mem1 += MAIN_MEM_r[1]

	r13_t4_in = S.Task('r13_t4_in', length=1, delay_cost=1)
	S += r13_t4_in >= 21
	r13_t4_in += MM_in[0]

	r13_t4_mem0 = S.Task('r13_t4_mem0', length=1, delay_cost=1)
	S += r13_t4_mem0 >= 21
	r13_t4_mem0 += MAS_MEM[0]

	r13_t4_mem1 = S.Task('r13_t4_mem1', length=1, delay_cost=1)
	S += r13_t4_mem1 >= 21
	r13_t4_mem1 += MAS_MEM[1]

	r3_t2 = S.Task('r3_t2', length=2, delay_cost=1)
	S += r3_t2 >= 21
	r3_t2 += MAS[0]

	r6_t2_in = S.Task('r6_t2_in', length=1, delay_cost=1)
	S += r6_t2_in >= 21
	r6_t2_in += MAS_in[0]

	r6_t2_mem0 = S.Task('r6_t2_mem0', length=1, delay_cost=1)
	S += r6_t2_mem0 >= 21
	r6_t2_mem0 += MAIN_MEM_r[0]

	r6_t2_mem1 = S.Task('r6_t2_mem1', length=1, delay_cost=1)
	S += r6_t2_mem1 >= 21
	r6_t2_mem1 += MAIN_MEM_r[1]

	r13_t4 = S.Task('r13_t4', length=6, delay_cost=1)
	S += r13_t4 >= 22
	r13_t4 += MM[0]

	r3_t3_in = S.Task('r3_t3_in', length=1, delay_cost=1)
	S += r3_t3_in >= 22
	r3_t3_in += MAS_in[0]

	r3_t3_mem0 = S.Task('r3_t3_mem0', length=1, delay_cost=1)
	S += r3_t3_mem0 >= 22
	r3_t3_mem0 += MAIN_MEM_r[0]

	r3_t3_mem1 = S.Task('r3_t3_mem1', length=1, delay_cost=1)
	S += r3_t3_mem1 >= 22
	r3_t3_mem1 += MAIN_MEM_r[1]

	r6_t2 = S.Task('r6_t2', length=2, delay_cost=1)
	S += r6_t2 >= 22
	r6_t2 += MAS[0]

	r3_t3 = S.Task('r3_t3', length=2, delay_cost=1)
	S += r3_t3 >= 23
	r3_t3 += MAS[0]

	r5_t3_in = S.Task('r5_t3_in', length=1, delay_cost=1)
	S += r5_t3_in >= 23
	r5_t3_in += MAS_in[0]

	r5_t3_mem0 = S.Task('r5_t3_mem0', length=1, delay_cost=1)
	S += r5_t3_mem0 >= 23
	r5_t3_mem0 += MAIN_MEM_r[0]

	r5_t3_mem1 = S.Task('r5_t3_mem1', length=1, delay_cost=1)
	S += r5_t3_mem1 >= 23
	r5_t3_mem1 += MAIN_MEM_r[1]

	r6_t4_in = S.Task('r6_t4_in', length=1, delay_cost=1)
	S += r6_t4_in >= 23
	r6_t4_in += MM_in[0]

	r6_t4_mem0 = S.Task('r6_t4_mem0', length=1, delay_cost=1)
	S += r6_t4_mem0 >= 23
	r6_t4_mem0 += MAS_MEM[0]

	r6_t4_mem1 = S.Task('r6_t4_mem1', length=1, delay_cost=1)
	S += r6_t4_mem1 >= 23
	r6_t4_mem1 += MAS_MEM[1]

	r30_in = S.Task('r30_in', length=1, delay_cost=1)
	S += r30_in >= 24
	r30_in += MAS_in[0]

	r30_mem0 = S.Task('r30_mem0', length=1, delay_cost=1)
	S += r30_mem0 >= 24
	r30_mem0 += MM_MEM[0]

	r30_mem1 = S.Task('r30_mem1', length=1, delay_cost=1)
	S += r30_mem1 >= 24
	r30_mem1 += MM_MEM[1]

	r5_t1_in = S.Task('r5_t1_in', length=1, delay_cost=1)
	S += r5_t1_in >= 24
	r5_t1_in += MM_in[0]

	r5_t1_mem0 = S.Task('r5_t1_mem0', length=1, delay_cost=1)
	S += r5_t1_mem0 >= 24
	r5_t1_mem0 += MAIN_MEM_r[0]

	r5_t1_mem1 = S.Task('r5_t1_mem1', length=1, delay_cost=1)
	S += r5_t1_mem1 >= 24
	r5_t1_mem1 += MAIN_MEM_r[1]

	r5_t3 = S.Task('r5_t3', length=2, delay_cost=1)
	S += r5_t3 >= 24
	r5_t3 += MAS[0]

	r6_t4 = S.Task('r6_t4', length=6, delay_cost=1)
	S += r6_t4 >= 24
	r6_t4 += MM[0]

	r1_t1_in = S.Task('r1_t1_in', length=1, delay_cost=1)
	S += r1_t1_in >= 25
	r1_t1_in += MM_in[0]

	r1_t1_mem0 = S.Task('r1_t1_mem0', length=1, delay_cost=1)
	S += r1_t1_mem0 >= 25
	r1_t1_mem0 += MAIN_MEM_r[0]

	r1_t1_mem1 = S.Task('r1_t1_mem1', length=1, delay_cost=1)
	S += r1_t1_mem1 >= 25
	r1_t1_mem1 += MAIN_MEM_r[1]

	r30 = S.Task('r30', length=2, delay_cost=1)
	S += r30 >= 25
	r30 += MAS[0]

	r41_in = S.Task('r41_in', length=1, delay_cost=1)
	S += r41_in >= 25
	r41_in += MAS_in[0]

	r41_mem0 = S.Task('r41_mem0', length=1, delay_cost=1)
	S += r41_mem0 >= 25
	r41_mem0 += MM_MEM[0]

	r41_mem1 = S.Task('r41_mem1', length=1, delay_cost=1)
	S += r41_mem1 >= 25
	r41_mem1 += MAS_MEM[1]

	r5_t1 = S.Task('r5_t1', length=6, delay_cost=1)
	S += r5_t1 >= 25
	r5_t1 += MM[0]

	r12_t3_in = S.Task('r12_t3_in', length=1, delay_cost=1)
	S += r12_t3_in >= 26
	r12_t3_in += MAS_in[0]

	r12_t3_mem0 = S.Task('r12_t3_mem0', length=1, delay_cost=1)
	S += r12_t3_mem0 >= 26
	r12_t3_mem0 += MAIN_MEM_r[0]

	r12_t3_mem1 = S.Task('r12_t3_mem1', length=1, delay_cost=1)
	S += r12_t3_mem1 >= 26
	r12_t3_mem1 += MAIN_MEM_r[1]

	r1_t1 = S.Task('r1_t1', length=6, delay_cost=1)
	S += r1_t1 >= 26
	r1_t1 += MM[0]

	r3_t4_in = S.Task('r3_t4_in', length=1, delay_cost=1)
	S += r3_t4_in >= 26
	r3_t4_in += MM_in[0]

	r3_t4_mem0 = S.Task('r3_t4_mem0', length=1, delay_cost=1)
	S += r3_t4_mem0 >= 26
	r3_t4_mem0 += MAS_MEM[0]

	r3_t4_mem1 = S.Task('r3_t4_mem1', length=1, delay_cost=1)
	S += r3_t4_mem1 >= 26
	r3_t4_mem1 += MAS_MEM[1]

	r41 = S.Task('r41', length=2, delay_cost=1)
	S += r41 >= 26
	r41 += MAS[0]

	r12_t2_in = S.Task('r12_t2_in', length=1, delay_cost=1)
	S += r12_t2_in >= 27
	r12_t2_in += MAS_in[0]

	r12_t2_mem0 = S.Task('r12_t2_mem0', length=1, delay_cost=1)
	S += r12_t2_mem0 >= 27
	r12_t2_mem0 += MAIN_MEM_r[0]

	r12_t2_mem1 = S.Task('r12_t2_mem1', length=1, delay_cost=1)
	S += r12_t2_mem1 >= 27
	r12_t2_mem1 += MAIN_MEM_r[1]

	r12_t3 = S.Task('r12_t3', length=2, delay_cost=1)
	S += r12_t3 >= 27
	r12_t3 += MAS[0]

	r3_t4 = S.Task('r3_t4', length=6, delay_cost=1)
	S += r3_t4 >= 27
	r3_t4 += MM[0]

	r5_t4_in = S.Task('r5_t4_in', length=1, delay_cost=1)
	S += r5_t4_in >= 27
	r5_t4_in += MM_in[0]

	r5_t4_mem0 = S.Task('r5_t4_mem0', length=1, delay_cost=1)
	S += r5_t4_mem0 >= 27
	r5_t4_mem0 += MAS_MEM[0]

	r5_t4_mem1 = S.Task('r5_t4_mem1', length=1, delay_cost=1)
	S += r5_t4_mem1 >= 27
	r5_t4_mem1 += MAS_MEM[1]

	r12_t1_in = S.Task('r12_t1_in', length=1, delay_cost=1)
	S += r12_t1_in >= 28
	r12_t1_in += MM_in[0]

	r12_t1_mem0 = S.Task('r12_t1_mem0', length=1, delay_cost=1)
	S += r12_t1_mem0 >= 28
	r12_t1_mem0 += MAIN_MEM_r[0]

	r12_t1_mem1 = S.Task('r12_t1_mem1', length=1, delay_cost=1)
	S += r12_t1_mem1 >= 28
	r12_t1_mem1 += MAIN_MEM_r[1]

	r12_t2 = S.Task('r12_t2', length=2, delay_cost=1)
	S += r12_t2 >= 28
	r12_t2 += MAS[0]

	r5_t4 = S.Task('r5_t4', length=6, delay_cost=1)
	S += r5_t4 >= 28
	r5_t4 += MM[0]

	r60_in = S.Task('r60_in', length=1, delay_cost=1)
	S += r60_in >= 28
	r60_in += MAS_in[0]

	r60_mem0 = S.Task('r60_mem0', length=1, delay_cost=1)
	S += r60_mem0 >= 28
	r60_mem0 += MM_MEM[0]

	r60_mem1 = S.Task('r60_mem1', length=1, delay_cost=1)
	S += r60_mem1 >= 28
	r60_mem1 += MM_MEM[1]

	r12_t0_in = S.Task('r12_t0_in', length=1, delay_cost=1)
	S += r12_t0_in >= 29
	r12_t0_in += MM_in[0]

	r12_t0_mem0 = S.Task('r12_t0_mem0', length=1, delay_cost=1)
	S += r12_t0_mem0 >= 29
	r12_t0_mem0 += MAIN_MEM_r[0]

	r12_t0_mem1 = S.Task('r12_t0_mem1', length=1, delay_cost=1)
	S += r12_t0_mem1 >= 29
	r12_t0_mem1 += MAIN_MEM_r[1]

	r12_t1 = S.Task('r12_t1', length=6, delay_cost=1)
	S += r12_t1 >= 29
	r12_t1 += MM[0]

	r60 = S.Task('r60', length=2, delay_cost=1)
	S += r60 >= 29
	r60 += MAS[0]

	r6_t5_in = S.Task('r6_t5_in', length=1, delay_cost=1)
	S += r6_t5_in >= 29
	r6_t5_in += MAS_in[0]

	r6_t5_mem0 = S.Task('r6_t5_mem0', length=1, delay_cost=1)
	S += r6_t5_mem0 >= 29
	r6_t5_mem0 += MM_MEM[0]

	r6_t5_mem1 = S.Task('r6_t5_mem1', length=1, delay_cost=1)
	S += r6_t5_mem1 >= 29
	r6_t5_mem1 += MM_MEM[1]

	r12_t0 = S.Task('r12_t0', length=6, delay_cost=1)
	S += r12_t0 >= 30
	r12_t0 += MM[0]

	r12_t4_in = S.Task('r12_t4_in', length=1, delay_cost=1)
	S += r12_t4_in >= 30
	r12_t4_in += MM_in[0]

	r12_t4_mem0 = S.Task('r12_t4_mem0', length=1, delay_cost=1)
	S += r12_t4_mem0 >= 30
	r12_t4_mem0 += MAS_MEM[0]

	r12_t4_mem1 = S.Task('r12_t4_mem1', length=1, delay_cost=1)
	S += r12_t4_mem1 >= 30
	r12_t4_mem1 += MAS_MEM[1]

	r50_in = S.Task('r50_in', length=1, delay_cost=1)
	S += r50_in >= 30
	r50_in += MAS_in[0]

	r50_mem0 = S.Task('r50_mem0', length=1, delay_cost=1)
	S += r50_mem0 >= 30
	r50_mem0 += MM_MEM[0]

	r50_mem1 = S.Task('r50_mem1', length=1, delay_cost=1)
	S += r50_mem1 >= 30
	r50_mem1 += MM_MEM[1]

	r6_t5 = S.Task('r6_t5', length=2, delay_cost=1)
	S += r6_t5 >= 30
	r6_t5 += MAS[0]

	r10_in = S.Task('r10_in', length=1, delay_cost=1)
	S += r10_in >= 31
	r10_in += MAS_in[0]

	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	S += r10_mem0 >= 31
	r10_mem0 += MM_MEM[0]

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	S += r10_mem1 >= 31
	r10_mem1 += MM_MEM[1]

	r12_t4 = S.Task('r12_t4', length=6, delay_cost=1)
	S += r12_t4 >= 31
	r12_t4 += MM[0]

	r50 = S.Task('r50', length=2, delay_cost=1)
	S += r50 >= 31
	r50 += MAS[0]

	r10 = S.Task('r10', length=2, delay_cost=1)
	S += r10 >= 32
	r10 += MAS[0]

	r70_in = S.Task('r70_in', length=1, delay_cost=1)
	S += r70_in >= 32
	r70_in += MAS_in[0]

	r70_mem0 = S.Task('r70_mem0', length=1, delay_cost=1)
	S += r70_mem0 >= 32
	r70_mem0 += MAS_MEM[0]

	r70_mem1 = S.Task('r70_mem1', length=1, delay_cost=1)
	S += r70_mem1 >= 32
	r70_mem1 += MAS_MEM[1]

	r20_in = S.Task('r20_in', length=1, delay_cost=1)
	S += r20_in >= 33
	r20_in += MAS_in[0]

	r20_mem0 = S.Task('r20_mem0', length=1, delay_cost=1)
	S += r20_mem0 >= 33
	r20_mem0 += MAS_MEM[0]

	r20_mem1 = S.Task('r20_mem1', length=1, delay_cost=1)
	S += r20_mem1 >= 33
	r20_mem1 += MAS_MEM[1]

	r70 = S.Task('r70', length=2, delay_cost=1)
	S += r70 >= 33
	r70 += MAS[0]

	r20 = S.Task('r20', length=2, delay_cost=1)
	S += r20 >= 34
	r20 += MAS[0]

	r5_t5_in = S.Task('r5_t5_in', length=1, delay_cost=1)
	S += r5_t5_in >= 34
	r5_t5_in += MAS_in[0]

	r5_t5_mem0 = S.Task('r5_t5_mem0', length=1, delay_cost=1)
	S += r5_t5_mem0 >= 34
	r5_t5_mem0 += MM_MEM[0]

	r5_t5_mem1 = S.Task('r5_t5_mem1', length=1, delay_cost=1)
	S += r5_t5_mem1 >= 34
	r5_t5_mem1 += MM_MEM[1]

	r9_t0_in = S.Task('r9_t0_in', length=1, delay_cost=1)
	S += r9_t0_in >= 34
	r9_t0_in += MM_in[0]

	r9_t0_mem0 = S.Task('r9_t0_mem0', length=1, delay_cost=1)
	S += r9_t0_mem0 >= 34
	r9_t0_mem0 += MAIN_MEM_r[0]

	r9_t0_mem1 = S.Task('r9_t0_mem1', length=1, delay_cost=1)
	S += r9_t0_mem1 >= 34
	r9_t0_mem1 += MAS_MEM[1]

	Z_new_t0_in = S.Task('Z_new_t0_in', length=1, delay_cost=1)
	S += Z_new_t0_in >= 35
	Z_new_t0_in += MM_in[0]

	Z_new_t0_mem0 = S.Task('Z_new_t0_mem0', length=1, delay_cost=1)
	S += Z_new_t0_mem0 >= 35
	Z_new_t0_mem0 += MAS_MEM[0]

	Z_new_t0_mem1 = S.Task('Z_new_t0_mem1', length=1, delay_cost=1)
	S += Z_new_t0_mem1 >= 35
	Z_new_t0_mem1 += MAS_MEM[1]

	r120_in = S.Task('r120_in', length=1, delay_cost=1)
	S += r120_in >= 35
	r120_in += MAS_in[0]

	r120_mem0 = S.Task('r120_mem0', length=1, delay_cost=1)
	S += r120_mem0 >= 35
	r120_mem0 += MM_MEM[0]

	r120_mem1 = S.Task('r120_mem1', length=1, delay_cost=1)
	S += r120_mem1 >= 35
	r120_mem1 += MM_MEM[1]

	r5_t5 = S.Task('r5_t5', length=2, delay_cost=1)
	S += r5_t5 >= 35
	r5_t5 += MAS[0]

	r9_t0 = S.Task('r9_t0', length=6, delay_cost=1)
	S += r9_t0 >= 35
	r9_t0 += MM[0]

	Z_new_t0 = S.Task('Z_new_t0', length=6, delay_cost=1)
	S += Z_new_t0 >= 36
	Z_new_t0 += MM[0]

	r120 = S.Task('r120', length=2, delay_cost=1)
	S += r120 >= 36
	r120 += MAS[0]

	r14_t0_in = S.Task('r14_t0_in', length=1, delay_cost=1)
	S += r14_t0_in >= 36
	r14_t0_in += MM_in[0]

	r14_t0_mem0 = S.Task('r14_t0_mem0', length=1, delay_cost=1)
	S += r14_t0_mem0 >= 36
	r14_t0_mem0 += MAS_MEM[0]

	r14_t0_mem1 = S.Task('r14_t0_mem1', length=1, delay_cost=1)
	S += r14_t0_mem1 >= 36
	r14_t0_mem1 += MAS_MEM[1]

	r3_t5_in = S.Task('r3_t5_in', length=1, delay_cost=1)
	S += r3_t5_in >= 36
	r3_t5_in += MAS_in[0]

	r3_t5_mem0 = S.Task('r3_t5_mem0', length=1, delay_cost=1)
	S += r3_t5_mem0 >= 36
	r3_t5_mem0 += MM_MEM[0]

	r3_t5_mem1 = S.Task('r3_t5_mem1', length=1, delay_cost=1)
	S += r3_t5_mem1 >= 36
	r3_t5_mem1 += MM_MEM[1]

	X_new_t0_in = S.Task('X_new_t0_in', length=1, delay_cost=1)
	S += X_new_t0_in >= 37
	X_new_t0_in += MM_in[0]

	X_new_t0_mem0 = S.Task('X_new_t0_mem0', length=1, delay_cost=1)
	S += X_new_t0_mem0 >= 37
	X_new_t0_mem0 += MAS_MEM[0]

	X_new_t0_mem1 = S.Task('X_new_t0_mem1', length=1, delay_cost=1)
	S += X_new_t0_mem1 >= 37
	X_new_t0_mem1 += MAS_MEM[1]

	r14_t0 = S.Task('r14_t0', length=6, delay_cost=1)
	S += r14_t0 >= 37
	r14_t0 += MM[0]

	r1_t5_in = S.Task('r1_t5_in', length=1, delay_cost=1)
	S += r1_t5_in >= 37
	r1_t5_in += MAS_in[0]

	r1_t5_mem0 = S.Task('r1_t5_mem0', length=1, delay_cost=1)
	S += r1_t5_mem0 >= 37
	r1_t5_mem0 += MM_MEM[0]

	r1_t5_mem1 = S.Task('r1_t5_mem1', length=1, delay_cost=1)
	S += r1_t5_mem1 >= 37
	r1_t5_mem1 += MM_MEM[1]

	r3_t5 = S.Task('r3_t5', length=2, delay_cost=1)
	S += r3_t5 >= 37
	r3_t5 += MAS[0]

	X_new_t0 = S.Task('X_new_t0', length=6, delay_cost=1)
	S += X_new_t0 >= 38
	X_new_t0 += MM[0]

	r1_t5 = S.Task('r1_t5', length=2, delay_cost=1)
	S += r1_t5 >= 38
	r1_t5 += MAS[0]

	r51_in = S.Task('r51_in', length=1, delay_cost=1)
	S += r51_in >= 38
	r51_in += MAS_in[0]

	r51_mem0 = S.Task('r51_mem0', length=1, delay_cost=1)
	S += r51_mem0 >= 38
	r51_mem0 += MM_MEM[0]

	r51_mem1 = S.Task('r51_mem1', length=1, delay_cost=1)
	S += r51_mem1 >= 38
	r51_mem1 += MAS_MEM[1]

	r51 = S.Task('r51', length=2, delay_cost=1)
	S += r51 >= 39
	r51 += MAS[0]

	r61_in = S.Task('r61_in', length=1, delay_cost=1)
	S += r61_in >= 39
	r61_in += MAS_in[0]

	r61_mem0 = S.Task('r61_mem0', length=1, delay_cost=1)
	S += r61_mem0 >= 39
	r61_mem0 += MM_MEM[0]

	r61_mem1 = S.Task('r61_mem1', length=1, delay_cost=1)
	S += r61_mem1 >= 39
	r61_mem1 += MAS_MEM[1]

	r40_in = S.Task('r40_in', length=1, delay_cost=1)
	S += r40_in >= 40
	r40_in += MAS_in[0]

	r40_mem0 = S.Task('r40_mem0', length=1, delay_cost=1)
	S += r40_mem0 >= 40
	r40_mem0 += MM_MEM[0]

	r40_mem1 = S.Task('r40_mem1', length=1, delay_cost=1)
	S += r40_mem1 >= 40
	r40_mem1 += MM_MEM[1]

	r61 = S.Task('r61', length=2, delay_cost=1)
	S += r61 >= 40
	r61 += MAS[0]

	r40 = S.Task('r40', length=2, delay_cost=1)
	S += r40 >= 41
	r40 += MAS[0]

	r71_in = S.Task('r71_in', length=1, delay_cost=1)
	S += r71_in >= 41
	r71_in += MAS_in[0]

	r71_mem0 = S.Task('r71_mem0', length=1, delay_cost=1)
	S += r71_mem0 >= 41
	r71_mem0 += MAS_MEM[0]

	r71_mem1 = S.Task('r71_mem1', length=1, delay_cost=1)
	S += r71_mem1 >= 41
	r71_mem1 += MAS_MEM[1]

	r71 = S.Task('r71', length=2, delay_cost=1)
	S += r71 >= 42
	r71 += MAS[0]

	r80_in = S.Task('r80_in', length=1, delay_cost=1)
	S += r80_in >= 42
	r80_in += MAS_in[0]

	r80_mem0 = S.Task('r80_mem0', length=1, delay_cost=1)
	S += r80_mem0 >= 42
	r80_mem0 += MAIN_MEM_r[0]

	r80_mem1 = S.Task('r80_mem1', length=1, delay_cost=1)
	S += r80_mem1 >= 42
	r80_mem1 += MAS_MEM[1]

	r31_in = S.Task('r31_in', length=1, delay_cost=1)
	S += r31_in >= 43
	r31_in += MAS_in[0]

	r31_mem0 = S.Task('r31_mem0', length=1, delay_cost=1)
	S += r31_mem0 >= 43
	r31_mem0 += MM_MEM[0]

	r31_mem1 = S.Task('r31_mem1', length=1, delay_cost=1)
	S += r31_mem1 >= 43
	r31_mem1 += MAS_MEM[1]

	r80 = S.Task('r80', length=2, delay_cost=1)
	S += r80 >= 43
	r80 += MAS[0]

	r13_t5_in = S.Task('r13_t5_in', length=1, delay_cost=1)
	S += r13_t5_in >= 44
	r13_t5_in += MAS_in[0]

	r13_t5_mem0 = S.Task('r13_t5_mem0', length=1, delay_cost=1)
	S += r13_t5_mem0 >= 44
	r13_t5_mem0 += MM_MEM[0]

	r13_t5_mem1 = S.Task('r13_t5_mem1', length=1, delay_cost=1)
	S += r13_t5_mem1 >= 44
	r13_t5_mem1 += MM_MEM[1]

	r31 = S.Task('r31', length=2, delay_cost=1)
	S += r31 >= 44
	r31 += MAS[0]

	r9_t1_in = S.Task('r9_t1_in', length=1, delay_cost=1)
	S += r9_t1_in >= 44
	r9_t1_in += MM_in[0]

	r9_t1_mem0 = S.Task('r9_t1_mem0', length=1, delay_cost=1)
	S += r9_t1_mem0 >= 44
	r9_t1_mem0 += MAIN_MEM_r[0]

	r9_t1_mem1 = S.Task('r9_t1_mem1', length=1, delay_cost=1)
	S += r9_t1_mem1 >= 44
	r9_t1_mem1 += MAS_MEM[1]

	r13_t5 = S.Task('r13_t5', length=2, delay_cost=1)
	S += r13_t5 >= 45
	r13_t5 += MAS[0]

	r81_in = S.Task('r81_in', length=1, delay_cost=1)
	S += r81_in >= 45
	r81_in += MAS_in[0]

	r81_mem0 = S.Task('r81_mem0', length=1, delay_cost=1)
	S += r81_mem0 >= 45
	r81_mem0 += MAIN_MEM_r[0]

	r81_mem1 = S.Task('r81_mem1', length=1, delay_cost=1)
	S += r81_mem1 >= 45
	r81_mem1 += MAS_MEM[1]

	r9_t1 = S.Task('r9_t1', length=6, delay_cost=1)
	S += r9_t1 >= 45
	r9_t1 += MM[0]

	r14_t3_in = S.Task('r14_t3_in', length=1, delay_cost=1)
	S += r14_t3_in >= 46
	r14_t3_in += MAS_in[0]

	r14_t3_mem0 = S.Task('r14_t3_mem0', length=1, delay_cost=1)
	S += r14_t3_mem0 >= 46
	r14_t3_mem0 += MAS_MEM[0]

	r14_t3_mem1 = S.Task('r14_t3_mem1', length=1, delay_cost=1)
	S += r14_t3_mem1 >= 46
	r14_t3_mem1 += MAS_MEM[1]

	r81 = S.Task('r81', length=2, delay_cost=1)
	S += r81 >= 46
	r81 += MAS[0]

	r11_in = S.Task('r11_in', length=1, delay_cost=1)
	S += r11_in >= 47
	r11_in += MAS_in[0]

	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	S += r11_mem0 >= 47
	r11_mem0 += MM_MEM[0]

	r11_mem1 = S.Task('r11_mem1', length=1, delay_cost=1)
	S += r11_mem1 >= 47
	r11_mem1 += MAS_MEM[1]

	r14_t3 = S.Task('r14_t3', length=2, delay_cost=1)
	S += r14_t3 >= 47
	r14_t3 += MAS[0]

	r11 = S.Task('r11', length=2, delay_cost=1)
	S += r11 >= 48
	r11 += MAS[0]

	r12_t5_in = S.Task('r12_t5_in', length=1, delay_cost=1)
	S += r12_t5_in >= 48
	r12_t5_in += MAS_in[0]

	r12_t5_mem0 = S.Task('r12_t5_mem0', length=1, delay_cost=1)
	S += r12_t5_mem0 >= 48
	r12_t5_mem0 += MM_MEM[0]

	r12_t5_mem1 = S.Task('r12_t5_mem1', length=1, delay_cost=1)
	S += r12_t5_mem1 >= 48
	r12_t5_mem1 += MM_MEM[1]

	r12_t5 = S.Task('r12_t5', length=2, delay_cost=1)
	S += r12_t5 >= 49
	r12_t5 += MAS[0]

	r131_in = S.Task('r131_in', length=1, delay_cost=1)
	S += r131_in >= 49
	r131_in += MAS_in[0]

	r131_mem0 = S.Task('r131_mem0', length=1, delay_cost=1)
	S += r131_mem0 >= 49
	r131_mem0 += MM_MEM[0]

	r131_mem1 = S.Task('r131_mem1', length=1, delay_cost=1)
	S += r131_mem1 >= 49
	r131_mem1 += MAS_MEM[1]

	r131 = S.Task('r131', length=2, delay_cost=1)
	S += r131 >= 50
	r131 += MAS[0]

	r21_in = S.Task('r21_in', length=1, delay_cost=1)
	S += r21_in >= 50
	r21_in += MAS_in[0]

	r21_mem0 = S.Task('r21_mem0', length=1, delay_cost=1)
	S += r21_mem0 >= 50
	r21_mem0 += MAS_MEM[0]

	r21_mem1 = S.Task('r21_mem1', length=1, delay_cost=1)
	S += r21_mem1 >= 50
	r21_mem1 += MAS_MEM[1]

	r121_in = S.Task('r121_in', length=1, delay_cost=1)
	S += r121_in >= 51
	r121_in += MAS_in[0]

	r121_mem0 = S.Task('r121_mem0', length=1, delay_cost=1)
	S += r121_mem0 >= 51
	r121_mem0 += MM_MEM[0]

	r121_mem1 = S.Task('r121_mem1', length=1, delay_cost=1)
	S += r121_mem1 >= 51
	r121_mem1 += MAS_MEM[1]

	r21 = S.Task('r21', length=2, delay_cost=1)
	S += r21 >= 51
	r21 += MAS[0]

	r101_in = S.Task('r101_in', length=1, delay_cost=1)
	S += r101_in >= 52
	r101_in += MAS_in[0]

	r101_mem0 = S.Task('r101_mem0', length=1, delay_cost=1)
	S += r101_mem0 >= 52
	r101_mem0 += MAIN_MEM_r[0]

	r101_mem1 = S.Task('r101_mem1', length=1, delay_cost=1)
	S += r101_mem1 >= 52
	r101_mem1 += MAS_MEM[1]

	r121 = S.Task('r121', length=2, delay_cost=1)
	S += r121 >= 52
	r121 += MAS[0]

	r100_in = S.Task('r100_in', length=1, delay_cost=1)
	S += r100_in >= 53
	r100_in += MAS_in[0]

	r100_mem0 = S.Task('r100_mem0', length=1, delay_cost=1)
	S += r100_mem0 >= 53
	r100_mem0 += MAIN_MEM_r[0]

	r100_mem1 = S.Task('r100_mem1', length=1, delay_cost=1)
	S += r100_mem1 >= 53
	r100_mem1 += MAS_MEM[1]

	r101 = S.Task('r101', length=2, delay_cost=1)
	S += r101 >= 53
	r101 += MAS[0]

	Z_new_t3_in = S.Task('Z_new_t3_in', length=1, delay_cost=1)
	S += Z_new_t3_in >= 54
	Z_new_t3_in += MAS_in[0]

	Z_new_t3_mem0 = S.Task('Z_new_t3_mem0', length=1, delay_cost=1)
	S += Z_new_t3_mem0 >= 54
	Z_new_t3_mem0 += MAS_MEM[0]

	Z_new_t3_mem1 = S.Task('Z_new_t3_mem1', length=1, delay_cost=1)
	S += Z_new_t3_mem1 >= 54
	Z_new_t3_mem1 += MAS_MEM[1]

	r100 = S.Task('r100', length=2, delay_cost=1)
	S += r100 >= 54
	r100 += MAS[0]

	X_new_t3_in = S.Task('X_new_t3_in', length=1, delay_cost=1)
	S += X_new_t3_in >= 55
	X_new_t3_in += MAS_in[0]

	X_new_t3_mem0 = S.Task('X_new_t3_mem0', length=1, delay_cost=1)
	S += X_new_t3_mem0 >= 55
	X_new_t3_mem0 += MAS_MEM[0]

	X_new_t3_mem1 = S.Task('X_new_t3_mem1', length=1, delay_cost=1)
	S += X_new_t3_mem1 >= 55
	X_new_t3_mem1 += MAS_MEM[1]

	Z_new_t3 = S.Task('Z_new_t3', length=2, delay_cost=1)
	S += Z_new_t3 >= 55
	Z_new_t3 += MAS[0]

	X_new_t1_in = S.Task('X_new_t1_in', length=1, delay_cost=1)
	S += X_new_t1_in >= 56
	X_new_t1_in += MM_in[0]

	X_new_t1_mem0 = S.Task('X_new_t1_mem0', length=1, delay_cost=1)
	S += X_new_t1_mem0 >= 56
	X_new_t1_mem0 += MAS_MEM[0]

	X_new_t1_mem1 = S.Task('X_new_t1_mem1', length=1, delay_cost=1)
	S += X_new_t1_mem1 >= 56
	X_new_t1_mem1 += MAS_MEM[1]

	X_new_t3 = S.Task('X_new_t3', length=2, delay_cost=1)
	S += X_new_t3 >= 56
	X_new_t3 += MAS[0]

	r9_t5_in = S.Task('r9_t5_in', length=1, delay_cost=1)
	S += r9_t5_in >= 56
	r9_t5_in += MAS_in[0]

	r9_t5_mem0 = S.Task('r9_t5_mem0', length=1, delay_cost=1)
	S += r9_t5_mem0 >= 56
	r9_t5_mem0 += MM_MEM[0]

	r9_t5_mem1 = S.Task('r9_t5_mem1', length=1, delay_cost=1)
	S += r9_t5_mem1 >= 56
	r9_t5_mem1 += MM_MEM[1]

	X_new_t1 = S.Task('X_new_t1', length=6, delay_cost=1)
	S += X_new_t1 >= 57
	X_new_t1 += MM[0]

	r11_t3_in = S.Task('r11_t3_in', length=1, delay_cost=1)
	S += r11_t3_in >= 57
	r11_t3_in += MM_in[0]

	r11_t3_mem0 = S.Task('r11_t3_mem0', length=1, delay_cost=1)
	S += r11_t3_mem0 >= 57
	r11_t3_mem0 += MAS_MEM[0]

	r11_t3_mem1 = S.Task('r11_t3_mem1', length=1, delay_cost=1)
	S += r11_t3_mem1 >= 57
	r11_t3_mem1 += MAS_MEM[1]

	r90_in = S.Task('r90_in', length=1, delay_cost=1)
	S += r90_in >= 57
	r90_in += MAS_in[0]

	r90_mem0 = S.Task('r90_mem0', length=1, delay_cost=1)
	S += r90_mem0 >= 57
	r90_mem0 += MM_MEM[0]

	r90_mem1 = S.Task('r90_mem1', length=1, delay_cost=1)
	S += r90_mem1 >= 57
	r90_mem1 += MM_MEM[1]

	r9_t5 = S.Task('r9_t5', length=2, delay_cost=1)
	S += r9_t5 >= 57
	r9_t5 += MAS[0]

	r11_t1_in = S.Task('r11_t1_in', length=1, delay_cost=1)
	S += r11_t1_in >= 58
	r11_t1_in += MAS_in[0]

	r11_t1_mem0 = S.Task('r11_t1_mem0', length=1, delay_cost=1)
	S += r11_t1_mem0 >= 58
	r11_t1_mem0 += MAS_MEM[0]

	r11_t1_mem1 = S.Task('r11_t1_mem1', length=1, delay_cost=1)
	S += r11_t1_mem1 >= 58
	r11_t1_mem1 += MAS_MEM[1]

	r11_t3 = S.Task('r11_t3', length=6, delay_cost=1)
	S += r11_t3 >= 58
	r11_t3 += MM[0]

	r90 = S.Task('r90', length=2, delay_cost=1)
	S += r90 >= 58
	r90 += MAS[0]

	r11_t1 = S.Task('r11_t1', length=2, delay_cost=1)
	S += r11_t1 >= 59
	r11_t1 += MAS[0]

	r9_t3_in = S.Task('r9_t3_in', length=1, delay_cost=1)
	S += r9_t3_in >= 59
	r9_t3_in += MAS_in[0]

	r9_t3_mem0 = S.Task('r9_t3_mem0', length=1, delay_cost=1)
	S += r9_t3_mem0 >= 59
	r9_t3_mem0 += MAS_MEM[0]

	r9_t3_mem1 = S.Task('r9_t3_mem1', length=1, delay_cost=1)
	S += r9_t3_mem1 >= 59
	r9_t3_mem1 += MAS_MEM[1]

	r11_t0_in = S.Task('r11_t0_in', length=1, delay_cost=1)
	S += r11_t0_in >= 60
	r11_t0_in += MAS_in[0]

	r11_t0_mem0 = S.Task('r11_t0_mem0', length=1, delay_cost=1)
	S += r11_t0_mem0 >= 60
	r11_t0_mem0 += MAS_MEM[0]

	r11_t0_mem1 = S.Task('r11_t0_mem1', length=1, delay_cost=1)
	S += r11_t0_mem1 >= 60
	r11_t0_mem1 += MAS_MEM[1]

	r9_t3 = S.Task('r9_t3', length=2, delay_cost=1)
	S += r9_t3 >= 60
	r9_t3 += MAS[0]

	X_new_t2_in = S.Task('X_new_t2_in', length=1, delay_cost=1)
	S += X_new_t2_in >= 61
	X_new_t2_in += MAS_in[0]

	X_new_t2_mem0 = S.Task('X_new_t2_mem0', length=1, delay_cost=1)
	S += X_new_t2_mem0 >= 61
	X_new_t2_mem0 += MAS_MEM[0]

	X_new_t2_mem1 = S.Task('X_new_t2_mem1', length=1, delay_cost=1)
	S += X_new_t2_mem1 >= 61
	X_new_t2_mem1 += MAS_MEM[1]

	r11_t0 = S.Task('r11_t0', length=2, delay_cost=1)
	S += r11_t0 >= 61
	r11_t0 += MAS[0]

	X_new0_in = S.Task('X_new0_in', length=1, delay_cost=1)
	S += X_new0_in >= 62
	X_new0_in += MAS_in[0]

	X_new0_mem0 = S.Task('X_new0_mem0', length=1, delay_cost=1)
	S += X_new0_mem0 >= 62
	X_new0_mem0 += MM_MEM[0]

	X_new0_mem1 = S.Task('X_new0_mem1', length=1, delay_cost=1)
	S += X_new0_mem1 >= 62
	X_new0_mem1 += MM_MEM[1]

	X_new_t2 = S.Task('X_new_t2', length=2, delay_cost=1)
	S += X_new_t2 >= 62
	X_new_t2 += MAS[0]

	r11_t2_in = S.Task('r11_t2_in', length=1, delay_cost=1)
	S += r11_t2_in >= 62
	r11_t2_in += MM_in[0]

	r11_t2_mem0 = S.Task('r11_t2_mem0', length=1, delay_cost=1)
	S += r11_t2_mem0 >= 62
	r11_t2_mem0 += MAS_MEM[0]

	r11_t2_mem1 = S.Task('r11_t2_mem1', length=1, delay_cost=1)
	S += r11_t2_mem1 >= 62
	r11_t2_mem1 += MAS_MEM[1]

	X_new0 = S.Task('X_new0', length=2, delay_cost=1)
	S += X_new0 >= 63
	X_new0 += MAS[0]

	Z_new_t1_in = S.Task('Z_new_t1_in', length=1, delay_cost=1)
	S += Z_new_t1_in >= 63
	Z_new_t1_in += MM_in[0]

	Z_new_t1_mem0 = S.Task('Z_new_t1_mem0', length=1, delay_cost=1)
	S += Z_new_t1_mem0 >= 63
	Z_new_t1_mem0 += MAS_MEM[0]

	Z_new_t1_mem1 = S.Task('Z_new_t1_mem1', length=1, delay_cost=1)
	S += Z_new_t1_mem1 >= 63
	Z_new_t1_mem1 += MAS_MEM[1]

	r111_in = S.Task('r111_in', length=1, delay_cost=1)
	S += r111_in >= 63
	r111_in += MAS_in[0]

	r111_mem0 = S.Task('r111_mem0', length=1, delay_cost=1)
	S += r111_mem0 >= 63
	r111_mem0 += MM_MEM[0]

	r111_mem1 = S.Task('r111_mem1', length=1, delay_cost=1)
	S += r111_mem1 >= 63
	r111_mem1 += MM_MEM[1]

	r11_t2 = S.Task('r11_t2', length=6, delay_cost=1)
	S += r11_t2 >= 63
	r11_t2 += MM[0]

	Z_new_t1 = S.Task('Z_new_t1', length=6, delay_cost=1)
	S += Z_new_t1 >= 64
	Z_new_t1 += MM[0]

	r111 = S.Task('r111', length=2, delay_cost=1)
	S += r111 >= 64
	r111 += MAS[0]

	r11_t5_in = S.Task('r11_t5_in', length=1, delay_cost=1)
	S += r11_t5_in >= 64
	r11_t5_in += MAS_in[0]

	r11_t5_mem0 = S.Task('r11_t5_mem0', length=1, delay_cost=1)
	S += r11_t5_mem0 >= 64
	r11_t5_mem0 += MM_MEM[0]

	r11_t5_mem1 = S.Task('r11_t5_mem1', length=1, delay_cost=1)
	S += r11_t5_mem1 >= 64
	r11_t5_mem1 += MM_MEM[1]

	r9_t4_in = S.Task('r9_t4_in', length=1, delay_cost=1)
	S += r9_t4_in >= 64
	r9_t4_in += MM_in[0]

	r9_t4_mem0 = S.Task('r9_t4_mem0', length=1, delay_cost=1)
	S += r9_t4_mem0 >= 64
	r9_t4_mem0 += MAS_MEM[0]

	r9_t4_mem1 = S.Task('r9_t4_mem1', length=1, delay_cost=1)
	S += r9_t4_mem1 >= 64
	r9_t4_mem1 += MAS_MEM[1]

	X_new0_w = S.Task('X_new0_w', length=1, delay_cost=1)
	S += X_new0_w >= 65
	X_new0_w += MAIN_MEM_w

	X_new_t5_in = S.Task('X_new_t5_in', length=1, delay_cost=1)
	S += X_new_t5_in >= 65
	X_new_t5_in += MAS_in[0]

	X_new_t5_mem0 = S.Task('X_new_t5_mem0', length=1, delay_cost=1)
	S += X_new_t5_mem0 >= 65
	X_new_t5_mem0 += MM_MEM[0]

	X_new_t5_mem1 = S.Task('X_new_t5_mem1', length=1, delay_cost=1)
	S += X_new_t5_mem1 >= 65
	X_new_t5_mem1 += MM_MEM[1]

	r11_t5 = S.Task('r11_t5', length=2, delay_cost=1)
	S += r11_t5 >= 65
	r11_t5 += MAS[0]

	r14_t1_in = S.Task('r14_t1_in', length=1, delay_cost=1)
	S += r14_t1_in >= 65
	r14_t1_in += MM_in[0]

	r14_t1_mem0 = S.Task('r14_t1_mem0', length=1, delay_cost=1)
	S += r14_t1_mem0 >= 65
	r14_t1_mem0 += MAS_MEM[0]

	r14_t1_mem1 = S.Task('r14_t1_mem1', length=1, delay_cost=1)
	S += r14_t1_mem1 >= 65
	r14_t1_mem1 += MAS_MEM[1]

	r9_t4 = S.Task('r9_t4', length=6, delay_cost=1)
	S += r9_t4 >= 65
	r9_t4 += MM[0]

	X_new_t5 = S.Task('X_new_t5', length=2, delay_cost=1)
	S += X_new_t5 >= 66
	X_new_t5 += MAS[0]

	r14_t1 = S.Task('r14_t1', length=6, delay_cost=1)
	S += r14_t1 >= 66
	r14_t1 += MM[0]

	r14_t2_in = S.Task('r14_t2_in', length=1, delay_cost=1)
	S += r14_t2_in >= 66
	r14_t2_in += MAS_in[0]

	r14_t2_mem0 = S.Task('r14_t2_mem0', length=1, delay_cost=1)
	S += r14_t2_mem0 >= 66
	r14_t2_mem0 += MAS_MEM[0]

	r14_t2_mem1 = S.Task('r14_t2_mem1', length=1, delay_cost=1)
	S += r14_t2_mem1 >= 66
	r14_t2_mem1 += MAS_MEM[1]

	Z_new_t2_in = S.Task('Z_new_t2_in', length=1, delay_cost=1)
	S += Z_new_t2_in >= 67
	Z_new_t2_in += MAS_in[0]

	Z_new_t2_mem0 = S.Task('Z_new_t2_mem0', length=1, delay_cost=1)
	S += Z_new_t2_mem0 >= 67
	Z_new_t2_mem0 += MAS_MEM[0]

	Z_new_t2_mem1 = S.Task('Z_new_t2_mem1', length=1, delay_cost=1)
	S += Z_new_t2_mem1 >= 67
	Z_new_t2_mem1 += MAS_MEM[1]

	r14_t2 = S.Task('r14_t2', length=2, delay_cost=1)
	S += r14_t2 >= 67
	r14_t2 += MAS[0]

	Z_new_t2 = S.Task('Z_new_t2', length=2, delay_cost=1)
	S += Z_new_t2 >= 68
	Z_new_t2 += MAS[0]

	r110_in = S.Task('r110_in', length=1, delay_cost=1)
	S += r110_in >= 68
	r110_in += MAS_in[0]

	r110_mem0 = S.Task('r110_mem0', length=1, delay_cost=1)
	S += r110_mem0 >= 68
	r110_mem0 += MM_MEM[0]

	r110_mem1 = S.Task('r110_mem1', length=1, delay_cost=1)
	S += r110_mem1 >= 68
	r110_mem1 += MAS_MEM[1]

	r16_t1_in = S.Task('r16_t1_in', length=1, delay_cost=1)
	S += r16_t1_in >= 68
	r16_t1_in += MM_in[0]

	r16_t1_mem0 = S.Task('r16_t1_mem0', length=1, delay_cost=1)
	S += r16_t1_mem0 >= 68
	r16_t1_mem0 += MAS_MEM[0]

	r16_t1_mem1 = S.Task('r16_t1_mem1', length=1, delay_cost=1)
	S += r16_t1_mem1 >= 68
	r16_t1_mem1 += MAIN_MEM_r[1]

	Z_new0_in = S.Task('Z_new0_in', length=1, delay_cost=1)
	S += Z_new0_in >= 69
	Z_new0_in += MAS_in[0]

	Z_new0_mem0 = S.Task('Z_new0_mem0', length=1, delay_cost=1)
	S += Z_new0_mem0 >= 69
	Z_new0_mem0 += MM_MEM[0]

	Z_new0_mem1 = S.Task('Z_new0_mem1', length=1, delay_cost=1)
	S += Z_new0_mem1 >= 69
	Z_new0_mem1 += MM_MEM[1]

	r110 = S.Task('r110', length=2, delay_cost=1)
	S += r110 >= 69
	r110 += MAS[0]

	r15_t0_in = S.Task('r15_t0_in', length=1, delay_cost=1)
	S += r15_t0_in >= 69
	r15_t0_in += MM_in[0]

	r15_t0_mem0 = S.Task('r15_t0_mem0', length=1, delay_cost=1)
	S += r15_t0_mem0 >= 69
	r15_t0_mem0 += MAS_MEM[0]

	r15_t0_mem1 = S.Task('r15_t0_mem1', length=1, delay_cost=1)
	S += r15_t0_mem1 >= 69
	r15_t0_mem1 += MAS_MEM[1]

	r16_t1 = S.Task('r16_t1', length=6, delay_cost=1)
	S += r16_t1 >= 69
	r16_t1 += MM[0]

	Z_new0 = S.Task('Z_new0', length=2, delay_cost=1)
	S += Z_new0 >= 70
	Z_new0 += MAS[0]

	r15_t0 = S.Task('r15_t0', length=6, delay_cost=1)
	S += r15_t0 >= 70
	r15_t0 += MM[0]

	r16_t0_in = S.Task('r16_t0_in', length=1, delay_cost=1)
	S += r16_t0_in >= 70
	r16_t0_in += MM_in[0]

	r16_t0_mem0 = S.Task('r16_t0_mem0', length=1, delay_cost=1)
	S += r16_t0_mem0 >= 70
	r16_t0_mem0 += MAS_MEM[0]

	r16_t0_mem1 = S.Task('r16_t0_mem1', length=1, delay_cost=1)
	S += r16_t0_mem1 >= 70
	r16_t0_mem1 += MAIN_MEM_r[1]

	r91_in = S.Task('r91_in', length=1, delay_cost=1)
	S += r91_in >= 70
	r91_in += MAS_in[0]

	r91_mem0 = S.Task('r91_mem0', length=1, delay_cost=1)
	S += r91_mem0 >= 70
	r91_mem0 += MM_MEM[0]

	r91_mem1 = S.Task('r91_mem1', length=1, delay_cost=1)
	S += r91_mem1 >= 70
	r91_mem1 += MAS_MEM[1]

	X_new_t4_in = S.Task('X_new_t4_in', length=1, delay_cost=1)
	S += X_new_t4_in >= 71
	X_new_t4_in += MM_in[0]

	X_new_t4_mem0 = S.Task('X_new_t4_mem0', length=1, delay_cost=1)
	S += X_new_t4_mem0 >= 71
	X_new_t4_mem0 += MAS_MEM[0]

	X_new_t4_mem1 = S.Task('X_new_t4_mem1', length=1, delay_cost=1)
	S += X_new_t4_mem1 >= 71
	X_new_t4_mem1 += MAS_MEM[1]

	r14_t5_in = S.Task('r14_t5_in', length=1, delay_cost=1)
	S += r14_t5_in >= 71
	r14_t5_in += MAS_in[0]

	r14_t5_mem0 = S.Task('r14_t5_mem0', length=1, delay_cost=1)
	S += r14_t5_mem0 >= 71
	r14_t5_mem0 += MM_MEM[0]

	r14_t5_mem1 = S.Task('r14_t5_mem1', length=1, delay_cost=1)
	S += r14_t5_mem1 >= 71
	r14_t5_mem1 += MM_MEM[1]

	r16_t0 = S.Task('r16_t0', length=6, delay_cost=1)
	S += r16_t0 >= 71
	r16_t0 += MM[0]

	r91 = S.Task('r91', length=2, delay_cost=1)
	S += r91 >= 71
	r91 += MAS[0]

	X_new_t4 = S.Task('X_new_t4', length=6, delay_cost=1)
	S += X_new_t4 >= 72
	X_new_t4 += MM[0]

	Z_new0_w = S.Task('Z_new0_w', length=1, delay_cost=1)
	S += Z_new0_w >= 72
	Z_new0_w += MAIN_MEM_w

	r140_in = S.Task('r140_in', length=1, delay_cost=1)
	S += r140_in >= 72
	r140_in += MAS_in[0]

	r140_mem0 = S.Task('r140_mem0', length=1, delay_cost=1)
	S += r140_mem0 >= 72
	r140_mem0 += MM_MEM[0]

	r140_mem1 = S.Task('r140_mem1', length=1, delay_cost=1)
	S += r140_mem1 >= 72
	r140_mem1 += MM_MEM[1]

	r14_t5 = S.Task('r14_t5', length=2, delay_cost=1)
	S += r14_t5 >= 72
	r14_t5 += MAS[0]

	Z_new_t4_in = S.Task('Z_new_t4_in', length=1, delay_cost=1)
	S += Z_new_t4_in >= 73
	Z_new_t4_in += MM_in[0]

	Z_new_t4_mem0 = S.Task('Z_new_t4_mem0', length=1, delay_cost=1)
	S += Z_new_t4_mem0 >= 73
	Z_new_t4_mem0 += MAS_MEM[0]

	Z_new_t4_mem1 = S.Task('Z_new_t4_mem1', length=1, delay_cost=1)
	S += Z_new_t4_mem1 >= 73
	Z_new_t4_mem1 += MAS_MEM[1]

	Z_new_t5_in = S.Task('Z_new_t5_in', length=1, delay_cost=1)
	S += Z_new_t5_in >= 73
	Z_new_t5_in += MAS_in[0]

	Z_new_t5_mem0 = S.Task('Z_new_t5_mem0', length=1, delay_cost=1)
	S += Z_new_t5_mem0 >= 73
	Z_new_t5_mem0 += MM_MEM[0]

	Z_new_t5_mem1 = S.Task('Z_new_t5_mem1', length=1, delay_cost=1)
	S += Z_new_t5_mem1 >= 73
	Z_new_t5_mem1 += MM_MEM[1]

	r140 = S.Task('r140', length=2, delay_cost=1)
	S += r140 >= 73
	r140 += MAS[0]

	Z_new_t4 = S.Task('Z_new_t4', length=6, delay_cost=1)
	S += Z_new_t4 >= 74
	Z_new_t4 += MM[0]

	Z_new_t5 = S.Task('Z_new_t5', length=2, delay_cost=1)
	S += Z_new_t5 >= 74
	Z_new_t5 += MAS[0]

	r15_t2_in = S.Task('r15_t2_in', length=1, delay_cost=1)
	S += r15_t2_in >= 74
	r15_t2_in += MAS_in[0]

	r15_t2_mem0 = S.Task('r15_t2_mem0', length=1, delay_cost=1)
	S += r15_t2_mem0 >= 74
	r15_t2_mem0 += MAS_MEM[0]

	r15_t2_mem1 = S.Task('r15_t2_mem1', length=1, delay_cost=1)
	S += r15_t2_mem1 >= 74
	r15_t2_mem1 += MAS_MEM[1]

	r15_t2 = S.Task('r15_t2', length=2, delay_cost=1)
	S += r15_t2 >= 75
	r15_t2 += MAS[0]

	r15_t3_in = S.Task('r15_t3_in', length=1, delay_cost=1)
	S += r15_t3_in >= 75
	r15_t3_in += MAS_in[0]

	r15_t3_mem0 = S.Task('r15_t3_mem0', length=1, delay_cost=1)
	S += r15_t3_mem0 >= 75
	r15_t3_mem0 += MAS_MEM[0]

	r15_t3_mem1 = S.Task('r15_t3_mem1', length=1, delay_cost=1)
	S += r15_t3_mem1 >= 75
	r15_t3_mem1 += MAS_MEM[1]

	r14_t4_in = S.Task('r14_t4_in', length=1, delay_cost=1)
	S += r14_t4_in >= 76
	r14_t4_in += MM_in[0]

	r14_t4_mem0 = S.Task('r14_t4_mem0', length=1, delay_cost=1)
	S += r14_t4_mem0 >= 76
	r14_t4_mem0 += MAS_MEM[0]

	r14_t4_mem1 = S.Task('r14_t4_mem1', length=1, delay_cost=1)
	S += r14_t4_mem1 >= 76
	r14_t4_mem1 += MAS_MEM[1]

	r15_t3 = S.Task('r15_t3', length=2, delay_cost=1)
	S += r15_t3 >= 76
	r15_t3 += MAS[0]

	r16_t5_in = S.Task('r16_t5_in', length=1, delay_cost=1)
	S += r16_t5_in >= 76
	r16_t5_in += MAS_in[0]

	r16_t5_mem0 = S.Task('r16_t5_mem0', length=1, delay_cost=1)
	S += r16_t5_mem0 >= 76
	r16_t5_mem0 += MM_MEM[0]

	r16_t5_mem1 = S.Task('r16_t5_mem1', length=1, delay_cost=1)
	S += r16_t5_mem1 >= 76
	r16_t5_mem1 += MM_MEM[1]

	r14_t4 = S.Task('r14_t4', length=6, delay_cost=1)
	S += r14_t4 >= 77
	r14_t4 += MM[0]

	r15_t4_in = S.Task('r15_t4_in', length=1, delay_cost=1)
	S += r15_t4_in >= 77
	r15_t4_in += MM_in[0]

	r15_t4_mem0 = S.Task('r15_t4_mem0', length=1, delay_cost=1)
	S += r15_t4_mem0 >= 77
	r15_t4_mem0 += MAS_MEM[0]

	r15_t4_mem1 = S.Task('r15_t4_mem1', length=1, delay_cost=1)
	S += r15_t4_mem1 >= 77
	r15_t4_mem1 += MAS_MEM[1]

	r160_in = S.Task('r160_in', length=1, delay_cost=1)
	S += r160_in >= 77
	r160_in += MAS_in[0]

	r160_mem0 = S.Task('r160_mem0', length=1, delay_cost=1)
	S += r160_mem0 >= 77
	r160_mem0 += MM_MEM[0]

	r160_mem1 = S.Task('r160_mem1', length=1, delay_cost=1)
	S += r160_mem1 >= 77
	r160_mem1 += MM_MEM[1]

	r16_t5 = S.Task('r16_t5', length=2, delay_cost=1)
	S += r16_t5 >= 77
	r16_t5 += MAS[0]

	r15_t4 = S.Task('r15_t4', length=6, delay_cost=1)
	S += r15_t4 >= 78
	r15_t4 += MM[0]

	r160 = S.Task('r160', length=2, delay_cost=1)
	S += r160 >= 78
	r160 += MAS[0]

	r16_t2_in = S.Task('r16_t2_in', length=1, delay_cost=1)
	S += r16_t2_in >= 78
	r16_t2_in += MAS_in[0]

	r16_t2_mem0 = S.Task('r16_t2_mem0', length=1, delay_cost=1)
	S += r16_t2_mem0 >= 78
	r16_t2_mem0 += MAS_MEM[0]

	r16_t2_mem1 = S.Task('r16_t2_mem1', length=1, delay_cost=1)
	S += r16_t2_mem1 >= 78
	r16_t2_mem1 += MAS_MEM[1]

	Z_new1_in = S.Task('Z_new1_in', length=1, delay_cost=1)
	S += Z_new1_in >= 79
	Z_new1_in += MAS_in[0]

	Z_new1_mem0 = S.Task('Z_new1_mem0', length=1, delay_cost=1)
	S += Z_new1_mem0 >= 79
	Z_new1_mem0 += MM_MEM[0]

	Z_new1_mem1 = S.Task('Z_new1_mem1', length=1, delay_cost=1)
	S += Z_new1_mem1 >= 79
	Z_new1_mem1 += MAS_MEM[1]

	r16_t2 = S.Task('r16_t2', length=2, delay_cost=1)
	S += r16_t2 >= 79
	r16_t2 += MAS[0]

	Z_new1 = S.Task('Z_new1', length=2, delay_cost=1)
	S += Z_new1 >= 80
	Z_new1 += MAS[0]

	r150_in = S.Task('r150_in', length=1, delay_cost=1)
	S += r150_in >= 80
	r150_in += MAS_in[0]

	r150_mem0 = S.Task('r150_mem0', length=1, delay_cost=1)
	S += r150_mem0 >= 80
	r150_mem0 += MM_MEM[0]

	r150_mem1 = S.Task('r150_mem1', length=1, delay_cost=1)
	S += r150_mem1 >= 80
	r150_mem1 += MM_MEM[1]

	r16_t4_in = S.Task('r16_t4_in', length=1, delay_cost=1)
	S += r16_t4_in >= 80
	r16_t4_in += MM_in[0]

	r16_t4_mem0 = S.Task('r16_t4_mem0', length=1, delay_cost=1)
	S += r16_t4_mem0 >= 80
	r16_t4_mem0 += MAS_MEM[0]

	r16_t4_mem1 = S.Task('r16_t4_mem1', length=1, delay_cost=1)
	S += r16_t4_mem1 >= 80
	r16_t4_mem1 += MAS_MEM[1]

	X_new1_in = S.Task('X_new1_in', length=1, delay_cost=1)
	S += X_new1_in >= 81
	X_new1_in += MAS_in[0]

	X_new1_mem0 = S.Task('X_new1_mem0', length=1, delay_cost=1)
	S += X_new1_mem0 >= 81
	X_new1_mem0 += MM_MEM[0]

	X_new1_mem1 = S.Task('X_new1_mem1', length=1, delay_cost=1)
	S += X_new1_mem1 >= 81
	X_new1_mem1 += MAS_MEM[1]

	r150 = S.Task('r150', length=2, delay_cost=1)
	S += r150 >= 81
	r150 += MAS[0]

	r16_t4 = S.Task('r16_t4', length=6, delay_cost=1)
	S += r16_t4 >= 81
	r16_t4 += MM[0]

	X_new1 = S.Task('X_new1', length=2, delay_cost=1)
	S += X_new1 >= 82
	X_new1 += MAS[0]

	Z_new1_w = S.Task('Z_new1_w', length=1, delay_cost=1)
	S += Z_new1_w >= 82
	Z_new1_w += MAIN_MEM_w

	r15_t5_in = S.Task('r15_t5_in', length=1, delay_cost=1)
	S += r15_t5_in >= 82
	r15_t5_in += MAS_in[0]

	r15_t5_mem0 = S.Task('r15_t5_mem0', length=1, delay_cost=1)
	S += r15_t5_mem0 >= 82
	r15_t5_mem0 += MM_MEM[0]

	r15_t5_mem1 = S.Task('r15_t5_mem1', length=1, delay_cost=1)
	S += r15_t5_mem1 >= 82
	r15_t5_mem1 += MM_MEM[1]

	r15_t5 = S.Task('r15_t5', length=2, delay_cost=1)
	S += r15_t5 >= 83
	r15_t5 += MAS[0]

	X_new1_w = S.Task('X_new1_w', length=1, delay_cost=1)
	S += X_new1_w >= 84
	X_new1_w += MAIN_MEM_w

	r141_in = S.Task('r141_in', length=1, delay_cost=1)
	S += r141_in >= 84
	r141_in += MAS_in[0]

	r141_mem0 = S.Task('r141_mem0', length=1, delay_cost=1)
	S += r141_mem0 >= 84
	r141_mem0 += MM_MEM[0]

	r141_mem1 = S.Task('r141_mem1', length=1, delay_cost=1)
	S += r141_mem1 >= 84
	r141_mem1 += MAS_MEM[1]

	r141 = S.Task('r141', length=2, delay_cost=1)
	S += r141 >= 85
	r141 += MAS[0]

	r151_in = S.Task('r151_in', length=1, delay_cost=1)
	S += r151_in >= 85
	r151_in += MAS_in[0]

	r151_mem0 = S.Task('r151_mem0', length=1, delay_cost=1)
	S += r151_mem0 >= 85
	r151_mem0 += MM_MEM[0]

	r151_mem1 = S.Task('r151_mem1', length=1, delay_cost=1)
	S += r151_mem1 >= 85
	r151_mem1 += MAS_MEM[1]

	r151 = S.Task('r151', length=2, delay_cost=1)
	S += r151 >= 86
	r151 += MAS[0]

	r161_in = S.Task('r161_in', length=1, delay_cost=1)
	S += r161_in >= 86
	r161_in += MAS_in[0]

	r161_mem0 = S.Task('r161_mem0', length=1, delay_cost=1)
	S += r161_mem0 >= 86
	r161_mem0 += MM_MEM[0]

	r161_mem1 = S.Task('r161_mem1', length=1, delay_cost=1)
	S += r161_mem1 >= 86
	r161_mem1 += MAS_MEM[1]

	r161 = S.Task('r161', length=2, delay_cost=1)
	S += r161 >= 87
	r161 += MAS[0]

	r171_in = S.Task('r171_in', length=1, delay_cost=1)
	S += r171_in >= 87
	r171_in += MAS_in[0]

	r171_mem0 = S.Task('r171_mem0', length=1, delay_cost=1)
	S += r171_mem0 >= 87
	r171_mem0 += MAS_MEM[0]

	r171_mem1 = S.Task('r171_mem1', length=1, delay_cost=1)
	S += r171_mem1 >= 87
	r171_mem1 += MAS_MEM[1]

	Y_new0_in = S.Task('Y_new0_in', length=1, delay_cost=1)
	S += Y_new0_in >= 88
	Y_new0_in += MAS_in[0]

	Y_new0_mem0 = S.Task('Y_new0_mem0', length=1, delay_cost=1)
	S += Y_new0_mem0 >= 88
	Y_new0_mem0 += MAS_MEM[0]

	Y_new0_mem1 = S.Task('Y_new0_mem1', length=1, delay_cost=1)
	S += Y_new0_mem1 >= 88
	Y_new0_mem1 += MAS_MEM[1]

	r171 = S.Task('r171', length=2, delay_cost=1)
	S += r171 >= 88
	r171 += MAS[0]

	Y_new0 = S.Task('Y_new0', length=2, delay_cost=1)
	S += Y_new0 >= 89
	Y_new0 += MAS[0]

	Y_new1_in = S.Task('Y_new1_in', length=1, delay_cost=1)
	S += Y_new1_in >= 89
	Y_new1_in += MAS_in[0]

	Y_new1_mem0 = S.Task('Y_new1_mem0', length=1, delay_cost=1)
	S += Y_new1_mem0 >= 89
	Y_new1_mem0 += MAS_MEM[0]

	Y_new1_mem1 = S.Task('Y_new1_mem1', length=1, delay_cost=1)
	S += Y_new1_mem1 >= 89
	Y_new1_mem1 += MAS_MEM[1]

	Y_new1 = S.Task('Y_new1', length=2, delay_cost=1)
	S += Y_new1 >= 90
	Y_new1 += MAS[0]

	Y_new0_w = S.Task('Y_new0_w', length=1, delay_cost=1)
	S += Y_new0_w >= 91
	Y_new0_w += MAIN_MEM_w

	Y_new1_w = S.Task('Y_new1_w', length=1, delay_cost=1)
	S += Y_new1_w >= 92
	Y_new1_w += MAIN_MEM_w


	# new tasks
	r15_t1 = S.Task('r15_t1', length=6, delay_cost=1)
	r15_t1 += alt(MM)
	r15_t1_in = S.Task('r15_t1_in', length=1, delay_cost=1)
	r15_t1_in += alt(MM_in)
	S += r15_t1_in*MM_in[0]<=r15_t1*MM[0]
	S += r15_t1<81

	r15_t1_mem0 = S.Task('r15_t1_mem0', length=1, delay_cost=1)
	r15_t1_mem0 += MAS_MEM[0]
	S += 47 < r15_t1_mem0
	S += r15_t1_mem0 <= r15_t1

	r15_t1_mem1 = S.Task('r15_t1_mem1', length=1, delay_cost=1)
	r15_t1_mem1 += MAS_MEM[1]
	S += 72 < r15_t1_mem1
	S += r15_t1_mem1 <= r15_t1

	r170 = S.Task('r170', length=2, delay_cost=1)
	r170 += alt(MAS)
	r170_in = S.Task('r170_in', length=1, delay_cost=1)
	r170_in += alt(MAS_in)
	S += r170_in*MAS_in[0]<=r170*MAS[0]

	S += r170<89

	r170_mem0 = S.Task('r170_mem0', length=1, delay_cost=1)
	r170_mem0 += MAS_MEM[0]
	S += 74 < r170_mem0
	S += r170_mem0 <= r170

	r170_mem1 = S.Task('r170_mem1', length=1, delay_cost=1)
	r170_mem1 += MAS_MEM[1]
	S += 82 < r170_mem1
	S += r170_mem1 <= r170

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage2MAS1/EP2_YRECOVER/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution

