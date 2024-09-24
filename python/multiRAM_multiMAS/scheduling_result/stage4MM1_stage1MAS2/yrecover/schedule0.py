from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=2, size=1, periods=range(1, horizon))
	MAS_in = S.Resources('MAS_in', num=2)
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	r1_in = S.Task('r1_in', length=1, delay_cost=1)
	r1_in += alt(MM_in)
	r1 = S.Task('r1', length=4, delay_cost=1)
	r1 += alt(MM)
	S += r1>=r1_in

	r1_mem0 = S.Task('r1_mem0', length=1, delay_cost=1)
	r1_mem0 += MAIN_MEM_r[0]
	S += r1_mem0 <= r1

	r1_mem1 = S.Task('r1_mem1', length=1, delay_cost=1)
	r1_mem1 += MAIN_MEM_r[1]
	S += r1_mem1 <= r1

	r3_in = S.Task('r3_in', length=1, delay_cost=1)
	r3_in += alt(MM_in)
	r3 = S.Task('r3', length=4, delay_cost=1)
	r3 += alt(MM)
	S += r3>=r3_in

	r3_mem0 = S.Task('r3_mem0', length=1, delay_cost=1)
	r3_mem0 += MAIN_MEM_r[0]
	S += r3_mem0 <= r3

	r3_mem1 = S.Task('r3_mem1', length=1, delay_cost=1)
	r3_mem1 += MAIN_MEM_r[1]
	S += r3_mem1 <= r3

	r4_in = S.Task('r4_in', length=1, delay_cost=1)
	r4_in += alt(MM_in)
	r4 = S.Task('r4', length=4, delay_cost=1)
	r4 += alt(MM)
	S += r4>=r4_in

	r4_mem0 = S.Task('r4_mem0', length=1, delay_cost=1)
	r4_mem0 += MAIN_MEM_r[0]
	S += r4_mem0 <= r4

	r4_mem1 = S.Task('r4_mem1', length=1, delay_cost=1)
	r4_mem1 += MAIN_MEM_r[1]
	S += r4_mem1 <= r4

	r5_in = S.Task('r5_in', length=1, delay_cost=1)
	r5_in += alt(MM_in)
	r5 = S.Task('r5', length=4, delay_cost=1)
	r5 += alt(MM)
	S += r5>=r5_in

	r5_mem0 = S.Task('r5_mem0', length=1, delay_cost=1)
	r5_mem0 += MAIN_MEM_r[0]
	S += r5_mem0 <= r5

	r5_mem1 = S.Task('r5_mem1', length=1, delay_cost=1)
	r5_mem1 += MAIN_MEM_r[1]
	S += r5_mem1 <= r5

	r6_in = S.Task('r6_in', length=1, delay_cost=1)
	r6_in += alt(MM_in)
	r6 = S.Task('r6', length=4, delay_cost=1)
	r6 += alt(MM)
	S += r6>=r6_in

	r6_mem0 = S.Task('r6_mem0', length=1, delay_cost=1)
	r6_mem0 += MAIN_MEM_r[0]
	S += r6_mem0 <= r6

	r6_mem1 = S.Task('r6_mem1', length=1, delay_cost=1)
	r6_mem1 += MAIN_MEM_r[1]
	S += r6_mem1 <= r6

	r12_in = S.Task('r12_in', length=1, delay_cost=1)
	r12_in += alt(MM_in)
	r12 = S.Task('r12', length=4, delay_cost=1)
	r12 += alt(MM)
	S += r12>=r12_in

	r12_mem0 = S.Task('r12_mem0', length=1, delay_cost=1)
	r12_mem0 += MAIN_MEM_r[0]
	S += r12_mem0 <= r12

	r12_mem1 = S.Task('r12_mem1', length=1, delay_cost=1)
	r12_mem1 += MAIN_MEM_r[1]
	S += r12_mem1 <= r12

	r13_in = S.Task('r13_in', length=1, delay_cost=1)
	r13_in += alt(MM_in)
	r13 = S.Task('r13', length=4, delay_cost=1)
	r13 += alt(MM)
	S += r13>=r13_in

	r13_mem0 = S.Task('r13_mem0', length=1, delay_cost=1)
	r13_mem0 += MAIN_MEM_r[0]
	S += r13_mem0 <= r13

	r13_mem1 = S.Task('r13_mem1', length=1, delay_cost=1)
	r13_mem1 += MAIN_MEM_r[1]
	S += r13_mem1 <= r13

	r2_in = S.Task('r2_in', length=1, delay_cost=1)
	r2_in += alt(MAS_in)
	r2 = S.Task('r2', length=1, delay_cost=1)
	r2 += alt(MAS)

	S += r2>=r2_in

	r2_mem0 = S.Task('r2_mem0', length=1, delay_cost=1)
	r2_mem0 += alt(MM_MEM)
	S += (r1*MM[0])-1 < r2_mem0*MM_MEM[0]
	S += r2_mem0 <= r2

	r2_mem1 = S.Task('r2_mem1', length=1, delay_cost=1)
	r2_mem1 += alt(MM_MEM)
	S += (r1*MM[0])-1 < r2_mem1*MM_MEM[1]
	S += r2_mem1 <= r2

	r7_in = S.Task('r7_in', length=1, delay_cost=1)
	r7_in += alt(MAS_in)
	r7 = S.Task('r7', length=1, delay_cost=1)
	r7 += alt(MAS)

	S += r7>=r7_in

	r7_mem0 = S.Task('r7_mem0', length=1, delay_cost=1)
	r7_mem0 += alt(MM_MEM)
	S += (r5*MM[0])-1 < r7_mem0*MM_MEM[0]
	S += r7_mem0 <= r7

	r7_mem1 = S.Task('r7_mem1', length=1, delay_cost=1)
	r7_mem1 += alt(MM_MEM)
	S += (r6*MM[0])-1 < r7_mem1*MM_MEM[1]
	S += r7_mem1 <= r7

	r8_in = S.Task('r8_in', length=1, delay_cost=1)
	r8_in += alt(MAS_in)
	r8 = S.Task('r8', length=1, delay_cost=1)
	r8 += alt(MAS)

	S += r8>=r8_in

	r8_mem0 = S.Task('r8_mem0', length=1, delay_cost=1)
	r8_mem0 += MAIN_MEM_r[0]
	S += r8_mem0 <= r8

	r8_mem1 = S.Task('r8_mem1', length=1, delay_cost=1)
	r8_mem1 += alt(MM_MEM)
	S += (r4*MM[0])-1 < r8_mem1*MM_MEM[1]
	S += r8_mem1 <= r8

	r10_in = S.Task('r10_in', length=1, delay_cost=1)
	r10_in += alt(MAS_in)
	r10 = S.Task('r10', length=1, delay_cost=1)
	r10 += alt(MAS)

	S += r10>=r10_in

	r10_mem0 = S.Task('r10_mem0', length=1, delay_cost=1)
	r10_mem0 += MAIN_MEM_r[0]
	S += r10_mem0 <= r10

	r10_mem1 = S.Task('r10_mem1', length=1, delay_cost=1)
	r10_mem1 += alt(MM_MEM)
	S += (r4*MM[0])-1 < r10_mem1*MM_MEM[1]
	S += r10_mem1 <= r10

	r9_in = S.Task('r9_in', length=1, delay_cost=1)
	r9_in += alt(MM_in)
	r9 = S.Task('r9', length=4, delay_cost=1)
	r9 += alt(MM)
	S += r9>=r9_in

	r9_mem0 = S.Task('r9_mem0', length=1, delay_cost=1)
	r9_mem0 += MAIN_MEM_r[0]
	S += r9_mem0 <= r9

	r9_mem1 = S.Task('r9_mem1', length=1, delay_cost=1)
	r9_mem1 += alt(MAS_MEM)
	S += (r7*MAS[0])-1 < r9_mem1*MAS_MEM[1]
	S += (r7*MAS[1])-1 < r9_mem1*MAS_MEM[3]
	S += r9_mem1 <= r9

	r11_in = S.Task('r11_in', length=1, delay_cost=1)
	r11_in += alt(MM_in)
	r11 = S.Task('r11', length=4, delay_cost=1)
	r11 += alt(MM)
	S += r11>=r11_in

	r11_mem0 = S.Task('r11_mem0', length=1, delay_cost=1)
	r11_mem0 += alt(MAS_MEM)
	S += (r10*MAS[0])-1 < r11_mem0*MAS_MEM[0]
	S += (r10*MAS[1])-1 < r11_mem0*MAS_MEM[2]
	S += r11_mem0 <= r11

	r11_mem1 = S.Task('r11_mem1', length=1, delay_cost=1)
	r11_mem1 += alt(MAS_MEM)
	S += (r10*MAS[0])-1 < r11_mem1*MAS_MEM[1]
	S += (r10*MAS[1])-1 < r11_mem1*MAS_MEM[3]
	S += r11_mem1 <= r11

	r14_in = S.Task('r14_in', length=1, delay_cost=1)
	r14_in += alt(MM_in)
	r14 = S.Task('r14', length=4, delay_cost=1)
	r14 += alt(MM)
	S += r14>=r14_in

	r14_mem0 = S.Task('r14_mem0', length=1, delay_cost=1)
	r14_mem0 += alt(MAS_MEM)
	S += (r2*MAS[0])-1 < r14_mem0*MAS_MEM[0]
	S += (r2*MAS[1])-1 < r14_mem0*MAS_MEM[2]
	S += r14_mem0 <= r14

	r14_mem1 = S.Task('r14_mem1', length=1, delay_cost=1)
	r14_mem1 += alt(MM_MEM)
	S += (r3*MM[0])-1 < r14_mem1*MM_MEM[1]
	S += r14_mem1 <= r14

	r15_in = S.Task('r15_in', length=1, delay_cost=1)
	r15_in += alt(MM_in)
	r15 = S.Task('r15', length=4, delay_cost=1)
	r15 += alt(MM)
	S += r15>=r15_in

	r15_mem0 = S.Task('r15_mem0', length=1, delay_cost=1)
	r15_mem0 += alt(MAS_MEM)
	S += (r8*MAS[0])-1 < r15_mem0*MAS_MEM[0]
	S += (r8*MAS[1])-1 < r15_mem0*MAS_MEM[2]
	S += r15_mem0 <= r15

	r15_mem1 = S.Task('r15_mem1', length=1, delay_cost=1)
	r15_mem1 += alt(MM_MEM)
	S += (r9*MM[0])-1 < r15_mem1*MM_MEM[1]
	S += r15_mem1 <= r15

	r16_in = S.Task('r16_in', length=1, delay_cost=1)
	r16_in += alt(MM_in)
	r16 = S.Task('r16', length=4, delay_cost=1)
	r16 += alt(MM)
	S += r16>=r16_in

	r16_mem0 = S.Task('r16_mem0', length=1, delay_cost=1)
	r16_mem0 += alt(MM_MEM)
	S += (r11*MM[0])-1 < r16_mem0*MM_MEM[0]
	S += r16_mem0 <= r16

	r16_mem1 = S.Task('r16_mem1', length=1, delay_cost=1)
	r16_mem1 += MAIN_MEM_r[1]
	S += r16_mem1 <= r16

	r17_in = S.Task('r17_in', length=1, delay_cost=1)
	r17_in += alt(MAS_in)
	r17 = S.Task('r17', length=1, delay_cost=1)
	r17 += alt(MAS)

	S += r17>=r17_in

	r17_mem0 = S.Task('r17_mem0', length=1, delay_cost=1)
	r17_mem0 += alt(MM_MEM)
	S += (r14*MM[0])-1 < r17_mem0*MM_MEM[0]
	S += r17_mem0 <= r17

	r17_mem1 = S.Task('r17_mem1', length=1, delay_cost=1)
	r17_mem1 += alt(MM_MEM)
	S += (r15*MM[0])-1 < r17_mem1*MM_MEM[1]
	S += r17_mem1 <= r17

	PX_new_in = S.Task('PX_new_in', length=1, delay_cost=1)
	PX_new_in += alt(MM_in)
	PX_new = S.Task('PX_new', length=4, delay_cost=1)
	PX_new += alt(MM)
	S += PX_new>=PX_new_in

	S += 0<PX_new

	PX_new_mem0 = S.Task('PX_new_mem0', length=1, delay_cost=1)
	PX_new_mem0 += alt(MAS_MEM)
	S += (r2*MAS[0])-1 < PX_new_mem0*MAS_MEM[0]
	S += (r2*MAS[1])-1 < PX_new_mem0*MAS_MEM[2]
	S += PX_new_mem0 <= PX_new

	PX_new_mem1 = S.Task('PX_new_mem1', length=1, delay_cost=1)
	PX_new_mem1 += alt(MM_MEM)
	S += (r12*MM[0])-1 < PX_new_mem1*MM_MEM[1]
	S += PX_new_mem1 <= PX_new

	PX_new_w = S.Task('PX_new_w', length=1, delay_cost=1)
	PX_new_w += alt(MAIN_MEM_w)
	S += PX_new <= PX_new_w

	Z1_new_in = S.Task('Z1_new_in', length=1, delay_cost=1)
	Z1_new_in += alt(MM_in)
	Z1_new = S.Task('Z1_new', length=4, delay_cost=1)
	Z1_new += alt(MM)
	S += Z1_new>=Z1_new_in

	S += 0<Z1_new

	Z1_new_mem0 = S.Task('Z1_new_mem0', length=1, delay_cost=1)
	Z1_new_mem0 += alt(MAS_MEM)
	S += (r2*MAS[0])-1 < Z1_new_mem0*MAS_MEM[0]
	S += (r2*MAS[1])-1 < Z1_new_mem0*MAS_MEM[2]
	S += Z1_new_mem0 <= Z1_new

	Z1_new_mem1 = S.Task('Z1_new_mem1', length=1, delay_cost=1)
	Z1_new_mem1 += alt(MM_MEM)
	S += (r13*MM[0])-1 < Z1_new_mem1*MM_MEM[1]
	S += Z1_new_mem1 <= Z1_new

	Z1_new_w = S.Task('Z1_new_w', length=1, delay_cost=1)
	Z1_new_w += alt(MAIN_MEM_w)
	S += Z1_new <= Z1_new_w

	PY_new_in = S.Task('PY_new_in', length=1, delay_cost=1)
	PY_new_in += alt(MAS_in)
	PY_new = S.Task('PY_new', length=1, delay_cost=1)
	PY_new += alt(MAS)

	S += PY_new>=PY_new_in

	S += 0<PY_new

	PY_new_mem0 = S.Task('PY_new_mem0', length=1, delay_cost=1)
	PY_new_mem0 += alt(MAS_MEM)
	S += (r17*MAS[0])-1 < PY_new_mem0*MAS_MEM[0]
	S += (r17*MAS[1])-1 < PY_new_mem0*MAS_MEM[2]
	S += PY_new_mem0 <= PY_new

	PY_new_mem1 = S.Task('PY_new_mem1', length=1, delay_cost=1)
	PY_new_mem1 += alt(MM_MEM)
	S += (r16*MM[0])-1 < PY_new_mem1*MM_MEM[1]
	S += PY_new_mem1 <= PY_new

	PY_new_w = S.Task('PY_new_w', length=1, delay_cost=1)
	PY_new_w += alt(MAIN_MEM_w)
	S += PY_new <= PY_new_w

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/yrecover_mul1_4_add2_1/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, fig_size=(cycles*0.25+3, 5))

	return solution

