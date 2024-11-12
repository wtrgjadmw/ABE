from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 167
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling
	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 0
	k0_10_Z1_in += MM_in[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 0
	k0_10_Z1_mem0 += MAIN_MEM_r

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 0
	k0_10_Z1_mem1 += MAIN_MEM_r

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 1
	NX0_in += MM_in[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 1
	NX0_mem0 += MAIN_MEM_r

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 1
	NX0_mem1 += MAIN_MEM_r

	k0_10_Z1 = S.Task('k0_10_Z1', length=5, delay_cost=1)
	S += k0_10_Z1 >= 1
	k0_10_Z1 += MM[0]

	NX0 = S.Task('NX0', length=5, delay_cost=1)
	S += NX0 >= 2
	NX0 += MM[0]

	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 2
	Z_exp2_in += MM_in[0]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 2
	Z_exp2_mem0 += MAIN_MEM_r

	Z_exp2_mem1 = S.Task('Z_exp2_mem1', length=1, delay_cost=1)
	S += Z_exp2_mem1 >= 2
	Z_exp2_mem1 += MAIN_MEM_r

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 3
	DY0_in += MM_in[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 3
	DY0_mem0 += MAIN_MEM_r

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 3
	DY0_mem1 += MAIN_MEM_r

	Z_exp2 = S.Task('Z_exp2', length=5, delay_cost=1)
	S += Z_exp2 >= 3
	Z_exp2 += MM[0]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 4
	DX0_in += MM_in[0]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 4
	DX0_mem0 += MAIN_MEM_r

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 4
	DX0_mem1 += MAIN_MEM_r

	DY0 = S.Task('DY0', length=5, delay_cost=1)
	S += DY0 >= 4
	DY0 += MM[0]

	DX0 = S.Task('DX0', length=5, delay_cost=1)
	S += DX0 >= 5
	DX0 += MM[0]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 5
	k2_14_Z1_in += MM_in[0]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 5
	k2_14_Z1_mem0 += MAIN_MEM_r

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 5
	k2_14_Z1_mem1 += MAIN_MEM_r

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 6
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 6
	NX1__mem1 += MM_MEM[0]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 6
	NY0_in += MM_in[0]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 6
	NY0_mem0 += MAIN_MEM_r

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 6
	NY0_mem1 += MAIN_MEM_r

	k2_14_Z1 = S.Task('k2_14_Z1', length=5, delay_cost=1)
	S += k2_14_Z1 >= 6
	k2_14_Z1 += MM[0]

	NX1_ = S.Task('NX1_', length=1, delay_cost=1)
	S += NX1_ >= 7
	NX1_ += MAS[0]

	NY0 = S.Task('NY0', length=5, delay_cost=1)
	S += NY0 >= 7
	NY0 += MM[0]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 7
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 7
	k3_14_Z2_mem0 += MAIN_MEM_r

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 7
	k3_14_Z2_mem1 += MM_MEM[0]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 8
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 8
	k1_9_Z2_mem0 += MAIN_MEM_r

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 8
	k1_9_Z2_mem1 += MM_MEM[0]

	k3_14_Z2 = S.Task('k3_14_Z2', length=5, delay_cost=1)
	S += k3_14_Z2 >= 8
	k3_14_Z2 += MM[0]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 9
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 9
	Z_exp3_mem0 += MM_MEM[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 9
	Z_exp3_mem1 += MAIN_MEM_r

	k1_9_Z2 = S.Task('k1_9_Z2', length=5, delay_cost=1)
	S += k1_9_Z2 >= 9
	k1_9_Z2 += MM[0]

	Z_exp3 = S.Task('Z_exp3', length=5, delay_cost=1)
	S += Z_exp3 >= 10
	Z_exp3 += MM[0]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 10
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 10
	k0_9_Z2_mem0 += MAIN_MEM_r

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 10
	k0_9_Z2_mem1 += MM_MEM[0]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 11
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 11
	NX1_mem0 += MAS_MEM[0]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 11
	NX1_mem1 += MAIN_MEM_r

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 11
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 11
	NY1__mem1 += MM_MEM[0]

	k0_9_Z2 = S.Task('k0_9_Z2', length=5, delay_cost=1)
	S += k0_9_Z2 >= 11
	k0_9_Z2 += MM[0]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 12
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 12
	DY1__mem1 += MM_MEM[0]

	NX1 = S.Task('NX1', length=5, delay_cost=1)
	S += NX1 >= 12
	NX1 += MM[0]

	NY1_ = S.Task('NY1_', length=1, delay_cost=1)
	S += NY1_ >= 12
	NY1_ += MAS[0]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 12
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 12
	NY1_mem0 += MAS_MEM[0]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 12
	NY1_mem1 += MAIN_MEM_r

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 13
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 13
	DX1__mem1 += MM_MEM[0]

	DY1_ = S.Task('DY1_', length=1, delay_cost=1)
	S += DY1_ >= 13
	DY1_ += MAS[3]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 13
	DY1_in += MM_in[0]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 13
	DY1_mem0 += MAS_MEM[3]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 13
	DY1_mem1 += MAIN_MEM_r

	NY1 = S.Task('NY1', length=5, delay_cost=1)
	S += NY1 >= 13
	NY1 += MM[0]

	DX1_ = S.Task('DX1_', length=1, delay_cost=1)
	S += DX1_ >= 14
	DX1_ += MAS[0]

	DY1 = S.Task('DY1', length=5, delay_cost=1)
	S += DY1 >= 14
	DY1 += MM[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 14
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 14
	k3_13_Z3_mem0 += MAIN_MEM_r

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 14
	k3_13_Z3_mem1 += MM_MEM[0]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 15
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 15
	k2_13_Z2_mem0 += MAIN_MEM_r

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 15
	k2_13_Z2_mem1 += MM_MEM[0]

	k3_13_Z3 = S.Task('k3_13_Z3', length=5, delay_cost=1)
	S += k3_13_Z3 >= 15
	k3_13_Z3 += MM[0]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 16
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 16
	DX1_mem0 += MAS_MEM[0]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 16
	DX1_mem1 += MAIN_MEM_r

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 16
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 16
	NX2__mem1 += MM_MEM[0]

	k2_13_Z2 = S.Task('k2_13_Z2', length=5, delay_cost=1)
	S += k2_13_Z2 >= 16
	k2_13_Z2 += MM[0]

	DX1 = S.Task('DX1', length=5, delay_cost=1)
	S += DX1 >= 17
	DX1 += MM[0]

	NX2_ = S.Task('NX2_', length=1, delay_cost=1)
	S += NX2_ >= 17
	NX2_ += MAS[2]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 17
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 17
	k1_8_Z3_mem0 += MAIN_MEM_r

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 17
	k1_8_Z3_mem1 += MM_MEM[0]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 18
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 18
	k0_8_Z3_mem0 += MAIN_MEM_r

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 18
	k0_8_Z3_mem1 += MM_MEM[0]

	k1_8_Z3 = S.Task('k1_8_Z3', length=5, delay_cost=1)
	S += k1_8_Z3 >= 18
	k1_8_Z3 += MM[0]

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 19
	DY2__mem0 += MM_MEM[0]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 19
	DY2__mem1 += MM_MEM[0]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 19
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 19
	NX2_mem0 += MAS_MEM[2]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 19
	NX2_mem1 += MAIN_MEM_r

	k0_8_Z3 = S.Task('k0_8_Z3', length=5, delay_cost=1)
	S += k0_8_Z3 >= 19
	k0_8_Z3 += MM[0]

	DY2_ = S.Task('DY2_', length=1, delay_cost=1)
	S += DY2_ >= 20
	DY2_ += MAS[3]

	NX2 = S.Task('NX2', length=5, delay_cost=1)
	S += NX2 >= 20
	NX2 += MM[0]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 20
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 20
	Z_exp4_mem0 += MM_MEM[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 20
	Z_exp4_mem1 += MAIN_MEM_r

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 21
	DY2_in += MM_in[0]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 21
	DY2_mem0 += MAS_MEM[3]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 21
	DY2_mem1 += MAIN_MEM_r

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 21
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 21
	NY2__mem1 += MM_MEM[0]

	Z_exp4 = S.Task('Z_exp4', length=5, delay_cost=1)
	S += Z_exp4 >= 21
	Z_exp4 += MM[0]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 22
	DX2__mem0 += MM_MEM[0]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 22
	DX2__mem1 += MM_MEM[0]

	DY2 = S.Task('DY2', length=5, delay_cost=1)
	S += DY2 >= 22
	DY2 += MM[0]

	NY2_ = S.Task('NY2_', length=1, delay_cost=1)
	S += NY2_ >= 22
	NY2_ += MAS[0]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 22
	NY2_in += MM_in[0]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 22
	NY2_mem0 += MAS_MEM[0]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 22
	NY2_mem1 += MAIN_MEM_r

	DX2_ = S.Task('DX2_', length=1, delay_cost=1)
	S += DX2_ >= 23
	DX2_ += MAS[0]

	NY2 = S.Task('NY2', length=5, delay_cost=1)
	S += NY2 >= 23
	NY2 += MM[0]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 23
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 23
	k2_12_Z3_mem0 += MAIN_MEM_r

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 23
	k2_12_Z3_mem1 += MM_MEM[0]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 24
	DX2_in += MM_in[0]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 24
	DX2_mem0 += MAS_MEM[0]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 24
	DX2_mem1 += MAIN_MEM_r

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 24
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 24
	NX3__mem1 += MM_MEM[0]

	k2_12_Z3 = S.Task('k2_12_Z3', length=5, delay_cost=1)
	S += k2_12_Z3 >= 24
	k2_12_Z3 += MM[0]

	DX2 = S.Task('DX2', length=5, delay_cost=1)
	S += DX2 >= 25
	DX2 += MM[0]

	NX3_ = S.Task('NX3_', length=1, delay_cost=1)
	S += NX3_ >= 25
	NX3_ += MAS[3]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 25
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 25
	Z_exp5_mem0 += MM_MEM[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 25
	Z_exp5_mem1 += MAIN_MEM_r

	Z_exp5 = S.Task('Z_exp5', length=5, delay_cost=1)
	S += Z_exp5 >= 26
	Z_exp5 += MM[0]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 26
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 26
	k2_11_Z4_mem0 += MAIN_MEM_r

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 26
	k2_11_Z4_mem1 += MM_MEM[0]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 27
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 27
	k0_7_Z4_mem0 += MAIN_MEM_r

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 27
	k0_7_Z4_mem1 += MM_MEM[0]

	k2_11_Z4 = S.Task('k2_11_Z4', length=5, delay_cost=1)
	S += k2_11_Z4 >= 27
	k2_11_Z4 += MM[0]

	k0_7_Z4 = S.Task('k0_7_Z4', length=5, delay_cost=1)
	S += k0_7_Z4 >= 28
	k0_7_Z4 += MM[0]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 28
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 28
	k3_12_Z4_mem0 += MAIN_MEM_r

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 28
	k3_12_Z4_mem1 += MM_MEM[0]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 29
	k1_7_Z4_in += MM_in[0]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 29
	k1_7_Z4_mem0 += MAIN_MEM_r

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 29
	k1_7_Z4_mem1 += MM_MEM[0]

	k3_12_Z4 = S.Task('k3_12_Z4', length=5, delay_cost=1)
	S += k3_12_Z4 >= 29
	k3_12_Z4 += MM[0]

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	S += Z_exp6_in >= 30
	Z_exp6_in += MM_in[0]

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	S += Z_exp6_mem0 >= 30
	Z_exp6_mem0 += MM_MEM[0]

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	S += Z_exp6_mem1 >= 30
	Z_exp6_mem1 += MAIN_MEM_r

	k1_7_Z4 = S.Task('k1_7_Z4', length=5, delay_cost=1)
	S += k1_7_Z4 >= 30
	k1_7_Z4 += MM[0]

	Z_exp6 = S.Task('Z_exp6', length=5, delay_cost=1)
	S += Z_exp6 >= 31
	Z_exp6 += MM[0]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 31
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 31
	k3_11_Z5_mem0 += MAIN_MEM_r

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 31
	k3_11_Z5_mem1 += MM_MEM[0]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 32
	k0_6_Z5_in += MM_in[0]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 32
	k0_6_Z5_mem0 += MAIN_MEM_r

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 32
	k0_6_Z5_mem1 += MM_MEM[0]

	k3_11_Z5 = S.Task('k3_11_Z5', length=5, delay_cost=1)
	S += k3_11_Z5 >= 32
	k3_11_Z5 += MM[0]

	k0_6_Z5 = S.Task('k0_6_Z5', length=5, delay_cost=1)
	S += k0_6_Z5 >= 33
	k0_6_Z5 += MM[0]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 33
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 33
	k2_10_Z5_mem0 += MAIN_MEM_r

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 33
	k2_10_Z5_mem1 += MM_MEM[0]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 34
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 34
	k1_6_Z5_mem0 += MAIN_MEM_r

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 34
	k1_6_Z5_mem1 += MM_MEM[0]

	k2_10_Z5 = S.Task('k2_10_Z5', length=5, delay_cost=1)
	S += k2_10_Z5 >= 34
	k2_10_Z5 += MM[0]

	k1_6_Z5 = S.Task('k1_6_Z5', length=5, delay_cost=1)
	S += k1_6_Z5 >= 35
	k1_6_Z5 += MM[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 35
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 35
	k3_10_Z6_mem0 += MAIN_MEM_r

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 35
	k3_10_Z6_mem1 += MM_MEM[0]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 36
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 36
	k2_9_Z6_mem0 += MAIN_MEM_r

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 36
	k2_9_Z6_mem1 += MM_MEM[0]

	k3_10_Z6 = S.Task('k3_10_Z6', length=5, delay_cost=1)
	S += k3_10_Z6 >= 36
	k3_10_Z6 += MM[0]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 37
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 37
	k0_5_Z6_mem0 += MAIN_MEM_r

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 37
	k0_5_Z6_mem1 += MM_MEM[0]

	k2_9_Z6 = S.Task('k2_9_Z6', length=5, delay_cost=1)
	S += k2_9_Z6 >= 37
	k2_9_Z6 += MM[0]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 38
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 38
	Z_exp7_mem0 += MM_MEM[0]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 38
	Z_exp7_mem1 += MAIN_MEM_r

	k0_5_Z6 = S.Task('k0_5_Z6', length=5, delay_cost=1)
	S += k0_5_Z6 >= 38
	k0_5_Z6 += MM[0]

	Z_exp7 = S.Task('Z_exp7', length=5, delay_cost=1)
	S += Z_exp7 >= 39
	Z_exp7 += MM[0]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 39
	k1_5_Z6_in += MM_in[0]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 39
	k1_5_Z6_mem0 += MAIN_MEM_r

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 39
	k1_5_Z6_mem1 += MM_MEM[0]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 40
	NX3_in += MM_in[0]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 40
	NX3_mem0 += MAS_MEM[3]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 40
	NX3_mem1 += MAIN_MEM_r

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 40
	NY3__mem0 += MM_MEM[0]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 40
	NY3__mem1 += MM_MEM[0]

	k1_5_Z6 = S.Task('k1_5_Z6', length=5, delay_cost=1)
	S += k1_5_Z6 >= 40
	k1_5_Z6 += MM[0]

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	S += DX3__mem0 >= 41
	DX3__mem0 += MM_MEM[0]

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	S += DX3__mem1 >= 41
	DX3__mem1 += MM_MEM[0]

	NX3 = S.Task('NX3', length=5, delay_cost=1)
	S += NX3 >= 41
	NX3 += MM[0]

	NY3_ = S.Task('NY3_', length=1, delay_cost=1)
	S += NY3_ >= 41
	NY3_ += MAS[0]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 41
	NY3_in += MM_in[0]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 41
	NY3_mem0 += MAS_MEM[0]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 41
	NY3_mem1 += MAIN_MEM_r

	DX3_ = S.Task('DX3_', length=1, delay_cost=1)
	S += DX3_ >= 42
	DX3_ += MAS[2]

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	S += DX3_in >= 42
	DX3_in += MM_in[0]

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	S += DX3_mem0 >= 42
	DX3_mem0 += MAS_MEM[2]

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	S += DX3_mem1 >= 42
	DX3_mem1 += MAIN_MEM_r

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	S += DY3__mem0 >= 42
	DY3__mem0 += MM_MEM[0]

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	S += DY3__mem1 >= 42
	DY3__mem1 += MM_MEM[0]

	NY3 = S.Task('NY3', length=5, delay_cost=1)
	S += NY3 >= 42
	NY3 += MM[0]

	DX3 = S.Task('DX3', length=5, delay_cost=1)
	S += DX3 >= 43
	DX3 += MM[0]

	DY3_ = S.Task('DY3_', length=1, delay_cost=1)
	S += DY3_ >= 43
	DY3_ += MAS[2]

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	S += Z_exp8_in >= 43
	Z_exp8_in += MM_in[0]

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	S += Z_exp8_mem0 >= 43
	Z_exp8_mem0 += MM_MEM[0]

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	S += Z_exp8_mem1 >= 43
	Z_exp8_mem1 += MAIN_MEM_r

	Z_exp8 = S.Task('Z_exp8', length=5, delay_cost=1)
	S += Z_exp8 >= 44
	Z_exp8 += MM[0]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 44
	k3_9_Z7_in += MM_in[0]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 44
	k3_9_Z7_mem0 += MAIN_MEM_r

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 44
	k3_9_Z7_mem1 += MM_MEM[0]

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	S += DY3_in >= 45
	DY3_in += MM_in[0]

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	S += DY3_mem0 >= 45
	DY3_mem0 += MAS_MEM[2]

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	S += DY3_mem1 >= 45
	DY3_mem1 += MAIN_MEM_r

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 45
	NX4__mem0 += MM_MEM[0]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 45
	NX4__mem1 += MM_MEM[0]

	k3_9_Z7 = S.Task('k3_9_Z7', length=5, delay_cost=1)
	S += k3_9_Z7 >= 45
	k3_9_Z7 += MM[0]

	DY3 = S.Task('DY3', length=5, delay_cost=1)
	S += DY3 >= 46
	DY3 += MM[0]

	NX4_ = S.Task('NX4_', length=1, delay_cost=1)
	S += NX4_ >= 46
	NX4_ += MAS[0]

	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	S += NX4_in >= 46
	NX4_in += MM_in[0]

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	S += NX4_mem0 >= 46
	NX4_mem0 += MAS_MEM[0]

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	S += NX4_mem1 >= 46
	NX4_mem1 += MAIN_MEM_r

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 46
	NY4__mem0 += MM_MEM[0]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 46
	NY4__mem1 += MM_MEM[0]

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	S += DX4__mem0 >= 47
	DX4__mem0 += MM_MEM[0]

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	S += DX4__mem1 >= 47
	DX4__mem1 += MM_MEM[0]

	NX4 = S.Task('NX4', length=5, delay_cost=1)
	S += NX4 >= 47
	NX4 += MM[0]

	NY4_ = S.Task('NY4_', length=1, delay_cost=1)
	S += NY4_ >= 47
	NY4_ += MAS[2]

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	S += NY4_in >= 47
	NY4_in += MM_in[0]

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	S += NY4_mem0 >= 47
	NY4_mem0 += MAS_MEM[2]

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	S += NY4_mem1 >= 47
	NY4_mem1 += MAIN_MEM_r

	DX4_ = S.Task('DX4_', length=1, delay_cost=1)
	S += DX4_ >= 48
	DX4_ += MAS[1]

	NY4 = S.Task('NY4', length=5, delay_cost=1)
	S += NY4 >= 48
	NY4 += MM[0]

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	S += Z_exp9_in >= 48
	Z_exp9_in += MM_in[0]

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	S += Z_exp9_mem0 >= 48
	Z_exp9_mem0 += MM_MEM[0]

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	S += Z_exp9_mem1 >= 48
	Z_exp9_mem1 += MAIN_MEM_r

	Z_exp9 = S.Task('Z_exp9', length=5, delay_cost=1)
	S += Z_exp9 >= 49
	Z_exp9 += MM[0]

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	S += k2_8_Z7_in >= 49
	k2_8_Z7_in += MM_in[0]

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	S += k2_8_Z7_mem0 >= 49
	k2_8_Z7_mem0 += MAIN_MEM_r

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	S += k2_8_Z7_mem1 >= 49
	k2_8_Z7_mem1 += MM_MEM[0]

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	S += DX4_in >= 50
	DX4_in += MM_in[0]

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	S += DX4_mem0 >= 50
	DX4_mem0 += MAS_MEM[1]

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	S += DX4_mem1 >= 50
	DX4_mem1 += MAIN_MEM_r

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	S += DY4__mem0 >= 50
	DY4__mem0 += MM_MEM[0]

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	S += DY4__mem1 >= 50
	DY4__mem1 += MM_MEM[0]

	k2_8_Z7 = S.Task('k2_8_Z7', length=5, delay_cost=1)
	S += k2_8_Z7 >= 50
	k2_8_Z7 += MM[0]

	DX4 = S.Task('DX4', length=5, delay_cost=1)
	S += DX4 >= 51
	DX4 += MM[0]

	DY4_ = S.Task('DY4_', length=1, delay_cost=1)
	S += DY4_ >= 51
	DY4_ += MAS[2]

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	S += DY4_in >= 51
	DY4_in += MM_in[0]

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	S += DY4_mem0 >= 51
	DY4_mem0 += MAS_MEM[2]

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	S += DY4_mem1 >= 51
	DY4_mem1 += MAIN_MEM_r

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	S += NX5__mem0 >= 51
	NX5__mem0 += MM_MEM[0]

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	S += NX5__mem1 >= 51
	NX5__mem1 += MM_MEM[0]

	DY4 = S.Task('DY4', length=5, delay_cost=1)
	S += DY4 >= 52
	DY4 += MM[0]

	NX5_ = S.Task('NX5_', length=1, delay_cost=1)
	S += NX5_ >= 52
	NX5_ += MAS[0]

	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	S += NX5_in >= 52
	NX5_in += MM_in[0]

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	S += NX5_mem0 >= 52
	NX5_mem0 += MAS_MEM[0]

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	S += NX5_mem1 >= 52
	NX5_mem1 += MAIN_MEM_r

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	S += NY5__mem0 >= 52
	NY5__mem0 += MM_MEM[0]

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	S += NY5__mem1 >= 52
	NY5__mem1 += MM_MEM[0]

	NX5 = S.Task('NX5', length=5, delay_cost=1)
	S += NX5 >= 53
	NX5 += MM[0]

	NY5_ = S.Task('NY5_', length=1, delay_cost=1)
	S += NY5_ >= 53
	NY5_ += MAS[3]

	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	S += k2_6_Z9_in >= 53
	k2_6_Z9_in += MM_in[0]

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	S += k2_6_Z9_mem0 >= 53
	k2_6_Z9_mem0 += MAIN_MEM_r

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	S += k2_6_Z9_mem1 >= 53
	k2_6_Z9_mem1 += MM_MEM[0]

	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	S += Z_exp10_in >= 54
	Z_exp10_in += MM_in[0]

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	S += Z_exp10_mem0 >= 54
	Z_exp10_mem0 += MM_MEM[0]

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	S += Z_exp10_mem1 >= 54
	Z_exp10_mem1 += MAIN_MEM_r

	k2_6_Z9 = S.Task('k2_6_Z9', length=5, delay_cost=1)
	S += k2_6_Z9 >= 54
	k2_6_Z9 += MM[0]

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	S += DX5__mem0 >= 55
	DX5__mem0 += MM_MEM[0]

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	S += DX5__mem1 >= 55
	DX5__mem1 += MM_MEM[0]

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	S += NY5_in >= 55
	NY5_in += MM_in[0]

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	S += NY5_mem0 >= 55
	NY5_mem0 += MAS_MEM[3]

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	S += NY5_mem1 >= 55
	NY5_mem1 += MAIN_MEM_r

	Z_exp10 = S.Task('Z_exp10', length=5, delay_cost=1)
	S += Z_exp10 >= 55
	Z_exp10 += MM[0]

	DX5_ = S.Task('DX5_', length=1, delay_cost=1)
	S += DX5_ >= 56
	DX5_ += MAS[2]

	NY5 = S.Task('NY5', length=5, delay_cost=1)
	S += NY5 >= 56
	NY5 += MM[0]

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	S += k3_7_Z9_in >= 56
	k3_7_Z9_in += MM_in[0]

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	S += k3_7_Z9_mem0 >= 56
	k3_7_Z9_mem0 += MAIN_MEM_r

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	S += k3_7_Z9_mem1 >= 56
	k3_7_Z9_mem1 += MM_MEM[0]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 57
	k1_4_Z7_in += MM_in[0]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 57
	k1_4_Z7_mem0 += MAIN_MEM_r

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 57
	k1_4_Z7_mem1 += MM_MEM[0]

	k3_7_Z9 = S.Task('k3_7_Z9', length=5, delay_cost=1)
	S += k3_7_Z9 >= 57
	k3_7_Z9 += MM[0]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 58
	k0_3_Z8_in += MM_in[0]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 58
	k0_3_Z8_mem0 += MAIN_MEM_r

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 58
	k0_3_Z8_mem1 += MM_MEM[0]

	k1_4_Z7 = S.Task('k1_4_Z7', length=5, delay_cost=1)
	S += k1_4_Z7 >= 58
	k1_4_Z7 += MM[0]

	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	S += k0_2_Z9_in >= 59
	k0_2_Z9_in += MM_in[0]

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	S += k0_2_Z9_mem0 >= 59
	k0_2_Z9_mem0 += MAIN_MEM_r

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	S += k0_2_Z9_mem1 >= 59
	k0_2_Z9_mem1 += MM_MEM[0]

	k0_3_Z8 = S.Task('k0_3_Z8', length=5, delay_cost=1)
	S += k0_3_Z8 >= 59
	k0_3_Z8 += MM[0]

	k0_2_Z9 = S.Task('k0_2_Z9', length=5, delay_cost=1)
	S += k0_2_Z9 >= 60
	k0_2_Z9 += MM[0]

	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	S += k3_6_Z10_in >= 60
	k3_6_Z10_in += MM_in[0]

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	S += k3_6_Z10_mem0 >= 60
	k3_6_Z10_mem0 += MAIN_MEM_r

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	S += k3_6_Z10_mem1 >= 60
	k3_6_Z10_mem1 += MM_MEM[0]

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	S += Z_exp11_in >= 61
	Z_exp11_in += MM_in[0]

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	S += Z_exp11_mem0 >= 61
	Z_exp11_mem0 += MM_MEM[0]

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	S += Z_exp11_mem1 >= 61
	Z_exp11_mem1 += MAIN_MEM_r

	k3_6_Z10 = S.Task('k3_6_Z10', length=5, delay_cost=1)
	S += k3_6_Z10 >= 61
	k3_6_Z10 += MM[0]

	Z_exp11 = S.Task('Z_exp11', length=5, delay_cost=1)
	S += Z_exp11 >= 62
	Z_exp11 += MM[0]

	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	S += k1_1_Z10_in >= 62
	k1_1_Z10_in += MM_in[0]

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	S += k1_1_Z10_mem0 >= 62
	k1_1_Z10_mem0 += MAIN_MEM_r

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	S += k1_1_Z10_mem1 >= 62
	k1_1_Z10_mem1 += MM_MEM[0]

	k1_1_Z10 = S.Task('k1_1_Z10', length=5, delay_cost=1)
	S += k1_1_Z10 >= 63
	k1_1_Z10 += MM[0]

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	S += k2_5_Z10_in >= 63
	k2_5_Z10_in += MM_in[0]

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	S += k2_5_Z10_mem0 >= 63
	k2_5_Z10_mem0 += MAIN_MEM_r

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	S += k2_5_Z10_mem1 >= 63
	k2_5_Z10_mem1 += MM_MEM[0]

	k2_5_Z10 = S.Task('k2_5_Z10', length=5, delay_cost=1)
	S += k2_5_Z10 >= 64
	k2_5_Z10 += MM[0]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 64
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 64
	k2_7_Z8_mem0 += MAIN_MEM_r

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 64
	k2_7_Z8_mem1 += MM_MEM[0]

	k2_7_Z8 = S.Task('k2_7_Z8', length=5, delay_cost=1)
	S += k2_7_Z8 >= 65
	k2_7_Z8 += MM[0]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 65
	k3_8_Z8_in += MM_in[0]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 65
	k3_8_Z8_mem0 += MAIN_MEM_r

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 65
	k3_8_Z8_mem1 += MM_MEM[0]

	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	S += k0_0_Z11_in >= 66
	k0_0_Z11_in += MM_in[0]

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	S += k0_0_Z11_mem0 >= 66
	k0_0_Z11_mem0 += MAIN_MEM_r

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	S += k0_0_Z11_mem1 >= 66
	k0_0_Z11_mem1 += MM_MEM[0]

	k3_8_Z8 = S.Task('k3_8_Z8', length=5, delay_cost=1)
	S += k3_8_Z8 >= 66
	k3_8_Z8 += MM[0]

	k0_0_Z11 = S.Task('k0_0_Z11', length=5, delay_cost=1)
	S += k0_0_Z11 >= 67
	k0_0_Z11 += MM[0]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 67
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 67
	k1_3_Z8_mem0 += MAIN_MEM_r

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 67
	k1_3_Z8_mem1 += MM_MEM[0]

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	S += Z_exp12_in >= 68
	Z_exp12_in += MM_in[0]

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	S += Z_exp12_mem0 >= 68
	Z_exp12_mem0 += MM_MEM[0]

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	S += Z_exp12_mem1 >= 68
	Z_exp12_mem1 += MAIN_MEM_r

	k1_3_Z8 = S.Task('k1_3_Z8', length=5, delay_cost=1)
	S += k1_3_Z8 >= 68
	k1_3_Z8 += MM[0]

	Z_exp12 = S.Task('Z_exp12', length=5, delay_cost=1)
	S += Z_exp12 >= 69
	Z_exp12 += MM[0]

	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	S += k2_4_Z11_in >= 69
	k2_4_Z11_in += MM_in[0]

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	S += k2_4_Z11_mem0 >= 69
	k2_4_Z11_mem0 += MAIN_MEM_r

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	S += k2_4_Z11_mem1 >= 69
	k2_4_Z11_mem1 += MM_MEM[0]

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	S += k1_0_Z11_in >= 70
	k1_0_Z11_in += MM_in[0]

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	S += k1_0_Z11_mem0 >= 70
	k1_0_Z11_mem0 += MAIN_MEM_r

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	S += k1_0_Z11_mem1 >= 70
	k1_0_Z11_mem1 += MM_MEM[0]

	k2_4_Z11 = S.Task('k2_4_Z11', length=5, delay_cost=1)
	S += k2_4_Z11 >= 70
	k2_4_Z11 += MM[0]

	k1_0_Z11 = S.Task('k1_0_Z11', length=5, delay_cost=1)
	S += k1_0_Z11 >= 71
	k1_0_Z11 += MM[0]

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	S += k1_2_Z9_in >= 71
	k1_2_Z9_in += MM_in[0]

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	S += k1_2_Z9_mem0 >= 71
	k1_2_Z9_mem0 += MAIN_MEM_r

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	S += k1_2_Z9_mem1 >= 71
	k1_2_Z9_mem1 += MM_MEM[0]

	k1_2_Z9 = S.Task('k1_2_Z9', length=5, delay_cost=1)
	S += k1_2_Z9 >= 72
	k1_2_Z9 += MM[0]

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	S += k3_5_Z11_in >= 72
	k3_5_Z11_in += MM_in[0]

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	S += k3_5_Z11_mem0 >= 72
	k3_5_Z11_mem0 += MAIN_MEM_r

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	S += k3_5_Z11_mem1 >= 72
	k3_5_Z11_mem1 += MM_MEM[0]

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	S += k0_1_Z10_in >= 73
	k0_1_Z10_in += MM_in[0]

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	S += k0_1_Z10_mem0 >= 73
	k0_1_Z10_mem0 += MAIN_MEM_r

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	S += k0_1_Z10_mem1 >= 73
	k0_1_Z10_mem1 += MM_MEM[0]

	k3_5_Z11 = S.Task('k3_5_Z11', length=5, delay_cost=1)
	S += k3_5_Z11 >= 73
	k3_5_Z11 += MM[0]

	k0_1_Z10 = S.Task('k0_1_Z10', length=5, delay_cost=1)
	S += k0_1_Z10 >= 74
	k0_1_Z10 += MM[0]

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	S += k0_4_Z7_in >= 74
	k0_4_Z7_in += MM_in[0]

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	S += k0_4_Z7_mem0 >= 74
	k0_4_Z7_mem0 += MAIN_MEM_r

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	S += k0_4_Z7_mem1 >= 74
	k0_4_Z7_mem1 += MM_MEM[0]

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	S += DY5__mem0 >= 75
	DY5__mem0 += MM_MEM[0]

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	S += DY5__mem1 >= 75
	DY5__mem1 += MM_MEM[0]

	k0_4_Z7 = S.Task('k0_4_Z7', length=5, delay_cost=1)
	S += k0_4_Z7 >= 75
	k0_4_Z7 += MM[0]

	DY5_ = S.Task('DY5_', length=1, delay_cost=1)
	S += DY5_ >= 76
	DY5_ += MAS[0]


	# new tasks
	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	Z_exp13_in += alt(MM_in)
	Z_exp13 = S.Task('Z_exp13', length=5, delay_cost=1)
	Z_exp13 += alt(MM)
	S += Z_exp13>=Z_exp13_in

	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	Z_exp13_mem0 += MM_MEM[0]
	S += 73 < Z_exp13_mem0
	S += Z_exp13_mem0 <= Z_exp13

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	Z_exp13_mem1 += MAIN_MEM_r
	S += Z_exp13_mem1 <= Z_exp13

	NX6_ = S.Task('NX6_', length=1, delay_cost=1)
	NX6_ += alt(MAS)

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	NX6__mem0 += MM_MEM[0]
	S += 57 < NX6__mem0
	S += NX6__mem0 <= NX6_

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	NX6__mem1 += MM_MEM[0]
	S += 42 < NX6__mem1
	S += NX6__mem1 <= NX6_

	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	DX5_in += alt(MM_in)
	DX5 = S.Task('DX5', length=5, delay_cost=1)
	DX5 += alt(MM)
	S += DX5>=DX5_in

	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	DX5_mem0 += MAS_MEM[2]
	S += 56 < DX5_mem0
	S += DX5_mem0 <= DX5

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	DX5_mem1 += MAIN_MEM_r
	S += DX5_mem1 <= DX5

	NY6_ = S.Task('NY6_', length=1, delay_cost=1)
	NY6_ += alt(MAS)

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	NY6__mem0 += MM_MEM[0]
	S += 60 < NY6__mem0
	S += NY6__mem0 <= NY6_

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	NY6__mem1 += MM_MEM[0]
	S += 41 < NY6__mem1
	S += NY6__mem1 <= NY6_

	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	k2_3_Z12_in += alt(MM_in)
	k2_3_Z12 = S.Task('k2_3_Z12', length=5, delay_cost=1)
	k2_3_Z12 += alt(MM)
	S += k2_3_Z12>=k2_3_Z12_in

	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	k2_3_Z12_mem0 += MAIN_MEM_r
	S += k2_3_Z12_mem0 <= k2_3_Z12

	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	k2_3_Z12_mem1 += MM_MEM[0]
	S += 73 < k2_3_Z12_mem1
	S += k2_3_Z12_mem1 <= k2_3_Z12

	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	DY5_in += alt(MM_in)
	DY5 = S.Task('DY5', length=5, delay_cost=1)
	DY5 += alt(MM)
	S += DY5>=DY5_in

	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	DY5_mem0 += MAS_MEM[0]
	S += 76 < DY5_mem0
	S += DY5_mem0 <= DY5

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	DY5_mem1 += MAIN_MEM_r
	S += DY5_mem1 <= DY5

	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	k3_4_Z12_in += alt(MM_in)
	k3_4_Z12 = S.Task('k3_4_Z12', length=5, delay_cost=1)
	k3_4_Z12 += alt(MM)
	S += k3_4_Z12>=k3_4_Z12_in

	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	k3_4_Z12_mem0 += MAIN_MEM_r
	S += k3_4_Z12_mem0 <= k3_4_Z12

	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	k3_4_Z12_mem1 += MM_MEM[0]
	S += 73 < k3_4_Z12_mem1
	S += k3_4_Z12_mem1 <= k3_4_Z12

	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	Z_exp14_in += alt(MM_in)
	Z_exp14 = S.Task('Z_exp14', length=5, delay_cost=1)
	Z_exp14 += alt(MM)
	S += Z_exp14>=Z_exp14_in

	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	Z_exp14_mem0 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < Z_exp14_mem0*MM_MEM[0]
	S += Z_exp14_mem0 <= Z_exp14

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	Z_exp14_mem1 += MAIN_MEM_r
	S += Z_exp14_mem1 <= Z_exp14

	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	NX6_in += alt(MM_in)
	NX6 = S.Task('NX6', length=5, delay_cost=1)
	NX6 += alt(MM)
	S += NX6>=NX6_in

	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	NX6_mem0 += alt(MAS_MEM)
	S += (NX6_*MAS[0])-1 < NX6_mem0*MAS_MEM[0]
	S += (NX6_*MAS[1])-1 < NX6_mem0*MAS_MEM[1]
	S += (NX6_*MAS[2])-1 < NX6_mem0*MAS_MEM[2]
	S += (NX6_*MAS[3])-1 < NX6_mem0*MAS_MEM[3]
	S += NX6_mem0 <= NX6

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	NX6_mem1 += MAIN_MEM_r
	S += NX6_mem1 <= NX6

	DX6_ = S.Task('DX6_', length=1, delay_cost=1)
	DX6_ += alt(MAS)

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	DX6__mem0 += alt(MM_MEM)
	S += (DX5*MM[0])-1 < DX6__mem0*MM_MEM[0]
	S += DX6__mem0 <= DX6_

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	DX6__mem1 += MM_MEM[0]
	S += 62 < DX6__mem1
	S += DX6__mem1 <= DX6_

	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	NY6_in += alt(MM_in)
	NY6 = S.Task('NY6', length=5, delay_cost=1)
	NY6 += alt(MM)
	S += NY6>=NY6_in

	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	NY6_mem0 += alt(MAS_MEM)
	S += (NY6_*MAS[0])-1 < NY6_mem0*MAS_MEM[0]
	S += (NY6_*MAS[1])-1 < NY6_mem0*MAS_MEM[1]
	S += (NY6_*MAS[2])-1 < NY6_mem0*MAS_MEM[2]
	S += (NY6_*MAS[3])-1 < NY6_mem0*MAS_MEM[3]
	S += NY6_mem0 <= NY6

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	NY6_mem1 += MAIN_MEM_r
	S += NY6_mem1 <= NY6

	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	k2_2_Z13_in += alt(MM_in)
	k2_2_Z13 = S.Task('k2_2_Z13', length=5, delay_cost=1)
	k2_2_Z13 += alt(MM)
	S += k2_2_Z13>=k2_2_Z13_in

	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	k2_2_Z13_mem0 += MAIN_MEM_r
	S += k2_2_Z13_mem0 <= k2_2_Z13

	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	k2_2_Z13_mem1 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < k2_2_Z13_mem1*MM_MEM[0]
	S += k2_2_Z13_mem1 <= k2_2_Z13

	DY6_ = S.Task('DY6_', length=1, delay_cost=1)
	DY6_ += alt(MAS)

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	DY6__mem0 += alt(MM_MEM)
	S += (DY5*MM[0])-1 < DY6__mem0*MM_MEM[0]
	S += DY6__mem0 <= DY6_

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	DY6__mem1 += MM_MEM[0]
	S += 49 < DY6__mem1
	S += DY6__mem1 <= DY6_

	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	k3_3_Z13_in += alt(MM_in)
	k3_3_Z13 = S.Task('k3_3_Z13', length=5, delay_cost=1)
	k3_3_Z13 += alt(MM)
	S += k3_3_Z13>=k3_3_Z13_in

	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	k3_3_Z13_mem0 += MAIN_MEM_r
	S += k3_3_Z13_mem0 <= k3_3_Z13

	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	k3_3_Z13_mem1 += alt(MM_MEM)
	S += (Z_exp13*MM[0])-1 < k3_3_Z13_mem1*MM_MEM[0]
	S += k3_3_Z13_mem1 <= k3_3_Z13

	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	Z_exp15_in += alt(MM_in)
	Z_exp15 = S.Task('Z_exp15', length=5, delay_cost=1)
	Z_exp15 += alt(MM)
	S += Z_exp15>=Z_exp15_in

	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	Z_exp15_mem0 += alt(MM_MEM)
	S += (Z_exp14*MM[0])-1 < Z_exp15_mem0*MM_MEM[0]
	S += Z_exp15_mem0 <= Z_exp15

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	Z_exp15_mem1 += MAIN_MEM_r
	S += Z_exp15_mem1 <= Z_exp15

	NX7_ = S.Task('NX7_', length=1, delay_cost=1)
	NX7_ += alt(MAS)

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	NX7__mem0 += alt(MM_MEM)
	S += (NX6*MM[0])-1 < NX7__mem0*MM_MEM[0]
	S += NX7__mem0 <= NX7_

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	NX7__mem1 += MM_MEM[0]
	S += 79 < NX7__mem1
	S += NX7__mem1 <= NX7_

	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	DX6_in += alt(MM_in)
	DX6 = S.Task('DX6', length=5, delay_cost=1)
	DX6 += alt(MM)
	S += DX6>=DX6_in

	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	DX6_mem0 += alt(MAS_MEM)
	S += (DX6_*MAS[0])-1 < DX6_mem0*MAS_MEM[0]
	S += (DX6_*MAS[1])-1 < DX6_mem0*MAS_MEM[1]
	S += (DX6_*MAS[2])-1 < DX6_mem0*MAS_MEM[2]
	S += (DX6_*MAS[3])-1 < DX6_mem0*MAS_MEM[3]
	S += DX6_mem0 <= DX6

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	DX6_mem1 += MAIN_MEM_r
	S += DX6_mem1 <= DX6

	NY7_ = S.Task('NY7_', length=1, delay_cost=1)
	NY7_ += alt(MAS)

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	NY7__mem0 += alt(MM_MEM)
	S += (NY6*MM[0])-1 < NY7__mem0*MM_MEM[0]
	S += NY7__mem0 <= NY7_

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	NY7__mem1 += MM_MEM[0]
	S += 54 < NY7__mem1
	S += NY7__mem1 <= NY7_

	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	k2_1_Z14_in += alt(MM_in)
	k2_1_Z14 = S.Task('k2_1_Z14', length=5, delay_cost=1)
	k2_1_Z14 += alt(MM)
	S += k2_1_Z14>=k2_1_Z14_in

	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	k2_1_Z14_mem0 += MAIN_MEM_r
	S += k2_1_Z14_mem0 <= k2_1_Z14

	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	k2_1_Z14_mem1 += alt(MM_MEM)
	S += (Z_exp14*MM[0])-1 < k2_1_Z14_mem1*MM_MEM[0]
	S += k2_1_Z14_mem1 <= k2_1_Z14

	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	DY6_in += alt(MM_in)
	DY6 = S.Task('DY6', length=5, delay_cost=1)
	DY6 += alt(MM)
	S += DY6>=DY6_in

	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	DY6_mem0 += alt(MAS_MEM)
	S += (DY6_*MAS[0])-1 < DY6_mem0*MAS_MEM[0]
	S += (DY6_*MAS[1])-1 < DY6_mem0*MAS_MEM[1]
	S += (DY6_*MAS[2])-1 < DY6_mem0*MAS_MEM[2]
	S += (DY6_*MAS[3])-1 < DY6_mem0*MAS_MEM[3]
	S += DY6_mem0 <= DY6

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	DY6_mem1 += MAIN_MEM_r
	S += DY6_mem1 <= DY6

	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	k3_2_Z14_in += alt(MM_in)
	k3_2_Z14 = S.Task('k3_2_Z14', length=5, delay_cost=1)
	k3_2_Z14 += alt(MM)
	S += k3_2_Z14>=k3_2_Z14_in

	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	k3_2_Z14_mem0 += MAIN_MEM_r
	S += k3_2_Z14_mem0 <= k3_2_Z14

	k3_2_Z14_mem1 = S.Task('k3_2_Z14_mem1', length=1, delay_cost=1)
	k3_2_Z14_mem1 += alt(MM_MEM)
	S += (Z_exp14*MM[0])-1 < k3_2_Z14_mem1*MM_MEM[0]
	S += k3_2_Z14_mem1 <= k3_2_Z14

	Z_exp16_in = S.Task('Z_exp16_in', length=1, delay_cost=1)
	Z_exp16_in += alt(MM_in)
	Z_exp16 = S.Task('Z_exp16', length=5, delay_cost=1)
	Z_exp16 += alt(MM)
	S += Z_exp16>=Z_exp16_in

	Z_exp16_mem0 = S.Task('Z_exp16_mem0', length=1, delay_cost=1)
	Z_exp16_mem0 += alt(MM_MEM)
	S += (Z_exp15*MM[0])-1 < Z_exp16_mem0*MM_MEM[0]
	S += Z_exp16_mem0 <= Z_exp16

	Z_exp16_mem1 = S.Task('Z_exp16_mem1', length=1, delay_cost=1)
	Z_exp16_mem1 += MAIN_MEM_r
	S += Z_exp16_mem1 <= Z_exp16

	NX7_in = S.Task('NX7_in', length=1, delay_cost=1)
	NX7_in += alt(MM_in)
	NX7 = S.Task('NX7', length=5, delay_cost=1)
	NX7 += alt(MM)
	S += NX7>=NX7_in

	NX7_mem0 = S.Task('NX7_mem0', length=1, delay_cost=1)
	NX7_mem0 += alt(MAS_MEM)
	S += (NX7_*MAS[0])-1 < NX7_mem0*MAS_MEM[0]
	S += (NX7_*MAS[1])-1 < NX7_mem0*MAS_MEM[1]
	S += (NX7_*MAS[2])-1 < NX7_mem0*MAS_MEM[2]
	S += (NX7_*MAS[3])-1 < NX7_mem0*MAS_MEM[3]
	S += NX7_mem0 <= NX7

	NX7_mem1 = S.Task('NX7_mem1', length=1, delay_cost=1)
	NX7_mem1 += MAIN_MEM_r
	S += NX7_mem1 <= NX7

	DX7_ = S.Task('DX7_', length=1, delay_cost=1)
	DX7_ += alt(MAS)

	DX7__mem0 = S.Task('DX7__mem0', length=1, delay_cost=1)
	DX7__mem0 += alt(MM_MEM)
	S += (DX6*MM[0])-1 < DX7__mem0*MM_MEM[0]
	S += DX7__mem0 <= DX7_

	DX7__mem1 = S.Task('DX7__mem1', length=1, delay_cost=1)
	DX7__mem1 += MM_MEM[0]
	S += 72 < DX7__mem1
	S += DX7__mem1 <= DX7_

	NY7_in = S.Task('NY7_in', length=1, delay_cost=1)
	NY7_in += alt(MM_in)
	NY7 = S.Task('NY7', length=5, delay_cost=1)
	NY7 += alt(MM)
	S += NY7>=NY7_in

	NY7_mem0 = S.Task('NY7_mem0', length=1, delay_cost=1)
	NY7_mem0 += alt(MAS_MEM)
	S += (NY7_*MAS[0])-1 < NY7_mem0*MAS_MEM[0]
	S += (NY7_*MAS[1])-1 < NY7_mem0*MAS_MEM[1]
	S += (NY7_*MAS[2])-1 < NY7_mem0*MAS_MEM[2]
	S += (NY7_*MAS[3])-1 < NY7_mem0*MAS_MEM[3]
	S += NY7_mem0 <= NY7

	NY7_mem1 = S.Task('NY7_mem1', length=1, delay_cost=1)
	NY7_mem1 += MAIN_MEM_r
	S += NY7_mem1 <= NY7

	k2_0_Z15_in = S.Task('k2_0_Z15_in', length=1, delay_cost=1)
	k2_0_Z15_in += alt(MM_in)
	k2_0_Z15 = S.Task('k2_0_Z15', length=5, delay_cost=1)
	k2_0_Z15 += alt(MM)
	S += k2_0_Z15>=k2_0_Z15_in

	k2_0_Z15_mem0 = S.Task('k2_0_Z15_mem0', length=1, delay_cost=1)
	k2_0_Z15_mem0 += MAIN_MEM_r
	S += k2_0_Z15_mem0 <= k2_0_Z15

	k2_0_Z15_mem1 = S.Task('k2_0_Z15_mem1', length=1, delay_cost=1)
	k2_0_Z15_mem1 += alt(MM_MEM)
	S += (Z_exp15*MM[0])-1 < k2_0_Z15_mem1*MM_MEM[0]
	S += k2_0_Z15_mem1 <= k2_0_Z15

	DY7_ = S.Task('DY7_', length=1, delay_cost=1)
	DY7_ += alt(MAS)

	DY7__mem0 = S.Task('DY7__mem0', length=1, delay_cost=1)
	DY7__mem0 += alt(MM_MEM)
	S += (DY6*MM[0])-1 < DY7__mem0*MM_MEM[0]
	S += DY7__mem0 <= DY7_

	DY7__mem1 = S.Task('DY7__mem1', length=1, delay_cost=1)
	DY7__mem1 += MM_MEM[0]
	S += 70 < DY7__mem1
	S += DY7__mem1 <= DY7_

	k3_1_Z15_in = S.Task('k3_1_Z15_in', length=1, delay_cost=1)
	k3_1_Z15_in += alt(MM_in)
	k3_1_Z15 = S.Task('k3_1_Z15', length=5, delay_cost=1)
	k3_1_Z15 += alt(MM)
	S += k3_1_Z15>=k3_1_Z15_in

	k3_1_Z15_mem0 = S.Task('k3_1_Z15_mem0', length=1, delay_cost=1)
	k3_1_Z15_mem0 += MAIN_MEM_r
	S += k3_1_Z15_mem0 <= k3_1_Z15

	k3_1_Z15_mem1 = S.Task('k3_1_Z15_mem1', length=1, delay_cost=1)
	k3_1_Z15_mem1 += alt(MM_MEM)
	S += (Z_exp15*MM[0])-1 < k3_1_Z15_mem1*MM_MEM[0]
	S += k3_1_Z15_mem1 <= k3_1_Z15

	NX8_ = S.Task('NX8_', length=1, delay_cost=1)
	NX8_ += alt(MAS)

	NX8__mem0 = S.Task('NX8__mem0', length=1, delay_cost=1)
	NX8__mem0 += alt(MM_MEM)
	S += (NX7*MM[0])-1 < NX8__mem0*MM_MEM[0]
	S += NX8__mem0 <= NX8_

	NX8__mem1 = S.Task('NX8__mem1', length=1, delay_cost=1)
	NX8__mem1 += MM_MEM[0]
	S += 63 < NX8__mem1
	S += NX8__mem1 <= NX8_

	DX7_in = S.Task('DX7_in', length=1, delay_cost=1)
	DX7_in += alt(MM_in)
	DX7 = S.Task('DX7', length=5, delay_cost=1)
	DX7 += alt(MM)
	S += DX7>=DX7_in

	DX7_mem0 = S.Task('DX7_mem0', length=1, delay_cost=1)
	DX7_mem0 += alt(MAS_MEM)
	S += (DX7_*MAS[0])-1 < DX7_mem0*MAS_MEM[0]
	S += (DX7_*MAS[1])-1 < DX7_mem0*MAS_MEM[1]
	S += (DX7_*MAS[2])-1 < DX7_mem0*MAS_MEM[2]
	S += (DX7_*MAS[3])-1 < DX7_mem0*MAS_MEM[3]
	S += DX7_mem0 <= DX7

	DX7_mem1 = S.Task('DX7_mem1', length=1, delay_cost=1)
	DX7_mem1 += MAIN_MEM_r
	S += DX7_mem1 <= DX7

	NY8_ = S.Task('NY8_', length=1, delay_cost=1)
	NY8_ += alt(MAS)

	NY8__mem0 = S.Task('NY8__mem0', length=1, delay_cost=1)
	NY8__mem0 += alt(MM_MEM)
	S += (NY7*MM[0])-1 < NY8__mem0*MM_MEM[0]
	S += NY8__mem0 <= NY8_

	NY8__mem1 = S.Task('NY8__mem1', length=1, delay_cost=1)
	NY8__mem1 += MM_MEM[0]
	S += 69 < NY8__mem1
	S += NY8__mem1 <= NY8_

	DY7_in = S.Task('DY7_in', length=1, delay_cost=1)
	DY7_in += alt(MM_in)
	DY7 = S.Task('DY7', length=5, delay_cost=1)
	DY7 += alt(MM)
	S += DY7>=DY7_in

	DY7_mem0 = S.Task('DY7_mem0', length=1, delay_cost=1)
	DY7_mem0 += alt(MAS_MEM)
	S += (DY7_*MAS[0])-1 < DY7_mem0*MAS_MEM[0]
	S += (DY7_*MAS[1])-1 < DY7_mem0*MAS_MEM[1]
	S += (DY7_*MAS[2])-1 < DY7_mem0*MAS_MEM[2]
	S += (DY7_*MAS[3])-1 < DY7_mem0*MAS_MEM[3]
	S += DY7_mem0 <= DY7

	DY7_mem1 = S.Task('DY7_mem1', length=1, delay_cost=1)
	DY7_mem1 += MAIN_MEM_r
	S += DY7_mem1 <= DY7

	k3_0_Z16_in = S.Task('k3_0_Z16_in', length=1, delay_cost=1)
	k3_0_Z16_in += alt(MM_in)
	k3_0_Z16 = S.Task('k3_0_Z16', length=5, delay_cost=1)
	k3_0_Z16 += alt(MM)
	S += k3_0_Z16>=k3_0_Z16_in

	k3_0_Z16_mem0 = S.Task('k3_0_Z16_mem0', length=1, delay_cost=1)
	k3_0_Z16_mem0 += MAIN_MEM_r
	S += k3_0_Z16_mem0 <= k3_0_Z16

	k3_0_Z16_mem1 = S.Task('k3_0_Z16_mem1', length=1, delay_cost=1)
	k3_0_Z16_mem1 += alt(MM_MEM)
	S += (Z_exp16*MM[0])-1 < k3_0_Z16_mem1*MM_MEM[0]
	S += k3_0_Z16_mem1 <= k3_0_Z16

	NX8_in = S.Task('NX8_in', length=1, delay_cost=1)
	NX8_in += alt(MM_in)
	NX8 = S.Task('NX8', length=5, delay_cost=1)
	NX8 += alt(MM)
	S += NX8>=NX8_in

	NX8_mem0 = S.Task('NX8_mem0', length=1, delay_cost=1)
	NX8_mem0 += alt(MAS_MEM)
	S += (NX8_*MAS[0])-1 < NX8_mem0*MAS_MEM[0]
	S += (NX8_*MAS[1])-1 < NX8_mem0*MAS_MEM[1]
	S += (NX8_*MAS[2])-1 < NX8_mem0*MAS_MEM[2]
	S += (NX8_*MAS[3])-1 < NX8_mem0*MAS_MEM[3]
	S += NX8_mem0 <= NX8

	NX8_mem1 = S.Task('NX8_mem1', length=1, delay_cost=1)
	NX8_mem1 += MAIN_MEM_r
	S += NX8_mem1 <= NX8

	DX8_ = S.Task('DX8_', length=1, delay_cost=1)
	DX8_ += alt(MAS)

	DX8__mem0 = S.Task('DX8__mem0', length=1, delay_cost=1)
	DX8__mem0 += alt(MM_MEM)
	S += (DX7*MM[0])-1 < DX8__mem0*MM_MEM[0]
	S += DX8__mem0 <= DX8_

	DX8__mem1 = S.Task('DX8__mem1', length=1, delay_cost=1)
	DX8__mem1 += MM_MEM[0]
	S += 76 < DX8__mem1
	S += DX8__mem1 <= DX8_

	NY8_in = S.Task('NY8_in', length=1, delay_cost=1)
	NY8_in += alt(MM_in)
	NY8 = S.Task('NY8', length=5, delay_cost=1)
	NY8 += alt(MM)
	S += NY8>=NY8_in

	NY8_mem0 = S.Task('NY8_mem0', length=1, delay_cost=1)
	NY8_mem0 += alt(MAS_MEM)
	S += (NY8_*MAS[0])-1 < NY8_mem0*MAS_MEM[0]
	S += (NY8_*MAS[1])-1 < NY8_mem0*MAS_MEM[1]
	S += (NY8_*MAS[2])-1 < NY8_mem0*MAS_MEM[2]
	S += (NY8_*MAS[3])-1 < NY8_mem0*MAS_MEM[3]
	S += NY8_mem0 <= NY8

	NY8_mem1 = S.Task('NY8_mem1', length=1, delay_cost=1)
	NY8_mem1 += MAIN_MEM_r
	S += NY8_mem1 <= NY8

	DY8_ = S.Task('DY8_', length=1, delay_cost=1)
	DY8_ += alt(MAS)

	DY8__mem0 = S.Task('DY8__mem0', length=1, delay_cost=1)
	DY8__mem0 += alt(MM_MEM)
	S += (DY7*MM[0])-1 < DY8__mem0*MM_MEM[0]
	S += DY8__mem0 <= DY8_

	DY8__mem1 = S.Task('DY8__mem1', length=1, delay_cost=1)
	DY8__mem1 += MM_MEM[0]
	S += 61 < DY8__mem1
	S += DY8__mem1 <= DY8_

	NX9_ = S.Task('NX9_', length=1, delay_cost=1)
	NX9_ += alt(MAS)

	NX9__mem0 = S.Task('NX9__mem0', length=1, delay_cost=1)
	NX9__mem0 += alt(MM_MEM)
	S += (NX8*MM[0])-1 < NX9__mem0*MM_MEM[0]
	S += NX9__mem0 <= NX9_

	NX9__mem1 = S.Task('NX9__mem1', length=1, delay_cost=1)
	NX9__mem1 += MM_MEM[0]
	S += 64 < NX9__mem1
	S += NX9__mem1 <= NX9_

	DX8_in = S.Task('DX8_in', length=1, delay_cost=1)
	DX8_in += alt(MM_in)
	DX8 = S.Task('DX8', length=5, delay_cost=1)
	DX8 += alt(MM)
	S += DX8>=DX8_in

	DX8_mem0 = S.Task('DX8_mem0', length=1, delay_cost=1)
	DX8_mem0 += alt(MAS_MEM)
	S += (DX8_*MAS[0])-1 < DX8_mem0*MAS_MEM[0]
	S += (DX8_*MAS[1])-1 < DX8_mem0*MAS_MEM[1]
	S += (DX8_*MAS[2])-1 < DX8_mem0*MAS_MEM[2]
	S += (DX8_*MAS[3])-1 < DX8_mem0*MAS_MEM[3]
	S += DX8_mem0 <= DX8

	DX8_mem1 = S.Task('DX8_mem1', length=1, delay_cost=1)
	DX8_mem1 += MAIN_MEM_r
	S += DX8_mem1 <= DX8

	NY9_ = S.Task('NY9_', length=1, delay_cost=1)
	NY9_ += alt(MAS)

	NY9__mem0 = S.Task('NY9__mem0', length=1, delay_cost=1)
	NY9__mem0 += alt(MM_MEM)
	S += (NY8*MM[0])-1 < NY9__mem0*MM_MEM[0]
	S += NY9__mem0 <= NY9_

	NY9__mem1 = S.Task('NY9__mem1', length=1, delay_cost=1)
	NY9__mem1 += MM_MEM[0]
	S += 58 < NY9__mem1
	S += NY9__mem1 <= NY9_

	DY8_in = S.Task('DY8_in', length=1, delay_cost=1)
	DY8_in += alt(MM_in)
	DY8 = S.Task('DY8', length=5, delay_cost=1)
	DY8 += alt(MM)
	S += DY8>=DY8_in

	DY8_mem0 = S.Task('DY8_mem0', length=1, delay_cost=1)
	DY8_mem0 += alt(MAS_MEM)
	S += (DY8_*MAS[0])-1 < DY8_mem0*MAS_MEM[0]
	S += (DY8_*MAS[1])-1 < DY8_mem0*MAS_MEM[1]
	S += (DY8_*MAS[2])-1 < DY8_mem0*MAS_MEM[2]
	S += (DY8_*MAS[3])-1 < DY8_mem0*MAS_MEM[3]
	S += DY8_mem0 <= DY8

	DY8_mem1 = S.Task('DY8_mem1', length=1, delay_cost=1)
	DY8_mem1 += MAIN_MEM_r
	S += DY8_mem1 <= DY8

	NX9_in = S.Task('NX9_in', length=1, delay_cost=1)
	NX9_in += alt(MM_in)
	NX9 = S.Task('NX9', length=5, delay_cost=1)
	NX9 += alt(MM)
	S += NX9>=NX9_in

	NX9_mem0 = S.Task('NX9_mem0', length=1, delay_cost=1)
	NX9_mem0 += alt(MAS_MEM)
	S += (NX9_*MAS[0])-1 < NX9_mem0*MAS_MEM[0]
	S += (NX9_*MAS[1])-1 < NX9_mem0*MAS_MEM[1]
	S += (NX9_*MAS[2])-1 < NX9_mem0*MAS_MEM[2]
	S += (NX9_*MAS[3])-1 < NX9_mem0*MAS_MEM[3]
	S += NX9_mem0 <= NX9

	NX9_mem1 = S.Task('NX9_mem1', length=1, delay_cost=1)
	NX9_mem1 += MAIN_MEM_r
	S += NX9_mem1 <= NX9

	DX9_ = S.Task('DX9_', length=1, delay_cost=1)
	DX9_ += alt(MAS)

	DX9__mem0 = S.Task('DX9__mem0', length=1, delay_cost=1)
	DX9__mem0 += alt(MM_MEM)
	S += (DX8*MM[0])-1 < DX9__mem0*MM_MEM[0]
	S += DX9__mem0 <= DX9_

	DX9__mem1 = S.Task('DX9__mem1', length=1, delay_cost=1)
	DX9__mem1 += MM_MEM[0]
	S += 67 < DX9__mem1
	S += DX9__mem1 <= DX9_

	NY9_in = S.Task('NY9_in', length=1, delay_cost=1)
	NY9_in += alt(MM_in)
	NY9 = S.Task('NY9', length=5, delay_cost=1)
	NY9 += alt(MM)
	S += NY9>=NY9_in

	NY9_mem0 = S.Task('NY9_mem0', length=1, delay_cost=1)
	NY9_mem0 += alt(MAS_MEM)
	S += (NY9_*MAS[0])-1 < NY9_mem0*MAS_MEM[0]
	S += (NY9_*MAS[1])-1 < NY9_mem0*MAS_MEM[1]
	S += (NY9_*MAS[2])-1 < NY9_mem0*MAS_MEM[2]
	S += (NY9_*MAS[3])-1 < NY9_mem0*MAS_MEM[3]
	S += NY9_mem0 <= NY9

	NY9_mem1 = S.Task('NY9_mem1', length=1, delay_cost=1)
	NY9_mem1 += MAIN_MEM_r
	S += NY9_mem1 <= NY9

	DY9_ = S.Task('DY9_', length=1, delay_cost=1)
	DY9_ += alt(MAS)

	DY9__mem0 = S.Task('DY9__mem0', length=1, delay_cost=1)
	DY9__mem0 += alt(MM_MEM)
	S += (DY8*MM[0])-1 < DY9__mem0*MM_MEM[0]
	S += DY9__mem0 <= DY9_

	DY9__mem1 = S.Task('DY9__mem1', length=1, delay_cost=1)
	DY9__mem1 += MM_MEM[0]
	S += 65 < DY9__mem1
	S += DY9__mem1 <= DY9_

	NX10_ = S.Task('NX10_', length=1, delay_cost=1)
	NX10_ += alt(MAS)

	NX10__mem0 = S.Task('NX10__mem0', length=1, delay_cost=1)
	NX10__mem0 += alt(MM_MEM)
	S += (NX9*MM[0])-1 < NX10__mem0*MM_MEM[0]
	S += NX10__mem0 <= NX10_

	NX10__mem1 = S.Task('NX10__mem1', length=1, delay_cost=1)
	NX10__mem1 += MM_MEM[0]
	S += 78 < NX10__mem1
	S += NX10__mem1 <= NX10_

	DX9_in = S.Task('DX9_in', length=1, delay_cost=1)
	DX9_in += alt(MM_in)
	DX9 = S.Task('DX9', length=5, delay_cost=1)
	DX9 += alt(MM)
	S += DX9>=DX9_in

	DX9_mem0 = S.Task('DX9_mem0', length=1, delay_cost=1)
	DX9_mem0 += alt(MAS_MEM)
	S += (DX9_*MAS[0])-1 < DX9_mem0*MAS_MEM[0]
	S += (DX9_*MAS[1])-1 < DX9_mem0*MAS_MEM[1]
	S += (DX9_*MAS[2])-1 < DX9_mem0*MAS_MEM[2]
	S += (DX9_*MAS[3])-1 < DX9_mem0*MAS_MEM[3]
	S += DX9_mem0 <= DX9

	DX9_mem1 = S.Task('DX9_mem1', length=1, delay_cost=1)
	DX9_mem1 += MAIN_MEM_r
	S += DX9_mem1 <= DX9

	NY10_ = S.Task('NY10_', length=1, delay_cost=1)
	NY10_ += alt(MAS)

	NY10__mem0 = S.Task('NY10__mem0', length=1, delay_cost=1)
	NY10__mem0 += alt(MM_MEM)
	S += (NY9*MM[0])-1 < NY10__mem0*MM_MEM[0]
	S += NY10__mem0 <= NY10_

	NY10__mem1 = S.Task('NY10__mem1', length=1, delay_cost=1)
	NY10__mem1 += MM_MEM[0]
	S += 68 < NY10__mem1
	S += NY10__mem1 <= NY10_

	DY9_in = S.Task('DY9_in', length=1, delay_cost=1)
	DY9_in += alt(MM_in)
	DY9 = S.Task('DY9', length=5, delay_cost=1)
	DY9 += alt(MM)
	S += DY9>=DY9_in

	DY9_mem0 = S.Task('DY9_mem0', length=1, delay_cost=1)
	DY9_mem0 += alt(MAS_MEM)
	S += (DY9_*MAS[0])-1 < DY9_mem0*MAS_MEM[0]
	S += (DY9_*MAS[1])-1 < DY9_mem0*MAS_MEM[1]
	S += (DY9_*MAS[2])-1 < DY9_mem0*MAS_MEM[2]
	S += (DY9_*MAS[3])-1 < DY9_mem0*MAS_MEM[3]
	S += DY9_mem0 <= DY9

	DY9_mem1 = S.Task('DY9_mem1', length=1, delay_cost=1)
	DY9_mem1 += MAIN_MEM_r
	S += DY9_mem1 <= DY9

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/ISOGENY/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

