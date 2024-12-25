from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	T1 = S.Task('T1', length=10, delay_cost=1)
	T1 += alt(MM)
	T1_in = S.Task('T1_in', length=1, delay_cost=1)
	T1_in += alt(MM_in)
	S += T1_in*MM_in[0]<=T1*MM[0]
	S += T1_in*MM_in[1]<=T1*MM[1]
	T1_mem0 = S.Task('T1_mem0', length=1, delay_cost=1)
	T1_mem0 += MAIN_MEM_r[0]
	S += T1_mem0 <= T1

	T1_mem1 = S.Task('T1_mem1', length=1, delay_cost=1)
	T1_mem1 += MAIN_MEM_r[1]
	S += T1_mem1 <= T1

	T2 = S.Task('T2', length=10, delay_cost=1)
	T2 += alt(MM)
	T2_in = S.Task('T2_in', length=1, delay_cost=1)
	T2_in += alt(MM_in)
	S += T2_in*MM_in[0]<=T2*MM[0]
	S += T2_in*MM_in[1]<=T2*MM[1]
	T2_mem0 = S.Task('T2_mem0', length=1, delay_cost=1)
	T2_mem0 += MAIN_MEM_r[0]
	S += T2_mem0 <= T2

	T2_mem1 = S.Task('T2_mem1', length=1, delay_cost=1)
	T2_mem1 += MAIN_MEM_r[1]
	S += T2_mem1 <= T2

	T3 = S.Task('T3', length=10, delay_cost=1)
	T3 += alt(MM)
	T3_in = S.Task('T3_in', length=1, delay_cost=1)
	T3_in += alt(MM_in)
	S += T3_in*MM_in[0]<=T3*MM[0]
	S += T3_in*MM_in[1]<=T3*MM[1]
	T3_mem0 = S.Task('T3_mem0', length=1, delay_cost=1)
	T3_mem0 += MAIN_MEM_r[0]
	S += T3_mem0 <= T3

	T3_mem1 = S.Task('T3_mem1', length=1, delay_cost=1)
	T3_mem1 += MAIN_MEM_r[1]
	S += T3_mem1 <= T3

	T4 = S.Task('T4', length=10, delay_cost=1)
	T4 += alt(MM)
	T4_in = S.Task('T4_in', length=1, delay_cost=1)
	T4_in += alt(MM_in)
	S += T4_in*MM_in[0]<=T4*MM[0]
	S += T4_in*MM_in[1]<=T4*MM[1]
	T4_mem0 = S.Task('T4_mem0', length=1, delay_cost=1)
	T4_mem0 += MAIN_MEM_r[0]
	S += T4_mem0 <= T4

	T4_mem1 = S.Task('T4_mem1', length=1, delay_cost=1)
	T4_mem1 += MAIN_MEM_r[1]
	S += T4_mem1 <= T4

	T5 = S.Task('T5', length=10, delay_cost=1)
	T5 += alt(MM)
	T5_in = S.Task('T5_in', length=1, delay_cost=1)
	T5_in += alt(MM_in)
	S += T5_in*MM_in[0]<=T5*MM[0]
	S += T5_in*MM_in[1]<=T5*MM[1]
	T5_mem0 = S.Task('T5_mem0', length=1, delay_cost=1)
	T5_mem0 += MAIN_MEM_r[0]
	S += T5_mem0 <= T5

	T5_mem1 = S.Task('T5_mem1', length=1, delay_cost=1)
	T5_mem1 += MAIN_MEM_r[1]
	S += T5_mem1 <= T5

	T6 = S.Task('T6', length=10, delay_cost=1)
	T6 += alt(MM)
	T6_in = S.Task('T6_in', length=1, delay_cost=1)
	T6_in += alt(MM_in)
	S += T6_in*MM_in[0]<=T6*MM[0]
	S += T6_in*MM_in[1]<=T6*MM[1]
	T6_mem0 = S.Task('T6_mem0', length=1, delay_cost=1)
	T6_mem0 += MAIN_MEM_r[0]
	S += T6_mem0 <= T6

	T6_mem1 = S.Task('T6_mem1', length=1, delay_cost=1)
	T6_mem1 += MAIN_MEM_r[1]
	S += T6_mem1 <= T6

	T7 = S.Task('T7', length=10, delay_cost=1)
	T7 += alt(MM)
	T7_in = S.Task('T7_in', length=1, delay_cost=1)
	T7_in += alt(MM_in)
	S += T7_in*MM_in[0]<=T7*MM[0]
	S += T7_in*MM_in[1]<=T7*MM[1]
	T7_mem0 = S.Task('T7_mem0', length=1, delay_cost=1)
	T7_mem0 += MAIN_MEM_r[0]
	S += T7_mem0 <= T7

	T7_mem1 = S.Task('T7_mem1', length=1, delay_cost=1)
	T7_mem1 += MAIN_MEM_r[1]
	S += T7_mem1 <= T7

	T8 = S.Task('T8', length=10, delay_cost=1)
	T8 += alt(MM)
	T8_in = S.Task('T8_in', length=1, delay_cost=1)
	T8_in += alt(MM_in)
	S += T8_in*MM_in[0]<=T8*MM[0]
	S += T8_in*MM_in[1]<=T8*MM[1]
	T8_mem0 = S.Task('T8_mem0', length=1, delay_cost=1)
	T8_mem0 += MAIN_MEM_r[0]
	S += T8_mem0 <= T8

	T8_mem1 = S.Task('T8_mem1', length=1, delay_cost=1)
	T8_mem1 += alt(MM_MEM)
	S += (T1*MM[0])-1 < T8_mem1*MM_MEM[1]
	S += (T1*MM[1])-1 < T8_mem1*MM_MEM[3]
	S += T8_mem1 <= T8

	T9 = S.Task('T9', length=10, delay_cost=1)
	T9 += alt(MM)
	T9_in = S.Task('T9_in', length=1, delay_cost=1)
	T9_in += alt(MM_in)
	S += T9_in*MM_in[0]<=T9*MM[0]
	S += T9_in*MM_in[1]<=T9*MM[1]
	T9_mem0 = S.Task('T9_mem0', length=1, delay_cost=1)
	T9_mem0 += MAIN_MEM_r[0]
	S += T9_mem0 <= T9

	T9_mem1 = S.Task('T9_mem1', length=1, delay_cost=1)
	T9_mem1 += alt(MM_MEM)
	S += (T1*MM[0])-1 < T9_mem1*MM_MEM[1]
	S += (T1*MM[1])-1 < T9_mem1*MM_MEM[3]
	S += T9_mem1 <= T9

	T10 = S.Task('T10', length=10, delay_cost=1)
	T10 += alt(MM)
	T10_in = S.Task('T10_in', length=1, delay_cost=1)
	T10_in += alt(MM_in)
	S += T10_in*MM_in[0]<=T10*MM[0]
	S += T10_in*MM_in[1]<=T10*MM[1]
	T10_mem0 = S.Task('T10_mem0', length=1, delay_cost=1)
	T10_mem0 += MAIN_MEM_r[0]
	S += T10_mem0 <= T10

	T10_mem1 = S.Task('T10_mem1', length=1, delay_cost=1)
	T10_mem1 += alt(MM_MEM)
	S += (T3*MM[0])-1 < T10_mem1*MM_MEM[1]
	S += (T3*MM[1])-1 < T10_mem1*MM_MEM[3]
	S += T10_mem1 <= T10

	T11 = S.Task('T11', length=10, delay_cost=1)
	T11 += alt(MM)
	T11_in = S.Task('T11_in', length=1, delay_cost=1)
	T11_in += alt(MM_in)
	S += T11_in*MM_in[0]<=T11*MM[0]
	S += T11_in*MM_in[1]<=T11*MM[1]
	T11_mem0 = S.Task('T11_mem0', length=1, delay_cost=1)
	T11_mem0 += MAIN_MEM_r[0]
	S += T11_mem0 <= T11

	T11_mem1 = S.Task('T11_mem1', length=1, delay_cost=1)
	T11_mem1 += alt(MM_MEM)
	S += (T3*MM[0])-1 < T11_mem1*MM_MEM[1]
	S += (T3*MM[1])-1 < T11_mem1*MM_MEM[3]
	S += T11_mem1 <= T11

	T12 = S.Task('T12', length=4, delay_cost=1)
	T12 += alt(MAS)
	T12_in = S.Task('T12_in', length=1, delay_cost=1)
	T12_in += alt(MAS_in)
	S += T12_in*MAS_in[0]<=T12*MAS[0]

	S += T12_in*MAS_in[1]<=T12*MAS[1]

	S += T12_in*MAS_in[2]<=T12*MAS[2]

	S += T12_in*MAS_in[3]<=T12*MAS[3]

	S += T12_in*MAS_in[4]<=T12*MAS[4]

	S += T12_in*MAS_in[5]<=T12*MAS[5]

	T12_mem0 = S.Task('T12_mem0', length=1, delay_cost=1)
	T12_mem0 += alt(MM_MEM)
	S += (T4*MM[0])-1 < T12_mem0*MM_MEM[0]
	S += (T4*MM[1])-1 < T12_mem0*MM_MEM[2]
	S += T12_mem0 <= T12

	T12_mem1 = S.Task('T12_mem1', length=1, delay_cost=1)
	T12_mem1 += alt(MM_MEM)
	S += (T2*MM[0])-1 < T12_mem1*MM_MEM[1]
	S += (T2*MM[1])-1 < T12_mem1*MM_MEM[3]
	S += T12_mem1 <= T12

	T13 = S.Task('T13', length=4, delay_cost=1)
	T13 += alt(MAS)
	T13_in = S.Task('T13_in', length=1, delay_cost=1)
	T13_in += alt(MAS_in)
	S += T13_in*MAS_in[0]<=T13*MAS[0]

	S += T13_in*MAS_in[1]<=T13*MAS[1]

	S += T13_in*MAS_in[2]<=T13*MAS[2]

	S += T13_in*MAS_in[3]<=T13*MAS[3]

	S += T13_in*MAS_in[4]<=T13*MAS[4]

	S += T13_in*MAS_in[5]<=T13*MAS[5]

	T13_mem0 = S.Task('T13_mem0', length=1, delay_cost=1)
	T13_mem0 += alt(MM_MEM)
	S += (T4*MM[0])-1 < T13_mem0*MM_MEM[0]
	S += (T4*MM[1])-1 < T13_mem0*MM_MEM[2]
	S += T13_mem0 <= T13

	T13_mem1 = S.Task('T13_mem1', length=1, delay_cost=1)
	T13_mem1 += alt(MM_MEM)
	S += (T2*MM[0])-1 < T13_mem1*MM_MEM[1]
	S += (T2*MM[1])-1 < T13_mem1*MM_MEM[3]
	S += T13_mem1 <= T13

	T15 = S.Task('T15', length=4, delay_cost=1)
	T15 += alt(MAS)
	T15_in = S.Task('T15_in', length=1, delay_cost=1)
	T15_in += alt(MAS_in)
	S += T15_in*MAS_in[0]<=T15*MAS[0]

	S += T15_in*MAS_in[1]<=T15*MAS[1]

	S += T15_in*MAS_in[2]<=T15*MAS[2]

	S += T15_in*MAS_in[3]<=T15*MAS[3]

	S += T15_in*MAS_in[4]<=T15*MAS[4]

	S += T15_in*MAS_in[5]<=T15*MAS[5]

	T15_mem0 = S.Task('T15_mem0', length=1, delay_cost=1)
	T15_mem0 += alt(MM_MEM)
	S += (T7*MM[0])-1 < T15_mem0*MM_MEM[0]
	S += (T7*MM[1])-1 < T15_mem0*MM_MEM[2]
	S += T15_mem0 <= T15

	T15_mem1 = S.Task('T15_mem1', length=1, delay_cost=1)
	T15_mem1 += alt(MM_MEM)
	S += (T7*MM[0])-1 < T15_mem1*MM_MEM[1]
	S += (T7*MM[1])-1 < T15_mem1*MM_MEM[3]
	S += T15_mem1 <= T15

	T14 = S.Task('T14', length=10, delay_cost=1)
	T14 += alt(MM)
	T14_in = S.Task('T14_in', length=1, delay_cost=1)
	T14_in += alt(MM_in)
	S += T14_in*MM_in[0]<=T14*MM[0]
	S += T14_in*MM_in[1]<=T14*MM[1]
	T14_mem0 = S.Task('T14_mem0', length=1, delay_cost=1)
	T14_mem0 += alt(MAS_MEM)
	S += (T13*MAS[0])-1 < T14_mem0*MAS_MEM[0]
	S += (T13*MAS[1])-1 < T14_mem0*MAS_MEM[2]
	S += (T13*MAS[2])-1 < T14_mem0*MAS_MEM[4]
	S += (T13*MAS[3])-1 < T14_mem0*MAS_MEM[6]
	S += (T13*MAS[4])-1 < T14_mem0*MAS_MEM[8]
	S += (T13*MAS[5])-1 < T14_mem0*MAS_MEM[10]
	S += T14_mem0 <= T14

	T14_mem1 = S.Task('T14_mem1', length=1, delay_cost=1)
	T14_mem1 += alt(MAS_MEM)
	S += (T13*MAS[0])-1 < T14_mem1*MAS_MEM[1]
	S += (T13*MAS[1])-1 < T14_mem1*MAS_MEM[3]
	S += (T13*MAS[2])-1 < T14_mem1*MAS_MEM[5]
	S += (T13*MAS[3])-1 < T14_mem1*MAS_MEM[7]
	S += (T13*MAS[4])-1 < T14_mem1*MAS_MEM[9]
	S += (T13*MAS[5])-1 < T14_mem1*MAS_MEM[11]
	S += T14_mem1 <= T14

	T16 = S.Task('T16', length=10, delay_cost=1)
	T16 += alt(MM)
	T16_in = S.Task('T16_in', length=1, delay_cost=1)
	T16_in += alt(MM_in)
	S += T16_in*MM_in[0]<=T16*MM[0]
	S += T16_in*MM_in[1]<=T16*MM[1]
	T16_mem0 = S.Task('T16_mem0', length=1, delay_cost=1)
	T16_mem0 += alt(MM_MEM)
	S += (T1*MM[0])-1 < T16_mem0*MM_MEM[0]
	S += (T1*MM[1])-1 < T16_mem0*MM_MEM[2]
	S += T16_mem0 <= T16

	T16_mem1 = S.Task('T16_mem1', length=1, delay_cost=1)
	T16_mem1 += alt(MM_MEM)
	S += (T8*MM[0])-1 < T16_mem1*MM_MEM[1]
	S += (T8*MM[1])-1 < T16_mem1*MM_MEM[3]
	S += T16_mem1 <= T16

	T17 = S.Task('T17', length=10, delay_cost=1)
	T17 += alt(MM)
	T17_in = S.Task('T17_in', length=1, delay_cost=1)
	T17_in += alt(MM_in)
	S += T17_in*MM_in[0]<=T17*MM[0]
	S += T17_in*MM_in[1]<=T17*MM[1]
	T17_mem0 = S.Task('T17_mem0', length=1, delay_cost=1)
	T17_mem0 += alt(MM_MEM)
	S += (T8*MM[0])-1 < T17_mem0*MM_MEM[0]
	S += (T8*MM[1])-1 < T17_mem0*MM_MEM[2]
	S += T17_mem0 <= T17

	T17_mem1 = S.Task('T17_mem1', length=1, delay_cost=1)
	T17_mem1 += alt(MAS_MEM)
	S += (T15*MAS[0])-1 < T17_mem1*MAS_MEM[1]
	S += (T15*MAS[1])-1 < T17_mem1*MAS_MEM[3]
	S += (T15*MAS[2])-1 < T17_mem1*MAS_MEM[5]
	S += (T15*MAS[3])-1 < T17_mem1*MAS_MEM[7]
	S += (T15*MAS[4])-1 < T17_mem1*MAS_MEM[9]
	S += (T15*MAS[5])-1 < T17_mem1*MAS_MEM[11]
	S += T17_mem1 <= T17

	T18 = S.Task('T18', length=4, delay_cost=1)
	T18 += alt(MAS)
	T18_in = S.Task('T18_in', length=1, delay_cost=1)
	T18_in += alt(MAS_in)
	S += T18_in*MAS_in[0]<=T18*MAS[0]

	S += T18_in*MAS_in[1]<=T18*MAS[1]

	S += T18_in*MAS_in[2]<=T18*MAS[2]

	S += T18_in*MAS_in[3]<=T18*MAS[3]

	S += T18_in*MAS_in[4]<=T18*MAS[4]

	S += T18_in*MAS_in[5]<=T18*MAS[5]

	T18_mem0 = S.Task('T18_mem0', length=1, delay_cost=1)
	T18_mem0 += alt(MM_MEM)
	S += (T5*MM[0])-1 < T18_mem0*MM_MEM[0]
	S += (T5*MM[1])-1 < T18_mem0*MM_MEM[2]
	S += T18_mem0 <= T18

	T18_mem1 = S.Task('T18_mem1', length=1, delay_cost=1)
	T18_mem1 += alt(MM_MEM)
	S += (T9*MM[0])-1 < T18_mem1*MM_MEM[1]
	S += (T9*MM[1])-1 < T18_mem1*MM_MEM[3]
	S += T18_mem1 <= T18

	T19 = S.Task('T19', length=4, delay_cost=1)
	T19 += alt(MAS)
	T19_in = S.Task('T19_in', length=1, delay_cost=1)
	T19_in += alt(MAS_in)
	S += T19_in*MAS_in[0]<=T19*MAS[0]

	S += T19_in*MAS_in[1]<=T19*MAS[1]

	S += T19_in*MAS_in[2]<=T19*MAS[2]

	S += T19_in*MAS_in[3]<=T19*MAS[3]

	S += T19_in*MAS_in[4]<=T19*MAS[4]

	S += T19_in*MAS_in[5]<=T19*MAS[5]

	T19_mem0 = S.Task('T19_mem0', length=1, delay_cost=1)
	T19_mem0 += alt(MM_MEM)
	S += (T5*MM[0])-1 < T19_mem0*MM_MEM[0]
	S += (T5*MM[1])-1 < T19_mem0*MM_MEM[2]
	S += T19_mem0 <= T19

	T19_mem1 = S.Task('T19_mem1', length=1, delay_cost=1)
	T19_mem1 += alt(MM_MEM)
	S += (T9*MM[0])-1 < T19_mem1*MM_MEM[1]
	S += (T9*MM[1])-1 < T19_mem1*MM_MEM[3]
	S += T19_mem1 <= T19

	T21 = S.Task('T21', length=4, delay_cost=1)
	T21 += alt(MAS)
	T21_in = S.Task('T21_in', length=1, delay_cost=1)
	T21_in += alt(MAS_in)
	S += T21_in*MAS_in[0]<=T21*MAS[0]

	S += T21_in*MAS_in[1]<=T21*MAS[1]

	S += T21_in*MAS_in[2]<=T21*MAS[2]

	S += T21_in*MAS_in[3]<=T21*MAS[3]

	S += T21_in*MAS_in[4]<=T21*MAS[4]

	S += T21_in*MAS_in[5]<=T21*MAS[5]

	T21_mem0 = S.Task('T21_mem0', length=1, delay_cost=1)
	T21_mem0 += alt(MM_MEM)
	S += (T6*MM[0])-1 < T21_mem0*MM_MEM[0]
	S += (T6*MM[1])-1 < T21_mem0*MM_MEM[2]
	S += T21_mem0 <= T21

	T21_mem1 = S.Task('T21_mem1', length=1, delay_cost=1)
	T21_mem1 += alt(MM_MEM)
	S += (T10*MM[0])-1 < T21_mem1*MM_MEM[1]
	S += (T10*MM[1])-1 < T21_mem1*MM_MEM[3]
	S += T21_mem1 <= T21

	T24 = S.Task('T24', length=10, delay_cost=1)
	T24 += alt(MM)
	T24_in = S.Task('T24_in', length=1, delay_cost=1)
	T24_in += alt(MM_in)
	S += T24_in*MM_in[0]<=T24*MM[0]
	S += T24_in*MM_in[1]<=T24*MM[1]
	T24_mem0 = S.Task('T24_mem0', length=1, delay_cost=1)
	T24_mem0 += alt(MM_MEM)
	S += (T11*MM[0])-1 < T24_mem0*MM_MEM[0]
	S += (T11*MM[1])-1 < T24_mem0*MM_MEM[2]
	S += T24_mem0 <= T24

	T24_mem1 = S.Task('T24_mem1', length=1, delay_cost=1)
	T24_mem1 += alt(MAS_MEM)
	S += (T12*MAS[0])-1 < T24_mem1*MAS_MEM[1]
	S += (T12*MAS[1])-1 < T24_mem1*MAS_MEM[3]
	S += (T12*MAS[2])-1 < T24_mem1*MAS_MEM[5]
	S += (T12*MAS[3])-1 < T24_mem1*MAS_MEM[7]
	S += (T12*MAS[4])-1 < T24_mem1*MAS_MEM[9]
	S += (T12*MAS[5])-1 < T24_mem1*MAS_MEM[11]
	S += T24_mem1 <= T24

	T20 = S.Task('T20', length=10, delay_cost=1)
	T20 += alt(MM)
	T20_in = S.Task('T20_in', length=1, delay_cost=1)
	T20_in += alt(MM_in)
	S += T20_in*MM_in[0]<=T20*MM[0]
	S += T20_in*MM_in[1]<=T20*MM[1]
	T20_mem0 = S.Task('T20_mem0', length=1, delay_cost=1)
	T20_mem0 += alt(MAS_MEM)
	S += (T15*MAS[0])-1 < T20_mem0*MAS_MEM[0]
	S += (T15*MAS[1])-1 < T20_mem0*MAS_MEM[2]
	S += (T15*MAS[2])-1 < T20_mem0*MAS_MEM[4]
	S += (T15*MAS[3])-1 < T20_mem0*MAS_MEM[6]
	S += (T15*MAS[4])-1 < T20_mem0*MAS_MEM[8]
	S += (T15*MAS[5])-1 < T20_mem0*MAS_MEM[10]
	S += T20_mem0 <= T20

	T20_mem1 = S.Task('T20_mem1', length=1, delay_cost=1)
	T20_mem1 += alt(MAS_MEM)
	S += (T18*MAS[0])-1 < T20_mem1*MAS_MEM[1]
	S += (T18*MAS[1])-1 < T20_mem1*MAS_MEM[3]
	S += (T18*MAS[2])-1 < T20_mem1*MAS_MEM[5]
	S += (T18*MAS[3])-1 < T20_mem1*MAS_MEM[7]
	S += (T18*MAS[4])-1 < T20_mem1*MAS_MEM[9]
	S += (T18*MAS[5])-1 < T20_mem1*MAS_MEM[11]
	S += T20_mem1 <= T20

	T22 = S.Task('T22', length=10, delay_cost=1)
	T22 += alt(MM)
	T22_in = S.Task('T22_in', length=1, delay_cost=1)
	T22_in += alt(MM_in)
	S += T22_in*MM_in[0]<=T22*MM[0]
	S += T22_in*MM_in[1]<=T22*MM[1]
	T22_mem0 = S.Task('T22_mem0', length=1, delay_cost=1)
	T22_mem0 += alt(MAS_MEM)
	S += (T21*MAS[0])-1 < T22_mem0*MAS_MEM[0]
	S += (T21*MAS[1])-1 < T22_mem0*MAS_MEM[2]
	S += (T21*MAS[2])-1 < T22_mem0*MAS_MEM[4]
	S += (T21*MAS[3])-1 < T22_mem0*MAS_MEM[6]
	S += (T21*MAS[4])-1 < T22_mem0*MAS_MEM[8]
	S += (T21*MAS[5])-1 < T22_mem0*MAS_MEM[10]
	S += T22_mem0 <= T22

	T22_mem1 = S.Task('T22_mem1', length=1, delay_cost=1)
	T22_mem1 += alt(MAS_MEM)
	S += (T21*MAS[0])-1 < T22_mem1*MAS_MEM[1]
	S += (T21*MAS[1])-1 < T22_mem1*MAS_MEM[3]
	S += (T21*MAS[2])-1 < T22_mem1*MAS_MEM[5]
	S += (T21*MAS[3])-1 < T22_mem1*MAS_MEM[7]
	S += (T21*MAS[4])-1 < T22_mem1*MAS_MEM[9]
	S += (T21*MAS[5])-1 < T22_mem1*MAS_MEM[11]
	S += T22_mem1 <= T22

	T23 = S.Task('T23', length=10, delay_cost=1)
	T23 += alt(MM)
	T23_in = S.Task('T23_in', length=1, delay_cost=1)
	T23_in += alt(MM_in)
	S += T23_in*MM_in[0]<=T23*MM[0]
	S += T23_in*MM_in[1]<=T23*MM[1]
	T23_mem0 = S.Task('T23_mem0', length=1, delay_cost=1)
	T23_mem0 += alt(MAS_MEM)
	S += (T19*MAS[0])-1 < T23_mem0*MAS_MEM[0]
	S += (T19*MAS[1])-1 < T23_mem0*MAS_MEM[2]
	S += (T19*MAS[2])-1 < T23_mem0*MAS_MEM[4]
	S += (T19*MAS[3])-1 < T23_mem0*MAS_MEM[6]
	S += (T19*MAS[4])-1 < T23_mem0*MAS_MEM[8]
	S += (T19*MAS[5])-1 < T23_mem0*MAS_MEM[10]
	S += T23_mem0 <= T23

	T23_mem1 = S.Task('T23_mem1', length=1, delay_cost=1)
	T23_mem1 += alt(MAS_MEM)
	S += (T19*MAS[0])-1 < T23_mem1*MAS_MEM[1]
	S += (T19*MAS[1])-1 < T23_mem1*MAS_MEM[3]
	S += (T19*MAS[2])-1 < T23_mem1*MAS_MEM[5]
	S += (T19*MAS[3])-1 < T23_mem1*MAS_MEM[7]
	S += (T19*MAS[4])-1 < T23_mem1*MAS_MEM[9]
	S += (T19*MAS[5])-1 < T23_mem1*MAS_MEM[11]
	S += T23_mem1 <= T23

	Z2_new = S.Task('Z2_new', length=10, delay_cost=1)
	Z2_new += alt(MM)
	Z2_new_in = S.Task('Z2_new_in', length=1, delay_cost=1)
	Z2_new_in += alt(MM_in)
	S += Z2_new_in*MM_in[0]<=Z2_new*MM[0]
	S += Z2_new_in*MM_in[1]<=Z2_new*MM[1]
	S += 0<Z2_new

	Z2_new_w = S.Task('Z2_new_w', length=1, delay_cost=1)
	Z2_new_w += alt(MAIN_MEM_w)
	S += Z2_new <= Z2_new_w

	Z2_new_mem0 = S.Task('Z2_new_mem0', length=1, delay_cost=1)
	Z2_new_mem0 += MAIN_MEM_r[0]
	S += Z2_new_mem0 <= Z2_new

	Z2_new_mem1 = S.Task('Z2_new_mem1', length=1, delay_cost=1)
	Z2_new_mem1 += alt(MM_MEM)
	S += (T14*MM[0])-1 < Z2_new_mem1*MM_MEM[1]
	S += (T14*MM[1])-1 < Z2_new_mem1*MM_MEM[3]
	S += Z2_new_mem1 <= Z2_new

	T25 = S.Task('T25', length=4, delay_cost=1)
	T25 += alt(MAS)
	T25_in = S.Task('T25_in', length=1, delay_cost=1)
	T25_in += alt(MAS_in)
	S += T25_in*MAS_in[0]<=T25*MAS[0]

	S += T25_in*MAS_in[1]<=T25*MAS[1]

	S += T25_in*MAS_in[2]<=T25*MAS[2]

	S += T25_in*MAS_in[3]<=T25*MAS[3]

	S += T25_in*MAS_in[4]<=T25*MAS[4]

	S += T25_in*MAS_in[5]<=T25*MAS[5]

	T25_mem0 = S.Task('T25_mem0', length=1, delay_cost=1)
	T25_mem0 += alt(MM_MEM)
	S += (T20*MM[0])-1 < T25_mem0*MM_MEM[0]
	S += (T20*MM[1])-1 < T25_mem0*MM_MEM[2]
	S += T25_mem0 <= T25

	T25_mem1 = S.Task('T25_mem1', length=1, delay_cost=1)
	T25_mem1 += alt(MM_MEM)
	S += (T20*MM[0])-1 < T25_mem1*MM_MEM[1]
	S += (T20*MM[1])-1 < T25_mem1*MM_MEM[3]
	S += T25_mem1 <= T25

	X2_new = S.Task('X2_new', length=4, delay_cost=1)
	X2_new += alt(MAS)
	X2_new_in = S.Task('X2_new_in', length=1, delay_cost=1)
	X2_new_in += alt(MAS_in)
	S += X2_new_in*MAS_in[0]<=X2_new*MAS[0]

	S += X2_new_in*MAS_in[1]<=X2_new*MAS[1]

	S += X2_new_in*MAS_in[2]<=X2_new*MAS[2]

	S += X2_new_in*MAS_in[3]<=X2_new*MAS[3]

	S += X2_new_in*MAS_in[4]<=X2_new*MAS[4]

	S += X2_new_in*MAS_in[5]<=X2_new*MAS[5]

	S += 0<X2_new

	X2_new_w = S.Task('X2_new_w', length=1, delay_cost=1)
	X2_new_w += alt(MAIN_MEM_w)
	S += X2_new <= X2_new_w

	X2_new_mem0 = S.Task('X2_new_mem0', length=1, delay_cost=1)
	X2_new_mem0 += alt(MM_MEM)
	S += (T22*MM[0])-1 < X2_new_mem0*MM_MEM[0]
	S += (T22*MM[1])-1 < X2_new_mem0*MM_MEM[2]
	S += X2_new_mem0 <= X2_new

	X2_new_mem1 = S.Task('X2_new_mem1', length=1, delay_cost=1)
	X2_new_mem1 += alt(MM_MEM)
	S += (T24*MM[0])-1 < X2_new_mem1*MM_MEM[1]
	S += (T24*MM[1])-1 < X2_new_mem1*MM_MEM[3]
	S += X2_new_mem1 <= X2_new

	X1_new = S.Task('X1_new', length=4, delay_cost=1)
	X1_new += alt(MAS)
	X1_new_in = S.Task('X1_new_in', length=1, delay_cost=1)
	X1_new_in += alt(MAS_in)
	S += X1_new_in*MAS_in[0]<=X1_new*MAS[0]

	S += X1_new_in*MAS_in[1]<=X1_new*MAS[1]

	S += X1_new_in*MAS_in[2]<=X1_new*MAS[2]

	S += X1_new_in*MAS_in[3]<=X1_new*MAS[3]

	S += X1_new_in*MAS_in[4]<=X1_new*MAS[4]

	S += X1_new_in*MAS_in[5]<=X1_new*MAS[5]

	S += 0<X1_new

	X1_new_w = S.Task('X1_new_w', length=1, delay_cost=1)
	X1_new_w += alt(MAIN_MEM_w)
	S += X1_new <= X1_new_w

	X1_new_mem0 = S.Task('X1_new_mem0', length=1, delay_cost=1)
	X1_new_mem0 += alt(MM_MEM)
	S += (T23*MM[0])-1 < X1_new_mem0*MM_MEM[0]
	S += (T23*MM[1])-1 < X1_new_mem0*MM_MEM[2]
	S += X1_new_mem0 <= X1_new

	X1_new_mem1 = S.Task('X1_new_mem1', length=1, delay_cost=1)
	X1_new_mem1 += alt(MM_MEM)
	S += (T17*MM[0])-1 < X1_new_mem1*MM_MEM[1]
	S += (T17*MM[1])-1 < X1_new_mem1*MM_MEM[3]
	S += X1_new_mem1 <= X1_new

	Z1_new = S.Task('Z1_new', length=4, delay_cost=1)
	Z1_new += alt(MAS)
	Z1_new_in = S.Task('Z1_new_in', length=1, delay_cost=1)
	Z1_new_in += alt(MAS_in)
	S += Z1_new_in*MAS_in[0]<=Z1_new*MAS[0]

	S += Z1_new_in*MAS_in[1]<=Z1_new*MAS[1]

	S += Z1_new_in*MAS_in[2]<=Z1_new*MAS[2]

	S += Z1_new_in*MAS_in[3]<=Z1_new*MAS[3]

	S += Z1_new_in*MAS_in[4]<=Z1_new*MAS[4]

	S += Z1_new_in*MAS_in[5]<=Z1_new*MAS[5]

	S += 0<Z1_new

	Z1_new_w = S.Task('Z1_new_w', length=1, delay_cost=1)
	Z1_new_w += alt(MAIN_MEM_w)
	S += Z1_new <= Z1_new_w

	Z1_new_mem0 = S.Task('Z1_new_mem0', length=1, delay_cost=1)
	Z1_new_mem0 += alt(MM_MEM)
	S += (T16*MM[0])-1 < Z1_new_mem0*MM_MEM[0]
	S += (T16*MM[1])-1 < Z1_new_mem0*MM_MEM[2]
	S += Z1_new_mem0 <= Z1_new

	Z1_new_mem1 = S.Task('Z1_new_mem1', length=1, delay_cost=1)
	Z1_new_mem1 += alt(MAS_MEM)
	S += (T25*MAS[0])-1 < Z1_new_mem1*MAS_MEM[1]
	S += (T25*MAS[1])-1 < Z1_new_mem1*MAS_MEM[3]
	S += (T25*MAS[2])-1 < Z1_new_mem1*MAS_MEM[5]
	S += (T25*MAS[3])-1 < Z1_new_mem1*MAS_MEM[7]
	S += (T25*MAS[4])-1 < Z1_new_mem1*MAS_MEM[9]
	S += (T25*MAS[5])-1 < Z1_new_mem1*MAS_MEM[11]
	S += Z1_new_mem1 <= Z1_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage4MAS6/EP_LADDERMUL/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

