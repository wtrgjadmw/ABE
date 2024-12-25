from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=6)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	t0_t0 = S.Task('t0_t0', length=6, delay_cost=1)
	t0_t0 += alt(MM)
	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	t0_t0_in += alt(MM_in)
	S += t0_t0_in*MM_in[0]<=t0_t0*MM[0]
	S += t0_t0_in*MM_in[1]<=t0_t0*MM[1]
	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	t0_t0_mem0 += MAIN_MEM_r[0]
	S += t0_t0_mem0 <= t0_t0

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	t0_t0_mem1 += MAIN_MEM_r[1]
	S += t0_t0_mem1 <= t0_t0

	t0_t1 = S.Task('t0_t1', length=6, delay_cost=1)
	t0_t1 += alt(MM)
	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	t0_t1_in += alt(MM_in)
	S += t0_t1_in*MM_in[0]<=t0_t1*MM[0]
	S += t0_t1_in*MM_in[1]<=t0_t1*MM[1]
	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	t0_t1_mem0 += MAIN_MEM_r[0]
	S += t0_t1_mem0 <= t0_t1

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	t0_t1_mem1 += MAIN_MEM_r[1]
	S += t0_t1_mem1 <= t0_t1

	t0_t2 = S.Task('t0_t2', length=2, delay_cost=1)
	t0_t2 += alt(MAS)
	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	t0_t2_in += alt(MAS_in)
	S += t0_t2_in*MAS_in[0]<=t0_t2*MAS[0]

	S += t0_t2_in*MAS_in[1]<=t0_t2*MAS[1]

	S += t0_t2_in*MAS_in[2]<=t0_t2*MAS[2]

	S += t0_t2_in*MAS_in[3]<=t0_t2*MAS[3]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	t0_t2_mem0 += MAIN_MEM_r[0]
	S += t0_t2_mem0 <= t0_t2

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	t0_t2_mem1 += MAIN_MEM_r[1]
	S += t0_t2_mem1 <= t0_t2

	t0_t3 = S.Task('t0_t3', length=2, delay_cost=1)
	t0_t3 += alt(MAS)
	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	t0_t3_in += alt(MAS_in)
	S += t0_t3_in*MAS_in[0]<=t0_t3*MAS[0]

	S += t0_t3_in*MAS_in[1]<=t0_t3*MAS[1]

	S += t0_t3_in*MAS_in[2]<=t0_t3*MAS[2]

	S += t0_t3_in*MAS_in[3]<=t0_t3*MAS[3]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	t0_t3_mem0 += MAIN_MEM_r[0]
	S += t0_t3_mem0 <= t0_t3

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	t0_t3_mem1 += MAIN_MEM_r[1]
	S += t0_t3_mem1 <= t0_t3

	t2_t0 = S.Task('t2_t0', length=6, delay_cost=1)
	t2_t0 += alt(MM)
	t2_t0_in = S.Task('t2_t0_in', length=1, delay_cost=1)
	t2_t0_in += alt(MM_in)
	S += t2_t0_in*MM_in[0]<=t2_t0*MM[0]
	S += t2_t0_in*MM_in[1]<=t2_t0*MM[1]
	t2_t0_mem0 = S.Task('t2_t0_mem0', length=1, delay_cost=1)
	t2_t0_mem0 += MAIN_MEM_r[0]
	S += t2_t0_mem0 <= t2_t0

	t2_t0_mem1 = S.Task('t2_t0_mem1', length=1, delay_cost=1)
	t2_t0_mem1 += MAIN_MEM_r[1]
	S += t2_t0_mem1 <= t2_t0

	t2_t1 = S.Task('t2_t1', length=6, delay_cost=1)
	t2_t1 += alt(MM)
	t2_t1_in = S.Task('t2_t1_in', length=1, delay_cost=1)
	t2_t1_in += alt(MM_in)
	S += t2_t1_in*MM_in[0]<=t2_t1*MM[0]
	S += t2_t1_in*MM_in[1]<=t2_t1*MM[1]
	t2_t1_mem0 = S.Task('t2_t1_mem0', length=1, delay_cost=1)
	t2_t1_mem0 += MAIN_MEM_r[0]
	S += t2_t1_mem0 <= t2_t1

	t2_t1_mem1 = S.Task('t2_t1_mem1', length=1, delay_cost=1)
	t2_t1_mem1 += MAIN_MEM_r[1]
	S += t2_t1_mem1 <= t2_t1

	t2_t2 = S.Task('t2_t2', length=2, delay_cost=1)
	t2_t2 += alt(MAS)
	t2_t2_in = S.Task('t2_t2_in', length=1, delay_cost=1)
	t2_t2_in += alt(MAS_in)
	S += t2_t2_in*MAS_in[0]<=t2_t2*MAS[0]

	S += t2_t2_in*MAS_in[1]<=t2_t2*MAS[1]

	S += t2_t2_in*MAS_in[2]<=t2_t2*MAS[2]

	S += t2_t2_in*MAS_in[3]<=t2_t2*MAS[3]

	t2_t2_mem0 = S.Task('t2_t2_mem0', length=1, delay_cost=1)
	t2_t2_mem0 += MAIN_MEM_r[0]
	S += t2_t2_mem0 <= t2_t2

	t2_t2_mem1 = S.Task('t2_t2_mem1', length=1, delay_cost=1)
	t2_t2_mem1 += MAIN_MEM_r[1]
	S += t2_t2_mem1 <= t2_t2

	t2_t3 = S.Task('t2_t3', length=2, delay_cost=1)
	t2_t3 += alt(MAS)
	t2_t3_in = S.Task('t2_t3_in', length=1, delay_cost=1)
	t2_t3_in += alt(MAS_in)
	S += t2_t3_in*MAS_in[0]<=t2_t3*MAS[0]

	S += t2_t3_in*MAS_in[1]<=t2_t3*MAS[1]

	S += t2_t3_in*MAS_in[2]<=t2_t3*MAS[2]

	S += t2_t3_in*MAS_in[3]<=t2_t3*MAS[3]

	t2_t3_mem0 = S.Task('t2_t3_mem0', length=1, delay_cost=1)
	t2_t3_mem0 += MAIN_MEM_r[0]
	S += t2_t3_mem0 <= t2_t3

	t2_t3_mem1 = S.Task('t2_t3_mem1', length=1, delay_cost=1)
	t2_t3_mem1 += MAIN_MEM_r[1]
	S += t2_t3_mem1 <= t2_t3

	t7_t2 = S.Task('t7_t2', length=2, delay_cost=1)
	t7_t2 += alt(MAS)
	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	t7_t2_in += alt(MAS_in)
	S += t7_t2_in*MAS_in[0]<=t7_t2*MAS[0]

	S += t7_t2_in*MAS_in[1]<=t7_t2*MAS[1]

	S += t7_t2_in*MAS_in[2]<=t7_t2*MAS[2]

	S += t7_t2_in*MAS_in[3]<=t7_t2*MAS[3]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	t7_t2_mem0 += MAIN_MEM_r[0]
	S += t7_t2_mem0 <= t7_t2

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	t7_t2_mem1 += MAIN_MEM_r[1]
	S += t7_t2_mem1 <= t7_t2

	t9_t2 = S.Task('t9_t2', length=2, delay_cost=1)
	t9_t2 += alt(MAS)
	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	t9_t2_in += alt(MAS_in)
	S += t9_t2_in*MAS_in[0]<=t9_t2*MAS[0]

	S += t9_t2_in*MAS_in[1]<=t9_t2*MAS[1]

	S += t9_t2_in*MAS_in[2]<=t9_t2*MAS[2]

	S += t9_t2_in*MAS_in[3]<=t9_t2*MAS[3]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	t9_t2_mem0 += MAIN_MEM_r[0]
	S += t9_t2_mem0 <= t9_t2

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	t9_t2_mem1 += MAIN_MEM_r[1]
	S += t9_t2_mem1 <= t9_t2

	t14_t2 = S.Task('t14_t2', length=2, delay_cost=1)
	t14_t2 += alt(MAS)
	t14_t2_in = S.Task('t14_t2_in', length=1, delay_cost=1)
	t14_t2_in += alt(MAS_in)
	S += t14_t2_in*MAS_in[0]<=t14_t2*MAS[0]

	S += t14_t2_in*MAS_in[1]<=t14_t2*MAS[1]

	S += t14_t2_in*MAS_in[2]<=t14_t2*MAS[2]

	S += t14_t2_in*MAS_in[3]<=t14_t2*MAS[3]

	t14_t2_mem0 = S.Task('t14_t2_mem0', length=1, delay_cost=1)
	t14_t2_mem0 += MAIN_MEM_r[0]
	S += t14_t2_mem0 <= t14_t2

	t14_t2_mem1 = S.Task('t14_t2_mem1', length=1, delay_cost=1)
	t14_t2_mem1 += MAIN_MEM_r[1]
	S += t14_t2_mem1 <= t14_t2

	new_TZ_t2 = S.Task('new_TZ_t2', length=2, delay_cost=1)
	new_TZ_t2 += alt(MAS)
	new_TZ_t2_in = S.Task('new_TZ_t2_in', length=1, delay_cost=1)
	new_TZ_t2_in += alt(MAS_in)
	S += new_TZ_t2_in*MAS_in[0]<=new_TZ_t2*MAS[0]

	S += new_TZ_t2_in*MAS_in[1]<=new_TZ_t2*MAS[1]

	S += new_TZ_t2_in*MAS_in[2]<=new_TZ_t2*MAS[2]

	S += new_TZ_t2_in*MAS_in[3]<=new_TZ_t2*MAS[3]

	new_TZ_t2_mem0 = S.Task('new_TZ_t2_mem0', length=1, delay_cost=1)
	new_TZ_t2_mem0 += MAIN_MEM_r[0]
	S += new_TZ_t2_mem0 <= new_TZ_t2

	new_TZ_t2_mem1 = S.Task('new_TZ_t2_mem1', length=1, delay_cost=1)
	new_TZ_t2_mem1 += MAIN_MEM_r[1]
	S += new_TZ_t2_mem1 <= new_TZ_t2

	t16_t2 = S.Task('t16_t2', length=2, delay_cost=1)
	t16_t2 += alt(MAS)
	t16_t2_in = S.Task('t16_t2_in', length=1, delay_cost=1)
	t16_t2_in += alt(MAS_in)
	S += t16_t2_in*MAS_in[0]<=t16_t2*MAS[0]

	S += t16_t2_in*MAS_in[1]<=t16_t2*MAS[1]

	S += t16_t2_in*MAS_in[2]<=t16_t2*MAS[2]

	S += t16_t2_in*MAS_in[3]<=t16_t2*MAS[3]

	t16_t2_mem0 = S.Task('t16_t2_mem0', length=1, delay_cost=1)
	t16_t2_mem0 += MAIN_MEM_r[0]
	S += t16_t2_mem0 <= t16_t2

	t16_t2_mem1 = S.Task('t16_t2_mem1', length=1, delay_cost=1)
	t16_t2_mem1 += MAIN_MEM_r[1]
	S += t16_t2_mem1 <= t16_t2

	t17_t2 = S.Task('t17_t2', length=2, delay_cost=1)
	t17_t2 += alt(MAS)
	t17_t2_in = S.Task('t17_t2_in', length=1, delay_cost=1)
	t17_t2_in += alt(MAS_in)
	S += t17_t2_in*MAS_in[0]<=t17_t2*MAS[0]

	S += t17_t2_in*MAS_in[1]<=t17_t2*MAS[1]

	S += t17_t2_in*MAS_in[2]<=t17_t2*MAS[2]

	S += t17_t2_in*MAS_in[3]<=t17_t2*MAS[3]

	t17_t2_mem0 = S.Task('t17_t2_mem0', length=1, delay_cost=1)
	t17_t2_mem0 += MAIN_MEM_r[0]
	S += t17_t2_mem0 <= t17_t2

	t17_t2_mem1 = S.Task('t17_t2_mem1', length=1, delay_cost=1)
	t17_t2_mem1 += MAIN_MEM_r[1]
	S += t17_t2_mem1 <= t17_t2

	t0_t4 = S.Task('t0_t4', length=6, delay_cost=1)
	t0_t4 += alt(MM)
	t0_t4_in = S.Task('t0_t4_in', length=1, delay_cost=1)
	t0_t4_in += alt(MM_in)
	S += t0_t4_in*MM_in[0]<=t0_t4*MM[0]
	S += t0_t4_in*MM_in[1]<=t0_t4*MM[1]
	t0_t4_mem0 = S.Task('t0_t4_mem0', length=1, delay_cost=1)
	t0_t4_mem0 += alt(MAS_MEM)
	S += (t0_t2*MAS[0])-1 < t0_t4_mem0*MAS_MEM[0]
	S += (t0_t2*MAS[1])-1 < t0_t4_mem0*MAS_MEM[2]
	S += (t0_t2*MAS[2])-1 < t0_t4_mem0*MAS_MEM[4]
	S += (t0_t2*MAS[3])-1 < t0_t4_mem0*MAS_MEM[6]
	S += t0_t4_mem0 <= t0_t4

	t0_t4_mem1 = S.Task('t0_t4_mem1', length=1, delay_cost=1)
	t0_t4_mem1 += alt(MAS_MEM)
	S += (t0_t3*MAS[0])-1 < t0_t4_mem1*MAS_MEM[1]
	S += (t0_t3*MAS[1])-1 < t0_t4_mem1*MAS_MEM[3]
	S += (t0_t3*MAS[2])-1 < t0_t4_mem1*MAS_MEM[5]
	S += (t0_t3*MAS[3])-1 < t0_t4_mem1*MAS_MEM[7]
	S += t0_t4_mem1 <= t0_t4

	t00 = S.Task('t00', length=2, delay_cost=1)
	t00 += alt(MAS)
	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	t00_in += alt(MAS_in)
	S += t00_in*MAS_in[0]<=t00*MAS[0]

	S += t00_in*MAS_in[1]<=t00*MAS[1]

	S += t00_in*MAS_in[2]<=t00*MAS[2]

	S += t00_in*MAS_in[3]<=t00*MAS[3]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	t00_mem0 += alt(MM_MEM)
	S += (t0_t0*MM[0])-1 < t00_mem0*MM_MEM[0]
	S += (t0_t0*MM[1])-1 < t00_mem0*MM_MEM[2]
	S += t00_mem0 <= t00

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	t00_mem1 += alt(MM_MEM)
	S += (t0_t1*MM[0])-1 < t00_mem1*MM_MEM[1]
	S += (t0_t1*MM[1])-1 < t00_mem1*MM_MEM[3]
	S += t00_mem1 <= t00

	t0_t5 = S.Task('t0_t5', length=2, delay_cost=1)
	t0_t5 += alt(MAS)
	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	t0_t5_in += alt(MAS_in)
	S += t0_t5_in*MAS_in[0]<=t0_t5*MAS[0]

	S += t0_t5_in*MAS_in[1]<=t0_t5*MAS[1]

	S += t0_t5_in*MAS_in[2]<=t0_t5*MAS[2]

	S += t0_t5_in*MAS_in[3]<=t0_t5*MAS[3]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	t0_t5_mem0 += alt(MM_MEM)
	S += (t0_t0*MM[0])-1 < t0_t5_mem0*MM_MEM[0]
	S += (t0_t0*MM[1])-1 < t0_t5_mem0*MM_MEM[2]
	S += t0_t5_mem0 <= t0_t5

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	t0_t5_mem1 += alt(MM_MEM)
	S += (t0_t1*MM[0])-1 < t0_t5_mem1*MM_MEM[1]
	S += (t0_t1*MM[1])-1 < t0_t5_mem1*MM_MEM[3]
	S += t0_t5_mem1 <= t0_t5

	t2_t4 = S.Task('t2_t4', length=6, delay_cost=1)
	t2_t4 += alt(MM)
	t2_t4_in = S.Task('t2_t4_in', length=1, delay_cost=1)
	t2_t4_in += alt(MM_in)
	S += t2_t4_in*MM_in[0]<=t2_t4*MM[0]
	S += t2_t4_in*MM_in[1]<=t2_t4*MM[1]
	t2_t4_mem0 = S.Task('t2_t4_mem0', length=1, delay_cost=1)
	t2_t4_mem0 += alt(MAS_MEM)
	S += (t2_t2*MAS[0])-1 < t2_t4_mem0*MAS_MEM[0]
	S += (t2_t2*MAS[1])-1 < t2_t4_mem0*MAS_MEM[2]
	S += (t2_t2*MAS[2])-1 < t2_t4_mem0*MAS_MEM[4]
	S += (t2_t2*MAS[3])-1 < t2_t4_mem0*MAS_MEM[6]
	S += t2_t4_mem0 <= t2_t4

	t2_t4_mem1 = S.Task('t2_t4_mem1', length=1, delay_cost=1)
	t2_t4_mem1 += alt(MAS_MEM)
	S += (t2_t3*MAS[0])-1 < t2_t4_mem1*MAS_MEM[1]
	S += (t2_t3*MAS[1])-1 < t2_t4_mem1*MAS_MEM[3]
	S += (t2_t3*MAS[2])-1 < t2_t4_mem1*MAS_MEM[5]
	S += (t2_t3*MAS[3])-1 < t2_t4_mem1*MAS_MEM[7]
	S += t2_t4_mem1 <= t2_t4

	t20 = S.Task('t20', length=2, delay_cost=1)
	t20 += alt(MAS)
	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	t20_in += alt(MAS_in)
	S += t20_in*MAS_in[0]<=t20*MAS[0]

	S += t20_in*MAS_in[1]<=t20*MAS[1]

	S += t20_in*MAS_in[2]<=t20*MAS[2]

	S += t20_in*MAS_in[3]<=t20*MAS[3]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	t20_mem0 += alt(MM_MEM)
	S += (t2_t0*MM[0])-1 < t20_mem0*MM_MEM[0]
	S += (t2_t0*MM[1])-1 < t20_mem0*MM_MEM[2]
	S += t20_mem0 <= t20

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	t20_mem1 += alt(MM_MEM)
	S += (t2_t1*MM[0])-1 < t20_mem1*MM_MEM[1]
	S += (t2_t1*MM[1])-1 < t20_mem1*MM_MEM[3]
	S += t20_mem1 <= t20

	t2_t5 = S.Task('t2_t5', length=2, delay_cost=1)
	t2_t5 += alt(MAS)
	t2_t5_in = S.Task('t2_t5_in', length=1, delay_cost=1)
	t2_t5_in += alt(MAS_in)
	S += t2_t5_in*MAS_in[0]<=t2_t5*MAS[0]

	S += t2_t5_in*MAS_in[1]<=t2_t5*MAS[1]

	S += t2_t5_in*MAS_in[2]<=t2_t5*MAS[2]

	S += t2_t5_in*MAS_in[3]<=t2_t5*MAS[3]

	t2_t5_mem0 = S.Task('t2_t5_mem0', length=1, delay_cost=1)
	t2_t5_mem0 += alt(MM_MEM)
	S += (t2_t0*MM[0])-1 < t2_t5_mem0*MM_MEM[0]
	S += (t2_t0*MM[1])-1 < t2_t5_mem0*MM_MEM[2]
	S += t2_t5_mem0 <= t2_t5

	t2_t5_mem1 = S.Task('t2_t5_mem1', length=1, delay_cost=1)
	t2_t5_mem1 += alt(MM_MEM)
	S += (t2_t1*MM[0])-1 < t2_t5_mem1*MM_MEM[1]
	S += (t2_t1*MM[1])-1 < t2_t5_mem1*MM_MEM[3]
	S += t2_t5_mem1 <= t2_t5

	t01 = S.Task('t01', length=2, delay_cost=1)
	t01 += alt(MAS)
	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	t01_in += alt(MAS_in)
	S += t01_in*MAS_in[0]<=t01*MAS[0]

	S += t01_in*MAS_in[1]<=t01*MAS[1]

	S += t01_in*MAS_in[2]<=t01*MAS[2]

	S += t01_in*MAS_in[3]<=t01*MAS[3]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	t01_mem0 += alt(MM_MEM)
	S += (t0_t4*MM[0])-1 < t01_mem0*MM_MEM[0]
	S += (t0_t4*MM[1])-1 < t01_mem0*MM_MEM[2]
	S += t01_mem0 <= t01

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	t01_mem1 += alt(MAS_MEM)
	S += (t0_t5*MAS[0])-1 < t01_mem1*MAS_MEM[1]
	S += (t0_t5*MAS[1])-1 < t01_mem1*MAS_MEM[3]
	S += (t0_t5*MAS[2])-1 < t01_mem1*MAS_MEM[5]
	S += (t0_t5*MAS[3])-1 < t01_mem1*MAS_MEM[7]
	S += t01_mem1 <= t01

	t10 = S.Task('t10', length=2, delay_cost=1)
	t10 += alt(MAS)
	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	t10_in += alt(MAS_in)
	S += t10_in*MAS_in[0]<=t10*MAS[0]

	S += t10_in*MAS_in[1]<=t10*MAS[1]

	S += t10_in*MAS_in[2]<=t10*MAS[2]

	S += t10_in*MAS_in[3]<=t10*MAS[3]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	t10_mem0 += MAIN_MEM_r[0]
	S += t10_mem0 <= t10

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	t10_mem1 += alt(MAS_MEM)
	S += (t00*MAS[0])-1 < t10_mem1*MAS_MEM[1]
	S += (t00*MAS[1])-1 < t10_mem1*MAS_MEM[3]
	S += (t00*MAS[2])-1 < t10_mem1*MAS_MEM[5]
	S += (t00*MAS[3])-1 < t10_mem1*MAS_MEM[7]
	S += t10_mem1 <= t10

	t21 = S.Task('t21', length=2, delay_cost=1)
	t21 += alt(MAS)
	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	t21_in += alt(MAS_in)
	S += t21_in*MAS_in[0]<=t21*MAS[0]

	S += t21_in*MAS_in[1]<=t21*MAS[1]

	S += t21_in*MAS_in[2]<=t21*MAS[2]

	S += t21_in*MAS_in[3]<=t21*MAS[3]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	t21_mem0 += alt(MM_MEM)
	S += (t2_t4*MM[0])-1 < t21_mem0*MM_MEM[0]
	S += (t2_t4*MM[1])-1 < t21_mem0*MM_MEM[2]
	S += t21_mem0 <= t21

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	t21_mem1 += alt(MAS_MEM)
	S += (t2_t5*MAS[0])-1 < t21_mem1*MAS_MEM[1]
	S += (t2_t5*MAS[1])-1 < t21_mem1*MAS_MEM[3]
	S += (t2_t5*MAS[2])-1 < t21_mem1*MAS_MEM[5]
	S += (t2_t5*MAS[3])-1 < t21_mem1*MAS_MEM[7]
	S += t21_mem1 <= t21

	t30 = S.Task('t30', length=2, delay_cost=1)
	t30 += alt(MAS)
	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	t30_in += alt(MAS_in)
	S += t30_in*MAS_in[0]<=t30*MAS[0]

	S += t30_in*MAS_in[1]<=t30*MAS[1]

	S += t30_in*MAS_in[2]<=t30*MAS[2]

	S += t30_in*MAS_in[3]<=t30*MAS[3]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	t30_mem0 += MAIN_MEM_r[0]
	S += t30_mem0 <= t30

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	t30_mem1 += alt(MAS_MEM)
	S += (t20*MAS[0])-1 < t30_mem1*MAS_MEM[1]
	S += (t20*MAS[1])-1 < t30_mem1*MAS_MEM[3]
	S += (t20*MAS[2])-1 < t30_mem1*MAS_MEM[5]
	S += (t20*MAS[3])-1 < t30_mem1*MAS_MEM[7]
	S += t30_mem1 <= t30

	t11 = S.Task('t11', length=2, delay_cost=1)
	t11 += alt(MAS)
	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	t11_in += alt(MAS_in)
	S += t11_in*MAS_in[0]<=t11*MAS[0]

	S += t11_in*MAS_in[1]<=t11*MAS[1]

	S += t11_in*MAS_in[2]<=t11*MAS[2]

	S += t11_in*MAS_in[3]<=t11*MAS[3]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	t11_mem0 += MAIN_MEM_r[0]
	S += t11_mem0 <= t11

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	t11_mem1 += alt(MAS_MEM)
	S += (t01*MAS[0])-1 < t11_mem1*MAS_MEM[1]
	S += (t01*MAS[1])-1 < t11_mem1*MAS_MEM[3]
	S += (t01*MAS[2])-1 < t11_mem1*MAS_MEM[5]
	S += (t01*MAS[3])-1 < t11_mem1*MAS_MEM[7]
	S += t11_mem1 <= t11

	t31 = S.Task('t31', length=2, delay_cost=1)
	t31 += alt(MAS)
	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	t31_in += alt(MAS_in)
	S += t31_in*MAS_in[0]<=t31*MAS[0]

	S += t31_in*MAS_in[1]<=t31*MAS[1]

	S += t31_in*MAS_in[2]<=t31*MAS[2]

	S += t31_in*MAS_in[3]<=t31*MAS[3]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	t31_mem0 += MAIN_MEM_r[0]
	S += t31_mem0 <= t31

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	t31_mem1 += alt(MAS_MEM)
	S += (t21*MAS[0])-1 < t31_mem1*MAS_MEM[1]
	S += (t21*MAS[1])-1 < t31_mem1*MAS_MEM[3]
	S += (t21*MAS[2])-1 < t31_mem1*MAS_MEM[5]
	S += (t21*MAS[3])-1 < t31_mem1*MAS_MEM[7]
	S += t31_mem1 <= t31

	c010 = S.Task('c010', length=6, delay_cost=1)
	c010 += alt(MM)
	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MM_in)
	S += c010_in*MM_in[0]<=c010*MM[0]
	S += c010_in*MM_in[1]<=c010*MM[1]
	S += 0<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += alt(MAS_MEM)
	S += (t30*MAS[0])-1 < c010_mem0*MAS_MEM[0]
	S += (t30*MAS[1])-1 < c010_mem0*MAS_MEM[2]
	S += (t30*MAS[2])-1 < c010_mem0*MAS_MEM[4]
	S += (t30*MAS[3])-1 < c010_mem0*MAS_MEM[6]
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += MAIN_MEM_r[1]
	S += c010_mem1 <= c010

	c200 = S.Task('c200', length=6, delay_cost=1)
	c200 += alt(MM)
	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MM_in)
	S += c200_in*MM_in[0]<=c200*MM[0]
	S += c200_in*MM_in[1]<=c200*MM[1]
	S += 0<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < c200_mem0*MAS_MEM[0]
	S += (t10*MAS[1])-1 < c200_mem0*MAS_MEM[2]
	S += (t10*MAS[2])-1 < c200_mem0*MAS_MEM[4]
	S += (t10*MAS[3])-1 < c200_mem0*MAS_MEM[6]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAIN_MEM_r[1]
	S += c200_mem1 <= c200

	t16_t0 = S.Task('t16_t0', length=6, delay_cost=1)
	t16_t0 += alt(MM)
	t16_t0_in = S.Task('t16_t0_in', length=1, delay_cost=1)
	t16_t0_in += alt(MM_in)
	S += t16_t0_in*MM_in[0]<=t16_t0*MM[0]
	S += t16_t0_in*MM_in[1]<=t16_t0*MM[1]
	t16_t0_mem0 = S.Task('t16_t0_mem0', length=1, delay_cost=1)
	t16_t0_mem0 += MAIN_MEM_r[0]
	S += t16_t0_mem0 <= t16_t0

	t16_t0_mem1 = S.Task('t16_t0_mem1', length=1, delay_cost=1)
	t16_t0_mem1 += alt(MAS_MEM)
	S += (t30*MAS[0])-1 < t16_t0_mem1*MAS_MEM[1]
	S += (t30*MAS[1])-1 < t16_t0_mem1*MAS_MEM[3]
	S += (t30*MAS[2])-1 < t16_t0_mem1*MAS_MEM[5]
	S += (t30*MAS[3])-1 < t16_t0_mem1*MAS_MEM[7]
	S += t16_t0_mem1 <= t16_t0

	t17_t0 = S.Task('t17_t0', length=6, delay_cost=1)
	t17_t0 += alt(MM)
	t17_t0_in = S.Task('t17_t0_in', length=1, delay_cost=1)
	t17_t0_in += alt(MM_in)
	S += t17_t0_in*MM_in[0]<=t17_t0*MM[0]
	S += t17_t0_in*MM_in[1]<=t17_t0*MM[1]
	t17_t0_mem0 = S.Task('t17_t0_mem0', length=1, delay_cost=1)
	t17_t0_mem0 += MAIN_MEM_r[0]
	S += t17_t0_mem0 <= t17_t0

	t17_t0_mem1 = S.Task('t17_t0_mem1', length=1, delay_cost=1)
	t17_t0_mem1 += alt(MAS_MEM)
	S += (t10*MAS[0])-1 < t17_t0_mem1*MAS_MEM[1]
	S += (t10*MAS[1])-1 < t17_t0_mem1*MAS_MEM[3]
	S += (t10*MAS[2])-1 < t17_t0_mem1*MAS_MEM[5]
	S += (t10*MAS[3])-1 < t17_t0_mem1*MAS_MEM[7]
	S += t17_t0_mem1 <= t17_t0

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM2_stage2MAS4/EP2_ADD_w_EVAL/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

