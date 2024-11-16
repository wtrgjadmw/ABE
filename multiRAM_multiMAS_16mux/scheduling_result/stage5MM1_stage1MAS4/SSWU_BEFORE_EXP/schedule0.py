from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 90
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	t2_in += alt(MM_in)
	t2 = S.Task('t2', length=5, delay_cost=1)
	t2 += alt(MM)
	S += t2>=t2_in

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	t2_mem0 += MAIN_MEM_r[0]
	S += t2_mem0 <= t2

	xit2 = S.Task('xit2', length=1, delay_cost=1)
	xit2 += alt(MAS)

	xit2_mem0 = S.Task('xit2_mem0', length=1, delay_cost=1)
	xit2_mem0 += MAIN_MEM_r[0]
	S += xit2_mem0 <= xit2

	xit2_mem1 = S.Task('xit2_mem1', length=1, delay_cost=1)
	xit2_mem1 += alt(MM_MEM)
	S += (t2*MM[0])-1 < xit2_mem1*MM_MEM[1]
	S += xit2_mem1 <= xit2

	xi2t4_in = S.Task('xi2t4_in', length=1, delay_cost=1)
	xi2t4_in += alt(MM_in)
	xi2t4 = S.Task('xi2t4', length=5, delay_cost=1)
	xi2t4 += alt(MM)
	S += xi2t4>=xi2t4_in

	xi2t4_mem0 = S.Task('xi2t4_mem0', length=1, delay_cost=1)
	xi2t4_mem0 += alt(MAS_MEM)
	S += (xit2*MAS[0])-1 < xi2t4_mem0*MAS_MEM[0]
	S += (xit2*MAS[1])-1 < xi2t4_mem0*MAS_MEM[2]
	S += (xit2*MAS[2])-1 < xi2t4_mem0*MAS_MEM[4]
	S += (xit2*MAS[3])-1 < xi2t4_mem0*MAS_MEM[6]
	S += xi2t4_mem0 <= xi2t4

	D_a_ = S.Task('D_a_', length=1, delay_cost=1)
	D_a_ += alt(MAS)

	D_a__mem0 = S.Task('D_a__mem0', length=1, delay_cost=1)
	D_a__mem0 += alt(MAS_MEM)
	S += (xit2*MAS[0])-1 < D_a__mem0*MAS_MEM[0]
	S += (xit2*MAS[1])-1 < D_a__mem0*MAS_MEM[2]
	S += (xit2*MAS[2])-1 < D_a__mem0*MAS_MEM[4]
	S += (xit2*MAS[3])-1 < D_a__mem0*MAS_MEM[6]
	S += D_a__mem0 <= D_a_

	D_a__mem1 = S.Task('D_a__mem1', length=1, delay_cost=1)
	D_a__mem1 += alt(MM_MEM)
	S += (xi2t4*MM[0])-1 < D_a__mem1*MM_MEM[1]
	S += D_a__mem1 <= D_a_

	negD_in = S.Task('negD_in', length=1, delay_cost=1)
	negD_in += alt(MM_in)
	negD = S.Task('negD', length=5, delay_cost=1)
	negD += alt(MM)
	S += negD>=negD_in

	negD_mem0 = S.Task('negD_mem0', length=1, delay_cost=1)
	negD_mem0 += alt(MAS_MEM)
	S += (D_a_*MAS[0])-1 < negD_mem0*MAS_MEM[0]
	S += (D_a_*MAS[1])-1 < negD_mem0*MAS_MEM[2]
	S += (D_a_*MAS[2])-1 < negD_mem0*MAS_MEM[4]
	S += (D_a_*MAS[3])-1 < negD_mem0*MAS_MEM[6]
	S += negD_mem0 <= negD

	negD_mem1 = S.Task('negD_mem1', length=1, delay_cost=1)
	negD_mem1 += MAIN_MEM_r[1]
	S += negD_mem1 <= negD

	N_b = S.Task('N_b', length=1, delay_cost=1)
	N_b += alt(MAS)

	N_b_mem0 = S.Task('N_b_mem0', length=1, delay_cost=1)
	N_b_mem0 += alt(MAS_MEM)
	S += (D_a_*MAS[0])-1 < N_b_mem0*MAS_MEM[0]
	S += (D_a_*MAS[1])-1 < N_b_mem0*MAS_MEM[2]
	S += (D_a_*MAS[2])-1 < N_b_mem0*MAS_MEM[4]
	S += (D_a_*MAS[3])-1 < N_b_mem0*MAS_MEM[6]
	S += N_b_mem0 <= N_b

	N_b_mem1 = S.Task('N_b_mem1', length=1, delay_cost=1)
	N_b_mem1 += MAIN_MEM_r[1]
	S += N_b_mem1 <= N_b

	D = S.Task('D', length=1, delay_cost=1)
	D += alt(MAS)

	D_mem0 = S.Task('D_mem0', length=1, delay_cost=1)
	D_mem0 += MAIN_MEM_r[0]
	S += D_mem0 <= D

	D_mem1 = S.Task('D_mem1', length=1, delay_cost=1)
	D_mem1 += alt(MM_MEM)
	S += (negD*MM[0])-1 < D_mem1*MM_MEM[1]
	S += D_mem1 <= D

	N_in = S.Task('N_in', length=1, delay_cost=1)
	N_in += alt(MM_in)
	N = S.Task('N', length=5, delay_cost=1)
	N += alt(MM)
	S += N>=N_in

	N_mem0 = S.Task('N_mem0', length=1, delay_cost=1)
	N_mem0 += MAIN_MEM_r[0]
	S += N_mem0 <= N

	N_mem1 = S.Task('N_mem1', length=1, delay_cost=1)
	N_mem1 += alt(MAS_MEM)
	S += (N_b*MAS[0])-1 < N_mem1*MAS_MEM[1]
	S += (N_b*MAS[1])-1 < N_mem1*MAS_MEM[3]
	S += (N_b*MAS[2])-1 < N_mem1*MAS_MEM[5]
	S += (N_b*MAS[3])-1 < N_mem1*MAS_MEM[7]
	S += N_mem1 <= N

	Z = S.Task('Z', length=3, delay_cost=1)
	Z += alt(CSEL)

	Z_mem0 = S.Task('Z_mem0', length=1, delay_cost=1)
	Z_mem0 += alt(MAS_MEM)
	S += (D*MAS[0])-1 < Z_mem0*MAS_MEM[0]
	S += (D*MAS[1])-1 < Z_mem0*MAS_MEM[2]
	S += (D*MAS[2])-1 < Z_mem0*MAS_MEM[4]
	S += (D*MAS[3])-1 < Z_mem0*MAS_MEM[6]
	S += Z_mem0 <= Z

	Z_mem1 = S.Task('Z_mem1', length=1, delay_cost=1)
	Z_mem1 += alt(MAS_MEM)
	S += (D*MAS[0])-1 < Z_mem1*MAS_MEM[1]
	S += (D*MAS[1])-1 < Z_mem1*MAS_MEM[3]
	S += (D*MAS[2])-1 < Z_mem1*MAS_MEM[5]
	S += (D*MAS[3])-1 < Z_mem1*MAS_MEM[7]
	S += Z_mem1 <= Z

	Z_mem2 = S.Task('Z_mem2', length=1, delay_cost=1)
	Z_mem2 += MAIN_MEM_r[0]
	S += Z_mem2 <= Z

	N2_in = S.Task('N2_in', length=1, delay_cost=1)
	N2_in += alt(MM_in)
	N2 = S.Task('N2', length=5, delay_cost=1)
	N2 += alt(MM)
	S += N2>=N2_in

	N2_mem0 = S.Task('N2_mem0', length=1, delay_cost=1)
	N2_mem0 += alt(MM_MEM)
	S += (N*MM[0])-1 < N2_mem0*MM_MEM[0]
	S += N2_mem0 <= N2

	D2_in = S.Task('D2_in', length=1, delay_cost=1)
	D2_in += alt(MM_in)
	D2 = S.Task('D2', length=5, delay_cost=1)
	D2 += alt(MM)
	S += D2>=D2_in

	S += Z < D2
	N3_in = S.Task('N3_in', length=1, delay_cost=1)
	N3_in += alt(MM_in)
	N3 = S.Task('N3', length=5, delay_cost=1)
	N3 += alt(MM)
	S += N3>=N3_in

	N3_mem0 = S.Task('N3_mem0', length=1, delay_cost=1)
	N3_mem0 += alt(MM_MEM)
	S += (N2*MM[0])-1 < N3_mem0*MM_MEM[0]
	S += N3_mem0 <= N3

	N3_mem1 = S.Task('N3_mem1', length=1, delay_cost=1)
	N3_mem1 += alt(MM_MEM)
	S += (N*MM[0])-1 < N3_mem1*MM_MEM[1]
	S += N3_mem1 <= N3

	V_in = S.Task('V_in', length=1, delay_cost=1)
	V_in += alt(MM_in)
	V = S.Task('V', length=5, delay_cost=1)
	V += alt(MM)
	S += V>=V_in

	V_mem0 = S.Task('V_mem0', length=1, delay_cost=1)
	V_mem0 += alt(MM_MEM)
	S += (D2*MM[0])-1 < V_mem0*MM_MEM[0]
	S += V_mem0 <= V

	S += Z < V
	ND2_in = S.Task('ND2_in', length=1, delay_cost=1)
	ND2_in += alt(MM_in)
	ND2 = S.Task('ND2', length=5, delay_cost=1)
	ND2 += alt(MM)
	S += ND2>=ND2_in

	ND2_mem0 = S.Task('ND2_mem0', length=1, delay_cost=1)
	ND2_mem0 += alt(MM_MEM)
	S += (N*MM[0])-1 < ND2_mem0*MM_MEM[0]
	S += ND2_mem0 <= ND2

	ND2_mem1 = S.Task('ND2_mem1', length=1, delay_cost=1)
	ND2_mem1 += alt(MM_MEM)
	S += (D2*MM[0])-1 < ND2_mem1*MM_MEM[1]
	S += ND2_mem1 <= ND2

	aND2_in = S.Task('aND2_in', length=1, delay_cost=1)
	aND2_in += alt(MM_in)
	aND2 = S.Task('aND2', length=5, delay_cost=1)
	aND2 += alt(MM)
	S += aND2>=aND2_in

	aND2_mem0 = S.Task('aND2_mem0', length=1, delay_cost=1)
	aND2_mem0 += MAIN_MEM_r[0]
	S += aND2_mem0 <= aND2

	aND2_mem1 = S.Task('aND2_mem1', length=1, delay_cost=1)
	aND2_mem1 += alt(MM_MEM)
	S += (ND2*MM[0])-1 < aND2_mem1*MM_MEM[1]
	S += aND2_mem1 <= aND2

	bD3_in = S.Task('bD3_in', length=1, delay_cost=1)
	bD3_in += alt(MM_in)
	bD3 = S.Task('bD3', length=5, delay_cost=1)
	bD3 += alt(MM)
	S += bD3>=bD3_in

	bD3_mem0 = S.Task('bD3_mem0', length=1, delay_cost=1)
	bD3_mem0 += MAIN_MEM_r[0]
	S += bD3_mem0 <= bD3

	bD3_mem1 = S.Task('bD3_mem1', length=1, delay_cost=1)
	bD3_mem1 += alt(MM_MEM)
	S += (V*MM[0])-1 < bD3_mem1*MM_MEM[1]
	S += bD3_mem1 <= bD3

	V2_in = S.Task('V2_in', length=1, delay_cost=1)
	V2_in += alt(MM_in)
	V2 = S.Task('V2', length=5, delay_cost=1)
	V2 += alt(MM)
	S += V2>=V2_in

	V2_mem0 = S.Task('V2_mem0', length=1, delay_cost=1)
	V2_mem0 += alt(MM_MEM)
	S += (V*MM[0])-1 < V2_mem0*MM_MEM[0]
	S += V2_mem0 <= V2

	U_ = S.Task('U_', length=1, delay_cost=1)
	U_ += alt(MAS)

	U__mem0 = S.Task('U__mem0', length=1, delay_cost=1)
	U__mem0 += alt(MM_MEM)
	S += (N3*MM[0])-1 < U__mem0*MM_MEM[0]
	S += U__mem0 <= U_

	U__mem1 = S.Task('U__mem1', length=1, delay_cost=1)
	U__mem1 += alt(MM_MEM)
	S += (aND2*MM[0])-1 < U__mem1*MM_MEM[1]
	S += U__mem1 <= U_

	U = S.Task('U', length=1, delay_cost=1)
	U += alt(MAS)

	U_mem0 = S.Task('U_mem0', length=1, delay_cost=1)
	U_mem0 += alt(MAS_MEM)
	S += (U_*MAS[0])-1 < U_mem0*MAS_MEM[0]
	S += (U_*MAS[1])-1 < U_mem0*MAS_MEM[2]
	S += (U_*MAS[2])-1 < U_mem0*MAS_MEM[4]
	S += (U_*MAS[3])-1 < U_mem0*MAS_MEM[6]
	S += U_mem0 <= U

	U_mem1 = S.Task('U_mem1', length=1, delay_cost=1)
	U_mem1 += alt(MM_MEM)
	S += (bD3*MM[0])-1 < U_mem1*MM_MEM[1]
	S += U_mem1 <= U

	UV_in = S.Task('UV_in', length=1, delay_cost=1)
	UV_in += alt(MM_in)
	UV = S.Task('UV', length=5, delay_cost=1)
	UV += alt(MM)
	S += UV>=UV_in

	UV_mem0 = S.Task('UV_mem0', length=1, delay_cost=1)
	UV_mem0 += alt(MAS_MEM)
	S += (U*MAS[0])-1 < UV_mem0*MAS_MEM[0]
	S += (U*MAS[1])-1 < UV_mem0*MAS_MEM[2]
	S += (U*MAS[2])-1 < UV_mem0*MAS_MEM[4]
	S += (U*MAS[3])-1 < UV_mem0*MAS_MEM[6]
	S += UV_mem0 <= UV

	UV_mem1 = S.Task('UV_mem1', length=1, delay_cost=1)
	UV_mem1 += alt(MM_MEM)
	S += (V*MM[0])-1 < UV_mem1*MM_MEM[1]
	S += UV_mem1 <= UV

	UV3_in = S.Task('UV3_in', length=1, delay_cost=1)
	UV3_in += alt(MM_in)
	UV3 = S.Task('UV3', length=5, delay_cost=1)
	UV3 += alt(MM)
	S += UV3>=UV3_in

	S += 0<UV3

	UV3_w = S.Task('UV3_w', length=1, delay_cost=1)
	UV3_w += alt(MAIN_MEM_w)
	S += UV3 <= UV3_w

	UV3_mem0 = S.Task('UV3_mem0', length=1, delay_cost=1)
	UV3_mem0 += alt(MM_MEM)
	S += (UV*MM[0])-1 < UV3_mem0*MM_MEM[0]
	S += UV3_mem0 <= UV3

	UV3_mem1 = S.Task('UV3_mem1', length=1, delay_cost=1)
	UV3_mem1 += alt(MM_MEM)
	S += (V2*MM[0])-1 < UV3_mem1*MM_MEM[1]
	S += UV3_mem1 <= UV3

	solvers.mip.solve(S,msg=1,ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage1MAS4/SSWU_BEFORE_EXP/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

