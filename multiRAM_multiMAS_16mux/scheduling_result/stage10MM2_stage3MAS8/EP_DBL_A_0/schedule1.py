from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 164
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=8)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	S += t2_in >= 0
	t2_in += MM_in[0]

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	S += t2_mem0 >= 0
	t2_mem0 += MAIN_MEM_r[0]

	t2_mem1 = S.Task('t2_mem1', length=1, delay_cost=1)
	S += t2_mem1 >= 0
	t2_mem1 += MAIN_MEM_r[1]

	t2 = S.Task('t2', length=10, delay_cost=1)
	S += t2 >= 1
	t2 += MM[0]

	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	S += t3_in >= 2
	t3_in += MM_in[0]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 2
	t3_mem0 += MAIN_MEM_r[0]

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 2
	t3_mem1 += MAIN_MEM_r[1]

	t3 = S.Task('t3', length=10, delay_cost=1)
	S += t3 >= 3
	t3 += MM[0]

	t6_in = S.Task('t6_in', length=1, delay_cost=1)
	S += t6_in >= 14
	t6_in += MAS_in[7]

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	S += t6_mem0 >= 14
	t6_mem0 += MAS_MEM[2]

	t6_mem1 = S.Task('t6_mem1', length=1, delay_cost=1)
	S += t6_mem1 >= 14
	t6_mem1 += MAS_MEM[3]

	t6 = S.Task('t6', length=3, delay_cost=1)
	S += t6 >= 15
	t6 += MAS[7]

	t7_in = S.Task('t7_in', length=1, delay_cost=1)
	S += t7_in >= 17
	t7_in += MAS_in[0]

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	S += t7_mem0 >= 17
	t7_mem0 += MAS_MEM[14]

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	S += t7_mem1 >= 17
	t7_mem1 += MAS_MEM[15]

	t7 = S.Task('t7', length=3, delay_cost=1)
	S += t7 >= 18
	t7 += MAS[0]

	new_PZ_in = S.Task('new_PZ_in', length=1, delay_cost=1)
	S += new_PZ_in >= 20
	new_PZ_in += MM_in[0]

	new_PZ_mem0 = S.Task('new_PZ_mem0', length=1, delay_cost=1)
	S += new_PZ_mem0 >= 20
	new_PZ_mem0 += MM_MEM[0]

	new_PZ_mem1 = S.Task('new_PZ_mem1', length=1, delay_cost=1)
	S += new_PZ_mem1 >= 20
	new_PZ_mem1 += MAS_MEM[1]

	new_PZ = S.Task('new_PZ', length=10, delay_cost=1)
	S += new_PZ >= 21
	new_PZ += MM[0]

	t9_in = S.Task('t9_in', length=1, delay_cost=1)
	S += t9_in >= 21
	t9_in += MAS_in[7]

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	S += t9_mem0 >= 21
	t9_mem0 += MM_MEM[0]

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	S += t9_mem1 >= 21
	t9_mem1 += MM_MEM[3]

	t9 = S.Task('t9', length=3, delay_cost=1)
	S += t9 >= 22
	t9 += MAS[7]

	new_PZ_w = S.Task('new_PZ_w', length=1, delay_cost=1)
	S += new_PZ_w >= 31
	new_PZ_w += MAIN_MEM_w

	new_PX_in = S.Task('new_PX_in', length=1, delay_cost=1)
	S += new_PX_in >= 39
	new_PX_in += MAS_in[7]

	new_PX_mem0 = S.Task('new_PX_mem0', length=1, delay_cost=1)
	S += new_PX_mem0 >= 39
	new_PX_mem0 += MM_MEM[0]

	new_PX_mem1 = S.Task('new_PX_mem1', length=1, delay_cost=1)
	S += new_PX_mem1 >= 39
	new_PX_mem1 += MM_MEM[1]

	new_PX = S.Task('new_PX', length=3, delay_cost=1)
	S += new_PX >= 40
	new_PX += MAS[7]

	new_PX_w = S.Task('new_PX_w', length=1, delay_cost=1)
	S += new_PX_w >= 43
	new_PX_w += MAIN_MEM_w


	# new tasks
	t0 = S.Task('t0', length=10, delay_cost=1)
	t0 += alt(MM)
	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	t0_in += alt(MM_in)
	S += t0_in*MM_in[0]<=t0*MM[0]
	S += t0_in*MM_in[1]<=t0*MM[1]
	S += t0<12

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	t0_mem0 += MAIN_MEM_r[0]
	S += t0_mem0 <= t0

	t0_mem1 = S.Task('t0_mem1', length=1, delay_cost=1)
	t0_mem1 += MAIN_MEM_r[1]
	S += t0_mem1 <= t0

	t1 = S.Task('t1', length=10, delay_cost=1)
	t1 += alt(MM)
	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	t1_in += alt(MM_in)
	S += t1_in*MM_in[0]<=t1*MM[0]
	S += t1_in*MM_in[1]<=t1*MM[1]
	S += t1<21

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	t1_mem0 += MAIN_MEM_r[0]
	S += t1_mem0 <= t1

	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	t1_mem1 += MAIN_MEM_r[1]
	S += t1_mem1 <= t1

	t4 = S.Task('t4', length=10, delay_cost=1)
	t4 += alt(MM)
	t4_in = S.Task('t4_in', length=1, delay_cost=1)
	t4_in += alt(MM_in)
	S += t4_in*MM_in[0]<=t4*MM[0]
	S += t4_in*MM_in[1]<=t4*MM[1]
	S += t4<21

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	t4_mem0 += MAIN_MEM_r[0]
	S += t4_mem0 <= t4

	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	t4_mem1 += MM_MEM[1]
	S += 10 < t4_mem1
	S += t4_mem1 <= t4

	t5 = S.Task('t5', length=3, delay_cost=1)
	t5 += alt(MAS)
	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	t5_in += alt(MAS_in)
	S += t5_in*MAS_in[0]<=t5*MAS[0]

	S += t5_in*MAS_in[1]<=t5*MAS[1]

	S += t5_in*MAS_in[2]<=t5*MAS[2]

	S += t5_in*MAS_in[3]<=t5*MAS[3]

	S += t5_in*MAS_in[4]<=t5*MAS[4]

	S += t5_in*MAS_in[5]<=t5*MAS[5]

	S += t5_in*MAS_in[6]<=t5*MAS[6]

	S += t5_in*MAS_in[7]<=t5*MAS[7]

	S += t5<15

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	t5_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t5_mem0*MM_MEM[0]
	S += (t0*MM[1])-1 < t5_mem0*MM_MEM[2]
	S += t5_mem0 <= t5

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	t5_mem1 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t5_mem1*MM_MEM[1]
	S += (t0*MM[1])-1 < t5_mem1*MM_MEM[3]
	S += t5_mem1 <= t5

	t10 = S.Task('t10', length=3, delay_cost=1)
	t10 += alt(MAS)
	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	t10_in += alt(MAS_in)
	S += t10_in*MAS_in[0]<=t10*MAS[0]

	S += t10_in*MAS_in[1]<=t10*MAS[1]

	S += t10_in*MAS_in[2]<=t10*MAS[2]

	S += t10_in*MAS_in[3]<=t10*MAS[3]

	S += t10_in*MAS_in[4]<=t10*MAS[4]

	S += t10_in*MAS_in[5]<=t10*MAS[5]

	S += t10_in*MAS_in[6]<=t10*MAS[6]

	S += t10_in*MAS_in[7]<=t10*MAS[7]

	S += t10<24

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += alt(MM_MEM)
	S += (t4*MM[0])-1 < t10_mem0*MM_MEM[0]
	S += (t4*MM[1])-1 < t10_mem0*MM_MEM[2]
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += alt(MM_MEM)
	S += (t4*MM[0])-1 < t10_mem1*MM_MEM[1]
	S += (t4*MM[1])-1 < t10_mem1*MM_MEM[3]
	S += t10_mem1 <= t10

	t11 = S.Task('t11', length=3, delay_cost=1)
	t11 += alt(MAS)
	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	t11_in += alt(MAS_in)
	S += t11_in*MAS_in[0]<=t11*MAS[0]

	S += t11_in*MAS_in[1]<=t11*MAS[1]

	S += t11_in*MAS_in[2]<=t11*MAS[2]

	S += t11_in*MAS_in[3]<=t11*MAS[3]

	S += t11_in*MAS_in[4]<=t11*MAS[4]

	S += t11_in*MAS_in[5]<=t11*MAS[5]

	S += t11_in*MAS_in[6]<=t11*MAS[6]

	S += t11_in*MAS_in[7]<=t11*MAS[7]

	S += t11<27

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t11_mem0*MAS_MEM[0]
	S += (t10*MAS[1])-1 < t11_mem0*MAS_MEM[2]
	S += (t10*MAS[2])-1 < t11_mem0*MAS_MEM[4]
	S += (t10*MAS[3])-1 < t11_mem0*MAS_MEM[6]
	S += (t10*MAS[4])-1 < t11_mem0*MAS_MEM[8]
	S += (t10*MAS[5])-1 < t11_mem0*MAS_MEM[10]
	S += (t10*MAS[6])-1 < t11_mem0*MAS_MEM[12]
	S += (t10*MAS[7])-1 < t11_mem0*MAS_MEM[14]
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += alt(MM_MEM)
	S += (t4*MM[0])-1 < t11_mem1*MM_MEM[1]
	S += (t4*MM[1])-1 < t11_mem1*MM_MEM[3]
	S += t11_mem1 <= t11

	t8 = S.Task('t8', length=10, delay_cost=1)
	t8 += alt(MM)
	t8_in = S.Task('t8_in', length=1, delay_cost=1)
	t8_in += alt(MM_in)
	S += t8_in*MM_in[0]<=t8*MM[0]
	S += t8_in*MM_in[1]<=t8*MM[1]
	S += t8<41

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	t8_mem0 += alt(MM_MEM)
	S += (t4*MM[0])-1 < t8_mem0*MM_MEM[0]
	S += (t4*MM[1])-1 < t8_mem0*MM_MEM[2]
	S += t8_mem0 <= t8

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	t8_mem1 += MAS_MEM[1]
	S += 20 < t8_mem1
	S += t8_mem1 <= t8

	t12 = S.Task('t12', length=3, delay_cost=1)
	t12 += alt(MAS)
	t12_in = S.Task('t12_in', length=1, delay_cost=1)
	t12_in += alt(MAS_in)
	S += t12_in*MAS_in[0]<=t12*MAS[0]

	S += t12_in*MAS_in[1]<=t12*MAS[1]

	S += t12_in*MAS_in[2]<=t12*MAS[2]

	S += t12_in*MAS_in[3]<=t12*MAS[3]

	S += t12_in*MAS_in[4]<=t12*MAS[4]

	S += t12_in*MAS_in[5]<=t12*MAS[5]

	S += t12_in*MAS_in[6]<=t12*MAS[6]

	S += t12_in*MAS_in[7]<=t12*MAS[7]

	S += t12<30

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	t12_mem0 += alt(MM_MEM)
	S += (t0*MM[0])-1 < t12_mem0*MM_MEM[0]
	S += (t0*MM[1])-1 < t12_mem0*MM_MEM[2]
	S += t12_mem0 <= t12

	t12_mem1 = S.Task('t12_mem1', length=1, delay_cost=1)
	t12_mem1 += alt(MAS_MEM)
	S += (t11*MAS[0])-1 < t12_mem1*MAS_MEM[1]
	S += (t11*MAS[1])-1 < t12_mem1*MAS_MEM[3]
	S += (t11*MAS[2])-1 < t12_mem1*MAS_MEM[5]
	S += (t11*MAS[3])-1 < t12_mem1*MAS_MEM[7]
	S += (t11*MAS[4])-1 < t12_mem1*MAS_MEM[9]
	S += (t11*MAS[5])-1 < t12_mem1*MAS_MEM[11]
	S += (t11*MAS[6])-1 < t12_mem1*MAS_MEM[13]
	S += (t11*MAS[7])-1 < t12_mem1*MAS_MEM[15]
	S += t12_mem1 <= t12

	t13 = S.Task('t13', length=10, delay_cost=1)
	t13 += alt(MM)
	t13_in = S.Task('t13_in', length=1, delay_cost=1)
	t13_in += alt(MM_in)
	S += t13_in*MM_in[0]<=t13*MM[0]
	S += t13_in*MM_in[1]<=t13*MM[1]
	S += t13<41

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	t13_mem0 += alt(MAS_MEM)
	S += (t12*MAS[0])-1 < t13_mem0*MAS_MEM[0]
	S += (t12*MAS[1])-1 < t13_mem0*MAS_MEM[2]
	S += (t12*MAS[2])-1 < t13_mem0*MAS_MEM[4]
	S += (t12*MAS[3])-1 < t13_mem0*MAS_MEM[6]
	S += (t12*MAS[4])-1 < t13_mem0*MAS_MEM[8]
	S += (t12*MAS[5])-1 < t13_mem0*MAS_MEM[10]
	S += (t12*MAS[6])-1 < t13_mem0*MAS_MEM[12]
	S += (t12*MAS[7])-1 < t13_mem0*MAS_MEM[14]
	S += t13_mem0 <= t13

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	t13_mem1 += MAS_MEM[15]
	S += 24 < t13_mem1
	S += t13_mem1 <= t13

	t14 = S.Task('t14', length=10, delay_cost=1)
	t14 += alt(MM)
	t14_in = S.Task('t14_in', length=1, delay_cost=1)
	t14_in += alt(MM_in)
	S += t14_in*MM_in[0]<=t14*MM[0]
	S += t14_in*MM_in[1]<=t14*MM[1]
	S += t14<40

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	t14_mem0 += alt(MAS_MEM)
	S += (t12*MAS[0])-1 < t14_mem0*MAS_MEM[0]
	S += (t12*MAS[1])-1 < t14_mem0*MAS_MEM[2]
	S += (t12*MAS[2])-1 < t14_mem0*MAS_MEM[4]
	S += (t12*MAS[3])-1 < t14_mem0*MAS_MEM[6]
	S += (t12*MAS[4])-1 < t14_mem0*MAS_MEM[8]
	S += (t12*MAS[5])-1 < t14_mem0*MAS_MEM[10]
	S += (t12*MAS[6])-1 < t14_mem0*MAS_MEM[12]
	S += (t12*MAS[7])-1 < t14_mem0*MAS_MEM[14]
	S += t14_mem0 <= t14

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	t14_mem1 += MM_MEM[1]
	S += 12 < t14_mem1
	S += t14_mem1 <= t14

	new_PY = S.Task('new_PY', length=3, delay_cost=1)
	new_PY += alt(MAS)
	new_PY_in = S.Task('new_PY_in', length=1, delay_cost=1)
	new_PY_in += alt(MAS_in)
	S += new_PY_in*MAS_in[0]<=new_PY*MAS[0]

	S += new_PY_in*MAS_in[1]<=new_PY*MAS[1]

	S += new_PY_in*MAS_in[2]<=new_PY*MAS[2]

	S += new_PY_in*MAS_in[3]<=new_PY*MAS[3]

	S += new_PY_in*MAS_in[4]<=new_PY*MAS[4]

	S += new_PY_in*MAS_in[5]<=new_PY*MAS[5]

	S += new_PY_in*MAS_in[6]<=new_PY*MAS[6]

	S += new_PY_in*MAS_in[7]<=new_PY*MAS[7]

	S += 3<new_PY

	new_PY_w = S.Task('new_PY_w', length=1, delay_cost=1)
	new_PY_w += alt(MAIN_MEM_w)
	S += new_PY <= new_PY_w

	S += new_PY<1000

	new_PY_mem0 = S.Task('new_PY_mem0', length=1, delay_cost=1)
	new_PY_mem0 += alt(MM_MEM)
	S += (t8*MM[0])-1 < new_PY_mem0*MM_MEM[0]
	S += (t8*MM[1])-1 < new_PY_mem0*MM_MEM[2]
	S += new_PY_mem0 <= new_PY

	new_PY_mem1 = S.Task('new_PY_mem1', length=1, delay_cost=1)
	new_PY_mem1 += alt(MM_MEM)
	S += (t13*MM[0])-1 < new_PY_mem1*MM_MEM[1]
	S += (t13*MM[1])-1 < new_PY_mem1*MM_MEM[3]
	S += new_PY_mem1 <= new_PY

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage3MAS8/EP_DBL_A_0/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

