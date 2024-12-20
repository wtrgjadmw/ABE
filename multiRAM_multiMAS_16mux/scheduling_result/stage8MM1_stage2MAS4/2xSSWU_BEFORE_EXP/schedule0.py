from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
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
	t20 = S.Task('t20', length=8, delay_cost=1)
	t20 += alt(MM)
	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	t20_in += alt(MM_in)
	S += t20_in*MM_in[0]<=t20*MM[0]
	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += MAIN_MEM_r[0]
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += MAIN_MEM_r[1]
	S += t20_mem1 <= t20

	t21 = S.Task('t21', length=8, delay_cost=1)
	t21 += alt(MM)
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	t21_in += alt(MM_in)
	S += t21_in*MM_in[0]<=t21*MM[0]
	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += MAIN_MEM_r[0]
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += MAIN_MEM_r[1]
	S += t21_mem1 <= t21

	xit20 = S.Task('xit20', length=2, delay_cost=1)
	xit20 += alt(MAS)
	xit20_in = S.Task('xit20_in', length=1, delay_cost=1)
	xit20_in += alt(MAS_in)
	S += xit20_in*MAS_in[0]<=xit20*MAS[0]

	S += xit20_in*MAS_in[1]<=xit20*MAS[1]

	S += xit20_in*MAS_in[2]<=xit20*MAS[2]

	S += xit20_in*MAS_in[3]<=xit20*MAS[3]

	xit20_mem0 = S.Task('xit20_mem0', length=1, delay_cost=1)
	xit20_mem0 += MAIN_MEM_r[0]
	S += xit20_mem0 <= xit20

	xit20_mem1 = S.Task('xit20_mem1', length=1, delay_cost=1)
	xit20_mem1 += alt(MM_MEM)
	S += (t20*MM[0])-1 < xit20_mem1*MM_MEM[1]
	S += xit20_mem1 <= xit20

	xit21 = S.Task('xit21', length=2, delay_cost=1)
	xit21 += alt(MAS)
	xit21_in = S.Task('xit21_in', length=1, delay_cost=1)
	xit21_in += alt(MAS_in)
	S += xit21_in*MAS_in[0]<=xit21*MAS[0]

	S += xit21_in*MAS_in[1]<=xit21*MAS[1]

	S += xit21_in*MAS_in[2]<=xit21*MAS[2]

	S += xit21_in*MAS_in[3]<=xit21*MAS[3]

	xit21_mem0 = S.Task('xit21_mem0', length=1, delay_cost=1)
	xit21_mem0 += MAIN_MEM_r[0]
	S += xit21_mem0 <= xit21

	xit21_mem1 = S.Task('xit21_mem1', length=1, delay_cost=1)
	xit21_mem1 += alt(MM_MEM)
	S += (t21*MM[0])-1 < xit21_mem1*MM_MEM[1]
	S += xit21_mem1 <= xit21

	xi2t40 = S.Task('xi2t40', length=8, delay_cost=1)
	xi2t40 += alt(MM)
	xi2t40_in = S.Task('xi2t40_in', length=1, delay_cost=1)
	xi2t40_in += alt(MM_in)
	S += xi2t40_in*MM_in[0]<=xi2t40*MM[0]
	xi2t40_mem0 = S.Task('xi2t40_mem0', length=1, delay_cost=1)
	xi2t40_mem0 += alt(MAS_MEM)
	S += (xit20*MAS[0])-1 < xi2t40_mem0*MAS_MEM[0]
	S += (xit20*MAS[1])-1 < xi2t40_mem0*MAS_MEM[2]
	S += (xit20*MAS[2])-1 < xi2t40_mem0*MAS_MEM[4]
	S += (xit20*MAS[3])-1 < xi2t40_mem0*MAS_MEM[6]
	S += xi2t40_mem0 <= xi2t40

	xi2t40_mem1 = S.Task('xi2t40_mem1', length=1, delay_cost=1)
	xi2t40_mem1 += alt(MAS_MEM)
	S += (xit20*MAS[0])-1 < xi2t40_mem1*MAS_MEM[1]
	S += (xit20*MAS[1])-1 < xi2t40_mem1*MAS_MEM[3]
	S += (xit20*MAS[2])-1 < xi2t40_mem1*MAS_MEM[5]
	S += (xit20*MAS[3])-1 < xi2t40_mem1*MAS_MEM[7]
	S += xi2t40_mem1 <= xi2t40

	xi2t41 = S.Task('xi2t41', length=8, delay_cost=1)
	xi2t41 += alt(MM)
	xi2t41_in = S.Task('xi2t41_in', length=1, delay_cost=1)
	xi2t41_in += alt(MM_in)
	S += xi2t41_in*MM_in[0]<=xi2t41*MM[0]
	xi2t41_mem0 = S.Task('xi2t41_mem0', length=1, delay_cost=1)
	xi2t41_mem0 += alt(MAS_MEM)
	S += (xit21*MAS[0])-1 < xi2t41_mem0*MAS_MEM[0]
	S += (xit21*MAS[1])-1 < xi2t41_mem0*MAS_MEM[2]
	S += (xit21*MAS[2])-1 < xi2t41_mem0*MAS_MEM[4]
	S += (xit21*MAS[3])-1 < xi2t41_mem0*MAS_MEM[6]
	S += xi2t41_mem0 <= xi2t41

	xi2t41_mem1 = S.Task('xi2t41_mem1', length=1, delay_cost=1)
	xi2t41_mem1 += alt(MAS_MEM)
	S += (xit21*MAS[0])-1 < xi2t41_mem1*MAS_MEM[1]
	S += (xit21*MAS[1])-1 < xi2t41_mem1*MAS_MEM[3]
	S += (xit21*MAS[2])-1 < xi2t41_mem1*MAS_MEM[5]
	S += (xit21*MAS[3])-1 < xi2t41_mem1*MAS_MEM[7]
	S += xi2t41_mem1 <= xi2t41

	D_a_0 = S.Task('D_a_0', length=2, delay_cost=1)
	D_a_0 += alt(MAS)
	D_a_0_in = S.Task('D_a_0_in', length=1, delay_cost=1)
	D_a_0_in += alt(MAS_in)
	S += D_a_0_in*MAS_in[0]<=D_a_0*MAS[0]

	S += D_a_0_in*MAS_in[1]<=D_a_0*MAS[1]

	S += D_a_0_in*MAS_in[2]<=D_a_0*MAS[2]

	S += D_a_0_in*MAS_in[3]<=D_a_0*MAS[3]

	D_a_0_mem0 = S.Task('D_a_0_mem0', length=1, delay_cost=1)
	D_a_0_mem0 += alt(MAS_MEM)
	S += (xit20*MAS[0])-1 < D_a_0_mem0*MAS_MEM[0]
	S += (xit20*MAS[1])-1 < D_a_0_mem0*MAS_MEM[2]
	S += (xit20*MAS[2])-1 < D_a_0_mem0*MAS_MEM[4]
	S += (xit20*MAS[3])-1 < D_a_0_mem0*MAS_MEM[6]
	S += D_a_0_mem0 <= D_a_0

	D_a_0_mem1 = S.Task('D_a_0_mem1', length=1, delay_cost=1)
	D_a_0_mem1 += alt(MM_MEM)
	S += (xi2t40*MM[0])-1 < D_a_0_mem1*MM_MEM[1]
	S += D_a_0_mem1 <= D_a_0

	D_a_1 = S.Task('D_a_1', length=2, delay_cost=1)
	D_a_1 += alt(MAS)
	D_a_1_in = S.Task('D_a_1_in', length=1, delay_cost=1)
	D_a_1_in += alt(MAS_in)
	S += D_a_1_in*MAS_in[0]<=D_a_1*MAS[0]

	S += D_a_1_in*MAS_in[1]<=D_a_1*MAS[1]

	S += D_a_1_in*MAS_in[2]<=D_a_1*MAS[2]

	S += D_a_1_in*MAS_in[3]<=D_a_1*MAS[3]

	D_a_1_mem0 = S.Task('D_a_1_mem0', length=1, delay_cost=1)
	D_a_1_mem0 += alt(MAS_MEM)
	S += (xit21*MAS[0])-1 < D_a_1_mem0*MAS_MEM[0]
	S += (xit21*MAS[1])-1 < D_a_1_mem0*MAS_MEM[2]
	S += (xit21*MAS[2])-1 < D_a_1_mem0*MAS_MEM[4]
	S += (xit21*MAS[3])-1 < D_a_1_mem0*MAS_MEM[6]
	S += D_a_1_mem0 <= D_a_1

	D_a_1_mem1 = S.Task('D_a_1_mem1', length=1, delay_cost=1)
	D_a_1_mem1 += alt(MM_MEM)
	S += (xi2t41*MM[0])-1 < D_a_1_mem1*MM_MEM[1]
	S += D_a_1_mem1 <= D_a_1

	negD0 = S.Task('negD0', length=8, delay_cost=1)
	negD0 += alt(MM)
	negD0_in = S.Task('negD0_in', length=1, delay_cost=1)
	negD0_in += alt(MM_in)
	S += negD0_in*MM_in[0]<=negD0*MM[0]
	negD0_mem0 = S.Task('negD0_mem0', length=1, delay_cost=1)
	negD0_mem0 += alt(MAS_MEM)
	S += (D_a_0*MAS[0])-1 < negD0_mem0*MAS_MEM[0]
	S += (D_a_0*MAS[1])-1 < negD0_mem0*MAS_MEM[2]
	S += (D_a_0*MAS[2])-1 < negD0_mem0*MAS_MEM[4]
	S += (D_a_0*MAS[3])-1 < negD0_mem0*MAS_MEM[6]
	S += negD0_mem0 <= negD0

	negD0_mem1 = S.Task('negD0_mem1', length=1, delay_cost=1)
	negD0_mem1 += MAIN_MEM_r[1]
	S += negD0_mem1 <= negD0

	negD1 = S.Task('negD1', length=8, delay_cost=1)
	negD1 += alt(MM)
	negD1_in = S.Task('negD1_in', length=1, delay_cost=1)
	negD1_in += alt(MM_in)
	S += negD1_in*MM_in[0]<=negD1*MM[0]
	negD1_mem0 = S.Task('negD1_mem0', length=1, delay_cost=1)
	negD1_mem0 += alt(MAS_MEM)
	S += (D_a_1*MAS[0])-1 < negD1_mem0*MAS_MEM[0]
	S += (D_a_1*MAS[1])-1 < negD1_mem0*MAS_MEM[2]
	S += (D_a_1*MAS[2])-1 < negD1_mem0*MAS_MEM[4]
	S += (D_a_1*MAS[3])-1 < negD1_mem0*MAS_MEM[6]
	S += negD1_mem0 <= negD1

	negD1_mem1 = S.Task('negD1_mem1', length=1, delay_cost=1)
	negD1_mem1 += MAIN_MEM_r[1]
	S += negD1_mem1 <= negD1

	N_b0 = S.Task('N_b0', length=2, delay_cost=1)
	N_b0 += alt(MAS)
	N_b0_in = S.Task('N_b0_in', length=1, delay_cost=1)
	N_b0_in += alt(MAS_in)
	S += N_b0_in*MAS_in[0]<=N_b0*MAS[0]

	S += N_b0_in*MAS_in[1]<=N_b0*MAS[1]

	S += N_b0_in*MAS_in[2]<=N_b0*MAS[2]

	S += N_b0_in*MAS_in[3]<=N_b0*MAS[3]

	N_b0_mem0 = S.Task('N_b0_mem0', length=1, delay_cost=1)
	N_b0_mem0 += alt(MAS_MEM)
	S += (D_a_0*MAS[0])-1 < N_b0_mem0*MAS_MEM[0]
	S += (D_a_0*MAS[1])-1 < N_b0_mem0*MAS_MEM[2]
	S += (D_a_0*MAS[2])-1 < N_b0_mem0*MAS_MEM[4]
	S += (D_a_0*MAS[3])-1 < N_b0_mem0*MAS_MEM[6]
	S += N_b0_mem0 <= N_b0

	N_b0_mem1 = S.Task('N_b0_mem1', length=1, delay_cost=1)
	N_b0_mem1 += MAIN_MEM_r[1]
	S += N_b0_mem1 <= N_b0

	N_b1 = S.Task('N_b1', length=2, delay_cost=1)
	N_b1 += alt(MAS)
	N_b1_in = S.Task('N_b1_in', length=1, delay_cost=1)
	N_b1_in += alt(MAS_in)
	S += N_b1_in*MAS_in[0]<=N_b1*MAS[0]

	S += N_b1_in*MAS_in[1]<=N_b1*MAS[1]

	S += N_b1_in*MAS_in[2]<=N_b1*MAS[2]

	S += N_b1_in*MAS_in[3]<=N_b1*MAS[3]

	N_b1_mem0 = S.Task('N_b1_mem0', length=1, delay_cost=1)
	N_b1_mem0 += alt(MAS_MEM)
	S += (D_a_1*MAS[0])-1 < N_b1_mem0*MAS_MEM[0]
	S += (D_a_1*MAS[1])-1 < N_b1_mem0*MAS_MEM[2]
	S += (D_a_1*MAS[2])-1 < N_b1_mem0*MAS_MEM[4]
	S += (D_a_1*MAS[3])-1 < N_b1_mem0*MAS_MEM[6]
	S += N_b1_mem0 <= N_b1

	N_b1_mem1 = S.Task('N_b1_mem1', length=1, delay_cost=1)
	N_b1_mem1 += MAIN_MEM_r[1]
	S += N_b1_mem1 <= N_b1

	D0 = S.Task('D0', length=2, delay_cost=1)
	D0 += alt(MAS)
	D0_in = S.Task('D0_in', length=1, delay_cost=1)
	D0_in += alt(MAS_in)
	S += D0_in*MAS_in[0]<=D0*MAS[0]

	S += D0_in*MAS_in[1]<=D0*MAS[1]

	S += D0_in*MAS_in[2]<=D0*MAS[2]

	S += D0_in*MAS_in[3]<=D0*MAS[3]

	S += 0<D0

	D0_w = S.Task('D0_w', length=1, delay_cost=1)
	D0_w += alt(MAIN_MEM_w)
	S += D0 <= D0_w

	D0_mem0 = S.Task('D0_mem0', length=1, delay_cost=1)
	D0_mem0 += MAIN_MEM_r[0]
	S += D0_mem0 <= D0

	D0_mem1 = S.Task('D0_mem1', length=1, delay_cost=1)
	D0_mem1 += alt(MM_MEM)
	S += (negD0*MM[0])-1 < D0_mem1*MM_MEM[1]
	S += D0_mem1 <= D0

	D1 = S.Task('D1', length=2, delay_cost=1)
	D1 += alt(MAS)
	D1_in = S.Task('D1_in', length=1, delay_cost=1)
	D1_in += alt(MAS_in)
	S += D1_in*MAS_in[0]<=D1*MAS[0]

	S += D1_in*MAS_in[1]<=D1*MAS[1]

	S += D1_in*MAS_in[2]<=D1*MAS[2]

	S += D1_in*MAS_in[3]<=D1*MAS[3]

	S += 0<D1

	D1_w = S.Task('D1_w', length=1, delay_cost=1)
	D1_w += alt(MAIN_MEM_w)
	S += D1 <= D1_w

	D1_mem0 = S.Task('D1_mem0', length=1, delay_cost=1)
	D1_mem0 += MAIN_MEM_r[0]
	S += D1_mem0 <= D1

	D1_mem1 = S.Task('D1_mem1', length=1, delay_cost=1)
	D1_mem1 += alt(MM_MEM)
	S += (negD1*MM[0])-1 < D1_mem1*MM_MEM[1]
	S += D1_mem1 <= D1

	N0 = S.Task('N0', length=8, delay_cost=1)
	N0 += alt(MM)
	N0_in = S.Task('N0_in', length=1, delay_cost=1)
	N0_in += alt(MM_in)
	S += N0_in*MM_in[0]<=N0*MM[0]
	N0_mem0 = S.Task('N0_mem0', length=1, delay_cost=1)
	N0_mem0 += MAIN_MEM_r[0]
	S += N0_mem0 <= N0

	N0_mem1 = S.Task('N0_mem1', length=1, delay_cost=1)
	N0_mem1 += alt(MAS_MEM)
	S += (N_b0*MAS[0])-1 < N0_mem1*MAS_MEM[1]
	S += (N_b0*MAS[1])-1 < N0_mem1*MAS_MEM[3]
	S += (N_b0*MAS[2])-1 < N0_mem1*MAS_MEM[5]
	S += (N_b0*MAS[3])-1 < N0_mem1*MAS_MEM[7]
	S += N0_mem1 <= N0

	N1 = S.Task('N1', length=8, delay_cost=1)
	N1 += alt(MM)
	N1_in = S.Task('N1_in', length=1, delay_cost=1)
	N1_in += alt(MM_in)
	S += N1_in*MM_in[0]<=N1*MM[0]
	N1_mem0 = S.Task('N1_mem0', length=1, delay_cost=1)
	N1_mem0 += MAIN_MEM_r[0]
	S += N1_mem0 <= N1

	N1_mem1 = S.Task('N1_mem1', length=1, delay_cost=1)
	N1_mem1 += alt(MAS_MEM)
	S += (N_b1*MAS[0])-1 < N1_mem1*MAS_MEM[1]
	S += (N_b1*MAS[1])-1 < N1_mem1*MAS_MEM[3]
	S += (N_b1*MAS[2])-1 < N1_mem1*MAS_MEM[5]
	S += (N_b1*MAS[3])-1 < N1_mem1*MAS_MEM[7]
	S += N1_mem1 <= N1

	Z0 = S.Task('Z0', length=3, delay_cost=1)
	Z0 += alt(CSEL)

	Z0_w = S.Task('Z0_w', length=1, delay_cost=1)
	Z0_w += alt(MAIN_MEM_w)
	S += Z0+2 <= Z0_w

	Z0_mem0 = S.Task('Z0_mem0', length=1, delay_cost=1)
	Z0_mem0 += MAIN_MEM_r[0]
	S += D0_w < Z0_mem0
	S += Z0_mem0+ 2 <= Z0

	Z0_mem1 = S.Task('Z0_mem1', length=1, delay_cost=1)
	Z0_mem1 += MAIN_MEM_r[0]
	S += D0_w < Z0_mem1
	S += Z0_mem1+ 1 <= Z0

	Z0_mem2 = S.Task('Z0_mem2', length=1, delay_cost=1)
	Z0_mem2 += MAIN_MEM_r[0]
	S += Z0_mem2+ 0 <= Z0

	Z1 = S.Task('Z1', length=3, delay_cost=1)
	Z1 += alt(CSEL)

	Z1_w = S.Task('Z1_w', length=1, delay_cost=1)
	Z1_w += alt(MAIN_MEM_w)
	S += Z1+2 <= Z1_w

	Z1_mem0 = S.Task('Z1_mem0', length=1, delay_cost=1)
	Z1_mem0 += MAIN_MEM_r[0]
	S += D1_w < Z1_mem0
	S += Z1_mem0+ 2 <= Z1

	Z1_mem1 = S.Task('Z1_mem1', length=1, delay_cost=1)
	Z1_mem1 += MAIN_MEM_r[0]
	S += D1_w < Z1_mem1
	S += Z1_mem1+ 1 <= Z1

	Z1_mem2 = S.Task('Z1_mem2', length=1, delay_cost=1)
	Z1_mem2 += MAIN_MEM_r[0]
	S += Z1_mem2+ 0 <= Z1

	N20 = S.Task('N20', length=8, delay_cost=1)
	N20 += alt(MM)
	N20_in = S.Task('N20_in', length=1, delay_cost=1)
	N20_in += alt(MM_in)
	S += N20_in*MM_in[0]<=N20*MM[0]
	N20_mem0 = S.Task('N20_mem0', length=1, delay_cost=1)
	N20_mem0 += alt(MM_MEM)
	S += (N0*MM[0])-1 < N20_mem0*MM_MEM[0]
	S += N20_mem0 <= N20

	N20_mem1 = S.Task('N20_mem1', length=1, delay_cost=1)
	N20_mem1 += alt(MM_MEM)
	S += (N0*MM[0])-1 < N20_mem1*MM_MEM[1]
	S += N20_mem1 <= N20

	N21 = S.Task('N21', length=8, delay_cost=1)
	N21 += alt(MM)
	N21_in = S.Task('N21_in', length=1, delay_cost=1)
	N21_in += alt(MM_in)
	S += N21_in*MM_in[0]<=N21*MM[0]
	N21_mem0 = S.Task('N21_mem0', length=1, delay_cost=1)
	N21_mem0 += alt(MM_MEM)
	S += (N1*MM[0])-1 < N21_mem0*MM_MEM[0]
	S += N21_mem0 <= N21

	N21_mem1 = S.Task('N21_mem1', length=1, delay_cost=1)
	N21_mem1 += alt(MM_MEM)
	S += (N1*MM[0])-1 < N21_mem1*MM_MEM[1]
	S += N21_mem1 <= N21

	D20 = S.Task('D20', length=8, delay_cost=1)
	D20 += alt(MM)
	D20_in = S.Task('D20_in', length=1, delay_cost=1)
	D20_in += alt(MM_in)
	S += D20_in*MM_in[0]<=D20*MM[0]
	D20_mem0 = S.Task('D20_mem0', length=1, delay_cost=1)
	D20_mem0 += MAIN_MEM_r[0]
	S += Z0_w < D20_mem0
	S += D20_mem0 <= D20

	D20_mem1 = S.Task('D20_mem1', length=1, delay_cost=1)
	D20_mem1 += MAIN_MEM_r[1]
	S += Z0_w < D20_mem1
	S += D20_mem1 <= D20

	D21 = S.Task('D21', length=8, delay_cost=1)
	D21 += alt(MM)
	D21_in = S.Task('D21_in', length=1, delay_cost=1)
	D21_in += alt(MM_in)
	S += D21_in*MM_in[0]<=D21*MM[0]
	D21_mem0 = S.Task('D21_mem0', length=1, delay_cost=1)
	D21_mem0 += MAIN_MEM_r[0]
	S += Z1_w < D21_mem0
	S += D21_mem0 <= D21

	D21_mem1 = S.Task('D21_mem1', length=1, delay_cost=1)
	D21_mem1 += MAIN_MEM_r[1]
	S += Z1_w < D21_mem1
	S += D21_mem1 <= D21

	N30 = S.Task('N30', length=8, delay_cost=1)
	N30 += alt(MM)
	N30_in = S.Task('N30_in', length=1, delay_cost=1)
	N30_in += alt(MM_in)
	S += N30_in*MM_in[0]<=N30*MM[0]
	N30_mem0 = S.Task('N30_mem0', length=1, delay_cost=1)
	N30_mem0 += alt(MM_MEM)
	S += (N20*MM[0])-1 < N30_mem0*MM_MEM[0]
	S += N30_mem0 <= N30

	N30_mem1 = S.Task('N30_mem1', length=1, delay_cost=1)
	N30_mem1 += alt(MM_MEM)
	S += (N0*MM[0])-1 < N30_mem1*MM_MEM[1]
	S += N30_mem1 <= N30

	N31 = S.Task('N31', length=8, delay_cost=1)
	N31 += alt(MM)
	N31_in = S.Task('N31_in', length=1, delay_cost=1)
	N31_in += alt(MM_in)
	S += N31_in*MM_in[0]<=N31*MM[0]
	N31_mem0 = S.Task('N31_mem0', length=1, delay_cost=1)
	N31_mem0 += alt(MM_MEM)
	S += (N21*MM[0])-1 < N31_mem0*MM_MEM[0]
	S += N31_mem0 <= N31

	N31_mem1 = S.Task('N31_mem1', length=1, delay_cost=1)
	N31_mem1 += alt(MM_MEM)
	S += (N1*MM[0])-1 < N31_mem1*MM_MEM[1]
	S += N31_mem1 <= N31

	V0 = S.Task('V0', length=8, delay_cost=1)
	V0 += alt(MM)
	V0_in = S.Task('V0_in', length=1, delay_cost=1)
	V0_in += alt(MM_in)
	S += V0_in*MM_in[0]<=V0*MM[0]
	V0_mem0 = S.Task('V0_mem0', length=1, delay_cost=1)
	V0_mem0 += alt(MM_MEM)
	S += (D20*MM[0])-1 < V0_mem0*MM_MEM[0]
	S += V0_mem0 <= V0

	V0_mem1 = S.Task('V0_mem1', length=1, delay_cost=1)
	V0_mem1 += MAIN_MEM_r[1]
	S += Z0_w < V0_mem1
	S += V0_mem1 <= V0

	V1 = S.Task('V1', length=8, delay_cost=1)
	V1 += alt(MM)
	V1_in = S.Task('V1_in', length=1, delay_cost=1)
	V1_in += alt(MM_in)
	S += V1_in*MM_in[0]<=V1*MM[0]
	V1_mem0 = S.Task('V1_mem0', length=1, delay_cost=1)
	V1_mem0 += alt(MM_MEM)
	S += (D21*MM[0])-1 < V1_mem0*MM_MEM[0]
	S += V1_mem0 <= V1

	V1_mem1 = S.Task('V1_mem1', length=1, delay_cost=1)
	V1_mem1 += MAIN_MEM_r[1]
	S += Z1_w < V1_mem1
	S += V1_mem1 <= V1

	ND20 = S.Task('ND20', length=8, delay_cost=1)
	ND20 += alt(MM)
	ND20_in = S.Task('ND20_in', length=1, delay_cost=1)
	ND20_in += alt(MM_in)
	S += ND20_in*MM_in[0]<=ND20*MM[0]
	ND20_mem0 = S.Task('ND20_mem0', length=1, delay_cost=1)
	ND20_mem0 += alt(MM_MEM)
	S += (N0*MM[0])-1 < ND20_mem0*MM_MEM[0]
	S += ND20_mem0 <= ND20

	ND20_mem1 = S.Task('ND20_mem1', length=1, delay_cost=1)
	ND20_mem1 += alt(MM_MEM)
	S += (D20*MM[0])-1 < ND20_mem1*MM_MEM[1]
	S += ND20_mem1 <= ND20

	ND21 = S.Task('ND21', length=8, delay_cost=1)
	ND21 += alt(MM)
	ND21_in = S.Task('ND21_in', length=1, delay_cost=1)
	ND21_in += alt(MM_in)
	S += ND21_in*MM_in[0]<=ND21*MM[0]
	ND21_mem0 = S.Task('ND21_mem0', length=1, delay_cost=1)
	ND21_mem0 += alt(MM_MEM)
	S += (N1*MM[0])-1 < ND21_mem0*MM_MEM[0]
	S += ND21_mem0 <= ND21

	ND21_mem1 = S.Task('ND21_mem1', length=1, delay_cost=1)
	ND21_mem1 += alt(MM_MEM)
	S += (D21*MM[0])-1 < ND21_mem1*MM_MEM[1]
	S += ND21_mem1 <= ND21

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage2MAS4/2xSSWU_BEFORE_EXP/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

