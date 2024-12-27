from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 131
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=8)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=8, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=16)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t0_in = S.Task('t0_in', length=1, delay_cost=1)
	S += t0_in >= 1
	t0_in += MM_in[1]

	t0_mem0 = S.Task('t0_mem0', length=1, delay_cost=1)
	S += t0_mem0 >= 1
	t0_mem0 += MAIN_MEM_r[0]

	t0_mem1 = S.Task('t0_mem1', length=1, delay_cost=1)
	S += t0_mem1 >= 1
	t0_mem1 += MAIN_MEM_r[1]

	t0 = S.Task('t0', length=10, delay_cost=1)
	S += t0 >= 2
	t0 += MM[1]

	t4_in = S.Task('t4_in', length=1, delay_cost=1)
	S += t4_in >= 5
	t4_in += MAS_in[7]

	t4_mem0 = S.Task('t4_mem0', length=1, delay_cost=1)
	S += t4_mem0 >= 5
	t4_mem0 += MAIN_MEM_r[0]

	t4_mem1 = S.Task('t4_mem1', length=1, delay_cost=1)
	S += t4_mem1 >= 5
	t4_mem1 += MAIN_MEM_r[1]

	t3_in = S.Task('t3_in', length=1, delay_cost=1)
	S += t3_in >= 6
	t3_in += MAS_in[6]

	t3_mem0 = S.Task('t3_mem0', length=1, delay_cost=1)
	S += t3_mem0 >= 6
	t3_mem0 += MAIN_MEM_r[0]

	t3_mem1 = S.Task('t3_mem1', length=1, delay_cost=1)
	S += t3_mem1 >= 6
	t3_mem1 += MAIN_MEM_r[1]

	t4 = S.Task('t4', length=2, delay_cost=1)
	S += t4 >= 6
	t4 += MAS[7]

	t3 = S.Task('t3', length=2, delay_cost=1)
	S += t3 >= 7
	t3 += MAS[6]

	t5_in = S.Task('t5_in', length=1, delay_cost=1)
	S += t5_in >= 8
	t5_in += MM_in[0]

	t5_mem0 = S.Task('t5_mem0', length=1, delay_cost=1)
	S += t5_mem0 >= 8
	t5_mem0 += MAS_MEM[12]

	t5_mem1 = S.Task('t5_mem1', length=1, delay_cost=1)
	S += t5_mem1 >= 8
	t5_mem1 += MAS_MEM[15]

	t8_in = S.Task('t8_in', length=1, delay_cost=1)
	S += t8_in >= 8
	t8_in += MAS_in[6]

	t8_mem0 = S.Task('t8_mem0', length=1, delay_cost=1)
	S += t8_mem0 >= 8
	t8_mem0 += MAIN_MEM_r[0]

	t8_mem1 = S.Task('t8_mem1', length=1, delay_cost=1)
	S += t8_mem1 >= 8
	t8_mem1 += MAIN_MEM_r[1]

	t5 = S.Task('t5', length=10, delay_cost=1)
	S += t5 >= 9
	t5 += MM[0]

	t8 = S.Task('t8', length=2, delay_cost=1)
	S += t8 >= 9
	t8 += MAS[6]


	# new tasks
	t1 = S.Task('t1', length=10, delay_cost=1)
	t1 += alt(MM)
	t1_in = S.Task('t1_in', length=1, delay_cost=1)
	t1_in += alt(MM_in)
	S += t1_in*MM_in[0]<=t1*MM[0]
	S += t1_in*MM_in[1]<=t1*MM[1]
	S += t1<15

	t1_mem0 = S.Task('t1_mem0', length=1, delay_cost=1)
	t1_mem0 += MAIN_MEM_r[0]
	S += t1_mem0 <= t1

	t1_mem1 = S.Task('t1_mem1', length=1, delay_cost=1)
	t1_mem1 += MAIN_MEM_r[1]
	S += t1_mem1 <= t1

	t2 = S.Task('t2', length=10, delay_cost=1)
	t2 += alt(MM)
	t2_in = S.Task('t2_in', length=1, delay_cost=1)
	t2_in += alt(MM_in)
	S += t2_in*MM_in[0]<=t2*MM[0]
	S += t2_in*MM_in[1]<=t2*MM[1]
	S += t2<11

	t2_mem0 = S.Task('t2_mem0', length=1, delay_cost=1)
	t2_mem0 += MAIN_MEM_r[0]
	S += t2_mem0 <= t2

	t2_mem1 = S.Task('t2_mem1', length=1, delay_cost=1)
	t2_mem1 += MAIN_MEM_r[1]
	S += t2_mem1 <= t2

	t9 = S.Task('t9', length=2, delay_cost=1)
	t9 += alt(MAS)
	t9_in = S.Task('t9_in', length=1, delay_cost=1)
	t9_in += alt(MAS_in)
	S += t9_in*MAS_in[0]<=t9*MAS[0]

	S += t9_in*MAS_in[1]<=t9*MAS[1]

	S += t9_in*MAS_in[2]<=t9*MAS[2]

	S += t9_in*MAS_in[3]<=t9*MAS[3]

	S += t9_in*MAS_in[4]<=t9*MAS[4]

	S += t9_in*MAS_in[5]<=t9*MAS[5]

	S += t9_in*MAS_in[6]<=t9*MAS[6]

	S += t9_in*MAS_in[7]<=t9*MAS[7]

	S += t9<11

	t9_mem0 = S.Task('t9_mem0', length=1, delay_cost=1)
	t9_mem0 += MAIN_MEM_r[0]
	S += t9_mem0 <= t9

	t9_mem1 = S.Task('t9_mem1', length=1, delay_cost=1)
	t9_mem1 += MAIN_MEM_r[1]
	S += t9_mem1 <= t9

	t13 = S.Task('t13', length=2, delay_cost=1)
	t13 += alt(MAS)
	t13_in = S.Task('t13_in', length=1, delay_cost=1)
	t13_in += alt(MAS_in)
	S += t13_in*MAS_in[0]<=t13*MAS[0]

	S += t13_in*MAS_in[1]<=t13*MAS[1]

	S += t13_in*MAS_in[2]<=t13*MAS[2]

	S += t13_in*MAS_in[3]<=t13*MAS[3]

	S += t13_in*MAS_in[4]<=t13*MAS[4]

	S += t13_in*MAS_in[5]<=t13*MAS[5]

	S += t13_in*MAS_in[6]<=t13*MAS[6]

	S += t13_in*MAS_in[7]<=t13*MAS[7]

	S += t13<6

	t13_mem0 = S.Task('t13_mem0', length=1, delay_cost=1)
	t13_mem0 += MAIN_MEM_r[0]
	S += t13_mem0 <= t13

	t13_mem1 = S.Task('t13_mem1', length=1, delay_cost=1)
	t13_mem1 += MAIN_MEM_r[1]
	S += t13_mem1 <= t13

	t14 = S.Task('t14', length=2, delay_cost=1)
	t14 += alt(MAS)
	t14_in = S.Task('t14_in', length=1, delay_cost=1)
	t14_in += alt(MAS_in)
	S += t14_in*MAS_in[0]<=t14*MAS[0]

	S += t14_in*MAS_in[1]<=t14*MAS[1]

	S += t14_in*MAS_in[2]<=t14*MAS[2]

	S += t14_in*MAS_in[3]<=t14*MAS[3]

	S += t14_in*MAS_in[4]<=t14*MAS[4]

	S += t14_in*MAS_in[5]<=t14*MAS[5]

	S += t14_in*MAS_in[6]<=t14*MAS[6]

	S += t14_in*MAS_in[7]<=t14*MAS[7]

	S += t14<6

	t14_mem0 = S.Task('t14_mem0', length=1, delay_cost=1)
	t14_mem0 += MAIN_MEM_r[0]
	S += t14_mem0 <= t14

	t14_mem1 = S.Task('t14_mem1', length=1, delay_cost=1)
	t14_mem1 += MAIN_MEM_r[1]
	S += t14_mem1 <= t14

	t6 = S.Task('t6', length=2, delay_cost=1)
	t6 += alt(MAS)
	t6_in = S.Task('t6_in', length=1, delay_cost=1)
	t6_in += alt(MAS_in)
	S += t6_in*MAS_in[0]<=t6*MAS[0]

	S += t6_in*MAS_in[1]<=t6*MAS[1]

	S += t6_in*MAS_in[2]<=t6*MAS[2]

	S += t6_in*MAS_in[3]<=t6*MAS[3]

	S += t6_in*MAS_in[4]<=t6*MAS[4]

	S += t6_in*MAS_in[5]<=t6*MAS[5]

	S += t6_in*MAS_in[6]<=t6*MAS[6]

	S += t6_in*MAS_in[7]<=t6*MAS[7]

	S += t6<1000

	t6_mem0 = S.Task('t6_mem0', length=1, delay_cost=1)
	t6_mem0 += MM_MEM[2]
	S += 11 < t6_mem0
	S += t6_mem0 <= t6

	t6_mem1 = S.Task('t6_mem1', length=1, delay_cost=1)
	t6_mem1 += alt(MM_MEM)
	S += (t1*MM[0])-1 < t6_mem1*MM_MEM[1]
	S += (t1*MM[1])-1 < t6_mem1*MM_MEM[3]
	S += t6_mem1 <= t6

	t10 = S.Task('t10', length=10, delay_cost=1)
	t10 += alt(MM)
	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	t10_in += alt(MM_in)
	S += t10_in*MM_in[0]<=t10*MM[0]
	S += t10_in*MM_in[1]<=t10*MM[1]
	S += t10<21

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += MAS_MEM[12]
	S += 10 < t10_mem0
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += alt(MAS_MEM)
	S += (t9*MAS[0])-1 < t10_mem1*MAS_MEM[1]
	S += (t9*MAS[1])-1 < t10_mem1*MAS_MEM[3]
	S += (t9*MAS[2])-1 < t10_mem1*MAS_MEM[5]
	S += (t9*MAS[3])-1 < t10_mem1*MAS_MEM[7]
	S += (t9*MAS[4])-1 < t10_mem1*MAS_MEM[9]
	S += (t9*MAS[5])-1 < t10_mem1*MAS_MEM[11]
	S += (t9*MAS[6])-1 < t10_mem1*MAS_MEM[13]
	S += (t9*MAS[7])-1 < t10_mem1*MAS_MEM[15]
	S += t10_mem1 <= t10

	t11 = S.Task('t11', length=2, delay_cost=1)
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

	S += t11<21

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += alt(MM_MEM)
	S += (t1*MM[0])-1 < t11_mem0*MM_MEM[0]
	S += (t1*MM[1])-1 < t11_mem0*MM_MEM[2]
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += alt(MM_MEM)
	S += (t2*MM[0])-1 < t11_mem1*MM_MEM[1]
	S += (t2*MM[1])-1 < t11_mem1*MM_MEM[3]
	S += t11_mem1 <= t11

	t15 = S.Task('t15', length=10, delay_cost=1)
	t15 += alt(MM)
	t15_in = S.Task('t15_in', length=1, delay_cost=1)
	t15_in += alt(MM_in)
	S += t15_in*MM_in[0]<=t15*MM[0]
	S += t15_in*MM_in[1]<=t15*MM[1]
	S += t15<16

	t15_mem0 = S.Task('t15_mem0', length=1, delay_cost=1)
	t15_mem0 += alt(MAS_MEM)
	S += (t13*MAS[0])-1 < t15_mem0*MAS_MEM[0]
	S += (t13*MAS[1])-1 < t15_mem0*MAS_MEM[2]
	S += (t13*MAS[2])-1 < t15_mem0*MAS_MEM[4]
	S += (t13*MAS[3])-1 < t15_mem0*MAS_MEM[6]
	S += (t13*MAS[4])-1 < t15_mem0*MAS_MEM[8]
	S += (t13*MAS[5])-1 < t15_mem0*MAS_MEM[10]
	S += (t13*MAS[6])-1 < t15_mem0*MAS_MEM[12]
	S += (t13*MAS[7])-1 < t15_mem0*MAS_MEM[14]
	S += t15_mem0 <= t15

	t15_mem1 = S.Task('t15_mem1', length=1, delay_cost=1)
	t15_mem1 += alt(MAS_MEM)
	S += (t14*MAS[0])-1 < t15_mem1*MAS_MEM[1]
	S += (t14*MAS[1])-1 < t15_mem1*MAS_MEM[3]
	S += (t14*MAS[2])-1 < t15_mem1*MAS_MEM[5]
	S += (t14*MAS[3])-1 < t15_mem1*MAS_MEM[7]
	S += (t14*MAS[4])-1 < t15_mem1*MAS_MEM[9]
	S += (t14*MAS[5])-1 < t15_mem1*MAS_MEM[11]
	S += (t14*MAS[6])-1 < t15_mem1*MAS_MEM[13]
	S += (t14*MAS[7])-1 < t15_mem1*MAS_MEM[15]
	S += t15_mem1 <= t15

	t16 = S.Task('t16', length=2, delay_cost=1)
	t16 += alt(MAS)
	t16_in = S.Task('t16_in', length=1, delay_cost=1)
	t16_in += alt(MAS_in)
	S += t16_in*MAS_in[0]<=t16*MAS[0]

	S += t16_in*MAS_in[1]<=t16*MAS[1]

	S += t16_in*MAS_in[2]<=t16*MAS[2]

	S += t16_in*MAS_in[3]<=t16*MAS[3]

	S += t16_in*MAS_in[4]<=t16*MAS[4]

	S += t16_in*MAS_in[5]<=t16*MAS[5]

	S += t16_in*MAS_in[6]<=t16*MAS[6]

	S += t16_in*MAS_in[7]<=t16*MAS[7]

	S += t16<16

	t16_mem0 = S.Task('t16_mem0', length=1, delay_cost=1)
	t16_mem0 += MM_MEM[2]
	S += 11 < t16_mem0
	S += t16_mem0 <= t16

	t16_mem1 = S.Task('t16_mem1', length=1, delay_cost=1)
	t16_mem1 += alt(MM_MEM)
	S += (t2*MM[0])-1 < t16_mem1*MM_MEM[1]
	S += (t2*MM[1])-1 < t16_mem1*MM_MEM[3]
	S += t16_mem1 <= t16

	t18 = S.Task('t18', length=2, delay_cost=1)
	t18 += alt(MAS)
	t18_in = S.Task('t18_in', length=1, delay_cost=1)
	t18_in += alt(MAS_in)
	S += t18_in*MAS_in[0]<=t18*MAS[0]

	S += t18_in*MAS_in[1]<=t18*MAS[1]

	S += t18_in*MAS_in[2]<=t18*MAS[2]

	S += t18_in*MAS_in[3]<=t18*MAS[3]

	S += t18_in*MAS_in[4]<=t18*MAS[4]

	S += t18_in*MAS_in[5]<=t18*MAS[5]

	S += t18_in*MAS_in[6]<=t18*MAS[6]

	S += t18_in*MAS_in[7]<=t18*MAS[7]

	S += t18<14

	t18_mem0 = S.Task('t18_mem0', length=1, delay_cost=1)
	t18_mem0 += MM_MEM[2]
	S += 11 < t18_mem0
	S += t18_mem0 <= t18

	t18_mem1 = S.Task('t18_mem1', length=1, delay_cost=1)
	t18_mem1 += MM_MEM[3]
	S += 11 < t18_mem1
	S += t18_mem1 <= t18

	t20 = S.Task('t20', length=10, delay_cost=1)
	t20 += alt(MM)
	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	t20_in += alt(MM_in)
	S += t20_in*MM_in[0]<=t20*MM[0]
	S += t20_in*MM_in[1]<=t20*MM[1]
	S += t20<21

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += alt(MM_MEM)
	S += (t2*MM[0])-1 < t20_mem0*MM_MEM[0]
	S += (t2*MM[1])-1 < t20_mem0*MM_MEM[2]
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += MAIN_MEM_r[1]
	S += t20_mem1 <= t20

	t7 = S.Task('t7', length=2, delay_cost=1)
	t7 += alt(MAS)
	t7_in = S.Task('t7_in', length=1, delay_cost=1)
	t7_in += alt(MAS_in)
	S += t7_in*MAS_in[0]<=t7*MAS[0]

	S += t7_in*MAS_in[1]<=t7*MAS[1]

	S += t7_in*MAS_in[2]<=t7*MAS[2]

	S += t7_in*MAS_in[3]<=t7*MAS[3]

	S += t7_in*MAS_in[4]<=t7*MAS[4]

	S += t7_in*MAS_in[5]<=t7*MAS[5]

	S += t7_in*MAS_in[6]<=t7*MAS[6]

	S += t7_in*MAS_in[7]<=t7*MAS[7]

	S += t7<21

	t7_mem0 = S.Task('t7_mem0', length=1, delay_cost=1)
	t7_mem0 += MM_MEM[0]
	S += 18 < t7_mem0
	S += t7_mem0 <= t7

	t7_mem1 = S.Task('t7_mem1', length=1, delay_cost=1)
	t7_mem1 += alt(MAS_MEM)
	S += (t6*MAS[0])-1 < t7_mem1*MAS_MEM[1]
	S += (t6*MAS[1])-1 < t7_mem1*MAS_MEM[3]
	S += (t6*MAS[2])-1 < t7_mem1*MAS_MEM[5]
	S += (t6*MAS[3])-1 < t7_mem1*MAS_MEM[7]
	S += (t6*MAS[4])-1 < t7_mem1*MAS_MEM[9]
	S += (t6*MAS[5])-1 < t7_mem1*MAS_MEM[11]
	S += (t6*MAS[6])-1 < t7_mem1*MAS_MEM[13]
	S += (t6*MAS[7])-1 < t7_mem1*MAS_MEM[15]
	S += t7_mem1 <= t7

	t12 = S.Task('t12', length=2, delay_cost=1)
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

	S += t12<24

	t12_mem0 = S.Task('t12_mem0', length=1, delay_cost=1)
	t12_mem0 += alt(MM_MEM)
	S += (t10*MM[0])-1 < t12_mem0*MM_MEM[0]
	S += (t10*MM[1])-1 < t12_mem0*MM_MEM[2]
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

	t17 = S.Task('t17', length=2, delay_cost=1)
	t17 += alt(MAS)
	t17_in = S.Task('t17_in', length=1, delay_cost=1)
	t17_in += alt(MAS_in)
	S += t17_in*MAS_in[0]<=t17*MAS[0]

	S += t17_in*MAS_in[1]<=t17*MAS[1]

	S += t17_in*MAS_in[2]<=t17*MAS[2]

	S += t17_in*MAS_in[3]<=t17*MAS[3]

	S += t17_in*MAS_in[4]<=t17*MAS[4]

	S += t17_in*MAS_in[5]<=t17*MAS[5]

	S += t17_in*MAS_in[6]<=t17*MAS[6]

	S += t17_in*MAS_in[7]<=t17*MAS[7]

	S += t17<18

	t17_mem0 = S.Task('t17_mem0', length=1, delay_cost=1)
	t17_mem0 += alt(MM_MEM)
	S += (t15*MM[0])-1 < t17_mem0*MM_MEM[0]
	S += (t15*MM[1])-1 < t17_mem0*MM_MEM[2]
	S += t17_mem0 <= t17

	t17_mem1 = S.Task('t17_mem1', length=1, delay_cost=1)
	t17_mem1 += alt(MAS_MEM)
	S += (t16*MAS[0])-1 < t17_mem1*MAS_MEM[1]
	S += (t16*MAS[1])-1 < t17_mem1*MAS_MEM[3]
	S += (t16*MAS[2])-1 < t17_mem1*MAS_MEM[5]
	S += (t16*MAS[3])-1 < t17_mem1*MAS_MEM[7]
	S += (t16*MAS[4])-1 < t17_mem1*MAS_MEM[9]
	S += (t16*MAS[5])-1 < t17_mem1*MAS_MEM[11]
	S += (t16*MAS[6])-1 < t17_mem1*MAS_MEM[13]
	S += (t16*MAS[7])-1 < t17_mem1*MAS_MEM[15]
	S += t17_mem1 <= t17

	t19 = S.Task('t19', length=2, delay_cost=1)
	t19 += alt(MAS)
	t19_in = S.Task('t19_in', length=1, delay_cost=1)
	t19_in += alt(MAS_in)
	S += t19_in*MAS_in[0]<=t19*MAS[0]

	S += t19_in*MAS_in[1]<=t19*MAS[1]

	S += t19_in*MAS_in[2]<=t19*MAS[2]

	S += t19_in*MAS_in[3]<=t19*MAS[3]

	S += t19_in*MAS_in[4]<=t19*MAS[4]

	S += t19_in*MAS_in[5]<=t19*MAS[5]

	S += t19_in*MAS_in[6]<=t19*MAS[6]

	S += t19_in*MAS_in[7]<=t19*MAS[7]

	S += t19<21

	t19_mem0 = S.Task('t19_mem0', length=1, delay_cost=1)
	t19_mem0 += MM_MEM[2]
	S += 11 < t19_mem0
	S += t19_mem0 <= t19

	t19_mem1 = S.Task('t19_mem1', length=1, delay_cost=1)
	t19_mem1 += alt(MAS_MEM)
	S += (t18*MAS[0])-1 < t19_mem1*MAS_MEM[1]
	S += (t18*MAS[1])-1 < t19_mem1*MAS_MEM[3]
	S += (t18*MAS[2])-1 < t19_mem1*MAS_MEM[5]
	S += (t18*MAS[3])-1 < t19_mem1*MAS_MEM[7]
	S += (t18*MAS[4])-1 < t19_mem1*MAS_MEM[9]
	S += (t18*MAS[5])-1 < t19_mem1*MAS_MEM[11]
	S += (t18*MAS[6])-1 < t19_mem1*MAS_MEM[13]
	S += (t18*MAS[7])-1 < t19_mem1*MAS_MEM[15]
	S += t19_mem1 <= t19

	t21 = S.Task('t21', length=2, delay_cost=1)
	t21 += alt(MAS)
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	t21_in += alt(MAS_in)
	S += t21_in*MAS_in[0]<=t21*MAS[0]

	S += t21_in*MAS_in[1]<=t21*MAS[1]

	S += t21_in*MAS_in[2]<=t21*MAS[2]

	S += t21_in*MAS_in[3]<=t21*MAS[3]

	S += t21_in*MAS_in[4]<=t21*MAS[4]

	S += t21_in*MAS_in[5]<=t21*MAS[5]

	S += t21_in*MAS_in[6]<=t21*MAS[6]

	S += t21_in*MAS_in[7]<=t21*MAS[7]

	S += t21<24

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += alt(MM_MEM)
	S += (t1*MM[0])-1 < t21_mem0*MM_MEM[0]
	S += (t1*MM[1])-1 < t21_mem0*MM_MEM[2]
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += alt(MM_MEM)
	S += (t20*MM[0])-1 < t21_mem1*MM_MEM[1]
	S += (t20*MM[1])-1 < t21_mem1*MM_MEM[3]
	S += t21_mem1 <= t21

	t22 = S.Task('t22', length=2, delay_cost=1)
	t22 += alt(MAS)
	t22_in = S.Task('t22_in', length=1, delay_cost=1)
	t22_in += alt(MAS_in)
	S += t22_in*MAS_in[0]<=t22*MAS[0]

	S += t22_in*MAS_in[1]<=t22*MAS[1]

	S += t22_in*MAS_in[2]<=t22*MAS[2]

	S += t22_in*MAS_in[3]<=t22*MAS[3]

	S += t22_in*MAS_in[4]<=t22*MAS[4]

	S += t22_in*MAS_in[5]<=t22*MAS[5]

	S += t22_in*MAS_in[6]<=t22*MAS[6]

	S += t22_in*MAS_in[7]<=t22*MAS[7]

	S += t22<23

	t22_mem0 = S.Task('t22_mem0', length=1, delay_cost=1)
	t22_mem0 += alt(MM_MEM)
	S += (t1*MM[0])-1 < t22_mem0*MM_MEM[0]
	S += (t1*MM[1])-1 < t22_mem0*MM_MEM[2]
	S += t22_mem0 <= t22

	t22_mem1 = S.Task('t22_mem1', length=1, delay_cost=1)
	t22_mem1 += alt(MM_MEM)
	S += (t20*MM[0])-1 < t22_mem1*MM_MEM[1]
	S += (t20*MM[1])-1 < t22_mem1*MM_MEM[3]
	S += t22_mem1 <= t22

	t23 = S.Task('t23', length=10, delay_cost=1)
	t23 += alt(MM)
	t23_in = S.Task('t23_in', length=1, delay_cost=1)
	t23_in += alt(MM_in)
	S += t23_in*MM_in[0]<=t23*MM[0]
	S += t23_in*MM_in[1]<=t23*MM[1]
	S += t23<1000

	t23_mem0 = S.Task('t23_mem0', length=1, delay_cost=1)
	t23_mem0 += alt(MAS_MEM)
	S += (t17*MAS[0])-1 < t23_mem0*MAS_MEM[0]
	S += (t17*MAS[1])-1 < t23_mem0*MAS_MEM[2]
	S += (t17*MAS[2])-1 < t23_mem0*MAS_MEM[4]
	S += (t17*MAS[3])-1 < t23_mem0*MAS_MEM[6]
	S += (t17*MAS[4])-1 < t23_mem0*MAS_MEM[8]
	S += (t17*MAS[5])-1 < t23_mem0*MAS_MEM[10]
	S += (t17*MAS[6])-1 < t23_mem0*MAS_MEM[12]
	S += (t17*MAS[7])-1 < t23_mem0*MAS_MEM[14]
	S += t23_mem0 <= t23

	t23_mem1 = S.Task('t23_mem1', length=1, delay_cost=1)
	t23_mem1 += MAIN_MEM_r[1]
	S += t23_mem1 <= t23

	t25 = S.Task('t25', length=10, delay_cost=1)
	t25 += alt(MM)
	t25_in = S.Task('t25_in', length=1, delay_cost=1)
	t25_in += alt(MM_in)
	S += t25_in*MM_in[0]<=t25*MM[0]
	S += t25_in*MM_in[1]<=t25*MM[1]
	S += t25<1000

	t25_mem0 = S.Task('t25_mem0', length=1, delay_cost=1)
	t25_mem0 += alt(MAS_MEM)
	S += (t7*MAS[0])-1 < t25_mem0*MAS_MEM[0]
	S += (t7*MAS[1])-1 < t25_mem0*MAS_MEM[2]
	S += (t7*MAS[2])-1 < t25_mem0*MAS_MEM[4]
	S += (t7*MAS[3])-1 < t25_mem0*MAS_MEM[6]
	S += (t7*MAS[4])-1 < t25_mem0*MAS_MEM[8]
	S += (t7*MAS[5])-1 < t25_mem0*MAS_MEM[10]
	S += (t7*MAS[6])-1 < t25_mem0*MAS_MEM[12]
	S += (t7*MAS[7])-1 < t25_mem0*MAS_MEM[14]
	S += t25_mem0 <= t25

	t25_mem1 = S.Task('t25_mem1', length=1, delay_cost=1)
	t25_mem1 += alt(MAS_MEM)
	S += (t22*MAS[0])-1 < t25_mem1*MAS_MEM[1]
	S += (t22*MAS[1])-1 < t25_mem1*MAS_MEM[3]
	S += (t22*MAS[2])-1 < t25_mem1*MAS_MEM[5]
	S += (t22*MAS[3])-1 < t25_mem1*MAS_MEM[7]
	S += (t22*MAS[4])-1 < t25_mem1*MAS_MEM[9]
	S += (t22*MAS[5])-1 < t25_mem1*MAS_MEM[11]
	S += (t22*MAS[6])-1 < t25_mem1*MAS_MEM[13]
	S += (t22*MAS[7])-1 < t25_mem1*MAS_MEM[15]
	S += t25_mem1 <= t25

	t27 = S.Task('t27', length=10, delay_cost=1)
	t27 += alt(MM)
	t27_in = S.Task('t27_in', length=1, delay_cost=1)
	t27_in += alt(MM_in)
	S += t27_in*MM_in[0]<=t27*MM[0]
	S += t27_in*MM_in[1]<=t27*MM[1]
	S += t27<1000

	t27_mem0 = S.Task('t27_mem0', length=1, delay_cost=1)
	t27_mem0 += alt(MAS_MEM)
	S += (t22*MAS[0])-1 < t27_mem0*MAS_MEM[0]
	S += (t22*MAS[1])-1 < t27_mem0*MAS_MEM[2]
	S += (t22*MAS[2])-1 < t27_mem0*MAS_MEM[4]
	S += (t22*MAS[3])-1 < t27_mem0*MAS_MEM[6]
	S += (t22*MAS[4])-1 < t27_mem0*MAS_MEM[8]
	S += (t22*MAS[5])-1 < t27_mem0*MAS_MEM[10]
	S += (t22*MAS[6])-1 < t27_mem0*MAS_MEM[12]
	S += (t22*MAS[7])-1 < t27_mem0*MAS_MEM[14]
	S += t27_mem0 <= t27

	t27_mem1 = S.Task('t27_mem1', length=1, delay_cost=1)
	t27_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t27_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t27_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t27_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t27_mem1*MAS_MEM[7]
	S += (t21*MAS[4])-1 < t27_mem1*MAS_MEM[9]
	S += (t21*MAS[5])-1 < t27_mem1*MAS_MEM[11]
	S += (t21*MAS[6])-1 < t27_mem1*MAS_MEM[13]
	S += (t21*MAS[7])-1 < t27_mem1*MAS_MEM[15]
	S += t27_mem1 <= t27

	t28 = S.Task('t28', length=10, delay_cost=1)
	t28 += alt(MM)
	t28_in = S.Task('t28_in', length=1, delay_cost=1)
	t28_in += alt(MM_in)
	S += t28_in*MM_in[0]<=t28*MM[0]
	S += t28_in*MM_in[1]<=t28*MM[1]
	S += t28<1000

	t28_mem0 = S.Task('t28_mem0', length=1, delay_cost=1)
	t28_mem0 += alt(MAS_MEM)
	S += (t19*MAS[0])-1 < t28_mem0*MAS_MEM[0]
	S += (t19*MAS[1])-1 < t28_mem0*MAS_MEM[2]
	S += (t19*MAS[2])-1 < t28_mem0*MAS_MEM[4]
	S += (t19*MAS[3])-1 < t28_mem0*MAS_MEM[6]
	S += (t19*MAS[4])-1 < t28_mem0*MAS_MEM[8]
	S += (t19*MAS[5])-1 < t28_mem0*MAS_MEM[10]
	S += (t19*MAS[6])-1 < t28_mem0*MAS_MEM[12]
	S += (t19*MAS[7])-1 < t28_mem0*MAS_MEM[14]
	S += t28_mem0 <= t28

	t28_mem1 = S.Task('t28_mem1', length=1, delay_cost=1)
	t28_mem1 += alt(MAS_MEM)
	S += (t7*MAS[0])-1 < t28_mem1*MAS_MEM[1]
	S += (t7*MAS[1])-1 < t28_mem1*MAS_MEM[3]
	S += (t7*MAS[2])-1 < t28_mem1*MAS_MEM[5]
	S += (t7*MAS[3])-1 < t28_mem1*MAS_MEM[7]
	S += (t7*MAS[4])-1 < t28_mem1*MAS_MEM[9]
	S += (t7*MAS[5])-1 < t28_mem1*MAS_MEM[11]
	S += (t7*MAS[6])-1 < t28_mem1*MAS_MEM[13]
	S += (t7*MAS[7])-1 < t28_mem1*MAS_MEM[15]
	S += t28_mem1 <= t28

	t29 = S.Task('t29', length=10, delay_cost=1)
	t29 += alt(MM)
	t29_in = S.Task('t29_in', length=1, delay_cost=1)
	t29_in += alt(MM_in)
	S += t29_in*MM_in[0]<=t29*MM[0]
	S += t29_in*MM_in[1]<=t29*MM[1]
	S += t29<1000

	t29_mem0 = S.Task('t29_mem0', length=1, delay_cost=1)
	t29_mem0 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t29_mem0*MAS_MEM[0]
	S += (t21*MAS[1])-1 < t29_mem0*MAS_MEM[2]
	S += (t21*MAS[2])-1 < t29_mem0*MAS_MEM[4]
	S += (t21*MAS[3])-1 < t29_mem0*MAS_MEM[6]
	S += (t21*MAS[4])-1 < t29_mem0*MAS_MEM[8]
	S += (t21*MAS[5])-1 < t29_mem0*MAS_MEM[10]
	S += (t21*MAS[6])-1 < t29_mem0*MAS_MEM[12]
	S += (t21*MAS[7])-1 < t29_mem0*MAS_MEM[14]
	S += t29_mem0 <= t29

	t29_mem1 = S.Task('t29_mem1', length=1, delay_cost=1)
	t29_mem1 += alt(MAS_MEM)
	S += (t12*MAS[0])-1 < t29_mem1*MAS_MEM[1]
	S += (t12*MAS[1])-1 < t29_mem1*MAS_MEM[3]
	S += (t12*MAS[2])-1 < t29_mem1*MAS_MEM[5]
	S += (t12*MAS[3])-1 < t29_mem1*MAS_MEM[7]
	S += (t12*MAS[4])-1 < t29_mem1*MAS_MEM[9]
	S += (t12*MAS[5])-1 < t29_mem1*MAS_MEM[11]
	S += (t12*MAS[6])-1 < t29_mem1*MAS_MEM[13]
	S += (t12*MAS[7])-1 < t29_mem1*MAS_MEM[15]
	S += t29_mem1 <= t29

	t24 = S.Task('t24', length=10, delay_cost=1)
	t24 += alt(MM)
	t24_in = S.Task('t24_in', length=1, delay_cost=1)
	t24_in += alt(MM_in)
	S += t24_in*MM_in[0]<=t24*MM[0]
	S += t24_in*MM_in[1]<=t24*MM[1]
	t24_mem0 = S.Task('t24_mem0', length=1, delay_cost=1)
	t24_mem0 += alt(MAS_MEM)
	S += (t12*MAS[0])-1 < t24_mem0*MAS_MEM[0]
	S += (t12*MAS[1])-1 < t24_mem0*MAS_MEM[2]
	S += (t12*MAS[2])-1 < t24_mem0*MAS_MEM[4]
	S += (t12*MAS[3])-1 < t24_mem0*MAS_MEM[6]
	S += (t12*MAS[4])-1 < t24_mem0*MAS_MEM[8]
	S += (t12*MAS[5])-1 < t24_mem0*MAS_MEM[10]
	S += (t12*MAS[6])-1 < t24_mem0*MAS_MEM[12]
	S += (t12*MAS[7])-1 < t24_mem0*MAS_MEM[14]
	S += t24_mem0 <= t24

	t24_mem1 = S.Task('t24_mem1', length=1, delay_cost=1)
	t24_mem1 += alt(MM_MEM)
	S += (t23*MM[0])-1 < t24_mem1*MM_MEM[1]
	S += (t23*MM[1])-1 < t24_mem1*MM_MEM[3]
	S += t24_mem1 <= t24

	t26 = S.Task('t26', length=10, delay_cost=1)
	t26 += alt(MM)
	t26_in = S.Task('t26_in', length=1, delay_cost=1)
	t26_in += alt(MM_in)
	S += t26_in*MM_in[0]<=t26*MM[0]
	S += t26_in*MM_in[1]<=t26*MM[1]
	t26_mem0 = S.Task('t26_mem0', length=1, delay_cost=1)
	t26_mem0 += alt(MAS_MEM)
	S += (t19*MAS[0])-1 < t26_mem0*MAS_MEM[0]
	S += (t19*MAS[1])-1 < t26_mem0*MAS_MEM[2]
	S += (t19*MAS[2])-1 < t26_mem0*MAS_MEM[4]
	S += (t19*MAS[3])-1 < t26_mem0*MAS_MEM[6]
	S += (t19*MAS[4])-1 < t26_mem0*MAS_MEM[8]
	S += (t19*MAS[5])-1 < t26_mem0*MAS_MEM[10]
	S += (t19*MAS[6])-1 < t26_mem0*MAS_MEM[12]
	S += (t19*MAS[7])-1 < t26_mem0*MAS_MEM[14]
	S += t26_mem0 <= t26

	t26_mem1 = S.Task('t26_mem1', length=1, delay_cost=1)
	t26_mem1 += alt(MM_MEM)
	S += (t23*MM[0])-1 < t26_mem1*MM_MEM[1]
	S += (t23*MM[1])-1 < t26_mem1*MM_MEM[3]
	S += t26_mem1 <= t26

	PZ_new = S.Task('PZ_new', length=10, delay_cost=1)
	PZ_new += alt(MM)
	PZ_new_in = S.Task('PZ_new_in', length=1, delay_cost=1)
	PZ_new_in += alt(MM_in)
	S += PZ_new_in*MM_in[0]<=PZ_new*MM[0]
	S += PZ_new_in*MM_in[1]<=PZ_new*MM[1]
	S += 0<PZ_new

	PZ_new_w = S.Task('PZ_new_w', length=1, delay_cost=1)
	PZ_new_w += alt(MAIN_MEM_w)
	S += PZ_new <= PZ_new_w

	PZ_new_mem0 = S.Task('PZ_new_mem0', length=1, delay_cost=1)
	PZ_new_mem0 += alt(MM_MEM)
	S += (t29*MM[0])-1 < PZ_new_mem0*MM_MEM[0]
	S += (t29*MM[1])-1 < PZ_new_mem0*MM_MEM[2]
	S += PZ_new_mem0 <= PZ_new

	PZ_new_mem1 = S.Task('PZ_new_mem1', length=1, delay_cost=1)
	PZ_new_mem1 += alt(MM_MEM)
	S += (t28*MM[0])-1 < PZ_new_mem1*MM_MEM[1]
	S += (t28*MM[1])-1 < PZ_new_mem1*MM_MEM[3]
	S += PZ_new_mem1 <= PZ_new

	PX_new = S.Task('PX_new', length=2, delay_cost=1)
	PX_new += alt(MAS)
	PX_new_in = S.Task('PX_new_in', length=1, delay_cost=1)
	PX_new_in += alt(MAS_in)
	S += PX_new_in*MAS_in[0]<=PX_new*MAS[0]

	S += PX_new_in*MAS_in[1]<=PX_new*MAS[1]

	S += PX_new_in*MAS_in[2]<=PX_new*MAS[2]

	S += PX_new_in*MAS_in[3]<=PX_new*MAS[3]

	S += PX_new_in*MAS_in[4]<=PX_new*MAS[4]

	S += PX_new_in*MAS_in[5]<=PX_new*MAS[5]

	S += PX_new_in*MAS_in[6]<=PX_new*MAS[6]

	S += PX_new_in*MAS_in[7]<=PX_new*MAS[7]

	S += 0<PX_new

	PX_new_w = S.Task('PX_new_w', length=1, delay_cost=1)
	PX_new_w += alt(MAIN_MEM_w)
	S += PX_new <= PX_new_w

	PX_new_mem0 = S.Task('PX_new_mem0', length=1, delay_cost=1)
	PX_new_mem0 += alt(MM_MEM)
	S += (t25*MM[0])-1 < PX_new_mem0*MM_MEM[0]
	S += (t25*MM[1])-1 < PX_new_mem0*MM_MEM[2]
	S += PX_new_mem0 <= PX_new

	PX_new_mem1 = S.Task('PX_new_mem1', length=1, delay_cost=1)
	PX_new_mem1 += alt(MM_MEM)
	S += (t24*MM[0])-1 < PX_new_mem1*MM_MEM[1]
	S += (t24*MM[1])-1 < PX_new_mem1*MM_MEM[3]
	S += PX_new_mem1 <= PX_new

	PY_new = S.Task('PY_new', length=2, delay_cost=1)
	PY_new += alt(MAS)
	PY_new_in = S.Task('PY_new_in', length=1, delay_cost=1)
	PY_new_in += alt(MAS_in)
	S += PY_new_in*MAS_in[0]<=PY_new*MAS[0]

	S += PY_new_in*MAS_in[1]<=PY_new*MAS[1]

	S += PY_new_in*MAS_in[2]<=PY_new*MAS[2]

	S += PY_new_in*MAS_in[3]<=PY_new*MAS[3]

	S += PY_new_in*MAS_in[4]<=PY_new*MAS[4]

	S += PY_new_in*MAS_in[5]<=PY_new*MAS[5]

	S += PY_new_in*MAS_in[6]<=PY_new*MAS[6]

	S += PY_new_in*MAS_in[7]<=PY_new*MAS[7]

	S += 0<PY_new

	PY_new_w = S.Task('PY_new_w', length=1, delay_cost=1)
	PY_new_w += alt(MAIN_MEM_w)
	S += PY_new <= PY_new_w

	PY_new_mem0 = S.Task('PY_new_mem0', length=1, delay_cost=1)
	PY_new_mem0 += alt(MM_MEM)
	S += (t27*MM[0])-1 < PY_new_mem0*MM_MEM[0]
	S += (t27*MM[1])-1 < PY_new_mem0*MM_MEM[2]
	S += PY_new_mem0 <= PY_new

	PY_new_mem1 = S.Task('PY_new_mem1', length=1, delay_cost=1)
	PY_new_mem1 += alt(MM_MEM)
	S += (t26*MM[0])-1 < PY_new_mem1*MM_MEM[1]
	S += (t26*MM[1])-1 < PY_new_mem1*MM_MEM[3]
	S += PY_new_mem1 <= PY_new

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage2MAS8/EP_ADD_A_0/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 10))

	return solution

