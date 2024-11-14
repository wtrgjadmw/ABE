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
	r1_in = S.Task('r1_in', length=1, delay_cost=1)
	r1_in += alt(MM_in)
	r1 = S.Task('r1', length=5, delay_cost=1)
	r1 += alt(MM)
	S += r1>=r1_in

	r1_mem0 = S.Task('r1_mem0', length=1, delay_cost=1)
	r1_mem0 += MAIN_MEM_r
	S += r1_mem0 <= r1

	r1_mem1 = S.Task('r1_mem1', length=1, delay_cost=1)
	r1_mem1 += MAIN_MEM_r
	S += r1_mem1 <= r1

	r3_in = S.Task('r3_in', length=1, delay_cost=1)
	r3_in += alt(MM_in)
	r3 = S.Task('r3', length=5, delay_cost=1)
	r3 += alt(MM)
	S += r3>=r3_in

	r3_mem0 = S.Task('r3_mem0', length=1, delay_cost=1)
	r3_mem0 += MAIN_MEM_r
	S += r3_mem0 <= r3

	r3_mem1 = S.Task('r3_mem1', length=1, delay_cost=1)
	r3_mem1 += MAIN_MEM_r
	S += r3_mem1 <= r3

	r4_in = S.Task('r4_in', length=1, delay_cost=1)
	r4_in += alt(MM_in)
	r4 = S.Task('r4', length=5, delay_cost=1)
	r4 += alt(MM)
	S += r4>=r4_in

	r4_mem0 = S.Task('r4_mem0', length=1, delay_cost=1)
	r4_mem0 += MAIN_MEM_r
	S += r4_mem0 <= r4

	r4_mem1 = S.Task('r4_mem1', length=1, delay_cost=1)
	r4_mem1 += MAIN_MEM_r
	S += r4_mem1 <= r4

	r5_in = S.Task('r5_in', length=1, delay_cost=1)
	r5_in += alt(MM_in)
	r5 = S.Task('r5', length=5, delay_cost=1)
	r5 += alt(MM)
	S += r5>=r5_in

	r5_mem0 = S.Task('r5_mem0', length=1, delay_cost=1)
	r5_mem0 += MAIN_MEM_r
	S += r5_mem0 <= r5

	r5_mem1 = S.Task('r5_mem1', length=1, delay_cost=1)
	r5_mem1 += MAIN_MEM_r
	S += r5_mem1 <= r5

	r6_in = S.Task('r6_in', length=1, delay_cost=1)
	r6_in += alt(MM_in)
	r6 = S.Task('r6', length=5, delay_cost=1)
	r6 += alt(MM)
	S += r6>=r6_in

	r6_mem0 = S.Task('r6_mem0', length=1, delay_cost=1)
	r6_mem0 += MAIN_MEM_r
	S += r6_mem0 <= r6

	r6_mem1 = S.Task('r6_mem1', length=1, delay_cost=1)
	r6_mem1 += MAIN_MEM_r
	S += r6_mem1 <= r6

	r12_in = S.Task('r12_in', length=1, delay_cost=1)
	r12_in += alt(MM_in)
	r12 = S.Task('r12', length=5, delay_cost=1)
	r12 += alt(MM)
	S += r12>=r12_in

	r12_mem0 = S.Task('r12_mem0', length=1, delay_cost=1)
	r12_mem0 += MAIN_MEM_r
	S += r12_mem0 <= r12

	r12_mem1 = S.Task('r12_mem1', length=1, delay_cost=1)
	r12_mem1 += MAIN_MEM_r
	S += r12_mem1 <= r12

	r13_in = S.Task('r13_in', length=1, delay_cost=1)
	r13_in += alt(MM_in)
	r13 = S.Task('r13', length=5, delay_cost=1)
	r13 += alt(MM)
	S += r13>=r13_in

	r13_mem0 = S.Task('r13_mem0', length=1, delay_cost=1)
	r13_mem0 += MAIN_MEM_r
	S += r13_mem0 <= r13

	r13_mem1 = S.Task('r13_mem1', length=1, delay_cost=1)
	r13_mem1 += MAIN_MEM_r
	S += r13_mem1 <= r13

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/yrecover/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

