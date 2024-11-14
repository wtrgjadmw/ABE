from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 112
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
	Z_exp2_in = S.Task('Z_exp2_in', length=1, delay_cost=1)
	Z_exp2_in += alt(MM_in)
	Z_exp2 = S.Task('Z_exp2', length=5, delay_cost=1)
	Z_exp2 += alt(MM)
	S += Z_exp2>=Z_exp2_in

	Z_exp2_mem0 = S.Task('Z_exp2_mem0', length=1, delay_cost=1)
	Z_exp2_mem0 += MAIN_MEM_r
	S += Z_exp2_mem0 <= Z_exp2

	Z_exp2_mem1 = S.Task('Z_exp2_mem1', length=1, delay_cost=1)
	Z_exp2_mem1 += MAIN_MEM_r
	S += Z_exp2_mem1 <= Z_exp2

	NX0_in = S.Task('NX0_in', length=1, delay_cost=1)
	NX0_in += alt(MM_in)
	NX0 = S.Task('NX0', length=5, delay_cost=1)
	NX0 += alt(MM)
	S += NX0>=NX0_in

	NX0_mem0 = S.Task('NX0_mem0', length=1, delay_cost=1)
	NX0_mem0 += MAIN_MEM_r
	S += NX0_mem0 <= NX0

	NX0_mem1 = S.Task('NX0_mem1', length=1, delay_cost=1)
	NX0_mem1 += MAIN_MEM_r
	S += NX0_mem1 <= NX0

	k0_10_Z1_in = S.Task('k0_10_Z1_in', length=1, delay_cost=1)
	k0_10_Z1_in += alt(MM_in)
	k0_10_Z1 = S.Task('k0_10_Z1', length=5, delay_cost=1)
	k0_10_Z1 += alt(MM)
	S += k0_10_Z1>=k0_10_Z1_in

	k0_10_Z1_mem0 = S.Task('k0_10_Z1_mem0', length=1, delay_cost=1)
	k0_10_Z1_mem0 += MAIN_MEM_r
	S += k0_10_Z1_mem0 <= k0_10_Z1

	k0_10_Z1_mem1 = S.Task('k0_10_Z1_mem1', length=1, delay_cost=1)
	k0_10_Z1_mem1 += MAIN_MEM_r
	S += k0_10_Z1_mem1 <= k0_10_Z1

	DX0_in = S.Task('DX0_in', length=1, delay_cost=1)
	DX0_in += alt(MM_in)
	DX0 = S.Task('DX0', length=5, delay_cost=1)
	DX0 += alt(MM)
	S += DX0>=DX0_in

	DX0_mem0 = S.Task('DX0_mem0', length=1, delay_cost=1)
	DX0_mem0 += MAIN_MEM_r
	S += DX0_mem0 <= DX0

	DX0_mem1 = S.Task('DX0_mem1', length=1, delay_cost=1)
	DX0_mem1 += MAIN_MEM_r
	S += DX0_mem1 <= DX0

	NY0_in = S.Task('NY0_in', length=1, delay_cost=1)
	NY0_in += alt(MM_in)
	NY0 = S.Task('NY0', length=5, delay_cost=1)
	NY0 += alt(MM)
	S += NY0>=NY0_in

	NY0_mem0 = S.Task('NY0_mem0', length=1, delay_cost=1)
	NY0_mem0 += MAIN_MEM_r
	S += NY0_mem0 <= NY0

	NY0_mem1 = S.Task('NY0_mem1', length=1, delay_cost=1)
	NY0_mem1 += MAIN_MEM_r
	S += NY0_mem1 <= NY0

	k2_14_Z1_in = S.Task('k2_14_Z1_in', length=1, delay_cost=1)
	k2_14_Z1_in += alt(MM_in)
	k2_14_Z1 = S.Task('k2_14_Z1', length=5, delay_cost=1)
	k2_14_Z1 += alt(MM)
	S += k2_14_Z1>=k2_14_Z1_in

	k2_14_Z1_mem0 = S.Task('k2_14_Z1_mem0', length=1, delay_cost=1)
	k2_14_Z1_mem0 += MAIN_MEM_r
	S += k2_14_Z1_mem0 <= k2_14_Z1

	k2_14_Z1_mem1 = S.Task('k2_14_Z1_mem1', length=1, delay_cost=1)
	k2_14_Z1_mem1 += MAIN_MEM_r
	S += k2_14_Z1_mem1 <= k2_14_Z1

	DY0_in = S.Task('DY0_in', length=1, delay_cost=1)
	DY0_in += alt(MM_in)
	DY0 = S.Task('DY0', length=5, delay_cost=1)
	DY0 += alt(MM)
	S += DY0>=DY0_in

	DY0_mem0 = S.Task('DY0_mem0', length=1, delay_cost=1)
	DY0_mem0 += MAIN_MEM_r
	S += DY0_mem0 <= DY0

	DY0_mem1 = S.Task('DY0_mem1', length=1, delay_cost=1)
	DY0_mem1 += MAIN_MEM_r
	S += DY0_mem1 <= DY0

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage5MM1_stage1MAS4/ISOGENY/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

