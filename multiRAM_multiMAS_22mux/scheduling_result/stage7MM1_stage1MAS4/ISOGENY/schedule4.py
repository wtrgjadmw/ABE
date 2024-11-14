from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 212
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling
	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 0
	DX0_in += MM_in[0]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 0
	DX0_mem0 += MAIN_MEM_r

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 0
	DX0_mem1 += MAIN_MEM_r

	DX0 = S.Task('DX0', length=7, delay_cost=1)
	S += DX0 >= 1
	DX0 += MM[0]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 1
	k2_14_Z1_in += MM_in[0]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 1
	k2_14_Z1_mem0 += MAIN_MEM_r

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 1
	k2_14_Z1_mem1 += MAIN_MEM_r

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 2
	k0_10_Z1_in += MM_in[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 2
	k0_10_Z1_mem0 += MAIN_MEM_r

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 2
	k0_10_Z1_mem1 += MAIN_MEM_r

	k2_14_Z1 = S.Task('k2_14_Z1', length=7, delay_cost=1)
	S += k2_14_Z1 >= 2
	k2_14_Z1 += MM[0]

	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 3
	Z_exp2_in += MM_in[0]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 3
	Z_exp2_mem0 += MAIN_MEM_r

	Z_exp2_mem1 = S.Task('Z_exp2_mem1', length=1, delay_cost=1)
	S += Z_exp2_mem1 >= 3
	Z_exp2_mem1 += MAIN_MEM_r

	k0_10_Z1 = S.Task('k0_10_Z1', length=7, delay_cost=1)
	S += k0_10_Z1 >= 3
	k0_10_Z1 += MM[0]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 4
	NY0_in += MM_in[0]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 4
	NY0_mem0 += MAIN_MEM_r

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 4
	NY0_mem1 += MAIN_MEM_r

	Z_exp2 = S.Task('Z_exp2', length=7, delay_cost=1)
	S += Z_exp2 >= 4
	Z_exp2 += MM[0]

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 5
	NX0_in += MM_in[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 5
	NX0_mem0 += MAIN_MEM_r

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 5
	NX0_mem1 += MAIN_MEM_r

	NY0 = S.Task('NY0', length=7, delay_cost=1)
	S += NY0 >= 5
	NY0 += MM[0]

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 6
	DY0_in += MM_in[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 6
	DY0_mem0 += MAIN_MEM_r

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 6
	DY0_mem1 += MAIN_MEM_r

	NX0 = S.Task('NX0', length=7, delay_cost=1)
	S += NX0 >= 6
	NX0 += MM[0]

	DY0 = S.Task('DY0', length=7, delay_cost=1)
	S += DY0 >= 7
	DY0 += MM[0]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 10
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 10
	k1_9_Z2_mem0 += MAIN_MEM_r

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 10
	k1_9_Z2_mem1 += MM_MEM[0]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 11
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 11
	Z_exp3_mem0 += MM_MEM[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 11
	Z_exp3_mem1 += MAIN_MEM_r

	k1_9_Z2 = S.Task('k1_9_Z2', length=7, delay_cost=1)
	S += k1_9_Z2 >= 11
	k1_9_Z2 += MM[0]

	Z_exp3 = S.Task('Z_exp3', length=7, delay_cost=1)
	S += Z_exp3 >= 12
	Z_exp3 += MM[0]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 12
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 12
	k3_14_Z2_mem0 += MAIN_MEM_r

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 12
	k3_14_Z2_mem1 += MM_MEM[0]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 13
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 13
	NY1__mem1 += MM_MEM[0]

	k3_14_Z2 = S.Task('k3_14_Z2', length=7, delay_cost=1)
	S += k3_14_Z2 >= 13
	k3_14_Z2 += MM[0]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 14
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 14
	NX1__mem1 += MM_MEM[0]

	NY1_ = S.Task('NY1_', length=1, delay_cost=1)
	S += NY1_ >= 14
	NY1_ += MAS[0]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 14
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 14
	NY1_mem0 += MAS_MEM[0]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 14
	NY1_mem1 += MAIN_MEM_r

	NX1_ = S.Task('NX1_', length=1, delay_cost=1)
	S += NX1_ >= 15
	NX1_ += MAS[0]

	NY1 = S.Task('NY1', length=7, delay_cost=1)
	S += NY1 >= 15
	NY1 += MM[0]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 15
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 15
	k2_13_Z2_mem0 += MAIN_MEM_r

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 15
	k2_13_Z2_mem1 += MM_MEM[0]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 16
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 16
	k0_9_Z2_mem0 += MAIN_MEM_r

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 16
	k0_9_Z2_mem1 += MM_MEM[0]

	k2_13_Z2 = S.Task('k2_13_Z2', length=7, delay_cost=1)
	S += k2_13_Z2 >= 16
	k2_13_Z2 += MM[0]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 17
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 17
	DX1__mem1 += MM_MEM[0]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 17
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 17
	NX1_mem0 += MAS_MEM[0]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 17
	NX1_mem1 += MAIN_MEM_r

	k0_9_Z2 = S.Task('k0_9_Z2', length=7, delay_cost=1)
	S += k0_9_Z2 >= 17
	k0_9_Z2 += MM[0]

	DX1_ = S.Task('DX1_', length=1, delay_cost=1)
	S += DX1_ >= 18
	DX1_ += MAS[3]

	NX1 = S.Task('NX1', length=7, delay_cost=1)
	S += NX1 >= 18
	NX1 += MM[0]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 18
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 18
	Z_exp4_mem0 += MM_MEM[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 18
	Z_exp4_mem1 += MAIN_MEM_r

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 19
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 19
	DX1_mem0 += MAS_MEM[3]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 19
	DX1_mem1 += MAIN_MEM_r

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 19
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 19
	DY1__mem1 += MM_MEM[0]

	Z_exp4 = S.Task('Z_exp4', length=7, delay_cost=1)
	S += Z_exp4 >= 19
	Z_exp4 += MM[0]

	DX1 = S.Task('DX1', length=7, delay_cost=1)
	S += DX1 >= 20
	DX1 += MM[0]

	DY1_ = S.Task('DY1_', length=1, delay_cost=1)
	S += DY1_ >= 20
	DY1_ += MAS[0]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 20
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 20
	k1_8_Z3_mem0 += MAIN_MEM_r

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 20
	k1_8_Z3_mem1 += MM_MEM[0]

	k1_8_Z3 = S.Task('k1_8_Z3', length=7, delay_cost=1)
	S += k1_8_Z3 >= 21
	k1_8_Z3 += MM[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 21
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 21
	k3_13_Z3_mem0 += MAIN_MEM_r

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 21
	k3_13_Z3_mem1 += MM_MEM[0]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 22
	DY1_in += MM_in[0]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 22
	DY1_mem0 += MAS_MEM[0]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 22
	DY1_mem1 += MAIN_MEM_r

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 22
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 22
	NY2__mem1 += MM_MEM[0]

	k3_13_Z3 = S.Task('k3_13_Z3', length=7, delay_cost=1)
	S += k3_13_Z3 >= 22
	k3_13_Z3 += MM[0]

	DY1 = S.Task('DY1', length=7, delay_cost=1)
	S += DY1 >= 23
	DY1 += MM[0]

	NY2_ = S.Task('NY2_', length=1, delay_cost=1)
	S += NY2_ >= 23
	NY2_ += MAS[0]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 23
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 23
	k2_12_Z3_mem0 += MAIN_MEM_r

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 23
	k2_12_Z3_mem1 += MM_MEM[0]

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 24
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 24
	NX2__mem1 += MM_MEM[0]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 24
	NY2_in += MM_in[0]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 24
	NY2_mem0 += MAS_MEM[0]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 24
	NY2_mem1 += MAIN_MEM_r

	k2_12_Z3 = S.Task('k2_12_Z3', length=7, delay_cost=1)
	S += k2_12_Z3 >= 24
	k2_12_Z3 += MM[0]

	NX2_ = S.Task('NX2_', length=1, delay_cost=1)
	S += NX2_ >= 25
	NX2_ += MAS[2]

	NY2 = S.Task('NY2', length=7, delay_cost=1)
	S += NY2 >= 25
	NY2 += MM[0]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 25
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 25
	Z_exp5_mem0 += MM_MEM[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 25
	Z_exp5_mem1 += MAIN_MEM_r

	Z_exp5 = S.Task('Z_exp5', length=7, delay_cost=1)
	S += Z_exp5 >= 26
	Z_exp5 += MM[0]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 26
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 26
	k0_8_Z3_mem0 += MAIN_MEM_r

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 26
	k0_8_Z3_mem1 += MM_MEM[0]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 27
	DX2__mem0 += MM_MEM[0]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 27
	DX2__mem1 += MM_MEM[0]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 27
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 27
	NX2_mem0 += MAS_MEM[2]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 27
	NX2_mem1 += MAIN_MEM_r

	k0_8_Z3 = S.Task('k0_8_Z3', length=7, delay_cost=1)
	S += k0_8_Z3 >= 27
	k0_8_Z3 += MM[0]

	DX2_ = S.Task('DX2_', length=1, delay_cost=1)
	S += DX2_ >= 28
	DX2_ += MAS[2]

	NX2 = S.Task('NX2', length=7, delay_cost=1)
	S += NX2 >= 28
	NX2 += MM[0]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 28
	k1_7_Z4_in += MM_in[0]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 28
	k1_7_Z4_mem0 += MAIN_MEM_r

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 28
	k1_7_Z4_mem1 += MM_MEM[0]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 29
	DX2_in += MM_in[0]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 29
	DX2_mem0 += MAS_MEM[2]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 29
	DX2_mem1 += MAIN_MEM_r

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 29
	DY2__mem0 += MM_MEM[0]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 29
	DY2__mem1 += MM_MEM[0]

	k1_7_Z4 = S.Task('k1_7_Z4', length=7, delay_cost=1)
	S += k1_7_Z4 >= 29
	k1_7_Z4 += MM[0]

	DX2 = S.Task('DX2', length=7, delay_cost=1)
	S += DX2 >= 30
	DX2 += MM[0]

	DY2_ = S.Task('DY2_', length=1, delay_cost=1)
	S += DY2_ >= 30
	DY2_ += MAS[0]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 30
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 30
	k3_12_Z4_mem0 += MAIN_MEM_r

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 30
	k3_12_Z4_mem1 += MM_MEM[0]

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 31
	DY2_in += MM_in[0]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 31
	DY2_mem0 += MAS_MEM[0]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 31
	DY2_mem1 += MAIN_MEM_r

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 31
	NY3__mem0 += MM_MEM[0]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 31
	NY3__mem1 += MM_MEM[0]

	k3_12_Z4 = S.Task('k3_12_Z4', length=7, delay_cost=1)
	S += k3_12_Z4 >= 31
	k3_12_Z4 += MM[0]

	DY2 = S.Task('DY2', length=7, delay_cost=1)
	S += DY2 >= 32
	DY2 += MM[0]

	NY3_ = S.Task('NY3_', length=1, delay_cost=1)
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
	Z_exp6_mem1 += MAIN_MEM_r

	Z_exp6 = S.Task('Z_exp6', length=7, delay_cost=1)
	S += Z_exp6 >= 33
	Z_exp6 += MM[0]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 33
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 33
	k3_11_Z5_mem0 += MAIN_MEM_r

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 33
	k3_11_Z5_mem1 += MM_MEM[0]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 34
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 34
	k1_6_Z5_mem0 += MAIN_MEM_r

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 34
	k1_6_Z5_mem1 += MM_MEM[0]

	k3_11_Z5 = S.Task('k3_11_Z5', length=7, delay_cost=1)
	S += k3_11_Z5 >= 34
	k3_11_Z5 += MM[0]

	k1_6_Z5 = S.Task('k1_6_Z5', length=7, delay_cost=1)
	S += k1_6_Z5 >= 35
	k1_6_Z5 += MM[0]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 35
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 35
	k2_11_Z4_mem0 += MAIN_MEM_r

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 35
	k2_11_Z4_mem1 += MM_MEM[0]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 36
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 36
	k2_10_Z5_mem0 += MAIN_MEM_r

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 36
	k2_10_Z5_mem1 += MM_MEM[0]

	k2_11_Z4 = S.Task('k2_11_Z4', length=7, delay_cost=1)
	S += k2_11_Z4 >= 36
	k2_11_Z4 += MM[0]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 37
	k0_6_Z5_in += MM_in[0]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 37
	k0_6_Z5_mem0 += MAIN_MEM_r

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 37
	k0_6_Z5_mem1 += MM_MEM[0]

	k2_10_Z5 = S.Task('k2_10_Z5', length=7, delay_cost=1)
	S += k2_10_Z5 >= 37
	k2_10_Z5 += MM[0]

	k0_6_Z5 = S.Task('k0_6_Z5', length=7, delay_cost=1)
	S += k0_6_Z5 >= 38
	k0_6_Z5 += MM[0]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 38
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 38
	k0_7_Z4_mem0 += MAIN_MEM_r

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 38
	k0_7_Z4_mem1 += MM_MEM[0]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 39
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 39
	Z_exp7_mem0 += MM_MEM[0]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 39
	Z_exp7_mem1 += MAIN_MEM_r

	k0_7_Z4 = S.Task('k0_7_Z4', length=7, delay_cost=1)
	S += k0_7_Z4 >= 39
	k0_7_Z4 += MM[0]

	Z_exp7 = S.Task('Z_exp7', length=7, delay_cost=1)
	S += Z_exp7 >= 40
	Z_exp7 += MM[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 40
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 40
	k3_10_Z6_mem0 += MAIN_MEM_r

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 40
	k3_10_Z6_mem1 += MM_MEM[0]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 41
	k1_5_Z6_in += MM_in[0]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 41
	k1_5_Z6_mem0 += MAIN_MEM_r

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 41
	k1_5_Z6_mem1 += MM_MEM[0]

	k3_10_Z6 = S.Task('k3_10_Z6', length=7, delay_cost=1)
	S += k3_10_Z6 >= 41
	k3_10_Z6 += MM[0]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 42
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 42
	k0_5_Z6_mem0 += MAIN_MEM_r

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 42
	k0_5_Z6_mem1 += MM_MEM[0]

	k1_5_Z6 = S.Task('k1_5_Z6', length=7, delay_cost=1)
	S += k1_5_Z6 >= 42
	k1_5_Z6 += MM[0]

	k0_5_Z6 = S.Task('k0_5_Z6', length=7, delay_cost=1)
	S += k0_5_Z6 >= 43
	k0_5_Z6 += MM[0]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 43
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 43
	k2_9_Z6_mem0 += MAIN_MEM_r

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 43
	k2_9_Z6_mem1 += MM_MEM[0]

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 44
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 44
	NX3__mem1 += MM_MEM[0]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 44
	NY3_in += MM_in[0]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 44
	NY3_mem0 += MAS_MEM[0]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 44
	NY3_mem1 += MAIN_MEM_r

	k2_9_Z6 = S.Task('k2_9_Z6', length=7, delay_cost=1)
	S += k2_9_Z6 >= 44
	k2_9_Z6 += MM[0]

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	S += DY3__mem0 >= 45
	DY3__mem0 += MM_MEM[0]

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	S += DY3__mem1 >= 45
	DY3__mem1 += MM_MEM[0]

	NX3_ = S.Task('NX3_', length=1, delay_cost=1)
	S += NX3_ >= 45
	NX3_ += MAS[0]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 45
	NX3_in += MM_in[0]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 45
	NX3_mem0 += MAS_MEM[0]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 45
	NX3_mem1 += MAIN_MEM_r

	NY3 = S.Task('NY3', length=7, delay_cost=1)
	S += NY3 >= 45
	NY3 += MM[0]

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	S += DX3__mem0 >= 46
	DX3__mem0 += MM_MEM[0]

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	S += DX3__mem1 >= 46
	DX3__mem1 += MM_MEM[0]

	DY3_ = S.Task('DY3_', length=1, delay_cost=1)
	S += DY3_ >= 46
	DY3_ += MAS[0]

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	S += DY3_in >= 46
	DY3_in += MM_in[0]

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	S += DY3_mem0 >= 46
	DY3_mem0 += MAS_MEM[0]

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	S += DY3_mem1 >= 46
	DY3_mem1 += MAIN_MEM_r

	NX3 = S.Task('NX3', length=7, delay_cost=1)
	S += NX3 >= 46
	NX3 += MM[0]

	DX3_ = S.Task('DX3_', length=1, delay_cost=1)
	S += DX3_ >= 47
	DX3_ += MAS[3]

	DY3 = S.Task('DY3', length=7, delay_cost=1)
	S += DY3 >= 47
	DY3 += MM[0]

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	S += Z_exp8_in >= 47
	Z_exp8_in += MM_in[0]

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	S += Z_exp8_mem0 >= 47
	Z_exp8_mem0 += MM_MEM[0]

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	S += Z_exp8_mem1 >= 47
	Z_exp8_mem1 += MAIN_MEM_r

	Z_exp8 = S.Task('Z_exp8', length=7, delay_cost=1)
	S += Z_exp8 >= 48
	Z_exp8 += MM[0]

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	S += k2_8_Z7_in >= 48
	k2_8_Z7_in += MM_in[0]

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	S += k2_8_Z7_mem0 >= 48
	k2_8_Z7_mem0 += MAIN_MEM_r

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	S += k2_8_Z7_mem1 >= 48
	k2_8_Z7_mem1 += MM_MEM[0]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 49
	k1_4_Z7_in += MM_in[0]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 49
	k1_4_Z7_mem0 += MAIN_MEM_r

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 49
	k1_4_Z7_mem1 += MM_MEM[0]

	k2_8_Z7 = S.Task('k2_8_Z7', length=7, delay_cost=1)
	S += k2_8_Z7 >= 49
	k2_8_Z7 += MM[0]

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	S += k0_4_Z7_in >= 50
	k0_4_Z7_in += MM_in[0]

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	S += k0_4_Z7_mem0 >= 50
	k0_4_Z7_mem0 += MAIN_MEM_r

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	S += k0_4_Z7_mem1 >= 50
	k0_4_Z7_mem1 += MM_MEM[0]

	k1_4_Z7 = S.Task('k1_4_Z7', length=7, delay_cost=1)
	S += k1_4_Z7 >= 50
	k1_4_Z7 += MM[0]

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	S += DX3_in >= 51
	DX3_in += MM_in[0]

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	S += DX3_mem0 >= 51
	DX3_mem0 += MAS_MEM[3]

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	S += DX3_mem1 >= 51
	DX3_mem1 += MAIN_MEM_r

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 51
	NY4__mem0 += MM_MEM[0]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 51
	NY4__mem1 += MM_MEM[0]

	k0_4_Z7 = S.Task('k0_4_Z7', length=7, delay_cost=1)
	S += k0_4_Z7 >= 51
	k0_4_Z7 += MM[0]

	DX3 = S.Task('DX3', length=7, delay_cost=1)
	S += DX3 >= 52
	DX3 += MM[0]

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 52
	NX4__mem0 += MM_MEM[0]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 52
	NX4__mem1 += MM_MEM[0]

	NY4_ = S.Task('NY4_', length=1, delay_cost=1)
	S += NY4_ >= 52
	NY4_ += MAS[0]

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	S += NY4_in >= 52
	NY4_in += MM_in[0]

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	S += NY4_mem0 >= 52
	NY4_mem0 += MAS_MEM[0]

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	S += NY4_mem1 >= 52
	NY4_mem1 += MAIN_MEM_r

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	S += DY4__mem0 >= 53
	DY4__mem0 += MM_MEM[0]

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	S += DY4__mem1 >= 53
	DY4__mem1 += MM_MEM[0]

	NX4_ = S.Task('NX4_', length=1, delay_cost=1)
	S += NX4_ >= 53
	NX4_ += MAS[3]

	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	S += NX4_in >= 53
	NX4_in += MM_in[0]

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	S += NX4_mem0 >= 53
	NX4_mem0 += MAS_MEM[3]

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	S += NX4_mem1 >= 53
	NX4_mem1 += MAIN_MEM_r

	NY4 = S.Task('NY4', length=7, delay_cost=1)
	S += NY4 >= 53
	NY4 += MM[0]

	DY4_ = S.Task('DY4_', length=1, delay_cost=1)
	S += DY4_ >= 54
	DY4_ += MAS[1]

	NX4 = S.Task('NX4', length=7, delay_cost=1)
	S += NX4 >= 54
	NX4 += MM[0]

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	S += Z_exp9_in >= 54
	Z_exp9_in += MM_in[0]

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	S += Z_exp9_mem0 >= 54
	Z_exp9_mem0 += MM_MEM[0]

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	S += Z_exp9_mem1 >= 54
	Z_exp9_mem1 += MAIN_MEM_r

	Z_exp9 = S.Task('Z_exp9', length=7, delay_cost=1)
	S += Z_exp9 >= 55
	Z_exp9 += MM[0]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 55
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 55
	k2_7_Z8_mem0 += MAIN_MEM_r

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 55
	k2_7_Z8_mem1 += MM_MEM[0]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 56
	k0_3_Z8_in += MM_in[0]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 56
	k0_3_Z8_mem0 += MAIN_MEM_r

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 56
	k0_3_Z8_mem1 += MM_MEM[0]

	k2_7_Z8 = S.Task('k2_7_Z8', length=7, delay_cost=1)
	S += k2_7_Z8 >= 56
	k2_7_Z8 += MM[0]

	k0_3_Z8 = S.Task('k0_3_Z8', length=7, delay_cost=1)
	S += k0_3_Z8 >= 57
	k0_3_Z8 += MM[0]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 57
	k3_8_Z8_in += MM_in[0]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 57
	k3_8_Z8_mem0 += MAIN_MEM_r

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 57
	k3_8_Z8_mem1 += MM_MEM[0]

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	S += DX4__mem0 >= 58
	DX4__mem0 += MM_MEM[0]

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	S += DX4__mem1 >= 58
	DX4__mem1 += MM_MEM[0]

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	S += DY4_in >= 58
	DY4_in += MM_in[0]

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	S += DY4_mem0 >= 58
	DY4_mem0 += MAS_MEM[1]

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	S += DY4_mem1 >= 58
	DY4_mem1 += MAIN_MEM_r

	k3_8_Z8 = S.Task('k3_8_Z8', length=7, delay_cost=1)
	S += k3_8_Z8 >= 58
	k3_8_Z8 += MM[0]

	DX4_ = S.Task('DX4_', length=1, delay_cost=1)
	S += DX4_ >= 59
	DX4_ += MAS[0]

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	S += DX4_in >= 59
	DX4_in += MM_in[0]

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	S += DX4_mem0 >= 59
	DX4_mem0 += MAS_MEM[0]

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	S += DX4_mem1 >= 59
	DX4_mem1 += MAIN_MEM_r

	DY4 = S.Task('DY4', length=7, delay_cost=1)
	S += DY4 >= 59
	DY4 += MM[0]

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	S += NY5__mem0 >= 59
	NY5__mem0 += MM_MEM[0]

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	S += NY5__mem1 >= 59
	NY5__mem1 += MM_MEM[0]

	DX4 = S.Task('DX4', length=7, delay_cost=1)
	S += DX4 >= 60
	DX4 += MM[0]

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	S += NX5__mem0 >= 60
	NX5__mem0 += MM_MEM[0]

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	S += NX5__mem1 >= 60
	NX5__mem1 += MM_MEM[0]

	NY5_ = S.Task('NY5_', length=1, delay_cost=1)
	S += NY5_ >= 60
	NY5_ += MAS[0]

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	S += NY5_in >= 60
	NY5_in += MM_in[0]

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	S += NY5_mem0 >= 60
	NY5_mem0 += MAS_MEM[0]

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	S += NY5_mem1 >= 60
	NY5_mem1 += MAIN_MEM_r

	NX5_ = S.Task('NX5_', length=1, delay_cost=1)
	S += NX5_ >= 61
	NX5_ += MAS[2]

	NY5 = S.Task('NY5', length=7, delay_cost=1)
	S += NY5 >= 61
	NY5 += MM[0]

	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	S += Z_exp10_in >= 61
	Z_exp10_in += MM_in[0]

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	S += Z_exp10_mem0 >= 61
	Z_exp10_mem0 += MM_MEM[0]

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	S += Z_exp10_mem1 >= 61
	Z_exp10_mem1 += MAIN_MEM_r

	Z_exp10 = S.Task('Z_exp10', length=7, delay_cost=1)
	S += Z_exp10 >= 62
	Z_exp10 += MM[0]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 62
	k3_9_Z7_in += MM_in[0]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 62
	k3_9_Z7_mem0 += MAIN_MEM_r

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 62
	k3_9_Z7_mem1 += MM_MEM[0]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 63
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 63
	k1_3_Z8_mem0 += MAIN_MEM_r

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 63
	k1_3_Z8_mem1 += MM_MEM[0]

	k3_9_Z7 = S.Task('k3_9_Z7', length=7, delay_cost=1)
	S += k3_9_Z7 >= 63
	k3_9_Z7 += MM[0]

	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	S += k0_2_Z9_in >= 64
	k0_2_Z9_in += MM_in[0]

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	S += k0_2_Z9_mem0 >= 64
	k0_2_Z9_mem0 += MAIN_MEM_r

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	S += k0_2_Z9_mem1 >= 64
	k0_2_Z9_mem1 += MM_MEM[0]

	k1_3_Z8 = S.Task('k1_3_Z8', length=7, delay_cost=1)
	S += k1_3_Z8 >= 64
	k1_3_Z8 += MM[0]

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	S += DY5__mem0 >= 65
	DY5__mem0 += MM_MEM[0]

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	S += DY5__mem1 >= 65
	DY5__mem1 += MM_MEM[0]

	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	S += NX5_in >= 65
	NX5_in += MM_in[0]

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	S += NX5_mem0 >= 65
	NX5_mem0 += MAS_MEM[2]

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	S += NX5_mem1 >= 65
	NX5_mem1 += MAIN_MEM_r

	k0_2_Z9 = S.Task('k0_2_Z9', length=7, delay_cost=1)
	S += k0_2_Z9 >= 65
	k0_2_Z9 += MM[0]

	DY5_ = S.Task('DY5_', length=1, delay_cost=1)
	S += DY5_ >= 66
	DY5_ += MAS[2]

	NX5 = S.Task('NX5', length=7, delay_cost=1)
	S += NX5 >= 66
	NX5 += MM[0]

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	S += k1_2_Z9_in >= 66
	k1_2_Z9_in += MM_in[0]

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	S += k1_2_Z9_mem0 >= 66
	k1_2_Z9_mem0 += MAIN_MEM_r

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	S += k1_2_Z9_mem1 >= 66
	k1_2_Z9_mem1 += MM_MEM[0]

	k1_2_Z9 = S.Task('k1_2_Z9', length=7, delay_cost=1)
	S += k1_2_Z9 >= 67
	k1_2_Z9 += MM[0]

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	S += k3_7_Z9_in >= 67
	k3_7_Z9_in += MM_in[0]

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	S += k3_7_Z9_mem0 >= 67
	k3_7_Z9_mem0 += MAIN_MEM_r

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	S += k3_7_Z9_mem1 >= 67
	k3_7_Z9_mem1 += MM_MEM[0]

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	S += Z_exp11_in >= 68
	Z_exp11_in += MM_in[0]

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	S += Z_exp11_mem0 >= 68
	Z_exp11_mem0 += MM_MEM[0]

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	S += Z_exp11_mem1 >= 68
	Z_exp11_mem1 += MAIN_MEM_r

	k3_7_Z9 = S.Task('k3_7_Z9', length=7, delay_cost=1)
	S += k3_7_Z9 >= 68
	k3_7_Z9 += MM[0]

	Z_exp11 = S.Task('Z_exp11', length=7, delay_cost=1)
	S += Z_exp11 >= 69
	Z_exp11 += MM[0]

	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	S += k3_6_Z10_in >= 69
	k3_6_Z10_in += MM_in[0]

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	S += k3_6_Z10_mem0 >= 69
	k3_6_Z10_mem0 += MAIN_MEM_r

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	S += k3_6_Z10_mem1 >= 69
	k3_6_Z10_mem1 += MM_MEM[0]

	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	S += k1_1_Z10_in >= 70
	k1_1_Z10_in += MM_in[0]

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	S += k1_1_Z10_mem0 >= 70
	k1_1_Z10_mem0 += MAIN_MEM_r

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	S += k1_1_Z10_mem1 >= 70
	k1_1_Z10_mem1 += MM_MEM[0]

	k3_6_Z10 = S.Task('k3_6_Z10', length=7, delay_cost=1)
	S += k3_6_Z10 >= 70
	k3_6_Z10 += MM[0]

	k1_1_Z10 = S.Task('k1_1_Z10', length=7, delay_cost=1)
	S += k1_1_Z10 >= 71
	k1_1_Z10 += MM[0]

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	S += k2_5_Z10_in >= 71
	k2_5_Z10_in += MM_in[0]

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	S += k2_5_Z10_mem0 >= 71
	k2_5_Z10_mem0 += MAIN_MEM_r

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	S += k2_5_Z10_mem1 >= 71
	k2_5_Z10_mem1 += MM_MEM[0]

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	S += k0_1_Z10_in >= 72
	k0_1_Z10_in += MM_in[0]

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	S += k0_1_Z10_mem0 >= 72
	k0_1_Z10_mem0 += MAIN_MEM_r

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	S += k0_1_Z10_mem1 >= 72
	k0_1_Z10_mem1 += MM_MEM[0]

	k2_5_Z10 = S.Task('k2_5_Z10', length=7, delay_cost=1)
	S += k2_5_Z10 >= 72
	k2_5_Z10 += MM[0]

	k0_1_Z10 = S.Task('k0_1_Z10', length=7, delay_cost=1)
	S += k0_1_Z10 >= 73
	k0_1_Z10 += MM[0]

	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	S += k2_6_Z9_in >= 73
	k2_6_Z9_in += MM_in[0]

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	S += k2_6_Z9_mem0 >= 73
	k2_6_Z9_mem0 += MAIN_MEM_r

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	S += k2_6_Z9_mem1 >= 73
	k2_6_Z9_mem1 += MM_MEM[0]

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	S += DX5__mem0 >= 74
	DX5__mem0 += MM_MEM[0]

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	S += DX5__mem1 >= 74
	DX5__mem1 += MM_MEM[0]

	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	S += DY5_in >= 74
	DY5_in += MM_in[0]

	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	S += DY5_mem0 >= 74
	DY5_mem0 += MAS_MEM[2]

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	S += DY5_mem1 >= 74
	DY5_mem1 += MAIN_MEM_r

	k2_6_Z9 = S.Task('k2_6_Z9', length=7, delay_cost=1)
	S += k2_6_Z9 >= 74
	k2_6_Z9 += MM[0]

	DX5_ = S.Task('DX5_', length=1, delay_cost=1)
	S += DX5_ >= 75
	DX5_ += MAS[0]

	DY5 = S.Task('DY5', length=7, delay_cost=1)
	S += DY5 >= 75
	DY5 += MM[0]

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	S += Z_exp12_in >= 75
	Z_exp12_in += MM_in[0]

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	S += Z_exp12_mem0 >= 75
	Z_exp12_mem0 += MM_MEM[0]

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	S += Z_exp12_mem1 >= 75
	Z_exp12_mem1 += MAIN_MEM_r

	Z_exp12 = S.Task('Z_exp12', length=7, delay_cost=1)
	S += Z_exp12 >= 76
	Z_exp12 += MM[0]

	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	S += k0_0_Z11_in >= 76
	k0_0_Z11_in += MM_in[0]

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	S += k0_0_Z11_mem0 >= 76
	k0_0_Z11_mem0 += MAIN_MEM_r

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	S += k0_0_Z11_mem1 >= 76
	k0_0_Z11_mem1 += MM_MEM[0]

	k0_0_Z11 = S.Task('k0_0_Z11', length=7, delay_cost=1)
	S += k0_0_Z11 >= 77
	k0_0_Z11 += MM[0]

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	S += k1_0_Z11_in >= 77
	k1_0_Z11_in += MM_in[0]

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	S += k1_0_Z11_mem0 >= 77
	k1_0_Z11_mem0 += MAIN_MEM_r

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	S += k1_0_Z11_mem1 >= 77
	k1_0_Z11_mem1 += MM_MEM[0]

	k1_0_Z11 = S.Task('k1_0_Z11', length=7, delay_cost=1)
	S += k1_0_Z11 >= 78
	k1_0_Z11 += MM[0]

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	S += k3_5_Z11_in >= 78
	k3_5_Z11_in += MM_in[0]

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	S += k3_5_Z11_mem0 >= 78
	k3_5_Z11_mem0 += MAIN_MEM_r

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	S += k3_5_Z11_mem1 >= 78
	k3_5_Z11_mem1 += MM_MEM[0]

	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	S += k2_4_Z11_in >= 79
	k2_4_Z11_in += MM_in[0]

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	S += k2_4_Z11_mem0 >= 79
	k2_4_Z11_mem0 += MAIN_MEM_r

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	S += k2_4_Z11_mem1 >= 79
	k2_4_Z11_mem1 += MM_MEM[0]

	k3_5_Z11 = S.Task('k3_5_Z11', length=7, delay_cost=1)
	S += k3_5_Z11 >= 79
	k3_5_Z11 += MM[0]

	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	S += DX5_in >= 80
	DX5_in += MM_in[0]

	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	S += DX5_mem0 >= 80
	DX5_mem0 += MAS_MEM[0]

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	S += DX5_mem1 >= 80
	DX5_mem1 += MAIN_MEM_r

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	S += NY6__mem0 >= 80
	NY6__mem0 += MM_MEM[0]

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	S += NY6__mem1 >= 80
	NY6__mem1 += MM_MEM[0]

	k2_4_Z11 = S.Task('k2_4_Z11', length=7, delay_cost=1)
	S += k2_4_Z11 >= 80
	k2_4_Z11 += MM[0]

	DX5 = S.Task('DX5', length=7, delay_cost=1)
	S += DX5 >= 81
	DX5 += MM[0]

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	S += NX6__mem0 >= 81
	NX6__mem0 += MM_MEM[0]

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	S += NX6__mem1 >= 81
	NX6__mem1 += MM_MEM[0]

	NY6_ = S.Task('NY6_', length=1, delay_cost=1)
	S += NY6_ >= 81
	NY6_ += MAS[0]

	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	S += NY6_in >= 81
	NY6_in += MM_in[0]

	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	S += NY6_mem0 >= 81
	NY6_mem0 += MAS_MEM[0]

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	S += NY6_mem1 >= 81
	NY6_mem1 += MAIN_MEM_r

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	S += DY6__mem0 >= 82
	DY6__mem0 += MM_MEM[0]

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	S += DY6__mem1 >= 82
	DY6__mem1 += MM_MEM[0]

	NX6_ = S.Task('NX6_', length=1, delay_cost=1)
	S += NX6_ >= 82
	NX6_ += MAS[1]

	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	S += NX6_in >= 82
	NX6_in += MM_in[0]

	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	S += NX6_mem0 >= 82
	NX6_mem0 += MAS_MEM[1]

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	S += NX6_mem1 >= 82
	NX6_mem1 += MAIN_MEM_r

	NY6 = S.Task('NY6', length=7, delay_cost=1)
	S += NY6 >= 82
	NY6 += MM[0]

	DY6_ = S.Task('DY6_', length=1, delay_cost=1)
	S += DY6_ >= 83
	DY6_ += MAS[3]

	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	S += DY6_in >= 83
	DY6_in += MM_in[0]

	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	S += DY6_mem0 >= 83
	DY6_mem0 += MAS_MEM[3]

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	S += DY6_mem1 >= 83
	DY6_mem1 += MAIN_MEM_r

	NX6 = S.Task('NX6', length=7, delay_cost=1)
	S += NX6 >= 83
	NX6 += MM[0]

	DY6 = S.Task('DY6', length=7, delay_cost=1)
	S += DY6 >= 84
	DY6 += MM[0]

	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	S += Z_exp13_in >= 84
	Z_exp13_in += MM_in[0]

	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	S += Z_exp13_mem0 >= 84
	Z_exp13_mem0 += MM_MEM[0]

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	S += Z_exp13_mem1 >= 84
	Z_exp13_mem1 += MAIN_MEM_r

	Z_exp13 = S.Task('Z_exp13', length=7, delay_cost=1)
	S += Z_exp13 >= 85
	Z_exp13 += MM[0]

	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	S += k2_3_Z12_in >= 85
	k2_3_Z12_in += MM_in[0]

	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	S += k2_3_Z12_mem0 >= 85
	k2_3_Z12_mem0 += MAIN_MEM_r

	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	S += k2_3_Z12_mem1 >= 85
	k2_3_Z12_mem1 += MM_MEM[0]

	k2_3_Z12 = S.Task('k2_3_Z12', length=7, delay_cost=1)
	S += k2_3_Z12 >= 86
	k2_3_Z12 += MM[0]

	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	S += k3_4_Z12_in >= 86
	k3_4_Z12_in += MM_in[0]

	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	S += k3_4_Z12_mem0 >= 86
	k3_4_Z12_mem0 += MAIN_MEM_r

	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	S += k3_4_Z12_mem1 >= 86
	k3_4_Z12_mem1 += MM_MEM[0]

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	S += DX6__mem0 >= 87
	DX6__mem0 += MM_MEM[0]

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	S += DX6__mem1 >= 87
	DX6__mem1 += MM_MEM[0]

	k3_4_Z12 = S.Task('k3_4_Z12', length=7, delay_cost=1)
	S += k3_4_Z12 >= 87
	k3_4_Z12 += MM[0]

	DX6_ = S.Task('DX6_', length=1, delay_cost=1)
	S += DX6_ >= 88
	DX6_ += MAS[0]

	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	S += DX6_in >= 88
	DX6_in += MM_in[0]

	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	S += DX6_mem0 >= 88
	DX6_mem0 += MAS_MEM[0]

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	S += DX6_mem1 >= 88
	DX6_mem1 += MAIN_MEM_r

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	S += NY7__mem0 >= 88
	NY7__mem0 += MM_MEM[0]

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	S += NY7__mem1 >= 88
	NY7__mem1 += MM_MEM[0]

	DX6 = S.Task('DX6', length=7, delay_cost=1)
	S += DX6 >= 89
	DX6 += MM[0]

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	S += NX7__mem0 >= 89
	NX7__mem0 += MM_MEM[0]

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	S += NX7__mem1 >= 89
	NX7__mem1 += MM_MEM[0]

	NY7_ = S.Task('NY7_', length=1, delay_cost=1)
	S += NY7_ >= 89
	NY7_ += MAS[0]

	NY7_in = S.Task('NY7_in', length=1, delay_cost=1)
	S += NY7_in >= 89
	NY7_in += MM_in[0]

	NY7_mem0 = S.Task('NY7_mem0', length=1, delay_cost=1)
	S += NY7_mem0 >= 89
	NY7_mem0 += MAS_MEM[0]

	NY7_mem1 = S.Task('NY7_mem1', length=1, delay_cost=1)
	S += NY7_mem1 >= 89
	NY7_mem1 += MAIN_MEM_r

	DY7__mem0 = S.Task('DY7__mem0', length=1, delay_cost=1)
	S += DY7__mem0 >= 90
	DY7__mem0 += MM_MEM[0]

	DY7__mem1 = S.Task('DY7__mem1', length=1, delay_cost=1)
	S += DY7__mem1 >= 90
	DY7__mem1 += MM_MEM[0]

	NX7_ = S.Task('NX7_', length=1, delay_cost=1)
	S += NX7_ >= 90
	NX7_ += MAS[3]

	NX7_in = S.Task('NX7_in', length=1, delay_cost=1)
	S += NX7_in >= 90
	NX7_in += MM_in[0]

	NX7_mem0 = S.Task('NX7_mem0', length=1, delay_cost=1)
	S += NX7_mem0 >= 90
	NX7_mem0 += MAS_MEM[3]

	NX7_mem1 = S.Task('NX7_mem1', length=1, delay_cost=1)
	S += NX7_mem1 >= 90
	NX7_mem1 += MAIN_MEM_r

	NY7 = S.Task('NY7', length=7, delay_cost=1)
	S += NY7 >= 90
	NY7 += MM[0]

	DY7_ = S.Task('DY7_', length=1, delay_cost=1)
	S += DY7_ >= 91
	DY7_ += MAS[3]

	DY7_in = S.Task('DY7_in', length=1, delay_cost=1)
	S += DY7_in >= 91
	DY7_in += MM_in[0]

	DY7_mem0 = S.Task('DY7_mem0', length=1, delay_cost=1)
	S += DY7_mem0 >= 91
	DY7_mem0 += MAS_MEM[3]

	DY7_mem1 = S.Task('DY7_mem1', length=1, delay_cost=1)
	S += DY7_mem1 >= 91
	DY7_mem1 += MAIN_MEM_r

	NX7 = S.Task('NX7', length=7, delay_cost=1)
	S += NX7 >= 91
	NX7 += MM[0]

	DY7 = S.Task('DY7', length=7, delay_cost=1)
	S += DY7 >= 92
	DY7 += MM[0]

	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	S += Z_exp14_in >= 92
	Z_exp14_in += MM_in[0]

	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	S += Z_exp14_mem0 >= 92
	Z_exp14_mem0 += MM_MEM[0]

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	S += Z_exp14_mem1 >= 92
	Z_exp14_mem1 += MAIN_MEM_r

	Z_exp14 = S.Task('Z_exp14', length=7, delay_cost=1)
	S += Z_exp14 >= 93
	Z_exp14 += MM[0]

	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	S += k2_2_Z13_in >= 93
	k2_2_Z13_in += MM_in[0]

	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	S += k2_2_Z13_mem0 >= 93
	k2_2_Z13_mem0 += MAIN_MEM_r

	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	S += k2_2_Z13_mem1 >= 93
	k2_2_Z13_mem1 += MM_MEM[0]

	k2_2_Z13 = S.Task('k2_2_Z13', length=7, delay_cost=1)
	S += k2_2_Z13 >= 94
	k2_2_Z13 += MM[0]

	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	S += k3_3_Z13_in >= 94
	k3_3_Z13_in += MM_in[0]

	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	S += k3_3_Z13_mem0 >= 94
	k3_3_Z13_mem0 += MAIN_MEM_r

	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	S += k3_3_Z13_mem1 >= 94
	k3_3_Z13_mem1 += MM_MEM[0]

	DX7__mem0 = S.Task('DX7__mem0', length=1, delay_cost=1)
	S += DX7__mem0 >= 95
	DX7__mem0 += MM_MEM[0]

	DX7__mem1 = S.Task('DX7__mem1', length=1, delay_cost=1)
	S += DX7__mem1 >= 95
	DX7__mem1 += MM_MEM[0]

	k3_3_Z13 = S.Task('k3_3_Z13', length=7, delay_cost=1)
	S += k3_3_Z13 >= 95
	k3_3_Z13 += MM[0]

	DX7_ = S.Task('DX7_', length=1, delay_cost=1)
	S += DX7_ >= 96
	DX7_ += MAS[0]

	DX7_in = S.Task('DX7_in', length=1, delay_cost=1)
	S += DX7_in >= 96
	DX7_in += MM_in[0]

	DX7_mem0 = S.Task('DX7_mem0', length=1, delay_cost=1)
	S += DX7_mem0 >= 96
	DX7_mem0 += MAS_MEM[0]

	DX7_mem1 = S.Task('DX7_mem1', length=1, delay_cost=1)
	S += DX7_mem1 >= 96
	DX7_mem1 += MAIN_MEM_r

	NY8__mem0 = S.Task('NY8__mem0', length=1, delay_cost=1)
	S += NY8__mem0 >= 96
	NY8__mem0 += MM_MEM[0]

	NY8__mem1 = S.Task('NY8__mem1', length=1, delay_cost=1)
	S += NY8__mem1 >= 96
	NY8__mem1 += MM_MEM[0]

	DX7 = S.Task('DX7', length=7, delay_cost=1)
	S += DX7 >= 97
	DX7 += MM[0]

	NX8__mem0 = S.Task('NX8__mem0', length=1, delay_cost=1)
	S += NX8__mem0 >= 97
	NX8__mem0 += MM_MEM[0]

	NX8__mem1 = S.Task('NX8__mem1', length=1, delay_cost=1)
	S += NX8__mem1 >= 97
	NX8__mem1 += MM_MEM[0]

	NY8_ = S.Task('NY8_', length=1, delay_cost=1)
	S += NY8_ >= 97
	NY8_ += MAS[0]

	NY8_in = S.Task('NY8_in', length=1, delay_cost=1)
	S += NY8_in >= 97
	NY8_in += MM_in[0]

	NY8_mem0 = S.Task('NY8_mem0', length=1, delay_cost=1)
	S += NY8_mem0 >= 97
	NY8_mem0 += MAS_MEM[0]

	NY8_mem1 = S.Task('NY8_mem1', length=1, delay_cost=1)
	S += NY8_mem1 >= 97
	NY8_mem1 += MAIN_MEM_r

	DY8__mem0 = S.Task('DY8__mem0', length=1, delay_cost=1)
	S += DY8__mem0 >= 98
	DY8__mem0 += MM_MEM[0]

	DY8__mem1 = S.Task('DY8__mem1', length=1, delay_cost=1)
	S += DY8__mem1 >= 98
	DY8__mem1 += MM_MEM[0]

	NX8_ = S.Task('NX8_', length=1, delay_cost=1)
	S += NX8_ >= 98
	NX8_ += MAS[0]

	NX8_in = S.Task('NX8_in', length=1, delay_cost=1)
	S += NX8_in >= 98
	NX8_in += MM_in[0]

	NX8_mem0 = S.Task('NX8_mem0', length=1, delay_cost=1)
	S += NX8_mem0 >= 98
	NX8_mem0 += MAS_MEM[0]

	NX8_mem1 = S.Task('NX8_mem1', length=1, delay_cost=1)
	S += NX8_mem1 >= 98
	NX8_mem1 += MAIN_MEM_r

	NY8 = S.Task('NY8', length=7, delay_cost=1)
	S += NY8 >= 98
	NY8 += MM[0]

	DY8_ = S.Task('DY8_', length=1, delay_cost=1)
	S += DY8_ >= 99
	DY8_ += MAS[3]

	DY8_in = S.Task('DY8_in', length=1, delay_cost=1)
	S += DY8_in >= 99
	DY8_in += MM_in[0]

	DY8_mem0 = S.Task('DY8_mem0', length=1, delay_cost=1)
	S += DY8_mem0 >= 99
	DY8_mem0 += MAS_MEM[3]

	DY8_mem1 = S.Task('DY8_mem1', length=1, delay_cost=1)
	S += DY8_mem1 >= 99
	DY8_mem1 += MAIN_MEM_r

	NX8 = S.Task('NX8', length=7, delay_cost=1)
	S += NX8 >= 99
	NX8 += MM[0]

	DY8 = S.Task('DY8', length=7, delay_cost=1)
	S += DY8 >= 100
	DY8 += MM[0]

	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	S += Z_exp15_in >= 100
	Z_exp15_in += MM_in[0]

	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	S += Z_exp15_mem0 >= 100
	Z_exp15_mem0 += MM_MEM[0]

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	S += Z_exp15_mem1 >= 100
	Z_exp15_mem1 += MAIN_MEM_r

	Z_exp15 = S.Task('Z_exp15', length=7, delay_cost=1)
	S += Z_exp15 >= 101
	Z_exp15 += MM[0]

	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	S += k2_1_Z14_in >= 101
	k2_1_Z14_in += MM_in[0]

	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	S += k2_1_Z14_mem0 >= 101
	k2_1_Z14_mem0 += MAIN_MEM_r

	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	S += k2_1_Z14_mem1 >= 101
	k2_1_Z14_mem1 += MM_MEM[0]

	k2_1_Z14 = S.Task('k2_1_Z14', length=7, delay_cost=1)
	S += k2_1_Z14 >= 102
	k2_1_Z14 += MM[0]

	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	S += k3_2_Z14_in >= 102
	k3_2_Z14_in += MM_in[0]

	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	S += k3_2_Z14_mem0 >= 102
	k3_2_Z14_mem0 += MAIN_MEM_r

	k3_2_Z14_mem1 = S.Task('k3_2_Z14_mem1', length=1, delay_cost=1)
	S += k3_2_Z14_mem1 >= 102
	k3_2_Z14_mem1 += MM_MEM[0]

	DX8__mem0 = S.Task('DX8__mem0', length=1, delay_cost=1)
	S += DX8__mem0 >= 103
	DX8__mem0 += MM_MEM[0]

	DX8__mem1 = S.Task('DX8__mem1', length=1, delay_cost=1)
	S += DX8__mem1 >= 103
	DX8__mem1 += MM_MEM[0]

	k3_2_Z14 = S.Task('k3_2_Z14', length=7, delay_cost=1)
	S += k3_2_Z14 >= 103
	k3_2_Z14 += MM[0]

	DX8_ = S.Task('DX8_', length=1, delay_cost=1)
	S += DX8_ >= 104
	DX8_ += MAS[2]

	DX8_in = S.Task('DX8_in', length=1, delay_cost=1)
	S += DX8_in >= 104
	DX8_in += MM_in[0]

	DX8_mem0 = S.Task('DX8_mem0', length=1, delay_cost=1)
	S += DX8_mem0 >= 104
	DX8_mem0 += MAS_MEM[2]

	DX8_mem1 = S.Task('DX8_mem1', length=1, delay_cost=1)
	S += DX8_mem1 >= 104
	DX8_mem1 += MAIN_MEM_r

	NY9__mem0 = S.Task('NY9__mem0', length=1, delay_cost=1)
	S += NY9__mem0 >= 104
	NY9__mem0 += MM_MEM[0]

	NY9__mem1 = S.Task('NY9__mem1', length=1, delay_cost=1)
	S += NY9__mem1 >= 104
	NY9__mem1 += MM_MEM[0]

	DX8 = S.Task('DX8', length=7, delay_cost=1)
	S += DX8 >= 105
	DX8 += MM[0]

	NX9__mem0 = S.Task('NX9__mem0', length=1, delay_cost=1)
	S += NX9__mem0 >= 105
	NX9__mem0 += MM_MEM[0]

	NX9__mem1 = S.Task('NX9__mem1', length=1, delay_cost=1)
	S += NX9__mem1 >= 105
	NX9__mem1 += MM_MEM[0]

	NY9_ = S.Task('NY9_', length=1, delay_cost=1)
	S += NY9_ >= 105
	NY9_ += MAS[0]

	NY9_in = S.Task('NY9_in', length=1, delay_cost=1)
	S += NY9_in >= 105
	NY9_in += MM_in[0]

	NY9_mem0 = S.Task('NY9_mem0', length=1, delay_cost=1)
	S += NY9_mem0 >= 105
	NY9_mem0 += MAS_MEM[0]

	NY9_mem1 = S.Task('NY9_mem1', length=1, delay_cost=1)
	S += NY9_mem1 >= 105
	NY9_mem1 += MAIN_MEM_r

	DY9__mem0 = S.Task('DY9__mem0', length=1, delay_cost=1)
	S += DY9__mem0 >= 106
	DY9__mem0 += MM_MEM[0]

	DY9__mem1 = S.Task('DY9__mem1', length=1, delay_cost=1)
	S += DY9__mem1 >= 106
	DY9__mem1 += MM_MEM[0]

	NX9_ = S.Task('NX9_', length=1, delay_cost=1)
	S += NX9_ >= 106
	NX9_ += MAS[0]

	NX9_in = S.Task('NX9_in', length=1, delay_cost=1)
	S += NX9_in >= 106
	NX9_in += MM_in[0]

	NX9_mem0 = S.Task('NX9_mem0', length=1, delay_cost=1)
	S += NX9_mem0 >= 106
	NX9_mem0 += MAS_MEM[0]

	NX9_mem1 = S.Task('NX9_mem1', length=1, delay_cost=1)
	S += NX9_mem1 >= 106
	NX9_mem1 += MAIN_MEM_r

	NY9 = S.Task('NY9', length=7, delay_cost=1)
	S += NY9 >= 106
	NY9 += MM[0]

	DY9_ = S.Task('DY9_', length=1, delay_cost=1)
	S += DY9_ >= 107
	DY9_ += MAS[0]

	NX9 = S.Task('NX9', length=7, delay_cost=1)
	S += NX9 >= 107
	NX9 += MM[0]

	Z_exp16_in = S.Task('Z_exp16_in', length=1, delay_cost=1)
	S += Z_exp16_in >= 107
	Z_exp16_in += MM_in[0]

	Z_exp16_mem0 = S.Task('Z_exp16_mem0', length=1, delay_cost=1)
	S += Z_exp16_mem0 >= 107
	Z_exp16_mem0 += MM_MEM[0]

	Z_exp16_mem1 = S.Task('Z_exp16_mem1', length=1, delay_cost=1)
	S += Z_exp16_mem1 >= 107
	Z_exp16_mem1 += MAIN_MEM_r

	DY9_in = S.Task('DY9_in', length=1, delay_cost=1)
	S += DY9_in >= 108
	DY9_in += MM_in[0]

	DY9_mem0 = S.Task('DY9_mem0', length=1, delay_cost=1)
	S += DY9_mem0 >= 108
	DY9_mem0 += MAS_MEM[0]

	DY9_mem1 = S.Task('DY9_mem1', length=1, delay_cost=1)
	S += DY9_mem1 >= 108
	DY9_mem1 += MAIN_MEM_r

	Z_exp16 = S.Task('Z_exp16', length=7, delay_cost=1)
	S += Z_exp16 >= 108
	Z_exp16 += MM[0]

	DY9 = S.Task('DY9', length=7, delay_cost=1)
	S += DY9 >= 109
	DY9 += MM[0]

	k2_0_Z15_in = S.Task('k2_0_Z15_in', length=1, delay_cost=1)
	S += k2_0_Z15_in >= 109
	k2_0_Z15_in += MM_in[0]

	k2_0_Z15_mem0 = S.Task('k2_0_Z15_mem0', length=1, delay_cost=1)
	S += k2_0_Z15_mem0 >= 109
	k2_0_Z15_mem0 += MAIN_MEM_r

	k2_0_Z15_mem1 = S.Task('k2_0_Z15_mem1', length=1, delay_cost=1)
	S += k2_0_Z15_mem1 >= 109
	k2_0_Z15_mem1 += MM_MEM[0]

	k2_0_Z15 = S.Task('k2_0_Z15', length=7, delay_cost=1)
	S += k2_0_Z15 >= 110
	k2_0_Z15 += MM[0]

	k3_1_Z15_in = S.Task('k3_1_Z15_in', length=1, delay_cost=1)
	S += k3_1_Z15_in >= 110
	k3_1_Z15_in += MM_in[0]

	k3_1_Z15_mem0 = S.Task('k3_1_Z15_mem0', length=1, delay_cost=1)
	S += k3_1_Z15_mem0 >= 110
	k3_1_Z15_mem0 += MAIN_MEM_r

	k3_1_Z15_mem1 = S.Task('k3_1_Z15_mem1', length=1, delay_cost=1)
	S += k3_1_Z15_mem1 >= 110
	k3_1_Z15_mem1 += MM_MEM[0]

	DX9__mem0 = S.Task('DX9__mem0', length=1, delay_cost=1)
	S += DX9__mem0 >= 111
	DX9__mem0 += MM_MEM[0]

	DX9__mem1 = S.Task('DX9__mem1', length=1, delay_cost=1)
	S += DX9__mem1 >= 111
	DX9__mem1 += MM_MEM[0]

	k3_1_Z15 = S.Task('k3_1_Z15', length=7, delay_cost=1)
	S += k3_1_Z15 >= 111
	k3_1_Z15 += MM[0]

	DX9_ = S.Task('DX9_', length=1, delay_cost=1)
	S += DX9_ >= 112
	DX9_ += MAS[0]

	DX9_in = S.Task('DX9_in', length=1, delay_cost=1)
	S += DX9_in >= 112
	DX9_in += MM_in[0]

	DX9_mem0 = S.Task('DX9_mem0', length=1, delay_cost=1)
	S += DX9_mem0 >= 112
	DX9_mem0 += MAS_MEM[0]

	DX9_mem1 = S.Task('DX9_mem1', length=1, delay_cost=1)
	S += DX9_mem1 >= 112
	DX9_mem1 += MAIN_MEM_r

	NY10__mem0 = S.Task('NY10__mem0', length=1, delay_cost=1)
	S += NY10__mem0 >= 112
	NY10__mem0 += MM_MEM[0]

	NY10__mem1 = S.Task('NY10__mem1', length=1, delay_cost=1)
	S += NY10__mem1 >= 112
	NY10__mem1 += MM_MEM[0]

	DX9 = S.Task('DX9', length=7, delay_cost=1)
	S += DX9 >= 113
	DX9 += MM[0]

	NX10__mem0 = S.Task('NX10__mem0', length=1, delay_cost=1)
	S += NX10__mem0 >= 113
	NX10__mem0 += MM_MEM[0]

	NX10__mem1 = S.Task('NX10__mem1', length=1, delay_cost=1)
	S += NX10__mem1 >= 113
	NX10__mem1 += MM_MEM[0]

	NY10_ = S.Task('NY10_', length=1, delay_cost=1)
	S += NY10_ >= 113
	NY10_ += MAS[0]

	NX10_ = S.Task('NX10_', length=1, delay_cost=1)
	S += NX10_ >= 114
	NX10_ += MAS[0]

	k3_0_Z16_in = S.Task('k3_0_Z16_in', length=1, delay_cost=1)
	S += k3_0_Z16_in >= 114
	k3_0_Z16_in += MM_in[0]

	k3_0_Z16_mem0 = S.Task('k3_0_Z16_mem0', length=1, delay_cost=1)
	S += k3_0_Z16_mem0 >= 114
	k3_0_Z16_mem0 += MAIN_MEM_r

	k3_0_Z16_mem1 = S.Task('k3_0_Z16_mem1', length=1, delay_cost=1)
	S += k3_0_Z16_mem1 >= 114
	k3_0_Z16_mem1 += MM_MEM[0]

	k3_0_Z16 = S.Task('k3_0_Z16', length=7, delay_cost=1)
	S += k3_0_Z16 >= 115
	k3_0_Z16 += MM[0]


	# new tasks
	NX10_in = S.Task('NX10_in', length=1, delay_cost=1)
	NX10_in += alt(MM_in)
	NX10 = S.Task('NX10', length=7, delay_cost=1)
	NX10 += alt(MM)
	S += NX10>=NX10_in

	NX10_mem0 = S.Task('NX10_mem0', length=1, delay_cost=1)
	NX10_mem0 += MAS_MEM[0]
	S += 114 < NX10_mem0
	S += NX10_mem0 <= NX10

	NX10_mem1 = S.Task('NX10_mem1', length=1, delay_cost=1)
	NX10_mem1 += MAIN_MEM_r
	S += NX10_mem1 <= NX10

	DX = S.Task('DX', length=1, delay_cost=1)
	DX += alt(MAS)

	DX_mem0 = S.Task('DX_mem0', length=1, delay_cost=1)
	DX_mem0 += MM_MEM[0]
	S += 119 < DX_mem0
	S += DX_mem0 <= DX

	DX_mem1 = S.Task('DX_mem1', length=1, delay_cost=1)
	DX_mem1 += MM_MEM[0]
	S += 84 < DX_mem1
	S += DX_mem1 <= DX

	NY10_in = S.Task('NY10_in', length=1, delay_cost=1)
	NY10_in += alt(MM_in)
	NY10 = S.Task('NY10', length=7, delay_cost=1)
	NY10 += alt(MM)
	S += NY10>=NY10_in

	NY10_mem0 = S.Task('NY10_mem0', length=1, delay_cost=1)
	NY10_mem0 += MAS_MEM[0]
	S += 113 < NY10_mem0
	S += NY10_mem0 <= NY10

	NY10_mem1 = S.Task('NY10_mem1', length=1, delay_cost=1)
	NY10_mem1 += MAIN_MEM_r
	S += NY10_mem1 <= NY10

	DY10_ = S.Task('DY10_', length=1, delay_cost=1)
	DY10_ += alt(MAS)

	DY10__mem0 = S.Task('DY10__mem0', length=1, delay_cost=1)
	DY10__mem0 += MM_MEM[0]
	S += 115 < DY10__mem0
	S += DY10__mem0 <= DY10_

	DY10__mem1 = S.Task('DY10__mem1', length=1, delay_cost=1)
	DY10__mem1 += MM_MEM[0]
	S += 85 < DY10__mem1
	S += DY10__mem1 <= DY10_

	NX = S.Task('NX', length=1, delay_cost=1)
	NX += alt(MAS)

	NX_mem0 = S.Task('NX_mem0', length=1, delay_cost=1)
	NX_mem0 += alt(MM_MEM)
	S += (NX10*MM[0])-1 < NX_mem0*MM_MEM[0]
	S += NX_mem0 <= NX

	NX_mem1 = S.Task('NX_mem1', length=1, delay_cost=1)
	NX_mem1 += MM_MEM[0]
	S += 83 < NX_mem1
	S += NX_mem1 <= NX

	NY11_ = S.Task('NY11_', length=1, delay_cost=1)
	NY11_ += alt(MAS)

	NY11__mem0 = S.Task('NY11__mem0', length=1, delay_cost=1)
	NY11__mem0 += alt(MM_MEM)
	S += (NY10*MM[0])-1 < NY11__mem0*MM_MEM[0]
	S += NY11__mem0 <= NY11_

	NY11__mem1 = S.Task('NY11__mem1', length=1, delay_cost=1)
	NY11__mem1 += MM_MEM[0]
	S += 86 < NY11__mem1
	S += NY11__mem1 <= NY11_

	DY10_in = S.Task('DY10_in', length=1, delay_cost=1)
	DY10_in += alt(MM_in)
	DY10 = S.Task('DY10', length=7, delay_cost=1)
	DY10 += alt(MM)
	S += DY10>=DY10_in

	DY10_mem0 = S.Task('DY10_mem0', length=1, delay_cost=1)
	DY10_mem0 += alt(MAS_MEM)
	S += (DY10_*MAS[0])-1 < DY10_mem0*MAS_MEM[0]
	S += (DY10_*MAS[1])-1 < DY10_mem0*MAS_MEM[1]
	S += (DY10_*MAS[2])-1 < DY10_mem0*MAS_MEM[2]
	S += (DY10_*MAS[3])-1 < DY10_mem0*MAS_MEM[3]
	S += DY10_mem0 <= DY10

	DY10_mem1 = S.Task('DY10_mem1', length=1, delay_cost=1)
	DY10_mem1 += MAIN_MEM_r
	S += DY10_mem1 <= DY10

	NY11_in = S.Task('NY11_in', length=1, delay_cost=1)
	NY11_in += alt(MM_in)
	NY11 = S.Task('NY11', length=7, delay_cost=1)
	NY11 += alt(MM)
	S += NY11>=NY11_in

	NY11_mem0 = S.Task('NY11_mem0', length=1, delay_cost=1)
	NY11_mem0 += alt(MAS_MEM)
	S += (NY11_*MAS[0])-1 < NY11_mem0*MAS_MEM[0]
	S += (NY11_*MAS[1])-1 < NY11_mem0*MAS_MEM[1]
	S += (NY11_*MAS[2])-1 < NY11_mem0*MAS_MEM[2]
	S += (NY11_*MAS[3])-1 < NY11_mem0*MAS_MEM[3]
	S += NY11_mem0 <= NY11

	NY11_mem1 = S.Task('NY11_mem1', length=1, delay_cost=1)
	NY11_mem1 += MAIN_MEM_r
	S += NY11_mem1 <= NY11

	DY11_ = S.Task('DY11_', length=1, delay_cost=1)
	DY11_ += alt(MAS)

	DY11__mem0 = S.Task('DY11__mem0', length=1, delay_cost=1)
	DY11__mem0 += alt(MM_MEM)
	S += (DY10*MM[0])-1 < DY11__mem0*MM_MEM[0]
	S += DY11__mem0 <= DY11_

	DY11__mem1 = S.Task('DY11__mem1', length=1, delay_cost=1)
	DY11__mem1 += MM_MEM[0]
	S += 93 < DY11__mem1
	S += DY11__mem1 <= DY11_

	NY12_ = S.Task('NY12_', length=1, delay_cost=1)
	NY12_ += alt(MAS)

	NY12__mem0 = S.Task('NY12__mem0', length=1, delay_cost=1)
	NY12__mem0 += alt(MM_MEM)
	S += (NY11*MM[0])-1 < NY12__mem0*MM_MEM[0]
	S += NY12__mem0 <= NY12_

	NY12__mem1 = S.Task('NY12__mem1', length=1, delay_cost=1)
	NY12__mem1 += MM_MEM[0]
	S += 92 < NY12__mem1
	S += NY12__mem1 <= NY12_

	DY11_in = S.Task('DY11_in', length=1, delay_cost=1)
	DY11_in += alt(MM_in)
	DY11 = S.Task('DY11', length=7, delay_cost=1)
	DY11 += alt(MM)
	S += DY11>=DY11_in

	DY11_mem0 = S.Task('DY11_mem0', length=1, delay_cost=1)
	DY11_mem0 += alt(MAS_MEM)
	S += (DY11_*MAS[0])-1 < DY11_mem0*MAS_MEM[0]
	S += (DY11_*MAS[1])-1 < DY11_mem0*MAS_MEM[1]
	S += (DY11_*MAS[2])-1 < DY11_mem0*MAS_MEM[2]
	S += (DY11_*MAS[3])-1 < DY11_mem0*MAS_MEM[3]
	S += DY11_mem0 <= DY11

	DY11_mem1 = S.Task('DY11_mem1', length=1, delay_cost=1)
	DY11_mem1 += MAIN_MEM_r
	S += DY11_mem1 <= DY11

	NY12_in = S.Task('NY12_in', length=1, delay_cost=1)
	NY12_in += alt(MM_in)
	NY12 = S.Task('NY12', length=7, delay_cost=1)
	NY12 += alt(MM)
	S += NY12>=NY12_in

	NY12_mem0 = S.Task('NY12_mem0', length=1, delay_cost=1)
	NY12_mem0 += alt(MAS_MEM)
	S += (NY12_*MAS[0])-1 < NY12_mem0*MAS_MEM[0]
	S += (NY12_*MAS[1])-1 < NY12_mem0*MAS_MEM[1]
	S += (NY12_*MAS[2])-1 < NY12_mem0*MAS_MEM[2]
	S += (NY12_*MAS[3])-1 < NY12_mem0*MAS_MEM[3]
	S += NY12_mem0 <= NY12

	NY12_mem1 = S.Task('NY12_mem1', length=1, delay_cost=1)
	NY12_mem1 += MAIN_MEM_r
	S += NY12_mem1 <= NY12

	DY12_ = S.Task('DY12_', length=1, delay_cost=1)
	DY12_ += alt(MAS)

	DY12__mem0 = S.Task('DY12__mem0', length=1, delay_cost=1)
	DY12__mem0 += alt(MM_MEM)
	S += (DY11*MM[0])-1 < DY12__mem0*MM_MEM[0]
	S += DY12__mem0 <= DY12_

	DY12__mem1 = S.Task('DY12__mem1', length=1, delay_cost=1)
	DY12__mem1 += MM_MEM[0]
	S += 101 < DY12__mem1
	S += DY12__mem1 <= DY12_

	NY13_ = S.Task('NY13_', length=1, delay_cost=1)
	NY13_ += alt(MAS)

	NY13__mem0 = S.Task('NY13__mem0', length=1, delay_cost=1)
	NY13__mem0 += alt(MM_MEM)
	S += (NY12*MM[0])-1 < NY13__mem0*MM_MEM[0]
	S += NY13__mem0 <= NY13_

	NY13__mem1 = S.Task('NY13__mem1', length=1, delay_cost=1)
	NY13__mem1 += MM_MEM[0]
	S += 100 < NY13__mem1
	S += NY13__mem1 <= NY13_

	DY12_in = S.Task('DY12_in', length=1, delay_cost=1)
	DY12_in += alt(MM_in)
	DY12 = S.Task('DY12', length=7, delay_cost=1)
	DY12 += alt(MM)
	S += DY12>=DY12_in

	DY12_mem0 = S.Task('DY12_mem0', length=1, delay_cost=1)
	DY12_mem0 += alt(MAS_MEM)
	S += (DY12_*MAS[0])-1 < DY12_mem0*MAS_MEM[0]
	S += (DY12_*MAS[1])-1 < DY12_mem0*MAS_MEM[1]
	S += (DY12_*MAS[2])-1 < DY12_mem0*MAS_MEM[2]
	S += (DY12_*MAS[3])-1 < DY12_mem0*MAS_MEM[3]
	S += DY12_mem0 <= DY12

	DY12_mem1 = S.Task('DY12_mem1', length=1, delay_cost=1)
	DY12_mem1 += MAIN_MEM_r
	S += DY12_mem1 <= DY12

	NY13_in = S.Task('NY13_in', length=1, delay_cost=1)
	NY13_in += alt(MM_in)
	NY13 = S.Task('NY13', length=7, delay_cost=1)
	NY13 += alt(MM)
	S += NY13>=NY13_in

	NY13_mem0 = S.Task('NY13_mem0', length=1, delay_cost=1)
	NY13_mem0 += alt(MAS_MEM)
	S += (NY13_*MAS[0])-1 < NY13_mem0*MAS_MEM[0]
	S += (NY13_*MAS[1])-1 < NY13_mem0*MAS_MEM[1]
	S += (NY13_*MAS[2])-1 < NY13_mem0*MAS_MEM[2]
	S += (NY13_*MAS[3])-1 < NY13_mem0*MAS_MEM[3]
	S += NY13_mem0 <= NY13

	NY13_mem1 = S.Task('NY13_mem1', length=1, delay_cost=1)
	NY13_mem1 += MAIN_MEM_r
	S += NY13_mem1 <= NY13

	DY13_ = S.Task('DY13_', length=1, delay_cost=1)
	DY13_ += alt(MAS)

	DY13__mem0 = S.Task('DY13__mem0', length=1, delay_cost=1)
	DY13__mem0 += alt(MM_MEM)
	S += (DY12*MM[0])-1 < DY13__mem0*MM_MEM[0]
	S += DY13__mem0 <= DY13_

	DY13__mem1 = S.Task('DY13__mem1', length=1, delay_cost=1)
	DY13__mem1 += MM_MEM[0]
	S += 109 < DY13__mem1
	S += DY13__mem1 <= DY13_

	NY14_ = S.Task('NY14_', length=1, delay_cost=1)
	NY14_ += alt(MAS)

	NY14__mem0 = S.Task('NY14__mem0', length=1, delay_cost=1)
	NY14__mem0 += alt(MM_MEM)
	S += (NY13*MM[0])-1 < NY14__mem0*MM_MEM[0]
	S += NY14__mem0 <= NY14_

	NY14__mem1 = S.Task('NY14__mem1', length=1, delay_cost=1)
	NY14__mem1 += MM_MEM[0]
	S += 108 < NY14__mem1
	S += NY14__mem1 <= NY14_

	DY13_in = S.Task('DY13_in', length=1, delay_cost=1)
	DY13_in += alt(MM_in)
	DY13 = S.Task('DY13', length=7, delay_cost=1)
	DY13 += alt(MM)
	S += DY13>=DY13_in

	DY13_mem0 = S.Task('DY13_mem0', length=1, delay_cost=1)
	DY13_mem0 += alt(MAS_MEM)
	S += (DY13_*MAS[0])-1 < DY13_mem0*MAS_MEM[0]
	S += (DY13_*MAS[1])-1 < DY13_mem0*MAS_MEM[1]
	S += (DY13_*MAS[2])-1 < DY13_mem0*MAS_MEM[2]
	S += (DY13_*MAS[3])-1 < DY13_mem0*MAS_MEM[3]
	S += DY13_mem0 <= DY13

	DY13_mem1 = S.Task('DY13_mem1', length=1, delay_cost=1)
	DY13_mem1 += MAIN_MEM_r
	S += DY13_mem1 <= DY13

	NY14_in = S.Task('NY14_in', length=1, delay_cost=1)
	NY14_in += alt(MM_in)
	NY14 = S.Task('NY14', length=7, delay_cost=1)
	NY14 += alt(MM)
	S += NY14>=NY14_in

	NY14_mem0 = S.Task('NY14_mem0', length=1, delay_cost=1)
	NY14_mem0 += alt(MAS_MEM)
	S += (NY14_*MAS[0])-1 < NY14_mem0*MAS_MEM[0]
	S += (NY14_*MAS[1])-1 < NY14_mem0*MAS_MEM[1]
	S += (NY14_*MAS[2])-1 < NY14_mem0*MAS_MEM[2]
	S += (NY14_*MAS[3])-1 < NY14_mem0*MAS_MEM[3]
	S += NY14_mem0 <= NY14

	NY14_mem1 = S.Task('NY14_mem1', length=1, delay_cost=1)
	NY14_mem1 += MAIN_MEM_r
	S += NY14_mem1 <= NY14

	DY14_ = S.Task('DY14_', length=1, delay_cost=1)
	DY14_ += alt(MAS)

	DY14__mem0 = S.Task('DY14__mem0', length=1, delay_cost=1)
	DY14__mem0 += alt(MM_MEM)
	S += (DY13*MM[0])-1 < DY14__mem0*MM_MEM[0]
	S += DY14__mem0 <= DY14_

	DY14__mem1 = S.Task('DY14__mem1', length=1, delay_cost=1)
	DY14__mem1 += MM_MEM[0]
	S += 117 < DY14__mem1
	S += DY14__mem1 <= DY14_

	NY15_ = S.Task('NY15_', length=1, delay_cost=1)
	NY15_ += alt(MAS)

	NY15__mem0 = S.Task('NY15__mem0', length=1, delay_cost=1)
	NY15__mem0 += alt(MM_MEM)
	S += (NY14*MM[0])-1 < NY15__mem0*MM_MEM[0]
	S += NY15__mem0 <= NY15_

	NY15__mem1 = S.Task('NY15__mem1', length=1, delay_cost=1)
	NY15__mem1 += MM_MEM[0]
	S += 116 < NY15__mem1
	S += NY15__mem1 <= NY15_

	DY14_in = S.Task('DY14_in', length=1, delay_cost=1)
	DY14_in += alt(MM_in)
	DY14 = S.Task('DY14', length=7, delay_cost=1)
	DY14 += alt(MM)
	S += DY14>=DY14_in

	DY14_mem0 = S.Task('DY14_mem0', length=1, delay_cost=1)
	DY14_mem0 += alt(MAS_MEM)
	S += (DY14_*MAS[0])-1 < DY14_mem0*MAS_MEM[0]
	S += (DY14_*MAS[1])-1 < DY14_mem0*MAS_MEM[1]
	S += (DY14_*MAS[2])-1 < DY14_mem0*MAS_MEM[2]
	S += (DY14_*MAS[3])-1 < DY14_mem0*MAS_MEM[3]
	S += DY14_mem0 <= DY14

	DY14_mem1 = S.Task('DY14_mem1', length=1, delay_cost=1)
	DY14_mem1 += MAIN_MEM_r
	S += DY14_mem1 <= DY14

	NY_in = S.Task('NY_in', length=1, delay_cost=1)
	NY_in += alt(MM_in)
	NY = S.Task('NY', length=7, delay_cost=1)
	NY += alt(MM)
	S += NY>=NY_in

	NY_mem0 = S.Task('NY_mem0', length=1, delay_cost=1)
	NY_mem0 += alt(MAS_MEM)
	S += (NY15_*MAS[0])-1 < NY_mem0*MAS_MEM[0]
	S += (NY15_*MAS[1])-1 < NY_mem0*MAS_MEM[1]
	S += (NY15_*MAS[2])-1 < NY_mem0*MAS_MEM[2]
	S += (NY15_*MAS[3])-1 < NY_mem0*MAS_MEM[3]
	S += NY_mem0 <= NY

	NY_mem1 = S.Task('NY_mem1', length=1, delay_cost=1)
	NY_mem1 += MAIN_MEM_r
	S += NY_mem1 <= NY

	DY = S.Task('DY', length=1, delay_cost=1)
	DY += alt(MAS)

	DY_mem0 = S.Task('DY_mem0', length=1, delay_cost=1)
	DY_mem0 += alt(MM_MEM)
	S += (DY14*MM[0])-1 < DY_mem0*MM_MEM[0]
	S += DY_mem0 <= DY

	DY_mem1 = S.Task('DY_mem1', length=1, delay_cost=1)
	DY_mem1 += MM_MEM[0]
	S += 121 < DY_mem1
	S += DY_mem1 <= DY

	Z_new_in = S.Task('Z_new_in', length=1, delay_cost=1)
	Z_new_in += alt(MM_in)
	Z_new = S.Task('Z_new', length=7, delay_cost=1)
	Z_new += alt(MM)
	S += Z_new>=Z_new_in

	S += 0<Z_new

	Z_new_mem0 = S.Task('Z_new_mem0', length=1, delay_cost=1)
	Z_new_mem0 += alt(MAS_MEM)
	S += (DX*MAS[0])-1 < Z_new_mem0*MAS_MEM[0]
	S += (DX*MAS[1])-1 < Z_new_mem0*MAS_MEM[1]
	S += (DX*MAS[2])-1 < Z_new_mem0*MAS_MEM[2]
	S += (DX*MAS[3])-1 < Z_new_mem0*MAS_MEM[3]
	S += Z_new_mem0 <= Z_new

	Z_new_mem1 = S.Task('Z_new_mem1', length=1, delay_cost=1)
	Z_new_mem1 += alt(MAS_MEM)
	S += (DY*MAS[0])-1 < Z_new_mem1*MAS_MEM[0]
	S += (DY*MAS[1])-1 < Z_new_mem1*MAS_MEM[1]
	S += (DY*MAS[2])-1 < Z_new_mem1*MAS_MEM[2]
	S += (DY*MAS[3])-1 < Z_new_mem1*MAS_MEM[3]
	S += Z_new_mem1 <= Z_new

	Z_new_w = S.Task('Z_new_w', length=1, delay_cost=1)
	Z_new_w += alt(MAIN_MEM_w)
	S += Z_new <= Z_new_w

	X_new_in = S.Task('X_new_in', length=1, delay_cost=1)
	X_new_in += alt(MM_in)
	X_new = S.Task('X_new', length=7, delay_cost=1)
	X_new += alt(MM)
	S += X_new>=X_new_in

	S += 0<X_new

	X_new_mem0 = S.Task('X_new_mem0', length=1, delay_cost=1)
	X_new_mem0 += alt(MAS_MEM)
	S += (NX*MAS[0])-1 < X_new_mem0*MAS_MEM[0]
	S += (NX*MAS[1])-1 < X_new_mem0*MAS_MEM[1]
	S += (NX*MAS[2])-1 < X_new_mem0*MAS_MEM[2]
	S += (NX*MAS[3])-1 < X_new_mem0*MAS_MEM[3]
	S += X_new_mem0 <= X_new

	X_new_mem1 = S.Task('X_new_mem1', length=1, delay_cost=1)
	X_new_mem1 += alt(MAS_MEM)
	S += (DY*MAS[0])-1 < X_new_mem1*MAS_MEM[0]
	S += (DY*MAS[1])-1 < X_new_mem1*MAS_MEM[1]
	S += (DY*MAS[2])-1 < X_new_mem1*MAS_MEM[2]
	S += (DY*MAS[3])-1 < X_new_mem1*MAS_MEM[3]
	S += X_new_mem1 <= X_new

	X_new_w = S.Task('X_new_w', length=1, delay_cost=1)
	X_new_w += alt(MAIN_MEM_w)
	S += X_new <= X_new_w

	Y_new_in = S.Task('Y_new_in', length=1, delay_cost=1)
	Y_new_in += alt(MM_in)
	Y_new = S.Task('Y_new', length=7, delay_cost=1)
	Y_new += alt(MM)
	S += Y_new>=Y_new_in

	S += 0<Y_new

	Y_new_mem0 = S.Task('Y_new_mem0', length=1, delay_cost=1)
	Y_new_mem0 += alt(MM_MEM)
	S += (NY*MM[0])-1 < Y_new_mem0*MM_MEM[0]
	S += Y_new_mem0 <= Y_new

	Y_new_mem1 = S.Task('Y_new_mem1', length=1, delay_cost=1)
	Y_new_mem1 += alt(MAS_MEM)
	S += (DX*MAS[0])-1 < Y_new_mem1*MAS_MEM[0]
	S += (DX*MAS[1])-1 < Y_new_mem1*MAS_MEM[1]
	S += (DX*MAS[2])-1 < Y_new_mem1*MAS_MEM[2]
	S += (DX*MAS[3])-1 < Y_new_mem1*MAS_MEM[3]
	S += Y_new_mem1 <= Y_new

	Y_new_w = S.Task('Y_new_w', length=1, delay_cost=1)
	Y_new_w += alt(MAIN_MEM_w)
	S += Y_new <= Y_new_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage7MM1_stage1MAS4/ISOGENY/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

