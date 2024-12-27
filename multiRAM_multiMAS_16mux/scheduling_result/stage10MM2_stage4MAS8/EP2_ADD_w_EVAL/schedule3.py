from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 221
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
	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 0
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 0
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 0
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t0 = S.Task('t0_t0', length=10, delay_cost=1)
	S += t0_t0 >= 1
	t0_t0 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 1
	t0_t1_in += MM_in[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 1
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 1
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=10, delay_cost=1)
	S += t0_t1 >= 2
	t0_t1 += MM[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 2
	t2_t1_in += MM_in[1]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 2
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 2
	t2_t1_mem1 += MAIN_MEM_r[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 3
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 3
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 3
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=10, delay_cost=1)
	S += t2_t1 >= 3
	t2_t1 += MM[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 4
	t0_t2_in += MAS_in[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 4
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 4
	t0_t2_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=10, delay_cost=1)
	S += t2_t0 >= 4
	t2_t0 += MM[0]

	t0_t2 = S.Task('t0_t2', length=4, delay_cost=1)
	S += t0_t2 >= 5
	t0_t2 += MAS[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 5
	t0_t3_in += MAS_in[5]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 5
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 5
	t0_t3_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=4, delay_cost=1)
	S += t0_t3 >= 6
	t0_t3 += MAS[5]

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
	t2_t2_in += MAS_in[6]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 7
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 7
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=4, delay_cost=1)
	S += t2_t3 >= 7
	t2_t3 += MAS[2]

	t16_t2_in = S.Task('t16_t2_in', length=1, delay_cost=1)
	S += t16_t2_in >= 8
	t16_t2_in += MAS_in[0]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 8
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 8
	t16_t2_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=4, delay_cost=1)
	S += t2_t2 >= 8
	t2_t2 += MAS[6]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 9
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 9
	t0_t4_mem0 += MAS_MEM[2]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 9
	t0_t4_mem1 += MAS_MEM[11]

	t16_t2 = S.Task('t16_t2', length=4, delay_cost=1)
	S += t16_t2 >= 9
	t16_t2 += MAS[0]

	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	S += t17_t2_in >= 9
	t17_t2_in += MAS_in[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 9
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 9
	t17_t2_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=10, delay_cost=1)
	S += t0_t4 >= 10
	t0_t4 += MM[0]

	t17_t2 = S.Task('t17_t2', length=4, delay_cost=1)
	S += t17_t2 >= 10
	t17_t2 += MAS[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 10
	t7_t2_in += MAS_in[6]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 10
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 10
	t7_t2_mem1 += MAIN_MEM_r[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 11
	t00_in += MAS_in[3]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 11
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 11
	t00_mem1 += MM_MEM[3]

	t14_t2_in = S.Task('t14_t2_in', length=1, delay_cost=1)
	S += t14_t2_in >= 11
	t14_t2_in += MAS_in[1]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 11
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 11
	t14_t2_mem1 += MAIN_MEM_r[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 11
	t2_t4_in += MM_in[1]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 11
	t2_t4_mem0 += MAS_MEM[12]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 11
	t2_t4_mem1 += MAS_MEM[5]

	t7_t2 = S.Task('t7_t2', length=4, delay_cost=1)
	S += t7_t2 >= 11
	t7_t2 += MAS[6]

	new_TZ_t2_in = S.Task('new_TZ_t2_in', length=1, delay_cost=1)
	S += new_TZ_t2_in >= 12
	new_TZ_t2_in += MAS_in[1]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 12
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 12
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t00 = S.Task('t00', length=4, delay_cost=1)
	S += t00 >= 12
	t00 += MAS[3]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 12
	t0_t5_in += MAS_in[5]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 12
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 12
	t0_t5_mem1 += MM_MEM[3]

	t14_t2 = S.Task('t14_t2', length=4, delay_cost=1)
	S += t14_t2 >= 12
	t14_t2 += MAS[1]

	t2_t4 = S.Task('t2_t4', length=10, delay_cost=1)
	S += t2_t4 >= 12
	t2_t4 += MM[1]

	new_TZ_t2 = S.Task('new_TZ_t2', length=4, delay_cost=1)
	S += new_TZ_t2 >= 13
	new_TZ_t2 += MAS[1]

	t0_t5 = S.Task('t0_t5', length=4, delay_cost=1)
	S += t0_t5 >= 13
	t0_t5 += MAS[5]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 13
	t20_in += MAS_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 13
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 13
	t20_mem1 += MM_MEM[3]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 13
	t9_t2_in += MAS_in[5]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 13
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 13
	t9_t2_mem1 += MAIN_MEM_r[1]

	t20 = S.Task('t20', length=4, delay_cost=1)
	S += t20 >= 14
	t20 += MAS[0]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 14
	t2_t5_in += MAS_in[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 14
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 14
	t2_t5_mem1 += MM_MEM[3]

	t9_t2 = S.Task('t9_t2', length=4, delay_cost=1)
	S += t9_t2 >= 14
	t9_t2 += MAS[5]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 15
	t10_in += MAS_in[3]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 15
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 15
	t10_mem1 += MAS_MEM[7]

	t2_t5 = S.Task('t2_t5', length=4, delay_cost=1)
	S += t2_t5 >= 15
	t2_t5 += MAS[0]

	t10 = S.Task('t10', length=4, delay_cost=1)
	S += t10 >= 16
	t10 += MAS[3]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 17
	t30_in += MAS_in[3]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 17
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 17
	t30_mem1 += MAS_MEM[1]

	t30 = S.Task('t30', length=4, delay_cost=1)
	S += t30 >= 18
	t30 += MAS[3]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 19
	c200_in += MM_in[1]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 19
	c200_mem0 += MAS_MEM[6]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 19
	c200_mem1 += MAIN_MEM_r[1]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 19
	t01_in += MAS_in[4]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 19
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 19
	t01_mem1 += MAS_MEM[11]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 19
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 19
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 19
	t17_t0_mem1 += MAS_MEM[7]

	c200 = S.Task('c200', length=10, delay_cost=1)
	S += c200 >= 20
	c200 += MM[1]

	t01 = S.Task('t01', length=4, delay_cost=1)
	S += t01 >= 20
	t01 += MAS[4]

	t17_t0 = S.Task('t17_t0', length=10, delay_cost=1)
	S += t17_t0 >= 20
	t17_t0 += MM[0]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 21
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 21
	c010_mem0 += MAS_MEM[6]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 21
	c010_mem1 += MAIN_MEM_r[1]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 21
	t16_t0_in += MM_in[1]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 21
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 21
	t16_t0_mem1 += MAS_MEM[7]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 21
	t21_in += MAS_in[2]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 21
	t21_mem0 += MM_MEM[2]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 21
	t21_mem1 += MAS_MEM[1]

	c010 = S.Task('c010', length=10, delay_cost=1)
	S += c010 >= 22
	c010 += MM[0]

	t16_t0 = S.Task('t16_t0', length=10, delay_cost=1)
	S += t16_t0 >= 22
	t16_t0 += MM[1]

	t21 = S.Task('t21', length=4, delay_cost=1)
	S += t21 >= 22
	t21 += MAS[2]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 23
	t11_in += MAS_in[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 23
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 23
	t11_mem1 += MAS_MEM[9]

	t11 = S.Task('t11', length=4, delay_cost=1)
	S += t11 >= 24
	t11 += MAS[1]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 25
	t31_in += MAS_in[7]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 25
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 25
	t31_mem1 += MAS_MEM[5]

	t31 = S.Task('t31', length=4, delay_cost=1)
	S += t31 >= 26
	t31 += MAS[7]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 27
	c201_in += MM_in[1]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 27
	c201_mem0 += MAS_MEM[2]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 27
	c201_mem1 += MAIN_MEM_r[1]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 27
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 27
	t4_t3_mem0 += MAS_MEM[6]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 27
	t4_t3_mem1 += MAS_MEM[3]

	c201 = S.Task('c201', length=10, delay_cost=1)
	S += c201 >= 28
	c201 += MM[1]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 28
	t4_t1_in += MAS_in[1]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 28
	t4_t1_mem0 += MAS_MEM[6]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 28
	t4_t1_mem1 += MAS_MEM[3]

	t4_t3 = S.Task('t4_t3', length=10, delay_cost=1)
	S += t4_t3 >= 28
	t4_t3 += MM[0]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 29
	c011_in += MM_in[1]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 29
	c011_mem0 += MAS_MEM[14]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 29
	c011_mem1 += MAIN_MEM_r[1]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 29
	t16_t1_in += MM_in[0]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 29
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 29
	t16_t1_mem1 += MAS_MEM[15]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 29
	t4_t0_in += MAS_in[0]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 29
	t4_t0_mem0 += MAS_MEM[6]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 29
	t4_t0_mem1 += MAS_MEM[3]

	t4_t1 = S.Task('t4_t1', length=4, delay_cost=1)
	S += t4_t1 >= 29
	t4_t1 += MAS[1]

	c011 = S.Task('c011', length=10, delay_cost=1)
	S += c011 >= 30
	c011 += MM[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 30
	c200_w += MAIN_MEM_w

	t16_t1 = S.Task('t16_t1', length=10, delay_cost=1)
	S += t16_t1 >= 30
	t16_t1 += MM[0]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 30
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 30
	t17_t1_mem0 += MAIN_MEM_r[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 30
	t17_t1_mem1 += MAS_MEM[3]

	t4_t0 = S.Task('t4_t0', length=4, delay_cost=1)
	S += t4_t0 >= 30
	t4_t0 += MAS[0]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 30
	t5_t3_in += MM_in[1]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 30
	t5_t3_mem0 += MAS_MEM[6]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 30
	t5_t3_mem1 += MAS_MEM[15]

	t17_t1 = S.Task('t17_t1', length=10, delay_cost=1)
	S += t17_t1 >= 31
	t17_t1 += MM[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 31
	t5_t1_in += MAS_in[2]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 31
	t5_t1_mem0 += MAS_MEM[6]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 31
	t5_t1_mem1 += MAS_MEM[15]

	t5_t3 = S.Task('t5_t3', length=10, delay_cost=1)
	S += t5_t3 >= 31
	t5_t3 += MM[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 32
	c010_w += MAIN_MEM_w

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 32
	t5_t0_in += MAS_in[5]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 32
	t5_t0_mem0 += MAS_MEM[6]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 32
	t5_t0_mem1 += MAS_MEM[15]

	t5_t1 = S.Task('t5_t1', length=4, delay_cost=1)
	S += t5_t1 >= 32
	t5_t1 += MAS[2]

	t16_t3_in = S.Task('t16_t3_in', length=1, delay_cost=1)
	S += t16_t3_in >= 33
	t16_t3_in += MAS_in[2]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 33
	t16_t3_mem0 += MAS_MEM[6]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 33
	t16_t3_mem1 += MAS_MEM[15]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 33
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 33
	t4_t2_mem0 += MAS_MEM[0]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 33
	t4_t2_mem1 += MAS_MEM[3]

	t5_t0 = S.Task('t5_t0', length=4, delay_cost=1)
	S += t5_t0 >= 33
	t5_t0 += MAS[5]

	t16_t3 = S.Task('t16_t3', length=4, delay_cost=1)
	S += t16_t3 >= 34
	t16_t3 += MAS[2]

	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	S += t17_t3_in >= 34
	t17_t3_in += MAS_in[0]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 34
	t17_t3_mem0 += MAS_MEM[6]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 34
	t17_t3_mem1 += MAS_MEM[3]

	t4_t2 = S.Task('t4_t2', length=10, delay_cost=1)
	S += t4_t2 >= 34
	t4_t2 += MM[0]

	t13_t2_in = S.Task('t13_t2_in', length=1, delay_cost=1)
	S += t13_t2_in >= 35
	t13_t2_in += MAS_in[1]

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 35
	t13_t2_mem0 += MAS_MEM[6]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 35
	t13_t2_mem1 += MAS_MEM[3]

	t17_t3 = S.Task('t17_t3', length=4, delay_cost=1)
	S += t17_t3 >= 35
	t17_t3 += MAS[0]

	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	S += new_TX_t2_in >= 36
	new_TX_t2_in += MAS_in[1]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 36
	new_TX_t2_mem0 += MAS_MEM[6]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 36
	new_TX_t2_mem1 += MAS_MEM[15]

	t13_t2 = S.Task('t13_t2', length=4, delay_cost=1)
	S += t13_t2 >= 36
	t13_t2 += MAS[1]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 36
	t5_t2_in += MM_in[1]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 36
	t5_t2_mem0 += MAS_MEM[10]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 36
	t5_t2_mem1 += MAS_MEM[5]

	new_TX_t2 = S.Task('new_TX_t2', length=4, delay_cost=1)
	S += new_TX_t2 >= 37
	new_TX_t2 += MAS[1]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 37
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 37
	t16_t4_mem0 += MAS_MEM[0]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 37
	t16_t4_mem1 += MAS_MEM[5]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 37
	t41_in += MAS_in[3]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 37
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 37
	t41_mem1 += MM_MEM[1]

	t5_t2 = S.Task('t5_t2', length=10, delay_cost=1)
	S += t5_t2 >= 37
	t5_t2 += MM[1]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 37
	t6_t2_in += MAS_in[0]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 37
	t6_t2_mem0 += MAS_MEM[6]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 37
	t6_t2_mem1 += MAS_MEM[15]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 38
	c201_w += MAIN_MEM_w

	t16_t4 = S.Task('t16_t4', length=10, delay_cost=1)
	S += t16_t4 >= 38
	t16_t4 += MM[0]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 38
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 38
	t17_t4_mem0 += MAS_MEM[0]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 38
	t17_t4_mem1 += MAS_MEM[1]

	t41 = S.Task('t41', length=4, delay_cost=1)
	S += t41 >= 38
	t41 += MAS[3]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 38
	t4_t5_in += MAS_in[3]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 38
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 38
	t4_t5_mem1 += MM_MEM[1]

	t6_t2 = S.Task('t6_t2', length=4, delay_cost=1)
	S += t6_t2 >= 38
	t6_t2 += MAS[0]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 39
	t160_in += MAS_in[6]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 39
	t160_mem0 += MM_MEM[2]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 39
	t160_mem1 += MM_MEM[1]

	t17_t4 = S.Task('t17_t4', length=10, delay_cost=1)
	S += t17_t4 >= 39
	t17_t4 += MM[0]

	t4_t5 = S.Task('t4_t5', length=4, delay_cost=1)
	S += t4_t5 >= 39
	t4_t5 += MAS[3]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 40
	c011_w += MAIN_MEM_w

	t160 = S.Task('t160', length=4, delay_cost=1)
	S += t160 >= 40
	t160 += MAS[6]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 40
	t170_in += MAS_in[4]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 40
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 40
	t170_mem1 += MM_MEM[1]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 40
	t51_in += MAS_in[2]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 40
	t51_mem0 += MM_MEM[2]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 40
	t51_mem1 += MM_MEM[3]

	t170 = S.Task('t170', length=4, delay_cost=1)
	S += t170 >= 41
	t170 += MAS[4]

	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	S += t17_t5_in >= 41
	t17_t5_in += MAS_in[7]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 41
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 41
	t17_t5_mem1 += MM_MEM[1]

	t51 = S.Task('t51', length=4, delay_cost=1)
	S += t51 >= 41
	t51 += MAS[2]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 41
	t5_t5_in += MAS_in[6]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 41
	t5_t5_mem0 += MM_MEM[2]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 41
	t5_t5_mem1 += MM_MEM[3]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 41
	t7_t1_in += MM_in[1]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 41
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 41
	t7_t1_mem1 += MAS_MEM[7]

	t16_t5_in = S.Task('t16_t5_in', length=1, delay_cost=1)
	S += t16_t5_in >= 42
	t16_t5_in += MAS_in[5]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 42
	t16_t5_mem0 += MM_MEM[2]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 42
	t16_t5_mem1 += MM_MEM[1]

	t17_t5 = S.Task('t17_t5', length=4, delay_cost=1)
	S += t17_t5 >= 42
	t17_t5 += MAS[7]

	t5_t5 = S.Task('t5_t5', length=4, delay_cost=1)
	S += t5_t5 >= 42
	t5_t5 += MAS[6]

	t7_t1 = S.Task('t7_t1', length=10, delay_cost=1)
	S += t7_t1 >= 42
	t7_t1 += MM[1]

	t16_t5 = S.Task('t16_t5', length=4, delay_cost=1)
	S += t16_t5 >= 43
	t16_t5 += MAS[5]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 43
	t40_in += MAS_in[4]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 43
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 43
	t40_mem1 += MAS_MEM[7]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 44
	c000_in += MAS_in[4]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 44
	c000_mem0 += MAS_MEM[12]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 44
	c000_mem1 += MAS_MEM[9]

	t40 = S.Task('t40', length=4, delay_cost=1)
	S += t40 >= 44
	t40 += MAS[4]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 44
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 44
	t6_t1_mem0 += MAS_MEM[14]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 44
	t6_t1_mem1 += MAS_MEM[5]

	c000 = S.Task('c000', length=4, delay_cost=1)
	S += c000 >= 45
	c000 += MAS[4]

	t6_t1 = S.Task('t6_t1', length=10, delay_cost=1)
	S += t6_t1 >= 45
	t6_t1 += MM[0]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 45
	t9_t1_in += MM_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 45
	t9_t1_mem0 += MAIN_MEM_r[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 45
	t9_t1_mem1 += MAS_MEM[5]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 46
	t50_in += MAS_in[4]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 46
	t50_mem0 += MM_MEM[2]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 46
	t50_mem1 += MAS_MEM[13]

	t9_t1 = S.Task('t9_t1', length=10, delay_cost=1)
	S += t9_t1 >= 46
	t9_t1 += MM[0]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 47
	t161_in += MAS_in[5]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 47
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 47
	t161_mem1 += MAS_MEM[11]

	t50 = S.Task('t50', length=4, delay_cost=1)
	S += t50 >= 47
	t50 += MAS[4]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 47
	t7_t0_in += MM_in[1]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 47
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 47
	t7_t0_mem1 += MAS_MEM[9]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 47
	t7_t3_in += MAS_in[6]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 47
	t7_t3_mem0 += MAS_MEM[8]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 47
	t7_t3_mem1 += MAS_MEM[7]

	t161 = S.Task('t161', length=4, delay_cost=1)
	S += t161 >= 48
	t161 += MAS[5]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 48
	t171_in += MAS_in[2]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 48
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 48
	t171_mem1 += MAS_MEM[15]

	t7_t0 = S.Task('t7_t0', length=10, delay_cost=1)
	S += t7_t0 >= 48
	t7_t0 += MM[1]

	t7_t3 = S.Task('t7_t3', length=4, delay_cost=1)
	S += t7_t3 >= 48
	t7_t3 += MAS[6]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 49
	c000_w += MAIN_MEM_w

	t171 = S.Task('t171', length=4, delay_cost=1)
	S += t171 >= 49
	t171 += MAS[2]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 50
	t6_t3_in += MAS_in[1]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 50
	t6_t3_mem0 += MAS_MEM[8]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 50
	t6_t3_mem1 += MAS_MEM[5]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 50
	t9_t0_in += MM_in[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 50
	t9_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 50
	t9_t0_mem1 += MAS_MEM[9]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 51
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 51
	t6_t0_mem0 += MAS_MEM[6]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 51
	t6_t0_mem1 += MAS_MEM[9]

	t6_t3 = S.Task('t6_t3', length=4, delay_cost=1)
	S += t6_t3 >= 51
	t6_t3 += MAS[1]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 51
	t7_t4_in += MM_in[1]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 51
	t7_t4_mem0 += MAS_MEM[12]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 51
	t7_t4_mem1 += MAS_MEM[13]

	t9_t0 = S.Task('t9_t0', length=10, delay_cost=1)
	S += t9_t0 >= 51
	t9_t0 += MM[0]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 51
	t9_t3_in += MAS_in[0]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 51
	t9_t3_mem0 += MAS_MEM[8]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 51
	t9_t3_mem1 += MAS_MEM[5]

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 52
	c001_in += MAS_in[0]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 52
	c001_mem0 += MAS_MEM[10]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 52
	c001_mem1 += MAS_MEM[5]

	t6_t0 = S.Task('t6_t0', length=10, delay_cost=1)
	S += t6_t0 >= 52
	t6_t0 += MM[0]

	t7_t4 = S.Task('t7_t4', length=10, delay_cost=1)
	S += t7_t4 >= 52
	t7_t4 += MM[1]

	t9_t3 = S.Task('t9_t3', length=4, delay_cost=1)
	S += t9_t3 >= 52
	t9_t3 += MAS[0]

	c001 = S.Task('c001', length=4, delay_cost=1)
	S += c001 >= 53
	c001 += MAS[0]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 54
	t6_t4_in += MM_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 54
	t6_t4_mem0 += MAS_MEM[0]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 54
	t6_t4_mem1 += MAS_MEM[3]

	t6_t4 = S.Task('t6_t4', length=10, delay_cost=1)
	S += t6_t4 >= 55
	t6_t4 += MM[0]

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	S += t9_t4_in >= 55
	t9_t4_in += MM_in[1]

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	S += t9_t4_mem0 >= 55
	t9_t4_mem0 += MAS_MEM[10]

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	S += t9_t4_mem1 >= 55
	t9_t4_mem1 += MAS_MEM[1]

	t9_t4 = S.Task('t9_t4', length=10, delay_cost=1)
	S += t9_t4 >= 56
	t9_t4 += MM[1]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 57
	c001_w += MAIN_MEM_w

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 57
	t7_t5_in += MAS_in[3]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 57
	t7_t5_mem0 += MM_MEM[2]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 57
	t7_t5_mem1 += MM_MEM[3]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 58
	t70_in += MAS_in[1]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 58
	t70_mem0 += MM_MEM[2]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 58
	t70_mem1 += MM_MEM[3]

	t7_t5 = S.Task('t7_t5', length=4, delay_cost=1)
	S += t7_t5 >= 58
	t7_t5 += MAS[3]

	t70 = S.Task('t70', length=4, delay_cost=1)
	S += t70 >= 59
	t70 += MAS[1]

	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	S += t9_t5_in >= 60
	t9_t5_in += MAS_in[3]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 60
	t9_t5_mem0 += MM_MEM[0]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 60
	t9_t5_mem1 += MM_MEM[1]

	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	S += t6_t5_in >= 61
	t6_t5_in += MAS_in[7]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 61
	t6_t5_mem0 += MM_MEM[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 61
	t6_t5_mem1 += MM_MEM[1]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 61
	t71_in += MAS_in[1]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 61
	t71_mem0 += MM_MEM[2]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 61
	t71_mem1 += MAS_MEM[7]

	t9_t5 = S.Task('t9_t5', length=4, delay_cost=1)
	S += t9_t5 >= 61
	t9_t5 += MAS[3]

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 62
	t60_in += MAS_in[6]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 62
	t60_mem0 += MM_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 62
	t60_mem1 += MM_MEM[1]

	t6_t5 = S.Task('t6_t5', length=4, delay_cost=1)
	S += t6_t5 >= 62
	t6_t5 += MAS[7]

	t71 = S.Task('t71', length=4, delay_cost=1)
	S += t71 >= 62
	t71 += MAS[1]

	t60 = S.Task('t60', length=4, delay_cost=1)
	S += t60 >= 63
	t60 += MAS[6]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 63
	t90_in += MAS_in[3]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 63
	t90_mem0 += MM_MEM[0]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 63
	t90_mem1 += MM_MEM[1]

	t90 = S.Task('t90', length=4, delay_cost=1)
	S += t90 >= 64
	t90 += MAS[3]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 65
	t61_in += MAS_in[7]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 65
	t61_mem0 += MM_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 65
	t61_mem1 += MAS_MEM[15]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 65
	t91_in += MAS_in[6]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 65
	t91_mem0 += MM_MEM[2]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 65
	t91_mem1 += MAS_MEM[7]

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	S += t14_t0_in >= 66
	t14_t0_in += MM_in[0]

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	S += t14_t0_mem0 >= 66
	t14_t0_mem0 += MAIN_MEM_r[0]

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	S += t14_t0_mem1 >= 66
	t14_t0_mem1 += MAS_MEM[13]

	t61 = S.Task('t61', length=4, delay_cost=1)
	S += t61 >= 66
	t61 += MAS[7]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 66
	t80_in += MAS_in[5]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 66
	t80_mem0 += MAS_MEM[12]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 66
	t80_mem1 += MAS_MEM[3]

	t91 = S.Task('t91', length=4, delay_cost=1)
	S += t91 >= 66
	t91 += MAS[6]

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	S += new_TZ_t0_in >= 67
	new_TZ_t0_in += MM_in[1]

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_mem0 >= 67
	new_TZ_t0_mem0 += MAIN_MEM_r[0]

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_mem1 >= 67
	new_TZ_t0_mem1 += MAS_MEM[13]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 67
	t100_in += MAS_in[3]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 67
	t100_mem0 += MAS_MEM[6]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 67
	t100_mem1 += MAS_MEM[7]

	t14_t0 = S.Task('t14_t0', length=10, delay_cost=1)
	S += t14_t0 >= 67
	t14_t0 += MM[0]

	t80 = S.Task('t80', length=4, delay_cost=1)
	S += t80 >= 67
	t80 += MAS[5]

	new_TZ_t0 = S.Task('new_TZ_t0', length=10, delay_cost=1)
	S += new_TZ_t0 >= 68
	new_TZ_t0 += MM[1]

	t100 = S.Task('t100', length=4, delay_cost=1)
	S += t100 >= 68
	t100 += MAS[3]

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	S += new_TZ_t1_in >= 69
	new_TZ_t1_in += MM_in[0]

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_mem0 >= 69
	new_TZ_t1_mem0 += MAIN_MEM_r[0]

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_mem1 >= 69
	new_TZ_t1_mem1 += MAS_MEM[15]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 69
	t101_in += MAS_in[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 69
	t101_mem0 += MAS_MEM[12]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 69
	t101_mem1 += MAS_MEM[13]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 69
	t81_in += MAS_in[3]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 69
	t81_mem0 += MAS_MEM[14]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 69
	t81_mem1 += MAS_MEM[3]

	new_TZ_t1 = S.Task('new_TZ_t1', length=10, delay_cost=1)
	S += new_TZ_t1 >= 70
	new_TZ_t1 += MM[0]

	new_TZ_t3_in = S.Task('new_TZ_t3_in', length=1, delay_cost=1)
	S += new_TZ_t3_in >= 70
	new_TZ_t3_in += MAS_in[2]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	S += new_TZ_t3_mem0 >= 70
	new_TZ_t3_mem0 += MAS_MEM[12]

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	S += new_TZ_t3_mem1 >= 70
	new_TZ_t3_mem1 += MAS_MEM[15]

	t101 = S.Task('t101', length=4, delay_cost=1)
	S += t101 >= 70
	t101 += MAS[1]

	t81 = S.Task('t81', length=4, delay_cost=1)
	S += t81 >= 70
	t81 += MAS[3]

	new_TZ_t3 = S.Task('new_TZ_t3', length=4, delay_cost=1)
	S += new_TZ_t3 >= 71
	new_TZ_t3 += MAS[2]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 71
	t110_in += MAS_in[2]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 71
	t110_mem0 += MAS_MEM[10]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 71
	t110_mem1 += MAS_MEM[7]

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	S += t14_t1_in >= 71
	t14_t1_in += MM_in[0]

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	S += t14_t1_mem0 >= 71
	t14_t1_mem0 += MAIN_MEM_r[0]

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	S += t14_t1_mem1 >= 71
	t14_t1_mem1 += MAS_MEM[15]

	t110 = S.Task('t110', length=4, delay_cost=1)
	S += t110 >= 72
	t110 += MAS[2]

	t14_t1 = S.Task('t14_t1', length=10, delay_cost=1)
	S += t14_t1 >= 72
	t14_t1 += MM[0]

	t14_t3_in = S.Task('t14_t3_in', length=1, delay_cost=1)
	S += t14_t3_in >= 72
	t14_t3_in += MAS_in[1]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	S += t14_t3_mem0 >= 72
	t14_t3_mem0 += MAS_MEM[12]

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	S += t14_t3_mem1 >= 72
	t14_t3_mem1 += MAS_MEM[15]

	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	S += t111_in >= 73
	t111_in += MAS_in[2]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 73
	t111_mem0 += MAS_MEM[6]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 73
	t111_mem1 += MAS_MEM[3]

	t14_t3 = S.Task('t14_t3', length=4, delay_cost=1)
	S += t14_t3 >= 73
	t14_t3 += MAS[1]

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	S += new_TZ_t4_in >= 74
	new_TZ_t4_in += MM_in[0]

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	S += new_TZ_t4_mem0 >= 74
	new_TZ_t4_mem0 += MAS_MEM[2]

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	S += new_TZ_t4_mem1 >= 74
	new_TZ_t4_mem1 += MAS_MEM[5]

	t111 = S.Task('t111', length=4, delay_cost=1)
	S += t111 >= 74
	t111 += MAS[2]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 75
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 75
	new_TX_t0_mem0 += MAS_MEM[6]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 75
	new_TX_t0_mem1 += MAS_MEM[5]

	new_TZ_t4 = S.Task('new_TZ_t4', length=10, delay_cost=1)
	S += new_TZ_t4 >= 75
	new_TZ_t4 += MM[0]

	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	S += t120_in >= 75
	t120_in += MAS_in[0]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 75
	t120_mem0 += MAS_MEM[4]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 75
	t120_mem1 += MAS_MEM[7]

	new_TX_t0 = S.Task('new_TX_t0', length=10, delay_cost=1)
	S += new_TX_t0 >= 76
	new_TX_t0 += MM[0]

	t120 = S.Task('t120', length=4, delay_cost=1)
	S += t120 >= 76
	t120 += MAS[0]

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	S += t14_t4_in >= 76
	t14_t4_in += MM_in[1]

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	S += t14_t4_mem0 >= 76
	t14_t4_mem0 += MAS_MEM[2]

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	S += t14_t4_mem1 >= 76
	t14_t4_mem1 += MAS_MEM[3]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 77
	new_TX_t1_in += MM_in[0]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 77
	new_TX_t1_mem0 += MAS_MEM[14]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 77
	new_TX_t1_mem1 += MAS_MEM[5]

	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	S += t121_in >= 77
	t121_in += MAS_in[3]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 77
	t121_mem0 += MAS_MEM[4]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 77
	t121_mem1 += MAS_MEM[13]

	t14_t4 = S.Task('t14_t4', length=10, delay_cost=1)
	S += t14_t4 >= 77
	t14_t4 += MM[1]

	new_TX_t1 = S.Task('new_TX_t1', length=10, delay_cost=1)
	S += new_TX_t1 >= 78
	new_TX_t1 += MM[0]

	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	S += new_TX_t3_in >= 78
	new_TX_t3_in += MAS_in[7]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 78
	new_TX_t3_mem0 += MAS_MEM[4]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 78
	new_TX_t3_mem1 += MAS_MEM[5]

	t121 = S.Task('t121', length=4, delay_cost=1)
	S += t121 >= 78
	t121 += MAS[3]

	new_TX_t3 = S.Task('new_TX_t3', length=4, delay_cost=1)
	S += new_TX_t3 >= 79
	new_TX_t3 += MAS[7]

	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	S += new_TZ0_in >= 79
	new_TZ0_in += MAS_in[2]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 79
	new_TZ0_mem0 += MM_MEM[2]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 79
	new_TZ0_mem1 += MM_MEM[1]

	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	S += t13_t0_in >= 79
	t13_t0_in += MM_in[1]

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	S += t13_t0_mem0 >= 79
	t13_t0_mem0 += MAS_MEM[6]

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	S += t13_t0_mem1 >= 79
	t13_t0_mem1 += MAS_MEM[1]

	new_TZ0 = S.Task('new_TZ0', length=4, delay_cost=1)
	S += new_TZ0 >= 80
	new_TZ0 += MAS[2]

	new_TZ_t5_in = S.Task('new_TZ_t5_in', length=1, delay_cost=1)
	S += new_TZ_t5_in >= 80
	new_TZ_t5_in += MAS_in[2]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	S += new_TZ_t5_mem0 >= 80
	new_TZ_t5_mem0 += MM_MEM[2]

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	S += new_TZ_t5_mem1 >= 80
	new_TZ_t5_mem1 += MM_MEM[1]

	t13_t0 = S.Task('t13_t0', length=10, delay_cost=1)
	S += t13_t0 >= 80
	t13_t0 += MM[1]

	new_TZ_t5 = S.Task('new_TZ_t5', length=4, delay_cost=1)
	S += new_TZ_t5 >= 81
	new_TZ_t5 += MAS[2]

	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	S += t13_t1_in >= 81
	t13_t1_in += MM_in[0]

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	S += t13_t1_mem0 >= 81
	t13_t1_mem0 += MAS_MEM[2]

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	S += t13_t1_mem1 >= 81
	t13_t1_mem1 += MAS_MEM[7]

	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	S += t140_in >= 81
	t140_in += MAS_in[4]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 81
	t140_mem0 += MM_MEM[0]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 81
	t140_mem1 += MM_MEM[1]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 82
	new_TX_t4_in += MM_in[0]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 82
	new_TX_t4_mem0 += MAS_MEM[2]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 82
	new_TX_t4_mem1 += MAS_MEM[15]

	t13_t1 = S.Task('t13_t1', length=10, delay_cost=1)
	S += t13_t1 >= 82
	t13_t1 += MM[0]

	t13_t3_in = S.Task('t13_t3_in', length=1, delay_cost=1)
	S += t13_t3_in >= 82
	t13_t3_in += MAS_in[3]

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	S += t13_t3_mem0 >= 82
	t13_t3_mem0 += MAS_MEM[0]

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	S += t13_t3_mem1 >= 82
	t13_t3_mem1 += MAS_MEM[7]

	t140 = S.Task('t140', length=4, delay_cost=1)
	S += t140 >= 82
	t140 += MAS[4]

	t14_t5_in = S.Task('t14_t5_in', length=1, delay_cost=1)
	S += t14_t5_in >= 82
	t14_t5_in += MAS_in[2]

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	S += t14_t5_mem0 >= 82
	t14_t5_mem0 += MM_MEM[0]

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	S += t14_t5_mem1 >= 82
	t14_t5_mem1 += MM_MEM[1]

	new_TX_t4 = S.Task('new_TX_t4', length=10, delay_cost=1)
	S += new_TX_t4 >= 83
	new_TX_t4 += MM[0]

	t13_t3 = S.Task('t13_t3', length=4, delay_cost=1)
	S += t13_t3 >= 83
	t13_t3 += MAS[3]

	t14_t5 = S.Task('t14_t5', length=4, delay_cost=1)
	S += t14_t5 >= 83
	t14_t5 += MAS[2]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 84
	new_TZ0_w += MAIN_MEM_w

	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	S += new_TZ1_in >= 84
	new_TZ1_in += MAS_in[2]

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 84
	new_TZ1_mem0 += MM_MEM[0]

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	S += new_TZ1_mem1 >= 84
	new_TZ1_mem1 += MAS_MEM[5]

	new_TZ1 = S.Task('new_TZ1', length=4, delay_cost=1)
	S += new_TZ1 >= 85
	new_TZ1 += MAS[2]

	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	S += t13_t4_in >= 86
	t13_t4_in += MM_in[1]

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	S += t13_t4_mem0 >= 86
	t13_t4_mem0 += MAS_MEM[2]

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	S += t13_t4_mem1 >= 86
	t13_t4_mem1 += MAS_MEM[7]

	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	S += t141_in >= 86
	t141_in += MAS_in[5]

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	S += t141_mem0 >= 86
	t141_mem0 += MM_MEM[2]

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	S += t141_mem1 >= 86
	t141_mem1 += MAS_MEM[5]

	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	S += new_TX0_in >= 87
	new_TX0_in += MAS_in[1]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 87
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 87
	new_TX0_mem1 += MM_MEM[1]

	t13_t4 = S.Task('t13_t4', length=10, delay_cost=1)
	S += t13_t4 >= 87
	t13_t4 += MM[1]

	t141 = S.Task('t141', length=4, delay_cost=1)
	S += t141 >= 87
	t141 += MAS[5]

	new_TX0 = S.Task('new_TX0', length=4, delay_cost=1)
	S += new_TX0 >= 88
	new_TX0 += MAS[1]

	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	S += new_TX_t5_in >= 88
	new_TX_t5_in += MAS_in[0]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 88
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 88
	new_TX_t5_mem1 += MM_MEM[1]

	new_TX_t5 = S.Task('new_TX_t5', length=4, delay_cost=1)
	S += new_TX_t5 >= 89
	new_TX_t5 += MAS[0]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 89
	new_TZ1_w += MAIN_MEM_w

	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	S += t130_in >= 91
	t130_in += MAS_in[6]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 91
	t130_mem0 += MM_MEM[2]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 91
	t130_mem1 += MM_MEM[1]

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 92
	new_TX0_w += MAIN_MEM_w

	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	S += new_TX1_in >= 92
	new_TX1_in += MAS_in[1]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 92
	new_TX1_mem0 += MM_MEM[0]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 92
	new_TX1_mem1 += MAS_MEM[1]

	t130 = S.Task('t130', length=4, delay_cost=1)
	S += t130 >= 92
	t130 += MAS[6]

	t13_t5_in = S.Task('t13_t5_in', length=1, delay_cost=1)
	S += t13_t5_in >= 92
	t13_t5_in += MAS_in[0]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	S += t13_t5_mem0 >= 92
	t13_t5_mem0 += MM_MEM[2]

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	S += t13_t5_mem1 >= 92
	t13_t5_mem1 += MM_MEM[1]

	new_TX1 = S.Task('new_TX1', length=4, delay_cost=1)
	S += new_TX1 >= 93
	new_TX1 += MAS[1]

	t13_t5 = S.Task('t13_t5', length=4, delay_cost=1)
	S += t13_t5 >= 93
	t13_t5 += MAS[0]

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 95
	t150_in += MAS_in[0]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 95
	t150_mem0 += MAS_MEM[12]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 95
	t150_mem1 += MAS_MEM[9]

	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	S += t131_in >= 96
	t131_in += MAS_in[0]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 96
	t131_mem0 += MM_MEM[2]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 96
	t131_mem1 += MAS_MEM[1]

	t150 = S.Task('t150', length=4, delay_cost=1)
	S += t150 >= 96
	t150 += MAS[0]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 97
	new_TX1_w += MAIN_MEM_w

	t131 = S.Task('t131', length=4, delay_cost=1)
	S += t131 >= 97
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

	S += t151_in*MAS_in[4]<=t151*MAS[4]

	S += t151_in*MAS_in[5]<=t151*MAS[5]

	S += t151_in*MAS_in[6]<=t151*MAS[6]

	S += t151_in*MAS_in[7]<=t151*MAS[7]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[0]
	S += 100 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += MAS_MEM[11]
	S += 90 < t151_mem1
	S += t151_mem1 <= t151

	new_TY0 = S.Task('new_TY0', length=4, delay_cost=1)
	new_TY0 += alt(MAS)
	new_TY0_in = S.Task('new_TY0_in', length=1, delay_cost=1)
	new_TY0_in += alt(MAS_in)
	S += new_TY0_in*MAS_in[0]<=new_TY0*MAS[0]

	S += new_TY0_in*MAS_in[1]<=new_TY0*MAS[1]

	S += new_TY0_in*MAS_in[2]<=new_TY0*MAS[2]

	S += new_TY0_in*MAS_in[3]<=new_TY0*MAS[3]

	S += new_TY0_in*MAS_in[4]<=new_TY0*MAS[4]

	S += new_TY0_in*MAS_in[5]<=new_TY0*MAS[5]

	S += new_TY0_in*MAS_in[6]<=new_TY0*MAS[6]

	S += new_TY0_in*MAS_in[7]<=new_TY0*MAS[7]

	S += 67<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += MAIN_MEM_r[0]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += MAS_MEM[1]
	S += 99 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=4, delay_cost=1)
	new_TY1 += alt(MAS)
	new_TY1_in = S.Task('new_TY1_in', length=1, delay_cost=1)
	new_TY1_in += alt(MAS_in)
	S += new_TY1_in*MAS_in[0]<=new_TY1*MAS[0]

	S += new_TY1_in*MAS_in[1]<=new_TY1*MAS[1]

	S += new_TY1_in*MAS_in[2]<=new_TY1*MAS[2]

	S += new_TY1_in*MAS_in[3]<=new_TY1*MAS[3]

	S += new_TY1_in*MAS_in[4]<=new_TY1*MAS[4]

	S += new_TY1_in*MAS_in[5]<=new_TY1*MAS[5]

	S += new_TY1_in*MAS_in[6]<=new_TY1*MAS[6]

	S += new_TY1_in*MAS_in[7]<=new_TY1*MAS[7]

	S += 72<new_TY1

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
	S += (t151*MAS[4])-1 < new_TY1_mem1*MAS_MEM[9]
	S += (t151*MAS[5])-1 < new_TY1_mem1*MAS_MEM[11]
	S += (t151*MAS[6])-1 < new_TY1_mem1*MAS_MEM[13]
	S += (t151*MAS[7])-1 < new_TY1_mem1*MAS_MEM[15]
	S += new_TY1_mem1 <= new_TY1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage4MAS8/EP2_ADD_w_EVAL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

