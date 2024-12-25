from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 208
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=7)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 0
	t2_t0_in += MM_in[1]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 0
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 0
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	S += t2_t0 >= 1
	t2_t0 += MM[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 1
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 1
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 1
	t2_t1_mem1 += MAIN_MEM_r[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 2
	t0_t1_in += MM_in[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 2
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 2
	t0_t1_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	S += t2_t1 >= 2
	t2_t1 += MM[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 3
	t0_t0_in += MM_in[1]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 3
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 3
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=7, delay_cost=1)
	S += t0_t1 >= 3
	t0_t1 += MM[1]

	t0_t0 = S.Task('t0_t0', length=7, delay_cost=1)
	S += t0_t0 >= 4
	t0_t0 += MM[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 4
	t0_t3_in += MAS_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 4
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 4
	t0_t3_mem1 += MAIN_MEM_r[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 5
	t0_t2_in += MAS_in[3]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 5
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 5
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=4, delay_cost=1)
	S += t0_t3 >= 5
	t0_t3 += MAS[0]

	t0_t2 = S.Task('t0_t2', length=4, delay_cost=1)
	S += t0_t2 >= 6
	t0_t2 += MAS[3]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 6
	t2_t3_in += MAS_in[2]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 6
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 6
	t2_t3_mem1 += MAIN_MEM_r[1]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 7
	t2_t2_in += MAS_in[2]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 7
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 7
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=4, delay_cost=1)
	S += t2_t3 >= 7
	t2_t3 += MAS[2]

	new_TZ_t2_in = S.Task('new_TZ_t2_in', length=1, delay_cost=1)
	S += new_TZ_t2_in >= 8
	new_TZ_t2_in += MAS_in[2]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 8
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 8
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 8
	t20_in += MAS_in[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 8
	t20_mem0 += MM_MEM[2]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 8
	t20_mem1 += MM_MEM[1]

	t2_t2 = S.Task('t2_t2', length=4, delay_cost=1)
	S += t2_t2 >= 8
	t2_t2 += MAS[2]

	new_TZ_t2 = S.Task('new_TZ_t2', length=4, delay_cost=1)
	S += new_TZ_t2 >= 9
	new_TZ_t2 += MAS[2]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 9
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 9
	t0_t4_mem0 += MAS_MEM[6]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 9
	t0_t4_mem1 += MAS_MEM[1]

	t16_t2_in = S.Task('t16_t2_in', length=1, delay_cost=1)
	S += t16_t2_in >= 9
	t16_t2_in += MAS_in[0]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 9
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 9
	t16_t2_mem1 += MAIN_MEM_r[1]

	t20 = S.Task('t20', length=4, delay_cost=1)
	S += t20 >= 9
	t20 += MAS[1]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 9
	t2_t5_in += MAS_in[1]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 9
	t2_t5_mem0 += MM_MEM[2]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 9
	t2_t5_mem1 += MM_MEM[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 10
	t00_in += MAS_in[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 10
	t00_mem0 += MM_MEM[2]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 10
	t00_mem1 += MM_MEM[3]

	t0_t4 = S.Task('t0_t4', length=7, delay_cost=1)
	S += t0_t4 >= 10
	t0_t4 += MM[0]

	t14_t2_in = S.Task('t14_t2_in', length=1, delay_cost=1)
	S += t14_t2_in >= 10
	t14_t2_in += MAS_in[1]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 10
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 10
	t14_t2_mem1 += MAIN_MEM_r[1]

	t16_t2 = S.Task('t16_t2', length=4, delay_cost=1)
	S += t16_t2 >= 10
	t16_t2 += MAS[0]

	t2_t5 = S.Task('t2_t5', length=4, delay_cost=1)
	S += t2_t5 >= 10
	t2_t5 += MAS[1]

	t00 = S.Task('t00', length=4, delay_cost=1)
	S += t00 >= 11
	t00 += MAS[0]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 11
	t0_t5_in += MAS_in[1]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 11
	t0_t5_mem0 += MM_MEM[2]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 11
	t0_t5_mem1 += MM_MEM[3]

	t14_t2 = S.Task('t14_t2', length=4, delay_cost=1)
	S += t14_t2 >= 11
	t14_t2 += MAS[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 11
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 11
	t2_t4_mem0 += MAS_MEM[4]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 11
	t2_t4_mem1 += MAS_MEM[5]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 11
	t7_t2_in += MAS_in[3]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 11
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 11
	t7_t2_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=4, delay_cost=1)
	S += t0_t5 >= 12
	t0_t5 += MAS[1]

	t2_t4 = S.Task('t2_t4', length=7, delay_cost=1)
	S += t2_t4 >= 12
	t2_t4 += MM[0]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 12
	t30_in += MAS_in[2]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 12
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 12
	t30_mem1 += MAS_MEM[3]

	t7_t2 = S.Task('t7_t2', length=4, delay_cost=1)
	S += t7_t2 >= 12
	t7_t2 += MAS[3]

	t30 = S.Task('t30', length=4, delay_cost=1)
	S += t30 >= 13
	t30 += MAS[2]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 13
	t9_t2_in += MAS_in[3]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 13
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 13
	t9_t2_mem1 += MAIN_MEM_r[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 14
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 14
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 14
	t10_mem1 += MAS_MEM[1]

	t9_t2 = S.Task('t9_t2', length=4, delay_cost=1)
	S += t9_t2 >= 14
	t9_t2 += MAS[3]

	t10 = S.Task('t10', length=4, delay_cost=1)
	S += t10 >= 15
	t10 += MAS[0]

	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	S += t17_t2_in >= 15
	t17_t2_in += MAS_in[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 15
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 15
	t17_t2_mem1 += MAIN_MEM_r[1]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 16
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 16
	c010_mem0 += MAS_MEM[4]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 16
	c010_mem1 += MAIN_MEM_r[1]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 16
	t01_in += MAS_in[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 16
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 16
	t01_mem1 += MAS_MEM[3]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 16
	t16_t0_in += MM_in[1]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 16
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 16
	t16_t0_mem1 += MAS_MEM[5]

	t17_t2 = S.Task('t17_t2', length=4, delay_cost=1)
	S += t17_t2 >= 16
	t17_t2 += MAS[0]

	c010 = S.Task('c010', length=7, delay_cost=1)
	S += c010 >= 17
	c010 += MM[0]

	t01 = S.Task('t01', length=4, delay_cost=1)
	S += t01 >= 17
	t01 += MAS[0]

	t16_t0 = S.Task('t16_t0', length=7, delay_cost=1)
	S += t16_t0 >= 17
	t16_t0 += MM[1]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 18
	c200_in += MM_in[1]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 18
	c200_mem0 += MAS_MEM[0]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 18
	c200_mem1 += MAIN_MEM_r[1]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 18
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 18
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 18
	t17_t0_mem1 += MAS_MEM[1]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 18
	t21_in += MAS_in[3]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 18
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 18
	t21_mem1 += MAS_MEM[3]

	c200 = S.Task('c200', length=7, delay_cost=1)
	S += c200 >= 19
	c200 += MM[1]

	t17_t0 = S.Task('t17_t0', length=7, delay_cost=1)
	S += t17_t0 >= 19
	t17_t0 += MM[0]

	t21 = S.Task('t21', length=4, delay_cost=1)
	S += t21 >= 19
	t21 += MAS[3]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 20
	t11_in += MAS_in[3]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 20
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 20
	t11_mem1 += MAS_MEM[1]

	t11 = S.Task('t11', length=4, delay_cost=1)
	S += t11 >= 21
	t11 += MAS[3]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 22
	t31_in += MAS_in[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 22
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 22
	t31_mem1 += MAS_MEM[7]

	t31 = S.Task('t31', length=4, delay_cost=1)
	S += t31 >= 23
	t31 += MAS[0]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 24
	c010_w += MAIN_MEM_w

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 24
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 24
	c201_mem0 += MAS_MEM[6]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 24
	c201_mem1 += MAIN_MEM_r[1]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 24
	t4_t3_in += MM_in[1]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 24
	t4_t3_mem0 += MAS_MEM[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 24
	t4_t3_mem1 += MAS_MEM[7]

	c201 = S.Task('c201', length=7, delay_cost=1)
	S += c201 >= 25
	c201 += MM[0]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 25
	t4_t1_in += MAS_in[1]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 25
	t4_t1_mem0 += MAS_MEM[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 25
	t4_t1_mem1 += MAS_MEM[7]

	t4_t3 = S.Task('t4_t3', length=7, delay_cost=1)
	S += t4_t3 >= 25
	t4_t3 += MM[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 26
	c200_w += MAIN_MEM_w

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 26
	t4_t0_in += MAS_in[1]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 26
	t4_t0_mem0 += MAS_MEM[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 26
	t4_t0_mem1 += MAS_MEM[7]

	t4_t1 = S.Task('t4_t1', length=4, delay_cost=1)
	S += t4_t1 >= 26
	t4_t1 += MAS[1]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 26
	t5_t3_in += MM_in[1]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 26
	t5_t3_mem0 += MAS_MEM[4]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 26
	t5_t3_mem1 += MAS_MEM[1]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 27
	c011_in += MM_in[1]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 27
	c011_mem0 += MAS_MEM[0]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 27
	c011_mem1 += MAIN_MEM_r[1]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 27
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 27
	t17_t1_mem0 += MAIN_MEM_r[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 27
	t17_t1_mem1 += MAS_MEM[7]

	t4_t0 = S.Task('t4_t0', length=4, delay_cost=1)
	S += t4_t0 >= 27
	t4_t0 += MAS[1]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 27
	t5_t0_in += MAS_in[3]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 27
	t5_t0_mem0 += MAS_MEM[4]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 27
	t5_t0_mem1 += MAS_MEM[1]

	t5_t3 = S.Task('t5_t3', length=7, delay_cost=1)
	S += t5_t3 >= 27
	t5_t3 += MM[1]

	c011 = S.Task('c011', length=7, delay_cost=1)
	S += c011 >= 28
	c011 += MM[1]

	t17_t1 = S.Task('t17_t1', length=7, delay_cost=1)
	S += t17_t1 >= 28
	t17_t1 += MM[0]

	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	S += t17_t3_in >= 28
	t17_t3_in += MAS_in[3]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 28
	t17_t3_mem0 += MAS_MEM[0]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 28
	t17_t3_mem1 += MAS_MEM[7]

	t5_t0 = S.Task('t5_t0', length=4, delay_cost=1)
	S += t5_t0 >= 28
	t5_t0 += MAS[3]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 28
	t5_t1_in += MAS_in[2]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 28
	t5_t1_mem0 += MAS_MEM[4]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 28
	t5_t1_mem1 += MAS_MEM[1]

	t13_t2_in = S.Task('t13_t2_in', length=1, delay_cost=1)
	S += t13_t2_in >= 29
	t13_t2_in += MAS_in[2]

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 29
	t13_t2_mem0 += MAS_MEM[0]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 29
	t13_t2_mem1 += MAS_MEM[7]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 29
	t16_t1_in += MM_in[1]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 29
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 29
	t16_t1_mem1 += MAS_MEM[1]

	t17_t3 = S.Task('t17_t3', length=4, delay_cost=1)
	S += t17_t3 >= 29
	t17_t3 += MAS[3]

	t5_t1 = S.Task('t5_t1', length=4, delay_cost=1)
	S += t5_t1 >= 29
	t5_t1 += MAS[2]

	t13_t2 = S.Task('t13_t2', length=4, delay_cost=1)
	S += t13_t2 >= 30
	t13_t2 += MAS[2]

	t16_t1 = S.Task('t16_t1', length=7, delay_cost=1)
	S += t16_t1 >= 30
	t16_t1 += MM[1]

	t16_t3_in = S.Task('t16_t3_in', length=1, delay_cost=1)
	S += t16_t3_in >= 30
	t16_t3_in += MAS_in[3]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 30
	t16_t3_mem0 += MAS_MEM[4]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 30
	t16_t3_mem1 += MAS_MEM[1]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 30
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 30
	t4_t2_mem0 += MAS_MEM[2]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 30
	t4_t2_mem1 += MAS_MEM[3]

	t16_t3 = S.Task('t16_t3', length=4, delay_cost=1)
	S += t16_t3 >= 31
	t16_t3 += MAS[3]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 31
	t41_in += MAS_in[3]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 31
	t41_mem0 += MM_MEM[2]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 31
	t41_mem1 += MM_MEM[3]

	t4_t2 = S.Task('t4_t2', length=7, delay_cost=1)
	S += t4_t2 >= 31
	t4_t2 += MM[0]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 31
	t6_t2_in += MAS_in[2]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 31
	t6_t2_mem0 += MAS_MEM[4]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 31
	t6_t2_mem1 += MAS_MEM[1]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 32
	c201_w += MAIN_MEM_w

	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	S += new_TX_t2_in >= 32
	new_TX_t2_in += MAS_in[1]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 32
	new_TX_t2_mem0 += MAS_MEM[4]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 32
	new_TX_t2_mem1 += MAS_MEM[1]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 32
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 32
	t17_t4_mem0 += MAS_MEM[0]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 32
	t17_t4_mem1 += MAS_MEM[7]

	t41 = S.Task('t41', length=4, delay_cost=1)
	S += t41 >= 32
	t41 += MAS[3]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 32
	t4_t5_in += MAS_in[0]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 32
	t4_t5_mem0 += MM_MEM[2]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 32
	t4_t5_mem1 += MM_MEM[3]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 32
	t5_t2_in += MM_in[1]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 32
	t5_t2_mem0 += MAS_MEM[6]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 32
	t5_t2_mem1 += MAS_MEM[5]

	t6_t2 = S.Task('t6_t2', length=4, delay_cost=1)
	S += t6_t2 >= 32
	t6_t2 += MAS[2]

	new_TX_t2 = S.Task('new_TX_t2', length=4, delay_cost=1)
	S += new_TX_t2 >= 33
	new_TX_t2 += MAS[1]

	t17_t4 = S.Task('t17_t4', length=7, delay_cost=1)
	S += t17_t4 >= 33
	t17_t4 += MM[0]

	t4_t5 = S.Task('t4_t5', length=4, delay_cost=1)
	S += t4_t5 >= 33
	t4_t5 += MAS[0]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 33
	t51_in += MAS_in[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 33
	t51_mem0 += MM_MEM[2]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 33
	t51_mem1 += MM_MEM[3]

	t5_t2 = S.Task('t5_t2', length=7, delay_cost=1)
	S += t5_t2 >= 33
	t5_t2 += MM[1]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 34
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 34
	t16_t4_mem0 += MAS_MEM[0]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 34
	t16_t4_mem1 += MAS_MEM[7]

	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	S += t17_t5_in >= 34
	t17_t5_in += MAS_in[0]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 34
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 34
	t17_t5_mem1 += MM_MEM[1]

	t51 = S.Task('t51', length=4, delay_cost=1)
	S += t51 >= 34
	t51 += MAS[1]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 34
	t5_t5_in += MAS_in[3]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 34
	t5_t5_mem0 += MM_MEM[2]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 34
	t5_t5_mem1 += MM_MEM[3]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 35
	c011_w += MAIN_MEM_w

	t16_t4 = S.Task('t16_t4', length=7, delay_cost=1)
	S += t16_t4 >= 35
	t16_t4 += MM[0]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 35
	t170_in += MAS_in[2]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 35
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 35
	t170_mem1 += MM_MEM[1]

	t17_t5 = S.Task('t17_t5', length=4, delay_cost=1)
	S += t17_t5 >= 35
	t17_t5 += MAS[0]

	t5_t5 = S.Task('t5_t5', length=4, delay_cost=1)
	S += t5_t5 >= 35
	t5_t5 += MAS[3]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 35
	t7_t1_in += MM_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 35
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 35
	t7_t1_mem1 += MAS_MEM[7]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 36
	t160_in += MAS_in[2]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 36
	t160_mem0 += MM_MEM[2]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 36
	t160_mem1 += MM_MEM[3]

	t170 = S.Task('t170', length=4, delay_cost=1)
	S += t170 >= 36
	t170 += MAS[2]

	t7_t1 = S.Task('t7_t1', length=7, delay_cost=1)
	S += t7_t1 >= 36
	t7_t1 += MM[0]

	t160 = S.Task('t160', length=4, delay_cost=1)
	S += t160 >= 37
	t160 += MAS[2]

	t16_t5_in = S.Task('t16_t5_in', length=1, delay_cost=1)
	S += t16_t5_in >= 37
	t16_t5_in += MAS_in[1]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 37
	t16_t5_mem0 += MM_MEM[2]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 37
	t16_t5_mem1 += MM_MEM[3]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 37
	t40_in += MAS_in[0]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 37
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 37
	t40_mem1 += MAS_MEM[1]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 37
	t9_t1_in += MM_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 37
	t9_t1_mem0 += MAIN_MEM_r[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 37
	t9_t1_mem1 += MAS_MEM[3]

	t16_t5 = S.Task('t16_t5', length=4, delay_cost=1)
	S += t16_t5 >= 38
	t16_t5 += MAS[1]

	t40 = S.Task('t40', length=4, delay_cost=1)
	S += t40 >= 38
	t40 += MAS[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 38
	t6_t1_in += MM_in[1]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 38
	t6_t1_mem0 += MAS_MEM[0]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 38
	t6_t1_mem1 += MAS_MEM[3]

	t9_t1 = S.Task('t9_t1', length=7, delay_cost=1)
	S += t9_t1 >= 38
	t9_t1 += MM[0]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 39
	t171_in += MAS_in[3]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 39
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 39
	t171_mem1 += MAS_MEM[1]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 39
	t50_in += MAS_in[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 39
	t50_mem0 += MM_MEM[2]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 39
	t50_mem1 += MAS_MEM[7]

	t6_t1 = S.Task('t6_t1', length=7, delay_cost=1)
	S += t6_t1 >= 39
	t6_t1 += MM[1]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 40
	c000_in += MAS_in[1]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 40
	c000_mem0 += MAS_MEM[4]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 40
	c000_mem1 += MAS_MEM[5]

	t171 = S.Task('t171', length=4, delay_cost=1)
	S += t171 >= 40
	t171 += MAS[3]

	t50 = S.Task('t50', length=4, delay_cost=1)
	S += t50 >= 40
	t50 += MAS[0]

	c000 = S.Task('c000', length=4, delay_cost=1)
	S += c000 >= 41
	c000 += MAS[1]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 41
	t161_in += MAS_in[3]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 41
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 41
	t161_mem1 += MAS_MEM[3]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 41
	t7_t0_in += MM_in[1]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 41
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 41
	t7_t0_mem1 += MAS_MEM[1]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 41
	t7_t3_in += MAS_in[2]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 41
	t7_t3_mem0 += MAS_MEM[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 41
	t7_t3_mem1 += MAS_MEM[7]

	t161 = S.Task('t161', length=4, delay_cost=1)
	S += t161 >= 42
	t161 += MAS[3]

	t7_t0 = S.Task('t7_t0', length=7, delay_cost=1)
	S += t7_t0 >= 42
	t7_t0 += MM[1]

	t7_t3 = S.Task('t7_t3', length=4, delay_cost=1)
	S += t7_t3 >= 42
	t7_t3 += MAS[2]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 43
	t6_t0_in += MM_in[1]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 43
	t6_t0_mem0 += MAS_MEM[4]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 43
	t6_t0_mem1 += MAS_MEM[1]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 43
	t9_t3_in += MAS_in[1]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 43
	t9_t3_mem0 += MAS_MEM[0]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 43
	t9_t3_mem1 += MAS_MEM[3]

	t6_t0 = S.Task('t6_t0', length=7, delay_cost=1)
	S += t6_t0 >= 44
	t6_t0 += MM[1]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 44
	t6_t3_in += MAS_in[3]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 44
	t6_t3_mem0 += MAS_MEM[0]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 44
	t6_t3_mem1 += MAS_MEM[3]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 44
	t9_t0_in += MM_in[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 44
	t9_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 44
	t9_t0_mem1 += MAS_MEM[1]

	t9_t3 = S.Task('t9_t3', length=4, delay_cost=1)
	S += t9_t3 >= 44
	t9_t3 += MAS[1]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 45
	c000_w += MAIN_MEM_w

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 45
	c001_in += MAS_in[0]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 45
	c001_mem0 += MAS_MEM[6]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 45
	c001_mem1 += MAS_MEM[7]

	t6_t3 = S.Task('t6_t3', length=4, delay_cost=1)
	S += t6_t3 >= 45
	t6_t3 += MAS[3]

	t9_t0 = S.Task('t9_t0', length=7, delay_cost=1)
	S += t9_t0 >= 45
	t9_t0 += MM[0]

	c001 = S.Task('c001', length=4, delay_cost=1)
	S += c001 >= 46
	c001 += MAS[0]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 46
	t7_t4_in += MM_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 46
	t7_t4_mem0 += MAS_MEM[6]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 46
	t7_t4_mem1 += MAS_MEM[5]

	t7_t4 = S.Task('t7_t4', length=7, delay_cost=1)
	S += t7_t4 >= 47
	t7_t4 += MM[0]

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	S += t9_t4_in >= 47
	t9_t4_in += MM_in[1]

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	S += t9_t4_mem0 >= 47
	t9_t4_mem0 += MAS_MEM[6]

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	S += t9_t4_mem1 >= 47
	t9_t4_mem1 += MAS_MEM[3]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 48
	t6_t4_in += MM_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 48
	t6_t4_mem0 += MAS_MEM[4]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 48
	t6_t4_mem1 += MAS_MEM[7]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 48
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 48
	t70_mem0 += MM_MEM[2]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 48
	t70_mem1 += MM_MEM[1]

	t9_t4 = S.Task('t9_t4', length=7, delay_cost=1)
	S += t9_t4 >= 48
	t9_t4 += MM[1]

	t6_t4 = S.Task('t6_t4', length=7, delay_cost=1)
	S += t6_t4 >= 49
	t6_t4 += MM[0]

	t70 = S.Task('t70', length=4, delay_cost=1)
	S += t70 >= 49
	t70 += MAS[0]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 49
	t7_t5_in += MAS_in[0]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 49
	t7_t5_mem0 += MM_MEM[2]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 49
	t7_t5_mem1 += MM_MEM[1]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 50
	c001_w += MAIN_MEM_w

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 50
	t60_in += MAS_in[1]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 50
	t60_mem0 += MM_MEM[2]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 50
	t60_mem1 += MM_MEM[3]

	t7_t5 = S.Task('t7_t5', length=4, delay_cost=1)
	S += t7_t5 >= 50
	t7_t5 += MAS[0]

	t60 = S.Task('t60', length=4, delay_cost=1)
	S += t60 >= 51
	t60 += MAS[1]

	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	S += t6_t5_in >= 51
	t6_t5_in += MAS_in[0]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 51
	t6_t5_mem0 += MM_MEM[2]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 51
	t6_t5_mem1 += MM_MEM[3]

	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	S += t9_t5_in >= 51
	t9_t5_in += MAS_in[2]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 51
	t9_t5_mem0 += MM_MEM[0]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 51
	t9_t5_mem1 += MM_MEM[1]

	t6_t5 = S.Task('t6_t5', length=4, delay_cost=1)
	S += t6_t5 >= 52
	t6_t5 += MAS[0]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 52
	t90_in += MAS_in[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 52
	t90_mem0 += MM_MEM[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 52
	t90_mem1 += MM_MEM[1]

	t9_t5 = S.Task('t9_t5', length=4, delay_cost=1)
	S += t9_t5 >= 52
	t9_t5 += MAS[2]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 53
	t71_in += MAS_in[3]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 53
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 53
	t71_mem1 += MAS_MEM[1]

	t90 = S.Task('t90', length=4, delay_cost=1)
	S += t90 >= 53
	t90 += MAS[0]

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	S += t14_t0_in >= 54
	t14_t0_in += MM_in[0]

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	S += t14_t0_mem0 >= 54
	t14_t0_mem0 += MAIN_MEM_r[0]

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	S += t14_t0_mem1 >= 54
	t14_t0_mem1 += MAS_MEM[3]

	t71 = S.Task('t71', length=4, delay_cost=1)
	S += t71 >= 54
	t71 += MAS[3]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 54
	t80_in += MAS_in[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 54
	t80_mem0 += MAS_MEM[2]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 54
	t80_mem1 += MAS_MEM[1]

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	S += new_TZ_t0_in >= 55
	new_TZ_t0_in += MM_in[1]

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_mem0 >= 55
	new_TZ_t0_mem0 += MAIN_MEM_r[0]

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_mem1 >= 55
	new_TZ_t0_mem1 += MAS_MEM[3]

	t14_t0 = S.Task('t14_t0', length=7, delay_cost=1)
	S += t14_t0 >= 55
	t14_t0 += MM[0]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 55
	t61_in += MAS_in[1]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 55
	t61_mem0 += MM_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 55
	t61_mem1 += MAS_MEM[1]

	t80 = S.Task('t80', length=4, delay_cost=1)
	S += t80 >= 55
	t80 += MAS[0]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 55
	t91_in += MAS_in[0]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 55
	t91_mem0 += MM_MEM[2]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 55
	t91_mem1 += MAS_MEM[5]

	new_TZ_t0 = S.Task('new_TZ_t0', length=7, delay_cost=1)
	S += new_TZ_t0 >= 56
	new_TZ_t0 += MM[1]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 56
	t100_in += MAS_in[0]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 56
	t100_mem0 += MAS_MEM[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 56
	t100_mem1 += MAS_MEM[1]

	t61 = S.Task('t61', length=4, delay_cost=1)
	S += t61 >= 56
	t61 += MAS[1]

	t91 = S.Task('t91', length=4, delay_cost=1)
	S += t91 >= 56
	t91 += MAS[0]

	t100 = S.Task('t100', length=4, delay_cost=1)
	S += t100 >= 57
	t100 += MAS[0]

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	S += new_TZ_t1_in >= 59
	new_TZ_t1_in += MM_in[1]

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_mem0 >= 59
	new_TZ_t1_mem0 += MAIN_MEM_r[0]

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_mem1 >= 59
	new_TZ_t1_mem1 += MAS_MEM[3]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 59
	t101_in += MAS_in[2]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 59
	t101_mem0 += MAS_MEM[0]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 59
	t101_mem1 += MAS_MEM[1]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 59
	t81_in += MAS_in[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 59
	t81_mem0 += MAS_MEM[2]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 59
	t81_mem1 += MAS_MEM[7]

	new_TZ_t1 = S.Task('new_TZ_t1', length=7, delay_cost=1)
	S += new_TZ_t1 >= 60
	new_TZ_t1 += MM[1]

	t101 = S.Task('t101', length=4, delay_cost=1)
	S += t101 >= 60
	t101 += MAS[2]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 60
	t110_in += MAS_in[3]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 60
	t110_mem0 += MAS_MEM[0]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 60
	t110_mem1 += MAS_MEM[1]

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	S += t14_t1_in >= 60
	t14_t1_in += MM_in[0]

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	S += t14_t1_mem0 >= 60
	t14_t1_mem0 += MAIN_MEM_r[0]

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	S += t14_t1_mem1 >= 60
	t14_t1_mem1 += MAS_MEM[3]

	t81 = S.Task('t81', length=4, delay_cost=1)
	S += t81 >= 60
	t81 += MAS[0]

	new_TZ_t3_in = S.Task('new_TZ_t3_in', length=1, delay_cost=1)
	S += new_TZ_t3_in >= 61
	new_TZ_t3_in += MAS_in[2]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	S += new_TZ_t3_mem0 >= 61
	new_TZ_t3_mem0 += MAS_MEM[2]

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	S += new_TZ_t3_mem1 >= 61
	new_TZ_t3_mem1 += MAS_MEM[3]

	t110 = S.Task('t110', length=4, delay_cost=1)
	S += t110 >= 61
	t110 += MAS[3]

	t14_t1 = S.Task('t14_t1', length=7, delay_cost=1)
	S += t14_t1 >= 61
	t14_t1 += MM[0]

	new_TZ_t3 = S.Task('new_TZ_t3', length=4, delay_cost=1)
	S += new_TZ_t3 >= 62
	new_TZ_t3 += MAS[2]

	t14_t3_in = S.Task('t14_t3_in', length=1, delay_cost=1)
	S += t14_t3_in >= 62
	t14_t3_in += MAS_in[3]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	S += t14_t3_mem0 >= 62
	t14_t3_mem0 += MAS_MEM[2]

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	S += t14_t3_mem1 >= 62
	t14_t3_mem1 += MAS_MEM[3]

	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	S += t111_in >= 63
	t111_in += MAS_in[1]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 63
	t111_mem0 += MAS_MEM[0]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 63
	t111_mem1 += MAS_MEM[5]

	t14_t3 = S.Task('t14_t3', length=4, delay_cost=1)
	S += t14_t3 >= 63
	t14_t3 += MAS[3]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 64
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 64
	new_TX_t0_mem0 += MAS_MEM[4]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 64
	new_TX_t0_mem1 += MAS_MEM[7]

	t111 = S.Task('t111', length=4, delay_cost=1)
	S += t111 >= 64
	t111 += MAS[1]

	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	S += t120_in >= 64
	t120_in += MAS_in[0]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 64
	t120_mem0 += MAS_MEM[6]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 64
	t120_mem1 += MAS_MEM[1]

	new_TX_t0 = S.Task('new_TX_t0', length=7, delay_cost=1)
	S += new_TX_t0 >= 65
	new_TX_t0 += MM[0]

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	S += new_TZ_t4_in >= 65
	new_TZ_t4_in += MM_in[1]

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	S += new_TZ_t4_mem0 >= 65
	new_TZ_t4_mem0 += MAS_MEM[4]

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	S += new_TZ_t4_mem1 >= 65
	new_TZ_t4_mem1 += MAS_MEM[5]

	t120 = S.Task('t120', length=4, delay_cost=1)
	S += t120 >= 65
	t120 += MAS[0]

	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	S += new_TZ0_in >= 66
	new_TZ0_in += MAS_in[1]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 66
	new_TZ0_mem0 += MM_MEM[2]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 66
	new_TZ0_mem1 += MM_MEM[3]

	new_TZ_t4 = S.Task('new_TZ_t4', length=7, delay_cost=1)
	S += new_TZ_t4 >= 66
	new_TZ_t4 += MM[1]

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	S += t14_t4_in >= 66
	t14_t4_in += MM_in[1]

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	S += t14_t4_mem0 >= 66
	t14_t4_mem0 += MAS_MEM[2]

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	S += t14_t4_mem1 >= 66
	t14_t4_mem1 += MAS_MEM[7]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 67
	new_TX_t1_in += MM_in[0]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 67
	new_TX_t1_mem0 += MAS_MEM[0]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 67
	new_TX_t1_mem1 += MAS_MEM[3]

	new_TZ0 = S.Task('new_TZ0', length=4, delay_cost=1)
	S += new_TZ0 >= 67
	new_TZ0 += MAS[1]

	new_TZ_t5_in = S.Task('new_TZ_t5_in', length=1, delay_cost=1)
	S += new_TZ_t5_in >= 67
	new_TZ_t5_in += MAS_in[0]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	S += new_TZ_t5_mem0 >= 67
	new_TZ_t5_mem0 += MM_MEM[2]

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	S += new_TZ_t5_mem1 >= 67
	new_TZ_t5_mem1 += MM_MEM[3]

	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	S += t121_in >= 67
	t121_in += MAS_in[1]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 67
	t121_mem0 += MAS_MEM[2]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 67
	t121_mem1 += MAS_MEM[1]

	t14_t4 = S.Task('t14_t4', length=7, delay_cost=1)
	S += t14_t4 >= 67
	t14_t4 += MM[1]

	t14_t5_in = S.Task('t14_t5_in', length=1, delay_cost=1)
	S += t14_t5_in >= 67
	t14_t5_in += MAS_in[2]

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	S += t14_t5_mem0 >= 67
	t14_t5_mem0 += MM_MEM[0]

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	S += t14_t5_mem1 >= 67
	t14_t5_mem1 += MM_MEM[1]

	new_TX_t1 = S.Task('new_TX_t1', length=7, delay_cost=1)
	S += new_TX_t1 >= 68
	new_TX_t1 += MM[0]

	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	S += new_TX_t3_in >= 68
	new_TX_t3_in += MAS_in[2]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 68
	new_TX_t3_mem0 += MAS_MEM[6]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 68
	new_TX_t3_mem1 += MAS_MEM[3]

	new_TZ_t5 = S.Task('new_TZ_t5', length=4, delay_cost=1)
	S += new_TZ_t5 >= 68
	new_TZ_t5 += MAS[0]

	t121 = S.Task('t121', length=4, delay_cost=1)
	S += t121 >= 68
	t121 += MAS[1]

	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	S += t13_t0_in >= 68
	t13_t0_in += MM_in[0]

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	S += t13_t0_mem0 >= 68
	t13_t0_mem0 += MAS_MEM[0]

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	S += t13_t0_mem1 >= 68
	t13_t0_mem1 += MAS_MEM[1]

	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	S += t140_in >= 68
	t140_in += MAS_in[3]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 68
	t140_mem0 += MM_MEM[0]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 68
	t140_mem1 += MM_MEM[1]

	t14_t5 = S.Task('t14_t5', length=4, delay_cost=1)
	S += t14_t5 >= 68
	t14_t5 += MAS[2]

	new_TX_t3 = S.Task('new_TX_t3', length=4, delay_cost=1)
	S += new_TX_t3 >= 69
	new_TX_t3 += MAS[2]

	t13_t0 = S.Task('t13_t0', length=7, delay_cost=1)
	S += t13_t0 >= 69
	t13_t0 += MM[0]

	t140 = S.Task('t140', length=4, delay_cost=1)
	S += t140 >= 69
	t140 += MAS[3]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 71
	new_TZ0_w += MAIN_MEM_w

	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	S += t13_t1_in >= 71
	t13_t1_in += MM_in[0]

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	S += t13_t1_mem0 >= 71
	t13_t1_mem0 += MAS_MEM[6]

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	S += t13_t1_mem1 >= 71
	t13_t1_mem1 += MAS_MEM[3]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 72
	new_TX_t4_in += MM_in[1]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 72
	new_TX_t4_mem0 += MAS_MEM[2]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 72
	new_TX_t4_mem1 += MAS_MEM[5]

	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	S += new_TZ1_in >= 72
	new_TZ1_in += MAS_in[3]

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 72
	new_TZ1_mem0 += MM_MEM[2]

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	S += new_TZ1_mem1 >= 72
	new_TZ1_mem1 += MAS_MEM[1]

	t13_t1 = S.Task('t13_t1', length=7, delay_cost=1)
	S += t13_t1 >= 72
	t13_t1 += MM[0]

	t13_t3_in = S.Task('t13_t3_in', length=1, delay_cost=1)
	S += t13_t3_in >= 72
	t13_t3_in += MAS_in[2]

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	S += t13_t3_mem0 >= 72
	t13_t3_mem0 += MAS_MEM[0]

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	S += t13_t3_mem1 >= 72
	t13_t3_mem1 += MAS_MEM[3]

	new_TX_t4 = S.Task('new_TX_t4', length=7, delay_cost=1)
	S += new_TX_t4 >= 73
	new_TX_t4 += MM[1]

	new_TZ1 = S.Task('new_TZ1', length=4, delay_cost=1)
	S += new_TZ1 >= 73
	new_TZ1 += MAS[3]

	t13_t3 = S.Task('t13_t3', length=4, delay_cost=1)
	S += t13_t3 >= 73
	t13_t3 += MAS[2]

	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	S += t141_in >= 73
	t141_in += MAS_in[0]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 73
	t141_mem0 += MM_MEM[2]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 73
	t141_mem1 += MAS_MEM[5]

	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	S += new_TX0_in >= 74
	new_TX0_in += MAS_in[0]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 74
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 74
	new_TX0_mem1 += MM_MEM[1]

	t141 = S.Task('t141', length=4, delay_cost=1)
	S += t141 >= 74
	t141 += MAS[0]

	new_TX0 = S.Task('new_TX0', length=4, delay_cost=1)
	S += new_TX0 >= 75
	new_TX0 += MAS[0]

	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	S += new_TX_t5_in >= 75
	new_TX_t5_in += MAS_in[3]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 75
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 75
	new_TX_t5_mem1 += MM_MEM[1]

	new_TX_t5 = S.Task('new_TX_t5', length=4, delay_cost=1)
	S += new_TX_t5 >= 76
	new_TX_t5 += MAS[3]

	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	S += t13_t4_in >= 76
	t13_t4_in += MM_in[0]

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	S += t13_t4_mem0 >= 76
	t13_t4_mem0 += MAS_MEM[4]

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	S += t13_t4_mem1 >= 76
	t13_t4_mem1 += MAS_MEM[5]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 77
	new_TZ1_w += MAIN_MEM_w

	t13_t4 = S.Task('t13_t4', length=7, delay_cost=1)
	S += t13_t4 >= 77
	t13_t4 += MM[0]

	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	S += t130_in >= 78
	t130_in += MAS_in[0]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 78
	t130_mem0 += MM_MEM[0]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 78
	t130_mem1 += MM_MEM[1]

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 79
	new_TX0_w += MAIN_MEM_w

	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	S += new_TX1_in >= 79
	new_TX1_in += MAS_in[2]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 79
	new_TX1_mem0 += MM_MEM[2]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 79
	new_TX1_mem1 += MAS_MEM[7]

	t130 = S.Task('t130', length=4, delay_cost=1)
	S += t130 >= 79
	t130 += MAS[0]

	t13_t5_in = S.Task('t13_t5_in', length=1, delay_cost=1)
	S += t13_t5_in >= 79
	t13_t5_in += MAS_in[3]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	S += t13_t5_mem0 >= 79
	t13_t5_mem0 += MM_MEM[0]

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	S += t13_t5_mem1 >= 79
	t13_t5_mem1 += MM_MEM[1]

	new_TX1 = S.Task('new_TX1', length=4, delay_cost=1)
	S += new_TX1 >= 80
	new_TX1 += MAS[2]

	t13_t5 = S.Task('t13_t5', length=4, delay_cost=1)
	S += t13_t5 >= 80
	t13_t5 += MAS[3]

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 82
	t150_in += MAS_in[0]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 82
	t150_mem0 += MAS_MEM[0]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 82
	t150_mem1 += MAS_MEM[7]

	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	S += t131_in >= 83
	t131_in += MAS_in[0]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 83
	t131_mem0 += MM_MEM[0]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 83
	t131_mem1 += MAS_MEM[7]

	t150 = S.Task('t150', length=4, delay_cost=1)
	S += t150 >= 83
	t150 += MAS[0]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 84
	new_TX1_w += MAIN_MEM_w

	t131 = S.Task('t131', length=4, delay_cost=1)
	S += t131 >= 84
	t131 += MAS[0]


	# new tasks
	t151 = S.Task('t151', length=4, delay_cost=1)
	t151 += alt(MAS)
	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	t151_in += alt(MAS_in)
	S += t151_in*MAS_in[0]<=t151*MAS[0]

	S += t151_in*MAS_in[1]<=t151*MAS[1]

	S += t151_in*MAS_in[2]<=t151*MAS[2]

	S += t151_in*MAS_in[3]<=t151*MAS[3]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[0]
	S += 87 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += MAS_MEM[1]
	S += 77 < t151_mem1
	S += t151_mem1 <= t151

	new_TY0 = S.Task('new_TY0', length=4, delay_cost=1)
	new_TY0 += alt(MAS)
	new_TY0_in = S.Task('new_TY0_in', length=1, delay_cost=1)
	new_TY0_in += alt(MAS_in)
	S += new_TY0_in*MAS_in[0]<=new_TY0*MAS[0]

	S += new_TY0_in*MAS_in[1]<=new_TY0*MAS[1]

	S += new_TY0_in*MAS_in[2]<=new_TY0*MAS[2]

	S += new_TY0_in*MAS_in[3]<=new_TY0*MAS[3]

	S += 55<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += MAIN_MEM_r[0]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += MAS_MEM[1]
	S += 86 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=4, delay_cost=1)
	new_TY1 += alt(MAS)
	new_TY1_in = S.Task('new_TY1_in', length=1, delay_cost=1)
	new_TY1_in += alt(MAS_in)
	S += new_TY1_in*MAS_in[0]<=new_TY1*MAS[0]

	S += new_TY1_in*MAS_in[1]<=new_TY1*MAS[1]

	S += new_TY1_in*MAS_in[2]<=new_TY1*MAS[2]

	S += new_TY1_in*MAS_in[3]<=new_TY1*MAS[3]

	S += 61<new_TY1

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
	S += (t151*MAS[3])-1 < new_TY1_mem1*MAS_MEM[7]
	S += new_TY1_mem1 <= new_TY1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM2_stage4MAS4/EP2_ADD_w_EVAL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

