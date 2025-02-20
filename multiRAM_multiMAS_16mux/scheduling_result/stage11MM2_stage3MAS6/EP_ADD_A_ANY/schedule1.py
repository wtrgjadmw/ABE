from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 168
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	S += t2_in >= 0
	t2_in += MM_in[1]

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

	t2 = S.Task('t2', length=11, delay_cost=1)
	S += t2 >= 1
	t2 += MM[1]

	t0 = S.Task('t0', length=11, delay_cost=1)
	S += t0 >= 2
	t0 += MM[0]

	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	S += t1_in >= 2
	t1_in += MM_in[1]

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	S += t1_mem0 >= 2
	t1_mem0 += MAIN_MEM_r[0]

	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	S += t1_mem1 >= 2
	t1_mem1 += MAIN_MEM_r[1]

	t1 = S.Task('t1', length=11, delay_cost=1)
	S += t1 >= 3
	t1 += MM[1]

	t8_in = S.Task('t8_in', length=1, delay_cost=1)
	S += t8_in >= 3
	t8_in += MAS_in[1]

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	S += t8_mem0 >= 3
	t8_mem0 += MAIN_MEM_r[0]

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	S += t8_mem1 >= 3
	t8_mem1 += MAIN_MEM_r[1]

	t8 = S.Task('t8', length=3, delay_cost=1)
	S += t8 >= 4
	t8 += MAS[1]

	t9_in = S.Task('t9_in', length=1, delay_cost=1)
	S += t9_in >= 4
	t9_in += MAS_in[1]

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	S += t9_mem0 >= 4
	t9_mem0 += MAIN_MEM_r[0]

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	S += t9_mem1 >= 4
	t9_mem1 += MAIN_MEM_r[1]

	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	S += t3_in >= 5
	t3_in += MAS_in[0]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 5
	t3_mem0 += MAIN_MEM_r[0]

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 5
	t3_mem1 += MAIN_MEM_r[1]

	t9 = S.Task('t9', length=3, delay_cost=1)
	S += t9 >= 5
	t9 += MAS[1]

	t3 = S.Task('t3', length=3, delay_cost=1)
	S += t3 >= 6
	t3 += MAS[0]

	t4_in = S.Task('t4_in', length=1, delay_cost=1)
	S += t4_in >= 6
	t4_in += MAS_in[5]

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	S += t4_mem0 >= 6
	t4_mem0 += MAIN_MEM_r[0]

	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	S += t4_mem1 >= 6
	t4_mem1 += MAIN_MEM_r[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 7
	t10_in += MM_in[1]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 7
	t10_mem0 += MAS_MEM[2]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 7
	t10_mem1 += MAS_MEM[3]

	t14_in = S.Task('t14_in', length=1, delay_cost=1)
	S += t14_in >= 7
	t14_in += MAS_in[2]

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	S += t14_mem0 >= 7
	t14_mem0 += MAIN_MEM_r[0]

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	S += t14_mem1 >= 7
	t14_mem1 += MAIN_MEM_r[1]

	t4 = S.Task('t4', length=3, delay_cost=1)
	S += t4 >= 7
	t4 += MAS[5]

	t10 = S.Task('t10', length=11, delay_cost=1)
	S += t10 >= 8
	t10 += MM[1]

	t13_in = S.Task('t13_in', length=1, delay_cost=1)
	S += t13_in >= 8
	t13_in += MAS_in[4]

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	S += t13_mem0 >= 8
	t13_mem0 += MAIN_MEM_r[0]

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	S += t13_mem1 >= 8
	t13_mem1 += MAIN_MEM_r[1]

	t14 = S.Task('t14', length=3, delay_cost=1)
	S += t14 >= 8
	t14 += MAS[2]

	t13 = S.Task('t13', length=3, delay_cost=1)
	S += t13 >= 9
	t13 += MAS[4]

	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	S += t5_in >= 9
	t5_in += MM_in[0]

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	S += t5_mem0 >= 9
	t5_mem0 += MAS_MEM[0]

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	S += t5_mem1 >= 9
	t5_mem1 += MAS_MEM[11]

	t5 = S.Task('t5', length=11, delay_cost=1)
	S += t5 >= 10
	t5 += MM[0]

	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	S += t15_in >= 11
	t15_in += MM_in[1]

	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	S += t15_mem0 >= 11
	t15_mem0 += MAS_MEM[8]

	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	S += t15_mem1 >= 11
	t15_mem1 += MAS_MEM[5]

	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	S += t26_in >= 11
	t26_in += MM_in[0]

	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	S += t26_mem0 >= 11
	t26_mem0 += MAIN_MEM_r[0]

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	S += t26_mem1 >= 11
	t26_mem1 += MM_MEM[3]

	t15 = S.Task('t15', length=11, delay_cost=1)
	S += t15 >= 12
	t15 += MM[1]

	t19_in = S.Task('t19_in', length=1, delay_cost=1)
	S += t19_in >= 12
	t19_in += MM_in[1]

	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	S += t19_mem0 >= 12
	t19_mem0 += MAIN_MEM_r[0]

	t19_mem1 = S.Task('t19_mem1', length=1, delay_cost=1)
	S += t19_mem1 >= 12
	t19_mem1 += MM_MEM[3]

	t24_in = S.Task('t24_in', length=1, delay_cost=1)
	S += t24_in >= 12
	t24_in += MAS_in[2]

	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	S += t24_mem0 >= 12
	t24_mem0 += MM_MEM[0]

	t24_mem1 = S.Task('t24_mem1', length=1, delay_cost=1)
	S += t24_mem1 >= 12
	t24_mem1 += MM_MEM[1]

	t26 = S.Task('t26', length=11, delay_cost=1)
	S += t26 >= 12
	t26 += MM[0]

	t16_in = S.Task('t16_in', length=1, delay_cost=1)
	S += t16_in >= 13
	t16_in += MAS_in[3]

	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	S += t16_mem0 >= 13
	t16_mem0 += MM_MEM[0]

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	S += t16_mem1 >= 13
	t16_mem1 += MM_MEM[3]

	t19 = S.Task('t19', length=11, delay_cost=1)
	S += t19 >= 13
	t19 += MM[1]

	t24 = S.Task('t24', length=3, delay_cost=1)
	S += t24 >= 13
	t24 += MAS[2]

	t16 = S.Task('t16', length=3, delay_cost=1)
	S += t16 >= 14
	t16 += MAS[3]

	t6_in = S.Task('t6_in', length=1, delay_cost=1)
	S += t6_in >= 14
	t6_in += MAS_in[5]

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	S += t6_mem0 >= 14
	t6_mem0 += MM_MEM[0]

	t6_mem1 = S.Task('t6_mem1', length=1, delay_cost=1)
	S += t6_mem1 >= 14
	t6_mem1 += MM_MEM[3]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 15
	t11_in += MAS_in[5]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 15
	t11_mem0 += MM_MEM[2]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 15
	t11_mem1 += MM_MEM[3]

	t25_in = S.Task('t25_in', length=1, delay_cost=1)
	S += t25_in >= 15
	t25_in += MAS_in[4]

	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	S += t25_mem0 >= 15
	t25_mem0 += MM_MEM[0]

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	S += t25_mem1 >= 15
	t25_mem1 += MAS_MEM[5]

	t6 = S.Task('t6', length=3, delay_cost=1)
	S += t6 >= 15
	t6 += MAS[5]

	t11 = S.Task('t11', length=3, delay_cost=1)
	S += t11 >= 16
	t11 += MAS[5]

	t25 = S.Task('t25', length=3, delay_cost=1)
	S += t25 >= 16
	t25 += MAS[4]

	t12_in = S.Task('t12_in', length=1, delay_cost=1)
	S += t12_in >= 18
	t12_in += MAS_in[0]

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	S += t12_mem0 >= 18
	t12_mem0 += MM_MEM[2]

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	S += t12_mem1 >= 18
	t12_mem1 += MAS_MEM[11]

	t12 = S.Task('t12', length=3, delay_cost=1)
	S += t12 >= 19
	t12 += MAS[0]

	t7_in = S.Task('t7_in', length=1, delay_cost=1)
	S += t7_in >= 20
	t7_in += MAS_in[3]

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	S += t7_mem0 >= 20
	t7_mem0 += MM_MEM[0]

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	S += t7_mem1 >= 20
	t7_mem1 += MAS_MEM[11]

	t18_in = S.Task('t18_in', length=1, delay_cost=1)
	S += t18_in >= 21
	t18_in += MM_in[0]

	t18_mem0 = S.Task('t18_mem0', length=1, delay_cost=1)
	S += t18_mem0 >= 21
	t18_mem0 += MAIN_MEM_r[0]

	t18_mem1 = S.Task('t18_mem1', length=1, delay_cost=1)
	S += t18_mem1 >= 21
	t18_mem1 += MAS_MEM[1]

	t7 = S.Task('t7', length=3, delay_cost=1)
	S += t7 >= 21
	t7 += MAS[3]

	t17_in = S.Task('t17_in', length=1, delay_cost=1)
	S += t17_in >= 22
	t17_in += MAS_in[1]

	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	S += t17_mem0 >= 22
	t17_mem0 += MM_MEM[2]

	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	S += t17_mem1 >= 22
	t17_mem1 += MAS_MEM[7]

	t18 = S.Task('t18', length=11, delay_cost=1)
	S += t18 >= 22
	t18 += MM[0]

	t27_in = S.Task('t27_in', length=1, delay_cost=1)
	S += t27_in >= 22
	t27_in += MM_in[0]

	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	S += t27_mem0 >= 22
	t27_mem0 += MAIN_MEM_r[0]

	t27_mem1 = S.Task('t27_mem1', length=1, delay_cost=1)
	S += t27_mem1 >= 22
	t27_mem1 += MAS_MEM[1]

	t29_in = S.Task('t29_in', length=1, delay_cost=1)
	S += t29_in >= 22
	t29_in += MAS_in[2]

	t29_mem0 = S.Task('t29_mem0', length=1, delay_cost=1)
	S += t29_mem0 >= 22
	t29_mem0 += MM_MEM[0]

	t29_mem1 = S.Task('t29_mem1', length=1, delay_cost=1)
	S += t29_mem1 >= 22
	t29_mem1 += MM_MEM[1]

	t17 = S.Task('t17', length=3, delay_cost=1)
	S += t17 >= 23
	t17 += MAS[1]

	t27 = S.Task('t27', length=11, delay_cost=1)
	S += t27 >= 23
	t27 += MM[0]

	t28_in = S.Task('t28_in', length=1, delay_cost=1)
	S += t28_in >= 23
	t28_in += MAS_in[2]

	t28_mem0 = S.Task('t28_mem0', length=1, delay_cost=1)
	S += t28_mem0 >= 23
	t28_mem0 += MAS_MEM[8]

	t28_mem1 = S.Task('t28_mem1', length=1, delay_cost=1)
	S += t28_mem1 >= 23
	t28_mem1 += MM_MEM[1]

	t29 = S.Task('t29', length=3, delay_cost=1)
	S += t29 >= 23
	t29 += MAS[2]

	t28 = S.Task('t28', length=3, delay_cost=1)
	S += t28 >= 24
	t28 += MAS[2]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 25
	t30_in += MM_in[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 25
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 25
	t30_mem1 += MAS_MEM[5]

	t30 = S.Task('t30', length=11, delay_cost=1)
	S += t30 >= 26
	t30 += MM[1]

	t35_in = S.Task('t35_in', length=1, delay_cost=1)
	S += t35_in >= 26
	t35_in += MM_in[1]

	t35_mem0 = S.Task('t35_mem0', length=1, delay_cost=1)
	S += t35_mem0 >= 26
	t35_mem0 += MAS_MEM[6]

	t35_mem1 = S.Task('t35_mem1', length=1, delay_cost=1)
	S += t35_mem1 >= 26
	t35_mem1 += MAS_MEM[5]

	t35 = S.Task('t35', length=11, delay_cost=1)
	S += t35 >= 27
	t35 += MM[1]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 32
	t20_in += MAS_in[4]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 32
	t20_mem0 += MM_MEM[2]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 32
	t20_mem1 += MM_MEM[1]

	t20 = S.Task('t20', length=3, delay_cost=1)
	S += t20 >= 33
	t20 += MAS[4]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 36
	t31_in += MM_in[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 36
	t31_mem0 += MM_MEM[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 36
	t31_mem1 += MM_MEM[3]

	t31 = S.Task('t31', length=11, delay_cost=1)
	S += t31 >= 37
	t31 += MM[0]


	# new tasks
	t21 = S.Task('t21', length=3, delay_cost=1)
	t21 += alt(MAS)
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	t21_in += alt(MAS_in)
	S += t21_in*MAS_in[0]<=t21*MAS[0]

	S += t21_in*MAS_in[1]<=t21*MAS[1]

	S += t21_in*MAS_in[2]<=t21*MAS[2]

	S += t21_in*MAS_in[3]<=t21*MAS[3]

	S += t21_in*MAS_in[4]<=t21*MAS[4]

	S += t21_in*MAS_in[5]<=t21*MAS[5]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MM_MEM[2]
	S += 13 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAS_MEM[9]
	S += 35 < t21_mem1
	S += t21_mem1 <= t21

	t22 = S.Task('t22', length=3, delay_cost=1)
	t22 += alt(MAS)
	t22_in = S.Task('t22_in', length=1, delay_cost=1)
	t22_in += alt(MAS_in)
	S += t22_in*MAS_in[0]<=t22*MAS[0]

	S += t22_in*MAS_in[1]<=t22*MAS[1]

	S += t22_in*MAS_in[2]<=t22*MAS[2]

	S += t22_in*MAS_in[3]<=t22*MAS[3]

	S += t22_in*MAS_in[4]<=t22*MAS[4]

	S += t22_in*MAS_in[5]<=t22*MAS[5]

	t22_mem0 = S.Task('t22_mem0', length=1, delay_cost=1)
	t22_mem0 += MM_MEM[2]
	S += 13 < t22_mem0
	S += t22_mem0 <= t22

	t22_mem1 = S.Task('t22_mem1', length=1, delay_cost=1)
	t22_mem1 += MAS_MEM[9]
	S += 35 < t22_mem1
	S += t22_mem1 <= t22

	t32 = S.Task('t32', length=11, delay_cost=1)
	t32 += alt(MM)
	t32_in = S.Task('t32_in', length=1, delay_cost=1)
	t32_in += alt(MM_in)
	S += t32_in*MM_in[0]<=t32*MM[0]
	S += t32_in*MM_in[1]<=t32*MM[1]
	t32_mem0 = S.Task('t32_mem0', length=1, delay_cost=1)
	t32_mem0 += MAS_MEM[4]
	S += 26 < t32_mem0
	S += t32_mem0 <= t32

	t32_mem1 = S.Task('t32_mem1', length=1, delay_cost=1)
	t32_mem1 += MM_MEM[1]
	S += 47 < t32_mem1
	S += t32_mem1 <= t32

	t33 = S.Task('t33', length=11, delay_cost=1)
	t33 += alt(MM)
	t33_in = S.Task('t33_in', length=1, delay_cost=1)
	t33_in += alt(MM_in)
	S += t33_in*MM_in[0]<=t33*MM[0]
	S += t33_in*MM_in[1]<=t33*MM[1]
	t33_mem0 = S.Task('t33_mem0', length=1, delay_cost=1)
	t33_mem0 += MAS_MEM[2]
	S += 25 < t33_mem0
	S += t33_mem0 <= t33

	t33_mem1 = S.Task('t33_mem1', length=1, delay_cost=1)
	t33_mem1 += MM_MEM[1]
	S += 47 < t33_mem1
	S += t33_mem1 <= t33

	t23 = S.Task('t23', length=11, delay_cost=1)
	t23 += alt(MM)
	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	t23_in += alt(MM_in)
	S += t23_in*MM_in[0]<=t23*MM[0]
	S += t23_in*MM_in[1]<=t23*MM[1]
	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	t23_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t23_mem0*MAS_MEM[0]
	S += (t21*MAS[1])-1 < t23_mem0*MAS_MEM[2]
	S += (t21*MAS[2])-1 < t23_mem0*MAS_MEM[4]
	S += (t21*MAS[3])-1 < t23_mem0*MAS_MEM[6]
	S += (t21*MAS[4])-1 < t23_mem0*MAS_MEM[8]
	S += (t21*MAS[5])-1 < t23_mem0*MAS_MEM[10]
	S += t23_mem0 <= t23

	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	t23_mem1 += alt(MAS_MEM)
	S += (t22*MAS[0])-1 < t23_mem1*MAS_MEM[1]
	S += (t22*MAS[1])-1 < t23_mem1*MAS_MEM[3]
	S += (t22*MAS[2])-1 < t23_mem1*MAS_MEM[5]
	S += (t22*MAS[3])-1 < t23_mem1*MAS_MEM[7]
	S += (t22*MAS[4])-1 < t23_mem1*MAS_MEM[9]
	S += (t22*MAS[5])-1 < t23_mem1*MAS_MEM[11]
	S += t23_mem1 <= t23

	t34 = S.Task('t34', length=11, delay_cost=1)
	t34 += alt(MM)
	t34_in = S.Task('t34_in', length=1, delay_cost=1)
	t34_in += alt(MM_in)
	S += t34_in*MM_in[0]<=t34*MM[0]
	S += t34_in*MM_in[1]<=t34*MM[1]
	t34_mem0 = S.Task('t34_mem0', length=1, delay_cost=1)
	t34_mem0 += MAS_MEM[6]
	S += 23 < t34_mem0
	S += t34_mem0 <= t34

	t34_mem1 = S.Task('t34_mem1', length=1, delay_cost=1)
	t34_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t34_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t34_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t34_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t34_mem1*MAS_MEM[7]
	S += (t21*MAS[4])-1 < t34_mem1*MAS_MEM[9]
	S += (t21*MAS[5])-1 < t34_mem1*MAS_MEM[11]
	S += t34_mem1 <= t34

	t36 = S.Task('t36', length=11, delay_cost=1)
	t36 += alt(MM)
	t36_in = S.Task('t36_in', length=1, delay_cost=1)
	t36_in += alt(MM_in)
	S += t36_in*MM_in[0]<=t36*MM[0]
	S += t36_in*MM_in[1]<=t36*MM[1]
	t36_mem0 = S.Task('t36_mem0', length=1, delay_cost=1)
	t36_mem0 += MAS_MEM[2]
	S += 25 < t36_mem0
	S += t36_mem0 <= t36

	t36_mem1 = S.Task('t36_mem1', length=1, delay_cost=1)
	t36_mem1 += alt(MAS_MEM)
	S += (t22*MAS[0])-1 < t36_mem1*MAS_MEM[1]
	S += (t22*MAS[1])-1 < t36_mem1*MAS_MEM[3]
	S += (t22*MAS[2])-1 < t36_mem1*MAS_MEM[5]
	S += (t22*MAS[3])-1 < t36_mem1*MAS_MEM[7]
	S += (t22*MAS[4])-1 < t36_mem1*MAS_MEM[9]
	S += (t22*MAS[5])-1 < t36_mem1*MAS_MEM[11]
	S += t36_mem1 <= t36

	PY_new = S.Task('PY_new', length=3, delay_cost=1)
	PY_new += alt(MAS)
	PY_new_in = S.Task('PY_new_in', length=1, delay_cost=1)
	PY_new_in += alt(MAS_in)
	S += PY_new_in*MAS_in[0]<=PY_new*MAS[0]

	S += PY_new_in*MAS_in[1]<=PY_new*MAS[1]

	S += PY_new_in*MAS_in[2]<=PY_new*MAS[2]

	S += PY_new_in*MAS_in[3]<=PY_new*MAS[3]

	S += PY_new_in*MAS_in[4]<=PY_new*MAS[4]

	S += PY_new_in*MAS_in[5]<=PY_new*MAS[5]

	S += 0<PY_new

	PY_new_w = S.Task('PY_new_w', length=1, delay_cost=1)
	PY_new_w += alt(MAIN_MEM_w)
	S += PY_new <= PY_new_w

	PY_new_mem0 = S.Task('PY_new_mem0', length=1, delay_cost=1)
	PY_new_mem0 += alt(MM_MEM)
	S += (t23*MM[0])-1 < PY_new_mem0*MM_MEM[0]
	S += (t23*MM[1])-1 < PY_new_mem0*MM_MEM[2]
	S += PY_new_mem0 <= PY_new

	PY_new_mem1 = S.Task('PY_new_mem1', length=1, delay_cost=1)
	PY_new_mem1 += alt(MM_MEM)
	S += (t32*MM[0])-1 < PY_new_mem1*MM_MEM[1]
	S += (t32*MM[1])-1 < PY_new_mem1*MM_MEM[3]
	S += PY_new_mem1 <= PY_new

	PX_new = S.Task('PX_new', length=3, delay_cost=1)
	PX_new += alt(MAS)
	PX_new_in = S.Task('PX_new_in', length=1, delay_cost=1)
	PX_new_in += alt(MAS_in)
	S += PX_new_in*MAS_in[0]<=PX_new*MAS[0]

	S += PX_new_in*MAS_in[1]<=PX_new*MAS[1]

	S += PX_new_in*MAS_in[2]<=PX_new*MAS[2]

	S += PX_new_in*MAS_in[3]<=PX_new*MAS[3]

	S += PX_new_in*MAS_in[4]<=PX_new*MAS[4]

	S += PX_new_in*MAS_in[5]<=PX_new*MAS[5]

	S += 0<PX_new

	PX_new_w = S.Task('PX_new_w', length=1, delay_cost=1)
	PX_new_w += alt(MAIN_MEM_w)
	S += PX_new <= PX_new_w

	PX_new_mem0 = S.Task('PX_new_mem0', length=1, delay_cost=1)
	PX_new_mem0 += alt(MM_MEM)
	S += (t34*MM[0])-1 < PX_new_mem0*MM_MEM[0]
	S += (t34*MM[1])-1 < PX_new_mem0*MM_MEM[2]
	S += PX_new_mem0 <= PX_new

	PX_new_mem1 = S.Task('PX_new_mem1', length=1, delay_cost=1)
	PX_new_mem1 += alt(MM_MEM)
	S += (t33*MM[0])-1 < PX_new_mem1*MM_MEM[1]
	S += (t33*MM[1])-1 < PX_new_mem1*MM_MEM[3]
	S += PX_new_mem1 <= PX_new

	PZ_new = S.Task('PZ_new', length=3, delay_cost=1)
	PZ_new += alt(MAS)
	PZ_new_in = S.Task('PZ_new_in', length=1, delay_cost=1)
	PZ_new_in += alt(MAS_in)
	S += PZ_new_in*MAS_in[0]<=PZ_new*MAS[0]

	S += PZ_new_in*MAS_in[1]<=PZ_new*MAS[1]

	S += PZ_new_in*MAS_in[2]<=PZ_new*MAS[2]

	S += PZ_new_in*MAS_in[3]<=PZ_new*MAS[3]

	S += PZ_new_in*MAS_in[4]<=PZ_new*MAS[4]

	S += PZ_new_in*MAS_in[5]<=PZ_new*MAS[5]

	S += 0<PZ_new

	PZ_new_w = S.Task('PZ_new_w', length=1, delay_cost=1)
	PZ_new_w += alt(MAIN_MEM_w)
	S += PZ_new <= PZ_new_w

	PZ_new_mem0 = S.Task('PZ_new_mem0', length=1, delay_cost=1)
	PZ_new_mem0 += alt(MM_MEM)
	S += (t36*MM[0])-1 < PZ_new_mem0*MM_MEM[0]
	S += (t36*MM[1])-1 < PZ_new_mem0*MM_MEM[2]
	S += PZ_new_mem0 <= PZ_new

	PZ_new_mem1 = S.Task('PZ_new_mem1', length=1, delay_cost=1)
	PZ_new_mem1 += MM_MEM[3]
	S += 37 < PZ_new_mem1
	S += PZ_new_mem1 <= PZ_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage3MAS6/EP_ADD_A_ANY/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

