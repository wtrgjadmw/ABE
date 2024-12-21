from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 187
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 0
	DY0_mem1 += MAIN_MEM_r[1]

	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 0
	Z_exp2_in += MM_in[0]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 0
	k2_14_Z1_mem0 += MAIN_MEM_r[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 1
	DY0_mem0 += MAIN_MEM_r[0]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 1
	NX1_mem1 += MAIN_MEM_r[1]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 1
	NY0_in += MM_in[0]

	Z_exp2 = S.Task('Z_exp2', length=6, delay_cost=1)
	S += Z_exp2 >= 1
	Z_exp2 += MM[0]

	NY0 = S.Task('NY0', length=6, delay_cost=1)
	S += NY0 >= 2
	NY0 += MM[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 2
	k0_10_Z1_mem0 += MAIN_MEM_r[0]

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 2
	k0_10_Z1_mem1 += MAIN_MEM_r[1]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 2
	k2_14_Z1_in += MM_in[0]

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 3
	NY0_mem1 += MAIN_MEM_r[1]

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 3
	k0_10_Z1_in += MM_in[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 3
	k1_8_Z3_mem0 += MAIN_MEM_r[0]

	k2_14_Z1 = S.Task('k2_14_Z1', length=6, delay_cost=1)
	S += k2_14_Z1 >= 3
	k2_14_Z1 += MM[0]

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 4
	NX0_in += MM_in[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 4
	Z_exp4_mem1 += MAIN_MEM_r[1]

	k0_10_Z1 = S.Task('k0_10_Z1', length=6, delay_cost=1)
	S += k0_10_Z1 >= 4
	k0_10_Z1 += MM[0]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 4
	k2_13_Z2_mem0 += MAIN_MEM_r[0]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 5
	DX0_in += MM_in[0]

	NX0 = S.Task('NX0', length=6, delay_cost=1)
	S += NX0 >= 5
	NX0 += MM[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 5
	k0_9_Z2_mem0 += MAIN_MEM_r[0]

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 5
	k2_14_Z1_mem1 += MAIN_MEM_r[1]

	DX0 = S.Task('DX0', length=6, delay_cost=1)
	S += DX0 >= 6
	DX0 += MM[0]

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 6
	DX0_mem1 += MAIN_MEM_r[1]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 6
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 6
	k1_9_Z2_mem1 += MM_MEM[1]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 6
	k3_14_Z2_mem0 += MAIN_MEM_r[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 7
	Z_exp3_mem1 += MAIN_MEM_r[1]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 7
	k0_8_Z3_mem0 += MAIN_MEM_r[0]

	k1_9_Z2 = S.Task('k1_9_Z2', length=6, delay_cost=1)
	S += k1_9_Z2 >= 7
	k1_9_Z2 += MM[0]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 7
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 7
	k3_14_Z2_mem1 += MM_MEM[1]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 8
	DX0_mem0 += MAIN_MEM_r[0]

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 8
	DY0_in += MM_in[0]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 8
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 8
	NY1__mem1 += MM_MEM[1]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 8
	NY1_mem1 += MAIN_MEM_r[1]

	k3_14_Z2 = S.Task('k3_14_Z2', length=6, delay_cost=1)
	S += k3_14_Z2 >= 8
	k3_14_Z2 += MM[0]

	DY0 = S.Task('DY0', length=6, delay_cost=1)
	S += DY0 >= 9
	DY0 += MM[0]

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 9
	NX0_mem1 += MAIN_MEM_r[1]

	NY1_ = S.Task('NY1_', length=1, delay_cost=1)
	S += NY1_ >= 9
	NY1_ += MAS[3]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 9
	Z_exp2_mem0 += MAIN_MEM_r[0]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 9
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 9
	Z_exp3_mem0 += MM_MEM[0]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 10
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 10
	NX1__mem1 += MM_MEM[1]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 10
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 10
	NY1_mem0 += MAS_MEM[6]

	Z_exp3 = S.Task('Z_exp3', length=6, delay_cost=1)
	S += Z_exp3 >= 10
	Z_exp3 += MM[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 10
	Z_exp5_mem1 += MAIN_MEM_r[1]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 10
	k3_13_Z3_mem0 += MAIN_MEM_r[0]

	NX1_ = S.Task('NX1_', length=1, delay_cost=1)
	S += NX1_ >= 11
	NX1_ += MAS[3]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 11
	NY0_mem0 += MAIN_MEM_r[0]

	NY1 = S.Task('NY1', length=6, delay_cost=1)
	S += NY1 >= 11
	NY1 += MM[0]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 11
	NY3_mem1 += MAIN_MEM_r[1]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 11
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 11
	k0_9_Z2_mem1 += MM_MEM[1]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 12
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 12
	DX1__mem1 += MM_MEM[1]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 12
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 12
	NX1_mem0 += MAS_MEM[6]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 12
	NY2_mem1 += MAIN_MEM_r[1]

	k0_9_Z2 = S.Task('k0_9_Z2', length=6, delay_cost=1)
	S += k0_9_Z2 >= 12
	k0_9_Z2 += MM[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 12
	k1_9_Z2_mem0 += MAIN_MEM_r[0]

	DX1_ = S.Task('DX1_', length=1, delay_cost=1)
	S += DX1_ >= 13
	DX1_ += MAS[3]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 13
	NX0_mem0 += MAIN_MEM_r[0]

	NX1 = S.Task('NX1', length=6, delay_cost=1)
	S += NX1 >= 13
	NX1 += MM[0]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 13
	NX3_mem1 += MAIN_MEM_r[1]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 13
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 13
	k2_13_Z2_mem1 += MM_MEM[1]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 14
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 14
	DX1_mem0 += MAS_MEM[6]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 14
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 14
	DY1__mem1 += MM_MEM[1]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 14
	NX2_mem1 += MAIN_MEM_r[1]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 14
	k2_12_Z3_mem0 += MAIN_MEM_r[0]

	k2_13_Z2 = S.Task('k2_13_Z2', length=6, delay_cost=1)
	S += k2_13_Z2 >= 14
	k2_13_Z2 += MM[0]

	DX1 = S.Task('DX1', length=6, delay_cost=1)
	S += DX1 >= 15
	DX1 += MM[0]

	DY1_ = S.Task('DY1_', length=1, delay_cost=1)
	S += DY1_ >= 15
	DY1_ += MAS[3]

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	S += DY3_mem1 >= 15
	DY3_mem1 += MAIN_MEM_r[1]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 15
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 15
	Z_exp4_mem0 += MM_MEM[0]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 15
	k3_8_Z8_mem0 += MAIN_MEM_r[0]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 16
	DY2_mem1 += MAIN_MEM_r[1]

	Z_exp4 = S.Task('Z_exp4', length=6, delay_cost=1)
	S += Z_exp4 >= 16
	Z_exp4 += MM[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 16
	k1_6_Z5_mem0 += MAIN_MEM_r[0]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 16
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 16
	k1_8_Z3_mem1 += MM_MEM[1]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 17
	DY1_mem1 += MAIN_MEM_r[1]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 17
	k1_5_Z6_mem0 += MAIN_MEM_r[0]

	k1_8_Z3 = S.Task('k1_8_Z3', length=6, delay_cost=1)
	S += k1_8_Z3 >= 17
	k1_8_Z3 += MM[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 17
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 17
	k3_13_Z3_mem1 += MM_MEM[1]

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	S += DX3_mem1 >= 18
	DX3_mem1 += MAIN_MEM_r[1]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 18
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 18
	k0_8_Z3_mem1 += MM_MEM[1]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 18
	k3_10_Z6_mem0 += MAIN_MEM_r[0]

	k3_13_Z3 = S.Task('k3_13_Z3', length=6, delay_cost=1)
	S += k3_13_Z3 >= 18
	k3_13_Z3 += MM[0]

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	S += Z_exp6_mem1 >= 19
	Z_exp6_mem1 += MAIN_MEM_r[1]

	k0_8_Z3 = S.Task('k0_8_Z3', length=6, delay_cost=1)
	S += k0_8_Z3 >= 19
	k0_8_Z3 += MM[0]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 19
	k1_3_Z8_mem0 += MAIN_MEM_r[0]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 19
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 19
	k2_12_Z3_mem1 += MM_MEM[1]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 20
	DX2_mem1 += MAIN_MEM_r[1]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 20
	DY1_in += MM_in[0]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 20
	DY1_mem0 += MAS_MEM[6]

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 20
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 20
	NY2__mem1 += MM_MEM[1]

	k2_12_Z3 = S.Task('k2_12_Z3', length=6, delay_cost=1)
	S += k2_12_Z3 >= 20
	k2_12_Z3 += MM[0]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 20
	k3_9_Z7_mem0 += MAIN_MEM_r[0]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 21
	DX1_mem1 += MAIN_MEM_r[1]

	DY1 = S.Task('DY1', length=6, delay_cost=1)
	S += DY1 >= 21
	DY1 += MM[0]

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 21
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 21
	NX2__mem1 += MM_MEM[1]

	NY2_ = S.Task('NY2_', length=1, delay_cost=1)
	S += NY2_ >= 21
	NY2_ += MAS[0]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 21
	NY2_in += MM_in[0]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 21
	NY2_mem0 += MAS_MEM[0]

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	S += k2_8_Z7_mem0 >= 21
	k2_8_Z7_mem0 += MAIN_MEM_r[0]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 22
	DX2__mem0 += MM_MEM[0]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 22
	DX2__mem1 += MM_MEM[1]

	NX2_ = S.Task('NX2_', length=1, delay_cost=1)
	S += NX2_ >= 22
	NX2_ += MAS[3]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 22
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 22
	NX2_mem0 += MAS_MEM[6]

	NY2 = S.Task('NY2', length=6, delay_cost=1)
	S += NY2 >= 22
	NY2 += MM[0]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 22
	Z_exp7_mem1 += MAIN_MEM_r[1]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 22
	k0_7_Z4_mem0 += MAIN_MEM_r[0]

	DX2_ = S.Task('DX2_', length=1, delay_cost=1)
	S += DX2_ >= 23
	DX2_ += MAS[0]

	NX2 = S.Task('NX2', length=6, delay_cost=1)
	S += NX2 >= 23
	NX2 += MM[0]

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	S += Z_exp8_mem1 >= 23
	Z_exp8_mem1 += MAIN_MEM_r[1]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 23
	k0_6_Z5_mem0 += MAIN_MEM_r[0]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 23
	k1_7_Z4_in += MM_in[0]

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 23
	k1_7_Z4_mem1 += MM_MEM[1]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 24
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 24
	Z_exp5_mem0 += MM_MEM[0]

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	S += Z_exp9_mem1 >= 24
	Z_exp9_mem1 += MAIN_MEM_r[1]

	k1_7_Z4 = S.Task('k1_7_Z4', length=6, delay_cost=1)
	S += k1_7_Z4 >= 24
	k1_7_Z4 += MM[0]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 24
	k2_10_Z5_mem0 += MAIN_MEM_r[0]

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	S += DX6_mem1 >= 25
	DX6_mem1 += MAIN_MEM_r[1]

	Z_exp5 = S.Task('Z_exp5', length=6, delay_cost=1)
	S += Z_exp5 >= 25
	Z_exp5 += MM[0]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 25
	k1_4_Z7_mem0 += MAIN_MEM_r[0]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 25
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 25
	k3_12_Z4_mem1 += MM_MEM[1]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 26
	DX2_in += MM_in[0]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 26
	DX2_mem0 += MAS_MEM[0]

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 26
	DY2__mem0 += MM_MEM[0]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 26
	DY2__mem1 += MM_MEM[1]

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	S += Z_exp13_mem1 >= 26
	Z_exp13_mem1 += MAIN_MEM_r[1]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 26
	k0_5_Z6_mem0 += MAIN_MEM_r[0]

	k3_12_Z4 = S.Task('k3_12_Z4', length=6, delay_cost=1)
	S += k3_12_Z4 >= 26
	k3_12_Z4 += MM[0]

	DX2 = S.Task('DX2', length=6, delay_cost=1)
	S += DX2 >= 27
	DX2 += MM[0]

	DY2_ = S.Task('DY2_', length=1, delay_cost=1)
	S += DY2_ >= 27
	DY2_ += MAS[1]

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 27
	DY2_in += MM_in[0]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 27
	DY2_mem0 += MAS_MEM[2]

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 27
	NY3__mem0 += MM_MEM[0]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 27
	NY3__mem1 += MM_MEM[1]

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	S += NY6_mem1 >= 27
	NY6_mem1 += MAIN_MEM_r[1]

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	S += k0_4_Z7_mem0 >= 27
	k0_4_Z7_mem0 += MAIN_MEM_r[0]

	DY2 = S.Task('DY2', length=6, delay_cost=1)
	S += DY2 >= 28
	DY2 += MM[0]

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 28
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 28
	NX3__mem1 += MM_MEM[1]

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	S += NX4_mem1 >= 28
	NX4_mem1 += MAIN_MEM_r[1]

	NY3_ = S.Task('NY3_', length=1, delay_cost=1)
	S += NY3_ >= 28
	NY3_ += MAS[0]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 28
	NY3_in += MM_in[0]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 28
	NY3_mem0 += MAS_MEM[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 28
	k3_12_Z4_mem0 += MAIN_MEM_r[0]

	NX3_ = S.Task('NX3_', length=1, delay_cost=1)
	S += NX3_ >= 29
	NX3_ += MAS[0]

	NY3 = S.Task('NY3', length=6, delay_cost=1)
	S += NY3 >= 29
	NY3 += MM[0]

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	S += Z_exp10_mem1 >= 29
	Z_exp10_mem1 += MAIN_MEM_r[1]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 29
	k1_7_Z4_mem0 += MAIN_MEM_r[0]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 29
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 29
	k2_11_Z4_mem1 += MM_MEM[1]

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	S += DY4_mem1 >= 30
	DY4_mem1 += MAIN_MEM_r[1]

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	S += Z_exp6_in >= 30
	Z_exp6_in += MM_in[0]

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	S += Z_exp6_mem0 >= 30
	Z_exp6_mem0 += MM_MEM[0]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 30
	k0_3_Z8_mem0 += MAIN_MEM_r[0]

	k2_11_Z4 = S.Task('k2_11_Z4', length=6, delay_cost=1)
	S += k2_11_Z4 >= 30
	k2_11_Z4 += MM[0]

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	S += DX5_mem1 >= 31
	DX5_mem1 += MAIN_MEM_r[1]

	Z_exp6 = S.Task('Z_exp6', length=6, delay_cost=1)
	S += Z_exp6 >= 31
	Z_exp6 += MM[0]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 31
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 31
	k2_10_Z5_mem1 += MM_MEM[1]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 31
	k2_7_Z8_mem0 += MAIN_MEM_r[0]

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	S += DX3__mem0 >= 32
	DX3__mem0 += MM_MEM[0]

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	S += DX3__mem1 >= 32
	DX3__mem1 += MM_MEM[1]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 32
	NX3_in += MM_in[0]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 32
	NX3_mem0 += MAS_MEM[0]

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	S += Z_exp12_mem1 >= 32
	Z_exp12_mem1 += MAIN_MEM_r[1]

	k2_10_Z5 = S.Task('k2_10_Z5', length=6, delay_cost=1)
	S += k2_10_Z5 >= 32
	k2_10_Z5 += MM[0]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 32
	k2_11_Z4_mem0 += MAIN_MEM_r[0]

	DX3_ = S.Task('DX3_', length=1, delay_cost=1)
	S += DX3_ >= 33
	DX3_ += MAS[0]

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	S += DX3_in >= 33
	DX3_in += MM_in[0]

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	S += DX3_mem0 >= 33
	DX3_mem0 += MAS_MEM[0]

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	S += DY3__mem0 >= 33
	DY3__mem0 += MM_MEM[0]

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	S += DY3__mem1 >= 33
	DY3__mem1 += MM_MEM[1]

	NX3 = S.Task('NX3', length=6, delay_cost=1)
	S += NX3 >= 33
	NX3 += MM[0]

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	S += Z_exp15_mem1 >= 33
	Z_exp15_mem1 += MAIN_MEM_r[1]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 33
	k3_11_Z5_mem0 += MAIN_MEM_r[0]

	DX3 = S.Task('DX3', length=6, delay_cost=1)
	S += DX3 >= 34
	DX3 += MM[0]

	DY3_ = S.Task('DY3_', length=1, delay_cost=1)
	S += DY3_ >= 34
	DY3_ += MAS[3]

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	S += DY6_mem1 >= 34
	DY6_mem1 += MAIN_MEM_r[1]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 34
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 34
	k0_7_Z4_mem1 += MM_MEM[1]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 34
	k2_9_Z6_mem0 += MAIN_MEM_r[0]

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	S += DY3_in >= 35
	DY3_in += MM_in[0]

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	S += DY3_mem0 >= 35
	DY3_mem0 += MAS_MEM[6]

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 35
	NY4__mem0 += MM_MEM[0]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 35
	NY4__mem1 += MM_MEM[1]

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	S += NY5_mem1 >= 35
	NY5_mem1 += MAIN_MEM_r[1]

	k0_7_Z4 = S.Task('k0_7_Z4', length=6, delay_cost=1)
	S += k0_7_Z4 >= 35
	k0_7_Z4 += MM[0]

	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	S += k3_2_Z14_mem0 >= 35
	k3_2_Z14_mem0 += MAIN_MEM_r[0]

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	S += DX4_mem1 >= 36
	DX4_mem1 += MAIN_MEM_r[1]

	DY3 = S.Task('DY3', length=6, delay_cost=1)
	S += DY3 >= 36
	DY3 += MM[0]

	NY4_ = S.Task('NY4_', length=1, delay_cost=1)
	S += NY4_ >= 36
	NY4_ += MAS[3]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 36
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 36
	Z_exp7_mem0 += MM_MEM[0]

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	S += k1_1_Z10_mem0 >= 36
	k1_1_Z10_mem0 += MAIN_MEM_r[0]

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	S += NX6_mem1 >= 37
	NX6_mem1 += MAIN_MEM_r[1]

	Z_exp7 = S.Task('Z_exp7', length=6, delay_cost=1)
	S += Z_exp7 >= 37
	Z_exp7 += MM[0]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 37
	k1_5_Z6_in += MM_in[0]

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 37
	k1_5_Z6_mem1 += MM_MEM[1]

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	S += k2_5_Z10_mem0 >= 37
	k2_5_Z10_mem0 += MAIN_MEM_r[0]

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	S += NX5_mem1 >= 38
	NX5_mem1 += MAIN_MEM_r[1]

	k1_5_Z6 = S.Task('k1_5_Z6', length=6, delay_cost=1)
	S += k1_5_Z6 >= 38
	k1_5_Z6 += MM[0]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 38
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 38
	k3_11_Z5_mem1 += MM_MEM[1]

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	S += k3_7_Z9_mem0 >= 38
	k3_7_Z9_mem0 += MAIN_MEM_r[0]

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	S += DY5_mem1 >= 39
	DY5_mem1 += MAIN_MEM_r[1]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 39
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 39
	k1_6_Z5_mem1 += MM_MEM[1]

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	S += k2_6_Z9_mem0 >= 39
	k2_6_Z9_mem0 += MAIN_MEM_r[0]

	k3_11_Z5 = S.Task('k3_11_Z5', length=6, delay_cost=1)
	S += k3_11_Z5 >= 39
	k3_11_Z5 += MM[0]

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	S += NY4_mem1 >= 40
	NY4_mem1 += MAIN_MEM_r[1]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 40
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 40
	k0_5_Z6_mem1 += MM_MEM[1]

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	S += k1_0_Z11_mem0 >= 40
	k1_0_Z11_mem0 += MAIN_MEM_r[0]

	k1_6_Z5 = S.Task('k1_6_Z5', length=6, delay_cost=1)
	S += k1_6_Z5 >= 40
	k1_6_Z5 += MM[0]

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	S += Z_exp14_mem1 >= 41
	Z_exp14_mem1 += MAIN_MEM_r[1]

	k0_5_Z6 = S.Task('k0_5_Z6', length=6, delay_cost=1)
	S += k0_5_Z6 >= 41
	k0_5_Z6 += MM[0]

	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	S += k2_1_Z14_mem0 >= 41
	k2_1_Z14_mem0 += MAIN_MEM_r[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 41
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 41
	k3_10_Z6_mem1 += MM_MEM[1]

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	S += Z_exp11_mem1 >= 42
	Z_exp11_mem1 += MAIN_MEM_r[1]

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	S += Z_exp8_in >= 42
	Z_exp8_in += MM_in[0]

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	S += Z_exp8_mem0 >= 42
	Z_exp8_mem0 += MM_MEM[0]

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	S += k0_2_Z9_mem0 >= 42
	k0_2_Z9_mem0 += MAIN_MEM_r[0]

	k3_10_Z6 = S.Task('k3_10_Z6', length=6, delay_cost=1)
	S += k3_10_Z6 >= 42
	k3_10_Z6 += MM[0]

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 43
	NX4__mem0 += MM_MEM[0]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 43
	NX4__mem1 += MM_MEM[1]

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	S += NY4_in >= 43
	NY4_in += MM_in[0]

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	S += NY4_mem0 >= 43
	NY4_mem0 += MAS_MEM[6]

	Z_exp8 = S.Task('Z_exp8', length=6, delay_cost=1)
	S += Z_exp8 >= 43
	Z_exp8 += MM[0]

	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	S += k3_3_Z13_mem0 >= 43
	k3_3_Z13_mem0 += MAIN_MEM_r[0]

	NX4_ = S.Task('NX4_', length=1, delay_cost=1)
	S += NX4_ >= 44
	NX4_ += MAS[0]

	NY4 = S.Task('NY4', length=6, delay_cost=1)
	S += NY4 >= 44
	NY4 += MM[0]

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	S += k0_4_Z7_in >= 44
	k0_4_Z7_in += MM_in[0]

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	S += k0_4_Z7_mem1 >= 44
	k0_4_Z7_mem1 += MM_MEM[1]

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	S += k3_6_Z10_mem0 >= 44
	k3_6_Z10_mem0 += MAIN_MEM_r[0]

	k0_4_Z7 = S.Task('k0_4_Z7', length=6, delay_cost=1)
	S += k0_4_Z7 >= 45
	k0_4_Z7 += MM[0]

	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	S += k2_3_Z12_mem0 >= 45
	k2_3_Z12_mem0 += MAIN_MEM_r[0]

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	S += k2_8_Z7_in >= 45
	k2_8_Z7_in += MM_in[0]

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	S += k2_8_Z7_mem1 >= 45
	k2_8_Z7_mem1 += MM_MEM[1]

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	S += k0_0_Z11_mem0 >= 46
	k0_0_Z11_mem0 += MAIN_MEM_r[0]

	k2_8_Z7 = S.Task('k2_8_Z7', length=6, delay_cost=1)
	S += k2_8_Z7 >= 46
	k2_8_Z7 += MM[0]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 46
	k3_9_Z7_in += MM_in[0]

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 46
	k3_9_Z7_mem1 += MM_MEM[1]

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	S += k0_1_Z10_mem0 >= 47
	k0_1_Z10_mem0 += MAIN_MEM_r[0]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 47
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 47
	k2_9_Z6_mem1 += MM_MEM[1]

	k3_9_Z7 = S.Task('k3_9_Z7', length=6, delay_cost=1)
	S += k3_9_Z7 >= 47
	k3_9_Z7 += MM[0]

	k2_9_Z6 = S.Task('k2_9_Z6', length=6, delay_cost=1)
	S += k2_9_Z6 >= 48
	k2_9_Z6 += MM[0]

	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	S += k3_4_Z12_mem0 >= 48
	k3_4_Z12_mem0 += MAIN_MEM_r[0]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 48
	k3_8_Z8_in += MM_in[0]

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 48
	k3_8_Z8_mem1 += MM_MEM[1]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 49
	k0_3_Z8_in += MM_in[0]

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 49
	k0_3_Z8_mem1 += MM_MEM[1]

	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	S += k2_2_Z13_mem0 >= 49
	k2_2_Z13_mem0 += MAIN_MEM_r[0]

	k3_8_Z8 = S.Task('k3_8_Z8', length=6, delay_cost=1)
	S += k3_8_Z8 >= 49
	k3_8_Z8 += MM[0]

	k0_3_Z8 = S.Task('k0_3_Z8', length=6, delay_cost=1)
	S += k0_3_Z8 >= 50
	k0_3_Z8 += MM[0]

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	S += k1_2_Z9_mem0 >= 50
	k1_2_Z9_mem0 += MAIN_MEM_r[0]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 50
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 50
	k2_7_Z8_mem1 += MM_MEM[1]

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	S += Z_exp9_in >= 51
	Z_exp9_in += MM_in[0]

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	S += Z_exp9_mem0 >= 51
	Z_exp9_mem0 += MM_MEM[0]

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	S += k2_4_Z11_mem0 >= 51
	k2_4_Z11_mem0 += MAIN_MEM_r[0]

	k2_7_Z8 = S.Task('k2_7_Z8', length=6, delay_cost=1)
	S += k2_7_Z8 >= 51
	k2_7_Z8 += MM[0]

	Z_exp9 = S.Task('Z_exp9', length=6, delay_cost=1)
	S += Z_exp9 >= 52
	Z_exp9 += MM[0]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 52
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 52
	k1_3_Z8_mem1 += MM_MEM[1]

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	S += k3_5_Z11_mem0 >= 52
	k3_5_Z11_mem0 += MAIN_MEM_r[0]

	k1_3_Z8 = S.Task('k1_3_Z8', length=6, delay_cost=1)
	S += k1_3_Z8 >= 53
	k1_3_Z8 += MM[0]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 53
	k1_4_Z7_in += MM_in[0]

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 53
	k1_4_Z7_mem1 += MM_MEM[1]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 54
	k0_6_Z5_in += MM_in[0]

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 54
	k0_6_Z5_mem1 += MM_MEM[1]

	k1_4_Z7 = S.Task('k1_4_Z7', length=6, delay_cost=1)
	S += k1_4_Z7 >= 54
	k1_4_Z7 += MM[0]

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	S += DX4__mem0 >= 55
	DX4__mem0 += MM_MEM[0]

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	S += DX4__mem1 >= 55
	DX4__mem1 += MM_MEM[1]

	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	S += NX4_in >= 55
	NX4_in += MM_in[0]

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	S += NX4_mem0 >= 55
	NX4_mem0 += MAS_MEM[0]

	k0_6_Z5 = S.Task('k0_6_Z5', length=6, delay_cost=1)
	S += k0_6_Z5 >= 55
	k0_6_Z5 += MM[0]

	DX4_ = S.Task('DX4_', length=1, delay_cost=1)
	S += DX4_ >= 56
	DX4_ += MAS[0]

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	S += DX4_in >= 56
	DX4_in += MM_in[0]

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	S += DX4_mem0 >= 56
	DX4_mem0 += MAS_MEM[0]

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	S += DY4__mem0 >= 56
	DY4__mem0 += MM_MEM[0]

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	S += DY4__mem1 >= 56
	DY4__mem1 += MM_MEM[1]

	NX4 = S.Task('NX4', length=6, delay_cost=1)
	S += NX4 >= 56
	NX4 += MM[0]

	DX4 = S.Task('DX4', length=6, delay_cost=1)
	S += DX4 >= 57
	DX4 += MM[0]

	DY4_ = S.Task('DY4_', length=1, delay_cost=1)
	S += DY4_ >= 57
	DY4_ += MAS[4]

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	S += DY4_in >= 57
	DY4_in += MM_in[0]

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	S += DY4_mem0 >= 57
	DY4_mem0 += MAS_MEM[8]

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	S += NY5__mem0 >= 57
	NY5__mem0 += MM_MEM[0]

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	S += NY5__mem1 >= 57
	NY5__mem1 += MM_MEM[1]

	DY4 = S.Task('DY4', length=6, delay_cost=1)
	S += DY4 >= 58
	DY4 += MM[0]

	NY5_ = S.Task('NY5_', length=1, delay_cost=1)
	S += NY5_ >= 58
	NY5_ += MAS[4]

	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	S += Z_exp10_in >= 58
	Z_exp10_in += MM_in[0]

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	S += Z_exp10_mem0 >= 58
	Z_exp10_mem0 += MM_MEM[0]

	Z_exp10 = S.Task('Z_exp10', length=6, delay_cost=1)
	S += Z_exp10 >= 59
	Z_exp10 += MM[0]

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	S += k1_2_Z9_in >= 59
	k1_2_Z9_in += MM_in[0]

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	S += k1_2_Z9_mem1 >= 59
	k1_2_Z9_mem1 += MM_MEM[1]

	k1_2_Z9 = S.Task('k1_2_Z9', length=6, delay_cost=1)
	S += k1_2_Z9 >= 60
	k1_2_Z9 += MM[0]

	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	S += k2_6_Z9_in >= 60
	k2_6_Z9_in += MM_in[0]

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	S += k2_6_Z9_mem1 >= 60
	k2_6_Z9_mem1 += MM_MEM[1]

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	S += NX5__mem0 >= 61
	NX5__mem0 += MM_MEM[0]

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	S += NX5__mem1 >= 61
	NX5__mem1 += MM_MEM[1]

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	S += NY5_in >= 61
	NY5_in += MM_in[0]

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	S += NY5_mem0 >= 61
	NY5_mem0 += MAS_MEM[8]

	k2_6_Z9 = S.Task('k2_6_Z9', length=6, delay_cost=1)
	S += k2_6_Z9 >= 61
	k2_6_Z9 += MM[0]

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	S += DX5__mem0 >= 62
	DX5__mem0 += MM_MEM[0]

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	S += DX5__mem1 >= 62
	DX5__mem1 += MM_MEM[1]

	NX5_ = S.Task('NX5_', length=1, delay_cost=1)
	S += NX5_ >= 62
	NX5_ += MAS[1]

	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	S += NX5_in >= 62
	NX5_in += MM_in[0]

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	S += NX5_mem0 >= 62
	NX5_mem0 += MAS_MEM[2]

	NY5 = S.Task('NY5', length=6, delay_cost=1)
	S += NY5 >= 62
	NY5 += MM[0]

	DX5_ = S.Task('DX5_', length=1, delay_cost=1)
	S += DX5_ >= 63
	DX5_ += MAS[2]

	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	S += DX5_in >= 63
	DX5_in += MM_in[0]

	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	S += DX5_mem0 >= 63
	DX5_mem0 += MAS_MEM[4]

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	S += DY5__mem0 >= 63
	DY5__mem0 += MM_MEM[0]

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	S += DY5__mem1 >= 63
	DY5__mem1 += MM_MEM[1]

	NX5 = S.Task('NX5', length=6, delay_cost=1)
	S += NX5 >= 63
	NX5 += MM[0]

	DX5 = S.Task('DX5', length=6, delay_cost=1)
	S += DX5 >= 64
	DX5 += MM[0]

	DY5_ = S.Task('DY5_', length=1, delay_cost=1)
	S += DY5_ >= 64
	DY5_ += MAS[3]

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	S += Z_exp11_in >= 64
	Z_exp11_in += MM_in[0]

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	S += Z_exp11_mem0 >= 64
	Z_exp11_mem0 += MM_MEM[0]

	Z_exp11 = S.Task('Z_exp11', length=6, delay_cost=1)
	S += Z_exp11 >= 65
	Z_exp11 += MM[0]

	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	S += k0_2_Z9_in >= 65
	k0_2_Z9_in += MM_in[0]

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	S += k0_2_Z9_mem1 >= 65
	k0_2_Z9_mem1 += MM_MEM[1]

	k0_2_Z9 = S.Task('k0_2_Z9', length=6, delay_cost=1)
	S += k0_2_Z9 >= 66
	k0_2_Z9 += MM[0]

	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	S += k1_1_Z10_in >= 66
	k1_1_Z10_in += MM_in[0]

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	S += k1_1_Z10_mem1 >= 66
	k1_1_Z10_mem1 += MM_MEM[1]

	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	S += DY5_in >= 67
	DY5_in += MM_in[0]

	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	S += DY5_mem0 >= 67
	DY5_mem0 += MAS_MEM[6]

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	S += NY6__mem0 >= 67
	NY6__mem0 += MM_MEM[0]

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	S += NY6__mem1 >= 67
	NY6__mem1 += MM_MEM[1]

	k1_1_Z10 = S.Task('k1_1_Z10', length=6, delay_cost=1)
	S += k1_1_Z10 >= 67
	k1_1_Z10 += MM[0]

	DY5 = S.Task('DY5', length=6, delay_cost=1)
	S += DY5 >= 68
	DY5 += MM[0]

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	S += NX6__mem0 >= 68
	NX6__mem0 += MM_MEM[0]

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	S += NX6__mem1 >= 68
	NX6__mem1 += MM_MEM[1]

	NY6_ = S.Task('NY6_', length=1, delay_cost=1)
	S += NY6_ >= 68
	NY6_ += MAS[0]

	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	S += NY6_in >= 68
	NY6_in += MM_in[0]

	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	S += NY6_mem0 >= 68
	NY6_mem0 += MAS_MEM[0]

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	S += DX6__mem0 >= 69
	DX6__mem0 += MM_MEM[0]

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	S += DX6__mem1 >= 69
	DX6__mem1 += MM_MEM[1]

	NX6_ = S.Task('NX6_', length=1, delay_cost=1)
	S += NX6_ >= 69
	NX6_ += MAS[1]

	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	S += NX6_in >= 69
	NX6_in += MM_in[0]

	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	S += NX6_mem0 >= 69
	NX6_mem0 += MAS_MEM[2]

	NY6 = S.Task('NY6', length=6, delay_cost=1)
	S += NY6 >= 69
	NY6 += MM[0]

	DX6_ = S.Task('DX6_', length=1, delay_cost=1)
	S += DX6_ >= 70
	DX6_ += MAS[1]

	NX6 = S.Task('NX6', length=6, delay_cost=1)
	S += NX6 >= 70
	NX6 += MM[0]

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	S += Z_exp12_in >= 70
	Z_exp12_in += MM_in[0]

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	S += Z_exp12_mem0 >= 70
	Z_exp12_mem0 += MM_MEM[0]

	Z_exp12 = S.Task('Z_exp12', length=6, delay_cost=1)
	S += Z_exp12 >= 71
	Z_exp12 += MM[0]

	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	S += k0_0_Z11_in >= 71
	k0_0_Z11_in += MM_in[0]

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	S += k0_0_Z11_mem1 >= 71
	k0_0_Z11_mem1 += MM_MEM[1]

	k0_0_Z11 = S.Task('k0_0_Z11', length=6, delay_cost=1)
	S += k0_0_Z11 >= 72
	k0_0_Z11 += MM[0]

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	S += k3_7_Z9_in >= 72
	k3_7_Z9_in += MM_in[0]

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	S += k3_7_Z9_mem1 >= 72
	k3_7_Z9_mem1 += MM_MEM[1]

	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	S += DX6_in >= 73
	DX6_in += MM_in[0]

	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	S += DX6_mem0 >= 73
	DX6_mem0 += MAS_MEM[2]

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	S += DY6__mem0 >= 73
	DY6__mem0 += MM_MEM[0]

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	S += DY6__mem1 >= 73
	DY6__mem1 += MM_MEM[1]

	k3_7_Z9 = S.Task('k3_7_Z9', length=6, delay_cost=1)
	S += k3_7_Z9 >= 73
	k3_7_Z9 += MM[0]

	DX6 = S.Task('DX6', length=6, delay_cost=1)
	S += DX6 >= 74
	DX6 += MM[0]

	DY6_ = S.Task('DY6_', length=1, delay_cost=1)
	S += DY6_ >= 74
	DY6_ += MAS[4]

	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	S += DY6_in >= 74
	DY6_in += MM_in[0]

	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	S += DY6_mem0 >= 74
	DY6_mem0 += MAS_MEM[8]

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	S += NY7__mem0 >= 74
	NY7__mem0 += MM_MEM[0]

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	S += NY7__mem1 >= 74
	NY7__mem1 += MM_MEM[1]

	DY6 = S.Task('DY6', length=6, delay_cost=1)
	S += DY6 >= 75
	DY6 += MM[0]

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	S += NX7__mem0 >= 75
	NX7__mem0 += MM_MEM[0]

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	S += NX7__mem1 >= 75
	NX7__mem1 += MM_MEM[1]

	NY7_ = S.Task('NY7_', length=1, delay_cost=1)
	S += NY7_ >= 75
	NY7_ += MAS[3]

	NX7_ = S.Task('NX7_', length=1, delay_cost=1)
	S += NX7_ >= 76
	NX7_ += MAS[3]

	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	S += Z_exp13_in >= 76
	Z_exp13_in += MM_in[0]

	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	S += Z_exp13_mem0 >= 76
	Z_exp13_mem0 += MM_MEM[0]

	Z_exp13 = S.Task('Z_exp13', length=6, delay_cost=1)
	S += Z_exp13 >= 77
	Z_exp13 += MM[0]

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	S += k0_1_Z10_in >= 77
	k0_1_Z10_in += MM_in[0]

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	S += k0_1_Z10_mem1 >= 77
	k0_1_Z10_mem1 += MM_MEM[1]

	k0_1_Z10 = S.Task('k0_1_Z10', length=6, delay_cost=1)
	S += k0_1_Z10 >= 78
	k0_1_Z10 += MM[0]

	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	S += k3_6_Z10_in >= 78
	k3_6_Z10_in += MM_in[0]

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	S += k3_6_Z10_mem1 >= 78
	k3_6_Z10_mem1 += MM_MEM[1]

	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	S += k2_3_Z12_in >= 79
	k2_3_Z12_in += MM_in[0]

	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	S += k2_3_Z12_mem1 >= 79
	k2_3_Z12_mem1 += MM_MEM[1]

	k3_6_Z10 = S.Task('k3_6_Z10', length=6, delay_cost=1)
	S += k3_6_Z10 >= 79
	k3_6_Z10 += MM[0]

	k2_3_Z12 = S.Task('k2_3_Z12', length=6, delay_cost=1)
	S += k2_3_Z12 >= 80
	k2_3_Z12 += MM[0]

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	S += k2_5_Z10_in >= 80
	k2_5_Z10_in += MM_in[0]

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	S += k2_5_Z10_mem1 >= 80
	k2_5_Z10_mem1 += MM_MEM[1]

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	S += k1_0_Z11_in >= 81
	k1_0_Z11_in += MM_in[0]

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	S += k1_0_Z11_mem1 >= 81
	k1_0_Z11_mem1 += MM_MEM[1]

	k2_5_Z10 = S.Task('k2_5_Z10', length=6, delay_cost=1)
	S += k2_5_Z10 >= 81
	k2_5_Z10 += MM[0]

	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	S += Z_exp14_in >= 82
	Z_exp14_in += MM_in[0]

	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	S += Z_exp14_mem0 >= 82
	Z_exp14_mem0 += MM_MEM[0]

	k1_0_Z11 = S.Task('k1_0_Z11', length=6, delay_cost=1)
	S += k1_0_Z11 >= 82
	k1_0_Z11 += MM[0]

	Z_exp14 = S.Task('Z_exp14', length=6, delay_cost=1)
	S += Z_exp14 >= 83
	Z_exp14 += MM[0]

	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	S += k3_4_Z12_in >= 83
	k3_4_Z12_in += MM_in[0]

	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	S += k3_4_Z12_mem1 >= 83
	k3_4_Z12_mem1 += MM_MEM[1]

	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	S += k2_4_Z11_in >= 84
	k2_4_Z11_in += MM_in[0]

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	S += k2_4_Z11_mem1 >= 84
	k2_4_Z11_mem1 += MM_MEM[1]

	k3_4_Z12 = S.Task('k3_4_Z12', length=6, delay_cost=1)
	S += k3_4_Z12 >= 84
	k3_4_Z12 += MM[0]

	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	S += k2_2_Z13_in >= 85
	k2_2_Z13_in += MM_in[0]

	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	S += k2_2_Z13_mem1 >= 85
	k2_2_Z13_mem1 += MM_MEM[1]

	k2_4_Z11 = S.Task('k2_4_Z11', length=6, delay_cost=1)
	S += k2_4_Z11 >= 85
	k2_4_Z11 += MM[0]

	k2_2_Z13 = S.Task('k2_2_Z13', length=6, delay_cost=1)
	S += k2_2_Z13 >= 86
	k2_2_Z13 += MM[0]

	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	S += k3_3_Z13_in >= 86
	k3_3_Z13_in += MM_in[0]

	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	S += k3_3_Z13_mem1 >= 86
	k3_3_Z13_mem1 += MM_MEM[1]

	k3_3_Z13 = S.Task('k3_3_Z13', length=6, delay_cost=1)
	S += k3_3_Z13 >= 87
	k3_3_Z13 += MM[0]

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	S += k3_5_Z11_in >= 87
	k3_5_Z11_in += MM_in[0]

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	S += k3_5_Z11_mem1 >= 87
	k3_5_Z11_mem1 += MM_MEM[1]

	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	S += k2_1_Z14_in >= 88
	k2_1_Z14_in += MM_in[0]

	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	S += k2_1_Z14_mem1 >= 88
	k2_1_Z14_mem1 += MM_MEM[1]

	k3_5_Z11 = S.Task('k3_5_Z11', length=6, delay_cost=1)
	S += k3_5_Z11 >= 88
	k3_5_Z11 += MM[0]

	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	S += Z_exp15_in >= 89
	Z_exp15_in += MM_in[0]

	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	S += Z_exp15_mem0 >= 89
	Z_exp15_mem0 += MM_MEM[0]

	k2_1_Z14 = S.Task('k2_1_Z14', length=6, delay_cost=1)
	S += k2_1_Z14 >= 89
	k2_1_Z14 += MM[0]

	Z_exp15 = S.Task('Z_exp15', length=6, delay_cost=1)
	S += Z_exp15 >= 90
	Z_exp15 += MM[0]

	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	S += k3_2_Z14_in >= 90
	k3_2_Z14_in += MM_in[0]

	k3_2_Z14_mem1 = S.Task('k3_2_Z14_mem1', length=1, delay_cost=1)
	S += k3_2_Z14_mem1 >= 90
	k3_2_Z14_mem1 += MM_MEM[1]

	k3_2_Z14 = S.Task('k3_2_Z14', length=6, delay_cost=1)
	S += k3_2_Z14 >= 91
	k3_2_Z14 += MM[0]


	# new tasks
	Z_exp16_in = S.Task('Z_exp16_in', length=1, delay_cost=1)
	Z_exp16_in += alt(MM_in)
	Z_exp16 = S.Task('Z_exp16', length=6, delay_cost=1)
	Z_exp16 += alt(MM)
	S += Z_exp16>=Z_exp16_in

	Z_exp16_mem0 = S.Task('Z_exp16_mem0', length=1, delay_cost=1)
	Z_exp16_mem0 += MM_MEM[0]
	S += 95 < Z_exp16_mem0
	S += Z_exp16_mem0 <= Z_exp16

	Z_exp16_mem1 = S.Task('Z_exp16_mem1', length=1, delay_cost=1)
	Z_exp16_mem1 += MAIN_MEM_r[1]
	NX7_in = S.Task('NX7_in', length=1, delay_cost=1)
	NX7_in += alt(MM_in)
	NX7 = S.Task('NX7', length=6, delay_cost=1)
	NX7 += alt(MM)
	S += NX7>=NX7_in

	NX7_mem0 = S.Task('NX7_mem0', length=1, delay_cost=1)
	NX7_mem0 += MAS_MEM[6]
	S += 76 < NX7_mem0
	S += NX7_mem0 <= NX7

	NX7_mem1 = S.Task('NX7_mem1', length=1, delay_cost=1)
	NX7_mem1 += MAIN_MEM_r[1]
	DX7_ = S.Task('DX7_', length=1, delay_cost=1)
	DX7_ += alt(MAS)

	DX7__mem0 = S.Task('DX7__mem0', length=1, delay_cost=1)
	DX7__mem0 += MM_MEM[0]
	S += 79 < DX7__mem0
	S += DX7__mem0 <= DX7_

	DX7__mem1 = S.Task('DX7__mem1', length=1, delay_cost=1)
	DX7__mem1 += MM_MEM[1]
	S += 58 < DX7__mem1
	S += DX7__mem1 <= DX7_

	NY7_in = S.Task('NY7_in', length=1, delay_cost=1)
	NY7_in += alt(MM_in)
	NY7 = S.Task('NY7', length=6, delay_cost=1)
	NY7 += alt(MM)
	S += NY7>=NY7_in

	NY7_mem0 = S.Task('NY7_mem0', length=1, delay_cost=1)
	NY7_mem0 += MAS_MEM[6]
	S += 75 < NY7_mem0
	S += NY7_mem0 <= NY7

	NY7_mem1 = S.Task('NY7_mem1', length=1, delay_cost=1)
	NY7_mem1 += MAIN_MEM_r[1]
	k2_0_Z15_in = S.Task('k2_0_Z15_in', length=1, delay_cost=1)
	k2_0_Z15_in += alt(MM_in)
	k2_0_Z15 = S.Task('k2_0_Z15', length=6, delay_cost=1)
	k2_0_Z15 += alt(MM)
	S += k2_0_Z15>=k2_0_Z15_in

	k2_0_Z15_mem0 = S.Task('k2_0_Z15_mem0', length=1, delay_cost=1)
	k2_0_Z15_mem0 += MAIN_MEM_r[0]
	k2_0_Z15_mem1 = S.Task('k2_0_Z15_mem1', length=1, delay_cost=1)
	k2_0_Z15_mem1 += MM_MEM[1]
	S += 95 < k2_0_Z15_mem1
	S += k2_0_Z15_mem1 <= k2_0_Z15

	DY7_ = S.Task('DY7_', length=1, delay_cost=1)
	DY7_ += alt(MAS)

	DY7__mem0 = S.Task('DY7__mem0', length=1, delay_cost=1)
	DY7__mem0 += MM_MEM[0]
	S += 80 < DY7__mem0
	S += DY7__mem0 <= DY7_

	DY7__mem1 = S.Task('DY7__mem1', length=1, delay_cost=1)
	DY7__mem1 += MM_MEM[1]
	S += 54 < DY7__mem1
	S += DY7__mem1 <= DY7_

	k3_1_Z15_in = S.Task('k3_1_Z15_in', length=1, delay_cost=1)
	k3_1_Z15_in += alt(MM_in)
	k3_1_Z15 = S.Task('k3_1_Z15', length=6, delay_cost=1)
	k3_1_Z15 += alt(MM)
	S += k3_1_Z15>=k3_1_Z15_in

	k3_1_Z15_mem0 = S.Task('k3_1_Z15_mem0', length=1, delay_cost=1)
	k3_1_Z15_mem0 += MAIN_MEM_r[0]
	k3_1_Z15_mem1 = S.Task('k3_1_Z15_mem1', length=1, delay_cost=1)
	k3_1_Z15_mem1 += MM_MEM[1]
	S += 95 < k3_1_Z15_mem1
	S += k3_1_Z15_mem1 <= k3_1_Z15

	NX8_ = S.Task('NX8_', length=1, delay_cost=1)
	NX8_ += alt(MAS)

	NX8__mem0 = S.Task('NX8__mem0', length=1, delay_cost=1)
	NX8__mem0 += alt(MM_MEM)
	S += (NX7*MM[0])-1 < NX8__mem0*MM_MEM[0]
	S += NX8__mem0 <= NX8_

	NX8__mem1 = S.Task('NX8__mem1', length=1, delay_cost=1)
	NX8__mem1 += MM_MEM[1]
	S += 55 < NX8__mem1
	S += NX8__mem1 <= NX8_

	DX7_in = S.Task('DX7_in', length=1, delay_cost=1)
	DX7_in += alt(MM_in)
	DX7 = S.Task('DX7', length=6, delay_cost=1)
	DX7 += alt(MM)
	S += DX7>=DX7_in

	DX7_mem0 = S.Task('DX7_mem0', length=1, delay_cost=1)
	DX7_mem0 += alt(MAS_MEM)
	S += (DX7_*MAS[0])-1 < DX7_mem0*MAS_MEM[0]
	S += (DX7_*MAS[1])-1 < DX7_mem0*MAS_MEM[2]
	S += (DX7_*MAS[2])-1 < DX7_mem0*MAS_MEM[4]
	S += (DX7_*MAS[3])-1 < DX7_mem0*MAS_MEM[6]
	S += (DX7_*MAS[4])-1 < DX7_mem0*MAS_MEM[8]
	S += DX7_mem0 <= DX7

	DX7_mem1 = S.Task('DX7_mem1', length=1, delay_cost=1)
	DX7_mem1 += MAIN_MEM_r[1]
	NY8_ = S.Task('NY8_', length=1, delay_cost=1)
	NY8_ += alt(MAS)

	NY8__mem0 = S.Task('NY8__mem0', length=1, delay_cost=1)
	NY8__mem0 += alt(MM_MEM)
	S += (NY7*MM[0])-1 < NY8__mem0*MM_MEM[0]
	S += NY8__mem0 <= NY8_

	NY8__mem1 = S.Task('NY8__mem1', length=1, delay_cost=1)
	NY8__mem1 += MM_MEM[1]
	S += 56 < NY8__mem1
	S += NY8__mem1 <= NY8_

	DY7_in = S.Task('DY7_in', length=1, delay_cost=1)
	DY7_in += alt(MM_in)
	DY7 = S.Task('DY7', length=6, delay_cost=1)
	DY7 += alt(MM)
	S += DY7>=DY7_in

	DY7_mem0 = S.Task('DY7_mem0', length=1, delay_cost=1)
	DY7_mem0 += alt(MAS_MEM)
	S += (DY7_*MAS[0])-1 < DY7_mem0*MAS_MEM[0]
	S += (DY7_*MAS[1])-1 < DY7_mem0*MAS_MEM[2]
	S += (DY7_*MAS[2])-1 < DY7_mem0*MAS_MEM[4]
	S += (DY7_*MAS[3])-1 < DY7_mem0*MAS_MEM[6]
	S += (DY7_*MAS[4])-1 < DY7_mem0*MAS_MEM[8]
	S += DY7_mem0 <= DY7

	DY7_mem1 = S.Task('DY7_mem1', length=1, delay_cost=1)
	DY7_mem1 += MAIN_MEM_r[1]
	k3_0_Z16_in = S.Task('k3_0_Z16_in', length=1, delay_cost=1)
	k3_0_Z16_in += alt(MM_in)
	k3_0_Z16 = S.Task('k3_0_Z16', length=6, delay_cost=1)
	k3_0_Z16 += alt(MM)
	S += k3_0_Z16>=k3_0_Z16_in

	k3_0_Z16_mem0 = S.Task('k3_0_Z16_mem0', length=1, delay_cost=1)
	k3_0_Z16_mem0 += MAIN_MEM_r[0]
	k3_0_Z16_mem1 = S.Task('k3_0_Z16_mem1', length=1, delay_cost=1)
	k3_0_Z16_mem1 += alt(MM_MEM)
	S += (Z_exp16*MM[0])-1 < k3_0_Z16_mem1*MM_MEM[1]
	S += k3_0_Z16_mem1 <= k3_0_Z16

	NX8_in = S.Task('NX8_in', length=1, delay_cost=1)
	NX8_in += alt(MM_in)
	NX8 = S.Task('NX8', length=6, delay_cost=1)
	NX8 += alt(MM)
	S += NX8>=NX8_in

	NX8_mem0 = S.Task('NX8_mem0', length=1, delay_cost=1)
	NX8_mem0 += alt(MAS_MEM)
	S += (NX8_*MAS[0])-1 < NX8_mem0*MAS_MEM[0]
	S += (NX8_*MAS[1])-1 < NX8_mem0*MAS_MEM[2]
	S += (NX8_*MAS[2])-1 < NX8_mem0*MAS_MEM[4]
	S += (NX8_*MAS[3])-1 < NX8_mem0*MAS_MEM[6]
	S += (NX8_*MAS[4])-1 < NX8_mem0*MAS_MEM[8]
	S += NX8_mem0 <= NX8

	NX8_mem1 = S.Task('NX8_mem1', length=1, delay_cost=1)
	NX8_mem1 += MAIN_MEM_r[1]
	DX8_ = S.Task('DX8_', length=1, delay_cost=1)
	DX8_ += alt(MAS)

	DX8__mem0 = S.Task('DX8__mem0', length=1, delay_cost=1)
	DX8__mem0 += alt(MM_MEM)
	S += (DX7*MM[0])-1 < DX8__mem0*MM_MEM[0]
	S += DX8__mem0 <= DX8_

	DX8__mem1 = S.Task('DX8__mem1', length=1, delay_cost=1)
	DX8__mem1 += MM_MEM[1]
	S += 65 < DX8__mem1
	S += DX8__mem1 <= DX8_

	NY8_in = S.Task('NY8_in', length=1, delay_cost=1)
	NY8_in += alt(MM_in)
	NY8 = S.Task('NY8', length=6, delay_cost=1)
	NY8 += alt(MM)
	S += NY8>=NY8_in

	NY8_mem0 = S.Task('NY8_mem0', length=1, delay_cost=1)
	NY8_mem0 += alt(MAS_MEM)
	S += (NY8_*MAS[0])-1 < NY8_mem0*MAS_MEM[0]
	S += (NY8_*MAS[1])-1 < NY8_mem0*MAS_MEM[2]
	S += (NY8_*MAS[2])-1 < NY8_mem0*MAS_MEM[4]
	S += (NY8_*MAS[3])-1 < NY8_mem0*MAS_MEM[6]
	S += (NY8_*MAS[4])-1 < NY8_mem0*MAS_MEM[8]
	S += NY8_mem0 <= NY8

	NY8_mem1 = S.Task('NY8_mem1', length=1, delay_cost=1)
	NY8_mem1 += MAIN_MEM_r[1]
	DY8_ = S.Task('DY8_', length=1, delay_cost=1)
	DY8_ += alt(MAS)

	DY8__mem0 = S.Task('DY8__mem0', length=1, delay_cost=1)
	DY8__mem0 += alt(MM_MEM)
	S += (DY7*MM[0])-1 < DY8__mem0*MM_MEM[0]
	S += DY8__mem0 <= DY8_

	DY8__mem1 = S.Task('DY8__mem1', length=1, delay_cost=1)
	DY8__mem1 += MM_MEM[1]
	S += 78 < DY8__mem1
	S += DY8__mem1 <= DY8_

	NX9_ = S.Task('NX9_', length=1, delay_cost=1)
	NX9_ += alt(MAS)

	NX9__mem0 = S.Task('NX9__mem0', length=1, delay_cost=1)
	NX9__mem0 += alt(MM_MEM)
	S += (NX8*MM[0])-1 < NX9__mem0*MM_MEM[0]
	S += NX9__mem0 <= NX9_

	NX9__mem1 = S.Task('NX9__mem1', length=1, delay_cost=1)
	NX9__mem1 += MM_MEM[1]
	S += 71 < NX9__mem1
	S += NX9__mem1 <= NX9_

	DX8_in = S.Task('DX8_in', length=1, delay_cost=1)
	DX8_in += alt(MM_in)
	DX8 = S.Task('DX8', length=6, delay_cost=1)
	DX8 += alt(MM)
	S += DX8>=DX8_in

	DX8_mem0 = S.Task('DX8_mem0', length=1, delay_cost=1)
	DX8_mem0 += alt(MAS_MEM)
	S += (DX8_*MAS[0])-1 < DX8_mem0*MAS_MEM[0]
	S += (DX8_*MAS[1])-1 < DX8_mem0*MAS_MEM[2]
	S += (DX8_*MAS[2])-1 < DX8_mem0*MAS_MEM[4]
	S += (DX8_*MAS[3])-1 < DX8_mem0*MAS_MEM[6]
	S += (DX8_*MAS[4])-1 < DX8_mem0*MAS_MEM[8]
	S += DX8_mem0 <= DX8

	DX8_mem1 = S.Task('DX8_mem1', length=1, delay_cost=1)
	DX8_mem1 += MAIN_MEM_r[1]
	NY9_ = S.Task('NY9_', length=1, delay_cost=1)
	NY9_ += alt(MAS)

	NY9__mem0 = S.Task('NY9__mem0', length=1, delay_cost=1)
	NY9__mem0 += alt(MM_MEM)
	S += (NY8*MM[0])-1 < NY9__mem0*MM_MEM[0]
	S += NY9__mem0 <= NY9_

	NY9__mem1 = S.Task('NY9__mem1', length=1, delay_cost=1)
	NY9__mem1 += MM_MEM[1]
	S += 66 < NY9__mem1
	S += NY9__mem1 <= NY9_

	DY8_in = S.Task('DY8_in', length=1, delay_cost=1)
	DY8_in += alt(MM_in)
	DY8 = S.Task('DY8', length=6, delay_cost=1)
	DY8 += alt(MM)
	S += DY8>=DY8_in

	DY8_mem0 = S.Task('DY8_mem0', length=1, delay_cost=1)
	DY8_mem0 += alt(MAS_MEM)
	S += (DY8_*MAS[0])-1 < DY8_mem0*MAS_MEM[0]
	S += (DY8_*MAS[1])-1 < DY8_mem0*MAS_MEM[2]
	S += (DY8_*MAS[2])-1 < DY8_mem0*MAS_MEM[4]
	S += (DY8_*MAS[3])-1 < DY8_mem0*MAS_MEM[6]
	S += (DY8_*MAS[4])-1 < DY8_mem0*MAS_MEM[8]
	S += DY8_mem0 <= DY8

	DY8_mem1 = S.Task('DY8_mem1', length=1, delay_cost=1)
	DY8_mem1 += MAIN_MEM_r[1]
	NX9_in = S.Task('NX9_in', length=1, delay_cost=1)
	NX9_in += alt(MM_in)
	NX9 = S.Task('NX9', length=6, delay_cost=1)
	NX9 += alt(MM)
	S += NX9>=NX9_in

	NX9_mem0 = S.Task('NX9_mem0', length=1, delay_cost=1)
	NX9_mem0 += alt(MAS_MEM)
	S += (NX9_*MAS[0])-1 < NX9_mem0*MAS_MEM[0]
	S += (NX9_*MAS[1])-1 < NX9_mem0*MAS_MEM[2]
	S += (NX9_*MAS[2])-1 < NX9_mem0*MAS_MEM[4]
	S += (NX9_*MAS[3])-1 < NX9_mem0*MAS_MEM[6]
	S += (NX9_*MAS[4])-1 < NX9_mem0*MAS_MEM[8]
	S += NX9_mem0 <= NX9

	NX9_mem1 = S.Task('NX9_mem1', length=1, delay_cost=1)
	NX9_mem1 += MAIN_MEM_r[1]
	DX9_ = S.Task('DX9_', length=1, delay_cost=1)
	DX9_ += alt(MAS)

	DX9__mem0 = S.Task('DX9__mem0', length=1, delay_cost=1)
	DX9__mem0 += alt(MM_MEM)
	S += (DX8*MM[0])-1 < DX9__mem0*MM_MEM[0]
	S += DX9__mem0 <= DX9_

	DX9__mem1 = S.Task('DX9__mem1', length=1, delay_cost=1)
	DX9__mem1 += MM_MEM[1]
	S += 72 < DX9__mem1
	S += DX9__mem1 <= DX9_

	NY9_in = S.Task('NY9_in', length=1, delay_cost=1)
	NY9_in += alt(MM_in)
	NY9 = S.Task('NY9', length=6, delay_cost=1)
	NY9 += alt(MM)
	S += NY9>=NY9_in

	NY9_mem0 = S.Task('NY9_mem0', length=1, delay_cost=1)
	NY9_mem0 += alt(MAS_MEM)
	S += (NY9_*MAS[0])-1 < NY9_mem0*MAS_MEM[0]
	S += (NY9_*MAS[1])-1 < NY9_mem0*MAS_MEM[2]
	S += (NY9_*MAS[2])-1 < NY9_mem0*MAS_MEM[4]
	S += (NY9_*MAS[3])-1 < NY9_mem0*MAS_MEM[6]
	S += (NY9_*MAS[4])-1 < NY9_mem0*MAS_MEM[8]
	S += NY9_mem0 <= NY9

	NY9_mem1 = S.Task('NY9_mem1', length=1, delay_cost=1)
	NY9_mem1 += MAIN_MEM_r[1]
	DY9_ = S.Task('DY9_', length=1, delay_cost=1)
	DY9_ += alt(MAS)

	DY9__mem0 = S.Task('DY9__mem0', length=1, delay_cost=1)
	DY9__mem0 += alt(MM_MEM)
	S += (DY8*MM[0])-1 < DY9__mem0*MM_MEM[0]
	S += DY9__mem0 <= DY9_

	DY9__mem1 = S.Task('DY9__mem1', length=1, delay_cost=1)
	DY9__mem1 += MM_MEM[1]
	S += 84 < DY9__mem1
	S += DY9__mem1 <= DY9_

	NX10_ = S.Task('NX10_', length=1, delay_cost=1)
	NX10_ += alt(MAS)

	NX10__mem0 = S.Task('NX10__mem0', length=1, delay_cost=1)
	NX10__mem0 += alt(MM_MEM)
	S += (NX9*MM[0])-1 < NX10__mem0*MM_MEM[0]
	S += NX10__mem0 <= NX10_

	NX10__mem1 = S.Task('NX10__mem1', length=1, delay_cost=1)
	NX10__mem1 += MM_MEM[1]
	S += 83 < NX10__mem1
	S += NX10__mem1 <= NX10_

	DX9_in = S.Task('DX9_in', length=1, delay_cost=1)
	DX9_in += alt(MM_in)
	DX9 = S.Task('DX9', length=6, delay_cost=1)
	DX9 += alt(MM)
	S += DX9>=DX9_in

	DX9_mem0 = S.Task('DX9_mem0', length=1, delay_cost=1)
	DX9_mem0 += alt(MAS_MEM)
	S += (DX9_*MAS[0])-1 < DX9_mem0*MAS_MEM[0]
	S += (DX9_*MAS[1])-1 < DX9_mem0*MAS_MEM[2]
	S += (DX9_*MAS[2])-1 < DX9_mem0*MAS_MEM[4]
	S += (DX9_*MAS[3])-1 < DX9_mem0*MAS_MEM[6]
	S += (DX9_*MAS[4])-1 < DX9_mem0*MAS_MEM[8]
	S += DX9_mem0 <= DX9

	DX9_mem1 = S.Task('DX9_mem1', length=1, delay_cost=1)
	DX9_mem1 += MAIN_MEM_r[1]
	NY10_ = S.Task('NY10_', length=1, delay_cost=1)
	NY10_ += alt(MAS)

	NY10__mem0 = S.Task('NY10__mem0', length=1, delay_cost=1)
	NY10__mem0 += alt(MM_MEM)
	S += (NY9*MM[0])-1 < NY10__mem0*MM_MEM[0]
	S += NY10__mem0 <= NY10_

	NY10__mem1 = S.Task('NY10__mem1', length=1, delay_cost=1)
	NY10__mem1 += MM_MEM[1]
	S += 86 < NY10__mem1
	S += NY10__mem1 <= NY10_

	DY9_in = S.Task('DY9_in', length=1, delay_cost=1)
	DY9_in += alt(MM_in)
	DY9 = S.Task('DY9', length=6, delay_cost=1)
	DY9 += alt(MM)
	S += DY9>=DY9_in

	DY9_mem0 = S.Task('DY9_mem0', length=1, delay_cost=1)
	DY9_mem0 += alt(MAS_MEM)
	S += (DY9_*MAS[0])-1 < DY9_mem0*MAS_MEM[0]
	S += (DY9_*MAS[1])-1 < DY9_mem0*MAS_MEM[2]
	S += (DY9_*MAS[2])-1 < DY9_mem0*MAS_MEM[4]
	S += (DY9_*MAS[3])-1 < DY9_mem0*MAS_MEM[6]
	S += (DY9_*MAS[4])-1 < DY9_mem0*MAS_MEM[8]
	S += DY9_mem0 <= DY9

	DY9_mem1 = S.Task('DY9_mem1', length=1, delay_cost=1)
	DY9_mem1 += MAIN_MEM_r[1]
	NX10_in = S.Task('NX10_in', length=1, delay_cost=1)
	NX10_in += alt(MM_in)
	NX10 = S.Task('NX10', length=6, delay_cost=1)
	NX10 += alt(MM)
	S += NX10>=NX10_in

	NX10_mem0 = S.Task('NX10_mem0', length=1, delay_cost=1)
	NX10_mem0 += alt(MAS_MEM)
	S += (NX10_*MAS[0])-1 < NX10_mem0*MAS_MEM[0]
	S += (NX10_*MAS[1])-1 < NX10_mem0*MAS_MEM[2]
	S += (NX10_*MAS[2])-1 < NX10_mem0*MAS_MEM[4]
	S += (NX10_*MAS[3])-1 < NX10_mem0*MAS_MEM[6]
	S += (NX10_*MAS[4])-1 < NX10_mem0*MAS_MEM[8]
	S += NX10_mem0 <= NX10

	NX10_mem1 = S.Task('NX10_mem1', length=1, delay_cost=1)
	NX10_mem1 += MAIN_MEM_r[1]
	DX = S.Task('DX', length=1, delay_cost=1)
	DX += alt(MAS)

	DX_mem0 = S.Task('DX_mem0', length=1, delay_cost=1)
	DX_mem0 += alt(MM_MEM)
	S += (DX9*MM[0])-1 < DX_mem0*MM_MEM[0]
	S += DX_mem0 <= DX

	DX_mem1 = S.Task('DX_mem1', length=1, delay_cost=1)
	DX_mem1 += MM_MEM[1]
	S += 87 < DX_mem1
	S += DX_mem1 <= DX

	NY10_in = S.Task('NY10_in', length=1, delay_cost=1)
	NY10_in += alt(MM_in)
	NY10 = S.Task('NY10', length=6, delay_cost=1)
	NY10 += alt(MM)
	S += NY10>=NY10_in

	NY10_mem0 = S.Task('NY10_mem0', length=1, delay_cost=1)
	NY10_mem0 += alt(MAS_MEM)
	S += (NY10_*MAS[0])-1 < NY10_mem0*MAS_MEM[0]
	S += (NY10_*MAS[1])-1 < NY10_mem0*MAS_MEM[2]
	S += (NY10_*MAS[2])-1 < NY10_mem0*MAS_MEM[4]
	S += (NY10_*MAS[3])-1 < NY10_mem0*MAS_MEM[6]
	S += (NY10_*MAS[4])-1 < NY10_mem0*MAS_MEM[8]
	S += NY10_mem0 <= NY10

	NY10_mem1 = S.Task('NY10_mem1', length=1, delay_cost=1)
	NY10_mem1 += MAIN_MEM_r[1]
	DY10_ = S.Task('DY10_', length=1, delay_cost=1)
	DY10_ += alt(MAS)

	DY10__mem0 = S.Task('DY10__mem0', length=1, delay_cost=1)
	DY10__mem0 += alt(MM_MEM)
	S += (DY9*MM[0])-1 < DY10__mem0*MM_MEM[0]
	S += DY10__mem0 <= DY10_

	DY10__mem1 = S.Task('DY10__mem1', length=1, delay_cost=1)
	DY10__mem1 += MM_MEM[1]
	S += 93 < DY10__mem1
	S += DY10__mem1 <= DY10_

	NX = S.Task('NX', length=1, delay_cost=1)
	NX += alt(MAS)

	NX_mem0 = S.Task('NX_mem0', length=1, delay_cost=1)
	NX_mem0 += alt(MM_MEM)
	S += (NX10*MM[0])-1 < NX_mem0*MM_MEM[0]
	S += NX_mem0 <= NX

	NX_mem1 = S.Task('NX_mem1', length=1, delay_cost=1)
	NX_mem1 += MM_MEM[1]
	S += 77 < NX_mem1
	S += NX_mem1 <= NX

	NY11_ = S.Task('NY11_', length=1, delay_cost=1)
	NY11_ += alt(MAS)

	NY11__mem0 = S.Task('NY11__mem0', length=1, delay_cost=1)
	NY11__mem0 += alt(MM_MEM)
	S += (NY10*MM[0])-1 < NY11__mem0*MM_MEM[0]
	S += NY11__mem0 <= NY11_

	NY11__mem1 = S.Task('NY11__mem1', length=1, delay_cost=1)
	NY11__mem1 += MM_MEM[1]
	S += 90 < NY11__mem1
	S += NY11__mem1 <= NY11_

	DY10_in = S.Task('DY10_in', length=1, delay_cost=1)
	DY10_in += alt(MM_in)
	DY10 = S.Task('DY10', length=6, delay_cost=1)
	DY10 += alt(MM)
	S += DY10>=DY10_in

	DY10_mem0 = S.Task('DY10_mem0', length=1, delay_cost=1)
	DY10_mem0 += alt(MAS_MEM)
	S += (DY10_*MAS[0])-1 < DY10_mem0*MAS_MEM[0]
	S += (DY10_*MAS[1])-1 < DY10_mem0*MAS_MEM[2]
	S += (DY10_*MAS[2])-1 < DY10_mem0*MAS_MEM[4]
	S += (DY10_*MAS[3])-1 < DY10_mem0*MAS_MEM[6]
	S += (DY10_*MAS[4])-1 < DY10_mem0*MAS_MEM[8]
	S += DY10_mem0 <= DY10

	DY10_mem1 = S.Task('DY10_mem1', length=1, delay_cost=1)
	DY10_mem1 += MAIN_MEM_r[1]
	NY11_in = S.Task('NY11_in', length=1, delay_cost=1)
	NY11_in += alt(MM_in)
	NY11 = S.Task('NY11', length=6, delay_cost=1)
	NY11 += alt(MM)
	S += NY11>=NY11_in

	NY11_mem0 = S.Task('NY11_mem0', length=1, delay_cost=1)
	NY11_mem0 += alt(MAS_MEM)
	S += (NY11_*MAS[0])-1 < NY11_mem0*MAS_MEM[0]
	S += (NY11_*MAS[1])-1 < NY11_mem0*MAS_MEM[2]
	S += (NY11_*MAS[2])-1 < NY11_mem0*MAS_MEM[4]
	S += (NY11_*MAS[3])-1 < NY11_mem0*MAS_MEM[6]
	S += (NY11_*MAS[4])-1 < NY11_mem0*MAS_MEM[8]
	S += NY11_mem0 <= NY11

	NY11_mem1 = S.Task('NY11_mem1', length=1, delay_cost=1)
	NY11_mem1 += MAIN_MEM_r[1]
	DY11_ = S.Task('DY11_', length=1, delay_cost=1)
	DY11_ += alt(MAS)

	DY11__mem0 = S.Task('DY11__mem0', length=1, delay_cost=1)
	DY11__mem0 += alt(MM_MEM)
	S += (DY10*MM[0])-1 < DY11__mem0*MM_MEM[0]
	S += DY11__mem0 <= DY11_

	DY11__mem1 = S.Task('DY11__mem1', length=1, delay_cost=1)
	DY11__mem1 += MM_MEM[1]
	S += 89 < DY11__mem1
	S += DY11__mem1 <= DY11_

	NY12_ = S.Task('NY12_', length=1, delay_cost=1)
	NY12_ += alt(MAS)

	NY12__mem0 = S.Task('NY12__mem0', length=1, delay_cost=1)
	NY12__mem0 += alt(MM_MEM)
	S += (NY11*MM[0])-1 < NY12__mem0*MM_MEM[0]
	S += NY12__mem0 <= NY12_

	NY12__mem1 = S.Task('NY12__mem1', length=1, delay_cost=1)
	NY12__mem1 += MM_MEM[1]
	S += 85 < NY12__mem1
	S += NY12__mem1 <= NY12_

	DY11_in = S.Task('DY11_in', length=1, delay_cost=1)
	DY11_in += alt(MM_in)
	DY11 = S.Task('DY11', length=6, delay_cost=1)
	DY11 += alt(MM)
	S += DY11>=DY11_in

	DY11_mem0 = S.Task('DY11_mem0', length=1, delay_cost=1)
	DY11_mem0 += alt(MAS_MEM)
	S += (DY11_*MAS[0])-1 < DY11_mem0*MAS_MEM[0]
	S += (DY11_*MAS[1])-1 < DY11_mem0*MAS_MEM[2]
	S += (DY11_*MAS[2])-1 < DY11_mem0*MAS_MEM[4]
	S += (DY11_*MAS[3])-1 < DY11_mem0*MAS_MEM[6]
	S += (DY11_*MAS[4])-1 < DY11_mem0*MAS_MEM[8]
	S += DY11_mem0 <= DY11

	DY11_mem1 = S.Task('DY11_mem1', length=1, delay_cost=1)
	DY11_mem1 += MAIN_MEM_r[1]
	NY12_in = S.Task('NY12_in', length=1, delay_cost=1)
	NY12_in += alt(MM_in)
	NY12 = S.Task('NY12', length=6, delay_cost=1)
	NY12 += alt(MM)
	S += NY12>=NY12_in

	NY12_mem0 = S.Task('NY12_mem0', length=1, delay_cost=1)
	NY12_mem0 += alt(MAS_MEM)
	S += (NY12_*MAS[0])-1 < NY12_mem0*MAS_MEM[0]
	S += (NY12_*MAS[1])-1 < NY12_mem0*MAS_MEM[2]
	S += (NY12_*MAS[2])-1 < NY12_mem0*MAS_MEM[4]
	S += (NY12_*MAS[3])-1 < NY12_mem0*MAS_MEM[6]
	S += (NY12_*MAS[4])-1 < NY12_mem0*MAS_MEM[8]
	S += NY12_mem0 <= NY12

	NY12_mem1 = S.Task('NY12_mem1', length=1, delay_cost=1)
	NY12_mem1 += MAIN_MEM_r[1]
	DY12_ = S.Task('DY12_', length=1, delay_cost=1)
	DY12_ += alt(MAS)

	DY12__mem0 = S.Task('DY12__mem0', length=1, delay_cost=1)
	DY12__mem0 += alt(MM_MEM)
	S += (DY11*MM[0])-1 < DY12__mem0*MM_MEM[0]
	S += DY12__mem0 <= DY12_

	DY12__mem1 = S.Task('DY12__mem1', length=1, delay_cost=1)
	DY12__mem1 += MM_MEM[1]
	S += 92 < DY12__mem1
	S += DY12__mem1 <= DY12_

	NY13_ = S.Task('NY13_', length=1, delay_cost=1)
	NY13_ += alt(MAS)

	NY13__mem0 = S.Task('NY13__mem0', length=1, delay_cost=1)
	NY13__mem0 += alt(MM_MEM)
	S += (NY12*MM[0])-1 < NY13__mem0*MM_MEM[0]
	S += NY13__mem0 <= NY13_

	NY13__mem1 = S.Task('NY13__mem1', length=1, delay_cost=1)
	NY13__mem1 += MM_MEM[1]
	S += 91 < NY13__mem1
	S += NY13__mem1 <= NY13_

	DY12_in = S.Task('DY12_in', length=1, delay_cost=1)
	DY12_in += alt(MM_in)
	DY12 = S.Task('DY12', length=6, delay_cost=1)
	DY12 += alt(MM)
	S += DY12>=DY12_in

	DY12_mem0 = S.Task('DY12_mem0', length=1, delay_cost=1)
	DY12_mem0 += alt(MAS_MEM)
	S += (DY12_*MAS[0])-1 < DY12_mem0*MAS_MEM[0]
	S += (DY12_*MAS[1])-1 < DY12_mem0*MAS_MEM[2]
	S += (DY12_*MAS[2])-1 < DY12_mem0*MAS_MEM[4]
	S += (DY12_*MAS[3])-1 < DY12_mem0*MAS_MEM[6]
	S += (DY12_*MAS[4])-1 < DY12_mem0*MAS_MEM[8]
	S += DY12_mem0 <= DY12

	DY12_mem1 = S.Task('DY12_mem1', length=1, delay_cost=1)
	DY12_mem1 += MAIN_MEM_r[1]
	NY13_in = S.Task('NY13_in', length=1, delay_cost=1)
	NY13_in += alt(MM_in)
	NY13 = S.Task('NY13', length=6, delay_cost=1)
	NY13 += alt(MM)
	S += NY13>=NY13_in

	NY13_mem0 = S.Task('NY13_mem0', length=1, delay_cost=1)
	NY13_mem0 += alt(MAS_MEM)
	S += (NY13_*MAS[0])-1 < NY13_mem0*MAS_MEM[0]
	S += (NY13_*MAS[1])-1 < NY13_mem0*MAS_MEM[2]
	S += (NY13_*MAS[2])-1 < NY13_mem0*MAS_MEM[4]
	S += (NY13_*MAS[3])-1 < NY13_mem0*MAS_MEM[6]
	S += (NY13_*MAS[4])-1 < NY13_mem0*MAS_MEM[8]
	S += NY13_mem0 <= NY13

	NY13_mem1 = S.Task('NY13_mem1', length=1, delay_cost=1)
	NY13_mem1 += MAIN_MEM_r[1]
	DY13_ = S.Task('DY13_', length=1, delay_cost=1)
	DY13_ += alt(MAS)

	DY13__mem0 = S.Task('DY13__mem0', length=1, delay_cost=1)
	DY13__mem0 += alt(MM_MEM)
	S += (DY12*MM[0])-1 < DY13__mem0*MM_MEM[0]
	S += DY13__mem0 <= DY13_

	DY13__mem1 = S.Task('DY13__mem1', length=1, delay_cost=1)
	DY13__mem1 += MM_MEM[1]
	S += 96 < DY13__mem1
	S += DY13__mem1 <= DY13_

	NY14_ = S.Task('NY14_', length=1, delay_cost=1)
	NY14_ += alt(MAS)

	NY14__mem0 = S.Task('NY14__mem0', length=1, delay_cost=1)
	NY14__mem0 += alt(MM_MEM)
	S += (NY13*MM[0])-1 < NY14__mem0*MM_MEM[0]
	S += NY14__mem0 <= NY14_

	NY14__mem1 = S.Task('NY14__mem1', length=1, delay_cost=1)
	NY14__mem1 += MM_MEM[1]
	S += 94 < NY14__mem1
	S += NY14__mem1 <= NY14_

	DY13_in = S.Task('DY13_in', length=1, delay_cost=1)
	DY13_in += alt(MM_in)
	DY13 = S.Task('DY13', length=6, delay_cost=1)
	DY13 += alt(MM)
	S += DY13>=DY13_in

	DY13_mem0 = S.Task('DY13_mem0', length=1, delay_cost=1)
	DY13_mem0 += alt(MAS_MEM)
	S += (DY13_*MAS[0])-1 < DY13_mem0*MAS_MEM[0]
	S += (DY13_*MAS[1])-1 < DY13_mem0*MAS_MEM[2]
	S += (DY13_*MAS[2])-1 < DY13_mem0*MAS_MEM[4]
	S += (DY13_*MAS[3])-1 < DY13_mem0*MAS_MEM[6]
	S += (DY13_*MAS[4])-1 < DY13_mem0*MAS_MEM[8]
	S += DY13_mem0 <= DY13

	DY13_mem1 = S.Task('DY13_mem1', length=1, delay_cost=1)
	DY13_mem1 += MAIN_MEM_r[1]
	NY14_in = S.Task('NY14_in', length=1, delay_cost=1)
	NY14_in += alt(MM_in)
	NY14 = S.Task('NY14', length=6, delay_cost=1)
	NY14 += alt(MM)
	S += NY14>=NY14_in

	NY14_mem0 = S.Task('NY14_mem0', length=1, delay_cost=1)
	NY14_mem0 += alt(MAS_MEM)
	S += (NY14_*MAS[0])-1 < NY14_mem0*MAS_MEM[0]
	S += (NY14_*MAS[1])-1 < NY14_mem0*MAS_MEM[2]
	S += (NY14_*MAS[2])-1 < NY14_mem0*MAS_MEM[4]
	S += (NY14_*MAS[3])-1 < NY14_mem0*MAS_MEM[6]
	S += (NY14_*MAS[4])-1 < NY14_mem0*MAS_MEM[8]
	S += NY14_mem0 <= NY14

	NY14_mem1 = S.Task('NY14_mem1', length=1, delay_cost=1)
	NY14_mem1 += MAIN_MEM_r[1]
	DY14_ = S.Task('DY14_', length=1, delay_cost=1)
	DY14_ += alt(MAS)

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

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS5/ISOGENY/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

