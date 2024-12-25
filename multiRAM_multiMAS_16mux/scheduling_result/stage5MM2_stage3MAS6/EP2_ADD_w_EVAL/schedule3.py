from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 190
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=5)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 0
	t0_t0_in += MM_in[1]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 0
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 0
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t0 = S.Task('t0_t0', length=5, delay_cost=1)
	S += t0_t0 >= 1
	t0_t0 += MM[1]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 1
	t0_t1_in += MM_in[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 1
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 1
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=5, delay_cost=1)
	S += t0_t1 >= 2
	t0_t1 += MM[1]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 2
	t2_t0_in += MM_in[1]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 2
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 2
	t2_t0_mem1 += MAIN_MEM_r[1]

	t2_t0 = S.Task('t2_t0', length=5, delay_cost=1)
	S += t2_t0 >= 3
	t2_t0 += MM[1]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 3
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 3
	t2_t1_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 3
	t2_t1_mem1 += MAIN_MEM_r[1]

	t2_t1 = S.Task('t2_t1', length=5, delay_cost=1)
	S += t2_t1 >= 4
	t2_t1 += MM[0]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 4
	t2_t2_in += MAS_in[2]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 4
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 4
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=3, delay_cost=1)
	S += t2_t2 >= 5
	t2_t2 += MAS[2]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 5
	t2_t3_in += MAS_in[2]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 5
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 5
	t2_t3_mem1 += MAIN_MEM_r[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 6
	t00_in += MAS_in[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 6
	t00_mem0 += MM_MEM[2]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 6
	t00_mem1 += MM_MEM[3]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 6
	t0_t3_in += MAS_in[3]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 6
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 6
	t0_t3_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=3, delay_cost=1)
	S += t2_t3 >= 6
	t2_t3 += MAS[2]

	t00 = S.Task('t00', length=3, delay_cost=1)
	S += t00 >= 7
	t00 += MAS[0]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 7
	t0_t2_in += MAS_in[5]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 7
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 7
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=3, delay_cost=1)
	S += t0_t3 >= 7
	t0_t3 += MAS[3]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 7
	t0_t5_in += MAS_in[4]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 7
	t0_t5_mem0 += MM_MEM[2]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 7
	t0_t5_mem1 += MM_MEM[3]

	t0_t2 = S.Task('t0_t2', length=3, delay_cost=1)
	S += t0_t2 >= 8
	t0_t2 += MAS[5]

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	S += t0_t5 >= 8
	t0_t5 += MAS[4]

	t14_t2_in = S.Task('t14_t2_in', length=1, delay_cost=1)
	S += t14_t2_in >= 8
	t14_t2_in += MAS_in[0]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 8
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 8
	t14_t2_mem1 += MAIN_MEM_r[1]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 8
	t20_in += MAS_in[4]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 8
	t20_mem0 += MM_MEM[2]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 8
	t20_mem1 += MM_MEM[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 8
	t2_t4_in += MM_in[1]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 8
	t2_t4_mem0 += MAS_MEM[4]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 8
	t2_t4_mem1 += MAS_MEM[5]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 9
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 9
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 9
	t10_mem1 += MAS_MEM[1]

	t14_t2 = S.Task('t14_t2', length=3, delay_cost=1)
	S += t14_t2 >= 9
	t14_t2 += MAS[0]

	t20 = S.Task('t20', length=3, delay_cost=1)
	S += t20 >= 9
	t20 += MAS[4]

	t2_t4 = S.Task('t2_t4', length=5, delay_cost=1)
	S += t2_t4 >= 9
	t2_t4 += MM[1]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 9
	t2_t5_in += MAS_in[5]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 9
	t2_t5_mem0 += MM_MEM[2]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 9
	t2_t5_mem1 += MM_MEM[1]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 10
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 10
	t0_t4_mem0 += MAS_MEM[10]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 10
	t0_t4_mem1 += MAS_MEM[7]

	t10 = S.Task('t10', length=3, delay_cost=1)
	S += t10 >= 10
	t10 += MAS[0]

	t16_t2_in = S.Task('t16_t2_in', length=1, delay_cost=1)
	S += t16_t2_in >= 10
	t16_t2_in += MAS_in[0]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 10
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 10
	t16_t2_mem1 += MAIN_MEM_r[1]

	t2_t5 = S.Task('t2_t5', length=3, delay_cost=1)
	S += t2_t5 >= 10
	t2_t5 += MAS[5]

	t0_t4 = S.Task('t0_t4', length=5, delay_cost=1)
	S += t0_t4 >= 11
	t0_t4 += MM[0]

	t16_t2 = S.Task('t16_t2', length=3, delay_cost=1)
	S += t16_t2 >= 11
	t16_t2 += MAS[0]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 11
	t30_in += MAS_in[3]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 11
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 11
	t30_mem1 += MAS_MEM[9]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 12
	c200_in += MM_in[1]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 12
	c200_mem0 += MAS_MEM[0]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 12
	c200_mem1 += MAIN_MEM_r[1]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 12
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 12
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 12
	t17_t0_mem1 += MAS_MEM[1]

	t30 = S.Task('t30', length=3, delay_cost=1)
	S += t30 >= 12
	t30 += MAS[3]

	c200 = S.Task('c200', length=5, delay_cost=1)
	S += c200 >= 13
	c200 += MM[1]

	new_TZ_t2_in = S.Task('new_TZ_t2_in', length=1, delay_cost=1)
	S += new_TZ_t2_in >= 13
	new_TZ_t2_in += MAS_in[0]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 13
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 13
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t17_t0 = S.Task('t17_t0', length=5, delay_cost=1)
	S += t17_t0 >= 13
	t17_t0 += MM[0]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 13
	t21_in += MAS_in[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 13
	t21_mem0 += MM_MEM[2]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 13
	t21_mem1 += MAS_MEM[11]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 14
	c010_in += MM_in[1]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 14
	c010_mem0 += MAS_MEM[6]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 14
	c010_mem1 += MAIN_MEM_r[1]

	new_TZ_t2 = S.Task('new_TZ_t2', length=3, delay_cost=1)
	S += new_TZ_t2 >= 14
	new_TZ_t2 += MAS[0]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 14
	t16_t0_in += MM_in[0]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 14
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 14
	t16_t0_mem1 += MAS_MEM[7]

	t21 = S.Task('t21', length=3, delay_cost=1)
	S += t21 >= 14
	t21 += MAS[1]

	c010 = S.Task('c010', length=5, delay_cost=1)
	S += c010 >= 15
	c010 += MM[1]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 15
	t01_in += MAS_in[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 15
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 15
	t01_mem1 += MAS_MEM[9]

	t16_t0 = S.Task('t16_t0', length=5, delay_cost=1)
	S += t16_t0 >= 15
	t16_t0 += MM[0]

	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	S += t17_t2_in >= 15
	t17_t2_in += MAS_in[1]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 15
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 15
	t17_t2_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=3, delay_cost=1)
	S += t01 >= 16
	t01 += MAS[0]

	t17_t2 = S.Task('t17_t2', length=3, delay_cost=1)
	S += t17_t2 >= 16
	t17_t2 += MAS[1]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 16
	t7_t2_in += MAS_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 16
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 16
	t7_t2_mem1 += MAIN_MEM_r[1]

	t7_t2 = S.Task('t7_t2', length=3, delay_cost=1)
	S += t7_t2 >= 17
	t7_t2 += MAS[0]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 17
	t9_t2_in += MAS_in[0]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 17
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 17
	t9_t2_mem1 += MAIN_MEM_r[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 18
	c200_w += MAIN_MEM_w

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 18
	t31_in += MAS_in[4]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 18
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 18
	t31_mem1 += MAS_MEM[3]

	t9_t2 = S.Task('t9_t2', length=3, delay_cost=1)
	S += t9_t2 >= 18
	t9_t2 += MAS[0]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 19
	t11_in += MAS_in[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 19
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 19
	t11_mem1 += MAS_MEM[1]

	t31 = S.Task('t31', length=3, delay_cost=1)
	S += t31 >= 19
	t31 += MAS[4]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 20
	c010_w += MAIN_MEM_w

	t11 = S.Task('t11', length=3, delay_cost=1)
	S += t11 >= 20
	t11 += MAS[0]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 21
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 21
	c011_mem0 += MAS_MEM[8]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 21
	c011_mem1 += MAIN_MEM_r[1]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 21
	t5_t3_in += MM_in[1]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 21
	t5_t3_mem0 += MAS_MEM[6]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 21
	t5_t3_mem1 += MAS_MEM[9]

	c011 = S.Task('c011', length=5, delay_cost=1)
	S += c011 >= 22
	c011 += MM[0]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 22
	c201_in += MM_in[1]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 22
	c201_mem0 += MAS_MEM[0]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 22
	c201_mem1 += MAIN_MEM_r[1]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 22
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 22
	t17_t1_mem0 += MAIN_MEM_r[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 22
	t17_t1_mem1 += MAS_MEM[1]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 22
	t5_t0_in += MAS_in[5]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 22
	t5_t0_mem0 += MAS_MEM[6]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 22
	t5_t0_mem1 += MAS_MEM[9]

	t5_t3 = S.Task('t5_t3', length=5, delay_cost=1)
	S += t5_t3 >= 22
	t5_t3 += MM[1]

	c201 = S.Task('c201', length=5, delay_cost=1)
	S += c201 >= 23
	c201 += MM[1]

	t17_t1 = S.Task('t17_t1', length=5, delay_cost=1)
	S += t17_t1 >= 23
	t17_t1 += MM[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 23
	t4_t3_in += MM_in[1]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 23
	t4_t3_mem0 += MAS_MEM[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 23
	t4_t3_mem1 += MAS_MEM[1]

	t5_t0 = S.Task('t5_t0', length=3, delay_cost=1)
	S += t5_t0 >= 23
	t5_t0 += MAS[5]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 23
	t5_t1_in += MAS_in[2]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 23
	t5_t1_mem0 += MAS_MEM[6]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 23
	t5_t1_mem1 += MAS_MEM[9]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 24
	t16_t1_in += MM_in[0]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 24
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 24
	t16_t1_mem1 += MAS_MEM[9]

	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	S += t17_t3_in >= 24
	t17_t3_in += MAS_in[3]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 24
	t17_t3_mem0 += MAS_MEM[0]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 24
	t17_t3_mem1 += MAS_MEM[1]

	t4_t3 = S.Task('t4_t3', length=5, delay_cost=1)
	S += t4_t3 >= 24
	t4_t3 += MM[1]

	t5_t1 = S.Task('t5_t1', length=3, delay_cost=1)
	S += t5_t1 >= 24
	t5_t1 += MAS[2]

	t16_t1 = S.Task('t16_t1', length=5, delay_cost=1)
	S += t16_t1 >= 25
	t16_t1 += MM[0]

	t16_t3_in = S.Task('t16_t3_in', length=1, delay_cost=1)
	S += t16_t3_in >= 25
	t16_t3_in += MAS_in[1]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 25
	t16_t3_mem0 += MAS_MEM[6]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 25
	t16_t3_mem1 += MAS_MEM[9]

	t17_t3 = S.Task('t17_t3', length=3, delay_cost=1)
	S += t17_t3 >= 25
	t17_t3 += MAS[3]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 25
	t4_t0_in += MAS_in[3]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 25
	t4_t0_mem0 += MAS_MEM[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 25
	t4_t0_mem1 += MAS_MEM[1]

	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	S += new_TX_t2_in >= 26
	new_TX_t2_in += MAS_in[5]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 26
	new_TX_t2_mem0 += MAS_MEM[6]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 26
	new_TX_t2_mem1 += MAS_MEM[9]

	t16_t3 = S.Task('t16_t3', length=3, delay_cost=1)
	S += t16_t3 >= 26
	t16_t3 += MAS[1]

	t4_t0 = S.Task('t4_t0', length=3, delay_cost=1)
	S += t4_t0 >= 26
	t4_t0 += MAS[3]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 26
	t4_t1_in += MAS_in[0]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 26
	t4_t1_mem0 += MAS_MEM[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 26
	t4_t1_mem1 += MAS_MEM[1]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 26
	t51_in += MAS_in[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 26
	t51_mem0 += MM_MEM[2]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 26
	t51_mem1 += MM_MEM[3]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 26
	t5_t2_in += MM_in[1]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 26
	t5_t2_mem0 += MAS_MEM[10]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 26
	t5_t2_mem1 += MAS_MEM[5]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 27
	c011_w += MAIN_MEM_w

	new_TX_t2 = S.Task('new_TX_t2', length=3, delay_cost=1)
	S += new_TX_t2 >= 27
	new_TX_t2 += MAS[5]

	t13_t2_in = S.Task('t13_t2_in', length=1, delay_cost=1)
	S += t13_t2_in >= 27
	t13_t2_in += MAS_in[1]

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 27
	t13_t2_mem0 += MAS_MEM[0]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 27
	t13_t2_mem1 += MAS_MEM[1]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 27
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 27
	t17_t4_mem0 += MAS_MEM[2]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 27
	t17_t4_mem1 += MAS_MEM[7]

	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	S += t17_t5_in >= 27
	t17_t5_in += MAS_in[0]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 27
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 27
	t17_t5_mem1 += MM_MEM[1]

	t4_t1 = S.Task('t4_t1', length=3, delay_cost=1)
	S += t4_t1 >= 27
	t4_t1 += MAS[0]

	t51 = S.Task('t51', length=3, delay_cost=1)
	S += t51 >= 27
	t51 += MAS[1]

	t5_t2 = S.Task('t5_t2', length=5, delay_cost=1)
	S += t5_t2 >= 27
	t5_t2 += MM[1]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 27
	t5_t5_in += MAS_in[2]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 27
	t5_t5_mem0 += MM_MEM[2]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 27
	t5_t5_mem1 += MM_MEM[3]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 27
	t6_t2_in += MAS_in[4]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 27
	t6_t2_mem0 += MAS_MEM[6]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 27
	t6_t2_mem1 += MAS_MEM[9]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 28
	c201_w += MAIN_MEM_w

	t13_t2 = S.Task('t13_t2', length=3, delay_cost=1)
	S += t13_t2 >= 28
	t13_t2 += MAS[1]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 28
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 28
	t16_t4_mem0 += MAS_MEM[0]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 28
	t16_t4_mem1 += MAS_MEM[3]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 28
	t170_in += MAS_in[2]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 28
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 28
	t170_mem1 += MM_MEM[1]

	t17_t4 = S.Task('t17_t4', length=5, delay_cost=1)
	S += t17_t4 >= 28
	t17_t4 += MM[0]

	t17_t5 = S.Task('t17_t5', length=3, delay_cost=1)
	S += t17_t5 >= 28
	t17_t5 += MAS[0]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 28
	t41_in += MAS_in[1]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 28
	t41_mem0 += MM_MEM[2]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 28
	t41_mem1 += MM_MEM[3]

	t5_t5 = S.Task('t5_t5', length=3, delay_cost=1)
	S += t5_t5 >= 28
	t5_t5 += MAS[2]

	t6_t2 = S.Task('t6_t2', length=3, delay_cost=1)
	S += t6_t2 >= 28
	t6_t2 += MAS[4]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 29
	t160_in += MAS_in[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 29
	t160_mem0 += MM_MEM[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 29
	t160_mem1 += MM_MEM[1]

	t16_t4 = S.Task('t16_t4', length=5, delay_cost=1)
	S += t16_t4 >= 29
	t16_t4 += MM[0]

	t170 = S.Task('t170', length=3, delay_cost=1)
	S += t170 >= 29
	t170 += MAS[2]

	t41 = S.Task('t41', length=3, delay_cost=1)
	S += t41 >= 29
	t41 += MAS[1]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 29
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 29
	t4_t2_mem0 += MAS_MEM[6]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 29
	t4_t2_mem1 += MAS_MEM[1]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 29
	t4_t5_in += MAS_in[2]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 29
	t4_t5_mem0 += MM_MEM[2]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 29
	t4_t5_mem1 += MM_MEM[3]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 29
	t9_t1_in += MM_in[1]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 29
	t9_t1_mem0 += MAIN_MEM_r[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 29
	t9_t1_mem1 += MAS_MEM[3]

	t160 = S.Task('t160', length=3, delay_cost=1)
	S += t160 >= 30
	t160 += MAS[0]

	t16_t5_in = S.Task('t16_t5_in', length=1, delay_cost=1)
	S += t16_t5_in >= 30
	t16_t5_in += MAS_in[4]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 30
	t16_t5_mem0 += MM_MEM[0]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 30
	t16_t5_mem1 += MM_MEM[1]

	t4_t2 = S.Task('t4_t2', length=5, delay_cost=1)
	S += t4_t2 >= 30
	t4_t2 += MM[0]

	t4_t5 = S.Task('t4_t5', length=3, delay_cost=1)
	S += t4_t5 >= 30
	t4_t5 += MAS[2]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 30
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 30
	t6_t1_mem0 += MAS_MEM[8]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 30
	t6_t1_mem1 += MAS_MEM[3]

	t9_t1 = S.Task('t9_t1', length=5, delay_cost=1)
	S += t9_t1 >= 30
	t9_t1 += MM[1]

	t16_t5 = S.Task('t16_t5', length=3, delay_cost=1)
	S += t16_t5 >= 31
	t16_t5 += MAS[4]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 31
	t50_in += MAS_in[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 31
	t50_mem0 += MM_MEM[2]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 31
	t50_mem1 += MAS_MEM[5]

	t6_t1 = S.Task('t6_t1', length=5, delay_cost=1)
	S += t6_t1 >= 31
	t6_t1 += MM[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 31
	t7_t1_in += MM_in[1]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 31
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 31
	t7_t1_mem1 += MAS_MEM[3]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 32
	c000_in += MAS_in[0]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 32
	c000_mem0 += MAS_MEM[0]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 32
	c000_mem1 += MAS_MEM[5]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 32
	t171_in += MAS_in[5]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 32
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 32
	t171_mem1 += MAS_MEM[1]

	t50 = S.Task('t50', length=3, delay_cost=1)
	S += t50 >= 32
	t50 += MAS[0]

	t7_t1 = S.Task('t7_t1', length=5, delay_cost=1)
	S += t7_t1 >= 32
	t7_t1 += MM[1]

	c000 = S.Task('c000', length=3, delay_cost=1)
	S += c000 >= 33
	c000 += MAS[0]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 33
	t161_in += MAS_in[4]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 33
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 33
	t161_mem1 += MAS_MEM[9]

	t171 = S.Task('t171', length=3, delay_cost=1)
	S += t171 >= 33
	t171 += MAS[5]

	t161 = S.Task('t161', length=3, delay_cost=1)
	S += t161 >= 34
	t161 += MAS[4]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 34
	t40_in += MAS_in[3]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 34
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 34
	t40_mem1 += MAS_MEM[5]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 34
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 34
	t6_t0_mem0 += MAS_MEM[6]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 34
	t6_t0_mem1 += MAS_MEM[1]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 34
	t6_t3_in += MAS_in[4]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 34
	t6_t3_mem0 += MAS_MEM[0]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 34
	t6_t3_mem1 += MAS_MEM[3]

	t40 = S.Task('t40', length=3, delay_cost=1)
	S += t40 >= 35
	t40 += MAS[3]

	t6_t0 = S.Task('t6_t0', length=5, delay_cost=1)
	S += t6_t0 >= 35
	t6_t0 += MM[0]

	t6_t3 = S.Task('t6_t3', length=3, delay_cost=1)
	S += t6_t3 >= 35
	t6_t3 += MAS[4]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 35
	t9_t0_in += MM_in[1]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 35
	t9_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 35
	t9_t0_mem1 += MAS_MEM[1]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 35
	t9_t3_in += MAS_in[4]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 35
	t9_t3_mem0 += MAS_MEM[0]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 35
	t9_t3_mem1 += MAS_MEM[3]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 36
	c000_w += MAIN_MEM_w

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 36
	c001_in += MAS_in[1]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 36
	c001_mem0 += MAS_MEM[8]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 36
	c001_mem1 += MAS_MEM[11]

	t9_t0 = S.Task('t9_t0', length=5, delay_cost=1)
	S += t9_t0 >= 36
	t9_t0 += MM[1]

	t9_t3 = S.Task('t9_t3', length=3, delay_cost=1)
	S += t9_t3 >= 36
	t9_t3 += MAS[4]

	c001 = S.Task('c001', length=3, delay_cost=1)
	S += c001 >= 37
	c001 += MAS[1]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 37
	t6_t4_in += MM_in[1]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 37
	t6_t4_mem0 += MAS_MEM[8]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 37
	t6_t4_mem1 += MAS_MEM[9]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 37
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 37
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 37
	t7_t0_mem1 += MAS_MEM[7]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 37
	t7_t3_in += MAS_in[2]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 37
	t7_t3_mem0 += MAS_MEM[6]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 37
	t7_t3_mem1 += MAS_MEM[3]

	t6_t4 = S.Task('t6_t4', length=5, delay_cost=1)
	S += t6_t4 >= 38
	t6_t4 += MM[1]

	t7_t0 = S.Task('t7_t0', length=5, delay_cost=1)
	S += t7_t0 >= 38
	t7_t0 += MM[0]

	t7_t3 = S.Task('t7_t3', length=3, delay_cost=1)
	S += t7_t3 >= 38
	t7_t3 += MAS[2]

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	S += t9_t4_in >= 38
	t9_t4_in += MM_in[1]

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	S += t9_t4_mem0 >= 38
	t9_t4_mem0 += MAS_MEM[0]

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	S += t9_t4_mem1 >= 38
	t9_t4_mem1 += MAS_MEM[9]

	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	S += t6_t5_in >= 39
	t6_t5_in += MAS_in[2]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 39
	t6_t5_mem0 += MM_MEM[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 39
	t6_t5_mem1 += MM_MEM[1]

	t9_t4 = S.Task('t9_t4', length=5, delay_cost=1)
	S += t9_t4 >= 39
	t9_t4 += MM[1]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 40
	c001_w += MAIN_MEM_w

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 40
	t60_in += MAS_in[2]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 40
	t60_mem0 += MM_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 40
	t60_mem1 += MM_MEM[1]

	t6_t5 = S.Task('t6_t5', length=3, delay_cost=1)
	S += t6_t5 >= 40
	t6_t5 += MAS[2]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 40
	t7_t4_in += MM_in[1]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 40
	t7_t4_mem0 += MAS_MEM[0]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 40
	t7_t4_mem1 += MAS_MEM[5]

	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	S += t9_t5_in >= 40
	t9_t5_in += MAS_in[0]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 40
	t9_t5_mem0 += MM_MEM[2]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 40
	t9_t5_mem1 += MM_MEM[3]

	t60 = S.Task('t60', length=3, delay_cost=1)
	S += t60 >= 41
	t60 += MAS[2]

	t7_t4 = S.Task('t7_t4', length=5, delay_cost=1)
	S += t7_t4 >= 41
	t7_t4 += MM[1]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 41
	t90_in += MAS_in[5]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 41
	t90_mem0 += MM_MEM[2]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 41
	t90_mem1 += MM_MEM[3]

	t9_t5 = S.Task('t9_t5', length=3, delay_cost=1)
	S += t9_t5 >= 41
	t9_t5 += MAS[0]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 42
	t61_in += MAS_in[0]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 42
	t61_mem0 += MM_MEM[2]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 42
	t61_mem1 += MAS_MEM[5]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 42
	t7_t5_in += MAS_in[5]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 42
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 42
	t7_t5_mem1 += MM_MEM[3]

	t90 = S.Task('t90', length=3, delay_cost=1)
	S += t90 >= 42
	t90 += MAS[5]

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	S += new_TZ_t0_in >= 43
	new_TZ_t0_in += MM_in[0]

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	S += new_TZ_t0_mem0 >= 43
	new_TZ_t0_mem0 += MAIN_MEM_r[0]

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	S += new_TZ_t0_mem1 >= 43
	new_TZ_t0_mem1 += MAS_MEM[5]

	t61 = S.Task('t61', length=3, delay_cost=1)
	S += t61 >= 43
	t61 += MAS[0]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 43
	t70_in += MAS_in[2]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 43
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 43
	t70_mem1 += MM_MEM[3]

	t7_t5 = S.Task('t7_t5', length=3, delay_cost=1)
	S += t7_t5 >= 43
	t7_t5 += MAS[5]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 43
	t91_in += MAS_in[4]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 43
	t91_mem0 += MM_MEM[2]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 43
	t91_mem1 += MAS_MEM[1]

	new_TZ_t0 = S.Task('new_TZ_t0', length=5, delay_cost=1)
	S += new_TZ_t0 >= 44
	new_TZ_t0 += MM[0]

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 44
	t100_in += MAS_in[2]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 44
	t100_mem0 += MAS_MEM[10]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 44
	t100_mem1 += MAS_MEM[11]

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	S += t14_t0_in >= 44
	t14_t0_in += MM_in[1]

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	S += t14_t0_mem0 >= 44
	t14_t0_mem0 += MAIN_MEM_r[0]

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	S += t14_t0_mem1 >= 44
	t14_t0_mem1 += MAS_MEM[5]

	t70 = S.Task('t70', length=3, delay_cost=1)
	S += t70 >= 44
	t70 += MAS[2]

	t91 = S.Task('t91', length=3, delay_cost=1)
	S += t91 >= 44
	t91 += MAS[4]

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	S += new_TZ_t1_in >= 45
	new_TZ_t1_in += MM_in[1]

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	S += new_TZ_t1_mem0 >= 45
	new_TZ_t1_mem0 += MAIN_MEM_r[0]

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	S += new_TZ_t1_mem1 >= 45
	new_TZ_t1_mem1 += MAS_MEM[1]

	t100 = S.Task('t100', length=3, delay_cost=1)
	S += t100 >= 45
	t100 += MAS[2]

	t14_t0 = S.Task('t14_t0', length=5, delay_cost=1)
	S += t14_t0 >= 45
	t14_t0 += MM[1]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 45
	t71_in += MAS_in[2]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 45
	t71_mem0 += MM_MEM[2]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 45
	t71_mem1 += MAS_MEM[11]

	new_TZ_t1 = S.Task('new_TZ_t1', length=5, delay_cost=1)
	S += new_TZ_t1 >= 46
	new_TZ_t1 += MM[1]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 46
	t101_in += MAS_in[2]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 46
	t101_mem0 += MAS_MEM[8]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 46
	t101_mem1 += MAS_MEM[9]

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	S += t14_t1_in >= 46
	t14_t1_in += MM_in[0]

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	S += t14_t1_mem0 >= 46
	t14_t1_mem0 += MAIN_MEM_r[0]

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	S += t14_t1_mem1 >= 46
	t14_t1_mem1 += MAS_MEM[1]

	t71 = S.Task('t71', length=3, delay_cost=1)
	S += t71 >= 46
	t71 += MAS[2]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 46
	t80_in += MAS_in[5]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 46
	t80_mem0 += MAS_MEM[4]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 46
	t80_mem1 += MAS_MEM[5]

	new_TZ_t3_in = S.Task('new_TZ_t3_in', length=1, delay_cost=1)
	S += new_TZ_t3_in >= 47
	new_TZ_t3_in += MAS_in[4]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	S += new_TZ_t3_mem0 >= 47
	new_TZ_t3_mem0 += MAS_MEM[4]

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	S += new_TZ_t3_mem1 >= 47
	new_TZ_t3_mem1 += MAS_MEM[1]

	t101 = S.Task('t101', length=3, delay_cost=1)
	S += t101 >= 47
	t101 += MAS[2]

	t14_t1 = S.Task('t14_t1', length=5, delay_cost=1)
	S += t14_t1 >= 47
	t14_t1 += MM[0]

	t80 = S.Task('t80', length=3, delay_cost=1)
	S += t80 >= 47
	t80 += MAS[5]

	new_TZ_t3 = S.Task('new_TZ_t3', length=3, delay_cost=1)
	S += new_TZ_t3 >= 48
	new_TZ_t3 += MAS[4]

	t14_t3_in = S.Task('t14_t3_in', length=1, delay_cost=1)
	S += t14_t3_in >= 48
	t14_t3_in += MAS_in[0]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	S += t14_t3_mem0 >= 48
	t14_t3_mem0 += MAS_MEM[4]

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	S += t14_t3_mem1 >= 48
	t14_t3_mem1 += MAS_MEM[1]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 48
	t81_in += MAS_in[3]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 48
	t81_mem0 += MAS_MEM[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 48
	t81_mem1 += MAS_MEM[5]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 49
	t110_in += MAS_in[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 49
	t110_mem0 += MAS_MEM[10]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 49
	t110_mem1 += MAS_MEM[5]

	t14_t3 = S.Task('t14_t3', length=3, delay_cost=1)
	S += t14_t3 >= 49
	t14_t3 += MAS[0]

	t81 = S.Task('t81', length=3, delay_cost=1)
	S += t81 >= 49
	t81 += MAS[3]

	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	S += new_TZ0_in >= 50
	new_TZ0_in += MAS_in[4]

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	S += new_TZ0_mem0 >= 50
	new_TZ0_mem0 += MM_MEM[0]

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	S += new_TZ0_mem1 >= 50
	new_TZ0_mem1 += MM_MEM[3]

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	S += new_TZ_t4_in >= 50
	new_TZ_t4_in += MM_in[1]

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	S += new_TZ_t4_mem0 >= 50
	new_TZ_t4_mem0 += MAS_MEM[0]

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	S += new_TZ_t4_mem1 >= 50
	new_TZ_t4_mem1 += MAS_MEM[9]

	t110 = S.Task('t110', length=3, delay_cost=1)
	S += t110 >= 50
	t110 += MAS[1]

	new_TZ0 = S.Task('new_TZ0', length=3, delay_cost=1)
	S += new_TZ0 >= 51
	new_TZ0 += MAS[4]

	new_TZ_t4 = S.Task('new_TZ_t4', length=5, delay_cost=1)
	S += new_TZ_t4 >= 51
	new_TZ_t4 += MM[1]

	new_TZ_t5_in = S.Task('new_TZ_t5_in', length=1, delay_cost=1)
	S += new_TZ_t5_in >= 51
	new_TZ_t5_in += MAS_in[5]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	S += new_TZ_t5_mem0 >= 51
	new_TZ_t5_mem0 += MM_MEM[0]

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	S += new_TZ_t5_mem1 >= 51
	new_TZ_t5_mem1 += MM_MEM[3]

	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	S += t111_in >= 51
	t111_in += MAS_in[2]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 51
	t111_mem0 += MAS_MEM[6]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 51
	t111_mem1 += MAS_MEM[5]

	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	S += t140_in >= 51
	t140_in += MAS_in[4]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	S += t140_mem0 >= 51
	t140_mem0 += MM_MEM[2]

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	S += t140_mem1 >= 51
	t140_mem1 += MM_MEM[1]

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	S += t14_t4_in >= 51
	t14_t4_in += MM_in[1]

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	S += t14_t4_mem0 >= 51
	t14_t4_mem0 += MAS_MEM[0]

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	S += t14_t4_mem1 >= 51
	t14_t4_mem1 += MAS_MEM[1]

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	S += new_TX_t0_in >= 52
	new_TX_t0_in += MM_in[0]

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	S += new_TX_t0_mem0 >= 52
	new_TX_t0_mem0 += MAS_MEM[6]

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	S += new_TX_t0_mem1 >= 52
	new_TX_t0_mem1 += MAS_MEM[3]

	new_TZ_t5 = S.Task('new_TZ_t5', length=3, delay_cost=1)
	S += new_TZ_t5 >= 52
	new_TZ_t5 += MAS[5]

	t111 = S.Task('t111', length=3, delay_cost=1)
	S += t111 >= 52
	t111 += MAS[2]

	t140 = S.Task('t140', length=3, delay_cost=1)
	S += t140 >= 52
	t140 += MAS[4]

	t14_t4 = S.Task('t14_t4', length=5, delay_cost=1)
	S += t14_t4 >= 52
	t14_t4 += MM[1]

	new_TX_t0 = S.Task('new_TX_t0', length=5, delay_cost=1)
	S += new_TX_t0 >= 53
	new_TX_t0 += MM[0]

	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	S += new_TX_t1_in >= 54
	new_TX_t1_in += MM_in[0]

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	S += new_TX_t1_mem0 >= 54
	new_TX_t1_mem0 += MAS_MEM[8]

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	S += new_TX_t1_mem1 >= 54
	new_TX_t1_mem1 += MAS_MEM[5]

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	S += new_TZ0_w >= 54
	new_TZ0_w += MAIN_MEM_w

	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	S += t121_in >= 54
	t121_in += MAS_in[4]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 54
	t121_mem0 += MAS_MEM[4]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 54
	t121_mem1 += MAS_MEM[9]

	new_TX_t1 = S.Task('new_TX_t1', length=5, delay_cost=1)
	S += new_TX_t1 >= 55
	new_TX_t1 += MM[0]

	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	S += new_TX_t3_in >= 55
	new_TX_t3_in += MAS_in[3]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	S += new_TX_t3_mem0 >= 55
	new_TX_t3_mem0 += MAS_MEM[2]

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	S += new_TX_t3_mem1 >= 55
	new_TX_t3_mem1 += MAS_MEM[5]

	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	S += new_TZ1_in >= 55
	new_TZ1_in += MAS_in[1]

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	S += new_TZ1_mem0 >= 55
	new_TZ1_mem0 += MM_MEM[2]

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	S += new_TZ1_mem1 >= 55
	new_TZ1_mem1 += MAS_MEM[11]

	t121 = S.Task('t121', length=3, delay_cost=1)
	S += t121 >= 55
	t121 += MAS[4]

	new_TX_t3 = S.Task('new_TX_t3', length=3, delay_cost=1)
	S += new_TX_t3 >= 56
	new_TX_t3 += MAS[3]

	new_TZ1 = S.Task('new_TZ1', length=3, delay_cost=1)
	S += new_TZ1 >= 56
	new_TZ1 += MAS[1]

	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	S += t13_t1_in >= 57
	t13_t1_in += MM_in[1]

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	S += t13_t1_mem0 >= 57
	t13_t1_mem0 += MAS_MEM[0]

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	S += t13_t1_mem1 >= 57
	t13_t1_mem1 += MAS_MEM[9]

	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	S += new_TX_t4_in >= 58
	new_TX_t4_in += MM_in[0]

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	S += new_TX_t4_mem0 >= 58
	new_TX_t4_mem0 += MAS_MEM[10]

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	S += new_TX_t4_mem1 >= 58
	new_TX_t4_mem1 += MAS_MEM[7]

	t13_t1 = S.Task('t13_t1', length=5, delay_cost=1)
	S += t13_t1 >= 58
	t13_t1 += MM[1]

	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	S += new_TX0_in >= 59
	new_TX0_in += MAS_in[2]

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	S += new_TX0_mem0 >= 59
	new_TX0_mem0 += MM_MEM[0]

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	S += new_TX0_mem1 >= 59
	new_TX0_mem1 += MM_MEM[1]

	new_TX_t4 = S.Task('new_TX_t4', length=5, delay_cost=1)
	S += new_TX_t4 >= 59
	new_TX_t4 += MM[0]

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	S += new_TZ1_w >= 59
	new_TZ1_w += MAIN_MEM_w

	new_TX0 = S.Task('new_TX0', length=3, delay_cost=1)
	S += new_TX0 >= 60
	new_TX0 += MAS[2]

	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	S += new_TX_t5_in >= 60
	new_TX_t5_in += MAS_in[3]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	S += new_TX_t5_mem0 >= 60
	new_TX_t5_mem0 += MM_MEM[0]

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	S += new_TX_t5_mem1 >= 60
	new_TX_t5_mem1 += MM_MEM[1]

	new_TX_t5 = S.Task('new_TX_t5', length=3, delay_cost=1)
	S += new_TX_t5 >= 61
	new_TX_t5 += MAS[3]

	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	S += t13_t4_in >= 61
	t13_t4_in += MM_in[0]

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	S += t13_t4_mem0 >= 61
	t13_t4_mem0 += MAS_MEM[2]

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	S += t13_t4_mem1 >= 61
	t13_t4_mem1 += MAS_MEM[11]

	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	S += t130_in >= 62
	t130_in += MAS_in[0]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 62
	t130_mem0 += MM_MEM[2]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 62
	t130_mem1 += MM_MEM[3]

	t13_t4 = S.Task('t13_t4', length=5, delay_cost=1)
	S += t13_t4 >= 62
	t13_t4 += MM[0]

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	S += new_TX0_w >= 63
	new_TX0_w += MAIN_MEM_w

	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	S += new_TX1_in >= 63
	new_TX1_in += MAS_in[2]

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	S += new_TX1_mem0 >= 63
	new_TX1_mem0 += MM_MEM[0]

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	S += new_TX1_mem1 >= 63
	new_TX1_mem1 += MAS_MEM[7]

	t130 = S.Task('t130', length=3, delay_cost=1)
	S += t130 >= 63
	t130 += MAS[0]

	t13_t5_in = S.Task('t13_t5_in', length=1, delay_cost=1)
	S += t13_t5_in >= 63
	t13_t5_in += MAS_in[1]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	S += t13_t5_mem0 >= 63
	t13_t5_mem0 += MM_MEM[2]

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	S += t13_t5_mem1 >= 63
	t13_t5_mem1 += MM_MEM[3]

	new_TX1 = S.Task('new_TX1', length=3, delay_cost=1)
	S += new_TX1 >= 64
	new_TX1 += MAS[2]

	t13_t5 = S.Task('t13_t5', length=3, delay_cost=1)
	S += t13_t5 >= 64
	t13_t5 += MAS[1]

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 65
	t150_in += MAS_in[2]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 65
	t150_mem0 += MAS_MEM[0]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 65
	t150_mem1 += MAS_MEM[9]

	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	S += t131_in >= 66
	t131_in += MAS_in[5]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 66
	t131_mem0 += MM_MEM[0]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 66
	t131_mem1 += MAS_MEM[3]

	t150 = S.Task('t150', length=3, delay_cost=1)
	S += t150 >= 66
	t150 += MAS[2]

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	S += new_TX1_w >= 67
	new_TX1_w += MAIN_MEM_w

	t131 = S.Task('t131', length=3, delay_cost=1)
	S += t131 >= 67
	t131 += MAS[5]


	# new tasks
	t120 = S.Task('t120', length=3, delay_cost=1)
	t120 += alt(MAS)
	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	t120_in += alt(MAS_in)
	S += t120_in*MAS_in[0]<=t120*MAS[0]

	S += t120_in*MAS_in[1]<=t120*MAS[1]

	S += t120_in*MAS_in[2]<=t120*MAS[2]

	S += t120_in*MAS_in[3]<=t120*MAS[3]

	S += t120_in*MAS_in[4]<=t120*MAS[4]

	S += t120_in*MAS_in[5]<=t120*MAS[5]

	S += t120<59

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += MAS_MEM[2]
	S += 52 < t120_mem0
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += MAS_MEM[11]
	S += 44 < t120_mem1
	S += t120_mem1 <= t120

	t14_t5 = S.Task('t14_t5', length=3, delay_cost=1)
	t14_t5 += alt(MAS)
	t14_t5_in = S.Task('t14_t5_in', length=1, delay_cost=1)
	t14_t5_in += alt(MAS_in)
	S += t14_t5_in*MAS_in[0]<=t14_t5*MAS[0]

	S += t14_t5_in*MAS_in[1]<=t14_t5*MAS[1]

	S += t14_t5_in*MAS_in[2]<=t14_t5*MAS[2]

	S += t14_t5_in*MAS_in[3]<=t14_t5*MAS[3]

	S += t14_t5_in*MAS_in[4]<=t14_t5*MAS[4]

	S += t14_t5_in*MAS_in[5]<=t14_t5*MAS[5]

	S += t14_t5<57

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	t14_t5_mem0 += MM_MEM[2]
	S += 49 < t14_t5_mem0
	S += t14_t5_mem0 <= t14_t5

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	t14_t5_mem1 += MM_MEM[1]
	S += 51 < t14_t5_mem1
	S += t14_t5_mem1 <= t14_t5

	t13_t0 = S.Task('t13_t0', length=5, delay_cost=1)
	t13_t0 += alt(MM)
	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	t13_t0_in += alt(MM_in)
	S += t13_t0_in*MM_in[0]<=t13_t0*MM[0]
	S += t13_t0_in*MM_in[1]<=t13_t0*MM[1]
	S += t13_t0<63

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	t13_t0_mem0 += MAS_MEM[0]
	S += 12 < t13_t0_mem0
	S += t13_t0_mem0 <= t13_t0

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	t13_t0_mem1 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t13_t0_mem1*MAS_MEM[1]
	S += (t120*MAS[1])-1 < t13_t0_mem1*MAS_MEM[3]
	S += (t120*MAS[2])-1 < t13_t0_mem1*MAS_MEM[5]
	S += (t120*MAS[3])-1 < t13_t0_mem1*MAS_MEM[7]
	S += (t120*MAS[4])-1 < t13_t0_mem1*MAS_MEM[9]
	S += (t120*MAS[5])-1 < t13_t0_mem1*MAS_MEM[11]
	S += t13_t0_mem1 <= t13_t0

	t141 = S.Task('t141', length=3, delay_cost=1)
	t141 += alt(MAS)
	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	t141_in += alt(MAS_in)
	S += t141_in*MAS_in[0]<=t141*MAS[0]

	S += t141_in*MAS_in[1]<=t141*MAS[1]

	S += t141_in*MAS_in[2]<=t141*MAS[2]

	S += t141_in*MAS_in[3]<=t141*MAS[3]

	S += t141_in*MAS_in[4]<=t141*MAS[4]

	S += t141_in*MAS_in[5]<=t141*MAS[5]

	S += t141<1000

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += MM_MEM[2]
	S += 56 < t141_mem0
	S += t141_mem0 <= t141

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	t141_mem1 += alt(MAS_MEM)
	S += (t14_t5*MAS[0])-1 < t141_mem1*MAS_MEM[1]
	S += (t14_t5*MAS[1])-1 < t141_mem1*MAS_MEM[3]
	S += (t14_t5*MAS[2])-1 < t141_mem1*MAS_MEM[5]
	S += (t14_t5*MAS[3])-1 < t141_mem1*MAS_MEM[7]
	S += (t14_t5*MAS[4])-1 < t141_mem1*MAS_MEM[9]
	S += (t14_t5*MAS[5])-1 < t141_mem1*MAS_MEM[11]
	S += t141_mem1 <= t141

	t13_t3 = S.Task('t13_t3', length=3, delay_cost=1)
	t13_t3 += alt(MAS)
	t13_t3_in = S.Task('t13_t3_in', length=1, delay_cost=1)
	t13_t3_in += alt(MAS_in)
	S += t13_t3_in*MAS_in[0]<=t13_t3*MAS[0]

	S += t13_t3_in*MAS_in[1]<=t13_t3*MAS[1]

	S += t13_t3_in*MAS_in[2]<=t13_t3*MAS[2]

	S += t13_t3_in*MAS_in[3]<=t13_t3*MAS[3]

	S += t13_t3_in*MAS_in[4]<=t13_t3*MAS[4]

	S += t13_t3_in*MAS_in[5]<=t13_t3*MAS[5]

	S += t13_t3<62

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	t13_t3_mem0 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t13_t3_mem0*MAS_MEM[0]
	S += (t120*MAS[1])-1 < t13_t3_mem0*MAS_MEM[2]
	S += (t120*MAS[2])-1 < t13_t3_mem0*MAS_MEM[4]
	S += (t120*MAS[3])-1 < t13_t3_mem0*MAS_MEM[6]
	S += (t120*MAS[4])-1 < t13_t3_mem0*MAS_MEM[8]
	S += (t120*MAS[5])-1 < t13_t3_mem0*MAS_MEM[10]
	S += t13_t3_mem0 <= t13_t3

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	t13_t3_mem1 += MAS_MEM[9]
	S += 57 < t13_t3_mem1
	S += t13_t3_mem1 <= t13_t3

	t151 = S.Task('t151', length=3, delay_cost=1)
	t151 += alt(MAS)
	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	t151_in += alt(MAS_in)
	S += t151_in*MAS_in[0]<=t151*MAS[0]

	S += t151_in*MAS_in[1]<=t151*MAS[1]

	S += t151_in*MAS_in[2]<=t151*MAS[2]

	S += t151_in*MAS_in[3]<=t151*MAS[3]

	S += t151_in*MAS_in[4]<=t151*MAS[4]

	S += t151_in*MAS_in[5]<=t151*MAS[5]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	t151_mem0 += MAS_MEM[10]
	S += 69 < t151_mem0
	S += t151_mem0 <= t151

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	t151_mem1 += alt(MAS_MEM)
	S += (t141*MAS[0])-1 < t151_mem1*MAS_MEM[1]
	S += (t141*MAS[1])-1 < t151_mem1*MAS_MEM[3]
	S += (t141*MAS[2])-1 < t151_mem1*MAS_MEM[5]
	S += (t141*MAS[3])-1 < t151_mem1*MAS_MEM[7]
	S += (t141*MAS[4])-1 < t151_mem1*MAS_MEM[9]
	S += (t141*MAS[5])-1 < t151_mem1*MAS_MEM[11]
	S += t151_mem1 <= t151

	new_TY0 = S.Task('new_TY0', length=3, delay_cost=1)
	new_TY0 += alt(MAS)
	new_TY0_in = S.Task('new_TY0_in', length=1, delay_cost=1)
	new_TY0_in += alt(MAS_in)
	S += new_TY0_in*MAS_in[0]<=new_TY0*MAS[0]

	S += new_TY0_in*MAS_in[1]<=new_TY0*MAS[1]

	S += new_TY0_in*MAS_in[2]<=new_TY0*MAS[2]

	S += new_TY0_in*MAS_in[3]<=new_TY0*MAS[3]

	S += new_TY0_in*MAS_in[4]<=new_TY0*MAS[4]

	S += new_TY0_in*MAS_in[5]<=new_TY0*MAS[5]

	S += 45<new_TY0

	new_TY0_w = S.Task('new_TY0_w', length=1, delay_cost=1)
	new_TY0_w += alt(MAIN_MEM_w)
	S += new_TY0 <= new_TY0_w

	new_TY0_mem0 = S.Task('new_TY0_mem0', length=1, delay_cost=1)
	new_TY0_mem0 += MAIN_MEM_r[0]
	S += new_TY0_mem0 <= new_TY0

	new_TY0_mem1 = S.Task('new_TY0_mem1', length=1, delay_cost=1)
	new_TY0_mem1 += MAS_MEM[5]
	S += 68 < new_TY0_mem1
	S += new_TY0_mem1 <= new_TY0

	new_TY1 = S.Task('new_TY1', length=3, delay_cost=1)
	new_TY1 += alt(MAS)
	new_TY1_in = S.Task('new_TY1_in', length=1, delay_cost=1)
	new_TY1_in += alt(MAS_in)
	S += new_TY1_in*MAS_in[0]<=new_TY1*MAS[0]

	S += new_TY1_in*MAS_in[1]<=new_TY1*MAS[1]

	S += new_TY1_in*MAS_in[2]<=new_TY1*MAS[2]

	S += new_TY1_in*MAS_in[3]<=new_TY1*MAS[3]

	S += new_TY1_in*MAS_in[4]<=new_TY1*MAS[4]

	S += new_TY1_in*MAS_in[5]<=new_TY1*MAS[5]

	S += 47<new_TY1

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
	S += new_TY1_mem1 <= new_TY1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM2_stage3MAS6/EP2_ADD_w_EVAL/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

