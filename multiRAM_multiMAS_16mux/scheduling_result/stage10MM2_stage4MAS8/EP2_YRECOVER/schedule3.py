from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 215
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=8)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	r3_t1_in = S.Task('r3_t1_in', length=1, delay_cost=1)
	S += r3_t1_in >= 0
	r3_t1_in += MM_in[0]

	r3_t1_mem0 = S.Task('r3_t1_mem0', length=1, delay_cost=1)
	S += r3_t1_mem0 >= 0
	r3_t1_mem0 += MAIN_MEM_r[0]

	r3_t1_mem1 = S.Task('r3_t1_mem1', length=1, delay_cost=1)
	S += r3_t1_mem1 >= 0
	r3_t1_mem1 += MAIN_MEM_r[1]

	r3_t1 = S.Task('r3_t1', length=10, delay_cost=1)
	S += r3_t1 >= 1
	r3_t1 += MM[0]

	r3_t2_in = S.Task('r3_t2_in', length=1, delay_cost=1)
	S += r3_t2_in >= 1
	r3_t2_in += MAS_in[5]

	r3_t2_mem0 = S.Task('r3_t2_mem0', length=1, delay_cost=1)
	S += r3_t2_mem0 >= 1
	r3_t2_mem0 += MAIN_MEM_r[0]

	r3_t2_mem1 = S.Task('r3_t2_mem1', length=1, delay_cost=1)
	S += r3_t2_mem1 >= 1
	r3_t2_mem1 += MAIN_MEM_r[1]

	r1_t1_in = S.Task('r1_t1_in', length=1, delay_cost=1)
	S += r1_t1_in >= 2
	r1_t1_in += MM_in[0]

	r1_t1_mem0 = S.Task('r1_t1_mem0', length=1, delay_cost=1)
	S += r1_t1_mem0 >= 2
	r1_t1_mem0 += MAIN_MEM_r[0]

	r1_t1_mem1 = S.Task('r1_t1_mem1', length=1, delay_cost=1)
	S += r1_t1_mem1 >= 2
	r1_t1_mem1 += MAIN_MEM_r[1]

	r3_t2 = S.Task('r3_t2', length=4, delay_cost=1)
	S += r3_t2 >= 2
	r3_t2 += MAS[5]

	r1_t1 = S.Task('r1_t1', length=10, delay_cost=1)
	S += r1_t1 >= 3
	r1_t1 += MM[0]

	r3_t3_in = S.Task('r3_t3_in', length=1, delay_cost=1)
	S += r3_t3_in >= 3
	r3_t3_in += MAS_in[2]

	r3_t3_mem0 = S.Task('r3_t3_mem0', length=1, delay_cost=1)
	S += r3_t3_mem0 >= 3
	r3_t3_mem0 += MAIN_MEM_r[0]

	r3_t3_mem1 = S.Task('r3_t3_mem1', length=1, delay_cost=1)
	S += r3_t3_mem1 >= 3
	r3_t3_mem1 += MAIN_MEM_r[1]

	r1_t3_in = S.Task('r1_t3_in', length=1, delay_cost=1)
	S += r1_t3_in >= 4
	r1_t3_in += MAS_in[0]

	r1_t3_mem0 = S.Task('r1_t3_mem0', length=1, delay_cost=1)
	S += r1_t3_mem0 >= 4
	r1_t3_mem0 += MAIN_MEM_r[0]

	r1_t3_mem1 = S.Task('r1_t3_mem1', length=1, delay_cost=1)
	S += r1_t3_mem1 >= 4
	r1_t3_mem1 += MAIN_MEM_r[1]

	r3_t3 = S.Task('r3_t3', length=4, delay_cost=1)
	S += r3_t3 >= 4
	r3_t3 += MAS[2]

	r1_t3 = S.Task('r1_t3', length=4, delay_cost=1)
	S += r1_t3 >= 5
	r1_t3 += MAS[0]

	r4_t0_in = S.Task('r4_t0_in', length=1, delay_cost=1)
	S += r4_t0_in >= 5
	r4_t0_in += MM_in[0]

	r4_t0_mem0 = S.Task('r4_t0_mem0', length=1, delay_cost=1)
	S += r4_t0_mem0 >= 5
	r4_t0_mem0 += MAIN_MEM_r[0]

	r4_t0_mem1 = S.Task('r4_t0_mem1', length=1, delay_cost=1)
	S += r4_t0_mem1 >= 5
	r4_t0_mem1 += MAIN_MEM_r[1]

	r4_t0 = S.Task('r4_t0', length=10, delay_cost=1)
	S += r4_t0 >= 6
	r4_t0 += MM[0]

	r6_t0_in = S.Task('r6_t0_in', length=1, delay_cost=1)
	S += r6_t0_in >= 6
	r6_t0_in += MM_in[0]

	r6_t0_mem0 = S.Task('r6_t0_mem0', length=1, delay_cost=1)
	S += r6_t0_mem0 >= 6
	r6_t0_mem0 += MAIN_MEM_r[0]

	r6_t0_mem1 = S.Task('r6_t0_mem1', length=1, delay_cost=1)
	S += r6_t0_mem1 >= 6
	r6_t0_mem1 += MAIN_MEM_r[1]

	r1_t0_in = S.Task('r1_t0_in', length=1, delay_cost=1)
	S += r1_t0_in >= 7
	r1_t0_in += MM_in[1]

	r1_t0_mem0 = S.Task('r1_t0_mem0', length=1, delay_cost=1)
	S += r1_t0_mem0 >= 7
	r1_t0_mem0 += MAIN_MEM_r[0]

	r1_t0_mem1 = S.Task('r1_t0_mem1', length=1, delay_cost=1)
	S += r1_t0_mem1 >= 7
	r1_t0_mem1 += MAIN_MEM_r[1]

	r3_t4_in = S.Task('r3_t4_in', length=1, delay_cost=1)
	S += r3_t4_in >= 7
	r3_t4_in += MM_in[0]

	r3_t4_mem0 = S.Task('r3_t4_mem0', length=1, delay_cost=1)
	S += r3_t4_mem0 >= 7
	r3_t4_mem0 += MAS_MEM[10]

	r3_t4_mem1 = S.Task('r3_t4_mem1', length=1, delay_cost=1)
	S += r3_t4_mem1 >= 7
	r3_t4_mem1 += MAS_MEM[5]

	r6_t0 = S.Task('r6_t0', length=10, delay_cost=1)
	S += r6_t0 >= 7
	r6_t0 += MM[0]

	r1_t0 = S.Task('r1_t0', length=10, delay_cost=1)
	S += r1_t0 >= 8
	r1_t0 += MM[1]

	r3_t4 = S.Task('r3_t4', length=10, delay_cost=1)
	S += r3_t4 >= 8
	r3_t4 += MM[0]

	r4_t1_in = S.Task('r4_t1_in', length=1, delay_cost=1)
	S += r4_t1_in >= 8
	r4_t1_in += MM_in[0]

	r4_t1_mem0 = S.Task('r4_t1_mem0', length=1, delay_cost=1)
	S += r4_t1_mem0 >= 8
	r4_t1_mem0 += MAIN_MEM_r[0]

	r4_t1_mem1 = S.Task('r4_t1_mem1', length=1, delay_cost=1)
	S += r4_t1_mem1 >= 8
	r4_t1_mem1 += MAIN_MEM_r[1]

	r4_t1 = S.Task('r4_t1', length=10, delay_cost=1)
	S += r4_t1 >= 9
	r4_t1 += MM[0]

	r5_t0_in = S.Task('r5_t0_in', length=1, delay_cost=1)
	S += r5_t0_in >= 9
	r5_t0_in += MM_in[0]

	r5_t0_mem0 = S.Task('r5_t0_mem0', length=1, delay_cost=1)
	S += r5_t0_mem0 >= 9
	r5_t0_mem0 += MAIN_MEM_r[0]

	r5_t0_mem1 = S.Task('r5_t0_mem1', length=1, delay_cost=1)
	S += r5_t0_mem1 >= 9
	r5_t0_mem1 += MAIN_MEM_r[1]

	r5_t0 = S.Task('r5_t0', length=10, delay_cost=1)
	S += r5_t0 >= 10
	r5_t0 += MM[0]

	r6_t1_in = S.Task('r6_t1_in', length=1, delay_cost=1)
	S += r6_t1_in >= 10
	r6_t1_in += MM_in[0]

	r6_t1_mem0 = S.Task('r6_t1_mem0', length=1, delay_cost=1)
	S += r6_t1_mem0 >= 10
	r6_t1_mem0 += MAIN_MEM_r[0]

	r6_t1_mem1 = S.Task('r6_t1_mem1', length=1, delay_cost=1)
	S += r6_t1_mem1 >= 10
	r6_t1_mem1 += MAIN_MEM_r[1]

	r5_t3_in = S.Task('r5_t3_in', length=1, delay_cost=1)
	S += r5_t3_in >= 11
	r5_t3_in += MAS_in[0]

	r5_t3_mem0 = S.Task('r5_t3_mem0', length=1, delay_cost=1)
	S += r5_t3_mem0 >= 11
	r5_t3_mem0 += MAIN_MEM_r[0]

	r5_t3_mem1 = S.Task('r5_t3_mem1', length=1, delay_cost=1)
	S += r5_t3_mem1 >= 11
	r5_t3_mem1 += MAIN_MEM_r[1]

	r6_t1 = S.Task('r6_t1', length=10, delay_cost=1)
	S += r6_t1 >= 11
	r6_t1 += MM[0]

	r4_t3_in = S.Task('r4_t3_in', length=1, delay_cost=1)
	S += r4_t3_in >= 12
	r4_t3_in += MAS_in[0]

	r4_t3_mem0 = S.Task('r4_t3_mem0', length=1, delay_cost=1)
	S += r4_t3_mem0 >= 12
	r4_t3_mem0 += MAIN_MEM_r[0]

	r4_t3_mem1 = S.Task('r4_t3_mem1', length=1, delay_cost=1)
	S += r4_t3_mem1 >= 12
	r4_t3_mem1 += MAIN_MEM_r[1]

	r5_t3 = S.Task('r5_t3', length=4, delay_cost=1)
	S += r5_t3 >= 12
	r5_t3 += MAS[0]

	r4_t3 = S.Task('r4_t3', length=4, delay_cost=1)
	S += r4_t3 >= 13
	r4_t3 += MAS[0]

	r5_t1_in = S.Task('r5_t1_in', length=1, delay_cost=1)
	S += r5_t1_in >= 13
	r5_t1_in += MM_in[0]

	r5_t1_mem0 = S.Task('r5_t1_mem0', length=1, delay_cost=1)
	S += r5_t1_mem0 >= 13
	r5_t1_mem0 += MAIN_MEM_r[0]

	r5_t1_mem1 = S.Task('r5_t1_mem1', length=1, delay_cost=1)
	S += r5_t1_mem1 >= 13
	r5_t1_mem1 += MAIN_MEM_r[1]

	r12_t0_in = S.Task('r12_t0_in', length=1, delay_cost=1)
	S += r12_t0_in >= 14
	r12_t0_in += MM_in[0]

	r12_t0_mem0 = S.Task('r12_t0_mem0', length=1, delay_cost=1)
	S += r12_t0_mem0 >= 14
	r12_t0_mem0 += MAIN_MEM_r[0]

	r12_t0_mem1 = S.Task('r12_t0_mem1', length=1, delay_cost=1)
	S += r12_t0_mem1 >= 14
	r12_t0_mem1 += MAIN_MEM_r[1]

	r5_t1 = S.Task('r5_t1', length=10, delay_cost=1)
	S += r5_t1 >= 14
	r5_t1 += MM[0]

	r12_t0 = S.Task('r12_t0', length=10, delay_cost=1)
	S += r12_t0 >= 15
	r12_t0 += MM[0]

	r6_t3_in = S.Task('r6_t3_in', length=1, delay_cost=1)
	S += r6_t3_in >= 15
	r6_t3_in += MAS_in[0]

	r6_t3_mem0 = S.Task('r6_t3_mem0', length=1, delay_cost=1)
	S += r6_t3_mem0 >= 15
	r6_t3_mem0 += MAIN_MEM_r[0]

	r6_t3_mem1 = S.Task('r6_t3_mem1', length=1, delay_cost=1)
	S += r6_t3_mem1 >= 15
	r6_t3_mem1 += MAIN_MEM_r[1]

	r12_t2_in = S.Task('r12_t2_in', length=1, delay_cost=1)
	S += r12_t2_in >= 16
	r12_t2_in += MAS_in[0]

	r12_t2_mem0 = S.Task('r12_t2_mem0', length=1, delay_cost=1)
	S += r12_t2_mem0 >= 16
	r12_t2_mem0 += MAIN_MEM_r[0]

	r12_t2_mem1 = S.Task('r12_t2_mem1', length=1, delay_cost=1)
	S += r12_t2_mem1 >= 16
	r12_t2_mem1 += MAIN_MEM_r[1]

	r6_t3 = S.Task('r6_t3', length=4, delay_cost=1)
	S += r6_t3 >= 16
	r6_t3 += MAS[0]

	r10_in = S.Task('r10_in', length=1, delay_cost=1)
	S += r10_in >= 17
	r10_in += MAS_in[4]

	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	S += r10_mem0 >= 17
	r10_mem0 += MM_MEM[2]

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	S += r10_mem1 >= 17
	r10_mem1 += MM_MEM[1]

	r12_t1_in = S.Task('r12_t1_in', length=1, delay_cost=1)
	S += r12_t1_in >= 17
	r12_t1_in += MM_in[0]

	r12_t1_mem0 = S.Task('r12_t1_mem0', length=1, delay_cost=1)
	S += r12_t1_mem0 >= 17
	r12_t1_mem0 += MAIN_MEM_r[0]

	r12_t1_mem1 = S.Task('r12_t1_mem1', length=1, delay_cost=1)
	S += r12_t1_mem1 >= 17
	r12_t1_mem1 += MAIN_MEM_r[1]

	r12_t2 = S.Task('r12_t2', length=4, delay_cost=1)
	S += r12_t2 >= 17
	r12_t2 += MAS[0]

	r10 = S.Task('r10', length=4, delay_cost=1)
	S += r10 >= 18
	r10 += MAS[4]

	r12_t1 = S.Task('r12_t1', length=10, delay_cost=1)
	S += r12_t1 >= 18
	r12_t1 += MM[0]

	r12_t3_in = S.Task('r12_t3_in', length=1, delay_cost=1)
	S += r12_t3_in >= 18
	r12_t3_in += MAS_in[0]

	r12_t3_mem0 = S.Task('r12_t3_mem0', length=1, delay_cost=1)
	S += r12_t3_mem0 >= 18
	r12_t3_mem0 += MAIN_MEM_r[0]

	r12_t3_mem1 = S.Task('r12_t3_mem1', length=1, delay_cost=1)
	S += r12_t3_mem1 >= 18
	r12_t3_mem1 += MAIN_MEM_r[1]

	r4_t5_in = S.Task('r4_t5_in', length=1, delay_cost=1)
	S += r4_t5_in >= 18
	r4_t5_in += MAS_in[2]

	r4_t5_mem0 = S.Task('r4_t5_mem0', length=1, delay_cost=1)
	S += r4_t5_mem0 >= 18
	r4_t5_mem0 += MM_MEM[0]

	r4_t5_mem1 = S.Task('r4_t5_mem1', length=1, delay_cost=1)
	S += r4_t5_mem1 >= 18
	r4_t5_mem1 += MM_MEM[1]

	r12_t3 = S.Task('r12_t3', length=4, delay_cost=1)
	S += r12_t3 >= 19
	r12_t3 += MAS[0]

	r13_t0_in = S.Task('r13_t0_in', length=1, delay_cost=1)
	S += r13_t0_in >= 19
	r13_t0_in += MM_in[0]

	r13_t0_mem0 = S.Task('r13_t0_mem0', length=1, delay_cost=1)
	S += r13_t0_mem0 >= 19
	r13_t0_mem0 += MAIN_MEM_r[0]

	r13_t0_mem1 = S.Task('r13_t0_mem1', length=1, delay_cost=1)
	S += r13_t0_mem1 >= 19
	r13_t0_mem1 += MAIN_MEM_r[1]

	r40_in = S.Task('r40_in', length=1, delay_cost=1)
	S += r40_in >= 19
	r40_in += MAS_in[4]

	r40_mem0 = S.Task('r40_mem0', length=1, delay_cost=1)
	S += r40_mem0 >= 19
	r40_mem0 += MM_MEM[0]

	r40_mem1 = S.Task('r40_mem1', length=1, delay_cost=1)
	S += r40_mem1 >= 19
	r40_mem1 += MM_MEM[1]

	r4_t5 = S.Task('r4_t5', length=4, delay_cost=1)
	S += r4_t5 >= 19
	r4_t5 += MAS[2]

	r13_t0 = S.Task('r13_t0', length=10, delay_cost=1)
	S += r13_t0 >= 20
	r13_t0 += MM[0]

	r40 = S.Task('r40', length=4, delay_cost=1)
	S += r40 >= 20
	r40 += MAS[4]

	r6_t2_in = S.Task('r6_t2_in', length=1, delay_cost=1)
	S += r6_t2_in >= 20
	r6_t2_in += MAS_in[0]

	r6_t2_mem0 = S.Task('r6_t2_mem0', length=1, delay_cost=1)
	S += r6_t2_mem0 >= 20
	r6_t2_mem0 += MAIN_MEM_r[0]

	r6_t2_mem1 = S.Task('r6_t2_mem1', length=1, delay_cost=1)
	S += r6_t2_mem1 >= 20
	r6_t2_mem1 += MAIN_MEM_r[1]

	r6_t5_in = S.Task('r6_t5_in', length=1, delay_cost=1)
	S += r6_t5_in >= 20
	r6_t5_in += MAS_in[1]

	r6_t5_mem0 = S.Task('r6_t5_mem0', length=1, delay_cost=1)
	S += r6_t5_mem0 >= 20
	r6_t5_mem0 += MM_MEM[0]

	r6_t5_mem1 = S.Task('r6_t5_mem1', length=1, delay_cost=1)
	S += r6_t5_mem1 >= 20
	r6_t5_mem1 += MM_MEM[1]

	r20_in = S.Task('r20_in', length=1, delay_cost=1)
	S += r20_in >= 21
	r20_in += MAS_in[1]

	r20_mem0 = S.Task('r20_mem0', length=1, delay_cost=1)
	S += r20_mem0 >= 21
	r20_mem0 += MAS_MEM[8]

	r20_mem1 = S.Task('r20_mem1', length=1, delay_cost=1)
	S += r20_mem1 >= 21
	r20_mem1 += MAS_MEM[9]

	r3_t0_in = S.Task('r3_t0_in', length=1, delay_cost=1)
	S += r3_t0_in >= 21
	r3_t0_in += MM_in[0]

	r3_t0_mem0 = S.Task('r3_t0_mem0', length=1, delay_cost=1)
	S += r3_t0_mem0 >= 21
	r3_t0_mem0 += MAIN_MEM_r[0]

	r3_t0_mem1 = S.Task('r3_t0_mem1', length=1, delay_cost=1)
	S += r3_t0_mem1 >= 21
	r3_t0_mem1 += MAIN_MEM_r[1]

	r60_in = S.Task('r60_in', length=1, delay_cost=1)
	S += r60_in >= 21
	r60_in += MAS_in[7]

	r60_mem0 = S.Task('r60_mem0', length=1, delay_cost=1)
	S += r60_mem0 >= 21
	r60_mem0 += MM_MEM[0]

	r60_mem1 = S.Task('r60_mem1', length=1, delay_cost=1)
	S += r60_mem1 >= 21
	r60_mem1 += MM_MEM[1]

	r6_t2 = S.Task('r6_t2', length=4, delay_cost=1)
	S += r6_t2 >= 21
	r6_t2 += MAS[0]

	r6_t5 = S.Task('r6_t5', length=4, delay_cost=1)
	S += r6_t5 >= 21
	r6_t5 += MAS[1]

	r12_t4_in = S.Task('r12_t4_in', length=1, delay_cost=1)
	S += r12_t4_in >= 22
	r12_t4_in += MM_in[1]

	r12_t4_mem0 = S.Task('r12_t4_mem0', length=1, delay_cost=1)
	S += r12_t4_mem0 >= 22
	r12_t4_mem0 += MAS_MEM[0]

	r12_t4_mem1 = S.Task('r12_t4_mem1', length=1, delay_cost=1)
	S += r12_t4_mem1 >= 22
	r12_t4_mem1 += MAS_MEM[1]

	r13_t1_in = S.Task('r13_t1_in', length=1, delay_cost=1)
	S += r13_t1_in >= 22
	r13_t1_in += MM_in[0]

	r13_t1_mem0 = S.Task('r13_t1_mem0', length=1, delay_cost=1)
	S += r13_t1_mem0 >= 22
	r13_t1_mem0 += MAIN_MEM_r[0]

	r13_t1_mem1 = S.Task('r13_t1_mem1', length=1, delay_cost=1)
	S += r13_t1_mem1 >= 22
	r13_t1_mem1 += MAIN_MEM_r[1]

	r1_t5_in = S.Task('r1_t5_in', length=1, delay_cost=1)
	S += r1_t5_in >= 22
	r1_t5_in += MAS_in[6]

	r1_t5_mem0 = S.Task('r1_t5_mem0', length=1, delay_cost=1)
	S += r1_t5_mem0 >= 22
	r1_t5_mem0 += MM_MEM[2]

	r1_t5_mem1 = S.Task('r1_t5_mem1', length=1, delay_cost=1)
	S += r1_t5_mem1 >= 22
	r1_t5_mem1 += MM_MEM[1]

	r20 = S.Task('r20', length=4, delay_cost=1)
	S += r20 >= 22
	r20 += MAS[1]

	r3_t0 = S.Task('r3_t0', length=10, delay_cost=1)
	S += r3_t0 >= 22
	r3_t0 += MM[0]

	r60 = S.Task('r60', length=4, delay_cost=1)
	S += r60 >= 22
	r60 += MAS[7]

	r12_t4 = S.Task('r12_t4', length=10, delay_cost=1)
	S += r12_t4 >= 23
	r12_t4 += MM[1]

	r13_t1 = S.Task('r13_t1', length=10, delay_cost=1)
	S += r13_t1 >= 23
	r13_t1 += MM[0]

	r1_t5 = S.Task('r1_t5', length=4, delay_cost=1)
	S += r1_t5 >= 23
	r1_t5 += MAS[6]

	r50_in = S.Task('r50_in', length=1, delay_cost=1)
	S += r50_in >= 23
	r50_in += MAS_in[5]

	r50_mem0 = S.Task('r50_mem0', length=1, delay_cost=1)
	S += r50_mem0 >= 23
	r50_mem0 += MM_MEM[0]

	r50_mem1 = S.Task('r50_mem1', length=1, delay_cost=1)
	S += r50_mem1 >= 23
	r50_mem1 += MM_MEM[1]

	r5_t2_in = S.Task('r5_t2_in', length=1, delay_cost=1)
	S += r5_t2_in >= 23
	r5_t2_in += MAS_in[0]

	r5_t2_mem0 = S.Task('r5_t2_mem0', length=1, delay_cost=1)
	S += r5_t2_mem0 >= 23
	r5_t2_mem0 += MAIN_MEM_r[0]

	r5_t2_mem1 = S.Task('r5_t2_mem1', length=1, delay_cost=1)
	S += r5_t2_mem1 >= 23
	r5_t2_mem1 += MAIN_MEM_r[1]

	r13_t2_in = S.Task('r13_t2_in', length=1, delay_cost=1)
	S += r13_t2_in >= 24
	r13_t2_in += MAS_in[0]

	r13_t2_mem0 = S.Task('r13_t2_mem0', length=1, delay_cost=1)
	S += r13_t2_mem0 >= 24
	r13_t2_mem0 += MAIN_MEM_r[0]

	r13_t2_mem1 = S.Task('r13_t2_mem1', length=1, delay_cost=1)
	S += r13_t2_mem1 >= 24
	r13_t2_mem1 += MAIN_MEM_r[1]

	r50 = S.Task('r50', length=4, delay_cost=1)
	S += r50 >= 24
	r50 += MAS[5]

	r5_t2 = S.Task('r5_t2', length=4, delay_cost=1)
	S += r5_t2 >= 24
	r5_t2 += MAS[0]

	r5_t5_in = S.Task('r5_t5_in', length=1, delay_cost=1)
	S += r5_t5_in >= 24
	r5_t5_in += MAS_in[3]

	r5_t5_mem0 = S.Task('r5_t5_mem0', length=1, delay_cost=1)
	S += r5_t5_mem0 >= 24
	r5_t5_mem0 += MM_MEM[0]

	r5_t5_mem1 = S.Task('r5_t5_mem1', length=1, delay_cost=1)
	S += r5_t5_mem1 >= 24
	r5_t5_mem1 += MM_MEM[1]

	r6_t4_in = S.Task('r6_t4_in', length=1, delay_cost=1)
	S += r6_t4_in >= 24
	r6_t4_in += MM_in[1]

	r6_t4_mem0 = S.Task('r6_t4_mem0', length=1, delay_cost=1)
	S += r6_t4_mem0 >= 24
	r6_t4_mem0 += MAS_MEM[0]

	r6_t4_mem1 = S.Task('r6_t4_mem1', length=1, delay_cost=1)
	S += r6_t4_mem1 >= 24
	r6_t4_mem1 += MAS_MEM[1]

	r13_t2 = S.Task('r13_t2', length=4, delay_cost=1)
	S += r13_t2 >= 25
	r13_t2 += MAS[0]

	r13_t3_in = S.Task('r13_t3_in', length=1, delay_cost=1)
	S += r13_t3_in >= 25
	r13_t3_in += MAS_in[0]

	r13_t3_mem0 = S.Task('r13_t3_mem0', length=1, delay_cost=1)
	S += r13_t3_mem0 >= 25
	r13_t3_mem0 += MAIN_MEM_r[0]

	r13_t3_mem1 = S.Task('r13_t3_mem1', length=1, delay_cost=1)
	S += r13_t3_mem1 >= 25
	r13_t3_mem1 += MAIN_MEM_r[1]

	r5_t5 = S.Task('r5_t5', length=4, delay_cost=1)
	S += r5_t5 >= 25
	r5_t5 += MAS[3]

	r6_t4 = S.Task('r6_t4', length=10, delay_cost=1)
	S += r6_t4 >= 25
	r6_t4 += MM[1]

	r13_t3 = S.Task('r13_t3', length=4, delay_cost=1)
	S += r13_t3 >= 26
	r13_t3 += MAS[0]

	r4_t2_in = S.Task('r4_t2_in', length=1, delay_cost=1)
	S += r4_t2_in >= 26
	r4_t2_in += MAS_in[0]

	r4_t2_mem0 = S.Task('r4_t2_mem0', length=1, delay_cost=1)
	S += r4_t2_mem0 >= 26
	r4_t2_mem0 += MAIN_MEM_r[0]

	r4_t2_mem1 = S.Task('r4_t2_mem1', length=1, delay_cost=1)
	S += r4_t2_mem1 >= 26
	r4_t2_mem1 += MAIN_MEM_r[1]

	r120_in = S.Task('r120_in', length=1, delay_cost=1)
	S += r120_in >= 27
	r120_in += MAS_in[3]

	r120_mem0 = S.Task('r120_mem0', length=1, delay_cost=1)
	S += r120_mem0 >= 27
	r120_mem0 += MM_MEM[0]

	r120_mem1 = S.Task('r120_mem1', length=1, delay_cost=1)
	S += r120_mem1 >= 27
	r120_mem1 += MM_MEM[1]

	r16_t3_in = S.Task('r16_t3_in', length=1, delay_cost=1)
	S += r16_t3_in >= 27
	r16_t3_in += MAS_in[1]

	r16_t3_mem0 = S.Task('r16_t3_mem0', length=1, delay_cost=1)
	S += r16_t3_mem0 >= 27
	r16_t3_mem0 += MAIN_MEM_r[0]

	r16_t3_mem1 = S.Task('r16_t3_mem1', length=1, delay_cost=1)
	S += r16_t3_mem1 >= 27
	r16_t3_mem1 += MAIN_MEM_r[1]

	r4_t2 = S.Task('r4_t2', length=4, delay_cost=1)
	S += r4_t2 >= 27
	r4_t2 += MAS[0]

	r5_t4_in = S.Task('r5_t4_in', length=1, delay_cost=1)
	S += r5_t4_in >= 27
	r5_t4_in += MM_in[1]

	r5_t4_mem0 = S.Task('r5_t4_mem0', length=1, delay_cost=1)
	S += r5_t4_mem0 >= 27
	r5_t4_mem0 += MAS_MEM[0]

	r5_t4_mem1 = S.Task('r5_t4_mem1', length=1, delay_cost=1)
	S += r5_t4_mem1 >= 27
	r5_t4_mem1 += MAS_MEM[1]

	r70_in = S.Task('r70_in', length=1, delay_cost=1)
	S += r70_in >= 27
	r70_in += MAS_in[0]

	r70_mem0 = S.Task('r70_mem0', length=1, delay_cost=1)
	S += r70_mem0 >= 27
	r70_mem0 += MAS_MEM[10]

	r70_mem1 = S.Task('r70_mem1', length=1, delay_cost=1)
	S += r70_mem1 >= 27
	r70_mem1 += MAS_MEM[15]

	r120 = S.Task('r120', length=4, delay_cost=1)
	S += r120 >= 28
	r120 += MAS[3]

	r12_t5_in = S.Task('r12_t5_in', length=1, delay_cost=1)
	S += r12_t5_in >= 28
	r12_t5_in += MAS_in[1]

	r12_t5_mem0 = S.Task('r12_t5_mem0', length=1, delay_cost=1)
	S += r12_t5_mem0 >= 28
	r12_t5_mem0 += MM_MEM[0]

	r12_t5_mem1 = S.Task('r12_t5_mem1', length=1, delay_cost=1)
	S += r12_t5_mem1 >= 28
	r12_t5_mem1 += MM_MEM[1]

	r16_t3 = S.Task('r16_t3', length=4, delay_cost=1)
	S += r16_t3 >= 28
	r16_t3 += MAS[1]

	r1_t2_in = S.Task('r1_t2_in', length=1, delay_cost=1)
	S += r1_t2_in >= 28
	r1_t2_in += MAS_in[7]

	r1_t2_mem0 = S.Task('r1_t2_mem0', length=1, delay_cost=1)
	S += r1_t2_mem0 >= 28
	r1_t2_mem0 += MAIN_MEM_r[0]

	r1_t2_mem1 = S.Task('r1_t2_mem1', length=1, delay_cost=1)
	S += r1_t2_mem1 >= 28
	r1_t2_mem1 += MAIN_MEM_r[1]

	r5_t4 = S.Task('r5_t4', length=10, delay_cost=1)
	S += r5_t4 >= 28
	r5_t4 += MM[1]

	r70 = S.Task('r70', length=4, delay_cost=1)
	S += r70 >= 28
	r70 += MAS[0]

	r12_t5 = S.Task('r12_t5', length=4, delay_cost=1)
	S += r12_t5 >= 29
	r12_t5 += MAS[1]

	r13_t4_in = S.Task('r13_t4_in', length=1, delay_cost=1)
	S += r13_t4_in >= 29
	r13_t4_in += MM_in[1]

	r13_t4_mem0 = S.Task('r13_t4_mem0', length=1, delay_cost=1)
	S += r13_t4_mem0 >= 29
	r13_t4_mem0 += MAS_MEM[0]

	r13_t4_mem1 = S.Task('r13_t4_mem1', length=1, delay_cost=1)
	S += r13_t4_mem1 >= 29
	r13_t4_mem1 += MAS_MEM[1]

	r1_t2 = S.Task('r1_t2', length=4, delay_cost=1)
	S += r1_t2 >= 29
	r1_t2 += MAS[7]

	r9_t2_in = S.Task('r9_t2_in', length=1, delay_cost=1)
	S += r9_t2_in >= 29
	r9_t2_in += MAS_in[1]

	r9_t2_mem0 = S.Task('r9_t2_mem0', length=1, delay_cost=1)
	S += r9_t2_mem0 >= 29
	r9_t2_mem0 += MAIN_MEM_r[0]

	r9_t2_mem1 = S.Task('r9_t2_mem1', length=1, delay_cost=1)
	S += r9_t2_mem1 >= 29
	r9_t2_mem1 += MAIN_MEM_r[1]

	r100_in = S.Task('r100_in', length=1, delay_cost=1)
	S += r100_in >= 30
	r100_in += MAS_in[5]

	r100_mem0 = S.Task('r100_mem0', length=1, delay_cost=1)
	S += r100_mem0 >= 30
	r100_mem0 += MAIN_MEM_r[0]

	r100_mem1 = S.Task('r100_mem1', length=1, delay_cost=1)
	S += r100_mem1 >= 30
	r100_mem1 += MAS_MEM[9]

	r13_t4 = S.Task('r13_t4', length=10, delay_cost=1)
	S += r13_t4 >= 30
	r13_t4 += MM[1]

	r4_t4_in = S.Task('r4_t4_in', length=1, delay_cost=1)
	S += r4_t4_in >= 30
	r4_t4_in += MM_in[1]

	r4_t4_mem0 = S.Task('r4_t4_mem0', length=1, delay_cost=1)
	S += r4_t4_mem0 >= 30
	r4_t4_mem0 += MAS_MEM[0]

	r4_t4_mem1 = S.Task('r4_t4_mem1', length=1, delay_cost=1)
	S += r4_t4_mem1 >= 30
	r4_t4_mem1 += MAS_MEM[1]

	r9_t2 = S.Task('r9_t2', length=4, delay_cost=1)
	S += r9_t2 >= 30
	r9_t2 += MAS[1]

	X_new_t0_in = S.Task('X_new_t0_in', length=1, delay_cost=1)
	S += X_new_t0_in >= 31
	X_new_t0_in += MM_in[0]

	X_new_t0_mem0 = S.Task('X_new_t0_mem0', length=1, delay_cost=1)
	S += X_new_t0_mem0 >= 31
	X_new_t0_mem0 += MAS_MEM[2]

	X_new_t0_mem1 = S.Task('X_new_t0_mem1', length=1, delay_cost=1)
	S += X_new_t0_mem1 >= 31
	X_new_t0_mem1 += MAS_MEM[7]

	r100 = S.Task('r100', length=4, delay_cost=1)
	S += r100 >= 31
	r100 += MAS[5]

	r3_t5_in = S.Task('r3_t5_in', length=1, delay_cost=1)
	S += r3_t5_in >= 31
	r3_t5_in += MAS_in[2]

	r3_t5_mem0 = S.Task('r3_t5_mem0', length=1, delay_cost=1)
	S += r3_t5_mem0 >= 31
	r3_t5_mem0 += MM_MEM[0]

	r3_t5_mem1 = S.Task('r3_t5_mem1', length=1, delay_cost=1)
	S += r3_t5_mem1 >= 31
	r3_t5_mem1 += MM_MEM[1]

	r4_t4 = S.Task('r4_t4', length=10, delay_cost=1)
	S += r4_t4 >= 31
	r4_t4 += MM[1]

	r9_t0_in = S.Task('r9_t0_in', length=1, delay_cost=1)
	S += r9_t0_in >= 31
	r9_t0_in += MM_in[1]

	r9_t0_mem0 = S.Task('r9_t0_mem0', length=1, delay_cost=1)
	S += r9_t0_mem0 >= 31
	r9_t0_mem0 += MAIN_MEM_r[0]

	r9_t0_mem1 = S.Task('r9_t0_mem1', length=1, delay_cost=1)
	S += r9_t0_mem1 >= 31
	r9_t0_mem1 += MAS_MEM[1]

	X_new_t0 = S.Task('X_new_t0', length=10, delay_cost=1)
	S += X_new_t0 >= 32
	X_new_t0 += MM[0]

	r121_in = S.Task('r121_in', length=1, delay_cost=1)
	S += r121_in >= 32
	r121_in += MAS_in[5]

	r121_mem0 = S.Task('r121_mem0', length=1, delay_cost=1)
	S += r121_mem0 >= 32
	r121_mem0 += MM_MEM[2]

	r121_mem1 = S.Task('r121_mem1', length=1, delay_cost=1)
	S += r121_mem1 >= 32
	r121_mem1 += MAS_MEM[3]

	r130_in = S.Task('r130_in', length=1, delay_cost=1)
	S += r130_in >= 32
	r130_in += MAS_in[6]

	r130_mem0 = S.Task('r130_mem0', length=1, delay_cost=1)
	S += r130_mem0 >= 32
	r130_mem0 += MM_MEM[0]

	r130_mem1 = S.Task('r130_mem1', length=1, delay_cost=1)
	S += r130_mem1 >= 32
	r130_mem1 += MM_MEM[1]

	r1_t4_in = S.Task('r1_t4_in', length=1, delay_cost=1)
	S += r1_t4_in >= 32
	r1_t4_in += MM_in[1]

	r1_t4_mem0 = S.Task('r1_t4_mem0', length=1, delay_cost=1)
	S += r1_t4_mem0 >= 32
	r1_t4_mem0 += MAS_MEM[14]

	r1_t4_mem1 = S.Task('r1_t4_mem1', length=1, delay_cost=1)
	S += r1_t4_mem1 >= 32
	r1_t4_mem1 += MAS_MEM[1]

	r3_t5 = S.Task('r3_t5', length=4, delay_cost=1)
	S += r3_t5 >= 32
	r3_t5 += MAS[2]

	r80_in = S.Task('r80_in', length=1, delay_cost=1)
	S += r80_in >= 32
	r80_in += MAS_in[3]

	r80_mem0 = S.Task('r80_mem0', length=1, delay_cost=1)
	S += r80_mem0 >= 32
	r80_mem0 += MAIN_MEM_r[0]

	r80_mem1 = S.Task('r80_mem1', length=1, delay_cost=1)
	S += r80_mem1 >= 32
	r80_mem1 += MAS_MEM[9]

	r9_t0 = S.Task('r9_t0', length=10, delay_cost=1)
	S += r9_t0 >= 32
	r9_t0 += MM[1]

	r121 = S.Task('r121', length=4, delay_cost=1)
	S += r121 >= 33
	r121 += MAS[5]

	r130 = S.Task('r130', length=4, delay_cost=1)
	S += r130 >= 33
	r130 += MAS[6]

	r1_t4 = S.Task('r1_t4', length=10, delay_cost=1)
	S += r1_t4 >= 33
	r1_t4 += MM[1]

	r30_in = S.Task('r30_in', length=1, delay_cost=1)
	S += r30_in >= 33
	r30_in += MAS_in[6]

	r30_mem0 = S.Task('r30_mem0', length=1, delay_cost=1)
	S += r30_mem0 >= 33
	r30_mem0 += MM_MEM[0]

	r30_mem1 = S.Task('r30_mem1', length=1, delay_cost=1)
	S += r30_mem1 >= 33
	r30_mem1 += MM_MEM[1]

	r80 = S.Task('r80', length=4, delay_cost=1)
	S += r80 >= 33
	r80 += MAS[3]

	r13_t5_in = S.Task('r13_t5_in', length=1, delay_cost=1)
	S += r13_t5_in >= 34
	r13_t5_in += MAS_in[2]

	r13_t5_mem0 = S.Task('r13_t5_mem0', length=1, delay_cost=1)
	S += r13_t5_mem0 >= 34
	r13_t5_mem0 += MM_MEM[0]

	r13_t5_mem1 = S.Task('r13_t5_mem1', length=1, delay_cost=1)
	S += r13_t5_mem1 >= 34
	r13_t5_mem1 += MM_MEM[1]

	r30 = S.Task('r30', length=4, delay_cost=1)
	S += r30 >= 34
	r30 += MAS[6]

	r61_in = S.Task('r61_in', length=1, delay_cost=1)
	S += r61_in >= 34
	r61_in += MAS_in[3]

	r61_mem0 = S.Task('r61_mem0', length=1, delay_cost=1)
	S += r61_mem0 >= 34
	r61_mem0 += MM_MEM[2]

	r61_mem1 = S.Task('r61_mem1', length=1, delay_cost=1)
	S += r61_mem1 >= 34
	r61_mem1 += MAS_MEM[3]

	r13_t5 = S.Task('r13_t5', length=4, delay_cost=1)
	S += r13_t5 >= 35
	r13_t5 += MAS[2]

	r31_in = S.Task('r31_in', length=1, delay_cost=1)
	S += r31_in >= 35
	r31_in += MAS_in[1]

	r31_mem0 = S.Task('r31_mem0', length=1, delay_cost=1)
	S += r31_mem0 >= 35
	r31_mem0 += MM_MEM[0]

	r31_mem1 = S.Task('r31_mem1', length=1, delay_cost=1)
	S += r31_mem1 >= 35
	r31_mem1 += MAS_MEM[5]

	r61 = S.Task('r61', length=4, delay_cost=1)
	S += r61 >= 35
	r61 += MAS[3]

	X_new_t3_in = S.Task('X_new_t3_in', length=1, delay_cost=1)
	S += X_new_t3_in >= 36
	X_new_t3_in += MAS_in[3]

	X_new_t3_mem0 = S.Task('X_new_t3_mem0', length=1, delay_cost=1)
	S += X_new_t3_mem0 >= 36
	X_new_t3_mem0 += MAS_MEM[6]

	X_new_t3_mem1 = S.Task('X_new_t3_mem1', length=1, delay_cost=1)
	S += X_new_t3_mem1 >= 36
	X_new_t3_mem1 += MAS_MEM[11]

	Z_new_t0_in = S.Task('Z_new_t0_in', length=1, delay_cost=1)
	S += Z_new_t0_in >= 36
	Z_new_t0_in += MM_in[1]

	Z_new_t0_mem0 = S.Task('Z_new_t0_mem0', length=1, delay_cost=1)
	S += Z_new_t0_mem0 >= 36
	Z_new_t0_mem0 += MAS_MEM[2]

	Z_new_t0_mem1 = S.Task('Z_new_t0_mem1', length=1, delay_cost=1)
	S += Z_new_t0_mem1 >= 36
	Z_new_t0_mem1 += MAS_MEM[13]

	r31 = S.Task('r31', length=4, delay_cost=1)
	S += r31 >= 36
	r31 += MAS[1]

	X_new_t3 = S.Task('X_new_t3', length=4, delay_cost=1)
	S += X_new_t3 >= 37
	X_new_t3 += MAS[3]

	Z_new_t0 = S.Task('Z_new_t0', length=10, delay_cost=1)
	S += Z_new_t0 >= 37
	Z_new_t0 += MM[1]

	r14_t0_in = S.Task('r14_t0_in', length=1, delay_cost=1)
	S += r14_t0_in >= 37
	r14_t0_in += MM_in[1]

	r14_t0_mem0 = S.Task('r14_t0_mem0', length=1, delay_cost=1)
	S += r14_t0_mem0 >= 37
	r14_t0_mem0 += MAS_MEM[2]

	r14_t0_mem1 = S.Task('r14_t0_mem1', length=1, delay_cost=1)
	S += r14_t0_mem1 >= 37
	r14_t0_mem1 += MAS_MEM[13]

	r51_in = S.Task('r51_in', length=1, delay_cost=1)
	S += r51_in >= 37
	r51_in += MAS_in[3]

	r51_mem0 = S.Task('r51_mem0', length=1, delay_cost=1)
	S += r51_mem0 >= 37
	r51_mem0 += MM_MEM[2]

	r51_mem1 = S.Task('r51_mem1', length=1, delay_cost=1)
	S += r51_mem1 >= 37
	r51_mem1 += MAS_MEM[7]

	r14_t0 = S.Task('r14_t0', length=10, delay_cost=1)
	S += r14_t0 >= 38
	r14_t0 += MM[1]

	r51 = S.Task('r51', length=4, delay_cost=1)
	S += r51 >= 38
	r51 += MAS[3]

	r131_in = S.Task('r131_in', length=1, delay_cost=1)
	S += r131_in >= 39
	r131_in += MAS_in[0]

	r131_mem0 = S.Task('r131_mem0', length=1, delay_cost=1)
	S += r131_mem0 >= 39
	r131_mem0 += MM_MEM[2]

	r131_mem1 = S.Task('r131_mem1', length=1, delay_cost=1)
	S += r131_mem1 >= 39
	r131_mem1 += MAS_MEM[5]

	r14_t3_in = S.Task('r14_t3_in', length=1, delay_cost=1)
	S += r14_t3_in >= 39
	r14_t3_in += MAS_in[3]

	r14_t3_mem0 = S.Task('r14_t3_mem0', length=1, delay_cost=1)
	S += r14_t3_mem0 >= 39
	r14_t3_mem0 += MAS_MEM[12]

	r14_t3_mem1 = S.Task('r14_t3_mem1', length=1, delay_cost=1)
	S += r14_t3_mem1 >= 39
	r14_t3_mem1 += MAS_MEM[3]

	r131 = S.Task('r131', length=4, delay_cost=1)
	S += r131 >= 40
	r131 += MAS[0]

	r14_t3 = S.Task('r14_t3', length=4, delay_cost=1)
	S += r14_t3 >= 40
	r14_t3 += MAS[3]

	r41_in = S.Task('r41_in', length=1, delay_cost=1)
	S += r41_in >= 40
	r41_in += MAS_in[0]

	r41_mem0 = S.Task('r41_mem0', length=1, delay_cost=1)
	S += r41_mem0 >= 40
	r41_mem0 += MM_MEM[2]

	r41_mem1 = S.Task('r41_mem1', length=1, delay_cost=1)
	S += r41_mem1 >= 40
	r41_mem1 += MAS_MEM[5]

	r41 = S.Task('r41', length=4, delay_cost=1)
	S += r41 >= 41
	r41 += MAS[0]

	r71_in = S.Task('r71_in', length=1, delay_cost=1)
	S += r71_in >= 41
	r71_in += MAS_in[5]

	r71_mem0 = S.Task('r71_mem0', length=1, delay_cost=1)
	S += r71_mem0 >= 41
	r71_mem0 += MAS_MEM[6]

	r71_mem1 = S.Task('r71_mem1', length=1, delay_cost=1)
	S += r71_mem1 >= 41
	r71_mem1 += MAS_MEM[7]

	r11_in = S.Task('r11_in', length=1, delay_cost=1)
	S += r11_in >= 42
	r11_in += MAS_in[7]

	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	S += r11_mem0 >= 42
	r11_mem0 += MM_MEM[2]

	r11_mem1 = S.Task('r11_mem1', length=1, delay_cost=1)
	S += r11_mem1 >= 42
	r11_mem1 += MAS_MEM[13]

	r71 = S.Task('r71', length=4, delay_cost=1)
	S += r71 >= 42
	r71 += MAS[5]

	Z_new_t3_in = S.Task('Z_new_t3_in', length=1, delay_cost=1)
	S += Z_new_t3_in >= 43
	Z_new_t3_in += MAS_in[4]

	Z_new_t3_mem0 = S.Task('Z_new_t3_mem0', length=1, delay_cost=1)
	S += Z_new_t3_mem0 >= 43
	Z_new_t3_mem0 += MAS_MEM[12]

	Z_new_t3_mem1 = S.Task('Z_new_t3_mem1', length=1, delay_cost=1)
	S += Z_new_t3_mem1 >= 43
	Z_new_t3_mem1 += MAS_MEM[1]

	r11 = S.Task('r11', length=4, delay_cost=1)
	S += r11 >= 43
	r11 += MAS[7]

	Z_new_t3 = S.Task('Z_new_t3', length=4, delay_cost=1)
	S += Z_new_t3 >= 44
	Z_new_t3 += MAS[4]

	r81_in = S.Task('r81_in', length=1, delay_cost=1)
	S += r81_in >= 44
	r81_in += MAS_in[5]

	r81_mem0 = S.Task('r81_mem0', length=1, delay_cost=1)
	S += r81_mem0 >= 44
	r81_mem0 += MAIN_MEM_r[0]

	r81_mem1 = S.Task('r81_mem1', length=1, delay_cost=1)
	S += r81_mem1 >= 44
	r81_mem1 += MAS_MEM[1]

	r101_in = S.Task('r101_in', length=1, delay_cost=1)
	S += r101_in >= 45
	r101_in += MAS_in[5]

	r101_mem0 = S.Task('r101_mem0', length=1, delay_cost=1)
	S += r101_mem0 >= 45
	r101_mem0 += MAIN_MEM_r[0]

	r101_mem1 = S.Task('r101_mem1', length=1, delay_cost=1)
	S += r101_mem1 >= 45
	r101_mem1 += MAS_MEM[1]

	r81 = S.Task('r81', length=4, delay_cost=1)
	S += r81 >= 45
	r81 += MAS[5]

	r9_t3_in = S.Task('r9_t3_in', length=1, delay_cost=1)
	S += r9_t3_in >= 45
	r9_t3_in += MAS_in[7]

	r9_t3_mem0 = S.Task('r9_t3_mem0', length=1, delay_cost=1)
	S += r9_t3_mem0 >= 45
	r9_t3_mem0 += MAS_MEM[0]

	r9_t3_mem1 = S.Task('r9_t3_mem1', length=1, delay_cost=1)
	S += r9_t3_mem1 >= 45
	r9_t3_mem1 += MAS_MEM[11]

	r101 = S.Task('r101', length=4, delay_cost=1)
	S += r101 >= 46
	r101 += MAS[5]

	r21_in = S.Task('r21_in', length=1, delay_cost=1)
	S += r21_in >= 46
	r21_in += MAS_in[5]

	r21_mem0 = S.Task('r21_mem0', length=1, delay_cost=1)
	S += r21_mem0 >= 46
	r21_mem0 += MAS_MEM[14]

	r21_mem1 = S.Task('r21_mem1', length=1, delay_cost=1)
	S += r21_mem1 >= 46
	r21_mem1 += MAS_MEM[15]

	r9_t1_in = S.Task('r9_t1_in', length=1, delay_cost=1)
	S += r9_t1_in >= 46
	r9_t1_in += MM_in[0]

	r9_t1_mem0 = S.Task('r9_t1_mem0', length=1, delay_cost=1)
	S += r9_t1_mem0 >= 46
	r9_t1_mem0 += MAIN_MEM_r[0]

	r9_t1_mem1 = S.Task('r9_t1_mem1', length=1, delay_cost=1)
	S += r9_t1_mem1 >= 46
	r9_t1_mem1 += MAS_MEM[11]

	r9_t3 = S.Task('r9_t3', length=4, delay_cost=1)
	S += r9_t3 >= 46
	r9_t3 += MAS[7]

	r21 = S.Task('r21', length=4, delay_cost=1)
	S += r21 >= 47
	r21 += MAS[5]

	r9_t1 = S.Task('r9_t1', length=10, delay_cost=1)
	S += r9_t1 >= 47
	r9_t1 += MM[0]

	r15_t2_in = S.Task('r15_t2_in', length=1, delay_cost=1)
	S += r15_t2_in >= 48
	r15_t2_in += MAS_in[1]

	r15_t2_mem0 = S.Task('r15_t2_mem0', length=1, delay_cost=1)
	S += r15_t2_mem0 >= 48
	r15_t2_mem0 += MAS_MEM[6]

	r15_t2_mem1 = S.Task('r15_t2_mem1', length=1, delay_cost=1)
	S += r15_t2_mem1 >= 48
	r15_t2_mem1 += MAS_MEM[11]

	r11_t3_in = S.Task('r11_t3_in', length=1, delay_cost=1)
	S += r11_t3_in >= 49
	r11_t3_in += MM_in[1]

	r11_t3_mem0 = S.Task('r11_t3_mem0', length=1, delay_cost=1)
	S += r11_t3_mem0 >= 49
	r11_t3_mem0 += MAS_MEM[10]

	r11_t3_mem1 = S.Task('r11_t3_mem1', length=1, delay_cost=1)
	S += r11_t3_mem1 >= 49
	r11_t3_mem1 += MAS_MEM[11]

	r15_t2 = S.Task('r15_t2', length=4, delay_cost=1)
	S += r15_t2 >= 49
	r15_t2 += MAS[1]

	r9_t4_in = S.Task('r9_t4_in', length=1, delay_cost=1)
	S += r9_t4_in >= 49
	r9_t4_in += MM_in[0]

	r9_t4_mem0 = S.Task('r9_t4_mem0', length=1, delay_cost=1)
	S += r9_t4_mem0 >= 49
	r9_t4_mem0 += MAS_MEM[2]

	r9_t4_mem1 = S.Task('r9_t4_mem1', length=1, delay_cost=1)
	S += r9_t4_mem1 >= 49
	r9_t4_mem1 += MAS_MEM[15]

	Z_new_t1_in = S.Task('Z_new_t1_in', length=1, delay_cost=1)
	S += Z_new_t1_in >= 50
	Z_new_t1_in += MM_in[1]

	Z_new_t1_mem0 = S.Task('Z_new_t1_mem0', length=1, delay_cost=1)
	S += Z_new_t1_mem0 >= 50
	Z_new_t1_mem0 += MAS_MEM[10]

	Z_new_t1_mem1 = S.Task('Z_new_t1_mem1', length=1, delay_cost=1)
	S += Z_new_t1_mem1 >= 50
	Z_new_t1_mem1 += MAS_MEM[1]

	Z_new_t2_in = S.Task('Z_new_t2_in', length=1, delay_cost=1)
	S += Z_new_t2_in >= 50
	Z_new_t2_in += MAS_in[3]

	Z_new_t2_mem0 = S.Task('Z_new_t2_mem0', length=1, delay_cost=1)
	S += Z_new_t2_mem0 >= 50
	Z_new_t2_mem0 += MAS_MEM[2]

	Z_new_t2_mem1 = S.Task('Z_new_t2_mem1', length=1, delay_cost=1)
	S += Z_new_t2_mem1 >= 50
	Z_new_t2_mem1 += MAS_MEM[11]

	r11_t3 = S.Task('r11_t3', length=10, delay_cost=1)
	S += r11_t3 >= 50
	r11_t3 += MM[1]

	r9_t4 = S.Task('r9_t4', length=10, delay_cost=1)
	S += r9_t4 >= 50
	r9_t4 += MM[0]

	Z_new_t1 = S.Task('Z_new_t1', length=10, delay_cost=1)
	S += Z_new_t1 >= 51
	Z_new_t1 += MM[1]

	Z_new_t2 = S.Task('Z_new_t2', length=4, delay_cost=1)
	S += Z_new_t2 >= 51
	Z_new_t2 += MAS[3]

	r11_t1_in = S.Task('r11_t1_in', length=1, delay_cost=1)
	S += r11_t1_in >= 51
	r11_t1_in += MAS_in[5]

	r11_t1_mem0 = S.Task('r11_t1_mem0', length=1, delay_cost=1)
	S += r11_t1_mem0 >= 51
	r11_t1_mem0 += MAS_MEM[10]

	r11_t1_mem1 = S.Task('r11_t1_mem1', length=1, delay_cost=1)
	S += r11_t1_mem1 >= 51
	r11_t1_mem1 += MAS_MEM[11]

	r11_t0_in = S.Task('r11_t0_in', length=1, delay_cost=1)
	S += r11_t0_in >= 52
	r11_t0_in += MAS_in[0]

	r11_t0_mem0 = S.Task('r11_t0_mem0', length=1, delay_cost=1)
	S += r11_t0_mem0 >= 52
	r11_t0_mem0 += MAS_MEM[10]

	r11_t0_mem1 = S.Task('r11_t0_mem1', length=1, delay_cost=1)
	S += r11_t0_mem1 >= 52
	r11_t0_mem1 += MAS_MEM[11]

	r11_t1 = S.Task('r11_t1', length=4, delay_cost=1)
	S += r11_t1 >= 52
	r11_t1 += MAS[5]

	r11_t0 = S.Task('r11_t0', length=4, delay_cost=1)
	S += r11_t0 >= 53
	r11_t0 += MAS[0]

	r14_t1_in = S.Task('r14_t1_in', length=1, delay_cost=1)
	S += r14_t1_in >= 53
	r14_t1_in += MM_in[1]

	r14_t1_mem0 = S.Task('r14_t1_mem0', length=1, delay_cost=1)
	S += r14_t1_mem0 >= 53
	r14_t1_mem0 += MAS_MEM[10]

	r14_t1_mem1 = S.Task('r14_t1_mem1', length=1, delay_cost=1)
	S += r14_t1_mem1 >= 53
	r14_t1_mem1 += MAS_MEM[3]

	r14_t2_in = S.Task('r14_t2_in', length=1, delay_cost=1)
	S += r14_t2_in >= 53
	r14_t2_in += MAS_in[6]

	r14_t2_mem0 = S.Task('r14_t2_mem0', length=1, delay_cost=1)
	S += r14_t2_mem0 >= 53
	r14_t2_mem0 += MAS_MEM[2]

	r14_t2_mem1 = S.Task('r14_t2_mem1', length=1, delay_cost=1)
	S += r14_t2_mem1 >= 53
	r14_t2_mem1 += MAS_MEM[11]

	X_new_t1_in = S.Task('X_new_t1_in', length=1, delay_cost=1)
	S += X_new_t1_in >= 54
	X_new_t1_in += MM_in[0]

	X_new_t1_mem0 = S.Task('X_new_t1_mem0', length=1, delay_cost=1)
	S += X_new_t1_mem0 >= 54
	X_new_t1_mem0 += MAS_MEM[10]

	X_new_t1_mem1 = S.Task('X_new_t1_mem1', length=1, delay_cost=1)
	S += X_new_t1_mem1 >= 54
	X_new_t1_mem1 += MAS_MEM[11]

	Z_new_t4_in = S.Task('Z_new_t4_in', length=1, delay_cost=1)
	S += Z_new_t4_in >= 54
	Z_new_t4_in += MM_in[1]

	Z_new_t4_mem0 = S.Task('Z_new_t4_mem0', length=1, delay_cost=1)
	S += Z_new_t4_mem0 >= 54
	Z_new_t4_mem0 += MAS_MEM[6]

	Z_new_t4_mem1 = S.Task('Z_new_t4_mem1', length=1, delay_cost=1)
	S += Z_new_t4_mem1 >= 54
	Z_new_t4_mem1 += MAS_MEM[9]

	r14_t1 = S.Task('r14_t1', length=10, delay_cost=1)
	S += r14_t1 >= 54
	r14_t1 += MM[1]

	r14_t2 = S.Task('r14_t2', length=4, delay_cost=1)
	S += r14_t2 >= 54
	r14_t2 += MAS[6]

	X_new_t1 = S.Task('X_new_t1', length=10, delay_cost=1)
	S += X_new_t1 >= 55
	X_new_t1 += MM[0]

	X_new_t2_in = S.Task('X_new_t2_in', length=1, delay_cost=1)
	S += X_new_t2_in >= 55
	X_new_t2_in += MAS_in[7]

	X_new_t2_mem0 = S.Task('X_new_t2_mem0', length=1, delay_cost=1)
	S += X_new_t2_mem0 >= 55
	X_new_t2_mem0 += MAS_MEM[2]

	X_new_t2_mem1 = S.Task('X_new_t2_mem1', length=1, delay_cost=1)
	S += X_new_t2_mem1 >= 55
	X_new_t2_mem1 += MAS_MEM[11]

	Z_new_t4 = S.Task('Z_new_t4', length=10, delay_cost=1)
	S += Z_new_t4 >= 55
	Z_new_t4 += MM[1]

	X_new_t2 = S.Task('X_new_t2', length=4, delay_cost=1)
	S += X_new_t2 >= 56
	X_new_t2 += MAS[7]

	r11_t2_in = S.Task('r11_t2_in', length=1, delay_cost=1)
	S += r11_t2_in >= 56
	r11_t2_in += MM_in[1]

	r11_t2_mem0 = S.Task('r11_t2_mem0', length=1, delay_cost=1)
	S += r11_t2_mem0 >= 56
	r11_t2_mem0 += MAS_MEM[0]

	r11_t2_mem1 = S.Task('r11_t2_mem1', length=1, delay_cost=1)
	S += r11_t2_mem1 >= 56
	r11_t2_mem1 += MAS_MEM[11]

	r9_t5_in = S.Task('r9_t5_in', length=1, delay_cost=1)
	S += r9_t5_in >= 56
	r9_t5_in += MAS_in[0]

	r9_t5_mem0 = S.Task('r9_t5_mem0', length=1, delay_cost=1)
	S += r9_t5_mem0 >= 56
	r9_t5_mem0 += MM_MEM[2]

	r9_t5_mem1 = S.Task('r9_t5_mem1', length=1, delay_cost=1)
	S += r9_t5_mem1 >= 56
	r9_t5_mem1 += MM_MEM[1]

	r11_t2 = S.Task('r11_t2', length=10, delay_cost=1)
	S += r11_t2 >= 57
	r11_t2 += MM[1]

	r14_t4_in = S.Task('r14_t4_in', length=1, delay_cost=1)
	S += r14_t4_in >= 57
	r14_t4_in += MM_in[0]

	r14_t4_mem0 = S.Task('r14_t4_mem0', length=1, delay_cost=1)
	S += r14_t4_mem0 >= 57
	r14_t4_mem0 += MAS_MEM[12]

	r14_t4_mem1 = S.Task('r14_t4_mem1', length=1, delay_cost=1)
	S += r14_t4_mem1 >= 57
	r14_t4_mem1 += MAS_MEM[7]

	r90_in = S.Task('r90_in', length=1, delay_cost=1)
	S += r90_in >= 57
	r90_in += MAS_in[1]

	r90_mem0 = S.Task('r90_mem0', length=1, delay_cost=1)
	S += r90_mem0 >= 57
	r90_mem0 += MM_MEM[2]

	r90_mem1 = S.Task('r90_mem1', length=1, delay_cost=1)
	S += r90_mem1 >= 57
	r90_mem1 += MM_MEM[1]

	r9_t5 = S.Task('r9_t5', length=4, delay_cost=1)
	S += r9_t5 >= 57
	r9_t5 += MAS[0]

	r14_t4 = S.Task('r14_t4', length=10, delay_cost=1)
	S += r14_t4 >= 58
	r14_t4 += MM[0]

	r90 = S.Task('r90', length=4, delay_cost=1)
	S += r90 >= 58
	r90 += MAS[1]

	X_new_t4_in = S.Task('X_new_t4_in', length=1, delay_cost=1)
	S += X_new_t4_in >= 59
	X_new_t4_in += MM_in[1]

	X_new_t4_mem0 = S.Task('X_new_t4_mem0', length=1, delay_cost=1)
	S += X_new_t4_mem0 >= 59
	X_new_t4_mem0 += MAS_MEM[14]

	X_new_t4_mem1 = S.Task('X_new_t4_mem1', length=1, delay_cost=1)
	S += X_new_t4_mem1 >= 59
	X_new_t4_mem1 += MAS_MEM[7]

	r111_in = S.Task('r111_in', length=1, delay_cost=1)
	S += r111_in >= 59
	r111_in += MAS_in[2]

	r111_mem0 = S.Task('r111_mem0', length=1, delay_cost=1)
	S += r111_mem0 >= 59
	r111_mem0 += MM_MEM[2]

	r111_mem1 = S.Task('r111_mem1', length=1, delay_cost=1)
	S += r111_mem1 >= 59
	r111_mem1 += MM_MEM[3]

	X_new_t4 = S.Task('X_new_t4', length=10, delay_cost=1)
	S += X_new_t4 >= 60
	X_new_t4 += MM[1]

	r111 = S.Task('r111', length=4, delay_cost=1)
	S += r111 >= 60
	r111 += MAS[2]

	r91_in = S.Task('r91_in', length=1, delay_cost=1)
	S += r91_in >= 60
	r91_in += MAS_in[2]

	r91_mem0 = S.Task('r91_mem0', length=1, delay_cost=1)
	S += r91_mem0 >= 60
	r91_mem0 += MM_MEM[0]

	r91_mem1 = S.Task('r91_mem1', length=1, delay_cost=1)
	S += r91_mem1 >= 60
	r91_mem1 += MAS_MEM[1]

	Z_new_t5_in = S.Task('Z_new_t5_in', length=1, delay_cost=1)
	S += Z_new_t5_in >= 61
	Z_new_t5_in += MAS_in[6]

	Z_new_t5_mem0 = S.Task('Z_new_t5_mem0', length=1, delay_cost=1)
	S += Z_new_t5_mem0 >= 61
	Z_new_t5_mem0 += MM_MEM[2]

	Z_new_t5_mem1 = S.Task('Z_new_t5_mem1', length=1, delay_cost=1)
	S += Z_new_t5_mem1 >= 61
	Z_new_t5_mem1 += MM_MEM[3]

	r15_t0_in = S.Task('r15_t0_in', length=1, delay_cost=1)
	S += r15_t0_in >= 61
	r15_t0_in += MM_in[0]

	r15_t0_mem0 = S.Task('r15_t0_mem0', length=1, delay_cost=1)
	S += r15_t0_mem0 >= 61
	r15_t0_mem0 += MAS_MEM[6]

	r15_t0_mem1 = S.Task('r15_t0_mem1', length=1, delay_cost=1)
	S += r15_t0_mem1 >= 61
	r15_t0_mem1 += MAS_MEM[3]

	r91 = S.Task('r91', length=4, delay_cost=1)
	S += r91 >= 61
	r91 += MAS[2]

	Z_new_t5 = S.Task('Z_new_t5', length=4, delay_cost=1)
	S += Z_new_t5 >= 62
	Z_new_t5 += MAS[6]

	r15_t0 = S.Task('r15_t0', length=10, delay_cost=1)
	S += r15_t0 >= 62
	r15_t0 += MM[0]

	r14_t5_in = S.Task('r14_t5_in', length=1, delay_cost=1)
	S += r14_t5_in >= 63
	r14_t5_in += MAS_in[2]

	r14_t5_mem0 = S.Task('r14_t5_mem0', length=1, delay_cost=1)
	S += r14_t5_mem0 >= 63
	r14_t5_mem0 += MM_MEM[2]

	r14_t5_mem1 = S.Task('r14_t5_mem1', length=1, delay_cost=1)
	S += r14_t5_mem1 >= 63
	r14_t5_mem1 += MM_MEM[3]

	r16_t1_in = S.Task('r16_t1_in', length=1, delay_cost=1)
	S += r16_t1_in >= 63
	r16_t1_in += MM_in[0]

	r16_t1_mem0 = S.Task('r16_t1_mem0', length=1, delay_cost=1)
	S += r16_t1_mem0 >= 63
	r16_t1_mem0 += MAS_MEM[4]

	r16_t1_mem1 = S.Task('r16_t1_mem1', length=1, delay_cost=1)
	S += r16_t1_mem1 >= 63
	r16_t1_mem1 += MAIN_MEM_r[1]

	X_new0_in = S.Task('X_new0_in', length=1, delay_cost=1)
	S += X_new0_in >= 64
	X_new0_in += MAS_in[5]

	X_new0_mem0 = S.Task('X_new0_mem0', length=1, delay_cost=1)
	S += X_new0_mem0 >= 64
	X_new0_mem0 += MM_MEM[0]

	X_new0_mem1 = S.Task('X_new0_mem1', length=1, delay_cost=1)
	S += X_new0_mem1 >= 64
	X_new0_mem1 += MM_MEM[1]

	r140_in = S.Task('r140_in', length=1, delay_cost=1)
	S += r140_in >= 64
	r140_in += MAS_in[3]

	r140_mem0 = S.Task('r140_mem0', length=1, delay_cost=1)
	S += r140_mem0 >= 64
	r140_mem0 += MM_MEM[2]

	r140_mem1 = S.Task('r140_mem1', length=1, delay_cost=1)
	S += r140_mem1 >= 64
	r140_mem1 += MM_MEM[3]

	r14_t5 = S.Task('r14_t5', length=4, delay_cost=1)
	S += r14_t5 >= 64
	r14_t5 += MAS[2]

	r15_t1_in = S.Task('r15_t1_in', length=1, delay_cost=1)
	S += r15_t1_in >= 64
	r15_t1_in += MM_in[0]

	r15_t1_mem0 = S.Task('r15_t1_mem0', length=1, delay_cost=1)
	S += r15_t1_mem0 >= 64
	r15_t1_mem0 += MAS_MEM[10]

	r15_t1_mem1 = S.Task('r15_t1_mem1', length=1, delay_cost=1)
	S += r15_t1_mem1 >= 64
	r15_t1_mem1 += MAS_MEM[5]

	r16_t1 = S.Task('r16_t1', length=10, delay_cost=1)
	S += r16_t1 >= 64
	r16_t1 += MM[0]

	X_new0 = S.Task('X_new0', length=4, delay_cost=1)
	S += X_new0 >= 65
	X_new0 += MAS[5]

	X_new_t5_in = S.Task('X_new_t5_in', length=1, delay_cost=1)
	S += X_new_t5_in >= 65
	X_new_t5_in += MAS_in[5]

	X_new_t5_mem0 = S.Task('X_new_t5_mem0', length=1, delay_cost=1)
	S += X_new_t5_mem0 >= 65
	X_new_t5_mem0 += MM_MEM[0]

	X_new_t5_mem1 = S.Task('X_new_t5_mem1', length=1, delay_cost=1)
	S += X_new_t5_mem1 >= 65
	X_new_t5_mem1 += MM_MEM[1]

	Z_new1_in = S.Task('Z_new1_in', length=1, delay_cost=1)
	S += Z_new1_in >= 65
	Z_new1_in += MAS_in[2]

	Z_new1_mem0 = S.Task('Z_new1_mem0', length=1, delay_cost=1)
	S += Z_new1_mem0 >= 65
	Z_new1_mem0 += MM_MEM[2]

	Z_new1_mem1 = S.Task('Z_new1_mem1', length=1, delay_cost=1)
	S += Z_new1_mem1 >= 65
	Z_new1_mem1 += MAS_MEM[13]

	r140 = S.Task('r140', length=4, delay_cost=1)
	S += r140 >= 65
	r140 += MAS[3]

	r15_t1 = S.Task('r15_t1', length=10, delay_cost=1)
	S += r15_t1 >= 65
	r15_t1 += MM[0]

	r15_t3_in = S.Task('r15_t3_in', length=1, delay_cost=1)
	S += r15_t3_in >= 65
	r15_t3_in += MAS_in[6]

	r15_t3_mem0 = S.Task('r15_t3_mem0', length=1, delay_cost=1)
	S += r15_t3_mem0 >= 65
	r15_t3_mem0 += MAS_MEM[2]

	r15_t3_mem1 = S.Task('r15_t3_mem1', length=1, delay_cost=1)
	S += r15_t3_mem1 >= 65
	r15_t3_mem1 += MAS_MEM[5]

	X_new_t5 = S.Task('X_new_t5', length=4, delay_cost=1)
	S += X_new_t5 >= 66
	X_new_t5 += MAS[5]

	Z_new1 = S.Task('Z_new1', length=4, delay_cost=1)
	S += Z_new1 >= 66
	Z_new1 += MAS[2]

	r15_t3 = S.Task('r15_t3', length=4, delay_cost=1)
	S += r15_t3 >= 66
	r15_t3 += MAS[6]

	r141_in = S.Task('r141_in', length=1, delay_cost=1)
	S += r141_in >= 67
	r141_in += MAS_in[0]

	r141_mem0 = S.Task('r141_mem0', length=1, delay_cost=1)
	S += r141_mem0 >= 67
	r141_mem0 += MM_MEM[0]

	r141_mem1 = S.Task('r141_mem1', length=1, delay_cost=1)
	S += r141_mem1 >= 67
	r141_mem1 += MAS_MEM[5]

	r141 = S.Task('r141', length=4, delay_cost=1)
	S += r141 >= 68
	r141 += MAS[0]

	X_new0_w = S.Task('X_new0_w', length=1, delay_cost=1)
	S += X_new0_w >= 69
	X_new0_w += MAIN_MEM_w

	X_new1_in = S.Task('X_new1_in', length=1, delay_cost=1)
	S += X_new1_in >= 69
	X_new1_in += MAS_in[6]

	X_new1_mem0 = S.Task('X_new1_mem0', length=1, delay_cost=1)
	S += X_new1_mem0 >= 69
	X_new1_mem0 += MM_MEM[2]

	X_new1_mem1 = S.Task('X_new1_mem1', length=1, delay_cost=1)
	S += X_new1_mem1 >= 69
	X_new1_mem1 += MAS_MEM[11]

	r15_t4_in = S.Task('r15_t4_in', length=1, delay_cost=1)
	S += r15_t4_in >= 69
	r15_t4_in += MM_in[0]

	r15_t4_mem0 = S.Task('r15_t4_mem0', length=1, delay_cost=1)
	S += r15_t4_mem0 >= 69
	r15_t4_mem0 += MAS_MEM[2]

	r15_t4_mem1 = S.Task('r15_t4_mem1', length=1, delay_cost=1)
	S += r15_t4_mem1 >= 69
	r15_t4_mem1 += MAS_MEM[13]

	X_new1 = S.Task('X_new1', length=4, delay_cost=1)
	S += X_new1 >= 70
	X_new1 += MAS[6]

	Z_new1_w = S.Task('Z_new1_w', length=1, delay_cost=1)
	S += Z_new1_w >= 70
	Z_new1_w += MAIN_MEM_w

	r15_t4 = S.Task('r15_t4', length=10, delay_cost=1)
	S += r15_t4 >= 70
	r15_t4 += MM[0]

	r16_t0_in = S.Task('r16_t0_in', length=1, delay_cost=1)
	S += r16_t0_in >= 70
	r16_t0_in += MM_in[0]

	r16_t0_mem0 = S.Task('r16_t0_mem0', length=1, delay_cost=1)
	S += r16_t0_mem0 >= 70
	r16_t0_mem0 += MAS_MEM[2]

	r16_t0_mem1 = S.Task('r16_t0_mem1', length=1, delay_cost=1)
	S += r16_t0_mem1 >= 70
	r16_t0_mem1 += MAIN_MEM_r[1]

	r16_t0 = S.Task('r16_t0', length=10, delay_cost=1)
	S += r16_t0 >= 71
	r16_t0 += MM[0]

	r16_t2_in = S.Task('r16_t2_in', length=1, delay_cost=1)
	S += r16_t2_in >= 71
	r16_t2_in += MAS_in[1]

	r16_t2_mem0 = S.Task('r16_t2_mem0', length=1, delay_cost=1)
	S += r16_t2_mem0 >= 71
	r16_t2_mem0 += MAS_MEM[2]

	r16_t2_mem1 = S.Task('r16_t2_mem1', length=1, delay_cost=1)
	S += r16_t2_mem1 >= 71
	r16_t2_mem1 += MAS_MEM[5]

	r16_t2 = S.Task('r16_t2', length=4, delay_cost=1)
	S += r16_t2 >= 72
	r16_t2 += MAS[1]

	X_new1_w = S.Task('X_new1_w', length=1, delay_cost=1)
	S += X_new1_w >= 74
	X_new1_w += MAIN_MEM_w

	r150_in = S.Task('r150_in', length=1, delay_cost=1)
	S += r150_in >= 74
	r150_in += MAS_in[3]

	r150_mem0 = S.Task('r150_mem0', length=1, delay_cost=1)
	S += r150_mem0 >= 74
	r150_mem0 += MM_MEM[0]

	r150_mem1 = S.Task('r150_mem1', length=1, delay_cost=1)
	S += r150_mem1 >= 74
	r150_mem1 += MM_MEM[1]

	r150 = S.Task('r150', length=4, delay_cost=1)
	S += r150 >= 75
	r150 += MAS[3]

	r15_t5_in = S.Task('r15_t5_in', length=1, delay_cost=1)
	S += r15_t5_in >= 75
	r15_t5_in += MAS_in[4]

	r15_t5_mem0 = S.Task('r15_t5_mem0', length=1, delay_cost=1)
	S += r15_t5_mem0 >= 75
	r15_t5_mem0 += MM_MEM[0]

	r15_t5_mem1 = S.Task('r15_t5_mem1', length=1, delay_cost=1)
	S += r15_t5_mem1 >= 75
	r15_t5_mem1 += MM_MEM[1]

	r16_t4_in = S.Task('r16_t4_in', length=1, delay_cost=1)
	S += r16_t4_in >= 75
	r16_t4_in += MM_in[1]

	r16_t4_mem0 = S.Task('r16_t4_mem0', length=1, delay_cost=1)
	S += r16_t4_mem0 >= 75
	r16_t4_mem0 += MAS_MEM[2]

	r16_t4_mem1 = S.Task('r16_t4_mem1', length=1, delay_cost=1)
	S += r16_t4_mem1 >= 75
	r16_t4_mem1 += MAS_MEM[3]

	r15_t5 = S.Task('r15_t5', length=4, delay_cost=1)
	S += r15_t5 >= 76
	r15_t5 += MAS[4]

	r16_t4 = S.Task('r16_t4', length=10, delay_cost=1)
	S += r16_t4 >= 76
	r16_t4 += MM[1]

	r170_in = S.Task('r170_in', length=1, delay_cost=1)
	S += r170_in >= 78
	r170_in += MAS_in[6]

	r170_mem0 = S.Task('r170_mem0', length=1, delay_cost=1)
	S += r170_mem0 >= 78
	r170_mem0 += MAS_MEM[6]

	r170_mem1 = S.Task('r170_mem1', length=1, delay_cost=1)
	S += r170_mem1 >= 78
	r170_mem1 += MAS_MEM[7]

	r151_in = S.Task('r151_in', length=1, delay_cost=1)
	S += r151_in >= 79
	r151_in += MAS_in[4]

	r151_mem0 = S.Task('r151_mem0', length=1, delay_cost=1)
	S += r151_mem0 >= 79
	r151_mem0 += MM_MEM[0]

	r151_mem1 = S.Task('r151_mem1', length=1, delay_cost=1)
	S += r151_mem1 >= 79
	r151_mem1 += MAS_MEM[9]

	r170 = S.Task('r170', length=4, delay_cost=1)
	S += r170 >= 79
	r170 += MAS[6]

	r151 = S.Task('r151', length=4, delay_cost=1)
	S += r151 >= 80
	r151 += MAS[4]

	r160_in = S.Task('r160_in', length=1, delay_cost=1)
	S += r160_in >= 80
	r160_in += MAS_in[3]

	r160_mem0 = S.Task('r160_mem0', length=1, delay_cost=1)
	S += r160_mem0 >= 80
	r160_mem0 += MM_MEM[0]

	r160_mem1 = S.Task('r160_mem1', length=1, delay_cost=1)
	S += r160_mem1 >= 80
	r160_mem1 += MM_MEM[1]

	r160 = S.Task('r160', length=4, delay_cost=1)
	S += r160 >= 81
	r160 += MAS[3]

	r16_t5_in = S.Task('r16_t5_in', length=1, delay_cost=1)
	S += r16_t5_in >= 81
	r16_t5_in += MAS_in[7]

	r16_t5_mem0 = S.Task('r16_t5_mem0', length=1, delay_cost=1)
	S += r16_t5_mem0 >= 81
	r16_t5_mem0 += MM_MEM[0]

	r16_t5_mem1 = S.Task('r16_t5_mem1', length=1, delay_cost=1)
	S += r16_t5_mem1 >= 81
	r16_t5_mem1 += MM_MEM[1]

	r16_t5 = S.Task('r16_t5', length=4, delay_cost=1)
	S += r16_t5 >= 82
	r16_t5 += MAS[7]

	r171_in = S.Task('r171_in', length=1, delay_cost=1)
	S += r171_in >= 83
	r171_in += MAS_in[7]

	r171_mem0 = S.Task('r171_mem0', length=1, delay_cost=1)
	S += r171_mem0 >= 83
	r171_mem0 += MAS_MEM[0]

	r171_mem1 = S.Task('r171_mem1', length=1, delay_cost=1)
	S += r171_mem1 >= 83
	r171_mem1 += MAS_MEM[9]

	Y_new0_in = S.Task('Y_new0_in', length=1, delay_cost=1)
	S += Y_new0_in >= 84
	Y_new0_in += MAS_in[1]

	Y_new0_mem0 = S.Task('Y_new0_mem0', length=1, delay_cost=1)
	S += Y_new0_mem0 >= 84
	Y_new0_mem0 += MAS_MEM[12]

	Y_new0_mem1 = S.Task('Y_new0_mem1', length=1, delay_cost=1)
	S += Y_new0_mem1 >= 84
	Y_new0_mem1 += MAS_MEM[7]

	r171 = S.Task('r171', length=4, delay_cost=1)
	S += r171 >= 84
	r171 += MAS[7]

	Y_new0 = S.Task('Y_new0', length=4, delay_cost=1)
	S += Y_new0 >= 85
	Y_new0 += MAS[1]

	r161_in = S.Task('r161_in', length=1, delay_cost=1)
	S += r161_in >= 85
	r161_in += MAS_in[7]

	r161_mem0 = S.Task('r161_mem0', length=1, delay_cost=1)
	S += r161_mem0 >= 85
	r161_mem0 += MM_MEM[2]

	r161_mem1 = S.Task('r161_mem1', length=1, delay_cost=1)
	S += r161_mem1 >= 85
	r161_mem1 += MAS_MEM[15]

	r161 = S.Task('r161', length=4, delay_cost=1)
	S += r161 >= 86
	r161 += MAS[7]

	Y_new0_w = S.Task('Y_new0_w', length=1, delay_cost=1)
	S += Y_new0_w >= 89
	Y_new0_w += MAIN_MEM_w

	Y_new1_in = S.Task('Y_new1_in', length=1, delay_cost=1)
	S += Y_new1_in >= 89
	Y_new1_in += MAS_in[7]

	Y_new1_mem0 = S.Task('Y_new1_mem0', length=1, delay_cost=1)
	S += Y_new1_mem0 >= 89
	Y_new1_mem0 += MAS_MEM[14]

	Y_new1_mem1 = S.Task('Y_new1_mem1', length=1, delay_cost=1)
	S += Y_new1_mem1 >= 89
	Y_new1_mem1 += MAS_MEM[15]

	Y_new1 = S.Task('Y_new1', length=4, delay_cost=1)
	S += Y_new1 >= 90
	Y_new1 += MAS[7]

	Y_new1_w = S.Task('Y_new1_w', length=1, delay_cost=1)
	S += Y_new1_w >= 94
	Y_new1_w += MAIN_MEM_w


	# new tasks
	r11_t5 = S.Task('r11_t5', length=4, delay_cost=1)
	r11_t5 += alt(MAS)
	r11_t5_in = S.Task('r11_t5_in', length=1, delay_cost=1)
	r11_t5_in += alt(MAS_in)
	S += r11_t5_in*MAS_in[0]<=r11_t5*MAS[0]

	S += r11_t5_in*MAS_in[1]<=r11_t5*MAS[1]

	S += r11_t5_in*MAS_in[2]<=r11_t5*MAS[2]

	S += r11_t5_in*MAS_in[3]<=r11_t5*MAS[3]

	S += r11_t5_in*MAS_in[4]<=r11_t5*MAS[4]

	S += r11_t5_in*MAS_in[5]<=r11_t5*MAS[5]

	S += r11_t5_in*MAS_in[6]<=r11_t5*MAS[6]

	S += r11_t5_in*MAS_in[7]<=r11_t5*MAS[7]

	S += r11_t5<67

	r11_t5_mem0 = S.Task('r11_t5_mem0', length=1, delay_cost=1)
	r11_t5_mem0 += MM_MEM[2]
	S += 59 < r11_t5_mem0
	S += r11_t5_mem0 <= r11_t5

	r11_t5_mem1 = S.Task('r11_t5_mem1', length=1, delay_cost=1)
	r11_t5_mem1 += MM_MEM[3]
	S += 59 < r11_t5_mem1
	S += r11_t5_mem1 <= r11_t5

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

	S += Z_new0_in*MAS_in[6]<=Z_new0*MAS[6]

	S += Z_new0_in*MAS_in[7]<=Z_new0*MAS[7]

	S += 0<Z_new0

	Z_new0_w = S.Task('Z_new0_w', length=1, delay_cost=1)
	Z_new0_w += alt(MAIN_MEM_w)
	S += Z_new0 <= Z_new0_w

	S += Z_new0<1000

	Z_new0_mem0 = S.Task('Z_new0_mem0', length=1, delay_cost=1)
	Z_new0_mem0 += MM_MEM[2]
	S += 46 < Z_new0_mem0
	S += Z_new0_mem0 <= Z_new0

	Z_new0_mem1 = S.Task('Z_new0_mem1', length=1, delay_cost=1)
	Z_new0_mem1 += MM_MEM[3]
	S += 60 < Z_new0_mem1
	S += Z_new0_mem1 <= Z_new0

	r110 = S.Task('r110', length=4, delay_cost=1)
	r110 += alt(MAS)
	r110_in = S.Task('r110_in', length=1, delay_cost=1)
	r110_in += alt(MAS_in)
	S += r110_in*MAS_in[0]<=r110*MAS[0]

	S += r110_in*MAS_in[1]<=r110*MAS[1]

	S += r110_in*MAS_in[2]<=r110*MAS[2]

	S += r110_in*MAS_in[3]<=r110*MAS[3]

	S += r110_in*MAS_in[4]<=r110*MAS[4]

	S += r110_in*MAS_in[5]<=r110*MAS[5]

	S += r110_in*MAS_in[6]<=r110*MAS[6]

	S += r110_in*MAS_in[7]<=r110*MAS[7]

	S += r110<71

	r110_mem0 = S.Task('r110_mem0', length=1, delay_cost=1)
	r110_mem0 += MM_MEM[2]
	S += 66 < r110_mem0
	S += r110_mem0 <= r110

	r110_mem1 = S.Task('r110_mem1', length=1, delay_cost=1)
	r110_mem1 += alt(MAS_MEM)
	S += (r11_t5*MAS[0])-1 < r110_mem1*MAS_MEM[1]
	S += (r11_t5*MAS[1])-1 < r110_mem1*MAS_MEM[3]
	S += (r11_t5*MAS[2])-1 < r110_mem1*MAS_MEM[5]
	S += (r11_t5*MAS[3])-1 < r110_mem1*MAS_MEM[7]
	S += (r11_t5*MAS[4])-1 < r110_mem1*MAS_MEM[9]
	S += (r11_t5*MAS[5])-1 < r110_mem1*MAS_MEM[11]
	S += (r11_t5*MAS[6])-1 < r110_mem1*MAS_MEM[13]
	S += (r11_t5*MAS[7])-1 < r110_mem1*MAS_MEM[15]
	S += r110_mem1 <= r110

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage4MAS8/EP2_YRECOVER/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

