from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 317
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 0
	Z_exp2_in += MM_in[1]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 0
	Z_exp2_mem0 += MAIN_MEM_r[0]

	Z_exp2_mem1 = S.Task('Z_exp2_mem1', length=1, delay_cost=1)
	S += Z_exp2_mem1 >= 0
	Z_exp2_mem1 += MAIN_MEM_r[1]

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 1
	NX0_in += MM_in[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 1
	NX0_mem0 += MAIN_MEM_r[0]

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 1
	NX0_mem1 += MAIN_MEM_r[1]

	Z_exp2 = S.Task('Z_exp2', length=11, delay_cost=1)
	S += Z_exp2 >= 1
	Z_exp2 += MM[1]

	NX0 = S.Task('NX0', length=11, delay_cost=1)
	S += NX0 >= 2
	NX0 += MM[0]

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 2
	k0_10_Z1_in += MM_in[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 2
	k0_10_Z1_mem0 += MAIN_MEM_r[0]

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 2
	k0_10_Z1_mem1 += MAIN_MEM_r[1]

	k0_10_Z1 = S.Task('k0_10_Z1', length=11, delay_cost=1)
	S += k0_10_Z1 >= 3
	k0_10_Z1 += MM[0]

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
	NY0_in += MM_in[1]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 4
	NY0_mem0 += MAIN_MEM_r[0]

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 4
	NY0_mem1 += MAIN_MEM_r[1]

	k2_14_Z1 = S.Task('k2_14_Z1', length=11, delay_cost=1)
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

	NY0 = S.Task('NY0', length=11, delay_cost=1)
	S += NY0 >= 5
	NY0 += MM[1]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 6
	DX0_in += MM_in[1]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 6
	DX0_mem0 += MAIN_MEM_r[0]

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 6
	DX0_mem1 += MAIN_MEM_r[1]

	DY0 = S.Task('DY0', length=11, delay_cost=1)
	S += DY0 >= 6
	DY0 += MM[0]

	DX0 = S.Task('DX0', length=11, delay_cost=1)
	S += DX0 >= 7
	DX0 += MM[1]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 11
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 11
	Z_exp3_mem0 += MM_MEM[2]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 11
	Z_exp3_mem1 += MAIN_MEM_r[1]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 11
	k1_9_Z2_in += MM_in[1]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 11
	k1_9_Z2_mem0 += MAIN_MEM_r[0]

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 11
	k1_9_Z2_mem1 += MM_MEM[3]

	Z_exp3 = S.Task('Z_exp3', length=11, delay_cost=1)
	S += Z_exp3 >= 12
	Z_exp3 += MM[0]

	k1_9_Z2 = S.Task('k1_9_Z2', length=11, delay_cost=1)
	S += k1_9_Z2 >= 12
	k1_9_Z2 += MM[1]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 12
	k3_14_Z2_in += MM_in[1]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 12
	k3_14_Z2_mem0 += MAIN_MEM_r[0]

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 12
	k3_14_Z2_mem1 += MM_MEM[3]

	NX1__in = S.Task('NX1__in', length=1, delay_cost=1)
	S += NX1__in >= 13
	NX1__in += MAS_in[2]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 13
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 13
	NX1__mem1 += MM_MEM[1]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 13
	k2_13_Z2_in += MM_in[1]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 13
	k2_13_Z2_mem0 += MAIN_MEM_r[0]

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 13
	k2_13_Z2_mem1 += MM_MEM[3]

	k3_14_Z2 = S.Task('k3_14_Z2', length=11, delay_cost=1)
	S += k3_14_Z2 >= 13
	k3_14_Z2 += MM[1]

	NX1_ = S.Task('NX1_', length=2, delay_cost=1)
	S += NX1_ >= 14
	NX1_ += MAS[2]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 14
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 14
	k0_9_Z2_mem0 += MAIN_MEM_r[0]

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 14
	k0_9_Z2_mem1 += MM_MEM[3]

	k2_13_Z2 = S.Task('k2_13_Z2', length=11, delay_cost=1)
	S += k2_13_Z2 >= 14
	k2_13_Z2 += MM[1]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 15
	NX1_in += MM_in[1]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 15
	NX1_mem0 += MAS_MEM[4]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 15
	NX1_mem1 += MAIN_MEM_r[1]

	NY1__in = S.Task('NY1__in', length=1, delay_cost=1)
	S += NY1__in >= 15
	NY1__in += MAS_in[3]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 15
	NY1__mem0 += MM_MEM[2]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 15
	NY1__mem1 += MM_MEM[1]

	k0_9_Z2 = S.Task('k0_9_Z2', length=11, delay_cost=1)
	S += k0_9_Z2 >= 15
	k0_9_Z2 += MM[0]

	NX1 = S.Task('NX1', length=11, delay_cost=1)
	S += NX1 >= 16
	NX1 += MM[1]

	NY1_ = S.Task('NY1_', length=2, delay_cost=1)
	S += NY1_ >= 16
	NY1_ += MAS[3]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 17
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 17
	NY1_mem0 += MAS_MEM[6]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 17
	NY1_mem1 += MAIN_MEM_r[1]

	NY1 = S.Task('NY1', length=11, delay_cost=1)
	S += NY1 >= 18
	NY1 += MM[0]

	DX1__in = S.Task('DX1__in', length=1, delay_cost=1)
	S += DX1__in >= 22
	DX1__in += MAS_in[2]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 22
	DX1__mem0 += MM_MEM[2]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 22
	DX1__mem1 += MM_MEM[3]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 22
	Z_exp4_in += MM_in[1]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 22
	Z_exp4_mem0 += MM_MEM[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 22
	Z_exp4_mem1 += MAIN_MEM_r[1]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 22
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 22
	k3_13_Z3_mem0 += MAIN_MEM_r[0]

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 22
	k3_13_Z3_mem1 += MM_MEM[1]

	DX1_ = S.Task('DX1_', length=2, delay_cost=1)
	S += DX1_ >= 23
	DX1_ += MAS[2]

	DY1__in = S.Task('DY1__in', length=1, delay_cost=1)
	S += DY1__in >= 23
	DY1__in += MAS_in[2]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 23
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 23
	DY1__mem1 += MM_MEM[3]

	Z_exp4 = S.Task('Z_exp4', length=11, delay_cost=1)
	S += Z_exp4 >= 23
	Z_exp4 += MM[1]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 23
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 23
	k2_12_Z3_mem0 += MAIN_MEM_r[0]

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 23
	k2_12_Z3_mem1 += MM_MEM[1]

	k3_13_Z3 = S.Task('k3_13_Z3', length=11, delay_cost=1)
	S += k3_13_Z3 >= 23
	k3_13_Z3 += MM[0]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 24
	DX1_in += MM_in[1]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 24
	DX1_mem0 += MAS_MEM[4]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 24
	DX1_mem1 += MAIN_MEM_r[1]

	DY1_ = S.Task('DY1_', length=2, delay_cost=1)
	S += DY1_ >= 24
	DY1_ += MAS[2]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 24
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 24
	k0_8_Z3_mem0 += MAIN_MEM_r[0]

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 24
	k0_8_Z3_mem1 += MM_MEM[1]

	k2_12_Z3 = S.Task('k2_12_Z3', length=11, delay_cost=1)
	S += k2_12_Z3 >= 24
	k2_12_Z3 += MM[0]

	DX1 = S.Task('DX1', length=11, delay_cost=1)
	S += DX1 >= 25
	DX1 += MM[1]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 25
	DY1_in += MM_in[1]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 25
	DY1_mem0 += MAS_MEM[4]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 25
	DY1_mem1 += MAIN_MEM_r[1]

	k0_8_Z3 = S.Task('k0_8_Z3', length=11, delay_cost=1)
	S += k0_8_Z3 >= 25
	k0_8_Z3 += MM[0]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 25
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 25
	k1_8_Z3_mem0 += MAIN_MEM_r[0]

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 25
	k1_8_Z3_mem1 += MM_MEM[1]

	DY1 = S.Task('DY1', length=11, delay_cost=1)
	S += DY1 >= 26
	DY1 += MM[1]

	NX2__in = S.Task('NX2__in', length=1, delay_cost=1)
	S += NX2__in >= 26
	NX2__in += MAS_in[1]

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 26
	NX2__mem0 += MM_MEM[2]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 26
	NX2__mem1 += MM_MEM[1]

	k1_8_Z3 = S.Task('k1_8_Z3', length=11, delay_cost=1)
	S += k1_8_Z3 >= 26
	k1_8_Z3 += MM[0]

	NX2_ = S.Task('NX2_', length=2, delay_cost=1)
	S += NX2_ >= 27
	NX2_ += MAS[1]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 28
	NX2_in += MM_in[1]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 28
	NX2_mem0 += MAS_MEM[2]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 28
	NX2_mem1 += MAIN_MEM_r[1]

	NY2__in = S.Task('NY2__in', length=1, delay_cost=1)
	S += NY2__in >= 28
	NY2__in += MAS_in[2]

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 28
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 28
	NY2__mem1 += MM_MEM[3]

	NX2 = S.Task('NX2', length=11, delay_cost=1)
	S += NX2 >= 29
	NX2 += MM[1]

	NY2_ = S.Task('NY2_', length=2, delay_cost=1)
	S += NY2_ >= 29
	NY2_ += MAS[2]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 30
	NY2_in += MM_in[1]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 30
	NY2_mem0 += MAS_MEM[4]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 30
	NY2_mem1 += MAIN_MEM_r[1]

	NY2 = S.Task('NY2', length=11, delay_cost=1)
	S += NY2 >= 31
	NY2 += MM[1]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 33
	Z_exp5_in += MM_in[1]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 33
	Z_exp5_mem0 += MM_MEM[2]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 33
	Z_exp5_mem1 += MAIN_MEM_r[1]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 33
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 33
	k3_12_Z4_mem0 += MAIN_MEM_r[0]

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 33
	k3_12_Z4_mem1 += MM_MEM[3]

	Z_exp5 = S.Task('Z_exp5', length=11, delay_cost=1)
	S += Z_exp5 >= 34
	Z_exp5 += MM[1]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 34
	k1_7_Z4_in += MM_in[1]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 34
	k1_7_Z4_mem0 += MAIN_MEM_r[0]

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 34
	k1_7_Z4_mem1 += MM_MEM[3]

	k3_12_Z4 = S.Task('k3_12_Z4', length=11, delay_cost=1)
	S += k3_12_Z4 >= 34
	k3_12_Z4 += MM[0]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 35
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 35
	k0_7_Z4_mem0 += MAIN_MEM_r[0]

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 35
	k0_7_Z4_mem1 += MM_MEM[3]

	k1_7_Z4 = S.Task('k1_7_Z4', length=11, delay_cost=1)
	S += k1_7_Z4 >= 35
	k1_7_Z4 += MM[1]

	DY2__in = S.Task('DY2__in', length=1, delay_cost=1)
	S += DY2__in >= 36
	DY2__in += MAS_in[2]

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 36
	DY2__mem0 += MM_MEM[2]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 36
	DY2__mem1 += MM_MEM[1]

	k0_7_Z4 = S.Task('k0_7_Z4', length=11, delay_cost=1)
	S += k0_7_Z4 >= 36
	k0_7_Z4 += MM[0]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 36
	k2_11_Z4_in += MM_in[1]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 36
	k2_11_Z4_mem0 += MAIN_MEM_r[0]

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 36
	k2_11_Z4_mem1 += MM_MEM[3]

	DX2__in = S.Task('DX2__in', length=1, delay_cost=1)
	S += DX2__in >= 37
	DX2__in += MAS_in[2]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 37
	DX2__mem0 += MM_MEM[2]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 37
	DX2__mem1 += MM_MEM[1]

	DY2_ = S.Task('DY2_', length=2, delay_cost=1)
	S += DY2_ >= 37
	DY2_ += MAS[2]

	k2_11_Z4 = S.Task('k2_11_Z4', length=11, delay_cost=1)
	S += k2_11_Z4 >= 37
	k2_11_Z4 += MM[1]

	DX2_ = S.Task('DX2_', length=2, delay_cost=1)
	S += DX2_ >= 38
	DX2_ += MAS[2]

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 38
	DY2_in += MM_in[1]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 38
	DY2_mem0 += MAS_MEM[4]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 38
	DY2_mem1 += MAIN_MEM_r[1]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 39
	DX2_in += MM_in[1]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 39
	DX2_mem0 += MAS_MEM[4]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 39
	DX2_mem1 += MAIN_MEM_r[1]

	DY2 = S.Task('DY2', length=11, delay_cost=1)
	S += DY2 >= 39
	DY2 += MM[1]

	NX3__in = S.Task('NX3__in', length=1, delay_cost=1)
	S += NX3__in >= 39
	NX3__in += MAS_in[2]

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 39
	NX3__mem0 += MM_MEM[2]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 39
	NX3__mem1 += MM_MEM[1]

	DX2 = S.Task('DX2', length=11, delay_cost=1)
	S += DX2 >= 40
	DX2 += MM[1]

	NX3_ = S.Task('NX3_', length=2, delay_cost=1)
	S += NX3_ >= 40
	NX3_ += MAS[2]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 41
	NX3_in += MM_in[1]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 41
	NX3_mem0 += MAS_MEM[4]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 41
	NX3_mem1 += MAIN_MEM_r[1]

	NY3__in = S.Task('NY3__in', length=1, delay_cost=1)
	S += NY3__in >= 41
	NY3__in += MAS_in[2]

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 41
	NY3__mem0 += MM_MEM[2]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 41
	NY3__mem1 += MM_MEM[1]

	NX3 = S.Task('NX3', length=11, delay_cost=1)
	S += NX3 >= 42
	NX3 += MM[1]

	NY3_ = S.Task('NY3_', length=2, delay_cost=1)
	S += NY3_ >= 42
	NY3_ += MAS[2]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 43
	NY3_in += MM_in[1]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 43
	NY3_mem0 += MAS_MEM[4]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 43
	NY3_mem1 += MAIN_MEM_r[1]

	NY3 = S.Task('NY3', length=11, delay_cost=1)
	S += NY3 >= 44
	NY3 += MM[1]

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	S += Z_exp6_in >= 44
	Z_exp6_in += MM_in[0]

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	S += Z_exp6_mem0 >= 44
	Z_exp6_mem0 += MM_MEM[2]

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	S += Z_exp6_mem1 >= 44
	Z_exp6_mem1 += MAIN_MEM_r[1]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 44
	k2_10_Z5_in += MM_in[1]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 44
	k2_10_Z5_mem0 += MAIN_MEM_r[0]

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 44
	k2_10_Z5_mem1 += MM_MEM[3]

	Z_exp6 = S.Task('Z_exp6', length=11, delay_cost=1)
	S += Z_exp6 >= 45
	Z_exp6 += MM[0]

	k2_10_Z5 = S.Task('k2_10_Z5', length=11, delay_cost=1)
	S += k2_10_Z5 >= 45
	k2_10_Z5 += MM[1]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 45
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 45
	k3_11_Z5_mem0 += MAIN_MEM_r[0]

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 45
	k3_11_Z5_mem1 += MM_MEM[3]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 46
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 46
	k1_6_Z5_mem0 += MAIN_MEM_r[0]

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 46
	k1_6_Z5_mem1 += MM_MEM[3]

	k3_11_Z5 = S.Task('k3_11_Z5', length=11, delay_cost=1)
	S += k3_11_Z5 >= 46
	k3_11_Z5 += MM[0]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 47
	k0_6_Z5_in += MM_in[1]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 47
	k0_6_Z5_mem0 += MAIN_MEM_r[0]

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 47
	k0_6_Z5_mem1 += MM_MEM[3]

	k1_6_Z5 = S.Task('k1_6_Z5', length=11, delay_cost=1)
	S += k1_6_Z5 >= 47
	k1_6_Z5 += MM[0]

	k0_6_Z5 = S.Task('k0_6_Z5', length=11, delay_cost=1)
	S += k0_6_Z5 >= 48
	k0_6_Z5 += MM[1]

	DY3__in = S.Task('DY3__in', length=1, delay_cost=1)
	S += DY3__in >= 49
	DY3__in += MAS_in[0]

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	S += DY3__mem0 >= 49
	DY3__mem0 += MM_MEM[2]

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	S += DY3__mem1 >= 49
	DY3__mem1 += MM_MEM[1]

	DX3__in = S.Task('DX3__in', length=1, delay_cost=1)
	S += DX3__in >= 50
	DX3__in += MAS_in[2]

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	S += DX3__mem0 >= 50
	DX3__mem0 += MM_MEM[2]

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	S += DX3__mem1 >= 50
	DX3__mem1 += MM_MEM[3]

	DY3_ = S.Task('DY3_', length=2, delay_cost=1)
	S += DY3_ >= 50
	DY3_ += MAS[0]

	DX3_ = S.Task('DX3_', length=2, delay_cost=1)
	S += DX3_ >= 51
	DX3_ += MAS[2]

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	S += DY3_in >= 51
	DY3_in += MM_in[1]

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	S += DY3_mem0 >= 51
	DY3_mem0 += MAS_MEM[0]

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	S += DY3_mem1 >= 51
	DY3_mem1 += MAIN_MEM_r[1]

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	S += DX3_in >= 52
	DX3_in += MM_in[1]

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	S += DX3_mem0 >= 52
	DX3_mem0 += MAS_MEM[4]

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	S += DX3_mem1 >= 52
	DX3_mem1 += MAIN_MEM_r[1]

	DY3 = S.Task('DY3', length=11, delay_cost=1)
	S += DY3 >= 52
	DY3 += MM[1]

	NX4__in = S.Task('NX4__in', length=1, delay_cost=1)
	S += NX4__in >= 52
	NX4__in += MAS_in[2]

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 52
	NX4__mem0 += MM_MEM[2]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 52
	NX4__mem1 += MM_MEM[1]

	DX3 = S.Task('DX3', length=11, delay_cost=1)
	S += DX3 >= 53
	DX3 += MM[1]

	NX4_ = S.Task('NX4_', length=2, delay_cost=1)
	S += NX4_ >= 53
	NX4_ += MAS[2]

	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	S += NX4_in >= 54
	NX4_in += MM_in[1]

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	S += NX4_mem0 >= 54
	NX4_mem0 += MAS_MEM[4]

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	S += NX4_mem1 >= 54
	NX4_mem1 += MAIN_MEM_r[1]

	NY4__in = S.Task('NY4__in', length=1, delay_cost=1)
	S += NY4__in >= 54
	NY4__in += MAS_in[2]

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 54
	NY4__mem0 += MM_MEM[2]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 54
	NY4__mem1 += MM_MEM[3]

	NX4 = S.Task('NX4', length=11, delay_cost=1)
	S += NX4 >= 55
	NX4 += MM[1]

	NY4_ = S.Task('NY4_', length=2, delay_cost=1)
	S += NY4_ >= 55
	NY4_ += MAS[2]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 55
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 55
	Z_exp7_mem0 += MM_MEM[0]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 55
	Z_exp7_mem1 += MAIN_MEM_r[1]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 55
	k0_5_Z6_in += MM_in[1]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 55
	k0_5_Z6_mem0 += MAIN_MEM_r[0]

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 55
	k0_5_Z6_mem1 += MM_MEM[1]

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	S += NY4_in >= 56
	NY4_in += MM_in[1]

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	S += NY4_mem0 >= 56
	NY4_mem0 += MAS_MEM[4]

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	S += NY4_mem1 >= 56
	NY4_mem1 += MAIN_MEM_r[1]

	Z_exp7 = S.Task('Z_exp7', length=11, delay_cost=1)
	S += Z_exp7 >= 56
	Z_exp7 += MM[0]

	k0_5_Z6 = S.Task('k0_5_Z6', length=11, delay_cost=1)
	S += k0_5_Z6 >= 56
	k0_5_Z6 += MM[1]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 56
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 56
	k2_9_Z6_mem0 += MAIN_MEM_r[0]

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 56
	k2_9_Z6_mem1 += MM_MEM[1]

	NY4 = S.Task('NY4', length=11, delay_cost=1)
	S += NY4 >= 57
	NY4 += MM[1]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 57
	k1_5_Z6_in += MM_in[0]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 57
	k1_5_Z6_mem0 += MAIN_MEM_r[0]

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 57
	k1_5_Z6_mem1 += MM_MEM[1]

	k2_9_Z6 = S.Task('k2_9_Z6', length=11, delay_cost=1)
	S += k2_9_Z6 >= 57
	k2_9_Z6 += MM[0]

	k1_5_Z6 = S.Task('k1_5_Z6', length=11, delay_cost=1)
	S += k1_5_Z6 >= 58
	k1_5_Z6 += MM[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 58
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 58
	k3_10_Z6_mem0 += MAIN_MEM_r[0]

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 58
	k3_10_Z6_mem1 += MM_MEM[1]

	k3_10_Z6 = S.Task('k3_10_Z6', length=11, delay_cost=1)
	S += k3_10_Z6 >= 59
	k3_10_Z6 += MM[0]

	DY4__in = S.Task('DY4__in', length=1, delay_cost=1)
	S += DY4__in >= 62
	DY4__in += MAS_in[2]

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	S += DY4__mem0 >= 62
	DY4__mem0 += MM_MEM[2]

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	S += DY4__mem1 >= 62
	DY4__mem1 += MM_MEM[1]

	DX4__in = S.Task('DX4__in', length=1, delay_cost=1)
	S += DX4__in >= 63
	DX4__in += MAS_in[2]

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	S += DX4__mem0 >= 63
	DX4__mem0 += MM_MEM[2]

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	S += DX4__mem1 >= 63
	DX4__mem1 += MM_MEM[1]

	DY4_ = S.Task('DY4_', length=2, delay_cost=1)
	S += DY4_ >= 63
	DY4_ += MAS[2]

	DX4_ = S.Task('DX4_', length=2, delay_cost=1)
	S += DX4_ >= 64
	DX4_ += MAS[2]

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	S += DY4_in >= 64
	DY4_in += MM_in[0]

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	S += DY4_mem0 >= 64
	DY4_mem0 += MAS_MEM[4]

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	S += DY4_mem1 >= 64
	DY4_mem1 += MAIN_MEM_r[1]

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	S += DX4_in >= 65
	DX4_in += MM_in[0]

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	S += DX4_mem0 >= 65
	DX4_mem0 += MAS_MEM[4]

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	S += DX4_mem1 >= 65
	DX4_mem1 += MAIN_MEM_r[1]

	DY4 = S.Task('DY4', length=11, delay_cost=1)
	S += DY4 >= 65
	DY4 += MM[0]

	NX5__in = S.Task('NX5__in', length=1, delay_cost=1)
	S += NX5__in >= 65
	NX5__in += MAS_in[2]

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	S += NX5__mem0 >= 65
	NX5__mem0 += MM_MEM[2]

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	S += NX5__mem1 >= 65
	NX5__mem1 += MM_MEM[3]

	DX4 = S.Task('DX4', length=11, delay_cost=1)
	S += DX4 >= 66
	DX4 += MM[0]

	NX5_ = S.Task('NX5_', length=2, delay_cost=1)
	S += NX5_ >= 66
	NX5_ += MAS[2]

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	S += Z_exp8_in >= 66
	Z_exp8_in += MM_in[1]

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	S += Z_exp8_mem0 >= 66
	Z_exp8_mem0 += MM_MEM[0]

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	S += Z_exp8_mem1 >= 66
	Z_exp8_mem1 += MAIN_MEM_r[1]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 66
	k3_9_Z7_in += MM_in[0]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 66
	k3_9_Z7_mem0 += MAIN_MEM_r[0]

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 66
	k3_9_Z7_mem1 += MM_MEM[1]

	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	S += NX5_in >= 67
	NX5_in += MM_in[0]

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	S += NX5_mem0 >= 67
	NX5_mem0 += MAS_MEM[4]

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	S += NX5_mem1 >= 67
	NX5_mem1 += MAIN_MEM_r[1]

	NY5__in = S.Task('NY5__in', length=1, delay_cost=1)
	S += NY5__in >= 67
	NY5__in += MAS_in[2]

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	S += NY5__mem0 >= 67
	NY5__mem0 += MM_MEM[2]

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	S += NY5__mem1 >= 67
	NY5__mem1 += MM_MEM[3]

	Z_exp8 = S.Task('Z_exp8', length=11, delay_cost=1)
	S += Z_exp8 >= 67
	Z_exp8 += MM[1]

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	S += k2_8_Z7_in >= 67
	k2_8_Z7_in += MM_in[1]

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	S += k2_8_Z7_mem0 >= 67
	k2_8_Z7_mem0 += MAIN_MEM_r[0]

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	S += k2_8_Z7_mem1 >= 67
	k2_8_Z7_mem1 += MM_MEM[1]

	k3_9_Z7 = S.Task('k3_9_Z7', length=11, delay_cost=1)
	S += k3_9_Z7 >= 67
	k3_9_Z7 += MM[0]

	NX5 = S.Task('NX5', length=11, delay_cost=1)
	S += NX5 >= 68
	NX5 += MM[0]

	NY5_ = S.Task('NY5_', length=2, delay_cost=1)
	S += NY5_ >= 68
	NY5_ += MAS[2]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 68
	k1_4_Z7_in += MM_in[1]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 68
	k1_4_Z7_mem0 += MAIN_MEM_r[0]

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 68
	k1_4_Z7_mem1 += MM_MEM[1]

	k2_8_Z7 = S.Task('k2_8_Z7', length=11, delay_cost=1)
	S += k2_8_Z7 >= 68
	k2_8_Z7 += MM[1]

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	S += NY5_in >= 69
	NY5_in += MM_in[0]

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	S += NY5_mem0 >= 69
	NY5_mem0 += MAS_MEM[4]

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	S += NY5_mem1 >= 69
	NY5_mem1 += MAIN_MEM_r[1]

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	S += k0_4_Z7_in >= 69
	k0_4_Z7_in += MM_in[1]

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	S += k0_4_Z7_mem0 >= 69
	k0_4_Z7_mem0 += MAIN_MEM_r[0]

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	S += k0_4_Z7_mem1 >= 69
	k0_4_Z7_mem1 += MM_MEM[1]

	k1_4_Z7 = S.Task('k1_4_Z7', length=11, delay_cost=1)
	S += k1_4_Z7 >= 69
	k1_4_Z7 += MM[1]

	NY5 = S.Task('NY5', length=11, delay_cost=1)
	S += NY5 >= 70
	NY5 += MM[0]

	k0_4_Z7 = S.Task('k0_4_Z7', length=11, delay_cost=1)
	S += k0_4_Z7 >= 70
	k0_4_Z7 += MM[1]

	DY5__in = S.Task('DY5__in', length=1, delay_cost=1)
	S += DY5__in >= 75
	DY5__in += MAS_in[0]

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	S += DY5__mem0 >= 75
	DY5__mem0 += MM_MEM[0]

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	S += DY5__mem1 >= 75
	DY5__mem1 += MM_MEM[1]

	DX5__in = S.Task('DX5__in', length=1, delay_cost=1)
	S += DX5__in >= 76
	DX5__in += MAS_in[0]

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	S += DX5__mem0 >= 76
	DX5__mem0 += MM_MEM[0]

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	S += DX5__mem1 >= 76
	DX5__mem1 += MM_MEM[1]

	DY5_ = S.Task('DY5_', length=2, delay_cost=1)
	S += DY5_ >= 76
	DY5_ += MAS[0]

	DX5_ = S.Task('DX5_', length=2, delay_cost=1)
	S += DX5_ >= 77
	DX5_ += MAS[0]

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	S += Z_exp9_in >= 77
	Z_exp9_in += MM_in[1]

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	S += Z_exp9_mem0 >= 77
	Z_exp9_mem0 += MM_MEM[2]

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	S += Z_exp9_mem1 >= 77
	Z_exp9_mem1 += MAIN_MEM_r[1]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 77
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 77
	k2_7_Z8_mem0 += MAIN_MEM_r[0]

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 77
	k2_7_Z8_mem1 += MM_MEM[3]

	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	S += DY5_in >= 78
	DY5_in += MM_in[1]

	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	S += DY5_mem0 >= 78
	DY5_mem0 += MAS_MEM[0]

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	S += DY5_mem1 >= 78
	DY5_mem1 += MAIN_MEM_r[1]

	Z_exp9 = S.Task('Z_exp9', length=11, delay_cost=1)
	S += Z_exp9 >= 78
	Z_exp9 += MM[1]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 78
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 78
	k1_3_Z8_mem0 += MAIN_MEM_r[0]

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 78
	k1_3_Z8_mem1 += MM_MEM[3]

	k2_7_Z8 = S.Task('k2_7_Z8', length=11, delay_cost=1)
	S += k2_7_Z8 >= 78
	k2_7_Z8 += MM[0]

	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	S += DX5_in >= 79
	DX5_in += MM_in[0]

	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	S += DX5_mem0 >= 79
	DX5_mem0 += MAS_MEM[0]

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	S += DX5_mem1 >= 79
	DX5_mem1 += MAIN_MEM_r[1]

	DY5 = S.Task('DY5', length=11, delay_cost=1)
	S += DY5 >= 79
	DY5 += MM[1]

	k1_3_Z8 = S.Task('k1_3_Z8', length=11, delay_cost=1)
	S += k1_3_Z8 >= 79
	k1_3_Z8 += MM[0]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 79
	k3_8_Z8_in += MM_in[1]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 79
	k3_8_Z8_mem0 += MAIN_MEM_r[0]

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 79
	k3_8_Z8_mem1 += MM_MEM[3]

	DX5 = S.Task('DX5', length=11, delay_cost=1)
	S += DX5 >= 80
	DX5 += MM[0]

	NY6__in = S.Task('NY6__in', length=1, delay_cost=1)
	S += NY6__in >= 80
	NY6__in += MAS_in[2]

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	S += NY6__mem0 >= 80
	NY6__mem0 += MM_MEM[0]

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	S += NY6__mem1 >= 80
	NY6__mem1 += MM_MEM[1]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 80
	k0_3_Z8_in += MM_in[0]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 80
	k0_3_Z8_mem0 += MAIN_MEM_r[0]

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 80
	k0_3_Z8_mem1 += MM_MEM[3]

	k3_8_Z8 = S.Task('k3_8_Z8', length=11, delay_cost=1)
	S += k3_8_Z8 >= 80
	k3_8_Z8 += MM[1]

	NX6__in = S.Task('NX6__in', length=1, delay_cost=1)
	S += NX6__in >= 81
	NX6__in += MAS_in[2]

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	S += NX6__mem0 >= 81
	NX6__mem0 += MM_MEM[0]

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	S += NX6__mem1 >= 81
	NX6__mem1 += MM_MEM[3]

	NY6_ = S.Task('NY6_', length=2, delay_cost=1)
	S += NY6_ >= 81
	NY6_ += MAS[2]

	k0_3_Z8 = S.Task('k0_3_Z8', length=11, delay_cost=1)
	S += k0_3_Z8 >= 81
	k0_3_Z8 += MM[0]

	NX6_ = S.Task('NX6_', length=2, delay_cost=1)
	S += NX6_ >= 82
	NX6_ += MAS[2]

	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	S += NY6_in >= 82
	NY6_in += MM_in[1]

	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	S += NY6_mem0 >= 82
	NY6_mem0 += MAS_MEM[4]

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	S += NY6_mem1 >= 82
	NY6_mem1 += MAIN_MEM_r[1]

	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	S += NX6_in >= 83
	NX6_in += MM_in[1]

	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	S += NX6_mem0 >= 83
	NX6_mem0 += MAS_MEM[4]

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	S += NX6_mem1 >= 83
	NX6_mem1 += MAIN_MEM_r[1]

	NY6 = S.Task('NY6', length=11, delay_cost=1)
	S += NY6 >= 83
	NY6 += MM[1]

	NX6 = S.Task('NX6', length=11, delay_cost=1)
	S += NX6 >= 84
	NX6 += MM[1]

	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	S += Z_exp10_in >= 88
	Z_exp10_in += MM_in[0]

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	S += Z_exp10_mem0 >= 88
	Z_exp10_mem0 += MM_MEM[2]

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	S += Z_exp10_mem1 >= 88
	Z_exp10_mem1 += MAIN_MEM_r[1]

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	S += k3_7_Z9_in >= 88
	k3_7_Z9_in += MM_in[1]

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	S += k3_7_Z9_mem0 >= 88
	k3_7_Z9_mem0 += MAIN_MEM_r[0]

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	S += k3_7_Z9_mem1 >= 88
	k3_7_Z9_mem1 += MM_MEM[3]

	DY6__in = S.Task('DY6__in', length=1, delay_cost=1)
	S += DY6__in >= 89
	DY6__in += MAS_in[2]

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	S += DY6__mem0 >= 89
	DY6__mem0 += MM_MEM[2]

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	S += DY6__mem1 >= 89
	DY6__mem1 += MM_MEM[1]

	Z_exp10 = S.Task('Z_exp10', length=11, delay_cost=1)
	S += Z_exp10 >= 89
	Z_exp10 += MM[0]

	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	S += k0_2_Z9_in >= 89
	k0_2_Z9_in += MM_in[0]

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	S += k0_2_Z9_mem0 >= 89
	k0_2_Z9_mem0 += MAIN_MEM_r[0]

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	S += k0_2_Z9_mem1 >= 89
	k0_2_Z9_mem1 += MM_MEM[3]

	k3_7_Z9 = S.Task('k3_7_Z9', length=11, delay_cost=1)
	S += k3_7_Z9 >= 89
	k3_7_Z9 += MM[1]

	DX6__in = S.Task('DX6__in', length=1, delay_cost=1)
	S += DX6__in >= 90
	DX6__in += MAS_in[1]

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	S += DX6__mem0 >= 90
	DX6__mem0 += MM_MEM[0]

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	S += DX6__mem1 >= 90
	DX6__mem1 += MM_MEM[3]

	DY6_ = S.Task('DY6_', length=2, delay_cost=1)
	S += DY6_ >= 90
	DY6_ += MAS[2]

	k0_2_Z9 = S.Task('k0_2_Z9', length=11, delay_cost=1)
	S += k0_2_Z9 >= 90
	k0_2_Z9 += MM[0]

	DX6_ = S.Task('DX6_', length=2, delay_cost=1)
	S += DX6_ >= 91
	DX6_ += MAS[1]

	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	S += DY6_in >= 91
	DY6_in += MM_in[1]

	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	S += DY6_mem0 >= 91
	DY6_mem0 += MAS_MEM[4]

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	S += DY6_mem1 >= 91
	DY6_mem1 += MAIN_MEM_r[1]

	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	S += k2_6_Z9_in >= 91
	k2_6_Z9_in += MM_in[0]

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	S += k2_6_Z9_mem0 >= 91
	k2_6_Z9_mem0 += MAIN_MEM_r[0]

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	S += k2_6_Z9_mem1 >= 91
	k2_6_Z9_mem1 += MM_MEM[3]

	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	S += DX6_in >= 92
	DX6_in += MM_in[0]

	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	S += DX6_mem0 >= 92
	DX6_mem0 += MAS_MEM[2]

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	S += DX6_mem1 >= 92
	DX6_mem1 += MAIN_MEM_r[1]

	DY6 = S.Task('DY6', length=11, delay_cost=1)
	S += DY6 >= 92
	DY6 += MM[1]

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	S += k1_2_Z9_in >= 92
	k1_2_Z9_in += MM_in[1]

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	S += k1_2_Z9_mem0 >= 92
	k1_2_Z9_mem0 += MAIN_MEM_r[0]

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	S += k1_2_Z9_mem1 >= 92
	k1_2_Z9_mem1 += MM_MEM[3]

	k2_6_Z9 = S.Task('k2_6_Z9', length=11, delay_cost=1)
	S += k2_6_Z9 >= 92
	k2_6_Z9 += MM[0]

	DX6 = S.Task('DX6', length=11, delay_cost=1)
	S += DX6 >= 93
	DX6 += MM[0]

	NY7__in = S.Task('NY7__in', length=1, delay_cost=1)
	S += NY7__in >= 93
	NY7__in += MAS_in[2]

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	S += NY7__mem0 >= 93
	NY7__mem0 += MM_MEM[2]

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	S += NY7__mem1 >= 93
	NY7__mem1 += MM_MEM[3]

	k1_2_Z9 = S.Task('k1_2_Z9', length=11, delay_cost=1)
	S += k1_2_Z9 >= 93
	k1_2_Z9 += MM[1]

	NX7__in = S.Task('NX7__in', length=1, delay_cost=1)
	S += NX7__in >= 94
	NX7__in += MAS_in[2]

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	S += NX7__mem0 >= 94
	NX7__mem0 += MM_MEM[2]

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	S += NX7__mem1 >= 94
	NX7__mem1 += MM_MEM[3]

	NY7_ = S.Task('NY7_', length=2, delay_cost=1)
	S += NY7_ >= 94
	NY7_ += MAS[2]

	NX7_ = S.Task('NX7_', length=2, delay_cost=1)
	S += NX7_ >= 95
	NX7_ += MAS[2]

	NY7_in = S.Task('NY7_in', length=1, delay_cost=1)
	S += NY7_in >= 95
	NY7_in += MM_in[0]

	NY7_mem0 = S.Task('NY7_mem0', length=1, delay_cost=1)
	S += NY7_mem0 >= 95
	NY7_mem0 += MAS_MEM[4]

	NY7_mem1 = S.Task('NY7_mem1', length=1, delay_cost=1)
	S += NY7_mem1 >= 95
	NY7_mem1 += MAIN_MEM_r[1]

	NX7_in = S.Task('NX7_in', length=1, delay_cost=1)
	S += NX7_in >= 96
	NX7_in += MM_in[0]

	NX7_mem0 = S.Task('NX7_mem0', length=1, delay_cost=1)
	S += NX7_mem0 >= 96
	NX7_mem0 += MAS_MEM[4]

	NX7_mem1 = S.Task('NX7_mem1', length=1, delay_cost=1)
	S += NX7_mem1 >= 96
	NX7_mem1 += MAIN_MEM_r[1]

	NY7 = S.Task('NY7', length=11, delay_cost=1)
	S += NY7 >= 96
	NY7 += MM[0]

	NX7 = S.Task('NX7', length=11, delay_cost=1)
	S += NX7 >= 97
	NX7 += MM[0]

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	S += Z_exp11_in >= 99
	Z_exp11_in += MM_in[0]

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	S += Z_exp11_mem0 >= 99
	Z_exp11_mem0 += MM_MEM[0]

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	S += Z_exp11_mem1 >= 99
	Z_exp11_mem1 += MAIN_MEM_r[1]

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	S += k2_5_Z10_in >= 99
	k2_5_Z10_in += MM_in[1]

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	S += k2_5_Z10_mem0 >= 99
	k2_5_Z10_mem0 += MAIN_MEM_r[0]

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	S += k2_5_Z10_mem1 >= 99
	k2_5_Z10_mem1 += MM_MEM[1]

	Z_exp11 = S.Task('Z_exp11', length=11, delay_cost=1)
	S += Z_exp11 >= 100
	Z_exp11 += MM[0]

	k2_5_Z10 = S.Task('k2_5_Z10', length=11, delay_cost=1)
	S += k2_5_Z10 >= 100
	k2_5_Z10 += MM[1]

	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	S += k3_6_Z10_in >= 100
	k3_6_Z10_in += MM_in[1]

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	S += k3_6_Z10_mem0 >= 100
	k3_6_Z10_mem0 += MAIN_MEM_r[0]

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	S += k3_6_Z10_mem1 >= 100
	k3_6_Z10_mem1 += MM_MEM[1]

	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	S += k1_1_Z10_in >= 101
	k1_1_Z10_in += MM_in[0]

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	S += k1_1_Z10_mem0 >= 101
	k1_1_Z10_mem0 += MAIN_MEM_r[0]

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	S += k1_1_Z10_mem1 >= 101
	k1_1_Z10_mem1 += MM_MEM[1]

	k3_6_Z10 = S.Task('k3_6_Z10', length=11, delay_cost=1)
	S += k3_6_Z10 >= 101
	k3_6_Z10 += MM[1]

	DY7__in = S.Task('DY7__in', length=1, delay_cost=1)
	S += DY7__in >= 102
	DY7__in += MAS_in[2]

	DY7__mem0 = S.Task('DY7__mem0', length=1, delay_cost=1)
	S += DY7__mem0 >= 102
	DY7__mem0 += MM_MEM[2]

	DY7__mem1 = S.Task('DY7__mem1', length=1, delay_cost=1)
	S += DY7__mem1 >= 102
	DY7__mem1 += MM_MEM[3]

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	S += k0_1_Z10_in >= 102
	k0_1_Z10_in += MM_in[0]

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	S += k0_1_Z10_mem0 >= 102
	k0_1_Z10_mem0 += MAIN_MEM_r[0]

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	S += k0_1_Z10_mem1 >= 102
	k0_1_Z10_mem1 += MM_MEM[1]

	k1_1_Z10 = S.Task('k1_1_Z10', length=11, delay_cost=1)
	S += k1_1_Z10 >= 102
	k1_1_Z10 += MM[0]

	DX7__in = S.Task('DX7__in', length=1, delay_cost=1)
	S += DX7__in >= 103
	DX7__in += MAS_in[0]

	DX7__mem0 = S.Task('DX7__mem0', length=1, delay_cost=1)
	S += DX7__mem0 >= 103
	DX7__mem0 += MM_MEM[0]

	DX7__mem1 = S.Task('DX7__mem1', length=1, delay_cost=1)
	S += DX7__mem1 >= 103
	DX7__mem1 += MM_MEM[1]

	DY7_ = S.Task('DY7_', length=2, delay_cost=1)
	S += DY7_ >= 103
	DY7_ += MAS[2]

	k0_1_Z10 = S.Task('k0_1_Z10', length=11, delay_cost=1)
	S += k0_1_Z10 >= 103
	k0_1_Z10 += MM[0]

	DX7_ = S.Task('DX7_', length=2, delay_cost=1)
	S += DX7_ >= 104
	DX7_ += MAS[0]

	DY7_in = S.Task('DY7_in', length=1, delay_cost=1)
	S += DY7_in >= 104
	DY7_in += MM_in[0]

	DY7_mem0 = S.Task('DY7_mem0', length=1, delay_cost=1)
	S += DY7_mem0 >= 104
	DY7_mem0 += MAS_MEM[4]

	DY7_mem1 = S.Task('DY7_mem1', length=1, delay_cost=1)
	S += DY7_mem1 >= 104
	DY7_mem1 += MAIN_MEM_r[1]

	DX7_in = S.Task('DX7_in', length=1, delay_cost=1)
	S += DX7_in >= 105
	DX7_in += MM_in[0]

	DX7_mem0 = S.Task('DX7_mem0', length=1, delay_cost=1)
	S += DX7_mem0 >= 105
	DX7_mem0 += MAS_MEM[0]

	DX7_mem1 = S.Task('DX7_mem1', length=1, delay_cost=1)
	S += DX7_mem1 >= 105
	DX7_mem1 += MAIN_MEM_r[1]

	DY7 = S.Task('DY7', length=11, delay_cost=1)
	S += DY7 >= 105
	DY7 += MM[0]

	DX7 = S.Task('DX7', length=11, delay_cost=1)
	S += DX7 >= 106
	DX7 += MM[0]

	NY8__in = S.Task('NY8__in', length=1, delay_cost=1)
	S += NY8__in >= 106
	NY8__in += MAS_in[0]

	NY8__mem0 = S.Task('NY8__mem0', length=1, delay_cost=1)
	S += NY8__mem0 >= 106
	NY8__mem0 += MM_MEM[0]

	NY8__mem1 = S.Task('NY8__mem1', length=1, delay_cost=1)
	S += NY8__mem1 >= 106
	NY8__mem1 += MM_MEM[1]

	NX8__in = S.Task('NX8__in', length=1, delay_cost=1)
	S += NX8__in >= 107
	NX8__in += MAS_in[0]

	NX8__mem0 = S.Task('NX8__mem0', length=1, delay_cost=1)
	S += NX8__mem0 >= 107
	NX8__mem0 += MM_MEM[0]

	NX8__mem1 = S.Task('NX8__mem1', length=1, delay_cost=1)
	S += NX8__mem1 >= 107
	NX8__mem1 += MM_MEM[1]

	NY8_ = S.Task('NY8_', length=2, delay_cost=1)
	S += NY8_ >= 107
	NY8_ += MAS[0]

	NX8_ = S.Task('NX8_', length=2, delay_cost=1)
	S += NX8_ >= 108
	NX8_ += MAS[0]

	NY8_in = S.Task('NY8_in', length=1, delay_cost=1)
	S += NY8_in >= 108
	NY8_in += MM_in[1]

	NY8_mem0 = S.Task('NY8_mem0', length=1, delay_cost=1)
	S += NY8_mem0 >= 108
	NY8_mem0 += MAS_MEM[0]

	NY8_mem1 = S.Task('NY8_mem1', length=1, delay_cost=1)
	S += NY8_mem1 >= 108
	NY8_mem1 += MAIN_MEM_r[1]

	NX8_in = S.Task('NX8_in', length=1, delay_cost=1)
	S += NX8_in >= 109
	NX8_in += MM_in[0]

	NX8_mem0 = S.Task('NX8_mem0', length=1, delay_cost=1)
	S += NX8_mem0 >= 109
	NX8_mem0 += MAS_MEM[0]

	NX8_mem1 = S.Task('NX8_mem1', length=1, delay_cost=1)
	S += NX8_mem1 >= 109
	NX8_mem1 += MAIN_MEM_r[1]

	NY8 = S.Task('NY8', length=11, delay_cost=1)
	S += NY8 >= 109
	NY8 += MM[1]

	NX8 = S.Task('NX8', length=11, delay_cost=1)
	S += NX8 >= 110
	NX8 += MM[0]

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	S += Z_exp12_in >= 110
	Z_exp12_in += MM_in[1]

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	S += Z_exp12_mem0 >= 110
	Z_exp12_mem0 += MM_MEM[0]

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	S += Z_exp12_mem1 >= 110
	Z_exp12_mem1 += MAIN_MEM_r[1]

	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	S += k2_4_Z11_in >= 110
	k2_4_Z11_in += MM_in[0]

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	S += k2_4_Z11_mem0 >= 110
	k2_4_Z11_mem0 += MAIN_MEM_r[0]

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	S += k2_4_Z11_mem1 >= 110
	k2_4_Z11_mem1 += MM_MEM[1]

	Z_exp12 = S.Task('Z_exp12', length=11, delay_cost=1)
	S += Z_exp12 >= 111
	Z_exp12 += MM[1]

	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	S += k0_0_Z11_in >= 111
	k0_0_Z11_in += MM_in[1]

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	S += k0_0_Z11_mem0 >= 111
	k0_0_Z11_mem0 += MAIN_MEM_r[0]

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	S += k0_0_Z11_mem1 >= 111
	k0_0_Z11_mem1 += MM_MEM[1]

	k2_4_Z11 = S.Task('k2_4_Z11', length=11, delay_cost=1)
	S += k2_4_Z11 >= 111
	k2_4_Z11 += MM[0]

	k0_0_Z11 = S.Task('k0_0_Z11', length=11, delay_cost=1)
	S += k0_0_Z11 >= 112
	k0_0_Z11 += MM[1]

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	S += k3_5_Z11_in >= 112
	k3_5_Z11_in += MM_in[0]

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	S += k3_5_Z11_mem0 >= 112
	k3_5_Z11_mem0 += MAIN_MEM_r[0]

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	S += k3_5_Z11_mem1 >= 112
	k3_5_Z11_mem1 += MM_MEM[1]

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	S += k1_0_Z11_in >= 113
	k1_0_Z11_in += MM_in[0]

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	S += k1_0_Z11_mem0 >= 113
	k1_0_Z11_mem0 += MAIN_MEM_r[0]

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	S += k1_0_Z11_mem1 >= 113
	k1_0_Z11_mem1 += MM_MEM[1]

	k3_5_Z11 = S.Task('k3_5_Z11', length=11, delay_cost=1)
	S += k3_5_Z11 >= 113
	k3_5_Z11 += MM[0]

	k1_0_Z11 = S.Task('k1_0_Z11', length=11, delay_cost=1)
	S += k1_0_Z11 >= 114
	k1_0_Z11 += MM[0]

	DY8__in = S.Task('DY8__in', length=1, delay_cost=1)
	S += DY8__in >= 115
	DY8__in += MAS_in[1]

	DY8__mem0 = S.Task('DY8__mem0', length=1, delay_cost=1)
	S += DY8__mem0 >= 115
	DY8__mem0 += MM_MEM[0]

	DY8__mem1 = S.Task('DY8__mem1', length=1, delay_cost=1)
	S += DY8__mem1 >= 115
	DY8__mem1 += MM_MEM[3]

	DX8__in = S.Task('DX8__in', length=1, delay_cost=1)
	S += DX8__in >= 116
	DX8__in += MAS_in[0]

	DX8__mem0 = S.Task('DX8__mem0', length=1, delay_cost=1)
	S += DX8__mem0 >= 116
	DX8__mem0 += MM_MEM[0]

	DX8__mem1 = S.Task('DX8__mem1', length=1, delay_cost=1)
	S += DX8__mem1 >= 116
	DX8__mem1 += MM_MEM[3]

	DY8_ = S.Task('DY8_', length=2, delay_cost=1)
	S += DY8_ >= 116
	DY8_ += MAS[1]

	DX8_ = S.Task('DX8_', length=2, delay_cost=1)
	S += DX8_ >= 117
	DX8_ += MAS[0]

	DY8_in = S.Task('DY8_in', length=1, delay_cost=1)
	S += DY8_in >= 117
	DY8_in += MM_in[0]

	DY8_mem0 = S.Task('DY8_mem0', length=1, delay_cost=1)
	S += DY8_mem0 >= 117
	DY8_mem0 += MAS_MEM[2]

	DY8_mem1 = S.Task('DY8_mem1', length=1, delay_cost=1)
	S += DY8_mem1 >= 117
	DY8_mem1 += MAIN_MEM_r[1]

	DX8_in = S.Task('DX8_in', length=1, delay_cost=1)
	S += DX8_in >= 118
	DX8_in += MM_in[0]

	DX8_mem0 = S.Task('DX8_mem0', length=1, delay_cost=1)
	S += DX8_mem0 >= 118
	DX8_mem0 += MAS_MEM[0]

	DX8_mem1 = S.Task('DX8_mem1', length=1, delay_cost=1)
	S += DX8_mem1 >= 118
	DX8_mem1 += MAIN_MEM_r[1]

	DY8 = S.Task('DY8', length=11, delay_cost=1)
	S += DY8 >= 118
	DY8 += MM[0]

	DX8 = S.Task('DX8', length=11, delay_cost=1)
	S += DX8 >= 119
	DX8 += MM[0]

	NY9__in = S.Task('NY9__in', length=1, delay_cost=1)
	S += NY9__in >= 119
	NY9__in += MAS_in[0]

	NY9__mem0 = S.Task('NY9__mem0', length=1, delay_cost=1)
	S += NY9__mem0 >= 119
	NY9__mem0 += MM_MEM[2]

	NY9__mem1 = S.Task('NY9__mem1', length=1, delay_cost=1)
	S += NY9__mem1 >= 119
	NY9__mem1 += MM_MEM[1]

	NX9__in = S.Task('NX9__in', length=1, delay_cost=1)
	S += NX9__in >= 120
	NX9__in += MAS_in[1]

	NX9__mem0 = S.Task('NX9__mem0', length=1, delay_cost=1)
	S += NX9__mem0 >= 120
	NX9__mem0 += MM_MEM[0]

	NX9__mem1 = S.Task('NX9__mem1', length=1, delay_cost=1)
	S += NX9__mem1 >= 120
	NX9__mem1 += MM_MEM[1]

	NY9_ = S.Task('NY9_', length=2, delay_cost=1)
	S += NY9_ >= 120
	NY9_ += MAS[0]

	NX9_ = S.Task('NX9_', length=2, delay_cost=1)
	S += NX9_ >= 121
	NX9_ += MAS[1]

	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	S += Z_exp13_in >= 121
	Z_exp13_in += MM_in[1]

	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	S += Z_exp13_mem0 >= 121
	Z_exp13_mem0 += MM_MEM[2]

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	S += Z_exp13_mem1 >= 121
	Z_exp13_mem1 += MAIN_MEM_r[1]

	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	S += k3_4_Z12_in >= 121
	k3_4_Z12_in += MM_in[0]

	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	S += k3_4_Z12_mem0 >= 121
	k3_4_Z12_mem0 += MAIN_MEM_r[0]

	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	S += k3_4_Z12_mem1 >= 121
	k3_4_Z12_mem1 += MM_MEM[3]

	NX9_in = S.Task('NX9_in', length=1, delay_cost=1)
	S += NX9_in >= 122
	NX9_in += MM_in[0]

	NX9_mem0 = S.Task('NX9_mem0', length=1, delay_cost=1)
	S += NX9_mem0 >= 122
	NX9_mem0 += MAS_MEM[2]

	NX9_mem1 = S.Task('NX9_mem1', length=1, delay_cost=1)
	S += NX9_mem1 >= 122
	NX9_mem1 += MAIN_MEM_r[1]

	Z_exp13 = S.Task('Z_exp13', length=11, delay_cost=1)
	S += Z_exp13 >= 122
	Z_exp13 += MM[1]

	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	S += k2_3_Z12_in >= 122
	k2_3_Z12_in += MM_in[1]

	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	S += k2_3_Z12_mem0 >= 122
	k2_3_Z12_mem0 += MAIN_MEM_r[0]

	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	S += k2_3_Z12_mem1 >= 122
	k2_3_Z12_mem1 += MM_MEM[3]

	k3_4_Z12 = S.Task('k3_4_Z12', length=11, delay_cost=1)
	S += k3_4_Z12 >= 122
	k3_4_Z12 += MM[0]

	NX9 = S.Task('NX9', length=11, delay_cost=1)
	S += NX9 >= 123
	NX9 += MM[0]

	NY9_in = S.Task('NY9_in', length=1, delay_cost=1)
	S += NY9_in >= 123
	NY9_in += MM_in[1]

	NY9_mem0 = S.Task('NY9_mem0', length=1, delay_cost=1)
	S += NY9_mem0 >= 123
	NY9_mem0 += MAS_MEM[0]

	NY9_mem1 = S.Task('NY9_mem1', length=1, delay_cost=1)
	S += NY9_mem1 >= 123
	NY9_mem1 += MAIN_MEM_r[1]

	k2_3_Z12 = S.Task('k2_3_Z12', length=11, delay_cost=1)
	S += k2_3_Z12 >= 123
	k2_3_Z12 += MM[1]

	NY9 = S.Task('NY9', length=11, delay_cost=1)
	S += NY9 >= 124
	NY9 += MM[1]

	DY9__in = S.Task('DY9__in', length=1, delay_cost=1)
	S += DY9__in >= 128
	DY9__in += MAS_in[0]

	DY9__mem0 = S.Task('DY9__mem0', length=1, delay_cost=1)
	S += DY9__mem0 >= 128
	DY9__mem0 += MM_MEM[0]

	DY9__mem1 = S.Task('DY9__mem1', length=1, delay_cost=1)
	S += DY9__mem1 >= 128
	DY9__mem1 += MM_MEM[3]

	DX9__in = S.Task('DX9__in', length=1, delay_cost=1)
	S += DX9__in >= 129
	DX9__in += MAS_in[1]

	DX9__mem0 = S.Task('DX9__mem0', length=1, delay_cost=1)
	S += DX9__mem0 >= 129
	DX9__mem0 += MM_MEM[0]

	DX9__mem1 = S.Task('DX9__mem1', length=1, delay_cost=1)
	S += DX9__mem1 >= 129
	DX9__mem1 += MM_MEM[1]

	DY9_ = S.Task('DY9_', length=2, delay_cost=1)
	S += DY9_ >= 129
	DY9_ += MAS[0]

	DX9_ = S.Task('DX9_', length=2, delay_cost=1)
	S += DX9_ >= 130
	DX9_ += MAS[1]

	DY9_in = S.Task('DY9_in', length=1, delay_cost=1)
	S += DY9_in >= 130
	DY9_in += MM_in[0]

	DY9_mem0 = S.Task('DY9_mem0', length=1, delay_cost=1)
	S += DY9_mem0 >= 130
	DY9_mem0 += MAS_MEM[0]

	DY9_mem1 = S.Task('DY9_mem1', length=1, delay_cost=1)
	S += DY9_mem1 >= 130
	DY9_mem1 += MAIN_MEM_r[1]

	DX9_in = S.Task('DX9_in', length=1, delay_cost=1)
	S += DX9_in >= 131
	DX9_in += MM_in[0]

	DX9_mem0 = S.Task('DX9_mem0', length=1, delay_cost=1)
	S += DX9_mem0 >= 131
	DX9_mem0 += MAS_MEM[2]

	DX9_mem1 = S.Task('DX9_mem1', length=1, delay_cost=1)
	S += DX9_mem1 >= 131
	DX9_mem1 += MAIN_MEM_r[1]

	DY9 = S.Task('DY9', length=11, delay_cost=1)
	S += DY9 >= 131
	DY9 += MM[0]

	DX9 = S.Task('DX9', length=11, delay_cost=1)
	S += DX9 >= 132
	DX9 += MM[0]

	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	S += Z_exp14_in >= 132
	Z_exp14_in += MM_in[1]

	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	S += Z_exp14_mem0 >= 132
	Z_exp14_mem0 += MM_MEM[2]

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	S += Z_exp14_mem1 >= 132
	Z_exp14_mem1 += MAIN_MEM_r[1]

	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	S += k2_2_Z13_in >= 132
	k2_2_Z13_in += MM_in[0]

	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	S += k2_2_Z13_mem0 >= 132
	k2_2_Z13_mem0 += MAIN_MEM_r[0]

	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	S += k2_2_Z13_mem1 >= 132
	k2_2_Z13_mem1 += MM_MEM[3]

	NX10__in = S.Task('NX10__in', length=1, delay_cost=1)
	S += NX10__in >= 133
	NX10__in += MAS_in[0]

	NX10__mem0 = S.Task('NX10__mem0', length=1, delay_cost=1)
	S += NX10__mem0 >= 133
	NX10__mem0 += MM_MEM[0]

	NX10__mem1 = S.Task('NX10__mem1', length=1, delay_cost=1)
	S += NX10__mem1 >= 133
	NX10__mem1 += MM_MEM[1]

	Z_exp14 = S.Task('Z_exp14', length=11, delay_cost=1)
	S += Z_exp14 >= 133
	Z_exp14 += MM[1]

	k2_2_Z13 = S.Task('k2_2_Z13', length=11, delay_cost=1)
	S += k2_2_Z13 >= 133
	k2_2_Z13 += MM[0]

	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	S += k3_3_Z13_in >= 133
	k3_3_Z13_in += MM_in[0]

	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	S += k3_3_Z13_mem0 >= 133
	k3_3_Z13_mem0 += MAIN_MEM_r[0]

	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	S += k3_3_Z13_mem1 >= 133
	k3_3_Z13_mem1 += MM_MEM[3]

	NX10_ = S.Task('NX10_', length=2, delay_cost=1)
	S += NX10_ >= 134
	NX10_ += MAS[0]

	NY10__in = S.Task('NY10__in', length=1, delay_cost=1)
	S += NY10__in >= 134
	NY10__in += MAS_in[0]

	NY10__mem0 = S.Task('NY10__mem0', length=1, delay_cost=1)
	S += NY10__mem0 >= 134
	NY10__mem0 += MM_MEM[2]

	NY10__mem1 = S.Task('NY10__mem1', length=1, delay_cost=1)
	S += NY10__mem1 >= 134
	NY10__mem1 += MM_MEM[3]

	k3_3_Z13 = S.Task('k3_3_Z13', length=11, delay_cost=1)
	S += k3_3_Z13 >= 134
	k3_3_Z13 += MM[0]

	NX10_in = S.Task('NX10_in', length=1, delay_cost=1)
	S += NX10_in >= 135
	NX10_in += MM_in[0]

	NX10_mem0 = S.Task('NX10_mem0', length=1, delay_cost=1)
	S += NX10_mem0 >= 135
	NX10_mem0 += MAS_MEM[0]

	NX10_mem1 = S.Task('NX10_mem1', length=1, delay_cost=1)
	S += NX10_mem1 >= 135
	NX10_mem1 += MAIN_MEM_r[1]

	NY10_ = S.Task('NY10_', length=2, delay_cost=1)
	S += NY10_ >= 135
	NY10_ += MAS[0]

	NX10 = S.Task('NX10', length=11, delay_cost=1)
	S += NX10 >= 136
	NX10 += MM[0]

	NY10_in = S.Task('NY10_in', length=1, delay_cost=1)
	S += NY10_in >= 136
	NY10_in += MM_in[0]

	NY10_mem0 = S.Task('NY10_mem0', length=1, delay_cost=1)
	S += NY10_mem0 >= 136
	NY10_mem0 += MAS_MEM[0]

	NY10_mem1 = S.Task('NY10_mem1', length=1, delay_cost=1)
	S += NY10_mem1 >= 136
	NY10_mem1 += MAIN_MEM_r[1]

	NY10 = S.Task('NY10', length=11, delay_cost=1)
	S += NY10 >= 137
	NY10 += MM[0]

	DY10__in = S.Task('DY10__in', length=1, delay_cost=1)
	S += DY10__in >= 141
	DY10__in += MAS_in[0]

	DY10__mem0 = S.Task('DY10__mem0', length=1, delay_cost=1)
	S += DY10__mem0 >= 141
	DY10__mem0 += MM_MEM[0]

	DY10__mem1 = S.Task('DY10__mem1', length=1, delay_cost=1)
	S += DY10__mem1 >= 141
	DY10__mem1 += MM_MEM[1]

	DX_in = S.Task('DX_in', length=1, delay_cost=1)
	S += DX_in >= 142
	DX_in += MAS_in[0]

	DX_mem0 = S.Task('DX_mem0', length=1, delay_cost=1)
	S += DX_mem0 >= 142
	DX_mem0 += MM_MEM[0]

	DX_mem1 = S.Task('DX_mem1', length=1, delay_cost=1)
	S += DX_mem1 >= 142
	DX_mem1 += MM_MEM[1]

	DY10_ = S.Task('DY10_', length=2, delay_cost=1)
	S += DY10_ >= 142
	DY10_ += MAS[0]

	DX = S.Task('DX', length=2, delay_cost=1)
	S += DX >= 143
	DX += MAS[0]

	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	S += Z_exp15_in >= 143
	Z_exp15_in += MM_in[0]

	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	S += Z_exp15_mem0 >= 143
	Z_exp15_mem0 += MM_MEM[2]

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	S += Z_exp15_mem1 >= 143
	Z_exp15_mem1 += MAIN_MEM_r[1]

	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	S += k2_1_Z14_in >= 143
	k2_1_Z14_in += MM_in[1]

	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	S += k2_1_Z14_mem0 >= 143
	k2_1_Z14_mem0 += MAIN_MEM_r[0]

	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	S += k2_1_Z14_mem1 >= 143
	k2_1_Z14_mem1 += MM_MEM[3]

	DY10_in = S.Task('DY10_in', length=1, delay_cost=1)
	S += DY10_in >= 144
	DY10_in += MM_in[1]

	DY10_mem0 = S.Task('DY10_mem0', length=1, delay_cost=1)
	S += DY10_mem0 >= 144
	DY10_mem0 += MAS_MEM[0]

	DY10_mem1 = S.Task('DY10_mem1', length=1, delay_cost=1)
	S += DY10_mem1 >= 144
	DY10_mem1 += MAIN_MEM_r[1]

	Z_exp15 = S.Task('Z_exp15', length=11, delay_cost=1)
	S += Z_exp15 >= 144
	Z_exp15 += MM[0]

	k2_1_Z14 = S.Task('k2_1_Z14', length=11, delay_cost=1)
	S += k2_1_Z14 >= 144
	k2_1_Z14 += MM[1]

	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	S += k3_2_Z14_in >= 144
	k3_2_Z14_in += MM_in[0]

	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	S += k3_2_Z14_mem0 >= 144
	k3_2_Z14_mem0 += MAIN_MEM_r[0]

	k3_2_Z14_mem1 = S.Task('k3_2_Z14_mem1', length=1, delay_cost=1)
	S += k3_2_Z14_mem1 >= 144
	k3_2_Z14_mem1 += MM_MEM[3]

	DY10 = S.Task('DY10', length=11, delay_cost=1)
	S += DY10 >= 145
	DY10 += MM[1]

	k3_2_Z14 = S.Task('k3_2_Z14', length=11, delay_cost=1)
	S += k3_2_Z14 >= 145
	k3_2_Z14 += MM[0]

	NX_in = S.Task('NX_in', length=1, delay_cost=1)
	S += NX_in >= 146
	NX_in += MAS_in[0]

	NX_mem0 = S.Task('NX_mem0', length=1, delay_cost=1)
	S += NX_mem0 >= 146
	NX_mem0 += MM_MEM[0]

	NX_mem1 = S.Task('NX_mem1', length=1, delay_cost=1)
	S += NX_mem1 >= 146
	NX_mem1 += MM_MEM[3]

	NX = S.Task('NX', length=2, delay_cost=1)
	S += NX >= 147
	NX += MAS[0]

	NY11__in = S.Task('NY11__in', length=1, delay_cost=1)
	S += NY11__in >= 147
	NY11__in += MAS_in[0]

	NY11__mem0 = S.Task('NY11__mem0', length=1, delay_cost=1)
	S += NY11__mem0 >= 147
	NY11__mem0 += MM_MEM[0]

	NY11__mem1 = S.Task('NY11__mem1', length=1, delay_cost=1)
	S += NY11__mem1 >= 147
	NY11__mem1 += MM_MEM[1]

	NY11_ = S.Task('NY11_', length=2, delay_cost=1)
	S += NY11_ >= 148
	NY11_ += MAS[0]

	NY11_in = S.Task('NY11_in', length=1, delay_cost=1)
	S += NY11_in >= 149
	NY11_in += MM_in[1]

	NY11_mem0 = S.Task('NY11_mem0', length=1, delay_cost=1)
	S += NY11_mem0 >= 149
	NY11_mem0 += MAS_MEM[0]

	NY11_mem1 = S.Task('NY11_mem1', length=1, delay_cost=1)
	S += NY11_mem1 >= 149
	NY11_mem1 += MAIN_MEM_r[1]

	NY11 = S.Task('NY11', length=11, delay_cost=1)
	S += NY11 >= 150
	NY11 += MM[1]

	Z_exp16_in = S.Task('Z_exp16_in', length=1, delay_cost=1)
	S += Z_exp16_in >= 154
	Z_exp16_in += MM_in[0]

	Z_exp16_mem0 = S.Task('Z_exp16_mem0', length=1, delay_cost=1)
	S += Z_exp16_mem0 >= 154
	Z_exp16_mem0 += MM_MEM[0]

	Z_exp16_mem1 = S.Task('Z_exp16_mem1', length=1, delay_cost=1)
	S += Z_exp16_mem1 >= 154
	Z_exp16_mem1 += MAIN_MEM_r[1]

	k3_1_Z15_in = S.Task('k3_1_Z15_in', length=1, delay_cost=1)
	S += k3_1_Z15_in >= 154
	k3_1_Z15_in += MM_in[1]

	k3_1_Z15_mem0 = S.Task('k3_1_Z15_mem0', length=1, delay_cost=1)
	S += k3_1_Z15_mem0 >= 154
	k3_1_Z15_mem0 += MAIN_MEM_r[0]

	k3_1_Z15_mem1 = S.Task('k3_1_Z15_mem1', length=1, delay_cost=1)
	S += k3_1_Z15_mem1 >= 154
	k3_1_Z15_mem1 += MM_MEM[1]

	DY11__in = S.Task('DY11__in', length=1, delay_cost=1)
	S += DY11__in >= 155
	DY11__in += MAS_in[2]

	DY11__mem0 = S.Task('DY11__mem0', length=1, delay_cost=1)
	S += DY11__mem0 >= 155
	DY11__mem0 += MM_MEM[2]

	DY11__mem1 = S.Task('DY11__mem1', length=1, delay_cost=1)
	S += DY11__mem1 >= 155
	DY11__mem1 += MM_MEM[1]

	Z_exp16 = S.Task('Z_exp16', length=11, delay_cost=1)
	S += Z_exp16 >= 155
	Z_exp16 += MM[0]

	k3_1_Z15 = S.Task('k3_1_Z15', length=11, delay_cost=1)
	S += k3_1_Z15 >= 155
	k3_1_Z15 += MM[1]

	DY11_ = S.Task('DY11_', length=2, delay_cost=1)
	S += DY11_ >= 156
	DY11_ += MAS[2]

	k2_0_Z15_in = S.Task('k2_0_Z15_in', length=1, delay_cost=1)
	S += k2_0_Z15_in >= 156
	k2_0_Z15_in += MM_in[0]

	k2_0_Z15_mem0 = S.Task('k2_0_Z15_mem0', length=1, delay_cost=1)
	S += k2_0_Z15_mem0 >= 156
	k2_0_Z15_mem0 += MAIN_MEM_r[0]

	k2_0_Z15_mem1 = S.Task('k2_0_Z15_mem1', length=1, delay_cost=1)
	S += k2_0_Z15_mem1 >= 156
	k2_0_Z15_mem1 += MM_MEM[1]

	DY11_in = S.Task('DY11_in', length=1, delay_cost=1)
	S += DY11_in >= 157
	DY11_in += MM_in[1]

	DY11_mem0 = S.Task('DY11_mem0', length=1, delay_cost=1)
	S += DY11_mem0 >= 157
	DY11_mem0 += MAS_MEM[4]

	DY11_mem1 = S.Task('DY11_mem1', length=1, delay_cost=1)
	S += DY11_mem1 >= 157
	DY11_mem1 += MAIN_MEM_r[1]

	k2_0_Z15 = S.Task('k2_0_Z15', length=11, delay_cost=1)
	S += k2_0_Z15 >= 157
	k2_0_Z15 += MM[0]

	DY11 = S.Task('DY11', length=11, delay_cost=1)
	S += DY11 >= 158
	DY11 += MM[1]

	NY12__in = S.Task('NY12__in', length=1, delay_cost=1)
	S += NY12__in >= 160
	NY12__in += MAS_in[1]

	NY12__mem0 = S.Task('NY12__mem0', length=1, delay_cost=1)
	S += NY12__mem0 >= 160
	NY12__mem0 += MM_MEM[2]

	NY12__mem1 = S.Task('NY12__mem1', length=1, delay_cost=1)
	S += NY12__mem1 >= 160
	NY12__mem1 += MM_MEM[3]

	NY12_ = S.Task('NY12_', length=2, delay_cost=1)
	S += NY12_ >= 161
	NY12_ += MAS[1]

	NY12_in = S.Task('NY12_in', length=1, delay_cost=1)
	S += NY12_in >= 162
	NY12_in += MM_in[0]

	NY12_mem0 = S.Task('NY12_mem0', length=1, delay_cost=1)
	S += NY12_mem0 >= 162
	NY12_mem0 += MAS_MEM[2]

	NY12_mem1 = S.Task('NY12_mem1', length=1, delay_cost=1)
	S += NY12_mem1 >= 162
	NY12_mem1 += MAIN_MEM_r[1]

	NY12 = S.Task('NY12', length=11, delay_cost=1)
	S += NY12 >= 163
	NY12 += MM[0]

	k3_0_Z16_in = S.Task('k3_0_Z16_in', length=1, delay_cost=1)
	S += k3_0_Z16_in >= 165
	k3_0_Z16_in += MM_in[0]

	k3_0_Z16_mem0 = S.Task('k3_0_Z16_mem0', length=1, delay_cost=1)
	S += k3_0_Z16_mem0 >= 165
	k3_0_Z16_mem0 += MAIN_MEM_r[0]

	k3_0_Z16_mem1 = S.Task('k3_0_Z16_mem1', length=1, delay_cost=1)
	S += k3_0_Z16_mem1 >= 165
	k3_0_Z16_mem1 += MM_MEM[1]

	k3_0_Z16 = S.Task('k3_0_Z16', length=11, delay_cost=1)
	S += k3_0_Z16 >= 166
	k3_0_Z16 += MM[0]

	DY12__in = S.Task('DY12__in', length=1, delay_cost=1)
	S += DY12__in >= 168
	DY12__in += MAS_in[0]

	DY12__mem0 = S.Task('DY12__mem0', length=1, delay_cost=1)
	S += DY12__mem0 >= 168
	DY12__mem0 += MM_MEM[2]

	DY12__mem1 = S.Task('DY12__mem1', length=1, delay_cost=1)
	S += DY12__mem1 >= 168
	DY12__mem1 += MM_MEM[1]

	DY12_ = S.Task('DY12_', length=2, delay_cost=1)
	S += DY12_ >= 169
	DY12_ += MAS[0]

	DY12_in = S.Task('DY12_in', length=1, delay_cost=1)
	S += DY12_in >= 170
	DY12_in += MM_in[1]

	DY12_mem0 = S.Task('DY12_mem0', length=1, delay_cost=1)
	S += DY12_mem0 >= 170
	DY12_mem0 += MAS_MEM[0]

	DY12_mem1 = S.Task('DY12_mem1', length=1, delay_cost=1)
	S += DY12_mem1 >= 170
	DY12_mem1 += MAIN_MEM_r[1]

	DY12 = S.Task('DY12', length=11, delay_cost=1)
	S += DY12 >= 171
	DY12 += MM[1]

	NY13__in = S.Task('NY13__in', length=1, delay_cost=1)
	S += NY13__in >= 173
	NY13__in += MAS_in[0]

	NY13__mem0 = S.Task('NY13__mem0', length=1, delay_cost=1)
	S += NY13__mem0 >= 173
	NY13__mem0 += MM_MEM[0]

	NY13__mem1 = S.Task('NY13__mem1', length=1, delay_cost=1)
	S += NY13__mem1 >= 173
	NY13__mem1 += MM_MEM[1]

	NY13_ = S.Task('NY13_', length=2, delay_cost=1)
	S += NY13_ >= 174
	NY13_ += MAS[0]

	NY13_in = S.Task('NY13_in', length=1, delay_cost=1)
	S += NY13_in >= 175
	NY13_in += MM_in[1]

	NY13_mem0 = S.Task('NY13_mem0', length=1, delay_cost=1)
	S += NY13_mem0 >= 175
	NY13_mem0 += MAS_MEM[0]

	NY13_mem1 = S.Task('NY13_mem1', length=1, delay_cost=1)
	S += NY13_mem1 >= 175
	NY13_mem1 += MAIN_MEM_r[1]

	NY13 = S.Task('NY13', length=11, delay_cost=1)
	S += NY13 >= 176
	NY13 += MM[1]

	DY13__in = S.Task('DY13__in', length=1, delay_cost=1)
	S += DY13__in >= 181
	DY13__in += MAS_in[0]

	DY13__mem0 = S.Task('DY13__mem0', length=1, delay_cost=1)
	S += DY13__mem0 >= 181
	DY13__mem0 += MM_MEM[2]

	DY13__mem1 = S.Task('DY13__mem1', length=1, delay_cost=1)
	S += DY13__mem1 >= 181
	DY13__mem1 += MM_MEM[1]

	DY13_ = S.Task('DY13_', length=2, delay_cost=1)
	S += DY13_ >= 182
	DY13_ += MAS[0]

	DY13_in = S.Task('DY13_in', length=1, delay_cost=1)
	S += DY13_in >= 183
	DY13_in += MM_in[1]

	DY13_mem0 = S.Task('DY13_mem0', length=1, delay_cost=1)
	S += DY13_mem0 >= 183
	DY13_mem0 += MAS_MEM[0]

	DY13_mem1 = S.Task('DY13_mem1', length=1, delay_cost=1)
	S += DY13_mem1 >= 183
	DY13_mem1 += MAIN_MEM_r[1]

	DY13 = S.Task('DY13', length=11, delay_cost=1)
	S += DY13 >= 184
	DY13 += MM[1]

	NY14__in = S.Task('NY14__in', length=1, delay_cost=1)
	S += NY14__in >= 186
	NY14__in += MAS_in[0]

	NY14__mem0 = S.Task('NY14__mem0', length=1, delay_cost=1)
	S += NY14__mem0 >= 186
	NY14__mem0 += MM_MEM[2]

	NY14__mem1 = S.Task('NY14__mem1', length=1, delay_cost=1)
	S += NY14__mem1 >= 186
	NY14__mem1 += MM_MEM[3]

	NY14_ = S.Task('NY14_', length=2, delay_cost=1)
	S += NY14_ >= 187
	NY14_ += MAS[0]

	NY14_in = S.Task('NY14_in', length=1, delay_cost=1)
	S += NY14_in >= 188
	NY14_in += MM_in[0]

	NY14_mem0 = S.Task('NY14_mem0', length=1, delay_cost=1)
	S += NY14_mem0 >= 188
	NY14_mem0 += MAS_MEM[0]

	NY14_mem1 = S.Task('NY14_mem1', length=1, delay_cost=1)
	S += NY14_mem1 >= 188
	NY14_mem1 += MAIN_MEM_r[1]

	NY14 = S.Task('NY14', length=11, delay_cost=1)
	S += NY14 >= 189
	NY14 += MM[0]

	DY14__in = S.Task('DY14__in', length=1, delay_cost=1)
	S += DY14__in >= 194
	DY14__in += MAS_in[3]

	DY14__mem0 = S.Task('DY14__mem0', length=1, delay_cost=1)
	S += DY14__mem0 >= 194
	DY14__mem0 += MM_MEM[2]

	DY14__mem1 = S.Task('DY14__mem1', length=1, delay_cost=1)
	S += DY14__mem1 >= 194
	DY14__mem1 += MM_MEM[3]

	DY14_ = S.Task('DY14_', length=2, delay_cost=1)
	S += DY14_ >= 195
	DY14_ += MAS[3]


	# new tasks
	NY15_ = S.Task('NY15_', length=2, delay_cost=1)
	NY15_ += alt(MAS)
	NY15__in = S.Task('NY15__in', length=1, delay_cost=1)
	NY15__in += alt(MAS_in)
	S += NY15__in*MAS_in[0]<=NY15_*MAS[0]

	S += NY15__in*MAS_in[1]<=NY15_*MAS[1]

	S += NY15__in*MAS_in[2]<=NY15_*MAS[2]

	S += NY15__in*MAS_in[3]<=NY15_*MAS[3]

	NY15__mem0 = S.Task('NY15__mem0', length=1, delay_cost=1)
	NY15__mem0 += MM_MEM[0]
	S += 199 < NY15__mem0
	S += NY15__mem0 <= NY15_

	NY15__mem1 = S.Task('NY15__mem1', length=1, delay_cost=1)
	NY15__mem1 += MM_MEM[1]
	S += 167 < NY15__mem1
	S += NY15__mem1 <= NY15_

	DY14 = S.Task('DY14', length=11, delay_cost=1)
	DY14 += alt(MM)
	DY14_in = S.Task('DY14_in', length=1, delay_cost=1)
	DY14_in += alt(MM_in)
	S += DY14_in*MM_in[0]<=DY14*MM[0]
	S += DY14_in*MM_in[1]<=DY14*MM[1]
	DY14_mem0 = S.Task('DY14_mem0', length=1, delay_cost=1)
	DY14_mem0 += MAS_MEM[6]
	S += 196 < DY14_mem0
	S += DY14_mem0 <= DY14

	DY14_mem1 = S.Task('DY14_mem1', length=1, delay_cost=1)
	DY14_mem1 += MAIN_MEM_r[1]
	S += DY14_mem1 <= DY14

	NY = S.Task('NY', length=11, delay_cost=1)
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

	DY_mem0 = S.Task('DY_mem0', length=1, delay_cost=1)
	DY_mem0 += alt(MM_MEM)
	S += (DY14*MM[0])-1 < DY_mem0*MM_MEM[0]
	S += (DY14*MM[1])-1 < DY_mem0*MM_MEM[2]
	S += DY_mem0 <= DY

	DY_mem1 = S.Task('DY_mem1', length=1, delay_cost=1)
	DY_mem1 += MM_MEM[1]
	S += 176 < DY_mem1
	S += DY_mem1 <= DY

	Z_new = S.Task('Z_new', length=11, delay_cost=1)
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
	Z_new_mem0 += MAS_MEM[0]
	S += 144 < Z_new_mem0
	S += Z_new_mem0 <= Z_new

	Z_new_mem1 = S.Task('Z_new_mem1', length=1, delay_cost=1)
	Z_new_mem1 += alt(MAS_MEM)
	S += (DY*MAS[0])-1 < Z_new_mem1*MAS_MEM[1]
	S += (DY*MAS[1])-1 < Z_new_mem1*MAS_MEM[3]
	S += (DY*MAS[2])-1 < Z_new_mem1*MAS_MEM[5]
	S += (DY*MAS[3])-1 < Z_new_mem1*MAS_MEM[7]
	S += Z_new_mem1 <= Z_new

	X_new = S.Task('X_new', length=11, delay_cost=1)
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
	X_new_mem0 += MAS_MEM[0]
	S += 148 < X_new_mem0
	S += X_new_mem0 <= X_new

	X_new_mem1 = S.Task('X_new_mem1', length=1, delay_cost=1)
	X_new_mem1 += alt(MAS_MEM)
	S += (DY*MAS[0])-1 < X_new_mem1*MAS_MEM[1]
	S += (DY*MAS[1])-1 < X_new_mem1*MAS_MEM[3]
	S += (DY*MAS[2])-1 < X_new_mem1*MAS_MEM[5]
	S += (DY*MAS[3])-1 < X_new_mem1*MAS_MEM[7]
	S += X_new_mem1 <= X_new

	Y_new = S.Task('Y_new', length=11, delay_cost=1)
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
	Y_new_mem1 += MAS_MEM[1]
	S += 144 < Y_new_mem1
	S += Y_new_mem1 <= Y_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage2MAS4/ISOGENY/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

