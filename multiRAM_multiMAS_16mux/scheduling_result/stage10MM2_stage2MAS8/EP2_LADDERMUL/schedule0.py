from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=8)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	T1_t0 = S.Task('T1_t0', length=2, delay_cost=1)
	T1_t0 += alt(MAS)
	T1_t0_in = S.Task('T1_t0_in', length=1, delay_cost=1)
	T1_t0_in += alt(MAS_in)
	S += T1_t0_in*MAS_in[0]<=T1_t0*MAS[0]

	S += T1_t0_in*MAS_in[1]<=T1_t0*MAS[1]

	S += T1_t0_in*MAS_in[2]<=T1_t0*MAS[2]

	S += T1_t0_in*MAS_in[3]<=T1_t0*MAS[3]

	S += T1_t0_in*MAS_in[4]<=T1_t0*MAS[4]

	S += T1_t0_in*MAS_in[5]<=T1_t0*MAS[5]

	S += T1_t0_in*MAS_in[6]<=T1_t0*MAS[6]

	S += T1_t0_in*MAS_in[7]<=T1_t0*MAS[7]

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	T1_t0_mem0 += MAIN_MEM_r[0]
	S += T1_t0_mem0 <= T1_t0

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	T1_t0_mem1 += MAIN_MEM_r[1]
	S += T1_t0_mem1 <= T1_t0

	T1_t1 = S.Task('T1_t1', length=2, delay_cost=1)
	T1_t1 += alt(MAS)
	T1_t1_in = S.Task('T1_t1_in', length=1, delay_cost=1)
	T1_t1_in += alt(MAS_in)
	S += T1_t1_in*MAS_in[0]<=T1_t1*MAS[0]

	S += T1_t1_in*MAS_in[1]<=T1_t1*MAS[1]

	S += T1_t1_in*MAS_in[2]<=T1_t1*MAS[2]

	S += T1_t1_in*MAS_in[3]<=T1_t1*MAS[3]

	S += T1_t1_in*MAS_in[4]<=T1_t1*MAS[4]

	S += T1_t1_in*MAS_in[5]<=T1_t1*MAS[5]

	S += T1_t1_in*MAS_in[6]<=T1_t1*MAS[6]

	S += T1_t1_in*MAS_in[7]<=T1_t1*MAS[7]

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	T1_t1_mem0 += MAIN_MEM_r[0]
	S += T1_t1_mem0 <= T1_t1

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	T1_t1_mem1 += MAIN_MEM_r[1]
	S += T1_t1_mem1 <= T1_t1

	T1_t3 = S.Task('T1_t3', length=10, delay_cost=1)
	T1_t3 += alt(MM)
	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	T1_t3_in += alt(MM_in)
	S += T1_t3_in*MM_in[0]<=T1_t3*MM[0]
	S += T1_t3_in*MM_in[1]<=T1_t3*MM[1]
	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	T1_t3_mem0 += MAIN_MEM_r[0]
	S += T1_t3_mem0 <= T1_t3

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	T1_t3_mem1 += MAIN_MEM_r[1]
	S += T1_t3_mem1 <= T1_t3

	T2_t0 = S.Task('T2_t0', length=10, delay_cost=1)
	T2_t0 += alt(MM)
	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	T2_t0_in += alt(MM_in)
	S += T2_t0_in*MM_in[0]<=T2_t0*MM[0]
	S += T2_t0_in*MM_in[1]<=T2_t0*MM[1]
	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	T2_t0_mem0 += MAIN_MEM_r[0]
	S += T2_t0_mem0 <= T2_t0

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	T2_t0_mem1 += MAIN_MEM_r[1]
	S += T2_t0_mem1 <= T2_t0

	T2_t1 = S.Task('T2_t1', length=10, delay_cost=1)
	T2_t1 += alt(MM)
	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	T2_t1_in += alt(MM_in)
	S += T2_t1_in*MM_in[0]<=T2_t1*MM[0]
	S += T2_t1_in*MM_in[1]<=T2_t1*MM[1]
	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	T2_t1_mem0 += MAIN_MEM_r[0]
	S += T2_t1_mem0 <= T2_t1

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	T2_t1_mem1 += MAIN_MEM_r[1]
	S += T2_t1_mem1 <= T2_t1

	T2_t2 = S.Task('T2_t2', length=2, delay_cost=1)
	T2_t2 += alt(MAS)
	T2_t2_in = S.Task('T2_t2_in', length=1, delay_cost=1)
	T2_t2_in += alt(MAS_in)
	S += T2_t2_in*MAS_in[0]<=T2_t2*MAS[0]

	S += T2_t2_in*MAS_in[1]<=T2_t2*MAS[1]

	S += T2_t2_in*MAS_in[2]<=T2_t2*MAS[2]

	S += T2_t2_in*MAS_in[3]<=T2_t2*MAS[3]

	S += T2_t2_in*MAS_in[4]<=T2_t2*MAS[4]

	S += T2_t2_in*MAS_in[5]<=T2_t2*MAS[5]

	S += T2_t2_in*MAS_in[6]<=T2_t2*MAS[6]

	S += T2_t2_in*MAS_in[7]<=T2_t2*MAS[7]

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	T2_t2_mem0 += MAIN_MEM_r[0]
	S += T2_t2_mem0 <= T2_t2

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	T2_t2_mem1 += MAIN_MEM_r[1]
	S += T2_t2_mem1 <= T2_t2

	T2_t3 = S.Task('T2_t3', length=2, delay_cost=1)
	T2_t3 += alt(MAS)
	T2_t3_in = S.Task('T2_t3_in', length=1, delay_cost=1)
	T2_t3_in += alt(MAS_in)
	S += T2_t3_in*MAS_in[0]<=T2_t3*MAS[0]

	S += T2_t3_in*MAS_in[1]<=T2_t3*MAS[1]

	S += T2_t3_in*MAS_in[2]<=T2_t3*MAS[2]

	S += T2_t3_in*MAS_in[3]<=T2_t3*MAS[3]

	S += T2_t3_in*MAS_in[4]<=T2_t3*MAS[4]

	S += T2_t3_in*MAS_in[5]<=T2_t3*MAS[5]

	S += T2_t3_in*MAS_in[6]<=T2_t3*MAS[6]

	S += T2_t3_in*MAS_in[7]<=T2_t3*MAS[7]

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	T2_t3_mem0 += MAIN_MEM_r[0]
	S += T2_t3_mem0 <= T2_t3

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	T2_t3_mem1 += MAIN_MEM_r[1]
	S += T2_t3_mem1 <= T2_t3

	T3_t0 = S.Task('T3_t0', length=10, delay_cost=1)
	T3_t0 += alt(MM)
	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	T3_t0_in += alt(MM_in)
	S += T3_t0_in*MM_in[0]<=T3_t0*MM[0]
	S += T3_t0_in*MM_in[1]<=T3_t0*MM[1]
	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	T3_t0_mem0 += MAIN_MEM_r[0]
	S += T3_t0_mem0 <= T3_t0

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	T3_t0_mem1 += MAIN_MEM_r[1]
	S += T3_t0_mem1 <= T3_t0

	T3_t1 = S.Task('T3_t1', length=10, delay_cost=1)
	T3_t1 += alt(MM)
	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	T3_t1_in += alt(MM_in)
	S += T3_t1_in*MM_in[0]<=T3_t1*MM[0]
	S += T3_t1_in*MM_in[1]<=T3_t1*MM[1]
	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	T3_t1_mem0 += MAIN_MEM_r[0]
	S += T3_t1_mem0 <= T3_t1

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	T3_t1_mem1 += MAIN_MEM_r[1]
	S += T3_t1_mem1 <= T3_t1

	T3_t2 = S.Task('T3_t2', length=2, delay_cost=1)
	T3_t2 += alt(MAS)
	T3_t2_in = S.Task('T3_t2_in', length=1, delay_cost=1)
	T3_t2_in += alt(MAS_in)
	S += T3_t2_in*MAS_in[0]<=T3_t2*MAS[0]

	S += T3_t2_in*MAS_in[1]<=T3_t2*MAS[1]

	S += T3_t2_in*MAS_in[2]<=T3_t2*MAS[2]

	S += T3_t2_in*MAS_in[3]<=T3_t2*MAS[3]

	S += T3_t2_in*MAS_in[4]<=T3_t2*MAS[4]

	S += T3_t2_in*MAS_in[5]<=T3_t2*MAS[5]

	S += T3_t2_in*MAS_in[6]<=T3_t2*MAS[6]

	S += T3_t2_in*MAS_in[7]<=T3_t2*MAS[7]

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	T3_t2_mem0 += MAIN_MEM_r[0]
	S += T3_t2_mem0 <= T3_t2

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	T3_t2_mem1 += MAIN_MEM_r[1]
	S += T3_t2_mem1 <= T3_t2

	T3_t3 = S.Task('T3_t3', length=2, delay_cost=1)
	T3_t3 += alt(MAS)
	T3_t3_in = S.Task('T3_t3_in', length=1, delay_cost=1)
	T3_t3_in += alt(MAS_in)
	S += T3_t3_in*MAS_in[0]<=T3_t3*MAS[0]

	S += T3_t3_in*MAS_in[1]<=T3_t3*MAS[1]

	S += T3_t3_in*MAS_in[2]<=T3_t3*MAS[2]

	S += T3_t3_in*MAS_in[3]<=T3_t3*MAS[3]

	S += T3_t3_in*MAS_in[4]<=T3_t3*MAS[4]

	S += T3_t3_in*MAS_in[5]<=T3_t3*MAS[5]

	S += T3_t3_in*MAS_in[6]<=T3_t3*MAS[6]

	S += T3_t3_in*MAS_in[7]<=T3_t3*MAS[7]

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	T3_t3_mem0 += MAIN_MEM_r[0]
	S += T3_t3_mem0 <= T3_t3

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	T3_t3_mem1 += MAIN_MEM_r[1]
	S += T3_t3_mem1 <= T3_t3

	T4_t0 = S.Task('T4_t0', length=10, delay_cost=1)
	T4_t0 += alt(MM)
	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	T4_t0_in += alt(MM_in)
	S += T4_t0_in*MM_in[0]<=T4_t0*MM[0]
	S += T4_t0_in*MM_in[1]<=T4_t0*MM[1]
	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	T4_t0_mem0 += MAIN_MEM_r[0]
	S += T4_t0_mem0 <= T4_t0

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	T4_t0_mem1 += MAIN_MEM_r[1]
	S += T4_t0_mem1 <= T4_t0

	T4_t1 = S.Task('T4_t1', length=10, delay_cost=1)
	T4_t1 += alt(MM)
	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	T4_t1_in += alt(MM_in)
	S += T4_t1_in*MM_in[0]<=T4_t1*MM[0]
	S += T4_t1_in*MM_in[1]<=T4_t1*MM[1]
	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	T4_t1_mem0 += MAIN_MEM_r[0]
	S += T4_t1_mem0 <= T4_t1

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	T4_t1_mem1 += MAIN_MEM_r[1]
	S += T4_t1_mem1 <= T4_t1

	T4_t2 = S.Task('T4_t2', length=2, delay_cost=1)
	T4_t2 += alt(MAS)
	T4_t2_in = S.Task('T4_t2_in', length=1, delay_cost=1)
	T4_t2_in += alt(MAS_in)
	S += T4_t2_in*MAS_in[0]<=T4_t2*MAS[0]

	S += T4_t2_in*MAS_in[1]<=T4_t2*MAS[1]

	S += T4_t2_in*MAS_in[2]<=T4_t2*MAS[2]

	S += T4_t2_in*MAS_in[3]<=T4_t2*MAS[3]

	S += T4_t2_in*MAS_in[4]<=T4_t2*MAS[4]

	S += T4_t2_in*MAS_in[5]<=T4_t2*MAS[5]

	S += T4_t2_in*MAS_in[6]<=T4_t2*MAS[6]

	S += T4_t2_in*MAS_in[7]<=T4_t2*MAS[7]

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	T4_t2_mem0 += MAIN_MEM_r[0]
	S += T4_t2_mem0 <= T4_t2

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	T4_t2_mem1 += MAIN_MEM_r[1]
	S += T4_t2_mem1 <= T4_t2

	T4_t3 = S.Task('T4_t3', length=2, delay_cost=1)
	T4_t3 += alt(MAS)
	T4_t3_in = S.Task('T4_t3_in', length=1, delay_cost=1)
	T4_t3_in += alt(MAS_in)
	S += T4_t3_in*MAS_in[0]<=T4_t3*MAS[0]

	S += T4_t3_in*MAS_in[1]<=T4_t3*MAS[1]

	S += T4_t3_in*MAS_in[2]<=T4_t3*MAS[2]

	S += T4_t3_in*MAS_in[3]<=T4_t3*MAS[3]

	S += T4_t3_in*MAS_in[4]<=T4_t3*MAS[4]

	S += T4_t3_in*MAS_in[5]<=T4_t3*MAS[5]

	S += T4_t3_in*MAS_in[6]<=T4_t3*MAS[6]

	S += T4_t3_in*MAS_in[7]<=T4_t3*MAS[7]

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	T4_t3_mem0 += MAIN_MEM_r[0]
	S += T4_t3_mem0 <= T4_t3

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	T4_t3_mem1 += MAIN_MEM_r[1]
	S += T4_t3_mem1 <= T4_t3

	T5_t0 = S.Task('T5_t0', length=2, delay_cost=1)
	T5_t0 += alt(MAS)
	T5_t0_in = S.Task('T5_t0_in', length=1, delay_cost=1)
	T5_t0_in += alt(MAS_in)
	S += T5_t0_in*MAS_in[0]<=T5_t0*MAS[0]

	S += T5_t0_in*MAS_in[1]<=T5_t0*MAS[1]

	S += T5_t0_in*MAS_in[2]<=T5_t0*MAS[2]

	S += T5_t0_in*MAS_in[3]<=T5_t0*MAS[3]

	S += T5_t0_in*MAS_in[4]<=T5_t0*MAS[4]

	S += T5_t0_in*MAS_in[5]<=T5_t0*MAS[5]

	S += T5_t0_in*MAS_in[6]<=T5_t0*MAS[6]

	S += T5_t0_in*MAS_in[7]<=T5_t0*MAS[7]

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	T5_t0_mem0 += MAIN_MEM_r[0]
	S += T5_t0_mem0 <= T5_t0

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	T5_t0_mem1 += MAIN_MEM_r[1]
	S += T5_t0_mem1 <= T5_t0

	T5_t1 = S.Task('T5_t1', length=2, delay_cost=1)
	T5_t1 += alt(MAS)
	T5_t1_in = S.Task('T5_t1_in', length=1, delay_cost=1)
	T5_t1_in += alt(MAS_in)
	S += T5_t1_in*MAS_in[0]<=T5_t1*MAS[0]

	S += T5_t1_in*MAS_in[1]<=T5_t1*MAS[1]

	S += T5_t1_in*MAS_in[2]<=T5_t1*MAS[2]

	S += T5_t1_in*MAS_in[3]<=T5_t1*MAS[3]

	S += T5_t1_in*MAS_in[4]<=T5_t1*MAS[4]

	S += T5_t1_in*MAS_in[5]<=T5_t1*MAS[5]

	S += T5_t1_in*MAS_in[6]<=T5_t1*MAS[6]

	S += T5_t1_in*MAS_in[7]<=T5_t1*MAS[7]

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	T5_t1_mem0 += MAIN_MEM_r[0]
	S += T5_t1_mem0 <= T5_t1

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	T5_t1_mem1 += MAIN_MEM_r[1]
	S += T5_t1_mem1 <= T5_t1

	T5_t3 = S.Task('T5_t3', length=10, delay_cost=1)
	T5_t3 += alt(MM)
	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	T5_t3_in += alt(MM_in)
	S += T5_t3_in*MM_in[0]<=T5_t3*MM[0]
	S += T5_t3_in*MM_in[1]<=T5_t3*MM[1]
	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	T5_t3_mem0 += MAIN_MEM_r[0]
	S += T5_t3_mem0 <= T5_t3

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	T5_t3_mem1 += MAIN_MEM_r[1]
	S += T5_t3_mem1 <= T5_t3

	T6_t0 = S.Task('T6_t0', length=10, delay_cost=1)
	T6_t0 += alt(MM)
	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	T6_t0_in += alt(MM_in)
	S += T6_t0_in*MM_in[0]<=T6_t0*MM[0]
	S += T6_t0_in*MM_in[1]<=T6_t0*MM[1]
	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	T6_t0_mem0 += MAIN_MEM_r[0]
	S += T6_t0_mem0 <= T6_t0

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	T6_t0_mem1 += MAIN_MEM_r[1]
	S += T6_t0_mem1 <= T6_t0

	T6_t1 = S.Task('T6_t1', length=10, delay_cost=1)
	T6_t1 += alt(MM)
	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	T6_t1_in += alt(MM_in)
	S += T6_t1_in*MM_in[0]<=T6_t1*MM[0]
	S += T6_t1_in*MM_in[1]<=T6_t1*MM[1]
	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	T6_t1_mem0 += MAIN_MEM_r[0]
	S += T6_t1_mem0 <= T6_t1

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	T6_t1_mem1 += MAIN_MEM_r[1]
	S += T6_t1_mem1 <= T6_t1

	T6_t2 = S.Task('T6_t2', length=2, delay_cost=1)
	T6_t2 += alt(MAS)
	T6_t2_in = S.Task('T6_t2_in', length=1, delay_cost=1)
	T6_t2_in += alt(MAS_in)
	S += T6_t2_in*MAS_in[0]<=T6_t2*MAS[0]

	S += T6_t2_in*MAS_in[1]<=T6_t2*MAS[1]

	S += T6_t2_in*MAS_in[2]<=T6_t2*MAS[2]

	S += T6_t2_in*MAS_in[3]<=T6_t2*MAS[3]

	S += T6_t2_in*MAS_in[4]<=T6_t2*MAS[4]

	S += T6_t2_in*MAS_in[5]<=T6_t2*MAS[5]

	S += T6_t2_in*MAS_in[6]<=T6_t2*MAS[6]

	S += T6_t2_in*MAS_in[7]<=T6_t2*MAS[7]

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	T6_t2_mem0 += MAIN_MEM_r[0]
	S += T6_t2_mem0 <= T6_t2

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	T6_t2_mem1 += MAIN_MEM_r[1]
	S += T6_t2_mem1 <= T6_t2

	T6_t3 = S.Task('T6_t3', length=2, delay_cost=1)
	T6_t3 += alt(MAS)
	T6_t3_in = S.Task('T6_t3_in', length=1, delay_cost=1)
	T6_t3_in += alt(MAS_in)
	S += T6_t3_in*MAS_in[0]<=T6_t3*MAS[0]

	S += T6_t3_in*MAS_in[1]<=T6_t3*MAS[1]

	S += T6_t3_in*MAS_in[2]<=T6_t3*MAS[2]

	S += T6_t3_in*MAS_in[3]<=T6_t3*MAS[3]

	S += T6_t3_in*MAS_in[4]<=T6_t3*MAS[4]

	S += T6_t3_in*MAS_in[5]<=T6_t3*MAS[5]

	S += T6_t3_in*MAS_in[6]<=T6_t3*MAS[6]

	S += T6_t3_in*MAS_in[7]<=T6_t3*MAS[7]

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	T6_t3_mem0 += MAIN_MEM_r[0]
	S += T6_t3_mem0 <= T6_t3

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	T6_t3_mem1 += MAIN_MEM_r[1]
	S += T6_t3_mem1 <= T6_t3

	T7_t0 = S.Task('T7_t0', length=10, delay_cost=1)
	T7_t0 += alt(MM)
	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	T7_t0_in += alt(MM_in)
	S += T7_t0_in*MM_in[0]<=T7_t0*MM[0]
	S += T7_t0_in*MM_in[1]<=T7_t0*MM[1]
	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	T7_t0_mem0 += MAIN_MEM_r[0]
	S += T7_t0_mem0 <= T7_t0

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	T7_t0_mem1 += MAIN_MEM_r[1]
	S += T7_t0_mem1 <= T7_t0

	T7_t1 = S.Task('T7_t1', length=10, delay_cost=1)
	T7_t1 += alt(MM)
	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	T7_t1_in += alt(MM_in)
	S += T7_t1_in*MM_in[0]<=T7_t1*MM[0]
	S += T7_t1_in*MM_in[1]<=T7_t1*MM[1]
	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	T7_t1_mem0 += MAIN_MEM_r[0]
	S += T7_t1_mem0 <= T7_t1

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	T7_t1_mem1 += MAIN_MEM_r[1]
	S += T7_t1_mem1 <= T7_t1

	T7_t2 = S.Task('T7_t2', length=2, delay_cost=1)
	T7_t2 += alt(MAS)
	T7_t2_in = S.Task('T7_t2_in', length=1, delay_cost=1)
	T7_t2_in += alt(MAS_in)
	S += T7_t2_in*MAS_in[0]<=T7_t2*MAS[0]

	S += T7_t2_in*MAS_in[1]<=T7_t2*MAS[1]

	S += T7_t2_in*MAS_in[2]<=T7_t2*MAS[2]

	S += T7_t2_in*MAS_in[3]<=T7_t2*MAS[3]

	S += T7_t2_in*MAS_in[4]<=T7_t2*MAS[4]

	S += T7_t2_in*MAS_in[5]<=T7_t2*MAS[5]

	S += T7_t2_in*MAS_in[6]<=T7_t2*MAS[6]

	S += T7_t2_in*MAS_in[7]<=T7_t2*MAS[7]

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	T7_t2_mem0 += MAIN_MEM_r[0]
	S += T7_t2_mem0 <= T7_t2

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	T7_t2_mem1 += MAIN_MEM_r[1]
	S += T7_t2_mem1 <= T7_t2

	T7_t3 = S.Task('T7_t3', length=2, delay_cost=1)
	T7_t3 += alt(MAS)
	T7_t3_in = S.Task('T7_t3_in', length=1, delay_cost=1)
	T7_t3_in += alt(MAS_in)
	S += T7_t3_in*MAS_in[0]<=T7_t3*MAS[0]

	S += T7_t3_in*MAS_in[1]<=T7_t3*MAS[1]

	S += T7_t3_in*MAS_in[2]<=T7_t3*MAS[2]

	S += T7_t3_in*MAS_in[3]<=T7_t3*MAS[3]

	S += T7_t3_in*MAS_in[4]<=T7_t3*MAS[4]

	S += T7_t3_in*MAS_in[5]<=T7_t3*MAS[5]

	S += T7_t3_in*MAS_in[6]<=T7_t3*MAS[6]

	S += T7_t3_in*MAS_in[7]<=T7_t3*MAS[7]

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	T7_t3_mem0 += MAIN_MEM_r[0]
	S += T7_t3_mem0 <= T7_t3

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	T7_t3_mem1 += MAIN_MEM_r[1]
	S += T7_t3_mem1 <= T7_t3

	T8_t2 = S.Task('T8_t2', length=2, delay_cost=1)
	T8_t2 += alt(MAS)
	T8_t2_in = S.Task('T8_t2_in', length=1, delay_cost=1)
	T8_t2_in += alt(MAS_in)
	S += T8_t2_in*MAS_in[0]<=T8_t2*MAS[0]

	S += T8_t2_in*MAS_in[1]<=T8_t2*MAS[1]

	S += T8_t2_in*MAS_in[2]<=T8_t2*MAS[2]

	S += T8_t2_in*MAS_in[3]<=T8_t2*MAS[3]

	S += T8_t2_in*MAS_in[4]<=T8_t2*MAS[4]

	S += T8_t2_in*MAS_in[5]<=T8_t2*MAS[5]

	S += T8_t2_in*MAS_in[6]<=T8_t2*MAS[6]

	S += T8_t2_in*MAS_in[7]<=T8_t2*MAS[7]

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	T8_t2_mem0 += MAIN_MEM_r[0]
	S += T8_t2_mem0 <= T8_t2

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	T8_t2_mem1 += MAIN_MEM_r[1]
	S += T8_t2_mem1 <= T8_t2

	T9_t2 = S.Task('T9_t2', length=2, delay_cost=1)
	T9_t2 += alt(MAS)
	T9_t2_in = S.Task('T9_t2_in', length=1, delay_cost=1)
	T9_t2_in += alt(MAS_in)
	S += T9_t2_in*MAS_in[0]<=T9_t2*MAS[0]

	S += T9_t2_in*MAS_in[1]<=T9_t2*MAS[1]

	S += T9_t2_in*MAS_in[2]<=T9_t2*MAS[2]

	S += T9_t2_in*MAS_in[3]<=T9_t2*MAS[3]

	S += T9_t2_in*MAS_in[4]<=T9_t2*MAS[4]

	S += T9_t2_in*MAS_in[5]<=T9_t2*MAS[5]

	S += T9_t2_in*MAS_in[6]<=T9_t2*MAS[6]

	S += T9_t2_in*MAS_in[7]<=T9_t2*MAS[7]

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	T9_t2_mem0 += MAIN_MEM_r[0]
	S += T9_t2_mem0 <= T9_t2

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	T9_t2_mem1 += MAIN_MEM_r[1]
	S += T9_t2_mem1 <= T9_t2

	T10_t2 = S.Task('T10_t2', length=2, delay_cost=1)
	T10_t2 += alt(MAS)
	T10_t2_in = S.Task('T10_t2_in', length=1, delay_cost=1)
	T10_t2_in += alt(MAS_in)
	S += T10_t2_in*MAS_in[0]<=T10_t2*MAS[0]

	S += T10_t2_in*MAS_in[1]<=T10_t2*MAS[1]

	S += T10_t2_in*MAS_in[2]<=T10_t2*MAS[2]

	S += T10_t2_in*MAS_in[3]<=T10_t2*MAS[3]

	S += T10_t2_in*MAS_in[4]<=T10_t2*MAS[4]

	S += T10_t2_in*MAS_in[5]<=T10_t2*MAS[5]

	S += T10_t2_in*MAS_in[6]<=T10_t2*MAS[6]

	S += T10_t2_in*MAS_in[7]<=T10_t2*MAS[7]

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	T10_t2_mem0 += MAIN_MEM_r[0]
	S += T10_t2_mem0 <= T10_t2

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	T10_t2_mem1 += MAIN_MEM_r[1]
	S += T10_t2_mem1 <= T10_t2

	T11_t2 = S.Task('T11_t2', length=2, delay_cost=1)
	T11_t2 += alt(MAS)
	T11_t2_in = S.Task('T11_t2_in', length=1, delay_cost=1)
	T11_t2_in += alt(MAS_in)
	S += T11_t2_in*MAS_in[0]<=T11_t2*MAS[0]

	S += T11_t2_in*MAS_in[1]<=T11_t2*MAS[1]

	S += T11_t2_in*MAS_in[2]<=T11_t2*MAS[2]

	S += T11_t2_in*MAS_in[3]<=T11_t2*MAS[3]

	S += T11_t2_in*MAS_in[4]<=T11_t2*MAS[4]

	S += T11_t2_in*MAS_in[5]<=T11_t2*MAS[5]

	S += T11_t2_in*MAS_in[6]<=T11_t2*MAS[6]

	S += T11_t2_in*MAS_in[7]<=T11_t2*MAS[7]

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	T11_t2_mem0 += MAIN_MEM_r[0]
	S += T11_t2_mem0 <= T11_t2

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	T11_t2_mem1 += MAIN_MEM_r[1]
	S += T11_t2_mem1 <= T11_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage2MAS8/EP2_LADDERMUL/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

