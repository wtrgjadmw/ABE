from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling

	# new tasks
	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	t0_in += alt(MM_in)
	t0 = S.Task('t0', length=5, delay_cost=1)
	t0 += alt(MM)
	S += t0>=t0_in

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	t0_mem0 += MAIN_MEM_r
	S += t0_mem0 <= t0

	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	t1_in += alt(MM_in)
	t1 = S.Task('t1', length=5, delay_cost=1)
	t1 += alt(MM)
	S += t1>=t1_in

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	t1_mem0 += MAIN_MEM_r
	S += t1_mem0 <= t1

	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	t2_in += alt(MM_in)
	t2 = S.Task('t2', length=5, delay_cost=1)
	t2 += alt(MM)
	S += t2>=t2_in

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	t2_mem0 += MAIN_MEM_r
	S += t2_mem0 <= t2

	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	t3_in += alt(MM_in)
	t3 = S.Task('t3', length=5, delay_cost=1)
	t3 += alt(MM)
	S += t3>=t3_in

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	t3_mem0 += MAIN_MEM_r
	S += t3_mem0 <= t3

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	t3_mem1 += MAIN_MEM_r
	S += t3_mem1 <= t3

	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	t5_in += alt(MM_in)
	t5 = S.Task('t5', length=5, delay_cost=1)
	t5 += alt(MM)
	S += t5>=t5_in

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	t5_mem0 += MAIN_MEM_r
	S += t5_mem0 <= t5

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	t5_mem1 += MAIN_MEM_r
	S += t5_mem1 <= t5

	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	t23_in += alt(MM_in)
	t23 = S.Task('t23', length=5, delay_cost=1)
	t23 += alt(MM)
	S += t23>=t23_in

	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	t23_mem0 += MAIN_MEM_r
	S += t23_mem0 <= t23

	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	t23_mem1 += MAIN_MEM_r
	S += t23_mem1 <= t23

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/EP_DBL_A_ANY/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

