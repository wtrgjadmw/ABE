from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	S += t0_mem0 >= 0
	t0_mem0 += MAIN_MEM_r[0]

	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	S += t5_in >= 0
	t5_in += MM_in[0]

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	S += t5_mem1 >= 0
	t5_mem1 += MAIN_MEM_r[1]

	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	S += t23_mem1 >= 1
	t23_mem1 += MAIN_MEM_r[1]

	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	S += t2_in >= 1
	t2_in += MM_in[0]

	t5 = S.Task('t5', length=5, delay_cost=1)
	S += t5 >= 1
	t5 += MM[0]

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	S += t8_mem0 >= 1
	t8_mem0 += MAIN_MEM_r[0]

	t2 = S.Task('t2', length=5, delay_cost=1)
	S += t2 >= 2
	t2 += MM[0]

	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	S += t23_in >= 2
	t23_in += MM_in[0]

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	S += t25_mem1 >= 2
	t25_mem1 += MAIN_MEM_r[1]

	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	S += t0_in >= 3
	t0_in += MM_in[0]

	t22_mem1 = S.Task('t22_mem1', length=1, delay_cost=1)
	S += t22_mem1 >= 3
	t22_mem1 += MAIN_MEM_r[1]

	t23 = S.Task('t23', length=5, delay_cost=1)
	S += t23 >= 3
	t23 += MM[0]

	t0 = S.Task('t0', length=5, delay_cost=1)
	S += t0 >= 4
	t0 += MM[0]

	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	S += t3_in >= 4
	t3_in += MM_in[0]

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 4
	t3_mem1 += MAIN_MEM_r[1]

	t3 = S.Task('t3', length=5, delay_cost=1)
	S += t3 >= 5
	t3 += MM[0]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 5
	t3_mem0 += MAIN_MEM_r[0]

	t6_in = S.Task('t6_in', length=1, delay_cost=1)
	S += t6_in >= 5
	t6_in += MAS_in[1]

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	S += t6_mem0 >= 5
	t6_mem0 += MM_MEM[0]

	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	S += t23_mem0 >= 6
	t23_mem0 += MAIN_MEM_r[0]

	t6 = S.Task('t6', length=3, delay_cost=1)
	S += t6 >= 6
	t6 += MAS[1]

	t24_in = S.Task('t24_in', length=1, delay_cost=1)
	S += t24_in >= 7
	t24_in += MAS_in[0]

	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	S += t24_mem0 >= 7
	t24_mem0 += MM_MEM[0]

	t8_in = S.Task('t8_in', length=1, delay_cost=1)
	S += t8_in >= 7
	t8_in += MM_in[0]

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	S += t8_mem1 >= 7
	t8_mem1 += MM_MEM[1]

	t24 = S.Task('t24', length=3, delay_cost=1)
	S += t24 >= 8
	t24 += MAS[0]

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	S += t2_mem0 >= 8
	t2_mem0 += MAIN_MEM_r[0]

	t7_in = S.Task('t7_in', length=1, delay_cost=1)
	S += t7_in >= 8
	t7_in += MM_in[0]

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	S += t7_mem1 >= 8
	t7_mem1 += MAS_MEM[3]

	t8 = S.Task('t8', length=5, delay_cost=1)
	S += t8 >= 8
	t8 += MM[0]

	t4_in = S.Task('t4_in', length=1, delay_cost=1)
	S += t4_in >= 9
	t4_in += MAS_in[0]

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	S += t4_mem0 >= 9
	t4_mem0 += MM_MEM[0]

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	S += t5_mem0 >= 9
	t5_mem0 += MAIN_MEM_r[0]

	t7 = S.Task('t7', length=5, delay_cost=1)
	S += t7 >= 9
	t7 += MM[0]

	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	S += t26_in >= 10
	t26_in += MM_in[0]

	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	S += t26_mem0 >= 10
	t26_mem0 += MAS_MEM[0]

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	S += t26_mem1 >= 10
	t26_mem1 += MM_MEM[1]

	t4 = S.Task('t4', length=3, delay_cost=1)
	S += t4 >= 10
	t4 += MAS[0]

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	S += t7_mem0 >= 10
	t7_mem0 += MAIN_MEM_r[0]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 11
	t20_in += MAS_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 11
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 11
	t20_mem1 += MAS_MEM[3]

	t25_in = S.Task('t25_in', length=1, delay_cost=1)
	S += t25_in >= 11
	t25_in += MM_in[0]

	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	S += t25_mem0 >= 11
	t25_mem0 += MAS_MEM[0]

	t26 = S.Task('t26', length=5, delay_cost=1)
	S += t26 >= 11
	t26 += MM[0]

	t20 = S.Task('t20', length=3, delay_cost=1)
	S += t20 >= 12
	t20 += MAS[0]

	t25 = S.Task('t25', length=5, delay_cost=1)
	S += t25 >= 12
	t25 += MM[0]

	t9_in = S.Task('t9_in', length=1, delay_cost=1)
	S += t9_in >= 13
	t9_in += MAS_in[0]

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	S += t9_mem0 >= 13
	t9_mem0 += MM_MEM[0]

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	S += t9_mem1 >= 13
	t9_mem1 += MM_MEM[1]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 14
	t21_in += MAS_in[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 14
	t21_mem0 += MAS_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 14
	t21_mem1 += MM_MEM[1]

	t9 = S.Task('t9', length=3, delay_cost=1)
	S += t9 >= 14
	t9 += MAS[0]

	t21 = S.Task('t21', length=3, delay_cost=1)
	S += t21 >= 15
	t21 += MAS[0]

	t27_in = S.Task('t27_in', length=1, delay_cost=1)
	S += t27_in >= 15
	t27_in += MAS_in[3]

	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	S += t27_mem0 >= 15
	t27_mem0 += MM_MEM[0]

	t27 = S.Task('t27', length=3, delay_cost=1)
	S += t27 >= 16
	t27 += MAS[3]

	t22_in = S.Task('t22_in', length=1, delay_cost=1)
	S += t22_in >= 17
	t22_in += MM_in[0]

	t22_mem0 = S.Task('t22_mem0', length=1, delay_cost=1)
	S += t22_mem0 >= 17
	t22_mem0 += MAS_MEM[0]

	new_PZ_in = S.Task('new_PZ_in', length=1, delay_cost=1)
	S += new_PZ_in >= 18
	new_PZ_in += MAS_in[0]

	new_PZ_mem0 = S.Task('new_PZ_mem0', length=1, delay_cost=1)
	S += new_PZ_mem0 >= 18
	new_PZ_mem0 += MAS_MEM[6]

	t22 = S.Task('t22', length=5, delay_cost=1)
	S += t22 >= 18
	t22 += MM[0]

	new_PZ = S.Task('new_PZ', length=3, delay_cost=1)
	S += new_PZ >= 19
	new_PZ += MAS[0]

	new_PZ_w = S.Task('new_PZ_w', length=1, delay_cost=1)
	S += new_PZ_w >= 22
	new_PZ_w += MAIN_MEM_w

	new_PX_in = S.Task('new_PX_in', length=1, delay_cost=1)
	S += new_PX_in >= 24
	new_PX_in += MAS_in[0]

	new_PX_mem0 = S.Task('new_PX_mem0', length=1, delay_cost=1)
	S += new_PX_mem0 >= 24
	new_PX_mem0 += MM_MEM[0]

	new_PX_mem1 = S.Task('new_PX_mem1', length=1, delay_cost=1)
	S += new_PX_mem1 >= 24
	new_PX_mem1 += MM_MEM[1]

	new_PX = S.Task('new_PX', length=3, delay_cost=1)
	S += new_PX >= 25
	new_PX += MAS[0]

	new_PY_in = S.Task('new_PY_in', length=1, delay_cost=1)
	S += new_PY_in >= 25
	new_PY_in += MAS_in[0]

	new_PY_mem0 = S.Task('new_PY_mem0', length=1, delay_cost=1)
	S += new_PY_mem0 >= 25
	new_PY_mem0 += MM_MEM[0]

	new_PY_mem1 = S.Task('new_PY_mem1', length=1, delay_cost=1)
	S += new_PY_mem1 >= 25
	new_PY_mem1 += MM_MEM[1]

	new_PY = S.Task('new_PY', length=3, delay_cost=1)
	S += new_PY >= 26
	new_PY += MAS[0]

	new_PX_w = S.Task('new_PX_w', length=1, delay_cost=1)
	S += new_PX_w >= 28
	new_PX_w += MAIN_MEM_w

	new_PY_w = S.Task('new_PY_w', length=1, delay_cost=1)
	S += new_PY_w >= 29
	new_PY_w += MAIN_MEM_w


	# new tasks
	t1 = S.Task('t1', length=5, delay_cost=1)
	t1 += alt(MM)
	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	t1_in += alt(MM_in)
	S += t1_in*MM_in[0]<=t1*MM[0]

	S += t1<11

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	t1_mem0 += MAIN_MEM_r[0]
	t15 = S.Task('t15', length=5, delay_cost=1)
	t15 += alt(MM)
	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	t15_in += alt(MM_in)
	S += t15_in*MM_in[0]<=t15*MM[0]

	S += t15<13

	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	t15_mem0 += MAIN_MEM_r[0]
	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	t15_mem1 += MM_MEM[1]
	S += 6 < t15_mem1
	S += t15_mem1 <= t15

	t19 = S.Task('t19', length=3, delay_cost=1)
	t19 += alt(MAS)
	t19_in = S.Task('t19_in', length=1, delay_cost=1)
	t19_in += alt(MAS_in)
	S += t19_in*MAS_in[0]<=t19*MAS[0]

	S += t19_in*MAS_in[1]<=t19*MAS[1]

	S += t19_in*MAS_in[2]<=t19*MAS[2]

	S += t19_in*MAS_in[3]<=t19*MAS[3]

	S += t19<12

	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	t19_mem0 += MM_MEM[0]
	S += 8 < t19_mem0
	S += t19_mem0 <= t19

	t14 = S.Task('t14', length=5, delay_cost=1)
	t14 += alt(MM)
	t14_in = S.Task('t14_in', length=1, delay_cost=1)
	t14_in += alt(MM_in)
	S += t14_in*MM_in[0]<=t14*MM[0]

	S += 0<t14

	t14_w = S.Task('t14_w', length=1, delay_cost=1)
	t14_w += alt(MAIN_MEM_w)
	S += t14 <= t14_w

	S += t14<1000

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	t14_mem0 += MAIN_MEM_r[0]
	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	t14_mem1 += MAS_MEM[3]
	S += 8 < t14_mem1
	S += t14_mem1 <= t14

	t16 = S.Task('t16', length=3, delay_cost=1)
	t16 += alt(MAS)
	t16_in = S.Task('t16_in', length=1, delay_cost=1)
	t16_in += alt(MAS_in)
	S += t16_in*MAS_in[0]<=t16*MAS[0]

	S += t16_in*MAS_in[1]<=t16*MAS[1]

	S += t16_in*MAS_in[2]<=t16*MAS[2]

	S += t16_in*MAS_in[3]<=t16*MAS[3]

	S += t16<16

	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	t16_mem0 += MM_MEM[0]
	S += 8 < t16_mem0
	S += t16_mem0 <= t16

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	t16_mem1 += alt(MM_MEM)
	S += (t15*MM[0])-1 < t16_mem1*MM_MEM[1]
	S += t16_mem1 <= t16

	t17 = S.Task('t17', length=5, delay_cost=1)
	t17 += alt(MM)
	t17_in = S.Task('t17_in', length=1, delay_cost=1)
	t17_in += alt(MM_in)
	S += t17_in*MM_in[0]<=t17*MM[0]

	S += 0<t17

	t17_w = S.Task('t17_w', length=1, delay_cost=1)
	t17_w += alt(MAIN_MEM_w)
	S += t17 <= t17_w

	S += t17<1000

	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	t17_mem0 += MAIN_MEM_r[0]
	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	t17_mem1 += alt(MAS_MEM)
	S += (t16*MAS[0])-1 < t17_mem1*MAS_MEM[1]
	S += (t16*MAS[1])-1 < t17_mem1*MAS_MEM[3]
	S += (t16*MAS[2])-1 < t17_mem1*MAS_MEM[5]
	S += (t16*MAS[3])-1 < t17_mem1*MAS_MEM[7]
	S += t17_mem1 <= t17

	t10 = S.Task('t10', length=3, delay_cost=1)
	t10 += alt(MAS)
	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	t10_in += alt(MAS_in)
	S += t10_in*MAS_in[0]<=t10*MAS[0]

	S += t10_in*MAS_in[1]<=t10*MAS[1]

	S += t10_in*MAS_in[2]<=t10*MAS[2]

	S += t10_in*MAS_in[3]<=t10*MAS[3]

	S += t10<20

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += alt(MM_MEM)
	S += (t1*MM[0])-1 < t10_mem0*MM_MEM[0]
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += MAS_MEM[1]
	S += 16 < t10_mem1
	S += t10_mem1 <= t10

	t11 = S.Task('t11', length=3, delay_cost=1)
	t11 += alt(MAS)
	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	t11_in += alt(MAS_in)
	S += t11_in*MAS_in[0]<=t11*MAS[0]

	S += t11_in*MAS_in[1]<=t11*MAS[1]

	S += t11_in*MAS_in[2]<=t11*MAS[2]

	S += t11_in*MAS_in[3]<=t11*MAS[3]

	S += t11<21

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += alt(MM_MEM)
	S += (t1*MM[0])-1 < t11_mem0*MM_MEM[0]
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += MAS_MEM[1]
	S += 16 < t11_mem1
	S += t11_mem1 <= t11

	t12 = S.Task('t12', length=5, delay_cost=1)
	t12 += alt(MM)
	t12_in = S.Task('t12_in', length=1, delay_cost=1)
	t12_in += alt(MM_in)
	S += t12_in*MM_in[0]<=t12*MM[0]

	S += t12<26

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	t12_mem0 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t12_mem0*MAS_MEM[0]
	S += (t10*MAS[1])-1 < t12_mem0*MAS_MEM[2]
	S += (t10*MAS[2])-1 < t12_mem0*MAS_MEM[4]
	S += (t10*MAS[3])-1 < t12_mem0*MAS_MEM[6]
	S += t12_mem0 <= t12

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	t12_mem1 += alt(MAS_MEM)
	S += (t11*MAS[0])-1 < t12_mem1*MAS_MEM[1]
	S += (t11*MAS[1])-1 < t12_mem1*MAS_MEM[3]
	S += (t11*MAS[2])-1 < t12_mem1*MAS_MEM[5]
	S += (t11*MAS[3])-1 < t12_mem1*MAS_MEM[7]
	S += t12_mem1 <= t12

	t13 = S.Task('t13', length=5, delay_cost=1)
	t13 += alt(MM)
	t13_in = S.Task('t13_in', length=1, delay_cost=1)
	t13_in += alt(MM_in)
	S += t13_in*MM_in[0]<=t13*MM[0]

	S += t13<25

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	t13_mem0 += MAS_MEM[0]
	S += 12 < t13_mem0
	S += t13_mem0 <= t13

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	t13_mem1 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t13_mem1*MAS_MEM[1]
	S += (t10*MAS[1])-1 < t13_mem1*MAS_MEM[3]
	S += (t10*MAS[2])-1 < t13_mem1*MAS_MEM[5]
	S += (t10*MAS[3])-1 < t13_mem1*MAS_MEM[7]
	S += t13_mem1 <= t13

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage3MAS4/EP_DBL_A_ANY/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

