from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 161
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=6)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	S += t3_t1_in >= 0
	t3_t1_in += MM_in[1]

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_mem0 >= 0
	t3_t1_mem0 += MAIN_MEM_r[0]

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_mem1 >= 0
	t3_t1_mem1 += MAIN_MEM_r[1]

	t3_t1 = S.Task('t3_t1', length=6, delay_cost=1)
	S += t3_t1 >= 1
	t3_t1 += MM[1]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 1
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 1
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 1
	t7_t0_mem1 += MAIN_MEM_r[1]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 2
	t6_t0_in += MM_in[1]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 2
	t6_t0_mem0 += MAIN_MEM_r[0]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 2
	t6_t0_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=6, delay_cost=1)
	S += t7_t0 >= 2
	t7_t0 += MM[0]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 3
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 3
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 3
	t0_t3_mem1 += MAIN_MEM_r[1]

	t6_t0 = S.Task('t6_t0', length=6, delay_cost=1)
	S += t6_t0 >= 3
	t6_t0 += MM[1]

	t0_t3 = S.Task('t0_t3', length=6, delay_cost=1)
	S += t0_t3 >= 4
	t0_t3 += MM[0]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 4
	t6_t1_in += MM_in[1]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 4
	t6_t1_mem0 += MAIN_MEM_r[0]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 4
	t6_t1_mem1 += MAIN_MEM_r[1]

	t6_t1 = S.Task('t6_t1', length=6, delay_cost=1)
	S += t6_t1 >= 5
	t6_t1 += MM[1]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 5
	t7_t1_in += MM_in[1]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 5
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 5
	t7_t1_mem1 += MAIN_MEM_r[1]

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	S += t3_t0_in >= 6
	t3_t0_in += MM_in[1]

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_mem0 >= 6
	t3_t0_mem0 += MAIN_MEM_r[0]

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_mem1 >= 6
	t3_t0_mem1 += MAIN_MEM_r[1]

	t7_t1 = S.Task('t7_t1', length=6, delay_cost=1)
	S += t7_t1 >= 6
	t7_t1 += MM[1]

	t3_t0 = S.Task('t3_t0', length=6, delay_cost=1)
	S += t3_t0 >= 7
	t3_t0 += MM[1]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 7
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 7
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 7
	t5_t1_mem1 += MAIN_MEM_r[1]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 8
	t5_t0_in += MM_in[1]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 8
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 8
	t5_t0_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=6, delay_cost=1)
	S += t5_t1 >= 8
	t5_t1 += MM[0]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 9
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 9
	t0_t5_mem1 += MM_MEM[1]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 9
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 9
	t4_t3_mem0 += MAIN_MEM_r[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 9
	t4_t3_mem1 += MAIN_MEM_r[1]

	t5_t0 = S.Task('t5_t0', length=6, delay_cost=1)
	S += t5_t0 >= 9
	t5_t0 += MM[1]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 10
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 10
	t01_mem1 += MM_MEM[1]

	t0_t5 = S.Task('t0_t5', length=1, delay_cost=1)
	S += t0_t5 >= 10
	t0_t5 += MAS[2]

	t4_t3 = S.Task('t4_t3', length=6, delay_cost=1)
	S += t4_t3 >= 10
	t4_t3 += MM[0]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 10
	t60_mem0 += MM_MEM[2]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 10
	t60_mem1 += MM_MEM[3]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 10
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 10
	t7_t3_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=1, delay_cost=1)
	S += t01 >= 11
	t01 += MAS[1]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 11
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 11
	t11_mem1 += MAIN_MEM_r[1]

	t220_mem0 = S.Task('t220_mem0', length=1, delay_cost=1)
	S += t220_mem0 >= 11
	t220_mem0 += MAS_MEM[4]

	t220_mem1 = S.Task('t220_mem1', length=1, delay_cost=1)
	S += t220_mem1 >= 11
	t220_mem1 += MAS_MEM[5]

	t60 = S.Task('t60', length=1, delay_cost=1)
	S += t60 >= 11
	t60 += MAS[2]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 11
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 11
	t70_mem1 += MM_MEM[3]

	t7_t3 = S.Task('t7_t3', length=1, delay_cost=1)
	S += t7_t3 >= 11
	t7_t3 += MAS[0]

	t11 = S.Task('t11', length=1, delay_cost=1)
	S += t11 >= 12
	t11 += MAS[3]

	t220 = S.Task('t220', length=1, delay_cost=1)
	S += t220 >= 12
	t220 += MAS[0]

	t230_mem0 = S.Task('t230_mem0', length=1, delay_cost=1)
	S += t230_mem0 >= 12
	t230_mem0 += MAS_MEM[0]

	t230_mem1 = S.Task('t230_mem1', length=1, delay_cost=1)
	S += t230_mem1 >= 12
	t230_mem1 += MAS_MEM[5]

	t260_mem0 = S.Task('t260_mem0', length=1, delay_cost=1)
	S += t260_mem0 >= 12
	t260_mem0 += MAS_MEM[2]

	t260_mem1 = S.Task('t260_mem1', length=1, delay_cost=1)
	S += t260_mem1 >= 12
	t260_mem1 += MAS_MEM[3]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 12
	t30_mem0 += MM_MEM[2]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 12
	t30_mem1 += MM_MEM[3]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 12
	t6_t2_mem0 += MAIN_MEM_r[0]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 12
	t6_t2_mem1 += MAIN_MEM_r[1]

	t70 = S.Task('t70', length=1, delay_cost=1)
	S += t70 >= 12
	t70 += MAS[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 13
	t110_mem0 += MAS_MEM[6]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 13
	t110_mem1 += MAS_MEM[7]

	t230 = S.Task('t230', length=1, delay_cost=1)
	S += t230 >= 13
	t230 += MAS[1]

	t260 = S.Task('t260', length=1, delay_cost=1)
	S += t260 >= 13
	t260 += MAS[2]

	t270_mem0 = S.Task('t270_mem0', length=1, delay_cost=1)
	S += t270_mem0 >= 13
	t270_mem0 += MAS_MEM[4]

	t270_mem1 = S.Task('t270_mem1', length=1, delay_cost=1)
	S += t270_mem1 >= 13
	t270_mem1 += MAS_MEM[3]

	t30 = S.Task('t30', length=1, delay_cost=1)
	S += t30 >= 13
	t30 += MAS[3]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 13
	t4_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 13
	t4_t1_mem1 += MAIN_MEM_r[1]

	t6_t2 = S.Task('t6_t2', length=1, delay_cost=1)
	S += t6_t2 >= 13
	t6_t2 += MAS[0]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 13
	t6_t5_mem0 += MM_MEM[2]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 13
	t6_t5_mem1 += MM_MEM[3]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 14
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 14
	t10_mem1 += MAIN_MEM_r[1]

	t110 = S.Task('t110', length=1, delay_cost=1)
	S += t110 >= 14
	t110 += MAS[3]

	t270 = S.Task('t270', length=1, delay_cost=1)
	S += t270 >= 14
	t270 += MAS[2]

	t4_t1 = S.Task('t4_t1', length=1, delay_cost=1)
	S += t4_t1 >= 14
	t4_t1 += MAS[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 14
	t50_mem0 += MM_MEM[2]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 14
	t50_mem1 += MM_MEM[1]

	t6_t5 = S.Task('t6_t5', length=1, delay_cost=1)
	S += t6_t5 >= 14
	t6_t5 += MAS[1]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 14
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 14
	t7_t5_mem1 += MM_MEM[3]

	t10 = S.Task('t10', length=1, delay_cost=1)
	S += t10 >= 15
	t10 += MAS[1]

	t290_mem0 = S.Task('t290_mem0', length=1, delay_cost=1)
	S += t290_mem0 >= 15
	t290_mem0 += MAS_MEM[4]

	t290_mem1 = S.Task('t290_mem1', length=1, delay_cost=1)
	S += t290_mem1 >= 15
	t290_mem1 += MAS_MEM[5]

	t3_t5_mem0 = S.Task('t3_t5_mem0', length=1, delay_cost=1)
	S += t3_t5_mem0 >= 15
	t3_t5_mem0 += MM_MEM[2]

	t3_t5_mem1 = S.Task('t3_t5_mem1', length=1, delay_cost=1)
	S += t3_t5_mem1 >= 15
	t3_t5_mem1 += MM_MEM[3]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 15
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 15
	t41_mem1 += MM_MEM[1]

	t50 = S.Task('t50', length=1, delay_cost=1)
	S += t50 >= 15
	t50 += MAS[2]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 15
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 15
	t5_t3_mem1 += MAIN_MEM_r[1]

	t7_t5 = S.Task('t7_t5', length=1, delay_cost=1)
	S += t7_t5 >= 15
	t7_t5 += MAS[0]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 16
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 16
	t0_t0_mem1 += MAIN_MEM_r[1]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 16
	t151_mem0 += MAS_MEM[2]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 16
	t151_mem1 += MAS_MEM[5]

	t290 = S.Task('t290', length=1, delay_cost=1)
	S += t290 >= 16
	t290 += MAS[1]

	t3_t5 = S.Task('t3_t5', length=1, delay_cost=1)
	S += t3_t5 >= 16
	t3_t5 += MAS[3]

	t41 = S.Task('t41', length=1, delay_cost=1)
	S += t41 >= 16
	t41 += MAS[2]

	t5_t3 = S.Task('t5_t3', length=1, delay_cost=1)
	S += t5_t3 >= 16
	t5_t3 += MAS[0]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 16
	t5_t5_mem0 += MM_MEM[2]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 16
	t5_t5_mem1 += MM_MEM[1]

	t0_t0 = S.Task('t0_t0', length=1, delay_cost=1)
	S += t0_t0 >= 17
	t0_t0 += MAS[0]

	t151 = S.Task('t151', length=1, delay_cost=1)
	S += t151 >= 17
	t151 += MAS[1]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 17
	t161_mem0 += MAS_MEM[2]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 17
	t161_mem1 += MAS_MEM[3]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 17
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 17
	t4_t5_mem1 += MM_MEM[1]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 17
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 17
	t5_t2_mem1 += MAIN_MEM_r[1]

	t5_t5 = S.Task('t5_t5', length=1, delay_cost=1)
	S += t5_t5 >= 17
	t5_t5 += MAS[2]

	t161 = S.Task('t161', length=1, delay_cost=1)
	S += t161 >= 18
	t161 += MAS[2]

	t300_mem0 = S.Task('t300_mem0', length=1, delay_cost=1)
	S += t300_mem0 >= 18
	t300_mem0 += MAS_MEM[2]

	t300_mem1 = S.Task('t300_mem1', length=1, delay_cost=1)
	S += t300_mem1 >= 18
	t300_mem1 += MAS_MEM[5]

	t4_t5 = S.Task('t4_t5', length=1, delay_cost=1)
	S += t4_t5 >= 18
	t4_t5 += MAS[0]

	t5_t2 = S.Task('t5_t2', length=1, delay_cost=1)
	S += t5_t2 >= 18
	t5_t2 += MAS[3]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 18
	t5_t4_in += MM_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 18
	t5_t4_mem0 += MAS_MEM[6]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 18
	t5_t4_mem1 += MAS_MEM[1]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 18
	t6_t3_mem0 += MAIN_MEM_r[0]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 18
	t6_t3_mem1 += MAIN_MEM_r[1]

	t300 = S.Task('t300', length=1, delay_cost=1)
	S += t300 >= 19
	t300 += MAS[1]

	t5_t4 = S.Task('t5_t4', length=6, delay_cost=1)
	S += t5_t4 >= 19
	t5_t4 += MM[0]

	t6_t3 = S.Task('t6_t3', length=1, delay_cost=1)
	S += t6_t3 >= 19
	t6_t3 += MAS[0]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 19
	t6_t4_in += MM_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 19
	t6_t4_mem0 += MAS_MEM[0]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 19
	t6_t4_mem1 += MAS_MEM[1]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 19
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 19
	t7_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 20
	t4_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 20
	t4_t0_mem1 += MAIN_MEM_r[1]

	t6_t4 = S.Task('t6_t4', length=6, delay_cost=1)
	S += t6_t4 >= 20
	t6_t4 += MM[0]

	t7_t2 = S.Task('t7_t2', length=1, delay_cost=1)
	S += t7_t2 >= 20
	t7_t2 += MAS[1]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 20
	t7_t4_in += MM_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 20
	t7_t4_mem0 += MAS_MEM[2]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 20
	t7_t4_mem1 += MAS_MEM[1]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 21
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 21
	t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t0 = S.Task('t4_t0', length=1, delay_cost=1)
	S += t4_t0 >= 21
	t4_t0 += MAS[0]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 21
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 21
	t4_t2_mem0 += MAS_MEM[0]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 21
	t4_t2_mem1 += MAS_MEM[1]

	t7_t4 = S.Task('t7_t4', length=6, delay_cost=1)
	S += t7_t4 >= 21
	t7_t4 += MM[0]

	t0_t1 = S.Task('t0_t1', length=1, delay_cost=1)
	S += t0_t1 >= 22
	t0_t1 += MAS[3]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 22
	t0_t2_in += MM_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 22
	t0_t2_mem0 += MAS_MEM[0]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 22
	t0_t2_mem1 += MAS_MEM[7]

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	S += t3_t3_mem0 >= 22
	t3_t3_mem0 += MAIN_MEM_r[0]

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	S += t3_t3_mem1 >= 22
	t3_t3_mem1 += MAIN_MEM_r[1]

	t4_t2 = S.Task('t4_t2', length=6, delay_cost=1)
	S += t4_t2 >= 22
	t4_t2 += MM[0]

	t0_t2 = S.Task('t0_t2', length=6, delay_cost=1)
	S += t0_t2 >= 23
	t0_t2 += MM[0]

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	S += t3_t2_mem0 >= 23
	t3_t2_mem0 += MAIN_MEM_r[0]

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	S += t3_t2_mem1 >= 23
	t3_t2_mem1 += MAIN_MEM_r[1]

	t3_t3 = S.Task('t3_t3', length=1, delay_cost=1)
	S += t3_t3 >= 23
	t3_t3 += MAS[0]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 24
	t21_mem0 += MAS_MEM[6]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 24
	t21_mem1 += MAIN_MEM_r[1]

	t3_t2 = S.Task('t3_t2', length=1, delay_cost=1)
	S += t3_t2 >= 24
	t3_t2 += MAS[1]

	t3_t4_in = S.Task('t3_t4_in', length=1, delay_cost=1)
	S += t3_t4_in >= 24
	t3_t4_in += MM_in[1]

	t3_t4_mem0 = S.Task('t3_t4_mem0', length=1, delay_cost=1)
	S += t3_t4_mem0 >= 24
	t3_t4_mem0 += MAS_MEM[2]

	t3_t4_mem1 = S.Task('t3_t4_mem1', length=1, delay_cost=1)
	S += t3_t4_mem1 >= 24
	t3_t4_mem1 += MAS_MEM[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 24
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 24
	t51_mem1 += MAS_MEM[5]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 25
	t20_mem0 += MAS_MEM[2]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 25
	t20_mem1 += MAIN_MEM_r[1]

	t21 = S.Task('t21', length=1, delay_cost=1)
	S += t21 >= 25
	t21 += MAS[3]

	t291_mem0 = S.Task('t291_mem0', length=1, delay_cost=1)
	S += t291_mem0 >= 25
	t291_mem0 += MAS_MEM[4]

	t291_mem1 = S.Task('t291_mem1', length=1, delay_cost=1)
	S += t291_mem1 >= 25
	t291_mem1 += MAS_MEM[5]

	t3_t4 = S.Task('t3_t4', length=6, delay_cost=1)
	S += t3_t4 >= 25
	t3_t4 += MM[1]

	t51 = S.Task('t51', length=1, delay_cost=1)
	S += t51 >= 25
	t51 += MAS[2]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 25
	t61_mem0 += MM_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 25
	t61_mem1 += MAS_MEM[3]

	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	S += t10_t3_in >= 26
	t10_t3_in += MM_in[1]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 26
	t10_t3_mem0 += MAS_MEM[0]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 26
	t10_t3_mem1 += MAS_MEM[7]

	t20 = S.Task('t20', length=1, delay_cost=1)
	S += t20 >= 26
	t20 += MAS[0]

	t291 = S.Task('t291', length=1, delay_cost=1)
	S += t291 >= 26
	t291 += MAS[2]

	t301_mem0 = S.Task('t301_mem0', length=1, delay_cost=1)
	S += t301_mem0 >= 26
	t301_mem0 += MAS_MEM[4]

	t301_mem1 = S.Task('t301_mem1', length=1, delay_cost=1)
	S += t301_mem1 >= 26
	t301_mem1 += MAS_MEM[5]

	t61 = S.Task('t61', length=1, delay_cost=1)
	S += t61 >= 26
	t61 += MAS[3]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 26
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 26
	t71_mem1 += MAS_MEM[1]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 26
	t80_mem0 += MAS_MEM[2]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 26
	t80_mem1 += MAIN_MEM_r[1]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 27
	t10_t0_mem0 += MAS_MEM[0]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 27
	t10_t0_mem1 += MAS_MEM[7]

	t10_t3 = S.Task('t10_t3', length=6, delay_cost=1)
	S += t10_t3 >= 27
	t10_t3 += MM[1]

	t261_mem0 = S.Task('t261_mem0', length=1, delay_cost=1)
	S += t261_mem0 >= 27
	t261_mem0 += MAS_MEM[2]

	t261_mem1 = S.Task('t261_mem1', length=1, delay_cost=1)
	S += t261_mem1 >= 27
	t261_mem1 += MAS_MEM[3]

	t301 = S.Task('t301', length=1, delay_cost=1)
	S += t301 >= 27
	t301 += MAS[0]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 27
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 27
	t40_mem1 += MAS_MEM[1]

	t71 = S.Task('t71', length=1, delay_cost=1)
	S += t71 >= 27
	t71 += MAS[1]

	t80 = S.Task('t80', length=1, delay_cost=1)
	S += t80 >= 27
	t80 += MAS[3]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 27
	t81_mem0 += MAS_MEM[6]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 27
	t81_mem1 += MAIN_MEM_r[1]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 28
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 28
	t00_mem1 += MAS_MEM[5]

	t10_t0 = S.Task('t10_t0', length=1, delay_cost=1)
	S += t10_t0 >= 28
	t10_t0 += MAS[2]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 28
	t10_t1_mem0 += MAS_MEM[0]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 28
	t10_t1_mem1 += MAS_MEM[7]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 28
	t181_mem0 += MAS_MEM[4]

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	S += t181_mem1 >= 28
	t181_mem1 += MAS_MEM[3]

	t261 = S.Task('t261', length=1, delay_cost=1)
	S += t261 >= 28
	t261 += MAS[3]

	t310_mem0 = S.Task('t310_mem0', length=1, delay_cost=1)
	S += t310_mem0 >= 28
	t310_mem0 += MAS_MEM[2]

	t310_mem1 = S.Task('t310_mem1', length=1, delay_cost=1)
	S += t310_mem1 >= 28
	t310_mem1 += MAIN_MEM_r[1]

	t40 = S.Task('t40', length=1, delay_cost=1)
	S += t40 >= 28
	t40 += MAS[1]

	t81 = S.Task('t81', length=1, delay_cost=1)
	S += t81 >= 28
	t81 += MAS[0]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 28
	t9_t3_in += MM_in[0]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 28
	t9_t3_mem0 += MAS_MEM[6]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 28
	t9_t3_mem1 += MAS_MEM[1]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 29
	c010_mem0 += MAS_MEM[4]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 29
	c010_mem1 += MAS_MEM[5]

	t00 = S.Task('t00', length=1, delay_cost=1)
	S += t00 >= 29
	t00 += MAS[1]

	t10_t1 = S.Task('t10_t1', length=1, delay_cost=1)
	S += t10_t1 >= 29
	t10_t1 += MAS[0]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 29
	t150_mem0 += MAS_MEM[2]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 29
	t150_mem1 += MAS_MEM[3]

	t181 = S.Task('t181', length=1, delay_cost=1)
	S += t181 >= 29
	t181 += MAS[3]

	t310 = S.Task('t310', length=1, delay_cost=1)
	S += t310 >= 29
	t310 += MAS[2]

	t311_mem0 = S.Task('t311_mem0', length=1, delay_cost=1)
	S += t311_mem0 >= 29
	t311_mem0 += MAS_MEM[0]

	t311_mem1 = S.Task('t311_mem1', length=1, delay_cost=1)
	S += t311_mem1 >= 29
	t311_mem1 += MAIN_MEM_r[1]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 29
	t9_t1_mem0 += MAS_MEM[6]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 29
	t9_t1_mem1 += MAS_MEM[1]

	t9_t3 = S.Task('t9_t3', length=6, delay_cost=1)
	S += t9_t3 >= 29
	t9_t3 += MM[0]

	c010 = S.Task('c010', length=1, delay_cost=1)
	S += c010 >= 30
	c010 += MAS[0]

	t150 = S.Task('t150', length=1, delay_cost=1)
	S += t150 >= 30
	t150 += MAS[1]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 30
	t180_mem0 += MAS_MEM[2]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 30
	t180_mem1 += MAS_MEM[5]

	t280_mem0 = S.Task('t280_mem0', length=1, delay_cost=1)
	S += t280_mem0 >= 30
	t280_mem0 += MAS_MEM[4]

	t280_mem1 = S.Task('t280_mem1', length=1, delay_cost=1)
	S += t280_mem1 >= 30
	t280_mem1 += MAIN_MEM_r[1]

	t311 = S.Task('t311', length=1, delay_cost=1)
	S += t311 >= 30
	t311 += MAS[2]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 30
	t31_mem0 += MM_MEM[2]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 30
	t31_mem1 += MAS_MEM[7]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 30
	t9_t0_mem0 += MAS_MEM[6]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 30
	t9_t0_mem1 += MAS_MEM[1]

	t9_t1 = S.Task('t9_t1', length=1, delay_cost=1)
	S += t9_t1 >= 30
	t9_t1 += MAS[3]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 31
	c010_w += MAIN_MEM_w

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	S += c210_mem0 >= 31
	c210_mem0 += MAS_MEM[0]

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	S += c210_mem1 >= 31
	c210_mem1 += MAS_MEM[1]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 31
	t111_mem0 += MAS_MEM[4]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 31
	t111_mem1 += MAS_MEM[5]

	t180 = S.Task('t180', length=1, delay_cost=1)
	S += t180 >= 31
	t180 += MAS[1]

	t190_mem0 = S.Task('t190_mem0', length=1, delay_cost=1)
	S += t190_mem0 >= 31
	t190_mem0 += MAS_MEM[2]

	t190_mem1 = S.Task('t190_mem1', length=1, delay_cost=1)
	S += t190_mem1 >= 31
	t190_mem1 += MAS_MEM[7]

	t271_mem0 = S.Task('t271_mem0', length=1, delay_cost=1)
	S += t271_mem0 >= 31
	t271_mem0 += MAS_MEM[6]

	t271_mem1 = S.Task('t271_mem1', length=1, delay_cost=1)
	S += t271_mem1 >= 31
	t271_mem1 += MAS_MEM[3]

	t280 = S.Task('t280', length=1, delay_cost=1)
	S += t280 >= 31
	t280 += MAS[0]

	t31 = S.Task('t31', length=1, delay_cost=1)
	S += t31 >= 31
	t31 += MAS[2]

	t9_t0 = S.Task('t9_t0', length=1, delay_cost=1)
	S += t9_t0 >= 31
	t9_t0 += MAS[3]

	c210 = S.Task('c210', length=1, delay_cost=1)
	S += c210 >= 32
	c210 += MAS[3]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 32
	t101_mem0 += MM_MEM[2]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 32
	t101_mem1 += MM_MEM[3]

	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	S += t10_t2_in >= 32
	t10_t2_in += MM_in[0]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 32
	t10_t2_mem0 += MAS_MEM[4]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 32
	t10_t2_mem1 += MAS_MEM[1]

	t111 = S.Task('t111', length=1, delay_cost=1)
	S += t111 >= 32
	t111 += MAS[1]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 32
	t160_mem0 += MAS_MEM[2]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 32
	t160_mem1 += MAS_MEM[3]

	t190 = S.Task('t190', length=1, delay_cost=1)
	S += t190 >= 32
	t190 += MAS[2]

	t271 = S.Task('t271', length=1, delay_cost=1)
	S += t271 >= 32
	t271 += MAS[0]

	t281_mem0 = S.Task('t281_mem0', length=1, delay_cost=1)
	S += t281_mem0 >= 32
	t281_mem0 += MAS_MEM[0]

	t281_mem1 = S.Task('t281_mem1', length=1, delay_cost=1)
	S += t281_mem1 >= 32
	t281_mem1 += MAIN_MEM_r[1]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 32
	t9_t2_in += MM_in[1]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 32
	t9_t2_mem0 += MAS_MEM[6]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 32
	t9_t2_mem1 += MAS_MEM[7]

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	S += c210_w >= 33
	c210_w += MAIN_MEM_w

	t101 = S.Task('t101', length=1, delay_cost=1)
	S += t101 >= 33
	t101 += MAS[2]

	t10_t2 = S.Task('t10_t2', length=6, delay_cost=1)
	S += t10_t2 >= 33
	t10_t2 += MM[0]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 33
	t10_t5_mem0 += MM_MEM[2]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 33
	t10_t5_mem1 += MM_MEM[3]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 33
	t121_mem0 += MAS_MEM[2]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 33
	t121_mem1 += MAS_MEM[7]

	t160 = S.Task('t160', length=1, delay_cost=1)
	S += t160 >= 33
	t160 += MAS[0]

	t191_mem0 = S.Task('t191_mem0', length=1, delay_cost=1)
	S += t191_mem0 >= 33
	t191_mem0 += MAS_MEM[6]

	t191_mem1 = S.Task('t191_mem1', length=1, delay_cost=1)
	S += t191_mem1 >= 33
	t191_mem1 += MAS_MEM[3]

	t200_mem0 = S.Task('t200_mem0', length=1, delay_cost=1)
	S += t200_mem0 >= 33
	t200_mem0 += MAS_MEM[4]

	t200_mem1 = S.Task('t200_mem1', length=1, delay_cost=1)
	S += t200_mem1 >= 33
	t200_mem1 += MAS_MEM[5]

	t281 = S.Task('t281', length=1, delay_cost=1)
	S += t281 >= 33
	t281 += MAS[1]

	t9_t2 = S.Task('t9_t2', length=6, delay_cost=1)
	S += t9_t2 >= 33
	t9_t2 += MM[1]

	t10_t5 = S.Task('t10_t5', length=1, delay_cost=1)
	S += t10_t5 >= 34
	t10_t5 += MAS[3]

	t121 = S.Task('t121', length=1, delay_cost=1)
	S += t121 >= 34
	t121 += MAS[1]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 34
	t131_mem0 += MAS_MEM[2]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 34
	t131_mem1 += MAS_MEM[3]

	t191 = S.Task('t191', length=1, delay_cost=1)
	S += t191 >= 34
	t191 += MAS[2]

	t200 = S.Task('t200', length=1, delay_cost=1)
	S += t200 >= 34
	t200 += MAS[0]

	t201_mem0 = S.Task('t201_mem0', length=1, delay_cost=1)
	S += t201_mem0 >= 34
	t201_mem0 += MAS_MEM[4]

	t201_mem1 = S.Task('t201_mem1', length=1, delay_cost=1)
	S += t201_mem1 >= 34
	t201_mem1 += MAS_MEM[5]

	t221_mem0 = S.Task('t221_mem0', length=1, delay_cost=1)
	S += t221_mem0 >= 34
	t221_mem0 += MAS_MEM[6]

	t221_mem1 = S.Task('t221_mem1', length=1, delay_cost=1)
	S += t221_mem1 >= 34
	t221_mem1 += MAS_MEM[7]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 34
	t91_mem0 += MM_MEM[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 34
	t91_mem1 += MM_MEM[1]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 35
	t120_mem0 += MAS_MEM[6]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 35
	t120_mem1 += MAS_MEM[3]

	t131 = S.Task('t131', length=1, delay_cost=1)
	S += t131 >= 35
	t131 += MAS[1]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 35
	t171_mem0 += MAS_MEM[0]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 35
	t171_mem1 += MAS_MEM[5]

	t201 = S.Task('t201', length=1, delay_cost=1)
	S += t201 >= 35
	t201 += MAS[3]

	t221 = S.Task('t221', length=1, delay_cost=1)
	S += t221 >= 35
	t221 += MAS[2]

	t231_mem0 = S.Task('t231_mem0', length=1, delay_cost=1)
	S += t231_mem0 >= 35
	t231_mem0 += MAS_MEM[4]

	t231_mem1 = S.Task('t231_mem1', length=1, delay_cost=1)
	S += t231_mem1 >= 35
	t231_mem1 += MAS_MEM[7]

	t91 = S.Task('t91', length=1, delay_cost=1)
	S += t91 >= 35
	t91 += MAS[0]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 35
	t9_t5_mem0 += MM_MEM[0]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 35
	t9_t5_mem1 += MM_MEM[1]

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	S += c111_mem0 >= 36
	c111_mem0 += MAS_MEM[4]

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	S += c111_mem1 >= 36
	c111_mem1 += MAS_MEM[7]

	t120 = S.Task('t120', length=1, delay_cost=1)
	S += t120 >= 36
	t120 += MAS[2]

	t171 = S.Task('t171', length=1, delay_cost=1)
	S += t171 >= 36
	t171 += MAS[3]

	t231 = S.Task('t231', length=1, delay_cost=1)
	S += t231 >= 36
	t231 += MAS[0]

	t240_mem0 = S.Task('t240_mem0', length=1, delay_cost=1)
	S += t240_mem0 >= 36
	t240_mem0 += MAS_MEM[2]

	t240_mem1 = S.Task('t240_mem1', length=1, delay_cost=1)
	S += t240_mem1 >= 36
	t240_mem1 += MAS_MEM[1]

	t241_mem0 = S.Task('t241_mem0', length=1, delay_cost=1)
	S += t241_mem0 >= 36
	t241_mem0 += MAS_MEM[0]

	t241_mem1 = S.Task('t241_mem1', length=1, delay_cost=1)
	S += t241_mem1 >= 36
	t241_mem1 += MAS_MEM[3]

	t9_t5 = S.Task('t9_t5', length=1, delay_cost=1)
	S += t9_t5 >= 36
	t9_t5 += MAS[1]

	c111 = S.Task('c111', length=1, delay_cost=1)
	S += c111 >= 37
	c111 += MAS[0]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 37
	t130_mem0 += MAS_MEM[2]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 37
	t130_mem1 += MAS_MEM[5]

	t240 = S.Task('t240', length=1, delay_cost=1)
	S += t240 >= 37
	t240 += MAS[3]

	t241 = S.Task('t241', length=1, delay_cost=1)
	S += t241 >= 37
	t241 += MAS[2]

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	S += c111_w >= 38
	c111_w += MAIN_MEM_w

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 38
	t100_mem0 += MM_MEM[0]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 38
	t100_mem1 += MAS_MEM[7]

	t130 = S.Task('t130', length=1, delay_cost=1)
	S += t130 >= 38
	t130 += MAS[0]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 38
	t90_mem0 += MM_MEM[2]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 38
	t90_mem1 += MAS_MEM[3]

	t100 = S.Task('t100', length=1, delay_cost=1)
	S += t100 >= 39
	t100 += MAS[1]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 39
	t170_mem0 += MAS_MEM[0]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 39
	t170_mem1 += MAS_MEM[1]

	t90 = S.Task('t90', length=1, delay_cost=1)
	S += t90 >= 39
	t90 += MAS[0]

	t170 = S.Task('t170', length=1, delay_cost=1)
	S += t170 >= 40
	t170 += MAS[0]


	# new tasks
	t140 = S.Task('t140', length=1, delay_cost=1)
	t140 += alt(MAS)
	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += MAS_MEM[0]
	S += 38 < t140_mem0
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += MAIN_MEM_r[1]
	S += t140_mem1 <= t140

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)
	S += 22<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[2]
	S += 35 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += MAS_MEM[3]
	S += 35 < c001_mem1
	S += c001_mem1 <= c001

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(MAS)
	S += 30<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MAS_MEM[4]
	S += 30 < c011_mem0
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += MAS_MEM[5]
	S += 30 < c011_mem1
	S += c011_mem1 <= c011

	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(MAS)
	S += 24<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[2]
	S += 39 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MAS_MEM[1]
	S += 40 < c110_mem1
	S += c110_mem1 <= c110

	t210 = S.Task('t210', length=1, delay_cost=1)
	t210 += alt(MAS)
	t210_mem0 = S.Task('t210_mem0', length=1, delay_cost=1)
	t210_mem0 += MAS_MEM[0]
	S += 34 < t210_mem0
	S += t210_mem0 <= t210

	t210_mem1 = S.Task('t210_mem1', length=1, delay_cost=1)
	t210_mem1 += MAS_MEM[1]
	S += 39 < t210_mem1
	S += t210_mem1 <= t210

	t211 = S.Task('t211', length=1, delay_cost=1)
	t211 += alt(MAS)
	t211_mem0 = S.Task('t211_mem0', length=1, delay_cost=1)
	t211_mem0 += MAS_MEM[6]
	S += 35 < t211_mem0
	S += t211_mem0 <= t211

	t211_mem1 = S.Task('t211_mem1', length=1, delay_cost=1)
	t211_mem1 += MAS_MEM[1]
	S += 35 < t211_mem1
	S += t211_mem1 <= t211

	t250 = S.Task('t250', length=1, delay_cost=1)
	t250 += alt(MAS)
	t250_mem0 = S.Task('t250_mem0', length=1, delay_cost=1)
	t250_mem0 += MAIN_MEM_r[0]
	S += t250_mem0 <= t250

	t250_mem1 = S.Task('t250_mem1', length=1, delay_cost=1)
	t250_mem1 += MAS_MEM[7]
	S += 37 < t250_mem1
	S += t250_mem1 <= t250

	t251 = S.Task('t251', length=1, delay_cost=1)
	t251 += alt(MAS)
	t251_mem0 = S.Task('t251_mem0', length=1, delay_cost=1)
	t251_mem0 += MAIN_MEM_r[0]
	S += t251_mem0 <= t251

	t251_mem1 = S.Task('t251_mem1', length=1, delay_cost=1)
	t251_mem1 += MAS_MEM[5]
	S += 37 < t251_mem1
	S += t251_mem1 <= t251

	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(MAS)
	S += 33<c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += MAS_MEM[2]
	S += 33 < c211_mem0
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += MAS_MEM[3]
	S += 33 < c211_mem1
	S += c211_mem1 <= c211

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)
	S += 22<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[0]
	S += 38 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (t140*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (t140*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (t140*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += c000_mem1 <= c000

	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(MAS)
	S += 27<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(MAS_MEM)
	S += (t210*MAS[0])-1 < c200_mem0*MAS_MEM[0]
	S += (t210*MAS[1])-1 < c200_mem0*MAS_MEM[2]
	S += (t210*MAS[2])-1 < c200_mem0*MAS_MEM[4]
	S += (t210*MAS[3])-1 < c200_mem0*MAS_MEM[6]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAS_MEM[3]
	S += 39 < c200_mem1
	S += c200_mem1 <= c200

	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(MAS)
	S += 28<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MAS_MEM)
	S += (t211*MAS[0])-1 < c201_mem0*MAS_MEM[0]
	S += (t211*MAS[1])-1 < c201_mem0*MAS_MEM[2]
	S += (t211*MAS[2])-1 < c201_mem0*MAS_MEM[4]
	S += (t211*MAS[3])-1 < c201_mem0*MAS_MEM[6]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += MAS_MEM[5]
	S += 33 < c201_mem1
	S += c201_mem1 <= c201

	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(MAS)
	S += 20<c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(MAS_MEM)
	S += (t250*MAS[0])-1 < c100_mem0*MAS_MEM[0]
	S += (t250*MAS[1])-1 < c100_mem0*MAS_MEM[2]
	S += (t250*MAS[2])-1 < c100_mem0*MAS_MEM[4]
	S += (t250*MAS[3])-1 < c100_mem0*MAS_MEM[6]
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += alt(MAS_MEM)
	S += (t250*MAS[0])-1 < c100_mem1*MAS_MEM[1]
	S += (t250*MAS[1])-1 < c100_mem1*MAS_MEM[3]
	S += (t250*MAS[2])-1 < c100_mem1*MAS_MEM[5]
	S += (t250*MAS[3])-1 < c100_mem1*MAS_MEM[7]
	S += c100_mem1 <= c100

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(MAS)
	S += 20<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MAS_MEM)
	S += (t251*MAS[0])-1 < c101_mem0*MAS_MEM[0]
	S += (t251*MAS[1])-1 < c101_mem0*MAS_MEM[2]
	S += (t251*MAS[2])-1 < c101_mem0*MAS_MEM[4]
	S += (t251*MAS[3])-1 < c101_mem0*MAS_MEM[6]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(MAS_MEM)
	S += (t251*MAS[0])-1 < c101_mem1*MAS_MEM[1]
	S += (t251*MAS[1])-1 < c101_mem1*MAS_MEM[3]
	S += (t251*MAS[2])-1 < c101_mem1*MAS_MEM[5]
	S += (t251*MAS[3])-1 < c101_mem1*MAS_MEM[7]
	S += c101_mem1 <= c101

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM2_stage1MAS4/SQR012345/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

