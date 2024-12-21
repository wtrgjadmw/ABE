from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 123
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	new_TZ_t2_in = S.Task('new_TZ_t2_in', length=1, delay_cost=1)
	S += new_TZ_t2_in >= 0
	new_TZ_t2_in += MAS_in[3]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 0
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 0
	t0_t3_in += MAS_in[1]

	t16_t2_in = S.Task('t16_t2_in', length=1, delay_cost=1)
	S += t16_t2_in >= 0
	t16_t2_in += MAS_in[2]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 0
	t2_t1_in += MM_in[0]

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 0
	t2_t2_mem1 += MAIN_MEM_r[1]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 0
	t7_t2_in += MAS_in[0]

	new_TZ_t2 = S.Task('new_TZ_t2', length=2, delay_cost=1)
	S += new_TZ_t2 >= 1
	new_TZ_t2 += MAS[3]

	t0_t3 = S.Task('t0_t3', length=2, delay_cost=1)
	S += t0_t3 >= 1
	t0_t3 += MAS[1]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 1
	t0_t3_mem1 += MAIN_MEM_r[1]

	t14_t2_in = S.Task('t14_t2_in', length=1, delay_cost=1)
	S += t14_t2_in >= 1
	t14_t2_in += MAS_in[3]

	t16_t2 = S.Task('t16_t2', length=2, delay_cost=1)
	S += t16_t2 >= 1
	t16_t2 += MAS[2]

	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	S += t17_t2_in >= 1
	t17_t2_in += MAS_in[2]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 1
	t2_t0_in += MM_in[0]

	t2_t1 = S.Task('t2_t1', length=4, delay_cost=1)
	S += t2_t1 >= 1
	t2_t1 += MM[0]

	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	S += t2_t3_in >= 1
	t2_t3_in += MAS_in[1]

	t7_t2 = S.Task('t7_t2', length=2, delay_cost=1)
	S += t7_t2 >= 1
	t7_t2 += MAS[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 1
	t7_t2_mem0 += MAIN_MEM_r[0]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 1
	t9_t2_in += MAS_in[0]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 2
	t0_t0_in += MM_in[0]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 2
	t0_t2_in += MAS_in[0]

	t14_t2 = S.Task('t14_t2', length=2, delay_cost=1)
	S += t14_t2 >= 2
	t14_t2 += MAS[3]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 2
	t16_t0_mem0 += MAIN_MEM_r[0]

	t17_t2 = S.Task('t17_t2', length=2, delay_cost=1)
	S += t17_t2 >= 2
	t17_t2 += MAS[2]

	t2_t0 = S.Task('t2_t0', length=4, delay_cost=1)
	S += t2_t0 >= 2
	t2_t0 += MM[0]

	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	S += t2_t2_in >= 2
	t2_t2_in += MAS_in[1]

	t2_t3 = S.Task('t2_t3', length=2, delay_cost=1)
	S += t2_t3 >= 2
	t2_t3 += MAS[1]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 2
	t7_t2_mem1 += MAIN_MEM_r[1]

	t9_t2 = S.Task('t9_t2', length=2, delay_cost=1)
	S += t9_t2 >= 2
	t9_t2 += MAS[0]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 3
	c010_mem1 += MAIN_MEM_r[1]

	t0_t0 = S.Task('t0_t0', length=4, delay_cost=1)
	S += t0_t0 >= 3
	t0_t0 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 3
	t0_t1_in += MM_in[0]

	t0_t2 = S.Task('t0_t2', length=2, delay_cost=1)
	S += t0_t2 >= 3
	t0_t2 += MAS[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 3
	t17_t2_mem0 += MAIN_MEM_r[0]

	t2_t2 = S.Task('t2_t2', length=2, delay_cost=1)
	S += t2_t2 >= 3
	t2_t2 += MAS[1]

	t0_t1 = S.Task('t0_t1', length=4, delay_cost=1)
	S += t0_t1 >= 4
	t0_t1 += MM[0]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 4
	t14_t2_mem0 += MAIN_MEM_r[0]

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 4
	t2_t3_mem1 += MAIN_MEM_r[1]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 4
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 4
	t2_t4_mem0 += MAS_MEM[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 4
	t2_t4_mem1 += MAS_MEM[3]

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 5
	new_TZ_t2_mem1 += MAIN_MEM_r[1]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 5
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 5
	t0_t4_mem0 += MAS_MEM[0]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 5
	t0_t4_mem1 += MAS_MEM[3]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 5
	t17_t0_mem0 += MAIN_MEM_r[0]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 5
	t20_in += MAS_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 5
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 5
	t20_mem1 += MM_MEM[1]

	t2_t4 = S.Task('t2_t4', length=4, delay_cost=1)
	S += t2_t4 >= 5
	t2_t4 += MM[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 6
	t0_t1_mem1 += MAIN_MEM_r[1]

	t0_t4 = S.Task('t0_t4', length=4, delay_cost=1)
	S += t0_t4 >= 6
	t0_t4 += MM[0]

	t20 = S.Task('t20', length=2, delay_cost=1)
	S += t20 >= 6
	t20 += MAS[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 6
	t2_t2_mem0 += MAIN_MEM_r[0]

	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	S += t2_t5_in >= 6
	t2_t5_in += MAS_in[0]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 6
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 6
	t2_t5_mem1 += MM_MEM[1]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 7
	t00_in += MAS_in[2]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 7
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 7
	t00_mem1 += MM_MEM[1]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 7
	t16_t2_mem0 += MAIN_MEM_r[0]

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 7
	t16_t2_mem1 += MAIN_MEM_r[1]

	t2_t5 = S.Task('t2_t5', length=2, delay_cost=1)
	S += t2_t5 >= 7
	t2_t5 += MAS[0]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 7
	t30_in += MAS_in[1]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 7
	t30_mem1 += MAS_MEM[1]

	t00 = S.Task('t00', length=2, delay_cost=1)
	S += t00 >= 8
	t00 += MAS[2]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 8
	t0_t5_in += MAS_in[2]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 8
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 8
	t0_t5_mem1 += MM_MEM[1]

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 8
	t14_t2_mem1 += MAIN_MEM_r[1]

	t30 = S.Task('t30', length=2, delay_cost=1)
	S += t30 >= 8
	t30 += MAS[1]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 8
	t9_t2_mem0 += MAIN_MEM_r[0]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 9
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 9
	c010_mem0 += MAS_MEM[2]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 9
	t0_t2_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=2, delay_cost=1)
	S += t0_t5 >= 9
	t0_t5 += MAS[2]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 9
	t10_in += MAS_in[3]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 9
	t10_mem1 += MAS_MEM[5]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 9
	t21_in += MAS_in[2]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 9
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 9
	t21_mem1 += MAS_MEM[1]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 9
	t2_t3_mem0 += MAIN_MEM_r[0]

	c010 = S.Task('c010', length=4, delay_cost=1)
	S += c010 >= 10
	c010 += MM[0]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 10
	c200_mem1 += MAIN_MEM_r[1]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 10
	t01_in += MAS_in[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 10
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 10
	t01_mem1 += MAS_MEM[5]

	t10 = S.Task('t10', length=2, delay_cost=1)
	S += t10 >= 10
	t10 += MAS[3]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 10
	t16_t0_in += MM_in[0]

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 10
	t16_t0_mem1 += MAS_MEM[3]

	t21 = S.Task('t21', length=2, delay_cost=1)
	S += t21 >= 10
	t21 += MAS[2]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 10
	t31_mem0 += MAIN_MEM_r[0]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 11
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 11
	c200_mem0 += MAS_MEM[6]

	t01 = S.Task('t01', length=2, delay_cost=1)
	S += t01 >= 11
	t01 += MAS[0]

	t16_t0 = S.Task('t16_t0', length=4, delay_cost=1)
	S += t16_t0 >= 11
	t16_t0 += MM[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 11
	t2_t0_mem0 += MAIN_MEM_r[0]

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 11
	t2_t1_mem1 += MAIN_MEM_r[1]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 11
	t31_in += MAS_in[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 11
	t31_mem1 += MAS_MEM[5]

	c200 = S.Task('c200', length=4, delay_cost=1)
	S += c200 >= 12
	c200 += MM[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 12
	t0_t1_mem0 += MAIN_MEM_r[0]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 12
	t11_in += MAS_in[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 12
	t11_mem1 += MAS_MEM[1]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 12
	t17_t0_in += MM_in[0]

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 12
	t17_t0_mem1 += MAS_MEM[7]

	t31 = S.Task('t31', length=2, delay_cost=1)
	S += t31 >= 12
	t31 += MAS[0]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 12
	t9_t2_mem1 += MAIN_MEM_r[1]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 13
	t0_t0_mem1 += MAIN_MEM_r[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 13
	t0_t2_mem0 += MAIN_MEM_r[0]

	t11 = S.Task('t11', length=2, delay_cost=1)
	S += t11 >= 13
	t11 += MAS[0]

	t17_t0 = S.Task('t17_t0', length=4, delay_cost=1)
	S += t17_t0 >= 13
	t17_t0 += MM[0]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 13
	t5_t3_in += MM_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 13
	t5_t3_mem0 += MAS_MEM[2]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 13
	t5_t3_mem1 += MAS_MEM[1]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 14
	c010_w += MAIN_MEM_w

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 14
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 14
	c011_mem0 += MAS_MEM[0]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 14
	new_TZ_t2_mem0 += MAIN_MEM_r[0]

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 14
	t2_t0_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=4, delay_cost=1)
	S += t5_t3 >= 14
	t5_t3 += MM[0]

	c011 = S.Task('c011', length=4, delay_cost=1)
	S += c011 >= 15
	c011 += MM[0]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 15
	t17_t1_in += MM_in[0]

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 15
	t17_t1_mem1 += MAS_MEM[1]

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 15
	t17_t2_mem1 += MAIN_MEM_r[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 15
	t30_mem0 += MAIN_MEM_r[0]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 16
	c200_w += MAIN_MEM_w

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 16
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 16
	c201_mem0 += MAS_MEM[0]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 16
	c201_mem1 += MAIN_MEM_r[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 16
	t10_mem0 += MAIN_MEM_r[0]

	t17_t1 = S.Task('t17_t1', length=4, delay_cost=1)
	S += t17_t1 >= 16
	t17_t1 += MM[0]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 17
	c011_mem1 += MAIN_MEM_r[1]

	c201 = S.Task('c201', length=4, delay_cost=1)
	S += c201 >= 17
	c201 += MM[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 17
	t0_t3_mem0 += MAIN_MEM_r[0]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 17
	t16_t1_in += MM_in[0]

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 17
	t16_t1_mem1 += MAS_MEM[1]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 17
	t51_in += MAS_in[3]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 17
	t51_mem0 += MM_MEM[0]

	t16_t1 = S.Task('t16_t1', length=4, delay_cost=1)
	S += t16_t1 >= 18
	t16_t1 += MM[0]

	t17_t3_in = S.Task('t17_t3_in', length=1, delay_cost=1)
	S += t17_t3_in >= 18
	t17_t3_in += MAS_in[3]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 18
	t17_t3_mem0 += MAS_MEM[6]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 18
	t17_t3_mem1 += MAS_MEM[1]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 18
	t2_t1_mem0 += MAIN_MEM_r[0]

	t51 = S.Task('t51', length=2, delay_cost=1)
	S += t51 >= 18
	t51 += MAS[3]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 18
	t5_t2_in += MM_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 18
	t5_t2_mem0 += MAS_MEM[4]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 18
	t5_t2_mem1 += MAS_MEM[5]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 18
	t5_t5_in += MAS_in[2]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 18
	t5_t5_mem0 += MM_MEM[0]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 19
	c011_w += MAIN_MEM_w

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 19
	t11_mem0 += MAIN_MEM_r[0]

	t16_t3_in = S.Task('t16_t3_in', length=1, delay_cost=1)
	S += t16_t3_in >= 19
	t16_t3_in += MAS_in[3]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 19
	t16_t3_mem0 += MAS_MEM[2]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 19
	t16_t3_mem1 += MAS_MEM[1]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 19
	t170_in += MAS_in[1]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 19
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 19
	t170_mem1 += MM_MEM[1]

	t17_t3 = S.Task('t17_t3', length=2, delay_cost=1)
	S += t17_t3 >= 19
	t17_t3 += MAS[3]

	t5_t2 = S.Task('t5_t2', length=4, delay_cost=1)
	S += t5_t2 >= 19
	t5_t2 += MM[0]

	t5_t5 = S.Task('t5_t5', length=2, delay_cost=1)
	S += t5_t5 >= 19
	t5_t5 += MAS[2]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 19
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 19
	t6_t1_mem0 += MAS_MEM[0]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 19
	t6_t1_mem1 += MAS_MEM[7]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 20
	t16_t1_mem0 += MAIN_MEM_r[0]

	t16_t3 = S.Task('t16_t3', length=2, delay_cost=1)
	S += t16_t3 >= 20
	t16_t3 += MAS[3]

	t170 = S.Task('t170', length=2, delay_cost=1)
	S += t170 >= 20
	t170 += MAS[1]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 20
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 20
	t17_t4_mem0 += MAS_MEM[4]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 20
	t17_t4_mem1 += MAS_MEM[7]

	t17_t5_in = S.Task('t17_t5_in', length=1, delay_cost=1)
	S += t17_t5_in >= 20
	t17_t5_in += MAS_in[1]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 20
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 20
	t17_t5_mem1 += MM_MEM[1]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 20
	t4_t1_in += MAS_in[2]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 20
	t4_t1_mem0 += MAS_MEM[6]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 20
	t4_t1_mem1 += MAS_MEM[1]

	t6_t1 = S.Task('t6_t1', length=4, delay_cost=1)
	S += t6_t1 >= 20
	t6_t1 += MM[0]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 21
	c201_w += MAIN_MEM_w

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 21
	t160_in += MAS_in[2]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 21
	t160_mem0 += MM_MEM[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 21
	t160_mem1 += MM_MEM[1]

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 21
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 21
	t16_t4_mem0 += MAS_MEM[4]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 21
	t16_t4_mem1 += MAS_MEM[7]

	t17_t4 = S.Task('t17_t4', length=4, delay_cost=1)
	S += t17_t4 >= 21
	t17_t4 += MM[0]

	t17_t5 = S.Task('t17_t5', length=2, delay_cost=1)
	S += t17_t5 >= 21
	t17_t5 += MAS[1]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 21
	t4_t0_in += MAS_in[0]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 21
	t4_t0_mem0 += MAS_MEM[6]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 21
	t4_t0_mem1 += MAS_MEM[1]

	t4_t1 = S.Task('t4_t1', length=2, delay_cost=1)
	S += t4_t1 >= 21
	t4_t1 += MAS[2]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 21
	t9_t1_mem0 += MAIN_MEM_r[0]

	t160 = S.Task('t160', length=2, delay_cost=1)
	S += t160 >= 22
	t160 += MAS[2]

	t16_t4 = S.Task('t16_t4', length=4, delay_cost=1)
	S += t16_t4 >= 22
	t16_t4 += MM[0]

	t4_t0 = S.Task('t4_t0', length=2, delay_cost=1)
	S += t4_t0 >= 22
	t4_t0 += MAS[0]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 22
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 22
	t4_t3_mem0 += MAS_MEM[6]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 22
	t4_t3_mem1 += MAS_MEM[1]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 22
	t50_in += MAS_in[2]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 22
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 22
	t50_mem1 += MAS_MEM[5]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 22
	t9_t0_mem0 += MAIN_MEM_r[0]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 23
	c000_in += MAS_in[0]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 23
	c000_mem0 += MAS_MEM[4]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 23
	c000_mem1 += MAS_MEM[3]

	new_TX_t2_in = S.Task('new_TX_t2_in', length=1, delay_cost=1)
	S += new_TX_t2_in >= 23
	new_TX_t2_in += MAS_in[3]

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 23
	new_TX_t2_mem0 += MAS_MEM[2]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 23
	new_TX_t2_mem1 += MAS_MEM[1]

	t16_t5_in = S.Task('t16_t5_in', length=1, delay_cost=1)
	S += t16_t5_in >= 23
	t16_t5_in += MAS_in[1]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 23
	t16_t5_mem0 += MM_MEM[0]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 23
	t16_t5_mem1 += MM_MEM[1]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 23
	t17_t1_mem0 += MAIN_MEM_r[0]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 23
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 23
	t4_t2_mem0 += MAS_MEM[0]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 23
	t4_t2_mem1 += MAS_MEM[5]

	t4_t3 = S.Task('t4_t3', length=4, delay_cost=1)
	S += t4_t3 >= 23
	t4_t3 += MM[0]

	t50 = S.Task('t50', length=2, delay_cost=1)
	S += t50 >= 23
	t50 += MAS[2]

	c000 = S.Task('c000', length=2, delay_cost=1)
	S += c000 >= 24
	c000 += MAS[0]

	new_TX_t2 = S.Task('new_TX_t2', length=2, delay_cost=1)
	S += new_TX_t2 >= 24
	new_TX_t2 += MAS[3]

	t13_t2_in = S.Task('t13_t2_in', length=1, delay_cost=1)
	S += t13_t2_in >= 24
	t13_t2_in += MAS_in[1]

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 24
	t13_t2_mem0 += MAS_MEM[6]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 24
	t13_t2_mem1 += MAS_MEM[1]

	t16_t5 = S.Task('t16_t5', length=2, delay_cost=1)
	S += t16_t5 >= 24
	t16_t5 += MAS[1]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 24
	t171_in += MAS_in[2]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 24
	t171_mem0 += MM_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 24
	t171_mem1 += MAS_MEM[3]

	t4_t2 = S.Task('t4_t2', length=4, delay_cost=1)
	S += t4_t2 >= 24
	t4_t2 += MM[0]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 24
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 24
	t6_t0_mem0 += MAS_MEM[2]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 24
	t6_t0_mem1 += MAS_MEM[5]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 24
	t7_t1_mem0 += MAIN_MEM_r[0]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 24
	t9_t3_in += MAS_in[0]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 24
	t9_t3_mem0 += MAS_MEM[4]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 24
	t9_t3_mem1 += MAS_MEM[7]

	t13_t2 = S.Task('t13_t2', length=2, delay_cost=1)
	S += t13_t2 >= 25
	t13_t2 += MAS[1]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 25
	t161_in += MAS_in[3]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 25
	t161_mem0 += MM_MEM[0]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 25
	t161_mem1 += MAS_MEM[3]

	t171 = S.Task('t171', length=2, delay_cost=1)
	S += t171 >= 25
	t171 += MAS[2]

	t6_t0 = S.Task('t6_t0', length=4, delay_cost=1)
	S += t6_t0 >= 25
	t6_t0 += MM[0]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 25
	t6_t2_in += MAS_in[1]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 25
	t6_t2_mem0 += MAS_MEM[2]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 25
	t6_t2_mem1 += MAS_MEM[1]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 25
	t6_t3_in += MAS_in[0]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 25
	t6_t3_mem0 += MAS_MEM[4]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 25
	t6_t3_mem1 += MAS_MEM[7]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 25
	t7_t0_mem0 += MAIN_MEM_r[0]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 25
	t9_t0_in += MM_in[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 25
	t9_t0_mem1 += MAS_MEM[5]

	t9_t3 = S.Task('t9_t3', length=2, delay_cost=1)
	S += t9_t3 >= 25
	t9_t3 += MAS[0]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 26
	c000_w += MAIN_MEM_w

	t161 = S.Task('t161', length=2, delay_cost=1)
	S += t161 >= 26
	t161 += MAS[3]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 26
	t4_t5_in += MAS_in[2]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 26
	t4_t5_mem0 += MM_MEM[0]

	t6_t2 = S.Task('t6_t2', length=2, delay_cost=1)
	S += t6_t2 >= 26
	t6_t2 += MAS[1]

	t6_t3 = S.Task('t6_t3', length=2, delay_cost=1)
	S += t6_t3 >= 26
	t6_t3 += MAS[0]

	t9_t0 = S.Task('t9_t0', length=4, delay_cost=1)
	S += t9_t0 >= 26
	t9_t0 += MM[0]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 26
	t9_t1_in += MM_in[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 26
	t9_t1_mem1 += MAS_MEM[7]

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 27
	c001_in += MAS_in[3]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 27
	c001_mem0 += MAS_MEM[6]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 27
	c001_mem1 += MAS_MEM[5]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 27
	t41_in += MAS_in[2]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 27
	t41_mem0 += MM_MEM[0]

	t4_t5 = S.Task('t4_t5', length=2, delay_cost=1)
	S += t4_t5 >= 27
	t4_t5 += MAS[2]

	t9_t1 = S.Task('t9_t1', length=4, delay_cost=1)
	S += t9_t1 >= 27
	t9_t1 += MM[0]

	c001 = S.Task('c001', length=2, delay_cost=1)
	S += c001 >= 28
	c001 += MAS[3]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 28
	t40_in += MAS_in[0]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 28
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 28
	t40_mem1 += MAS_MEM[5]

	t41 = S.Task('t41', length=2, delay_cost=1)
	S += t41 >= 28
	t41 += MAS[2]

	t40 = S.Task('t40', length=2, delay_cost=1)
	S += t40 >= 29
	t40 += MAS[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 29
	t7_t1_in += MM_in[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 29
	t7_t1_mem1 += MAS_MEM[5]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 30
	c001_w += MAIN_MEM_w

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 30
	t7_t0_in += MM_in[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 30
	t7_t0_mem1 += MAS_MEM[1]

	t7_t1 = S.Task('t7_t1', length=4, delay_cost=1)
	S += t7_t1 >= 30
	t7_t1 += MM[0]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 30
	t7_t3_in += MAS_in[2]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 30
	t7_t3_mem0 += MAS_MEM[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 30
	t7_t3_mem1 += MAS_MEM[5]

	t7_t0 = S.Task('t7_t0', length=4, delay_cost=1)
	S += t7_t0 >= 31
	t7_t0 += MM[0]

	t7_t3 = S.Task('t7_t3', length=2, delay_cost=1)
	S += t7_t3 >= 31
	t7_t3 += MAS[2]


	# new tasks
	t5_t0 = S.Task('t5_t0', length=2, delay_cost=1)
	t5_t0 += alt(MAS)
	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	t5_t0_in += alt(MAS_in)
	S += t5_t0_in*MAS_in[0]<=t5_t0*MAS[0]

	S += t5_t0_in*MAS_in[1]<=t5_t0*MAS[1]

	S += t5_t0_in*MAS_in[2]<=t5_t0*MAS[2]

	S += t5_t0_in*MAS_in[3]<=t5_t0*MAS[3]

	S += t5_t0<19

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	t5_t0_mem0 += MAS_MEM[2]
	S += 9 < t5_t0_mem0
	S += t5_t0_mem0 <= t5_t0

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	t5_t0_mem1 += MAS_MEM[1]
	S += 13 < t5_t0_mem1
	S += t5_t0_mem1 <= t5_t0

	t5_t1 = S.Task('t5_t1', length=2, delay_cost=1)
	t5_t1 += alt(MAS)
	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	t5_t1_in += alt(MAS_in)
	S += t5_t1_in*MAS_in[0]<=t5_t1*MAS[0]

	S += t5_t1_in*MAS_in[1]<=t5_t1*MAS[1]

	S += t5_t1_in*MAS_in[2]<=t5_t1*MAS[2]

	S += t5_t1_in*MAS_in[3]<=t5_t1*MAS[3]

	S += t5_t1<19

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	t5_t1_mem0 += MAS_MEM[2]
	S += 9 < t5_t1_mem0
	S += t5_t1_mem0 <= t5_t1

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	t5_t1_mem1 += MAS_MEM[1]
	S += 13 < t5_t1_mem1
	S += t5_t1_mem1 <= t5_t1

	t6_t4 = S.Task('t6_t4', length=4, delay_cost=1)
	t6_t4 += alt(MM)
	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	t6_t4_in += alt(MM_in)
	S += t6_t4>=t6_t4_in

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	t6_t4_mem0 += MAS_MEM[2]
	S += 27 < t6_t4_mem0
	S += t6_t4_mem0 <= t6_t4

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	t6_t4_mem1 += MAS_MEM[1]
	S += 27 < t6_t4_mem1
	S += t6_t4_mem1 <= t6_t4

	t60 = S.Task('t60', length=2, delay_cost=1)
	t60 += alt(MAS)
	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	t60_in += alt(MAS_in)
	S += t60_in*MAS_in[0]<=t60*MAS[0]

	S += t60_in*MAS_in[1]<=t60*MAS[1]

	S += t60_in*MAS_in[2]<=t60*MAS[2]

	S += t60_in*MAS_in[3]<=t60*MAS[3]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	t60_mem0 += MM_MEM[0]
	S += 28 < t60_mem0
	S += t60_mem0 <= t60

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	t60_mem1 += MM_MEM[1]
	S += 23 < t60_mem1
	S += t60_mem1 <= t60

	t6_t5 = S.Task('t6_t5', length=2, delay_cost=1)
	t6_t5 += alt(MAS)
	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	t6_t5_in += alt(MAS_in)
	S += t6_t5_in*MAS_in[0]<=t6_t5*MAS[0]

	S += t6_t5_in*MAS_in[1]<=t6_t5*MAS[1]

	S += t6_t5_in*MAS_in[2]<=t6_t5*MAS[2]

	S += t6_t5_in*MAS_in[3]<=t6_t5*MAS[3]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	t6_t5_mem0 += MM_MEM[0]
	S += 28 < t6_t5_mem0
	S += t6_t5_mem0 <= t6_t5

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	t6_t5_mem1 += MM_MEM[1]
	S += 23 < t6_t5_mem1
	S += t6_t5_mem1 <= t6_t5

	t7_t4 = S.Task('t7_t4', length=4, delay_cost=1)
	t7_t4 += alt(MM)
	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	t7_t4_in += alt(MM_in)
	S += t7_t4>=t7_t4_in

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	t7_t4_mem0 += MAS_MEM[0]
	S += 2 < t7_t4_mem0
	S += t7_t4_mem0 <= t7_t4

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	t7_t4_mem1 += MAS_MEM[5]
	S += 32 < t7_t4_mem1
	S += t7_t4_mem1 <= t7_t4

	t70 = S.Task('t70', length=2, delay_cost=1)
	t70 += alt(MAS)
	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	t70_in += alt(MAS_in)
	S += t70_in*MAS_in[0]<=t70*MAS[0]

	S += t70_in*MAS_in[1]<=t70*MAS[1]

	S += t70_in*MAS_in[2]<=t70*MAS[2]

	S += t70_in*MAS_in[3]<=t70*MAS[3]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += MM_MEM[0]
	S += 34 < t70_mem0
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += MM_MEM[1]
	S += 33 < t70_mem1
	S += t70_mem1 <= t70

	t7_t5 = S.Task('t7_t5', length=2, delay_cost=1)
	t7_t5 += alt(MAS)
	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	t7_t5_in += alt(MAS_in)
	S += t7_t5_in*MAS_in[0]<=t7_t5*MAS[0]

	S += t7_t5_in*MAS_in[1]<=t7_t5*MAS[1]

	S += t7_t5_in*MAS_in[2]<=t7_t5*MAS[2]

	S += t7_t5_in*MAS_in[3]<=t7_t5*MAS[3]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	t7_t5_mem0 += MM_MEM[0]
	S += 34 < t7_t5_mem0
	S += t7_t5_mem0 <= t7_t5

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	t7_t5_mem1 += MM_MEM[1]
	S += 33 < t7_t5_mem1
	S += t7_t5_mem1 <= t7_t5

	t9_t4 = S.Task('t9_t4', length=4, delay_cost=1)
	t9_t4 += alt(MM)
	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	t9_t4_in += alt(MM_in)
	S += t9_t4>=t9_t4_in

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	t9_t4_mem0 += MAS_MEM[0]
	S += 3 < t9_t4_mem0
	S += t9_t4_mem0 <= t9_t4

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	t9_t4_mem1 += MAS_MEM[1]
	S += 26 < t9_t4_mem1
	S += t9_t4_mem1 <= t9_t4

	t90 = S.Task('t90', length=2, delay_cost=1)
	t90 += alt(MAS)
	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	t90_in += alt(MAS_in)
	S += t90_in*MAS_in[0]<=t90*MAS[0]

	S += t90_in*MAS_in[1]<=t90*MAS[1]

	S += t90_in*MAS_in[2]<=t90*MAS[2]

	S += t90_in*MAS_in[3]<=t90*MAS[3]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += MM_MEM[0]
	S += 29 < t90_mem0
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += MM_MEM[1]
	S += 30 < t90_mem1
	S += t90_mem1 <= t90

	t9_t5 = S.Task('t9_t5', length=2, delay_cost=1)
	t9_t5 += alt(MAS)
	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	t9_t5_in += alt(MAS_in)
	S += t9_t5_in*MAS_in[0]<=t9_t5*MAS[0]

	S += t9_t5_in*MAS_in[1]<=t9_t5*MAS[1]

	S += t9_t5_in*MAS_in[2]<=t9_t5*MAS[2]

	S += t9_t5_in*MAS_in[3]<=t9_t5*MAS[3]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	t9_t5_mem0 += MM_MEM[0]
	S += 29 < t9_t5_mem0
	S += t9_t5_mem0 <= t9_t5

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	t9_t5_mem1 += MM_MEM[1]
	S += 30 < t9_t5_mem1
	S += t9_t5_mem1 <= t9_t5

	t61 = S.Task('t61', length=2, delay_cost=1)
	t61 += alt(MAS)
	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	t61_in += alt(MAS_in)
	S += t61_in*MAS_in[0]<=t61*MAS[0]

	S += t61_in*MAS_in[1]<=t61*MAS[1]

	S += t61_in*MAS_in[2]<=t61*MAS[2]

	S += t61_in*MAS_in[3]<=t61*MAS[3]

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
	S += t61_mem1 <= t61

	t71 = S.Task('t71', length=2, delay_cost=1)
	t71 += alt(MAS)
	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	t71_in += alt(MAS_in)
	S += t71_in*MAS_in[0]<=t71*MAS[0]

	S += t71_in*MAS_in[1]<=t71*MAS[1]

	S += t71_in*MAS_in[2]<=t71*MAS[2]

	S += t71_in*MAS_in[3]<=t71*MAS[3]

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
	S += t71_mem1 <= t71

	t80 = S.Task('t80', length=2, delay_cost=1)
	t80 += alt(MAS)
	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	t80_in += alt(MAS_in)
	S += t80_in*MAS_in[0]<=t80*MAS[0]

	S += t80_in*MAS_in[1]<=t80*MAS[1]

	S += t80_in*MAS_in[2]<=t80*MAS[2]

	S += t80_in*MAS_in[3]<=t80*MAS[3]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t80_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < t80_mem0*MAS_MEM[2]
	S += (t60*MAS[2])-1 < t80_mem0*MAS_MEM[4]
	S += (t60*MAS[3])-1 < t80_mem0*MAS_MEM[6]
	S += t80_mem0 <= t80

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	t80_mem1 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t80_mem1*MAS_MEM[1]
	S += (t70*MAS[1])-1 < t80_mem1*MAS_MEM[3]
	S += (t70*MAS[2])-1 < t80_mem1*MAS_MEM[5]
	S += (t70*MAS[3])-1 < t80_mem1*MAS_MEM[7]
	S += t80_mem1 <= t80

	t91 = S.Task('t91', length=2, delay_cost=1)
	t91 += alt(MAS)
	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	t91_in += alt(MAS_in)
	S += t91_in*MAS_in[0]<=t91*MAS[0]

	S += t91_in*MAS_in[1]<=t91*MAS[1]

	S += t91_in*MAS_in[2]<=t91*MAS[2]

	S += t91_in*MAS_in[3]<=t91*MAS[3]

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
	S += t91_mem1 <= t91

	t100 = S.Task('t100', length=2, delay_cost=1)
	t100 += alt(MAS)
	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	t100_in += alt(MAS_in)
	S += t100_in*MAS_in[0]<=t100*MAS[0]

	S += t100_in*MAS_in[1]<=t100*MAS[1]

	S += t100_in*MAS_in[2]<=t100*MAS[2]

	S += t100_in*MAS_in[3]<=t100*MAS[3]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t100_mem0*MAS_MEM[0]
	S += (t90*MAS[1])-1 < t100_mem0*MAS_MEM[2]
	S += (t90*MAS[2])-1 < t100_mem0*MAS_MEM[4]
	S += (t90*MAS[3])-1 < t100_mem0*MAS_MEM[6]
	S += t100_mem0 <= t100

	t14_t0 = S.Task('t14_t0', length=4, delay_cost=1)
	t14_t0 += alt(MM)
	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	t14_t0_in += alt(MM_in)
	S += t14_t0>=t14_t0_in

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	t14_t0_mem0 += MAIN_MEM_r[0]
	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	t14_t0_mem1 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t14_t0_mem1*MAS_MEM[1]
	S += (t60*MAS[1])-1 < t14_t0_mem1*MAS_MEM[3]
	S += (t60*MAS[2])-1 < t14_t0_mem1*MAS_MEM[5]
	S += (t60*MAS[3])-1 < t14_t0_mem1*MAS_MEM[7]
	S += t14_t0_mem1 <= t14_t0

	new_TZ_t0 = S.Task('new_TZ_t0', length=4, delay_cost=1)
	new_TZ_t0 += alt(MM)
	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	new_TZ_t0_in += alt(MM_in)
	S += new_TZ_t0>=new_TZ_t0_in

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	new_TZ_t0_mem0 += MAIN_MEM_r[0]
	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	new_TZ_t0_mem1 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < new_TZ_t0_mem1*MAS_MEM[1]
	S += (t60*MAS[1])-1 < new_TZ_t0_mem1*MAS_MEM[3]
	S += (t60*MAS[2])-1 < new_TZ_t0_mem1*MAS_MEM[5]
	S += (t60*MAS[3])-1 < new_TZ_t0_mem1*MAS_MEM[7]
	S += new_TZ_t0_mem1 <= new_TZ_t0

	t81 = S.Task('t81', length=2, delay_cost=1)
	t81 += alt(MAS)
	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	t81_in += alt(MAS_in)
	S += t81_in*MAS_in[0]<=t81*MAS[0]

	S += t81_in*MAS_in[1]<=t81*MAS[1]

	S += t81_in*MAS_in[2]<=t81*MAS[2]

	S += t81_in*MAS_in[3]<=t81*MAS[3]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < t81_mem0*MAS_MEM[0]
	S += (t61*MAS[1])-1 < t81_mem0*MAS_MEM[2]
	S += (t61*MAS[2])-1 < t81_mem0*MAS_MEM[4]
	S += (t61*MAS[3])-1 < t81_mem0*MAS_MEM[6]
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += alt(MAS_MEM)
	S += (t71*MAS[0])-1 < t81_mem1*MAS_MEM[1]
	S += (t71*MAS[1])-1 < t81_mem1*MAS_MEM[3]
	S += (t71*MAS[2])-1 < t81_mem1*MAS_MEM[5]
	S += (t71*MAS[3])-1 < t81_mem1*MAS_MEM[7]
	S += t81_mem1 <= t81

	t101 = S.Task('t101', length=2, delay_cost=1)
	t101 += alt(MAS)
	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	t101_in += alt(MAS_in)
	S += t101_in*MAS_in[0]<=t101*MAS[0]

	S += t101_in*MAS_in[1]<=t101*MAS[1]

	S += t101_in*MAS_in[2]<=t101*MAS[2]

	S += t101_in*MAS_in[3]<=t101*MAS[3]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < t101_mem0*MAS_MEM[0]
	S += (t91*MAS[1])-1 < t101_mem0*MAS_MEM[2]
	S += (t91*MAS[2])-1 < t101_mem0*MAS_MEM[4]
	S += (t91*MAS[3])-1 < t101_mem0*MAS_MEM[6]
	S += t101_mem0 <= t101

	t110 = S.Task('t110', length=2, delay_cost=1)
	t110 += alt(MAS)
	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	t110_in += alt(MAS_in)
	S += t110_in*MAS_in[0]<=t110*MAS[0]

	S += t110_in*MAS_in[1]<=t110*MAS[1]

	S += t110_in*MAS_in[2]<=t110*MAS[2]

	S += t110_in*MAS_in[3]<=t110*MAS[3]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t110_mem0*MAS_MEM[0]
	S += (t80*MAS[1])-1 < t110_mem0*MAS_MEM[2]
	S += (t80*MAS[2])-1 < t110_mem0*MAS_MEM[4]
	S += (t80*MAS[3])-1 < t110_mem0*MAS_MEM[6]
	S += t110_mem0 <= t110

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	t110_mem1 += alt(MAS_MEM)
	S += (t100*MAS[0])-1 < t110_mem1*MAS_MEM[1]
	S += (t100*MAS[1])-1 < t110_mem1*MAS_MEM[3]
	S += (t100*MAS[2])-1 < t110_mem1*MAS_MEM[5]
	S += (t100*MAS[3])-1 < t110_mem1*MAS_MEM[7]
	S += t110_mem1 <= t110

	t14_t1 = S.Task('t14_t1', length=4, delay_cost=1)
	t14_t1 += alt(MM)
	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	t14_t1_in += alt(MM_in)
	S += t14_t1>=t14_t1_in

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	t14_t1_mem0 += MAIN_MEM_r[0]
	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	t14_t1_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < t14_t1_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < t14_t1_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < t14_t1_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < t14_t1_mem1*MAS_MEM[7]
	S += t14_t1_mem1 <= t14_t1

	t14_t3 = S.Task('t14_t3', length=2, delay_cost=1)
	t14_t3 += alt(MAS)
	t14_t3_in = S.Task('t14_t3_in', length=1, delay_cost=1)
	t14_t3_in += alt(MAS_in)
	S += t14_t3_in*MAS_in[0]<=t14_t3*MAS[0]

	S += t14_t3_in*MAS_in[1]<=t14_t3*MAS[1]

	S += t14_t3_in*MAS_in[2]<=t14_t3*MAS[2]

	S += t14_t3_in*MAS_in[3]<=t14_t3*MAS[3]

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	t14_t3_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t14_t3_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < t14_t3_mem0*MAS_MEM[2]
	S += (t60*MAS[2])-1 < t14_t3_mem0*MAS_MEM[4]
	S += (t60*MAS[3])-1 < t14_t3_mem0*MAS_MEM[6]
	S += t14_t3_mem0 <= t14_t3

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	t14_t3_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < t14_t3_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < t14_t3_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < t14_t3_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < t14_t3_mem1*MAS_MEM[7]
	S += t14_t3_mem1 <= t14_t3

	new_TZ_t1 = S.Task('new_TZ_t1', length=4, delay_cost=1)
	new_TZ_t1 += alt(MM)
	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	new_TZ_t1_in += alt(MM_in)
	S += new_TZ_t1>=new_TZ_t1_in

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	new_TZ_t1_mem0 += MAIN_MEM_r[0]
	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	new_TZ_t1_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < new_TZ_t1_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < new_TZ_t1_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < new_TZ_t1_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < new_TZ_t1_mem1*MAS_MEM[7]
	S += new_TZ_t1_mem1 <= new_TZ_t1

	new_TZ_t3 = S.Task('new_TZ_t3', length=2, delay_cost=1)
	new_TZ_t3 += alt(MAS)
	new_TZ_t3_in = S.Task('new_TZ_t3_in', length=1, delay_cost=1)
	new_TZ_t3_in += alt(MAS_in)
	S += new_TZ_t3_in*MAS_in[0]<=new_TZ_t3*MAS[0]

	S += new_TZ_t3_in*MAS_in[1]<=new_TZ_t3*MAS[1]

	S += new_TZ_t3_in*MAS_in[2]<=new_TZ_t3*MAS[2]

	S += new_TZ_t3_in*MAS_in[3]<=new_TZ_t3*MAS[3]

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	new_TZ_t3_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < new_TZ_t3_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < new_TZ_t3_mem0*MAS_MEM[2]
	S += (t60*MAS[2])-1 < new_TZ_t3_mem0*MAS_MEM[4]
	S += (t60*MAS[3])-1 < new_TZ_t3_mem0*MAS_MEM[6]
	S += new_TZ_t3_mem0 <= new_TZ_t3

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	new_TZ_t3_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < new_TZ_t3_mem1*MAS_MEM[1]
	S += (t61*MAS[1])-1 < new_TZ_t3_mem1*MAS_MEM[3]
	S += (t61*MAS[2])-1 < new_TZ_t3_mem1*MAS_MEM[5]
	S += (t61*MAS[3])-1 < new_TZ_t3_mem1*MAS_MEM[7]
	S += new_TZ_t3_mem1 <= new_TZ_t3

	t111 = S.Task('t111', length=2, delay_cost=1)
	t111 += alt(MAS)
	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	t111_in += alt(MAS_in)
	S += t111_in*MAS_in[0]<=t111*MAS[0]

	S += t111_in*MAS_in[1]<=t111*MAS[1]

	S += t111_in*MAS_in[2]<=t111*MAS[2]

	S += t111_in*MAS_in[3]<=t111*MAS[3]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t111_mem0*MAS_MEM[0]
	S += (t81*MAS[1])-1 < t111_mem0*MAS_MEM[2]
	S += (t81*MAS[2])-1 < t111_mem0*MAS_MEM[4]
	S += (t81*MAS[3])-1 < t111_mem0*MAS_MEM[6]
	S += t111_mem0 <= t111

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	t111_mem1 += alt(MAS_MEM)
	S += (t101*MAS[0])-1 < t111_mem1*MAS_MEM[1]
	S += (t101*MAS[1])-1 < t111_mem1*MAS_MEM[3]
	S += (t101*MAS[2])-1 < t111_mem1*MAS_MEM[5]
	S += (t101*MAS[3])-1 < t111_mem1*MAS_MEM[7]
	S += t111_mem1 <= t111

	t120 = S.Task('t120', length=2, delay_cost=1)
	t120 += alt(MAS)
	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	t120_in += alt(MAS_in)
	S += t120_in*MAS_in[0]<=t120*MAS[0]

	S += t120_in*MAS_in[1]<=t120*MAS[1]

	S += t120_in*MAS_in[2]<=t120*MAS[2]

	S += t120_in*MAS_in[3]<=t120*MAS[3]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < t120_mem0*MAS_MEM[0]
	S += (t110*MAS[1])-1 < t120_mem0*MAS_MEM[2]
	S += (t110*MAS[2])-1 < t120_mem0*MAS_MEM[4]
	S += (t110*MAS[3])-1 < t120_mem0*MAS_MEM[6]
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t120_mem1*MAS_MEM[1]
	S += (t90*MAS[1])-1 < t120_mem1*MAS_MEM[3]
	S += (t90*MAS[2])-1 < t120_mem1*MAS_MEM[5]
	S += (t90*MAS[3])-1 < t120_mem1*MAS_MEM[7]
	S += t120_mem1 <= t120

	new_TX_t0 = S.Task('new_TX_t0', length=4, delay_cost=1)
	new_TX_t0 += alt(MM)
	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	new_TX_t0_in += alt(MM_in)
	S += new_TX_t0>=new_TX_t0_in

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	new_TX_t0_mem0 += MAS_MEM[2]
	S += 9 < new_TX_t0_mem0
	S += new_TX_t0_mem0 <= new_TX_t0

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	new_TX_t0_mem1 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < new_TX_t0_mem1*MAS_MEM[1]
	S += (t110*MAS[1])-1 < new_TX_t0_mem1*MAS_MEM[3]
	S += (t110*MAS[2])-1 < new_TX_t0_mem1*MAS_MEM[5]
	S += (t110*MAS[3])-1 < new_TX_t0_mem1*MAS_MEM[7]
	S += new_TX_t0_mem1 <= new_TX_t0

	t14_t4 = S.Task('t14_t4', length=4, delay_cost=1)
	t14_t4 += alt(MM)
	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	t14_t4_in += alt(MM_in)
	S += t14_t4>=t14_t4_in

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	t14_t4_mem0 += MAS_MEM[6]
	S += 3 < t14_t4_mem0
	S += t14_t4_mem0 <= t14_t4

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	t14_t4_mem1 += alt(MAS_MEM)
	S += (t14_t3*MAS[0])-1 < t14_t4_mem1*MAS_MEM[1]
	S += (t14_t3*MAS[1])-1 < t14_t4_mem1*MAS_MEM[3]
	S += (t14_t3*MAS[2])-1 < t14_t4_mem1*MAS_MEM[5]
	S += (t14_t3*MAS[3])-1 < t14_t4_mem1*MAS_MEM[7]
	S += t14_t4_mem1 <= t14_t4

	t140 = S.Task('t140', length=2, delay_cost=1)
	t140 += alt(MAS)
	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	t140_in += alt(MAS_in)
	S += t140_in*MAS_in[0]<=t140*MAS[0]

	S += t140_in*MAS_in[1]<=t140*MAS[1]

	S += t140_in*MAS_in[2]<=t140*MAS[2]

	S += t140_in*MAS_in[3]<=t140*MAS[3]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(MM_MEM)
	S += (t14_t0*MM[0])-1 < t140_mem0*MM_MEM[0]
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += alt(MM_MEM)
	S += (t14_t1*MM[0])-1 < t140_mem1*MM_MEM[1]
	S += t140_mem1 <= t140

	t14_t5 = S.Task('t14_t5', length=2, delay_cost=1)
	t14_t5 += alt(MAS)
	t14_t5_in = S.Task('t14_t5_in', length=1, delay_cost=1)
	t14_t5_in += alt(MAS_in)
	S += t14_t5_in*MAS_in[0]<=t14_t5*MAS[0]

	S += t14_t5_in*MAS_in[1]<=t14_t5*MAS[1]

	S += t14_t5_in*MAS_in[2]<=t14_t5*MAS[2]

	S += t14_t5_in*MAS_in[3]<=t14_t5*MAS[3]

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	t14_t5_mem0 += alt(MM_MEM)
	S += (t14_t0*MM[0])-1 < t14_t5_mem0*MM_MEM[0]
	S += t14_t5_mem0 <= t14_t5

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	t14_t5_mem1 += alt(MM_MEM)
	S += (t14_t1*MM[0])-1 < t14_t5_mem1*MM_MEM[1]
	S += t14_t5_mem1 <= t14_t5

	new_TZ_t4 = S.Task('new_TZ_t4', length=4, delay_cost=1)
	new_TZ_t4 += alt(MM)
	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	new_TZ_t4_in += alt(MM_in)
	S += new_TZ_t4>=new_TZ_t4_in

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	new_TZ_t4_mem0 += MAS_MEM[6]
	S += 2 < new_TZ_t4_mem0
	S += new_TZ_t4_mem0 <= new_TZ_t4

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	new_TZ_t4_mem1 += alt(MAS_MEM)
	S += (new_TZ_t3*MAS[0])-1 < new_TZ_t4_mem1*MAS_MEM[1]
	S += (new_TZ_t3*MAS[1])-1 < new_TZ_t4_mem1*MAS_MEM[3]
	S += (new_TZ_t3*MAS[2])-1 < new_TZ_t4_mem1*MAS_MEM[5]
	S += (new_TZ_t3*MAS[3])-1 < new_TZ_t4_mem1*MAS_MEM[7]
	S += new_TZ_t4_mem1 <= new_TZ_t4

	new_TZ0 = S.Task('new_TZ0', length=2, delay_cost=1)
	new_TZ0 += alt(MAS)
	new_TZ0_in = S.Task('new_TZ0_in', length=1, delay_cost=1)
	new_TZ0_in += alt(MAS_in)
	S += new_TZ0_in*MAS_in[0]<=new_TZ0*MAS[0]

	S += new_TZ0_in*MAS_in[1]<=new_TZ0*MAS[1]

	S += new_TZ0_in*MAS_in[2]<=new_TZ0*MAS[2]

	S += new_TZ0_in*MAS_in[3]<=new_TZ0*MAS[3]

	S += 31<new_TZ0

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

	new_TZ_t5 = S.Task('new_TZ_t5', length=2, delay_cost=1)
	new_TZ_t5 += alt(MAS)
	new_TZ_t5_in = S.Task('new_TZ_t5_in', length=1, delay_cost=1)
	new_TZ_t5_in += alt(MAS_in)
	S += new_TZ_t5_in*MAS_in[0]<=new_TZ_t5*MAS[0]

	S += new_TZ_t5_in*MAS_in[1]<=new_TZ_t5*MAS[1]

	S += new_TZ_t5_in*MAS_in[2]<=new_TZ_t5*MAS[2]

	S += new_TZ_t5_in*MAS_in[3]<=new_TZ_t5*MAS[3]

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	new_TZ_t5_mem0 += alt(MM_MEM)
	S += (new_TZ_t0*MM[0])-1 < new_TZ_t5_mem0*MM_MEM[0]
	S += new_TZ_t5_mem0 <= new_TZ_t5

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	new_TZ_t5_mem1 += alt(MM_MEM)
	S += (new_TZ_t1*MM[0])-1 < new_TZ_t5_mem1*MM_MEM[1]
	S += new_TZ_t5_mem1 <= new_TZ_t5

	t121 = S.Task('t121', length=2, delay_cost=1)
	t121 += alt(MAS)
	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	t121_in += alt(MAS_in)
	S += t121_in*MAS_in[0]<=t121*MAS[0]

	S += t121_in*MAS_in[1]<=t121*MAS[1]

	S += t121_in*MAS_in[2]<=t121*MAS[2]

	S += t121_in*MAS_in[3]<=t121*MAS[3]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	t121_mem0 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < t121_mem0*MAS_MEM[0]
	S += (t111*MAS[1])-1 < t121_mem0*MAS_MEM[2]
	S += (t111*MAS[2])-1 < t121_mem0*MAS_MEM[4]
	S += (t111*MAS[3])-1 < t121_mem0*MAS_MEM[6]
	S += t121_mem0 <= t121

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	t121_mem1 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < t121_mem1*MAS_MEM[1]
	S += (t91*MAS[1])-1 < t121_mem1*MAS_MEM[3]
	S += (t91*MAS[2])-1 < t121_mem1*MAS_MEM[5]
	S += (t91*MAS[3])-1 < t121_mem1*MAS_MEM[7]
	S += t121_mem1 <= t121

	new_TX_t1 = S.Task('new_TX_t1', length=4, delay_cost=1)
	new_TX_t1 += alt(MM)
	new_TX_t1_in = S.Task('new_TX_t1_in', length=1, delay_cost=1)
	new_TX_t1_in += alt(MM_in)
	S += new_TX_t1>=new_TX_t1_in

	new_TX_t1_mem0 = S.Task('new_TX_t1_mem0', length=1, delay_cost=1)
	new_TX_t1_mem0 += MAS_MEM[0]
	S += 13 < new_TX_t1_mem0
	S += new_TX_t1_mem0 <= new_TX_t1

	new_TX_t1_mem1 = S.Task('new_TX_t1_mem1', length=1, delay_cost=1)
	new_TX_t1_mem1 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < new_TX_t1_mem1*MAS_MEM[1]
	S += (t111*MAS[1])-1 < new_TX_t1_mem1*MAS_MEM[3]
	S += (t111*MAS[2])-1 < new_TX_t1_mem1*MAS_MEM[5]
	S += (t111*MAS[3])-1 < new_TX_t1_mem1*MAS_MEM[7]
	S += new_TX_t1_mem1 <= new_TX_t1

	new_TX_t3 = S.Task('new_TX_t3', length=2, delay_cost=1)
	new_TX_t3 += alt(MAS)
	new_TX_t3_in = S.Task('new_TX_t3_in', length=1, delay_cost=1)
	new_TX_t3_in += alt(MAS_in)
	S += new_TX_t3_in*MAS_in[0]<=new_TX_t3*MAS[0]

	S += new_TX_t3_in*MAS_in[1]<=new_TX_t3*MAS[1]

	S += new_TX_t3_in*MAS_in[2]<=new_TX_t3*MAS[2]

	S += new_TX_t3_in*MAS_in[3]<=new_TX_t3*MAS[3]

	new_TX_t3_mem0 = S.Task('new_TX_t3_mem0', length=1, delay_cost=1)
	new_TX_t3_mem0 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < new_TX_t3_mem0*MAS_MEM[0]
	S += (t110*MAS[1])-1 < new_TX_t3_mem0*MAS_MEM[2]
	S += (t110*MAS[2])-1 < new_TX_t3_mem0*MAS_MEM[4]
	S += (t110*MAS[3])-1 < new_TX_t3_mem0*MAS_MEM[6]
	S += new_TX_t3_mem0 <= new_TX_t3

	new_TX_t3_mem1 = S.Task('new_TX_t3_mem1', length=1, delay_cost=1)
	new_TX_t3_mem1 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < new_TX_t3_mem1*MAS_MEM[1]
	S += (t111*MAS[1])-1 < new_TX_t3_mem1*MAS_MEM[3]
	S += (t111*MAS[2])-1 < new_TX_t3_mem1*MAS_MEM[5]
	S += (t111*MAS[3])-1 < new_TX_t3_mem1*MAS_MEM[7]
	S += new_TX_t3_mem1 <= new_TX_t3

	t13_t0 = S.Task('t13_t0', length=4, delay_cost=1)
	t13_t0 += alt(MM)
	t13_t0_in = S.Task('t13_t0_in', length=1, delay_cost=1)
	t13_t0_in += alt(MM_in)
	S += t13_t0>=t13_t0_in

	t13_t0_mem0 = S.Task('t13_t0_mem0', length=1, delay_cost=1)
	t13_t0_mem0 += MAS_MEM[6]
	S += 11 < t13_t0_mem0
	S += t13_t0_mem0 <= t13_t0

	t13_t0_mem1 = S.Task('t13_t0_mem1', length=1, delay_cost=1)
	t13_t0_mem1 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t13_t0_mem1*MAS_MEM[1]
	S += (t120*MAS[1])-1 < t13_t0_mem1*MAS_MEM[3]
	S += (t120*MAS[2])-1 < t13_t0_mem1*MAS_MEM[5]
	S += (t120*MAS[3])-1 < t13_t0_mem1*MAS_MEM[7]
	S += t13_t0_mem1 <= t13_t0

	t141 = S.Task('t141', length=2, delay_cost=1)
	t141 += alt(MAS)
	t141_in = S.Task('t141_in', length=1, delay_cost=1)
	t141_in += alt(MAS_in)
	S += t141_in*MAS_in[0]<=t141*MAS[0]

	S += t141_in*MAS_in[1]<=t141*MAS[1]

	S += t141_in*MAS_in[2]<=t141*MAS[2]

	S += t141_in*MAS_in[3]<=t141*MAS[3]

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
	S += t141_mem1 <= t141

	new_TZ1 = S.Task('new_TZ1', length=2, delay_cost=1)
	new_TZ1 += alt(MAS)
	new_TZ1_in = S.Task('new_TZ1_in', length=1, delay_cost=1)
	new_TZ1_in += alt(MAS_in)
	S += new_TZ1_in*MAS_in[0]<=new_TZ1*MAS[0]

	S += new_TZ1_in*MAS_in[1]<=new_TZ1*MAS[1]

	S += new_TZ1_in*MAS_in[2]<=new_TZ1*MAS[2]

	S += new_TZ1_in*MAS_in[3]<=new_TZ1*MAS[3]

	S += 30<new_TZ1

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
	S += new_TZ1_mem1 <= new_TZ1

	new_TX_t4 = S.Task('new_TX_t4', length=4, delay_cost=1)
	new_TX_t4 += alt(MM)
	new_TX_t4_in = S.Task('new_TX_t4_in', length=1, delay_cost=1)
	new_TX_t4_in += alt(MM_in)
	S += new_TX_t4>=new_TX_t4_in

	new_TX_t4_mem0 = S.Task('new_TX_t4_mem0', length=1, delay_cost=1)
	new_TX_t4_mem0 += MAS_MEM[6]
	S += 25 < new_TX_t4_mem0
	S += new_TX_t4_mem0 <= new_TX_t4

	new_TX_t4_mem1 = S.Task('new_TX_t4_mem1', length=1, delay_cost=1)
	new_TX_t4_mem1 += alt(MAS_MEM)
	S += (new_TX_t3*MAS[0])-1 < new_TX_t4_mem1*MAS_MEM[1]
	S += (new_TX_t3*MAS[1])-1 < new_TX_t4_mem1*MAS_MEM[3]
	S += (new_TX_t3*MAS[2])-1 < new_TX_t4_mem1*MAS_MEM[5]
	S += (new_TX_t3*MAS[3])-1 < new_TX_t4_mem1*MAS_MEM[7]
	S += new_TX_t4_mem1 <= new_TX_t4

	new_TX0 = S.Task('new_TX0', length=2, delay_cost=1)
	new_TX0 += alt(MAS)
	new_TX0_in = S.Task('new_TX0_in', length=1, delay_cost=1)
	new_TX0_in += alt(MAS_in)
	S += new_TX0_in*MAS_in[0]<=new_TX0*MAS[0]

	S += new_TX0_in*MAS_in[1]<=new_TX0*MAS[1]

	S += new_TX0_in*MAS_in[2]<=new_TX0*MAS[2]

	S += new_TX0_in*MAS_in[3]<=new_TX0*MAS[3]

	S += 26<new_TX0

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

	new_TX_t5 = S.Task('new_TX_t5', length=2, delay_cost=1)
	new_TX_t5 += alt(MAS)
	new_TX_t5_in = S.Task('new_TX_t5_in', length=1, delay_cost=1)
	new_TX_t5_in += alt(MAS_in)
	S += new_TX_t5_in*MAS_in[0]<=new_TX_t5*MAS[0]

	S += new_TX_t5_in*MAS_in[1]<=new_TX_t5*MAS[1]

	S += new_TX_t5_in*MAS_in[2]<=new_TX_t5*MAS[2]

	S += new_TX_t5_in*MAS_in[3]<=new_TX_t5*MAS[3]

	new_TX_t5_mem0 = S.Task('new_TX_t5_mem0', length=1, delay_cost=1)
	new_TX_t5_mem0 += alt(MM_MEM)
	S += (new_TX_t0*MM[0])-1 < new_TX_t5_mem0*MM_MEM[0]
	S += new_TX_t5_mem0 <= new_TX_t5

	new_TX_t5_mem1 = S.Task('new_TX_t5_mem1', length=1, delay_cost=1)
	new_TX_t5_mem1 += alt(MM_MEM)
	S += (new_TX_t1*MM[0])-1 < new_TX_t5_mem1*MM_MEM[1]
	S += new_TX_t5_mem1 <= new_TX_t5

	t13_t1 = S.Task('t13_t1', length=4, delay_cost=1)
	t13_t1 += alt(MM)
	t13_t1_in = S.Task('t13_t1_in', length=1, delay_cost=1)
	t13_t1_in += alt(MM_in)
	S += t13_t1>=t13_t1_in

	t13_t1_mem0 = S.Task('t13_t1_mem0', length=1, delay_cost=1)
	t13_t1_mem0 += MAS_MEM[0]
	S += 14 < t13_t1_mem0
	S += t13_t1_mem0 <= t13_t1

	t13_t1_mem1 = S.Task('t13_t1_mem1', length=1, delay_cost=1)
	t13_t1_mem1 += alt(MAS_MEM)
	S += (t121*MAS[0])-1 < t13_t1_mem1*MAS_MEM[1]
	S += (t121*MAS[1])-1 < t13_t1_mem1*MAS_MEM[3]
	S += (t121*MAS[2])-1 < t13_t1_mem1*MAS_MEM[5]
	S += (t121*MAS[3])-1 < t13_t1_mem1*MAS_MEM[7]
	S += t13_t1_mem1 <= t13_t1

	t13_t3 = S.Task('t13_t3', length=2, delay_cost=1)
	t13_t3 += alt(MAS)
	t13_t3_in = S.Task('t13_t3_in', length=1, delay_cost=1)
	t13_t3_in += alt(MAS_in)
	S += t13_t3_in*MAS_in[0]<=t13_t3*MAS[0]

	S += t13_t3_in*MAS_in[1]<=t13_t3*MAS[1]

	S += t13_t3_in*MAS_in[2]<=t13_t3*MAS[2]

	S += t13_t3_in*MAS_in[3]<=t13_t3*MAS[3]

	t13_t3_mem0 = S.Task('t13_t3_mem0', length=1, delay_cost=1)
	t13_t3_mem0 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t13_t3_mem0*MAS_MEM[0]
	S += (t120*MAS[1])-1 < t13_t3_mem0*MAS_MEM[2]
	S += (t120*MAS[2])-1 < t13_t3_mem0*MAS_MEM[4]
	S += (t120*MAS[3])-1 < t13_t3_mem0*MAS_MEM[6]
	S += t13_t3_mem0 <= t13_t3

	t13_t3_mem1 = S.Task('t13_t3_mem1', length=1, delay_cost=1)
	t13_t3_mem1 += alt(MAS_MEM)
	S += (t121*MAS[0])-1 < t13_t3_mem1*MAS_MEM[1]
	S += (t121*MAS[1])-1 < t13_t3_mem1*MAS_MEM[3]
	S += (t121*MAS[2])-1 < t13_t3_mem1*MAS_MEM[5]
	S += (t121*MAS[3])-1 < t13_t3_mem1*MAS_MEM[7]
	S += t13_t3_mem1 <= t13_t3

	new_TX1 = S.Task('new_TX1', length=2, delay_cost=1)
	new_TX1 += alt(MAS)
	new_TX1_in = S.Task('new_TX1_in', length=1, delay_cost=1)
	new_TX1_in += alt(MAS_in)
	S += new_TX1_in*MAS_in[0]<=new_TX1*MAS[0]

	S += new_TX1_in*MAS_in[1]<=new_TX1*MAS[1]

	S += new_TX1_in*MAS_in[2]<=new_TX1*MAS[2]

	S += new_TX1_in*MAS_in[3]<=new_TX1*MAS[3]

	S += 27<new_TX1

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
	S += new_TX1_mem1 <= new_TX1

	t13_t4 = S.Task('t13_t4', length=4, delay_cost=1)
	t13_t4 += alt(MM)
	t13_t4_in = S.Task('t13_t4_in', length=1, delay_cost=1)
	t13_t4_in += alt(MM_in)
	S += t13_t4>=t13_t4_in

	t13_t4_mem0 = S.Task('t13_t4_mem0', length=1, delay_cost=1)
	t13_t4_mem0 += MAS_MEM[2]
	S += 26 < t13_t4_mem0
	S += t13_t4_mem0 <= t13_t4

	t13_t4_mem1 = S.Task('t13_t4_mem1', length=1, delay_cost=1)
	t13_t4_mem1 += alt(MAS_MEM)
	S += (t13_t3*MAS[0])-1 < t13_t4_mem1*MAS_MEM[1]
	S += (t13_t3*MAS[1])-1 < t13_t4_mem1*MAS_MEM[3]
	S += (t13_t3*MAS[2])-1 < t13_t4_mem1*MAS_MEM[5]
	S += (t13_t3*MAS[3])-1 < t13_t4_mem1*MAS_MEM[7]
	S += t13_t4_mem1 <= t13_t4

	t130 = S.Task('t130', length=2, delay_cost=1)
	t130 += alt(MAS)
	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	t130_in += alt(MAS_in)
	S += t130_in*MAS_in[0]<=t130*MAS[0]

	S += t130_in*MAS_in[1]<=t130*MAS[1]

	S += t130_in*MAS_in[2]<=t130*MAS[2]

	S += t130_in*MAS_in[3]<=t130*MAS[3]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	t130_mem0 += alt(MM_MEM)
	S += (t13_t0*MM[0])-1 < t130_mem0*MM_MEM[0]
	S += t130_mem0 <= t130

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	t130_mem1 += alt(MM_MEM)
	S += (t13_t1*MM[0])-1 < t130_mem1*MM_MEM[1]
	S += t130_mem1 <= t130

	t13_t5 = S.Task('t13_t5', length=2, delay_cost=1)
	t13_t5 += alt(MAS)
	t13_t5_in = S.Task('t13_t5_in', length=1, delay_cost=1)
	t13_t5_in += alt(MAS_in)
	S += t13_t5_in*MAS_in[0]<=t13_t5*MAS[0]

	S += t13_t5_in*MAS_in[1]<=t13_t5*MAS[1]

	S += t13_t5_in*MAS_in[2]<=t13_t5*MAS[2]

	S += t13_t5_in*MAS_in[3]<=t13_t5*MAS[3]

	t13_t5_mem0 = S.Task('t13_t5_mem0', length=1, delay_cost=1)
	t13_t5_mem0 += alt(MM_MEM)
	S += (t13_t0*MM[0])-1 < t13_t5_mem0*MM_MEM[0]
	S += t13_t5_mem0 <= t13_t5

	t13_t5_mem1 = S.Task('t13_t5_mem1', length=1, delay_cost=1)
	t13_t5_mem1 += alt(MM_MEM)
	S += (t13_t1*MM[0])-1 < t13_t5_mem1*MM_MEM[1]
	S += t13_t5_mem1 <= t13_t5

	t131 = S.Task('t131', length=2, delay_cost=1)
	t131 += alt(MAS)
	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	t131_in += alt(MAS_in)
	S += t131_in*MAS_in[0]<=t131*MAS[0]

	S += t131_in*MAS_in[1]<=t131*MAS[1]

	S += t131_in*MAS_in[2]<=t131*MAS[2]

	S += t131_in*MAS_in[3]<=t131*MAS[3]

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
	S += t131_mem1 <= t131

	t150 = S.Task('t150', length=2, delay_cost=1)
	t150 += alt(MAS)
	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	t150_in += alt(MAS_in)
	S += t150_in*MAS_in[0]<=t150*MAS[0]

	S += t150_in*MAS_in[1]<=t150*MAS[1]

	S += t150_in*MAS_in[2]<=t150*MAS[2]

	S += t150_in*MAS_in[3]<=t150*MAS[3]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += alt(MAS_MEM)
	S += (t130*MAS[0])-1 < t150_mem0*MAS_MEM[0]
	S += (t130*MAS[1])-1 < t150_mem0*MAS_MEM[2]
	S += (t130*MAS[2])-1 < t150_mem0*MAS_MEM[4]
	S += (t130*MAS[3])-1 < t150_mem0*MAS_MEM[6]
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < t150_mem1*MAS_MEM[1]
	S += (t140*MAS[1])-1 < t150_mem1*MAS_MEM[3]
	S += (t140*MAS[2])-1 < t150_mem1*MAS_MEM[5]
	S += (t140*MAS[3])-1 < t150_mem1*MAS_MEM[7]
	S += t150_mem1 <= t150

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage2MAS4/EP2_ADD_w_EVAL/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

