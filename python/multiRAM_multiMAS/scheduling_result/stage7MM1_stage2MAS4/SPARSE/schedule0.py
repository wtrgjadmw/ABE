from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 95
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	t1_t0_in += alt(MM_in)
	t1_t0 = S.Task('t1_t0', length=7, delay_cost=1)
	t1_t0 += alt(MM)
	S += t1_t0>=t1_t0_in

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	t1_t0_mem0 += MAIN_MEM_r[0]
	S += t1_t0_mem0 <= t1_t0

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	t1_t0_mem1 += MAIN_MEM_r[1]
	S += t1_t0_mem1 <= t1_t0

	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	t1_t1_in += alt(MM_in)
	t1_t1 = S.Task('t1_t1', length=7, delay_cost=1)
	t1_t1 += alt(MM)
	S += t1_t1>=t1_t1_in

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	t1_t1_mem0 += MAIN_MEM_r[0]
	S += t1_t1_mem0 <= t1_t1

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	t1_t1_mem1 += MAIN_MEM_r[1]
	S += t1_t1_mem1 <= t1_t1

	t1_t2 = S.Task('t1_t2', length=2, delay_cost=1)
	t1_t2 += alt(MAS)

	t1_t2_mem0 = S.Task('t1_t2_mem0', length=1, delay_cost=1)
	t1_t2_mem0 += MAIN_MEM_r[0]
	S += t1_t2_mem0 <= t1_t2

	t1_t2_mem1 = S.Task('t1_t2_mem1', length=1, delay_cost=1)
	t1_t2_mem1 += MAIN_MEM_r[1]
	S += t1_t2_mem1 <= t1_t2

	t1_t3 = S.Task('t1_t3', length=2, delay_cost=1)
	t1_t3 += alt(MAS)

	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	t1_t3_mem0 += MAIN_MEM_r[0]
	S += t1_t3_mem0 <= t1_t3

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	t1_t3_mem1 += MAIN_MEM_r[1]
	S += t1_t3_mem1 <= t1_t3

	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	t2_t0_in += alt(MM_in)
	t2_t0 = S.Task('t2_t0', length=7, delay_cost=1)
	t2_t0 += alt(MM)
	S += t2_t0>=t2_t0_in

	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	t2_t0_mem0 += MAIN_MEM_r[0]
	S += t2_t0_mem0 <= t2_t0

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	t2_t0_mem1 += MAIN_MEM_r[1]
	S += t2_t0_mem1 <= t2_t0

	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	t2_t1_in += alt(MM_in)
	t2_t1 = S.Task('t2_t1', length=7, delay_cost=1)
	t2_t1 += alt(MM)
	S += t2_t1>=t2_t1_in

	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	t2_t1_mem0 += MAIN_MEM_r[0]
	S += t2_t1_mem0 <= t2_t1

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	t2_t1_mem1 += MAIN_MEM_r[1]
	S += t2_t1_mem1 <= t2_t1

	t2_t2 = S.Task('t2_t2', length=2, delay_cost=1)
	t2_t2 += alt(MAS)

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	t2_t2_mem0 += MAIN_MEM_r[0]
	S += t2_t2_mem0 <= t2_t2

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	t2_t2_mem1 += MAIN_MEM_r[1]
	S += t2_t2_mem1 <= t2_t2

	t2_t3 = S.Task('t2_t3', length=2, delay_cost=1)
	t2_t3 += alt(MAS)

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	t2_t3_mem0 += MAIN_MEM_r[0]
	S += t2_t3_mem0 <= t2_t3

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	t2_t3_mem1 += MAIN_MEM_r[1]
	S += t2_t3_mem1 <= t2_t3

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	t0_t0_in += alt(MM_in)
	t0_t0 = S.Task('t0_t0', length=7, delay_cost=1)
	t0_t0 += alt(MM)
	S += t0_t0>=t0_t0_in

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	t0_t0_mem0 += MAIN_MEM_r[0]
	S += t0_t0_mem0 <= t0_t0

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	t0_t0_mem1 += MAIN_MEM_r[1]
	S += t0_t0_mem1 <= t0_t0

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	t0_t1_in += alt(MM_in)
	t0_t1 = S.Task('t0_t1', length=7, delay_cost=1)
	t0_t1 += alt(MM)
	S += t0_t1>=t0_t1_in

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	t0_t1_mem0 += MAIN_MEM_r[0]
	S += t0_t1_mem0 <= t0_t1

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	t0_t1_mem1 += MAIN_MEM_r[1]
	S += t0_t1_mem1 <= t0_t1

	t0_t2 = S.Task('t0_t2', length=2, delay_cost=1)
	t0_t2 += alt(MAS)

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	t0_t2_mem0 += MAIN_MEM_r[0]
	S += t0_t2_mem0 <= t0_t2

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	t0_t2_mem1 += MAIN_MEM_r[1]
	S += t0_t2_mem1 <= t0_t2

	t0_t3 = S.Task('t0_t3', length=2, delay_cost=1)
	t0_t3 += alt(MAS)

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	t0_t3_mem0 += MAIN_MEM_r[0]
	S += t0_t3_mem0 <= t0_t3

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	t0_t3_mem1 += MAIN_MEM_r[1]
	S += t0_t3_mem1 <= t0_t3

	t4_t0_t0_in = S.Task('t4_t0_t0_in', length=1, delay_cost=1)
	t4_t0_t0_in += alt(MM_in)
	t4_t0_t0 = S.Task('t4_t0_t0', length=7, delay_cost=1)
	t4_t0_t0 += alt(MM)
	S += t4_t0_t0>=t4_t0_t0_in

	t4_t0_t0_mem0 = S.Task('t4_t0_t0_mem0', length=1, delay_cost=1)
	t4_t0_t0_mem0 += MAIN_MEM_r[0]
	S += t4_t0_t0_mem0 <= t4_t0_t0

	t4_t0_t0_mem1 = S.Task('t4_t0_t0_mem1', length=1, delay_cost=1)
	t4_t0_t0_mem1 += MAIN_MEM_r[1]
	S += t4_t0_t0_mem1 <= t4_t0_t0

	t4_t0_t1_in = S.Task('t4_t0_t1_in', length=1, delay_cost=1)
	t4_t0_t1_in += alt(MM_in)
	t4_t0_t1 = S.Task('t4_t0_t1', length=7, delay_cost=1)
	t4_t0_t1 += alt(MM)
	S += t4_t0_t1>=t4_t0_t1_in

	t4_t0_t1_mem0 = S.Task('t4_t0_t1_mem0', length=1, delay_cost=1)
	t4_t0_t1_mem0 += MAIN_MEM_r[0]
	S += t4_t0_t1_mem0 <= t4_t0_t1

	t4_t0_t1_mem1 = S.Task('t4_t0_t1_mem1', length=1, delay_cost=1)
	t4_t0_t1_mem1 += MAIN_MEM_r[1]
	S += t4_t0_t1_mem1 <= t4_t0_t1

	t4_t0_t2 = S.Task('t4_t0_t2', length=2, delay_cost=1)
	t4_t0_t2 += alt(MAS)

	t4_t0_t2_mem0 = S.Task('t4_t0_t2_mem0', length=1, delay_cost=1)
	t4_t0_t2_mem0 += MAIN_MEM_r[0]
	S += t4_t0_t2_mem0 <= t4_t0_t2

	t4_t0_t2_mem1 = S.Task('t4_t0_t2_mem1', length=1, delay_cost=1)
	t4_t0_t2_mem1 += MAIN_MEM_r[1]
	S += t4_t0_t2_mem1 <= t4_t0_t2

	t4_t0_t3 = S.Task('t4_t0_t3', length=2, delay_cost=1)
	t4_t0_t3 += alt(MAS)

	t4_t0_t3_mem0 = S.Task('t4_t0_t3_mem0', length=1, delay_cost=1)
	t4_t0_t3_mem0 += MAIN_MEM_r[0]
	S += t4_t0_t3_mem0 <= t4_t0_t3

	t4_t0_t3_mem1 = S.Task('t4_t0_t3_mem1', length=1, delay_cost=1)
	t4_t0_t3_mem1 += MAIN_MEM_r[1]
	S += t4_t0_t3_mem1 <= t4_t0_t3

	t4_t1_t0_in = S.Task('t4_t1_t0_in', length=1, delay_cost=1)
	t4_t1_t0_in += alt(MM_in)
	t4_t1_t0 = S.Task('t4_t1_t0', length=7, delay_cost=1)
	t4_t1_t0 += alt(MM)
	S += t4_t1_t0>=t4_t1_t0_in

	t4_t1_t0_mem0 = S.Task('t4_t1_t0_mem0', length=1, delay_cost=1)
	t4_t1_t0_mem0 += MAIN_MEM_r[0]
	S += t4_t1_t0_mem0 <= t4_t1_t0

	t4_t1_t0_mem1 = S.Task('t4_t1_t0_mem1', length=1, delay_cost=1)
	t4_t1_t0_mem1 += MAIN_MEM_r[1]
	S += t4_t1_t0_mem1 <= t4_t1_t0

	t4_t1_t1_in = S.Task('t4_t1_t1_in', length=1, delay_cost=1)
	t4_t1_t1_in += alt(MM_in)
	t4_t1_t1 = S.Task('t4_t1_t1', length=7, delay_cost=1)
	t4_t1_t1 += alt(MM)
	S += t4_t1_t1>=t4_t1_t1_in

	t4_t1_t1_mem0 = S.Task('t4_t1_t1_mem0', length=1, delay_cost=1)
	t4_t1_t1_mem0 += MAIN_MEM_r[0]
	S += t4_t1_t1_mem0 <= t4_t1_t1

	t4_t1_t1_mem1 = S.Task('t4_t1_t1_mem1', length=1, delay_cost=1)
	t4_t1_t1_mem1 += MAIN_MEM_r[1]
	S += t4_t1_t1_mem1 <= t4_t1_t1

	t4_t1_t2 = S.Task('t4_t1_t2', length=2, delay_cost=1)
	t4_t1_t2 += alt(MAS)

	t4_t1_t2_mem0 = S.Task('t4_t1_t2_mem0', length=1, delay_cost=1)
	t4_t1_t2_mem0 += MAIN_MEM_r[0]
	S += t4_t1_t2_mem0 <= t4_t1_t2

	t4_t1_t2_mem1 = S.Task('t4_t1_t2_mem1', length=1, delay_cost=1)
	t4_t1_t2_mem1 += MAIN_MEM_r[1]
	S += t4_t1_t2_mem1 <= t4_t1_t2

	t4_t1_t3 = S.Task('t4_t1_t3', length=2, delay_cost=1)
	t4_t1_t3 += alt(MAS)

	t4_t1_t3_mem0 = S.Task('t4_t1_t3_mem0', length=1, delay_cost=1)
	t4_t1_t3_mem0 += MAIN_MEM_r[0]
	S += t4_t1_t3_mem0 <= t4_t1_t3

	t4_t1_t3_mem1 = S.Task('t4_t1_t3_mem1', length=1, delay_cost=1)
	t4_t1_t3_mem1 += MAIN_MEM_r[1]
	S += t4_t1_t3_mem1 <= t4_t1_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage7MM1_stage2MAS4/SPARSE/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

