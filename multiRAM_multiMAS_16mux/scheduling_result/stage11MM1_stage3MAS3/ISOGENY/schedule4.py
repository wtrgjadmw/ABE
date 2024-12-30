from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 344
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=11)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=3)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=3, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=6)
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

	Z_exp2 = S.Task('Z_exp2', length=11, delay_cost=1)
	S += Z_exp2 >= 1
	Z_exp2 += MM[0]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 1
	k2_14_Z1_in += MM_in[0]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 1
	k2_14_Z1_mem0 += MAIN_MEM_r[0]

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 1
	k2_14_Z1_mem1 += MAIN_MEM_r[1]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 2
	NY0_in += MM_in[0]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 2
	NY0_mem0 += MAIN_MEM_r[0]

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 2
	NY0_mem1 += MAIN_MEM_r[1]

	k2_14_Z1 = S.Task('k2_14_Z1', length=11, delay_cost=1)
	S += k2_14_Z1 >= 2
	k2_14_Z1 += MM[0]

	NY0 = S.Task('NY0', length=11, delay_cost=1)
	S += NY0 >= 3
	NY0 += MM[0]

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 3
	k0_10_Z1_in += MM_in[0]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 3
	k0_10_Z1_mem0 += MAIN_MEM_r[0]

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 3
	k0_10_Z1_mem1 += MAIN_MEM_r[1]

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 4
	NX0_in += MM_in[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 4
	NX0_mem0 += MAIN_MEM_r[0]

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 4
	NX0_mem1 += MAIN_MEM_r[1]

	k0_10_Z1 = S.Task('k0_10_Z1', length=11, delay_cost=1)
	S += k0_10_Z1 >= 4
	k0_10_Z1 += MM[0]

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 5
	DY0_in += MM_in[0]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 5
	DY0_mem0 += MAIN_MEM_r[0]

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 5
	DY0_mem1 += MAIN_MEM_r[1]

	NX0 = S.Task('NX0', length=11, delay_cost=1)
	S += NX0 >= 5
	NX0 += MM[0]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 6
	DX0_in += MM_in[0]

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
	DX0 += MM[0]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 11
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 11
	Z_exp3_mem0 += MM_MEM[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 11
	Z_exp3_mem1 += MAIN_MEM_r[1]

	Z_exp3 = S.Task('Z_exp3', length=11, delay_cost=1)
	S += Z_exp3 >= 12
	Z_exp3 += MM[0]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 12
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 12
	k1_9_Z2_mem0 += MAIN_MEM_r[0]

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 12
	k1_9_Z2_mem1 += MM_MEM[1]

	NY1__in = S.Task('NY1__in', length=1, delay_cost=1)
	S += NY1__in >= 13
	NY1__in += MAS_in[0]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 13
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 13
	NY1__mem1 += MM_MEM[1]

	k1_9_Z2 = S.Task('k1_9_Z2', length=11, delay_cost=1)
	S += k1_9_Z2 >= 13
	k1_9_Z2 += MM[0]

	NY1_ = S.Task('NY1_', length=3, delay_cost=1)
	S += NY1_ >= 14
	NY1_ += MAS[0]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 14
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 14
	k3_14_Z2_mem0 += MAIN_MEM_r[0]

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 14
	k3_14_Z2_mem1 += MM_MEM[1]

	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	S += k0_9_Z2_in >= 15
	k0_9_Z2_in += MM_in[0]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 15
	k0_9_Z2_mem0 += MAIN_MEM_r[0]

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	S += k0_9_Z2_mem1 >= 15
	k0_9_Z2_mem1 += MM_MEM[1]

	k3_14_Z2 = S.Task('k3_14_Z2', length=11, delay_cost=1)
	S += k3_14_Z2 >= 15
	k3_14_Z2 += MM[0]

	NX1__in = S.Task('NX1__in', length=1, delay_cost=1)
	S += NX1__in >= 16
	NX1__in += MAS_in[0]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 16
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 16
	NX1__mem1 += MM_MEM[1]

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 16
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 16
	NY1_mem0 += MAS_MEM[0]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 16
	NY1_mem1 += MAIN_MEM_r[1]

	k0_9_Z2 = S.Task('k0_9_Z2', length=11, delay_cost=1)
	S += k0_9_Z2 >= 16
	k0_9_Z2 += MM[0]

	NX1_ = S.Task('NX1_', length=3, delay_cost=1)
	S += NX1_ >= 17
	NX1_ += MAS[0]

	NY1 = S.Task('NY1', length=11, delay_cost=1)
	S += NY1 >= 17
	NY1 += MM[0]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 17
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 17
	k2_13_Z2_mem0 += MAIN_MEM_r[0]

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 17
	k2_13_Z2_mem1 += MM_MEM[1]

	k2_13_Z2 = S.Task('k2_13_Z2', length=11, delay_cost=1)
	S += k2_13_Z2 >= 18
	k2_13_Z2 += MM[0]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 19
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 19
	NX1_mem0 += MAS_MEM[0]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 19
	NX1_mem1 += MAIN_MEM_r[1]

	NX1 = S.Task('NX1', length=11, delay_cost=1)
	S += NX1 >= 20
	NX1 += MM[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 22
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 22
	k3_13_Z3_mem0 += MAIN_MEM_r[0]

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 22
	k3_13_Z3_mem1 += MM_MEM[1]

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

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 24
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 24
	k1_8_Z3_mem0 += MAIN_MEM_r[0]

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 24
	k1_8_Z3_mem1 += MM_MEM[1]

	k2_12_Z3 = S.Task('k2_12_Z3', length=11, delay_cost=1)
	S += k2_12_Z3 >= 24
	k2_12_Z3 += MM[0]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 25
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 25
	Z_exp4_mem0 += MM_MEM[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 25
	Z_exp4_mem1 += MAIN_MEM_r[1]

	k1_8_Z3 = S.Task('k1_8_Z3', length=11, delay_cost=1)
	S += k1_8_Z3 >= 25
	k1_8_Z3 += MM[0]

	Z_exp4 = S.Task('Z_exp4', length=11, delay_cost=1)
	S += Z_exp4 >= 26
	Z_exp4 += MM[0]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 26
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 26
	k0_8_Z3_mem0 += MAIN_MEM_r[0]

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 26
	k0_8_Z3_mem1 += MM_MEM[1]

	DY1__in = S.Task('DY1__in', length=1, delay_cost=1)
	S += DY1__in >= 27
	DY1__in += MAS_in[2]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 27
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 27
	DY1__mem1 += MM_MEM[1]

	k0_8_Z3 = S.Task('k0_8_Z3', length=11, delay_cost=1)
	S += k0_8_Z3 >= 27
	k0_8_Z3 += MM[0]

	DX1__in = S.Task('DX1__in', length=1, delay_cost=1)
	S += DX1__in >= 28
	DX1__in += MAS_in[0]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	S += DX1__mem0 >= 28
	DX1__mem0 += MM_MEM[0]

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	S += DX1__mem1 >= 28
	DX1__mem1 += MM_MEM[1]

	DY1_ = S.Task('DY1_', length=3, delay_cost=1)
	S += DY1_ >= 28
	DY1_ += MAS[2]

	DX1_ = S.Task('DX1_', length=3, delay_cost=1)
	S += DX1_ >= 29
	DX1_ += MAS[0]

	NY2__in = S.Task('NY2__in', length=1, delay_cost=1)
	S += NY2__in >= 29
	NY2__in += MAS_in[0]

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	S += NY2__mem0 >= 29
	NY2__mem0 += MM_MEM[0]

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	S += NY2__mem1 >= 29
	NY2__mem1 += MM_MEM[1]

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	S += DY1_in >= 30
	DY1_in += MM_in[0]

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	S += DY1_mem0 >= 30
	DY1_mem0 += MAS_MEM[4]

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	S += DY1_mem1 >= 30
	DY1_mem1 += MAIN_MEM_r[1]

	NX2__in = S.Task('NX2__in', length=1, delay_cost=1)
	S += NX2__in >= 30
	NX2__in += MAS_in[0]

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	S += NX2__mem0 >= 30
	NX2__mem0 += MM_MEM[0]

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	S += NX2__mem1 >= 30
	NX2__mem1 += MM_MEM[1]

	NY2_ = S.Task('NY2_', length=3, delay_cost=1)
	S += NY2_ >= 30
	NY2_ += MAS[0]

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	S += DX1_in >= 31
	DX1_in += MM_in[0]

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	S += DX1_mem0 >= 31
	DX1_mem0 += MAS_MEM[0]

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	S += DX1_mem1 >= 31
	DX1_mem1 += MAIN_MEM_r[1]

	DY1 = S.Task('DY1', length=11, delay_cost=1)
	S += DY1 >= 31
	DY1 += MM[0]

	NX2_ = S.Task('NX2_', length=3, delay_cost=1)
	S += NX2_ >= 31
	NX2_ += MAS[0]

	DX1 = S.Task('DX1', length=11, delay_cost=1)
	S += DX1 >= 32
	DX1 += MM[0]

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	S += NY2_in >= 32
	NY2_in += MM_in[0]

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	S += NY2_mem0 >= 32
	NY2_mem0 += MAS_MEM[0]

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	S += NY2_mem1 >= 32
	NY2_mem1 += MAIN_MEM_r[1]

	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	S += NX2_in >= 33
	NX2_in += MM_in[0]

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	S += NX2_mem0 >= 33
	NX2_mem0 += MAS_MEM[0]

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	S += NX2_mem1 >= 33
	NX2_mem1 += MAIN_MEM_r[1]

	NY2 = S.Task('NY2', length=11, delay_cost=1)
	S += NY2 >= 33
	NY2 += MM[0]

	NX2 = S.Task('NX2', length=11, delay_cost=1)
	S += NX2 >= 34
	NX2 += MM[0]

	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	S += Z_exp5_in >= 36
	Z_exp5_in += MM_in[0]

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	S += Z_exp5_mem0 >= 36
	Z_exp5_mem0 += MM_MEM[0]

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	S += Z_exp5_mem1 >= 36
	Z_exp5_mem1 += MAIN_MEM_r[1]

	Z_exp5 = S.Task('Z_exp5', length=11, delay_cost=1)
	S += Z_exp5 >= 37
	Z_exp5 += MM[0]

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	S += k0_7_Z4_in >= 37
	k0_7_Z4_in += MM_in[0]

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	S += k0_7_Z4_mem0 >= 37
	k0_7_Z4_mem0 += MAIN_MEM_r[0]

	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	S += k0_7_Z4_mem1 >= 37
	k0_7_Z4_mem1 += MM_MEM[1]

	k0_7_Z4 = S.Task('k0_7_Z4', length=11, delay_cost=1)
	S += k0_7_Z4 >= 38
	k0_7_Z4 += MM[0]

	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	S += k3_12_Z4_in >= 38
	k3_12_Z4_in += MM_in[0]

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	S += k3_12_Z4_mem0 >= 38
	k3_12_Z4_mem0 += MAIN_MEM_r[0]

	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	S += k3_12_Z4_mem1 >= 38
	k3_12_Z4_mem1 += MM_MEM[1]

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	S += k2_11_Z4_in >= 39
	k2_11_Z4_in += MM_in[0]

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	S += k2_11_Z4_mem0 >= 39
	k2_11_Z4_mem0 += MAIN_MEM_r[0]

	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	S += k2_11_Z4_mem1 >= 39
	k2_11_Z4_mem1 += MM_MEM[1]

	k3_12_Z4 = S.Task('k3_12_Z4', length=11, delay_cost=1)
	S += k3_12_Z4 >= 39
	k3_12_Z4 += MM[0]

	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	S += k1_7_Z4_in >= 40
	k1_7_Z4_in += MM_in[0]

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	S += k1_7_Z4_mem0 >= 40
	k1_7_Z4_mem0 += MAIN_MEM_r[0]

	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	S += k1_7_Z4_mem1 >= 40
	k1_7_Z4_mem1 += MM_MEM[1]

	k2_11_Z4 = S.Task('k2_11_Z4', length=11, delay_cost=1)
	S += k2_11_Z4 >= 40
	k2_11_Z4 += MM[0]

	DY2__in = S.Task('DY2__in', length=1, delay_cost=1)
	S += DY2__in >= 41
	DY2__in += MAS_in[0]

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	S += DY2__mem0 >= 41
	DY2__mem0 += MM_MEM[0]

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	S += DY2__mem1 >= 41
	DY2__mem1 += MM_MEM[1]

	k1_7_Z4 = S.Task('k1_7_Z4', length=11, delay_cost=1)
	S += k1_7_Z4 >= 41
	k1_7_Z4 += MM[0]

	DX2__in = S.Task('DX2__in', length=1, delay_cost=1)
	S += DX2__in >= 42
	DX2__in += MAS_in[0]

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	S += DX2__mem0 >= 42
	DX2__mem0 += MM_MEM[0]

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	S += DX2__mem1 >= 42
	DX2__mem1 += MM_MEM[1]

	DY2_ = S.Task('DY2_', length=3, delay_cost=1)
	S += DY2_ >= 42
	DY2_ += MAS[0]

	DX2_ = S.Task('DX2_', length=3, delay_cost=1)
	S += DX2_ >= 43
	DX2_ += MAS[0]

	NY3__in = S.Task('NY3__in', length=1, delay_cost=1)
	S += NY3__in >= 43
	NY3__in += MAS_in[0]

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	S += NY3__mem0 >= 43
	NY3__mem0 += MM_MEM[0]

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	S += NY3__mem1 >= 43
	NY3__mem1 += MM_MEM[1]

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	S += DY2_in >= 44
	DY2_in += MM_in[0]

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	S += DY2_mem0 >= 44
	DY2_mem0 += MAS_MEM[0]

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	S += DY2_mem1 >= 44
	DY2_mem1 += MAIN_MEM_r[1]

	NX3__in = S.Task('NX3__in', length=1, delay_cost=1)
	S += NX3__in >= 44
	NX3__in += MAS_in[2]

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	S += NX3__mem0 >= 44
	NX3__mem0 += MM_MEM[0]

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	S += NX3__mem1 >= 44
	NX3__mem1 += MM_MEM[1]

	NY3_ = S.Task('NY3_', length=3, delay_cost=1)
	S += NY3_ >= 44
	NY3_ += MAS[0]

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	S += DX2_in >= 45
	DX2_in += MM_in[0]

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	S += DX2_mem0 >= 45
	DX2_mem0 += MAS_MEM[0]

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	S += DX2_mem1 >= 45
	DX2_mem1 += MAIN_MEM_r[1]

	DY2 = S.Task('DY2', length=11, delay_cost=1)
	S += DY2 >= 45
	DY2 += MM[0]

	NX3_ = S.Task('NX3_', length=3, delay_cost=1)
	S += NX3_ >= 45
	NX3_ += MAS[2]

	DX2 = S.Task('DX2', length=11, delay_cost=1)
	S += DX2 >= 46
	DX2 += MM[0]

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	S += NY3_in >= 46
	NY3_in += MM_in[0]

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	S += NY3_mem0 >= 46
	NY3_mem0 += MAS_MEM[0]

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	S += NY3_mem1 >= 46
	NY3_mem1 += MAIN_MEM_r[1]

	NY3 = S.Task('NY3', length=11, delay_cost=1)
	S += NY3 >= 47
	NY3 += MM[0]

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	S += Z_exp6_in >= 47
	Z_exp6_in += MM_in[0]

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	S += Z_exp6_mem0 >= 47
	Z_exp6_mem0 += MM_MEM[0]

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	S += Z_exp6_mem1 >= 47
	Z_exp6_mem1 += MAIN_MEM_r[1]

	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	S += NX3_in >= 48
	NX3_in += MM_in[0]

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	S += NX3_mem0 >= 48
	NX3_mem0 += MAS_MEM[4]

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	S += NX3_mem1 >= 48
	NX3_mem1 += MAIN_MEM_r[1]

	Z_exp6 = S.Task('Z_exp6', length=11, delay_cost=1)
	S += Z_exp6 >= 48
	Z_exp6 += MM[0]

	NX3 = S.Task('NX3', length=11, delay_cost=1)
	S += NX3 >= 49
	NX3 += MM[0]

	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	S += k0_6_Z5_in >= 49
	k0_6_Z5_in += MM_in[0]

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	S += k0_6_Z5_mem0 >= 49
	k0_6_Z5_mem0 += MAIN_MEM_r[0]

	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	S += k0_6_Z5_mem1 >= 49
	k0_6_Z5_mem1 += MM_MEM[1]

	k0_6_Z5 = S.Task('k0_6_Z5', length=11, delay_cost=1)
	S += k0_6_Z5 >= 50
	k0_6_Z5 += MM[0]

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	S += k1_6_Z5_in >= 50
	k1_6_Z5_in += MM_in[0]

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	S += k1_6_Z5_mem0 >= 50
	k1_6_Z5_mem0 += MAIN_MEM_r[0]

	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	S += k1_6_Z5_mem1 >= 50
	k1_6_Z5_mem1 += MM_MEM[1]

	k1_6_Z5 = S.Task('k1_6_Z5', length=11, delay_cost=1)
	S += k1_6_Z5 >= 51
	k1_6_Z5 += MM[0]

	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	S += k2_10_Z5_in >= 51
	k2_10_Z5_in += MM_in[0]

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	S += k2_10_Z5_mem0 >= 51
	k2_10_Z5_mem0 += MAIN_MEM_r[0]

	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	S += k2_10_Z5_mem1 >= 51
	k2_10_Z5_mem1 += MM_MEM[1]

	k2_10_Z5 = S.Task('k2_10_Z5', length=11, delay_cost=1)
	S += k2_10_Z5 >= 52
	k2_10_Z5 += MM[0]

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	S += k3_11_Z5_in >= 52
	k3_11_Z5_in += MM_in[0]

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	S += k3_11_Z5_mem0 >= 52
	k3_11_Z5_mem0 += MAIN_MEM_r[0]

	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	S += k3_11_Z5_mem1 >= 52
	k3_11_Z5_mem1 += MM_MEM[1]

	k3_11_Z5 = S.Task('k3_11_Z5', length=11, delay_cost=1)
	S += k3_11_Z5 >= 53
	k3_11_Z5 += MM[0]

	DY3__in = S.Task('DY3__in', length=1, delay_cost=1)
	S += DY3__in >= 55
	DY3__in += MAS_in[0]

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	S += DY3__mem0 >= 55
	DY3__mem0 += MM_MEM[0]

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	S += DY3__mem1 >= 55
	DY3__mem1 += MM_MEM[1]

	DX3__in = S.Task('DX3__in', length=1, delay_cost=1)
	S += DX3__in >= 56
	DX3__in += MAS_in[0]

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	S += DX3__mem0 >= 56
	DX3__mem0 += MM_MEM[0]

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	S += DX3__mem1 >= 56
	DX3__mem1 += MM_MEM[1]

	DY3_ = S.Task('DY3_', length=3, delay_cost=1)
	S += DY3_ >= 56
	DY3_ += MAS[0]

	DX3_ = S.Task('DX3_', length=3, delay_cost=1)
	S += DX3_ >= 57
	DX3_ += MAS[0]

	NY4__in = S.Task('NY4__in', length=1, delay_cost=1)
	S += NY4__in >= 57
	NY4__in += MAS_in[0]

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	S += NY4__mem0 >= 57
	NY4__mem0 += MM_MEM[0]

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	S += NY4__mem1 >= 57
	NY4__mem1 += MM_MEM[1]

	NY4_ = S.Task('NY4_', length=3, delay_cost=1)
	S += NY4_ >= 58
	NY4_ += MAS[0]

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	S += Z_exp7_in >= 58
	Z_exp7_in += MM_in[0]

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	S += Z_exp7_mem0 >= 58
	Z_exp7_mem0 += MM_MEM[0]

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	S += Z_exp7_mem1 >= 58
	Z_exp7_mem1 += MAIN_MEM_r[1]

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	S += DX3_in >= 59
	DX3_in += MM_in[0]

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	S += DX3_mem0 >= 59
	DX3_mem0 += MAS_MEM[0]

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	S += DX3_mem1 >= 59
	DX3_mem1 += MAIN_MEM_r[1]

	NX4__in = S.Task('NX4__in', length=1, delay_cost=1)
	S += NX4__in >= 59
	NX4__in += MAS_in[2]

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	S += NX4__mem0 >= 59
	NX4__mem0 += MM_MEM[0]

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	S += NX4__mem1 >= 59
	NX4__mem1 += MM_MEM[1]

	Z_exp7 = S.Task('Z_exp7', length=11, delay_cost=1)
	S += Z_exp7 >= 59
	Z_exp7 += MM[0]

	DX3 = S.Task('DX3', length=11, delay_cost=1)
	S += DX3 >= 60
	DX3 += MM[0]

	NX4_ = S.Task('NX4_', length=3, delay_cost=1)
	S += NX4_ >= 60
	NX4_ += MAS[2]

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	S += k0_5_Z6_in >= 60
	k0_5_Z6_in += MM_in[0]

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	S += k0_5_Z6_mem0 >= 60
	k0_5_Z6_mem0 += MAIN_MEM_r[0]

	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	S += k0_5_Z6_mem1 >= 60
	k0_5_Z6_mem1 += MM_MEM[1]

	k0_5_Z6 = S.Task('k0_5_Z6', length=11, delay_cost=1)
	S += k0_5_Z6 >= 61
	k0_5_Z6 += MM[0]

	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	S += k1_5_Z6_in >= 61
	k1_5_Z6_in += MM_in[0]

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	S += k1_5_Z6_mem0 >= 61
	k1_5_Z6_mem0 += MAIN_MEM_r[0]

	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	S += k1_5_Z6_mem1 >= 61
	k1_5_Z6_mem1 += MM_MEM[1]

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	S += DY3_in >= 62
	DY3_in += MM_in[0]

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	S += DY3_mem0 >= 62
	DY3_mem0 += MAS_MEM[0]

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	S += DY3_mem1 >= 62
	DY3_mem1 += MAIN_MEM_r[1]

	k1_5_Z6 = S.Task('k1_5_Z6', length=11, delay_cost=1)
	S += k1_5_Z6 >= 62
	k1_5_Z6 += MM[0]

	DY3 = S.Task('DY3', length=11, delay_cost=1)
	S += DY3 >= 63
	DY3 += MM[0]

	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	S += k3_10_Z6_in >= 63
	k3_10_Z6_in += MM_in[0]

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	S += k3_10_Z6_mem0 >= 63
	k3_10_Z6_mem0 += MAIN_MEM_r[0]

	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	S += k3_10_Z6_mem1 >= 63
	k3_10_Z6_mem1 += MM_MEM[1]

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	S += k2_9_Z6_in >= 64
	k2_9_Z6_in += MM_in[0]

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	S += k2_9_Z6_mem0 >= 64
	k2_9_Z6_mem0 += MAIN_MEM_r[0]

	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	S += k2_9_Z6_mem1 >= 64
	k2_9_Z6_mem1 += MM_MEM[1]

	k3_10_Z6 = S.Task('k3_10_Z6', length=11, delay_cost=1)
	S += k3_10_Z6 >= 64
	k3_10_Z6 += MM[0]

	NX4_in = S.Task('NX4_in', length=1, delay_cost=1)
	S += NX4_in >= 65
	NX4_in += MM_in[0]

	NX4_mem0 = S.Task('NX4_mem0', length=1, delay_cost=1)
	S += NX4_mem0 >= 65
	NX4_mem0 += MAS_MEM[4]

	NX4_mem1 = S.Task('NX4_mem1', length=1, delay_cost=1)
	S += NX4_mem1 >= 65
	NX4_mem1 += MAIN_MEM_r[1]

	k2_9_Z6 = S.Task('k2_9_Z6', length=11, delay_cost=1)
	S += k2_9_Z6 >= 65
	k2_9_Z6 += MM[0]

	NX4 = S.Task('NX4', length=11, delay_cost=1)
	S += NX4 >= 66
	NX4 += MM[0]

	NY4_in = S.Task('NY4_in', length=1, delay_cost=1)
	S += NY4_in >= 66
	NY4_in += MM_in[0]

	NY4_mem0 = S.Task('NY4_mem0', length=1, delay_cost=1)
	S += NY4_mem0 >= 66
	NY4_mem0 += MAS_MEM[0]

	NY4_mem1 = S.Task('NY4_mem1', length=1, delay_cost=1)
	S += NY4_mem1 >= 66
	NY4_mem1 += MAIN_MEM_r[1]

	NY4 = S.Task('NY4', length=11, delay_cost=1)
	S += NY4 >= 67
	NY4 += MM[0]

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	S += Z_exp8_in >= 69
	Z_exp8_in += MM_in[0]

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	S += Z_exp8_mem0 >= 69
	Z_exp8_mem0 += MM_MEM[0]

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	S += Z_exp8_mem1 >= 69
	Z_exp8_mem1 += MAIN_MEM_r[1]

	Z_exp8 = S.Task('Z_exp8', length=11, delay_cost=1)
	S += Z_exp8 >= 70
	Z_exp8 += MM[0]

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	S += k3_9_Z7_in >= 70
	k3_9_Z7_in += MM_in[0]

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	S += k3_9_Z7_mem0 >= 70
	k3_9_Z7_mem0 += MAIN_MEM_r[0]

	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	S += k3_9_Z7_mem1 >= 70
	k3_9_Z7_mem1 += MM_MEM[1]

	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	S += k0_4_Z7_in >= 71
	k0_4_Z7_in += MM_in[0]

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	S += k0_4_Z7_mem0 >= 71
	k0_4_Z7_mem0 += MAIN_MEM_r[0]

	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	S += k0_4_Z7_mem1 >= 71
	k0_4_Z7_mem1 += MM_MEM[1]

	k3_9_Z7 = S.Task('k3_9_Z7', length=11, delay_cost=1)
	S += k3_9_Z7 >= 71
	k3_9_Z7 += MM[0]

	k0_4_Z7 = S.Task('k0_4_Z7', length=11, delay_cost=1)
	S += k0_4_Z7 >= 72
	k0_4_Z7 += MM[0]

	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	S += k2_8_Z7_in >= 72
	k2_8_Z7_in += MM_in[0]

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	S += k2_8_Z7_mem0 >= 72
	k2_8_Z7_mem0 += MAIN_MEM_r[0]

	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	S += k2_8_Z7_mem1 >= 72
	k2_8_Z7_mem1 += MM_MEM[1]

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	S += k1_4_Z7_in >= 73
	k1_4_Z7_in += MM_in[0]

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	S += k1_4_Z7_mem0 >= 73
	k1_4_Z7_mem0 += MAIN_MEM_r[0]

	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	S += k1_4_Z7_mem1 >= 73
	k1_4_Z7_mem1 += MM_MEM[1]

	k2_8_Z7 = S.Task('k2_8_Z7', length=11, delay_cost=1)
	S += k2_8_Z7 >= 73
	k2_8_Z7 += MM[0]

	DY4__in = S.Task('DY4__in', length=1, delay_cost=1)
	S += DY4__in >= 74
	DY4__in += MAS_in[0]

	DY4__mem0 = S.Task('DY4__mem0', length=1, delay_cost=1)
	S += DY4__mem0 >= 74
	DY4__mem0 += MM_MEM[0]

	DY4__mem1 = S.Task('DY4__mem1', length=1, delay_cost=1)
	S += DY4__mem1 >= 74
	DY4__mem1 += MM_MEM[1]

	k1_4_Z7 = S.Task('k1_4_Z7', length=11, delay_cost=1)
	S += k1_4_Z7 >= 74
	k1_4_Z7 += MM[0]

	DX4__in = S.Task('DX4__in', length=1, delay_cost=1)
	S += DX4__in >= 75
	DX4__in += MAS_in[0]

	DX4__mem0 = S.Task('DX4__mem0', length=1, delay_cost=1)
	S += DX4__mem0 >= 75
	DX4__mem0 += MM_MEM[0]

	DX4__mem1 = S.Task('DX4__mem1', length=1, delay_cost=1)
	S += DX4__mem1 >= 75
	DX4__mem1 += MM_MEM[1]

	DY4_ = S.Task('DY4_', length=3, delay_cost=1)
	S += DY4_ >= 75
	DY4_ += MAS[0]

	DX4_ = S.Task('DX4_', length=3, delay_cost=1)
	S += DX4_ >= 76
	DX4_ += MAS[0]

	NX5__in = S.Task('NX5__in', length=1, delay_cost=1)
	S += NX5__in >= 76
	NX5__in += MAS_in[0]

	NX5__mem0 = S.Task('NX5__mem0', length=1, delay_cost=1)
	S += NX5__mem0 >= 76
	NX5__mem0 += MM_MEM[0]

	NX5__mem1 = S.Task('NX5__mem1', length=1, delay_cost=1)
	S += NX5__mem1 >= 76
	NX5__mem1 += MM_MEM[1]

	DY4_in = S.Task('DY4_in', length=1, delay_cost=1)
	S += DY4_in >= 77
	DY4_in += MM_in[0]

	DY4_mem0 = S.Task('DY4_mem0', length=1, delay_cost=1)
	S += DY4_mem0 >= 77
	DY4_mem0 += MAS_MEM[0]

	DY4_mem1 = S.Task('DY4_mem1', length=1, delay_cost=1)
	S += DY4_mem1 >= 77
	DY4_mem1 += MAIN_MEM_r[1]

	NX5_ = S.Task('NX5_', length=3, delay_cost=1)
	S += NX5_ >= 77
	NX5_ += MAS[0]

	NY5__in = S.Task('NY5__in', length=1, delay_cost=1)
	S += NY5__in >= 77
	NY5__in += MAS_in[2]

	NY5__mem0 = S.Task('NY5__mem0', length=1, delay_cost=1)
	S += NY5__mem0 >= 77
	NY5__mem0 += MM_MEM[0]

	NY5__mem1 = S.Task('NY5__mem1', length=1, delay_cost=1)
	S += NY5__mem1 >= 77
	NY5__mem1 += MM_MEM[1]

	DX4_in = S.Task('DX4_in', length=1, delay_cost=1)
	S += DX4_in >= 78
	DX4_in += MM_in[0]

	DX4_mem0 = S.Task('DX4_mem0', length=1, delay_cost=1)
	S += DX4_mem0 >= 78
	DX4_mem0 += MAS_MEM[0]

	DX4_mem1 = S.Task('DX4_mem1', length=1, delay_cost=1)
	S += DX4_mem1 >= 78
	DX4_mem1 += MAIN_MEM_r[1]

	DY4 = S.Task('DY4', length=11, delay_cost=1)
	S += DY4 >= 78
	DY4 += MM[0]

	NY5_ = S.Task('NY5_', length=3, delay_cost=1)
	S += NY5_ >= 78
	NY5_ += MAS[2]

	DX4 = S.Task('DX4', length=11, delay_cost=1)
	S += DX4 >= 79
	DX4 += MM[0]

	NX5_in = S.Task('NX5_in', length=1, delay_cost=1)
	S += NX5_in >= 79
	NX5_in += MM_in[0]

	NX5_mem0 = S.Task('NX5_mem0', length=1, delay_cost=1)
	S += NX5_mem0 >= 79
	NX5_mem0 += MAS_MEM[0]

	NX5_mem1 = S.Task('NX5_mem1', length=1, delay_cost=1)
	S += NX5_mem1 >= 79
	NX5_mem1 += MAIN_MEM_r[1]

	NX5 = S.Task('NX5', length=11, delay_cost=1)
	S += NX5 >= 80
	NX5 += MM[0]

	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	S += k3_8_Z8_in >= 80
	k3_8_Z8_in += MM_in[0]

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	S += k3_8_Z8_mem0 >= 80
	k3_8_Z8_mem0 += MAIN_MEM_r[0]

	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	S += k3_8_Z8_mem1 >= 80
	k3_8_Z8_mem1 += MM_MEM[1]

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	S += Z_exp9_in >= 81
	Z_exp9_in += MM_in[0]

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	S += Z_exp9_mem0 >= 81
	Z_exp9_mem0 += MM_MEM[0]

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	S += Z_exp9_mem1 >= 81
	Z_exp9_mem1 += MAIN_MEM_r[1]

	k3_8_Z8 = S.Task('k3_8_Z8', length=11, delay_cost=1)
	S += k3_8_Z8 >= 81
	k3_8_Z8 += MM[0]

	Z_exp9 = S.Task('Z_exp9', length=11, delay_cost=1)
	S += Z_exp9 >= 82
	Z_exp9 += MM[0]

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	S += k2_7_Z8_in >= 82
	k2_7_Z8_in += MM_in[0]

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	S += k2_7_Z8_mem0 >= 82
	k2_7_Z8_mem0 += MAIN_MEM_r[0]

	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	S += k2_7_Z8_mem1 >= 82
	k2_7_Z8_mem1 += MM_MEM[1]

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	S += k0_3_Z8_in >= 83
	k0_3_Z8_in += MM_in[0]

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	S += k0_3_Z8_mem0 >= 83
	k0_3_Z8_mem0 += MAIN_MEM_r[0]

	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	S += k0_3_Z8_mem1 >= 83
	k0_3_Z8_mem1 += MM_MEM[1]

	k2_7_Z8 = S.Task('k2_7_Z8', length=11, delay_cost=1)
	S += k2_7_Z8 >= 83
	k2_7_Z8 += MM[0]

	k0_3_Z8 = S.Task('k0_3_Z8', length=11, delay_cost=1)
	S += k0_3_Z8 >= 84
	k0_3_Z8 += MM[0]

	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	S += k1_3_Z8_in >= 84
	k1_3_Z8_in += MM_in[0]

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	S += k1_3_Z8_mem0 >= 84
	k1_3_Z8_mem0 += MAIN_MEM_r[0]

	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	S += k1_3_Z8_mem1 >= 84
	k1_3_Z8_mem1 += MM_MEM[1]

	NY5_in = S.Task('NY5_in', length=1, delay_cost=1)
	S += NY5_in >= 85
	NY5_in += MM_in[0]

	NY5_mem0 = S.Task('NY5_mem0', length=1, delay_cost=1)
	S += NY5_mem0 >= 85
	NY5_mem0 += MAS_MEM[4]

	NY5_mem1 = S.Task('NY5_mem1', length=1, delay_cost=1)
	S += NY5_mem1 >= 85
	NY5_mem1 += MAIN_MEM_r[1]

	k1_3_Z8 = S.Task('k1_3_Z8', length=11, delay_cost=1)
	S += k1_3_Z8 >= 85
	k1_3_Z8 += MM[0]

	NY5 = S.Task('NY5', length=11, delay_cost=1)
	S += NY5 >= 86
	NY5 += MM[0]

	DY5__in = S.Task('DY5__in', length=1, delay_cost=1)
	S += DY5__in >= 88
	DY5__in += MAS_in[0]

	DY5__mem0 = S.Task('DY5__mem0', length=1, delay_cost=1)
	S += DY5__mem0 >= 88
	DY5__mem0 += MM_MEM[0]

	DY5__mem1 = S.Task('DY5__mem1', length=1, delay_cost=1)
	S += DY5__mem1 >= 88
	DY5__mem1 += MM_MEM[1]

	DX5__in = S.Task('DX5__in', length=1, delay_cost=1)
	S += DX5__in >= 89
	DX5__in += MAS_in[2]

	DX5__mem0 = S.Task('DX5__mem0', length=1, delay_cost=1)
	S += DX5__mem0 >= 89
	DX5__mem0 += MM_MEM[0]

	DX5__mem1 = S.Task('DX5__mem1', length=1, delay_cost=1)
	S += DX5__mem1 >= 89
	DX5__mem1 += MM_MEM[1]

	DY5_ = S.Task('DY5_', length=3, delay_cost=1)
	S += DY5_ >= 89
	DY5_ += MAS[0]

	DX5_ = S.Task('DX5_', length=3, delay_cost=1)
	S += DX5_ >= 90
	DX5_ += MAS[2]

	NX6__in = S.Task('NX6__in', length=1, delay_cost=1)
	S += NX6__in >= 90
	NX6__in += MAS_in[0]

	NX6__mem0 = S.Task('NX6__mem0', length=1, delay_cost=1)
	S += NX6__mem0 >= 90
	NX6__mem0 += MM_MEM[0]

	NX6__mem1 = S.Task('NX6__mem1', length=1, delay_cost=1)
	S += NX6__mem1 >= 90
	NX6__mem1 += MM_MEM[1]

	DY5_in = S.Task('DY5_in', length=1, delay_cost=1)
	S += DY5_in >= 91
	DY5_in += MM_in[0]

	DY5_mem0 = S.Task('DY5_mem0', length=1, delay_cost=1)
	S += DY5_mem0 >= 91
	DY5_mem0 += MAS_MEM[0]

	DY5_mem1 = S.Task('DY5_mem1', length=1, delay_cost=1)
	S += DY5_mem1 >= 91
	DY5_mem1 += MAIN_MEM_r[1]

	NX6_ = S.Task('NX6_', length=3, delay_cost=1)
	S += NX6_ >= 91
	NX6_ += MAS[0]

	DY5 = S.Task('DY5', length=11, delay_cost=1)
	S += DY5 >= 92
	DY5 += MM[0]

	Z_exp10_in = S.Task('Z_exp10_in', length=1, delay_cost=1)
	S += Z_exp10_in >= 92
	Z_exp10_in += MM_in[0]

	Z_exp10_mem0 = S.Task('Z_exp10_mem0', length=1, delay_cost=1)
	S += Z_exp10_mem0 >= 92
	Z_exp10_mem0 += MM_MEM[0]

	Z_exp10_mem1 = S.Task('Z_exp10_mem1', length=1, delay_cost=1)
	S += Z_exp10_mem1 >= 92
	Z_exp10_mem1 += MAIN_MEM_r[1]

	DX5_in = S.Task('DX5_in', length=1, delay_cost=1)
	S += DX5_in >= 93
	DX5_in += MM_in[0]

	DX5_mem0 = S.Task('DX5_mem0', length=1, delay_cost=1)
	S += DX5_mem0 >= 93
	DX5_mem0 += MAS_MEM[4]

	DX5_mem1 = S.Task('DX5_mem1', length=1, delay_cost=1)
	S += DX5_mem1 >= 93
	DX5_mem1 += MAIN_MEM_r[1]

	Z_exp10 = S.Task('Z_exp10', length=11, delay_cost=1)
	S += Z_exp10 >= 93
	Z_exp10 += MM[0]

	DX5 = S.Task('DX5', length=11, delay_cost=1)
	S += DX5 >= 94
	DX5 += MM[0]

	k1_2_Z9_in = S.Task('k1_2_Z9_in', length=1, delay_cost=1)
	S += k1_2_Z9_in >= 94
	k1_2_Z9_in += MM_in[0]

	k1_2_Z9_mem0 = S.Task('k1_2_Z9_mem0', length=1, delay_cost=1)
	S += k1_2_Z9_mem0 >= 94
	k1_2_Z9_mem0 += MAIN_MEM_r[0]

	k1_2_Z9_mem1 = S.Task('k1_2_Z9_mem1', length=1, delay_cost=1)
	S += k1_2_Z9_mem1 >= 94
	k1_2_Z9_mem1 += MM_MEM[1]

	k0_2_Z9_in = S.Task('k0_2_Z9_in', length=1, delay_cost=1)
	S += k0_2_Z9_in >= 95
	k0_2_Z9_in += MM_in[0]

	k0_2_Z9_mem0 = S.Task('k0_2_Z9_mem0', length=1, delay_cost=1)
	S += k0_2_Z9_mem0 >= 95
	k0_2_Z9_mem0 += MAIN_MEM_r[0]

	k0_2_Z9_mem1 = S.Task('k0_2_Z9_mem1', length=1, delay_cost=1)
	S += k0_2_Z9_mem1 >= 95
	k0_2_Z9_mem1 += MM_MEM[1]

	k1_2_Z9 = S.Task('k1_2_Z9', length=11, delay_cost=1)
	S += k1_2_Z9 >= 95
	k1_2_Z9 += MM[0]

	NX6_in = S.Task('NX6_in', length=1, delay_cost=1)
	S += NX6_in >= 96
	NX6_in += MM_in[0]

	NX6_mem0 = S.Task('NX6_mem0', length=1, delay_cost=1)
	S += NX6_mem0 >= 96
	NX6_mem0 += MAS_MEM[0]

	NX6_mem1 = S.Task('NX6_mem1', length=1, delay_cost=1)
	S += NX6_mem1 >= 96
	NX6_mem1 += MAIN_MEM_r[1]

	NY6__in = S.Task('NY6__in', length=1, delay_cost=1)
	S += NY6__in >= 96
	NY6__in += MAS_in[0]

	NY6__mem0 = S.Task('NY6__mem0', length=1, delay_cost=1)
	S += NY6__mem0 >= 96
	NY6__mem0 += MM_MEM[0]

	NY6__mem1 = S.Task('NY6__mem1', length=1, delay_cost=1)
	S += NY6__mem1 >= 96
	NY6__mem1 += MM_MEM[1]

	k0_2_Z9 = S.Task('k0_2_Z9', length=11, delay_cost=1)
	S += k0_2_Z9 >= 96
	k0_2_Z9 += MM[0]

	NX6 = S.Task('NX6', length=11, delay_cost=1)
	S += NX6 >= 97
	NX6 += MM[0]

	NY6_ = S.Task('NY6_', length=3, delay_cost=1)
	S += NY6_ >= 97
	NY6_ += MAS[0]

	k2_6_Z9_in = S.Task('k2_6_Z9_in', length=1, delay_cost=1)
	S += k2_6_Z9_in >= 97
	k2_6_Z9_in += MM_in[0]

	k2_6_Z9_mem0 = S.Task('k2_6_Z9_mem0', length=1, delay_cost=1)
	S += k2_6_Z9_mem0 >= 97
	k2_6_Z9_mem0 += MAIN_MEM_r[0]

	k2_6_Z9_mem1 = S.Task('k2_6_Z9_mem1', length=1, delay_cost=1)
	S += k2_6_Z9_mem1 >= 97
	k2_6_Z9_mem1 += MM_MEM[1]

	k2_6_Z9 = S.Task('k2_6_Z9', length=11, delay_cost=1)
	S += k2_6_Z9 >= 98
	k2_6_Z9 += MM[0]

	k3_7_Z9_in = S.Task('k3_7_Z9_in', length=1, delay_cost=1)
	S += k3_7_Z9_in >= 98
	k3_7_Z9_in += MM_in[0]

	k3_7_Z9_mem0 = S.Task('k3_7_Z9_mem0', length=1, delay_cost=1)
	S += k3_7_Z9_mem0 >= 98
	k3_7_Z9_mem0 += MAIN_MEM_r[0]

	k3_7_Z9_mem1 = S.Task('k3_7_Z9_mem1', length=1, delay_cost=1)
	S += k3_7_Z9_mem1 >= 98
	k3_7_Z9_mem1 += MM_MEM[1]

	NY6_in = S.Task('NY6_in', length=1, delay_cost=1)
	S += NY6_in >= 99
	NY6_in += MM_in[0]

	NY6_mem0 = S.Task('NY6_mem0', length=1, delay_cost=1)
	S += NY6_mem0 >= 99
	NY6_mem0 += MAS_MEM[0]

	NY6_mem1 = S.Task('NY6_mem1', length=1, delay_cost=1)
	S += NY6_mem1 >= 99
	NY6_mem1 += MAIN_MEM_r[1]

	k3_7_Z9 = S.Task('k3_7_Z9', length=11, delay_cost=1)
	S += k3_7_Z9 >= 99
	k3_7_Z9 += MM[0]

	NY6 = S.Task('NY6', length=11, delay_cost=1)
	S += NY6 >= 100
	NY6 += MM[0]

	DY6__in = S.Task('DY6__in', length=1, delay_cost=1)
	S += DY6__in >= 102
	DY6__in += MAS_in[1]

	DY6__mem0 = S.Task('DY6__mem0', length=1, delay_cost=1)
	S += DY6__mem0 >= 102
	DY6__mem0 += MM_MEM[0]

	DY6__mem1 = S.Task('DY6__mem1', length=1, delay_cost=1)
	S += DY6__mem1 >= 102
	DY6__mem1 += MM_MEM[1]

	DY6_ = S.Task('DY6_', length=3, delay_cost=1)
	S += DY6_ >= 103
	DY6_ += MAS[1]

	Z_exp11_in = S.Task('Z_exp11_in', length=1, delay_cost=1)
	S += Z_exp11_in >= 103
	Z_exp11_in += MM_in[0]

	Z_exp11_mem0 = S.Task('Z_exp11_mem0', length=1, delay_cost=1)
	S += Z_exp11_mem0 >= 103
	Z_exp11_mem0 += MM_MEM[0]

	Z_exp11_mem1 = S.Task('Z_exp11_mem1', length=1, delay_cost=1)
	S += Z_exp11_mem1 >= 103
	Z_exp11_mem1 += MAIN_MEM_r[1]

	Z_exp11 = S.Task('Z_exp11', length=11, delay_cost=1)
	S += Z_exp11 >= 104
	Z_exp11 += MM[0]

	k3_6_Z10_in = S.Task('k3_6_Z10_in', length=1, delay_cost=1)
	S += k3_6_Z10_in >= 104
	k3_6_Z10_in += MM_in[0]

	k3_6_Z10_mem0 = S.Task('k3_6_Z10_mem0', length=1, delay_cost=1)
	S += k3_6_Z10_mem0 >= 104
	k3_6_Z10_mem0 += MAIN_MEM_r[0]

	k3_6_Z10_mem1 = S.Task('k3_6_Z10_mem1', length=1, delay_cost=1)
	S += k3_6_Z10_mem1 >= 104
	k3_6_Z10_mem1 += MM_MEM[1]

	DX6__in = S.Task('DX6__in', length=1, delay_cost=1)
	S += DX6__in >= 105
	DX6__in += MAS_in[2]

	DX6__mem0 = S.Task('DX6__mem0', length=1, delay_cost=1)
	S += DX6__mem0 >= 105
	DX6__mem0 += MM_MEM[0]

	DX6__mem1 = S.Task('DX6__mem1', length=1, delay_cost=1)
	S += DX6__mem1 >= 105
	DX6__mem1 += MM_MEM[1]

	DY6_in = S.Task('DY6_in', length=1, delay_cost=1)
	S += DY6_in >= 105
	DY6_in += MM_in[0]

	DY6_mem0 = S.Task('DY6_mem0', length=1, delay_cost=1)
	S += DY6_mem0 >= 105
	DY6_mem0 += MAS_MEM[2]

	DY6_mem1 = S.Task('DY6_mem1', length=1, delay_cost=1)
	S += DY6_mem1 >= 105
	DY6_mem1 += MAIN_MEM_r[1]

	k3_6_Z10 = S.Task('k3_6_Z10', length=11, delay_cost=1)
	S += k3_6_Z10 >= 105
	k3_6_Z10 += MM[0]

	DX6_ = S.Task('DX6_', length=3, delay_cost=1)
	S += DX6_ >= 106
	DX6_ += MAS[2]

	DY6 = S.Task('DY6', length=11, delay_cost=1)
	S += DY6 >= 106
	DY6 += MM[0]

	k1_1_Z10_in = S.Task('k1_1_Z10_in', length=1, delay_cost=1)
	S += k1_1_Z10_in >= 106
	k1_1_Z10_in += MM_in[0]

	k1_1_Z10_mem0 = S.Task('k1_1_Z10_mem0', length=1, delay_cost=1)
	S += k1_1_Z10_mem0 >= 106
	k1_1_Z10_mem0 += MAIN_MEM_r[0]

	k1_1_Z10_mem1 = S.Task('k1_1_Z10_mem1', length=1, delay_cost=1)
	S += k1_1_Z10_mem1 >= 106
	k1_1_Z10_mem1 += MM_MEM[1]

	k1_1_Z10 = S.Task('k1_1_Z10', length=11, delay_cost=1)
	S += k1_1_Z10 >= 107
	k1_1_Z10 += MM[0]

	k2_5_Z10_in = S.Task('k2_5_Z10_in', length=1, delay_cost=1)
	S += k2_5_Z10_in >= 107
	k2_5_Z10_in += MM_in[0]

	k2_5_Z10_mem0 = S.Task('k2_5_Z10_mem0', length=1, delay_cost=1)
	S += k2_5_Z10_mem0 >= 107
	k2_5_Z10_mem0 += MAIN_MEM_r[0]

	k2_5_Z10_mem1 = S.Task('k2_5_Z10_mem1', length=1, delay_cost=1)
	S += k2_5_Z10_mem1 >= 107
	k2_5_Z10_mem1 += MM_MEM[1]

	DX6_in = S.Task('DX6_in', length=1, delay_cost=1)
	S += DX6_in >= 108
	DX6_in += MM_in[0]

	DX6_mem0 = S.Task('DX6_mem0', length=1, delay_cost=1)
	S += DX6_mem0 >= 108
	DX6_mem0 += MAS_MEM[4]

	DX6_mem1 = S.Task('DX6_mem1', length=1, delay_cost=1)
	S += DX6_mem1 >= 108
	DX6_mem1 += MAIN_MEM_r[1]

	NX7__in = S.Task('NX7__in', length=1, delay_cost=1)
	S += NX7__in >= 108
	NX7__in += MAS_in[2]

	NX7__mem0 = S.Task('NX7__mem0', length=1, delay_cost=1)
	S += NX7__mem0 >= 108
	NX7__mem0 += MM_MEM[0]

	NX7__mem1 = S.Task('NX7__mem1', length=1, delay_cost=1)
	S += NX7__mem1 >= 108
	NX7__mem1 += MM_MEM[1]

	k2_5_Z10 = S.Task('k2_5_Z10', length=11, delay_cost=1)
	S += k2_5_Z10 >= 108
	k2_5_Z10 += MM[0]

	DX6 = S.Task('DX6', length=11, delay_cost=1)
	S += DX6 >= 109
	DX6 += MM[0]

	NX7_ = S.Task('NX7_', length=3, delay_cost=1)
	S += NX7_ >= 109
	NX7_ += MAS[2]

	k0_1_Z10_in = S.Task('k0_1_Z10_in', length=1, delay_cost=1)
	S += k0_1_Z10_in >= 109
	k0_1_Z10_in += MM_in[0]

	k0_1_Z10_mem0 = S.Task('k0_1_Z10_mem0', length=1, delay_cost=1)
	S += k0_1_Z10_mem0 >= 109
	k0_1_Z10_mem0 += MAIN_MEM_r[0]

	k0_1_Z10_mem1 = S.Task('k0_1_Z10_mem1', length=1, delay_cost=1)
	S += k0_1_Z10_mem1 >= 109
	k0_1_Z10_mem1 += MM_MEM[1]

	NY7__in = S.Task('NY7__in', length=1, delay_cost=1)
	S += NY7__in >= 110
	NY7__in += MAS_in[0]

	NY7__mem0 = S.Task('NY7__mem0', length=1, delay_cost=1)
	S += NY7__mem0 >= 110
	NY7__mem0 += MM_MEM[0]

	NY7__mem1 = S.Task('NY7__mem1', length=1, delay_cost=1)
	S += NY7__mem1 >= 110
	NY7__mem1 += MM_MEM[1]

	k0_1_Z10 = S.Task('k0_1_Z10', length=11, delay_cost=1)
	S += k0_1_Z10 >= 110
	k0_1_Z10 += MM[0]

	NX7_in = S.Task('NX7_in', length=1, delay_cost=1)
	S += NX7_in >= 111
	NX7_in += MM_in[0]

	NX7_mem0 = S.Task('NX7_mem0', length=1, delay_cost=1)
	S += NX7_mem0 >= 111
	NX7_mem0 += MAS_MEM[4]

	NX7_mem1 = S.Task('NX7_mem1', length=1, delay_cost=1)
	S += NX7_mem1 >= 111
	NX7_mem1 += MAIN_MEM_r[1]

	NY7_ = S.Task('NY7_', length=3, delay_cost=1)
	S += NY7_ >= 111
	NY7_ += MAS[0]

	NX7 = S.Task('NX7', length=11, delay_cost=1)
	S += NX7 >= 112
	NX7 += MM[0]

	NY7_in = S.Task('NY7_in', length=1, delay_cost=1)
	S += NY7_in >= 113
	NY7_in += MM_in[0]

	NY7_mem0 = S.Task('NY7_mem0', length=1, delay_cost=1)
	S += NY7_mem0 >= 113
	NY7_mem0 += MAS_MEM[0]

	NY7_mem1 = S.Task('NY7_mem1', length=1, delay_cost=1)
	S += NY7_mem1 >= 113
	NY7_mem1 += MAIN_MEM_r[1]

	NY7 = S.Task('NY7', length=11, delay_cost=1)
	S += NY7 >= 114
	NY7 += MM[0]

	Z_exp12_in = S.Task('Z_exp12_in', length=1, delay_cost=1)
	S += Z_exp12_in >= 114
	Z_exp12_in += MM_in[0]

	Z_exp12_mem0 = S.Task('Z_exp12_mem0', length=1, delay_cost=1)
	S += Z_exp12_mem0 >= 114
	Z_exp12_mem0 += MM_MEM[0]

	Z_exp12_mem1 = S.Task('Z_exp12_mem1', length=1, delay_cost=1)
	S += Z_exp12_mem1 >= 114
	Z_exp12_mem1 += MAIN_MEM_r[1]

	Z_exp12 = S.Task('Z_exp12', length=11, delay_cost=1)
	S += Z_exp12 >= 115
	Z_exp12 += MM[0]

	k2_4_Z11_in = S.Task('k2_4_Z11_in', length=1, delay_cost=1)
	S += k2_4_Z11_in >= 115
	k2_4_Z11_in += MM_in[0]

	k2_4_Z11_mem0 = S.Task('k2_4_Z11_mem0', length=1, delay_cost=1)
	S += k2_4_Z11_mem0 >= 115
	k2_4_Z11_mem0 += MAIN_MEM_r[0]

	k2_4_Z11_mem1 = S.Task('k2_4_Z11_mem1', length=1, delay_cost=1)
	S += k2_4_Z11_mem1 >= 115
	k2_4_Z11_mem1 += MM_MEM[1]

	k0_0_Z11_in = S.Task('k0_0_Z11_in', length=1, delay_cost=1)
	S += k0_0_Z11_in >= 116
	k0_0_Z11_in += MM_in[0]

	k0_0_Z11_mem0 = S.Task('k0_0_Z11_mem0', length=1, delay_cost=1)
	S += k0_0_Z11_mem0 >= 116
	k0_0_Z11_mem0 += MAIN_MEM_r[0]

	k0_0_Z11_mem1 = S.Task('k0_0_Z11_mem1', length=1, delay_cost=1)
	S += k0_0_Z11_mem1 >= 116
	k0_0_Z11_mem1 += MM_MEM[1]

	k2_4_Z11 = S.Task('k2_4_Z11', length=11, delay_cost=1)
	S += k2_4_Z11 >= 116
	k2_4_Z11 += MM[0]

	k0_0_Z11 = S.Task('k0_0_Z11', length=11, delay_cost=1)
	S += k0_0_Z11 >= 117
	k0_0_Z11 += MM[0]

	k3_5_Z11_in = S.Task('k3_5_Z11_in', length=1, delay_cost=1)
	S += k3_5_Z11_in >= 117
	k3_5_Z11_in += MM_in[0]

	k3_5_Z11_mem0 = S.Task('k3_5_Z11_mem0', length=1, delay_cost=1)
	S += k3_5_Z11_mem0 >= 117
	k3_5_Z11_mem0 += MAIN_MEM_r[0]

	k3_5_Z11_mem1 = S.Task('k3_5_Z11_mem1', length=1, delay_cost=1)
	S += k3_5_Z11_mem1 >= 117
	k3_5_Z11_mem1 += MM_MEM[1]

	k1_0_Z11_in = S.Task('k1_0_Z11_in', length=1, delay_cost=1)
	S += k1_0_Z11_in >= 118
	k1_0_Z11_in += MM_in[0]

	k1_0_Z11_mem0 = S.Task('k1_0_Z11_mem0', length=1, delay_cost=1)
	S += k1_0_Z11_mem0 >= 118
	k1_0_Z11_mem0 += MAIN_MEM_r[0]

	k1_0_Z11_mem1 = S.Task('k1_0_Z11_mem1', length=1, delay_cost=1)
	S += k1_0_Z11_mem1 >= 118
	k1_0_Z11_mem1 += MM_MEM[1]

	k3_5_Z11 = S.Task('k3_5_Z11', length=11, delay_cost=1)
	S += k3_5_Z11 >= 118
	k3_5_Z11 += MM[0]

	DY7__in = S.Task('DY7__in', length=1, delay_cost=1)
	S += DY7__in >= 119
	DY7__in += MAS_in[0]

	DY7__mem0 = S.Task('DY7__mem0', length=1, delay_cost=1)
	S += DY7__mem0 >= 119
	DY7__mem0 += MM_MEM[0]

	DY7__mem1 = S.Task('DY7__mem1', length=1, delay_cost=1)
	S += DY7__mem1 >= 119
	DY7__mem1 += MM_MEM[1]

	k1_0_Z11 = S.Task('k1_0_Z11', length=11, delay_cost=1)
	S += k1_0_Z11 >= 119
	k1_0_Z11 += MM[0]

	DX7__in = S.Task('DX7__in', length=1, delay_cost=1)
	S += DX7__in >= 120
	DX7__in += MAS_in[1]

	DX7__mem0 = S.Task('DX7__mem0', length=1, delay_cost=1)
	S += DX7__mem0 >= 120
	DX7__mem0 += MM_MEM[0]

	DX7__mem1 = S.Task('DX7__mem1', length=1, delay_cost=1)
	S += DX7__mem1 >= 120
	DX7__mem1 += MM_MEM[1]

	DY7_ = S.Task('DY7_', length=3, delay_cost=1)
	S += DY7_ >= 120
	DY7_ += MAS[0]

	DX7_ = S.Task('DX7_', length=3, delay_cost=1)
	S += DX7_ >= 121
	DX7_ += MAS[1]

	DY7_in = S.Task('DY7_in', length=1, delay_cost=1)
	S += DY7_in >= 122
	DY7_in += MM_in[0]

	DY7_mem0 = S.Task('DY7_mem0', length=1, delay_cost=1)
	S += DY7_mem0 >= 122
	DY7_mem0 += MAS_MEM[0]

	DY7_mem1 = S.Task('DY7_mem1', length=1, delay_cost=1)
	S += DY7_mem1 >= 122
	DY7_mem1 += MAIN_MEM_r[1]

	NX8__in = S.Task('NX8__in', length=1, delay_cost=1)
	S += NX8__in >= 122
	NX8__in += MAS_in[0]

	NX8__mem0 = S.Task('NX8__mem0', length=1, delay_cost=1)
	S += NX8__mem0 >= 122
	NX8__mem0 += MM_MEM[0]

	NX8__mem1 = S.Task('NX8__mem1', length=1, delay_cost=1)
	S += NX8__mem1 >= 122
	NX8__mem1 += MM_MEM[1]

	DX7_in = S.Task('DX7_in', length=1, delay_cost=1)
	S += DX7_in >= 123
	DX7_in += MM_in[0]

	DX7_mem0 = S.Task('DX7_mem0', length=1, delay_cost=1)
	S += DX7_mem0 >= 123
	DX7_mem0 += MAS_MEM[2]

	DX7_mem1 = S.Task('DX7_mem1', length=1, delay_cost=1)
	S += DX7_mem1 >= 123
	DX7_mem1 += MAIN_MEM_r[1]

	DY7 = S.Task('DY7', length=11, delay_cost=1)
	S += DY7 >= 123
	DY7 += MM[0]

	NX8_ = S.Task('NX8_', length=3, delay_cost=1)
	S += NX8_ >= 123
	NX8_ += MAS[0]

	DX7 = S.Task('DX7', length=11, delay_cost=1)
	S += DX7 >= 124
	DX7 += MM[0]

	NY8__in = S.Task('NY8__in', length=1, delay_cost=1)
	S += NY8__in >= 124
	NY8__in += MAS_in[1]

	NY8__mem0 = S.Task('NY8__mem0', length=1, delay_cost=1)
	S += NY8__mem0 >= 124
	NY8__mem0 += MM_MEM[0]

	NY8__mem1 = S.Task('NY8__mem1', length=1, delay_cost=1)
	S += NY8__mem1 >= 124
	NY8__mem1 += MM_MEM[1]

	NY8_ = S.Task('NY8_', length=3, delay_cost=1)
	S += NY8_ >= 125
	NY8_ += MAS[1]

	Z_exp13_in = S.Task('Z_exp13_in', length=1, delay_cost=1)
	S += Z_exp13_in >= 125
	Z_exp13_in += MM_in[0]

	Z_exp13_mem0 = S.Task('Z_exp13_mem0', length=1, delay_cost=1)
	S += Z_exp13_mem0 >= 125
	Z_exp13_mem0 += MM_MEM[0]

	Z_exp13_mem1 = S.Task('Z_exp13_mem1', length=1, delay_cost=1)
	S += Z_exp13_mem1 >= 125
	Z_exp13_mem1 += MAIN_MEM_r[1]

	Z_exp13 = S.Task('Z_exp13', length=11, delay_cost=1)
	S += Z_exp13 >= 126
	Z_exp13 += MM[0]

	k3_4_Z12_in = S.Task('k3_4_Z12_in', length=1, delay_cost=1)
	S += k3_4_Z12_in >= 126
	k3_4_Z12_in += MM_in[0]

	k3_4_Z12_mem0 = S.Task('k3_4_Z12_mem0', length=1, delay_cost=1)
	S += k3_4_Z12_mem0 >= 126
	k3_4_Z12_mem0 += MAIN_MEM_r[0]

	k3_4_Z12_mem1 = S.Task('k3_4_Z12_mem1', length=1, delay_cost=1)
	S += k3_4_Z12_mem1 >= 126
	k3_4_Z12_mem1 += MM_MEM[1]

	k2_3_Z12_in = S.Task('k2_3_Z12_in', length=1, delay_cost=1)
	S += k2_3_Z12_in >= 127
	k2_3_Z12_in += MM_in[0]

	k2_3_Z12_mem0 = S.Task('k2_3_Z12_mem0', length=1, delay_cost=1)
	S += k2_3_Z12_mem0 >= 127
	k2_3_Z12_mem0 += MAIN_MEM_r[0]

	k2_3_Z12_mem1 = S.Task('k2_3_Z12_mem1', length=1, delay_cost=1)
	S += k2_3_Z12_mem1 >= 127
	k2_3_Z12_mem1 += MM_MEM[1]

	k3_4_Z12 = S.Task('k3_4_Z12', length=11, delay_cost=1)
	S += k3_4_Z12 >= 127
	k3_4_Z12 += MM[0]

	NY8_in = S.Task('NY8_in', length=1, delay_cost=1)
	S += NY8_in >= 128
	NY8_in += MM_in[0]

	NY8_mem0 = S.Task('NY8_mem0', length=1, delay_cost=1)
	S += NY8_mem0 >= 128
	NY8_mem0 += MAS_MEM[2]

	NY8_mem1 = S.Task('NY8_mem1', length=1, delay_cost=1)
	S += NY8_mem1 >= 128
	NY8_mem1 += MAIN_MEM_r[1]

	k2_3_Z12 = S.Task('k2_3_Z12', length=11, delay_cost=1)
	S += k2_3_Z12 >= 128
	k2_3_Z12 += MM[0]

	NX8_in = S.Task('NX8_in', length=1, delay_cost=1)
	S += NX8_in >= 129
	NX8_in += MM_in[0]

	NX8_mem0 = S.Task('NX8_mem0', length=1, delay_cost=1)
	S += NX8_mem0 >= 129
	NX8_mem0 += MAS_MEM[0]

	NX8_mem1 = S.Task('NX8_mem1', length=1, delay_cost=1)
	S += NX8_mem1 >= 129
	NX8_mem1 += MAIN_MEM_r[1]

	NY8 = S.Task('NY8', length=11, delay_cost=1)
	S += NY8 >= 129
	NY8 += MM[0]

	NX8 = S.Task('NX8', length=11, delay_cost=1)
	S += NX8 >= 130
	NX8 += MM[0]

	DY8__in = S.Task('DY8__in', length=1, delay_cost=1)
	S += DY8__in >= 133
	DY8__in += MAS_in[1]

	DY8__mem0 = S.Task('DY8__mem0', length=1, delay_cost=1)
	S += DY8__mem0 >= 133
	DY8__mem0 += MM_MEM[0]

	DY8__mem1 = S.Task('DY8__mem1', length=1, delay_cost=1)
	S += DY8__mem1 >= 133
	DY8__mem1 += MM_MEM[1]

	DX8__in = S.Task('DX8__in', length=1, delay_cost=1)
	S += DX8__in >= 134
	DX8__in += MAS_in[0]

	DX8__mem0 = S.Task('DX8__mem0', length=1, delay_cost=1)
	S += DX8__mem0 >= 134
	DX8__mem0 += MM_MEM[0]

	DX8__mem1 = S.Task('DX8__mem1', length=1, delay_cost=1)
	S += DX8__mem1 >= 134
	DX8__mem1 += MM_MEM[1]

	DY8_ = S.Task('DY8_', length=3, delay_cost=1)
	S += DY8_ >= 134
	DY8_ += MAS[1]

	DX8_ = S.Task('DX8_', length=3, delay_cost=1)
	S += DX8_ >= 135
	DX8_ += MAS[0]

	Z_exp14_in = S.Task('Z_exp14_in', length=1, delay_cost=1)
	S += Z_exp14_in >= 136
	Z_exp14_in += MM_in[0]

	Z_exp14_mem0 = S.Task('Z_exp14_mem0', length=1, delay_cost=1)
	S += Z_exp14_mem0 >= 136
	Z_exp14_mem0 += MM_MEM[0]

	Z_exp14_mem1 = S.Task('Z_exp14_mem1', length=1, delay_cost=1)
	S += Z_exp14_mem1 >= 136
	Z_exp14_mem1 += MAIN_MEM_r[1]

	Z_exp14 = S.Task('Z_exp14', length=11, delay_cost=1)
	S += Z_exp14 >= 137
	Z_exp14 += MM[0]

	k2_2_Z13_in = S.Task('k2_2_Z13_in', length=1, delay_cost=1)
	S += k2_2_Z13_in >= 137
	k2_2_Z13_in += MM_in[0]

	k2_2_Z13_mem0 = S.Task('k2_2_Z13_mem0', length=1, delay_cost=1)
	S += k2_2_Z13_mem0 >= 137
	k2_2_Z13_mem0 += MAIN_MEM_r[0]

	k2_2_Z13_mem1 = S.Task('k2_2_Z13_mem1', length=1, delay_cost=1)
	S += k2_2_Z13_mem1 >= 137
	k2_2_Z13_mem1 += MM_MEM[1]

	k2_2_Z13 = S.Task('k2_2_Z13', length=11, delay_cost=1)
	S += k2_2_Z13 >= 138
	k2_2_Z13 += MM[0]

	k3_3_Z13_in = S.Task('k3_3_Z13_in', length=1, delay_cost=1)
	S += k3_3_Z13_in >= 138
	k3_3_Z13_in += MM_in[0]

	k3_3_Z13_mem0 = S.Task('k3_3_Z13_mem0', length=1, delay_cost=1)
	S += k3_3_Z13_mem0 >= 138
	k3_3_Z13_mem0 += MAIN_MEM_r[0]

	k3_3_Z13_mem1 = S.Task('k3_3_Z13_mem1', length=1, delay_cost=1)
	S += k3_3_Z13_mem1 >= 138
	k3_3_Z13_mem1 += MM_MEM[1]

	DY8_in = S.Task('DY8_in', length=1, delay_cost=1)
	S += DY8_in >= 139
	DY8_in += MM_in[0]

	DY8_mem0 = S.Task('DY8_mem0', length=1, delay_cost=1)
	S += DY8_mem0 >= 139
	DY8_mem0 += MAS_MEM[2]

	DY8_mem1 = S.Task('DY8_mem1', length=1, delay_cost=1)
	S += DY8_mem1 >= 139
	DY8_mem1 += MAIN_MEM_r[1]

	NY9__in = S.Task('NY9__in', length=1, delay_cost=1)
	S += NY9__in >= 139
	NY9__in += MAS_in[1]

	NY9__mem0 = S.Task('NY9__mem0', length=1, delay_cost=1)
	S += NY9__mem0 >= 139
	NY9__mem0 += MM_MEM[0]

	NY9__mem1 = S.Task('NY9__mem1', length=1, delay_cost=1)
	S += NY9__mem1 >= 139
	NY9__mem1 += MM_MEM[1]

	k3_3_Z13 = S.Task('k3_3_Z13', length=11, delay_cost=1)
	S += k3_3_Z13 >= 139
	k3_3_Z13 += MM[0]

	DX8_in = S.Task('DX8_in', length=1, delay_cost=1)
	S += DX8_in >= 140
	DX8_in += MM_in[0]

	DX8_mem0 = S.Task('DX8_mem0', length=1, delay_cost=1)
	S += DX8_mem0 >= 140
	DX8_mem0 += MAS_MEM[0]

	DX8_mem1 = S.Task('DX8_mem1', length=1, delay_cost=1)
	S += DX8_mem1 >= 140
	DX8_mem1 += MAIN_MEM_r[1]

	DY8 = S.Task('DY8', length=11, delay_cost=1)
	S += DY8 >= 140
	DY8 += MM[0]

	NX9__in = S.Task('NX9__in', length=1, delay_cost=1)
	S += NX9__in >= 140
	NX9__in += MAS_in[1]

	NX9__mem0 = S.Task('NX9__mem0', length=1, delay_cost=1)
	S += NX9__mem0 >= 140
	NX9__mem0 += MM_MEM[0]

	NX9__mem1 = S.Task('NX9__mem1', length=1, delay_cost=1)
	S += NX9__mem1 >= 140
	NX9__mem1 += MM_MEM[1]

	NY9_ = S.Task('NY9_', length=3, delay_cost=1)
	S += NY9_ >= 140
	NY9_ += MAS[1]

	DX8 = S.Task('DX8', length=11, delay_cost=1)
	S += DX8 >= 141
	DX8 += MM[0]

	NX9_ = S.Task('NX9_', length=3, delay_cost=1)
	S += NX9_ >= 141
	NX9_ += MAS[1]

	NY9_in = S.Task('NY9_in', length=1, delay_cost=1)
	S += NY9_in >= 142
	NY9_in += MM_in[0]

	NY9_mem0 = S.Task('NY9_mem0', length=1, delay_cost=1)
	S += NY9_mem0 >= 142
	NY9_mem0 += MAS_MEM[2]

	NY9_mem1 = S.Task('NY9_mem1', length=1, delay_cost=1)
	S += NY9_mem1 >= 142
	NY9_mem1 += MAIN_MEM_r[1]

	NX9_in = S.Task('NX9_in', length=1, delay_cost=1)
	S += NX9_in >= 143
	NX9_in += MM_in[0]

	NX9_mem0 = S.Task('NX9_mem0', length=1, delay_cost=1)
	S += NX9_mem0 >= 143
	NX9_mem0 += MAS_MEM[2]

	NX9_mem1 = S.Task('NX9_mem1', length=1, delay_cost=1)
	S += NX9_mem1 >= 143
	NX9_mem1 += MAIN_MEM_r[1]

	NY9 = S.Task('NY9', length=11, delay_cost=1)
	S += NY9 >= 143
	NY9 += MM[0]

	NX9 = S.Task('NX9', length=11, delay_cost=1)
	S += NX9 >= 144
	NX9 += MM[0]

	k3_2_Z14_in = S.Task('k3_2_Z14_in', length=1, delay_cost=1)
	S += k3_2_Z14_in >= 147
	k3_2_Z14_in += MM_in[0]

	k3_2_Z14_mem0 = S.Task('k3_2_Z14_mem0', length=1, delay_cost=1)
	S += k3_2_Z14_mem0 >= 147
	k3_2_Z14_mem0 += MAIN_MEM_r[0]

	k3_2_Z14_mem1 = S.Task('k3_2_Z14_mem1', length=1, delay_cost=1)
	S += k3_2_Z14_mem1 >= 147
	k3_2_Z14_mem1 += MM_MEM[1]

	Z_exp15_in = S.Task('Z_exp15_in', length=1, delay_cost=1)
	S += Z_exp15_in >= 148
	Z_exp15_in += MM_in[0]

	Z_exp15_mem0 = S.Task('Z_exp15_mem0', length=1, delay_cost=1)
	S += Z_exp15_mem0 >= 148
	Z_exp15_mem0 += MM_MEM[0]

	Z_exp15_mem1 = S.Task('Z_exp15_mem1', length=1, delay_cost=1)
	S += Z_exp15_mem1 >= 148
	Z_exp15_mem1 += MAIN_MEM_r[1]

	k3_2_Z14 = S.Task('k3_2_Z14', length=11, delay_cost=1)
	S += k3_2_Z14 >= 148
	k3_2_Z14 += MM[0]

	Z_exp15 = S.Task('Z_exp15', length=11, delay_cost=1)
	S += Z_exp15 >= 149
	Z_exp15 += MM[0]

	k2_1_Z14_in = S.Task('k2_1_Z14_in', length=1, delay_cost=1)
	S += k2_1_Z14_in >= 149
	k2_1_Z14_in += MM_in[0]

	k2_1_Z14_mem0 = S.Task('k2_1_Z14_mem0', length=1, delay_cost=1)
	S += k2_1_Z14_mem0 >= 149
	k2_1_Z14_mem0 += MAIN_MEM_r[0]

	k2_1_Z14_mem1 = S.Task('k2_1_Z14_mem1', length=1, delay_cost=1)
	S += k2_1_Z14_mem1 >= 149
	k2_1_Z14_mem1 += MM_MEM[1]

	DY9__in = S.Task('DY9__in', length=1, delay_cost=1)
	S += DY9__in >= 150
	DY9__in += MAS_in[1]

	DY9__mem0 = S.Task('DY9__mem0', length=1, delay_cost=1)
	S += DY9__mem0 >= 150
	DY9__mem0 += MM_MEM[0]

	DY9__mem1 = S.Task('DY9__mem1', length=1, delay_cost=1)
	S += DY9__mem1 >= 150
	DY9__mem1 += MM_MEM[1]

	k2_1_Z14 = S.Task('k2_1_Z14', length=11, delay_cost=1)
	S += k2_1_Z14 >= 150
	k2_1_Z14 += MM[0]

	DX9__in = S.Task('DX9__in', length=1, delay_cost=1)
	S += DX9__in >= 151
	DX9__in += MAS_in[0]

	DX9__mem0 = S.Task('DX9__mem0', length=1, delay_cost=1)
	S += DX9__mem0 >= 151
	DX9__mem0 += MM_MEM[0]

	DX9__mem1 = S.Task('DX9__mem1', length=1, delay_cost=1)
	S += DX9__mem1 >= 151
	DX9__mem1 += MM_MEM[1]

	DY9_ = S.Task('DY9_', length=3, delay_cost=1)
	S += DY9_ >= 151
	DY9_ += MAS[1]

	DX9_ = S.Task('DX9_', length=3, delay_cost=1)
	S += DX9_ >= 152
	DX9_ += MAS[0]

	DY9_in = S.Task('DY9_in', length=1, delay_cost=1)
	S += DY9_in >= 153
	DY9_in += MM_in[0]

	DY9_mem0 = S.Task('DY9_mem0', length=1, delay_cost=1)
	S += DY9_mem0 >= 153
	DY9_mem0 += MAS_MEM[2]

	DY9_mem1 = S.Task('DY9_mem1', length=1, delay_cost=1)
	S += DY9_mem1 >= 153
	DY9_mem1 += MAIN_MEM_r[1]

	NY10__in = S.Task('NY10__in', length=1, delay_cost=1)
	S += NY10__in >= 153
	NY10__in += MAS_in[1]

	NY10__mem0 = S.Task('NY10__mem0', length=1, delay_cost=1)
	S += NY10__mem0 >= 153
	NY10__mem0 += MM_MEM[0]

	NY10__mem1 = S.Task('NY10__mem1', length=1, delay_cost=1)
	S += NY10__mem1 >= 153
	NY10__mem1 += MM_MEM[1]

	DX9_in = S.Task('DX9_in', length=1, delay_cost=1)
	S += DX9_in >= 154
	DX9_in += MM_in[0]

	DX9_mem0 = S.Task('DX9_mem0', length=1, delay_cost=1)
	S += DX9_mem0 >= 154
	DX9_mem0 += MAS_MEM[0]

	DX9_mem1 = S.Task('DX9_mem1', length=1, delay_cost=1)
	S += DX9_mem1 >= 154
	DX9_mem1 += MAIN_MEM_r[1]

	DY9 = S.Task('DY9', length=11, delay_cost=1)
	S += DY9 >= 154
	DY9 += MM[0]

	NX10__in = S.Task('NX10__in', length=1, delay_cost=1)
	S += NX10__in >= 154
	NX10__in += MAS_in[2]

	NX10__mem0 = S.Task('NX10__mem0', length=1, delay_cost=1)
	S += NX10__mem0 >= 154
	NX10__mem0 += MM_MEM[0]

	NX10__mem1 = S.Task('NX10__mem1', length=1, delay_cost=1)
	S += NX10__mem1 >= 154
	NX10__mem1 += MM_MEM[1]

	NY10_ = S.Task('NY10_', length=3, delay_cost=1)
	S += NY10_ >= 154
	NY10_ += MAS[1]

	DX9 = S.Task('DX9', length=11, delay_cost=1)
	S += DX9 >= 155
	DX9 += MM[0]

	NX10_ = S.Task('NX10_', length=3, delay_cost=1)
	S += NX10_ >= 155
	NX10_ += MAS[2]

	NY10_in = S.Task('NY10_in', length=1, delay_cost=1)
	S += NY10_in >= 156
	NY10_in += MM_in[0]

	NY10_mem0 = S.Task('NY10_mem0', length=1, delay_cost=1)
	S += NY10_mem0 >= 156
	NY10_mem0 += MAS_MEM[2]

	NY10_mem1 = S.Task('NY10_mem1', length=1, delay_cost=1)
	S += NY10_mem1 >= 156
	NY10_mem1 += MAIN_MEM_r[1]

	NX10_in = S.Task('NX10_in', length=1, delay_cost=1)
	S += NX10_in >= 157
	NX10_in += MM_in[0]

	NX10_mem0 = S.Task('NX10_mem0', length=1, delay_cost=1)
	S += NX10_mem0 >= 157
	NX10_mem0 += MAS_MEM[4]

	NX10_mem1 = S.Task('NX10_mem1', length=1, delay_cost=1)
	S += NX10_mem1 >= 157
	NX10_mem1 += MAIN_MEM_r[1]

	NY10 = S.Task('NY10', length=11, delay_cost=1)
	S += NY10 >= 157
	NY10 += MM[0]

	NX10 = S.Task('NX10', length=11, delay_cost=1)
	S += NX10 >= 158
	NX10 += MM[0]

	k3_1_Z15_in = S.Task('k3_1_Z15_in', length=1, delay_cost=1)
	S += k3_1_Z15_in >= 159
	k3_1_Z15_in += MM_in[0]

	k3_1_Z15_mem0 = S.Task('k3_1_Z15_mem0', length=1, delay_cost=1)
	S += k3_1_Z15_mem0 >= 159
	k3_1_Z15_mem0 += MAIN_MEM_r[0]

	k3_1_Z15_mem1 = S.Task('k3_1_Z15_mem1', length=1, delay_cost=1)
	S += k3_1_Z15_mem1 >= 159
	k3_1_Z15_mem1 += MM_MEM[1]

	Z_exp16_in = S.Task('Z_exp16_in', length=1, delay_cost=1)
	S += Z_exp16_in >= 160
	Z_exp16_in += MM_in[0]

	Z_exp16_mem0 = S.Task('Z_exp16_mem0', length=1, delay_cost=1)
	S += Z_exp16_mem0 >= 160
	Z_exp16_mem0 += MM_MEM[0]

	Z_exp16_mem1 = S.Task('Z_exp16_mem1', length=1, delay_cost=1)
	S += Z_exp16_mem1 >= 160
	Z_exp16_mem1 += MAIN_MEM_r[1]

	k3_1_Z15 = S.Task('k3_1_Z15', length=11, delay_cost=1)
	S += k3_1_Z15 >= 160
	k3_1_Z15 += MM[0]

	Z_exp16 = S.Task('Z_exp16', length=11, delay_cost=1)
	S += Z_exp16 >= 161
	Z_exp16 += MM[0]

	k2_0_Z15_in = S.Task('k2_0_Z15_in', length=1, delay_cost=1)
	S += k2_0_Z15_in >= 161
	k2_0_Z15_in += MM_in[0]

	k2_0_Z15_mem0 = S.Task('k2_0_Z15_mem0', length=1, delay_cost=1)
	S += k2_0_Z15_mem0 >= 161
	k2_0_Z15_mem0 += MAIN_MEM_r[0]

	k2_0_Z15_mem1 = S.Task('k2_0_Z15_mem1', length=1, delay_cost=1)
	S += k2_0_Z15_mem1 >= 161
	k2_0_Z15_mem1 += MM_MEM[1]

	k2_0_Z15 = S.Task('k2_0_Z15', length=11, delay_cost=1)
	S += k2_0_Z15 >= 162
	k2_0_Z15 += MM[0]

	DY10__in = S.Task('DY10__in', length=1, delay_cost=1)
	S += DY10__in >= 164
	DY10__in += MAS_in[1]

	DY10__mem0 = S.Task('DY10__mem0', length=1, delay_cost=1)
	S += DY10__mem0 >= 164
	DY10__mem0 += MM_MEM[0]

	DY10__mem1 = S.Task('DY10__mem1', length=1, delay_cost=1)
	S += DY10__mem1 >= 164
	DY10__mem1 += MM_MEM[1]

	DX_in = S.Task('DX_in', length=1, delay_cost=1)
	S += DX_in >= 165
	DX_in += MAS_in[1]

	DX_mem0 = S.Task('DX_mem0', length=1, delay_cost=1)
	S += DX_mem0 >= 165
	DX_mem0 += MM_MEM[0]

	DX_mem1 = S.Task('DX_mem1', length=1, delay_cost=1)
	S += DX_mem1 >= 165
	DX_mem1 += MM_MEM[1]

	DY10_ = S.Task('DY10_', length=3, delay_cost=1)
	S += DY10_ >= 165
	DY10_ += MAS[1]

	DX = S.Task('DX', length=3, delay_cost=1)
	S += DX >= 166
	DX += MAS[1]

	DY10_in = S.Task('DY10_in', length=1, delay_cost=1)
	S += DY10_in >= 167
	DY10_in += MM_in[0]

	DY10_mem0 = S.Task('DY10_mem0', length=1, delay_cost=1)
	S += DY10_mem0 >= 167
	DY10_mem0 += MAS_MEM[2]

	DY10_mem1 = S.Task('DY10_mem1', length=1, delay_cost=1)
	S += DY10_mem1 >= 167
	DY10_mem1 += MAIN_MEM_r[1]

	NY11__in = S.Task('NY11__in', length=1, delay_cost=1)
	S += NY11__in >= 167
	NY11__in += MAS_in[1]

	NY11__mem0 = S.Task('NY11__mem0', length=1, delay_cost=1)
	S += NY11__mem0 >= 167
	NY11__mem0 += MM_MEM[0]

	NY11__mem1 = S.Task('NY11__mem1', length=1, delay_cost=1)
	S += NY11__mem1 >= 167
	NY11__mem1 += MM_MEM[1]

	DY10 = S.Task('DY10', length=11, delay_cost=1)
	S += DY10 >= 168
	DY10 += MM[0]

	NX_in = S.Task('NX_in', length=1, delay_cost=1)
	S += NX_in >= 168
	NX_in += MAS_in[0]

	NX_mem0 = S.Task('NX_mem0', length=1, delay_cost=1)
	S += NX_mem0 >= 168
	NX_mem0 += MM_MEM[0]

	NX_mem1 = S.Task('NX_mem1', length=1, delay_cost=1)
	S += NX_mem1 >= 168
	NX_mem1 += MM_MEM[1]

	NY11_ = S.Task('NY11_', length=3, delay_cost=1)
	S += NY11_ >= 168
	NY11_ += MAS[1]

	NX = S.Task('NX', length=3, delay_cost=1)
	S += NX >= 169
	NX += MAS[0]

	NY11_in = S.Task('NY11_in', length=1, delay_cost=1)
	S += NY11_in >= 170
	NY11_in += MM_in[0]

	NY11_mem0 = S.Task('NY11_mem0', length=1, delay_cost=1)
	S += NY11_mem0 >= 170
	NY11_mem0 += MAS_MEM[2]

	NY11_mem1 = S.Task('NY11_mem1', length=1, delay_cost=1)
	S += NY11_mem1 >= 170
	NY11_mem1 += MAIN_MEM_r[1]

	NY11 = S.Task('NY11', length=11, delay_cost=1)
	S += NY11 >= 171
	NY11 += MM[0]

	k3_0_Z16_in = S.Task('k3_0_Z16_in', length=1, delay_cost=1)
	S += k3_0_Z16_in >= 171
	k3_0_Z16_in += MM_in[0]

	k3_0_Z16_mem0 = S.Task('k3_0_Z16_mem0', length=1, delay_cost=1)
	S += k3_0_Z16_mem0 >= 171
	k3_0_Z16_mem0 += MAIN_MEM_r[0]

	k3_0_Z16_mem1 = S.Task('k3_0_Z16_mem1', length=1, delay_cost=1)
	S += k3_0_Z16_mem1 >= 171
	k3_0_Z16_mem1 += MM_MEM[1]

	k3_0_Z16 = S.Task('k3_0_Z16', length=11, delay_cost=1)
	S += k3_0_Z16 >= 172
	k3_0_Z16 += MM[0]

	DY11__in = S.Task('DY11__in', length=1, delay_cost=1)
	S += DY11__in >= 178
	DY11__in += MAS_in[1]

	DY11__mem0 = S.Task('DY11__mem0', length=1, delay_cost=1)
	S += DY11__mem0 >= 178
	DY11__mem0 += MM_MEM[0]

	DY11__mem1 = S.Task('DY11__mem1', length=1, delay_cost=1)
	S += DY11__mem1 >= 178
	DY11__mem1 += MM_MEM[1]

	DY11_ = S.Task('DY11_', length=3, delay_cost=1)
	S += DY11_ >= 179
	DY11_ += MAS[1]

	DY11_in = S.Task('DY11_in', length=1, delay_cost=1)
	S += DY11_in >= 181
	DY11_in += MM_in[0]

	DY11_mem0 = S.Task('DY11_mem0', length=1, delay_cost=1)
	S += DY11_mem0 >= 181
	DY11_mem0 += MAS_MEM[2]

	DY11_mem1 = S.Task('DY11_mem1', length=1, delay_cost=1)
	S += DY11_mem1 >= 181
	DY11_mem1 += MAIN_MEM_r[1]

	NY12__in = S.Task('NY12__in', length=1, delay_cost=1)
	S += NY12__in >= 181
	NY12__in += MAS_in[1]

	NY12__mem0 = S.Task('NY12__mem0', length=1, delay_cost=1)
	S += NY12__mem0 >= 181
	NY12__mem0 += MM_MEM[0]

	NY12__mem1 = S.Task('NY12__mem1', length=1, delay_cost=1)
	S += NY12__mem1 >= 181
	NY12__mem1 += MM_MEM[1]

	DY11 = S.Task('DY11', length=11, delay_cost=1)
	S += DY11 >= 182
	DY11 += MM[0]

	NY12_ = S.Task('NY12_', length=3, delay_cost=1)
	S += NY12_ >= 182
	NY12_ += MAS[1]

	NY12_in = S.Task('NY12_in', length=1, delay_cost=1)
	S += NY12_in >= 184
	NY12_in += MM_in[0]

	NY12_mem0 = S.Task('NY12_mem0', length=1, delay_cost=1)
	S += NY12_mem0 >= 184
	NY12_mem0 += MAS_MEM[2]

	NY12_mem1 = S.Task('NY12_mem1', length=1, delay_cost=1)
	S += NY12_mem1 >= 184
	NY12_mem1 += MAIN_MEM_r[1]

	NY12 = S.Task('NY12', length=11, delay_cost=1)
	S += NY12 >= 185
	NY12 += MM[0]

	DY12__in = S.Task('DY12__in', length=1, delay_cost=1)
	S += DY12__in >= 192
	DY12__in += MAS_in[1]

	DY12__mem0 = S.Task('DY12__mem0', length=1, delay_cost=1)
	S += DY12__mem0 >= 192
	DY12__mem0 += MM_MEM[0]

	DY12__mem1 = S.Task('DY12__mem1', length=1, delay_cost=1)
	S += DY12__mem1 >= 192
	DY12__mem1 += MM_MEM[1]

	DY12_ = S.Task('DY12_', length=3, delay_cost=1)
	S += DY12_ >= 193
	DY12_ += MAS[1]

	DY12_in = S.Task('DY12_in', length=1, delay_cost=1)
	S += DY12_in >= 195
	DY12_in += MM_in[0]

	DY12_mem0 = S.Task('DY12_mem0', length=1, delay_cost=1)
	S += DY12_mem0 >= 195
	DY12_mem0 += MAS_MEM[2]

	DY12_mem1 = S.Task('DY12_mem1', length=1, delay_cost=1)
	S += DY12_mem1 >= 195
	DY12_mem1 += MAIN_MEM_r[1]

	NY13__in = S.Task('NY13__in', length=1, delay_cost=1)
	S += NY13__in >= 195
	NY13__in += MAS_in[1]

	NY13__mem0 = S.Task('NY13__mem0', length=1, delay_cost=1)
	S += NY13__mem0 >= 195
	NY13__mem0 += MM_MEM[0]

	NY13__mem1 = S.Task('NY13__mem1', length=1, delay_cost=1)
	S += NY13__mem1 >= 195
	NY13__mem1 += MM_MEM[1]

	DY12 = S.Task('DY12', length=11, delay_cost=1)
	S += DY12 >= 196
	DY12 += MM[0]

	NY13_ = S.Task('NY13_', length=3, delay_cost=1)
	S += NY13_ >= 196
	NY13_ += MAS[1]

	NY13_in = S.Task('NY13_in', length=1, delay_cost=1)
	S += NY13_in >= 198
	NY13_in += MM_in[0]

	NY13_mem0 = S.Task('NY13_mem0', length=1, delay_cost=1)
	S += NY13_mem0 >= 198
	NY13_mem0 += MAS_MEM[2]

	NY13_mem1 = S.Task('NY13_mem1', length=1, delay_cost=1)
	S += NY13_mem1 >= 198
	NY13_mem1 += MAIN_MEM_r[1]

	NY13 = S.Task('NY13', length=11, delay_cost=1)
	S += NY13 >= 199
	NY13 += MM[0]

	DY13__in = S.Task('DY13__in', length=1, delay_cost=1)
	S += DY13__in >= 206
	DY13__in += MAS_in[1]

	DY13__mem0 = S.Task('DY13__mem0', length=1, delay_cost=1)
	S += DY13__mem0 >= 206
	DY13__mem0 += MM_MEM[0]

	DY13__mem1 = S.Task('DY13__mem1', length=1, delay_cost=1)
	S += DY13__mem1 >= 206
	DY13__mem1 += MM_MEM[1]

	DY13_ = S.Task('DY13_', length=3, delay_cost=1)
	S += DY13_ >= 207
	DY13_ += MAS[1]

	DY13_in = S.Task('DY13_in', length=1, delay_cost=1)
	S += DY13_in >= 209
	DY13_in += MM_in[0]

	DY13_mem0 = S.Task('DY13_mem0', length=1, delay_cost=1)
	S += DY13_mem0 >= 209
	DY13_mem0 += MAS_MEM[2]

	DY13_mem1 = S.Task('DY13_mem1', length=1, delay_cost=1)
	S += DY13_mem1 >= 209
	DY13_mem1 += MAIN_MEM_r[1]

	NY14__in = S.Task('NY14__in', length=1, delay_cost=1)
	S += NY14__in >= 209
	NY14__in += MAS_in[0]

	NY14__mem0 = S.Task('NY14__mem0', length=1, delay_cost=1)
	S += NY14__mem0 >= 209
	NY14__mem0 += MM_MEM[0]

	NY14__mem1 = S.Task('NY14__mem1', length=1, delay_cost=1)
	S += NY14__mem1 >= 209
	NY14__mem1 += MM_MEM[1]

	DY13 = S.Task('DY13', length=11, delay_cost=1)
	S += DY13 >= 210
	DY13 += MM[0]

	NY14_ = S.Task('NY14_', length=3, delay_cost=1)
	S += NY14_ >= 210
	NY14_ += MAS[0]

	NY14_in = S.Task('NY14_in', length=1, delay_cost=1)
	S += NY14_in >= 212
	NY14_in += MM_in[0]

	NY14_mem0 = S.Task('NY14_mem0', length=1, delay_cost=1)
	S += NY14_mem0 >= 212
	NY14_mem0 += MAS_MEM[0]

	NY14_mem1 = S.Task('NY14_mem1', length=1, delay_cost=1)
	S += NY14_mem1 >= 212
	NY14_mem1 += MAIN_MEM_r[1]

	NY14 = S.Task('NY14', length=11, delay_cost=1)
	S += NY14 >= 213
	NY14 += MM[0]

	DY14__in = S.Task('DY14__in', length=1, delay_cost=1)
	S += DY14__in >= 220
	DY14__in += MAS_in[1]

	DY14__mem0 = S.Task('DY14__mem0', length=1, delay_cost=1)
	S += DY14__mem0 >= 220
	DY14__mem0 += MM_MEM[0]

	DY14__mem1 = S.Task('DY14__mem1', length=1, delay_cost=1)
	S += DY14__mem1 >= 220
	DY14__mem1 += MM_MEM[1]

	DY14_ = S.Task('DY14_', length=3, delay_cost=1)
	S += DY14_ >= 221
	DY14_ += MAS[1]


	# new tasks
	NY15_ = S.Task('NY15_', length=3, delay_cost=1)
	NY15_ += alt(MAS)
	NY15__in = S.Task('NY15__in', length=1, delay_cost=1)
	NY15__in += alt(MAS_in)
	S += NY15__in*MAS_in[0]<=NY15_*MAS[0]

	S += NY15__in*MAS_in[1]<=NY15_*MAS[1]

	S += NY15__in*MAS_in[2]<=NY15_*MAS[2]

	NY15__mem0 = S.Task('NY15__mem0', length=1, delay_cost=1)
	NY15__mem0 += MM_MEM[0]
	S += 223 < NY15__mem0
	S += NY15__mem0 <= NY15_

	NY15__mem1 = S.Task('NY15__mem1', length=1, delay_cost=1)
	NY15__mem1 += MM_MEM[1]
	S += 172 < NY15__mem1
	S += NY15__mem1 <= NY15_

	DY14 = S.Task('DY14', length=11, delay_cost=1)
	DY14 += alt(MM)
	DY14_in = S.Task('DY14_in', length=1, delay_cost=1)
	DY14_in += alt(MM_in)
	S += DY14_in*MM_in[0]<=DY14*MM[0]
	DY14_mem0 = S.Task('DY14_mem0', length=1, delay_cost=1)
	DY14_mem0 += MAS_MEM[2]
	S += 223 < DY14_mem0
	S += DY14_mem0 <= DY14

	DY14_mem1 = S.Task('DY14_mem1', length=1, delay_cost=1)
	DY14_mem1 += MAIN_MEM_r[1]
	S += DY14_mem1 <= DY14

	NY = S.Task('NY', length=11, delay_cost=1)
	NY += alt(MM)
	NY_in = S.Task('NY_in', length=1, delay_cost=1)
	NY_in += alt(MM_in)
	S += NY_in*MM_in[0]<=NY*MM[0]
	NY_mem0 = S.Task('NY_mem0', length=1, delay_cost=1)
	NY_mem0 += alt(MAS_MEM)
	S += (NY15_*MAS[0])-1 < NY_mem0*MAS_MEM[0]
	S += (NY15_*MAS[1])-1 < NY_mem0*MAS_MEM[2]
	S += (NY15_*MAS[2])-1 < NY_mem0*MAS_MEM[4]
	S += NY_mem0 <= NY

	NY_mem1 = S.Task('NY_mem1', length=1, delay_cost=1)
	NY_mem1 += MAIN_MEM_r[1]
	S += NY_mem1 <= NY

	DY = S.Task('DY', length=3, delay_cost=1)
	DY += alt(MAS)
	DY_in = S.Task('DY_in', length=1, delay_cost=1)
	DY_in += alt(MAS_in)
	S += DY_in*MAS_in[0]<=DY*MAS[0]

	S += DY_in*MAS_in[1]<=DY*MAS[1]

	S += DY_in*MAS_in[2]<=DY*MAS[2]

	DY_mem0 = S.Task('DY_mem0', length=1, delay_cost=1)
	DY_mem0 += alt(MM_MEM)
	S += (DY14*MM[0])-1 < DY_mem0*MM_MEM[0]
	S += DY_mem0 <= DY

	DY_mem1 = S.Task('DY_mem1', length=1, delay_cost=1)
	DY_mem1 += MM_MEM[1]
	S += 182 < DY_mem1
	S += DY_mem1 <= DY

	Z_new = S.Task('Z_new', length=11, delay_cost=1)
	Z_new += alt(MM)
	Z_new_in = S.Task('Z_new_in', length=1, delay_cost=1)
	Z_new_in += alt(MM_in)
	S += Z_new_in*MM_in[0]<=Z_new*MM[0]
	S += 0<Z_new

	Z_new_w = S.Task('Z_new_w', length=1, delay_cost=1)
	Z_new_w += alt(MAIN_MEM_w)
	S += Z_new <= Z_new_w

	Z_new_mem0 = S.Task('Z_new_mem0', length=1, delay_cost=1)
	Z_new_mem0 += MAS_MEM[2]
	S += 168 < Z_new_mem0
	S += Z_new_mem0 <= Z_new

	Z_new_mem1 = S.Task('Z_new_mem1', length=1, delay_cost=1)
	Z_new_mem1 += alt(MAS_MEM)
	S += (DY*MAS[0])-1 < Z_new_mem1*MAS_MEM[1]
	S += (DY*MAS[1])-1 < Z_new_mem1*MAS_MEM[3]
	S += (DY*MAS[2])-1 < Z_new_mem1*MAS_MEM[5]
	S += Z_new_mem1 <= Z_new

	X_new = S.Task('X_new', length=11, delay_cost=1)
	X_new += alt(MM)
	X_new_in = S.Task('X_new_in', length=1, delay_cost=1)
	X_new_in += alt(MM_in)
	S += X_new_in*MM_in[0]<=X_new*MM[0]
	S += 0<X_new

	X_new_w = S.Task('X_new_w', length=1, delay_cost=1)
	X_new_w += alt(MAIN_MEM_w)
	S += X_new <= X_new_w

	X_new_mem0 = S.Task('X_new_mem0', length=1, delay_cost=1)
	X_new_mem0 += MAS_MEM[0]
	S += 171 < X_new_mem0
	S += X_new_mem0 <= X_new

	X_new_mem1 = S.Task('X_new_mem1', length=1, delay_cost=1)
	X_new_mem1 += alt(MAS_MEM)
	S += (DY*MAS[0])-1 < X_new_mem1*MAS_MEM[1]
	S += (DY*MAS[1])-1 < X_new_mem1*MAS_MEM[3]
	S += (DY*MAS[2])-1 < X_new_mem1*MAS_MEM[5]
	S += X_new_mem1 <= X_new

	Y_new = S.Task('Y_new', length=11, delay_cost=1)
	Y_new += alt(MM)
	Y_new_in = S.Task('Y_new_in', length=1, delay_cost=1)
	Y_new_in += alt(MM_in)
	S += Y_new_in*MM_in[0]<=Y_new*MM[0]
	S += 0<Y_new

	Y_new_w = S.Task('Y_new_w', length=1, delay_cost=1)
	Y_new_w += alt(MAIN_MEM_w)
	S += Y_new <= Y_new_w

	Y_new_mem0 = S.Task('Y_new_mem0', length=1, delay_cost=1)
	Y_new_mem0 += alt(MM_MEM)
	S += (NY*MM[0])-1 < Y_new_mem0*MM_MEM[0]
	S += Y_new_mem0 <= Y_new

	Y_new_mem1 = S.Task('Y_new_mem1', length=1, delay_cost=1)
	Y_new_mem1 += MAS_MEM[3]
	S += 168 < Y_new_mem1
	S += Y_new_mem1 <= Y_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM1_stage3MAS3/ISOGENY/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 4))

	return solution

