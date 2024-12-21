from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 112
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	S += Z_exp2_in >= 0
	Z_exp2_in += MM_in[0]

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	S += Z_exp3_mem1 >= 0
	Z_exp3_mem1 += MAIN_MEM_r[1]

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	S += k2_14_Z1_mem0 >= 0
	k2_14_Z1_mem0 += MAIN_MEM_r[0]

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	S += DX0_mem1 >= 1
	DX0_mem1 += MAIN_MEM_r[1]

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	S += DY0_mem0 >= 1
	DY0_mem0 += MAIN_MEM_r[0]

	Z_exp2 = S.Task('Z_exp2', length=6, delay_cost=1)
	S += Z_exp2 >= 1
	Z_exp2 += MM[0]

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	S += k0_10_Z1_in >= 1
	k0_10_Z1_in += MM_in[0]

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	S += NX0_in >= 2
	NX0_in += MM_in[0]

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	S += NY1_mem1 >= 2
	NY1_mem1 += MAIN_MEM_r[1]

	k0_10_Z1 = S.Task('k0_10_Z1', length=6, delay_cost=1)
	S += k0_10_Z1 >= 2
	k0_10_Z1 += MM[0]

	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	S += k2_12_Z3_mem0 >= 2
	k2_12_Z3_mem0 += MAIN_MEM_r[0]

	NX0 = S.Task('NX0', length=6, delay_cost=1)
	S += NX0 >= 3
	NX0 += MM[0]

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	S += NX0_mem1 >= 3
	NX0_mem1 += MAIN_MEM_r[1]

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	S += NY0_in >= 3
	NY0_in += MM_in[0]

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	S += NY0_mem0 >= 3
	NY0_mem0 += MAIN_MEM_r[0]

	NY0 = S.Task('NY0', length=6, delay_cost=1)
	S += NY0 >= 4
	NY0 += MM[0]

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	S += Z_exp4_mem1 >= 4
	Z_exp4_mem1 += MAIN_MEM_r[1]

	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	S += k2_13_Z2_mem0 >= 4
	k2_13_Z2_mem0 += MAIN_MEM_r[0]

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	S += k2_14_Z1_in >= 4
	k2_14_Z1_in += MM_in[0]

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	S += DX0_in >= 5
	DX0_in += MM_in[0]

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	S += NX1_mem1 >= 5
	NX1_mem1 += MAIN_MEM_r[1]

	k2_14_Z1 = S.Task('k2_14_Z1', length=6, delay_cost=1)
	S += k2_14_Z1 >= 5
	k2_14_Z1 += MM[0]

	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	S += k3_14_Z2_mem0 >= 5
	k3_14_Z2_mem0 += MAIN_MEM_r[0]

	DX0 = S.Task('DX0', length=6, delay_cost=1)
	S += DX0 >= 6
	DX0 += MM[0]

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	S += DY0_mem1 >= 6
	DY0_mem1 += MAIN_MEM_r[1]

	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	S += k1_9_Z2_in >= 6
	k1_9_Z2_in += MM_in[0]

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	S += k1_9_Z2_mem1 >= 6
	k1_9_Z2_mem1 += MM_MEM[1]

	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	S += k3_13_Z3_mem0 >= 6
	k3_13_Z3_mem0 += MAIN_MEM_r[0]

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	S += DX0_mem0 >= 7
	DX0_mem0 += MAIN_MEM_r[0]

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	S += NY0_mem1 >= 7
	NY0_mem1 += MAIN_MEM_r[1]

	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	S += Z_exp3_in >= 7
	Z_exp3_in += MM_in[0]

	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	S += Z_exp3_mem0 >= 7
	Z_exp3_mem0 += MM_MEM[0]

	k1_9_Z2 = S.Task('k1_9_Z2', length=6, delay_cost=1)
	S += k1_9_Z2 >= 7
	k1_9_Z2 += MM[0]

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	S += DY0_in >= 8
	DY0_in += MM_in[0]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	S += NX1__mem0 >= 8
	NX1__mem0 += MM_MEM[0]

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	S += NX1__mem1 >= 8
	NX1__mem1 += MM_MEM[1]

	Z_exp3 = S.Task('Z_exp3', length=6, delay_cost=1)
	S += Z_exp3 >= 8
	Z_exp3 += MM[0]

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	S += k0_10_Z1_mem1 >= 8
	k0_10_Z1_mem1 += MAIN_MEM_r[1]

	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	S += k0_9_Z2_mem0 >= 8
	k0_9_Z2_mem0 += MAIN_MEM_r[0]

	DY0 = S.Task('DY0', length=6, delay_cost=1)
	S += DY0 >= 9
	DY0 += MM[0]

	NX1_ = S.Task('NX1_', length=1, delay_cost=1)
	S += NX1_ >= 9
	NX1_ += MAS[0]

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	S += Z_exp2_mem0 >= 9
	Z_exp2_mem0 += MAIN_MEM_r[0]

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	S += k2_14_Z1_mem1 >= 9
	k2_14_Z1_mem1 += MAIN_MEM_r[1]

	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	S += k3_14_Z2_in >= 9
	k3_14_Z2_in += MM_in[0]

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	S += k3_14_Z2_mem1 >= 9
	k3_14_Z2_mem1 += MM_MEM[1]

	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	S += NX1_in >= 10
	NX1_in += MM_in[0]

	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	S += NX1_mem0 >= 10
	NX1_mem0 += MAS_MEM[0]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	S += NY1__mem0 >= 10
	NY1__mem0 += MM_MEM[0]

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	S += NY1__mem1 >= 10
	NY1__mem1 += MM_MEM[1]

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	S += k0_10_Z1_mem0 >= 10
	k0_10_Z1_mem0 += MAIN_MEM_r[0]

	k3_14_Z2 = S.Task('k3_14_Z2', length=6, delay_cost=1)
	S += k3_14_Z2 >= 10
	k3_14_Z2 += MM[0]

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	S += NX0_mem0 >= 11
	NX0_mem0 += MAIN_MEM_r[0]

	NX1 = S.Task('NX1', length=6, delay_cost=1)
	S += NX1 >= 11
	NX1 += MM[0]

	NY1_ = S.Task('NY1_', length=1, delay_cost=1)
	S += NY1_ >= 11
	NY1_ += MAS[1]

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

	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	S += NY1_in >= 12
	NY1_in += MM_in[0]

	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	S += NY1_mem0 >= 12
	NY1_mem0 += MAS_MEM[2]

	k0_9_Z2 = S.Task('k0_9_Z2', length=6, delay_cost=1)
	S += k0_9_Z2 >= 12
	k0_9_Z2 += MM[0]

	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	S += k1_9_Z2_mem0 >= 12
	k1_9_Z2_mem0 += MAIN_MEM_r[0]

	DX1_ = S.Task('DX1_', length=1, delay_cost=1)
	S += DX1_ >= 13
	DX1_ += MAS[0]

	NY1 = S.Task('NY1', length=6, delay_cost=1)
	S += NY1 >= 13
	NY1 += MM[0]

	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	S += k1_8_Z3_mem0 >= 13
	k1_8_Z3_mem0 += MAIN_MEM_r[0]

	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	S += k2_13_Z2_in >= 13
	k2_13_Z2_in += MM_in[0]

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	S += k2_13_Z2_mem1 >= 13
	k2_13_Z2_mem1 += MM_MEM[1]

	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	S += k0_8_Z3_mem0 >= 14
	k0_8_Z3_mem0 += MAIN_MEM_r[0]

	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	S += k2_12_Z3_in >= 14
	k2_12_Z3_in += MM_in[0]

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	S += k2_12_Z3_mem1 >= 14
	k2_12_Z3_mem1 += MM_MEM[1]

	k2_13_Z2 = S.Task('k2_13_Z2', length=6, delay_cost=1)
	S += k2_13_Z2 >= 14
	k2_13_Z2 += MM[0]

	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	S += k0_8_Z3_in >= 15
	k0_8_Z3_in += MM_in[0]

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	S += k0_8_Z3_mem1 >= 15
	k0_8_Z3_mem1 += MM_MEM[1]

	k2_12_Z3 = S.Task('k2_12_Z3', length=6, delay_cost=1)
	S += k2_12_Z3 >= 15
	k2_12_Z3 += MM[0]

	k0_8_Z3 = S.Task('k0_8_Z3', length=6, delay_cost=1)
	S += k0_8_Z3 >= 16
	k0_8_Z3 += MM[0]

	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	S += k1_8_Z3_in >= 16
	k1_8_Z3_in += MM_in[0]

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	S += k1_8_Z3_mem1 >= 16
	k1_8_Z3_mem1 += MM_MEM[1]

	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	S += Z_exp4_in >= 17
	Z_exp4_in += MM_in[0]

	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	S += Z_exp4_mem0 >= 17
	Z_exp4_mem0 += MM_MEM[0]

	k1_8_Z3 = S.Task('k1_8_Z3', length=6, delay_cost=1)
	S += k1_8_Z3 >= 17
	k1_8_Z3 += MM[0]

	Z_exp4 = S.Task('Z_exp4', length=6, delay_cost=1)
	S += Z_exp4 >= 18
	Z_exp4 += MM[0]

	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	S += k3_13_Z3_in >= 18
	k3_13_Z3_in += MM_in[0]

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	S += k3_13_Z3_mem1 >= 18
	k3_13_Z3_mem1 += MM_MEM[1]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	S += DY1__mem0 >= 19
	DY1__mem0 += MM_MEM[0]

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	S += DY1__mem1 >= 19
	DY1__mem1 += MM_MEM[1]

	k3_13_Z3 = S.Task('k3_13_Z3', length=6, delay_cost=1)
	S += k3_13_Z3 >= 19
	k3_13_Z3 += MM[0]

	DY1_ = S.Task('DY1_', length=1, delay_cost=1)
	S += DY1_ >= 20
	DY1_ += MAS[0]


	# new tasks
	Z_exp5_in = S.Task('Z_exp5_in', length=1, delay_cost=1)
	Z_exp5_in += alt(MM_in)
	Z_exp5 = S.Task('Z_exp5', length=6, delay_cost=1)
	Z_exp5 += alt(MM)
	S += Z_exp5>=Z_exp5_in

	Z_exp5_mem0 = S.Task('Z_exp5_mem0', length=1, delay_cost=1)
	Z_exp5_mem0 += MM_MEM[0]
	S += 23 < Z_exp5_mem0
	S += Z_exp5_mem0 <= Z_exp5

	Z_exp5_mem1 = S.Task('Z_exp5_mem1', length=1, delay_cost=1)
	Z_exp5_mem1 += MAIN_MEM_r[1]
	NX2_ = S.Task('NX2_', length=1, delay_cost=1)
	NX2_ += alt(MAS)

	NX2__mem0 = S.Task('NX2__mem0', length=1, delay_cost=1)
	NX2__mem0 += MM_MEM[0]
	S += 16 < NX2__mem0
	S += NX2__mem0 <= NX2_

	NX2__mem1 = S.Task('NX2__mem1', length=1, delay_cost=1)
	NX2__mem1 += MM_MEM[1]
	S += 17 < NX2__mem1
	S += NX2__mem1 <= NX2_

	k0_7_Z4_in = S.Task('k0_7_Z4_in', length=1, delay_cost=1)
	k0_7_Z4_in += alt(MM_in)
	k0_7_Z4 = S.Task('k0_7_Z4', length=6, delay_cost=1)
	k0_7_Z4 += alt(MM)
	S += k0_7_Z4>=k0_7_Z4_in

	k0_7_Z4_mem0 = S.Task('k0_7_Z4_mem0', length=1, delay_cost=1)
	k0_7_Z4_mem0 += MAIN_MEM_r[0]
	k0_7_Z4_mem1 = S.Task('k0_7_Z4_mem1', length=1, delay_cost=1)
	k0_7_Z4_mem1 += MM_MEM[1]
	S += 23 < k0_7_Z4_mem1
	S += k0_7_Z4_mem1 <= k0_7_Z4

	DX1_in = S.Task('DX1_in', length=1, delay_cost=1)
	DX1_in += alt(MM_in)
	DX1 = S.Task('DX1', length=6, delay_cost=1)
	DX1 += alt(MM)
	S += DX1>=DX1_in

	DX1_mem0 = S.Task('DX1_mem0', length=1, delay_cost=1)
	DX1_mem0 += MAS_MEM[0]
	S += 13 < DX1_mem0
	S += DX1_mem0 <= DX1

	DX1_mem1 = S.Task('DX1_mem1', length=1, delay_cost=1)
	DX1_mem1 += MAIN_MEM_r[1]
	k1_7_Z4_in = S.Task('k1_7_Z4_in', length=1, delay_cost=1)
	k1_7_Z4_in += alt(MM_in)
	k1_7_Z4 = S.Task('k1_7_Z4', length=6, delay_cost=1)
	k1_7_Z4 += alt(MM)
	S += k1_7_Z4>=k1_7_Z4_in

	k1_7_Z4_mem0 = S.Task('k1_7_Z4_mem0', length=1, delay_cost=1)
	k1_7_Z4_mem0 += MAIN_MEM_r[0]
	k1_7_Z4_mem1 = S.Task('k1_7_Z4_mem1', length=1, delay_cost=1)
	k1_7_Z4_mem1 += MM_MEM[1]
	S += 23 < k1_7_Z4_mem1
	S += k1_7_Z4_mem1 <= k1_7_Z4

	NY2_ = S.Task('NY2_', length=1, delay_cost=1)
	NY2_ += alt(MAS)

	NY2__mem0 = S.Task('NY2__mem0', length=1, delay_cost=1)
	NY2__mem0 += MM_MEM[0]
	S += 18 < NY2__mem0
	S += NY2__mem0 <= NY2_

	NY2__mem1 = S.Task('NY2__mem1', length=1, delay_cost=1)
	NY2__mem1 += MM_MEM[1]
	S += 19 < NY2__mem1
	S += NY2__mem1 <= NY2_

	k2_11_Z4_in = S.Task('k2_11_Z4_in', length=1, delay_cost=1)
	k2_11_Z4_in += alt(MM_in)
	k2_11_Z4 = S.Task('k2_11_Z4', length=6, delay_cost=1)
	k2_11_Z4 += alt(MM)
	S += k2_11_Z4>=k2_11_Z4_in

	k2_11_Z4_mem0 = S.Task('k2_11_Z4_mem0', length=1, delay_cost=1)
	k2_11_Z4_mem0 += MAIN_MEM_r[0]
	k2_11_Z4_mem1 = S.Task('k2_11_Z4_mem1', length=1, delay_cost=1)
	k2_11_Z4_mem1 += MM_MEM[1]
	S += 23 < k2_11_Z4_mem1
	S += k2_11_Z4_mem1 <= k2_11_Z4

	DY1_in = S.Task('DY1_in', length=1, delay_cost=1)
	DY1_in += alt(MM_in)
	DY1 = S.Task('DY1', length=6, delay_cost=1)
	DY1 += alt(MM)
	S += DY1>=DY1_in

	DY1_mem0 = S.Task('DY1_mem0', length=1, delay_cost=1)
	DY1_mem0 += MAS_MEM[0]
	S += 20 < DY1_mem0
	S += DY1_mem0 <= DY1

	DY1_mem1 = S.Task('DY1_mem1', length=1, delay_cost=1)
	DY1_mem1 += MAIN_MEM_r[1]
	k3_12_Z4_in = S.Task('k3_12_Z4_in', length=1, delay_cost=1)
	k3_12_Z4_in += alt(MM_in)
	k3_12_Z4 = S.Task('k3_12_Z4', length=6, delay_cost=1)
	k3_12_Z4 += alt(MM)
	S += k3_12_Z4>=k3_12_Z4_in

	k3_12_Z4_mem0 = S.Task('k3_12_Z4_mem0', length=1, delay_cost=1)
	k3_12_Z4_mem0 += MAIN_MEM_r[0]
	k3_12_Z4_mem1 = S.Task('k3_12_Z4_mem1', length=1, delay_cost=1)
	k3_12_Z4_mem1 += MM_MEM[1]
	S += 23 < k3_12_Z4_mem1
	S += k3_12_Z4_mem1 <= k3_12_Z4

	Z_exp6_in = S.Task('Z_exp6_in', length=1, delay_cost=1)
	Z_exp6_in += alt(MM_in)
	Z_exp6 = S.Task('Z_exp6', length=6, delay_cost=1)
	Z_exp6 += alt(MM)
	S += Z_exp6>=Z_exp6_in

	Z_exp6_mem0 = S.Task('Z_exp6_mem0', length=1, delay_cost=1)
	Z_exp6_mem0 += alt(MM_MEM)
	S += (Z_exp5*MM[0])-1 < Z_exp6_mem0*MM_MEM[0]
	S += Z_exp6_mem0 <= Z_exp6

	Z_exp6_mem1 = S.Task('Z_exp6_mem1', length=1, delay_cost=1)
	Z_exp6_mem1 += MAIN_MEM_r[1]
	NX2_in = S.Task('NX2_in', length=1, delay_cost=1)
	NX2_in += alt(MM_in)
	NX2 = S.Task('NX2', length=6, delay_cost=1)
	NX2 += alt(MM)
	S += NX2>=NX2_in

	NX2_mem0 = S.Task('NX2_mem0', length=1, delay_cost=1)
	NX2_mem0 += alt(MAS_MEM)
	S += (NX2_*MAS[0])-1 < NX2_mem0*MAS_MEM[0]
	S += (NX2_*MAS[1])-1 < NX2_mem0*MAS_MEM[2]
	S += (NX2_*MAS[2])-1 < NX2_mem0*MAS_MEM[4]
	S += (NX2_*MAS[3])-1 < NX2_mem0*MAS_MEM[6]
	S += NX2_mem0 <= NX2

	NX2_mem1 = S.Task('NX2_mem1', length=1, delay_cost=1)
	NX2_mem1 += MAIN_MEM_r[1]
	k0_6_Z5_in = S.Task('k0_6_Z5_in', length=1, delay_cost=1)
	k0_6_Z5_in += alt(MM_in)
	k0_6_Z5 = S.Task('k0_6_Z5', length=6, delay_cost=1)
	k0_6_Z5 += alt(MM)
	S += k0_6_Z5>=k0_6_Z5_in

	k0_6_Z5_mem0 = S.Task('k0_6_Z5_mem0', length=1, delay_cost=1)
	k0_6_Z5_mem0 += MAIN_MEM_r[0]
	k0_6_Z5_mem1 = S.Task('k0_6_Z5_mem1', length=1, delay_cost=1)
	k0_6_Z5_mem1 += alt(MM_MEM)
	S += (Z_exp5*MM[0])-1 < k0_6_Z5_mem1*MM_MEM[1]
	S += k0_6_Z5_mem1 <= k0_6_Z5

	DX2_ = S.Task('DX2_', length=1, delay_cost=1)
	DX2_ += alt(MAS)

	DX2__mem0 = S.Task('DX2__mem0', length=1, delay_cost=1)
	DX2__mem0 += alt(MM_MEM)
	S += (DX1*MM[0])-1 < DX2__mem0*MM_MEM[0]
	S += DX2__mem0 <= DX2_

	DX2__mem1 = S.Task('DX2__mem1', length=1, delay_cost=1)
	DX2__mem1 += MM_MEM[1]
	S += 22 < DX2__mem1
	S += DX2__mem1 <= DX2_

	k1_6_Z5_in = S.Task('k1_6_Z5_in', length=1, delay_cost=1)
	k1_6_Z5_in += alt(MM_in)
	k1_6_Z5 = S.Task('k1_6_Z5', length=6, delay_cost=1)
	k1_6_Z5 += alt(MM)
	S += k1_6_Z5>=k1_6_Z5_in

	k1_6_Z5_mem0 = S.Task('k1_6_Z5_mem0', length=1, delay_cost=1)
	k1_6_Z5_mem0 += MAIN_MEM_r[0]
	k1_6_Z5_mem1 = S.Task('k1_6_Z5_mem1', length=1, delay_cost=1)
	k1_6_Z5_mem1 += alt(MM_MEM)
	S += (Z_exp5*MM[0])-1 < k1_6_Z5_mem1*MM_MEM[1]
	S += k1_6_Z5_mem1 <= k1_6_Z5

	NY2_in = S.Task('NY2_in', length=1, delay_cost=1)
	NY2_in += alt(MM_in)
	NY2 = S.Task('NY2', length=6, delay_cost=1)
	NY2 += alt(MM)
	S += NY2>=NY2_in

	NY2_mem0 = S.Task('NY2_mem0', length=1, delay_cost=1)
	NY2_mem0 += alt(MAS_MEM)
	S += (NY2_*MAS[0])-1 < NY2_mem0*MAS_MEM[0]
	S += (NY2_*MAS[1])-1 < NY2_mem0*MAS_MEM[2]
	S += (NY2_*MAS[2])-1 < NY2_mem0*MAS_MEM[4]
	S += (NY2_*MAS[3])-1 < NY2_mem0*MAS_MEM[6]
	S += NY2_mem0 <= NY2

	NY2_mem1 = S.Task('NY2_mem1', length=1, delay_cost=1)
	NY2_mem1 += MAIN_MEM_r[1]
	k2_10_Z5_in = S.Task('k2_10_Z5_in', length=1, delay_cost=1)
	k2_10_Z5_in += alt(MM_in)
	k2_10_Z5 = S.Task('k2_10_Z5', length=6, delay_cost=1)
	k2_10_Z5 += alt(MM)
	S += k2_10_Z5>=k2_10_Z5_in

	k2_10_Z5_mem0 = S.Task('k2_10_Z5_mem0', length=1, delay_cost=1)
	k2_10_Z5_mem0 += MAIN_MEM_r[0]
	k2_10_Z5_mem1 = S.Task('k2_10_Z5_mem1', length=1, delay_cost=1)
	k2_10_Z5_mem1 += alt(MM_MEM)
	S += (Z_exp5*MM[0])-1 < k2_10_Z5_mem1*MM_MEM[1]
	S += k2_10_Z5_mem1 <= k2_10_Z5

	DY2_ = S.Task('DY2_', length=1, delay_cost=1)
	DY2_ += alt(MAS)

	DY2__mem0 = S.Task('DY2__mem0', length=1, delay_cost=1)
	DY2__mem0 += alt(MM_MEM)
	S += (DY1*MM[0])-1 < DY2__mem0*MM_MEM[0]
	S += DY2__mem0 <= DY2_

	DY2__mem1 = S.Task('DY2__mem1', length=1, delay_cost=1)
	DY2__mem1 += MM_MEM[1]
	S += 24 < DY2__mem1
	S += DY2__mem1 <= DY2_

	k3_11_Z5_in = S.Task('k3_11_Z5_in', length=1, delay_cost=1)
	k3_11_Z5_in += alt(MM_in)
	k3_11_Z5 = S.Task('k3_11_Z5', length=6, delay_cost=1)
	k3_11_Z5 += alt(MM)
	S += k3_11_Z5>=k3_11_Z5_in

	k3_11_Z5_mem0 = S.Task('k3_11_Z5_mem0', length=1, delay_cost=1)
	k3_11_Z5_mem0 += MAIN_MEM_r[0]
	k3_11_Z5_mem1 = S.Task('k3_11_Z5_mem1', length=1, delay_cost=1)
	k3_11_Z5_mem1 += alt(MM_MEM)
	S += (Z_exp5*MM[0])-1 < k3_11_Z5_mem1*MM_MEM[1]
	S += k3_11_Z5_mem1 <= k3_11_Z5

	Z_exp7_in = S.Task('Z_exp7_in', length=1, delay_cost=1)
	Z_exp7_in += alt(MM_in)
	Z_exp7 = S.Task('Z_exp7', length=6, delay_cost=1)
	Z_exp7 += alt(MM)
	S += Z_exp7>=Z_exp7_in

	Z_exp7_mem0 = S.Task('Z_exp7_mem0', length=1, delay_cost=1)
	Z_exp7_mem0 += alt(MM_MEM)
	S += (Z_exp6*MM[0])-1 < Z_exp7_mem0*MM_MEM[0]
	S += Z_exp7_mem0 <= Z_exp7

	Z_exp7_mem1 = S.Task('Z_exp7_mem1', length=1, delay_cost=1)
	Z_exp7_mem1 += MAIN_MEM_r[1]
	NX3_ = S.Task('NX3_', length=1, delay_cost=1)
	NX3_ += alt(MAS)

	NX3__mem0 = S.Task('NX3__mem0', length=1, delay_cost=1)
	NX3__mem0 += alt(MM_MEM)
	S += (NX2*MM[0])-1 < NX3__mem0*MM_MEM[0]
	S += NX3__mem0 <= NX3_

	NX3__mem1 = S.Task('NX3__mem1', length=1, delay_cost=1)
	NX3__mem1 += MM_MEM[1]
	S += 21 < NX3__mem1
	S += NX3__mem1 <= NX3_

	k0_5_Z6_in = S.Task('k0_5_Z6_in', length=1, delay_cost=1)
	k0_5_Z6_in += alt(MM_in)
	k0_5_Z6 = S.Task('k0_5_Z6', length=6, delay_cost=1)
	k0_5_Z6 += alt(MM)
	S += k0_5_Z6>=k0_5_Z6_in

	k0_5_Z6_mem0 = S.Task('k0_5_Z6_mem0', length=1, delay_cost=1)
	k0_5_Z6_mem0 += MAIN_MEM_r[0]
	k0_5_Z6_mem1 = S.Task('k0_5_Z6_mem1', length=1, delay_cost=1)
	k0_5_Z6_mem1 += alt(MM_MEM)
	S += (Z_exp6*MM[0])-1 < k0_5_Z6_mem1*MM_MEM[1]
	S += k0_5_Z6_mem1 <= k0_5_Z6

	DX2_in = S.Task('DX2_in', length=1, delay_cost=1)
	DX2_in += alt(MM_in)
	DX2 = S.Task('DX2', length=6, delay_cost=1)
	DX2 += alt(MM)
	S += DX2>=DX2_in

	DX2_mem0 = S.Task('DX2_mem0', length=1, delay_cost=1)
	DX2_mem0 += alt(MAS_MEM)
	S += (DX2_*MAS[0])-1 < DX2_mem0*MAS_MEM[0]
	S += (DX2_*MAS[1])-1 < DX2_mem0*MAS_MEM[2]
	S += (DX2_*MAS[2])-1 < DX2_mem0*MAS_MEM[4]
	S += (DX2_*MAS[3])-1 < DX2_mem0*MAS_MEM[6]
	S += DX2_mem0 <= DX2

	DX2_mem1 = S.Task('DX2_mem1', length=1, delay_cost=1)
	DX2_mem1 += MAIN_MEM_r[1]
	k1_5_Z6_in = S.Task('k1_5_Z6_in', length=1, delay_cost=1)
	k1_5_Z6_in += alt(MM_in)
	k1_5_Z6 = S.Task('k1_5_Z6', length=6, delay_cost=1)
	k1_5_Z6 += alt(MM)
	S += k1_5_Z6>=k1_5_Z6_in

	k1_5_Z6_mem0 = S.Task('k1_5_Z6_mem0', length=1, delay_cost=1)
	k1_5_Z6_mem0 += MAIN_MEM_r[0]
	k1_5_Z6_mem1 = S.Task('k1_5_Z6_mem1', length=1, delay_cost=1)
	k1_5_Z6_mem1 += alt(MM_MEM)
	S += (Z_exp6*MM[0])-1 < k1_5_Z6_mem1*MM_MEM[1]
	S += k1_5_Z6_mem1 <= k1_5_Z6

	NY3_ = S.Task('NY3_', length=1, delay_cost=1)
	NY3_ += alt(MAS)

	NY3__mem0 = S.Task('NY3__mem0', length=1, delay_cost=1)
	NY3__mem0 += alt(MM_MEM)
	S += (NY2*MM[0])-1 < NY3__mem0*MM_MEM[0]
	S += NY3__mem0 <= NY3_

	NY3__mem1 = S.Task('NY3__mem1', length=1, delay_cost=1)
	NY3__mem1 += MM_MEM[1]
	S += 20 < NY3__mem1
	S += NY3__mem1 <= NY3_

	k2_9_Z6_in = S.Task('k2_9_Z6_in', length=1, delay_cost=1)
	k2_9_Z6_in += alt(MM_in)
	k2_9_Z6 = S.Task('k2_9_Z6', length=6, delay_cost=1)
	k2_9_Z6 += alt(MM)
	S += k2_9_Z6>=k2_9_Z6_in

	k2_9_Z6_mem0 = S.Task('k2_9_Z6_mem0', length=1, delay_cost=1)
	k2_9_Z6_mem0 += MAIN_MEM_r[0]
	k2_9_Z6_mem1 = S.Task('k2_9_Z6_mem1', length=1, delay_cost=1)
	k2_9_Z6_mem1 += alt(MM_MEM)
	S += (Z_exp6*MM[0])-1 < k2_9_Z6_mem1*MM_MEM[1]
	S += k2_9_Z6_mem1 <= k2_9_Z6

	DY2_in = S.Task('DY2_in', length=1, delay_cost=1)
	DY2_in += alt(MM_in)
	DY2 = S.Task('DY2', length=6, delay_cost=1)
	DY2 += alt(MM)
	S += DY2>=DY2_in

	DY2_mem0 = S.Task('DY2_mem0', length=1, delay_cost=1)
	DY2_mem0 += alt(MAS_MEM)
	S += (DY2_*MAS[0])-1 < DY2_mem0*MAS_MEM[0]
	S += (DY2_*MAS[1])-1 < DY2_mem0*MAS_MEM[2]
	S += (DY2_*MAS[2])-1 < DY2_mem0*MAS_MEM[4]
	S += (DY2_*MAS[3])-1 < DY2_mem0*MAS_MEM[6]
	S += DY2_mem0 <= DY2

	DY2_mem1 = S.Task('DY2_mem1', length=1, delay_cost=1)
	DY2_mem1 += MAIN_MEM_r[1]
	k3_10_Z6_in = S.Task('k3_10_Z6_in', length=1, delay_cost=1)
	k3_10_Z6_in += alt(MM_in)
	k3_10_Z6 = S.Task('k3_10_Z6', length=6, delay_cost=1)
	k3_10_Z6 += alt(MM)
	S += k3_10_Z6>=k3_10_Z6_in

	k3_10_Z6_mem0 = S.Task('k3_10_Z6_mem0', length=1, delay_cost=1)
	k3_10_Z6_mem0 += MAIN_MEM_r[0]
	k3_10_Z6_mem1 = S.Task('k3_10_Z6_mem1', length=1, delay_cost=1)
	k3_10_Z6_mem1 += alt(MM_MEM)
	S += (Z_exp6*MM[0])-1 < k3_10_Z6_mem1*MM_MEM[1]
	S += k3_10_Z6_mem1 <= k3_10_Z6

	Z_exp8_in = S.Task('Z_exp8_in', length=1, delay_cost=1)
	Z_exp8_in += alt(MM_in)
	Z_exp8 = S.Task('Z_exp8', length=6, delay_cost=1)
	Z_exp8 += alt(MM)
	S += Z_exp8>=Z_exp8_in

	Z_exp8_mem0 = S.Task('Z_exp8_mem0', length=1, delay_cost=1)
	Z_exp8_mem0 += alt(MM_MEM)
	S += (Z_exp7*MM[0])-1 < Z_exp8_mem0*MM_MEM[0]
	S += Z_exp8_mem0 <= Z_exp8

	Z_exp8_mem1 = S.Task('Z_exp8_mem1', length=1, delay_cost=1)
	Z_exp8_mem1 += MAIN_MEM_r[1]
	NX3_in = S.Task('NX3_in', length=1, delay_cost=1)
	NX3_in += alt(MM_in)
	NX3 = S.Task('NX3', length=6, delay_cost=1)
	NX3 += alt(MM)
	S += NX3>=NX3_in

	NX3_mem0 = S.Task('NX3_mem0', length=1, delay_cost=1)
	NX3_mem0 += alt(MAS_MEM)
	S += (NX3_*MAS[0])-1 < NX3_mem0*MAS_MEM[0]
	S += (NX3_*MAS[1])-1 < NX3_mem0*MAS_MEM[2]
	S += (NX3_*MAS[2])-1 < NX3_mem0*MAS_MEM[4]
	S += (NX3_*MAS[3])-1 < NX3_mem0*MAS_MEM[6]
	S += NX3_mem0 <= NX3

	NX3_mem1 = S.Task('NX3_mem1', length=1, delay_cost=1)
	NX3_mem1 += MAIN_MEM_r[1]
	k0_4_Z7_in = S.Task('k0_4_Z7_in', length=1, delay_cost=1)
	k0_4_Z7_in += alt(MM_in)
	k0_4_Z7 = S.Task('k0_4_Z7', length=6, delay_cost=1)
	k0_4_Z7 += alt(MM)
	S += k0_4_Z7>=k0_4_Z7_in

	k0_4_Z7_mem0 = S.Task('k0_4_Z7_mem0', length=1, delay_cost=1)
	k0_4_Z7_mem0 += MAIN_MEM_r[0]
	k0_4_Z7_mem1 = S.Task('k0_4_Z7_mem1', length=1, delay_cost=1)
	k0_4_Z7_mem1 += alt(MM_MEM)
	S += (Z_exp7*MM[0])-1 < k0_4_Z7_mem1*MM_MEM[1]
	S += k0_4_Z7_mem1 <= k0_4_Z7

	DX3_ = S.Task('DX3_', length=1, delay_cost=1)
	DX3_ += alt(MAS)

	DX3__mem0 = S.Task('DX3__mem0', length=1, delay_cost=1)
	DX3__mem0 += alt(MM_MEM)
	S += (DX2*MM[0])-1 < DX3__mem0*MM_MEM[0]
	S += DX3__mem0 <= DX3_

	DX3__mem1 = S.Task('DX3__mem1', length=1, delay_cost=1)
	DX3__mem1 += alt(MM_MEM)
	S += (k1_7_Z4*MM[0])-1 < DX3__mem1*MM_MEM[1]
	S += DX3__mem1 <= DX3_

	k1_4_Z7_in = S.Task('k1_4_Z7_in', length=1, delay_cost=1)
	k1_4_Z7_in += alt(MM_in)
	k1_4_Z7 = S.Task('k1_4_Z7', length=6, delay_cost=1)
	k1_4_Z7 += alt(MM)
	S += k1_4_Z7>=k1_4_Z7_in

	k1_4_Z7_mem0 = S.Task('k1_4_Z7_mem0', length=1, delay_cost=1)
	k1_4_Z7_mem0 += MAIN_MEM_r[0]
	k1_4_Z7_mem1 = S.Task('k1_4_Z7_mem1', length=1, delay_cost=1)
	k1_4_Z7_mem1 += alt(MM_MEM)
	S += (Z_exp7*MM[0])-1 < k1_4_Z7_mem1*MM_MEM[1]
	S += k1_4_Z7_mem1 <= k1_4_Z7

	NY3_in = S.Task('NY3_in', length=1, delay_cost=1)
	NY3_in += alt(MM_in)
	NY3 = S.Task('NY3', length=6, delay_cost=1)
	NY3 += alt(MM)
	S += NY3>=NY3_in

	NY3_mem0 = S.Task('NY3_mem0', length=1, delay_cost=1)
	NY3_mem0 += alt(MAS_MEM)
	S += (NY3_*MAS[0])-1 < NY3_mem0*MAS_MEM[0]
	S += (NY3_*MAS[1])-1 < NY3_mem0*MAS_MEM[2]
	S += (NY3_*MAS[2])-1 < NY3_mem0*MAS_MEM[4]
	S += (NY3_*MAS[3])-1 < NY3_mem0*MAS_MEM[6]
	S += NY3_mem0 <= NY3

	NY3_mem1 = S.Task('NY3_mem1', length=1, delay_cost=1)
	NY3_mem1 += MAIN_MEM_r[1]
	k2_8_Z7_in = S.Task('k2_8_Z7_in', length=1, delay_cost=1)
	k2_8_Z7_in += alt(MM_in)
	k2_8_Z7 = S.Task('k2_8_Z7', length=6, delay_cost=1)
	k2_8_Z7 += alt(MM)
	S += k2_8_Z7>=k2_8_Z7_in

	k2_8_Z7_mem0 = S.Task('k2_8_Z7_mem0', length=1, delay_cost=1)
	k2_8_Z7_mem0 += MAIN_MEM_r[0]
	k2_8_Z7_mem1 = S.Task('k2_8_Z7_mem1', length=1, delay_cost=1)
	k2_8_Z7_mem1 += alt(MM_MEM)
	S += (Z_exp7*MM[0])-1 < k2_8_Z7_mem1*MM_MEM[1]
	S += k2_8_Z7_mem1 <= k2_8_Z7

	DY3_ = S.Task('DY3_', length=1, delay_cost=1)
	DY3_ += alt(MAS)

	DY3__mem0 = S.Task('DY3__mem0', length=1, delay_cost=1)
	DY3__mem0 += alt(MM_MEM)
	S += (DY2*MM[0])-1 < DY3__mem0*MM_MEM[0]
	S += DY3__mem0 <= DY3_

	DY3__mem1 = S.Task('DY3__mem1', length=1, delay_cost=1)
	DY3__mem1 += alt(MM_MEM)
	S += (k3_12_Z4*MM[0])-1 < DY3__mem1*MM_MEM[1]
	S += DY3__mem1 <= DY3_

	k3_9_Z7_in = S.Task('k3_9_Z7_in', length=1, delay_cost=1)
	k3_9_Z7_in += alt(MM_in)
	k3_9_Z7 = S.Task('k3_9_Z7', length=6, delay_cost=1)
	k3_9_Z7 += alt(MM)
	S += k3_9_Z7>=k3_9_Z7_in

	k3_9_Z7_mem0 = S.Task('k3_9_Z7_mem0', length=1, delay_cost=1)
	k3_9_Z7_mem0 += MAIN_MEM_r[0]
	k3_9_Z7_mem1 = S.Task('k3_9_Z7_mem1', length=1, delay_cost=1)
	k3_9_Z7_mem1 += alt(MM_MEM)
	S += (Z_exp7*MM[0])-1 < k3_9_Z7_mem1*MM_MEM[1]
	S += k3_9_Z7_mem1 <= k3_9_Z7

	Z_exp9_in = S.Task('Z_exp9_in', length=1, delay_cost=1)
	Z_exp9_in += alt(MM_in)
	Z_exp9 = S.Task('Z_exp9', length=6, delay_cost=1)
	Z_exp9 += alt(MM)
	S += Z_exp9>=Z_exp9_in

	Z_exp9_mem0 = S.Task('Z_exp9_mem0', length=1, delay_cost=1)
	Z_exp9_mem0 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < Z_exp9_mem0*MM_MEM[0]
	S += Z_exp9_mem0 <= Z_exp9

	Z_exp9_mem1 = S.Task('Z_exp9_mem1', length=1, delay_cost=1)
	Z_exp9_mem1 += MAIN_MEM_r[1]
	NX4_ = S.Task('NX4_', length=1, delay_cost=1)
	NX4_ += alt(MAS)

	NX4__mem0 = S.Task('NX4__mem0', length=1, delay_cost=1)
	NX4__mem0 += alt(MM_MEM)
	S += (NX3*MM[0])-1 < NX4__mem0*MM_MEM[0]
	S += NX4__mem0 <= NX4_

	NX4__mem1 = S.Task('NX4__mem1', length=1, delay_cost=1)
	NX4__mem1 += alt(MM_MEM)
	S += (k0_7_Z4*MM[0])-1 < NX4__mem1*MM_MEM[1]
	S += NX4__mem1 <= NX4_

	k0_3_Z8_in = S.Task('k0_3_Z8_in', length=1, delay_cost=1)
	k0_3_Z8_in += alt(MM_in)
	k0_3_Z8 = S.Task('k0_3_Z8', length=6, delay_cost=1)
	k0_3_Z8 += alt(MM)
	S += k0_3_Z8>=k0_3_Z8_in

	k0_3_Z8_mem0 = S.Task('k0_3_Z8_mem0', length=1, delay_cost=1)
	k0_3_Z8_mem0 += MAIN_MEM_r[0]
	k0_3_Z8_mem1 = S.Task('k0_3_Z8_mem1', length=1, delay_cost=1)
	k0_3_Z8_mem1 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < k0_3_Z8_mem1*MM_MEM[1]
	S += k0_3_Z8_mem1 <= k0_3_Z8

	DX3_in = S.Task('DX3_in', length=1, delay_cost=1)
	DX3_in += alt(MM_in)
	DX3 = S.Task('DX3', length=6, delay_cost=1)
	DX3 += alt(MM)
	S += DX3>=DX3_in

	DX3_mem0 = S.Task('DX3_mem0', length=1, delay_cost=1)
	DX3_mem0 += alt(MAS_MEM)
	S += (DX3_*MAS[0])-1 < DX3_mem0*MAS_MEM[0]
	S += (DX3_*MAS[1])-1 < DX3_mem0*MAS_MEM[2]
	S += (DX3_*MAS[2])-1 < DX3_mem0*MAS_MEM[4]
	S += (DX3_*MAS[3])-1 < DX3_mem0*MAS_MEM[6]
	S += DX3_mem0 <= DX3

	DX3_mem1 = S.Task('DX3_mem1', length=1, delay_cost=1)
	DX3_mem1 += MAIN_MEM_r[1]
	k1_3_Z8_in = S.Task('k1_3_Z8_in', length=1, delay_cost=1)
	k1_3_Z8_in += alt(MM_in)
	k1_3_Z8 = S.Task('k1_3_Z8', length=6, delay_cost=1)
	k1_3_Z8 += alt(MM)
	S += k1_3_Z8>=k1_3_Z8_in

	k1_3_Z8_mem0 = S.Task('k1_3_Z8_mem0', length=1, delay_cost=1)
	k1_3_Z8_mem0 += MAIN_MEM_r[0]
	k1_3_Z8_mem1 = S.Task('k1_3_Z8_mem1', length=1, delay_cost=1)
	k1_3_Z8_mem1 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < k1_3_Z8_mem1*MM_MEM[1]
	S += k1_3_Z8_mem1 <= k1_3_Z8

	NY4_ = S.Task('NY4_', length=1, delay_cost=1)
	NY4_ += alt(MAS)

	NY4__mem0 = S.Task('NY4__mem0', length=1, delay_cost=1)
	NY4__mem0 += alt(MM_MEM)
	S += (NY3*MM[0])-1 < NY4__mem0*MM_MEM[0]
	S += NY4__mem0 <= NY4_

	NY4__mem1 = S.Task('NY4__mem1', length=1, delay_cost=1)
	NY4__mem1 += alt(MM_MEM)
	S += (k2_11_Z4*MM[0])-1 < NY4__mem1*MM_MEM[1]
	S += NY4__mem1 <= NY4_

	k2_7_Z8_in = S.Task('k2_7_Z8_in', length=1, delay_cost=1)
	k2_7_Z8_in += alt(MM_in)
	k2_7_Z8 = S.Task('k2_7_Z8', length=6, delay_cost=1)
	k2_7_Z8 += alt(MM)
	S += k2_7_Z8>=k2_7_Z8_in

	k2_7_Z8_mem0 = S.Task('k2_7_Z8_mem0', length=1, delay_cost=1)
	k2_7_Z8_mem0 += MAIN_MEM_r[0]
	k2_7_Z8_mem1 = S.Task('k2_7_Z8_mem1', length=1, delay_cost=1)
	k2_7_Z8_mem1 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < k2_7_Z8_mem1*MM_MEM[1]
	S += k2_7_Z8_mem1 <= k2_7_Z8

	DY3_in = S.Task('DY3_in', length=1, delay_cost=1)
	DY3_in += alt(MM_in)
	DY3 = S.Task('DY3', length=6, delay_cost=1)
	DY3 += alt(MM)
	S += DY3>=DY3_in

	DY3_mem0 = S.Task('DY3_mem0', length=1, delay_cost=1)
	DY3_mem0 += alt(MAS_MEM)
	S += (DY3_*MAS[0])-1 < DY3_mem0*MAS_MEM[0]
	S += (DY3_*MAS[1])-1 < DY3_mem0*MAS_MEM[2]
	S += (DY3_*MAS[2])-1 < DY3_mem0*MAS_MEM[4]
	S += (DY3_*MAS[3])-1 < DY3_mem0*MAS_MEM[6]
	S += DY3_mem0 <= DY3

	DY3_mem1 = S.Task('DY3_mem1', length=1, delay_cost=1)
	DY3_mem1 += MAIN_MEM_r[1]
	k3_8_Z8_in = S.Task('k3_8_Z8_in', length=1, delay_cost=1)
	k3_8_Z8_in += alt(MM_in)
	k3_8_Z8 = S.Task('k3_8_Z8', length=6, delay_cost=1)
	k3_8_Z8 += alt(MM)
	S += k3_8_Z8>=k3_8_Z8_in

	k3_8_Z8_mem0 = S.Task('k3_8_Z8_mem0', length=1, delay_cost=1)
	k3_8_Z8_mem0 += MAIN_MEM_r[0]
	k3_8_Z8_mem1 = S.Task('k3_8_Z8_mem1', length=1, delay_cost=1)
	k3_8_Z8_mem1 += alt(MM_MEM)
	S += (Z_exp8*MM[0])-1 < k3_8_Z8_mem1*MM_MEM[1]
	S += k3_8_Z8_mem1 <= k3_8_Z8

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage1MAS4/ISOGENY/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

