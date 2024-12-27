from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 226
	S = Scenario("schedule7", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 0
	d_t0_t3_t0_in += MM_in[0]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 0
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 0
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 1
	d_t0_t10_in += MAS_in[0]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 1
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 1
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=11, delay_cost=1)
	S += d_t0_t3_t0 >= 1
	d_t0_t3_t0 += MM[0]

	d_t0_t10 = S.Task('d_t0_t10', length=3, delay_cost=1)
	S += d_t0_t10 >= 2
	d_t0_t10 += MAS[0]

	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 2
	d_t0_t3_t3_in += MAS_in[0]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 2
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 2
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=3, delay_cost=1)
	S += d_t0_t3_t3 >= 3
	d_t0_t3_t3 += MAS[0]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 3
	d_t1_a1_0_in += MAS_in[0]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 3
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 3
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=3, delay_cost=1)
	S += d_t1_a1_0 >= 4
	d_t1_a1_0 += MAS[0]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 4
	d_t3001_in += MAS_in[0]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 4
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 4
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 5
	d_t2_t11_in += MAS_in[0]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 5
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 5
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t3001 = S.Task('d_t3001', length=3, delay_cost=1)
	S += d_t3001 >= 5
	d_t3001 += MAS[0]

	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 6
	d_t1_a1_1_in += MAS_in[0]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 6
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 6
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_t11 = S.Task('d_t2_t11', length=3, delay_cost=1)
	S += d_t2_t11 >= 6
	d_t2_t11 += MAS[0]

	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 7
	d_t0_a1_0_in += MAS_in[1]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 7
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 7
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=3, delay_cost=1)
	S += d_t1_a1_1 >= 7
	d_t1_a1_1 += MAS[0]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=3, delay_cost=1)
	S += d_t0_a1_0 >= 8
	d_t0_a1_0 += MAS[1]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 8
	d_t0_a1_1_in += MAS_in[0]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 8
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 8
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=3, delay_cost=1)
	S += d_t0_a1_1 >= 9
	d_t0_a1_1 += MAS[0]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 9
	d_t2_t10_in += MAS_in[0]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 9
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 9
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 10
	d_t1_t3_t3_in += MAS_in[0]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 10
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 10
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t2_t10 = S.Task('d_t2_t10', length=3, delay_cost=1)
	S += d_t2_t10 >= 10
	d_t2_t10 += MAS[0]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=3, delay_cost=1)
	S += d_t1_t3_t3 >= 11
	d_t1_t3_t3 += MAS[0]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 11
	d_t3011_in += MAS_in[0]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 11
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 11
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t2_t2_t3_in = S.Task('d_t2_t2_t3_in', length=1, delay_cost=1)
	S += d_t2_t2_t3_in >= 12
	d_t2_t2_t3_in += MAS_in[1]

	d_t2_t2_t3_mem0 = S.Task('d_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem0 >= 12
	d_t2_t2_t3_mem0 += MAS_MEM[0]

	d_t2_t2_t3_mem1 = S.Task('d_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem1 >= 12
	d_t2_t2_t3_mem1 += MAS_MEM[1]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 12
	d_t2_t3_t2_in += MAS_in[0]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 12
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 12
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t3011 = S.Task('d_t3011', length=3, delay_cost=1)
	S += d_t3011 >= 12
	d_t3011 += MAS[0]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 13
	d_t1_t3_t2_in += MAS_in[0]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 13
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 13
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t2_t3 = S.Task('d_t2_t2_t3', length=3, delay_cost=1)
	S += d_t2_t2_t3 >= 13
	d_t2_t2_t3 += MAS[1]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=3, delay_cost=1)
	S += d_t2_t3_t2 >= 13
	d_t2_t3_t2 += MAS[0]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=3, delay_cost=1)
	S += d_t1_t3_t2 >= 14
	d_t1_t3_t2 += MAS[0]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 14
	d_t2_t3_t3_in += MAS_in[0]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 14
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 14
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3_t3_t1_in = S.Task('d_t3_t3_t1_in', length=1, delay_cost=1)
	S += d_t3_t3_t1_in >= 14
	d_t3_t3_t1_in += MM_in[0]

	d_t3_t3_t1_mem0 = S.Task('d_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem0 >= 14
	d_t3_t3_t1_mem0 += MAS_MEM[0]

	d_t3_t3_t1_mem1 = S.Task('d_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem1 >= 14
	d_t3_t3_t1_mem1 += MAS_MEM[1]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=3, delay_cost=1)
	S += d_t2_t3_t3 >= 15
	d_t2_t3_t3 += MAS[0]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 15
	d_t3010_in += MAS_in[0]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 15
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 15
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t3_t11_in = S.Task('d_t3_t11_in', length=1, delay_cost=1)
	S += d_t3_t11_in >= 15
	d_t3_t11_in += MAS_in[5]

	d_t3_t11_mem0 = S.Task('d_t3_t11_mem0', length=1, delay_cost=1)
	S += d_t3_t11_mem0 >= 15
	d_t3_t11_mem0 += MAS_MEM[0]

	d_t3_t11_mem1 = S.Task('d_t3_t11_mem1', length=1, delay_cost=1)
	S += d_t3_t11_mem1 >= 15
	d_t3_t11_mem1 += MAS_MEM[1]

	d_t3_t3_t1 = S.Task('d_t3_t3_t1', length=11, delay_cost=1)
	S += d_t3_t3_t1 >= 15
	d_t3_t3_t1 += MM[0]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 16
	d_t1_t10_in += MAS_in[0]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 16
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 16
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t4_in = S.Task('d_t1_t3_t4_in', length=1, delay_cost=1)
	S += d_t1_t3_t4_in >= 16
	d_t1_t3_t4_in += MM_in[0]

	d_t1_t3_t4_mem0 = S.Task('d_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem0 >= 16
	d_t1_t3_t4_mem0 += MAS_MEM[0]

	d_t1_t3_t4_mem1 = S.Task('d_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem1 >= 16
	d_t1_t3_t4_mem1 += MAS_MEM[1]

	d_t3010 = S.Task('d_t3010', length=3, delay_cost=1)
	S += d_t3010 >= 16
	d_t3010 += MAS[0]

	d_t3_t11 = S.Task('d_t3_t11', length=3, delay_cost=1)
	S += d_t3_t11 >= 16
	d_t3_t11 += MAS[5]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 17
	d_t0_t3_t2_in += MAS_in[0]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 17
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 17
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t1_t10 = S.Task('d_t1_t10', length=3, delay_cost=1)
	S += d_t1_t10 >= 17
	d_t1_t10 += MAS[0]

	d_t1_t3_t4 = S.Task('d_t1_t3_t4', length=11, delay_cost=1)
	S += d_t1_t3_t4 >= 17
	d_t1_t3_t4 += MM[0]

	d_t2_t3_t4_in = S.Task('d_t2_t3_t4_in', length=1, delay_cost=1)
	S += d_t2_t3_t4_in >= 17
	d_t2_t3_t4_in += MM_in[0]

	d_t2_t3_t4_mem0 = S.Task('d_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem0 >= 17
	d_t2_t3_t4_mem0 += MAS_MEM[0]

	d_t2_t3_t4_mem1 = S.Task('d_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem1 >= 17
	d_t2_t3_t4_mem1 += MAS_MEM[1]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 18
	d_t0_t3_t1_in += MM_in[0]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 18
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 18
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=3, delay_cost=1)
	S += d_t0_t3_t2 >= 18
	d_t0_t3_t2 += MAS[0]

	d_t2_t3_t4 = S.Task('d_t2_t3_t4', length=11, delay_cost=1)
	S += d_t2_t3_t4 >= 18
	d_t2_t3_t4 += MM[0]

	d_t3_a1_0_in = S.Task('d_t3_a1_0_in', length=1, delay_cost=1)
	S += d_t3_a1_0_in >= 18
	d_t3_a1_0_in += MAS_in[5]

	d_t3_a1_0_mem0 = S.Task('d_t3_a1_0_mem0', length=1, delay_cost=1)
	S += d_t3_a1_0_mem0 >= 18
	d_t3_a1_0_mem0 += MAS_MEM[0]

	d_t3_a1_0_mem1 = S.Task('d_t3_a1_0_mem1', length=1, delay_cost=1)
	S += d_t3_a1_0_mem1 >= 18
	d_t3_a1_0_mem1 += MAS_MEM[1]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=11, delay_cost=1)
	S += d_t0_t3_t1 >= 19
	d_t0_t3_t1 += MM[0]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 19
	d_t1_t11_in += MAS_in[0]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 19
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 19
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t3_a1_0 = S.Task('d_t3_a1_0', length=3, delay_cost=1)
	S += d_t3_a1_0 >= 19
	d_t3_a1_0 += MAS[5]

	d_t3_a1_1_in = S.Task('d_t3_a1_1_in', length=1, delay_cost=1)
	S += d_t3_a1_1_in >= 19
	d_t3_a1_1_in += MAS_in[1]

	d_t3_a1_1_mem0 = S.Task('d_t3_a1_1_mem0', length=1, delay_cost=1)
	S += d_t3_a1_1_mem0 >= 19
	d_t3_a1_1_mem0 += MAS_MEM[0]

	d_t3_a1_1_mem1 = S.Task('d_t3_a1_1_mem1', length=1, delay_cost=1)
	S += d_t3_a1_1_mem1 >= 19
	d_t3_a1_1_mem1 += MAS_MEM[1]

	d_t0_t3_t4_in = S.Task('d_t0_t3_t4_in', length=1, delay_cost=1)
	S += d_t0_t3_t4_in >= 20
	d_t0_t3_t4_in += MM_in[1]

	d_t0_t3_t4_mem0 = S.Task('d_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem0 >= 20
	d_t0_t3_t4_mem0 += MAS_MEM[0]

	d_t0_t3_t4_mem1 = S.Task('d_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem1 >= 20
	d_t0_t3_t4_mem1 += MAS_MEM[1]

	d_t1_t11 = S.Task('d_t1_t11', length=3, delay_cost=1)
	S += d_t1_t11 >= 20
	d_t1_t11 += MAS[0]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 20
	d_t1_t3_t0_in += MM_in[0]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 20
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 20
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t3_a1_1 = S.Task('d_t3_a1_1', length=3, delay_cost=1)
	S += d_t3_a1_1 >= 20
	d_t3_a1_1 += MAS[1]

	d_t0_t3_t4 = S.Task('d_t0_t3_t4', length=11, delay_cost=1)
	S += d_t0_t3_t4 >= 21
	d_t0_t3_t4 += MM[1]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=11, delay_cost=1)
	S += d_t1_t3_t0 >= 21
	d_t1_t3_t0 += MM[0]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 21
	d_t2_a1_0_in += MAS_in[0]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 21
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 21
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t3_t3_t3_in = S.Task('d_t3_t3_t3_in', length=1, delay_cost=1)
	S += d_t3_t3_t3_in >= 21
	d_t3_t3_t3_in += MAS_in[1]

	d_t3_t3_t3_mem0 = S.Task('d_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem0 >= 21
	d_t3_t3_t3_mem0 += MAS_MEM[0]

	d_t3_t3_t3_mem1 = S.Task('d_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem1 >= 21
	d_t3_t3_t3_mem1 += MAS_MEM[1]

	d_t1_t2_t3_in = S.Task('d_t1_t2_t3_in', length=1, delay_cost=1)
	S += d_t1_t2_t3_in >= 22
	d_t1_t2_t3_in += MAS_in[2]

	d_t1_t2_t3_mem0 = S.Task('d_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem0 >= 22
	d_t1_t2_t3_mem0 += MAS_MEM[0]

	d_t1_t2_t3_mem1 = S.Task('d_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem1 >= 22
	d_t1_t2_t3_mem1 += MAS_MEM[1]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=3, delay_cost=1)
	S += d_t2_a1_0 >= 22
	d_t2_a1_0 += MAS[0]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 22
	d_t2_t3_t0_in += MM_in[0]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 22
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 22
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t3_t3_t3 = S.Task('d_t3_t3_t3', length=3, delay_cost=1)
	S += d_t3_t3_t3 >= 22
	d_t3_t3_t3 += MAS[1]

	d_t1_t2_t3 = S.Task('d_t1_t2_t3', length=3, delay_cost=1)
	S += d_t1_t2_t3 >= 23
	d_t1_t2_t3 += MAS[2]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 23
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 23
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 23
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=11, delay_cost=1)
	S += d_t2_t3_t0 >= 23
	d_t2_t3_t0 += MM[0]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=11, delay_cost=1)
	S += d_t1_t3_t1 >= 24
	d_t1_t3_t1 += MM[0]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 24
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 24
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 24
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=11, delay_cost=1)
	S += d_t2_t3_t1 >= 25
	d_t2_t3_t1 += MM[0]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 25
	d_t3000_in += MAS_in[0]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 25
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 25
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t3000 = S.Task('d_t3000', length=3, delay_cost=1)
	S += d_t3000 >= 26
	d_t3000 += MAS[0]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 26
	d_t4001_in += MAS_in[0]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 26
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 26
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 27
	d_t4000_in += MAS_in[4]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 27
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 27
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t4001 = S.Task('d_t4001', length=3, delay_cost=1)
	S += d_t4001 >= 27
	d_t4001 += MAS[0]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 28
	d_t2_a1_1_in += MAS_in[2]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 28
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 28
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t3_t10_in = S.Task('d_t3_t10_in', length=1, delay_cost=1)
	S += d_t3_t10_in >= 28
	d_t3_t10_in += MAS_in[0]

	d_t3_t10_mem0 = S.Task('d_t3_t10_mem0', length=1, delay_cost=1)
	S += d_t3_t10_mem0 >= 28
	d_t3_t10_mem0 += MAS_MEM[0]

	d_t3_t10_mem1 = S.Task('d_t3_t10_mem1', length=1, delay_cost=1)
	S += d_t3_t10_mem1 >= 28
	d_t3_t10_mem1 += MAS_MEM[1]

	d_t4000 = S.Task('d_t4000', length=3, delay_cost=1)
	S += d_t4000 >= 28
	d_t4000 += MAS[4]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 29
	d_t0_t11_in += MAS_in[1]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 29
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 29
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t5_in = S.Task('d_t0_t3_t5_in', length=1, delay_cost=1)
	S += d_t0_t3_t5_in >= 29
	d_t0_t3_t5_in += MAS_in[3]

	d_t0_t3_t5_mem0 = S.Task('d_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem0 >= 29
	d_t0_t3_t5_mem0 += MM_MEM[0]

	d_t0_t3_t5_mem1 = S.Task('d_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem1 >= 29
	d_t0_t3_t5_mem1 += MM_MEM[1]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=3, delay_cost=1)
	S += d_t2_a1_1 >= 29
	d_t2_a1_1 += MAS[2]

	d_t3_t10 = S.Task('d_t3_t10', length=3, delay_cost=1)
	S += d_t3_t10 >= 29
	d_t3_t10 += MAS[0]

	d_t3_t3_t2_in = S.Task('d_t3_t3_t2_in', length=1, delay_cost=1)
	S += d_t3_t3_t2_in >= 29
	d_t3_t3_t2_in += MAS_in[2]

	d_t3_t3_t2_mem0 = S.Task('d_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem0 >= 29
	d_t3_t3_t2_mem0 += MAS_MEM[0]

	d_t3_t3_t2_mem1 = S.Task('d_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem1 >= 29
	d_t3_t3_t2_mem1 += MAS_MEM[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 30
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 30
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 30
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	d_t0_t11 = S.Task('d_t0_t11', length=3, delay_cost=1)
	S += d_t0_t11 >= 30
	d_t0_t11 += MAS[1]

	d_t0_t30_in = S.Task('d_t0_t30_in', length=1, delay_cost=1)
	S += d_t0_t30_in >= 30
	d_t0_t30_in += MAS_in[4]

	d_t0_t30_mem0 = S.Task('d_t0_t30_mem0', length=1, delay_cost=1)
	S += d_t0_t30_mem0 >= 30
	d_t0_t30_mem0 += MM_MEM[0]

	d_t0_t30_mem1 = S.Task('d_t0_t30_mem1', length=1, delay_cost=1)
	S += d_t0_t30_mem1 >= 30
	d_t0_t30_mem1 += MM_MEM[1]

	d_t0_t3_t5 = S.Task('d_t0_t3_t5', length=3, delay_cost=1)
	S += d_t0_t3_t5 >= 30
	d_t0_t3_t5 += MAS[3]

	d_t3_t3_t2 = S.Task('d_t3_t3_t2', length=3, delay_cost=1)
	S += d_t3_t3_t2 >= 30
	d_t3_t3_t2 += MAS[2]

	d_t4_t3_t2_in = S.Task('d_t4_t3_t2_in', length=1, delay_cost=1)
	S += d_t4_t3_t2_in >= 30
	d_t4_t3_t2_in += MAS_in[3]

	d_t4_t3_t2_mem0 = S.Task('d_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem0 >= 30
	d_t4_t3_t2_mem0 += MAS_MEM[8]

	d_t4_t3_t2_mem1 = S.Task('d_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem1 >= 30
	d_t4_t3_t2_mem1 += MAS_MEM[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=11, delay_cost=1)
	S += c_t1_t0_t1 >= 31
	c_t1_t0_t1 += MM[0]

	d_t0_t30 = S.Task('d_t0_t30', length=3, delay_cost=1)
	S += d_t0_t30 >= 31
	d_t0_t30 += MAS[4]

	d_t3_t3_t0_in = S.Task('d_t3_t3_t0_in', length=1, delay_cost=1)
	S += d_t3_t3_t0_in >= 31
	d_t3_t3_t0_in += MM_in[0]

	d_t3_t3_t0_mem0 = S.Task('d_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem0 >= 31
	d_t3_t3_t0_mem0 += MAS_MEM[0]

	d_t3_t3_t0_mem1 = S.Task('d_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem1 >= 31
	d_t3_t3_t0_mem1 += MAS_MEM[1]

	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	S += d_t4010_in >= 31
	d_t4010_in += MAS_in[0]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 31
	d_t4010_mem0 += MAIN_MEM_r[0]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 31
	d_t4010_mem1 += MAIN_MEM_r[1]

	d_t4_t3_t2 = S.Task('d_t4_t3_t2', length=3, delay_cost=1)
	S += d_t4_t3_t2 >= 31
	d_t4_t3_t2 += MAS[3]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 32
	c_t1_t1_t3_in += MAS_in[2]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 32
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 32
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	d_t0_t2_t3_in = S.Task('d_t0_t2_t3_in', length=1, delay_cost=1)
	S += d_t0_t2_t3_in >= 32
	d_t0_t2_t3_in += MAS_in[4]

	d_t0_t2_t3_mem0 = S.Task('d_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem0 >= 32
	d_t0_t2_t3_mem0 += MAS_MEM[0]

	d_t0_t2_t3_mem1 = S.Task('d_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem1 >= 32
	d_t0_t2_t3_mem1 += MAS_MEM[3]

	d_t3_t3_t0 = S.Task('d_t3_t3_t0', length=11, delay_cost=1)
	S += d_t3_t3_t0 >= 32
	d_t3_t3_t0 += MM[0]

	d_t4010 = S.Task('d_t4010', length=3, delay_cost=1)
	S += d_t4010 >= 32
	d_t4010 += MAS[0]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=3, delay_cost=1)
	S += c_t1_t1_t3 >= 33
	c_t1_t1_t3 += MAS[2]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 33
	c_t1_t21_in += MAS_in[0]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 33
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 33
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	d_t0_t2_t3 = S.Task('d_t0_t2_t3', length=3, delay_cost=1)
	S += d_t0_t2_t3 >= 33
	d_t0_t2_t3 += MAS[4]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 34
	c_t0_t1_t2_in += MAS_in[4]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 34
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 34
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t21 = S.Task('c_t1_t21', length=3, delay_cost=1)
	S += c_t1_t21 >= 34
	c_t1_t21 += MAS[0]

	d_t1_t30_in = S.Task('d_t1_t30_in', length=1, delay_cost=1)
	S += d_t1_t30_in >= 34
	d_t1_t30_in += MAS_in[1]

	d_t1_t30_mem0 = S.Task('d_t1_t30_mem0', length=1, delay_cost=1)
	S += d_t1_t30_mem0 >= 34
	d_t1_t30_mem0 += MM_MEM[0]

	d_t1_t30_mem1 = S.Task('d_t1_t30_mem1', length=1, delay_cost=1)
	S += d_t1_t30_mem1 >= 34
	d_t1_t30_mem1 += MM_MEM[1]

	d_t4_t10_in = S.Task('d_t4_t10_in', length=1, delay_cost=1)
	S += d_t4_t10_in >= 34
	d_t4_t10_in += MAS_in[3]

	d_t4_t10_mem0 = S.Task('d_t4_t10_mem0', length=1, delay_cost=1)
	S += d_t4_t10_mem0 >= 34
	d_t4_t10_mem0 += MAS_MEM[8]

	d_t4_t10_mem1 = S.Task('d_t4_t10_mem1', length=1, delay_cost=1)
	S += d_t4_t10_mem1 >= 34
	d_t4_t10_mem1 += MAS_MEM[1]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=3, delay_cost=1)
	S += c_t0_t1_t2 >= 35
	c_t0_t1_t2 += MAS[4]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 35
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 35
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 35
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	d_t1_t30 = S.Task('d_t1_t30', length=3, delay_cost=1)
	S += d_t1_t30 >= 35
	d_t1_t30 += MAS[1]

	d_t2_t3_t5_in = S.Task('d_t2_t3_t5_in', length=1, delay_cost=1)
	S += d_t2_t3_t5_in >= 35
	d_t2_t3_t5_in += MAS_in[1]

	d_t2_t3_t5_mem0 = S.Task('d_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem0 >= 35
	d_t2_t3_t5_mem0 += MM_MEM[0]

	d_t2_t3_t5_mem1 = S.Task('d_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem1 >= 35
	d_t2_t3_t5_mem1 += MM_MEM[1]

	d_t4_t10 = S.Task('d_t4_t10', length=3, delay_cost=1)
	S += d_t4_t10 >= 35
	d_t4_t10 += MAS[3]

	d_t4_t3_t0_in = S.Task('d_t4_t3_t0_in', length=1, delay_cost=1)
	S += d_t4_t3_t0_in >= 35
	d_t4_t3_t0_in += MM_in[1]

	d_t4_t3_t0_mem0 = S.Task('d_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem0 >= 35
	d_t4_t3_t0_mem0 += MAS_MEM[8]

	d_t4_t3_t0_mem1 = S.Task('d_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem1 >= 35
	d_t4_t3_t0_mem1 += MAS_MEM[1]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 36
	c_t0_t0_t3_in += MAS_in[2]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 36
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 36
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=11, delay_cost=1)
	S += c_t1_t1_t0 >= 36
	c_t1_t1_t0 += MM[0]

	d_t1_t3_t5_in = S.Task('d_t1_t3_t5_in', length=1, delay_cost=1)
	S += d_t1_t3_t5_in >= 36
	d_t1_t3_t5_in += MAS_in[5]

	d_t1_t3_t5_mem0 = S.Task('d_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem0 >= 36
	d_t1_t3_t5_mem0 += MM_MEM[0]

	d_t1_t3_t5_mem1 = S.Task('d_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem1 >= 36
	d_t1_t3_t5_mem1 += MM_MEM[1]

	d_t2_t3_t5 = S.Task('d_t2_t3_t5', length=3, delay_cost=1)
	S += d_t2_t3_t5 >= 36
	d_t2_t3_t5 += MAS[1]

	d_t4_t3_t0 = S.Task('d_t4_t3_t0', length=11, delay_cost=1)
	S += d_t4_t3_t0 >= 36
	d_t4_t3_t0 += MM[1]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=3, delay_cost=1)
	S += c_t0_t0_t3 >= 37
	c_t0_t0_t3 += MAS[2]

	d_t1_t3_t5 = S.Task('d_t1_t3_t5', length=3, delay_cost=1)
	S += d_t1_t3_t5 >= 37
	d_t1_t3_t5 += MAS[5]

	d_t2_t30_in = S.Task('d_t2_t30_in', length=1, delay_cost=1)
	S += d_t2_t30_in >= 37
	d_t2_t30_in += MAS_in[4]

	d_t2_t30_mem0 = S.Task('d_t2_t30_mem0', length=1, delay_cost=1)
	S += d_t2_t30_mem0 >= 37
	d_t2_t30_mem0 += MM_MEM[0]

	d_t2_t30_mem1 = S.Task('d_t2_t30_mem1', length=1, delay_cost=1)
	S += d_t2_t30_mem1 >= 37
	d_t2_t30_mem1 += MM_MEM[1]

	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	S += d_t4011_in >= 37
	d_t4011_in += MAS_in[5]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 37
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 37
	d_t4011_mem1 += MAIN_MEM_r[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 38
	c_t0_t31_in += MAS_in[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 38
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 38
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	d_t2_t30 = S.Task('d_t2_t30', length=3, delay_cost=1)
	S += d_t2_t30 >= 38
	d_t2_t30 += MAS[4]

	d_t4011 = S.Task('d_t4011', length=3, delay_cost=1)
	S += d_t4011 >= 38
	d_t4011 += MAS[5]

	c_t0_t31 = S.Task('c_t0_t31', length=3, delay_cost=1)
	S += c_t0_t31 >= 39
	c_t0_t31 += MAS[0]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 39
	c_t1_t31_in += MAS_in[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 39
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 39
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 40
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 40
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 40
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=3, delay_cost=1)
	S += c_t1_t31 >= 40
	c_t1_t31 += MAS[1]

	d_t4_a1_0_in = S.Task('d_t4_a1_0_in', length=1, delay_cost=1)
	S += d_t4_a1_0_in >= 40
	d_t4_a1_0_in += MAS_in[4]

	d_t4_a1_0_mem0 = S.Task('d_t4_a1_0_mem0', length=1, delay_cost=1)
	S += d_t4_a1_0_mem0 >= 40
	d_t4_a1_0_mem0 += MAS_MEM[0]

	d_t4_a1_0_mem1 = S.Task('d_t4_a1_0_mem1', length=1, delay_cost=1)
	S += d_t4_a1_0_mem1 >= 40
	d_t4_a1_0_mem1 += MAS_MEM[11]

	d_t4_a1_1_in = S.Task('d_t4_a1_1_in', length=1, delay_cost=1)
	S += d_t4_a1_1_in >= 40
	d_t4_a1_1_in += MAS_in[1]

	d_t4_a1_1_mem0 = S.Task('d_t4_a1_1_mem0', length=1, delay_cost=1)
	S += d_t4_a1_1_mem0 >= 40
	d_t4_a1_1_mem0 += MAS_MEM[10]

	d_t4_a1_1_mem1 = S.Task('d_t4_a1_1_mem1', length=1, delay_cost=1)
	S += d_t4_a1_1_mem1 >= 40
	d_t4_a1_1_mem1 += MAS_MEM[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=11, delay_cost=1)
	S += c_t1_t1_t1 >= 41
	c_t1_t1_t1 += MM[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 41
	c_t1_t20_in += MAS_in[3]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 41
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 41
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	d_t4_a1_0 = S.Task('d_t4_a1_0', length=3, delay_cost=1)
	S += d_t4_a1_0 >= 41
	d_t4_a1_0 += MAS[4]

	d_t4_a1_1 = S.Task('d_t4_a1_1', length=3, delay_cost=1)
	S += d_t4_a1_1 >= 41
	d_t4_a1_1 += MAS[1]

	d_t4_t11_in = S.Task('d_t4_t11_in', length=1, delay_cost=1)
	S += d_t4_t11_in >= 41
	d_t4_t11_in += MAS_in[1]

	d_t4_t11_mem0 = S.Task('d_t4_t11_mem0', length=1, delay_cost=1)
	S += d_t4_t11_mem0 >= 41
	d_t4_t11_mem0 += MAS_MEM[0]

	d_t4_t11_mem1 = S.Task('d_t4_t11_mem1', length=1, delay_cost=1)
	S += d_t4_t11_mem1 >= 41
	d_t4_t11_mem1 += MAS_MEM[11]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 42
	c_t0_t21_in += MAS_in[3]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 42
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 42
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t20 = S.Task('c_t1_t20', length=3, delay_cost=1)
	S += c_t1_t20 >= 42
	c_t1_t20 += MAS[3]

	d_t4_t11 = S.Task('d_t4_t11', length=3, delay_cost=1)
	S += d_t4_t11 >= 42
	d_t4_t11 += MAS[1]

	d_t4_t3_t3_in = S.Task('d_t4_t3_t3_in', length=1, delay_cost=1)
	S += d_t4_t3_t3_in >= 42
	d_t4_t3_t3_in += MAS_in[5]

	d_t4_t3_t3_mem0 = S.Task('d_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem0 >= 42
	d_t4_t3_t3_mem0 += MAS_MEM[0]

	d_t4_t3_t3_mem1 = S.Task('d_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem1 >= 42
	d_t4_t3_t3_mem1 += MAS_MEM[11]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 43
	c_t0_t0_t0_in += MM_in[1]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 43
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 43
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t21 = S.Task('c_t0_t21', length=3, delay_cost=1)
	S += c_t0_t21 >= 43
	c_t0_t21 += MAS[3]

	d_t4_t3_t1_in = S.Task('d_t4_t3_t1_in', length=1, delay_cost=1)
	S += d_t4_t3_t1_in >= 43
	d_t4_t3_t1_in += MM_in[0]

	d_t4_t3_t1_mem0 = S.Task('d_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem0 >= 43
	d_t4_t3_t1_mem0 += MAS_MEM[0]

	d_t4_t3_t1_mem1 = S.Task('d_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem1 >= 43
	d_t4_t3_t1_mem1 += MAS_MEM[11]

	d_t4_t3_t3 = S.Task('d_t4_t3_t3', length=3, delay_cost=1)
	S += d_t4_t3_t3 >= 43
	d_t4_t3_t3 += MAS[5]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=11, delay_cost=1)
	S += c_t0_t0_t0 >= 44
	c_t0_t0_t0 += MM[1]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 44
	c_t0_t30_in += MAS_in[3]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 44
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 44
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 44
	c_t1_t4_t1_in += MM_in[1]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 44
	c_t1_t4_t1_mem0 += MAS_MEM[0]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 44
	c_t1_t4_t1_mem1 += MAS_MEM[3]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 44
	c_t1_t4_t2_in += MAS_in[0]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 44
	c_t1_t4_t2_mem0 += MAS_MEM[6]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 44
	c_t1_t4_t2_mem1 += MAS_MEM[1]

	d_t4_t3_t1 = S.Task('d_t4_t3_t1', length=11, delay_cost=1)
	S += d_t4_t3_t1 >= 44
	d_t4_t3_t1 += MM[0]

	c_t0_t30 = S.Task('c_t0_t30', length=3, delay_cost=1)
	S += c_t0_t30 >= 45
	c_t0_t30 += MAS[3]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 45
	c_t0_t4_t1_in += MM_in[1]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 45
	c_t0_t4_t1_mem0 += MAS_MEM[6]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 45
	c_t0_t4_t1_mem1 += MAS_MEM[1]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 45
	c_t1_t1_t2_in += MAS_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 45
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 45
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=11, delay_cost=1)
	S += c_t1_t4_t1 >= 45
	c_t1_t4_t1 += MM[1]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=3, delay_cost=1)
	S += c_t1_t4_t2 >= 45
	c_t1_t4_t2 += MAS[0]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=11, delay_cost=1)
	S += c_t0_t4_t1 >= 46
	c_t0_t4_t1 += MM[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=3, delay_cost=1)
	S += c_t1_t1_t2 >= 46
	c_t1_t1_t2 += MAS[0]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 46
	c_t1_t30_in += MAS_in[4]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 46
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 46
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 47
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 47
	c_t0_t4_t3_mem0 += MAS_MEM[6]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 47
	c_t0_t4_t3_mem1 += MAS_MEM[1]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 47
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 47
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 47
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=3, delay_cost=1)
	S += c_t1_t30 >= 47
	c_t1_t30 += MAS[4]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 48
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 48
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 48
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=3, delay_cost=1)
	S += c_t0_t4_t3 >= 48
	c_t0_t4_t3 += MAS[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=11, delay_cost=1)
	S += c_t1_t0_t0 >= 48
	c_t1_t0_t0 += MM[0]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 48
	c_t1_t1_t4_in += MM_in[1]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 48
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 48
	c_t1_t1_t4_mem1 += MAS_MEM[5]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=11, delay_cost=1)
	S += c_t0_t1_t0 >= 49
	c_t0_t1_t0 += MM[0]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=11, delay_cost=1)
	S += c_t1_t1_t4 >= 49
	c_t1_t1_t4 += MM[1]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 49
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 49
	c_t1_t4_t0_mem0 += MAS_MEM[6]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 49
	c_t1_t4_t0_mem1 += MAS_MEM[9]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 49
	c_t1_t4_t3_in += MAS_in[3]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 49
	c_t1_t4_t3_mem0 += MAS_MEM[8]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 49
	c_t1_t4_t3_mem1 += MAS_MEM[3]

	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	S += d_t5000_in >= 49
	d_t5000_in += MAS_in[1]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 49
	d_t5000_mem0 += MAIN_MEM_r[0]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 49
	d_t5000_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 50
	c_t0_t0_t2_in += MAS_in[3]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 50
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 50
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=11, delay_cost=1)
	S += c_t1_t4_t0 >= 50
	c_t1_t4_t0 += MM[0]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=3, delay_cost=1)
	S += c_t1_t4_t3 >= 50
	c_t1_t4_t3 += MAS[3]

	d_t5000 = S.Task('d_t5000', length=3, delay_cost=1)
	S += d_t5000 >= 50
	d_t5000 += MAS[1]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=3, delay_cost=1)
	S += c_t0_t0_t2 >= 51
	c_t0_t0_t2 += MAS[3]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 51
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 51
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 51
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 51
	c_t1_t10_in += MAS_in[2]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 51
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 51
	c_t1_t10_mem1 += MM_MEM[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=11, delay_cost=1)
	S += c_t0_t1_t1 >= 52
	c_t0_t1_t1 += MM[0]

	c_t1_t10 = S.Task('c_t1_t10', length=3, delay_cost=1)
	S += c_t1_t10 >= 52
	c_t1_t10 += MAS[2]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 52
	c_t1_t1_t5_in += MAS_in[4]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 52
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 52
	c_t1_t1_t5_mem1 += MM_MEM[1]

	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	S += d_t5010_in >= 52
	d_t5010_in += MAS_in[2]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 52
	d_t5010_mem0 += MAIN_MEM_r[0]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 52
	d_t5010_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 53
	c_t0_t0_t4_in += MM_in[1]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 53
	c_t0_t0_t4_mem0 += MAS_MEM[6]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 53
	c_t0_t0_t4_mem1 += MAS_MEM[5]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 53
	c_t0_t20_in += MAS_in[4]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 53
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 53
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=3, delay_cost=1)
	S += c_t1_t1_t5 >= 53
	c_t1_t1_t5 += MAS[4]

	d_t5010 = S.Task('d_t5010', length=3, delay_cost=1)
	S += d_t5010 >= 53
	d_t5010 += MAS[2]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=11, delay_cost=1)
	S += c_t0_t0_t4 >= 54
	c_t0_t0_t4 += MM[1]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 54
	c_t0_t1_t3_in += MAS_in[2]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 54
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 54
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t20 = S.Task('c_t0_t20', length=3, delay_cost=1)
	S += c_t0_t20 >= 54
	c_t0_t20 += MAS[4]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=3, delay_cost=1)
	S += c_t0_t1_t3 >= 55
	c_t0_t1_t3 += MAS[2]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 55
	c_t1_t0_t3_in += MAS_in[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 55
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 55
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	d_t5_t3_t0_in = S.Task('d_t5_t3_t0_in', length=1, delay_cost=1)
	S += d_t5_t3_t0_in >= 55
	d_t5_t3_t0_in += MM_in[0]

	d_t5_t3_t0_mem0 = S.Task('d_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem0 >= 55
	d_t5_t3_t0_mem0 += MAS_MEM[2]

	d_t5_t3_t0_mem1 = S.Task('d_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem1 >= 55
	d_t5_t3_t0_mem1 += MAS_MEM[5]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 56
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 56
	c_t0_t4_t0_mem0 += MAS_MEM[8]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 56
	c_t0_t4_t0_mem1 += MAS_MEM[7]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=3, delay_cost=1)
	S += c_t1_t0_t3 >= 56
	c_t1_t0_t3 += MAS[1]

	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	S += d_t5011_in >= 56
	d_t5011_in += MAS_in[1]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 56
	d_t5011_mem0 += MAIN_MEM_r[0]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 56
	d_t5011_mem1 += MAIN_MEM_r[1]

	d_t5_t10_in = S.Task('d_t5_t10_in', length=1, delay_cost=1)
	S += d_t5_t10_in >= 56
	d_t5_t10_in += MAS_in[3]

	d_t5_t10_mem0 = S.Task('d_t5_t10_mem0', length=1, delay_cost=1)
	S += d_t5_t10_mem0 >= 56
	d_t5_t10_mem0 += MAS_MEM[2]

	d_t5_t10_mem1 = S.Task('d_t5_t10_mem1', length=1, delay_cost=1)
	S += d_t5_t10_mem1 >= 56
	d_t5_t10_mem1 += MAS_MEM[5]

	d_t5_t3_t0 = S.Task('d_t5_t3_t0', length=11, delay_cost=1)
	S += d_t5_t3_t0 >= 56
	d_t5_t3_t0 += MM[0]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 57
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 57
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 57
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 57
	c_t0_t1_t4_in += MM_in[1]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 57
	c_t0_t1_t4_mem0 += MAS_MEM[8]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 57
	c_t0_t1_t4_mem1 += MAS_MEM[5]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=11, delay_cost=1)
	S += c_t0_t4_t0 >= 57
	c_t0_t4_t0 += MM[0]

	d_t5011 = S.Task('d_t5011', length=3, delay_cost=1)
	S += d_t5011 >= 57
	d_t5011 += MAS[1]

	d_t5_t10 = S.Task('d_t5_t10', length=3, delay_cost=1)
	S += d_t5_t10 >= 57
	d_t5_t10 += MAS[3]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=11, delay_cost=1)
	S += c_t0_t0_t1 >= 58
	c_t0_t0_t1 += MM[0]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=11, delay_cost=1)
	S += c_t0_t1_t4 >= 58
	c_t0_t1_t4 += MM[1]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 58
	c_t0_t4_t2_in += MAS_in[4]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 58
	c_t0_t4_t2_mem0 += MAS_MEM[8]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 58
	c_t0_t4_t2_mem1 += MAS_MEM[7]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 58
	c_t1_t00_in += MAS_in[2]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 58
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 58
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 58
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 58
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 58
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=3, delay_cost=1)
	S += c_t0_t4_t2 >= 59
	c_t0_t4_t2 += MAS[4]

	c_t1_t00 = S.Task('c_t1_t00', length=3, delay_cost=1)
	S += c_t1_t00 >= 59
	c_t1_t00 += MAS[2]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=3, delay_cost=1)
	S += c_t1_t0_t2 >= 59
	c_t1_t0_t2 += MAS[0]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 59
	c_t1_t0_t5_in += MAS_in[1]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 59
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 59
	c_t1_t0_t5_mem1 += MM_MEM[1]

	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	S += d_t5001_in >= 59
	d_t5001_in += MAS_in[0]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 59
	d_t5001_mem0 += MAIN_MEM_r[0]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 59
	d_t5001_mem1 += MAIN_MEM_r[1]

	d_t5_a1_0_in = S.Task('d_t5_a1_0_in', length=1, delay_cost=1)
	S += d_t5_a1_0_in >= 59
	d_t5_a1_0_in += MAS_in[2]

	d_t5_a1_0_mem0 = S.Task('d_t5_a1_0_mem0', length=1, delay_cost=1)
	S += d_t5_a1_0_mem0 >= 59
	d_t5_a1_0_mem0 += MAS_MEM[4]

	d_t5_a1_0_mem1 = S.Task('d_t5_a1_0_mem1', length=1, delay_cost=1)
	S += d_t5_a1_0_mem1 >= 59
	d_t5_a1_0_mem1 += MAS_MEM[3]

	d_t5_a1_1_in = S.Task('d_t5_a1_1_in', length=1, delay_cost=1)
	S += d_t5_a1_1_in >= 59
	d_t5_a1_1_in += MAS_in[4]

	d_t5_a1_1_mem0 = S.Task('d_t5_a1_1_mem0', length=1, delay_cost=1)
	S += d_t5_a1_1_mem0 >= 59
	d_t5_a1_1_mem0 += MAS_MEM[2]

	d_t5_a1_1_mem1 = S.Task('d_t5_a1_1_mem1', length=1, delay_cost=1)
	S += d_t5_a1_1_mem1 >= 59
	d_t5_a1_1_mem1 += MAS_MEM[5]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=3, delay_cost=1)
	S += c_t1_t0_t5 >= 60
	c_t1_t0_t5 += MAS[1]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 60
	c_t3110_in += MAS_in[0]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 60
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 60
	c_t3110_mem1 += MAIN_MEM_r[1]

	d_t5001 = S.Task('d_t5001', length=3, delay_cost=1)
	S += d_t5001 >= 60
	d_t5001 += MAS[0]

	d_t5_a1_0 = S.Task('d_t5_a1_0', length=3, delay_cost=1)
	S += d_t5_a1_0 >= 60
	d_t5_a1_0 += MAS[2]

	d_t5_a1_1 = S.Task('d_t5_a1_1', length=3, delay_cost=1)
	S += d_t5_a1_1 >= 60
	d_t5_a1_1 += MAS[4]

	d_t5_t3_t3_in = S.Task('d_t5_t3_t3_in', length=1, delay_cost=1)
	S += d_t5_t3_t3_in >= 60
	d_t5_t3_t3_in += MAS_in[2]

	d_t5_t3_t3_mem0 = S.Task('d_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem0 >= 60
	d_t5_t3_t3_mem0 += MAS_MEM[4]

	d_t5_t3_t3_mem1 = S.Task('d_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem1 >= 60
	d_t5_t3_t3_mem1 += MAS_MEM[3]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 61
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 61
	c_t1_t0_t4_mem0 += MAS_MEM[0]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 61
	c_t1_t0_t4_mem1 += MAS_MEM[3]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 61
	c_t2_t20_in += MAS_in[0]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 61
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 61
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t3110 = S.Task('c_t3110', length=3, delay_cost=1)
	S += c_t3110 >= 61
	c_t3110 += MAS[0]

	d_t5_t3_t3 = S.Task('d_t5_t3_t3', length=3, delay_cost=1)
	S += d_t5_t3_t3 >= 61
	d_t5_t3_t3 += MAS[2]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 62
	c_t0_t1_t5_in += MAS_in[2]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 62
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 62
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=11, delay_cost=1)
	S += c_t1_t0_t4 >= 62
	c_t1_t0_t4 += MM[0]

	c_t2_t20 = S.Task('c_t2_t20', length=3, delay_cost=1)
	S += c_t2_t20 >= 62
	c_t2_t20 += MAS[0]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 62
	c_t4100_in += MAS_in[0]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 62
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 62
	c_t4100_mem1 += MAIN_MEM_r[1]

	d_t5_t11_in = S.Task('d_t5_t11_in', length=1, delay_cost=1)
	S += d_t5_t11_in >= 62
	d_t5_t11_in += MAS_in[5]

	d_t5_t11_mem0 = S.Task('d_t5_t11_mem0', length=1, delay_cost=1)
	S += d_t5_t11_mem0 >= 62
	d_t5_t11_mem0 += MAS_MEM[0]

	d_t5_t11_mem1 = S.Task('d_t5_t11_mem1', length=1, delay_cost=1)
	S += d_t5_t11_mem1 >= 62
	d_t5_t11_mem1 += MAS_MEM[3]

	d_t5_t3_t2_in = S.Task('d_t5_t3_t2_in', length=1, delay_cost=1)
	S += d_t5_t3_t2_in >= 62
	d_t5_t3_t2_in += MAS_in[4]

	d_t5_t3_t2_mem0 = S.Task('d_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem0 >= 62
	d_t5_t3_t2_mem0 += MAS_MEM[2]

	d_t5_t3_t2_mem1 = S.Task('d_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem1 >= 62
	d_t5_t3_t2_mem1 += MAS_MEM[1]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 63
	c_t0_t10_in += MAS_in[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 63
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 63
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=3, delay_cost=1)
	S += c_t0_t1_t5 >= 63
	c_t0_t1_t5 += MAS[2]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 63
	c_t2_t1_t3_in += MAS_in[0]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 63
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 63
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t4100 = S.Task('c_t4100', length=3, delay_cost=1)
	S += c_t4100 >= 63
	c_t4100 += MAS[0]

	d_t5_t11 = S.Task('d_t5_t11', length=3, delay_cost=1)
	S += d_t5_t11 >= 63
	d_t5_t11 += MAS[5]

	d_t5_t3_t1_in = S.Task('d_t5_t3_t1_in', length=1, delay_cost=1)
	S += d_t5_t3_t1_in >= 63
	d_t5_t3_t1_in += MM_in[0]

	d_t5_t3_t1_mem0 = S.Task('d_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem0 >= 63
	d_t5_t3_t1_mem0 += MAS_MEM[0]

	d_t5_t3_t1_mem1 = S.Task('d_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem1 >= 63
	d_t5_t3_t1_mem1 += MAS_MEM[3]

	d_t5_t3_t2 = S.Task('d_t5_t3_t2', length=3, delay_cost=1)
	S += d_t5_t3_t2 >= 63
	d_t5_t3_t2 += MAS[4]

	c_t0_t10 = S.Task('c_t0_t10', length=3, delay_cost=1)
	S += c_t0_t10 >= 64
	c_t0_t10 += MAS[1]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=3, delay_cost=1)
	S += c_t2_t1_t3 >= 64
	c_t2_t1_t3 += MAS[0]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 64
	c_t4110_in += MAS_in[5]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 64
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 64
	c_t4110_mem1 += MAIN_MEM_r[1]

	d_t5_t3_t1 = S.Task('d_t5_t3_t1', length=11, delay_cost=1)
	S += d_t5_t3_t1 >= 64
	d_t5_t3_t1 += MM[0]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 65
	c_t4000_in += MAS_in[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 65
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 65
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4110 = S.Task('c_t4110', length=3, delay_cost=1)
	S += c_t4110 >= 65
	c_t4110 += MAS[5]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 66
	c_t3101_in += MAS_in[3]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 66
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 66
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=3, delay_cost=1)
	S += c_t4000 >= 66
	c_t4000 += MAS[1]

	c_t3101 = S.Task('c_t3101', length=3, delay_cost=1)
	S += c_t3101 >= 67
	c_t3101 += MAS[3]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 67
	c_t3111_in += MAS_in[2]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 67
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 67
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 67
	c_t4_t30_in += MAS_in[4]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 67
	c_t4_t30_mem0 += MAS_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 67
	c_t4_t30_mem1 += MAS_MEM[11]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 68
	c_t0_t0_t5_in += MAS_in[3]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 68
	c_t0_t0_t5_mem0 += MM_MEM[2]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 68
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t3111 = S.Task('c_t3111', length=3, delay_cost=1)
	S += c_t3111 >= 68
	c_t3111 += MAS[2]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 68
	c_t4001_in += MAS_in[5]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 68
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 68
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 68
	c_t4_t0_t0_in += MM_in[1]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 68
	c_t4_t0_t0_mem0 += MAS_MEM[2]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 68
	c_t4_t0_t0_mem1 += MAS_MEM[1]

	c_t4_t30 = S.Task('c_t4_t30', length=3, delay_cost=1)
	S += c_t4_t30 >= 68
	c_t4_t30 += MAS[4]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 69
	c_t0_t00_in += MAS_in[1]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 69
	c_t0_t00_mem0 += MM_MEM[2]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 69
	c_t0_t00_mem1 += MM_MEM[1]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=3, delay_cost=1)
	S += c_t0_t0_t5 >= 69
	c_t0_t0_t5 += MAS[3]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 69
	c_t2_t21_in += MAS_in[2]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 69
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 69
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t4001 = S.Task('c_t4001', length=3, delay_cost=1)
	S += c_t4001 >= 69
	c_t4001 += MAS[5]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=11, delay_cost=1)
	S += c_t4_t0_t0 >= 69
	c_t4_t0_t0 += MM[1]

	c_t0_t00 = S.Task('c_t0_t00', length=3, delay_cost=1)
	S += c_t0_t00 >= 70
	c_t0_t00 += MAS[1]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 70
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 70
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 70
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t21 = S.Task('c_t2_t21', length=3, delay_cost=1)
	S += c_t2_t21 >= 70
	c_t2_t21 += MAS[2]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 70
	c_t3_t31_in += MAS_in[4]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 70
	c_t3_t31_mem0 += MAS_MEM[6]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 70
	c_t3_t31_mem1 += MAS_MEM[5]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=11, delay_cost=1)
	S += c_t2_t0_t0 >= 71
	c_t2_t0_t0 += MM[0]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 71
	c_t3_t1_t3_in += MAS_in[0]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 71
	c_t3_t1_t3_mem0 += MAS_MEM[0]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 71
	c_t3_t1_t3_mem1 += MAS_MEM[5]

	c_t3_t31 = S.Task('c_t3_t31', length=3, delay_cost=1)
	S += c_t3_t31 >= 71
	c_t3_t31 += MAS[4]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 71
	c_t4011_in += MAS_in[3]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 71
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 71
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 71
	c_t4_t0_t2_in += MAS_in[4]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 71
	c_t4_t0_t2_mem0 += MAS_MEM[2]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 71
	c_t4_t0_t2_mem1 += MAS_MEM[11]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 72
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 72
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 72
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 72
	c_t2_t4_t2_in += MAS_in[1]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 72
	c_t2_t4_t2_mem0 += MAS_MEM[0]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 72
	c_t2_t4_t2_mem1 += MAS_MEM[5]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=3, delay_cost=1)
	S += c_t3_t1_t3 >= 72
	c_t3_t1_t3 += MAS[0]

	c_t4011 = S.Task('c_t4011', length=3, delay_cost=1)
	S += c_t4011 >= 72
	c_t4011 += MAS[3]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=3, delay_cost=1)
	S += c_t4_t0_t2 >= 72
	c_t4_t0_t2 += MAS[4]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=11, delay_cost=1)
	S += c_t2_t0_t1 >= 73
	c_t2_t0_t1 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 73
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 73
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 73
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=3, delay_cost=1)
	S += c_t2_t4_t2 >= 73
	c_t2_t4_t2 += MAS[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=11, delay_cost=1)
	S += c_t2_t1_t1 >= 74
	c_t2_t1_t1 += MM[0]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 74
	c_t2_t1_t2_in += MAS_in[0]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 74
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 74
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 74
	c_t4_t21_in += MAS_in[4]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 74
	c_t4_t21_mem0 += MAS_MEM[10]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 74
	c_t4_t21_mem1 += MAS_MEM[7]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=3, delay_cost=1)
	S += c_t2_t1_t2 >= 75
	c_t2_t1_t2 += MAS[0]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 75
	c_t3100_in += MAS_in[1]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 75
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 75
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t4_t21 = S.Task('c_t4_t21', length=3, delay_cost=1)
	S += c_t4_t21 >= 75
	c_t4_t21 += MAS[4]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 76
	c_t3011_in += MAS_in[2]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 76
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 76
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3100 = S.Task('c_t3100', length=3, delay_cost=1)
	S += c_t3100 >= 76
	c_t3100 += MAS[1]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 77
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 77
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 77
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 77
	c_t2_t1_t4_in += MM_in[1]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 77
	c_t2_t1_t4_mem0 += MAS_MEM[0]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 77
	c_t2_t1_t4_mem1 += MAS_MEM[1]

	c_t3011 = S.Task('c_t3011', length=3, delay_cost=1)
	S += c_t3011 >= 77
	c_t3011 += MAS[2]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=11, delay_cost=1)
	S += c_t2_t1_t0 >= 78
	c_t2_t1_t0 += MM[0]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=11, delay_cost=1)
	S += c_t2_t1_t4 >= 78
	c_t2_t1_t4 += MM[1]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 78
	c_t3_t0_t3_in += MAS_in[4]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 78
	c_t3_t0_t3_mem0 += MAS_MEM[2]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 78
	c_t3_t0_t3_mem1 += MAS_MEM[7]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 78
	c_t4010_in += MAS_in[3]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 78
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 78
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 79
	c_t3000_in += MAS_in[1]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 79
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 79
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=3, delay_cost=1)
	S += c_t3_t0_t3 >= 79
	c_t3_t0_t3 += MAS[4]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 79
	c_t3_t1_t1_in += MM_in[1]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 79
	c_t3_t1_t1_mem0 += MAS_MEM[4]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 79
	c_t3_t1_t1_mem1 += MAS_MEM[5]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 79
	c_t3_t30_in += MAS_in[0]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 79
	c_t3_t30_mem0 += MAS_MEM[2]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 79
	c_t3_t30_mem1 += MAS_MEM[1]

	c_t4010 = S.Task('c_t4010', length=3, delay_cost=1)
	S += c_t4010 >= 79
	c_t4010 += MAS[3]

	c_t3000 = S.Task('c_t3000', length=3, delay_cost=1)
	S += c_t3000 >= 80
	c_t3000 += MAS[1]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 80
	c_t3001_in += MAS_in[4]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 80
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 80
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=11, delay_cost=1)
	S += c_t3_t1_t1 >= 80
	c_t3_t1_t1 += MM[1]

	c_t3_t30 = S.Task('c_t3_t30', length=3, delay_cost=1)
	S += c_t3_t30 >= 80
	c_t3_t30 += MAS[0]

	c_t3001 = S.Task('c_t3001', length=3, delay_cost=1)
	S += c_t3001 >= 81
	c_t3001 += MAS[4]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 81
	c_t4101_in += MAS_in[1]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 81
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 81
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 81
	c_t4_t1_t0_in += MM_in[1]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 81
	c_t4_t1_t0_mem0 += MAS_MEM[6]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 81
	c_t4_t1_t0_mem1 += MAS_MEM[11]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 81
	c_t4_t20_in += MAS_in[4]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 81
	c_t4_t20_mem0 += MAS_MEM[2]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 81
	c_t4_t20_mem1 += MAS_MEM[7]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 82
	c_t2_t0_t3_in += MAS_in[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 82
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 82
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 82
	c_t3_t0_t0_in += MM_in[1]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 82
	c_t3_t0_t0_mem0 += MAS_MEM[2]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 82
	c_t3_t0_t0_mem1 += MAS_MEM[3]

	c_t4101 = S.Task('c_t4101', length=3, delay_cost=1)
	S += c_t4101 >= 82
	c_t4101 += MAS[1]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=11, delay_cost=1)
	S += c_t4_t1_t0 >= 82
	c_t4_t1_t0 += MM[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 82
	c_t4_t1_t2_in += MAS_in[3]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 82
	c_t4_t1_t2_mem0 += MAS_MEM[6]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 82
	c_t4_t1_t2_mem1 += MAS_MEM[7]

	c_t4_t20 = S.Task('c_t4_t20', length=3, delay_cost=1)
	S += c_t4_t20 >= 82
	c_t4_t20 += MAS[4]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=3, delay_cost=1)
	S += c_t2_t0_t3 >= 83
	c_t2_t0_t3 += MAS[0]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 83
	c_t2_t0_t5_in += MAS_in[2]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 83
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 83
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 83
	c_t2_t30_in += MAS_in[0]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 83
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 83
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=11, delay_cost=1)
	S += c_t3_t0_t0 >= 83
	c_t3_t0_t0 += MM[1]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 83
	c_t3_t0_t1_in += MM_in[1]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 83
	c_t3_t0_t1_mem0 += MAS_MEM[8]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 83
	c_t3_t0_t1_mem1 += MAS_MEM[7]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 83
	c_t3_t0_t2_in += MAS_in[4]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 83
	c_t3_t0_t2_mem0 += MAS_MEM[2]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 83
	c_t3_t0_t2_mem1 += MAS_MEM[9]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=3, delay_cost=1)
	S += c_t4_t1_t2 >= 83
	c_t4_t1_t2 += MAS[3]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 84
	c_t2_t00_in += MAS_in[3]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 84
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 84
	c_t2_t00_mem1 += MM_MEM[1]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=3, delay_cost=1)
	S += c_t2_t0_t5 >= 84
	c_t2_t0_t5 += MAS[2]

	c_t2_t30 = S.Task('c_t2_t30', length=3, delay_cost=1)
	S += c_t2_t30 >= 84
	c_t2_t30 += MAS[0]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 84
	c_t3010_in += MAS_in[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 84
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 84
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=11, delay_cost=1)
	S += c_t3_t0_t1 >= 84
	c_t3_t0_t1 += MM[1]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=3, delay_cost=1)
	S += c_t3_t0_t2 >= 84
	c_t3_t0_t2 += MAS[4]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 84
	c_t3_t21_in += MAS_in[5]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 84
	c_t3_t21_mem0 += MAS_MEM[8]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 84
	c_t3_t21_mem1 += MAS_MEM[5]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 84
	c_t4_t0_t3_in += MAS_in[4]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 84
	c_t4_t0_t3_mem0 += MAS_MEM[0]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 84
	c_t4_t0_t3_mem1 += MAS_MEM[3]

	c_t2_t00 = S.Task('c_t2_t00', length=3, delay_cost=1)
	S += c_t2_t00 >= 85
	c_t2_t00 += MAS[3]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 85
	c_t2_t31_in += MAS_in[5]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 85
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 85
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t3010 = S.Task('c_t3010', length=3, delay_cost=1)
	S += c_t3010 >= 85
	c_t3010 += MAS[0]

	c_t3_t21 = S.Task('c_t3_t21', length=3, delay_cost=1)
	S += c_t3_t21 >= 85
	c_t3_t21 += MAS[5]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 85
	c_t4_t0_t1_in += MM_in[1]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 85
	c_t4_t0_t1_mem0 += MAS_MEM[10]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 85
	c_t4_t0_t1_mem1 += MAS_MEM[3]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=3, delay_cost=1)
	S += c_t4_t0_t3 >= 85
	c_t4_t0_t3 += MAS[4]

	c_t2_t31 = S.Task('c_t2_t31', length=3, delay_cost=1)
	S += c_t2_t31 >= 86
	c_t2_t31 += MAS[5]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 86
	c_t2_t4_t0_in += MM_in[1]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 86
	c_t2_t4_t0_mem0 += MAS_MEM[0]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 86
	c_t2_t4_t0_mem1 += MAS_MEM[1]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=11, delay_cost=1)
	S += c_t4_t0_t1 >= 86
	c_t4_t0_t1 += MM[1]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 86
	c_t5001_in += MAS_in[2]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 86
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 86
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 87
	c_t2_t0_t2_in += MAS_in[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 87
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 87
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=11, delay_cost=1)
	S += c_t2_t4_t0 >= 87
	c_t2_t4_t0 += MM[1]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 87
	c_t3_t1_t2_in += MAS_in[1]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 87
	c_t3_t1_t2_mem0 += MAS_MEM[0]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 87
	c_t3_t1_t2_mem1 += MAS_MEM[5]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 87
	c_t3_t20_in += MAS_in[4]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 87
	c_t3_t20_mem0 += MAS_MEM[2]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 87
	c_t3_t20_mem1 += MAS_MEM[1]

	c_t5001 = S.Task('c_t5001', length=3, delay_cost=1)
	S += c_t5001 >= 87
	c_t5001 += MAS[2]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=3, delay_cost=1)
	S += c_t2_t0_t2 >= 88
	c_t2_t0_t2 += MAS[0]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 88
	c_t2_t10_in += MAS_in[5]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 88
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 88
	c_t2_t10_mem1 += MM_MEM[1]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 88
	c_t2_t4_t1_in += MM_in[1]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 88
	c_t2_t4_t1_mem0 += MAS_MEM[4]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 88
	c_t2_t4_t1_mem1 += MAS_MEM[11]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 88
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 88
	c_t3_t1_t0_mem0 += MAS_MEM[0]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 88
	c_t3_t1_t0_mem1 += MAS_MEM[1]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=3, delay_cost=1)
	S += c_t3_t1_t2 >= 88
	c_t3_t1_t2 += MAS[1]

	c_t3_t20 = S.Task('c_t3_t20', length=3, delay_cost=1)
	S += c_t3_t20 >= 88
	c_t3_t20 += MAS[4]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 88
	c_t5000_in += MAS_in[0]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 88
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 88
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=3, delay_cost=1)
	S += c_t2_t10 >= 89
	c_t2_t10 += MAS[5]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 89
	c_t2_t1_t5_in += MAS_in[2]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 89
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 89
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=11, delay_cost=1)
	S += c_t2_t4_t1 >= 89
	c_t2_t4_t1 += MM[1]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 89
	c_t2_t4_t3_in += MAS_in[3]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 89
	c_t2_t4_t3_mem0 += MAS_MEM[0]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 89
	c_t2_t4_t3_mem1 += MAS_MEM[11]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=11, delay_cost=1)
	S += c_t3_t1_t0 >= 89
	c_t3_t1_t0 += MM[0]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 89
	c_t4111_in += MAS_in[0]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 89
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 89
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t5000 = S.Task('c_t5000', length=3, delay_cost=1)
	S += c_t5000 >= 89
	c_t5000 += MAS[0]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 90
	c_t2_t0_t4_in += MM_in[1]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 90
	c_t2_t0_t4_mem0 += MAS_MEM[0]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 90
	c_t2_t0_t4_mem1 += MAS_MEM[1]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=3, delay_cost=1)
	S += c_t2_t1_t5 >= 90
	c_t2_t1_t5 += MAS[2]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=3, delay_cost=1)
	S += c_t2_t4_t3 >= 90
	c_t2_t4_t3 += MAS[3]

	c_t4111 = S.Task('c_t4111', length=3, delay_cost=1)
	S += c_t4111 >= 90
	c_t4111 += MAS[0]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 90
	c_t5101_in += MAS_in[1]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 90
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 90
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=11, delay_cost=1)
	S += c_t2_t0_t4 >= 91
	c_t2_t0_t4 += MM[1]

	c_t5101 = S.Task('c_t5101', length=3, delay_cost=1)
	S += c_t5101 >= 91
	c_t5101 += MAS[1]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 91
	c_t5111_in += MAS_in[1]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 91
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 91
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 91
	c_t5_t0_t2_in += MAS_in[3]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 91
	c_t5_t0_t2_mem0 += MAS_MEM[0]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 91
	c_t5_t0_t2_mem1 += MAS_MEM[5]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 92
	c_t4_t1_t1_in += MM_in[1]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 92
	c_t4_t1_t1_mem0 += MAS_MEM[6]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 92
	c_t4_t1_t1_mem1 += MAS_MEM[1]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 92
	c_t5010_in += MAS_in[0]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 92
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 92
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5111 = S.Task('c_t5111', length=3, delay_cost=1)
	S += c_t5111 >= 92
	c_t5111 += MAS[1]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=3, delay_cost=1)
	S += c_t5_t0_t2 >= 92
	c_t5_t0_t2 += MAS[3]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=11, delay_cost=1)
	S += c_t4_t1_t1 >= 93
	c_t4_t1_t1 += MM[1]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 93
	c_t4_t31_in += MAS_in[1]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 93
	c_t4_t31_mem0 += MAS_MEM[2]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 93
	c_t4_t31_mem1 += MAS_MEM[1]

	c_t5010 = S.Task('c_t5010', length=3, delay_cost=1)
	S += c_t5010 >= 93
	c_t5010 += MAS[0]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 93
	c_t5110_in += MAS_in[3]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 93
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 93
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 93
	c_t5_t0_t1_in += MM_in[1]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 93
	c_t5_t0_t1_mem0 += MAS_MEM[4]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 93
	c_t5_t0_t1_mem1 += MAS_MEM[3]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 94
	c_t4_t1_t3_in += MAS_in[2]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 94
	c_t4_t1_t3_mem0 += MAS_MEM[10]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 94
	c_t4_t1_t3_mem1 += MAS_MEM[1]

	c_t4_t31 = S.Task('c_t4_t31', length=3, delay_cost=1)
	S += c_t4_t31 >= 94
	c_t4_t31 += MAS[1]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 94
	c_t5100_in += MAS_in[1]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 94
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 94
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5110 = S.Task('c_t5110', length=3, delay_cost=1)
	S += c_t5110 >= 94
	c_t5110 += MAS[3]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=11, delay_cost=1)
	S += c_t5_t0_t1 >= 94
	c_t5_t0_t1 += MM[1]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 94
	c_t5_t31_in += MAS_in[0]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 94
	c_t5_t31_mem0 += MAS_MEM[2]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 94
	c_t5_t31_mem1 += MAS_MEM[3]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=3, delay_cost=1)
	S += c_t4_t1_t3 >= 95
	c_t4_t1_t3 += MAS[2]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 95
	c_t5011_in += MAS_in[1]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 95
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 95
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5100 = S.Task('c_t5100', length=3, delay_cost=1)
	S += c_t5100 >= 95
	c_t5100 += MAS[1]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 95
	c_t5_t20_in += MAS_in[3]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 95
	c_t5_t20_mem0 += MAS_MEM[0]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 95
	c_t5_t20_mem1 += MAS_MEM[1]

	c_t5_t31 = S.Task('c_t5_t31', length=3, delay_cost=1)
	S += c_t5_t31 >= 95
	c_t5_t31 += MAS[0]

	c_t5011 = S.Task('c_t5011', length=3, delay_cost=1)
	S += c_t5011 >= 96
	c_t5011 += MAS[1]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 96
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 96
	c_t5_t1_t0_mem0 += MAS_MEM[0]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 96
	c_t5_t1_t0_mem1 += MAS_MEM[7]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 96
	c_t5_t1_t3_in += MAS_in[4]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 96
	c_t5_t1_t3_mem0 += MAS_MEM[6]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 96
	c_t5_t1_t3_mem1 += MAS_MEM[3]

	c_t5_t20 = S.Task('c_t5_t20', length=3, delay_cost=1)
	S += c_t5_t20 >= 96
	c_t5_t20 += MAS[3]

	d_t2_t01_in = S.Task('d_t2_t01_in', length=1, delay_cost=1)
	S += d_t2_t01_in >= 96
	d_t2_t01_in += MAS_in[2]

	d_t2_t01_mem0 = S.Task('d_t2_t01_mem0', length=1, delay_cost=1)
	S += d_t2_t01_mem0 >= 96
	d_t2_t01_mem0 += MAIN_MEM_r[0]

	d_t2_t01_mem1 = S.Task('d_t2_t01_mem1', length=1, delay_cost=1)
	S += d_t2_t01_mem1 >= 96
	d_t2_t01_mem1 += MAS_MEM[5]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=11, delay_cost=1)
	S += c_t5_t1_t0 >= 97
	c_t5_t1_t0 += MM[0]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=3, delay_cost=1)
	S += c_t5_t1_t3 >= 97
	c_t5_t1_t3 += MAS[4]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 97
	c_t5_t30_in += MAS_in[2]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 97
	c_t5_t30_mem0 += MAS_MEM[2]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 97
	c_t5_t30_mem1 += MAS_MEM[7]

	d_t0_t00_in = S.Task('d_t0_t00_in', length=1, delay_cost=1)
	S += d_t0_t00_in >= 97
	d_t0_t00_in += MAS_in[3]

	d_t0_t00_mem0 = S.Task('d_t0_t00_mem0', length=1, delay_cost=1)
	S += d_t0_t00_mem0 >= 97
	d_t0_t00_mem0 += MAIN_MEM_r[0]

	d_t0_t00_mem1 = S.Task('d_t0_t00_mem1', length=1, delay_cost=1)
	S += d_t0_t00_mem1 >= 97
	d_t0_t00_mem1 += MAS_MEM[3]

	d_t2_t01 = S.Task('d_t2_t01', length=3, delay_cost=1)
	S += d_t2_t01 >= 97
	d_t2_t01 += MAS[2]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 98
	c_t5_t0_t0_in += MM_in[1]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 98
	c_t5_t0_t0_mem0 += MAS_MEM[0]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 98
	c_t5_t0_t0_mem1 += MAS_MEM[3]

	c_t5_t30 = S.Task('c_t5_t30', length=3, delay_cost=1)
	S += c_t5_t30 >= 98
	c_t5_t30 += MAS[2]

	d_t0_t00 = S.Task('d_t0_t00', length=3, delay_cost=1)
	S += d_t0_t00 >= 98
	d_t0_t00 += MAS[3]

	d_t1_t01_in = S.Task('d_t1_t01_in', length=1, delay_cost=1)
	S += d_t1_t01_in >= 98
	d_t1_t01_in += MAS_in[3]

	d_t1_t01_mem0 = S.Task('d_t1_t01_mem0', length=1, delay_cost=1)
	S += d_t1_t01_mem0 >= 98
	d_t1_t01_mem0 += MAIN_MEM_r[0]

	d_t1_t01_mem1 = S.Task('d_t1_t01_mem1', length=1, delay_cost=1)
	S += d_t1_t01_mem1 >= 98
	d_t1_t01_mem1 += MAS_MEM[1]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=11, delay_cost=1)
	S += c_t5_t0_t0 >= 99
	c_t5_t0_t0 += MM[1]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 99
	c_t5_t0_t3_in += MAS_in[1]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 99
	c_t5_t0_t3_mem0 += MAS_MEM[2]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 99
	c_t5_t0_t3_mem1 += MAS_MEM[3]

	d_t0_t01_in = S.Task('d_t0_t01_in', length=1, delay_cost=1)
	S += d_t0_t01_in >= 99
	d_t0_t01_in += MAS_in[5]

	d_t0_t01_mem0 = S.Task('d_t0_t01_mem0', length=1, delay_cost=1)
	S += d_t0_t01_mem0 >= 99
	d_t0_t01_mem0 += MAIN_MEM_r[0]

	d_t0_t01_mem1 = S.Task('d_t0_t01_mem1', length=1, delay_cost=1)
	S += d_t0_t01_mem1 >= 99
	d_t0_t01_mem1 += MAS_MEM[1]

	d_t1_t01 = S.Task('d_t1_t01', length=3, delay_cost=1)
	S += d_t1_t01 >= 99
	d_t1_t01 += MAS[3]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=3, delay_cost=1)
	S += c_t5_t0_t3 >= 100
	c_t5_t0_t3 += MAS[1]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 100
	c_t5_t21_in += MAS_in[2]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 100
	c_t5_t21_mem0 += MAS_MEM[4]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 100
	c_t5_t21_mem1 += MAS_MEM[3]

	d_t0_t01 = S.Task('d_t0_t01', length=3, delay_cost=1)
	S += d_t0_t01 >= 100
	d_t0_t01 += MAS[5]

	d_t2_t00_in = S.Task('d_t2_t00_in', length=1, delay_cost=1)
	S += d_t2_t00_in >= 100
	d_t2_t00_in += MAS_in[3]

	d_t2_t00_mem0 = S.Task('d_t2_t00_mem0', length=1, delay_cost=1)
	S += d_t2_t00_mem0 >= 100
	d_t2_t00_mem0 += MAIN_MEM_r[0]

	d_t2_t00_mem1 = S.Task('d_t2_t00_mem1', length=1, delay_cost=1)
	S += d_t2_t00_mem1 >= 100
	d_t2_t00_mem1 += MAS_MEM[1]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 101
	c_t5_t1_t1_in += MM_in[1]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 101
	c_t5_t1_t1_mem0 += MAS_MEM[2]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 101
	c_t5_t1_t1_mem1 += MAS_MEM[3]

	c_t5_t21 = S.Task('c_t5_t21', length=3, delay_cost=1)
	S += c_t5_t21 >= 101
	c_t5_t21 += MAS[2]

	d_t1_t00_in = S.Task('d_t1_t00_in', length=1, delay_cost=1)
	S += d_t1_t00_in >= 101
	d_t1_t00_in += MAS_in[4]

	d_t1_t00_mem0 = S.Task('d_t1_t00_mem0', length=1, delay_cost=1)
	S += d_t1_t00_mem0 >= 101
	d_t1_t00_mem0 += MAIN_MEM_r[0]

	d_t1_t00_mem1 = S.Task('d_t1_t00_mem1', length=1, delay_cost=1)
	S += d_t1_t00_mem1 >= 101
	d_t1_t00_mem1 += MAS_MEM[1]

	d_t2_t00 = S.Task('d_t2_t00', length=3, delay_cost=1)
	S += d_t2_t00 >= 101
	d_t2_t00 += MAS[3]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=11, delay_cost=1)
	S += c_t5_t1_t1 >= 102
	c_t5_t1_t1 += MM[1]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 102
	c_t5_t1_t2_in += MAS_in[2]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 102
	c_t5_t1_t2_mem0 += MAS_MEM[0]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 102
	c_t5_t1_t2_mem1 += MAS_MEM[3]

	d_t1_t00 = S.Task('d_t1_t00', length=3, delay_cost=1)
	S += d_t1_t00 >= 102
	d_t1_t00 += MAS[4]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=3, delay_cost=1)
	S += c_t5_t1_t2 >= 103
	c_t5_t1_t2 += MAS[2]


	# new tasks
	d_t0_t2_t0 = S.Task('d_t0_t2_t0', length=11, delay_cost=1)
	d_t0_t2_t0 += alt(MM)
	d_t0_t2_t0_in = S.Task('d_t0_t2_t0_in', length=1, delay_cost=1)
	d_t0_t2_t0_in += alt(MM_in)
	S += d_t0_t2_t0_in*MM_in[0]<=d_t0_t2_t0*MM[0]
	S += d_t0_t2_t0_in*MM_in[1]<=d_t0_t2_t0*MM[1]
	d_t0_t2_t0_mem0 = S.Task('d_t0_t2_t0_mem0', length=1, delay_cost=1)
	d_t0_t2_t0_mem0 += MAS_MEM[6]
	S += 100 < d_t0_t2_t0_mem0
	S += d_t0_t2_t0_mem0 <= d_t0_t2_t0

	d_t0_t2_t0_mem1 = S.Task('d_t0_t2_t0_mem1', length=1, delay_cost=1)
	d_t0_t2_t0_mem1 += MAS_MEM[1]
	S += 4 < d_t0_t2_t0_mem1
	S += d_t0_t2_t0_mem1 <= d_t0_t2_t0

	d_t0_t2_t1 = S.Task('d_t0_t2_t1', length=11, delay_cost=1)
	d_t0_t2_t1 += alt(MM)
	d_t0_t2_t1_in = S.Task('d_t0_t2_t1_in', length=1, delay_cost=1)
	d_t0_t2_t1_in += alt(MM_in)
	S += d_t0_t2_t1_in*MM_in[0]<=d_t0_t2_t1*MM[0]
	S += d_t0_t2_t1_in*MM_in[1]<=d_t0_t2_t1*MM[1]
	d_t0_t2_t1_mem0 = S.Task('d_t0_t2_t1_mem0', length=1, delay_cost=1)
	d_t0_t2_t1_mem0 += MAS_MEM[10]
	S += 102 < d_t0_t2_t1_mem0
	S += d_t0_t2_t1_mem0 <= d_t0_t2_t1

	d_t0_t2_t1_mem1 = S.Task('d_t0_t2_t1_mem1', length=1, delay_cost=1)
	d_t0_t2_t1_mem1 += MAS_MEM[3]
	S += 32 < d_t0_t2_t1_mem1
	S += d_t0_t2_t1_mem1 <= d_t0_t2_t1

	d_t0_t2_t2 = S.Task('d_t0_t2_t2', length=3, delay_cost=1)
	d_t0_t2_t2 += alt(MAS)
	d_t0_t2_t2_in = S.Task('d_t0_t2_t2_in', length=1, delay_cost=1)
	d_t0_t2_t2_in += alt(MAS_in)
	S += d_t0_t2_t2_in*MAS_in[0]<=d_t0_t2_t2*MAS[0]

	S += d_t0_t2_t2_in*MAS_in[1]<=d_t0_t2_t2*MAS[1]

	S += d_t0_t2_t2_in*MAS_in[2]<=d_t0_t2_t2*MAS[2]

	S += d_t0_t2_t2_in*MAS_in[3]<=d_t0_t2_t2*MAS[3]

	S += d_t0_t2_t2_in*MAS_in[4]<=d_t0_t2_t2*MAS[4]

	S += d_t0_t2_t2_in*MAS_in[5]<=d_t0_t2_t2*MAS[5]

	d_t0_t2_t2_mem0 = S.Task('d_t0_t2_t2_mem0', length=1, delay_cost=1)
	d_t0_t2_t2_mem0 += MAS_MEM[6]
	S += 100 < d_t0_t2_t2_mem0
	S += d_t0_t2_t2_mem0 <= d_t0_t2_t2

	d_t0_t2_t2_mem1 = S.Task('d_t0_t2_t2_mem1', length=1, delay_cost=1)
	d_t0_t2_t2_mem1 += MAS_MEM[11]
	S += 102 < d_t0_t2_t2_mem1
	S += d_t0_t2_t2_mem1 <= d_t0_t2_t2

	d_t0_t31 = S.Task('d_t0_t31', length=3, delay_cost=1)
	d_t0_t31 += alt(MAS)
	d_t0_t31_in = S.Task('d_t0_t31_in', length=1, delay_cost=1)
	d_t0_t31_in += alt(MAS_in)
	S += d_t0_t31_in*MAS_in[0]<=d_t0_t31*MAS[0]

	S += d_t0_t31_in*MAS_in[1]<=d_t0_t31*MAS[1]

	S += d_t0_t31_in*MAS_in[2]<=d_t0_t31*MAS[2]

	S += d_t0_t31_in*MAS_in[3]<=d_t0_t31*MAS[3]

	S += d_t0_t31_in*MAS_in[4]<=d_t0_t31*MAS[4]

	S += d_t0_t31_in*MAS_in[5]<=d_t0_t31*MAS[5]

	d_t0_t31_mem0 = S.Task('d_t0_t31_mem0', length=1, delay_cost=1)
	d_t0_t31_mem0 += MM_MEM[2]
	S += 31 < d_t0_t31_mem0
	S += d_t0_t31_mem0 <= d_t0_t31

	d_t0_t31_mem1 = S.Task('d_t0_t31_mem1', length=1, delay_cost=1)
	d_t0_t31_mem1 += MAS_MEM[7]
	S += 32 < d_t0_t31_mem1
	S += d_t0_t31_mem1 <= d_t0_t31

	d_t010 = S.Task('d_t010', length=3, delay_cost=1)
	d_t010 += alt(MAS)
	d_t010_in = S.Task('d_t010_in', length=1, delay_cost=1)
	d_t010_in += alt(MAS_in)
	S += d_t010_in*MAS_in[0]<=d_t010*MAS[0]

	S += d_t010_in*MAS_in[1]<=d_t010*MAS[1]

	S += d_t010_in*MAS_in[2]<=d_t010*MAS[2]

	S += d_t010_in*MAS_in[3]<=d_t010*MAS[3]

	S += d_t010_in*MAS_in[4]<=d_t010*MAS[4]

	S += d_t010_in*MAS_in[5]<=d_t010*MAS[5]

	d_t010_mem0 = S.Task('d_t010_mem0', length=1, delay_cost=1)
	d_t010_mem0 += MAS_MEM[8]
	S += 33 < d_t010_mem0
	S += d_t010_mem0 <= d_t010

	d_t010_mem1 = S.Task('d_t010_mem1', length=1, delay_cost=1)
	d_t010_mem1 += MAS_MEM[9]
	S += 33 < d_t010_mem1
	S += d_t010_mem1 <= d_t010

	d_t1_t2_t0 = S.Task('d_t1_t2_t0', length=11, delay_cost=1)
	d_t1_t2_t0 += alt(MM)
	d_t1_t2_t0_in = S.Task('d_t1_t2_t0_in', length=1, delay_cost=1)
	d_t1_t2_t0_in += alt(MM_in)
	S += d_t1_t2_t0_in*MM_in[0]<=d_t1_t2_t0*MM[0]
	S += d_t1_t2_t0_in*MM_in[1]<=d_t1_t2_t0*MM[1]
	d_t1_t2_t0_mem0 = S.Task('d_t1_t2_t0_mem0', length=1, delay_cost=1)
	d_t1_t2_t0_mem0 += MAS_MEM[8]
	S += 104 < d_t1_t2_t0_mem0
	S += d_t1_t2_t0_mem0 <= d_t1_t2_t0

	d_t1_t2_t0_mem1 = S.Task('d_t1_t2_t0_mem1', length=1, delay_cost=1)
	d_t1_t2_t0_mem1 += MAS_MEM[1]
	S += 19 < d_t1_t2_t0_mem1
	S += d_t1_t2_t0_mem1 <= d_t1_t2_t0

	d_t1_t2_t1 = S.Task('d_t1_t2_t1', length=11, delay_cost=1)
	d_t1_t2_t1 += alt(MM)
	d_t1_t2_t1_in = S.Task('d_t1_t2_t1_in', length=1, delay_cost=1)
	d_t1_t2_t1_in += alt(MM_in)
	S += d_t1_t2_t1_in*MM_in[0]<=d_t1_t2_t1*MM[0]
	S += d_t1_t2_t1_in*MM_in[1]<=d_t1_t2_t1*MM[1]
	d_t1_t2_t1_mem0 = S.Task('d_t1_t2_t1_mem0', length=1, delay_cost=1)
	d_t1_t2_t1_mem0 += MAS_MEM[6]
	S += 101 < d_t1_t2_t1_mem0
	S += d_t1_t2_t1_mem0 <= d_t1_t2_t1

	d_t1_t2_t1_mem1 = S.Task('d_t1_t2_t1_mem1', length=1, delay_cost=1)
	d_t1_t2_t1_mem1 += MAS_MEM[1]
	S += 22 < d_t1_t2_t1_mem1
	S += d_t1_t2_t1_mem1 <= d_t1_t2_t1

	d_t1_t2_t2 = S.Task('d_t1_t2_t2', length=3, delay_cost=1)
	d_t1_t2_t2 += alt(MAS)
	d_t1_t2_t2_in = S.Task('d_t1_t2_t2_in', length=1, delay_cost=1)
	d_t1_t2_t2_in += alt(MAS_in)
	S += d_t1_t2_t2_in*MAS_in[0]<=d_t1_t2_t2*MAS[0]

	S += d_t1_t2_t2_in*MAS_in[1]<=d_t1_t2_t2*MAS[1]

	S += d_t1_t2_t2_in*MAS_in[2]<=d_t1_t2_t2*MAS[2]

	S += d_t1_t2_t2_in*MAS_in[3]<=d_t1_t2_t2*MAS[3]

	S += d_t1_t2_t2_in*MAS_in[4]<=d_t1_t2_t2*MAS[4]

	S += d_t1_t2_t2_in*MAS_in[5]<=d_t1_t2_t2*MAS[5]

	d_t1_t2_t2_mem0 = S.Task('d_t1_t2_t2_mem0', length=1, delay_cost=1)
	d_t1_t2_t2_mem0 += MAS_MEM[8]
	S += 104 < d_t1_t2_t2_mem0
	S += d_t1_t2_t2_mem0 <= d_t1_t2_t2

	d_t1_t2_t2_mem1 = S.Task('d_t1_t2_t2_mem1', length=1, delay_cost=1)
	d_t1_t2_t2_mem1 += MAS_MEM[7]
	S += 101 < d_t1_t2_t2_mem1
	S += d_t1_t2_t2_mem1 <= d_t1_t2_t2

	d_t1_t31 = S.Task('d_t1_t31', length=3, delay_cost=1)
	d_t1_t31 += alt(MAS)
	d_t1_t31_in = S.Task('d_t1_t31_in', length=1, delay_cost=1)
	d_t1_t31_in += alt(MAS_in)
	S += d_t1_t31_in*MAS_in[0]<=d_t1_t31*MAS[0]

	S += d_t1_t31_in*MAS_in[1]<=d_t1_t31*MAS[1]

	S += d_t1_t31_in*MAS_in[2]<=d_t1_t31*MAS[2]

	S += d_t1_t31_in*MAS_in[3]<=d_t1_t31*MAS[3]

	S += d_t1_t31_in*MAS_in[4]<=d_t1_t31*MAS[4]

	S += d_t1_t31_in*MAS_in[5]<=d_t1_t31*MAS[5]

	d_t1_t31_mem0 = S.Task('d_t1_t31_mem0', length=1, delay_cost=1)
	d_t1_t31_mem0 += MM_MEM[0]
	S += 27 < d_t1_t31_mem0
	S += d_t1_t31_mem0 <= d_t1_t31

	d_t1_t31_mem1 = S.Task('d_t1_t31_mem1', length=1, delay_cost=1)
	d_t1_t31_mem1 += MAS_MEM[11]
	S += 39 < d_t1_t31_mem1
	S += d_t1_t31_mem1 <= d_t1_t31

	d_t110 = S.Task('d_t110', length=3, delay_cost=1)
	d_t110 += alt(MAS)
	d_t110_in = S.Task('d_t110_in', length=1, delay_cost=1)
	d_t110_in += alt(MAS_in)
	S += d_t110_in*MAS_in[0]<=d_t110*MAS[0]

	S += d_t110_in*MAS_in[1]<=d_t110*MAS[1]

	S += d_t110_in*MAS_in[2]<=d_t110*MAS[2]

	S += d_t110_in*MAS_in[3]<=d_t110*MAS[3]

	S += d_t110_in*MAS_in[4]<=d_t110*MAS[4]

	S += d_t110_in*MAS_in[5]<=d_t110*MAS[5]

	d_t110_mem0 = S.Task('d_t110_mem0', length=1, delay_cost=1)
	d_t110_mem0 += MAS_MEM[2]
	S += 37 < d_t110_mem0
	S += d_t110_mem0 <= d_t110

	d_t110_mem1 = S.Task('d_t110_mem1', length=1, delay_cost=1)
	d_t110_mem1 += MAS_MEM[3]
	S += 37 < d_t110_mem1
	S += d_t110_mem1 <= d_t110

	d_t2_t2_t0 = S.Task('d_t2_t2_t0', length=11, delay_cost=1)
	d_t2_t2_t0 += alt(MM)
	d_t2_t2_t0_in = S.Task('d_t2_t2_t0_in', length=1, delay_cost=1)
	d_t2_t2_t0_in += alt(MM_in)
	S += d_t2_t2_t0_in*MM_in[0]<=d_t2_t2_t0*MM[0]
	S += d_t2_t2_t0_in*MM_in[1]<=d_t2_t2_t0*MM[1]
	d_t2_t2_t0_mem0 = S.Task('d_t2_t2_t0_mem0', length=1, delay_cost=1)
	d_t2_t2_t0_mem0 += MAS_MEM[6]
	S += 103 < d_t2_t2_t0_mem0
	S += d_t2_t2_t0_mem0 <= d_t2_t2_t0

	d_t2_t2_t0_mem1 = S.Task('d_t2_t2_t0_mem1', length=1, delay_cost=1)
	d_t2_t2_t0_mem1 += MAS_MEM[1]
	S += 12 < d_t2_t2_t0_mem1
	S += d_t2_t2_t0_mem1 <= d_t2_t2_t0

	d_t2_t2_t1 = S.Task('d_t2_t2_t1', length=11, delay_cost=1)
	d_t2_t2_t1 += alt(MM)
	d_t2_t2_t1_in = S.Task('d_t2_t2_t1_in', length=1, delay_cost=1)
	d_t2_t2_t1_in += alt(MM_in)
	S += d_t2_t2_t1_in*MM_in[0]<=d_t2_t2_t1*MM[0]
	S += d_t2_t2_t1_in*MM_in[1]<=d_t2_t2_t1*MM[1]
	d_t2_t2_t1_mem0 = S.Task('d_t2_t2_t1_mem0', length=1, delay_cost=1)
	d_t2_t2_t1_mem0 += MAS_MEM[4]
	S += 99 < d_t2_t2_t1_mem0
	S += d_t2_t2_t1_mem0 <= d_t2_t2_t1

	d_t2_t2_t1_mem1 = S.Task('d_t2_t2_t1_mem1', length=1, delay_cost=1)
	d_t2_t2_t1_mem1 += MAS_MEM[1]
	S += 8 < d_t2_t2_t1_mem1
	S += d_t2_t2_t1_mem1 <= d_t2_t2_t1

	d_t2_t2_t2 = S.Task('d_t2_t2_t2', length=3, delay_cost=1)
	d_t2_t2_t2 += alt(MAS)
	d_t2_t2_t2_in = S.Task('d_t2_t2_t2_in', length=1, delay_cost=1)
	d_t2_t2_t2_in += alt(MAS_in)
	S += d_t2_t2_t2_in*MAS_in[0]<=d_t2_t2_t2*MAS[0]

	S += d_t2_t2_t2_in*MAS_in[1]<=d_t2_t2_t2*MAS[1]

	S += d_t2_t2_t2_in*MAS_in[2]<=d_t2_t2_t2*MAS[2]

	S += d_t2_t2_t2_in*MAS_in[3]<=d_t2_t2_t2*MAS[3]

	S += d_t2_t2_t2_in*MAS_in[4]<=d_t2_t2_t2*MAS[4]

	S += d_t2_t2_t2_in*MAS_in[5]<=d_t2_t2_t2*MAS[5]

	d_t2_t2_t2_mem0 = S.Task('d_t2_t2_t2_mem0', length=1, delay_cost=1)
	d_t2_t2_t2_mem0 += MAS_MEM[6]
	S += 103 < d_t2_t2_t2_mem0
	S += d_t2_t2_t2_mem0 <= d_t2_t2_t2

	d_t2_t2_t2_mem1 = S.Task('d_t2_t2_t2_mem1', length=1, delay_cost=1)
	d_t2_t2_t2_mem1 += MAS_MEM[5]
	S += 99 < d_t2_t2_t2_mem1
	S += d_t2_t2_t2_mem1 <= d_t2_t2_t2

	d_t2_t31 = S.Task('d_t2_t31', length=3, delay_cost=1)
	d_t2_t31 += alt(MAS)
	d_t2_t31_in = S.Task('d_t2_t31_in', length=1, delay_cost=1)
	d_t2_t31_in += alt(MAS_in)
	S += d_t2_t31_in*MAS_in[0]<=d_t2_t31*MAS[0]

	S += d_t2_t31_in*MAS_in[1]<=d_t2_t31*MAS[1]

	S += d_t2_t31_in*MAS_in[2]<=d_t2_t31*MAS[2]

	S += d_t2_t31_in*MAS_in[3]<=d_t2_t31*MAS[3]

	S += d_t2_t31_in*MAS_in[4]<=d_t2_t31*MAS[4]

	S += d_t2_t31_in*MAS_in[5]<=d_t2_t31*MAS[5]

	d_t2_t31_mem0 = S.Task('d_t2_t31_mem0', length=1, delay_cost=1)
	d_t2_t31_mem0 += MM_MEM[0]
	S += 28 < d_t2_t31_mem0
	S += d_t2_t31_mem0 <= d_t2_t31

	d_t2_t31_mem1 = S.Task('d_t2_t31_mem1', length=1, delay_cost=1)
	d_t2_t31_mem1 += MAS_MEM[3]
	S += 38 < d_t2_t31_mem1
	S += d_t2_t31_mem1 <= d_t2_t31

	d_t210 = S.Task('d_t210', length=3, delay_cost=1)
	d_t210 += alt(MAS)
	d_t210_in = S.Task('d_t210_in', length=1, delay_cost=1)
	d_t210_in += alt(MAS_in)
	S += d_t210_in*MAS_in[0]<=d_t210*MAS[0]

	S += d_t210_in*MAS_in[1]<=d_t210*MAS[1]

	S += d_t210_in*MAS_in[2]<=d_t210*MAS[2]

	S += d_t210_in*MAS_in[3]<=d_t210*MAS[3]

	S += d_t210_in*MAS_in[4]<=d_t210*MAS[4]

	S += d_t210_in*MAS_in[5]<=d_t210*MAS[5]

	d_t210_mem0 = S.Task('d_t210_mem0', length=1, delay_cost=1)
	d_t210_mem0 += MAS_MEM[8]
	S += 40 < d_t210_mem0
	S += d_t210_mem0 <= d_t210

	d_t210_mem1 = S.Task('d_t210_mem1', length=1, delay_cost=1)
	d_t210_mem1 += MAS_MEM[9]
	S += 40 < d_t210_mem1
	S += d_t210_mem1 <= d_t210

	d_t3_t00 = S.Task('d_t3_t00', length=3, delay_cost=1)
	d_t3_t00 += alt(MAS)
	d_t3_t00_in = S.Task('d_t3_t00_in', length=1, delay_cost=1)
	d_t3_t00_in += alt(MAS_in)
	S += d_t3_t00_in*MAS_in[0]<=d_t3_t00*MAS[0]

	S += d_t3_t00_in*MAS_in[1]<=d_t3_t00*MAS[1]

	S += d_t3_t00_in*MAS_in[2]<=d_t3_t00*MAS[2]

	S += d_t3_t00_in*MAS_in[3]<=d_t3_t00*MAS[3]

	S += d_t3_t00_in*MAS_in[4]<=d_t3_t00*MAS[4]

	S += d_t3_t00_in*MAS_in[5]<=d_t3_t00*MAS[5]

	d_t3_t00_mem0 = S.Task('d_t3_t00_mem0', length=1, delay_cost=1)
	d_t3_t00_mem0 += MAS_MEM[0]
	S += 28 < d_t3_t00_mem0
	S += d_t3_t00_mem0 <= d_t3_t00

	d_t3_t00_mem1 = S.Task('d_t3_t00_mem1', length=1, delay_cost=1)
	d_t3_t00_mem1 += MAS_MEM[11]
	S += 21 < d_t3_t00_mem1
	S += d_t3_t00_mem1 <= d_t3_t00

	d_t3_t01 = S.Task('d_t3_t01', length=3, delay_cost=1)
	d_t3_t01 += alt(MAS)
	d_t3_t01_in = S.Task('d_t3_t01_in', length=1, delay_cost=1)
	d_t3_t01_in += alt(MAS_in)
	S += d_t3_t01_in*MAS_in[0]<=d_t3_t01*MAS[0]

	S += d_t3_t01_in*MAS_in[1]<=d_t3_t01*MAS[1]

	S += d_t3_t01_in*MAS_in[2]<=d_t3_t01*MAS[2]

	S += d_t3_t01_in*MAS_in[3]<=d_t3_t01*MAS[3]

	S += d_t3_t01_in*MAS_in[4]<=d_t3_t01*MAS[4]

	S += d_t3_t01_in*MAS_in[5]<=d_t3_t01*MAS[5]

	d_t3_t01_mem0 = S.Task('d_t3_t01_mem0', length=1, delay_cost=1)
	d_t3_t01_mem0 += MAS_MEM[0]
	S += 7 < d_t3_t01_mem0
	S += d_t3_t01_mem0 <= d_t3_t01

	d_t3_t01_mem1 = S.Task('d_t3_t01_mem1', length=1, delay_cost=1)
	d_t3_t01_mem1 += MAS_MEM[3]
	S += 22 < d_t3_t01_mem1
	S += d_t3_t01_mem1 <= d_t3_t01

	d_t3_t2_t3 = S.Task('d_t3_t2_t3', length=3, delay_cost=1)
	d_t3_t2_t3 += alt(MAS)
	d_t3_t2_t3_in = S.Task('d_t3_t2_t3_in', length=1, delay_cost=1)
	d_t3_t2_t3_in += alt(MAS_in)
	S += d_t3_t2_t3_in*MAS_in[0]<=d_t3_t2_t3*MAS[0]

	S += d_t3_t2_t3_in*MAS_in[1]<=d_t3_t2_t3*MAS[1]

	S += d_t3_t2_t3_in*MAS_in[2]<=d_t3_t2_t3*MAS[2]

	S += d_t3_t2_t3_in*MAS_in[3]<=d_t3_t2_t3*MAS[3]

	S += d_t3_t2_t3_in*MAS_in[4]<=d_t3_t2_t3*MAS[4]

	S += d_t3_t2_t3_in*MAS_in[5]<=d_t3_t2_t3*MAS[5]

	d_t3_t2_t3_mem0 = S.Task('d_t3_t2_t3_mem0', length=1, delay_cost=1)
	d_t3_t2_t3_mem0 += MAS_MEM[0]
	S += 31 < d_t3_t2_t3_mem0
	S += d_t3_t2_t3_mem0 <= d_t3_t2_t3

	d_t3_t2_t3_mem1 = S.Task('d_t3_t2_t3_mem1', length=1, delay_cost=1)
	d_t3_t2_t3_mem1 += MAS_MEM[11]
	S += 18 < d_t3_t2_t3_mem1
	S += d_t3_t2_t3_mem1 <= d_t3_t2_t3

	d_t3_t3_t4 = S.Task('d_t3_t3_t4', length=11, delay_cost=1)
	d_t3_t3_t4 += alt(MM)
	d_t3_t3_t4_in = S.Task('d_t3_t3_t4_in', length=1, delay_cost=1)
	d_t3_t3_t4_in += alt(MM_in)
	S += d_t3_t3_t4_in*MM_in[0]<=d_t3_t3_t4*MM[0]
	S += d_t3_t3_t4_in*MM_in[1]<=d_t3_t3_t4*MM[1]
	d_t3_t3_t4_mem0 = S.Task('d_t3_t3_t4_mem0', length=1, delay_cost=1)
	d_t3_t3_t4_mem0 += MAS_MEM[4]
	S += 32 < d_t3_t3_t4_mem0
	S += d_t3_t3_t4_mem0 <= d_t3_t3_t4

	d_t3_t3_t4_mem1 = S.Task('d_t3_t3_t4_mem1', length=1, delay_cost=1)
	d_t3_t3_t4_mem1 += MAS_MEM[3]
	S += 24 < d_t3_t3_t4_mem1
	S += d_t3_t3_t4_mem1 <= d_t3_t3_t4

	d_t3_t30 = S.Task('d_t3_t30', length=3, delay_cost=1)
	d_t3_t30 += alt(MAS)
	d_t3_t30_in = S.Task('d_t3_t30_in', length=1, delay_cost=1)
	d_t3_t30_in += alt(MAS_in)
	S += d_t3_t30_in*MAS_in[0]<=d_t3_t30*MAS[0]

	S += d_t3_t30_in*MAS_in[1]<=d_t3_t30*MAS[1]

	S += d_t3_t30_in*MAS_in[2]<=d_t3_t30*MAS[2]

	S += d_t3_t30_in*MAS_in[3]<=d_t3_t30*MAS[3]

	S += d_t3_t30_in*MAS_in[4]<=d_t3_t30*MAS[4]

	S += d_t3_t30_in*MAS_in[5]<=d_t3_t30*MAS[5]

	d_t3_t30_mem0 = S.Task('d_t3_t30_mem0', length=1, delay_cost=1)
	d_t3_t30_mem0 += MM_MEM[0]
	S += 42 < d_t3_t30_mem0
	S += d_t3_t30_mem0 <= d_t3_t30

	d_t3_t30_mem1 = S.Task('d_t3_t30_mem1', length=1, delay_cost=1)
	d_t3_t30_mem1 += MM_MEM[1]
	S += 25 < d_t3_t30_mem1
	S += d_t3_t30_mem1 <= d_t3_t30

	d_t3_t3_t5 = S.Task('d_t3_t3_t5', length=3, delay_cost=1)
	d_t3_t3_t5 += alt(MAS)
	d_t3_t3_t5_in = S.Task('d_t3_t3_t5_in', length=1, delay_cost=1)
	d_t3_t3_t5_in += alt(MAS_in)
	S += d_t3_t3_t5_in*MAS_in[0]<=d_t3_t3_t5*MAS[0]

	S += d_t3_t3_t5_in*MAS_in[1]<=d_t3_t3_t5*MAS[1]

	S += d_t3_t3_t5_in*MAS_in[2]<=d_t3_t3_t5*MAS[2]

	S += d_t3_t3_t5_in*MAS_in[3]<=d_t3_t3_t5*MAS[3]

	S += d_t3_t3_t5_in*MAS_in[4]<=d_t3_t3_t5*MAS[4]

	S += d_t3_t3_t5_in*MAS_in[5]<=d_t3_t3_t5*MAS[5]

	d_t3_t3_t5_mem0 = S.Task('d_t3_t3_t5_mem0', length=1, delay_cost=1)
	d_t3_t3_t5_mem0 += MM_MEM[0]
	S += 42 < d_t3_t3_t5_mem0
	S += d_t3_t3_t5_mem0 <= d_t3_t3_t5

	d_t3_t3_t5_mem1 = S.Task('d_t3_t3_t5_mem1', length=1, delay_cost=1)
	d_t3_t3_t5_mem1 += MM_MEM[1]
	S += 25 < d_t3_t3_t5_mem1
	S += d_t3_t3_t5_mem1 <= d_t3_t3_t5

	d_t4_t00 = S.Task('d_t4_t00', length=3, delay_cost=1)
	d_t4_t00 += alt(MAS)
	d_t4_t00_in = S.Task('d_t4_t00_in', length=1, delay_cost=1)
	d_t4_t00_in += alt(MAS_in)
	S += d_t4_t00_in*MAS_in[0]<=d_t4_t00*MAS[0]

	S += d_t4_t00_in*MAS_in[1]<=d_t4_t00*MAS[1]

	S += d_t4_t00_in*MAS_in[2]<=d_t4_t00*MAS[2]

	S += d_t4_t00_in*MAS_in[3]<=d_t4_t00*MAS[3]

	S += d_t4_t00_in*MAS_in[4]<=d_t4_t00*MAS[4]

	S += d_t4_t00_in*MAS_in[5]<=d_t4_t00*MAS[5]

	d_t4_t00_mem0 = S.Task('d_t4_t00_mem0', length=1, delay_cost=1)
	d_t4_t00_mem0 += MAS_MEM[8]
	S += 30 < d_t4_t00_mem0
	S += d_t4_t00_mem0 <= d_t4_t00

	d_t4_t00_mem1 = S.Task('d_t4_t00_mem1', length=1, delay_cost=1)
	d_t4_t00_mem1 += MAS_MEM[9]
	S += 43 < d_t4_t00_mem1
	S += d_t4_t00_mem1 <= d_t4_t00

	d_t4_t01 = S.Task('d_t4_t01', length=3, delay_cost=1)
	d_t4_t01 += alt(MAS)
	d_t4_t01_in = S.Task('d_t4_t01_in', length=1, delay_cost=1)
	d_t4_t01_in += alt(MAS_in)
	S += d_t4_t01_in*MAS_in[0]<=d_t4_t01*MAS[0]

	S += d_t4_t01_in*MAS_in[1]<=d_t4_t01*MAS[1]

	S += d_t4_t01_in*MAS_in[2]<=d_t4_t01*MAS[2]

	S += d_t4_t01_in*MAS_in[3]<=d_t4_t01*MAS[3]

	S += d_t4_t01_in*MAS_in[4]<=d_t4_t01*MAS[4]

	S += d_t4_t01_in*MAS_in[5]<=d_t4_t01*MAS[5]

	d_t4_t01_mem0 = S.Task('d_t4_t01_mem0', length=1, delay_cost=1)
	d_t4_t01_mem0 += MAS_MEM[0]
	S += 29 < d_t4_t01_mem0
	S += d_t4_t01_mem0 <= d_t4_t01

	d_t4_t01_mem1 = S.Task('d_t4_t01_mem1', length=1, delay_cost=1)
	d_t4_t01_mem1 += MAS_MEM[3]
	S += 43 < d_t4_t01_mem1
	S += d_t4_t01_mem1 <= d_t4_t01

	d_t4_t2_t3 = S.Task('d_t4_t2_t3', length=3, delay_cost=1)
	d_t4_t2_t3 += alt(MAS)
	d_t4_t2_t3_in = S.Task('d_t4_t2_t3_in', length=1, delay_cost=1)
	d_t4_t2_t3_in += alt(MAS_in)
	S += d_t4_t2_t3_in*MAS_in[0]<=d_t4_t2_t3*MAS[0]

	S += d_t4_t2_t3_in*MAS_in[1]<=d_t4_t2_t3*MAS[1]

	S += d_t4_t2_t3_in*MAS_in[2]<=d_t4_t2_t3*MAS[2]

	S += d_t4_t2_t3_in*MAS_in[3]<=d_t4_t2_t3*MAS[3]

	S += d_t4_t2_t3_in*MAS_in[4]<=d_t4_t2_t3*MAS[4]

	S += d_t4_t2_t3_in*MAS_in[5]<=d_t4_t2_t3*MAS[5]

	d_t4_t2_t3_mem0 = S.Task('d_t4_t2_t3_mem0', length=1, delay_cost=1)
	d_t4_t2_t3_mem0 += MAS_MEM[6]
	S += 37 < d_t4_t2_t3_mem0
	S += d_t4_t2_t3_mem0 <= d_t4_t2_t3

	d_t4_t2_t3_mem1 = S.Task('d_t4_t2_t3_mem1', length=1, delay_cost=1)
	d_t4_t2_t3_mem1 += MAS_MEM[3]
	S += 44 < d_t4_t2_t3_mem1
	S += d_t4_t2_t3_mem1 <= d_t4_t2_t3

	d_t4_t3_t4 = S.Task('d_t4_t3_t4', length=11, delay_cost=1)
	d_t4_t3_t4 += alt(MM)
	d_t4_t3_t4_in = S.Task('d_t4_t3_t4_in', length=1, delay_cost=1)
	d_t4_t3_t4_in += alt(MM_in)
	S += d_t4_t3_t4_in*MM_in[0]<=d_t4_t3_t4*MM[0]
	S += d_t4_t3_t4_in*MM_in[1]<=d_t4_t3_t4*MM[1]
	d_t4_t3_t4_mem0 = S.Task('d_t4_t3_t4_mem0', length=1, delay_cost=1)
	d_t4_t3_t4_mem0 += MAS_MEM[6]
	S += 33 < d_t4_t3_t4_mem0
	S += d_t4_t3_t4_mem0 <= d_t4_t3_t4

	d_t4_t3_t4_mem1 = S.Task('d_t4_t3_t4_mem1', length=1, delay_cost=1)
	d_t4_t3_t4_mem1 += MAS_MEM[11]
	S += 45 < d_t4_t3_t4_mem1
	S += d_t4_t3_t4_mem1 <= d_t4_t3_t4

	d_t4_t30 = S.Task('d_t4_t30', length=3, delay_cost=1)
	d_t4_t30 += alt(MAS)
	d_t4_t30_in = S.Task('d_t4_t30_in', length=1, delay_cost=1)
	d_t4_t30_in += alt(MAS_in)
	S += d_t4_t30_in*MAS_in[0]<=d_t4_t30*MAS[0]

	S += d_t4_t30_in*MAS_in[1]<=d_t4_t30*MAS[1]

	S += d_t4_t30_in*MAS_in[2]<=d_t4_t30*MAS[2]

	S += d_t4_t30_in*MAS_in[3]<=d_t4_t30*MAS[3]

	S += d_t4_t30_in*MAS_in[4]<=d_t4_t30*MAS[4]

	S += d_t4_t30_in*MAS_in[5]<=d_t4_t30*MAS[5]

	d_t4_t30_mem0 = S.Task('d_t4_t30_mem0', length=1, delay_cost=1)
	d_t4_t30_mem0 += MM_MEM[2]
	S += 46 < d_t4_t30_mem0
	S += d_t4_t30_mem0 <= d_t4_t30

	d_t4_t30_mem1 = S.Task('d_t4_t30_mem1', length=1, delay_cost=1)
	d_t4_t30_mem1 += MM_MEM[1]
	S += 54 < d_t4_t30_mem1
	S += d_t4_t30_mem1 <= d_t4_t30

	d_t4_t3_t5 = S.Task('d_t4_t3_t5', length=3, delay_cost=1)
	d_t4_t3_t5 += alt(MAS)
	d_t4_t3_t5_in = S.Task('d_t4_t3_t5_in', length=1, delay_cost=1)
	d_t4_t3_t5_in += alt(MAS_in)
	S += d_t4_t3_t5_in*MAS_in[0]<=d_t4_t3_t5*MAS[0]

	S += d_t4_t3_t5_in*MAS_in[1]<=d_t4_t3_t5*MAS[1]

	S += d_t4_t3_t5_in*MAS_in[2]<=d_t4_t3_t5*MAS[2]

	S += d_t4_t3_t5_in*MAS_in[3]<=d_t4_t3_t5*MAS[3]

	S += d_t4_t3_t5_in*MAS_in[4]<=d_t4_t3_t5*MAS[4]

	S += d_t4_t3_t5_in*MAS_in[5]<=d_t4_t3_t5*MAS[5]

	d_t4_t3_t5_mem0 = S.Task('d_t4_t3_t5_mem0', length=1, delay_cost=1)
	d_t4_t3_t5_mem0 += MM_MEM[2]
	S += 46 < d_t4_t3_t5_mem0
	S += d_t4_t3_t5_mem0 <= d_t4_t3_t5

	d_t4_t3_t5_mem1 = S.Task('d_t4_t3_t5_mem1', length=1, delay_cost=1)
	d_t4_t3_t5_mem1 += MM_MEM[1]
	S += 54 < d_t4_t3_t5_mem1
	S += d_t4_t3_t5_mem1 <= d_t4_t3_t5

	d_t5_t00 = S.Task('d_t5_t00', length=3, delay_cost=1)
	d_t5_t00 += alt(MAS)
	d_t5_t00_in = S.Task('d_t5_t00_in', length=1, delay_cost=1)
	d_t5_t00_in += alt(MAS_in)
	S += d_t5_t00_in*MAS_in[0]<=d_t5_t00*MAS[0]

	S += d_t5_t00_in*MAS_in[1]<=d_t5_t00*MAS[1]

	S += d_t5_t00_in*MAS_in[2]<=d_t5_t00*MAS[2]

	S += d_t5_t00_in*MAS_in[3]<=d_t5_t00*MAS[3]

	S += d_t5_t00_in*MAS_in[4]<=d_t5_t00*MAS[4]

	S += d_t5_t00_in*MAS_in[5]<=d_t5_t00*MAS[5]

	d_t5_t00_mem0 = S.Task('d_t5_t00_mem0', length=1, delay_cost=1)
	d_t5_t00_mem0 += MAS_MEM[2]
	S += 52 < d_t5_t00_mem0
	S += d_t5_t00_mem0 <= d_t5_t00

	d_t5_t00_mem1 = S.Task('d_t5_t00_mem1', length=1, delay_cost=1)
	d_t5_t00_mem1 += MAS_MEM[5]
	S += 62 < d_t5_t00_mem1
	S += d_t5_t00_mem1 <= d_t5_t00

	d_t5_t01 = S.Task('d_t5_t01', length=3, delay_cost=1)
	d_t5_t01 += alt(MAS)
	d_t5_t01_in = S.Task('d_t5_t01_in', length=1, delay_cost=1)
	d_t5_t01_in += alt(MAS_in)
	S += d_t5_t01_in*MAS_in[0]<=d_t5_t01*MAS[0]

	S += d_t5_t01_in*MAS_in[1]<=d_t5_t01*MAS[1]

	S += d_t5_t01_in*MAS_in[2]<=d_t5_t01*MAS[2]

	S += d_t5_t01_in*MAS_in[3]<=d_t5_t01*MAS[3]

	S += d_t5_t01_in*MAS_in[4]<=d_t5_t01*MAS[4]

	S += d_t5_t01_in*MAS_in[5]<=d_t5_t01*MAS[5]

	d_t5_t01_mem0 = S.Task('d_t5_t01_mem0', length=1, delay_cost=1)
	d_t5_t01_mem0 += MAS_MEM[0]
	S += 62 < d_t5_t01_mem0
	S += d_t5_t01_mem0 <= d_t5_t01

	d_t5_t01_mem1 = S.Task('d_t5_t01_mem1', length=1, delay_cost=1)
	d_t5_t01_mem1 += MAS_MEM[9]
	S += 62 < d_t5_t01_mem1
	S += d_t5_t01_mem1 <= d_t5_t01

	d_t5_t2_t3 = S.Task('d_t5_t2_t3', length=3, delay_cost=1)
	d_t5_t2_t3 += alt(MAS)
	d_t5_t2_t3_in = S.Task('d_t5_t2_t3_in', length=1, delay_cost=1)
	d_t5_t2_t3_in += alt(MAS_in)
	S += d_t5_t2_t3_in*MAS_in[0]<=d_t5_t2_t3*MAS[0]

	S += d_t5_t2_t3_in*MAS_in[1]<=d_t5_t2_t3*MAS[1]

	S += d_t5_t2_t3_in*MAS_in[2]<=d_t5_t2_t3*MAS[2]

	S += d_t5_t2_t3_in*MAS_in[3]<=d_t5_t2_t3*MAS[3]

	S += d_t5_t2_t3_in*MAS_in[4]<=d_t5_t2_t3*MAS[4]

	S += d_t5_t2_t3_in*MAS_in[5]<=d_t5_t2_t3*MAS[5]

	d_t5_t2_t3_mem0 = S.Task('d_t5_t2_t3_mem0', length=1, delay_cost=1)
	d_t5_t2_t3_mem0 += MAS_MEM[6]
	S += 59 < d_t5_t2_t3_mem0
	S += d_t5_t2_t3_mem0 <= d_t5_t2_t3

	d_t5_t2_t3_mem1 = S.Task('d_t5_t2_t3_mem1', length=1, delay_cost=1)
	d_t5_t2_t3_mem1 += MAS_MEM[11]
	S += 65 < d_t5_t2_t3_mem1
	S += d_t5_t2_t3_mem1 <= d_t5_t2_t3

	d_t5_t3_t4 = S.Task('d_t5_t3_t4', length=11, delay_cost=1)
	d_t5_t3_t4 += alt(MM)
	d_t5_t3_t4_in = S.Task('d_t5_t3_t4_in', length=1, delay_cost=1)
	d_t5_t3_t4_in += alt(MM_in)
	S += d_t5_t3_t4_in*MM_in[0]<=d_t5_t3_t4*MM[0]
	S += d_t5_t3_t4_in*MM_in[1]<=d_t5_t3_t4*MM[1]
	d_t5_t3_t4_mem0 = S.Task('d_t5_t3_t4_mem0', length=1, delay_cost=1)
	d_t5_t3_t4_mem0 += MAS_MEM[8]
	S += 65 < d_t5_t3_t4_mem0
	S += d_t5_t3_t4_mem0 <= d_t5_t3_t4

	d_t5_t3_t4_mem1 = S.Task('d_t5_t3_t4_mem1', length=1, delay_cost=1)
	d_t5_t3_t4_mem1 += MAS_MEM[5]
	S += 63 < d_t5_t3_t4_mem1
	S += d_t5_t3_t4_mem1 <= d_t5_t3_t4

	d_t5_t30 = S.Task('d_t5_t30', length=3, delay_cost=1)
	d_t5_t30 += alt(MAS)
	d_t5_t30_in = S.Task('d_t5_t30_in', length=1, delay_cost=1)
	d_t5_t30_in += alt(MAS_in)
	S += d_t5_t30_in*MAS_in[0]<=d_t5_t30*MAS[0]

	S += d_t5_t30_in*MAS_in[1]<=d_t5_t30*MAS[1]

	S += d_t5_t30_in*MAS_in[2]<=d_t5_t30*MAS[2]

	S += d_t5_t30_in*MAS_in[3]<=d_t5_t30*MAS[3]

	S += d_t5_t30_in*MAS_in[4]<=d_t5_t30*MAS[4]

	S += d_t5_t30_in*MAS_in[5]<=d_t5_t30*MAS[5]

	d_t5_t30_mem0 = S.Task('d_t5_t30_mem0', length=1, delay_cost=1)
	d_t5_t30_mem0 += MM_MEM[0]
	S += 66 < d_t5_t30_mem0
	S += d_t5_t30_mem0 <= d_t5_t30

	d_t5_t30_mem1 = S.Task('d_t5_t30_mem1', length=1, delay_cost=1)
	d_t5_t30_mem1 += MM_MEM[1]
	S += 74 < d_t5_t30_mem1
	S += d_t5_t30_mem1 <= d_t5_t30

	d_t5_t3_t5 = S.Task('d_t5_t3_t5', length=3, delay_cost=1)
	d_t5_t3_t5 += alt(MAS)
	d_t5_t3_t5_in = S.Task('d_t5_t3_t5_in', length=1, delay_cost=1)
	d_t5_t3_t5_in += alt(MAS_in)
	S += d_t5_t3_t5_in*MAS_in[0]<=d_t5_t3_t5*MAS[0]

	S += d_t5_t3_t5_in*MAS_in[1]<=d_t5_t3_t5*MAS[1]

	S += d_t5_t3_t5_in*MAS_in[2]<=d_t5_t3_t5*MAS[2]

	S += d_t5_t3_t5_in*MAS_in[3]<=d_t5_t3_t5*MAS[3]

	S += d_t5_t3_t5_in*MAS_in[4]<=d_t5_t3_t5*MAS[4]

	S += d_t5_t3_t5_in*MAS_in[5]<=d_t5_t3_t5*MAS[5]

	d_t5_t3_t5_mem0 = S.Task('d_t5_t3_t5_mem0', length=1, delay_cost=1)
	d_t5_t3_t5_mem0 += MM_MEM[0]
	S += 66 < d_t5_t3_t5_mem0
	S += d_t5_t3_t5_mem0 <= d_t5_t3_t5

	d_t5_t3_t5_mem1 = S.Task('d_t5_t3_t5_mem1', length=1, delay_cost=1)
	d_t5_t3_t5_mem1 += MM_MEM[1]
	S += 74 < d_t5_t3_t5_mem1
	S += d_t5_t3_t5_mem1 <= d_t5_t3_t5

	c_t0_t01 = S.Task('c_t0_t01', length=3, delay_cost=1)
	c_t0_t01 += alt(MAS)
	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	c_t0_t01_in += alt(MAS_in)
	S += c_t0_t01_in*MAS_in[0]<=c_t0_t01*MAS[0]

	S += c_t0_t01_in*MAS_in[1]<=c_t0_t01*MAS[1]

	S += c_t0_t01_in*MAS_in[2]<=c_t0_t01*MAS[2]

	S += c_t0_t01_in*MAS_in[3]<=c_t0_t01*MAS[3]

	S += c_t0_t01_in*MAS_in[4]<=c_t0_t01*MAS[4]

	S += c_t0_t01_in*MAS_in[5]<=c_t0_t01*MAS[5]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	c_t0_t01_mem0 += MM_MEM[2]
	S += 64 < c_t0_t01_mem0
	S += c_t0_t01_mem0 <= c_t0_t01

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	c_t0_t01_mem1 += MAS_MEM[7]
	S += 71 < c_t0_t01_mem1
	S += c_t0_t01_mem1 <= c_t0_t01

	c_t0_t11 = S.Task('c_t0_t11', length=3, delay_cost=1)
	c_t0_t11 += alt(MAS)
	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	c_t0_t11_in += alt(MAS_in)
	S += c_t0_t11_in*MAS_in[0]<=c_t0_t11*MAS[0]

	S += c_t0_t11_in*MAS_in[1]<=c_t0_t11*MAS[1]

	S += c_t0_t11_in*MAS_in[2]<=c_t0_t11*MAS[2]

	S += c_t0_t11_in*MAS_in[3]<=c_t0_t11*MAS[3]

	S += c_t0_t11_in*MAS_in[4]<=c_t0_t11*MAS[4]

	S += c_t0_t11_in*MAS_in[5]<=c_t0_t11*MAS[5]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	c_t0_t11_mem0 += MM_MEM[2]
	S += 68 < c_t0_t11_mem0
	S += c_t0_t11_mem0 <= c_t0_t11

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	c_t0_t11_mem1 += MAS_MEM[5]
	S += 65 < c_t0_t11_mem1
	S += c_t0_t11_mem1 <= c_t0_t11

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=11, delay_cost=1)
	c_t0_t4_t4 += alt(MM)
	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	c_t0_t4_t4_in += alt(MM_in)
	S += c_t0_t4_t4_in*MM_in[0]<=c_t0_t4_t4*MM[0]
	S += c_t0_t4_t4_in*MM_in[1]<=c_t0_t4_t4*MM[1]
	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	c_t0_t4_t4_mem0 += MAS_MEM[8]
	S += 61 < c_t0_t4_t4_mem0
	S += c_t0_t4_t4_mem0 <= c_t0_t4_t4

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	c_t0_t4_t4_mem1 += MAS_MEM[3]
	S += 50 < c_t0_t4_t4_mem1
	S += c_t0_t4_t4_mem1 <= c_t0_t4_t4

	c_t0_t40 = S.Task('c_t0_t40', length=3, delay_cost=1)
	c_t0_t40 += alt(MAS)
	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	c_t0_t40_in += alt(MAS_in)
	S += c_t0_t40_in*MAS_in[0]<=c_t0_t40*MAS[0]

	S += c_t0_t40_in*MAS_in[1]<=c_t0_t40*MAS[1]

	S += c_t0_t40_in*MAS_in[2]<=c_t0_t40*MAS[2]

	S += c_t0_t40_in*MAS_in[3]<=c_t0_t40*MAS[3]

	S += c_t0_t40_in*MAS_in[4]<=c_t0_t40*MAS[4]

	S += c_t0_t40_in*MAS_in[5]<=c_t0_t40*MAS[5]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	c_t0_t40_mem0 += MM_MEM[0]
	S += 67 < c_t0_t40_mem0
	S += c_t0_t40_mem0 <= c_t0_t40

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	c_t0_t40_mem1 += MM_MEM[3]
	S += 56 < c_t0_t40_mem1
	S += c_t0_t40_mem1 <= c_t0_t40

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=3, delay_cost=1)
	c_t0_t4_t5 += alt(MAS)
	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	c_t0_t4_t5_in += alt(MAS_in)
	S += c_t0_t4_t5_in*MAS_in[0]<=c_t0_t4_t5*MAS[0]

	S += c_t0_t4_t5_in*MAS_in[1]<=c_t0_t4_t5*MAS[1]

	S += c_t0_t4_t5_in*MAS_in[2]<=c_t0_t4_t5*MAS[2]

	S += c_t0_t4_t5_in*MAS_in[3]<=c_t0_t4_t5*MAS[3]

	S += c_t0_t4_t5_in*MAS_in[4]<=c_t0_t4_t5*MAS[4]

	S += c_t0_t4_t5_in*MAS_in[5]<=c_t0_t4_t5*MAS[5]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	c_t0_t4_t5_mem0 += MM_MEM[0]
	S += 67 < c_t0_t4_t5_mem0
	S += c_t0_t4_t5_mem0 <= c_t0_t4_t5

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	c_t0_t4_t5_mem1 += MM_MEM[3]
	S += 56 < c_t0_t4_t5_mem1
	S += c_t0_t4_t5_mem1 <= c_t0_t4_t5

	c_t0_t50 = S.Task('c_t0_t50', length=3, delay_cost=1)
	c_t0_t50 += alt(MAS)
	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	c_t0_t50_in += alt(MAS_in)
	S += c_t0_t50_in*MAS_in[0]<=c_t0_t50*MAS[0]

	S += c_t0_t50_in*MAS_in[1]<=c_t0_t50*MAS[1]

	S += c_t0_t50_in*MAS_in[2]<=c_t0_t50*MAS[2]

	S += c_t0_t50_in*MAS_in[3]<=c_t0_t50*MAS[3]

	S += c_t0_t50_in*MAS_in[4]<=c_t0_t50*MAS[4]

	S += c_t0_t50_in*MAS_in[5]<=c_t0_t50*MAS[5]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	c_t0_t50_mem0 += MAS_MEM[2]
	S += 72 < c_t0_t50_mem0
	S += c_t0_t50_mem0 <= c_t0_t50

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	c_t0_t50_mem1 += MAS_MEM[3]
	S += 66 < c_t0_t50_mem1
	S += c_t0_t50_mem1 <= c_t0_t50

	c_t1_t01 = S.Task('c_t1_t01', length=3, delay_cost=1)
	c_t1_t01 += alt(MAS)
	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	c_t1_t01_in += alt(MAS_in)
	S += c_t1_t01_in*MAS_in[0]<=c_t1_t01*MAS[0]

	S += c_t1_t01_in*MAS_in[1]<=c_t1_t01*MAS[1]

	S += c_t1_t01_in*MAS_in[2]<=c_t1_t01*MAS[2]

	S += c_t1_t01_in*MAS_in[3]<=c_t1_t01*MAS[3]

	S += c_t1_t01_in*MAS_in[4]<=c_t1_t01*MAS[4]

	S += c_t1_t01_in*MAS_in[5]<=c_t1_t01*MAS[5]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	c_t1_t01_mem0 += MM_MEM[0]
	S += 72 < c_t1_t01_mem0
	S += c_t1_t01_mem0 <= c_t1_t01

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	c_t1_t01_mem1 += MAS_MEM[3]
	S += 62 < c_t1_t01_mem1
	S += c_t1_t01_mem1 <= c_t1_t01

	c_t1_t11 = S.Task('c_t1_t11', length=3, delay_cost=1)
	c_t1_t11 += alt(MAS)
	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	c_t1_t11_in += alt(MAS_in)
	S += c_t1_t11_in*MAS_in[0]<=c_t1_t11*MAS[0]

	S += c_t1_t11_in*MAS_in[1]<=c_t1_t11*MAS[1]

	S += c_t1_t11_in*MAS_in[2]<=c_t1_t11*MAS[2]

	S += c_t1_t11_in*MAS_in[3]<=c_t1_t11*MAS[3]

	S += c_t1_t11_in*MAS_in[4]<=c_t1_t11*MAS[4]

	S += c_t1_t11_in*MAS_in[5]<=c_t1_t11*MAS[5]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	c_t1_t11_mem0 += MM_MEM[2]
	S += 59 < c_t1_t11_mem0
	S += c_t1_t11_mem0 <= c_t1_t11

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	c_t1_t11_mem1 += MAS_MEM[9]
	S += 55 < c_t1_t11_mem1
	S += c_t1_t11_mem1 <= c_t1_t11

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=11, delay_cost=1)
	c_t1_t4_t4 += alt(MM)
	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	c_t1_t4_t4_in += alt(MM_in)
	S += c_t1_t4_t4_in*MM_in[0]<=c_t1_t4_t4*MM[0]
	S += c_t1_t4_t4_in*MM_in[1]<=c_t1_t4_t4*MM[1]
	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	c_t1_t4_t4_mem0 += MAS_MEM[0]
	S += 47 < c_t1_t4_t4_mem0
	S += c_t1_t4_t4_mem0 <= c_t1_t4_t4

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	c_t1_t4_t4_mem1 += MAS_MEM[7]
	S += 52 < c_t1_t4_t4_mem1
	S += c_t1_t4_t4_mem1 <= c_t1_t4_t4

	c_t1_t40 = S.Task('c_t1_t40', length=3, delay_cost=1)
	c_t1_t40 += alt(MAS)
	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	c_t1_t40_in += alt(MAS_in)
	S += c_t1_t40_in*MAS_in[0]<=c_t1_t40*MAS[0]

	S += c_t1_t40_in*MAS_in[1]<=c_t1_t40*MAS[1]

	S += c_t1_t40_in*MAS_in[2]<=c_t1_t40*MAS[2]

	S += c_t1_t40_in*MAS_in[3]<=c_t1_t40*MAS[3]

	S += c_t1_t40_in*MAS_in[4]<=c_t1_t40*MAS[4]

	S += c_t1_t40_in*MAS_in[5]<=c_t1_t40*MAS[5]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	c_t1_t40_mem0 += MM_MEM[0]
	S += 60 < c_t1_t40_mem0
	S += c_t1_t40_mem0 <= c_t1_t40

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	c_t1_t40_mem1 += MM_MEM[3]
	S += 55 < c_t1_t40_mem1
	S += c_t1_t40_mem1 <= c_t1_t40

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=3, delay_cost=1)
	c_t1_t4_t5 += alt(MAS)
	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	c_t1_t4_t5_in += alt(MAS_in)
	S += c_t1_t4_t5_in*MAS_in[0]<=c_t1_t4_t5*MAS[0]

	S += c_t1_t4_t5_in*MAS_in[1]<=c_t1_t4_t5*MAS[1]

	S += c_t1_t4_t5_in*MAS_in[2]<=c_t1_t4_t5*MAS[2]

	S += c_t1_t4_t5_in*MAS_in[3]<=c_t1_t4_t5*MAS[3]

	S += c_t1_t4_t5_in*MAS_in[4]<=c_t1_t4_t5*MAS[4]

	S += c_t1_t4_t5_in*MAS_in[5]<=c_t1_t4_t5*MAS[5]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	c_t1_t4_t5_mem0 += MM_MEM[0]
	S += 60 < c_t1_t4_t5_mem0
	S += c_t1_t4_t5_mem0 <= c_t1_t4_t5

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	c_t1_t4_t5_mem1 += MM_MEM[3]
	S += 55 < c_t1_t4_t5_mem1
	S += c_t1_t4_t5_mem1 <= c_t1_t4_t5

	c_t1_t50 = S.Task('c_t1_t50', length=3, delay_cost=1)
	c_t1_t50 += alt(MAS)
	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	c_t1_t50_in += alt(MAS_in)
	S += c_t1_t50_in*MAS_in[0]<=c_t1_t50*MAS[0]

	S += c_t1_t50_in*MAS_in[1]<=c_t1_t50*MAS[1]

	S += c_t1_t50_in*MAS_in[2]<=c_t1_t50*MAS[2]

	S += c_t1_t50_in*MAS_in[3]<=c_t1_t50*MAS[3]

	S += c_t1_t50_in*MAS_in[4]<=c_t1_t50*MAS[4]

	S += c_t1_t50_in*MAS_in[5]<=c_t1_t50*MAS[5]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	c_t1_t50_mem0 += MAS_MEM[4]
	S += 61 < c_t1_t50_mem0
	S += c_t1_t50_mem0 <= c_t1_t50

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	c_t1_t50_mem1 += MAS_MEM[5]
	S += 54 < c_t1_t50_mem1
	S += c_t1_t50_mem1 <= c_t1_t50

	c_t2_t01 = S.Task('c_t2_t01', length=3, delay_cost=1)
	c_t2_t01 += alt(MAS)
	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	c_t2_t01_in += alt(MAS_in)
	S += c_t2_t01_in*MAS_in[0]<=c_t2_t01*MAS[0]

	S += c_t2_t01_in*MAS_in[1]<=c_t2_t01*MAS[1]

	S += c_t2_t01_in*MAS_in[2]<=c_t2_t01*MAS[2]

	S += c_t2_t01_in*MAS_in[3]<=c_t2_t01*MAS[3]

	S += c_t2_t01_in*MAS_in[4]<=c_t2_t01*MAS[4]

	S += c_t2_t01_in*MAS_in[5]<=c_t2_t01*MAS[5]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	c_t2_t01_mem0 += MM_MEM[2]
	S += 101 < c_t2_t01_mem0
	S += c_t2_t01_mem0 <= c_t2_t01

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	c_t2_t01_mem1 += MAS_MEM[5]
	S += 86 < c_t2_t01_mem1
	S += c_t2_t01_mem1 <= c_t2_t01

	c_t2_t11 = S.Task('c_t2_t11', length=3, delay_cost=1)
	c_t2_t11 += alt(MAS)
	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	c_t2_t11_in += alt(MAS_in)
	S += c_t2_t11_in*MAS_in[0]<=c_t2_t11*MAS[0]

	S += c_t2_t11_in*MAS_in[1]<=c_t2_t11*MAS[1]

	S += c_t2_t11_in*MAS_in[2]<=c_t2_t11*MAS[2]

	S += c_t2_t11_in*MAS_in[3]<=c_t2_t11*MAS[3]

	S += c_t2_t11_in*MAS_in[4]<=c_t2_t11*MAS[4]

	S += c_t2_t11_in*MAS_in[5]<=c_t2_t11*MAS[5]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	c_t2_t11_mem0 += MM_MEM[2]
	S += 88 < c_t2_t11_mem0
	S += c_t2_t11_mem0 <= c_t2_t11

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	c_t2_t11_mem1 += MAS_MEM[5]
	S += 92 < c_t2_t11_mem1
	S += c_t2_t11_mem1 <= c_t2_t11

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=11, delay_cost=1)
	c_t2_t4_t4 += alt(MM)
	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	c_t2_t4_t4_in += alt(MM_in)
	S += c_t2_t4_t4_in*MM_in[0]<=c_t2_t4_t4*MM[0]
	S += c_t2_t4_t4_in*MM_in[1]<=c_t2_t4_t4*MM[1]
	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	c_t2_t4_t4_mem0 += MAS_MEM[2]
	S += 75 < c_t2_t4_t4_mem0
	S += c_t2_t4_t4_mem0 <= c_t2_t4_t4

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	c_t2_t4_t4_mem1 += MAS_MEM[7]
	S += 92 < c_t2_t4_t4_mem1
	S += c_t2_t4_t4_mem1 <= c_t2_t4_t4

	c_t2_t40 = S.Task('c_t2_t40', length=3, delay_cost=1)
	c_t2_t40 += alt(MAS)
	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	c_t2_t40_in += alt(MAS_in)
	S += c_t2_t40_in*MAS_in[0]<=c_t2_t40*MAS[0]

	S += c_t2_t40_in*MAS_in[1]<=c_t2_t40*MAS[1]

	S += c_t2_t40_in*MAS_in[2]<=c_t2_t40*MAS[2]

	S += c_t2_t40_in*MAS_in[3]<=c_t2_t40*MAS[3]

	S += c_t2_t40_in*MAS_in[4]<=c_t2_t40*MAS[4]

	S += c_t2_t40_in*MAS_in[5]<=c_t2_t40*MAS[5]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	c_t2_t40_mem0 += MM_MEM[2]
	S += 97 < c_t2_t40_mem0
	S += c_t2_t40_mem0 <= c_t2_t40

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	c_t2_t40_mem1 += MM_MEM[3]
	S += 99 < c_t2_t40_mem1
	S += c_t2_t40_mem1 <= c_t2_t40

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=3, delay_cost=1)
	c_t2_t4_t5 += alt(MAS)
	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	c_t2_t4_t5_in += alt(MAS_in)
	S += c_t2_t4_t5_in*MAS_in[0]<=c_t2_t4_t5*MAS[0]

	S += c_t2_t4_t5_in*MAS_in[1]<=c_t2_t4_t5*MAS[1]

	S += c_t2_t4_t5_in*MAS_in[2]<=c_t2_t4_t5*MAS[2]

	S += c_t2_t4_t5_in*MAS_in[3]<=c_t2_t4_t5*MAS[3]

	S += c_t2_t4_t5_in*MAS_in[4]<=c_t2_t4_t5*MAS[4]

	S += c_t2_t4_t5_in*MAS_in[5]<=c_t2_t4_t5*MAS[5]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	c_t2_t4_t5_mem0 += MM_MEM[2]
	S += 97 < c_t2_t4_t5_mem0
	S += c_t2_t4_t5_mem0 <= c_t2_t4_t5

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	c_t2_t4_t5_mem1 += MM_MEM[3]
	S += 99 < c_t2_t4_t5_mem1
	S += c_t2_t4_t5_mem1 <= c_t2_t4_t5

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage3MAS6/FP12_LADDERMUL/schedule7.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

