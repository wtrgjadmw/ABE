from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 153
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=11)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=2, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 0
	c001_in += MAS_in[0]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 0
	c001_mem0 += MAIN_MEM_r[0]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 0
	c001_mem1 += MAIN_MEM_r[1]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 1
	c000_in += MAS_in[1]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 1
	c000_mem0 += MAIN_MEM_r[0]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 1
	c000_mem1 += MAIN_MEM_r[1]

	c001 = S.Task('c001', length=3, delay_cost=1)
	S += c001 >= 1
	c001 += MAS[0]

	c000 = S.Task('c000', length=3, delay_cost=1)
	S += c000 >= 2
	c000 += MAS[1]

	c21_t2_in = S.Task('c21_t2_in', length=1, delay_cost=1)
	S += c21_t2_in >= 2
	c21_t2_in += MAS_in[0]

	c21_t2_mem0 = S.Task('c21_t2_mem0', length=1, delay_cost=1)
	S += c21_t2_mem0 >= 2
	c21_t2_mem0 += MAIN_MEM_r[0]

	c21_t2_mem1 = S.Task('c21_t2_mem1', length=1, delay_cost=1)
	S += c21_t2_mem1 >= 2
	c21_t2_mem1 += MAIN_MEM_r[1]

	c11_t1_in = S.Task('c11_t1_in', length=1, delay_cost=1)
	S += c11_t1_in >= 3
	c11_t1_in += MM_in[0]

	c11_t1_mem0 = S.Task('c11_t1_mem0', length=1, delay_cost=1)
	S += c11_t1_mem0 >= 3
	c11_t1_mem0 += MAIN_MEM_r[0]

	c11_t1_mem1 = S.Task('c11_t1_mem1', length=1, delay_cost=1)
	S += c11_t1_mem1 >= 3
	c11_t1_mem1 += MAIN_MEM_r[1]

	c21_t2 = S.Task('c21_t2', length=3, delay_cost=1)
	S += c21_t2 >= 3
	c21_t2 += MAS[0]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 4
	c001_w += MAIN_MEM_w

	c11_t1 = S.Task('c11_t1', length=11, delay_cost=1)
	S += c11_t1 >= 4
	c11_t1 += MM[0]

	c20_t2_in = S.Task('c20_t2_in', length=1, delay_cost=1)
	S += c20_t2_in >= 4
	c20_t2_in += MAS_in[1]

	c20_t2_mem0 = S.Task('c20_t2_mem0', length=1, delay_cost=1)
	S += c20_t2_mem0 >= 4
	c20_t2_mem0 += MAIN_MEM_r[0]

	c20_t2_mem1 = S.Task('c20_t2_mem1', length=1, delay_cost=1)
	S += c20_t2_mem1 >= 4
	c20_t2_mem1 += MAIN_MEM_r[1]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 5
	c000_w += MAIN_MEM_w

	c01_t2_in = S.Task('c01_t2_in', length=1, delay_cost=1)
	S += c01_t2_in >= 5
	c01_t2_in += MAS_in[0]

	c01_t2_mem0 = S.Task('c01_t2_mem0', length=1, delay_cost=1)
	S += c01_t2_mem0 >= 5
	c01_t2_mem0 += MAIN_MEM_r[0]

	c01_t2_mem1 = S.Task('c01_t2_mem1', length=1, delay_cost=1)
	S += c01_t2_mem1 >= 5
	c01_t2_mem1 += MAIN_MEM_r[1]

	c20_t2 = S.Task('c20_t2', length=3, delay_cost=1)
	S += c20_t2 >= 5
	c20_t2 += MAS[1]

	c01_t2 = S.Task('c01_t2', length=3, delay_cost=1)
	S += c01_t2 >= 6
	c01_t2 += MAS[0]

	c20_t1_in = S.Task('c20_t1_in', length=1, delay_cost=1)
	S += c20_t1_in >= 6
	c20_t1_in += MM_in[0]

	c20_t1_mem0 = S.Task('c20_t1_mem0', length=1, delay_cost=1)
	S += c20_t1_mem0 >= 6
	c20_t1_mem0 += MAIN_MEM_r[0]

	c20_t1_mem1 = S.Task('c20_t1_mem1', length=1, delay_cost=1)
	S += c20_t1_mem1 >= 6
	c20_t1_mem1 += MAIN_MEM_r[1]

	c20_t1 = S.Task('c20_t1', length=11, delay_cost=1)
	S += c20_t1 >= 7
	c20_t1 += MM[0]

	c20_t3_in = S.Task('c20_t3_in', length=1, delay_cost=1)
	S += c20_t3_in >= 7
	c20_t3_in += MAS_in[0]

	c20_t3_mem0 = S.Task('c20_t3_mem0', length=1, delay_cost=1)
	S += c20_t3_mem0 >= 7
	c20_t3_mem0 += MAIN_MEM_r[0]

	c20_t3_mem1 = S.Task('c20_t3_mem1', length=1, delay_cost=1)
	S += c20_t3_mem1 >= 7
	c20_t3_mem1 += MAIN_MEM_r[1]

	c10_t3_in = S.Task('c10_t3_in', length=1, delay_cost=1)
	S += c10_t3_in >= 8
	c10_t3_in += MAS_in[1]

	c10_t3_mem0 = S.Task('c10_t3_mem0', length=1, delay_cost=1)
	S += c10_t3_mem0 >= 8
	c10_t3_mem0 += MAIN_MEM_r[0]

	c10_t3_mem1 = S.Task('c10_t3_mem1', length=1, delay_cost=1)
	S += c10_t3_mem1 >= 8
	c10_t3_mem1 += MAIN_MEM_r[1]

	c20_t3 = S.Task('c20_t3', length=3, delay_cost=1)
	S += c20_t3 >= 8
	c20_t3 += MAS[0]

	c10_t3 = S.Task('c10_t3', length=3, delay_cost=1)
	S += c10_t3 >= 9
	c10_t3 += MAS[1]

	c11_t0_in = S.Task('c11_t0_in', length=1, delay_cost=1)
	S += c11_t0_in >= 9
	c11_t0_in += MM_in[0]

	c11_t0_mem0 = S.Task('c11_t0_mem0', length=1, delay_cost=1)
	S += c11_t0_mem0 >= 9
	c11_t0_mem0 += MAIN_MEM_r[0]

	c11_t0_mem1 = S.Task('c11_t0_mem1', length=1, delay_cost=1)
	S += c11_t0_mem1 >= 9
	c11_t0_mem1 += MAIN_MEM_r[1]

	c10_t2_in = S.Task('c10_t2_in', length=1, delay_cost=1)
	S += c10_t2_in >= 10
	c10_t2_in += MAS_in[1]

	c10_t2_mem0 = S.Task('c10_t2_mem0', length=1, delay_cost=1)
	S += c10_t2_mem0 >= 10
	c10_t2_mem0 += MAIN_MEM_r[0]

	c10_t2_mem1 = S.Task('c10_t2_mem1', length=1, delay_cost=1)
	S += c10_t2_mem1 >= 10
	c10_t2_mem1 += MAIN_MEM_r[1]

	c11_t0 = S.Task('c11_t0', length=11, delay_cost=1)
	S += c11_t0 >= 10
	c11_t0 += MM[0]

	c10_t2 = S.Task('c10_t2', length=3, delay_cost=1)
	S += c10_t2 >= 11
	c10_t2 += MAS[1]

	c21_t0_in = S.Task('c21_t0_in', length=1, delay_cost=1)
	S += c21_t0_in >= 11
	c21_t0_in += MM_in[0]

	c21_t0_mem0 = S.Task('c21_t0_mem0', length=1, delay_cost=1)
	S += c21_t0_mem0 >= 11
	c21_t0_mem0 += MAIN_MEM_r[0]

	c21_t0_mem1 = S.Task('c21_t0_mem1', length=1, delay_cost=1)
	S += c21_t0_mem1 >= 11
	c21_t0_mem1 += MAIN_MEM_r[1]

	c21_t0 = S.Task('c21_t0', length=11, delay_cost=1)
	S += c21_t0 >= 12
	c21_t0 += MM[0]

	c21_t3_in = S.Task('c21_t3_in', length=1, delay_cost=1)
	S += c21_t3_in >= 12
	c21_t3_in += MAS_in[0]

	c21_t3_mem0 = S.Task('c21_t3_mem0', length=1, delay_cost=1)
	S += c21_t3_mem0 >= 12
	c21_t3_mem0 += MAIN_MEM_r[0]

	c21_t3_mem1 = S.Task('c21_t3_mem1', length=1, delay_cost=1)
	S += c21_t3_mem1 >= 12
	c21_t3_mem1 += MAIN_MEM_r[1]

	c20_t0_in = S.Task('c20_t0_in', length=1, delay_cost=1)
	S += c20_t0_in >= 13
	c20_t0_in += MM_in[0]

	c20_t0_mem0 = S.Task('c20_t0_mem0', length=1, delay_cost=1)
	S += c20_t0_mem0 >= 13
	c20_t0_mem0 += MAIN_MEM_r[0]

	c20_t0_mem1 = S.Task('c20_t0_mem1', length=1, delay_cost=1)
	S += c20_t0_mem1 >= 13
	c20_t0_mem1 += MAIN_MEM_r[1]

	c21_t3 = S.Task('c21_t3', length=3, delay_cost=1)
	S += c21_t3 >= 13
	c21_t3 += MAS[0]

	c20_t0 = S.Task('c20_t0', length=11, delay_cost=1)
	S += c20_t0 >= 14
	c20_t0 += MM[0]

	c21_t1_in = S.Task('c21_t1_in', length=1, delay_cost=1)
	S += c21_t1_in >= 14
	c21_t1_in += MM_in[0]

	c21_t1_mem0 = S.Task('c21_t1_mem0', length=1, delay_cost=1)
	S += c21_t1_mem0 >= 14
	c21_t1_mem0 += MAIN_MEM_r[0]

	c21_t1_mem1 = S.Task('c21_t1_mem1', length=1, delay_cost=1)
	S += c21_t1_mem1 >= 14
	c21_t1_mem1 += MAIN_MEM_r[1]

	c11_t3_in = S.Task('c11_t3_in', length=1, delay_cost=1)
	S += c11_t3_in >= 15
	c11_t3_in += MAS_in[1]

	c11_t3_mem0 = S.Task('c11_t3_mem0', length=1, delay_cost=1)
	S += c11_t3_mem0 >= 15
	c11_t3_mem0 += MAIN_MEM_r[0]

	c11_t3_mem1 = S.Task('c11_t3_mem1', length=1, delay_cost=1)
	S += c11_t3_mem1 >= 15
	c11_t3_mem1 += MAIN_MEM_r[1]

	c21_t1 = S.Task('c21_t1', length=11, delay_cost=1)
	S += c21_t1 >= 15
	c21_t1 += MM[0]

	c10_t1_in = S.Task('c10_t1_in', length=1, delay_cost=1)
	S += c10_t1_in >= 16
	c10_t1_in += MM_in[0]

	c10_t1_mem0 = S.Task('c10_t1_mem0', length=1, delay_cost=1)
	S += c10_t1_mem0 >= 16
	c10_t1_mem0 += MAIN_MEM_r[0]

	c10_t1_mem1 = S.Task('c10_t1_mem1', length=1, delay_cost=1)
	S += c10_t1_mem1 >= 16
	c10_t1_mem1 += MAIN_MEM_r[1]

	c11_t3 = S.Task('c11_t3', length=3, delay_cost=1)
	S += c11_t3 >= 16
	c11_t3 += MAS[1]

	c10_t0_in = S.Task('c10_t0_in', length=1, delay_cost=1)
	S += c10_t0_in >= 17
	c10_t0_in += MM_in[0]

	c10_t0_mem0 = S.Task('c10_t0_mem0', length=1, delay_cost=1)
	S += c10_t0_mem0 >= 17
	c10_t0_mem0 += MAIN_MEM_r[0]

	c10_t0_mem1 = S.Task('c10_t0_mem1', length=1, delay_cost=1)
	S += c10_t0_mem1 >= 17
	c10_t0_mem1 += MAIN_MEM_r[1]

	c10_t1 = S.Task('c10_t1', length=11, delay_cost=1)
	S += c10_t1 >= 17
	c10_t1 += MM[0]

	c01_t3_in = S.Task('c01_t3_in', length=1, delay_cost=1)
	S += c01_t3_in >= 18
	c01_t3_in += MAS_in[1]

	c01_t3_mem0 = S.Task('c01_t3_mem0', length=1, delay_cost=1)
	S += c01_t3_mem0 >= 18
	c01_t3_mem0 += MAIN_MEM_r[0]

	c01_t3_mem1 = S.Task('c01_t3_mem1', length=1, delay_cost=1)
	S += c01_t3_mem1 >= 18
	c01_t3_mem1 += MAIN_MEM_r[1]

	c10_t0 = S.Task('c10_t0', length=11, delay_cost=1)
	S += c10_t0 >= 18
	c10_t0 += MM[0]

	c01_t3 = S.Task('c01_t3', length=3, delay_cost=1)
	S += c01_t3 >= 19
	c01_t3 += MAS[1]

	c11_t2_in = S.Task('c11_t2_in', length=1, delay_cost=1)
	S += c11_t2_in >= 19
	c11_t2_in += MAS_in[0]

	c11_t2_mem0 = S.Task('c11_t2_mem0', length=1, delay_cost=1)
	S += c11_t2_mem0 >= 19
	c11_t2_mem0 += MAIN_MEM_r[0]

	c11_t2_mem1 = S.Task('c11_t2_mem1', length=1, delay_cost=1)
	S += c11_t2_mem1 >= 19
	c11_t2_mem1 += MAIN_MEM_r[1]

	c01_t1_in = S.Task('c01_t1_in', length=1, delay_cost=1)
	S += c01_t1_in >= 20
	c01_t1_in += MM_in[0]

	c01_t1_mem0 = S.Task('c01_t1_mem0', length=1, delay_cost=1)
	S += c01_t1_mem0 >= 20
	c01_t1_mem0 += MAIN_MEM_r[0]

	c01_t1_mem1 = S.Task('c01_t1_mem1', length=1, delay_cost=1)
	S += c01_t1_mem1 >= 20
	c01_t1_mem1 += MAIN_MEM_r[1]

	c11_t2 = S.Task('c11_t2', length=3, delay_cost=1)
	S += c11_t2 >= 20
	c11_t2 += MAS[0]

	c01_t0_in = S.Task('c01_t0_in', length=1, delay_cost=1)
	S += c01_t0_in >= 21
	c01_t0_in += MM_in[0]

	c01_t0_mem0 = S.Task('c01_t0_mem0', length=1, delay_cost=1)
	S += c01_t0_mem0 >= 21
	c01_t0_mem0 += MAIN_MEM_r[0]

	c01_t0_mem1 = S.Task('c01_t0_mem1', length=1, delay_cost=1)
	S += c01_t0_mem1 >= 21
	c01_t0_mem1 += MAIN_MEM_r[1]

	c01_t1 = S.Task('c01_t1', length=11, delay_cost=1)
	S += c01_t1 >= 21
	c01_t1 += MM[0]

	c01_t0 = S.Task('c01_t0', length=11, delay_cost=1)
	S += c01_t0 >= 22
	c01_t0 += MM[0]


	# new tasks
	c10_t4 = S.Task('c10_t4', length=11, delay_cost=1)
	c10_t4 += alt(MM)
	c10_t4_in = S.Task('c10_t4_in', length=1, delay_cost=1)
	c10_t4_in += alt(MM_in)
	S += c10_t4_in*MM_in[0]<=c10_t4*MM[0]
	c10_t4_mem0 = S.Task('c10_t4_mem0', length=1, delay_cost=1)
	c10_t4_mem0 += MAS_MEM[2]
	S += 13 < c10_t4_mem0
	S += c10_t4_mem0 <= c10_t4

	c10_t4_mem1 = S.Task('c10_t4_mem1', length=1, delay_cost=1)
	c10_t4_mem1 += MAS_MEM[3]
	S += 11 < c10_t4_mem1
	S += c10_t4_mem1 <= c10_t4

	c100 = S.Task('c100', length=3, delay_cost=1)
	c100 += alt(MAS)
	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	c100_in += alt(MAS_in)
	S += c100_in*MAS_in[0]<=c100*MAS[0]

	S += c100_in*MAS_in[1]<=c100*MAS[1]

	S += 18<c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += MM_MEM[0]
	S += 28 < c100_mem0
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += MM_MEM[1]
	S += 27 < c100_mem1
	S += c100_mem1 <= c100

	c10_t5 = S.Task('c10_t5', length=3, delay_cost=1)
	c10_t5 += alt(MAS)
	c10_t5_in = S.Task('c10_t5_in', length=1, delay_cost=1)
	c10_t5_in += alt(MAS_in)
	S += c10_t5_in*MAS_in[0]<=c10_t5*MAS[0]

	S += c10_t5_in*MAS_in[1]<=c10_t5*MAS[1]

	c10_t5_mem0 = S.Task('c10_t5_mem0', length=1, delay_cost=1)
	c10_t5_mem0 += MM_MEM[0]
	S += 28 < c10_t5_mem0
	S += c10_t5_mem0 <= c10_t5

	c10_t5_mem1 = S.Task('c10_t5_mem1', length=1, delay_cost=1)
	c10_t5_mem1 += MM_MEM[1]
	S += 27 < c10_t5_mem1
	S += c10_t5_mem1 <= c10_t5

	c20_t4 = S.Task('c20_t4', length=11, delay_cost=1)
	c20_t4 += alt(MM)
	c20_t4_in = S.Task('c20_t4_in', length=1, delay_cost=1)
	c20_t4_in += alt(MM_in)
	S += c20_t4_in*MM_in[0]<=c20_t4*MM[0]
	c20_t4_mem0 = S.Task('c20_t4_mem0', length=1, delay_cost=1)
	c20_t4_mem0 += MAS_MEM[2]
	S += 7 < c20_t4_mem0
	S += c20_t4_mem0 <= c20_t4

	c20_t4_mem1 = S.Task('c20_t4_mem1', length=1, delay_cost=1)
	c20_t4_mem1 += MAS_MEM[1]
	S += 10 < c20_t4_mem1
	S += c20_t4_mem1 <= c20_t4

	c200 = S.Task('c200', length=3, delay_cost=1)
	c200 += alt(MAS)
	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MAS_in)
	S += c200_in*MAS_in[0]<=c200*MAS[0]

	S += c200_in*MAS_in[1]<=c200*MAS[1]

	S += 14<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += MM_MEM[0]
	S += 24 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MM_MEM[1]
	S += 17 < c200_mem1
	S += c200_mem1 <= c200

	c20_t5 = S.Task('c20_t5', length=3, delay_cost=1)
	c20_t5 += alt(MAS)
	c20_t5_in = S.Task('c20_t5_in', length=1, delay_cost=1)
	c20_t5_in += alt(MAS_in)
	S += c20_t5_in*MAS_in[0]<=c20_t5*MAS[0]

	S += c20_t5_in*MAS_in[1]<=c20_t5*MAS[1]

	c20_t5_mem0 = S.Task('c20_t5_mem0', length=1, delay_cost=1)
	c20_t5_mem0 += MM_MEM[0]
	S += 24 < c20_t5_mem0
	S += c20_t5_mem0 <= c20_t5

	c20_t5_mem1 = S.Task('c20_t5_mem1', length=1, delay_cost=1)
	c20_t5_mem1 += MM_MEM[1]
	S += 17 < c20_t5_mem1
	S += c20_t5_mem1 <= c20_t5

	c01_t4 = S.Task('c01_t4', length=11, delay_cost=1)
	c01_t4 += alt(MM)
	c01_t4_in = S.Task('c01_t4_in', length=1, delay_cost=1)
	c01_t4_in += alt(MM_in)
	S += c01_t4_in*MM_in[0]<=c01_t4*MM[0]
	c01_t4_mem0 = S.Task('c01_t4_mem0', length=1, delay_cost=1)
	c01_t4_mem0 += MAS_MEM[0]
	S += 8 < c01_t4_mem0
	S += c01_t4_mem0 <= c01_t4

	c01_t4_mem1 = S.Task('c01_t4_mem1', length=1, delay_cost=1)
	c01_t4_mem1 += MAS_MEM[3]
	S += 21 < c01_t4_mem1
	S += c01_t4_mem1 <= c01_t4

	c010 = S.Task('c010', length=3, delay_cost=1)
	c010 += alt(MAS)
	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MAS_in)
	S += c010_in*MAS_in[0]<=c010*MAS[0]

	S += c010_in*MAS_in[1]<=c010*MAS[1]

	S += 22<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += MM_MEM[0]
	S += 32 < c010_mem0
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += MM_MEM[1]
	S += 31 < c010_mem1
	S += c010_mem1 <= c010

	c01_t5 = S.Task('c01_t5', length=3, delay_cost=1)
	c01_t5 += alt(MAS)
	c01_t5_in = S.Task('c01_t5_in', length=1, delay_cost=1)
	c01_t5_in += alt(MAS_in)
	S += c01_t5_in*MAS_in[0]<=c01_t5*MAS[0]

	S += c01_t5_in*MAS_in[1]<=c01_t5*MAS[1]

	c01_t5_mem0 = S.Task('c01_t5_mem0', length=1, delay_cost=1)
	c01_t5_mem0 += MM_MEM[0]
	S += 32 < c01_t5_mem0
	S += c01_t5_mem0 <= c01_t5

	c01_t5_mem1 = S.Task('c01_t5_mem1', length=1, delay_cost=1)
	c01_t5_mem1 += MM_MEM[1]
	S += 31 < c01_t5_mem1
	S += c01_t5_mem1 <= c01_t5

	c11_t4 = S.Task('c11_t4', length=11, delay_cost=1)
	c11_t4 += alt(MM)
	c11_t4_in = S.Task('c11_t4_in', length=1, delay_cost=1)
	c11_t4_in += alt(MM_in)
	S += c11_t4_in*MM_in[0]<=c11_t4*MM[0]
	c11_t4_mem0 = S.Task('c11_t4_mem0', length=1, delay_cost=1)
	c11_t4_mem0 += MAS_MEM[0]
	S += 22 < c11_t4_mem0
	S += c11_t4_mem0 <= c11_t4

	c11_t4_mem1 = S.Task('c11_t4_mem1', length=1, delay_cost=1)
	c11_t4_mem1 += MAS_MEM[3]
	S += 18 < c11_t4_mem1
	S += c11_t4_mem1 <= c11_t4

	c110 = S.Task('c110', length=3, delay_cost=1)
	c110 += alt(MAS)
	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	c110_in += alt(MAS_in)
	S += c110_in*MAS_in[0]<=c110*MAS[0]

	S += c110_in*MAS_in[1]<=c110*MAS[1]

	S += 20<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MM_MEM[0]
	S += 20 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MM_MEM[1]
	S += 14 < c110_mem1
	S += c110_mem1 <= c110

	c11_t5 = S.Task('c11_t5', length=3, delay_cost=1)
	c11_t5 += alt(MAS)
	c11_t5_in = S.Task('c11_t5_in', length=1, delay_cost=1)
	c11_t5_in += alt(MAS_in)
	S += c11_t5_in*MAS_in[0]<=c11_t5*MAS[0]

	S += c11_t5_in*MAS_in[1]<=c11_t5*MAS[1]

	c11_t5_mem0 = S.Task('c11_t5_mem0', length=1, delay_cost=1)
	c11_t5_mem0 += MM_MEM[0]
	S += 20 < c11_t5_mem0
	S += c11_t5_mem0 <= c11_t5

	c11_t5_mem1 = S.Task('c11_t5_mem1', length=1, delay_cost=1)
	c11_t5_mem1 += MM_MEM[1]
	S += 14 < c11_t5_mem1
	S += c11_t5_mem1 <= c11_t5

	c21_t4 = S.Task('c21_t4', length=11, delay_cost=1)
	c21_t4 += alt(MM)
	c21_t4_in = S.Task('c21_t4_in', length=1, delay_cost=1)
	c21_t4_in += alt(MM_in)
	S += c21_t4_in*MM_in[0]<=c21_t4*MM[0]
	c21_t4_mem0 = S.Task('c21_t4_mem0', length=1, delay_cost=1)
	c21_t4_mem0 += MAS_MEM[0]
	S += 5 < c21_t4_mem0
	S += c21_t4_mem0 <= c21_t4

	c21_t4_mem1 = S.Task('c21_t4_mem1', length=1, delay_cost=1)
	c21_t4_mem1 += MAS_MEM[1]
	S += 15 < c21_t4_mem1
	S += c21_t4_mem1 <= c21_t4

	c210 = S.Task('c210', length=3, delay_cost=1)
	c210 += alt(MAS)
	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	c210_in += alt(MAS_in)
	S += c210_in*MAS_in[0]<=c210*MAS[0]

	S += c210_in*MAS_in[1]<=c210*MAS[1]

	S += 12<c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MM_MEM[0]
	S += 22 < c210_mem0
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MM_MEM[1]
	S += 25 < c210_mem1
	S += c210_mem1 <= c210

	c21_t5 = S.Task('c21_t5', length=3, delay_cost=1)
	c21_t5 += alt(MAS)
	c21_t5_in = S.Task('c21_t5_in', length=1, delay_cost=1)
	c21_t5_in += alt(MAS_in)
	S += c21_t5_in*MAS_in[0]<=c21_t5*MAS[0]

	S += c21_t5_in*MAS_in[1]<=c21_t5*MAS[1]

	c21_t5_mem0 = S.Task('c21_t5_mem0', length=1, delay_cost=1)
	c21_t5_mem0 += MM_MEM[0]
	S += 22 < c21_t5_mem0
	S += c21_t5_mem0 <= c21_t5

	c21_t5_mem1 = S.Task('c21_t5_mem1', length=1, delay_cost=1)
	c21_t5_mem1 += MM_MEM[1]
	S += 25 < c21_t5_mem1
	S += c21_t5_mem1 <= c21_t5

	c101 = S.Task('c101', length=3, delay_cost=1)
	c101 += alt(MAS)
	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	c101_in += alt(MAS_in)
	S += c101_in*MAS_in[0]<=c101*MAS[0]

	S += c101_in*MAS_in[1]<=c101*MAS[1]

	S += 17<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MM_MEM)
	S += (c10_t4*MM[0])-1 < c101_mem0*MM_MEM[0]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(MAS_MEM)
	S += (c10_t5*MAS[0])-1 < c101_mem1*MAS_MEM[1]
	S += (c10_t5*MAS[1])-1 < c101_mem1*MAS_MEM[3]
	S += c101_mem1 <= c101

	c201 = S.Task('c201', length=3, delay_cost=1)
	c201 += alt(MAS)
	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MAS_in)
	S += c201_in*MAS_in[0]<=c201*MAS[0]

	S += c201_in*MAS_in[1]<=c201*MAS[1]

	S += 7<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MM_MEM)
	S += (c20_t4*MM[0])-1 < c201_mem0*MM_MEM[0]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += alt(MAS_MEM)
	S += (c20_t5*MAS[0])-1 < c201_mem1*MAS_MEM[1]
	S += (c20_t5*MAS[1])-1 < c201_mem1*MAS_MEM[3]
	S += c201_mem1 <= c201

	c011 = S.Task('c011', length=3, delay_cost=1)
	c011 += alt(MAS)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MAS_in)
	S += c011_in*MAS_in[0]<=c011*MAS[0]

	S += c011_in*MAS_in[1]<=c011*MAS[1]

	S += 21<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(MM_MEM)
	S += (c01_t4*MM[0])-1 < c011_mem0*MM_MEM[0]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(MAS_MEM)
	S += (c01_t5*MAS[0])-1 < c011_mem1*MAS_MEM[1]
	S += (c01_t5*MAS[1])-1 < c011_mem1*MAS_MEM[3]
	S += c011_mem1 <= c011

	c111 = S.Task('c111', length=3, delay_cost=1)
	c111 += alt(MAS)
	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	c111_in += alt(MAS_in)
	S += c111_in*MAS_in[0]<=c111*MAS[0]

	S += c111_in*MAS_in[1]<=c111*MAS[1]

	S += 20<c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += alt(MM_MEM)
	S += (c11_t4*MM[0])-1 < c111_mem0*MM_MEM[0]
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += alt(MAS_MEM)
	S += (c11_t5*MAS[0])-1 < c111_mem1*MAS_MEM[1]
	S += (c11_t5*MAS[1])-1 < c111_mem1*MAS_MEM[3]
	S += c111_mem1 <= c111

	c211 = S.Task('c211', length=3, delay_cost=1)
	c211 += alt(MAS)
	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	c211_in += alt(MAS_in)
	S += c211_in*MAS_in[0]<=c211*MAS[0]

	S += c211_in*MAS_in[1]<=c211*MAS[1]

	S += 15<c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(MM_MEM)
	S += (c21_t4*MM[0])-1 < c211_mem0*MM_MEM[0]
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += alt(MAS_MEM)
	S += (c21_t5*MAS[0])-1 < c211_mem1*MAS_MEM[1]
	S += (c21_t5*MAS[1])-1 < c211_mem1*MAS_MEM[3]
	S += c211_mem1 <= c211

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS2/FROB/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution

