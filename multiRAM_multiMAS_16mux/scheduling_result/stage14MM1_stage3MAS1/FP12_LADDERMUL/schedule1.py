from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 153
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=14)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=1, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 0
	d_t0_a1_0_in += MAS_in[0]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 0
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 0
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=3, delay_cost=1)
	S += d_t0_a1_0 >= 1
	d_t0_a1_0 += MAS[0]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 1
	d_t3010_in += MAS_in[0]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 1
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 1
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 2
	d_t3001_in += MAS_in[0]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 2
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 2
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t3010 = S.Task('d_t3010', length=3, delay_cost=1)
	S += d_t3010 >= 2
	d_t3010 += MAS[0]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 3
	d_t3000_in += MAS_in[0]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 3
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 3
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t3001 = S.Task('d_t3001', length=3, delay_cost=1)
	S += d_t3001 >= 3
	d_t3001 += MAS[0]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 4
	d_t2_t3_t3_in += MAS_in[0]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 4
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 4
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3000 = S.Task('d_t3000', length=3, delay_cost=1)
	S += d_t3000 >= 4
	d_t3000 += MAS[0]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 5
	d_t1_t3_t0_in += MM_in[0]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 5
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 5
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=3, delay_cost=1)
	S += d_t2_t3_t3 >= 5
	d_t2_t3_t3 += MAS[0]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=14, delay_cost=1)
	S += d_t1_t3_t0 >= 6
	d_t1_t3_t0 += MM[0]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 6
	d_t3011_in += MAS_in[0]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 6
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 6
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 7
	d_t0_a1_1_in += MAS_in[0]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 7
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 7
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t3011 = S.Task('d_t3011', length=3, delay_cost=1)
	S += d_t3011 >= 7
	d_t3011 += MAS[0]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=3, delay_cost=1)
	S += d_t0_a1_1 >= 8
	d_t0_a1_1 += MAS[0]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 8
	d_t1_t11_in += MAS_in[0]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 8
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 8
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t1_t11 = S.Task('d_t1_t11', length=3, delay_cost=1)
	S += d_t1_t11 >= 9
	d_t1_t11 += MAS[0]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 9
	d_t1_t3_t2_in += MAS_in[0]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 9
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 9
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 10
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 10
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 10
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=3, delay_cost=1)
	S += d_t1_t3_t2 >= 10
	d_t1_t3_t2 += MAS[0]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 11
	d_t1_t10_in += MAS_in[0]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 11
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 11
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=14, delay_cost=1)
	S += d_t1_t3_t1 >= 11
	d_t1_t3_t1 += MM[0]

	d_t1_t10 = S.Task('d_t1_t10', length=3, delay_cost=1)
	S += d_t1_t10 >= 12
	d_t1_t10 += MAS[0]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 12
	d_t4000_in += MAS_in[0]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 12
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 12
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t4000 = S.Task('d_t4000', length=3, delay_cost=1)
	S += d_t4000 >= 13
	d_t4000 += MAS[0]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 13
	d_t4001_in += MAS_in[0]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 13
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 13
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 14
	d_t1_a1_1_in += MAS_in[0]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 14
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 14
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t4001 = S.Task('d_t4001', length=3, delay_cost=1)
	S += d_t4001 >= 14
	d_t4001 += MAS[0]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 15
	d_t1_a1_0_in += MAS_in[0]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 15
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 15
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=3, delay_cost=1)
	S += d_t1_a1_1 >= 15
	d_t1_a1_1 += MAS[0]

	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 16
	d_t0_t3_t3_in += MAS_in[0]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 16
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 16
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=3, delay_cost=1)
	S += d_t1_a1_0 >= 16
	d_t1_a1_0 += MAS[0]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 17
	d_t0_t3_t2_in += MAS_in[0]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 17
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 17
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=3, delay_cost=1)
	S += d_t0_t3_t3 >= 17
	d_t0_t3_t3 += MAS[0]

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

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 19
	d_t0_t3_t0_in += MM_in[0]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 19
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 19
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=14, delay_cost=1)
	S += d_t0_t3_t1 >= 19
	d_t0_t3_t1 += MM[0]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 20
	d_t0_t11_in += MAS_in[0]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 20
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 20
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=14, delay_cost=1)
	S += d_t0_t3_t0 >= 20
	d_t0_t3_t0 += MM[0]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 21
	d_t0_t10_in += MAS_in[0]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 21
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 21
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t0_t11 = S.Task('d_t0_t11', length=3, delay_cost=1)
	S += d_t0_t11 >= 21
	d_t0_t11 += MAS[0]

	d_t0_t10 = S.Task('d_t0_t10', length=3, delay_cost=1)
	S += d_t0_t10 >= 22
	d_t0_t10 += MAS[0]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 22
	d_t2_t3_t2_in += MAS_in[0]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 22
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 22
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 23
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 23
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 23
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=3, delay_cost=1)
	S += d_t2_t3_t2 >= 23
	d_t2_t3_t2 += MAS[0]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 24
	d_t2_t3_t0_in += MM_in[0]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 24
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 24
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=14, delay_cost=1)
	S += d_t2_t3_t1 >= 24
	d_t2_t3_t1 += MM[0]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 25
	d_t2_t11_in += MAS_in[0]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 25
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 25
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=14, delay_cost=1)
	S += d_t2_t3_t0 >= 25
	d_t2_t3_t0 += MM[0]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 26
	d_t2_t10_in += MAS_in[0]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 26
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 26
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t11 = S.Task('d_t2_t11', length=3, delay_cost=1)
	S += d_t2_t11 >= 26
	d_t2_t11 += MAS[0]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 27
	d_t2_a1_1_in += MAS_in[0]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 27
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 27
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_t10 = S.Task('d_t2_t10', length=3, delay_cost=1)
	S += d_t2_t10 >= 27
	d_t2_t10 += MAS[0]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 28
	d_t2_a1_0_in += MAS_in[0]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 28
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 28
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=3, delay_cost=1)
	S += d_t2_a1_1 >= 28
	d_t2_a1_1 += MAS[0]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 29
	d_t1_t3_t3_in += MAS_in[0]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 29
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 29
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=3, delay_cost=1)
	S += d_t2_a1_0 >= 29
	d_t2_a1_0 += MAS[0]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=3, delay_cost=1)
	S += d_t1_t3_t3 >= 30
	d_t1_t3_t3 += MAS[0]


	# new tasks
	d_t4010 = S.Task('d_t4010', length=3, delay_cost=1)
	d_t4010 += alt(MAS)
	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	d_t4010_in += alt(MAS_in)
	S += d_t4010_in*MAS_in[0]<=d_t4010*MAS[0]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	d_t4010_mem0 += MAIN_MEM_r[0]
	S += d_t4010_mem0 <= d_t4010

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	d_t4010_mem1 += MAIN_MEM_r[1]
	S += d_t4010_mem1 <= d_t4010

	d_t4011 = S.Task('d_t4011', length=3, delay_cost=1)
	d_t4011 += alt(MAS)
	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	d_t4011_in += alt(MAS_in)
	S += d_t4011_in*MAS_in[0]<=d_t4011*MAS[0]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	d_t4011_mem0 += MAIN_MEM_r[0]
	S += d_t4011_mem0 <= d_t4011

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	d_t4011_mem1 += MAIN_MEM_r[1]
	S += d_t4011_mem1 <= d_t4011

	d_t5000 = S.Task('d_t5000', length=3, delay_cost=1)
	d_t5000 += alt(MAS)
	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	d_t5000_in += alt(MAS_in)
	S += d_t5000_in*MAS_in[0]<=d_t5000*MAS[0]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	d_t5000_mem0 += MAIN_MEM_r[0]
	S += d_t5000_mem0 <= d_t5000

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	d_t5000_mem1 += MAIN_MEM_r[1]
	S += d_t5000_mem1 <= d_t5000

	d_t5001 = S.Task('d_t5001', length=3, delay_cost=1)
	d_t5001 += alt(MAS)
	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	d_t5001_in += alt(MAS_in)
	S += d_t5001_in*MAS_in[0]<=d_t5001*MAS[0]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	d_t5001_mem0 += MAIN_MEM_r[0]
	S += d_t5001_mem0 <= d_t5001

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	d_t5001_mem1 += MAIN_MEM_r[1]
	S += d_t5001_mem1 <= d_t5001

	d_t5010 = S.Task('d_t5010', length=3, delay_cost=1)
	d_t5010 += alt(MAS)
	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	d_t5010_in += alt(MAS_in)
	S += d_t5010_in*MAS_in[0]<=d_t5010*MAS[0]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	d_t5010_mem0 += MAIN_MEM_r[0]
	S += d_t5010_mem0 <= d_t5010

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	d_t5010_mem1 += MAIN_MEM_r[1]
	S += d_t5010_mem1 <= d_t5010

	d_t5011 = S.Task('d_t5011', length=3, delay_cost=1)
	d_t5011 += alt(MAS)
	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	d_t5011_in += alt(MAS_in)
	S += d_t5011_in*MAS_in[0]<=d_t5011*MAS[0]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	d_t5011_mem0 += MAIN_MEM_r[0]
	S += d_t5011_mem0 <= d_t5011

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	d_t5011_mem1 += MAIN_MEM_r[1]
	S += d_t5011_mem1 <= d_t5011

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=14, delay_cost=1)
	c_t0_t0_t0 += alt(MM)
	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	c_t0_t0_t0_in += alt(MM_in)
	S += c_t0_t0_t0_in*MM_in[0]<=c_t0_t0_t0*MM[0]
	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c_t0_t0_t0_mem0 <= c_t0_t0_t0

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_t0_t0_t0_mem1 <= c_t0_t0_t0

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=14, delay_cost=1)
	c_t0_t0_t1 += alt(MM)
	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	c_t0_t0_t1_in += alt(MM_in)
	S += c_t0_t0_t1_in*MM_in[0]<=c_t0_t0_t1*MM[0]
	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c_t0_t0_t1_mem0 <= c_t0_t0_t1

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_t0_t0_t1_mem1 <= c_t0_t0_t1

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=3, delay_cost=1)
	c_t0_t0_t2 += alt(MAS)
	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	c_t0_t0_t2_in += alt(MAS_in)
	S += c_t0_t0_t2_in*MAS_in[0]<=c_t0_t0_t2*MAS[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c_t0_t0_t2_mem0 <= c_t0_t0_t2

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c_t0_t0_t2_mem1 <= c_t0_t0_t2

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=3, delay_cost=1)
	c_t0_t0_t3 += alt(MAS)
	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	c_t0_t0_t3_in += alt(MAS_in)
	S += c_t0_t0_t3_in*MAS_in[0]<=c_t0_t0_t3*MAS[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_t0_t0_t3_mem0 <= c_t0_t0_t3

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_t0_t0_t3_mem1 <= c_t0_t0_t3

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=14, delay_cost=1)
	c_t0_t1_t0 += alt(MM)
	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	c_t0_t1_t0_in += alt(MM_in)
	S += c_t0_t1_t0_in*MM_in[0]<=c_t0_t1_t0*MM[0]
	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c_t0_t1_t0_mem0 <= c_t0_t1_t0

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_t0_t1_t0_mem1 <= c_t0_t1_t0

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=14, delay_cost=1)
	c_t0_t1_t1 += alt(MM)
	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	c_t0_t1_t1_in += alt(MM_in)
	S += c_t0_t1_t1_in*MM_in[0]<=c_t0_t1_t1*MM[0]
	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c_t0_t1_t1_mem0 <= c_t0_t1_t1

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_t0_t1_t1_mem1 <= c_t0_t1_t1

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=3, delay_cost=1)
	c_t0_t1_t2 += alt(MAS)
	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	c_t0_t1_t2_in += alt(MAS_in)
	S += c_t0_t1_t2_in*MAS_in[0]<=c_t0_t1_t2*MAS[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c_t0_t1_t2_mem0 <= c_t0_t1_t2

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c_t0_t1_t2_mem1 <= c_t0_t1_t2

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=3, delay_cost=1)
	c_t0_t1_t3 += alt(MAS)
	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	c_t0_t1_t3_in += alt(MAS_in)
	S += c_t0_t1_t3_in*MAS_in[0]<=c_t0_t1_t3*MAS[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_t0_t1_t3_mem0 <= c_t0_t1_t3

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_t0_t1_t3_mem1 <= c_t0_t1_t3

	c_t0_t20 = S.Task('c_t0_t20', length=3, delay_cost=1)
	c_t0_t20 += alt(MAS)
	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	c_t0_t20_in += alt(MAS_in)
	S += c_t0_t20_in*MAS_in[0]<=c_t0_t20*MAS[0]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	c_t0_t20_mem0 += MAIN_MEM_r[0]
	S += c_t0_t20_mem0 <= c_t0_t20

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	c_t0_t20_mem1 += MAIN_MEM_r[1]
	S += c_t0_t20_mem1 <= c_t0_t20

	c_t0_t21 = S.Task('c_t0_t21', length=3, delay_cost=1)
	c_t0_t21 += alt(MAS)
	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	c_t0_t21_in += alt(MAS_in)
	S += c_t0_t21_in*MAS_in[0]<=c_t0_t21*MAS[0]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	c_t0_t21_mem0 += MAIN_MEM_r[0]
	S += c_t0_t21_mem0 <= c_t0_t21

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	c_t0_t21_mem1 += MAIN_MEM_r[1]
	S += c_t0_t21_mem1 <= c_t0_t21

	c_t0_t30 = S.Task('c_t0_t30', length=3, delay_cost=1)
	c_t0_t30 += alt(MAS)
	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	c_t0_t30_in += alt(MAS_in)
	S += c_t0_t30_in*MAS_in[0]<=c_t0_t30*MAS[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	c_t0_t30_mem0 += MAIN_MEM_r[0]
	S += c_t0_t30_mem0 <= c_t0_t30

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	c_t0_t30_mem1 += MAIN_MEM_r[1]
	S += c_t0_t30_mem1 <= c_t0_t30

	c_t0_t31 = S.Task('c_t0_t31', length=3, delay_cost=1)
	c_t0_t31 += alt(MAS)
	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	c_t0_t31_in += alt(MAS_in)
	S += c_t0_t31_in*MAS_in[0]<=c_t0_t31*MAS[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	c_t0_t31_mem0 += MAIN_MEM_r[0]
	S += c_t0_t31_mem0 <= c_t0_t31

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	c_t0_t31_mem1 += MAIN_MEM_r[1]
	S += c_t0_t31_mem1 <= c_t0_t31

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=14, delay_cost=1)
	c_t1_t0_t0 += alt(MM)
	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	c_t1_t0_t0_in += alt(MM_in)
	S += c_t1_t0_t0_in*MM_in[0]<=c_t1_t0_t0*MM[0]
	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c_t1_t0_t0_mem0 <= c_t1_t0_t0

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_t1_t0_t0_mem1 <= c_t1_t0_t0

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=14, delay_cost=1)
	c_t1_t0_t1 += alt(MM)
	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	c_t1_t0_t1_in += alt(MM_in)
	S += c_t1_t0_t1_in*MM_in[0]<=c_t1_t0_t1*MM[0]
	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c_t1_t0_t1_mem0 <= c_t1_t0_t1

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_t1_t0_t1_mem1 <= c_t1_t0_t1

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=3, delay_cost=1)
	c_t1_t0_t2 += alt(MAS)
	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	c_t1_t0_t2_in += alt(MAS_in)
	S += c_t1_t0_t2_in*MAS_in[0]<=c_t1_t0_t2*MAS[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c_t1_t0_t2_mem0 <= c_t1_t0_t2

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c_t1_t0_t2_mem1 <= c_t1_t0_t2

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=3, delay_cost=1)
	c_t1_t0_t3 += alt(MAS)
	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	c_t1_t0_t3_in += alt(MAS_in)
	S += c_t1_t0_t3_in*MAS_in[0]<=c_t1_t0_t3*MAS[0]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_t1_t0_t3_mem0 <= c_t1_t0_t3

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_t1_t0_t3_mem1 <= c_t1_t0_t3

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=14, delay_cost=1)
	c_t1_t1_t0 += alt(MM)
	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	c_t1_t1_t0_in += alt(MM_in)
	S += c_t1_t1_t0_in*MM_in[0]<=c_t1_t1_t0*MM[0]
	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c_t1_t1_t0_mem0 <= c_t1_t1_t0

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_t1_t1_t0_mem1 <= c_t1_t1_t0

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=14, delay_cost=1)
	c_t1_t1_t1 += alt(MM)
	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	c_t1_t1_t1_in += alt(MM_in)
	S += c_t1_t1_t1_in*MM_in[0]<=c_t1_t1_t1*MM[0]
	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c_t1_t1_t1_mem0 <= c_t1_t1_t1

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_t1_t1_t1_mem1 <= c_t1_t1_t1

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=3, delay_cost=1)
	c_t1_t1_t2 += alt(MAS)
	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	c_t1_t1_t2_in += alt(MAS_in)
	S += c_t1_t1_t2_in*MAS_in[0]<=c_t1_t1_t2*MAS[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c_t1_t1_t2_mem0 <= c_t1_t1_t2

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c_t1_t1_t2_mem1 <= c_t1_t1_t2

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=3, delay_cost=1)
	c_t1_t1_t3 += alt(MAS)
	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	c_t1_t1_t3_in += alt(MAS_in)
	S += c_t1_t1_t3_in*MAS_in[0]<=c_t1_t1_t3*MAS[0]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_t1_t1_t3_mem0 <= c_t1_t1_t3

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_t1_t1_t3_mem1 <= c_t1_t1_t3

	c_t1_t20 = S.Task('c_t1_t20', length=3, delay_cost=1)
	c_t1_t20 += alt(MAS)
	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	c_t1_t20_in += alt(MAS_in)
	S += c_t1_t20_in*MAS_in[0]<=c_t1_t20*MAS[0]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	c_t1_t20_mem0 += MAIN_MEM_r[0]
	S += c_t1_t20_mem0 <= c_t1_t20

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	c_t1_t20_mem1 += MAIN_MEM_r[1]
	S += c_t1_t20_mem1 <= c_t1_t20

	c_t1_t21 = S.Task('c_t1_t21', length=3, delay_cost=1)
	c_t1_t21 += alt(MAS)
	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	c_t1_t21_in += alt(MAS_in)
	S += c_t1_t21_in*MAS_in[0]<=c_t1_t21*MAS[0]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	c_t1_t21_mem0 += MAIN_MEM_r[0]
	S += c_t1_t21_mem0 <= c_t1_t21

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	c_t1_t21_mem1 += MAIN_MEM_r[1]
	S += c_t1_t21_mem1 <= c_t1_t21

	c_t1_t30 = S.Task('c_t1_t30', length=3, delay_cost=1)
	c_t1_t30 += alt(MAS)
	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	c_t1_t30_in += alt(MAS_in)
	S += c_t1_t30_in*MAS_in[0]<=c_t1_t30*MAS[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	c_t1_t30_mem0 += MAIN_MEM_r[0]
	S += c_t1_t30_mem0 <= c_t1_t30

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	c_t1_t30_mem1 += MAIN_MEM_r[1]
	S += c_t1_t30_mem1 <= c_t1_t30

	c_t1_t31 = S.Task('c_t1_t31', length=3, delay_cost=1)
	c_t1_t31 += alt(MAS)
	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	c_t1_t31_in += alt(MAS_in)
	S += c_t1_t31_in*MAS_in[0]<=c_t1_t31*MAS[0]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	c_t1_t31_mem0 += MAIN_MEM_r[0]
	S += c_t1_t31_mem0 <= c_t1_t31

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	c_t1_t31_mem1 += MAIN_MEM_r[1]
	S += c_t1_t31_mem1 <= c_t1_t31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM1_stage3MAS1/FP12_LADDERMUL/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution
