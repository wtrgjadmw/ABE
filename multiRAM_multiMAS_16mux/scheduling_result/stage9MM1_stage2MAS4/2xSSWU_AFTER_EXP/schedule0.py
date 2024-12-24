from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

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

	# new tasks
	alpha0 = S.Task('alpha0', length=9, delay_cost=1)
	alpha0 += alt(MM)
	alpha0_in = S.Task('alpha0_in', length=1, delay_cost=1)
	alpha0_in += alt(MM_in)
	S += alpha0_in*MM_in[0]<=alpha0*MM[0]
	alpha0_mem0 = S.Task('alpha0_mem0', length=1, delay_cost=1)
	alpha0_mem0 += MAIN_MEM_r[0]
	S += alpha0_mem0 <= alpha0

	alpha0_mem1 = S.Task('alpha0_mem1', length=1, delay_cost=1)
	alpha0_mem1 += MAIN_MEM_r[1]
	S += alpha0_mem1 <= alpha0

	alpha1 = S.Task('alpha1', length=9, delay_cost=1)
	alpha1 += alt(MM)
	alpha1_in = S.Task('alpha1_in', length=1, delay_cost=1)
	alpha1_in += alt(MM_in)
	S += alpha1_in*MM_in[0]<=alpha1*MM[0]
	alpha1_mem0 = S.Task('alpha1_mem0', length=1, delay_cost=1)
	alpha1_mem0 += MAIN_MEM_r[0]
	S += alpha1_mem0 <= alpha1

	alpha1_mem1 = S.Task('alpha1_mem1', length=1, delay_cost=1)
	alpha1_mem1 += MAIN_MEM_r[1]
	S += alpha1_mem1 <= alpha1

	xit2N0 = S.Task('xit2N0', length=9, delay_cost=1)
	xit2N0 += alt(MM)
	xit2N0_in = S.Task('xit2N0_in', length=1, delay_cost=1)
	xit2N0_in += alt(MM_in)
	S += xit2N0_in*MM_in[0]<=xit2N0*MM[0]
	S += 0<xit2N0

	xit2N0_w = S.Task('xit2N0_w', length=1, delay_cost=1)
	xit2N0_w += alt(MAIN_MEM_w)
	S += xit2N0 <= xit2N0_w

	xit2N0_mem0 = S.Task('xit2N0_mem0', length=1, delay_cost=1)
	xit2N0_mem0 += MAIN_MEM_r[0]
	S += xit2N0_mem0 <= xit2N0

	xit2N0_mem1 = S.Task('xit2N0_mem1', length=1, delay_cost=1)
	xit2N0_mem1 += MAIN_MEM_r[1]
	S += xit2N0_mem1 <= xit2N0

	xit2N1 = S.Task('xit2N1', length=9, delay_cost=1)
	xit2N1 += alt(MM)
	xit2N1_in = S.Task('xit2N1_in', length=1, delay_cost=1)
	xit2N1_in += alt(MM_in)
	S += xit2N1_in*MM_in[0]<=xit2N1*MM[0]
	S += 0<xit2N1

	xit2N1_w = S.Task('xit2N1_w', length=1, delay_cost=1)
	xit2N1_w += alt(MAIN_MEM_w)
	S += xit2N1 <= xit2N1_w

	xit2N1_mem0 = S.Task('xit2N1_mem0', length=1, delay_cost=1)
	xit2N1_mem0 += MAIN_MEM_r[0]
	S += xit2N1_mem0 <= xit2N1

	xit2N1_mem1 = S.Task('xit2N1_mem1', length=1, delay_cost=1)
	xit2N1_mem1 += MAIN_MEM_r[1]
	S += xit2N1_mem1 <= xit2N1

	t30 = S.Task('t30', length=9, delay_cost=1)
	t30 += alt(MM)
	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	t30_in += alt(MM_in)
	S += t30_in*MM_in[0]<=t30*MM[0]
	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MAIN_MEM_r[0]
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += MAIN_MEM_r[1]
	S += t30_mem1 <= t30

	t31 = S.Task('t31', length=9, delay_cost=1)
	t31 += alt(MM)
	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	t31_in += alt(MM_in)
	S += t31_in*MM_in[0]<=t31*MM[0]
	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += MAIN_MEM_r[0]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += MAIN_MEM_r[1]
	S += t31_mem1 <= t31

	alphaD0 = S.Task('alphaD0', length=9, delay_cost=1)
	alphaD0 += alt(MM)
	alphaD0_in = S.Task('alphaD0_in', length=1, delay_cost=1)
	alphaD0_in += alt(MM_in)
	S += alphaD0_in*MM_in[0]<=alphaD0*MM[0]
	S += 0<alphaD0

	alphaD0_w = S.Task('alphaD0_w', length=1, delay_cost=1)
	alphaD0_w += alt(MAIN_MEM_w)
	S += alphaD0 <= alphaD0_w

	alphaD0_mem0 = S.Task('alphaD0_mem0', length=1, delay_cost=1)
	alphaD0_mem0 += alt(MM_MEM)
	S += (alpha0*MM[0])-1 < alphaD0_mem0*MM_MEM[0]
	S += alphaD0_mem0 <= alphaD0

	alphaD0_mem1 = S.Task('alphaD0_mem1', length=1, delay_cost=1)
	alphaD0_mem1 += MAIN_MEM_r[1]
	S += alphaD0_mem1 <= alphaD0

	alphaD1 = S.Task('alphaD1', length=9, delay_cost=1)
	alphaD1 += alt(MM)
	alphaD1_in = S.Task('alphaD1_in', length=1, delay_cost=1)
	alphaD1_in += alt(MM_in)
	S += alphaD1_in*MM_in[0]<=alphaD1*MM[0]
	S += 0<alphaD1

	alphaD1_w = S.Task('alphaD1_w', length=1, delay_cost=1)
	alphaD1_w += alt(MAIN_MEM_w)
	S += alphaD1 <= alphaD1_w

	alphaD1_mem0 = S.Task('alphaD1_mem0', length=1, delay_cost=1)
	alphaD1_mem0 += alt(MM_MEM)
	S += (alpha1*MM[0])-1 < alphaD1_mem0*MM_MEM[0]
	S += alphaD1_mem0 <= alphaD1

	alphaD1_mem1 = S.Task('alphaD1_mem1', length=1, delay_cost=1)
	alphaD1_mem1 += MAIN_MEM_r[1]
	S += alphaD1_mem1 <= alphaD1

	alpha20 = S.Task('alpha20', length=9, delay_cost=1)
	alpha20 += alt(MM)
	alpha20_in = S.Task('alpha20_in', length=1, delay_cost=1)
	alpha20_in += alt(MM_in)
	S += alpha20_in*MM_in[0]<=alpha20*MM[0]
	alpha20_mem0 = S.Task('alpha20_mem0', length=1, delay_cost=1)
	alpha20_mem0 += alt(MM_MEM)
	S += (alpha0*MM[0])-1 < alpha20_mem0*MM_MEM[0]
	S += alpha20_mem0 <= alpha20

	alpha20_mem1 = S.Task('alpha20_mem1', length=1, delay_cost=1)
	alpha20_mem1 += alt(MM_MEM)
	S += (alpha0*MM[0])-1 < alpha20_mem1*MM_MEM[1]
	S += alpha20_mem1 <= alpha20

	alpha21 = S.Task('alpha21', length=9, delay_cost=1)
	alpha21 += alt(MM)
	alpha21_in = S.Task('alpha21_in', length=1, delay_cost=1)
	alpha21_in += alt(MM_in)
	S += alpha21_in*MM_in[0]<=alpha21*MM[0]
	alpha21_mem0 = S.Task('alpha21_mem0', length=1, delay_cost=1)
	alpha21_mem0 += alt(MM_MEM)
	S += (alpha1*MM[0])-1 < alpha21_mem0*MM_MEM[0]
	S += alpha21_mem0 <= alpha21

	alpha21_mem1 = S.Task('alpha21_mem1', length=1, delay_cost=1)
	alpha21_mem1 += alt(MM_MEM)
	S += (alpha1*MM[0])-1 < alpha21_mem1*MM_MEM[1]
	S += alpha21_mem1 <= alpha21

	alpha2V0 = S.Task('alpha2V0', length=9, delay_cost=1)
	alpha2V0 += alt(MM)
	alpha2V0_in = S.Task('alpha2V0_in', length=1, delay_cost=1)
	alpha2V0_in += alt(MM_in)
	S += alpha2V0_in*MM_in[0]<=alpha2V0*MM[0]
	alpha2V0_mem0 = S.Task('alpha2V0_mem0', length=1, delay_cost=1)
	alpha2V0_mem0 += alt(MM_MEM)
	S += (alpha20*MM[0])-1 < alpha2V0_mem0*MM_MEM[0]
	S += alpha2V0_mem0 <= alpha2V0

	alpha2V0_mem1 = S.Task('alpha2V0_mem1', length=1, delay_cost=1)
	alpha2V0_mem1 += MAIN_MEM_r[1]
	S += alpha2V0_mem1 <= alpha2V0

	alpha2V1 = S.Task('alpha2V1', length=9, delay_cost=1)
	alpha2V1 += alt(MM)
	alpha2V1_in = S.Task('alpha2V1_in', length=1, delay_cost=1)
	alpha2V1_in += alt(MM_in)
	S += alpha2V1_in*MM_in[0]<=alpha2V1*MM[0]
	alpha2V1_mem0 = S.Task('alpha2V1_mem0', length=1, delay_cost=1)
	alpha2V1_mem0 += alt(MM_MEM)
	S += (alpha21*MM[0])-1 < alpha2V1_mem0*MM_MEM[0]
	S += alpha2V1_mem0 <= alpha2V1

	alpha2V1_mem1 = S.Task('alpha2V1_mem1', length=1, delay_cost=1)
	alpha2V1_mem1 += MAIN_MEM_r[1]
	S += alpha2V1_mem1 <= alpha2V1

	t3alphaD0 = S.Task('t3alphaD0', length=9, delay_cost=1)
	t3alphaD0 += alt(MM)
	t3alphaD0_in = S.Task('t3alphaD0_in', length=1, delay_cost=1)
	t3alphaD0_in += alt(MM_in)
	S += t3alphaD0_in*MM_in[0]<=t3alphaD0*MM[0]
	t3alphaD0_mem0 = S.Task('t3alphaD0_mem0', length=1, delay_cost=1)
	t3alphaD0_mem0 += alt(MM_MEM)
	S += (t30*MM[0])-1 < t3alphaD0_mem0*MM_MEM[0]
	S += t3alphaD0_mem0 <= t3alphaD0

	t3alphaD0_mem1 = S.Task('t3alphaD0_mem1', length=1, delay_cost=1)
	t3alphaD0_mem1 += alt(MM_MEM)
	S += (alphaD0*MM[0])-1 < t3alphaD0_mem1*MM_MEM[1]
	S += t3alphaD0_mem1 <= t3alphaD0

	t3alphaD1 = S.Task('t3alphaD1', length=9, delay_cost=1)
	t3alphaD1 += alt(MM)
	t3alphaD1_in = S.Task('t3alphaD1_in', length=1, delay_cost=1)
	t3alphaD1_in += alt(MM_in)
	S += t3alphaD1_in*MM_in[0]<=t3alphaD1*MM[0]
	t3alphaD1_mem0 = S.Task('t3alphaD1_mem0', length=1, delay_cost=1)
	t3alphaD1_mem0 += alt(MM_MEM)
	S += (t31*MM[0])-1 < t3alphaD1_mem0*MM_MEM[0]
	S += t3alphaD1_mem0 <= t3alphaD1

	t3alphaD1_mem1 = S.Task('t3alphaD1_mem1', length=1, delay_cost=1)
	t3alphaD1_mem1 += alt(MM_MEM)
	S += (alphaD1*MM[0])-1 < t3alphaD1_mem1*MM_MEM[1]
	S += t3alphaD1_mem1 <= t3alphaD1

	y20 = S.Task('y20', length=9, delay_cost=1)
	y20 += alt(MM)
	y20_in = S.Task('y20_in', length=1, delay_cost=1)
	y20_in += alt(MM_in)
	S += y20_in*MM_in[0]<=y20*MM[0]
	S += 0<y20

	y20_w = S.Task('y20_w', length=1, delay_cost=1)
	y20_w += alt(MAIN_MEM_w)
	S += y20 <= y20_w

	y20_mem0 = S.Task('y20_mem0', length=1, delay_cost=1)
	y20_mem0 += MAIN_MEM_r[0]
	S += y20_mem0 <= y20

	y20_mem1 = S.Task('y20_mem1', length=1, delay_cost=1)
	y20_mem1 += alt(MM_MEM)
	S += (t3alphaD0*MM[0])-1 < y20_mem1*MM_MEM[1]
	S += y20_mem1 <= y20

	y21 = S.Task('y21', length=9, delay_cost=1)
	y21 += alt(MM)
	y21_in = S.Task('y21_in', length=1, delay_cost=1)
	y21_in += alt(MM_in)
	S += y21_in*MM_in[0]<=y21*MM[0]
	S += 0<y21

	y21_w = S.Task('y21_w', length=1, delay_cost=1)
	y21_w += alt(MAIN_MEM_w)
	S += y21 <= y21_w

	y21_mem0 = S.Task('y21_mem0', length=1, delay_cost=1)
	y21_mem0 += MAIN_MEM_r[0]
	S += y21_mem0 <= y21

	y21_mem1 = S.Task('y21_mem1', length=1, delay_cost=1)
	y21_mem1 += alt(MM_MEM)
	S += (t3alphaD1*MM[0])-1 < y21_mem1*MM_MEM[1]
	S += y21_mem1 <= y21

	alpha2V_U0 = S.Task('alpha2V_U0', length=2, delay_cost=1)
	alpha2V_U0 += alt(MAS)
	alpha2V_U0_in = S.Task('alpha2V_U0_in', length=1, delay_cost=1)
	alpha2V_U0_in += alt(MAS_in)
	S += alpha2V_U0_in*MAS_in[0]<=alpha2V_U0*MAS[0]

	S += alpha2V_U0_in*MAS_in[1]<=alpha2V_U0*MAS[1]

	S += alpha2V_U0_in*MAS_in[2]<=alpha2V_U0*MAS[2]

	S += alpha2V_U0_in*MAS_in[3]<=alpha2V_U0*MAS[3]

	S += 0<alpha2V_U0

	alpha2V_U0_w = S.Task('alpha2V_U0_w', length=1, delay_cost=1)
	alpha2V_U0_w += alt(MAIN_MEM_w)
	S += alpha2V_U0 <= alpha2V_U0_w

	alpha2V_U0_mem0 = S.Task('alpha2V_U0_mem0', length=1, delay_cost=1)
	alpha2V_U0_mem0 += alt(MM_MEM)
	S += (alpha2V0*MM[0])-1 < alpha2V_U0_mem0*MM_MEM[0]
	S += alpha2V_U0_mem0 <= alpha2V_U0

	alpha2V_U0_mem1 = S.Task('alpha2V_U0_mem1', length=1, delay_cost=1)
	alpha2V_U0_mem1 += MAIN_MEM_r[1]
	S += alpha2V_U0_mem1 <= alpha2V_U0

	alpha2V_U1 = S.Task('alpha2V_U1', length=2, delay_cost=1)
	alpha2V_U1 += alt(MAS)
	alpha2V_U1_in = S.Task('alpha2V_U1_in', length=1, delay_cost=1)
	alpha2V_U1_in += alt(MAS_in)
	S += alpha2V_U1_in*MAS_in[0]<=alpha2V_U1*MAS[0]

	S += alpha2V_U1_in*MAS_in[1]<=alpha2V_U1*MAS[1]

	S += alpha2V_U1_in*MAS_in[2]<=alpha2V_U1*MAS[2]

	S += alpha2V_U1_in*MAS_in[3]<=alpha2V_U1*MAS[3]

	S += 0<alpha2V_U1

	alpha2V_U1_w = S.Task('alpha2V_U1_w', length=1, delay_cost=1)
	alpha2V_U1_w += alt(MAIN_MEM_w)
	S += alpha2V_U1 <= alpha2V_U1_w

	alpha2V_U1_mem0 = S.Task('alpha2V_U1_mem0', length=1, delay_cost=1)
	alpha2V_U1_mem0 += alt(MM_MEM)
	S += (alpha2V1*MM[0])-1 < alpha2V_U1_mem0*MM_MEM[0]
	S += alpha2V_U1_mem0 <= alpha2V_U1

	alpha2V_U1_mem1 = S.Task('alpha2V_U1_mem1', length=1, delay_cost=1)
	alpha2V_U1_mem1 += MAIN_MEM_r[1]
	S += alpha2V_U1_mem1 <= alpha2V_U1

	X0 = S.Task('X0', length=3, delay_cost=1)
	X0 += alt(CSEL)

	X0_w = S.Task('X0_w', length=1, delay_cost=1)
	X0_w += alt(MAIN_MEM_w)
	S += X0+2 <= X0_w

	X0_mem0 = S.Task('X0_mem0', length=1, delay_cost=1)
	X0_mem0 += MAIN_MEM_r[0]
	S += alpha2V_U0_w < X0_mem0
	S += X0_mem0+ 2 <= X0

	X0_mem1 = S.Task('X0_mem1', length=1, delay_cost=1)
	X0_mem1 += MAIN_MEM_r[0]
	S += xit2N0_w < X0_mem1
	S += X0_mem1+ 1 <= X0

	X0_mem2 = S.Task('X0_mem2', length=1, delay_cost=1)
	X0_mem2 += MAIN_MEM_r[0]
	S += X0_mem2+ 0 <= X0

	X1 = S.Task('X1', length=3, delay_cost=1)
	X1 += alt(CSEL)

	X1_w = S.Task('X1_w', length=1, delay_cost=1)
	X1_w += alt(MAIN_MEM_w)
	S += X1+2 <= X1_w

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

	y0 = S.Task('y0', length=3, delay_cost=1)
	y0 += alt(CSEL)

	y0_w = S.Task('y0_w', length=1, delay_cost=1)
	y0_w += alt(MAIN_MEM_w)
	S += y0+2 <= y0_w

	y0_mem0 = S.Task('y0_mem0', length=1, delay_cost=1)
	y0_mem0 += MAIN_MEM_r[0]
	S += alpha2V_U0_w < y0_mem0
	S += y0_mem0+ 2 <= y0

	y0_mem1 = S.Task('y0_mem1', length=1, delay_cost=1)
	y0_mem1 += MAIN_MEM_r[0]
	S += y20_w < y0_mem1
	S += y0_mem1+ 1 <= y0

	y0_mem2 = S.Task('y0_mem2', length=1, delay_cost=1)
	y0_mem2 += MAIN_MEM_r[0]
	S += alphaD0_w < y0_mem2
	S += y0_mem2+ 0 <= y0

	y1 = S.Task('y1', length=3, delay_cost=1)
	y1 += alt(CSEL)

	y1_w = S.Task('y1_w', length=1, delay_cost=1)
	y1_w += alt(MAIN_MEM_w)
	S += y1+2 <= y1_w

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

	y_alt1_mem0 = S.Task('y_alt1_mem0', length=1, delay_cost=1)
	y_alt1_mem0 += MAIN_MEM_r[0]
	S += y_alt1_mem0 <= y_alt1

	y_alt1_mem1 = S.Task('y_alt1_mem1', length=1, delay_cost=1)
	y_alt1_mem1 += MAIN_MEM_r[1]
	S += y1_w < y_alt1_mem1
	S += y_alt1_mem1 <= y_alt1

	Y0 = S.Task('Y0', length=3, delay_cost=1)
	Y0 += alt(CSEL)

	Y0_w = S.Task('Y0_w', length=1, delay_cost=1)
	Y0_w += alt(MAIN_MEM_w)
	S += Y0+2 <= Y0_w

	Y0_mem0 = S.Task('Y0_mem0', length=1, delay_cost=1)
	Y0_mem0 += MAIN_MEM_r[0]
	S += Y0_mem0+ 2 <= Y0

	Y0_mem1 = S.Task('Y0_mem1', length=1, delay_cost=1)
	Y0_mem1 += MAIN_MEM_r[0]
	S += y0_w < Y0_mem1
	S += Y0_mem1+ 1 <= Y0

	Y0_mem2 = S.Task('Y0_mem2', length=1, delay_cost=1)
	Y0_mem2 += MAIN_MEM_r[0]
	S += y_alt0_w < Y0_mem2
	S += Y0_mem2+ 0 <= Y0

	Y1 = S.Task('Y1', length=3, delay_cost=1)
	Y1 += alt(CSEL)

	Y1_w = S.Task('Y1_w', length=1, delay_cost=1)
	Y1_w += alt(MAIN_MEM_w)
	S += Y1+2 <= Y1_w

	Y1_mem0 = S.Task('Y1_mem0', length=1, delay_cost=1)
	Y1_mem0 += MAIN_MEM_r[0]
	S += Y1_mem0+ 2 <= Y1

	Y1_mem1 = S.Task('Y1_mem1', length=1, delay_cost=1)
	Y1_mem1 += MAIN_MEM_r[0]
	S += y1_w < Y1_mem1
	S += Y1_mem1+ 1 <= Y1

	Y1_mem2 = S.Task('Y1_mem2', length=1, delay_cost=1)
	Y1_mem2 += MAIN_MEM_r[0]
	S += y_alt1_w < Y1_mem2
	S += Y1_mem2+ 0 <= Y1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM1_stage2MAS4/2xSSWU_AFTER_EXP/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

