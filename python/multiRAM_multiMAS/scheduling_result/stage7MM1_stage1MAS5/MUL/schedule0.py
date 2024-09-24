from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 110
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
	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	c_t0_t0_t0_in += alt(MM_in)
	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=7, delay_cost=1)
	c_t0_t0_t0 += alt(MM)
	S += c_t0_t0_t0>=c_t0_t0_t0_in

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c_t0_t0_t0_mem0 <= c_t0_t0_t0

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_t0_t0_t0_mem1 <= c_t0_t0_t0

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	c_t0_t0_t1_in += alt(MM_in)
	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=7, delay_cost=1)
	c_t0_t0_t1 += alt(MM)
	S += c_t0_t0_t1>=c_t0_t0_t1_in

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c_t0_t0_t1_mem0 <= c_t0_t0_t1

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_t0_t0_t1_mem1 <= c_t0_t0_t1

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=1, delay_cost=1)
	c_t0_t0_t2 += alt(MAS)

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c_t0_t0_t2_mem0 <= c_t0_t0_t2

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c_t0_t0_t2_mem1 <= c_t0_t0_t2

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=1, delay_cost=1)
	c_t0_t0_t3 += alt(MAS)

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_t0_t0_t3_mem0 <= c_t0_t0_t3

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_t0_t0_t3_mem1 <= c_t0_t0_t3

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	c_t0_t1_t0_in += alt(MM_in)
	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=7, delay_cost=1)
	c_t0_t1_t0 += alt(MM)
	S += c_t0_t1_t0>=c_t0_t1_t0_in

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c_t0_t1_t0_mem0 <= c_t0_t1_t0

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_t0_t1_t0_mem1 <= c_t0_t1_t0

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	c_t0_t1_t1_in += alt(MM_in)
	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=7, delay_cost=1)
	c_t0_t1_t1 += alt(MM)
	S += c_t0_t1_t1>=c_t0_t1_t1_in

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c_t0_t1_t1_mem0 <= c_t0_t1_t1

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_t0_t1_t1_mem1 <= c_t0_t1_t1

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=1, delay_cost=1)
	c_t0_t1_t2 += alt(MAS)

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c_t0_t1_t2_mem0 <= c_t0_t1_t2

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c_t0_t1_t2_mem1 <= c_t0_t1_t2

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=1, delay_cost=1)
	c_t0_t1_t3 += alt(MAS)

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_t0_t1_t3_mem0 <= c_t0_t1_t3

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_t0_t1_t3_mem1 <= c_t0_t1_t3

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	c_t0_t20 += alt(MAS)

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	c_t0_t20_mem0 += MAIN_MEM_r[0]
	S += c_t0_t20_mem0 <= c_t0_t20

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	c_t0_t20_mem1 += MAIN_MEM_r[1]
	S += c_t0_t20_mem1 <= c_t0_t20

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	c_t0_t21 += alt(MAS)

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	c_t0_t21_mem0 += MAIN_MEM_r[0]
	S += c_t0_t21_mem0 <= c_t0_t21

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	c_t0_t21_mem1 += MAIN_MEM_r[1]
	S += c_t0_t21_mem1 <= c_t0_t21

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	c_t0_t30 += alt(MAS)

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	c_t0_t30_mem0 += MAIN_MEM_r[0]
	S += c_t0_t30_mem0 <= c_t0_t30

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	c_t0_t30_mem1 += MAIN_MEM_r[1]
	S += c_t0_t30_mem1 <= c_t0_t30

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	c_t0_t31 += alt(MAS)

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	c_t0_t31_mem0 += MAIN_MEM_r[0]
	S += c_t0_t31_mem0 <= c_t0_t31

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	c_t0_t31_mem1 += MAIN_MEM_r[1]
	S += c_t0_t31_mem1 <= c_t0_t31

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	c_t1_t0_t0_in += alt(MM_in)
	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=7, delay_cost=1)
	c_t1_t0_t0 += alt(MM)
	S += c_t1_t0_t0>=c_t1_t0_t0_in

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c_t1_t0_t0_mem0 <= c_t1_t0_t0

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_t1_t0_t0_mem1 <= c_t1_t0_t0

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	c_t1_t0_t1_in += alt(MM_in)
	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=7, delay_cost=1)
	c_t1_t0_t1 += alt(MM)
	S += c_t1_t0_t1>=c_t1_t0_t1_in

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c_t1_t0_t1_mem0 <= c_t1_t0_t1

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_t1_t0_t1_mem1 <= c_t1_t0_t1

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=1, delay_cost=1)
	c_t1_t0_t2 += alt(MAS)

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c_t1_t0_t2_mem0 <= c_t1_t0_t2

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c_t1_t0_t2_mem1 <= c_t1_t0_t2

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=1, delay_cost=1)
	c_t1_t0_t3 += alt(MAS)

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_t1_t0_t3_mem0 <= c_t1_t0_t3

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_t1_t0_t3_mem1 <= c_t1_t0_t3

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	c_t1_t1_t0_in += alt(MM_in)
	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=7, delay_cost=1)
	c_t1_t1_t0 += alt(MM)
	S += c_t1_t1_t0>=c_t1_t1_t0_in

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c_t1_t1_t0_mem0 <= c_t1_t1_t0

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_t1_t1_t0_mem1 <= c_t1_t1_t0

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	c_t1_t1_t1_in += alt(MM_in)
	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=7, delay_cost=1)
	c_t1_t1_t1 += alt(MM)
	S += c_t1_t1_t1>=c_t1_t1_t1_in

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c_t1_t1_t1_mem0 <= c_t1_t1_t1

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_t1_t1_t1_mem1 <= c_t1_t1_t1

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=1, delay_cost=1)
	c_t1_t1_t2 += alt(MAS)

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c_t1_t1_t2_mem0 <= c_t1_t1_t2

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c_t1_t1_t2_mem1 <= c_t1_t1_t2

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=1, delay_cost=1)
	c_t1_t1_t3 += alt(MAS)

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_t1_t1_t3_mem0 <= c_t1_t1_t3

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_t1_t1_t3_mem1 <= c_t1_t1_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage7MM1_stage1MAS5/MUL/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

