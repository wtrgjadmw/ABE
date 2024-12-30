from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 227
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=14)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=3)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=3, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=6)
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

	t2_t0 = S.Task('t2_t0', length=14, delay_cost=1)
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

	t2_t1 = S.Task('t2_t1', length=14, delay_cost=1)
	S += t2_t1 >= 2
	t2_t1 += MM[0]

	t0_t0 = S.Task('t0_t0', length=14, delay_cost=1)
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

	t0_t1 = S.Task('t0_t1', length=14, delay_cost=1)
	S += t0_t1 >= 4
	t0_t1 += MM[0]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 4
	t2_t2_in += MAS_in[1]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 4
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 4
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=3, delay_cost=1)
	S += t2_t2 >= 5
	t2_t2 += MAS[1]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 5
	t2_t3_in += MAS_in[0]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 5
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 5
	t2_t3_mem1 += MAIN_MEM_r[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 6
	t0_t2_in += MAS_in[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 6
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 6
	t0_t2_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=3, delay_cost=1)
	S += t2_t3 >= 6
	t2_t3 += MAS[0]

	t0_t2 = S.Task('t0_t2', length=3, delay_cost=1)
	S += t0_t2 >= 7
	t0_t2 += MAS[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 7
	t0_t3_in += MAS_in[2]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 7
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 7
	t0_t3_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=3, delay_cost=1)
	S += t0_t3 >= 8
	t0_t3 += MAS[2]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 8
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 8
	t2_t4_mem0 += MAS_MEM[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 8
	t2_t4_mem1 += MAS_MEM[1]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 8
	t7_t2_in += MAS_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 8
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 8
	t7_t2_mem1 += MAIN_MEM_r[1]

	new_TZ_t2_in = S.Task('new_TZ_t2_in', length=1, delay_cost=1)
	S += new_TZ_t2_in >= 9
	new_TZ_t2_in += MAS_in[0]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 9
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 9
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t2_t4 = S.Task('t2_t4', length=14, delay_cost=1)
	S += t2_t4 >= 9
	t2_t4 += MM[0]

	t7_t2 = S.Task('t7_t2', length=3, delay_cost=1)
	S += t7_t2 >= 9
	t7_t2 += MAS[0]

	new_TZ_t2 = S.Task('new_TZ_t2', length=3, delay_cost=1)
	S += new_TZ_t2 >= 10
	new_TZ_t2 += MAS[0]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 10
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 10
	t0_t4_mem0 += MAS_MEM[2]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 10
	t0_t4_mem1 += MAS_MEM[5]

	t14_t2_in = S.Task('t14_t2_in', length=1, delay_cost=1)
	S += t14_t2_in >= 10
	t14_t2_in += MAS_in[0]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 10
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 10
	t14_t2_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=14, delay_cost=1)
	S += t0_t4 >= 11
	t0_t4 += MM[0]

	t14_t2 = S.Task('t14_t2', length=3, delay_cost=1)
	S += t14_t2 >= 11
	t14_t2 += MAS[0]

	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	S += t17_t2_in >= 11
	t17_t2_in += MAS_in[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 11
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 11
	t17_t2_mem1 += MAIN_MEM_r[1]

	t16_t2_in = S.Task('t16_t2_in', length=1, delay_cost=1)
	S += t16_t2_in >= 12
	t16_t2_in += MAS_in[0]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 12
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 12
	t16_t2_mem1 += MAIN_MEM_r[1]

	t17_t2 = S.Task('t17_t2', length=3, delay_cost=1)
	S += t17_t2 >= 12
	t17_t2 += MAS[0]

	t16_t2 = S.Task('t16_t2', length=3, delay_cost=1)
	S += t16_t2 >= 13
	t16_t2 += MAS[0]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 13
	t9_t2_in += MAS_in[0]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 13
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 13
	t9_t2_mem1 += MAIN_MEM_r[1]

	t9_t2 = S.Task('t9_t2', length=3, delay_cost=1)
	S += t9_t2 >= 14
	t9_t2 += MAS[0]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 15
	t20_in += MAS_in[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 15
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 15
	t20_mem1 += MM_MEM[1]

	t20 = S.Task('t20', length=3, delay_cost=1)
	S += t20 >= 16
	t20 += MAS[1]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 16
	t2_t5_in += MAS_in[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 16
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 16
	t2_t5_mem1 += MM_MEM[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 17
	t00_in += MAS_in[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 17
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 17
	t00_mem1 += MM_MEM[1]

	t2_t5 = S.Task('t2_t5', length=3, delay_cost=1)
	S += t2_t5 >= 17
	t2_t5 += MAS[0]

	t00 = S.Task('t00', length=3, delay_cost=1)
	S += t00 >= 18
	t00 += MAS[1]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 18
	t0_t5_in += MAS_in[2]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 18
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 18
	t0_t5_mem1 += MM_MEM[1]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 18
	t30_in += MAS_in[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 18
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 18
	t30_mem1 += MAS_MEM[3]

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	S += t0_t5 >= 19
	t0_t5 += MAS[2]

	t30 = S.Task('t30', length=3, delay_cost=1)
	S += t30 >= 19
	t30 += MAS[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 20
	t10_in += MAS_in[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 20
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 20
	t10_mem1 += MAS_MEM[3]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 21
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 21
	c010_mem0 += MAS_MEM[2]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 21
	c010_mem1 += MAIN_MEM_r[1]

	t10 = S.Task('t10', length=3, delay_cost=1)
	S += t10 >= 21
	t10 += MAS[1]

	c010 = S.Task('c010', length=14, delay_cost=1)
	S += c010 >= 22
	c010 += MM[0]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 22
	t16_t0_in += MM_in[0]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 22
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 22
	t16_t0_mem1 += MAS_MEM[3]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 22
	t21_in += MAS_in[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 22
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 22
	t21_mem1 += MAS_MEM[1]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 23
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 23
	c200_mem0 += MAS_MEM[2]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 23
	c200_mem1 += MAIN_MEM_r[1]

	t16_t0 = S.Task('t16_t0', length=14, delay_cost=1)
	S += t16_t0 >= 23
	t16_t0 += MM[0]

	t21 = S.Task('t21', length=3, delay_cost=1)
	S += t21 >= 23
	t21 += MAS[1]

	c200 = S.Task('c200', length=14, delay_cost=1)
	S += c200 >= 24
	c200 += MM[0]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 24
	t01_in += MAS_in[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 24
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 24
	t01_mem1 += MAS_MEM[5]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 24
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 24
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 24
	t17_t0_mem1 += MAS_MEM[3]

	t01 = S.Task('t01', length=3, delay_cost=1)
	S += t01 >= 25
	t01 += MAS[0]

	t17_t0 = S.Task('t17_t0', length=14, delay_cost=1)
	S += t17_t0 >= 25
	t17_t0 += MM[0]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 25
	t31_in += MAS_in[1]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 25
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 25
	t31_mem1 += MAS_MEM[3]

	t31 = S.Task('t31', length=3, delay_cost=1)
	S += t31 >= 26
	t31 += MAS[1]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 27
	t11_in += MAS_in[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 27
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 27
	t11_mem1 += MAS_MEM[1]

	t11 = S.Task('t11', length=3, delay_cost=1)
	S += t11 >= 28
	t11 += MAS[1]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 28
	t5_t3_in += MM_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 28
	t5_t3_mem0 += MAS_MEM[2]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 28
	t5_t3_mem1 += MAS_MEM[3]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 29
	t5_t1_in += MAS_in[2]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 29
	t5_t1_mem0 += MAS_MEM[2]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 29
	t5_t1_mem1 += MAS_MEM[3]

	t5_t3 = S.Task('t5_t3', length=14, delay_cost=1)
	S += t5_t3 >= 29
	t5_t3 += MM[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 30
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 30
	t4_t3_mem0 += MAS_MEM[2]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 30
	t4_t3_mem1 += MAS_MEM[3]

	t5_t1 = S.Task('t5_t1', length=3, delay_cost=1)
	S += t5_t1 >= 30
	t5_t1 += MAS[2]

	t4_t3 = S.Task('t4_t3', length=14, delay_cost=1)
	S += t4_t3 >= 31
	t4_t3 += MM[0]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 31
	t5_t0_in += MAS_in[2]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 31
	t5_t0_mem0 += MAS_MEM[2]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 31
	t5_t0_mem1 += MAS_MEM[3]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 32
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 32
	t17_t1_mem0 += MAIN_MEM_r[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 32
	t17_t1_mem1 += MAS_MEM[3]

	t5_t0 = S.Task('t5_t0', length=3, delay_cost=1)
	S += t5_t0 >= 32
	t5_t0 += MAS[2]

	t17_t1 = S.Task('t17_t1', length=14, delay_cost=1)
	S += t17_t1 >= 33
	t17_t1 += MM[0]

	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	S += t17_t3_in >= 33
	t17_t3_in += MAS_in[0]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 33
	t17_t3_mem0 += MAS_MEM[2]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 33
	t17_t3_mem1 += MAS_MEM[3]

	t16_t3_in = S.Task('t16_t3_in', length=1, delay_cost=1)
	S += t16_t3_in >= 34
	t16_t3_in += MAS_in[0]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 34
	t16_t3_mem0 += MAS_MEM[2]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 34
	t16_t3_mem1 += MAS_MEM[3]

	t17_t3 = S.Task('t17_t3', length=3, delay_cost=1)
	S += t17_t3 >= 34
	t17_t3 += MAS[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 34
	t5_t2_in += MM_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 34
	t5_t2_mem0 += MAS_MEM[4]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 34
	t5_t2_mem1 += MAS_MEM[5]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 35
	t16_t1_in += MM_in[0]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 35
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 35
	t16_t1_mem1 += MAS_MEM[3]

	t16_t3 = S.Task('t16_t3', length=3, delay_cost=1)
	S += t16_t3 >= 35
	t16_t3 += MAS[0]

	t5_t2 = S.Task('t5_t2', length=14, delay_cost=1)
	S += t5_t2 >= 35
	t5_t2 += MM[0]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 36
	c010_w += MAIN_MEM_w

	t16_t1 = S.Task('t16_t1', length=14, delay_cost=1)
	S += t16_t1 >= 36
	t16_t1 += MM[0]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 36
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 36
	t17_t4_mem0 += MAS_MEM[0]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 36
	t17_t4_mem1 += MAS_MEM[1]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 36
	t4_t1_in += MAS_in[2]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 36
	t4_t1_mem0 += MAS_MEM[2]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 36
	t4_t1_mem1 += MAS_MEM[3]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 37
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 37
	t16_t4_mem0 += MAS_MEM[0]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 37
	t16_t4_mem1 += MAS_MEM[1]

	t17_t4 = S.Task('t17_t4', length=14, delay_cost=1)
	S += t17_t4 >= 37
	t17_t4 += MM[0]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 37
	t4_t0_in += MAS_in[2]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 37
	t4_t0_mem0 += MAS_MEM[2]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 37
	t4_t0_mem1 += MAS_MEM[3]

	t4_t1 = S.Task('t4_t1', length=3, delay_cost=1)
	S += t4_t1 >= 37
	t4_t1 += MAS[2]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 38
	c200_w += MAIN_MEM_w

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 38
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 38
	c201_mem0 += MAS_MEM[2]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 38
	c201_mem1 += MAIN_MEM_r[1]

	t16_t4 = S.Task('t16_t4', length=14, delay_cost=1)
	S += t16_t4 >= 38
	t16_t4 += MM[0]

	t4_t0 = S.Task('t4_t0', length=3, delay_cost=1)
	S += t4_t0 >= 38
	t4_t0 += MAS[2]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 39
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 39
	c011_mem0 += MAS_MEM[2]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 39
	c011_mem1 += MAIN_MEM_r[1]

	c201 = S.Task('c201', length=14, delay_cost=1)
	S += c201 >= 39
	c201 += MM[0]

	c011 = S.Task('c011', length=14, delay_cost=1)
	S += c011 >= 40
	c011 += MM[0]

	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	S += new_TX_t2_in >= 40
	new_TX_t2_in += MAS_in[1]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 40
	new_TX_t2_mem0 += MAS_MEM[2]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 40
	new_TX_t2_mem1 += MAS_MEM[3]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 40
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 40
	t4_t2_mem0 += MAS_MEM[4]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 40
	t4_t2_mem1 += MAS_MEM[5]

	new_TX_t2 = S.Task('new_TX_t2', length=3, delay_cost=1)
	S += new_TX_t2 >= 41
	new_TX_t2 += MAS[1]

	t13_t2_in = S.Task('t13_t2_in', length=1, delay_cost=1)
	S += t13_t2_in >= 41
	t13_t2_in += MAS_in[0]

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 41
	t13_t2_mem0 += MAS_MEM[2]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 41
	t13_t2_mem1 += MAS_MEM[3]

	t4_t2 = S.Task('t4_t2', length=14, delay_cost=1)
	S += t4_t2 >= 41
	t4_t2 += MM[0]

	t13_t2 = S.Task('t13_t2', length=3, delay_cost=1)
	S += t13_t2 >= 42
	t13_t2 += MAS[0]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 42
	t51_in += MAS_in[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 42
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 42
	t51_mem1 += MM_MEM[1]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 42
	t6_t2_in += MAS_in[2]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 42
	t6_t2_mem0 += MAS_MEM[2]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 42
	t6_t2_mem1 += MAS_MEM[3]

	t51 = S.Task('t51', length=3, delay_cost=1)
	S += t51 >= 43
	t51 += MAS[1]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 43
	t5_t5_in += MAS_in[1]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 43
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 43
	t5_t5_mem1 += MM_MEM[1]

	t6_t2 = S.Task('t6_t2', length=3, delay_cost=1)
	S += t6_t2 >= 43
	t6_t2 += MAS[2]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 44
	t41_in += MAS_in[0]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 44
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 44
	t41_mem1 += MM_MEM[1]

	t5_t5 = S.Task('t5_t5', length=3, delay_cost=1)
	S += t5_t5 >= 44
	t5_t5 += MAS[1]

	t41 = S.Task('t41', length=3, delay_cost=1)
	S += t41 >= 45
	t41 += MAS[0]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 45
	t4_t5_in += MAS_in[1]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 45
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 45
	t4_t5_mem1 += MM_MEM[1]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 45
	t9_t1_in += MM_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 45
	t9_t1_mem0 += MAIN_MEM_r[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 45
	t9_t1_mem1 += MAS_MEM[3]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 46
	t170_in += MAS_in[2]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 46
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 46
	t170_mem1 += MM_MEM[1]

	t4_t5 = S.Task('t4_t5', length=3, delay_cost=1)
	S += t4_t5 >= 46
	t4_t5 += MAS[1]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 46
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 46
	t6_t1_mem0 += MAS_MEM[2]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 46
	t6_t1_mem1 += MAS_MEM[3]

	t9_t1 = S.Task('t9_t1', length=14, delay_cost=1)
	S += t9_t1 >= 46
	t9_t1 += MM[0]

	t170 = S.Task('t170', length=3, delay_cost=1)
	S += t170 >= 47
	t170 += MAS[2]

	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	S += t17_t5_in >= 47
	t17_t5_in += MAS_in[2]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 47
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 47
	t17_t5_mem1 += MM_MEM[1]

	t6_t1 = S.Task('t6_t1', length=14, delay_cost=1)
	S += t6_t1 >= 47
	t6_t1 += MM[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 47
	t7_t1_in += MM_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 47
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 47
	t7_t1_mem1 += MAS_MEM[1]

	t17_t5 = S.Task('t17_t5', length=3, delay_cost=1)
	S += t17_t5 >= 48
	t17_t5 += MAS[2]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 48
	t50_in += MAS_in[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 48
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 48
	t50_mem1 += MAS_MEM[3]

	t7_t1 = S.Task('t7_t1', length=14, delay_cost=1)
	S += t7_t1 >= 48
	t7_t1 += MM[0]

	t16_t5_in = S.Task('t16_t5_in', length=1, delay_cost=1)
	S += t16_t5_in >= 49
	t16_t5_in += MAS_in[2]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 49
	t16_t5_mem0 += MM_MEM[0]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 49
	t16_t5_mem1 += MM_MEM[1]

	t50 = S.Task('t50', length=3, delay_cost=1)
	S += t50 >= 49
	t50 += MAS[0]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 50
	t160_in += MAS_in[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 50
	t160_mem0 += MM_MEM[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 50
	t160_mem1 += MM_MEM[1]

	t16_t5 = S.Task('t16_t5', length=3, delay_cost=1)
	S += t16_t5 >= 50
	t16_t5 += MAS[2]

	t160 = S.Task('t160', length=3, delay_cost=1)
	S += t160 >= 51
	t160 += MAS[0]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 51
	t171_in += MAS_in[0]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 51
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 51
	t171_mem1 += MAS_MEM[5]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 51
	t9_t0_in += MM_in[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 51
	t9_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 51
	t9_t0_mem1 += MAS_MEM[1]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 51
	t9_t3_in += MAS_in[2]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 51
	t9_t3_mem0 += MAS_MEM[0]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 51
	t9_t3_mem1 += MAS_MEM[3]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 52
	t161_in += MAS_in[1]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 52
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 52
	t161_mem1 += MAS_MEM[5]

	t171 = S.Task('t171', length=3, delay_cost=1)
	S += t171 >= 52
	t171 += MAS[0]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 52
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 52
	t6_t0_mem0 += MAS_MEM[2]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 52
	t6_t0_mem1 += MAS_MEM[1]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 52
	t6_t3_in += MAS_in[0]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 52
	t6_t3_mem0 += MAS_MEM[0]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 52
	t6_t3_mem1 += MAS_MEM[3]

	t9_t0 = S.Task('t9_t0', length=14, delay_cost=1)
	S += t9_t0 >= 52
	t9_t0 += MM[0]

	t9_t3 = S.Task('t9_t3', length=3, delay_cost=1)
	S += t9_t3 >= 52
	t9_t3 += MAS[2]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 53
	c000_in += MAS_in[2]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 53
	c000_mem0 += MAS_MEM[0]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 53
	c000_mem1 += MAS_MEM[5]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 53
	c201_w += MAIN_MEM_w

	t161 = S.Task('t161', length=3, delay_cost=1)
	S += t161 >= 53
	t161 += MAS[1]

	t6_t0 = S.Task('t6_t0', length=14, delay_cost=1)
	S += t6_t0 >= 53
	t6_t0 += MM[0]

	t6_t3 = S.Task('t6_t3', length=3, delay_cost=1)
	S += t6_t3 >= 53
	t6_t3 += MAS[0]

	c000 = S.Task('c000', length=3, delay_cost=1)
	S += c000 >= 54
	c000 += MAS[2]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 54
	c011_w += MAIN_MEM_w

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 54
	t40_in += MAS_in[1]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 54
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 54
	t40_mem1 += MAS_MEM[3]

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	S += t9_t4_in >= 54
	t9_t4_in += MM_in[0]

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	S += t9_t4_mem0 >= 54
	t9_t4_mem0 += MAS_MEM[0]

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	S += t9_t4_mem1 >= 54
	t9_t4_mem1 += MAS_MEM[5]

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 55
	c001_in += MAS_in[0]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 55
	c001_mem0 += MAS_MEM[2]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 55
	c001_mem1 += MAS_MEM[1]

	t40 = S.Task('t40', length=3, delay_cost=1)
	S += t40 >= 55
	t40 += MAS[1]

	t9_t4 = S.Task('t9_t4', length=14, delay_cost=1)
	S += t9_t4 >= 55
	t9_t4 += MM[0]

	c001 = S.Task('c001', length=3, delay_cost=1)
	S += c001 >= 56
	c001 += MAS[0]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 56
	t6_t4_in += MM_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 56
	t6_t4_mem0 += MAS_MEM[4]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 56
	t6_t4_mem1 += MAS_MEM[1]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 57
	c000_w += MAIN_MEM_w

	t6_t4 = S.Task('t6_t4', length=14, delay_cost=1)
	S += t6_t4 >= 57
	t6_t4 += MM[0]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 57
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 57
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 57
	t7_t0_mem1 += MAS_MEM[3]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 57
	t7_t3_in += MAS_in[1]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 57
	t7_t3_mem0 += MAS_MEM[2]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 57
	t7_t3_mem1 += MAS_MEM[1]

	t7_t0 = S.Task('t7_t0', length=14, delay_cost=1)
	S += t7_t0 >= 58
	t7_t0 += MM[0]

	t7_t3 = S.Task('t7_t3', length=3, delay_cost=1)
	S += t7_t3 >= 58
	t7_t3 += MAS[1]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 59
	c001_w += MAIN_MEM_w

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 60
	t7_t4_in += MM_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 60
	t7_t4_mem0 += MAS_MEM[0]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 60
	t7_t4_mem1 += MAS_MEM[3]

	t7_t4 = S.Task('t7_t4', length=14, delay_cost=1)
	S += t7_t4 >= 61
	t7_t4 += MM[0]

	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	S += t9_t5_in >= 65
	t9_t5_in += MAS_in[1]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 65
	t9_t5_mem0 += MM_MEM[0]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 65
	t9_t5_mem1 += MM_MEM[1]

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 66
	t60_in += MAS_in[0]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 66
	t60_mem0 += MM_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 66
	t60_mem1 += MM_MEM[1]

	t9_t5 = S.Task('t9_t5', length=3, delay_cost=1)
	S += t9_t5 >= 66
	t9_t5 += MAS[1]

	t60 = S.Task('t60', length=3, delay_cost=1)
	S += t60 >= 67
	t60 += MAS[0]

	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	S += t6_t5_in >= 67
	t6_t5_in += MAS_in[2]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 67
	t6_t5_mem0 += MM_MEM[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 67
	t6_t5_mem1 += MM_MEM[1]

	t6_t5 = S.Task('t6_t5', length=3, delay_cost=1)
	S += t6_t5 >= 68
	t6_t5 += MAS[2]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 68
	t90_in += MAS_in[2]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 68
	t90_mem0 += MM_MEM[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 68
	t90_mem1 += MM_MEM[1]

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	S += t14_t0_in >= 69
	t14_t0_in += MM_in[0]

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	S += t14_t0_mem0 >= 69
	t14_t0_mem0 += MAIN_MEM_r[0]

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	S += t14_t0_mem1 >= 69
	t14_t0_mem1 += MAS_MEM[1]

	t90 = S.Task('t90', length=3, delay_cost=1)
	S += t90 >= 69
	t90 += MAS[2]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 69
	t91_in += MAS_in[0]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 69
	t91_mem0 += MM_MEM[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 69
	t91_mem1 += MAS_MEM[3]

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	S += new_TZ_t0_in >= 70
	new_TZ_t0_in += MM_in[0]

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_mem0 >= 70
	new_TZ_t0_mem0 += MAIN_MEM_r[0]

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_mem1 >= 70
	new_TZ_t0_mem1 += MAS_MEM[1]

	t14_t0 = S.Task('t14_t0', length=14, delay_cost=1)
	S += t14_t0 >= 70
	t14_t0 += MM[0]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 70
	t61_in += MAS_in[1]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 70
	t61_mem0 += MM_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 70
	t61_mem1 += MAS_MEM[5]

	t91 = S.Task('t91', length=3, delay_cost=1)
	S += t91 >= 70
	t91 += MAS[0]

	new_TZ_t0 = S.Task('new_TZ_t0', length=14, delay_cost=1)
	S += new_TZ_t0 >= 71
	new_TZ_t0 += MM[0]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 71
	t100_in += MAS_in[1]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 71
	t100_mem0 += MAS_MEM[4]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 71
	t100_mem1 += MAS_MEM[5]

	t61 = S.Task('t61', length=3, delay_cost=1)
	S += t61 >= 71
	t61 += MAS[1]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 71
	t7_t5_in += MAS_in[0]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 71
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 71
	t7_t5_mem1 += MM_MEM[1]

	t100 = S.Task('t100', length=3, delay_cost=1)
	S += t100 >= 72
	t100 += MAS[1]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 72
	t101_in += MAS_in[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 72
	t101_mem0 += MAS_MEM[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 72
	t101_mem1 += MAS_MEM[1]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 72
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 72
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 72
	t70_mem1 += MM_MEM[1]

	t7_t5 = S.Task('t7_t5', length=3, delay_cost=1)
	S += t7_t5 >= 72
	t7_t5 += MAS[0]

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	S += new_TZ_t1_in >= 73
	new_TZ_t1_in += MM_in[0]

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_mem0 >= 73
	new_TZ_t1_mem0 += MAIN_MEM_r[0]

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_mem1 >= 73
	new_TZ_t1_mem1 += MAS_MEM[3]

	t101 = S.Task('t101', length=3, delay_cost=1)
	S += t101 >= 73
	t101 += MAS[1]

	t70 = S.Task('t70', length=3, delay_cost=1)
	S += t70 >= 73
	t70 += MAS[0]

	new_TZ_t1 = S.Task('new_TZ_t1', length=14, delay_cost=1)
	S += new_TZ_t1 >= 74
	new_TZ_t1 += MM[0]

	new_TZ_t3_in = S.Task('new_TZ_t3_in', length=1, delay_cost=1)
	S += new_TZ_t3_in >= 74
	new_TZ_t3_in += MAS_in[2]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	S += new_TZ_t3_mem0 >= 74
	new_TZ_t3_mem0 += MAS_MEM[0]

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	S += new_TZ_t3_mem1 >= 74
	new_TZ_t3_mem1 += MAS_MEM[3]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 74
	t71_in += MAS_in[1]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 74
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 74
	t71_mem1 += MAS_MEM[1]

	new_TZ_t3 = S.Task('new_TZ_t3', length=3, delay_cost=1)
	S += new_TZ_t3 >= 75
	new_TZ_t3 += MAS[2]

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	S += t14_t1_in >= 75
	t14_t1_in += MM_in[0]

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	S += t14_t1_mem0 >= 75
	t14_t1_mem0 += MAIN_MEM_r[0]

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	S += t14_t1_mem1 >= 75
	t14_t1_mem1 += MAS_MEM[3]

	t71 = S.Task('t71', length=3, delay_cost=1)
	S += t71 >= 75
	t71 += MAS[1]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 75
	t80_in += MAS_in[2]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 75
	t80_mem0 += MAS_MEM[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 75
	t80_mem1 += MAS_MEM[1]

	t14_t1 = S.Task('t14_t1', length=14, delay_cost=1)
	S += t14_t1 >= 76
	t14_t1 += MM[0]

	t14_t3_in = S.Task('t14_t3_in', length=1, delay_cost=1)
	S += t14_t3_in >= 76
	t14_t3_in += MAS_in[0]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	S += t14_t3_mem0 >= 76
	t14_t3_mem0 += MAS_MEM[0]

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	S += t14_t3_mem1 >= 76
	t14_t3_mem1 += MAS_MEM[3]

	t80 = S.Task('t80', length=3, delay_cost=1)
	S += t80 >= 76
	t80 += MAS[2]

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	S += new_TZ_t4_in >= 77
	new_TZ_t4_in += MM_in[0]

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	S += new_TZ_t4_mem0 >= 77
	new_TZ_t4_mem0 += MAS_MEM[0]

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	S += new_TZ_t4_mem1 >= 77
	new_TZ_t4_mem1 += MAS_MEM[5]

	t14_t3 = S.Task('t14_t3', length=3, delay_cost=1)
	S += t14_t3 >= 77
	t14_t3 += MAS[0]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 77
	t81_in += MAS_in[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 77
	t81_mem0 += MAS_MEM[2]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 77
	t81_mem1 += MAS_MEM[3]

	new_TZ_t4 = S.Task('new_TZ_t4', length=14, delay_cost=1)
	S += new_TZ_t4 >= 78
	new_TZ_t4 += MM[0]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 78
	t110_in += MAS_in[0]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 78
	t110_mem0 += MAS_MEM[4]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 78
	t110_mem1 += MAS_MEM[3]

	t81 = S.Task('t81', length=3, delay_cost=1)
	S += t81 >= 78
	t81 += MAS[0]

	t110 = S.Task('t110', length=3, delay_cost=1)
	S += t110 >= 79
	t110 += MAS[0]

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	S += t14_t4_in >= 79
	t14_t4_in += MM_in[0]

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	S += t14_t4_mem0 >= 79
	t14_t4_mem0 += MAS_MEM[0]

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	S += t14_t4_mem1 >= 79
	t14_t4_mem1 += MAS_MEM[1]

	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	S += t111_in >= 80
	t111_in += MAS_in[2]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 80
	t111_mem0 += MAS_MEM[0]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 80
	t111_mem1 += MAS_MEM[3]

	t14_t4 = S.Task('t14_t4', length=14, delay_cost=1)
	S += t14_t4 >= 80
	t14_t4 += MM[0]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 81
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 81
	new_TX_t0_mem0 += MAS_MEM[2]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 81
	new_TX_t0_mem1 += MAS_MEM[1]

	t111 = S.Task('t111', length=3, delay_cost=1)
	S += t111 >= 81
	t111 += MAS[2]

	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	S += t120_in >= 81
	t120_in += MAS_in[0]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 81
	t120_mem0 += MAS_MEM[0]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 81
	t120_mem1 += MAS_MEM[5]

	new_TX_t0 = S.Task('new_TX_t0', length=14, delay_cost=1)
	S += new_TX_t0 >= 82
	new_TX_t0 += MM[0]

	t120 = S.Task('t120', length=3, delay_cost=1)
	S += t120 >= 82
	t120 += MAS[0]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 83
	new_TX_t1_in += MM_in[0]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 83
	new_TX_t1_mem0 += MAS_MEM[2]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 83
	new_TX_t1_mem1 += MAS_MEM[5]

	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	S += t121_in >= 83
	t121_in += MAS_in[0]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 83
	t121_mem0 += MAS_MEM[4]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 83
	t121_mem1 += MAS_MEM[1]

	new_TX_t1 = S.Task('new_TX_t1', length=14, delay_cost=1)
	S += new_TX_t1 >= 84
	new_TX_t1 += MM[0]

	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	S += new_TX_t3_in >= 84
	new_TX_t3_in += MAS_in[2]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 84
	new_TX_t3_mem0 += MAS_MEM[0]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 84
	new_TX_t3_mem1 += MAS_MEM[5]

	t121 = S.Task('t121', length=3, delay_cost=1)
	S += t121 >= 84
	t121 += MAS[0]

	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	S += t13_t0_in >= 84
	t13_t0_in += MM_in[0]

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	S += t13_t0_mem0 >= 84
	t13_t0_mem0 += MAS_MEM[2]

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	S += t13_t0_mem1 >= 84
	t13_t0_mem1 += MAS_MEM[1]

	new_TX_t3 = S.Task('new_TX_t3', length=3, delay_cost=1)
	S += new_TX_t3 >= 85
	new_TX_t3 += MAS[2]

	t13_t0 = S.Task('t13_t0', length=14, delay_cost=1)
	S += t13_t0 >= 85
	t13_t0 += MM[0]

	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	S += t13_t1_in >= 86
	t13_t1_in += MM_in[0]

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	S += t13_t1_mem0 >= 86
	t13_t1_mem0 += MAS_MEM[2]

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	S += t13_t1_mem1 >= 86
	t13_t1_mem1 += MAS_MEM[1]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 87
	new_TX_t4_in += MM_in[0]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 87
	new_TX_t4_mem0 += MAS_MEM[2]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 87
	new_TX_t4_mem1 += MAS_MEM[5]

	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	S += new_TZ0_in >= 87
	new_TZ0_in += MAS_in[2]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 87
	new_TZ0_mem0 += MM_MEM[0]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 87
	new_TZ0_mem1 += MM_MEM[1]

	t13_t1 = S.Task('t13_t1', length=14, delay_cost=1)
	S += t13_t1 >= 87
	t13_t1 += MM[0]

	t13_t3_in = S.Task('t13_t3_in', length=1, delay_cost=1)
	S += t13_t3_in >= 87
	t13_t3_in += MAS_in[1]

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	S += t13_t3_mem0 >= 87
	t13_t3_mem0 += MAS_MEM[0]

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	S += t13_t3_mem1 >= 87
	t13_t3_mem1 += MAS_MEM[1]

	new_TX_t4 = S.Task('new_TX_t4', length=14, delay_cost=1)
	S += new_TX_t4 >= 88
	new_TX_t4 += MM[0]

	new_TZ0 = S.Task('new_TZ0', length=3, delay_cost=1)
	S += new_TZ0 >= 88
	new_TZ0 += MAS[2]

	new_TZ_t5_in = S.Task('new_TZ_t5_in', length=1, delay_cost=1)
	S += new_TZ_t5_in >= 88
	new_TZ_t5_in += MAS_in[0]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	S += new_TZ_t5_mem0 >= 88
	new_TZ_t5_mem0 += MM_MEM[0]

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	S += new_TZ_t5_mem1 >= 88
	new_TZ_t5_mem1 += MM_MEM[1]

	t13_t3 = S.Task('t13_t3', length=3, delay_cost=1)
	S += t13_t3 >= 88
	t13_t3 += MAS[1]

	new_TZ_t5 = S.Task('new_TZ_t5', length=3, delay_cost=1)
	S += new_TZ_t5 >= 89
	new_TZ_t5 += MAS[0]

	t14_t5_in = S.Task('t14_t5_in', length=1, delay_cost=1)
	S += t14_t5_in >= 89
	t14_t5_in += MAS_in[0]

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	S += t14_t5_mem0 >= 89
	t14_t5_mem0 += MM_MEM[0]

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	S += t14_t5_mem1 >= 89
	t14_t5_mem1 += MM_MEM[1]

	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	S += t13_t4_in >= 90
	t13_t4_in += MM_in[0]

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	S += t13_t4_mem0 >= 90
	t13_t4_mem0 += MAS_MEM[0]

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	S += t13_t4_mem1 >= 90
	t13_t4_mem1 += MAS_MEM[3]

	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	S += t140_in >= 90
	t140_in += MAS_in[0]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 90
	t140_mem0 += MM_MEM[0]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 90
	t140_mem1 += MM_MEM[1]

	t14_t5 = S.Task('t14_t5', length=3, delay_cost=1)
	S += t14_t5 >= 90
	t14_t5 += MAS[0]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 91
	new_TZ0_w += MAIN_MEM_w

	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	S += new_TZ1_in >= 91
	new_TZ1_in += MAS_in[0]

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 91
	new_TZ1_mem0 += MM_MEM[0]

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	S += new_TZ1_mem1 >= 91
	new_TZ1_mem1 += MAS_MEM[1]

	t13_t4 = S.Task('t13_t4', length=14, delay_cost=1)
	S += t13_t4 >= 91
	t13_t4 += MM[0]

	t140 = S.Task('t140', length=3, delay_cost=1)
	S += t140 >= 91
	t140 += MAS[0]

	new_TZ1 = S.Task('new_TZ1', length=3, delay_cost=1)
	S += new_TZ1 >= 92
	new_TZ1 += MAS[0]

	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	S += t141_in >= 93
	t141_in += MAS_in[2]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 93
	t141_mem0 += MM_MEM[0]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 93
	t141_mem1 += MAS_MEM[1]

	t141 = S.Task('t141', length=3, delay_cost=1)
	S += t141 >= 94
	t141 += MAS[2]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 95
	new_TZ1_w += MAIN_MEM_w

	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	S += new_TX0_in >= 97
	new_TX0_in += MAS_in[0]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 97
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 97
	new_TX0_mem1 += MM_MEM[1]

	new_TX0 = S.Task('new_TX0', length=3, delay_cost=1)
	S += new_TX0 >= 98
	new_TX0 += MAS[0]

	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	S += new_TX_t5_in >= 98
	new_TX_t5_in += MAS_in[2]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 98
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 98
	new_TX_t5_mem1 += MM_MEM[1]

	new_TX_t5 = S.Task('new_TX_t5', length=3, delay_cost=1)
	S += new_TX_t5 >= 99
	new_TX_t5 += MAS[2]

	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	S += t130_in >= 100
	t130_in += MAS_in[1]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 100
	t130_mem0 += MM_MEM[0]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 100
	t130_mem1 += MM_MEM[1]

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 101
	new_TX0_w += MAIN_MEM_w

	t130 = S.Task('t130', length=3, delay_cost=1)
	S += t130 >= 101
	t130 += MAS[1]

	t13_t5_in = S.Task('t13_t5_in', length=1, delay_cost=1)
	S += t13_t5_in >= 101
	t13_t5_in += MAS_in[1]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	S += t13_t5_mem0 >= 101
	t13_t5_mem0 += MM_MEM[0]

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	S += t13_t5_mem1 >= 101
	t13_t5_mem1 += MM_MEM[1]

	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	S += new_TX1_in >= 102
	new_TX1_in += MAS_in[2]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 102
	new_TX1_mem0 += MM_MEM[0]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 102
	new_TX1_mem1 += MAS_MEM[5]

	t13_t5 = S.Task('t13_t5', length=3, delay_cost=1)
	S += t13_t5 >= 102
	t13_t5 += MAS[1]

	new_TX1 = S.Task('new_TX1', length=3, delay_cost=1)
	S += new_TX1 >= 103
	new_TX1 += MAS[2]

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 103
	t150_in += MAS_in[0]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 103
	t150_mem0 += MAS_MEM[2]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 103
	t150_mem1 += MAS_MEM[1]

	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	S += t131_in >= 104
	t131_in += MAS_in[0]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 104
	t131_mem0 += MM_MEM[0]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 104
	t131_mem1 += MAS_MEM[3]

	t150 = S.Task('t150', length=3, delay_cost=1)
	S += t150 >= 104
	t150 += MAS[0]

	t131 = S.Task('t131', length=3, delay_cost=1)
	S += t131 >= 105
	t131 += MAS[0]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 106
	new_TX1_w += MAIN_MEM_w


	# new tasks
	t151 = S.Task('t151', length=3, delay_cost=1)
	t151 += alt(MAS)
	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	t151_in += alt(MAS_in)
	S += t151_in*MAS_in[0]<=t151*MAS[0]

	S += t151_in*MAS_in[1]<=t151*MAS[1]

	S += t151_in*MAS_in[2]<=t151*MAS[2]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[0]
	S += 107 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += MAS_MEM[5]
	S += 96 < t151_mem1
	S += t151_mem1 <= t151

	new_TY0 = S.Task('new_TY0', length=3, delay_cost=1)
	new_TY0 += alt(MAS)
	new_TY0_in = S.Task('new_TY0_in', length=1, delay_cost=1)
	new_TY0_in += alt(MAS_in)
	S += new_TY0_in*MAS_in[0]<=new_TY0*MAS[0]

	S += new_TY0_in*MAS_in[1]<=new_TY0*MAS[1]

	S += new_TY0_in*MAS_in[2]<=new_TY0*MAS[2]

	S += 70<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += MAIN_MEM_r[0]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += MAS_MEM[1]
	S += 106 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=3, delay_cost=1)
	new_TY1 += alt(MAS)
	new_TY1_in = S.Task('new_TY1_in', length=1, delay_cost=1)
	new_TY1_in += alt(MAS_in)
	S += new_TY1_in*MAS_in[0]<=new_TY1*MAS[0]

	S += new_TY1_in*MAS_in[1]<=new_TY1*MAS[1]

	S += new_TY1_in*MAS_in[2]<=new_TY1*MAS[2]

	S += 76<new_TY1

	new_TY1_w = S.Task('new_TY1_w', length=1, delay_cost=1)
	new_TY1_w += alt(MAIN_MEM_w)
	S += new_TY1 <= new_TY1_w

	new_TY1_mem0 = S.Task('new_TY1_mem0', length=1, delay_cost=1)
	new_TY1_mem0 += MAIN_MEM_r[0]
	S += new_TY1_mem0 <= new_TY1

	new_TY1_mem1 = S.Task('new_TY1_mem1', length=1, delay_cost=1)
	new_TY1_mem1 += alt(MAS_MEM)
	S += (t151*MAS[0])-1 < new_TY1_mem1*MAS_MEM[1]
	S += (t151*MAS[1])-1 < new_TY1_mem1*MAS_MEM[3]
	S += (t151*MAS[2])-1 < new_TY1_mem1*MAS_MEM[5]
	S += new_TY1_mem1 <= new_TY1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM1_stage3MAS3/EP2_ADD_w_EVAL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 4))

	return solution

