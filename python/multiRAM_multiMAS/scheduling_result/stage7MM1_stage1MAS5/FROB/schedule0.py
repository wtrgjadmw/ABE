from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	c10_t0_in = S.Task('c10_t0_in', length=1, delay_cost=1)
	c10_t0_in += alt(MM_in)
	c10_t0 = S.Task('c10_t0', length=7, delay_cost=1)
	c10_t0 += alt(MM)
	S += c10_t0>=c10_t0_in

	c10_t0_mem0 = S.Task('c10_t0_mem0', length=1, delay_cost=1)
	c10_t0_mem0 += MAIN_MEM_r[0]
	S += c10_t0_mem0 <= c10_t0

	c10_t0_mem1 = S.Task('c10_t0_mem1', length=1, delay_cost=1)
	c10_t0_mem1 += MAIN_MEM_r[1]
	S += c10_t0_mem1 <= c10_t0

	c10_t1_in = S.Task('c10_t1_in', length=1, delay_cost=1)
	c10_t1_in += alt(MM_in)
	c10_t1 = S.Task('c10_t1', length=7, delay_cost=1)
	c10_t1 += alt(MM)
	S += c10_t1>=c10_t1_in

	c10_t1_mem0 = S.Task('c10_t1_mem0', length=1, delay_cost=1)
	c10_t1_mem0 += MAIN_MEM_r[0]
	S += c10_t1_mem0 <= c10_t1

	c10_t1_mem1 = S.Task('c10_t1_mem1', length=1, delay_cost=1)
	c10_t1_mem1 += MAIN_MEM_r[1]
	S += c10_t1_mem1 <= c10_t1

	c10_t2 = S.Task('c10_t2', length=1, delay_cost=1)
	c10_t2 += alt(MAS)

	c10_t2_mem0 = S.Task('c10_t2_mem0', length=1, delay_cost=1)
	c10_t2_mem0 += MAIN_MEM_r[0]
	S += c10_t2_mem0 <= c10_t2

	c10_t2_mem1 = S.Task('c10_t2_mem1', length=1, delay_cost=1)
	c10_t2_mem1 += MAIN_MEM_r[1]
	S += c10_t2_mem1 <= c10_t2

	c10_t3 = S.Task('c10_t3', length=1, delay_cost=1)
	c10_t3 += alt(MAS)

	c10_t3_mem0 = S.Task('c10_t3_mem0', length=1, delay_cost=1)
	c10_t3_mem0 += MAIN_MEM_r[0]
	S += c10_t3_mem0 <= c10_t3

	c10_t3_mem1 = S.Task('c10_t3_mem1', length=1, delay_cost=1)
	c10_t3_mem1 += MAIN_MEM_r[1]
	S += c10_t3_mem1 <= c10_t3

	c20_t0_in = S.Task('c20_t0_in', length=1, delay_cost=1)
	c20_t0_in += alt(MM_in)
	c20_t0 = S.Task('c20_t0', length=7, delay_cost=1)
	c20_t0 += alt(MM)
	S += c20_t0>=c20_t0_in

	c20_t0_mem0 = S.Task('c20_t0_mem0', length=1, delay_cost=1)
	c20_t0_mem0 += MAIN_MEM_r[0]
	S += c20_t0_mem0 <= c20_t0

	c20_t0_mem1 = S.Task('c20_t0_mem1', length=1, delay_cost=1)
	c20_t0_mem1 += MAIN_MEM_r[1]
	S += c20_t0_mem1 <= c20_t0

	c20_t1_in = S.Task('c20_t1_in', length=1, delay_cost=1)
	c20_t1_in += alt(MM_in)
	c20_t1 = S.Task('c20_t1', length=7, delay_cost=1)
	c20_t1 += alt(MM)
	S += c20_t1>=c20_t1_in

	c20_t1_mem0 = S.Task('c20_t1_mem0', length=1, delay_cost=1)
	c20_t1_mem0 += MAIN_MEM_r[0]
	S += c20_t1_mem0 <= c20_t1

	c20_t1_mem1 = S.Task('c20_t1_mem1', length=1, delay_cost=1)
	c20_t1_mem1 += MAIN_MEM_r[1]
	S += c20_t1_mem1 <= c20_t1

	c20_t2 = S.Task('c20_t2', length=1, delay_cost=1)
	c20_t2 += alt(MAS)

	c20_t2_mem0 = S.Task('c20_t2_mem0', length=1, delay_cost=1)
	c20_t2_mem0 += MAIN_MEM_r[0]
	S += c20_t2_mem0 <= c20_t2

	c20_t2_mem1 = S.Task('c20_t2_mem1', length=1, delay_cost=1)
	c20_t2_mem1 += MAIN_MEM_r[1]
	S += c20_t2_mem1 <= c20_t2

	c20_t3 = S.Task('c20_t3', length=1, delay_cost=1)
	c20_t3 += alt(MAS)

	c20_t3_mem0 = S.Task('c20_t3_mem0', length=1, delay_cost=1)
	c20_t3_mem0 += MAIN_MEM_r[0]
	S += c20_t3_mem0 <= c20_t3

	c20_t3_mem1 = S.Task('c20_t3_mem1', length=1, delay_cost=1)
	c20_t3_mem1 += MAIN_MEM_r[1]
	S += c20_t3_mem1 <= c20_t3

	c01_t0_in = S.Task('c01_t0_in', length=1, delay_cost=1)
	c01_t0_in += alt(MM_in)
	c01_t0 = S.Task('c01_t0', length=7, delay_cost=1)
	c01_t0 += alt(MM)
	S += c01_t0>=c01_t0_in

	c01_t0_mem0 = S.Task('c01_t0_mem0', length=1, delay_cost=1)
	c01_t0_mem0 += MAIN_MEM_r[0]
	S += c01_t0_mem0 <= c01_t0

	c01_t0_mem1 = S.Task('c01_t0_mem1', length=1, delay_cost=1)
	c01_t0_mem1 += MAIN_MEM_r[1]
	S += c01_t0_mem1 <= c01_t0

	c01_t1_in = S.Task('c01_t1_in', length=1, delay_cost=1)
	c01_t1_in += alt(MM_in)
	c01_t1 = S.Task('c01_t1', length=7, delay_cost=1)
	c01_t1 += alt(MM)
	S += c01_t1>=c01_t1_in

	c01_t1_mem0 = S.Task('c01_t1_mem0', length=1, delay_cost=1)
	c01_t1_mem0 += MAIN_MEM_r[0]
	S += c01_t1_mem0 <= c01_t1

	c01_t1_mem1 = S.Task('c01_t1_mem1', length=1, delay_cost=1)
	c01_t1_mem1 += MAIN_MEM_r[1]
	S += c01_t1_mem1 <= c01_t1

	c01_t2 = S.Task('c01_t2', length=1, delay_cost=1)
	c01_t2 += alt(MAS)

	c01_t2_mem0 = S.Task('c01_t2_mem0', length=1, delay_cost=1)
	c01_t2_mem0 += MAIN_MEM_r[0]
	S += c01_t2_mem0 <= c01_t2

	c01_t2_mem1 = S.Task('c01_t2_mem1', length=1, delay_cost=1)
	c01_t2_mem1 += MAIN_MEM_r[1]
	S += c01_t2_mem1 <= c01_t2

	c01_t3 = S.Task('c01_t3', length=1, delay_cost=1)
	c01_t3 += alt(MAS)

	c01_t3_mem0 = S.Task('c01_t3_mem0', length=1, delay_cost=1)
	c01_t3_mem0 += MAIN_MEM_r[0]
	S += c01_t3_mem0 <= c01_t3

	c01_t3_mem1 = S.Task('c01_t3_mem1', length=1, delay_cost=1)
	c01_t3_mem1 += MAIN_MEM_r[1]
	S += c01_t3_mem1 <= c01_t3

	c11_t0_in = S.Task('c11_t0_in', length=1, delay_cost=1)
	c11_t0_in += alt(MM_in)
	c11_t0 = S.Task('c11_t0', length=7, delay_cost=1)
	c11_t0 += alt(MM)
	S += c11_t0>=c11_t0_in

	c11_t0_mem0 = S.Task('c11_t0_mem0', length=1, delay_cost=1)
	c11_t0_mem0 += MAIN_MEM_r[0]
	S += c11_t0_mem0 <= c11_t0

	c11_t0_mem1 = S.Task('c11_t0_mem1', length=1, delay_cost=1)
	c11_t0_mem1 += MAIN_MEM_r[1]
	S += c11_t0_mem1 <= c11_t0

	c11_t1_in = S.Task('c11_t1_in', length=1, delay_cost=1)
	c11_t1_in += alt(MM_in)
	c11_t1 = S.Task('c11_t1', length=7, delay_cost=1)
	c11_t1 += alt(MM)
	S += c11_t1>=c11_t1_in

	c11_t1_mem0 = S.Task('c11_t1_mem0', length=1, delay_cost=1)
	c11_t1_mem0 += MAIN_MEM_r[0]
	S += c11_t1_mem0 <= c11_t1

	c11_t1_mem1 = S.Task('c11_t1_mem1', length=1, delay_cost=1)
	c11_t1_mem1 += MAIN_MEM_r[1]
	S += c11_t1_mem1 <= c11_t1

	c11_t2 = S.Task('c11_t2', length=1, delay_cost=1)
	c11_t2 += alt(MAS)

	c11_t2_mem0 = S.Task('c11_t2_mem0', length=1, delay_cost=1)
	c11_t2_mem0 += MAIN_MEM_r[0]
	S += c11_t2_mem0 <= c11_t2

	c11_t2_mem1 = S.Task('c11_t2_mem1', length=1, delay_cost=1)
	c11_t2_mem1 += MAIN_MEM_r[1]
	S += c11_t2_mem1 <= c11_t2

	c11_t3 = S.Task('c11_t3', length=1, delay_cost=1)
	c11_t3 += alt(MAS)

	c11_t3_mem0 = S.Task('c11_t3_mem0', length=1, delay_cost=1)
	c11_t3_mem0 += MAIN_MEM_r[0]
	S += c11_t3_mem0 <= c11_t3

	c11_t3_mem1 = S.Task('c11_t3_mem1', length=1, delay_cost=1)
	c11_t3_mem1 += MAIN_MEM_r[1]
	S += c11_t3_mem1 <= c11_t3

	c21_t0_in = S.Task('c21_t0_in', length=1, delay_cost=1)
	c21_t0_in += alt(MM_in)
	c21_t0 = S.Task('c21_t0', length=7, delay_cost=1)
	c21_t0 += alt(MM)
	S += c21_t0>=c21_t0_in

	c21_t0_mem0 = S.Task('c21_t0_mem0', length=1, delay_cost=1)
	c21_t0_mem0 += MAIN_MEM_r[0]
	S += c21_t0_mem0 <= c21_t0

	c21_t0_mem1 = S.Task('c21_t0_mem1', length=1, delay_cost=1)
	c21_t0_mem1 += MAIN_MEM_r[1]
	S += c21_t0_mem1 <= c21_t0

	c21_t1_in = S.Task('c21_t1_in', length=1, delay_cost=1)
	c21_t1_in += alt(MM_in)
	c21_t1 = S.Task('c21_t1', length=7, delay_cost=1)
	c21_t1 += alt(MM)
	S += c21_t1>=c21_t1_in

	c21_t1_mem0 = S.Task('c21_t1_mem0', length=1, delay_cost=1)
	c21_t1_mem0 += MAIN_MEM_r[0]
	S += c21_t1_mem0 <= c21_t1

	c21_t1_mem1 = S.Task('c21_t1_mem1', length=1, delay_cost=1)
	c21_t1_mem1 += MAIN_MEM_r[1]
	S += c21_t1_mem1 <= c21_t1

	c21_t2 = S.Task('c21_t2', length=1, delay_cost=1)
	c21_t2 += alt(MAS)

	c21_t2_mem0 = S.Task('c21_t2_mem0', length=1, delay_cost=1)
	c21_t2_mem0 += MAIN_MEM_r[0]
	S += c21_t2_mem0 <= c21_t2

	c21_t2_mem1 = S.Task('c21_t2_mem1', length=1, delay_cost=1)
	c21_t2_mem1 += MAIN_MEM_r[1]
	S += c21_t2_mem1 <= c21_t2

	c21_t3 = S.Task('c21_t3', length=1, delay_cost=1)
	c21_t3 += alt(MAS)

	c21_t3_mem0 = S.Task('c21_t3_mem0', length=1, delay_cost=1)
	c21_t3_mem0 += MAIN_MEM_r[0]
	S += c21_t3_mem0 <= c21_t3

	c21_t3_mem1 = S.Task('c21_t3_mem1', length=1, delay_cost=1)
	c21_t3_mem1 += MAIN_MEM_r[1]
	S += c21_t3_mem1 <= c21_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage7MM1_stage1MAS5/FROB/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

