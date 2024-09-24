from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 111
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c21_t0_in = S.Task('c21_t0_in', length=1, delay_cost=1)
	S += c21_t0_in >= 0
	c21_t0_in += MM_in[0]

	c21_t0_mem0 = S.Task('c21_t0_mem0', length=1, delay_cost=1)
	S += c21_t0_mem0 >= 0
	c21_t0_mem0 += MAIN_MEM_r[0]

	c21_t0_mem1 = S.Task('c21_t0_mem1', length=1, delay_cost=1)
	S += c21_t0_mem1 >= 0
	c21_t0_mem1 += MAIN_MEM_r[1]

	c21_t0 = S.Task('c21_t0', length=5, delay_cost=1)
	S += c21_t0 >= 1
	c21_t0 += MM[0]

	c21_t1_in = S.Task('c21_t1_in', length=1, delay_cost=1)
	S += c21_t1_in >= 1
	c21_t1_in += MM_in[0]

	c21_t1_mem0 = S.Task('c21_t1_mem0', length=1, delay_cost=1)
	S += c21_t1_mem0 >= 1
	c21_t1_mem0 += MAIN_MEM_r[0]

	c21_t1_mem1 = S.Task('c21_t1_mem1', length=1, delay_cost=1)
	S += c21_t1_mem1 >= 1
	c21_t1_mem1 += MAIN_MEM_r[1]

	c01_t0_in = S.Task('c01_t0_in', length=1, delay_cost=1)
	S += c01_t0_in >= 2
	c01_t0_in += MM_in[0]

	c01_t0_mem0 = S.Task('c01_t0_mem0', length=1, delay_cost=1)
	S += c01_t0_mem0 >= 2
	c01_t0_mem0 += MAIN_MEM_r[0]

	c01_t0_mem1 = S.Task('c01_t0_mem1', length=1, delay_cost=1)
	S += c01_t0_mem1 >= 2
	c01_t0_mem1 += MAIN_MEM_r[1]

	c21_t1 = S.Task('c21_t1', length=5, delay_cost=1)
	S += c21_t1 >= 2
	c21_t1 += MM[0]

	c01_t0 = S.Task('c01_t0', length=5, delay_cost=1)
	S += c01_t0 >= 3
	c01_t0 += MM[0]

	c10_t1_in = S.Task('c10_t1_in', length=1, delay_cost=1)
	S += c10_t1_in >= 3
	c10_t1_in += MM_in[0]

	c10_t1_mem0 = S.Task('c10_t1_mem0', length=1, delay_cost=1)
	S += c10_t1_mem0 >= 3
	c10_t1_mem0 += MAIN_MEM_r[0]

	c10_t1_mem1 = S.Task('c10_t1_mem1', length=1, delay_cost=1)
	S += c10_t1_mem1 >= 3
	c10_t1_mem1 += MAIN_MEM_r[1]

	c01_t1_in = S.Task('c01_t1_in', length=1, delay_cost=1)
	S += c01_t1_in >= 4
	c01_t1_in += MM_in[0]

	c01_t1_mem0 = S.Task('c01_t1_mem0', length=1, delay_cost=1)
	S += c01_t1_mem0 >= 4
	c01_t1_mem0 += MAIN_MEM_r[0]

	c01_t1_mem1 = S.Task('c01_t1_mem1', length=1, delay_cost=1)
	S += c01_t1_mem1 >= 4
	c01_t1_mem1 += MAIN_MEM_r[1]

	c10_t1 = S.Task('c10_t1', length=5, delay_cost=1)
	S += c10_t1 >= 4
	c10_t1 += MM[0]

	c01_t1 = S.Task('c01_t1', length=5, delay_cost=1)
	S += c01_t1 >= 5
	c01_t1 += MM[0]

	c20_t0_in = S.Task('c20_t0_in', length=1, delay_cost=1)
	S += c20_t0_in >= 5
	c20_t0_in += MM_in[0]

	c20_t0_mem0 = S.Task('c20_t0_mem0', length=1, delay_cost=1)
	S += c20_t0_mem0 >= 5
	c20_t0_mem0 += MAIN_MEM_r[0]

	c20_t0_mem1 = S.Task('c20_t0_mem1', length=1, delay_cost=1)
	S += c20_t0_mem1 >= 5
	c20_t0_mem1 += MAIN_MEM_r[1]

	c10_t0_in = S.Task('c10_t0_in', length=1, delay_cost=1)
	S += c10_t0_in >= 6
	c10_t0_in += MM_in[0]

	c10_t0_mem0 = S.Task('c10_t0_mem0', length=1, delay_cost=1)
	S += c10_t0_mem0 >= 6
	c10_t0_mem0 += MAIN_MEM_r[0]

	c10_t0_mem1 = S.Task('c10_t0_mem1', length=1, delay_cost=1)
	S += c10_t0_mem1 >= 6
	c10_t0_mem1 += MAIN_MEM_r[1]

	c20_t0 = S.Task('c20_t0', length=5, delay_cost=1)
	S += c20_t0 >= 6
	c20_t0 += MM[0]

	c10_t0 = S.Task('c10_t0', length=5, delay_cost=1)
	S += c10_t0 >= 7
	c10_t0 += MM[0]

	c20_t1_in = S.Task('c20_t1_in', length=1, delay_cost=1)
	S += c20_t1_in >= 7
	c20_t1_in += MM_in[0]

	c20_t1_mem0 = S.Task('c20_t1_mem0', length=1, delay_cost=1)
	S += c20_t1_mem0 >= 7
	c20_t1_mem0 += MAIN_MEM_r[0]

	c20_t1_mem1 = S.Task('c20_t1_mem1', length=1, delay_cost=1)
	S += c20_t1_mem1 >= 7
	c20_t1_mem1 += MAIN_MEM_r[1]

	c11_t0_in = S.Task('c11_t0_in', length=1, delay_cost=1)
	S += c11_t0_in >= 8
	c11_t0_in += MM_in[0]

	c11_t0_mem0 = S.Task('c11_t0_mem0', length=1, delay_cost=1)
	S += c11_t0_mem0 >= 8
	c11_t0_mem0 += MAIN_MEM_r[0]

	c11_t0_mem1 = S.Task('c11_t0_mem1', length=1, delay_cost=1)
	S += c11_t0_mem1 >= 8
	c11_t0_mem1 += MAIN_MEM_r[1]

	c20_t1 = S.Task('c20_t1', length=5, delay_cost=1)
	S += c20_t1 >= 8
	c20_t1 += MM[0]

	c11_t0 = S.Task('c11_t0', length=5, delay_cost=1)
	S += c11_t0 >= 9
	c11_t0 += MM[0]

	c11_t1_in = S.Task('c11_t1_in', length=1, delay_cost=1)
	S += c11_t1_in >= 9
	c11_t1_in += MM_in[0]

	c11_t1_mem0 = S.Task('c11_t1_mem0', length=1, delay_cost=1)
	S += c11_t1_mem0 >= 9
	c11_t1_mem0 += MAIN_MEM_r[0]

	c11_t1_mem1 = S.Task('c11_t1_mem1', length=1, delay_cost=1)
	S += c11_t1_mem1 >= 9
	c11_t1_mem1 += MAIN_MEM_r[1]

	c11_t1 = S.Task('c11_t1', length=5, delay_cost=1)
	S += c11_t1 >= 10
	c11_t1 += MM[0]

	c20_t2_mem0 = S.Task('c20_t2_mem0', length=1, delay_cost=1)
	S += c20_t2_mem0 >= 10
	c20_t2_mem0 += MAIN_MEM_r[0]

	c20_t2_mem1 = S.Task('c20_t2_mem1', length=1, delay_cost=1)
	S += c20_t2_mem1 >= 10
	c20_t2_mem1 += MAIN_MEM_r[1]

	c01_t2_mem0 = S.Task('c01_t2_mem0', length=1, delay_cost=1)
	S += c01_t2_mem0 >= 11
	c01_t2_mem0 += MAIN_MEM_r[0]

	c01_t2_mem1 = S.Task('c01_t2_mem1', length=1, delay_cost=1)
	S += c01_t2_mem1 >= 11
	c01_t2_mem1 += MAIN_MEM_r[1]

	c20_t2 = S.Task('c20_t2', length=1, delay_cost=1)
	S += c20_t2 >= 11
	c20_t2 += MAS[1]

	c01_t2 = S.Task('c01_t2', length=1, delay_cost=1)
	S += c01_t2 >= 12
	c01_t2 += MAS[4]

	c11_t3_mem0 = S.Task('c11_t3_mem0', length=1, delay_cost=1)
	S += c11_t3_mem0 >= 12
	c11_t3_mem0 += MAIN_MEM_r[0]

	c11_t3_mem1 = S.Task('c11_t3_mem1', length=1, delay_cost=1)
	S += c11_t3_mem1 >= 12
	c11_t3_mem1 += MAIN_MEM_r[1]

	c11_t3 = S.Task('c11_t3', length=1, delay_cost=1)
	S += c11_t3 >= 13
	c11_t3 += MAS[2]

	c21_t3_mem0 = S.Task('c21_t3_mem0', length=1, delay_cost=1)
	S += c21_t3_mem0 >= 13
	c21_t3_mem0 += MAIN_MEM_r[0]

	c21_t3_mem1 = S.Task('c21_t3_mem1', length=1, delay_cost=1)
	S += c21_t3_mem1 >= 13
	c21_t3_mem1 += MAIN_MEM_r[1]

	c21_t2_mem0 = S.Task('c21_t2_mem0', length=1, delay_cost=1)
	S += c21_t2_mem0 >= 14
	c21_t2_mem0 += MAIN_MEM_r[0]

	c21_t2_mem1 = S.Task('c21_t2_mem1', length=1, delay_cost=1)
	S += c21_t2_mem1 >= 14
	c21_t2_mem1 += MAIN_MEM_r[1]

	c21_t3 = S.Task('c21_t3', length=1, delay_cost=1)
	S += c21_t3 >= 14
	c21_t3 += MAS[2]

	c10_t2_mem0 = S.Task('c10_t2_mem0', length=1, delay_cost=1)
	S += c10_t2_mem0 >= 15
	c10_t2_mem0 += MAIN_MEM_r[0]

	c10_t2_mem1 = S.Task('c10_t2_mem1', length=1, delay_cost=1)
	S += c10_t2_mem1 >= 15
	c10_t2_mem1 += MAIN_MEM_r[1]

	c21_t2 = S.Task('c21_t2', length=1, delay_cost=1)
	S += c21_t2 >= 15
	c21_t2 += MAS[3]

	c10_t2 = S.Task('c10_t2', length=1, delay_cost=1)
	S += c10_t2 >= 16
	c10_t2 += MAS[0]

	c20_t3_mem0 = S.Task('c20_t3_mem0', length=1, delay_cost=1)
	S += c20_t3_mem0 >= 16
	c20_t3_mem0 += MAIN_MEM_r[0]

	c20_t3_mem1 = S.Task('c20_t3_mem1', length=1, delay_cost=1)
	S += c20_t3_mem1 >= 16
	c20_t3_mem1 += MAIN_MEM_r[1]

	c11_t2_mem0 = S.Task('c11_t2_mem0', length=1, delay_cost=1)
	S += c11_t2_mem0 >= 17
	c11_t2_mem0 += MAIN_MEM_r[0]

	c11_t2_mem1 = S.Task('c11_t2_mem1', length=1, delay_cost=1)
	S += c11_t2_mem1 >= 17
	c11_t2_mem1 += MAIN_MEM_r[1]

	c20_t3 = S.Task('c20_t3', length=1, delay_cost=1)
	S += c20_t3 >= 17
	c20_t3 += MAS[1]

	c01_t3_mem0 = S.Task('c01_t3_mem0', length=1, delay_cost=1)
	S += c01_t3_mem0 >= 18
	c01_t3_mem0 += MAIN_MEM_r[0]

	c01_t3_mem1 = S.Task('c01_t3_mem1', length=1, delay_cost=1)
	S += c01_t3_mem1 >= 18
	c01_t3_mem1 += MAIN_MEM_r[1]

	c11_t2 = S.Task('c11_t2', length=1, delay_cost=1)
	S += c11_t2 >= 18
	c11_t2 += MAS[0]

	c01_t3 = S.Task('c01_t3', length=1, delay_cost=1)
	S += c01_t3 >= 19
	c01_t3 += MAS[0]

	c10_t3_mem0 = S.Task('c10_t3_mem0', length=1, delay_cost=1)
	S += c10_t3_mem0 >= 19
	c10_t3_mem0 += MAIN_MEM_r[0]

	c10_t3_mem1 = S.Task('c10_t3_mem1', length=1, delay_cost=1)
	S += c10_t3_mem1 >= 19
	c10_t3_mem1 += MAIN_MEM_r[1]

	c10_t3 = S.Task('c10_t3', length=1, delay_cost=1)
	S += c10_t3 >= 20
	c10_t3 += MAS[3]


	# new tasks
	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)

	S += 0<c000

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAIN_MEM_r[0]
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += MAIN_MEM_r[1]
	S += c000_mem1 <= c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)

	S += 0<c001

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAIN_MEM_r[0]
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += MAIN_MEM_r[1]
	S += c001_mem1 <= c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS5/FROB/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

