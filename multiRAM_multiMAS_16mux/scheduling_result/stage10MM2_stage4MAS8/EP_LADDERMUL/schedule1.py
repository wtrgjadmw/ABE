from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 165
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=8)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	T1_in = S.Task('T1_in', length=1, delay_cost=1)
	S += T1_in >= 0
	T1_in += MM_in[1]

	T1_mem0 = S.Task('T1_mem0', length=1, delay_cost=1)
	S += T1_mem0 >= 0
	T1_mem0 += MAIN_MEM_r[0]

	T1_mem1 = S.Task('T1_mem1', length=1, delay_cost=1)
	S += T1_mem1 >= 0
	T1_mem1 += MAIN_MEM_r[1]

	T1 = S.Task('T1', length=10, delay_cost=1)
	S += T1 >= 1
	T1 += MM[1]

	T3_in = S.Task('T3_in', length=1, delay_cost=1)
	S += T3_in >= 1
	T3_in += MM_in[1]

	T3_mem0 = S.Task('T3_mem0', length=1, delay_cost=1)
	S += T3_mem0 >= 1
	T3_mem0 += MAIN_MEM_r[0]

	T3_mem1 = S.Task('T3_mem1', length=1, delay_cost=1)
	S += T3_mem1 >= 1
	T3_mem1 += MAIN_MEM_r[1]

	T3 = S.Task('T3', length=10, delay_cost=1)
	S += T3 >= 2
	T3 += MM[1]

	T4_in = S.Task('T4_in', length=1, delay_cost=1)
	S += T4_in >= 2
	T4_in += MM_in[0]

	T4_mem0 = S.Task('T4_mem0', length=1, delay_cost=1)
	S += T4_mem0 >= 2
	T4_mem0 += MAIN_MEM_r[0]

	T4_mem1 = S.Task('T4_mem1', length=1, delay_cost=1)
	S += T4_mem1 >= 2
	T4_mem1 += MAIN_MEM_r[1]

	T2_in = S.Task('T2_in', length=1, delay_cost=1)
	S += T2_in >= 3
	T2_in += MM_in[0]

	T2_mem0 = S.Task('T2_mem0', length=1, delay_cost=1)
	S += T2_mem0 >= 3
	T2_mem0 += MAIN_MEM_r[0]

	T2_mem1 = S.Task('T2_mem1', length=1, delay_cost=1)
	S += T2_mem1 >= 3
	T2_mem1 += MAIN_MEM_r[1]

	T4 = S.Task('T4', length=10, delay_cost=1)
	S += T4 >= 3
	T4 += MM[0]

	T2 = S.Task('T2', length=10, delay_cost=1)
	S += T2 >= 4
	T2 += MM[0]

	T7_in = S.Task('T7_in', length=1, delay_cost=1)
	S += T7_in >= 4
	T7_in += MM_in[1]

	T7_mem0 = S.Task('T7_mem0', length=1, delay_cost=1)
	S += T7_mem0 >= 4
	T7_mem0 += MAIN_MEM_r[0]

	T7_mem1 = S.Task('T7_mem1', length=1, delay_cost=1)
	S += T7_mem1 >= 4
	T7_mem1 += MAIN_MEM_r[1]

	T6_in = S.Task('T6_in', length=1, delay_cost=1)
	S += T6_in >= 5
	T6_in += MM_in[1]

	T6_mem0 = S.Task('T6_mem0', length=1, delay_cost=1)
	S += T6_mem0 >= 5
	T6_mem0 += MAIN_MEM_r[0]

	T6_mem1 = S.Task('T6_mem1', length=1, delay_cost=1)
	S += T6_mem1 >= 5
	T6_mem1 += MAIN_MEM_r[1]

	T7 = S.Task('T7', length=10, delay_cost=1)
	S += T7 >= 5
	T7 += MM[1]

	T5_in = S.Task('T5_in', length=1, delay_cost=1)
	S += T5_in >= 6
	T5_in += MM_in[0]

	T5_mem0 = S.Task('T5_mem0', length=1, delay_cost=1)
	S += T5_mem0 >= 6
	T5_mem0 += MAIN_MEM_r[0]

	T5_mem1 = S.Task('T5_mem1', length=1, delay_cost=1)
	S += T5_mem1 >= 6
	T5_mem1 += MAIN_MEM_r[1]

	T6 = S.Task('T6', length=10, delay_cost=1)
	S += T6 >= 6
	T6 += MM[1]

	T5 = S.Task('T5', length=10, delay_cost=1)
	S += T5 >= 7
	T5 += MM[0]

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	S += T10_in >= 11
	T10_in += MM_in[1]

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	S += T10_mem0 >= 11
	T10_mem0 += MAIN_MEM_r[0]

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	S += T10_mem1 >= 11
	T10_mem1 += MM_MEM[3]

	T10 = S.Task('T10', length=10, delay_cost=1)
	S += T10 >= 12
	T10 += MM[1]

	T8_in = S.Task('T8_in', length=1, delay_cost=1)
	S += T8_in >= 12
	T8_in += MM_in[0]

	T8_mem0 = S.Task('T8_mem0', length=1, delay_cost=1)
	S += T8_mem0 >= 12
	T8_mem0 += MAIN_MEM_r[0]

	T8_mem1 = S.Task('T8_mem1', length=1, delay_cost=1)
	S += T8_mem1 >= 12
	T8_mem1 += MM_MEM[3]

	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	S += T11_in >= 13
	T11_in += MM_in[0]

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	S += T11_mem0 >= 13
	T11_mem0 += MAIN_MEM_r[0]

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	S += T11_mem1 >= 13
	T11_mem1 += MM_MEM[3]

	T13_in = S.Task('T13_in', length=1, delay_cost=1)
	S += T13_in >= 13
	T13_in += MAS_in[6]

	T13_mem0 = S.Task('T13_mem0', length=1, delay_cost=1)
	S += T13_mem0 >= 13
	T13_mem0 += MM_MEM[0]

	T13_mem1 = S.Task('T13_mem1', length=1, delay_cost=1)
	S += T13_mem1 >= 13
	T13_mem1 += MM_MEM[1]

	T8 = S.Task('T8', length=10, delay_cost=1)
	S += T8 >= 13
	T8 += MM[0]

	T11 = S.Task('T11', length=10, delay_cost=1)
	S += T11 >= 14
	T11 += MM[0]

	T12_in = S.Task('T12_in', length=1, delay_cost=1)
	S += T12_in >= 14
	T12_in += MAS_in[3]

	T12_mem0 = S.Task('T12_mem0', length=1, delay_cost=1)
	S += T12_mem0 >= 14
	T12_mem0 += MM_MEM[0]

	T12_mem1 = S.Task('T12_mem1', length=1, delay_cost=1)
	S += T12_mem1 >= 14
	T12_mem1 += MM_MEM[1]

	T13 = S.Task('T13', length=4, delay_cost=1)
	S += T13 >= 14
	T13 += MAS[6]

	T15_in = S.Task('T15_in', length=1, delay_cost=1)
	S += T15_in >= 14
	T15_in += MAS_in[4]

	T15_mem0 = S.Task('T15_mem0', length=1, delay_cost=1)
	S += T15_mem0 >= 14
	T15_mem0 += MM_MEM[2]

	T15_mem1 = S.Task('T15_mem1', length=1, delay_cost=1)
	S += T15_mem1 >= 14
	T15_mem1 += MM_MEM[3]

	T12 = S.Task('T12', length=4, delay_cost=1)
	S += T12 >= 15
	T12 += MAS[3]

	T15 = S.Task('T15', length=4, delay_cost=1)
	S += T15 >= 15
	T15 += MAS[4]

	T14_in = S.Task('T14_in', length=1, delay_cost=1)
	S += T14_in >= 17
	T14_in += MM_in[0]

	T14_mem0 = S.Task('T14_mem0', length=1, delay_cost=1)
	S += T14_mem0 >= 17
	T14_mem0 += MAS_MEM[12]

	T14_mem1 = S.Task('T14_mem1', length=1, delay_cost=1)
	S += T14_mem1 >= 17
	T14_mem1 += MAS_MEM[13]

	T14 = S.Task('T14', length=10, delay_cost=1)
	S += T14 >= 18
	T14 += MM[0]

	T19_in = S.Task('T19_in', length=1, delay_cost=1)
	S += T19_in >= 20
	T19_in += MAS_in[0]

	T19_mem0 = S.Task('T19_mem0', length=1, delay_cost=1)
	S += T19_mem0 >= 20
	T19_mem0 += MM_MEM[0]

	T19_mem1 = S.Task('T19_mem1', length=1, delay_cost=1)
	S += T19_mem1 >= 20
	T19_mem1 += MM_MEM[1]

	T18_in = S.Task('T18_in', length=1, delay_cost=1)
	S += T18_in >= 21
	T18_in += MAS_in[5]

	T18_mem0 = S.Task('T18_mem0', length=1, delay_cost=1)
	S += T18_mem0 >= 21
	T18_mem0 += MM_MEM[0]

	T18_mem1 = S.Task('T18_mem1', length=1, delay_cost=1)
	S += T18_mem1 >= 21
	T18_mem1 += MM_MEM[1]

	T19 = S.Task('T19', length=4, delay_cost=1)
	S += T19 >= 21
	T19 += MAS[0]

	T21_in = S.Task('T21_in', length=1, delay_cost=1)
	S += T21_in >= 21
	T21_in += MAS_in[0]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	S += T21_mem0 >= 21
	T21_mem0 += MM_MEM[2]

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	S += T21_mem1 >= 21
	T21_mem1 += MM_MEM[3]

	T16_in = S.Task('T16_in', length=1, delay_cost=1)
	S += T16_in >= 22
	T16_in += MM_in[1]

	T16_mem0 = S.Task('T16_mem0', length=1, delay_cost=1)
	S += T16_mem0 >= 22
	T16_mem0 += MM_MEM[2]

	T16_mem1 = S.Task('T16_mem1', length=1, delay_cost=1)
	S += T16_mem1 >= 22
	T16_mem1 += MM_MEM[1]

	T17_in = S.Task('T17_in', length=1, delay_cost=1)
	S += T17_in >= 22
	T17_in += MM_in[0]

	T17_mem0 = S.Task('T17_mem0', length=1, delay_cost=1)
	S += T17_mem0 >= 22
	T17_mem0 += MM_MEM[0]

	T17_mem1 = S.Task('T17_mem1', length=1, delay_cost=1)
	S += T17_mem1 >= 22
	T17_mem1 += MAS_MEM[9]

	T18 = S.Task('T18', length=4, delay_cost=1)
	S += T18 >= 22
	T18 += MAS[5]

	T21 = S.Task('T21', length=4, delay_cost=1)
	S += T21 >= 22
	T21 += MAS[0]

	T16 = S.Task('T16', length=10, delay_cost=1)
	S += T16 >= 23
	T16 += MM[1]

	T17 = S.Task('T17', length=10, delay_cost=1)
	S += T17 >= 23
	T17 += MM[0]

	T24_in = S.Task('T24_in', length=1, delay_cost=1)
	S += T24_in >= 23
	T24_in += MM_in[1]

	T24_mem0 = S.Task('T24_mem0', length=1, delay_cost=1)
	S += T24_mem0 >= 23
	T24_mem0 += MM_MEM[0]

	T24_mem1 = S.Task('T24_mem1', length=1, delay_cost=1)
	S += T24_mem1 >= 23
	T24_mem1 += MAS_MEM[7]

	T23_in = S.Task('T23_in', length=1, delay_cost=1)
	S += T23_in >= 24
	T23_in += MM_in[1]

	T23_mem0 = S.Task('T23_mem0', length=1, delay_cost=1)
	S += T23_mem0 >= 24
	T23_mem0 += MAS_MEM[0]

	T23_mem1 = S.Task('T23_mem1', length=1, delay_cost=1)
	S += T23_mem1 >= 24
	T23_mem1 += MAS_MEM[1]

	T24 = S.Task('T24', length=10, delay_cost=1)
	S += T24 >= 24
	T24 += MM[1]

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	S += T20_in >= 25
	T20_in += MM_in[0]

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	S += T20_mem0 >= 25
	T20_mem0 += MAS_MEM[8]

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	S += T20_mem1 >= 25
	T20_mem1 += MAS_MEM[11]

	T22_in = S.Task('T22_in', length=1, delay_cost=1)
	S += T22_in >= 25
	T22_in += MM_in[1]

	T22_mem0 = S.Task('T22_mem0', length=1, delay_cost=1)
	S += T22_mem0 >= 25
	T22_mem0 += MAS_MEM[0]

	T22_mem1 = S.Task('T22_mem1', length=1, delay_cost=1)
	S += T22_mem1 >= 25
	T22_mem1 += MAS_MEM[1]

	T23 = S.Task('T23', length=10, delay_cost=1)
	S += T23 >= 25
	T23 += MM[1]

	T20 = S.Task('T20', length=10, delay_cost=1)
	S += T20 >= 26
	T20 += MM[0]

	T22 = S.Task('T22', length=10, delay_cost=1)
	S += T22 >= 26
	T22 += MM[1]

	Z2_new_in = S.Task('Z2_new_in', length=1, delay_cost=1)
	S += Z2_new_in >= 27
	Z2_new_in += MM_in[0]

	Z2_new_mem0 = S.Task('Z2_new_mem0', length=1, delay_cost=1)
	S += Z2_new_mem0 >= 27
	Z2_new_mem0 += MAIN_MEM_r[0]

	Z2_new_mem1 = S.Task('Z2_new_mem1', length=1, delay_cost=1)
	S += Z2_new_mem1 >= 27
	Z2_new_mem1 += MM_MEM[1]

	Z2_new = S.Task('Z2_new', length=10, delay_cost=1)
	S += Z2_new >= 28
	Z2_new += MM[0]

	X1_new_in = S.Task('X1_new_in', length=1, delay_cost=1)
	S += X1_new_in >= 34
	X1_new_in += MAS_in[2]

	X1_new_mem0 = S.Task('X1_new_mem0', length=1, delay_cost=1)
	S += X1_new_mem0 >= 34
	X1_new_mem0 += MM_MEM[2]

	X1_new_mem1 = S.Task('X1_new_mem1', length=1, delay_cost=1)
	S += X1_new_mem1 >= 34
	X1_new_mem1 += MM_MEM[1]

	T25_in = S.Task('T25_in', length=1, delay_cost=1)
	S += T25_in >= 35
	T25_in += MAS_in[4]

	T25_mem0 = S.Task('T25_mem0', length=1, delay_cost=1)
	S += T25_mem0 >= 35
	T25_mem0 += MM_MEM[0]

	T25_mem1 = S.Task('T25_mem1', length=1, delay_cost=1)
	S += T25_mem1 >= 35
	T25_mem1 += MM_MEM[1]

	X1_new = S.Task('X1_new', length=4, delay_cost=1)
	S += X1_new >= 35
	X1_new += MAS[2]

	X2_new_in = S.Task('X2_new_in', length=1, delay_cost=1)
	S += X2_new_in >= 35
	X2_new_in += MAS_in[2]

	X2_new_mem0 = S.Task('X2_new_mem0', length=1, delay_cost=1)
	S += X2_new_mem0 >= 35
	X2_new_mem0 += MM_MEM[2]

	X2_new_mem1 = S.Task('X2_new_mem1', length=1, delay_cost=1)
	S += X2_new_mem1 >= 35
	X2_new_mem1 += MM_MEM[3]

	T25 = S.Task('T25', length=4, delay_cost=1)
	S += T25 >= 36
	T25 += MAS[4]

	X2_new = S.Task('X2_new', length=4, delay_cost=1)
	S += X2_new >= 36
	X2_new += MAS[2]

	Z2_new_w = S.Task('Z2_new_w', length=1, delay_cost=1)
	S += Z2_new_w >= 38
	Z2_new_w += MAIN_MEM_w

	X1_new_w = S.Task('X1_new_w', length=1, delay_cost=1)
	S += X1_new_w >= 39
	X1_new_w += MAIN_MEM_w

	Z1_new_in = S.Task('Z1_new_in', length=1, delay_cost=1)
	S += Z1_new_in >= 39
	Z1_new_in += MAS_in[1]

	Z1_new_mem0 = S.Task('Z1_new_mem0', length=1, delay_cost=1)
	S += Z1_new_mem0 >= 39
	Z1_new_mem0 += MM_MEM[2]

	Z1_new_mem1 = S.Task('Z1_new_mem1', length=1, delay_cost=1)
	S += Z1_new_mem1 >= 39
	Z1_new_mem1 += MAS_MEM[9]

	X2_new_w = S.Task('X2_new_w', length=1, delay_cost=1)
	S += X2_new_w >= 40
	X2_new_w += MAIN_MEM_w

	Z1_new = S.Task('Z1_new', length=4, delay_cost=1)
	S += Z1_new >= 40
	Z1_new += MAS[1]

	Z1_new_w = S.Task('Z1_new_w', length=1, delay_cost=1)
	S += Z1_new_w >= 44
	Z1_new_w += MAIN_MEM_w


	# new tasks
	T9 = S.Task('T9', length=10, delay_cost=1)
	T9 += alt(MM)
	T9_in = S.Task('T9_in', length=1, delay_cost=1)
	T9_in += alt(MM_in)
	S += T9_in*MM_in[0]<=T9*MM[0]
	S += T9_in*MM_in[1]<=T9*MM[1]
	S += T9<21

	T9_mem0 = S.Task('T9_mem0', length=1, delay_cost=1)
	T9_mem0 += MAIN_MEM_r[0]
	S += T9_mem0 <= T9

	T9_mem1 = S.Task('T9_mem1', length=1, delay_cost=1)
	T9_mem1 += MM_MEM[3]
	S += 10 < T9_mem1
	S += T9_mem1 <= T9

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage4MAS8/EP_LADDERMUL/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

