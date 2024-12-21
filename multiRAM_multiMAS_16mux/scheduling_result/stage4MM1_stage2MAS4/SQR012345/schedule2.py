from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 157
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	t0_t3_in = S.Task('t0_t3_in', length=1, delay_cost=1)
	S += t0_t3_in >= 0
	t0_t3_in += MM_in[0]

	t0_t3_mem0 = S.Task('t0_t3_mem0', length=1, delay_cost=1)
	S += t0_t3_mem0 >= 0
	t0_t3_mem0 += MAIN_MEM_r[0]

	t0_t3_mem1 = S.Task('t0_t3_mem1', length=1, delay_cost=1)
	S += t0_t3_mem1 >= 0
	t0_t3_mem1 += MAIN_MEM_r[1]

	t0_t3 = S.Task('t0_t3', length=4, delay_cost=1)
	S += t0_t3 >= 1
	t0_t3 += MM[0]

	t3_t3_in = S.Task('t3_t3_in', length=1, delay_cost=1)
	S += t3_t3_in >= 1
	t3_t3_in += MAS_in[0]

	t3_t3_mem0 = S.Task('t3_t3_mem0', length=1, delay_cost=1)
	S += t3_t3_mem0 >= 1
	t3_t3_mem0 += MAIN_MEM_r[0]

	t3_t3_mem1 = S.Task('t3_t3_mem1', length=1, delay_cost=1)
	S += t3_t3_mem1 >= 1
	t3_t3_mem1 += MAIN_MEM_r[1]

	t3_t3 = S.Task('t3_t3', length=2, delay_cost=1)
	S += t3_t3 >= 2
	t3_t3 += MAS[0]

	t5_t3_in = S.Task('t5_t3_in', length=1, delay_cost=1)
	S += t5_t3_in >= 2
	t5_t3_in += MAS_in[0]

	t5_t3_mem0 = S.Task('t5_t3_mem0', length=1, delay_cost=1)
	S += t5_t3_mem0 >= 2
	t5_t3_mem0 += MAIN_MEM_r[0]

	t5_t3_mem1 = S.Task('t5_t3_mem1', length=1, delay_cost=1)
	S += t5_t3_mem1 >= 2
	t5_t3_mem1 += MAIN_MEM_r[1]

	t4_t1_in = S.Task('t4_t1_in', length=1, delay_cost=1)
	S += t4_t1_in >= 3
	t4_t1_in += MAS_in[0]

	t4_t1_mem0 = S.Task('t4_t1_mem0', length=1, delay_cost=1)
	S += t4_t1_mem0 >= 3
	t4_t1_mem0 += MAIN_MEM_r[0]

	t4_t1_mem1 = S.Task('t4_t1_mem1', length=1, delay_cost=1)
	S += t4_t1_mem1 >= 3
	t4_t1_mem1 += MAIN_MEM_r[1]

	t5_t3 = S.Task('t5_t3', length=2, delay_cost=1)
	S += t5_t3 >= 3
	t5_t3 += MAS[0]

	t01_in = S.Task('t01_in', length=1, delay_cost=1)
	S += t01_in >= 4
	t01_in += MAS_in[3]

	t01_mem0 = S.Task('t01_mem0', length=1, delay_cost=1)
	S += t01_mem0 >= 4
	t01_mem0 += MM_MEM[0]

	t01_mem1 = S.Task('t01_mem1', length=1, delay_cost=1)
	S += t01_mem1 >= 4
	t01_mem1 += MM_MEM[1]

	t4_t1 = S.Task('t4_t1', length=2, delay_cost=1)
	S += t4_t1 >= 4
	t4_t1 += MAS[0]

	t5_t2_in = S.Task('t5_t2_in', length=1, delay_cost=1)
	S += t5_t2_in >= 4
	t5_t2_in += MAS_in[0]

	t5_t2_mem0 = S.Task('t5_t2_mem0', length=1, delay_cost=1)
	S += t5_t2_mem0 >= 4
	t5_t2_mem0 += MAIN_MEM_r[0]

	t5_t2_mem1 = S.Task('t5_t2_mem1', length=1, delay_cost=1)
	S += t5_t2_mem1 >= 4
	t5_t2_mem1 += MAIN_MEM_r[1]

	t01 = S.Task('t01', length=2, delay_cost=1)
	S += t01 >= 5
	t01 += MAS[3]

	t0_t5_in = S.Task('t0_t5_in', length=1, delay_cost=1)
	S += t0_t5_in >= 5
	t0_t5_in += MAS_in[2]

	t0_t5_mem0 = S.Task('t0_t5_mem0', length=1, delay_cost=1)
	S += t0_t5_mem0 >= 5
	t0_t5_mem0 += MM_MEM[0]

	t0_t5_mem1 = S.Task('t0_t5_mem1', length=1, delay_cost=1)
	S += t0_t5_mem1 >= 5
	t0_t5_mem1 += MM_MEM[1]

	t5_t2 = S.Task('t5_t2', length=2, delay_cost=1)
	S += t5_t2 >= 5
	t5_t2 += MAS[0]

	t6_t3_in = S.Task('t6_t3_in', length=1, delay_cost=1)
	S += t6_t3_in >= 5
	t6_t3_in += MAS_in[0]

	t6_t3_mem0 = S.Task('t6_t3_mem0', length=1, delay_cost=1)
	S += t6_t3_mem0 >= 5
	t6_t3_mem0 += MAIN_MEM_r[0]

	t6_t3_mem1 = S.Task('t6_t3_mem1', length=1, delay_cost=1)
	S += t6_t3_mem1 >= 5
	t6_t3_mem1 += MAIN_MEM_r[1]

	t0_t5 = S.Task('t0_t5', length=2, delay_cost=1)
	S += t0_t5 >= 6
	t0_t5 += MAS[2]

	t5_t4_in = S.Task('t5_t4_in', length=1, delay_cost=1)
	S += t5_t4_in >= 6
	t5_t4_in += MM_in[0]

	t5_t4_mem0 = S.Task('t5_t4_mem0', length=1, delay_cost=1)
	S += t5_t4_mem0 >= 6
	t5_t4_mem0 += MAS_MEM[0]

	t5_t4_mem1 = S.Task('t5_t4_mem1', length=1, delay_cost=1)
	S += t5_t4_mem1 >= 6
	t5_t4_mem1 += MAS_MEM[1]

	t6_t3 = S.Task('t6_t3', length=2, delay_cost=1)
	S += t6_t3 >= 6
	t6_t3 += MAS[0]

	t7_t2_in = S.Task('t7_t2_in', length=1, delay_cost=1)
	S += t7_t2_in >= 6
	t7_t2_in += MAS_in[0]

	t7_t2_mem0 = S.Task('t7_t2_mem0', length=1, delay_cost=1)
	S += t7_t2_mem0 >= 6
	t7_t2_mem0 += MAIN_MEM_r[0]

	t7_t2_mem1 = S.Task('t7_t2_mem1', length=1, delay_cost=1)
	S += t7_t2_mem1 >= 6
	t7_t2_mem1 += MAIN_MEM_r[1]

	t0_t0_in = S.Task('t0_t0_in', length=1, delay_cost=1)
	S += t0_t0_in >= 7
	t0_t0_in += MAS_in[3]

	t0_t0_mem0 = S.Task('t0_t0_mem0', length=1, delay_cost=1)
	S += t0_t0_mem0 >= 7
	t0_t0_mem0 += MAIN_MEM_r[0]

	t0_t0_mem1 = S.Task('t0_t0_mem1', length=1, delay_cost=1)
	S += t0_t0_mem1 >= 7
	t0_t0_mem1 += MAIN_MEM_r[1]

	t5_t4 = S.Task('t5_t4', length=4, delay_cost=1)
	S += t5_t4 >= 7
	t5_t4 += MM[0]

	t7_t2 = S.Task('t7_t2', length=2, delay_cost=1)
	S += t7_t2 >= 7
	t7_t2 += MAS[0]

	t0_t0 = S.Task('t0_t0', length=2, delay_cost=1)
	S += t0_t0 >= 8
	t0_t0 += MAS[3]

	t7_t3_in = S.Task('t7_t3_in', length=1, delay_cost=1)
	S += t7_t3_in >= 8
	t7_t3_in += MAS_in[0]

	t7_t3_mem0 = S.Task('t7_t3_mem0', length=1, delay_cost=1)
	S += t7_t3_mem0 >= 8
	t7_t3_mem0 += MAIN_MEM_r[0]

	t7_t3_mem1 = S.Task('t7_t3_mem1', length=1, delay_cost=1)
	S += t7_t3_mem1 >= 8
	t7_t3_mem1 += MAIN_MEM_r[1]

	t3_t0_in = S.Task('t3_t0_in', length=1, delay_cost=1)
	S += t3_t0_in >= 9
	t3_t0_in += MM_in[0]

	t3_t0_mem0 = S.Task('t3_t0_mem0', length=1, delay_cost=1)
	S += t3_t0_mem0 >= 9
	t3_t0_mem0 += MAIN_MEM_r[0]

	t3_t0_mem1 = S.Task('t3_t0_mem1', length=1, delay_cost=1)
	S += t3_t0_mem1 >= 9
	t3_t0_mem1 += MAIN_MEM_r[1]

	t7_t3 = S.Task('t7_t3', length=2, delay_cost=1)
	S += t7_t3 >= 9
	t7_t3 += MAS[0]

	t3_t0 = S.Task('t3_t0', length=4, delay_cost=1)
	S += t3_t0 >= 10
	t3_t0 += MM[0]

	t3_t2_in = S.Task('t3_t2_in', length=1, delay_cost=1)
	S += t3_t2_in >= 10
	t3_t2_in += MAS_in[0]

	t3_t2_mem0 = S.Task('t3_t2_mem0', length=1, delay_cost=1)
	S += t3_t2_mem0 >= 10
	t3_t2_mem0 += MAIN_MEM_r[0]

	t3_t2_mem1 = S.Task('t3_t2_mem1', length=1, delay_cost=1)
	S += t3_t2_mem1 >= 10
	t3_t2_mem1 += MAIN_MEM_r[1]

	t7_t4_in = S.Task('t7_t4_in', length=1, delay_cost=1)
	S += t7_t4_in >= 10
	t7_t4_in += MM_in[0]

	t7_t4_mem0 = S.Task('t7_t4_mem0', length=1, delay_cost=1)
	S += t7_t4_mem0 >= 10
	t7_t4_mem0 += MAS_MEM[0]

	t7_t4_mem1 = S.Task('t7_t4_mem1', length=1, delay_cost=1)
	S += t7_t4_mem1 >= 10
	t7_t4_mem1 += MAS_MEM[1]

	t3_t2 = S.Task('t3_t2', length=2, delay_cost=1)
	S += t3_t2 >= 11
	t3_t2 += MAS[0]

	t4_t0_in = S.Task('t4_t0_in', length=1, delay_cost=1)
	S += t4_t0_in >= 11
	t4_t0_in += MAS_in[0]

	t4_t0_mem0 = S.Task('t4_t0_mem0', length=1, delay_cost=1)
	S += t4_t0_mem0 >= 11
	t4_t0_mem0 += MAIN_MEM_r[0]

	t4_t0_mem1 = S.Task('t4_t0_mem1', length=1, delay_cost=1)
	S += t4_t0_mem1 >= 11
	t4_t0_mem1 += MAIN_MEM_r[1]

	t7_t4 = S.Task('t7_t4', length=4, delay_cost=1)
	S += t7_t4 >= 11
	t7_t4 += MM[0]

	t0_t1_in = S.Task('t0_t1_in', length=1, delay_cost=1)
	S += t0_t1_in >= 12
	t0_t1_in += MAS_in[2]

	t0_t1_mem0 = S.Task('t0_t1_mem0', length=1, delay_cost=1)
	S += t0_t1_mem0 >= 12
	t0_t1_mem0 += MAIN_MEM_r[0]

	t0_t1_mem1 = S.Task('t0_t1_mem1', length=1, delay_cost=1)
	S += t0_t1_mem1 >= 12
	t0_t1_mem1 += MAIN_MEM_r[1]

	t3_t4_in = S.Task('t3_t4_in', length=1, delay_cost=1)
	S += t3_t4_in >= 12
	t3_t4_in += MM_in[0]

	t3_t4_mem0 = S.Task('t3_t4_mem0', length=1, delay_cost=1)
	S += t3_t4_mem0 >= 12
	t3_t4_mem0 += MAS_MEM[0]

	t3_t4_mem1 = S.Task('t3_t4_mem1', length=1, delay_cost=1)
	S += t3_t4_mem1 >= 12
	t3_t4_mem1 += MAS_MEM[1]

	t4_t0 = S.Task('t4_t0', length=2, delay_cost=1)
	S += t4_t0 >= 12
	t4_t0 += MAS[0]

	t0_t1 = S.Task('t0_t1', length=2, delay_cost=1)
	S += t0_t1 >= 13
	t0_t1 += MAS[2]

	t10_in = S.Task('t10_in', length=1, delay_cost=1)
	S += t10_in >= 13
	t10_in += MAS_in[0]

	t10_mem0 = S.Task('t10_mem0', length=1, delay_cost=1)
	S += t10_mem0 >= 13
	t10_mem0 += MAIN_MEM_r[0]

	t10_mem1 = S.Task('t10_mem1', length=1, delay_cost=1)
	S += t10_mem1 >= 13
	t10_mem1 += MAIN_MEM_r[1]

	t3_t4 = S.Task('t3_t4', length=4, delay_cost=1)
	S += t3_t4 >= 13
	t3_t4 += MM[0]

	t4_t2_in = S.Task('t4_t2_in', length=1, delay_cost=1)
	S += t4_t2_in >= 13
	t4_t2_in += MM_in[0]

	t4_t2_mem0 = S.Task('t4_t2_mem0', length=1, delay_cost=1)
	S += t4_t2_mem0 >= 13
	t4_t2_mem0 += MAS_MEM[0]

	t4_t2_mem1 = S.Task('t4_t2_mem1', length=1, delay_cost=1)
	S += t4_t2_mem1 >= 13
	t4_t2_mem1 += MAS_MEM[1]

	t0_t2_in = S.Task('t0_t2_in', length=1, delay_cost=1)
	S += t0_t2_in >= 14
	t0_t2_in += MM_in[0]

	t0_t2_mem0 = S.Task('t0_t2_mem0', length=1, delay_cost=1)
	S += t0_t2_mem0 >= 14
	t0_t2_mem0 += MAS_MEM[6]

	t0_t2_mem1 = S.Task('t0_t2_mem1', length=1, delay_cost=1)
	S += t0_t2_mem1 >= 14
	t0_t2_mem1 += MAS_MEM[5]

	t10 = S.Task('t10', length=2, delay_cost=1)
	S += t10 >= 14
	t10 += MAS[0]

	t11_in = S.Task('t11_in', length=1, delay_cost=1)
	S += t11_in >= 14
	t11_in += MAS_in[0]

	t11_mem0 = S.Task('t11_mem0', length=1, delay_cost=1)
	S += t11_mem0 >= 14
	t11_mem0 += MAIN_MEM_r[0]

	t11_mem1 = S.Task('t11_mem1', length=1, delay_cost=1)
	S += t11_mem1 >= 14
	t11_mem1 += MAIN_MEM_r[1]

	t4_t2 = S.Task('t4_t2', length=4, delay_cost=1)
	S += t4_t2 >= 14
	t4_t2 += MM[0]

	t0_t2 = S.Task('t0_t2', length=4, delay_cost=1)
	S += t0_t2 >= 15
	t0_t2 += MM[0]

	t11 = S.Task('t11', length=2, delay_cost=1)
	S += t11 >= 15
	t11 += MAS[0]

	t6_t2_in = S.Task('t6_t2_in', length=1, delay_cost=1)
	S += t6_t2_in >= 15
	t6_t2_in += MAS_in[2]

	t6_t2_mem0 = S.Task('t6_t2_mem0', length=1, delay_cost=1)
	S += t6_t2_mem0 >= 15
	t6_t2_mem0 += MAIN_MEM_r[0]

	t6_t2_mem1 = S.Task('t6_t2_mem1', length=1, delay_cost=1)
	S += t6_t2_mem1 >= 15
	t6_t2_mem1 += MAIN_MEM_r[1]

	t4_t3_in = S.Task('t4_t3_in', length=1, delay_cost=1)
	S += t4_t3_in >= 16
	t4_t3_in += MM_in[0]

	t4_t3_mem0 = S.Task('t4_t3_mem0', length=1, delay_cost=1)
	S += t4_t3_mem0 >= 16
	t4_t3_mem0 += MAIN_MEM_r[0]

	t4_t3_mem1 = S.Task('t4_t3_mem1', length=1, delay_cost=1)
	S += t4_t3_mem1 >= 16
	t4_t3_mem1 += MAIN_MEM_r[1]

	t6_t2 = S.Task('t6_t2', length=2, delay_cost=1)
	S += t6_t2 >= 16
	t6_t2 += MAS[2]

	t3_t1_in = S.Task('t3_t1_in', length=1, delay_cost=1)
	S += t3_t1_in >= 17
	t3_t1_in += MM_in[0]

	t3_t1_mem0 = S.Task('t3_t1_mem0', length=1, delay_cost=1)
	S += t3_t1_mem0 >= 17
	t3_t1_mem0 += MAIN_MEM_r[0]

	t3_t1_mem1 = S.Task('t3_t1_mem1', length=1, delay_cost=1)
	S += t3_t1_mem1 >= 17
	t3_t1_mem1 += MAIN_MEM_r[1]

	t4_t3 = S.Task('t4_t3', length=4, delay_cost=1)
	S += t4_t3 >= 17
	t4_t3 += MM[0]

	t00_in = S.Task('t00_in', length=1, delay_cost=1)
	S += t00_in >= 18
	t00_in += MAS_in[0]

	t00_mem0 = S.Task('t00_mem0', length=1, delay_cost=1)
	S += t00_mem0 >= 18
	t00_mem0 += MM_MEM[0]

	t00_mem1 = S.Task('t00_mem1', length=1, delay_cost=1)
	S += t00_mem1 >= 18
	t00_mem1 += MAS_MEM[5]

	t3_t1 = S.Task('t3_t1', length=4, delay_cost=1)
	S += t3_t1 >= 18
	t3_t1 += MM[0]

	t7_t1_in = S.Task('t7_t1_in', length=1, delay_cost=1)
	S += t7_t1_in >= 18
	t7_t1_in += MM_in[0]

	t7_t1_mem0 = S.Task('t7_t1_mem0', length=1, delay_cost=1)
	S += t7_t1_mem0 >= 18
	t7_t1_mem0 += MAIN_MEM_r[0]

	t7_t1_mem1 = S.Task('t7_t1_mem1', length=1, delay_cost=1)
	S += t7_t1_mem1 >= 18
	t7_t1_mem1 += MAIN_MEM_r[1]

	t00 = S.Task('t00', length=2, delay_cost=1)
	S += t00 >= 19
	t00 += MAS[0]

	t7_t0_in = S.Task('t7_t0_in', length=1, delay_cost=1)
	S += t7_t0_in >= 19
	t7_t0_in += MM_in[0]

	t7_t0_mem0 = S.Task('t7_t0_mem0', length=1, delay_cost=1)
	S += t7_t0_mem0 >= 19
	t7_t0_mem0 += MAIN_MEM_r[0]

	t7_t0_mem1 = S.Task('t7_t0_mem1', length=1, delay_cost=1)
	S += t7_t0_mem1 >= 19
	t7_t0_mem1 += MAIN_MEM_r[1]

	t7_t1 = S.Task('t7_t1', length=4, delay_cost=1)
	S += t7_t1 >= 19
	t7_t1 += MM[0]

	t41_in = S.Task('t41_in', length=1, delay_cost=1)
	S += t41_in >= 20
	t41_in += MAS_in[0]

	t41_mem0 = S.Task('t41_mem0', length=1, delay_cost=1)
	S += t41_mem0 >= 20
	t41_mem0 += MM_MEM[0]

	t41_mem1 = S.Task('t41_mem1', length=1, delay_cost=1)
	S += t41_mem1 >= 20
	t41_mem1 += MM_MEM[1]

	t6_t1_in = S.Task('t6_t1_in', length=1, delay_cost=1)
	S += t6_t1_in >= 20
	t6_t1_in += MM_in[0]

	t6_t1_mem0 = S.Task('t6_t1_mem0', length=1, delay_cost=1)
	S += t6_t1_mem0 >= 20
	t6_t1_mem0 += MAIN_MEM_r[0]

	t6_t1_mem1 = S.Task('t6_t1_mem1', length=1, delay_cost=1)
	S += t6_t1_mem1 >= 20
	t6_t1_mem1 += MAIN_MEM_r[1]

	t7_t0 = S.Task('t7_t0', length=4, delay_cost=1)
	S += t7_t0 >= 20
	t7_t0 += MM[0]

	t30_in = S.Task('t30_in', length=1, delay_cost=1)
	S += t30_in >= 21
	t30_in += MAS_in[1]

	t30_mem0 = S.Task('t30_mem0', length=1, delay_cost=1)
	S += t30_mem0 >= 21
	t30_mem0 += MM_MEM[0]

	t30_mem1 = S.Task('t30_mem1', length=1, delay_cost=1)
	S += t30_mem1 >= 21
	t30_mem1 += MM_MEM[1]

	t41 = S.Task('t41', length=2, delay_cost=1)
	S += t41 >= 21
	t41 += MAS[0]

	t6_t0_in = S.Task('t6_t0_in', length=1, delay_cost=1)
	S += t6_t0_in >= 21
	t6_t0_in += MM_in[0]

	t6_t0_mem0 = S.Task('t6_t0_mem0', length=1, delay_cost=1)
	S += t6_t0_mem0 >= 21
	t6_t0_mem0 += MAIN_MEM_r[0]

	t6_t0_mem1 = S.Task('t6_t0_mem1', length=1, delay_cost=1)
	S += t6_t0_mem1 >= 21
	t6_t0_mem1 += MAIN_MEM_r[1]

	t6_t1 = S.Task('t6_t1', length=4, delay_cost=1)
	S += t6_t1 >= 21
	t6_t1 += MM[0]

	t151_in = S.Task('t151_in', length=1, delay_cost=1)
	S += t151_in >= 22
	t151_in += MAS_in[3]

	t151_mem0 = S.Task('t151_mem0', length=1, delay_cost=1)
	S += t151_mem0 >= 22
	t151_mem0 += MAS_MEM[6]

	t151_mem1 = S.Task('t151_mem1', length=1, delay_cost=1)
	S += t151_mem1 >= 22
	t151_mem1 += MAS_MEM[1]

	t30 = S.Task('t30', length=2, delay_cost=1)
	S += t30 >= 22
	t30 += MAS[1]

	t3_t5_in = S.Task('t3_t5_in', length=1, delay_cost=1)
	S += t3_t5_in >= 22
	t3_t5_in += MAS_in[2]

	t3_t5_mem0 = S.Task('t3_t5_mem0', length=1, delay_cost=1)
	S += t3_t5_mem0 >= 22
	t3_t5_mem0 += MM_MEM[0]

	t3_t5_mem1 = S.Task('t3_t5_mem1', length=1, delay_cost=1)
	S += t3_t5_mem1 >= 22
	t3_t5_mem1 += MM_MEM[1]

	t5_t1_in = S.Task('t5_t1_in', length=1, delay_cost=1)
	S += t5_t1_in >= 22
	t5_t1_in += MM_in[0]

	t5_t1_mem0 = S.Task('t5_t1_mem0', length=1, delay_cost=1)
	S += t5_t1_mem0 >= 22
	t5_t1_mem0 += MAIN_MEM_r[0]

	t5_t1_mem1 = S.Task('t5_t1_mem1', length=1, delay_cost=1)
	S += t5_t1_mem1 >= 22
	t5_t1_mem1 += MAIN_MEM_r[1]

	t6_t0 = S.Task('t6_t0', length=4, delay_cost=1)
	S += t6_t0 >= 22
	t6_t0 += MM[0]

	t110_in = S.Task('t110_in', length=1, delay_cost=1)
	S += t110_in >= 23
	t110_in += MAS_in[1]

	t110_mem0 = S.Task('t110_mem0', length=1, delay_cost=1)
	S += t110_mem0 >= 23
	t110_mem0 += MAS_MEM[2]

	t110_mem1 = S.Task('t110_mem1', length=1, delay_cost=1)
	S += t110_mem1 >= 23
	t110_mem1 += MAS_MEM[3]

	t151 = S.Task('t151', length=2, delay_cost=1)
	S += t151 >= 23
	t151 += MAS[3]

	t3_t5 = S.Task('t3_t5', length=2, delay_cost=1)
	S += t3_t5 >= 23
	t3_t5 += MAS[2]

	t5_t0_in = S.Task('t5_t0_in', length=1, delay_cost=1)
	S += t5_t0_in >= 23
	t5_t0_in += MM_in[0]

	t5_t0_mem0 = S.Task('t5_t0_mem0', length=1, delay_cost=1)
	S += t5_t0_mem0 >= 23
	t5_t0_mem0 += MAIN_MEM_r[0]

	t5_t0_mem1 = S.Task('t5_t0_mem1', length=1, delay_cost=1)
	S += t5_t0_mem1 >= 23
	t5_t0_mem1 += MAIN_MEM_r[1]

	t5_t1 = S.Task('t5_t1', length=4, delay_cost=1)
	S += t5_t1 >= 23
	t5_t1 += MM[0]

	t70_in = S.Task('t70_in', length=1, delay_cost=1)
	S += t70_in >= 23
	t70_in += MAS_in[3]

	t70_mem0 = S.Task('t70_mem0', length=1, delay_cost=1)
	S += t70_mem0 >= 23
	t70_mem0 += MM_MEM[0]

	t70_mem1 = S.Task('t70_mem1', length=1, delay_cost=1)
	S += t70_mem1 >= 23
	t70_mem1 += MM_MEM[1]

	t110 = S.Task('t110', length=2, delay_cost=1)
	S += t110 >= 24
	t110 += MAS[1]

	t20_in = S.Task('t20_in', length=1, delay_cost=1)
	S += t20_in >= 24
	t20_in += MAS_in[1]

	t20_mem0 = S.Task('t20_mem0', length=1, delay_cost=1)
	S += t20_mem0 >= 24
	t20_mem0 += MAS_MEM[0]

	t20_mem1 = S.Task('t20_mem1', length=1, delay_cost=1)
	S += t20_mem1 >= 24
	t20_mem1 += MAIN_MEM_r[1]

	t5_t0 = S.Task('t5_t0', length=4, delay_cost=1)
	S += t5_t0 >= 24
	t5_t0 += MM[0]

	t6_t4_in = S.Task('t6_t4_in', length=1, delay_cost=1)
	S += t6_t4_in >= 24
	t6_t4_in += MM_in[0]

	t6_t4_mem0 = S.Task('t6_t4_mem0', length=1, delay_cost=1)
	S += t6_t4_mem0 >= 24
	t6_t4_mem0 += MAS_MEM[4]

	t6_t4_mem1 = S.Task('t6_t4_mem1', length=1, delay_cost=1)
	S += t6_t4_mem1 >= 24
	t6_t4_mem1 += MAS_MEM[1]

	t70 = S.Task('t70', length=2, delay_cost=1)
	S += t70 >= 24
	t70 += MAS[3]

	t7_t5_in = S.Task('t7_t5_in', length=1, delay_cost=1)
	S += t7_t5_in >= 24
	t7_t5_in += MAS_in[3]

	t7_t5_mem0 = S.Task('t7_t5_mem0', length=1, delay_cost=1)
	S += t7_t5_mem0 >= 24
	t7_t5_mem0 += MM_MEM[0]

	t7_t5_mem1 = S.Task('t7_t5_mem1', length=1, delay_cost=1)
	S += t7_t5_mem1 >= 24
	t7_t5_mem1 += MM_MEM[1]

	t20 = S.Task('t20', length=2, delay_cost=1)
	S += t20 >= 25
	t20 += MAS[1]

	t21_in = S.Task('t21_in', length=1, delay_cost=1)
	S += t21_in >= 25
	t21_in += MAS_in[1]

	t21_mem0 = S.Task('t21_mem0', length=1, delay_cost=1)
	S += t21_mem0 >= 25
	t21_mem0 += MAS_MEM[0]

	t21_mem1 = S.Task('t21_mem1', length=1, delay_cost=1)
	S += t21_mem1 >= 25
	t21_mem1 += MAIN_MEM_r[1]

	t260_in = S.Task('t260_in', length=1, delay_cost=1)
	S += t260_in >= 25
	t260_in += MAS_in[0]

	t260_mem0 = S.Task('t260_mem0', length=1, delay_cost=1)
	S += t260_mem0 >= 25
	t260_mem0 += MAS_MEM[6]

	t260_mem1 = S.Task('t260_mem1', length=1, delay_cost=1)
	S += t260_mem1 >= 25
	t260_mem1 += MAS_MEM[7]

	t60_in = S.Task('t60_in', length=1, delay_cost=1)
	S += t60_in >= 25
	t60_in += MAS_in[2]

	t60_mem0 = S.Task('t60_mem0', length=1, delay_cost=1)
	S += t60_mem0 >= 25
	t60_mem0 += MM_MEM[0]

	t60_mem1 = S.Task('t60_mem1', length=1, delay_cost=1)
	S += t60_mem1 >= 25
	t60_mem1 += MM_MEM[1]

	t6_t4 = S.Task('t6_t4', length=4, delay_cost=1)
	S += t6_t4 >= 25
	t6_t4 += MM[0]

	t7_t5 = S.Task('t7_t5', length=2, delay_cost=1)
	S += t7_t5 >= 25
	t7_t5 += MAS[3]

	t21 = S.Task('t21', length=2, delay_cost=1)
	S += t21 >= 26
	t21 += MAS[1]

	t260 = S.Task('t260', length=2, delay_cost=1)
	S += t260 >= 26
	t260 += MAS[0]

	t60 = S.Task('t60', length=2, delay_cost=1)
	S += t60 >= 26
	t60 += MAS[2]

	t6_t5_in = S.Task('t6_t5_in', length=1, delay_cost=1)
	S += t6_t5_in >= 26
	t6_t5_in += MAS_in[2]

	t6_t5_mem0 = S.Task('t6_t5_mem0', length=1, delay_cost=1)
	S += t6_t5_mem0 >= 26
	t6_t5_mem0 += MM_MEM[0]

	t6_t5_mem1 = S.Task('t6_t5_mem1', length=1, delay_cost=1)
	S += t6_t5_mem1 >= 26
	t6_t5_mem1 += MM_MEM[1]

	t80_in = S.Task('t80_in', length=1, delay_cost=1)
	S += t80_in >= 26
	t80_in += MAS_in[0]

	t80_mem0 = S.Task('t80_mem0', length=1, delay_cost=1)
	S += t80_mem0 >= 26
	t80_mem0 += MAS_MEM[0]

	t80_mem1 = S.Task('t80_mem1', length=1, delay_cost=1)
	S += t80_mem1 >= 26
	t80_mem1 += MAIN_MEM_r[1]

	t10_t0_in = S.Task('t10_t0_in', length=1, delay_cost=1)
	S += t10_t0_in >= 27
	t10_t0_in += MAS_in[1]

	t10_t0_mem0 = S.Task('t10_t0_mem0', length=1, delay_cost=1)
	S += t10_t0_mem0 >= 27
	t10_t0_mem0 += MAS_MEM[2]

	t10_t0_mem1 = S.Task('t10_t0_mem1', length=1, delay_cost=1)
	S += t10_t0_mem1 >= 27
	t10_t0_mem1 += MAS_MEM[3]

	t220_in = S.Task('t220_in', length=1, delay_cost=1)
	S += t220_in >= 27
	t220_in += MAS_in[3]

	t220_mem0 = S.Task('t220_mem0', length=1, delay_cost=1)
	S += t220_mem0 >= 27
	t220_mem0 += MAS_MEM[4]

	t220_mem1 = S.Task('t220_mem1', length=1, delay_cost=1)
	S += t220_mem1 >= 27
	t220_mem1 += MAS_MEM[5]

	t50_in = S.Task('t50_in', length=1, delay_cost=1)
	S += t50_in >= 27
	t50_in += MAS_in[2]

	t50_mem0 = S.Task('t50_mem0', length=1, delay_cost=1)
	S += t50_mem0 >= 27
	t50_mem0 += MM_MEM[0]

	t50_mem1 = S.Task('t50_mem1', length=1, delay_cost=1)
	S += t50_mem1 >= 27
	t50_mem1 += MM_MEM[1]

	t6_t5 = S.Task('t6_t5', length=2, delay_cost=1)
	S += t6_t5 >= 27
	t6_t5 += MAS[2]

	t80 = S.Task('t80', length=2, delay_cost=1)
	S += t80 >= 27
	t80 += MAS[0]

	t81_in = S.Task('t81_in', length=1, delay_cost=1)
	S += t81_in >= 27
	t81_in += MAS_in[0]

	t81_mem0 = S.Task('t81_mem0', length=1, delay_cost=1)
	S += t81_mem0 >= 27
	t81_mem0 += MAS_MEM[0]

	t81_mem1 = S.Task('t81_mem1', length=1, delay_cost=1)
	S += t81_mem1 >= 27
	t81_mem1 += MAIN_MEM_r[1]

	t10_t0 = S.Task('t10_t0', length=2, delay_cost=1)
	S += t10_t0 >= 28
	t10_t0 += MAS[1]

	t10_t1_in = S.Task('t10_t1_in', length=1, delay_cost=1)
	S += t10_t1_in >= 28
	t10_t1_in += MAS_in[0]

	t10_t1_mem0 = S.Task('t10_t1_mem0', length=1, delay_cost=1)
	S += t10_t1_mem0 >= 28
	t10_t1_mem0 += MAS_MEM[2]

	t10_t1_mem1 = S.Task('t10_t1_mem1', length=1, delay_cost=1)
	S += t10_t1_mem1 >= 28
	t10_t1_mem1 += MAS_MEM[3]

	t220 = S.Task('t220', length=2, delay_cost=1)
	S += t220 >= 28
	t220 += MAS[3]

	t50 = S.Task('t50', length=2, delay_cost=1)
	S += t50 >= 28
	t50 += MAS[2]

	t5_t5_in = S.Task('t5_t5_in', length=1, delay_cost=1)
	S += t5_t5_in >= 28
	t5_t5_in += MAS_in[2]

	t5_t5_mem0 = S.Task('t5_t5_mem0', length=1, delay_cost=1)
	S += t5_t5_mem0 >= 28
	t5_t5_mem0 += MM_MEM[0]

	t5_t5_mem1 = S.Task('t5_t5_mem1', length=1, delay_cost=1)
	S += t5_t5_mem1 >= 28
	t5_t5_mem1 += MM_MEM[1]

	t81 = S.Task('t81', length=2, delay_cost=1)
	S += t81 >= 28
	t81 += MAS[0]

	t10_t1 = S.Task('t10_t1', length=2, delay_cost=1)
	S += t10_t1 >= 29
	t10_t1 += MAS[0]

	t10_t3_in = S.Task('t10_t3_in', length=1, delay_cost=1)
	S += t10_t3_in >= 29
	t10_t3_in += MM_in[0]

	t10_t3_mem0 = S.Task('t10_t3_mem0', length=1, delay_cost=1)
	S += t10_t3_mem0 >= 29
	t10_t3_mem0 += MAS_MEM[2]

	t10_t3_mem1 = S.Task('t10_t3_mem1', length=1, delay_cost=1)
	S += t10_t3_mem1 >= 29
	t10_t3_mem1 += MAS_MEM[3]

	t290_in = S.Task('t290_in', length=1, delay_cost=1)
	S += t290_in >= 29
	t290_in += MAS_in[3]

	t290_mem0 = S.Task('t290_mem0', length=1, delay_cost=1)
	S += t290_mem0 >= 29
	t290_mem0 += MAS_MEM[4]

	t290_mem1 = S.Task('t290_mem1', length=1, delay_cost=1)
	S += t290_mem1 >= 29
	t290_mem1 += MAS_MEM[5]

	t4_t5_in = S.Task('t4_t5_in', length=1, delay_cost=1)
	S += t4_t5_in >= 29
	t4_t5_in += MAS_in[2]

	t4_t5_mem0 = S.Task('t4_t5_mem0', length=1, delay_cost=1)
	S += t4_t5_mem0 >= 29
	t4_t5_mem0 += MM_MEM[0]

	t4_t5_mem1 = S.Task('t4_t5_mem1', length=1, delay_cost=1)
	S += t4_t5_mem1 >= 29
	t4_t5_mem1 += MM_MEM[1]

	t5_t5 = S.Task('t5_t5', length=2, delay_cost=1)
	S += t5_t5 >= 29
	t5_t5 += MAS[2]

	t9_t0_in = S.Task('t9_t0_in', length=1, delay_cost=1)
	S += t9_t0_in >= 29
	t9_t0_in += MAS_in[1]

	t9_t0_mem0 = S.Task('t9_t0_mem0', length=1, delay_cost=1)
	S += t9_t0_mem0 >= 29
	t9_t0_mem0 += MAS_MEM[0]

	t9_t0_mem1 = S.Task('t9_t0_mem1', length=1, delay_cost=1)
	S += t9_t0_mem1 >= 29
	t9_t0_mem1 += MAS_MEM[1]

	t10_t3 = S.Task('t10_t3', length=4, delay_cost=1)
	S += t10_t3 >= 30
	t10_t3 += MM[0]

	t290 = S.Task('t290', length=2, delay_cost=1)
	S += t290 >= 30
	t290 += MAS[3]

	t31_in = S.Task('t31_in', length=1, delay_cost=1)
	S += t31_in >= 30
	t31_in += MAS_in[2]

	t31_mem0 = S.Task('t31_mem0', length=1, delay_cost=1)
	S += t31_mem0 >= 30
	t31_mem0 += MM_MEM[0]

	t31_mem1 = S.Task('t31_mem1', length=1, delay_cost=1)
	S += t31_mem1 >= 30
	t31_mem1 += MAS_MEM[5]

	t4_t5 = S.Task('t4_t5', length=2, delay_cost=1)
	S += t4_t5 >= 30
	t4_t5 += MAS[2]

	t9_t0 = S.Task('t9_t0', length=2, delay_cost=1)
	S += t9_t0 >= 30
	t9_t0 += MAS[1]

	t9_t3_in = S.Task('t9_t3_in', length=1, delay_cost=1)
	S += t9_t3_in >= 30
	t9_t3_in += MM_in[0]

	t9_t3_mem0 = S.Task('t9_t3_mem0', length=1, delay_cost=1)
	S += t9_t3_mem0 >= 30
	t9_t3_mem0 += MAS_MEM[0]

	t9_t3_mem1 = S.Task('t9_t3_mem1', length=1, delay_cost=1)
	S += t9_t3_mem1 >= 30
	t9_t3_mem1 += MAS_MEM[1]

	t31 = S.Task('t31', length=2, delay_cost=1)
	S += t31 >= 31
	t31 += MAS[2]

	t61_in = S.Task('t61_in', length=1, delay_cost=1)
	S += t61_in >= 31
	t61_in += MAS_in[2]

	t61_mem0 = S.Task('t61_mem0', length=1, delay_cost=1)
	S += t61_mem0 >= 31
	t61_mem0 += MM_MEM[0]

	t61_mem1 = S.Task('t61_mem1', length=1, delay_cost=1)
	S += t61_mem1 >= 31
	t61_mem1 += MAS_MEM[5]

	t9_t1_in = S.Task('t9_t1_in', length=1, delay_cost=1)
	S += t9_t1_in >= 31
	t9_t1_in += MAS_in[0]

	t9_t1_mem0 = S.Task('t9_t1_mem0', length=1, delay_cost=1)
	S += t9_t1_mem0 >= 31
	t9_t1_mem0 += MAS_MEM[0]

	t9_t1_mem1 = S.Task('t9_t1_mem1', length=1, delay_cost=1)
	S += t9_t1_mem1 >= 31
	t9_t1_mem1 += MAS_MEM[1]

	t9_t3 = S.Task('t9_t3', length=4, delay_cost=1)
	S += t9_t3 >= 31
	t9_t3 += MM[0]

	t51_in = S.Task('t51_in', length=1, delay_cost=1)
	S += t51_in >= 32
	t51_in += MAS_in[1]

	t51_mem0 = S.Task('t51_mem0', length=1, delay_cost=1)
	S += t51_mem0 >= 32
	t51_mem0 += MM_MEM[0]

	t51_mem1 = S.Task('t51_mem1', length=1, delay_cost=1)
	S += t51_mem1 >= 32
	t51_mem1 += MAS_MEM[5]

	t61 = S.Task('t61', length=2, delay_cost=1)
	S += t61 >= 32
	t61 += MAS[2]

	t9_t1 = S.Task('t9_t1', length=2, delay_cost=1)
	S += t9_t1 >= 32
	t9_t1 += MAS[0]

	t40_in = S.Task('t40_in', length=1, delay_cost=1)
	S += t40_in >= 33
	t40_in += MAS_in[1]

	t40_mem0 = S.Task('t40_mem0', length=1, delay_cost=1)
	S += t40_mem0 >= 33
	t40_mem0 += MM_MEM[0]

	t40_mem1 = S.Task('t40_mem1', length=1, delay_cost=1)
	S += t40_mem1 >= 33
	t40_mem1 += MAS_MEM[5]

	t51 = S.Task('t51', length=2, delay_cost=1)
	S += t51 >= 33
	t51 += MAS[1]

	t40 = S.Task('t40', length=2, delay_cost=1)
	S += t40 >= 34
	t40 += MAS[1]

	t71_in = S.Task('t71_in', length=1, delay_cost=1)
	S += t71_in >= 34
	t71_in += MAS_in[3]

	t71_mem0 = S.Task('t71_mem0', length=1, delay_cost=1)
	S += t71_mem0 >= 34
	t71_mem0 += MM_MEM[0]

	t71_mem1 = S.Task('t71_mem1', length=1, delay_cost=1)
	S += t71_mem1 >= 34
	t71_mem1 += MAS_MEM[7]

	t71 = S.Task('t71', length=2, delay_cost=1)
	S += t71 >= 35
	t71 += MAS[3]


	# new tasks
	t9_t2 = S.Task('t9_t2', length=4, delay_cost=1)
	t9_t2 += alt(MM)
	t9_t2_in = S.Task('t9_t2_in', length=1, delay_cost=1)
	t9_t2_in += alt(MM_in)
	S += t9_t2_in*MM_in[0]<=t9_t2*MM[0]
	t9_t2_mem0 = S.Task('t9_t2_mem0', length=1, delay_cost=1)
	t9_t2_mem0 += MAS_MEM[2]
	S += 31 < t9_t2_mem0
	S += t9_t2_mem0 <= t9_t2

	t9_t2_mem1 = S.Task('t9_t2_mem1', length=1, delay_cost=1)
	t9_t2_mem1 += MAS_MEM[1]
	S += 33 < t9_t2_mem1
	S += t9_t2_mem1 <= t9_t2

	t9_t5 = S.Task('t9_t5', length=2, delay_cost=1)
	t9_t5 += alt(MAS)
	t9_t5_in = S.Task('t9_t5_in', length=1, delay_cost=1)
	t9_t5_in += alt(MAS_in)
	S += t9_t5_in*MAS_in[0]<=t9_t5*MAS[0]

	S += t9_t5_in*MAS_in[1]<=t9_t5*MAS[1]

	S += t9_t5_in*MAS_in[2]<=t9_t5*MAS[2]

	S += t9_t5_in*MAS_in[3]<=t9_t5*MAS[3]

	t9_t5_mem0 = S.Task('t9_t5_mem0', length=1, delay_cost=1)
	t9_t5_mem0 += MM_MEM[0]
	S += 34 < t9_t5_mem0
	S += t9_t5_mem0 <= t9_t5

	t9_t5_mem1 = S.Task('t9_t5_mem1', length=1, delay_cost=1)
	t9_t5_mem1 += MM_MEM[1]
	S += 34 < t9_t5_mem1
	S += t9_t5_mem1 <= t9_t5

	t91 = S.Task('t91', length=2, delay_cost=1)
	t91 += alt(MAS)
	t91_in = S.Task('t91_in', length=1, delay_cost=1)
	t91_in += alt(MAS_in)
	S += t91_in*MAS_in[0]<=t91*MAS[0]

	S += t91_in*MAS_in[1]<=t91*MAS[1]

	S += t91_in*MAS_in[2]<=t91*MAS[2]

	S += t91_in*MAS_in[3]<=t91*MAS[3]

	t91_mem0 = S.Task('t91_mem0', length=1, delay_cost=1)
	t91_mem0 += MM_MEM[0]
	S += 34 < t91_mem0
	S += t91_mem0 <= t91

	t91_mem1 = S.Task('t91_mem1', length=1, delay_cost=1)
	t91_mem1 += MM_MEM[1]
	S += 34 < t91_mem1
	S += t91_mem1 <= t91

	t10_t2 = S.Task('t10_t2', length=4, delay_cost=1)
	t10_t2 += alt(MM)
	t10_t2_in = S.Task('t10_t2_in', length=1, delay_cost=1)
	t10_t2_in += alt(MM_in)
	S += t10_t2_in*MM_in[0]<=t10_t2*MM[0]
	t10_t2_mem0 = S.Task('t10_t2_mem0', length=1, delay_cost=1)
	t10_t2_mem0 += MAS_MEM[2]
	S += 29 < t10_t2_mem0
	S += t10_t2_mem0 <= t10_t2

	t10_t2_mem1 = S.Task('t10_t2_mem1', length=1, delay_cost=1)
	t10_t2_mem1 += MAS_MEM[1]
	S += 30 < t10_t2_mem1
	S += t10_t2_mem1 <= t10_t2

	t10_t5 = S.Task('t10_t5', length=2, delay_cost=1)
	t10_t5 += alt(MAS)
	t10_t5_in = S.Task('t10_t5_in', length=1, delay_cost=1)
	t10_t5_in += alt(MAS_in)
	S += t10_t5_in*MAS_in[0]<=t10_t5*MAS[0]

	S += t10_t5_in*MAS_in[1]<=t10_t5*MAS[1]

	S += t10_t5_in*MAS_in[2]<=t10_t5*MAS[2]

	S += t10_t5_in*MAS_in[3]<=t10_t5*MAS[3]

	t10_t5_mem0 = S.Task('t10_t5_mem0', length=1, delay_cost=1)
	t10_t5_mem0 += MM_MEM[0]
	S += 33 < t10_t5_mem0
	S += t10_t5_mem0 <= t10_t5

	t10_t5_mem1 = S.Task('t10_t5_mem1', length=1, delay_cost=1)
	t10_t5_mem1 += MM_MEM[1]
	S += 33 < t10_t5_mem1
	S += t10_t5_mem1 <= t10_t5

	t101 = S.Task('t101', length=2, delay_cost=1)
	t101 += alt(MAS)
	t101_in = S.Task('t101_in', length=1, delay_cost=1)
	t101_in += alt(MAS_in)
	S += t101_in*MAS_in[0]<=t101*MAS[0]

	S += t101_in*MAS_in[1]<=t101*MAS[1]

	S += t101_in*MAS_in[2]<=t101*MAS[2]

	S += t101_in*MAS_in[3]<=t101*MAS[3]

	t101_mem0 = S.Task('t101_mem0', length=1, delay_cost=1)
	t101_mem0 += MM_MEM[0]
	S += 33 < t101_mem0
	S += t101_mem0 <= t101

	t101_mem1 = S.Task('t101_mem1', length=1, delay_cost=1)
	t101_mem1 += MM_MEM[1]
	S += 33 < t101_mem1
	S += t101_mem1 <= t101

	t111 = S.Task('t111', length=2, delay_cost=1)
	t111 += alt(MAS)
	t111_in = S.Task('t111_in', length=1, delay_cost=1)
	t111_in += alt(MAS_in)
	S += t111_in*MAS_in[0]<=t111*MAS[0]

	S += t111_in*MAS_in[1]<=t111*MAS[1]

	S += t111_in*MAS_in[2]<=t111*MAS[2]

	S += t111_in*MAS_in[3]<=t111*MAS[3]

	t111_mem0 = S.Task('t111_mem0', length=1, delay_cost=1)
	t111_mem0 += MAS_MEM[4]
	S += 32 < t111_mem0
	S += t111_mem0 <= t111

	t111_mem1 = S.Task('t111_mem1', length=1, delay_cost=1)
	t111_mem1 += MAS_MEM[5]
	S += 32 < t111_mem1
	S += t111_mem1 <= t111

	t291 = S.Task('t291', length=2, delay_cost=1)
	t291 += alt(MAS)
	t291_in = S.Task('t291_in', length=1, delay_cost=1)
	t291_in += alt(MAS_in)
	S += t291_in*MAS_in[0]<=t291*MAS[0]

	S += t291_in*MAS_in[1]<=t291*MAS[1]

	S += t291_in*MAS_in[2]<=t291*MAS[2]

	S += t291_in*MAS_in[3]<=t291*MAS[3]

	t291_mem0 = S.Task('t291_mem0', length=1, delay_cost=1)
	t291_mem0 += MAS_MEM[2]
	S += 34 < t291_mem0
	S += t291_mem0 <= t291

	t291_mem1 = S.Task('t291_mem1', length=1, delay_cost=1)
	t291_mem1 += MAS_MEM[3]
	S += 34 < t291_mem1
	S += t291_mem1 <= t291

	t300 = S.Task('t300', length=2, delay_cost=1)
	t300 += alt(MAS)
	t300_in = S.Task('t300_in', length=1, delay_cost=1)
	t300_in += alt(MAS_in)
	S += t300_in*MAS_in[0]<=t300*MAS[0]

	S += t300_in*MAS_in[1]<=t300*MAS[1]

	S += t300_in*MAS_in[2]<=t300*MAS[2]

	S += t300_in*MAS_in[3]<=t300*MAS[3]

	t300_mem0 = S.Task('t300_mem0', length=1, delay_cost=1)
	t300_mem0 += MAS_MEM[6]
	S += 31 < t300_mem0
	S += t300_mem0 <= t300

	t300_mem1 = S.Task('t300_mem1', length=1, delay_cost=1)
	t300_mem1 += MAS_MEM[5]
	S += 29 < t300_mem1
	S += t300_mem1 <= t300

	t150 = S.Task('t150', length=2, delay_cost=1)
	t150 += alt(MAS)
	t150_in = S.Task('t150_in', length=1, delay_cost=1)
	t150_in += alt(MAS_in)
	S += t150_in*MAS_in[0]<=t150*MAS[0]

	S += t150_in*MAS_in[1]<=t150*MAS[1]

	S += t150_in*MAS_in[2]<=t150*MAS[2]

	S += t150_in*MAS_in[3]<=t150*MAS[3]

	t150_mem0 = S.Task('t150_mem0', length=1, delay_cost=1)
	t150_mem0 += MAS_MEM[0]
	S += 20 < t150_mem0
	S += t150_mem0 <= t150

	t150_mem1 = S.Task('t150_mem1', length=1, delay_cost=1)
	t150_mem1 += MAS_MEM[3]
	S += 35 < t150_mem1
	S += t150_mem1 <= t150

	t161 = S.Task('t161', length=2, delay_cost=1)
	t161 += alt(MAS)
	t161_in = S.Task('t161_in', length=1, delay_cost=1)
	t161_in += alt(MAS_in)
	S += t161_in*MAS_in[0]<=t161*MAS[0]

	S += t161_in*MAS_in[1]<=t161*MAS[1]

	S += t161_in*MAS_in[2]<=t161*MAS[2]

	S += t161_in*MAS_in[3]<=t161*MAS[3]

	t161_mem0 = S.Task('t161_mem0', length=1, delay_cost=1)
	t161_mem0 += MAS_MEM[6]
	S += 24 < t161_mem0
	S += t161_mem0 <= t161

	t161_mem1 = S.Task('t161_mem1', length=1, delay_cost=1)
	t161_mem1 += MAS_MEM[7]
	S += 24 < t161_mem1
	S += t161_mem1 <= t161

	t180 = S.Task('t180', length=2, delay_cost=1)
	t180 += alt(MAS)
	t180_in = S.Task('t180_in', length=1, delay_cost=1)
	t180_in += alt(MAS_in)
	S += t180_in*MAS_in[0]<=t180*MAS[0]

	S += t180_in*MAS_in[1]<=t180*MAS[1]

	S += t180_in*MAS_in[2]<=t180*MAS[2]

	S += t180_in*MAS_in[3]<=t180*MAS[3]

	t180_mem0 = S.Task('t180_mem0', length=1, delay_cost=1)
	t180_mem0 += MAS_MEM[2]
	S += 35 < t180_mem0
	S += t180_mem0 <= t180

	t180_mem1 = S.Task('t180_mem1', length=1, delay_cost=1)
	t180_mem1 += MAS_MEM[1]
	S += 22 < t180_mem1
	S += t180_mem1 <= t180

	t181 = S.Task('t181', length=2, delay_cost=1)
	t181 += alt(MAS)
	t181_in = S.Task('t181_in', length=1, delay_cost=1)
	t181_in += alt(MAS_in)
	S += t181_in*MAS_in[0]<=t181*MAS[0]

	S += t181_in*MAS_in[1]<=t181*MAS[1]

	S += t181_in*MAS_in[2]<=t181*MAS[2]

	S += t181_in*MAS_in[3]<=t181*MAS[3]

	t181_mem0 = S.Task('t181_mem0', length=1, delay_cost=1)
	t181_mem0 += MAS_MEM[0]
	S += 22 < t181_mem0
	S += t181_mem0 <= t181

	t181_mem1 = S.Task('t181_mem1', length=1, delay_cost=1)
	t181_mem1 += MAS_MEM[3]
	S += 35 < t181_mem1
	S += t181_mem1 <= t181

	t221 = S.Task('t221', length=2, delay_cost=1)
	t221 += alt(MAS)
	t221_in = S.Task('t221_in', length=1, delay_cost=1)
	t221_in += alt(MAS_in)
	S += t221_in*MAS_in[0]<=t221*MAS[0]

	S += t221_in*MAS_in[1]<=t221*MAS[1]

	S += t221_in*MAS_in[2]<=t221*MAS[2]

	S += t221_in*MAS_in[3]<=t221*MAS[3]

	t221_mem0 = S.Task('t221_mem0', length=1, delay_cost=1)
	t221_mem0 += MAS_MEM[4]
	S += 33 < t221_mem0
	S += t221_mem0 <= t221

	t221_mem1 = S.Task('t221_mem1', length=1, delay_cost=1)
	t221_mem1 += MAS_MEM[5]
	S += 33 < t221_mem1
	S += t221_mem1 <= t221

	t230 = S.Task('t230', length=2, delay_cost=1)
	t230 += alt(MAS)
	t230_in = S.Task('t230_in', length=1, delay_cost=1)
	t230_in += alt(MAS_in)
	S += t230_in*MAS_in[0]<=t230*MAS[0]

	S += t230_in*MAS_in[1]<=t230*MAS[1]

	S += t230_in*MAS_in[2]<=t230*MAS[2]

	S += t230_in*MAS_in[3]<=t230*MAS[3]

	t230_mem0 = S.Task('t230_mem0', length=1, delay_cost=1)
	t230_mem0 += MAS_MEM[6]
	S += 29 < t230_mem0
	S += t230_mem0 <= t230

	t230_mem1 = S.Task('t230_mem1', length=1, delay_cost=1)
	t230_mem1 += MAS_MEM[5]
	S += 27 < t230_mem1
	S += t230_mem1 <= t230

	t261 = S.Task('t261', length=2, delay_cost=1)
	t261 += alt(MAS)
	t261_in = S.Task('t261_in', length=1, delay_cost=1)
	t261_in += alt(MAS_in)
	S += t261_in*MAS_in[0]<=t261*MAS[0]

	S += t261_in*MAS_in[1]<=t261*MAS[1]

	S += t261_in*MAS_in[2]<=t261*MAS[2]

	S += t261_in*MAS_in[3]<=t261*MAS[3]

	t261_mem0 = S.Task('t261_mem0', length=1, delay_cost=1)
	t261_mem0 += MAS_MEM[6]
	S += 36 < t261_mem0
	S += t261_mem0 <= t261

	t261_mem1 = S.Task('t261_mem1', length=1, delay_cost=1)
	t261_mem1 += MAS_MEM[7]
	S += 36 < t261_mem1
	S += t261_mem1 <= t261

	t270 = S.Task('t270', length=2, delay_cost=1)
	t270 += alt(MAS)
	t270_in = S.Task('t270_in', length=1, delay_cost=1)
	t270_in += alt(MAS_in)
	S += t270_in*MAS_in[0]<=t270*MAS[0]

	S += t270_in*MAS_in[1]<=t270*MAS[1]

	S += t270_in*MAS_in[2]<=t270*MAS[2]

	S += t270_in*MAS_in[3]<=t270*MAS[3]

	t270_mem0 = S.Task('t270_mem0', length=1, delay_cost=1)
	t270_mem0 += MAS_MEM[0]
	S += 27 < t270_mem0
	S += t270_mem0 <= t270

	t270_mem1 = S.Task('t270_mem1', length=1, delay_cost=1)
	t270_mem1 += MAS_MEM[7]
	S += 25 < t270_mem1
	S += t270_mem1 <= t270

	t90 = S.Task('t90', length=2, delay_cost=1)
	t90 += alt(MAS)
	t90_in = S.Task('t90_in', length=1, delay_cost=1)
	t90_in += alt(MAS_in)
	S += t90_in*MAS_in[0]<=t90*MAS[0]

	S += t90_in*MAS_in[1]<=t90*MAS[1]

	S += t90_in*MAS_in[2]<=t90*MAS[2]

	S += t90_in*MAS_in[3]<=t90*MAS[3]

	t90_mem0 = S.Task('t90_mem0', length=1, delay_cost=1)
	t90_mem0 += alt(MM_MEM)
	S += (t9_t2*MM[0])-1 < t90_mem0*MM_MEM[0]
	S += t90_mem0 <= t90

	t90_mem1 = S.Task('t90_mem1', length=1, delay_cost=1)
	t90_mem1 += alt(MAS_MEM)
	S += (t9_t5*MAS[0])-1 < t90_mem1*MAS_MEM[1]
	S += (t9_t5*MAS[1])-1 < t90_mem1*MAS_MEM[3]
	S += (t9_t5*MAS[2])-1 < t90_mem1*MAS_MEM[5]
	S += (t9_t5*MAS[3])-1 < t90_mem1*MAS_MEM[7]
	S += t90_mem1 <= t90

	t100 = S.Task('t100', length=2, delay_cost=1)
	t100 += alt(MAS)
	t100_in = S.Task('t100_in', length=1, delay_cost=1)
	t100_in += alt(MAS_in)
	S += t100_in*MAS_in[0]<=t100*MAS[0]

	S += t100_in*MAS_in[1]<=t100*MAS[1]

	S += t100_in*MAS_in[2]<=t100*MAS[2]

	S += t100_in*MAS_in[3]<=t100*MAS[3]

	t100_mem0 = S.Task('t100_mem0', length=1, delay_cost=1)
	t100_mem0 += alt(MM_MEM)
	S += (t10_t2*MM[0])-1 < t100_mem0*MM_MEM[0]
	S += t100_mem0 <= t100

	t100_mem1 = S.Task('t100_mem1', length=1, delay_cost=1)
	t100_mem1 += alt(MAS_MEM)
	S += (t10_t5*MAS[0])-1 < t100_mem1*MAS_MEM[1]
	S += (t10_t5*MAS[1])-1 < t100_mem1*MAS_MEM[3]
	S += (t10_t5*MAS[2])-1 < t100_mem1*MAS_MEM[5]
	S += (t10_t5*MAS[3])-1 < t100_mem1*MAS_MEM[7]
	S += t100_mem1 <= t100

	t120 = S.Task('t120', length=2, delay_cost=1)
	t120 += alt(MAS)
	t120_in = S.Task('t120_in', length=1, delay_cost=1)
	t120_in += alt(MAS_in)
	S += t120_in*MAS_in[0]<=t120*MAS[0]

	S += t120_in*MAS_in[1]<=t120*MAS[1]

	S += t120_in*MAS_in[2]<=t120*MAS[2]

	S += t120_in*MAS_in[3]<=t120*MAS[3]

	t120_mem0 = S.Task('t120_mem0', length=1, delay_cost=1)
	t120_mem0 += MAS_MEM[2]
	S += 25 < t120_mem0
	S += t120_mem0 <= t120

	t120_mem1 = S.Task('t120_mem1', length=1, delay_cost=1)
	t120_mem1 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < t120_mem1*MAS_MEM[1]
	S += (t111*MAS[1])-1 < t120_mem1*MAS_MEM[3]
	S += (t111*MAS[2])-1 < t120_mem1*MAS_MEM[5]
	S += (t111*MAS[3])-1 < t120_mem1*MAS_MEM[7]
	S += t120_mem1 <= t120

	t121 = S.Task('t121', length=2, delay_cost=1)
	t121 += alt(MAS)
	t121_in = S.Task('t121_in', length=1, delay_cost=1)
	t121_in += alt(MAS_in)
	S += t121_in*MAS_in[0]<=t121*MAS[0]

	S += t121_in*MAS_in[1]<=t121*MAS[1]

	S += t121_in*MAS_in[2]<=t121*MAS[2]

	S += t121_in*MAS_in[3]<=t121*MAS[3]

	t121_mem0 = S.Task('t121_mem0', length=1, delay_cost=1)
	t121_mem0 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < t121_mem0*MAS_MEM[0]
	S += (t111*MAS[1])-1 < t121_mem0*MAS_MEM[2]
	S += (t111*MAS[2])-1 < t121_mem0*MAS_MEM[4]
	S += (t111*MAS[3])-1 < t121_mem0*MAS_MEM[6]
	S += t121_mem0 <= t121

	t121_mem1 = S.Task('t121_mem1', length=1, delay_cost=1)
	t121_mem1 += MAS_MEM[3]
	S += 25 < t121_mem1
	S += t121_mem1 <= t121

	t301 = S.Task('t301', length=2, delay_cost=1)
	t301 += alt(MAS)
	t301_in = S.Task('t301_in', length=1, delay_cost=1)
	t301_in += alt(MAS_in)
	S += t301_in*MAS_in[0]<=t301*MAS[0]

	S += t301_in*MAS_in[1]<=t301*MAS[1]

	S += t301_in*MAS_in[2]<=t301*MAS[2]

	S += t301_in*MAS_in[3]<=t301*MAS[3]

	t301_mem0 = S.Task('t301_mem0', length=1, delay_cost=1)
	t301_mem0 += alt(MAS_MEM)
	S += (t291*MAS[0])-1 < t301_mem0*MAS_MEM[0]
	S += (t291*MAS[1])-1 < t301_mem0*MAS_MEM[2]
	S += (t291*MAS[2])-1 < t301_mem0*MAS_MEM[4]
	S += (t291*MAS[3])-1 < t301_mem0*MAS_MEM[6]
	S += t301_mem0 <= t301

	t301_mem1 = S.Task('t301_mem1', length=1, delay_cost=1)
	t301_mem1 += MAS_MEM[3]
	S += 34 < t301_mem1
	S += t301_mem1 <= t301

	t310 = S.Task('t310', length=2, delay_cost=1)
	t310 += alt(MAS)
	t310_in = S.Task('t310_in', length=1, delay_cost=1)
	t310_in += alt(MAS_in)
	S += t310_in*MAS_in[0]<=t310*MAS[0]

	S += t310_in*MAS_in[1]<=t310*MAS[1]

	S += t310_in*MAS_in[2]<=t310*MAS[2]

	S += t310_in*MAS_in[3]<=t310*MAS[3]

	t310_mem0 = S.Task('t310_mem0', length=1, delay_cost=1)
	t310_mem0 += alt(MAS_MEM)
	S += (t300*MAS[0])-1 < t310_mem0*MAS_MEM[0]
	S += (t300*MAS[1])-1 < t310_mem0*MAS_MEM[2]
	S += (t300*MAS[2])-1 < t310_mem0*MAS_MEM[4]
	S += (t300*MAS[3])-1 < t310_mem0*MAS_MEM[6]
	S += t310_mem0 <= t310

	t310_mem1 = S.Task('t310_mem1', length=1, delay_cost=1)
	t310_mem1 += MAIN_MEM_r[1]
	S += t310_mem1 <= t310

	t160 = S.Task('t160', length=2, delay_cost=1)
	t160 += alt(MAS)
	t160_in = S.Task('t160_in', length=1, delay_cost=1)
	t160_in += alt(MAS_in)
	S += t160_in*MAS_in[0]<=t160*MAS[0]

	S += t160_in*MAS_in[1]<=t160*MAS[1]

	S += t160_in*MAS_in[2]<=t160*MAS[2]

	S += t160_in*MAS_in[3]<=t160*MAS[3]

	t160_mem0 = S.Task('t160_mem0', length=1, delay_cost=1)
	t160_mem0 += alt(MAS_MEM)
	S += (t150*MAS[0])-1 < t160_mem0*MAS_MEM[0]
	S += (t150*MAS[1])-1 < t160_mem0*MAS_MEM[2]
	S += (t150*MAS[2])-1 < t160_mem0*MAS_MEM[4]
	S += (t150*MAS[3])-1 < t160_mem0*MAS_MEM[6]
	S += t160_mem0 <= t160

	t160_mem1 = S.Task('t160_mem1', length=1, delay_cost=1)
	t160_mem1 += alt(MAS_MEM)
	S += (t150*MAS[0])-1 < t160_mem1*MAS_MEM[1]
	S += (t150*MAS[1])-1 < t160_mem1*MAS_MEM[3]
	S += (t150*MAS[2])-1 < t160_mem1*MAS_MEM[5]
	S += (t150*MAS[3])-1 < t160_mem1*MAS_MEM[7]
	S += t160_mem1 <= t160

	t171 = S.Task('t171', length=2, delay_cost=1)
	t171 += alt(MAS)
	t171_in = S.Task('t171_in', length=1, delay_cost=1)
	t171_in += alt(MAS_in)
	S += t171_in*MAS_in[0]<=t171*MAS[0]

	S += t171_in*MAS_in[1]<=t171*MAS[1]

	S += t171_in*MAS_in[2]<=t171*MAS[2]

	S += t171_in*MAS_in[3]<=t171*MAS[3]

	t171_mem0 = S.Task('t171_mem0', length=1, delay_cost=1)
	t171_mem0 += alt(MAS_MEM)
	S += (t91*MAS[0])-1 < t171_mem0*MAS_MEM[0]
	S += (t91*MAS[1])-1 < t171_mem0*MAS_MEM[2]
	S += (t91*MAS[2])-1 < t171_mem0*MAS_MEM[4]
	S += (t91*MAS[3])-1 < t171_mem0*MAS_MEM[6]
	S += t171_mem0 <= t171

	t171_mem1 = S.Task('t171_mem1', length=1, delay_cost=1)
	t171_mem1 += alt(MAS_MEM)
	S += (t161*MAS[0])-1 < t171_mem1*MAS_MEM[1]
	S += (t161*MAS[1])-1 < t171_mem1*MAS_MEM[3]
	S += (t161*MAS[2])-1 < t171_mem1*MAS_MEM[5]
	S += (t161*MAS[3])-1 < t171_mem1*MAS_MEM[7]
	S += t171_mem1 <= t171

	t190 = S.Task('t190', length=2, delay_cost=1)
	t190 += alt(MAS)
	t190_in = S.Task('t190_in', length=1, delay_cost=1)
	t190_in += alt(MAS_in)
	S += t190_in*MAS_in[0]<=t190*MAS[0]

	S += t190_in*MAS_in[1]<=t190*MAS[1]

	S += t190_in*MAS_in[2]<=t190*MAS[2]

	S += t190_in*MAS_in[3]<=t190*MAS[3]

	t190_mem0 = S.Task('t190_mem0', length=1, delay_cost=1)
	t190_mem0 += alt(MAS_MEM)
	S += (t180*MAS[0])-1 < t190_mem0*MAS_MEM[0]
	S += (t180*MAS[1])-1 < t190_mem0*MAS_MEM[2]
	S += (t180*MAS[2])-1 < t190_mem0*MAS_MEM[4]
	S += (t180*MAS[3])-1 < t190_mem0*MAS_MEM[6]
	S += t190_mem0 <= t190

	t190_mem1 = S.Task('t190_mem1', length=1, delay_cost=1)
	t190_mem1 += MAS_MEM[3]
	S += 25 < t190_mem1
	S += t190_mem1 <= t190

	t191 = S.Task('t191', length=2, delay_cost=1)
	t191 += alt(MAS)
	t191_in = S.Task('t191_in', length=1, delay_cost=1)
	t191_in += alt(MAS_in)
	S += t191_in*MAS_in[0]<=t191*MAS[0]

	S += t191_in*MAS_in[1]<=t191*MAS[1]

	S += t191_in*MAS_in[2]<=t191*MAS[2]

	S += t191_in*MAS_in[3]<=t191*MAS[3]

	t191_mem0 = S.Task('t191_mem0', length=1, delay_cost=1)
	t191_mem0 += alt(MAS_MEM)
	S += (t181*MAS[0])-1 < t191_mem0*MAS_MEM[0]
	S += (t181*MAS[1])-1 < t191_mem0*MAS_MEM[2]
	S += (t181*MAS[2])-1 < t191_mem0*MAS_MEM[4]
	S += (t181*MAS[3])-1 < t191_mem0*MAS_MEM[6]
	S += t191_mem0 <= t191

	t191_mem1 = S.Task('t191_mem1', length=1, delay_cost=1)
	t191_mem1 += alt(MAS_MEM)
	S += (t111*MAS[0])-1 < t191_mem1*MAS_MEM[1]
	S += (t111*MAS[1])-1 < t191_mem1*MAS_MEM[3]
	S += (t111*MAS[2])-1 < t191_mem1*MAS_MEM[5]
	S += (t111*MAS[3])-1 < t191_mem1*MAS_MEM[7]
	S += t191_mem1 <= t191

	t231 = S.Task('t231', length=2, delay_cost=1)
	t231 += alt(MAS)
	t231_in = S.Task('t231_in', length=1, delay_cost=1)
	t231_in += alt(MAS_in)
	S += t231_in*MAS_in[0]<=t231*MAS[0]

	S += t231_in*MAS_in[1]<=t231*MAS[1]

	S += t231_in*MAS_in[2]<=t231*MAS[2]

	S += t231_in*MAS_in[3]<=t231*MAS[3]

	t231_mem0 = S.Task('t231_mem0', length=1, delay_cost=1)
	t231_mem0 += alt(MAS_MEM)
	S += (t221*MAS[0])-1 < t231_mem0*MAS_MEM[0]
	S += (t221*MAS[1])-1 < t231_mem0*MAS_MEM[2]
	S += (t221*MAS[2])-1 < t231_mem0*MAS_MEM[4]
	S += (t221*MAS[3])-1 < t231_mem0*MAS_MEM[6]
	S += t231_mem0 <= t231

	t231_mem1 = S.Task('t231_mem1', length=1, delay_cost=1)
	t231_mem1 += MAS_MEM[5]
	S += 33 < t231_mem1
	S += t231_mem1 <= t231

	t271 = S.Task('t271', length=2, delay_cost=1)
	t271 += alt(MAS)
	t271_in = S.Task('t271_in', length=1, delay_cost=1)
	t271_in += alt(MAS_in)
	S += t271_in*MAS_in[0]<=t271*MAS[0]

	S += t271_in*MAS_in[1]<=t271*MAS[1]

	S += t271_in*MAS_in[2]<=t271*MAS[2]

	S += t271_in*MAS_in[3]<=t271*MAS[3]

	t271_mem0 = S.Task('t271_mem0', length=1, delay_cost=1)
	t271_mem0 += alt(MAS_MEM)
	S += (t261*MAS[0])-1 < t271_mem0*MAS_MEM[0]
	S += (t261*MAS[1])-1 < t271_mem0*MAS_MEM[2]
	S += (t261*MAS[2])-1 < t271_mem0*MAS_MEM[4]
	S += (t261*MAS[3])-1 < t271_mem0*MAS_MEM[6]
	S += t271_mem0 <= t271

	t271_mem1 = S.Task('t271_mem1', length=1, delay_cost=1)
	t271_mem1 += MAS_MEM[7]
	S += 36 < t271_mem1
	S += t271_mem1 <= t271

	t280 = S.Task('t280', length=2, delay_cost=1)
	t280 += alt(MAS)
	t280_in = S.Task('t280_in', length=1, delay_cost=1)
	t280_in += alt(MAS_in)
	S += t280_in*MAS_in[0]<=t280*MAS[0]

	S += t280_in*MAS_in[1]<=t280*MAS[1]

	S += t280_in*MAS_in[2]<=t280*MAS[2]

	S += t280_in*MAS_in[3]<=t280*MAS[3]

	t280_mem0 = S.Task('t280_mem0', length=1, delay_cost=1)
	t280_mem0 += alt(MAS_MEM)
	S += (t270*MAS[0])-1 < t280_mem0*MAS_MEM[0]
	S += (t270*MAS[1])-1 < t280_mem0*MAS_MEM[2]
	S += (t270*MAS[2])-1 < t280_mem0*MAS_MEM[4]
	S += (t270*MAS[3])-1 < t280_mem0*MAS_MEM[6]
	S += t280_mem0 <= t280

	t280_mem1 = S.Task('t280_mem1', length=1, delay_cost=1)
	t280_mem1 += MAIN_MEM_r[1]
	S += t280_mem1 <= t280

	t130 = S.Task('t130', length=2, delay_cost=1)
	t130 += alt(MAS)
	t130_in = S.Task('t130_in', length=1, delay_cost=1)
	t130_in += alt(MAS_in)
	S += t130_in*MAS_in[0]<=t130*MAS[0]

	S += t130_in*MAS_in[1]<=t130*MAS[1]

	S += t130_in*MAS_in[2]<=t130*MAS[2]

	S += t130_in*MAS_in[3]<=t130*MAS[3]

	t130_mem0 = S.Task('t130_mem0', length=1, delay_cost=1)
	t130_mem0 += MAS_MEM[0]
	S += 20 < t130_mem0
	S += t130_mem0 <= t130

	t130_mem1 = S.Task('t130_mem1', length=1, delay_cost=1)
	t130_mem1 += alt(MAS_MEM)
	S += (t120*MAS[0])-1 < t130_mem1*MAS_MEM[1]
	S += (t120*MAS[1])-1 < t130_mem1*MAS_MEM[3]
	S += (t120*MAS[2])-1 < t130_mem1*MAS_MEM[5]
	S += (t120*MAS[3])-1 < t130_mem1*MAS_MEM[7]
	S += t130_mem1 <= t130

	t131 = S.Task('t131', length=2, delay_cost=1)
	t131 += alt(MAS)
	t131_in = S.Task('t131_in', length=1, delay_cost=1)
	t131_in += alt(MAS_in)
	S += t131_in*MAS_in[0]<=t131*MAS[0]

	S += t131_in*MAS_in[1]<=t131*MAS[1]

	S += t131_in*MAS_in[2]<=t131*MAS[2]

	S += t131_in*MAS_in[3]<=t131*MAS[3]

	t131_mem0 = S.Task('t131_mem0', length=1, delay_cost=1)
	t131_mem0 += MAS_MEM[6]
	S += 6 < t131_mem0
	S += t131_mem0 <= t131

	t131_mem1 = S.Task('t131_mem1', length=1, delay_cost=1)
	t131_mem1 += alt(MAS_MEM)
	S += (t121*MAS[0])-1 < t131_mem1*MAS_MEM[1]
	S += (t121*MAS[1])-1 < t131_mem1*MAS_MEM[3]
	S += (t121*MAS[2])-1 < t131_mem1*MAS_MEM[5]
	S += (t121*MAS[3])-1 < t131_mem1*MAS_MEM[7]
	S += t131_mem1 <= t131

	t311 = S.Task('t311', length=2, delay_cost=1)
	t311 += alt(MAS)
	t311_in = S.Task('t311_in', length=1, delay_cost=1)
	t311_in += alt(MAS_in)
	S += t311_in*MAS_in[0]<=t311*MAS[0]

	S += t311_in*MAS_in[1]<=t311*MAS[1]

	S += t311_in*MAS_in[2]<=t311*MAS[2]

	S += t311_in*MAS_in[3]<=t311*MAS[3]

	t311_mem0 = S.Task('t311_mem0', length=1, delay_cost=1)
	t311_mem0 += alt(MAS_MEM)
	S += (t301*MAS[0])-1 < t311_mem0*MAS_MEM[0]
	S += (t301*MAS[1])-1 < t311_mem0*MAS_MEM[2]
	S += (t301*MAS[2])-1 < t311_mem0*MAS_MEM[4]
	S += (t301*MAS[3])-1 < t311_mem0*MAS_MEM[6]
	S += t311_mem0 <= t311

	t311_mem1 = S.Task('t311_mem1', length=1, delay_cost=1)
	t311_mem1 += MAIN_MEM_r[1]
	S += t311_mem1 <= t311

	c010 = S.Task('c010', length=2, delay_cost=1)
	c010 += alt(MAS)
	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MAS_in)
	S += c010_in*MAS_in[0]<=c010*MAS[0]

	S += c010_in*MAS_in[1]<=c010*MAS[1]

	S += c010_in*MAS_in[2]<=c010*MAS[2]

	S += c010_in*MAS_in[3]<=c010*MAS[3]

	S += 24<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += alt(MAS_MEM)
	S += (t310*MAS[0])-1 < c010_mem0*MAS_MEM[0]
	S += (t310*MAS[1])-1 < c010_mem0*MAS_MEM[2]
	S += (t310*MAS[2])-1 < c010_mem0*MAS_MEM[4]
	S += (t310*MAS[3])-1 < c010_mem0*MAS_MEM[6]
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += alt(MAS_MEM)
	S += (t310*MAS[0])-1 < c010_mem1*MAS_MEM[1]
	S += (t310*MAS[1])-1 < c010_mem1*MAS_MEM[3]
	S += (t310*MAS[2])-1 < c010_mem1*MAS_MEM[5]
	S += (t310*MAS[3])-1 < c010_mem1*MAS_MEM[7]
	S += c010_mem1 <= c010

	t170 = S.Task('t170', length=2, delay_cost=1)
	t170 += alt(MAS)
	t170_in = S.Task('t170_in', length=1, delay_cost=1)
	t170_in += alt(MAS_in)
	S += t170_in*MAS_in[0]<=t170*MAS[0]

	S += t170_in*MAS_in[1]<=t170*MAS[1]

	S += t170_in*MAS_in[2]<=t170*MAS[2]

	S += t170_in*MAS_in[3]<=t170*MAS[3]

	t170_mem0 = S.Task('t170_mem0', length=1, delay_cost=1)
	t170_mem0 += alt(MAS_MEM)
	S += (t90*MAS[0])-1 < t170_mem0*MAS_MEM[0]
	S += (t90*MAS[1])-1 < t170_mem0*MAS_MEM[2]
	S += (t90*MAS[2])-1 < t170_mem0*MAS_MEM[4]
	S += (t90*MAS[3])-1 < t170_mem0*MAS_MEM[6]
	S += t170_mem0 <= t170

	t170_mem1 = S.Task('t170_mem1', length=1, delay_cost=1)
	t170_mem1 += alt(MAS_MEM)
	S += (t160*MAS[0])-1 < t170_mem1*MAS_MEM[1]
	S += (t160*MAS[1])-1 < t170_mem1*MAS_MEM[3]
	S += (t160*MAS[2])-1 < t170_mem1*MAS_MEM[5]
	S += (t160*MAS[3])-1 < t170_mem1*MAS_MEM[7]
	S += t170_mem1 <= t170

	c111 = S.Task('c111', length=2, delay_cost=1)
	c111 += alt(MAS)
	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	c111_in += alt(MAS_in)
	S += c111_in*MAS_in[0]<=c111*MAS[0]

	S += c111_in*MAS_in[1]<=c111*MAS[1]

	S += c111_in*MAS_in[2]<=c111*MAS[2]

	S += c111_in*MAS_in[3]<=c111*MAS[3]

	S += 19<c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += alt(MAS_MEM)
	S += (t101*MAS[0])-1 < c111_mem0*MAS_MEM[0]
	S += (t101*MAS[1])-1 < c111_mem0*MAS_MEM[2]
	S += (t101*MAS[2])-1 < c111_mem0*MAS_MEM[4]
	S += (t101*MAS[3])-1 < c111_mem0*MAS_MEM[6]
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += alt(MAS_MEM)
	S += (t171*MAS[0])-1 < c111_mem1*MAS_MEM[1]
	S += (t171*MAS[1])-1 < c111_mem1*MAS_MEM[3]
	S += (t171*MAS[2])-1 < c111_mem1*MAS_MEM[5]
	S += (t171*MAS[3])-1 < c111_mem1*MAS_MEM[7]
	S += c111_mem1 <= c111

	t200 = S.Task('t200', length=2, delay_cost=1)
	t200 += alt(MAS)
	t200_in = S.Task('t200_in', length=1, delay_cost=1)
	t200_in += alt(MAS_in)
	S += t200_in*MAS_in[0]<=t200*MAS[0]

	S += t200_in*MAS_in[1]<=t200*MAS[1]

	S += t200_in*MAS_in[2]<=t200*MAS[2]

	S += t200_in*MAS_in[3]<=t200*MAS[3]

	t200_mem0 = S.Task('t200_mem0', length=1, delay_cost=1)
	t200_mem0 += alt(MAS_MEM)
	S += (t190*MAS[0])-1 < t200_mem0*MAS_MEM[0]
	S += (t190*MAS[1])-1 < t200_mem0*MAS_MEM[2]
	S += (t190*MAS[2])-1 < t200_mem0*MAS_MEM[4]
	S += (t190*MAS[3])-1 < t200_mem0*MAS_MEM[6]
	S += t200_mem0 <= t200

	t200_mem1 = S.Task('t200_mem1', length=1, delay_cost=1)
	t200_mem1 += alt(MAS_MEM)
	S += (t190*MAS[0])-1 < t200_mem1*MAS_MEM[1]
	S += (t190*MAS[1])-1 < t200_mem1*MAS_MEM[3]
	S += (t190*MAS[2])-1 < t200_mem1*MAS_MEM[5]
	S += (t190*MAS[3])-1 < t200_mem1*MAS_MEM[7]
	S += t200_mem1 <= t200

	t201 = S.Task('t201', length=2, delay_cost=1)
	t201 += alt(MAS)
	t201_in = S.Task('t201_in', length=1, delay_cost=1)
	t201_in += alt(MAS_in)
	S += t201_in*MAS_in[0]<=t201*MAS[0]

	S += t201_in*MAS_in[1]<=t201*MAS[1]

	S += t201_in*MAS_in[2]<=t201*MAS[2]

	S += t201_in*MAS_in[3]<=t201*MAS[3]

	t201_mem0 = S.Task('t201_mem0', length=1, delay_cost=1)
	t201_mem0 += alt(MAS_MEM)
	S += (t191*MAS[0])-1 < t201_mem0*MAS_MEM[0]
	S += (t191*MAS[1])-1 < t201_mem0*MAS_MEM[2]
	S += (t191*MAS[2])-1 < t201_mem0*MAS_MEM[4]
	S += (t191*MAS[3])-1 < t201_mem0*MAS_MEM[6]
	S += t201_mem0 <= t201

	t201_mem1 = S.Task('t201_mem1', length=1, delay_cost=1)
	t201_mem1 += alt(MAS_MEM)
	S += (t191*MAS[0])-1 < t201_mem1*MAS_MEM[1]
	S += (t191*MAS[1])-1 < t201_mem1*MAS_MEM[3]
	S += (t191*MAS[2])-1 < t201_mem1*MAS_MEM[5]
	S += (t191*MAS[3])-1 < t201_mem1*MAS_MEM[7]
	S += t201_mem1 <= t201

	t240 = S.Task('t240', length=2, delay_cost=1)
	t240 += alt(MAS)
	t240_in = S.Task('t240_in', length=1, delay_cost=1)
	t240_in += alt(MAS_in)
	S += t240_in*MAS_in[0]<=t240*MAS[0]

	S += t240_in*MAS_in[1]<=t240*MAS[1]

	S += t240_in*MAS_in[2]<=t240*MAS[2]

	S += t240_in*MAS_in[3]<=t240*MAS[3]

	t240_mem0 = S.Task('t240_mem0', length=1, delay_cost=1)
	t240_mem0 += alt(MAS_MEM)
	S += (t230*MAS[0])-1 < t240_mem0*MAS_MEM[0]
	S += (t230*MAS[1])-1 < t240_mem0*MAS_MEM[2]
	S += (t230*MAS[2])-1 < t240_mem0*MAS_MEM[4]
	S += (t230*MAS[3])-1 < t240_mem0*MAS_MEM[6]
	S += t240_mem0 <= t240

	t240_mem1 = S.Task('t240_mem1', length=1, delay_cost=1)
	t240_mem1 += alt(MAS_MEM)
	S += (t231*MAS[0])-1 < t240_mem1*MAS_MEM[1]
	S += (t231*MAS[1])-1 < t240_mem1*MAS_MEM[3]
	S += (t231*MAS[2])-1 < t240_mem1*MAS_MEM[5]
	S += (t231*MAS[3])-1 < t240_mem1*MAS_MEM[7]
	S += t240_mem1 <= t240

	t241 = S.Task('t241', length=2, delay_cost=1)
	t241 += alt(MAS)
	t241_in = S.Task('t241_in', length=1, delay_cost=1)
	t241_in += alt(MAS_in)
	S += t241_in*MAS_in[0]<=t241*MAS[0]

	S += t241_in*MAS_in[1]<=t241*MAS[1]

	S += t241_in*MAS_in[2]<=t241*MAS[2]

	S += t241_in*MAS_in[3]<=t241*MAS[3]

	t241_mem0 = S.Task('t241_mem0', length=1, delay_cost=1)
	t241_mem0 += alt(MAS_MEM)
	S += (t231*MAS[0])-1 < t241_mem0*MAS_MEM[0]
	S += (t231*MAS[1])-1 < t241_mem0*MAS_MEM[2]
	S += (t231*MAS[2])-1 < t241_mem0*MAS_MEM[4]
	S += (t231*MAS[3])-1 < t241_mem0*MAS_MEM[6]
	S += t241_mem0 <= t241

	t241_mem1 = S.Task('t241_mem1', length=1, delay_cost=1)
	t241_mem1 += alt(MAS_MEM)
	S += (t230*MAS[0])-1 < t241_mem1*MAS_MEM[1]
	S += (t230*MAS[1])-1 < t241_mem1*MAS_MEM[3]
	S += (t230*MAS[2])-1 < t241_mem1*MAS_MEM[5]
	S += (t230*MAS[3])-1 < t241_mem1*MAS_MEM[7]
	S += t241_mem1 <= t241

	t281 = S.Task('t281', length=2, delay_cost=1)
	t281 += alt(MAS)
	t281_in = S.Task('t281_in', length=1, delay_cost=1)
	t281_in += alt(MAS_in)
	S += t281_in*MAS_in[0]<=t281*MAS[0]

	S += t281_in*MAS_in[1]<=t281*MAS[1]

	S += t281_in*MAS_in[2]<=t281*MAS[2]

	S += t281_in*MAS_in[3]<=t281*MAS[3]

	t281_mem0 = S.Task('t281_mem0', length=1, delay_cost=1)
	t281_mem0 += alt(MAS_MEM)
	S += (t271*MAS[0])-1 < t281_mem0*MAS_MEM[0]
	S += (t271*MAS[1])-1 < t281_mem0*MAS_MEM[2]
	S += (t271*MAS[2])-1 < t281_mem0*MAS_MEM[4]
	S += (t271*MAS[3])-1 < t281_mem0*MAS_MEM[6]
	S += t281_mem0 <= t281

	t281_mem1 = S.Task('t281_mem1', length=1, delay_cost=1)
	t281_mem1 += MAIN_MEM_r[1]
	S += t281_mem1 <= t281

	c210 = S.Task('c210', length=2, delay_cost=1)
	c210 += alt(MAS)
	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	c210_in += alt(MAS_in)
	S += c210_in*MAS_in[0]<=c210*MAS[0]

	S += c210_in*MAS_in[1]<=c210*MAS[1]

	S += c210_in*MAS_in[2]<=c210*MAS[2]

	S += c210_in*MAS_in[3]<=c210*MAS[3]

	S += 22<c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += alt(MAS_MEM)
	S += (t280*MAS[0])-1 < c210_mem0*MAS_MEM[0]
	S += (t280*MAS[1])-1 < c210_mem0*MAS_MEM[2]
	S += (t280*MAS[2])-1 < c210_mem0*MAS_MEM[4]
	S += (t280*MAS[3])-1 < c210_mem0*MAS_MEM[6]
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += alt(MAS_MEM)
	S += (t280*MAS[0])-1 < c210_mem1*MAS_MEM[1]
	S += (t280*MAS[1])-1 < c210_mem1*MAS_MEM[3]
	S += (t280*MAS[2])-1 < c210_mem1*MAS_MEM[5]
	S += (t280*MAS[3])-1 < c210_mem1*MAS_MEM[7]
	S += c210_mem1 <= c210

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage2MAS4/SQR012345/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

