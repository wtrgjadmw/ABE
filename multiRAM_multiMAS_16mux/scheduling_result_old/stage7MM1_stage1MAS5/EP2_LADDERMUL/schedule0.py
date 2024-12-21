from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	T1_t0 = S.Task('T1_t0', length=1, delay_cost=1)
	T1_t0 += alt(MAS)

	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	T1_t0_mem0 += MAIN_MEM_r[0]
	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	T1_t0_mem1 += MAIN_MEM_r[1]
	T1_t1 = S.Task('T1_t1', length=1, delay_cost=1)
	T1_t1 += alt(MAS)

	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	T1_t1_mem0 += MAIN_MEM_r[0]
	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	T1_t1_mem1 += MAIN_MEM_r[1]
	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	T1_t3_in += alt(MM_in)
	T1_t3 = S.Task('T1_t3', length=7, delay_cost=1)
	T1_t3 += alt(MM)
	S += T1_t3>=T1_t3_in

	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	T1_t3_mem0 += MAIN_MEM_r[0]
	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	T1_t3_mem1 += MAIN_MEM_r[1]
	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	T2_t0_in += alt(MM_in)
	T2_t0 = S.Task('T2_t0', length=7, delay_cost=1)
	T2_t0 += alt(MM)
	S += T2_t0>=T2_t0_in

	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	T2_t0_mem0 += MAIN_MEM_r[0]
	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	T2_t0_mem1 += MAIN_MEM_r[1]
	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	T2_t1_in += alt(MM_in)
	T2_t1 = S.Task('T2_t1', length=7, delay_cost=1)
	T2_t1 += alt(MM)
	S += T2_t1>=T2_t1_in

	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	T2_t1_mem0 += MAIN_MEM_r[0]
	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	T2_t1_mem1 += MAIN_MEM_r[1]
	T2_t2 = S.Task('T2_t2', length=1, delay_cost=1)
	T2_t2 += alt(MAS)

	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	T2_t2_mem0 += MAIN_MEM_r[0]
	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	T2_t2_mem1 += MAIN_MEM_r[1]
	T2_t3 = S.Task('T2_t3', length=1, delay_cost=1)
	T2_t3 += alt(MAS)

	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	T2_t3_mem0 += MAIN_MEM_r[0]
	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	T2_t3_mem1 += MAIN_MEM_r[1]
	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	T3_t0_in += alt(MM_in)
	T3_t0 = S.Task('T3_t0', length=7, delay_cost=1)
	T3_t0 += alt(MM)
	S += T3_t0>=T3_t0_in

	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	T3_t0_mem0 += MAIN_MEM_r[0]
	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	T3_t0_mem1 += MAIN_MEM_r[1]
	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	T3_t1_in += alt(MM_in)
	T3_t1 = S.Task('T3_t1', length=7, delay_cost=1)
	T3_t1 += alt(MM)
	S += T3_t1>=T3_t1_in

	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	T3_t1_mem0 += MAIN_MEM_r[0]
	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	T3_t1_mem1 += MAIN_MEM_r[1]
	T3_t2 = S.Task('T3_t2', length=1, delay_cost=1)
	T3_t2 += alt(MAS)

	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	T3_t2_mem0 += MAIN_MEM_r[0]
	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	T3_t2_mem1 += MAIN_MEM_r[1]
	T3_t3 = S.Task('T3_t3', length=1, delay_cost=1)
	T3_t3 += alt(MAS)

	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	T3_t3_mem0 += MAIN_MEM_r[0]
	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	T3_t3_mem1 += MAIN_MEM_r[1]
	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	T4_t0_in += alt(MM_in)
	T4_t0 = S.Task('T4_t0', length=7, delay_cost=1)
	T4_t0 += alt(MM)
	S += T4_t0>=T4_t0_in

	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	T4_t0_mem0 += MAIN_MEM_r[0]
	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	T4_t0_mem1 += MAIN_MEM_r[1]
	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	T4_t1_in += alt(MM_in)
	T4_t1 = S.Task('T4_t1', length=7, delay_cost=1)
	T4_t1 += alt(MM)
	S += T4_t1>=T4_t1_in

	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	T4_t1_mem0 += MAIN_MEM_r[0]
	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	T4_t1_mem1 += MAIN_MEM_r[1]
	T4_t2 = S.Task('T4_t2', length=1, delay_cost=1)
	T4_t2 += alt(MAS)

	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	T4_t2_mem0 += MAIN_MEM_r[0]
	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	T4_t2_mem1 += MAIN_MEM_r[1]
	T4_t3 = S.Task('T4_t3', length=1, delay_cost=1)
	T4_t3 += alt(MAS)

	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	T4_t3_mem0 += MAIN_MEM_r[0]
	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	T4_t3_mem1 += MAIN_MEM_r[1]
	T5_t0 = S.Task('T5_t0', length=1, delay_cost=1)
	T5_t0 += alt(MAS)

	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	T5_t0_mem0 += MAIN_MEM_r[0]
	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	T5_t0_mem1 += MAIN_MEM_r[1]
	T5_t1 = S.Task('T5_t1', length=1, delay_cost=1)
	T5_t1 += alt(MAS)

	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	T5_t1_mem0 += MAIN_MEM_r[0]
	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	T5_t1_mem1 += MAIN_MEM_r[1]
	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	T5_t3_in += alt(MM_in)
	T5_t3 = S.Task('T5_t3', length=7, delay_cost=1)
	T5_t3 += alt(MM)
	S += T5_t3>=T5_t3_in

	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	T5_t3_mem0 += MAIN_MEM_r[0]
	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	T5_t3_mem1 += MAIN_MEM_r[1]
	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	T6_t0_in += alt(MM_in)
	T6_t0 = S.Task('T6_t0', length=7, delay_cost=1)
	T6_t0 += alt(MM)
	S += T6_t0>=T6_t0_in

	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	T6_t0_mem0 += MAIN_MEM_r[0]
	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	T6_t0_mem1 += MAIN_MEM_r[1]
	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	T6_t1_in += alt(MM_in)
	T6_t1 = S.Task('T6_t1', length=7, delay_cost=1)
	T6_t1 += alt(MM)
	S += T6_t1>=T6_t1_in

	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	T6_t1_mem0 += MAIN_MEM_r[0]
	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	T6_t1_mem1 += MAIN_MEM_r[1]
	T6_t2 = S.Task('T6_t2', length=1, delay_cost=1)
	T6_t2 += alt(MAS)

	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	T6_t2_mem0 += MAIN_MEM_r[0]
	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	T6_t2_mem1 += MAIN_MEM_r[1]
	T6_t3 = S.Task('T6_t3', length=1, delay_cost=1)
	T6_t3 += alt(MAS)

	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	T6_t3_mem0 += MAIN_MEM_r[0]
	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	T6_t3_mem1 += MAIN_MEM_r[1]
	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	T7_t0_in += alt(MM_in)
	T7_t0 = S.Task('T7_t0', length=7, delay_cost=1)
	T7_t0 += alt(MM)
	S += T7_t0>=T7_t0_in

	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	T7_t0_mem0 += MAIN_MEM_r[0]
	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	T7_t0_mem1 += MAIN_MEM_r[1]
	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	T7_t1_in += alt(MM_in)
	T7_t1 = S.Task('T7_t1', length=7, delay_cost=1)
	T7_t1 += alt(MM)
	S += T7_t1>=T7_t1_in

	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	T7_t1_mem0 += MAIN_MEM_r[0]
	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	T7_t1_mem1 += MAIN_MEM_r[1]
	T7_t2 = S.Task('T7_t2', length=1, delay_cost=1)
	T7_t2 += alt(MAS)

	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	T7_t2_mem0 += MAIN_MEM_r[0]
	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	T7_t2_mem1 += MAIN_MEM_r[1]
	T7_t3 = S.Task('T7_t3', length=1, delay_cost=1)
	T7_t3 += alt(MAS)

	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	T7_t3_mem0 += MAIN_MEM_r[0]
	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	T7_t3_mem1 += MAIN_MEM_r[1]
	T8_t2 = S.Task('T8_t2', length=1, delay_cost=1)
	T8_t2 += alt(MAS)

	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	T8_t2_mem0 += MAIN_MEM_r[0]
	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	T8_t2_mem1 += MAIN_MEM_r[1]
	T9_t2 = S.Task('T9_t2', length=1, delay_cost=1)
	T9_t2 += alt(MAS)

	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	T9_t2_mem0 += MAIN_MEM_r[0]
	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	T9_t2_mem1 += MAIN_MEM_r[1]
	T10_t2 = S.Task('T10_t2', length=1, delay_cost=1)
	T10_t2 += alt(MAS)

	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	T10_t2_mem0 += MAIN_MEM_r[0]
	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	T10_t2_mem1 += MAIN_MEM_r[1]
	T11_t2 = S.Task('T11_t2', length=1, delay_cost=1)
	T11_t2 += alt(MAS)

	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	T11_t2_mem0 += MAIN_MEM_r[0]
	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	T11_t2_mem1 += MAIN_MEM_r[1]
	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM1_stage1MAS5/EP2_LADDERMUL/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

