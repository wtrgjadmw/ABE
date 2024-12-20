from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=6)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	c_t0_a1_0 = S.Task('c_t0_a1_0', length=1, delay_cost=1)
	c_t0_a1_0 += alt(MAS)
	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	c_t0_a1_0_mem0 += MAIN_MEM_r[0]
	S += c_t0_a1_0_mem0 <= c_t0_a1_0

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	c_t0_a1_0_mem1 += MAIN_MEM_r[1]
	S += c_t0_a1_0_mem1 <= c_t0_a1_0

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=1, delay_cost=1)
	c_t0_a1_1 += alt(MAS)
	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	c_t0_a1_1_mem0 += MAIN_MEM_r[0]
	S += c_t0_a1_1_mem0 <= c_t0_a1_1

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	c_t0_a1_1_mem1 += MAIN_MEM_r[1]
	S += c_t0_a1_1_mem1 <= c_t0_a1_1

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	c_t0_t10 += alt(MAS)
	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	c_t0_t10_mem0 += MAIN_MEM_r[0]
	S += c_t0_t10_mem0 <= c_t0_t10

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	c_t0_t10_mem1 += MAIN_MEM_r[1]
	S += c_t0_t10_mem1 <= c_t0_t10

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	c_t0_t11 += alt(MAS)
	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	c_t0_t11_mem0 += MAIN_MEM_r[0]
	S += c_t0_t11_mem0 <= c_t0_t11

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	c_t0_t11_mem1 += MAIN_MEM_r[1]
	S += c_t0_t11_mem1 <= c_t0_t11

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=6, delay_cost=1)
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

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=6, delay_cost=1)
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

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=1, delay_cost=1)
	c_t0_t3_t2 += alt(MAS)
	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	c_t0_t3_t2_mem0 += MAIN_MEM_r[0]
	S += c_t0_t3_t2_mem0 <= c_t0_t3_t2

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	c_t0_t3_t2_mem1 += MAIN_MEM_r[1]
	S += c_t0_t3_t2_mem1 <= c_t0_t3_t2

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=1, delay_cost=1)
	c_t0_t3_t3 += alt(MAS)
	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	c_t0_t3_t3_mem0 += MAIN_MEM_r[0]
	S += c_t0_t3_t3_mem0 <= c_t0_t3_t3

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	c_t0_t3_t3_mem1 += MAIN_MEM_r[1]
	S += c_t0_t3_t3_mem1 <= c_t0_t3_t3

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=1, delay_cost=1)
	c_t1_a1_0 += alt(MAS)
	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	c_t1_a1_0_mem0 += MAIN_MEM_r[0]
	S += c_t1_a1_0_mem0 <= c_t1_a1_0

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	c_t1_a1_0_mem1 += MAIN_MEM_r[1]
	S += c_t1_a1_0_mem1 <= c_t1_a1_0

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=1, delay_cost=1)
	c_t1_a1_1 += alt(MAS)
	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	c_t1_a1_1_mem0 += MAIN_MEM_r[0]
	S += c_t1_a1_1_mem0 <= c_t1_a1_1

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	c_t1_a1_1_mem1 += MAIN_MEM_r[1]
	S += c_t1_a1_1_mem1 <= c_t1_a1_1

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	c_t1_t10 += alt(MAS)
	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	c_t1_t10_mem0 += MAIN_MEM_r[0]
	S += c_t1_t10_mem0 <= c_t1_t10

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	c_t1_t10_mem1 += MAIN_MEM_r[1]
	S += c_t1_t10_mem1 <= c_t1_t10

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	c_t1_t11 += alt(MAS)
	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	c_t1_t11_mem0 += MAIN_MEM_r[0]
	S += c_t1_t11_mem0 <= c_t1_t11

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	c_t1_t11_mem1 += MAIN_MEM_r[1]
	S += c_t1_t11_mem1 <= c_t1_t11

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=6, delay_cost=1)
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

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=6, delay_cost=1)
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

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=1, delay_cost=1)
	c_t1_t3_t2 += alt(MAS)
	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	c_t1_t3_t2_mem0 += MAIN_MEM_r[0]
	S += c_t1_t3_t2_mem0 <= c_t1_t3_t2

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	c_t1_t3_t2_mem1 += MAIN_MEM_r[1]
	S += c_t1_t3_t2_mem1 <= c_t1_t3_t2

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=1, delay_cost=1)
	c_t1_t3_t3 += alt(MAS)
	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	c_t1_t3_t3_mem0 += MAIN_MEM_r[0]
	S += c_t1_t3_t3_mem0 <= c_t1_t3_t3

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	c_t1_t3_t3_mem1 += MAIN_MEM_r[1]
	S += c_t1_t3_t3_mem1 <= c_t1_t3_t3

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=1, delay_cost=1)
	c_t2_a1_0 += alt(MAS)
	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	c_t2_a1_0_mem0 += MAIN_MEM_r[0]
	S += c_t2_a1_0_mem0 <= c_t2_a1_0

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	c_t2_a1_0_mem1 += MAIN_MEM_r[1]
	S += c_t2_a1_0_mem1 <= c_t2_a1_0

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=1, delay_cost=1)
	c_t2_a1_1 += alt(MAS)
	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	c_t2_a1_1_mem0 += MAIN_MEM_r[0]
	S += c_t2_a1_1_mem0 <= c_t2_a1_1

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	c_t2_a1_1_mem1 += MAIN_MEM_r[1]
	S += c_t2_a1_1_mem1 <= c_t2_a1_1

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	c_t2_t10 += alt(MAS)
	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	c_t2_t10_mem0 += MAIN_MEM_r[0]
	S += c_t2_t10_mem0 <= c_t2_t10

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	c_t2_t10_mem1 += MAIN_MEM_r[1]
	S += c_t2_t10_mem1 <= c_t2_t10

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	c_t2_t11 += alt(MAS)
	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	c_t2_t11_mem0 += MAIN_MEM_r[0]
	S += c_t2_t11_mem0 <= c_t2_t11

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	c_t2_t11_mem1 += MAIN_MEM_r[1]
	S += c_t2_t11_mem1 <= c_t2_t11

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=6, delay_cost=1)
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

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=6, delay_cost=1)
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

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=1, delay_cost=1)
	c_t2_t3_t2 += alt(MAS)
	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	c_t2_t3_t2_mem0 += MAIN_MEM_r[0]
	S += c_t2_t3_t2_mem0 <= c_t2_t3_t2

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	c_t2_t3_t2_mem1 += MAIN_MEM_r[1]
	S += c_t2_t3_t2_mem1 <= c_t2_t3_t2

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=1, delay_cost=1)
	c_t2_t3_t3 += alt(MAS)
	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	c_t2_t3_t3_mem0 += MAIN_MEM_r[0]
	S += c_t2_t3_t3_mem0 <= c_t2_t3_t3

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	c_t2_t3_t3_mem1 += MAIN_MEM_r[1]
	S += c_t2_t3_t3_mem1 <= c_t2_t3_t3

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	c_t3000 += alt(MAS)
	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	c_t3000_mem0 += MAIN_MEM_r[0]
	S += c_t3000_mem0 <= c_t3000

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	c_t3000_mem1 += MAIN_MEM_r[1]
	S += c_t3000_mem1 <= c_t3000

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	c_t3001 += alt(MAS)
	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	c_t3001_mem0 += MAIN_MEM_r[0]
	S += c_t3001_mem0 <= c_t3001

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	c_t3001_mem1 += MAIN_MEM_r[1]
	S += c_t3001_mem1 <= c_t3001

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	c_t3010 += alt(MAS)
	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	c_t3010_mem0 += MAIN_MEM_r[0]
	S += c_t3010_mem0 <= c_t3010

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	c_t3010_mem1 += MAIN_MEM_r[1]
	S += c_t3010_mem1 <= c_t3010

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	c_t3011 += alt(MAS)
	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	c_t3011_mem0 += MAIN_MEM_r[0]
	S += c_t3011_mem0 <= c_t3011

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	c_t3011_mem1 += MAIN_MEM_r[1]
	S += c_t3011_mem1 <= c_t3011

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	c_t4000 += alt(MAS)
	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	c_t4000_mem0 += MAIN_MEM_r[0]
	S += c_t4000_mem0 <= c_t4000

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	c_t4000_mem1 += MAIN_MEM_r[1]
	S += c_t4000_mem1 <= c_t4000

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	c_t4001 += alt(MAS)
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

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM2_stage1MAS8/SQR/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

