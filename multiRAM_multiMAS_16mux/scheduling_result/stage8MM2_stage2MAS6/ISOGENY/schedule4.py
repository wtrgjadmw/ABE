from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 271
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=8)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
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

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 1
	NX0_in += MM_in[1]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 1
	NX0_mem0 += MAIN_MEM_r[0]

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 1
	NX0_mem1 += MAIN_MEM_r[1]

	Z_exp2 = S.Task('Z_exp2', length=8, delay_cost=1)
	S += Z_exp2 >= 1
	Z_exp2 += MM[0]

	NX0 = S.Task('NX0', length=8, delay_cost=1)
	S += NX0 >= 2
	NX0 += MM[1]

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 2
	k0_10_Z1_in += MM_in[1]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 2
	k0_10_Z1_mem0 += MAIN_MEM_r[0]

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 2
	k0_10_Z1_mem1 += MAIN_MEM_r[1]

	k0_10_Z1 = S.Task('k0_10_Z1', length=8, delay_cost=1)
	S += k0_10_Z1 >= 3
	k0_10_Z1 += MM[1]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 3
	k2_14_Z1_in += MM_in[1]

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

	k2_14_Z1 = S.Task('k2_14_Z1', length=8, delay_cost=1)
	S += k2_14_Z1 >= 4
	k2_14_Z1 += MM[1]

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 5
	DY0_in += MM_in[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 5
	DY0_mem0 += MAIN_MEM_r[0]

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 5
	DY0_mem1 += MAIN_MEM_r[1]

	NY0 = S.Task('NY0', length=8, delay_cost=1)
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

	DY0 = S.Task('DY0', length=8, delay_cost=1)
	S += DY0 >= 6
	DY0 += MM[0]

	DX0 = S.Task('DX0', length=8, delay_cost=1)
	S += DX0 >= 7
	DX0 += MM[0]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 8
	Z_exp3_in += MM_in[1]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 8
	Z_exp3_mem0 += MM_MEM[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 8
	Z_exp3_mem1 += MAIN_MEM_r[1]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 8
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 8
	k3_14_Z2_mem0 += MAIN_MEM_r[0]

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 8
	k3_14_Z2_mem1 += MM_MEM[1]

	Z_exp3 = S.Task('Z_exp3', length=8, delay_cost=1)
	S += Z_exp3 >= 9
	Z_exp3 += MM[1]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 9
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 9
	k1_9_Z2_mem0 += MAIN_MEM_r[0]

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 9
	k1_9_Z2_mem1 += MM_MEM[1]

	k3_14_Z2 = S.Task('k3_14_Z2', length=8, delay_cost=1)
	S += k3_14_Z2 >= 9
	k3_14_Z2 += MM[0]

	NX1__in = S.Task('NX1__in', length=1, delay_cost=1)
	S += NX1__in >= 10
	NX1__in += MAS_in[2]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 10
	NX1__mem0 += MM_MEM[2]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 10
	NX1__mem1 += MM_MEM[3]

	k1_9_Z2 = S.Task('k1_9_Z2', length=8, delay_cost=1)
	S += k1_9_Z2 >= 10
	k1_9_Z2 += MM[0]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 10
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 10
	k2_13_Z2_mem0 += MAIN_MEM_r[0]

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 10
	k2_13_Z2_mem1 += MM_MEM[1]

	NX1_ = S.Task('NX1_', length=2, delay_cost=1)
	S += NX1_ >= 11
	NX1_ += MAS[2]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 11
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 11
	k0_9_Z2_mem0 += MAIN_MEM_r[0]

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 11
	k0_9_Z2_mem1 += MM_MEM[1]

	k2_13_Z2 = S.Task('k2_13_Z2', length=8, delay_cost=1)
	S += k2_13_Z2 >= 11
	k2_13_Z2 += MM[0]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 12
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 12
	NX1_mem0 += MAS_MEM[4]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 12
	NX1_mem1 += MAIN_MEM_r[1]

	NY1__in = S.Task('NY1__in', length=1, delay_cost=1)
	S += NY1__in >= 12
	NY1__in += MAS_in[4]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 12
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 12
	NY1__mem1 += MM_MEM[3]

	k0_9_Z2 = S.Task('k0_9_Z2', length=8, delay_cost=1)
	S += k0_9_Z2 >= 12
	k0_9_Z2 += MM[0]

	NX1 = S.Task('NX1', length=8, delay_cost=1)
	S += NX1 >= 13
	NX1 += MM[0]

	NY1_ = S.Task('NY1_', length=2, delay_cost=1)
	S += NY1_ >= 13
	NY1_ += MAS[4]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 14
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 14
	NY1_mem0 += MAS_MEM[8]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 14
	NY1_mem1 += MAIN_MEM_r[1]

	NY1 = S.Task('NY1', length=8, delay_cost=1)
	S += NY1 >= 15
	NY1 += MM[0]

	DY1__in = S.Task('DY1__in', length=1, delay_cost=1)
	S += DY1__in >= 16
	DY1__in += MAS_in[2]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 16
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 16
	DY1__mem1 += MM_MEM[1]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 16
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 16
	Z_exp4_mem0 += MM_MEM[2]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 16
	Z_exp4_mem1 += MAIN_MEM_r[1]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 16
	k1_8_Z3_in += MM_in[1]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 16
	k1_8_Z3_mem0 += MAIN_MEM_r[0]

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 16
	k1_8_Z3_mem1 += MM_MEM[3]

	DX1__in = S.Task('DX1__in', length=1, delay_cost=1)
	S += DX1__in >= 17
	DX1__in += MAS_in[5]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 17
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 17
	DX1__mem1 += MM_MEM[1]

	DY1_ = S.Task('DY1_', length=2, delay_cost=1)
	S += DY1_ >= 17
	DY1_ += MAS[2]

	Z_exp4 = S.Task('Z_exp4', length=8, delay_cost=1)
	S += Z_exp4 >= 17
	Z_exp4 += MM[0]

	k1_8_Z3 = S.Task('k1_8_Z3', length=8, delay_cost=1)
	S += k1_8_Z3 >= 17
	k1_8_Z3 += MM[1]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 17
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 17
	k3_13_Z3_mem0 += MAIN_MEM_r[0]

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 17
	k3_13_Z3_mem1 += MM_MEM[3]

	DX1_ = S.Task('DX1_', length=2, delay_cost=1)
	S += DX1_ >= 18
	DX1_ += MAS[5]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 18
	DY1_in += MM_in[1]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 18
	DY1_mem0 += MAS_MEM[4]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 18
	DY1_mem1 += MAIN_MEM_r[1]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 18
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 18
	k0_8_Z3_mem0 += MAIN_MEM_r[0]

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 18
	k0_8_Z3_mem1 += MM_MEM[3]

	k3_13_Z3 = S.Task('k3_13_Z3', length=8, delay_cost=1)
	S += k3_13_Z3 >= 18
	k3_13_Z3 += MM[0]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 19
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 19
	DX1_mem0 += MAS_MEM[10]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 19
	DX1_mem1 += MAIN_MEM_r[1]

	DY1 = S.Task('DY1', length=8, delay_cost=1)
	S += DY1 >= 19
	DY1 += MM[1]

	k0_8_Z3 = S.Task('k0_8_Z3', length=8, delay_cost=1)
	S += k0_8_Z3 >= 19
	k0_8_Z3 += MM[0]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 19
	k2_12_Z3_in += MM_in[1]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 19
	k2_12_Z3_mem0 += MAIN_MEM_r[0]

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 19
	k2_12_Z3_mem1 += MM_MEM[3]

	DX1 = S.Task('DX1', length=8, delay_cost=1)
	S += DX1 >= 20
	DX1 += MM[0]

	NX2__in = S.Task('NX2__in', length=1, delay_cost=1)
	S += NX2__in >= 20
	NX2__in += MAS_in[5]

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 20
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 20
	NX2__mem1 += MM_MEM[1]

	k2_12_Z3 = S.Task('k2_12_Z3', length=8, delay_cost=1)
	S += k2_12_Z3 >= 20
	k2_12_Z3 += MM[1]

	NX2_ = S.Task('NX2_', length=2, delay_cost=1)
	S += NX2_ >= 21
	NX2_ += MAS[5]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 22
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 22
	NX2_mem0 += MAS_MEM[10]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 22
	NX2_mem1 += MAIN_MEM_r[1]

	NY2__in = S.Task('NY2__in', length=1, delay_cost=1)
	S += NY2__in >= 22
	NY2__in += MAS_in[0]

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 22
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 22
	NY2__mem1 += MM_MEM[1]

	NX2 = S.Task('NX2', length=8, delay_cost=1)
	S += NX2 >= 23
	NX2 += MM[0]

	NY2_ = S.Task('NY2_', length=2, delay_cost=1)
	S += NY2_ >= 23
	NY2_ += MAS[0]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 24
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 24
	Z_exp5_mem0 += MM_MEM[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 24
	Z_exp5_mem1 += MAIN_MEM_r[1]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 24
	k1_7_Z4_in += MM_in[1]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 24
	k1_7_Z4_mem0 += MAIN_MEM_r[0]

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 24
	k1_7_Z4_mem1 += MM_MEM[1]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 25
	NY2_in += MM_in[1]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 25
	NY2_mem0 += MAS_MEM[0]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 25
	NY2_mem1 += MAIN_MEM_r[1]

	Z_exp5 = S.Task('Z_exp5', length=8, delay_cost=1)
	S += Z_exp5 >= 25
	Z_exp5 += MM[0]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 25
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 25
	k0_7_Z4_mem0 += MAIN_MEM_r[0]

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 25
	k0_7_Z4_mem1 += MM_MEM[1]

	k1_7_Z4 = S.Task('k1_7_Z4', length=8, delay_cost=1)
	S += k1_7_Z4 >= 25
	k1_7_Z4 += MM[1]

	DY2__in = S.Task('DY2__in', length=1, delay_cost=1)
	S += DY2__in >= 26
	DY2__in += MAS_in[1]

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 26
	DY2__mem0 += MM_MEM[2]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 26
	DY2__mem1 += MM_MEM[1]

	NY2 = S.Task('NY2', length=8, delay_cost=1)
	S += NY2 >= 26
	NY2 += MM[1]

	k0_7_Z4 = S.Task('k0_7_Z4', length=8, delay_cost=1)
	S += k0_7_Z4 >= 26
	k0_7_Z4 += MM[0]

	DX2__in = S.Task('DX2__in', length=1, delay_cost=1)
	S += DX2__in >= 27
	DX2__in += MAS_in[1]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 27
	DX2__mem0 += MM_MEM[0]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 27
	DX2__mem1 += MM_MEM[3]

	DY2_ = S.Task('DY2_', length=2, delay_cost=1)
	S += DY2_ >= 27
	DY2_ += MAS[1]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 27
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 27
	k2_11_Z4_mem0 += MAIN_MEM_r[0]

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 27
	k2_11_Z4_mem1 += MM_MEM[1]

	DX2_ = S.Task('DX2_', length=2, delay_cost=1)
	S += DX2_ >= 28
	DX2_ += MAS[1]

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 28
	DY2_in += MM_in[1]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 28
	DY2_mem0 += MAS_MEM[2]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 28
	DY2_mem1 += MAIN_MEM_r[1]

	k2_11_Z4 = S.Task('k2_11_Z4', length=8, delay_cost=1)
	S += k2_11_Z4 >= 28
	k2_11_Z4 += MM[0]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 28
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 28
	k3_12_Z4_mem0 += MAIN_MEM_r[0]

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 28
	k3_12_Z4_mem1 += MM_MEM[1]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 29
	DX2_in += MM_in[0]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 29
	DX2_mem0 += MAS_MEM[2]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 29
	DX2_mem1 += MAIN_MEM_r[1]

	DY2 = S.Task('DY2', length=8, delay_cost=1)
	S += DY2 >= 29
	DY2 += MM[1]

	k3_12_Z4 = S.Task('k3_12_Z4', length=8, delay_cost=1)
	S += k3_12_Z4 >= 29
	k3_12_Z4 += MM[0]

	DX2 = S.Task('DX2', length=8, delay_cost=1)
	S += DX2 >= 30
	DX2 += MM[0]

	NX3__in = S.Task('NX3__in', length=1, delay_cost=1)
	S += NX3__in >= 30
	NX3__in += MAS_in[3]

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 30
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 30
	NX3__mem1 += MM_MEM[1]

	NX3_ = S.Task('NX3_', length=2, delay_cost=1)
	S += NX3_ >= 31
	NX3_ += MAS[3]

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	S += Z_exp6_in >= 32
	Z_exp6_in += MM_in[1]

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	S += Z_exp6_mem0 >= 32
	Z_exp6_mem0 += MM_MEM[0]

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	S += Z_exp6_mem1 >= 32
	Z_exp6_mem1 += MAIN_MEM_r[1]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 32
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 32
	k3_11_Z5_mem0 += MAIN_MEM_r[0]

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 32
	k3_11_Z5_mem1 += MM_MEM[1]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 33
	NX3_in += MM_in[1]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 33
	NX3_mem0 += MAS_MEM[6]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 33
	NX3_mem1 += MAIN_MEM_r[1]

	NY3__in = S.Task('NY3__in', length=1, delay_cost=1)
	S += NY3__in >= 33
	NY3__in += MAS_in[3]

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 33
	NY3__mem0 += MM_MEM[2]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 33
	NY3__mem1 += MM_MEM[3]

	Z_exp6 = S.Task('Z_exp6', length=8, delay_cost=1)
	S += Z_exp6 >= 33
	Z_exp6 += MM[1]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 33
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 33
	k2_10_Z5_mem0 += MAIN_MEM_r[0]

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 33
	k2_10_Z5_mem1 += MM_MEM[1]

	k3_11_Z5 = S.Task('k3_11_Z5', length=8, delay_cost=1)
	S += k3_11_Z5 >= 33
	k3_11_Z5 += MM[0]

	NX3 = S.Task('NX3', length=8, delay_cost=1)
	S += NX3 >= 34
	NX3 += MM[1]

	NY3_ = S.Task('NY3_', length=2, delay_cost=1)
	S += NY3_ >= 34
	NY3_ += MAS[3]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 34
	k0_6_Z5_in += MM_in[1]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 34
	k0_6_Z5_mem0 += MAIN_MEM_r[0]

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 34
	k0_6_Z5_mem1 += MM_MEM[1]

	k2_10_Z5 = S.Task('k2_10_Z5', length=8, delay_cost=1)
	S += k2_10_Z5 >= 34
	k2_10_Z5 += MM[0]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 35
	NY3_in += MM_in[0]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 35
	NY3_mem0 += MAS_MEM[6]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 35
	NY3_mem1 += MAIN_MEM_r[1]

	k0_6_Z5 = S.Task('k0_6_Z5', length=8, delay_cost=1)
	S += k0_6_Z5 >= 35
	k0_6_Z5 += MM[1]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 35
	k1_6_Z5_in += MM_in[1]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 35
	k1_6_Z5_mem0 += MAIN_MEM_r[0]

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 35
	k1_6_Z5_mem1 += MM_MEM[1]

	DY3__in = S.Task('DY3__in', length=1, delay_cost=1)
	S += DY3__in >= 36
	DY3__in += MAS_in[0]

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	S += DY3__mem0 >= 36
	DY3__mem0 += MM_MEM[2]

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	S += DY3__mem1 >= 36
	DY3__mem1 += MM_MEM[1]

	NY3 = S.Task('NY3', length=8, delay_cost=1)
	S += NY3 >= 36
	NY3 += MM[0]

	k1_6_Z5 = S.Task('k1_6_Z5', length=8, delay_cost=1)
	S += k1_6_Z5 >= 36
	k1_6_Z5 += MM[1]

	DX3__in = S.Task('DX3__in', length=1, delay_cost=1)
	S += DX3__in >= 37
	DX3__in += MAS_in[4]

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	S += DX3__mem0 >= 37
	DX3__mem0 += MM_MEM[0]

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	S += DX3__mem1 >= 37
	DX3__mem1 += MM_MEM[3]

	DY3_ = S.Task('DY3_', length=2, delay_cost=1)
	S += DY3_ >= 37
	DY3_ += MAS[0]

	DX3_ = S.Task('DX3_', length=2, delay_cost=1)
	S += DX3_ >= 38
	DX3_ += MAS[4]

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	S += DY3_in >= 38
	DY3_in += MM_in[0]

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	S += DY3_mem0 >= 38
	DY3_mem0 += MAS_MEM[0]

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	S += DY3_mem1 >= 38
	DY3_mem1 += MAIN_MEM_r[1]

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	S += DX3_in >= 39
	DX3_in += MM_in[0]

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	S += DX3_mem0 >= 39
	DX3_mem0 += MAS_MEM[8]

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	S += DX3_mem1 >= 39
	DX3_mem1 += MAIN_MEM_r[1]

	DY3 = S.Task('DY3', length=8, delay_cost=1)
	S += DY3 >= 39
	DY3 += MM[0]

	DX3 = S.Task('DX3', length=8, delay_cost=1)
	S += DX3 >= 40
	DX3 += MM[0]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 40
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 40
	Z_exp7_mem0 += MM_MEM[2]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 40
	Z_exp7_mem1 += MAIN_MEM_r[1]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 40
	k1_5_Z6_in += MM_in[1]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 40
	k1_5_Z6_mem0 += MAIN_MEM_r[0]

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 40
	k1_5_Z6_mem1 += MM_MEM[3]

	NX4__in = S.Task('NX4__in', length=1, delay_cost=1)
	S += NX4__in >= 41
	NX4__in += MAS_in[0]

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 41
	NX4__mem0 += MM_MEM[2]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 41
	NX4__mem1 += MM_MEM[1]

	Z_exp7 = S.Task('Z_exp7', length=8, delay_cost=1)
	S += Z_exp7 >= 41
	Z_exp7 += MM[0]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 41
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 41
	k0_5_Z6_mem0 += MAIN_MEM_r[0]

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 41
	k0_5_Z6_mem1 += MM_MEM[3]

	k1_5_Z6 = S.Task('k1_5_Z6', length=8, delay_cost=1)
	S += k1_5_Z6 >= 41
	k1_5_Z6 += MM[1]

	NX4_ = S.Task('NX4_', length=2, delay_cost=1)
	S += NX4_ >= 42
	NX4_ += MAS[0]

	k0_5_Z6 = S.Task('k0_5_Z6', length=8, delay_cost=1)
	S += k0_5_Z6 >= 42
	k0_5_Z6 += MM[0]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 42
	k2_9_Z6_in += MM_in[1]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 42
	k2_9_Z6_mem0 += MAIN_MEM_r[0]

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 42
	k2_9_Z6_mem1 += MM_MEM[3]

	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	S += NX4_in >= 43
	NX4_in += MM_in[0]

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	S += NX4_mem0 >= 43
	NX4_mem0 += MAS_MEM[0]

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	S += NX4_mem1 >= 43
	NX4_mem1 += MAIN_MEM_r[1]

	NY4__in = S.Task('NY4__in', length=1, delay_cost=1)
	S += NY4__in >= 43
	NY4__in += MAS_in[0]

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 43
	NY4__mem0 += MM_MEM[0]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 43
	NY4__mem1 += MM_MEM[1]

	k2_9_Z6 = S.Task('k2_9_Z6', length=8, delay_cost=1)
	S += k2_9_Z6 >= 43
	k2_9_Z6 += MM[1]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 43
	k3_10_Z6_in += MM_in[1]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 43
	k3_10_Z6_mem0 += MAIN_MEM_r[0]

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 43
	k3_10_Z6_mem1 += MM_MEM[3]

	NX4 = S.Task('NX4', length=8, delay_cost=1)
	S += NX4 >= 44
	NX4 += MM[0]

	NY4_ = S.Task('NY4_', length=2, delay_cost=1)
	S += NY4_ >= 44
	NY4_ += MAS[0]

	k3_10_Z6 = S.Task('k3_10_Z6', length=8, delay_cost=1)
	S += k3_10_Z6 >= 44
	k3_10_Z6 += MM[1]

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	S += NY4_in >= 45
	NY4_in += MM_in[1]

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	S += NY4_mem0 >= 45
	NY4_mem0 += MAS_MEM[0]

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	S += NY4_mem1 >= 45
	NY4_mem1 += MAIN_MEM_r[1]

	DY4__in = S.Task('DY4__in', length=1, delay_cost=1)
	S += DY4__in >= 46
	DY4__in += MAS_in[2]

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	S += DY4__mem0 >= 46
	DY4__mem0 += MM_MEM[0]

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	S += DY4__mem1 >= 46
	DY4__mem1 += MM_MEM[1]

	NY4 = S.Task('NY4', length=8, delay_cost=1)
	S += NY4 >= 46
	NY4 += MM[1]

	DX4__in = S.Task('DX4__in', length=1, delay_cost=1)
	S += DX4__in >= 47
	DX4__in += MAS_in[0]

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	S += DX4__mem0 >= 47
	DX4__mem0 += MM_MEM[0]

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	S += DX4__mem1 >= 47
	DX4__mem1 += MM_MEM[3]

	DY4_ = S.Task('DY4_', length=2, delay_cost=1)
	S += DY4_ >= 47
	DY4_ += MAS[2]

	DX4_ = S.Task('DX4_', length=2, delay_cost=1)
	S += DX4_ >= 48
	DX4_ += MAS[0]

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	S += Z_exp8_in >= 48
	Z_exp8_in += MM_in[0]

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	S += Z_exp8_mem0 >= 48
	Z_exp8_mem0 += MM_MEM[0]

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	S += Z_exp8_mem1 >= 48
	Z_exp8_mem1 += MAIN_MEM_r[1]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 48
	k1_4_Z7_in += MM_in[1]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 48
	k1_4_Z7_mem0 += MAIN_MEM_r[0]

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 48
	k1_4_Z7_mem1 += MM_MEM[1]

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	S += DY4_in >= 49
	DY4_in += MM_in[0]

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	S += DY4_mem0 >= 49
	DY4_mem0 += MAS_MEM[4]

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	S += DY4_mem1 >= 49
	DY4_mem1 += MAIN_MEM_r[1]

	Z_exp8 = S.Task('Z_exp8', length=8, delay_cost=1)
	S += Z_exp8 >= 49
	Z_exp8 += MM[0]

	k1_4_Z7 = S.Task('k1_4_Z7', length=8, delay_cost=1)
	S += k1_4_Z7 >= 49
	k1_4_Z7 += MM[1]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 49
	k3_9_Z7_in += MM_in[1]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 49
	k3_9_Z7_mem0 += MAIN_MEM_r[0]

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 49
	k3_9_Z7_mem1 += MM_MEM[1]

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	S += DX4_in >= 50
	DX4_in += MM_in[1]

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	S += DX4_mem0 >= 50
	DX4_mem0 += MAS_MEM[0]

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	S += DX4_mem1 >= 50
	DX4_mem1 += MAIN_MEM_r[1]

	DY4 = S.Task('DY4', length=8, delay_cost=1)
	S += DY4 >= 50
	DY4 += MM[0]

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	S += k0_4_Z7_in >= 50
	k0_4_Z7_in += MM_in[0]

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	S += k0_4_Z7_mem0 >= 50
	k0_4_Z7_mem0 += MAIN_MEM_r[0]

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	S += k0_4_Z7_mem1 >= 50
	k0_4_Z7_mem1 += MM_MEM[1]

	k3_9_Z7 = S.Task('k3_9_Z7', length=8, delay_cost=1)
	S += k3_9_Z7 >= 50
	k3_9_Z7 += MM[1]

	DX4 = S.Task('DX4', length=8, delay_cost=1)
	S += DX4 >= 51
	DX4 += MM[1]

	NX5__in = S.Task('NX5__in', length=1, delay_cost=1)
	S += NX5__in >= 51
	NX5__in += MAS_in[2]

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	S += NX5__mem0 >= 51
	NX5__mem0 += MM_MEM[0]

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	S += NX5__mem1 >= 51
	NX5__mem1 += MM_MEM[3]

	k0_4_Z7 = S.Task('k0_4_Z7', length=8, delay_cost=1)
	S += k0_4_Z7 >= 51
	k0_4_Z7 += MM[0]

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	S += k2_8_Z7_in >= 51
	k2_8_Z7_in += MM_in[1]

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	S += k2_8_Z7_mem0 >= 51
	k2_8_Z7_mem0 += MAIN_MEM_r[0]

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	S += k2_8_Z7_mem1 >= 51
	k2_8_Z7_mem1 += MM_MEM[1]

	NX5_ = S.Task('NX5_', length=2, delay_cost=1)
	S += NX5_ >= 52
	NX5_ += MAS[2]

	k2_8_Z7 = S.Task('k2_8_Z7', length=8, delay_cost=1)
	S += k2_8_Z7 >= 52
	k2_8_Z7 += MM[1]

	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	S += NX5_in >= 53
	NX5_in += MM_in[1]

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	S += NX5_mem0 >= 53
	NX5_mem0 += MAS_MEM[4]

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	S += NX5_mem1 >= 53
	NX5_mem1 += MAIN_MEM_r[1]

	NY5__in = S.Task('NY5__in', length=1, delay_cost=1)
	S += NY5__in >= 53
	NY5__in += MAS_in[1]

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	S += NY5__mem0 >= 53
	NY5__mem0 += MM_MEM[2]

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	S += NY5__mem1 >= 53
	NY5__mem1 += MM_MEM[1]

	NX5 = S.Task('NX5', length=8, delay_cost=1)
	S += NX5 >= 54
	NX5 += MM[1]

	NY5_ = S.Task('NY5_', length=2, delay_cost=1)
	S += NY5_ >= 54
	NY5_ += MAS[1]

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	S += NY5_in >= 55
	NY5_in += MM_in[1]

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	S += NY5_mem0 >= 55
	NY5_mem0 += MAS_MEM[2]

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	S += NY5_mem1 >= 55
	NY5_mem1 += MAIN_MEM_r[1]

	NY5 = S.Task('NY5', length=8, delay_cost=1)
	S += NY5 >= 56
	NY5 += MM[1]

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	S += Z_exp9_in >= 56
	Z_exp9_in += MM_in[1]

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	S += Z_exp9_mem0 >= 56
	Z_exp9_mem0 += MM_MEM[0]

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	S += Z_exp9_mem1 >= 56
	Z_exp9_mem1 += MAIN_MEM_r[1]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 56
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 56
	k1_3_Z8_mem0 += MAIN_MEM_r[0]

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 56
	k1_3_Z8_mem1 += MM_MEM[1]

	DY5__in = S.Task('DY5__in', length=1, delay_cost=1)
	S += DY5__in >= 57
	DY5__in += MAS_in[3]

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	S += DY5__mem0 >= 57
	DY5__mem0 += MM_MEM[0]

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	S += DY5__mem1 >= 57
	DY5__mem1 += MM_MEM[3]

	Z_exp9 = S.Task('Z_exp9', length=8, delay_cost=1)
	S += Z_exp9 >= 57
	Z_exp9 += MM[1]

	k1_3_Z8 = S.Task('k1_3_Z8', length=8, delay_cost=1)
	S += k1_3_Z8 >= 57
	k1_3_Z8 += MM[0]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 57
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 57
	k2_7_Z8_mem0 += MAIN_MEM_r[0]

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 57
	k2_7_Z8_mem1 += MM_MEM[1]

	DX5__in = S.Task('DX5__in', length=1, delay_cost=1)
	S += DX5__in >= 58
	DX5__in += MAS_in[1]

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	S += DX5__mem0 >= 58
	DX5__mem0 += MM_MEM[2]

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	S += DX5__mem1 >= 58
	DX5__mem1 += MM_MEM[3]

	DY5_ = S.Task('DY5_', length=2, delay_cost=1)
	S += DY5_ >= 58
	DY5_ += MAS[3]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 58
	k0_3_Z8_in += MM_in[1]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 58
	k0_3_Z8_mem0 += MAIN_MEM_r[0]

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 58
	k0_3_Z8_mem1 += MM_MEM[1]

	k2_7_Z8 = S.Task('k2_7_Z8', length=8, delay_cost=1)
	S += k2_7_Z8 >= 58
	k2_7_Z8 += MM[0]

	DX5_ = S.Task('DX5_', length=2, delay_cost=1)
	S += DX5_ >= 59
	DX5_ += MAS[1]

	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	S += DY5_in >= 59
	DY5_in += MM_in[0]

	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	S += DY5_mem0 >= 59
	DY5_mem0 += MAS_MEM[6]

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	S += DY5_mem1 >= 59
	DY5_mem1 += MAIN_MEM_r[1]

	k0_3_Z8 = S.Task('k0_3_Z8', length=8, delay_cost=1)
	S += k0_3_Z8 >= 59
	k0_3_Z8 += MM[1]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 59
	k3_8_Z8_in += MM_in[1]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 59
	k3_8_Z8_mem0 += MAIN_MEM_r[0]

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 59
	k3_8_Z8_mem1 += MM_MEM[1]

	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	S += DX5_in >= 60
	DX5_in += MM_in[0]

	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	S += DX5_mem0 >= 60
	DX5_mem0 += MAS_MEM[2]

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	S += DX5_mem1 >= 60
	DX5_mem1 += MAIN_MEM_r[1]

	DY5 = S.Task('DY5', length=8, delay_cost=1)
	S += DY5 >= 60
	DY5 += MM[0]

	k3_8_Z8 = S.Task('k3_8_Z8', length=8, delay_cost=1)
	S += k3_8_Z8 >= 60
	k3_8_Z8 += MM[1]

	DX5 = S.Task('DX5', length=8, delay_cost=1)
	S += DX5 >= 61
	DX5 += MM[0]

	NX6__in = S.Task('NX6__in', length=1, delay_cost=1)
	S += NX6__in >= 61
	NX6__in += MAS_in[0]

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	S += NX6__mem0 >= 61
	NX6__mem0 += MM_MEM[2]

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	S += NX6__mem1 >= 61
	NX6__mem1 += MM_MEM[1]

	NX6_ = S.Task('NX6_', length=2, delay_cost=1)
	S += NX6_ >= 62
	NX6_ += MAS[0]

	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	S += NX6_in >= 63
	NX6_in += MM_in[1]

	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	S += NX6_mem0 >= 63
	NX6_mem0 += MAS_MEM[0]

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	S += NX6_mem1 >= 63
	NX6_mem1 += MAIN_MEM_r[1]

	NY6__in = S.Task('NY6__in', length=1, delay_cost=1)
	S += NY6__in >= 63
	NY6__in += MAS_in[5]

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	S += NY6__mem0 >= 63
	NY6__mem0 += MM_MEM[2]

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	S += NY6__mem1 >= 63
	NY6__mem1 += MM_MEM[3]

	NX6 = S.Task('NX6', length=8, delay_cost=1)
	S += NX6 >= 64
	NX6 += MM[1]

	NY6_ = S.Task('NY6_', length=2, delay_cost=1)
	S += NY6_ >= 64
	NY6_ += MAS[5]

	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	S += Z_exp10_in >= 64
	Z_exp10_in += MM_in[0]

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	S += Z_exp10_mem0 >= 64
	Z_exp10_mem0 += MM_MEM[2]

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	S += Z_exp10_mem1 >= 64
	Z_exp10_mem1 += MAIN_MEM_r[1]

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	S += k3_7_Z9_in >= 64
	k3_7_Z9_in += MM_in[1]

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	S += k3_7_Z9_mem0 >= 64
	k3_7_Z9_mem0 += MAIN_MEM_r[0]

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	S += k3_7_Z9_mem1 >= 64
	k3_7_Z9_mem1 += MM_MEM[3]

	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	S += NY6_in >= 65
	NY6_in += MM_in[1]

	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	S += NY6_mem0 >= 65
	NY6_mem0 += MAS_MEM[10]

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	S += NY6_mem1 >= 65
	NY6_mem1 += MAIN_MEM_r[1]

	Z_exp10 = S.Task('Z_exp10', length=8, delay_cost=1)
	S += Z_exp10 >= 65
	Z_exp10 += MM[0]

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	S += k1_2_Z9_in >= 65
	k1_2_Z9_in += MM_in[0]

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	S += k1_2_Z9_mem0 >= 65
	k1_2_Z9_mem0 += MAIN_MEM_r[0]

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	S += k1_2_Z9_mem1 >= 65
	k1_2_Z9_mem1 += MM_MEM[3]

	k3_7_Z9 = S.Task('k3_7_Z9', length=8, delay_cost=1)
	S += k3_7_Z9 >= 65
	k3_7_Z9 += MM[1]

	NY6 = S.Task('NY6', length=8, delay_cost=1)
	S += NY6 >= 66
	NY6 += MM[1]

	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	S += k0_2_Z9_in >= 66
	k0_2_Z9_in += MM_in[1]

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	S += k0_2_Z9_mem0 >= 66
	k0_2_Z9_mem0 += MAIN_MEM_r[0]

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	S += k0_2_Z9_mem1 >= 66
	k0_2_Z9_mem1 += MM_MEM[3]

	k1_2_Z9 = S.Task('k1_2_Z9', length=8, delay_cost=1)
	S += k1_2_Z9 >= 66
	k1_2_Z9 += MM[0]

	DY6__in = S.Task('DY6__in', length=1, delay_cost=1)
	S += DY6__in >= 67
	DY6__in += MAS_in[5]

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	S += DY6__mem0 >= 67
	DY6__mem0 += MM_MEM[0]

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	S += DY6__mem1 >= 67
	DY6__mem1 += MM_MEM[3]

	k0_2_Z9 = S.Task('k0_2_Z9', length=8, delay_cost=1)
	S += k0_2_Z9 >= 67
	k0_2_Z9 += MM[1]

	DX6__in = S.Task('DX6__in', length=1, delay_cost=1)
	S += DX6__in >= 68
	DX6__in += MAS_in[4]

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	S += DX6__mem0 >= 68
	DX6__mem0 += MM_MEM[0]

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	S += DX6__mem1 >= 68
	DX6__mem1 += MM_MEM[3]

	DY6_ = S.Task('DY6_', length=2, delay_cost=1)
	S += DY6_ >= 68
	DY6_ += MAS[5]

	DX6_ = S.Task('DX6_', length=2, delay_cost=1)
	S += DX6_ >= 69
	DX6_ += MAS[4]

	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	S += DY6_in >= 69
	DY6_in += MM_in[1]

	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	S += DY6_mem0 >= 69
	DY6_mem0 += MAS_MEM[10]

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	S += DY6_mem1 >= 69
	DY6_mem1 += MAIN_MEM_r[1]

	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	S += k2_6_Z9_in >= 69
	k2_6_Z9_in += MM_in[0]

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	S += k2_6_Z9_mem0 >= 69
	k2_6_Z9_mem0 += MAIN_MEM_r[0]

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	S += k2_6_Z9_mem1 >= 69
	k2_6_Z9_mem1 += MM_MEM[3]

	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	S += DX6_in >= 70
	DX6_in += MM_in[1]

	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	S += DX6_mem0 >= 70
	DX6_mem0 += MAS_MEM[8]

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	S += DX6_mem1 >= 70
	DX6_mem1 += MAIN_MEM_r[1]

	DY6 = S.Task('DY6', length=8, delay_cost=1)
	S += DY6 >= 70
	DY6 += MM[1]

	k2_6_Z9 = S.Task('k2_6_Z9', length=8, delay_cost=1)
	S += k2_6_Z9 >= 70
	k2_6_Z9 += MM[0]

	DX6 = S.Task('DX6', length=8, delay_cost=1)
	S += DX6 >= 71
	DX6 += MM[1]

	NX7__in = S.Task('NX7__in', length=1, delay_cost=1)
	S += NX7__in >= 71
	NX7__in += MAS_in[2]

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	S += NX7__mem0 >= 71
	NX7__mem0 += MM_MEM[2]

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	S += NX7__mem1 >= 71
	NX7__mem1 += MM_MEM[1]

	NX7_ = S.Task('NX7_', length=2, delay_cost=1)
	S += NX7_ >= 72
	NX7_ += MAS[2]

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	S += Z_exp11_in >= 72
	Z_exp11_in += MM_in[1]

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	S += Z_exp11_mem0 >= 72
	Z_exp11_mem0 += MM_MEM[0]

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	S += Z_exp11_mem1 >= 72
	Z_exp11_mem1 += MAIN_MEM_r[1]

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	S += k0_1_Z10_in >= 72
	k0_1_Z10_in += MM_in[0]

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	S += k0_1_Z10_mem0 >= 72
	k0_1_Z10_mem0 += MAIN_MEM_r[0]

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	S += k0_1_Z10_mem1 >= 72
	k0_1_Z10_mem1 += MM_MEM[1]

	NX7_in = S.Task('NX7_in', length=1, delay_cost=1)
	S += NX7_in >= 73
	NX7_in += MM_in[0]

	NX7_mem0 = S.Task('NX7_mem0', length=1, delay_cost=1)
	S += NX7_mem0 >= 73
	NX7_mem0 += MAS_MEM[4]

	NX7_mem1 = S.Task('NX7_mem1', length=1, delay_cost=1)
	S += NX7_mem1 >= 73
	NX7_mem1 += MAIN_MEM_r[1]

	NY7__in = S.Task('NY7__in', length=1, delay_cost=1)
	S += NY7__in >= 73
	NY7__in += MAS_in[2]

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	S += NY7__mem0 >= 73
	NY7__mem0 += MM_MEM[2]

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	S += NY7__mem1 >= 73
	NY7__mem1 += MM_MEM[3]

	Z_exp11 = S.Task('Z_exp11', length=8, delay_cost=1)
	S += Z_exp11 >= 73
	Z_exp11 += MM[1]

	k0_1_Z10 = S.Task('k0_1_Z10', length=8, delay_cost=1)
	S += k0_1_Z10 >= 73
	k0_1_Z10 += MM[0]

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	S += k2_5_Z10_in >= 73
	k2_5_Z10_in += MM_in[1]

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	S += k2_5_Z10_mem0 >= 73
	k2_5_Z10_mem0 += MAIN_MEM_r[0]

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	S += k2_5_Z10_mem1 >= 73
	k2_5_Z10_mem1 += MM_MEM[1]

	NX7 = S.Task('NX7', length=8, delay_cost=1)
	S += NX7 >= 74
	NX7 += MM[0]

	NY7_ = S.Task('NY7_', length=2, delay_cost=1)
	S += NY7_ >= 74
	NY7_ += MAS[2]

	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	S += k1_1_Z10_in >= 74
	k1_1_Z10_in += MM_in[1]

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	S += k1_1_Z10_mem0 >= 74
	k1_1_Z10_mem0 += MAIN_MEM_r[0]

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	S += k1_1_Z10_mem1 >= 74
	k1_1_Z10_mem1 += MM_MEM[1]

	k2_5_Z10 = S.Task('k2_5_Z10', length=8, delay_cost=1)
	S += k2_5_Z10 >= 74
	k2_5_Z10 += MM[1]

	NY7_in = S.Task('NY7_in', length=1, delay_cost=1)
	S += NY7_in >= 75
	NY7_in += MM_in[1]

	NY7_mem0 = S.Task('NY7_mem0', length=1, delay_cost=1)
	S += NY7_mem0 >= 75
	NY7_mem0 += MAS_MEM[4]

	NY7_mem1 = S.Task('NY7_mem1', length=1, delay_cost=1)
	S += NY7_mem1 >= 75
	NY7_mem1 += MAIN_MEM_r[1]

	k1_1_Z10 = S.Task('k1_1_Z10', length=8, delay_cost=1)
	S += k1_1_Z10 >= 75
	k1_1_Z10 += MM[1]

	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	S += k3_6_Z10_in >= 75
	k3_6_Z10_in += MM_in[0]

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	S += k3_6_Z10_mem0 >= 75
	k3_6_Z10_mem0 += MAIN_MEM_r[0]

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	S += k3_6_Z10_mem1 >= 75
	k3_6_Z10_mem1 += MM_MEM[1]

	NY7 = S.Task('NY7', length=8, delay_cost=1)
	S += NY7 >= 76
	NY7 += MM[1]

	k3_6_Z10 = S.Task('k3_6_Z10', length=8, delay_cost=1)
	S += k3_6_Z10 >= 76
	k3_6_Z10 += MM[0]

	DY7__in = S.Task('DY7__in', length=1, delay_cost=1)
	S += DY7__in >= 77
	DY7__in += MAS_in[0]

	DY7__mem0 = S.Task('DY7__mem0', length=1, delay_cost=1)
	S += DY7__mem0 >= 77
	DY7__mem0 += MM_MEM[2]

	DY7__mem1 = S.Task('DY7__mem1', length=1, delay_cost=1)
	S += DY7__mem1 >= 77
	DY7__mem1 += MM_MEM[3]

	DX7__in = S.Task('DX7__in', length=1, delay_cost=1)
	S += DX7__in >= 78
	DX7__in += MAS_in[1]

	DX7__mem0 = S.Task('DX7__mem0', length=1, delay_cost=1)
	S += DX7__mem0 >= 78
	DX7__mem0 += MM_MEM[2]

	DX7__mem1 = S.Task('DX7__mem1', length=1, delay_cost=1)
	S += DX7__mem1 >= 78
	DX7__mem1 += MM_MEM[1]

	DY7_ = S.Task('DY7_', length=2, delay_cost=1)
	S += DY7_ >= 78
	DY7_ += MAS[0]

	DX7_ = S.Task('DX7_', length=2, delay_cost=1)
	S += DX7_ >= 79
	DX7_ += MAS[1]

	DY7_in = S.Task('DY7_in', length=1, delay_cost=1)
	S += DY7_in >= 79
	DY7_in += MM_in[0]

	DY7_mem0 = S.Task('DY7_mem0', length=1, delay_cost=1)
	S += DY7_mem0 >= 79
	DY7_mem0 += MAS_MEM[0]

	DY7_mem1 = S.Task('DY7_mem1', length=1, delay_cost=1)
	S += DY7_mem1 >= 79
	DY7_mem1 += MAIN_MEM_r[1]

	DY7 = S.Task('DY7', length=8, delay_cost=1)
	S += DY7 >= 80
	DY7 += MM[0]

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	S += Z_exp12_in >= 80
	Z_exp12_in += MM_in[1]

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	S += Z_exp12_mem0 >= 80
	Z_exp12_mem0 += MM_MEM[2]

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	S += Z_exp12_mem1 >= 80
	Z_exp12_mem1 += MAIN_MEM_r[1]

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	S += k3_5_Z11_in >= 80
	k3_5_Z11_in += MM_in[0]

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	S += k3_5_Z11_mem0 >= 80
	k3_5_Z11_mem0 += MAIN_MEM_r[0]

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	S += k3_5_Z11_mem1 >= 80
	k3_5_Z11_mem1 += MM_MEM[3]

	DX7_in = S.Task('DX7_in', length=1, delay_cost=1)
	S += DX7_in >= 81
	DX7_in += MM_in[0]

	DX7_mem0 = S.Task('DX7_mem0', length=1, delay_cost=1)
	S += DX7_mem0 >= 81
	DX7_mem0 += MAS_MEM[2]

	DX7_mem1 = S.Task('DX7_mem1', length=1, delay_cost=1)
	S += DX7_mem1 >= 81
	DX7_mem1 += MAIN_MEM_r[1]

	Z_exp12 = S.Task('Z_exp12', length=8, delay_cost=1)
	S += Z_exp12 >= 81
	Z_exp12 += MM[1]

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	S += k1_0_Z11_in >= 81
	k1_0_Z11_in += MM_in[1]

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	S += k1_0_Z11_mem0 >= 81
	k1_0_Z11_mem0 += MAIN_MEM_r[0]

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	S += k1_0_Z11_mem1 >= 81
	k1_0_Z11_mem1 += MM_MEM[3]

	k3_5_Z11 = S.Task('k3_5_Z11', length=8, delay_cost=1)
	S += k3_5_Z11 >= 81
	k3_5_Z11 += MM[0]

	DX7 = S.Task('DX7', length=8, delay_cost=1)
	S += DX7 >= 82
	DX7 += MM[0]

	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	S += k0_0_Z11_in >= 82
	k0_0_Z11_in += MM_in[0]

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	S += k0_0_Z11_mem0 >= 82
	k0_0_Z11_mem0 += MAIN_MEM_r[0]

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	S += k0_0_Z11_mem1 >= 82
	k0_0_Z11_mem1 += MM_MEM[3]

	k1_0_Z11 = S.Task('k1_0_Z11', length=8, delay_cost=1)
	S += k1_0_Z11 >= 82
	k1_0_Z11 += MM[1]

	NY8__in = S.Task('NY8__in', length=1, delay_cost=1)
	S += NY8__in >= 83
	NY8__in += MAS_in[2]

	NY8__mem0 = S.Task('NY8__mem0', length=1, delay_cost=1)
	S += NY8__mem0 >= 83
	NY8__mem0 += MM_MEM[2]

	NY8__mem1 = S.Task('NY8__mem1', length=1, delay_cost=1)
	S += NY8__mem1 >= 83
	NY8__mem1 += MM_MEM[1]

	k0_0_Z11 = S.Task('k0_0_Z11', length=8, delay_cost=1)
	S += k0_0_Z11 >= 83
	k0_0_Z11 += MM[0]

	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	S += k2_4_Z11_in >= 83
	k2_4_Z11_in += MM_in[0]

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	S += k2_4_Z11_mem0 >= 83
	k2_4_Z11_mem0 += MAIN_MEM_r[0]

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	S += k2_4_Z11_mem1 >= 83
	k2_4_Z11_mem1 += MM_MEM[3]

	NX8__in = S.Task('NX8__in', length=1, delay_cost=1)
	S += NX8__in >= 84
	NX8__in += MAS_in[2]

	NX8__mem0 = S.Task('NX8__mem0', length=1, delay_cost=1)
	S += NX8__mem0 >= 84
	NX8__mem0 += MM_MEM[0]

	NX8__mem1 = S.Task('NX8__mem1', length=1, delay_cost=1)
	S += NX8__mem1 >= 84
	NX8__mem1 += MM_MEM[3]

	NY8_ = S.Task('NY8_', length=2, delay_cost=1)
	S += NY8_ >= 84
	NY8_ += MAS[2]

	k2_4_Z11 = S.Task('k2_4_Z11', length=8, delay_cost=1)
	S += k2_4_Z11 >= 84
	k2_4_Z11 += MM[0]

	NX8_ = S.Task('NX8_', length=2, delay_cost=1)
	S += NX8_ >= 85
	NX8_ += MAS[2]

	NY8_in = S.Task('NY8_in', length=1, delay_cost=1)
	S += NY8_in >= 85
	NY8_in += MM_in[1]

	NY8_mem0 = S.Task('NY8_mem0', length=1, delay_cost=1)
	S += NY8_mem0 >= 85
	NY8_mem0 += MAS_MEM[4]

	NY8_mem1 = S.Task('NY8_mem1', length=1, delay_cost=1)
	S += NY8_mem1 >= 85
	NY8_mem1 += MAIN_MEM_r[1]

	NX8_in = S.Task('NX8_in', length=1, delay_cost=1)
	S += NX8_in >= 86
	NX8_in += MM_in[0]

	NX8_mem0 = S.Task('NX8_mem0', length=1, delay_cost=1)
	S += NX8_mem0 >= 86
	NX8_mem0 += MAS_MEM[4]

	NX8_mem1 = S.Task('NX8_mem1', length=1, delay_cost=1)
	S += NX8_mem1 >= 86
	NX8_mem1 += MAIN_MEM_r[1]

	NY8 = S.Task('NY8', length=8, delay_cost=1)
	S += NY8 >= 86
	NY8 += MM[1]

	DY8__in = S.Task('DY8__in', length=1, delay_cost=1)
	S += DY8__in >= 87
	DY8__in += MAS_in[2]

	DY8__mem0 = S.Task('DY8__mem0', length=1, delay_cost=1)
	S += DY8__mem0 >= 87
	DY8__mem0 += MM_MEM[0]

	DY8__mem1 = S.Task('DY8__mem1', length=1, delay_cost=1)
	S += DY8__mem1 >= 87
	DY8__mem1 += MM_MEM[3]

	NX8 = S.Task('NX8', length=8, delay_cost=1)
	S += NX8 >= 87
	NX8 += MM[0]

	DY8_ = S.Task('DY8_', length=2, delay_cost=1)
	S += DY8_ >= 88
	DY8_ += MAS[2]

	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	S += Z_exp13_in >= 88
	Z_exp13_in += MM_in[0]

	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	S += Z_exp13_mem0 >= 88
	Z_exp13_mem0 += MM_MEM[2]

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	S += Z_exp13_mem1 >= 88
	Z_exp13_mem1 += MAIN_MEM_r[1]

	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	S += k2_3_Z12_in >= 88
	k2_3_Z12_in += MM_in[1]

	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	S += k2_3_Z12_mem0 >= 88
	k2_3_Z12_mem0 += MAIN_MEM_r[0]

	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	S += k2_3_Z12_mem1 >= 88
	k2_3_Z12_mem1 += MM_MEM[3]

	DX8__in = S.Task('DX8__in', length=1, delay_cost=1)
	S += DX8__in >= 89
	DX8__in += MAS_in[2]

	DX8__mem0 = S.Task('DX8__mem0', length=1, delay_cost=1)
	S += DX8__mem0 >= 89
	DX8__mem0 += MM_MEM[0]

	DX8__mem1 = S.Task('DX8__mem1', length=1, delay_cost=1)
	S += DX8__mem1 >= 89
	DX8__mem1 += MM_MEM[1]

	DY8_in = S.Task('DY8_in', length=1, delay_cost=1)
	S += DY8_in >= 89
	DY8_in += MM_in[1]

	DY8_mem0 = S.Task('DY8_mem0', length=1, delay_cost=1)
	S += DY8_mem0 >= 89
	DY8_mem0 += MAS_MEM[4]

	DY8_mem1 = S.Task('DY8_mem1', length=1, delay_cost=1)
	S += DY8_mem1 >= 89
	DY8_mem1 += MAIN_MEM_r[1]

	Z_exp13 = S.Task('Z_exp13', length=8, delay_cost=1)
	S += Z_exp13 >= 89
	Z_exp13 += MM[0]

	k2_3_Z12 = S.Task('k2_3_Z12', length=8, delay_cost=1)
	S += k2_3_Z12 >= 89
	k2_3_Z12 += MM[1]

	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	S += k3_4_Z12_in >= 89
	k3_4_Z12_in += MM_in[0]

	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	S += k3_4_Z12_mem0 >= 89
	k3_4_Z12_mem0 += MAIN_MEM_r[0]

	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	S += k3_4_Z12_mem1 >= 89
	k3_4_Z12_mem1 += MM_MEM[3]

	DX8_ = S.Task('DX8_', length=2, delay_cost=1)
	S += DX8_ >= 90
	DX8_ += MAS[2]

	DY8 = S.Task('DY8', length=8, delay_cost=1)
	S += DY8 >= 90
	DY8 += MM[1]

	k3_4_Z12 = S.Task('k3_4_Z12', length=8, delay_cost=1)
	S += k3_4_Z12 >= 90
	k3_4_Z12 += MM[0]

	DX8_in = S.Task('DX8_in', length=1, delay_cost=1)
	S += DX8_in >= 91
	DX8_in += MM_in[0]

	DX8_mem0 = S.Task('DX8_mem0', length=1, delay_cost=1)
	S += DX8_mem0 >= 91
	DX8_mem0 += MAS_MEM[4]

	DX8_mem1 = S.Task('DX8_mem1', length=1, delay_cost=1)
	S += DX8_mem1 >= 91
	DX8_mem1 += MAIN_MEM_r[1]

	DX8 = S.Task('DX8', length=8, delay_cost=1)
	S += DX8 >= 92
	DX8 += MM[0]

	NY9__in = S.Task('NY9__in', length=1, delay_cost=1)
	S += NY9__in >= 93
	NY9__in += MAS_in[4]

	NY9__mem0 = S.Task('NY9__mem0', length=1, delay_cost=1)
	S += NY9__mem0 >= 93
	NY9__mem0 += MM_MEM[2]

	NY9__mem1 = S.Task('NY9__mem1', length=1, delay_cost=1)
	S += NY9__mem1 >= 93
	NY9__mem1 += MM_MEM[1]

	NX9__in = S.Task('NX9__in', length=1, delay_cost=1)
	S += NX9__in >= 94
	NX9__in += MAS_in[4]

	NX9__mem0 = S.Task('NX9__mem0', length=1, delay_cost=1)
	S += NX9__mem0 >= 94
	NX9__mem0 += MM_MEM[0]

	NX9__mem1 = S.Task('NX9__mem1', length=1, delay_cost=1)
	S += NX9__mem1 >= 94
	NX9__mem1 += MM_MEM[3]

	NY9_ = S.Task('NY9_', length=2, delay_cost=1)
	S += NY9_ >= 94
	NY9_ += MAS[4]

	NX9_ = S.Task('NX9_', length=2, delay_cost=1)
	S += NX9_ >= 95
	NX9_ += MAS[4]

	NY9_in = S.Task('NY9_in', length=1, delay_cost=1)
	S += NY9_in >= 95
	NY9_in += MM_in[1]

	NY9_mem0 = S.Task('NY9_mem0', length=1, delay_cost=1)
	S += NY9_mem0 >= 95
	NY9_mem0 += MAS_MEM[8]

	NY9_mem1 = S.Task('NY9_mem1', length=1, delay_cost=1)
	S += NY9_mem1 >= 95
	NY9_mem1 += MAIN_MEM_r[1]

	NY9 = S.Task('NY9', length=8, delay_cost=1)
	S += NY9 >= 96
	NY9 += MM[1]

	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	S += Z_exp14_in >= 96
	Z_exp14_in += MM_in[0]

	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	S += Z_exp14_mem0 >= 96
	Z_exp14_mem0 += MM_MEM[0]

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	S += Z_exp14_mem1 >= 96
	Z_exp14_mem1 += MAIN_MEM_r[1]

	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	S += k2_2_Z13_in >= 96
	k2_2_Z13_in += MM_in[1]

	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	S += k2_2_Z13_mem0 >= 96
	k2_2_Z13_mem0 += MAIN_MEM_r[0]

	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	S += k2_2_Z13_mem1 >= 96
	k2_2_Z13_mem1 += MM_MEM[1]

	NX9_in = S.Task('NX9_in', length=1, delay_cost=1)
	S += NX9_in >= 97
	NX9_in += MM_in[1]

	NX9_mem0 = S.Task('NX9_mem0', length=1, delay_cost=1)
	S += NX9_mem0 >= 97
	NX9_mem0 += MAS_MEM[8]

	NX9_mem1 = S.Task('NX9_mem1', length=1, delay_cost=1)
	S += NX9_mem1 >= 97
	NX9_mem1 += MAIN_MEM_r[1]

	Z_exp14 = S.Task('Z_exp14', length=8, delay_cost=1)
	S += Z_exp14 >= 97
	Z_exp14 += MM[0]

	k2_2_Z13 = S.Task('k2_2_Z13', length=8, delay_cost=1)
	S += k2_2_Z13 >= 97
	k2_2_Z13 += MM[1]

	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	S += k3_3_Z13_in >= 97
	k3_3_Z13_in += MM_in[0]

	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	S += k3_3_Z13_mem0 >= 97
	k3_3_Z13_mem0 += MAIN_MEM_r[0]

	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	S += k3_3_Z13_mem1 >= 97
	k3_3_Z13_mem1 += MM_MEM[1]

	DY9__in = S.Task('DY9__in', length=1, delay_cost=1)
	S += DY9__in >= 98
	DY9__in += MAS_in[2]

	DY9__mem0 = S.Task('DY9__mem0', length=1, delay_cost=1)
	S += DY9__mem0 >= 98
	DY9__mem0 += MM_MEM[2]

	DY9__mem1 = S.Task('DY9__mem1', length=1, delay_cost=1)
	S += DY9__mem1 >= 98
	DY9__mem1 += MM_MEM[1]

	NX9 = S.Task('NX9', length=8, delay_cost=1)
	S += NX9 >= 98
	NX9 += MM[1]

	k3_3_Z13 = S.Task('k3_3_Z13', length=8, delay_cost=1)
	S += k3_3_Z13 >= 98
	k3_3_Z13 += MM[0]

	DX9__in = S.Task('DX9__in', length=1, delay_cost=1)
	S += DX9__in >= 99
	DX9__in += MAS_in[4]

	DX9__mem0 = S.Task('DX9__mem0', length=1, delay_cost=1)
	S += DX9__mem0 >= 99
	DX9__mem0 += MM_MEM[0]

	DX9__mem1 = S.Task('DX9__mem1', length=1, delay_cost=1)
	S += DX9__mem1 >= 99
	DX9__mem1 += MM_MEM[3]

	DY9_ = S.Task('DY9_', length=2, delay_cost=1)
	S += DY9_ >= 99
	DY9_ += MAS[2]

	DX9_ = S.Task('DX9_', length=2, delay_cost=1)
	S += DX9_ >= 100
	DX9_ += MAS[4]

	DY9_in = S.Task('DY9_in', length=1, delay_cost=1)
	S += DY9_in >= 100
	DY9_in += MM_in[1]

	DY9_mem0 = S.Task('DY9_mem0', length=1, delay_cost=1)
	S += DY9_mem0 >= 100
	DY9_mem0 += MAS_MEM[4]

	DY9_mem1 = S.Task('DY9_mem1', length=1, delay_cost=1)
	S += DY9_mem1 >= 100
	DY9_mem1 += MAIN_MEM_r[1]

	DX9_in = S.Task('DX9_in', length=1, delay_cost=1)
	S += DX9_in >= 101
	DX9_in += MM_in[1]

	DX9_mem0 = S.Task('DX9_mem0', length=1, delay_cost=1)
	S += DX9_mem0 >= 101
	DX9_mem0 += MAS_MEM[8]

	DX9_mem1 = S.Task('DX9_mem1', length=1, delay_cost=1)
	S += DX9_mem1 >= 101
	DX9_mem1 += MAIN_MEM_r[1]

	DY9 = S.Task('DY9', length=8, delay_cost=1)
	S += DY9 >= 101
	DY9 += MM[1]

	DX9 = S.Task('DX9', length=8, delay_cost=1)
	S += DX9 >= 102
	DX9 += MM[1]

	NY10__in = S.Task('NY10__in', length=1, delay_cost=1)
	S += NY10__in >= 103
	NY10__in += MAS_in[5]

	NY10__mem0 = S.Task('NY10__mem0', length=1, delay_cost=1)
	S += NY10__mem0 >= 103
	NY10__mem0 += MM_MEM[2]

	NY10__mem1 = S.Task('NY10__mem1', length=1, delay_cost=1)
	S += NY10__mem1 >= 103
	NY10__mem1 += MM_MEM[3]

	NY10_ = S.Task('NY10_', length=2, delay_cost=1)
	S += NY10_ >= 104
	NY10_ += MAS[5]

	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	S += Z_exp15_in >= 104
	Z_exp15_in += MM_in[0]

	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	S += Z_exp15_mem0 >= 104
	Z_exp15_mem0 += MM_MEM[0]

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	S += Z_exp15_mem1 >= 104
	Z_exp15_mem1 += MAIN_MEM_r[1]

	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	S += k2_1_Z14_in >= 104
	k2_1_Z14_in += MM_in[1]

	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	S += k2_1_Z14_mem0 >= 104
	k2_1_Z14_mem0 += MAIN_MEM_r[0]

	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	S += k2_1_Z14_mem1 >= 104
	k2_1_Z14_mem1 += MM_MEM[1]

	NY10_in = S.Task('NY10_in', length=1, delay_cost=1)
	S += NY10_in >= 105
	NY10_in += MM_in[1]

	NY10_mem0 = S.Task('NY10_mem0', length=1, delay_cost=1)
	S += NY10_mem0 >= 105
	NY10_mem0 += MAS_MEM[10]

	NY10_mem1 = S.Task('NY10_mem1', length=1, delay_cost=1)
	S += NY10_mem1 >= 105
	NY10_mem1 += MAIN_MEM_r[1]

	Z_exp15 = S.Task('Z_exp15', length=8, delay_cost=1)
	S += Z_exp15 >= 105
	Z_exp15 += MM[0]

	k2_1_Z14 = S.Task('k2_1_Z14', length=8, delay_cost=1)
	S += k2_1_Z14 >= 105
	k2_1_Z14 += MM[1]

	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	S += k3_2_Z14_in >= 105
	k3_2_Z14_in += MM_in[0]

	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	S += k3_2_Z14_mem0 >= 105
	k3_2_Z14_mem0 += MAIN_MEM_r[0]

	k3_2_Z14_mem1 = S.Task('k3_2_Z14_mem1', length=1, delay_cost=1)
	S += k3_2_Z14_mem1 >= 105
	k3_2_Z14_mem1 += MM_MEM[1]

	NX10__in = S.Task('NX10__in', length=1, delay_cost=1)
	S += NX10__in >= 106
	NX10__in += MAS_in[2]

	NX10__mem0 = S.Task('NX10__mem0', length=1, delay_cost=1)
	S += NX10__mem0 >= 106
	NX10__mem0 += MM_MEM[2]

	NX10__mem1 = S.Task('NX10__mem1', length=1, delay_cost=1)
	S += NX10__mem1 >= 106
	NX10__mem1 += MM_MEM[1]

	NY10 = S.Task('NY10', length=8, delay_cost=1)
	S += NY10 >= 106
	NY10 += MM[1]

	k3_2_Z14 = S.Task('k3_2_Z14', length=8, delay_cost=1)
	S += k3_2_Z14 >= 106
	k3_2_Z14 += MM[0]

	NX10_ = S.Task('NX10_', length=2, delay_cost=1)
	S += NX10_ >= 107
	NX10_ += MAS[2]

	DY10__in = S.Task('DY10__in', length=1, delay_cost=1)
	S += DY10__in >= 108
	DY10__in += MAS_in[1]

	DY10__mem0 = S.Task('DY10__mem0', length=1, delay_cost=1)
	S += DY10__mem0 >= 108
	DY10__mem0 += MM_MEM[2]

	DY10__mem1 = S.Task('DY10__mem1', length=1, delay_cost=1)
	S += DY10__mem1 >= 108
	DY10__mem1 += MM_MEM[1]

	NX10_in = S.Task('NX10_in', length=1, delay_cost=1)
	S += NX10_in >= 108
	NX10_in += MM_in[1]

	NX10_mem0 = S.Task('NX10_mem0', length=1, delay_cost=1)
	S += NX10_mem0 >= 108
	NX10_mem0 += MAS_MEM[4]

	NX10_mem1 = S.Task('NX10_mem1', length=1, delay_cost=1)
	S += NX10_mem1 >= 108
	NX10_mem1 += MAIN_MEM_r[1]

	DX_in = S.Task('DX_in', length=1, delay_cost=1)
	S += DX_in >= 109
	DX_in += MAS_in[4]

	DX_mem0 = S.Task('DX_mem0', length=1, delay_cost=1)
	S += DX_mem0 >= 109
	DX_mem0 += MM_MEM[2]

	DX_mem1 = S.Task('DX_mem1', length=1, delay_cost=1)
	S += DX_mem1 >= 109
	DX_mem1 += MM_MEM[3]

	DY10_ = S.Task('DY10_', length=2, delay_cost=1)
	S += DY10_ >= 109
	DY10_ += MAS[1]

	NX10 = S.Task('NX10', length=8, delay_cost=1)
	S += NX10 >= 109
	NX10 += MM[1]

	DX = S.Task('DX', length=2, delay_cost=1)
	S += DX >= 110
	DX += MAS[4]

	DY10_in = S.Task('DY10_in', length=1, delay_cost=1)
	S += DY10_in >= 110
	DY10_in += MM_in[1]

	DY10_mem0 = S.Task('DY10_mem0', length=1, delay_cost=1)
	S += DY10_mem0 >= 110
	DY10_mem0 += MAS_MEM[2]

	DY10_mem1 = S.Task('DY10_mem1', length=1, delay_cost=1)
	S += DY10_mem1 >= 110
	DY10_mem1 += MAIN_MEM_r[1]

	DY10 = S.Task('DY10', length=8, delay_cost=1)
	S += DY10 >= 111
	DY10 += MM[1]

	Z_exp16_in = S.Task('Z_exp16_in', length=1, delay_cost=1)
	S += Z_exp16_in >= 112
	Z_exp16_in += MM_in[0]

	Z_exp16_mem0 = S.Task('Z_exp16_mem0', length=1, delay_cost=1)
	S += Z_exp16_mem0 >= 112
	Z_exp16_mem0 += MM_MEM[0]

	Z_exp16_mem1 = S.Task('Z_exp16_mem1', length=1, delay_cost=1)
	S += Z_exp16_mem1 >= 112
	Z_exp16_mem1 += MAIN_MEM_r[1]

	k3_1_Z15_in = S.Task('k3_1_Z15_in', length=1, delay_cost=1)
	S += k3_1_Z15_in >= 112
	k3_1_Z15_in += MM_in[1]

	k3_1_Z15_mem0 = S.Task('k3_1_Z15_mem0', length=1, delay_cost=1)
	S += k3_1_Z15_mem0 >= 112
	k3_1_Z15_mem0 += MAIN_MEM_r[0]

	k3_1_Z15_mem1 = S.Task('k3_1_Z15_mem1', length=1, delay_cost=1)
	S += k3_1_Z15_mem1 >= 112
	k3_1_Z15_mem1 += MM_MEM[1]

	NY11__in = S.Task('NY11__in', length=1, delay_cost=1)
	S += NY11__in >= 113
	NY11__in += MAS_in[5]

	NY11__mem0 = S.Task('NY11__mem0', length=1, delay_cost=1)
	S += NY11__mem0 >= 113
	NY11__mem0 += MM_MEM[2]

	NY11__mem1 = S.Task('NY11__mem1', length=1, delay_cost=1)
	S += NY11__mem1 >= 113
	NY11__mem1 += MM_MEM[1]

	Z_exp16 = S.Task('Z_exp16', length=8, delay_cost=1)
	S += Z_exp16 >= 113
	Z_exp16 += MM[0]

	k3_1_Z15 = S.Task('k3_1_Z15', length=8, delay_cost=1)
	S += k3_1_Z15 >= 113
	k3_1_Z15 += MM[1]

	NY11_ = S.Task('NY11_', length=2, delay_cost=1)
	S += NY11_ >= 114
	NY11_ += MAS[5]

	k2_0_Z15_in = S.Task('k2_0_Z15_in', length=1, delay_cost=1)
	S += k2_0_Z15_in >= 114
	k2_0_Z15_in += MM_in[0]

	k2_0_Z15_mem0 = S.Task('k2_0_Z15_mem0', length=1, delay_cost=1)
	S += k2_0_Z15_mem0 >= 114
	k2_0_Z15_mem0 += MAIN_MEM_r[0]

	k2_0_Z15_mem1 = S.Task('k2_0_Z15_mem1', length=1, delay_cost=1)
	S += k2_0_Z15_mem1 >= 114
	k2_0_Z15_mem1 += MM_MEM[1]

	NY11_in = S.Task('NY11_in', length=1, delay_cost=1)
	S += NY11_in >= 115
	NY11_in += MM_in[1]

	NY11_mem0 = S.Task('NY11_mem0', length=1, delay_cost=1)
	S += NY11_mem0 >= 115
	NY11_mem0 += MAS_MEM[10]

	NY11_mem1 = S.Task('NY11_mem1', length=1, delay_cost=1)
	S += NY11_mem1 >= 115
	NY11_mem1 += MAIN_MEM_r[1]

	k2_0_Z15 = S.Task('k2_0_Z15', length=8, delay_cost=1)
	S += k2_0_Z15 >= 115
	k2_0_Z15 += MM[0]

	NX_in = S.Task('NX_in', length=1, delay_cost=1)
	S += NX_in >= 116
	NX_in += MAS_in[5]

	NX_mem0 = S.Task('NX_mem0', length=1, delay_cost=1)
	S += NX_mem0 >= 116
	NX_mem0 += MM_MEM[2]

	NX_mem1 = S.Task('NX_mem1', length=1, delay_cost=1)
	S += NX_mem1 >= 116
	NX_mem1 += MM_MEM[1]

	NY11 = S.Task('NY11', length=8, delay_cost=1)
	S += NY11 >= 116
	NY11 += MM[1]

	NX = S.Task('NX', length=2, delay_cost=1)
	S += NX >= 117
	NX += MAS[5]

	DY11__in = S.Task('DY11__in', length=1, delay_cost=1)
	S += DY11__in >= 118
	DY11__in += MAS_in[5]

	DY11__mem0 = S.Task('DY11__mem0', length=1, delay_cost=1)
	S += DY11__mem0 >= 118
	DY11__mem0 += MM_MEM[2]

	DY11__mem1 = S.Task('DY11__mem1', length=1, delay_cost=1)
	S += DY11__mem1 >= 118
	DY11__mem1 += MM_MEM[1]

	DY11_ = S.Task('DY11_', length=2, delay_cost=1)
	S += DY11_ >= 119
	DY11_ += MAS[5]

	DY11_in = S.Task('DY11_in', length=1, delay_cost=1)
	S += DY11_in >= 120
	DY11_in += MM_in[1]

	DY11_mem0 = S.Task('DY11_mem0', length=1, delay_cost=1)
	S += DY11_mem0 >= 120
	DY11_mem0 += MAS_MEM[10]

	DY11_mem1 = S.Task('DY11_mem1', length=1, delay_cost=1)
	S += DY11_mem1 >= 120
	DY11_mem1 += MAIN_MEM_r[1]

	k3_0_Z16_in = S.Task('k3_0_Z16_in', length=1, delay_cost=1)
	S += k3_0_Z16_in >= 120
	k3_0_Z16_in += MM_in[0]

	k3_0_Z16_mem0 = S.Task('k3_0_Z16_mem0', length=1, delay_cost=1)
	S += k3_0_Z16_mem0 >= 120
	k3_0_Z16_mem0 += MAIN_MEM_r[0]

	k3_0_Z16_mem1 = S.Task('k3_0_Z16_mem1', length=1, delay_cost=1)
	S += k3_0_Z16_mem1 >= 120
	k3_0_Z16_mem1 += MM_MEM[1]

	DY11 = S.Task('DY11', length=8, delay_cost=1)
	S += DY11 >= 121
	DY11 += MM[1]

	k3_0_Z16 = S.Task('k3_0_Z16', length=8, delay_cost=1)
	S += k3_0_Z16 >= 121
	k3_0_Z16 += MM[0]

	NY12__in = S.Task('NY12__in', length=1, delay_cost=1)
	S += NY12__in >= 123
	NY12__in += MAS_in[5]

	NY12__mem0 = S.Task('NY12__mem0', length=1, delay_cost=1)
	S += NY12__mem0 >= 123
	NY12__mem0 += MM_MEM[2]

	NY12__mem1 = S.Task('NY12__mem1', length=1, delay_cost=1)
	S += NY12__mem1 >= 123
	NY12__mem1 += MM_MEM[3]

	NY12_ = S.Task('NY12_', length=2, delay_cost=1)
	S += NY12_ >= 124
	NY12_ += MAS[5]

	NY12_in = S.Task('NY12_in', length=1, delay_cost=1)
	S += NY12_in >= 125
	NY12_in += MM_in[1]

	NY12_mem0 = S.Task('NY12_mem0', length=1, delay_cost=1)
	S += NY12_mem0 >= 125
	NY12_mem0 += MAS_MEM[10]

	NY12_mem1 = S.Task('NY12_mem1', length=1, delay_cost=1)
	S += NY12_mem1 >= 125
	NY12_mem1 += MAIN_MEM_r[1]

	NY12 = S.Task('NY12', length=8, delay_cost=1)
	S += NY12 >= 126
	NY12 += MM[1]

	DY12__in = S.Task('DY12__in', length=1, delay_cost=1)
	S += DY12__in >= 128
	DY12__in += MAS_in[0]

	DY12__mem0 = S.Task('DY12__mem0', length=1, delay_cost=1)
	S += DY12__mem0 >= 128
	DY12__mem0 += MM_MEM[2]

	DY12__mem1 = S.Task('DY12__mem1', length=1, delay_cost=1)
	S += DY12__mem1 >= 128
	DY12__mem1 += MM_MEM[1]

	DY12_ = S.Task('DY12_', length=2, delay_cost=1)
	S += DY12_ >= 129
	DY12_ += MAS[0]

	DY12_in = S.Task('DY12_in', length=1, delay_cost=1)
	S += DY12_in >= 130
	DY12_in += MM_in[1]

	DY12_mem0 = S.Task('DY12_mem0', length=1, delay_cost=1)
	S += DY12_mem0 >= 130
	DY12_mem0 += MAS_MEM[0]

	DY12_mem1 = S.Task('DY12_mem1', length=1, delay_cost=1)
	S += DY12_mem1 >= 130
	DY12_mem1 += MAIN_MEM_r[1]

	DY12 = S.Task('DY12', length=8, delay_cost=1)
	S += DY12 >= 131
	DY12 += MM[1]

	NY13__in = S.Task('NY13__in', length=1, delay_cost=1)
	S += NY13__in >= 133
	NY13__in += MAS_in[5]

	NY13__mem0 = S.Task('NY13__mem0', length=1, delay_cost=1)
	S += NY13__mem0 >= 133
	NY13__mem0 += MM_MEM[2]

	NY13__mem1 = S.Task('NY13__mem1', length=1, delay_cost=1)
	S += NY13__mem1 >= 133
	NY13__mem1 += MM_MEM[3]

	NY13_ = S.Task('NY13_', length=2, delay_cost=1)
	S += NY13_ >= 134
	NY13_ += MAS[5]

	NY13_in = S.Task('NY13_in', length=1, delay_cost=1)
	S += NY13_in >= 135
	NY13_in += MM_in[1]

	NY13_mem0 = S.Task('NY13_mem0', length=1, delay_cost=1)
	S += NY13_mem0 >= 135
	NY13_mem0 += MAS_MEM[10]

	NY13_mem1 = S.Task('NY13_mem1', length=1, delay_cost=1)
	S += NY13_mem1 >= 135
	NY13_mem1 += MAIN_MEM_r[1]

	NY13 = S.Task('NY13', length=8, delay_cost=1)
	S += NY13 >= 136
	NY13 += MM[1]

	DY13__in = S.Task('DY13__in', length=1, delay_cost=1)
	S += DY13__in >= 138
	DY13__in += MAS_in[0]

	DY13__mem0 = S.Task('DY13__mem0', length=1, delay_cost=1)
	S += DY13__mem0 >= 138
	DY13__mem0 += MM_MEM[2]

	DY13__mem1 = S.Task('DY13__mem1', length=1, delay_cost=1)
	S += DY13__mem1 >= 138
	DY13__mem1 += MM_MEM[1]

	DY13_ = S.Task('DY13_', length=2, delay_cost=1)
	S += DY13_ >= 139
	DY13_ += MAS[0]

	DY13_in = S.Task('DY13_in', length=1, delay_cost=1)
	S += DY13_in >= 140
	DY13_in += MM_in[1]

	DY13_mem0 = S.Task('DY13_mem0', length=1, delay_cost=1)
	S += DY13_mem0 >= 140
	DY13_mem0 += MAS_MEM[0]

	DY13_mem1 = S.Task('DY13_mem1', length=1, delay_cost=1)
	S += DY13_mem1 >= 140
	DY13_mem1 += MAIN_MEM_r[1]

	DY13 = S.Task('DY13', length=8, delay_cost=1)
	S += DY13 >= 141
	DY13 += MM[1]

	NY14__in = S.Task('NY14__in', length=1, delay_cost=1)
	S += NY14__in >= 143
	NY14__in += MAS_in[5]

	NY14__mem0 = S.Task('NY14__mem0', length=1, delay_cost=1)
	S += NY14__mem0 >= 143
	NY14__mem0 += MM_MEM[2]

	NY14__mem1 = S.Task('NY14__mem1', length=1, delay_cost=1)
	S += NY14__mem1 >= 143
	NY14__mem1 += MM_MEM[3]

	NY14_ = S.Task('NY14_', length=2, delay_cost=1)
	S += NY14_ >= 144
	NY14_ += MAS[5]

	NY14_in = S.Task('NY14_in', length=1, delay_cost=1)
	S += NY14_in >= 145
	NY14_in += MM_in[1]

	NY14_mem0 = S.Task('NY14_mem0', length=1, delay_cost=1)
	S += NY14_mem0 >= 145
	NY14_mem0 += MAS_MEM[10]

	NY14_mem1 = S.Task('NY14_mem1', length=1, delay_cost=1)
	S += NY14_mem1 >= 145
	NY14_mem1 += MAIN_MEM_r[1]

	NY14 = S.Task('NY14', length=8, delay_cost=1)
	S += NY14 >= 146
	NY14 += MM[1]

	DY14__in = S.Task('DY14__in', length=1, delay_cost=1)
	S += DY14__in >= 148
	DY14__in += MAS_in[0]

	DY14__mem0 = S.Task('DY14__mem0', length=1, delay_cost=1)
	S += DY14__mem0 >= 148
	DY14__mem0 += MM_MEM[2]

	DY14__mem1 = S.Task('DY14__mem1', length=1, delay_cost=1)
	S += DY14__mem1 >= 148
	DY14__mem1 += MM_MEM[3]

	DY14_ = S.Task('DY14_', length=2, delay_cost=1)
	S += DY14_ >= 149
	DY14_ += MAS[0]


	# new tasks
	NY15_ = S.Task('NY15_', length=2, delay_cost=1)
	NY15_ += alt(MAS)
	NY15__in = S.Task('NY15__in', length=1, delay_cost=1)
	NY15__in += alt(MAS_in)
	S += NY15__in*MAS_in[0]<=NY15_*MAS[0]

	S += NY15__in*MAS_in[1]<=NY15_*MAS[1]

	S += NY15__in*MAS_in[2]<=NY15_*MAS[2]

	S += NY15__in*MAS_in[3]<=NY15_*MAS[3]

	S += NY15__in*MAS_in[4]<=NY15_*MAS[4]

	S += NY15__in*MAS_in[5]<=NY15_*MAS[5]

	NY15__mem0 = S.Task('NY15__mem0', length=1, delay_cost=1)
	NY15__mem0 += MM_MEM[2]
	S += 153 < NY15__mem0
	S += NY15__mem0 <= NY15_

	NY15__mem1 = S.Task('NY15__mem1', length=1, delay_cost=1)
	NY15__mem1 += MM_MEM[1]
	S += 122 < NY15__mem1
	S += NY15__mem1 <= NY15_

	DY14 = S.Task('DY14', length=8, delay_cost=1)
	DY14 += alt(MM)
	DY14_in = S.Task('DY14_in', length=1, delay_cost=1)
	DY14_in += alt(MM_in)
	S += DY14_in*MM_in[0]<=DY14*MM[0]
	S += DY14_in*MM_in[1]<=DY14*MM[1]
	DY14_mem0 = S.Task('DY14_mem0', length=1, delay_cost=1)
	DY14_mem0 += MAS_MEM[0]
	S += 150 < DY14_mem0
	S += DY14_mem0 <= DY14

	DY14_mem1 = S.Task('DY14_mem1', length=1, delay_cost=1)
	DY14_mem1 += MAIN_MEM_r[1]
	S += DY14_mem1 <= DY14

	NY = S.Task('NY', length=8, delay_cost=1)
	NY += alt(MM)
	NY_in = S.Task('NY_in', length=1, delay_cost=1)
	NY_in += alt(MM_in)
	S += NY_in*MM_in[0]<=NY*MM[0]
	S += NY_in*MM_in[1]<=NY*MM[1]
	NY_mem0 = S.Task('NY_mem0', length=1, delay_cost=1)
	NY_mem0 += alt(MAS_MEM)
	S += (NY15_*MAS[0])-1 < NY_mem0*MAS_MEM[0]
	S += (NY15_*MAS[1])-1 < NY_mem0*MAS_MEM[2]
	S += (NY15_*MAS[2])-1 < NY_mem0*MAS_MEM[4]
	S += (NY15_*MAS[3])-1 < NY_mem0*MAS_MEM[6]
	S += (NY15_*MAS[4])-1 < NY_mem0*MAS_MEM[8]
	S += (NY15_*MAS[5])-1 < NY_mem0*MAS_MEM[10]
	S += NY_mem0 <= NY

	NY_mem1 = S.Task('NY_mem1', length=1, delay_cost=1)
	NY_mem1 += MAIN_MEM_r[1]
	S += NY_mem1 <= NY

	DY = S.Task('DY', length=2, delay_cost=1)
	DY += alt(MAS)
	DY_in = S.Task('DY_in', length=1, delay_cost=1)
	DY_in += alt(MAS_in)
	S += DY_in*MAS_in[0]<=DY*MAS[0]

	S += DY_in*MAS_in[1]<=DY*MAS[1]

	S += DY_in*MAS_in[2]<=DY*MAS[2]

	S += DY_in*MAS_in[3]<=DY*MAS[3]

	S += DY_in*MAS_in[4]<=DY*MAS[4]

	S += DY_in*MAS_in[5]<=DY*MAS[5]

	DY_mem0 = S.Task('DY_mem0', length=1, delay_cost=1)
	DY_mem0 += alt(MM_MEM)
	S += (DY14*MM[0])-1 < DY_mem0*MM_MEM[0]
	S += (DY14*MM[1])-1 < DY_mem0*MM_MEM[2]
	S += DY_mem0 <= DY

	DY_mem1 = S.Task('DY_mem1', length=1, delay_cost=1)
	DY_mem1 += MM_MEM[1]
	S += 128 < DY_mem1
	S += DY_mem1 <= DY

	Z_new = S.Task('Z_new', length=8, delay_cost=1)
	Z_new += alt(MM)
	Z_new_in = S.Task('Z_new_in', length=1, delay_cost=1)
	Z_new_in += alt(MM_in)
	S += Z_new_in*MM_in[0]<=Z_new*MM[0]
	S += Z_new_in*MM_in[1]<=Z_new*MM[1]
	S += 0<Z_new

	Z_new_w = S.Task('Z_new_w', length=1, delay_cost=1)
	Z_new_w += alt(MAIN_MEM_w)
	S += Z_new <= Z_new_w

	Z_new_mem0 = S.Task('Z_new_mem0', length=1, delay_cost=1)
	Z_new_mem0 += MAS_MEM[8]
	S += 111 < Z_new_mem0
	S += Z_new_mem0 <= Z_new

	Z_new_mem1 = S.Task('Z_new_mem1', length=1, delay_cost=1)
	Z_new_mem1 += alt(MAS_MEM)
	S += (DY*MAS[0])-1 < Z_new_mem1*MAS_MEM[1]
	S += (DY*MAS[1])-1 < Z_new_mem1*MAS_MEM[3]
	S += (DY*MAS[2])-1 < Z_new_mem1*MAS_MEM[5]
	S += (DY*MAS[3])-1 < Z_new_mem1*MAS_MEM[7]
	S += (DY*MAS[4])-1 < Z_new_mem1*MAS_MEM[9]
	S += (DY*MAS[5])-1 < Z_new_mem1*MAS_MEM[11]
	S += Z_new_mem1 <= Z_new

	X_new = S.Task('X_new', length=8, delay_cost=1)
	X_new += alt(MM)
	X_new_in = S.Task('X_new_in', length=1, delay_cost=1)
	X_new_in += alt(MM_in)
	S += X_new_in*MM_in[0]<=X_new*MM[0]
	S += X_new_in*MM_in[1]<=X_new*MM[1]
	S += 0<X_new

	X_new_w = S.Task('X_new_w', length=1, delay_cost=1)
	X_new_w += alt(MAIN_MEM_w)
	S += X_new <= X_new_w

	X_new_mem0 = S.Task('X_new_mem0', length=1, delay_cost=1)
	X_new_mem0 += MAS_MEM[10]
	S += 118 < X_new_mem0
	S += X_new_mem0 <= X_new

	X_new_mem1 = S.Task('X_new_mem1', length=1, delay_cost=1)
	X_new_mem1 += alt(MAS_MEM)
	S += (DY*MAS[0])-1 < X_new_mem1*MAS_MEM[1]
	S += (DY*MAS[1])-1 < X_new_mem1*MAS_MEM[3]
	S += (DY*MAS[2])-1 < X_new_mem1*MAS_MEM[5]
	S += (DY*MAS[3])-1 < X_new_mem1*MAS_MEM[7]
	S += (DY*MAS[4])-1 < X_new_mem1*MAS_MEM[9]
	S += (DY*MAS[5])-1 < X_new_mem1*MAS_MEM[11]
	S += X_new_mem1 <= X_new

	Y_new = S.Task('Y_new', length=8, delay_cost=1)
	Y_new += alt(MM)
	Y_new_in = S.Task('Y_new_in', length=1, delay_cost=1)
	Y_new_in += alt(MM_in)
	S += Y_new_in*MM_in[0]<=Y_new*MM[0]
	S += Y_new_in*MM_in[1]<=Y_new*MM[1]
	S += 0<Y_new

	Y_new_w = S.Task('Y_new_w', length=1, delay_cost=1)
	Y_new_w += alt(MAIN_MEM_w)
	S += Y_new <= Y_new_w

	Y_new_mem0 = S.Task('Y_new_mem0', length=1, delay_cost=1)
	Y_new_mem0 += alt(MM_MEM)
	S += (NY*MM[0])-1 < Y_new_mem0*MM_MEM[0]
	S += (NY*MM[1])-1 < Y_new_mem0*MM_MEM[2]
	S += Y_new_mem0 <= Y_new

	Y_new_mem1 = S.Task('Y_new_mem1', length=1, delay_cost=1)
	Y_new_mem1 += MAS_MEM[9]
	S += 111 < Y_new_mem1
	S += Y_new_mem1 <= Y_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM2_stage2MAS6/ISOGENY/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

