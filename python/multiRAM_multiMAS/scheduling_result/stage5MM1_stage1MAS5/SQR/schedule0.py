from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
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

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	c_t0_t3_t0_in += alt(MM_in)
	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=5, delay_cost=1)
	c_t0_t3_t0 += alt(MM)
	S += c_t0_t3_t0>=c_t0_t3_t0_in

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	c_t0_t3_t0_mem0 += MAIN_MEM_r[0]
	S += c_t0_t3_t0_mem0 <= c_t0_t3_t0

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	c_t0_t3_t0_mem1 += MAIN_MEM_r[1]
	S += c_t0_t3_t0_mem1 <= c_t0_t3_t0

	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	c_t0_t3_t1_in += alt(MM_in)
	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=5, delay_cost=1)
	c_t0_t3_t1 += alt(MM)
	S += c_t0_t3_t1>=c_t0_t3_t1_in

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

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	c_t1_t3_t0_in += alt(MM_in)
	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=5, delay_cost=1)
	c_t1_t3_t0 += alt(MM)
	S += c_t1_t3_t0>=c_t1_t3_t0_in

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	c_t1_t3_t0_mem0 += MAIN_MEM_r[0]
	S += c_t1_t3_t0_mem0 <= c_t1_t3_t0

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	c_t1_t3_t0_mem1 += MAIN_MEM_r[1]
	S += c_t1_t3_t0_mem1 <= c_t1_t3_t0

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	c_t1_t3_t1_in += alt(MM_in)
	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=5, delay_cost=1)
	c_t1_t3_t1 += alt(MM)
	S += c_t1_t3_t1>=c_t1_t3_t1_in

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

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS5/SQR/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

