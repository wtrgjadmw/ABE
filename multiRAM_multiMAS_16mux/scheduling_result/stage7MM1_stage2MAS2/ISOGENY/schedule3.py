from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 228
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=2, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 0
	Z_exp2_in += MM_in[0]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 0
	Z_exp2_mem0 += MAIN_MEM_r[0]

	Z_exp2_mem1 = S.Task('Z_exp2_mem1', length=1, delay_cost=1)
	S += Z_exp2_mem1 >= 0
	Z_exp2_mem1 += MAIN_MEM_r[1]

	Z_exp2 = S.Task('Z_exp2', length=7, delay_cost=1)
	S += Z_exp2 >= 1
	Z_exp2 += MM[0]

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 1
	k0_10_Z1_in += MM_in[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 1
	k0_10_Z1_mem0 += MAIN_MEM_r[0]

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 1
	k0_10_Z1_mem1 += MAIN_MEM_r[1]

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 2
	NX0_in += MM_in[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 2
	NX0_mem0 += MAIN_MEM_r[0]

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 2
	NX0_mem1 += MAIN_MEM_r[1]

	k0_10_Z1 = S.Task('k0_10_Z1', length=7, delay_cost=1)
	S += k0_10_Z1 >= 2
	k0_10_Z1 += MM[0]

	NX0 = S.Task('NX0', length=7, delay_cost=1)
	S += NX0 >= 3
	NX0 += MM[0]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 3
	k2_14_Z1_in += MM_in[0]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 3
	k2_14_Z1_mem0 += MAIN_MEM_r[0]

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 3
	k2_14_Z1_mem1 += MAIN_MEM_r[1]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 4
	NY0_in += MM_in[0]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 4
	NY0_mem0 += MAIN_MEM_r[0]

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 4
	NY0_mem1 += MAIN_MEM_r[1]

	k2_14_Z1 = S.Task('k2_14_Z1', length=7, delay_cost=1)
	S += k2_14_Z1 >= 4
	k2_14_Z1 += MM[0]

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 5
	DY0_in += MM_in[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 5
	DY0_mem0 += MAIN_MEM_r[0]

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 5
	DY0_mem1 += MAIN_MEM_r[1]

	NY0 = S.Task('NY0', length=7, delay_cost=1)
	S += NY0 >= 5
	NY0 += MM[0]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 6
	DX0_in += MM_in[0]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 6
	DX0_mem0 += MAIN_MEM_r[0]

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 6
	DX0_mem1 += MAIN_MEM_r[1]

	DY0 = S.Task('DY0', length=7, delay_cost=1)
	S += DY0 >= 6
	DY0 += MM[0]

	DX0 = S.Task('DX0', length=7, delay_cost=1)
	S += DX0 >= 7
	DX0 += MM[0]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 7
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 7
	k1_9_Z2_mem0 += MAIN_MEM_r[0]

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 7
	k1_9_Z2_mem1 += MM_MEM[1]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 8
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 8
	Z_exp3_mem0 += MM_MEM[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 8
	Z_exp3_mem1 += MAIN_MEM_r[1]

	k1_9_Z2 = S.Task('k1_9_Z2', length=7, delay_cost=1)
	S += k1_9_Z2 >= 8
	k1_9_Z2 += MM[0]

	NX1__in = S.Task('NX1__in', length=1, delay_cost=1)
	S += NX1__in >= 9
	NX1__in += MAS_in[1]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 9
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 9
	NX1__mem1 += MM_MEM[1]

	Z_exp3 = S.Task('Z_exp3', length=7, delay_cost=1)
	S += Z_exp3 >= 9
	Z_exp3 += MM[0]

	NX1_ = S.Task('NX1_', length=2, delay_cost=1)
	S += NX1_ >= 10
	NX1_ += MAS[1]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 10
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 10
	k2_13_Z2_mem0 += MAIN_MEM_r[0]

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 10
	k2_13_Z2_mem1 += MM_MEM[1]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 11
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 11
	NX1_mem0 += MAS_MEM[2]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 11
	NX1_mem1 += MAIN_MEM_r[1]

	NY1__in = S.Task('NY1__in', length=1, delay_cost=1)
	S += NY1__in >= 11
	NY1__in += MAS_in[1]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 11
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 11
	NY1__mem1 += MM_MEM[1]

	k2_13_Z2 = S.Task('k2_13_Z2', length=7, delay_cost=1)
	S += k2_13_Z2 >= 11
	k2_13_Z2 += MM[0]

	NX1 = S.Task('NX1', length=7, delay_cost=1)
	S += NX1 >= 12
	NX1 += MM[0]

	NY1_ = S.Task('NY1_', length=2, delay_cost=1)
	S += NY1_ >= 12
	NY1_ += MAS[1]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 12
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 12
	k0_9_Z2_mem0 += MAIN_MEM_r[0]

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 12
	k0_9_Z2_mem1 += MM_MEM[1]

	k0_9_Z2 = S.Task('k0_9_Z2', length=7, delay_cost=1)
	S += k0_9_Z2 >= 13
	k0_9_Z2 += MM[0]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 13
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 13
	k3_14_Z2_mem0 += MAIN_MEM_r[0]

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 13
	k3_14_Z2_mem1 += MM_MEM[1]

	DX1__in = S.Task('DX1__in', length=1, delay_cost=1)
	S += DX1__in >= 14
	DX1__in += MAS_in[0]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 14
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 14
	DX1__mem1 += MM_MEM[1]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 14
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 14
	NY1_mem0 += MAS_MEM[2]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 14
	NY1_mem1 += MAIN_MEM_r[1]

	k3_14_Z2 = S.Task('k3_14_Z2', length=7, delay_cost=1)
	S += k3_14_Z2 >= 14
	k3_14_Z2 += MM[0]

	DX1_ = S.Task('DX1_', length=2, delay_cost=1)
	S += DX1_ >= 15
	DX1_ += MAS[0]

	NY1 = S.Task('NY1', length=7, delay_cost=1)
	S += NY1 >= 15
	NY1 += MM[0]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 15
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 15
	k0_8_Z3_mem0 += MAIN_MEM_r[0]

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 15
	k0_8_Z3_mem1 += MM_MEM[1]

	k0_8_Z3 = S.Task('k0_8_Z3', length=7, delay_cost=1)
	S += k0_8_Z3 >= 16
	k0_8_Z3 += MM[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 16
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 16
	k3_13_Z3_mem0 += MAIN_MEM_r[0]

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 16
	k3_13_Z3_mem1 += MM_MEM[1]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 17
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 17
	k2_12_Z3_mem0 += MAIN_MEM_r[0]

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 17
	k2_12_Z3_mem1 += MM_MEM[1]

	k3_13_Z3 = S.Task('k3_13_Z3', length=7, delay_cost=1)
	S += k3_13_Z3 >= 17
	k3_13_Z3 += MM[0]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 18
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 18
	Z_exp4_mem0 += MM_MEM[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 18
	Z_exp4_mem1 += MAIN_MEM_r[1]

	k2_12_Z3 = S.Task('k2_12_Z3', length=7, delay_cost=1)
	S += k2_12_Z3 >= 18
	k2_12_Z3 += MM[0]

	Z_exp4 = S.Task('Z_exp4', length=7, delay_cost=1)
	S += Z_exp4 >= 19
	Z_exp4 += MM[0]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 19
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 19
	k1_8_Z3_mem0 += MAIN_MEM_r[0]

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 19
	k1_8_Z3_mem1 += MM_MEM[1]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 20
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 20
	DX1_mem0 += MAS_MEM[0]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 20
	DX1_mem1 += MAIN_MEM_r[1]

	DY1__in = S.Task('DY1__in', length=1, delay_cost=1)
	S += DY1__in >= 20
	DY1__in += MAS_in[0]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 20
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 20
	DY1__mem1 += MM_MEM[1]

	k1_8_Z3 = S.Task('k1_8_Z3', length=7, delay_cost=1)
	S += k1_8_Z3 >= 20
	k1_8_Z3 += MM[0]

	DX1 = S.Task('DX1', length=7, delay_cost=1)
	S += DX1 >= 21
	DX1 += MM[0]

	DY1_ = S.Task('DY1_', length=2, delay_cost=1)
	S += DY1_ >= 21
	DY1_ += MAS[0]

	NY2__in = S.Task('NY2__in', length=1, delay_cost=1)
	S += NY2__in >= 21
	NY2__in += MAS_in[0]

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 21
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 21
	NY2__mem1 += MM_MEM[1]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 22
	DY1_in += MM_in[0]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 22
	DY1_mem0 += MAS_MEM[0]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 22
	DY1_mem1 += MAIN_MEM_r[1]

	NX2__in = S.Task('NX2__in', length=1, delay_cost=1)
	S += NX2__in >= 22
	NX2__in += MAS_in[0]

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 22
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 22
	NX2__mem1 += MM_MEM[1]

	NY2_ = S.Task('NY2_', length=2, delay_cost=1)
	S += NY2_ >= 22
	NY2_ += MAS[0]

	DY1 = S.Task('DY1', length=7, delay_cost=1)
	S += DY1 >= 23
	DY1 += MM[0]

	NX2_ = S.Task('NX2_', length=2, delay_cost=1)
	S += NX2_ >= 23
	NX2_ += MAS[0]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 23
	NY2_in += MM_in[0]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 23
	NY2_mem0 += MAS_MEM[0]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 23
	NY2_mem1 += MAIN_MEM_r[1]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 24
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 24
	NX2_mem0 += MAS_MEM[0]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 24
	NX2_mem1 += MAIN_MEM_r[1]

	NY2 = S.Task('NY2', length=7, delay_cost=1)
	S += NY2 >= 24
	NY2 += MM[0]

	NX2 = S.Task('NX2', length=7, delay_cost=1)
	S += NX2 >= 25
	NX2 += MM[0]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 25
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 25
	Z_exp5_mem0 += MM_MEM[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 25
	Z_exp5_mem1 += MAIN_MEM_r[1]

	Z_exp5 = S.Task('Z_exp5', length=7, delay_cost=1)
	S += Z_exp5 >= 26
	Z_exp5 += MM[0]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 26
	k1_7_Z4_in += MM_in[0]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 26
	k1_7_Z4_mem0 += MAIN_MEM_r[0]

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 26
	k1_7_Z4_mem1 += MM_MEM[1]

	DX2__in = S.Task('DX2__in', length=1, delay_cost=1)
	S += DX2__in >= 27
	DX2__in += MAS_in[0]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 27
	DX2__mem0 += MM_MEM[0]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 27
	DX2__mem1 += MM_MEM[1]

	k1_7_Z4 = S.Task('k1_7_Z4', length=7, delay_cost=1)
	S += k1_7_Z4 >= 27
	k1_7_Z4 += MM[0]

	DX2_ = S.Task('DX2_', length=2, delay_cost=1)
	S += DX2_ >= 28
	DX2_ += MAS[0]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 28
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 28
	k2_11_Z4_mem0 += MAIN_MEM_r[0]

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 28
	k2_11_Z4_mem1 += MM_MEM[1]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 29
	DX2_in += MM_in[0]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 29
	DX2_mem0 += MAS_MEM[0]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 29
	DX2_mem1 += MAIN_MEM_r[1]

	DY2__in = S.Task('DY2__in', length=1, delay_cost=1)
	S += DY2__in >= 29
	DY2__in += MAS_in[0]

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 29
	DY2__mem0 += MM_MEM[0]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 29
	DY2__mem1 += MM_MEM[1]

	k2_11_Z4 = S.Task('k2_11_Z4', length=7, delay_cost=1)
	S += k2_11_Z4 >= 29
	k2_11_Z4 += MM[0]

	DX2 = S.Task('DX2', length=7, delay_cost=1)
	S += DX2 >= 30
	DX2 += MM[0]

	DY2_ = S.Task('DY2_', length=2, delay_cost=1)
	S += DY2_ >= 30
	DY2_ += MAS[0]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 30
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 30
	k3_12_Z4_mem0 += MAIN_MEM_r[0]

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 30
	k3_12_Z4_mem1 += MM_MEM[1]

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 31
	DY2_in += MM_in[0]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 31
	DY2_mem0 += MAS_MEM[0]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 31
	DY2_mem1 += MAIN_MEM_r[1]

	NY3__in = S.Task('NY3__in', length=1, delay_cost=1)
	S += NY3__in >= 31
	NY3__in += MAS_in[0]

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 31
	NY3__mem0 += MM_MEM[0]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 31
	NY3__mem1 += MM_MEM[1]

	k3_12_Z4 = S.Task('k3_12_Z4', length=7, delay_cost=1)
	S += k3_12_Z4 >= 31
	k3_12_Z4 += MM[0]

	DY2 = S.Task('DY2', length=7, delay_cost=1)
	S += DY2 >= 32
	DY2 += MM[0]

	NY3_ = S.Task('NY3_', length=2, delay_cost=1)
	S += NY3_ >= 32
	NY3_ += MAS[0]

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	S += Z_exp6_in >= 32
	Z_exp6_in += MM_in[0]

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	S += Z_exp6_mem0 >= 32
	Z_exp6_mem0 += MM_MEM[0]

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	S += Z_exp6_mem1 >= 32
	Z_exp6_mem1 += MAIN_MEM_r[1]

	NX3__in = S.Task('NX3__in', length=1, delay_cost=1)
	S += NX3__in >= 33
	NX3__in += MAS_in[0]

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 33
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 33
	NX3__mem1 += MM_MEM[1]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 33
	NY3_in += MM_in[0]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 33
	NY3_mem0 += MAS_MEM[0]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 33
	NY3_mem1 += MAIN_MEM_r[1]

	Z_exp6 = S.Task('Z_exp6', length=7, delay_cost=1)
	S += Z_exp6 >= 33
	Z_exp6 += MM[0]

	NX3_ = S.Task('NX3_', length=2, delay_cost=1)
	S += NX3_ >= 34
	NX3_ += MAS[0]

	NY3 = S.Task('NY3', length=7, delay_cost=1)
	S += NY3 >= 34
	NY3 += MM[0]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 34
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 34
	k2_10_Z5_mem0 += MAIN_MEM_r[0]

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 34
	k2_10_Z5_mem1 += MM_MEM[1]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 35
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 35
	k1_6_Z5_mem0 += MAIN_MEM_r[0]

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 35
	k1_6_Z5_mem1 += MM_MEM[1]

	k2_10_Z5 = S.Task('k2_10_Z5', length=7, delay_cost=1)
	S += k2_10_Z5 >= 35
	k2_10_Z5 += MM[0]

	DX3__in = S.Task('DX3__in', length=1, delay_cost=1)
	S += DX3__in >= 36
	DX3__in += MAS_in[0]

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	S += DX3__mem0 >= 36
	DX3__mem0 += MM_MEM[0]

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	S += DX3__mem1 >= 36
	DX3__mem1 += MM_MEM[1]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 36
	NX3_in += MM_in[0]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 36
	NX3_mem0 += MAS_MEM[0]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 36
	NX3_mem1 += MAIN_MEM_r[1]

	k1_6_Z5 = S.Task('k1_6_Z5', length=7, delay_cost=1)
	S += k1_6_Z5 >= 36
	k1_6_Z5 += MM[0]

	DX3_ = S.Task('DX3_', length=2, delay_cost=1)
	S += DX3_ >= 37
	DX3_ += MAS[0]

	NX3 = S.Task('NX3', length=7, delay_cost=1)
	S += NX3 >= 37
	NX3 += MM[0]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 37
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 37
	k3_11_Z5_mem0 += MAIN_MEM_r[0]

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 37
	k3_11_Z5_mem1 += MM_MEM[1]

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	S += DX3_in >= 38
	DX3_in += MM_in[0]

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	S += DX3_mem0 >= 38
	DX3_mem0 += MAS_MEM[0]

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	S += DX3_mem1 >= 38
	DX3_mem1 += MAIN_MEM_r[1]

	DY3__in = S.Task('DY3__in', length=1, delay_cost=1)
	S += DY3__in >= 38
	DY3__in += MAS_in[0]

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	S += DY3__mem0 >= 38
	DY3__mem0 += MM_MEM[0]

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	S += DY3__mem1 >= 38
	DY3__mem1 += MM_MEM[1]

	k3_11_Z5 = S.Task('k3_11_Z5', length=7, delay_cost=1)
	S += k3_11_Z5 >= 38
	k3_11_Z5 += MM[0]

	DX3 = S.Task('DX3', length=7, delay_cost=1)
	S += DX3 >= 39
	DX3 += MM[0]

	DY3_ = S.Task('DY3_', length=2, delay_cost=1)
	S += DY3_ >= 39
	DY3_ += MAS[0]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 39
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 39
	Z_exp7_mem0 += MM_MEM[0]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 39
	Z_exp7_mem1 += MAIN_MEM_r[1]

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	S += DY3_in >= 40
	DY3_in += MM_in[0]

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	S += DY3_mem0 >= 40
	DY3_mem0 += MAS_MEM[0]

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	S += DY3_mem1 >= 40
	DY3_mem1 += MAIN_MEM_r[1]

	NY4__in = S.Task('NY4__in', length=1, delay_cost=1)
	S += NY4__in >= 40
	NY4__in += MAS_in[0]

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 40
	NY4__mem0 += MM_MEM[0]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 40
	NY4__mem1 += MM_MEM[1]

	Z_exp7 = S.Task('Z_exp7', length=7, delay_cost=1)
	S += Z_exp7 >= 40
	Z_exp7 += MM[0]

	DY3 = S.Task('DY3', length=7, delay_cost=1)
	S += DY3 >= 41
	DY3 += MM[0]

	NY4_ = S.Task('NY4_', length=2, delay_cost=1)
	S += NY4_ >= 41
	NY4_ += MAS[0]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 41
	k1_5_Z6_in += MM_in[0]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 41
	k1_5_Z6_mem0 += MAIN_MEM_r[0]

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 41
	k1_5_Z6_mem1 += MM_MEM[1]

	k1_5_Z6 = S.Task('k1_5_Z6', length=7, delay_cost=1)
	S += k1_5_Z6 >= 42
	k1_5_Z6 += MM[0]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 42
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 42
	k2_9_Z6_mem0 += MAIN_MEM_r[0]

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 42
	k2_9_Z6_mem1 += MM_MEM[1]

	k2_9_Z6 = S.Task('k2_9_Z6', length=7, delay_cost=1)
	S += k2_9_Z6 >= 43
	k2_9_Z6 += MM[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 43
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 43
	k3_10_Z6_mem0 += MAIN_MEM_r[0]

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 43
	k3_10_Z6_mem1 += MM_MEM[1]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 44
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 44
	k0_7_Z4_mem0 += MAIN_MEM_r[0]

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 44
	k0_7_Z4_mem1 += MM_MEM[1]

	k3_10_Z6 = S.Task('k3_10_Z6', length=7, delay_cost=1)
	S += k3_10_Z6 >= 44
	k3_10_Z6 += MM[0]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 45
	k0_6_Z5_in += MM_in[0]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 45
	k0_6_Z5_mem0 += MAIN_MEM_r[0]

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 45
	k0_6_Z5_mem1 += MM_MEM[1]

	k0_7_Z4 = S.Task('k0_7_Z4', length=7, delay_cost=1)
	S += k0_7_Z4 >= 45
	k0_7_Z4 += MM[0]

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	S += Z_exp8_in >= 46
	Z_exp8_in += MM_in[0]

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	S += Z_exp8_mem0 >= 46
	Z_exp8_mem0 += MM_MEM[0]

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	S += Z_exp8_mem1 >= 46
	Z_exp8_mem1 += MAIN_MEM_r[1]

	k0_6_Z5 = S.Task('k0_6_Z5', length=7, delay_cost=1)
	S += k0_6_Z5 >= 46
	k0_6_Z5 += MM[0]

	Z_exp8 = S.Task('Z_exp8', length=7, delay_cost=1)
	S += Z_exp8 >= 47
	Z_exp8 += MM[0]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 47
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 47
	k0_5_Z6_mem0 += MAIN_MEM_r[0]

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 47
	k0_5_Z6_mem1 += MM_MEM[1]

	k0_5_Z6 = S.Task('k0_5_Z6', length=7, delay_cost=1)
	S += k0_5_Z6 >= 48
	k0_5_Z6 += MM[0]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 48
	k1_4_Z7_in += MM_in[0]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 48
	k1_4_Z7_mem0 += MAIN_MEM_r[0]

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 48
	k1_4_Z7_mem1 += MM_MEM[1]

	k1_4_Z7 = S.Task('k1_4_Z7', length=7, delay_cost=1)
	S += k1_4_Z7 >= 49
	k1_4_Z7 += MM[0]

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	S += k2_8_Z7_in >= 49
	k2_8_Z7_in += MM_in[0]

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	S += k2_8_Z7_mem0 >= 49
	k2_8_Z7_mem0 += MAIN_MEM_r[0]

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	S += k2_8_Z7_mem1 >= 49
	k2_8_Z7_mem1 += MM_MEM[1]

	k2_8_Z7 = S.Task('k2_8_Z7', length=7, delay_cost=1)
	S += k2_8_Z7 >= 50
	k2_8_Z7 += MM[0]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 50
	k3_9_Z7_in += MM_in[0]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 50
	k3_9_Z7_mem0 += MAIN_MEM_r[0]

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 50
	k3_9_Z7_mem1 += MM_MEM[1]

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	S += k0_4_Z7_in >= 51
	k0_4_Z7_in += MM_in[0]

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	S += k0_4_Z7_mem0 >= 51
	k0_4_Z7_mem0 += MAIN_MEM_r[0]

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	S += k0_4_Z7_mem1 >= 51
	k0_4_Z7_mem1 += MM_MEM[1]

	k3_9_Z7 = S.Task('k3_9_Z7', length=7, delay_cost=1)
	S += k3_9_Z7 >= 51
	k3_9_Z7 += MM[0]

	NX4__in = S.Task('NX4__in', length=1, delay_cost=1)
	S += NX4__in >= 52
	NX4__in += MAS_in[0]

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 52
	NX4__mem0 += MM_MEM[0]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 52
	NX4__mem1 += MM_MEM[1]

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	S += NY4_in >= 52
	NY4_in += MM_in[0]

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	S += NY4_mem0 >= 52
	NY4_mem0 += MAS_MEM[0]

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	S += NY4_mem1 >= 52
	NY4_mem1 += MAIN_MEM_r[1]

	k0_4_Z7 = S.Task('k0_4_Z7', length=7, delay_cost=1)
	S += k0_4_Z7 >= 52
	k0_4_Z7 += MM[0]

	NX4_ = S.Task('NX4_', length=2, delay_cost=1)
	S += NX4_ >= 53
	NX4_ += MAS[0]

	NY4 = S.Task('NY4', length=7, delay_cost=1)
	S += NY4 >= 53
	NY4 += MM[0]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 53
	k3_8_Z8_in += MM_in[0]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 53
	k3_8_Z8_mem0 += MAIN_MEM_r[0]

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 53
	k3_8_Z8_mem1 += MM_MEM[1]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 54
	k0_3_Z8_in += MM_in[0]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 54
	k0_3_Z8_mem0 += MAIN_MEM_r[0]

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 54
	k0_3_Z8_mem1 += MM_MEM[1]

	k3_8_Z8 = S.Task('k3_8_Z8', length=7, delay_cost=1)
	S += k3_8_Z8 >= 54
	k3_8_Z8 += MM[0]

	k0_3_Z8 = S.Task('k0_3_Z8', length=7, delay_cost=1)
	S += k0_3_Z8 >= 55
	k0_3_Z8 += MM[0]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 55
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 55
	k1_3_Z8_mem0 += MAIN_MEM_r[0]

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 55
	k1_3_Z8_mem1 += MM_MEM[1]

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	S += Z_exp9_in >= 56
	Z_exp9_in += MM_in[0]

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	S += Z_exp9_mem0 >= 56
	Z_exp9_mem0 += MM_MEM[0]

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	S += Z_exp9_mem1 >= 56
	Z_exp9_mem1 += MAIN_MEM_r[1]

	k1_3_Z8 = S.Task('k1_3_Z8', length=7, delay_cost=1)
	S += k1_3_Z8 >= 56
	k1_3_Z8 += MM[0]

	Z_exp9 = S.Task('Z_exp9', length=7, delay_cost=1)
	S += Z_exp9 >= 57
	Z_exp9 += MM[0]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 57
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 57
	k2_7_Z8_mem0 += MAIN_MEM_r[0]

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 57
	k2_7_Z8_mem1 += MM_MEM[1]

	DX4__in = S.Task('DX4__in', length=1, delay_cost=1)
	S += DX4__in >= 58
	DX4__in += MAS_in[0]

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	S += DX4__mem0 >= 58
	DX4__mem0 += MM_MEM[0]

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	S += DX4__mem1 >= 58
	DX4__mem1 += MM_MEM[1]

	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	S += NX4_in >= 58
	NX4_in += MM_in[0]

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	S += NX4_mem0 >= 58
	NX4_mem0 += MAS_MEM[0]

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	S += NX4_mem1 >= 58
	NX4_mem1 += MAIN_MEM_r[1]

	k2_7_Z8 = S.Task('k2_7_Z8', length=7, delay_cost=1)
	S += k2_7_Z8 >= 58
	k2_7_Z8 += MM[0]

	DX4_ = S.Task('DX4_', length=2, delay_cost=1)
	S += DX4_ >= 59
	DX4_ += MAS[0]

	DY4__in = S.Task('DY4__in', length=1, delay_cost=1)
	S += DY4__in >= 59
	DY4__in += MAS_in[1]

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	S += DY4__mem0 >= 59
	DY4__mem0 += MM_MEM[0]

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	S += DY4__mem1 >= 59
	DY4__mem1 += MM_MEM[1]

	NX4 = S.Task('NX4', length=7, delay_cost=1)
	S += NX4 >= 59
	NX4 += MM[0]

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	S += DX4_in >= 60
	DX4_in += MM_in[0]

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	S += DX4_mem0 >= 60
	DX4_mem0 += MAS_MEM[0]

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	S += DX4_mem1 >= 60
	DX4_mem1 += MAIN_MEM_r[1]

	DY4_ = S.Task('DY4_', length=2, delay_cost=1)
	S += DY4_ >= 60
	DY4_ += MAS[1]

	NY5__in = S.Task('NY5__in', length=1, delay_cost=1)
	S += NY5__in >= 60
	NY5__in += MAS_in[1]

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	S += NY5__mem0 >= 60
	NY5__mem0 += MM_MEM[0]

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	S += NY5__mem1 >= 60
	NY5__mem1 += MM_MEM[1]

	DX4 = S.Task('DX4', length=7, delay_cost=1)
	S += DX4 >= 61
	DX4 += MM[0]

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	S += DY4_in >= 61
	DY4_in += MM_in[0]

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	S += DY4_mem0 >= 61
	DY4_mem0 += MAS_MEM[2]

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	S += DY4_mem1 >= 61
	DY4_mem1 += MAIN_MEM_r[1]

	NY5_ = S.Task('NY5_', length=2, delay_cost=1)
	S += NY5_ >= 61
	NY5_ += MAS[1]

	DY4 = S.Task('DY4', length=7, delay_cost=1)
	S += DY4 >= 62
	DY4 += MM[0]

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	S += NY5_in >= 62
	NY5_in += MM_in[0]

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	S += NY5_mem0 >= 62
	NY5_mem0 += MAS_MEM[2]

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	S += NY5_mem1 >= 62
	NY5_mem1 += MAIN_MEM_r[1]

	NY5 = S.Task('NY5', length=7, delay_cost=1)
	S += NY5 >= 63
	NY5 += MM[0]

	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	S += Z_exp10_in >= 63
	Z_exp10_in += MM_in[0]

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	S += Z_exp10_mem0 >= 63
	Z_exp10_mem0 += MM_MEM[0]

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	S += Z_exp10_mem1 >= 63
	Z_exp10_mem1 += MAIN_MEM_r[1]

	Z_exp10 = S.Task('Z_exp10', length=7, delay_cost=1)
	S += Z_exp10 >= 64
	Z_exp10 += MM[0]

	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	S += k2_6_Z9_in >= 64
	k2_6_Z9_in += MM_in[0]

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	S += k2_6_Z9_mem0 >= 64
	k2_6_Z9_mem0 += MAIN_MEM_r[0]

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	S += k2_6_Z9_mem1 >= 64
	k2_6_Z9_mem1 += MM_MEM[1]

	NX5__in = S.Task('NX5__in', length=1, delay_cost=1)
	S += NX5__in >= 65
	NX5__in += MAS_in[0]

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	S += NX5__mem0 >= 65
	NX5__mem0 += MM_MEM[0]

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	S += NX5__mem1 >= 65
	NX5__mem1 += MM_MEM[1]

	k2_6_Z9 = S.Task('k2_6_Z9', length=7, delay_cost=1)
	S += k2_6_Z9 >= 65
	k2_6_Z9 += MM[0]

	NX5_ = S.Task('NX5_', length=2, delay_cost=1)
	S += NX5_ >= 66
	NX5_ += MAS[0]

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	S += k1_2_Z9_in >= 66
	k1_2_Z9_in += MM_in[0]

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	S += k1_2_Z9_mem0 >= 66
	k1_2_Z9_mem0 += MAIN_MEM_r[0]

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	S += k1_2_Z9_mem1 >= 66
	k1_2_Z9_mem1 += MM_MEM[1]

	DX5__in = S.Task('DX5__in', length=1, delay_cost=1)
	S += DX5__in >= 67
	DX5__in += MAS_in[0]

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	S += DX5__mem0 >= 67
	DX5__mem0 += MM_MEM[0]

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	S += DX5__mem1 >= 67
	DX5__mem1 += MM_MEM[1]

	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	S += NX5_in >= 67
	NX5_in += MM_in[0]

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	S += NX5_mem0 >= 67
	NX5_mem0 += MAS_MEM[0]

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	S += NX5_mem1 >= 67
	NX5_mem1 += MAIN_MEM_r[1]

	k1_2_Z9 = S.Task('k1_2_Z9', length=7, delay_cost=1)
	S += k1_2_Z9 >= 67
	k1_2_Z9 += MM[0]

	DX5_ = S.Task('DX5_', length=2, delay_cost=1)
	S += DX5_ >= 68
	DX5_ += MAS[0]

	NX5 = S.Task('NX5', length=7, delay_cost=1)
	S += NX5 >= 68
	NX5 += MM[0]

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	S += k3_7_Z9_in >= 68
	k3_7_Z9_in += MM_in[0]

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	S += k3_7_Z9_mem0 >= 68
	k3_7_Z9_mem0 += MAIN_MEM_r[0]

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	S += k3_7_Z9_mem1 >= 68
	k3_7_Z9_mem1 += MM_MEM[1]

	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	S += DX5_in >= 69
	DX5_in += MM_in[0]

	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	S += DX5_mem0 >= 69
	DX5_mem0 += MAS_MEM[0]

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	S += DX5_mem1 >= 69
	DX5_mem1 += MAIN_MEM_r[1]

	DY5__in = S.Task('DY5__in', length=1, delay_cost=1)
	S += DY5__in >= 69
	DY5__in += MAS_in[0]

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	S += DY5__mem0 >= 69
	DY5__mem0 += MM_MEM[0]

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	S += DY5__mem1 >= 69
	DY5__mem1 += MM_MEM[1]

	k3_7_Z9 = S.Task('k3_7_Z9', length=7, delay_cost=1)
	S += k3_7_Z9 >= 69
	k3_7_Z9 += MM[0]

	DX5 = S.Task('DX5', length=7, delay_cost=1)
	S += DX5 >= 70
	DX5 += MM[0]

	DY5_ = S.Task('DY5_', length=2, delay_cost=1)
	S += DY5_ >= 70
	DY5_ += MAS[0]

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	S += Z_exp11_in >= 70
	Z_exp11_in += MM_in[0]

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	S += Z_exp11_mem0 >= 70
	Z_exp11_mem0 += MM_MEM[0]

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	S += Z_exp11_mem1 >= 70
	Z_exp11_mem1 += MAIN_MEM_r[1]

	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	S += DY5_in >= 71
	DY5_in += MM_in[0]

	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	S += DY5_mem0 >= 71
	DY5_mem0 += MAS_MEM[0]

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	S += DY5_mem1 >= 71
	DY5_mem1 += MAIN_MEM_r[1]

	NY6__in = S.Task('NY6__in', length=1, delay_cost=1)
	S += NY6__in >= 71
	NY6__in += MAS_in[0]

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	S += NY6__mem0 >= 71
	NY6__mem0 += MM_MEM[0]

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	S += NY6__mem1 >= 71
	NY6__mem1 += MM_MEM[1]

	Z_exp11 = S.Task('Z_exp11', length=7, delay_cost=1)
	S += Z_exp11 >= 71
	Z_exp11 += MM[0]

	DY5 = S.Task('DY5', length=7, delay_cost=1)
	S += DY5 >= 72
	DY5 += MM[0]

	NY6_ = S.Task('NY6_', length=2, delay_cost=1)
	S += NY6_ >= 72
	NY6_ += MAS[0]

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	S += k0_1_Z10_in >= 72
	k0_1_Z10_in += MM_in[0]

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	S += k0_1_Z10_mem0 >= 72
	k0_1_Z10_mem0 += MAIN_MEM_r[0]

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	S += k0_1_Z10_mem1 >= 72
	k0_1_Z10_mem1 += MM_MEM[1]

	k0_1_Z10 = S.Task('k0_1_Z10', length=7, delay_cost=1)
	S += k0_1_Z10 >= 73
	k0_1_Z10 += MM[0]

	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	S += k3_6_Z10_in >= 73
	k3_6_Z10_in += MM_in[0]

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	S += k3_6_Z10_mem0 >= 73
	k3_6_Z10_mem0 += MAIN_MEM_r[0]

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	S += k3_6_Z10_mem1 >= 73
	k3_6_Z10_mem1 += MM_MEM[1]

	NX6__in = S.Task('NX6__in', length=1, delay_cost=1)
	S += NX6__in >= 74
	NX6__in += MAS_in[1]

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	S += NX6__mem0 >= 74
	NX6__mem0 += MM_MEM[0]

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	S += NX6__mem1 >= 74
	NX6__mem1 += MM_MEM[1]

	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	S += NY6_in >= 74
	NY6_in += MM_in[0]

	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	S += NY6_mem0 >= 74
	NY6_mem0 += MAS_MEM[0]

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	S += NY6_mem1 >= 74
	NY6_mem1 += MAIN_MEM_r[1]

	k3_6_Z10 = S.Task('k3_6_Z10', length=7, delay_cost=1)
	S += k3_6_Z10 >= 74
	k3_6_Z10 += MM[0]

	NX6_ = S.Task('NX6_', length=2, delay_cost=1)
	S += NX6_ >= 75
	NX6_ += MAS[1]

	NY6 = S.Task('NY6', length=7, delay_cost=1)
	S += NY6 >= 75
	NY6 += MM[0]

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	S += k2_5_Z10_in >= 75
	k2_5_Z10_in += MM_in[0]

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	S += k2_5_Z10_mem0 >= 75
	k2_5_Z10_mem0 += MAIN_MEM_r[0]

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	S += k2_5_Z10_mem1 >= 75
	k2_5_Z10_mem1 += MM_MEM[1]

	DX6__in = S.Task('DX6__in', length=1, delay_cost=1)
	S += DX6__in >= 76
	DX6__in += MAS_in[1]

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	S += DX6__mem0 >= 76
	DX6__mem0 += MM_MEM[0]

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	S += DX6__mem1 >= 76
	DX6__mem1 += MM_MEM[1]

	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	S += NX6_in >= 76
	NX6_in += MM_in[0]

	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	S += NX6_mem0 >= 76
	NX6_mem0 += MAS_MEM[2]

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	S += NX6_mem1 >= 76
	NX6_mem1 += MAIN_MEM_r[1]

	k2_5_Z10 = S.Task('k2_5_Z10', length=7, delay_cost=1)
	S += k2_5_Z10 >= 76
	k2_5_Z10 += MM[0]

	DX6_ = S.Task('DX6_', length=2, delay_cost=1)
	S += DX6_ >= 77
	DX6_ += MAS[1]

	NX6 = S.Task('NX6', length=7, delay_cost=1)
	S += NX6 >= 77
	NX6 += MM[0]

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	S += Z_exp12_in >= 77
	Z_exp12_in += MM_in[0]

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	S += Z_exp12_mem0 >= 77
	Z_exp12_mem0 += MM_MEM[0]

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	S += Z_exp12_mem1 >= 77
	Z_exp12_mem1 += MAIN_MEM_r[1]

	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	S += DX6_in >= 78
	DX6_in += MM_in[0]

	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	S += DX6_mem0 >= 78
	DX6_mem0 += MAS_MEM[2]

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	S += DX6_mem1 >= 78
	DX6_mem1 += MAIN_MEM_r[1]

	DY6__in = S.Task('DY6__in', length=1, delay_cost=1)
	S += DY6__in >= 78
	DY6__in += MAS_in[1]

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	S += DY6__mem0 >= 78
	DY6__mem0 += MM_MEM[0]

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	S += DY6__mem1 >= 78
	DY6__mem1 += MM_MEM[1]

	Z_exp12 = S.Task('Z_exp12', length=7, delay_cost=1)
	S += Z_exp12 >= 78
	Z_exp12 += MM[0]

	DX6 = S.Task('DX6', length=7, delay_cost=1)
	S += DX6 >= 79
	DX6 += MM[0]

	DY6_ = S.Task('DY6_', length=2, delay_cost=1)
	S += DY6_ >= 79
	DY6_ += MAS[1]

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	S += k3_5_Z11_in >= 79
	k3_5_Z11_in += MM_in[0]

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	S += k3_5_Z11_mem0 >= 79
	k3_5_Z11_mem0 += MAIN_MEM_r[0]

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	S += k3_5_Z11_mem1 >= 79
	k3_5_Z11_mem1 += MM_MEM[1]

	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	S += k1_1_Z10_in >= 80
	k1_1_Z10_in += MM_in[0]

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	S += k1_1_Z10_mem0 >= 80
	k1_1_Z10_mem0 += MAIN_MEM_r[0]

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	S += k1_1_Z10_mem1 >= 80
	k1_1_Z10_mem1 += MM_MEM[1]

	k3_5_Z11 = S.Task('k3_5_Z11', length=7, delay_cost=1)
	S += k3_5_Z11 >= 80
	k3_5_Z11 += MM[0]

	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	S += DY6_in >= 81
	DY6_in += MM_in[0]

	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	S += DY6_mem0 >= 81
	DY6_mem0 += MAS_MEM[2]

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	S += DY6_mem1 >= 81
	DY6_mem1 += MAIN_MEM_r[1]

	NY7__in = S.Task('NY7__in', length=1, delay_cost=1)
	S += NY7__in >= 81
	NY7__in += MAS_in[0]

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	S += NY7__mem0 >= 81
	NY7__mem0 += MM_MEM[0]

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	S += NY7__mem1 >= 81
	NY7__mem1 += MM_MEM[1]

	k1_1_Z10 = S.Task('k1_1_Z10', length=7, delay_cost=1)
	S += k1_1_Z10 >= 81
	k1_1_Z10 += MM[0]

	DY6 = S.Task('DY6', length=7, delay_cost=1)
	S += DY6 >= 82
	DY6 += MM[0]

	NY7_ = S.Task('NY7_', length=2, delay_cost=1)
	S += NY7_ >= 82
	NY7_ += MAS[0]

	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	S += k2_4_Z11_in >= 82
	k2_4_Z11_in += MM_in[0]

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	S += k2_4_Z11_mem0 >= 82
	k2_4_Z11_mem0 += MAIN_MEM_r[0]

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	S += k2_4_Z11_mem1 >= 82
	k2_4_Z11_mem1 += MM_MEM[1]

	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	S += k0_0_Z11_in >= 83
	k0_0_Z11_in += MM_in[0]

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	S += k0_0_Z11_mem0 >= 83
	k0_0_Z11_mem0 += MAIN_MEM_r[0]

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	S += k0_0_Z11_mem1 >= 83
	k0_0_Z11_mem1 += MM_MEM[1]

	k2_4_Z11 = S.Task('k2_4_Z11', length=7, delay_cost=1)
	S += k2_4_Z11 >= 83
	k2_4_Z11 += MM[0]

	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	S += Z_exp13_in >= 84
	Z_exp13_in += MM_in[0]

	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	S += Z_exp13_mem0 >= 84
	Z_exp13_mem0 += MM_MEM[0]

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	S += Z_exp13_mem1 >= 84
	Z_exp13_mem1 += MAIN_MEM_r[1]

	k0_0_Z11 = S.Task('k0_0_Z11', length=7, delay_cost=1)
	S += k0_0_Z11 >= 84
	k0_0_Z11 += MM[0]

	Z_exp13 = S.Task('Z_exp13', length=7, delay_cost=1)
	S += Z_exp13 >= 85
	Z_exp13 += MM[0]

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	S += k1_0_Z11_in >= 85
	k1_0_Z11_in += MM_in[0]

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	S += k1_0_Z11_mem0 >= 85
	k1_0_Z11_mem0 += MAIN_MEM_r[0]

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	S += k1_0_Z11_mem1 >= 85
	k1_0_Z11_mem1 += MM_MEM[1]

	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	S += k0_2_Z9_in >= 86
	k0_2_Z9_in += MM_in[0]

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	S += k0_2_Z9_mem0 >= 86
	k0_2_Z9_mem0 += MAIN_MEM_r[0]

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	S += k0_2_Z9_mem1 >= 86
	k0_2_Z9_mem1 += MM_MEM[1]

	k1_0_Z11 = S.Task('k1_0_Z11', length=7, delay_cost=1)
	S += k1_0_Z11 >= 86
	k1_0_Z11 += MM[0]

	k0_2_Z9 = S.Task('k0_2_Z9', length=7, delay_cost=1)
	S += k0_2_Z9 >= 87
	k0_2_Z9 += MM[0]

	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	S += k3_4_Z12_in >= 87
	k3_4_Z12_in += MM_in[0]

	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	S += k3_4_Z12_mem0 >= 87
	k3_4_Z12_mem0 += MAIN_MEM_r[0]

	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	S += k3_4_Z12_mem1 >= 87
	k3_4_Z12_mem1 += MM_MEM[1]

	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	S += k2_3_Z12_in >= 88
	k2_3_Z12_in += MM_in[0]

	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	S += k2_3_Z12_mem0 >= 88
	k2_3_Z12_mem0 += MAIN_MEM_r[0]

	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	S += k2_3_Z12_mem1 >= 88
	k2_3_Z12_mem1 += MM_MEM[1]

	k3_4_Z12 = S.Task('k3_4_Z12', length=7, delay_cost=1)
	S += k3_4_Z12 >= 88
	k3_4_Z12 += MM[0]

	NX7__in = S.Task('NX7__in', length=1, delay_cost=1)
	S += NX7__in >= 89
	NX7__in += MAS_in[0]

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	S += NX7__mem0 >= 89
	NX7__mem0 += MM_MEM[0]

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	S += NX7__mem1 >= 89
	NX7__mem1 += MM_MEM[1]

	k2_3_Z12 = S.Task('k2_3_Z12', length=7, delay_cost=1)
	S += k2_3_Z12 >= 89
	k2_3_Z12 += MM[0]

	NX7_ = S.Task('NX7_', length=2, delay_cost=1)
	S += NX7_ >= 90
	NX7_ += MAS[0]

	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	S += Z_exp14_in >= 91
	Z_exp14_in += MM_in[0]

	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	S += Z_exp14_mem0 >= 91
	Z_exp14_mem0 += MM_MEM[0]

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	S += Z_exp14_mem1 >= 91
	Z_exp14_mem1 += MAIN_MEM_r[1]

	Z_exp14 = S.Task('Z_exp14', length=7, delay_cost=1)
	S += Z_exp14 >= 92
	Z_exp14 += MM[0]

	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	S += k2_2_Z13_in >= 92
	k2_2_Z13_in += MM_in[0]

	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	S += k2_2_Z13_mem0 >= 92
	k2_2_Z13_mem0 += MAIN_MEM_r[0]

	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	S += k2_2_Z13_mem1 >= 92
	k2_2_Z13_mem1 += MM_MEM[1]

	k2_2_Z13 = S.Task('k2_2_Z13', length=7, delay_cost=1)
	S += k2_2_Z13 >= 93
	k2_2_Z13 += MM[0]

	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	S += k3_3_Z13_in >= 93
	k3_3_Z13_in += MM_in[0]

	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	S += k3_3_Z13_mem0 >= 93
	k3_3_Z13_mem0 += MAIN_MEM_r[0]

	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	S += k3_3_Z13_mem1 >= 93
	k3_3_Z13_mem1 += MM_MEM[1]

	k3_3_Z13 = S.Task('k3_3_Z13', length=7, delay_cost=1)
	S += k3_3_Z13 >= 94
	k3_3_Z13 += MM[0]

	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	S += k3_2_Z14_in >= 98
	k3_2_Z14_in += MM_in[0]

	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	S += k3_2_Z14_mem0 >= 98
	k3_2_Z14_mem0 += MAIN_MEM_r[0]

	k3_2_Z14_mem1 = S.Task('k3_2_Z14_mem1', length=1, delay_cost=1)
	S += k3_2_Z14_mem1 >= 98
	k3_2_Z14_mem1 += MM_MEM[1]

	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	S += Z_exp15_in >= 99
	Z_exp15_in += MM_in[0]

	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	S += Z_exp15_mem0 >= 99
	Z_exp15_mem0 += MM_MEM[0]

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	S += Z_exp15_mem1 >= 99
	Z_exp15_mem1 += MAIN_MEM_r[1]

	k3_2_Z14 = S.Task('k3_2_Z14', length=7, delay_cost=1)
	S += k3_2_Z14 >= 99
	k3_2_Z14 += MM[0]

	Z_exp15 = S.Task('Z_exp15', length=7, delay_cost=1)
	S += Z_exp15 >= 100
	Z_exp15 += MM[0]

	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	S += k2_1_Z14_in >= 100
	k2_1_Z14_in += MM_in[0]

	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	S += k2_1_Z14_mem0 >= 100
	k2_1_Z14_mem0 += MAIN_MEM_r[0]

	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	S += k2_1_Z14_mem1 >= 100
	k2_1_Z14_mem1 += MM_MEM[1]

	k2_1_Z14 = S.Task('k2_1_Z14', length=7, delay_cost=1)
	S += k2_1_Z14 >= 101
	k2_1_Z14 += MM[0]


	# new tasks
	Z_exp16 = S.Task('Z_exp16', length=7, delay_cost=1)
	Z_exp16 += alt(MM)
	Z_exp16_in = S.Task('Z_exp16_in', length=1, delay_cost=1)
	Z_exp16_in += alt(MM_in)
	S += Z_exp16_in*MM_in[0]<=Z_exp16*MM[0]
	Z_exp16_mem0 = S.Task('Z_exp16_mem0', length=1, delay_cost=1)
	Z_exp16_mem0 += MM_MEM[0]
	S += 106 < Z_exp16_mem0
	S += Z_exp16_mem0 <= Z_exp16

	Z_exp16_mem1 = S.Task('Z_exp16_mem1', length=1, delay_cost=1)
	Z_exp16_mem1 += MAIN_MEM_r[1]
	S += Z_exp16_mem1 <= Z_exp16

	NX7 = S.Task('NX7', length=7, delay_cost=1)
	NX7 += alt(MM)
	NX7_in = S.Task('NX7_in', length=1, delay_cost=1)
	NX7_in += alt(MM_in)
	S += NX7_in*MM_in[0]<=NX7*MM[0]
	NX7_mem0 = S.Task('NX7_mem0', length=1, delay_cost=1)
	NX7_mem0 += MAS_MEM[0]
	S += 91 < NX7_mem0
	S += NX7_mem0 <= NX7

	NX7_mem1 = S.Task('NX7_mem1', length=1, delay_cost=1)
	NX7_mem1 += MAIN_MEM_r[1]
	S += NX7_mem1 <= NX7

	DX7_ = S.Task('DX7_', length=2, delay_cost=1)
	DX7_ += alt(MAS)
	DX7__in = S.Task('DX7__in', length=1, delay_cost=1)
	DX7__in += alt(MAS_in)
	S += DX7__in*MAS_in[0]<=DX7_*MAS[0]

	S += DX7__in*MAS_in[1]<=DX7_*MAS[1]

	DX7__mem0 = S.Task('DX7__mem0', length=1, delay_cost=1)
	DX7__mem0 += MM_MEM[0]
	S += 85 < DX7__mem0
	S += DX7__mem0 <= DX7_

	DX7__mem1 = S.Task('DX7__mem1', length=1, delay_cost=1)
	DX7__mem1 += MM_MEM[1]
	S += 62 < DX7__mem1
	S += DX7__mem1 <= DX7_

	NY7 = S.Task('NY7', length=7, delay_cost=1)
	NY7 += alt(MM)
	NY7_in = S.Task('NY7_in', length=1, delay_cost=1)
	NY7_in += alt(MM_in)
	S += NY7_in*MM_in[0]<=NY7*MM[0]
	NY7_mem0 = S.Task('NY7_mem0', length=1, delay_cost=1)
	NY7_mem0 += MAS_MEM[0]
	S += 83 < NY7_mem0
	S += NY7_mem0 <= NY7

	NY7_mem1 = S.Task('NY7_mem1', length=1, delay_cost=1)
	NY7_mem1 += MAIN_MEM_r[1]
	S += NY7_mem1 <= NY7

	k2_0_Z15 = S.Task('k2_0_Z15', length=7, delay_cost=1)
	k2_0_Z15 += alt(MM)
	k2_0_Z15_in = S.Task('k2_0_Z15_in', length=1, delay_cost=1)
	k2_0_Z15_in += alt(MM_in)
	S += k2_0_Z15_in*MM_in[0]<=k2_0_Z15*MM[0]
	k2_0_Z15_mem0 = S.Task('k2_0_Z15_mem0', length=1, delay_cost=1)
	k2_0_Z15_mem0 += MAIN_MEM_r[0]
	S += k2_0_Z15_mem0 <= k2_0_Z15

	k2_0_Z15_mem1 = S.Task('k2_0_Z15_mem1', length=1, delay_cost=1)
	k2_0_Z15_mem1 += MM_MEM[1]
	S += 106 < k2_0_Z15_mem1
	S += k2_0_Z15_mem1 <= k2_0_Z15

	DY7_ = S.Task('DY7_', length=2, delay_cost=1)
	DY7_ += alt(MAS)
	DY7__in = S.Task('DY7__in', length=1, delay_cost=1)
	DY7__in += alt(MAS_in)
	S += DY7__in*MAS_in[0]<=DY7_*MAS[0]

	S += DY7__in*MAS_in[1]<=DY7_*MAS[1]

	DY7__mem0 = S.Task('DY7__mem0', length=1, delay_cost=1)
	DY7__mem0 += MM_MEM[0]
	S += 88 < DY7__mem0
	S += DY7__mem0 <= DY7_

	DY7__mem1 = S.Task('DY7__mem1', length=1, delay_cost=1)
	DY7__mem1 += MM_MEM[1]
	S += 60 < DY7__mem1
	S += DY7__mem1 <= DY7_

	k3_1_Z15 = S.Task('k3_1_Z15', length=7, delay_cost=1)
	k3_1_Z15 += alt(MM)
	k3_1_Z15_in = S.Task('k3_1_Z15_in', length=1, delay_cost=1)
	k3_1_Z15_in += alt(MM_in)
	S += k3_1_Z15_in*MM_in[0]<=k3_1_Z15*MM[0]
	k3_1_Z15_mem0 = S.Task('k3_1_Z15_mem0', length=1, delay_cost=1)
	k3_1_Z15_mem0 += MAIN_MEM_r[0]
	S += k3_1_Z15_mem0 <= k3_1_Z15

	k3_1_Z15_mem1 = S.Task('k3_1_Z15_mem1', length=1, delay_cost=1)
	k3_1_Z15_mem1 += MM_MEM[1]
	S += 106 < k3_1_Z15_mem1
	S += k3_1_Z15_mem1 <= k3_1_Z15

	NX8_ = S.Task('NX8_', length=2, delay_cost=1)
	NX8_ += alt(MAS)
	NX8__in = S.Task('NX8__in', length=1, delay_cost=1)
	NX8__in += alt(MAS_in)
	S += NX8__in*MAS_in[0]<=NX8_*MAS[0]

	S += NX8__in*MAS_in[1]<=NX8_*MAS[1]

	NX8__mem0 = S.Task('NX8__mem0', length=1, delay_cost=1)
	NX8__mem0 += alt(MM_MEM)
	S += (NX7*MM[0])-1 < NX8__mem0*MM_MEM[0]
	S += NX8__mem0 <= NX8_

	NX8__mem1 = S.Task('NX8__mem1', length=1, delay_cost=1)
	NX8__mem1 += MM_MEM[1]
	S += 61 < NX8__mem1
	S += NX8__mem1 <= NX8_

	DX7 = S.Task('DX7', length=7, delay_cost=1)
	DX7 += alt(MM)
	DX7_in = S.Task('DX7_in', length=1, delay_cost=1)
	DX7_in += alt(MM_in)
	S += DX7_in*MM_in[0]<=DX7*MM[0]
	DX7_mem0 = S.Task('DX7_mem0', length=1, delay_cost=1)
	DX7_mem0 += alt(MAS_MEM)
	S += (DX7_*MAS[0])-1 < DX7_mem0*MAS_MEM[0]
	S += (DX7_*MAS[1])-1 < DX7_mem0*MAS_MEM[2]
	S += DX7_mem0 <= DX7

	DX7_mem1 = S.Task('DX7_mem1', length=1, delay_cost=1)
	DX7_mem1 += MAIN_MEM_r[1]
	S += DX7_mem1 <= DX7

	NY8_ = S.Task('NY8_', length=2, delay_cost=1)
	NY8_ += alt(MAS)
	NY8__in = S.Task('NY8__in', length=1, delay_cost=1)
	NY8__in += alt(MAS_in)
	S += NY8__in*MAS_in[0]<=NY8_*MAS[0]

	S += NY8__in*MAS_in[1]<=NY8_*MAS[1]

	NY8__mem0 = S.Task('NY8__mem0', length=1, delay_cost=1)
	NY8__mem0 += alt(MM_MEM)
	S += (NY7*MM[0])-1 < NY8__mem0*MM_MEM[0]
	S += NY8__mem0 <= NY8_

	NY8__mem1 = S.Task('NY8__mem1', length=1, delay_cost=1)
	NY8__mem1 += MM_MEM[1]
	S += 64 < NY8__mem1
	S += NY8__mem1 <= NY8_

	DY7 = S.Task('DY7', length=7, delay_cost=1)
	DY7 += alt(MM)
	DY7_in = S.Task('DY7_in', length=1, delay_cost=1)
	DY7_in += alt(MM_in)
	S += DY7_in*MM_in[0]<=DY7*MM[0]
	DY7_mem0 = S.Task('DY7_mem0', length=1, delay_cost=1)
	DY7_mem0 += alt(MAS_MEM)
	S += (DY7_*MAS[0])-1 < DY7_mem0*MAS_MEM[0]
	S += (DY7_*MAS[1])-1 < DY7_mem0*MAS_MEM[2]
	S += DY7_mem0 <= DY7

	DY7_mem1 = S.Task('DY7_mem1', length=1, delay_cost=1)
	DY7_mem1 += MAIN_MEM_r[1]
	S += DY7_mem1 <= DY7

	k3_0_Z16 = S.Task('k3_0_Z16', length=7, delay_cost=1)
	k3_0_Z16 += alt(MM)
	k3_0_Z16_in = S.Task('k3_0_Z16_in', length=1, delay_cost=1)
	k3_0_Z16_in += alt(MM_in)
	S += k3_0_Z16_in*MM_in[0]<=k3_0_Z16*MM[0]
	k3_0_Z16_mem0 = S.Task('k3_0_Z16_mem0', length=1, delay_cost=1)
	k3_0_Z16_mem0 += MAIN_MEM_r[0]
	S += k3_0_Z16_mem0 <= k3_0_Z16

	k3_0_Z16_mem1 = S.Task('k3_0_Z16_mem1', length=1, delay_cost=1)
	k3_0_Z16_mem1 += alt(MM_MEM)
	S += (Z_exp16*MM[0])-1 < k3_0_Z16_mem1*MM_MEM[1]
	S += k3_0_Z16_mem1 <= k3_0_Z16

	NX8 = S.Task('NX8', length=7, delay_cost=1)
	NX8 += alt(MM)
	NX8_in = S.Task('NX8_in', length=1, delay_cost=1)
	NX8_in += alt(MM_in)
	S += NX8_in*MM_in[0]<=NX8*MM[0]
	NX8_mem0 = S.Task('NX8_mem0', length=1, delay_cost=1)
	NX8_mem0 += alt(MAS_MEM)
	S += (NX8_*MAS[0])-1 < NX8_mem0*MAS_MEM[0]
	S += (NX8_*MAS[1])-1 < NX8_mem0*MAS_MEM[2]
	S += NX8_mem0 <= NX8

	NX8_mem1 = S.Task('NX8_mem1', length=1, delay_cost=1)
	NX8_mem1 += MAIN_MEM_r[1]
	S += NX8_mem1 <= NX8

	DX8_ = S.Task('DX8_', length=2, delay_cost=1)
	DX8_ += alt(MAS)
	DX8__in = S.Task('DX8__in', length=1, delay_cost=1)
	DX8__in += alt(MAS_in)
	S += DX8__in*MAS_in[0]<=DX8_*MAS[0]

	S += DX8__in*MAS_in[1]<=DX8_*MAS[1]

	DX8__mem0 = S.Task('DX8__mem0', length=1, delay_cost=1)
	DX8__mem0 += alt(MM_MEM)
	S += (DX7*MM[0])-1 < DX8__mem0*MM_MEM[0]
	S += DX8__mem0 <= DX8_

	DX8__mem1 = S.Task('DX8__mem1', length=1, delay_cost=1)
	DX8__mem1 += MM_MEM[1]
	S += 73 < DX8__mem1
	S += DX8__mem1 <= DX8_

	NY8 = S.Task('NY8', length=7, delay_cost=1)
	NY8 += alt(MM)
	NY8_in = S.Task('NY8_in', length=1, delay_cost=1)
	NY8_in += alt(MM_in)
	S += NY8_in*MM_in[0]<=NY8*MM[0]
	NY8_mem0 = S.Task('NY8_mem0', length=1, delay_cost=1)
	NY8_mem0 += alt(MAS_MEM)
	S += (NY8_*MAS[0])-1 < NY8_mem0*MAS_MEM[0]
	S += (NY8_*MAS[1])-1 < NY8_mem0*MAS_MEM[2]
	S += NY8_mem0 <= NY8

	NY8_mem1 = S.Task('NY8_mem1', length=1, delay_cost=1)
	NY8_mem1 += MAIN_MEM_r[1]
	S += NY8_mem1 <= NY8

	DY8_ = S.Task('DY8_', length=2, delay_cost=1)
	DY8_ += alt(MAS)
	DY8__in = S.Task('DY8__in', length=1, delay_cost=1)
	DY8__in += alt(MAS_in)
	S += DY8__in*MAS_in[0]<=DY8_*MAS[0]

	S += DY8__in*MAS_in[1]<=DY8_*MAS[1]

	DY8__mem0 = S.Task('DY8__mem0', length=1, delay_cost=1)
	DY8__mem0 += alt(MM_MEM)
	S += (DY7*MM[0])-1 < DY8__mem0*MM_MEM[0]
	S += DY8__mem0 <= DY8_

	DY8__mem1 = S.Task('DY8__mem1', length=1, delay_cost=1)
	DY8__mem1 += MM_MEM[1]
	S += 75 < DY8__mem1
	S += DY8__mem1 <= DY8_

	NX9_ = S.Task('NX9_', length=2, delay_cost=1)
	NX9_ += alt(MAS)
	NX9__in = S.Task('NX9__in', length=1, delay_cost=1)
	NX9__in += alt(MAS_in)
	S += NX9__in*MAS_in[0]<=NX9_*MAS[0]

	S += NX9__in*MAS_in[1]<=NX9_*MAS[1]

	NX9__mem0 = S.Task('NX9__mem0', length=1, delay_cost=1)
	NX9__mem0 += alt(MM_MEM)
	S += (NX8*MM[0])-1 < NX9__mem0*MM_MEM[0]
	S += NX9__mem0 <= NX9_

	NX9__mem1 = S.Task('NX9__mem1', length=1, delay_cost=1)
	NX9__mem1 += MM_MEM[1]
	S += 93 < NX9__mem1
	S += NX9__mem1 <= NX9_

	DX8 = S.Task('DX8', length=7, delay_cost=1)
	DX8 += alt(MM)
	DX8_in = S.Task('DX8_in', length=1, delay_cost=1)
	DX8_in += alt(MM_in)
	S += DX8_in*MM_in[0]<=DX8*MM[0]
	DX8_mem0 = S.Task('DX8_mem0', length=1, delay_cost=1)
	DX8_mem0 += alt(MAS_MEM)
	S += (DX8_*MAS[0])-1 < DX8_mem0*MAS_MEM[0]
	S += (DX8_*MAS[1])-1 < DX8_mem0*MAS_MEM[2]
	S += DX8_mem0 <= DX8

	DX8_mem1 = S.Task('DX8_mem1', length=1, delay_cost=1)
	DX8_mem1 += MAIN_MEM_r[1]
	S += DX8_mem1 <= DX8

	NY9_ = S.Task('NY9_', length=2, delay_cost=1)
	NY9_ += alt(MAS)
	NY9__in = S.Task('NY9__in', length=1, delay_cost=1)
	NY9__in += alt(MAS_in)
	S += NY9__in*MAS_in[0]<=NY9_*MAS[0]

	S += NY9__in*MAS_in[1]<=NY9_*MAS[1]

	NY9__mem0 = S.Task('NY9__mem0', length=1, delay_cost=1)
	NY9__mem0 += alt(MM_MEM)
	S += (NY8*MM[0])-1 < NY9__mem0*MM_MEM[0]
	S += NY9__mem0 <= NY9_

	NY9__mem1 = S.Task('NY9__mem1', length=1, delay_cost=1)
	NY9__mem1 += MM_MEM[1]
	S += 71 < NY9__mem1
	S += NY9__mem1 <= NY9_

	DY8 = S.Task('DY8', length=7, delay_cost=1)
	DY8 += alt(MM)
	DY8_in = S.Task('DY8_in', length=1, delay_cost=1)
	DY8_in += alt(MM_in)
	S += DY8_in*MM_in[0]<=DY8*MM[0]
	DY8_mem0 = S.Task('DY8_mem0', length=1, delay_cost=1)
	DY8_mem0 += alt(MAS_MEM)
	S += (DY8_*MAS[0])-1 < DY8_mem0*MAS_MEM[0]
	S += (DY8_*MAS[1])-1 < DY8_mem0*MAS_MEM[2]
	S += DY8_mem0 <= DY8

	DY8_mem1 = S.Task('DY8_mem1', length=1, delay_cost=1)
	DY8_mem1 += MAIN_MEM_r[1]
	S += DY8_mem1 <= DY8

	NX9 = S.Task('NX9', length=7, delay_cost=1)
	NX9 += alt(MM)
	NX9_in = S.Task('NX9_in', length=1, delay_cost=1)
	NX9_in += alt(MM_in)
	S += NX9_in*MM_in[0]<=NX9*MM[0]
	NX9_mem0 = S.Task('NX9_mem0', length=1, delay_cost=1)
	NX9_mem0 += alt(MAS_MEM)
	S += (NX9_*MAS[0])-1 < NX9_mem0*MAS_MEM[0]
	S += (NX9_*MAS[1])-1 < NX9_mem0*MAS_MEM[2]
	S += NX9_mem0 <= NX9

	NX9_mem1 = S.Task('NX9_mem1', length=1, delay_cost=1)
	NX9_mem1 += MAIN_MEM_r[1]
	S += NX9_mem1 <= NX9

	DX9_ = S.Task('DX9_', length=2, delay_cost=1)
	DX9_ += alt(MAS)
	DX9__in = S.Task('DX9__in', length=1, delay_cost=1)
	DX9__in += alt(MAS_in)
	S += DX9__in*MAS_in[0]<=DX9_*MAS[0]

	S += DX9__in*MAS_in[1]<=DX9_*MAS[1]

	DX9__mem0 = S.Task('DX9__mem0', length=1, delay_cost=1)
	DX9__mem0 += alt(MM_MEM)
	S += (DX8*MM[0])-1 < DX9__mem0*MM_MEM[0]
	S += DX9__mem0 <= DX9_

	DX9__mem1 = S.Task('DX9__mem1', length=1, delay_cost=1)
	DX9__mem1 += MM_MEM[1]
	S += 87 < DX9__mem1
	S += DX9__mem1 <= DX9_

	NY9 = S.Task('NY9', length=7, delay_cost=1)
	NY9 += alt(MM)
	NY9_in = S.Task('NY9_in', length=1, delay_cost=1)
	NY9_in += alt(MM_in)
	S += NY9_in*MM_in[0]<=NY9*MM[0]
	NY9_mem0 = S.Task('NY9_mem0', length=1, delay_cost=1)
	NY9_mem0 += alt(MAS_MEM)
	S += (NY9_*MAS[0])-1 < NY9_mem0*MAS_MEM[0]
	S += (NY9_*MAS[1])-1 < NY9_mem0*MAS_MEM[2]
	S += NY9_mem0 <= NY9

	NY9_mem1 = S.Task('NY9_mem1', length=1, delay_cost=1)
	NY9_mem1 += MAIN_MEM_r[1]
	S += NY9_mem1 <= NY9

	DY9_ = S.Task('DY9_', length=2, delay_cost=1)
	DY9_ += alt(MAS)
	DY9__in = S.Task('DY9__in', length=1, delay_cost=1)
	DY9__in += alt(MAS_in)
	S += DY9__in*MAS_in[0]<=DY9_*MAS[0]

	S += DY9__in*MAS_in[1]<=DY9_*MAS[1]

	DY9__mem0 = S.Task('DY9__mem0', length=1, delay_cost=1)
	DY9__mem0 += alt(MM_MEM)
	S += (DY8*MM[0])-1 < DY9__mem0*MM_MEM[0]
	S += DY9__mem0 <= DY9_

	DY9__mem1 = S.Task('DY9__mem1', length=1, delay_cost=1)
	DY9__mem1 += MM_MEM[1]
	S += 80 < DY9__mem1
	S += DY9__mem1 <= DY9_

	NX10_ = S.Task('NX10_', length=2, delay_cost=1)
	NX10_ += alt(MAS)
	NX10__in = S.Task('NX10__in', length=1, delay_cost=1)
	NX10__in += alt(MAS_in)
	S += NX10__in*MAS_in[0]<=NX10_*MAS[0]

	S += NX10__in*MAS_in[1]<=NX10_*MAS[1]

	NX10__mem0 = S.Task('NX10__mem0', length=1, delay_cost=1)
	NX10__mem0 += alt(MM_MEM)
	S += (NX9*MM[0])-1 < NX10__mem0*MM_MEM[0]
	S += NX10__mem0 <= NX10_

	NX10__mem1 = S.Task('NX10__mem1', length=1, delay_cost=1)
	NX10__mem1 += MM_MEM[1]
	S += 79 < NX10__mem1
	S += NX10__mem1 <= NX10_

	DX9 = S.Task('DX9', length=7, delay_cost=1)
	DX9 += alt(MM)
	DX9_in = S.Task('DX9_in', length=1, delay_cost=1)
	DX9_in += alt(MM_in)
	S += DX9_in*MM_in[0]<=DX9*MM[0]
	DX9_mem0 = S.Task('DX9_mem0', length=1, delay_cost=1)
	DX9_mem0 += alt(MAS_MEM)
	S += (DX9_*MAS[0])-1 < DX9_mem0*MAS_MEM[0]
	S += (DX9_*MAS[1])-1 < DX9_mem0*MAS_MEM[2]
	S += DX9_mem0 <= DX9

	DX9_mem1 = S.Task('DX9_mem1', length=1, delay_cost=1)
	DX9_mem1 += MAIN_MEM_r[1]
	S += DX9_mem1 <= DX9

	NY10_ = S.Task('NY10_', length=2, delay_cost=1)
	NY10_ += alt(MAS)
	NY10__in = S.Task('NY10__in', length=1, delay_cost=1)
	NY10__in += alt(MAS_in)
	S += NY10__in*MAS_in[0]<=NY10_*MAS[0]

	S += NY10__in*MAS_in[1]<=NY10_*MAS[1]

	NY10__mem0 = S.Task('NY10__mem0', length=1, delay_cost=1)
	NY10__mem0 += alt(MM_MEM)
	S += (NY9*MM[0])-1 < NY10__mem0*MM_MEM[0]
	S += NY10__mem0 <= NY10_

	NY10__mem1 = S.Task('NY10__mem1', length=1, delay_cost=1)
	NY10__mem1 += MM_MEM[1]
	S += 82 < NY10__mem1
	S += NY10__mem1 <= NY10_

	DY9 = S.Task('DY9', length=7, delay_cost=1)
	DY9 += alt(MM)
	DY9_in = S.Task('DY9_in', length=1, delay_cost=1)
	DY9_in += alt(MM_in)
	S += DY9_in*MM_in[0]<=DY9*MM[0]
	DY9_mem0 = S.Task('DY9_mem0', length=1, delay_cost=1)
	DY9_mem0 += alt(MAS_MEM)
	S += (DY9_*MAS[0])-1 < DY9_mem0*MAS_MEM[0]
	S += (DY9_*MAS[1])-1 < DY9_mem0*MAS_MEM[2]
	S += DY9_mem0 <= DY9

	DY9_mem1 = S.Task('DY9_mem1', length=1, delay_cost=1)
	DY9_mem1 += MAIN_MEM_r[1]
	S += DY9_mem1 <= DY9

	NX10 = S.Task('NX10', length=7, delay_cost=1)
	NX10 += alt(MM)
	NX10_in = S.Task('NX10_in', length=1, delay_cost=1)
	NX10_in += alt(MM_in)
	S += NX10_in*MM_in[0]<=NX10*MM[0]
	NX10_mem0 = S.Task('NX10_mem0', length=1, delay_cost=1)
	NX10_mem0 += alt(MAS_MEM)
	S += (NX10_*MAS[0])-1 < NX10_mem0*MAS_MEM[0]
	S += (NX10_*MAS[1])-1 < NX10_mem0*MAS_MEM[2]
	S += NX10_mem0 <= NX10

	NX10_mem1 = S.Task('NX10_mem1', length=1, delay_cost=1)
	NX10_mem1 += MAIN_MEM_r[1]
	S += NX10_mem1 <= NX10

	DX = S.Task('DX', length=2, delay_cost=1)
	DX += alt(MAS)
	DX_in = S.Task('DX_in', length=1, delay_cost=1)
	DX_in += alt(MAS_in)
	S += DX_in*MAS_in[0]<=DX*MAS[0]

	S += DX_in*MAS_in[1]<=DX*MAS[1]

	DX_mem0 = S.Task('DX_mem0', length=1, delay_cost=1)
	DX_mem0 += alt(MM_MEM)
	S += (DX9*MM[0])-1 < DX_mem0*MM_MEM[0]
	S += DX_mem0 <= DX

	DX_mem1 = S.Task('DX_mem1', length=1, delay_cost=1)
	DX_mem1 += MM_MEM[1]
	S += 92 < DX_mem1
	S += DX_mem1 <= DX

	NY10 = S.Task('NY10', length=7, delay_cost=1)
	NY10 += alt(MM)
	NY10_in = S.Task('NY10_in', length=1, delay_cost=1)
	NY10_in += alt(MM_in)
	S += NY10_in*MM_in[0]<=NY10*MM[0]
	NY10_mem0 = S.Task('NY10_mem0', length=1, delay_cost=1)
	NY10_mem0 += alt(MAS_MEM)
	S += (NY10_*MAS[0])-1 < NY10_mem0*MAS_MEM[0]
	S += (NY10_*MAS[1])-1 < NY10_mem0*MAS_MEM[2]
	S += NY10_mem0 <= NY10

	NY10_mem1 = S.Task('NY10_mem1', length=1, delay_cost=1)
	NY10_mem1 += MAIN_MEM_r[1]
	S += NY10_mem1 <= NY10

	DY10_ = S.Task('DY10_', length=2, delay_cost=1)
	DY10_ += alt(MAS)
	DY10__in = S.Task('DY10__in', length=1, delay_cost=1)
	DY10__in += alt(MAS_in)
	S += DY10__in*MAS_in[0]<=DY10_*MAS[0]

	S += DY10__in*MAS_in[1]<=DY10_*MAS[1]

	DY10__mem0 = S.Task('DY10__mem0', length=1, delay_cost=1)
	DY10__mem0 += alt(MM_MEM)
	S += (DY9*MM[0])-1 < DY10__mem0*MM_MEM[0]
	S += DY10__mem0 <= DY10_

	DY10__mem1 = S.Task('DY10__mem1', length=1, delay_cost=1)
	DY10__mem1 += MM_MEM[1]
	S += 86 < DY10__mem1
	S += DY10__mem1 <= DY10_

	NX = S.Task('NX', length=2, delay_cost=1)
	NX += alt(MAS)
	NX_in = S.Task('NX_in', length=1, delay_cost=1)
	NX_in += alt(MAS_in)
	S += NX_in*MAS_in[0]<=NX*MAS[0]

	S += NX_in*MAS_in[1]<=NX*MAS[1]

	NX_mem0 = S.Task('NX_mem0', length=1, delay_cost=1)
	NX_mem0 += alt(MM_MEM)
	S += (NX10*MM[0])-1 < NX_mem0*MM_MEM[0]
	S += NX_mem0 <= NX

	NX_mem1 = S.Task('NX_mem1', length=1, delay_cost=1)
	NX_mem1 += MM_MEM[1]
	S += 90 < NX_mem1
	S += NX_mem1 <= NX

	NY11_ = S.Task('NY11_', length=2, delay_cost=1)
	NY11_ += alt(MAS)
	NY11__in = S.Task('NY11__in', length=1, delay_cost=1)
	NY11__in += alt(MAS_in)
	S += NY11__in*MAS_in[0]<=NY11_*MAS[0]

	S += NY11__in*MAS_in[1]<=NY11_*MAS[1]

	NY11__mem0 = S.Task('NY11__mem0', length=1, delay_cost=1)
	NY11__mem0 += alt(MM_MEM)
	S += (NY10*MM[0])-1 < NY11__mem0*MM_MEM[0]
	S += NY11__mem0 <= NY11_

	NY11__mem1 = S.Task('NY11__mem1', length=1, delay_cost=1)
	NY11__mem1 += MM_MEM[1]
	S += 89 < NY11__mem1
	S += NY11__mem1 <= NY11_

	DY10 = S.Task('DY10', length=7, delay_cost=1)
	DY10 += alt(MM)
	DY10_in = S.Task('DY10_in', length=1, delay_cost=1)
	DY10_in += alt(MM_in)
	S += DY10_in*MM_in[0]<=DY10*MM[0]
	DY10_mem0 = S.Task('DY10_mem0', length=1, delay_cost=1)
	DY10_mem0 += alt(MAS_MEM)
	S += (DY10_*MAS[0])-1 < DY10_mem0*MAS_MEM[0]
	S += (DY10_*MAS[1])-1 < DY10_mem0*MAS_MEM[2]
	S += DY10_mem0 <= DY10

	DY10_mem1 = S.Task('DY10_mem1', length=1, delay_cost=1)
	DY10_mem1 += MAIN_MEM_r[1]
	S += DY10_mem1 <= DY10

	NY11 = S.Task('NY11', length=7, delay_cost=1)
	NY11 += alt(MM)
	NY11_in = S.Task('NY11_in', length=1, delay_cost=1)
	NY11_in += alt(MM_in)
	S += NY11_in*MM_in[0]<=NY11*MM[0]
	NY11_mem0 = S.Task('NY11_mem0', length=1, delay_cost=1)
	NY11_mem0 += alt(MAS_MEM)
	S += (NY11_*MAS[0])-1 < NY11_mem0*MAS_MEM[0]
	S += (NY11_*MAS[1])-1 < NY11_mem0*MAS_MEM[2]
	S += NY11_mem0 <= NY11

	NY11_mem1 = S.Task('NY11_mem1', length=1, delay_cost=1)
	NY11_mem1 += MAIN_MEM_r[1]
	S += NY11_mem1 <= NY11

	DY11_ = S.Task('DY11_', length=2, delay_cost=1)
	DY11_ += alt(MAS)
	DY11__in = S.Task('DY11__in', length=1, delay_cost=1)
	DY11__in += alt(MAS_in)
	S += DY11__in*MAS_in[0]<=DY11_*MAS[0]

	S += DY11__in*MAS_in[1]<=DY11_*MAS[1]

	DY11__mem0 = S.Task('DY11__mem0', length=1, delay_cost=1)
	DY11__mem0 += alt(MM_MEM)
	S += (DY10*MM[0])-1 < DY11__mem0*MM_MEM[0]
	S += DY11__mem0 <= DY11_

	DY11__mem1 = S.Task('DY11__mem1', length=1, delay_cost=1)
	DY11__mem1 += MM_MEM[1]
	S += 94 < DY11__mem1
	S += DY11__mem1 <= DY11_

	NY12_ = S.Task('NY12_', length=2, delay_cost=1)
	NY12_ += alt(MAS)
	NY12__in = S.Task('NY12__in', length=1, delay_cost=1)
	NY12__in += alt(MAS_in)
	S += NY12__in*MAS_in[0]<=NY12_*MAS[0]

	S += NY12__in*MAS_in[1]<=NY12_*MAS[1]

	NY12__mem0 = S.Task('NY12__mem0', length=1, delay_cost=1)
	NY12__mem0 += alt(MM_MEM)
	S += (NY11*MM[0])-1 < NY12__mem0*MM_MEM[0]
	S += NY12__mem0 <= NY12_

	NY12__mem1 = S.Task('NY12__mem1', length=1, delay_cost=1)
	NY12__mem1 += MM_MEM[1]
	S += 95 < NY12__mem1
	S += NY12__mem1 <= NY12_

	DY11 = S.Task('DY11', length=7, delay_cost=1)
	DY11 += alt(MM)
	DY11_in = S.Task('DY11_in', length=1, delay_cost=1)
	DY11_in += alt(MM_in)
	S += DY11_in*MM_in[0]<=DY11*MM[0]
	DY11_mem0 = S.Task('DY11_mem0', length=1, delay_cost=1)
	DY11_mem0 += alt(MAS_MEM)
	S += (DY11_*MAS[0])-1 < DY11_mem0*MAS_MEM[0]
	S += (DY11_*MAS[1])-1 < DY11_mem0*MAS_MEM[2]
	S += DY11_mem0 <= DY11

	DY11_mem1 = S.Task('DY11_mem1', length=1, delay_cost=1)
	DY11_mem1 += MAIN_MEM_r[1]
	S += DY11_mem1 <= DY11

	NY12 = S.Task('NY12', length=7, delay_cost=1)
	NY12 += alt(MM)
	NY12_in = S.Task('NY12_in', length=1, delay_cost=1)
	NY12_in += alt(MM_in)
	S += NY12_in*MM_in[0]<=NY12*MM[0]
	NY12_mem0 = S.Task('NY12_mem0', length=1, delay_cost=1)
	NY12_mem0 += alt(MAS_MEM)
	S += (NY12_*MAS[0])-1 < NY12_mem0*MAS_MEM[0]
	S += (NY12_*MAS[1])-1 < NY12_mem0*MAS_MEM[2]
	S += NY12_mem0 <= NY12

	NY12_mem1 = S.Task('NY12_mem1', length=1, delay_cost=1)
	NY12_mem1 += MAIN_MEM_r[1]
	S += NY12_mem1 <= NY12

	DY12_ = S.Task('DY12_', length=2, delay_cost=1)
	DY12_ += alt(MAS)
	DY12__in = S.Task('DY12__in', length=1, delay_cost=1)
	DY12__in += alt(MAS_in)
	S += DY12__in*MAS_in[0]<=DY12_*MAS[0]

	S += DY12__in*MAS_in[1]<=DY12_*MAS[1]

	DY12__mem0 = S.Task('DY12__mem0', length=1, delay_cost=1)
	DY12__mem0 += alt(MM_MEM)
	S += (DY11*MM[0])-1 < DY12__mem0*MM_MEM[0]
	S += DY12__mem0 <= DY12_

	DY12__mem1 = S.Task('DY12__mem1', length=1, delay_cost=1)
	DY12__mem1 += MM_MEM[1]
	S += 100 < DY12__mem1
	S += DY12__mem1 <= DY12_

	NY13_ = S.Task('NY13_', length=2, delay_cost=1)
	NY13_ += alt(MAS)
	NY13__in = S.Task('NY13__in', length=1, delay_cost=1)
	NY13__in += alt(MAS_in)
	S += NY13__in*MAS_in[0]<=NY13_*MAS[0]

	S += NY13__in*MAS_in[1]<=NY13_*MAS[1]

	NY13__mem0 = S.Task('NY13__mem0', length=1, delay_cost=1)
	NY13__mem0 += alt(MM_MEM)
	S += (NY12*MM[0])-1 < NY13__mem0*MM_MEM[0]
	S += NY13__mem0 <= NY13_

	NY13__mem1 = S.Task('NY13__mem1', length=1, delay_cost=1)
	NY13__mem1 += MM_MEM[1]
	S += 99 < NY13__mem1
	S += NY13__mem1 <= NY13_

	DY12 = S.Task('DY12', length=7, delay_cost=1)
	DY12 += alt(MM)
	DY12_in = S.Task('DY12_in', length=1, delay_cost=1)
	DY12_in += alt(MM_in)
	S += DY12_in*MM_in[0]<=DY12*MM[0]
	DY12_mem0 = S.Task('DY12_mem0', length=1, delay_cost=1)
	DY12_mem0 += alt(MAS_MEM)
	S += (DY12_*MAS[0])-1 < DY12_mem0*MAS_MEM[0]
	S += (DY12_*MAS[1])-1 < DY12_mem0*MAS_MEM[2]
	S += DY12_mem0 <= DY12

	DY12_mem1 = S.Task('DY12_mem1', length=1, delay_cost=1)
	DY12_mem1 += MAIN_MEM_r[1]
	S += DY12_mem1 <= DY12

	NY13 = S.Task('NY13', length=7, delay_cost=1)
	NY13 += alt(MM)
	NY13_in = S.Task('NY13_in', length=1, delay_cost=1)
	NY13_in += alt(MM_in)
	S += NY13_in*MM_in[0]<=NY13*MM[0]
	NY13_mem0 = S.Task('NY13_mem0', length=1, delay_cost=1)
	NY13_mem0 += alt(MAS_MEM)
	S += (NY13_*MAS[0])-1 < NY13_mem0*MAS_MEM[0]
	S += (NY13_*MAS[1])-1 < NY13_mem0*MAS_MEM[2]
	S += NY13_mem0 <= NY13

	NY13_mem1 = S.Task('NY13_mem1', length=1, delay_cost=1)
	NY13_mem1 += MAIN_MEM_r[1]
	S += NY13_mem1 <= NY13

	DY13_ = S.Task('DY13_', length=2, delay_cost=1)
	DY13_ += alt(MAS)
	DY13__in = S.Task('DY13__in', length=1, delay_cost=1)
	DY13__in += alt(MAS_in)
	S += DY13__in*MAS_in[0]<=DY13_*MAS[0]

	S += DY13__in*MAS_in[1]<=DY13_*MAS[1]

	DY13__mem0 = S.Task('DY13__mem0', length=1, delay_cost=1)
	DY13__mem0 += alt(MM_MEM)
	S += (DY12*MM[0])-1 < DY13__mem0*MM_MEM[0]
	S += DY13__mem0 <= DY13_

	DY13__mem1 = S.Task('DY13__mem1', length=1, delay_cost=1)
	DY13__mem1 += MM_MEM[1]
	S += 105 < DY13__mem1
	S += DY13__mem1 <= DY13_

	NY14_ = S.Task('NY14_', length=2, delay_cost=1)
	NY14_ += alt(MAS)
	NY14__in = S.Task('NY14__in', length=1, delay_cost=1)
	NY14__in += alt(MAS_in)
	S += NY14__in*MAS_in[0]<=NY14_*MAS[0]

	S += NY14__in*MAS_in[1]<=NY14_*MAS[1]

	NY14__mem0 = S.Task('NY14__mem0', length=1, delay_cost=1)
	NY14__mem0 += alt(MM_MEM)
	S += (NY13*MM[0])-1 < NY14__mem0*MM_MEM[0]
	S += NY14__mem0 <= NY14_

	NY14__mem1 = S.Task('NY14__mem1', length=1, delay_cost=1)
	NY14__mem1 += MM_MEM[1]
	S += 107 < NY14__mem1
	S += NY14__mem1 <= NY14_

	DY13 = S.Task('DY13', length=7, delay_cost=1)
	DY13 += alt(MM)
	DY13_in = S.Task('DY13_in', length=1, delay_cost=1)
	DY13_in += alt(MM_in)
	S += DY13_in*MM_in[0]<=DY13*MM[0]
	DY13_mem0 = S.Task('DY13_mem0', length=1, delay_cost=1)
	DY13_mem0 += alt(MAS_MEM)
	S += (DY13_*MAS[0])-1 < DY13_mem0*MAS_MEM[0]
	S += (DY13_*MAS[1])-1 < DY13_mem0*MAS_MEM[2]
	S += DY13_mem0 <= DY13

	DY13_mem1 = S.Task('DY13_mem1', length=1, delay_cost=1)
	DY13_mem1 += MAIN_MEM_r[1]
	S += DY13_mem1 <= DY13

	NY14 = S.Task('NY14', length=7, delay_cost=1)
	NY14 += alt(MM)
	NY14_in = S.Task('NY14_in', length=1, delay_cost=1)
	NY14_in += alt(MM_in)
	S += NY14_in*MM_in[0]<=NY14*MM[0]
	NY14_mem0 = S.Task('NY14_mem0', length=1, delay_cost=1)
	NY14_mem0 += alt(MAS_MEM)
	S += (NY14_*MAS[0])-1 < NY14_mem0*MAS_MEM[0]
	S += (NY14_*MAS[1])-1 < NY14_mem0*MAS_MEM[2]
	S += NY14_mem0 <= NY14

	NY14_mem1 = S.Task('NY14_mem1', length=1, delay_cost=1)
	NY14_mem1 += MAIN_MEM_r[1]
	S += NY14_mem1 <= NY14

	DY14_ = S.Task('DY14_', length=2, delay_cost=1)
	DY14_ += alt(MAS)
	DY14__in = S.Task('DY14__in', length=1, delay_cost=1)
	DY14__in += alt(MAS_in)
	S += DY14__in*MAS_in[0]<=DY14_*MAS[0]

	S += DY14__in*MAS_in[1]<=DY14_*MAS[1]

	DY14__mem0 = S.Task('DY14__mem0', length=1, delay_cost=1)
	DY14__mem0 += alt(MM_MEM)
	S += (DY13*MM[0])-1 < DY14__mem0*MM_MEM[0]
	S += DY14__mem0 <= DY14_

	DY14__mem1 = S.Task('DY14__mem1', length=1, delay_cost=1)
	DY14__mem1 += alt(MM_MEM)
	S += (k3_1_Z15*MM[0])-1 < DY14__mem1*MM_MEM[1]
	S += DY14__mem1 <= DY14_

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM1_stage2MAS2/ISOGENY/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution

