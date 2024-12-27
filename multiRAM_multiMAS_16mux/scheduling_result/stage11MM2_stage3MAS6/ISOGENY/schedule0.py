from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	Z_exp2 = S.Task('Z_exp2', length=11, delay_cost=1)
	Z_exp2 += alt(MM)
	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	Z_exp2_in += alt(MM_in)
	S += Z_exp2_in*MM_in[0]<=Z_exp2*MM[0]
	S += Z_exp2_in*MM_in[1]<=Z_exp2*MM[1]
	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	Z_exp2_mem0 += MAIN_MEM_r[0]
	S += Z_exp2_mem0 <= Z_exp2

	Z_exp2_mem1 = S.Task('Z_exp2_mem1', length=1, delay_cost=1)
	Z_exp2_mem1 += MAIN_MEM_r[1]
	S += Z_exp2_mem1 <= Z_exp2

	NX0 = S.Task('NX0', length=11, delay_cost=1)
	NX0 += alt(MM)
	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	NX0_in += alt(MM_in)
	S += NX0_in*MM_in[0]<=NX0*MM[0]
	S += NX0_in*MM_in[1]<=NX0*MM[1]
	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	NX0_mem0 += MAIN_MEM_r[0]
	S += NX0_mem0 <= NX0

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	NX0_mem1 += MAIN_MEM_r[1]
	S += NX0_mem1 <= NX0

	k0_10_Z1 = S.Task('k0_10_Z1', length=11, delay_cost=1)
	k0_10_Z1 += alt(MM)
	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	k0_10_Z1_in += alt(MM_in)
	S += k0_10_Z1_in*MM_in[0]<=k0_10_Z1*MM[0]
	S += k0_10_Z1_in*MM_in[1]<=k0_10_Z1*MM[1]
	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	k0_10_Z1_mem0 += MAIN_MEM_r[0]
	S += k0_10_Z1_mem0 <= k0_10_Z1

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	k0_10_Z1_mem1 += MAIN_MEM_r[1]
	S += k0_10_Z1_mem1 <= k0_10_Z1

	DX0 = S.Task('DX0', length=11, delay_cost=1)
	DX0 += alt(MM)
	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	DX0_in += alt(MM_in)
	S += DX0_in*MM_in[0]<=DX0*MM[0]
	S += DX0_in*MM_in[1]<=DX0*MM[1]
	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	DX0_mem0 += MAIN_MEM_r[0]
	S += DX0_mem0 <= DX0

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	DX0_mem1 += MAIN_MEM_r[1]
	S += DX0_mem1 <= DX0

	NY0 = S.Task('NY0', length=11, delay_cost=1)
	NY0 += alt(MM)
	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	NY0_in += alt(MM_in)
	S += NY0_in*MM_in[0]<=NY0*MM[0]
	S += NY0_in*MM_in[1]<=NY0*MM[1]
	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	NY0_mem0 += MAIN_MEM_r[0]
	S += NY0_mem0 <= NY0

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	NY0_mem1 += MAIN_MEM_r[1]
	S += NY0_mem1 <= NY0

	k2_14_Z1 = S.Task('k2_14_Z1', length=11, delay_cost=1)
	k2_14_Z1 += alt(MM)
	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	k2_14_Z1_in += alt(MM_in)
	S += k2_14_Z1_in*MM_in[0]<=k2_14_Z1*MM[0]
	S += k2_14_Z1_in*MM_in[1]<=k2_14_Z1*MM[1]
	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	k2_14_Z1_mem0 += MAIN_MEM_r[0]
	S += k2_14_Z1_mem0 <= k2_14_Z1

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	k2_14_Z1_mem1 += MAIN_MEM_r[1]
	S += k2_14_Z1_mem1 <= k2_14_Z1

	DY0 = S.Task('DY0', length=11, delay_cost=1)
	DY0 += alt(MM)
	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	DY0_in += alt(MM_in)
	S += DY0_in*MM_in[0]<=DY0*MM[0]
	S += DY0_in*MM_in[1]<=DY0*MM[1]
	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	DY0_mem0 += MAIN_MEM_r[0]
	S += DY0_mem0 <= DY0

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	DY0_mem1 += MAIN_MEM_r[1]
	S += DY0_mem1 <= DY0

	Z_exp3 = S.Task('Z_exp3', length=11, delay_cost=1)
	Z_exp3 += alt(MM)
	Z_exp3_in = S.Task('Z_exp3_in', length=1, delay_cost=1)
	Z_exp3_in += alt(MM_in)
	S += Z_exp3_in*MM_in[0]<=Z_exp3*MM[0]
	S += Z_exp3_in*MM_in[1]<=Z_exp3*MM[1]
	Z_exp3_mem0 = S.Task('Z_exp3_mem0', length=1, delay_cost=1)
	Z_exp3_mem0 += alt(MM_MEM)
	S += (Z_exp2*MM[0])-1 < Z_exp3_mem0*MM_MEM[0]
	S += (Z_exp2*MM[1])-1 < Z_exp3_mem0*MM_MEM[2]
	S += Z_exp3_mem0 <= Z_exp3

	Z_exp3_mem1 = S.Task('Z_exp3_mem1', length=1, delay_cost=1)
	Z_exp3_mem1 += MAIN_MEM_r[1]
	S += Z_exp3_mem1 <= Z_exp3

	NX1_ = S.Task('NX1_', length=3, delay_cost=1)
	NX1_ += alt(MAS)
	NX1__in = S.Task('NX1__in', length=1, delay_cost=1)
	NX1__in += alt(MAS_in)
	S += NX1__in*MAS_in[0]<=NX1_*MAS[0]

	S += NX1__in*MAS_in[1]<=NX1_*MAS[1]

	S += NX1__in*MAS_in[2]<=NX1_*MAS[2]

	S += NX1__in*MAS_in[3]<=NX1_*MAS[3]

	S += NX1__in*MAS_in[4]<=NX1_*MAS[4]

	S += NX1__in*MAS_in[5]<=NX1_*MAS[5]

	NX1__mem0 = S.Task('NX1__mem0', length=1, delay_cost=1)
	NX1__mem0 += alt(MM_MEM)
	S += (NX0*MM[0])-1 < NX1__mem0*MM_MEM[0]
	S += (NX0*MM[1])-1 < NX1__mem0*MM_MEM[2]
	S += NX1__mem0 <= NX1_

	NX1__mem1 = S.Task('NX1__mem1', length=1, delay_cost=1)
	NX1__mem1 += alt(MM_MEM)
	S += (k0_10_Z1*MM[0])-1 < NX1__mem1*MM_MEM[1]
	S += (k0_10_Z1*MM[1])-1 < NX1__mem1*MM_MEM[3]
	S += NX1__mem1 <= NX1_

	k0_9_Z2 = S.Task('k0_9_Z2', length=11, delay_cost=1)
	k0_9_Z2 += alt(MM)
	k0_9_Z2_in = S.Task('k0_9_Z2_in', length=1, delay_cost=1)
	k0_9_Z2_in += alt(MM_in)
	S += k0_9_Z2_in*MM_in[0]<=k0_9_Z2*MM[0]
	S += k0_9_Z2_in*MM_in[1]<=k0_9_Z2*MM[1]
	k0_9_Z2_mem0 = S.Task('k0_9_Z2_mem0', length=1, delay_cost=1)
	k0_9_Z2_mem0 += MAIN_MEM_r[0]
	S += k0_9_Z2_mem0 <= k0_9_Z2

	k0_9_Z2_mem1 = S.Task('k0_9_Z2_mem1', length=1, delay_cost=1)
	k0_9_Z2_mem1 += alt(MM_MEM)
	S += (Z_exp2*MM[0])-1 < k0_9_Z2_mem1*MM_MEM[1]
	S += (Z_exp2*MM[1])-1 < k0_9_Z2_mem1*MM_MEM[3]
	S += k0_9_Z2_mem1 <= k0_9_Z2

	k1_9_Z2 = S.Task('k1_9_Z2', length=11, delay_cost=1)
	k1_9_Z2 += alt(MM)
	k1_9_Z2_in = S.Task('k1_9_Z2_in', length=1, delay_cost=1)
	k1_9_Z2_in += alt(MM_in)
	S += k1_9_Z2_in*MM_in[0]<=k1_9_Z2*MM[0]
	S += k1_9_Z2_in*MM_in[1]<=k1_9_Z2*MM[1]
	k1_9_Z2_mem0 = S.Task('k1_9_Z2_mem0', length=1, delay_cost=1)
	k1_9_Z2_mem0 += MAIN_MEM_r[0]
	S += k1_9_Z2_mem0 <= k1_9_Z2

	k1_9_Z2_mem1 = S.Task('k1_9_Z2_mem1', length=1, delay_cost=1)
	k1_9_Z2_mem1 += alt(MM_MEM)
	S += (Z_exp2*MM[0])-1 < k1_9_Z2_mem1*MM_MEM[1]
	S += (Z_exp2*MM[1])-1 < k1_9_Z2_mem1*MM_MEM[3]
	S += k1_9_Z2_mem1 <= k1_9_Z2

	NY1_ = S.Task('NY1_', length=3, delay_cost=1)
	NY1_ += alt(MAS)
	NY1__in = S.Task('NY1__in', length=1, delay_cost=1)
	NY1__in += alt(MAS_in)
	S += NY1__in*MAS_in[0]<=NY1_*MAS[0]

	S += NY1__in*MAS_in[1]<=NY1_*MAS[1]

	S += NY1__in*MAS_in[2]<=NY1_*MAS[2]

	S += NY1__in*MAS_in[3]<=NY1_*MAS[3]

	S += NY1__in*MAS_in[4]<=NY1_*MAS[4]

	S += NY1__in*MAS_in[5]<=NY1_*MAS[5]

	NY1__mem0 = S.Task('NY1__mem0', length=1, delay_cost=1)
	NY1__mem0 += alt(MM_MEM)
	S += (NY0*MM[0])-1 < NY1__mem0*MM_MEM[0]
	S += (NY0*MM[1])-1 < NY1__mem0*MM_MEM[2]
	S += NY1__mem0 <= NY1_

	NY1__mem1 = S.Task('NY1__mem1', length=1, delay_cost=1)
	NY1__mem1 += alt(MM_MEM)
	S += (k2_14_Z1*MM[0])-1 < NY1__mem1*MM_MEM[1]
	S += (k2_14_Z1*MM[1])-1 < NY1__mem1*MM_MEM[3]
	S += NY1__mem1 <= NY1_

	k2_13_Z2 = S.Task('k2_13_Z2', length=11, delay_cost=1)
	k2_13_Z2 += alt(MM)
	k2_13_Z2_in = S.Task('k2_13_Z2_in', length=1, delay_cost=1)
	k2_13_Z2_in += alt(MM_in)
	S += k2_13_Z2_in*MM_in[0]<=k2_13_Z2*MM[0]
	S += k2_13_Z2_in*MM_in[1]<=k2_13_Z2*MM[1]
	k2_13_Z2_mem0 = S.Task('k2_13_Z2_mem0', length=1, delay_cost=1)
	k2_13_Z2_mem0 += MAIN_MEM_r[0]
	S += k2_13_Z2_mem0 <= k2_13_Z2

	k2_13_Z2_mem1 = S.Task('k2_13_Z2_mem1', length=1, delay_cost=1)
	k2_13_Z2_mem1 += alt(MM_MEM)
	S += (Z_exp2*MM[0])-1 < k2_13_Z2_mem1*MM_MEM[1]
	S += (Z_exp2*MM[1])-1 < k2_13_Z2_mem1*MM_MEM[3]
	S += k2_13_Z2_mem1 <= k2_13_Z2

	k3_14_Z2 = S.Task('k3_14_Z2', length=11, delay_cost=1)
	k3_14_Z2 += alt(MM)
	k3_14_Z2_in = S.Task('k3_14_Z2_in', length=1, delay_cost=1)
	k3_14_Z2_in += alt(MM_in)
	S += k3_14_Z2_in*MM_in[0]<=k3_14_Z2*MM[0]
	S += k3_14_Z2_in*MM_in[1]<=k3_14_Z2*MM[1]
	k3_14_Z2_mem0 = S.Task('k3_14_Z2_mem0', length=1, delay_cost=1)
	k3_14_Z2_mem0 += MAIN_MEM_r[0]
	S += k3_14_Z2_mem0 <= k3_14_Z2

	k3_14_Z2_mem1 = S.Task('k3_14_Z2_mem1', length=1, delay_cost=1)
	k3_14_Z2_mem1 += alt(MM_MEM)
	S += (Z_exp2*MM[0])-1 < k3_14_Z2_mem1*MM_MEM[1]
	S += (Z_exp2*MM[1])-1 < k3_14_Z2_mem1*MM_MEM[3]
	S += k3_14_Z2_mem1 <= k3_14_Z2

	Z_exp4 = S.Task('Z_exp4', length=11, delay_cost=1)
	Z_exp4 += alt(MM)
	Z_exp4_in = S.Task('Z_exp4_in', length=1, delay_cost=1)
	Z_exp4_in += alt(MM_in)
	S += Z_exp4_in*MM_in[0]<=Z_exp4*MM[0]
	S += Z_exp4_in*MM_in[1]<=Z_exp4*MM[1]
	Z_exp4_mem0 = S.Task('Z_exp4_mem0', length=1, delay_cost=1)
	Z_exp4_mem0 += alt(MM_MEM)
	S += (Z_exp3*MM[0])-1 < Z_exp4_mem0*MM_MEM[0]
	S += (Z_exp3*MM[1])-1 < Z_exp4_mem0*MM_MEM[2]
	S += Z_exp4_mem0 <= Z_exp4

	Z_exp4_mem1 = S.Task('Z_exp4_mem1', length=1, delay_cost=1)
	Z_exp4_mem1 += MAIN_MEM_r[1]
	S += Z_exp4_mem1 <= Z_exp4

	NX1 = S.Task('NX1', length=11, delay_cost=1)
	NX1 += alt(MM)
	NX1_in = S.Task('NX1_in', length=1, delay_cost=1)
	NX1_in += alt(MM_in)
	S += NX1_in*MM_in[0]<=NX1*MM[0]
	S += NX1_in*MM_in[1]<=NX1*MM[1]
	NX1_mem0 = S.Task('NX1_mem0', length=1, delay_cost=1)
	NX1_mem0 += alt(MAS_MEM)
	S += (NX1_*MAS[0])-1 < NX1_mem0*MAS_MEM[0]
	S += (NX1_*MAS[1])-1 < NX1_mem0*MAS_MEM[2]
	S += (NX1_*MAS[2])-1 < NX1_mem0*MAS_MEM[4]
	S += (NX1_*MAS[3])-1 < NX1_mem0*MAS_MEM[6]
	S += (NX1_*MAS[4])-1 < NX1_mem0*MAS_MEM[8]
	S += (NX1_*MAS[5])-1 < NX1_mem0*MAS_MEM[10]
	S += NX1_mem0 <= NX1

	NX1_mem1 = S.Task('NX1_mem1', length=1, delay_cost=1)
	NX1_mem1 += MAIN_MEM_r[1]
	S += NX1_mem1 <= NX1

	k0_8_Z3 = S.Task('k0_8_Z3', length=11, delay_cost=1)
	k0_8_Z3 += alt(MM)
	k0_8_Z3_in = S.Task('k0_8_Z3_in', length=1, delay_cost=1)
	k0_8_Z3_in += alt(MM_in)
	S += k0_8_Z3_in*MM_in[0]<=k0_8_Z3*MM[0]
	S += k0_8_Z3_in*MM_in[1]<=k0_8_Z3*MM[1]
	k0_8_Z3_mem0 = S.Task('k0_8_Z3_mem0', length=1, delay_cost=1)
	k0_8_Z3_mem0 += MAIN_MEM_r[0]
	S += k0_8_Z3_mem0 <= k0_8_Z3

	k0_8_Z3_mem1 = S.Task('k0_8_Z3_mem1', length=1, delay_cost=1)
	k0_8_Z3_mem1 += alt(MM_MEM)
	S += (Z_exp3*MM[0])-1 < k0_8_Z3_mem1*MM_MEM[1]
	S += (Z_exp3*MM[1])-1 < k0_8_Z3_mem1*MM_MEM[3]
	S += k0_8_Z3_mem1 <= k0_8_Z3

	DX1_ = S.Task('DX1_', length=3, delay_cost=1)
	DX1_ += alt(MAS)
	DX1__in = S.Task('DX1__in', length=1, delay_cost=1)
	DX1__in += alt(MAS_in)
	S += DX1__in*MAS_in[0]<=DX1_*MAS[0]

	S += DX1__in*MAS_in[1]<=DX1_*MAS[1]

	S += DX1__in*MAS_in[2]<=DX1_*MAS[2]

	S += DX1__in*MAS_in[3]<=DX1_*MAS[3]

	S += DX1__in*MAS_in[4]<=DX1_*MAS[4]

	S += DX1__in*MAS_in[5]<=DX1_*MAS[5]

	DX1__mem0 = S.Task('DX1__mem0', length=1, delay_cost=1)
	DX1__mem0 += alt(MM_MEM)
	S += (DX0*MM[0])-1 < DX1__mem0*MM_MEM[0]
	S += (DX0*MM[1])-1 < DX1__mem0*MM_MEM[2]
	S += DX1__mem0 <= DX1_

	DX1__mem1 = S.Task('DX1__mem1', length=1, delay_cost=1)
	DX1__mem1 += alt(MM_MEM)
	S += (k1_9_Z2*MM[0])-1 < DX1__mem1*MM_MEM[1]
	S += (k1_9_Z2*MM[1])-1 < DX1__mem1*MM_MEM[3]
	S += DX1__mem1 <= DX1_

	k1_8_Z3 = S.Task('k1_8_Z3', length=11, delay_cost=1)
	k1_8_Z3 += alt(MM)
	k1_8_Z3_in = S.Task('k1_8_Z3_in', length=1, delay_cost=1)
	k1_8_Z3_in += alt(MM_in)
	S += k1_8_Z3_in*MM_in[0]<=k1_8_Z3*MM[0]
	S += k1_8_Z3_in*MM_in[1]<=k1_8_Z3*MM[1]
	k1_8_Z3_mem0 = S.Task('k1_8_Z3_mem0', length=1, delay_cost=1)
	k1_8_Z3_mem0 += MAIN_MEM_r[0]
	S += k1_8_Z3_mem0 <= k1_8_Z3

	k1_8_Z3_mem1 = S.Task('k1_8_Z3_mem1', length=1, delay_cost=1)
	k1_8_Z3_mem1 += alt(MM_MEM)
	S += (Z_exp3*MM[0])-1 < k1_8_Z3_mem1*MM_MEM[1]
	S += (Z_exp3*MM[1])-1 < k1_8_Z3_mem1*MM_MEM[3]
	S += k1_8_Z3_mem1 <= k1_8_Z3

	NY1 = S.Task('NY1', length=11, delay_cost=1)
	NY1 += alt(MM)
	NY1_in = S.Task('NY1_in', length=1, delay_cost=1)
	NY1_in += alt(MM_in)
	S += NY1_in*MM_in[0]<=NY1*MM[0]
	S += NY1_in*MM_in[1]<=NY1*MM[1]
	NY1_mem0 = S.Task('NY1_mem0', length=1, delay_cost=1)
	NY1_mem0 += alt(MAS_MEM)
	S += (NY1_*MAS[0])-1 < NY1_mem0*MAS_MEM[0]
	S += (NY1_*MAS[1])-1 < NY1_mem0*MAS_MEM[2]
	S += (NY1_*MAS[2])-1 < NY1_mem0*MAS_MEM[4]
	S += (NY1_*MAS[3])-1 < NY1_mem0*MAS_MEM[6]
	S += (NY1_*MAS[4])-1 < NY1_mem0*MAS_MEM[8]
	S += (NY1_*MAS[5])-1 < NY1_mem0*MAS_MEM[10]
	S += NY1_mem0 <= NY1

	NY1_mem1 = S.Task('NY1_mem1', length=1, delay_cost=1)
	NY1_mem1 += MAIN_MEM_r[1]
	S += NY1_mem1 <= NY1

	k2_12_Z3 = S.Task('k2_12_Z3', length=11, delay_cost=1)
	k2_12_Z3 += alt(MM)
	k2_12_Z3_in = S.Task('k2_12_Z3_in', length=1, delay_cost=1)
	k2_12_Z3_in += alt(MM_in)
	S += k2_12_Z3_in*MM_in[0]<=k2_12_Z3*MM[0]
	S += k2_12_Z3_in*MM_in[1]<=k2_12_Z3*MM[1]
	k2_12_Z3_mem0 = S.Task('k2_12_Z3_mem0', length=1, delay_cost=1)
	k2_12_Z3_mem0 += MAIN_MEM_r[0]
	S += k2_12_Z3_mem0 <= k2_12_Z3

	k2_12_Z3_mem1 = S.Task('k2_12_Z3_mem1', length=1, delay_cost=1)
	k2_12_Z3_mem1 += alt(MM_MEM)
	S += (Z_exp3*MM[0])-1 < k2_12_Z3_mem1*MM_MEM[1]
	S += (Z_exp3*MM[1])-1 < k2_12_Z3_mem1*MM_MEM[3]
	S += k2_12_Z3_mem1 <= k2_12_Z3

	DY1_ = S.Task('DY1_', length=3, delay_cost=1)
	DY1_ += alt(MAS)
	DY1__in = S.Task('DY1__in', length=1, delay_cost=1)
	DY1__in += alt(MAS_in)
	S += DY1__in*MAS_in[0]<=DY1_*MAS[0]

	S += DY1__in*MAS_in[1]<=DY1_*MAS[1]

	S += DY1__in*MAS_in[2]<=DY1_*MAS[2]

	S += DY1__in*MAS_in[3]<=DY1_*MAS[3]

	S += DY1__in*MAS_in[4]<=DY1_*MAS[4]

	S += DY1__in*MAS_in[5]<=DY1_*MAS[5]

	DY1__mem0 = S.Task('DY1__mem0', length=1, delay_cost=1)
	DY1__mem0 += alt(MM_MEM)
	S += (DY0*MM[0])-1 < DY1__mem0*MM_MEM[0]
	S += (DY0*MM[1])-1 < DY1__mem0*MM_MEM[2]
	S += DY1__mem0 <= DY1_

	DY1__mem1 = S.Task('DY1__mem1', length=1, delay_cost=1)
	DY1__mem1 += alt(MM_MEM)
	S += (k3_14_Z2*MM[0])-1 < DY1__mem1*MM_MEM[1]
	S += (k3_14_Z2*MM[1])-1 < DY1__mem1*MM_MEM[3]
	S += DY1__mem1 <= DY1_

	k3_13_Z3 = S.Task('k3_13_Z3', length=11, delay_cost=1)
	k3_13_Z3 += alt(MM)
	k3_13_Z3_in = S.Task('k3_13_Z3_in', length=1, delay_cost=1)
	k3_13_Z3_in += alt(MM_in)
	S += k3_13_Z3_in*MM_in[0]<=k3_13_Z3*MM[0]
	S += k3_13_Z3_in*MM_in[1]<=k3_13_Z3*MM[1]
	k3_13_Z3_mem0 = S.Task('k3_13_Z3_mem0', length=1, delay_cost=1)
	k3_13_Z3_mem0 += MAIN_MEM_r[0]
	S += k3_13_Z3_mem0 <= k3_13_Z3

	k3_13_Z3_mem1 = S.Task('k3_13_Z3_mem1', length=1, delay_cost=1)
	k3_13_Z3_mem1 += alt(MM_MEM)
	S += (Z_exp3*MM[0])-1 < k3_13_Z3_mem1*MM_MEM[1]
	S += (Z_exp3*MM[1])-1 < k3_13_Z3_mem1*MM_MEM[3]
	S += k3_13_Z3_mem1 <= k3_13_Z3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage3MAS6/ISOGENY/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

