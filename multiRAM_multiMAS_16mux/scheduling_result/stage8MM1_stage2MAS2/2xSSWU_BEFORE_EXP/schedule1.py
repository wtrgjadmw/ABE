from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 188
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=2, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 0
	t20_in += MM_in[0]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 0
	t20_mem0 += MAIN_MEM_r[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 0
	t20_mem1 += MAIN_MEM_r[1]

	t20 = S.Task('t20', length=8, delay_cost=1)
	S += t20 >= 1
	t20 += MM[0]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 1
	t21_in += MM_in[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 1
	t21_mem0 += MAIN_MEM_r[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 1
	t21_mem1 += MAIN_MEM_r[1]

	t21 = S.Task('t21', length=8, delay_cost=1)
	S += t21 >= 2
	t21 += MM[0]

	xit20_in = S.Task('xit20_in', length=1, delay_cost=1)
	S += xit20_in >= 8
	xit20_in += MM_in[0]

	xit20_mem0 = S.Task('xit20_mem0', length=1, delay_cost=1)
	S += xit20_mem0 >= 8
	xit20_mem0 += MAIN_MEM_r[0]

	xit20_mem1 = S.Task('xit20_mem1', length=1, delay_cost=1)
	S += xit20_mem1 >= 8
	xit20_mem1 += MM_MEM[1]

	t20_w = S.Task('t20_w', length=1, delay_cost=1)
	S += t20_w >= 9
	t20_w += MAIN_MEM_w

	xit20 = S.Task('xit20', length=8, delay_cost=1)
	S += xit20 >= 9
	xit20 += MM[0]

	xit21_in = S.Task('xit21_in', length=1, delay_cost=1)
	S += xit21_in >= 9
	xit21_in += MM_in[0]

	xit21_mem0 = S.Task('xit21_mem0', length=1, delay_cost=1)
	S += xit21_mem0 >= 9
	xit21_mem0 += MAIN_MEM_r[0]

	xit21_mem1 = S.Task('xit21_mem1', length=1, delay_cost=1)
	S += xit21_mem1 >= 9
	xit21_mem1 += MM_MEM[1]

	t21_w = S.Task('t21_w', length=1, delay_cost=1)
	S += t21_w >= 10
	t21_w += MAIN_MEM_w

	xit21 = S.Task('xit21', length=8, delay_cost=1)
	S += xit21 >= 10
	xit21 += MM[0]

	xi2t40_in = S.Task('xi2t40_in', length=1, delay_cost=1)
	S += xi2t40_in >= 16
	xi2t40_in += MM_in[0]

	xi2t40_mem0 = S.Task('xi2t40_mem0', length=1, delay_cost=1)
	S += xi2t40_mem0 >= 16
	xi2t40_mem0 += MM_MEM[0]

	xi2t40_mem1 = S.Task('xi2t40_mem1', length=1, delay_cost=1)
	S += xi2t40_mem1 >= 16
	xi2t40_mem1 += MM_MEM[1]

	xi2t40 = S.Task('xi2t40', length=8, delay_cost=1)
	S += xi2t40 >= 17
	xi2t40 += MM[0]

	xi2t41_in = S.Task('xi2t41_in', length=1, delay_cost=1)
	S += xi2t41_in >= 17
	xi2t41_in += MM_in[0]

	xi2t41_mem0 = S.Task('xi2t41_mem0', length=1, delay_cost=1)
	S += xi2t41_mem0 >= 17
	xi2t41_mem0 += MM_MEM[0]

	xi2t41_mem1 = S.Task('xi2t41_mem1', length=1, delay_cost=1)
	S += xi2t41_mem1 >= 17
	xi2t41_mem1 += MM_MEM[1]

	xit20_w = S.Task('xit20_w', length=1, delay_cost=1)
	S += xit20_w >= 17
	xit20_w += MAIN_MEM_w

	xi2t41 = S.Task('xi2t41', length=8, delay_cost=1)
	S += xi2t41 >= 18
	xi2t41 += MM[0]

	xit21_w = S.Task('xit21_w', length=1, delay_cost=1)
	S += xit21_w >= 18
	xit21_w += MAIN_MEM_w

	D_a_0_in = S.Task('D_a_0_in', length=1, delay_cost=1)
	S += D_a_0_in >= 24
	D_a_0_in += MAS_in[1]

	D_a_0_mem0 = S.Task('D_a_0_mem0', length=1, delay_cost=1)
	S += D_a_0_mem0 >= 24
	D_a_0_mem0 += MM_MEM[0]

	D_a_0_mem1 = S.Task('D_a_0_mem1', length=1, delay_cost=1)
	S += D_a_0_mem1 >= 24
	D_a_0_mem1 += MM_MEM[1]

	D_a_0 = S.Task('D_a_0', length=2, delay_cost=1)
	S += D_a_0 >= 25
	D_a_0 += MAS[1]

	D_a_1_in = S.Task('D_a_1_in', length=1, delay_cost=1)
	S += D_a_1_in >= 25
	D_a_1_in += MAS_in[1]

	D_a_1_mem0 = S.Task('D_a_1_mem0', length=1, delay_cost=1)
	S += D_a_1_mem0 >= 25
	D_a_1_mem0 += MM_MEM[0]

	D_a_1_mem1 = S.Task('D_a_1_mem1', length=1, delay_cost=1)
	S += D_a_1_mem1 >= 25
	D_a_1_mem1 += MM_MEM[1]

	D0_in = S.Task('D0_in', length=1, delay_cost=1)
	S += D0_in >= 26
	D0_in += MM_in[0]

	D0_mem0 = S.Task('D0_mem0', length=1, delay_cost=1)
	S += D0_mem0 >= 26
	D0_mem0 += MAS_MEM[2]

	D0_mem1 = S.Task('D0_mem1', length=1, delay_cost=1)
	S += D0_mem1 >= 26
	D0_mem1 += MAIN_MEM_r[1]

	D_a_1 = S.Task('D_a_1', length=2, delay_cost=1)
	S += D_a_1 >= 26
	D_a_1 += MAS[1]

	D0 = S.Task('D0', length=8, delay_cost=1)
	S += D0 >= 27
	D0 += MM[0]

	N_b0_in = S.Task('N_b0_in', length=1, delay_cost=1)
	S += N_b0_in >= 27
	N_b0_in += MAS_in[0]

	N_b0_mem0 = S.Task('N_b0_mem0', length=1, delay_cost=1)
	S += N_b0_mem0 >= 27
	N_b0_mem0 += MAS_MEM[2]

	N_b0_mem1 = S.Task('N_b0_mem1', length=1, delay_cost=1)
	S += N_b0_mem1 >= 27
	N_b0_mem1 += MAIN_MEM_r[1]

	D1_in = S.Task('D1_in', length=1, delay_cost=1)
	S += D1_in >= 28
	D1_in += MM_in[0]

	D1_mem0 = S.Task('D1_mem0', length=1, delay_cost=1)
	S += D1_mem0 >= 28
	D1_mem0 += MAS_MEM[2]

	D1_mem1 = S.Task('D1_mem1', length=1, delay_cost=1)
	S += D1_mem1 >= 28
	D1_mem1 += MAIN_MEM_r[1]

	N_b0 = S.Task('N_b0', length=2, delay_cost=1)
	S += N_b0 >= 28
	N_b0 += MAS[0]

	D1 = S.Task('D1', length=8, delay_cost=1)
	S += D1 >= 29
	D1 += MM[0]

	N0_in = S.Task('N0_in', length=1, delay_cost=1)
	S += N0_in >= 29
	N0_in += MM_in[0]

	N0_mem0 = S.Task('N0_mem0', length=1, delay_cost=1)
	S += N0_mem0 >= 29
	N0_mem0 += MAIN_MEM_r[0]

	N0_mem1 = S.Task('N0_mem1', length=1, delay_cost=1)
	S += N0_mem1 >= 29
	N0_mem1 += MAS_MEM[1]

	N_b1_in = S.Task('N_b1_in', length=1, delay_cost=1)
	S += N_b1_in >= 29
	N_b1_in += MAS_in[0]

	N_b1_mem0 = S.Task('N_b1_mem0', length=1, delay_cost=1)
	S += N_b1_mem0 >= 29
	N_b1_mem0 += MAS_MEM[2]

	N_b1_mem1 = S.Task('N_b1_mem1', length=1, delay_cost=1)
	S += N_b1_mem1 >= 29
	N_b1_mem1 += MAIN_MEM_r[1]

	N0 = S.Task('N0', length=8, delay_cost=1)
	S += N0 >= 30
	N0 += MM[0]

	N_b1 = S.Task('N_b1', length=2, delay_cost=1)
	S += N_b1 >= 30
	N_b1 += MAS[0]

	N1_in = S.Task('N1_in', length=1, delay_cost=1)
	S += N1_in >= 31
	N1_in += MM_in[0]

	N1_mem0 = S.Task('N1_mem0', length=1, delay_cost=1)
	S += N1_mem0 >= 31
	N1_mem0 += MAIN_MEM_r[0]

	N1_mem1 = S.Task('N1_mem1', length=1, delay_cost=1)
	S += N1_mem1 >= 31
	N1_mem1 += MAS_MEM[1]

	N1 = S.Task('N1', length=8, delay_cost=1)
	S += N1 >= 32
	N1 += MM[0]

	D0_w = S.Task('D0_w', length=1, delay_cost=1)
	S += D0_w >= 35
	D0_w += MAIN_MEM_w

	Z_SSWU0_mem0 = S.Task('Z_SSWU0_mem0', length=1, delay_cost=1)
	S += Z_SSWU0_mem0 >= 36
	Z_SSWU0_mem0 += MAIN_MEM_r[0]

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

	Z_SSWU0_mem1 = S.Task('Z_SSWU0_mem1', length=1, delay_cost=1)
	S += Z_SSWU0_mem1 >= 37
	Z_SSWU0_mem1 += MAIN_MEM_r[0]

	N0_w = S.Task('N0_w', length=1, delay_cost=1)
	S += N0_w >= 38
	N0_w += MAIN_MEM_w

	N20 = S.Task('N20', length=8, delay_cost=1)
	S += N20 >= 38
	N20 += MM[0]

	Z_SSWU0_mem2 = S.Task('Z_SSWU0_mem2', length=1, delay_cost=1)
	S += Z_SSWU0_mem2 >= 38
	Z_SSWU0_mem2 += MAIN_MEM_r[0]

	N21_in = S.Task('N21_in', length=1, delay_cost=1)
	S += N21_in >= 39
	N21_in += MM_in[0]

	N21_mem0 = S.Task('N21_mem0', length=1, delay_cost=1)
	S += N21_mem0 >= 39
	N21_mem0 += MM_MEM[0]

	N21_mem1 = S.Task('N21_mem1', length=1, delay_cost=1)
	S += N21_mem1 >= 39
	N21_mem1 += MM_MEM[1]

	Z_SSWU0 = S.Task('Z_SSWU0', length=3, delay_cost=1)
	S += Z_SSWU0 >= 39
	Z_SSWU0 += CSEL

	Z_SSWU1_mem0 = S.Task('Z_SSWU1_mem0', length=1, delay_cost=1)
	S += Z_SSWU1_mem0 >= 39
	Z_SSWU1_mem0 += MAIN_MEM_r[0]

	N1_w = S.Task('N1_w', length=1, delay_cost=1)
	S += N1_w >= 40
	N1_w += MAIN_MEM_w

	N21 = S.Task('N21', length=8, delay_cost=1)
	S += N21 >= 40
	N21 += MM[0]

	Z_SSWU1_mem1 = S.Task('Z_SSWU1_mem1', length=1, delay_cost=1)
	S += Z_SSWU1_mem1 >= 40
	Z_SSWU1_mem1 += MAIN_MEM_r[0]

	Z_SSWU1_mem2 = S.Task('Z_SSWU1_mem2', length=1, delay_cost=1)
	S += Z_SSWU1_mem2 >= 41
	Z_SSWU1_mem2 += MAIN_MEM_r[0]

	Z_SSWU1 = S.Task('Z_SSWU1', length=3, delay_cost=1)
	S += Z_SSWU1 >= 42
	Z_SSWU1 += CSEL

	N30_in = S.Task('N30_in', length=1, delay_cost=1)
	S += N30_in >= 45
	N30_in += MM_in[0]

	N30_mem0 = S.Task('N30_mem0', length=1, delay_cost=1)
	S += N30_mem0 >= 45
	N30_mem0 += MM_MEM[0]

	N30_mem1 = S.Task('N30_mem1', length=1, delay_cost=1)
	S += N30_mem1 >= 45
	N30_mem1 += MM_MEM[1]

	N30 = S.Task('N30', length=8, delay_cost=1)
	S += N30 >= 46
	N30 += MM[0]

	Z_SSWU0_w = S.Task('Z_SSWU0_w', length=1, delay_cost=1)
	S += Z_SSWU0_w >= 46
	Z_SSWU0_w += MAIN_MEM_w

	D20_in = S.Task('D20_in', length=1, delay_cost=1)
	S += D20_in >= 47
	D20_in += MM_in[0]

	D20_mem0 = S.Task('D20_mem0', length=1, delay_cost=1)
	S += D20_mem0 >= 47
	D20_mem0 += MAIN_MEM_r[0]

	D20_mem1 = S.Task('D20_mem1', length=1, delay_cost=1)
	S += D20_mem1 >= 47
	D20_mem1 += MAIN_MEM_r[1]

	D20 = S.Task('D20', length=8, delay_cost=1)
	S += D20 >= 48
	D20 += MM[0]

	N31_in = S.Task('N31_in', length=1, delay_cost=1)
	S += N31_in >= 48
	N31_in += MM_in[0]

	N31_mem0 = S.Task('N31_mem0', length=1, delay_cost=1)
	S += N31_mem0 >= 48
	N31_mem0 += MM_MEM[0]

	N31_mem1 = S.Task('N31_mem1', length=1, delay_cost=1)
	S += N31_mem1 >= 48
	N31_mem1 += MM_MEM[1]

	N31 = S.Task('N31', length=8, delay_cost=1)
	S += N31 >= 49
	N31 += MM[0]

	Z_SSWU1_w = S.Task('Z_SSWU1_w', length=1, delay_cost=1)
	S += Z_SSWU1_w >= 49
	Z_SSWU1_w += MAIN_MEM_w

	D21_in = S.Task('D21_in', length=1, delay_cost=1)
	S += D21_in >= 50
	D21_in += MM_in[0]

	D21_mem0 = S.Task('D21_mem0', length=1, delay_cost=1)
	S += D21_mem0 >= 50
	D21_mem0 += MAIN_MEM_r[0]

	D21_mem1 = S.Task('D21_mem1', length=1, delay_cost=1)
	S += D21_mem1 >= 50
	D21_mem1 += MAIN_MEM_r[1]

	D21 = S.Task('D21', length=8, delay_cost=1)
	S += D21 >= 51
	D21 += MM[0]

	V0_in = S.Task('V0_in', length=1, delay_cost=1)
	S += V0_in >= 55
	V0_in += MM_in[0]

	V0_mem0 = S.Task('V0_mem0', length=1, delay_cost=1)
	S += V0_mem0 >= 55
	V0_mem0 += MM_MEM[0]

	V0_mem1 = S.Task('V0_mem1', length=1, delay_cost=1)
	S += V0_mem1 >= 55
	V0_mem1 += MAIN_MEM_r[1]

	ND20_in = S.Task('ND20_in', length=1, delay_cost=1)
	S += ND20_in >= 56
	ND20_in += MM_in[0]

	ND20_mem0 = S.Task('ND20_mem0', length=1, delay_cost=1)
	S += ND20_mem0 >= 56
	ND20_mem0 += MM_MEM[0]

	ND20_mem1 = S.Task('ND20_mem1', length=1, delay_cost=1)
	S += ND20_mem1 >= 56
	ND20_mem1 += MM_MEM[1]

	V0 = S.Task('V0', length=8, delay_cost=1)
	S += V0 >= 56
	V0 += MM[0]

	ND20 = S.Task('ND20', length=8, delay_cost=1)
	S += ND20 >= 57
	ND20 += MM[0]

	V1_in = S.Task('V1_in', length=1, delay_cost=1)
	S += V1_in >= 58
	V1_in += MM_in[0]

	V1_mem0 = S.Task('V1_mem0', length=1, delay_cost=1)
	S += V1_mem0 >= 58
	V1_mem0 += MM_MEM[0]

	V1_mem1 = S.Task('V1_mem1', length=1, delay_cost=1)
	S += V1_mem1 >= 58
	V1_mem1 += MAIN_MEM_r[1]

	ND21_in = S.Task('ND21_in', length=1, delay_cost=1)
	S += ND21_in >= 59
	ND21_in += MM_in[0]

	ND21_mem0 = S.Task('ND21_mem0', length=1, delay_cost=1)
	S += ND21_mem0 >= 59
	ND21_mem0 += MM_MEM[0]

	ND21_mem1 = S.Task('ND21_mem1', length=1, delay_cost=1)
	S += ND21_mem1 >= 59
	ND21_mem1 += MM_MEM[1]

	V1 = S.Task('V1', length=8, delay_cost=1)
	S += V1 >= 59
	V1 += MM[0]

	ND21 = S.Task('ND21', length=8, delay_cost=1)
	S += ND21 >= 60
	ND21 += MM[0]

	V0_w = S.Task('V0_w', length=1, delay_cost=1)
	S += V0_w >= 64
	V0_w += MAIN_MEM_w

	V1_w = S.Task('V1_w', length=1, delay_cost=1)
	S += V1_w >= 67
	V1_w += MAIN_MEM_w


	# new tasks
	aND20 = S.Task('aND20', length=8, delay_cost=1)
	aND20 += alt(MM)
	aND20_in = S.Task('aND20_in', length=1, delay_cost=1)
	aND20_in += alt(MM_in)
	S += aND20_in*MM_in[0]<=aND20*MM[0]
	aND20_mem0 = S.Task('aND20_mem0', length=1, delay_cost=1)
	aND20_mem0 += MAIN_MEM_r[0]
	S += aND20_mem0 <= aND20

	aND20_mem1 = S.Task('aND20_mem1', length=1, delay_cost=1)
	aND20_mem1 += MM_MEM[1]
	S += 64 < aND20_mem1
	S += aND20_mem1 <= aND20

	aND21 = S.Task('aND21', length=8, delay_cost=1)
	aND21 += alt(MM)
	aND21_in = S.Task('aND21_in', length=1, delay_cost=1)
	aND21_in += alt(MM_in)
	S += aND21_in*MM_in[0]<=aND21*MM[0]
	aND21_mem0 = S.Task('aND21_mem0', length=1, delay_cost=1)
	aND21_mem0 += MAIN_MEM_r[0]
	S += aND21_mem0 <= aND21

	aND21_mem1 = S.Task('aND21_mem1', length=1, delay_cost=1)
	aND21_mem1 += MM_MEM[1]
	S += 67 < aND21_mem1
	S += aND21_mem1 <= aND21

	bD30 = S.Task('bD30', length=8, delay_cost=1)
	bD30 += alt(MM)
	bD30_in = S.Task('bD30_in', length=1, delay_cost=1)
	bD30_in += alt(MM_in)
	S += bD30_in*MM_in[0]<=bD30*MM[0]
	bD30_mem0 = S.Task('bD30_mem0', length=1, delay_cost=1)
	bD30_mem0 += MAIN_MEM_r[0]
	S += bD30_mem0 <= bD30

	bD30_mem1 = S.Task('bD30_mem1', length=1, delay_cost=1)
	bD30_mem1 += MM_MEM[1]
	S += 63 < bD30_mem1
	S += bD30_mem1 <= bD30

	bD31 = S.Task('bD31', length=8, delay_cost=1)
	bD31 += alt(MM)
	bD31_in = S.Task('bD31_in', length=1, delay_cost=1)
	bD31_in += alt(MM_in)
	S += bD31_in*MM_in[0]<=bD31*MM[0]
	bD31_mem0 = S.Task('bD31_mem0', length=1, delay_cost=1)
	bD31_mem0 += MAIN_MEM_r[0]
	S += bD31_mem0 <= bD31

	bD31_mem1 = S.Task('bD31_mem1', length=1, delay_cost=1)
	bD31_mem1 += MM_MEM[1]
	S += 66 < bD31_mem1
	S += bD31_mem1 <= bD31

	V20 = S.Task('V20', length=8, delay_cost=1)
	V20 += alt(MM)
	V20_in = S.Task('V20_in', length=1, delay_cost=1)
	V20_in += alt(MM_in)
	S += V20_in*MM_in[0]<=V20*MM[0]
	V20_mem0 = S.Task('V20_mem0', length=1, delay_cost=1)
	V20_mem0 += MM_MEM[0]
	S += 63 < V20_mem0
	S += V20_mem0 <= V20

	V20_mem1 = S.Task('V20_mem1', length=1, delay_cost=1)
	V20_mem1 += MM_MEM[1]
	S += 63 < V20_mem1
	S += V20_mem1 <= V20

	V21 = S.Task('V21', length=8, delay_cost=1)
	V21 += alt(MM)
	V21_in = S.Task('V21_in', length=1, delay_cost=1)
	V21_in += alt(MM_in)
	S += V21_in*MM_in[0]<=V21*MM[0]
	V21_mem0 = S.Task('V21_mem0', length=1, delay_cost=1)
	V21_mem0 += MM_MEM[0]
	S += 66 < V21_mem0
	S += V21_mem0 <= V21

	V21_mem1 = S.Task('V21_mem1', length=1, delay_cost=1)
	V21_mem1 += MM_MEM[1]
	S += 66 < V21_mem1
	S += V21_mem1 <= V21

	U_0 = S.Task('U_0', length=2, delay_cost=1)
	U_0 += alt(MAS)
	U_0_in = S.Task('U_0_in', length=1, delay_cost=1)
	U_0_in += alt(MAS_in)
	S += U_0_in*MAS_in[0]<=U_0*MAS[0]

	S += U_0_in*MAS_in[1]<=U_0*MAS[1]

	U_0_mem0 = S.Task('U_0_mem0', length=1, delay_cost=1)
	U_0_mem0 += MM_MEM[0]
	S += 53 < U_0_mem0
	S += U_0_mem0 <= U_0

	U_0_mem1 = S.Task('U_0_mem1', length=1, delay_cost=1)
	U_0_mem1 += alt(MM_MEM)
	S += (aND20*MM[0])-1 < U_0_mem1*MM_MEM[1]
	S += U_0_mem1 <= U_0

	U_1 = S.Task('U_1', length=2, delay_cost=1)
	U_1 += alt(MAS)
	U_1_in = S.Task('U_1_in', length=1, delay_cost=1)
	U_1_in += alt(MAS_in)
	S += U_1_in*MAS_in[0]<=U_1*MAS[0]

	S += U_1_in*MAS_in[1]<=U_1*MAS[1]

	U_1_mem0 = S.Task('U_1_mem0', length=1, delay_cost=1)
	U_1_mem0 += MM_MEM[0]
	S += 56 < U_1_mem0
	S += U_1_mem0 <= U_1

	U_1_mem1 = S.Task('U_1_mem1', length=1, delay_cost=1)
	U_1_mem1 += alt(MM_MEM)
	S += (aND21*MM[0])-1 < U_1_mem1*MM_MEM[1]
	S += U_1_mem1 <= U_1

	U0 = S.Task('U0', length=2, delay_cost=1)
	U0 += alt(MAS)
	U0_in = S.Task('U0_in', length=1, delay_cost=1)
	U0_in += alt(MAS_in)
	S += U0_in*MAS_in[0]<=U0*MAS[0]

	S += U0_in*MAS_in[1]<=U0*MAS[1]

	S += 0<U0

	U0_w = S.Task('U0_w', length=1, delay_cost=1)
	U0_w += alt(MAIN_MEM_w)
	S += U0 <= U0_w

	U0_mem0 = S.Task('U0_mem0', length=1, delay_cost=1)
	U0_mem0 += alt(MAS_MEM)
	S += (U_0*MAS[0])-1 < U0_mem0*MAS_MEM[0]
	S += (U_0*MAS[1])-1 < U0_mem0*MAS_MEM[2]
	S += U0_mem0 <= U0

	U0_mem1 = S.Task('U0_mem1', length=1, delay_cost=1)
	U0_mem1 += alt(MM_MEM)
	S += (bD30*MM[0])-1 < U0_mem1*MM_MEM[1]
	S += U0_mem1 <= U0

	U1 = S.Task('U1', length=2, delay_cost=1)
	U1 += alt(MAS)
	U1_in = S.Task('U1_in', length=1, delay_cost=1)
	U1_in += alt(MAS_in)
	S += U1_in*MAS_in[0]<=U1*MAS[0]

	S += U1_in*MAS_in[1]<=U1*MAS[1]

	S += 0<U1

	U1_w = S.Task('U1_w', length=1, delay_cost=1)
	U1_w += alt(MAIN_MEM_w)
	S += U1 <= U1_w

	U1_mem0 = S.Task('U1_mem0', length=1, delay_cost=1)
	U1_mem0 += alt(MAS_MEM)
	S += (U_1*MAS[0])-1 < U1_mem0*MAS_MEM[0]
	S += (U_1*MAS[1])-1 < U1_mem0*MAS_MEM[2]
	S += U1_mem0 <= U1

	U1_mem1 = S.Task('U1_mem1', length=1, delay_cost=1)
	U1_mem1 += alt(MM_MEM)
	S += (bD31*MM[0])-1 < U1_mem1*MM_MEM[1]
	S += U1_mem1 <= U1

	UV0 = S.Task('UV0', length=8, delay_cost=1)
	UV0 += alt(MM)
	UV0_in = S.Task('UV0_in', length=1, delay_cost=1)
	UV0_in += alt(MM_in)
	S += UV0_in*MM_in[0]<=UV0*MM[0]
	S += 0<UV0

	UV0_w = S.Task('UV0_w', length=1, delay_cost=1)
	UV0_w += alt(MAIN_MEM_w)
	S += UV0 <= UV0_w

	UV0_mem0 = S.Task('UV0_mem0', length=1, delay_cost=1)
	UV0_mem0 += alt(MAS_MEM)
	S += (U0*MAS[0])-1 < UV0_mem0*MAS_MEM[0]
	S += (U0*MAS[1])-1 < UV0_mem0*MAS_MEM[2]
	S += UV0_mem0 <= UV0

	UV0_mem1 = S.Task('UV0_mem1', length=1, delay_cost=1)
	UV0_mem1 += MM_MEM[1]
	S += 63 < UV0_mem1
	S += UV0_mem1 <= UV0

	UV1 = S.Task('UV1', length=8, delay_cost=1)
	UV1 += alt(MM)
	UV1_in = S.Task('UV1_in', length=1, delay_cost=1)
	UV1_in += alt(MM_in)
	S += UV1_in*MM_in[0]<=UV1*MM[0]
	S += 0<UV1

	UV1_w = S.Task('UV1_w', length=1, delay_cost=1)
	UV1_w += alt(MAIN_MEM_w)
	S += UV1 <= UV1_w

	UV1_mem0 = S.Task('UV1_mem0', length=1, delay_cost=1)
	UV1_mem0 += alt(MAS_MEM)
	S += (U1*MAS[0])-1 < UV1_mem0*MAS_MEM[0]
	S += (U1*MAS[1])-1 < UV1_mem0*MAS_MEM[2]
	S += UV1_mem0 <= UV1

	UV1_mem1 = S.Task('UV1_mem1', length=1, delay_cost=1)
	UV1_mem1 += MM_MEM[1]
	S += 66 < UV1_mem1
	S += UV1_mem1 <= UV1

	UV30 = S.Task('UV30', length=8, delay_cost=1)
	UV30 += alt(MM)
	UV30_in = S.Task('UV30_in', length=1, delay_cost=1)
	UV30_in += alt(MM_in)
	S += UV30_in*MM_in[0]<=UV30*MM[0]
	S += 0<UV30

	UV30_w = S.Task('UV30_w', length=1, delay_cost=1)
	UV30_w += alt(MAIN_MEM_w)
	S += UV30 <= UV30_w

	UV30_mem0 = S.Task('UV30_mem0', length=1, delay_cost=1)
	UV30_mem0 += alt(MM_MEM)
	S += (UV0*MM[0])-1 < UV30_mem0*MM_MEM[0]
	S += UV30_mem0 <= UV30

	UV30_mem1 = S.Task('UV30_mem1', length=1, delay_cost=1)
	UV30_mem1 += alt(MM_MEM)
	S += (V20*MM[0])-1 < UV30_mem1*MM_MEM[1]
	S += UV30_mem1 <= UV30

	UV31 = S.Task('UV31', length=8, delay_cost=1)
	UV31 += alt(MM)
	UV31_in = S.Task('UV31_in', length=1, delay_cost=1)
	UV31_in += alt(MM_in)
	S += UV31_in*MM_in[0]<=UV31*MM[0]
	S += 0<UV31

	UV31_w = S.Task('UV31_w', length=1, delay_cost=1)
	UV31_w += alt(MAIN_MEM_w)
	S += UV31 <= UV31_w

	UV31_mem0 = S.Task('UV31_mem0', length=1, delay_cost=1)
	UV31_mem0 += alt(MM_MEM)
	S += (UV1*MM[0])-1 < UV31_mem0*MM_MEM[0]
	S += UV31_mem0 <= UV31

	UV31_mem1 = S.Task('UV31_mem1', length=1, delay_cost=1)
	UV31_mem1 += alt(MM_MEM)
	S += (V21*MM[0])-1 < UV31_mem1*MM_MEM[1]
	S += UV31_mem1 <= UV31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage2MAS2/2xSSWU_BEFORE_EXP/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution

