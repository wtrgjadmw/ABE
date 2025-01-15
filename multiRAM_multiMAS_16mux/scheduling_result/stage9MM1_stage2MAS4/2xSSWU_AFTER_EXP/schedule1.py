from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 187
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=9)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
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

	alpha0 = S.Task('alpha0', length=9, delay_cost=1)
	S += alpha0 >= 1
	alpha0 += MM[0]

	alpha1_in = S.Task('alpha1_in', length=1, delay_cost=1)
	S += alpha1_in >= 1
	alpha1_in += MM_in[0]

	alpha1_mem0 = S.Task('alpha1_mem0', length=1, delay_cost=1)
	S += alpha1_mem0 >= 1
	alpha1_mem0 += MAIN_MEM_r[0]

	alpha1_mem1 = S.Task('alpha1_mem1', length=1, delay_cost=1)
	S += alpha1_mem1 >= 1
	alpha1_mem1 += MAIN_MEM_r[1]

	alpha1 = S.Task('alpha1', length=9, delay_cost=1)
	S += alpha1 >= 2
	alpha1 += MM[0]

	xit2N0_in = S.Task('xit2N0_in', length=1, delay_cost=1)
	S += xit2N0_in >= 2
	xit2N0_in += MM_in[0]

	xit2N0_mem0 = S.Task('xit2N0_mem0', length=1, delay_cost=1)
	S += xit2N0_mem0 >= 2
	xit2N0_mem0 += MAIN_MEM_r[0]

	xit2N0_mem1 = S.Task('xit2N0_mem1', length=1, delay_cost=1)
	S += xit2N0_mem1 >= 2
	xit2N0_mem1 += MAIN_MEM_r[1]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 3
	t31_in += MM_in[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 3
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 3
	t31_mem1 += MAIN_MEM_r[1]

	xit2N0 = S.Task('xit2N0', length=9, delay_cost=1)
	S += xit2N0 >= 3
	xit2N0 += MM[0]

	t31 = S.Task('t31', length=9, delay_cost=1)
	S += t31 >= 4
	t31 += MM[0]

	xit2N1_in = S.Task('xit2N1_in', length=1, delay_cost=1)
	S += xit2N1_in >= 4
	xit2N1_in += MM_in[0]

	xit2N1_mem0 = S.Task('xit2N1_mem0', length=1, delay_cost=1)
	S += xit2N1_mem0 >= 4
	xit2N1_mem0 += MAIN_MEM_r[0]

	xit2N1_mem1 = S.Task('xit2N1_mem1', length=1, delay_cost=1)
	S += xit2N1_mem1 >= 4
	xit2N1_mem1 += MAIN_MEM_r[1]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 5
	t30_in += MM_in[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 5
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 5
	t30_mem1 += MAIN_MEM_r[1]

	xit2N1 = S.Task('xit2N1', length=9, delay_cost=1)
	S += xit2N1 >= 5
	xit2N1 += MM[0]

	t30 = S.Task('t30', length=9, delay_cost=1)
	S += t30 >= 6
	t30 += MM[0]

	alpha0_w = S.Task('alpha0_w', length=1, delay_cost=1)
	S += alpha0_w >= 10
	alpha0_w += MAIN_MEM_w

	alpha1_w = S.Task('alpha1_w', length=1, delay_cost=1)
	S += alpha1_w >= 11
	alpha1_w += MAIN_MEM_w

	alpha20_in = S.Task('alpha20_in', length=1, delay_cost=1)
	S += alpha20_in >= 11
	alpha20_in += MM_in[0]

	alpha20_mem0 = S.Task('alpha20_mem0', length=1, delay_cost=1)
	S += alpha20_mem0 >= 11
	alpha20_mem0 += MAIN_MEM_r[0]

	alpha20_mem1 = S.Task('alpha20_mem1', length=1, delay_cost=1)
	S += alpha20_mem1 >= 11
	alpha20_mem1 += MAIN_MEM_r[1]

	alpha20 = S.Task('alpha20', length=9, delay_cost=1)
	S += alpha20 >= 12
	alpha20 += MM[0]

	t3alpha1_in = S.Task('t3alpha1_in', length=1, delay_cost=1)
	S += t3alpha1_in >= 12
	t3alpha1_in += MM_in[0]

	t3alpha1_mem0 = S.Task('t3alpha1_mem0', length=1, delay_cost=1)
	S += t3alpha1_mem0 >= 12
	t3alpha1_mem0 += MM_MEM[0]

	t3alpha1_mem1 = S.Task('t3alpha1_mem1', length=1, delay_cost=1)
	S += t3alpha1_mem1 >= 12
	t3alpha1_mem1 += MAIN_MEM_r[1]

	xit2N0_w = S.Task('xit2N0_w', length=1, delay_cost=1)
	S += xit2N0_w >= 12
	xit2N0_w += MAIN_MEM_w

	alpha21_in = S.Task('alpha21_in', length=1, delay_cost=1)
	S += alpha21_in >= 13
	alpha21_in += MM_in[0]

	alpha21_mem0 = S.Task('alpha21_mem0', length=1, delay_cost=1)
	S += alpha21_mem0 >= 13
	alpha21_mem0 += MAIN_MEM_r[0]

	alpha21_mem1 = S.Task('alpha21_mem1', length=1, delay_cost=1)
	S += alpha21_mem1 >= 13
	alpha21_mem1 += MAIN_MEM_r[1]

	t3alpha1 = S.Task('t3alpha1', length=9, delay_cost=1)
	S += t3alpha1 >= 13
	t3alpha1 += MM[0]

	alpha21 = S.Task('alpha21', length=9, delay_cost=1)
	S += alpha21 >= 14
	alpha21 += MM[0]

	t3alpha0_in = S.Task('t3alpha0_in', length=1, delay_cost=1)
	S += t3alpha0_in >= 14
	t3alpha0_in += MM_in[0]

	t3alpha0_mem0 = S.Task('t3alpha0_mem0', length=1, delay_cost=1)
	S += t3alpha0_mem0 >= 14
	t3alpha0_mem0 += MM_MEM[0]

	t3alpha0_mem1 = S.Task('t3alpha0_mem1', length=1, delay_cost=1)
	S += t3alpha0_mem1 >= 14
	t3alpha0_mem1 += MAIN_MEM_r[1]

	xit2N1_w = S.Task('xit2N1_w', length=1, delay_cost=1)
	S += xit2N1_w >= 14
	xit2N1_w += MAIN_MEM_w

	t3alpha0 = S.Task('t3alpha0', length=9, delay_cost=1)
	S += t3alpha0 >= 15
	t3alpha0 += MM[0]

	alpha2V0_in = S.Task('alpha2V0_in', length=1, delay_cost=1)
	S += alpha2V0_in >= 20
	alpha2V0_in += MM_in[0]

	alpha2V0_mem0 = S.Task('alpha2V0_mem0', length=1, delay_cost=1)
	S += alpha2V0_mem0 >= 20
	alpha2V0_mem0 += MM_MEM[0]

	alpha2V0_mem1 = S.Task('alpha2V0_mem1', length=1, delay_cost=1)
	S += alpha2V0_mem1 >= 20
	alpha2V0_mem1 += MAIN_MEM_r[1]

	alpha2V0 = S.Task('alpha2V0', length=9, delay_cost=1)
	S += alpha2V0 >= 21
	alpha2V0 += MM[0]

	y21_in = S.Task('y21_in', length=1, delay_cost=1)
	S += y21_in >= 21
	y21_in += MM_in[0]

	y21_mem0 = S.Task('y21_mem0', length=1, delay_cost=1)
	S += y21_mem0 >= 21
	y21_mem0 += MAIN_MEM_r[0]

	y21_mem1 = S.Task('y21_mem1', length=1, delay_cost=1)
	S += y21_mem1 >= 21
	y21_mem1 += MM_MEM[1]

	alpha2V1_in = S.Task('alpha2V1_in', length=1, delay_cost=1)
	S += alpha2V1_in >= 22
	alpha2V1_in += MM_in[0]

	alpha2V1_mem0 = S.Task('alpha2V1_mem0', length=1, delay_cost=1)
	S += alpha2V1_mem0 >= 22
	alpha2V1_mem0 += MM_MEM[0]

	alpha2V1_mem1 = S.Task('alpha2V1_mem1', length=1, delay_cost=1)
	S += alpha2V1_mem1 >= 22
	alpha2V1_mem1 += MAIN_MEM_r[1]

	y21 = S.Task('y21', length=9, delay_cost=1)
	S += y21 >= 22
	y21 += MM[0]

	alpha2V1 = S.Task('alpha2V1', length=9, delay_cost=1)
	S += alpha2V1 >= 23
	alpha2V1 += MM[0]

	y20_in = S.Task('y20_in', length=1, delay_cost=1)
	S += y20_in >= 23
	y20_in += MM_in[0]

	y20_mem0 = S.Task('y20_mem0', length=1, delay_cost=1)
	S += y20_mem0 >= 23
	y20_mem0 += MAIN_MEM_r[0]

	y20_mem1 = S.Task('y20_mem1', length=1, delay_cost=1)
	S += y20_mem1 >= 23
	y20_mem1 += MM_MEM[1]

	y20 = S.Task('y20', length=9, delay_cost=1)
	S += y20 >= 24
	y20 += MM[0]

	alpha2V_U0_in = S.Task('alpha2V_U0_in', length=1, delay_cost=1)
	S += alpha2V_U0_in >= 29
	alpha2V_U0_in += MAS_in[3]

	alpha2V_U0_mem0 = S.Task('alpha2V_U0_mem0', length=1, delay_cost=1)
	S += alpha2V_U0_mem0 >= 29
	alpha2V_U0_mem0 += MM_MEM[0]

	alpha2V_U0_mem1 = S.Task('alpha2V_U0_mem1', length=1, delay_cost=1)
	S += alpha2V_U0_mem1 >= 29
	alpha2V_U0_mem1 += MAIN_MEM_r[1]

	alpha2V_U0 = S.Task('alpha2V_U0', length=2, delay_cost=1)
	S += alpha2V_U0 >= 30
	alpha2V_U0 += MAS[3]

	alpha2V_U1_in = S.Task('alpha2V_U1_in', length=1, delay_cost=1)
	S += alpha2V_U1_in >= 31
	alpha2V_U1_in += MAS_in[0]

	alpha2V_U1_mem0 = S.Task('alpha2V_U1_mem0', length=1, delay_cost=1)
	S += alpha2V_U1_mem0 >= 31
	alpha2V_U1_mem0 += MM_MEM[0]

	alpha2V_U1_mem1 = S.Task('alpha2V_U1_mem1', length=1, delay_cost=1)
	S += alpha2V_U1_mem1 >= 31
	alpha2V_U1_mem1 += MAIN_MEM_r[1]

	y21_w = S.Task('y21_w', length=1, delay_cost=1)
	S += y21_w >= 31
	y21_w += MAIN_MEM_w

	alpha2V_U0_w = S.Task('alpha2V_U0_w', length=1, delay_cost=1)
	S += alpha2V_U0_w >= 32
	alpha2V_U0_w += MAIN_MEM_w

	alpha2V_U1 = S.Task('alpha2V_U1', length=2, delay_cost=1)
	S += alpha2V_U1 >= 32
	alpha2V_U1 += MAS[0]

	y0_mem0 = S.Task('y0_mem0', length=1, delay_cost=1)
	S += y0_mem0 >= 33
	y0_mem0 += MAIN_MEM_r[0]

	y20_w = S.Task('y20_w', length=1, delay_cost=1)
	S += y20_w >= 33
	y20_w += MAIN_MEM_w

	alpha2V_U1_w = S.Task('alpha2V_U1_w', length=1, delay_cost=1)
	S += alpha2V_U1_w >= 34
	alpha2V_U1_w += MAIN_MEM_w

	y0 = S.Task('y0', length=3, delay_cost=1)
	S += y0 >= 34
	y0 += CSEL

	y0_mem1 = S.Task('y0_mem1', length=1, delay_cost=1)
	S += y0_mem1 >= 34
	y0_mem1 += MAIN_MEM_r[0]

	y0_mem2 = S.Task('y0_mem2', length=1, delay_cost=1)
	S += y0_mem2 >= 35
	y0_mem2 += MAIN_MEM_r[0]

	X_Hash1_mem0 = S.Task('X_Hash1_mem0', length=1, delay_cost=1)
	S += X_Hash1_mem0 >= 39
	X_Hash1_mem0 += MAIN_MEM_r[0]

	X_Hash1 = S.Task('X_Hash1', length=3, delay_cost=1)
	S += X_Hash1 >= 40
	X_Hash1 += CSEL

	X_Hash1_mem1 = S.Task('X_Hash1_mem1', length=1, delay_cost=1)
	S += X_Hash1_mem1 >= 40
	X_Hash1_mem1 += MAIN_MEM_r[0]

	X_Hash1_mem2 = S.Task('X_Hash1_mem2', length=1, delay_cost=1)
	S += X_Hash1_mem2 >= 41
	X_Hash1_mem2 += MAIN_MEM_r[0]

	y0_w = S.Task('y0_w', length=1, delay_cost=1)
	S += y0_w >= 41
	y0_w += MAIN_MEM_w

	X_Hash0_mem0 = S.Task('X_Hash0_mem0', length=1, delay_cost=1)
	S += X_Hash0_mem0 >= 43
	X_Hash0_mem0 += MAIN_MEM_r[0]

	X_Hash0 = S.Task('X_Hash0', length=3, delay_cost=1)
	S += X_Hash0 >= 44
	X_Hash0 += CSEL

	X_Hash0_mem1 = S.Task('X_Hash0_mem1', length=1, delay_cost=1)
	S += X_Hash0_mem1 >= 44
	X_Hash0_mem1 += MAIN_MEM_r[0]

	X_Hash0_mem2 = S.Task('X_Hash0_mem2', length=1, delay_cost=1)
	S += X_Hash0_mem2 >= 45
	X_Hash0_mem2 += MAIN_MEM_r[0]

	X_Hash1_w = S.Task('X_Hash1_w', length=1, delay_cost=1)
	S += X_Hash1_w >= 47
	X_Hash1_w += MAIN_MEM_w

	Y_0_mem0 = S.Task('Y_0_mem0', length=1, delay_cost=1)
	S += Y_0_mem0 >= 47
	Y_0_mem0 += MAIN_MEM_r[0]

	Y_0 = S.Task('Y_0', length=3, delay_cost=1)
	S += Y_0 >= 48
	Y_0 += CSEL

	Y_0_mem1 = S.Task('Y_0_mem1', length=1, delay_cost=1)
	S += Y_0_mem1 >= 48
	Y_0_mem1 += MAIN_MEM_r[0]

	Y_0_mem2 = S.Task('Y_0_mem2', length=1, delay_cost=1)
	S += Y_0_mem2 >= 49
	Y_0_mem2 += MAIN_MEM_r[0]

	X_Hash0_w = S.Task('X_Hash0_w', length=1, delay_cost=1)
	S += X_Hash0_w >= 51
	X_Hash0_w += MAIN_MEM_w

	Y_0_w = S.Task('Y_0_w', length=1, delay_cost=1)
	S += Y_0_w >= 55
	Y_0_w += MAIN_MEM_w

	Y_Hash0_in = S.Task('Y_Hash0_in', length=1, delay_cost=1)
	S += Y_Hash0_in >= 56
	Y_Hash0_in += MM_in[0]

	Y_Hash0_mem0 = S.Task('Y_Hash0_mem0', length=1, delay_cost=1)
	S += Y_Hash0_mem0 >= 56
	Y_Hash0_mem0 += MAIN_MEM_r[0]

	Y_Hash0_mem1 = S.Task('Y_Hash0_mem1', length=1, delay_cost=1)
	S += Y_Hash0_mem1 >= 56
	Y_Hash0_mem1 += MAIN_MEM_r[1]

	Y_Hash0 = S.Task('Y_Hash0', length=9, delay_cost=1)
	S += Y_Hash0 >= 57
	Y_Hash0 += MM[0]

	Y_Hash0_w = S.Task('Y_Hash0_w', length=1, delay_cost=1)
	S += Y_Hash0_w >= 66
	Y_Hash0_w += MAIN_MEM_w


	# new tasks
	y1 = S.Task('y1', length=3, delay_cost=1)
	y1 += alt(CSEL)

	y1_w = S.Task('y1_w', length=1, delay_cost=1)
	y1_w += alt(MAIN_MEM_w)
	S += y1+4 <= y1_w

	S += y1<1000

	y1_mem0 = S.Task('y1_mem0', length=1, delay_cost=1)
	y1_mem0 += MAIN_MEM_r[0]
	S += alpha2V_U1_w < y1_mem0
	S += y1- 4 <= y1_mem0

	y1_mem1 = S.Task('y1_mem1', length=1, delay_cost=1)
	y1_mem1 += MAIN_MEM_r[0]
	S += y21_w < y1_mem1
	S += y1- 3 <= y1_mem1

	y1_mem2 = S.Task('y1_mem2', length=1, delay_cost=1)
	y1_mem2 += MAIN_MEM_r[0]
	S += alpha1_w < y1_mem2
	S += y1- 2 <= y1_mem2

	y_alt0 = S.Task('y_alt0', length=2, delay_cost=1)
	y_alt0 += alt(MAS)
	y_alt0_in = S.Task('y_alt0_in', length=1, delay_cost=1)
	y_alt0_in += alt(MAS_in)
	S += y_alt0_in*MAS_in[0]<=y_alt0*MAS[0]

	S += y_alt0_in*MAS_in[1]<=y_alt0*MAS[1]

	S += y_alt0_in*MAS_in[2]<=y_alt0*MAS[2]

	S += y_alt0_in*MAS_in[3]<=y_alt0*MAS[3]

	S += 0<y_alt0

	y_alt0_w = S.Task('y_alt0_w', length=1, delay_cost=1)
	y_alt0_w += alt(MAIN_MEM_w)
	S += y_alt0 <= y_alt0_w

	S += y_alt0<48

	y_alt0_mem0 = S.Task('y_alt0_mem0', length=1, delay_cost=1)
	y_alt0_mem0 += MAIN_MEM_r[0]
	S += y_alt0_mem0 <= y_alt0

	y_alt0_mem1 = S.Task('y_alt0_mem1', length=1, delay_cost=1)
	y_alt0_mem1 += MAIN_MEM_r[1]
	S += y0_w < y_alt0_mem1
	S += y_alt0_mem1 <= y_alt0

	y_alt1 = S.Task('y_alt1', length=2, delay_cost=1)
	y_alt1 += alt(MAS)
	y_alt1_in = S.Task('y_alt1_in', length=1, delay_cost=1)
	y_alt1_in += alt(MAS_in)
	S += y_alt1_in*MAS_in[0]<=y_alt1*MAS[0]

	S += y_alt1_in*MAS_in[1]<=y_alt1*MAS[1]

	S += y_alt1_in*MAS_in[2]<=y_alt1*MAS[2]

	S += y_alt1_in*MAS_in[3]<=y_alt1*MAS[3]

	S += 0<y_alt1

	y_alt1_w = S.Task('y_alt1_w', length=1, delay_cost=1)
	y_alt1_w += alt(MAIN_MEM_w)
	S += y_alt1 <= y_alt1_w

	S += y_alt1<1000

	y_alt1_mem0 = S.Task('y_alt1_mem0', length=1, delay_cost=1)
	y_alt1_mem0 += MAIN_MEM_r[0]
	S += y_alt1_mem0 <= y_alt1

	y_alt1_mem1 = S.Task('y_alt1_mem1', length=1, delay_cost=1)
	y_alt1_mem1 += MAIN_MEM_r[1]
	S += y1_w < y_alt1_mem1
	S += y_alt1_mem1 <= y_alt1

	Y_1 = S.Task('Y_1', length=3, delay_cost=1)
	Y_1 += alt(CSEL)

	Y_1_w = S.Task('Y_1_w', length=1, delay_cost=1)
	Y_1_w += alt(MAIN_MEM_w)
	S += Y_1+4 <= Y_1_w

	S += Y_1<1000

	Y_1_mem0 = S.Task('Y_1_mem0', length=1, delay_cost=1)
	Y_1_mem0 += MAIN_MEM_r[0]
	S += Y_1- 4 <= Y_1_mem0

	Y_1_mem1 = S.Task('Y_1_mem1', length=1, delay_cost=1)
	Y_1_mem1 += MAIN_MEM_r[0]
	S += y1_w < Y_1_mem1
	S += Y_1- 3 <= Y_1_mem1

	Y_1_mem2 = S.Task('Y_1_mem2', length=1, delay_cost=1)
	Y_1_mem2 += MAIN_MEM_r[0]
	S += y_alt1_w < Y_1_mem2
	S += Y_1- 2 <= Y_1_mem2

	Y_Hash1 = S.Task('Y_Hash1', length=9, delay_cost=1)
	Y_Hash1 += alt(MM)
	Y_Hash1_in = S.Task('Y_Hash1_in', length=1, delay_cost=1)
	Y_Hash1_in += alt(MM_in)
	S += Y_Hash1_in*MM_in[0]<=Y_Hash1*MM[0]
	S += 0<Y_Hash1

	Y_Hash1_w = S.Task('Y_Hash1_w', length=1, delay_cost=1)
	Y_Hash1_w += alt(MAIN_MEM_w)
	S += Y_Hash1 <= Y_Hash1_w

	S += Y_Hash1<1000

	Y_Hash1_mem0 = S.Task('Y_Hash1_mem0', length=1, delay_cost=1)
	Y_Hash1_mem0 += MAIN_MEM_r[0]
	S += Y_1_w < Y_Hash1_mem0
	S += Y_Hash1_mem0 <= Y_Hash1

	Y_Hash1_mem1 = S.Task('Y_Hash1_mem1', length=1, delay_cost=1)
	Y_Hash1_mem1 += MAIN_MEM_r[1]
	S += Y_Hash1_mem1 <= Y_Hash1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM1_stage2MAS4/2xSSWU_AFTER_EXP/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

