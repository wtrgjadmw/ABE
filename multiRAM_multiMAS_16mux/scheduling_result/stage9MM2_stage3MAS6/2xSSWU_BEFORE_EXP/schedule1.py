from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 189
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=9)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 0
	t21_in += MM_in[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 0
	t21_mem0 += MAIN_MEM_r[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 0
	t21_mem1 += MAIN_MEM_r[1]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 1
	t20_in += MM_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 1
	t20_mem0 += MAIN_MEM_r[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 1
	t20_mem1 += MAIN_MEM_r[1]

	t21 = S.Task('t21', length=9, delay_cost=1)
	S += t21 >= 1
	t21 += MM[1]

	t20 = S.Task('t20', length=9, delay_cost=1)
	S += t20 >= 2
	t20 += MM[0]

	xit21_in = S.Task('xit21_in', length=1, delay_cost=1)
	S += xit21_in >= 9
	xit21_in += MAS_in[5]

	xit21_mem0 = S.Task('xit21_mem0', length=1, delay_cost=1)
	S += xit21_mem0 >= 9
	xit21_mem0 += MAIN_MEM_r[0]

	xit21_mem1 = S.Task('xit21_mem1', length=1, delay_cost=1)
	S += xit21_mem1 >= 9
	xit21_mem1 += MM_MEM[3]

	xit20_in = S.Task('xit20_in', length=1, delay_cost=1)
	S += xit20_in >= 10
	xit20_in += MAS_in[0]

	xit20_mem0 = S.Task('xit20_mem0', length=1, delay_cost=1)
	S += xit20_mem0 >= 10
	xit20_mem0 += MAIN_MEM_r[0]

	xit20_mem1 = S.Task('xit20_mem1', length=1, delay_cost=1)
	S += xit20_mem1 >= 10
	xit20_mem1 += MM_MEM[1]

	xit21 = S.Task('xit21', length=3, delay_cost=1)
	S += xit21 >= 10
	xit21 += MAS[5]

	xit20 = S.Task('xit20', length=3, delay_cost=1)
	S += xit20 >= 11
	xit20 += MAS[0]

	xi2t41_in = S.Task('xi2t41_in', length=1, delay_cost=1)
	S += xi2t41_in >= 12
	xi2t41_in += MM_in[0]

	xi2t41_mem0 = S.Task('xi2t41_mem0', length=1, delay_cost=1)
	S += xi2t41_mem0 >= 12
	xi2t41_mem0 += MAS_MEM[10]

	xi2t41_mem1 = S.Task('xi2t41_mem1', length=1, delay_cost=1)
	S += xi2t41_mem1 >= 12
	xi2t41_mem1 += MAS_MEM[11]

	xi2t40_in = S.Task('xi2t40_in', length=1, delay_cost=1)
	S += xi2t40_in >= 13
	xi2t40_in += MM_in[1]

	xi2t40_mem0 = S.Task('xi2t40_mem0', length=1, delay_cost=1)
	S += xi2t40_mem0 >= 13
	xi2t40_mem0 += MAS_MEM[0]

	xi2t40_mem1 = S.Task('xi2t40_mem1', length=1, delay_cost=1)
	S += xi2t40_mem1 >= 13
	xi2t40_mem1 += MAS_MEM[1]

	xi2t41 = S.Task('xi2t41', length=9, delay_cost=1)
	S += xi2t41 >= 13
	xi2t41 += MM[0]

	xi2t40 = S.Task('xi2t40', length=9, delay_cost=1)
	S += xi2t40 >= 14
	xi2t40 += MM[1]

	D_a_1_in = S.Task('D_a_1_in', length=1, delay_cost=1)
	S += D_a_1_in >= 21
	D_a_1_in += MAS_in[0]

	D_a_1_mem0 = S.Task('D_a_1_mem0', length=1, delay_cost=1)
	S += D_a_1_mem0 >= 21
	D_a_1_mem0 += MAS_MEM[10]

	D_a_1_mem1 = S.Task('D_a_1_mem1', length=1, delay_cost=1)
	S += D_a_1_mem1 >= 21
	D_a_1_mem1 += MM_MEM[1]

	D_a_0_in = S.Task('D_a_0_in', length=1, delay_cost=1)
	S += D_a_0_in >= 22
	D_a_0_in += MAS_in[0]

	D_a_0_mem0 = S.Task('D_a_0_mem0', length=1, delay_cost=1)
	S += D_a_0_mem0 >= 22
	D_a_0_mem0 += MAS_MEM[0]

	D_a_0_mem1 = S.Task('D_a_0_mem1', length=1, delay_cost=1)
	S += D_a_0_mem1 >= 22
	D_a_0_mem1 += MM_MEM[3]

	D_a_1 = S.Task('D_a_1', length=3, delay_cost=1)
	S += D_a_1 >= 22
	D_a_1 += MAS[0]

	D_a_0 = S.Task('D_a_0', length=3, delay_cost=1)
	S += D_a_0 >= 23
	D_a_0 += MAS[0]

	negD1_in = S.Task('negD1_in', length=1, delay_cost=1)
	S += negD1_in >= 24
	negD1_in += MM_in[1]

	negD1_mem0 = S.Task('negD1_mem0', length=1, delay_cost=1)
	S += negD1_mem0 >= 24
	negD1_mem0 += MAS_MEM[0]

	negD1_mem1 = S.Task('negD1_mem1', length=1, delay_cost=1)
	S += negD1_mem1 >= 24
	negD1_mem1 += MAIN_MEM_r[1]

	N_b0_in = S.Task('N_b0_in', length=1, delay_cost=1)
	S += N_b0_in >= 25
	N_b0_in += MAS_in[0]

	N_b0_mem0 = S.Task('N_b0_mem0', length=1, delay_cost=1)
	S += N_b0_mem0 >= 25
	N_b0_mem0 += MAS_MEM[0]

	N_b0_mem1 = S.Task('N_b0_mem1', length=1, delay_cost=1)
	S += N_b0_mem1 >= 25
	N_b0_mem1 += MAIN_MEM_r[1]

	negD1 = S.Task('negD1', length=9, delay_cost=1)
	S += negD1 >= 25
	negD1 += MM[1]

	N_b0 = S.Task('N_b0', length=3, delay_cost=1)
	S += N_b0 >= 26
	N_b0 += MAS[0]

	N_b1_in = S.Task('N_b1_in', length=1, delay_cost=1)
	S += N_b1_in >= 26
	N_b1_in += MAS_in[4]

	N_b1_mem0 = S.Task('N_b1_mem0', length=1, delay_cost=1)
	S += N_b1_mem0 >= 26
	N_b1_mem0 += MAS_MEM[0]

	N_b1_mem1 = S.Task('N_b1_mem1', length=1, delay_cost=1)
	S += N_b1_mem1 >= 26
	N_b1_mem1 += MAIN_MEM_r[1]

	N_b1 = S.Task('N_b1', length=3, delay_cost=1)
	S += N_b1 >= 27
	N_b1 += MAS[4]

	negD0_in = S.Task('negD0_in', length=1, delay_cost=1)
	S += negD0_in >= 27
	negD0_in += MM_in[1]

	negD0_mem0 = S.Task('negD0_mem0', length=1, delay_cost=1)
	S += negD0_mem0 >= 27
	negD0_mem0 += MAS_MEM[0]

	negD0_mem1 = S.Task('negD0_mem1', length=1, delay_cost=1)
	S += negD0_mem1 >= 27
	negD0_mem1 += MAIN_MEM_r[1]

	N0_in = S.Task('N0_in', length=1, delay_cost=1)
	S += N0_in >= 28
	N0_in += MM_in[0]

	N0_mem0 = S.Task('N0_mem0', length=1, delay_cost=1)
	S += N0_mem0 >= 28
	N0_mem0 += MAIN_MEM_r[0]

	N0_mem1 = S.Task('N0_mem1', length=1, delay_cost=1)
	S += N0_mem1 >= 28
	N0_mem1 += MAS_MEM[1]

	negD0 = S.Task('negD0', length=9, delay_cost=1)
	S += negD0 >= 28
	negD0 += MM[1]

	N0 = S.Task('N0', length=9, delay_cost=1)
	S += N0 >= 29
	N0 += MM[0]

	N1_in = S.Task('N1_in', length=1, delay_cost=1)
	S += N1_in >= 29
	N1_in += MM_in[1]

	N1_mem0 = S.Task('N1_mem0', length=1, delay_cost=1)
	S += N1_mem0 >= 29
	N1_mem0 += MAIN_MEM_r[0]

	N1_mem1 = S.Task('N1_mem1', length=1, delay_cost=1)
	S += N1_mem1 >= 29
	N1_mem1 += MAS_MEM[9]

	N1 = S.Task('N1', length=9, delay_cost=1)
	S += N1 >= 30
	N1 += MM[1]

	D1_in = S.Task('D1_in', length=1, delay_cost=1)
	S += D1_in >= 33
	D1_in += MAS_in[0]

	D1_mem0 = S.Task('D1_mem0', length=1, delay_cost=1)
	S += D1_mem0 >= 33
	D1_mem0 += MAIN_MEM_r[0]

	D1_mem1 = S.Task('D1_mem1', length=1, delay_cost=1)
	S += D1_mem1 >= 33
	D1_mem1 += MM_MEM[3]

	D1 = S.Task('D1', length=3, delay_cost=1)
	S += D1 >= 34
	D1 += MAS[0]

	D0_in = S.Task('D0_in', length=1, delay_cost=1)
	S += D0_in >= 36
	D0_in += MAS_in[5]

	D0_mem0 = S.Task('D0_mem0', length=1, delay_cost=1)
	S += D0_mem0 >= 36
	D0_mem0 += MAIN_MEM_r[0]

	D0_mem1 = S.Task('D0_mem1', length=1, delay_cost=1)
	S += D0_mem1 >= 36
	D0_mem1 += MM_MEM[3]

	D0 = S.Task('D0', length=3, delay_cost=1)
	S += D0 >= 37
	D0 += MAS[5]

	D1_w = S.Task('D1_w', length=1, delay_cost=1)
	S += D1_w >= 37
	D1_w += MAIN_MEM_w

	N20_in = S.Task('N20_in', length=1, delay_cost=1)
	S += N20_in >= 37
	N20_in += MM_in[0]

	N20_mem0 = S.Task('N20_mem0', length=1, delay_cost=1)
	S += N20_mem0 >= 37
	N20_mem0 += MM_MEM[0]

	N20_mem1 = S.Task('N20_mem1', length=1, delay_cost=1)
	S += N20_mem1 >= 37
	N20_mem1 += MM_MEM[1]

	N20 = S.Task('N20', length=9, delay_cost=1)
	S += N20 >= 38
	N20 += MM[0]

	N21_in = S.Task('N21_in', length=1, delay_cost=1)
	S += N21_in >= 38
	N21_in += MM_in[0]

	N21_mem0 = S.Task('N21_mem0', length=1, delay_cost=1)
	S += N21_mem0 >= 38
	N21_mem0 += MM_MEM[2]

	N21_mem1 = S.Task('N21_mem1', length=1, delay_cost=1)
	S += N21_mem1 >= 38
	N21_mem1 += MM_MEM[3]

	Z1_mem0 = S.Task('Z1_mem0', length=1, delay_cost=1)
	S += Z1_mem0 >= 38
	Z1_mem0 += MAIN_MEM_r[0]

	N21 = S.Task('N21', length=9, delay_cost=1)
	S += N21 >= 39
	N21 += MM[0]

	Z1_mem1 = S.Task('Z1_mem1', length=1, delay_cost=1)
	S += Z1_mem1 >= 39
	Z1_mem1 += MAIN_MEM_r[0]

	D0_w = S.Task('D0_w', length=1, delay_cost=1)
	S += D0_w >= 40
	D0_w += MAIN_MEM_w

	Z1_mem2 = S.Task('Z1_mem2', length=1, delay_cost=1)
	S += Z1_mem2 >= 40
	Z1_mem2 += MAIN_MEM_r[0]

	Z0_mem0 = S.Task('Z0_mem0', length=1, delay_cost=1)
	S += Z0_mem0 >= 41
	Z0_mem0 += MAIN_MEM_r[0]

	Z1 = S.Task('Z1', length=3, delay_cost=1)
	S += Z1 >= 41
	Z1 += CSEL

	Z0_mem1 = S.Task('Z0_mem1', length=1, delay_cost=1)
	S += Z0_mem1 >= 42
	Z0_mem1 += MAIN_MEM_r[0]

	Z0_mem2 = S.Task('Z0_mem2', length=1, delay_cost=1)
	S += Z0_mem2 >= 43
	Z0_mem2 += MAIN_MEM_r[0]

	Z0 = S.Task('Z0', length=3, delay_cost=1)
	S += Z0 >= 44
	Z0 += CSEL

	N30_in = S.Task('N30_in', length=1, delay_cost=1)
	S += N30_in >= 46
	N30_in += MM_in[1]

	N30_mem0 = S.Task('N30_mem0', length=1, delay_cost=1)
	S += N30_mem0 >= 46
	N30_mem0 += MM_MEM[0]

	N30_mem1 = S.Task('N30_mem1', length=1, delay_cost=1)
	S += N30_mem1 >= 46
	N30_mem1 += MM_MEM[1]

	Z1_w = S.Task('Z1_w', length=1, delay_cost=1)
	S += Z1_w >= 46
	Z1_w += MAIN_MEM_w

	D21_in = S.Task('D21_in', length=1, delay_cost=1)
	S += D21_in >= 47
	D21_in += MM_in[0]

	D21_mem0 = S.Task('D21_mem0', length=1, delay_cost=1)
	S += D21_mem0 >= 47
	D21_mem0 += MAIN_MEM_r[0]

	D21_mem1 = S.Task('D21_mem1', length=1, delay_cost=1)
	S += D21_mem1 >= 47
	D21_mem1 += MAIN_MEM_r[1]

	N30 = S.Task('N30', length=9, delay_cost=1)
	S += N30 >= 47
	N30 += MM[1]

	N31_in = S.Task('N31_in', length=1, delay_cost=1)
	S += N31_in >= 47
	N31_in += MM_in[1]

	N31_mem0 = S.Task('N31_mem0', length=1, delay_cost=1)
	S += N31_mem0 >= 47
	N31_mem0 += MM_MEM[0]

	N31_mem1 = S.Task('N31_mem1', length=1, delay_cost=1)
	S += N31_mem1 >= 47
	N31_mem1 += MM_MEM[3]

	D21 = S.Task('D21', length=9, delay_cost=1)
	S += D21 >= 48
	D21 += MM[0]

	N31 = S.Task('N31', length=9, delay_cost=1)
	S += N31 >= 48
	N31 += MM[1]

	Z0_w = S.Task('Z0_w', length=1, delay_cost=1)
	S += Z0_w >= 49
	Z0_w += MAIN_MEM_w

	D20_in = S.Task('D20_in', length=1, delay_cost=1)
	S += D20_in >= 50
	D20_in += MM_in[1]

	D20_mem0 = S.Task('D20_mem0', length=1, delay_cost=1)
	S += D20_mem0 >= 50
	D20_mem0 += MAIN_MEM_r[0]

	D20_mem1 = S.Task('D20_mem1', length=1, delay_cost=1)
	S += D20_mem1 >= 50
	D20_mem1 += MAIN_MEM_r[1]

	D20 = S.Task('D20', length=9, delay_cost=1)
	S += D20 >= 51
	D20 += MM[1]

	ND21_in = S.Task('ND21_in', length=1, delay_cost=1)
	S += ND21_in >= 56
	ND21_in += MM_in[0]

	ND21_mem0 = S.Task('ND21_mem0', length=1, delay_cost=1)
	S += ND21_mem0 >= 56
	ND21_mem0 += MM_MEM[2]

	ND21_mem1 = S.Task('ND21_mem1', length=1, delay_cost=1)
	S += ND21_mem1 >= 56
	ND21_mem1 += MM_MEM[1]

	V1_in = S.Task('V1_in', length=1, delay_cost=1)
	S += V1_in >= 56
	V1_in += MM_in[1]

	V1_mem0 = S.Task('V1_mem0', length=1, delay_cost=1)
	S += V1_mem0 >= 56
	V1_mem0 += MM_MEM[0]

	V1_mem1 = S.Task('V1_mem1', length=1, delay_cost=1)
	S += V1_mem1 >= 56
	V1_mem1 += MAIN_MEM_r[1]

	ND21 = S.Task('ND21', length=9, delay_cost=1)
	S += ND21 >= 57
	ND21 += MM[0]

	V1 = S.Task('V1', length=9, delay_cost=1)
	S += V1 >= 57
	V1 += MM[1]

	ND20_in = S.Task('ND20_in', length=1, delay_cost=1)
	S += ND20_in >= 59
	ND20_in += MM_in[0]

	ND20_mem0 = S.Task('ND20_mem0', length=1, delay_cost=1)
	S += ND20_mem0 >= 59
	ND20_mem0 += MM_MEM[0]

	ND20_mem1 = S.Task('ND20_mem1', length=1, delay_cost=1)
	S += ND20_mem1 >= 59
	ND20_mem1 += MM_MEM[3]

	V0_in = S.Task('V0_in', length=1, delay_cost=1)
	S += V0_in >= 59
	V0_in += MM_in[1]

	V0_mem0 = S.Task('V0_mem0', length=1, delay_cost=1)
	S += V0_mem0 >= 59
	V0_mem0 += MM_MEM[2]

	V0_mem1 = S.Task('V0_mem1', length=1, delay_cost=1)
	S += V0_mem1 >= 59
	V0_mem1 += MAIN_MEM_r[1]

	ND20 = S.Task('ND20', length=9, delay_cost=1)
	S += ND20 >= 60
	ND20 += MM[0]

	V0 = S.Task('V0', length=9, delay_cost=1)
	S += V0 >= 60
	V0 += MM[1]


	# new tasks
	aND20 = S.Task('aND20', length=9, delay_cost=1)
	aND20 += alt(MM)
	aND20_in = S.Task('aND20_in', length=1, delay_cost=1)
	aND20_in += alt(MM_in)
	S += aND20_in*MM_in[0]<=aND20*MM[0]
	S += aND20_in*MM_in[1]<=aND20*MM[1]
	aND20_mem0 = S.Task('aND20_mem0', length=1, delay_cost=1)
	aND20_mem0 += MAIN_MEM_r[0]
	S += aND20_mem0 <= aND20

	aND20_mem1 = S.Task('aND20_mem1', length=1, delay_cost=1)
	aND20_mem1 += MM_MEM[1]
	S += 68 < aND20_mem1
	S += aND20_mem1 <= aND20

	aND21 = S.Task('aND21', length=9, delay_cost=1)
	aND21 += alt(MM)
	aND21_in = S.Task('aND21_in', length=1, delay_cost=1)
	aND21_in += alt(MM_in)
	S += aND21_in*MM_in[0]<=aND21*MM[0]
	S += aND21_in*MM_in[1]<=aND21*MM[1]
	aND21_mem0 = S.Task('aND21_mem0', length=1, delay_cost=1)
	aND21_mem0 += MAIN_MEM_r[0]
	S += aND21_mem0 <= aND21

	aND21_mem1 = S.Task('aND21_mem1', length=1, delay_cost=1)
	aND21_mem1 += MM_MEM[1]
	S += 65 < aND21_mem1
	S += aND21_mem1 <= aND21

	bD30 = S.Task('bD30', length=9, delay_cost=1)
	bD30 += alt(MM)
	bD30_in = S.Task('bD30_in', length=1, delay_cost=1)
	bD30_in += alt(MM_in)
	S += bD30_in*MM_in[0]<=bD30*MM[0]
	S += bD30_in*MM_in[1]<=bD30*MM[1]
	bD30_mem0 = S.Task('bD30_mem0', length=1, delay_cost=1)
	bD30_mem0 += MAIN_MEM_r[0]
	S += bD30_mem0 <= bD30

	bD30_mem1 = S.Task('bD30_mem1', length=1, delay_cost=1)
	bD30_mem1 += MM_MEM[3]
	S += 68 < bD30_mem1
	S += bD30_mem1 <= bD30

	bD31 = S.Task('bD31', length=9, delay_cost=1)
	bD31 += alt(MM)
	bD31_in = S.Task('bD31_in', length=1, delay_cost=1)
	bD31_in += alt(MM_in)
	S += bD31_in*MM_in[0]<=bD31*MM[0]
	S += bD31_in*MM_in[1]<=bD31*MM[1]
	bD31_mem0 = S.Task('bD31_mem0', length=1, delay_cost=1)
	bD31_mem0 += MAIN_MEM_r[0]
	S += bD31_mem0 <= bD31

	bD31_mem1 = S.Task('bD31_mem1', length=1, delay_cost=1)
	bD31_mem1 += MM_MEM[3]
	S += 65 < bD31_mem1
	S += bD31_mem1 <= bD31

	V20 = S.Task('V20', length=9, delay_cost=1)
	V20 += alt(MM)
	V20_in = S.Task('V20_in', length=1, delay_cost=1)
	V20_in += alt(MM_in)
	S += V20_in*MM_in[0]<=V20*MM[0]
	S += V20_in*MM_in[1]<=V20*MM[1]
	V20_mem0 = S.Task('V20_mem0', length=1, delay_cost=1)
	V20_mem0 += MM_MEM[2]
	S += 68 < V20_mem0
	S += V20_mem0 <= V20

	V20_mem1 = S.Task('V20_mem1', length=1, delay_cost=1)
	V20_mem1 += MM_MEM[3]
	S += 68 < V20_mem1
	S += V20_mem1 <= V20

	V21 = S.Task('V21', length=9, delay_cost=1)
	V21 += alt(MM)
	V21_in = S.Task('V21_in', length=1, delay_cost=1)
	V21_in += alt(MM_in)
	S += V21_in*MM_in[0]<=V21*MM[0]
	S += V21_in*MM_in[1]<=V21*MM[1]
	V21_mem0 = S.Task('V21_mem0', length=1, delay_cost=1)
	V21_mem0 += MM_MEM[2]
	S += 65 < V21_mem0
	S += V21_mem0 <= V21

	V21_mem1 = S.Task('V21_mem1', length=1, delay_cost=1)
	V21_mem1 += MM_MEM[3]
	S += 65 < V21_mem1
	S += V21_mem1 <= V21

	U_0 = S.Task('U_0', length=3, delay_cost=1)
	U_0 += alt(MAS)
	U_0_in = S.Task('U_0_in', length=1, delay_cost=1)
	U_0_in += alt(MAS_in)
	S += U_0_in*MAS_in[0]<=U_0*MAS[0]

	S += U_0_in*MAS_in[1]<=U_0*MAS[1]

	S += U_0_in*MAS_in[2]<=U_0*MAS[2]

	S += U_0_in*MAS_in[3]<=U_0*MAS[3]

	S += U_0_in*MAS_in[4]<=U_0*MAS[4]

	S += U_0_in*MAS_in[5]<=U_0*MAS[5]

	U_0_mem0 = S.Task('U_0_mem0', length=1, delay_cost=1)
	U_0_mem0 += MM_MEM[2]
	S += 55 < U_0_mem0
	S += U_0_mem0 <= U_0

	U_0_mem1 = S.Task('U_0_mem1', length=1, delay_cost=1)
	U_0_mem1 += alt(MM_MEM)
	S += (aND20*MM[0])-1 < U_0_mem1*MM_MEM[1]
	S += (aND20*MM[1])-1 < U_0_mem1*MM_MEM[3]
	S += U_0_mem1 <= U_0

	U_1 = S.Task('U_1', length=3, delay_cost=1)
	U_1 += alt(MAS)
	U_1_in = S.Task('U_1_in', length=1, delay_cost=1)
	U_1_in += alt(MAS_in)
	S += U_1_in*MAS_in[0]<=U_1*MAS[0]

	S += U_1_in*MAS_in[1]<=U_1*MAS[1]

	S += U_1_in*MAS_in[2]<=U_1*MAS[2]

	S += U_1_in*MAS_in[3]<=U_1*MAS[3]

	S += U_1_in*MAS_in[4]<=U_1*MAS[4]

	S += U_1_in*MAS_in[5]<=U_1*MAS[5]

	U_1_mem0 = S.Task('U_1_mem0', length=1, delay_cost=1)
	U_1_mem0 += MM_MEM[2]
	S += 56 < U_1_mem0
	S += U_1_mem0 <= U_1

	U_1_mem1 = S.Task('U_1_mem1', length=1, delay_cost=1)
	U_1_mem1 += alt(MM_MEM)
	S += (aND21*MM[0])-1 < U_1_mem1*MM_MEM[1]
	S += (aND21*MM[1])-1 < U_1_mem1*MM_MEM[3]
	S += U_1_mem1 <= U_1

	U0 = S.Task('U0', length=3, delay_cost=1)
	U0 += alt(MAS)
	U0_in = S.Task('U0_in', length=1, delay_cost=1)
	U0_in += alt(MAS_in)
	S += U0_in*MAS_in[0]<=U0*MAS[0]

	S += U0_in*MAS_in[1]<=U0*MAS[1]

	S += U0_in*MAS_in[2]<=U0*MAS[2]

	S += U0_in*MAS_in[3]<=U0*MAS[3]

	S += U0_in*MAS_in[4]<=U0*MAS[4]

	S += U0_in*MAS_in[5]<=U0*MAS[5]

	U0_mem0 = S.Task('U0_mem0', length=1, delay_cost=1)
	U0_mem0 += alt(MAS_MEM)
	S += (U_0*MAS[0])-1 < U0_mem0*MAS_MEM[0]
	S += (U_0*MAS[1])-1 < U0_mem0*MAS_MEM[2]
	S += (U_0*MAS[2])-1 < U0_mem0*MAS_MEM[4]
	S += (U_0*MAS[3])-1 < U0_mem0*MAS_MEM[6]
	S += (U_0*MAS[4])-1 < U0_mem0*MAS_MEM[8]
	S += (U_0*MAS[5])-1 < U0_mem0*MAS_MEM[10]
	S += U0_mem0 <= U0

	U0_mem1 = S.Task('U0_mem1', length=1, delay_cost=1)
	U0_mem1 += alt(MM_MEM)
	S += (bD30*MM[0])-1 < U0_mem1*MM_MEM[1]
	S += (bD30*MM[1])-1 < U0_mem1*MM_MEM[3]
	S += U0_mem1 <= U0

	U1 = S.Task('U1', length=3, delay_cost=1)
	U1 += alt(MAS)
	U1_in = S.Task('U1_in', length=1, delay_cost=1)
	U1_in += alt(MAS_in)
	S += U1_in*MAS_in[0]<=U1*MAS[0]

	S += U1_in*MAS_in[1]<=U1*MAS[1]

	S += U1_in*MAS_in[2]<=U1*MAS[2]

	S += U1_in*MAS_in[3]<=U1*MAS[3]

	S += U1_in*MAS_in[4]<=U1*MAS[4]

	S += U1_in*MAS_in[5]<=U1*MAS[5]

	U1_mem0 = S.Task('U1_mem0', length=1, delay_cost=1)
	U1_mem0 += alt(MAS_MEM)
	S += (U_1*MAS[0])-1 < U1_mem0*MAS_MEM[0]
	S += (U_1*MAS[1])-1 < U1_mem0*MAS_MEM[2]
	S += (U_1*MAS[2])-1 < U1_mem0*MAS_MEM[4]
	S += (U_1*MAS[3])-1 < U1_mem0*MAS_MEM[6]
	S += (U_1*MAS[4])-1 < U1_mem0*MAS_MEM[8]
	S += (U_1*MAS[5])-1 < U1_mem0*MAS_MEM[10]
	S += U1_mem0 <= U1

	U1_mem1 = S.Task('U1_mem1', length=1, delay_cost=1)
	U1_mem1 += alt(MM_MEM)
	S += (bD31*MM[0])-1 < U1_mem1*MM_MEM[1]
	S += (bD31*MM[1])-1 < U1_mem1*MM_MEM[3]
	S += U1_mem1 <= U1

	UV0 = S.Task('UV0', length=9, delay_cost=1)
	UV0 += alt(MM)
	UV0_in = S.Task('UV0_in', length=1, delay_cost=1)
	UV0_in += alt(MM_in)
	S += UV0_in*MM_in[0]<=UV0*MM[0]
	S += UV0_in*MM_in[1]<=UV0*MM[1]
	UV0_mem0 = S.Task('UV0_mem0', length=1, delay_cost=1)
	UV0_mem0 += alt(MAS_MEM)
	S += (U0*MAS[0])-1 < UV0_mem0*MAS_MEM[0]
	S += (U0*MAS[1])-1 < UV0_mem0*MAS_MEM[2]
	S += (U0*MAS[2])-1 < UV0_mem0*MAS_MEM[4]
	S += (U0*MAS[3])-1 < UV0_mem0*MAS_MEM[6]
	S += (U0*MAS[4])-1 < UV0_mem0*MAS_MEM[8]
	S += (U0*MAS[5])-1 < UV0_mem0*MAS_MEM[10]
	S += UV0_mem0 <= UV0

	UV0_mem1 = S.Task('UV0_mem1', length=1, delay_cost=1)
	UV0_mem1 += MM_MEM[3]
	S += 68 < UV0_mem1
	S += UV0_mem1 <= UV0

	UV1 = S.Task('UV1', length=9, delay_cost=1)
	UV1 += alt(MM)
	UV1_in = S.Task('UV1_in', length=1, delay_cost=1)
	UV1_in += alt(MM_in)
	S += UV1_in*MM_in[0]<=UV1*MM[0]
	S += UV1_in*MM_in[1]<=UV1*MM[1]
	UV1_mem0 = S.Task('UV1_mem0', length=1, delay_cost=1)
	UV1_mem0 += alt(MAS_MEM)
	S += (U1*MAS[0])-1 < UV1_mem0*MAS_MEM[0]
	S += (U1*MAS[1])-1 < UV1_mem0*MAS_MEM[2]
	S += (U1*MAS[2])-1 < UV1_mem0*MAS_MEM[4]
	S += (U1*MAS[3])-1 < UV1_mem0*MAS_MEM[6]
	S += (U1*MAS[4])-1 < UV1_mem0*MAS_MEM[8]
	S += (U1*MAS[5])-1 < UV1_mem0*MAS_MEM[10]
	S += UV1_mem0 <= UV1

	UV1_mem1 = S.Task('UV1_mem1', length=1, delay_cost=1)
	UV1_mem1 += MM_MEM[3]
	S += 65 < UV1_mem1
	S += UV1_mem1 <= UV1

	UV30 = S.Task('UV30', length=9, delay_cost=1)
	UV30 += alt(MM)
	UV30_in = S.Task('UV30_in', length=1, delay_cost=1)
	UV30_in += alt(MM_in)
	S += UV30_in*MM_in[0]<=UV30*MM[0]
	S += UV30_in*MM_in[1]<=UV30*MM[1]
	S += 0<UV30

	UV30_w = S.Task('UV30_w', length=1, delay_cost=1)
	UV30_w += alt(MAIN_MEM_w)
	S += UV30 <= UV30_w

	UV30_mem0 = S.Task('UV30_mem0', length=1, delay_cost=1)
	UV30_mem0 += alt(MM_MEM)
	S += (UV0*MM[0])-1 < UV30_mem0*MM_MEM[0]
	S += (UV0*MM[1])-1 < UV30_mem0*MM_MEM[2]
	S += UV30_mem0 <= UV30

	UV30_mem1 = S.Task('UV30_mem1', length=1, delay_cost=1)
	UV30_mem1 += alt(MM_MEM)
	S += (V20*MM[0])-1 < UV30_mem1*MM_MEM[1]
	S += (V20*MM[1])-1 < UV30_mem1*MM_MEM[3]
	S += UV30_mem1 <= UV30

	UV31 = S.Task('UV31', length=9, delay_cost=1)
	UV31 += alt(MM)
	UV31_in = S.Task('UV31_in', length=1, delay_cost=1)
	UV31_in += alt(MM_in)
	S += UV31_in*MM_in[0]<=UV31*MM[0]
	S += UV31_in*MM_in[1]<=UV31*MM[1]
	S += 0<UV31

	UV31_w = S.Task('UV31_w', length=1, delay_cost=1)
	UV31_w += alt(MAIN_MEM_w)
	S += UV31 <= UV31_w

	UV31_mem0 = S.Task('UV31_mem0', length=1, delay_cost=1)
	UV31_mem0 += alt(MM_MEM)
	S += (UV1*MM[0])-1 < UV31_mem0*MM_MEM[0]
	S += (UV1*MM[1])-1 < UV31_mem0*MM_MEM[2]
	S += UV31_mem0 <= UV31

	UV31_mem1 = S.Task('UV31_mem1', length=1, delay_cost=1)
	UV31_mem1 += alt(MM_MEM)
	S += (V21*MM[0])-1 < UV31_mem1*MM_MEM[1]
	S += (V21*MM[1])-1 < UV31_mem1*MM_MEM[3]
	S += UV31_mem1 <= UV31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM2_stage3MAS6/2xSSWU_BEFORE_EXP/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

