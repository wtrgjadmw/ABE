from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=5)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	T1_t0 = S.Task('T1_t0', length=1, delay_cost=1)
	T1_t0 += alt(MAS)
	T1_t0_mem0 = S.Task('T1_t0_mem0', length=1, delay_cost=1)
	T1_t0_mem0 += MAIN_MEM_r[0]
	S += T1_t0_mem0 <= T1_t0

	T1_t0_mem1 = S.Task('T1_t0_mem1', length=1, delay_cost=1)
	T1_t0_mem1 += MAIN_MEM_r[1]
	S += T1_t0_mem1 <= T1_t0

	T1_t1 = S.Task('T1_t1', length=1, delay_cost=1)
	T1_t1 += alt(MAS)
	T1_t1_mem0 = S.Task('T1_t1_mem0', length=1, delay_cost=1)
	T1_t1_mem0 += MAIN_MEM_r[0]
	S += T1_t1_mem0 <= T1_t1

	T1_t1_mem1 = S.Task('T1_t1_mem1', length=1, delay_cost=1)
	T1_t1_mem1 += MAIN_MEM_r[1]
	S += T1_t1_mem1 <= T1_t1

	T1_t3 = S.Task('T1_t3', length=5, delay_cost=1)
	T1_t3 += alt(MM)
	T1_t3_in = S.Task('T1_t3_in', length=1, delay_cost=1)
	T1_t3_in += alt(MM_in)
	S += T1_t3_in*MM_in[0]<=T1_t3*MM[0]
	S += T1_t3_in*MM_in[1]<=T1_t3*MM[1]
	T1_t3_mem0 = S.Task('T1_t3_mem0', length=1, delay_cost=1)
	T1_t3_mem0 += MAIN_MEM_r[0]
	S += T1_t3_mem0 <= T1_t3

	T1_t3_mem1 = S.Task('T1_t3_mem1', length=1, delay_cost=1)
	T1_t3_mem1 += MAIN_MEM_r[1]
	S += T1_t3_mem1 <= T1_t3

	T2_t0 = S.Task('T2_t0', length=5, delay_cost=1)
	T2_t0 += alt(MM)
	T2_t0_in = S.Task('T2_t0_in', length=1, delay_cost=1)
	T2_t0_in += alt(MM_in)
	S += T2_t0_in*MM_in[0]<=T2_t0*MM[0]
	S += T2_t0_in*MM_in[1]<=T2_t0*MM[1]
	T2_t0_mem0 = S.Task('T2_t0_mem0', length=1, delay_cost=1)
	T2_t0_mem0 += MAIN_MEM_r[0]
	S += T2_t0_mem0 <= T2_t0

	T2_t0_mem1 = S.Task('T2_t0_mem1', length=1, delay_cost=1)
	T2_t0_mem1 += MAIN_MEM_r[1]
	S += T2_t0_mem1 <= T2_t0

	T2_t1 = S.Task('T2_t1', length=5, delay_cost=1)
	T2_t1 += alt(MM)
	T2_t1_in = S.Task('T2_t1_in', length=1, delay_cost=1)
	T2_t1_in += alt(MM_in)
	S += T2_t1_in*MM_in[0]<=T2_t1*MM[0]
	S += T2_t1_in*MM_in[1]<=T2_t1*MM[1]
	T2_t1_mem0 = S.Task('T2_t1_mem0', length=1, delay_cost=1)
	T2_t1_mem0 += MAIN_MEM_r[0]
	S += T2_t1_mem0 <= T2_t1

	T2_t1_mem1 = S.Task('T2_t1_mem1', length=1, delay_cost=1)
	T2_t1_mem1 += MAIN_MEM_r[1]
	S += T2_t1_mem1 <= T2_t1

	T2_t2 = S.Task('T2_t2', length=1, delay_cost=1)
	T2_t2 += alt(MAS)
	T2_t2_mem0 = S.Task('T2_t2_mem0', length=1, delay_cost=1)
	T2_t2_mem0 += MAIN_MEM_r[0]
	S += T2_t2_mem0 <= T2_t2

	T2_t2_mem1 = S.Task('T2_t2_mem1', length=1, delay_cost=1)
	T2_t2_mem1 += MAIN_MEM_r[1]
	S += T2_t2_mem1 <= T2_t2

	T2_t3 = S.Task('T2_t3', length=1, delay_cost=1)
	T2_t3 += alt(MAS)
	T2_t3_mem0 = S.Task('T2_t3_mem0', length=1, delay_cost=1)
	T2_t3_mem0 += MAIN_MEM_r[0]
	S += T2_t3_mem0 <= T2_t3

	T2_t3_mem1 = S.Task('T2_t3_mem1', length=1, delay_cost=1)
	T2_t3_mem1 += MAIN_MEM_r[1]
	S += T2_t3_mem1 <= T2_t3

	T3_t0 = S.Task('T3_t0', length=5, delay_cost=1)
	T3_t0 += alt(MM)
	T3_t0_in = S.Task('T3_t0_in', length=1, delay_cost=1)
	T3_t0_in += alt(MM_in)
	S += T3_t0_in*MM_in[0]<=T3_t0*MM[0]
	S += T3_t0_in*MM_in[1]<=T3_t0*MM[1]
	T3_t0_mem0 = S.Task('T3_t0_mem0', length=1, delay_cost=1)
	T3_t0_mem0 += MAIN_MEM_r[0]
	S += T3_t0_mem0 <= T3_t0

	T3_t0_mem1 = S.Task('T3_t0_mem1', length=1, delay_cost=1)
	T3_t0_mem1 += MAIN_MEM_r[1]
	S += T3_t0_mem1 <= T3_t0

	T3_t1 = S.Task('T3_t1', length=5, delay_cost=1)
	T3_t1 += alt(MM)
	T3_t1_in = S.Task('T3_t1_in', length=1, delay_cost=1)
	T3_t1_in += alt(MM_in)
	S += T3_t1_in*MM_in[0]<=T3_t1*MM[0]
	S += T3_t1_in*MM_in[1]<=T3_t1*MM[1]
	T3_t1_mem0 = S.Task('T3_t1_mem0', length=1, delay_cost=1)
	T3_t1_mem0 += MAIN_MEM_r[0]
	S += T3_t1_mem0 <= T3_t1

	T3_t1_mem1 = S.Task('T3_t1_mem1', length=1, delay_cost=1)
	T3_t1_mem1 += MAIN_MEM_r[1]
	S += T3_t1_mem1 <= T3_t1

	T3_t2 = S.Task('T3_t2', length=1, delay_cost=1)
	T3_t2 += alt(MAS)
	T3_t2_mem0 = S.Task('T3_t2_mem0', length=1, delay_cost=1)
	T3_t2_mem0 += MAIN_MEM_r[0]
	S += T3_t2_mem0 <= T3_t2

	T3_t2_mem1 = S.Task('T3_t2_mem1', length=1, delay_cost=1)
	T3_t2_mem1 += MAIN_MEM_r[1]
	S += T3_t2_mem1 <= T3_t2

	T3_t3 = S.Task('T3_t3', length=1, delay_cost=1)
	T3_t3 += alt(MAS)
	T3_t3_mem0 = S.Task('T3_t3_mem0', length=1, delay_cost=1)
	T3_t3_mem0 += MAIN_MEM_r[0]
	S += T3_t3_mem0 <= T3_t3

	T3_t3_mem1 = S.Task('T3_t3_mem1', length=1, delay_cost=1)
	T3_t3_mem1 += MAIN_MEM_r[1]
	S += T3_t3_mem1 <= T3_t3

	T4_t0 = S.Task('T4_t0', length=5, delay_cost=1)
	T4_t0 += alt(MM)
	T4_t0_in = S.Task('T4_t0_in', length=1, delay_cost=1)
	T4_t0_in += alt(MM_in)
	S += T4_t0_in*MM_in[0]<=T4_t0*MM[0]
	S += T4_t0_in*MM_in[1]<=T4_t0*MM[1]
	T4_t0_mem0 = S.Task('T4_t0_mem0', length=1, delay_cost=1)
	T4_t0_mem0 += MAIN_MEM_r[0]
	S += T4_t0_mem0 <= T4_t0

	T4_t0_mem1 = S.Task('T4_t0_mem1', length=1, delay_cost=1)
	T4_t0_mem1 += MAIN_MEM_r[1]
	S += T4_t0_mem1 <= T4_t0

	T4_t1 = S.Task('T4_t1', length=5, delay_cost=1)
	T4_t1 += alt(MM)
	T4_t1_in = S.Task('T4_t1_in', length=1, delay_cost=1)
	T4_t1_in += alt(MM_in)
	S += T4_t1_in*MM_in[0]<=T4_t1*MM[0]
	S += T4_t1_in*MM_in[1]<=T4_t1*MM[1]
	T4_t1_mem0 = S.Task('T4_t1_mem0', length=1, delay_cost=1)
	T4_t1_mem0 += MAIN_MEM_r[0]
	S += T4_t1_mem0 <= T4_t1

	T4_t1_mem1 = S.Task('T4_t1_mem1', length=1, delay_cost=1)
	T4_t1_mem1 += MAIN_MEM_r[1]
	S += T4_t1_mem1 <= T4_t1

	T4_t2 = S.Task('T4_t2', length=1, delay_cost=1)
	T4_t2 += alt(MAS)
	T4_t2_mem0 = S.Task('T4_t2_mem0', length=1, delay_cost=1)
	T4_t2_mem0 += MAIN_MEM_r[0]
	S += T4_t2_mem0 <= T4_t2

	T4_t2_mem1 = S.Task('T4_t2_mem1', length=1, delay_cost=1)
	T4_t2_mem1 += MAIN_MEM_r[1]
	S += T4_t2_mem1 <= T4_t2

	T4_t3 = S.Task('T4_t3', length=1, delay_cost=1)
	T4_t3 += alt(MAS)
	T4_t3_mem0 = S.Task('T4_t3_mem0', length=1, delay_cost=1)
	T4_t3_mem0 += MAIN_MEM_r[0]
	S += T4_t3_mem0 <= T4_t3

	T4_t3_mem1 = S.Task('T4_t3_mem1', length=1, delay_cost=1)
	T4_t3_mem1 += MAIN_MEM_r[1]
	S += T4_t3_mem1 <= T4_t3

	T5_t0 = S.Task('T5_t0', length=1, delay_cost=1)
	T5_t0 += alt(MAS)
	T5_t0_mem0 = S.Task('T5_t0_mem0', length=1, delay_cost=1)
	T5_t0_mem0 += MAIN_MEM_r[0]
	S += T5_t0_mem0 <= T5_t0

	T5_t0_mem1 = S.Task('T5_t0_mem1', length=1, delay_cost=1)
	T5_t0_mem1 += MAIN_MEM_r[1]
	S += T5_t0_mem1 <= T5_t0

	T5_t1 = S.Task('T5_t1', length=1, delay_cost=1)
	T5_t1 += alt(MAS)
	T5_t1_mem0 = S.Task('T5_t1_mem0', length=1, delay_cost=1)
	T5_t1_mem0 += MAIN_MEM_r[0]
	S += T5_t1_mem0 <= T5_t1

	T5_t1_mem1 = S.Task('T5_t1_mem1', length=1, delay_cost=1)
	T5_t1_mem1 += MAIN_MEM_r[1]
	S += T5_t1_mem1 <= T5_t1

	T5_t3 = S.Task('T5_t3', length=5, delay_cost=1)
	T5_t3 += alt(MM)
	T5_t3_in = S.Task('T5_t3_in', length=1, delay_cost=1)
	T5_t3_in += alt(MM_in)
	S += T5_t3_in*MM_in[0]<=T5_t3*MM[0]
	S += T5_t3_in*MM_in[1]<=T5_t3*MM[1]
	T5_t3_mem0 = S.Task('T5_t3_mem0', length=1, delay_cost=1)
	T5_t3_mem0 += MAIN_MEM_r[0]
	S += T5_t3_mem0 <= T5_t3

	T5_t3_mem1 = S.Task('T5_t3_mem1', length=1, delay_cost=1)
	T5_t3_mem1 += MAIN_MEM_r[1]
	S += T5_t3_mem1 <= T5_t3

	T6_t0 = S.Task('T6_t0', length=5, delay_cost=1)
	T6_t0 += alt(MM)
	T6_t0_in = S.Task('T6_t0_in', length=1, delay_cost=1)
	T6_t0_in += alt(MM_in)
	S += T6_t0_in*MM_in[0]<=T6_t0*MM[0]
	S += T6_t0_in*MM_in[1]<=T6_t0*MM[1]
	T6_t0_mem0 = S.Task('T6_t0_mem0', length=1, delay_cost=1)
	T6_t0_mem0 += MAIN_MEM_r[0]
	S += T6_t0_mem0 <= T6_t0

	T6_t0_mem1 = S.Task('T6_t0_mem1', length=1, delay_cost=1)
	T6_t0_mem1 += MAIN_MEM_r[1]
	S += T6_t0_mem1 <= T6_t0

	T6_t1 = S.Task('T6_t1', length=5, delay_cost=1)
	T6_t1 += alt(MM)
	T6_t1_in = S.Task('T6_t1_in', length=1, delay_cost=1)
	T6_t1_in += alt(MM_in)
	S += T6_t1_in*MM_in[0]<=T6_t1*MM[0]
	S += T6_t1_in*MM_in[1]<=T6_t1*MM[1]
	T6_t1_mem0 = S.Task('T6_t1_mem0', length=1, delay_cost=1)
	T6_t1_mem0 += MAIN_MEM_r[0]
	S += T6_t1_mem0 <= T6_t1

	T6_t1_mem1 = S.Task('T6_t1_mem1', length=1, delay_cost=1)
	T6_t1_mem1 += MAIN_MEM_r[1]
	S += T6_t1_mem1 <= T6_t1

	T6_t2 = S.Task('T6_t2', length=1, delay_cost=1)
	T6_t2 += alt(MAS)
	T6_t2_mem0 = S.Task('T6_t2_mem0', length=1, delay_cost=1)
	T6_t2_mem0 += MAIN_MEM_r[0]
	S += T6_t2_mem0 <= T6_t2

	T6_t2_mem1 = S.Task('T6_t2_mem1', length=1, delay_cost=1)
	T6_t2_mem1 += MAIN_MEM_r[1]
	S += T6_t2_mem1 <= T6_t2

	T6_t3 = S.Task('T6_t3', length=1, delay_cost=1)
	T6_t3 += alt(MAS)
	T6_t3_mem0 = S.Task('T6_t3_mem0', length=1, delay_cost=1)
	T6_t3_mem0 += MAIN_MEM_r[0]
	S += T6_t3_mem0 <= T6_t3

	T6_t3_mem1 = S.Task('T6_t3_mem1', length=1, delay_cost=1)
	T6_t3_mem1 += MAIN_MEM_r[1]
	S += T6_t3_mem1 <= T6_t3

	T7_t0 = S.Task('T7_t0', length=5, delay_cost=1)
	T7_t0 += alt(MM)
	T7_t0_in = S.Task('T7_t0_in', length=1, delay_cost=1)
	T7_t0_in += alt(MM_in)
	S += T7_t0_in*MM_in[0]<=T7_t0*MM[0]
	S += T7_t0_in*MM_in[1]<=T7_t0*MM[1]
	T7_t0_mem0 = S.Task('T7_t0_mem0', length=1, delay_cost=1)
	T7_t0_mem0 += MAIN_MEM_r[0]
	S += T7_t0_mem0 <= T7_t0

	T7_t0_mem1 = S.Task('T7_t0_mem1', length=1, delay_cost=1)
	T7_t0_mem1 += MAIN_MEM_r[1]
	S += T7_t0_mem1 <= T7_t0

	T7_t1 = S.Task('T7_t1', length=5, delay_cost=1)
	T7_t1 += alt(MM)
	T7_t1_in = S.Task('T7_t1_in', length=1, delay_cost=1)
	T7_t1_in += alt(MM_in)
	S += T7_t1_in*MM_in[0]<=T7_t1*MM[0]
	S += T7_t1_in*MM_in[1]<=T7_t1*MM[1]
	T7_t1_mem0 = S.Task('T7_t1_mem0', length=1, delay_cost=1)
	T7_t1_mem0 += MAIN_MEM_r[0]
	S += T7_t1_mem0 <= T7_t1

	T7_t1_mem1 = S.Task('T7_t1_mem1', length=1, delay_cost=1)
	T7_t1_mem1 += MAIN_MEM_r[1]
	S += T7_t1_mem1 <= T7_t1

	T7_t2 = S.Task('T7_t2', length=1, delay_cost=1)
	T7_t2 += alt(MAS)
	T7_t2_mem0 = S.Task('T7_t2_mem0', length=1, delay_cost=1)
	T7_t2_mem0 += MAIN_MEM_r[0]
	S += T7_t2_mem0 <= T7_t2

	T7_t2_mem1 = S.Task('T7_t2_mem1', length=1, delay_cost=1)
	T7_t2_mem1 += MAIN_MEM_r[1]
	S += T7_t2_mem1 <= T7_t2

	T7_t3 = S.Task('T7_t3', length=1, delay_cost=1)
	T7_t3 += alt(MAS)
	T7_t3_mem0 = S.Task('T7_t3_mem0', length=1, delay_cost=1)
	T7_t3_mem0 += MAIN_MEM_r[0]
	S += T7_t3_mem0 <= T7_t3

	T7_t3_mem1 = S.Task('T7_t3_mem1', length=1, delay_cost=1)
	T7_t3_mem1 += MAIN_MEM_r[1]
	S += T7_t3_mem1 <= T7_t3

	T8_t2 = S.Task('T8_t2', length=1, delay_cost=1)
	T8_t2 += alt(MAS)
	T8_t2_mem0 = S.Task('T8_t2_mem0', length=1, delay_cost=1)
	T8_t2_mem0 += MAIN_MEM_r[0]
	S += T8_t2_mem0 <= T8_t2

	T8_t2_mem1 = S.Task('T8_t2_mem1', length=1, delay_cost=1)
	T8_t2_mem1 += MAIN_MEM_r[1]
	S += T8_t2_mem1 <= T8_t2

	T9_t2 = S.Task('T9_t2', length=1, delay_cost=1)
	T9_t2 += alt(MAS)
	T9_t2_mem0 = S.Task('T9_t2_mem0', length=1, delay_cost=1)
	T9_t2_mem0 += MAIN_MEM_r[0]
	S += T9_t2_mem0 <= T9_t2

	T9_t2_mem1 = S.Task('T9_t2_mem1', length=1, delay_cost=1)
	T9_t2_mem1 += MAIN_MEM_r[1]
	S += T9_t2_mem1 <= T9_t2

	T10_t2 = S.Task('T10_t2', length=1, delay_cost=1)
	T10_t2 += alt(MAS)
	T10_t2_mem0 = S.Task('T10_t2_mem0', length=1, delay_cost=1)
	T10_t2_mem0 += MAIN_MEM_r[0]
	S += T10_t2_mem0 <= T10_t2

	T10_t2_mem1 = S.Task('T10_t2_mem1', length=1, delay_cost=1)
	T10_t2_mem1 += MAIN_MEM_r[1]
	S += T10_t2_mem1 <= T10_t2

	T11_t2 = S.Task('T11_t2', length=1, delay_cost=1)
	T11_t2 += alt(MAS)
	T11_t2_mem0 = S.Task('T11_t2_mem0', length=1, delay_cost=1)
	T11_t2_mem0 += MAIN_MEM_r[0]
	S += T11_t2_mem0 <= T11_t2

	T11_t2_mem1 = S.Task('T11_t2_mem1', length=1, delay_cost=1)
	T11_t2_mem1 += MAIN_MEM_r[1]
	S += T11_t2_mem1 <= T11_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM2_stage1MAS4/EP2_LADDERMUL/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

