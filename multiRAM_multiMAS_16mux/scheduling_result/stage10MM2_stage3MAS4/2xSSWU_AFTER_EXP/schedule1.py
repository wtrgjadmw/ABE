from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 184
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
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

	alpha0 = S.Task('alpha0', length=10, delay_cost=1)
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

	alpha1 = S.Task('alpha1', length=10, delay_cost=1)
	S += alpha1 >= 2
	alpha1 += MM[1]

	xit2N0_in = S.Task('xit2N0_in', length=1, delay_cost=1)
	S += xit2N0_in >= 2
	xit2N0_in += MM_in[0]

	xit2N0_mem0 = S.Task('xit2N0_mem0', length=1, delay_cost=1)
	S += xit2N0_mem0 >= 2
	xit2N0_mem0 += MAIN_MEM_r[0]

	xit2N0_mem1 = S.Task('xit2N0_mem1', length=1, delay_cost=1)
	S += xit2N0_mem1 >= 2
	xit2N0_mem1 += MAIN_MEM_r[1]

	xit2N0 = S.Task('xit2N0', length=10, delay_cost=1)
	S += xit2N0 >= 3
	xit2N0 += MM[0]

	xit2N1_in = S.Task('xit2N1_in', length=1, delay_cost=1)
	S += xit2N1_in >= 3
	xit2N1_in += MM_in[1]

	xit2N1_mem0 = S.Task('xit2N1_mem0', length=1, delay_cost=1)
	S += xit2N1_mem0 >= 3
	xit2N1_mem0 += MAIN_MEM_r[0]

	xit2N1_mem1 = S.Task('xit2N1_mem1', length=1, delay_cost=1)
	S += xit2N1_mem1 >= 3
	xit2N1_mem1 += MAIN_MEM_r[1]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 4
	t30_in += MM_in[0]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 4
	t30_mem0 += MAIN_MEM_r[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 4
	t30_mem1 += MAIN_MEM_r[1]

	xit2N1 = S.Task('xit2N1', length=10, delay_cost=1)
	S += xit2N1 >= 4
	xit2N1 += MM[1]

	t30 = S.Task('t30', length=10, delay_cost=1)
	S += t30 >= 5
	t30 += MM[0]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 5
	t31_in += MM_in[0]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 5
	t31_mem0 += MAIN_MEM_r[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 5
	t31_mem1 += MAIN_MEM_r[1]

	t31 = S.Task('t31', length=10, delay_cost=1)
	S += t31 >= 6
	t31 += MM[0]

	alpha20_in = S.Task('alpha20_in', length=1, delay_cost=1)
	S += alpha20_in >= 10
	alpha20_in += MM_in[1]

	alpha20_mem0 = S.Task('alpha20_mem0', length=1, delay_cost=1)
	S += alpha20_mem0 >= 10
	alpha20_mem0 += MM_MEM[0]

	alpha20_mem1 = S.Task('alpha20_mem1', length=1, delay_cost=1)
	S += alpha20_mem1 >= 10
	alpha20_mem1 += MM_MEM[1]

	alpha20 = S.Task('alpha20', length=10, delay_cost=1)
	S += alpha20 >= 11
	alpha20 += MM[1]

	alpha21_in = S.Task('alpha21_in', length=1, delay_cost=1)
	S += alpha21_in >= 11
	alpha21_in += MM_in[1]

	alpha21_mem0 = S.Task('alpha21_mem0', length=1, delay_cost=1)
	S += alpha21_mem0 >= 11
	alpha21_mem0 += MM_MEM[2]

	alpha21_mem1 = S.Task('alpha21_mem1', length=1, delay_cost=1)
	S += alpha21_mem1 >= 11
	alpha21_mem1 += MM_MEM[3]

	alphaD0_in = S.Task('alphaD0_in', length=1, delay_cost=1)
	S += alphaD0_in >= 11
	alphaD0_in += MM_in[0]

	alphaD0_mem0 = S.Task('alphaD0_mem0', length=1, delay_cost=1)
	S += alphaD0_mem0 >= 11
	alphaD0_mem0 += MM_MEM[0]

	alphaD0_mem1 = S.Task('alphaD0_mem1', length=1, delay_cost=1)
	S += alphaD0_mem1 >= 11
	alphaD0_mem1 += MAIN_MEM_r[1]

	alpha21 = S.Task('alpha21', length=10, delay_cost=1)
	S += alpha21 >= 12
	alpha21 += MM[1]

	alphaD0 = S.Task('alphaD0', length=10, delay_cost=1)
	S += alphaD0 >= 12
	alphaD0 += MM[0]

	alphaD1_in = S.Task('alphaD1_in', length=1, delay_cost=1)
	S += alphaD1_in >= 12
	alphaD1_in += MM_in[1]

	alphaD1_mem0 = S.Task('alphaD1_mem0', length=1, delay_cost=1)
	S += alphaD1_mem0 >= 12
	alphaD1_mem0 += MM_MEM[2]

	alphaD1_mem1 = S.Task('alphaD1_mem1', length=1, delay_cost=1)
	S += alphaD1_mem1 >= 12
	alphaD1_mem1 += MAIN_MEM_r[1]

	alphaD1 = S.Task('alphaD1', length=10, delay_cost=1)
	S += alphaD1 >= 13
	alphaD1 += MM[1]

	xit2N0_w = S.Task('xit2N0_w', length=1, delay_cost=1)
	S += xit2N0_w >= 13
	xit2N0_w += MAIN_MEM_w

	xit2N1_w = S.Task('xit2N1_w', length=1, delay_cost=1)
	S += xit2N1_w >= 14
	xit2N1_w += MAIN_MEM_w

	alpha2V0_in = S.Task('alpha2V0_in', length=1, delay_cost=1)
	S += alpha2V0_in >= 20
	alpha2V0_in += MM_in[1]

	alpha2V0_mem0 = S.Task('alpha2V0_mem0', length=1, delay_cost=1)
	S += alpha2V0_mem0 >= 20
	alpha2V0_mem0 += MM_MEM[2]

	alpha2V0_mem1 = S.Task('alpha2V0_mem1', length=1, delay_cost=1)
	S += alpha2V0_mem1 >= 20
	alpha2V0_mem1 += MAIN_MEM_r[1]

	alpha2V0 = S.Task('alpha2V0', length=10, delay_cost=1)
	S += alpha2V0 >= 21
	alpha2V0 += MM[1]

	alpha2V1_in = S.Task('alpha2V1_in', length=1, delay_cost=1)
	S += alpha2V1_in >= 21
	alpha2V1_in += MM_in[0]

	alpha2V1_mem0 = S.Task('alpha2V1_mem0', length=1, delay_cost=1)
	S += alpha2V1_mem0 >= 21
	alpha2V1_mem0 += MM_MEM[2]

	alpha2V1_mem1 = S.Task('alpha2V1_mem1', length=1, delay_cost=1)
	S += alpha2V1_mem1 >= 21
	alpha2V1_mem1 += MAIN_MEM_r[1]

	t3alphaD0_in = S.Task('t3alphaD0_in', length=1, delay_cost=1)
	S += t3alphaD0_in >= 21
	t3alphaD0_in += MM_in[1]

	t3alphaD0_mem0 = S.Task('t3alphaD0_mem0', length=1, delay_cost=1)
	S += t3alphaD0_mem0 >= 21
	t3alphaD0_mem0 += MM_MEM[0]

	t3alphaD0_mem1 = S.Task('t3alphaD0_mem1', length=1, delay_cost=1)
	S += t3alphaD0_mem1 >= 21
	t3alphaD0_mem1 += MM_MEM[1]

	alpha2V1 = S.Task('alpha2V1', length=10, delay_cost=1)
	S += alpha2V1 >= 22
	alpha2V1 += MM[0]

	alphaD0_w = S.Task('alphaD0_w', length=1, delay_cost=1)
	S += alphaD0_w >= 22
	alphaD0_w += MAIN_MEM_w

	t3alphaD0 = S.Task('t3alphaD0', length=10, delay_cost=1)
	S += t3alphaD0 >= 22
	t3alphaD0 += MM[1]

	t3alphaD1_in = S.Task('t3alphaD1_in', length=1, delay_cost=1)
	S += t3alphaD1_in >= 22
	t3alphaD1_in += MM_in[0]

	t3alphaD1_mem0 = S.Task('t3alphaD1_mem0', length=1, delay_cost=1)
	S += t3alphaD1_mem0 >= 22
	t3alphaD1_mem0 += MM_MEM[0]

	t3alphaD1_mem1 = S.Task('t3alphaD1_mem1', length=1, delay_cost=1)
	S += t3alphaD1_mem1 >= 22
	t3alphaD1_mem1 += MM_MEM[3]

	alphaD1_w = S.Task('alphaD1_w', length=1, delay_cost=1)
	S += alphaD1_w >= 23
	alphaD1_w += MAIN_MEM_w

	t3alphaD1 = S.Task('t3alphaD1', length=10, delay_cost=1)
	S += t3alphaD1 >= 23
	t3alphaD1 += MM[0]

	alpha2V_U0_in = S.Task('alpha2V_U0_in', length=1, delay_cost=1)
	S += alpha2V_U0_in >= 30
	alpha2V_U0_in += MAS_in[2]

	alpha2V_U0_mem0 = S.Task('alpha2V_U0_mem0', length=1, delay_cost=1)
	S += alpha2V_U0_mem0 >= 30
	alpha2V_U0_mem0 += MM_MEM[2]

	alpha2V_U0_mem1 = S.Task('alpha2V_U0_mem1', length=1, delay_cost=1)
	S += alpha2V_U0_mem1 >= 30
	alpha2V_U0_mem1 += MAIN_MEM_r[1]

	alpha2V_U0 = S.Task('alpha2V_U0', length=3, delay_cost=1)
	S += alpha2V_U0 >= 31
	alpha2V_U0 += MAS[2]

	alpha2V_U1_in = S.Task('alpha2V_U1_in', length=1, delay_cost=1)
	S += alpha2V_U1_in >= 31
	alpha2V_U1_in += MAS_in[2]

	alpha2V_U1_mem0 = S.Task('alpha2V_U1_mem0', length=1, delay_cost=1)
	S += alpha2V_U1_mem0 >= 31
	alpha2V_U1_mem0 += MM_MEM[0]

	alpha2V_U1_mem1 = S.Task('alpha2V_U1_mem1', length=1, delay_cost=1)
	S += alpha2V_U1_mem1 >= 31
	alpha2V_U1_mem1 += MAIN_MEM_r[1]

	y20_in = S.Task('y20_in', length=1, delay_cost=1)
	S += y20_in >= 31
	y20_in += MM_in[1]

	y20_mem0 = S.Task('y20_mem0', length=1, delay_cost=1)
	S += y20_mem0 >= 31
	y20_mem0 += MAIN_MEM_r[0]

	y20_mem1 = S.Task('y20_mem1', length=1, delay_cost=1)
	S += y20_mem1 >= 31
	y20_mem1 += MM_MEM[3]

	alpha2V_U1 = S.Task('alpha2V_U1', length=3, delay_cost=1)
	S += alpha2V_U1 >= 32
	alpha2V_U1 += MAS[2]

	y20 = S.Task('y20', length=10, delay_cost=1)
	S += y20 >= 32
	y20 += MM[1]

	y21_in = S.Task('y21_in', length=1, delay_cost=1)
	S += y21_in >= 33
	y21_in += MM_in[0]

	y21_mem0 = S.Task('y21_mem0', length=1, delay_cost=1)
	S += y21_mem0 >= 33
	y21_mem0 += MAIN_MEM_r[0]

	y21_mem1 = S.Task('y21_mem1', length=1, delay_cost=1)
	S += y21_mem1 >= 33
	y21_mem1 += MM_MEM[1]

	alpha2V_U0_w = S.Task('alpha2V_U0_w', length=1, delay_cost=1)
	S += alpha2V_U0_w >= 34
	alpha2V_U0_w += MAIN_MEM_w

	y21 = S.Task('y21', length=10, delay_cost=1)
	S += y21 >= 34
	y21 += MM[0]

	X0_mem0 = S.Task('X0_mem0', length=1, delay_cost=1)
	S += X0_mem0 >= 35
	X0_mem0 += MAIN_MEM_r[0]

	alpha2V_U1_w = S.Task('alpha2V_U1_w', length=1, delay_cost=1)
	S += alpha2V_U1_w >= 35
	alpha2V_U1_w += MAIN_MEM_w

	X0_mem1 = S.Task('X0_mem1', length=1, delay_cost=1)
	S += X0_mem1 >= 36
	X0_mem1 += MAIN_MEM_r[0]

	X0_mem2 = S.Task('X0_mem2', length=1, delay_cost=1)
	S += X0_mem2 >= 37
	X0_mem2 += MAIN_MEM_r[0]

	X0 = S.Task('X0', length=3, delay_cost=1)
	S += X0 >= 38
	X0 += CSEL

	X1_mem0 = S.Task('X1_mem0', length=1, delay_cost=1)
	S += X1_mem0 >= 38
	X1_mem0 += MAIN_MEM_r[0]

	X1_mem1 = S.Task('X1_mem1', length=1, delay_cost=1)
	S += X1_mem1 >= 39
	X1_mem1 += MAIN_MEM_r[0]

	X1_mem2 = S.Task('X1_mem2', length=1, delay_cost=1)
	S += X1_mem2 >= 40
	X1_mem2 += MAIN_MEM_r[0]

	X1 = S.Task('X1', length=3, delay_cost=1)
	S += X1 >= 41
	X1 += CSEL

	y0_mem0 = S.Task('y0_mem0', length=1, delay_cost=1)
	S += y0_mem0 >= 42
	y0_mem0 += MAIN_MEM_r[0]

	y20_w = S.Task('y20_w', length=1, delay_cost=1)
	S += y20_w >= 42
	y20_w += MAIN_MEM_w

	X0_w = S.Task('X0_w', length=1, delay_cost=1)
	S += X0_w >= 43
	X0_w += MAIN_MEM_w

	y0_mem1 = S.Task('y0_mem1', length=1, delay_cost=1)
	S += y0_mem1 >= 43
	y0_mem1 += MAIN_MEM_r[0]

	y0_mem2 = S.Task('y0_mem2', length=1, delay_cost=1)
	S += y0_mem2 >= 44
	y0_mem2 += MAIN_MEM_r[0]

	y21_w = S.Task('y21_w', length=1, delay_cost=1)
	S += y21_w >= 44
	y21_w += MAIN_MEM_w

	y0 = S.Task('y0', length=3, delay_cost=1)
	S += y0 >= 45
	y0 += CSEL

	y1_mem0 = S.Task('y1_mem0', length=1, delay_cost=1)
	S += y1_mem0 >= 45
	y1_mem0 += MAIN_MEM_r[0]

	X1_w = S.Task('X1_w', length=1, delay_cost=1)
	S += X1_w >= 46
	X1_w += MAIN_MEM_w

	y1_mem1 = S.Task('y1_mem1', length=1, delay_cost=1)
	S += y1_mem1 >= 46
	y1_mem1 += MAIN_MEM_r[0]

	y1_mem2 = S.Task('y1_mem2', length=1, delay_cost=1)
	S += y1_mem2 >= 47
	y1_mem2 += MAIN_MEM_r[0]

	y1 = S.Task('y1', length=3, delay_cost=1)
	S += y1 >= 48
	y1 += CSEL

	y0_w = S.Task('y0_w', length=1, delay_cost=1)
	S += y0_w >= 50
	y0_w += MAIN_MEM_w

	y_alt0_in = S.Task('y_alt0_in', length=1, delay_cost=1)
	S += y_alt0_in >= 51
	y_alt0_in += MAS_in[2]

	y_alt0_mem0 = S.Task('y_alt0_mem0', length=1, delay_cost=1)
	S += y_alt0_mem0 >= 51
	y_alt0_mem0 += MAIN_MEM_r[0]

	y_alt0_mem1 = S.Task('y_alt0_mem1', length=1, delay_cost=1)
	S += y_alt0_mem1 >= 51
	y_alt0_mem1 += MAIN_MEM_r[1]

	y_alt0 = S.Task('y_alt0', length=3, delay_cost=1)
	S += y_alt0 >= 52
	y_alt0 += MAS[2]

	y1_w = S.Task('y1_w', length=1, delay_cost=1)
	S += y1_w >= 53
	y1_w += MAIN_MEM_w

	Y0_mem0 = S.Task('Y0_mem0', length=1, delay_cost=1)
	S += Y0_mem0 >= 55
	Y0_mem0 += MAIN_MEM_r[0]

	y_alt0_w = S.Task('y_alt0_w', length=1, delay_cost=1)
	S += y_alt0_w >= 55
	y_alt0_w += MAIN_MEM_w

	Y0_mem1 = S.Task('Y0_mem1', length=1, delay_cost=1)
	S += Y0_mem1 >= 56
	Y0_mem1 += MAIN_MEM_r[0]

	Y0_mem2 = S.Task('Y0_mem2', length=1, delay_cost=1)
	S += Y0_mem2 >= 57
	Y0_mem2 += MAIN_MEM_r[0]

	Y0 = S.Task('Y0', length=3, delay_cost=1)
	S += Y0 >= 58
	Y0 += CSEL

	Y0_w = S.Task('Y0_w', length=1, delay_cost=1)
	S += Y0_w >= 63
	Y0_w += MAIN_MEM_w


	# new tasks
	y_alt1 = S.Task('y_alt1', length=3, delay_cost=1)
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
