from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MUL = S.Resources('MUL', num=1, size=5)
	MUL_in = S.Resources('MUL_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=1, periods=range(1, horizon))
	INPUT_mem_w = S.Resource('INPUT_mem_w', size=2)
	INPUT_mem_r = S.Resource('INPUT_mem_r', size=4)

	# result of previous scheduling

	# new tasks
	T1_in = S.Task('T1_in', length=1, delay_cost=1)
	T1_in += alt(MUL_in)
	T1 = S.Task('T1', length=5, delay_cost=1)
	T1 += alt(MUL)
	S += T1>=T1_in

	T1_mem0 = S.Task('T1_mem0', length=1, delay_cost=1)
	T1_mem0 += INPUT_mem_r
	S += T1_mem0-1 <= T1

	T2_in = S.Task('T2_in', length=1, delay_cost=1)
	T2_in += alt(MUL_in)
	T2 = S.Task('T2', length=5, delay_cost=1)
	T2 += alt(MUL)
	S += T2>=T2_in

	T2_mem0 = S.Task('T2_mem0', length=1, delay_cost=1)
	T2_mem0 += INPUT_mem_r
	S += T2_mem0-1 <= T2

	T2_mem1 = S.Task('T2_mem1', length=1, delay_cost=1)
	T2_mem1 += INPUT_mem_r
	S += T2_mem1-1 <= T2

	T3_in = S.Task('T3_in', length=1, delay_cost=1)
	T3_in += alt(MUL_in)
	T3 = S.Task('T3', length=5, delay_cost=1)
	T3 += alt(MUL)
	S += T3>=T3_in

	T3_mem0 = S.Task('T3_mem0', length=1, delay_cost=1)
	T3_mem0 += INPUT_mem_r
	S += T3_mem0-1 <= T3

	T3_mem1 = S.Task('T3_mem1', length=1, delay_cost=1)
	T3_mem1 += INPUT_mem_r
	S += T3_mem1-1 <= T3

	T4_in = S.Task('T4_in', length=1, delay_cost=1)
	T4_in += alt(MUL_in)
	T4 = S.Task('T4', length=5, delay_cost=1)
	T4 += alt(MUL)
	S += T4>=T4_in

	T4_mem0 = S.Task('T4_mem0', length=1, delay_cost=1)
	T4_mem0 += INPUT_mem_r
	S += T4_mem0-1 <= T4

	T4_mem1 = S.Task('T4_mem1', length=1, delay_cost=1)
	T4_mem1 += INPUT_mem_r
	S += T4_mem1-1 <= T4

	T5_in = S.Task('T5_in', length=1, delay_cost=1)
	T5_in += alt(MUL_in)
	T5 = S.Task('T5', length=5, delay_cost=1)
	T5 += alt(MUL)
	S += T5>=T5_in

	T5_mem0 = S.Task('T5_mem0', length=1, delay_cost=1)
	T5_mem0 += INPUT_mem_r
	S += T5_mem0-1 <= T5

	T6_in = S.Task('T6_in', length=1, delay_cost=1)
	T6_in += alt(MUL_in)
	T6 = S.Task('T6', length=5, delay_cost=1)
	T6 += alt(MUL)
	S += T6>=T6_in

	T6_mem0 = S.Task('T6_mem0', length=1, delay_cost=1)
	T6_mem0 += INPUT_mem_r
	S += T6_mem0-1 <= T6

	T6_mem1 = S.Task('T6_mem1', length=1, delay_cost=1)
	T6_mem1 += INPUT_mem_r
	S += T6_mem1-1 <= T6

	T7_in = S.Task('T7_in', length=1, delay_cost=1)
	T7_in += alt(MUL_in)
	T7 = S.Task('T7', length=5, delay_cost=1)
	T7 += alt(MUL)
	S += T7>=T7_in

	T7_mem0 = S.Task('T7_mem0', length=1, delay_cost=1)
	T7_mem0 += INPUT_mem_r
	S += T7_mem0-1 <= T7

	T7_mem1 = S.Task('T7_mem1', length=1, delay_cost=1)
	T7_mem1 += INPUT_mem_r
	S += T7_mem1-1 <= T7

	T8_in = S.Task('T8_in', length=1, delay_cost=1)
	T8_in += alt(MUL_in)
	T8 = S.Task('T8', length=5, delay_cost=1)
	T8 += alt(MUL)
	S += T8>=T8_in

	T8_mem0 = S.Task('T8_mem0', length=1, delay_cost=1)
	T8_mem0 += INPUT_mem_r
	S += T8_mem0-1 <= T8

	T8_mem1 = S.Task('T8_mem1', length=1, delay_cost=1)
	T8_mem1 += alt(INPUT_mem_r)
	S += T1 < T8_mem1
	S += T8_mem1-1 <= T8

	T9_in = S.Task('T9_in', length=1, delay_cost=1)
	T9_in += alt(MUL_in)
	T9 = S.Task('T9', length=5, delay_cost=1)
	T9 += alt(MUL)
	S += T9>=T9_in

	T9_mem0 = S.Task('T9_mem0', length=1, delay_cost=1)
	T9_mem0 += INPUT_mem_r
	S += T9_mem0-1 <= T9

	T9_mem1 = S.Task('T9_mem1', length=1, delay_cost=1)
	T9_mem1 += alt(INPUT_mem_r)
	S += T1 < T9_mem1
	S += T9_mem1-1 <= T9

	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	T10_in += alt(MUL_in)
	T10 = S.Task('T10', length=5, delay_cost=1)
	T10 += alt(MUL)
	S += T10>=T10_in

	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += INPUT_mem_r
	S += T10_mem0-1 <= T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += alt(INPUT_mem_r)
	S += T3 < T10_mem1
	S += T10_mem1-1 <= T10

	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	T11_in += alt(MUL_in)
	T11 = S.Task('T11', length=5, delay_cost=1)
	T11 += alt(MUL)
	S += T11>=T11_in

	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += INPUT_mem_r
	S += T11_mem0-1 <= T11

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	T11_mem1 += alt(INPUT_mem_r)
	S += T3 < T11_mem1
	S += T11_mem1-1 <= T11

	T12 = S.Task('T12', length=1, delay_cost=1)
	T12 += alt(MAS)

	T12_mem0 = S.Task('T12_mem0', length=1, delay_cost=1)
	T12_mem0 += alt(INPUT_mem_r)
	S += T4 < T12_mem0
	S += T12_mem0-1 <= T12

	T12_mem1 = S.Task('T12_mem1', length=1, delay_cost=1)
	T12_mem1 += alt(INPUT_mem_r)
	S += T2 < T12_mem1
	S += T12_mem1-1 <= T12

	T13 = S.Task('T13', length=1, delay_cost=1)
	T13 += alt(MAS)

	T13_mem0 = S.Task('T13_mem0', length=1, delay_cost=1)
	T13_mem0 += alt(INPUT_mem_r)
	S += T4 < T13_mem0
	S += T13_mem0-1 <= T13

	T13_mem1 = S.Task('T13_mem1', length=1, delay_cost=1)
	T13_mem1 += alt(INPUT_mem_r)
	S += T2 < T13_mem1
	S += T13_mem1-1 <= T13

	T15 = S.Task('T15', length=1, delay_cost=1)
	T15 += alt(MAS)

	T15_mem0 = S.Task('T15_mem0', length=1, delay_cost=1)
	T15_mem0 += alt(INPUT_mem_r)
	S += T7 < T15_mem0
	S += T15_mem0-1 <= T15

	T14_in = S.Task('T14_in', length=1, delay_cost=1)
	T14_in += alt(MUL_in)
	T14 = S.Task('T14', length=5, delay_cost=1)
	T14 += alt(MUL)
	S += T14>=T14_in

	T14_mem0 = S.Task('T14_mem0', length=1, delay_cost=1)
	T14_mem0 += alt(INPUT_mem_r)
	S += T13 < T14_mem0
	S += T14_mem0-1 <= T14

	T16_in = S.Task('T16_in', length=1, delay_cost=1)
	T16_in += alt(MUL_in)
	T16 = S.Task('T16', length=5, delay_cost=1)
	T16 += alt(MUL)
	S += T16>=T16_in

	T16_mem0 = S.Task('T16_mem0', length=1, delay_cost=1)
	T16_mem0 += alt(INPUT_mem_r)
	S += T1 < T16_mem0
	S += T16_mem0-1 <= T16

	T16_mem1 = S.Task('T16_mem1', length=1, delay_cost=1)
	T16_mem1 += alt(INPUT_mem_r)
	S += T8 < T16_mem1
	S += T16_mem1-1 <= T16

	T17_in = S.Task('T17_in', length=1, delay_cost=1)
	T17_in += alt(MUL_in)
	T17 = S.Task('T17', length=5, delay_cost=1)
	T17 += alt(MUL)
	S += T17>=T17_in

	T17_mem0 = S.Task('T17_mem0', length=1, delay_cost=1)
	T17_mem0 += alt(INPUT_mem_r)
	S += T8 < T17_mem0
	S += T17_mem0-1 <= T17

	T17_mem1 = S.Task('T17_mem1', length=1, delay_cost=1)
	T17_mem1 += alt(INPUT_mem_r)
	S += T15 < T17_mem1
	S += T17_mem1-1 <= T17

	T18 = S.Task('T18', length=1, delay_cost=1)
	T18 += alt(MAS)

	T18_mem0 = S.Task('T18_mem0', length=1, delay_cost=1)
	T18_mem0 += alt(INPUT_mem_r)
	S += T5 < T18_mem0
	S += T18_mem0-1 <= T18

	T18_mem1 = S.Task('T18_mem1', length=1, delay_cost=1)
	T18_mem1 += alt(INPUT_mem_r)
	S += T9 < T18_mem1
	S += T18_mem1-1 <= T18

	T19 = S.Task('T19', length=1, delay_cost=1)
	T19 += alt(MAS)

	T19_mem0 = S.Task('T19_mem0', length=1, delay_cost=1)
	T19_mem0 += alt(INPUT_mem_r)
	S += T5 < T19_mem0
	S += T19_mem0-1 <= T19

	T19_mem1 = S.Task('T19_mem1', length=1, delay_cost=1)
	T19_mem1 += alt(INPUT_mem_r)
	S += T9 < T19_mem1
	S += T19_mem1-1 <= T19

	T21 = S.Task('T21', length=1, delay_cost=1)
	T21 += alt(MAS)

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += alt(INPUT_mem_r)
	S += T6 < T21_mem0
	S += T21_mem0-1 <= T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += alt(INPUT_mem_r)
	S += T10 < T21_mem1
	S += T21_mem1-1 <= T21

	T24_in = S.Task('T24_in', length=1, delay_cost=1)
	T24_in += alt(MUL_in)
	T24 = S.Task('T24', length=5, delay_cost=1)
	T24 += alt(MUL)
	S += T24>=T24_in

	T24_mem0 = S.Task('T24_mem0', length=1, delay_cost=1)
	T24_mem0 += alt(INPUT_mem_r)
	S += T11 < T24_mem0
	S += T24_mem0-1 <= T24

	T24_mem1 = S.Task('T24_mem1', length=1, delay_cost=1)
	T24_mem1 += alt(INPUT_mem_r)
	S += T12 < T24_mem1
	S += T24_mem1-1 <= T24

	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	T20_in += alt(MUL_in)
	T20 = S.Task('T20', length=5, delay_cost=1)
	T20 += alt(MUL)
	S += T20>=T20_in

	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += alt(INPUT_mem_r)
	S += T15 < T20_mem0
	S += T20_mem0-1 <= T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += alt(INPUT_mem_r)
	S += T18 < T20_mem1
	S += T20_mem1-1 <= T20

	T22_in = S.Task('T22_in', length=1, delay_cost=1)
	T22_in += alt(MUL_in)
	T22 = S.Task('T22', length=5, delay_cost=1)
	T22 += alt(MUL)
	S += T22>=T22_in

	T22_mem0 = S.Task('T22_mem0', length=1, delay_cost=1)
	T22_mem0 += alt(INPUT_mem_r)
	S += T21 < T22_mem0
	S += T22_mem0-1 <= T22

	T23_in = S.Task('T23_in', length=1, delay_cost=1)
	T23_in += alt(MUL_in)
	T23 = S.Task('T23', length=5, delay_cost=1)
	T23 += alt(MUL)
	S += T23>=T23_in

	T23_mem0 = S.Task('T23_mem0', length=1, delay_cost=1)
	T23_mem0 += alt(INPUT_mem_r)
	S += T19 < T23_mem0
	S += T23_mem0-1 <= T23

	T25 = S.Task('T25', length=1, delay_cost=1)
	T25 += alt(MAS)

	T25_mem0 = S.Task('T25_mem0', length=1, delay_cost=1)
	T25_mem0 += alt(INPUT_mem_r)
	S += T20 < T25_mem0
	S += T25_mem0-1 <= T25

	Z2_new_in = S.Task('Z2_new_in', length=1, delay_cost=1)
	Z2_new_in += alt(MUL_in)
	Z2_new = S.Task('Z2_new', length=5, delay_cost=1)
	Z2_new += alt(MUL)
	S += Z2_new>=Z2_new_in

	S += 0<Z2_new

	Z2_new_mem0 = S.Task('Z2_new_mem0', length=1, delay_cost=1)
	Z2_new_mem0 += INPUT_mem_r
	S += Z2_new_mem0-1 <= Z2_new

	Z2_new_mem1 = S.Task('Z2_new_mem1', length=1, delay_cost=1)
	Z2_new_mem1 += alt(INPUT_mem_r)
	S += T14 < Z2_new_mem1
	S += Z2_new_mem1-1 <= Z2_new

	Z2_new_w = S.Task('Z2_new_w', length=1, delay_cost=1)
	Z2_new_w += alt(INPUT_mem_w)
	S += Z2_new <= Z2_new_w

	X2_new = S.Task('X2_new', length=1, delay_cost=1)
	X2_new += alt(MAS)

	S += 0<X2_new

	X2_new_mem0 = S.Task('X2_new_mem0', length=1, delay_cost=1)
	X2_new_mem0 += alt(INPUT_mem_r)
	S += T22 < X2_new_mem0
	S += X2_new_mem0-1 <= X2_new

	X2_new_mem1 = S.Task('X2_new_mem1', length=1, delay_cost=1)
	X2_new_mem1 += alt(INPUT_mem_r)
	S += T24 < X2_new_mem1
	S += X2_new_mem1-1 <= X2_new

	X2_new_w = S.Task('X2_new_w', length=1, delay_cost=1)
	X2_new_w += alt(INPUT_mem_w)
	S += X2_new <= X2_new_w

	X1_new = S.Task('X1_new', length=1, delay_cost=1)
	X1_new += alt(MAS)

	S += 0<X1_new

	X1_new_mem0 = S.Task('X1_new_mem0', length=1, delay_cost=1)
	X1_new_mem0 += alt(INPUT_mem_r)
	S += T23 < X1_new_mem0
	S += X1_new_mem0-1 <= X1_new

	X1_new_mem1 = S.Task('X1_new_mem1', length=1, delay_cost=1)
	X1_new_mem1 += alt(INPUT_mem_r)
	S += T17 < X1_new_mem1
	S += X1_new_mem1-1 <= X1_new

	X1_new_w = S.Task('X1_new_w', length=1, delay_cost=1)
	X1_new_w += alt(INPUT_mem_w)
	S += X1_new <= X1_new_w

	Z1_new = S.Task('Z1_new', length=1, delay_cost=1)
	Z1_new += alt(MAS)

	S += 0<Z1_new

	Z1_new_mem0 = S.Task('Z1_new_mem0', length=1, delay_cost=1)
	Z1_new_mem0 += alt(INPUT_mem_r)
	S += T16 < Z1_new_mem0
	S += Z1_new_mem0-1 <= Z1_new

	Z1_new_mem1 = S.Task('Z1_new_mem1', length=1, delay_cost=1)
	Z1_new_mem1 += alt(INPUT_mem_r)
	S += T25 < Z1_new_mem1
	S += Z1_new_mem1-1 <= Z1_new

	Z1_new_w = S.Task('Z1_new_w', length=1, delay_cost=1)
	Z1_new_w += alt(INPUT_mem_w)
	S += Z1_new <= Z1_new_w

	solvers.mip.solve(S,msg=1,ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/Users/fukudamomoko/Desktop/research/ABE/python/scheduling/ladderMul_mul1_5_add1_1/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=False, fig_size=(cycles*0.25+3, 5))

	return solution

