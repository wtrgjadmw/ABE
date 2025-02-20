from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 117
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	S += t2_in >= 0
	t2_in += MM_in[0]

	t2_mem1 = S.Task('t2_mem1', length=1, delay_cost=1)
	S += t2_mem1 >= 0
	t2_mem1 += MAIN_MEM_r[1]

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	S += t8_mem0 >= 0
	t8_mem0 += MAIN_MEM_r[0]

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	S += t0_mem0 >= 1
	t0_mem0 += MAIN_MEM_r[0]

	t0_mem1 = S.Task('t0_mem1', length=1, delay_cost=1)
	S += t0_mem1 >= 1
	t0_mem1 += MAIN_MEM_r[1]

	t13 = S.Task('t13', length=1, delay_cost=1)
	S += t13 >= 1
	t13 += MAS[2]

	t14 = S.Task('t14', length=1, delay_cost=1)
	S += t14 >= 1
	t14 += MAS[1]

	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	S += t1_in >= 1
	t1_in += MM_in[0]

	t2 = S.Task('t2', length=6, delay_cost=1)
	S += t2 >= 1
	t2 += MM[0]

	t4 = S.Task('t4', length=1, delay_cost=1)
	S += t4 >= 1
	t4 += MAS[0]

	t8 = S.Task('t8', length=1, delay_cost=1)
	S += t8 >= 1
	t8 += MAS[3]

	t9 = S.Task('t9', length=1, delay_cost=1)
	S += t9 >= 1
	t9 += MAS[4]

	t1 = S.Task('t1', length=6, delay_cost=1)
	S += t1 >= 2
	t1 += MM[0]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 2
	t10_in += MM_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 2
	t10_mem0 += MAS_MEM[6]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 2
	t10_mem1 += MAS_MEM[9]

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	S += t14_mem1 >= 2
	t14_mem1 += MAIN_MEM_r[1]

	t3 = S.Task('t3', length=1, delay_cost=1)
	S += t3 >= 2
	t3 += MAS[3]

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	S += t4_mem0 >= 2
	t4_mem0 += MAIN_MEM_r[0]

	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	S += t0_in >= 3
	t0_in += MM_in[0]

	t10 = S.Task('t10', length=6, delay_cost=1)
	S += t10 >= 3
	t10 += MM[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 3
	t30_mem0 += MAIN_MEM_r[0]

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 3
	t3_mem1 += MAIN_MEM_r[1]

	t0 = S.Task('t0', length=6, delay_cost=1)
	S += t0 >= 4
	t0 += MM[0]

	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	S += t4_mem1 >= 4
	t4_mem1 += MAIN_MEM_r[1]

	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	S += t5_in >= 4
	t5_in += MM_in[0]

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	S += t5_mem0 >= 4
	t5_mem0 += MAS_MEM[6]

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	S += t5_mem1 >= 4
	t5_mem1 += MAS_MEM[1]

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	S += t9_mem0 >= 4
	t9_mem0 += MAIN_MEM_r[0]

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	S += t13_mem0 >= 5
	t13_mem0 += MAIN_MEM_r[0]

	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	S += t15_in >= 5
	t15_in += MM_in[0]

	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	S += t15_mem0 >= 5
	t15_mem0 += MAS_MEM[4]

	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	S += t15_mem1 >= 5
	t15_mem1 += MAS_MEM[3]

	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	S += t1_mem1 >= 5
	t1_mem1 += MAIN_MEM_r[1]

	t5 = S.Task('t5', length=6, delay_cost=1)
	S += t5 >= 5
	t5 += MM[0]

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	S += t13_mem1 >= 6
	t13_mem1 += MAIN_MEM_r[1]

	t15 = S.Task('t15', length=6, delay_cost=1)
	S += t15 >= 6
	t15 += MM[0]

	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	S += t26_in >= 6
	t26_in += MM_in[0]

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	S += t26_mem1 >= 6
	t26_mem1 += MM_MEM[1]

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	S += t2_mem0 >= 6
	t2_mem0 += MAIN_MEM_r[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 7
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 7
	t11_mem1 += MM_MEM[1]

	t26 = S.Task('t26', length=6, delay_cost=1)
	S += t26 >= 7
	t26 += MM[0]

	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	S += t27_mem0 >= 7
	t27_mem0 += MAIN_MEM_r[0]

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	S += t8_mem1 >= 7
	t8_mem1 += MAIN_MEM_r[1]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 8
	t11 += MAS[3]

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	S += t12_mem0 >= 8
	t12_mem0 += MM_MEM[0]

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	S += t12_mem1 >= 8
	t12_mem1 += MAS_MEM[7]

	t19_in = S.Task('t19_in', length=1, delay_cost=1)
	S += t19_in >= 8
	t19_in += MM_in[0]

	t19_mem1 = S.Task('t19_mem1', length=1, delay_cost=1)
	S += t19_mem1 >= 8
	t19_mem1 += MM_MEM[1]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 8
	t3_mem0 += MAIN_MEM_r[0]

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	S += t9_mem1 >= 8
	t9_mem1 += MAIN_MEM_r[1]

	t12 = S.Task('t12', length=1, delay_cost=1)
	S += t12 >= 9
	t12 += MAS[2]

	t18_in = S.Task('t18_in', length=1, delay_cost=1)
	S += t18_in >= 9
	t18_in += MM_in[0]

	t18_mem1 = S.Task('t18_mem1', length=1, delay_cost=1)
	S += t18_mem1 >= 9
	t18_mem1 += MAS_MEM[5]

	t19 = S.Task('t19', length=6, delay_cost=1)
	S += t19 >= 9
	t19 += MM[0]

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	S += t1_mem0 >= 9
	t1_mem0 += MAIN_MEM_r[0]

	t18 = S.Task('t18', length=6, delay_cost=1)
	S += t18 >= 10
	t18 += MM[0]

	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	S += t24_mem0 >= 10
	t24_mem0 += MM_MEM[0]

	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	S += t26_mem0 >= 10
	t26_mem0 += MAIN_MEM_r[0]

	t27_in = S.Task('t27_in', length=1, delay_cost=1)
	S += t27_in >= 10
	t27_in += MM_in[0]

	t27_mem1 = S.Task('t27_mem1', length=1, delay_cost=1)
	S += t27_mem1 >= 10
	t27_mem1 += MAS_MEM[5]

	t18_mem0 = S.Task('t18_mem0', length=1, delay_cost=1)
	S += t18_mem0 >= 11
	t18_mem0 += MAIN_MEM_r[0]

	t24 = S.Task('t24', length=1, delay_cost=1)
	S += t24 >= 11
	t24 += MAS[1]

	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	S += t25_mem0 >= 11
	t25_mem0 += MM_MEM[0]

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	S += t25_mem1 >= 11
	t25_mem1 += MAS_MEM[3]

	t27 = S.Task('t27', length=6, delay_cost=1)
	S += t27 >= 11
	t27 += MM[0]

	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	S += t19_mem0 >= 12
	t19_mem0 += MAIN_MEM_r[0]

	t25 = S.Task('t25', length=1, delay_cost=1)
	S += t25 >= 12
	t25 += MAS[2]

	t28_mem0 = S.Task('t28_mem0', length=1, delay_cost=1)
	S += t28_mem0 >= 12
	t28_mem0 += MAS_MEM[4]

	t28_mem1 = S.Task('t28_mem1', length=1, delay_cost=1)
	S += t28_mem1 >= 12
	t28_mem1 += MM_MEM[1]

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	S += t7_mem0 >= 12
	t7_mem0 += MM_MEM[0]

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	S += t7_mem1 >= 12
	t7_mem1 += MAS_MEM[5]

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	S += t14_mem0 >= 13
	t14_mem0 += MAIN_MEM_r[0]

	t28 = S.Task('t28', length=1, delay_cost=1)
	S += t28 >= 13
	t28 += MAS[1]

	t29_mem0 = S.Task('t29_mem0', length=1, delay_cost=1)
	S += t29_mem0 >= 13
	t29_mem0 += MM_MEM[0]

	t29_mem1 = S.Task('t29_mem1', length=1, delay_cost=1)
	S += t29_mem1 >= 13
	t29_mem1 += MM_MEM[1]

	t35_in = S.Task('t35_in', length=1, delay_cost=1)
	S += t35_in >= 13
	t35_in += MM_in[0]

	t35_mem0 = S.Task('t35_mem0', length=1, delay_cost=1)
	S += t35_mem0 >= 13
	t35_mem0 += MAS_MEM[4]

	t35_mem1 = S.Task('t35_mem1', length=1, delay_cost=1)
	S += t35_mem1 >= 13
	t35_mem1 += MAS_MEM[3]

	t7 = S.Task('t7', length=1, delay_cost=1)
	S += t7 >= 13
	t7 += MAS[2]

	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	S += t16_mem0 >= 14
	t16_mem0 += MM_MEM[0]

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	S += t16_mem1 >= 14
	t16_mem1 += MM_MEM[1]

	t29 = S.Task('t29', length=1, delay_cost=1)
	S += t29 >= 14
	t29 += MAS[2]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 14
	t30_in += MM_in[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 14
	t30_mem1 += MAS_MEM[5]

	t35 = S.Task('t35', length=6, delay_cost=1)
	S += t35 >= 14
	t35 += MM[0]

	t16 = S.Task('t16', length=1, delay_cost=1)
	S += t16 >= 15
	t16 += MAS[3]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 15
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 15
	t20_mem1 += MM_MEM[1]

	t30 = S.Task('t30', length=6, delay_cost=1)
	S += t30 >= 15
	t30 += MM[0]

	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	S += t17_mem0 >= 16
	t17_mem0 += MM_MEM[0]

	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	S += t17_mem1 >= 16
	t17_mem1 += MAS_MEM[7]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 16
	t20 += MAS[2]

	t17 = S.Task('t17', length=1, delay_cost=1)
	S += t17 >= 17
	t17 += MAS[3]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 20
	t31_in += MM_in[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 20
	t31_mem0 += MM_MEM[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 20
	t31_mem1 += MM_MEM[1]

	t31 = S.Task('t31', length=6, delay_cost=1)
	S += t31 >= 21
	t31 += MM[0]


	# new tasks
	t6 = S.Task('t6', length=1, delay_cost=1)
	t6 += alt(MAS)

	S += t6<13

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	t6_mem0 += MM_MEM[0]
	S += 9 < t6_mem0
	S += t6_mem0 <= t6

	t6_mem1 = S.Task('t6_mem1', length=1, delay_cost=1)
	t6_mem1 += MM_MEM[1]
	S += 7 < t6_mem1
	S += t6_mem1 <= t6

	t21 = S.Task('t21', length=1, delay_cost=1)
	t21 += alt(MAS)

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MM_MEM[0]
	S += 7 < t21_mem0
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAS_MEM[5]
	S += 16 < t21_mem1
	S += t21_mem1 <= t21

	t22 = S.Task('t22', length=1, delay_cost=1)
	t22 += alt(MAS)

	t22_mem0 = S.Task('t22_mem0', length=1, delay_cost=1)
	t22_mem0 += MM_MEM[0]
	S += 7 < t22_mem0
	S += t22_mem0 <= t22

	t22_mem1 = S.Task('t22_mem1', length=1, delay_cost=1)
	t22_mem1 += MAS_MEM[5]
	S += 16 < t22_mem1
	S += t22_mem1 <= t22

	t32_in = S.Task('t32_in', length=1, delay_cost=1)
	t32_in += alt(MM_in)
	t32 = S.Task('t32', length=6, delay_cost=1)
	t32 += alt(MM)
	S += t32>=t32_in

	t32_mem0 = S.Task('t32_mem0', length=1, delay_cost=1)
	t32_mem0 += MAS_MEM[2]
	S += 13 < t32_mem0
	S += t32_mem0 <= t32

	t32_mem1 = S.Task('t32_mem1', length=1, delay_cost=1)
	t32_mem1 += MM_MEM[1]
	S += 26 < t32_mem1
	S += t32_mem1 <= t32

	t33_in = S.Task('t33_in', length=1, delay_cost=1)
	t33_in += alt(MM_in)
	t33 = S.Task('t33', length=6, delay_cost=1)
	t33 += alt(MM)
	S += t33>=t33_in

	t33_mem0 = S.Task('t33_mem0', length=1, delay_cost=1)
	t33_mem0 += MAS_MEM[6]
	S += 17 < t33_mem0
	S += t33_mem0 <= t33

	t33_mem1 = S.Task('t33_mem1', length=1, delay_cost=1)
	t33_mem1 += MM_MEM[1]
	S += 26 < t33_mem1
	S += t33_mem1 <= t33

	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	t23_in += alt(MM_in)
	t23 = S.Task('t23', length=6, delay_cost=1)
	t23 += alt(MM)
	S += t23>=t23_in

	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	t23_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t23_mem0*MAS_MEM[0]
	S += (t21*MAS[1])-1 < t23_mem0*MAS_MEM[2]
	S += (t21*MAS[2])-1 < t23_mem0*MAS_MEM[4]
	S += (t21*MAS[3])-1 < t23_mem0*MAS_MEM[6]
	S += (t21*MAS[4])-1 < t23_mem0*MAS_MEM[8]
	S += t23_mem0 <= t23

	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	t23_mem1 += alt(MAS_MEM)
	S += (t22*MAS[0])-1 < t23_mem1*MAS_MEM[1]
	S += (t22*MAS[1])-1 < t23_mem1*MAS_MEM[3]
	S += (t22*MAS[2])-1 < t23_mem1*MAS_MEM[5]
	S += (t22*MAS[3])-1 < t23_mem1*MAS_MEM[7]
	S += (t22*MAS[4])-1 < t23_mem1*MAS_MEM[9]
	S += t23_mem1 <= t23

	t34_in = S.Task('t34_in', length=1, delay_cost=1)
	t34_in += alt(MM_in)
	t34 = S.Task('t34', length=6, delay_cost=1)
	t34 += alt(MM)
	S += t34>=t34_in

	t34_mem0 = S.Task('t34_mem0', length=1, delay_cost=1)
	t34_mem0 += MAS_MEM[4]
	S += 13 < t34_mem0
	S += t34_mem0 <= t34

	t34_mem1 = S.Task('t34_mem1', length=1, delay_cost=1)
	t34_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t34_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t34_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t34_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t34_mem1*MAS_MEM[7]
	S += (t21*MAS[4])-1 < t34_mem1*MAS_MEM[9]
	S += t34_mem1 <= t34

	t36_in = S.Task('t36_in', length=1, delay_cost=1)
	t36_in += alt(MM_in)
	t36 = S.Task('t36', length=6, delay_cost=1)
	t36 += alt(MM)
	S += t36>=t36_in

	t36_mem0 = S.Task('t36_mem0', length=1, delay_cost=1)
	t36_mem0 += MAS_MEM[6]
	S += 17 < t36_mem0
	S += t36_mem0 <= t36

	t36_mem1 = S.Task('t36_mem1', length=1, delay_cost=1)
	t36_mem1 += alt(MAS_MEM)
	S += (t22*MAS[0])-1 < t36_mem1*MAS_MEM[1]
	S += (t22*MAS[1])-1 < t36_mem1*MAS_MEM[3]
	S += (t22*MAS[2])-1 < t36_mem1*MAS_MEM[5]
	S += (t22*MAS[3])-1 < t36_mem1*MAS_MEM[7]
	S += (t22*MAS[4])-1 < t36_mem1*MAS_MEM[9]
	S += t36_mem1 <= t36

	PY_new = S.Task('PY_new', length=1, delay_cost=1)
	PY_new += alt(MAS)

	S += 0<PY_new

	PY_new_w = S.Task('PY_new_w', length=1, delay_cost=1)
	PY_new_w += alt(MAIN_MEM_w)
	S += PY_new <= PY_new_w

	PY_new_mem0 = S.Task('PY_new_mem0', length=1, delay_cost=1)
	PY_new_mem0 += alt(MM_MEM)
	S += (t23*MM[0])-1 < PY_new_mem0*MM_MEM[0]
	S += PY_new_mem0 <= PY_new

	PY_new_mem1 = S.Task('PY_new_mem1', length=1, delay_cost=1)
	PY_new_mem1 += alt(MM_MEM)
	S += (t32*MM[0])-1 < PY_new_mem1*MM_MEM[1]
	S += PY_new_mem1 <= PY_new

	PX_new = S.Task('PX_new', length=1, delay_cost=1)
	PX_new += alt(MAS)

	S += 0<PX_new

	PX_new_w = S.Task('PX_new_w', length=1, delay_cost=1)
	PX_new_w += alt(MAIN_MEM_w)
	S += PX_new <= PX_new_w

	PX_new_mem0 = S.Task('PX_new_mem0', length=1, delay_cost=1)
	PX_new_mem0 += alt(MM_MEM)
	S += (t34*MM[0])-1 < PX_new_mem0*MM_MEM[0]
	S += PX_new_mem0 <= PX_new

	PX_new_mem1 = S.Task('PX_new_mem1', length=1, delay_cost=1)
	PX_new_mem1 += alt(MM_MEM)
	S += (t33*MM[0])-1 < PX_new_mem1*MM_MEM[1]
	S += PX_new_mem1 <= PX_new

	PZ_new = S.Task('PZ_new', length=1, delay_cost=1)
	PZ_new += alt(MAS)

	S += 0<PZ_new

	PZ_new_w = S.Task('PZ_new_w', length=1, delay_cost=1)
	PZ_new_w += alt(MAIN_MEM_w)
	S += PZ_new <= PZ_new_w

	PZ_new_mem0 = S.Task('PZ_new_mem0', length=1, delay_cost=1)
	PZ_new_mem0 += alt(MM_MEM)
	S += (t36*MM[0])-1 < PZ_new_mem0*MM_MEM[0]
	S += PZ_new_mem0 <= PZ_new

	PZ_new_mem1 = S.Task('PZ_new_mem1', length=1, delay_cost=1)
	PZ_new_mem1 += MM_MEM[1]
	S += 19 < PZ_new_mem1
	S += PZ_new_mem1 <= PZ_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS5/EP_ADD_A_ANY/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

