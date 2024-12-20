from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 166
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=5)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	alpha0_in = S.Task('alpha0_in', length=1, delay_cost=1)
	S += alpha0_in >= 0
	alpha0_in += MM_in[0]

	alpha0_mem0 = S.Task('alpha0_mem0', length=1, delay_cost=1)
	S += alpha0_mem0 >= 0
	alpha0_mem0 += MAIN_MEM_r[0]

	alpha0_mem1 = S.Task('alpha0_mem1', length=1, delay_cost=1)
	S += alpha0_mem1 >= 0
	alpha0_mem1 += MAIN_MEM_r[1]

	alpha0 = S.Task('alpha0', length=5, delay_cost=1)
	S += alpha0 >= 1
	alpha0 += MM[0]

	alpha1_in = S.Task('alpha1_in', length=1, delay_cost=1)
	S += alpha1_in >= 1
	alpha1_in += MM_in[1]

	alpha1_mem0 = S.Task('alpha1_mem0', length=1, delay_cost=1)
	S += alpha1_mem0 >= 1
	alpha1_mem0 += MAIN_MEM_r[0]

	alpha1_mem1 = S.Task('alpha1_mem1', length=1, delay_cost=1)
	S += alpha1_mem1 >= 1
	alpha1_mem1 += MAIN_MEM_r[1]

	alpha1 = S.Task('alpha1', length=5, delay_cost=1)
	S += alpha1 >= 2
	alpha1 += MM[1]

	xit2N1_in = S.Task('xit2N1_in', length=1, delay_cost=1)
	S += xit2N1_in >= 2
	xit2N1_in += MM_in[0]

	xit2N1_mem0 = S.Task('xit2N1_mem0', length=1, delay_cost=1)
	S += xit2N1_mem0 >= 2
	xit2N1_mem0 += MAIN_MEM_r[0]

	xit2N1_mem1 = S.Task('xit2N1_mem1', length=1, delay_cost=1)
	S += xit2N1_mem1 >= 2
	xit2N1_mem1 += MAIN_MEM_r[1]

	xit2N0_in = S.Task('xit2N0_in', length=1, delay_cost=1)
	S += xit2N0_in >= 3
	xit2N0_in += MM_in[1]

	xit2N0_mem0 = S.Task('xit2N0_mem0', length=1, delay_cost=1)
	S += xit2N0_mem0 >= 3
	xit2N0_mem0 += MAIN_MEM_r[0]

	xit2N0_mem1 = S.Task('xit2N0_mem1', length=1, delay_cost=1)
	S += xit2N0_mem1 >= 3
	xit2N0_mem1 += MAIN_MEM_r[1]

	xit2N1 = S.Task('xit2N1', length=5, delay_cost=1)
	S += xit2N1 >= 3
	xit2N1 += MM[0]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 4
	t30_in += MM_in[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 4
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 4
	t30_mem1 += MAIN_MEM_r[1]

	xit2N0 = S.Task('xit2N0', length=5, delay_cost=1)
	S += xit2N0 >= 4
	xit2N0 += MM[1]

	alpha20_in = S.Task('alpha20_in', length=1, delay_cost=1)
	S += alpha20_in >= 5
	alpha20_in += MM_in[0]

	alpha20_mem0 = S.Task('alpha20_mem0', length=1, delay_cost=1)
	S += alpha20_mem0 >= 5
	alpha20_mem0 += MM_MEM[0]

	alpha20_mem1 = S.Task('alpha20_mem1', length=1, delay_cost=1)
	S += alpha20_mem1 >= 5
	alpha20_mem1 += MM_MEM[1]

	t30 = S.Task('t30', length=5, delay_cost=1)
	S += t30 >= 5
	t30 += MM[1]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 5
	t31_in += MM_in[1]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 5
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 5
	t31_mem1 += MAIN_MEM_r[1]

	alpha20 = S.Task('alpha20', length=5, delay_cost=1)
	S += alpha20 >= 6
	alpha20 += MM[0]

	alpha21_in = S.Task('alpha21_in', length=1, delay_cost=1)
	S += alpha21_in >= 6
	alpha21_in += MM_in[0]

	alpha21_mem0 = S.Task('alpha21_mem0', length=1, delay_cost=1)
	S += alpha21_mem0 >= 6
	alpha21_mem0 += MM_MEM[2]

	alpha21_mem1 = S.Task('alpha21_mem1', length=1, delay_cost=1)
	S += alpha21_mem1 >= 6
	alpha21_mem1 += MM_MEM[3]

	alphaD0_in = S.Task('alphaD0_in', length=1, delay_cost=1)
	S += alphaD0_in >= 6
	alphaD0_in += MM_in[1]

	alphaD0_mem0 = S.Task('alphaD0_mem0', length=1, delay_cost=1)
	S += alphaD0_mem0 >= 6
	alphaD0_mem0 += MM_MEM[0]

	alphaD0_mem1 = S.Task('alphaD0_mem1', length=1, delay_cost=1)
	S += alphaD0_mem1 >= 6
	alphaD0_mem1 += MAIN_MEM_r[1]

	t31 = S.Task('t31', length=5, delay_cost=1)
	S += t31 >= 6
	t31 += MM[1]

	alpha21 = S.Task('alpha21', length=5, delay_cost=1)
	S += alpha21 >= 7
	alpha21 += MM[0]

	alphaD0 = S.Task('alphaD0', length=5, delay_cost=1)
	S += alphaD0 >= 7
	alphaD0 += MM[1]

	alphaD1_in = S.Task('alphaD1_in', length=1, delay_cost=1)
	S += alphaD1_in >= 7
	alphaD1_in += MM_in[0]

	alphaD1_mem0 = S.Task('alphaD1_mem0', length=1, delay_cost=1)
	S += alphaD1_mem0 >= 7
	alphaD1_mem0 += MM_MEM[2]

	alphaD1_mem1 = S.Task('alphaD1_mem1', length=1, delay_cost=1)
	S += alphaD1_mem1 >= 7
	alphaD1_mem1 += MAIN_MEM_r[1]

	alphaD1 = S.Task('alphaD1', length=5, delay_cost=1)
	S += alphaD1 >= 8
	alphaD1 += MM[0]

	xit2N1_w = S.Task('xit2N1_w', length=1, delay_cost=1)
	S += xit2N1_w >= 8
	xit2N1_w += MAIN_MEM_w

	xit2N0_w = S.Task('xit2N0_w', length=1, delay_cost=1)
	S += xit2N0_w >= 9
	xit2N0_w += MAIN_MEM_w

	alpha2V0_in = S.Task('alpha2V0_in', length=1, delay_cost=1)
	S += alpha2V0_in >= 10
	alpha2V0_in += MM_in[1]

	alpha2V0_mem0 = S.Task('alpha2V0_mem0', length=1, delay_cost=1)
	S += alpha2V0_mem0 >= 10
	alpha2V0_mem0 += MM_MEM[0]

	alpha2V0_mem1 = S.Task('alpha2V0_mem1', length=1, delay_cost=1)
	S += alpha2V0_mem1 >= 10
	alpha2V0_mem1 += MAIN_MEM_r[1]

	alpha2V0 = S.Task('alpha2V0', length=5, delay_cost=1)
	S += alpha2V0 >= 11
	alpha2V0 += MM[1]

	alpha2V1_in = S.Task('alpha2V1_in', length=1, delay_cost=1)
	S += alpha2V1_in >= 11
	alpha2V1_in += MM_in[1]

	alpha2V1_mem0 = S.Task('alpha2V1_mem0', length=1, delay_cost=1)
	S += alpha2V1_mem0 >= 11
	alpha2V1_mem0 += MM_MEM[0]

	alpha2V1_mem1 = S.Task('alpha2V1_mem1', length=1, delay_cost=1)
	S += alpha2V1_mem1 >= 11
	alpha2V1_mem1 += MAIN_MEM_r[1]

	t3alphaD0_in = S.Task('t3alphaD0_in', length=1, delay_cost=1)
	S += t3alphaD0_in >= 11
	t3alphaD0_in += MM_in[0]

	t3alphaD0_mem0 = S.Task('t3alphaD0_mem0', length=1, delay_cost=1)
	S += t3alphaD0_mem0 >= 11
	t3alphaD0_mem0 += MM_MEM[2]

	t3alphaD0_mem1 = S.Task('t3alphaD0_mem1', length=1, delay_cost=1)
	S += t3alphaD0_mem1 >= 11
	t3alphaD0_mem1 += MM_MEM[3]

	alpha2V1 = S.Task('alpha2V1', length=5, delay_cost=1)
	S += alpha2V1 >= 12
	alpha2V1 += MM[1]

	alphaD0_w = S.Task('alphaD0_w', length=1, delay_cost=1)
	S += alphaD0_w >= 12
	alphaD0_w += MAIN_MEM_w

	t3alphaD0 = S.Task('t3alphaD0', length=5, delay_cost=1)
	S += t3alphaD0 >= 12
	t3alphaD0 += MM[0]

	t3alphaD1_in = S.Task('t3alphaD1_in', length=1, delay_cost=1)
	S += t3alphaD1_in >= 12
	t3alphaD1_in += MM_in[1]

	t3alphaD1_mem0 = S.Task('t3alphaD1_mem0', length=1, delay_cost=1)
	S += t3alphaD1_mem0 >= 12
	t3alphaD1_mem0 += MM_MEM[2]

	t3alphaD1_mem1 = S.Task('t3alphaD1_mem1', length=1, delay_cost=1)
	S += t3alphaD1_mem1 >= 12
	t3alphaD1_mem1 += MM_MEM[1]

	alphaD1_w = S.Task('alphaD1_w', length=1, delay_cost=1)
	S += alphaD1_w >= 13
	alphaD1_w += MAIN_MEM_w

	t3alphaD1 = S.Task('t3alphaD1', length=5, delay_cost=1)
	S += t3alphaD1 >= 13
	t3alphaD1 += MM[1]

	alpha2V_U0_mem0 = S.Task('alpha2V_U0_mem0', length=1, delay_cost=1)
	S += alpha2V_U0_mem0 >= 15
	alpha2V_U0_mem0 += MM_MEM[2]

	alpha2V_U0_mem1 = S.Task('alpha2V_U0_mem1', length=1, delay_cost=1)
	S += alpha2V_U0_mem1 >= 15
	alpha2V_U0_mem1 += MAIN_MEM_r[1]

	alpha2V_U0 = S.Task('alpha2V_U0', length=1, delay_cost=1)
	S += alpha2V_U0 >= 16
	alpha2V_U0 += MAS[1]

	alpha2V_U1_mem0 = S.Task('alpha2V_U1_mem0', length=1, delay_cost=1)
	S += alpha2V_U1_mem0 >= 16
	alpha2V_U1_mem0 += MM_MEM[2]

	alpha2V_U1_mem1 = S.Task('alpha2V_U1_mem1', length=1, delay_cost=1)
	S += alpha2V_U1_mem1 >= 16
	alpha2V_U1_mem1 += MAIN_MEM_r[1]

	y20_in = S.Task('y20_in', length=1, delay_cost=1)
	S += y20_in >= 16
	y20_in += MM_in[0]

	y20_mem0 = S.Task('y20_mem0', length=1, delay_cost=1)
	S += y20_mem0 >= 16
	y20_mem0 += MAIN_MEM_r[0]

	y20_mem1 = S.Task('y20_mem1', length=1, delay_cost=1)
	S += y20_mem1 >= 16
	y20_mem1 += MM_MEM[1]

	alpha2V_U0_w = S.Task('alpha2V_U0_w', length=1, delay_cost=1)
	S += alpha2V_U0_w >= 17
	alpha2V_U0_w += MAIN_MEM_w

	alpha2V_U1 = S.Task('alpha2V_U1', length=1, delay_cost=1)
	S += alpha2V_U1 >= 17
	alpha2V_U1 += MAS[3]

	y20 = S.Task('y20', length=5, delay_cost=1)
	S += y20 >= 17
	y20 += MM[0]

	y21_in = S.Task('y21_in', length=1, delay_cost=1)
	S += y21_in >= 17
	y21_in += MM_in[1]

	y21_mem0 = S.Task('y21_mem0', length=1, delay_cost=1)
	S += y21_mem0 >= 17
	y21_mem0 += MAIN_MEM_r[0]

	y21_mem1 = S.Task('y21_mem1', length=1, delay_cost=1)
	S += y21_mem1 >= 17
	y21_mem1 += MM_MEM[3]

	X0_mem0 = S.Task('X0_mem0', length=1, delay_cost=1)
	S += X0_mem0 >= 18
	X0_mem0 += MAIN_MEM_r[0]

	alpha2V_U1_w = S.Task('alpha2V_U1_w', length=1, delay_cost=1)
	S += alpha2V_U1_w >= 18
	alpha2V_U1_w += MAIN_MEM_w

	y21 = S.Task('y21', length=5, delay_cost=1)
	S += y21 >= 18
	y21 += MM[1]

	X0_mem1 = S.Task('X0_mem1', length=1, delay_cost=1)
	S += X0_mem1 >= 19
	X0_mem1 += MAIN_MEM_r[0]

	X0_mem2 = S.Task('X0_mem2', length=1, delay_cost=1)
	S += X0_mem2 >= 20
	X0_mem2 += MAIN_MEM_r[0]

	X0 = S.Task('X0', length=3, delay_cost=1)
	S += X0 >= 21
	X0 += CSEL

	y0_mem0 = S.Task('y0_mem0', length=1, delay_cost=1)
	S += y0_mem0 >= 22
	y0_mem0 += MAIN_MEM_r[0]

	y20_w = S.Task('y20_w', length=1, delay_cost=1)
	S += y20_w >= 22
	y20_w += MAIN_MEM_w

	y0_mem1 = S.Task('y0_mem1', length=1, delay_cost=1)
	S += y0_mem1 >= 23
	y0_mem1 += MAIN_MEM_r[0]

	y21_w = S.Task('y21_w', length=1, delay_cost=1)
	S += y21_w >= 23
	y21_w += MAIN_MEM_w

	y0_mem2 = S.Task('y0_mem2', length=1, delay_cost=1)
	S += y0_mem2 >= 24
	y0_mem2 += MAIN_MEM_r[0]

	y0 = S.Task('y0', length=3, delay_cost=1)
	S += y0 >= 25
	y0 += CSEL

	X0_w = S.Task('X0_w', length=1, delay_cost=1)
	S += X0_w >= 26
	X0_w += MAIN_MEM_w

	y0_w = S.Task('y0_w', length=1, delay_cost=1)
	S += y0_w >= 30
	y0_w += MAIN_MEM_w

	y_alt0_mem0 = S.Task('y_alt0_mem0', length=1, delay_cost=1)
	S += y_alt0_mem0 >= 32
	y_alt0_mem0 += MAIN_MEM_r[0]

	y_alt0_mem1 = S.Task('y_alt0_mem1', length=1, delay_cost=1)
	S += y_alt0_mem1 >= 32
	y_alt0_mem1 += MAIN_MEM_r[1]

	Y0_mem0 = S.Task('Y0_mem0', length=1, delay_cost=1)
	S += Y0_mem0 >= 33
	Y0_mem0 += MAIN_MEM_r[0]

	y_alt0 = S.Task('y_alt0', length=1, delay_cost=1)
	S += y_alt0 >= 33
	y_alt0 += MAS[1]

	Y0_mem1 = S.Task('Y0_mem1', length=1, delay_cost=1)
	S += Y0_mem1 >= 34
	Y0_mem1 += MAIN_MEM_r[0]

	y_alt0_w = S.Task('y_alt0_w', length=1, delay_cost=1)
	S += y_alt0_w >= 34
	y_alt0_w += MAIN_MEM_w

	Y0_mem2 = S.Task('Y0_mem2', length=1, delay_cost=1)
	S += Y0_mem2 >= 35
	Y0_mem2 += MAIN_MEM_r[0]

	Y0 = S.Task('Y0', length=3, delay_cost=1)
	S += Y0 >= 36
	Y0 += CSEL

	y_alt1_mem0 = S.Task('y_alt1_mem0', length=1, delay_cost=1)
	S += y_alt1_mem0 >= 36
	y_alt1_mem0 += MAIN_MEM_r[0]

	y_alt1_mem1 = S.Task('y_alt1_mem1', length=1, delay_cost=1)
	S += y_alt1_mem1 >= 36
	y_alt1_mem1 += MAIN_MEM_r[1]

	Y1_mem0 = S.Task('Y1_mem0', length=1, delay_cost=1)
	S += Y1_mem0 >= 37
	Y1_mem0 += MAIN_MEM_r[0]

	y_alt1 = S.Task('y_alt1', length=1, delay_cost=1)
	S += y_alt1 >= 37
	y_alt1 += MAS[3]

	Y1_mem1 = S.Task('Y1_mem1', length=1, delay_cost=1)
	S += Y1_mem1 >= 38
	Y1_mem1 += MAIN_MEM_r[0]

	y_alt1_w = S.Task('y_alt1_w', length=1, delay_cost=1)
	S += y_alt1_w >= 38
	y_alt1_w += MAIN_MEM_w

	Y1_mem2 = S.Task('Y1_mem2', length=1, delay_cost=1)
	S += Y1_mem2 >= 39
	Y1_mem2 += MAIN_MEM_r[0]

	Y1 = S.Task('Y1', length=3, delay_cost=1)
	S += Y1 >= 40
	Y1 += CSEL

	Y0_w = S.Task('Y0_w', length=1, delay_cost=1)
	S += Y0_w >= 41
	Y0_w += MAIN_MEM_w

	Y1_w = S.Task('Y1_w', length=1, delay_cost=1)
	S += Y1_w >= 45
	Y1_w += MAIN_MEM_w


	# new tasks
	X1 = S.Task('X1', length=3, delay_cost=1)
	X1 += alt(CSEL)

	X1_w = S.Task('X1_w', length=1, delay_cost=1)
	X1_w += alt(MAIN_MEM_w)
	S += X1+2 <= X1_w

	S += X1<1000

	X1_mem0 = S.Task('X1_mem0', length=1, delay_cost=1)
	X1_mem0 += MAIN_MEM_r[0]
	S += alpha2V_U1_w < X1_mem0
	S += X1_mem0+ 2 <= X1

	X1_mem1 = S.Task('X1_mem1', length=1, delay_cost=1)
	X1_mem1 += MAIN_MEM_r[0]
	S += xit2N1_w < X1_mem1
	S += X1_mem1+ 1 <= X1

	X1_mem2 = S.Task('X1_mem2', length=1, delay_cost=1)
	X1_mem2 += MAIN_MEM_r[0]
	S += X1_mem2+ 0 <= X1

	y1 = S.Task('y1', length=3, delay_cost=1)
	y1 += alt(CSEL)

	y1_w = S.Task('y1_w', length=1, delay_cost=1)
	y1_w += alt(MAIN_MEM_w)
	S += y1+2 <= y1_w

	S += y1<37

	y1_mem0 = S.Task('y1_mem0', length=1, delay_cost=1)
	y1_mem0 += MAIN_MEM_r[0]
	S += alpha2V_U1_w < y1_mem0
	S += y1_mem0+ 2 <= y1

	y1_mem1 = S.Task('y1_mem1', length=1, delay_cost=1)
	y1_mem1 += MAIN_MEM_r[0]
	S += y21_w < y1_mem1
	S += y1_mem1+ 1 <= y1

	y1_mem2 = S.Task('y1_mem2', length=1, delay_cost=1)
	y1_mem2 += MAIN_MEM_r[0]
	S += alphaD1_w < y1_mem2
	S += y1_mem2+ 0 <= y1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM2_stage1MAS4/2xSSWU_AFTER_EXP/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

