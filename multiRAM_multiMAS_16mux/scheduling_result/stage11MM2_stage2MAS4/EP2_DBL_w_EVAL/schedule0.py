from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	t0_t0 = S.Task('t0_t0', length=2, delay_cost=1)
	t0_t0 += alt(MAS)
	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	t0_t0_in += alt(MAS_in)
	S += t0_t0_in*MAS_in[0]<=t0_t0*MAS[0]

	S += t0_t0_in*MAS_in[1]<=t0_t0*MAS[1]

	S += t0_t0_in*MAS_in[2]<=t0_t0*MAS[2]

	S += t0_t0_in*MAS_in[3]<=t0_t0*MAS[3]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	t0_t0_mem0 += MAIN_MEM_r[0]
	S += t0_t0_mem0 <= t0_t0

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	t0_t0_mem1 += MAIN_MEM_r[1]
	S += t0_t0_mem1 <= t0_t0

	t0_t1 = S.Task('t0_t1', length=2, delay_cost=1)
	t0_t1 += alt(MAS)
	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	t0_t1_in += alt(MAS_in)
	S += t0_t1_in*MAS_in[0]<=t0_t1*MAS[0]

	S += t0_t1_in*MAS_in[1]<=t0_t1*MAS[1]

	S += t0_t1_in*MAS_in[2]<=t0_t1*MAS[2]

	S += t0_t1_in*MAS_in[3]<=t0_t1*MAS[3]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	t0_t1_mem0 += MAIN_MEM_r[0]
	S += t0_t1_mem0 <= t0_t1

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	t0_t1_mem1 += MAIN_MEM_r[1]
	S += t0_t1_mem1 <= t0_t1

	t0_t3 = S.Task('t0_t3', length=11, delay_cost=1)
	t0_t3 += alt(MM)
	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	t0_t3_in += alt(MM_in)
	S += t0_t3_in*MM_in[0]<=t0_t3*MM[0]
	S += t0_t3_in*MM_in[1]<=t0_t3*MM[1]
	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	t0_t3_mem0 += MAIN_MEM_r[0]
	S += t0_t3_mem0 <= t0_t3

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	t0_t3_mem1 += MAIN_MEM_r[1]
	S += t0_t3_mem1 <= t0_t3

	t1_t0 = S.Task('t1_t0', length=2, delay_cost=1)
	t1_t0 += alt(MAS)
	t1_t0_in = S.Task('t1_t0_in', length=1, delay_cost=1)
	t1_t0_in += alt(MAS_in)
	S += t1_t0_in*MAS_in[0]<=t1_t0*MAS[0]

	S += t1_t0_in*MAS_in[1]<=t1_t0*MAS[1]

	S += t1_t0_in*MAS_in[2]<=t1_t0*MAS[2]

	S += t1_t0_in*MAS_in[3]<=t1_t0*MAS[3]

	t1_t0_mem0 = S.Task('t1_t0_mem0', length=1, delay_cost=1)
	t1_t0_mem0 += MAIN_MEM_r[0]
	S += t1_t0_mem0 <= t1_t0

	t1_t0_mem1 = S.Task('t1_t0_mem1', length=1, delay_cost=1)
	t1_t0_mem1 += MAIN_MEM_r[1]
	S += t1_t0_mem1 <= t1_t0

	t1_t1 = S.Task('t1_t1', length=2, delay_cost=1)
	t1_t1 += alt(MAS)
	t1_t1_in = S.Task('t1_t1_in', length=1, delay_cost=1)
	t1_t1_in += alt(MAS_in)
	S += t1_t1_in*MAS_in[0]<=t1_t1*MAS[0]

	S += t1_t1_in*MAS_in[1]<=t1_t1*MAS[1]

	S += t1_t1_in*MAS_in[2]<=t1_t1*MAS[2]

	S += t1_t1_in*MAS_in[3]<=t1_t1*MAS[3]

	t1_t1_mem0 = S.Task('t1_t1_mem0', length=1, delay_cost=1)
	t1_t1_mem0 += MAIN_MEM_r[0]
	S += t1_t1_mem0 <= t1_t1

	t1_t1_mem1 = S.Task('t1_t1_mem1', length=1, delay_cost=1)
	t1_t1_mem1 += MAIN_MEM_r[1]
	S += t1_t1_mem1 <= t1_t1

	t1_t3 = S.Task('t1_t3', length=11, delay_cost=1)
	t1_t3 += alt(MM)
	t1_t3_in = S.Task('t1_t3_in', length=1, delay_cost=1)
	t1_t3_in += alt(MM_in)
	S += t1_t3_in*MM_in[0]<=t1_t3*MM[0]
	S += t1_t3_in*MM_in[1]<=t1_t3*MM[1]
	t1_t3_mem0 = S.Task('t1_t3_mem0', length=1, delay_cost=1)
	t1_t3_mem0 += MAIN_MEM_r[0]
	S += t1_t3_mem0 <= t1_t3

	t1_t3_mem1 = S.Task('t1_t3_mem1', length=1, delay_cost=1)
	t1_t3_mem1 += MAIN_MEM_r[1]
	S += t1_t3_mem1 <= t1_t3

	t2_t2 = S.Task('t2_t2', length=2, delay_cost=1)
	t2_t2 += alt(MAS)
	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	t2_t2_in += alt(MAS_in)
	S += t2_t2_in*MAS_in[0]<=t2_t2*MAS[0]

	S += t2_t2_in*MAS_in[1]<=t2_t2*MAS[1]

	S += t2_t2_in*MAS_in[2]<=t2_t2*MAS[2]

	S += t2_t2_in*MAS_in[3]<=t2_t2*MAS[3]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	t2_t2_mem0 += MAIN_MEM_r[0]
	S += t2_t2_mem0 <= t2_t2

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	t2_t2_mem1 += MAIN_MEM_r[1]
	S += t2_t2_mem1 <= t2_t2

	t5_t0 = S.Task('t5_t0', length=11, delay_cost=1)
	t5_t0 += alt(MM)
	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	t5_t0_in += alt(MM_in)
	S += t5_t0_in*MM_in[0]<=t5_t0*MM[0]
	S += t5_t0_in*MM_in[1]<=t5_t0*MM[1]
	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	t5_t0_mem0 += MAIN_MEM_r[0]
	S += t5_t0_mem0 <= t5_t0

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	t5_t0_mem1 += MAIN_MEM_r[1]
	S += t5_t0_mem1 <= t5_t0

	t5_t1 = S.Task('t5_t1', length=11, delay_cost=1)
	t5_t1 += alt(MM)
	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	t5_t1_in += alt(MM_in)
	S += t5_t1_in*MM_in[0]<=t5_t1*MM[0]
	S += t5_t1_in*MM_in[1]<=t5_t1*MM[1]
	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	t5_t1_mem0 += MAIN_MEM_r[0]
	S += t5_t1_mem0 <= t5_t1

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	t5_t1_mem1 += MAIN_MEM_r[1]
	S += t5_t1_mem1 <= t5_t1

	t5_t2 = S.Task('t5_t2', length=2, delay_cost=1)
	t5_t2 += alt(MAS)
	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	t5_t2_in += alt(MAS_in)
	S += t5_t2_in*MAS_in[0]<=t5_t2*MAS[0]

	S += t5_t2_in*MAS_in[1]<=t5_t2*MAS[1]

	S += t5_t2_in*MAS_in[2]<=t5_t2*MAS[2]

	S += t5_t2_in*MAS_in[3]<=t5_t2*MAS[3]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	t5_t2_mem0 += MAIN_MEM_r[0]
	S += t5_t2_mem0 <= t5_t2

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	t5_t2_mem1 += MAIN_MEM_r[1]
	S += t5_t2_mem1 <= t5_t2

	t5_t3 = S.Task('t5_t3', length=2, delay_cost=1)
	t5_t3 += alt(MAS)
	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	t5_t3_in += alt(MAS_in)
	S += t5_t3_in*MAS_in[0]<=t5_t3*MAS[0]

	S += t5_t3_in*MAS_in[1]<=t5_t3*MAS[1]

	S += t5_t3_in*MAS_in[2]<=t5_t3*MAS[2]

	S += t5_t3_in*MAS_in[3]<=t5_t3*MAS[3]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	t5_t3_mem0 += MAIN_MEM_r[0]
	S += t5_t3_mem0 <= t5_t3

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	t5_t3_mem1 += MAIN_MEM_r[1]
	S += t5_t3_mem1 <= t5_t3

	t7_t0 = S.Task('t7_t0', length=2, delay_cost=1)
	t7_t0 += alt(MAS)
	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	t7_t0_in += alt(MAS_in)
	S += t7_t0_in*MAS_in[0]<=t7_t0*MAS[0]

	S += t7_t0_in*MAS_in[1]<=t7_t0*MAS[1]

	S += t7_t0_in*MAS_in[2]<=t7_t0*MAS[2]

	S += t7_t0_in*MAS_in[3]<=t7_t0*MAS[3]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	t7_t0_mem0 += MAIN_MEM_r[0]
	S += t7_t0_mem0 <= t7_t0

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	t7_t0_mem1 += MAIN_MEM_r[1]
	S += t7_t0_mem1 <= t7_t0

	t7_t1 = S.Task('t7_t1', length=2, delay_cost=1)
	t7_t1 += alt(MAS)
	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	t7_t1_in += alt(MAS_in)
	S += t7_t1_in*MAS_in[0]<=t7_t1*MAS[0]

	S += t7_t1_in*MAS_in[1]<=t7_t1*MAS[1]

	S += t7_t1_in*MAS_in[2]<=t7_t1*MAS[2]

	S += t7_t1_in*MAS_in[3]<=t7_t1*MAS[3]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	t7_t1_mem0 += MAIN_MEM_r[0]
	S += t7_t1_mem0 <= t7_t1

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	t7_t1_mem1 += MAIN_MEM_r[1]
	S += t7_t1_mem1 <= t7_t1

	t7_t3 = S.Task('t7_t3', length=11, delay_cost=1)
	t7_t3 += alt(MM)
	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	t7_t3_in += alt(MM_in)
	S += t7_t3_in*MM_in[0]<=t7_t3*MM[0]
	S += t7_t3_in*MM_in[1]<=t7_t3*MM[1]
	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	t7_t3_mem0 += MAIN_MEM_r[0]
	S += t7_t3_mem0 <= t7_t3

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	t7_t3_mem1 += MAIN_MEM_r[1]
	S += t7_t3_mem1 <= t7_t3

	t10_t0 = S.Task('t10_t0', length=11, delay_cost=1)
	t10_t0 += alt(MM)
	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	t10_t0_in += alt(MM_in)
	S += t10_t0_in*MM_in[0]<=t10_t0*MM[0]
	S += t10_t0_in*MM_in[1]<=t10_t0*MM[1]
	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	t10_t0_mem0 += MAIN_MEM_r[0]
	S += t10_t0_mem0 <= t10_t0

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	t10_t0_mem1 += MAIN_MEM_r[1]
	S += t10_t0_mem1 <= t10_t0

	t10_t1 = S.Task('t10_t1', length=11, delay_cost=1)
	t10_t1 += alt(MM)
	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	t10_t1_in += alt(MM_in)
	S += t10_t1_in*MM_in[0]<=t10_t1*MM[0]
	S += t10_t1_in*MM_in[1]<=t10_t1*MM[1]
	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	t10_t1_mem0 += MAIN_MEM_r[0]
	S += t10_t1_mem0 <= t10_t1

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	t10_t1_mem1 += MAIN_MEM_r[1]
	S += t10_t1_mem1 <= t10_t1

	t10_t2 = S.Task('t10_t2', length=2, delay_cost=1)
	t10_t2 += alt(MAS)
	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	t10_t2_in += alt(MAS_in)
	S += t10_t2_in*MAS_in[0]<=t10_t2*MAS[0]

	S += t10_t2_in*MAS_in[1]<=t10_t2*MAS[1]

	S += t10_t2_in*MAS_in[2]<=t10_t2*MAS[2]

	S += t10_t2_in*MAS_in[3]<=t10_t2*MAS[3]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	t10_t2_mem0 += MAIN_MEM_r[0]
	S += t10_t2_mem0 <= t10_t2

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	t10_t2_mem1 += MAIN_MEM_r[1]
	S += t10_t2_mem1 <= t10_t2

	t10_t3 = S.Task('t10_t3', length=2, delay_cost=1)
	t10_t3 += alt(MAS)
	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	t10_t3_in += alt(MAS_in)
	S += t10_t3_in*MAS_in[0]<=t10_t3*MAS[0]

	S += t10_t3_in*MAS_in[1]<=t10_t3*MAS[1]

	S += t10_t3_in*MAS_in[2]<=t10_t3*MAS[2]

	S += t10_t3_in*MAS_in[3]<=t10_t3*MAS[3]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	t10_t3_mem0 += MAIN_MEM_r[0]
	S += t10_t3_mem0 <= t10_t3

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	t10_t3_mem1 += MAIN_MEM_r[1]
	S += t10_t3_mem1 <= t10_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage2MAS4/EP2_DBL_w_EVAL/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

