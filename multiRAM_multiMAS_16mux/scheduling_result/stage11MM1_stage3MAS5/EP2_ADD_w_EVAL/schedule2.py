from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 175
	S = Scenario("schedule2", horizon=horizon)

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
	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 0
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 0
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 0
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 1
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 1
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 1
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t1 = S.Task('t0_t1', length=11, delay_cost=1)
	S += t0_t1 >= 1
	t0_t1 += MM[0]

	t0_t0 = S.Task('t0_t0', length=11, delay_cost=1)
	S += t0_t0 >= 2
	t0_t0 += MM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 2
	t2_t1_in += MM_in[0]

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

	t2_t1 = S.Task('t2_t1', length=11, delay_cost=1)
	S += t2_t1 >= 3
	t2_t1 += MM[0]

	t2_t0 = S.Task('t2_t0', length=11, delay_cost=1)
	S += t2_t0 >= 4
	t2_t0 += MM[0]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 4
	t2_t2_in += MAS_in[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 4
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 4
	t2_t2_mem1 += MAIN_MEM_r[1]

	t2_t2 = S.Task('t2_t2', length=3, delay_cost=1)
	S += t2_t2 >= 5
	t2_t2 += MAS[0]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 5
	t2_t3_in += MAS_in[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 5
	t2_t3_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 5
	t2_t3_mem1 += MAIN_MEM_r[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 6
	t0_t3_in += MAS_in[2]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 6
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 6
	t0_t3_mem1 += MAIN_MEM_r[1]

	t2_t3 = S.Task('t2_t3', length=3, delay_cost=1)
	S += t2_t3 >= 6
	t2_t3 += MAS[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 7
	t0_t2_in += MAS_in[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 7
	t0_t2_mem0 += MAIN_MEM_r[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 7
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=3, delay_cost=1)
	S += t0_t3 >= 7
	t0_t3 += MAS[2]

	t0_t2 = S.Task('t0_t2', length=3, delay_cost=1)
	S += t0_t2 >= 8
	t0_t2 += MAS[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 8
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 8
	t2_t4_mem0 += MAS_MEM[0]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 8
	t2_t4_mem1 += MAS_MEM[3]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 8
	t9_t2_in += MAS_in[0]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 8
	t9_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 8
	t9_t2_mem1 += MAIN_MEM_r[1]

	t2_t4 = S.Task('t2_t4', length=11, delay_cost=1)
	S += t2_t4 >= 9
	t2_t4 += MM[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 9
	t7_t2_in += MAS_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 9
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 9
	t7_t2_mem1 += MAIN_MEM_r[1]

	t9_t2 = S.Task('t9_t2', length=3, delay_cost=1)
	S += t9_t2 >= 9
	t9_t2 += MAS[0]

	new_TZ_t2_in = S.Task('new_TZ_t2_in', length=1, delay_cost=1)
	S += new_TZ_t2_in >= 10
	new_TZ_t2_in += MAS_in[0]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 10
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 10
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 10
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 10
	t0_t4_mem0 += MAS_MEM[2]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 10
	t0_t4_mem1 += MAS_MEM[5]

	t7_t2 = S.Task('t7_t2', length=3, delay_cost=1)
	S += t7_t2 >= 10
	t7_t2 += MAS[0]

	new_TZ_t2 = S.Task('new_TZ_t2', length=3, delay_cost=1)
	S += new_TZ_t2 >= 11
	new_TZ_t2 += MAS[0]

	t0_t4 = S.Task('t0_t4', length=11, delay_cost=1)
	S += t0_t4 >= 11
	t0_t4 += MM[0]

	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	S += t17_t2_in >= 11
	t17_t2_in += MAS_in[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 11
	t17_t2_mem0 += MAIN_MEM_r[0]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 11
	t17_t2_mem1 += MAIN_MEM_r[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 12
	t00_in += MAS_in[3]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 12
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 12
	t00_mem1 += MM_MEM[1]

	t14_t2_in = S.Task('t14_t2_in', length=1, delay_cost=1)
	S += t14_t2_in >= 12
	t14_t2_in += MAS_in[0]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 12
	t14_t2_mem0 += MAIN_MEM_r[0]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 12
	t14_t2_mem1 += MAIN_MEM_r[1]

	t17_t2 = S.Task('t17_t2', length=3, delay_cost=1)
	S += t17_t2 >= 12
	t17_t2 += MAS[0]

	t00 = S.Task('t00', length=3, delay_cost=1)
	S += t00 >= 13
	t00 += MAS[3]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 13
	t0_t5_in += MAS_in[3]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 13
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 13
	t0_t5_mem1 += MM_MEM[1]

	t14_t2 = S.Task('t14_t2', length=3, delay_cost=1)
	S += t14_t2 >= 13
	t14_t2 += MAS[0]

	t16_t2_in = S.Task('t16_t2_in', length=1, delay_cost=1)
	S += t16_t2_in >= 13
	t16_t2_in += MAS_in[4]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 13
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 13
	t16_t2_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=3, delay_cost=1)
	S += t0_t5 >= 14
	t0_t5 += MAS[3]

	t16_t2 = S.Task('t16_t2', length=3, delay_cost=1)
	S += t16_t2 >= 14
	t16_t2 += MAS[4]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 14
	t20_in += MAS_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 14
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 14
	t20_mem1 += MM_MEM[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 15
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 15
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 15
	t10_mem1 += MAS_MEM[7]

	t20 = S.Task('t20', length=3, delay_cost=1)
	S += t20 >= 15
	t20 += MAS[0]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 15
	t2_t5_in += MAS_in[3]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 15
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 15
	t2_t5_mem1 += MM_MEM[1]

	t10 = S.Task('t10', length=3, delay_cost=1)
	S += t10 >= 16
	t10 += MAS[0]

	t2_t5 = S.Task('t2_t5', length=3, delay_cost=1)
	S += t2_t5 >= 16
	t2_t5 += MAS[3]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 17
	t30_in += MAS_in[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 17
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 17
	t30_mem1 += MAS_MEM[1]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 18
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 18
	c200_mem0 += MAS_MEM[0]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 18
	c200_mem1 += MAIN_MEM_r[1]

	t30 = S.Task('t30', length=3, delay_cost=1)
	S += t30 >= 18
	t30 += MAS[1]

	c200 = S.Task('c200', length=11, delay_cost=1)
	S += c200 >= 19
	c200 += MM[0]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 19
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 19
	t17_t0_mem0 += MAIN_MEM_r[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 19
	t17_t0_mem1 += MAS_MEM[1]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 19
	t21_in += MAS_in[4]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 19
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 19
	t21_mem1 += MAS_MEM[7]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 20
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 20
	c010_mem0 += MAS_MEM[2]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 20
	c010_mem1 += MAIN_MEM_r[1]

	t17_t0 = S.Task('t17_t0', length=11, delay_cost=1)
	S += t17_t0 >= 20
	t17_t0 += MM[0]

	t21 = S.Task('t21', length=3, delay_cost=1)
	S += t21 >= 20
	t21 += MAS[4]

	c010 = S.Task('c010', length=11, delay_cost=1)
	S += c010 >= 21
	c010 += MM[0]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 21
	t01_in += MAS_in[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 21
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 21
	t01_mem1 += MAS_MEM[7]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 21
	t16_t0_in += MM_in[0]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 21
	t16_t0_mem0 += MAIN_MEM_r[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 21
	t16_t0_mem1 += MAS_MEM[3]

	t01 = S.Task('t01', length=3, delay_cost=1)
	S += t01 >= 22
	t01 += MAS[0]

	t16_t0 = S.Task('t16_t0', length=11, delay_cost=1)
	S += t16_t0 >= 22
	t16_t0 += MM[0]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 22
	t31_in += MAS_in[3]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 22
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 22
	t31_mem1 += MAS_MEM[9]

	t31 = S.Task('t31', length=3, delay_cost=1)
	S += t31 >= 23
	t31 += MAS[3]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 24
	t11_in += MAS_in[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 24
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 24
	t11_mem1 += MAS_MEM[1]

	t11 = S.Task('t11', length=3, delay_cost=1)
	S += t11 >= 25
	t11 += MAS[1]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 25
	t5_t3_in += MM_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 25
	t5_t3_mem0 += MAS_MEM[2]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 25
	t5_t3_mem1 += MAS_MEM[7]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 26
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 26
	c011_mem0 += MAS_MEM[6]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 26
	c011_mem1 += MAIN_MEM_r[1]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 26
	t5_t0_in += MAS_in[2]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 26
	t5_t0_mem0 += MAS_MEM[2]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 26
	t5_t0_mem1 += MAS_MEM[7]

	t5_t3 = S.Task('t5_t3', length=11, delay_cost=1)
	S += t5_t3 >= 26
	t5_t3 += MM[0]

	c011 = S.Task('c011', length=11, delay_cost=1)
	S += c011 >= 27
	c011 += MM[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 27
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 27
	t4_t3_mem0 += MAS_MEM[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 27
	t4_t3_mem1 += MAS_MEM[3]

	t5_t0 = S.Task('t5_t0', length=3, delay_cost=1)
	S += t5_t0 >= 27
	t5_t0 += MAS[2]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 27
	t5_t1_in += MAS_in[4]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 27
	t5_t1_mem0 += MAS_MEM[2]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 27
	t5_t1_mem1 += MAS_MEM[7]

	t16_t3_in = S.Task('t16_t3_in', length=1, delay_cost=1)
	S += t16_t3_in >= 28
	t16_t3_in += MAS_in[2]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 28
	t16_t3_mem0 += MAS_MEM[2]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 28
	t16_t3_mem1 += MAS_MEM[7]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 28
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 28
	t17_t1_mem0 += MAIN_MEM_r[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 28
	t17_t1_mem1 += MAS_MEM[3]

	t4_t3 = S.Task('t4_t3', length=11, delay_cost=1)
	S += t4_t3 >= 28
	t4_t3 += MM[0]

	t5_t1 = S.Task('t5_t1', length=3, delay_cost=1)
	S += t5_t1 >= 28
	t5_t1 += MAS[4]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 29
	t16_t1_in += MM_in[0]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 29
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 29
	t16_t1_mem1 += MAS_MEM[7]

	t16_t3 = S.Task('t16_t3', length=3, delay_cost=1)
	S += t16_t3 >= 29
	t16_t3 += MAS[2]

	t17_t1 = S.Task('t17_t1', length=11, delay_cost=1)
	S += t17_t1 >= 29
	t17_t1 += MM[0]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 29
	t4_t1_in += MAS_in[3]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 29
	t4_t1_mem0 += MAS_MEM[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 29
	t4_t1_mem1 += MAS_MEM[3]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 30
	c200_w += MAIN_MEM_w

	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	S += new_TX_t2_in >= 30
	new_TX_t2_in += MAS_in[1]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 30
	new_TX_t2_mem0 += MAS_MEM[2]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 30
	new_TX_t2_mem1 += MAS_MEM[7]

	t16_t1 = S.Task('t16_t1', length=11, delay_cost=1)
	S += t16_t1 >= 30
	t16_t1 += MM[0]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 30
	t4_t0_in += MAS_in[0]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 30
	t4_t0_mem0 += MAS_MEM[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 30
	t4_t0_mem1 += MAS_MEM[3]

	t4_t1 = S.Task('t4_t1', length=3, delay_cost=1)
	S += t4_t1 >= 30
	t4_t1 += MAS[3]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 30
	t5_t2_in += MM_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 30
	t5_t2_mem0 += MAS_MEM[4]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 30
	t5_t2_mem1 += MAS_MEM[9]

	new_TX_t2 = S.Task('new_TX_t2', length=3, delay_cost=1)
	S += new_TX_t2 >= 31
	new_TX_t2 += MAS[1]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 31
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 31
	t16_t4_mem0 += MAS_MEM[8]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 31
	t16_t4_mem1 += MAS_MEM[5]

	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	S += t17_t3_in >= 31
	t17_t3_in += MAS_in[3]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 31
	t17_t3_mem0 += MAS_MEM[0]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 31
	t17_t3_mem1 += MAS_MEM[3]

	t4_t0 = S.Task('t4_t0', length=3, delay_cost=1)
	S += t4_t0 >= 31
	t4_t0 += MAS[0]

	t5_t2 = S.Task('t5_t2', length=11, delay_cost=1)
	S += t5_t2 >= 31
	t5_t2 += MM[0]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 31
	t6_t2_in += MAS_in[2]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 31
	t6_t2_mem0 += MAS_MEM[2]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 31
	t6_t2_mem1 += MAS_MEM[7]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 32
	c010_w += MAIN_MEM_w

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 32
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 32
	c201_mem0 += MAS_MEM[2]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 32
	c201_mem1 += MAIN_MEM_r[1]

	t13_t2_in = S.Task('t13_t2_in', length=1, delay_cost=1)
	S += t13_t2_in >= 32
	t13_t2_in += MAS_in[3]

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 32
	t13_t2_mem0 += MAS_MEM[0]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 32
	t13_t2_mem1 += MAS_MEM[3]

	t16_t4 = S.Task('t16_t4', length=11, delay_cost=1)
	S += t16_t4 >= 32
	t16_t4 += MM[0]

	t17_t3 = S.Task('t17_t3', length=3, delay_cost=1)
	S += t17_t3 >= 32
	t17_t3 += MAS[3]

	t6_t2 = S.Task('t6_t2', length=3, delay_cost=1)
	S += t6_t2 >= 32
	t6_t2 += MAS[2]

	c201 = S.Task('c201', length=11, delay_cost=1)
	S += c201 >= 33
	c201 += MM[0]

	t13_t2 = S.Task('t13_t2', length=3, delay_cost=1)
	S += t13_t2 >= 33
	t13_t2 += MAS[3]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 33
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 33
	t4_t2_mem0 += MAS_MEM[0]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 33
	t4_t2_mem1 += MAS_MEM[7]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 34
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 34
	t17_t4_mem0 += MAS_MEM[0]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 34
	t17_t4_mem1 += MAS_MEM[7]

	t4_t2 = S.Task('t4_t2', length=11, delay_cost=1)
	S += t4_t2 >= 34
	t4_t2 += MM[0]

	t17_t4 = S.Task('t17_t4', length=11, delay_cost=1)
	S += t17_t4 >= 35
	t17_t4 += MM[0]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 36
	t51_in += MAS_in[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 36
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 36
	t51_mem1 += MM_MEM[1]

	t51 = S.Task('t51', length=3, delay_cost=1)
	S += t51 >= 37
	t51 += MAS[1]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 37
	t5_t5_in += MAS_in[3]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 37
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 37
	t5_t5_mem1 += MM_MEM[1]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 38
	c011_w += MAIN_MEM_w

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 38
	t41_in += MAS_in[2]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 38
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 38
	t41_mem1 += MM_MEM[1]

	t5_t5 = S.Task('t5_t5', length=3, delay_cost=1)
	S += t5_t5 >= 38
	t5_t5 += MAS[3]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 39
	t170_in += MAS_in[4]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 39
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 39
	t170_mem1 += MM_MEM[1]

	t41 = S.Task('t41', length=3, delay_cost=1)
	S += t41 >= 39
	t41 += MAS[2]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 39
	t9_t1_in += MM_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 39
	t9_t1_mem0 += MAIN_MEM_r[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 39
	t9_t1_mem1 += MAS_MEM[3]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 40
	t160_in += MAS_in[2]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 40
	t160_mem0 += MM_MEM[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 40
	t160_mem1 += MM_MEM[1]

	t170 = S.Task('t170', length=3, delay_cost=1)
	S += t170 >= 40
	t170 += MAS[4]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 40
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 40
	t6_t1_mem0 += MAS_MEM[6]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 40
	t6_t1_mem1 += MAS_MEM[3]

	t9_t1 = S.Task('t9_t1', length=11, delay_cost=1)
	S += t9_t1 >= 40
	t9_t1 += MM[0]

	t160 = S.Task('t160', length=3, delay_cost=1)
	S += t160 >= 41
	t160 += MAS[2]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 41
	t50_in += MAS_in[2]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 41
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 41
	t50_mem1 += MAS_MEM[7]

	t6_t1 = S.Task('t6_t1', length=11, delay_cost=1)
	S += t6_t1 >= 41
	t6_t1 += MM[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 41
	t7_t1_in += MM_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 41
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 41
	t7_t1_mem1 += MAS_MEM[5]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 42
	t4_t5_in += MAS_in[4]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 42
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 42
	t4_t5_mem1 += MM_MEM[1]

	t50 = S.Task('t50', length=3, delay_cost=1)
	S += t50 >= 42
	t50 += MAS[2]

	t7_t1 = S.Task('t7_t1', length=11, delay_cost=1)
	S += t7_t1 >= 42
	t7_t1 += MM[0]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 43
	c000_in += MAS_in[0]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 43
	c000_mem0 += MAS_MEM[4]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 43
	c000_mem1 += MAS_MEM[9]

	t16_t5_in = S.Task('t16_t5_in', length=1, delay_cost=1)
	S += t16_t5_in >= 43
	t16_t5_in += MAS_in[1]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 43
	t16_t5_mem0 += MM_MEM[0]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 43
	t16_t5_mem1 += MM_MEM[1]

	t4_t5 = S.Task('t4_t5', length=3, delay_cost=1)
	S += t4_t5 >= 43
	t4_t5 += MAS[4]

	c000 = S.Task('c000', length=3, delay_cost=1)
	S += c000 >= 44
	c000 += MAS[0]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 44
	c201_w += MAIN_MEM_w

	t16_t5 = S.Task('t16_t5', length=3, delay_cost=1)
	S += t16_t5 >= 44
	t16_t5 += MAS[1]

	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	S += t17_t5_in >= 44
	t17_t5_in += MAS_in[3]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 44
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 44
	t17_t5_mem1 += MM_MEM[1]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 44
	t9_t0_in += MM_in[0]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 44
	t9_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 44
	t9_t0_mem1 += MAS_MEM[5]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 44
	t9_t3_in += MAS_in[4]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 44
	t9_t3_mem0 += MAS_MEM[4]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 44
	t9_t3_mem1 += MAS_MEM[3]

	t17_t5 = S.Task('t17_t5', length=3, delay_cost=1)
	S += t17_t5 >= 45
	t17_t5 += MAS[3]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 45
	t40_in += MAS_in[0]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 45
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 45
	t40_mem1 += MAS_MEM[9]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 45
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 45
	t6_t0_mem0 += MAS_MEM[2]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 45
	t6_t0_mem1 += MAS_MEM[5]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 45
	t6_t3_in += MAS_in[2]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 45
	t6_t3_mem0 += MAS_MEM[4]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 45
	t6_t3_mem1 += MAS_MEM[3]

	t9_t0 = S.Task('t9_t0', length=11, delay_cost=1)
	S += t9_t0 >= 45
	t9_t0 += MM[0]

	t9_t3 = S.Task('t9_t3', length=3, delay_cost=1)
	S += t9_t3 >= 45
	t9_t3 += MAS[4]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 46
	t161_in += MAS_in[2]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 46
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 46
	t161_mem1 += MAS_MEM[3]

	t40 = S.Task('t40', length=3, delay_cost=1)
	S += t40 >= 46
	t40 += MAS[0]

	t6_t0 = S.Task('t6_t0', length=11, delay_cost=1)
	S += t6_t0 >= 46
	t6_t0 += MM[0]

	t6_t3 = S.Task('t6_t3', length=3, delay_cost=1)
	S += t6_t3 >= 46
	t6_t3 += MAS[2]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 47
	c000_w += MAIN_MEM_w

	t161 = S.Task('t161', length=3, delay_cost=1)
	S += t161 >= 47
	t161 += MAS[2]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 47
	t171_in += MAS_in[1]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 47
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 47
	t171_mem1 += MAS_MEM[7]

	t171 = S.Task('t171', length=3, delay_cost=1)
	S += t171 >= 48
	t171 += MAS[1]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 48
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 48
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 48
	t7_t0_mem1 += MAS_MEM[1]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 48
	t7_t3_in += MAS_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 48
	t7_t3_mem0 += MAS_MEM[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 48
	t7_t3_mem1 += MAS_MEM[5]

	t7_t0 = S.Task('t7_t0', length=11, delay_cost=1)
	S += t7_t0 >= 49
	t7_t0 += MM[0]

	t7_t3 = S.Task('t7_t3', length=3, delay_cost=1)
	S += t7_t3 >= 49
	t7_t3 += MAS[0]

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 50
	c001_in += MAS_in[3]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 50
	c001_mem0 += MAS_MEM[4]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 50
	c001_mem1 += MAS_MEM[3]

	c001 = S.Task('c001', length=3, delay_cost=1)
	S += c001 >= 51
	c001 += MAS[3]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 54
	c001_w += MAIN_MEM_w


	# new tasks
	t6_t4 = S.Task('t6_t4', length=11, delay_cost=1)
	t6_t4 += alt(MM)
	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	t6_t4_in += alt(MM_in)
	S += t6_t4_in*MM_in[0]<=t6_t4*MM[0]
	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	t6_t4_mem0 += MAS_MEM[4]
	S += 34 < t6_t4_mem0
	S += t6_t4_mem0 <= t6_t4

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	t6_t4_mem1 += MAS_MEM[5]
	S += 48 < t6_t4_mem1
	S += t6_t4_mem1 <= t6_t4

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
	t60_mem0 += MM_MEM[0]
	S += 56 < t60_mem0
	S += t60_mem0 <= t60

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	t60_mem1 += MM_MEM[1]
	S += 51 < t60_mem1
	S += t60_mem1 <= t60

	t6_t5 = S.Task('t6_t5', length=3, delay_cost=1)
	t6_t5 += alt(MAS)
	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	t6_t5_in += alt(MAS_in)
	S += t6_t5_in*MAS_in[0]<=t6_t5*MAS[0]

	S += t6_t5_in*MAS_in[1]<=t6_t5*MAS[1]

	S += t6_t5_in*MAS_in[2]<=t6_t5*MAS[2]

	S += t6_t5_in*MAS_in[3]<=t6_t5*MAS[3]

	S += t6_t5_in*MAS_in[4]<=t6_t5*MAS[4]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	t6_t5_mem0 += MM_MEM[0]
	S += 56 < t6_t5_mem0
	S += t6_t5_mem0 <= t6_t5

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	t6_t5_mem1 += MM_MEM[1]
	S += 51 < t6_t5_mem1
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
	S += 51 < t7_t4_mem1
	S += t7_t4_mem1 <= t7_t4

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
	t70_mem0 += MM_MEM[0]
	S += 59 < t70_mem0
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += MM_MEM[1]
	S += 52 < t70_mem1
	S += t70_mem1 <= t70

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
	S += 59 < t7_t5_mem0
	S += t7_t5_mem0 <= t7_t5

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	t7_t5_mem1 += MM_MEM[1]
	S += 52 < t7_t5_mem1
	S += t7_t5_mem1 <= t7_t5

	t9_t4 = S.Task('t9_t4', length=11, delay_cost=1)
	t9_t4 += alt(MM)
	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	t9_t4_in += alt(MM_in)
	S += t9_t4_in*MM_in[0]<=t9_t4*MM[0]
	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	t9_t4_mem0 += MAS_MEM[0]
	S += 11 < t9_t4_mem0
	S += t9_t4_mem0 <= t9_t4

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	t9_t4_mem1 += MAS_MEM[9]
	S += 47 < t9_t4_mem1
	S += t9_t4_mem1 <= t9_t4

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
	t90_mem0 += MM_MEM[0]
	S += 55 < t90_mem0
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += MM_MEM[1]
	S += 50 < t90_mem1
	S += t90_mem1 <= t90

	t9_t5 = S.Task('t9_t5', length=3, delay_cost=1)
	t9_t5 += alt(MAS)
	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	t9_t5_in += alt(MAS_in)
	S += t9_t5_in*MAS_in[0]<=t9_t5*MAS[0]

	S += t9_t5_in*MAS_in[1]<=t9_t5*MAS[1]

	S += t9_t5_in*MAS_in[2]<=t9_t5*MAS[2]

	S += t9_t5_in*MAS_in[3]<=t9_t5*MAS[3]

	S += t9_t5_in*MAS_in[4]<=t9_t5*MAS[4]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	t9_t5_mem0 += MM_MEM[0]
	S += 55 < t9_t5_mem0
	S += t9_t5_mem0 <= t9_t5

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	t9_t5_mem1 += MM_MEM[1]
	S += 50 < t9_t5_mem1
	S += t9_t5_mem1 <= t9_t5

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
	t61_mem0 += alt(MM_MEM)
	S += (t6_t4*MM[0])-1 < t61_mem0*MM_MEM[0]
	S += t61_mem0 <= t61

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	t61_mem1 += alt(MAS_MEM)
	S += (t6_t5*MAS[0])-1 < t61_mem1*MAS_MEM[1]
	S += (t6_t5*MAS[1])-1 < t61_mem1*MAS_MEM[3]
	S += (t6_t5*MAS[2])-1 < t61_mem1*MAS_MEM[5]
	S += (t6_t5*MAS[3])-1 < t61_mem1*MAS_MEM[7]
	S += (t6_t5*MAS[4])-1 < t61_mem1*MAS_MEM[9]
	S += t61_mem1 <= t61

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
	t71_mem0 += alt(MM_MEM)
	S += (t7_t4*MM[0])-1 < t71_mem0*MM_MEM[0]
	S += t71_mem0 <= t71

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	t71_mem1 += alt(MAS_MEM)
	S += (t7_t5*MAS[0])-1 < t71_mem1*MAS_MEM[1]
	S += (t7_t5*MAS[1])-1 < t71_mem1*MAS_MEM[3]
	S += (t7_t5*MAS[2])-1 < t71_mem1*MAS_MEM[5]
	S += (t7_t5*MAS[3])-1 < t71_mem1*MAS_MEM[7]
	S += (t7_t5*MAS[4])-1 < t71_mem1*MAS_MEM[9]
	S += t71_mem1 <= t71

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
	S += (t60*MAS[0])-1 < t80_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < t80_mem0*MAS_MEM[2]
	S += (t60*MAS[2])-1 < t80_mem0*MAS_MEM[4]
	S += (t60*MAS[3])-1 < t80_mem0*MAS_MEM[6]
	S += (t60*MAS[4])-1 < t80_mem0*MAS_MEM[8]
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
	t91_mem0 += alt(MM_MEM)
	S += (t9_t4*MM[0])-1 < t91_mem0*MM_MEM[0]
	S += t91_mem0 <= t91

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	t91_mem1 += alt(MAS_MEM)
	S += (t9_t5*MAS[0])-1 < t91_mem1*MAS_MEM[1]
	S += (t9_t5*MAS[1])-1 < t91_mem1*MAS_MEM[3]
	S += (t9_t5*MAS[2])-1 < t91_mem1*MAS_MEM[5]
	S += (t9_t5*MAS[3])-1 < t91_mem1*MAS_MEM[7]
	S += (t9_t5*MAS[4])-1 < t91_mem1*MAS_MEM[9]
	S += t91_mem1 <= t91

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
	t100_mem0 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t100_mem0*MAS_MEM[0]
	S += (t90*MAS[1])-1 < t100_mem0*MAS_MEM[2]
	S += (t90*MAS[2])-1 < t100_mem0*MAS_MEM[4]
	S += (t90*MAS[3])-1 < t100_mem0*MAS_MEM[6]
	S += (t90*MAS[4])-1 < t100_mem0*MAS_MEM[8]
	S += t100_mem0 <= t100

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	t100_mem1 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t100_mem1*MAS_MEM[1]
	S += (t90*MAS[1])-1 < t100_mem1*MAS_MEM[3]
	S += (t90*MAS[2])-1 < t100_mem1*MAS_MEM[5]
	S += (t90*MAS[3])-1 < t100_mem1*MAS_MEM[7]
	S += (t90*MAS[4])-1 < t100_mem1*MAS_MEM[9]
	S += t100_mem1 <= t100

	t14_t0 = S.Task('t14_t0', length=11, delay_cost=1)
	t14_t0 += alt(MM)
	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	t14_t0_in += alt(MM_in)
	S += t14_t0_in*MM_in[0]<=t14_t0*MM[0]
	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	t14_t0_mem0 += MAIN_MEM_r[0]
	S += t14_t0_mem0 <= t14_t0

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	t14_t0_mem1 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t14_t0_mem1*MAS_MEM[1]
	S += (t60*MAS[1])-1 < t14_t0_mem1*MAS_MEM[3]
	S += (t60*MAS[2])-1 < t14_t0_mem1*MAS_MEM[5]
	S += (t60*MAS[3])-1 < t14_t0_mem1*MAS_MEM[7]
	S += (t60*MAS[4])-1 < t14_t0_mem1*MAS_MEM[9]
	S += t14_t0_mem1 <= t14_t0

	new_TZ_t0 = S.Task('new_TZ_t0', length=11, delay_cost=1)
	new_TZ_t0 += alt(MM)
	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	new_TZ_t0_in += alt(MM_in)
	S += new_TZ_t0_in*MM_in[0]<=new_TZ_t0*MM[0]
	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	new_TZ_t0_mem0 += MAIN_MEM_r[0]
	S += new_TZ_t0_mem0 <= new_TZ_t0

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	new_TZ_t0_mem1 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < new_TZ_t0_mem1*MAS_MEM[1]
	S += (t60*MAS[1])-1 < new_TZ_t0_mem1*MAS_MEM[3]
	S += (t60*MAS[2])-1 < new_TZ_t0_mem1*MAS_MEM[5]
	S += (t60*MAS[3])-1 < new_TZ_t0_mem1*MAS_MEM[7]
	S += (t60*MAS[4])-1 < new_TZ_t0_mem1*MAS_MEM[9]
	S += new_TZ_t0_mem1 <= new_TZ_t0

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
	S += (t61*MAS[0])-1 < t81_mem0*MAS_MEM[0]
	S += (t61*MAS[1])-1 < t81_mem0*MAS_MEM[2]
	S += (t61*MAS[2])-1 < t81_mem0*MAS_MEM[4]
	S += (t61*MAS[3])-1 < t81_mem0*MAS_MEM[6]
	S += (t61*MAS[4])-1 < t81_mem0*MAS_MEM[8]
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
	t101_mem0 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < t101_mem0*MAS_MEM[0]
	S += (t91*MAS[1])-1 < t101_mem0*MAS_MEM[2]
	S += (t91*MAS[2])-1 < t101_mem0*MAS_MEM[4]
	S += (t91*MAS[3])-1 < t101_mem0*MAS_MEM[6]
	S += (t91*MAS[4])-1 < t101_mem0*MAS_MEM[8]
	S += t101_mem0 <= t101

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	t101_mem1 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < t101_mem1*MAS_MEM[1]
	S += (t91*MAS[1])-1 < t101_mem1*MAS_MEM[3]
	S += (t91*MAS[2])-1 < t101_mem1*MAS_MEM[5]
	S += (t91*MAS[3])-1 < t101_mem1*MAS_MEM[7]
	S += (t91*MAS[4])-1 < t101_mem1*MAS_MEM[9]
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
	S += (t80*MAS[0])-1 < t110_mem0*MAS_MEM[0]
	S += (t80*MAS[1])-1 < t110_mem0*MAS_MEM[2]
	S += (t80*MAS[2])-1 < t110_mem0*MAS_MEM[4]
	S += (t80*MAS[3])-1 < t110_mem0*MAS_MEM[6]
	S += (t80*MAS[4])-1 < t110_mem0*MAS_MEM[8]
	S += t110_mem0 <= t110

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	t110_mem1 += alt(MAS_MEM)
	S += (t100*MAS[0])-1 < t110_mem1*MAS_MEM[1]
	S += (t100*MAS[1])-1 < t110_mem1*MAS_MEM[3]
	S += (t100*MAS[2])-1 < t110_mem1*MAS_MEM[5]
	S += (t100*MAS[3])-1 < t110_mem1*MAS_MEM[7]
	S += (t100*MAS[4])-1 < t110_mem1*MAS_MEM[9]
	S += t110_mem1 <= t110

	t14_t1 = S.Task('t14_t1', length=11, delay_cost=1)
	t14_t1 += alt(MM)
	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	t14_t1_in += alt(MM_in)
	S += t14_t1_in*MM_in[0]<=t14_t1*MM[0]
	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	t14_t1_mem0 += MAIN_MEM_r[0]
	S += t14_t1_mem0 <= t14_t1

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	t14_t1_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < t14_t1_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < t14_t1_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < t14_t1_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < t14_t1_mem1*MAS_MEM[7]
	S += (t61*MAS[4])-1 < t14_t1_mem1*MAS_MEM[9]
	S += t14_t1_mem1 <= t14_t1

	t14_t3 = S.Task('t14_t3', length=3, delay_cost=1)
	t14_t3 += alt(MAS)
	t14_t3_in = S.Task('t14_t3_in', length=1, delay_cost=1)
	t14_t3_in += alt(MAS_in)
	S += t14_t3_in*MAS_in[0]<=t14_t3*MAS[0]

	S += t14_t3_in*MAS_in[1]<=t14_t3*MAS[1]

	S += t14_t3_in*MAS_in[2]<=t14_t3*MAS[2]

	S += t14_t3_in*MAS_in[3]<=t14_t3*MAS[3]

	S += t14_t3_in*MAS_in[4]<=t14_t3*MAS[4]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	t14_t3_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t14_t3_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < t14_t3_mem0*MAS_MEM[2]
	S += (t60*MAS[2])-1 < t14_t3_mem0*MAS_MEM[4]
	S += (t60*MAS[3])-1 < t14_t3_mem0*MAS_MEM[6]
	S += (t60*MAS[4])-1 < t14_t3_mem0*MAS_MEM[8]
	S += t14_t3_mem0 <= t14_t3

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	t14_t3_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < t14_t3_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < t14_t3_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < t14_t3_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < t14_t3_mem1*MAS_MEM[7]
	S += (t61*MAS[4])-1 < t14_t3_mem1*MAS_MEM[9]
	S += t14_t3_mem1 <= t14_t3

	new_TZ_t1 = S.Task('new_TZ_t1', length=11, delay_cost=1)
	new_TZ_t1 += alt(MM)
	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	new_TZ_t1_in += alt(MM_in)
	S += new_TZ_t1_in*MM_in[0]<=new_TZ_t1*MM[0]
	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	new_TZ_t1_mem0 += MAIN_MEM_r[0]
	S += new_TZ_t1_mem0 <= new_TZ_t1

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	new_TZ_t1_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < new_TZ_t1_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < new_TZ_t1_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < new_TZ_t1_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < new_TZ_t1_mem1*MAS_MEM[7]
	S += (t61*MAS[4])-1 < new_TZ_t1_mem1*MAS_MEM[9]
	S += new_TZ_t1_mem1 <= new_TZ_t1

	new_TZ_t3 = S.Task('new_TZ_t3', length=3, delay_cost=1)
	new_TZ_t3 += alt(MAS)
	new_TZ_t3_in = S.Task('new_TZ_t3_in', length=1, delay_cost=1)
	new_TZ_t3_in += alt(MAS_in)
	S += new_TZ_t3_in*MAS_in[0]<=new_TZ_t3*MAS[0]

	S += new_TZ_t3_in*MAS_in[1]<=new_TZ_t3*MAS[1]

	S += new_TZ_t3_in*MAS_in[2]<=new_TZ_t3*MAS[2]

	S += new_TZ_t3_in*MAS_in[3]<=new_TZ_t3*MAS[3]

	S += new_TZ_t3_in*MAS_in[4]<=new_TZ_t3*MAS[4]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	new_TZ_t3_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < new_TZ_t3_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < new_TZ_t3_mem0*MAS_MEM[2]
	S += (t60*MAS[2])-1 < new_TZ_t3_mem0*MAS_MEM[4]
	S += (t60*MAS[3])-1 < new_TZ_t3_mem0*MAS_MEM[6]
	S += (t60*MAS[4])-1 < new_TZ_t3_mem0*MAS_MEM[8]
	S += new_TZ_t3_mem0 <= new_TZ_t3

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	new_TZ_t3_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < new_TZ_t3_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < new_TZ_t3_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < new_TZ_t3_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < new_TZ_t3_mem1*MAS_MEM[7]
	S += (t61*MAS[4])-1 < new_TZ_t3_mem1*MAS_MEM[9]
	S += new_TZ_t3_mem1 <= new_TZ_t3

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
	S += (t81*MAS[0])-1 < t111_mem0*MAS_MEM[0]
	S += (t81*MAS[1])-1 < t111_mem0*MAS_MEM[2]
	S += (t81*MAS[2])-1 < t111_mem0*MAS_MEM[4]
	S += (t81*MAS[3])-1 < t111_mem0*MAS_MEM[6]
	S += (t81*MAS[4])-1 < t111_mem0*MAS_MEM[8]
	S += t111_mem0 <= t111

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	t111_mem1 += alt(MAS_MEM)
	S += (t101*MAS[0])-1 < t111_mem1*MAS_MEM[1]
	S += (t101*MAS[1])-1 < t111_mem1*MAS_MEM[3]
	S += (t101*MAS[2])-1 < t111_mem1*MAS_MEM[5]
	S += (t101*MAS[3])-1 < t111_mem1*MAS_MEM[7]
	S += (t101*MAS[4])-1 < t111_mem1*MAS_MEM[9]
	S += t111_mem1 <= t111

	t120 = S.Task('t120', length=3, delay_cost=1)
	t120 += alt(MAS)
	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	t120_in += alt(MAS_in)
	S += t120_in*MAS_in[0]<=t120*MAS[0]

	S += t120_in*MAS_in[1]<=t120*MAS[1]

	S += t120_in*MAS_in[2]<=t120*MAS[2]

	S += t120_in*MAS_in[3]<=t120*MAS[3]

	S += t120_in*MAS_in[4]<=t120*MAS[4]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < t120_mem0*MAS_MEM[0]
	S += (t110*MAS[1])-1 < t120_mem0*MAS_MEM[2]
	S += (t110*MAS[2])-1 < t120_mem0*MAS_MEM[4]
	S += (t110*MAS[3])-1 < t120_mem0*MAS_MEM[6]
	S += (t110*MAS[4])-1 < t120_mem0*MAS_MEM[8]
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t120_mem1*MAS_MEM[1]
	S += (t90*MAS[1])-1 < t120_mem1*MAS_MEM[3]
	S += (t90*MAS[2])-1 < t120_mem1*MAS_MEM[5]
	S += (t90*MAS[3])-1 < t120_mem1*MAS_MEM[7]
	S += (t90*MAS[4])-1 < t120_mem1*MAS_MEM[9]
	S += t120_mem1 <= t120

	new_TX_t0 = S.Task('new_TX_t0', length=11, delay_cost=1)
	new_TX_t0 += alt(MM)
	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	new_TX_t0_in += alt(MM_in)
	S += new_TX_t0_in*MM_in[0]<=new_TX_t0*MM[0]
	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	new_TX_t0_mem0 += MAS_MEM[2]
	S += 20 < new_TX_t0_mem0
	S += new_TX_t0_mem0 <= new_TX_t0

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	new_TX_t0_mem1 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < new_TX_t0_mem1*MAS_MEM[1]
	S += (t110*MAS[1])-1 < new_TX_t0_mem1*MAS_MEM[3]
	S += (t110*MAS[2])-1 < new_TX_t0_mem1*MAS_MEM[5]
	S += (t110*MAS[3])-1 < new_TX_t0_mem1*MAS_MEM[7]
	S += (t110*MAS[4])-1 < new_TX_t0_mem1*MAS_MEM[9]
	S += new_TX_t0_mem1 <= new_TX_t0

	t14_t4 = S.Task('t14_t4', length=11, delay_cost=1)
	t14_t4 += alt(MM)
	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	t14_t4_in += alt(MM_in)
	S += t14_t4_in*MM_in[0]<=t14_t4*MM[0]
	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	t14_t4_mem0 += MAS_MEM[0]
	S += 15 < t14_t4_mem0
	S += t14_t4_mem0 <= t14_t4

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	t14_t4_mem1 += alt(MAS_MEM)
	S += (t14_t3*MAS[0])-1 < t14_t4_mem1*MAS_MEM[1]
	S += (t14_t3*MAS[1])-1 < t14_t4_mem1*MAS_MEM[3]
	S += (t14_t3*MAS[2])-1 < t14_t4_mem1*MAS_MEM[5]
	S += (t14_t3*MAS[3])-1 < t14_t4_mem1*MAS_MEM[7]
	S += (t14_t3*MAS[4])-1 < t14_t4_mem1*MAS_MEM[9]
	S += t14_t4_mem1 <= t14_t4

	t140 = S.Task('t140', length=3, delay_cost=1)
	t140 += alt(MAS)
	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	t140_in += alt(MAS_in)
	S += t140_in*MAS_in[0]<=t140*MAS[0]

	S += t140_in*MAS_in[1]<=t140*MAS[1]

	S += t140_in*MAS_in[2]<=t140*MAS[2]

	S += t140_in*MAS_in[3]<=t140*MAS[3]

	S += t140_in*MAS_in[4]<=t140*MAS[4]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(MM_MEM)
	S += (t14_t0*MM[0])-1 < t140_mem0*MM_MEM[0]
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += alt(MM_MEM)
	S += (t14_t1*MM[0])-1 < t140_mem1*MM_MEM[1]
	S += t140_mem1 <= t140

	t14_t5 = S.Task('t14_t5', length=3, delay_cost=1)
	t14_t5 += alt(MAS)
	t14_t5_in = S.Task('t14_t5_in', length=1, delay_cost=1)
	t14_t5_in += alt(MAS_in)
	S += t14_t5_in*MAS_in[0]<=t14_t5*MAS[0]

	S += t14_t5_in*MAS_in[1]<=t14_t5*MAS[1]

	S += t14_t5_in*MAS_in[2]<=t14_t5*MAS[2]

	S += t14_t5_in*MAS_in[3]<=t14_t5*MAS[3]

	S += t14_t5_in*MAS_in[4]<=t14_t5*MAS[4]

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	t14_t5_mem0 += alt(MM_MEM)
	S += (t14_t0*MM[0])-1 < t14_t5_mem0*MM_MEM[0]
	S += t14_t5_mem0 <= t14_t5

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	t14_t5_mem1 += alt(MM_MEM)
	S += (t14_t1*MM[0])-1 < t14_t5_mem1*MM_MEM[1]
	S += t14_t5_mem1 <= t14_t5

	new_TZ_t4 = S.Task('new_TZ_t4', length=11, delay_cost=1)
	new_TZ_t4 += alt(MM)
	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	new_TZ_t4_in += alt(MM_in)
	S += new_TZ_t4_in*MM_in[0]<=new_TZ_t4*MM[0]
	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	new_TZ_t4_mem0 += MAS_MEM[0]
	S += 13 < new_TZ_t4_mem0
	S += new_TZ_t4_mem0 <= new_TZ_t4

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	new_TZ_t4_mem1 += alt(MAS_MEM)
	S += (new_TZ_t3*MAS[0])-1 < new_TZ_t4_mem1*MAS_MEM[1]
	S += (new_TZ_t3*MAS[1])-1 < new_TZ_t4_mem1*MAS_MEM[3]
	S += (new_TZ_t3*MAS[2])-1 < new_TZ_t4_mem1*MAS_MEM[5]
	S += (new_TZ_t3*MAS[3])-1 < new_TZ_t4_mem1*MAS_MEM[7]
	S += (new_TZ_t3*MAS[4])-1 < new_TZ_t4_mem1*MAS_MEM[9]
	S += new_TZ_t4_mem1 <= new_TZ_t4

	new_TZ0 = S.Task('new_TZ0', length=3, delay_cost=1)
	new_TZ0 += alt(MAS)
	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	new_TZ0_in += alt(MAS_in)
	S += new_TZ0_in*MAS_in[0]<=new_TZ0*MAS[0]

	S += new_TZ0_in*MAS_in[1]<=new_TZ0*MAS[1]

	S += new_TZ0_in*MAS_in[2]<=new_TZ0*MAS[2]

	S += new_TZ0_in*MAS_in[3]<=new_TZ0*MAS[3]

	S += new_TZ0_in*MAS_in[4]<=new_TZ0*MAS[4]

	S += 49<new_TZ0

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	new_TZ0_w += alt(MAIN_MEM_w)
	S += new_TZ0 <= new_TZ0_w

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	new_TZ0_mem0 += alt(MM_MEM)
	S += (new_TZ_t0*MM[0])-1 < new_TZ0_mem0*MM_MEM[0]
	S += new_TZ0_mem0 <= new_TZ0

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	new_TZ0_mem1 += alt(MM_MEM)
	S += (new_TZ_t1*MM[0])-1 < new_TZ0_mem1*MM_MEM[1]
	S += new_TZ0_mem1 <= new_TZ0

	new_TZ_t5 = S.Task('new_TZ_t5', length=3, delay_cost=1)
	new_TZ_t5 += alt(MAS)
	new_TZ_t5_in = S.Task('new_TZ_t5_in', length=1, delay_cost=1)
	new_TZ_t5_in += alt(MAS_in)
	S += new_TZ_t5_in*MAS_in[0]<=new_TZ_t5*MAS[0]

	S += new_TZ_t5_in*MAS_in[1]<=new_TZ_t5*MAS[1]

	S += new_TZ_t5_in*MAS_in[2]<=new_TZ_t5*MAS[2]

	S += new_TZ_t5_in*MAS_in[3]<=new_TZ_t5*MAS[3]

	S += new_TZ_t5_in*MAS_in[4]<=new_TZ_t5*MAS[4]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	new_TZ_t5_mem0 += alt(MM_MEM)
	S += (new_TZ_t0*MM[0])-1 < new_TZ_t5_mem0*MM_MEM[0]
	S += new_TZ_t5_mem0 <= new_TZ_t5

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	new_TZ_t5_mem1 += alt(MM_MEM)
	S += (new_TZ_t1*MM[0])-1 < new_TZ_t5_mem1*MM_MEM[1]
	S += new_TZ_t5_mem1 <= new_TZ_t5

	t121 = S.Task('t121', length=3, delay_cost=1)
	t121 += alt(MAS)
	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	t121_in += alt(MAS_in)
	S += t121_in*MAS_in[0]<=t121*MAS[0]

	S += t121_in*MAS_in[1]<=t121*MAS[1]

	S += t121_in*MAS_in[2]<=t121*MAS[2]

	S += t121_in*MAS_in[3]<=t121*MAS[3]

	S += t121_in*MAS_in[4]<=t121*MAS[4]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	t121_mem0 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < t121_mem0*MAS_MEM[0]
	S += (t111*MAS[1])-1 < t121_mem0*MAS_MEM[2]
	S += (t111*MAS[2])-1 < t121_mem0*MAS_MEM[4]
	S += (t111*MAS[3])-1 < t121_mem0*MAS_MEM[6]
	S += (t111*MAS[4])-1 < t121_mem0*MAS_MEM[8]
	S += t121_mem0 <= t121

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	t121_mem1 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < t121_mem1*MAS_MEM[1]
	S += (t91*MAS[1])-1 < t121_mem1*MAS_MEM[3]
	S += (t91*MAS[2])-1 < t121_mem1*MAS_MEM[5]
	S += (t91*MAS[3])-1 < t121_mem1*MAS_MEM[7]
	S += (t91*MAS[4])-1 < t121_mem1*MAS_MEM[9]
	S += t121_mem1 <= t121

	new_TX_t1 = S.Task('new_TX_t1', length=11, delay_cost=1)
	new_TX_t1 += alt(MM)
	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	new_TX_t1_in += alt(MM_in)
	S += new_TX_t1_in*MM_in[0]<=new_TX_t1*MM[0]
	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	new_TX_t1_mem0 += MAS_MEM[6]
	S += 25 < new_TX_t1_mem0
	S += new_TX_t1_mem0 <= new_TX_t1

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	new_TX_t1_mem1 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < new_TX_t1_mem1*MAS_MEM[1]
	S += (t111*MAS[1])-1 < new_TX_t1_mem1*MAS_MEM[3]
	S += (t111*MAS[2])-1 < new_TX_t1_mem1*MAS_MEM[5]
	S += (t111*MAS[3])-1 < new_TX_t1_mem1*MAS_MEM[7]
	S += (t111*MAS[4])-1 < new_TX_t1_mem1*MAS_MEM[9]
	S += new_TX_t1_mem1 <= new_TX_t1

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
	S += (t110*MAS[0])-1 < new_TX_t3_mem0*MAS_MEM[0]
	S += (t110*MAS[1])-1 < new_TX_t3_mem0*MAS_MEM[2]
	S += (t110*MAS[2])-1 < new_TX_t3_mem0*MAS_MEM[4]
	S += (t110*MAS[3])-1 < new_TX_t3_mem0*MAS_MEM[6]
	S += (t110*MAS[4])-1 < new_TX_t3_mem0*MAS_MEM[8]
	S += new_TX_t3_mem0 <= new_TX_t3

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	new_TX_t3_mem1 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < new_TX_t3_mem1*MAS_MEM[1]
	S += (t111*MAS[1])-1 < new_TX_t3_mem1*MAS_MEM[3]
	S += (t111*MAS[2])-1 < new_TX_t3_mem1*MAS_MEM[5]
	S += (t111*MAS[3])-1 < new_TX_t3_mem1*MAS_MEM[7]
	S += (t111*MAS[4])-1 < new_TX_t3_mem1*MAS_MEM[9]
	S += new_TX_t3_mem1 <= new_TX_t3

	t13_t0 = S.Task('t13_t0', length=11, delay_cost=1)
	t13_t0 += alt(MM)
	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	t13_t0_in += alt(MM_in)
	S += t13_t0_in*MM_in[0]<=t13_t0*MM[0]
	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	t13_t0_mem0 += MAS_MEM[0]
	S += 18 < t13_t0_mem0
	S += t13_t0_mem0 <= t13_t0

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	t13_t0_mem1 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t13_t0_mem1*MAS_MEM[1]
	S += (t120*MAS[1])-1 < t13_t0_mem1*MAS_MEM[3]
	S += (t120*MAS[2])-1 < t13_t0_mem1*MAS_MEM[5]
	S += (t120*MAS[3])-1 < t13_t0_mem1*MAS_MEM[7]
	S += (t120*MAS[4])-1 < t13_t0_mem1*MAS_MEM[9]
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

	t141_mem0 = S.Task('t141_mem0', length=1, delay_cost=1)
	t141_mem0 += alt(MM_MEM)
	S += (t14_t4*MM[0])-1 < t141_mem0*MM_MEM[0]
	S += t141_mem0 <= t141

	t141_mem1 = S.Task('t141_mem1', length=1, delay_cost=1)
	t141_mem1 += alt(MAS_MEM)
	S += (t14_t5*MAS[0])-1 < t141_mem1*MAS_MEM[1]
	S += (t14_t5*MAS[1])-1 < t141_mem1*MAS_MEM[3]
	S += (t14_t5*MAS[2])-1 < t141_mem1*MAS_MEM[5]
	S += (t14_t5*MAS[3])-1 < t141_mem1*MAS_MEM[7]
	S += (t14_t5*MAS[4])-1 < t141_mem1*MAS_MEM[9]
	S += t141_mem1 <= t141

	new_TZ1 = S.Task('new_TZ1', length=3, delay_cost=1)
	new_TZ1 += alt(MAS)
	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	new_TZ1_in += alt(MAS_in)
	S += new_TZ1_in*MAS_in[0]<=new_TZ1*MAS[0]

	S += new_TZ1_in*MAS_in[1]<=new_TZ1*MAS[1]

	S += new_TZ1_in*MAS_in[2]<=new_TZ1*MAS[2]

	S += new_TZ1_in*MAS_in[3]<=new_TZ1*MAS[3]

	S += new_TZ1_in*MAS_in[4]<=new_TZ1*MAS[4]

	S += 42<new_TZ1

	new_TZ1_w = S.Task('new_TZ1_w', length=1, delay_cost=1)
	new_TZ1_w += alt(MAIN_MEM_w)
	S += new_TZ1 <= new_TZ1_w

	new_TZ1_mem0 = S.Task('new_TZ1_mem0', length=1, delay_cost=1)
	new_TZ1_mem0 += alt(MM_MEM)
	S += (new_TZ_t4*MM[0])-1 < new_TZ1_mem0*MM_MEM[0]
	S += new_TZ1_mem0 <= new_TZ1

	new_TZ1_mem1 = S.Task('new_TZ1_mem1', length=1, delay_cost=1)
	new_TZ1_mem1 += alt(MAS_MEM)
	S += (new_TZ_t5*MAS[0])-1 < new_TZ1_mem1*MAS_MEM[1]
	S += (new_TZ_t5*MAS[1])-1 < new_TZ1_mem1*MAS_MEM[3]
	S += (new_TZ_t5*MAS[2])-1 < new_TZ1_mem1*MAS_MEM[5]
	S += (new_TZ_t5*MAS[3])-1 < new_TZ1_mem1*MAS_MEM[7]
	S += (new_TZ_t5*MAS[4])-1 < new_TZ1_mem1*MAS_MEM[9]
	S += new_TZ1_mem1 <= new_TZ1

	new_TX_t4 = S.Task('new_TX_t4', length=11, delay_cost=1)
	new_TX_t4 += alt(MM)
	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	new_TX_t4_in += alt(MM_in)
	S += new_TX_t4_in*MM_in[0]<=new_TX_t4*MM[0]
	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	new_TX_t4_mem0 += MAS_MEM[2]
	S += 33 < new_TX_t4_mem0
	S += new_TX_t4_mem0 <= new_TX_t4

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	new_TX_t4_mem1 += alt(MAS_MEM)
	S += (new_TX_t3*MAS[0])-1 < new_TX_t4_mem1*MAS_MEM[1]
	S += (new_TX_t3*MAS[1])-1 < new_TX_t4_mem1*MAS_MEM[3]
	S += (new_TX_t3*MAS[2])-1 < new_TX_t4_mem1*MAS_MEM[5]
	S += (new_TX_t3*MAS[3])-1 < new_TX_t4_mem1*MAS_MEM[7]
	S += (new_TX_t3*MAS[4])-1 < new_TX_t4_mem1*MAS_MEM[9]
	S += new_TX_t4_mem1 <= new_TX_t4

	new_TX0 = S.Task('new_TX0', length=3, delay_cost=1)
	new_TX0 += alt(MAS)
	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	new_TX0_in += alt(MAS_in)
	S += new_TX0_in*MAS_in[0]<=new_TX0*MAS[0]

	S += new_TX0_in*MAS_in[1]<=new_TX0*MAS[1]

	S += new_TX0_in*MAS_in[2]<=new_TX0*MAS[2]

	S += new_TX0_in*MAS_in[3]<=new_TX0*MAS[3]

	S += new_TX0_in*MAS_in[4]<=new_TX0*MAS[4]

	S += 45<new_TX0

	new_TX0_w = S.Task('new_TX0_w', length=1, delay_cost=1)
	new_TX0_w += alt(MAIN_MEM_w)
	S += new_TX0 <= new_TX0_w

	new_TX0_mem0 = S.Task('new_TX0_mem0', length=1, delay_cost=1)
	new_TX0_mem0 += alt(MM_MEM)
	S += (new_TX_t0*MM[0])-1 < new_TX0_mem0*MM_MEM[0]
	S += new_TX0_mem0 <= new_TX0

	new_TX0_mem1 = S.Task('new_TX0_mem1', length=1, delay_cost=1)
	new_TX0_mem1 += alt(MM_MEM)
	S += (new_TX_t1*MM[0])-1 < new_TX0_mem1*MM_MEM[1]
	S += new_TX0_mem1 <= new_TX0

	new_TX_t5 = S.Task('new_TX_t5', length=3, delay_cost=1)
	new_TX_t5 += alt(MAS)
	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	new_TX_t5_in += alt(MAS_in)
	S += new_TX_t5_in*MAS_in[0]<=new_TX_t5*MAS[0]

	S += new_TX_t5_in*MAS_in[1]<=new_TX_t5*MAS[1]

	S += new_TX_t5_in*MAS_in[2]<=new_TX_t5*MAS[2]

	S += new_TX_t5_in*MAS_in[3]<=new_TX_t5*MAS[3]

	S += new_TX_t5_in*MAS_in[4]<=new_TX_t5*MAS[4]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	new_TX_t5_mem0 += alt(MM_MEM)
	S += (new_TX_t0*MM[0])-1 < new_TX_t5_mem0*MM_MEM[0]
	S += new_TX_t5_mem0 <= new_TX_t5

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	new_TX_t5_mem1 += alt(MM_MEM)
	S += (new_TX_t1*MM[0])-1 < new_TX_t5_mem1*MM_MEM[1]
	S += new_TX_t5_mem1 <= new_TX_t5

	t13_t1 = S.Task('t13_t1', length=11, delay_cost=1)
	t13_t1 += alt(MM)
	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	t13_t1_in += alt(MM_in)
	S += t13_t1_in*MM_in[0]<=t13_t1*MM[0]
	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	t13_t1_mem0 += MAS_MEM[2]
	S += 27 < t13_t1_mem0
	S += t13_t1_mem0 <= t13_t1

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	t13_t1_mem1 += alt(MAS_MEM)
	S += (t121*MAS[0])-1 < t13_t1_mem1*MAS_MEM[1]
	S += (t121*MAS[1])-1 < t13_t1_mem1*MAS_MEM[3]
	S += (t121*MAS[2])-1 < t13_t1_mem1*MAS_MEM[5]
	S += (t121*MAS[3])-1 < t13_t1_mem1*MAS_MEM[7]
	S += (t121*MAS[4])-1 < t13_t1_mem1*MAS_MEM[9]
	S += t13_t1_mem1 <= t13_t1

	t13_t3 = S.Task('t13_t3', length=3, delay_cost=1)
	t13_t3 += alt(MAS)
	t13_t3_in = S.Task('t13_t3_in', length=1, delay_cost=1)
	t13_t3_in += alt(MAS_in)
	S += t13_t3_in*MAS_in[0]<=t13_t3*MAS[0]

	S += t13_t3_in*MAS_in[1]<=t13_t3*MAS[1]

	S += t13_t3_in*MAS_in[2]<=t13_t3*MAS[2]

	S += t13_t3_in*MAS_in[3]<=t13_t3*MAS[3]

	S += t13_t3_in*MAS_in[4]<=t13_t3*MAS[4]

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	t13_t3_mem0 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t13_t3_mem0*MAS_MEM[0]
	S += (t120*MAS[1])-1 < t13_t3_mem0*MAS_MEM[2]
	S += (t120*MAS[2])-1 < t13_t3_mem0*MAS_MEM[4]
	S += (t120*MAS[3])-1 < t13_t3_mem0*MAS_MEM[6]
	S += (t120*MAS[4])-1 < t13_t3_mem0*MAS_MEM[8]
	S += t13_t3_mem0 <= t13_t3

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	t13_t3_mem1 += alt(MAS_MEM)
	S += (t121*MAS[0])-1 < t13_t3_mem1*MAS_MEM[1]
	S += (t121*MAS[1])-1 < t13_t3_mem1*MAS_MEM[3]
	S += (t121*MAS[2])-1 < t13_t3_mem1*MAS_MEM[5]
	S += (t121*MAS[3])-1 < t13_t3_mem1*MAS_MEM[7]
	S += (t121*MAS[4])-1 < t13_t3_mem1*MAS_MEM[9]
	S += t13_t3_mem1 <= t13_t3

	new_TX1 = S.Task('new_TX1', length=3, delay_cost=1)
	new_TX1 += alt(MAS)
	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	new_TX1_in += alt(MAS_in)
	S += new_TX1_in*MAS_in[0]<=new_TX1*MAS[0]

	S += new_TX1_in*MAS_in[1]<=new_TX1*MAS[1]

	S += new_TX1_in*MAS_in[2]<=new_TX1*MAS[2]

	S += new_TX1_in*MAS_in[3]<=new_TX1*MAS[3]

	S += new_TX1_in*MAS_in[4]<=new_TX1*MAS[4]

	S += 40<new_TX1

	new_TX1_w = S.Task('new_TX1_w', length=1, delay_cost=1)
	new_TX1_w += alt(MAIN_MEM_w)
	S += new_TX1 <= new_TX1_w

	new_TX1_mem0 = S.Task('new_TX1_mem0', length=1, delay_cost=1)
	new_TX1_mem0 += alt(MM_MEM)
	S += (new_TX_t4*MM[0])-1 < new_TX1_mem0*MM_MEM[0]
	S += new_TX1_mem0 <= new_TX1

	new_TX1_mem1 = S.Task('new_TX1_mem1', length=1, delay_cost=1)
	new_TX1_mem1 += alt(MAS_MEM)
	S += (new_TX_t5*MAS[0])-1 < new_TX1_mem1*MAS_MEM[1]
	S += (new_TX_t5*MAS[1])-1 < new_TX1_mem1*MAS_MEM[3]
	S += (new_TX_t5*MAS[2])-1 < new_TX1_mem1*MAS_MEM[5]
	S += (new_TX_t5*MAS[3])-1 < new_TX1_mem1*MAS_MEM[7]
	S += (new_TX_t5*MAS[4])-1 < new_TX1_mem1*MAS_MEM[9]
	S += new_TX1_mem1 <= new_TX1

	t13_t4 = S.Task('t13_t4', length=11, delay_cost=1)
	t13_t4 += alt(MM)
	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	t13_t4_in += alt(MM_in)
	S += t13_t4_in*MM_in[0]<=t13_t4*MM[0]
	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	t13_t4_mem0 += MAS_MEM[6]
	S += 35 < t13_t4_mem0
	S += t13_t4_mem0 <= t13_t4

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	t13_t4_mem1 += alt(MAS_MEM)
	S += (t13_t3*MAS[0])-1 < t13_t4_mem1*MAS_MEM[1]
	S += (t13_t3*MAS[1])-1 < t13_t4_mem1*MAS_MEM[3]
	S += (t13_t3*MAS[2])-1 < t13_t4_mem1*MAS_MEM[5]
	S += (t13_t3*MAS[3])-1 < t13_t4_mem1*MAS_MEM[7]
	S += (t13_t3*MAS[4])-1 < t13_t4_mem1*MAS_MEM[9]
	S += t13_t4_mem1 <= t13_t4

	t130 = S.Task('t130', length=3, delay_cost=1)
	t130 += alt(MAS)
	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	t130_in += alt(MAS_in)
	S += t130_in*MAS_in[0]<=t130*MAS[0]

	S += t130_in*MAS_in[1]<=t130*MAS[1]

	S += t130_in*MAS_in[2]<=t130*MAS[2]

	S += t130_in*MAS_in[3]<=t130*MAS[3]

	S += t130_in*MAS_in[4]<=t130*MAS[4]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	t130_mem0 += alt(MM_MEM)
	S += (t13_t0*MM[0])-1 < t130_mem0*MM_MEM[0]
	S += t130_mem0 <= t130

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	t130_mem1 += alt(MM_MEM)
	S += (t13_t1*MM[0])-1 < t130_mem1*MM_MEM[1]
	S += t130_mem1 <= t130

	t13_t5 = S.Task('t13_t5', length=3, delay_cost=1)
	t13_t5 += alt(MAS)
	t13_t5_in = S.Task('t13_t5_in', length=1, delay_cost=1)
	t13_t5_in += alt(MAS_in)
	S += t13_t5_in*MAS_in[0]<=t13_t5*MAS[0]

	S += t13_t5_in*MAS_in[1]<=t13_t5*MAS[1]

	S += t13_t5_in*MAS_in[2]<=t13_t5*MAS[2]

	S += t13_t5_in*MAS_in[3]<=t13_t5*MAS[3]

	S += t13_t5_in*MAS_in[4]<=t13_t5*MAS[4]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	t13_t5_mem0 += alt(MM_MEM)
	S += (t13_t0*MM[0])-1 < t13_t5_mem0*MM_MEM[0]
	S += t13_t5_mem0 <= t13_t5

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	t13_t5_mem1 += alt(MM_MEM)
	S += (t13_t1*MM[0])-1 < t13_t5_mem1*MM_MEM[1]
	S += t13_t5_mem1 <= t13_t5

	t131 = S.Task('t131', length=3, delay_cost=1)
	t131 += alt(MAS)
	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	t131_in += alt(MAS_in)
	S += t131_in*MAS_in[0]<=t131*MAS[0]

	S += t131_in*MAS_in[1]<=t131*MAS[1]

	S += t131_in*MAS_in[2]<=t131*MAS[2]

	S += t131_in*MAS_in[3]<=t131*MAS[3]

	S += t131_in*MAS_in[4]<=t131*MAS[4]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += alt(MM_MEM)
	S += (t13_t4*MM[0])-1 < t131_mem0*MM_MEM[0]
	S += t131_mem0 <= t131

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	t131_mem1 += alt(MAS_MEM)
	S += (t13_t5*MAS[0])-1 < t131_mem1*MAS_MEM[1]
	S += (t13_t5*MAS[1])-1 < t131_mem1*MAS_MEM[3]
	S += (t13_t5*MAS[2])-1 < t131_mem1*MAS_MEM[5]
	S += (t13_t5*MAS[3])-1 < t131_mem1*MAS_MEM[7]
	S += (t13_t5*MAS[4])-1 < t131_mem1*MAS_MEM[9]
	S += t131_mem1 <= t131

	t150 = S.Task('t150', length=3, delay_cost=1)
	t150 += alt(MAS)
	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	t150_in += alt(MAS_in)
	S += t150_in*MAS_in[0]<=t150*MAS[0]

	S += t150_in*MAS_in[1]<=t150*MAS[1]

	S += t150_in*MAS_in[2]<=t150*MAS[2]

	S += t150_in*MAS_in[3]<=t150*MAS[3]

	S += t150_in*MAS_in[4]<=t150*MAS[4]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += alt(MAS_MEM)
	S += (t130*MAS[0])-1 < t150_mem0*MAS_MEM[0]
	S += (t130*MAS[1])-1 < t150_mem0*MAS_MEM[2]
	S += (t130*MAS[2])-1 < t150_mem0*MAS_MEM[4]
	S += (t130*MAS[3])-1 < t150_mem0*MAS_MEM[6]
	S += (t130*MAS[4])-1 < t150_mem0*MAS_MEM[8]
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < t150_mem1*MAS_MEM[1]
	S += (t140*MAS[1])-1 < t150_mem1*MAS_MEM[3]
	S += (t140*MAS[2])-1 < t150_mem1*MAS_MEM[5]
	S += (t140*MAS[3])-1 < t150_mem1*MAS_MEM[7]
	S += (t140*MAS[4])-1 < t150_mem1*MAS_MEM[9]
	S += t150_mem1 <= t150

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS5/EP2_ADD_w_EVAL/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

