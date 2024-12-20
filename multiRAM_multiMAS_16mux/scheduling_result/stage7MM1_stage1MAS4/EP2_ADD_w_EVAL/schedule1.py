from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 143
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 0
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 0
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 0
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	S += t2_t0 >= 1
	t2_t0 += MM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 1
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 1
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 1
	t2_t1_mem1 += MAIN_MEM_r[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 2
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 2
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 2
	t0_t0_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	S += t2_t1 >= 2
	t2_t1 += MM[0]

	t0_t0 = S.Task('t0_t0', length=7, delay_cost=1)
	S += t0_t0 >= 3
	t0_t0 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 3
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 3
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 3
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=7, delay_cost=1)
	S += t0_t1 >= 4
	t0_t1 += MM[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 4
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 4
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 5
	t2_t2 += MAS[2]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 5
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 5
	t2_t3_mem1 += MAIN_MEM_r[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 6
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 6
	t0_t3_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 6
	t2_t3 += MAS[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 6
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 6
	t2_t4_mem0 += MAS_MEM[4]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 6
	t2_t4_mem1 += MAS_MEM[3]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 7
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 7
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 7
	t0_t3 += MAS[2]

	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	S += t2_t4 >= 7
	t2_t4 += MM[0]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 8
	t0_t2 += MAS[3]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 8
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 8
	t0_t4_mem0 += MAS_MEM[6]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 8
	t0_t4_mem1 += MAS_MEM[5]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 8
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 8
	t14_t2_mem1 += MAIN_MEM_r[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 8
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 8
	t20_mem1 += MM_MEM[1]

	t0_t4 = S.Task('t0_t4', length=7, delay_cost=1)
	S += t0_t4 >= 9
	t0_t4 += MM[0]

	t14_t2 = S.Task('t14_t2', length=1, delay_cost=1)
	S += t14_t2 >= 9
	t14_t2 += MAS[3]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 9
	t20 += MAS[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 9
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 9
	t2_t5_mem1 += MM_MEM[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 9
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 9
	t30_mem1 += MAS_MEM[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 10
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 10
	t00_mem1 += MM_MEM[1]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 10
	t16_t0_in += MM_in[0]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 10
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 10
	t16_t0_mem1 += MAS_MEM[7]

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 10
	t2_t5 += MAS[0]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 10
	t30 += MAS[3]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 11
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 11
	c010_mem0 += MAS_MEM[6]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 11
	c010_mem1 += MAIN_MEM_r[1]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 11
	t00 += MAS[3]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 11
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 11
	t0_t5_mem1 += MM_MEM[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 11
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 11
	t10_mem1 += MAS_MEM[7]

	t16_t0 = S.Task('t16_t0', length=7, delay_cost=1)
	S += t16_t0 >= 11
	t16_t0 += MM[0]

	c010 = S.Task('c010', length=7, delay_cost=1)
	S += c010 >= 12
	c010 += MM[0]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 12
	t0_t5 += MAS[0]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 12
	t10 += MAS[1]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 12
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 12
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 12
	t17_t0_mem1 += MAS_MEM[3]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 13
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 13
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t17_t0 = S.Task('t17_t0', length=7, delay_cost=1)
	S += t17_t0 >= 13
	t17_t0 += MM[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 13
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 13
	t21_mem1 += MAS_MEM[1]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 14
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 14
	c200_mem0 += MAS_MEM[2]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 14
	c200_mem1 += MAIN_MEM_r[1]

	new_TZ_t2 = S.Task('new_TZ_t2', length=1, delay_cost=1)
	S += new_TZ_t2 >= 14
	new_TZ_t2 += MAS[0]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 14
	t21 += MAS[1]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 14
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 14
	t31_mem1 += MAS_MEM[3]

	c200 = S.Task('c200', length=7, delay_cost=1)
	S += c200 >= 15
	c200 += MM[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 15
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 15
	t01_mem1 += MAS_MEM[1]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 15
	t31 += MAS[2]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 15
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 15
	t9_t2_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 16
	t01 += MAS[1]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 16
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 16
	t16_t2_mem1 += MAIN_MEM_r[1]

	t9_t2 = S.Task('t9_t2', length=1, delay_cost=1)
	S += t9_t2 >= 16
	t9_t2 += MAS[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 17
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 17
	t11_mem1 += MAS_MEM[3]

	t16_t2 = S.Task('t16_t2', length=1, delay_cost=1)
	S += t16_t2 >= 17
	t16_t2 += MAS[2]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 18
	t11 += MAS[1]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 18
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 18
	t7_t2_mem1 += MAIN_MEM_r[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 19
	c010_w += MAIN_MEM_w

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 19
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 19
	t17_t2_mem1 += MAIN_MEM_r[1]

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 19
	t7_t2 += MAS[0]

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	S += t17_t2 >= 20
	t17_t2 += MAS[3]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 22
	c200_w += MAIN_MEM_w


	# new tasks
	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	t4_t0 += alt(MAS)
	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	t4_t0_mem0 += MAS_MEM[2]
	S += 12 < t4_t0_mem0
	S += t4_t0_mem0 <= t4_t0

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	t4_t0_mem1 += MAS_MEM[3]
	S += 18 < t4_t0_mem1
	S += t4_t0_mem1 <= t4_t0

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	t4_t1 += alt(MAS)
	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	t4_t1_mem0 += MAS_MEM[2]
	S += 12 < t4_t1_mem0
	S += t4_t1_mem0 <= t4_t1

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	t4_t1_mem1 += MAS_MEM[3]
	S += 18 < t4_t1_mem1
	S += t4_t1_mem1 <= t4_t1

	t4_t3 = S.Task('t4_t3', length=7, delay_cost=1)
	t4_t3 += alt(MM)
	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	t4_t3_in += alt(MM_in)
	S += t4_t3_in*MM_in[0]<=t4_t3*MM[0]
	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	t4_t3_mem0 += MAS_MEM[2]
	S += 12 < t4_t3_mem0
	S += t4_t3_mem0 <= t4_t3

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	t4_t3_mem1 += MAS_MEM[3]
	S += 18 < t4_t3_mem1
	S += t4_t3_mem1 <= t4_t3

	t5_t0 = S.Task('t5_t0', length=1, delay_cost=1)
	t5_t0 += alt(MAS)
	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	t5_t0_mem0 += MAS_MEM[6]
	S += 10 < t5_t0_mem0
	S += t5_t0_mem0 <= t5_t0

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	t5_t0_mem1 += MAS_MEM[5]
	S += 15 < t5_t0_mem1
	S += t5_t0_mem1 <= t5_t0

	t5_t1 = S.Task('t5_t1', length=1, delay_cost=1)
	t5_t1 += alt(MAS)
	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	t5_t1_mem0 += MAS_MEM[6]
	S += 10 < t5_t1_mem0
	S += t5_t1_mem0 <= t5_t1

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	t5_t1_mem1 += MAS_MEM[5]
	S += 15 < t5_t1_mem1
	S += t5_t1_mem1 <= t5_t1

	t5_t3 = S.Task('t5_t3', length=7, delay_cost=1)
	t5_t3 += alt(MM)
	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	t5_t3_in += alt(MM_in)
	S += t5_t3_in*MM_in[0]<=t5_t3*MM[0]
	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	t5_t3_mem0 += MAS_MEM[6]
	S += 10 < t5_t3_mem0
	S += t5_t3_mem0 <= t5_t3

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	t5_t3_mem1 += MAS_MEM[5]
	S += 15 < t5_t3_mem1
	S += t5_t3_mem1 <= t5_t3

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	t6_t2 += alt(MAS)
	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	t6_t2_mem0 += MAS_MEM[6]
	S += 10 < t6_t2_mem0
	S += t6_t2_mem0 <= t6_t2

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	t6_t2_mem1 += MAS_MEM[5]
	S += 15 < t6_t2_mem1
	S += t6_t2_mem1 <= t6_t2

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	new_TX_t2 += alt(MAS)
	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	new_TX_t2_mem0 += MAS_MEM[6]
	S += 10 < new_TX_t2_mem0
	S += new_TX_t2_mem0 <= new_TX_t2

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	new_TX_t2_mem1 += MAS_MEM[5]
	S += 15 < new_TX_t2_mem1
	S += new_TX_t2_mem1 <= new_TX_t2

	t13_t2 = S.Task('t13_t2', length=1, delay_cost=1)
	t13_t2 += alt(MAS)
	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	t13_t2_mem0 += MAS_MEM[2]
	S += 12 < t13_t2_mem0
	S += t13_t2_mem0 <= t13_t2

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	t13_t2_mem1 += MAS_MEM[3]
	S += 18 < t13_t2_mem1
	S += t13_t2_mem1 <= t13_t2

	c011 = S.Task('c011', length=7, delay_cost=1)
	c011 += alt(MM)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MM_in)
	S += c011_in*MM_in[0]<=c011*MM[0]
	S += 0<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MAS_MEM[4]
	S += 15 < c011_mem0
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += MAIN_MEM_r[1]
	S += c011_mem1 <= c011

	c201 = S.Task('c201', length=7, delay_cost=1)
	c201 += alt(MM)
	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MM_in)
	S += c201_in*MM_in[0]<=c201*MM[0]
	S += 0<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += MAS_MEM[2]
	S += 18 < c201_mem0
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += MAIN_MEM_r[1]
	S += c201_mem1 <= c201

	t16_t1 = S.Task('t16_t1', length=7, delay_cost=1)
	t16_t1 += alt(MM)
	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	t16_t1_in += alt(MM_in)
	S += t16_t1_in*MM_in[0]<=t16_t1*MM[0]
	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	t16_t1_mem0 += MAIN_MEM_r[0]
	S += t16_t1_mem0 <= t16_t1

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	t16_t1_mem1 += MAS_MEM[5]
	S += 15 < t16_t1_mem1
	S += t16_t1_mem1 <= t16_t1

	t16_t3 = S.Task('t16_t3', length=1, delay_cost=1)
	t16_t3 += alt(MAS)
	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	t16_t3_mem0 += MAS_MEM[6]
	S += 10 < t16_t3_mem0
	S += t16_t3_mem0 <= t16_t3

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	t16_t3_mem1 += MAS_MEM[5]
	S += 15 < t16_t3_mem1
	S += t16_t3_mem1 <= t16_t3

	t17_t1 = S.Task('t17_t1', length=7, delay_cost=1)
	t17_t1 += alt(MM)
	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	t17_t1_in += alt(MM_in)
	S += t17_t1_in*MM_in[0]<=t17_t1*MM[0]
	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	t17_t1_mem0 += MAIN_MEM_r[0]
	S += t17_t1_mem0 <= t17_t1

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	t17_t1_mem1 += MAS_MEM[3]
	S += 18 < t17_t1_mem1
	S += t17_t1_mem1 <= t17_t1

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	t17_t3 += alt(MAS)
	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	t17_t3_mem0 += MAS_MEM[2]
	S += 12 < t17_t3_mem0
	S += t17_t3_mem0 <= t17_t3

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	t17_t3_mem1 += MAS_MEM[3]
	S += 18 < t17_t3_mem1
	S += t17_t3_mem1 <= t17_t3

	t4_t2 = S.Task('t4_t2', length=7, delay_cost=1)
	t4_t2 += alt(MM)
	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	t4_t2_in += alt(MM_in)
	S += t4_t2_in*MM_in[0]<=t4_t2*MM[0]
	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	t4_t2_mem0 += alt(MAS_MEM)
	S += (t4_t0*MAS[0])-1 < t4_t2_mem0*MAS_MEM[0]
	S += (t4_t0*MAS[1])-1 < t4_t2_mem0*MAS_MEM[2]
	S += (t4_t0*MAS[2])-1 < t4_t2_mem0*MAS_MEM[4]
	S += (t4_t0*MAS[3])-1 < t4_t2_mem0*MAS_MEM[6]
	S += t4_t2_mem0 <= t4_t2

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	t4_t2_mem1 += alt(MAS_MEM)
	S += (t4_t1*MAS[0])-1 < t4_t2_mem1*MAS_MEM[1]
	S += (t4_t1*MAS[1])-1 < t4_t2_mem1*MAS_MEM[3]
	S += (t4_t1*MAS[2])-1 < t4_t2_mem1*MAS_MEM[5]
	S += (t4_t1*MAS[3])-1 < t4_t2_mem1*MAS_MEM[7]
	S += t4_t2_mem1 <= t4_t2

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	t4_t5 += alt(MAS)
	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	t4_t5_mem0 += alt(MM_MEM)
	S += (t4_t3*MM[0])-1 < t4_t5_mem0*MM_MEM[0]
	S += t4_t5_mem0 <= t4_t5

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	t4_t5_mem1 += alt(MM_MEM)
	S += (t4_t3*MM[0])-1 < t4_t5_mem1*MM_MEM[1]
	S += t4_t5_mem1 <= t4_t5

	t41 = S.Task('t41', length=1, delay_cost=1)
	t41 += alt(MAS)
	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	t41_mem0 += alt(MM_MEM)
	S += (t4_t3*MM[0])-1 < t41_mem0*MM_MEM[0]
	S += t41_mem0 <= t41

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	t41_mem1 += alt(MM_MEM)
	S += (t4_t3*MM[0])-1 < t41_mem1*MM_MEM[1]
	S += t41_mem1 <= t41

	t5_t2 = S.Task('t5_t2', length=7, delay_cost=1)
	t5_t2 += alt(MM)
	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	t5_t2_in += alt(MM_in)
	S += t5_t2_in*MM_in[0]<=t5_t2*MM[0]
	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	t5_t2_mem0 += alt(MAS_MEM)
	S += (t5_t0*MAS[0])-1 < t5_t2_mem0*MAS_MEM[0]
	S += (t5_t0*MAS[1])-1 < t5_t2_mem0*MAS_MEM[2]
	S += (t5_t0*MAS[2])-1 < t5_t2_mem0*MAS_MEM[4]
	S += (t5_t0*MAS[3])-1 < t5_t2_mem0*MAS_MEM[6]
	S += t5_t2_mem0 <= t5_t2

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	t5_t2_mem1 += alt(MAS_MEM)
	S += (t5_t1*MAS[0])-1 < t5_t2_mem1*MAS_MEM[1]
	S += (t5_t1*MAS[1])-1 < t5_t2_mem1*MAS_MEM[3]
	S += (t5_t1*MAS[2])-1 < t5_t2_mem1*MAS_MEM[5]
	S += (t5_t1*MAS[3])-1 < t5_t2_mem1*MAS_MEM[7]
	S += t5_t2_mem1 <= t5_t2

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	t5_t5 += alt(MAS)
	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	t5_t5_mem0 += alt(MM_MEM)
	S += (t5_t3*MM[0])-1 < t5_t5_mem0*MM_MEM[0]
	S += t5_t5_mem0 <= t5_t5

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	t5_t5_mem1 += alt(MM_MEM)
	S += (t5_t3*MM[0])-1 < t5_t5_mem1*MM_MEM[1]
	S += t5_t5_mem1 <= t5_t5

	t51 = S.Task('t51', length=1, delay_cost=1)
	t51 += alt(MAS)
	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	t51_mem0 += alt(MM_MEM)
	S += (t5_t3*MM[0])-1 < t51_mem0*MM_MEM[0]
	S += t51_mem0 <= t51

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	t51_mem1 += alt(MM_MEM)
	S += (t5_t3*MM[0])-1 < t51_mem1*MM_MEM[1]
	S += t51_mem1 <= t51

	t16_t4 = S.Task('t16_t4', length=7, delay_cost=1)
	t16_t4 += alt(MM)
	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	t16_t4_in += alt(MM_in)
	S += t16_t4_in*MM_in[0]<=t16_t4*MM[0]
	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	t16_t4_mem0 += MAS_MEM[4]
	S += 17 < t16_t4_mem0
	S += t16_t4_mem0 <= t16_t4

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	t16_t4_mem1 += alt(MAS_MEM)
	S += (t16_t3*MAS[0])-1 < t16_t4_mem1*MAS_MEM[1]
	S += (t16_t3*MAS[1])-1 < t16_t4_mem1*MAS_MEM[3]
	S += (t16_t3*MAS[2])-1 < t16_t4_mem1*MAS_MEM[5]
	S += (t16_t3*MAS[3])-1 < t16_t4_mem1*MAS_MEM[7]
	S += t16_t4_mem1 <= t16_t4

	t160 = S.Task('t160', length=1, delay_cost=1)
	t160 += alt(MAS)
	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += MM_MEM[0]
	S += 17 < t160_mem0
	S += t160_mem0 <= t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(MM_MEM)
	S += (t16_t1*MM[0])-1 < t160_mem1*MM_MEM[1]
	S += t160_mem1 <= t160

	t16_t5 = S.Task('t16_t5', length=1, delay_cost=1)
	t16_t5 += alt(MAS)
	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	t16_t5_mem0 += MM_MEM[0]
	S += 17 < t16_t5_mem0
	S += t16_t5_mem0 <= t16_t5

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	t16_t5_mem1 += alt(MM_MEM)
	S += (t16_t1*MM[0])-1 < t16_t5_mem1*MM_MEM[1]
	S += t16_t5_mem1 <= t16_t5

	t17_t4 = S.Task('t17_t4', length=7, delay_cost=1)
	t17_t4 += alt(MM)
	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	t17_t4_in += alt(MM_in)
	S += t17_t4_in*MM_in[0]<=t17_t4*MM[0]
	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	t17_t4_mem0 += MAS_MEM[6]
	S += 20 < t17_t4_mem0
	S += t17_t4_mem0 <= t17_t4

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	t17_t4_mem1 += alt(MAS_MEM)
	S += (t17_t3*MAS[0])-1 < t17_t4_mem1*MAS_MEM[1]
	S += (t17_t3*MAS[1])-1 < t17_t4_mem1*MAS_MEM[3]
	S += (t17_t3*MAS[2])-1 < t17_t4_mem1*MAS_MEM[5]
	S += (t17_t3*MAS[3])-1 < t17_t4_mem1*MAS_MEM[7]
	S += t17_t4_mem1 <= t17_t4

	t170 = S.Task('t170', length=1, delay_cost=1)
	t170 += alt(MAS)
	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += MM_MEM[0]
	S += 19 < t170_mem0
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(MM_MEM)
	S += (t17_t1*MM[0])-1 < t170_mem1*MM_MEM[1]
	S += t170_mem1 <= t170

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	t17_t5 += alt(MAS)
	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	t17_t5_mem0 += MM_MEM[0]
	S += 19 < t17_t5_mem0
	S += t17_t5_mem0 <= t17_t5

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	t17_t5_mem1 += alt(MM_MEM)
	S += (t17_t1*MM[0])-1 < t17_t5_mem1*MM_MEM[1]
	S += t17_t5_mem1 <= t17_t5

	t40 = S.Task('t40', length=1, delay_cost=1)
	t40 += alt(MAS)
	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	t40_mem0 += alt(MM_MEM)
	S += (t4_t2*MM[0])-1 < t40_mem0*MM_MEM[0]
	S += t40_mem0 <= t40

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	t40_mem1 += alt(MAS_MEM)
	S += (t4_t5*MAS[0])-1 < t40_mem1*MAS_MEM[1]
	S += (t4_t5*MAS[1])-1 < t40_mem1*MAS_MEM[3]
	S += (t4_t5*MAS[2])-1 < t40_mem1*MAS_MEM[5]
	S += (t4_t5*MAS[3])-1 < t40_mem1*MAS_MEM[7]
	S += t40_mem1 <= t40

	t50 = S.Task('t50', length=1, delay_cost=1)
	t50 += alt(MAS)
	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	t50_mem0 += alt(MM_MEM)
	S += (t5_t2*MM[0])-1 < t50_mem0*MM_MEM[0]
	S += t50_mem0 <= t50

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	t50_mem1 += alt(MAS_MEM)
	S += (t5_t5*MAS[0])-1 < t50_mem1*MAS_MEM[1]
	S += (t5_t5*MAS[1])-1 < t50_mem1*MAS_MEM[3]
	S += (t5_t5*MAS[2])-1 < t50_mem1*MAS_MEM[5]
	S += (t5_t5*MAS[3])-1 < t50_mem1*MAS_MEM[7]
	S += t50_mem1 <= t50

	t6_t1 = S.Task('t6_t1', length=7, delay_cost=1)
	t6_t1 += alt(MM)
	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	t6_t1_in += alt(MM_in)
	S += t6_t1_in*MM_in[0]<=t6_t1*MM[0]
	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	t6_t1_mem0 += MAS_MEM[4]
	S += 15 < t6_t1_mem0
	S += t6_t1_mem0 <= t6_t1

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	t6_t1_mem1 += alt(MAS_MEM)
	S += (t51*MAS[0])-1 < t6_t1_mem1*MAS_MEM[1]
	S += (t51*MAS[1])-1 < t6_t1_mem1*MAS_MEM[3]
	S += (t51*MAS[2])-1 < t6_t1_mem1*MAS_MEM[5]
	S += (t51*MAS[3])-1 < t6_t1_mem1*MAS_MEM[7]
	S += t6_t1_mem1 <= t6_t1

	t7_t1 = S.Task('t7_t1', length=7, delay_cost=1)
	t7_t1 += alt(MM)
	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	t7_t1_in += alt(MM_in)
	S += t7_t1_in*MM_in[0]<=t7_t1*MM[0]
	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	t7_t1_mem0 += MAIN_MEM_r[0]
	S += t7_t1_mem0 <= t7_t1

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	t7_t1_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < t7_t1_mem1*MAS_MEM[1]
	S += (t41*MAS[1])-1 < t7_t1_mem1*MAS_MEM[3]
	S += (t41*MAS[2])-1 < t7_t1_mem1*MAS_MEM[5]
	S += (t41*MAS[3])-1 < t7_t1_mem1*MAS_MEM[7]
	S += t7_t1_mem1 <= t7_t1

	t9_t1 = S.Task('t9_t1', length=7, delay_cost=1)
	t9_t1 += alt(MM)
	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	t9_t1_in += alt(MM_in)
	S += t9_t1_in*MM_in[0]<=t9_t1*MM[0]
	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	t9_t1_mem0 += MAIN_MEM_r[0]
	S += t9_t1_mem0 <= t9_t1

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	t9_t1_mem1 += alt(MAS_MEM)
	S += (t51*MAS[0])-1 < t9_t1_mem1*MAS_MEM[1]
	S += (t51*MAS[1])-1 < t9_t1_mem1*MAS_MEM[3]
	S += (t51*MAS[2])-1 < t9_t1_mem1*MAS_MEM[5]
	S += (t51*MAS[3])-1 < t9_t1_mem1*MAS_MEM[7]
	S += t9_t1_mem1 <= t9_t1

	t161 = S.Task('t161', length=1, delay_cost=1)
	t161 += alt(MAS)
	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += alt(MM_MEM)
	S += (t16_t4*MM[0])-1 < t161_mem0*MM_MEM[0]
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += alt(MAS_MEM)
	S += (t16_t5*MAS[0])-1 < t161_mem1*MAS_MEM[1]
	S += (t16_t5*MAS[1])-1 < t161_mem1*MAS_MEM[3]
	S += (t16_t5*MAS[2])-1 < t161_mem1*MAS_MEM[5]
	S += (t16_t5*MAS[3])-1 < t161_mem1*MAS_MEM[7]
	S += t161_mem1 <= t161

	t171 = S.Task('t171', length=1, delay_cost=1)
	t171 += alt(MAS)
	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(MM_MEM)
	S += (t17_t4*MM[0])-1 < t171_mem0*MM_MEM[0]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += alt(MAS_MEM)
	S += (t17_t5*MAS[0])-1 < t171_mem1*MAS_MEM[1]
	S += (t17_t5*MAS[1])-1 < t171_mem1*MAS_MEM[3]
	S += (t17_t5*MAS[2])-1 < t171_mem1*MAS_MEM[5]
	S += (t17_t5*MAS[3])-1 < t171_mem1*MAS_MEM[7]
	S += t171_mem1 <= t171

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)
	S += 0<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += alt(MAS_MEM)
	S += (t160*MAS[0])-1 < c000_mem0*MAS_MEM[0]
	S += (t160*MAS[1])-1 < c000_mem0*MAS_MEM[2]
	S += (t160*MAS[2])-1 < c000_mem0*MAS_MEM[4]
	S += (t160*MAS[3])-1 < c000_mem0*MAS_MEM[6]
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (t170*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (t170*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (t170*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (t170*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += c000_mem1 <= c000

	t6_t0 = S.Task('t6_t0', length=7, delay_cost=1)
	t6_t0 += alt(MM)
	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	t6_t0_in += alt(MM_in)
	S += t6_t0_in*MM_in[0]<=t6_t0*MM[0]
	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	t6_t0_mem0 += MAS_MEM[6]
	S += 10 < t6_t0_mem0
	S += t6_t0_mem0 <= t6_t0

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	t6_t0_mem1 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t6_t0_mem1*MAS_MEM[1]
	S += (t50*MAS[1])-1 < t6_t0_mem1*MAS_MEM[3]
	S += (t50*MAS[2])-1 < t6_t0_mem1*MAS_MEM[5]
	S += (t50*MAS[3])-1 < t6_t0_mem1*MAS_MEM[7]
	S += t6_t0_mem1 <= t6_t0

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	t6_t3 += alt(MAS)
	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	t6_t3_mem0 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t6_t3_mem0*MAS_MEM[0]
	S += (t50*MAS[1])-1 < t6_t3_mem0*MAS_MEM[2]
	S += (t50*MAS[2])-1 < t6_t3_mem0*MAS_MEM[4]
	S += (t50*MAS[3])-1 < t6_t3_mem0*MAS_MEM[6]
	S += t6_t3_mem0 <= t6_t3

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	t6_t3_mem1 += alt(MAS_MEM)
	S += (t51*MAS[0])-1 < t6_t3_mem1*MAS_MEM[1]
	S += (t51*MAS[1])-1 < t6_t3_mem1*MAS_MEM[3]
	S += (t51*MAS[2])-1 < t6_t3_mem1*MAS_MEM[5]
	S += (t51*MAS[3])-1 < t6_t3_mem1*MAS_MEM[7]
	S += t6_t3_mem1 <= t6_t3

	t7_t0 = S.Task('t7_t0', length=7, delay_cost=1)
	t7_t0 += alt(MM)
	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	t7_t0_in += alt(MM_in)
	S += t7_t0_in*MM_in[0]<=t7_t0*MM[0]
	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	t7_t0_mem0 += MAIN_MEM_r[0]
	S += t7_t0_mem0 <= t7_t0

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	t7_t0_mem1 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < t7_t0_mem1*MAS_MEM[1]
	S += (t40*MAS[1])-1 < t7_t0_mem1*MAS_MEM[3]
	S += (t40*MAS[2])-1 < t7_t0_mem1*MAS_MEM[5]
	S += (t40*MAS[3])-1 < t7_t0_mem1*MAS_MEM[7]
	S += t7_t0_mem1 <= t7_t0

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	t7_t3 += alt(MAS)
	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	t7_t3_mem0 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < t7_t3_mem0*MAS_MEM[0]
	S += (t40*MAS[1])-1 < t7_t3_mem0*MAS_MEM[2]
	S += (t40*MAS[2])-1 < t7_t3_mem0*MAS_MEM[4]
	S += (t40*MAS[3])-1 < t7_t3_mem0*MAS_MEM[6]
	S += t7_t3_mem0 <= t7_t3

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	t7_t3_mem1 += alt(MAS_MEM)
	S += (t41*MAS[0])-1 < t7_t3_mem1*MAS_MEM[1]
	S += (t41*MAS[1])-1 < t7_t3_mem1*MAS_MEM[3]
	S += (t41*MAS[2])-1 < t7_t3_mem1*MAS_MEM[5]
	S += (t41*MAS[3])-1 < t7_t3_mem1*MAS_MEM[7]
	S += t7_t3_mem1 <= t7_t3

	t9_t0 = S.Task('t9_t0', length=7, delay_cost=1)
	t9_t0 += alt(MM)
	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	t9_t0_in += alt(MM_in)
	S += t9_t0_in*MM_in[0]<=t9_t0*MM[0]
	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	t9_t0_mem0 += MAIN_MEM_r[0]
	S += t9_t0_mem0 <= t9_t0

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	t9_t0_mem1 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t9_t0_mem1*MAS_MEM[1]
	S += (t50*MAS[1])-1 < t9_t0_mem1*MAS_MEM[3]
	S += (t50*MAS[2])-1 < t9_t0_mem1*MAS_MEM[5]
	S += (t50*MAS[3])-1 < t9_t0_mem1*MAS_MEM[7]
	S += t9_t0_mem1 <= t9_t0

	t9_t3 = S.Task('t9_t3', length=1, delay_cost=1)
	t9_t3 += alt(MAS)
	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	t9_t3_mem0 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t9_t3_mem0*MAS_MEM[0]
	S += (t50*MAS[1])-1 < t9_t3_mem0*MAS_MEM[2]
	S += (t50*MAS[2])-1 < t9_t3_mem0*MAS_MEM[4]
	S += (t50*MAS[3])-1 < t9_t3_mem0*MAS_MEM[6]
	S += t9_t3_mem0 <= t9_t3

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	t9_t3_mem1 += alt(MAS_MEM)
	S += (t51*MAS[0])-1 < t9_t3_mem1*MAS_MEM[1]
	S += (t51*MAS[1])-1 < t9_t3_mem1*MAS_MEM[3]
	S += (t51*MAS[2])-1 < t9_t3_mem1*MAS_MEM[5]
	S += (t51*MAS[3])-1 < t9_t3_mem1*MAS_MEM[7]
	S += t9_t3_mem1 <= t9_t3

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)
	S += 0<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < c001_mem0*MAS_MEM[0]
	S += (t161*MAS[1])-1 < c001_mem0*MAS_MEM[2]
	S += (t161*MAS[2])-1 < c001_mem0*MAS_MEM[4]
	S += (t161*MAS[3])-1 < c001_mem0*MAS_MEM[6]
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (t171*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += (t171*MAS[1])-1 < c001_mem1*MAS_MEM[3]
	S += (t171*MAS[2])-1 < c001_mem1*MAS_MEM[5]
	S += (t171*MAS[3])-1 < c001_mem1*MAS_MEM[7]
	S += c001_mem1 <= c001

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM1_stage1MAS4/EP2_ADD_w_EVAL/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

