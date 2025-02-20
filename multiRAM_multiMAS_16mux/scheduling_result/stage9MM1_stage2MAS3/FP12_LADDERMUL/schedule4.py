from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 218
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=9)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=3)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=3, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=6)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 0
	d_t0_t3_t3_in += MAS_in[0]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 0
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 0
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 1
	d_t0_t3_t2_in += MAS_in[0]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 1
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 1
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=2, delay_cost=1)
	S += d_t0_t3_t3 >= 1
	d_t0_t3_t3 += MAS[0]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 2
	d_t0_t11_in += MAS_in[0]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 2
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 2
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=2, delay_cost=1)
	S += d_t0_t3_t2 >= 2
	d_t0_t3_t2 += MAS[0]

	d_t0_t11 = S.Task('d_t0_t11', length=2, delay_cost=1)
	S += d_t0_t11 >= 3
	d_t0_t11 += MAS[0]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 3
	d_t2_a1_0_in += MAS_in[0]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 3
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 3
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=2, delay_cost=1)
	S += d_t2_a1_0 >= 4
	d_t2_a1_0 += MAS[0]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 4
	d_t2_t11_in += MAS_in[0]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 4
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 4
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 5
	d_t1_a1_0_in += MAS_in[0]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 5
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 5
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_t11 = S.Task('d_t2_t11', length=2, delay_cost=1)
	S += d_t2_t11 >= 5
	d_t2_t11 += MAS[0]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=2, delay_cost=1)
	S += d_t1_a1_0 >= 6
	d_t1_a1_0 += MAS[0]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 6
	d_t3011_in += MAS_in[0]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 6
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 6
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 7
	d_t1_t10_in += MAS_in[0]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 7
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 7
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t3011 = S.Task('d_t3011', length=2, delay_cost=1)
	S += d_t3011 >= 7
	d_t3011 += MAS[0]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 8
	d_t0_t10_in += MAS_in[1]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 8
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 8
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t1_t10 = S.Task('d_t1_t10', length=2, delay_cost=1)
	S += d_t1_t10 >= 8
	d_t1_t10 += MAS[0]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 9
	d_t0_a1_1_in += MAS_in[0]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 9
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 9
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t0_t10 = S.Task('d_t0_t10', length=2, delay_cost=1)
	S += d_t0_t10 >= 9
	d_t0_t10 += MAS[1]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=2, delay_cost=1)
	S += d_t0_a1_1 >= 10
	d_t0_a1_1 += MAS[0]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 10
	d_t2_t3_t2_in += MAS_in[1]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 10
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 10
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=2, delay_cost=1)
	S += d_t2_t3_t2 >= 11
	d_t2_t3_t2 += MAS[1]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 11
	d_t3001_in += MAS_in[1]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 11
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 11
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t3001 = S.Task('d_t3001', length=2, delay_cost=1)
	S += d_t3001 >= 12
	d_t3001 += MAS[1]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 12
	d_t4000_in += MAS_in[1]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 12
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 12
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 13
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 13
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 13
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t4000 = S.Task('d_t4000', length=2, delay_cost=1)
	S += d_t4000 >= 13
	d_t4000 += MAS[1]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 14
	d_t1_t3_t2_in += MAS_in[2]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 14
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 14
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=9, delay_cost=1)
	S += d_t2_t3_t1 >= 14
	d_t2_t3_t1 += MM[0]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=2, delay_cost=1)
	S += d_t1_t3_t2 >= 15
	d_t1_t3_t2 += MAS[2]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 15
	d_t2_a1_1_in += MAS_in[0]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 15
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 15
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 16
	d_t1_a1_1_in += MAS_in[1]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 16
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 16
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=2, delay_cost=1)
	S += d_t2_a1_1 >= 16
	d_t2_a1_1 += MAS[0]

	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 17
	d_t0_a1_0_in += MAS_in[0]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 17
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 17
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=2, delay_cost=1)
	S += d_t1_a1_1 >= 17
	d_t1_a1_1 += MAS[1]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=2, delay_cost=1)
	S += d_t0_a1_0 >= 18
	d_t0_a1_0 += MAS[0]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 18
	d_t2_t10_in += MAS_in[0]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 18
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 18
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t10 = S.Task('d_t2_t10', length=2, delay_cost=1)
	S += d_t2_t10 >= 19
	d_t2_t10 += MAS[0]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 19
	d_t3010_in += MAS_in[1]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 19
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 19
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 20
	d_t3000_in += MAS_in[0]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 20
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 20
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t3010 = S.Task('d_t3010', length=2, delay_cost=1)
	S += d_t3010 >= 20
	d_t3010 += MAS[1]

	d_t3000 = S.Task('d_t3000', length=2, delay_cost=1)
	S += d_t3000 >= 21
	d_t3000 += MAS[0]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 21
	d_t4001_in += MAS_in[1]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 21
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 21
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 22
	d_t2_t3_t3_in += MAS_in[1]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 22
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 22
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t4001 = S.Task('d_t4001', length=2, delay_cost=1)
	S += d_t4001 >= 22
	d_t4001 += MAS[1]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 23
	d_t1_t11_in += MAS_in[0]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 23
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 23
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=2, delay_cost=1)
	S += d_t2_t3_t3 >= 23
	d_t2_t3_t3 += MAS[1]

	d_t1_t11 = S.Task('d_t1_t11', length=2, delay_cost=1)
	S += d_t1_t11 >= 24
	d_t1_t11 += MAS[0]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 24
	d_t1_t3_t3_in += MAS_in[0]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 24
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 24
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=2, delay_cost=1)
	S += d_t1_t3_t3 >= 25
	d_t1_t3_t3 += MAS[0]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 25
	d_t2_t3_t0_in += MM_in[0]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 25
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 25
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 26
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 26
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 26
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=9, delay_cost=1)
	S += d_t2_t3_t0 >= 26
	d_t2_t3_t0 += MM[0]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 27
	d_t1_t3_t0_in += MM_in[0]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 27
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 27
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=9, delay_cost=1)
	S += d_t1_t3_t1 >= 27
	d_t1_t3_t1 += MM[0]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 28
	d_t0_t3_t1_in += MM_in[0]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 28
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 28
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=9, delay_cost=1)
	S += d_t1_t3_t0 >= 28
	d_t1_t3_t0 += MM[0]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 29
	d_t0_t3_t0_in += MM_in[0]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 29
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 29
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=9, delay_cost=1)
	S += d_t0_t3_t1 >= 29
	d_t0_t3_t1 += MM[0]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=9, delay_cost=1)
	S += d_t0_t3_t0 >= 30
	d_t0_t3_t0 += MM[0]

	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	S += d_t4010_in >= 30
	d_t4010_in += MAS_in[0]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 30
	d_t4010_mem0 += MAIN_MEM_r[0]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 30
	d_t4010_mem1 += MAIN_MEM_r[1]

	d_t4010 = S.Task('d_t4010', length=2, delay_cost=1)
	S += d_t4010 >= 31
	d_t4010 += MAS[0]

	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	S += d_t5001_in >= 31
	d_t5001_in += MAS_in[2]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 31
	d_t5001_mem0 += MAIN_MEM_r[0]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 31
	d_t5001_mem1 += MAIN_MEM_r[1]

	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	S += d_t5000_in >= 32
	d_t5000_in += MAS_in[0]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 32
	d_t5000_mem0 += MAIN_MEM_r[0]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 32
	d_t5000_mem1 += MAIN_MEM_r[1]

	d_t5001 = S.Task('d_t5001', length=2, delay_cost=1)
	S += d_t5001 >= 32
	d_t5001 += MAS[2]

	d_t5000 = S.Task('d_t5000', length=2, delay_cost=1)
	S += d_t5000 >= 33
	d_t5000 += MAS[0]

	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	S += d_t5010_in >= 33
	d_t5010_in += MAS_in[0]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 33
	d_t5010_mem0 += MAIN_MEM_r[0]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 33
	d_t5010_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 34
	c_t0_t0_t3_in += MAS_in[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 34
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 34
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	d_t5010 = S.Task('d_t5010', length=2, delay_cost=1)
	S += d_t5010 >= 34
	d_t5010 += MAS[0]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=2, delay_cost=1)
	S += c_t0_t0_t3 >= 35
	c_t0_t0_t3 += MAS[0]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 35
	c_t0_t20_in += MAS_in[0]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 35
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 35
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 36
	c_t0_t0_t2_in += MAS_in[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 36
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 36
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t20 = S.Task('c_t0_t20', length=2, delay_cost=1)
	S += c_t0_t20 >= 36
	c_t0_t20 += MAS[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=2, delay_cost=1)
	S += c_t0_t0_t2 >= 37
	c_t0_t0_t2 += MAS[0]

	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	S += d_t5011_in >= 37
	d_t5011_in += MAS_in[0]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 37
	d_t5011_mem0 += MAIN_MEM_r[0]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 37
	d_t5011_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 38
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 38
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 38
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	d_t5011 = S.Task('d_t5011', length=2, delay_cost=1)
	S += d_t5011 >= 38
	d_t5011 += MAS[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 39
	c_t0_t1_t2_in += MAS_in[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 39
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 39
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=2, delay_cost=1)
	S += c_t1_t0_t2 >= 39
	c_t1_t0_t2 += MAS[0]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=2, delay_cost=1)
	S += c_t0_t1_t2 >= 40
	c_t0_t1_t2 += MAS[0]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 40
	c_t0_t30_in += MAS_in[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 40
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 40
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t30 = S.Task('c_t0_t30', length=2, delay_cost=1)
	S += c_t0_t30 >= 41
	c_t0_t30 += MAS[0]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 41
	c_t0_t31_in += MAS_in[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 41
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 41
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 42
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 42
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 42
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t31 = S.Task('c_t0_t31', length=2, delay_cost=1)
	S += c_t0_t31 >= 42
	c_t0_t31 += MAS[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=2, delay_cost=1)
	S += c_t0_t1_t3 >= 43
	c_t0_t1_t3 += MAS[0]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 43
	c_t0_t21_in += MAS_in[0]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 43
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 43
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t21 = S.Task('c_t0_t21', length=2, delay_cost=1)
	S += c_t0_t21 >= 44
	c_t0_t21 += MAS[0]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 44
	c_t1_t1_t3_in += MAS_in[0]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 44
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 44
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 45
	c_t1_t1_t2_in += MAS_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 45
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 45
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=2, delay_cost=1)
	S += c_t1_t1_t3 >= 45
	c_t1_t1_t3 += MAS[0]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 46
	c_t1_t0_t3_in += MAS_in[0]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 46
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 46
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=2, delay_cost=1)
	S += c_t1_t1_t2 >= 46
	c_t1_t1_t2 += MAS[0]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=2, delay_cost=1)
	S += c_t1_t0_t3 >= 47
	c_t1_t0_t3 += MAS[0]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 47
	c_t1_t30_in += MAS_in[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 47
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 47
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=2, delay_cost=1)
	S += c_t1_t30 >= 48
	c_t1_t30 += MAS[0]

	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	S += d_t4011_in >= 48
	d_t4011_in += MAS_in[1]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 48
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 48
	d_t4011_mem1 += MAIN_MEM_r[1]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 49
	c_t1_t21_in += MAS_in[1]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 49
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 49
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	d_t4011 = S.Task('d_t4011', length=2, delay_cost=1)
	S += d_t4011 >= 49
	d_t4011 += MAS[1]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 50
	c_t1_t20_in += MAS_in[2]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 50
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 50
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t21 = S.Task('c_t1_t21', length=2, delay_cost=1)
	S += c_t1_t21 >= 50
	c_t1_t21 += MAS[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 51
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 51
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 51
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t20 = S.Task('c_t1_t20', length=2, delay_cost=1)
	S += c_t1_t20 >= 51
	c_t1_t20 += MAS[2]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 52
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 52
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 52
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=9, delay_cost=1)
	S += c_t1_t0_t1 >= 52
	c_t1_t0_t1 += MM[0]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 53
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 53
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 53
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=9, delay_cost=1)
	S += c_t1_t0_t0 >= 53
	c_t1_t0_t0 += MM[0]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 54
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 54
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 54
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=9, delay_cost=1)
	S += c_t0_t1_t1 >= 54
	c_t0_t1_t1 += MM[0]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=9, delay_cost=1)
	S += c_t0_t1_t0 >= 55
	c_t0_t1_t0 += MM[0]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 55
	c_t1_t31_in += MAS_in[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 55
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 55
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 56
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 56
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 56
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=2, delay_cost=1)
	S += c_t1_t31 >= 56
	c_t1_t31 += MAS[1]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 57
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 57
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 57
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=9, delay_cost=1)
	S += c_t0_t0_t1 >= 57
	c_t0_t0_t1 += MM[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=9, delay_cost=1)
	S += c_t0_t0_t0 >= 58
	c_t0_t0_t0 += MM[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 58
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 58
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 58
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 59
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 59
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 59
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=9, delay_cost=1)
	S += c_t1_t1_t1 >= 59
	c_t1_t1_t1 += MM[0]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=9, delay_cost=1)
	S += c_t1_t1_t0 >= 60
	c_t1_t1_t0 += MM[0]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 60
	c_t4100_in += MAS_in[2]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 60
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 60
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 61
	c_t2_t31_in += MAS_in[0]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 61
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 61
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t4100 = S.Task('c_t4100', length=2, delay_cost=1)
	S += c_t4100 >= 61
	c_t4100 += MAS[2]

	c_t2_t31 = S.Task('c_t2_t31', length=2, delay_cost=1)
	S += c_t2_t31 >= 62
	c_t2_t31 += MAS[0]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 62
	c_t3010_in += MAS_in[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 62
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 62
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3010 = S.Task('c_t3010', length=2, delay_cost=1)
	S += c_t3010 >= 63
	c_t3010 += MAS[0]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 63
	c_t3111_in += MAS_in[0]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 63
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 63
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 64
	c_t3011_in += MAS_in[0]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 64
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 64
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3111 = S.Task('c_t3111', length=2, delay_cost=1)
	S += c_t3111 >= 64
	c_t3111 += MAS[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 65
	c_t2_t0_t3_in += MAS_in[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 65
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 65
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=2, delay_cost=1)
	S += c_t3011 >= 65
	c_t3011 += MAS[0]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=2, delay_cost=1)
	S += c_t2_t0_t3 >= 66
	c_t2_t0_t3 += MAS[0]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 66
	c_t5001_in += MAS_in[0]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 66
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 66
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 67
	c_t4000_in += MAS_in[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 67
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 67
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t5001 = S.Task('c_t5001', length=2, delay_cost=1)
	S += c_t5001 >= 67
	c_t5001 += MAS[0]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 68
	c_t2_t0_t2_in += MAS_in[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 68
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 68
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=2, delay_cost=1)
	S += c_t4000 >= 68
	c_t4000 += MAS[1]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=2, delay_cost=1)
	S += c_t2_t0_t2 >= 69
	c_t2_t0_t2 += MAS[0]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 69
	c_t2_t1_t3_in += MAS_in[1]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 69
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 69
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=2, delay_cost=1)
	S += c_t2_t1_t3 >= 70
	c_t2_t1_t3 += MAS[1]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 70
	c_t3101_in += MAS_in[0]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 70
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 70
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 71
	c_t2_t30_in += MAS_in[0]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 71
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 71
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t3101 = S.Task('c_t3101', length=2, delay_cost=1)
	S += c_t3101 >= 71
	c_t3101 += MAS[0]

	c_t2_t30 = S.Task('c_t2_t30', length=2, delay_cost=1)
	S += c_t2_t30 >= 72
	c_t2_t30 += MAS[0]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 72
	c_t3000_in += MAS_in[0]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 72
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 72
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3000 = S.Task('c_t3000', length=2, delay_cost=1)
	S += c_t3000 >= 73
	c_t3000 += MAS[0]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 73
	c_t4101_in += MAS_in[1]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 73
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 73
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t4101 = S.Task('c_t4101', length=2, delay_cost=1)
	S += c_t4101 >= 74
	c_t4101 += MAS[1]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 74
	c_t5000_in += MAS_in[1]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 74
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 74
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 75
	c_t4010_in += MAS_in[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 75
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 75
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t5000 = S.Task('c_t5000', length=2, delay_cost=1)
	S += c_t5000 >= 75
	c_t5000 += MAS[1]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 76
	c_t3001_in += MAS_in[0]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 76
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 76
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t4010 = S.Task('c_t4010', length=2, delay_cost=1)
	S += c_t4010 >= 76
	c_t4010 += MAS[1]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 77
	c_t2_t1_t2_in += MAS_in[0]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 77
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 77
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=2, delay_cost=1)
	S += c_t3001 >= 77
	c_t3001 += MAS[0]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=2, delay_cost=1)
	S += c_t2_t1_t2 >= 78
	c_t2_t1_t2 += MAS[0]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 78
	c_t4111_in += MAS_in[2]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 78
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 78
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 79
	c_t3110_in += MAS_in[1]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 79
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 79
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t4111 = S.Task('c_t4111', length=2, delay_cost=1)
	S += c_t4111 >= 79
	c_t4111 += MAS[2]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 80
	c_t3100_in += MAS_in[2]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 80
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 80
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t3110 = S.Task('c_t3110', length=2, delay_cost=1)
	S += c_t3110 >= 80
	c_t3110 += MAS[1]

	c_t3100 = S.Task('c_t3100', length=2, delay_cost=1)
	S += c_t3100 >= 81
	c_t3100 += MAS[2]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 81
	c_t4011_in += MAS_in[2]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 81
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 81
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4011 = S.Task('c_t4011', length=2, delay_cost=1)
	S += c_t4011 >= 82
	c_t4011 += MAS[2]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 82
	c_t4110_in += MAS_in[2]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 82
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 82
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 83
	c_t2_t21_in += MAS_in[0]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 83
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 83
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t4110 = S.Task('c_t4110', length=2, delay_cost=1)
	S += c_t4110 >= 83
	c_t4110 += MAS[2]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 84
	c_t2_t20_in += MAS_in[1]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 84
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 84
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t21 = S.Task('c_t2_t21', length=2, delay_cost=1)
	S += c_t2_t21 >= 84
	c_t2_t21 += MAS[0]

	c_t2_t20 = S.Task('c_t2_t20', length=2, delay_cost=1)
	S += c_t2_t20 >= 85
	c_t2_t20 += MAS[1]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 85
	c_t4001_in += MAS_in[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 85
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 85
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 86
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 86
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 86
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t4001 = S.Task('c_t4001', length=2, delay_cost=1)
	S += c_t4001 >= 86
	c_t4001 += MAS[1]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 87
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 87
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 87
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=9, delay_cost=1)
	S += c_t2_t1_t1 >= 87
	c_t2_t1_t1 += MM[0]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 88
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 88
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 88
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=9, delay_cost=1)
	S += c_t2_t1_t0 >= 88
	c_t2_t1_t0 += MM[0]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 89
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 89
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 89
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=9, delay_cost=1)
	S += c_t2_t0_t1 >= 89
	c_t2_t0_t1 += MM[0]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=9, delay_cost=1)
	S += c_t2_t0_t0 >= 90
	c_t2_t0_t0 += MM[0]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 90
	c_t5010_in += MAS_in[0]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 90
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 90
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5010 = S.Task('c_t5010', length=2, delay_cost=1)
	S += c_t5010 >= 91
	c_t5010 += MAS[0]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 91
	c_t5011_in += MAS_in[2]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 91
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 91
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=2, delay_cost=1)
	S += c_t5011 >= 92
	c_t5011 += MAS[2]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 92
	c_t5101_in += MAS_in[2]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 92
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 92
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5101 = S.Task('c_t5101', length=2, delay_cost=1)
	S += c_t5101 >= 93
	c_t5101 += MAS[2]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 93
	c_t5110_in += MAS_in[0]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 93
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 93
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 94
	c_t5100_in += MAS_in[1]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 94
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 94
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5110 = S.Task('c_t5110', length=2, delay_cost=1)
	S += c_t5110 >= 94
	c_t5110 += MAS[0]

	c_t5100 = S.Task('c_t5100', length=2, delay_cost=1)
	S += c_t5100 >= 95
	c_t5100 += MAS[1]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 95
	c_t5111_in += MAS_in[2]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 95
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 95
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5111 = S.Task('c_t5111', length=2, delay_cost=1)
	S += c_t5111 >= 96
	c_t5111 += MAS[2]


	# new tasks
	d_t0_t00 = S.Task('d_t0_t00', length=2, delay_cost=1)
	d_t0_t00 += alt(MAS)
	d_t0_t00_in = S.Task('d_t0_t00_in', length=1, delay_cost=1)
	d_t0_t00_in += alt(MAS_in)
	S += d_t0_t00_in*MAS_in[0]<=d_t0_t00*MAS[0]

	S += d_t0_t00_in*MAS_in[1]<=d_t0_t00*MAS[1]

	S += d_t0_t00_in*MAS_in[2]<=d_t0_t00*MAS[2]

	d_t0_t00_mem0 = S.Task('d_t0_t00_mem0', length=1, delay_cost=1)
	d_t0_t00_mem0 += MAIN_MEM_r[0]
	S += d_t0_t00_mem0 <= d_t0_t00

	d_t0_t00_mem1 = S.Task('d_t0_t00_mem1', length=1, delay_cost=1)
	d_t0_t00_mem1 += MAS_MEM[1]
	S += 19 < d_t0_t00_mem1
	S += d_t0_t00_mem1 <= d_t0_t00

	d_t0_t01 = S.Task('d_t0_t01', length=2, delay_cost=1)
	d_t0_t01 += alt(MAS)
	d_t0_t01_in = S.Task('d_t0_t01_in', length=1, delay_cost=1)
	d_t0_t01_in += alt(MAS_in)
	S += d_t0_t01_in*MAS_in[0]<=d_t0_t01*MAS[0]

	S += d_t0_t01_in*MAS_in[1]<=d_t0_t01*MAS[1]

	S += d_t0_t01_in*MAS_in[2]<=d_t0_t01*MAS[2]

	d_t0_t01_mem0 = S.Task('d_t0_t01_mem0', length=1, delay_cost=1)
	d_t0_t01_mem0 += MAIN_MEM_r[0]
	S += d_t0_t01_mem0 <= d_t0_t01

	d_t0_t01_mem1 = S.Task('d_t0_t01_mem1', length=1, delay_cost=1)
	d_t0_t01_mem1 += MAS_MEM[1]
	S += 11 < d_t0_t01_mem1
	S += d_t0_t01_mem1 <= d_t0_t01

	d_t0_t2_t3 = S.Task('d_t0_t2_t3', length=2, delay_cost=1)
	d_t0_t2_t3 += alt(MAS)
	d_t0_t2_t3_in = S.Task('d_t0_t2_t3_in', length=1, delay_cost=1)
	d_t0_t2_t3_in += alt(MAS_in)
	S += d_t0_t2_t3_in*MAS_in[0]<=d_t0_t2_t3*MAS[0]

	S += d_t0_t2_t3_in*MAS_in[1]<=d_t0_t2_t3*MAS[1]

	S += d_t0_t2_t3_in*MAS_in[2]<=d_t0_t2_t3*MAS[2]

	d_t0_t2_t3_mem0 = S.Task('d_t0_t2_t3_mem0', length=1, delay_cost=1)
	d_t0_t2_t3_mem0 += MAS_MEM[2]
	S += 10 < d_t0_t2_t3_mem0
	S += d_t0_t2_t3_mem0 <= d_t0_t2_t3

	d_t0_t2_t3_mem1 = S.Task('d_t0_t2_t3_mem1', length=1, delay_cost=1)
	d_t0_t2_t3_mem1 += MAS_MEM[1]
	S += 4 < d_t0_t2_t3_mem1
	S += d_t0_t2_t3_mem1 <= d_t0_t2_t3

	d_t0_t3_t4 = S.Task('d_t0_t3_t4', length=9, delay_cost=1)
	d_t0_t3_t4 += alt(MM)
	d_t0_t3_t4_in = S.Task('d_t0_t3_t4_in', length=1, delay_cost=1)
	d_t0_t3_t4_in += alt(MM_in)
	S += d_t0_t3_t4_in*MM_in[0]<=d_t0_t3_t4*MM[0]
	d_t0_t3_t4_mem0 = S.Task('d_t0_t3_t4_mem0', length=1, delay_cost=1)
	d_t0_t3_t4_mem0 += MAS_MEM[0]
	S += 3 < d_t0_t3_t4_mem0
	S += d_t0_t3_t4_mem0 <= d_t0_t3_t4

	d_t0_t3_t4_mem1 = S.Task('d_t0_t3_t4_mem1', length=1, delay_cost=1)
	d_t0_t3_t4_mem1 += MAS_MEM[1]
	S += 2 < d_t0_t3_t4_mem1
	S += d_t0_t3_t4_mem1 <= d_t0_t3_t4

	d_t0_t30 = S.Task('d_t0_t30', length=2, delay_cost=1)
	d_t0_t30 += alt(MAS)
	d_t0_t30_in = S.Task('d_t0_t30_in', length=1, delay_cost=1)
	d_t0_t30_in += alt(MAS_in)
	S += d_t0_t30_in*MAS_in[0]<=d_t0_t30*MAS[0]

	S += d_t0_t30_in*MAS_in[1]<=d_t0_t30*MAS[1]

	S += d_t0_t30_in*MAS_in[2]<=d_t0_t30*MAS[2]

	d_t0_t30_mem0 = S.Task('d_t0_t30_mem0', length=1, delay_cost=1)
	d_t0_t30_mem0 += MM_MEM[0]
	S += 38 < d_t0_t30_mem0
	S += d_t0_t30_mem0 <= d_t0_t30

	d_t0_t30_mem1 = S.Task('d_t0_t30_mem1', length=1, delay_cost=1)
	d_t0_t30_mem1 += MM_MEM[1]
	S += 37 < d_t0_t30_mem1
	S += d_t0_t30_mem1 <= d_t0_t30

	d_t0_t3_t5 = S.Task('d_t0_t3_t5', length=2, delay_cost=1)
	d_t0_t3_t5 += alt(MAS)
	d_t0_t3_t5_in = S.Task('d_t0_t3_t5_in', length=1, delay_cost=1)
	d_t0_t3_t5_in += alt(MAS_in)
	S += d_t0_t3_t5_in*MAS_in[0]<=d_t0_t3_t5*MAS[0]

	S += d_t0_t3_t5_in*MAS_in[1]<=d_t0_t3_t5*MAS[1]

	S += d_t0_t3_t5_in*MAS_in[2]<=d_t0_t3_t5*MAS[2]

	d_t0_t3_t5_mem0 = S.Task('d_t0_t3_t5_mem0', length=1, delay_cost=1)
	d_t0_t3_t5_mem0 += MM_MEM[0]
	S += 38 < d_t0_t3_t5_mem0
	S += d_t0_t3_t5_mem0 <= d_t0_t3_t5

	d_t0_t3_t5_mem1 = S.Task('d_t0_t3_t5_mem1', length=1, delay_cost=1)
	d_t0_t3_t5_mem1 += MM_MEM[1]
	S += 37 < d_t0_t3_t5_mem1
	S += d_t0_t3_t5_mem1 <= d_t0_t3_t5

	d_t1_t00 = S.Task('d_t1_t00', length=2, delay_cost=1)
	d_t1_t00 += alt(MAS)
	d_t1_t00_in = S.Task('d_t1_t00_in', length=1, delay_cost=1)
	d_t1_t00_in += alt(MAS_in)
	S += d_t1_t00_in*MAS_in[0]<=d_t1_t00*MAS[0]

	S += d_t1_t00_in*MAS_in[1]<=d_t1_t00*MAS[1]

	S += d_t1_t00_in*MAS_in[2]<=d_t1_t00*MAS[2]

	d_t1_t00_mem0 = S.Task('d_t1_t00_mem0', length=1, delay_cost=1)
	d_t1_t00_mem0 += MAIN_MEM_r[0]
	S += d_t1_t00_mem0 <= d_t1_t00

	d_t1_t00_mem1 = S.Task('d_t1_t00_mem1', length=1, delay_cost=1)
	d_t1_t00_mem1 += MAS_MEM[1]
	S += 7 < d_t1_t00_mem1
	S += d_t1_t00_mem1 <= d_t1_t00

	d_t1_t01 = S.Task('d_t1_t01', length=2, delay_cost=1)
	d_t1_t01 += alt(MAS)
	d_t1_t01_in = S.Task('d_t1_t01_in', length=1, delay_cost=1)
	d_t1_t01_in += alt(MAS_in)
	S += d_t1_t01_in*MAS_in[0]<=d_t1_t01*MAS[0]

	S += d_t1_t01_in*MAS_in[1]<=d_t1_t01*MAS[1]

	S += d_t1_t01_in*MAS_in[2]<=d_t1_t01*MAS[2]

	d_t1_t01_mem0 = S.Task('d_t1_t01_mem0', length=1, delay_cost=1)
	d_t1_t01_mem0 += MAIN_MEM_r[0]
	S += d_t1_t01_mem0 <= d_t1_t01

	d_t1_t01_mem1 = S.Task('d_t1_t01_mem1', length=1, delay_cost=1)
	d_t1_t01_mem1 += MAS_MEM[3]
	S += 18 < d_t1_t01_mem1
	S += d_t1_t01_mem1 <= d_t1_t01

	d_t1_t2_t3 = S.Task('d_t1_t2_t3', length=2, delay_cost=1)
	d_t1_t2_t3 += alt(MAS)
	d_t1_t2_t3_in = S.Task('d_t1_t2_t3_in', length=1, delay_cost=1)
	d_t1_t2_t3_in += alt(MAS_in)
	S += d_t1_t2_t3_in*MAS_in[0]<=d_t1_t2_t3*MAS[0]

	S += d_t1_t2_t3_in*MAS_in[1]<=d_t1_t2_t3*MAS[1]

	S += d_t1_t2_t3_in*MAS_in[2]<=d_t1_t2_t3*MAS[2]

	d_t1_t2_t3_mem0 = S.Task('d_t1_t2_t3_mem0', length=1, delay_cost=1)
	d_t1_t2_t3_mem0 += MAS_MEM[0]
	S += 9 < d_t1_t2_t3_mem0
	S += d_t1_t2_t3_mem0 <= d_t1_t2_t3

	d_t1_t2_t3_mem1 = S.Task('d_t1_t2_t3_mem1', length=1, delay_cost=1)
	d_t1_t2_t3_mem1 += MAS_MEM[1]
	S += 25 < d_t1_t2_t3_mem1
	S += d_t1_t2_t3_mem1 <= d_t1_t2_t3

	d_t1_t3_t4 = S.Task('d_t1_t3_t4', length=9, delay_cost=1)
	d_t1_t3_t4 += alt(MM)
	d_t1_t3_t4_in = S.Task('d_t1_t3_t4_in', length=1, delay_cost=1)
	d_t1_t3_t4_in += alt(MM_in)
	S += d_t1_t3_t4_in*MM_in[0]<=d_t1_t3_t4*MM[0]
	d_t1_t3_t4_mem0 = S.Task('d_t1_t3_t4_mem0', length=1, delay_cost=1)
	d_t1_t3_t4_mem0 += MAS_MEM[4]
	S += 16 < d_t1_t3_t4_mem0
	S += d_t1_t3_t4_mem0 <= d_t1_t3_t4

	d_t1_t3_t4_mem1 = S.Task('d_t1_t3_t4_mem1', length=1, delay_cost=1)
	d_t1_t3_t4_mem1 += MAS_MEM[1]
	S += 26 < d_t1_t3_t4_mem1
	S += d_t1_t3_t4_mem1 <= d_t1_t3_t4

	d_t1_t30 = S.Task('d_t1_t30', length=2, delay_cost=1)
	d_t1_t30 += alt(MAS)
	d_t1_t30_in = S.Task('d_t1_t30_in', length=1, delay_cost=1)
	d_t1_t30_in += alt(MAS_in)
	S += d_t1_t30_in*MAS_in[0]<=d_t1_t30*MAS[0]

	S += d_t1_t30_in*MAS_in[1]<=d_t1_t30*MAS[1]

	S += d_t1_t30_in*MAS_in[2]<=d_t1_t30*MAS[2]

	d_t1_t30_mem0 = S.Task('d_t1_t30_mem0', length=1, delay_cost=1)
	d_t1_t30_mem0 += MM_MEM[0]
	S += 36 < d_t1_t30_mem0
	S += d_t1_t30_mem0 <= d_t1_t30

	d_t1_t30_mem1 = S.Task('d_t1_t30_mem1', length=1, delay_cost=1)
	d_t1_t30_mem1 += MM_MEM[1]
	S += 35 < d_t1_t30_mem1
	S += d_t1_t30_mem1 <= d_t1_t30

	d_t1_t3_t5 = S.Task('d_t1_t3_t5', length=2, delay_cost=1)
	d_t1_t3_t5 += alt(MAS)
	d_t1_t3_t5_in = S.Task('d_t1_t3_t5_in', length=1, delay_cost=1)
	d_t1_t3_t5_in += alt(MAS_in)
	S += d_t1_t3_t5_in*MAS_in[0]<=d_t1_t3_t5*MAS[0]

	S += d_t1_t3_t5_in*MAS_in[1]<=d_t1_t3_t5*MAS[1]

	S += d_t1_t3_t5_in*MAS_in[2]<=d_t1_t3_t5*MAS[2]

	d_t1_t3_t5_mem0 = S.Task('d_t1_t3_t5_mem0', length=1, delay_cost=1)
	d_t1_t3_t5_mem0 += MM_MEM[0]
	S += 36 < d_t1_t3_t5_mem0
	S += d_t1_t3_t5_mem0 <= d_t1_t3_t5

	d_t1_t3_t5_mem1 = S.Task('d_t1_t3_t5_mem1', length=1, delay_cost=1)
	d_t1_t3_t5_mem1 += MM_MEM[1]
	S += 35 < d_t1_t3_t5_mem1
	S += d_t1_t3_t5_mem1 <= d_t1_t3_t5

	d_t2_t00 = S.Task('d_t2_t00', length=2, delay_cost=1)
	d_t2_t00 += alt(MAS)
	d_t2_t00_in = S.Task('d_t2_t00_in', length=1, delay_cost=1)
	d_t2_t00_in += alt(MAS_in)
	S += d_t2_t00_in*MAS_in[0]<=d_t2_t00*MAS[0]

	S += d_t2_t00_in*MAS_in[1]<=d_t2_t00*MAS[1]

	S += d_t2_t00_in*MAS_in[2]<=d_t2_t00*MAS[2]

	d_t2_t00_mem0 = S.Task('d_t2_t00_mem0', length=1, delay_cost=1)
	d_t2_t00_mem0 += MAIN_MEM_r[0]
	S += d_t2_t00_mem0 <= d_t2_t00

	d_t2_t00_mem1 = S.Task('d_t2_t00_mem1', length=1, delay_cost=1)
	d_t2_t00_mem1 += MAS_MEM[1]
	S += 5 < d_t2_t00_mem1
	S += d_t2_t00_mem1 <= d_t2_t00

	d_t2_t01 = S.Task('d_t2_t01', length=2, delay_cost=1)
	d_t2_t01 += alt(MAS)
	d_t2_t01_in = S.Task('d_t2_t01_in', length=1, delay_cost=1)
	d_t2_t01_in += alt(MAS_in)
	S += d_t2_t01_in*MAS_in[0]<=d_t2_t01*MAS[0]

	S += d_t2_t01_in*MAS_in[1]<=d_t2_t01*MAS[1]

	S += d_t2_t01_in*MAS_in[2]<=d_t2_t01*MAS[2]

	d_t2_t01_mem0 = S.Task('d_t2_t01_mem0', length=1, delay_cost=1)
	d_t2_t01_mem0 += MAIN_MEM_r[0]
	S += d_t2_t01_mem0 <= d_t2_t01

	d_t2_t01_mem1 = S.Task('d_t2_t01_mem1', length=1, delay_cost=1)
	d_t2_t01_mem1 += MAS_MEM[1]
	S += 17 < d_t2_t01_mem1
	S += d_t2_t01_mem1 <= d_t2_t01

	d_t2_t2_t3 = S.Task('d_t2_t2_t3', length=2, delay_cost=1)
	d_t2_t2_t3 += alt(MAS)
	d_t2_t2_t3_in = S.Task('d_t2_t2_t3_in', length=1, delay_cost=1)
	d_t2_t2_t3_in += alt(MAS_in)
	S += d_t2_t2_t3_in*MAS_in[0]<=d_t2_t2_t3*MAS[0]

	S += d_t2_t2_t3_in*MAS_in[1]<=d_t2_t2_t3*MAS[1]

	S += d_t2_t2_t3_in*MAS_in[2]<=d_t2_t2_t3*MAS[2]

	d_t2_t2_t3_mem0 = S.Task('d_t2_t2_t3_mem0', length=1, delay_cost=1)
	d_t2_t2_t3_mem0 += MAS_MEM[0]
	S += 20 < d_t2_t2_t3_mem0
	S += d_t2_t2_t3_mem0 <= d_t2_t2_t3

	d_t2_t2_t3_mem1 = S.Task('d_t2_t2_t3_mem1', length=1, delay_cost=1)
	d_t2_t2_t3_mem1 += MAS_MEM[1]
	S += 6 < d_t2_t2_t3_mem1
	S += d_t2_t2_t3_mem1 <= d_t2_t2_t3

	d_t2_t3_t4 = S.Task('d_t2_t3_t4', length=9, delay_cost=1)
	d_t2_t3_t4 += alt(MM)
	d_t2_t3_t4_in = S.Task('d_t2_t3_t4_in', length=1, delay_cost=1)
	d_t2_t3_t4_in += alt(MM_in)
	S += d_t2_t3_t4_in*MM_in[0]<=d_t2_t3_t4*MM[0]
	d_t2_t3_t4_mem0 = S.Task('d_t2_t3_t4_mem0', length=1, delay_cost=1)
	d_t2_t3_t4_mem0 += MAS_MEM[2]
	S += 12 < d_t2_t3_t4_mem0
	S += d_t2_t3_t4_mem0 <= d_t2_t3_t4

	d_t2_t3_t4_mem1 = S.Task('d_t2_t3_t4_mem1', length=1, delay_cost=1)
	d_t2_t3_t4_mem1 += MAS_MEM[3]
	S += 24 < d_t2_t3_t4_mem1
	S += d_t2_t3_t4_mem1 <= d_t2_t3_t4

	d_t2_t30 = S.Task('d_t2_t30', length=2, delay_cost=1)
	d_t2_t30 += alt(MAS)
	d_t2_t30_in = S.Task('d_t2_t30_in', length=1, delay_cost=1)
	d_t2_t30_in += alt(MAS_in)
	S += d_t2_t30_in*MAS_in[0]<=d_t2_t30*MAS[0]

	S += d_t2_t30_in*MAS_in[1]<=d_t2_t30*MAS[1]

	S += d_t2_t30_in*MAS_in[2]<=d_t2_t30*MAS[2]

	d_t2_t30_mem0 = S.Task('d_t2_t30_mem0', length=1, delay_cost=1)
	d_t2_t30_mem0 += MM_MEM[0]
	S += 34 < d_t2_t30_mem0
	S += d_t2_t30_mem0 <= d_t2_t30

	d_t2_t30_mem1 = S.Task('d_t2_t30_mem1', length=1, delay_cost=1)
	d_t2_t30_mem1 += MM_MEM[1]
	S += 22 < d_t2_t30_mem1
	S += d_t2_t30_mem1 <= d_t2_t30

	d_t2_t3_t5 = S.Task('d_t2_t3_t5', length=2, delay_cost=1)
	d_t2_t3_t5 += alt(MAS)
	d_t2_t3_t5_in = S.Task('d_t2_t3_t5_in', length=1, delay_cost=1)
	d_t2_t3_t5_in += alt(MAS_in)
	S += d_t2_t3_t5_in*MAS_in[0]<=d_t2_t3_t5*MAS[0]

	S += d_t2_t3_t5_in*MAS_in[1]<=d_t2_t3_t5*MAS[1]

	S += d_t2_t3_t5_in*MAS_in[2]<=d_t2_t3_t5*MAS[2]

	d_t2_t3_t5_mem0 = S.Task('d_t2_t3_t5_mem0', length=1, delay_cost=1)
	d_t2_t3_t5_mem0 += MM_MEM[0]
	S += 34 < d_t2_t3_t5_mem0
	S += d_t2_t3_t5_mem0 <= d_t2_t3_t5

	d_t2_t3_t5_mem1 = S.Task('d_t2_t3_t5_mem1', length=1, delay_cost=1)
	d_t2_t3_t5_mem1 += MM_MEM[1]
	S += 22 < d_t2_t3_t5_mem1
	S += d_t2_t3_t5_mem1 <= d_t2_t3_t5

	d_t3_a1_0 = S.Task('d_t3_a1_0', length=2, delay_cost=1)
	d_t3_a1_0 += alt(MAS)
	d_t3_a1_0_in = S.Task('d_t3_a1_0_in', length=1, delay_cost=1)
	d_t3_a1_0_in += alt(MAS_in)
	S += d_t3_a1_0_in*MAS_in[0]<=d_t3_a1_0*MAS[0]

	S += d_t3_a1_0_in*MAS_in[1]<=d_t3_a1_0*MAS[1]

	S += d_t3_a1_0_in*MAS_in[2]<=d_t3_a1_0*MAS[2]

	d_t3_a1_0_mem0 = S.Task('d_t3_a1_0_mem0', length=1, delay_cost=1)
	d_t3_a1_0_mem0 += MAS_MEM[2]
	S += 21 < d_t3_a1_0_mem0
	S += d_t3_a1_0_mem0 <= d_t3_a1_0

	d_t3_a1_0_mem1 = S.Task('d_t3_a1_0_mem1', length=1, delay_cost=1)
	d_t3_a1_0_mem1 += MAS_MEM[1]
	S += 8 < d_t3_a1_0_mem1
	S += d_t3_a1_0_mem1 <= d_t3_a1_0

	d_t3_a1_1 = S.Task('d_t3_a1_1', length=2, delay_cost=1)
	d_t3_a1_1 += alt(MAS)
	d_t3_a1_1_in = S.Task('d_t3_a1_1_in', length=1, delay_cost=1)
	d_t3_a1_1_in += alt(MAS_in)
	S += d_t3_a1_1_in*MAS_in[0]<=d_t3_a1_1*MAS[0]

	S += d_t3_a1_1_in*MAS_in[1]<=d_t3_a1_1*MAS[1]

	S += d_t3_a1_1_in*MAS_in[2]<=d_t3_a1_1*MAS[2]

	d_t3_a1_1_mem0 = S.Task('d_t3_a1_1_mem0', length=1, delay_cost=1)
	d_t3_a1_1_mem0 += MAS_MEM[0]
	S += 8 < d_t3_a1_1_mem0
	S += d_t3_a1_1_mem0 <= d_t3_a1_1

	d_t3_a1_1_mem1 = S.Task('d_t3_a1_1_mem1', length=1, delay_cost=1)
	d_t3_a1_1_mem1 += MAS_MEM[3]
	S += 21 < d_t3_a1_1_mem1
	S += d_t3_a1_1_mem1 <= d_t3_a1_1

	d_t3_t10 = S.Task('d_t3_t10', length=2, delay_cost=1)
	d_t3_t10 += alt(MAS)
	d_t3_t10_in = S.Task('d_t3_t10_in', length=1, delay_cost=1)
	d_t3_t10_in += alt(MAS_in)
	S += d_t3_t10_in*MAS_in[0]<=d_t3_t10*MAS[0]

	S += d_t3_t10_in*MAS_in[1]<=d_t3_t10*MAS[1]

	S += d_t3_t10_in*MAS_in[2]<=d_t3_t10*MAS[2]

	d_t3_t10_mem0 = S.Task('d_t3_t10_mem0', length=1, delay_cost=1)
	d_t3_t10_mem0 += MAS_MEM[0]
	S += 22 < d_t3_t10_mem0
	S += d_t3_t10_mem0 <= d_t3_t10

	d_t3_t10_mem1 = S.Task('d_t3_t10_mem1', length=1, delay_cost=1)
	d_t3_t10_mem1 += MAS_MEM[3]
	S += 21 < d_t3_t10_mem1
	S += d_t3_t10_mem1 <= d_t3_t10

	d_t3_t11 = S.Task('d_t3_t11', length=2, delay_cost=1)
	d_t3_t11 += alt(MAS)
	d_t3_t11_in = S.Task('d_t3_t11_in', length=1, delay_cost=1)
	d_t3_t11_in += alt(MAS_in)
	S += d_t3_t11_in*MAS_in[0]<=d_t3_t11*MAS[0]

	S += d_t3_t11_in*MAS_in[1]<=d_t3_t11*MAS[1]

	S += d_t3_t11_in*MAS_in[2]<=d_t3_t11*MAS[2]

	d_t3_t11_mem0 = S.Task('d_t3_t11_mem0', length=1, delay_cost=1)
	d_t3_t11_mem0 += MAS_MEM[2]
	S += 13 < d_t3_t11_mem0
	S += d_t3_t11_mem0 <= d_t3_t11

	d_t3_t11_mem1 = S.Task('d_t3_t11_mem1', length=1, delay_cost=1)
	d_t3_t11_mem1 += MAS_MEM[1]
	S += 8 < d_t3_t11_mem1
	S += d_t3_t11_mem1 <= d_t3_t11

	d_t3_t3_t0 = S.Task('d_t3_t3_t0', length=9, delay_cost=1)
	d_t3_t3_t0 += alt(MM)
	d_t3_t3_t0_in = S.Task('d_t3_t3_t0_in', length=1, delay_cost=1)
	d_t3_t3_t0_in += alt(MM_in)
	S += d_t3_t3_t0_in*MM_in[0]<=d_t3_t3_t0*MM[0]
	d_t3_t3_t0_mem0 = S.Task('d_t3_t3_t0_mem0', length=1, delay_cost=1)
	d_t3_t3_t0_mem0 += MAS_MEM[0]
	S += 22 < d_t3_t3_t0_mem0
	S += d_t3_t3_t0_mem0 <= d_t3_t3_t0

	d_t3_t3_t0_mem1 = S.Task('d_t3_t3_t0_mem1', length=1, delay_cost=1)
	d_t3_t3_t0_mem1 += MAS_MEM[3]
	S += 21 < d_t3_t3_t0_mem1
	S += d_t3_t3_t0_mem1 <= d_t3_t3_t0

	d_t3_t3_t1 = S.Task('d_t3_t3_t1', length=9, delay_cost=1)
	d_t3_t3_t1 += alt(MM)
	d_t3_t3_t1_in = S.Task('d_t3_t3_t1_in', length=1, delay_cost=1)
	d_t3_t3_t1_in += alt(MM_in)
	S += d_t3_t3_t1_in*MM_in[0]<=d_t3_t3_t1*MM[0]
	d_t3_t3_t1_mem0 = S.Task('d_t3_t3_t1_mem0', length=1, delay_cost=1)
	d_t3_t3_t1_mem0 += MAS_MEM[2]
	S += 13 < d_t3_t3_t1_mem0
	S += d_t3_t3_t1_mem0 <= d_t3_t3_t1

	d_t3_t3_t1_mem1 = S.Task('d_t3_t3_t1_mem1', length=1, delay_cost=1)
	d_t3_t3_t1_mem1 += MAS_MEM[1]
	S += 8 < d_t3_t3_t1_mem1
	S += d_t3_t3_t1_mem1 <= d_t3_t3_t1

	d_t3_t3_t2 = S.Task('d_t3_t3_t2', length=2, delay_cost=1)
	d_t3_t3_t2 += alt(MAS)
	d_t3_t3_t2_in = S.Task('d_t3_t3_t2_in', length=1, delay_cost=1)
	d_t3_t3_t2_in += alt(MAS_in)
	S += d_t3_t3_t2_in*MAS_in[0]<=d_t3_t3_t2*MAS[0]

	S += d_t3_t3_t2_in*MAS_in[1]<=d_t3_t3_t2*MAS[1]

	S += d_t3_t3_t2_in*MAS_in[2]<=d_t3_t3_t2*MAS[2]

	d_t3_t3_t2_mem0 = S.Task('d_t3_t3_t2_mem0', length=1, delay_cost=1)
	d_t3_t3_t2_mem0 += MAS_MEM[0]
	S += 22 < d_t3_t3_t2_mem0
	S += d_t3_t3_t2_mem0 <= d_t3_t3_t2

	d_t3_t3_t2_mem1 = S.Task('d_t3_t3_t2_mem1', length=1, delay_cost=1)
	d_t3_t3_t2_mem1 += MAS_MEM[3]
	S += 13 < d_t3_t3_t2_mem1
	S += d_t3_t3_t2_mem1 <= d_t3_t3_t2

	d_t3_t3_t3 = S.Task('d_t3_t3_t3', length=2, delay_cost=1)
	d_t3_t3_t3 += alt(MAS)
	d_t3_t3_t3_in = S.Task('d_t3_t3_t3_in', length=1, delay_cost=1)
	d_t3_t3_t3_in += alt(MAS_in)
	S += d_t3_t3_t3_in*MAS_in[0]<=d_t3_t3_t3*MAS[0]

	S += d_t3_t3_t3_in*MAS_in[1]<=d_t3_t3_t3*MAS[1]

	S += d_t3_t3_t3_in*MAS_in[2]<=d_t3_t3_t3*MAS[2]

	d_t3_t3_t3_mem0 = S.Task('d_t3_t3_t3_mem0', length=1, delay_cost=1)
	d_t3_t3_t3_mem0 += MAS_MEM[2]
	S += 21 < d_t3_t3_t3_mem0
	S += d_t3_t3_t3_mem0 <= d_t3_t3_t3

	d_t3_t3_t3_mem1 = S.Task('d_t3_t3_t3_mem1', length=1, delay_cost=1)
	d_t3_t3_t3_mem1 += MAS_MEM[1]
	S += 8 < d_t3_t3_t3_mem1
	S += d_t3_t3_t3_mem1 <= d_t3_t3_t3

	d_t4_a1_0 = S.Task('d_t4_a1_0', length=2, delay_cost=1)
	d_t4_a1_0 += alt(MAS)
	d_t4_a1_0_in = S.Task('d_t4_a1_0_in', length=1, delay_cost=1)
	d_t4_a1_0_in += alt(MAS_in)
	S += d_t4_a1_0_in*MAS_in[0]<=d_t4_a1_0*MAS[0]

	S += d_t4_a1_0_in*MAS_in[1]<=d_t4_a1_0*MAS[1]

	S += d_t4_a1_0_in*MAS_in[2]<=d_t4_a1_0*MAS[2]

	d_t4_a1_0_mem0 = S.Task('d_t4_a1_0_mem0', length=1, delay_cost=1)
	d_t4_a1_0_mem0 += MAS_MEM[0]
	S += 32 < d_t4_a1_0_mem0
	S += d_t4_a1_0_mem0 <= d_t4_a1_0

	d_t4_a1_0_mem1 = S.Task('d_t4_a1_0_mem1', length=1, delay_cost=1)
	d_t4_a1_0_mem1 += MAS_MEM[3]
	S += 50 < d_t4_a1_0_mem1
	S += d_t4_a1_0_mem1 <= d_t4_a1_0

	d_t4_a1_1 = S.Task('d_t4_a1_1', length=2, delay_cost=1)
	d_t4_a1_1 += alt(MAS)
	d_t4_a1_1_in = S.Task('d_t4_a1_1_in', length=1, delay_cost=1)
	d_t4_a1_1_in += alt(MAS_in)
	S += d_t4_a1_1_in*MAS_in[0]<=d_t4_a1_1*MAS[0]

	S += d_t4_a1_1_in*MAS_in[1]<=d_t4_a1_1*MAS[1]

	S += d_t4_a1_1_in*MAS_in[2]<=d_t4_a1_1*MAS[2]

	d_t4_a1_1_mem0 = S.Task('d_t4_a1_1_mem0', length=1, delay_cost=1)
	d_t4_a1_1_mem0 += MAS_MEM[2]
	S += 50 < d_t4_a1_1_mem0
	S += d_t4_a1_1_mem0 <= d_t4_a1_1

	d_t4_a1_1_mem1 = S.Task('d_t4_a1_1_mem1', length=1, delay_cost=1)
	d_t4_a1_1_mem1 += MAS_MEM[1]
	S += 32 < d_t4_a1_1_mem1
	S += d_t4_a1_1_mem1 <= d_t4_a1_1

	d_t4_t10 = S.Task('d_t4_t10', length=2, delay_cost=1)
	d_t4_t10 += alt(MAS)
	d_t4_t10_in = S.Task('d_t4_t10_in', length=1, delay_cost=1)
	d_t4_t10_in += alt(MAS_in)
	S += d_t4_t10_in*MAS_in[0]<=d_t4_t10*MAS[0]

	S += d_t4_t10_in*MAS_in[1]<=d_t4_t10*MAS[1]

	S += d_t4_t10_in*MAS_in[2]<=d_t4_t10*MAS[2]

	d_t4_t10_mem0 = S.Task('d_t4_t10_mem0', length=1, delay_cost=1)
	d_t4_t10_mem0 += MAS_MEM[2]
	S += 14 < d_t4_t10_mem0
	S += d_t4_t10_mem0 <= d_t4_t10

	d_t4_t10_mem1 = S.Task('d_t4_t10_mem1', length=1, delay_cost=1)
	d_t4_t10_mem1 += MAS_MEM[1]
	S += 32 < d_t4_t10_mem1
	S += d_t4_t10_mem1 <= d_t4_t10

	d_t4_t11 = S.Task('d_t4_t11', length=2, delay_cost=1)
	d_t4_t11 += alt(MAS)
	d_t4_t11_in = S.Task('d_t4_t11_in', length=1, delay_cost=1)
	d_t4_t11_in += alt(MAS_in)
	S += d_t4_t11_in*MAS_in[0]<=d_t4_t11*MAS[0]

	S += d_t4_t11_in*MAS_in[1]<=d_t4_t11*MAS[1]

	S += d_t4_t11_in*MAS_in[2]<=d_t4_t11*MAS[2]

	d_t4_t11_mem0 = S.Task('d_t4_t11_mem0', length=1, delay_cost=1)
	d_t4_t11_mem0 += MAS_MEM[2]
	S += 23 < d_t4_t11_mem0
	S += d_t4_t11_mem0 <= d_t4_t11

	d_t4_t11_mem1 = S.Task('d_t4_t11_mem1', length=1, delay_cost=1)
	d_t4_t11_mem1 += MAS_MEM[3]
	S += 50 < d_t4_t11_mem1
	S += d_t4_t11_mem1 <= d_t4_t11

	d_t4_t3_t0 = S.Task('d_t4_t3_t0', length=9, delay_cost=1)
	d_t4_t3_t0 += alt(MM)
	d_t4_t3_t0_in = S.Task('d_t4_t3_t0_in', length=1, delay_cost=1)
	d_t4_t3_t0_in += alt(MM_in)
	S += d_t4_t3_t0_in*MM_in[0]<=d_t4_t3_t0*MM[0]
	d_t4_t3_t0_mem0 = S.Task('d_t4_t3_t0_mem0', length=1, delay_cost=1)
	d_t4_t3_t0_mem0 += MAS_MEM[2]
	S += 14 < d_t4_t3_t0_mem0
	S += d_t4_t3_t0_mem0 <= d_t4_t3_t0

	d_t4_t3_t0_mem1 = S.Task('d_t4_t3_t0_mem1', length=1, delay_cost=1)
	d_t4_t3_t0_mem1 += MAS_MEM[1]
	S += 32 < d_t4_t3_t0_mem1
	S += d_t4_t3_t0_mem1 <= d_t4_t3_t0

	d_t4_t3_t1 = S.Task('d_t4_t3_t1', length=9, delay_cost=1)
	d_t4_t3_t1 += alt(MM)
	d_t4_t3_t1_in = S.Task('d_t4_t3_t1_in', length=1, delay_cost=1)
	d_t4_t3_t1_in += alt(MM_in)
	S += d_t4_t3_t1_in*MM_in[0]<=d_t4_t3_t1*MM[0]
	d_t4_t3_t1_mem0 = S.Task('d_t4_t3_t1_mem0', length=1, delay_cost=1)
	d_t4_t3_t1_mem0 += MAS_MEM[2]
	S += 23 < d_t4_t3_t1_mem0
	S += d_t4_t3_t1_mem0 <= d_t4_t3_t1

	d_t4_t3_t1_mem1 = S.Task('d_t4_t3_t1_mem1', length=1, delay_cost=1)
	d_t4_t3_t1_mem1 += MAS_MEM[3]
	S += 50 < d_t4_t3_t1_mem1
	S += d_t4_t3_t1_mem1 <= d_t4_t3_t1

	d_t4_t3_t2 = S.Task('d_t4_t3_t2', length=2, delay_cost=1)
	d_t4_t3_t2 += alt(MAS)
	d_t4_t3_t2_in = S.Task('d_t4_t3_t2_in', length=1, delay_cost=1)
	d_t4_t3_t2_in += alt(MAS_in)
	S += d_t4_t3_t2_in*MAS_in[0]<=d_t4_t3_t2*MAS[0]

	S += d_t4_t3_t2_in*MAS_in[1]<=d_t4_t3_t2*MAS[1]

	S += d_t4_t3_t2_in*MAS_in[2]<=d_t4_t3_t2*MAS[2]

	d_t4_t3_t2_mem0 = S.Task('d_t4_t3_t2_mem0', length=1, delay_cost=1)
	d_t4_t3_t2_mem0 += MAS_MEM[2]
	S += 14 < d_t4_t3_t2_mem0
	S += d_t4_t3_t2_mem0 <= d_t4_t3_t2

	d_t4_t3_t2_mem1 = S.Task('d_t4_t3_t2_mem1', length=1, delay_cost=1)
	d_t4_t3_t2_mem1 += MAS_MEM[3]
	S += 23 < d_t4_t3_t2_mem1
	S += d_t4_t3_t2_mem1 <= d_t4_t3_t2

	d_t4_t3_t3 = S.Task('d_t4_t3_t3', length=2, delay_cost=1)
	d_t4_t3_t3 += alt(MAS)
	d_t4_t3_t3_in = S.Task('d_t4_t3_t3_in', length=1, delay_cost=1)
	d_t4_t3_t3_in += alt(MAS_in)
	S += d_t4_t3_t3_in*MAS_in[0]<=d_t4_t3_t3*MAS[0]

	S += d_t4_t3_t3_in*MAS_in[1]<=d_t4_t3_t3*MAS[1]

	S += d_t4_t3_t3_in*MAS_in[2]<=d_t4_t3_t3*MAS[2]

	d_t4_t3_t3_mem0 = S.Task('d_t4_t3_t3_mem0', length=1, delay_cost=1)
	d_t4_t3_t3_mem0 += MAS_MEM[0]
	S += 32 < d_t4_t3_t3_mem0
	S += d_t4_t3_t3_mem0 <= d_t4_t3_t3

	d_t4_t3_t3_mem1 = S.Task('d_t4_t3_t3_mem1', length=1, delay_cost=1)
	d_t4_t3_t3_mem1 += MAS_MEM[3]
	S += 50 < d_t4_t3_t3_mem1
	S += d_t4_t3_t3_mem1 <= d_t4_t3_t3

	d_t5_a1_0 = S.Task('d_t5_a1_0', length=2, delay_cost=1)
	d_t5_a1_0 += alt(MAS)
	d_t5_a1_0_in = S.Task('d_t5_a1_0_in', length=1, delay_cost=1)
	d_t5_a1_0_in += alt(MAS_in)
	S += d_t5_a1_0_in*MAS_in[0]<=d_t5_a1_0*MAS[0]

	S += d_t5_a1_0_in*MAS_in[1]<=d_t5_a1_0*MAS[1]

	S += d_t5_a1_0_in*MAS_in[2]<=d_t5_a1_0*MAS[2]

	d_t5_a1_0_mem0 = S.Task('d_t5_a1_0_mem0', length=1, delay_cost=1)
	d_t5_a1_0_mem0 += MAS_MEM[0]
	S += 35 < d_t5_a1_0_mem0
	S += d_t5_a1_0_mem0 <= d_t5_a1_0

	d_t5_a1_0_mem1 = S.Task('d_t5_a1_0_mem1', length=1, delay_cost=1)
	d_t5_a1_0_mem1 += MAS_MEM[1]
	S += 39 < d_t5_a1_0_mem1
	S += d_t5_a1_0_mem1 <= d_t5_a1_0

	d_t5_a1_1 = S.Task('d_t5_a1_1', length=2, delay_cost=1)
	d_t5_a1_1 += alt(MAS)
	d_t5_a1_1_in = S.Task('d_t5_a1_1_in', length=1, delay_cost=1)
	d_t5_a1_1_in += alt(MAS_in)
	S += d_t5_a1_1_in*MAS_in[0]<=d_t5_a1_1*MAS[0]

	S += d_t5_a1_1_in*MAS_in[1]<=d_t5_a1_1*MAS[1]

	S += d_t5_a1_1_in*MAS_in[2]<=d_t5_a1_1*MAS[2]

	d_t5_a1_1_mem0 = S.Task('d_t5_a1_1_mem0', length=1, delay_cost=1)
	d_t5_a1_1_mem0 += MAS_MEM[0]
	S += 39 < d_t5_a1_1_mem0
	S += d_t5_a1_1_mem0 <= d_t5_a1_1

	d_t5_a1_1_mem1 = S.Task('d_t5_a1_1_mem1', length=1, delay_cost=1)
	d_t5_a1_1_mem1 += MAS_MEM[1]
	S += 35 < d_t5_a1_1_mem1
	S += d_t5_a1_1_mem1 <= d_t5_a1_1

	d_t5_t10 = S.Task('d_t5_t10', length=2, delay_cost=1)
	d_t5_t10 += alt(MAS)
	d_t5_t10_in = S.Task('d_t5_t10_in', length=1, delay_cost=1)
	d_t5_t10_in += alt(MAS_in)
	S += d_t5_t10_in*MAS_in[0]<=d_t5_t10*MAS[0]

	S += d_t5_t10_in*MAS_in[1]<=d_t5_t10*MAS[1]

	S += d_t5_t10_in*MAS_in[2]<=d_t5_t10*MAS[2]

	d_t5_t10_mem0 = S.Task('d_t5_t10_mem0', length=1, delay_cost=1)
	d_t5_t10_mem0 += MAS_MEM[0]
	S += 34 < d_t5_t10_mem0
	S += d_t5_t10_mem0 <= d_t5_t10

	d_t5_t10_mem1 = S.Task('d_t5_t10_mem1', length=1, delay_cost=1)
	d_t5_t10_mem1 += MAS_MEM[1]
	S += 35 < d_t5_t10_mem1
	S += d_t5_t10_mem1 <= d_t5_t10

	d_t5_t11 = S.Task('d_t5_t11', length=2, delay_cost=1)
	d_t5_t11 += alt(MAS)
	d_t5_t11_in = S.Task('d_t5_t11_in', length=1, delay_cost=1)
	d_t5_t11_in += alt(MAS_in)
	S += d_t5_t11_in*MAS_in[0]<=d_t5_t11*MAS[0]

	S += d_t5_t11_in*MAS_in[1]<=d_t5_t11*MAS[1]

	S += d_t5_t11_in*MAS_in[2]<=d_t5_t11*MAS[2]

	d_t5_t11_mem0 = S.Task('d_t5_t11_mem0', length=1, delay_cost=1)
	d_t5_t11_mem0 += MAS_MEM[4]
	S += 33 < d_t5_t11_mem0
	S += d_t5_t11_mem0 <= d_t5_t11

	d_t5_t11_mem1 = S.Task('d_t5_t11_mem1', length=1, delay_cost=1)
	d_t5_t11_mem1 += MAS_MEM[1]
	S += 39 < d_t5_t11_mem1
	S += d_t5_t11_mem1 <= d_t5_t11

	d_t5_t3_t0 = S.Task('d_t5_t3_t0', length=9, delay_cost=1)
	d_t5_t3_t0 += alt(MM)
	d_t5_t3_t0_in = S.Task('d_t5_t3_t0_in', length=1, delay_cost=1)
	d_t5_t3_t0_in += alt(MM_in)
	S += d_t5_t3_t0_in*MM_in[0]<=d_t5_t3_t0*MM[0]
	d_t5_t3_t0_mem0 = S.Task('d_t5_t3_t0_mem0', length=1, delay_cost=1)
	d_t5_t3_t0_mem0 += MAS_MEM[0]
	S += 34 < d_t5_t3_t0_mem0
	S += d_t5_t3_t0_mem0 <= d_t5_t3_t0

	d_t5_t3_t0_mem1 = S.Task('d_t5_t3_t0_mem1', length=1, delay_cost=1)
	d_t5_t3_t0_mem1 += MAS_MEM[1]
	S += 35 < d_t5_t3_t0_mem1
	S += d_t5_t3_t0_mem1 <= d_t5_t3_t0

	d_t5_t3_t1 = S.Task('d_t5_t3_t1', length=9, delay_cost=1)
	d_t5_t3_t1 += alt(MM)
	d_t5_t3_t1_in = S.Task('d_t5_t3_t1_in', length=1, delay_cost=1)
	d_t5_t3_t1_in += alt(MM_in)
	S += d_t5_t3_t1_in*MM_in[0]<=d_t5_t3_t1*MM[0]
	d_t5_t3_t1_mem0 = S.Task('d_t5_t3_t1_mem0', length=1, delay_cost=1)
	d_t5_t3_t1_mem0 += MAS_MEM[4]
	S += 33 < d_t5_t3_t1_mem0
	S += d_t5_t3_t1_mem0 <= d_t5_t3_t1

	d_t5_t3_t1_mem1 = S.Task('d_t5_t3_t1_mem1', length=1, delay_cost=1)
	d_t5_t3_t1_mem1 += MAS_MEM[1]
	S += 39 < d_t5_t3_t1_mem1
	S += d_t5_t3_t1_mem1 <= d_t5_t3_t1

	d_t5_t3_t2 = S.Task('d_t5_t3_t2', length=2, delay_cost=1)
	d_t5_t3_t2 += alt(MAS)
	d_t5_t3_t2_in = S.Task('d_t5_t3_t2_in', length=1, delay_cost=1)
	d_t5_t3_t2_in += alt(MAS_in)
	S += d_t5_t3_t2_in*MAS_in[0]<=d_t5_t3_t2*MAS[0]

	S += d_t5_t3_t2_in*MAS_in[1]<=d_t5_t3_t2*MAS[1]

	S += d_t5_t3_t2_in*MAS_in[2]<=d_t5_t3_t2*MAS[2]

	d_t5_t3_t2_mem0 = S.Task('d_t5_t3_t2_mem0', length=1, delay_cost=1)
	d_t5_t3_t2_mem0 += MAS_MEM[0]
	S += 34 < d_t5_t3_t2_mem0
	S += d_t5_t3_t2_mem0 <= d_t5_t3_t2

	d_t5_t3_t2_mem1 = S.Task('d_t5_t3_t2_mem1', length=1, delay_cost=1)
	d_t5_t3_t2_mem1 += MAS_MEM[5]
	S += 33 < d_t5_t3_t2_mem1
	S += d_t5_t3_t2_mem1 <= d_t5_t3_t2

	d_t5_t3_t3 = S.Task('d_t5_t3_t3', length=2, delay_cost=1)
	d_t5_t3_t3 += alt(MAS)
	d_t5_t3_t3_in = S.Task('d_t5_t3_t3_in', length=1, delay_cost=1)
	d_t5_t3_t3_in += alt(MAS_in)
	S += d_t5_t3_t3_in*MAS_in[0]<=d_t5_t3_t3*MAS[0]

	S += d_t5_t3_t3_in*MAS_in[1]<=d_t5_t3_t3*MAS[1]

	S += d_t5_t3_t3_in*MAS_in[2]<=d_t5_t3_t3*MAS[2]

	d_t5_t3_t3_mem0 = S.Task('d_t5_t3_t3_mem0', length=1, delay_cost=1)
	d_t5_t3_t3_mem0 += MAS_MEM[0]
	S += 35 < d_t5_t3_t3_mem0
	S += d_t5_t3_t3_mem0 <= d_t5_t3_t3

	d_t5_t3_t3_mem1 = S.Task('d_t5_t3_t3_mem1', length=1, delay_cost=1)
	d_t5_t3_t3_mem1 += MAS_MEM[1]
	S += 39 < d_t5_t3_t3_mem1
	S += d_t5_t3_t3_mem1 <= d_t5_t3_t3

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=9, delay_cost=1)
	c_t0_t0_t4 += alt(MM)
	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	c_t0_t0_t4_in += alt(MM_in)
	S += c_t0_t0_t4_in*MM_in[0]<=c_t0_t0_t4*MM[0]
	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	c_t0_t0_t4_mem0 += MAS_MEM[0]
	S += 38 < c_t0_t0_t4_mem0
	S += c_t0_t0_t4_mem0 <= c_t0_t0_t4

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	c_t0_t0_t4_mem1 += MAS_MEM[1]
	S += 36 < c_t0_t0_t4_mem1
	S += c_t0_t0_t4_mem1 <= c_t0_t0_t4

	c_t0_t00 = S.Task('c_t0_t00', length=2, delay_cost=1)
	c_t0_t00 += alt(MAS)
	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	c_t0_t00_in += alt(MAS_in)
	S += c_t0_t00_in*MAS_in[0]<=c_t0_t00*MAS[0]

	S += c_t0_t00_in*MAS_in[1]<=c_t0_t00*MAS[1]

	S += c_t0_t00_in*MAS_in[2]<=c_t0_t00*MAS[2]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	c_t0_t00_mem0 += MM_MEM[0]
	S += 66 < c_t0_t00_mem0
	S += c_t0_t00_mem0 <= c_t0_t00

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	c_t0_t00_mem1 += MM_MEM[1]
	S += 65 < c_t0_t00_mem1
	S += c_t0_t00_mem1 <= c_t0_t00

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=2, delay_cost=1)
	c_t0_t0_t5 += alt(MAS)
	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	c_t0_t0_t5_in += alt(MAS_in)
	S += c_t0_t0_t5_in*MAS_in[0]<=c_t0_t0_t5*MAS[0]

	S += c_t0_t0_t5_in*MAS_in[1]<=c_t0_t0_t5*MAS[1]

	S += c_t0_t0_t5_in*MAS_in[2]<=c_t0_t0_t5*MAS[2]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	c_t0_t0_t5_mem0 += MM_MEM[0]
	S += 66 < c_t0_t0_t5_mem0
	S += c_t0_t0_t5_mem0 <= c_t0_t0_t5

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	c_t0_t0_t5_mem1 += MM_MEM[1]
	S += 65 < c_t0_t0_t5_mem1
	S += c_t0_t0_t5_mem1 <= c_t0_t0_t5

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=9, delay_cost=1)
	c_t0_t1_t4 += alt(MM)
	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	c_t0_t1_t4_in += alt(MM_in)
	S += c_t0_t1_t4_in*MM_in[0]<=c_t0_t1_t4*MM[0]
	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	c_t0_t1_t4_mem0 += MAS_MEM[0]
	S += 41 < c_t0_t1_t4_mem0
	S += c_t0_t1_t4_mem0 <= c_t0_t1_t4

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	c_t0_t1_t4_mem1 += MAS_MEM[1]
	S += 44 < c_t0_t1_t4_mem1
	S += c_t0_t1_t4_mem1 <= c_t0_t1_t4

	c_t0_t10 = S.Task('c_t0_t10', length=2, delay_cost=1)
	c_t0_t10 += alt(MAS)
	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	c_t0_t10_in += alt(MAS_in)
	S += c_t0_t10_in*MAS_in[0]<=c_t0_t10*MAS[0]

	S += c_t0_t10_in*MAS_in[1]<=c_t0_t10*MAS[1]

	S += c_t0_t10_in*MAS_in[2]<=c_t0_t10*MAS[2]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	c_t0_t10_mem0 += MM_MEM[0]
	S += 63 < c_t0_t10_mem0
	S += c_t0_t10_mem0 <= c_t0_t10

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	c_t0_t10_mem1 += MM_MEM[1]
	S += 62 < c_t0_t10_mem1
	S += c_t0_t10_mem1 <= c_t0_t10

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=2, delay_cost=1)
	c_t0_t1_t5 += alt(MAS)
	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	c_t0_t1_t5_in += alt(MAS_in)
	S += c_t0_t1_t5_in*MAS_in[0]<=c_t0_t1_t5*MAS[0]

	S += c_t0_t1_t5_in*MAS_in[1]<=c_t0_t1_t5*MAS[1]

	S += c_t0_t1_t5_in*MAS_in[2]<=c_t0_t1_t5*MAS[2]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	c_t0_t1_t5_mem0 += MM_MEM[0]
	S += 63 < c_t0_t1_t5_mem0
	S += c_t0_t1_t5_mem0 <= c_t0_t1_t5

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	c_t0_t1_t5_mem1 += MM_MEM[1]
	S += 62 < c_t0_t1_t5_mem1
	S += c_t0_t1_t5_mem1 <= c_t0_t1_t5

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=9, delay_cost=1)
	c_t0_t4_t0 += alt(MM)
	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	c_t0_t4_t0_in += alt(MM_in)
	S += c_t0_t4_t0_in*MM_in[0]<=c_t0_t4_t0*MM[0]
	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	c_t0_t4_t0_mem0 += MAS_MEM[0]
	S += 37 < c_t0_t4_t0_mem0
	S += c_t0_t4_t0_mem0 <= c_t0_t4_t0

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	c_t0_t4_t0_mem1 += MAS_MEM[1]
	S += 42 < c_t0_t4_t0_mem1
	S += c_t0_t4_t0_mem1 <= c_t0_t4_t0

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=9, delay_cost=1)
	c_t0_t4_t1 += alt(MM)
	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	c_t0_t4_t1_in += alt(MM_in)
	S += c_t0_t4_t1_in*MM_in[0]<=c_t0_t4_t1*MM[0]
	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	c_t0_t4_t1_mem0 += MAS_MEM[0]
	S += 45 < c_t0_t4_t1_mem0
	S += c_t0_t4_t1_mem0 <= c_t0_t4_t1

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	c_t0_t4_t1_mem1 += MAS_MEM[1]
	S += 43 < c_t0_t4_t1_mem1
	S += c_t0_t4_t1_mem1 <= c_t0_t4_t1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM1_stage2MAS3/FP12_LADDERMUL/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 4))

	return solution

