from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4, size=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resource('MAIN_MEM_r', size=2)

	# result of previous scheduling

	# new tasks
	T1_in = S.Task('T1_in', length=1, delay_cost=1)
	T1_in += alt(MM_in)
	T1 = S.Task('T1', length=5, delay_cost=1)
	T1 += alt(MM)
	S += T1>=T1_in

	T1_mem0 = S.Task('T1_mem0', length=1, delay_cost=1)
	T1_mem0 += MAIN_MEM_r
	S += T1_mem0 <= T1

	T1_mem1 = S.Task('T1_mem1', length=1, delay_cost=1)
	T1_mem1 += MAIN_MEM_r
	S += T1_mem1 <= T1

	T2_in = S.Task('T2_in', length=1, delay_cost=1)
	T2_in += alt(MM_in)
	T2 = S.Task('T2', length=5, delay_cost=1)
	T2 += alt(MM)
	S += T2>=T2_in

	T2_mem0 = S.Task('T2_mem0', length=1, delay_cost=1)
	T2_mem0 += MAIN_MEM_r
	S += T2_mem0 <= T2

	T2_mem1 = S.Task('T2_mem1', length=1, delay_cost=1)
	T2_mem1 += MAIN_MEM_r
	S += T2_mem1 <= T2

	T3_in = S.Task('T3_in', length=1, delay_cost=1)
	T3_in += alt(MM_in)
	T3 = S.Task('T3', length=5, delay_cost=1)
	T3 += alt(MM)
	S += T3>=T3_in

	T3_mem0 = S.Task('T3_mem0', length=1, delay_cost=1)
	T3_mem0 += MAIN_MEM_r
	S += T3_mem0 <= T3

	T3_mem1 = S.Task('T3_mem1', length=1, delay_cost=1)
	T3_mem1 += MAIN_MEM_r
	S += T3_mem1 <= T3

	T4_in = S.Task('T4_in', length=1, delay_cost=1)
	T4_in += alt(MM_in)
	T4 = S.Task('T4', length=5, delay_cost=1)
	T4 += alt(MM)
	S += T4>=T4_in

	T4_mem0 = S.Task('T4_mem0', length=1, delay_cost=1)
	T4_mem0 += MAIN_MEM_r
	S += T4_mem0 <= T4

	T4_mem1 = S.Task('T4_mem1', length=1, delay_cost=1)
	T4_mem1 += MAIN_MEM_r
	S += T4_mem1 <= T4

	T5_in = S.Task('T5_in', length=1, delay_cost=1)
	T5_in += alt(MM_in)
	T5 = S.Task('T5', length=5, delay_cost=1)
	T5 += alt(MM)
	S += T5>=T5_in

	T5_mem0 = S.Task('T5_mem0', length=1, delay_cost=1)
	T5_mem0 += MAIN_MEM_r
	S += T5_mem0 <= T5

	T5_mem1 = S.Task('T5_mem1', length=1, delay_cost=1)
	T5_mem1 += MAIN_MEM_r
	S += T5_mem1 <= T5

	T6_in = S.Task('T6_in', length=1, delay_cost=1)
	T6_in += alt(MM_in)
	T6 = S.Task('T6', length=5, delay_cost=1)
	T6 += alt(MM)
	S += T6>=T6_in

	T6_mem0 = S.Task('T6_mem0', length=1, delay_cost=1)
	T6_mem0 += MAIN_MEM_r
	S += T6_mem0 <= T6

	T6_mem1 = S.Task('T6_mem1', length=1, delay_cost=1)
	T6_mem1 += MAIN_MEM_r
	S += T6_mem1 <= T6

	T7_in = S.Task('T7_in', length=1, delay_cost=1)
	T7_in += alt(MM_in)
	T7 = S.Task('T7', length=5, delay_cost=1)
	T7 += alt(MM)
	S += T7>=T7_in

	T7_mem0 = S.Task('T7_mem0', length=1, delay_cost=1)
	T7_mem0 += MAIN_MEM_r
	S += T7_mem0 <= T7

	T7_mem1 = S.Task('T7_mem1', length=1, delay_cost=1)
	T7_mem1 += MAIN_MEM_r
	S += T7_mem1 <= T7

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/ladderMul/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

