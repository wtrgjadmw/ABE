from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 117
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	S += t5_in >= 0
	t5_in += MM_in[0]

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	S += t5_mem0 >= 0
	t5_mem0 += MAIN_MEM_r[0]

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	S += t5_mem1 >= 0
	t5_mem1 += MAIN_MEM_r[1]

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	S += t14_mem0 >= 1
	t14_mem0 += MAIN_MEM_r[0]

	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	S += t2_in >= 1
	t2_in += MM_in[0]

	t5 = S.Task('t5', length=5, delay_cost=1)
	S += t5 >= 1
	t5 += MM[0]

	t2 = S.Task('t2', length=5, delay_cost=1)
	S += t2 >= 2
	t2 += MM[0]

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	S += t25_mem1 >= 2
	t25_mem1 += MAIN_MEM_r[1]

	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	S += t0_in >= 3
	t0_in += MM_in[0]

	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	S += t15_mem0 >= 3
	t15_mem0 += MAIN_MEM_r[0]

	t22_mem1 = S.Task('t22_mem1', length=1, delay_cost=1)
	S += t22_mem1 >= 3
	t22_mem1 += MAIN_MEM_r[1]

	t0 = S.Task('t0', length=5, delay_cost=1)
	S += t0 >= 4
	t0 += MM[0]

	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	S += t1_in >= 4
	t1_in += MM_in[0]

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	S += t2_mem0 >= 4
	t2_mem0 += MAIN_MEM_r[0]

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 4
	t3_mem1 += MAIN_MEM_r[1]

	t1 = S.Task('t1', length=5, delay_cost=1)
	S += t1 >= 5
	t1 += MM[0]

	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	S += t3_in >= 5
	t3_in += MM_in[0]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 5
	t3_mem0 += MAIN_MEM_r[0]

	t6_in = S.Task('t6_in', length=1, delay_cost=1)
	S += t6_in >= 5
	t6_in += MAS_in[2]

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	S += t6_mem0 >= 5
	t6_mem0 += MM_MEM[0]

	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	S += t15_in >= 6
	t15_in += MM_in[0]

	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	S += t15_mem1 >= 6
	t15_mem1 += MM_MEM[1]

	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	S += t17_mem0 >= 6
	t17_mem0 += MAIN_MEM_r[0]

	t3 = S.Task('t3', length=5, delay_cost=1)
	S += t3 >= 6
	t3 += MM[0]

	t6 = S.Task('t6', length=2, delay_cost=1)
	S += t6 >= 6
	t6 += MAS[2]

	t15 = S.Task('t15', length=5, delay_cost=1)
	S += t15 >= 7
	t15 += MM[0]

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	S += t1_mem0 >= 7
	t1_mem0 += MAIN_MEM_r[0]

	t24_in = S.Task('t24_in', length=1, delay_cost=1)
	S += t24_in >= 7
	t24_in += MAS_in[0]

	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	S += t24_mem0 >= 7
	t24_mem0 += MM_MEM[0]

	t19_in = S.Task('t19_in', length=1, delay_cost=1)
	S += t19_in >= 8
	t19_in += MAS_in[0]

	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	S += t19_mem0 >= 8
	t19_mem0 += MM_MEM[0]

	t24 = S.Task('t24', length=2, delay_cost=1)
	S += t24 >= 8
	t24 += MAS[0]

	t8_in = S.Task('t8_in', length=1, delay_cost=1)
	S += t8_in >= 8
	t8_in += MM_in[0]

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	S += t8_mem0 >= 8
	t8_mem0 += MAIN_MEM_r[0]

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	S += t8_mem1 >= 8
	t8_mem1 += MM_MEM[1]

	t19 = S.Task('t19', length=2, delay_cost=1)
	S += t19 >= 9
	t19 += MAS[0]

	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	S += t26_in >= 9
	t26_in += MM_in[0]

	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	S += t26_mem0 >= 9
	t26_mem0 += MAS_MEM[0]

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	S += t26_mem1 >= 9
	t26_mem1 += MM_MEM[1]

	t8 = S.Task('t8', length=5, delay_cost=1)
	S += t8 >= 9
	t8 += MM[0]

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	S += t0_mem0 >= 10
	t0_mem0 += MAIN_MEM_r[0]

	t14_in = S.Task('t14_in', length=1, delay_cost=1)
	S += t14_in >= 10
	t14_in += MM_in[0]

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	S += t14_mem1 >= 10
	t14_mem1 += MAS_MEM[5]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 10
	t20_in += MAS_in[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 10
	t20_mem0 += MM_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 10
	t20_mem1 += MAS_MEM[1]

	t26 = S.Task('t26', length=5, delay_cost=1)
	S += t26 >= 10
	t26 += MM[0]

	t14 = S.Task('t14', length=5, delay_cost=1)
	S += t14 >= 11
	t14 += MM[0]

	t16_in = S.Task('t16_in', length=1, delay_cost=1)
	S += t16_in >= 11
	t16_in += MAS_in[3]

	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	S += t16_mem0 >= 11
	t16_mem0 += MM_MEM[0]

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	S += t16_mem1 >= 11
	t16_mem1 += MM_MEM[1]

	t20 = S.Task('t20', length=2, delay_cost=1)
	S += t20 >= 11
	t20 += MAS[1]

	t25_in = S.Task('t25_in', length=1, delay_cost=1)
	S += t25_in >= 11
	t25_in += MM_in[0]

	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	S += t25_mem0 >= 11
	t25_mem0 += MAS_MEM[0]

	t16 = S.Task('t16', length=2, delay_cost=1)
	S += t16 >= 12
	t16 += MAS[3]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 12
	t21_in += MAS_in[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 12
	t21_mem0 += MAS_MEM[2]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 12
	t21_mem1 += MM_MEM[1]

	t25 = S.Task('t25', length=5, delay_cost=1)
	S += t25 >= 12
	t25 += MM[0]

	t4_in = S.Task('t4_in', length=1, delay_cost=1)
	S += t4_in >= 12
	t4_in += MAS_in[0]

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	S += t4_mem0 >= 12
	t4_mem0 += MM_MEM[0]

	t17_in = S.Task('t17_in', length=1, delay_cost=1)
	S += t17_in >= 13
	t17_in += MM_in[0]

	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	S += t17_mem1 >= 13
	t17_mem1 += MAS_MEM[7]

	t21 = S.Task('t21', length=2, delay_cost=1)
	S += t21 >= 13
	t21 += MAS[1]

	t4 = S.Task('t4', length=2, delay_cost=1)
	S += t4 >= 13
	t4 += MAS[0]

	t9_in = S.Task('t9_in', length=1, delay_cost=1)
	S += t9_in >= 13
	t9_in += MAS_in[3]

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	S += t9_mem0 >= 13
	t9_mem0 += MM_MEM[0]

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	S += t9_mem1 >= 13
	t9_mem1 += MM_MEM[1]

	t17 = S.Task('t17', length=5, delay_cost=1)
	S += t17 >= 14
	t17 += MM[0]

	t22_in = S.Task('t22_in', length=1, delay_cost=1)
	S += t22_in >= 14
	t22_in += MM_in[0]

	t22_mem0 = S.Task('t22_mem0', length=1, delay_cost=1)
	S += t22_mem0 >= 14
	t22_mem0 += MAS_MEM[2]

	t27_in = S.Task('t27_in', length=1, delay_cost=1)
	S += t27_in >= 14
	t27_in += MAS_in[3]

	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	S += t27_mem0 >= 14
	t27_mem0 += MM_MEM[0]

	t9 = S.Task('t9', length=2, delay_cost=1)
	S += t9 >= 14
	t9 += MAS[3]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 15
	t10_in += MAS_in[2]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 15
	t10_mem0 += MM_MEM[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 15
	t10_mem1 += MAS_MEM[7]

	t22 = S.Task('t22', length=5, delay_cost=1)
	S += t22 >= 15
	t22 += MM[0]

	t27 = S.Task('t27', length=2, delay_cost=1)
	S += t27 >= 15
	t27 += MAS[3]

	t10 = S.Task('t10', length=2, delay_cost=1)
	S += t10 >= 16
	t10 += MAS[2]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 16
	t11_in += MAS_in[3]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 16
	t11_mem0 += MM_MEM[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 16
	t11_mem1 += MAS_MEM[7]

	t14_w = S.Task('t14_w', length=1, delay_cost=1)
	S += t14_w >= 16
	t14_w += MAIN_MEM_w

	new_PZ_in = S.Task('new_PZ_in', length=1, delay_cost=1)
	S += new_PZ_in >= 17
	new_PZ_in += MAS_in[0]

	new_PZ_mem0 = S.Task('new_PZ_mem0', length=1, delay_cost=1)
	S += new_PZ_mem0 >= 17
	new_PZ_mem0 += MAS_MEM[6]

	t11 = S.Task('t11', length=2, delay_cost=1)
	S += t11 >= 17
	t11 += MAS[3]

	t13_in = S.Task('t13_in', length=1, delay_cost=1)
	S += t13_in >= 17
	t13_in += MM_in[0]

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	S += t13_mem0 >= 17
	t13_mem0 += MAS_MEM[0]

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	S += t13_mem1 >= 17
	t13_mem1 += MAS_MEM[5]

	new_PZ = S.Task('new_PZ', length=2, delay_cost=1)
	S += new_PZ >= 18
	new_PZ += MAS[0]

	t12_in = S.Task('t12_in', length=1, delay_cost=1)
	S += t12_in >= 18
	t12_in += MM_in[0]

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	S += t12_mem0 >= 18
	t12_mem0 += MAS_MEM[4]

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	S += t12_mem1 >= 18
	t12_mem1 += MAS_MEM[7]

	t13 = S.Task('t13', length=5, delay_cost=1)
	S += t13 >= 18
	t13 += MM[0]

	t12 = S.Task('t12', length=5, delay_cost=1)
	S += t12 >= 19
	t12 += MM[0]

	t17_w = S.Task('t17_w', length=1, delay_cost=1)
	S += t17_w >= 19
	t17_w += MAIN_MEM_w

	new_PZ_w = S.Task('new_PZ_w', length=1, delay_cost=1)
	S += new_PZ_w >= 20
	new_PZ_w += MAIN_MEM_w

	new_PX_in = S.Task('new_PX_in', length=1, delay_cost=1)
	S += new_PX_in >= 22
	new_PX_in += MAS_in[0]

	new_PX_mem0 = S.Task('new_PX_mem0', length=1, delay_cost=1)
	S += new_PX_mem0 >= 22
	new_PX_mem0 += MM_MEM[0]

	new_PX_mem1 = S.Task('new_PX_mem1', length=1, delay_cost=1)
	S += new_PX_mem1 >= 22
	new_PX_mem1 += MM_MEM[1]

	new_PX = S.Task('new_PX', length=2, delay_cost=1)
	S += new_PX >= 23
	new_PX += MAS[0]

	new_PY_in = S.Task('new_PY_in', length=1, delay_cost=1)
	S += new_PY_in >= 23
	new_PY_in += MAS_in[3]

	new_PY_mem0 = S.Task('new_PY_mem0', length=1, delay_cost=1)
	S += new_PY_mem0 >= 23
	new_PY_mem0 += MM_MEM[0]

	new_PY_mem1 = S.Task('new_PY_mem1', length=1, delay_cost=1)
	S += new_PY_mem1 >= 23
	new_PY_mem1 += MM_MEM[1]

	new_PY = S.Task('new_PY', length=2, delay_cost=1)
	S += new_PY >= 24
	new_PY += MAS[3]

	new_PX_w = S.Task('new_PX_w', length=1, delay_cost=1)
	S += new_PX_w >= 25
	new_PX_w += MAIN_MEM_w

	new_PY_w = S.Task('new_PY_w', length=1, delay_cost=1)
	S += new_PY_w >= 26
	new_PY_w += MAIN_MEM_w


	# new tasks
	t23 = S.Task('t23', length=5, delay_cost=1)
	t23 += alt(MM)
	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	t23_in += alt(MM_in)
	S += t23_in*MM_in[0]<=t23*MM[0]

	S += t23<8

	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	t23_mem0 += MAIN_MEM_r[0]
	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	t23_mem1 += MAIN_MEM_r[1]
	t7 = S.Task('t7', length=5, delay_cost=1)
	t7 += alt(MM)
	t7_in = S.Task('t7_in', length=1, delay_cost=1)
	t7_in += alt(MM_in)
	S += t7_in*MM_in[0]<=t7*MM[0]

	S += t7<14

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	t7_mem0 += MAIN_MEM_r[0]
	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	t7_mem1 += MAS_MEM[5]
	S += 7 < t7_mem1
	S += t7_mem1 <= t7

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage2MAS4/EP_DBL_A_ANY/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

