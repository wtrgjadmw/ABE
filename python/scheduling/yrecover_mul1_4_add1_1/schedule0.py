from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MUL = S.Resources('MUL', num=1, size=4)
	MUL_in = S.Resources('MUL_in', num=1)
	INV = S.Resource('INV')
	ADD = S.Resources('ADD', num=1, periods=range(1, horizon))
	SUB = S.Resources('SUB', num=1, periods=range(1, horizon))
	INPUT_mem_w = S.Resource('INPUT_mem_w', size=2)
	INPUT_mem_r = S.Resource('INPUT_mem_r', size=4)

	# result of previous scheduling

	# new tasks
	r1_in = S.Task('r1_in', length=1, delay_cost=1)
	r1_in += alt(MUL_in)
	r1 = S.Task('r1', length=4, delay_cost=1)
	r1 += alt(MUL)
	S += r1>=r1_in

	r1_mem0 = S.Task('r1_mem0', length=1, delay_cost=1)
	r1_mem0 += INPUT_mem_r
	S += r1_mem0-1 <= r1

	r1_mem1 = S.Task('r1_mem1', length=1, delay_cost=1)
	r1_mem1 += INPUT_mem_r
	S += r1_mem1-1 <= r1

	r3_in = S.Task('r3_in', length=1, delay_cost=1)
	r3_in += alt(MUL_in)
	r3 = S.Task('r3', length=4, delay_cost=1)
	r3 += alt(MUL)
	S += r3>=r3_in

	r3_mem0 = S.Task('r3_mem0', length=1, delay_cost=1)
	r3_mem0 += INPUT_mem_r
	S += r3_mem0-1 <= r3

	r3_mem1 = S.Task('r3_mem1', length=1, delay_cost=1)
	r3_mem1 += INPUT_mem_r
	S += r3_mem1-1 <= r3

	r4_in = S.Task('r4_in', length=1, delay_cost=1)
	r4_in += alt(MUL_in)
	r4 = S.Task('r4', length=4, delay_cost=1)
	r4 += alt(MUL)
	S += r4>=r4_in

	r4_mem0 = S.Task('r4_mem0', length=1, delay_cost=1)
	r4_mem0 += INPUT_mem_r
	S += r4_mem0-1 <= r4

	r4_mem1 = S.Task('r4_mem1', length=1, delay_cost=1)
	r4_mem1 += INPUT_mem_r
	S += r4_mem1-1 <= r4

	r5_in = S.Task('r5_in', length=1, delay_cost=1)
	r5_in += alt(MUL_in)
	r5 = S.Task('r5', length=4, delay_cost=1)
	r5 += alt(MUL)
	S += r5>=r5_in

	r5_mem0 = S.Task('r5_mem0', length=1, delay_cost=1)
	r5_mem0 += INPUT_mem_r
	S += r5_mem0-1 <= r5

	r5_mem1 = S.Task('r5_mem1', length=1, delay_cost=1)
	r5_mem1 += INPUT_mem_r
	S += r5_mem1-1 <= r5

	r6_in = S.Task('r6_in', length=1, delay_cost=1)
	r6_in += alt(MUL_in)
	r6 = S.Task('r6', length=4, delay_cost=1)
	r6 += alt(MUL)
	S += r6>=r6_in

	r6_mem0 = S.Task('r6_mem0', length=1, delay_cost=1)
	r6_mem0 += INPUT_mem_r
	S += r6_mem0-1 <= r6

	r6_mem1 = S.Task('r6_mem1', length=1, delay_cost=1)
	r6_mem1 += INPUT_mem_r
	S += r6_mem1-1 <= r6

	r12_in = S.Task('r12_in', length=1, delay_cost=1)
	r12_in += alt(MUL_in)
	r12 = S.Task('r12', length=4, delay_cost=1)
	r12 += alt(MUL)
	S += r12>=r12_in

	r12_mem0 = S.Task('r12_mem0', length=1, delay_cost=1)
	r12_mem0 += INPUT_mem_r
	S += r12_mem0-1 <= r12

	r12_mem1 = S.Task('r12_mem1', length=1, delay_cost=1)
	r12_mem1 += INPUT_mem_r
	S += r12_mem1-1 <= r12

	r13_in = S.Task('r13_in', length=1, delay_cost=1)
	r13_in += alt(MUL_in)
	r13 = S.Task('r13', length=4, delay_cost=1)
	r13 += alt(MUL)
	S += r13>=r13_in

	r13_mem0 = S.Task('r13_mem0', length=1, delay_cost=1)
	r13_mem0 += INPUT_mem_r
	S += r13_mem0-1 <= r13

	r13_mem1 = S.Task('r13_mem1', length=1, delay_cost=1)
	r13_mem1 += INPUT_mem_r
	S += r13_mem1-1 <= r13

	r2 = S.Task('r2', length=1, delay_cost=1)
	r2 += alt(ADD)

	r2_mem0 = S.Task('r2_mem0', length=1, delay_cost=1)
	r2_mem0 += alt(INPUT_mem_r)
	S += r1 < r2_mem0
	S += r2_mem0-1 <= r2

	r7 = S.Task('r7', length=1, delay_cost=1)
	r7 += alt(ADD)

	r7_mem0 = S.Task('r7_mem0', length=1, delay_cost=1)
	r7_mem0 += alt(INPUT_mem_r)
	S += r5 < r7_mem0
	S += r7_mem0-1 <= r7

	r7_mem1 = S.Task('r7_mem1', length=1, delay_cost=1)
	r7_mem1 += alt(INPUT_mem_r)
	S += r6 < r7_mem1
	S += r7_mem1-1 <= r7

	r8 = S.Task('r8', length=1, delay_cost=1)
	r8 += alt(ADD)

	r8_mem0 = S.Task('r8_mem0', length=1, delay_cost=1)
	r8_mem0 += INPUT_mem_r
	S += r8_mem0-1 <= r8

	r8_mem1 = S.Task('r8_mem1', length=1, delay_cost=1)
	r8_mem1 += alt(INPUT_mem_r)
	S += r4 < r8_mem1
	S += r8_mem1-1 <= r8

	r10 = S.Task('r10', length=1, delay_cost=1)
	r10 += alt(SUB)

	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	r10_mem0 += INPUT_mem_r
	S += r10_mem0-1 <= r10

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	r10_mem1 += alt(INPUT_mem_r)
	S += r4 < r10_mem1
	S += r10_mem1-1 <= r10

	r9_in = S.Task('r9_in', length=1, delay_cost=1)
	r9_in += alt(MUL_in)
	r9 = S.Task('r9', length=4, delay_cost=1)
	r9 += alt(MUL)
	S += r9>=r9_in

	r9_mem0 = S.Task('r9_mem0', length=1, delay_cost=1)
	r9_mem0 += INPUT_mem_r
	S += r9_mem0-1 <= r9

	r9_mem1 = S.Task('r9_mem1', length=1, delay_cost=1)
	r9_mem1 += alt(INPUT_mem_r)
	S += r7 < r9_mem1
	S += r9_mem1-1 <= r9

	r11_in = S.Task('r11_in', length=1, delay_cost=1)
	r11_in += alt(MUL_in)
	r11 = S.Task('r11', length=4, delay_cost=1)
	r11 += alt(MUL)
	S += r11>=r11_in

	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	r11_mem0 += alt(INPUT_mem_r)
	S += r10 < r11_mem0
	S += r11_mem0-1 <= r11

	r14_in = S.Task('r14_in', length=1, delay_cost=1)
	r14_in += alt(MUL_in)
	r14 = S.Task('r14', length=4, delay_cost=1)
	r14 += alt(MUL)
	S += r14>=r14_in

	r14_mem0 = S.Task('r14_mem0', length=1, delay_cost=1)
	r14_mem0 += alt(INPUT_mem_r)
	S += r2 < r14_mem0
	S += r14_mem0-1 <= r14

	r14_mem1 = S.Task('r14_mem1', length=1, delay_cost=1)
	r14_mem1 += alt(INPUT_mem_r)
	S += r3 < r14_mem1
	S += r14_mem1-1 <= r14

	r15_in = S.Task('r15_in', length=1, delay_cost=1)
	r15_in += alt(MUL_in)
	r15 = S.Task('r15', length=4, delay_cost=1)
	r15 += alt(MUL)
	S += r15>=r15_in

	r15_mem0 = S.Task('r15_mem0', length=1, delay_cost=1)
	r15_mem0 += alt(INPUT_mem_r)
	S += r8 < r15_mem0
	S += r15_mem0-1 <= r15

	r15_mem1 = S.Task('r15_mem1', length=1, delay_cost=1)
	r15_mem1 += alt(INPUT_mem_r)
	S += r9 < r15_mem1
	S += r15_mem1-1 <= r15

	r16_in = S.Task('r16_in', length=1, delay_cost=1)
	r16_in += alt(MUL_in)
	r16 = S.Task('r16', length=4, delay_cost=1)
	r16 += alt(MUL)
	S += r16>=r16_in

	r16_mem0 = S.Task('r16_mem0', length=1, delay_cost=1)
	r16_mem0 += alt(INPUT_mem_r)
	S += r11 < r16_mem0
	S += r16_mem0-1 <= r16

	r16_mem1 = S.Task('r16_mem1', length=1, delay_cost=1)
	r16_mem1 += INPUT_mem_r
	S += r16_mem1-1 <= r16

	r17 = S.Task('r17', length=1, delay_cost=1)
	r17 += alt(ADD)

	r17_mem0 = S.Task('r17_mem0', length=1, delay_cost=1)
	r17_mem0 += alt(INPUT_mem_r)
	S += r14 < r17_mem0
	S += r17_mem0-1 <= r17

	r17_mem1 = S.Task('r17_mem1', length=1, delay_cost=1)
	r17_mem1 += alt(INPUT_mem_r)
	S += r15 < r17_mem1
	S += r17_mem1-1 <= r17

	PX_new_in = S.Task('PX_new_in', length=1, delay_cost=1)
	PX_new_in += alt(MUL_in)
	PX_new = S.Task('PX_new', length=4, delay_cost=1)
	PX_new += alt(MUL)
	S += PX_new>=PX_new_in

	S += 0<PX_new

	PX_new_mem0 = S.Task('PX_new_mem0', length=1, delay_cost=1)
	PX_new_mem0 += alt(INPUT_mem_r)
	S += r2 < PX_new_mem0
	S += PX_new_mem0-1 <= PX_new

	PX_new_mem1 = S.Task('PX_new_mem1', length=1, delay_cost=1)
	PX_new_mem1 += alt(INPUT_mem_r)
	S += r12 < PX_new_mem1
	S += PX_new_mem1-1 <= PX_new

	PX_new_w = S.Task('PX_new_w', length=1, delay_cost=1)
	PX_new_w += alt(INPUT_mem_w)
	S += PX_new <= PX_new_w

	Z1_new_in = S.Task('Z1_new_in', length=1, delay_cost=1)
	Z1_new_in += alt(MUL_in)
	Z1_new = S.Task('Z1_new', length=4, delay_cost=1)
	Z1_new += alt(MUL)
	S += Z1_new>=Z1_new_in

	S += 0<Z1_new

	Z1_new_mem0 = S.Task('Z1_new_mem0', length=1, delay_cost=1)
	Z1_new_mem0 += alt(INPUT_mem_r)
	S += r2 < Z1_new_mem0
	S += Z1_new_mem0-1 <= Z1_new

	Z1_new_mem1 = S.Task('Z1_new_mem1', length=1, delay_cost=1)
	Z1_new_mem1 += alt(INPUT_mem_r)
	S += r13 < Z1_new_mem1
	S += Z1_new_mem1-1 <= Z1_new

	Z1_new_w = S.Task('Z1_new_w', length=1, delay_cost=1)
	Z1_new_w += alt(INPUT_mem_w)
	S += Z1_new <= Z1_new_w

	PY_new = S.Task('PY_new', length=1, delay_cost=1)
	PY_new += alt(SUB)

	S += 0<PY_new

	PY_new_mem0 = S.Task('PY_new_mem0', length=1, delay_cost=1)
	PY_new_mem0 += alt(INPUT_mem_r)
	S += r17 < PY_new_mem0
	S += PY_new_mem0-1 <= PY_new

	PY_new_mem1 = S.Task('PY_new_mem1', length=1, delay_cost=1)
	PY_new_mem1 += alt(INPUT_mem_r)
	S += r16 < PY_new_mem1
	S += PY_new_mem1-1 <= PY_new

	PY_new_w = S.Task('PY_new_w', length=1, delay_cost=1)
	PY_new_w += alt(INPUT_mem_w)
	S += PY_new <= PY_new_w

	solvers.mip.solve(S,msg=1,ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/Users/fukudamomoko/Desktop/research/ABE/python/scheduling/yrecover_mul1_4_add1_1/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, vertical_text=False, fig_size=(cycles*0.25+3, 5))

	return solution

