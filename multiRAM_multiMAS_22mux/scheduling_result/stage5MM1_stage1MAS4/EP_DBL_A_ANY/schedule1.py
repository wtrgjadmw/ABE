from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 101
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling
	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	S += t23_in >= 0
	t23_in += MM_in[0]

	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	S += t23_mem0 >= 0
	t23_mem0 += MAIN_MEM_r

	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	S += t23_mem1 >= 0
	t23_mem1 += MAIN_MEM_r

	t23 = S.Task('t23', length=5, delay_cost=1)
	S += t23 >= 1
	t23 += MM[0]

	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	S += t5_in >= 1
	t5_in += MM_in[0]

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	S += t5_mem0 >= 1
	t5_mem0 += MAIN_MEM_r

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	S += t5_mem1 >= 1
	t5_mem1 += MAIN_MEM_r

	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	S += t3_in >= 2
	t3_in += MM_in[0]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 2
	t3_mem0 += MAIN_MEM_r

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 2
	t3_mem1 += MAIN_MEM_r

	t5 = S.Task('t5', length=5, delay_cost=1)
	S += t5 >= 2
	t5 += MM[0]

	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	S += t1_in >= 3
	t1_in += MM_in[0]

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	S += t1_mem0 >= 3
	t1_mem0 += MAIN_MEM_r

	t3 = S.Task('t3', length=5, delay_cost=1)
	S += t3 >= 3
	t3 += MM[0]

	t1 = S.Task('t1', length=5, delay_cost=1)
	S += t1 >= 4
	t1 += MM[0]

	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	S += t2_in >= 4
	t2_in += MM_in[0]

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	S += t2_mem0 >= 4
	t2_mem0 += MAIN_MEM_r

	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	S += t0_in >= 5
	t0_in += MM_in[0]

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	S += t0_mem0 >= 5
	t0_mem0 += MAIN_MEM_r

	t2 = S.Task('t2', length=5, delay_cost=1)
	S += t2 >= 5
	t2 += MM[0]

	t0 = S.Task('t0', length=5, delay_cost=1)
	S += t0 >= 6
	t0 += MM[0]


	# new tasks
	t4 = S.Task('t4', length=1, delay_cost=1)
	t4 += alt(MAS)

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	t4_mem0 += MM_MEM[0]
	S += 7 < t4_mem0
	S += t4_mem0 <= t4

	t6 = S.Task('t6', length=1, delay_cost=1)
	t6 += alt(MAS)

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	t6_mem0 += MM_MEM[0]
	S += 6 < t6_mem0
	S += t6_mem0 <= t6

	t8_in = S.Task('t8_in', length=1, delay_cost=1)
	t8_in += alt(MM_in)
	t8 = S.Task('t8', length=5, delay_cost=1)
	t8 += alt(MM)
	S += t8>=t8_in

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	t8_mem0 += MAIN_MEM_r
	S += t8_mem0 <= t8

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	t8_mem1 += MM_MEM[0]
	S += 9 < t8_mem1
	S += t8_mem1 <= t8

	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	t15_in += alt(MM_in)
	t15 = S.Task('t15', length=5, delay_cost=1)
	t15 += alt(MM)
	S += t15>=t15_in

	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	t15_mem0 += MAIN_MEM_r
	S += t15_mem0 <= t15

	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	t15_mem1 += MM_MEM[0]
	S += 9 < t15_mem1
	S += t15_mem1 <= t15

	t19 = S.Task('t19', length=1, delay_cost=1)
	t19 += alt(MAS)

	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	t19_mem0 += MM_MEM[0]
	S += 10 < t19_mem0
	S += t19_mem0 <= t19

	t24 = S.Task('t24', length=1, delay_cost=1)
	t24 += alt(MAS)

	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	t24_mem0 += MM_MEM[0]
	S += 5 < t24_mem0
	S += t24_mem0 <= t24

	t7_in = S.Task('t7_in', length=1, delay_cost=1)
	t7_in += alt(MM_in)
	t7 = S.Task('t7', length=5, delay_cost=1)
	t7 += alt(MM)
	S += t7>=t7_in

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	t7_mem0 += MAIN_MEM_r
	S += t7_mem0 <= t7

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	t7_mem1 += alt(MAS_MEM)
	S += (t6*MAS[0])-1 < t7_mem1*MAS_MEM[0]
	S += (t6*MAS[1])-1 < t7_mem1*MAS_MEM[1]
	S += (t6*MAS[2])-1 < t7_mem1*MAS_MEM[2]
	S += (t6*MAS[3])-1 < t7_mem1*MAS_MEM[3]
	S += t7_mem1 <= t7

	t14_in = S.Task('t14_in', length=1, delay_cost=1)
	t14_in += alt(MM_in)
	t14 = S.Task('t14', length=5, delay_cost=1)
	t14 += alt(MM)
	S += t14>=t14_in

	S += 0<t14

	t14_w = S.Task('t14_w', length=1, delay_cost=1)
	t14_w += alt(MAIN_MEM_w)
	S += t14 <= t14_w

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	t14_mem0 += MAIN_MEM_r
	S += t14_mem0 <= t14

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	t14_mem1 += alt(MAS_MEM)
	S += (t6*MAS[0])-1 < t14_mem1*MAS_MEM[0]
	S += (t6*MAS[1])-1 < t14_mem1*MAS_MEM[1]
	S += (t6*MAS[2])-1 < t14_mem1*MAS_MEM[2]
	S += (t6*MAS[3])-1 < t14_mem1*MAS_MEM[3]
	S += t14_mem1 <= t14

	t16 = S.Task('t16', length=1, delay_cost=1)
	t16 += alt(MAS)

	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	t16_mem0 += MM_MEM[0]
	S += 10 < t16_mem0
	S += t16_mem0 <= t16

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	t16_mem1 += alt(MM_MEM)
	S += (t15*MM[0])-1 < t16_mem1*MM_MEM[0]
	S += t16_mem1 <= t16

	t20 = S.Task('t20', length=1, delay_cost=1)
	t20 += alt(MAS)

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += MM_MEM[0]
	S += 10 < t20_mem0
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += alt(MAS_MEM)
	S += (t19*MAS[0])-1 < t20_mem1*MAS_MEM[0]
	S += (t19*MAS[1])-1 < t20_mem1*MAS_MEM[1]
	S += (t19*MAS[2])-1 < t20_mem1*MAS_MEM[2]
	S += (t19*MAS[3])-1 < t20_mem1*MAS_MEM[3]
	S += t20_mem1 <= t20

	t25_in = S.Task('t25_in', length=1, delay_cost=1)
	t25_in += alt(MM_in)
	t25 = S.Task('t25', length=5, delay_cost=1)
	t25 += alt(MM)
	S += t25>=t25_in

	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	t25_mem0 += alt(MAS_MEM)
	S += (t24*MAS[0])-1 < t25_mem0*MAS_MEM[0]
	S += (t24*MAS[1])-1 < t25_mem0*MAS_MEM[1]
	S += (t24*MAS[2])-1 < t25_mem0*MAS_MEM[2]
	S += (t24*MAS[3])-1 < t25_mem0*MAS_MEM[3]
	S += t25_mem0 <= t25

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	t25_mem1 += MAIN_MEM_r
	S += t25_mem1 <= t25

	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	t26_in += alt(MM_in)
	t26 = S.Task('t26', length=5, delay_cost=1)
	t26 += alt(MM)
	S += t26>=t26_in

	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	t26_mem0 += alt(MAS_MEM)
	S += (t24*MAS[0])-1 < t26_mem0*MAS_MEM[0]
	S += (t24*MAS[1])-1 < t26_mem0*MAS_MEM[1]
	S += (t24*MAS[2])-1 < t26_mem0*MAS_MEM[2]
	S += (t24*MAS[3])-1 < t26_mem0*MAS_MEM[3]
	S += t26_mem0 <= t26

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	t26_mem1 += MM_MEM[0]
	S += 8 < t26_mem1
	S += t26_mem1 <= t26

	t9 = S.Task('t9', length=1, delay_cost=1)
	t9 += alt(MAS)

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	t9_mem0 += alt(MM_MEM)
	S += (t7*MM[0])-1 < t9_mem0*MM_MEM[0]
	S += t9_mem0 <= t9

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	t9_mem1 += alt(MM_MEM)
	S += (t8*MM[0])-1 < t9_mem1*MM_MEM[0]
	S += t9_mem1 <= t9

	t17_in = S.Task('t17_in', length=1, delay_cost=1)
	t17_in += alt(MM_in)
	t17 = S.Task('t17', length=5, delay_cost=1)
	t17 += alt(MM)
	S += t17>=t17_in

	S += 0<t17

	t17_w = S.Task('t17_w', length=1, delay_cost=1)
	t17_w += alt(MAIN_MEM_w)
	S += t17 <= t17_w

	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	t17_mem0 += MAIN_MEM_r
	S += t17_mem0 <= t17

	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	t17_mem1 += alt(MAS_MEM)
	S += (t16*MAS[0])-1 < t17_mem1*MAS_MEM[0]
	S += (t16*MAS[1])-1 < t17_mem1*MAS_MEM[1]
	S += (t16*MAS[2])-1 < t17_mem1*MAS_MEM[2]
	S += (t16*MAS[3])-1 < t17_mem1*MAS_MEM[3]
	S += t17_mem1 <= t17

	t21 = S.Task('t21', length=1, delay_cost=1)
	t21 += alt(MAS)

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += alt(MAS_MEM)
	S += (t20*MAS[0])-1 < t21_mem0*MAS_MEM[0]
	S += (t20*MAS[1])-1 < t21_mem0*MAS_MEM[1]
	S += (t20*MAS[2])-1 < t21_mem0*MAS_MEM[2]
	S += (t20*MAS[3])-1 < t21_mem0*MAS_MEM[3]
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += alt(MM_MEM)
	S += (t15*MM[0])-1 < t21_mem1*MM_MEM[0]
	S += t21_mem1 <= t21

	t27 = S.Task('t27', length=1, delay_cost=1)
	t27 += alt(MAS)

	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	t27_mem0 += alt(MM_MEM)
	S += (t26*MM[0])-1 < t27_mem0*MM_MEM[0]
	S += t27_mem0 <= t27

	t10 = S.Task('t10', length=1, delay_cost=1)
	t10 += alt(MAS)

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += MM_MEM[0]
	S += 8 < t10_mem0
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += alt(MAS_MEM)
	S += (t9*MAS[0])-1 < t10_mem1*MAS_MEM[0]
	S += (t9*MAS[1])-1 < t10_mem1*MAS_MEM[1]
	S += (t9*MAS[2])-1 < t10_mem1*MAS_MEM[2]
	S += (t9*MAS[3])-1 < t10_mem1*MAS_MEM[3]
	S += t10_mem1 <= t10

	t11 = S.Task('t11', length=1, delay_cost=1)
	t11 += alt(MAS)

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += MM_MEM[0]
	S += 8 < t11_mem0
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += alt(MAS_MEM)
	S += (t9*MAS[0])-1 < t11_mem1*MAS_MEM[0]
	S += (t9*MAS[1])-1 < t11_mem1*MAS_MEM[1]
	S += (t9*MAS[2])-1 < t11_mem1*MAS_MEM[2]
	S += (t9*MAS[3])-1 < t11_mem1*MAS_MEM[3]
	S += t11_mem1 <= t11

	t22_in = S.Task('t22_in', length=1, delay_cost=1)
	t22_in += alt(MM_in)
	t22 = S.Task('t22', length=5, delay_cost=1)
	t22 += alt(MM)
	S += t22>=t22_in

	t22_mem0 = S.Task('t22_mem0', length=1, delay_cost=1)
	t22_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t22_mem0*MAS_MEM[0]
	S += (t21*MAS[1])-1 < t22_mem0*MAS_MEM[1]
	S += (t21*MAS[2])-1 < t22_mem0*MAS_MEM[2]
	S += (t21*MAS[3])-1 < t22_mem0*MAS_MEM[3]
	S += t22_mem0 <= t22

	t22_mem1 = S.Task('t22_mem1', length=1, delay_cost=1)
	t22_mem1 += MAIN_MEM_r
	S += t22_mem1 <= t22

	new_PZ = S.Task('new_PZ', length=1, delay_cost=1)
	new_PZ += alt(MAS)

	S += 5<new_PZ

	new_PZ_w = S.Task('new_PZ_w', length=1, delay_cost=1)
	new_PZ_w += alt(MAIN_MEM_w)
	S += new_PZ <= new_PZ_w

	new_PZ_mem0 = S.Task('new_PZ_mem0', length=1, delay_cost=1)
	new_PZ_mem0 += alt(MAS_MEM)
	S += (t27*MAS[0])-1 < new_PZ_mem0*MAS_MEM[0]
	S += (t27*MAS[1])-1 < new_PZ_mem0*MAS_MEM[1]
	S += (t27*MAS[2])-1 < new_PZ_mem0*MAS_MEM[2]
	S += (t27*MAS[3])-1 < new_PZ_mem0*MAS_MEM[3]
	S += new_PZ_mem0 <= new_PZ

	t12_in = S.Task('t12_in', length=1, delay_cost=1)
	t12_in += alt(MM_in)
	t12 = S.Task('t12', length=5, delay_cost=1)
	t12 += alt(MM)
	S += t12>=t12_in

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	t12_mem0 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t12_mem0*MAS_MEM[0]
	S += (t10*MAS[1])-1 < t12_mem0*MAS_MEM[1]
	S += (t10*MAS[2])-1 < t12_mem0*MAS_MEM[2]
	S += (t10*MAS[3])-1 < t12_mem0*MAS_MEM[3]
	S += t12_mem0 <= t12

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	t12_mem1 += alt(MAS_MEM)
	S += (t11*MAS[0])-1 < t12_mem1*MAS_MEM[0]
	S += (t11*MAS[1])-1 < t12_mem1*MAS_MEM[1]
	S += (t11*MAS[2])-1 < t12_mem1*MAS_MEM[2]
	S += (t11*MAS[3])-1 < t12_mem1*MAS_MEM[3]
	S += t12_mem1 <= t12

	t13_in = S.Task('t13_in', length=1, delay_cost=1)
	t13_in += alt(MM_in)
	t13 = S.Task('t13', length=5, delay_cost=1)
	t13 += alt(MM)
	S += t13>=t13_in

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	t13_mem0 += alt(MAS_MEM)
	S += (t4*MAS[0])-1 < t13_mem0*MAS_MEM[0]
	S += (t4*MAS[1])-1 < t13_mem0*MAS_MEM[1]
	S += (t4*MAS[2])-1 < t13_mem0*MAS_MEM[2]
	S += (t4*MAS[3])-1 < t13_mem0*MAS_MEM[3]
	S += t13_mem0 <= t13

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	t13_mem1 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t13_mem1*MAS_MEM[0]
	S += (t10*MAS[1])-1 < t13_mem1*MAS_MEM[1]
	S += (t10*MAS[2])-1 < t13_mem1*MAS_MEM[2]
	S += (t10*MAS[3])-1 < t13_mem1*MAS_MEM[3]
	S += t13_mem1 <= t13

	new_PY = S.Task('new_PY', length=1, delay_cost=1)
	new_PY += alt(MAS)

	S += 4<new_PY

	new_PY_w = S.Task('new_PY_w', length=1, delay_cost=1)
	new_PY_w += alt(MAIN_MEM_w)
	S += new_PY <= new_PY_w

	new_PY_mem0 = S.Task('new_PY_mem0', length=1, delay_cost=1)
	new_PY_mem0 += alt(MM_MEM)
	S += (t12*MM[0])-1 < new_PY_mem0*MM_MEM[0]
	S += new_PY_mem0 <= new_PY

	new_PY_mem1 = S.Task('new_PY_mem1', length=1, delay_cost=1)
	new_PY_mem1 += alt(MM_MEM)
	S += (t22*MM[0])-1 < new_PY_mem1*MM_MEM[0]
	S += new_PY_mem1 <= new_PY

	new_PX = S.Task('new_PX', length=1, delay_cost=1)
	new_PX += alt(MAS)

	S += 6<new_PX

	new_PX_w = S.Task('new_PX_w', length=1, delay_cost=1)
	new_PX_w += alt(MAIN_MEM_w)
	S += new_PX <= new_PX_w

	new_PX_mem0 = S.Task('new_PX_mem0', length=1, delay_cost=1)
	new_PX_mem0 += alt(MM_MEM)
	S += (t13*MM[0])-1 < new_PX_mem0*MM_MEM[0]
	S += new_PX_mem0 <= new_PX

	new_PX_mem1 = S.Task('new_PX_mem1', length=1, delay_cost=1)
	new_PX_mem1 += alt(MM_MEM)
	S += (t25*MM[0])-1 < new_PX_mem1*MM_MEM[0]
	S += new_PX_mem1 <= new_PX

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/EP_DBL_A_ANY/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

