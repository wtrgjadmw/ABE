from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 145
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=6)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	S += t3_t1_in >= 0
	t3_t1_in += MM_in[1]

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_mem0 >= 0
	t3_t1_mem0 += MAIN_MEM_r[0]

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_mem1 >= 0
	t3_t1_mem1 += MAIN_MEM_r[1]

	t3_t1 = S.Task('t3_t1', length=6, delay_cost=1)
	S += t3_t1 >= 1
	t3_t1 += MM[1]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 1
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 1
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 1
	t7_t0_mem1 += MAIN_MEM_r[1]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 2
	t6_t0_in += MM_in[1]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 2
	t6_t0_mem0 += MAIN_MEM_r[0]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 2
	t6_t0_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=6, delay_cost=1)
	S += t7_t0 >= 2
	t7_t0 += MM[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 3
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 3
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 3
	t0_t3_mem1 += MAIN_MEM_r[1]

	t6_t0 = S.Task('t6_t0', length=6, delay_cost=1)
	S += t6_t0 >= 3
	t6_t0 += MM[1]

	t0_t3 = S.Task('t0_t3', length=6, delay_cost=1)
	S += t0_t3 >= 4
	t0_t3 += MM[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 4
	t6_t1_in += MM_in[1]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 4
	t6_t1_mem0 += MAIN_MEM_r[0]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 4
	t6_t1_mem1 += MAIN_MEM_r[1]

	t6_t1 = S.Task('t6_t1', length=6, delay_cost=1)
	S += t6_t1 >= 5
	t6_t1 += MM[1]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 5
	t7_t1_in += MM_in[1]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 5
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 5
	t7_t1_mem1 += MAIN_MEM_r[1]

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	S += t3_t0_in >= 6
	t3_t0_in += MM_in[1]

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_mem0 >= 6
	t3_t0_mem0 += MAIN_MEM_r[0]

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_mem1 >= 6
	t3_t0_mem1 += MAIN_MEM_r[1]

	t7_t1 = S.Task('t7_t1', length=6, delay_cost=1)
	S += t7_t1 >= 6
	t7_t1 += MM[1]

	t3_t0 = S.Task('t3_t0', length=6, delay_cost=1)
	S += t3_t0 >= 7
	t3_t0 += MM[1]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 7
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 7
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 7
	t5_t1_mem1 += MAIN_MEM_r[1]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 8
	t5_t0_in += MM_in[1]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 8
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 8
	t5_t0_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=6, delay_cost=1)
	S += t5_t1 >= 8
	t5_t1 += MM[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 9
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 9
	t4_t3_mem0 += MAIN_MEM_r[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 9
	t4_t3_mem1 += MAIN_MEM_r[1]

	t5_t0 = S.Task('t5_t0', length=6, delay_cost=1)
	S += t5_t0 >= 9
	t5_t0 += MM[1]

	t4_t3 = S.Task('t4_t3', length=6, delay_cost=1)
	S += t4_t3 >= 10
	t4_t3 += MM[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 10
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 10
	t7_t3_mem1 += MAIN_MEM_r[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 11
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 11
	t11_mem1 += MAIN_MEM_r[1]

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	S += t7_t3 >= 11
	t7_t3 += MAS[0]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 12
	t11 += MAS[3]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 12
	t6_t2_mem0 += MAIN_MEM_r[0]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 12
	t6_t2_mem1 += MAIN_MEM_r[1]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 13
	t4_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 13
	t4_t1_mem1 += MAIN_MEM_r[1]

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	S += t6_t2 >= 13
	t6_t2 += MAS[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 14
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 14
	t10_mem1 += MAIN_MEM_r[1]

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	S += t4_t1 >= 14
	t4_t1 += MAS[0]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 15
	t10 += MAS[1]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 15
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 15
	t5_t3_mem1 += MAIN_MEM_r[1]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 16
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 16
	t0_t0_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 16
	t5_t3 += MAS[0]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 17
	t0_t0 += MAS[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 17
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 17
	t5_t2_mem1 += MAIN_MEM_r[1]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 18
	t5_t2 += MAS[3]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 18
	t6_t3_mem0 += MAIN_MEM_r[0]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 18
	t6_t3_mem1 += MAIN_MEM_r[1]

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	S += t6_t3 >= 19
	t6_t3 += MAS[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 19
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 19
	t7_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 20
	t4_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 20
	t4_t0_mem1 += MAIN_MEM_r[1]

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 20
	t7_t2 += MAS[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 21
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 21
	t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	S += t4_t0 >= 21
	t4_t0 += MAS[0]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 22
	t0_t1 += MAS[3]

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	S += t3_t3_mem0 >= 22
	t3_t3_mem0 += MAIN_MEM_r[0]

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	S += t3_t3_mem1 >= 22
	t3_t3_mem1 += MAIN_MEM_r[1]

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	S += t3_t2_mem0 >= 23
	t3_t2_mem0 += MAIN_MEM_r[0]

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	S += t3_t2_mem1 >= 23
	t3_t2_mem1 += MAIN_MEM_r[1]

	t3_t3 = S.Task('t3_t3', length=1, delay_cost=1)
	S += t3_t3 >= 23
	t3_t3 += MAS[0]

	t3_t2 = S.Task('t3_t2', length=1, delay_cost=1)
	S += t3_t2 >= 24
	t3_t2 += MAS[1]


	# new tasks
	t0_t2 = S.Task('t0_t2', length=6, delay_cost=1)
	t0_t2 += alt(MM)
	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	t0_t2_in += alt(MM_in)
	S += t0_t2_in*MM_in[0]<=t0_t2*MM[0]
	S += t0_t2_in*MM_in[1]<=t0_t2*MM[1]
	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	t0_t2_mem0 += MAS_MEM[0]
	S += 17 < t0_t2_mem0
	S += t0_t2_mem0 <= t0_t2

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	t0_t2_mem1 += MAS_MEM[7]
	S += 22 < t0_t2_mem1
	S += t0_t2_mem1 <= t0_t2

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	t0_t5 += alt(MAS)
	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MM_MEM[0]
	S += 9 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	t0_t5_mem1 += MM_MEM[1]
	S += 9 < t0_t5_mem1
	S += t0_t5_mem1 <= t0_t5

	t01 = S.Task('t01', length=1, delay_cost=1)
	t01 += alt(MAS)
	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MM_MEM[0]
	S += 9 < t01_mem0
	S += t01_mem0 <= t01

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	t01_mem1 += MM_MEM[1]
	S += 9 < t01_mem1
	S += t01_mem1 <= t01

	t20 = S.Task('t20', length=1, delay_cost=1)
	t20 += alt(MAS)
	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += MAS_MEM[2]
	S += 15 < t20_mem0
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += MAIN_MEM_r[1]
	S += t20_mem1 <= t20

	t21 = S.Task('t21', length=1, delay_cost=1)
	t21 += alt(MAS)
	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MAS_MEM[6]
	S += 12 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAIN_MEM_r[1]
	S += t21_mem1 <= t21

	t80 = S.Task('t80', length=1, delay_cost=1)
	t80 += alt(MAS)
	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += MAS_MEM[2]
	S += 15 < t80_mem0
	S += t80_mem0 <= t80

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	t80_mem1 += MAIN_MEM_r[1]
	S += t80_mem1 <= t80

	t81 = S.Task('t81', length=1, delay_cost=1)
	t81 += alt(MAS)
	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += MAS_MEM[6]
	S += 12 < t81_mem0
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += MAIN_MEM_r[1]
	S += t81_mem1 <= t81

	t3_t4 = S.Task('t3_t4', length=6, delay_cost=1)
	t3_t4 += alt(MM)
	t3_t4_in = S.Task('t3_t4_in', length=1, delay_cost=1)
	t3_t4_in += alt(MM_in)
	S += t3_t4_in*MM_in[0]<=t3_t4*MM[0]
	S += t3_t4_in*MM_in[1]<=t3_t4*MM[1]
	t3_t4_mem0 = S.Task('t3_t4_mem0', length=1, delay_cost=1)
	t3_t4_mem0 += MAS_MEM[2]
	S += 24 < t3_t4_mem0
	S += t3_t4_mem0 <= t3_t4

	t3_t4_mem1 = S.Task('t3_t4_mem1', length=1, delay_cost=1)
	t3_t4_mem1 += MAS_MEM[1]
	S += 23 < t3_t4_mem1
	S += t3_t4_mem1 <= t3_t4

	t30 = S.Task('t30', length=1, delay_cost=1)
	t30 += alt(MAS)
	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MM_MEM[2]
	S += 12 < t30_mem0
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += MM_MEM[3]
	S += 6 < t30_mem1
	S += t30_mem1 <= t30

	t3_t5 = S.Task('t3_t5', length=1, delay_cost=1)
	t3_t5 += alt(MAS)
	t3_t5_mem0 = S.Task('t3_t5_mem0', length=1, delay_cost=1)
	t3_t5_mem0 += MM_MEM[2]
	S += 12 < t3_t5_mem0
	S += t3_t5_mem0 <= t3_t5

	t3_t5_mem1 = S.Task('t3_t5_mem1', length=1, delay_cost=1)
	t3_t5_mem1 += MM_MEM[3]
	S += 6 < t3_t5_mem1
	S += t3_t5_mem1 <= t3_t5

	t4_t2 = S.Task('t4_t2', length=6, delay_cost=1)
	t4_t2 += alt(MM)
	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	t4_t2_in += alt(MM_in)
	S += t4_t2_in*MM_in[0]<=t4_t2*MM[0]
	S += t4_t2_in*MM_in[1]<=t4_t2*MM[1]
	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	t4_t2_mem0 += MAS_MEM[0]
	S += 21 < t4_t2_mem0
	S += t4_t2_mem0 <= t4_t2

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	t4_t2_mem1 += MAS_MEM[1]
	S += 14 < t4_t2_mem1
	S += t4_t2_mem1 <= t4_t2

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	t4_t5 += alt(MAS)
	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	t4_t5_mem0 += MM_MEM[0]
	S += 15 < t4_t5_mem0
	S += t4_t5_mem0 <= t4_t5

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	t4_t5_mem1 += MM_MEM[1]
	S += 15 < t4_t5_mem1
	S += t4_t5_mem1 <= t4_t5

	t41 = S.Task('t41', length=1, delay_cost=1)
	t41 += alt(MAS)
	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	t41_mem0 += MM_MEM[0]
	S += 15 < t41_mem0
	S += t41_mem0 <= t41

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	t41_mem1 += MM_MEM[1]
	S += 15 < t41_mem1
	S += t41_mem1 <= t41

	t5_t4 = S.Task('t5_t4', length=6, delay_cost=1)
	t5_t4 += alt(MM)
	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	t5_t4_in += alt(MM_in)
	S += t5_t4_in*MM_in[0]<=t5_t4*MM[0]
	S += t5_t4_in*MM_in[1]<=t5_t4*MM[1]
	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	t5_t4_mem0 += MAS_MEM[6]
	S += 18 < t5_t4_mem0
	S += t5_t4_mem0 <= t5_t4

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	t5_t4_mem1 += MAS_MEM[1]
	S += 16 < t5_t4_mem1
	S += t5_t4_mem1 <= t5_t4

	t50 = S.Task('t50', length=1, delay_cost=1)
	t50 += alt(MAS)
	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	t50_mem0 += MM_MEM[2]
	S += 14 < t50_mem0
	S += t50_mem0 <= t50

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	t50_mem1 += MM_MEM[1]
	S += 13 < t50_mem1
	S += t50_mem1 <= t50

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	t5_t5 += alt(MAS)
	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	t5_t5_mem0 += MM_MEM[2]
	S += 14 < t5_t5_mem0
	S += t5_t5_mem0 <= t5_t5

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	t5_t5_mem1 += MM_MEM[1]
	S += 13 < t5_t5_mem1
	S += t5_t5_mem1 <= t5_t5

	t6_t4 = S.Task('t6_t4', length=6, delay_cost=1)
	t6_t4 += alt(MM)
	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	t6_t4_in += alt(MM_in)
	S += t6_t4_in*MM_in[0]<=t6_t4*MM[0]
	S += t6_t4_in*MM_in[1]<=t6_t4*MM[1]
	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	t6_t4_mem0 += MAS_MEM[0]
	S += 13 < t6_t4_mem0
	S += t6_t4_mem0 <= t6_t4

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	t6_t4_mem1 += MAS_MEM[1]
	S += 19 < t6_t4_mem1
	S += t6_t4_mem1 <= t6_t4

	t60 = S.Task('t60', length=1, delay_cost=1)
	t60 += alt(MAS)
	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	t60_mem0 += MM_MEM[2]
	S += 8 < t60_mem0
	S += t60_mem0 <= t60

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	t60_mem1 += MM_MEM[3]
	S += 10 < t60_mem1
	S += t60_mem1 <= t60

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	t6_t5 += alt(MAS)
	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	t6_t5_mem0 += MM_MEM[2]
	S += 8 < t6_t5_mem0
	S += t6_t5_mem0 <= t6_t5

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	t6_t5_mem1 += MM_MEM[3]
	S += 10 < t6_t5_mem1
	S += t6_t5_mem1 <= t6_t5

	t7_t4 = S.Task('t7_t4', length=6, delay_cost=1)
	t7_t4 += alt(MM)
	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	t7_t4_in += alt(MM_in)
	S += t7_t4_in*MM_in[0]<=t7_t4*MM[0]
	S += t7_t4_in*MM_in[1]<=t7_t4*MM[1]
	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	t7_t4_mem0 += MAS_MEM[2]
	S += 20 < t7_t4_mem0
	S += t7_t4_mem0 <= t7_t4

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	t7_t4_mem1 += MAS_MEM[1]
	S += 11 < t7_t4_mem1
	S += t7_t4_mem1 <= t7_t4

	t70 = S.Task('t70', length=1, delay_cost=1)
	t70 += alt(MAS)
	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += MM_MEM[0]
	S += 7 < t70_mem0
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += MM_MEM[3]
	S += 11 < t70_mem1
	S += t70_mem1 <= t70

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	t7_t5 += alt(MAS)
	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	t7_t5_mem0 += MM_MEM[0]
	S += 7 < t7_t5_mem0
	S += t7_t5_mem0 <= t7_t5

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	t7_t5_mem1 += MM_MEM[3]
	S += 11 < t7_t5_mem1
	S += t7_t5_mem1 <= t7_t5

	t00 = S.Task('t00', length=1, delay_cost=1)
	t00 += alt(MAS)
	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += alt(MM_MEM)
	S += (t0_t2*MM[0])-1 < t00_mem0*MM_MEM[0]
	S += (t0_t2*MM[1])-1 < t00_mem0*MM_MEM[2]
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += alt(MAS_MEM)
	S += (t0_t5*MAS[0])-1 < t00_mem1*MAS_MEM[1]
	S += (t0_t5*MAS[1])-1 < t00_mem1*MAS_MEM[3]
	S += (t0_t5*MAS[2])-1 < t00_mem1*MAS_MEM[5]
	S += (t0_t5*MAS[3])-1 < t00_mem1*MAS_MEM[7]
	S += t00_mem1 <= t00

	t9_t0 = S.Task('t9_t0', length=1, delay_cost=1)
	t9_t0 += alt(MAS)
	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	t9_t0_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t9_t0_mem0*MAS_MEM[0]
	S += (t80*MAS[1])-1 < t9_t0_mem0*MAS_MEM[2]
	S += (t80*MAS[2])-1 < t9_t0_mem0*MAS_MEM[4]
	S += (t80*MAS[3])-1 < t9_t0_mem0*MAS_MEM[6]
	S += t9_t0_mem0 <= t9_t0

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	t9_t0_mem1 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t9_t0_mem1*MAS_MEM[1]
	S += (t81*MAS[1])-1 < t9_t0_mem1*MAS_MEM[3]
	S += (t81*MAS[2])-1 < t9_t0_mem1*MAS_MEM[5]
	S += (t81*MAS[3])-1 < t9_t0_mem1*MAS_MEM[7]
	S += t9_t0_mem1 <= t9_t0

	t9_t1 = S.Task('t9_t1', length=1, delay_cost=1)
	t9_t1 += alt(MAS)
	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	t9_t1_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t9_t1_mem0*MAS_MEM[0]
	S += (t80*MAS[1])-1 < t9_t1_mem0*MAS_MEM[2]
	S += (t80*MAS[2])-1 < t9_t1_mem0*MAS_MEM[4]
	S += (t80*MAS[3])-1 < t9_t1_mem0*MAS_MEM[6]
	S += t9_t1_mem0 <= t9_t1

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	t9_t1_mem1 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t9_t1_mem1*MAS_MEM[1]
	S += (t81*MAS[1])-1 < t9_t1_mem1*MAS_MEM[3]
	S += (t81*MAS[2])-1 < t9_t1_mem1*MAS_MEM[5]
	S += (t81*MAS[3])-1 < t9_t1_mem1*MAS_MEM[7]
	S += t9_t1_mem1 <= t9_t1

	t9_t3 = S.Task('t9_t3', length=6, delay_cost=1)
	t9_t3 += alt(MM)
	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	t9_t3_in += alt(MM_in)
	S += t9_t3_in*MM_in[0]<=t9_t3*MM[0]
	S += t9_t3_in*MM_in[1]<=t9_t3*MM[1]
	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	t9_t3_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t9_t3_mem0*MAS_MEM[0]
	S += (t80*MAS[1])-1 < t9_t3_mem0*MAS_MEM[2]
	S += (t80*MAS[2])-1 < t9_t3_mem0*MAS_MEM[4]
	S += (t80*MAS[3])-1 < t9_t3_mem0*MAS_MEM[6]
	S += t9_t3_mem0 <= t9_t3

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	t9_t3_mem1 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t9_t3_mem1*MAS_MEM[1]
	S += (t81*MAS[1])-1 < t9_t3_mem1*MAS_MEM[3]
	S += (t81*MAS[2])-1 < t9_t3_mem1*MAS_MEM[5]
	S += (t81*MAS[3])-1 < t9_t3_mem1*MAS_MEM[7]
	S += t9_t3_mem1 <= t9_t3

	t10_t0 = S.Task('t10_t0', length=1, delay_cost=1)
	t10_t0 += alt(MAS)
	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	t10_t0_mem0 += alt(MAS_MEM)
	S += (t20*MAS[0])-1 < t10_t0_mem0*MAS_MEM[0]
	S += (t20*MAS[1])-1 < t10_t0_mem0*MAS_MEM[2]
	S += (t20*MAS[2])-1 < t10_t0_mem0*MAS_MEM[4]
	S += (t20*MAS[3])-1 < t10_t0_mem0*MAS_MEM[6]
	S += t10_t0_mem0 <= t10_t0

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	t10_t0_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t10_t0_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t10_t0_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t10_t0_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t10_t0_mem1*MAS_MEM[7]
	S += t10_t0_mem1 <= t10_t0

	t10_t1 = S.Task('t10_t1', length=1, delay_cost=1)
	t10_t1 += alt(MAS)
	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	t10_t1_mem0 += alt(MAS_MEM)
	S += (t20*MAS[0])-1 < t10_t1_mem0*MAS_MEM[0]
	S += (t20*MAS[1])-1 < t10_t1_mem0*MAS_MEM[2]
	S += (t20*MAS[2])-1 < t10_t1_mem0*MAS_MEM[4]
	S += (t20*MAS[3])-1 < t10_t1_mem0*MAS_MEM[6]
	S += t10_t1_mem0 <= t10_t1

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	t10_t1_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t10_t1_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t10_t1_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t10_t1_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t10_t1_mem1*MAS_MEM[7]
	S += t10_t1_mem1 <= t10_t1

	t10_t3 = S.Task('t10_t3', length=6, delay_cost=1)
	t10_t3 += alt(MM)
	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	t10_t3_in += alt(MM_in)
	S += t10_t3_in*MM_in[0]<=t10_t3*MM[0]
	S += t10_t3_in*MM_in[1]<=t10_t3*MM[1]
	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	t10_t3_mem0 += alt(MAS_MEM)
	S += (t20*MAS[0])-1 < t10_t3_mem0*MAS_MEM[0]
	S += (t20*MAS[1])-1 < t10_t3_mem0*MAS_MEM[2]
	S += (t20*MAS[2])-1 < t10_t3_mem0*MAS_MEM[4]
	S += (t20*MAS[3])-1 < t10_t3_mem0*MAS_MEM[6]
	S += t10_t3_mem0 <= t10_t3

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	t10_t3_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t10_t3_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t10_t3_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t10_t3_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t10_t3_mem1*MAS_MEM[7]
	S += t10_t3_mem1 <= t10_t3

	t31 = S.Task('t31', length=1, delay_cost=1)
	t31 += alt(MAS)
	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(MM_MEM)
	S += (t3_t4*MM[0])-1 < t31_mem0*MM_MEM[0]
	S += (t3_t4*MM[1])-1 < t31_mem0*MM_MEM[2]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += alt(MAS_MEM)
	S += (t3_t5*MAS[0])-1 < t31_mem1*MAS_MEM[1]
	S += (t3_t5*MAS[1])-1 < t31_mem1*MAS_MEM[3]
	S += (t3_t5*MAS[2])-1 < t31_mem1*MAS_MEM[5]
	S += (t3_t5*MAS[3])-1 < t31_mem1*MAS_MEM[7]
	S += t31_mem1 <= t31

	t110 = S.Task('t110', length=1, delay_cost=1)
	t110 += alt(MAS)
	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(MAS_MEM)
	S += (t30*MAS[0])-1 < t110_mem0*MAS_MEM[0]
	S += (t30*MAS[1])-1 < t110_mem0*MAS_MEM[2]
	S += (t30*MAS[2])-1 < t110_mem0*MAS_MEM[4]
	S += (t30*MAS[3])-1 < t110_mem0*MAS_MEM[6]
	S += t110_mem0 <= t110

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	t110_mem1 += alt(MAS_MEM)
	S += (t30*MAS[0])-1 < t110_mem1*MAS_MEM[1]
	S += (t30*MAS[1])-1 < t110_mem1*MAS_MEM[3]
	S += (t30*MAS[2])-1 < t110_mem1*MAS_MEM[5]
	S += (t30*MAS[3])-1 < t110_mem1*MAS_MEM[7]
	S += t110_mem1 <= t110

	t40 = S.Task('t40', length=1, delay_cost=1)
	t40 += alt(MAS)
	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	t40_mem0 += alt(MM_MEM)
	S += (t4_t2*MM[0])-1 < t40_mem0*MM_MEM[0]
	S += (t4_t2*MM[1])-1 < t40_mem0*MM_MEM[2]
	S += t40_mem0 <= t40

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	t40_mem1 += alt(MAS_MEM)
	S += (t4_t5*MAS[0])-1 < t40_mem1*MAS_MEM[1]
	S += (t4_t5*MAS[1])-1 < t40_mem1*MAS_MEM[3]
	S += (t4_t5*MAS[2])-1 < t40_mem1*MAS_MEM[5]
	S += (t4_t5*MAS[3])-1 < t40_mem1*MAS_MEM[7]
	S += t40_mem1 <= t40

	t51 = S.Task('t51', length=1, delay_cost=1)
	t51 += alt(MAS)
	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	t51_mem0 += alt(MM_MEM)
	S += (t5_t4*MM[0])-1 < t51_mem0*MM_MEM[0]
	S += (t5_t4*MM[1])-1 < t51_mem0*MM_MEM[2]
	S += t51_mem0 <= t51

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	t51_mem1 += alt(MAS_MEM)
	S += (t5_t5*MAS[0])-1 < t51_mem1*MAS_MEM[1]
	S += (t5_t5*MAS[1])-1 < t51_mem1*MAS_MEM[3]
	S += (t5_t5*MAS[2])-1 < t51_mem1*MAS_MEM[5]
	S += (t5_t5*MAS[3])-1 < t51_mem1*MAS_MEM[7]
	S += t51_mem1 <= t51

	t61 = S.Task('t61', length=1, delay_cost=1)
	t61 += alt(MAS)
	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	t61_mem0 += alt(MM_MEM)
	S += (t6_t4*MM[0])-1 < t61_mem0*MM_MEM[0]
	S += (t6_t4*MM[1])-1 < t61_mem0*MM_MEM[2]
	S += t61_mem0 <= t61

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	t61_mem1 += alt(MAS_MEM)
	S += (t6_t5*MAS[0])-1 < t61_mem1*MAS_MEM[1]
	S += (t6_t5*MAS[1])-1 < t61_mem1*MAS_MEM[3]
	S += (t6_t5*MAS[2])-1 < t61_mem1*MAS_MEM[5]
	S += (t6_t5*MAS[3])-1 < t61_mem1*MAS_MEM[7]
	S += t61_mem1 <= t61

	t71 = S.Task('t71', length=1, delay_cost=1)
	t71 += alt(MAS)
	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	t71_mem0 += alt(MM_MEM)
	S += (t7_t4*MM[0])-1 < t71_mem0*MM_MEM[0]
	S += (t7_t4*MM[1])-1 < t71_mem0*MM_MEM[2]
	S += t71_mem0 <= t71

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	t71_mem1 += alt(MAS_MEM)
	S += (t7_t5*MAS[0])-1 < t71_mem1*MAS_MEM[1]
	S += (t7_t5*MAS[1])-1 < t71_mem1*MAS_MEM[3]
	S += (t7_t5*MAS[2])-1 < t71_mem1*MAS_MEM[5]
	S += (t7_t5*MAS[3])-1 < t71_mem1*MAS_MEM[7]
	S += t71_mem1 <= t71

	t290 = S.Task('t290', length=1, delay_cost=1)
	t290 += alt(MAS)
	t290_mem0 = S.Task('t290_mem0', length=1, delay_cost=1)
	t290_mem0 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t290_mem0*MAS_MEM[0]
	S += (t50*MAS[1])-1 < t290_mem0*MAS_MEM[2]
	S += (t50*MAS[2])-1 < t290_mem0*MAS_MEM[4]
	S += (t50*MAS[3])-1 < t290_mem0*MAS_MEM[6]
	S += t290_mem0 <= t290

	t290_mem1 = S.Task('t290_mem1', length=1, delay_cost=1)
	t290_mem1 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t290_mem1*MAS_MEM[1]
	S += (t50*MAS[1])-1 < t290_mem1*MAS_MEM[3]
	S += (t50*MAS[2])-1 < t290_mem1*MAS_MEM[5]
	S += (t50*MAS[3])-1 < t290_mem1*MAS_MEM[7]
	S += t290_mem1 <= t290

	t151 = S.Task('t151', length=1, delay_cost=1)
	t151 += alt(MAS)
	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t151_mem0*MAS_MEM[0]
	S += (t01*MAS[1])-1 < t151_mem0*MAS_MEM[2]
	S += (t01*MAS[2])-1 < t151_mem0*MAS_MEM[4]
	S += (t01*MAS[3])-1 < t151_mem0*MAS_MEM[6]
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < t151_mem1*MAS_MEM[1]
	S += (t41*MAS[1])-1 < t151_mem1*MAS_MEM[3]
	S += (t41*MAS[2])-1 < t151_mem1*MAS_MEM[5]
	S += (t41*MAS[3])-1 < t151_mem1*MAS_MEM[7]
	S += t151_mem1 <= t151

	t220 = S.Task('t220', length=1, delay_cost=1)
	t220 += alt(MAS)
	t220_mem0 = S.Task('t220_mem0', length=1, delay_cost=1)
	t220_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t220_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < t220_mem0*MAS_MEM[2]
	S += (t60*MAS[2])-1 < t220_mem0*MAS_MEM[4]
	S += (t60*MAS[3])-1 < t220_mem0*MAS_MEM[6]
	S += t220_mem0 <= t220

	t220_mem1 = S.Task('t220_mem1', length=1, delay_cost=1)
	t220_mem1 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t220_mem1*MAS_MEM[1]
	S += (t60*MAS[1])-1 < t220_mem1*MAS_MEM[3]
	S += (t60*MAS[2])-1 < t220_mem1*MAS_MEM[5]
	S += (t60*MAS[3])-1 < t220_mem1*MAS_MEM[7]
	S += t220_mem1 <= t220

	t260 = S.Task('t260', length=1, delay_cost=1)
	t260 += alt(MAS)
	t260_mem0 = S.Task('t260_mem0', length=1, delay_cost=1)
	t260_mem0 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t260_mem0*MAS_MEM[0]
	S += (t70*MAS[1])-1 < t260_mem0*MAS_MEM[2]
	S += (t70*MAS[2])-1 < t260_mem0*MAS_MEM[4]
	S += (t70*MAS[3])-1 < t260_mem0*MAS_MEM[6]
	S += t260_mem0 <= t260

	t260_mem1 = S.Task('t260_mem1', length=1, delay_cost=1)
	t260_mem1 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t260_mem1*MAS_MEM[1]
	S += (t70*MAS[1])-1 < t260_mem1*MAS_MEM[3]
	S += (t70*MAS[2])-1 < t260_mem1*MAS_MEM[5]
	S += (t70*MAS[3])-1 < t260_mem1*MAS_MEM[7]
	S += t260_mem1 <= t260

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM2_stage1MAS4/SQR012345/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

