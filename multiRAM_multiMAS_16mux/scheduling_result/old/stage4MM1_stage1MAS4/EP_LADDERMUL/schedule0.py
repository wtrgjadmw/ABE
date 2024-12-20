from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	T1_in = S.Task('T1_in', length=1, delay_cost=1)
	T1_in += alt(MM_in)
	T1 = S.Task('T1', length=4, delay_cost=1)
	T1 += alt(MM)
	S += T1>=T1_in

	T1_mem0 = S.Task('T1_mem0', length=1, delay_cost=1)
	T1_mem0 += MAIN_MEM_r[0]
	T2_in = S.Task('T2_in', length=1, delay_cost=1)
	T2_in += alt(MM_in)
	T2 = S.Task('T2', length=4, delay_cost=1)
	T2 += alt(MM)
	S += T2>=T2_in

	T2_mem0 = S.Task('T2_mem0', length=1, delay_cost=1)
	T2_mem0 += MAIN_MEM_r[0]
	T2_mem1 = S.Task('T2_mem1', length=1, delay_cost=1)
	T2_mem1 += MAIN_MEM_r[1]
	T3_in = S.Task('T3_in', length=1, delay_cost=1)
	T3_in += alt(MM_in)
	T3 = S.Task('T3', length=4, delay_cost=1)
	T3 += alt(MM)
	S += T3>=T3_in

	T3_mem0 = S.Task('T3_mem0', length=1, delay_cost=1)
	T3_mem0 += MAIN_MEM_r[0]
	T3_mem1 = S.Task('T3_mem1', length=1, delay_cost=1)
	T3_mem1 += MAIN_MEM_r[1]
	T4_in = S.Task('T4_in', length=1, delay_cost=1)
	T4_in += alt(MM_in)
	T4 = S.Task('T4', length=4, delay_cost=1)
	T4 += alt(MM)
	S += T4>=T4_in

	T4_mem0 = S.Task('T4_mem0', length=1, delay_cost=1)
	T4_mem0 += MAIN_MEM_r[0]
	T4_mem1 = S.Task('T4_mem1', length=1, delay_cost=1)
	T4_mem1 += MAIN_MEM_r[1]
	T5_in = S.Task('T5_in', length=1, delay_cost=1)
	T5_in += alt(MM_in)
	T5 = S.Task('T5', length=4, delay_cost=1)
	T5 += alt(MM)
	S += T5>=T5_in

	T5_mem0 = S.Task('T5_mem0', length=1, delay_cost=1)
	T5_mem0 += MAIN_MEM_r[0]
	T6_in = S.Task('T6_in', length=1, delay_cost=1)
	T6_in += alt(MM_in)
	T6 = S.Task('T6', length=4, delay_cost=1)
	T6 += alt(MM)
	S += T6>=T6_in

	T6_mem0 = S.Task('T6_mem0', length=1, delay_cost=1)
	T6_mem0 += MAIN_MEM_r[0]
	T6_mem1 = S.Task('T6_mem1', length=1, delay_cost=1)
	T6_mem1 += MAIN_MEM_r[1]
	T7_in = S.Task('T7_in', length=1, delay_cost=1)
	T7_in += alt(MM_in)
	T7 = S.Task('T7', length=4, delay_cost=1)
	T7 += alt(MM)
	S += T7>=T7_in

	T7_mem0 = S.Task('T7_mem0', length=1, delay_cost=1)
	T7_mem0 += MAIN_MEM_r[0]
	T7_mem1 = S.Task('T7_mem1', length=1, delay_cost=1)
	T7_mem1 += MAIN_MEM_r[1]
	T8_in = S.Task('T8_in', length=1, delay_cost=1)
	T8_in += alt(MM_in)
	T8 = S.Task('T8', length=4, delay_cost=1)
	T8 += alt(MM)
	S += T8>=T8_in

	T8_mem0 = S.Task('T8_mem0', length=1, delay_cost=1)
	T8_mem0 += MAIN_MEM_r[0]
	T8_mem1 = S.Task('T8_mem1', length=1, delay_cost=1)
	T8_mem1 += alt(MM_MEM)
	S += (T1*MM[0])-1 < T8_mem1*MM_MEM[1]
	S += T8_mem1 <= T8

	T9_in = S.Task('T9_in', length=1, delay_cost=1)
	T9_in += alt(MM_in)
	T9 = S.Task('T9', length=4, delay_cost=1)
	T9 += alt(MM)
	S += T9>=T9_in

	T9_mem0 = S.Task('T9_mem0', length=1, delay_cost=1)
	T9_mem0 += MAIN_MEM_r[0]
	T9_mem1 = S.Task('T9_mem1', length=1, delay_cost=1)
	T9_mem1 += alt(MM_MEM)
	S += (T1*MM[0])-1 < T9_mem1*MM_MEM[1]
	S += T9_mem1 <= T9

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	T10_in += alt(MM_in)
	T10 = S.Task('T10', length=4, delay_cost=1)
	T10 += alt(MM)
	S += T10>=T10_in

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += MAIN_MEM_r[0]
	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += alt(MM_MEM)
	S += (T3*MM[0])-1 < T10_mem1*MM_MEM[1]
	S += T10_mem1 <= T10

	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	T11_in += alt(MM_in)
	T11 = S.Task('T11', length=4, delay_cost=1)
	T11 += alt(MM)
	S += T11>=T11_in

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += MAIN_MEM_r[0]
	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	T11_mem1 += alt(MM_MEM)
	S += (T3*MM[0])-1 < T11_mem1*MM_MEM[1]
	S += T11_mem1 <= T11

	T12 = S.Task('T12', length=1, delay_cost=1)
	T12 += alt(MAS)

	T12_mem0 = S.Task('T12_mem0', length=1, delay_cost=1)
	T12_mem0 += alt(MM_MEM)
	S += (T4*MM[0])-1 < T12_mem0*MM_MEM[0]
	S += T12_mem0 <= T12

	T12_mem1 = S.Task('T12_mem1', length=1, delay_cost=1)
	T12_mem1 += alt(MM_MEM)
	S += (T2*MM[0])-1 < T12_mem1*MM_MEM[1]
	S += T12_mem1 <= T12

	T13 = S.Task('T13', length=1, delay_cost=1)
	T13 += alt(MAS)

	T13_mem0 = S.Task('T13_mem0', length=1, delay_cost=1)
	T13_mem0 += alt(MM_MEM)
	S += (T4*MM[0])-1 < T13_mem0*MM_MEM[0]
	S += T13_mem0 <= T13

	T13_mem1 = S.Task('T13_mem1', length=1, delay_cost=1)
	T13_mem1 += alt(MM_MEM)
	S += (T2*MM[0])-1 < T13_mem1*MM_MEM[1]
	S += T13_mem1 <= T13

	T15 = S.Task('T15', length=1, delay_cost=1)
	T15 += alt(MAS)

	T15_mem0 = S.Task('T15_mem0', length=1, delay_cost=1)
	T15_mem0 += alt(MM_MEM)
	S += (T7*MM[0])-1 < T15_mem0*MM_MEM[0]
	S += T15_mem0 <= T15

	T14_in = S.Task('T14_in', length=1, delay_cost=1)
	T14_in += alt(MM_in)
	T14 = S.Task('T14', length=4, delay_cost=1)
	T14 += alt(MM)
	S += T14>=T14_in

	T14_mem0 = S.Task('T14_mem0', length=1, delay_cost=1)
	T14_mem0 += alt(MAS_MEM)
	S += (T13*MAS[0])-1 < T14_mem0*MAS_MEM[0]
	S += (T13*MAS[1])-1 < T14_mem0*MAS_MEM[2]
	S += (T13*MAS[2])-1 < T14_mem0*MAS_MEM[4]
	S += (T13*MAS[3])-1 < T14_mem0*MAS_MEM[6]
	S += T14_mem0 <= T14

	T16_in = S.Task('T16_in', length=1, delay_cost=1)
	T16_in += alt(MM_in)
	T16 = S.Task('T16', length=4, delay_cost=1)
	T16 += alt(MM)
	S += T16>=T16_in

	T16_mem0 = S.Task('T16_mem0', length=1, delay_cost=1)
	T16_mem0 += alt(MM_MEM)
	S += (T1*MM[0])-1 < T16_mem0*MM_MEM[0]
	S += T16_mem0 <= T16

	T16_mem1 = S.Task('T16_mem1', length=1, delay_cost=1)
	T16_mem1 += alt(MM_MEM)
	S += (T8*MM[0])-1 < T16_mem1*MM_MEM[1]
	S += T16_mem1 <= T16

	T17_in = S.Task('T17_in', length=1, delay_cost=1)
	T17_in += alt(MM_in)
	T17 = S.Task('T17', length=4, delay_cost=1)
	T17 += alt(MM)
	S += T17>=T17_in

	T17_mem0 = S.Task('T17_mem0', length=1, delay_cost=1)
	T17_mem0 += alt(MM_MEM)
	S += (T8*MM[0])-1 < T17_mem0*MM_MEM[0]
	S += T17_mem0 <= T17

	T17_mem1 = S.Task('T17_mem1', length=1, delay_cost=1)
	T17_mem1 += alt(MAS_MEM)
	S += (T15*MAS[0])-1 < T17_mem1*MAS_MEM[1]
	S += (T15*MAS[1])-1 < T17_mem1*MAS_MEM[3]
	S += (T15*MAS[2])-1 < T17_mem1*MAS_MEM[5]
	S += (T15*MAS[3])-1 < T17_mem1*MAS_MEM[7]
	S += T17_mem1 <= T17

	T18 = S.Task('T18', length=1, delay_cost=1)
	T18 += alt(MAS)

	T18_mem0 = S.Task('T18_mem0', length=1, delay_cost=1)
	T18_mem0 += alt(MM_MEM)
	S += (T5*MM[0])-1 < T18_mem0*MM_MEM[0]
	S += T18_mem0 <= T18

	T18_mem1 = S.Task('T18_mem1', length=1, delay_cost=1)
	T18_mem1 += alt(MM_MEM)
	S += (T9*MM[0])-1 < T18_mem1*MM_MEM[1]
	S += T18_mem1 <= T18

	T19 = S.Task('T19', length=1, delay_cost=1)
	T19 += alt(MAS)

	T19_mem0 = S.Task('T19_mem0', length=1, delay_cost=1)
	T19_mem0 += alt(MM_MEM)
	S += (T5*MM[0])-1 < T19_mem0*MM_MEM[0]
	S += T19_mem0 <= T19

	T19_mem1 = S.Task('T19_mem1', length=1, delay_cost=1)
	T19_mem1 += alt(MM_MEM)
	S += (T9*MM[0])-1 < T19_mem1*MM_MEM[1]
	S += T19_mem1 <= T19

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(MAS)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += alt(MM_MEM)
	S += (T6*MM[0])-1 < T21_mem0*MM_MEM[0]
	S += T21_mem0 <= T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += alt(MM_MEM)
	S += (T10*MM[0])-1 < T21_mem1*MM_MEM[1]
	S += T21_mem1 <= T21

	T24_in = S.Task('T24_in', length=1, delay_cost=1)
	T24_in += alt(MM_in)
	T24 = S.Task('T24', length=4, delay_cost=1)
	T24 += alt(MM)
	S += T24>=T24_in

	T24_mem0 = S.Task('T24_mem0', length=1, delay_cost=1)
	T24_mem0 += alt(MM_MEM)
	S += (T11*MM[0])-1 < T24_mem0*MM_MEM[0]
	S += T24_mem0 <= T24

	T24_mem1 = S.Task('T24_mem1', length=1, delay_cost=1)
	T24_mem1 += alt(MAS_MEM)
	S += (T12*MAS[0])-1 < T24_mem1*MAS_MEM[1]
	S += (T12*MAS[1])-1 < T24_mem1*MAS_MEM[3]
	S += (T12*MAS[2])-1 < T24_mem1*MAS_MEM[5]
	S += (T12*MAS[3])-1 < T24_mem1*MAS_MEM[7]
	S += T24_mem1 <= T24

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	T20_in += alt(MM_in)
	T20 = S.Task('T20', length=4, delay_cost=1)
	T20 += alt(MM)
	S += T20>=T20_in

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += alt(MAS_MEM)
	S += (T15*MAS[0])-1 < T20_mem0*MAS_MEM[0]
	S += (T15*MAS[1])-1 < T20_mem0*MAS_MEM[2]
	S += (T15*MAS[2])-1 < T20_mem0*MAS_MEM[4]
	S += (T15*MAS[3])-1 < T20_mem0*MAS_MEM[6]
	S += T20_mem0 <= T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += alt(MAS_MEM)
	S += (T18*MAS[0])-1 < T20_mem1*MAS_MEM[1]
	S += (T18*MAS[1])-1 < T20_mem1*MAS_MEM[3]
	S += (T18*MAS[2])-1 < T20_mem1*MAS_MEM[5]
	S += (T18*MAS[3])-1 < T20_mem1*MAS_MEM[7]
	S += T20_mem1 <= T20

	T22_in = S.Task('T22_in', length=1, delay_cost=1)
	T22_in += alt(MM_in)
	T22 = S.Task('T22', length=4, delay_cost=1)
	T22 += alt(MM)
	S += T22>=T22_in

	T22_mem0 = S.Task('T22_mem0', length=1, delay_cost=1)
	T22_mem0 += alt(MAS_MEM)
	S += (T21*MAS[0])-1 < T22_mem0*MAS_MEM[0]
	S += (T21*MAS[1])-1 < T22_mem0*MAS_MEM[2]
	S += (T21*MAS[2])-1 < T22_mem0*MAS_MEM[4]
	S += (T21*MAS[3])-1 < T22_mem0*MAS_MEM[6]
	S += T22_mem0 <= T22

	T23_in = S.Task('T23_in', length=1, delay_cost=1)
	T23_in += alt(MM_in)
	T23 = S.Task('T23', length=4, delay_cost=1)
	T23 += alt(MM)
	S += T23>=T23_in

	T23_mem0 = S.Task('T23_mem0', length=1, delay_cost=1)
	T23_mem0 += alt(MAS_MEM)
	S += (T19*MAS[0])-1 < T23_mem0*MAS_MEM[0]
	S += (T19*MAS[1])-1 < T23_mem0*MAS_MEM[2]
	S += (T19*MAS[2])-1 < T23_mem0*MAS_MEM[4]
	S += (T19*MAS[3])-1 < T23_mem0*MAS_MEM[6]
	S += T23_mem0 <= T23

	Z2_new_in = S.Task('Z2_new_in', length=1, delay_cost=1)
	Z2_new_in += alt(MM_in)
	Z2_new = S.Task('Z2_new', length=4, delay_cost=1)
	Z2_new += alt(MM)
	S += Z2_new>=Z2_new_in

	S += 0<Z2_new

	Z2_new_w = S.Task('Z2_new_w', length=1, delay_cost=1)
	Z2_new_w += alt(MAIN_MEM_w)
	S += Z2_new <= Z2_new_w

	Z2_new_mem0 = S.Task('Z2_new_mem0', length=1, delay_cost=1)
	Z2_new_mem0 += MAIN_MEM_r[0]
	Z2_new_mem1 = S.Task('Z2_new_mem1', length=1, delay_cost=1)
	Z2_new_mem1 += alt(MM_MEM)
	S += (T14*MM[0])-1 < Z2_new_mem1*MM_MEM[1]
	S += Z2_new_mem1 <= Z2_new

	T25 = S.Task('T25', length=1, delay_cost=1)
	T25 += alt(MAS)

	T25_mem0 = S.Task('T25_mem0', length=1, delay_cost=1)
	T25_mem0 += alt(MM_MEM)
	S += (T20*MM[0])-1 < T25_mem0*MM_MEM[0]
	S += T25_mem0 <= T25

	X2_new = S.Task('X2_new', length=1, delay_cost=1)
	X2_new += alt(MAS)

	S += 0<X2_new

	X2_new_w = S.Task('X2_new_w', length=1, delay_cost=1)
	X2_new_w += alt(MAIN_MEM_w)
	S += X2_new <= X2_new_w

	X2_new_mem0 = S.Task('X2_new_mem0', length=1, delay_cost=1)
	X2_new_mem0 += alt(MM_MEM)
	S += (T22*MM[0])-1 < X2_new_mem0*MM_MEM[0]
	S += X2_new_mem0 <= X2_new

	X2_new_mem1 = S.Task('X2_new_mem1', length=1, delay_cost=1)
	X2_new_mem1 += alt(MM_MEM)
	S += (T24*MM[0])-1 < X2_new_mem1*MM_MEM[1]
	S += X2_new_mem1 <= X2_new

	X1_new = S.Task('X1_new', length=1, delay_cost=1)
	X1_new += alt(MAS)

	S += 0<X1_new

	X1_new_w = S.Task('X1_new_w', length=1, delay_cost=1)
	X1_new_w += alt(MAIN_MEM_w)
	S += X1_new <= X1_new_w

	X1_new_mem0 = S.Task('X1_new_mem0', length=1, delay_cost=1)
	X1_new_mem0 += alt(MM_MEM)
	S += (T23*MM[0])-1 < X1_new_mem0*MM_MEM[0]
	S += X1_new_mem0 <= X1_new

	X1_new_mem1 = S.Task('X1_new_mem1', length=1, delay_cost=1)
	X1_new_mem1 += alt(MM_MEM)
	S += (T17*MM[0])-1 < X1_new_mem1*MM_MEM[1]
	S += X1_new_mem1 <= X1_new

	Z1_new = S.Task('Z1_new', length=1, delay_cost=1)
	Z1_new += alt(MAS)

	S += 0<Z1_new

	Z1_new_w = S.Task('Z1_new_w', length=1, delay_cost=1)
	Z1_new_w += alt(MAIN_MEM_w)
	S += Z1_new <= Z1_new_w

	Z1_new_mem0 = S.Task('Z1_new_mem0', length=1, delay_cost=1)
	Z1_new_mem0 += alt(MM_MEM)
	S += (T16*MM[0])-1 < Z1_new_mem0*MM_MEM[0]
	S += Z1_new_mem0 <= Z1_new

	Z1_new_mem1 = S.Task('Z1_new_mem1', length=1, delay_cost=1)
	Z1_new_mem1 += alt(MAS_MEM)
	S += (T25*MAS[0])-1 < Z1_new_mem1*MAS_MEM[1]
	S += (T25*MAS[1])-1 < Z1_new_mem1*MAS_MEM[3]
	S += (T25*MAS[2])-1 < Z1_new_mem1*MAS_MEM[5]
	S += (T25*MAS[3])-1 < Z1_new_mem1*MAS_MEM[7]
	S += Z1_new_mem1 <= Z1_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage1MAS4/ladderMul/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

