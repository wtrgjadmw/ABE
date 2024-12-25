from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	t1_t0 = S.Task('t1_t0', length=10, delay_cost=1)
	t1_t0 += alt(MM)
	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	t1_t0_in += alt(MM_in)
	S += t1_t0_in*MM_in[0]<=t1_t0*MM[0]
	S += t1_t0_in*MM_in[1]<=t1_t0*MM[1]
	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	t1_t0_mem0 += MAIN_MEM_r[0]
	S += t1_t0_mem0 <= t1_t0

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	t1_t0_mem1 += MAIN_MEM_r[1]
	S += t1_t0_mem1 <= t1_t0

	t1_t1 = S.Task('t1_t1', length=10, delay_cost=1)
	t1_t1 += alt(MM)
	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	t1_t1_in += alt(MM_in)
	S += t1_t1_in*MM_in[0]<=t1_t1*MM[0]
	S += t1_t1_in*MM_in[1]<=t1_t1*MM[1]
	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	t1_t1_mem0 += MAIN_MEM_r[0]
	S += t1_t1_mem0 <= t1_t1

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	t1_t1_mem1 += MAIN_MEM_r[1]
	S += t1_t1_mem1 <= t1_t1

	t1_t2 = S.Task('t1_t2', length=4, delay_cost=1)
	t1_t2 += alt(MAS)
	t1_t2_in = S.Task('t1_t2_in', length=1, delay_cost=1)
	t1_t2_in += alt(MAS_in)
	S += t1_t2_in*MAS_in[0]<=t1_t2*MAS[0]

	S += t1_t2_in*MAS_in[1]<=t1_t2*MAS[1]

	S += t1_t2_in*MAS_in[2]<=t1_t2*MAS[2]

	S += t1_t2_in*MAS_in[3]<=t1_t2*MAS[3]

	S += t1_t2_in*MAS_in[4]<=t1_t2*MAS[4]

	S += t1_t2_in*MAS_in[5]<=t1_t2*MAS[5]

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	t1_t2_mem0 += MAIN_MEM_r[0]
	S += t1_t2_mem0 <= t1_t2

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	t1_t2_mem1 += MAIN_MEM_r[1]
	S += t1_t2_mem1 <= t1_t2

	t1_t3 = S.Task('t1_t3', length=4, delay_cost=1)
	t1_t3 += alt(MAS)
	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	t1_t3_in += alt(MAS_in)
	S += t1_t3_in*MAS_in[0]<=t1_t3*MAS[0]

	S += t1_t3_in*MAS_in[1]<=t1_t3*MAS[1]

	S += t1_t3_in*MAS_in[2]<=t1_t3*MAS[2]

	S += t1_t3_in*MAS_in[3]<=t1_t3*MAS[3]

	S += t1_t3_in*MAS_in[4]<=t1_t3*MAS[4]

	S += t1_t3_in*MAS_in[5]<=t1_t3*MAS[5]

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	t1_t3_mem0 += MAIN_MEM_r[0]
	S += t1_t3_mem0 <= t1_t3

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	t1_t3_mem1 += MAIN_MEM_r[1]
	S += t1_t3_mem1 <= t1_t3

	t2_t0 = S.Task('t2_t0', length=10, delay_cost=1)
	t2_t0 += alt(MM)
	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	t2_t0_in += alt(MM_in)
	S += t2_t0_in*MM_in[0]<=t2_t0*MM[0]
	S += t2_t0_in*MM_in[1]<=t2_t0*MM[1]
	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	t2_t0_mem0 += MAIN_MEM_r[0]
	S += t2_t0_mem0 <= t2_t0

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	t2_t0_mem1 += MAIN_MEM_r[1]
	S += t2_t0_mem1 <= t2_t0

	t2_t1 = S.Task('t2_t1', length=10, delay_cost=1)
	t2_t1 += alt(MM)
	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	t2_t1_in += alt(MM_in)
	S += t2_t1_in*MM_in[0]<=t2_t1*MM[0]
	S += t2_t1_in*MM_in[1]<=t2_t1*MM[1]
	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	t2_t1_mem0 += MAIN_MEM_r[0]
	S += t2_t1_mem0 <= t2_t1

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	t2_t1_mem1 += MAIN_MEM_r[1]
	S += t2_t1_mem1 <= t2_t1

	t2_t2 = S.Task('t2_t2', length=4, delay_cost=1)
	t2_t2 += alt(MAS)
	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	t2_t2_in += alt(MAS_in)
	S += t2_t2_in*MAS_in[0]<=t2_t2*MAS[0]

	S += t2_t2_in*MAS_in[1]<=t2_t2*MAS[1]

	S += t2_t2_in*MAS_in[2]<=t2_t2*MAS[2]

	S += t2_t2_in*MAS_in[3]<=t2_t2*MAS[3]

	S += t2_t2_in*MAS_in[4]<=t2_t2*MAS[4]

	S += t2_t2_in*MAS_in[5]<=t2_t2*MAS[5]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	t2_t2_mem0 += MAIN_MEM_r[0]
	S += t2_t2_mem0 <= t2_t2

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	t2_t2_mem1 += MAIN_MEM_r[1]
	S += t2_t2_mem1 <= t2_t2

	t2_t3 = S.Task('t2_t3', length=4, delay_cost=1)
	t2_t3 += alt(MAS)
	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	t2_t3_in += alt(MAS_in)
	S += t2_t3_in*MAS_in[0]<=t2_t3*MAS[0]

	S += t2_t3_in*MAS_in[1]<=t2_t3*MAS[1]

	S += t2_t3_in*MAS_in[2]<=t2_t3*MAS[2]

	S += t2_t3_in*MAS_in[3]<=t2_t3*MAS[3]

	S += t2_t3_in*MAS_in[4]<=t2_t3*MAS[4]

	S += t2_t3_in*MAS_in[5]<=t2_t3*MAS[5]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	t2_t3_mem0 += MAIN_MEM_r[0]
	S += t2_t3_mem0 <= t2_t3

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	t2_t3_mem1 += MAIN_MEM_r[1]
	S += t2_t3_mem1 <= t2_t3

	t0_t0 = S.Task('t0_t0', length=10, delay_cost=1)
	t0_t0 += alt(MM)
	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	t0_t0_in += alt(MM_in)
	S += t0_t0_in*MM_in[0]<=t0_t0*MM[0]
	S += t0_t0_in*MM_in[1]<=t0_t0*MM[1]
	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	t0_t0_mem0 += MAIN_MEM_r[0]
	S += t0_t0_mem0 <= t0_t0

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	t0_t0_mem1 += MAIN_MEM_r[1]
	S += t0_t0_mem1 <= t0_t0

	t0_t1 = S.Task('t0_t1', length=10, delay_cost=1)
	t0_t1 += alt(MM)
	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	t0_t1_in += alt(MM_in)
	S += t0_t1_in*MM_in[0]<=t0_t1*MM[0]
	S += t0_t1_in*MM_in[1]<=t0_t1*MM[1]
	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	t0_t1_mem0 += MAIN_MEM_r[0]
	S += t0_t1_mem0 <= t0_t1

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	t0_t1_mem1 += MAIN_MEM_r[1]
	S += t0_t1_mem1 <= t0_t1

	t0_t2 = S.Task('t0_t2', length=4, delay_cost=1)
	t0_t2 += alt(MAS)
	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	t0_t2_in += alt(MAS_in)
	S += t0_t2_in*MAS_in[0]<=t0_t2*MAS[0]

	S += t0_t2_in*MAS_in[1]<=t0_t2*MAS[1]

	S += t0_t2_in*MAS_in[2]<=t0_t2*MAS[2]

	S += t0_t2_in*MAS_in[3]<=t0_t2*MAS[3]

	S += t0_t2_in*MAS_in[4]<=t0_t2*MAS[4]

	S += t0_t2_in*MAS_in[5]<=t0_t2*MAS[5]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	t0_t2_mem0 += MAIN_MEM_r[0]
	S += t0_t2_mem0 <= t0_t2

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	t0_t2_mem1 += MAIN_MEM_r[1]
	S += t0_t2_mem1 <= t0_t2

	t0_t3 = S.Task('t0_t3', length=4, delay_cost=1)
	t0_t3 += alt(MAS)
	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	t0_t3_in += alt(MAS_in)
	S += t0_t3_in*MAS_in[0]<=t0_t3*MAS[0]

	S += t0_t3_in*MAS_in[1]<=t0_t3*MAS[1]

	S += t0_t3_in*MAS_in[2]<=t0_t3*MAS[2]

	S += t0_t3_in*MAS_in[3]<=t0_t3*MAS[3]

	S += t0_t3_in*MAS_in[4]<=t0_t3*MAS[4]

	S += t0_t3_in*MAS_in[5]<=t0_t3*MAS[5]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	t0_t3_mem0 += MAIN_MEM_r[0]
	S += t0_t3_mem0 <= t0_t3

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	t0_t3_mem1 += MAIN_MEM_r[1]
	S += t0_t3_mem1 <= t0_t3

	t4_t0_t0 = S.Task('t4_t0_t0', length=10, delay_cost=1)
	t4_t0_t0 += alt(MM)
	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	t4_t0_t0_in += alt(MM_in)
	S += t4_t0_t0_in*MM_in[0]<=t4_t0_t0*MM[0]
	S += t4_t0_t0_in*MM_in[1]<=t4_t0_t0*MM[1]
	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	t4_t0_t0_mem0 += MAIN_MEM_r[0]
	S += t4_t0_t0_mem0 <= t4_t0_t0

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	t4_t0_t0_mem1 += MAIN_MEM_r[1]
	S += t4_t0_t0_mem1 <= t4_t0_t0

	t4_t0_t1 = S.Task('t4_t0_t1', length=10, delay_cost=1)
	t4_t0_t1 += alt(MM)
	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	t4_t0_t1_in += alt(MM_in)
	S += t4_t0_t1_in*MM_in[0]<=t4_t0_t1*MM[0]
	S += t4_t0_t1_in*MM_in[1]<=t4_t0_t1*MM[1]
	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	t4_t0_t1_mem0 += MAIN_MEM_r[0]
	S += t4_t0_t1_mem0 <= t4_t0_t1

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	t4_t0_t1_mem1 += MAIN_MEM_r[1]
	S += t4_t0_t1_mem1 <= t4_t0_t1

	t4_t0_t2 = S.Task('t4_t0_t2', length=4, delay_cost=1)
	t4_t0_t2 += alt(MAS)
	t4_t0_t2_in = S.Task('t4_t0_t2_in', length=1, delay_cost=1)
	t4_t0_t2_in += alt(MAS_in)
	S += t4_t0_t2_in*MAS_in[0]<=t4_t0_t2*MAS[0]

	S += t4_t0_t2_in*MAS_in[1]<=t4_t0_t2*MAS[1]

	S += t4_t0_t2_in*MAS_in[2]<=t4_t0_t2*MAS[2]

	S += t4_t0_t2_in*MAS_in[3]<=t4_t0_t2*MAS[3]

	S += t4_t0_t2_in*MAS_in[4]<=t4_t0_t2*MAS[4]

	S += t4_t0_t2_in*MAS_in[5]<=t4_t0_t2*MAS[5]

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	t4_t0_t2_mem0 += MAIN_MEM_r[0]
	S += t4_t0_t2_mem0 <= t4_t0_t2

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	t4_t0_t2_mem1 += MAIN_MEM_r[1]
	S += t4_t0_t2_mem1 <= t4_t0_t2

	t4_t0_t3 = S.Task('t4_t0_t3', length=4, delay_cost=1)
	t4_t0_t3 += alt(MAS)
	t4_t0_t3_in = S.Task('t4_t0_t3_in', length=1, delay_cost=1)
	t4_t0_t3_in += alt(MAS_in)
	S += t4_t0_t3_in*MAS_in[0]<=t4_t0_t3*MAS[0]

	S += t4_t0_t3_in*MAS_in[1]<=t4_t0_t3*MAS[1]

	S += t4_t0_t3_in*MAS_in[2]<=t4_t0_t3*MAS[2]

	S += t4_t0_t3_in*MAS_in[3]<=t4_t0_t3*MAS[3]

	S += t4_t0_t3_in*MAS_in[4]<=t4_t0_t3*MAS[4]

	S += t4_t0_t3_in*MAS_in[5]<=t4_t0_t3*MAS[5]

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	t4_t0_t3_mem0 += MAIN_MEM_r[0]
	S += t4_t0_t3_mem0 <= t4_t0_t3

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	t4_t0_t3_mem1 += MAIN_MEM_r[1]
	S += t4_t0_t3_mem1 <= t4_t0_t3

	t4_t1_t0 = S.Task('t4_t1_t0', length=10, delay_cost=1)
	t4_t1_t0 += alt(MM)
	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	t4_t1_t0_in += alt(MM_in)
	S += t4_t1_t0_in*MM_in[0]<=t4_t1_t0*MM[0]
	S += t4_t1_t0_in*MM_in[1]<=t4_t1_t0*MM[1]
	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	t4_t1_t0_mem0 += MAIN_MEM_r[0]
	S += t4_t1_t0_mem0 <= t4_t1_t0

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	t4_t1_t0_mem1 += MAIN_MEM_r[1]
	S += t4_t1_t0_mem1 <= t4_t1_t0

	t4_t1_t1 = S.Task('t4_t1_t1', length=10, delay_cost=1)
	t4_t1_t1 += alt(MM)
	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	t4_t1_t1_in += alt(MM_in)
	S += t4_t1_t1_in*MM_in[0]<=t4_t1_t1*MM[0]
	S += t4_t1_t1_in*MM_in[1]<=t4_t1_t1*MM[1]
	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	t4_t1_t1_mem0 += MAIN_MEM_r[0]
	S += t4_t1_t1_mem0 <= t4_t1_t1

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	t4_t1_t1_mem1 += MAIN_MEM_r[1]
	S += t4_t1_t1_mem1 <= t4_t1_t1

	t4_t1_t2 = S.Task('t4_t1_t2', length=4, delay_cost=1)
	t4_t1_t2 += alt(MAS)
	t4_t1_t2_in = S.Task('t4_t1_t2_in', length=1, delay_cost=1)
	t4_t1_t2_in += alt(MAS_in)
	S += t4_t1_t2_in*MAS_in[0]<=t4_t1_t2*MAS[0]

	S += t4_t1_t2_in*MAS_in[1]<=t4_t1_t2*MAS[1]

	S += t4_t1_t2_in*MAS_in[2]<=t4_t1_t2*MAS[2]

	S += t4_t1_t2_in*MAS_in[3]<=t4_t1_t2*MAS[3]

	S += t4_t1_t2_in*MAS_in[4]<=t4_t1_t2*MAS[4]

	S += t4_t1_t2_in*MAS_in[5]<=t4_t1_t2*MAS[5]

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	t4_t1_t2_mem0 += MAIN_MEM_r[0]
	S += t4_t1_t2_mem0 <= t4_t1_t2

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	t4_t1_t2_mem1 += MAIN_MEM_r[1]
	S += t4_t1_t2_mem1 <= t4_t1_t2

	t4_t1_t3 = S.Task('t4_t1_t3', length=4, delay_cost=1)
	t4_t1_t3 += alt(MAS)
	t4_t1_t3_in = S.Task('t4_t1_t3_in', length=1, delay_cost=1)
	t4_t1_t3_in += alt(MAS_in)
	S += t4_t1_t3_in*MAS_in[0]<=t4_t1_t3*MAS[0]

	S += t4_t1_t3_in*MAS_in[1]<=t4_t1_t3*MAS[1]

	S += t4_t1_t3_in*MAS_in[2]<=t4_t1_t3*MAS[2]

	S += t4_t1_t3_in*MAS_in[3]<=t4_t1_t3*MAS[3]

	S += t4_t1_t3_in*MAS_in[4]<=t4_t1_t3*MAS[4]

	S += t4_t1_t3_in*MAS_in[5]<=t4_t1_t3*MAS[5]

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	t4_t1_t3_mem0 += MAIN_MEM_r[0]
	S += t4_t1_t3_mem0 <= t4_t1_t3

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	t4_t1_t3_mem1 += MAIN_MEM_r[1]
	S += t4_t1_t3_mem1 <= t4_t1_t3

	t4_t2_t0 = S.Task('t4_t2_t0', length=10, delay_cost=1)
	t4_t2_t0 += alt(MM)
	t4_t2_t0_in = S.Task('t4_t2_t0_in', length=1, delay_cost=1)
	t4_t2_t0_in += alt(MM_in)
	S += t4_t2_t0_in*MM_in[0]<=t4_t2_t0*MM[0]
	S += t4_t2_t0_in*MM_in[1]<=t4_t2_t0*MM[1]
	t4_t2_t0_mem0 = S.Task('t4_t2_t0_mem0', length=1, delay_cost=1)
	t4_t2_t0_mem0 += MAIN_MEM_r[0]
	S += t4_t2_t0_mem0 <= t4_t2_t0

	t4_t2_t0_mem1 = S.Task('t4_t2_t0_mem1', length=1, delay_cost=1)
	t4_t2_t0_mem1 += MAIN_MEM_r[1]
	S += t4_t2_t0_mem1 <= t4_t2_t0

	t4_t2_t1 = S.Task('t4_t2_t1', length=10, delay_cost=1)
	t4_t2_t1 += alt(MM)
	t4_t2_t1_in = S.Task('t4_t2_t1_in', length=1, delay_cost=1)
	t4_t2_t1_in += alt(MM_in)
	S += t4_t2_t1_in*MM_in[0]<=t4_t2_t1*MM[0]
	S += t4_t2_t1_in*MM_in[1]<=t4_t2_t1*MM[1]
	t4_t2_t1_mem0 = S.Task('t4_t2_t1_mem0', length=1, delay_cost=1)
	t4_t2_t1_mem0 += MAIN_MEM_r[0]
	S += t4_t2_t1_mem0 <= t4_t2_t1

	t4_t2_t1_mem1 = S.Task('t4_t2_t1_mem1', length=1, delay_cost=1)
	t4_t2_t1_mem1 += MAIN_MEM_r[1]
	S += t4_t2_t1_mem1 <= t4_t2_t1

	t4_t2_t2 = S.Task('t4_t2_t2', length=4, delay_cost=1)
	t4_t2_t2 += alt(MAS)
	t4_t2_t2_in = S.Task('t4_t2_t2_in', length=1, delay_cost=1)
	t4_t2_t2_in += alt(MAS_in)
	S += t4_t2_t2_in*MAS_in[0]<=t4_t2_t2*MAS[0]

	S += t4_t2_t2_in*MAS_in[1]<=t4_t2_t2*MAS[1]

	S += t4_t2_t2_in*MAS_in[2]<=t4_t2_t2*MAS[2]

	S += t4_t2_t2_in*MAS_in[3]<=t4_t2_t2*MAS[3]

	S += t4_t2_t2_in*MAS_in[4]<=t4_t2_t2*MAS[4]

	S += t4_t2_t2_in*MAS_in[5]<=t4_t2_t2*MAS[5]

	t4_t2_t2_mem0 = S.Task('t4_t2_t2_mem0', length=1, delay_cost=1)
	t4_t2_t2_mem0 += MAIN_MEM_r[0]
	S += t4_t2_t2_mem0 <= t4_t2_t2

	t4_t2_t2_mem1 = S.Task('t4_t2_t2_mem1', length=1, delay_cost=1)
	t4_t2_t2_mem1 += MAIN_MEM_r[1]
	S += t4_t2_t2_mem1 <= t4_t2_t2

	t4_t2_t3 = S.Task('t4_t2_t3', length=4, delay_cost=1)
	t4_t2_t3 += alt(MAS)
	t4_t2_t3_in = S.Task('t4_t2_t3_in', length=1, delay_cost=1)
	t4_t2_t3_in += alt(MAS_in)
	S += t4_t2_t3_in*MAS_in[0]<=t4_t2_t3*MAS[0]

	S += t4_t2_t3_in*MAS_in[1]<=t4_t2_t3*MAS[1]

	S += t4_t2_t3_in*MAS_in[2]<=t4_t2_t3*MAS[2]

	S += t4_t2_t3_in*MAS_in[3]<=t4_t2_t3*MAS[3]

	S += t4_t2_t3_in*MAS_in[4]<=t4_t2_t3*MAS[4]

	S += t4_t2_t3_in*MAS_in[5]<=t4_t2_t3*MAS[5]

	t4_t2_t3_mem0 = S.Task('t4_t2_t3_mem0', length=1, delay_cost=1)
	t4_t2_t3_mem0 += MAIN_MEM_r[0]
	S += t4_t2_t3_mem0 <= t4_t2_t3

	t4_t2_t3_mem1 = S.Task('t4_t2_t3_mem1', length=1, delay_cost=1)
	t4_t2_t3_mem1 += MAIN_MEM_r[1]
	S += t4_t2_t3_mem1 <= t4_t2_t3

	t4_t40 = S.Task('t4_t40', length=4, delay_cost=1)
	t4_t40 += alt(MAS)
	t4_t40_in = S.Task('t4_t40_in', length=1, delay_cost=1)
	t4_t40_in += alt(MAS_in)
	S += t4_t40_in*MAS_in[0]<=t4_t40*MAS[0]

	S += t4_t40_in*MAS_in[1]<=t4_t40*MAS[1]

	S += t4_t40_in*MAS_in[2]<=t4_t40*MAS[2]

	S += t4_t40_in*MAS_in[3]<=t4_t40*MAS[3]

	S += t4_t40_in*MAS_in[4]<=t4_t40*MAS[4]

	S += t4_t40_in*MAS_in[5]<=t4_t40*MAS[5]

	t4_t40_mem0 = S.Task('t4_t40_mem0', length=1, delay_cost=1)
	t4_t40_mem0 += MAIN_MEM_r[0]
	S += t4_t40_mem0 <= t4_t40

	t4_t40_mem1 = S.Task('t4_t40_mem1', length=1, delay_cost=1)
	t4_t40_mem1 += MAIN_MEM_r[1]
	S += t4_t40_mem1 <= t4_t40

	t4_t41 = S.Task('t4_t41', length=4, delay_cost=1)
	t4_t41 += alt(MAS)
	t4_t41_in = S.Task('t4_t41_in', length=1, delay_cost=1)
	t4_t41_in += alt(MAS_in)
	S += t4_t41_in*MAS_in[0]<=t4_t41*MAS[0]

	S += t4_t41_in*MAS_in[1]<=t4_t41*MAS[1]

	S += t4_t41_in*MAS_in[2]<=t4_t41*MAS[2]

	S += t4_t41_in*MAS_in[3]<=t4_t41*MAS[3]

	S += t4_t41_in*MAS_in[4]<=t4_t41*MAS[4]

	S += t4_t41_in*MAS_in[5]<=t4_t41*MAS[5]

	t4_t41_mem0 = S.Task('t4_t41_mem0', length=1, delay_cost=1)
	t4_t41_mem0 += MAIN_MEM_r[0]
	S += t4_t41_mem0 <= t4_t41

	t4_t41_mem1 = S.Task('t4_t41_mem1', length=1, delay_cost=1)
	t4_t41_mem1 += MAIN_MEM_r[1]
	S += t4_t41_mem1 <= t4_t41

	t4_t50 = S.Task('t4_t50', length=4, delay_cost=1)
	t4_t50 += alt(MAS)
	t4_t50_in = S.Task('t4_t50_in', length=1, delay_cost=1)
	t4_t50_in += alt(MAS_in)
	S += t4_t50_in*MAS_in[0]<=t4_t50*MAS[0]

	S += t4_t50_in*MAS_in[1]<=t4_t50*MAS[1]

	S += t4_t50_in*MAS_in[2]<=t4_t50*MAS[2]

	S += t4_t50_in*MAS_in[3]<=t4_t50*MAS[3]

	S += t4_t50_in*MAS_in[4]<=t4_t50*MAS[4]

	S += t4_t50_in*MAS_in[5]<=t4_t50*MAS[5]

	t4_t50_mem0 = S.Task('t4_t50_mem0', length=1, delay_cost=1)
	t4_t50_mem0 += MAIN_MEM_r[0]
	S += t4_t50_mem0 <= t4_t50

	t4_t50_mem1 = S.Task('t4_t50_mem1', length=1, delay_cost=1)
	t4_t50_mem1 += MAIN_MEM_r[1]
	S += t4_t50_mem1 <= t4_t50

	t4_t51 = S.Task('t4_t51', length=4, delay_cost=1)
	t4_t51 += alt(MAS)
	t4_t51_in = S.Task('t4_t51_in', length=1, delay_cost=1)
	t4_t51_in += alt(MAS_in)
	S += t4_t51_in*MAS_in[0]<=t4_t51*MAS[0]

	S += t4_t51_in*MAS_in[1]<=t4_t51*MAS[1]

	S += t4_t51_in*MAS_in[2]<=t4_t51*MAS[2]

	S += t4_t51_in*MAS_in[3]<=t4_t51*MAS[3]

	S += t4_t51_in*MAS_in[4]<=t4_t51*MAS[4]

	S += t4_t51_in*MAS_in[5]<=t4_t51*MAS[5]

	t4_t51_mem0 = S.Task('t4_t51_mem0', length=1, delay_cost=1)
	t4_t51_mem0 += MAIN_MEM_r[0]
	S += t4_t51_mem0 <= t4_t51

	t4_t51_mem1 = S.Task('t4_t51_mem1', length=1, delay_cost=1)
	t4_t51_mem1 += MAIN_MEM_r[1]
	S += t4_t51_mem1 <= t4_t51

	t4_t8_t0 = S.Task('t4_t8_t0', length=10, delay_cost=1)
	t4_t8_t0 += alt(MM)
	t4_t8_t0_in = S.Task('t4_t8_t0_in', length=1, delay_cost=1)
	t4_t8_t0_in += alt(MM_in)
	S += t4_t8_t0_in*MM_in[0]<=t4_t8_t0*MM[0]
	S += t4_t8_t0_in*MM_in[1]<=t4_t8_t0*MM[1]
	t4_t8_t0_mem0 = S.Task('t4_t8_t0_mem0', length=1, delay_cost=1)
	t4_t8_t0_mem0 += MAIN_MEM_r[0]
	S += t4_t8_t0_mem0 <= t4_t8_t0

	t4_t8_t0_mem1 = S.Task('t4_t8_t0_mem1', length=1, delay_cost=1)
	t4_t8_t0_mem1 += MAIN_MEM_r[1]
	S += t4_t8_t0_mem1 <= t4_t8_t0

	t4_t8_t1 = S.Task('t4_t8_t1', length=10, delay_cost=1)
	t4_t8_t1 += alt(MM)
	t4_t8_t1_in = S.Task('t4_t8_t1_in', length=1, delay_cost=1)
	t4_t8_t1_in += alt(MM_in)
	S += t4_t8_t1_in*MM_in[0]<=t4_t8_t1*MM[0]
	S += t4_t8_t1_in*MM_in[1]<=t4_t8_t1*MM[1]
	t4_t8_t1_mem0 = S.Task('t4_t8_t1_mem0', length=1, delay_cost=1)
	t4_t8_t1_mem0 += MAIN_MEM_r[0]
	S += t4_t8_t1_mem0 <= t4_t8_t1

	t4_t8_t1_mem1 = S.Task('t4_t8_t1_mem1', length=1, delay_cost=1)
	t4_t8_t1_mem1 += MAIN_MEM_r[1]
	S += t4_t8_t1_mem1 <= t4_t8_t1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage4MAS6/SPARSE/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

