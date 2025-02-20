from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 181
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=8)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 0
	d_t1_t3_t1_in += MM_in[1]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 0
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 0
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 1
	d_t1_t3_t0_in += MM_in[1]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 1
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 1
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=8, delay_cost=1)
	S += d_t1_t3_t1 >= 1
	d_t1_t3_t1 += MM[1]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=8, delay_cost=1)
	S += d_t1_t3_t0 >= 2
	d_t1_t3_t0 += MM[1]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 2
	d_t2_t3_t0_in += MM_in[1]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 2
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 2
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=8, delay_cost=1)
	S += d_t2_t3_t0 >= 3
	d_t2_t3_t0 += MM[1]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 3
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 3
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 3
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 4
	d_t0_t3_t1_in += MM_in[1]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 4
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 4
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=8, delay_cost=1)
	S += d_t2_t3_t1 >= 4
	d_t2_t3_t1 += MM[0]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 5
	d_t0_t3_t0_in += MM_in[1]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 5
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 5
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=8, delay_cost=1)
	S += d_t0_t3_t1 >= 5
	d_t0_t3_t1 += MM[1]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=8, delay_cost=1)
	S += d_t0_t3_t0 >= 6
	d_t0_t3_t0 += MM[1]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 6
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 6
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 7
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 7
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t3011 = S.Task('d_t3011', length=1, delay_cost=1)
	S += d_t3011 >= 7
	d_t3011 += MAS[0]

	d_t2_t11 = S.Task('d_t2_t11', length=1, delay_cost=1)
	S += d_t2_t11 >= 8
	d_t2_t11 += MAS[0]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 8
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 8
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 9
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 9
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=1, delay_cost=1)
	S += d_t2_t3_t2 >= 9
	d_t2_t3_t2 += MAS[0]

	d_t0_t10 = S.Task('d_t0_t10', length=1, delay_cost=1)
	S += d_t0_t10 >= 10
	d_t0_t10 += MAS[0]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 10
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 10
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=1, delay_cost=1)
	S += d_t2_a1_0 >= 11
	d_t2_a1_0 += MAS[5]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 11
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 11
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t10 = S.Task('d_t2_t10', length=1, delay_cost=1)
	S += d_t2_t10 >= 12
	d_t2_t10 += MAS[0]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 12
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 12
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t4000 = S.Task('d_t4000', length=1, delay_cost=1)
	S += d_t4000 >= 13
	d_t4000 += MAS[0]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 13
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 13
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 14
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 14
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t4001 = S.Task('d_t4001', length=1, delay_cost=1)
	S += d_t4001 >= 14
	d_t4001 += MAS[3]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 15
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 15
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3010 = S.Task('d_t3010', length=1, delay_cost=1)
	S += d_t3010 >= 15
	d_t3010 += MAS[0]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 16
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 16
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=1, delay_cost=1)
	S += d_t2_t3_t3 >= 16
	d_t2_t3_t3 += MAS[3]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=1, delay_cost=1)
	S += d_t1_t3_t2 >= 17
	d_t1_t3_t2 += MAS[0]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 17
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 17
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=1, delay_cost=1)
	S += d_t2_a1_1 >= 18
	d_t2_a1_1 += MAS[3]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 18
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 18
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 19
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 19
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t3001 = S.Task('d_t3001', length=1, delay_cost=1)
	S += d_t3001 >= 19
	d_t3001 += MAS[0]

	d_t0_t11 = S.Task('d_t0_t11', length=1, delay_cost=1)
	S += d_t0_t11 >= 20
	d_t0_t11 += MAS[0]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 20
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 20
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 21
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 21
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=1, delay_cost=1)
	S += d_t1_t3_t3 >= 21
	d_t1_t3_t3 += MAS[2]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=1, delay_cost=1)
	S += d_t0_a1_0 >= 22
	d_t0_a1_0 += MAS[4]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 22
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 22
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 23
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 23
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t3000 = S.Task('d_t3000', length=1, delay_cost=1)
	S += d_t3000 >= 23
	d_t3000 += MAS[5]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 24
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 24
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t1_t11 = S.Task('d_t1_t11', length=1, delay_cost=1)
	S += d_t1_t11 >= 24
	d_t1_t11 += MAS[0]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 25
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 25
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_t10 = S.Task('d_t1_t10', length=1, delay_cost=1)
	S += d_t1_t10 >= 25
	d_t1_t10 += MAS[1]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=1, delay_cost=1)
	S += d_t0_a1_1 >= 26
	d_t0_a1_1 += MAS[0]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 26
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 26
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 27
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 27
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=1, delay_cost=1)
	S += d_t1_a1_1 >= 27
	d_t1_a1_1 += MAS[5]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 28
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 28
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=1, delay_cost=1)
	S += d_t1_a1_0 >= 28
	d_t1_a1_0 += MAS[0]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 29
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 29
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=1, delay_cost=1)
	S += d_t0_t3_t3 >= 29
	d_t0_t3_t3 += MAS[0]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 30
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 30
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 30
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=1, delay_cost=1)
	S += d_t0_t3_t2 >= 30
	d_t0_t3_t2 += MAS[5]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=8, delay_cost=1)
	S += c_t1_t0_t1 >= 31
	c_t1_t0_t1 += MM[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 31
	c_t1_t1_t1_in += MM_in[1]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 31
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 31
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 32
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 32
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 32
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=8, delay_cost=1)
	S += c_t1_t1_t1 >= 32
	c_t1_t1_t1 += MM[1]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 33
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 33
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 33
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=8, delay_cost=1)
	S += c_t1_t1_t0 >= 33
	c_t1_t1_t0 += MM[0]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 34
	c_t0_t0_t1_in += MM_in[1]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 34
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 34
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=8, delay_cost=1)
	S += c_t1_t0_t0 >= 34
	c_t1_t0_t0 += MM[0]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=8, delay_cost=1)
	S += c_t0_t0_t1 >= 35
	c_t0_t0_t1 += MM[1]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 35
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 35
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 35
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=8, delay_cost=1)
	S += c_t0_t1_t0 >= 36
	c_t0_t1_t0 += MM[0]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 36
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 36
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 36
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 37
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 37
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 37
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=8, delay_cost=1)
	S += c_t0_t1_t1 >= 37
	c_t0_t1_t1 += MM[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=8, delay_cost=1)
	S += c_t0_t0_t0 >= 38
	c_t0_t0_t0 += MM[0]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 38
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 38
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 39
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 39
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	S += c_t1_t31 >= 39
	c_t1_t31 += MAS[3]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 40
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 40
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	S += c_t1_t20 >= 40
	c_t1_t20 += MAS[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=1, delay_cost=1)
	S += c_t1_t1_t3 >= 41
	c_t1_t1_t3 += MAS[0]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 41
	d_t5001_mem0 += MAIN_MEM_r[0]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 41
	d_t5001_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 42
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 42
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	d_t5001 = S.Task('d_t5001', length=1, delay_cost=1)
	S += d_t5001 >= 42
	d_t5001 += MAS[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 43
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 43
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=1, delay_cost=1)
	S += c_t1_t0_t3 >= 43
	c_t1_t0_t3 += MAS[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 44
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 44
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=1, delay_cost=1)
	S += c_t1_t0_t2 >= 44
	c_t1_t0_t2 += MAS[0]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 45
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 45
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	S += c_t0_t31 >= 45
	c_t0_t31 += MAS[0]

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	S += c_t0_t21 >= 46
	c_t0_t21 += MAS[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 46
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 46
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 47
	c_t1_t30 += MAS[0]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 47
	d_t5011_mem0 += MAIN_MEM_r[0]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 47
	d_t5011_mem1 += MAIN_MEM_r[1]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 48
	d_t5000_mem0 += MAIN_MEM_r[0]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 48
	d_t5000_mem1 += MAIN_MEM_r[1]

	d_t5011 = S.Task('d_t5011', length=1, delay_cost=1)
	S += d_t5011 >= 48
	d_t5011 += MAS[4]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 49
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 49
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	d_t5000 = S.Task('d_t5000', length=1, delay_cost=1)
	S += d_t5000 >= 49
	d_t5000 += MAS[1]

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 50
	c_t0_t30 += MAS[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 50
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 50
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=1, delay_cost=1)
	S += c_t1_t1_t2 >= 51
	c_t1_t1_t2 += MAS[2]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 51
	d_t5010_mem0 += MAIN_MEM_r[0]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 51
	d_t5010_mem1 += MAIN_MEM_r[1]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 52
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 52
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	d_t5010 = S.Task('d_t5010', length=1, delay_cost=1)
	S += d_t5010 >= 52
	d_t5010 += MAS[2]

	c_t1_t21 = S.Task('c_t1_t21', length=1, delay_cost=1)
	S += c_t1_t21 >= 53
	c_t1_t21 += MAS[3]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 53
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 53
	d_t4011_mem1 += MAIN_MEM_r[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 54
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 54
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	d_t4011 = S.Task('d_t4011', length=1, delay_cost=1)
	S += d_t4011 >= 54
	d_t4011 += MAS[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 55
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 55
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	S += c_t0_t20 >= 55
	c_t0_t20 += MAS[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 56
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 56
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=1, delay_cost=1)
	S += c_t0_t1_t3 >= 56
	c_t0_t1_t3 += MAS[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 57
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 57
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=1, delay_cost=1)
	S += c_t0_t1_t2 >= 57
	c_t0_t1_t2 += MAS[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 58
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 58
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=1, delay_cost=1)
	S += c_t0_t0_t3 >= 58
	c_t0_t0_t3 += MAS[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=1, delay_cost=1)
	S += c_t0_t0_t2 >= 59
	c_t0_t0_t2 += MAS[4]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 59
	d_t4010_mem0 += MAIN_MEM_r[0]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 59
	d_t4010_mem1 += MAIN_MEM_r[1]

	d_t4010 = S.Task('d_t4010', length=1, delay_cost=1)
	S += d_t4010 >= 60
	d_t4010 += MAS[3]


	# new tasks
	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=8, delay_cost=1)
	c_t2_t0_t0 += alt(MM)
	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	c_t2_t0_t0_in += alt(MM_in)
	S += c_t2_t0_t0_in*MM_in[0]<=c_t2_t0_t0*MM[0]
	S += c_t2_t0_t0_in*MM_in[1]<=c_t2_t0_t0*MM[1]
	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c_t2_t0_t0_mem0 <= c_t2_t0_t0

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]
	S += c_t2_t0_t0_mem1 <= c_t2_t0_t0

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=8, delay_cost=1)
	c_t2_t0_t1 += alt(MM)
	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	c_t2_t0_t1_in += alt(MM_in)
	S += c_t2_t0_t1_in*MM_in[0]<=c_t2_t0_t1*MM[0]
	S += c_t2_t0_t1_in*MM_in[1]<=c_t2_t0_t1*MM[1]
	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c_t2_t0_t1_mem0 <= c_t2_t0_t1

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]
	S += c_t2_t0_t1_mem1 <= c_t2_t0_t1

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=1, delay_cost=1)
	c_t2_t0_t2 += alt(MAS)
	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c_t2_t0_t2_mem0 <= c_t2_t0_t2

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c_t2_t0_t2_mem1 <= c_t2_t0_t2

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=1, delay_cost=1)
	c_t2_t0_t3 += alt(MAS)
	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]
	S += c_t2_t0_t3_mem0 <= c_t2_t0_t3

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]
	S += c_t2_t0_t3_mem1 <= c_t2_t0_t3

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=8, delay_cost=1)
	c_t2_t1_t0 += alt(MM)
	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	c_t2_t1_t0_in += alt(MM_in)
	S += c_t2_t1_t0_in*MM_in[0]<=c_t2_t1_t0*MM[0]
	S += c_t2_t1_t0_in*MM_in[1]<=c_t2_t1_t0*MM[1]
	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c_t2_t1_t0_mem0 <= c_t2_t1_t0

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]
	S += c_t2_t1_t0_mem1 <= c_t2_t1_t0

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=8, delay_cost=1)
	c_t2_t1_t1 += alt(MM)
	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	c_t2_t1_t1_in += alt(MM_in)
	S += c_t2_t1_t1_in*MM_in[0]<=c_t2_t1_t1*MM[0]
	S += c_t2_t1_t1_in*MM_in[1]<=c_t2_t1_t1*MM[1]
	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c_t2_t1_t1_mem0 <= c_t2_t1_t1

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]
	S += c_t2_t1_t1_mem1 <= c_t2_t1_t1

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=1, delay_cost=1)
	c_t2_t1_t2 += alt(MAS)
	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c_t2_t1_t2_mem0 <= c_t2_t1_t2

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c_t2_t1_t2_mem1 <= c_t2_t1_t2

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=1, delay_cost=1)
	c_t2_t1_t3 += alt(MAS)
	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]
	S += c_t2_t1_t3_mem0 <= c_t2_t1_t3

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]
	S += c_t2_t1_t3_mem1 <= c_t2_t1_t3

	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	c_t2_t20 += alt(MAS)
	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	c_t2_t20_mem0 += MAIN_MEM_r[0]
	S += c_t2_t20_mem0 <= c_t2_t20

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	c_t2_t20_mem1 += MAIN_MEM_r[1]
	S += c_t2_t20_mem1 <= c_t2_t20

	c_t2_t21 = S.Task('c_t2_t21', length=1, delay_cost=1)
	c_t2_t21 += alt(MAS)
	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	c_t2_t21_mem0 += MAIN_MEM_r[0]
	S += c_t2_t21_mem0 <= c_t2_t21

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	c_t2_t21_mem1 += MAIN_MEM_r[1]
	S += c_t2_t21_mem1 <= c_t2_t21

	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	c_t2_t30 += alt(MAS)
	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	c_t2_t30_mem0 += MAIN_MEM_r[0]
	S += c_t2_t30_mem0 <= c_t2_t30

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	c_t2_t30_mem1 += MAIN_MEM_r[1]
	S += c_t2_t30_mem1 <= c_t2_t30

	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	c_t2_t31 += alt(MAS)
	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	c_t2_t31_mem0 += MAIN_MEM_r[0]
	S += c_t2_t31_mem0 <= c_t2_t31

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	c_t2_t31_mem1 += MAIN_MEM_r[1]
	S += c_t2_t31_mem1 <= c_t2_t31

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	c_t3000 += alt(MAS)
	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	c_t3000_mem0 += MAIN_MEM_r[0]
	S += c_t3000_mem0 <= c_t3000

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	c_t3000_mem1 += MAIN_MEM_r[1]
	S += c_t3000_mem1 <= c_t3000

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	c_t3001 += alt(MAS)
	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	c_t3001_mem0 += MAIN_MEM_r[0]
	S += c_t3001_mem0 <= c_t3001

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	c_t3001_mem1 += MAIN_MEM_r[1]
	S += c_t3001_mem1 <= c_t3001

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	c_t3010 += alt(MAS)
	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	c_t3010_mem0 += MAIN_MEM_r[0]
	S += c_t3010_mem0 <= c_t3010

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	c_t3010_mem1 += MAIN_MEM_r[1]
	S += c_t3010_mem1 <= c_t3010

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	c_t3011 += alt(MAS)
	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	c_t3011_mem0 += MAIN_MEM_r[0]
	S += c_t3011_mem0 <= c_t3011

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	c_t3011_mem1 += MAIN_MEM_r[1]
	S += c_t3011_mem1 <= c_t3011

	c_t3100 = S.Task('c_t3100', length=1, delay_cost=1)
	c_t3100 += alt(MAS)
	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	c_t3100_mem0 += MAIN_MEM_r[0]
	S += c_t3100_mem0 <= c_t3100

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	c_t3100_mem1 += MAIN_MEM_r[1]
	S += c_t3100_mem1 <= c_t3100

	c_t3101 = S.Task('c_t3101', length=1, delay_cost=1)
	c_t3101 += alt(MAS)
	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	c_t3101_mem0 += MAIN_MEM_r[0]
	S += c_t3101_mem0 <= c_t3101

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	c_t3101_mem1 += MAIN_MEM_r[1]
	S += c_t3101_mem1 <= c_t3101

	c_t3110 = S.Task('c_t3110', length=1, delay_cost=1)
	c_t3110 += alt(MAS)
	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	c_t3110_mem0 += MAIN_MEM_r[0]
	S += c_t3110_mem0 <= c_t3110

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	c_t3110_mem1 += MAIN_MEM_r[1]
	S += c_t3110_mem1 <= c_t3110

	c_t3111 = S.Task('c_t3111', length=1, delay_cost=1)
	c_t3111 += alt(MAS)
	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	c_t3111_mem0 += MAIN_MEM_r[0]
	S += c_t3111_mem0 <= c_t3111

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	c_t3111_mem1 += MAIN_MEM_r[1]
	S += c_t3111_mem1 <= c_t3111

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	c_t4000 += alt(MAS)
	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	c_t4000_mem0 += MAIN_MEM_r[0]
	S += c_t4000_mem0 <= c_t4000

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	c_t4000_mem1 += MAIN_MEM_r[1]
	S += c_t4000_mem1 <= c_t4000

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	c_t4001 += alt(MAS)
	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	c_t4001_mem0 += MAIN_MEM_r[0]
	S += c_t4001_mem0 <= c_t4001

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	c_t4001_mem1 += MAIN_MEM_r[1]
	S += c_t4001_mem1 <= c_t4001

	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	c_t4010 += alt(MAS)
	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	c_t4010_mem0 += MAIN_MEM_r[0]
	S += c_t4010_mem0 <= c_t4010

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	c_t4010_mem1 += MAIN_MEM_r[1]
	S += c_t4010_mem1 <= c_t4010

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	c_t4011 += alt(MAS)
	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	c_t4011_mem0 += MAIN_MEM_r[0]
	S += c_t4011_mem0 <= c_t4011

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	c_t4011_mem1 += MAIN_MEM_r[1]
	S += c_t4011_mem1 <= c_t4011

	c_t4100 = S.Task('c_t4100', length=1, delay_cost=1)
	c_t4100 += alt(MAS)
	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	c_t4100_mem0 += MAIN_MEM_r[0]
	S += c_t4100_mem0 <= c_t4100

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	c_t4100_mem1 += MAIN_MEM_r[1]
	S += c_t4100_mem1 <= c_t4100

	c_t4101 = S.Task('c_t4101', length=1, delay_cost=1)
	c_t4101 += alt(MAS)
	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	c_t4101_mem0 += MAIN_MEM_r[0]
	S += c_t4101_mem0 <= c_t4101

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	c_t4101_mem1 += MAIN_MEM_r[1]
	S += c_t4101_mem1 <= c_t4101

	c_t4110 = S.Task('c_t4110', length=1, delay_cost=1)
	c_t4110 += alt(MAS)
	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	c_t4110_mem0 += MAIN_MEM_r[0]
	S += c_t4110_mem0 <= c_t4110

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	c_t4110_mem1 += MAIN_MEM_r[1]
	S += c_t4110_mem1 <= c_t4110

	c_t4111 = S.Task('c_t4111', length=1, delay_cost=1)
	c_t4111 += alt(MAS)
	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	c_t4111_mem0 += MAIN_MEM_r[0]
	S += c_t4111_mem0 <= c_t4111

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	c_t4111_mem1 += MAIN_MEM_r[1]
	S += c_t4111_mem1 <= c_t4111

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	c_t5000 += alt(MAS)
	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	c_t5000_mem0 += MAIN_MEM_r[0]
	S += c_t5000_mem0 <= c_t5000

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	c_t5000_mem1 += MAIN_MEM_r[1]
	S += c_t5000_mem1 <= c_t5000

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	c_t5001 += alt(MAS)
	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	c_t5001_mem0 += MAIN_MEM_r[0]
	S += c_t5001_mem0 <= c_t5001

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	c_t5001_mem1 += MAIN_MEM_r[1]
	S += c_t5001_mem1 <= c_t5001

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM2_stage1MAS6/FP12_LADDERMUL/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

