from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 121
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling
	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 0
	t0_t1_in += MM_in[0]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 0
	t0_t1_mem0 += MAIN_MEM_r

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 0
	t0_t1_mem1 += MAIN_MEM_r

	t0_t1 = S.Task('t0_t1', length=5, delay_cost=1)
	S += t0_t1 >= 1
	t0_t1 += MM[0]

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	S += t2_t0_in >= 1
	t2_t0_in += MM_in[0]

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	S += t2_t0_mem0 >= 1
	t2_t0_mem0 += MAIN_MEM_r

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	S += t2_t0_mem1 >= 1
	t2_t0_mem1 += MAIN_MEM_r

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 2
	t0_t0_in += MM_in[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 2
	t0_t0_mem0 += MAIN_MEM_r

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 2
	t0_t0_mem1 += MAIN_MEM_r

	t2_t0 = S.Task('t2_t0', length=5, delay_cost=1)
	S += t2_t0 >= 2
	t2_t0 += MM[0]

	t0_t0 = S.Task('t0_t0', length=5, delay_cost=1)
	S += t0_t0 >= 3
	t0_t0 += MM[0]

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	S += t2_t1_in >= 3
	t2_t1_in += MM_in[0]

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	S += t2_t1_mem0 >= 3
	t2_t1_mem0 += MAIN_MEM_r

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	S += t2_t1_mem1 >= 3
	t2_t1_mem1 += MAIN_MEM_r

	t2_t1 = S.Task('t2_t1', length=5, delay_cost=1)
	S += t2_t1 >= 4
	t2_t1 += MM[0]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 4
	t9_t2_mem0 += MAIN_MEM_r

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 4
	t9_t2_mem1 += MAIN_MEM_r

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 5
	t7_t2_mem0 += MAIN_MEM_r

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 5
	t7_t2_mem1 += MAIN_MEM_r

	t9_t2 = S.Task('t9_t2', length=1, delay_cost=1)
	S += t9_t2 >= 5
	t9_t2 += MAS[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 6
	t0_t3_mem0 += MAIN_MEM_r

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 6
	t0_t3_mem1 += MAIN_MEM_r

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 6
	t7_t2 += MAS[0]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	S += new_TZ_t2_mem0 >= 7
	new_TZ_t2_mem0 += MAIN_MEM_r

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	S += new_TZ_t2_mem1 >= 7
	new_TZ_t2_mem1 += MAIN_MEM_r

	t0_t3 = S.Task('t0_t3', length=1, delay_cost=1)
	S += t0_t3 >= 7
	t0_t3 += MAS[3]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 7
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 7
	t0_t5_mem1 += MM_MEM[0]

	new_TZ_t2 = S.Task('new_TZ_t2', length=1, delay_cost=1)
	S += new_TZ_t2 >= 8
	new_TZ_t2 += MAS[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 8
	t0_t5 += MAS[2]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 8
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 8
	t20_mem1 += MM_MEM[0]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	S += t2_t3_mem0 >= 8
	t2_t3_mem0 += MAIN_MEM_r

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	S += t2_t3_mem1 >= 8
	t2_t3_mem1 += MAIN_MEM_r

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 9
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 9
	t00_mem1 += MM_MEM[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 9
	t0_t2_mem0 += MAIN_MEM_r

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 9
	t0_t2_mem1 += MAIN_MEM_r

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 9
	t20 += MAS[1]

	t2_t3 = S.Task('t2_t3', length=1, delay_cost=1)
	S += t2_t3 >= 9
	t2_t3 += MAS[3]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 10
	t00 += MAS[1]

	t0_t2 = S.Task('t0_t2', length=1, delay_cost=1)
	S += t0_t2 >= 10
	t0_t2 += MAS[2]

	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	S += t0_t4_in >= 10
	t0_t4_in += MM_in[0]

	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	S += t0_t4_mem0 >= 10
	t0_t4_mem0 += MAS_MEM[2]

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	S += t0_t4_mem1 >= 10
	t0_t4_mem1 += MAS_MEM[3]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	S += t14_t2_mem0 >= 10
	t14_t2_mem0 += MAIN_MEM_r

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	S += t14_t2_mem1 >= 10
	t14_t2_mem1 += MAIN_MEM_r

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	S += t2_t5_mem0 >= 10
	t2_t5_mem0 += MM_MEM[0]

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	S += t2_t5_mem1 >= 10
	t2_t5_mem1 += MM_MEM[0]

	t0_t4 = S.Task('t0_t4', length=5, delay_cost=1)
	S += t0_t4 >= 11
	t0_t4 += MM[0]

	t14_t2 = S.Task('t14_t2', length=1, delay_cost=1)
	S += t14_t2 >= 11
	t14_t2 += MAS[0]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	S += t2_t2_mem0 >= 11
	t2_t2_mem0 += MAIN_MEM_r

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	S += t2_t2_mem1 >= 11
	t2_t2_mem1 += MAIN_MEM_r

	t2_t5 = S.Task('t2_t5', length=1, delay_cost=1)
	S += t2_t5 >= 11
	t2_t5 += MAS[1]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	S += t16_t2_mem0 >= 12
	t16_t2_mem0 += MAIN_MEM_r

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	S += t16_t2_mem1 >= 12
	t16_t2_mem1 += MAIN_MEM_r

	t2_t2 = S.Task('t2_t2', length=1, delay_cost=1)
	S += t2_t2 >= 12
	t2_t2 += MAS[2]

	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	S += t2_t4_in >= 12
	t2_t4_in += MM_in[0]

	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	S += t2_t4_mem0 >= 12
	t2_t4_mem0 += MAS_MEM[2]

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	S += t2_t4_mem1 >= 12
	t2_t4_mem1 += MAS_MEM[3]

	t16_t2 = S.Task('t16_t2', length=1, delay_cost=1)
	S += t16_t2 >= 13
	t16_t2 += MAS[0]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	S += t17_t2_mem0 >= 13
	t17_t2_mem0 += MAIN_MEM_r

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	S += t17_t2_mem1 >= 13
	t17_t2_mem1 += MAIN_MEM_r

	t2_t4 = S.Task('t2_t4', length=5, delay_cost=1)
	S += t2_t4 >= 13
	t2_t4 += MM[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 14
	t10_mem0 += MAIN_MEM_r

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 14
	t10_mem1 += MAS_MEM[1]

	t17_t2 = S.Task('t17_t2', length=1, delay_cost=1)
	S += t17_t2 >= 14
	t17_t2 += MAS[2]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 14
	t30_mem0 += MAIN_MEM_r

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 14
	t30_mem1 += MAS_MEM[1]

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 15
	c200_in += MM_in[0]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 15
	c200_mem0 += MAS_MEM[0]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 15
	c200_mem1 += MAIN_MEM_r

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 15
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 15
	t01_mem1 += MAS_MEM[2]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 15
	t10 += MAS[0]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 15
	t30 += MAS[1]

	c200 = S.Task('c200', length=5, delay_cost=1)
	S += c200 >= 16
	c200 += MM[0]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 16
	t01 += MAS[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 16
	t11_mem0 += MAIN_MEM_r

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 16
	t11_mem1 += MAS_MEM[1]

	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	S += t17_t0_in >= 16
	t17_t0_in += MM_in[0]

	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	S += t17_t0_mem0 >= 16
	t17_t0_mem0 += MAIN_MEM_r

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	S += t17_t0_mem1 >= 16
	t17_t0_mem1 += MAS_MEM[0]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 17
	t11 += MAS[2]

	t17_t0 = S.Task('t17_t0', length=5, delay_cost=1)
	S += t17_t0 >= 17
	t17_t0 += MM[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 17
	t21_mem0 += MM_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 17
	t21_mem1 += MAS_MEM[1]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 17
	t4_t0_mem0 += MAS_MEM[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 17
	t4_t0_mem1 += MAS_MEM[2]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 17
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 17
	t4_t3_mem0 += MAS_MEM[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 17
	t4_t3_mem1 += MAS_MEM[2]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 18
	c010_in += MM_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 18
	c010_mem0 += MAS_MEM[1]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 18
	c010_mem1 += MAIN_MEM_r

	t13_t2_mem0 = S.Task('t13_t2_mem0', length=1, delay_cost=1)
	S += t13_t2_mem0 >= 18
	t13_t2_mem0 += MAS_MEM[0]

	t13_t2_mem1 = S.Task('t13_t2_mem1', length=1, delay_cost=1)
	S += t13_t2_mem1 >= 18
	t13_t2_mem1 += MAS_MEM[2]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 18
	t21 += MAS[1]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 18
	t31_mem0 += MAIN_MEM_r

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 18
	t31_mem1 += MAS_MEM[1]

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	S += t4_t0 >= 18
	t4_t0 += MAS[2]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 18
	t4_t1_mem0 += MAS_MEM[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 18
	t4_t1_mem1 += MAS_MEM[2]

	t4_t3 = S.Task('t4_t3', length=5, delay_cost=1)
	S += t4_t3 >= 18
	t4_t3 += MM[0]

	c010 = S.Task('c010', length=5, delay_cost=1)
	S += c010 >= 19
	c010 += MM[0]

	t13_t2 = S.Task('t13_t2', length=1, delay_cost=1)
	S += t13_t2 >= 19
	t13_t2 += MAS[2]

	t17_t1_in = S.Task('t17_t1_in', length=1, delay_cost=1)
	S += t17_t1_in >= 19
	t17_t1_in += MM_in[0]

	t17_t1_mem0 = S.Task('t17_t1_mem0', length=1, delay_cost=1)
	S += t17_t1_mem0 >= 19
	t17_t1_mem0 += MAIN_MEM_r

	t17_t1_mem1 = S.Task('t17_t1_mem1', length=1, delay_cost=1)
	S += t17_t1_mem1 >= 19
	t17_t1_mem1 += MAS_MEM[2]

	t17_t3_mem0 = S.Task('t17_t3_mem0', length=1, delay_cost=1)
	S += t17_t3_mem0 >= 19
	t17_t3_mem0 += MAS_MEM[0]

	t17_t3_mem1 = S.Task('t17_t3_mem1', length=1, delay_cost=1)
	S += t17_t3_mem1 >= 19
	t17_t3_mem1 += MAS_MEM[2]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 19
	t31 += MAS[3]

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	S += t4_t1 >= 19
	t4_t1 += MAS[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 19
	t5_t1_mem0 += MAS_MEM[1]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 19
	t5_t1_mem1 += MAS_MEM[3]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 19
	t6_t2_mem0 += MAS_MEM[1]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 19
	t6_t2_mem1 += MAS_MEM[3]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 20
	c201_in += MM_in[0]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 20
	c201_mem0 += MAS_MEM[2]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 20
	c201_mem1 += MAIN_MEM_r

	new_TX_t2_mem0 = S.Task('new_TX_t2_mem0', length=1, delay_cost=1)
	S += new_TX_t2_mem0 >= 20
	new_TX_t2_mem0 += MAS_MEM[1]

	new_TX_t2_mem1 = S.Task('new_TX_t2_mem1', length=1, delay_cost=1)
	S += new_TX_t2_mem1 >= 20
	new_TX_t2_mem1 += MAS_MEM[3]

	t16_t3_mem0 = S.Task('t16_t3_mem0', length=1, delay_cost=1)
	S += t16_t3_mem0 >= 20
	t16_t3_mem0 += MAS_MEM[1]

	t16_t3_mem1 = S.Task('t16_t3_mem1', length=1, delay_cost=1)
	S += t16_t3_mem1 >= 20
	t16_t3_mem1 += MAS_MEM[3]

	t17_t1 = S.Task('t17_t1', length=5, delay_cost=1)
	S += t17_t1 >= 20
	t17_t1 += MM[0]

	t17_t3 = S.Task('t17_t3', length=1, delay_cost=1)
	S += t17_t3 >= 20
	t17_t3 += MAS[1]

	t5_t1 = S.Task('t5_t1', length=1, delay_cost=1)
	S += t5_t1 >= 20
	t5_t1 += MAS[2]

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	S += t6_t2 >= 20
	t6_t2 += MAS[0]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 21
	c200_w += MAIN_MEM_w

	c201 = S.Task('c201', length=5, delay_cost=1)
	S += c201 >= 21
	c201 += MM[0]

	new_TX_t2 = S.Task('new_TX_t2', length=1, delay_cost=1)
	S += new_TX_t2 >= 21
	new_TX_t2 += MAS[2]

	t16_t3 = S.Task('t16_t3', length=1, delay_cost=1)
	S += t16_t3 >= 21
	t16_t3 += MAS[3]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 21
	t5_t0_mem0 += MAS_MEM[1]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 21
	t5_t0_mem1 += MAS_MEM[3]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 21
	t5_t3_in += MM_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 21
	t5_t3_mem0 += MAS_MEM[1]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 21
	t5_t3_mem1 += MAS_MEM[3]

	t16_t1_in = S.Task('t16_t1_in', length=1, delay_cost=1)
	S += t16_t1_in >= 22
	t16_t1_in += MM_in[0]

	t16_t1_mem0 = S.Task('t16_t1_mem0', length=1, delay_cost=1)
	S += t16_t1_mem0 >= 22
	t16_t1_mem0 += MAIN_MEM_r

	t16_t1_mem1 = S.Task('t16_t1_mem1', length=1, delay_cost=1)
	S += t16_t1_mem1 >= 22
	t16_t1_mem1 += MAS_MEM[3]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 22
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 22
	t4_t5_mem1 += MM_MEM[0]

	t5_t0 = S.Task('t5_t0', length=1, delay_cost=1)
	S += t5_t0 >= 22
	t5_t0 += MAS[3]

	t5_t3 = S.Task('t5_t3', length=5, delay_cost=1)
	S += t5_t3 >= 22
	t5_t3 += MM[0]

	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	S += t16_t0_in >= 23
	t16_t0_in += MM_in[0]

	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	S += t16_t0_mem0 >= 23
	t16_t0_mem0 += MAIN_MEM_r

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	S += t16_t0_mem1 >= 23
	t16_t0_mem1 += MAS_MEM[1]

	t16_t1 = S.Task('t16_t1', length=5, delay_cost=1)
	S += t16_t1 >= 23
	t16_t1 += MM[0]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 23
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 23
	t41_mem1 += MM_MEM[0]

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	S += t4_t5 >= 23
	t4_t5 += MAS[2]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 24
	c010_w += MAIN_MEM_w

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 24
	c011_in += MM_in[0]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 24
	c011_mem0 += MAS_MEM[3]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 24
	c011_mem1 += MAIN_MEM_r

	t16_t0 = S.Task('t16_t0', length=5, delay_cost=1)
	S += t16_t0 >= 24
	t16_t0 += MM[0]

	t17_t5_mem0 = S.Task('t17_t5_mem0', length=1, delay_cost=1)
	S += t17_t5_mem0 >= 24
	t17_t5_mem0 += MM_MEM[0]

	t17_t5_mem1 = S.Task('t17_t5_mem1', length=1, delay_cost=1)
	S += t17_t5_mem1 >= 24
	t17_t5_mem1 += MM_MEM[0]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 24
	t41 += MAS[2]

	c011 = S.Task('c011', length=5, delay_cost=1)
	S += c011 >= 25
	c011 += MM[0]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 25
	t170_mem0 += MM_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 25
	t170_mem1 += MM_MEM[0]

	t17_t4_in = S.Task('t17_t4_in', length=1, delay_cost=1)
	S += t17_t4_in >= 25
	t17_t4_in += MM_in[0]

	t17_t4_mem0 = S.Task('t17_t4_mem0', length=1, delay_cost=1)
	S += t17_t4_mem0 >= 25
	t17_t4_mem0 += MAS_MEM[2]

	t17_t4_mem1 = S.Task('t17_t4_mem1', length=1, delay_cost=1)
	S += t17_t4_mem1 >= 25
	t17_t4_mem1 += MAS_MEM[1]

	t17_t5 = S.Task('t17_t5', length=1, delay_cost=1)
	S += t17_t5 >= 25
	t17_t5 += MAS[3]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 26
	c201_w += MAIN_MEM_w

	t16_t4_in = S.Task('t16_t4_in', length=1, delay_cost=1)
	S += t16_t4_in >= 26
	t16_t4_in += MM_in[0]

	t16_t4_mem0 = S.Task('t16_t4_mem0', length=1, delay_cost=1)
	S += t16_t4_mem0 >= 26
	t16_t4_mem0 += MAS_MEM[0]

	t16_t4_mem1 = S.Task('t16_t4_mem1', length=1, delay_cost=1)
	S += t16_t4_mem1 >= 26
	t16_t4_mem1 += MAS_MEM[3]

	t170 = S.Task('t170', length=1, delay_cost=1)
	S += t170 >= 26
	t170 += MAS[3]

	t17_t4 = S.Task('t17_t4', length=5, delay_cost=1)
	S += t17_t4 >= 26
	t17_t4 += MM[0]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 26
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 26
	t5_t5_mem1 += MM_MEM[0]

	t16_t4 = S.Task('t16_t4', length=5, delay_cost=1)
	S += t16_t4 >= 27
	t16_t4 += MM[0]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 27
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 27
	t51_mem1 += MM_MEM[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 27
	t5_t2_in += MM_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 27
	t5_t2_mem0 += MAS_MEM[3]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 27
	t5_t2_mem1 += MAS_MEM[2]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 27
	t5_t5 += MAS[3]

	t16_t5_mem0 = S.Task('t16_t5_mem0', length=1, delay_cost=1)
	S += t16_t5_mem0 >= 28
	t16_t5_mem0 += MM_MEM[0]

	t16_t5_mem1 = S.Task('t16_t5_mem1', length=1, delay_cost=1)
	S += t16_t5_mem1 >= 28
	t16_t5_mem1 += MM_MEM[0]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 28
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 28
	t4_t2_mem0 += MAS_MEM[2]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 28
	t4_t2_mem1 += MAS_MEM[0]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 28
	t51 += MAS[0]

	t5_t2 = S.Task('t5_t2', length=5, delay_cost=1)
	S += t5_t2 >= 28
	t5_t2 += MM[0]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 29
	t160_mem0 += MM_MEM[0]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 29
	t160_mem1 += MM_MEM[0]

	t16_t5 = S.Task('t16_t5', length=1, delay_cost=1)
	S += t16_t5 >= 29
	t16_t5 += MAS[3]

	t4_t2 = S.Task('t4_t2', length=5, delay_cost=1)
	S += t4_t2 >= 29
	t4_t2 += MM[0]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 30
	c011_w += MAIN_MEM_w

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 30
	t160 += MAS[1]


	# new tasks
	t40 = S.Task('t40', length=1, delay_cost=1)
	t40 += alt(MAS)

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	t40_mem0 += MM_MEM[0]
	S += 33 < t40_mem0
	S += t40_mem0 <= t40

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	t40_mem1 += MAS_MEM[2]
	S += 23 < t40_mem1
	S += t40_mem1 <= t40

	t50 = S.Task('t50', length=1, delay_cost=1)
	t50 += alt(MAS)

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	t50_mem0 += MM_MEM[0]
	S += 32 < t50_mem0
	S += t50_mem0 <= t50

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	t50_mem1 += MAS_MEM[3]
	S += 27 < t50_mem1
	S += t50_mem1 <= t50

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	t6_t1_in += alt(MM_in)
	t6_t1 = S.Task('t6_t1', length=5, delay_cost=1)
	t6_t1 += alt(MM)
	S += t6_t1>=t6_t1_in

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	t6_t1_mem0 += MAS_MEM[3]
	S += 19 < t6_t1_mem0
	S += t6_t1_mem0 <= t6_t1

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	t6_t1_mem1 += MAS_MEM[0]
	S += 28 < t6_t1_mem1
	S += t6_t1_mem1 <= t6_t1

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	t7_t1_in += alt(MM_in)
	t7_t1 = S.Task('t7_t1', length=5, delay_cost=1)
	t7_t1 += alt(MM)
	S += t7_t1>=t7_t1_in

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	t7_t1_mem0 += MAIN_MEM_r
	S += t7_t1_mem0 <= t7_t1

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	t7_t1_mem1 += MAS_MEM[2]
	S += 24 < t7_t1_mem1
	S += t7_t1_mem1 <= t7_t1

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	t9_t1_in += alt(MM_in)
	t9_t1 = S.Task('t9_t1', length=5, delay_cost=1)
	t9_t1 += alt(MM)
	S += t9_t1>=t9_t1_in

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	t9_t1_mem0 += MAIN_MEM_r
	S += t9_t1_mem0 <= t9_t1

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	t9_t1_mem1 += MAS_MEM[0]
	S += 28 < t9_t1_mem1
	S += t9_t1_mem1 <= t9_t1

	t161 = S.Task('t161', length=1, delay_cost=1)
	t161 += alt(MAS)

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += MM_MEM[0]
	S += 31 < t161_mem0
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += MAS_MEM[3]
	S += 29 < t161_mem1
	S += t161_mem1 <= t161

	t171 = S.Task('t171', length=1, delay_cost=1)
	t171 += alt(MAS)

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += MM_MEM[0]
	S += 30 < t171_mem0
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += MAS_MEM[3]
	S += 25 < t171_mem1
	S += t171_mem1 <= t171

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)

	S += 0<c000

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[1]
	S += 30 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += MAS_MEM[3]
	S += 26 < c000_mem1
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	t6_t0_in += alt(MM_in)
	t6_t0 = S.Task('t6_t0', length=5, delay_cost=1)
	t6_t0 += alt(MM)
	S += t6_t0>=t6_t0_in

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	t6_t0_mem0 += MAS_MEM[1]
	S += 15 < t6_t0_mem0
	S += t6_t0_mem0 <= t6_t0

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	t6_t0_mem1 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t6_t0_mem1*MAS_MEM[0]
	S += (t50*MAS[1])-1 < t6_t0_mem1*MAS_MEM[1]
	S += (t50*MAS[2])-1 < t6_t0_mem1*MAS_MEM[2]
	S += (t50*MAS[3])-1 < t6_t0_mem1*MAS_MEM[3]
	S += t6_t0_mem1 <= t6_t0

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	t6_t3 += alt(MAS)

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	t6_t3_mem0 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t6_t3_mem0*MAS_MEM[0]
	S += (t50*MAS[1])-1 < t6_t3_mem0*MAS_MEM[1]
	S += (t50*MAS[2])-1 < t6_t3_mem0*MAS_MEM[2]
	S += (t50*MAS[3])-1 < t6_t3_mem0*MAS_MEM[3]
	S += t6_t3_mem0 <= t6_t3

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	t6_t3_mem1 += MAS_MEM[0]
	S += 28 < t6_t3_mem1
	S += t6_t3_mem1 <= t6_t3

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	t7_t0_in += alt(MM_in)
	t7_t0 = S.Task('t7_t0', length=5, delay_cost=1)
	t7_t0 += alt(MM)
	S += t7_t0>=t7_t0_in

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	t7_t0_mem0 += MAIN_MEM_r
	S += t7_t0_mem0 <= t7_t0

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	t7_t0_mem1 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < t7_t0_mem1*MAS_MEM[0]
	S += (t40*MAS[1])-1 < t7_t0_mem1*MAS_MEM[1]
	S += (t40*MAS[2])-1 < t7_t0_mem1*MAS_MEM[2]
	S += (t40*MAS[3])-1 < t7_t0_mem1*MAS_MEM[3]
	S += t7_t0_mem1 <= t7_t0

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	t7_t3 += alt(MAS)

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	t7_t3_mem0 += alt(MAS_MEM)
	S += (t40*MAS[0])-1 < t7_t3_mem0*MAS_MEM[0]
	S += (t40*MAS[1])-1 < t7_t3_mem0*MAS_MEM[1]
	S += (t40*MAS[2])-1 < t7_t3_mem0*MAS_MEM[2]
	S += (t40*MAS[3])-1 < t7_t3_mem0*MAS_MEM[3]
	S += t7_t3_mem0 <= t7_t3

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	t7_t3_mem1 += MAS_MEM[2]
	S += 24 < t7_t3_mem1
	S += t7_t3_mem1 <= t7_t3

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	t9_t0_in += alt(MM_in)
	t9_t0 = S.Task('t9_t0', length=5, delay_cost=1)
	t9_t0 += alt(MM)
	S += t9_t0>=t9_t0_in

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	t9_t0_mem0 += MAIN_MEM_r
	S += t9_t0_mem0 <= t9_t0

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	t9_t0_mem1 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t9_t0_mem1*MAS_MEM[0]
	S += (t50*MAS[1])-1 < t9_t0_mem1*MAS_MEM[1]
	S += (t50*MAS[2])-1 < t9_t0_mem1*MAS_MEM[2]
	S += (t50*MAS[3])-1 < t9_t0_mem1*MAS_MEM[3]
	S += t9_t0_mem1 <= t9_t0

	t9_t3 = S.Task('t9_t3', length=1, delay_cost=1)
	t9_t3 += alt(MAS)

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	t9_t3_mem0 += alt(MAS_MEM)
	S += (t50*MAS[0])-1 < t9_t3_mem0*MAS_MEM[0]
	S += (t50*MAS[1])-1 < t9_t3_mem0*MAS_MEM[1]
	S += (t50*MAS[2])-1 < t9_t3_mem0*MAS_MEM[2]
	S += (t50*MAS[3])-1 < t9_t3_mem0*MAS_MEM[3]
	S += t9_t3_mem0 <= t9_t3

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	t9_t3_mem1 += MAS_MEM[0]
	S += 28 < t9_t3_mem1
	S += t9_t3_mem1 <= t9_t3

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)

	S += 0<c001

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < c001_mem0*MAS_MEM[0]
	S += (t161*MAS[1])-1 < c001_mem0*MAS_MEM[1]
	S += (t161*MAS[2])-1 < c001_mem0*MAS_MEM[2]
	S += (t161*MAS[3])-1 < c001_mem0*MAS_MEM[3]
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (t171*MAS[0])-1 < c001_mem1*MAS_MEM[0]
	S += (t171*MAS[1])-1 < c001_mem1*MAS_MEM[1]
	S += (t171*MAS[2])-1 < c001_mem1*MAS_MEM[2]
	S += (t171*MAS[3])-1 < c001_mem1*MAS_MEM[3]
	S += c001_mem1 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	t6_t4_in += alt(MM_in)
	t6_t4 = S.Task('t6_t4', length=5, delay_cost=1)
	t6_t4 += alt(MM)
	S += t6_t4>=t6_t4_in

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	t6_t4_mem0 += MAS_MEM[0]
	S += 20 < t6_t4_mem0
	S += t6_t4_mem0 <= t6_t4

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	t6_t4_mem1 += alt(MAS_MEM)
	S += (t6_t3*MAS[0])-1 < t6_t4_mem1*MAS_MEM[0]
	S += (t6_t3*MAS[1])-1 < t6_t4_mem1*MAS_MEM[1]
	S += (t6_t3*MAS[2])-1 < t6_t4_mem1*MAS_MEM[2]
	S += (t6_t3*MAS[3])-1 < t6_t4_mem1*MAS_MEM[3]
	S += t6_t4_mem1 <= t6_t4

	t60 = S.Task('t60', length=1, delay_cost=1)
	t60 += alt(MAS)

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	t60_mem0 += alt(MM_MEM)
	S += (t6_t0*MM[0])-1 < t60_mem0*MM_MEM[0]
	S += t60_mem0 <= t60

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	t60_mem1 += alt(MM_MEM)
	S += (t6_t1*MM[0])-1 < t60_mem1*MM_MEM[0]
	S += t60_mem1 <= t60

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	t6_t5 += alt(MAS)

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	t6_t5_mem0 += alt(MM_MEM)
	S += (t6_t0*MM[0])-1 < t6_t5_mem0*MM_MEM[0]
	S += t6_t5_mem0 <= t6_t5

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	t6_t5_mem1 += alt(MM_MEM)
	S += (t6_t1*MM[0])-1 < t6_t5_mem1*MM_MEM[0]
	S += t6_t5_mem1 <= t6_t5

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	t7_t4_in += alt(MM_in)
	t7_t4 = S.Task('t7_t4', length=5, delay_cost=1)
	t7_t4 += alt(MM)
	S += t7_t4>=t7_t4_in

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	t7_t4_mem0 += MAS_MEM[0]
	S += 6 < t7_t4_mem0
	S += t7_t4_mem0 <= t7_t4

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	t7_t4_mem1 += alt(MAS_MEM)
	S += (t7_t3*MAS[0])-1 < t7_t4_mem1*MAS_MEM[0]
	S += (t7_t3*MAS[1])-1 < t7_t4_mem1*MAS_MEM[1]
	S += (t7_t3*MAS[2])-1 < t7_t4_mem1*MAS_MEM[2]
	S += (t7_t3*MAS[3])-1 < t7_t4_mem1*MAS_MEM[3]
	S += t7_t4_mem1 <= t7_t4

	t70 = S.Task('t70', length=1, delay_cost=1)
	t70 += alt(MAS)

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	t70_mem0 += alt(MM_MEM)
	S += (t7_t0*MM[0])-1 < t70_mem0*MM_MEM[0]
	S += t70_mem0 <= t70

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	t70_mem1 += alt(MM_MEM)
	S += (t7_t1*MM[0])-1 < t70_mem1*MM_MEM[0]
	S += t70_mem1 <= t70

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	t7_t5 += alt(MAS)

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	t7_t5_mem0 += alt(MM_MEM)
	S += (t7_t0*MM[0])-1 < t7_t5_mem0*MM_MEM[0]
	S += t7_t5_mem0 <= t7_t5

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	t7_t5_mem1 += alt(MM_MEM)
	S += (t7_t1*MM[0])-1 < t7_t5_mem1*MM_MEM[0]
	S += t7_t5_mem1 <= t7_t5

	t9_t4_in = S.Task('t9_t4_in', length=1, delay_cost=1)
	t9_t4_in += alt(MM_in)
	t9_t4 = S.Task('t9_t4', length=5, delay_cost=1)
	t9_t4 += alt(MM)
	S += t9_t4>=t9_t4_in

	t9_t4_mem0 = S.Task('t9_t4_mem0', length=1, delay_cost=1)
	t9_t4_mem0 += MAS_MEM[0]
	S += 5 < t9_t4_mem0
	S += t9_t4_mem0 <= t9_t4

	t9_t4_mem1 = S.Task('t9_t4_mem1', length=1, delay_cost=1)
	t9_t4_mem1 += alt(MAS_MEM)
	S += (t9_t3*MAS[0])-1 < t9_t4_mem1*MAS_MEM[0]
	S += (t9_t3*MAS[1])-1 < t9_t4_mem1*MAS_MEM[1]
	S += (t9_t3*MAS[2])-1 < t9_t4_mem1*MAS_MEM[2]
	S += (t9_t3*MAS[3])-1 < t9_t4_mem1*MAS_MEM[3]
	S += t9_t4_mem1 <= t9_t4

	t90 = S.Task('t90', length=1, delay_cost=1)
	t90 += alt(MAS)

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += alt(MM_MEM)
	S += (t9_t0*MM[0])-1 < t90_mem0*MM_MEM[0]
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += alt(MM_MEM)
	S += (t9_t1*MM[0])-1 < t90_mem1*MM_MEM[0]
	S += t90_mem1 <= t90

	t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
	t9_t5 += alt(MAS)

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	t9_t5_mem0 += alt(MM_MEM)
	S += (t9_t0*MM[0])-1 < t9_t5_mem0*MM_MEM[0]
	S += t9_t5_mem0 <= t9_t5

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	t9_t5_mem1 += alt(MM_MEM)
	S += (t9_t1*MM[0])-1 < t9_t5_mem1*MM_MEM[0]
	S += t9_t5_mem1 <= t9_t5

	t61 = S.Task('t61', length=1, delay_cost=1)
	t61 += alt(MAS)

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	t61_mem0 += alt(MM_MEM)
	S += (t6_t4*MM[0])-1 < t61_mem0*MM_MEM[0]
	S += t61_mem0 <= t61

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	t61_mem1 += alt(MAS_MEM)
	S += (t6_t5*MAS[0])-1 < t61_mem1*MAS_MEM[0]
	S += (t6_t5*MAS[1])-1 < t61_mem1*MAS_MEM[1]
	S += (t6_t5*MAS[2])-1 < t61_mem1*MAS_MEM[2]
	S += (t6_t5*MAS[3])-1 < t61_mem1*MAS_MEM[3]
	S += t61_mem1 <= t61

	t71 = S.Task('t71', length=1, delay_cost=1)
	t71 += alt(MAS)

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	t71_mem0 += alt(MM_MEM)
	S += (t7_t4*MM[0])-1 < t71_mem0*MM_MEM[0]
	S += t71_mem0 <= t71

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	t71_mem1 += alt(MAS_MEM)
	S += (t7_t5*MAS[0])-1 < t71_mem1*MAS_MEM[0]
	S += (t7_t5*MAS[1])-1 < t71_mem1*MAS_MEM[1]
	S += (t7_t5*MAS[2])-1 < t71_mem1*MAS_MEM[2]
	S += (t7_t5*MAS[3])-1 < t71_mem1*MAS_MEM[3]
	S += t71_mem1 <= t71

	t80 = S.Task('t80', length=1, delay_cost=1)
	t80 += alt(MAS)

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	t80_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t80_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < t80_mem0*MAS_MEM[1]
	S += (t60*MAS[2])-1 < t80_mem0*MAS_MEM[2]
	S += (t60*MAS[3])-1 < t80_mem0*MAS_MEM[3]
	S += t80_mem0 <= t80

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	t80_mem1 += alt(MAS_MEM)
	S += (t70*MAS[0])-1 < t80_mem1*MAS_MEM[0]
	S += (t70*MAS[1])-1 < t80_mem1*MAS_MEM[1]
	S += (t70*MAS[2])-1 < t80_mem1*MAS_MEM[2]
	S += (t70*MAS[3])-1 < t80_mem1*MAS_MEM[3]
	S += t80_mem1 <= t80

	t91 = S.Task('t91', length=1, delay_cost=1)
	t91 += alt(MAS)

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	t91_mem0 += alt(MM_MEM)
	S += (t9_t4*MM[0])-1 < t91_mem0*MM_MEM[0]
	S += t91_mem0 <= t91

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	t91_mem1 += alt(MAS_MEM)
	S += (t9_t5*MAS[0])-1 < t91_mem1*MAS_MEM[0]
	S += (t9_t5*MAS[1])-1 < t91_mem1*MAS_MEM[1]
	S += (t9_t5*MAS[2])-1 < t91_mem1*MAS_MEM[2]
	S += (t9_t5*MAS[3])-1 < t91_mem1*MAS_MEM[3]
	S += t91_mem1 <= t91

	t100 = S.Task('t100', length=1, delay_cost=1)
	t100 += alt(MAS)

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t100_mem0*MAS_MEM[0]
	S += (t90*MAS[1])-1 < t100_mem0*MAS_MEM[1]
	S += (t90*MAS[2])-1 < t100_mem0*MAS_MEM[2]
	S += (t90*MAS[3])-1 < t100_mem0*MAS_MEM[3]
	S += t100_mem0 <= t100

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	t100_mem1 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t100_mem1*MAS_MEM[0]
	S += (t90*MAS[1])-1 < t100_mem1*MAS_MEM[1]
	S += (t90*MAS[2])-1 < t100_mem1*MAS_MEM[2]
	S += (t90*MAS[3])-1 < t100_mem1*MAS_MEM[3]
	S += t100_mem1 <= t100

	t14_t0_in = S.Task('t14_t0_in', length=1, delay_cost=1)
	t14_t0_in += alt(MM_in)
	t14_t0 = S.Task('t14_t0', length=5, delay_cost=1)
	t14_t0 += alt(MM)
	S += t14_t0>=t14_t0_in

	t14_t0_mem0 = S.Task('t14_t0_mem0', length=1, delay_cost=1)
	t14_t0_mem0 += MAIN_MEM_r
	S += t14_t0_mem0 <= t14_t0

	t14_t0_mem1 = S.Task('t14_t0_mem1', length=1, delay_cost=1)
	t14_t0_mem1 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t14_t0_mem1*MAS_MEM[0]
	S += (t60*MAS[1])-1 < t14_t0_mem1*MAS_MEM[1]
	S += (t60*MAS[2])-1 < t14_t0_mem1*MAS_MEM[2]
	S += (t60*MAS[3])-1 < t14_t0_mem1*MAS_MEM[3]
	S += t14_t0_mem1 <= t14_t0

	new_TZ_t0_in = S.Task('new_TZ_t0_in', length=1, delay_cost=1)
	new_TZ_t0_in += alt(MM_in)
	new_TZ_t0 = S.Task('new_TZ_t0', length=5, delay_cost=1)
	new_TZ_t0 += alt(MM)
	S += new_TZ_t0>=new_TZ_t0_in

	new_TZ_t0_mem0 = S.Task('new_TZ_t0_mem0', length=1, delay_cost=1)
	new_TZ_t0_mem0 += MAIN_MEM_r
	S += new_TZ_t0_mem0 <= new_TZ_t0

	new_TZ_t0_mem1 = S.Task('new_TZ_t0_mem1', length=1, delay_cost=1)
	new_TZ_t0_mem1 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < new_TZ_t0_mem1*MAS_MEM[0]
	S += (t60*MAS[1])-1 < new_TZ_t0_mem1*MAS_MEM[1]
	S += (t60*MAS[2])-1 < new_TZ_t0_mem1*MAS_MEM[2]
	S += (t60*MAS[3])-1 < new_TZ_t0_mem1*MAS_MEM[3]
	S += new_TZ_t0_mem1 <= new_TZ_t0

	t81 = S.Task('t81', length=1, delay_cost=1)
	t81 += alt(MAS)

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	t81_mem0 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < t81_mem0*MAS_MEM[0]
	S += (t61*MAS[1])-1 < t81_mem0*MAS_MEM[1]
	S += (t61*MAS[2])-1 < t81_mem0*MAS_MEM[2]
	S += (t61*MAS[3])-1 < t81_mem0*MAS_MEM[3]
	S += t81_mem0 <= t81

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	t81_mem1 += alt(MAS_MEM)
	S += (t71*MAS[0])-1 < t81_mem1*MAS_MEM[0]
	S += (t71*MAS[1])-1 < t81_mem1*MAS_MEM[1]
	S += (t71*MAS[2])-1 < t81_mem1*MAS_MEM[2]
	S += (t71*MAS[3])-1 < t81_mem1*MAS_MEM[3]
	S += t81_mem1 <= t81

	t101 = S.Task('t101', length=1, delay_cost=1)
	t101 += alt(MAS)

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < t101_mem0*MAS_MEM[0]
	S += (t91*MAS[1])-1 < t101_mem0*MAS_MEM[1]
	S += (t91*MAS[2])-1 < t101_mem0*MAS_MEM[2]
	S += (t91*MAS[3])-1 < t101_mem0*MAS_MEM[3]
	S += t101_mem0 <= t101

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	t101_mem1 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < t101_mem1*MAS_MEM[0]
	S += (t91*MAS[1])-1 < t101_mem1*MAS_MEM[1]
	S += (t91*MAS[2])-1 < t101_mem1*MAS_MEM[2]
	S += (t91*MAS[3])-1 < t101_mem1*MAS_MEM[3]
	S += t101_mem1 <= t101

	t110 = S.Task('t110', length=1, delay_cost=1)
	t110 += alt(MAS)

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	t110_mem0 += alt(MAS_MEM)
	S += (t80*MAS[0])-1 < t110_mem0*MAS_MEM[0]
	S += (t80*MAS[1])-1 < t110_mem0*MAS_MEM[1]
	S += (t80*MAS[2])-1 < t110_mem0*MAS_MEM[2]
	S += (t80*MAS[3])-1 < t110_mem0*MAS_MEM[3]
	S += t110_mem0 <= t110

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	t110_mem1 += alt(MAS_MEM)
	S += (t100*MAS[0])-1 < t110_mem1*MAS_MEM[0]
	S += (t100*MAS[1])-1 < t110_mem1*MAS_MEM[1]
	S += (t100*MAS[2])-1 < t110_mem1*MAS_MEM[2]
	S += (t100*MAS[3])-1 < t110_mem1*MAS_MEM[3]
	S += t110_mem1 <= t110

	t14_t1_in = S.Task('t14_t1_in', length=1, delay_cost=1)
	t14_t1_in += alt(MM_in)
	t14_t1 = S.Task('t14_t1', length=5, delay_cost=1)
	t14_t1 += alt(MM)
	S += t14_t1>=t14_t1_in

	t14_t1_mem0 = S.Task('t14_t1_mem0', length=1, delay_cost=1)
	t14_t1_mem0 += MAIN_MEM_r
	S += t14_t1_mem0 <= t14_t1

	t14_t1_mem1 = S.Task('t14_t1_mem1', length=1, delay_cost=1)
	t14_t1_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < t14_t1_mem1*MAS_MEM[0]
	S += (t61*MAS[1])-1 < t14_t1_mem1*MAS_MEM[1]
	S += (t61*MAS[2])-1 < t14_t1_mem1*MAS_MEM[2]
	S += (t61*MAS[3])-1 < t14_t1_mem1*MAS_MEM[3]
	S += t14_t1_mem1 <= t14_t1

	t14_t3 = S.Task('t14_t3', length=1, delay_cost=1)
	t14_t3 += alt(MAS)

	t14_t3_mem0 = S.Task('t14_t3_mem0', length=1, delay_cost=1)
	t14_t3_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < t14_t3_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < t14_t3_mem0*MAS_MEM[1]
	S += (t60*MAS[2])-1 < t14_t3_mem0*MAS_MEM[2]
	S += (t60*MAS[3])-1 < t14_t3_mem0*MAS_MEM[3]
	S += t14_t3_mem0 <= t14_t3

	t14_t3_mem1 = S.Task('t14_t3_mem1', length=1, delay_cost=1)
	t14_t3_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < t14_t3_mem1*MAS_MEM[0]
	S += (t61*MAS[1])-1 < t14_t3_mem1*MAS_MEM[1]
	S += (t61*MAS[2])-1 < t14_t3_mem1*MAS_MEM[2]
	S += (t61*MAS[3])-1 < t14_t3_mem1*MAS_MEM[3]
	S += t14_t3_mem1 <= t14_t3

	new_TZ_t1_in = S.Task('new_TZ_t1_in', length=1, delay_cost=1)
	new_TZ_t1_in += alt(MM_in)
	new_TZ_t1 = S.Task('new_TZ_t1', length=5, delay_cost=1)
	new_TZ_t1 += alt(MM)
	S += new_TZ_t1>=new_TZ_t1_in

	new_TZ_t1_mem0 = S.Task('new_TZ_t1_mem0', length=1, delay_cost=1)
	new_TZ_t1_mem0 += MAIN_MEM_r
	S += new_TZ_t1_mem0 <= new_TZ_t1

	new_TZ_t1_mem1 = S.Task('new_TZ_t1_mem1', length=1, delay_cost=1)
	new_TZ_t1_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < new_TZ_t1_mem1*MAS_MEM[0]
	S += (t61*MAS[1])-1 < new_TZ_t1_mem1*MAS_MEM[1]
	S += (t61*MAS[2])-1 < new_TZ_t1_mem1*MAS_MEM[2]
	S += (t61*MAS[3])-1 < new_TZ_t1_mem1*MAS_MEM[3]
	S += new_TZ_t1_mem1 <= new_TZ_t1

	new_TZ_t3 = S.Task('new_TZ_t3', length=1, delay_cost=1)
	new_TZ_t3 += alt(MAS)

	new_TZ_t3_mem0 = S.Task('new_TZ_t3_mem0', length=1, delay_cost=1)
	new_TZ_t3_mem0 += alt(MAS_MEM)
	S += (t60*MAS[0])-1 < new_TZ_t3_mem0*MAS_MEM[0]
	S += (t60*MAS[1])-1 < new_TZ_t3_mem0*MAS_MEM[1]
	S += (t60*MAS[2])-1 < new_TZ_t3_mem0*MAS_MEM[2]
	S += (t60*MAS[3])-1 < new_TZ_t3_mem0*MAS_MEM[3]
	S += new_TZ_t3_mem0 <= new_TZ_t3

	new_TZ_t3_mem1 = S.Task('new_TZ_t3_mem1', length=1, delay_cost=1)
	new_TZ_t3_mem1 += alt(MAS_MEM)
	S += (t61*MAS[0])-1 < new_TZ_t3_mem1*MAS_MEM[0]
	S += (t61*MAS[1])-1 < new_TZ_t3_mem1*MAS_MEM[1]
	S += (t61*MAS[2])-1 < new_TZ_t3_mem1*MAS_MEM[2]
	S += (t61*MAS[3])-1 < new_TZ_t3_mem1*MAS_MEM[3]
	S += new_TZ_t3_mem1 <= new_TZ_t3

	t111 = S.Task('t111', length=1, delay_cost=1)
	t111 += alt(MAS)

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += alt(MAS_MEM)
	S += (t81*MAS[0])-1 < t111_mem0*MAS_MEM[0]
	S += (t81*MAS[1])-1 < t111_mem0*MAS_MEM[1]
	S += (t81*MAS[2])-1 < t111_mem0*MAS_MEM[2]
	S += (t81*MAS[3])-1 < t111_mem0*MAS_MEM[3]
	S += t111_mem0 <= t111

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	t111_mem1 += alt(MAS_MEM)
	S += (t101*MAS[0])-1 < t111_mem1*MAS_MEM[0]
	S += (t101*MAS[1])-1 < t111_mem1*MAS_MEM[1]
	S += (t101*MAS[2])-1 < t111_mem1*MAS_MEM[2]
	S += (t101*MAS[3])-1 < t111_mem1*MAS_MEM[3]
	S += t111_mem1 <= t111

	t120 = S.Task('t120', length=1, delay_cost=1)
	t120 += alt(MAS)

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < t120_mem0*MAS_MEM[0]
	S += (t110*MAS[1])-1 < t120_mem0*MAS_MEM[1]
	S += (t110*MAS[2])-1 < t120_mem0*MAS_MEM[2]
	S += (t110*MAS[3])-1 < t120_mem0*MAS_MEM[3]
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t120_mem1*MAS_MEM[0]
	S += (t90*MAS[1])-1 < t120_mem1*MAS_MEM[1]
	S += (t90*MAS[2])-1 < t120_mem1*MAS_MEM[2]
	S += (t90*MAS[3])-1 < t120_mem1*MAS_MEM[3]
	S += t120_mem1 <= t120

	new_TX_t0_in = S.Task('new_TX_t0_in', length=1, delay_cost=1)
	new_TX_t0_in += alt(MM_in)
	new_TX_t0 = S.Task('new_TX_t0', length=5, delay_cost=1)
	new_TX_t0 += alt(MM)
	S += new_TX_t0>=new_TX_t0_in

	new_TX_t0_mem0 = S.Task('new_TX_t0_mem0', length=1, delay_cost=1)
	new_TX_t0_mem0 += MAS_MEM[1]
	S += 15 < new_TX_t0_mem0
	S += new_TX_t0_mem0 <= new_TX_t0

	new_TX_t0_mem1 = S.Task('new_TX_t0_mem1', length=1, delay_cost=1)
	new_TX_t0_mem1 += alt(MAS_MEM)
	S += (t110*MAS[0])-1 < new_TX_t0_mem1*MAS_MEM[0]
	S += (t110*MAS[1])-1 < new_TX_t0_mem1*MAS_MEM[1]
	S += (t110*MAS[2])-1 < new_TX_t0_mem1*MAS_MEM[2]
	S += (t110*MAS[3])-1 < new_TX_t0_mem1*MAS_MEM[3]
	S += new_TX_t0_mem1 <= new_TX_t0

	t14_t4_in = S.Task('t14_t4_in', length=1, delay_cost=1)
	t14_t4_in += alt(MM_in)
	t14_t4 = S.Task('t14_t4', length=5, delay_cost=1)
	t14_t4 += alt(MM)
	S += t14_t4>=t14_t4_in

	t14_t4_mem0 = S.Task('t14_t4_mem0', length=1, delay_cost=1)
	t14_t4_mem0 += MAS_MEM[0]
	S += 11 < t14_t4_mem0
	S += t14_t4_mem0 <= t14_t4

	t14_t4_mem1 = S.Task('t14_t4_mem1', length=1, delay_cost=1)
	t14_t4_mem1 += alt(MAS_MEM)
	S += (t14_t3*MAS[0])-1 < t14_t4_mem1*MAS_MEM[0]
	S += (t14_t3*MAS[1])-1 < t14_t4_mem1*MAS_MEM[1]
	S += (t14_t3*MAS[2])-1 < t14_t4_mem1*MAS_MEM[2]
	S += (t14_t3*MAS[3])-1 < t14_t4_mem1*MAS_MEM[3]
	S += t14_t4_mem1 <= t14_t4

	t140 = S.Task('t140', length=1, delay_cost=1)
	t140 += alt(MAS)

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += alt(MM_MEM)
	S += (t14_t0*MM[0])-1 < t140_mem0*MM_MEM[0]
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += alt(MM_MEM)
	S += (t14_t1*MM[0])-1 < t140_mem1*MM_MEM[0]
	S += t140_mem1 <= t140

	t14_t5 = S.Task('t14_t5', length=1, delay_cost=1)
	t14_t5 += alt(MAS)

	t14_t5_mem0 = S.Task('t14_t5_mem0', length=1, delay_cost=1)
	t14_t5_mem0 += alt(MM_MEM)
	S += (t14_t0*MM[0])-1 < t14_t5_mem0*MM_MEM[0]
	S += t14_t5_mem0 <= t14_t5

	t14_t5_mem1 = S.Task('t14_t5_mem1', length=1, delay_cost=1)
	t14_t5_mem1 += alt(MM_MEM)
	S += (t14_t1*MM[0])-1 < t14_t5_mem1*MM_MEM[0]
	S += t14_t5_mem1 <= t14_t5

	new_TZ_t4_in = S.Task('new_TZ_t4_in', length=1, delay_cost=1)
	new_TZ_t4_in += alt(MM_in)
	new_TZ_t4 = S.Task('new_TZ_t4', length=5, delay_cost=1)
	new_TZ_t4 += alt(MM)
	S += new_TZ_t4>=new_TZ_t4_in

	new_TZ_t4_mem0 = S.Task('new_TZ_t4_mem0', length=1, delay_cost=1)
	new_TZ_t4_mem0 += MAS_MEM[1]
	S += 8 < new_TZ_t4_mem0
	S += new_TZ_t4_mem0 <= new_TZ_t4

	new_TZ_t4_mem1 = S.Task('new_TZ_t4_mem1', length=1, delay_cost=1)
	new_TZ_t4_mem1 += alt(MAS_MEM)
	S += (new_TZ_t3*MAS[0])-1 < new_TZ_t4_mem1*MAS_MEM[0]
	S += (new_TZ_t3*MAS[1])-1 < new_TZ_t4_mem1*MAS_MEM[1]
	S += (new_TZ_t3*MAS[2])-1 < new_TZ_t4_mem1*MAS_MEM[2]
	S += (new_TZ_t3*MAS[3])-1 < new_TZ_t4_mem1*MAS_MEM[3]
	S += new_TZ_t4_mem1 <= new_TZ_t4

	new_TZ0 = S.Task('new_TZ0', length=1, delay_cost=1)
	new_TZ0 += alt(MAS)

	S += 9<new_TZ0

	new_TZ0_mem0 = S.Task('new_TZ0_mem0', length=1, delay_cost=1)
	new_TZ0_mem0 += alt(MM_MEM)
	S += (new_TZ_t0*MM[0])-1 < new_TZ0_mem0*MM_MEM[0]
	S += new_TZ0_mem0 <= new_TZ0

	new_TZ0_mem1 = S.Task('new_TZ0_mem1', length=1, delay_cost=1)
	new_TZ0_mem1 += alt(MM_MEM)
	S += (new_TZ_t1*MM[0])-1 < new_TZ0_mem1*MM_MEM[0]
	S += new_TZ0_mem1 <= new_TZ0

	new_TZ0_w = S.Task('new_TZ0_w', length=1, delay_cost=1)
	new_TZ0_w += alt(MAIN_MEM_w)
	S += new_TZ0 <= new_TZ0_w

	new_TZ_t5 = S.Task('new_TZ_t5', length=1, delay_cost=1)
	new_TZ_t5 += alt(MAS)

	new_TZ_t5_mem0 = S.Task('new_TZ_t5_mem0', length=1, delay_cost=1)
	new_TZ_t5_mem0 += alt(MM_MEM)
	S += (new_TZ_t0*MM[0])-1 < new_TZ_t5_mem0*MM_MEM[0]
	S += new_TZ_t5_mem0 <= new_TZ_t5

	new_TZ_t5_mem1 = S.Task('new_TZ_t5_mem1', length=1, delay_cost=1)
	new_TZ_t5_mem1 += alt(MM_MEM)
	S += (new_TZ_t1*MM[0])-1 < new_TZ_t5_mem1*MM_MEM[0]
	S += new_TZ_t5_mem1 <= new_TZ_t5

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/PADD/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

