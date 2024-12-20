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
	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	t0_in += alt(MM_in)
	t0 = S.Task('t0', length=7, delay_cost=1)
	t0 += alt(MM)
	S += t0>=t0_in

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	t0_mem0 += MAIN_MEM_r[0]
	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	t3_in += alt(MM_in)
	t3 = S.Task('t3', length=7, delay_cost=1)
	t3 += alt(MM)
	S += t3>=t3_in

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	t3_mem0 += MAIN_MEM_r[0]
	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	t3_mem1 += MAIN_MEM_r[1]
	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	t1_in += alt(MM_in)
	t1 = S.Task('t1', length=7, delay_cost=1)
	t1 += alt(MM)
	S += t1>=t1_in

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	t1_mem0 += MAIN_MEM_r[0]
	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	t1_mem1 += MAIN_MEM_r[1]
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	t2_in += alt(MM_in)
	t2 = S.Task('t2', length=7, delay_cost=1)
	t2 += alt(MM)
	S += t2>=t2_in

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	t2_mem0 += MAIN_MEM_r[0]
	t4_in = S.Task('t4_in', length=1, delay_cost=1)
	t4_in += alt(MM_in)
	t4 = S.Task('t4', length=7, delay_cost=1)
	t4 += alt(MM)
	S += t4>=t4_in

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	t4_mem0 += MAIN_MEM_r[0]
	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	t4_mem1 += alt(MM_MEM)
	S += (t2*MM[0])-1 < t4_mem1*MM_MEM[1]
	S += t4_mem1 <= t4

	t5 = S.Task('t5', length=1, delay_cost=1)
	t5 += alt(MAS)

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	t5_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t5_mem0*MM_MEM[0]
	S += t5_mem0 <= t5

	t6 = S.Task('t6', length=1, delay_cost=1)
	t6 += alt(MAS)

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	t6_mem0 += alt(MAS_MEM)
	S += (t5*MAS[0])-1 < t6_mem0*MAS_MEM[0]
	S += (t5*MAS[1])-1 < t6_mem0*MAS_MEM[2]
	S += (t5*MAS[2])-1 < t6_mem0*MAS_MEM[4]
	S += (t5*MAS[3])-1 < t6_mem0*MAS_MEM[6]
	S += (t5*MAS[4])-1 < t6_mem0*MAS_MEM[8]
	S += t6_mem0 <= t6

	t9 = S.Task('t9', length=1, delay_cost=1)
	t9 += alt(MAS)

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	t9_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t9_mem0*MM_MEM[0]
	S += t9_mem0 <= t9

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	t9_mem1 += alt(MM_MEM)
	S += (t4*MM[0])-1 < t9_mem1*MM_MEM[1]
	S += t9_mem1 <= t9

	t10 = S.Task('t10', length=1, delay_cost=1)
	t10 += alt(MAS)

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += alt(MM_MEM)
	S += (t4*MM[0])-1 < t10_mem0*MM_MEM[0]
	S += t10_mem0 <= t10

	t7 = S.Task('t7', length=1, delay_cost=1)
	t7 += alt(MAS)

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	t7_mem0 += alt(MAS_MEM)
	S += (t6*MAS[0])-1 < t7_mem0*MAS_MEM[0]
	S += (t6*MAS[1])-1 < t7_mem0*MAS_MEM[2]
	S += (t6*MAS[2])-1 < t7_mem0*MAS_MEM[4]
	S += (t6*MAS[3])-1 < t7_mem0*MAS_MEM[6]
	S += (t6*MAS[4])-1 < t7_mem0*MAS_MEM[8]
	S += t7_mem0 <= t7

	t11 = S.Task('t11', length=1, delay_cost=1)
	t11 += alt(MAS)

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t11_mem0*MAS_MEM[0]
	S += (t10*MAS[1])-1 < t11_mem0*MAS_MEM[2]
	S += (t10*MAS[2])-1 < t11_mem0*MAS_MEM[4]
	S += (t10*MAS[3])-1 < t11_mem0*MAS_MEM[6]
	S += (t10*MAS[4])-1 < t11_mem0*MAS_MEM[8]
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += alt(MM_MEM)
	S += (t4*MM[0])-1 < t11_mem1*MM_MEM[1]
	S += t11_mem1 <= t11

	t8_in = S.Task('t8_in', length=1, delay_cost=1)
	t8_in += alt(MM_in)
	t8 = S.Task('t8', length=7, delay_cost=1)
	t8 += alt(MM)
	S += t8>=t8_in

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	t8_mem0 += alt(MM_MEM)
	S += (t4*MM[0])-1 < t8_mem0*MM_MEM[0]
	S += t8_mem0 <= t8

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	t8_mem1 += alt(MAS_MEM)
	S += (t7*MAS[0])-1 < t8_mem1*MAS_MEM[1]
	S += (t7*MAS[1])-1 < t8_mem1*MAS_MEM[3]
	S += (t7*MAS[2])-1 < t8_mem1*MAS_MEM[5]
	S += (t7*MAS[3])-1 < t8_mem1*MAS_MEM[7]
	S += (t7*MAS[4])-1 < t8_mem1*MAS_MEM[9]
	S += t8_mem1 <= t8

	new_PZ_in = S.Task('new_PZ_in', length=1, delay_cost=1)
	new_PZ_in += alt(MM_in)
	new_PZ = S.Task('new_PZ', length=7, delay_cost=1)
	new_PZ += alt(MM)
	S += new_PZ>=new_PZ_in

	S += 0<new_PZ

	new_PZ_w = S.Task('new_PZ_w', length=1, delay_cost=1)
	new_PZ_w += alt(MAIN_MEM_w)
	S += new_PZ <= new_PZ_w

	new_PZ_mem0 = S.Task('new_PZ_mem0', length=1, delay_cost=1)
	new_PZ_mem0 += alt(MM_MEM)
	S += (t1*MM[0])-1 < new_PZ_mem0*MM_MEM[0]
	S += new_PZ_mem0 <= new_PZ

	new_PZ_mem1 = S.Task('new_PZ_mem1', length=1, delay_cost=1)
	new_PZ_mem1 += alt(MAS_MEM)
	S += (t7*MAS[0])-1 < new_PZ_mem1*MAS_MEM[1]
	S += (t7*MAS[1])-1 < new_PZ_mem1*MAS_MEM[3]
	S += (t7*MAS[2])-1 < new_PZ_mem1*MAS_MEM[5]
	S += (t7*MAS[3])-1 < new_PZ_mem1*MAS_MEM[7]
	S += (t7*MAS[4])-1 < new_PZ_mem1*MAS_MEM[9]
	S += new_PZ_mem1 <= new_PZ

	t12 = S.Task('t12', length=1, delay_cost=1)
	t12 += alt(MAS)

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	t12_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t12_mem0*MM_MEM[0]
	S += t12_mem0 <= t12

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	t12_mem1 += alt(MAS_MEM)
	S += (t11*MAS[0])-1 < t12_mem1*MAS_MEM[1]
	S += (t11*MAS[1])-1 < t12_mem1*MAS_MEM[3]
	S += (t11*MAS[2])-1 < t12_mem1*MAS_MEM[5]
	S += (t11*MAS[3])-1 < t12_mem1*MAS_MEM[7]
	S += (t11*MAS[4])-1 < t12_mem1*MAS_MEM[9]
	S += t12_mem1 <= t12

	t13_in = S.Task('t13_in', length=1, delay_cost=1)
	t13_in += alt(MM_in)
	t13 = S.Task('t13', length=7, delay_cost=1)
	t13 += alt(MM)
	S += t13>=t13_in

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	t13_mem0 += alt(MAS_MEM)
	S += (t12*MAS[0])-1 < t13_mem0*MAS_MEM[0]
	S += (t12*MAS[1])-1 < t13_mem0*MAS_MEM[2]
	S += (t12*MAS[2])-1 < t13_mem0*MAS_MEM[4]
	S += (t12*MAS[3])-1 < t13_mem0*MAS_MEM[6]
	S += (t12*MAS[4])-1 < t13_mem0*MAS_MEM[8]
	S += t13_mem0 <= t13

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	t13_mem1 += alt(MAS_MEM)
	S += (t9*MAS[0])-1 < t13_mem1*MAS_MEM[1]
	S += (t9*MAS[1])-1 < t13_mem1*MAS_MEM[3]
	S += (t9*MAS[2])-1 < t13_mem1*MAS_MEM[5]
	S += (t9*MAS[3])-1 < t13_mem1*MAS_MEM[7]
	S += (t9*MAS[4])-1 < t13_mem1*MAS_MEM[9]
	S += t13_mem1 <= t13

	t14_in = S.Task('t14_in', length=1, delay_cost=1)
	t14_in += alt(MM_in)
	t14 = S.Task('t14', length=7, delay_cost=1)
	t14 += alt(MM)
	S += t14>=t14_in

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	t14_mem0 += alt(MAS_MEM)
	S += (t12*MAS[0])-1 < t14_mem0*MAS_MEM[0]
	S += (t12*MAS[1])-1 < t14_mem0*MAS_MEM[2]
	S += (t12*MAS[2])-1 < t14_mem0*MAS_MEM[4]
	S += (t12*MAS[3])-1 < t14_mem0*MAS_MEM[6]
	S += (t12*MAS[4])-1 < t14_mem0*MAS_MEM[8]
	S += t14_mem0 <= t14

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	t14_mem1 += alt(MM_MEM)
	S += (t3*MM[0])-1 < t14_mem1*MM_MEM[1]
	S += t14_mem1 <= t14

	new_PY = S.Task('new_PY', length=1, delay_cost=1)
	new_PY += alt(MAS)

	S += 0<new_PY

	new_PY_w = S.Task('new_PY_w', length=1, delay_cost=1)
	new_PY_w += alt(MAIN_MEM_w)
	S += new_PY <= new_PY_w

	new_PY_mem0 = S.Task('new_PY_mem0', length=1, delay_cost=1)
	new_PY_mem0 += alt(MM_MEM)
	S += (t8*MM[0])-1 < new_PY_mem0*MM_MEM[0]
	S += new_PY_mem0 <= new_PY

	new_PY_mem1 = S.Task('new_PY_mem1', length=1, delay_cost=1)
	new_PY_mem1 += alt(MM_MEM)
	S += (t13*MM[0])-1 < new_PY_mem1*MM_MEM[1]
	S += new_PY_mem1 <= new_PY

	new_PX = S.Task('new_PX', length=1, delay_cost=1)
	new_PX += alt(MAS)

	S += 0<new_PX

	new_PX_w = S.Task('new_PX_w', length=1, delay_cost=1)
	new_PX_w += alt(MAIN_MEM_w)
	S += new_PX <= new_PX_w

	new_PX_mem0 = S.Task('new_PX_mem0', length=1, delay_cost=1)
	new_PX_mem0 += alt(MM_MEM)
	S += (t14*MM[0])-1 < new_PX_mem0*MM_MEM[0]
	S += new_PX_mem0 <= new_PX

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM1_stage1MAS5/EP_DBL_A_0/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

