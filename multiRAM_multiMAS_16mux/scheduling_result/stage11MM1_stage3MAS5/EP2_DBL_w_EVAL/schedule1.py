from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 141
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=11)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=5)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	S += t10_t3_in >= 0
	t10_t3_in += MAS_in[3]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 0
	t10_t3_mem0 += MAIN_MEM_r[0]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 0
	t10_t3_mem1 += MAIN_MEM_r[1]

	t10_t3 = S.Task('t10_t3', length=3, delay_cost=1)
	S += t10_t3 >= 1
	t10_t3 += MAS[3]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 1
	t7_t3_in += MM_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 1
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 1
	t7_t3_mem1 += MAIN_MEM_r[1]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 2
	t7_t1_in += MAS_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 2
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 2
	t7_t1_mem1 += MAIN_MEM_r[1]

	t7_t3 = S.Task('t7_t3', length=11, delay_cost=1)
	S += t7_t3 >= 2
	t7_t3 += MM[0]

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	S += t1_t1_in >= 3
	t1_t1_in += MAS_in[0]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	S += t1_t1_mem0 >= 3
	t1_t1_mem0 += MAIN_MEM_r[0]

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	S += t1_t1_mem1 >= 3
	t1_t1_mem1 += MAIN_MEM_r[1]

	t7_t1 = S.Task('t7_t1', length=3, delay_cost=1)
	S += t7_t1 >= 3
	t7_t1 += MAS[0]

	t1_t1 = S.Task('t1_t1', length=3, delay_cost=1)
	S += t1_t1 >= 4
	t1_t1 += MAS[0]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 4
	t7_t0_in += MAS_in[4]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 4
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 4
	t7_t0_mem1 += MAIN_MEM_r[1]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 5
	t5_t3_in += MAS_in[4]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 5
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 5
	t5_t3_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=3, delay_cost=1)
	S += t7_t0 >= 5
	t7_t0 += MAS[4]

	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	S += t10_t2_in >= 6
	t10_t2_in += MAS_in[0]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 6
	t10_t2_mem0 += MAIN_MEM_r[0]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 6
	t10_t2_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=3, delay_cost=1)
	S += t5_t3 >= 6
	t5_t3 += MAS[4]

	t10_t2 = S.Task('t10_t2', length=3, delay_cost=1)
	S += t10_t2 >= 7
	t10_t2 += MAS[0]

	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	S += t1_t0_in >= 7
	t1_t0_in += MAS_in[1]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	S += t1_t0_mem0 >= 7
	t1_t0_mem0 += MAIN_MEM_r[0]

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	S += t1_t0_mem1 >= 7
	t1_t0_mem1 += MAIN_MEM_r[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 8
	t0_t0_in += MAS_in[4]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 8
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 8
	t0_t0_mem1 += MAIN_MEM_r[1]

	t1_t0 = S.Task('t1_t0', length=3, delay_cost=1)
	S += t1_t0 >= 8
	t1_t0 += MAS[1]

	t0_t0 = S.Task('t0_t0', length=3, delay_cost=1)
	S += t0_t0 >= 9
	t0_t0 += MAS[4]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 9
	t5_t0_in += MM_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 9
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 9
	t5_t0_mem1 += MAIN_MEM_r[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 10
	t0_t1_in += MAS_in[2]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 10
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 10
	t0_t1_mem1 += MAIN_MEM_r[1]

	t5_t0 = S.Task('t5_t0', length=11, delay_cost=1)
	S += t5_t0 >= 10
	t5_t0 += MM[0]

	t0_t1 = S.Task('t0_t1', length=3, delay_cost=1)
	S += t0_t1 >= 11
	t0_t1 += MAS[2]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 11
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 11
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 11
	t5_t1_mem1 += MAIN_MEM_r[1]

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 12
	t10_t0_in += MM_in[0]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 12
	t10_t0_mem0 += MAIN_MEM_r[0]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 12
	t10_t0_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=11, delay_cost=1)
	S += t5_t1 >= 12
	t5_t1 += MM[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 13
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 13
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 13
	t0_t3_mem1 += MAIN_MEM_r[1]

	t10_t0 = S.Task('t10_t0', length=11, delay_cost=1)
	S += t10_t0 >= 13
	t10_t0 += MM[0]

	t0_t3 = S.Task('t0_t3', length=11, delay_cost=1)
	S += t0_t3 >= 14
	t0_t3 += MM[0]

	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	S += t1_t3_in >= 14
	t1_t3_in += MM_in[0]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	S += t1_t3_mem0 >= 14
	t1_t3_mem0 += MAIN_MEM_r[0]

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	S += t1_t3_mem1 >= 14
	t1_t3_mem1 += MAIN_MEM_r[1]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 15
	t10_t1_in += MM_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 15
	t10_t1_mem0 += MAIN_MEM_r[0]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 15
	t10_t1_mem1 += MAIN_MEM_r[1]

	t1_t3 = S.Task('t1_t3', length=11, delay_cost=1)
	S += t1_t3 >= 15
	t1_t3 += MM[0]

	t10_t1 = S.Task('t10_t1', length=11, delay_cost=1)
	S += t10_t1 >= 16
	t10_t1 += MM[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 16
	t5_t2_in += MAS_in[4]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 16
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 16
	t5_t2_mem1 += MAIN_MEM_r[1]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 17
	t2_t2_in += MAS_in[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 17
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 17
	t2_t2_mem1 += MAIN_MEM_r[1]

	t5_t2 = S.Task('t5_t2', length=3, delay_cost=1)
	S += t5_t2 >= 17
	t5_t2 += MAS[4]

	t2_t2 = S.Task('t2_t2', length=3, delay_cost=1)
	S += t2_t2 >= 18
	t2_t2 += MAS[0]


	# new tasks
	t0_t2 = S.Task('t0_t2', length=11, delay_cost=1)
	t0_t2 += alt(MM)
	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	t0_t2_in += alt(MM_in)
	S += t0_t2_in*MM_in[0]<=t0_t2*MM[0]
	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	t0_t2_mem0 += MAS_MEM[8]
	S += 11 < t0_t2_mem0
	S += t0_t2_mem0 <= t0_t2

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	t0_t2_mem1 += MAS_MEM[5]
	S += 13 < t0_t2_mem1
	S += t0_t2_mem1 <= t0_t2

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	t0_t5 += alt(MAS)
	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	t0_t5_in += alt(MAS_in)
	S += t0_t5_in*MAS_in[0]<=t0_t5*MAS[0]

	S += t0_t5_in*MAS_in[1]<=t0_t5*MAS[1]

	S += t0_t5_in*MAS_in[2]<=t0_t5*MAS[2]

	S += t0_t5_in*MAS_in[3]<=t0_t5*MAS[3]

	S += t0_t5_in*MAS_in[4]<=t0_t5*MAS[4]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += MM_MEM[0]
	S += 24 < t0_t5_mem0
	S += t0_t5_mem0 <= t0_t5

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	t0_t5_mem1 += MM_MEM[1]
	S += 24 < t0_t5_mem1
	S += t0_t5_mem1 <= t0_t5

	t01 = S.Task('t01', length=3, delay_cost=1)
	t01 += alt(MAS)
	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	t01_in += alt(MAS_in)
	S += t01_in*MAS_in[0]<=t01*MAS[0]

	S += t01_in*MAS_in[1]<=t01*MAS[1]

	S += t01_in*MAS_in[2]<=t01*MAS[2]

	S += t01_in*MAS_in[3]<=t01*MAS[3]

	S += t01_in*MAS_in[4]<=t01*MAS[4]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += MM_MEM[0]
	S += 24 < t01_mem0
	S += t01_mem0 <= t01

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	t01_mem1 += MM_MEM[1]
	S += 24 < t01_mem1
	S += t01_mem1 <= t01

	t1_t2 = S.Task('t1_t2', length=11, delay_cost=1)
	t1_t2 += alt(MM)
	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	t1_t2_in += alt(MM_in)
	S += t1_t2_in*MM_in[0]<=t1_t2*MM[0]
	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	t1_t2_mem0 += MAS_MEM[2]
	S += 10 < t1_t2_mem0
	S += t1_t2_mem0 <= t1_t2

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	t1_t2_mem1 += MAS_MEM[1]
	S += 6 < t1_t2_mem1
	S += t1_t2_mem1 <= t1_t2

	t1_t5 = S.Task('t1_t5', length=3, delay_cost=1)
	t1_t5 += alt(MAS)
	t1_t5_in = S.Task('t1_t5_in', length=1, delay_cost=1)
	t1_t5_in += alt(MAS_in)
	S += t1_t5_in*MAS_in[0]<=t1_t5*MAS[0]

	S += t1_t5_in*MAS_in[1]<=t1_t5*MAS[1]

	S += t1_t5_in*MAS_in[2]<=t1_t5*MAS[2]

	S += t1_t5_in*MAS_in[3]<=t1_t5*MAS[3]

	S += t1_t5_in*MAS_in[4]<=t1_t5*MAS[4]

	t1_t5_mem0 = S.Task('t1_t5_mem0', length=1, delay_cost=1)
	t1_t5_mem0 += MM_MEM[0]
	S += 25 < t1_t5_mem0
	S += t1_t5_mem0 <= t1_t5

	t1_t5_mem1 = S.Task('t1_t5_mem1', length=1, delay_cost=1)
	t1_t5_mem1 += MM_MEM[1]
	S += 25 < t1_t5_mem1
	S += t1_t5_mem1 <= t1_t5

	t11 = S.Task('t11', length=3, delay_cost=1)
	t11 += alt(MAS)
	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	t11_in += alt(MAS_in)
	S += t11_in*MAS_in[0]<=t11*MAS[0]

	S += t11_in*MAS_in[1]<=t11*MAS[1]

	S += t11_in*MAS_in[2]<=t11*MAS[2]

	S += t11_in*MAS_in[3]<=t11*MAS[3]

	S += t11_in*MAS_in[4]<=t11*MAS[4]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += MM_MEM[0]
	S += 25 < t11_mem0
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += MM_MEM[1]
	S += 25 < t11_mem1
	S += t11_mem1 <= t11

	t5_t4 = S.Task('t5_t4', length=11, delay_cost=1)
	t5_t4 += alt(MM)
	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	t5_t4_in += alt(MM_in)
	S += t5_t4_in*MM_in[0]<=t5_t4*MM[0]
	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	t5_t4_mem0 += MAS_MEM[8]
	S += 19 < t5_t4_mem0
	S += t5_t4_mem0 <= t5_t4

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	t5_t4_mem1 += MAS_MEM[9]
	S += 8 < t5_t4_mem1
	S += t5_t4_mem1 <= t5_t4

	t50 = S.Task('t50', length=3, delay_cost=1)
	t50 += alt(MAS)
	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	t50_in += alt(MAS_in)
	S += t50_in*MAS_in[0]<=t50*MAS[0]

	S += t50_in*MAS_in[1]<=t50*MAS[1]

	S += t50_in*MAS_in[2]<=t50*MAS[2]

	S += t50_in*MAS_in[3]<=t50*MAS[3]

	S += t50_in*MAS_in[4]<=t50*MAS[4]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	t50_mem0 += MM_MEM[0]
	S += 20 < t50_mem0
	S += t50_mem0 <= t50

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	t50_mem1 += MM_MEM[1]
	S += 22 < t50_mem1
	S += t50_mem1 <= t50

	t5_t5 = S.Task('t5_t5', length=3, delay_cost=1)
	t5_t5 += alt(MAS)
	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	t5_t5_in += alt(MAS_in)
	S += t5_t5_in*MAS_in[0]<=t5_t5*MAS[0]

	S += t5_t5_in*MAS_in[1]<=t5_t5*MAS[1]

	S += t5_t5_in*MAS_in[2]<=t5_t5*MAS[2]

	S += t5_t5_in*MAS_in[3]<=t5_t5*MAS[3]

	S += t5_t5_in*MAS_in[4]<=t5_t5*MAS[4]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	t5_t5_mem0 += MM_MEM[0]
	S += 20 < t5_t5_mem0
	S += t5_t5_mem0 <= t5_t5

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	t5_t5_mem1 += MM_MEM[1]
	S += 22 < t5_t5_mem1
	S += t5_t5_mem1 <= t5_t5

	t7_t2 = S.Task('t7_t2', length=11, delay_cost=1)
	t7_t2 += alt(MM)
	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	t7_t2_in += alt(MM_in)
	S += t7_t2_in*MM_in[0]<=t7_t2*MM[0]
	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	t7_t2_mem0 += MAS_MEM[8]
	S += 7 < t7_t2_mem0
	S += t7_t2_mem0 <= t7_t2

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	t7_t2_mem1 += MAS_MEM[1]
	S += 5 < t7_t2_mem1
	S += t7_t2_mem1 <= t7_t2

	t7_t5 = S.Task('t7_t5', length=3, delay_cost=1)
	t7_t5 += alt(MAS)
	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	t7_t5_in += alt(MAS_in)
	S += t7_t5_in*MAS_in[0]<=t7_t5*MAS[0]

	S += t7_t5_in*MAS_in[1]<=t7_t5*MAS[1]

	S += t7_t5_in*MAS_in[2]<=t7_t5*MAS[2]

	S += t7_t5_in*MAS_in[3]<=t7_t5*MAS[3]

	S += t7_t5_in*MAS_in[4]<=t7_t5*MAS[4]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	t7_t5_mem0 += MM_MEM[0]
	S += 12 < t7_t5_mem0
	S += t7_t5_mem0 <= t7_t5

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	t7_t5_mem1 += MM_MEM[1]
	S += 12 < t7_t5_mem1
	S += t7_t5_mem1 <= t7_t5

	t71 = S.Task('t71', length=3, delay_cost=1)
	t71 += alt(MAS)
	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	t71_in += alt(MAS_in)
	S += t71_in*MAS_in[0]<=t71*MAS[0]

	S += t71_in*MAS_in[1]<=t71*MAS[1]

	S += t71_in*MAS_in[2]<=t71*MAS[2]

	S += t71_in*MAS_in[3]<=t71*MAS[3]

	S += t71_in*MAS_in[4]<=t71*MAS[4]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	t71_mem0 += MM_MEM[0]
	S += 12 < t71_mem0
	S += t71_mem0 <= t71

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	t71_mem1 += MM_MEM[1]
	S += 12 < t71_mem1
	S += t71_mem1 <= t71

	t10_t4 = S.Task('t10_t4', length=11, delay_cost=1)
	t10_t4 += alt(MM)
	t10_t4_in = S.Task('t10_t4_in', length=1, delay_cost=1)
	t10_t4_in += alt(MM_in)
	S += t10_t4_in*MM_in[0]<=t10_t4*MM[0]
	t10_t4_mem0 = S.Task('t10_t4_mem0', length=1, delay_cost=1)
	t10_t4_mem0 += MAS_MEM[0]
	S += 9 < t10_t4_mem0
	S += t10_t4_mem0 <= t10_t4

	t10_t4_mem1 = S.Task('t10_t4_mem1', length=1, delay_cost=1)
	t10_t4_mem1 += MAS_MEM[7]
	S += 3 < t10_t4_mem1
	S += t10_t4_mem1 <= t10_t4

	t100 = S.Task('t100', length=3, delay_cost=1)
	t100 += alt(MAS)
	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	t100_in += alt(MAS_in)
	S += t100_in*MAS_in[0]<=t100*MAS[0]

	S += t100_in*MAS_in[1]<=t100*MAS[1]

	S += t100_in*MAS_in[2]<=t100*MAS[2]

	S += t100_in*MAS_in[3]<=t100*MAS[3]

	S += t100_in*MAS_in[4]<=t100*MAS[4]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += MM_MEM[0]
	S += 23 < t100_mem0
	S += t100_mem0 <= t100

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	t100_mem1 += MM_MEM[1]
	S += 26 < t100_mem1
	S += t100_mem1 <= t100

	t10_t5 = S.Task('t10_t5', length=3, delay_cost=1)
	t10_t5 += alt(MAS)
	t10_t5_in = S.Task('t10_t5_in', length=1, delay_cost=1)
	t10_t5_in += alt(MAS_in)
	S += t10_t5_in*MAS_in[0]<=t10_t5*MAS[0]

	S += t10_t5_in*MAS_in[1]<=t10_t5*MAS[1]

	S += t10_t5_in*MAS_in[2]<=t10_t5*MAS[2]

	S += t10_t5_in*MAS_in[3]<=t10_t5*MAS[3]

	S += t10_t5_in*MAS_in[4]<=t10_t5*MAS[4]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	t10_t5_mem0 += MM_MEM[0]
	S += 23 < t10_t5_mem0
	S += t10_t5_mem0 <= t10_t5

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	t10_t5_mem1 += MM_MEM[1]
	S += 26 < t10_t5_mem1
	S += t10_t5_mem1 <= t10_t5

	t00 = S.Task('t00', length=3, delay_cost=1)
	t00 += alt(MAS)
	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	t00_in += alt(MAS_in)
	S += t00_in*MAS_in[0]<=t00*MAS[0]

	S += t00_in*MAS_in[1]<=t00*MAS[1]

	S += t00_in*MAS_in[2]<=t00*MAS[2]

	S += t00_in*MAS_in[3]<=t00*MAS[3]

	S += t00_in*MAS_in[4]<=t00*MAS[4]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += alt(MM_MEM)
	S += (t0_t2*MM[0])-1 < t00_mem0*MM_MEM[0]
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += alt(MAS_MEM)
	S += (t0_t5*MAS[0])-1 < t00_mem1*MAS_MEM[1]
	S += (t0_t5*MAS[1])-1 < t00_mem1*MAS_MEM[3]
	S += (t0_t5*MAS[2])-1 < t00_mem1*MAS_MEM[5]
	S += (t0_t5*MAS[3])-1 < t00_mem1*MAS_MEM[7]
	S += (t0_t5*MAS[4])-1 < t00_mem1*MAS_MEM[9]
	S += t00_mem1 <= t00

	t10 = S.Task('t10', length=3, delay_cost=1)
	t10 += alt(MAS)
	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	t10_in += alt(MAS_in)
	S += t10_in*MAS_in[0]<=t10*MAS[0]

	S += t10_in*MAS_in[1]<=t10*MAS[1]

	S += t10_in*MAS_in[2]<=t10*MAS[2]

	S += t10_in*MAS_in[3]<=t10*MAS[3]

	S += t10_in*MAS_in[4]<=t10*MAS[4]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += alt(MM_MEM)
	S += (t1_t2*MM[0])-1 < t10_mem0*MM_MEM[0]
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += alt(MAS_MEM)
	S += (t1_t5*MAS[0])-1 < t10_mem1*MAS_MEM[1]
	S += (t1_t5*MAS[1])-1 < t10_mem1*MAS_MEM[3]
	S += (t1_t5*MAS[2])-1 < t10_mem1*MAS_MEM[5]
	S += (t1_t5*MAS[3])-1 < t10_mem1*MAS_MEM[7]
	S += (t1_t5*MAS[4])-1 < t10_mem1*MAS_MEM[9]
	S += t10_mem1 <= t10

	t2_t1 = S.Task('t2_t1', length=11, delay_cost=1)
	t2_t1 += alt(MM)
	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	t2_t1_in += alt(MM_in)
	S += t2_t1_in*MM_in[0]<=t2_t1*MM[0]
	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	t2_t1_mem0 += MAIN_MEM_r[0]
	S += t2_t1_mem0 <= t2_t1

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	t2_t1_mem1 += alt(MAS_MEM)
	S += (t11*MAS[0])-1 < t2_t1_mem1*MAS_MEM[1]
	S += (t11*MAS[1])-1 < t2_t1_mem1*MAS_MEM[3]
	S += (t11*MAS[2])-1 < t2_t1_mem1*MAS_MEM[5]
	S += (t11*MAS[3])-1 < t2_t1_mem1*MAS_MEM[7]
	S += (t11*MAS[4])-1 < t2_t1_mem1*MAS_MEM[9]
	S += t2_t1_mem1 <= t2_t1

	t51 = S.Task('t51', length=3, delay_cost=1)
	t51 += alt(MAS)
	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	t51_in += alt(MAS_in)
	S += t51_in*MAS_in[0]<=t51*MAS[0]

	S += t51_in*MAS_in[1]<=t51*MAS[1]

	S += t51_in*MAS_in[2]<=t51*MAS[2]

	S += t51_in*MAS_in[3]<=t51*MAS[3]

	S += t51_in*MAS_in[4]<=t51*MAS[4]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	t51_mem0 += alt(MM_MEM)
	S += (t5_t4*MM[0])-1 < t51_mem0*MM_MEM[0]
	S += t51_mem0 <= t51

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	t51_mem1 += alt(MAS_MEM)
	S += (t5_t5*MAS[0])-1 < t51_mem1*MAS_MEM[1]
	S += (t5_t5*MAS[1])-1 < t51_mem1*MAS_MEM[3]
	S += (t5_t5*MAS[2])-1 < t51_mem1*MAS_MEM[5]
	S += (t5_t5*MAS[3])-1 < t51_mem1*MAS_MEM[7]
	S += (t5_t5*MAS[4])-1 < t51_mem1*MAS_MEM[9]
	S += t51_mem1 <= t51

	t60 = S.Task('t60', length=3, delay_cost=1)
	t60 += alt(MAS)
	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	t60_in += alt(MAS_in)
	S += t60_in*MAS_in[0]<=t60*MAS[0]

	S += t60_in*MAS_in[1]<=t60*MAS[1]

	S += t60_in*MAS_in[2]<=t60*MAS[2]

	S += t60_in*MAS_in[3]<=t60*MAS[3]

	S += t60_in*MAS_in[4]<=t60*MAS[4]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	t60_mem0 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t60_mem0*MAS_MEM[0]
	S += (t50*MAS[1])-1 < t60_mem0*MAS_MEM[2]
	S += (t50*MAS[2])-1 < t60_mem0*MAS_MEM[4]
	S += (t50*MAS[3])-1 < t60_mem0*MAS_MEM[6]
	S += (t50*MAS[4])-1 < t60_mem0*MAS_MEM[8]
	S += t60_mem0 <= t60

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	t60_mem1 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t60_mem1*MAS_MEM[1]
	S += (t50*MAS[1])-1 < t60_mem1*MAS_MEM[3]
	S += (t50*MAS[2])-1 < t60_mem1*MAS_MEM[5]
	S += (t50*MAS[3])-1 < t60_mem1*MAS_MEM[7]
	S += (t50*MAS[4])-1 < t60_mem1*MAS_MEM[9]
	S += t60_mem1 <= t60

	t70 = S.Task('t70', length=3, delay_cost=1)
	t70 += alt(MAS)
	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	t70_in += alt(MAS_in)
	S += t70_in*MAS_in[0]<=t70*MAS[0]

	S += t70_in*MAS_in[1]<=t70*MAS[1]

	S += t70_in*MAS_in[2]<=t70*MAS[2]

	S += t70_in*MAS_in[3]<=t70*MAS[3]

	S += t70_in*MAS_in[4]<=t70*MAS[4]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += alt(MM_MEM)
	S += (t7_t2*MM[0])-1 < t70_mem0*MM_MEM[0]
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += alt(MAS_MEM)
	S += (t7_t5*MAS[0])-1 < t70_mem1*MAS_MEM[1]
	S += (t7_t5*MAS[1])-1 < t70_mem1*MAS_MEM[3]
	S += (t7_t5*MAS[2])-1 < t70_mem1*MAS_MEM[5]
	S += (t7_t5*MAS[3])-1 < t70_mem1*MAS_MEM[7]
	S += (t7_t5*MAS[4])-1 < t70_mem1*MAS_MEM[9]
	S += t70_mem1 <= t70

	t81 = S.Task('t81', length=3, delay_cost=1)
	t81 += alt(MAS)
	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	t81_in += alt(MAS_in)
	S += t81_in*MAS_in[0]<=t81*MAS[0]

	S += t81_in*MAS_in[1]<=t81*MAS[1]

	S += t81_in*MAS_in[2]<=t81*MAS[2]

	S += t81_in*MAS_in[3]<=t81*MAS[3]

	S += t81_in*MAS_in[4]<=t81*MAS[4]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += alt(MAS_MEM)
	S += (t71*MAS[0])-1 < t81_mem0*MAS_MEM[0]
	S += (t71*MAS[1])-1 < t81_mem0*MAS_MEM[2]
	S += (t71*MAS[2])-1 < t81_mem0*MAS_MEM[4]
	S += (t71*MAS[3])-1 < t81_mem0*MAS_MEM[6]
	S += (t71*MAS[4])-1 < t81_mem0*MAS_MEM[8]
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += alt(MAS_MEM)
	S += (t71*MAS[0])-1 < t81_mem1*MAS_MEM[1]
	S += (t71*MAS[1])-1 < t81_mem1*MAS_MEM[3]
	S += (t71*MAS[2])-1 < t81_mem1*MAS_MEM[5]
	S += (t71*MAS[3])-1 < t81_mem1*MAS_MEM[7]
	S += (t71*MAS[4])-1 < t81_mem1*MAS_MEM[9]
	S += t81_mem1 <= t81

	t101 = S.Task('t101', length=3, delay_cost=1)
	t101 += alt(MAS)
	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	t101_in += alt(MAS_in)
	S += t101_in*MAS_in[0]<=t101*MAS[0]

	S += t101_in*MAS_in[1]<=t101*MAS[1]

	S += t101_in*MAS_in[2]<=t101*MAS[2]

	S += t101_in*MAS_in[3]<=t101*MAS[3]

	S += t101_in*MAS_in[4]<=t101*MAS[4]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += alt(MM_MEM)
	S += (t10_t4*MM[0])-1 < t101_mem0*MM_MEM[0]
	S += t101_mem0 <= t101

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	t101_mem1 += alt(MAS_MEM)
	S += (t10_t5*MAS[0])-1 < t101_mem1*MAS_MEM[1]
	S += (t10_t5*MAS[1])-1 < t101_mem1*MAS_MEM[3]
	S += (t10_t5*MAS[2])-1 < t101_mem1*MAS_MEM[5]
	S += (t10_t5*MAS[3])-1 < t101_mem1*MAS_MEM[7]
	S += (t10_t5*MAS[4])-1 < t101_mem1*MAS_MEM[9]
	S += t101_mem1 <= t101

	t110 = S.Task('t110', length=3, delay_cost=1)
	t110 += alt(MAS)
	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	t110_in += alt(MAS_in)
	S += t110_in*MAS_in[0]<=t110*MAS[0]

	S += t110_in*MAS_in[1]<=t110*MAS[1]

	S += t110_in*MAS_in[2]<=t110*MAS[2]

	S += t110_in*MAS_in[3]<=t110*MAS[3]

	S += t110_in*MAS_in[4]<=t110*MAS[4]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(MAS_MEM)
	S += (t100*MAS[0])-1 < t110_mem0*MAS_MEM[0]
	S += (t100*MAS[1])-1 < t110_mem0*MAS_MEM[2]
	S += (t100*MAS[2])-1 < t110_mem0*MAS_MEM[4]
	S += (t100*MAS[3])-1 < t110_mem0*MAS_MEM[6]
	S += (t100*MAS[4])-1 < t110_mem0*MAS_MEM[8]
	S += t110_mem0 <= t110

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	t110_mem1 += alt(MAS_MEM)
	S += (t100*MAS[0])-1 < t110_mem1*MAS_MEM[1]
	S += (t100*MAS[1])-1 < t110_mem1*MAS_MEM[3]
	S += (t100*MAS[2])-1 < t110_mem1*MAS_MEM[5]
	S += (t100*MAS[3])-1 < t110_mem1*MAS_MEM[7]
	S += (t100*MAS[4])-1 < t110_mem1*MAS_MEM[9]
	S += t110_mem1 <= t110

	t2_t0 = S.Task('t2_t0', length=11, delay_cost=1)
	t2_t0 += alt(MM)
	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	t2_t0_in += alt(MM_in)
	S += t2_t0_in*MM_in[0]<=t2_t0*MM[0]
	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	t2_t0_mem0 += MAIN_MEM_r[0]
	S += t2_t0_mem0 <= t2_t0

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	t2_t0_mem1 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t2_t0_mem1*MAS_MEM[1]
	S += (t10*MAS[1])-1 < t2_t0_mem1*MAS_MEM[3]
	S += (t10*MAS[2])-1 < t2_t0_mem1*MAS_MEM[5]
	S += (t10*MAS[3])-1 < t2_t0_mem1*MAS_MEM[7]
	S += (t10*MAS[4])-1 < t2_t0_mem1*MAS_MEM[9]
	S += t2_t0_mem1 <= t2_t0

	t2_t3 = S.Task('t2_t3', length=3, delay_cost=1)
	t2_t3 += alt(MAS)
	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	t2_t3_in += alt(MAS_in)
	S += t2_t3_in*MAS_in[0]<=t2_t3*MAS[0]

	S += t2_t3_in*MAS_in[1]<=t2_t3*MAS[1]

	S += t2_t3_in*MAS_in[2]<=t2_t3*MAS[2]

	S += t2_t3_in*MAS_in[3]<=t2_t3*MAS[3]

	S += t2_t3_in*MAS_in[4]<=t2_t3*MAS[4]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	t2_t3_mem0 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t2_t3_mem0*MAS_MEM[0]
	S += (t10*MAS[1])-1 < t2_t3_mem0*MAS_MEM[2]
	S += (t10*MAS[2])-1 < t2_t3_mem0*MAS_MEM[4]
	S += (t10*MAS[3])-1 < t2_t3_mem0*MAS_MEM[6]
	S += (t10*MAS[4])-1 < t2_t3_mem0*MAS_MEM[8]
	S += t2_t3_mem0 <= t2_t3

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	t2_t3_mem1 += alt(MAS_MEM)
	S += (t11*MAS[0])-1 < t2_t3_mem1*MAS_MEM[1]
	S += (t11*MAS[1])-1 < t2_t3_mem1*MAS_MEM[3]
	S += (t11*MAS[2])-1 < t2_t3_mem1*MAS_MEM[5]
	S += (t11*MAS[3])-1 < t2_t3_mem1*MAS_MEM[7]
	S += (t11*MAS[4])-1 < t2_t3_mem1*MAS_MEM[9]
	S += t2_t3_mem1 <= t2_t3

	t61 = S.Task('t61', length=3, delay_cost=1)
	t61 += alt(MAS)
	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	t61_in += alt(MAS_in)
	S += t61_in*MAS_in[0]<=t61*MAS[0]

	S += t61_in*MAS_in[1]<=t61*MAS[1]

	S += t61_in*MAS_in[2]<=t61*MAS[2]

	S += t61_in*MAS_in[3]<=t61*MAS[3]

	S += t61_in*MAS_in[4]<=t61*MAS[4]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	t61_mem0 += alt(MAS_MEM)
	S += (t51*MAS[0])-1 < t61_mem0*MAS_MEM[0]
	S += (t51*MAS[1])-1 < t61_mem0*MAS_MEM[2]
	S += (t51*MAS[2])-1 < t61_mem0*MAS_MEM[4]
	S += (t51*MAS[3])-1 < t61_mem0*MAS_MEM[6]
	S += (t51*MAS[4])-1 < t61_mem0*MAS_MEM[8]
	S += t61_mem0 <= t61

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	t61_mem1 += alt(MAS_MEM)
	S += (t51*MAS[0])-1 < t61_mem1*MAS_MEM[1]
	S += (t51*MAS[1])-1 < t61_mem1*MAS_MEM[3]
	S += (t51*MAS[2])-1 < t61_mem1*MAS_MEM[5]
	S += (t51*MAS[3])-1 < t61_mem1*MAS_MEM[7]
	S += (t51*MAS[4])-1 < t61_mem1*MAS_MEM[9]
	S += t61_mem1 <= t61

	t80 = S.Task('t80', length=3, delay_cost=1)
	t80 += alt(MAS)
	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	t80_in += alt(MAS_in)
	S += t80_in*MAS_in[0]<=t80*MAS[0]

	S += t80_in*MAS_in[1]<=t80*MAS[1]

	S += t80_in*MAS_in[2]<=t80*MAS[2]

	S += t80_in*MAS_in[3]<=t80*MAS[3]

	S += t80_in*MAS_in[4]<=t80*MAS[4]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t80_mem0*MAS_MEM[0]
	S += (t70*MAS[1])-1 < t80_mem0*MAS_MEM[2]
	S += (t70*MAS[2])-1 < t80_mem0*MAS_MEM[4]
	S += (t70*MAS[3])-1 < t80_mem0*MAS_MEM[6]
	S += (t70*MAS[4])-1 < t80_mem0*MAS_MEM[8]
	S += t80_mem0 <= t80

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	t80_mem1 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t80_mem1*MAS_MEM[1]
	S += (t70*MAS[1])-1 < t80_mem1*MAS_MEM[3]
	S += (t70*MAS[2])-1 < t80_mem1*MAS_MEM[5]
	S += (t70*MAS[3])-1 < t80_mem1*MAS_MEM[7]
	S += (t70*MAS[4])-1 < t80_mem1*MAS_MEM[9]
	S += t80_mem1 <= t80

	t91 = S.Task('t91', length=3, delay_cost=1)
	t91 += alt(MAS)
	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	t91_in += alt(MAS_in)
	S += t91_in*MAS_in[0]<=t91*MAS[0]

	S += t91_in*MAS_in[1]<=t91*MAS[1]

	S += t91_in*MAS_in[2]<=t91*MAS[2]

	S += t91_in*MAS_in[3]<=t91*MAS[3]

	S += t91_in*MAS_in[4]<=t91*MAS[4]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	t91_mem0 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t91_mem0*MAS_MEM[0]
	S += (t81*MAS[1])-1 < t91_mem0*MAS_MEM[2]
	S += (t81*MAS[2])-1 < t91_mem0*MAS_MEM[4]
	S += (t81*MAS[3])-1 < t91_mem0*MAS_MEM[6]
	S += (t81*MAS[4])-1 < t91_mem0*MAS_MEM[8]
	S += t91_mem0 <= t91

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	t91_mem1 += alt(MAS_MEM)
	S += (t71*MAS[0])-1 < t91_mem1*MAS_MEM[1]
	S += (t71*MAS[1])-1 < t91_mem1*MAS_MEM[3]
	S += (t71*MAS[2])-1 < t91_mem1*MAS_MEM[5]
	S += (t71*MAS[3])-1 < t91_mem1*MAS_MEM[7]
	S += (t71*MAS[4])-1 < t91_mem1*MAS_MEM[9]
	S += t91_mem1 <= t91

	t111 = S.Task('t111', length=3, delay_cost=1)
	t111 += alt(MAS)
	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	t111_in += alt(MAS_in)
	S += t111_in*MAS_in[0]<=t111*MAS[0]

	S += t111_in*MAS_in[1]<=t111*MAS[1]

	S += t111_in*MAS_in[2]<=t111*MAS[2]

	S += t111_in*MAS_in[3]<=t111*MAS[3]

	S += t111_in*MAS_in[4]<=t111*MAS[4]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += alt(MAS_MEM)
	S += (t101*MAS[0])-1 < t111_mem0*MAS_MEM[0]
	S += (t101*MAS[1])-1 < t111_mem0*MAS_MEM[2]
	S += (t101*MAS[2])-1 < t111_mem0*MAS_MEM[4]
	S += (t101*MAS[3])-1 < t111_mem0*MAS_MEM[6]
	S += (t101*MAS[4])-1 < t111_mem0*MAS_MEM[8]
	S += t111_mem0 <= t111

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	t111_mem1 += alt(MAS_MEM)
	S += (t101*MAS[0])-1 < t111_mem1*MAS_MEM[1]
	S += (t101*MAS[1])-1 < t111_mem1*MAS_MEM[3]
	S += (t101*MAS[2])-1 < t111_mem1*MAS_MEM[5]
	S += (t101*MAS[3])-1 < t111_mem1*MAS_MEM[7]
	S += (t101*MAS[4])-1 < t111_mem1*MAS_MEM[9]
	S += t111_mem1 <= t111

	t12_t0 = S.Task('t12_t0', length=11, delay_cost=1)
	t12_t0 += alt(MM)
	t12_t0_in = S.Task('t12_t0_in', length=1, delay_cost=1)
	t12_t0_in += alt(MM_in)
	S += t12_t0_in*MM_in[0]<=t12_t0*MM[0]
	t12_t0_mem0 = S.Task('t12_t0_mem0', length=1, delay_cost=1)
	t12_t0_mem0 += alt(MAS_MEM)
	S += (t00*MAS[0])-1 < t12_t0_mem0*MAS_MEM[0]
	S += (t00*MAS[1])-1 < t12_t0_mem0*MAS_MEM[2]
	S += (t00*MAS[2])-1 < t12_t0_mem0*MAS_MEM[4]
	S += (t00*MAS[3])-1 < t12_t0_mem0*MAS_MEM[6]
	S += (t00*MAS[4])-1 < t12_t0_mem0*MAS_MEM[8]
	S += t12_t0_mem0 <= t12_t0

	t12_t0_mem1 = S.Task('t12_t0_mem1', length=1, delay_cost=1)
	t12_t0_mem1 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < t12_t0_mem1*MAS_MEM[1]
	S += (t110*MAS[1])-1 < t12_t0_mem1*MAS_MEM[3]
	S += (t110*MAS[2])-1 < t12_t0_mem1*MAS_MEM[5]
	S += (t110*MAS[3])-1 < t12_t0_mem1*MAS_MEM[7]
	S += (t110*MAS[4])-1 < t12_t0_mem1*MAS_MEM[9]
	S += t12_t0_mem1 <= t12_t0

	t12_t2 = S.Task('t12_t2', length=3, delay_cost=1)
	t12_t2 += alt(MAS)
	t12_t2_in = S.Task('t12_t2_in', length=1, delay_cost=1)
	t12_t2_in += alt(MAS_in)
	S += t12_t2_in*MAS_in[0]<=t12_t2*MAS[0]

	S += t12_t2_in*MAS_in[1]<=t12_t2*MAS[1]

	S += t12_t2_in*MAS_in[2]<=t12_t2*MAS[2]

	S += t12_t2_in*MAS_in[3]<=t12_t2*MAS[3]

	S += t12_t2_in*MAS_in[4]<=t12_t2*MAS[4]

	t12_t2_mem0 = S.Task('t12_t2_mem0', length=1, delay_cost=1)
	t12_t2_mem0 += alt(MAS_MEM)
	S += (t00*MAS[0])-1 < t12_t2_mem0*MAS_MEM[0]
	S += (t00*MAS[1])-1 < t12_t2_mem0*MAS_MEM[2]
	S += (t00*MAS[2])-1 < t12_t2_mem0*MAS_MEM[4]
	S += (t00*MAS[3])-1 < t12_t2_mem0*MAS_MEM[6]
	S += (t00*MAS[4])-1 < t12_t2_mem0*MAS_MEM[8]
	S += t12_t2_mem0 <= t12_t2

	t12_t2_mem1 = S.Task('t12_t2_mem1', length=1, delay_cost=1)
	t12_t2_mem1 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t12_t2_mem1*MAS_MEM[1]
	S += (t01*MAS[1])-1 < t12_t2_mem1*MAS_MEM[3]
	S += (t01*MAS[2])-1 < t12_t2_mem1*MAS_MEM[5]
	S += (t01*MAS[3])-1 < t12_t2_mem1*MAS_MEM[7]
	S += (t01*MAS[4])-1 < t12_t2_mem1*MAS_MEM[9]
	S += t12_t2_mem1 <= t12_t2

	t18_t0 = S.Task('t18_t0', length=3, delay_cost=1)
	t18_t0 += alt(MAS)
	t18_t0_in = S.Task('t18_t0_in', length=1, delay_cost=1)
	t18_t0_in += alt(MAS_in)
	S += t18_t0_in*MAS_in[0]<=t18_t0*MAS[0]

	S += t18_t0_in*MAS_in[1]<=t18_t0*MAS[1]

	S += t18_t0_in*MAS_in[2]<=t18_t0*MAS[2]

	S += t18_t0_in*MAS_in[3]<=t18_t0*MAS[3]

	S += t18_t0_in*MAS_in[4]<=t18_t0*MAS[4]

	t18_t0_mem0 = S.Task('t18_t0_mem0', length=1, delay_cost=1)
	t18_t0_mem0 += alt(MAS_MEM)
	S += (t00*MAS[0])-1 < t18_t0_mem0*MAS_MEM[0]
	S += (t00*MAS[1])-1 < t18_t0_mem0*MAS_MEM[2]
	S += (t00*MAS[2])-1 < t18_t0_mem0*MAS_MEM[4]
	S += (t00*MAS[3])-1 < t18_t0_mem0*MAS_MEM[6]
	S += (t00*MAS[4])-1 < t18_t0_mem0*MAS_MEM[8]
	S += t18_t0_mem0 <= t18_t0

	t18_t0_mem1 = S.Task('t18_t0_mem1', length=1, delay_cost=1)
	t18_t0_mem1 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t18_t0_mem1*MAS_MEM[1]
	S += (t01*MAS[1])-1 < t18_t0_mem1*MAS_MEM[3]
	S += (t01*MAS[2])-1 < t18_t0_mem1*MAS_MEM[5]
	S += (t01*MAS[3])-1 < t18_t0_mem1*MAS_MEM[7]
	S += (t01*MAS[4])-1 < t18_t0_mem1*MAS_MEM[9]
	S += t18_t0_mem1 <= t18_t0

	t18_t1 = S.Task('t18_t1', length=3, delay_cost=1)
	t18_t1 += alt(MAS)
	t18_t1_in = S.Task('t18_t1_in', length=1, delay_cost=1)
	t18_t1_in += alt(MAS_in)
	S += t18_t1_in*MAS_in[0]<=t18_t1*MAS[0]

	S += t18_t1_in*MAS_in[1]<=t18_t1*MAS[1]

	S += t18_t1_in*MAS_in[2]<=t18_t1*MAS[2]

	S += t18_t1_in*MAS_in[3]<=t18_t1*MAS[3]

	S += t18_t1_in*MAS_in[4]<=t18_t1*MAS[4]

	t18_t1_mem0 = S.Task('t18_t1_mem0', length=1, delay_cost=1)
	t18_t1_mem0 += alt(MAS_MEM)
	S += (t00*MAS[0])-1 < t18_t1_mem0*MAS_MEM[0]
	S += (t00*MAS[1])-1 < t18_t1_mem0*MAS_MEM[2]
	S += (t00*MAS[2])-1 < t18_t1_mem0*MAS_MEM[4]
	S += (t00*MAS[3])-1 < t18_t1_mem0*MAS_MEM[6]
	S += (t00*MAS[4])-1 < t18_t1_mem0*MAS_MEM[8]
	S += t18_t1_mem0 <= t18_t1

	t18_t1_mem1 = S.Task('t18_t1_mem1', length=1, delay_cost=1)
	t18_t1_mem1 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t18_t1_mem1*MAS_MEM[1]
	S += (t01*MAS[1])-1 < t18_t1_mem1*MAS_MEM[3]
	S += (t01*MAS[2])-1 < t18_t1_mem1*MAS_MEM[5]
	S += (t01*MAS[3])-1 < t18_t1_mem1*MAS_MEM[7]
	S += (t01*MAS[4])-1 < t18_t1_mem1*MAS_MEM[9]
	S += t18_t1_mem1 <= t18_t1

	t18_t3 = S.Task('t18_t3', length=11, delay_cost=1)
	t18_t3 += alt(MM)
	t18_t3_in = S.Task('t18_t3_in', length=1, delay_cost=1)
	t18_t3_in += alt(MM_in)
	S += t18_t3_in*MM_in[0]<=t18_t3*MM[0]
	t18_t3_mem0 = S.Task('t18_t3_mem0', length=1, delay_cost=1)
	t18_t3_mem0 += alt(MAS_MEM)
	S += (t00*MAS[0])-1 < t18_t3_mem0*MAS_MEM[0]
	S += (t00*MAS[1])-1 < t18_t3_mem0*MAS_MEM[2]
	S += (t00*MAS[2])-1 < t18_t3_mem0*MAS_MEM[4]
	S += (t00*MAS[3])-1 < t18_t3_mem0*MAS_MEM[6]
	S += (t00*MAS[4])-1 < t18_t3_mem0*MAS_MEM[8]
	S += t18_t3_mem0 <= t18_t3

	t18_t3_mem1 = S.Task('t18_t3_mem1', length=1, delay_cost=1)
	t18_t3_mem1 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t18_t3_mem1*MAS_MEM[1]
	S += (t01*MAS[1])-1 < t18_t3_mem1*MAS_MEM[3]
	S += (t01*MAS[2])-1 < t18_t3_mem1*MAS_MEM[5]
	S += (t01*MAS[3])-1 < t18_t3_mem1*MAS_MEM[7]
	S += (t01*MAS[4])-1 < t18_t3_mem1*MAS_MEM[9]
	S += t18_t3_mem1 <= t18_t3

	c010 = S.Task('c010', length=11, delay_cost=1)
	c010 += alt(MM)
	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MM_in)
	S += c010_in*MM_in[0]<=c010*MM[0]
	S += 0<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < c010_mem0*MAS_MEM[0]
	S += (t110*MAS[1])-1 < c010_mem0*MAS_MEM[2]
	S += (t110*MAS[2])-1 < c010_mem0*MAS_MEM[4]
	S += (t110*MAS[3])-1 < c010_mem0*MAS_MEM[6]
	S += (t110*MAS[4])-1 < c010_mem0*MAS_MEM[8]
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += MAIN_MEM_r[1]
	S += c010_mem1 <= c010

	t2_t4 = S.Task('t2_t4', length=11, delay_cost=1)
	t2_t4 += alt(MM)
	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	t2_t4_in += alt(MM_in)
	S += t2_t4_in*MM_in[0]<=t2_t4*MM[0]
	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	t2_t4_mem0 += MAS_MEM[0]
	S += 20 < t2_t4_mem0
	S += t2_t4_mem0 <= t2_t4

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	t2_t4_mem1 += alt(MAS_MEM)
	S += (t2_t3*MAS[0])-1 < t2_t4_mem1*MAS_MEM[1]
	S += (t2_t3*MAS[1])-1 < t2_t4_mem1*MAS_MEM[3]
	S += (t2_t3*MAS[2])-1 < t2_t4_mem1*MAS_MEM[5]
	S += (t2_t3*MAS[3])-1 < t2_t4_mem1*MAS_MEM[7]
	S += (t2_t3*MAS[4])-1 < t2_t4_mem1*MAS_MEM[9]
	S += t2_t4_mem1 <= t2_t4

	t20 = S.Task('t20', length=3, delay_cost=1)
	t20 += alt(MAS)
	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	t20_in += alt(MAS_in)
	S += t20_in*MAS_in[0]<=t20*MAS[0]

	S += t20_in*MAS_in[1]<=t20*MAS[1]

	S += t20_in*MAS_in[2]<=t20*MAS[2]

	S += t20_in*MAS_in[3]<=t20*MAS[3]

	S += t20_in*MAS_in[4]<=t20*MAS[4]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += alt(MM_MEM)
	S += (t2_t0*MM[0])-1 < t20_mem0*MM_MEM[0]
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += alt(MM_MEM)
	S += (t2_t1*MM[0])-1 < t20_mem1*MM_MEM[1]
	S += t20_mem1 <= t20

	t2_t5 = S.Task('t2_t5', length=3, delay_cost=1)
	t2_t5 += alt(MAS)
	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	t2_t5_in += alt(MAS_in)
	S += t2_t5_in*MAS_in[0]<=t2_t5*MAS[0]

	S += t2_t5_in*MAS_in[1]<=t2_t5*MAS[1]

	S += t2_t5_in*MAS_in[2]<=t2_t5*MAS[2]

	S += t2_t5_in*MAS_in[3]<=t2_t5*MAS[3]

	S += t2_t5_in*MAS_in[4]<=t2_t5*MAS[4]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	t2_t5_mem0 += alt(MM_MEM)
	S += (t2_t0*MM[0])-1 < t2_t5_mem0*MM_MEM[0]
	S += t2_t5_mem0 <= t2_t5

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	t2_t5_mem1 += alt(MM_MEM)
	S += (t2_t1*MM[0])-1 < t2_t5_mem1*MM_MEM[1]
	S += t2_t5_mem1 <= t2_t5

	t90 = S.Task('t90', length=3, delay_cost=1)
	t90 += alt(MAS)
	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	t90_in += alt(MAS_in)
	S += t90_in*MAS_in[0]<=t90*MAS[0]

	S += t90_in*MAS_in[1]<=t90*MAS[1]

	S += t90_in*MAS_in[2]<=t90*MAS[2]

	S += t90_in*MAS_in[3]<=t90*MAS[3]

	S += t90_in*MAS_in[4]<=t90*MAS[4]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t90_mem0*MAS_MEM[0]
	S += (t80*MAS[1])-1 < t90_mem0*MAS_MEM[2]
	S += (t80*MAS[2])-1 < t90_mem0*MAS_MEM[4]
	S += (t80*MAS[3])-1 < t90_mem0*MAS_MEM[6]
	S += (t80*MAS[4])-1 < t90_mem0*MAS_MEM[8]
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t90_mem1*MAS_MEM[1]
	S += (t70*MAS[1])-1 < t90_mem1*MAS_MEM[3]
	S += (t70*MAS[2])-1 < t90_mem1*MAS_MEM[5]
	S += (t70*MAS[3])-1 < t90_mem1*MAS_MEM[7]
	S += (t70*MAS[4])-1 < t90_mem1*MAS_MEM[9]
	S += t90_mem1 <= t90

	t12_t1 = S.Task('t12_t1', length=11, delay_cost=1)
	t12_t1 += alt(MM)
	t12_t1_in = S.Task('t12_t1_in', length=1, delay_cost=1)
	t12_t1_in += alt(MM_in)
	S += t12_t1_in*MM_in[0]<=t12_t1*MM[0]
	t12_t1_mem0 = S.Task('t12_t1_mem0', length=1, delay_cost=1)
	t12_t1_mem0 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t12_t1_mem0*MAS_MEM[0]
	S += (t01*MAS[1])-1 < t12_t1_mem0*MAS_MEM[2]
	S += (t01*MAS[2])-1 < t12_t1_mem0*MAS_MEM[4]
	S += (t01*MAS[3])-1 < t12_t1_mem0*MAS_MEM[6]
	S += (t01*MAS[4])-1 < t12_t1_mem0*MAS_MEM[8]
	S += t12_t1_mem0 <= t12_t1

	t12_t1_mem1 = S.Task('t12_t1_mem1', length=1, delay_cost=1)
	t12_t1_mem1 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < t12_t1_mem1*MAS_MEM[1]
	S += (t111*MAS[1])-1 < t12_t1_mem1*MAS_MEM[3]
	S += (t111*MAS[2])-1 < t12_t1_mem1*MAS_MEM[5]
	S += (t111*MAS[3])-1 < t12_t1_mem1*MAS_MEM[7]
	S += (t111*MAS[4])-1 < t12_t1_mem1*MAS_MEM[9]
	S += t12_t1_mem1 <= t12_t1

	t12_t3 = S.Task('t12_t3', length=3, delay_cost=1)
	t12_t3 += alt(MAS)
	t12_t3_in = S.Task('t12_t3_in', length=1, delay_cost=1)
	t12_t3_in += alt(MAS_in)
	S += t12_t3_in*MAS_in[0]<=t12_t3*MAS[0]

	S += t12_t3_in*MAS_in[1]<=t12_t3*MAS[1]

	S += t12_t3_in*MAS_in[2]<=t12_t3*MAS[2]

	S += t12_t3_in*MAS_in[3]<=t12_t3*MAS[3]

	S += t12_t3_in*MAS_in[4]<=t12_t3*MAS[4]

	t12_t3_mem0 = S.Task('t12_t3_mem0', length=1, delay_cost=1)
	t12_t3_mem0 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < t12_t3_mem0*MAS_MEM[0]
	S += (t110*MAS[1])-1 < t12_t3_mem0*MAS_MEM[2]
	S += (t110*MAS[2])-1 < t12_t3_mem0*MAS_MEM[4]
	S += (t110*MAS[3])-1 < t12_t3_mem0*MAS_MEM[6]
	S += (t110*MAS[4])-1 < t12_t3_mem0*MAS_MEM[8]
	S += t12_t3_mem0 <= t12_t3

	t12_t3_mem1 = S.Task('t12_t3_mem1', length=1, delay_cost=1)
	t12_t3_mem1 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < t12_t3_mem1*MAS_MEM[1]
	S += (t111*MAS[1])-1 < t12_t3_mem1*MAS_MEM[3]
	S += (t111*MAS[2])-1 < t12_t3_mem1*MAS_MEM[5]
	S += (t111*MAS[3])-1 < t12_t3_mem1*MAS_MEM[7]
	S += (t111*MAS[4])-1 < t12_t3_mem1*MAS_MEM[9]
	S += t12_t3_mem1 <= t12_t3

	new_TX_t3 = S.Task('new_TX_t3', length=3, delay_cost=1)
	new_TX_t3 += alt(MAS)
	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	new_TX_t3_in += alt(MAS_in)
	S += new_TX_t3_in*MAS_in[0]<=new_TX_t3*MAS[0]

	S += new_TX_t3_in*MAS_in[1]<=new_TX_t3*MAS[1]

	S += new_TX_t3_in*MAS_in[2]<=new_TX_t3*MAS[2]

	S += new_TX_t3_in*MAS_in[3]<=new_TX_t3*MAS[3]

	S += new_TX_t3_in*MAS_in[4]<=new_TX_t3*MAS[4]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	new_TX_t3_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < new_TX_t3_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < new_TX_t3_mem0*MAS_MEM[2]
	S += (t60*MAS[2])-1 < new_TX_t3_mem0*MAS_MEM[4]
	S += (t60*MAS[3])-1 < new_TX_t3_mem0*MAS_MEM[6]
	S += (t60*MAS[4])-1 < new_TX_t3_mem0*MAS_MEM[8]
	S += new_TX_t3_mem0 <= new_TX_t3

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	new_TX_t3_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < new_TX_t3_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < new_TX_t3_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < new_TX_t3_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < new_TX_t3_mem1*MAS_MEM[7]
	S += (t61*MAS[4])-1 < new_TX_t3_mem1*MAS_MEM[9]
	S += new_TX_t3_mem1 <= new_TX_t3

	t18_t2 = S.Task('t18_t2', length=11, delay_cost=1)
	t18_t2 += alt(MM)
	t18_t2_in = S.Task('t18_t2_in', length=1, delay_cost=1)
	t18_t2_in += alt(MM_in)
	S += t18_t2_in*MM_in[0]<=t18_t2*MM[0]
	t18_t2_mem0 = S.Task('t18_t2_mem0', length=1, delay_cost=1)
	t18_t2_mem0 += alt(MAS_MEM)
	S += (t18_t0*MAS[0])-1 < t18_t2_mem0*MAS_MEM[0]
	S += (t18_t0*MAS[1])-1 < t18_t2_mem0*MAS_MEM[2]
	S += (t18_t0*MAS[2])-1 < t18_t2_mem0*MAS_MEM[4]
	S += (t18_t0*MAS[3])-1 < t18_t2_mem0*MAS_MEM[6]
	S += (t18_t0*MAS[4])-1 < t18_t2_mem0*MAS_MEM[8]
	S += t18_t2_mem0 <= t18_t2

	t18_t2_mem1 = S.Task('t18_t2_mem1', length=1, delay_cost=1)
	t18_t2_mem1 += alt(MAS_MEM)
	S += (t18_t1*MAS[0])-1 < t18_t2_mem1*MAS_MEM[1]
	S += (t18_t1*MAS[1])-1 < t18_t2_mem1*MAS_MEM[3]
	S += (t18_t1*MAS[2])-1 < t18_t2_mem1*MAS_MEM[5]
	S += (t18_t1*MAS[3])-1 < t18_t2_mem1*MAS_MEM[7]
	S += (t18_t1*MAS[4])-1 < t18_t2_mem1*MAS_MEM[9]
	S += t18_t2_mem1 <= t18_t2

	t18_t5 = S.Task('t18_t5', length=3, delay_cost=1)
	t18_t5 += alt(MAS)
	t18_t5_in = S.Task('t18_t5_in', length=1, delay_cost=1)
	t18_t5_in += alt(MAS_in)
	S += t18_t5_in*MAS_in[0]<=t18_t5*MAS[0]

	S += t18_t5_in*MAS_in[1]<=t18_t5*MAS[1]

	S += t18_t5_in*MAS_in[2]<=t18_t5*MAS[2]

	S += t18_t5_in*MAS_in[3]<=t18_t5*MAS[3]

	S += t18_t5_in*MAS_in[4]<=t18_t5*MAS[4]

	t18_t5_mem0 = S.Task('t18_t5_mem0', length=1, delay_cost=1)
	t18_t5_mem0 += alt(MM_MEM)
	S += (t18_t3*MM[0])-1 < t18_t5_mem0*MM_MEM[0]
	S += t18_t5_mem0 <= t18_t5

	t18_t5_mem1 = S.Task('t18_t5_mem1', length=1, delay_cost=1)
	t18_t5_mem1 += alt(MM_MEM)
	S += (t18_t3*MM[0])-1 < t18_t5_mem1*MM_MEM[1]
	S += t18_t5_mem1 <= t18_t5

	t181 = S.Task('t181', length=3, delay_cost=1)
	t181 += alt(MAS)
	t181_in = S.Task('t181_in', length=1, delay_cost=1)
	t181_in += alt(MAS_in)
	S += t181_in*MAS_in[0]<=t181*MAS[0]

	S += t181_in*MAS_in[1]<=t181*MAS[1]

	S += t181_in*MAS_in[2]<=t181*MAS[2]

	S += t181_in*MAS_in[3]<=t181*MAS[3]

	S += t181_in*MAS_in[4]<=t181*MAS[4]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	t181_mem0 += alt(MM_MEM)
	S += (t18_t3*MM[0])-1 < t181_mem0*MM_MEM[0]
	S += t181_mem0 <= t181

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	t181_mem1 += alt(MM_MEM)
	S += (t18_t3*MM[0])-1 < t181_mem1*MM_MEM[1]
	S += t181_mem1 <= t181

	c011 = S.Task('c011', length=11, delay_cost=1)
	c011 += alt(MM)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MM_in)
	S += c011_in*MM_in[0]<=c011*MM[0]
	S += 0<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < c011_mem0*MAS_MEM[0]
	S += (t111*MAS[1])-1 < c011_mem0*MAS_MEM[2]
	S += (t111*MAS[2])-1 < c011_mem0*MAS_MEM[4]
	S += (t111*MAS[3])-1 < c011_mem0*MAS_MEM[6]
	S += (t111*MAS[4])-1 < c011_mem0*MAS_MEM[8]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += MAIN_MEM_r[1]
	S += c011_mem1 <= c011

	c201 = S.Task('c201', length=11, delay_cost=1)
	c201 += alt(MM)
	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MM_in)
	S += c201_in*MM_in[0]<=c201*MM[0]
	S += 0<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < c201_mem0*MAS_MEM[0]
	S += (t91*MAS[1])-1 < c201_mem0*MAS_MEM[2]
	S += (t91*MAS[2])-1 < c201_mem0*MAS_MEM[4]
	S += (t91*MAS[3])-1 < c201_mem0*MAS_MEM[6]
	S += (t91*MAS[4])-1 < c201_mem0*MAS_MEM[8]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += MAIN_MEM_r[1]
	S += c201_mem1 <= c201

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS5/EP2_DBL_w_EVAL/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

