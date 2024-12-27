from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 178
	S = Scenario("schedule4", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=5)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 0
	c_t3011_in += MAS_in[4]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 0
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 0
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t2_in = S.Task('c_t1_t3_t2_in', length=1, delay_cost=1)
	S += c_t1_t3_t2_in >= 1
	c_t1_t3_t2_in += MAS_in[0]

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem0 >= 1
	c_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem1 >= 1
	c_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=2, delay_cost=1)
	S += c_t3011 >= 1
	c_t3011 += MAS[4]

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=2, delay_cost=1)
	S += c_t1_t3_t2 >= 2
	c_t1_t3_t2 += MAS[0]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 2
	c_t3010_in += MAS_in[0]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 2
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 2
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t1_a1_0_in = S.Task('c_t1_a1_0_in', length=1, delay_cost=1)
	S += c_t1_a1_0_in >= 3
	c_t1_a1_0_in += MAS_in[0]

	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	S += c_t1_a1_0_mem0 >= 3
	c_t1_a1_0_mem0 += MAIN_MEM_r[0]

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	S += c_t1_a1_0_mem1 >= 3
	c_t1_a1_0_mem1 += MAIN_MEM_r[1]

	c_t3010 = S.Task('c_t3010', length=2, delay_cost=1)
	S += c_t3010 >= 3
	c_t3010 += MAS[0]

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=2, delay_cost=1)
	S += c_t1_a1_0 >= 4
	c_t1_a1_0 += MAS[0]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 4
	c_t2_t11_in += MAS_in[2]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 4
	c_t2_t11_mem0 += MAIN_MEM_r[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 4
	c_t2_t11_mem1 += MAIN_MEM_r[1]

	c_t3_a1_1_in = S.Task('c_t3_a1_1_in', length=1, delay_cost=1)
	S += c_t3_a1_1_in >= 4
	c_t3_a1_1_in += MAS_in[3]

	c_t3_a1_1_mem0 = S.Task('c_t3_a1_1_mem0', length=1, delay_cost=1)
	S += c_t3_a1_1_mem0 >= 4
	c_t3_a1_1_mem0 += MAS_MEM[8]

	c_t3_a1_1_mem1 = S.Task('c_t3_a1_1_mem1', length=1, delay_cost=1)
	S += c_t3_a1_1_mem1 >= 4
	c_t3_a1_1_mem1 += MAS_MEM[1]

	c_t3_t3_t3_in = S.Task('c_t3_t3_t3_in', length=1, delay_cost=1)
	S += c_t3_t3_t3_in >= 4
	c_t3_t3_t3_in += MAS_in[0]

	c_t3_t3_t3_mem0 = S.Task('c_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem0 >= 4
	c_t3_t3_t3_mem0 += MAS_MEM[0]

	c_t3_t3_t3_mem1 = S.Task('c_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem1 >= 4
	c_t3_t3_t3_mem1 += MAS_MEM[9]

	c_t2_a1_1_in = S.Task('c_t2_a1_1_in', length=1, delay_cost=1)
	S += c_t2_a1_1_in >= 5
	c_t2_a1_1_in += MAS_in[3]

	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	S += c_t2_a1_1_mem0 >= 5
	c_t2_a1_1_mem0 += MAIN_MEM_r[0]

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	S += c_t2_a1_1_mem1 >= 5
	c_t2_a1_1_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=2, delay_cost=1)
	S += c_t2_t11 >= 5
	c_t2_t11 += MAS[2]

	c_t3_a1_0_in = S.Task('c_t3_a1_0_in', length=1, delay_cost=1)
	S += c_t3_a1_0_in >= 5
	c_t3_a1_0_in += MAS_in[0]

	c_t3_a1_0_mem0 = S.Task('c_t3_a1_0_mem0', length=1, delay_cost=1)
	S += c_t3_a1_0_mem0 >= 5
	c_t3_a1_0_mem0 += MAS_MEM[0]

	c_t3_a1_0_mem1 = S.Task('c_t3_a1_0_mem1', length=1, delay_cost=1)
	S += c_t3_a1_0_mem1 >= 5
	c_t3_a1_0_mem1 += MAS_MEM[9]

	c_t3_a1_1 = S.Task('c_t3_a1_1', length=2, delay_cost=1)
	S += c_t3_a1_1 >= 5
	c_t3_a1_1 += MAS[3]

	c_t3_t3_t3 = S.Task('c_t3_t3_t3', length=2, delay_cost=1)
	S += c_t3_t3_t3 >= 5
	c_t3_t3_t3 += MAS[0]

	c_t0_t3_t3_in = S.Task('c_t0_t3_t3_in', length=1, delay_cost=1)
	S += c_t0_t3_t3_in >= 6
	c_t0_t3_t3_in += MAS_in[0]

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem0 >= 6
	c_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem1 >= 6
	c_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=2, delay_cost=1)
	S += c_t2_a1_1 >= 6
	c_t2_a1_1 += MAS[3]

	c_t3_a1_0 = S.Task('c_t3_a1_0', length=2, delay_cost=1)
	S += c_t3_a1_0 >= 6
	c_t3_a1_0 += MAS[0]

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=2, delay_cost=1)
	S += c_t0_t3_t3 >= 7
	c_t0_t3_t3 += MAS[0]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 7
	c_t3000_in += MAS_in[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 7
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 7
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 8
	c_t0_t11_in += MAS_in[0]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 8
	c_t0_t11_mem0 += MAIN_MEM_r[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 8
	c_t0_t11_mem1 += MAIN_MEM_r[1]

	c_t3000 = S.Task('c_t3000', length=2, delay_cost=1)
	S += c_t3000 >= 8
	c_t3000 += MAS[3]

	c_t0_t11 = S.Task('c_t0_t11', length=2, delay_cost=1)
	S += c_t0_t11 >= 9
	c_t0_t11 += MAS[0]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 9
	c_t1_t11_in += MAS_in[4]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 9
	c_t1_t11_mem0 += MAIN_MEM_r[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 9
	c_t1_t11_mem1 += MAIN_MEM_r[1]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 9
	c_t3_t10_in += MAS_in[3]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 9
	c_t3_t10_mem0 += MAS_MEM[6]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 9
	c_t3_t10_mem1 += MAS_MEM[1]

	c_t1_a1_1_in = S.Task('c_t1_a1_1_in', length=1, delay_cost=1)
	S += c_t1_a1_1_in >= 10
	c_t1_a1_1_in += MAS_in[2]

	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	S += c_t1_a1_1_mem0 >= 10
	c_t1_a1_1_mem0 += MAIN_MEM_r[0]

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	S += c_t1_a1_1_mem1 >= 10
	c_t1_a1_1_mem1 += MAIN_MEM_r[1]

	c_t1_t11 = S.Task('c_t1_t11', length=2, delay_cost=1)
	S += c_t1_t11 >= 10
	c_t1_t11 += MAS[4]

	c_t3_t10 = S.Task('c_t3_t10', length=2, delay_cost=1)
	S += c_t3_t10 >= 10
	c_t3_t10 += MAS[3]

	c_t3_t3_t0_in = S.Task('c_t3_t3_t0_in', length=1, delay_cost=1)
	S += c_t3_t3_t0_in >= 10
	c_t3_t3_t0_in += MM_in[0]

	c_t3_t3_t0_mem0 = S.Task('c_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem0 >= 10
	c_t3_t3_t0_mem0 += MAS_MEM[6]

	c_t3_t3_t0_mem1 = S.Task('c_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem1 >= 10
	c_t3_t3_t0_mem1 += MAS_MEM[1]

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=2, delay_cost=1)
	S += c_t1_a1_1 >= 11
	c_t1_a1_1 += MAS[2]

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	S += c_t2_t3_t0_in >= 11
	c_t2_t3_t0_in += MM_in[0]

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem0 >= 11
	c_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem1 >= 11
	c_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	S += c_t3_t00_in >= 11
	c_t3_t00_in += MAS_in[0]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 11
	c_t3_t00_mem0 += MAS_MEM[6]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 11
	c_t3_t00_mem1 += MAS_MEM[1]

	c_t3_t3_t0 = S.Task('c_t3_t3_t0', length=6, delay_cost=1)
	S += c_t3_t3_t0 >= 11
	c_t3_t3_t0 += MM[0]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 12
	c_t2_t10_in += MAS_in[1]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 12
	c_t2_t10_mem0 += MAIN_MEM_r[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 12
	c_t2_t10_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=6, delay_cost=1)
	S += c_t2_t3_t0 >= 12
	c_t2_t3_t0 += MM[0]

	c_t3_t00 = S.Task('c_t3_t00', length=2, delay_cost=1)
	S += c_t3_t00 >= 12
	c_t3_t00 += MAS[0]

	c_t1_t3_t3_in = S.Task('c_t1_t3_t3_in', length=1, delay_cost=1)
	S += c_t1_t3_t3_in >= 13
	c_t1_t3_t3_in += MAS_in[0]

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem0 >= 13
	c_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem1 >= 13
	c_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=2, delay_cost=1)
	S += c_t2_t10 >= 13
	c_t2_t10 += MAS[1]

	c_t3_t2_t0_in = S.Task('c_t3_t2_t0_in', length=1, delay_cost=1)
	S += c_t3_t2_t0_in >= 13
	c_t3_t2_t0_in += MM_in[0]

	c_t3_t2_t0_mem0 = S.Task('c_t3_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t0_mem0 >= 13
	c_t3_t2_t0_mem0 += MAS_MEM[0]

	c_t3_t2_t0_mem1 = S.Task('c_t3_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t0_mem1 >= 13
	c_t3_t2_t0_mem1 += MAS_MEM[7]

	c_t0_t3_t2_in = S.Task('c_t0_t3_t2_in', length=1, delay_cost=1)
	S += c_t0_t3_t2_in >= 14
	c_t0_t3_t2_in += MAS_in[2]

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem0 >= 14
	c_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem1 >= 14
	c_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=2, delay_cost=1)
	S += c_t1_t3_t3 >= 14
	c_t1_t3_t3 += MAS[0]

	c_t2_t2_t3_in = S.Task('c_t2_t2_t3_in', length=1, delay_cost=1)
	S += c_t2_t2_t3_in >= 14
	c_t2_t2_t3_in += MAS_in[4]

	c_t2_t2_t3_mem0 = S.Task('c_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem0 >= 14
	c_t2_t2_t3_mem0 += MAS_MEM[2]

	c_t2_t2_t3_mem1 = S.Task('c_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem1 >= 14
	c_t2_t2_t3_mem1 += MAS_MEM[5]

	c_t3_t2_t0 = S.Task('c_t3_t2_t0', length=6, delay_cost=1)
	S += c_t3_t2_t0 >= 14
	c_t3_t2_t0 += MM[0]

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=2, delay_cost=1)
	S += c_t0_t3_t2 >= 15
	c_t0_t3_t2 += MAS[2]

	c_t1_t3_t4_in = S.Task('c_t1_t3_t4_in', length=1, delay_cost=1)
	S += c_t1_t3_t4_in >= 15
	c_t1_t3_t4_in += MM_in[0]

	c_t1_t3_t4_mem0 = S.Task('c_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem0 >= 15
	c_t1_t3_t4_mem0 += MAS_MEM[0]

	c_t1_t3_t4_mem1 = S.Task('c_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem1 >= 15
	c_t1_t3_t4_mem1 += MAS_MEM[1]

	c_t2_t2_t3 = S.Task('c_t2_t2_t3', length=2, delay_cost=1)
	S += c_t2_t2_t3 >= 15
	c_t2_t2_t3 += MAS[4]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 15
	c_t3001_in += MAS_in[0]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 15
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 15
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t4_in = S.Task('c_t0_t3_t4_in', length=1, delay_cost=1)
	S += c_t0_t3_t4_in >= 16
	c_t0_t3_t4_in += MM_in[0]

	c_t0_t3_t4_mem0 = S.Task('c_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem0 >= 16
	c_t0_t3_t4_mem0 += MAS_MEM[4]

	c_t0_t3_t4_mem1 = S.Task('c_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem1 >= 16
	c_t0_t3_t4_mem1 += MAS_MEM[1]

	c_t1_t3_t4 = S.Task('c_t1_t3_t4', length=6, delay_cost=1)
	S += c_t1_t3_t4 >= 16
	c_t1_t3_t4 += MM[0]

	c_t2_t3_t2_in = S.Task('c_t2_t3_t2_in', length=1, delay_cost=1)
	S += c_t2_t3_t2_in >= 16
	c_t2_t3_t2_in += MAS_in[1]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem0 >= 16
	c_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem1 >= 16
	c_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=2, delay_cost=1)
	S += c_t3001 >= 16
	c_t3001 += MAS[0]

	c_t0_t3_t4 = S.Task('c_t0_t3_t4', length=6, delay_cost=1)
	S += c_t0_t3_t4 >= 17
	c_t0_t3_t4 += MM[0]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 17
	c_t1_t10_in += MAS_in[2]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 17
	c_t1_t10_mem0 += MAIN_MEM_r[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 17
	c_t1_t10_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=2, delay_cost=1)
	S += c_t2_t3_t2 >= 17
	c_t2_t3_t2 += MAS[1]

	c_t3_t11_in = S.Task('c_t3_t11_in', length=1, delay_cost=1)
	S += c_t3_t11_in >= 17
	c_t3_t11_in += MAS_in[0]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 17
	c_t3_t11_mem0 += MAS_MEM[0]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 17
	c_t3_t11_mem1 += MAS_MEM[9]

	c_t3_t3_t2_in = S.Task('c_t3_t3_t2_in', length=1, delay_cost=1)
	S += c_t3_t3_t2_in >= 17
	c_t3_t3_t2_in += MAS_in[1]

	c_t3_t3_t2_mem0 = S.Task('c_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem0 >= 17
	c_t3_t3_t2_mem0 += MAS_MEM[6]

	c_t3_t3_t2_mem1 = S.Task('c_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem1 >= 17
	c_t3_t3_t2_mem1 += MAS_MEM[1]

	c_t1_t10 = S.Task('c_t1_t10', length=2, delay_cost=1)
	S += c_t1_t10 >= 18
	c_t1_t10 += MAS[2]

	c_t2_a1_0_in = S.Task('c_t2_a1_0_in', length=1, delay_cost=1)
	S += c_t2_a1_0_in >= 18
	c_t2_a1_0_in += MAS_in[2]

	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	S += c_t2_a1_0_mem0 >= 18
	c_t2_a1_0_mem0 += MAIN_MEM_r[0]

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	S += c_t2_a1_0_mem1 >= 18
	c_t2_a1_0_mem1 += MAIN_MEM_r[1]

	c_t3_t11 = S.Task('c_t3_t11', length=2, delay_cost=1)
	S += c_t3_t11 >= 18
	c_t3_t11 += MAS[0]

	c_t3_t3_t1_in = S.Task('c_t3_t3_t1_in', length=1, delay_cost=1)
	S += c_t3_t3_t1_in >= 18
	c_t3_t3_t1_in += MM_in[0]

	c_t3_t3_t1_mem0 = S.Task('c_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem0 >= 18
	c_t3_t3_t1_mem0 += MAS_MEM[0]

	c_t3_t3_t1_mem1 = S.Task('c_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem1 >= 18
	c_t3_t3_t1_mem1 += MAS_MEM[9]

	c_t3_t3_t2 = S.Task('c_t3_t3_t2', length=2, delay_cost=1)
	S += c_t3_t3_t2 >= 18
	c_t3_t3_t2 += MAS[1]

	c_t0_a1_0_in = S.Task('c_t0_a1_0_in', length=1, delay_cost=1)
	S += c_t0_a1_0_in >= 19
	c_t0_a1_0_in += MAS_in[0]

	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	S += c_t0_a1_0_mem0 >= 19
	c_t0_a1_0_mem0 += MAIN_MEM_r[0]

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	S += c_t0_a1_0_mem1 >= 19
	c_t0_a1_0_mem1 += MAIN_MEM_r[1]

	c_t1_t2_t3_in = S.Task('c_t1_t2_t3_in', length=1, delay_cost=1)
	S += c_t1_t2_t3_in >= 19
	c_t1_t2_t3_in += MAS_in[3]

	c_t1_t2_t3_mem0 = S.Task('c_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem0 >= 19
	c_t1_t2_t3_mem0 += MAS_MEM[4]

	c_t1_t2_t3_mem1 = S.Task('c_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem1 >= 19
	c_t1_t2_t3_mem1 += MAS_MEM[9]

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=2, delay_cost=1)
	S += c_t2_a1_0 >= 19
	c_t2_a1_0 += MAS[2]

	c_t3_t01_in = S.Task('c_t3_t01_in', length=1, delay_cost=1)
	S += c_t3_t01_in >= 19
	c_t3_t01_in += MAS_in[1]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 19
	c_t3_t01_mem0 += MAS_MEM[0]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 19
	c_t3_t01_mem1 += MAS_MEM[7]

	c_t3_t3_t1 = S.Task('c_t3_t3_t1', length=6, delay_cost=1)
	S += c_t3_t3_t1 >= 19
	c_t3_t3_t1 += MM[0]

	c_t3_t3_t4_in = S.Task('c_t3_t3_t4_in', length=1, delay_cost=1)
	S += c_t3_t3_t4_in >= 19
	c_t3_t3_t4_in += MM_in[0]

	c_t3_t3_t4_mem0 = S.Task('c_t3_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t4_mem0 >= 19
	c_t3_t3_t4_mem0 += MAS_MEM[2]

	c_t3_t3_t4_mem1 = S.Task('c_t3_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t4_mem1 >= 19
	c_t3_t3_t4_mem1 += MAS_MEM[1]

	c_t0_a1_0 = S.Task('c_t0_a1_0', length=2, delay_cost=1)
	S += c_t0_a1_0 >= 20
	c_t0_a1_0 += MAS[0]

	c_t1_t2_t3 = S.Task('c_t1_t2_t3', length=2, delay_cost=1)
	S += c_t1_t2_t3 >= 20
	c_t1_t2_t3 += MAS[3]

	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	S += c_t2_t3_t1_in >= 20
	c_t2_t3_t1_in += MM_in[0]

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem0 >= 20
	c_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem1 >= 20
	c_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t3_t01 = S.Task('c_t3_t01', length=2, delay_cost=1)
	S += c_t3_t01 >= 20
	c_t3_t01 += MAS[1]

	c_t3_t2_t3_in = S.Task('c_t3_t2_t3_in', length=1, delay_cost=1)
	S += c_t3_t2_t3_in >= 20
	c_t3_t2_t3_in += MAS_in[3]

	c_t3_t2_t3_mem0 = S.Task('c_t3_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t3_mem0 >= 20
	c_t3_t2_t3_mem0 += MAS_MEM[6]

	c_t3_t2_t3_mem1 = S.Task('c_t3_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t3_mem1 >= 20
	c_t3_t2_t3_mem1 += MAS_MEM[1]

	c_t3_t3_t4 = S.Task('c_t3_t3_t4', length=6, delay_cost=1)
	S += c_t3_t3_t4 >= 20
	c_t3_t3_t4 += MM[0]

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	S += c_t1_t3_t1_in >= 21
	c_t1_t3_t1_in += MM_in[0]

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem0 >= 21
	c_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem1 >= 21
	c_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=6, delay_cost=1)
	S += c_t2_t3_t1 >= 21
	c_t2_t3_t1 += MM[0]

	c_t3_t2_t2_in = S.Task('c_t3_t2_t2_in', length=1, delay_cost=1)
	S += c_t3_t2_t2_in >= 21
	c_t3_t2_t2_in += MAS_in[1]

	c_t3_t2_t2_mem0 = S.Task('c_t3_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t2_mem0 >= 21
	c_t3_t2_t2_mem0 += MAS_MEM[0]

	c_t3_t2_t2_mem1 = S.Task('c_t3_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t2_mem1 >= 21
	c_t3_t2_t2_mem1 += MAS_MEM[3]

	c_t3_t2_t3 = S.Task('c_t3_t2_t3', length=2, delay_cost=1)
	S += c_t3_t2_t3 >= 21
	c_t3_t2_t3 += MAS[3]

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=6, delay_cost=1)
	S += c_t1_t3_t1 >= 22
	c_t1_t3_t1 += MM[0]

	c_t3_t2_t1_in = S.Task('c_t3_t2_t1_in', length=1, delay_cost=1)
	S += c_t3_t2_t1_in >= 22
	c_t3_t2_t1_in += MM_in[0]

	c_t3_t2_t1_mem0 = S.Task('c_t3_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t1_mem0 >= 22
	c_t3_t2_t1_mem0 += MAS_MEM[2]

	c_t3_t2_t1_mem1 = S.Task('c_t3_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t1_mem1 >= 22
	c_t3_t2_t1_mem1 += MAS_MEM[1]

	c_t3_t2_t2 = S.Task('c_t3_t2_t2', length=2, delay_cost=1)
	S += c_t3_t2_t2 >= 22
	c_t3_t2_t2 += MAS[1]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 22
	c_t4000_in += MAS_in[3]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 22
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 22
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t3_in = S.Task('c_t2_t3_t3_in', length=1, delay_cost=1)
	S += c_t2_t3_t3_in >= 23
	c_t2_t3_t3_in += MAS_in[1]

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem0 >= 23
	c_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem1 >= 23
	c_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t3_t2_t1 = S.Task('c_t3_t2_t1', length=6, delay_cost=1)
	S += c_t3_t2_t1 >= 23
	c_t3_t2_t1 += MM[0]

	c_t4000 = S.Task('c_t4000', length=2, delay_cost=1)
	S += c_t4000 >= 23
	c_t4000 += MAS[3]

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=2, delay_cost=1)
	S += c_t2_t3_t3 >= 24
	c_t2_t3_t3 += MAS[1]

	c_t3_t3_t5_in = S.Task('c_t3_t3_t5_in', length=1, delay_cost=1)
	S += c_t3_t3_t5_in >= 24
	c_t3_t3_t5_in += MAS_in[1]

	c_t3_t3_t5_mem0 = S.Task('c_t3_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t5_mem0 >= 24
	c_t3_t3_t5_mem0 += MM_MEM[0]

	c_t3_t3_t5_mem1 = S.Task('c_t3_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t5_mem1 >= 24
	c_t3_t3_t5_mem1 += MM_MEM[1]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 24
	c_t4001_in += MAS_in[0]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 24
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 24
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	S += c_t1_t3_t0_in >= 25
	c_t1_t3_t0_in += MM_in[0]

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem0 >= 25
	c_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem1 >= 25
	c_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 25
	c_t3_t30_in += MAS_in[1]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 25
	c_t3_t30_mem0 += MM_MEM[0]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 25
	c_t3_t30_mem1 += MM_MEM[1]

	c_t3_t3_t5 = S.Task('c_t3_t3_t5', length=2, delay_cost=1)
	S += c_t3_t3_t5 >= 25
	c_t3_t3_t5 += MAS[1]

	c_t4001 = S.Task('c_t4001', length=2, delay_cost=1)
	S += c_t4001 >= 25
	c_t4001 += MAS[0]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 26
	c_t0_t10_in += MAS_in[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 26
	c_t0_t10_mem0 += MAIN_MEM_r[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 26
	c_t0_t10_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=6, delay_cost=1)
	S += c_t1_t3_t0 >= 26
	c_t1_t3_t0 += MM[0]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 26
	c_t2_t30_in += MAS_in[4]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 26
	c_t2_t30_mem0 += MM_MEM[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 26
	c_t2_t30_mem1 += MM_MEM[1]

	c_t2_t3_t4_in = S.Task('c_t2_t3_t4_in', length=1, delay_cost=1)
	S += c_t2_t3_t4_in >= 26
	c_t2_t3_t4_in += MM_in[0]

	c_t2_t3_t4_mem0 = S.Task('c_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem0 >= 26
	c_t2_t3_t4_mem0 += MAS_MEM[2]

	c_t2_t3_t4_mem1 = S.Task('c_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem1 >= 26
	c_t2_t3_t4_mem1 += MAS_MEM[3]

	c_t3_t30 = S.Task('c_t3_t30', length=2, delay_cost=1)
	S += c_t3_t30 >= 26
	c_t3_t30 += MAS[1]

	c_t4_t3_t2_in = S.Task('c_t4_t3_t2_in', length=1, delay_cost=1)
	S += c_t4_t3_t2_in >= 26
	c_t4_t3_t2_in += MAS_in[3]

	c_t4_t3_t2_mem0 = S.Task('c_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem0 >= 26
	c_t4_t3_t2_mem0 += MAS_MEM[6]

	c_t4_t3_t2_mem1 = S.Task('c_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem1 >= 26
	c_t4_t3_t2_mem1 += MAS_MEM[1]

	c_t0_t10 = S.Task('c_t0_t10', length=2, delay_cost=1)
	S += c_t0_t10 >= 27
	c_t0_t10 += MAS[1]

	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	S += c_t0_t3_t1_in >= 27
	c_t0_t3_t1_in += MM_in[0]

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem0 >= 27
	c_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem1 >= 27
	c_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t30 = S.Task('c_t2_t30', length=2, delay_cost=1)
	S += c_t2_t30 >= 27
	c_t2_t30 += MAS[4]

	c_t2_t3_t4 = S.Task('c_t2_t3_t4', length=6, delay_cost=1)
	S += c_t2_t3_t4 >= 27
	c_t2_t3_t4 += MM[0]

	c_t2_t3_t5_in = S.Task('c_t2_t3_t5_in', length=1, delay_cost=1)
	S += c_t2_t3_t5_in >= 27
	c_t2_t3_t5_in += MAS_in[4]

	c_t2_t3_t5_mem0 = S.Task('c_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem0 >= 27
	c_t2_t3_t5_mem0 += MM_MEM[0]

	c_t2_t3_t5_mem1 = S.Task('c_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem1 >= 27
	c_t2_t3_t5_mem1 += MM_MEM[1]

	c_t310_in = S.Task('c_t310_in', length=1, delay_cost=1)
	S += c_t310_in >= 27
	c_t310_in += MAS_in[3]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 27
	c_t310_mem0 += MAS_MEM[2]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 27
	c_t310_mem1 += MAS_MEM[3]

	c_t4_t3_t2 = S.Task('c_t4_t3_t2', length=2, delay_cost=1)
	S += c_t4_t3_t2 >= 27
	c_t4_t3_t2 += MAS[3]

	c_t0_a1_1_in = S.Task('c_t0_a1_1_in', length=1, delay_cost=1)
	S += c_t0_a1_1_in >= 28
	c_t0_a1_1_in += MAS_in[0]

	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	S += c_t0_a1_1_mem0 >= 28
	c_t0_a1_1_mem0 += MAIN_MEM_r[0]

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	S += c_t0_a1_1_mem1 >= 28
	c_t0_a1_1_mem1 += MAIN_MEM_r[1]

	c_t0_t2_t3_in = S.Task('c_t0_t2_t3_in', length=1, delay_cost=1)
	S += c_t0_t2_t3_in >= 28
	c_t0_t2_t3_in += MAS_in[3]

	c_t0_t2_t3_mem0 = S.Task('c_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem0 >= 28
	c_t0_t2_t3_mem0 += MAS_MEM[2]

	c_t0_t2_t3_mem1 = S.Task('c_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem1 >= 28
	c_t0_t2_t3_mem1 += MAS_MEM[1]

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=6, delay_cost=1)
	S += c_t0_t3_t1 >= 28
	c_t0_t3_t1 += MM[0]

	c_t210_in = S.Task('c_t210_in', length=1, delay_cost=1)
	S += c_t210_in >= 28
	c_t210_in += MAS_in[1]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 28
	c_t210_mem0 += MAS_MEM[8]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 28
	c_t210_mem1 += MAS_MEM[9]

	c_t2_t3_t5 = S.Task('c_t2_t3_t5', length=2, delay_cost=1)
	S += c_t2_t3_t5 >= 28
	c_t2_t3_t5 += MAS[4]

	c_t310 = S.Task('c_t310', length=2, delay_cost=1)
	S += c_t310 >= 28
	c_t310 += MAS[3]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 28
	c_t3_t31_in += MAS_in[4]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 28
	c_t3_t31_mem0 += MM_MEM[0]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 28
	c_t3_t31_mem1 += MAS_MEM[3]

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=2, delay_cost=1)
	S += c_t0_a1_1 >= 29
	c_t0_a1_1 += MAS[0]

	c_t0_t2_t3 = S.Task('c_t0_t2_t3', length=2, delay_cost=1)
	S += c_t0_t2_t3 >= 29
	c_t0_t2_t3 += MAS[3]

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	S += c_t0_t3_t0_in >= 29
	c_t0_t3_t0_in += MM_in[0]

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem0 >= 29
	c_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem1 >= 29
	c_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t210 = S.Task('c_t210', length=2, delay_cost=1)
	S += c_t210 >= 29
	c_t210 += MAS[1]

	c_t3_t31 = S.Task('c_t3_t31', length=2, delay_cost=1)
	S += c_t3_t31 >= 29
	c_t3_t31 += MAS[4]

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=6, delay_cost=1)
	S += c_t0_t3_t0 >= 30
	c_t0_t3_t0 += MM[0]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 30
	c_t4011_in += MAS_in[4]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 30
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 30
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t5_in = S.Task('c_t1_t3_t5_in', length=1, delay_cost=1)
	S += c_t1_t3_t5_in >= 31
	c_t1_t3_t5_in += MAS_in[3]

	c_t1_t3_t5_mem0 = S.Task('c_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem0 >= 31
	c_t1_t3_t5_mem0 += MM_MEM[0]

	c_t1_t3_t5_mem1 = S.Task('c_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem1 >= 31
	c_t1_t3_t5_mem1 += MM_MEM[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 31
	c_t4010_in += MAS_in[0]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 31
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 31
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4011 = S.Task('c_t4011', length=2, delay_cost=1)
	S += c_t4011 >= 31
	c_t4011 += MAS[4]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 32
	c_t1_t30_in += MAS_in[2]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 32
	c_t1_t30_mem0 += MM_MEM[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 32
	c_t1_t30_mem1 += MM_MEM[1]

	c_t1_t3_t5 = S.Task('c_t1_t3_t5', length=2, delay_cost=1)
	S += c_t1_t3_t5 >= 32
	c_t1_t3_t5 += MAS[3]

	c_t4010 = S.Task('c_t4010', length=2, delay_cost=1)
	S += c_t4010 >= 32
	c_t4010 += MAS[0]

	c_t4_t11_in = S.Task('c_t4_t11_in', length=1, delay_cost=1)
	S += c_t4_t11_in >= 32
	c_t4_t11_in += MAS_in[4]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 32
	c_t4_t11_mem0 += MAS_MEM[0]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 32
	c_t4_t11_mem1 += MAS_MEM[9]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 32
	c_t5011_in += MAS_in[1]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 32
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 32
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=2, delay_cost=1)
	S += c_t1_t30 >= 33
	c_t1_t30 += MAS[2]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 33
	c_t1_t31_in += MAS_in[0]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 33
	c_t1_t31_mem0 += MM_MEM[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 33
	c_t1_t31_mem1 += MAS_MEM[7]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 33
	c_t4_t10_in += MAS_in[4]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 33
	c_t4_t10_mem0 += MAS_MEM[6]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 33
	c_t4_t10_mem1 += MAS_MEM[1]

	c_t4_t11 = S.Task('c_t4_t11', length=2, delay_cost=1)
	S += c_t4_t11 >= 33
	c_t4_t11 += MAS[4]

	c_t4_t3_t1_in = S.Task('c_t4_t3_t1_in', length=1, delay_cost=1)
	S += c_t4_t3_t1_in >= 33
	c_t4_t3_t1_in += MM_in[0]

	c_t4_t3_t1_mem0 = S.Task('c_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem0 >= 33
	c_t4_t3_t1_mem0 += MAS_MEM[0]

	c_t4_t3_t1_mem1 = S.Task('c_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem1 >= 33
	c_t4_t3_t1_mem1 += MAS_MEM[9]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 33
	c_t5010_in += MAS_in[2]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 33
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 33
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=2, delay_cost=1)
	S += c_t5011 >= 33
	c_t5011 += MAS[1]

	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	S += c_t110_in >= 34
	c_t110_in += MAS_in[3]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 34
	c_t110_mem0 += MAS_MEM[4]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 34
	c_t110_mem1 += MAS_MEM[5]

	c_t1_t31 = S.Task('c_t1_t31', length=2, delay_cost=1)
	S += c_t1_t31 >= 34
	c_t1_t31 += MAS[0]

	c_t4_a1_1_in = S.Task('c_t4_a1_1_in', length=1, delay_cost=1)
	S += c_t4_a1_1_in >= 34
	c_t4_a1_1_in += MAS_in[2]

	c_t4_a1_1_mem0 = S.Task('c_t4_a1_1_mem0', length=1, delay_cost=1)
	S += c_t4_a1_1_mem0 >= 34
	c_t4_a1_1_mem0 += MAS_MEM[8]

	c_t4_a1_1_mem1 = S.Task('c_t4_a1_1_mem1', length=1, delay_cost=1)
	S += c_t4_a1_1_mem1 >= 34
	c_t4_a1_1_mem1 += MAS_MEM[1]

	c_t4_t10 = S.Task('c_t4_t10', length=2, delay_cost=1)
	S += c_t4_t10 >= 34
	c_t4_t10 += MAS[4]

	c_t4_t3_t1 = S.Task('c_t4_t3_t1', length=6, delay_cost=1)
	S += c_t4_t3_t1 >= 34
	c_t4_t3_t1 += MM[0]

	c_t4_t3_t3_in = S.Task('c_t4_t3_t3_in', length=1, delay_cost=1)
	S += c_t4_t3_t3_in >= 34
	c_t4_t3_t3_in += MAS_in[4]

	c_t4_t3_t3_mem0 = S.Task('c_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem0 >= 34
	c_t4_t3_t3_mem0 += MAS_MEM[0]

	c_t4_t3_t3_mem1 = S.Task('c_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem1 >= 34
	c_t4_t3_t3_mem1 += MAS_MEM[9]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 34
	c_t5000_in += MAS_in[0]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 34
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 34
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5010 = S.Task('c_t5010', length=2, delay_cost=1)
	S += c_t5010 >= 34
	c_t5010 += MAS[2]

	c_t0_t3_t5_in = S.Task('c_t0_t3_t5_in', length=1, delay_cost=1)
	S += c_t0_t3_t5_in >= 35
	c_t0_t3_t5_in += MAS_in[1]

	c_t0_t3_t5_mem0 = S.Task('c_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem0 >= 35
	c_t0_t3_t5_mem0 += MM_MEM[0]

	c_t0_t3_t5_mem1 = S.Task('c_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem1 >= 35
	c_t0_t3_t5_mem1 += MM_MEM[1]

	c_t110 = S.Task('c_t110', length=2, delay_cost=1)
	S += c_t110 >= 35
	c_t110 += MAS[3]

	c_t4_a1_0_in = S.Task('c_t4_a1_0_in', length=1, delay_cost=1)
	S += c_t4_a1_0_in >= 35
	c_t4_a1_0_in += MAS_in[2]

	c_t4_a1_0_mem0 = S.Task('c_t4_a1_0_mem0', length=1, delay_cost=1)
	S += c_t4_a1_0_mem0 >= 35
	c_t4_a1_0_mem0 += MAS_MEM[0]

	c_t4_a1_0_mem1 = S.Task('c_t4_a1_0_mem1', length=1, delay_cost=1)
	S += c_t4_a1_0_mem1 >= 35
	c_t4_a1_0_mem1 += MAS_MEM[9]

	c_t4_a1_1 = S.Task('c_t4_a1_1', length=2, delay_cost=1)
	S += c_t4_a1_1 >= 35
	c_t4_a1_1 += MAS[2]

	c_t4_t3_t0_in = S.Task('c_t4_t3_t0_in', length=1, delay_cost=1)
	S += c_t4_t3_t0_in >= 35
	c_t4_t3_t0_in += MM_in[0]

	c_t4_t3_t0_mem0 = S.Task('c_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem0 >= 35
	c_t4_t3_t0_mem0 += MAS_MEM[6]

	c_t4_t3_t0_mem1 = S.Task('c_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem1 >= 35
	c_t4_t3_t0_mem1 += MAS_MEM[1]

	c_t4_t3_t3 = S.Task('c_t4_t3_t3', length=2, delay_cost=1)
	S += c_t4_t3_t3 >= 35
	c_t4_t3_t3 += MAS[4]

	c_t5000 = S.Task('c_t5000', length=2, delay_cost=1)
	S += c_t5000 >= 35
	c_t5000 += MAS[0]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 35
	c_t5001_in += MAS_in[3]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 35
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 35
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5_a1_0_in = S.Task('c_t5_a1_0_in', length=1, delay_cost=1)
	S += c_t5_a1_0_in >= 35
	c_t5_a1_0_in += MAS_in[0]

	c_t5_a1_0_mem0 = S.Task('c_t5_a1_0_mem0', length=1, delay_cost=1)
	S += c_t5_a1_0_mem0 >= 35
	c_t5_a1_0_mem0 += MAS_MEM[4]

	c_t5_a1_0_mem1 = S.Task('c_t5_a1_0_mem1', length=1, delay_cost=1)
	S += c_t5_a1_0_mem1 >= 35
	c_t5_a1_0_mem1 += MAS_MEM[3]

	c_t5_a1_1_in = S.Task('c_t5_a1_1_in', length=1, delay_cost=1)
	S += c_t5_a1_1_in >= 35
	c_t5_a1_1_in += MAS_in[4]

	c_t5_a1_1_mem0 = S.Task('c_t5_a1_1_mem0', length=1, delay_cost=1)
	S += c_t5_a1_1_mem0 >= 35
	c_t5_a1_1_mem0 += MAS_MEM[2]

	c_t5_a1_1_mem1 = S.Task('c_t5_a1_1_mem1', length=1, delay_cost=1)
	S += c_t5_a1_1_mem1 >= 35
	c_t5_a1_1_mem1 += MAS_MEM[5]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 36
	c_t0_t30_in += MAS_in[1]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 36
	c_t0_t30_mem0 += MM_MEM[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 36
	c_t0_t30_mem1 += MM_MEM[1]

	c_t0_t3_t5 = S.Task('c_t0_t3_t5', length=2, delay_cost=1)
	S += c_t0_t3_t5 >= 36
	c_t0_t3_t5 += MAS[1]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 36
	c_t2_t01_in += MAS_in[0]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 36
	c_t2_t01_mem0 += MAIN_MEM_r[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 36
	c_t2_t01_mem1 += MAS_MEM[7]

	c_t4_a1_0 = S.Task('c_t4_a1_0', length=2, delay_cost=1)
	S += c_t4_a1_0 >= 36
	c_t4_a1_0 += MAS[2]

	c_t4_t2_t3_in = S.Task('c_t4_t2_t3_in', length=1, delay_cost=1)
	S += c_t4_t2_t3_in >= 36
	c_t4_t2_t3_in += MAS_in[2]

	c_t4_t2_t3_mem0 = S.Task('c_t4_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t3_mem0 >= 36
	c_t4_t2_t3_mem0 += MAS_MEM[8]

	c_t4_t2_t3_mem1 = S.Task('c_t4_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t3_mem1 >= 36
	c_t4_t2_t3_mem1 += MAS_MEM[9]

	c_t4_t3_t0 = S.Task('c_t4_t3_t0', length=6, delay_cost=1)
	S += c_t4_t3_t0 >= 36
	c_t4_t3_t0 += MM[0]

	c_t5001 = S.Task('c_t5001', length=2, delay_cost=1)
	S += c_t5001 >= 36
	c_t5001 += MAS[3]

	c_t5_a1_0 = S.Task('c_t5_a1_0', length=2, delay_cost=1)
	S += c_t5_a1_0 >= 36
	c_t5_a1_0 += MAS[0]

	c_t5_a1_1 = S.Task('c_t5_a1_1', length=2, delay_cost=1)
	S += c_t5_a1_1 >= 36
	c_t5_a1_1 += MAS[4]

	c_t5_t3_t0_in = S.Task('c_t5_t3_t0_in', length=1, delay_cost=1)
	S += c_t5_t3_t0_in >= 36
	c_t5_t3_t0_in += MM_in[0]

	c_t5_t3_t0_mem0 = S.Task('c_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem0 >= 36
	c_t5_t3_t0_mem0 += MAS_MEM[0]

	c_t5_t3_t0_mem1 = S.Task('c_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem1 >= 36
	c_t5_t3_t0_mem1 += MAS_MEM[5]

	c_t5_t3_t3_in = S.Task('c_t5_t3_t3_in', length=1, delay_cost=1)
	S += c_t5_t3_t3_in >= 36
	c_t5_t3_t3_in += MAS_in[3]

	c_t5_t3_t3_mem0 = S.Task('c_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem0 >= 36
	c_t5_t3_t3_mem0 += MAS_MEM[4]

	c_t5_t3_t3_mem1 = S.Task('c_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem1 >= 36
	c_t5_t3_t3_mem1 += MAS_MEM[3]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 37
	c_t0_t01_in += MAS_in[0]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 37
	c_t0_t01_mem0 += MAIN_MEM_r[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 37
	c_t0_t01_mem1 += MAS_MEM[1]

	c_t0_t30 = S.Task('c_t0_t30', length=2, delay_cost=1)
	S += c_t0_t30 >= 37
	c_t0_t30 += MAS[1]

	c_t2_t01 = S.Task('c_t2_t01', length=2, delay_cost=1)
	S += c_t2_t01 >= 37
	c_t2_t01 += MAS[0]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 37
	c_t2_t31_in += MAS_in[2]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 37
	c_t2_t31_mem0 += MM_MEM[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 37
	c_t2_t31_mem1 += MAS_MEM[9]

	c_t4_t2_t3 = S.Task('c_t4_t2_t3', length=2, delay_cost=1)
	S += c_t4_t2_t3 >= 37
	c_t4_t2_t3 += MAS[2]

	c_t5_t11_in = S.Task('c_t5_t11_in', length=1, delay_cost=1)
	S += c_t5_t11_in >= 37
	c_t5_t11_in += MAS_in[1]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 37
	c_t5_t11_mem0 += MAS_MEM[6]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 37
	c_t5_t11_mem1 += MAS_MEM[3]

	c_t5_t3_t0 = S.Task('c_t5_t3_t0', length=6, delay_cost=1)
	S += c_t5_t3_t0 >= 37
	c_t5_t3_t0 += MM[0]

	c_t5_t3_t2_in = S.Task('c_t5_t3_t2_in', length=1, delay_cost=1)
	S += c_t5_t3_t2_in >= 37
	c_t5_t3_t2_in += MAS_in[3]

	c_t5_t3_t2_mem0 = S.Task('c_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem0 >= 37
	c_t5_t3_t2_mem0 += MAS_MEM[0]

	c_t5_t3_t2_mem1 = S.Task('c_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem1 >= 37
	c_t5_t3_t2_mem1 += MAS_MEM[7]

	c_t5_t3_t3 = S.Task('c_t5_t3_t3', length=2, delay_cost=1)
	S += c_t5_t3_t3 >= 37
	c_t5_t3_t3 += MAS[3]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 38
	c_t0_t00_in += MAS_in[2]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 38
	c_t0_t00_mem0 += MAIN_MEM_r[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 38
	c_t0_t00_mem1 += MAS_MEM[1]

	c_t0_t01 = S.Task('c_t0_t01', length=2, delay_cost=1)
	S += c_t0_t01 >= 38
	c_t0_t01 += MAS[0]

	c_t2_t31 = S.Task('c_t2_t31', length=2, delay_cost=1)
	S += c_t2_t31 >= 38
	c_t2_t31 += MAS[2]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 38
	c_t5_t10_in += MAS_in[0]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 38
	c_t5_t10_mem0 += MAS_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 38
	c_t5_t10_mem1 += MAS_MEM[5]

	c_t5_t11 = S.Task('c_t5_t11', length=2, delay_cost=1)
	S += c_t5_t11 >= 38
	c_t5_t11 += MAS[1]

	c_t5_t3_t1_in = S.Task('c_t5_t3_t1_in', length=1, delay_cost=1)
	S += c_t5_t3_t1_in >= 38
	c_t5_t3_t1_in += MM_in[0]

	c_t5_t3_t1_mem0 = S.Task('c_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem0 >= 38
	c_t5_t3_t1_mem0 += MAS_MEM[6]

	c_t5_t3_t1_mem1 = S.Task('c_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem1 >= 38
	c_t5_t3_t1_mem1 += MAS_MEM[3]

	c_t5_t3_t2 = S.Task('c_t5_t3_t2', length=2, delay_cost=1)
	S += c_t5_t3_t2 >= 38
	c_t5_t3_t2 += MAS[3]

	c_t0_t00 = S.Task('c_t0_t00', length=2, delay_cost=1)
	S += c_t0_t00 >= 39
	c_t0_t00 += MAS[2]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 39
	c_t0_t31_in += MAS_in[4]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 39
	c_t0_t31_mem0 += MM_MEM[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 39
	c_t0_t31_mem1 += MAS_MEM[3]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 39
	c_t2_t00_in += MAS_in[0]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 39
	c_t2_t00_mem0 += MAIN_MEM_r[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 39
	c_t2_t00_mem1 += MAS_MEM[5]

	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	S += c_t5_t00_in >= 39
	c_t5_t00_in += MAS_in[2]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 39
	c_t5_t00_mem0 += MAS_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 39
	c_t5_t00_mem1 += MAS_MEM[1]

	c_t5_t01_in = S.Task('c_t5_t01_in', length=1, delay_cost=1)
	S += c_t5_t01_in >= 39
	c_t5_t01_in += MAS_in[3]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 39
	c_t5_t01_mem0 += MAS_MEM[6]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 39
	c_t5_t01_mem1 += MAS_MEM[9]

	c_t5_t10 = S.Task('c_t5_t10', length=2, delay_cost=1)
	S += c_t5_t10 >= 39
	c_t5_t10 += MAS[0]

	c_t5_t3_t1 = S.Task('c_t5_t3_t1', length=6, delay_cost=1)
	S += c_t5_t3_t1 >= 39
	c_t5_t3_t1 += MM[0]

	c_t0_t2_t2_in = S.Task('c_t0_t2_t2_in', length=1, delay_cost=1)
	S += c_t0_t2_t2_in >= 40
	c_t0_t2_t2_in += MAS_in[2]

	c_t0_t2_t2_mem0 = S.Task('c_t0_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t2_mem0 >= 40
	c_t0_t2_t2_mem0 += MAS_MEM[4]

	c_t0_t2_t2_mem1 = S.Task('c_t0_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t2_mem1 >= 40
	c_t0_t2_t2_mem1 += MAS_MEM[1]

	c_t0_t31 = S.Task('c_t0_t31', length=2, delay_cost=1)
	S += c_t0_t31 >= 40
	c_t0_t31 += MAS[4]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 40
	c_t1_t01_in += MAS_in[0]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 40
	c_t1_t01_mem0 += MAIN_MEM_r[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 40
	c_t1_t01_mem1 += MAS_MEM[5]

	c_t2_t00 = S.Task('c_t2_t00', length=2, delay_cost=1)
	S += c_t2_t00 >= 40
	c_t2_t00 += MAS[0]

	c_t4_t3_t4_in = S.Task('c_t4_t3_t4_in', length=1, delay_cost=1)
	S += c_t4_t3_t4_in >= 40
	c_t4_t3_t4_in += MM_in[0]

	c_t4_t3_t4_mem0 = S.Task('c_t4_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t4_mem0 >= 40
	c_t4_t3_t4_mem0 += MAS_MEM[6]

	c_t4_t3_t4_mem1 = S.Task('c_t4_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t4_mem1 >= 40
	c_t4_t3_t4_mem1 += MAS_MEM[9]

	c_t5_t00 = S.Task('c_t5_t00', length=2, delay_cost=1)
	S += c_t5_t00 >= 40
	c_t5_t00 += MAS[2]

	c_t5_t01 = S.Task('c_t5_t01', length=2, delay_cost=1)
	S += c_t5_t01 >= 40
	c_t5_t01 += MAS[3]

	c_t5_t2_t3_in = S.Task('c_t5_t2_t3_in', length=1, delay_cost=1)
	S += c_t5_t2_t3_in >= 40
	c_t5_t2_t3_in += MAS_in[4]

	c_t5_t2_t3_mem0 = S.Task('c_t5_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t3_mem0 >= 40
	c_t5_t2_t3_mem0 += MAS_MEM[0]

	c_t5_t2_t3_mem1 = S.Task('c_t5_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t3_mem1 >= 40
	c_t5_t2_t3_mem1 += MAS_MEM[3]

	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	S += c_t010_in >= 41
	c_t010_in += MAS_in[1]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 41
	c_t010_mem0 += MAS_MEM[2]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 41
	c_t010_mem1 += MAS_MEM[3]

	c_t0_t2_t2 = S.Task('c_t0_t2_t2', length=2, delay_cost=1)
	S += c_t0_t2_t2 >= 41
	c_t0_t2_t2 += MAS[2]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 41
	c_t1_t00_in += MAS_in[0]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 41
	c_t1_t00_mem0 += MAIN_MEM_r[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 41
	c_t1_t00_mem1 += MAS_MEM[1]

	c_t1_t01 = S.Task('c_t1_t01', length=2, delay_cost=1)
	S += c_t1_t01 >= 41
	c_t1_t01 += MAS[0]

	c_t2_t41_in = S.Task('c_t2_t41_in', length=1, delay_cost=1)
	S += c_t2_t41_in >= 41
	c_t2_t41_in += MAS_in[2]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 41
	c_t2_t41_mem0 += MAS_MEM[4]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 41
	c_t2_t41_mem1 += MAS_MEM[9]

	c_t4_t01_in = S.Task('c_t4_t01_in', length=1, delay_cost=1)
	S += c_t4_t01_in >= 41
	c_t4_t01_in += MAS_in[3]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 41
	c_t4_t01_mem0 += MAS_MEM[0]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 41
	c_t4_t01_mem1 += MAS_MEM[5]

	c_t4_t3_t4 = S.Task('c_t4_t3_t4', length=6, delay_cost=1)
	S += c_t4_t3_t4 >= 41
	c_t4_t3_t4 += MM[0]

	c_t4_t3_t5_in = S.Task('c_t4_t3_t5_in', length=1, delay_cost=1)
	S += c_t4_t3_t5_in >= 41
	c_t4_t3_t5_in += MAS_in[4]

	c_t4_t3_t5_mem0 = S.Task('c_t4_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t5_mem0 >= 41
	c_t4_t3_t5_mem0 += MM_MEM[0]

	c_t4_t3_t5_mem1 = S.Task('c_t4_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t5_mem1 >= 41
	c_t4_t3_t5_mem1 += MM_MEM[1]

	c_t5_t2_t3 = S.Task('c_t5_t2_t3', length=2, delay_cost=1)
	S += c_t5_t2_t3 >= 41
	c_t5_t2_t3 += MAS[4]

	c_t5_t3_t4_in = S.Task('c_t5_t3_t4_in', length=1, delay_cost=1)
	S += c_t5_t3_t4_in >= 41
	c_t5_t3_t4_in += MM_in[0]

	c_t5_t3_t4_mem0 = S.Task('c_t5_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t4_mem0 >= 41
	c_t5_t3_t4_mem0 += MAS_MEM[6]

	c_t5_t3_t4_mem1 = S.Task('c_t5_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t4_mem1 >= 41
	c_t5_t3_t4_mem1 += MAS_MEM[7]

	c_t010 = S.Task('c_t010', length=2, delay_cost=1)
	S += c_t010 >= 42
	c_t010 += MAS[1]

	c_t0_t2_t0_in = S.Task('c_t0_t2_t0_in', length=1, delay_cost=1)
	S += c_t0_t2_t0_in >= 42
	c_t0_t2_t0_in += MM_in[0]

	c_t0_t2_t0_mem0 = S.Task('c_t0_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t0_mem0 >= 42
	c_t0_t2_t0_mem0 += MAS_MEM[4]

	c_t0_t2_t0_mem1 = S.Task('c_t0_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t0_mem1 >= 42
	c_t0_t2_t0_mem1 += MAS_MEM[3]

	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	S += c_t0_t40_in >= 42
	c_t0_t40_in += MAS_in[1]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 42
	c_t0_t40_mem0 += MAS_MEM[2]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 42
	c_t0_t40_mem1 += MAS_MEM[9]

	c_t1_t00 = S.Task('c_t1_t00', length=2, delay_cost=1)
	S += c_t1_t00 >= 42
	c_t1_t00 += MAS[0]

	c_t2_t2_t2_in = S.Task('c_t2_t2_t2_in', length=1, delay_cost=1)
	S += c_t2_t2_t2_in >= 42
	c_t2_t2_t2_in += MAS_in[4]

	c_t2_t2_t2_mem0 = S.Task('c_t2_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t2_mem0 >= 42
	c_t2_t2_t2_mem0 += MAS_MEM[0]

	c_t2_t2_t2_mem1 = S.Task('c_t2_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t2_mem1 >= 42
	c_t2_t2_t2_mem1 += MAS_MEM[1]

	c_t2_t41 = S.Task('c_t2_t41', length=2, delay_cost=1)
	S += c_t2_t41 >= 42
	c_t2_t41 += MAS[2]

	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	S += c_t4_t00_in >= 42
	c_t4_t00_in += MAS_in[2]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 42
	c_t4_t00_mem0 += MAS_MEM[6]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 42
	c_t4_t00_mem1 += MAS_MEM[5]

	c_t4_t01 = S.Task('c_t4_t01', length=2, delay_cost=1)
	S += c_t4_t01 >= 42
	c_t4_t01 += MAS[3]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 42
	c_t4_t30_in += MAS_in[3]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 42
	c_t4_t30_mem0 += MM_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 42
	c_t4_t30_mem1 += MM_MEM[1]

	c_t4_t3_t5 = S.Task('c_t4_t3_t5', length=2, delay_cost=1)
	S += c_t4_t3_t5 >= 42
	c_t4_t3_t5 += MAS[4]

	c_t5_t3_t4 = S.Task('c_t5_t3_t4', length=6, delay_cost=1)
	S += c_t5_t3_t4 >= 42
	c_t5_t3_t4 += MM[0]

	c_s0010_in = S.Task('c_s0010_in', length=1, delay_cost=1)
	S += c_s0010_in >= 43
	c_s0010_in += MAS_in[0]

	c_s0010_mem0 = S.Task('c_s0010_mem0', length=1, delay_cost=1)
	S += c_s0010_mem0 >= 43
	c_s0010_mem0 += MAS_MEM[2]

	c_s0010_mem1 = S.Task('c_s0010_mem1', length=1, delay_cost=1)
	S += c_s0010_mem1 >= 43
	c_s0010_mem1 += MAS_MEM[7]

	c_s1010_in = S.Task('c_s1010_in', length=1, delay_cost=1)
	S += c_s1010_in >= 43
	c_s1010_in += MAS_in[2]

	c_s1010_mem0 = S.Task('c_s1010_mem0', length=1, delay_cost=1)
	S += c_s1010_mem0 >= 43
	c_s1010_mem0 += MAS_MEM[6]

	c_s1010_mem1 = S.Task('c_s1010_mem1', length=1, delay_cost=1)
	S += c_s1010_mem1 >= 43
	c_s1010_mem1 += MAS_MEM[3]

	c_t011_in = S.Task('c_t011_in', length=1, delay_cost=1)
	S += c_t011_in >= 43
	c_t011_in += MAS_in[3]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 43
	c_t011_mem0 += MAS_MEM[8]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 43
	c_t011_mem1 += MAS_MEM[9]

	c_t0_t2_t0 = S.Task('c_t0_t2_t0', length=6, delay_cost=1)
	S += c_t0_t2_t0 >= 43
	c_t0_t2_t0 += MM[0]

	c_t0_t40 = S.Task('c_t0_t40', length=2, delay_cost=1)
	S += c_t0_t40 >= 43
	c_t0_t40 += MAS[1]

	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	S += c_t1_t40_in >= 43
	c_t1_t40_in += MAS_in[4]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 43
	c_t1_t40_mem0 += MAS_MEM[4]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 43
	c_t1_t40_mem1 += MAS_MEM[1]

	c_t2_t2_t1_in = S.Task('c_t2_t2_t1_in', length=1, delay_cost=1)
	S += c_t2_t2_t1_in >= 43
	c_t2_t2_t1_in += MM_in[0]

	c_t2_t2_t1_mem0 = S.Task('c_t2_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t1_mem0 >= 43
	c_t2_t2_t1_mem0 += MAS_MEM[0]

	c_t2_t2_t1_mem1 = S.Task('c_t2_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t1_mem1 >= 43
	c_t2_t2_t1_mem1 += MAS_MEM[5]

	c_t2_t2_t2 = S.Task('c_t2_t2_t2', length=2, delay_cost=1)
	S += c_t2_t2_t2 >= 43
	c_t2_t2_t2 += MAS[4]

	c_t4_t00 = S.Task('c_t4_t00', length=2, delay_cost=1)
	S += c_t4_t00 >= 43
	c_t4_t00 += MAS[2]

	c_t4_t30 = S.Task('c_t4_t30', length=2, delay_cost=1)
	S += c_t4_t30 >= 43
	c_t4_t30 += MAS[3]

	c_s0010 = S.Task('c_s0010', length=2, delay_cost=1)
	S += c_s0010 >= 44
	c_s0010 += MAS[0]

	c_s1010 = S.Task('c_s1010', length=2, delay_cost=1)
	S += c_s1010 >= 44
	c_s1010 += MAS[2]

	c_t011 = S.Task('c_t011', length=2, delay_cost=1)
	S += c_t011 >= 44
	c_t011 += MAS[3]

	c_t0_t2_t1_in = S.Task('c_t0_t2_t1_in', length=1, delay_cost=1)
	S += c_t0_t2_t1_in >= 44
	c_t0_t2_t1_in += MM_in[0]

	c_t0_t2_t1_mem0 = S.Task('c_t0_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t1_mem0 >= 44
	c_t0_t2_t1_mem0 += MAS_MEM[0]

	c_t0_t2_t1_mem1 = S.Task('c_t0_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t1_mem1 >= 44
	c_t0_t2_t1_mem1 += MAS_MEM[1]

	c_t0_t41_in = S.Task('c_t0_t41_in', length=1, delay_cost=1)
	S += c_t0_t41_in >= 44
	c_t0_t41_in += MAS_in[3]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 44
	c_t0_t41_mem0 += MAS_MEM[8]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 44
	c_t0_t41_mem1 += MAS_MEM[3]

	c_t1_t40 = S.Task('c_t1_t40', length=2, delay_cost=1)
	S += c_t1_t40 >= 44
	c_t1_t40 += MAS[4]

	c_t211_in = S.Task('c_t211_in', length=1, delay_cost=1)
	S += c_t211_in >= 44
	c_t211_in += MAS_in[0]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 44
	c_t211_mem0 += MAS_MEM[4]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 44
	c_t211_mem1 += MAS_MEM[5]

	c_t2_t2_t1 = S.Task('c_t2_t2_t1', length=6, delay_cost=1)
	S += c_t2_t2_t1 >= 44
	c_t2_t2_t1 += MM[0]

	c_t410_in = S.Task('c_t410_in', length=1, delay_cost=1)
	S += c_t410_in >= 44
	c_t410_in += MAS_in[1]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	S += c_t410_mem0 >= 44
	c_t410_mem0 += MAS_MEM[6]

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	S += c_t410_mem1 >= 44
	c_t410_mem1 += MAS_MEM[7]

	c_t5_t3_t5_in = S.Task('c_t5_t3_t5_in', length=1, delay_cost=1)
	S += c_t5_t3_t5_in >= 44
	c_t5_t3_t5_in += MAS_in[4]

	c_t5_t3_t5_mem0 = S.Task('c_t5_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t5_mem0 >= 44
	c_t5_t3_t5_mem0 += MM_MEM[0]

	c_t5_t3_t5_mem1 = S.Task('c_t5_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t5_mem1 >= 44
	c_t5_t3_t5_mem1 += MM_MEM[1]

	c_s2010_in = S.Task('c_s2010_in', length=1, delay_cost=1)
	S += c_s2010_in >= 45
	c_s2010_in += MAS_in[2]

	c_s2010_mem0 = S.Task('c_s2010_mem0', length=1, delay_cost=1)
	S += c_s2010_mem0 >= 45
	c_s2010_mem0 += MAS_MEM[2]

	c_s2010_mem1 = S.Task('c_s2010_mem1', length=1, delay_cost=1)
	S += c_s2010_mem1 >= 45
	c_s2010_mem1 += MAS_MEM[3]

	c_t0_t2_t1 = S.Task('c_t0_t2_t1', length=6, delay_cost=1)
	S += c_t0_t2_t1 >= 45
	c_t0_t2_t1 += MM[0]

	c_t0_t41 = S.Task('c_t0_t41', length=2, delay_cost=1)
	S += c_t0_t41 >= 45
	c_t0_t41 += MAS[3]

	c_t1_t2_t0_in = S.Task('c_t1_t2_t0_in', length=1, delay_cost=1)
	S += c_t1_t2_t0_in >= 45
	c_t1_t2_t0_in += MM_in[0]

	c_t1_t2_t0_mem0 = S.Task('c_t1_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t0_mem0 >= 45
	c_t1_t2_t0_mem0 += MAS_MEM[0]

	c_t1_t2_t0_mem1 = S.Task('c_t1_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t0_mem1 >= 45
	c_t1_t2_t0_mem1 += MAS_MEM[5]

	c_t211 = S.Task('c_t211', length=2, delay_cost=1)
	S += c_t211 >= 45
	c_t211 += MAS[0]

	c_t410 = S.Task('c_t410', length=2, delay_cost=1)
	S += c_t410 >= 45
	c_t410 += MAS[1]

	c_t5_t2_t2_in = S.Task('c_t5_t2_t2_in', length=1, delay_cost=1)
	S += c_t5_t2_t2_in >= 45
	c_t5_t2_t2_in += MAS_in[3]

	c_t5_t2_t2_mem0 = S.Task('c_t5_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t2_mem0 >= 45
	c_t5_t2_t2_mem0 += MAS_MEM[4]

	c_t5_t2_t2_mem1 = S.Task('c_t5_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t2_mem1 >= 45
	c_t5_t2_t2_mem1 += MAS_MEM[7]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 45
	c_t5_t30_in += MAS_in[4]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 45
	c_t5_t30_mem0 += MM_MEM[0]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 45
	c_t5_t30_mem1 += MM_MEM[1]

	c_t5_t3_t5 = S.Task('c_t5_t3_t5', length=2, delay_cost=1)
	S += c_t5_t3_t5 >= 45
	c_t5_t3_t5 += MAS[4]

	c_s2010 = S.Task('c_s2010', length=2, delay_cost=1)
	S += c_s2010 >= 46
	c_s2010 += MAS[2]

	c_t1_t2_t0 = S.Task('c_t1_t2_t0', length=6, delay_cost=1)
	S += c_t1_t2_t0 >= 46
	c_t1_t2_t0 += MM[0]

	c_t1_t2_t1_in = S.Task('c_t1_t2_t1_in', length=1, delay_cost=1)
	S += c_t1_t2_t1_in >= 46
	c_t1_t2_t1_in += MM_in[0]

	c_t1_t2_t1_mem0 = S.Task('c_t1_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t1_mem0 >= 46
	c_t1_t2_t1_mem0 += MAS_MEM[0]

	c_t1_t2_t1_mem1 = S.Task('c_t1_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t1_mem1 >= 46
	c_t1_t2_t1_mem1 += MAS_MEM[9]

	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	S += c_t2_t40_in >= 46
	c_t2_t40_in += MAS_in[0]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 46
	c_t2_t40_mem0 += MAS_MEM[8]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 46
	c_t2_t40_mem1 += MAS_MEM[5]

	c_t4_t2_t2_in = S.Task('c_t4_t2_t2_in', length=1, delay_cost=1)
	S += c_t4_t2_t2_in >= 46
	c_t4_t2_t2_in += MAS_in[3]

	c_t4_t2_t2_mem0 = S.Task('c_t4_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t2_mem0 >= 46
	c_t4_t2_t2_mem0 += MAS_MEM[4]

	c_t4_t2_t2_mem1 = S.Task('c_t4_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t2_mem1 >= 46
	c_t4_t2_t2_mem1 += MAS_MEM[7]

	c_t5_t2_t2 = S.Task('c_t5_t2_t2', length=2, delay_cost=1)
	S += c_t5_t2_t2 >= 46
	c_t5_t2_t2 += MAS[3]

	c_t5_t30 = S.Task('c_t5_t30', length=2, delay_cost=1)
	S += c_t5_t30 >= 46
	c_t5_t30 += MAS[4]

	c_t1_t2_t1 = S.Task('c_t1_t2_t1', length=6, delay_cost=1)
	S += c_t1_t2_t1 >= 47
	c_t1_t2_t1 += MM[0]

	c_t2_t2_t0_in = S.Task('c_t2_t2_t0_in', length=1, delay_cost=1)
	S += c_t2_t2_t0_in >= 47
	c_t2_t2_t0_in += MM_in[0]

	c_t2_t2_t0_mem0 = S.Task('c_t2_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t0_mem0 >= 47
	c_t2_t2_t0_mem0 += MAS_MEM[0]

	c_t2_t2_t0_mem1 = S.Task('c_t2_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t0_mem1 >= 47
	c_t2_t2_t0_mem1 += MAS_MEM[3]

	c_t2_t40 = S.Task('c_t2_t40', length=2, delay_cost=1)
	S += c_t2_t40 >= 47
	c_t2_t40 += MAS[0]

	c_t4_t2_t2 = S.Task('c_t4_t2_t2', length=2, delay_cost=1)
	S += c_t4_t2_t2 >= 47
	c_t4_t2_t2 += MAS[3]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 47
	c_t4_t31_in += MAS_in[1]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 47
	c_t4_t31_mem0 += MM_MEM[0]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 47
	c_t4_t31_mem1 += MAS_MEM[9]

	c_t1_t2_t2_in = S.Task('c_t1_t2_t2_in', length=1, delay_cost=1)
	S += c_t1_t2_t2_in >= 48
	c_t1_t2_t2_in += MAS_in[1]

	c_t1_t2_t2_mem0 = S.Task('c_t1_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t2_mem0 >= 48
	c_t1_t2_t2_mem0 += MAS_MEM[0]

	c_t1_t2_t2_mem1 = S.Task('c_t1_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t2_mem1 >= 48
	c_t1_t2_t2_mem1 += MAS_MEM[1]

	c_t2_t2_t0 = S.Task('c_t2_t2_t0', length=6, delay_cost=1)
	S += c_t2_t2_t0 >= 48
	c_t2_t2_t0 += MM[0]

	c_t4_t31 = S.Task('c_t4_t31', length=2, delay_cost=1)
	S += c_t4_t31 >= 48
	c_t4_t31 += MAS[1]

	c_t510_in = S.Task('c_t510_in', length=1, delay_cost=1)
	S += c_t510_in >= 48
	c_t510_in += MAS_in[3]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	S += c_t510_mem0 >= 48
	c_t510_mem0 += MAS_MEM[8]

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	S += c_t510_mem1 >= 48
	c_t510_mem1 += MAS_MEM[9]

	c_t5_t2_t1_in = S.Task('c_t5_t2_t1_in', length=1, delay_cost=1)
	S += c_t5_t2_t1_in >= 48
	c_t5_t2_t1_in += MM_in[0]

	c_t5_t2_t1_mem0 = S.Task('c_t5_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t1_mem0 >= 48
	c_t5_t2_t1_mem0 += MAS_MEM[6]

	c_t5_t2_t1_mem1 = S.Task('c_t5_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t1_mem1 >= 48
	c_t5_t2_t1_mem1 += MAS_MEM[3]

	c_t1_t2_t2 = S.Task('c_t1_t2_t2', length=2, delay_cost=1)
	S += c_t1_t2_t2 >= 49
	c_t1_t2_t2 += MAS[1]

	c_t1_t41_in = S.Task('c_t1_t41_in', length=1, delay_cost=1)
	S += c_t1_t41_in >= 49
	c_t1_t41_in += MAS_in[2]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 49
	c_t1_t41_mem0 += MAS_MEM[0]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 49
	c_t1_t41_mem1 += MAS_MEM[5]

	c_t510 = S.Task('c_t510', length=2, delay_cost=1)
	S += c_t510 >= 49
	c_t510 += MAS[3]

	c_t5_t2_t0_in = S.Task('c_t5_t2_t0_in', length=1, delay_cost=1)
	S += c_t5_t2_t0_in >= 49
	c_t5_t2_t0_in += MM_in[0]

	c_t5_t2_t0_mem0 = S.Task('c_t5_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t0_mem0 >= 49
	c_t5_t2_t0_mem0 += MAS_MEM[4]

	c_t5_t2_t0_mem1 = S.Task('c_t5_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t0_mem1 >= 49
	c_t5_t2_t0_mem1 += MAS_MEM[1]

	c_t5_t2_t1 = S.Task('c_t5_t2_t1', length=6, delay_cost=1)
	S += c_t5_t2_t1 >= 49
	c_t5_t2_t1 += MM[0]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 49
	c_t5_t31_in += MAS_in[3]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 49
	c_t5_t31_mem0 += MM_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 49
	c_t5_t31_mem1 += MAS_MEM[9]

	c_t0_t2_t4_in = S.Task('c_t0_t2_t4_in', length=1, delay_cost=1)
	S += c_t0_t2_t4_in >= 50
	c_t0_t2_t4_in += MM_in[0]

	c_t0_t2_t4_mem0 = S.Task('c_t0_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t4_mem0 >= 50
	c_t0_t2_t4_mem0 += MAS_MEM[4]

	c_t0_t2_t4_mem1 = S.Task('c_t0_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t4_mem1 >= 50
	c_t0_t2_t4_mem1 += MAS_MEM[7]

	c_t0_t2_t5_in = S.Task('c_t0_t2_t5_in', length=1, delay_cost=1)
	S += c_t0_t2_t5_in >= 50
	c_t0_t2_t5_in += MAS_in[2]

	c_t0_t2_t5_mem0 = S.Task('c_t0_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t5_mem0 >= 50
	c_t0_t2_t5_mem0 += MM_MEM[0]

	c_t0_t2_t5_mem1 = S.Task('c_t0_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t5_mem1 >= 50
	c_t0_t2_t5_mem1 += MM_MEM[1]

	c_t111_in = S.Task('c_t111_in', length=1, delay_cost=1)
	S += c_t111_in >= 50
	c_t111_in += MAS_in[0]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 50
	c_t111_mem0 += MAS_MEM[0]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 50
	c_t111_mem1 += MAS_MEM[1]

	c_t1_t41 = S.Task('c_t1_t41', length=2, delay_cost=1)
	S += c_t1_t41 >= 50
	c_t1_t41 += MAS[2]

	c_t5_t2_t0 = S.Task('c_t5_t2_t0', length=6, delay_cost=1)
	S += c_t5_t2_t0 >= 50
	c_t5_t2_t0 += MM[0]

	c_t5_t31 = S.Task('c_t5_t31', length=2, delay_cost=1)
	S += c_t5_t31 >= 50
	c_t5_t31 += MAS[3]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 51
	c_t0_t20_in += MAS_in[3]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 51
	c_t0_t20_mem0 += MM_MEM[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 51
	c_t0_t20_mem1 += MM_MEM[1]

	c_t0_t2_t4 = S.Task('c_t0_t2_t4', length=6, delay_cost=1)
	S += c_t0_t2_t4 >= 51
	c_t0_t2_t4 += MM[0]

	c_t0_t2_t5 = S.Task('c_t0_t2_t5', length=2, delay_cost=1)
	S += c_t0_t2_t5 >= 51
	c_t0_t2_t5 += MAS[2]

	c_t111 = S.Task('c_t111', length=2, delay_cost=1)
	S += c_t111 >= 51
	c_t111 += MAS[0]

	c_t1_t2_t4_in = S.Task('c_t1_t2_t4_in', length=1, delay_cost=1)
	S += c_t1_t2_t4_in >= 51
	c_t1_t2_t4_in += MM_in[0]

	c_t1_t2_t4_mem0 = S.Task('c_t1_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t4_mem0 >= 51
	c_t1_t2_t4_mem0 += MAS_MEM[2]

	c_t1_t2_t4_mem1 = S.Task('c_t1_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t4_mem1 >= 51
	c_t1_t2_t4_mem1 += MAS_MEM[7]

	c_t0_t20 = S.Task('c_t0_t20', length=2, delay_cost=1)
	S += c_t0_t20 >= 52
	c_t0_t20 += MAS[3]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 52
	c_t1_t20_in += MAS_in[2]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 52
	c_t1_t20_mem0 += MM_MEM[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 52
	c_t1_t20_mem1 += MM_MEM[1]

	c_t1_t2_t4 = S.Task('c_t1_t2_t4', length=6, delay_cost=1)
	S += c_t1_t2_t4 >= 52
	c_t1_t2_t4 += MM[0]

	c_t4_t2_t0_in = S.Task('c_t4_t2_t0_in', length=1, delay_cost=1)
	S += c_t4_t2_t0_in >= 52
	c_t4_t2_t0_in += MM_in[0]

	c_t4_t2_t0_mem0 = S.Task('c_t4_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t0_mem0 >= 52
	c_t4_t2_t0_mem0 += MAS_MEM[4]

	c_t4_t2_t0_mem1 = S.Task('c_t4_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t0_mem1 >= 52
	c_t4_t2_t0_mem1 += MAS_MEM[9]

	c_t1_t20 = S.Task('c_t1_t20', length=2, delay_cost=1)
	S += c_t1_t20 >= 53
	c_t1_t20 += MAS[2]

	c_t2_t2_t4_in = S.Task('c_t2_t2_t4_in', length=1, delay_cost=1)
	S += c_t2_t2_t4_in >= 53
	c_t2_t2_t4_in += MM_in[0]

	c_t2_t2_t4_mem0 = S.Task('c_t2_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t4_mem0 >= 53
	c_t2_t2_t4_mem0 += MAS_MEM[8]

	c_t2_t2_t4_mem1 = S.Task('c_t2_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t4_mem1 >= 53
	c_t2_t2_t4_mem1 += MAS_MEM[9]

	c_t2_t2_t5_in = S.Task('c_t2_t2_t5_in', length=1, delay_cost=1)
	S += c_t2_t2_t5_in >= 53
	c_t2_t2_t5_in += MAS_in[2]

	c_t2_t2_t5_mem0 = S.Task('c_t2_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t5_mem0 >= 53
	c_t2_t2_t5_mem0 += MM_MEM[0]

	c_t2_t2_t5_mem1 = S.Task('c_t2_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t5_mem1 >= 53
	c_t2_t2_t5_mem1 += MM_MEM[1]

	c_t4_t2_t0 = S.Task('c_t4_t2_t0', length=6, delay_cost=1)
	S += c_t4_t2_t0 >= 53
	c_t4_t2_t0 += MM[0]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 54
	c_t2_t20_in += MAS_in[2]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 54
	c_t2_t20_mem0 += MM_MEM[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 54
	c_t2_t20_mem1 += MM_MEM[1]

	c_t2_t2_t4 = S.Task('c_t2_t2_t4', length=6, delay_cost=1)
	S += c_t2_t2_t4 >= 54
	c_t2_t2_t4 += MM[0]

	c_t2_t2_t5 = S.Task('c_t2_t2_t5', length=2, delay_cost=1)
	S += c_t2_t2_t5 >= 54
	c_t2_t2_t5 += MAS[2]

	c_t4_t2_t1_in = S.Task('c_t4_t2_t1_in', length=1, delay_cost=1)
	S += c_t4_t2_t1_in >= 54
	c_t4_t2_t1_in += MM_in[0]

	c_t4_t2_t1_mem0 = S.Task('c_t4_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t1_mem0 >= 54
	c_t4_t2_t1_mem0 += MAS_MEM[6]

	c_t4_t2_t1_mem1 = S.Task('c_t4_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t1_mem1 >= 54
	c_t4_t2_t1_mem1 += MAS_MEM[9]

	c_t1_t2_t5_in = S.Task('c_t1_t2_t5_in', length=1, delay_cost=1)
	S += c_t1_t2_t5_in >= 55
	c_t1_t2_t5_in += MAS_in[4]

	c_t1_t2_t5_mem0 = S.Task('c_t1_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t5_mem0 >= 55
	c_t1_t2_t5_mem0 += MM_MEM[0]

	c_t1_t2_t5_mem1 = S.Task('c_t1_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t5_mem1 >= 55
	c_t1_t2_t5_mem1 += MM_MEM[1]

	c_t2_t20 = S.Task('c_t2_t20', length=2, delay_cost=1)
	S += c_t2_t20 >= 55
	c_t2_t20 += MAS[2]

	c_t4_t2_t1 = S.Task('c_t4_t2_t1', length=6, delay_cost=1)
	S += c_t4_t2_t1 >= 55
	c_t4_t2_t1 += MM[0]

	c_t1_t2_t5 = S.Task('c_t1_t2_t5', length=2, delay_cost=1)
	S += c_t1_t2_t5 >= 56
	c_t1_t2_t5 += MAS[4]


	# new tasks
	c_t0_t21 = S.Task('c_t0_t21', length=2, delay_cost=1)
	c_t0_t21 += alt(MAS)
	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	c_t0_t21_in += alt(MAS_in)
	S += c_t0_t21_in*MAS_in[0]<=c_t0_t21*MAS[0]

	S += c_t0_t21_in*MAS_in[1]<=c_t0_t21*MAS[1]

	S += c_t0_t21_in*MAS_in[2]<=c_t0_t21*MAS[2]

	S += c_t0_t21_in*MAS_in[3]<=c_t0_t21*MAS[3]

	S += c_t0_t21_in*MAS_in[4]<=c_t0_t21*MAS[4]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	c_t0_t21_mem0 += MM_MEM[0]
	S += 56 < c_t0_t21_mem0
	S += c_t0_t21_mem0 <= c_t0_t21

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	c_t0_t21_mem1 += MAS_MEM[5]
	S += 52 < c_t0_t21_mem1
	S += c_t0_t21_mem1 <= c_t0_t21

	c_t0_t50 = S.Task('c_t0_t50', length=2, delay_cost=1)
	c_t0_t50 += alt(MAS)
	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	c_t0_t50_in += alt(MAS_in)
	S += c_t0_t50_in*MAS_in[0]<=c_t0_t50*MAS[0]

	S += c_t0_t50_in*MAS_in[1]<=c_t0_t50*MAS[1]

	S += c_t0_t50_in*MAS_in[2]<=c_t0_t50*MAS[2]

	S += c_t0_t50_in*MAS_in[3]<=c_t0_t50*MAS[3]

	S += c_t0_t50_in*MAS_in[4]<=c_t0_t50*MAS[4]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	c_t0_t50_mem0 += MAS_MEM[2]
	S += 38 < c_t0_t50_mem0
	S += c_t0_t50_mem0 <= c_t0_t50

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	c_t0_t50_mem1 += MAS_MEM[3]
	S += 44 < c_t0_t50_mem1
	S += c_t0_t50_mem1 <= c_t0_t50

	c_t0_t51 = S.Task('c_t0_t51', length=2, delay_cost=1)
	c_t0_t51 += alt(MAS)
	c_t0_t51_in = S.Task('c_t0_t51_in', length=1, delay_cost=1)
	c_t0_t51_in += alt(MAS_in)
	S += c_t0_t51_in*MAS_in[0]<=c_t0_t51*MAS[0]

	S += c_t0_t51_in*MAS_in[1]<=c_t0_t51*MAS[1]

	S += c_t0_t51_in*MAS_in[2]<=c_t0_t51*MAS[2]

	S += c_t0_t51_in*MAS_in[3]<=c_t0_t51*MAS[3]

	S += c_t0_t51_in*MAS_in[4]<=c_t0_t51*MAS[4]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	c_t0_t51_mem0 += MAS_MEM[8]
	S += 41 < c_t0_t51_mem0
	S += c_t0_t51_mem0 <= c_t0_t51

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	c_t0_t51_mem1 += MAS_MEM[7]
	S += 46 < c_t0_t51_mem1
	S += c_t0_t51_mem1 <= c_t0_t51

	c_t1_t21 = S.Task('c_t1_t21', length=2, delay_cost=1)
	c_t1_t21 += alt(MAS)
	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	c_t1_t21_in += alt(MAS_in)
	S += c_t1_t21_in*MAS_in[0]<=c_t1_t21*MAS[0]

	S += c_t1_t21_in*MAS_in[1]<=c_t1_t21*MAS[1]

	S += c_t1_t21_in*MAS_in[2]<=c_t1_t21*MAS[2]

	S += c_t1_t21_in*MAS_in[3]<=c_t1_t21*MAS[3]

	S += c_t1_t21_in*MAS_in[4]<=c_t1_t21*MAS[4]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	c_t1_t21_mem0 += MM_MEM[0]
	S += 57 < c_t1_t21_mem0
	S += c_t1_t21_mem0 <= c_t1_t21

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	c_t1_t21_mem1 += MAS_MEM[9]
	S += 57 < c_t1_t21_mem1
	S += c_t1_t21_mem1 <= c_t1_t21

	c_t1_t50 = S.Task('c_t1_t50', length=2, delay_cost=1)
	c_t1_t50 += alt(MAS)
	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	c_t1_t50_in += alt(MAS_in)
	S += c_t1_t50_in*MAS_in[0]<=c_t1_t50*MAS[0]

	S += c_t1_t50_in*MAS_in[1]<=c_t1_t50*MAS[1]

	S += c_t1_t50_in*MAS_in[2]<=c_t1_t50*MAS[2]

	S += c_t1_t50_in*MAS_in[3]<=c_t1_t50*MAS[3]

	S += c_t1_t50_in*MAS_in[4]<=c_t1_t50*MAS[4]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	c_t1_t50_mem0 += MAS_MEM[4]
	S += 34 < c_t1_t50_mem0
	S += c_t1_t50_mem0 <= c_t1_t50

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	c_t1_t50_mem1 += MAS_MEM[9]
	S += 45 < c_t1_t50_mem1
	S += c_t1_t50_mem1 <= c_t1_t50

	c_t1_t51 = S.Task('c_t1_t51', length=2, delay_cost=1)
	c_t1_t51 += alt(MAS)
	c_t1_t51_in = S.Task('c_t1_t51_in', length=1, delay_cost=1)
	c_t1_t51_in += alt(MAS_in)
	S += c_t1_t51_in*MAS_in[0]<=c_t1_t51*MAS[0]

	S += c_t1_t51_in*MAS_in[1]<=c_t1_t51*MAS[1]

	S += c_t1_t51_in*MAS_in[2]<=c_t1_t51*MAS[2]

	S += c_t1_t51_in*MAS_in[3]<=c_t1_t51*MAS[3]

	S += c_t1_t51_in*MAS_in[4]<=c_t1_t51*MAS[4]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	c_t1_t51_mem0 += MAS_MEM[0]
	S += 35 < c_t1_t51_mem0
	S += c_t1_t51_mem0 <= c_t1_t51

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	c_t1_t51_mem1 += MAS_MEM[5]
	S += 51 < c_t1_t51_mem1
	S += c_t1_t51_mem1 <= c_t1_t51

	c_t2_t21 = S.Task('c_t2_t21', length=2, delay_cost=1)
	c_t2_t21 += alt(MAS)
	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	c_t2_t21_in += alt(MAS_in)
	S += c_t2_t21_in*MAS_in[0]<=c_t2_t21*MAS[0]

	S += c_t2_t21_in*MAS_in[1]<=c_t2_t21*MAS[1]

	S += c_t2_t21_in*MAS_in[2]<=c_t2_t21*MAS[2]

	S += c_t2_t21_in*MAS_in[3]<=c_t2_t21*MAS[3]

	S += c_t2_t21_in*MAS_in[4]<=c_t2_t21*MAS[4]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	c_t2_t21_mem0 += MM_MEM[0]
	S += 59 < c_t2_t21_mem0
	S += c_t2_t21_mem0 <= c_t2_t21

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	c_t2_t21_mem1 += MAS_MEM[5]
	S += 55 < c_t2_t21_mem1
	S += c_t2_t21_mem1 <= c_t2_t21

	c_t2_t50 = S.Task('c_t2_t50', length=2, delay_cost=1)
	c_t2_t50 += alt(MAS)
	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	c_t2_t50_in += alt(MAS_in)
	S += c_t2_t50_in*MAS_in[0]<=c_t2_t50*MAS[0]

	S += c_t2_t50_in*MAS_in[1]<=c_t2_t50*MAS[1]

	S += c_t2_t50_in*MAS_in[2]<=c_t2_t50*MAS[2]

	S += c_t2_t50_in*MAS_in[3]<=c_t2_t50*MAS[3]

	S += c_t2_t50_in*MAS_in[4]<=c_t2_t50*MAS[4]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	c_t2_t50_mem0 += MAS_MEM[8]
	S += 28 < c_t2_t50_mem0
	S += c_t2_t50_mem0 <= c_t2_t50

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	c_t2_t50_mem1 += MAS_MEM[1]
	S += 48 < c_t2_t50_mem1
	S += c_t2_t50_mem1 <= c_t2_t50

	c_t2_t51 = S.Task('c_t2_t51', length=2, delay_cost=1)
	c_t2_t51 += alt(MAS)
	c_t2_t51_in = S.Task('c_t2_t51_in', length=1, delay_cost=1)
	c_t2_t51_in += alt(MAS_in)
	S += c_t2_t51_in*MAS_in[0]<=c_t2_t51*MAS[0]

	S += c_t2_t51_in*MAS_in[1]<=c_t2_t51*MAS[1]

	S += c_t2_t51_in*MAS_in[2]<=c_t2_t51*MAS[2]

	S += c_t2_t51_in*MAS_in[3]<=c_t2_t51*MAS[3]

	S += c_t2_t51_in*MAS_in[4]<=c_t2_t51*MAS[4]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	c_t2_t51_mem0 += MAS_MEM[4]
	S += 39 < c_t2_t51_mem0
	S += c_t2_t51_mem0 <= c_t2_t51

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	c_t2_t51_mem1 += MAS_MEM[5]
	S += 43 < c_t2_t51_mem1
	S += c_t2_t51_mem1 <= c_t2_t51

	c_t3_t2_t4 = S.Task('c_t3_t2_t4', length=6, delay_cost=1)
	c_t3_t2_t4 += alt(MM)
	c_t3_t2_t4_in = S.Task('c_t3_t2_t4_in', length=1, delay_cost=1)
	c_t3_t2_t4_in += alt(MM_in)
	S += c_t3_t2_t4_in*MM_in[0]<=c_t3_t2_t4*MM[0]
	c_t3_t2_t4_mem0 = S.Task('c_t3_t2_t4_mem0', length=1, delay_cost=1)
	c_t3_t2_t4_mem0 += MAS_MEM[2]
	S += 23 < c_t3_t2_t4_mem0
	S += c_t3_t2_t4_mem0 <= c_t3_t2_t4

	c_t3_t2_t4_mem1 = S.Task('c_t3_t2_t4_mem1', length=1, delay_cost=1)
	c_t3_t2_t4_mem1 += MAS_MEM[7]
	S += 22 < c_t3_t2_t4_mem1
	S += c_t3_t2_t4_mem1 <= c_t3_t2_t4

	c_t3_t20 = S.Task('c_t3_t20', length=2, delay_cost=1)
	c_t3_t20 += alt(MAS)
	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	c_t3_t20_in += alt(MAS_in)
	S += c_t3_t20_in*MAS_in[0]<=c_t3_t20*MAS[0]

	S += c_t3_t20_in*MAS_in[1]<=c_t3_t20*MAS[1]

	S += c_t3_t20_in*MAS_in[2]<=c_t3_t20*MAS[2]

	S += c_t3_t20_in*MAS_in[3]<=c_t3_t20*MAS[3]

	S += c_t3_t20_in*MAS_in[4]<=c_t3_t20*MAS[4]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	c_t3_t20_mem0 += MM_MEM[0]
	S += 19 < c_t3_t20_mem0
	S += c_t3_t20_mem0 <= c_t3_t20

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	c_t3_t20_mem1 += MM_MEM[1]
	S += 28 < c_t3_t20_mem1
	S += c_t3_t20_mem1 <= c_t3_t20

	c_t3_t2_t5 = S.Task('c_t3_t2_t5', length=2, delay_cost=1)
	c_t3_t2_t5 += alt(MAS)
	c_t3_t2_t5_in = S.Task('c_t3_t2_t5_in', length=1, delay_cost=1)
	c_t3_t2_t5_in += alt(MAS_in)
	S += c_t3_t2_t5_in*MAS_in[0]<=c_t3_t2_t5*MAS[0]

	S += c_t3_t2_t5_in*MAS_in[1]<=c_t3_t2_t5*MAS[1]

	S += c_t3_t2_t5_in*MAS_in[2]<=c_t3_t2_t5*MAS[2]

	S += c_t3_t2_t5_in*MAS_in[3]<=c_t3_t2_t5*MAS[3]

	S += c_t3_t2_t5_in*MAS_in[4]<=c_t3_t2_t5*MAS[4]

	c_t3_t2_t5_mem0 = S.Task('c_t3_t2_t5_mem0', length=1, delay_cost=1)
	c_t3_t2_t5_mem0 += MM_MEM[0]
	S += 19 < c_t3_t2_t5_mem0
	S += c_t3_t2_t5_mem0 <= c_t3_t2_t5

	c_t3_t2_t5_mem1 = S.Task('c_t3_t2_t5_mem1', length=1, delay_cost=1)
	c_t3_t2_t5_mem1 += MM_MEM[1]
	S += 28 < c_t3_t2_t5_mem1
	S += c_t3_t2_t5_mem1 <= c_t3_t2_t5

	c_t3_t40 = S.Task('c_t3_t40', length=2, delay_cost=1)
	c_t3_t40 += alt(MAS)
	c_t3_t40_in = S.Task('c_t3_t40_in', length=1, delay_cost=1)
	c_t3_t40_in += alt(MAS_in)
	S += c_t3_t40_in*MAS_in[0]<=c_t3_t40*MAS[0]

	S += c_t3_t40_in*MAS_in[1]<=c_t3_t40*MAS[1]

	S += c_t3_t40_in*MAS_in[2]<=c_t3_t40*MAS[2]

	S += c_t3_t40_in*MAS_in[3]<=c_t3_t40*MAS[3]

	S += c_t3_t40_in*MAS_in[4]<=c_t3_t40*MAS[4]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	c_t3_t40_mem0 += MAS_MEM[2]
	S += 27 < c_t3_t40_mem0
	S += c_t3_t40_mem0 <= c_t3_t40

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	c_t3_t40_mem1 += MAS_MEM[9]
	S += 30 < c_t3_t40_mem1
	S += c_t3_t40_mem1 <= c_t3_t40

	c_t3_t41 = S.Task('c_t3_t41', length=2, delay_cost=1)
	c_t3_t41 += alt(MAS)
	c_t3_t41_in = S.Task('c_t3_t41_in', length=1, delay_cost=1)
	c_t3_t41_in += alt(MAS_in)
	S += c_t3_t41_in*MAS_in[0]<=c_t3_t41*MAS[0]

	S += c_t3_t41_in*MAS_in[1]<=c_t3_t41*MAS[1]

	S += c_t3_t41_in*MAS_in[2]<=c_t3_t41*MAS[2]

	S += c_t3_t41_in*MAS_in[3]<=c_t3_t41*MAS[3]

	S += c_t3_t41_in*MAS_in[4]<=c_t3_t41*MAS[4]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	c_t3_t41_mem0 += MAS_MEM[8]
	S += 30 < c_t3_t41_mem0
	S += c_t3_t41_mem0 <= c_t3_t41

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	c_t3_t41_mem1 += MAS_MEM[3]
	S += 27 < c_t3_t41_mem1
	S += c_t3_t41_mem1 <= c_t3_t41

	c_t311 = S.Task('c_t311', length=2, delay_cost=1)
	c_t311 += alt(MAS)
	c_t311_in = S.Task('c_t311_in', length=1, delay_cost=1)
	c_t311_in += alt(MAS_in)
	S += c_t311_in*MAS_in[0]<=c_t311*MAS[0]

	S += c_t311_in*MAS_in[1]<=c_t311*MAS[1]

	S += c_t311_in*MAS_in[2]<=c_t311*MAS[2]

	S += c_t311_in*MAS_in[3]<=c_t311*MAS[3]

	S += c_t311_in*MAS_in[4]<=c_t311*MAS[4]

	c_t311_mem0 = S.Task('c_t311_mem0', length=1, delay_cost=1)
	c_t311_mem0 += MAS_MEM[8]
	S += 30 < c_t311_mem0
	S += c_t311_mem0 <= c_t311

	c_t311_mem1 = S.Task('c_t311_mem1', length=1, delay_cost=1)
	c_t311_mem1 += MAS_MEM[9]
	S += 30 < c_t311_mem1
	S += c_t311_mem1 <= c_t311

	c_t4_t2_t4 = S.Task('c_t4_t2_t4', length=6, delay_cost=1)
	c_t4_t2_t4 += alt(MM)
	c_t4_t2_t4_in = S.Task('c_t4_t2_t4_in', length=1, delay_cost=1)
	c_t4_t2_t4_in += alt(MM_in)
	S += c_t4_t2_t4_in*MM_in[0]<=c_t4_t2_t4*MM[0]
	c_t4_t2_t4_mem0 = S.Task('c_t4_t2_t4_mem0', length=1, delay_cost=1)
	c_t4_t2_t4_mem0 += MAS_MEM[6]
	S += 48 < c_t4_t2_t4_mem0
	S += c_t4_t2_t4_mem0 <= c_t4_t2_t4

	c_t4_t2_t4_mem1 = S.Task('c_t4_t2_t4_mem1', length=1, delay_cost=1)
	c_t4_t2_t4_mem1 += MAS_MEM[5]
	S += 38 < c_t4_t2_t4_mem1
	S += c_t4_t2_t4_mem1 <= c_t4_t2_t4

	c_t4_t20 = S.Task('c_t4_t20', length=2, delay_cost=1)
	c_t4_t20 += alt(MAS)
	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	c_t4_t20_in += alt(MAS_in)
	S += c_t4_t20_in*MAS_in[0]<=c_t4_t20*MAS[0]

	S += c_t4_t20_in*MAS_in[1]<=c_t4_t20*MAS[1]

	S += c_t4_t20_in*MAS_in[2]<=c_t4_t20*MAS[2]

	S += c_t4_t20_in*MAS_in[3]<=c_t4_t20*MAS[3]

	S += c_t4_t20_in*MAS_in[4]<=c_t4_t20*MAS[4]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	c_t4_t20_mem0 += MM_MEM[0]
	S += 58 < c_t4_t20_mem0
	S += c_t4_t20_mem0 <= c_t4_t20

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	c_t4_t20_mem1 += MM_MEM[1]
	S += 60 < c_t4_t20_mem1
	S += c_t4_t20_mem1 <= c_t4_t20

	c_t4_t2_t5 = S.Task('c_t4_t2_t5', length=2, delay_cost=1)
	c_t4_t2_t5 += alt(MAS)
	c_t4_t2_t5_in = S.Task('c_t4_t2_t5_in', length=1, delay_cost=1)
	c_t4_t2_t5_in += alt(MAS_in)
	S += c_t4_t2_t5_in*MAS_in[0]<=c_t4_t2_t5*MAS[0]

	S += c_t4_t2_t5_in*MAS_in[1]<=c_t4_t2_t5*MAS[1]

	S += c_t4_t2_t5_in*MAS_in[2]<=c_t4_t2_t5*MAS[2]

	S += c_t4_t2_t5_in*MAS_in[3]<=c_t4_t2_t5*MAS[3]

	S += c_t4_t2_t5_in*MAS_in[4]<=c_t4_t2_t5*MAS[4]

	c_t4_t2_t5_mem0 = S.Task('c_t4_t2_t5_mem0', length=1, delay_cost=1)
	c_t4_t2_t5_mem0 += MM_MEM[0]
	S += 58 < c_t4_t2_t5_mem0
	S += c_t4_t2_t5_mem0 <= c_t4_t2_t5

	c_t4_t2_t5_mem1 = S.Task('c_t4_t2_t5_mem1', length=1, delay_cost=1)
	c_t4_t2_t5_mem1 += MM_MEM[1]
	S += 60 < c_t4_t2_t5_mem1
	S += c_t4_t2_t5_mem1 <= c_t4_t2_t5

	c_t4_t40 = S.Task('c_t4_t40', length=2, delay_cost=1)
	c_t4_t40 += alt(MAS)
	c_t4_t40_in = S.Task('c_t4_t40_in', length=1, delay_cost=1)
	c_t4_t40_in += alt(MAS_in)
	S += c_t4_t40_in*MAS_in[0]<=c_t4_t40*MAS[0]

	S += c_t4_t40_in*MAS_in[1]<=c_t4_t40*MAS[1]

	S += c_t4_t40_in*MAS_in[2]<=c_t4_t40*MAS[2]

	S += c_t4_t40_in*MAS_in[3]<=c_t4_t40*MAS[3]

	S += c_t4_t40_in*MAS_in[4]<=c_t4_t40*MAS[4]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	c_t4_t40_mem0 += MAS_MEM[6]
	S += 44 < c_t4_t40_mem0
	S += c_t4_t40_mem0 <= c_t4_t40

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	c_t4_t40_mem1 += MAS_MEM[3]
	S += 49 < c_t4_t40_mem1
	S += c_t4_t40_mem1 <= c_t4_t40

	c_t4_t41 = S.Task('c_t4_t41', length=2, delay_cost=1)
	c_t4_t41 += alt(MAS)
	c_t4_t41_in = S.Task('c_t4_t41_in', length=1, delay_cost=1)
	c_t4_t41_in += alt(MAS_in)
	S += c_t4_t41_in*MAS_in[0]<=c_t4_t41*MAS[0]

	S += c_t4_t41_in*MAS_in[1]<=c_t4_t41*MAS[1]

	S += c_t4_t41_in*MAS_in[2]<=c_t4_t41*MAS[2]

	S += c_t4_t41_in*MAS_in[3]<=c_t4_t41*MAS[3]

	S += c_t4_t41_in*MAS_in[4]<=c_t4_t41*MAS[4]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	c_t4_t41_mem0 += MAS_MEM[2]
	S += 49 < c_t4_t41_mem0
	S += c_t4_t41_mem0 <= c_t4_t41

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	c_t4_t41_mem1 += MAS_MEM[7]
	S += 44 < c_t4_t41_mem1
	S += c_t4_t41_mem1 <= c_t4_t41

	c_t411 = S.Task('c_t411', length=2, delay_cost=1)
	c_t411 += alt(MAS)
	c_t411_in = S.Task('c_t411_in', length=1, delay_cost=1)
	c_t411_in += alt(MAS_in)
	S += c_t411_in*MAS_in[0]<=c_t411*MAS[0]

	S += c_t411_in*MAS_in[1]<=c_t411*MAS[1]

	S += c_t411_in*MAS_in[2]<=c_t411*MAS[2]

	S += c_t411_in*MAS_in[3]<=c_t411*MAS[3]

	S += c_t411_in*MAS_in[4]<=c_t411*MAS[4]

	c_t411_mem0 = S.Task('c_t411_mem0', length=1, delay_cost=1)
	c_t411_mem0 += MAS_MEM[2]
	S += 49 < c_t411_mem0
	S += c_t411_mem0 <= c_t411

	c_t411_mem1 = S.Task('c_t411_mem1', length=1, delay_cost=1)
	c_t411_mem1 += MAS_MEM[3]
	S += 49 < c_t411_mem1
	S += c_t411_mem1 <= c_t411

	c_t5_t2_t4 = S.Task('c_t5_t2_t4', length=6, delay_cost=1)
	c_t5_t2_t4 += alt(MM)
	c_t5_t2_t4_in = S.Task('c_t5_t2_t4_in', length=1, delay_cost=1)
	c_t5_t2_t4_in += alt(MM_in)
	S += c_t5_t2_t4_in*MM_in[0]<=c_t5_t2_t4*MM[0]
	c_t5_t2_t4_mem0 = S.Task('c_t5_t2_t4_mem0', length=1, delay_cost=1)
	c_t5_t2_t4_mem0 += MAS_MEM[6]
	S += 47 < c_t5_t2_t4_mem0
	S += c_t5_t2_t4_mem0 <= c_t5_t2_t4

	c_t5_t2_t4_mem1 = S.Task('c_t5_t2_t4_mem1', length=1, delay_cost=1)
	c_t5_t2_t4_mem1 += MAS_MEM[9]
	S += 42 < c_t5_t2_t4_mem1
	S += c_t5_t2_t4_mem1 <= c_t5_t2_t4

	c_t5_t20 = S.Task('c_t5_t20', length=2, delay_cost=1)
	c_t5_t20 += alt(MAS)
	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	c_t5_t20_in += alt(MAS_in)
	S += c_t5_t20_in*MAS_in[0]<=c_t5_t20*MAS[0]

	S += c_t5_t20_in*MAS_in[1]<=c_t5_t20*MAS[1]

	S += c_t5_t20_in*MAS_in[2]<=c_t5_t20*MAS[2]

	S += c_t5_t20_in*MAS_in[3]<=c_t5_t20*MAS[3]

	S += c_t5_t20_in*MAS_in[4]<=c_t5_t20*MAS[4]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	c_t5_t20_mem0 += MM_MEM[0]
	S += 55 < c_t5_t20_mem0
	S += c_t5_t20_mem0 <= c_t5_t20

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	c_t5_t20_mem1 += MM_MEM[1]
	S += 54 < c_t5_t20_mem1
	S += c_t5_t20_mem1 <= c_t5_t20

	c_t5_t2_t5 = S.Task('c_t5_t2_t5', length=2, delay_cost=1)
	c_t5_t2_t5 += alt(MAS)
	c_t5_t2_t5_in = S.Task('c_t5_t2_t5_in', length=1, delay_cost=1)
	c_t5_t2_t5_in += alt(MAS_in)
	S += c_t5_t2_t5_in*MAS_in[0]<=c_t5_t2_t5*MAS[0]

	S += c_t5_t2_t5_in*MAS_in[1]<=c_t5_t2_t5*MAS[1]

	S += c_t5_t2_t5_in*MAS_in[2]<=c_t5_t2_t5*MAS[2]

	S += c_t5_t2_t5_in*MAS_in[3]<=c_t5_t2_t5*MAS[3]

	S += c_t5_t2_t5_in*MAS_in[4]<=c_t5_t2_t5*MAS[4]

	c_t5_t2_t5_mem0 = S.Task('c_t5_t2_t5_mem0', length=1, delay_cost=1)
	c_t5_t2_t5_mem0 += MM_MEM[0]
	S += 55 < c_t5_t2_t5_mem0
	S += c_t5_t2_t5_mem0 <= c_t5_t2_t5

	c_t5_t2_t5_mem1 = S.Task('c_t5_t2_t5_mem1', length=1, delay_cost=1)
	c_t5_t2_t5_mem1 += MM_MEM[1]
	S += 54 < c_t5_t2_t5_mem1
	S += c_t5_t2_t5_mem1 <= c_t5_t2_t5

	c_t5_t40 = S.Task('c_t5_t40', length=2, delay_cost=1)
	c_t5_t40 += alt(MAS)
	c_t5_t40_in = S.Task('c_t5_t40_in', length=1, delay_cost=1)
	c_t5_t40_in += alt(MAS_in)
	S += c_t5_t40_in*MAS_in[0]<=c_t5_t40*MAS[0]

	S += c_t5_t40_in*MAS_in[1]<=c_t5_t40*MAS[1]

	S += c_t5_t40_in*MAS_in[2]<=c_t5_t40*MAS[2]

	S += c_t5_t40_in*MAS_in[3]<=c_t5_t40*MAS[3]

	S += c_t5_t40_in*MAS_in[4]<=c_t5_t40*MAS[4]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	c_t5_t40_mem0 += MAS_MEM[8]
	S += 47 < c_t5_t40_mem0
	S += c_t5_t40_mem0 <= c_t5_t40

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	c_t5_t40_mem1 += MAS_MEM[7]
	S += 51 < c_t5_t40_mem1
	S += c_t5_t40_mem1 <= c_t5_t40

	c_t5_t41 = S.Task('c_t5_t41', length=2, delay_cost=1)
	c_t5_t41 += alt(MAS)
	c_t5_t41_in = S.Task('c_t5_t41_in', length=1, delay_cost=1)
	c_t5_t41_in += alt(MAS_in)
	S += c_t5_t41_in*MAS_in[0]<=c_t5_t41*MAS[0]

	S += c_t5_t41_in*MAS_in[1]<=c_t5_t41*MAS[1]

	S += c_t5_t41_in*MAS_in[2]<=c_t5_t41*MAS[2]

	S += c_t5_t41_in*MAS_in[3]<=c_t5_t41*MAS[3]

	S += c_t5_t41_in*MAS_in[4]<=c_t5_t41*MAS[4]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	c_t5_t41_mem0 += MAS_MEM[6]
	S += 51 < c_t5_t41_mem0
	S += c_t5_t41_mem0 <= c_t5_t41

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	c_t5_t41_mem1 += MAS_MEM[9]
	S += 47 < c_t5_t41_mem1
	S += c_t5_t41_mem1 <= c_t5_t41

	c_t511 = S.Task('c_t511', length=2, delay_cost=1)
	c_t511 += alt(MAS)
	c_t511_in = S.Task('c_t511_in', length=1, delay_cost=1)
	c_t511_in += alt(MAS_in)
	S += c_t511_in*MAS_in[0]<=c_t511*MAS[0]

	S += c_t511_in*MAS_in[1]<=c_t511*MAS[1]

	S += c_t511_in*MAS_in[2]<=c_t511*MAS[2]

	S += c_t511_in*MAS_in[3]<=c_t511*MAS[3]

	S += c_t511_in*MAS_in[4]<=c_t511*MAS[4]

	c_t511_mem0 = S.Task('c_t511_mem0', length=1, delay_cost=1)
	c_t511_mem0 += MAS_MEM[6]
	S += 51 < c_t511_mem0
	S += c_t511_mem0 <= c_t511

	c_t511_mem1 = S.Task('c_t511_mem1', length=1, delay_cost=1)
	c_t511_mem1 += MAS_MEM[7]
	S += 51 < c_t511_mem1
	S += c_t511_mem1 <= c_t511

	c_s0011 = S.Task('c_s0011', length=2, delay_cost=1)
	c_s0011 += alt(MAS)
	c_s0011_in = S.Task('c_s0011_in', length=1, delay_cost=1)
	c_s0011_in += alt(MAS_in)
	S += c_s0011_in*MAS_in[0]<=c_s0011*MAS[0]

	S += c_s0011_in*MAS_in[1]<=c_s0011*MAS[1]

	S += c_s0011_in*MAS_in[2]<=c_s0011*MAS[2]

	S += c_s0011_in*MAS_in[3]<=c_s0011*MAS[3]

	S += c_s0011_in*MAS_in[4]<=c_s0011*MAS[4]

	c_s0011_mem0 = S.Task('c_s0011_mem0', length=1, delay_cost=1)
	c_s0011_mem0 += MAS_MEM[6]
	S += 45 < c_s0011_mem0
	S += c_s0011_mem0 <= c_s0011

	c_s0011_mem1 = S.Task('c_s0011_mem1', length=1, delay_cost=1)
	c_s0011_mem1 += MAS_MEM[1]
	S += 52 < c_s0011_mem1
	S += c_s0011_mem1 <= c_s0011

	c_s010 = S.Task('c_s010', length=2, delay_cost=1)
	c_s010 += alt(MAS)
	c_s010_in = S.Task('c_s010_in', length=1, delay_cost=1)
	c_s010_in += alt(MAS_in)
	S += c_s010_in*MAS_in[0]<=c_s010*MAS[0]

	S += c_s010_in*MAS_in[1]<=c_s010*MAS[1]

	S += c_s010_in*MAS_in[2]<=c_s010*MAS[2]

	S += c_s010_in*MAS_in[3]<=c_s010*MAS[3]

	S += c_s010_in*MAS_in[4]<=c_s010*MAS[4]

	c_s010_mem0 = S.Task('c_s010_mem0', length=1, delay_cost=1)
	c_s010_mem0 += MAS_MEM[6]
	S += 29 < c_s010_mem0
	S += c_s010_mem0 <= c_s010

	c_s010_mem1 = S.Task('c_s010_mem1', length=1, delay_cost=1)
	c_s010_mem1 += MAS_MEM[1]
	S += 45 < c_s010_mem1
	S += c_s010_mem1 <= c_s010

	c_s1011 = S.Task('c_s1011', length=2, delay_cost=1)
	c_s1011 += alt(MAS)
	c_s1011_in = S.Task('c_s1011_in', length=1, delay_cost=1)
	c_s1011_in += alt(MAS_in)
	S += c_s1011_in*MAS_in[0]<=c_s1011*MAS[0]

	S += c_s1011_in*MAS_in[1]<=c_s1011*MAS[1]

	S += c_s1011_in*MAS_in[2]<=c_s1011*MAS[2]

	S += c_s1011_in*MAS_in[3]<=c_s1011*MAS[3]

	S += c_s1011_in*MAS_in[4]<=c_s1011*MAS[4]

	c_s1011_mem0 = S.Task('c_s1011_mem0', length=1, delay_cost=1)
	c_s1011_mem0 += MAS_MEM[0]
	S += 52 < c_s1011_mem0
	S += c_s1011_mem0 <= c_s1011

	c_s1011_mem1 = S.Task('c_s1011_mem1', length=1, delay_cost=1)
	c_s1011_mem1 += MAS_MEM[1]
	S += 46 < c_s1011_mem1
	S += c_s1011_mem1 <= c_s1011

	c_s1110 = S.Task('c_s1110', length=2, delay_cost=1)
	c_s1110 += alt(MAS)
	c_s1110_in = S.Task('c_s1110_in', length=1, delay_cost=1)
	c_s1110_in += alt(MAS_in)
	S += c_s1110_in*MAS_in[0]<=c_s1110*MAS[0]

	S += c_s1110_in*MAS_in[1]<=c_s1110*MAS[1]

	S += c_s1110_in*MAS_in[2]<=c_s1110*MAS[2]

	S += c_s1110_in*MAS_in[3]<=c_s1110*MAS[3]

	S += c_s1110_in*MAS_in[4]<=c_s1110*MAS[4]

	c_s1110_mem0 = S.Task('c_s1110_mem0', length=1, delay_cost=1)
	c_s1110_mem0 += MAS_MEM[2]
	S += 46 < c_s1110_mem0
	S += c_s1110_mem0 <= c_s1110

	c_s1110_mem1 = S.Task('c_s1110_mem1', length=1, delay_cost=1)
	c_s1110_mem1 += MAS_MEM[5]
	S += 45 < c_s1110_mem1
	S += c_s1110_mem1 <= c_s1110

	c_s2011 = S.Task('c_s2011', length=2, delay_cost=1)
	c_s2011 += alt(MAS)
	c_s2011_in = S.Task('c_s2011_in', length=1, delay_cost=1)
	c_s2011_in += alt(MAS_in)
	S += c_s2011_in*MAS_in[0]<=c_s2011*MAS[0]

	S += c_s2011_in*MAS_in[1]<=c_s2011*MAS[1]

	S += c_s2011_in*MAS_in[2]<=c_s2011*MAS[2]

	S += c_s2011_in*MAS_in[3]<=c_s2011*MAS[3]

	S += c_s2011_in*MAS_in[4]<=c_s2011*MAS[4]

	c_s2011_mem0 = S.Task('c_s2011_mem0', length=1, delay_cost=1)
	c_s2011_mem0 += MAS_MEM[0]
	S += 46 < c_s2011_mem0
	S += c_s2011_mem0 <= c_s2011

	c_s2011_mem1 = S.Task('c_s2011_mem1', length=1, delay_cost=1)
	c_s2011_mem1 += MAS_MEM[7]
	S += 45 < c_s2011_mem1
	S += c_s2011_mem1 <= c_s2011

	c_s210 = S.Task('c_s210', length=2, delay_cost=1)
	c_s210 += alt(MAS)
	c_s210_in = S.Task('c_s210_in', length=1, delay_cost=1)
	c_s210_in += alt(MAS_in)
	S += c_s210_in*MAS_in[0]<=c_s210*MAS[0]

	S += c_s210_in*MAS_in[1]<=c_s210*MAS[1]

	S += c_s210_in*MAS_in[2]<=c_s210*MAS[2]

	S += c_s210_in*MAS_in[3]<=c_s210*MAS[3]

	S += c_s210_in*MAS_in[4]<=c_s210*MAS[4]

	c_s210_mem0 = S.Task('c_s210_mem0', length=1, delay_cost=1)
	c_s210_mem0 += MAS_MEM[6]
	S += 50 < c_s210_mem0
	S += c_s210_mem0 <= c_s210

	c_s210_mem1 = S.Task('c_s210_mem1', length=1, delay_cost=1)
	c_s210_mem1 += MAS_MEM[5]
	S += 47 < c_s210_mem1
	S += c_s210_mem1 <= c_s210

	c_t6_y1_0 = S.Task('c_t6_y1_0', length=2, delay_cost=1)
	c_t6_y1_0 += alt(MAS)
	c_t6_y1_0_in = S.Task('c_t6_y1_0_in', length=1, delay_cost=1)
	c_t6_y1_0_in += alt(MAS_in)
	S += c_t6_y1_0_in*MAS_in[0]<=c_t6_y1_0*MAS[0]

	S += c_t6_y1_0_in*MAS_in[1]<=c_t6_y1_0*MAS[1]

	S += c_t6_y1_0_in*MAS_in[2]<=c_t6_y1_0*MAS[2]

	S += c_t6_y1_0_in*MAS_in[3]<=c_t6_y1_0*MAS[3]

	S += c_t6_y1_0_in*MAS_in[4]<=c_t6_y1_0*MAS[4]

	c_t6_y1_0_mem0 = S.Task('c_t6_y1_0_mem0', length=1, delay_cost=1)
	c_t6_y1_0_mem0 += MAS_MEM[2]
	S += 30 < c_t6_y1_0_mem0
	S += c_t6_y1_0_mem0 <= c_t6_y1_0

	c_t6_y1_0_mem1 = S.Task('c_t6_y1_0_mem1', length=1, delay_cost=1)
	c_t6_y1_0_mem1 += MAS_MEM[1]
	S += 46 < c_t6_y1_0_mem1
	S += c_t6_y1_0_mem1 <= c_t6_y1_0

	c_t6_y1_1 = S.Task('c_t6_y1_1', length=2, delay_cost=1)
	c_t6_y1_1 += alt(MAS)
	c_t6_y1_1_in = S.Task('c_t6_y1_1_in', length=1, delay_cost=1)
	c_t6_y1_1_in += alt(MAS_in)
	S += c_t6_y1_1_in*MAS_in[0]<=c_t6_y1_1*MAS[0]

	S += c_t6_y1_1_in*MAS_in[1]<=c_t6_y1_1*MAS[1]

	S += c_t6_y1_1_in*MAS_in[2]<=c_t6_y1_1*MAS[2]

	S += c_t6_y1_1_in*MAS_in[3]<=c_t6_y1_1*MAS[3]

	S += c_t6_y1_1_in*MAS_in[4]<=c_t6_y1_1*MAS[4]

	c_t6_y1_1_mem0 = S.Task('c_t6_y1_1_mem0', length=1, delay_cost=1)
	c_t6_y1_1_mem0 += MAS_MEM[0]
	S += 46 < c_t6_y1_1_mem0
	S += c_t6_y1_1_mem0 <= c_t6_y1_1

	c_t6_y1_1_mem1 = S.Task('c_t6_y1_1_mem1', length=1, delay_cost=1)
	c_t6_y1_1_mem1 += MAS_MEM[3]
	S += 30 < c_t6_y1_1_mem1
	S += c_t6_y1_1_mem1 <= c_t6_y1_1

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage2MAS5/SQR/schedule4.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

