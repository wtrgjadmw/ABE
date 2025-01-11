from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 149
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=1, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	S += t2_in >= 0
	t2_in += MM_in[0]

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	S += t2_mem0 >= 0
	t2_mem0 += MAIN_MEM_r[0]

	t2_mem1 = S.Task('t2_mem1', length=1, delay_cost=1)
	S += t2_mem1 >= 0
	t2_mem1 += MAIN_MEM_r[1]

	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	S += t0_in >= 1
	t0_in += MM_in[0]

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	S += t0_mem0 >= 1
	t0_mem0 += MAIN_MEM_r[0]

	t0_mem1 = S.Task('t0_mem1', length=1, delay_cost=1)
	S += t0_mem1 >= 1
	t0_mem1 += MAIN_MEM_r[1]

	t2 = S.Task('t2', length=8, delay_cost=1)
	S += t2 >= 1
	t2 += MM[0]

	t0 = S.Task('t0', length=8, delay_cost=1)
	S += t0 >= 2
	t0 += MM[0]

	t9_in = S.Task('t9_in', length=1, delay_cost=1)
	S += t9_in >= 2
	t9_in += MAS_in[0]

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	S += t9_mem0 >= 2
	t9_mem0 += MAIN_MEM_r[0]

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	S += t9_mem1 >= 2
	t9_mem1 += MAIN_MEM_r[1]

	t8_in = S.Task('t8_in', length=1, delay_cost=1)
	S += t8_in >= 3
	t8_in += MAS_in[0]

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	S += t8_mem0 >= 3
	t8_mem0 += MAIN_MEM_r[0]

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	S += t8_mem1 >= 3
	t8_mem1 += MAIN_MEM_r[1]

	t9 = S.Task('t9', length=2, delay_cost=1)
	S += t9 >= 3
	t9 += MAS[0]

	t4_in = S.Task('t4_in', length=1, delay_cost=1)
	S += t4_in >= 4
	t4_in += MAS_in[0]

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	S += t4_mem0 >= 4
	t4_mem0 += MAIN_MEM_r[0]

	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	S += t4_mem1 >= 4
	t4_mem1 += MAIN_MEM_r[1]

	t8 = S.Task('t8', length=2, delay_cost=1)
	S += t8 >= 4
	t8 += MAS[0]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 5
	t10_in += MM_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 5
	t10_mem0 += MAS_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 5
	t10_mem1 += MAS_MEM[1]

	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	S += t3_in >= 5
	t3_in += MAS_in[0]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 5
	t3_mem0 += MAIN_MEM_r[0]

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 5
	t3_mem1 += MAIN_MEM_r[1]

	t4 = S.Task('t4', length=2, delay_cost=1)
	S += t4 >= 5
	t4 += MAS[0]

	t10 = S.Task('t10', length=8, delay_cost=1)
	S += t10 >= 6
	t10 += MM[0]

	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	S += t1_in >= 6
	t1_in += MM_in[0]

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	S += t1_mem0 >= 6
	t1_mem0 += MAIN_MEM_r[0]

	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	S += t1_mem1 >= 6
	t1_mem1 += MAIN_MEM_r[1]

	t3 = S.Task('t3', length=2, delay_cost=1)
	S += t3 >= 6
	t3 += MAS[0]

	t1 = S.Task('t1', length=8, delay_cost=1)
	S += t1 >= 7
	t1 += MM[0]

	t13_in = S.Task('t13_in', length=1, delay_cost=1)
	S += t13_in >= 7
	t13_in += MAS_in[0]

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	S += t13_mem0 >= 7
	t13_mem0 += MAIN_MEM_r[0]

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	S += t13_mem1 >= 7
	t13_mem1 += MAIN_MEM_r[1]

	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	S += t5_in >= 7
	t5_in += MM_in[0]

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	S += t5_mem0 >= 7
	t5_mem0 += MAS_MEM[0]

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	S += t5_mem1 >= 7
	t5_mem1 += MAS_MEM[1]

	t13 = S.Task('t13', length=2, delay_cost=1)
	S += t13 >= 8
	t13 += MAS[0]

	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	S += t26_in >= 8
	t26_in += MM_in[0]

	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	S += t26_mem0 >= 8
	t26_mem0 += MAIN_MEM_r[0]

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	S += t26_mem1 >= 8
	t26_mem1 += MM_MEM[1]

	t5 = S.Task('t5', length=8, delay_cost=1)
	S += t5 >= 8
	t5 += MM[0]

	t14_in = S.Task('t14_in', length=1, delay_cost=1)
	S += t14_in >= 9
	t14_in += MAS_in[0]

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	S += t14_mem0 >= 9
	t14_mem0 += MAIN_MEM_r[0]

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	S += t14_mem1 >= 9
	t14_mem1 += MAIN_MEM_r[1]

	t26 = S.Task('t26', length=8, delay_cost=1)
	S += t26 >= 9
	t26 += MM[0]

	t14 = S.Task('t14', length=2, delay_cost=1)
	S += t14 >= 10
	t14 += MAS[0]

	t24_in = S.Task('t24_in', length=1, delay_cost=1)
	S += t24_in >= 10
	t24_in += MAS_in[0]

	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	S += t24_mem0 >= 10
	t24_mem0 += MM_MEM[0]

	t24_mem1 = S.Task('t24_mem1', length=1, delay_cost=1)
	S += t24_mem1 >= 10
	t24_mem1 += MM_MEM[1]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 11
	t11_in += MAS_in[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 11
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 11
	t11_mem1 += MM_MEM[1]

	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	S += t15_in >= 11
	t15_in += MM_in[0]

	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	S += t15_mem0 >= 11
	t15_mem0 += MAS_MEM[0]

	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	S += t15_mem1 >= 11
	t15_mem1 += MAS_MEM[1]

	t24 = S.Task('t24', length=2, delay_cost=1)
	S += t24 >= 11
	t24 += MAS[0]

	t11 = S.Task('t11', length=2, delay_cost=1)
	S += t11 >= 12
	t11 += MAS[0]

	t15 = S.Task('t15', length=8, delay_cost=1)
	S += t15 >= 12
	t15 += MM[0]

	t19_in = S.Task('t19_in', length=1, delay_cost=1)
	S += t19_in >= 12
	t19_in += MM_in[0]

	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	S += t19_mem0 >= 12
	t19_mem0 += MAIN_MEM_r[0]

	t19_mem1 = S.Task('t19_mem1', length=1, delay_cost=1)
	S += t19_mem1 >= 12
	t19_mem1 += MM_MEM[1]

	t25_in = S.Task('t25_in', length=1, delay_cost=1)
	S += t25_in >= 12
	t25_in += MAS_in[0]

	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	S += t25_mem0 >= 12
	t25_mem0 += MM_MEM[0]

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	S += t25_mem1 >= 12
	t25_mem1 += MAS_MEM[1]

	t12_in = S.Task('t12_in', length=1, delay_cost=1)
	S += t12_in >= 13
	t12_in += MAS_in[0]

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	S += t12_mem0 >= 13
	t12_mem0 += MM_MEM[0]

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	S += t12_mem1 >= 13
	t12_mem1 += MAS_MEM[1]

	t19 = S.Task('t19', length=8, delay_cost=1)
	S += t19 >= 13
	t19 += MM[0]

	t25 = S.Task('t25', length=2, delay_cost=1)
	S += t25 >= 13
	t25 += MAS[0]

	t12 = S.Task('t12', length=2, delay_cost=1)
	S += t12 >= 14
	t12 += MAS[0]

	t16_in = S.Task('t16_in', length=1, delay_cost=1)
	S += t16_in >= 14
	t16_in += MAS_in[0]

	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	S += t16_mem0 >= 14
	t16_mem0 += MM_MEM[0]

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	S += t16_mem1 >= 14
	t16_mem1 += MM_MEM[1]

	t16 = S.Task('t16', length=2, delay_cost=1)
	S += t16 >= 15
	t16 += MAS[0]

	t18_in = S.Task('t18_in', length=1, delay_cost=1)
	S += t18_in >= 15
	t18_in += MM_in[0]

	t18_mem0 = S.Task('t18_mem0', length=1, delay_cost=1)
	S += t18_mem0 >= 15
	t18_mem0 += MAIN_MEM_r[0]

	t18_mem1 = S.Task('t18_mem1', length=1, delay_cost=1)
	S += t18_mem1 >= 15
	t18_mem1 += MAS_MEM[1]

	t6_in = S.Task('t6_in', length=1, delay_cost=1)
	S += t6_in >= 15
	t6_in += MAS_in[0]

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	S += t6_mem0 >= 15
	t6_mem0 += MM_MEM[0]

	t6_mem1 = S.Task('t6_mem1', length=1, delay_cost=1)
	S += t6_mem1 >= 15
	t6_mem1 += MM_MEM[1]

	t18 = S.Task('t18', length=8, delay_cost=1)
	S += t18 >= 16
	t18 += MM[0]

	t27_in = S.Task('t27_in', length=1, delay_cost=1)
	S += t27_in >= 16
	t27_in += MM_in[0]

	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	S += t27_mem0 >= 16
	t27_mem0 += MAIN_MEM_r[0]

	t27_mem1 = S.Task('t27_mem1', length=1, delay_cost=1)
	S += t27_mem1 >= 16
	t27_mem1 += MAS_MEM[1]

	t29_in = S.Task('t29_in', length=1, delay_cost=1)
	S += t29_in >= 16
	t29_in += MAS_in[0]

	t29_mem0 = S.Task('t29_mem0', length=1, delay_cost=1)
	S += t29_mem0 >= 16
	t29_mem0 += MM_MEM[0]

	t29_mem1 = S.Task('t29_mem1', length=1, delay_cost=1)
	S += t29_mem1 >= 16
	t29_mem1 += MM_MEM[1]

	t6 = S.Task('t6', length=2, delay_cost=1)
	S += t6 >= 16
	t6 += MAS[0]

	t27 = S.Task('t27', length=8, delay_cost=1)
	S += t27 >= 17
	t27 += MM[0]

	t29 = S.Task('t29', length=2, delay_cost=1)
	S += t29 >= 17
	t29 += MAS[0]

	t7_in = S.Task('t7_in', length=1, delay_cost=1)
	S += t7_in >= 17
	t7_in += MAS_in[0]

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	S += t7_mem0 >= 17
	t7_mem0 += MM_MEM[0]

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	S += t7_mem1 >= 17
	t7_mem1 += MAS_MEM[1]

	t28_in = S.Task('t28_in', length=1, delay_cost=1)
	S += t28_in >= 18
	t28_in += MAS_in[0]

	t28_mem0 = S.Task('t28_mem0', length=1, delay_cost=1)
	S += t28_mem0 >= 18
	t28_mem0 += MAS_MEM[0]

	t28_mem1 = S.Task('t28_mem1', length=1, delay_cost=1)
	S += t28_mem1 >= 18
	t28_mem1 += MM_MEM[1]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 18
	t30_in += MM_in[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 18
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 18
	t30_mem1 += MAS_MEM[1]

	t7 = S.Task('t7', length=2, delay_cost=1)
	S += t7 >= 18
	t7 += MAS[0]

	t17_in = S.Task('t17_in', length=1, delay_cost=1)
	S += t17_in >= 19
	t17_in += MAS_in[0]

	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	S += t17_mem0 >= 19
	t17_mem0 += MM_MEM[0]

	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	S += t17_mem1 >= 19
	t17_mem1 += MAS_MEM[1]

	t28 = S.Task('t28', length=2, delay_cost=1)
	S += t28 >= 19
	t28 += MAS[0]

	t30 = S.Task('t30', length=8, delay_cost=1)
	S += t30 >= 19
	t30 += MM[0]

	t17 = S.Task('t17', length=2, delay_cost=1)
	S += t17 >= 20
	t17 += MAS[0]

	t35_in = S.Task('t35_in', length=1, delay_cost=1)
	S += t35_in >= 20
	t35_in += MM_in[0]

	t35_mem0 = S.Task('t35_mem0', length=1, delay_cost=1)
	S += t35_mem0 >= 20
	t35_mem0 += MAS_MEM[0]

	t35_mem1 = S.Task('t35_mem1', length=1, delay_cost=1)
	S += t35_mem1 >= 20
	t35_mem1 += MAS_MEM[1]

	t35 = S.Task('t35', length=8, delay_cost=1)
	S += t35 >= 21
	t35 += MM[0]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 23
	t20_in += MAS_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 23
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 23
	t20_mem1 += MM_MEM[1]

	t20 = S.Task('t20', length=2, delay_cost=1)
	S += t20 >= 24
	t20 += MAS[0]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 26
	t31_in += MAS_in[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 26
	t31_mem0 += MM_MEM[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 26
	t31_mem1 += MM_MEM[1]

	t31 = S.Task('t31', length=2, delay_cost=1)
	S += t31 >= 27
	t31 += MAS[0]


	# new tasks
	t21 = S.Task('t21', length=2, delay_cost=1)
	t21 += alt(MAS)
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	t21_in += alt(MAS_in)
	S += t21_in*MAS_in[0]<=t21*MAS[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MM_MEM[0]
	S += 14 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAS_MEM[1]
	S += 25 < t21_mem1
	S += t21_mem1 <= t21

	t22 = S.Task('t22', length=2, delay_cost=1)
	t22 += alt(MAS)
	t22_in = S.Task('t22_in', length=1, delay_cost=1)
	t22_in += alt(MAS_in)
	S += t22_in*MAS_in[0]<=t22*MAS[0]

	t22_mem0 = S.Task('t22_mem0', length=1, delay_cost=1)
	t22_mem0 += MM_MEM[0]
	S += 14 < t22_mem0
	S += t22_mem0 <= t22

	t22_mem1 = S.Task('t22_mem1', length=1, delay_cost=1)
	t22_mem1 += MAS_MEM[1]
	S += 25 < t22_mem1
	S += t22_mem1 <= t22

	t32 = S.Task('t32', length=8, delay_cost=1)
	t32 += alt(MM)
	t32_in = S.Task('t32_in', length=1, delay_cost=1)
	t32_in += alt(MM_in)
	S += t32_in*MM_in[0]<=t32*MM[0]
	t32_mem0 = S.Task('t32_mem0', length=1, delay_cost=1)
	t32_mem0 += MAS_MEM[0]
	S += 20 < t32_mem0
	S += t32_mem0 <= t32

	t32_mem1 = S.Task('t32_mem1', length=1, delay_cost=1)
	t32_mem1 += MAS_MEM[1]
	S += 28 < t32_mem1
	S += t32_mem1 <= t32

	t33 = S.Task('t33', length=8, delay_cost=1)
	t33 += alt(MM)
	t33_in = S.Task('t33_in', length=1, delay_cost=1)
	t33_in += alt(MM_in)
	S += t33_in*MM_in[0]<=t33*MM[0]
	t33_mem0 = S.Task('t33_mem0', length=1, delay_cost=1)
	t33_mem0 += MAS_MEM[0]
	S += 21 < t33_mem0
	S += t33_mem0 <= t33

	t33_mem1 = S.Task('t33_mem1', length=1, delay_cost=1)
	t33_mem1 += MAS_MEM[1]
	S += 28 < t33_mem1
	S += t33_mem1 <= t33

	t23 = S.Task('t23', length=8, delay_cost=1)
	t23 += alt(MM)
	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	t23_in += alt(MM_in)
	S += t23_in*MM_in[0]<=t23*MM[0]
	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	t23_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t23_mem0*MAS_MEM[0]
	S += t23_mem0 <= t23

	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	t23_mem1 += alt(MAS_MEM)
	S += (t22*MAS[0])-1 < t23_mem1*MAS_MEM[1]
	S += t23_mem1 <= t23

	t34 = S.Task('t34', length=8, delay_cost=1)
	t34 += alt(MM)
	t34_in = S.Task('t34_in', length=1, delay_cost=1)
	t34_in += alt(MM_in)
	S += t34_in*MM_in[0]<=t34*MM[0]
	t34_mem0 = S.Task('t34_mem0', length=1, delay_cost=1)
	t34_mem0 += MAS_MEM[0]
	S += 19 < t34_mem0
	S += t34_mem0 <= t34

	t34_mem1 = S.Task('t34_mem1', length=1, delay_cost=1)
	t34_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t34_mem1*MAS_MEM[1]
	S += t34_mem1 <= t34

	t36 = S.Task('t36', length=8, delay_cost=1)
	t36 += alt(MM)
	t36_in = S.Task('t36_in', length=1, delay_cost=1)
	t36_in += alt(MM_in)
	S += t36_in*MM_in[0]<=t36*MM[0]
	t36_mem0 = S.Task('t36_mem0', length=1, delay_cost=1)
	t36_mem0 += MAS_MEM[0]
	S += 21 < t36_mem0
	S += t36_mem0 <= t36

	t36_mem1 = S.Task('t36_mem1', length=1, delay_cost=1)
	t36_mem1 += alt(MAS_MEM)
	S += (t22*MAS[0])-1 < t36_mem1*MAS_MEM[1]
	S += t36_mem1 <= t36

	Y_Hash0_new = S.Task('Y_Hash0_new', length=2, delay_cost=1)
	Y_Hash0_new += alt(MAS)
	Y_Hash0_new_in = S.Task('Y_Hash0_new_in', length=1, delay_cost=1)
	Y_Hash0_new_in += alt(MAS_in)
	S += Y_Hash0_new_in*MAS_in[0]<=Y_Hash0_new*MAS[0]

	S += 0<Y_Hash0_new

	Y_Hash0_new_w = S.Task('Y_Hash0_new_w', length=1, delay_cost=1)
	Y_Hash0_new_w += alt(MAIN_MEM_w)
	S += Y_Hash0_new <= Y_Hash0_new_w

	Y_Hash0_new_mem0 = S.Task('Y_Hash0_new_mem0', length=1, delay_cost=1)
	Y_Hash0_new_mem0 += alt(MM_MEM)
	S += (t23*MM[0])-1 < Y_Hash0_new_mem0*MM_MEM[0]
	S += Y_Hash0_new_mem0 <= Y_Hash0_new

	Y_Hash0_new_mem1 = S.Task('Y_Hash0_new_mem1', length=1, delay_cost=1)
	Y_Hash0_new_mem1 += alt(MM_MEM)
	S += (t32*MM[0])-1 < Y_Hash0_new_mem1*MM_MEM[1]
	S += Y_Hash0_new_mem1 <= Y_Hash0_new

	X_Hash0_new = S.Task('X_Hash0_new', length=2, delay_cost=1)
	X_Hash0_new += alt(MAS)
	X_Hash0_new_in = S.Task('X_Hash0_new_in', length=1, delay_cost=1)
	X_Hash0_new_in += alt(MAS_in)
	S += X_Hash0_new_in*MAS_in[0]<=X_Hash0_new*MAS[0]

	S += 0<X_Hash0_new

	X_Hash0_new_w = S.Task('X_Hash0_new_w', length=1, delay_cost=1)
	X_Hash0_new_w += alt(MAIN_MEM_w)
	S += X_Hash0_new <= X_Hash0_new_w

	X_Hash0_new_mem0 = S.Task('X_Hash0_new_mem0', length=1, delay_cost=1)
	X_Hash0_new_mem0 += alt(MM_MEM)
	S += (t34*MM[0])-1 < X_Hash0_new_mem0*MM_MEM[0]
	S += X_Hash0_new_mem0 <= X_Hash0_new

	X_Hash0_new_mem1 = S.Task('X_Hash0_new_mem1', length=1, delay_cost=1)
	X_Hash0_new_mem1 += alt(MM_MEM)
	S += (t33*MM[0])-1 < X_Hash0_new_mem1*MM_MEM[1]
	S += X_Hash0_new_mem1 <= X_Hash0_new

	Z_Hash0_new = S.Task('Z_Hash0_new', length=2, delay_cost=1)
	Z_Hash0_new += alt(MAS)
	Z_Hash0_new_in = S.Task('Z_Hash0_new_in', length=1, delay_cost=1)
	Z_Hash0_new_in += alt(MAS_in)
	S += Z_Hash0_new_in*MAS_in[0]<=Z_Hash0_new*MAS[0]

	S += 0<Z_Hash0_new

	Z_Hash0_new_w = S.Task('Z_Hash0_new_w', length=1, delay_cost=1)
	Z_Hash0_new_w += alt(MAIN_MEM_w)
	S += Z_Hash0_new <= Z_Hash0_new_w

	Z_Hash0_new_mem0 = S.Task('Z_Hash0_new_mem0', length=1, delay_cost=1)
	Z_Hash0_new_mem0 += alt(MM_MEM)
	S += (t36*MM[0])-1 < Z_Hash0_new_mem0*MM_MEM[0]
	S += Z_Hash0_new_mem0 <= Z_Hash0_new

	Z_Hash0_new_mem1 = S.Task('Z_Hash0_new_mem1', length=1, delay_cost=1)
	Z_Hash0_new_mem1 += MM_MEM[1]
	S += 28 < Z_Hash0_new_mem1
	S += Z_Hash0_new_mem1 <= Z_Hash0_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage2MAS1/EP_ADD_A_ANY/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution

