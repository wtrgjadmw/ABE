from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 168
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=14)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=2, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t1_t3_t3_in = S.Task('c_t1_t3_t3_in', length=1, delay_cost=1)
	S += c_t1_t3_t3_in >= 0
	c_t1_t3_t3_in += MAS_in[0]

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem0 >= 0
	c_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem1 >= 0
	c_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=3, delay_cost=1)
	S += c_t1_t3_t3 >= 1
	c_t1_t3_t3 += MAS[0]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 1
	c_t3011_in += MAS_in[0]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 1
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 1
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=3, delay_cost=1)
	S += c_t3011 >= 2
	c_t3011 += MAS[0]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 2
	c_t4000_in += MAS_in[0]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 2
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 2
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 3
	c_t3010_in += MAS_in[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 3
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 3
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=3, delay_cost=1)
	S += c_t4000 >= 3
	c_t4000 += MAS[0]

	c_t3010 = S.Task('c_t3010', length=3, delay_cost=1)
	S += c_t3010 >= 4
	c_t3010 += MAS[0]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 4
	c_t4001_in += MAS_in[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 4
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 4
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t2_a1_1_in = S.Task('c_t2_a1_1_in', length=1, delay_cost=1)
	S += c_t2_a1_1_in >= 5
	c_t2_a1_1_in += MAS_in[0]

	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	S += c_t2_a1_1_mem0 >= 5
	c_t2_a1_1_mem0 += MAIN_MEM_r[0]

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	S += c_t2_a1_1_mem1 >= 5
	c_t2_a1_1_mem1 += MAIN_MEM_r[1]

	c_t4001 = S.Task('c_t4001', length=3, delay_cost=1)
	S += c_t4001 >= 5
	c_t4001 += MAS[0]

	c_t1_t3_t2_in = S.Task('c_t1_t3_t2_in', length=1, delay_cost=1)
	S += c_t1_t3_t2_in >= 6
	c_t1_t3_t2_in += MAS_in[0]

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem0 >= 6
	c_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem1 >= 6
	c_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=3, delay_cost=1)
	S += c_t2_a1_1 >= 6
	c_t2_a1_1 += MAS[0]

	c_t3_t3_t3_in = S.Task('c_t3_t3_t3_in', length=1, delay_cost=1)
	S += c_t3_t3_t3_in >= 6
	c_t3_t3_t3_in += MAS_in[1]

	c_t3_t3_t3_mem0 = S.Task('c_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem0 >= 6
	c_t3_t3_t3_mem0 += MAS_MEM[0]

	c_t3_t3_t3_mem1 = S.Task('c_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem1 >= 6
	c_t3_t3_t3_mem1 += MAS_MEM[1]

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=3, delay_cost=1)
	S += c_t1_t3_t2 >= 7
	c_t1_t3_t2 += MAS[0]

	c_t2_t3_t2_in = S.Task('c_t2_t3_t2_in', length=1, delay_cost=1)
	S += c_t2_t3_t2_in >= 7
	c_t2_t3_t2_in += MAS_in[0]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem0 >= 7
	c_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem1 >= 7
	c_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t3_t3_t3 = S.Task('c_t3_t3_t3', length=3, delay_cost=1)
	S += c_t3_t3_t3 >= 7
	c_t3_t3_t3 += MAS[1]

	c_t4_t3_t2_in = S.Task('c_t4_t3_t2_in', length=1, delay_cost=1)
	S += c_t4_t3_t2_in >= 7
	c_t4_t3_t2_in += MAS_in[1]

	c_t4_t3_t2_mem0 = S.Task('c_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem0 >= 7
	c_t4_t3_t2_mem0 += MAS_MEM[0]

	c_t4_t3_t2_mem1 = S.Task('c_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem1 >= 7
	c_t4_t3_t2_mem1 += MAS_MEM[1]

	c_t1_a1_0_in = S.Task('c_t1_a1_0_in', length=1, delay_cost=1)
	S += c_t1_a1_0_in >= 8
	c_t1_a1_0_in += MAS_in[0]

	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	S += c_t1_a1_0_mem0 >= 8
	c_t1_a1_0_mem0 += MAIN_MEM_r[0]

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	S += c_t1_a1_0_mem1 >= 8
	c_t1_a1_0_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=3, delay_cost=1)
	S += c_t2_t3_t2 >= 8
	c_t2_t3_t2 += MAS[0]

	c_t3_a1_0_in = S.Task('c_t3_a1_0_in', length=1, delay_cost=1)
	S += c_t3_a1_0_in >= 8
	c_t3_a1_0_in += MAS_in[1]

	c_t3_a1_0_mem0 = S.Task('c_t3_a1_0_mem0', length=1, delay_cost=1)
	S += c_t3_a1_0_mem0 >= 8
	c_t3_a1_0_mem0 += MAS_MEM[0]

	c_t3_a1_0_mem1 = S.Task('c_t3_a1_0_mem1', length=1, delay_cost=1)
	S += c_t3_a1_0_mem1 >= 8
	c_t3_a1_0_mem1 += MAS_MEM[1]

	c_t4_t3_t2 = S.Task('c_t4_t3_t2', length=3, delay_cost=1)
	S += c_t4_t3_t2 >= 8
	c_t4_t3_t2 += MAS[1]

	c_t0_t3_t3_in = S.Task('c_t0_t3_t3_in', length=1, delay_cost=1)
	S += c_t0_t3_t3_in >= 9
	c_t0_t3_t3_in += MAS_in[0]

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem0 >= 9
	c_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem1 >= 9
	c_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=3, delay_cost=1)
	S += c_t1_a1_0 >= 9
	c_t1_a1_0 += MAS[0]

	c_t1_t3_t4_in = S.Task('c_t1_t3_t4_in', length=1, delay_cost=1)
	S += c_t1_t3_t4_in >= 9
	c_t1_t3_t4_in += MM_in[0]

	c_t1_t3_t4_mem0 = S.Task('c_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem0 >= 9
	c_t1_t3_t4_mem0 += MAS_MEM[0]

	c_t1_t3_t4_mem1 = S.Task('c_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem1 >= 9
	c_t1_t3_t4_mem1 += MAS_MEM[1]

	c_t3_a1_0 = S.Task('c_t3_a1_0', length=3, delay_cost=1)
	S += c_t3_a1_0 >= 9
	c_t3_a1_0 += MAS[1]

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=3, delay_cost=1)
	S += c_t0_t3_t3 >= 10
	c_t0_t3_t3 += MAS[0]

	c_t1_t3_t4 = S.Task('c_t1_t3_t4', length=14, delay_cost=1)
	S += c_t1_t3_t4 >= 10
	c_t1_t3_t4 += MM[0]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 10
	c_t2_t11_in += MAS_in[0]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 10
	c_t2_t11_mem0 += MAIN_MEM_r[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 10
	c_t2_t11_mem1 += MAIN_MEM_r[1]

	c_t3_a1_1_in = S.Task('c_t3_a1_1_in', length=1, delay_cost=1)
	S += c_t3_a1_1_in >= 10
	c_t3_a1_1_in += MAS_in[1]

	c_t3_a1_1_mem0 = S.Task('c_t3_a1_1_mem0', length=1, delay_cost=1)
	S += c_t3_a1_1_mem0 >= 10
	c_t3_a1_1_mem0 += MAS_MEM[0]

	c_t3_a1_1_mem1 = S.Task('c_t3_a1_1_mem1', length=1, delay_cost=1)
	S += c_t3_a1_1_mem1 >= 10
	c_t3_a1_1_mem1 += MAS_MEM[1]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 11
	c_t1_t10_in += MAS_in[0]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 11
	c_t1_t10_mem0 += MAIN_MEM_r[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 11
	c_t1_t10_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=3, delay_cost=1)
	S += c_t2_t11 >= 11
	c_t2_t11 += MAS[0]

	c_t3_a1_1 = S.Task('c_t3_a1_1', length=3, delay_cost=1)
	S += c_t3_a1_1 >= 11
	c_t3_a1_1 += MAS[1]

	c_t0_t3_t2_in = S.Task('c_t0_t3_t2_in', length=1, delay_cost=1)
	S += c_t0_t3_t2_in >= 12
	c_t0_t3_t2_in += MAS_in[0]

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem0 >= 12
	c_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem1 >= 12
	c_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t10 = S.Task('c_t1_t10', length=3, delay_cost=1)
	S += c_t1_t10 >= 12
	c_t1_t10 += MAS[0]

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=3, delay_cost=1)
	S += c_t0_t3_t2 >= 13
	c_t0_t3_t2 += MAS[0]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 13
	c_t3000_in += MAS_in[0]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 13
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 13
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t0_a1_0_in = S.Task('c_t0_a1_0_in', length=1, delay_cost=1)
	S += c_t0_a1_0_in >= 14
	c_t0_a1_0_in += MAS_in[0]

	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	S += c_t0_a1_0_mem0 >= 14
	c_t0_a1_0_mem0 += MAIN_MEM_r[0]

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	S += c_t0_a1_0_mem1 >= 14
	c_t0_a1_0_mem1 += MAIN_MEM_r[1]

	c_t3000 = S.Task('c_t3000', length=3, delay_cost=1)
	S += c_t3000 >= 14
	c_t3000 += MAS[0]

	c_t0_a1_0 = S.Task('c_t0_a1_0', length=3, delay_cost=1)
	S += c_t0_a1_0 >= 15
	c_t0_a1_0 += MAS[0]

	c_t0_t3_t4_in = S.Task('c_t0_t3_t4_in', length=1, delay_cost=1)
	S += c_t0_t3_t4_in >= 15
	c_t0_t3_t4_in += MM_in[0]

	c_t0_t3_t4_mem0 = S.Task('c_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem0 >= 15
	c_t0_t3_t4_mem0 += MAS_MEM[0]

	c_t0_t3_t4_mem1 = S.Task('c_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem1 >= 15
	c_t0_t3_t4_mem1 += MAS_MEM[1]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 15
	c_t3001_in += MAS_in[0]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 15
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 15
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t4 = S.Task('c_t0_t3_t4', length=14, delay_cost=1)
	S += c_t0_t3_t4 >= 16
	c_t0_t3_t4 += MM[0]

	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	S += c_t2_t3_t1_in >= 16
	c_t2_t3_t1_in += MM_in[0]

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem0 >= 16
	c_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem1 >= 16
	c_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=3, delay_cost=1)
	S += c_t3001 >= 16
	c_t3001 += MAS[0]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 16
	c_t3_t10_in += MAS_in[0]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 16
	c_t3_t10_mem0 += MAS_MEM[0]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 16
	c_t3_t10_mem1 += MAS_MEM[1]

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	S += c_t2_t3_t0_in >= 17
	c_t2_t3_t0_in += MM_in[0]

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem0 >= 17
	c_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem1 >= 17
	c_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=14, delay_cost=1)
	S += c_t2_t3_t1 >= 17
	c_t2_t3_t1 += MM[0]

	c_t3_t10 = S.Task('c_t3_t10', length=3, delay_cost=1)
	S += c_t3_t10 >= 17
	c_t3_t10 += MAS[0]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 18
	c_t0_t10_in += MAS_in[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 18
	c_t0_t10_mem0 += MAIN_MEM_r[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 18
	c_t0_t10_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=14, delay_cost=1)
	S += c_t2_t3_t0 >= 18
	c_t2_t3_t0 += MM[0]

	c_t3_t3_t2_in = S.Task('c_t3_t3_t2_in', length=1, delay_cost=1)
	S += c_t3_t3_t2_in >= 18
	c_t3_t3_t2_in += MAS_in[0]

	c_t3_t3_t2_mem0 = S.Task('c_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem0 >= 18
	c_t3_t3_t2_mem0 += MAS_MEM[0]

	c_t3_t3_t2_mem1 = S.Task('c_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem1 >= 18
	c_t3_t3_t2_mem1 += MAS_MEM[1]

	c_t0_t10 = S.Task('c_t0_t10', length=3, delay_cost=1)
	S += c_t0_t10 >= 19
	c_t0_t10 += MAS[1]

	c_t2_a1_0_in = S.Task('c_t2_a1_0_in', length=1, delay_cost=1)
	S += c_t2_a1_0_in >= 19
	c_t2_a1_0_in += MAS_in[0]

	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	S += c_t2_a1_0_mem0 >= 19
	c_t2_a1_0_mem0 += MAIN_MEM_r[0]

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	S += c_t2_a1_0_mem1 >= 19
	c_t2_a1_0_mem1 += MAIN_MEM_r[1]

	c_t3_t11_in = S.Task('c_t3_t11_in', length=1, delay_cost=1)
	S += c_t3_t11_in >= 19
	c_t3_t11_in += MAS_in[1]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 19
	c_t3_t11_mem0 += MAS_MEM[0]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 19
	c_t3_t11_mem1 += MAS_MEM[1]

	c_t3_t3_t2 = S.Task('c_t3_t3_t2', length=3, delay_cost=1)
	S += c_t3_t3_t2 >= 19
	c_t3_t3_t2 += MAS[0]

	c_t1_a1_1_in = S.Task('c_t1_a1_1_in', length=1, delay_cost=1)
	S += c_t1_a1_1_in >= 20
	c_t1_a1_1_in += MAS_in[1]

	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	S += c_t1_a1_1_mem0 >= 20
	c_t1_a1_1_mem0 += MAIN_MEM_r[0]

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	S += c_t1_a1_1_mem1 >= 20
	c_t1_a1_1_mem1 += MAIN_MEM_r[1]

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=3, delay_cost=1)
	S += c_t2_a1_0 >= 20
	c_t2_a1_0 += MAS[0]

	c_t3_t11 = S.Task('c_t3_t11', length=3, delay_cost=1)
	S += c_t3_t11 >= 20
	c_t3_t11 += MAS[1]

	c_t3_t3_t0_in = S.Task('c_t3_t3_t0_in', length=1, delay_cost=1)
	S += c_t3_t3_t0_in >= 20
	c_t3_t3_t0_in += MM_in[0]

	c_t3_t3_t0_mem0 = S.Task('c_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem0 >= 20
	c_t3_t3_t0_mem0 += MAS_MEM[0]

	c_t3_t3_t0_mem1 = S.Task('c_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem1 >= 20
	c_t3_t3_t0_mem1 += MAS_MEM[1]

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=3, delay_cost=1)
	S += c_t1_a1_1 >= 21
	c_t1_a1_1 += MAS[1]

	c_t2_t3_t3_in = S.Task('c_t2_t3_t3_in', length=1, delay_cost=1)
	S += c_t2_t3_t3_in >= 21
	c_t2_t3_t3_in += MAS_in[0]

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem0 >= 21
	c_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem1 >= 21
	c_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t3_t3_t0 = S.Task('c_t3_t3_t0', length=14, delay_cost=1)
	S += c_t3_t3_t0 >= 21
	c_t3_t3_t0 += MM[0]

	c_t3_t3_t1_in = S.Task('c_t3_t3_t1_in', length=1, delay_cost=1)
	S += c_t3_t3_t1_in >= 21
	c_t3_t3_t1_in += MM_in[0]

	c_t3_t3_t1_mem0 = S.Task('c_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem0 >= 21
	c_t3_t3_t1_mem0 += MAS_MEM[0]

	c_t3_t3_t1_mem1 = S.Task('c_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem1 >= 21
	c_t3_t3_t1_mem1 += MAS_MEM[1]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 22
	c_t1_t11_in += MAS_in[0]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 22
	c_t1_t11_mem0 += MAIN_MEM_r[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 22
	c_t1_t11_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=3, delay_cost=1)
	S += c_t2_t3_t3 >= 22
	c_t2_t3_t3 += MAS[0]

	c_t3_t3_t1 = S.Task('c_t3_t3_t1', length=14, delay_cost=1)
	S += c_t3_t3_t1 >= 22
	c_t3_t3_t1 += MM[0]

	c_t1_t11 = S.Task('c_t1_t11', length=3, delay_cost=1)
	S += c_t1_t11 >= 23
	c_t1_t11 += MAS[0]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 23
	c_t2_t10_in += MAS_in[1]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 23
	c_t2_t10_mem0 += MAIN_MEM_r[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 23
	c_t2_t10_mem1 += MAIN_MEM_r[1]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 24
	c_t0_t11_in += MAS_in[0]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 24
	c_t0_t11_mem0 += MAIN_MEM_r[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 24
	c_t0_t11_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=3, delay_cost=1)
	S += c_t2_t10 >= 24
	c_t2_t10 += MAS[1]

	c_t2_t3_t4_in = S.Task('c_t2_t3_t4_in', length=1, delay_cost=1)
	S += c_t2_t3_t4_in >= 24
	c_t2_t3_t4_in += MM_in[0]

	c_t2_t3_t4_mem0 = S.Task('c_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem0 >= 24
	c_t2_t3_t4_mem0 += MAS_MEM[0]

	c_t2_t3_t4_mem1 = S.Task('c_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem1 >= 24
	c_t2_t3_t4_mem1 += MAS_MEM[1]

	c_t0_a1_1_in = S.Task('c_t0_a1_1_in', length=1, delay_cost=1)
	S += c_t0_a1_1_in >= 25
	c_t0_a1_1_in += MAS_in[0]

	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	S += c_t0_a1_1_mem0 >= 25
	c_t0_a1_1_mem0 += MAIN_MEM_r[0]

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	S += c_t0_a1_1_mem1 >= 25
	c_t0_a1_1_mem1 += MAIN_MEM_r[1]

	c_t0_t11 = S.Task('c_t0_t11', length=3, delay_cost=1)
	S += c_t0_t11 >= 25
	c_t0_t11 += MAS[0]

	c_t1_t2_t3_in = S.Task('c_t1_t2_t3_in', length=1, delay_cost=1)
	S += c_t1_t2_t3_in >= 25
	c_t1_t2_t3_in += MAS_in[1]

	c_t1_t2_t3_mem0 = S.Task('c_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem0 >= 25
	c_t1_t2_t3_mem0 += MAS_MEM[0]

	c_t1_t2_t3_mem1 = S.Task('c_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem1 >= 25
	c_t1_t2_t3_mem1 += MAS_MEM[1]

	c_t2_t3_t4 = S.Task('c_t2_t3_t4', length=14, delay_cost=1)
	S += c_t2_t3_t4 >= 25
	c_t2_t3_t4 += MM[0]

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=3, delay_cost=1)
	S += c_t0_a1_1 >= 26
	c_t0_a1_1 += MAS[0]

	c_t1_t2_t3 = S.Task('c_t1_t2_t3', length=3, delay_cost=1)
	S += c_t1_t2_t3 >= 26
	c_t1_t2_t3 += MAS[1]

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	S += c_t1_t3_t1_in >= 26
	c_t1_t3_t1_in += MM_in[0]

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem0 >= 26
	c_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem1 >= 26
	c_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t2_t3_in = S.Task('c_t2_t2_t3_in', length=1, delay_cost=1)
	S += c_t2_t2_t3_in >= 26
	c_t2_t2_t3_in += MAS_in[0]

	c_t2_t2_t3_mem0 = S.Task('c_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem0 >= 26
	c_t2_t2_t3_mem0 += MAS_MEM[2]

	c_t2_t2_t3_mem1 = S.Task('c_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem1 >= 26
	c_t2_t2_t3_mem1 += MAS_MEM[1]

	c_t0_t2_t3_in = S.Task('c_t0_t2_t3_in', length=1, delay_cost=1)
	S += c_t0_t2_t3_in >= 27
	c_t0_t2_t3_in += MAS_in[0]

	c_t0_t2_t3_mem0 = S.Task('c_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem0 >= 27
	c_t0_t2_t3_mem0 += MAS_MEM[2]

	c_t0_t2_t3_mem1 = S.Task('c_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem1 >= 27
	c_t0_t2_t3_mem1 += MAS_MEM[1]

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	S += c_t1_t3_t0_in >= 27
	c_t1_t3_t0_in += MM_in[0]

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem0 >= 27
	c_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem1 >= 27
	c_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=14, delay_cost=1)
	S += c_t1_t3_t1 >= 27
	c_t1_t3_t1 += MM[0]

	c_t2_t2_t3 = S.Task('c_t2_t2_t3', length=3, delay_cost=1)
	S += c_t2_t2_t3 >= 27
	c_t2_t2_t3 += MAS[0]

	c_t0_t2_t3 = S.Task('c_t0_t2_t3', length=3, delay_cost=1)
	S += c_t0_t2_t3 >= 28
	c_t0_t2_t3 += MAS[0]

	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	S += c_t0_t3_t1_in >= 28
	c_t0_t3_t1_in += MM_in[0]

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem0 >= 28
	c_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem1 >= 28
	c_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=14, delay_cost=1)
	S += c_t1_t3_t0 >= 28
	c_t1_t3_t0 += MM[0]

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	S += c_t0_t3_t0_in >= 29
	c_t0_t3_t0_in += MM_in[0]

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem0 >= 29
	c_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem1 >= 29
	c_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=14, delay_cost=1)
	S += c_t0_t3_t1 >= 29
	c_t0_t3_t1 += MM[0]

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=14, delay_cost=1)
	S += c_t0_t3_t0 >= 30
	c_t0_t3_t0 += MM[0]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 30
	c_t4011_in += MAS_in[0]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 30
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 30
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t5_in = S.Task('c_t2_t3_t5_in', length=1, delay_cost=1)
	S += c_t2_t3_t5_in >= 31
	c_t2_t3_t5_in += MAS_in[0]

	c_t2_t3_t5_mem0 = S.Task('c_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem0 >= 31
	c_t2_t3_t5_mem0 += MM_MEM[0]

	c_t2_t3_t5_mem1 = S.Task('c_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem1 >= 31
	c_t2_t3_t5_mem1 += MM_MEM[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 31
	c_t4010_in += MAS_in[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 31
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 31
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4011 = S.Task('c_t4011', length=3, delay_cost=1)
	S += c_t4011 >= 31
	c_t4011 += MAS[0]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 32
	c_t2_t30_in += MAS_in[0]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 32
	c_t2_t30_mem0 += MM_MEM[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 32
	c_t2_t30_mem1 += MM_MEM[1]

	c_t2_t3_t5 = S.Task('c_t2_t3_t5', length=3, delay_cost=1)
	S += c_t2_t3_t5 >= 32
	c_t2_t3_t5 += MAS[0]

	c_t4010 = S.Task('c_t4010', length=3, delay_cost=1)
	S += c_t4010 >= 32
	c_t4010 += MAS[1]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 32
	c_t5001_in += MAS_in[1]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 32
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 32
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t2_t30 = S.Task('c_t2_t30', length=3, delay_cost=1)
	S += c_t2_t30 >= 33
	c_t2_t30 += MAS[0]

	c_t4_t11_in = S.Task('c_t4_t11_in', length=1, delay_cost=1)
	S += c_t4_t11_in >= 33
	c_t4_t11_in += MAS_in[0]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 33
	c_t4_t11_mem0 += MAS_MEM[0]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 33
	c_t4_t11_mem1 += MAS_MEM[1]

	c_t5001 = S.Task('c_t5001', length=3, delay_cost=1)
	S += c_t5001 >= 33
	c_t5001 += MAS[1]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 33
	c_t5011_in += MAS_in[1]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 33
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 33
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t4_a1_0_in = S.Task('c_t4_a1_0_in', length=1, delay_cost=1)
	S += c_t4_a1_0_in >= 34
	c_t4_a1_0_in += MAS_in[1]

	c_t4_a1_0_mem0 = S.Task('c_t4_a1_0_mem0', length=1, delay_cost=1)
	S += c_t4_a1_0_mem0 >= 34
	c_t4_a1_0_mem0 += MAS_MEM[2]

	c_t4_a1_0_mem1 = S.Task('c_t4_a1_0_mem1', length=1, delay_cost=1)
	S += c_t4_a1_0_mem1 >= 34
	c_t4_a1_0_mem1 += MAS_MEM[1]

	c_t4_t11 = S.Task('c_t4_t11', length=3, delay_cost=1)
	S += c_t4_t11 >= 34
	c_t4_t11 += MAS[0]

	c_t4_t3_t0_in = S.Task('c_t4_t3_t0_in', length=1, delay_cost=1)
	S += c_t4_t3_t0_in >= 34
	c_t4_t3_t0_in += MM_in[0]

	c_t4_t3_t0_mem0 = S.Task('c_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem0 >= 34
	c_t4_t3_t0_mem0 += MAS_MEM[0]

	c_t4_t3_t0_mem1 = S.Task('c_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem1 >= 34
	c_t4_t3_t0_mem1 += MAS_MEM[3]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 34
	c_t5010_in += MAS_in[0]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 34
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 34
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=3, delay_cost=1)
	S += c_t5011 >= 34
	c_t5011 += MAS[1]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 35
	c_t2_t00_in += MAS_in[1]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 35
	c_t2_t00_mem0 += MAIN_MEM_r[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 35
	c_t2_t00_mem1 += MAS_MEM[1]

	c_t4_a1_0 = S.Task('c_t4_a1_0', length=3, delay_cost=1)
	S += c_t4_a1_0 >= 35
	c_t4_a1_0 += MAS[1]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 35
	c_t4_t10_in += MAS_in[0]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 35
	c_t4_t10_mem0 += MAS_MEM[0]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 35
	c_t4_t10_mem1 += MAS_MEM[3]

	c_t4_t3_t0 = S.Task('c_t4_t3_t0', length=14, delay_cost=1)
	S += c_t4_t3_t0 >= 35
	c_t4_t3_t0 += MM[0]

	c_t5010 = S.Task('c_t5010', length=3, delay_cost=1)
	S += c_t5010 >= 35
	c_t5010 += MAS[0]

	c_t2_t00 = S.Task('c_t2_t00', length=3, delay_cost=1)
	S += c_t2_t00 >= 36
	c_t2_t00 += MAS[1]

	c_t4_t10 = S.Task('c_t4_t10', length=3, delay_cost=1)
	S += c_t4_t10 >= 36
	c_t4_t10 += MAS[0]

	c_t4_t3_t1_in = S.Task('c_t4_t3_t1_in', length=1, delay_cost=1)
	S += c_t4_t3_t1_in >= 36
	c_t4_t3_t1_in += MM_in[0]

	c_t4_t3_t1_mem0 = S.Task('c_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem0 >= 36
	c_t4_t3_t1_mem0 += MAS_MEM[0]

	c_t4_t3_t1_mem1 = S.Task('c_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem1 >= 36
	c_t4_t3_t1_mem1 += MAS_MEM[1]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 36
	c_t5000_in += MAS_in[1]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 36
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 36
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5_t11_in = S.Task('c_t5_t11_in', length=1, delay_cost=1)
	S += c_t5_t11_in >= 36
	c_t5_t11_in += MAS_in[0]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 36
	c_t5_t11_mem0 += MAS_MEM[2]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 36
	c_t5_t11_mem1 += MAS_MEM[3]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 37
	c_t1_t01_in += MAS_in[0]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 37
	c_t1_t01_mem0 += MAIN_MEM_r[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 37
	c_t1_t01_mem1 += MAS_MEM[3]

	c_t4_t3_t1 = S.Task('c_t4_t3_t1', length=14, delay_cost=1)
	S += c_t4_t3_t1 >= 37
	c_t4_t3_t1 += MM[0]

	c_t4_t3_t3_in = S.Task('c_t4_t3_t3_in', length=1, delay_cost=1)
	S += c_t4_t3_t3_in >= 37
	c_t4_t3_t3_in += MAS_in[1]

	c_t4_t3_t3_mem0 = S.Task('c_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem0 >= 37
	c_t4_t3_t3_mem0 += MAS_MEM[2]

	c_t4_t3_t3_mem1 = S.Task('c_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem1 >= 37
	c_t4_t3_t3_mem1 += MAS_MEM[1]

	c_t5000 = S.Task('c_t5000', length=3, delay_cost=1)
	S += c_t5000 >= 37
	c_t5000 += MAS[1]

	c_t5_t11 = S.Task('c_t5_t11', length=3, delay_cost=1)
	S += c_t5_t11 >= 37
	c_t5_t11 += MAS[0]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 38
	c_t0_t00_in += MAS_in[0]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 38
	c_t0_t00_mem0 += MAIN_MEM_r[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 38
	c_t0_t00_mem1 += MAS_MEM[1]

	c_t1_t01 = S.Task('c_t1_t01', length=3, delay_cost=1)
	S += c_t1_t01 >= 38
	c_t1_t01 += MAS[0]

	c_t4_a1_1_in = S.Task('c_t4_a1_1_in', length=1, delay_cost=1)
	S += c_t4_a1_1_in >= 38
	c_t4_a1_1_in += MAS_in[1]

	c_t4_a1_1_mem0 = S.Task('c_t4_a1_1_mem0', length=1, delay_cost=1)
	S += c_t4_a1_1_mem0 >= 38
	c_t4_a1_1_mem0 += MAS_MEM[0]

	c_t4_a1_1_mem1 = S.Task('c_t4_a1_1_mem1', length=1, delay_cost=1)
	S += c_t4_a1_1_mem1 >= 38
	c_t4_a1_1_mem1 += MAS_MEM[3]

	c_t4_t3_t3 = S.Task('c_t4_t3_t3', length=3, delay_cost=1)
	S += c_t4_t3_t3 >= 38
	c_t4_t3_t3 += MAS[1]

	c_t0_t00 = S.Task('c_t0_t00', length=3, delay_cost=1)
	S += c_t0_t00 >= 39
	c_t0_t00 += MAS[0]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 39
	c_t1_t00_in += MAS_in[0]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 39
	c_t1_t00_mem0 += MAIN_MEM_r[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 39
	c_t1_t00_mem1 += MAS_MEM[1]

	c_t4_a1_1 = S.Task('c_t4_a1_1', length=3, delay_cost=1)
	S += c_t4_a1_1 >= 39
	c_t4_a1_1 += MAS[1]

	c_t5_t3_t2_in = S.Task('c_t5_t3_t2_in', length=1, delay_cost=1)
	S += c_t5_t3_t2_in >= 39
	c_t5_t3_t2_in += MAS_in[1]

	c_t5_t3_t2_mem0 = S.Task('c_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem0 >= 39
	c_t5_t3_t2_mem0 += MAS_MEM[2]

	c_t5_t3_t2_mem1 = S.Task('c_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem1 >= 39
	c_t5_t3_t2_mem1 += MAS_MEM[3]

	c_t1_t00 = S.Task('c_t1_t00', length=3, delay_cost=1)
	S += c_t1_t00 >= 40
	c_t1_t00 += MAS[0]

	c_t5_a1_0_in = S.Task('c_t5_a1_0_in', length=1, delay_cost=1)
	S += c_t5_a1_0_in >= 40
	c_t5_a1_0_in += MAS_in[1]

	c_t5_a1_0_mem0 = S.Task('c_t5_a1_0_mem0', length=1, delay_cost=1)
	S += c_t5_a1_0_mem0 >= 40
	c_t5_a1_0_mem0 += MAS_MEM[0]

	c_t5_a1_0_mem1 = S.Task('c_t5_a1_0_mem1', length=1, delay_cost=1)
	S += c_t5_a1_0_mem1 >= 40
	c_t5_a1_0_mem1 += MAS_MEM[3]

	c_t5_a1_1_in = S.Task('c_t5_a1_1_in', length=1, delay_cost=1)
	S += c_t5_a1_1_in >= 40
	c_t5_a1_1_in += MAS_in[0]

	c_t5_a1_1_mem0 = S.Task('c_t5_a1_1_mem0', length=1, delay_cost=1)
	S += c_t5_a1_1_mem0 >= 40
	c_t5_a1_1_mem0 += MAS_MEM[2]

	c_t5_a1_1_mem1 = S.Task('c_t5_a1_1_mem1', length=1, delay_cost=1)
	S += c_t5_a1_1_mem1 >= 40
	c_t5_a1_1_mem1 += MAS_MEM[1]

	c_t5_t3_t2 = S.Task('c_t5_t3_t2', length=3, delay_cost=1)
	S += c_t5_t3_t2 >= 40
	c_t5_t3_t2 += MAS[1]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 41
	c_t1_t30_in += MAS_in[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 41
	c_t1_t30_mem0 += MM_MEM[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 41
	c_t1_t30_mem1 += MM_MEM[1]

	c_t5_a1_0 = S.Task('c_t5_a1_0', length=3, delay_cost=1)
	S += c_t5_a1_0 >= 41
	c_t5_a1_0 += MAS[1]

	c_t5_a1_1 = S.Task('c_t5_a1_1', length=3, delay_cost=1)
	S += c_t5_a1_1 >= 41
	c_t5_a1_1 += MAS[0]

	c_t5_t3_t0_in = S.Task('c_t5_t3_t0_in', length=1, delay_cost=1)
	S += c_t5_t3_t0_in >= 41
	c_t5_t3_t0_in += MM_in[0]

	c_t5_t3_t0_mem0 = S.Task('c_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem0 >= 41
	c_t5_t3_t0_mem0 += MAS_MEM[2]

	c_t5_t3_t0_mem1 = S.Task('c_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem1 >= 41
	c_t5_t3_t0_mem1 += MAS_MEM[1]

	c_t5_t3_t3_in = S.Task('c_t5_t3_t3_in', length=1, delay_cost=1)
	S += c_t5_t3_t3_in >= 41
	c_t5_t3_t3_in += MAS_in[1]

	c_t5_t3_t3_mem0 = S.Task('c_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem0 >= 41
	c_t5_t3_t3_mem0 += MAS_MEM[0]

	c_t5_t3_t3_mem1 = S.Task('c_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem1 >= 41
	c_t5_t3_t3_mem1 += MAS_MEM[3]

	c_t1_t30 = S.Task('c_t1_t30', length=3, delay_cost=1)
	S += c_t1_t30 >= 42
	c_t1_t30 += MAS[0]

	c_t1_t3_t5_in = S.Task('c_t1_t3_t5_in', length=1, delay_cost=1)
	S += c_t1_t3_t5_in >= 42
	c_t1_t3_t5_in += MAS_in[1]

	c_t1_t3_t5_mem0 = S.Task('c_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem0 >= 42
	c_t1_t3_t5_mem0 += MM_MEM[0]

	c_t1_t3_t5_mem1 = S.Task('c_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem1 >= 42
	c_t1_t3_t5_mem1 += MM_MEM[1]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 42
	c_t2_t01_in += MAS_in[0]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 42
	c_t2_t01_mem0 += MAIN_MEM_r[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 42
	c_t2_t01_mem1 += MAS_MEM[1]

	c_t5_t3_t0 = S.Task('c_t5_t3_t0', length=14, delay_cost=1)
	S += c_t5_t3_t0 >= 42
	c_t5_t3_t0 += MM[0]

	c_t5_t3_t1_in = S.Task('c_t5_t3_t1_in', length=1, delay_cost=1)
	S += c_t5_t3_t1_in >= 42
	c_t5_t3_t1_in += MM_in[0]

	c_t5_t3_t1_mem0 = S.Task('c_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem0 >= 42
	c_t5_t3_t1_mem0 += MAS_MEM[2]

	c_t5_t3_t1_mem1 = S.Task('c_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem1 >= 42
	c_t5_t3_t1_mem1 += MAS_MEM[3]

	c_t5_t3_t3 = S.Task('c_t5_t3_t3', length=3, delay_cost=1)
	S += c_t5_t3_t3 >= 42
	c_t5_t3_t3 += MAS[1]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 43
	c_t0_t01_in += MAS_in[1]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 43
	c_t0_t01_mem0 += MAIN_MEM_r[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 43
	c_t0_t01_mem1 += MAS_MEM[1]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 43
	c_t0_t30_in += MAS_in[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 43
	c_t0_t30_mem0 += MM_MEM[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 43
	c_t0_t30_mem1 += MM_MEM[1]

	c_t1_t3_t5 = S.Task('c_t1_t3_t5', length=3, delay_cost=1)
	S += c_t1_t3_t5 >= 43
	c_t1_t3_t5 += MAS[1]

	c_t2_t01 = S.Task('c_t2_t01', length=3, delay_cost=1)
	S += c_t2_t01 >= 43
	c_t2_t01 += MAS[0]

	c_t5_t3_t1 = S.Task('c_t5_t3_t1', length=14, delay_cost=1)
	S += c_t5_t3_t1 >= 43
	c_t5_t3_t1 += MM[0]

	c_t0_t01 = S.Task('c_t0_t01', length=3, delay_cost=1)
	S += c_t0_t01 >= 44
	c_t0_t01 += MAS[1]

	c_t0_t30 = S.Task('c_t0_t30', length=3, delay_cost=1)
	S += c_t0_t30 >= 44
	c_t0_t30 += MAS[0]

	c_t0_t3_t5_in = S.Task('c_t0_t3_t5_in', length=1, delay_cost=1)
	S += c_t0_t3_t5_in >= 44
	c_t0_t3_t5_in += MAS_in[0]

	c_t0_t3_t5_mem0 = S.Task('c_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem0 >= 44
	c_t0_t3_t5_mem0 += MM_MEM[0]

	c_t0_t3_t5_mem1 = S.Task('c_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem1 >= 44
	c_t0_t3_t5_mem1 += MM_MEM[1]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 44
	c_t5_t10_in += MAS_in[1]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 44
	c_t5_t10_mem0 += MAS_MEM[2]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 44
	c_t5_t10_mem1 += MAS_MEM[1]

	c_t0_t3_t5 = S.Task('c_t0_t3_t5', length=3, delay_cost=1)
	S += c_t0_t3_t5 >= 45
	c_t0_t3_t5 += MAS[0]

	c_t5_t10 = S.Task('c_t5_t10', length=3, delay_cost=1)
	S += c_t5_t10 >= 45
	c_t5_t10 += MAS[1]


	# new tasks
	c_t0_t2_t0 = S.Task('c_t0_t2_t0', length=14, delay_cost=1)
	c_t0_t2_t0 += alt(MM)
	c_t0_t2_t0_in = S.Task('c_t0_t2_t0_in', length=1, delay_cost=1)
	c_t0_t2_t0_in += alt(MM_in)
	S += c_t0_t2_t0_in*MM_in[0]<=c_t0_t2_t0*MM[0]
	c_t0_t2_t0_mem0 = S.Task('c_t0_t2_t0_mem0', length=1, delay_cost=1)
	c_t0_t2_t0_mem0 += MAS_MEM[0]
	S += 41 < c_t0_t2_t0_mem0
	S += c_t0_t2_t0_mem0 <= c_t0_t2_t0

	c_t0_t2_t0_mem1 = S.Task('c_t0_t2_t0_mem1', length=1, delay_cost=1)
	c_t0_t2_t0_mem1 += MAS_MEM[3]
	S += 21 < c_t0_t2_t0_mem1
	S += c_t0_t2_t0_mem1 <= c_t0_t2_t0

	c_t0_t2_t1 = S.Task('c_t0_t2_t1', length=14, delay_cost=1)
	c_t0_t2_t1 += alt(MM)
	c_t0_t2_t1_in = S.Task('c_t0_t2_t1_in', length=1, delay_cost=1)
	c_t0_t2_t1_in += alt(MM_in)
	S += c_t0_t2_t1_in*MM_in[0]<=c_t0_t2_t1*MM[0]
	c_t0_t2_t1_mem0 = S.Task('c_t0_t2_t1_mem0', length=1, delay_cost=1)
	c_t0_t2_t1_mem0 += MAS_MEM[2]
	S += 46 < c_t0_t2_t1_mem0
	S += c_t0_t2_t1_mem0 <= c_t0_t2_t1

	c_t0_t2_t1_mem1 = S.Task('c_t0_t2_t1_mem1', length=1, delay_cost=1)
	c_t0_t2_t1_mem1 += MAS_MEM[1]
	S += 27 < c_t0_t2_t1_mem1
	S += c_t0_t2_t1_mem1 <= c_t0_t2_t1

	c_t0_t2_t2 = S.Task('c_t0_t2_t2', length=3, delay_cost=1)
	c_t0_t2_t2 += alt(MAS)
	c_t0_t2_t2_in = S.Task('c_t0_t2_t2_in', length=1, delay_cost=1)
	c_t0_t2_t2_in += alt(MAS_in)
	S += c_t0_t2_t2_in*MAS_in[0]<=c_t0_t2_t2*MAS[0]

	S += c_t0_t2_t2_in*MAS_in[1]<=c_t0_t2_t2*MAS[1]

	c_t0_t2_t2_mem0 = S.Task('c_t0_t2_t2_mem0', length=1, delay_cost=1)
	c_t0_t2_t2_mem0 += MAS_MEM[0]
	S += 41 < c_t0_t2_t2_mem0
	S += c_t0_t2_t2_mem0 <= c_t0_t2_t2

	c_t0_t2_t2_mem1 = S.Task('c_t0_t2_t2_mem1', length=1, delay_cost=1)
	c_t0_t2_t2_mem1 += MAS_MEM[3]
	S += 46 < c_t0_t2_t2_mem1
	S += c_t0_t2_t2_mem1 <= c_t0_t2_t2

	c_t0_t31 = S.Task('c_t0_t31', length=3, delay_cost=1)
	c_t0_t31 += alt(MAS)
	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	c_t0_t31_in += alt(MAS_in)
	S += c_t0_t31_in*MAS_in[0]<=c_t0_t31*MAS[0]

	S += c_t0_t31_in*MAS_in[1]<=c_t0_t31*MAS[1]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	c_t0_t31_mem0 += MM_MEM[0]
	S += 29 < c_t0_t31_mem0
	S += c_t0_t31_mem0 <= c_t0_t31

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	c_t0_t31_mem1 += MAS_MEM[1]
	S += 47 < c_t0_t31_mem1
	S += c_t0_t31_mem1 <= c_t0_t31

	c_t010 = S.Task('c_t010', length=3, delay_cost=1)
	c_t010 += alt(MAS)
	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	c_t010_in += alt(MAS_in)
	S += c_t010_in*MAS_in[0]<=c_t010*MAS[0]

	S += c_t010_in*MAS_in[1]<=c_t010*MAS[1]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	c_t010_mem0 += MAS_MEM[0]
	S += 46 < c_t010_mem0
	S += c_t010_mem0 <= c_t010

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	c_t010_mem1 += MAS_MEM[1]
	S += 46 < c_t010_mem1
	S += c_t010_mem1 <= c_t010

	c_t1_t2_t0 = S.Task('c_t1_t2_t0', length=14, delay_cost=1)
	c_t1_t2_t0 += alt(MM)
	c_t1_t2_t0_in = S.Task('c_t1_t2_t0_in', length=1, delay_cost=1)
	c_t1_t2_t0_in += alt(MM_in)
	S += c_t1_t2_t0_in*MM_in[0]<=c_t1_t2_t0*MM[0]
	c_t1_t2_t0_mem0 = S.Task('c_t1_t2_t0_mem0', length=1, delay_cost=1)
	c_t1_t2_t0_mem0 += MAS_MEM[0]
	S += 42 < c_t1_t2_t0_mem0
	S += c_t1_t2_t0_mem0 <= c_t1_t2_t0

	c_t1_t2_t0_mem1 = S.Task('c_t1_t2_t0_mem1', length=1, delay_cost=1)
	c_t1_t2_t0_mem1 += MAS_MEM[1]
	S += 14 < c_t1_t2_t0_mem1
	S += c_t1_t2_t0_mem1 <= c_t1_t2_t0

	c_t1_t2_t1 = S.Task('c_t1_t2_t1', length=14, delay_cost=1)
	c_t1_t2_t1 += alt(MM)
	c_t1_t2_t1_in = S.Task('c_t1_t2_t1_in', length=1, delay_cost=1)
	c_t1_t2_t1_in += alt(MM_in)
	S += c_t1_t2_t1_in*MM_in[0]<=c_t1_t2_t1*MM[0]
	c_t1_t2_t1_mem0 = S.Task('c_t1_t2_t1_mem0', length=1, delay_cost=1)
	c_t1_t2_t1_mem0 += MAS_MEM[0]
	S += 40 < c_t1_t2_t1_mem0
	S += c_t1_t2_t1_mem0 <= c_t1_t2_t1

	c_t1_t2_t1_mem1 = S.Task('c_t1_t2_t1_mem1', length=1, delay_cost=1)
	c_t1_t2_t1_mem1 += MAS_MEM[1]
	S += 25 < c_t1_t2_t1_mem1
	S += c_t1_t2_t1_mem1 <= c_t1_t2_t1

	c_t1_t2_t2 = S.Task('c_t1_t2_t2', length=3, delay_cost=1)
	c_t1_t2_t2 += alt(MAS)
	c_t1_t2_t2_in = S.Task('c_t1_t2_t2_in', length=1, delay_cost=1)
	c_t1_t2_t2_in += alt(MAS_in)
	S += c_t1_t2_t2_in*MAS_in[0]<=c_t1_t2_t2*MAS[0]

	S += c_t1_t2_t2_in*MAS_in[1]<=c_t1_t2_t2*MAS[1]

	c_t1_t2_t2_mem0 = S.Task('c_t1_t2_t2_mem0', length=1, delay_cost=1)
	c_t1_t2_t2_mem0 += MAS_MEM[0]
	S += 42 < c_t1_t2_t2_mem0
	S += c_t1_t2_t2_mem0 <= c_t1_t2_t2

	c_t1_t2_t2_mem1 = S.Task('c_t1_t2_t2_mem1', length=1, delay_cost=1)
	c_t1_t2_t2_mem1 += MAS_MEM[1]
	S += 40 < c_t1_t2_t2_mem1
	S += c_t1_t2_t2_mem1 <= c_t1_t2_t2

	c_t1_t31 = S.Task('c_t1_t31', length=3, delay_cost=1)
	c_t1_t31 += alt(MAS)
	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	c_t1_t31_in += alt(MAS_in)
	S += c_t1_t31_in*MAS_in[0]<=c_t1_t31*MAS[0]

	S += c_t1_t31_in*MAS_in[1]<=c_t1_t31*MAS[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	c_t1_t31_mem0 += MM_MEM[0]
	S += 23 < c_t1_t31_mem0
	S += c_t1_t31_mem0 <= c_t1_t31

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	c_t1_t31_mem1 += MAS_MEM[3]
	S += 45 < c_t1_t31_mem1
	S += c_t1_t31_mem1 <= c_t1_t31

	c_t110 = S.Task('c_t110', length=3, delay_cost=1)
	c_t110 += alt(MAS)
	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	c_t110_in += alt(MAS_in)
	S += c_t110_in*MAS_in[0]<=c_t110*MAS[0]

	S += c_t110_in*MAS_in[1]<=c_t110*MAS[1]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	c_t110_mem0 += MAS_MEM[0]
	S += 44 < c_t110_mem0
	S += c_t110_mem0 <= c_t110

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	c_t110_mem1 += MAS_MEM[1]
	S += 44 < c_t110_mem1
	S += c_t110_mem1 <= c_t110

	c_t2_t2_t0 = S.Task('c_t2_t2_t0', length=14, delay_cost=1)
	c_t2_t2_t0 += alt(MM)
	c_t2_t2_t0_in = S.Task('c_t2_t2_t0_in', length=1, delay_cost=1)
	c_t2_t2_t0_in += alt(MM_in)
	S += c_t2_t2_t0_in*MM_in[0]<=c_t2_t2_t0*MM[0]
	c_t2_t2_t0_mem0 = S.Task('c_t2_t2_t0_mem0', length=1, delay_cost=1)
	c_t2_t2_t0_mem0 += MAS_MEM[2]
	S += 38 < c_t2_t2_t0_mem0
	S += c_t2_t2_t0_mem0 <= c_t2_t2_t0

	c_t2_t2_t0_mem1 = S.Task('c_t2_t2_t0_mem1', length=1, delay_cost=1)
	c_t2_t2_t0_mem1 += MAS_MEM[3]
	S += 26 < c_t2_t2_t0_mem1
	S += c_t2_t2_t0_mem1 <= c_t2_t2_t0

	c_t2_t2_t1 = S.Task('c_t2_t2_t1', length=14, delay_cost=1)
	c_t2_t2_t1 += alt(MM)
	c_t2_t2_t1_in = S.Task('c_t2_t2_t1_in', length=1, delay_cost=1)
	c_t2_t2_t1_in += alt(MM_in)
	S += c_t2_t2_t1_in*MM_in[0]<=c_t2_t2_t1*MM[0]
	c_t2_t2_t1_mem0 = S.Task('c_t2_t2_t1_mem0', length=1, delay_cost=1)
	c_t2_t2_t1_mem0 += MAS_MEM[0]
	S += 45 < c_t2_t2_t1_mem0
	S += c_t2_t2_t1_mem0 <= c_t2_t2_t1

	c_t2_t2_t1_mem1 = S.Task('c_t2_t2_t1_mem1', length=1, delay_cost=1)
	c_t2_t2_t1_mem1 += MAS_MEM[1]
	S += 13 < c_t2_t2_t1_mem1
	S += c_t2_t2_t1_mem1 <= c_t2_t2_t1

	c_t2_t2_t2 = S.Task('c_t2_t2_t2', length=3, delay_cost=1)
	c_t2_t2_t2 += alt(MAS)
	c_t2_t2_t2_in = S.Task('c_t2_t2_t2_in', length=1, delay_cost=1)
	c_t2_t2_t2_in += alt(MAS_in)
	S += c_t2_t2_t2_in*MAS_in[0]<=c_t2_t2_t2*MAS[0]

	S += c_t2_t2_t2_in*MAS_in[1]<=c_t2_t2_t2*MAS[1]

	c_t2_t2_t2_mem0 = S.Task('c_t2_t2_t2_mem0', length=1, delay_cost=1)
	c_t2_t2_t2_mem0 += MAS_MEM[2]
	S += 38 < c_t2_t2_t2_mem0
	S += c_t2_t2_t2_mem0 <= c_t2_t2_t2

	c_t2_t2_t2_mem1 = S.Task('c_t2_t2_t2_mem1', length=1, delay_cost=1)
	c_t2_t2_t2_mem1 += MAS_MEM[1]
	S += 45 < c_t2_t2_t2_mem1
	S += c_t2_t2_t2_mem1 <= c_t2_t2_t2

	c_t2_t31 = S.Task('c_t2_t31', length=3, delay_cost=1)
	c_t2_t31 += alt(MAS)
	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	c_t2_t31_in += alt(MAS_in)
	S += c_t2_t31_in*MAS_in[0]<=c_t2_t31*MAS[0]

	S += c_t2_t31_in*MAS_in[1]<=c_t2_t31*MAS[1]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	c_t2_t31_mem0 += MM_MEM[0]
	S += 38 < c_t2_t31_mem0
	S += c_t2_t31_mem0 <= c_t2_t31

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	c_t2_t31_mem1 += MAS_MEM[1]
	S += 34 < c_t2_t31_mem1
	S += c_t2_t31_mem1 <= c_t2_t31

	c_t210 = S.Task('c_t210', length=3, delay_cost=1)
	c_t210 += alt(MAS)
	c_t210_in = S.Task('c_t210_in', length=1, delay_cost=1)
	c_t210_in += alt(MAS_in)
	S += c_t210_in*MAS_in[0]<=c_t210*MAS[0]

	S += c_t210_in*MAS_in[1]<=c_t210*MAS[1]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	c_t210_mem0 += MAS_MEM[0]
	S += 35 < c_t210_mem0
	S += c_t210_mem0 <= c_t210

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	c_t210_mem1 += MAS_MEM[1]
	S += 35 < c_t210_mem1
	S += c_t210_mem1 <= c_t210

	c_t3_t00 = S.Task('c_t3_t00', length=3, delay_cost=1)
	c_t3_t00 += alt(MAS)
	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	c_t3_t00_in += alt(MAS_in)
	S += c_t3_t00_in*MAS_in[0]<=c_t3_t00*MAS[0]

	S += c_t3_t00_in*MAS_in[1]<=c_t3_t00*MAS[1]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	c_t3_t00_mem0 += MAS_MEM[0]
	S += 16 < c_t3_t00_mem0
	S += c_t3_t00_mem0 <= c_t3_t00

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	c_t3_t00_mem1 += MAS_MEM[3]
	S += 11 < c_t3_t00_mem1
	S += c_t3_t00_mem1 <= c_t3_t00

	c_t3_t01 = S.Task('c_t3_t01', length=3, delay_cost=1)
	c_t3_t01 += alt(MAS)
	c_t3_t01_in = S.Task('c_t3_t01_in', length=1, delay_cost=1)
	c_t3_t01_in += alt(MAS_in)
	S += c_t3_t01_in*MAS_in[0]<=c_t3_t01*MAS[0]

	S += c_t3_t01_in*MAS_in[1]<=c_t3_t01*MAS[1]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	c_t3_t01_mem0 += MAS_MEM[0]
	S += 18 < c_t3_t01_mem0
	S += c_t3_t01_mem0 <= c_t3_t01

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	c_t3_t01_mem1 += MAS_MEM[3]
	S += 13 < c_t3_t01_mem1
	S += c_t3_t01_mem1 <= c_t3_t01

	c_t3_t2_t3 = S.Task('c_t3_t2_t3', length=3, delay_cost=1)
	c_t3_t2_t3 += alt(MAS)
	c_t3_t2_t3_in = S.Task('c_t3_t2_t3_in', length=1, delay_cost=1)
	c_t3_t2_t3_in += alt(MAS_in)
	S += c_t3_t2_t3_in*MAS_in[0]<=c_t3_t2_t3*MAS[0]

	S += c_t3_t2_t3_in*MAS_in[1]<=c_t3_t2_t3*MAS[1]

	c_t3_t2_t3_mem0 = S.Task('c_t3_t2_t3_mem0', length=1, delay_cost=1)
	c_t3_t2_t3_mem0 += MAS_MEM[0]
	S += 19 < c_t3_t2_t3_mem0
	S += c_t3_t2_t3_mem0 <= c_t3_t2_t3

	c_t3_t2_t3_mem1 = S.Task('c_t3_t2_t3_mem1', length=1, delay_cost=1)
	c_t3_t2_t3_mem1 += MAS_MEM[3]
	S += 22 < c_t3_t2_t3_mem1
	S += c_t3_t2_t3_mem1 <= c_t3_t2_t3

	c_t3_t3_t4 = S.Task('c_t3_t3_t4', length=14, delay_cost=1)
	c_t3_t3_t4 += alt(MM)
	c_t3_t3_t4_in = S.Task('c_t3_t3_t4_in', length=1, delay_cost=1)
	c_t3_t3_t4_in += alt(MM_in)
	S += c_t3_t3_t4_in*MM_in[0]<=c_t3_t3_t4*MM[0]
	c_t3_t3_t4_mem0 = S.Task('c_t3_t3_t4_mem0', length=1, delay_cost=1)
	c_t3_t3_t4_mem0 += MAS_MEM[0]
	S += 21 < c_t3_t3_t4_mem0
	S += c_t3_t3_t4_mem0 <= c_t3_t3_t4

	c_t3_t3_t4_mem1 = S.Task('c_t3_t3_t4_mem1', length=1, delay_cost=1)
	c_t3_t3_t4_mem1 += MAS_MEM[3]
	S += 9 < c_t3_t3_t4_mem1
	S += c_t3_t3_t4_mem1 <= c_t3_t3_t4

	c_t3_t30 = S.Task('c_t3_t30', length=3, delay_cost=1)
	c_t3_t30 += alt(MAS)
	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	c_t3_t30_in += alt(MAS_in)
	S += c_t3_t30_in*MAS_in[0]<=c_t3_t30*MAS[0]

	S += c_t3_t30_in*MAS_in[1]<=c_t3_t30*MAS[1]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	c_t3_t30_mem0 += MM_MEM[0]
	S += 34 < c_t3_t30_mem0
	S += c_t3_t30_mem0 <= c_t3_t30

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	c_t3_t30_mem1 += MM_MEM[1]
	S += 35 < c_t3_t30_mem1
	S += c_t3_t30_mem1 <= c_t3_t30

	c_t3_t3_t5 = S.Task('c_t3_t3_t5', length=3, delay_cost=1)
	c_t3_t3_t5 += alt(MAS)
	c_t3_t3_t5_in = S.Task('c_t3_t3_t5_in', length=1, delay_cost=1)
	c_t3_t3_t5_in += alt(MAS_in)
	S += c_t3_t3_t5_in*MAS_in[0]<=c_t3_t3_t5*MAS[0]

	S += c_t3_t3_t5_in*MAS_in[1]<=c_t3_t3_t5*MAS[1]

	c_t3_t3_t5_mem0 = S.Task('c_t3_t3_t5_mem0', length=1, delay_cost=1)
	c_t3_t3_t5_mem0 += MM_MEM[0]
	S += 34 < c_t3_t3_t5_mem0
	S += c_t3_t3_t5_mem0 <= c_t3_t3_t5

	c_t3_t3_t5_mem1 = S.Task('c_t3_t3_t5_mem1', length=1, delay_cost=1)
	c_t3_t3_t5_mem1 += MM_MEM[1]
	S += 35 < c_t3_t3_t5_mem1
	S += c_t3_t3_t5_mem1 <= c_t3_t3_t5

	c_t4_t00 = S.Task('c_t4_t00', length=3, delay_cost=1)
	c_t4_t00 += alt(MAS)
	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	c_t4_t00_in += alt(MAS_in)
	S += c_t4_t00_in*MAS_in[0]<=c_t4_t00*MAS[0]

	S += c_t4_t00_in*MAS_in[1]<=c_t4_t00*MAS[1]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	c_t4_t00_mem0 += MAS_MEM[0]
	S += 5 < c_t4_t00_mem0
	S += c_t4_t00_mem0 <= c_t4_t00

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	c_t4_t00_mem1 += MAS_MEM[3]
	S += 37 < c_t4_t00_mem1
	S += c_t4_t00_mem1 <= c_t4_t00

	c_t4_t01 = S.Task('c_t4_t01', length=3, delay_cost=1)
	c_t4_t01 += alt(MAS)
	c_t4_t01_in = S.Task('c_t4_t01_in', length=1, delay_cost=1)
	c_t4_t01_in += alt(MAS_in)
	S += c_t4_t01_in*MAS_in[0]<=c_t4_t01*MAS[0]

	S += c_t4_t01_in*MAS_in[1]<=c_t4_t01*MAS[1]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	c_t4_t01_mem0 += MAS_MEM[0]
	S += 7 < c_t4_t01_mem0
	S += c_t4_t01_mem0 <= c_t4_t01

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	c_t4_t01_mem1 += MAS_MEM[3]
	S += 41 < c_t4_t01_mem1
	S += c_t4_t01_mem1 <= c_t4_t01

	c_t4_t2_t3 = S.Task('c_t4_t2_t3', length=3, delay_cost=1)
	c_t4_t2_t3 += alt(MAS)
	c_t4_t2_t3_in = S.Task('c_t4_t2_t3_in', length=1, delay_cost=1)
	c_t4_t2_t3_in += alt(MAS_in)
	S += c_t4_t2_t3_in*MAS_in[0]<=c_t4_t2_t3*MAS[0]

	S += c_t4_t2_t3_in*MAS_in[1]<=c_t4_t2_t3*MAS[1]

	c_t4_t2_t3_mem0 = S.Task('c_t4_t2_t3_mem0', length=1, delay_cost=1)
	c_t4_t2_t3_mem0 += MAS_MEM[0]
	S += 38 < c_t4_t2_t3_mem0
	S += c_t4_t2_t3_mem0 <= c_t4_t2_t3

	c_t4_t2_t3_mem1 = S.Task('c_t4_t2_t3_mem1', length=1, delay_cost=1)
	c_t4_t2_t3_mem1 += MAS_MEM[1]
	S += 36 < c_t4_t2_t3_mem1
	S += c_t4_t2_t3_mem1 <= c_t4_t2_t3

	c_t4_t3_t4 = S.Task('c_t4_t3_t4', length=14, delay_cost=1)
	c_t4_t3_t4 += alt(MM)
	c_t4_t3_t4_in = S.Task('c_t4_t3_t4_in', length=1, delay_cost=1)
	c_t4_t3_t4_in += alt(MM_in)
	S += c_t4_t3_t4_in*MM_in[0]<=c_t4_t3_t4*MM[0]
	c_t4_t3_t4_mem0 = S.Task('c_t4_t3_t4_mem0', length=1, delay_cost=1)
	c_t4_t3_t4_mem0 += MAS_MEM[2]
	S += 10 < c_t4_t3_t4_mem0
	S += c_t4_t3_t4_mem0 <= c_t4_t3_t4

	c_t4_t3_t4_mem1 = S.Task('c_t4_t3_t4_mem1', length=1, delay_cost=1)
	c_t4_t3_t4_mem1 += MAS_MEM[3]
	S += 40 < c_t4_t3_t4_mem1
	S += c_t4_t3_t4_mem1 <= c_t4_t3_t4

	c_t4_t30 = S.Task('c_t4_t30', length=3, delay_cost=1)
	c_t4_t30 += alt(MAS)
	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	c_t4_t30_in += alt(MAS_in)
	S += c_t4_t30_in*MAS_in[0]<=c_t4_t30*MAS[0]

	S += c_t4_t30_in*MAS_in[1]<=c_t4_t30*MAS[1]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	c_t4_t30_mem0 += MM_MEM[0]
	S += 48 < c_t4_t30_mem0
	S += c_t4_t30_mem0 <= c_t4_t30

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	c_t4_t30_mem1 += MM_MEM[1]
	S += 50 < c_t4_t30_mem1
	S += c_t4_t30_mem1 <= c_t4_t30

	c_t4_t3_t5 = S.Task('c_t4_t3_t5', length=3, delay_cost=1)
	c_t4_t3_t5 += alt(MAS)
	c_t4_t3_t5_in = S.Task('c_t4_t3_t5_in', length=1, delay_cost=1)
	c_t4_t3_t5_in += alt(MAS_in)
	S += c_t4_t3_t5_in*MAS_in[0]<=c_t4_t3_t5*MAS[0]

	S += c_t4_t3_t5_in*MAS_in[1]<=c_t4_t3_t5*MAS[1]

	c_t4_t3_t5_mem0 = S.Task('c_t4_t3_t5_mem0', length=1, delay_cost=1)
	c_t4_t3_t5_mem0 += MM_MEM[0]
	S += 48 < c_t4_t3_t5_mem0
	S += c_t4_t3_t5_mem0 <= c_t4_t3_t5

	c_t4_t3_t5_mem1 = S.Task('c_t4_t3_t5_mem1', length=1, delay_cost=1)
	c_t4_t3_t5_mem1 += MM_MEM[1]
	S += 50 < c_t4_t3_t5_mem1
	S += c_t4_t3_t5_mem1 <= c_t4_t3_t5

	c_t5_t00 = S.Task('c_t5_t00', length=3, delay_cost=1)
	c_t5_t00 += alt(MAS)
	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	c_t5_t00_in += alt(MAS_in)
	S += c_t5_t00_in*MAS_in[0]<=c_t5_t00*MAS[0]

	S += c_t5_t00_in*MAS_in[1]<=c_t5_t00*MAS[1]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	c_t5_t00_mem0 += MAS_MEM[2]
	S += 39 < c_t5_t00_mem0
	S += c_t5_t00_mem0 <= c_t5_t00

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	c_t5_t00_mem1 += MAS_MEM[3]
	S += 43 < c_t5_t00_mem1
	S += c_t5_t00_mem1 <= c_t5_t00

	c_t5_t01 = S.Task('c_t5_t01', length=3, delay_cost=1)
	c_t5_t01 += alt(MAS)
	c_t5_t01_in = S.Task('c_t5_t01_in', length=1, delay_cost=1)
	c_t5_t01_in += alt(MAS_in)
	S += c_t5_t01_in*MAS_in[0]<=c_t5_t01*MAS[0]

	S += c_t5_t01_in*MAS_in[1]<=c_t5_t01*MAS[1]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	c_t5_t01_mem0 += MAS_MEM[2]
	S += 35 < c_t5_t01_mem0
	S += c_t5_t01_mem0 <= c_t5_t01

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	c_t5_t01_mem1 += MAS_MEM[1]
	S += 43 < c_t5_t01_mem1
	S += c_t5_t01_mem1 <= c_t5_t01

	c_t5_t2_t3 = S.Task('c_t5_t2_t3', length=3, delay_cost=1)
	c_t5_t2_t3 += alt(MAS)
	c_t5_t2_t3_in = S.Task('c_t5_t2_t3_in', length=1, delay_cost=1)
	c_t5_t2_t3_in += alt(MAS_in)
	S += c_t5_t2_t3_in*MAS_in[0]<=c_t5_t2_t3*MAS[0]

	S += c_t5_t2_t3_in*MAS_in[1]<=c_t5_t2_t3*MAS[1]

	c_t5_t2_t3_mem0 = S.Task('c_t5_t2_t3_mem0', length=1, delay_cost=1)
	c_t5_t2_t3_mem0 += MAS_MEM[2]
	S += 47 < c_t5_t2_t3_mem0
	S += c_t5_t2_t3_mem0 <= c_t5_t2_t3

	c_t5_t2_t3_mem1 = S.Task('c_t5_t2_t3_mem1', length=1, delay_cost=1)
	c_t5_t2_t3_mem1 += MAS_MEM[1]
	S += 39 < c_t5_t2_t3_mem1
	S += c_t5_t2_t3_mem1 <= c_t5_t2_t3

	c_t5_t3_t4 = S.Task('c_t5_t3_t4', length=14, delay_cost=1)
	c_t5_t3_t4 += alt(MM)
	c_t5_t3_t4_in = S.Task('c_t5_t3_t4_in', length=1, delay_cost=1)
	c_t5_t3_t4_in += alt(MM_in)
	S += c_t5_t3_t4_in*MM_in[0]<=c_t5_t3_t4*MM[0]
	c_t5_t3_t4_mem0 = S.Task('c_t5_t3_t4_mem0', length=1, delay_cost=1)
	c_t5_t3_t4_mem0 += MAS_MEM[2]
	S += 42 < c_t5_t3_t4_mem0
	S += c_t5_t3_t4_mem0 <= c_t5_t3_t4

	c_t5_t3_t4_mem1 = S.Task('c_t5_t3_t4_mem1', length=1, delay_cost=1)
	c_t5_t3_t4_mem1 += MAS_MEM[3]
	S += 44 < c_t5_t3_t4_mem1
	S += c_t5_t3_t4_mem1 <= c_t5_t3_t4

	c_t5_t30 = S.Task('c_t5_t30', length=3, delay_cost=1)
	c_t5_t30 += alt(MAS)
	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	c_t5_t30_in += alt(MAS_in)
	S += c_t5_t30_in*MAS_in[0]<=c_t5_t30*MAS[0]

	S += c_t5_t30_in*MAS_in[1]<=c_t5_t30*MAS[1]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	c_t5_t30_mem0 += MM_MEM[0]
	S += 55 < c_t5_t30_mem0
	S += c_t5_t30_mem0 <= c_t5_t30

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	c_t5_t30_mem1 += MM_MEM[1]
	S += 56 < c_t5_t30_mem1
	S += c_t5_t30_mem1 <= c_t5_t30

	c_t5_t3_t5 = S.Task('c_t5_t3_t5', length=3, delay_cost=1)
	c_t5_t3_t5 += alt(MAS)
	c_t5_t3_t5_in = S.Task('c_t5_t3_t5_in', length=1, delay_cost=1)
	c_t5_t3_t5_in += alt(MAS_in)
	S += c_t5_t3_t5_in*MAS_in[0]<=c_t5_t3_t5*MAS[0]

	S += c_t5_t3_t5_in*MAS_in[1]<=c_t5_t3_t5*MAS[1]

	c_t5_t3_t5_mem0 = S.Task('c_t5_t3_t5_mem0', length=1, delay_cost=1)
	c_t5_t3_t5_mem0 += MM_MEM[0]
	S += 55 < c_t5_t3_t5_mem0
	S += c_t5_t3_t5_mem0 <= c_t5_t3_t5

	c_t5_t3_t5_mem1 = S.Task('c_t5_t3_t5_mem1', length=1, delay_cost=1)
	c_t5_t3_t5_mem1 += MM_MEM[1]
	S += 56 < c_t5_t3_t5_mem1
	S += c_t5_t3_t5_mem1 <= c_t5_t3_t5

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM1_stage3MAS2/SQR/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution
