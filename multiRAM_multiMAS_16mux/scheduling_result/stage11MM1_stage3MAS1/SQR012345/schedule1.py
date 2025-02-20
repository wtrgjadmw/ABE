from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 155
	S = Scenario("schedule1", horizon=horizon)

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
	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 0
	t0_t0_in += MAS_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 0
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 0
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t0 = S.Task('t0_t0', length=3, delay_cost=1)
	S += t0_t0 >= 1
	t0_t0 += MAS[0]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 1
	t7_t3_in += MAS_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 1
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 1
	t7_t3_mem1 += MAIN_MEM_r[1]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 2
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 2
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 2
	t7_t0_mem1 += MAIN_MEM_r[1]

	t7_t3 = S.Task('t7_t3', length=3, delay_cost=1)
	S += t7_t3 >= 2
	t7_t3 += MAS[0]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 3
	t6_t3_in += MAS_in[0]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 3
	t6_t3_mem0 += MAIN_MEM_r[0]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 3
	t6_t3_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=11, delay_cost=1)
	S += t7_t0 >= 3
	t7_t0 += MM[0]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 4
	t6_t2_in += MAS_in[0]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 4
	t6_t2_mem0 += MAIN_MEM_r[0]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 4
	t6_t2_mem1 += MAIN_MEM_r[1]

	t6_t3 = S.Task('t6_t3', length=3, delay_cost=1)
	S += t6_t3 >= 4
	t6_t3 += MAS[0]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 5
	t5_t0_in += MM_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 5
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 5
	t5_t0_mem1 += MAIN_MEM_r[1]

	t6_t2 = S.Task('t6_t2', length=3, delay_cost=1)
	S += t6_t2 >= 5
	t6_t2 += MAS[0]

	t5_t0 = S.Task('t5_t0', length=11, delay_cost=1)
	S += t5_t0 >= 6
	t5_t0 += MM[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 6
	t7_t1_in += MM_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 6
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 6
	t7_t1_mem1 += MAIN_MEM_r[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 7
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 7
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 7
	t0_t3_mem1 += MAIN_MEM_r[1]

	t7_t1 = S.Task('t7_t1', length=11, delay_cost=1)
	S += t7_t1 >= 7
	t7_t1 += MM[0]

	t0_t3 = S.Task('t0_t3', length=11, delay_cost=1)
	S += t0_t3 >= 8
	t0_t3 += MM[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 8
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 8
	t4_t3_mem0 += MAIN_MEM_r[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 8
	t4_t3_mem1 += MAIN_MEM_r[1]

	t4_t3 = S.Task('t4_t3', length=11, delay_cost=1)
	S += t4_t3 >= 9
	t4_t3 += MM[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 9
	t7_t2_in += MAS_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 9
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 9
	t7_t2_mem1 += MAIN_MEM_r[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 10
	t0_t1_in += MAS_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 10
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 10
	t0_t1_mem1 += MAIN_MEM_r[1]

	t7_t2 = S.Task('t7_t2', length=3, delay_cost=1)
	S += t7_t2 >= 10
	t7_t2 += MAS[0]

	t0_t1 = S.Task('t0_t1', length=3, delay_cost=1)
	S += t0_t1 >= 11
	t0_t1 += MAS[0]

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	S += t3_t0_in >= 11
	t3_t0_in += MM_in[0]

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_mem0 >= 11
	t3_t0_mem0 += MAIN_MEM_r[0]

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_mem1 >= 11
	t3_t0_mem1 += MAIN_MEM_r[1]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 12
	t11_in += MAS_in[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 12
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 12
	t11_mem1 += MAIN_MEM_r[1]

	t3_t0 = S.Task('t3_t0', length=11, delay_cost=1)
	S += t3_t0 >= 12
	t3_t0 += MM[0]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 13
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 13
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 13
	t10_mem1 += MAIN_MEM_r[1]

	t11 = S.Task('t11', length=3, delay_cost=1)
	S += t11 >= 13
	t11 += MAS[0]

	t10 = S.Task('t10', length=3, delay_cost=1)
	S += t10 >= 14
	t10 += MAS[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 14
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 14
	t6_t1_mem0 += MAIN_MEM_r[0]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 14
	t6_t1_mem1 += MAIN_MEM_r[1]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 15
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 15
	t6_t0_mem0 += MAIN_MEM_r[0]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 15
	t6_t0_mem1 += MAIN_MEM_r[1]

	t6_t1 = S.Task('t6_t1', length=11, delay_cost=1)
	S += t6_t1 >= 15
	t6_t1 += MM[0]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 16
	t5_t3_in += MAS_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 16
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 16
	t5_t3_mem1 += MAIN_MEM_r[1]

	t6_t0 = S.Task('t6_t0', length=11, delay_cost=1)
	S += t6_t0 >= 16
	t6_t0 += MM[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 17
	t5_t2_in += MAS_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 17
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 17
	t5_t2_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=3, delay_cost=1)
	S += t5_t3 >= 17
	t5_t3 += MAS[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 18
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 18
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 18
	t5_t1_mem1 += MAIN_MEM_r[1]

	t5_t2 = S.Task('t5_t2', length=3, delay_cost=1)
	S += t5_t2 >= 18
	t5_t2 += MAS[0]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 19
	t4_t1_in += MAS_in[0]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 19
	t4_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 19
	t4_t1_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=11, delay_cost=1)
	S += t5_t1 >= 19
	t5_t1 += MM[0]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 20
	t4_t0_in += MAS_in[0]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 20
	t4_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 20
	t4_t0_mem1 += MAIN_MEM_r[1]

	t4_t1 = S.Task('t4_t1', length=3, delay_cost=1)
	S += t4_t1 >= 20
	t4_t1 += MAS[0]

	t3_t3_in = S.Task('t3_t3_in', length=1, delay_cost=1)
	S += t3_t3_in >= 21
	t3_t3_in += MAS_in[0]

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	S += t3_t3_mem0 >= 21
	t3_t3_mem0 += MAIN_MEM_r[0]

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	S += t3_t3_mem1 >= 21
	t3_t3_mem1 += MAIN_MEM_r[1]

	t4_t0 = S.Task('t4_t0', length=3, delay_cost=1)
	S += t4_t0 >= 21
	t4_t0 += MAS[0]

	t3_t2_in = S.Task('t3_t2_in', length=1, delay_cost=1)
	S += t3_t2_in >= 22
	t3_t2_in += MAS_in[0]

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	S += t3_t2_mem0 >= 22
	t3_t2_mem0 += MAIN_MEM_r[0]

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	S += t3_t2_mem1 >= 22
	t3_t2_mem1 += MAIN_MEM_r[1]

	t3_t3 = S.Task('t3_t3', length=3, delay_cost=1)
	S += t3_t3 >= 22
	t3_t3 += MAS[0]

	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	S += t3_t1_in >= 23
	t3_t1_in += MM_in[0]

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_mem0 >= 23
	t3_t1_mem0 += MAIN_MEM_r[0]

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_mem1 >= 23
	t3_t1_mem1 += MAIN_MEM_r[1]

	t3_t2 = S.Task('t3_t2', length=3, delay_cost=1)
	S += t3_t2 >= 23
	t3_t2 += MAS[0]

	t3_t1 = S.Task('t3_t1', length=11, delay_cost=1)
	S += t3_t1 >= 24
	t3_t1 += MM[0]


	# new tasks
	t0_t2 = S.Task('t0_t2', length=11, delay_cost=1)
	t0_t2 += alt(MM)
	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	t0_t2_in += alt(MM_in)
	S += t0_t2_in*MM_in[0]<=t0_t2*MM[0]
	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	t0_t2_mem0 += MAS_MEM[0]
	S += 3 < t0_t2_mem0
	S += t0_t2_mem0 <= t0_t2

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	t0_t2_mem1 += MAS_MEM[1]
	S += 13 < t0_t2_mem1
	S += t0_t2_mem1 <= t0_t2

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	t0_t5 += alt(MAS)
	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	t0_t5_in += alt(MAS_in)
	S += t0_t5_in*MAS_in[0]<=t0_t5*MAS[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MM_MEM[0]
	S += 18 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	t0_t5_mem1 += MM_MEM[1]
	S += 18 < t0_t5_mem1
	S += t0_t5_mem1 <= t0_t5

	t01 = S.Task('t01', length=3, delay_cost=1)
	t01 += alt(MAS)
	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	t01_in += alt(MAS_in)
	S += t01_in*MAS_in[0]<=t01*MAS[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MM_MEM[0]
	S += 18 < t01_mem0
	S += t01_mem0 <= t01

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	t01_mem1 += MM_MEM[1]
	S += 18 < t01_mem1
	S += t01_mem1 <= t01

	t20 = S.Task('t20', length=3, delay_cost=1)
	t20 += alt(MAS)
	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	t20_in += alt(MAS_in)
	S += t20_in*MAS_in[0]<=t20*MAS[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += MAS_MEM[0]
	S += 16 < t20_mem0
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += MAIN_MEM_r[1]
	S += t20_mem1 <= t20

	t21 = S.Task('t21', length=3, delay_cost=1)
	t21 += alt(MAS)
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	t21_in += alt(MAS_in)
	S += t21_in*MAS_in[0]<=t21*MAS[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MAS_MEM[0]
	S += 15 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAIN_MEM_r[1]
	S += t21_mem1 <= t21

	t80 = S.Task('t80', length=3, delay_cost=1)
	t80 += alt(MAS)
	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	t80_in += alt(MAS_in)
	S += t80_in*MAS_in[0]<=t80*MAS[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += MAS_MEM[0]
	S += 16 < t80_mem0
	S += t80_mem0 <= t80

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	t80_mem1 += MAIN_MEM_r[1]
	S += t80_mem1 <= t80

	t81 = S.Task('t81', length=3, delay_cost=1)
	t81 += alt(MAS)
	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	t81_in += alt(MAS_in)
	S += t81_in*MAS_in[0]<=t81*MAS[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += MAS_MEM[0]
	S += 15 < t81_mem0
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += MAIN_MEM_r[1]
	S += t81_mem1 <= t81

	t3_t4 = S.Task('t3_t4', length=11, delay_cost=1)
	t3_t4 += alt(MM)
	t3_t4_in = S.Task('t3_t4_in', length=1, delay_cost=1)
	t3_t4_in += alt(MM_in)
	S += t3_t4_in*MM_in[0]<=t3_t4*MM[0]
	t3_t4_mem0 = S.Task('t3_t4_mem0', length=1, delay_cost=1)
	t3_t4_mem0 += MAS_MEM[0]
	S += 25 < t3_t4_mem0
	S += t3_t4_mem0 <= t3_t4

	t3_t4_mem1 = S.Task('t3_t4_mem1', length=1, delay_cost=1)
	t3_t4_mem1 += MAS_MEM[1]
	S += 24 < t3_t4_mem1
	S += t3_t4_mem1 <= t3_t4

	t30 = S.Task('t30', length=3, delay_cost=1)
	t30 += alt(MAS)
	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	t30_in += alt(MAS_in)
	S += t30_in*MAS_in[0]<=t30*MAS[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MM_MEM[0]
	S += 22 < t30_mem0
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += MM_MEM[1]
	S += 34 < t30_mem1
	S += t30_mem1 <= t30

	t3_t5 = S.Task('t3_t5', length=3, delay_cost=1)
	t3_t5 += alt(MAS)
	t3_t5_in = S.Task('t3_t5_in', length=1, delay_cost=1)
	t3_t5_in += alt(MAS_in)
	S += t3_t5_in*MAS_in[0]<=t3_t5*MAS[0]

	t3_t5_mem0 = S.Task('t3_t5_mem0', length=1, delay_cost=1)
	t3_t5_mem0 += MM_MEM[0]
	S += 22 < t3_t5_mem0
	S += t3_t5_mem0 <= t3_t5

	t3_t5_mem1 = S.Task('t3_t5_mem1', length=1, delay_cost=1)
	t3_t5_mem1 += MM_MEM[1]
	S += 34 < t3_t5_mem1
	S += t3_t5_mem1 <= t3_t5

	t4_t2 = S.Task('t4_t2', length=11, delay_cost=1)
	t4_t2 += alt(MM)
	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	t4_t2_in += alt(MM_in)
	S += t4_t2_in*MM_in[0]<=t4_t2*MM[0]
	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	t4_t2_mem0 += MAS_MEM[0]
	S += 23 < t4_t2_mem0
	S += t4_t2_mem0 <= t4_t2

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	t4_t2_mem1 += MAS_MEM[1]
	S += 22 < t4_t2_mem1
	S += t4_t2_mem1 <= t4_t2

	t4_t5 = S.Task('t4_t5', length=3, delay_cost=1)
	t4_t5 += alt(MAS)
	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	t4_t5_in += alt(MAS_in)
	S += t4_t5_in*MAS_in[0]<=t4_t5*MAS[0]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	t4_t5_mem0 += MM_MEM[0]
	S += 19 < t4_t5_mem0
	S += t4_t5_mem0 <= t4_t5

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	t4_t5_mem1 += MM_MEM[1]
	S += 19 < t4_t5_mem1
	S += t4_t5_mem1 <= t4_t5

	t41 = S.Task('t41', length=3, delay_cost=1)
	t41 += alt(MAS)
	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	t41_in += alt(MAS_in)
	S += t41_in*MAS_in[0]<=t41*MAS[0]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	t41_mem0 += MM_MEM[0]
	S += 19 < t41_mem0
	S += t41_mem0 <= t41

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	t41_mem1 += MM_MEM[1]
	S += 19 < t41_mem1
	S += t41_mem1 <= t41

	t5_t4 = S.Task('t5_t4', length=11, delay_cost=1)
	t5_t4 += alt(MM)
	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	t5_t4_in += alt(MM_in)
	S += t5_t4_in*MM_in[0]<=t5_t4*MM[0]
	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	t5_t4_mem0 += MAS_MEM[0]
	S += 20 < t5_t4_mem0
	S += t5_t4_mem0 <= t5_t4

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	t5_t4_mem1 += MAS_MEM[1]
	S += 19 < t5_t4_mem1
	S += t5_t4_mem1 <= t5_t4

	t50 = S.Task('t50', length=3, delay_cost=1)
	t50 += alt(MAS)
	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	t50_in += alt(MAS_in)
	S += t50_in*MAS_in[0]<=t50*MAS[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	t50_mem0 += MM_MEM[0]
	S += 16 < t50_mem0
	S += t50_mem0 <= t50

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	t50_mem1 += MM_MEM[1]
	S += 29 < t50_mem1
	S += t50_mem1 <= t50

	t5_t5 = S.Task('t5_t5', length=3, delay_cost=1)
	t5_t5 += alt(MAS)
	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	t5_t5_in += alt(MAS_in)
	S += t5_t5_in*MAS_in[0]<=t5_t5*MAS[0]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	t5_t5_mem0 += MM_MEM[0]
	S += 16 < t5_t5_mem0
	S += t5_t5_mem0 <= t5_t5

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	t5_t5_mem1 += MM_MEM[1]
	S += 29 < t5_t5_mem1
	S += t5_t5_mem1 <= t5_t5

	t6_t4 = S.Task('t6_t4', length=11, delay_cost=1)
	t6_t4 += alt(MM)
	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	t6_t4_in += alt(MM_in)
	S += t6_t4_in*MM_in[0]<=t6_t4*MM[0]
	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	t6_t4_mem0 += MAS_MEM[0]
	S += 7 < t6_t4_mem0
	S += t6_t4_mem0 <= t6_t4

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	t6_t4_mem1 += MAS_MEM[1]
	S += 6 < t6_t4_mem1
	S += t6_t4_mem1 <= t6_t4

	t60 = S.Task('t60', length=3, delay_cost=1)
	t60 += alt(MAS)
	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	t60_in += alt(MAS_in)
	S += t60_in*MAS_in[0]<=t60*MAS[0]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	t60_mem0 += MM_MEM[0]
	S += 26 < t60_mem0
	S += t60_mem0 <= t60

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	t60_mem1 += MM_MEM[1]
	S += 25 < t60_mem1
	S += t60_mem1 <= t60

	t6_t5 = S.Task('t6_t5', length=3, delay_cost=1)
	t6_t5 += alt(MAS)
	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	t6_t5_in += alt(MAS_in)
	S += t6_t5_in*MAS_in[0]<=t6_t5*MAS[0]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	t6_t5_mem0 += MM_MEM[0]
	S += 26 < t6_t5_mem0
	S += t6_t5_mem0 <= t6_t5

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	t6_t5_mem1 += MM_MEM[1]
	S += 25 < t6_t5_mem1
	S += t6_t5_mem1 <= t6_t5

	t7_t4 = S.Task('t7_t4', length=11, delay_cost=1)
	t7_t4 += alt(MM)
	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	t7_t4_in += alt(MM_in)
	S += t7_t4_in*MM_in[0]<=t7_t4*MM[0]
	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	t7_t4_mem0 += MAS_MEM[0]
	S += 12 < t7_t4_mem0
	S += t7_t4_mem0 <= t7_t4

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	t7_t4_mem1 += MAS_MEM[1]
	S += 4 < t7_t4_mem1
	S += t7_t4_mem1 <= t7_t4

	t70 = S.Task('t70', length=3, delay_cost=1)
	t70 += alt(MAS)
	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	t70_in += alt(MAS_in)
	S += t70_in*MAS_in[0]<=t70*MAS[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += MM_MEM[0]
	S += 13 < t70_mem0
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += MM_MEM[1]
	S += 17 < t70_mem1
	S += t70_mem1 <= t70

	t7_t5 = S.Task('t7_t5', length=3, delay_cost=1)
	t7_t5 += alt(MAS)
	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	t7_t5_in += alt(MAS_in)
	S += t7_t5_in*MAS_in[0]<=t7_t5*MAS[0]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	t7_t5_mem0 += MM_MEM[0]
	S += 13 < t7_t5_mem0
	S += t7_t5_mem0 <= t7_t5

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	t7_t5_mem1 += MM_MEM[1]
	S += 17 < t7_t5_mem1
	S += t7_t5_mem1 <= t7_t5

	t00 = S.Task('t00', length=3, delay_cost=1)
	t00 += alt(MAS)
	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	t00_in += alt(MAS_in)
	S += t00_in*MAS_in[0]<=t00*MAS[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += alt(MM_MEM)
	S += (t0_t2*MM[0])-1 < t00_mem0*MM_MEM[0]
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += alt(MAS_MEM)
	S += (t0_t5*MAS[0])-1 < t00_mem1*MAS_MEM[1]
	S += t00_mem1 <= t00

	t9_t0 = S.Task('t9_t0', length=3, delay_cost=1)
	t9_t0 += alt(MAS)
	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	t9_t0_in += alt(MAS_in)
	S += t9_t0_in*MAS_in[0]<=t9_t0*MAS[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	t9_t0_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t9_t0_mem0*MAS_MEM[0]
	S += t9_t0_mem0 <= t9_t0

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	t9_t0_mem1 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t9_t0_mem1*MAS_MEM[1]
	S += t9_t0_mem1 <= t9_t0

	t9_t1 = S.Task('t9_t1', length=3, delay_cost=1)
	t9_t1 += alt(MAS)
	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	t9_t1_in += alt(MAS_in)
	S += t9_t1_in*MAS_in[0]<=t9_t1*MAS[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	t9_t1_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t9_t1_mem0*MAS_MEM[0]
	S += t9_t1_mem0 <= t9_t1

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	t9_t1_mem1 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t9_t1_mem1*MAS_MEM[1]
	S += t9_t1_mem1 <= t9_t1

	t9_t3 = S.Task('t9_t3', length=11, delay_cost=1)
	t9_t3 += alt(MM)
	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	t9_t3_in += alt(MM_in)
	S += t9_t3_in*MM_in[0]<=t9_t3*MM[0]
	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	t9_t3_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t9_t3_mem0*MAS_MEM[0]
	S += t9_t3_mem0 <= t9_t3

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	t9_t3_mem1 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t9_t3_mem1*MAS_MEM[1]
	S += t9_t3_mem1 <= t9_t3

	t10_t0 = S.Task('t10_t0', length=3, delay_cost=1)
	t10_t0 += alt(MAS)
	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	t10_t0_in += alt(MAS_in)
	S += t10_t0_in*MAS_in[0]<=t10_t0*MAS[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	t10_t0_mem0 += alt(MAS_MEM)
	S += (t20*MAS[0])-1 < t10_t0_mem0*MAS_MEM[0]
	S += t10_t0_mem0 <= t10_t0

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	t10_t0_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t10_t0_mem1*MAS_MEM[1]
	S += t10_t0_mem1 <= t10_t0

	t10_t1 = S.Task('t10_t1', length=3, delay_cost=1)
	t10_t1 += alt(MAS)
	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	t10_t1_in += alt(MAS_in)
	S += t10_t1_in*MAS_in[0]<=t10_t1*MAS[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	t10_t1_mem0 += alt(MAS_MEM)
	S += (t20*MAS[0])-1 < t10_t1_mem0*MAS_MEM[0]
	S += t10_t1_mem0 <= t10_t1

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	t10_t1_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t10_t1_mem1*MAS_MEM[1]
	S += t10_t1_mem1 <= t10_t1

	t10_t3 = S.Task('t10_t3', length=11, delay_cost=1)
	t10_t3 += alt(MM)
	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	t10_t3_in += alt(MM_in)
	S += t10_t3_in*MM_in[0]<=t10_t3*MM[0]
	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	t10_t3_mem0 += alt(MAS_MEM)
	S += (t20*MAS[0])-1 < t10_t3_mem0*MAS_MEM[0]
	S += t10_t3_mem0 <= t10_t3

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	t10_t3_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t10_t3_mem1*MAS_MEM[1]
	S += t10_t3_mem1 <= t10_t3

	t31 = S.Task('t31', length=3, delay_cost=1)
	t31 += alt(MAS)
	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	t31_in += alt(MAS_in)
	S += t31_in*MAS_in[0]<=t31*MAS[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += alt(MM_MEM)
	S += (t3_t4*MM[0])-1 < t31_mem0*MM_MEM[0]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += alt(MAS_MEM)
	S += (t3_t5*MAS[0])-1 < t31_mem1*MAS_MEM[1]
	S += t31_mem1 <= t31

	t110 = S.Task('t110', length=3, delay_cost=1)
	t110 += alt(MAS)
	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	t110_in += alt(MAS_in)
	S += t110_in*MAS_in[0]<=t110*MAS[0]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(MAS_MEM)
	S += (t30*MAS[0])-1 < t110_mem0*MAS_MEM[0]
	S += t110_mem0 <= t110

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	t110_mem1 += alt(MAS_MEM)
	S += (t30*MAS[0])-1 < t110_mem1*MAS_MEM[1]
	S += t110_mem1 <= t110

	t40 = S.Task('t40', length=3, delay_cost=1)
	t40 += alt(MAS)
	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	t40_in += alt(MAS_in)
	S += t40_in*MAS_in[0]<=t40*MAS[0]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	t40_mem0 += alt(MM_MEM)
	S += (t4_t2*MM[0])-1 < t40_mem0*MM_MEM[0]
	S += t40_mem0 <= t40

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	t40_mem1 += alt(MAS_MEM)
	S += (t4_t5*MAS[0])-1 < t40_mem1*MAS_MEM[1]
	S += t40_mem1 <= t40

	t51 = S.Task('t51', length=3, delay_cost=1)
	t51 += alt(MAS)
	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	t51_in += alt(MAS_in)
	S += t51_in*MAS_in[0]<=t51*MAS[0]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	t51_mem0 += alt(MM_MEM)
	S += (t5_t4*MM[0])-1 < t51_mem0*MM_MEM[0]
	S += t51_mem0 <= t51

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	t51_mem1 += alt(MAS_MEM)
	S += (t5_t5*MAS[0])-1 < t51_mem1*MAS_MEM[1]
	S += t51_mem1 <= t51

	t61 = S.Task('t61', length=3, delay_cost=1)
	t61 += alt(MAS)
	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	t61_in += alt(MAS_in)
	S += t61_in*MAS_in[0]<=t61*MAS[0]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	t61_mem0 += alt(MM_MEM)
	S += (t6_t4*MM[0])-1 < t61_mem0*MM_MEM[0]
	S += t61_mem0 <= t61

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	t61_mem1 += alt(MAS_MEM)
	S += (t6_t5*MAS[0])-1 < t61_mem1*MAS_MEM[1]
	S += t61_mem1 <= t61

	t71 = S.Task('t71', length=3, delay_cost=1)
	t71 += alt(MAS)
	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	t71_in += alt(MAS_in)
	S += t71_in*MAS_in[0]<=t71*MAS[0]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	t71_mem0 += alt(MM_MEM)
	S += (t7_t4*MM[0])-1 < t71_mem0*MM_MEM[0]
	S += t71_mem0 <= t71

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	t71_mem1 += alt(MAS_MEM)
	S += (t7_t5*MAS[0])-1 < t71_mem1*MAS_MEM[1]
	S += t71_mem1 <= t71

	t290 = S.Task('t290', length=3, delay_cost=1)
	t290 += alt(MAS)
	t290_in = S.Task('t290_in', length=1, delay_cost=1)
	t290_in += alt(MAS_in)
	S += t290_in*MAS_in[0]<=t290*MAS[0]

	t290_mem0 = S.Task('t290_mem0', length=1, delay_cost=1)
	t290_mem0 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t290_mem0*MAS_MEM[0]
	S += t290_mem0 <= t290

	t290_mem1 = S.Task('t290_mem1', length=1, delay_cost=1)
	t290_mem1 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t290_mem1*MAS_MEM[1]
	S += t290_mem1 <= t290

	t151 = S.Task('t151', length=3, delay_cost=1)
	t151 += alt(MAS)
	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	t151_in += alt(MAS_in)
	S += t151_in*MAS_in[0]<=t151*MAS[0]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t151_mem0*MAS_MEM[0]
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < t151_mem1*MAS_MEM[1]
	S += t151_mem1 <= t151

	t220 = S.Task('t220', length=3, delay_cost=1)
	t220 += alt(MAS)
	t220_in = S.Task('t220_in', length=1, delay_cost=1)
	t220_in += alt(MAS_in)
	S += t220_in*MAS_in[0]<=t220*MAS[0]

	t220_mem0 = S.Task('t220_mem0', length=1, delay_cost=1)
	t220_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t220_mem0*MAS_MEM[0]
	S += t220_mem0 <= t220

	t220_mem1 = S.Task('t220_mem1', length=1, delay_cost=1)
	t220_mem1 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t220_mem1*MAS_MEM[1]
	S += t220_mem1 <= t220

	t260 = S.Task('t260', length=3, delay_cost=1)
	t260 += alt(MAS)
	t260_in = S.Task('t260_in', length=1, delay_cost=1)
	t260_in += alt(MAS_in)
	S += t260_in*MAS_in[0]<=t260*MAS[0]

	t260_mem0 = S.Task('t260_mem0', length=1, delay_cost=1)
	t260_mem0 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t260_mem0*MAS_MEM[0]
	S += t260_mem0 <= t260

	t260_mem1 = S.Task('t260_mem1', length=1, delay_cost=1)
	t260_mem1 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t260_mem1*MAS_MEM[1]
	S += t260_mem1 <= t260

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS1/SQR012345/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution

