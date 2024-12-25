from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 215
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	r1_t1_in = S.Task('r1_t1_in', length=1, delay_cost=1)
	S += r1_t1_in >= 0
	r1_t1_in += MM_in[0]

	r1_t1_mem0 = S.Task('r1_t1_mem0', length=1, delay_cost=1)
	S += r1_t1_mem0 >= 0
	r1_t1_mem0 += MAIN_MEM_r[0]

	r1_t1_mem1 = S.Task('r1_t1_mem1', length=1, delay_cost=1)
	S += r1_t1_mem1 >= 0
	r1_t1_mem1 += MAIN_MEM_r[1]

	r1_t1 = S.Task('r1_t1', length=10, delay_cost=1)
	S += r1_t1 >= 1
	r1_t1 += MM[0]

	r3_t1_in = S.Task('r3_t1_in', length=1, delay_cost=1)
	S += r3_t1_in >= 1
	r3_t1_in += MM_in[0]

	r3_t1_mem0 = S.Task('r3_t1_mem0', length=1, delay_cost=1)
	S += r3_t1_mem0 >= 1
	r3_t1_mem0 += MAIN_MEM_r[0]

	r3_t1_mem1 = S.Task('r3_t1_mem1', length=1, delay_cost=1)
	S += r3_t1_mem1 >= 1
	r3_t1_mem1 += MAIN_MEM_r[1]

	r3_t1 = S.Task('r3_t1', length=10, delay_cost=1)
	S += r3_t1 >= 2
	r3_t1 += MM[0]

	r3_t2_in = S.Task('r3_t2_in', length=1, delay_cost=1)
	S += r3_t2_in >= 2
	r3_t2_in += MAS_in[5]

	r3_t2_mem0 = S.Task('r3_t2_mem0', length=1, delay_cost=1)
	S += r3_t2_mem0 >= 2
	r3_t2_mem0 += MAIN_MEM_r[0]

	r3_t2_mem1 = S.Task('r3_t2_mem1', length=1, delay_cost=1)
	S += r3_t2_mem1 >= 2
	r3_t2_mem1 += MAIN_MEM_r[1]

	r3_t2 = S.Task('r3_t2', length=4, delay_cost=1)
	S += r3_t2 >= 3
	r3_t2 += MAS[5]

	r4_t0_in = S.Task('r4_t0_in', length=1, delay_cost=1)
	S += r4_t0_in >= 3
	r4_t0_in += MM_in[0]

	r4_t0_mem0 = S.Task('r4_t0_mem0', length=1, delay_cost=1)
	S += r4_t0_mem0 >= 3
	r4_t0_mem0 += MAIN_MEM_r[0]

	r4_t0_mem1 = S.Task('r4_t0_mem1', length=1, delay_cost=1)
	S += r4_t0_mem1 >= 3
	r4_t0_mem1 += MAIN_MEM_r[1]

	r4_t0 = S.Task('r4_t0', length=10, delay_cost=1)
	S += r4_t0 >= 4
	r4_t0 += MM[0]

	r4_t1_in = S.Task('r4_t1_in', length=1, delay_cost=1)
	S += r4_t1_in >= 4
	r4_t1_in += MM_in[0]

	r4_t1_mem0 = S.Task('r4_t1_mem0', length=1, delay_cost=1)
	S += r4_t1_mem0 >= 4
	r4_t1_mem0 += MAIN_MEM_r[0]

	r4_t1_mem1 = S.Task('r4_t1_mem1', length=1, delay_cost=1)
	S += r4_t1_mem1 >= 4
	r4_t1_mem1 += MAIN_MEM_r[1]

	r4_t1 = S.Task('r4_t1', length=10, delay_cost=1)
	S += r4_t1 >= 5
	r4_t1 += MM[0]

	r5_t1_in = S.Task('r5_t1_in', length=1, delay_cost=1)
	S += r5_t1_in >= 5
	r5_t1_in += MM_in[0]

	r5_t1_mem0 = S.Task('r5_t1_mem0', length=1, delay_cost=1)
	S += r5_t1_mem0 >= 5
	r5_t1_mem0 += MAIN_MEM_r[0]

	r5_t1_mem1 = S.Task('r5_t1_mem1', length=1, delay_cost=1)
	S += r5_t1_mem1 >= 5
	r5_t1_mem1 += MAIN_MEM_r[1]

	r5_t1 = S.Task('r5_t1', length=10, delay_cost=1)
	S += r5_t1 >= 6
	r5_t1 += MM[0]

	r5_t2_in = S.Task('r5_t2_in', length=1, delay_cost=1)
	S += r5_t2_in >= 6
	r5_t2_in += MAS_in[0]

	r5_t2_mem0 = S.Task('r5_t2_mem0', length=1, delay_cost=1)
	S += r5_t2_mem0 >= 6
	r5_t2_mem0 += MAIN_MEM_r[0]

	r5_t2_mem1 = S.Task('r5_t2_mem1', length=1, delay_cost=1)
	S += r5_t2_mem1 >= 6
	r5_t2_mem1 += MAIN_MEM_r[1]

	r1_t0_in = S.Task('r1_t0_in', length=1, delay_cost=1)
	S += r1_t0_in >= 7
	r1_t0_in += MM_in[0]

	r1_t0_mem0 = S.Task('r1_t0_mem0', length=1, delay_cost=1)
	S += r1_t0_mem0 >= 7
	r1_t0_mem0 += MAIN_MEM_r[0]

	r1_t0_mem1 = S.Task('r1_t0_mem1', length=1, delay_cost=1)
	S += r1_t0_mem1 >= 7
	r1_t0_mem1 += MAIN_MEM_r[1]

	r5_t2 = S.Task('r5_t2', length=4, delay_cost=1)
	S += r5_t2 >= 7
	r5_t2 += MAS[0]

	r1_t0 = S.Task('r1_t0', length=10, delay_cost=1)
	S += r1_t0 >= 8
	r1_t0 += MM[0]

	r1_t3_in = S.Task('r1_t3_in', length=1, delay_cost=1)
	S += r1_t3_in >= 8
	r1_t3_in += MAS_in[0]

	r1_t3_mem0 = S.Task('r1_t3_mem0', length=1, delay_cost=1)
	S += r1_t3_mem0 >= 8
	r1_t3_mem0 += MAIN_MEM_r[0]

	r1_t3_mem1 = S.Task('r1_t3_mem1', length=1, delay_cost=1)
	S += r1_t3_mem1 >= 8
	r1_t3_mem1 += MAIN_MEM_r[1]

	r1_t3 = S.Task('r1_t3', length=4, delay_cost=1)
	S += r1_t3 >= 9
	r1_t3 += MAS[0]

	r6_t0_in = S.Task('r6_t0_in', length=1, delay_cost=1)
	S += r6_t0_in >= 9
	r6_t0_in += MM_in[0]

	r6_t0_mem0 = S.Task('r6_t0_mem0', length=1, delay_cost=1)
	S += r6_t0_mem0 >= 9
	r6_t0_mem0 += MAIN_MEM_r[0]

	r6_t0_mem1 = S.Task('r6_t0_mem1', length=1, delay_cost=1)
	S += r6_t0_mem1 >= 9
	r6_t0_mem1 += MAIN_MEM_r[1]

	r6_t0 = S.Task('r6_t0', length=10, delay_cost=1)
	S += r6_t0 >= 10
	r6_t0 += MM[0]

	r6_t1_in = S.Task('r6_t1_in', length=1, delay_cost=1)
	S += r6_t1_in >= 10
	r6_t1_in += MM_in[0]

	r6_t1_mem0 = S.Task('r6_t1_mem0', length=1, delay_cost=1)
	S += r6_t1_mem0 >= 10
	r6_t1_mem0 += MAIN_MEM_r[0]

	r6_t1_mem1 = S.Task('r6_t1_mem1', length=1, delay_cost=1)
	S += r6_t1_mem1 >= 10
	r6_t1_mem1 += MAIN_MEM_r[1]

	r4_t2_in = S.Task('r4_t2_in', length=1, delay_cost=1)
	S += r4_t2_in >= 11
	r4_t2_in += MAS_in[0]

	r4_t2_mem0 = S.Task('r4_t2_mem0', length=1, delay_cost=1)
	S += r4_t2_mem0 >= 11
	r4_t2_mem0 += MAIN_MEM_r[0]

	r4_t2_mem1 = S.Task('r4_t2_mem1', length=1, delay_cost=1)
	S += r4_t2_mem1 >= 11
	r4_t2_mem1 += MAIN_MEM_r[1]

	r6_t1 = S.Task('r6_t1', length=10, delay_cost=1)
	S += r6_t1 >= 11
	r6_t1 += MM[0]

	r4_t2 = S.Task('r4_t2', length=4, delay_cost=1)
	S += r4_t2 >= 12
	r4_t2 += MAS[0]

	r5_t3_in = S.Task('r5_t3_in', length=1, delay_cost=1)
	S += r5_t3_in >= 12
	r5_t3_in += MAS_in[0]

	r5_t3_mem0 = S.Task('r5_t3_mem0', length=1, delay_cost=1)
	S += r5_t3_mem0 >= 12
	r5_t3_mem0 += MAIN_MEM_r[0]

	r5_t3_mem1 = S.Task('r5_t3_mem1', length=1, delay_cost=1)
	S += r5_t3_mem1 >= 12
	r5_t3_mem1 += MAIN_MEM_r[1]

	r5_t3 = S.Task('r5_t3', length=4, delay_cost=1)
	S += r5_t3 >= 13
	r5_t3 += MAS[0]

	r6_t2_in = S.Task('r6_t2_in', length=1, delay_cost=1)
	S += r6_t2_in >= 13
	r6_t2_in += MAS_in[0]

	r6_t2_mem0 = S.Task('r6_t2_mem0', length=1, delay_cost=1)
	S += r6_t2_mem0 >= 13
	r6_t2_mem0 += MAIN_MEM_r[0]

	r6_t2_mem1 = S.Task('r6_t2_mem1', length=1, delay_cost=1)
	S += r6_t2_mem1 >= 13
	r6_t2_mem1 += MAIN_MEM_r[1]

	r12_t0_in = S.Task('r12_t0_in', length=1, delay_cost=1)
	S += r12_t0_in >= 14
	r12_t0_in += MM_in[0]

	r12_t0_mem0 = S.Task('r12_t0_mem0', length=1, delay_cost=1)
	S += r12_t0_mem0 >= 14
	r12_t0_mem0 += MAIN_MEM_r[0]

	r12_t0_mem1 = S.Task('r12_t0_mem1', length=1, delay_cost=1)
	S += r12_t0_mem1 >= 14
	r12_t0_mem1 += MAIN_MEM_r[1]

	r4_t5_in = S.Task('r4_t5_in', length=1, delay_cost=1)
	S += r4_t5_in >= 14
	r4_t5_in += MAS_in[0]

	r4_t5_mem0 = S.Task('r4_t5_mem0', length=1, delay_cost=1)
	S += r4_t5_mem0 >= 14
	r4_t5_mem0 += MM_MEM[0]

	r4_t5_mem1 = S.Task('r4_t5_mem1', length=1, delay_cost=1)
	S += r4_t5_mem1 >= 14
	r4_t5_mem1 += MM_MEM[1]

	r6_t2 = S.Task('r6_t2', length=4, delay_cost=1)
	S += r6_t2 >= 14
	r6_t2 += MAS[0]

	r12_t0 = S.Task('r12_t0', length=10, delay_cost=1)
	S += r12_t0 >= 15
	r12_t0 += MM[0]

	r40_in = S.Task('r40_in', length=1, delay_cost=1)
	S += r40_in >= 15
	r40_in += MAS_in[2]

	r40_mem0 = S.Task('r40_mem0', length=1, delay_cost=1)
	S += r40_mem0 >= 15
	r40_mem0 += MM_MEM[0]

	r40_mem1 = S.Task('r40_mem1', length=1, delay_cost=1)
	S += r40_mem1 >= 15
	r40_mem1 += MM_MEM[1]

	r4_t3_in = S.Task('r4_t3_in', length=1, delay_cost=1)
	S += r4_t3_in >= 15
	r4_t3_in += MAS_in[0]

	r4_t3_mem0 = S.Task('r4_t3_mem0', length=1, delay_cost=1)
	S += r4_t3_mem0 >= 15
	r4_t3_mem0 += MAIN_MEM_r[0]

	r4_t3_mem1 = S.Task('r4_t3_mem1', length=1, delay_cost=1)
	S += r4_t3_mem1 >= 15
	r4_t3_mem1 += MAIN_MEM_r[1]

	r4_t5 = S.Task('r4_t5', length=4, delay_cost=1)
	S += r4_t5 >= 15
	r4_t5 += MAS[0]

	r12_t2_in = S.Task('r12_t2_in', length=1, delay_cost=1)
	S += r12_t2_in >= 16
	r12_t2_in += MAS_in[0]

	r12_t2_mem0 = S.Task('r12_t2_mem0', length=1, delay_cost=1)
	S += r12_t2_mem0 >= 16
	r12_t2_mem0 += MAIN_MEM_r[0]

	r12_t2_mem1 = S.Task('r12_t2_mem1', length=1, delay_cost=1)
	S += r12_t2_mem1 >= 16
	r12_t2_mem1 += MAIN_MEM_r[1]

	r40 = S.Task('r40', length=4, delay_cost=1)
	S += r40 >= 16
	r40 += MAS[2]

	r4_t3 = S.Task('r4_t3', length=4, delay_cost=1)
	S += r4_t3 >= 16
	r4_t3 += MAS[0]

	r5_t4_in = S.Task('r5_t4_in', length=1, delay_cost=1)
	S += r5_t4_in >= 16
	r5_t4_in += MM_in[1]

	r5_t4_mem0 = S.Task('r5_t4_mem0', length=1, delay_cost=1)
	S += r5_t4_mem0 >= 16
	r5_t4_mem0 += MAS_MEM[0]

	r5_t4_mem1 = S.Task('r5_t4_mem1', length=1, delay_cost=1)
	S += r5_t4_mem1 >= 16
	r5_t4_mem1 += MAS_MEM[1]

	r10_in = S.Task('r10_in', length=1, delay_cost=1)
	S += r10_in >= 17
	r10_in += MAS_in[5]

	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	S += r10_mem0 >= 17
	r10_mem0 += MM_MEM[0]

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	S += r10_mem1 >= 17
	r10_mem1 += MM_MEM[1]

	r12_t2 = S.Task('r12_t2', length=4, delay_cost=1)
	S += r12_t2 >= 17
	r12_t2 += MAS[0]

	r13_t0_in = S.Task('r13_t0_in', length=1, delay_cost=1)
	S += r13_t0_in >= 17
	r13_t0_in += MM_in[0]

	r13_t0_mem0 = S.Task('r13_t0_mem0', length=1, delay_cost=1)
	S += r13_t0_mem0 >= 17
	r13_t0_mem0 += MAIN_MEM_r[0]

	r13_t0_mem1 = S.Task('r13_t0_mem1', length=1, delay_cost=1)
	S += r13_t0_mem1 >= 17
	r13_t0_mem1 += MAIN_MEM_r[1]

	r5_t4 = S.Task('r5_t4', length=10, delay_cost=1)
	S += r5_t4 >= 17
	r5_t4 += MM[1]

	r10 = S.Task('r10', length=4, delay_cost=1)
	S += r10 >= 18
	r10 += MAS[5]

	r12_t1_in = S.Task('r12_t1_in', length=1, delay_cost=1)
	S += r12_t1_in >= 18
	r12_t1_in += MM_in[0]

	r12_t1_mem0 = S.Task('r12_t1_mem0', length=1, delay_cost=1)
	S += r12_t1_mem0 >= 18
	r12_t1_mem0 += MAIN_MEM_r[0]

	r12_t1_mem1 = S.Task('r12_t1_mem1', length=1, delay_cost=1)
	S += r12_t1_mem1 >= 18
	r12_t1_mem1 += MAIN_MEM_r[1]

	r13_t0 = S.Task('r13_t0', length=10, delay_cost=1)
	S += r13_t0 >= 18
	r13_t0 += MM[0]

	r1_t5_in = S.Task('r1_t5_in', length=1, delay_cost=1)
	S += r1_t5_in >= 18
	r1_t5_in += MAS_in[2]

	r1_t5_mem0 = S.Task('r1_t5_mem0', length=1, delay_cost=1)
	S += r1_t5_mem0 >= 18
	r1_t5_mem0 += MM_MEM[0]

	r1_t5_mem1 = S.Task('r1_t5_mem1', length=1, delay_cost=1)
	S += r1_t5_mem1 >= 18
	r1_t5_mem1 += MM_MEM[1]

	r12_t1 = S.Task('r12_t1', length=10, delay_cost=1)
	S += r12_t1 >= 19
	r12_t1 += MM[0]

	r1_t2_in = S.Task('r1_t2_in', length=1, delay_cost=1)
	S += r1_t2_in >= 19
	r1_t2_in += MAS_in[0]

	r1_t2_mem0 = S.Task('r1_t2_mem0', length=1, delay_cost=1)
	S += r1_t2_mem0 >= 19
	r1_t2_mem0 += MAIN_MEM_r[0]

	r1_t2_mem1 = S.Task('r1_t2_mem1', length=1, delay_cost=1)
	S += r1_t2_mem1 >= 19
	r1_t2_mem1 += MAIN_MEM_r[1]

	r1_t5 = S.Task('r1_t5', length=4, delay_cost=1)
	S += r1_t5 >= 19
	r1_t5 += MAS[2]

	r4_t4_in = S.Task('r4_t4_in', length=1, delay_cost=1)
	S += r4_t4_in >= 19
	r4_t4_in += MM_in[1]

	r4_t4_mem0 = S.Task('r4_t4_mem0', length=1, delay_cost=1)
	S += r4_t4_mem0 >= 19
	r4_t4_mem0 += MAS_MEM[0]

	r4_t4_mem1 = S.Task('r4_t4_mem1', length=1, delay_cost=1)
	S += r4_t4_mem1 >= 19
	r4_t4_mem1 += MAS_MEM[1]

	r13_t2_in = S.Task('r13_t2_in', length=1, delay_cost=1)
	S += r13_t2_in >= 20
	r13_t2_in += MAS_in[0]

	r13_t2_mem0 = S.Task('r13_t2_mem0', length=1, delay_cost=1)
	S += r13_t2_mem0 >= 20
	r13_t2_mem0 += MAIN_MEM_r[0]

	r13_t2_mem1 = S.Task('r13_t2_mem1', length=1, delay_cost=1)
	S += r13_t2_mem1 >= 20
	r13_t2_mem1 += MAIN_MEM_r[1]

	r1_t2 = S.Task('r1_t2', length=4, delay_cost=1)
	S += r1_t2 >= 20
	r1_t2 += MAS[0]

	r4_t4 = S.Task('r4_t4', length=10, delay_cost=1)
	S += r4_t4 >= 20
	r4_t4 += MM[1]

	r60_in = S.Task('r60_in', length=1, delay_cost=1)
	S += r60_in >= 20
	r60_in += MAS_in[4]

	r60_mem0 = S.Task('r60_mem0', length=1, delay_cost=1)
	S += r60_mem0 >= 20
	r60_mem0 += MM_MEM[0]

	r60_mem1 = S.Task('r60_mem1', length=1, delay_cost=1)
	S += r60_mem1 >= 20
	r60_mem1 += MM_MEM[1]

	r13_t2 = S.Task('r13_t2', length=4, delay_cost=1)
	S += r13_t2 >= 21
	r13_t2 += MAS[0]

	r20_in = S.Task('r20_in', length=1, delay_cost=1)
	S += r20_in >= 21
	r20_in += MAS_in[4]

	r20_mem0 = S.Task('r20_mem0', length=1, delay_cost=1)
	S += r20_mem0 >= 21
	r20_mem0 += MAS_MEM[10]

	r20_mem1 = S.Task('r20_mem1', length=1, delay_cost=1)
	S += r20_mem1 >= 21
	r20_mem1 += MAS_MEM[11]

	r3_t0_in = S.Task('r3_t0_in', length=1, delay_cost=1)
	S += r3_t0_in >= 21
	r3_t0_in += MM_in[0]

	r3_t0_mem0 = S.Task('r3_t0_mem0', length=1, delay_cost=1)
	S += r3_t0_mem0 >= 21
	r3_t0_mem0 += MAIN_MEM_r[0]

	r3_t0_mem1 = S.Task('r3_t0_mem1', length=1, delay_cost=1)
	S += r3_t0_mem1 >= 21
	r3_t0_mem1 += MAIN_MEM_r[1]

	r60 = S.Task('r60', length=4, delay_cost=1)
	S += r60 >= 21
	r60 += MAS[4]

	r6_t5_in = S.Task('r6_t5_in', length=1, delay_cost=1)
	S += r6_t5_in >= 21
	r6_t5_in += MAS_in[0]

	r6_t5_mem0 = S.Task('r6_t5_mem0', length=1, delay_cost=1)
	S += r6_t5_mem0 >= 21
	r6_t5_mem0 += MM_MEM[0]

	r6_t5_mem1 = S.Task('r6_t5_mem1', length=1, delay_cost=1)
	S += r6_t5_mem1 >= 21
	r6_t5_mem1 += MM_MEM[1]

	r16_t3_in = S.Task('r16_t3_in', length=1, delay_cost=1)
	S += r16_t3_in >= 22
	r16_t3_in += MAS_in[0]

	r16_t3_mem0 = S.Task('r16_t3_mem0', length=1, delay_cost=1)
	S += r16_t3_mem0 >= 22
	r16_t3_mem0 += MAIN_MEM_r[0]

	r16_t3_mem1 = S.Task('r16_t3_mem1', length=1, delay_cost=1)
	S += r16_t3_mem1 >= 22
	r16_t3_mem1 += MAIN_MEM_r[1]

	r20 = S.Task('r20', length=4, delay_cost=1)
	S += r20 >= 22
	r20 += MAS[4]

	r3_t0 = S.Task('r3_t0', length=10, delay_cost=1)
	S += r3_t0 >= 22
	r3_t0 += MM[0]

	r6_t5 = S.Task('r6_t5', length=4, delay_cost=1)
	S += r6_t5 >= 22
	r6_t5 += MAS[0]

	r16_t3 = S.Task('r16_t3', length=4, delay_cost=1)
	S += r16_t3 >= 23
	r16_t3 += MAS[0]

	r1_t4_in = S.Task('r1_t4_in', length=1, delay_cost=1)
	S += r1_t4_in >= 23
	r1_t4_in += MM_in[0]

	r1_t4_mem0 = S.Task('r1_t4_mem0', length=1, delay_cost=1)
	S += r1_t4_mem0 >= 23
	r1_t4_mem0 += MAS_MEM[0]

	r1_t4_mem1 = S.Task('r1_t4_mem1', length=1, delay_cost=1)
	S += r1_t4_mem1 >= 23
	r1_t4_mem1 += MAS_MEM[1]

	r6_t3_in = S.Task('r6_t3_in', length=1, delay_cost=1)
	S += r6_t3_in >= 23
	r6_t3_in += MAS_in[0]

	r6_t3_mem0 = S.Task('r6_t3_mem0', length=1, delay_cost=1)
	S += r6_t3_mem0 >= 23
	r6_t3_mem0 += MAIN_MEM_r[0]

	r6_t3_mem1 = S.Task('r6_t3_mem1', length=1, delay_cost=1)
	S += r6_t3_mem1 >= 23
	r6_t3_mem1 += MAIN_MEM_r[1]

	r13_t1_in = S.Task('r13_t1_in', length=1, delay_cost=1)
	S += r13_t1_in >= 24
	r13_t1_in += MM_in[0]

	r13_t1_mem0 = S.Task('r13_t1_mem0', length=1, delay_cost=1)
	S += r13_t1_mem0 >= 24
	r13_t1_mem0 += MAIN_MEM_r[0]

	r13_t1_mem1 = S.Task('r13_t1_mem1', length=1, delay_cost=1)
	S += r13_t1_mem1 >= 24
	r13_t1_mem1 += MAIN_MEM_r[1]

	r1_t4 = S.Task('r1_t4', length=10, delay_cost=1)
	S += r1_t4 >= 24
	r1_t4 += MM[0]

	r6_t3 = S.Task('r6_t3', length=4, delay_cost=1)
	S += r6_t3 >= 24
	r6_t3 += MAS[0]

	r13_t1 = S.Task('r13_t1', length=10, delay_cost=1)
	S += r13_t1 >= 25
	r13_t1 += MM[0]

	r5_t0_in = S.Task('r5_t0_in', length=1, delay_cost=1)
	S += r5_t0_in >= 25
	r5_t0_in += MM_in[1]

	r5_t0_mem0 = S.Task('r5_t0_mem0', length=1, delay_cost=1)
	S += r5_t0_mem0 >= 25
	r5_t0_mem0 += MAIN_MEM_r[0]

	r5_t0_mem1 = S.Task('r5_t0_mem1', length=1, delay_cost=1)
	S += r5_t0_mem1 >= 25
	r5_t0_mem1 += MAIN_MEM_r[1]

	r13_t3_in = S.Task('r13_t3_in', length=1, delay_cost=1)
	S += r13_t3_in >= 26
	r13_t3_in += MAS_in[4]

	r13_t3_mem0 = S.Task('r13_t3_mem0', length=1, delay_cost=1)
	S += r13_t3_mem0 >= 26
	r13_t3_mem0 += MAIN_MEM_r[0]

	r13_t3_mem1 = S.Task('r13_t3_mem1', length=1, delay_cost=1)
	S += r13_t3_mem1 >= 26
	r13_t3_mem1 += MAIN_MEM_r[1]

	r5_t0 = S.Task('r5_t0', length=10, delay_cost=1)
	S += r5_t0 >= 26
	r5_t0 += MM[1]

	r13_t3 = S.Task('r13_t3', length=4, delay_cost=1)
	S += r13_t3 >= 27
	r13_t3 += MAS[4]

	r6_t4_in = S.Task('r6_t4_in', length=1, delay_cost=1)
	S += r6_t4_in >= 27
	r6_t4_in += MM_in[0]

	r6_t4_mem0 = S.Task('r6_t4_mem0', length=1, delay_cost=1)
	S += r6_t4_mem0 >= 27
	r6_t4_mem0 += MAS_MEM[0]

	r6_t4_mem1 = S.Task('r6_t4_mem1', length=1, delay_cost=1)
	S += r6_t4_mem1 >= 27
	r6_t4_mem1 += MAS_MEM[1]

	r9_t2_in = S.Task('r9_t2_in', length=1, delay_cost=1)
	S += r9_t2_in >= 27
	r9_t2_in += MAS_in[4]

	r9_t2_mem0 = S.Task('r9_t2_mem0', length=1, delay_cost=1)
	S += r9_t2_mem0 >= 27
	r9_t2_mem0 += MAIN_MEM_r[0]

	r9_t2_mem1 = S.Task('r9_t2_mem1', length=1, delay_cost=1)
	S += r9_t2_mem1 >= 27
	r9_t2_mem1 += MAIN_MEM_r[1]

	r120_in = S.Task('r120_in', length=1, delay_cost=1)
	S += r120_in >= 28
	r120_in += MAS_in[0]

	r120_mem0 = S.Task('r120_mem0', length=1, delay_cost=1)
	S += r120_mem0 >= 28
	r120_mem0 += MM_MEM[0]

	r120_mem1 = S.Task('r120_mem1', length=1, delay_cost=1)
	S += r120_mem1 >= 28
	r120_mem1 += MM_MEM[1]

	r3_t3_in = S.Task('r3_t3_in', length=1, delay_cost=1)
	S += r3_t3_in >= 28
	r3_t3_in += MAS_in[4]

	r3_t3_mem0 = S.Task('r3_t3_mem0', length=1, delay_cost=1)
	S += r3_t3_mem0 >= 28
	r3_t3_mem0 += MAIN_MEM_r[0]

	r3_t3_mem1 = S.Task('r3_t3_mem1', length=1, delay_cost=1)
	S += r3_t3_mem1 >= 28
	r3_t3_mem1 += MAIN_MEM_r[1]

	r6_t4 = S.Task('r6_t4', length=10, delay_cost=1)
	S += r6_t4 >= 28
	r6_t4 += MM[0]

	r9_t2 = S.Task('r9_t2', length=4, delay_cost=1)
	S += r9_t2 >= 28
	r9_t2 += MAS[4]

	r120 = S.Task('r120', length=4, delay_cost=1)
	S += r120 >= 29
	r120 += MAS[0]

	r12_t3_in = S.Task('r12_t3_in', length=1, delay_cost=1)
	S += r12_t3_in >= 29
	r12_t3_in += MAS_in[5]

	r12_t3_mem0 = S.Task('r12_t3_mem0', length=1, delay_cost=1)
	S += r12_t3_mem0 >= 29
	r12_t3_mem0 += MAIN_MEM_r[0]

	r12_t3_mem1 = S.Task('r12_t3_mem1', length=1, delay_cost=1)
	S += r12_t3_mem1 >= 29
	r12_t3_mem1 += MAIN_MEM_r[1]

	r12_t5_in = S.Task('r12_t5_in', length=1, delay_cost=1)
	S += r12_t5_in >= 29
	r12_t5_in += MAS_in[4]

	r12_t5_mem0 = S.Task('r12_t5_mem0', length=1, delay_cost=1)
	S += r12_t5_mem0 >= 29
	r12_t5_mem0 += MM_MEM[0]

	r12_t5_mem1 = S.Task('r12_t5_mem1', length=1, delay_cost=1)
	S += r12_t5_mem1 >= 29
	r12_t5_mem1 += MM_MEM[1]

	r3_t3 = S.Task('r3_t3', length=4, delay_cost=1)
	S += r3_t3 >= 29
	r3_t3 += MAS[4]

	r41_in = S.Task('r41_in', length=1, delay_cost=1)
	S += r41_in >= 29
	r41_in += MAS_in[0]

	r41_mem0 = S.Task('r41_mem0', length=1, delay_cost=1)
	S += r41_mem0 >= 29
	r41_mem0 += MM_MEM[2]

	r41_mem1 = S.Task('r41_mem1', length=1, delay_cost=1)
	S += r41_mem1 >= 29
	r41_mem1 += MAS_MEM[1]

	r100_in = S.Task('r100_in', length=1, delay_cost=1)
	S += r100_in >= 30
	r100_in += MAS_in[0]

	r100_mem0 = S.Task('r100_mem0', length=1, delay_cost=1)
	S += r100_mem0 >= 30
	r100_mem0 += MAIN_MEM_r[0]

	r100_mem1 = S.Task('r100_mem1', length=1, delay_cost=1)
	S += r100_mem1 >= 30
	r100_mem1 += MAS_MEM[5]

	r12_t3 = S.Task('r12_t3', length=4, delay_cost=1)
	S += r12_t3 >= 30
	r12_t3 += MAS[5]

	r12_t5 = S.Task('r12_t5', length=4, delay_cost=1)
	S += r12_t5 >= 30
	r12_t5 += MAS[4]

	r13_t4_in = S.Task('r13_t4_in', length=1, delay_cost=1)
	S += r13_t4_in >= 30
	r13_t4_in += MM_in[0]

	r13_t4_mem0 = S.Task('r13_t4_mem0', length=1, delay_cost=1)
	S += r13_t4_mem0 >= 30
	r13_t4_mem0 += MAS_MEM[0]

	r13_t4_mem1 = S.Task('r13_t4_mem1', length=1, delay_cost=1)
	S += r13_t4_mem1 >= 30
	r13_t4_mem1 += MAS_MEM[9]

	r41 = S.Task('r41', length=4, delay_cost=1)
	S += r41 >= 30
	r41 += MAS[0]

	r100 = S.Task('r100', length=4, delay_cost=1)
	S += r100 >= 31
	r100 += MAS[0]

	r13_t4 = S.Task('r13_t4', length=10, delay_cost=1)
	S += r13_t4 >= 31
	r13_t4 += MM[0]

	r30_in = S.Task('r30_in', length=1, delay_cost=1)
	S += r30_in >= 31
	r30_in += MAS_in[5]

	r30_mem0 = S.Task('r30_mem0', length=1, delay_cost=1)
	S += r30_mem0 >= 31
	r30_mem0 += MM_MEM[0]

	r30_mem1 = S.Task('r30_mem1', length=1, delay_cost=1)
	S += r30_mem1 >= 31
	r30_mem1 += MM_MEM[1]

	r80_in = S.Task('r80_in', length=1, delay_cost=1)
	S += r80_in >= 31
	r80_in += MAS_in[0]

	r80_mem0 = S.Task('r80_mem0', length=1, delay_cost=1)
	S += r80_mem0 >= 31
	r80_mem0 += MAIN_MEM_r[0]

	r80_mem1 = S.Task('r80_mem1', length=1, delay_cost=1)
	S += r80_mem1 >= 31
	r80_mem1 += MAS_MEM[5]

	X_new_t0_in = S.Task('X_new_t0_in', length=1, delay_cost=1)
	S += X_new_t0_in >= 32
	X_new_t0_in += MM_in[1]

	X_new_t0_mem0 = S.Task('X_new_t0_mem0', length=1, delay_cost=1)
	S += X_new_t0_mem0 >= 32
	X_new_t0_mem0 += MAS_MEM[8]

	X_new_t0_mem1 = S.Task('X_new_t0_mem1', length=1, delay_cost=1)
	S += X_new_t0_mem1 >= 32
	X_new_t0_mem1 += MAS_MEM[1]

	r30 = S.Task('r30', length=4, delay_cost=1)
	S += r30 >= 32
	r30 += MAS[5]

	r3_t4_in = S.Task('r3_t4_in', length=1, delay_cost=1)
	S += r3_t4_in >= 32
	r3_t4_in += MM_in[0]

	r3_t4_mem0 = S.Task('r3_t4_mem0', length=1, delay_cost=1)
	S += r3_t4_mem0 >= 32
	r3_t4_mem0 += MAS_MEM[10]

	r3_t4_mem1 = S.Task('r3_t4_mem1', length=1, delay_cost=1)
	S += r3_t4_mem1 >= 32
	r3_t4_mem1 += MAS_MEM[9]

	r3_t5_in = S.Task('r3_t5_in', length=1, delay_cost=1)
	S += r3_t5_in >= 32
	r3_t5_in += MAS_in[0]

	r3_t5_mem0 = S.Task('r3_t5_mem0', length=1, delay_cost=1)
	S += r3_t5_mem0 >= 32
	r3_t5_mem0 += MM_MEM[0]

	r3_t5_mem1 = S.Task('r3_t5_mem1', length=1, delay_cost=1)
	S += r3_t5_mem1 >= 32
	r3_t5_mem1 += MM_MEM[1]

	r80 = S.Task('r80', length=4, delay_cost=1)
	S += r80 >= 32
	r80 += MAS[0]

	X_new_t0 = S.Task('X_new_t0', length=10, delay_cost=1)
	S += X_new_t0 >= 33
	X_new_t0 += MM[1]

	r101_in = S.Task('r101_in', length=1, delay_cost=1)
	S += r101_in >= 33
	r101_in += MAS_in[0]

	r101_mem0 = S.Task('r101_mem0', length=1, delay_cost=1)
	S += r101_mem0 >= 33
	r101_mem0 += MAIN_MEM_r[0]

	r101_mem1 = S.Task('r101_mem1', length=1, delay_cost=1)
	S += r101_mem1 >= 33
	r101_mem1 += MAS_MEM[1]

	r11_in = S.Task('r11_in', length=1, delay_cost=1)
	S += r11_in >= 33
	r11_in += MAS_in[5]

	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	S += r11_mem0 >= 33
	r11_mem0 += MM_MEM[0]

	r11_mem1 = S.Task('r11_mem1', length=1, delay_cost=1)
	S += r11_mem1 >= 33
	r11_mem1 += MAS_MEM[5]

	r12_t4_in = S.Task('r12_t4_in', length=1, delay_cost=1)
	S += r12_t4_in >= 33
	r12_t4_in += MM_in[0]

	r12_t4_mem0 = S.Task('r12_t4_mem0', length=1, delay_cost=1)
	S += r12_t4_mem0 >= 33
	r12_t4_mem0 += MAS_MEM[0]

	r12_t4_mem1 = S.Task('r12_t4_mem1', length=1, delay_cost=1)
	S += r12_t4_mem1 >= 33
	r12_t4_mem1 += MAS_MEM[11]

	r3_t4 = S.Task('r3_t4', length=10, delay_cost=1)
	S += r3_t4 >= 33
	r3_t4 += MM[0]

	r3_t5 = S.Task('r3_t5', length=4, delay_cost=1)
	S += r3_t5 >= 33
	r3_t5 += MAS[0]

	r101 = S.Task('r101', length=4, delay_cost=1)
	S += r101 >= 34
	r101 += MAS[0]

	r11 = S.Task('r11', length=4, delay_cost=1)
	S += r11 >= 34
	r11 += MAS[5]

	r12_t4 = S.Task('r12_t4', length=10, delay_cost=1)
	S += r12_t4 >= 34
	r12_t4 += MM[0]

	r130_in = S.Task('r130_in', length=1, delay_cost=1)
	S += r130_in >= 34
	r130_in += MAS_in[3]

	r130_mem0 = S.Task('r130_mem0', length=1, delay_cost=1)
	S += r130_mem0 >= 34
	r130_mem0 += MM_MEM[0]

	r130_mem1 = S.Task('r130_mem1', length=1, delay_cost=1)
	S += r130_mem1 >= 34
	r130_mem1 += MM_MEM[1]

	r81_in = S.Task('r81_in', length=1, delay_cost=1)
	S += r81_in >= 34
	r81_in += MAS_in[0]

	r81_mem0 = S.Task('r81_mem0', length=1, delay_cost=1)
	S += r81_mem0 >= 34
	r81_mem0 += MAIN_MEM_r[0]

	r81_mem1 = S.Task('r81_mem1', length=1, delay_cost=1)
	S += r81_mem1 >= 34
	r81_mem1 += MAS_MEM[1]

	r130 = S.Task('r130', length=4, delay_cost=1)
	S += r130 >= 35
	r130 += MAS[3]

	r14_t0_in = S.Task('r14_t0_in', length=1, delay_cost=1)
	S += r14_t0_in >= 35
	r14_t0_in += MM_in[0]

	r14_t0_mem0 = S.Task('r14_t0_mem0', length=1, delay_cost=1)
	S += r14_t0_mem0 >= 35
	r14_t0_mem0 += MAS_MEM[8]

	r14_t0_mem1 = S.Task('r14_t0_mem1', length=1, delay_cost=1)
	S += r14_t0_mem1 >= 35
	r14_t0_mem1 += MAS_MEM[11]

	r5_t5_in = S.Task('r5_t5_in', length=1, delay_cost=1)
	S += r5_t5_in >= 35
	r5_t5_in += MAS_in[0]

	r5_t5_mem0 = S.Task('r5_t5_mem0', length=1, delay_cost=1)
	S += r5_t5_mem0 >= 35
	r5_t5_mem0 += MM_MEM[2]

	r5_t5_mem1 = S.Task('r5_t5_mem1', length=1, delay_cost=1)
	S += r5_t5_mem1 >= 35
	r5_t5_mem1 += MM_MEM[1]

	r81 = S.Task('r81', length=4, delay_cost=1)
	S += r81 >= 35
	r81 += MAS[0]

	r13_t5_in = S.Task('r13_t5_in', length=1, delay_cost=1)
	S += r13_t5_in >= 36
	r13_t5_in += MAS_in[0]

	r13_t5_mem0 = S.Task('r13_t5_mem0', length=1, delay_cost=1)
	S += r13_t5_mem0 >= 36
	r13_t5_mem0 += MM_MEM[0]

	r13_t5_mem1 = S.Task('r13_t5_mem1', length=1, delay_cost=1)
	S += r13_t5_mem1 >= 36
	r13_t5_mem1 += MM_MEM[1]

	r14_t0 = S.Task('r14_t0', length=10, delay_cost=1)
	S += r14_t0 >= 36
	r14_t0 += MM[0]

	r5_t5 = S.Task('r5_t5', length=4, delay_cost=1)
	S += r5_t5 >= 36
	r5_t5 += MAS[0]

	r13_t5 = S.Task('r13_t5', length=4, delay_cost=1)
	S += r13_t5 >= 37
	r13_t5 += MAS[0]

	r21_in = S.Task('r21_in', length=1, delay_cost=1)
	S += r21_in >= 37
	r21_in += MAS_in[5]

	r21_mem0 = S.Task('r21_mem0', length=1, delay_cost=1)
	S += r21_mem0 >= 37
	r21_mem0 += MAS_MEM[10]

	r21_mem1 = S.Task('r21_mem1', length=1, delay_cost=1)
	S += r21_mem1 >= 37
	r21_mem1 += MAS_MEM[11]

	r50_in = S.Task('r50_in', length=1, delay_cost=1)
	S += r50_in >= 37
	r50_in += MAS_in[2]

	r50_mem0 = S.Task('r50_mem0', length=1, delay_cost=1)
	S += r50_mem0 >= 37
	r50_mem0 += MM_MEM[2]

	r50_mem1 = S.Task('r50_mem1', length=1, delay_cost=1)
	S += r50_mem1 >= 37
	r50_mem1 += MM_MEM[1]

	r61_in = S.Task('r61_in', length=1, delay_cost=1)
	S += r61_in >= 37
	r61_in += MAS_in[0]

	r61_mem0 = S.Task('r61_mem0', length=1, delay_cost=1)
	S += r61_mem0 >= 37
	r61_mem0 += MM_MEM[0]

	r61_mem1 = S.Task('r61_mem1', length=1, delay_cost=1)
	S += r61_mem1 >= 37
	r61_mem1 += MAS_MEM[1]

	Z_new_t0_in = S.Task('Z_new_t0_in', length=1, delay_cost=1)
	S += Z_new_t0_in >= 38
	Z_new_t0_in += MM_in[0]

	Z_new_t0_mem0 = S.Task('Z_new_t0_mem0', length=1, delay_cost=1)
	S += Z_new_t0_mem0 >= 38
	Z_new_t0_mem0 += MAS_MEM[8]

	Z_new_t0_mem1 = S.Task('Z_new_t0_mem1', length=1, delay_cost=1)
	S += Z_new_t0_mem1 >= 38
	Z_new_t0_mem1 += MAS_MEM[7]

	r11_t3_in = S.Task('r11_t3_in', length=1, delay_cost=1)
	S += r11_t3_in >= 38
	r11_t3_in += MM_in[1]

	r11_t3_mem0 = S.Task('r11_t3_mem0', length=1, delay_cost=1)
	S += r11_t3_mem0 >= 38
	r11_t3_mem0 += MAS_MEM[0]

	r11_t3_mem1 = S.Task('r11_t3_mem1', length=1, delay_cost=1)
	S += r11_t3_mem1 >= 38
	r11_t3_mem1 += MAS_MEM[1]

	r21 = S.Task('r21', length=4, delay_cost=1)
	S += r21 >= 38
	r21 += MAS[5]

	r50 = S.Task('r50', length=4, delay_cost=1)
	S += r50 >= 38
	r50 += MAS[2]

	r61 = S.Task('r61', length=4, delay_cost=1)
	S += r61 >= 38
	r61 += MAS[0]

	Z_new_t0 = S.Task('Z_new_t0', length=10, delay_cost=1)
	S += Z_new_t0 >= 39
	Z_new_t0 += MM[0]

	r11_t3 = S.Task('r11_t3', length=10, delay_cost=1)
	S += r11_t3 >= 39
	r11_t3 += MM[1]

	r51_in = S.Task('r51_in', length=1, delay_cost=1)
	S += r51_in >= 39
	r51_in += MAS_in[0]

	r51_mem0 = S.Task('r51_mem0', length=1, delay_cost=1)
	S += r51_mem0 >= 39
	r51_mem0 += MM_MEM[2]

	r51_mem1 = S.Task('r51_mem1', length=1, delay_cost=1)
	S += r51_mem1 >= 39
	r51_mem1 += MAS_MEM[1]

	r131_in = S.Task('r131_in', length=1, delay_cost=1)
	S += r131_in >= 40
	r131_in += MAS_in[0]

	r131_mem0 = S.Task('r131_mem0', length=1, delay_cost=1)
	S += r131_mem0 >= 40
	r131_mem0 += MM_MEM[0]

	r131_mem1 = S.Task('r131_mem1', length=1, delay_cost=1)
	S += r131_mem1 >= 40
	r131_mem1 += MAS_MEM[1]

	r51 = S.Task('r51', length=4, delay_cost=1)
	S += r51 >= 40
	r51 += MAS[0]

	Z_new_t2_in = S.Task('Z_new_t2_in', length=1, delay_cost=1)
	S += Z_new_t2_in >= 41
	Z_new_t2_in += MAS_in[0]

	Z_new_t2_mem0 = S.Task('Z_new_t2_mem0', length=1, delay_cost=1)
	S += Z_new_t2_mem0 >= 41
	Z_new_t2_mem0 += MAS_MEM[8]

	Z_new_t2_mem1 = S.Task('Z_new_t2_mem1', length=1, delay_cost=1)
	S += Z_new_t2_mem1 >= 41
	Z_new_t2_mem1 += MAS_MEM[11]

	r11_t0_in = S.Task('r11_t0_in', length=1, delay_cost=1)
	S += r11_t0_in >= 41
	r11_t0_in += MAS_in[4]

	r11_t0_mem0 = S.Task('r11_t0_mem0', length=1, delay_cost=1)
	S += r11_t0_mem0 >= 41
	r11_t0_mem0 += MAS_MEM[0]

	r11_t0_mem1 = S.Task('r11_t0_mem1', length=1, delay_cost=1)
	S += r11_t0_mem1 >= 41
	r11_t0_mem1 += MAS_MEM[1]

	r131 = S.Task('r131', length=4, delay_cost=1)
	S += r131 >= 41
	r131 += MAS[0]

	r70_in = S.Task('r70_in', length=1, delay_cost=1)
	S += r70_in >= 41
	r70_in += MAS_in[2]

	r70_mem0 = S.Task('r70_mem0', length=1, delay_cost=1)
	S += r70_mem0 >= 41
	r70_mem0 += MAS_MEM[4]

	r70_mem1 = S.Task('r70_mem1', length=1, delay_cost=1)
	S += r70_mem1 >= 41
	r70_mem1 += MAS_MEM[9]

	Z_new_t2 = S.Task('Z_new_t2', length=4, delay_cost=1)
	S += Z_new_t2 >= 42
	Z_new_t2 += MAS[0]

	r11_t0 = S.Task('r11_t0', length=4, delay_cost=1)
	S += r11_t0 >= 42
	r11_t0 += MAS[4]

	r14_t2_in = S.Task('r14_t2_in', length=1, delay_cost=1)
	S += r14_t2_in >= 42
	r14_t2_in += MAS_in[4]

	r14_t2_mem0 = S.Task('r14_t2_mem0', length=1, delay_cost=1)
	S += r14_t2_mem0 >= 42
	r14_t2_mem0 += MAS_MEM[8]

	r14_t2_mem1 = S.Task('r14_t2_mem1', length=1, delay_cost=1)
	S += r14_t2_mem1 >= 42
	r14_t2_mem1 += MAS_MEM[11]

	r31_in = S.Task('r31_in', length=1, delay_cost=1)
	S += r31_in >= 42
	r31_in += MAS_in[0]

	r31_mem0 = S.Task('r31_mem0', length=1, delay_cost=1)
	S += r31_mem0 >= 42
	r31_mem0 += MM_MEM[0]

	r31_mem1 = S.Task('r31_mem1', length=1, delay_cost=1)
	S += r31_mem1 >= 42
	r31_mem1 += MAS_MEM[1]

	r70 = S.Task('r70', length=4, delay_cost=1)
	S += r70 >= 42
	r70 += MAS[2]

	X_new_t2_in = S.Task('X_new_t2_in', length=1, delay_cost=1)
	S += X_new_t2_in >= 43
	X_new_t2_in += MAS_in[5]

	X_new_t2_mem0 = S.Task('X_new_t2_mem0', length=1, delay_cost=1)
	S += X_new_t2_mem0 >= 43
	X_new_t2_mem0 += MAS_MEM[8]

	X_new_t2_mem1 = S.Task('X_new_t2_mem1', length=1, delay_cost=1)
	S += X_new_t2_mem1 >= 43
	X_new_t2_mem1 += MAS_MEM[11]

	r121_in = S.Task('r121_in', length=1, delay_cost=1)
	S += r121_in >= 43
	r121_in += MAS_in[2]

	r121_mem0 = S.Task('r121_mem0', length=1, delay_cost=1)
	S += r121_mem0 >= 43
	r121_mem0 += MM_MEM[0]

	r121_mem1 = S.Task('r121_mem1', length=1, delay_cost=1)
	S += r121_mem1 >= 43
	r121_mem1 += MAS_MEM[9]

	r14_t2 = S.Task('r14_t2', length=4, delay_cost=1)
	S += r14_t2 >= 43
	r14_t2 += MAS[4]

	r31 = S.Task('r31', length=4, delay_cost=1)
	S += r31 >= 43
	r31 += MAS[0]

	r71_in = S.Task('r71_in', length=1, delay_cost=1)
	S += r71_in >= 43
	r71_in += MAS_in[0]

	r71_mem0 = S.Task('r71_mem0', length=1, delay_cost=1)
	S += r71_mem0 >= 43
	r71_mem0 += MAS_MEM[0]

	r71_mem1 = S.Task('r71_mem1', length=1, delay_cost=1)
	S += r71_mem1 >= 43
	r71_mem1 += MAS_MEM[1]

	X_new_t2 = S.Task('X_new_t2', length=4, delay_cost=1)
	S += X_new_t2 >= 44
	X_new_t2 += MAS[5]

	Z_new_t3_in = S.Task('Z_new_t3_in', length=1, delay_cost=1)
	S += Z_new_t3_in >= 44
	Z_new_t3_in += MAS_in[0]

	Z_new_t3_mem0 = S.Task('Z_new_t3_mem0', length=1, delay_cost=1)
	S += Z_new_t3_mem0 >= 44
	Z_new_t3_mem0 += MAS_MEM[6]

	Z_new_t3_mem1 = S.Task('Z_new_t3_mem1', length=1, delay_cost=1)
	S += Z_new_t3_mem1 >= 44
	Z_new_t3_mem1 += MAS_MEM[1]

	r121 = S.Task('r121', length=4, delay_cost=1)
	S += r121 >= 44
	r121 += MAS[2]

	r71 = S.Task('r71', length=4, delay_cost=1)
	S += r71 >= 44
	r71 += MAS[0]

	Z_new_t3 = S.Task('Z_new_t3', length=4, delay_cost=1)
	S += Z_new_t3 >= 45
	Z_new_t3 += MAS[0]

	r11_t1_in = S.Task('r11_t1_in', length=1, delay_cost=1)
	S += r11_t1_in >= 45
	r11_t1_in += MAS_in[2]

	r11_t1_mem0 = S.Task('r11_t1_mem0', length=1, delay_cost=1)
	S += r11_t1_mem0 >= 45
	r11_t1_mem0 += MAS_MEM[0]

	r11_t1_mem1 = S.Task('r11_t1_mem1', length=1, delay_cost=1)
	S += r11_t1_mem1 >= 45
	r11_t1_mem1 += MAS_MEM[1]

	r9_t0_in = S.Task('r9_t0_in', length=1, delay_cost=1)
	S += r9_t0_in >= 45
	r9_t0_in += MM_in[0]

	r9_t0_mem0 = S.Task('r9_t0_mem0', length=1, delay_cost=1)
	S += r9_t0_mem0 >= 45
	r9_t0_mem0 += MAIN_MEM_r[0]

	r9_t0_mem1 = S.Task('r9_t0_mem1', length=1, delay_cost=1)
	S += r9_t0_mem1 >= 45
	r9_t0_mem1 += MAS_MEM[5]

	r11_t1 = S.Task('r11_t1', length=4, delay_cost=1)
	S += r11_t1 >= 46
	r11_t1 += MAS[2]

	r14_t3_in = S.Task('r14_t3_in', length=1, delay_cost=1)
	S += r14_t3_in >= 46
	r14_t3_in += MAS_in[1]

	r14_t3_mem0 = S.Task('r14_t3_mem0', length=1, delay_cost=1)
	S += r14_t3_mem0 >= 46
	r14_t3_mem0 += MAS_MEM[10]

	r14_t3_mem1 = S.Task('r14_t3_mem1', length=1, delay_cost=1)
	S += r14_t3_mem1 >= 46
	r14_t3_mem1 += MAS_MEM[1]

	r9_t0 = S.Task('r9_t0', length=10, delay_cost=1)
	S += r9_t0 >= 46
	r9_t0 += MM[0]

	X_new_t3_in = S.Task('X_new_t3_in', length=1, delay_cost=1)
	S += X_new_t3_in >= 47
	X_new_t3_in += MAS_in[0]

	X_new_t3_mem0 = S.Task('X_new_t3_mem0', length=1, delay_cost=1)
	S += X_new_t3_mem0 >= 47
	X_new_t3_mem0 += MAS_MEM[0]

	X_new_t3_mem1 = S.Task('X_new_t3_mem1', length=1, delay_cost=1)
	S += X_new_t3_mem1 >= 47
	X_new_t3_mem1 += MAS_MEM[5]

	r14_t3 = S.Task('r14_t3', length=4, delay_cost=1)
	S += r14_t3 >= 47
	r14_t3 += MAS[1]

	X_new_t1_in = S.Task('X_new_t1_in', length=1, delay_cost=1)
	S += X_new_t1_in >= 48
	X_new_t1_in += MM_in[1]

	X_new_t1_mem0 = S.Task('X_new_t1_mem0', length=1, delay_cost=1)
	S += X_new_t1_mem0 >= 48
	X_new_t1_mem0 += MAS_MEM[10]

	X_new_t1_mem1 = S.Task('X_new_t1_mem1', length=1, delay_cost=1)
	S += X_new_t1_mem1 >= 48
	X_new_t1_mem1 += MAS_MEM[5]

	X_new_t3 = S.Task('X_new_t3', length=4, delay_cost=1)
	S += X_new_t3 >= 48
	X_new_t3 += MAS[0]

	r111_in = S.Task('r111_in', length=1, delay_cost=1)
	S += r111_in >= 48
	r111_in += MAS_in[5]

	r111_mem0 = S.Task('r111_mem0', length=1, delay_cost=1)
	S += r111_mem0 >= 48
	r111_mem0 += MM_MEM[2]

	r111_mem1 = S.Task('r111_mem1', length=1, delay_cost=1)
	S += r111_mem1 >= 48
	r111_mem1 += MM_MEM[3]

	X_new_t1 = S.Task('X_new_t1', length=10, delay_cost=1)
	S += X_new_t1 >= 49
	X_new_t1 += MM[1]

	r111 = S.Task('r111', length=4, delay_cost=1)
	S += r111 >= 49
	r111 += MAS[5]

	r11_t2_in = S.Task('r11_t2_in', length=1, delay_cost=1)
	S += r11_t2_in >= 49
	r11_t2_in += MM_in[1]

	r11_t2_mem0 = S.Task('r11_t2_mem0', length=1, delay_cost=1)
	S += r11_t2_mem0 >= 49
	r11_t2_mem0 += MAS_MEM[8]

	r11_t2_mem1 = S.Task('r11_t2_mem1', length=1, delay_cost=1)
	S += r11_t2_mem1 >= 49
	r11_t2_mem1 += MAS_MEM[5]

	r11_t5_in = S.Task('r11_t5_in', length=1, delay_cost=1)
	S += r11_t5_in >= 49
	r11_t5_in += MAS_in[5]

	r11_t5_mem0 = S.Task('r11_t5_mem0', length=1, delay_cost=1)
	S += r11_t5_mem0 >= 49
	r11_t5_mem0 += MM_MEM[2]

	r11_t5_mem1 = S.Task('r11_t5_mem1', length=1, delay_cost=1)
	S += r11_t5_mem1 >= 49
	r11_t5_mem1 += MM_MEM[3]

	r11_t2 = S.Task('r11_t2', length=10, delay_cost=1)
	S += r11_t2 >= 50
	r11_t2 += MM[1]

	r11_t5 = S.Task('r11_t5', length=4, delay_cost=1)
	S += r11_t5 >= 50
	r11_t5 += MAS[5]

	r14_t1_in = S.Task('r14_t1_in', length=1, delay_cost=1)
	S += r14_t1_in >= 50
	r14_t1_in += MM_in[0]

	r14_t1_mem0 = S.Task('r14_t1_mem0', length=1, delay_cost=1)
	S += r14_t1_mem0 >= 50
	r14_t1_mem0 += MAS_MEM[10]

	r14_t1_mem1 = S.Task('r14_t1_mem1', length=1, delay_cost=1)
	S += r14_t1_mem1 >= 50
	r14_t1_mem1 += MAS_MEM[1]

	r14_t4_in = S.Task('r14_t4_in', length=1, delay_cost=1)
	S += r14_t4_in >= 50
	r14_t4_in += MM_in[1]

	r14_t4_mem0 = S.Task('r14_t4_mem0', length=1, delay_cost=1)
	S += r14_t4_mem0 >= 50
	r14_t4_mem0 += MAS_MEM[8]

	r14_t4_mem1 = S.Task('r14_t4_mem1', length=1, delay_cost=1)
	S += r14_t4_mem1 >= 50
	r14_t4_mem1 += MAS_MEM[3]

	X_new_t4_in = S.Task('X_new_t4_in', length=1, delay_cost=1)
	S += X_new_t4_in >= 51
	X_new_t4_in += MM_in[1]

	X_new_t4_mem0 = S.Task('X_new_t4_mem0', length=1, delay_cost=1)
	S += X_new_t4_mem0 >= 51
	X_new_t4_mem0 += MAS_MEM[10]

	X_new_t4_mem1 = S.Task('X_new_t4_mem1', length=1, delay_cost=1)
	S += X_new_t4_mem1 >= 51
	X_new_t4_mem1 += MAS_MEM[1]

	r14_t1 = S.Task('r14_t1', length=10, delay_cost=1)
	S += r14_t1 >= 51
	r14_t1 += MM[0]

	r14_t4 = S.Task('r14_t4', length=10, delay_cost=1)
	S += r14_t4 >= 51
	r14_t4 += MM[1]

	X_new_t4 = S.Task('X_new_t4', length=10, delay_cost=1)
	S += X_new_t4 >= 52
	X_new_t4 += MM[1]

	r15_t2_in = S.Task('r15_t2_in', length=1, delay_cost=1)
	S += r15_t2_in >= 52
	r15_t2_in += MAS_in[0]

	r15_t2_mem0 = S.Task('r15_t2_mem0', length=1, delay_cost=1)
	S += r15_t2_mem0 >= 52
	r15_t2_mem0 += MAS_MEM[0]

	r15_t2_mem1 = S.Task('r15_t2_mem1', length=1, delay_cost=1)
	S += r15_t2_mem1 >= 52
	r15_t2_mem1 += MAS_MEM[1]

	r16_t1_in = S.Task('r16_t1_in', length=1, delay_cost=1)
	S += r16_t1_in >= 52
	r16_t1_in += MM_in[1]

	r16_t1_mem0 = S.Task('r16_t1_mem0', length=1, delay_cost=1)
	S += r16_t1_mem0 >= 52
	r16_t1_mem0 += MAS_MEM[10]

	r16_t1_mem1 = S.Task('r16_t1_mem1', length=1, delay_cost=1)
	S += r16_t1_mem1 >= 52
	r16_t1_mem1 += MAIN_MEM_r[1]

	r15_t2 = S.Task('r15_t2', length=4, delay_cost=1)
	S += r15_t2 >= 53
	r15_t2 += MAS[0]

	r16_t1 = S.Task('r16_t1', length=10, delay_cost=1)
	S += r16_t1 >= 53
	r16_t1 += MM[1]

	X_new_t5_in = S.Task('X_new_t5_in', length=1, delay_cost=1)
	S += X_new_t5_in >= 58
	X_new_t5_in += MAS_in[3]

	X_new_t5_mem0 = S.Task('X_new_t5_mem0', length=1, delay_cost=1)
	S += X_new_t5_mem0 >= 58
	X_new_t5_mem0 += MM_MEM[2]

	X_new_t5_mem1 = S.Task('X_new_t5_mem1', length=1, delay_cost=1)
	S += X_new_t5_mem1 >= 58
	X_new_t5_mem1 += MM_MEM[3]

	X_new_t5 = S.Task('X_new_t5', length=4, delay_cost=1)
	S += X_new_t5 >= 59
	X_new_t5 += MAS[3]

	r110_in = S.Task('r110_in', length=1, delay_cost=1)
	S += r110_in >= 59
	r110_in += MAS_in[3]

	r110_mem0 = S.Task('r110_mem0', length=1, delay_cost=1)
	S += r110_mem0 >= 59
	r110_mem0 += MM_MEM[2]

	r110_mem1 = S.Task('r110_mem1', length=1, delay_cost=1)
	S += r110_mem1 >= 59
	r110_mem1 += MAS_MEM[11]

	X_new0_in = S.Task('X_new0_in', length=1, delay_cost=1)
	S += X_new0_in >= 60
	X_new0_in += MAS_in[5]

	X_new0_mem0 = S.Task('X_new0_mem0', length=1, delay_cost=1)
	S += X_new0_mem0 >= 60
	X_new0_mem0 += MM_MEM[2]

	X_new0_mem1 = S.Task('X_new0_mem1', length=1, delay_cost=1)
	S += X_new0_mem1 >= 60
	X_new0_mem1 += MM_MEM[3]

	r110 = S.Task('r110', length=4, delay_cost=1)
	S += r110 >= 60
	r110 += MAS[3]

	r14_t5_in = S.Task('r14_t5_in', length=1, delay_cost=1)
	S += r14_t5_in >= 60
	r14_t5_in += MAS_in[2]

	r14_t5_mem0 = S.Task('r14_t5_mem0', length=1, delay_cost=1)
	S += r14_t5_mem0 >= 60
	r14_t5_mem0 += MM_MEM[0]

	r14_t5_mem1 = S.Task('r14_t5_mem1', length=1, delay_cost=1)
	S += r14_t5_mem1 >= 60
	r14_t5_mem1 += MM_MEM[1]

	X_new0 = S.Task('X_new0', length=4, delay_cost=1)
	S += X_new0 >= 61
	X_new0 += MAS[5]

	r14_t5 = S.Task('r14_t5', length=4, delay_cost=1)
	S += r14_t5 >= 61
	r14_t5 += MAS[2]

	X_new1_in = S.Task('X_new1_in', length=1, delay_cost=1)
	S += X_new1_in >= 62
	X_new1_in += MAS_in[0]

	X_new1_mem0 = S.Task('X_new1_mem0', length=1, delay_cost=1)
	S += X_new1_mem0 >= 62
	X_new1_mem0 += MM_MEM[2]

	X_new1_mem1 = S.Task('X_new1_mem1', length=1, delay_cost=1)
	S += X_new1_mem1 >= 62
	X_new1_mem1 += MAS_MEM[7]

	X_new1 = S.Task('X_new1', length=4, delay_cost=1)
	S += X_new1 >= 63
	X_new1 += MAS[0]

	r140_in = S.Task('r140_in', length=1, delay_cost=1)
	S += r140_in >= 63
	r140_in += MAS_in[1]

	r140_mem0 = S.Task('r140_mem0', length=1, delay_cost=1)
	S += r140_mem0 >= 63
	r140_mem0 += MM_MEM[0]

	r140_mem1 = S.Task('r140_mem1', length=1, delay_cost=1)
	S += r140_mem1 >= 63
	r140_mem1 += MM_MEM[1]

	r16_t0_in = S.Task('r16_t0_in', length=1, delay_cost=1)
	S += r16_t0_in >= 63
	r16_t0_in += MM_in[1]

	r16_t0_mem0 = S.Task('r16_t0_mem0', length=1, delay_cost=1)
	S += r16_t0_mem0 >= 63
	r16_t0_mem0 += MAS_MEM[6]

	r16_t0_mem1 = S.Task('r16_t0_mem1', length=1, delay_cost=1)
	S += r16_t0_mem1 >= 63
	r16_t0_mem1 += MAIN_MEM_r[1]

	r140 = S.Task('r140', length=4, delay_cost=1)
	S += r140 >= 64
	r140 += MAS[1]

	r141_in = S.Task('r141_in', length=1, delay_cost=1)
	S += r141_in >= 64
	r141_in += MAS_in[0]

	r141_mem0 = S.Task('r141_mem0', length=1, delay_cost=1)
	S += r141_mem0 >= 64
	r141_mem0 += MM_MEM[2]

	r141_mem1 = S.Task('r141_mem1', length=1, delay_cost=1)
	S += r141_mem1 >= 64
	r141_mem1 += MAS_MEM[5]

	r16_t0 = S.Task('r16_t0', length=10, delay_cost=1)
	S += r16_t0 >= 64
	r16_t0 += MM[1]

	r16_t2_in = S.Task('r16_t2_in', length=1, delay_cost=1)
	S += r16_t2_in >= 64
	r16_t2_in += MAS_in[5]

	r16_t2_mem0 = S.Task('r16_t2_mem0', length=1, delay_cost=1)
	S += r16_t2_mem0 >= 64
	r16_t2_mem0 += MAS_MEM[6]

	r16_t2_mem1 = S.Task('r16_t2_mem1', length=1, delay_cost=1)
	S += r16_t2_mem1 >= 64
	r16_t2_mem1 += MAS_MEM[11]

	X_new0_w = S.Task('X_new0_w', length=1, delay_cost=1)
	S += X_new0_w >= 65
	X_new0_w += MAIN_MEM_w

	r141 = S.Task('r141', length=4, delay_cost=1)
	S += r141 >= 65
	r141 += MAS[0]

	r16_t2 = S.Task('r16_t2', length=4, delay_cost=1)
	S += r16_t2 >= 65
	r16_t2 += MAS[5]

	r15_t1_in = S.Task('r15_t1_in', length=1, delay_cost=1)
	S += r15_t1_in >= 66
	r15_t1_in += MM_in[1]

	r15_t1_mem0 = S.Task('r15_t1_mem0', length=1, delay_cost=1)
	S += r15_t1_mem0 >= 66
	r15_t1_mem0 += MAS_MEM[0]

	r15_t1_mem1 = S.Task('r15_t1_mem1', length=1, delay_cost=1)
	S += r15_t1_mem1 >= 66
	r15_t1_mem1 += MAS_MEM[5]

	X_new1_w = S.Task('X_new1_w', length=1, delay_cost=1)
	S += X_new1_w >= 67
	X_new1_w += MAIN_MEM_w

	r15_t1 = S.Task('r15_t1', length=10, delay_cost=1)
	S += r15_t1 >= 67
	r15_t1 += MM[1]

	r15_t3_in = S.Task('r15_t3_in', length=1, delay_cost=1)
	S += r15_t3_in >= 67
	r15_t3_in += MAS_in[0]

	r15_t3_mem0 = S.Task('r15_t3_mem0', length=1, delay_cost=1)
	S += r15_t3_mem0 >= 67
	r15_t3_mem0 += MAS_MEM[2]

	r15_t3_mem1 = S.Task('r15_t3_mem1', length=1, delay_cost=1)
	S += r15_t3_mem1 >= 67
	r15_t3_mem1 += MAS_MEM[5]

	r15_t3 = S.Task('r15_t3', length=4, delay_cost=1)
	S += r15_t3 >= 68
	r15_t3 += MAS[0]

	r16_t4_in = S.Task('r16_t4_in', length=1, delay_cost=1)
	S += r16_t4_in >= 68
	r16_t4_in += MM_in[1]

	r16_t4_mem0 = S.Task('r16_t4_mem0', length=1, delay_cost=1)
	S += r16_t4_mem0 >= 68
	r16_t4_mem0 += MAS_MEM[10]

	r16_t4_mem1 = S.Task('r16_t4_mem1', length=1, delay_cost=1)
	S += r16_t4_mem1 >= 68
	r16_t4_mem1 += MAS_MEM[1]

	r16_t4 = S.Task('r16_t4', length=10, delay_cost=1)
	S += r16_t4 >= 69
	r16_t4 += MM[1]

	r15_t4_in = S.Task('r15_t4_in', length=1, delay_cost=1)
	S += r15_t4_in >= 71
	r15_t4_in += MM_in[0]

	r15_t4_mem0 = S.Task('r15_t4_mem0', length=1, delay_cost=1)
	S += r15_t4_mem0 >= 71
	r15_t4_mem0 += MAS_MEM[0]

	r15_t4_mem1 = S.Task('r15_t4_mem1', length=1, delay_cost=1)
	S += r15_t4_mem1 >= 71
	r15_t4_mem1 += MAS_MEM[1]

	r15_t4 = S.Task('r15_t4', length=10, delay_cost=1)
	S += r15_t4 >= 72
	r15_t4 += MM[0]

	r160_in = S.Task('r160_in', length=1, delay_cost=1)
	S += r160_in >= 73
	r160_in += MAS_in[0]

	r160_mem0 = S.Task('r160_mem0', length=1, delay_cost=1)
	S += r160_mem0 >= 73
	r160_mem0 += MM_MEM[2]

	r160_mem1 = S.Task('r160_mem1', length=1, delay_cost=1)
	S += r160_mem1 >= 73
	r160_mem1 += MM_MEM[3]

	r160 = S.Task('r160', length=4, delay_cost=1)
	S += r160 >= 74
	r160 += MAS[0]

	r16_t5_in = S.Task('r16_t5_in', length=1, delay_cost=1)
	S += r16_t5_in >= 74
	r16_t5_in += MAS_in[5]

	r16_t5_mem0 = S.Task('r16_t5_mem0', length=1, delay_cost=1)
	S += r16_t5_mem0 >= 74
	r16_t5_mem0 += MM_MEM[2]

	r16_t5_mem1 = S.Task('r16_t5_mem1', length=1, delay_cost=1)
	S += r16_t5_mem1 >= 74
	r16_t5_mem1 += MM_MEM[3]

	r16_t5 = S.Task('r16_t5', length=4, delay_cost=1)
	S += r16_t5 >= 75
	r16_t5 += MAS[5]

	r150_in = S.Task('r150_in', length=1, delay_cost=1)
	S += r150_in >= 76
	r150_in += MAS_in[0]

	r150_mem0 = S.Task('r150_mem0', length=1, delay_cost=1)
	S += r150_mem0 >= 76
	r150_mem0 += MM_MEM[0]

	r150_mem1 = S.Task('r150_mem1', length=1, delay_cost=1)
	S += r150_mem1 >= 76
	r150_mem1 += MM_MEM[3]

	r150 = S.Task('r150', length=4, delay_cost=1)
	S += r150 >= 77
	r150 += MAS[0]

	r15_t5_in = S.Task('r15_t5_in', length=1, delay_cost=1)
	S += r15_t5_in >= 77
	r15_t5_in += MAS_in[5]

	r15_t5_mem0 = S.Task('r15_t5_mem0', length=1, delay_cost=1)
	S += r15_t5_mem0 >= 77
	r15_t5_mem0 += MM_MEM[0]

	r15_t5_mem1 = S.Task('r15_t5_mem1', length=1, delay_cost=1)
	S += r15_t5_mem1 >= 77
	r15_t5_mem1 += MM_MEM[3]

	r15_t5 = S.Task('r15_t5', length=4, delay_cost=1)
	S += r15_t5 >= 78
	r15_t5 += MAS[5]

	r161_in = S.Task('r161_in', length=1, delay_cost=1)
	S += r161_in >= 78
	r161_in += MAS_in[0]

	r161_mem0 = S.Task('r161_mem0', length=1, delay_cost=1)
	S += r161_mem0 >= 78
	r161_mem0 += MM_MEM[2]

	r161_mem1 = S.Task('r161_mem1', length=1, delay_cost=1)
	S += r161_mem1 >= 78
	r161_mem1 += MAS_MEM[11]

	r161 = S.Task('r161', length=4, delay_cost=1)
	S += r161 >= 79
	r161 += MAS[0]

	r170_in = S.Task('r170_in', length=1, delay_cost=1)
	S += r170_in >= 80
	r170_in += MAS_in[0]

	r170_mem0 = S.Task('r170_mem0', length=1, delay_cost=1)
	S += r170_mem0 >= 80
	r170_mem0 += MAS_MEM[2]

	r170_mem1 = S.Task('r170_mem1', length=1, delay_cost=1)
	S += r170_mem1 >= 80
	r170_mem1 += MAS_MEM[1]

	r151_in = S.Task('r151_in', length=1, delay_cost=1)
	S += r151_in >= 81
	r151_in += MAS_in[0]

	r151_mem0 = S.Task('r151_mem0', length=1, delay_cost=1)
	S += r151_mem0 >= 81
	r151_mem0 += MM_MEM[0]

	r151_mem1 = S.Task('r151_mem1', length=1, delay_cost=1)
	S += r151_mem1 >= 81
	r151_mem1 += MAS_MEM[11]

	r170 = S.Task('r170', length=4, delay_cost=1)
	S += r170 >= 81
	r170 += MAS[0]

	r151 = S.Task('r151', length=4, delay_cost=1)
	S += r151 >= 82
	r151 += MAS[0]

	Y_new0_in = S.Task('Y_new0_in', length=1, delay_cost=1)
	S += Y_new0_in >= 84
	Y_new0_in += MAS_in[0]

	Y_new0_mem0 = S.Task('Y_new0_mem0', length=1, delay_cost=1)
	S += Y_new0_mem0 >= 84
	Y_new0_mem0 += MAS_MEM[0]

	Y_new0_mem1 = S.Task('Y_new0_mem1', length=1, delay_cost=1)
	S += Y_new0_mem1 >= 84
	Y_new0_mem1 += MAS_MEM[1]

	Y_new0 = S.Task('Y_new0', length=4, delay_cost=1)
	S += Y_new0 >= 85
	Y_new0 += MAS[0]

	r171_in = S.Task('r171_in', length=1, delay_cost=1)
	S += r171_in >= 85
	r171_in += MAS_in[0]

	r171_mem0 = S.Task('r171_mem0', length=1, delay_cost=1)
	S += r171_mem0 >= 85
	r171_mem0 += MAS_MEM[0]

	r171_mem1 = S.Task('r171_mem1', length=1, delay_cost=1)
	S += r171_mem1 >= 85
	r171_mem1 += MAS_MEM[1]

	r171 = S.Task('r171', length=4, delay_cost=1)
	S += r171 >= 86
	r171 += MAS[0]

	Y_new0_w = S.Task('Y_new0_w', length=1, delay_cost=1)
	S += Y_new0_w >= 89
	Y_new0_w += MAIN_MEM_w

	Y_new1_in = S.Task('Y_new1_in', length=1, delay_cost=1)
	S += Y_new1_in >= 89
	Y_new1_in += MAS_in[5]

	Y_new1_mem0 = S.Task('Y_new1_mem0', length=1, delay_cost=1)
	S += Y_new1_mem0 >= 89
	Y_new1_mem0 += MAS_MEM[0]

	Y_new1_mem1 = S.Task('Y_new1_mem1', length=1, delay_cost=1)
	S += Y_new1_mem1 >= 89
	Y_new1_mem1 += MAS_MEM[1]

	Y_new1 = S.Task('Y_new1', length=4, delay_cost=1)
	S += Y_new1 >= 90
	Y_new1 += MAS[5]

	Y_new1_w = S.Task('Y_new1_w', length=1, delay_cost=1)
	S += Y_new1_w >= 94
	Y_new1_w += MAIN_MEM_w


	# new tasks
	r9_t1 = S.Task('r9_t1', length=10, delay_cost=1)
	r9_t1 += alt(MM)
	r9_t1_in = S.Task('r9_t1_in', length=1, delay_cost=1)
	r9_t1_in += alt(MM_in)
	S += r9_t1_in*MM_in[0]<=r9_t1*MM[0]
	S += r9_t1_in*MM_in[1]<=r9_t1*MM[1]
	S += r9_t1<1000

	r9_t1_mem0 = S.Task('r9_t1_mem0', length=1, delay_cost=1)
	r9_t1_mem0 += MAIN_MEM_r[0]
	S += r9_t1_mem0 <= r9_t1

	r9_t1_mem1 = S.Task('r9_t1_mem1', length=1, delay_cost=1)
	r9_t1_mem1 += MAS_MEM[1]
	S += 47 < r9_t1_mem1
	S += r9_t1_mem1 <= r9_t1

	r9_t3 = S.Task('r9_t3', length=4, delay_cost=1)
	r9_t3 += alt(MAS)
	r9_t3_in = S.Task('r9_t3_in', length=1, delay_cost=1)
	r9_t3_in += alt(MAS_in)
	S += r9_t3_in*MAS_in[0]<=r9_t3*MAS[0]

	S += r9_t3_in*MAS_in[1]<=r9_t3*MAS[1]

	S += r9_t3_in*MAS_in[2]<=r9_t3*MAS[2]

	S += r9_t3_in*MAS_in[3]<=r9_t3*MAS[3]

	S += r9_t3_in*MAS_in[4]<=r9_t3*MAS[4]

	S += r9_t3_in*MAS_in[5]<=r9_t3*MAS[5]

	S += r9_t3<1000

	r9_t3_mem0 = S.Task('r9_t3_mem0', length=1, delay_cost=1)
	r9_t3_mem0 += MAS_MEM[4]
	S += 45 < r9_t3_mem0
	S += r9_t3_mem0 <= r9_t3

	r9_t3_mem1 = S.Task('r9_t3_mem1', length=1, delay_cost=1)
	r9_t3_mem1 += MAS_MEM[1]
	S += 47 < r9_t3_mem1
	S += r9_t3_mem1 <= r9_t3

	Z_new_t1 = S.Task('Z_new_t1', length=10, delay_cost=1)
	Z_new_t1 += alt(MM)
	Z_new_t1_in = S.Task('Z_new_t1_in', length=1, delay_cost=1)
	Z_new_t1_in += alt(MM_in)
	S += Z_new_t1_in*MM_in[0]<=Z_new_t1*MM[0]
	S += Z_new_t1_in*MM_in[1]<=Z_new_t1*MM[1]
	S += Z_new_t1<1000

	Z_new_t1_mem0 = S.Task('Z_new_t1_mem0', length=1, delay_cost=1)
	Z_new_t1_mem0 += MAS_MEM[10]
	S += 41 < Z_new_t1_mem0
	S += Z_new_t1_mem0 <= Z_new_t1

	Z_new_t1_mem1 = S.Task('Z_new_t1_mem1', length=1, delay_cost=1)
	Z_new_t1_mem1 += MAS_MEM[1]
	S += 44 < Z_new_t1_mem1
	S += Z_new_t1_mem1 <= Z_new_t1

	r9_t4 = S.Task('r9_t4', length=10, delay_cost=1)
	r9_t4 += alt(MM)
	r9_t4_in = S.Task('r9_t4_in', length=1, delay_cost=1)
	r9_t4_in += alt(MM_in)
	S += r9_t4_in*MM_in[0]<=r9_t4*MM[0]
	S += r9_t4_in*MM_in[1]<=r9_t4*MM[1]
	S += r9_t4<63

	r9_t4_mem0 = S.Task('r9_t4_mem0', length=1, delay_cost=1)
	r9_t4_mem0 += MAS_MEM[8]
	S += 31 < r9_t4_mem0
	S += r9_t4_mem0 <= r9_t4

	r9_t4_mem1 = S.Task('r9_t4_mem1', length=1, delay_cost=1)
	r9_t4_mem1 += alt(MAS_MEM)
	S += (r9_t3*MAS[0])-1 < r9_t4_mem1*MAS_MEM[1]
	S += (r9_t3*MAS[1])-1 < r9_t4_mem1*MAS_MEM[3]
	S += (r9_t3*MAS[2])-1 < r9_t4_mem1*MAS_MEM[5]
	S += (r9_t3*MAS[3])-1 < r9_t4_mem1*MAS_MEM[7]
	S += (r9_t3*MAS[4])-1 < r9_t4_mem1*MAS_MEM[9]
	S += (r9_t3*MAS[5])-1 < r9_t4_mem1*MAS_MEM[11]
	S += r9_t4_mem1 <= r9_t4

	r90 = S.Task('r90', length=4, delay_cost=1)
	r90 += alt(MAS)
	r90_in = S.Task('r90_in', length=1, delay_cost=1)
	r90_in += alt(MAS_in)
	S += r90_in*MAS_in[0]<=r90*MAS[0]

	S += r90_in*MAS_in[1]<=r90*MAS[1]

	S += r90_in*MAS_in[2]<=r90*MAS[2]

	S += r90_in*MAS_in[3]<=r90*MAS[3]

	S += r90_in*MAS_in[4]<=r90*MAS[4]

	S += r90_in*MAS_in[5]<=r90*MAS[5]

	S += r90<62

	r90_mem0 = S.Task('r90_mem0', length=1, delay_cost=1)
	r90_mem0 += MM_MEM[0]
	S += 55 < r90_mem0
	S += r90_mem0 <= r90

	r90_mem1 = S.Task('r90_mem1', length=1, delay_cost=1)
	r90_mem1 += alt(MM_MEM)
	S += (r9_t1*MM[0])-1 < r90_mem1*MM_MEM[1]
	S += (r9_t1*MM[1])-1 < r90_mem1*MM_MEM[3]
	S += r90_mem1 <= r90

	r9_t5 = S.Task('r9_t5', length=4, delay_cost=1)
	r9_t5 += alt(MAS)
	r9_t5_in = S.Task('r9_t5_in', length=1, delay_cost=1)
	r9_t5_in += alt(MAS_in)
	S += r9_t5_in*MAS_in[0]<=r9_t5*MAS[0]

	S += r9_t5_in*MAS_in[1]<=r9_t5*MAS[1]

	S += r9_t5_in*MAS_in[2]<=r9_t5*MAS[2]

	S += r9_t5_in*MAS_in[3]<=r9_t5*MAS[3]

	S += r9_t5_in*MAS_in[4]<=r9_t5*MAS[4]

	S += r9_t5_in*MAS_in[5]<=r9_t5*MAS[5]

	S += r9_t5<63

	r9_t5_mem0 = S.Task('r9_t5_mem0', length=1, delay_cost=1)
	r9_t5_mem0 += MM_MEM[0]
	S += 55 < r9_t5_mem0
	S += r9_t5_mem0 <= r9_t5

	r9_t5_mem1 = S.Task('r9_t5_mem1', length=1, delay_cost=1)
	r9_t5_mem1 += alt(MM_MEM)
	S += (r9_t1*MM[0])-1 < r9_t5_mem1*MM_MEM[1]
	S += (r9_t1*MM[1])-1 < r9_t5_mem1*MM_MEM[3]
	S += r9_t5_mem1 <= r9_t5

	Z_new_t4 = S.Task('Z_new_t4', length=10, delay_cost=1)
	Z_new_t4 += alt(MM)
	Z_new_t4_in = S.Task('Z_new_t4_in', length=1, delay_cost=1)
	Z_new_t4_in += alt(MM_in)
	S += Z_new_t4_in*MM_in[0]<=Z_new_t4*MM[0]
	S += Z_new_t4_in*MM_in[1]<=Z_new_t4*MM[1]
	S += Z_new_t4<64

	Z_new_t4_mem0 = S.Task('Z_new_t4_mem0', length=1, delay_cost=1)
	Z_new_t4_mem0 += MAS_MEM[0]
	S += 45 < Z_new_t4_mem0
	S += Z_new_t4_mem0 <= Z_new_t4

	Z_new_t4_mem1 = S.Task('Z_new_t4_mem1', length=1, delay_cost=1)
	Z_new_t4_mem1 += MAS_MEM[1]
	S += 48 < Z_new_t4_mem1
	S += Z_new_t4_mem1 <= Z_new_t4

	Z_new0 = S.Task('Z_new0', length=4, delay_cost=1)
	Z_new0 += alt(MAS)
	Z_new0_in = S.Task('Z_new0_in', length=1, delay_cost=1)
	Z_new0_in += alt(MAS_in)
	S += Z_new0_in*MAS_in[0]<=Z_new0*MAS[0]

	S += Z_new0_in*MAS_in[1]<=Z_new0*MAS[1]

	S += Z_new0_in*MAS_in[2]<=Z_new0*MAS[2]

	S += Z_new0_in*MAS_in[3]<=Z_new0*MAS[3]

	S += Z_new0_in*MAS_in[4]<=Z_new0*MAS[4]

	S += Z_new0_in*MAS_in[5]<=Z_new0*MAS[5]

	S += 0<Z_new0

	Z_new0_w = S.Task('Z_new0_w', length=1, delay_cost=1)
	Z_new0_w += alt(MAIN_MEM_w)
	S += Z_new0 <= Z_new0_w

	S += Z_new0<1000

	Z_new0_mem0 = S.Task('Z_new0_mem0', length=1, delay_cost=1)
	Z_new0_mem0 += MM_MEM[0]
	S += 48 < Z_new0_mem0
	S += Z_new0_mem0 <= Z_new0

	Z_new0_mem1 = S.Task('Z_new0_mem1', length=1, delay_cost=1)
	Z_new0_mem1 += alt(MM_MEM)
	S += (Z_new_t1*MM[0])-1 < Z_new0_mem1*MM_MEM[1]
	S += (Z_new_t1*MM[1])-1 < Z_new0_mem1*MM_MEM[3]
	S += Z_new0_mem1 <= Z_new0

	Z_new_t5 = S.Task('Z_new_t5', length=4, delay_cost=1)
	Z_new_t5 += alt(MAS)
	Z_new_t5_in = S.Task('Z_new_t5_in', length=1, delay_cost=1)
	Z_new_t5_in += alt(MAS_in)
	S += Z_new_t5_in*MAS_in[0]<=Z_new_t5*MAS[0]

	S += Z_new_t5_in*MAS_in[1]<=Z_new_t5*MAS[1]

	S += Z_new_t5_in*MAS_in[2]<=Z_new_t5*MAS[2]

	S += Z_new_t5_in*MAS_in[3]<=Z_new_t5*MAS[3]

	S += Z_new_t5_in*MAS_in[4]<=Z_new_t5*MAS[4]

	S += Z_new_t5_in*MAS_in[5]<=Z_new_t5*MAS[5]

	S += Z_new_t5<64

	Z_new_t5_mem0 = S.Task('Z_new_t5_mem0', length=1, delay_cost=1)
	Z_new_t5_mem0 += MM_MEM[0]
	S += 48 < Z_new_t5_mem0
	S += Z_new_t5_mem0 <= Z_new_t5

	Z_new_t5_mem1 = S.Task('Z_new_t5_mem1', length=1, delay_cost=1)
	Z_new_t5_mem1 += alt(MM_MEM)
	S += (Z_new_t1*MM[0])-1 < Z_new_t5_mem1*MM_MEM[1]
	S += (Z_new_t1*MM[1])-1 < Z_new_t5_mem1*MM_MEM[3]
	S += Z_new_t5_mem1 <= Z_new_t5

	r91 = S.Task('r91', length=4, delay_cost=1)
	r91 += alt(MAS)
	r91_in = S.Task('r91_in', length=1, delay_cost=1)
	r91_in += alt(MAS_in)
	S += r91_in*MAS_in[0]<=r91*MAS[0]

	S += r91_in*MAS_in[1]<=r91*MAS[1]

	S += r91_in*MAS_in[2]<=r91*MAS[2]

	S += r91_in*MAS_in[3]<=r91*MAS[3]

	S += r91_in*MAS_in[4]<=r91*MAS[4]

	S += r91_in*MAS_in[5]<=r91*MAS[5]

	S += r91<67

	r91_mem0 = S.Task('r91_mem0', length=1, delay_cost=1)
	r91_mem0 += alt(MM_MEM)
	S += (r9_t4*MM[0])-1 < r91_mem0*MM_MEM[0]
	S += (r9_t4*MM[1])-1 < r91_mem0*MM_MEM[2]
	S += r91_mem0 <= r91

	r91_mem1 = S.Task('r91_mem1', length=1, delay_cost=1)
	r91_mem1 += alt(MAS_MEM)
	S += (r9_t5*MAS[0])-1 < r91_mem1*MAS_MEM[1]
	S += (r9_t5*MAS[1])-1 < r91_mem1*MAS_MEM[3]
	S += (r9_t5*MAS[2])-1 < r91_mem1*MAS_MEM[5]
	S += (r9_t5*MAS[3])-1 < r91_mem1*MAS_MEM[7]
	S += (r9_t5*MAS[4])-1 < r91_mem1*MAS_MEM[9]
	S += (r9_t5*MAS[5])-1 < r91_mem1*MAS_MEM[11]
	S += r91_mem1 <= r91

	r15_t0 = S.Task('r15_t0', length=10, delay_cost=1)
	r15_t0 += alt(MM)
	r15_t0_in = S.Task('r15_t0_in', length=1, delay_cost=1)
	r15_t0_in += alt(MM_in)
	S += r15_t0_in*MM_in[0]<=r15_t0*MM[0]
	S += r15_t0_in*MM_in[1]<=r15_t0*MM[1]
	S += r15_t0<77

	r15_t0_mem0 = S.Task('r15_t0_mem0', length=1, delay_cost=1)
	r15_t0_mem0 += MAS_MEM[0]
	S += 35 < r15_t0_mem0
	S += r15_t0_mem0 <= r15_t0

	r15_t0_mem1 = S.Task('r15_t0_mem1', length=1, delay_cost=1)
	r15_t0_mem1 += alt(MAS_MEM)
	S += (r90*MAS[0])-1 < r15_t0_mem1*MAS_MEM[1]
	S += (r90*MAS[1])-1 < r15_t0_mem1*MAS_MEM[3]
	S += (r90*MAS[2])-1 < r15_t0_mem1*MAS_MEM[5]
	S += (r90*MAS[3])-1 < r15_t0_mem1*MAS_MEM[7]
	S += (r90*MAS[4])-1 < r15_t0_mem1*MAS_MEM[9]
	S += (r90*MAS[5])-1 < r15_t0_mem1*MAS_MEM[11]
	S += r15_t0_mem1 <= r15_t0

	Z_new1 = S.Task('Z_new1', length=4, delay_cost=1)
	Z_new1 += alt(MAS)
	Z_new1_in = S.Task('Z_new1_in', length=1, delay_cost=1)
	Z_new1_in += alt(MAS_in)
	S += Z_new1_in*MAS_in[0]<=Z_new1*MAS[0]

	S += Z_new1_in*MAS_in[1]<=Z_new1*MAS[1]

	S += Z_new1_in*MAS_in[2]<=Z_new1*MAS[2]

	S += Z_new1_in*MAS_in[3]<=Z_new1*MAS[3]

	S += Z_new1_in*MAS_in[4]<=Z_new1*MAS[4]

	S += Z_new1_in*MAS_in[5]<=Z_new1*MAS[5]

	S += 0<Z_new1

	Z_new1_w = S.Task('Z_new1_w', length=1, delay_cost=1)
	Z_new1_w += alt(MAIN_MEM_w)
	S += Z_new1 <= Z_new1_w

	S += Z_new1<1000

	Z_new1_mem0 = S.Task('Z_new1_mem0', length=1, delay_cost=1)
	Z_new1_mem0 += alt(MM_MEM)
	S += (Z_new_t4*MM[0])-1 < Z_new1_mem0*MM_MEM[0]
	S += (Z_new_t4*MM[1])-1 < Z_new1_mem0*MM_MEM[2]
	S += Z_new1_mem0 <= Z_new1

	Z_new1_mem1 = S.Task('Z_new1_mem1', length=1, delay_cost=1)
	Z_new1_mem1 += alt(MAS_MEM)
	S += (Z_new_t5*MAS[0])-1 < Z_new1_mem1*MAS_MEM[1]
	S += (Z_new_t5*MAS[1])-1 < Z_new1_mem1*MAS_MEM[3]
	S += (Z_new_t5*MAS[2])-1 < Z_new1_mem1*MAS_MEM[5]
	S += (Z_new_t5*MAS[3])-1 < Z_new1_mem1*MAS_MEM[7]
	S += (Z_new_t5*MAS[4])-1 < Z_new1_mem1*MAS_MEM[9]
	S += (Z_new_t5*MAS[5])-1 < Z_new1_mem1*MAS_MEM[11]
	S += Z_new1_mem1 <= Z_new1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage4MAS6/EP2_YRECOVER/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

