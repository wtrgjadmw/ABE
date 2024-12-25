from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 176
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=4, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 0
	t7_t1_in += MM_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 0
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 0
	t7_t1_mem1 += MAIN_MEM_r[1]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 1
	t7_t0_in += MM_in[1]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 1
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 1
	t7_t0_mem1 += MAIN_MEM_r[1]

	t7_t1 = S.Task('t7_t1', length=11, delay_cost=1)
	S += t7_t1 >= 1
	t7_t1 += MM[0]

	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	S += t3_t1_in >= 2
	t3_t1_in += MM_in[0]

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_mem0 >= 2
	t3_t1_mem0 += MAIN_MEM_r[0]

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_mem1 >= 2
	t3_t1_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=11, delay_cost=1)
	S += t7_t0 >= 2
	t7_t0 += MM[1]

	t3_t1 = S.Task('t3_t1', length=11, delay_cost=1)
	S += t3_t1 >= 3
	t3_t1 += MM[0]

	t3_t2_in = S.Task('t3_t2_in', length=1, delay_cost=1)
	S += t3_t2_in >= 3
	t3_t2_in += MAS_in[0]

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	S += t3_t2_mem0 >= 3
	t3_t2_mem0 += MAIN_MEM_r[0]

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	S += t3_t2_mem1 >= 3
	t3_t2_mem1 += MAIN_MEM_r[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 4
	t0_t0_in += MAS_in[5]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 4
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 4
	t0_t0_mem1 += MAIN_MEM_r[1]

	t3_t2 = S.Task('t3_t2', length=4, delay_cost=1)
	S += t3_t2 >= 4
	t3_t2 += MAS[0]

	t0_t0 = S.Task('t0_t0', length=4, delay_cost=1)
	S += t0_t0 >= 5
	t0_t0 += MAS[5]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 5
	t6_t1_in += MM_in[1]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 5
	t6_t1_mem0 += MAIN_MEM_r[0]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 5
	t6_t1_mem1 += MAIN_MEM_r[1]

	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 6
	t0_t3_in += MM_in[1]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 6
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 6
	t0_t3_mem1 += MAIN_MEM_r[1]

	t6_t1 = S.Task('t6_t1', length=11, delay_cost=1)
	S += t6_t1 >= 6
	t6_t1 += MM[1]

	t0_t3 = S.Task('t0_t3', length=11, delay_cost=1)
	S += t0_t3 >= 7
	t0_t3 += MM[1]

	t3_t3_in = S.Task('t3_t3_in', length=1, delay_cost=1)
	S += t3_t3_in >= 7
	t3_t3_in += MAS_in[2]

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	S += t3_t3_mem0 >= 7
	t3_t3_mem0 += MAIN_MEM_r[0]

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	S += t3_t3_mem1 >= 7
	t3_t3_mem1 += MAIN_MEM_r[1]

	t3_t3 = S.Task('t3_t3', length=4, delay_cost=1)
	S += t3_t3 >= 8
	t3_t3 += MAS[2]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 8
	t6_t2_in += MAS_in[3]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 8
	t6_t2_mem0 += MAIN_MEM_r[0]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 8
	t6_t2_mem1 += MAIN_MEM_r[1]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 9
	t4_t0_in += MAS_in[4]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 9
	t4_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 9
	t4_t0_mem1 += MAIN_MEM_r[1]

	t6_t2 = S.Task('t6_t2', length=4, delay_cost=1)
	S += t6_t2 >= 9
	t6_t2 += MAS[3]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 10
	t0_t1_in += MAS_in[4]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 10
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 10
	t0_t1_mem1 += MAIN_MEM_r[1]

	t4_t0 = S.Task('t4_t0', length=4, delay_cost=1)
	S += t4_t0 >= 10
	t4_t0 += MAS[4]

	t0_t1 = S.Task('t0_t1', length=4, delay_cost=1)
	S += t0_t1 >= 11
	t0_t1 += MAS[4]

	t3_t4_in = S.Task('t3_t4_in', length=1, delay_cost=1)
	S += t3_t4_in >= 11
	t3_t4_in += MM_in[1]

	t3_t4_mem0 = S.Task('t3_t4_mem0', length=1, delay_cost=1)
	S += t3_t4_mem0 >= 11
	t3_t4_mem0 += MAS_MEM[0]

	t3_t4_mem1 = S.Task('t3_t4_mem1', length=1, delay_cost=1)
	S += t3_t4_mem1 >= 11
	t3_t4_mem1 += MAS_MEM[5]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 11
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 11
	t6_t0_mem0 += MAIN_MEM_r[0]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 11
	t6_t0_mem1 += MAIN_MEM_r[1]

	t3_t4 = S.Task('t3_t4', length=11, delay_cost=1)
	S += t3_t4 >= 12
	t3_t4 += MM[1]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 12
	t5_t3_in += MAS_in[5]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 12
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 12
	t5_t3_mem1 += MAIN_MEM_r[1]

	t6_t0 = S.Task('t6_t0', length=11, delay_cost=1)
	S += t6_t0 >= 12
	t6_t0 += MM[0]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 12
	t70_in += MAS_in[0]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 12
	t70_mem0 += MM_MEM[2]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 12
	t70_mem1 += MM_MEM[1]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 13
	t4_t1_in += MAS_in[5]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 13
	t4_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 13
	t4_t1_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=4, delay_cost=1)
	S += t5_t3 >= 13
	t5_t3 += MAS[5]

	t70 = S.Task('t70', length=4, delay_cost=1)
	S += t70 >= 13
	t70 += MAS[0]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 13
	t7_t5_in += MAS_in[3]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 13
	t7_t5_mem0 += MM_MEM[2]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 13
	t7_t5_mem1 += MM_MEM[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 14
	t0_t2_in += MM_in[1]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 14
	t0_t2_mem0 += MAS_MEM[10]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 14
	t0_t2_mem1 += MAS_MEM[9]

	t4_t1 = S.Task('t4_t1', length=4, delay_cost=1)
	S += t4_t1 >= 14
	t4_t1 += MAS[5]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 14
	t5_t0_in += MM_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 14
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 14
	t5_t0_mem1 += MAIN_MEM_r[1]

	t7_t5 = S.Task('t7_t5', length=4, delay_cost=1)
	S += t7_t5 >= 14
	t7_t5 += MAS[3]

	t0_t2 = S.Task('t0_t2', length=11, delay_cost=1)
	S += t0_t2 >= 15
	t0_t2 += MM[1]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 15
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 15
	t4_t3_mem0 += MAIN_MEM_r[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 15
	t4_t3_mem1 += MAIN_MEM_r[1]

	t5_t0 = S.Task('t5_t0', length=11, delay_cost=1)
	S += t5_t0 >= 15
	t5_t0 += MM[0]

	t260_in = S.Task('t260_in', length=1, delay_cost=1)
	S += t260_in >= 16
	t260_in += MAS_in[2]

	t260_mem0 = S.Task('t260_mem0', length=1, delay_cost=1)
	S += t260_mem0 >= 16
	t260_mem0 += MAS_MEM[0]

	t260_mem1 = S.Task('t260_mem1', length=1, delay_cost=1)
	S += t260_mem1 >= 16
	t260_mem1 += MAS_MEM[1]

	t4_t3 = S.Task('t4_t3', length=11, delay_cost=1)
	S += t4_t3 >= 16
	t4_t3 += MM[0]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 16
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 16
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 16
	t5_t1_mem1 += MAIN_MEM_r[1]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 17
	t01_in += MAS_in[0]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 17
	t01_mem0 += MM_MEM[2]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 17
	t01_mem1 += MM_MEM[3]

	t260 = S.Task('t260', length=4, delay_cost=1)
	S += t260 >= 17
	t260 += MAS[2]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 17
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 17
	t4_t2_mem0 += MAS_MEM[8]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 17
	t4_t2_mem1 += MAS_MEM[11]

	t5_t1 = S.Task('t5_t1', length=11, delay_cost=1)
	S += t5_t1 >= 17
	t5_t1 += MM[0]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 17
	t6_t3_in += MAS_in[5]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 17
	t6_t3_mem0 += MAIN_MEM_r[0]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 17
	t6_t3_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=4, delay_cost=1)
	S += t01 >= 18
	t01 += MAS[0]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 18
	t0_t5_in += MAS_in[2]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 18
	t0_t5_mem0 += MM_MEM[2]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 18
	t0_t5_mem1 += MM_MEM[3]

	t4_t2 = S.Task('t4_t2', length=11, delay_cost=1)
	S += t4_t2 >= 18
	t4_t2 += MM[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 18
	t5_t2_in += MAS_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 18
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 18
	t5_t2_mem1 += MAIN_MEM_r[1]

	t6_t3 = S.Task('t6_t3', length=4, delay_cost=1)
	S += t6_t3 >= 18
	t6_t3 += MAS[5]

	t0_t5 = S.Task('t0_t5', length=4, delay_cost=1)
	S += t0_t5 >= 19
	t0_t5 += MAS[2]

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	S += t3_t0_in >= 19
	t3_t0_in += MM_in[0]

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_mem0 >= 19
	t3_t0_mem0 += MAIN_MEM_r[0]

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_mem1 >= 19
	t3_t0_mem1 += MAIN_MEM_r[1]

	t5_t2 = S.Task('t5_t2', length=4, delay_cost=1)
	S += t5_t2 >= 19
	t5_t2 += MAS[0]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 20
	t11_in += MAS_in[2]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 20
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 20
	t11_mem1 += MAIN_MEM_r[1]

	t270_in = S.Task('t270_in', length=1, delay_cost=1)
	S += t270_in >= 20
	t270_in += MAS_in[5]

	t270_mem0 = S.Task('t270_mem0', length=1, delay_cost=1)
	S += t270_mem0 >= 20
	t270_mem0 += MAS_MEM[4]

	t270_mem1 = S.Task('t270_mem1', length=1, delay_cost=1)
	S += t270_mem1 >= 20
	t270_mem1 += MAS_MEM[1]

	t3_t0 = S.Task('t3_t0', length=11, delay_cost=1)
	S += t3_t0 >= 20
	t3_t0 += MM[0]

	t11 = S.Task('t11', length=4, delay_cost=1)
	S += t11 >= 21
	t11 += MAS[2]

	t270 = S.Task('t270', length=4, delay_cost=1)
	S += t270 >= 21
	t270 += MAS[5]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 21
	t6_t4_in += MM_in[1]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 21
	t6_t4_mem0 += MAS_MEM[6]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 21
	t6_t4_mem1 += MAS_MEM[11]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 21
	t7_t2_in += MAS_in[5]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 21
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 21
	t7_t2_mem1 += MAIN_MEM_r[1]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 22
	t10_in += MAS_in[4]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 22
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 22
	t10_mem1 += MAIN_MEM_r[1]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 22
	t5_t4_in += MM_in[1]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 22
	t5_t4_mem0 += MAS_MEM[0]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 22
	t5_t4_mem1 += MAS_MEM[11]

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 22
	t60_in += MAS_in[2]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 22
	t60_mem0 += MM_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 22
	t60_mem1 += MM_MEM[3]

	t6_t4 = S.Task('t6_t4', length=11, delay_cost=1)
	S += t6_t4 >= 22
	t6_t4 += MM[1]

	t7_t2 = S.Task('t7_t2', length=4, delay_cost=1)
	S += t7_t2 >= 22
	t7_t2 += MAS[5]

	t10 = S.Task('t10', length=4, delay_cost=1)
	S += t10 >= 23
	t10 += MAS[4]

	t5_t4 = S.Task('t5_t4', length=11, delay_cost=1)
	S += t5_t4 >= 23
	t5_t4 += MM[1]

	t60 = S.Task('t60', length=4, delay_cost=1)
	S += t60 >= 23
	t60 += MAS[2]

	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	S += t6_t5_in >= 23
	t6_t5_in += MAS_in[1]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 23
	t6_t5_mem0 += MM_MEM[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 23
	t6_t5_mem1 += MM_MEM[3]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 23
	t7_t3_in += MAS_in[5]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 23
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 23
	t7_t3_mem1 += MAIN_MEM_r[1]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 24
	t21_in += MAS_in[4]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 24
	t21_mem0 += MAS_MEM[4]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 24
	t21_mem1 += MAIN_MEM_r[1]

	t6_t5 = S.Task('t6_t5', length=4, delay_cost=1)
	S += t6_t5 >= 24
	t6_t5 += MAS[1]

	t7_t3 = S.Task('t7_t3', length=4, delay_cost=1)
	S += t7_t3 >= 24
	t7_t3 += MAS[5]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 25
	t00_in += MAS_in[4]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 25
	t00_mem0 += MM_MEM[2]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 25
	t00_mem1 += MAS_MEM[5]

	t21 = S.Task('t21', length=4, delay_cost=1)
	S += t21 >= 25
	t21 += MAS[4]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 25
	t81_in += MAS_in[2]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 25
	t81_mem0 += MAS_MEM[4]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 25
	t81_mem1 += MAIN_MEM_r[1]

	t00 = S.Task('t00', length=4, delay_cost=1)
	S += t00 >= 26
	t00 += MAS[4]

	t220_in = S.Task('t220_in', length=1, delay_cost=1)
	S += t220_in >= 26
	t220_in += MAS_in[2]

	t220_mem0 = S.Task('t220_mem0', length=1, delay_cost=1)
	S += t220_mem0 >= 26
	t220_mem0 += MAS_MEM[4]

	t220_mem1 = S.Task('t220_mem1', length=1, delay_cost=1)
	S += t220_mem1 >= 26
	t220_mem1 += MAS_MEM[5]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 26
	t41_in += MAS_in[1]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 26
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 26
	t41_mem1 += MM_MEM[1]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 26
	t80_in += MAS_in[3]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 26
	t80_mem0 += MAS_MEM[8]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 26
	t80_mem1 += MAIN_MEM_r[1]

	t81 = S.Task('t81', length=4, delay_cost=1)
	S += t81 >= 26
	t81 += MAS[2]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 27
	t20_in += MAS_in[4]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 27
	t20_mem0 += MAS_MEM[8]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 27
	t20_mem1 += MAIN_MEM_r[1]

	t220 = S.Task('t220', length=4, delay_cost=1)
	S += t220 >= 27
	t220 += MAS[2]

	t41 = S.Task('t41', length=4, delay_cost=1)
	S += t41 >= 27
	t41 += MAS[1]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 27
	t50_in += MAS_in[0]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 27
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 27
	t50_mem1 += MM_MEM[1]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 27
	t7_t4_in += MM_in[1]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 27
	t7_t4_mem0 += MAS_MEM[10]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 27
	t7_t4_mem1 += MAS_MEM[11]

	t80 = S.Task('t80', length=4, delay_cost=1)
	S += t80 >= 27
	t80 += MAS[3]

	t20 = S.Task('t20', length=4, delay_cost=1)
	S += t20 >= 28
	t20 += MAS[4]

	t280_in = S.Task('t280_in', length=1, delay_cost=1)
	S += t280_in >= 28
	t280_in += MAS_in[5]

	t280_mem0 = S.Task('t280_mem0', length=1, delay_cost=1)
	S += t280_mem0 >= 28
	t280_mem0 += MAS_MEM[10]

	t280_mem1 = S.Task('t280_mem1', length=1, delay_cost=1)
	S += t280_mem1 >= 28
	t280_mem1 += MAIN_MEM_r[1]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 28
	t4_t5_in += MAS_in[3]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 28
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 28
	t4_t5_mem1 += MM_MEM[1]

	t50 = S.Task('t50', length=4, delay_cost=1)
	S += t50 >= 28
	t50 += MAS[0]

	t7_t4 = S.Task('t7_t4', length=11, delay_cost=1)
	S += t7_t4 >= 28
	t7_t4 += MM[1]

	t280 = S.Task('t280', length=4, delay_cost=1)
	S += t280 >= 29
	t280 += MAS[5]

	t4_t5 = S.Task('t4_t5', length=4, delay_cost=1)
	S += t4_t5 >= 29
	t4_t5 += MAS[3]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 29
	t5_t5_in += MAS_in[1]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 29
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 29
	t5_t5_mem1 += MM_MEM[1]

	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	S += t151_in >= 30
	t151_in += MAS_in[5]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 30
	t151_mem0 += MAS_MEM[0]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 30
	t151_mem1 += MAS_MEM[3]

	t3_t5_in = S.Task('t3_t5_in', length=1, delay_cost=1)
	S += t3_t5_in >= 30
	t3_t5_in += MAS_in[3]

	t3_t5_mem0 = S.Task('t3_t5_mem0', length=1, delay_cost=1)
	S += t3_t5_mem0 >= 30
	t3_t5_mem0 += MM_MEM[0]

	t3_t5_mem1 = S.Task('t3_t5_mem1', length=1, delay_cost=1)
	S += t3_t5_mem1 >= 30
	t3_t5_mem1 += MM_MEM[1]

	t5_t5 = S.Task('t5_t5', length=4, delay_cost=1)
	S += t5_t5 >= 30
	t5_t5 += MAS[1]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 30
	t9_t1_in += MAS_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 30
	t9_t1_mem0 += MAS_MEM[6]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 30
	t9_t1_mem1 += MAS_MEM[5]

	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	S += t10_t3_in >= 31
	t10_t3_in += MM_in[1]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 31
	t10_t3_mem0 += MAS_MEM[8]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 31
	t10_t3_mem1 += MAS_MEM[9]

	t151 = S.Task('t151', length=4, delay_cost=1)
	S += t151 >= 31
	t151 += MAS[5]

	t290_in = S.Task('t290_in', length=1, delay_cost=1)
	S += t290_in >= 31
	t290_in += MAS_in[1]

	t290_mem0 = S.Task('t290_mem0', length=1, delay_cost=1)
	S += t290_mem0 >= 31
	t290_mem0 += MAS_MEM[0]

	t290_mem1 = S.Task('t290_mem1', length=1, delay_cost=1)
	S += t290_mem1 >= 31
	t290_mem1 += MAS_MEM[1]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 31
	t30_in += MAS_in[2]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 31
	t30_mem0 += MM_MEM[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 31
	t30_mem1 += MM_MEM[1]

	t3_t5 = S.Task('t3_t5', length=4, delay_cost=1)
	S += t3_t5 >= 31
	t3_t5 += MAS[3]

	t9_t1 = S.Task('t9_t1', length=4, delay_cost=1)
	S += t9_t1 >= 31
	t9_t1 += MAS[0]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 31
	t9_t3_in += MM_in[0]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 31
	t9_t3_mem0 += MAS_MEM[6]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 31
	t9_t3_mem1 += MAS_MEM[5]

	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	S += c210_in >= 32
	c210_in += MAS_in[3]

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	S += c210_mem0 >= 32
	c210_mem0 += MAS_MEM[10]

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	S += c210_mem1 >= 32
	c210_mem1 += MAS_MEM[11]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 32
	t10_t1_in += MAS_in[4]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 32
	t10_t1_mem0 += MAS_MEM[8]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 32
	t10_t1_mem1 += MAS_MEM[9]

	t10_t3 = S.Task('t10_t3', length=11, delay_cost=1)
	S += t10_t3 >= 32
	t10_t3 += MM[1]

	t290 = S.Task('t290', length=4, delay_cost=1)
	S += t290 >= 32
	t290 += MAS[1]

	t30 = S.Task('t30', length=4, delay_cost=1)
	S += t30 >= 32
	t30 += MAS[2]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 32
	t40_in += MAS_in[1]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 32
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 32
	t40_mem1 += MAS_MEM[7]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 32
	t61_in += MAS_in[0]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 32
	t61_mem0 += MM_MEM[2]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 32
	t61_mem1 += MAS_MEM[3]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 32
	t9_t0_in += MAS_in[2]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 32
	t9_t0_mem0 += MAS_MEM[6]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 32
	t9_t0_mem1 += MAS_MEM[5]

	t9_t3 = S.Task('t9_t3', length=11, delay_cost=1)
	S += t9_t3 >= 32
	t9_t3 += MM[0]

	c210 = S.Task('c210', length=4, delay_cost=1)
	S += c210 >= 33
	c210 += MAS[3]

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 33
	t10_t0_in += MAS_in[5]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 33
	t10_t0_mem0 += MAS_MEM[8]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 33
	t10_t0_mem1 += MAS_MEM[9]

	t10_t1 = S.Task('t10_t1', length=4, delay_cost=1)
	S += t10_t1 >= 33
	t10_t1 += MAS[4]

	t230_in = S.Task('t230_in', length=1, delay_cost=1)
	S += t230_in >= 33
	t230_in += MAS_in[3]

	t230_mem0 = S.Task('t230_mem0', length=1, delay_cost=1)
	S += t230_mem0 >= 33
	t230_mem0 += MAS_MEM[4]

	t230_mem1 = S.Task('t230_mem1', length=1, delay_cost=1)
	S += t230_mem1 >= 33
	t230_mem1 += MAS_MEM[5]

	t40 = S.Task('t40', length=4, delay_cost=1)
	S += t40 >= 33
	t40 += MAS[1]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 33
	t51_in += MAS_in[2]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 33
	t51_mem0 += MM_MEM[2]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 33
	t51_mem1 += MAS_MEM[3]

	t61 = S.Task('t61', length=4, delay_cost=1)
	S += t61 >= 33
	t61 += MAS[0]

	t9_t0 = S.Task('t9_t0', length=4, delay_cost=1)
	S += t9_t0 >= 33
	t9_t0 += MAS[2]

	t10_t0 = S.Task('t10_t0', length=4, delay_cost=1)
	S += t10_t0 >= 34
	t10_t0 += MAS[5]

	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	S += t161_in >= 34
	t161_in += MAS_in[5]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	S += t161_mem0 >= 34
	t161_mem0 += MAS_MEM[10]

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	S += t161_mem1 >= 34
	t161_mem1 += MAS_MEM[11]

	t230 = S.Task('t230', length=4, delay_cost=1)
	S += t230 >= 34
	t230 += MAS[3]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 34
	t31_in += MAS_in[2]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 34
	t31_mem0 += MM_MEM[2]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 34
	t31_mem1 += MAS_MEM[7]

	t51 = S.Task('t51', length=4, delay_cost=1)
	S += t51 >= 34
	t51 += MAS[2]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 35
	t110_in += MAS_in[4]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 35
	t110_mem0 += MAS_MEM[4]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 35
	t110_mem1 += MAS_MEM[5]

	t161 = S.Task('t161', length=4, delay_cost=1)
	S += t161 >= 35
	t161 += MAS[5]

	t300_in = S.Task('t300_in', length=1, delay_cost=1)
	S += t300_in >= 35
	t300_in += MAS_in[2]

	t300_mem0 = S.Task('t300_mem0', length=1, delay_cost=1)
	S += t300_mem0 >= 35
	t300_mem0 += MAS_MEM[2]

	t300_mem1 = S.Task('t300_mem1', length=1, delay_cost=1)
	S += t300_mem1 >= 35
	t300_mem1 += MAS_MEM[1]

	t31 = S.Task('t31', length=4, delay_cost=1)
	S += t31 >= 35
	t31 += MAS[2]

	t110 = S.Task('t110', length=4, delay_cost=1)
	S += t110 >= 36
	t110 += MAS[4]

	t180_in = S.Task('t180_in', length=1, delay_cost=1)
	S += t180_in >= 36
	t180_in += MAS_in[0]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	S += t180_mem0 >= 36
	t180_mem0 += MAS_MEM[2]

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	S += t180_mem1 >= 36
	t180_mem1 += MAS_MEM[3]

	t300 = S.Task('t300', length=4, delay_cost=1)
	S += t300 >= 36
	t300 += MAS[2]

	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	S += t9_t2_in >= 36
	t9_t2_in += MM_in[1]

	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	S += t9_t2_mem0 >= 36
	t9_t2_mem0 += MAS_MEM[4]

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	S += t9_t2_mem1 >= 36
	t9_t2_mem1 += MAS_MEM[1]

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	S += c210_w >= 37
	c210_w += MAIN_MEM_w

	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	S += t10_t2_in >= 37
	t10_t2_in += MM_in[1]

	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	S += t10_t2_mem0 >= 37
	t10_t2_mem0 += MAS_MEM[10]

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	S += t10_t2_mem1 >= 37
	t10_t2_mem1 += MAS_MEM[9]

	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	S += t150_in >= 37
	t150_in += MAS_in[3]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	S += t150_mem0 >= 37
	t150_mem0 += MAS_MEM[8]

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	S += t150_mem1 >= 37
	t150_mem1 += MAS_MEM[3]

	t180 = S.Task('t180', length=4, delay_cost=1)
	S += t180 >= 37
	t180 += MAS[0]

	t221_in = S.Task('t221_in', length=1, delay_cost=1)
	S += t221_in >= 37
	t221_in += MAS_in[5]

	t221_mem0 = S.Task('t221_mem0', length=1, delay_cost=1)
	S += t221_mem0 >= 37
	t221_mem0 += MAS_MEM[0]

	t221_mem1 = S.Task('t221_mem1', length=1, delay_cost=1)
	S += t221_mem1 >= 37
	t221_mem1 += MAS_MEM[1]

	t291_in = S.Task('t291_in', length=1, delay_cost=1)
	S += t291_in >= 37
	t291_in += MAS_in[2]

	t291_mem0 = S.Task('t291_mem0', length=1, delay_cost=1)
	S += t291_mem0 >= 37
	t291_mem0 += MAS_MEM[4]

	t291_mem1 = S.Task('t291_mem1', length=1, delay_cost=1)
	S += t291_mem1 >= 37
	t291_mem1 += MAS_MEM[5]

	t9_t2 = S.Task('t9_t2', length=11, delay_cost=1)
	S += t9_t2 >= 37
	t9_t2 += MM[1]

	t10_t2 = S.Task('t10_t2', length=11, delay_cost=1)
	S += t10_t2 >= 38
	t10_t2 += MM[1]

	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	S += t111_in >= 38
	t111_in += MAS_in[0]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	S += t111_mem0 >= 38
	t111_mem0 += MAS_MEM[4]

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	S += t111_mem1 >= 38
	t111_mem1 += MAS_MEM[5]

	t150 = S.Task('t150', length=4, delay_cost=1)
	S += t150 >= 38
	t150 += MAS[3]

	t181_in = S.Task('t181_in', length=1, delay_cost=1)
	S += t181_in >= 38
	t181_in += MAS_in[5]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	S += t181_mem0 >= 38
	t181_mem0 += MAS_MEM[2]

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	S += t181_mem1 >= 38
	t181_mem1 += MAS_MEM[3]

	t221 = S.Task('t221', length=4, delay_cost=1)
	S += t221 >= 38
	t221 += MAS[5]

	t291 = S.Task('t291', length=4, delay_cost=1)
	S += t291 >= 38
	t291 += MAS[2]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 38
	t71_in += MAS_in[2]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 38
	t71_mem0 += MM_MEM[2]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 38
	t71_mem1 += MAS_MEM[7]

	t111 = S.Task('t111', length=4, delay_cost=1)
	S += t111 >= 39
	t111 += MAS[0]

	t181 = S.Task('t181', length=4, delay_cost=1)
	S += t181 >= 39
	t181 += MAS[5]

	t310_in = S.Task('t310_in', length=1, delay_cost=1)
	S += t310_in >= 39
	t310_in += MAS_in[3]

	t310_mem0 = S.Task('t310_mem0', length=1, delay_cost=1)
	S += t310_mem0 >= 39
	t310_mem0 += MAS_MEM[4]

	t310_mem1 = S.Task('t310_mem1', length=1, delay_cost=1)
	S += t310_mem1 >= 39
	t310_mem1 += MAIN_MEM_r[1]

	t71 = S.Task('t71', length=4, delay_cost=1)
	S += t71 >= 39
	t71 += MAS[2]

	t190_in = S.Task('t190_in', length=1, delay_cost=1)
	S += t190_in >= 40
	t190_in += MAS_in[5]

	t190_mem0 = S.Task('t190_mem0', length=1, delay_cost=1)
	S += t190_mem0 >= 40
	t190_mem0 += MAS_MEM[0]

	t190_mem1 = S.Task('t190_mem1', length=1, delay_cost=1)
	S += t190_mem1 >= 40
	t190_mem1 += MAS_MEM[9]

	t310 = S.Task('t310', length=4, delay_cost=1)
	S += t310 >= 40
	t310 += MAS[3]

	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	S += t160_in >= 41
	t160_in += MAS_in[2]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	S += t160_mem0 >= 41
	t160_mem0 += MAS_MEM[6]

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	S += t160_mem1 >= 41
	t160_mem1 += MAS_MEM[7]

	t190 = S.Task('t190', length=4, delay_cost=1)
	S += t190 >= 41
	t190 += MAS[5]

	t231_in = S.Task('t231_in', length=1, delay_cost=1)
	S += t231_in >= 41
	t231_in += MAS_in[4]

	t231_mem0 = S.Task('t231_mem0', length=1, delay_cost=1)
	S += t231_mem0 >= 41
	t231_mem0 += MAS_MEM[10]

	t231_mem1 = S.Task('t231_mem1', length=1, delay_cost=1)
	S += t231_mem1 >= 41
	t231_mem1 += MAS_MEM[1]

	t301_in = S.Task('t301_in', length=1, delay_cost=1)
	S += t301_in >= 41
	t301_in += MAS_in[1]

	t301_mem0 = S.Task('t301_mem0', length=1, delay_cost=1)
	S += t301_mem0 >= 41
	t301_mem0 += MAS_MEM[4]

	t301_mem1 = S.Task('t301_mem1', length=1, delay_cost=1)
	S += t301_mem1 >= 41
	t301_mem1 += MAS_MEM[5]

	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	S += t101_in >= 42
	t101_in += MAS_in[1]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	S += t101_mem0 >= 42
	t101_mem0 += MM_MEM[2]

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	S += t101_mem1 >= 42
	t101_mem1 += MM_MEM[3]

	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	S += t120_in >= 42
	t120_in += MAS_in[0]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	S += t120_mem0 >= 42
	t120_mem0 += MAS_MEM[8]

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	S += t120_mem1 >= 42
	t120_mem1 += MAS_MEM[1]

	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	S += t121_in >= 42
	t121_in += MAS_in[3]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	S += t121_mem0 >= 42
	t121_mem0 += MAS_MEM[0]

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	S += t121_mem1 >= 42
	t121_mem1 += MAS_MEM[9]

	t160 = S.Task('t160', length=4, delay_cost=1)
	S += t160 >= 42
	t160 += MAS[2]

	t231 = S.Task('t231', length=4, delay_cost=1)
	S += t231 >= 42
	t231 += MAS[4]

	t261_in = S.Task('t261_in', length=1, delay_cost=1)
	S += t261_in >= 42
	t261_in += MAS_in[5]

	t261_mem0 = S.Task('t261_mem0', length=1, delay_cost=1)
	S += t261_mem0 >= 42
	t261_mem0 += MAS_MEM[4]

	t261_mem1 = S.Task('t261_mem1', length=1, delay_cost=1)
	S += t261_mem1 >= 42
	t261_mem1 += MAS_MEM[5]

	t301 = S.Task('t301', length=4, delay_cost=1)
	S += t301 >= 42
	t301 += MAS[1]

	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	S += t91_in >= 42
	t91_in += MAS_in[2]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	S += t91_mem0 >= 42
	t91_mem0 += MM_MEM[0]

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	S += t91_mem1 >= 42
	t91_mem1 += MM_MEM[1]

	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	S += c010_in >= 43
	c010_in += MAS_in[0]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 43
	c010_mem0 += MAS_MEM[6]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 43
	c010_mem1 += MAS_MEM[7]

	t101 = S.Task('t101', length=4, delay_cost=1)
	S += t101 >= 43
	t101 += MAS[1]

	t10_t5_in = S.Task('t10_t5_in', length=1, delay_cost=1)
	S += t10_t5_in >= 43
	t10_t5_in += MAS_in[1]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	S += t10_t5_mem0 >= 43
	t10_t5_mem0 += MM_MEM[2]

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	S += t10_t5_mem1 >= 43
	t10_t5_mem1 += MM_MEM[3]

	t120 = S.Task('t120', length=4, delay_cost=1)
	S += t120 >= 43
	t120 += MAS[0]

	t121 = S.Task('t121', length=4, delay_cost=1)
	S += t121 >= 43
	t121 += MAS[3]

	t191_in = S.Task('t191_in', length=1, delay_cost=1)
	S += t191_in >= 43
	t191_in += MAS_in[5]

	t191_mem0 = S.Task('t191_mem0', length=1, delay_cost=1)
	S += t191_mem0 >= 43
	t191_mem0 += MAS_MEM[10]

	t191_mem1 = S.Task('t191_mem1', length=1, delay_cost=1)
	S += t191_mem1 >= 43
	t191_mem1 += MAS_MEM[1]

	t261 = S.Task('t261', length=4, delay_cost=1)
	S += t261 >= 43
	t261 += MAS[5]

	t91 = S.Task('t91', length=4, delay_cost=1)
	S += t91 >= 43
	t91 += MAS[2]

	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	S += t9_t5_in >= 43
	t9_t5_in += MAS_in[2]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	S += t9_t5_mem0 >= 43
	t9_t5_mem0 += MM_MEM[0]

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	S += t9_t5_mem1 >= 43
	t9_t5_mem1 += MM_MEM[1]

	c010 = S.Task('c010', length=4, delay_cost=1)
	S += c010 >= 44
	c010 += MAS[0]

	t10_t5 = S.Task('t10_t5', length=4, delay_cost=1)
	S += t10_t5 >= 44
	t10_t5 += MAS[1]

	t191 = S.Task('t191', length=4, delay_cost=1)
	S += t191 >= 44
	t191 += MAS[5]

	t200_in = S.Task('t200_in', length=1, delay_cost=1)
	S += t200_in >= 44
	t200_in += MAS_in[2]

	t200_mem0 = S.Task('t200_mem0', length=1, delay_cost=1)
	S += t200_mem0 >= 44
	t200_mem0 += MAS_MEM[10]

	t200_mem1 = S.Task('t200_mem1', length=1, delay_cost=1)
	S += t200_mem1 >= 44
	t200_mem1 += MAS_MEM[11]

	t9_t5 = S.Task('t9_t5', length=4, delay_cost=1)
	S += t9_t5 >= 44
	t9_t5 += MAS[2]

	t200 = S.Task('t200', length=4, delay_cost=1)
	S += t200 >= 45
	t200 += MAS[2]

	t240_in = S.Task('t240_in', length=1, delay_cost=1)
	S += t240_in >= 45
	t240_in += MAS_in[4]

	t240_mem0 = S.Task('t240_mem0', length=1, delay_cost=1)
	S += t240_mem0 >= 45
	t240_mem0 += MAS_MEM[6]

	t240_mem1 = S.Task('t240_mem1', length=1, delay_cost=1)
	S += t240_mem1 >= 45
	t240_mem1 += MAS_MEM[9]

	t241_in = S.Task('t241_in', length=1, delay_cost=1)
	S += t241_in >= 45
	t241_in += MAS_in[2]

	t241_mem0 = S.Task('t241_mem0', length=1, delay_cost=1)
	S += t241_mem0 >= 45
	t241_mem0 += MAS_MEM[8]

	t241_mem1 = S.Task('t241_mem1', length=1, delay_cost=1)
	S += t241_mem1 >= 45
	t241_mem1 += MAS_MEM[7]

	t311_in = S.Task('t311_in', length=1, delay_cost=1)
	S += t311_in >= 45
	t311_in += MAS_in[5]

	t311_mem0 = S.Task('t311_mem0', length=1, delay_cost=1)
	S += t311_mem0 >= 45
	t311_mem0 += MAS_MEM[2]

	t311_mem1 = S.Task('t311_mem1', length=1, delay_cost=1)
	S += t311_mem1 >= 45
	t311_mem1 += MAIN_MEM_r[1]

	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	S += t130_in >= 46
	t130_in += MAS_in[3]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	S += t130_mem0 >= 46
	t130_mem0 += MAS_MEM[8]

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	S += t130_mem1 >= 46
	t130_mem1 += MAS_MEM[1]

	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	S += t131_in >= 46
	t131_in += MAS_in[4]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	S += t131_mem0 >= 46
	t131_mem0 += MAS_MEM[0]

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	S += t131_mem1 >= 46
	t131_mem1 += MAS_MEM[7]

	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	S += t171_in >= 46
	t171_in += MAS_in[5]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	S += t171_mem0 >= 46
	t171_mem0 += MAS_MEM[4]

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	S += t171_mem1 >= 46
	t171_mem1 += MAS_MEM[11]

	t240 = S.Task('t240', length=4, delay_cost=1)
	S += t240 >= 46
	t240 += MAS[4]

	t241 = S.Task('t241', length=4, delay_cost=1)
	S += t241 >= 46
	t241 += MAS[2]

	t271_in = S.Task('t271_in', length=1, delay_cost=1)
	S += t271_in >= 46
	t271_in += MAS_in[0]

	t271_mem0 = S.Task('t271_mem0', length=1, delay_cost=1)
	S += t271_mem0 >= 46
	t271_mem0 += MAS_MEM[10]

	t271_mem1 = S.Task('t271_mem1', length=1, delay_cost=1)
	S += t271_mem1 >= 46
	t271_mem1 += MAS_MEM[5]

	t311 = S.Task('t311', length=4, delay_cost=1)
	S += t311 >= 46
	t311 += MAS[5]

	t130 = S.Task('t130', length=4, delay_cost=1)
	S += t130 >= 47
	t130 += MAS[3]

	t131 = S.Task('t131', length=4, delay_cost=1)
	S += t131 >= 47
	t131 += MAS[4]

	t171 = S.Task('t171', length=4, delay_cost=1)
	S += t171 >= 47
	t171 += MAS[5]

	t201_in = S.Task('t201_in', length=1, delay_cost=1)
	S += t201_in >= 47
	t201_in += MAS_in[3]

	t201_mem0 = S.Task('t201_mem0', length=1, delay_cost=1)
	S += t201_mem0 >= 47
	t201_mem0 += MAS_MEM[10]

	t201_mem1 = S.Task('t201_mem1', length=1, delay_cost=1)
	S += t201_mem1 >= 47
	t201_mem1 += MAS_MEM[11]

	t271 = S.Task('t271', length=4, delay_cost=1)
	S += t271 >= 47
	t271 += MAS[0]

	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	S += t90_in >= 47
	t90_in += MAS_in[2]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	S += t90_mem0 >= 47
	t90_mem0 += MM_MEM[2]

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	S += t90_mem1 >= 47
	t90_mem1 += MAS_MEM[5]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 48
	c010_w += MAIN_MEM_w

	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	S += t100_in >= 48
	t100_in += MAS_in[2]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	S += t100_mem0 >= 48
	t100_mem0 += MM_MEM[2]

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	S += t100_mem1 >= 48
	t100_mem1 += MAS_MEM[3]

	t201 = S.Task('t201', length=4, delay_cost=1)
	S += t201 >= 48
	t201 += MAS[3]

	t90 = S.Task('t90', length=4, delay_cost=1)
	S += t90 >= 48
	t90 += MAS[2]

	t100 = S.Task('t100', length=4, delay_cost=1)
	S += t100 >= 49
	t100 += MAS[2]

	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	S += c111_in >= 50
	c111_in += MAS_in[2]

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	S += c111_mem0 >= 50
	c111_mem0 += MAS_MEM[2]

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	S += c111_mem1 >= 50
	c111_mem1 += MAS_MEM[11]

	t281_in = S.Task('t281_in', length=1, delay_cost=1)
	S += t281_in >= 50
	t281_in += MAS_in[5]

	t281_mem0 = S.Task('t281_mem0', length=1, delay_cost=1)
	S += t281_mem0 >= 50
	t281_mem0 += MAS_MEM[0]

	t281_mem1 = S.Task('t281_mem1', length=1, delay_cost=1)
	S += t281_mem1 >= 50
	t281_mem1 += MAIN_MEM_r[1]

	c111 = S.Task('c111', length=4, delay_cost=1)
	S += c111 >= 51
	c111 += MAS[2]

	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	S += t170_in >= 51
	t170_in += MAS_in[2]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	S += t170_mem0 >= 51
	t170_mem0 += MAS_MEM[4]

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	S += t170_mem1 >= 51
	t170_mem1 += MAS_MEM[5]

	t281 = S.Task('t281', length=4, delay_cost=1)
	S += t281 >= 51
	t281 += MAS[5]

	t170 = S.Task('t170', length=4, delay_cost=1)
	S += t170 >= 52
	t170 += MAS[2]

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	S += c111_w >= 55
	c111_w += MAIN_MEM_w


	# new tasks
	t140 = S.Task('t140', length=4, delay_cost=1)
	t140 += alt(MAS)
	t140_in = S.Task('t140_in', length=1, delay_cost=1)
	t140_in += alt(MAS_in)
	S += t140_in*MAS_in[0]<=t140*MAS[0]

	S += t140_in*MAS_in[1]<=t140*MAS[1]

	S += t140_in*MAS_in[2]<=t140*MAS[2]

	S += t140_in*MAS_in[3]<=t140*MAS[3]

	S += t140_in*MAS_in[4]<=t140*MAS[4]

	S += t140_in*MAS_in[5]<=t140*MAS[5]

	t140_mem0 = S.Task('t140_mem0', length=1, delay_cost=1)
	t140_mem0 += MAS_MEM[6]
	S += 50 < t140_mem0
	S += t140_mem0 <= t140

	t140_mem1 = S.Task('t140_mem1', length=1, delay_cost=1)
	t140_mem1 += MAIN_MEM_r[1]
	S += t140_mem1 <= t140

	c001 = S.Task('c001', length=4, delay_cost=1)
	c001 += alt(MAS)
	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	c001_in += alt(MAS_in)
	S += c001_in*MAS_in[0]<=c001*MAS[0]

	S += c001_in*MAS_in[1]<=c001*MAS[1]

	S += c001_in*MAS_in[2]<=c001*MAS[2]

	S += c001_in*MAS_in[3]<=c001*MAS[3]

	S += c001_in*MAS_in[4]<=c001*MAS[4]

	S += c001_in*MAS_in[5]<=c001*MAS[5]

	S += 21<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[8]
	S += 50 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += MAS_MEM[9]
	S += 50 < c001_mem1
	S += c001_mem1 <= c001

	c011 = S.Task('c011', length=4, delay_cost=1)
	c011 += alt(MAS)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MAS_in)
	S += c011_in*MAS_in[0]<=c011*MAS[0]

	S += c011_in*MAS_in[1]<=c011*MAS[1]

	S += c011_in*MAS_in[2]<=c011*MAS[2]

	S += c011_in*MAS_in[3]<=c011*MAS[3]

	S += c011_in*MAS_in[4]<=c011*MAS[4]

	S += c011_in*MAS_in[5]<=c011*MAS[5]

	S += 46<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MAS_MEM[10]
	S += 49 < c011_mem0
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += MAS_MEM[11]
	S += 49 < c011_mem1
	S += c011_mem1 <= c011

	c110 = S.Task('c110', length=4, delay_cost=1)
	c110 += alt(MAS)
	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	c110_in += alt(MAS_in)
	S += c110_in*MAS_in[0]<=c110*MAS[0]

	S += c110_in*MAS_in[1]<=c110*MAS[1]

	S += c110_in*MAS_in[2]<=c110*MAS[2]

	S += c110_in*MAS_in[3]<=c110*MAS[3]

	S += c110_in*MAS_in[4]<=c110*MAS[4]

	S += c110_in*MAS_in[5]<=c110*MAS[5]

	S += 24<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[4]
	S += 52 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MAS_MEM[5]
	S += 55 < c110_mem1
	S += c110_mem1 <= c110

	t210 = S.Task('t210', length=4, delay_cost=1)
	t210 += alt(MAS)
	t210_in = S.Task('t210_in', length=1, delay_cost=1)
	t210_in += alt(MAS_in)
	S += t210_in*MAS_in[0]<=t210*MAS[0]

	S += t210_in*MAS_in[1]<=t210*MAS[1]

	S += t210_in*MAS_in[2]<=t210*MAS[2]

	S += t210_in*MAS_in[3]<=t210*MAS[3]

	S += t210_in*MAS_in[4]<=t210*MAS[4]

	S += t210_in*MAS_in[5]<=t210*MAS[5]

	t210_mem0 = S.Task('t210_mem0', length=1, delay_cost=1)
	t210_mem0 += MAS_MEM[4]
	S += 48 < t210_mem0
	S += t210_mem0 <= t210

	t210_mem1 = S.Task('t210_mem1', length=1, delay_cost=1)
	t210_mem1 += MAS_MEM[5]
	S += 51 < t210_mem1
	S += t210_mem1 <= t210

	t211 = S.Task('t211', length=4, delay_cost=1)
	t211 += alt(MAS)
	t211_in = S.Task('t211_in', length=1, delay_cost=1)
	t211_in += alt(MAS_in)
	S += t211_in*MAS_in[0]<=t211*MAS[0]

	S += t211_in*MAS_in[1]<=t211*MAS[1]

	S += t211_in*MAS_in[2]<=t211*MAS[2]

	S += t211_in*MAS_in[3]<=t211*MAS[3]

	S += t211_in*MAS_in[4]<=t211*MAS[4]

	S += t211_in*MAS_in[5]<=t211*MAS[5]

	t211_mem0 = S.Task('t211_mem0', length=1, delay_cost=1)
	t211_mem0 += MAS_MEM[6]
	S += 51 < t211_mem0
	S += t211_mem0 <= t211

	t211_mem1 = S.Task('t211_mem1', length=1, delay_cost=1)
	t211_mem1 += MAS_MEM[5]
	S += 46 < t211_mem1
	S += t211_mem1 <= t211

	t250 = S.Task('t250', length=4, delay_cost=1)
	t250 += alt(MAS)
	t250_in = S.Task('t250_in', length=1, delay_cost=1)
	t250_in += alt(MAS_in)
	S += t250_in*MAS_in[0]<=t250*MAS[0]

	S += t250_in*MAS_in[1]<=t250*MAS[1]

	S += t250_in*MAS_in[2]<=t250*MAS[2]

	S += t250_in*MAS_in[3]<=t250*MAS[3]

	S += t250_in*MAS_in[4]<=t250*MAS[4]

	S += t250_in*MAS_in[5]<=t250*MAS[5]

	t250_mem0 = S.Task('t250_mem0', length=1, delay_cost=1)
	t250_mem0 += MAIN_MEM_r[0]
	S += t250_mem0 <= t250

	t250_mem1 = S.Task('t250_mem1', length=1, delay_cost=1)
	t250_mem1 += MAS_MEM[9]
	S += 49 < t250_mem1
	S += t250_mem1 <= t250

	t251 = S.Task('t251', length=4, delay_cost=1)
	t251 += alt(MAS)
	t251_in = S.Task('t251_in', length=1, delay_cost=1)
	t251_in += alt(MAS_in)
	S += t251_in*MAS_in[0]<=t251*MAS[0]

	S += t251_in*MAS_in[1]<=t251*MAS[1]

	S += t251_in*MAS_in[2]<=t251*MAS[2]

	S += t251_in*MAS_in[3]<=t251*MAS[3]

	S += t251_in*MAS_in[4]<=t251*MAS[4]

	S += t251_in*MAS_in[5]<=t251*MAS[5]

	t251_mem0 = S.Task('t251_mem0', length=1, delay_cost=1)
	t251_mem0 += MAIN_MEM_r[0]
	S += t251_mem0 <= t251

	t251_mem1 = S.Task('t251_mem1', length=1, delay_cost=1)
	t251_mem1 += MAS_MEM[5]
	S += 49 < t251_mem1
	S += t251_mem1 <= t251

	c211 = S.Task('c211', length=4, delay_cost=1)
	c211 += alt(MAS)
	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	c211_in += alt(MAS_in)
	S += c211_in*MAS_in[0]<=c211*MAS[0]

	S += c211_in*MAS_in[1]<=c211*MAS[1]

	S += c211_in*MAS_in[2]<=c211*MAS[2]

	S += c211_in*MAS_in[3]<=c211*MAS[3]

	S += c211_in*MAS_in[4]<=c211*MAS[4]

	S += c211_in*MAS_in[5]<=c211*MAS[5]

	S += 51<c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += MAS_MEM[10]
	S += 54 < c211_mem0
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += MAS_MEM[11]
	S += 54 < c211_mem1
	S += c211_mem1 <= c211

	c000 = S.Task('c000', length=4, delay_cost=1)
	c000 += alt(MAS)
	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	c000_in += alt(MAS_in)
	S += c000_in*MAS_in[0]<=c000*MAS[0]

	S += c000_in*MAS_in[1]<=c000*MAS[1]

	S += c000_in*MAS_in[2]<=c000*MAS[2]

	S += c000_in*MAS_in[3]<=c000*MAS[3]

	S += c000_in*MAS_in[4]<=c000*MAS[4]

	S += c000_in*MAS_in[5]<=c000*MAS[5]

	S += 23<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[6]
	S += 50 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (t140*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (t140*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (t140*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (t140*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += (t140*MAS[4])-1 < c000_mem1*MAS_MEM[9]
	S += (t140*MAS[5])-1 < c000_mem1*MAS_MEM[11]
	S += c000_mem1 <= c000

	c200 = S.Task('c200', length=4, delay_cost=1)
	c200 += alt(MAS)
	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MAS_in)
	S += c200_in*MAS_in[0]<=c200*MAS[0]

	S += c200_in*MAS_in[1]<=c200*MAS[1]

	S += c200_in*MAS_in[2]<=c200*MAS[2]

	S += c200_in*MAS_in[3]<=c200*MAS[3]

	S += c200_in*MAS_in[4]<=c200*MAS[4]

	S += c200_in*MAS_in[5]<=c200*MAS[5]

	S += 28<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(MAS_MEM)
	S += (t210*MAS[0])-1 < c200_mem0*MAS_MEM[0]
	S += (t210*MAS[1])-1 < c200_mem0*MAS_MEM[2]
	S += (t210*MAS[2])-1 < c200_mem0*MAS_MEM[4]
	S += (t210*MAS[3])-1 < c200_mem0*MAS_MEM[6]
	S += (t210*MAS[4])-1 < c200_mem0*MAS_MEM[8]
	S += (t210*MAS[5])-1 < c200_mem0*MAS_MEM[10]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAS_MEM[5]
	S += 52 < c200_mem1
	S += c200_mem1 <= c200

	c201 = S.Task('c201', length=4, delay_cost=1)
	c201 += alt(MAS)
	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MAS_in)
	S += c201_in*MAS_in[0]<=c201*MAS[0]

	S += c201_in*MAS_in[1]<=c201*MAS[1]

	S += c201_in*MAS_in[2]<=c201*MAS[2]

	S += c201_in*MAS_in[3]<=c201*MAS[3]

	S += c201_in*MAS_in[4]<=c201*MAS[4]

	S += c201_in*MAS_in[5]<=c201*MAS[5]

	S += 26<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MAS_MEM)
	S += (t211*MAS[0])-1 < c201_mem0*MAS_MEM[0]
	S += (t211*MAS[1])-1 < c201_mem0*MAS_MEM[2]
	S += (t211*MAS[2])-1 < c201_mem0*MAS_MEM[4]
	S += (t211*MAS[3])-1 < c201_mem0*MAS_MEM[6]
	S += (t211*MAS[4])-1 < c201_mem0*MAS_MEM[8]
	S += (t211*MAS[5])-1 < c201_mem0*MAS_MEM[10]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += MAS_MEM[3]
	S += 46 < c201_mem1
	S += c201_mem1 <= c201

	c100 = S.Task('c100', length=4, delay_cost=1)
	c100 += alt(MAS)
	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	c100_in += alt(MAS_in)
	S += c100_in*MAS_in[0]<=c100*MAS[0]

	S += c100_in*MAS_in[1]<=c100*MAS[1]

	S += c100_in*MAS_in[2]<=c100*MAS[2]

	S += c100_in*MAS_in[3]<=c100*MAS[3]

	S += c100_in*MAS_in[4]<=c100*MAS[4]

	S += c100_in*MAS_in[5]<=c100*MAS[5]

	S += 22<c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(MAS_MEM)
	S += (t250*MAS[0])-1 < c100_mem0*MAS_MEM[0]
	S += (t250*MAS[1])-1 < c100_mem0*MAS_MEM[2]
	S += (t250*MAS[2])-1 < c100_mem0*MAS_MEM[4]
	S += (t250*MAS[3])-1 < c100_mem0*MAS_MEM[6]
	S += (t250*MAS[4])-1 < c100_mem0*MAS_MEM[8]
	S += (t250*MAS[5])-1 < c100_mem0*MAS_MEM[10]
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += alt(MAS_MEM)
	S += (t250*MAS[0])-1 < c100_mem1*MAS_MEM[1]
	S += (t250*MAS[1])-1 < c100_mem1*MAS_MEM[3]
	S += (t250*MAS[2])-1 < c100_mem1*MAS_MEM[5]
	S += (t250*MAS[3])-1 < c100_mem1*MAS_MEM[7]
	S += (t250*MAS[4])-1 < c100_mem1*MAS_MEM[9]
	S += (t250*MAS[5])-1 < c100_mem1*MAS_MEM[11]
	S += c100_mem1 <= c100

	c101 = S.Task('c101', length=4, delay_cost=1)
	c101 += alt(MAS)
	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	c101_in += alt(MAS_in)
	S += c101_in*MAS_in[0]<=c101*MAS[0]

	S += c101_in*MAS_in[1]<=c101*MAS[1]

	S += c101_in*MAS_in[2]<=c101*MAS[2]

	S += c101_in*MAS_in[3]<=c101*MAS[3]

	S += c101_in*MAS_in[4]<=c101*MAS[4]

	S += c101_in*MAS_in[5]<=c101*MAS[5]

	S += 22<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MAS_MEM)
	S += (t251*MAS[0])-1 < c101_mem0*MAS_MEM[0]
	S += (t251*MAS[1])-1 < c101_mem0*MAS_MEM[2]
	S += (t251*MAS[2])-1 < c101_mem0*MAS_MEM[4]
	S += (t251*MAS[3])-1 < c101_mem0*MAS_MEM[6]
	S += (t251*MAS[4])-1 < c101_mem0*MAS_MEM[8]
	S += (t251*MAS[5])-1 < c101_mem0*MAS_MEM[10]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(MAS_MEM)
	S += (t251*MAS[0])-1 < c101_mem1*MAS_MEM[1]
	S += (t251*MAS[1])-1 < c101_mem1*MAS_MEM[3]
	S += (t251*MAS[2])-1 < c101_mem1*MAS_MEM[5]
	S += (t251*MAS[3])-1 < c101_mem1*MAS_MEM[7]
	S += (t251*MAS[4])-1 < c101_mem1*MAS_MEM[9]
	S += (t251*MAS[5])-1 < c101_mem1*MAS_MEM[11]
	S += c101_mem1 <= c101

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage4MAS6/SQR012345/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

