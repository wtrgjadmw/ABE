from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 127
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	S += c_t0_t3_t1_in >= 0
	c_t0_t3_t1_in += MM_in[0]

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem0 >= 0
	c_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem1 >= 0
	c_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=7, delay_cost=1)
	S += c_t0_t3_t1 >= 1
	c_t0_t3_t1 += MM[0]

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	S += c_t1_t3_t1_in >= 1
	c_t1_t3_t1_in += MM_in[0]

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem0 >= 1
	c_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem1 >= 1
	c_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	S += c_t1_t3_t0_in >= 2
	c_t1_t3_t0_in += MM_in[0]

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem0 >= 2
	c_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem1 >= 2
	c_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=7, delay_cost=1)
	S += c_t1_t3_t1 >= 2
	c_t1_t3_t1 += MM[0]

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	S += c_t0_t3_t0_in >= 3
	c_t0_t3_t0_in += MM_in[0]

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem0 >= 3
	c_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem1 >= 3
	c_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=7, delay_cost=1)
	S += c_t1_t3_t0 >= 3
	c_t1_t3_t0 += MM[0]

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=7, delay_cost=1)
	S += c_t0_t3_t0 >= 4
	c_t0_t3_t0 += MM[0]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 4
	c_t1_t10_mem0 += MAIN_MEM_r[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 4
	c_t1_t10_mem1 += MAIN_MEM_r[1]

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	S += c_t1_t10 >= 5
	c_t1_t10 += MAS[2]

	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	S += c_t2_a1_1_mem0 >= 5
	c_t2_a1_1_mem0 += MAIN_MEM_r[0]

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	S += c_t2_a1_1_mem1 >= 5
	c_t2_a1_1_mem1 += MAIN_MEM_r[1]

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=1, delay_cost=1)
	S += c_t2_a1_1 >= 6
	c_t2_a1_1 += MAS[0]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 6
	c_t2_t10_mem0 += MAIN_MEM_r[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 6
	c_t2_t10_mem1 += MAIN_MEM_r[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 7
	c_t0_t10_mem0 += MAIN_MEM_r[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 7
	c_t0_t10_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	S += c_t2_t10 >= 7
	c_t2_t10 += MAS[3]

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	S += c_t0_t10 >= 8
	c_t0_t10 += MAS[4]

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem0 >= 8
	c_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem1 >= 8
	c_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=1, delay_cost=1)
	S += c_t0_t3_t2 >= 9
	c_t0_t3_t2 += MAS[1]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 9
	c_t2_t11_mem0 += MAIN_MEM_r[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 9
	c_t2_t11_mem1 += MAIN_MEM_r[1]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 10
	c_t0_t11_mem0 += MAIN_MEM_r[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 10
	c_t0_t11_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	S += c_t2_t11 >= 10
	c_t2_t11 += MAS[2]

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	S += c_t0_t11 >= 11
	c_t0_t11 += MAS[1]

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem0 >= 11
	c_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem1 >= 11
	c_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=1, delay_cost=1)
	S += c_t1_t3_t2 >= 12
	c_t1_t3_t2 += MAS[0]

	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	S += c_t2_a1_0_mem0 >= 12
	c_t2_a1_0_mem0 += MAIN_MEM_r[0]

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	S += c_t2_a1_0_mem1 >= 12
	c_t2_a1_0_mem1 += MAIN_MEM_r[1]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 13
	c_t1_t11_mem0 += MAIN_MEM_r[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 13
	c_t1_t11_mem1 += MAIN_MEM_r[1]

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=1, delay_cost=1)
	S += c_t2_a1_0 >= 13
	c_t2_a1_0 += MAS[3]

	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	S += c_t0_a1_0_mem0 >= 14
	c_t0_a1_0_mem0 += MAIN_MEM_r[0]

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	S += c_t0_a1_0_mem1 >= 14
	c_t0_a1_0_mem1 += MAIN_MEM_r[1]

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	S += c_t1_t11 >= 14
	c_t1_t11 += MAS[0]

	c_t0_a1_0 = S.Task('c_t0_a1_0', length=1, delay_cost=1)
	S += c_t0_a1_0 >= 15
	c_t0_a1_0 += MAS[4]

	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	S += c_t1_a1_0_mem0 >= 15
	c_t1_a1_0_mem0 += MAIN_MEM_r[0]

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	S += c_t1_a1_0_mem1 >= 15
	c_t1_a1_0_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem0 >= 16
	c_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem1 >= 16
	c_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=1, delay_cost=1)
	S += c_t1_a1_0 >= 16
	c_t1_a1_0 += MAS[0]

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=1, delay_cost=1)
	S += c_t0_t3_t3 >= 17
	c_t0_t3_t3 += MAS[0]

	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	S += c_t1_a1_1_mem0 >= 17
	c_t1_a1_1_mem0 += MAIN_MEM_r[0]

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	S += c_t1_a1_1_mem1 >= 17
	c_t1_a1_1_mem1 += MAIN_MEM_r[1]

	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	S += c_t0_a1_1_mem0 >= 18
	c_t0_a1_1_mem0 += MAIN_MEM_r[0]

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	S += c_t0_a1_1_mem1 >= 18
	c_t0_a1_1_mem1 += MAIN_MEM_r[1]

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=1, delay_cost=1)
	S += c_t1_a1_1 >= 18
	c_t1_a1_1 += MAS[2]

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=1, delay_cost=1)
	S += c_t0_a1_1 >= 19
	c_t0_a1_1 += MAS[4]

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem0 >= 19
	c_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem1 >= 19
	c_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=1, delay_cost=1)
	S += c_t1_t3_t3 >= 20
	c_t1_t3_t3 += MAS[1]

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	S += c_t2_t3_t0_in >= 20
	c_t2_t3_t0_in += MM_in[0]

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem0 >= 20
	c_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem1 >= 20
	c_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=7, delay_cost=1)
	S += c_t2_t3_t0 >= 21
	c_t2_t3_t0 += MM[0]

	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	S += c_t2_t3_t1_in >= 21
	c_t2_t3_t1_in += MM_in[0]

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem0 >= 21
	c_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem1 >= 21
	c_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=7, delay_cost=1)
	S += c_t2_t3_t1 >= 22
	c_t2_t3_t1 += MM[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 22
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 22
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	S += c_t4001 >= 23
	c_t4001 += MAS[4]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 23
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 23
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	S += c_t4011 >= 24
	c_t4011 += MAS[1]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 24
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 24
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	S += c_t5010 >= 25
	c_t5010 += MAS[3]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 25
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 25
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 26
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 26
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	S += c_t5011 >= 26
	c_t5011 += MAS[2]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 27
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 27
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	S += c_t5000 >= 27
	c_t5000 += MAS[3]

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	S += c_t3001 >= 28
	c_t3001 += MAS[4]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 28
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 28
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	S += c_t4010 >= 29
	c_t4010 += MAS[0]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 29
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 29
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 30
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 30
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	S += c_t5001 >= 30
	c_t5001 += MAS[2]

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	S += c_t3010 >= 31
	c_t3010 += MAS[0]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 31
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 31
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem0 >= 32
	c_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem1 >= 32
	c_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	S += c_t3011 >= 32
	c_t3011 += MAS[1]

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=1, delay_cost=1)
	S += c_t2_t3_t2 >= 33
	c_t2_t3_t2 += MAS[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 33
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 33
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	S += c_t3000 >= 34
	c_t3000 += MAS[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 34
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 34
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem0 >= 35
	c_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem1 >= 35
	c_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	S += c_t4000 >= 35
	c_t4000 += MAS[0]

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=1, delay_cost=1)
	S += c_t2_t3_t3 >= 36
	c_t2_t3_t3 += MAS[0]


	# new tasks
	c_t0_t00 = S.Task('c_t0_t00', length=1, delay_cost=1)
	c_t0_t00 += alt(MAS)

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	c_t0_t00_mem0 += MAIN_MEM_r[0]
	S += c_t0_t00_mem0 <= c_t0_t00

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	c_t0_t00_mem1 += MAS_MEM[9]
	S += 15 < c_t0_t00_mem1
	S += c_t0_t00_mem1 <= c_t0_t00

	c_t0_t01 = S.Task('c_t0_t01', length=1, delay_cost=1)
	c_t0_t01 += alt(MAS)

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	c_t0_t01_mem0 += MAIN_MEM_r[0]
	S += c_t0_t01_mem0 <= c_t0_t01

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	c_t0_t01_mem1 += MAS_MEM[9]
	S += 19 < c_t0_t01_mem1
	S += c_t0_t01_mem1 <= c_t0_t01

	c_t0_t2_t3 = S.Task('c_t0_t2_t3', length=1, delay_cost=1)
	c_t0_t2_t3 += alt(MAS)

	c_t0_t2_t3_mem0 = S.Task('c_t0_t2_t3_mem0', length=1, delay_cost=1)
	c_t0_t2_t3_mem0 += MAS_MEM[8]
	S += 8 < c_t0_t2_t3_mem0
	S += c_t0_t2_t3_mem0 <= c_t0_t2_t3

	c_t0_t2_t3_mem1 = S.Task('c_t0_t2_t3_mem1', length=1, delay_cost=1)
	c_t0_t2_t3_mem1 += MAS_MEM[3]
	S += 11 < c_t0_t2_t3_mem1
	S += c_t0_t2_t3_mem1 <= c_t0_t2_t3

	c_t0_t3_t4_in = S.Task('c_t0_t3_t4_in', length=1, delay_cost=1)
	c_t0_t3_t4_in += alt(MM_in)
	c_t0_t3_t4 = S.Task('c_t0_t3_t4', length=7, delay_cost=1)
	c_t0_t3_t4 += alt(MM)
	S += c_t0_t3_t4>=c_t0_t3_t4_in

	c_t0_t3_t4_mem0 = S.Task('c_t0_t3_t4_mem0', length=1, delay_cost=1)
	c_t0_t3_t4_mem0 += MAS_MEM[2]
	S += 9 < c_t0_t3_t4_mem0
	S += c_t0_t3_t4_mem0 <= c_t0_t3_t4

	c_t0_t3_t4_mem1 = S.Task('c_t0_t3_t4_mem1', length=1, delay_cost=1)
	c_t0_t3_t4_mem1 += MAS_MEM[1]
	S += 17 < c_t0_t3_t4_mem1
	S += c_t0_t3_t4_mem1 <= c_t0_t3_t4

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	c_t0_t30 += alt(MAS)

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	c_t0_t30_mem0 += MM_MEM[0]
	S += 10 < c_t0_t30_mem0
	S += c_t0_t30_mem0 <= c_t0_t30

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	c_t0_t30_mem1 += MM_MEM[1]
	S += 7 < c_t0_t30_mem1
	S += c_t0_t30_mem1 <= c_t0_t30

	c_t0_t3_t5 = S.Task('c_t0_t3_t5', length=1, delay_cost=1)
	c_t0_t3_t5 += alt(MAS)

	c_t0_t3_t5_mem0 = S.Task('c_t0_t3_t5_mem0', length=1, delay_cost=1)
	c_t0_t3_t5_mem0 += MM_MEM[0]
	S += 10 < c_t0_t3_t5_mem0
	S += c_t0_t3_t5_mem0 <= c_t0_t3_t5

	c_t0_t3_t5_mem1 = S.Task('c_t0_t3_t5_mem1', length=1, delay_cost=1)
	c_t0_t3_t5_mem1 += MM_MEM[1]
	S += 7 < c_t0_t3_t5_mem1
	S += c_t0_t3_t5_mem1 <= c_t0_t3_t5

	c_t1_t00 = S.Task('c_t1_t00', length=1, delay_cost=1)
	c_t1_t00 += alt(MAS)

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	c_t1_t00_mem0 += MAIN_MEM_r[0]
	S += c_t1_t00_mem0 <= c_t1_t00

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	c_t1_t00_mem1 += MAS_MEM[1]
	S += 16 < c_t1_t00_mem1
	S += c_t1_t00_mem1 <= c_t1_t00

	c_t1_t01 = S.Task('c_t1_t01', length=1, delay_cost=1)
	c_t1_t01 += alt(MAS)

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	c_t1_t01_mem0 += MAIN_MEM_r[0]
	S += c_t1_t01_mem0 <= c_t1_t01

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	c_t1_t01_mem1 += MAS_MEM[5]
	S += 18 < c_t1_t01_mem1
	S += c_t1_t01_mem1 <= c_t1_t01

	c_t1_t2_t3 = S.Task('c_t1_t2_t3', length=1, delay_cost=1)
	c_t1_t2_t3 += alt(MAS)

	c_t1_t2_t3_mem0 = S.Task('c_t1_t2_t3_mem0', length=1, delay_cost=1)
	c_t1_t2_t3_mem0 += MAS_MEM[4]
	S += 5 < c_t1_t2_t3_mem0
	S += c_t1_t2_t3_mem0 <= c_t1_t2_t3

	c_t1_t2_t3_mem1 = S.Task('c_t1_t2_t3_mem1', length=1, delay_cost=1)
	c_t1_t2_t3_mem1 += MAS_MEM[1]
	S += 14 < c_t1_t2_t3_mem1
	S += c_t1_t2_t3_mem1 <= c_t1_t2_t3

	c_t1_t3_t4_in = S.Task('c_t1_t3_t4_in', length=1, delay_cost=1)
	c_t1_t3_t4_in += alt(MM_in)
	c_t1_t3_t4 = S.Task('c_t1_t3_t4', length=7, delay_cost=1)
	c_t1_t3_t4 += alt(MM)
	S += c_t1_t3_t4>=c_t1_t3_t4_in

	c_t1_t3_t4_mem0 = S.Task('c_t1_t3_t4_mem0', length=1, delay_cost=1)
	c_t1_t3_t4_mem0 += MAS_MEM[0]
	S += 12 < c_t1_t3_t4_mem0
	S += c_t1_t3_t4_mem0 <= c_t1_t3_t4

	c_t1_t3_t4_mem1 = S.Task('c_t1_t3_t4_mem1', length=1, delay_cost=1)
	c_t1_t3_t4_mem1 += MAS_MEM[3]
	S += 20 < c_t1_t3_t4_mem1
	S += c_t1_t3_t4_mem1 <= c_t1_t3_t4

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	c_t1_t30 += alt(MAS)

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	c_t1_t30_mem0 += MM_MEM[0]
	S += 9 < c_t1_t30_mem0
	S += c_t1_t30_mem0 <= c_t1_t30

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	c_t1_t30_mem1 += MM_MEM[1]
	S += 8 < c_t1_t30_mem1
	S += c_t1_t30_mem1 <= c_t1_t30

	c_t1_t3_t5 = S.Task('c_t1_t3_t5', length=1, delay_cost=1)
	c_t1_t3_t5 += alt(MAS)

	c_t1_t3_t5_mem0 = S.Task('c_t1_t3_t5_mem0', length=1, delay_cost=1)
	c_t1_t3_t5_mem0 += MM_MEM[0]
	S += 9 < c_t1_t3_t5_mem0
	S += c_t1_t3_t5_mem0 <= c_t1_t3_t5

	c_t1_t3_t5_mem1 = S.Task('c_t1_t3_t5_mem1', length=1, delay_cost=1)
	c_t1_t3_t5_mem1 += MM_MEM[1]
	S += 8 < c_t1_t3_t5_mem1
	S += c_t1_t3_t5_mem1 <= c_t1_t3_t5

	c_t2_t00 = S.Task('c_t2_t00', length=1, delay_cost=1)
	c_t2_t00 += alt(MAS)

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	c_t2_t00_mem0 += MAIN_MEM_r[0]
	S += c_t2_t00_mem0 <= c_t2_t00

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	c_t2_t00_mem1 += MAS_MEM[7]
	S += 13 < c_t2_t00_mem1
	S += c_t2_t00_mem1 <= c_t2_t00

	c_t2_t01 = S.Task('c_t2_t01', length=1, delay_cost=1)
	c_t2_t01 += alt(MAS)

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	c_t2_t01_mem0 += MAIN_MEM_r[0]
	S += c_t2_t01_mem0 <= c_t2_t01

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	c_t2_t01_mem1 += MAS_MEM[1]
	S += 6 < c_t2_t01_mem1
	S += c_t2_t01_mem1 <= c_t2_t01

	c_t2_t2_t3 = S.Task('c_t2_t2_t3', length=1, delay_cost=1)
	c_t2_t2_t3 += alt(MAS)

	c_t2_t2_t3_mem0 = S.Task('c_t2_t2_t3_mem0', length=1, delay_cost=1)
	c_t2_t2_t3_mem0 += MAS_MEM[6]
	S += 7 < c_t2_t2_t3_mem0
	S += c_t2_t2_t3_mem0 <= c_t2_t2_t3

	c_t2_t2_t3_mem1 = S.Task('c_t2_t2_t3_mem1', length=1, delay_cost=1)
	c_t2_t2_t3_mem1 += MAS_MEM[5]
	S += 10 < c_t2_t2_t3_mem1
	S += c_t2_t2_t3_mem1 <= c_t2_t2_t3

	c_t2_t3_t4_in = S.Task('c_t2_t3_t4_in', length=1, delay_cost=1)
	c_t2_t3_t4_in += alt(MM_in)
	c_t2_t3_t4 = S.Task('c_t2_t3_t4', length=7, delay_cost=1)
	c_t2_t3_t4 += alt(MM)
	S += c_t2_t3_t4>=c_t2_t3_t4_in

	c_t2_t3_t4_mem0 = S.Task('c_t2_t3_t4_mem0', length=1, delay_cost=1)
	c_t2_t3_t4_mem0 += MAS_MEM[6]
	S += 33 < c_t2_t3_t4_mem0
	S += c_t2_t3_t4_mem0 <= c_t2_t3_t4

	c_t2_t3_t4_mem1 = S.Task('c_t2_t3_t4_mem1', length=1, delay_cost=1)
	c_t2_t3_t4_mem1 += MAS_MEM[1]
	S += 36 < c_t2_t3_t4_mem1
	S += c_t2_t3_t4_mem1 <= c_t2_t3_t4

	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	c_t2_t30 += alt(MAS)

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	c_t2_t30_mem0 += MM_MEM[0]
	S += 27 < c_t2_t30_mem0
	S += c_t2_t30_mem0 <= c_t2_t30

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	c_t2_t30_mem1 += MM_MEM[1]
	S += 28 < c_t2_t30_mem1
	S += c_t2_t30_mem1 <= c_t2_t30

	c_t2_t3_t5 = S.Task('c_t2_t3_t5', length=1, delay_cost=1)
	c_t2_t3_t5 += alt(MAS)

	c_t2_t3_t5_mem0 = S.Task('c_t2_t3_t5_mem0', length=1, delay_cost=1)
	c_t2_t3_t5_mem0 += MM_MEM[0]
	S += 27 < c_t2_t3_t5_mem0
	S += c_t2_t3_t5_mem0 <= c_t2_t3_t5

	c_t2_t3_t5_mem1 = S.Task('c_t2_t3_t5_mem1', length=1, delay_cost=1)
	c_t2_t3_t5_mem1 += MM_MEM[1]
	S += 28 < c_t2_t3_t5_mem1
	S += c_t2_t3_t5_mem1 <= c_t2_t3_t5

	c_t3_a1_0 = S.Task('c_t3_a1_0', length=1, delay_cost=1)
	c_t3_a1_0 += alt(MAS)

	c_t3_a1_0_mem0 = S.Task('c_t3_a1_0_mem0', length=1, delay_cost=1)
	c_t3_a1_0_mem0 += MAS_MEM[0]
	S += 31 < c_t3_a1_0_mem0
	S += c_t3_a1_0_mem0 <= c_t3_a1_0

	c_t3_a1_0_mem1 = S.Task('c_t3_a1_0_mem1', length=1, delay_cost=1)
	c_t3_a1_0_mem1 += MAS_MEM[3]
	S += 32 < c_t3_a1_0_mem1
	S += c_t3_a1_0_mem1 <= c_t3_a1_0

	c_t3_a1_1 = S.Task('c_t3_a1_1', length=1, delay_cost=1)
	c_t3_a1_1 += alt(MAS)

	c_t3_a1_1_mem0 = S.Task('c_t3_a1_1_mem0', length=1, delay_cost=1)
	c_t3_a1_1_mem0 += MAS_MEM[2]
	S += 32 < c_t3_a1_1_mem0
	S += c_t3_a1_1_mem0 <= c_t3_a1_1

	c_t3_a1_1_mem1 = S.Task('c_t3_a1_1_mem1', length=1, delay_cost=1)
	c_t3_a1_1_mem1 += MAS_MEM[1]
	S += 31 < c_t3_a1_1_mem1
	S += c_t3_a1_1_mem1 <= c_t3_a1_1

	c_t3_t10 = S.Task('c_t3_t10', length=1, delay_cost=1)
	c_t3_t10 += alt(MAS)

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	c_t3_t10_mem0 += MAS_MEM[2]
	S += 34 < c_t3_t10_mem0
	S += c_t3_t10_mem0 <= c_t3_t10

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	c_t3_t10_mem1 += MAS_MEM[1]
	S += 31 < c_t3_t10_mem1
	S += c_t3_t10_mem1 <= c_t3_t10

	c_t3_t11 = S.Task('c_t3_t11', length=1, delay_cost=1)
	c_t3_t11 += alt(MAS)

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	c_t3_t11_mem0 += MAS_MEM[8]
	S += 28 < c_t3_t11_mem0
	S += c_t3_t11_mem0 <= c_t3_t11

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	c_t3_t11_mem1 += MAS_MEM[3]
	S += 32 < c_t3_t11_mem1
	S += c_t3_t11_mem1 <= c_t3_t11

	c_t3_t3_t0_in = S.Task('c_t3_t3_t0_in', length=1, delay_cost=1)
	c_t3_t3_t0_in += alt(MM_in)
	c_t3_t3_t0 = S.Task('c_t3_t3_t0', length=7, delay_cost=1)
	c_t3_t3_t0 += alt(MM)
	S += c_t3_t3_t0>=c_t3_t3_t0_in

	c_t3_t3_t0_mem0 = S.Task('c_t3_t3_t0_mem0', length=1, delay_cost=1)
	c_t3_t3_t0_mem0 += MAS_MEM[2]
	S += 34 < c_t3_t3_t0_mem0
	S += c_t3_t3_t0_mem0 <= c_t3_t3_t0

	c_t3_t3_t0_mem1 = S.Task('c_t3_t3_t0_mem1', length=1, delay_cost=1)
	c_t3_t3_t0_mem1 += MAS_MEM[1]
	S += 31 < c_t3_t3_t0_mem1
	S += c_t3_t3_t0_mem1 <= c_t3_t3_t0

	c_t3_t3_t1_in = S.Task('c_t3_t3_t1_in', length=1, delay_cost=1)
	c_t3_t3_t1_in += alt(MM_in)
	c_t3_t3_t1 = S.Task('c_t3_t3_t1', length=7, delay_cost=1)
	c_t3_t3_t1 += alt(MM)
	S += c_t3_t3_t1>=c_t3_t3_t1_in

	c_t3_t3_t1_mem0 = S.Task('c_t3_t3_t1_mem0', length=1, delay_cost=1)
	c_t3_t3_t1_mem0 += MAS_MEM[8]
	S += 28 < c_t3_t3_t1_mem0
	S += c_t3_t3_t1_mem0 <= c_t3_t3_t1

	c_t3_t3_t1_mem1 = S.Task('c_t3_t3_t1_mem1', length=1, delay_cost=1)
	c_t3_t3_t1_mem1 += MAS_MEM[3]
	S += 32 < c_t3_t3_t1_mem1
	S += c_t3_t3_t1_mem1 <= c_t3_t3_t1

	c_t3_t3_t2 = S.Task('c_t3_t3_t2', length=1, delay_cost=1)
	c_t3_t3_t2 += alt(MAS)

	c_t3_t3_t2_mem0 = S.Task('c_t3_t3_t2_mem0', length=1, delay_cost=1)
	c_t3_t3_t2_mem0 += MAS_MEM[2]
	S += 34 < c_t3_t3_t2_mem0
	S += c_t3_t3_t2_mem0 <= c_t3_t3_t2

	c_t3_t3_t2_mem1 = S.Task('c_t3_t3_t2_mem1', length=1, delay_cost=1)
	c_t3_t3_t2_mem1 += MAS_MEM[9]
	S += 28 < c_t3_t3_t2_mem1
	S += c_t3_t3_t2_mem1 <= c_t3_t3_t2

	c_t3_t3_t3 = S.Task('c_t3_t3_t3', length=1, delay_cost=1)
	c_t3_t3_t3 += alt(MAS)

	c_t3_t3_t3_mem0 = S.Task('c_t3_t3_t3_mem0', length=1, delay_cost=1)
	c_t3_t3_t3_mem0 += MAS_MEM[0]
	S += 31 < c_t3_t3_t3_mem0
	S += c_t3_t3_t3_mem0 <= c_t3_t3_t3

	c_t3_t3_t3_mem1 = S.Task('c_t3_t3_t3_mem1', length=1, delay_cost=1)
	c_t3_t3_t3_mem1 += MAS_MEM[3]
	S += 32 < c_t3_t3_t3_mem1
	S += c_t3_t3_t3_mem1 <= c_t3_t3_t3

	c_t4_a1_0 = S.Task('c_t4_a1_0', length=1, delay_cost=1)
	c_t4_a1_0 += alt(MAS)

	c_t4_a1_0_mem0 = S.Task('c_t4_a1_0_mem0', length=1, delay_cost=1)
	c_t4_a1_0_mem0 += MAS_MEM[0]
	S += 29 < c_t4_a1_0_mem0
	S += c_t4_a1_0_mem0 <= c_t4_a1_0

	c_t4_a1_0_mem1 = S.Task('c_t4_a1_0_mem1', length=1, delay_cost=1)
	c_t4_a1_0_mem1 += MAS_MEM[3]
	S += 24 < c_t4_a1_0_mem1
	S += c_t4_a1_0_mem1 <= c_t4_a1_0

	c_t4_a1_1 = S.Task('c_t4_a1_1', length=1, delay_cost=1)
	c_t4_a1_1 += alt(MAS)

	c_t4_a1_1_mem0 = S.Task('c_t4_a1_1_mem0', length=1, delay_cost=1)
	c_t4_a1_1_mem0 += MAS_MEM[2]
	S += 24 < c_t4_a1_1_mem0
	S += c_t4_a1_1_mem0 <= c_t4_a1_1

	c_t4_a1_1_mem1 = S.Task('c_t4_a1_1_mem1', length=1, delay_cost=1)
	c_t4_a1_1_mem1 += MAS_MEM[1]
	S += 29 < c_t4_a1_1_mem1
	S += c_t4_a1_1_mem1 <= c_t4_a1_1

	c_t4_t10 = S.Task('c_t4_t10', length=1, delay_cost=1)
	c_t4_t10 += alt(MAS)

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	c_t4_t10_mem0 += MAS_MEM[0]
	S += 35 < c_t4_t10_mem0
	S += c_t4_t10_mem0 <= c_t4_t10

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	c_t4_t10_mem1 += MAS_MEM[1]
	S += 29 < c_t4_t10_mem1
	S += c_t4_t10_mem1 <= c_t4_t10

	c_t4_t11 = S.Task('c_t4_t11', length=1, delay_cost=1)
	c_t4_t11 += alt(MAS)

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	c_t4_t11_mem0 += MAS_MEM[8]
	S += 23 < c_t4_t11_mem0
	S += c_t4_t11_mem0 <= c_t4_t11

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	c_t4_t11_mem1 += MAS_MEM[3]
	S += 24 < c_t4_t11_mem1
	S += c_t4_t11_mem1 <= c_t4_t11

	c_t4_t3_t0_in = S.Task('c_t4_t3_t0_in', length=1, delay_cost=1)
	c_t4_t3_t0_in += alt(MM_in)
	c_t4_t3_t0 = S.Task('c_t4_t3_t0', length=7, delay_cost=1)
	c_t4_t3_t0 += alt(MM)
	S += c_t4_t3_t0>=c_t4_t3_t0_in

	c_t4_t3_t0_mem0 = S.Task('c_t4_t3_t0_mem0', length=1, delay_cost=1)
	c_t4_t3_t0_mem0 += MAS_MEM[0]
	S += 35 < c_t4_t3_t0_mem0
	S += c_t4_t3_t0_mem0 <= c_t4_t3_t0

	c_t4_t3_t0_mem1 = S.Task('c_t4_t3_t0_mem1', length=1, delay_cost=1)
	c_t4_t3_t0_mem1 += MAS_MEM[1]
	S += 29 < c_t4_t3_t0_mem1
	S += c_t4_t3_t0_mem1 <= c_t4_t3_t0

	c_t4_t3_t1_in = S.Task('c_t4_t3_t1_in', length=1, delay_cost=1)
	c_t4_t3_t1_in += alt(MM_in)
	c_t4_t3_t1 = S.Task('c_t4_t3_t1', length=7, delay_cost=1)
	c_t4_t3_t1 += alt(MM)
	S += c_t4_t3_t1>=c_t4_t3_t1_in

	c_t4_t3_t1_mem0 = S.Task('c_t4_t3_t1_mem0', length=1, delay_cost=1)
	c_t4_t3_t1_mem0 += MAS_MEM[8]
	S += 23 < c_t4_t3_t1_mem0
	S += c_t4_t3_t1_mem0 <= c_t4_t3_t1

	c_t4_t3_t1_mem1 = S.Task('c_t4_t3_t1_mem1', length=1, delay_cost=1)
	c_t4_t3_t1_mem1 += MAS_MEM[3]
	S += 24 < c_t4_t3_t1_mem1
	S += c_t4_t3_t1_mem1 <= c_t4_t3_t1

	c_t4_t3_t2 = S.Task('c_t4_t3_t2', length=1, delay_cost=1)
	c_t4_t3_t2 += alt(MAS)

	c_t4_t3_t2_mem0 = S.Task('c_t4_t3_t2_mem0', length=1, delay_cost=1)
	c_t4_t3_t2_mem0 += MAS_MEM[0]
	S += 35 < c_t4_t3_t2_mem0
	S += c_t4_t3_t2_mem0 <= c_t4_t3_t2

	c_t4_t3_t2_mem1 = S.Task('c_t4_t3_t2_mem1', length=1, delay_cost=1)
	c_t4_t3_t2_mem1 += MAS_MEM[9]
	S += 23 < c_t4_t3_t2_mem1
	S += c_t4_t3_t2_mem1 <= c_t4_t3_t2

	c_t4_t3_t3 = S.Task('c_t4_t3_t3', length=1, delay_cost=1)
	c_t4_t3_t3 += alt(MAS)

	c_t4_t3_t3_mem0 = S.Task('c_t4_t3_t3_mem0', length=1, delay_cost=1)
	c_t4_t3_t3_mem0 += MAS_MEM[0]
	S += 29 < c_t4_t3_t3_mem0
	S += c_t4_t3_t3_mem0 <= c_t4_t3_t3

	c_t4_t3_t3_mem1 = S.Task('c_t4_t3_t3_mem1', length=1, delay_cost=1)
	c_t4_t3_t3_mem1 += MAS_MEM[3]
	S += 24 < c_t4_t3_t3_mem1
	S += c_t4_t3_t3_mem1 <= c_t4_t3_t3

	c_t5_a1_0 = S.Task('c_t5_a1_0', length=1, delay_cost=1)
	c_t5_a1_0 += alt(MAS)

	c_t5_a1_0_mem0 = S.Task('c_t5_a1_0_mem0', length=1, delay_cost=1)
	c_t5_a1_0_mem0 += MAS_MEM[6]
	S += 25 < c_t5_a1_0_mem0
	S += c_t5_a1_0_mem0 <= c_t5_a1_0

	c_t5_a1_0_mem1 = S.Task('c_t5_a1_0_mem1', length=1, delay_cost=1)
	c_t5_a1_0_mem1 += MAS_MEM[5]
	S += 26 < c_t5_a1_0_mem1
	S += c_t5_a1_0_mem1 <= c_t5_a1_0

	c_t5_a1_1 = S.Task('c_t5_a1_1', length=1, delay_cost=1)
	c_t5_a1_1 += alt(MAS)

	c_t5_a1_1_mem0 = S.Task('c_t5_a1_1_mem0', length=1, delay_cost=1)
	c_t5_a1_1_mem0 += MAS_MEM[4]
	S += 26 < c_t5_a1_1_mem0
	S += c_t5_a1_1_mem0 <= c_t5_a1_1

	c_t5_a1_1_mem1 = S.Task('c_t5_a1_1_mem1', length=1, delay_cost=1)
	c_t5_a1_1_mem1 += MAS_MEM[7]
	S += 25 < c_t5_a1_1_mem1
	S += c_t5_a1_1_mem1 <= c_t5_a1_1

	c_t5_t10 = S.Task('c_t5_t10', length=1, delay_cost=1)
	c_t5_t10 += alt(MAS)

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	c_t5_t10_mem0 += MAS_MEM[6]
	S += 27 < c_t5_t10_mem0
	S += c_t5_t10_mem0 <= c_t5_t10

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	c_t5_t10_mem1 += MAS_MEM[7]
	S += 25 < c_t5_t10_mem1
	S += c_t5_t10_mem1 <= c_t5_t10

	c_t5_t11 = S.Task('c_t5_t11', length=1, delay_cost=1)
	c_t5_t11 += alt(MAS)

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	c_t5_t11_mem0 += MAS_MEM[4]
	S += 30 < c_t5_t11_mem0
	S += c_t5_t11_mem0 <= c_t5_t11

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	c_t5_t11_mem1 += MAS_MEM[5]
	S += 26 < c_t5_t11_mem1
	S += c_t5_t11_mem1 <= c_t5_t11

	c_t5_t3_t0_in = S.Task('c_t5_t3_t0_in', length=1, delay_cost=1)
	c_t5_t3_t0_in += alt(MM_in)
	c_t5_t3_t0 = S.Task('c_t5_t3_t0', length=7, delay_cost=1)
	c_t5_t3_t0 += alt(MM)
	S += c_t5_t3_t0>=c_t5_t3_t0_in

	c_t5_t3_t0_mem0 = S.Task('c_t5_t3_t0_mem0', length=1, delay_cost=1)
	c_t5_t3_t0_mem0 += MAS_MEM[6]
	S += 27 < c_t5_t3_t0_mem0
	S += c_t5_t3_t0_mem0 <= c_t5_t3_t0

	c_t5_t3_t0_mem1 = S.Task('c_t5_t3_t0_mem1', length=1, delay_cost=1)
	c_t5_t3_t0_mem1 += MAS_MEM[7]
	S += 25 < c_t5_t3_t0_mem1
	S += c_t5_t3_t0_mem1 <= c_t5_t3_t0

	c_t5_t3_t1_in = S.Task('c_t5_t3_t1_in', length=1, delay_cost=1)
	c_t5_t3_t1_in += alt(MM_in)
	c_t5_t3_t1 = S.Task('c_t5_t3_t1', length=7, delay_cost=1)
	c_t5_t3_t1 += alt(MM)
	S += c_t5_t3_t1>=c_t5_t3_t1_in

	c_t5_t3_t1_mem0 = S.Task('c_t5_t3_t1_mem0', length=1, delay_cost=1)
	c_t5_t3_t1_mem0 += MAS_MEM[4]
	S += 30 < c_t5_t3_t1_mem0
	S += c_t5_t3_t1_mem0 <= c_t5_t3_t1

	c_t5_t3_t1_mem1 = S.Task('c_t5_t3_t1_mem1', length=1, delay_cost=1)
	c_t5_t3_t1_mem1 += MAS_MEM[5]
	S += 26 < c_t5_t3_t1_mem1
	S += c_t5_t3_t1_mem1 <= c_t5_t3_t1

	c_t5_t3_t2 = S.Task('c_t5_t3_t2', length=1, delay_cost=1)
	c_t5_t3_t2 += alt(MAS)

	c_t5_t3_t2_mem0 = S.Task('c_t5_t3_t2_mem0', length=1, delay_cost=1)
	c_t5_t3_t2_mem0 += MAS_MEM[6]
	S += 27 < c_t5_t3_t2_mem0
	S += c_t5_t3_t2_mem0 <= c_t5_t3_t2

	c_t5_t3_t2_mem1 = S.Task('c_t5_t3_t2_mem1', length=1, delay_cost=1)
	c_t5_t3_t2_mem1 += MAS_MEM[5]
	S += 30 < c_t5_t3_t2_mem1
	S += c_t5_t3_t2_mem1 <= c_t5_t3_t2

	c_t5_t3_t3 = S.Task('c_t5_t3_t3', length=1, delay_cost=1)
	c_t5_t3_t3 += alt(MAS)

	c_t5_t3_t3_mem0 = S.Task('c_t5_t3_t3_mem0', length=1, delay_cost=1)
	c_t5_t3_t3_mem0 += MAS_MEM[6]
	S += 25 < c_t5_t3_t3_mem0
	S += c_t5_t3_t3_mem0 <= c_t5_t3_t3

	c_t5_t3_t3_mem1 = S.Task('c_t5_t3_t3_mem1', length=1, delay_cost=1)
	c_t5_t3_t3_mem1 += MAS_MEM[5]
	S += 26 < c_t5_t3_t3_mem1
	S += c_t5_t3_t3_mem1 <= c_t5_t3_t3

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/multiRAM_multiMAS/scheduling_result/stage7MM1_stage1MAS5/SQR/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

