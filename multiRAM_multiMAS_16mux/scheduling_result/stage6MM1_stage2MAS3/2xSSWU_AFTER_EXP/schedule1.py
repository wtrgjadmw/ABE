from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 171
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=3)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=3, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=6)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	alpha1_in = S.Task('alpha1_in', length=1, delay_cost=1)
	S += alpha1_in >= 0
	alpha1_in += MM_in[0]

	alpha1_mem0 = S.Task('alpha1_mem0', length=1, delay_cost=1)
	S += alpha1_mem0 >= 0
	alpha1_mem0 += MAIN_MEM_r[0]

	alpha1_mem1 = S.Task('alpha1_mem1', length=1, delay_cost=1)
	S += alpha1_mem1 >= 0
	alpha1_mem1 += MAIN_MEM_r[1]

	alpha1 = S.Task('alpha1', length=6, delay_cost=1)
	S += alpha1 >= 1
	alpha1 += MM[0]

	xit2N1_in = S.Task('xit2N1_in', length=1, delay_cost=1)
	S += xit2N1_in >= 1
	xit2N1_in += MM_in[0]

	xit2N1_mem0 = S.Task('xit2N1_mem0', length=1, delay_cost=1)
	S += xit2N1_mem0 >= 1
	xit2N1_mem0 += MAIN_MEM_r[0]

	xit2N1_mem1 = S.Task('xit2N1_mem1', length=1, delay_cost=1)
	S += xit2N1_mem1 >= 1
	xit2N1_mem1 += MAIN_MEM_r[1]

	alpha0_in = S.Task('alpha0_in', length=1, delay_cost=1)
	S += alpha0_in >= 2
	alpha0_in += MM_in[0]

	alpha0_mem0 = S.Task('alpha0_mem0', length=1, delay_cost=1)
	S += alpha0_mem0 >= 2
	alpha0_mem0 += MAIN_MEM_r[0]

	alpha0_mem1 = S.Task('alpha0_mem1', length=1, delay_cost=1)
	S += alpha0_mem1 >= 2
	alpha0_mem1 += MAIN_MEM_r[1]

	xit2N1 = S.Task('xit2N1', length=6, delay_cost=1)
	S += xit2N1 >= 2
	xit2N1 += MM[0]

	alpha0 = S.Task('alpha0', length=6, delay_cost=1)
	S += alpha0 >= 3
	alpha0 += MM[0]

	xit2N0_in = S.Task('xit2N0_in', length=1, delay_cost=1)
	S += xit2N0_in >= 3
	xit2N0_in += MM_in[0]

	xit2N0_mem0 = S.Task('xit2N0_mem0', length=1, delay_cost=1)
	S += xit2N0_mem0 >= 3
	xit2N0_mem0 += MAIN_MEM_r[0]

	xit2N0_mem1 = S.Task('xit2N0_mem1', length=1, delay_cost=1)
	S += xit2N0_mem1 >= 3
	xit2N0_mem1 += MAIN_MEM_r[1]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 4
	t31_in += MM_in[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 4
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 4
	t31_mem1 += MAIN_MEM_r[1]

	xit2N0 = S.Task('xit2N0', length=6, delay_cost=1)
	S += xit2N0 >= 4
	xit2N0 += MM[0]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 5
	t30_in += MM_in[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 5
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 5
	t30_mem1 += MAIN_MEM_r[1]

	t31 = S.Task('t31', length=6, delay_cost=1)
	S += t31 >= 5
	t31 += MM[0]

	alphaD1_in = S.Task('alphaD1_in', length=1, delay_cost=1)
	S += alphaD1_in >= 6
	alphaD1_in += MM_in[0]

	alphaD1_mem0 = S.Task('alphaD1_mem0', length=1, delay_cost=1)
	S += alphaD1_mem0 >= 6
	alphaD1_mem0 += MM_MEM[0]

	alphaD1_mem1 = S.Task('alphaD1_mem1', length=1, delay_cost=1)
	S += alphaD1_mem1 >= 6
	alphaD1_mem1 += MAIN_MEM_r[1]

	t30 = S.Task('t30', length=6, delay_cost=1)
	S += t30 >= 6
	t30 += MM[0]

	alpha21_in = S.Task('alpha21_in', length=1, delay_cost=1)
	S += alpha21_in >= 7
	alpha21_in += MM_in[0]

	alpha21_mem0 = S.Task('alpha21_mem0', length=1, delay_cost=1)
	S += alpha21_mem0 >= 7
	alpha21_mem0 += MM_MEM[0]

	alpha21_mem1 = S.Task('alpha21_mem1', length=1, delay_cost=1)
	S += alpha21_mem1 >= 7
	alpha21_mem1 += MM_MEM[1]

	alphaD1 = S.Task('alphaD1', length=6, delay_cost=1)
	S += alphaD1 >= 7
	alphaD1 += MM[0]

	alpha21 = S.Task('alpha21', length=6, delay_cost=1)
	S += alpha21 >= 8
	alpha21 += MM[0]

	alphaD0_in = S.Task('alphaD0_in', length=1, delay_cost=1)
	S += alphaD0_in >= 8
	alphaD0_in += MM_in[0]

	alphaD0_mem0 = S.Task('alphaD0_mem0', length=1, delay_cost=1)
	S += alphaD0_mem0 >= 8
	alphaD0_mem0 += MM_MEM[0]

	alphaD0_mem1 = S.Task('alphaD0_mem1', length=1, delay_cost=1)
	S += alphaD0_mem1 >= 8
	alphaD0_mem1 += MAIN_MEM_r[1]

	xit2N1_w = S.Task('xit2N1_w', length=1, delay_cost=1)
	S += xit2N1_w >= 8
	xit2N1_w += MAIN_MEM_w

	alpha20_in = S.Task('alpha20_in', length=1, delay_cost=1)
	S += alpha20_in >= 9
	alpha20_in += MM_in[0]

	alpha20_mem0 = S.Task('alpha20_mem0', length=1, delay_cost=1)
	S += alpha20_mem0 >= 9
	alpha20_mem0 += MM_MEM[0]

	alpha20_mem1 = S.Task('alpha20_mem1', length=1, delay_cost=1)
	S += alpha20_mem1 >= 9
	alpha20_mem1 += MM_MEM[1]

	alphaD0 = S.Task('alphaD0', length=6, delay_cost=1)
	S += alphaD0 >= 9
	alphaD0 += MM[0]

	alpha20 = S.Task('alpha20', length=6, delay_cost=1)
	S += alpha20 >= 10
	alpha20 += MM[0]

	xit2N0_w = S.Task('xit2N0_w', length=1, delay_cost=1)
	S += xit2N0_w >= 10
	xit2N0_w += MAIN_MEM_w

	alpha2V1_in = S.Task('alpha2V1_in', length=1, delay_cost=1)
	S += alpha2V1_in >= 13
	alpha2V1_in += MM_in[0]

	alpha2V1_mem0 = S.Task('alpha2V1_mem0', length=1, delay_cost=1)
	S += alpha2V1_mem0 >= 13
	alpha2V1_mem0 += MM_MEM[0]

	alpha2V1_mem1 = S.Task('alpha2V1_mem1', length=1, delay_cost=1)
	S += alpha2V1_mem1 >= 13
	alpha2V1_mem1 += MAIN_MEM_r[1]

	alphaD1_w = S.Task('alphaD1_w', length=1, delay_cost=1)
	S += alphaD1_w >= 13
	alphaD1_w += MAIN_MEM_w

	alpha2V1 = S.Task('alpha2V1', length=6, delay_cost=1)
	S += alpha2V1 >= 14
	alpha2V1 += MM[0]

	t3alphaD1_in = S.Task('t3alphaD1_in', length=1, delay_cost=1)
	S += t3alphaD1_in >= 14
	t3alphaD1_in += MM_in[0]

	t3alphaD1_mem0 = S.Task('t3alphaD1_mem0', length=1, delay_cost=1)
	S += t3alphaD1_mem0 >= 14
	t3alphaD1_mem0 += MM_MEM[0]

	t3alphaD1_mem1 = S.Task('t3alphaD1_mem1', length=1, delay_cost=1)
	S += t3alphaD1_mem1 >= 14
	t3alphaD1_mem1 += MAIN_MEM_r[1]

	alpha2V0_in = S.Task('alpha2V0_in', length=1, delay_cost=1)
	S += alpha2V0_in >= 15
	alpha2V0_in += MM_in[0]

	alpha2V0_mem0 = S.Task('alpha2V0_mem0', length=1, delay_cost=1)
	S += alpha2V0_mem0 >= 15
	alpha2V0_mem0 += MM_MEM[0]

	alpha2V0_mem1 = S.Task('alpha2V0_mem1', length=1, delay_cost=1)
	S += alpha2V0_mem1 >= 15
	alpha2V0_mem1 += MAIN_MEM_r[1]

	alphaD0_w = S.Task('alphaD0_w', length=1, delay_cost=1)
	S += alphaD0_w >= 15
	alphaD0_w += MAIN_MEM_w

	t3alphaD1 = S.Task('t3alphaD1', length=6, delay_cost=1)
	S += t3alphaD1 >= 15
	t3alphaD1 += MM[0]

	alpha2V0 = S.Task('alpha2V0', length=6, delay_cost=1)
	S += alpha2V0 >= 16
	alpha2V0 += MM[0]

	t3alphaD0_in = S.Task('t3alphaD0_in', length=1, delay_cost=1)
	S += t3alphaD0_in >= 16
	t3alphaD0_in += MM_in[0]

	t3alphaD0_mem0 = S.Task('t3alphaD0_mem0', length=1, delay_cost=1)
	S += t3alphaD0_mem0 >= 16
	t3alphaD0_mem0 += MM_MEM[0]

	t3alphaD0_mem1 = S.Task('t3alphaD0_mem1', length=1, delay_cost=1)
	S += t3alphaD0_mem1 >= 16
	t3alphaD0_mem1 += MAIN_MEM_r[1]

	t3alphaD0 = S.Task('t3alphaD0', length=6, delay_cost=1)
	S += t3alphaD0 >= 17
	t3alphaD0 += MM[0]

	alpha2V_U1_in = S.Task('alpha2V_U1_in', length=1, delay_cost=1)
	S += alpha2V_U1_in >= 19
	alpha2V_U1_in += MAS_in[2]

	alpha2V_U1_mem0 = S.Task('alpha2V_U1_mem0', length=1, delay_cost=1)
	S += alpha2V_U1_mem0 >= 19
	alpha2V_U1_mem0 += MM_MEM[0]

	alpha2V_U1_mem1 = S.Task('alpha2V_U1_mem1', length=1, delay_cost=1)
	S += alpha2V_U1_mem1 >= 19
	alpha2V_U1_mem1 += MAIN_MEM_r[1]

	alpha2V_U1 = S.Task('alpha2V_U1', length=2, delay_cost=1)
	S += alpha2V_U1 >= 20
	alpha2V_U1 += MAS[2]

	y21_in = S.Task('y21_in', length=1, delay_cost=1)
	S += y21_in >= 20
	y21_in += MM_in[0]

	y21_mem0 = S.Task('y21_mem0', length=1, delay_cost=1)
	S += y21_mem0 >= 20
	y21_mem0 += MAIN_MEM_r[0]

	y21_mem1 = S.Task('y21_mem1', length=1, delay_cost=1)
	S += y21_mem1 >= 20
	y21_mem1 += MM_MEM[1]

	alpha2V_U0_in = S.Task('alpha2V_U0_in', length=1, delay_cost=1)
	S += alpha2V_U0_in >= 21
	alpha2V_U0_in += MAS_in[2]

	alpha2V_U0_mem0 = S.Task('alpha2V_U0_mem0', length=1, delay_cost=1)
	S += alpha2V_U0_mem0 >= 21
	alpha2V_U0_mem0 += MM_MEM[0]

	alpha2V_U0_mem1 = S.Task('alpha2V_U0_mem1', length=1, delay_cost=1)
	S += alpha2V_U0_mem1 >= 21
	alpha2V_U0_mem1 += MAIN_MEM_r[1]

	y21 = S.Task('y21', length=6, delay_cost=1)
	S += y21 >= 21
	y21 += MM[0]

	alpha2V_U0 = S.Task('alpha2V_U0', length=2, delay_cost=1)
	S += alpha2V_U0 >= 22
	alpha2V_U0 += MAS[2]

	alpha2V_U1_w = S.Task('alpha2V_U1_w', length=1, delay_cost=1)
	S += alpha2V_U1_w >= 22
	alpha2V_U1_w += MAIN_MEM_w

	y20_in = S.Task('y20_in', length=1, delay_cost=1)
	S += y20_in >= 22
	y20_in += MM_in[0]

	y20_mem0 = S.Task('y20_mem0', length=1, delay_cost=1)
	S += y20_mem0 >= 22
	y20_mem0 += MAIN_MEM_r[0]

	y20_mem1 = S.Task('y20_mem1', length=1, delay_cost=1)
	S += y20_mem1 >= 22
	y20_mem1 += MM_MEM[1]

	X_SSWU1_mem0 = S.Task('X_SSWU1_mem0', length=1, delay_cost=1)
	S += X_SSWU1_mem0 >= 23
	X_SSWU1_mem0 += MAIN_MEM_r[0]

	y20 = S.Task('y20', length=6, delay_cost=1)
	S += y20 >= 23
	y20 += MM[0]

	X_SSWU1_mem1 = S.Task('X_SSWU1_mem1', length=1, delay_cost=1)
	S += X_SSWU1_mem1 >= 24
	X_SSWU1_mem1 += MAIN_MEM_r[0]

	alpha2V_U0_w = S.Task('alpha2V_U0_w', length=1, delay_cost=1)
	S += alpha2V_U0_w >= 24
	alpha2V_U0_w += MAIN_MEM_w

	X_SSWU1_mem2 = S.Task('X_SSWU1_mem2', length=1, delay_cost=1)
	S += X_SSWU1_mem2 >= 25
	X_SSWU1_mem2 += MAIN_MEM_r[0]

	X_SSWU1 = S.Task('X_SSWU1', length=3, delay_cost=1)
	S += X_SSWU1 >= 26
	X_SSWU1 += CSEL

	y1_mem0 = S.Task('y1_mem0', length=1, delay_cost=1)
	S += y1_mem0 >= 27
	y1_mem0 += MAIN_MEM_r[0]

	y21_w = S.Task('y21_w', length=1, delay_cost=1)
	S += y21_w >= 27
	y21_w += MAIN_MEM_w

	y1_mem1 = S.Task('y1_mem1', length=1, delay_cost=1)
	S += y1_mem1 >= 28
	y1_mem1 += MAIN_MEM_r[0]

	y1_mem2 = S.Task('y1_mem2', length=1, delay_cost=1)
	S += y1_mem2 >= 29
	y1_mem2 += MAIN_MEM_r[0]

	y20_w = S.Task('y20_w', length=1, delay_cost=1)
	S += y20_w >= 29
	y20_w += MAIN_MEM_w

	y0_mem0 = S.Task('y0_mem0', length=1, delay_cost=1)
	S += y0_mem0 >= 30
	y0_mem0 += MAIN_MEM_r[0]

	y1 = S.Task('y1', length=3, delay_cost=1)
	S += y1 >= 30
	y1 += CSEL

	y0_mem1 = S.Task('y0_mem1', length=1, delay_cost=1)
	S += y0_mem1 >= 31
	y0_mem1 += MAIN_MEM_r[0]

	y0_mem2 = S.Task('y0_mem2', length=1, delay_cost=1)
	S += y0_mem2 >= 32
	y0_mem2 += MAIN_MEM_r[0]

	X_SSWU0_mem0 = S.Task('X_SSWU0_mem0', length=1, delay_cost=1)
	S += X_SSWU0_mem0 >= 33
	X_SSWU0_mem0 += MAIN_MEM_r[0]

	X_SSWU1_w = S.Task('X_SSWU1_w', length=1, delay_cost=1)
	S += X_SSWU1_w >= 33
	X_SSWU1_w += MAIN_MEM_w

	y0 = S.Task('y0', length=3, delay_cost=1)
	S += y0 >= 33
	y0 += CSEL

	X_SSWU0_mem1 = S.Task('X_SSWU0_mem1', length=1, delay_cost=1)
	S += X_SSWU0_mem1 >= 34
	X_SSWU0_mem1 += MAIN_MEM_r[0]

	X_SSWU0_mem2 = S.Task('X_SSWU0_mem2', length=1, delay_cost=1)
	S += X_SSWU0_mem2 >= 35
	X_SSWU0_mem2 += MAIN_MEM_r[0]

	X_SSWU0 = S.Task('X_SSWU0', length=3, delay_cost=1)
	S += X_SSWU0 >= 36
	X_SSWU0 += CSEL

	y1_w = S.Task('y1_w', length=1, delay_cost=1)
	S += y1_w >= 37
	y1_w += MAIN_MEM_w

	y_alt1_in = S.Task('y_alt1_in', length=1, delay_cost=1)
	S += y_alt1_in >= 38
	y_alt1_in += MAS_in[0]

	y_alt1_mem0 = S.Task('y_alt1_mem0', length=1, delay_cost=1)
	S += y_alt1_mem0 >= 38
	y_alt1_mem0 += MAIN_MEM_r[0]

	y_alt1_mem1 = S.Task('y_alt1_mem1', length=1, delay_cost=1)
	S += y_alt1_mem1 >= 38
	y_alt1_mem1 += MAIN_MEM_r[1]

	y_alt1 = S.Task('y_alt1', length=2, delay_cost=1)
	S += y_alt1 >= 39
	y_alt1 += MAS[0]

	Y_SSWU1_mem0 = S.Task('Y_SSWU1_mem0', length=1, delay_cost=1)
	S += Y_SSWU1_mem0 >= 40
	Y_SSWU1_mem0 += MAIN_MEM_r[0]

	y0_w = S.Task('y0_w', length=1, delay_cost=1)
	S += y0_w >= 40
	y0_w += MAIN_MEM_w

	Y_SSWU1_mem1 = S.Task('Y_SSWU1_mem1', length=1, delay_cost=1)
	S += Y_SSWU1_mem1 >= 41
	Y_SSWU1_mem1 += MAIN_MEM_r[0]

	y_alt1_w = S.Task('y_alt1_w', length=1, delay_cost=1)
	S += y_alt1_w >= 41
	y_alt1_w += MAIN_MEM_w

	Y_SSWU1_mem2 = S.Task('Y_SSWU1_mem2', length=1, delay_cost=1)
	S += Y_SSWU1_mem2 >= 42
	Y_SSWU1_mem2 += MAIN_MEM_r[0]

	X_SSWU0_w = S.Task('X_SSWU0_w', length=1, delay_cost=1)
	S += X_SSWU0_w >= 43
	X_SSWU0_w += MAIN_MEM_w

	Y_SSWU1 = S.Task('Y_SSWU1', length=3, delay_cost=1)
	S += Y_SSWU1 >= 43
	Y_SSWU1 += CSEL

	Y_SSWU1_w = S.Task('Y_SSWU1_w', length=1, delay_cost=1)
	S += Y_SSWU1_w >= 50
	Y_SSWU1_w += MAIN_MEM_w


	# new tasks
	y_alt0 = S.Task('y_alt0', length=2, delay_cost=1)
	y_alt0 += alt(MAS)
	y_alt0_in = S.Task('y_alt0_in', length=1, delay_cost=1)
	y_alt0_in += alt(MAS_in)
	S += y_alt0_in*MAS_in[0]<=y_alt0*MAS[0]

	S += y_alt0_in*MAS_in[1]<=y_alt0*MAS[1]

	S += y_alt0_in*MAS_in[2]<=y_alt0*MAS[2]

	S += 0<y_alt0

	y_alt0_w = S.Task('y_alt0_w', length=1, delay_cost=1)
	y_alt0_w += alt(MAIN_MEM_w)
	S += y_alt0 <= y_alt0_w

	S += y_alt0<1000

	y_alt0_mem0 = S.Task('y_alt0_mem0', length=1, delay_cost=1)
	y_alt0_mem0 += MAIN_MEM_r[0]
	S += y_alt0_mem0 <= y_alt0

	y_alt0_mem1 = S.Task('y_alt0_mem1', length=1, delay_cost=1)
	y_alt0_mem1 += MAIN_MEM_r[1]
	S += y0_w < y_alt0_mem1
	S += y_alt0_mem1 <= y_alt0

	Y_SSWU0 = S.Task('Y_SSWU0', length=3, delay_cost=1)
	Y_SSWU0 += alt(CSEL)

	Y_SSWU0_w = S.Task('Y_SSWU0_w', length=1, delay_cost=1)
	Y_SSWU0_w += alt(MAIN_MEM_w)
	S += Y_SSWU0+4 <= Y_SSWU0_w

	S += Y_SSWU0<1000

	Y_SSWU0_mem0 = S.Task('Y_SSWU0_mem0', length=1, delay_cost=1)
	Y_SSWU0_mem0 += MAIN_MEM_r[0]
	S += Y_SSWU0_mem0+ 2 <= Y_SSWU0

	Y_SSWU0_mem1 = S.Task('Y_SSWU0_mem1', length=1, delay_cost=1)
	Y_SSWU0_mem1 += MAIN_MEM_r[0]
	S += y0_w < Y_SSWU0_mem1
	S += Y_SSWU0_mem1+ 1 <= Y_SSWU0

	Y_SSWU0_mem2 = S.Task('Y_SSWU0_mem2', length=1, delay_cost=1)
	Y_SSWU0_mem2 += MAIN_MEM_r[0]
	S += y_alt0_w < Y_SSWU0_mem2
	S += Y_SSWU0_mem2+ 0 <= Y_SSWU0

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage2MAS3/2xSSWU_AFTER_EXP/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 4))

	return solution

