from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
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
	c10_t0 = S.Task('c10_t0', length=11, delay_cost=1)
	c10_t0 += alt(MM)
	c10_t0_in = S.Task('c10_t0_in', length=1, delay_cost=1)
	c10_t0_in += alt(MM_in)
	S += c10_t0_in*MM_in[0]<=c10_t0*MM[0]
	S += c10_t0_in*MM_in[1]<=c10_t0*MM[1]
	c10_t0_mem0 = S.Task('c10_t0_mem0', length=1, delay_cost=1)
	c10_t0_mem0 += MAIN_MEM_r[0]
	S += c10_t0_mem0 <= c10_t0

	c10_t0_mem1 = S.Task('c10_t0_mem1', length=1, delay_cost=1)
	c10_t0_mem1 += MAIN_MEM_r[1]
	S += c10_t0_mem1 <= c10_t0

	c10_t1 = S.Task('c10_t1', length=11, delay_cost=1)
	c10_t1 += alt(MM)
	c10_t1_in = S.Task('c10_t1_in', length=1, delay_cost=1)
	c10_t1_in += alt(MM_in)
	S += c10_t1_in*MM_in[0]<=c10_t1*MM[0]
	S += c10_t1_in*MM_in[1]<=c10_t1*MM[1]
	c10_t1_mem0 = S.Task('c10_t1_mem0', length=1, delay_cost=1)
	c10_t1_mem0 += MAIN_MEM_r[0]
	S += c10_t1_mem0 <= c10_t1

	c10_t1_mem1 = S.Task('c10_t1_mem1', length=1, delay_cost=1)
	c10_t1_mem1 += MAIN_MEM_r[1]
	S += c10_t1_mem1 <= c10_t1

	c10_t2 = S.Task('c10_t2', length=4, delay_cost=1)
	c10_t2 += alt(MAS)
	c10_t2_in = S.Task('c10_t2_in', length=1, delay_cost=1)
	c10_t2_in += alt(MAS_in)
	S += c10_t2_in*MAS_in[0]<=c10_t2*MAS[0]

	S += c10_t2_in*MAS_in[1]<=c10_t2*MAS[1]

	S += c10_t2_in*MAS_in[2]<=c10_t2*MAS[2]

	S += c10_t2_in*MAS_in[3]<=c10_t2*MAS[3]

	c10_t2_mem0 = S.Task('c10_t2_mem0', length=1, delay_cost=1)
	c10_t2_mem0 += MAIN_MEM_r[0]
	S += c10_t2_mem0 <= c10_t2

	c10_t2_mem1 = S.Task('c10_t2_mem1', length=1, delay_cost=1)
	c10_t2_mem1 += MAIN_MEM_r[1]
	S += c10_t2_mem1 <= c10_t2

	c10_t3 = S.Task('c10_t3', length=4, delay_cost=1)
	c10_t3 += alt(MAS)
	c10_t3_in = S.Task('c10_t3_in', length=1, delay_cost=1)
	c10_t3_in += alt(MAS_in)
	S += c10_t3_in*MAS_in[0]<=c10_t3*MAS[0]

	S += c10_t3_in*MAS_in[1]<=c10_t3*MAS[1]

	S += c10_t3_in*MAS_in[2]<=c10_t3*MAS[2]

	S += c10_t3_in*MAS_in[3]<=c10_t3*MAS[3]

	c10_t3_mem0 = S.Task('c10_t3_mem0', length=1, delay_cost=1)
	c10_t3_mem0 += MAIN_MEM_r[0]
	S += c10_t3_mem0 <= c10_t3

	c10_t3_mem1 = S.Task('c10_t3_mem1', length=1, delay_cost=1)
	c10_t3_mem1 += MAIN_MEM_r[1]
	S += c10_t3_mem1 <= c10_t3

	c20_t0 = S.Task('c20_t0', length=11, delay_cost=1)
	c20_t0 += alt(MM)
	c20_t0_in = S.Task('c20_t0_in', length=1, delay_cost=1)
	c20_t0_in += alt(MM_in)
	S += c20_t0_in*MM_in[0]<=c20_t0*MM[0]
	S += c20_t0_in*MM_in[1]<=c20_t0*MM[1]
	c20_t0_mem0 = S.Task('c20_t0_mem0', length=1, delay_cost=1)
	c20_t0_mem0 += MAIN_MEM_r[0]
	S += c20_t0_mem0 <= c20_t0

	c20_t0_mem1 = S.Task('c20_t0_mem1', length=1, delay_cost=1)
	c20_t0_mem1 += MAIN_MEM_r[1]
	S += c20_t0_mem1 <= c20_t0

	c20_t1 = S.Task('c20_t1', length=11, delay_cost=1)
	c20_t1 += alt(MM)
	c20_t1_in = S.Task('c20_t1_in', length=1, delay_cost=1)
	c20_t1_in += alt(MM_in)
	S += c20_t1_in*MM_in[0]<=c20_t1*MM[0]
	S += c20_t1_in*MM_in[1]<=c20_t1*MM[1]
	c20_t1_mem0 = S.Task('c20_t1_mem0', length=1, delay_cost=1)
	c20_t1_mem0 += MAIN_MEM_r[0]
	S += c20_t1_mem0 <= c20_t1

	c20_t1_mem1 = S.Task('c20_t1_mem1', length=1, delay_cost=1)
	c20_t1_mem1 += MAIN_MEM_r[1]
	S += c20_t1_mem1 <= c20_t1

	c20_t2 = S.Task('c20_t2', length=4, delay_cost=1)
	c20_t2 += alt(MAS)
	c20_t2_in = S.Task('c20_t2_in', length=1, delay_cost=1)
	c20_t2_in += alt(MAS_in)
	S += c20_t2_in*MAS_in[0]<=c20_t2*MAS[0]

	S += c20_t2_in*MAS_in[1]<=c20_t2*MAS[1]

	S += c20_t2_in*MAS_in[2]<=c20_t2*MAS[2]

	S += c20_t2_in*MAS_in[3]<=c20_t2*MAS[3]

	c20_t2_mem0 = S.Task('c20_t2_mem0', length=1, delay_cost=1)
	c20_t2_mem0 += MAIN_MEM_r[0]
	S += c20_t2_mem0 <= c20_t2

	c20_t2_mem1 = S.Task('c20_t2_mem1', length=1, delay_cost=1)
	c20_t2_mem1 += MAIN_MEM_r[1]
	S += c20_t2_mem1 <= c20_t2

	c20_t3 = S.Task('c20_t3', length=4, delay_cost=1)
	c20_t3 += alt(MAS)
	c20_t3_in = S.Task('c20_t3_in', length=1, delay_cost=1)
	c20_t3_in += alt(MAS_in)
	S += c20_t3_in*MAS_in[0]<=c20_t3*MAS[0]

	S += c20_t3_in*MAS_in[1]<=c20_t3*MAS[1]

	S += c20_t3_in*MAS_in[2]<=c20_t3*MAS[2]

	S += c20_t3_in*MAS_in[3]<=c20_t3*MAS[3]

	c20_t3_mem0 = S.Task('c20_t3_mem0', length=1, delay_cost=1)
	c20_t3_mem0 += MAIN_MEM_r[0]
	S += c20_t3_mem0 <= c20_t3

	c20_t3_mem1 = S.Task('c20_t3_mem1', length=1, delay_cost=1)
	c20_t3_mem1 += MAIN_MEM_r[1]
	S += c20_t3_mem1 <= c20_t3

	c01_t0 = S.Task('c01_t0', length=11, delay_cost=1)
	c01_t0 += alt(MM)
	c01_t0_in = S.Task('c01_t0_in', length=1, delay_cost=1)
	c01_t0_in += alt(MM_in)
	S += c01_t0_in*MM_in[0]<=c01_t0*MM[0]
	S += c01_t0_in*MM_in[1]<=c01_t0*MM[1]
	c01_t0_mem0 = S.Task('c01_t0_mem0', length=1, delay_cost=1)
	c01_t0_mem0 += MAIN_MEM_r[0]
	S += c01_t0_mem0 <= c01_t0

	c01_t0_mem1 = S.Task('c01_t0_mem1', length=1, delay_cost=1)
	c01_t0_mem1 += MAIN_MEM_r[1]
	S += c01_t0_mem1 <= c01_t0

	c01_t1 = S.Task('c01_t1', length=11, delay_cost=1)
	c01_t1 += alt(MM)
	c01_t1_in = S.Task('c01_t1_in', length=1, delay_cost=1)
	c01_t1_in += alt(MM_in)
	S += c01_t1_in*MM_in[0]<=c01_t1*MM[0]
	S += c01_t1_in*MM_in[1]<=c01_t1*MM[1]
	c01_t1_mem0 = S.Task('c01_t1_mem0', length=1, delay_cost=1)
	c01_t1_mem0 += MAIN_MEM_r[0]
	S += c01_t1_mem0 <= c01_t1

	c01_t1_mem1 = S.Task('c01_t1_mem1', length=1, delay_cost=1)
	c01_t1_mem1 += MAIN_MEM_r[1]
	S += c01_t1_mem1 <= c01_t1

	c01_t2 = S.Task('c01_t2', length=4, delay_cost=1)
	c01_t2 += alt(MAS)
	c01_t2_in = S.Task('c01_t2_in', length=1, delay_cost=1)
	c01_t2_in += alt(MAS_in)
	S += c01_t2_in*MAS_in[0]<=c01_t2*MAS[0]

	S += c01_t2_in*MAS_in[1]<=c01_t2*MAS[1]

	S += c01_t2_in*MAS_in[2]<=c01_t2*MAS[2]

	S += c01_t2_in*MAS_in[3]<=c01_t2*MAS[3]

	c01_t2_mem0 = S.Task('c01_t2_mem0', length=1, delay_cost=1)
	c01_t2_mem0 += MAIN_MEM_r[0]
	S += c01_t2_mem0 <= c01_t2

	c01_t2_mem1 = S.Task('c01_t2_mem1', length=1, delay_cost=1)
	c01_t2_mem1 += MAIN_MEM_r[1]
	S += c01_t2_mem1 <= c01_t2

	c01_t3 = S.Task('c01_t3', length=4, delay_cost=1)
	c01_t3 += alt(MAS)
	c01_t3_in = S.Task('c01_t3_in', length=1, delay_cost=1)
	c01_t3_in += alt(MAS_in)
	S += c01_t3_in*MAS_in[0]<=c01_t3*MAS[0]

	S += c01_t3_in*MAS_in[1]<=c01_t3*MAS[1]

	S += c01_t3_in*MAS_in[2]<=c01_t3*MAS[2]

	S += c01_t3_in*MAS_in[3]<=c01_t3*MAS[3]

	c01_t3_mem0 = S.Task('c01_t3_mem0', length=1, delay_cost=1)
	c01_t3_mem0 += MAIN_MEM_r[0]
	S += c01_t3_mem0 <= c01_t3

	c01_t3_mem1 = S.Task('c01_t3_mem1', length=1, delay_cost=1)
	c01_t3_mem1 += MAIN_MEM_r[1]
	S += c01_t3_mem1 <= c01_t3

	c11_t0 = S.Task('c11_t0', length=11, delay_cost=1)
	c11_t0 += alt(MM)
	c11_t0_in = S.Task('c11_t0_in', length=1, delay_cost=1)
	c11_t0_in += alt(MM_in)
	S += c11_t0_in*MM_in[0]<=c11_t0*MM[0]
	S += c11_t0_in*MM_in[1]<=c11_t0*MM[1]
	c11_t0_mem0 = S.Task('c11_t0_mem0', length=1, delay_cost=1)
	c11_t0_mem0 += MAIN_MEM_r[0]
	S += c11_t0_mem0 <= c11_t0

	c11_t0_mem1 = S.Task('c11_t0_mem1', length=1, delay_cost=1)
	c11_t0_mem1 += MAIN_MEM_r[1]
	S += c11_t0_mem1 <= c11_t0

	c11_t1 = S.Task('c11_t1', length=11, delay_cost=1)
	c11_t1 += alt(MM)
	c11_t1_in = S.Task('c11_t1_in', length=1, delay_cost=1)
	c11_t1_in += alt(MM_in)
	S += c11_t1_in*MM_in[0]<=c11_t1*MM[0]
	S += c11_t1_in*MM_in[1]<=c11_t1*MM[1]
	c11_t1_mem0 = S.Task('c11_t1_mem0', length=1, delay_cost=1)
	c11_t1_mem0 += MAIN_MEM_r[0]
	S += c11_t1_mem0 <= c11_t1

	c11_t1_mem1 = S.Task('c11_t1_mem1', length=1, delay_cost=1)
	c11_t1_mem1 += MAIN_MEM_r[1]
	S += c11_t1_mem1 <= c11_t1

	c11_t2 = S.Task('c11_t2', length=4, delay_cost=1)
	c11_t2 += alt(MAS)
	c11_t2_in = S.Task('c11_t2_in', length=1, delay_cost=1)
	c11_t2_in += alt(MAS_in)
	S += c11_t2_in*MAS_in[0]<=c11_t2*MAS[0]

	S += c11_t2_in*MAS_in[1]<=c11_t2*MAS[1]

	S += c11_t2_in*MAS_in[2]<=c11_t2*MAS[2]

	S += c11_t2_in*MAS_in[3]<=c11_t2*MAS[3]

	c11_t2_mem0 = S.Task('c11_t2_mem0', length=1, delay_cost=1)
	c11_t2_mem0 += MAIN_MEM_r[0]
	S += c11_t2_mem0 <= c11_t2

	c11_t2_mem1 = S.Task('c11_t2_mem1', length=1, delay_cost=1)
	c11_t2_mem1 += MAIN_MEM_r[1]
	S += c11_t2_mem1 <= c11_t2

	c11_t3 = S.Task('c11_t3', length=4, delay_cost=1)
	c11_t3 += alt(MAS)
	c11_t3_in = S.Task('c11_t3_in', length=1, delay_cost=1)
	c11_t3_in += alt(MAS_in)
	S += c11_t3_in*MAS_in[0]<=c11_t3*MAS[0]

	S += c11_t3_in*MAS_in[1]<=c11_t3*MAS[1]

	S += c11_t3_in*MAS_in[2]<=c11_t3*MAS[2]

	S += c11_t3_in*MAS_in[3]<=c11_t3*MAS[3]

	c11_t3_mem0 = S.Task('c11_t3_mem0', length=1, delay_cost=1)
	c11_t3_mem0 += MAIN_MEM_r[0]
	S += c11_t3_mem0 <= c11_t3

	c11_t3_mem1 = S.Task('c11_t3_mem1', length=1, delay_cost=1)
	c11_t3_mem1 += MAIN_MEM_r[1]
	S += c11_t3_mem1 <= c11_t3

	c21_t0 = S.Task('c21_t0', length=11, delay_cost=1)
	c21_t0 += alt(MM)
	c21_t0_in = S.Task('c21_t0_in', length=1, delay_cost=1)
	c21_t0_in += alt(MM_in)
	S += c21_t0_in*MM_in[0]<=c21_t0*MM[0]
	S += c21_t0_in*MM_in[1]<=c21_t0*MM[1]
	c21_t0_mem0 = S.Task('c21_t0_mem0', length=1, delay_cost=1)
	c21_t0_mem0 += MAIN_MEM_r[0]
	S += c21_t0_mem0 <= c21_t0

	c21_t0_mem1 = S.Task('c21_t0_mem1', length=1, delay_cost=1)
	c21_t0_mem1 += MAIN_MEM_r[1]
	S += c21_t0_mem1 <= c21_t0

	c21_t1 = S.Task('c21_t1', length=11, delay_cost=1)
	c21_t1 += alt(MM)
	c21_t1_in = S.Task('c21_t1_in', length=1, delay_cost=1)
	c21_t1_in += alt(MM_in)
	S += c21_t1_in*MM_in[0]<=c21_t1*MM[0]
	S += c21_t1_in*MM_in[1]<=c21_t1*MM[1]
	c21_t1_mem0 = S.Task('c21_t1_mem0', length=1, delay_cost=1)
	c21_t1_mem0 += MAIN_MEM_r[0]
	S += c21_t1_mem0 <= c21_t1

	c21_t1_mem1 = S.Task('c21_t1_mem1', length=1, delay_cost=1)
	c21_t1_mem1 += MAIN_MEM_r[1]
	S += c21_t1_mem1 <= c21_t1

	c21_t2 = S.Task('c21_t2', length=4, delay_cost=1)
	c21_t2 += alt(MAS)
	c21_t2_in = S.Task('c21_t2_in', length=1, delay_cost=1)
	c21_t2_in += alt(MAS_in)
	S += c21_t2_in*MAS_in[0]<=c21_t2*MAS[0]

	S += c21_t2_in*MAS_in[1]<=c21_t2*MAS[1]

	S += c21_t2_in*MAS_in[2]<=c21_t2*MAS[2]

	S += c21_t2_in*MAS_in[3]<=c21_t2*MAS[3]

	c21_t2_mem0 = S.Task('c21_t2_mem0', length=1, delay_cost=1)
	c21_t2_mem0 += MAIN_MEM_r[0]
	S += c21_t2_mem0 <= c21_t2

	c21_t2_mem1 = S.Task('c21_t2_mem1', length=1, delay_cost=1)
	c21_t2_mem1 += MAIN_MEM_r[1]
	S += c21_t2_mem1 <= c21_t2

	c21_t3 = S.Task('c21_t3', length=4, delay_cost=1)
	c21_t3 += alt(MAS)
	c21_t3_in = S.Task('c21_t3_in', length=1, delay_cost=1)
	c21_t3_in += alt(MAS_in)
	S += c21_t3_in*MAS_in[0]<=c21_t3*MAS[0]

	S += c21_t3_in*MAS_in[1]<=c21_t3*MAS[1]

	S += c21_t3_in*MAS_in[2]<=c21_t3*MAS[2]

	S += c21_t3_in*MAS_in[3]<=c21_t3*MAS[3]

	c21_t3_mem0 = S.Task('c21_t3_mem0', length=1, delay_cost=1)
	c21_t3_mem0 += MAIN_MEM_r[0]
	S += c21_t3_mem0 <= c21_t3

	c21_t3_mem1 = S.Task('c21_t3_mem1', length=1, delay_cost=1)
	c21_t3_mem1 += MAIN_MEM_r[1]
	S += c21_t3_mem1 <= c21_t3

	c000 = S.Task('c000', length=4, delay_cost=1)
	c000 += alt(MAS)
	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	c000_in += alt(MAS_in)
	S += c000_in*MAS_in[0]<=c000*MAS[0]

	S += c000_in*MAS_in[1]<=c000*MAS[1]

	S += c000_in*MAS_in[2]<=c000*MAS[2]

	S += c000_in*MAS_in[3]<=c000*MAS[3]

	S += 0<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAIN_MEM_r[0]
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += MAIN_MEM_r[1]
	S += c000_mem1 <= c000

	c001 = S.Task('c001', length=4, delay_cost=1)
	c001 += alt(MAS)
	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	c001_in += alt(MAS_in)
	S += c001_in*MAS_in[0]<=c001*MAS[0]

	S += c001_in*MAS_in[1]<=c001*MAS[1]

	S += c001_in*MAS_in[2]<=c001*MAS[2]

	S += c001_in*MAS_in[3]<=c001*MAS[3]

	S += 0<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAIN_MEM_r[0]
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += MAIN_MEM_r[1]
	S += c001_mem1 <= c001

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage4MAS4/FROB/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

