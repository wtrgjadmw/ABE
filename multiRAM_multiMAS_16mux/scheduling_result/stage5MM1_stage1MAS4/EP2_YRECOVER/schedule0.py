from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	r1_t0 = S.Task('r1_t0', length=5, delay_cost=1)
	r1_t0 += alt(MM)
	r1_t0_in = S.Task('r1_t0_in', length=1, delay_cost=1)
	r1_t0_in += alt(MM_in)
	S += r1_t0_in*MM_in[0]<=r1_t0*MM[0]
	r1_t0_mem0 = S.Task('r1_t0_mem0', length=1, delay_cost=1)
	r1_t0_mem0 += MAIN_MEM_r[0]
	S += r1_t0_mem0 <= r1_t0

	r1_t0_mem1 = S.Task('r1_t0_mem1', length=1, delay_cost=1)
	r1_t0_mem1 += MAIN_MEM_r[1]
	S += r1_t0_mem1 <= r1_t0

	r1_t1 = S.Task('r1_t1', length=5, delay_cost=1)
	r1_t1 += alt(MM)
	r1_t1_in = S.Task('r1_t1_in', length=1, delay_cost=1)
	r1_t1_in += alt(MM_in)
	S += r1_t1_in*MM_in[0]<=r1_t1*MM[0]
	r1_t1_mem0 = S.Task('r1_t1_mem0', length=1, delay_cost=1)
	r1_t1_mem0 += MAIN_MEM_r[0]
	S += r1_t1_mem0 <= r1_t1

	r1_t1_mem1 = S.Task('r1_t1_mem1', length=1, delay_cost=1)
	r1_t1_mem1 += MAIN_MEM_r[1]
	S += r1_t1_mem1 <= r1_t1

	r1_t2 = S.Task('r1_t2', length=1, delay_cost=1)
	r1_t2 += alt(MAS)
	r1_t2_mem0 = S.Task('r1_t2_mem0', length=1, delay_cost=1)
	r1_t2_mem0 += MAIN_MEM_r[0]
	S += r1_t2_mem0 <= r1_t2

	r1_t2_mem1 = S.Task('r1_t2_mem1', length=1, delay_cost=1)
	r1_t2_mem1 += MAIN_MEM_r[1]
	S += r1_t2_mem1 <= r1_t2

	r1_t3 = S.Task('r1_t3', length=1, delay_cost=1)
	r1_t3 += alt(MAS)
	r1_t3_mem0 = S.Task('r1_t3_mem0', length=1, delay_cost=1)
	r1_t3_mem0 += MAIN_MEM_r[0]
	S += r1_t3_mem0 <= r1_t3

	r1_t3_mem1 = S.Task('r1_t3_mem1', length=1, delay_cost=1)
	r1_t3_mem1 += MAIN_MEM_r[1]
	S += r1_t3_mem1 <= r1_t3

	r3_t0 = S.Task('r3_t0', length=5, delay_cost=1)
	r3_t0 += alt(MM)
	r3_t0_in = S.Task('r3_t0_in', length=1, delay_cost=1)
	r3_t0_in += alt(MM_in)
	S += r3_t0_in*MM_in[0]<=r3_t0*MM[0]
	r3_t0_mem0 = S.Task('r3_t0_mem0', length=1, delay_cost=1)
	r3_t0_mem0 += MAIN_MEM_r[0]
	S += r3_t0_mem0 <= r3_t0

	r3_t0_mem1 = S.Task('r3_t0_mem1', length=1, delay_cost=1)
	r3_t0_mem1 += MAIN_MEM_r[1]
	S += r3_t0_mem1 <= r3_t0

	r3_t1 = S.Task('r3_t1', length=5, delay_cost=1)
	r3_t1 += alt(MM)
	r3_t1_in = S.Task('r3_t1_in', length=1, delay_cost=1)
	r3_t1_in += alt(MM_in)
	S += r3_t1_in*MM_in[0]<=r3_t1*MM[0]
	r3_t1_mem0 = S.Task('r3_t1_mem0', length=1, delay_cost=1)
	r3_t1_mem0 += MAIN_MEM_r[0]
	S += r3_t1_mem0 <= r3_t1

	r3_t1_mem1 = S.Task('r3_t1_mem1', length=1, delay_cost=1)
	r3_t1_mem1 += MAIN_MEM_r[1]
	S += r3_t1_mem1 <= r3_t1

	r3_t2 = S.Task('r3_t2', length=1, delay_cost=1)
	r3_t2 += alt(MAS)
	r3_t2_mem0 = S.Task('r3_t2_mem0', length=1, delay_cost=1)
	r3_t2_mem0 += MAIN_MEM_r[0]
	S += r3_t2_mem0 <= r3_t2

	r3_t2_mem1 = S.Task('r3_t2_mem1', length=1, delay_cost=1)
	r3_t2_mem1 += MAIN_MEM_r[1]
	S += r3_t2_mem1 <= r3_t2

	r3_t3 = S.Task('r3_t3', length=1, delay_cost=1)
	r3_t3 += alt(MAS)
	r3_t3_mem0 = S.Task('r3_t3_mem0', length=1, delay_cost=1)
	r3_t3_mem0 += MAIN_MEM_r[0]
	S += r3_t3_mem0 <= r3_t3

	r3_t3_mem1 = S.Task('r3_t3_mem1', length=1, delay_cost=1)
	r3_t3_mem1 += MAIN_MEM_r[1]
	S += r3_t3_mem1 <= r3_t3

	r4_t0 = S.Task('r4_t0', length=5, delay_cost=1)
	r4_t0 += alt(MM)
	r4_t0_in = S.Task('r4_t0_in', length=1, delay_cost=1)
	r4_t0_in += alt(MM_in)
	S += r4_t0_in*MM_in[0]<=r4_t0*MM[0]
	r4_t0_mem0 = S.Task('r4_t0_mem0', length=1, delay_cost=1)
	r4_t0_mem0 += MAIN_MEM_r[0]
	S += r4_t0_mem0 <= r4_t0

	r4_t0_mem1 = S.Task('r4_t0_mem1', length=1, delay_cost=1)
	r4_t0_mem1 += MAIN_MEM_r[1]
	S += r4_t0_mem1 <= r4_t0

	r4_t1 = S.Task('r4_t1', length=5, delay_cost=1)
	r4_t1 += alt(MM)
	r4_t1_in = S.Task('r4_t1_in', length=1, delay_cost=1)
	r4_t1_in += alt(MM_in)
	S += r4_t1_in*MM_in[0]<=r4_t1*MM[0]
	r4_t1_mem0 = S.Task('r4_t1_mem0', length=1, delay_cost=1)
	r4_t1_mem0 += MAIN_MEM_r[0]
	S += r4_t1_mem0 <= r4_t1

	r4_t1_mem1 = S.Task('r4_t1_mem1', length=1, delay_cost=1)
	r4_t1_mem1 += MAIN_MEM_r[1]
	S += r4_t1_mem1 <= r4_t1

	r4_t2 = S.Task('r4_t2', length=1, delay_cost=1)
	r4_t2 += alt(MAS)
	r4_t2_mem0 = S.Task('r4_t2_mem0', length=1, delay_cost=1)
	r4_t2_mem0 += MAIN_MEM_r[0]
	S += r4_t2_mem0 <= r4_t2

	r4_t2_mem1 = S.Task('r4_t2_mem1', length=1, delay_cost=1)
	r4_t2_mem1 += MAIN_MEM_r[1]
	S += r4_t2_mem1 <= r4_t2

	r4_t3 = S.Task('r4_t3', length=1, delay_cost=1)
	r4_t3 += alt(MAS)
	r4_t3_mem0 = S.Task('r4_t3_mem0', length=1, delay_cost=1)
	r4_t3_mem0 += MAIN_MEM_r[0]
	S += r4_t3_mem0 <= r4_t3

	r4_t3_mem1 = S.Task('r4_t3_mem1', length=1, delay_cost=1)
	r4_t3_mem1 += MAIN_MEM_r[1]
	S += r4_t3_mem1 <= r4_t3

	r5_t0 = S.Task('r5_t0', length=5, delay_cost=1)
	r5_t0 += alt(MM)
	r5_t0_in = S.Task('r5_t0_in', length=1, delay_cost=1)
	r5_t0_in += alt(MM_in)
	S += r5_t0_in*MM_in[0]<=r5_t0*MM[0]
	r5_t0_mem0 = S.Task('r5_t0_mem0', length=1, delay_cost=1)
	r5_t0_mem0 += MAIN_MEM_r[0]
	S += r5_t0_mem0 <= r5_t0

	r5_t0_mem1 = S.Task('r5_t0_mem1', length=1, delay_cost=1)
	r5_t0_mem1 += MAIN_MEM_r[1]
	S += r5_t0_mem1 <= r5_t0

	r5_t1 = S.Task('r5_t1', length=5, delay_cost=1)
	r5_t1 += alt(MM)
	r5_t1_in = S.Task('r5_t1_in', length=1, delay_cost=1)
	r5_t1_in += alt(MM_in)
	S += r5_t1_in*MM_in[0]<=r5_t1*MM[0]
	r5_t1_mem0 = S.Task('r5_t1_mem0', length=1, delay_cost=1)
	r5_t1_mem0 += MAIN_MEM_r[0]
	S += r5_t1_mem0 <= r5_t1

	r5_t1_mem1 = S.Task('r5_t1_mem1', length=1, delay_cost=1)
	r5_t1_mem1 += MAIN_MEM_r[1]
	S += r5_t1_mem1 <= r5_t1

	r5_t2 = S.Task('r5_t2', length=1, delay_cost=1)
	r5_t2 += alt(MAS)
	r5_t2_mem0 = S.Task('r5_t2_mem0', length=1, delay_cost=1)
	r5_t2_mem0 += MAIN_MEM_r[0]
	S += r5_t2_mem0 <= r5_t2

	r5_t2_mem1 = S.Task('r5_t2_mem1', length=1, delay_cost=1)
	r5_t2_mem1 += MAIN_MEM_r[1]
	S += r5_t2_mem1 <= r5_t2

	r5_t3 = S.Task('r5_t3', length=1, delay_cost=1)
	r5_t3 += alt(MAS)
	r5_t3_mem0 = S.Task('r5_t3_mem0', length=1, delay_cost=1)
	r5_t3_mem0 += MAIN_MEM_r[0]
	S += r5_t3_mem0 <= r5_t3

	r5_t3_mem1 = S.Task('r5_t3_mem1', length=1, delay_cost=1)
	r5_t3_mem1 += MAIN_MEM_r[1]
	S += r5_t3_mem1 <= r5_t3

	r6_t0 = S.Task('r6_t0', length=5, delay_cost=1)
	r6_t0 += alt(MM)
	r6_t0_in = S.Task('r6_t0_in', length=1, delay_cost=1)
	r6_t0_in += alt(MM_in)
	S += r6_t0_in*MM_in[0]<=r6_t0*MM[0]
	r6_t0_mem0 = S.Task('r6_t0_mem0', length=1, delay_cost=1)
	r6_t0_mem0 += MAIN_MEM_r[0]
	S += r6_t0_mem0 <= r6_t0

	r6_t0_mem1 = S.Task('r6_t0_mem1', length=1, delay_cost=1)
	r6_t0_mem1 += MAIN_MEM_r[1]
	S += r6_t0_mem1 <= r6_t0

	r6_t1 = S.Task('r6_t1', length=5, delay_cost=1)
	r6_t1 += alt(MM)
	r6_t1_in = S.Task('r6_t1_in', length=1, delay_cost=1)
	r6_t1_in += alt(MM_in)
	S += r6_t1_in*MM_in[0]<=r6_t1*MM[0]
	r6_t1_mem0 = S.Task('r6_t1_mem0', length=1, delay_cost=1)
	r6_t1_mem0 += MAIN_MEM_r[0]
	S += r6_t1_mem0 <= r6_t1

	r6_t1_mem1 = S.Task('r6_t1_mem1', length=1, delay_cost=1)
	r6_t1_mem1 += MAIN_MEM_r[1]
	S += r6_t1_mem1 <= r6_t1

	r6_t2 = S.Task('r6_t2', length=1, delay_cost=1)
	r6_t2 += alt(MAS)
	r6_t2_mem0 = S.Task('r6_t2_mem0', length=1, delay_cost=1)
	r6_t2_mem0 += MAIN_MEM_r[0]
	S += r6_t2_mem0 <= r6_t2

	r6_t2_mem1 = S.Task('r6_t2_mem1', length=1, delay_cost=1)
	r6_t2_mem1 += MAIN_MEM_r[1]
	S += r6_t2_mem1 <= r6_t2

	r6_t3 = S.Task('r6_t3', length=1, delay_cost=1)
	r6_t3 += alt(MAS)
	r6_t3_mem0 = S.Task('r6_t3_mem0', length=1, delay_cost=1)
	r6_t3_mem0 += MAIN_MEM_r[0]
	S += r6_t3_mem0 <= r6_t3

	r6_t3_mem1 = S.Task('r6_t3_mem1', length=1, delay_cost=1)
	r6_t3_mem1 += MAIN_MEM_r[1]
	S += r6_t3_mem1 <= r6_t3

	r9_t2 = S.Task('r9_t2', length=1, delay_cost=1)
	r9_t2 += alt(MAS)
	r9_t2_mem0 = S.Task('r9_t2_mem0', length=1, delay_cost=1)
	r9_t2_mem0 += MAIN_MEM_r[0]
	S += r9_t2_mem0 <= r9_t2

	r9_t2_mem1 = S.Task('r9_t2_mem1', length=1, delay_cost=1)
	r9_t2_mem1 += MAIN_MEM_r[1]
	S += r9_t2_mem1 <= r9_t2

	r12_t0 = S.Task('r12_t0', length=5, delay_cost=1)
	r12_t0 += alt(MM)
	r12_t0_in = S.Task('r12_t0_in', length=1, delay_cost=1)
	r12_t0_in += alt(MM_in)
	S += r12_t0_in*MM_in[0]<=r12_t0*MM[0]
	r12_t0_mem0 = S.Task('r12_t0_mem0', length=1, delay_cost=1)
	r12_t0_mem0 += MAIN_MEM_r[0]
	S += r12_t0_mem0 <= r12_t0

	r12_t0_mem1 = S.Task('r12_t0_mem1', length=1, delay_cost=1)
	r12_t0_mem1 += MAIN_MEM_r[1]
	S += r12_t0_mem1 <= r12_t0

	r12_t1 = S.Task('r12_t1', length=5, delay_cost=1)
	r12_t1 += alt(MM)
	r12_t1_in = S.Task('r12_t1_in', length=1, delay_cost=1)
	r12_t1_in += alt(MM_in)
	S += r12_t1_in*MM_in[0]<=r12_t1*MM[0]
	r12_t1_mem0 = S.Task('r12_t1_mem0', length=1, delay_cost=1)
	r12_t1_mem0 += MAIN_MEM_r[0]
	S += r12_t1_mem0 <= r12_t1

	r12_t1_mem1 = S.Task('r12_t1_mem1', length=1, delay_cost=1)
	r12_t1_mem1 += MAIN_MEM_r[1]
	S += r12_t1_mem1 <= r12_t1

	r12_t2 = S.Task('r12_t2', length=1, delay_cost=1)
	r12_t2 += alt(MAS)
	r12_t2_mem0 = S.Task('r12_t2_mem0', length=1, delay_cost=1)
	r12_t2_mem0 += MAIN_MEM_r[0]
	S += r12_t2_mem0 <= r12_t2

	r12_t2_mem1 = S.Task('r12_t2_mem1', length=1, delay_cost=1)
	r12_t2_mem1 += MAIN_MEM_r[1]
	S += r12_t2_mem1 <= r12_t2

	r12_t3 = S.Task('r12_t3', length=1, delay_cost=1)
	r12_t3 += alt(MAS)
	r12_t3_mem0 = S.Task('r12_t3_mem0', length=1, delay_cost=1)
	r12_t3_mem0 += MAIN_MEM_r[0]
	S += r12_t3_mem0 <= r12_t3

	r12_t3_mem1 = S.Task('r12_t3_mem1', length=1, delay_cost=1)
	r12_t3_mem1 += MAIN_MEM_r[1]
	S += r12_t3_mem1 <= r12_t3

	r13_t0 = S.Task('r13_t0', length=5, delay_cost=1)
	r13_t0 += alt(MM)
	r13_t0_in = S.Task('r13_t0_in', length=1, delay_cost=1)
	r13_t0_in += alt(MM_in)
	S += r13_t0_in*MM_in[0]<=r13_t0*MM[0]
	r13_t0_mem0 = S.Task('r13_t0_mem0', length=1, delay_cost=1)
	r13_t0_mem0 += MAIN_MEM_r[0]
	S += r13_t0_mem0 <= r13_t0

	r13_t0_mem1 = S.Task('r13_t0_mem1', length=1, delay_cost=1)
	r13_t0_mem1 += MAIN_MEM_r[1]
	S += r13_t0_mem1 <= r13_t0

	r13_t1 = S.Task('r13_t1', length=5, delay_cost=1)
	r13_t1 += alt(MM)
	r13_t1_in = S.Task('r13_t1_in', length=1, delay_cost=1)
	r13_t1_in += alt(MM_in)
	S += r13_t1_in*MM_in[0]<=r13_t1*MM[0]
	r13_t1_mem0 = S.Task('r13_t1_mem0', length=1, delay_cost=1)
	r13_t1_mem0 += MAIN_MEM_r[0]
	S += r13_t1_mem0 <= r13_t1

	r13_t1_mem1 = S.Task('r13_t1_mem1', length=1, delay_cost=1)
	r13_t1_mem1 += MAIN_MEM_r[1]
	S += r13_t1_mem1 <= r13_t1

	r13_t2 = S.Task('r13_t2', length=1, delay_cost=1)
	r13_t2 += alt(MAS)
	r13_t2_mem0 = S.Task('r13_t2_mem0', length=1, delay_cost=1)
	r13_t2_mem0 += MAIN_MEM_r[0]
	S += r13_t2_mem0 <= r13_t2

	r13_t2_mem1 = S.Task('r13_t2_mem1', length=1, delay_cost=1)
	r13_t2_mem1 += MAIN_MEM_r[1]
	S += r13_t2_mem1 <= r13_t2

	r13_t3 = S.Task('r13_t3', length=1, delay_cost=1)
	r13_t3 += alt(MAS)
	r13_t3_mem0 = S.Task('r13_t3_mem0', length=1, delay_cost=1)
	r13_t3_mem0 += MAIN_MEM_r[0]
	S += r13_t3_mem0 <= r13_t3

	r13_t3_mem1 = S.Task('r13_t3_mem1', length=1, delay_cost=1)
	r13_t3_mem1 += MAIN_MEM_r[1]
	S += r13_t3_mem1 <= r13_t3

	r16_t3 = S.Task('r16_t3', length=1, delay_cost=1)
	r16_t3 += alt(MAS)
	r16_t3_mem0 = S.Task('r16_t3_mem0', length=1, delay_cost=1)
	r16_t3_mem0 += MAIN_MEM_r[0]
	S += r16_t3_mem0 <= r16_t3

	r16_t3_mem1 = S.Task('r16_t3_mem1', length=1, delay_cost=1)
	r16_t3_mem1 += MAIN_MEM_r[1]
	S += r16_t3_mem1 <= r16_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage1MAS4/EP2_YRECOVER/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

