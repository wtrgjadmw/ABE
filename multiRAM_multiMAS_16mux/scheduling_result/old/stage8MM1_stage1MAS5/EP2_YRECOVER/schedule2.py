from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 126
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	r13_t0_in = S.Task('r13_t0_in', length=1, delay_cost=1)
	S += r13_t0_in >= 0
	r13_t0_in += MM_in[0]

	r3_t3_mem1 = S.Task('r3_t3_mem1', length=1, delay_cost=1)
	S += r3_t3_mem1 >= 0
	r3_t3_mem1 += MAIN_MEM_r[1]

	r6_t1_mem0 = S.Task('r6_t1_mem0', length=1, delay_cost=1)
	S += r6_t1_mem0 >= 0
	r6_t1_mem0 += MAIN_MEM_r[0]

	r12_t0_in = S.Task('r12_t0_in', length=1, delay_cost=1)
	S += r12_t0_in >= 1
	r12_t0_in += MM_in[0]

	r12_t3 = S.Task('r12_t3', length=1, delay_cost=1)
	S += r12_t3 >= 1
	r12_t3 += MAS[4]

	r13_t0 = S.Task('r13_t0', length=8, delay_cost=1)
	S += r13_t0 >= 1
	r13_t0 += MM[0]

	r13_t3_mem0 = S.Task('r13_t3_mem0', length=1, delay_cost=1)
	S += r13_t3_mem0 >= 1
	r13_t3_mem0 += MAIN_MEM_r[0]

	r13_t3_mem1 = S.Task('r13_t3_mem1', length=1, delay_cost=1)
	S += r13_t3_mem1 >= 1
	r13_t3_mem1 += MAIN_MEM_r[1]

	r16_t3 = S.Task('r16_t3', length=1, delay_cost=1)
	S += r16_t3 >= 1
	r16_t3 += MAS[3]

	r1_t3 = S.Task('r1_t3', length=1, delay_cost=1)
	S += r1_t3 >= 1
	r1_t3 += MAS[1]

	r4_t2 = S.Task('r4_t2', length=1, delay_cost=1)
	S += r4_t2 >= 1
	r4_t2 += MAS[2]

	r6_t3 = S.Task('r6_t3', length=1, delay_cost=1)
	S += r6_t3 >= 1
	r6_t3 += MAS[0]

	r12_t0 = S.Task('r12_t0', length=8, delay_cost=1)
	S += r12_t0 >= 2
	r12_t0 += MM[0]

	r13_t3 = S.Task('r13_t3', length=1, delay_cost=1)
	S += r13_t3 >= 2
	r13_t3 += MAS[2]

	r1_t0_in = S.Task('r1_t0_in', length=1, delay_cost=1)
	S += r1_t0_in >= 2
	r1_t0_in += MM_in[0]

	r1_t2 = S.Task('r1_t2', length=1, delay_cost=1)
	S += r1_t2 >= 2
	r1_t2 += MAS[0]

	r3_t2 = S.Task('r3_t2', length=1, delay_cost=1)
	S += r3_t2 >= 2
	r3_t2 += MAS[3]

	r4_t3_mem0 = S.Task('r4_t3_mem0', length=1, delay_cost=1)
	S += r4_t3_mem0 >= 2
	r4_t3_mem0 += MAIN_MEM_r[0]

	r5_t2 = S.Task('r5_t2', length=1, delay_cost=1)
	S += r5_t2 >= 2
	r5_t2 += MAS[4]

	r6_t2_mem1 = S.Task('r6_t2_mem1', length=1, delay_cost=1)
	S += r6_t2_mem1 >= 2
	r6_t2_mem1 += MAIN_MEM_r[1]

	r9_t2 = S.Task('r9_t2', length=1, delay_cost=1)
	S += r9_t2 >= 2
	r9_t2 += MAS[1]

	r12_t2 = S.Task('r12_t2', length=1, delay_cost=1)
	S += r12_t2 >= 3
	r12_t2 += MAS[4]

	r13_t2 = S.Task('r13_t2', length=1, delay_cost=1)
	S += r13_t2 >= 3
	r13_t2 += MAS[0]

	r1_t0 = S.Task('r1_t0', length=8, delay_cost=1)
	S += r1_t0 >= 3
	r1_t0 += MM[0]

	r4_t0_in = S.Task('r4_t0_in', length=1, delay_cost=1)
	S += r4_t0_in >= 3
	r4_t0_in += MM_in[0]

	r4_t3 = S.Task('r4_t3', length=1, delay_cost=1)
	S += r4_t3 >= 3
	r4_t3 += MAS[1]

	r5_t1_mem0 = S.Task('r5_t1_mem0', length=1, delay_cost=1)
	S += r5_t1_mem0 >= 3
	r5_t1_mem0 += MAIN_MEM_r[0]

	r5_t1_mem1 = S.Task('r5_t1_mem1', length=1, delay_cost=1)
	S += r5_t1_mem1 >= 3
	r5_t1_mem1 += MAIN_MEM_r[1]

	r5_t3 = S.Task('r5_t3', length=1, delay_cost=1)
	S += r5_t3 >= 3
	r5_t3 += MAS[2]

	r6_t2 = S.Task('r6_t2', length=1, delay_cost=1)
	S += r6_t2 >= 3
	r6_t2 += MAS[3]

	r16_t3_mem1 = S.Task('r16_t3_mem1', length=1, delay_cost=1)
	S += r16_t3_mem1 >= 4
	r16_t3_mem1 += MAIN_MEM_r[1]

	r3_t3 = S.Task('r3_t3', length=1, delay_cost=1)
	S += r3_t3 >= 4
	r3_t3 += MAS[3]

	r4_t0 = S.Task('r4_t0', length=8, delay_cost=1)
	S += r4_t0 >= 4
	r4_t0 += MM[0]

	r6_t1_in = S.Task('r6_t1_in', length=1, delay_cost=1)
	S += r6_t1_in >= 4
	r6_t1_in += MM_in[0]

	r6_t3_mem0 = S.Task('r6_t3_mem0', length=1, delay_cost=1)
	S += r6_t3_mem0 >= 4
	r6_t3_mem0 += MAIN_MEM_r[0]

	r12_t0_mem0 = S.Task('r12_t0_mem0', length=1, delay_cost=1)
	S += r12_t0_mem0 >= 5
	r12_t0_mem0 += MAIN_MEM_r[0]

	r12_t1_in = S.Task('r12_t1_in', length=1, delay_cost=1)
	S += r12_t1_in >= 5
	r12_t1_in += MM_in[0]

	r5_t3_mem1 = S.Task('r5_t3_mem1', length=1, delay_cost=1)
	S += r5_t3_mem1 >= 5
	r5_t3_mem1 += MAIN_MEM_r[1]

	r6_t1 = S.Task('r6_t1', length=8, delay_cost=1)
	S += r6_t1 >= 5
	r6_t1 += MM[0]

	r12_t1 = S.Task('r12_t1', length=8, delay_cost=1)
	S += r12_t1 >= 6
	r12_t1 += MM[0]

	r1_t1_in = S.Task('r1_t1_in', length=1, delay_cost=1)
	S += r1_t1_in >= 6
	r1_t1_in += MM_in[0]

	r9_t2_mem0 = S.Task('r9_t2_mem0', length=1, delay_cost=1)
	S += r9_t2_mem0 >= 6
	r9_t2_mem0 += MAIN_MEM_r[0]

	r9_t2_mem1 = S.Task('r9_t2_mem1', length=1, delay_cost=1)
	S += r9_t2_mem1 >= 6
	r9_t2_mem1 += MAIN_MEM_r[1]

	r1_t1 = S.Task('r1_t1', length=8, delay_cost=1)
	S += r1_t1 >= 7
	r1_t1 += MM[0]

	r4_t1_in = S.Task('r4_t1_in', length=1, delay_cost=1)
	S += r4_t1_in >= 7
	r4_t1_in += MM_in[0]

	r4_t3_mem1 = S.Task('r4_t3_mem1', length=1, delay_cost=1)
	S += r4_t3_mem1 >= 7
	r4_t3_mem1 += MAIN_MEM_r[1]

	r5_t0_mem0 = S.Task('r5_t0_mem0', length=1, delay_cost=1)
	S += r5_t0_mem0 >= 7
	r5_t0_mem0 += MAIN_MEM_r[0]

	r12_t0_mem1 = S.Task('r12_t0_mem1', length=1, delay_cost=1)
	S += r12_t0_mem1 >= 8
	r12_t0_mem1 += MAIN_MEM_r[1]

	r3_t0_in = S.Task('r3_t0_in', length=1, delay_cost=1)
	S += r3_t0_in >= 8
	r3_t0_in += MM_in[0]

	r4_t0_mem0 = S.Task('r4_t0_mem0', length=1, delay_cost=1)
	S += r4_t0_mem0 >= 8
	r4_t0_mem0 += MAIN_MEM_r[0]

	r4_t1 = S.Task('r4_t1', length=8, delay_cost=1)
	S += r4_t1 >= 8
	r4_t1 += MM[0]

	r3_t0 = S.Task('r3_t0', length=8, delay_cost=1)
	S += r3_t0 >= 9
	r3_t0 += MM[0]

	r5_t1_in = S.Task('r5_t1_in', length=1, delay_cost=1)
	S += r5_t1_in >= 9
	r5_t1_in += MM_in[0]

	r6_t2_mem0 = S.Task('r6_t2_mem0', length=1, delay_cost=1)
	S += r6_t2_mem0 >= 9
	r6_t2_mem0 += MAIN_MEM_r[0]

	r6_t3_mem1 = S.Task('r6_t3_mem1', length=1, delay_cost=1)
	S += r6_t3_mem1 >= 9
	r6_t3_mem1 += MAIN_MEM_r[1]

	r13_t1_mem0 = S.Task('r13_t1_mem0', length=1, delay_cost=1)
	S += r13_t1_mem0 >= 10
	r13_t1_mem0 += MAIN_MEM_r[0]

	r13_t1_mem1 = S.Task('r13_t1_mem1', length=1, delay_cost=1)
	S += r13_t1_mem1 >= 10
	r13_t1_mem1 += MAIN_MEM_r[1]

	r3_t1_in = S.Task('r3_t1_in', length=1, delay_cost=1)
	S += r3_t1_in >= 10
	r3_t1_in += MM_in[0]

	r5_t1 = S.Task('r5_t1', length=8, delay_cost=1)
	S += r5_t1 >= 10
	r5_t1 += MM[0]

	r3_t1 = S.Task('r3_t1', length=8, delay_cost=1)
	S += r3_t1 >= 11
	r3_t1 += MM[0]

	r4_t2_mem0 = S.Task('r4_t2_mem0', length=1, delay_cost=1)
	S += r4_t2_mem0 >= 11
	r4_t2_mem0 += MAIN_MEM_r[0]

	r5_t0_mem1 = S.Task('r5_t0_mem1', length=1, delay_cost=1)
	S += r5_t0_mem1 >= 11
	r5_t0_mem1 += MAIN_MEM_r[1]

	r6_t0_in = S.Task('r6_t0_in', length=1, delay_cost=1)
	S += r6_t0_in >= 11
	r6_t0_in += MM_in[0]

	r3_t3_mem0 = S.Task('r3_t3_mem0', length=1, delay_cost=1)
	S += r3_t3_mem0 >= 12
	r3_t3_mem0 += MAIN_MEM_r[0]

	r5_t0_in = S.Task('r5_t0_in', length=1, delay_cost=1)
	S += r5_t0_in >= 12
	r5_t0_in += MM_in[0]

	r5_t2_mem1 = S.Task('r5_t2_mem1', length=1, delay_cost=1)
	S += r5_t2_mem1 >= 12
	r5_t2_mem1 += MAIN_MEM_r[1]

	r6_t0 = S.Task('r6_t0', length=8, delay_cost=1)
	S += r6_t0 >= 12
	r6_t0 += MM[0]

	r120_mem0 = S.Task('r120_mem0', length=1, delay_cost=1)
	S += r120_mem0 >= 13
	r120_mem0 += MM_MEM[0]

	r120_mem1 = S.Task('r120_mem1', length=1, delay_cost=1)
	S += r120_mem1 >= 13
	r120_mem1 += MM_MEM[1]

	r12_t1_mem0 = S.Task('r12_t1_mem0', length=1, delay_cost=1)
	S += r12_t1_mem0 >= 13
	r12_t1_mem0 += MAIN_MEM_r[0]

	r13_t1_in = S.Task('r13_t1_in', length=1, delay_cost=1)
	S += r13_t1_in >= 13
	r13_t1_in += MM_in[0]

	r4_t0_mem1 = S.Task('r4_t0_mem1', length=1, delay_cost=1)
	S += r4_t0_mem1 >= 13
	r4_t0_mem1 += MAIN_MEM_r[1]

	r5_t0 = S.Task('r5_t0', length=8, delay_cost=1)
	S += r5_t0 >= 13
	r5_t0 += MM[0]

	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	S += r10_mem0 >= 14
	r10_mem0 += MM_MEM[0]

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	S += r10_mem1 >= 14
	r10_mem1 += MM_MEM[1]

	r120 = S.Task('r120', length=1, delay_cost=1)
	S += r120 >= 14
	r120 += MAS[1]

	r13_t0_mem0 = S.Task('r13_t0_mem0', length=1, delay_cost=1)
	S += r13_t0_mem0 >= 14
	r13_t0_mem0 += MAIN_MEM_r[0]

	r13_t1 = S.Task('r13_t1', length=8, delay_cost=1)
	S += r13_t1 >= 14
	r13_t1 += MM[0]

	r13_t2_mem1 = S.Task('r13_t2_mem1', length=1, delay_cost=1)
	S += r13_t2_mem1 >= 14
	r13_t2_mem1 += MAIN_MEM_r[1]

	r4_t4_in = S.Task('r4_t4_in', length=1, delay_cost=1)
	S += r4_t4_in >= 14
	r4_t4_in += MM_in[0]

	r4_t4_mem0 = S.Task('r4_t4_mem0', length=1, delay_cost=1)
	S += r4_t4_mem0 >= 14
	r4_t4_mem0 += MAS_MEM[4]

	r4_t4_mem1 = S.Task('r4_t4_mem1', length=1, delay_cost=1)
	S += r4_t4_mem1 >= 14
	r4_t4_mem1 += MAS_MEM[3]

	r10 = S.Task('r10', length=1, delay_cost=1)
	S += r10 >= 15
	r10 += MAS[0]

	r12_t1_mem1 = S.Task('r12_t1_mem1', length=1, delay_cost=1)
	S += r12_t1_mem1 >= 15
	r12_t1_mem1 += MAIN_MEM_r[1]

	r12_t4_in = S.Task('r12_t4_in', length=1, delay_cost=1)
	S += r12_t4_in >= 15
	r12_t4_in += MM_in[0]

	r12_t4_mem0 = S.Task('r12_t4_mem0', length=1, delay_cost=1)
	S += r12_t4_mem0 >= 15
	r12_t4_mem0 += MAS_MEM[8]

	r12_t4_mem1 = S.Task('r12_t4_mem1', length=1, delay_cost=1)
	S += r12_t4_mem1 >= 15
	r12_t4_mem1 += MAS_MEM[9]

	r20_mem0 = S.Task('r20_mem0', length=1, delay_cost=1)
	S += r20_mem0 >= 15
	r20_mem0 += MAS_MEM[0]

	r40_mem0 = S.Task('r40_mem0', length=1, delay_cost=1)
	S += r40_mem0 >= 15
	r40_mem0 += MM_MEM[0]

	r40_mem1 = S.Task('r40_mem1', length=1, delay_cost=1)
	S += r40_mem1 >= 15
	r40_mem1 += MM_MEM[1]

	r4_t4 = S.Task('r4_t4', length=8, delay_cost=1)
	S += r4_t4 >= 15
	r4_t4 += MM[0]

	r6_t0_mem0 = S.Task('r6_t0_mem0', length=1, delay_cost=1)
	S += r6_t0_mem0 >= 15
	r6_t0_mem0 += MAIN_MEM_r[0]

	r12_t4 = S.Task('r12_t4', length=8, delay_cost=1)
	S += r12_t4 >= 16
	r12_t4 += MM[0]

	r20 = S.Task('r20', length=1, delay_cost=1)
	S += r20 >= 16
	r20 += MAS[4]

	r3_t4_in = S.Task('r3_t4_in', length=1, delay_cost=1)
	S += r3_t4_in >= 16
	r3_t4_in += MM_in[0]

	r3_t4_mem0 = S.Task('r3_t4_mem0', length=1, delay_cost=1)
	S += r3_t4_mem0 >= 16
	r3_t4_mem0 += MAS_MEM[6]

	r3_t4_mem1 = S.Task('r3_t4_mem1', length=1, delay_cost=1)
	S += r3_t4_mem1 >= 16
	r3_t4_mem1 += MAS_MEM[7]

	r40 = S.Task('r40', length=1, delay_cost=1)
	S += r40 >= 16
	r40 += MAS[1]

	r4_t1_mem1 = S.Task('r4_t1_mem1', length=1, delay_cost=1)
	S += r4_t1_mem1 >= 16
	r4_t1_mem1 += MAIN_MEM_r[1]

	r4_t5_mem0 = S.Task('r4_t5_mem0', length=1, delay_cost=1)
	S += r4_t5_mem0 >= 16
	r4_t5_mem0 += MM_MEM[0]

	r4_t5_mem1 = S.Task('r4_t5_mem1', length=1, delay_cost=1)
	S += r4_t5_mem1 >= 16
	r4_t5_mem1 += MM_MEM[1]

	r5_t2_mem0 = S.Task('r5_t2_mem0', length=1, delay_cost=1)
	S += r5_t2_mem0 >= 16
	r5_t2_mem0 += MAIN_MEM_r[0]

	r80_mem1 = S.Task('r80_mem1', length=1, delay_cost=1)
	S += r80_mem1 >= 16
	r80_mem1 += MAS_MEM[3]

	r100_mem1 = S.Task('r100_mem1', length=1, delay_cost=1)
	S += r100_mem1 >= 17
	r100_mem1 += MAS_MEM[3]

	r12_t5_mem0 = S.Task('r12_t5_mem0', length=1, delay_cost=1)
	S += r12_t5_mem0 >= 17
	r12_t5_mem0 += MM_MEM[0]

	r12_t5_mem1 = S.Task('r12_t5_mem1', length=1, delay_cost=1)
	S += r12_t5_mem1 >= 17
	r12_t5_mem1 += MM_MEM[1]

	r13_t2_mem0 = S.Task('r13_t2_mem0', length=1, delay_cost=1)
	S += r13_t2_mem0 >= 17
	r13_t2_mem0 += MAIN_MEM_r[0]

	r13_t4_in = S.Task('r13_t4_in', length=1, delay_cost=1)
	S += r13_t4_in >= 17
	r13_t4_in += MM_in[0]

	r13_t4_mem0 = S.Task('r13_t4_mem0', length=1, delay_cost=1)
	S += r13_t4_mem0 >= 17
	r13_t4_mem0 += MAS_MEM[0]

	r13_t4_mem1 = S.Task('r13_t4_mem1', length=1, delay_cost=1)
	S += r13_t4_mem1 >= 17
	r13_t4_mem1 += MAS_MEM[5]

	r3_t4 = S.Task('r3_t4', length=8, delay_cost=1)
	S += r3_t4 >= 17
	r3_t4 += MM[0]

	r4_t5 = S.Task('r4_t5', length=1, delay_cost=1)
	S += r4_t5 >= 17
	r4_t5 += MAS[4]

	r6_t0_mem1 = S.Task('r6_t0_mem1', length=1, delay_cost=1)
	S += r6_t0_mem1 >= 17
	r6_t0_mem1 += MAIN_MEM_r[1]

	r80 = S.Task('r80', length=1, delay_cost=1)
	S += r80 >= 17
	r80 += MAS[3]

	r100 = S.Task('r100', length=1, delay_cost=1)
	S += r100 >= 18
	r100 += MAS[1]

	r12_t2_mem0 = S.Task('r12_t2_mem0', length=1, delay_cost=1)
	S += r12_t2_mem0 >= 18
	r12_t2_mem0 += MAIN_MEM_r[0]

	r12_t2_mem1 = S.Task('r12_t2_mem1', length=1, delay_cost=1)
	S += r12_t2_mem1 >= 18
	r12_t2_mem1 += MAIN_MEM_r[1]

	r12_t5 = S.Task('r12_t5', length=1, delay_cost=1)
	S += r12_t5 >= 18
	r12_t5 += MAS[3]

	r13_t4 = S.Task('r13_t4', length=8, delay_cost=1)
	S += r13_t4 >= 18
	r13_t4 += MM[0]

	r30_mem0 = S.Task('r30_mem0', length=1, delay_cost=1)
	S += r30_mem0 >= 18
	r30_mem0 += MM_MEM[0]

	r30_mem1 = S.Task('r30_mem1', length=1, delay_cost=1)
	S += r30_mem1 >= 18
	r30_mem1 += MM_MEM[1]

	r5_t4_in = S.Task('r5_t4_in', length=1, delay_cost=1)
	S += r5_t4_in >= 18
	r5_t4_in += MM_in[0]

	r5_t4_mem0 = S.Task('r5_t4_mem0', length=1, delay_cost=1)
	S += r5_t4_mem0 >= 18
	r5_t4_mem0 += MAS_MEM[8]

	r5_t4_mem1 = S.Task('r5_t4_mem1', length=1, delay_cost=1)
	S += r5_t4_mem1 >= 18
	r5_t4_mem1 += MAS_MEM[5]

	r12_t3_mem0 = S.Task('r12_t3_mem0', length=1, delay_cost=1)
	S += r12_t3_mem0 >= 19
	r12_t3_mem0 += MAIN_MEM_r[0]

	r12_t3_mem1 = S.Task('r12_t3_mem1', length=1, delay_cost=1)
	S += r12_t3_mem1 >= 19
	r12_t3_mem1 += MAIN_MEM_r[1]

	r14_t0_in = S.Task('r14_t0_in', length=1, delay_cost=1)
	S += r14_t0_in >= 19
	r14_t0_in += MM_in[0]

	r14_t0_mem0 = S.Task('r14_t0_mem0', length=1, delay_cost=1)
	S += r14_t0_mem0 >= 19
	r14_t0_mem0 += MAS_MEM[8]

	r14_t0_mem1 = S.Task('r14_t0_mem1', length=1, delay_cost=1)
	S += r14_t0_mem1 >= 19
	r14_t0_mem1 += MAS_MEM[5]

	r30 = S.Task('r30', length=1, delay_cost=1)
	S += r30 >= 19
	r30 += MAS[2]

	r5_t4 = S.Task('r5_t4', length=8, delay_cost=1)
	S += r5_t4 >= 19
	r5_t4 += MM[0]

	r60_mem0 = S.Task('r60_mem0', length=1, delay_cost=1)
	S += r60_mem0 >= 19
	r60_mem0 += MM_MEM[0]

	r60_mem1 = S.Task('r60_mem1', length=1, delay_cost=1)
	S += r60_mem1 >= 19
	r60_mem1 += MM_MEM[1]

	r14_t0 = S.Task('r14_t0', length=8, delay_cost=1)
	S += r14_t0 >= 20
	r14_t0 += MM[0]

	r1_t4_in = S.Task('r1_t4_in', length=1, delay_cost=1)
	S += r1_t4_in >= 20
	r1_t4_in += MM_in[0]

	r1_t4_mem0 = S.Task('r1_t4_mem0', length=1, delay_cost=1)
	S += r1_t4_mem0 >= 20
	r1_t4_mem0 += MAS_MEM[0]

	r1_t4_mem1 = S.Task('r1_t4_mem1', length=1, delay_cost=1)
	S += r1_t4_mem1 >= 20
	r1_t4_mem1 += MAS_MEM[3]

	r3_t2_mem0 = S.Task('r3_t2_mem0', length=1, delay_cost=1)
	S += r3_t2_mem0 >= 20
	r3_t2_mem0 += MAIN_MEM_r[0]

	r3_t2_mem1 = S.Task('r3_t2_mem1', length=1, delay_cost=1)
	S += r3_t2_mem1 >= 20
	r3_t2_mem1 += MAIN_MEM_r[1]

	r50_mem0 = S.Task('r50_mem0', length=1, delay_cost=1)
	S += r50_mem0 >= 20
	r50_mem0 += MM_MEM[0]

	r50_mem1 = S.Task('r50_mem1', length=1, delay_cost=1)
	S += r50_mem1 >= 20
	r50_mem1 += MM_MEM[1]

	r60 = S.Task('r60', length=1, delay_cost=1)
	S += r60 >= 20
	r60 += MAS[2]

	X_new_t0_in = S.Task('X_new_t0_in', length=1, delay_cost=1)
	S += X_new_t0_in >= 21
	X_new_t0_in += MM_in[0]

	X_new_t0_mem0 = S.Task('X_new_t0_mem0', length=1, delay_cost=1)
	S += X_new_t0_mem0 >= 21
	X_new_t0_mem0 += MAS_MEM[8]

	X_new_t0_mem1 = S.Task('X_new_t0_mem1', length=1, delay_cost=1)
	S += X_new_t0_mem1 >= 21
	X_new_t0_mem1 += MAS_MEM[3]

	r130_mem0 = S.Task('r130_mem0', length=1, delay_cost=1)
	S += r130_mem0 >= 21
	r130_mem0 += MM_MEM[0]

	r130_mem1 = S.Task('r130_mem1', length=1, delay_cost=1)
	S += r130_mem1 >= 21
	r130_mem1 += MM_MEM[1]

	r13_t0_mem1 = S.Task('r13_t0_mem1', length=1, delay_cost=1)
	S += r13_t0_mem1 >= 21
	r13_t0_mem1 += MAIN_MEM_r[1]

	r1_t4 = S.Task('r1_t4', length=8, delay_cost=1)
	S += r1_t4 >= 21
	r1_t4 += MM[0]

	r50 = S.Task('r50', length=1, delay_cost=1)
	S += r50 >= 21
	r50 += MAS[1]

	r5_t3_mem0 = S.Task('r5_t3_mem0', length=1, delay_cost=1)
	S += r5_t3_mem0 >= 21
	r5_t3_mem0 += MAIN_MEM_r[0]

	r70_mem0 = S.Task('r70_mem0', length=1, delay_cost=1)
	S += r70_mem0 >= 21
	r70_mem0 += MAS_MEM[2]

	r70_mem1 = S.Task('r70_mem1', length=1, delay_cost=1)
	S += r70_mem1 >= 21
	r70_mem1 += MAS_MEM[5]

	X_new_t0 = S.Task('X_new_t0', length=8, delay_cost=1)
	S += X_new_t0 >= 22
	X_new_t0 += MM[0]

	Z_new_t0_in = S.Task('Z_new_t0_in', length=1, delay_cost=1)
	S += Z_new_t0_in >= 22
	Z_new_t0_in += MM_in[0]

	Z_new_t0_mem0 = S.Task('Z_new_t0_mem0', length=1, delay_cost=1)
	S += Z_new_t0_mem0 >= 22
	Z_new_t0_mem0 += MAS_MEM[8]

	Z_new_t0_mem1 = S.Task('Z_new_t0_mem1', length=1, delay_cost=1)
	S += Z_new_t0_mem1 >= 22
	Z_new_t0_mem1 += MAS_MEM[3]

	r130 = S.Task('r130', length=1, delay_cost=1)
	S += r130 >= 22
	r130 += MAS[1]

	r3_t0_mem0 = S.Task('r3_t0_mem0', length=1, delay_cost=1)
	S += r3_t0_mem0 >= 22
	r3_t0_mem0 += MAIN_MEM_r[0]

	r41_mem0 = S.Task('r41_mem0', length=1, delay_cost=1)
	S += r41_mem0 >= 22
	r41_mem0 += MM_MEM[0]

	r41_mem1 = S.Task('r41_mem1', length=1, delay_cost=1)
	S += r41_mem1 >= 22
	r41_mem1 += MAS_MEM[9]

	r6_t1_mem1 = S.Task('r6_t1_mem1', length=1, delay_cost=1)
	S += r6_t1_mem1 >= 22
	r6_t1_mem1 += MAIN_MEM_r[1]

	r70 = S.Task('r70', length=1, delay_cost=1)
	S += r70 >= 22
	r70 += MAS[2]

	Z_new_t0 = S.Task('Z_new_t0', length=8, delay_cost=1)
	S += Z_new_t0 >= 23
	Z_new_t0 += MM[0]

	r101_mem1 = S.Task('r101_mem1', length=1, delay_cost=1)
	S += r101_mem1 >= 23
	r101_mem1 += MAS_MEM[3]

	r121_mem0 = S.Task('r121_mem0', length=1, delay_cost=1)
	S += r121_mem0 >= 23
	r121_mem0 += MM_MEM[0]

	r121_mem1 = S.Task('r121_mem1', length=1, delay_cost=1)
	S += r121_mem1 >= 23
	r121_mem1 += MAS_MEM[7]

	r41 = S.Task('r41', length=1, delay_cost=1)
	S += r41 >= 23
	r41 += MAS[1]

	r4_t1_mem0 = S.Task('r4_t1_mem0', length=1, delay_cost=1)
	S += r4_t1_mem0 >= 23
	r4_t1_mem0 += MAIN_MEM_r[0]

	r4_t2_mem1 = S.Task('r4_t2_mem1', length=1, delay_cost=1)
	S += r4_t2_mem1 >= 23
	r4_t2_mem1 += MAIN_MEM_r[1]

	r6_t4_in = S.Task('r6_t4_in', length=1, delay_cost=1)
	S += r6_t4_in >= 23
	r6_t4_in += MM_in[0]

	r6_t4_mem0 = S.Task('r6_t4_mem0', length=1, delay_cost=1)
	S += r6_t4_mem0 >= 23
	r6_t4_mem0 += MAS_MEM[6]

	r6_t4_mem1 = S.Task('r6_t4_mem1', length=1, delay_cost=1)
	S += r6_t4_mem1 >= 23
	r6_t4_mem1 += MAS_MEM[1]

	X_new_t3_mem0 = S.Task('X_new_t3_mem0', length=1, delay_cost=1)
	S += X_new_t3_mem0 >= 24
	X_new_t3_mem0 += MAS_MEM[2]

	X_new_t3_mem1 = S.Task('X_new_t3_mem1', length=1, delay_cost=1)
	S += X_new_t3_mem1 >= 24
	X_new_t3_mem1 += MAS_MEM[7]

	r101 = S.Task('r101', length=1, delay_cost=1)
	S += r101 >= 24
	r101 += MAS[4]

	r121 = S.Task('r121', length=1, delay_cost=1)
	S += r121 >= 24
	r121 += MAS[3]

	r13_t5_mem0 = S.Task('r13_t5_mem0', length=1, delay_cost=1)
	S += r13_t5_mem0 >= 24
	r13_t5_mem0 += MM_MEM[0]

	r13_t5_mem1 = S.Task('r13_t5_mem1', length=1, delay_cost=1)
	S += r13_t5_mem1 >= 24
	r13_t5_mem1 += MM_MEM[1]

	r1_t0_mem1 = S.Task('r1_t0_mem1', length=1, delay_cost=1)
	S += r1_t0_mem1 >= 24
	r1_t0_mem1 += MAIN_MEM_r[1]

	r3_t1_mem0 = S.Task('r3_t1_mem0', length=1, delay_cost=1)
	S += r3_t1_mem0 >= 24
	r3_t1_mem0 += MAIN_MEM_r[0]

	r6_t4 = S.Task('r6_t4', length=8, delay_cost=1)
	S += r6_t4 >= 24
	r6_t4 += MM[0]

	r81_mem1 = S.Task('r81_mem1', length=1, delay_cost=1)
	S += r81_mem1 >= 24
	r81_mem1 += MAS_MEM[3]

	r9_t0_in = S.Task('r9_t0_in', length=1, delay_cost=1)
	S += r9_t0_in >= 24
	r9_t0_in += MM_in[0]

	r9_t0_mem1 = S.Task('r9_t0_mem1', length=1, delay_cost=1)
	S += r9_t0_mem1 >= 24
	r9_t0_mem1 += MAS_MEM[5]

	X_new_t3 = S.Task('X_new_t3', length=1, delay_cost=1)
	S += X_new_t3 >= 25
	X_new_t3 += MAS[3]

	r131_mem0 = S.Task('r131_mem0', length=1, delay_cost=1)
	S += r131_mem0 >= 25
	r131_mem0 += MM_MEM[0]

	r131_mem1 = S.Task('r131_mem1', length=1, delay_cost=1)
	S += r131_mem1 >= 25
	r131_mem1 += MAS_MEM[5]

	r13_t5 = S.Task('r13_t5', length=1, delay_cost=1)
	S += r13_t5 >= 25
	r13_t5 += MAS[2]

	r1_t3_mem0 = S.Task('r1_t3_mem0', length=1, delay_cost=1)
	S += r1_t3_mem0 >= 25
	r1_t3_mem0 += MAIN_MEM_r[0]

	r3_t1_mem1 = S.Task('r3_t1_mem1', length=1, delay_cost=1)
	S += r3_t1_mem1 >= 25
	r3_t1_mem1 += MAIN_MEM_r[1]

	r81 = S.Task('r81', length=1, delay_cost=1)
	S += r81 >= 25
	r81 += MAS[0]

	r9_t0 = S.Task('r9_t0', length=8, delay_cost=1)
	S += r9_t0 >= 25
	r9_t0 += MM[0]

	Z_new_t3_mem0 = S.Task('Z_new_t3_mem0', length=1, delay_cost=1)
	S += Z_new_t3_mem0 >= 26
	Z_new_t3_mem0 += MAS_MEM[2]

	Z_new_t3_mem1 = S.Task('Z_new_t3_mem1', length=1, delay_cost=1)
	S += Z_new_t3_mem1 >= 26
	Z_new_t3_mem1 += MAS_MEM[9]

	r131 = S.Task('r131', length=1, delay_cost=1)
	S += r131 >= 26
	r131 += MAS[4]

	r1_t0_mem0 = S.Task('r1_t0_mem0', length=1, delay_cost=1)
	S += r1_t0_mem0 >= 26
	r1_t0_mem0 += MAIN_MEM_r[0]

	r1_t3_mem1 = S.Task('r1_t3_mem1', length=1, delay_cost=1)
	S += r1_t3_mem1 >= 26
	r1_t3_mem1 += MAIN_MEM_r[1]

	r3_t5_mem0 = S.Task('r3_t5_mem0', length=1, delay_cost=1)
	S += r3_t5_mem0 >= 26
	r3_t5_mem0 += MM_MEM[0]

	r3_t5_mem1 = S.Task('r3_t5_mem1', length=1, delay_cost=1)
	S += r3_t5_mem1 >= 26
	r3_t5_mem1 += MM_MEM[1]

	Z_new_t3 = S.Task('Z_new_t3', length=1, delay_cost=1)
	S += Z_new_t3 >= 27
	Z_new_t3 += MAS[3]

	r16_t3_mem0 = S.Task('r16_t3_mem0', length=1, delay_cost=1)
	S += r16_t3_mem0 >= 27
	r16_t3_mem0 += MAIN_MEM_r[0]

	r31_mem0 = S.Task('r31_mem0', length=1, delay_cost=1)
	S += r31_mem0 >= 27
	r31_mem0 += MM_MEM[0]

	r31_mem1 = S.Task('r31_mem1', length=1, delay_cost=1)
	S += r31_mem1 >= 27
	r31_mem1 += MAS_MEM[9]

	r3_t0_mem1 = S.Task('r3_t0_mem1', length=1, delay_cost=1)
	S += r3_t0_mem1 >= 27
	r3_t0_mem1 += MAIN_MEM_r[1]

	r3_t5 = S.Task('r3_t5', length=1, delay_cost=1)
	S += r3_t5 >= 27
	r3_t5 += MAS[4]

	r14_t3_mem0 = S.Task('r14_t3_mem0', length=1, delay_cost=1)
	S += r14_t3_mem0 >= 28
	r14_t3_mem0 += MAS_MEM[4]

	r14_t3_mem1 = S.Task('r14_t3_mem1', length=1, delay_cost=1)
	S += r14_t3_mem1 >= 28
	r14_t3_mem1 += MAS_MEM[3]

	r1_t2_mem0 = S.Task('r1_t2_mem0', length=1, delay_cost=1)
	S += r1_t2_mem0 >= 28
	r1_t2_mem0 += MAIN_MEM_r[0]

	r1_t2_mem1 = S.Task('r1_t2_mem1', length=1, delay_cost=1)
	S += r1_t2_mem1 >= 28
	r1_t2_mem1 += MAIN_MEM_r[1]

	r1_t5_mem0 = S.Task('r1_t5_mem0', length=1, delay_cost=1)
	S += r1_t5_mem0 >= 28
	r1_t5_mem0 += MM_MEM[0]

	r1_t5_mem1 = S.Task('r1_t5_mem1', length=1, delay_cost=1)
	S += r1_t5_mem1 >= 28
	r1_t5_mem1 += MM_MEM[1]

	r31 = S.Task('r31', length=1, delay_cost=1)
	S += r31 >= 28
	r31 += MAS[1]

	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	S += r11_mem0 >= 29
	r11_mem0 += MM_MEM[0]

	r11_mem1 = S.Task('r11_mem1', length=1, delay_cost=1)
	S += r11_mem1 >= 29
	r11_mem1 += MAS_MEM[3]

	r14_t3 = S.Task('r14_t3', length=1, delay_cost=1)
	S += r14_t3 >= 29
	r14_t3 += MAS[2]

	r1_t1_mem0 = S.Task('r1_t1_mem0', length=1, delay_cost=1)
	S += r1_t1_mem0 >= 29
	r1_t1_mem0 += MAIN_MEM_r[0]

	r1_t1_mem1 = S.Task('r1_t1_mem1', length=1, delay_cost=1)
	S += r1_t1_mem1 >= 29
	r1_t1_mem1 += MAIN_MEM_r[1]

	r1_t5 = S.Task('r1_t5', length=1, delay_cost=1)
	S += r1_t5 >= 29
	r1_t5 += MAS[1]

	r11 = S.Task('r11', length=1, delay_cost=1)
	S += r11 >= 30
	r11 += MAS[4]

	r21_mem0 = S.Task('r21_mem0', length=1, delay_cost=1)
	S += r21_mem0 >= 30
	r21_mem0 += MAS_MEM[8]

	r5_t5_mem0 = S.Task('r5_t5_mem0', length=1, delay_cost=1)
	S += r5_t5_mem0 >= 30
	r5_t5_mem0 += MM_MEM[0]

	r5_t5_mem1 = S.Task('r5_t5_mem1', length=1, delay_cost=1)
	S += r5_t5_mem1 >= 30
	r5_t5_mem1 += MM_MEM[1]

	r80_mem0 = S.Task('r80_mem0', length=1, delay_cost=1)
	S += r80_mem0 >= 30
	r80_mem0 += MAIN_MEM_r[0]

	r21 = S.Task('r21', length=1, delay_cost=1)
	S += r21 >= 31
	r21 += MAS[1]

	r51_mem0 = S.Task('r51_mem0', length=1, delay_cost=1)
	S += r51_mem0 >= 31
	r51_mem0 += MM_MEM[0]

	r51_mem1 = S.Task('r51_mem1', length=1, delay_cost=1)
	S += r51_mem1 >= 31
	r51_mem1 += MAS_MEM[1]

	r5_t5 = S.Task('r5_t5', length=1, delay_cost=1)
	S += r5_t5 >= 31
	r5_t5 += MAS[0]

	r9_t0_mem0 = S.Task('r9_t0_mem0', length=1, delay_cost=1)
	S += r9_t0_mem0 >= 31
	r9_t0_mem0 += MAIN_MEM_r[0]

	r100_mem0 = S.Task('r100_mem0', length=1, delay_cost=1)
	S += r100_mem0 >= 32
	r100_mem0 += MAIN_MEM_r[0]

	r51 = S.Task('r51', length=1, delay_cost=1)
	S += r51 >= 32
	r51 += MAS[4]

	r6_t5_mem0 = S.Task('r6_t5_mem0', length=1, delay_cost=1)
	S += r6_t5_mem0 >= 32
	r6_t5_mem0 += MM_MEM[0]

	r6_t5_mem1 = S.Task('r6_t5_mem1', length=1, delay_cost=1)
	S += r6_t5_mem1 >= 32
	r6_t5_mem1 += MM_MEM[1]

	r61_mem0 = S.Task('r61_mem0', length=1, delay_cost=1)
	S += r61_mem0 >= 33
	r61_mem0 += MM_MEM[0]

	r61_mem1 = S.Task('r61_mem1', length=1, delay_cost=1)
	S += r61_mem1 >= 33
	r61_mem1 += MAS_MEM[9]

	r6_t5 = S.Task('r6_t5', length=1, delay_cost=1)
	S += r6_t5 >= 33
	r6_t5 += MAS[4]

	r81_mem0 = S.Task('r81_mem0', length=1, delay_cost=1)
	S += r81_mem0 >= 33
	r81_mem0 += MAIN_MEM_r[0]

	r101_mem0 = S.Task('r101_mem0', length=1, delay_cost=1)
	S += r101_mem0 >= 34
	r101_mem0 += MAIN_MEM_r[0]

	r61 = S.Task('r61', length=1, delay_cost=1)
	S += r61 >= 34
	r61 += MAS[3]

	r71_mem0 = S.Task('r71_mem0', length=1, delay_cost=1)
	S += r71_mem0 >= 34
	r71_mem0 += MAS_MEM[8]

	r71_mem1 = S.Task('r71_mem1', length=1, delay_cost=1)
	S += r71_mem1 >= 34
	r71_mem1 += MAS_MEM[7]

	r71 = S.Task('r71', length=1, delay_cost=1)
	S += r71 >= 35
	r71 += MAS[1]


	# new tasks
	r9_t1_in = S.Task('r9_t1_in', length=1, delay_cost=1)
	r9_t1_in += alt(MM_in)
	r9_t1 = S.Task('r9_t1', length=8, delay_cost=1)
	r9_t1 += alt(MM)
	S += r9_t1>=r9_t1_in

	r9_t1_mem0 = S.Task('r9_t1_mem0', length=1, delay_cost=1)
	r9_t1_mem0 += MAIN_MEM_r[0]
	r9_t1_mem1 = S.Task('r9_t1_mem1', length=1, delay_cost=1)
	r9_t1_mem1 += MAS_MEM[3]
	S += 35 < r9_t1_mem1
	S += r9_t1_mem1 <= r9_t1

	r9_t3 = S.Task('r9_t3', length=1, delay_cost=1)
	r9_t3 += alt(MAS)

	r9_t3_mem0 = S.Task('r9_t3_mem0', length=1, delay_cost=1)
	r9_t3_mem0 += MAS_MEM[4]
	S += 22 < r9_t3_mem0
	S += r9_t3_mem0 <= r9_t3

	r9_t3_mem1 = S.Task('r9_t3_mem1', length=1, delay_cost=1)
	r9_t3_mem1 += MAS_MEM[3]
	S += 35 < r9_t3_mem1
	S += r9_t3_mem1 <= r9_t3

	r11_t0 = S.Task('r11_t0', length=1, delay_cost=1)
	r11_t0 += alt(MAS)

	r11_t0_mem0 = S.Task('r11_t0_mem0', length=1, delay_cost=1)
	r11_t0_mem0 += MAS_MEM[2]
	S += 18 < r11_t0_mem0
	S += r11_t0_mem0 <= r11_t0

	r11_t0_mem1 = S.Task('r11_t0_mem1', length=1, delay_cost=1)
	r11_t0_mem1 += MAS_MEM[9]
	S += 24 < r11_t0_mem1
	S += r11_t0_mem1 <= r11_t0

	r11_t1 = S.Task('r11_t1', length=1, delay_cost=1)
	r11_t1 += alt(MAS)

	r11_t1_mem0 = S.Task('r11_t1_mem0', length=1, delay_cost=1)
	r11_t1_mem0 += MAS_MEM[2]
	S += 18 < r11_t1_mem0
	S += r11_t1_mem0 <= r11_t1

	r11_t1_mem1 = S.Task('r11_t1_mem1', length=1, delay_cost=1)
	r11_t1_mem1 += MAS_MEM[9]
	S += 24 < r11_t1_mem1
	S += r11_t1_mem1 <= r11_t1

	r11_t3_in = S.Task('r11_t3_in', length=1, delay_cost=1)
	r11_t3_in += alt(MM_in)
	r11_t3 = S.Task('r11_t3', length=8, delay_cost=1)
	r11_t3 += alt(MM)
	S += r11_t3>=r11_t3_in

	r11_t3_mem0 = S.Task('r11_t3_mem0', length=1, delay_cost=1)
	r11_t3_mem0 += MAS_MEM[2]
	S += 18 < r11_t3_mem0
	S += r11_t3_mem0 <= r11_t3

	r11_t3_mem1 = S.Task('r11_t3_mem1', length=1, delay_cost=1)
	r11_t3_mem1 += MAS_MEM[9]
	S += 24 < r11_t3_mem1
	S += r11_t3_mem1 <= r11_t3

	X_new_t1_in = S.Task('X_new_t1_in', length=1, delay_cost=1)
	X_new_t1_in += alt(MM_in)
	X_new_t1 = S.Task('X_new_t1', length=8, delay_cost=1)
	X_new_t1 += alt(MM)
	S += X_new_t1>=X_new_t1_in

	X_new_t1_mem0 = S.Task('X_new_t1_mem0', length=1, delay_cost=1)
	X_new_t1_mem0 += MAS_MEM[2]
	S += 31 < X_new_t1_mem0
	S += X_new_t1_mem0 <= X_new_t1

	X_new_t1_mem1 = S.Task('X_new_t1_mem1', length=1, delay_cost=1)
	X_new_t1_mem1 += MAS_MEM[7]
	S += 24 < X_new_t1_mem1
	S += X_new_t1_mem1 <= X_new_t1

	X_new_t2 = S.Task('X_new_t2', length=1, delay_cost=1)
	X_new_t2 += alt(MAS)

	X_new_t2_mem0 = S.Task('X_new_t2_mem0', length=1, delay_cost=1)
	X_new_t2_mem0 += MAS_MEM[8]
	S += 16 < X_new_t2_mem0
	S += X_new_t2_mem0 <= X_new_t2

	X_new_t2_mem1 = S.Task('X_new_t2_mem1', length=1, delay_cost=1)
	X_new_t2_mem1 += MAS_MEM[3]
	S += 31 < X_new_t2_mem1
	S += X_new_t2_mem1 <= X_new_t2

	r14_t1_in = S.Task('r14_t1_in', length=1, delay_cost=1)
	r14_t1_in += alt(MM_in)
	r14_t1 = S.Task('r14_t1', length=8, delay_cost=1)
	r14_t1 += alt(MM)
	S += r14_t1>=r14_t1_in

	r14_t1_mem0 = S.Task('r14_t1_mem0', length=1, delay_cost=1)
	r14_t1_mem0 += MAS_MEM[2]
	S += 31 < r14_t1_mem0
	S += r14_t1_mem0 <= r14_t1

	r14_t1_mem1 = S.Task('r14_t1_mem1', length=1, delay_cost=1)
	r14_t1_mem1 += MAS_MEM[3]
	S += 28 < r14_t1_mem1
	S += r14_t1_mem1 <= r14_t1

	r14_t2 = S.Task('r14_t2', length=1, delay_cost=1)
	r14_t2 += alt(MAS)

	r14_t2_mem0 = S.Task('r14_t2_mem0', length=1, delay_cost=1)
	r14_t2_mem0 += MAS_MEM[8]
	S += 16 < r14_t2_mem0
	S += r14_t2_mem0 <= r14_t2

	r14_t2_mem1 = S.Task('r14_t2_mem1', length=1, delay_cost=1)
	r14_t2_mem1 += MAS_MEM[3]
	S += 31 < r14_t2_mem1
	S += r14_t2_mem1 <= r14_t2

	r15_t2 = S.Task('r15_t2', length=1, delay_cost=1)
	r15_t2 += alt(MAS)

	r15_t2_mem0 = S.Task('r15_t2_mem0', length=1, delay_cost=1)
	r15_t2_mem0 += MAS_MEM[6]
	S += 17 < r15_t2_mem0
	S += r15_t2_mem0 <= r15_t2

	r15_t2_mem1 = S.Task('r15_t2_mem1', length=1, delay_cost=1)
	r15_t2_mem1 += MAS_MEM[1]
	S += 25 < r15_t2_mem1
	S += r15_t2_mem1 <= r15_t2

	Z_new_t1_in = S.Task('Z_new_t1_in', length=1, delay_cost=1)
	Z_new_t1_in += alt(MM_in)
	Z_new_t1 = S.Task('Z_new_t1', length=8, delay_cost=1)
	Z_new_t1 += alt(MM)
	S += Z_new_t1>=Z_new_t1_in

	Z_new_t1_mem0 = S.Task('Z_new_t1_mem0', length=1, delay_cost=1)
	Z_new_t1_mem0 += MAS_MEM[2]
	S += 31 < Z_new_t1_mem0
	S += Z_new_t1_mem0 <= Z_new_t1

	Z_new_t1_mem1 = S.Task('Z_new_t1_mem1', length=1, delay_cost=1)
	Z_new_t1_mem1 += MAS_MEM[9]
	S += 26 < Z_new_t1_mem1
	S += Z_new_t1_mem1 <= Z_new_t1

	Z_new_t2 = S.Task('Z_new_t2', length=1, delay_cost=1)
	Z_new_t2 += alt(MAS)

	Z_new_t2_mem0 = S.Task('Z_new_t2_mem0', length=1, delay_cost=1)
	Z_new_t2_mem0 += MAS_MEM[8]
	S += 16 < Z_new_t2_mem0
	S += Z_new_t2_mem0 <= Z_new_t2

	Z_new_t2_mem1 = S.Task('Z_new_t2_mem1', length=1, delay_cost=1)
	Z_new_t2_mem1 += MAS_MEM[3]
	S += 31 < Z_new_t2_mem1
	S += Z_new_t2_mem1 <= Z_new_t2

	r9_t4_in = S.Task('r9_t4_in', length=1, delay_cost=1)
	r9_t4_in += alt(MM_in)
	r9_t4 = S.Task('r9_t4', length=8, delay_cost=1)
	r9_t4 += alt(MM)
	S += r9_t4>=r9_t4_in

	r9_t4_mem0 = S.Task('r9_t4_mem0', length=1, delay_cost=1)
	r9_t4_mem0 += MAS_MEM[2]
	S += 2 < r9_t4_mem0
	S += r9_t4_mem0 <= r9_t4

	r9_t4_mem1 = S.Task('r9_t4_mem1', length=1, delay_cost=1)
	r9_t4_mem1 += alt(MAS_MEM)
	S += (r9_t3*MAS[0])-1 < r9_t4_mem1*MAS_MEM[1]
	S += (r9_t3*MAS[1])-1 < r9_t4_mem1*MAS_MEM[3]
	S += (r9_t3*MAS[2])-1 < r9_t4_mem1*MAS_MEM[5]
	S += (r9_t3*MAS[3])-1 < r9_t4_mem1*MAS_MEM[7]
	S += (r9_t3*MAS[4])-1 < r9_t4_mem1*MAS_MEM[9]
	S += r9_t4_mem1 <= r9_t4

	r90 = S.Task('r90', length=1, delay_cost=1)
	r90 += alt(MAS)

	r90_mem0 = S.Task('r90_mem0', length=1, delay_cost=1)
	r90_mem0 += MM_MEM[0]
	S += 32 < r90_mem0
	S += r90_mem0 <= r90

	r90_mem1 = S.Task('r90_mem1', length=1, delay_cost=1)
	r90_mem1 += alt(MM_MEM)
	S += (r9_t1*MM[0])-1 < r90_mem1*MM_MEM[1]
	S += r90_mem1 <= r90

	r9_t5 = S.Task('r9_t5', length=1, delay_cost=1)
	r9_t5 += alt(MAS)

	r9_t5_mem0 = S.Task('r9_t5_mem0', length=1, delay_cost=1)
	r9_t5_mem0 += MM_MEM[0]
	S += 32 < r9_t5_mem0
	S += r9_t5_mem0 <= r9_t5

	r9_t5_mem1 = S.Task('r9_t5_mem1', length=1, delay_cost=1)
	r9_t5_mem1 += alt(MM_MEM)
	S += (r9_t1*MM[0])-1 < r9_t5_mem1*MM_MEM[1]
	S += r9_t5_mem1 <= r9_t5

	r11_t2_in = S.Task('r11_t2_in', length=1, delay_cost=1)
	r11_t2_in += alt(MM_in)
	r11_t2 = S.Task('r11_t2', length=8, delay_cost=1)
	r11_t2 += alt(MM)
	S += r11_t2>=r11_t2_in

	r11_t2_mem0 = S.Task('r11_t2_mem0', length=1, delay_cost=1)
	r11_t2_mem0 += alt(MAS_MEM)
	S += (r11_t0*MAS[0])-1 < r11_t2_mem0*MAS_MEM[0]
	S += (r11_t0*MAS[1])-1 < r11_t2_mem0*MAS_MEM[2]
	S += (r11_t0*MAS[2])-1 < r11_t2_mem0*MAS_MEM[4]
	S += (r11_t0*MAS[3])-1 < r11_t2_mem0*MAS_MEM[6]
	S += (r11_t0*MAS[4])-1 < r11_t2_mem0*MAS_MEM[8]
	S += r11_t2_mem0 <= r11_t2

	r11_t2_mem1 = S.Task('r11_t2_mem1', length=1, delay_cost=1)
	r11_t2_mem1 += alt(MAS_MEM)
	S += (r11_t1*MAS[0])-1 < r11_t2_mem1*MAS_MEM[1]
	S += (r11_t1*MAS[1])-1 < r11_t2_mem1*MAS_MEM[3]
	S += (r11_t1*MAS[2])-1 < r11_t2_mem1*MAS_MEM[5]
	S += (r11_t1*MAS[3])-1 < r11_t2_mem1*MAS_MEM[7]
	S += (r11_t1*MAS[4])-1 < r11_t2_mem1*MAS_MEM[9]
	S += r11_t2_mem1 <= r11_t2

	r11_t5 = S.Task('r11_t5', length=1, delay_cost=1)
	r11_t5 += alt(MAS)

	r11_t5_mem0 = S.Task('r11_t5_mem0', length=1, delay_cost=1)
	r11_t5_mem0 += alt(MM_MEM)
	S += (r11_t3*MM[0])-1 < r11_t5_mem0*MM_MEM[0]
	S += r11_t5_mem0 <= r11_t5

	r111 = S.Task('r111', length=1, delay_cost=1)
	r111 += alt(MAS)

	r111_mem0 = S.Task('r111_mem0', length=1, delay_cost=1)
	r111_mem0 += alt(MM_MEM)
	S += (r11_t3*MM[0])-1 < r111_mem0*MM_MEM[0]
	S += r111_mem0 <= r111

	X_new_t4_in = S.Task('X_new_t4_in', length=1, delay_cost=1)
	X_new_t4_in += alt(MM_in)
	X_new_t4 = S.Task('X_new_t4', length=8, delay_cost=1)
	X_new_t4 += alt(MM)
	S += X_new_t4>=X_new_t4_in

	X_new_t4_mem0 = S.Task('X_new_t4_mem0', length=1, delay_cost=1)
	X_new_t4_mem0 += alt(MAS_MEM)
	S += (X_new_t2*MAS[0])-1 < X_new_t4_mem0*MAS_MEM[0]
	S += (X_new_t2*MAS[1])-1 < X_new_t4_mem0*MAS_MEM[2]
	S += (X_new_t2*MAS[2])-1 < X_new_t4_mem0*MAS_MEM[4]
	S += (X_new_t2*MAS[3])-1 < X_new_t4_mem0*MAS_MEM[6]
	S += (X_new_t2*MAS[4])-1 < X_new_t4_mem0*MAS_MEM[8]
	S += X_new_t4_mem0 <= X_new_t4

	X_new_t4_mem1 = S.Task('X_new_t4_mem1', length=1, delay_cost=1)
	X_new_t4_mem1 += MAS_MEM[7]
	S += 25 < X_new_t4_mem1
	S += X_new_t4_mem1 <= X_new_t4

	X_new0 = S.Task('X_new0', length=1, delay_cost=1)
	X_new0 += alt(MAS)

	S += 0<X_new0

	X_new0_w = S.Task('X_new0_w', length=1, delay_cost=1)
	X_new0_w += alt(MAIN_MEM_w)
	S += X_new0 <= X_new0_w

	X_new0_mem0 = S.Task('X_new0_mem0', length=1, delay_cost=1)
	X_new0_mem0 += MM_MEM[0]
	S += 29 < X_new0_mem0
	S += X_new0_mem0 <= X_new0

	X_new0_mem1 = S.Task('X_new0_mem1', length=1, delay_cost=1)
	X_new0_mem1 += alt(MM_MEM)
	S += (X_new_t1*MM[0])-1 < X_new0_mem1*MM_MEM[1]
	S += X_new0_mem1 <= X_new0

	X_new_t5 = S.Task('X_new_t5', length=1, delay_cost=1)
	X_new_t5 += alt(MAS)

	X_new_t5_mem0 = S.Task('X_new_t5_mem0', length=1, delay_cost=1)
	X_new_t5_mem0 += MM_MEM[0]
	S += 29 < X_new_t5_mem0
	S += X_new_t5_mem0 <= X_new_t5

	X_new_t5_mem1 = S.Task('X_new_t5_mem1', length=1, delay_cost=1)
	X_new_t5_mem1 += alt(MM_MEM)
	S += (X_new_t1*MM[0])-1 < X_new_t5_mem1*MM_MEM[1]
	S += X_new_t5_mem1 <= X_new_t5

	r14_t4_in = S.Task('r14_t4_in', length=1, delay_cost=1)
	r14_t4_in += alt(MM_in)
	r14_t4 = S.Task('r14_t4', length=8, delay_cost=1)
	r14_t4 += alt(MM)
	S += r14_t4>=r14_t4_in

	r14_t4_mem0 = S.Task('r14_t4_mem0', length=1, delay_cost=1)
	r14_t4_mem0 += alt(MAS_MEM)
	S += (r14_t2*MAS[0])-1 < r14_t4_mem0*MAS_MEM[0]
	S += (r14_t2*MAS[1])-1 < r14_t4_mem0*MAS_MEM[2]
	S += (r14_t2*MAS[2])-1 < r14_t4_mem0*MAS_MEM[4]
	S += (r14_t2*MAS[3])-1 < r14_t4_mem0*MAS_MEM[6]
	S += (r14_t2*MAS[4])-1 < r14_t4_mem0*MAS_MEM[8]
	S += r14_t4_mem0 <= r14_t4

	r14_t4_mem1 = S.Task('r14_t4_mem1', length=1, delay_cost=1)
	r14_t4_mem1 += MAS_MEM[5]
	S += 29 < r14_t4_mem1
	S += r14_t4_mem1 <= r14_t4

	r140 = S.Task('r140', length=1, delay_cost=1)
	r140 += alt(MAS)

	r140_mem0 = S.Task('r140_mem0', length=1, delay_cost=1)
	r140_mem0 += MM_MEM[0]
	S += 27 < r140_mem0
	S += r140_mem0 <= r140

	r140_mem1 = S.Task('r140_mem1', length=1, delay_cost=1)
	r140_mem1 += alt(MM_MEM)
	S += (r14_t1*MM[0])-1 < r140_mem1*MM_MEM[1]
	S += r140_mem1 <= r140

	r14_t5 = S.Task('r14_t5', length=1, delay_cost=1)
	r14_t5 += alt(MAS)

	r14_t5_mem0 = S.Task('r14_t5_mem0', length=1, delay_cost=1)
	r14_t5_mem0 += MM_MEM[0]
	S += 27 < r14_t5_mem0
	S += r14_t5_mem0 <= r14_t5

	r14_t5_mem1 = S.Task('r14_t5_mem1', length=1, delay_cost=1)
	r14_t5_mem1 += alt(MM_MEM)
	S += (r14_t1*MM[0])-1 < r14_t5_mem1*MM_MEM[1]
	S += r14_t5_mem1 <= r14_t5

	Z_new_t4_in = S.Task('Z_new_t4_in', length=1, delay_cost=1)
	Z_new_t4_in += alt(MM_in)
	Z_new_t4 = S.Task('Z_new_t4', length=8, delay_cost=1)
	Z_new_t4 += alt(MM)
	S += Z_new_t4>=Z_new_t4_in

	Z_new_t4_mem0 = S.Task('Z_new_t4_mem0', length=1, delay_cost=1)
	Z_new_t4_mem0 += alt(MAS_MEM)
	S += (Z_new_t2*MAS[0])-1 < Z_new_t4_mem0*MAS_MEM[0]
	S += (Z_new_t2*MAS[1])-1 < Z_new_t4_mem0*MAS_MEM[2]
	S += (Z_new_t2*MAS[2])-1 < Z_new_t4_mem0*MAS_MEM[4]
	S += (Z_new_t2*MAS[3])-1 < Z_new_t4_mem0*MAS_MEM[6]
	S += (Z_new_t2*MAS[4])-1 < Z_new_t4_mem0*MAS_MEM[8]
	S += Z_new_t4_mem0 <= Z_new_t4

	Z_new_t4_mem1 = S.Task('Z_new_t4_mem1', length=1, delay_cost=1)
	Z_new_t4_mem1 += MAS_MEM[7]
	S += 27 < Z_new_t4_mem1
	S += Z_new_t4_mem1 <= Z_new_t4

	Z_new0 = S.Task('Z_new0', length=1, delay_cost=1)
	Z_new0 += alt(MAS)

	S += 0<Z_new0

	Z_new0_w = S.Task('Z_new0_w', length=1, delay_cost=1)
	Z_new0_w += alt(MAIN_MEM_w)
	S += Z_new0 <= Z_new0_w

	Z_new0_mem0 = S.Task('Z_new0_mem0', length=1, delay_cost=1)
	Z_new0_mem0 += MM_MEM[0]
	S += 30 < Z_new0_mem0
	S += Z_new0_mem0 <= Z_new0

	Z_new0_mem1 = S.Task('Z_new0_mem1', length=1, delay_cost=1)
	Z_new0_mem1 += alt(MM_MEM)
	S += (Z_new_t1*MM[0])-1 < Z_new0_mem1*MM_MEM[1]
	S += Z_new0_mem1 <= Z_new0

	Z_new_t5 = S.Task('Z_new_t5', length=1, delay_cost=1)
	Z_new_t5 += alt(MAS)

	Z_new_t5_mem0 = S.Task('Z_new_t5_mem0', length=1, delay_cost=1)
	Z_new_t5_mem0 += MM_MEM[0]
	S += 30 < Z_new_t5_mem0
	S += Z_new_t5_mem0 <= Z_new_t5

	Z_new_t5_mem1 = S.Task('Z_new_t5_mem1', length=1, delay_cost=1)
	Z_new_t5_mem1 += alt(MM_MEM)
	S += (Z_new_t1*MM[0])-1 < Z_new_t5_mem1*MM_MEM[1]
	S += Z_new_t5_mem1 <= Z_new_t5

	r91 = S.Task('r91', length=1, delay_cost=1)
	r91 += alt(MAS)

	r91_mem0 = S.Task('r91_mem0', length=1, delay_cost=1)
	r91_mem0 += alt(MM_MEM)
	S += (r9_t4*MM[0])-1 < r91_mem0*MM_MEM[0]
	S += r91_mem0 <= r91

	r91_mem1 = S.Task('r91_mem1', length=1, delay_cost=1)
	r91_mem1 += alt(MAS_MEM)
	S += (r9_t5*MAS[0])-1 < r91_mem1*MAS_MEM[1]
	S += (r9_t5*MAS[1])-1 < r91_mem1*MAS_MEM[3]
	S += (r9_t5*MAS[2])-1 < r91_mem1*MAS_MEM[5]
	S += (r9_t5*MAS[3])-1 < r91_mem1*MAS_MEM[7]
	S += (r9_t5*MAS[4])-1 < r91_mem1*MAS_MEM[9]
	S += r91_mem1 <= r91

	r110 = S.Task('r110', length=1, delay_cost=1)
	r110 += alt(MAS)

	r110_mem0 = S.Task('r110_mem0', length=1, delay_cost=1)
	r110_mem0 += alt(MM_MEM)
	S += (r11_t2*MM[0])-1 < r110_mem0*MM_MEM[0]
	S += r110_mem0 <= r110

	r110_mem1 = S.Task('r110_mem1', length=1, delay_cost=1)
	r110_mem1 += alt(MAS_MEM)
	S += (r11_t5*MAS[0])-1 < r110_mem1*MAS_MEM[1]
	S += (r11_t5*MAS[1])-1 < r110_mem1*MAS_MEM[3]
	S += (r11_t5*MAS[2])-1 < r110_mem1*MAS_MEM[5]
	S += (r11_t5*MAS[3])-1 < r110_mem1*MAS_MEM[7]
	S += (r11_t5*MAS[4])-1 < r110_mem1*MAS_MEM[9]
	S += r110_mem1 <= r110

	X_new1 = S.Task('X_new1', length=1, delay_cost=1)
	X_new1 += alt(MAS)

	S += 0<X_new1

	X_new1_w = S.Task('X_new1_w', length=1, delay_cost=1)
	X_new1_w += alt(MAIN_MEM_w)
	S += X_new1 <= X_new1_w

	X_new1_mem0 = S.Task('X_new1_mem0', length=1, delay_cost=1)
	X_new1_mem0 += alt(MM_MEM)
	S += (X_new_t4*MM[0])-1 < X_new1_mem0*MM_MEM[0]
	S += X_new1_mem0 <= X_new1

	X_new1_mem1 = S.Task('X_new1_mem1', length=1, delay_cost=1)
	X_new1_mem1 += alt(MAS_MEM)
	S += (X_new_t5*MAS[0])-1 < X_new1_mem1*MAS_MEM[1]
	S += (X_new_t5*MAS[1])-1 < X_new1_mem1*MAS_MEM[3]
	S += (X_new_t5*MAS[2])-1 < X_new1_mem1*MAS_MEM[5]
	S += (X_new_t5*MAS[3])-1 < X_new1_mem1*MAS_MEM[7]
	S += (X_new_t5*MAS[4])-1 < X_new1_mem1*MAS_MEM[9]
	S += X_new1_mem1 <= X_new1

	r141 = S.Task('r141', length=1, delay_cost=1)
	r141 += alt(MAS)

	r141_mem0 = S.Task('r141_mem0', length=1, delay_cost=1)
	r141_mem0 += alt(MM_MEM)
	S += (r14_t4*MM[0])-1 < r141_mem0*MM_MEM[0]
	S += r141_mem0 <= r141

	r141_mem1 = S.Task('r141_mem1', length=1, delay_cost=1)
	r141_mem1 += alt(MAS_MEM)
	S += (r14_t5*MAS[0])-1 < r141_mem1*MAS_MEM[1]
	S += (r14_t5*MAS[1])-1 < r141_mem1*MAS_MEM[3]
	S += (r14_t5*MAS[2])-1 < r141_mem1*MAS_MEM[5]
	S += (r14_t5*MAS[3])-1 < r141_mem1*MAS_MEM[7]
	S += (r14_t5*MAS[4])-1 < r141_mem1*MAS_MEM[9]
	S += r141_mem1 <= r141

	r15_t0_in = S.Task('r15_t0_in', length=1, delay_cost=1)
	r15_t0_in += alt(MM_in)
	r15_t0 = S.Task('r15_t0', length=8, delay_cost=1)
	r15_t0 += alt(MM)
	S += r15_t0>=r15_t0_in

	r15_t0_mem0 = S.Task('r15_t0_mem0', length=1, delay_cost=1)
	r15_t0_mem0 += MAS_MEM[6]
	S += 17 < r15_t0_mem0
	S += r15_t0_mem0 <= r15_t0

	r15_t0_mem1 = S.Task('r15_t0_mem1', length=1, delay_cost=1)
	r15_t0_mem1 += alt(MAS_MEM)
	S += (r90*MAS[0])-1 < r15_t0_mem1*MAS_MEM[1]
	S += (r90*MAS[1])-1 < r15_t0_mem1*MAS_MEM[3]
	S += (r90*MAS[2])-1 < r15_t0_mem1*MAS_MEM[5]
	S += (r90*MAS[3])-1 < r15_t0_mem1*MAS_MEM[7]
	S += (r90*MAS[4])-1 < r15_t0_mem1*MAS_MEM[9]
	S += r15_t0_mem1 <= r15_t0

	r16_t1_in = S.Task('r16_t1_in', length=1, delay_cost=1)
	r16_t1_in += alt(MM_in)
	r16_t1 = S.Task('r16_t1', length=8, delay_cost=1)
	r16_t1 += alt(MM)
	S += r16_t1>=r16_t1_in

	r16_t1_mem0 = S.Task('r16_t1_mem0', length=1, delay_cost=1)
	r16_t1_mem0 += alt(MAS_MEM)
	S += (r111*MAS[0])-1 < r16_t1_mem0*MAS_MEM[0]
	S += (r111*MAS[1])-1 < r16_t1_mem0*MAS_MEM[2]
	S += (r111*MAS[2])-1 < r16_t1_mem0*MAS_MEM[4]
	S += (r111*MAS[3])-1 < r16_t1_mem0*MAS_MEM[6]
	S += (r111*MAS[4])-1 < r16_t1_mem0*MAS_MEM[8]
	S += r16_t1_mem0 <= r16_t1

	r16_t1_mem1 = S.Task('r16_t1_mem1', length=1, delay_cost=1)
	r16_t1_mem1 += MAIN_MEM_r[1]
	Z_new1 = S.Task('Z_new1', length=1, delay_cost=1)
	Z_new1 += alt(MAS)

	S += 0<Z_new1

	Z_new1_w = S.Task('Z_new1_w', length=1, delay_cost=1)
	Z_new1_w += alt(MAIN_MEM_w)
	S += Z_new1 <= Z_new1_w

	Z_new1_mem0 = S.Task('Z_new1_mem0', length=1, delay_cost=1)
	Z_new1_mem0 += alt(MM_MEM)
	S += (Z_new_t4*MM[0])-1 < Z_new1_mem0*MM_MEM[0]
	S += Z_new1_mem0 <= Z_new1

	Z_new1_mem1 = S.Task('Z_new1_mem1', length=1, delay_cost=1)
	Z_new1_mem1 += alt(MAS_MEM)
	S += (Z_new_t5*MAS[0])-1 < Z_new1_mem1*MAS_MEM[1]
	S += (Z_new_t5*MAS[1])-1 < Z_new1_mem1*MAS_MEM[3]
	S += (Z_new_t5*MAS[2])-1 < Z_new1_mem1*MAS_MEM[5]
	S += (Z_new_t5*MAS[3])-1 < Z_new1_mem1*MAS_MEM[7]
	S += (Z_new_t5*MAS[4])-1 < Z_new1_mem1*MAS_MEM[9]
	S += Z_new1_mem1 <= Z_new1

	r15_t1_in = S.Task('r15_t1_in', length=1, delay_cost=1)
	r15_t1_in += alt(MM_in)
	r15_t1 = S.Task('r15_t1', length=8, delay_cost=1)
	r15_t1 += alt(MM)
	S += r15_t1>=r15_t1_in

	r15_t1_mem0 = S.Task('r15_t1_mem0', length=1, delay_cost=1)
	r15_t1_mem0 += MAS_MEM[0]
	S += 25 < r15_t1_mem0
	S += r15_t1_mem0 <= r15_t1

	r15_t1_mem1 = S.Task('r15_t1_mem1', length=1, delay_cost=1)
	r15_t1_mem1 += alt(MAS_MEM)
	S += (r91*MAS[0])-1 < r15_t1_mem1*MAS_MEM[1]
	S += (r91*MAS[1])-1 < r15_t1_mem1*MAS_MEM[3]
	S += (r91*MAS[2])-1 < r15_t1_mem1*MAS_MEM[5]
	S += (r91*MAS[3])-1 < r15_t1_mem1*MAS_MEM[7]
	S += (r91*MAS[4])-1 < r15_t1_mem1*MAS_MEM[9]
	S += r15_t1_mem1 <= r15_t1

	r15_t3 = S.Task('r15_t3', length=1, delay_cost=1)
	r15_t3 += alt(MAS)

	r15_t3_mem0 = S.Task('r15_t3_mem0', length=1, delay_cost=1)
	r15_t3_mem0 += alt(MAS_MEM)
	S += (r90*MAS[0])-1 < r15_t3_mem0*MAS_MEM[0]
	S += (r90*MAS[1])-1 < r15_t3_mem0*MAS_MEM[2]
	S += (r90*MAS[2])-1 < r15_t3_mem0*MAS_MEM[4]
	S += (r90*MAS[3])-1 < r15_t3_mem0*MAS_MEM[6]
	S += (r90*MAS[4])-1 < r15_t3_mem0*MAS_MEM[8]
	S += r15_t3_mem0 <= r15_t3

	r15_t3_mem1 = S.Task('r15_t3_mem1', length=1, delay_cost=1)
	r15_t3_mem1 += alt(MAS_MEM)
	S += (r91*MAS[0])-1 < r15_t3_mem1*MAS_MEM[1]
	S += (r91*MAS[1])-1 < r15_t3_mem1*MAS_MEM[3]
	S += (r91*MAS[2])-1 < r15_t3_mem1*MAS_MEM[5]
	S += (r91*MAS[3])-1 < r15_t3_mem1*MAS_MEM[7]
	S += (r91*MAS[4])-1 < r15_t3_mem1*MAS_MEM[9]
	S += r15_t3_mem1 <= r15_t3

	r16_t0_in = S.Task('r16_t0_in', length=1, delay_cost=1)
	r16_t0_in += alt(MM_in)
	r16_t0 = S.Task('r16_t0', length=8, delay_cost=1)
	r16_t0 += alt(MM)
	S += r16_t0>=r16_t0_in

	r16_t0_mem0 = S.Task('r16_t0_mem0', length=1, delay_cost=1)
	r16_t0_mem0 += alt(MAS_MEM)
	S += (r110*MAS[0])-1 < r16_t0_mem0*MAS_MEM[0]
	S += (r110*MAS[1])-1 < r16_t0_mem0*MAS_MEM[2]
	S += (r110*MAS[2])-1 < r16_t0_mem0*MAS_MEM[4]
	S += (r110*MAS[3])-1 < r16_t0_mem0*MAS_MEM[6]
	S += (r110*MAS[4])-1 < r16_t0_mem0*MAS_MEM[8]
	S += r16_t0_mem0 <= r16_t0

	r16_t0_mem1 = S.Task('r16_t0_mem1', length=1, delay_cost=1)
	r16_t0_mem1 += MAIN_MEM_r[1]
	r16_t2 = S.Task('r16_t2', length=1, delay_cost=1)
	r16_t2 += alt(MAS)

	r16_t2_mem0 = S.Task('r16_t2_mem0', length=1, delay_cost=1)
	r16_t2_mem0 += alt(MAS_MEM)
	S += (r110*MAS[0])-1 < r16_t2_mem0*MAS_MEM[0]
	S += (r110*MAS[1])-1 < r16_t2_mem0*MAS_MEM[2]
	S += (r110*MAS[2])-1 < r16_t2_mem0*MAS_MEM[4]
	S += (r110*MAS[3])-1 < r16_t2_mem0*MAS_MEM[6]
	S += (r110*MAS[4])-1 < r16_t2_mem0*MAS_MEM[8]
	S += r16_t2_mem0 <= r16_t2

	r16_t2_mem1 = S.Task('r16_t2_mem1', length=1, delay_cost=1)
	r16_t2_mem1 += alt(MAS_MEM)
	S += (r111*MAS[0])-1 < r16_t2_mem1*MAS_MEM[1]
	S += (r111*MAS[1])-1 < r16_t2_mem1*MAS_MEM[3]
	S += (r111*MAS[2])-1 < r16_t2_mem1*MAS_MEM[5]
	S += (r111*MAS[3])-1 < r16_t2_mem1*MAS_MEM[7]
	S += (r111*MAS[4])-1 < r16_t2_mem1*MAS_MEM[9]
	S += r16_t2_mem1 <= r16_t2

	r15_t4_in = S.Task('r15_t4_in', length=1, delay_cost=1)
	r15_t4_in += alt(MM_in)
	r15_t4 = S.Task('r15_t4', length=8, delay_cost=1)
	r15_t4 += alt(MM)
	S += r15_t4>=r15_t4_in

	r15_t4_mem0 = S.Task('r15_t4_mem0', length=1, delay_cost=1)
	r15_t4_mem0 += alt(MAS_MEM)
	S += (r15_t2*MAS[0])-1 < r15_t4_mem0*MAS_MEM[0]
	S += (r15_t2*MAS[1])-1 < r15_t4_mem0*MAS_MEM[2]
	S += (r15_t2*MAS[2])-1 < r15_t4_mem0*MAS_MEM[4]
	S += (r15_t2*MAS[3])-1 < r15_t4_mem0*MAS_MEM[6]
	S += (r15_t2*MAS[4])-1 < r15_t4_mem0*MAS_MEM[8]
	S += r15_t4_mem0 <= r15_t4

	r15_t4_mem1 = S.Task('r15_t4_mem1', length=1, delay_cost=1)
	r15_t4_mem1 += alt(MAS_MEM)
	S += (r15_t3*MAS[0])-1 < r15_t4_mem1*MAS_MEM[1]
	S += (r15_t3*MAS[1])-1 < r15_t4_mem1*MAS_MEM[3]
	S += (r15_t3*MAS[2])-1 < r15_t4_mem1*MAS_MEM[5]
	S += (r15_t3*MAS[3])-1 < r15_t4_mem1*MAS_MEM[7]
	S += (r15_t3*MAS[4])-1 < r15_t4_mem1*MAS_MEM[9]
	S += r15_t4_mem1 <= r15_t4

	r150 = S.Task('r150', length=1, delay_cost=1)
	r150 += alt(MAS)

	r150_mem0 = S.Task('r150_mem0', length=1, delay_cost=1)
	r150_mem0 += alt(MM_MEM)
	S += (r15_t0*MM[0])-1 < r150_mem0*MM_MEM[0]
	S += r150_mem0 <= r150

	r150_mem1 = S.Task('r150_mem1', length=1, delay_cost=1)
	r150_mem1 += alt(MM_MEM)
	S += (r15_t1*MM[0])-1 < r150_mem1*MM_MEM[1]
	S += r150_mem1 <= r150

	r15_t5 = S.Task('r15_t5', length=1, delay_cost=1)
	r15_t5 += alt(MAS)

	r15_t5_mem0 = S.Task('r15_t5_mem0', length=1, delay_cost=1)
	r15_t5_mem0 += alt(MM_MEM)
	S += (r15_t0*MM[0])-1 < r15_t5_mem0*MM_MEM[0]
	S += r15_t5_mem0 <= r15_t5

	r15_t5_mem1 = S.Task('r15_t5_mem1', length=1, delay_cost=1)
	r15_t5_mem1 += alt(MM_MEM)
	S += (r15_t1*MM[0])-1 < r15_t5_mem1*MM_MEM[1]
	S += r15_t5_mem1 <= r15_t5

	r16_t4_in = S.Task('r16_t4_in', length=1, delay_cost=1)
	r16_t4_in += alt(MM_in)
	r16_t4 = S.Task('r16_t4', length=8, delay_cost=1)
	r16_t4 += alt(MM)
	S += r16_t4>=r16_t4_in

	r16_t4_mem0 = S.Task('r16_t4_mem0', length=1, delay_cost=1)
	r16_t4_mem0 += alt(MAS_MEM)
	S += (r16_t2*MAS[0])-1 < r16_t4_mem0*MAS_MEM[0]
	S += (r16_t2*MAS[1])-1 < r16_t4_mem0*MAS_MEM[2]
	S += (r16_t2*MAS[2])-1 < r16_t4_mem0*MAS_MEM[4]
	S += (r16_t2*MAS[3])-1 < r16_t4_mem0*MAS_MEM[6]
	S += (r16_t2*MAS[4])-1 < r16_t4_mem0*MAS_MEM[8]
	S += r16_t4_mem0 <= r16_t4

	r16_t4_mem1 = S.Task('r16_t4_mem1', length=1, delay_cost=1)
	r16_t4_mem1 += MAS_MEM[7]
	S += 1 < r16_t4_mem1
	S += r16_t4_mem1 <= r16_t4

	r160 = S.Task('r160', length=1, delay_cost=1)
	r160 += alt(MAS)

	r160_mem0 = S.Task('r160_mem0', length=1, delay_cost=1)
	r160_mem0 += alt(MM_MEM)
	S += (r16_t0*MM[0])-1 < r160_mem0*MM_MEM[0]
	S += r160_mem0 <= r160

	r160_mem1 = S.Task('r160_mem1', length=1, delay_cost=1)
	r160_mem1 += alt(MM_MEM)
	S += (r16_t1*MM[0])-1 < r160_mem1*MM_MEM[1]
	S += r160_mem1 <= r160

	r16_t5 = S.Task('r16_t5', length=1, delay_cost=1)
	r16_t5 += alt(MAS)

	r16_t5_mem0 = S.Task('r16_t5_mem0', length=1, delay_cost=1)
	r16_t5_mem0 += alt(MM_MEM)
	S += (r16_t0*MM[0])-1 < r16_t5_mem0*MM_MEM[0]
	S += r16_t5_mem0 <= r16_t5

	r16_t5_mem1 = S.Task('r16_t5_mem1', length=1, delay_cost=1)
	r16_t5_mem1 += alt(MM_MEM)
	S += (r16_t1*MM[0])-1 < r16_t5_mem1*MM_MEM[1]
	S += r16_t5_mem1 <= r16_t5

	r151 = S.Task('r151', length=1, delay_cost=1)
	r151 += alt(MAS)

	r151_mem0 = S.Task('r151_mem0', length=1, delay_cost=1)
	r151_mem0 += alt(MM_MEM)
	S += (r15_t4*MM[0])-1 < r151_mem0*MM_MEM[0]
	S += r151_mem0 <= r151

	r151_mem1 = S.Task('r151_mem1', length=1, delay_cost=1)
	r151_mem1 += alt(MAS_MEM)
	S += (r15_t5*MAS[0])-1 < r151_mem1*MAS_MEM[1]
	S += (r15_t5*MAS[1])-1 < r151_mem1*MAS_MEM[3]
	S += (r15_t5*MAS[2])-1 < r151_mem1*MAS_MEM[5]
	S += (r15_t5*MAS[3])-1 < r151_mem1*MAS_MEM[7]
	S += (r15_t5*MAS[4])-1 < r151_mem1*MAS_MEM[9]
	S += r151_mem1 <= r151

	r161 = S.Task('r161', length=1, delay_cost=1)
	r161 += alt(MAS)

	r161_mem0 = S.Task('r161_mem0', length=1, delay_cost=1)
	r161_mem0 += alt(MM_MEM)
	S += (r16_t4*MM[0])-1 < r161_mem0*MM_MEM[0]
	S += r161_mem0 <= r161

	r161_mem1 = S.Task('r161_mem1', length=1, delay_cost=1)
	r161_mem1 += alt(MAS_MEM)
	S += (r16_t5*MAS[0])-1 < r161_mem1*MAS_MEM[1]
	S += (r16_t5*MAS[1])-1 < r161_mem1*MAS_MEM[3]
	S += (r16_t5*MAS[2])-1 < r161_mem1*MAS_MEM[5]
	S += (r16_t5*MAS[3])-1 < r161_mem1*MAS_MEM[7]
	S += (r16_t5*MAS[4])-1 < r161_mem1*MAS_MEM[9]
	S += r161_mem1 <= r161

	r170 = S.Task('r170', length=1, delay_cost=1)
	r170 += alt(MAS)

	r170_mem0 = S.Task('r170_mem0', length=1, delay_cost=1)
	r170_mem0 += alt(MAS_MEM)
	S += (r140*MAS[0])-1 < r170_mem0*MAS_MEM[0]
	S += (r140*MAS[1])-1 < r170_mem0*MAS_MEM[2]
	S += (r140*MAS[2])-1 < r170_mem0*MAS_MEM[4]
	S += (r140*MAS[3])-1 < r170_mem0*MAS_MEM[6]
	S += (r140*MAS[4])-1 < r170_mem0*MAS_MEM[8]
	S += r170_mem0 <= r170

	r170_mem1 = S.Task('r170_mem1', length=1, delay_cost=1)
	r170_mem1 += alt(MAS_MEM)
	S += (r150*MAS[0])-1 < r170_mem1*MAS_MEM[1]
	S += (r150*MAS[1])-1 < r170_mem1*MAS_MEM[3]
	S += (r150*MAS[2])-1 < r170_mem1*MAS_MEM[5]
	S += (r150*MAS[3])-1 < r170_mem1*MAS_MEM[7]
	S += (r150*MAS[4])-1 < r170_mem1*MAS_MEM[9]
	S += r170_mem1 <= r170

	r171 = S.Task('r171', length=1, delay_cost=1)
	r171 += alt(MAS)

	r171_mem0 = S.Task('r171_mem0', length=1, delay_cost=1)
	r171_mem0 += alt(MAS_MEM)
	S += (r141*MAS[0])-1 < r171_mem0*MAS_MEM[0]
	S += (r141*MAS[1])-1 < r171_mem0*MAS_MEM[2]
	S += (r141*MAS[2])-1 < r171_mem0*MAS_MEM[4]
	S += (r141*MAS[3])-1 < r171_mem0*MAS_MEM[6]
	S += (r141*MAS[4])-1 < r171_mem0*MAS_MEM[8]
	S += r171_mem0 <= r171

	r171_mem1 = S.Task('r171_mem1', length=1, delay_cost=1)
	r171_mem1 += alt(MAS_MEM)
	S += (r151*MAS[0])-1 < r171_mem1*MAS_MEM[1]
	S += (r151*MAS[1])-1 < r171_mem1*MAS_MEM[3]
	S += (r151*MAS[2])-1 < r171_mem1*MAS_MEM[5]
	S += (r151*MAS[3])-1 < r171_mem1*MAS_MEM[7]
	S += (r151*MAS[4])-1 < r171_mem1*MAS_MEM[9]
	S += r171_mem1 <= r171

	Y_new0 = S.Task('Y_new0', length=1, delay_cost=1)
	Y_new0 += alt(MAS)

	S += 0<Y_new0

	Y_new0_w = S.Task('Y_new0_w', length=1, delay_cost=1)
	Y_new0_w += alt(MAIN_MEM_w)
	S += Y_new0 <= Y_new0_w

	Y_new0_mem0 = S.Task('Y_new0_mem0', length=1, delay_cost=1)
	Y_new0_mem0 += alt(MAS_MEM)
	S += (r170*MAS[0])-1 < Y_new0_mem0*MAS_MEM[0]
	S += (r170*MAS[1])-1 < Y_new0_mem0*MAS_MEM[2]
	S += (r170*MAS[2])-1 < Y_new0_mem0*MAS_MEM[4]
	S += (r170*MAS[3])-1 < Y_new0_mem0*MAS_MEM[6]
	S += (r170*MAS[4])-1 < Y_new0_mem0*MAS_MEM[8]
	S += Y_new0_mem0 <= Y_new0

	Y_new0_mem1 = S.Task('Y_new0_mem1', length=1, delay_cost=1)
	Y_new0_mem1 += alt(MAS_MEM)
	S += (r160*MAS[0])-1 < Y_new0_mem1*MAS_MEM[1]
	S += (r160*MAS[1])-1 < Y_new0_mem1*MAS_MEM[3]
	S += (r160*MAS[2])-1 < Y_new0_mem1*MAS_MEM[5]
	S += (r160*MAS[3])-1 < Y_new0_mem1*MAS_MEM[7]
	S += (r160*MAS[4])-1 < Y_new0_mem1*MAS_MEM[9]
	S += Y_new0_mem1 <= Y_new0

	Y_new1 = S.Task('Y_new1', length=1, delay_cost=1)
	Y_new1 += alt(MAS)

	S += 0<Y_new1

	Y_new1_w = S.Task('Y_new1_w', length=1, delay_cost=1)
	Y_new1_w += alt(MAIN_MEM_w)
	S += Y_new1 <= Y_new1_w

	Y_new1_mem0 = S.Task('Y_new1_mem0', length=1, delay_cost=1)
	Y_new1_mem0 += alt(MAS_MEM)
	S += (r171*MAS[0])-1 < Y_new1_mem0*MAS_MEM[0]
	S += (r171*MAS[1])-1 < Y_new1_mem0*MAS_MEM[2]
	S += (r171*MAS[2])-1 < Y_new1_mem0*MAS_MEM[4]
	S += (r171*MAS[3])-1 < Y_new1_mem0*MAS_MEM[6]
	S += (r171*MAS[4])-1 < Y_new1_mem0*MAS_MEM[8]
	S += Y_new1_mem0 <= Y_new1

	Y_new1_mem1 = S.Task('Y_new1_mem1', length=1, delay_cost=1)
	Y_new1_mem1 += alt(MAS_MEM)
	S += (r161*MAS[0])-1 < Y_new1_mem1*MAS_MEM[1]
	S += (r161*MAS[1])-1 < Y_new1_mem1*MAS_MEM[3]
	S += (r161*MAS[2])-1 < Y_new1_mem1*MAS_MEM[5]
	S += (r161*MAS[3])-1 < Y_new1_mem1*MAS_MEM[7]
	S += (r161*MAS[4])-1 < Y_new1_mem1*MAS_MEM[9]
	S += Y_new1_mem1 <= Y_new1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage1MAS5/EP2_YRECOVER/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

