from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MAS_in = S.Resources('MAS_in', num=4)
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	c000_in += alt(MAS_in)
	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)

	S += c000>=c000_in

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

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	c001_in += alt(MAS_in)
	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)

	S += c001>=c001_in

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

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MAS_in)
	c010 = S.Task('c010', length=1, delay_cost=1)
	c010 += alt(MAS)

	S += c010>=c010_in

	S += 0<c010

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += MAIN_MEM_r[0]
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += MAIN_MEM_r[1]
	S += c010_mem1 <= c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MAS_in)
	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(MAS)

	S += c011>=c011_in

	S += 0<c011

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MAIN_MEM_r[0]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += MAIN_MEM_r[1]
	S += c011_mem1 <= c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	c100_in += alt(MAS_in)
	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(MAS)

	S += c100>=c100_in

	S += 0<c100

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += MAIN_MEM_r[0]
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += MAIN_MEM_r[1]
	S += c100_mem1 <= c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	c101_in += alt(MAS_in)
	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(MAS)

	S += c101>=c101_in

	S += 0<c101

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += MAIN_MEM_r[0]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += MAIN_MEM_r[1]
	S += c101_mem1 <= c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	c110_in += alt(MAS_in)
	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(MAS)

	S += c110>=c110_in

	S += 0<c110

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAIN_MEM_r[0]
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MAIN_MEM_r[1]
	S += c110_mem1 <= c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	c111_in += alt(MAS_in)
	c111 = S.Task('c111', length=1, delay_cost=1)
	c111 += alt(MAS)

	S += c111>=c111_in

	S += 0<c111

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += MAIN_MEM_r[0]
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += MAIN_MEM_r[1]
	S += c111_mem1 <= c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MAS_in)
	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(MAS)

	S += c200>=c200_in

	S += 0<c200

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += MAIN_MEM_r[0]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAIN_MEM_r[1]
	S += c200_mem1 <= c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MAS_in)
	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(MAS)

	S += c201>=c201_in

	S += 0<c201

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += MAIN_MEM_r[0]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += MAIN_MEM_r[1]
	S += c201_mem1 <= c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	c210_in += alt(MAS_in)
	c210 = S.Task('c210', length=1, delay_cost=1)
	c210 += alt(MAS)

	S += c210>=c210_in

	S += 0<c210

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MAIN_MEM_r[0]
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MAIN_MEM_r[1]
	S += c210_mem1 <= c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	c211_in += alt(MAS_in)
	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(MAS)

	S += c211>=c211_in

	S += 0<c211

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += MAIN_MEM_r[0]
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += MAIN_MEM_r[1]
	S += c211_mem1 <= c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage6MM1_stage1MAS4/CONJ/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

