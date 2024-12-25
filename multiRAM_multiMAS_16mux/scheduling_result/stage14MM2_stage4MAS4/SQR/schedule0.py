from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=14)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	c_t0_a1_0 = S.Task('c_t0_a1_0', length=4, delay_cost=1)
	c_t0_a1_0 += alt(MAS)
	c_t0_a1_0_in = S.Task('c_t0_a1_0_in', length=1, delay_cost=1)
	c_t0_a1_0_in += alt(MAS_in)
	S += c_t0_a1_0_in*MAS_in[0]<=c_t0_a1_0*MAS[0]

	S += c_t0_a1_0_in*MAS_in[1]<=c_t0_a1_0*MAS[1]

	S += c_t0_a1_0_in*MAS_in[2]<=c_t0_a1_0*MAS[2]

	S += c_t0_a1_0_in*MAS_in[3]<=c_t0_a1_0*MAS[3]

	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	c_t0_a1_0_mem0 += MAIN_MEM_r[0]
	S += c_t0_a1_0_mem0 <= c_t0_a1_0

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	c_t0_a1_0_mem1 += MAIN_MEM_r[1]
	S += c_t0_a1_0_mem1 <= c_t0_a1_0

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=4, delay_cost=1)
	c_t0_a1_1 += alt(MAS)
	c_t0_a1_1_in = S.Task('c_t0_a1_1_in', length=1, delay_cost=1)
	c_t0_a1_1_in += alt(MAS_in)
	S += c_t0_a1_1_in*MAS_in[0]<=c_t0_a1_1*MAS[0]

	S += c_t0_a1_1_in*MAS_in[1]<=c_t0_a1_1*MAS[1]

	S += c_t0_a1_1_in*MAS_in[2]<=c_t0_a1_1*MAS[2]

	S += c_t0_a1_1_in*MAS_in[3]<=c_t0_a1_1*MAS[3]

	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	c_t0_a1_1_mem0 += MAIN_MEM_r[0]
	S += c_t0_a1_1_mem0 <= c_t0_a1_1

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	c_t0_a1_1_mem1 += MAIN_MEM_r[1]
	S += c_t0_a1_1_mem1 <= c_t0_a1_1

	c_t0_t10 = S.Task('c_t0_t10', length=4, delay_cost=1)
	c_t0_t10 += alt(MAS)
	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	c_t0_t10_in += alt(MAS_in)
	S += c_t0_t10_in*MAS_in[0]<=c_t0_t10*MAS[0]

	S += c_t0_t10_in*MAS_in[1]<=c_t0_t10*MAS[1]

	S += c_t0_t10_in*MAS_in[2]<=c_t0_t10*MAS[2]

	S += c_t0_t10_in*MAS_in[3]<=c_t0_t10*MAS[3]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	c_t0_t10_mem0 += MAIN_MEM_r[0]
	S += c_t0_t10_mem0 <= c_t0_t10

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	c_t0_t10_mem1 += MAIN_MEM_r[1]
	S += c_t0_t10_mem1 <= c_t0_t10

	c_t0_t11 = S.Task('c_t0_t11', length=4, delay_cost=1)
	c_t0_t11 += alt(MAS)
	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	c_t0_t11_in += alt(MAS_in)
	S += c_t0_t11_in*MAS_in[0]<=c_t0_t11*MAS[0]

	S += c_t0_t11_in*MAS_in[1]<=c_t0_t11*MAS[1]

	S += c_t0_t11_in*MAS_in[2]<=c_t0_t11*MAS[2]

	S += c_t0_t11_in*MAS_in[3]<=c_t0_t11*MAS[3]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	c_t0_t11_mem0 += MAIN_MEM_r[0]
	S += c_t0_t11_mem0 <= c_t0_t11

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	c_t0_t11_mem1 += MAIN_MEM_r[1]
	S += c_t0_t11_mem1 <= c_t0_t11

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=14, delay_cost=1)
	c_t0_t3_t0 += alt(MM)
	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	c_t0_t3_t0_in += alt(MM_in)
	S += c_t0_t3_t0_in*MM_in[0]<=c_t0_t3_t0*MM[0]
	S += c_t0_t3_t0_in*MM_in[1]<=c_t0_t3_t0*MM[1]
	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	c_t0_t3_t0_mem0 += MAIN_MEM_r[0]
	S += c_t0_t3_t0_mem0 <= c_t0_t3_t0

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	c_t0_t3_t0_mem1 += MAIN_MEM_r[1]
	S += c_t0_t3_t0_mem1 <= c_t0_t3_t0

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=14, delay_cost=1)
	c_t0_t3_t1 += alt(MM)
	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	c_t0_t3_t1_in += alt(MM_in)
	S += c_t0_t3_t1_in*MM_in[0]<=c_t0_t3_t1*MM[0]
	S += c_t0_t3_t1_in*MM_in[1]<=c_t0_t3_t1*MM[1]
	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	c_t0_t3_t1_mem0 += MAIN_MEM_r[0]
	S += c_t0_t3_t1_mem0 <= c_t0_t3_t1

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	c_t0_t3_t1_mem1 += MAIN_MEM_r[1]
	S += c_t0_t3_t1_mem1 <= c_t0_t3_t1

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=4, delay_cost=1)
	c_t0_t3_t2 += alt(MAS)
	c_t0_t3_t2_in = S.Task('c_t0_t3_t2_in', length=1, delay_cost=1)
	c_t0_t3_t2_in += alt(MAS_in)
	S += c_t0_t3_t2_in*MAS_in[0]<=c_t0_t3_t2*MAS[0]

	S += c_t0_t3_t2_in*MAS_in[1]<=c_t0_t3_t2*MAS[1]

	S += c_t0_t3_t2_in*MAS_in[2]<=c_t0_t3_t2*MAS[2]

	S += c_t0_t3_t2_in*MAS_in[3]<=c_t0_t3_t2*MAS[3]

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	c_t0_t3_t2_mem0 += MAIN_MEM_r[0]
	S += c_t0_t3_t2_mem0 <= c_t0_t3_t2

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	c_t0_t3_t2_mem1 += MAIN_MEM_r[1]
	S += c_t0_t3_t2_mem1 <= c_t0_t3_t2

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=4, delay_cost=1)
	c_t0_t3_t3 += alt(MAS)
	c_t0_t3_t3_in = S.Task('c_t0_t3_t3_in', length=1, delay_cost=1)
	c_t0_t3_t3_in += alt(MAS_in)
	S += c_t0_t3_t3_in*MAS_in[0]<=c_t0_t3_t3*MAS[0]

	S += c_t0_t3_t3_in*MAS_in[1]<=c_t0_t3_t3*MAS[1]

	S += c_t0_t3_t3_in*MAS_in[2]<=c_t0_t3_t3*MAS[2]

	S += c_t0_t3_t3_in*MAS_in[3]<=c_t0_t3_t3*MAS[3]

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	c_t0_t3_t3_mem0 += MAIN_MEM_r[0]
	S += c_t0_t3_t3_mem0 <= c_t0_t3_t3

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	c_t0_t3_t3_mem1 += MAIN_MEM_r[1]
	S += c_t0_t3_t3_mem1 <= c_t0_t3_t3

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=4, delay_cost=1)
	c_t1_a1_0 += alt(MAS)
	c_t1_a1_0_in = S.Task('c_t1_a1_0_in', length=1, delay_cost=1)
	c_t1_a1_0_in += alt(MAS_in)
	S += c_t1_a1_0_in*MAS_in[0]<=c_t1_a1_0*MAS[0]

	S += c_t1_a1_0_in*MAS_in[1]<=c_t1_a1_0*MAS[1]

	S += c_t1_a1_0_in*MAS_in[2]<=c_t1_a1_0*MAS[2]

	S += c_t1_a1_0_in*MAS_in[3]<=c_t1_a1_0*MAS[3]

	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	c_t1_a1_0_mem0 += MAIN_MEM_r[0]
	S += c_t1_a1_0_mem0 <= c_t1_a1_0

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	c_t1_a1_0_mem1 += MAIN_MEM_r[1]
	S += c_t1_a1_0_mem1 <= c_t1_a1_0

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=4, delay_cost=1)
	c_t1_a1_1 += alt(MAS)
	c_t1_a1_1_in = S.Task('c_t1_a1_1_in', length=1, delay_cost=1)
	c_t1_a1_1_in += alt(MAS_in)
	S += c_t1_a1_1_in*MAS_in[0]<=c_t1_a1_1*MAS[0]

	S += c_t1_a1_1_in*MAS_in[1]<=c_t1_a1_1*MAS[1]

	S += c_t1_a1_1_in*MAS_in[2]<=c_t1_a1_1*MAS[2]

	S += c_t1_a1_1_in*MAS_in[3]<=c_t1_a1_1*MAS[3]

	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	c_t1_a1_1_mem0 += MAIN_MEM_r[0]
	S += c_t1_a1_1_mem0 <= c_t1_a1_1

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	c_t1_a1_1_mem1 += MAIN_MEM_r[1]
	S += c_t1_a1_1_mem1 <= c_t1_a1_1

	c_t1_t10 = S.Task('c_t1_t10', length=4, delay_cost=1)
	c_t1_t10 += alt(MAS)
	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	c_t1_t10_in += alt(MAS_in)
	S += c_t1_t10_in*MAS_in[0]<=c_t1_t10*MAS[0]

	S += c_t1_t10_in*MAS_in[1]<=c_t1_t10*MAS[1]

	S += c_t1_t10_in*MAS_in[2]<=c_t1_t10*MAS[2]

	S += c_t1_t10_in*MAS_in[3]<=c_t1_t10*MAS[3]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	c_t1_t10_mem0 += MAIN_MEM_r[0]
	S += c_t1_t10_mem0 <= c_t1_t10

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	c_t1_t10_mem1 += MAIN_MEM_r[1]
	S += c_t1_t10_mem1 <= c_t1_t10

	c_t1_t11 = S.Task('c_t1_t11', length=4, delay_cost=1)
	c_t1_t11 += alt(MAS)
	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	c_t1_t11_in += alt(MAS_in)
	S += c_t1_t11_in*MAS_in[0]<=c_t1_t11*MAS[0]

	S += c_t1_t11_in*MAS_in[1]<=c_t1_t11*MAS[1]

	S += c_t1_t11_in*MAS_in[2]<=c_t1_t11*MAS[2]

	S += c_t1_t11_in*MAS_in[3]<=c_t1_t11*MAS[3]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	c_t1_t11_mem0 += MAIN_MEM_r[0]
	S += c_t1_t11_mem0 <= c_t1_t11

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	c_t1_t11_mem1 += MAIN_MEM_r[1]
	S += c_t1_t11_mem1 <= c_t1_t11

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=14, delay_cost=1)
	c_t1_t3_t0 += alt(MM)
	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	c_t1_t3_t0_in += alt(MM_in)
	S += c_t1_t3_t0_in*MM_in[0]<=c_t1_t3_t0*MM[0]
	S += c_t1_t3_t0_in*MM_in[1]<=c_t1_t3_t0*MM[1]
	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	c_t1_t3_t0_mem0 += MAIN_MEM_r[0]
	S += c_t1_t3_t0_mem0 <= c_t1_t3_t0

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	c_t1_t3_t0_mem1 += MAIN_MEM_r[1]
	S += c_t1_t3_t0_mem1 <= c_t1_t3_t0

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=14, delay_cost=1)
	c_t1_t3_t1 += alt(MM)
	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	c_t1_t3_t1_in += alt(MM_in)
	S += c_t1_t3_t1_in*MM_in[0]<=c_t1_t3_t1*MM[0]
	S += c_t1_t3_t1_in*MM_in[1]<=c_t1_t3_t1*MM[1]
	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	c_t1_t3_t1_mem0 += MAIN_MEM_r[0]
	S += c_t1_t3_t1_mem0 <= c_t1_t3_t1

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	c_t1_t3_t1_mem1 += MAIN_MEM_r[1]
	S += c_t1_t3_t1_mem1 <= c_t1_t3_t1

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=4, delay_cost=1)
	c_t1_t3_t2 += alt(MAS)
	c_t1_t3_t2_in = S.Task('c_t1_t3_t2_in', length=1, delay_cost=1)
	c_t1_t3_t2_in += alt(MAS_in)
	S += c_t1_t3_t2_in*MAS_in[0]<=c_t1_t3_t2*MAS[0]

	S += c_t1_t3_t2_in*MAS_in[1]<=c_t1_t3_t2*MAS[1]

	S += c_t1_t3_t2_in*MAS_in[2]<=c_t1_t3_t2*MAS[2]

	S += c_t1_t3_t2_in*MAS_in[3]<=c_t1_t3_t2*MAS[3]

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	c_t1_t3_t2_mem0 += MAIN_MEM_r[0]
	S += c_t1_t3_t2_mem0 <= c_t1_t3_t2

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	c_t1_t3_t2_mem1 += MAIN_MEM_r[1]
	S += c_t1_t3_t2_mem1 <= c_t1_t3_t2

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=4, delay_cost=1)
	c_t1_t3_t3 += alt(MAS)
	c_t1_t3_t3_in = S.Task('c_t1_t3_t3_in', length=1, delay_cost=1)
	c_t1_t3_t3_in += alt(MAS_in)
	S += c_t1_t3_t3_in*MAS_in[0]<=c_t1_t3_t3*MAS[0]

	S += c_t1_t3_t3_in*MAS_in[1]<=c_t1_t3_t3*MAS[1]

	S += c_t1_t3_t3_in*MAS_in[2]<=c_t1_t3_t3*MAS[2]

	S += c_t1_t3_t3_in*MAS_in[3]<=c_t1_t3_t3*MAS[3]

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	c_t1_t3_t3_mem0 += MAIN_MEM_r[0]
	S += c_t1_t3_t3_mem0 <= c_t1_t3_t3

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	c_t1_t3_t3_mem1 += MAIN_MEM_r[1]
	S += c_t1_t3_t3_mem1 <= c_t1_t3_t3

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=4, delay_cost=1)
	c_t2_a1_0 += alt(MAS)
	c_t2_a1_0_in = S.Task('c_t2_a1_0_in', length=1, delay_cost=1)
	c_t2_a1_0_in += alt(MAS_in)
	S += c_t2_a1_0_in*MAS_in[0]<=c_t2_a1_0*MAS[0]

	S += c_t2_a1_0_in*MAS_in[1]<=c_t2_a1_0*MAS[1]

	S += c_t2_a1_0_in*MAS_in[2]<=c_t2_a1_0*MAS[2]

	S += c_t2_a1_0_in*MAS_in[3]<=c_t2_a1_0*MAS[3]

	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	c_t2_a1_0_mem0 += MAIN_MEM_r[0]
	S += c_t2_a1_0_mem0 <= c_t2_a1_0

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	c_t2_a1_0_mem1 += MAIN_MEM_r[1]
	S += c_t2_a1_0_mem1 <= c_t2_a1_0

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=4, delay_cost=1)
	c_t2_a1_1 += alt(MAS)
	c_t2_a1_1_in = S.Task('c_t2_a1_1_in', length=1, delay_cost=1)
	c_t2_a1_1_in += alt(MAS_in)
	S += c_t2_a1_1_in*MAS_in[0]<=c_t2_a1_1*MAS[0]

	S += c_t2_a1_1_in*MAS_in[1]<=c_t2_a1_1*MAS[1]

	S += c_t2_a1_1_in*MAS_in[2]<=c_t2_a1_1*MAS[2]

	S += c_t2_a1_1_in*MAS_in[3]<=c_t2_a1_1*MAS[3]

	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	c_t2_a1_1_mem0 += MAIN_MEM_r[0]
	S += c_t2_a1_1_mem0 <= c_t2_a1_1

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	c_t2_a1_1_mem1 += MAIN_MEM_r[1]
	S += c_t2_a1_1_mem1 <= c_t2_a1_1

	c_t2_t10 = S.Task('c_t2_t10', length=4, delay_cost=1)
	c_t2_t10 += alt(MAS)
	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	c_t2_t10_in += alt(MAS_in)
	S += c_t2_t10_in*MAS_in[0]<=c_t2_t10*MAS[0]

	S += c_t2_t10_in*MAS_in[1]<=c_t2_t10*MAS[1]

	S += c_t2_t10_in*MAS_in[2]<=c_t2_t10*MAS[2]

	S += c_t2_t10_in*MAS_in[3]<=c_t2_t10*MAS[3]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	c_t2_t10_mem0 += MAIN_MEM_r[0]
	S += c_t2_t10_mem0 <= c_t2_t10

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	c_t2_t10_mem1 += MAIN_MEM_r[1]
	S += c_t2_t10_mem1 <= c_t2_t10

	c_t2_t11 = S.Task('c_t2_t11', length=4, delay_cost=1)
	c_t2_t11 += alt(MAS)
	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	c_t2_t11_in += alt(MAS_in)
	S += c_t2_t11_in*MAS_in[0]<=c_t2_t11*MAS[0]

	S += c_t2_t11_in*MAS_in[1]<=c_t2_t11*MAS[1]

	S += c_t2_t11_in*MAS_in[2]<=c_t2_t11*MAS[2]

	S += c_t2_t11_in*MAS_in[3]<=c_t2_t11*MAS[3]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	c_t2_t11_mem0 += MAIN_MEM_r[0]
	S += c_t2_t11_mem0 <= c_t2_t11

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	c_t2_t11_mem1 += MAIN_MEM_r[1]
	S += c_t2_t11_mem1 <= c_t2_t11

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=14, delay_cost=1)
	c_t2_t3_t0 += alt(MM)
	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	c_t2_t3_t0_in += alt(MM_in)
	S += c_t2_t3_t0_in*MM_in[0]<=c_t2_t3_t0*MM[0]
	S += c_t2_t3_t0_in*MM_in[1]<=c_t2_t3_t0*MM[1]
	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	c_t2_t3_t0_mem0 += MAIN_MEM_r[0]
	S += c_t2_t3_t0_mem0 <= c_t2_t3_t0

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	c_t2_t3_t0_mem1 += MAIN_MEM_r[1]
	S += c_t2_t3_t0_mem1 <= c_t2_t3_t0

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=14, delay_cost=1)
	c_t2_t3_t1 += alt(MM)
	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	c_t2_t3_t1_in += alt(MM_in)
	S += c_t2_t3_t1_in*MM_in[0]<=c_t2_t3_t1*MM[0]
	S += c_t2_t3_t1_in*MM_in[1]<=c_t2_t3_t1*MM[1]
	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	c_t2_t3_t1_mem0 += MAIN_MEM_r[0]
	S += c_t2_t3_t1_mem0 <= c_t2_t3_t1

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	c_t2_t3_t1_mem1 += MAIN_MEM_r[1]
	S += c_t2_t3_t1_mem1 <= c_t2_t3_t1

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=4, delay_cost=1)
	c_t2_t3_t2 += alt(MAS)
	c_t2_t3_t2_in = S.Task('c_t2_t3_t2_in', length=1, delay_cost=1)
	c_t2_t3_t2_in += alt(MAS_in)
	S += c_t2_t3_t2_in*MAS_in[0]<=c_t2_t3_t2*MAS[0]

	S += c_t2_t3_t2_in*MAS_in[1]<=c_t2_t3_t2*MAS[1]

	S += c_t2_t3_t2_in*MAS_in[2]<=c_t2_t3_t2*MAS[2]

	S += c_t2_t3_t2_in*MAS_in[3]<=c_t2_t3_t2*MAS[3]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	c_t2_t3_t2_mem0 += MAIN_MEM_r[0]
	S += c_t2_t3_t2_mem0 <= c_t2_t3_t2

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	c_t2_t3_t2_mem1 += MAIN_MEM_r[1]
	S += c_t2_t3_t2_mem1 <= c_t2_t3_t2

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=4, delay_cost=1)
	c_t2_t3_t3 += alt(MAS)
	c_t2_t3_t3_in = S.Task('c_t2_t3_t3_in', length=1, delay_cost=1)
	c_t2_t3_t3_in += alt(MAS_in)
	S += c_t2_t3_t3_in*MAS_in[0]<=c_t2_t3_t3*MAS[0]

	S += c_t2_t3_t3_in*MAS_in[1]<=c_t2_t3_t3*MAS[1]

	S += c_t2_t3_t3_in*MAS_in[2]<=c_t2_t3_t3*MAS[2]

	S += c_t2_t3_t3_in*MAS_in[3]<=c_t2_t3_t3*MAS[3]

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	c_t2_t3_t3_mem0 += MAIN_MEM_r[0]
	S += c_t2_t3_t3_mem0 <= c_t2_t3_t3

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	c_t2_t3_t3_mem1 += MAIN_MEM_r[1]
	S += c_t2_t3_t3_mem1 <= c_t2_t3_t3

	c_t3000 = S.Task('c_t3000', length=4, delay_cost=1)
	c_t3000 += alt(MAS)
	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	c_t3000_in += alt(MAS_in)
	S += c_t3000_in*MAS_in[0]<=c_t3000*MAS[0]

	S += c_t3000_in*MAS_in[1]<=c_t3000*MAS[1]

	S += c_t3000_in*MAS_in[2]<=c_t3000*MAS[2]

	S += c_t3000_in*MAS_in[3]<=c_t3000*MAS[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	c_t3000_mem0 += MAIN_MEM_r[0]
	S += c_t3000_mem0 <= c_t3000

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	c_t3000_mem1 += MAIN_MEM_r[1]
	S += c_t3000_mem1 <= c_t3000

	c_t3001 = S.Task('c_t3001', length=4, delay_cost=1)
	c_t3001 += alt(MAS)
	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	c_t3001_in += alt(MAS_in)
	S += c_t3001_in*MAS_in[0]<=c_t3001*MAS[0]

	S += c_t3001_in*MAS_in[1]<=c_t3001*MAS[1]

	S += c_t3001_in*MAS_in[2]<=c_t3001*MAS[2]

	S += c_t3001_in*MAS_in[3]<=c_t3001*MAS[3]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	c_t3001_mem0 += MAIN_MEM_r[0]
	S += c_t3001_mem0 <= c_t3001

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	c_t3001_mem1 += MAIN_MEM_r[1]
	S += c_t3001_mem1 <= c_t3001

	c_t3010 = S.Task('c_t3010', length=4, delay_cost=1)
	c_t3010 += alt(MAS)
	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	c_t3010_in += alt(MAS_in)
	S += c_t3010_in*MAS_in[0]<=c_t3010*MAS[0]

	S += c_t3010_in*MAS_in[1]<=c_t3010*MAS[1]

	S += c_t3010_in*MAS_in[2]<=c_t3010*MAS[2]

	S += c_t3010_in*MAS_in[3]<=c_t3010*MAS[3]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	c_t3010_mem0 += MAIN_MEM_r[0]
	S += c_t3010_mem0 <= c_t3010

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	c_t3010_mem1 += MAIN_MEM_r[1]
	S += c_t3010_mem1 <= c_t3010

	c_t3011 = S.Task('c_t3011', length=4, delay_cost=1)
	c_t3011 += alt(MAS)
	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	c_t3011_in += alt(MAS_in)
	S += c_t3011_in*MAS_in[0]<=c_t3011*MAS[0]

	S += c_t3011_in*MAS_in[1]<=c_t3011*MAS[1]

	S += c_t3011_in*MAS_in[2]<=c_t3011*MAS[2]

	S += c_t3011_in*MAS_in[3]<=c_t3011*MAS[3]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	c_t3011_mem0 += MAIN_MEM_r[0]
	S += c_t3011_mem0 <= c_t3011

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	c_t3011_mem1 += MAIN_MEM_r[1]
	S += c_t3011_mem1 <= c_t3011

	c_t4000 = S.Task('c_t4000', length=4, delay_cost=1)
	c_t4000 += alt(MAS)
	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	c_t4000_in += alt(MAS_in)
	S += c_t4000_in*MAS_in[0]<=c_t4000*MAS[0]

	S += c_t4000_in*MAS_in[1]<=c_t4000*MAS[1]

	S += c_t4000_in*MAS_in[2]<=c_t4000*MAS[2]

	S += c_t4000_in*MAS_in[3]<=c_t4000*MAS[3]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	c_t4000_mem0 += MAIN_MEM_r[0]
	S += c_t4000_mem0 <= c_t4000

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	c_t4000_mem1 += MAIN_MEM_r[1]
	S += c_t4000_mem1 <= c_t4000

	c_t4001 = S.Task('c_t4001', length=4, delay_cost=1)
	c_t4001 += alt(MAS)
	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	c_t4001_in += alt(MAS_in)
	S += c_t4001_in*MAS_in[0]<=c_t4001*MAS[0]

	S += c_t4001_in*MAS_in[1]<=c_t4001*MAS[1]

	S += c_t4001_in*MAS_in[2]<=c_t4001*MAS[2]

	S += c_t4001_in*MAS_in[3]<=c_t4001*MAS[3]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	c_t4001_mem0 += MAIN_MEM_r[0]
	S += c_t4001_mem0 <= c_t4001

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	c_t4001_mem1 += MAIN_MEM_r[1]
	S += c_t4001_mem1 <= c_t4001

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM2_stage4MAS4/SQR/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

