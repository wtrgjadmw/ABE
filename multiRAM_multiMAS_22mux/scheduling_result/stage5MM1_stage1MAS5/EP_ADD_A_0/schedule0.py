from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=1, size=2)
	MAS_MEM = S.Resources('MAS_MEM', num=5, size=2)
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

	t0_mem1 = S.Task('t0_mem1', length=1, delay_cost=1)
	t0_mem1 += MAIN_MEM_r
	S += t0_mem1 <= t0

	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	t1_in += alt(MM_in)
	t1 = S.Task('t1', length=5, delay_cost=1)
	t1 += alt(MM)
	S += t1>=t1_in

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	t1_mem0 += MAIN_MEM_r
	S += t1_mem0 <= t1

	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	t1_mem1 += MAIN_MEM_r
	S += t1_mem1 <= t1

	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	t2_in += alt(MM_in)
	t2 = S.Task('t2', length=5, delay_cost=1)
	t2 += alt(MM)
	S += t2>=t2_in

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	t2_mem0 += MAIN_MEM_r
	S += t2_mem0 <= t2

	t2_mem1 = S.Task('t2_mem1', length=1, delay_cost=1)
	t2_mem1 += MAIN_MEM_r
	S += t2_mem1 <= t2

	t3 = S.Task('t3', length=1, delay_cost=1)
	t3 += alt(MAS)

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	t3_mem0 += MAIN_MEM_r
	S += t3_mem0 <= t3

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	t3_mem1 += MAIN_MEM_r
	S += t3_mem1 <= t3

	t4 = S.Task('t4', length=1, delay_cost=1)
	t4 += alt(MAS)

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	t4_mem0 += MAIN_MEM_r
	S += t4_mem0 <= t4

	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	t4_mem1 += MAIN_MEM_r
	S += t4_mem1 <= t4

	t8 = S.Task('t8', length=1, delay_cost=1)
	t8 += alt(MAS)

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	t8_mem0 += MAIN_MEM_r
	S += t8_mem0 <= t8

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	t8_mem1 += MAIN_MEM_r
	S += t8_mem1 <= t8

	t9 = S.Task('t9', length=1, delay_cost=1)
	t9 += alt(MAS)

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	t9_mem0 += MAIN_MEM_r
	S += t9_mem0 <= t9

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	t9_mem1 += MAIN_MEM_r
	S += t9_mem1 <= t9

	t13 = S.Task('t13', length=1, delay_cost=1)
	t13 += alt(MAS)

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	t13_mem0 += MAIN_MEM_r
	S += t13_mem0 <= t13

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	t13_mem1 += MAIN_MEM_r
	S += t13_mem1 <= t13

	t14 = S.Task('t14', length=1, delay_cost=1)
	t14 += alt(MAS)

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	t14_mem0 += MAIN_MEM_r
	S += t14_mem0 <= t14

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	t14_mem1 += MAIN_MEM_r
	S += t14_mem1 <= t14

	t18 = S.Task('t18', length=1, delay_cost=1)
	t18 += alt(MAS)

	t18_mem0 = S.Task('t18_mem0', length=1, delay_cost=1)
	t18_mem0 += MAIN_MEM_r
	S += t18_mem0 <= t18

	t18_mem1 = S.Task('t18_mem1', length=1, delay_cost=1)
	t18_mem1 += MAIN_MEM_r
	S += t18_mem1 <= t18

	solvers.mip.solve(S,msg=1,ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/Users/fukudamomoko/Desktop/research/ABE/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS5/EP_ADD_A_0/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

