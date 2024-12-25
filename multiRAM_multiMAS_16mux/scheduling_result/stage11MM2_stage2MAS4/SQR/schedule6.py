from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 203
	S = Scenario("schedule6", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 0
	c_t3010_in += MAS_in[3]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 0
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 0
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3010 = S.Task('c_t3010', length=2, delay_cost=1)
	S += c_t3010 >= 1
	c_t3010 += MAS[3]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 1
	c_t4000_in += MAS_in[0]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 1
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 1
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t2_in = S.Task('c_t1_t3_t2_in', length=1, delay_cost=1)
	S += c_t1_t3_t2_in >= 2
	c_t1_t3_t2_in += MAS_in[0]

	c_t1_t3_t2_mem0 = S.Task('c_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem0 >= 2
	c_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t2_mem1 = S.Task('c_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t2_mem1 >= 2
	c_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=2, delay_cost=1)
	S += c_t4000 >= 2
	c_t4000 += MAS[0]

	c_t1_a1_0_in = S.Task('c_t1_a1_0_in', length=1, delay_cost=1)
	S += c_t1_a1_0_in >= 3
	c_t1_a1_0_in += MAS_in[0]

	c_t1_a1_0_mem0 = S.Task('c_t1_a1_0_mem0', length=1, delay_cost=1)
	S += c_t1_a1_0_mem0 >= 3
	c_t1_a1_0_mem0 += MAIN_MEM_r[0]

	c_t1_a1_0_mem1 = S.Task('c_t1_a1_0_mem1', length=1, delay_cost=1)
	S += c_t1_a1_0_mem1 >= 3
	c_t1_a1_0_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t2 = S.Task('c_t1_t3_t2', length=2, delay_cost=1)
	S += c_t1_t3_t2 >= 3
	c_t1_t3_t2 += MAS[0]

	c_t1_a1_0 = S.Task('c_t1_a1_0', length=2, delay_cost=1)
	S += c_t1_a1_0 >= 4
	c_t1_a1_0 += MAS[0]

	c_t2_t3_t3_in = S.Task('c_t2_t3_t3_in', length=1, delay_cost=1)
	S += c_t2_t3_t3_in >= 4
	c_t2_t3_t3_in += MAS_in[1]

	c_t2_t3_t3_mem0 = S.Task('c_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem0 >= 4
	c_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t3_mem1 = S.Task('c_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t3_mem1 >= 4
	c_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t2_in = S.Task('c_t0_t3_t2_in', length=1, delay_cost=1)
	S += c_t0_t3_t2_in >= 5
	c_t0_t3_t2_in += MAS_in[1]

	c_t0_t3_t2_mem0 = S.Task('c_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem0 >= 5
	c_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t2_mem1 = S.Task('c_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t2_mem1 >= 5
	c_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t3 = S.Task('c_t2_t3_t3', length=2, delay_cost=1)
	S += c_t2_t3_t3 >= 5
	c_t2_t3_t3 += MAS[1]

	c_t0_t3_t2 = S.Task('c_t0_t3_t2', length=2, delay_cost=1)
	S += c_t0_t3_t2 >= 6
	c_t0_t3_t2 += MAS[1]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 6
	c_t1_t11_in += MAS_in[0]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 6
	c_t1_t11_mem0 += MAIN_MEM_r[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 6
	c_t1_t11_mem1 += MAIN_MEM_r[1]

	c_t1_t11 = S.Task('c_t1_t11', length=2, delay_cost=1)
	S += c_t1_t11 >= 7
	c_t1_t11 += MAS[0]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 7
	c_t2_t10_in += MAS_in[2]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 7
	c_t2_t10_mem0 += MAIN_MEM_r[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 7
	c_t2_t10_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=2, delay_cost=1)
	S += c_t2_t10 >= 8
	c_t2_t10 += MAS[2]

	c_t2_t3_t2_in = S.Task('c_t2_t3_t2_in', length=1, delay_cost=1)
	S += c_t2_t3_t2_in >= 8
	c_t2_t3_t2_in += MAS_in[0]

	c_t2_t3_t2_mem0 = S.Task('c_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem0 >= 8
	c_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t2_mem1 = S.Task('c_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t2_mem1 >= 8
	c_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 9
	c_t2_t11_in += MAS_in[2]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 9
	c_t2_t11_mem0 += MAIN_MEM_r[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 9
	c_t2_t11_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t2 = S.Task('c_t2_t3_t2', length=2, delay_cost=1)
	S += c_t2_t3_t2 >= 9
	c_t2_t3_t2 += MAS[0]

	c_t0_t3_t1_in = S.Task('c_t0_t3_t1_in', length=1, delay_cost=1)
	S += c_t0_t3_t1_in >= 10
	c_t0_t3_t1_in += MM_in[1]

	c_t0_t3_t1_mem0 = S.Task('c_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem0 >= 10
	c_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t1_mem1 = S.Task('c_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t1_mem1 >= 10
	c_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=2, delay_cost=1)
	S += c_t2_t11 >= 10
	c_t2_t11 += MAS[2]

	c_t2_t3_t4_in = S.Task('c_t2_t3_t4_in', length=1, delay_cost=1)
	S += c_t2_t3_t4_in >= 10
	c_t2_t3_t4_in += MM_in[0]

	c_t2_t3_t4_mem0 = S.Task('c_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem0 >= 10
	c_t2_t3_t4_mem0 += MAS_MEM[0]

	c_t2_t3_t4_mem1 = S.Task('c_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t4_mem1 >= 10
	c_t2_t3_t4_mem1 += MAS_MEM[3]

	c_t0_t3_t1 = S.Task('c_t0_t3_t1', length=11, delay_cost=1)
	S += c_t0_t3_t1 >= 11
	c_t0_t3_t1 += MM[1]

	c_t1_a1_1_in = S.Task('c_t1_a1_1_in', length=1, delay_cost=1)
	S += c_t1_a1_1_in >= 11
	c_t1_a1_1_in += MAS_in[1]

	c_t1_a1_1_mem0 = S.Task('c_t1_a1_1_mem0', length=1, delay_cost=1)
	S += c_t1_a1_1_mem0 >= 11
	c_t1_a1_1_mem0 += MAIN_MEM_r[0]

	c_t1_a1_1_mem1 = S.Task('c_t1_a1_1_mem1', length=1, delay_cost=1)
	S += c_t1_a1_1_mem1 >= 11
	c_t1_a1_1_mem1 += MAIN_MEM_r[1]

	c_t2_t2_t3_in = S.Task('c_t2_t2_t3_in', length=1, delay_cost=1)
	S += c_t2_t2_t3_in >= 11
	c_t2_t2_t3_in += MAS_in[0]

	c_t2_t2_t3_mem0 = S.Task('c_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem0 >= 11
	c_t2_t2_t3_mem0 += MAS_MEM[4]

	c_t2_t2_t3_mem1 = S.Task('c_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t3_mem1 >= 11
	c_t2_t2_t3_mem1 += MAS_MEM[5]

	c_t2_t3_t4 = S.Task('c_t2_t3_t4', length=11, delay_cost=1)
	S += c_t2_t3_t4 >= 11
	c_t2_t3_t4 += MM[0]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 12
	c_t0_t11_in += MAS_in[0]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 12
	c_t0_t11_mem0 += MAIN_MEM_r[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 12
	c_t0_t11_mem1 += MAIN_MEM_r[1]

	c_t1_a1_1 = S.Task('c_t1_a1_1', length=2, delay_cost=1)
	S += c_t1_a1_1 >= 12
	c_t1_a1_1 += MAS[1]

	c_t2_t2_t3 = S.Task('c_t2_t2_t3', length=2, delay_cost=1)
	S += c_t2_t2_t3 >= 12
	c_t2_t2_t3 += MAS[0]

	c_t0_t11 = S.Task('c_t0_t11', length=2, delay_cost=1)
	S += c_t0_t11 >= 13
	c_t0_t11 += MAS[0]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 13
	c_t3001_in += MAS_in[3]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 13
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 13
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t0_in = S.Task('c_t1_t3_t0_in', length=1, delay_cost=1)
	S += c_t1_t3_t0_in >= 14
	c_t1_t3_t0_in += MM_in[0]

	c_t1_t3_t0_mem0 = S.Task('c_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem0 >= 14
	c_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t0_mem1 = S.Task('c_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t0_mem1 >= 14
	c_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=2, delay_cost=1)
	S += c_t3001 >= 14
	c_t3001 += MAS[3]

	c_t1_t3_t0 = S.Task('c_t1_t3_t0', length=11, delay_cost=1)
	S += c_t1_t3_t0 >= 15
	c_t1_t3_t0 += MM[0]

	c_t2_a1_1_in = S.Task('c_t2_a1_1_in', length=1, delay_cost=1)
	S += c_t2_a1_1_in >= 15
	c_t2_a1_1_in += MAS_in[3]

	c_t2_a1_1_mem0 = S.Task('c_t2_a1_1_mem0', length=1, delay_cost=1)
	S += c_t2_a1_1_mem0 >= 15
	c_t2_a1_1_mem0 += MAIN_MEM_r[0]

	c_t2_a1_1_mem1 = S.Task('c_t2_a1_1_mem1', length=1, delay_cost=1)
	S += c_t2_a1_1_mem1 >= 15
	c_t2_a1_1_mem1 += MAIN_MEM_r[1]

	c_t2_a1_1 = S.Task('c_t2_a1_1', length=2, delay_cost=1)
	S += c_t2_a1_1 >= 16
	c_t2_a1_1 += MAS[3]

	c_t2_t3_t0_in = S.Task('c_t2_t3_t0_in', length=1, delay_cost=1)
	S += c_t2_t3_t0_in >= 16
	c_t2_t3_t0_in += MM_in[0]

	c_t2_t3_t0_mem0 = S.Task('c_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem0 >= 16
	c_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t0_mem1 = S.Task('c_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t0_mem1 >= 16
	c_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t0 = S.Task('c_t2_t3_t0', length=11, delay_cost=1)
	S += c_t2_t3_t0 >= 17
	c_t2_t3_t0 += MM[0]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 17
	c_t4001_in += MAS_in[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 17
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 17
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t2_a1_0_in = S.Task('c_t2_a1_0_in', length=1, delay_cost=1)
	S += c_t2_a1_0_in >= 18
	c_t2_a1_0_in += MAS_in[0]

	c_t2_a1_0_mem0 = S.Task('c_t2_a1_0_mem0', length=1, delay_cost=1)
	S += c_t2_a1_0_mem0 >= 18
	c_t2_a1_0_mem0 += MAIN_MEM_r[0]

	c_t2_a1_0_mem1 = S.Task('c_t2_a1_0_mem1', length=1, delay_cost=1)
	S += c_t2_a1_0_mem1 >= 18
	c_t2_a1_0_mem1 += MAIN_MEM_r[1]

	c_t4001 = S.Task('c_t4001', length=2, delay_cost=1)
	S += c_t4001 >= 18
	c_t4001 += MAS[1]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 19
	c_t1_t10_in += MAS_in[2]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 19
	c_t1_t10_mem0 += MAIN_MEM_r[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 19
	c_t1_t10_mem1 += MAIN_MEM_r[1]

	c_t2_a1_0 = S.Task('c_t2_a1_0', length=2, delay_cost=1)
	S += c_t2_a1_0 >= 19
	c_t2_a1_0 += MAS[0]

	c_t4_t3_t2_in = S.Task('c_t4_t3_t2_in', length=1, delay_cost=1)
	S += c_t4_t3_t2_in >= 19
	c_t4_t3_t2_in += MAS_in[0]

	c_t4_t3_t2_mem0 = S.Task('c_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem0 >= 19
	c_t4_t3_t2_mem0 += MAS_MEM[0]

	c_t4_t3_t2_mem1 = S.Task('c_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t2_mem1 >= 19
	c_t4_t3_t2_mem1 += MAS_MEM[3]

	c_t1_t10 = S.Task('c_t1_t10', length=2, delay_cost=1)
	S += c_t1_t10 >= 20
	c_t1_t10 += MAS[2]

	c_t1_t3_t1_in = S.Task('c_t1_t3_t1_in', length=1, delay_cost=1)
	S += c_t1_t3_t1_in >= 20
	c_t1_t3_t1_in += MM_in[1]

	c_t1_t3_t1_mem0 = S.Task('c_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem0 >= 20
	c_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t1_mem1 = S.Task('c_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t1_mem1 >= 20
	c_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t4_t3_t2 = S.Task('c_t4_t3_t2', length=2, delay_cost=1)
	S += c_t4_t3_t2 >= 20
	c_t4_t3_t2 += MAS[0]

	c_t1_t2_t3_in = S.Task('c_t1_t2_t3_in', length=1, delay_cost=1)
	S += c_t1_t2_t3_in >= 21
	c_t1_t2_t3_in += MAS_in[2]

	c_t1_t2_t3_mem0 = S.Task('c_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem0 >= 21
	c_t1_t2_t3_mem0 += MAS_MEM[4]

	c_t1_t2_t3_mem1 = S.Task('c_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t3_mem1 >= 21
	c_t1_t2_t3_mem1 += MAS_MEM[1]

	c_t1_t3_t1 = S.Task('c_t1_t3_t1', length=11, delay_cost=1)
	S += c_t1_t3_t1 >= 21
	c_t1_t3_t1 += MM[1]

	c_t1_t3_t3_in = S.Task('c_t1_t3_t3_in', length=1, delay_cost=1)
	S += c_t1_t3_t3_in >= 21
	c_t1_t3_t3_in += MAS_in[3]

	c_t1_t3_t3_mem0 = S.Task('c_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem0 >= 21
	c_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t3_t3_mem1 = S.Task('c_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t3_mem1 >= 21
	c_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t3_in = S.Task('c_t0_t3_t3_in', length=1, delay_cost=1)
	S += c_t0_t3_t3_in >= 22
	c_t0_t3_t3_in += MAS_in[3]

	c_t0_t3_t3_mem0 = S.Task('c_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem0 >= 22
	c_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t3_mem1 = S.Task('c_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t3_mem1 >= 22
	c_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t2_t3 = S.Task('c_t1_t2_t3', length=2, delay_cost=1)
	S += c_t1_t2_t3 >= 22
	c_t1_t2_t3 += MAS[2]

	c_t1_t3_t3 = S.Task('c_t1_t3_t3', length=2, delay_cost=1)
	S += c_t1_t3_t3 >= 22
	c_t1_t3_t3 += MAS[3]

	c_t0_t3_t3 = S.Task('c_t0_t3_t3', length=2, delay_cost=1)
	S += c_t0_t3_t3 >= 23
	c_t0_t3_t3 += MAS[3]

	c_t1_t3_t4_in = S.Task('c_t1_t3_t4_in', length=1, delay_cost=1)
	S += c_t1_t3_t4_in >= 23
	c_t1_t3_t4_in += MM_in[0]

	c_t1_t3_t4_mem0 = S.Task('c_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem0 >= 23
	c_t1_t3_t4_mem0 += MAS_MEM[0]

	c_t1_t3_t4_mem1 = S.Task('c_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t4_mem1 >= 23
	c_t1_t3_t4_mem1 += MAS_MEM[7]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 23
	c_t3000_in += MAS_in[0]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 23
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 23
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t4_in = S.Task('c_t0_t3_t4_in', length=1, delay_cost=1)
	S += c_t0_t3_t4_in >= 24
	c_t0_t3_t4_in += MM_in[0]

	c_t0_t3_t4_mem0 = S.Task('c_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem0 >= 24
	c_t0_t3_t4_mem0 += MAS_MEM[2]

	c_t0_t3_t4_mem1 = S.Task('c_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t4_mem1 >= 24
	c_t0_t3_t4_mem1 += MAS_MEM[7]

	c_t1_t3_t4 = S.Task('c_t1_t3_t4', length=11, delay_cost=1)
	S += c_t1_t3_t4 >= 24
	c_t1_t3_t4 += MM[0]

	c_t3000 = S.Task('c_t3000', length=2, delay_cost=1)
	S += c_t3000 >= 24
	c_t3000 += MAS[0]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 24
	c_t3011_in += MAS_in[0]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 24
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 24
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t0_t3_t4 = S.Task('c_t0_t3_t4', length=11, delay_cost=1)
	S += c_t0_t3_t4 >= 25
	c_t0_t3_t4 += MM[0]

	c_t2_t3_t1_in = S.Task('c_t2_t3_t1_in', length=1, delay_cost=1)
	S += c_t2_t3_t1_in >= 25
	c_t2_t3_t1_in += MM_in[1]

	c_t2_t3_t1_mem0 = S.Task('c_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem0 >= 25
	c_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t3_t1_mem1 = S.Task('c_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t1_mem1 >= 25
	c_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=2, delay_cost=1)
	S += c_t3011 >= 25
	c_t3011 += MAS[0]

	c_t3_t3_t2_in = S.Task('c_t3_t3_t2_in', length=1, delay_cost=1)
	S += c_t3_t3_t2_in >= 25
	c_t3_t3_t2_in += MAS_in[0]

	c_t3_t3_t2_mem0 = S.Task('c_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem0 >= 25
	c_t3_t3_t2_mem0 += MAS_MEM[0]

	c_t3_t3_t2_mem1 = S.Task('c_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t2_mem1 >= 25
	c_t3_t3_t2_mem1 += MAS_MEM[7]

	c_t0_a1_1_in = S.Task('c_t0_a1_1_in', length=1, delay_cost=1)
	S += c_t0_a1_1_in >= 26
	c_t0_a1_1_in += MAS_in[0]

	c_t0_a1_1_mem0 = S.Task('c_t0_a1_1_mem0', length=1, delay_cost=1)
	S += c_t0_a1_1_mem0 >= 26
	c_t0_a1_1_mem0 += MAIN_MEM_r[0]

	c_t0_a1_1_mem1 = S.Task('c_t0_a1_1_mem1', length=1, delay_cost=1)
	S += c_t0_a1_1_mem1 >= 26
	c_t0_a1_1_mem1 += MAIN_MEM_r[1]

	c_t2_t3_t1 = S.Task('c_t2_t3_t1', length=11, delay_cost=1)
	S += c_t2_t3_t1 >= 26
	c_t2_t3_t1 += MM[1]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 26
	c_t3_t10_in += MAS_in[1]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 26
	c_t3_t10_mem0 += MAS_MEM[0]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 26
	c_t3_t10_mem1 += MAS_MEM[7]

	c_t3_t11_in = S.Task('c_t3_t11_in', length=1, delay_cost=1)
	S += c_t3_t11_in >= 26
	c_t3_t11_in += MAS_in[3]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 26
	c_t3_t11_mem0 += MAS_MEM[6]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 26
	c_t3_t11_mem1 += MAS_MEM[1]

	c_t3_t3_t2 = S.Task('c_t3_t3_t2', length=2, delay_cost=1)
	S += c_t3_t3_t2 >= 26
	c_t3_t3_t2 += MAS[0]

	c_t0_a1_1 = S.Task('c_t0_a1_1', length=2, delay_cost=1)
	S += c_t0_a1_1 >= 27
	c_t0_a1_1 += MAS[0]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 27
	c_t0_t10_in += MAS_in[0]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 27
	c_t0_t10_mem0 += MAIN_MEM_r[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 27
	c_t0_t10_mem1 += MAIN_MEM_r[1]

	c_t3_t10 = S.Task('c_t3_t10', length=2, delay_cost=1)
	S += c_t3_t10 >= 27
	c_t3_t10 += MAS[1]

	c_t3_t11 = S.Task('c_t3_t11', length=2, delay_cost=1)
	S += c_t3_t11 >= 27
	c_t3_t11 += MAS[3]

	c_t3_t3_t0_in = S.Task('c_t3_t3_t0_in', length=1, delay_cost=1)
	S += c_t3_t3_t0_in >= 27
	c_t3_t3_t0_in += MM_in[1]

	c_t3_t3_t0_mem0 = S.Task('c_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem0 >= 27
	c_t3_t3_t0_mem0 += MAS_MEM[0]

	c_t3_t3_t0_mem1 = S.Task('c_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t0_mem1 >= 27
	c_t3_t3_t0_mem1 += MAS_MEM[7]

	c_t3_t3_t1_in = S.Task('c_t3_t3_t1_in', length=1, delay_cost=1)
	S += c_t3_t3_t1_in >= 27
	c_t3_t3_t1_in += MM_in[0]

	c_t3_t3_t1_mem0 = S.Task('c_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem0 >= 27
	c_t3_t3_t1_mem0 += MAS_MEM[6]

	c_t3_t3_t1_mem1 = S.Task('c_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t1_mem1 >= 27
	c_t3_t3_t1_mem1 += MAS_MEM[1]

	c_t0_a1_0_in = S.Task('c_t0_a1_0_in', length=1, delay_cost=1)
	S += c_t0_a1_0_in >= 28
	c_t0_a1_0_in += MAS_in[0]

	c_t0_a1_0_mem0 = S.Task('c_t0_a1_0_mem0', length=1, delay_cost=1)
	S += c_t0_a1_0_mem0 >= 28
	c_t0_a1_0_mem0 += MAIN_MEM_r[0]

	c_t0_a1_0_mem1 = S.Task('c_t0_a1_0_mem1', length=1, delay_cost=1)
	S += c_t0_a1_0_mem1 >= 28
	c_t0_a1_0_mem1 += MAIN_MEM_r[1]

	c_t0_t10 = S.Task('c_t0_t10', length=2, delay_cost=1)
	S += c_t0_t10 >= 28
	c_t0_t10 += MAS[0]

	c_t3_a1_1_in = S.Task('c_t3_a1_1_in', length=1, delay_cost=1)
	S += c_t3_a1_1_in >= 28
	c_t3_a1_1_in += MAS_in[3]

	c_t3_a1_1_mem0 = S.Task('c_t3_a1_1_mem0', length=1, delay_cost=1)
	S += c_t3_a1_1_mem0 >= 28
	c_t3_a1_1_mem0 += MAS_MEM[0]

	c_t3_a1_1_mem1 = S.Task('c_t3_a1_1_mem1', length=1, delay_cost=1)
	S += c_t3_a1_1_mem1 >= 28
	c_t3_a1_1_mem1 += MAS_MEM[7]

	c_t3_t3_t0 = S.Task('c_t3_t3_t0', length=11, delay_cost=1)
	S += c_t3_t3_t0 >= 28
	c_t3_t3_t0 += MM[1]

	c_t3_t3_t1 = S.Task('c_t3_t3_t1', length=11, delay_cost=1)
	S += c_t3_t3_t1 >= 28
	c_t3_t3_t1 += MM[0]

	c_t3_t3_t3_in = S.Task('c_t3_t3_t3_in', length=1, delay_cost=1)
	S += c_t3_t3_t3_in >= 28
	c_t3_t3_t3_in += MAS_in[1]

	c_t3_t3_t3_mem0 = S.Task('c_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem0 >= 28
	c_t3_t3_t3_mem0 += MAS_MEM[6]

	c_t3_t3_t3_mem1 = S.Task('c_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t3_mem1 >= 28
	c_t3_t3_t3_mem1 += MAS_MEM[1]

	c_t0_a1_0 = S.Task('c_t0_a1_0', length=2, delay_cost=1)
	S += c_t0_a1_0 >= 29
	c_t0_a1_0 += MAS[0]

	c_t0_t2_t3_in = S.Task('c_t0_t2_t3_in', length=1, delay_cost=1)
	S += c_t0_t2_t3_in >= 29
	c_t0_t2_t3_in += MAS_in[2]

	c_t0_t2_t3_mem0 = S.Task('c_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem0 >= 29
	c_t0_t2_t3_mem0 += MAS_MEM[0]

	c_t0_t2_t3_mem1 = S.Task('c_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t3_mem1 >= 29
	c_t0_t2_t3_mem1 += MAS_MEM[1]

	c_t0_t3_t0_in = S.Task('c_t0_t3_t0_in', length=1, delay_cost=1)
	S += c_t0_t3_t0_in >= 29
	c_t0_t3_t0_in += MM_in[0]

	c_t0_t3_t0_mem0 = S.Task('c_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem0 >= 29
	c_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t3_t0_mem1 = S.Task('c_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t0_mem1 >= 29
	c_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t3_a1_1 = S.Task('c_t3_a1_1', length=2, delay_cost=1)
	S += c_t3_a1_1 >= 29
	c_t3_a1_1 += MAS[3]

	c_t3_t2_t3_in = S.Task('c_t3_t2_t3_in', length=1, delay_cost=1)
	S += c_t3_t2_t3_in >= 29
	c_t3_t2_t3_in += MAS_in[0]

	c_t3_t2_t3_mem0 = S.Task('c_t3_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t3_mem0 >= 29
	c_t3_t2_t3_mem0 += MAS_MEM[2]

	c_t3_t2_t3_mem1 = S.Task('c_t3_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t3_mem1 >= 29
	c_t3_t2_t3_mem1 += MAS_MEM[7]

	c_t3_t3_t3 = S.Task('c_t3_t3_t3', length=2, delay_cost=1)
	S += c_t3_t3_t3 >= 29
	c_t3_t3_t3 += MAS[1]

	c_t0_t2_t3 = S.Task('c_t0_t2_t3', length=2, delay_cost=1)
	S += c_t0_t2_t3 >= 30
	c_t0_t2_t3 += MAS[2]

	c_t0_t3_t0 = S.Task('c_t0_t3_t0', length=11, delay_cost=1)
	S += c_t0_t3_t0 >= 30
	c_t0_t3_t0 += MM[0]

	c_t3_a1_0_in = S.Task('c_t3_a1_0_in', length=1, delay_cost=1)
	S += c_t3_a1_0_in >= 30
	c_t3_a1_0_in += MAS_in[1]

	c_t3_a1_0_mem0 = S.Task('c_t3_a1_0_mem0', length=1, delay_cost=1)
	S += c_t3_a1_0_mem0 >= 30
	c_t3_a1_0_mem0 += MAS_MEM[6]

	c_t3_a1_0_mem1 = S.Task('c_t3_a1_0_mem1', length=1, delay_cost=1)
	S += c_t3_a1_0_mem1 >= 30
	c_t3_a1_0_mem1 += MAS_MEM[1]

	c_t3_t2_t3 = S.Task('c_t3_t2_t3', length=2, delay_cost=1)
	S += c_t3_t2_t3 >= 30
	c_t3_t2_t3 += MAS[0]

	c_t3_t3_t4_in = S.Task('c_t3_t3_t4_in', length=1, delay_cost=1)
	S += c_t3_t3_t4_in >= 30
	c_t3_t3_t4_in += MM_in[0]

	c_t3_t3_t4_mem0 = S.Task('c_t3_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t4_mem0 >= 30
	c_t3_t3_t4_mem0 += MAS_MEM[0]

	c_t3_t3_t4_mem1 = S.Task('c_t3_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t4_mem1 >= 30
	c_t3_t3_t4_mem1 += MAS_MEM[3]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 30
	c_t4011_in += MAS_in[0]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 30
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 30
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t1_t3_t5_in = S.Task('c_t1_t3_t5_in', length=1, delay_cost=1)
	S += c_t1_t3_t5_in >= 31
	c_t1_t3_t5_in += MAS_in[0]

	c_t1_t3_t5_mem0 = S.Task('c_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem0 >= 31
	c_t1_t3_t5_mem0 += MM_MEM[0]

	c_t1_t3_t5_mem1 = S.Task('c_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t3_t5_mem1 >= 31
	c_t1_t3_t5_mem1 += MM_MEM[3]

	c_t3_a1_0 = S.Task('c_t3_a1_0', length=2, delay_cost=1)
	S += c_t3_a1_0 >= 31
	c_t3_a1_0 += MAS[1]

	c_t3_t01_in = S.Task('c_t3_t01_in', length=1, delay_cost=1)
	S += c_t3_t01_in >= 31
	c_t3_t01_in += MAS_in[3]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 31
	c_t3_t01_mem0 += MAS_MEM[6]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 31
	c_t3_t01_mem1 += MAS_MEM[7]

	c_t3_t3_t4 = S.Task('c_t3_t3_t4', length=11, delay_cost=1)
	S += c_t3_t3_t4 >= 31
	c_t3_t3_t4 += MM[0]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 31
	c_t4010_in += MAS_in[2]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 31
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 31
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4011 = S.Task('c_t4011', length=2, delay_cost=1)
	S += c_t4011 >= 31
	c_t4011 += MAS[0]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 32
	c_t1_t30_in += MAS_in[2]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 32
	c_t1_t30_mem0 += MM_MEM[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 32
	c_t1_t30_mem1 += MM_MEM[3]

	c_t1_t3_t5 = S.Task('c_t1_t3_t5', length=2, delay_cost=1)
	S += c_t1_t3_t5 >= 32
	c_t1_t3_t5 += MAS[0]

	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	S += c_t3_t00_in >= 32
	c_t3_t00_in += MAS_in[0]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 32
	c_t3_t00_mem0 += MAS_MEM[0]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 32
	c_t3_t00_mem1 += MAS_MEM[3]

	c_t3_t01 = S.Task('c_t3_t01', length=2, delay_cost=1)
	S += c_t3_t01 >= 32
	c_t3_t01 += MAS[3]

	c_t4010 = S.Task('c_t4010', length=2, delay_cost=1)
	S += c_t4010 >= 32
	c_t4010 += MAS[2]

	c_t4_t11_in = S.Task('c_t4_t11_in', length=1, delay_cost=1)
	S += c_t4_t11_in >= 32
	c_t4_t11_in += MAS_in[1]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 32
	c_t4_t11_mem0 += MAS_MEM[2]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 32
	c_t4_t11_mem1 += MAS_MEM[1]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 32
	c_t5011_in += MAS_in[3]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 32
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 32
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t1_t30 = S.Task('c_t1_t30', length=2, delay_cost=1)
	S += c_t1_t30 >= 33
	c_t1_t30 += MAS[2]

	c_t3_t00 = S.Task('c_t3_t00', length=2, delay_cost=1)
	S += c_t3_t00 >= 33
	c_t3_t00 += MAS[0]

	c_t3_t2_t1_in = S.Task('c_t3_t2_t1_in', length=1, delay_cost=1)
	S += c_t3_t2_t1_in >= 33
	c_t3_t2_t1_in += MM_in[0]

	c_t3_t2_t1_mem0 = S.Task('c_t3_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t1_mem0 >= 33
	c_t3_t2_t1_mem0 += MAS_MEM[6]

	c_t3_t2_t1_mem1 = S.Task('c_t3_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t1_mem1 >= 33
	c_t3_t2_t1_mem1 += MAS_MEM[7]

	c_t4_a1_1_in = S.Task('c_t4_a1_1_in', length=1, delay_cost=1)
	S += c_t4_a1_1_in >= 33
	c_t4_a1_1_in += MAS_in[2]

	c_t4_a1_1_mem0 = S.Task('c_t4_a1_1_mem0', length=1, delay_cost=1)
	S += c_t4_a1_1_mem0 >= 33
	c_t4_a1_1_mem0 += MAS_MEM[0]

	c_t4_a1_1_mem1 = S.Task('c_t4_a1_1_mem1', length=1, delay_cost=1)
	S += c_t4_a1_1_mem1 >= 33
	c_t4_a1_1_mem1 += MAS_MEM[5]

	c_t4_t11 = S.Task('c_t4_t11', length=2, delay_cost=1)
	S += c_t4_t11 >= 33
	c_t4_t11 += MAS[1]

	c_t4_t3_t1_in = S.Task('c_t4_t3_t1_in', length=1, delay_cost=1)
	S += c_t4_t3_t1_in >= 33
	c_t4_t3_t1_in += MM_in[1]

	c_t4_t3_t1_mem0 = S.Task('c_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem0 >= 33
	c_t4_t3_t1_mem0 += MAS_MEM[2]

	c_t4_t3_t1_mem1 = S.Task('c_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t1_mem1 >= 33
	c_t4_t3_t1_mem1 += MAS_MEM[1]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 33
	c_t5010_in += MAS_in[1]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 33
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 33
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5011 = S.Task('c_t5011', length=2, delay_cost=1)
	S += c_t5011 >= 33
	c_t5011 += MAS[3]

	c_t3_t2_t1 = S.Task('c_t3_t2_t1', length=11, delay_cost=1)
	S += c_t3_t2_t1 >= 34
	c_t3_t2_t1 += MM[0]

	c_t4_a1_1 = S.Task('c_t4_a1_1', length=2, delay_cost=1)
	S += c_t4_a1_1 >= 34
	c_t4_a1_1 += MAS[2]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 34
	c_t4_t10_in += MAS_in[3]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 34
	c_t4_t10_mem0 += MAS_MEM[0]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 34
	c_t4_t10_mem1 += MAS_MEM[5]

	c_t4_t3_t1 = S.Task('c_t4_t3_t1', length=11, delay_cost=1)
	S += c_t4_t3_t1 >= 34
	c_t4_t3_t1 += MM[1]

	c_t4_t3_t3_in = S.Task('c_t4_t3_t3_in', length=1, delay_cost=1)
	S += c_t4_t3_t3_in >= 34
	c_t4_t3_t3_in += MAS_in[2]

	c_t4_t3_t3_mem0 = S.Task('c_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem0 >= 34
	c_t4_t3_t3_mem0 += MAS_MEM[4]

	c_t4_t3_t3_mem1 = S.Task('c_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t3_mem1 >= 34
	c_t4_t3_t3_mem1 += MAS_MEM[1]

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
	c_t5010 += MAS[1]

	c_t4_a1_0_in = S.Task('c_t4_a1_0_in', length=1, delay_cost=1)
	S += c_t4_a1_0_in >= 35
	c_t4_a1_0_in += MAS_in[3]

	c_t4_a1_0_mem0 = S.Task('c_t4_a1_0_mem0', length=1, delay_cost=1)
	S += c_t4_a1_0_mem0 >= 35
	c_t4_a1_0_mem0 += MAS_MEM[4]

	c_t4_a1_0_mem1 = S.Task('c_t4_a1_0_mem1', length=1, delay_cost=1)
	S += c_t4_a1_0_mem1 >= 35
	c_t4_a1_0_mem1 += MAS_MEM[1]

	c_t4_t10 = S.Task('c_t4_t10', length=2, delay_cost=1)
	S += c_t4_t10 >= 35
	c_t4_t10 += MAS[3]

	c_t4_t3_t0_in = S.Task('c_t4_t3_t0_in', length=1, delay_cost=1)
	S += c_t4_t3_t0_in >= 35
	c_t4_t3_t0_in += MM_in[0]

	c_t4_t3_t0_mem0 = S.Task('c_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem0 >= 35
	c_t4_t3_t0_mem0 += MAS_MEM[0]

	c_t4_t3_t0_mem1 = S.Task('c_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t0_mem1 >= 35
	c_t4_t3_t0_mem1 += MAS_MEM[5]

	c_t4_t3_t3 = S.Task('c_t4_t3_t3', length=2, delay_cost=1)
	S += c_t4_t3_t3 >= 35
	c_t4_t3_t3 += MAS[2]

	c_t5000 = S.Task('c_t5000', length=2, delay_cost=1)
	S += c_t5000 >= 35
	c_t5000 += MAS[0]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 35
	c_t5001_in += MAS_in[1]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 35
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 35
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5_a1_0_in = S.Task('c_t5_a1_0_in', length=1, delay_cost=1)
	S += c_t5_a1_0_in >= 35
	c_t5_a1_0_in += MAS_in[2]

	c_t5_a1_0_mem0 = S.Task('c_t5_a1_0_mem0', length=1, delay_cost=1)
	S += c_t5_a1_0_mem0 >= 35
	c_t5_a1_0_mem0 += MAS_MEM[2]

	c_t5_a1_0_mem1 = S.Task('c_t5_a1_0_mem1', length=1, delay_cost=1)
	S += c_t5_a1_0_mem1 >= 35
	c_t5_a1_0_mem1 += MAS_MEM[7]

	c_t5_a1_1_in = S.Task('c_t5_a1_1_in', length=1, delay_cost=1)
	S += c_t5_a1_1_in >= 35
	c_t5_a1_1_in += MAS_in[0]

	c_t5_a1_1_mem0 = S.Task('c_t5_a1_1_mem0', length=1, delay_cost=1)
	S += c_t5_a1_1_mem0 >= 35
	c_t5_a1_1_mem0 += MAS_MEM[6]

	c_t5_a1_1_mem1 = S.Task('c_t5_a1_1_mem1', length=1, delay_cost=1)
	S += c_t5_a1_1_mem1 >= 35
	c_t5_a1_1_mem1 += MAS_MEM[3]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 36
	c_t0_t01_in += MAS_in[2]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 36
	c_t0_t01_mem0 += MAIN_MEM_r[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 36
	c_t0_t01_mem1 += MAS_MEM[1]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 36
	c_t2_t30_in += MAS_in[1]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 36
	c_t2_t30_mem0 += MM_MEM[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 36
	c_t2_t30_mem1 += MM_MEM[3]

	c_t4_a1_0 = S.Task('c_t4_a1_0', length=2, delay_cost=1)
	S += c_t4_a1_0 >= 36
	c_t4_a1_0 += MAS[3]

	c_t4_t3_t0 = S.Task('c_t4_t3_t0', length=11, delay_cost=1)
	S += c_t4_t3_t0 >= 36
	c_t4_t3_t0 += MM[0]

	c_t5001 = S.Task('c_t5001', length=2, delay_cost=1)
	S += c_t5001 >= 36
	c_t5001 += MAS[1]

	c_t5_a1_0 = S.Task('c_t5_a1_0', length=2, delay_cost=1)
	S += c_t5_a1_0 >= 36
	c_t5_a1_0 += MAS[2]

	c_t5_a1_1 = S.Task('c_t5_a1_1', length=2, delay_cost=1)
	S += c_t5_a1_1 >= 36
	c_t5_a1_1 += MAS[0]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 36
	c_t5_t10_in += MAS_in[3]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 36
	c_t5_t10_mem0 += MAS_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 36
	c_t5_t10_mem1 += MAS_MEM[3]

	c_t5_t3_t3_in = S.Task('c_t5_t3_t3_in', length=1, delay_cost=1)
	S += c_t5_t3_t3_in >= 36
	c_t5_t3_t3_in += MAS_in[0]

	c_t5_t3_t3_mem0 = S.Task('c_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem0 >= 36
	c_t5_t3_t3_mem0 += MAS_MEM[2]

	c_t5_t3_t3_mem1 = S.Task('c_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t3_mem1 >= 36
	c_t5_t3_t3_mem1 += MAS_MEM[7]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 37
	c_t0_t00_in += MAS_in[2]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 37
	c_t0_t00_mem0 += MAIN_MEM_r[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 37
	c_t0_t00_mem1 += MAS_MEM[1]

	c_t0_t01 = S.Task('c_t0_t01', length=2, delay_cost=1)
	S += c_t0_t01 >= 37
	c_t0_t01 += MAS[2]

	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	S += c_t110_in >= 37
	c_t110_in += MAS_in[3]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 37
	c_t110_mem0 += MAS_MEM[4]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 37
	c_t110_mem1 += MAS_MEM[5]

	c_t2_t30 = S.Task('c_t2_t30', length=2, delay_cost=1)
	S += c_t2_t30 >= 37
	c_t2_t30 += MAS[1]

	c_t2_t3_t5_in = S.Task('c_t2_t3_t5_in', length=1, delay_cost=1)
	S += c_t2_t3_t5_in >= 37
	c_t2_t3_t5_in += MAS_in[0]

	c_t2_t3_t5_mem0 = S.Task('c_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem0 >= 37
	c_t2_t3_t5_mem0 += MM_MEM[0]

	c_t2_t3_t5_mem1 = S.Task('c_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t3_t5_mem1 >= 37
	c_t2_t3_t5_mem1 += MM_MEM[3]

	c_t5_t10 = S.Task('c_t5_t10', length=2, delay_cost=1)
	S += c_t5_t10 >= 37
	c_t5_t10 += MAS[3]

	c_t5_t11_in = S.Task('c_t5_t11_in', length=1, delay_cost=1)
	S += c_t5_t11_in >= 37
	c_t5_t11_in += MAS_in[1]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 37
	c_t5_t11_mem0 += MAS_MEM[2]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 37
	c_t5_t11_mem1 += MAS_MEM[7]

	c_t5_t3_t0_in = S.Task('c_t5_t3_t0_in', length=1, delay_cost=1)
	S += c_t5_t3_t0_in >= 37
	c_t5_t3_t0_in += MM_in[1]

	c_t5_t3_t0_mem0 = S.Task('c_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem0 >= 37
	c_t5_t3_t0_mem0 += MAS_MEM[0]

	c_t5_t3_t0_mem1 = S.Task('c_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t0_mem1 >= 37
	c_t5_t3_t0_mem1 += MAS_MEM[3]

	c_t5_t3_t3 = S.Task('c_t5_t3_t3', length=2, delay_cost=1)
	S += c_t5_t3_t3 >= 37
	c_t5_t3_t3 += MAS[0]

	c_t0_t00 = S.Task('c_t0_t00', length=2, delay_cost=1)
	S += c_t0_t00 >= 38
	c_t0_t00 += MAS[2]

	c_t110 = S.Task('c_t110', length=2, delay_cost=1)
	S += c_t110 >= 38
	c_t110 += MAS[3]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 38
	c_t1_t00_in += MAS_in[2]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 38
	c_t1_t00_mem0 += MAIN_MEM_r[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 38
	c_t1_t00_mem1 += MAS_MEM[1]

	c_t2_t3_t5 = S.Task('c_t2_t3_t5', length=2, delay_cost=1)
	S += c_t2_t3_t5 >= 38
	c_t2_t3_t5 += MAS[0]

	c_t3_t3_t5_in = S.Task('c_t3_t3_t5_in', length=1, delay_cost=1)
	S += c_t3_t3_t5_in >= 38
	c_t3_t3_t5_in += MAS_in[0]

	c_t3_t3_t5_mem0 = S.Task('c_t3_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t3_t5_mem0 >= 38
	c_t3_t3_t5_mem0 += MM_MEM[2]

	c_t3_t3_t5_mem1 = S.Task('c_t3_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t3_t5_mem1 >= 38
	c_t3_t3_t5_mem1 += MM_MEM[1]

	c_t5_t11 = S.Task('c_t5_t11', length=2, delay_cost=1)
	S += c_t5_t11 >= 38
	c_t5_t11 += MAS[1]

	c_t5_t3_t0 = S.Task('c_t5_t3_t0', length=11, delay_cost=1)
	S += c_t5_t3_t0 >= 38
	c_t5_t3_t0 += MM[1]

	c_t5_t3_t1_in = S.Task('c_t5_t3_t1_in', length=1, delay_cost=1)
	S += c_t5_t3_t1_in >= 38
	c_t5_t3_t1_in += MM_in[1]

	c_t5_t3_t1_mem0 = S.Task('c_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem0 >= 38
	c_t5_t3_t1_mem0 += MAS_MEM[2]

	c_t5_t3_t1_mem1 = S.Task('c_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t1_mem1 >= 38
	c_t5_t3_t1_mem1 += MAS_MEM[7]

	c_t5_t3_t2_in = S.Task('c_t5_t3_t2_in', length=1, delay_cost=1)
	S += c_t5_t3_t2_in >= 38
	c_t5_t3_t2_in += MAS_in[1]

	c_t5_t3_t2_mem0 = S.Task('c_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem0 >= 38
	c_t5_t3_t2_mem0 += MAS_MEM[0]

	c_t5_t3_t2_mem1 = S.Task('c_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t2_mem1 >= 38
	c_t5_t3_t2_mem1 += MAS_MEM[3]

	c_t0_t2_t0_in = S.Task('c_t0_t2_t0_in', length=1, delay_cost=1)
	S += c_t0_t2_t0_in >= 39
	c_t0_t2_t0_in += MM_in[1]

	c_t0_t2_t0_mem0 = S.Task('c_t0_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t0_mem0 >= 39
	c_t0_t2_t0_mem0 += MAS_MEM[4]

	c_t0_t2_t0_mem1 = S.Task('c_t0_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t0_mem1 >= 39
	c_t0_t2_t0_mem1 += MAS_MEM[1]

	c_t1_t00 = S.Task('c_t1_t00', length=2, delay_cost=1)
	S += c_t1_t00 >= 39
	c_t1_t00 += MAS[2]

	c_t210_in = S.Task('c_t210_in', length=1, delay_cost=1)
	S += c_t210_in >= 39
	c_t210_in += MAS_in[1]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 39
	c_t210_mem0 += MAS_MEM[2]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 39
	c_t210_mem1 += MAS_MEM[3]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 39
	c_t2_t01_in += MAS_in[0]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 39
	c_t2_t01_mem0 += MAIN_MEM_r[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 39
	c_t2_t01_mem1 += MAS_MEM[7]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 39
	c_t3_t30_in += MAS_in[2]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 39
	c_t3_t30_mem0 += MM_MEM[2]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 39
	c_t3_t30_mem1 += MM_MEM[1]

	c_t3_t3_t5 = S.Task('c_t3_t3_t5', length=2, delay_cost=1)
	S += c_t3_t3_t5 >= 39
	c_t3_t3_t5 += MAS[0]

	c_t4_t3_t4_in = S.Task('c_t4_t3_t4_in', length=1, delay_cost=1)
	S += c_t4_t3_t4_in >= 39
	c_t4_t3_t4_in += MM_in[0]

	c_t4_t3_t4_mem0 = S.Task('c_t4_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t4_mem0 >= 39
	c_t4_t3_t4_mem0 += MAS_MEM[0]

	c_t4_t3_t4_mem1 = S.Task('c_t4_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t4_mem1 >= 39
	c_t4_t3_t4_mem1 += MAS_MEM[5]

	c_t5_t3_t1 = S.Task('c_t5_t3_t1', length=11, delay_cost=1)
	S += c_t5_t3_t1 >= 39
	c_t5_t3_t1 += MM[1]

	c_t5_t3_t2 = S.Task('c_t5_t3_t2', length=2, delay_cost=1)
	S += c_t5_t3_t2 >= 39
	c_t5_t3_t2 += MAS[1]

	c_t0_t2_t0 = S.Task('c_t0_t2_t0', length=11, delay_cost=1)
	S += c_t0_t2_t0 >= 40
	c_t0_t2_t0 += MM[1]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 40
	c_t0_t30_in += MAS_in[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 40
	c_t0_t30_mem0 += MM_MEM[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 40
	c_t0_t30_mem1 += MM_MEM[3]

	c_t1_t2_t0_in = S.Task('c_t1_t2_t0_in', length=1, delay_cost=1)
	S += c_t1_t2_t0_in >= 40
	c_t1_t2_t0_in += MM_in[0]

	c_t1_t2_t0_mem0 = S.Task('c_t1_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t0_mem0 >= 40
	c_t1_t2_t0_mem0 += MAS_MEM[4]

	c_t1_t2_t0_mem1 = S.Task('c_t1_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t0_mem1 >= 40
	c_t1_t2_t0_mem1 += MAS_MEM[5]

	c_t210 = S.Task('c_t210', length=2, delay_cost=1)
	S += c_t210 >= 40
	c_t210 += MAS[1]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 40
	c_t2_t00_in += MAS_in[1]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 40
	c_t2_t00_mem0 += MAIN_MEM_r[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 40
	c_t2_t00_mem1 += MAS_MEM[1]

	c_t2_t01 = S.Task('c_t2_t01', length=2, delay_cost=1)
	S += c_t2_t01 >= 40
	c_t2_t01 += MAS[0]

	c_t3_t30 = S.Task('c_t3_t30', length=2, delay_cost=1)
	S += c_t3_t30 >= 40
	c_t3_t30 += MAS[2]

	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	S += c_t4_t00_in >= 40
	c_t4_t00_in += MAS_in[3]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 40
	c_t4_t00_mem0 += MAS_MEM[0]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 40
	c_t4_t00_mem1 += MAS_MEM[7]

	c_t4_t2_t3_in = S.Task('c_t4_t2_t3_in', length=1, delay_cost=1)
	S += c_t4_t2_t3_in >= 40
	c_t4_t2_t3_in += MAS_in[2]

	c_t4_t2_t3_mem0 = S.Task('c_t4_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t3_mem0 >= 40
	c_t4_t2_t3_mem0 += MAS_MEM[6]

	c_t4_t2_t3_mem1 = S.Task('c_t4_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t3_mem1 >= 40
	c_t4_t2_t3_mem1 += MAS_MEM[3]

	c_t4_t3_t4 = S.Task('c_t4_t3_t4', length=11, delay_cost=1)
	S += c_t4_t3_t4 >= 40
	c_t4_t3_t4 += MM[0]

	c_t0_t30 = S.Task('c_t0_t30', length=2, delay_cost=1)
	S += c_t0_t30 >= 41
	c_t0_t30 += MAS[0]

	c_t0_t3_t5_in = S.Task('c_t0_t3_t5_in', length=1, delay_cost=1)
	S += c_t0_t3_t5_in >= 41
	c_t0_t3_t5_in += MAS_in[1]

	c_t0_t3_t5_mem0 = S.Task('c_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem0 >= 41
	c_t0_t3_t5_mem0 += MM_MEM[0]

	c_t0_t3_t5_mem1 = S.Task('c_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t3_t5_mem1 >= 41
	c_t0_t3_t5_mem1 += MM_MEM[3]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 41
	c_t1_t01_in += MAS_in[0]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 41
	c_t1_t01_mem0 += MAIN_MEM_r[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 41
	c_t1_t01_mem1 += MAS_MEM[3]

	c_t1_t2_t0 = S.Task('c_t1_t2_t0', length=11, delay_cost=1)
	S += c_t1_t2_t0 >= 41
	c_t1_t2_t0 += MM[0]

	c_t2_t00 = S.Task('c_t2_t00', length=2, delay_cost=1)
	S += c_t2_t00 >= 41
	c_t2_t00 += MAS[1]

	c_t2_t2_t1_in = S.Task('c_t2_t2_t1_in', length=1, delay_cost=1)
	S += c_t2_t2_t1_in >= 41
	c_t2_t2_t1_in += MM_in[1]

	c_t2_t2_t1_mem0 = S.Task('c_t2_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t1_mem0 >= 41
	c_t2_t2_t1_mem0 += MAS_MEM[0]

	c_t2_t2_t1_mem1 = S.Task('c_t2_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t1_mem1 >= 41
	c_t2_t2_t1_mem1 += MAS_MEM[5]

	c_t4_t00 = S.Task('c_t4_t00', length=2, delay_cost=1)
	S += c_t4_t00 >= 41
	c_t4_t00 += MAS[3]

	c_t4_t2_t3 = S.Task('c_t4_t2_t3', length=2, delay_cost=1)
	S += c_t4_t2_t3 >= 41
	c_t4_t2_t3 += MAS[2]

	c_t5_t01_in = S.Task('c_t5_t01_in', length=1, delay_cost=1)
	S += c_t5_t01_in >= 41
	c_t5_t01_in += MAS_in[2]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 41
	c_t5_t01_mem0 += MAS_MEM[2]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 41
	c_t5_t01_mem1 += MAS_MEM[1]

	c_t0_t3_t5 = S.Task('c_t0_t3_t5', length=2, delay_cost=1)
	S += c_t0_t3_t5 >= 42
	c_t0_t3_t5 += MAS[1]

	c_t1_t01 = S.Task('c_t1_t01', length=2, delay_cost=1)
	S += c_t1_t01 >= 42
	c_t1_t01 += MAS[0]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 42
	c_t1_t31_in += MAS_in[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 42
	c_t1_t31_mem0 += MM_MEM[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 42
	c_t1_t31_mem1 += MAS_MEM[1]

	c_t2_t2_t1 = S.Task('c_t2_t2_t1', length=11, delay_cost=1)
	S += c_t2_t2_t1 >= 42
	c_t2_t2_t1 += MM[1]

	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	S += c_t5_t00_in >= 42
	c_t5_t00_in += MAS_in[0]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 42
	c_t5_t00_mem0 += MAS_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 42
	c_t5_t00_mem1 += MAS_MEM[5]

	c_t5_t01 = S.Task('c_t5_t01', length=2, delay_cost=1)
	S += c_t5_t01 >= 42
	c_t5_t01 += MAS[2]

	c_t5_t2_t3_in = S.Task('c_t5_t2_t3_in', length=1, delay_cost=1)
	S += c_t5_t2_t3_in >= 42
	c_t5_t2_t3_in += MAS_in[2]

	c_t5_t2_t3_mem0 = S.Task('c_t5_t2_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t3_mem0 >= 42
	c_t5_t2_t3_mem0 += MAS_MEM[6]

	c_t5_t2_t3_mem1 = S.Task('c_t5_t2_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t3_mem1 >= 42
	c_t5_t2_t3_mem1 += MAS_MEM[3]

	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	S += c_t010_in >= 43
	c_t010_in += MAS_in[3]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 43
	c_t010_mem0 += MAS_MEM[0]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 43
	c_t010_mem1 += MAS_MEM[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 43
	c_t0_t31_in += MAS_in[2]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 43
	c_t0_t31_mem0 += MM_MEM[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 43
	c_t0_t31_mem1 += MAS_MEM[3]

	c_t1_t31 = S.Task('c_t1_t31', length=2, delay_cost=1)
	S += c_t1_t31 >= 43
	c_t1_t31 += MAS[1]

	c_t2_t2_t0_in = S.Task('c_t2_t2_t0_in', length=1, delay_cost=1)
	S += c_t2_t2_t0_in >= 43
	c_t2_t2_t0_in += MM_in[1]

	c_t2_t2_t0_mem0 = S.Task('c_t2_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t0_mem0 >= 43
	c_t2_t2_t0_mem0 += MAS_MEM[2]

	c_t2_t2_t0_mem1 = S.Task('c_t2_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t0_mem1 >= 43
	c_t2_t2_t0_mem1 += MAS_MEM[5]

	c_t4_t2_t0_in = S.Task('c_t4_t2_t0_in', length=1, delay_cost=1)
	S += c_t4_t2_t0_in >= 43
	c_t4_t2_t0_in += MM_in[0]

	c_t4_t2_t0_mem0 = S.Task('c_t4_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t0_mem0 >= 43
	c_t4_t2_t0_mem0 += MAS_MEM[6]

	c_t4_t2_t0_mem1 = S.Task('c_t4_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t0_mem1 >= 43
	c_t4_t2_t0_mem1 += MAS_MEM[7]

	c_t5_t00 = S.Task('c_t5_t00', length=2, delay_cost=1)
	S += c_t5_t00 >= 43
	c_t5_t00 += MAS[0]

	c_t5_t2_t3 = S.Task('c_t5_t2_t3', length=2, delay_cost=1)
	S += c_t5_t2_t3 >= 43
	c_t5_t2_t3 += MAS[2]

	c_s1010_in = S.Task('c_s1010_in', length=1, delay_cost=1)
	S += c_s1010_in >= 44
	c_s1010_in += MAS_in[1]

	c_s1010_mem0 = S.Task('c_s1010_mem0', length=1, delay_cost=1)
	S += c_s1010_mem0 >= 44
	c_s1010_mem0 += MAS_MEM[6]

	c_s1010_mem1 = S.Task('c_s1010_mem1', length=1, delay_cost=1)
	S += c_s1010_mem1 >= 44
	c_s1010_mem1 += MAS_MEM[3]

	c_t010 = S.Task('c_t010', length=2, delay_cost=1)
	S += c_t010 >= 44
	c_t010 += MAS[3]

	c_t0_t31 = S.Task('c_t0_t31', length=2, delay_cost=1)
	S += c_t0_t31 >= 44
	c_t0_t31 += MAS[2]

	c_t1_t2_t2_in = S.Task('c_t1_t2_t2_in', length=1, delay_cost=1)
	S += c_t1_t2_t2_in >= 44
	c_t1_t2_t2_in += MAS_in[3]

	c_t1_t2_t2_mem0 = S.Task('c_t1_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t2_mem0 >= 44
	c_t1_t2_t2_mem0 += MAS_MEM[4]

	c_t1_t2_t2_mem1 = S.Task('c_t1_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t2_mem1 >= 44
	c_t1_t2_t2_mem1 += MAS_MEM[1]

	c_t2_t2_t0 = S.Task('c_t2_t2_t0', length=11, delay_cost=1)
	S += c_t2_t2_t0 >= 44
	c_t2_t2_t0 += MM[1]

	c_t4_t01_in = S.Task('c_t4_t01_in', length=1, delay_cost=1)
	S += c_t4_t01_in >= 44
	c_t4_t01_in += MAS_in[2]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 44
	c_t4_t01_mem0 += MAS_MEM[2]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 44
	c_t4_t01_mem1 += MAS_MEM[5]

	c_t4_t2_t0 = S.Task('c_t4_t2_t0', length=11, delay_cost=1)
	S += c_t4_t2_t0 >= 44
	c_t4_t2_t0 += MM[0]

	c_t5_t2_t0_in = S.Task('c_t5_t2_t0_in', length=1, delay_cost=1)
	S += c_t5_t2_t0_in >= 44
	c_t5_t2_t0_in += MM_in[0]

	c_t5_t2_t0_mem0 = S.Task('c_t5_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t0_mem0 >= 44
	c_t5_t2_t0_mem0 += MAS_MEM[0]

	c_t5_t2_t0_mem1 = S.Task('c_t5_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t0_mem1 >= 44
	c_t5_t2_t0_mem1 += MAS_MEM[7]

	c_s0010_in = S.Task('c_s0010_in', length=1, delay_cost=1)
	S += c_s0010_in >= 45
	c_s0010_in += MAS_in[1]

	c_s0010_mem0 = S.Task('c_s0010_mem0', length=1, delay_cost=1)
	S += c_s0010_mem0 >= 45
	c_s0010_mem0 += MAS_MEM[6]

	c_s0010_mem1 = S.Task('c_s0010_mem1', length=1, delay_cost=1)
	S += c_s0010_mem1 >= 45
	c_s0010_mem1 += MAS_MEM[7]

	c_s1010 = S.Task('c_s1010', length=2, delay_cost=1)
	S += c_s1010 >= 45
	c_s1010 += MAS[1]

	c_t0_t2_t2_in = S.Task('c_t0_t2_t2_in', length=1, delay_cost=1)
	S += c_t0_t2_t2_in >= 45
	c_t0_t2_t2_in += MAS_in[3]

	c_t0_t2_t2_mem0 = S.Task('c_t0_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t2_mem0 >= 45
	c_t0_t2_t2_mem0 += MAS_MEM[4]

	c_t0_t2_t2_mem1 = S.Task('c_t0_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t2_mem1 >= 45
	c_t0_t2_t2_mem1 += MAS_MEM[5]

	c_t1_t2_t2 = S.Task('c_t1_t2_t2', length=2, delay_cost=1)
	S += c_t1_t2_t2 >= 45
	c_t1_t2_t2 += MAS[3]

	c_t2_t2_t2_in = S.Task('c_t2_t2_t2_in', length=1, delay_cost=1)
	S += c_t2_t2_t2_in >= 45
	c_t2_t2_t2_in += MAS_in[2]

	c_t2_t2_t2_mem0 = S.Task('c_t2_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t2_mem0 >= 45
	c_t2_t2_t2_mem0 += MAS_MEM[2]

	c_t2_t2_t2_mem1 = S.Task('c_t2_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t2_mem1 >= 45
	c_t2_t2_t2_mem1 += MAS_MEM[1]

	c_t3_t2_t0_in = S.Task('c_t3_t2_t0_in', length=1, delay_cost=1)
	S += c_t3_t2_t0_in >= 45
	c_t3_t2_t0_in += MM_in[0]

	c_t3_t2_t0_mem0 = S.Task('c_t3_t2_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t0_mem0 >= 45
	c_t3_t2_t0_mem0 += MAS_MEM[0]

	c_t3_t2_t0_mem1 = S.Task('c_t3_t2_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t0_mem1 >= 45
	c_t3_t2_t0_mem1 += MAS_MEM[3]

	c_t4_t01 = S.Task('c_t4_t01', length=2, delay_cost=1)
	S += c_t4_t01 >= 45
	c_t4_t01 += MAS[2]

	c_t5_t2_t0 = S.Task('c_t5_t2_t0', length=11, delay_cost=1)
	S += c_t5_t2_t0 >= 45
	c_t5_t2_t0 += MM[0]

	c_s0010 = S.Task('c_s0010', length=2, delay_cost=1)
	S += c_s0010 >= 46
	c_s0010 += MAS[1]

	c_t0_t2_t2 = S.Task('c_t0_t2_t2', length=2, delay_cost=1)
	S += c_t0_t2_t2 >= 46
	c_t0_t2_t2 += MAS[3]

	c_t2_t2_t2 = S.Task('c_t2_t2_t2', length=2, delay_cost=1)
	S += c_t2_t2_t2 >= 46
	c_t2_t2_t2 += MAS[2]

	c_t3_t2_t0 = S.Task('c_t3_t2_t0', length=11, delay_cost=1)
	S += c_t3_t2_t0 >= 46
	c_t3_t2_t0 += MM[0]

	c_t3_t2_t2_in = S.Task('c_t3_t2_t2_in', length=1, delay_cost=1)
	S += c_t3_t2_t2_in >= 46
	c_t3_t2_t2_in += MAS_in[1]

	c_t3_t2_t2_mem0 = S.Task('c_t3_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t2_mem0 >= 46
	c_t3_t2_t2_mem0 += MAS_MEM[0]

	c_t3_t2_t2_mem1 = S.Task('c_t3_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t2_mem1 >= 46
	c_t3_t2_t2_mem1 += MAS_MEM[7]

	c_t4_t2_t1_in = S.Task('c_t4_t2_t1_in', length=1, delay_cost=1)
	S += c_t4_t2_t1_in >= 46
	c_t4_t2_t1_in += MM_in[1]

	c_t4_t2_t1_mem0 = S.Task('c_t4_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t1_mem0 >= 46
	c_t4_t2_t1_mem0 += MAS_MEM[4]

	c_t4_t2_t1_mem1 = S.Task('c_t4_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t1_mem1 >= 46
	c_t4_t2_t1_mem1 += MAS_MEM[3]

	c_t4_t2_t2_in = S.Task('c_t4_t2_t2_in', length=1, delay_cost=1)
	S += c_t4_t2_t2_in >= 46
	c_t4_t2_t2_in += MAS_in[0]

	c_t4_t2_t2_mem0 = S.Task('c_t4_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t2_mem0 >= 46
	c_t4_t2_t2_mem0 += MAS_MEM[6]

	c_t4_t2_t2_mem1 = S.Task('c_t4_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t2_mem1 >= 46
	c_t4_t2_t2_mem1 += MAS_MEM[5]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 46
	c_t4_t30_in += MAS_in[2]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 46
	c_t4_t30_mem0 += MM_MEM[0]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 46
	c_t4_t30_mem1 += MM_MEM[3]

	c_t5_t3_t4_in = S.Task('c_t5_t3_t4_in', length=1, delay_cost=1)
	S += c_t5_t3_t4_in >= 46
	c_t5_t3_t4_in += MM_in[0]

	c_t5_t3_t4_mem0 = S.Task('c_t5_t3_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t4_mem0 >= 46
	c_t5_t3_t4_mem0 += MAS_MEM[2]

	c_t5_t3_t4_mem1 = S.Task('c_t5_t3_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t4_mem1 >= 46
	c_t5_t3_t4_mem1 += MAS_MEM[1]

	c_s2010_in = S.Task('c_s2010_in', length=1, delay_cost=1)
	S += c_s2010_in >= 47
	c_s2010_in += MAS_in[1]

	c_s2010_mem0 = S.Task('c_s2010_mem0', length=1, delay_cost=1)
	S += c_s2010_mem0 >= 47
	c_s2010_mem0 += MAS_MEM[2]

	c_s2010_mem1 = S.Task('c_s2010_mem1', length=1, delay_cost=1)
	S += c_s2010_mem1 >= 47
	c_s2010_mem1 += MAS_MEM[7]

	c_t0_t2_t4_in = S.Task('c_t0_t2_t4_in', length=1, delay_cost=1)
	S += c_t0_t2_t4_in >= 47
	c_t0_t2_t4_in += MM_in[1]

	c_t0_t2_t4_mem0 = S.Task('c_t0_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t4_mem0 >= 47
	c_t0_t2_t4_mem0 += MAS_MEM[6]

	c_t0_t2_t4_mem1 = S.Task('c_t0_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t4_mem1 >= 47
	c_t0_t2_t4_mem1 += MAS_MEM[5]

	c_t1_t2_t1_in = S.Task('c_t1_t2_t1_in', length=1, delay_cost=1)
	S += c_t1_t2_t1_in >= 47
	c_t1_t2_t1_in += MM_in[0]

	c_t1_t2_t1_mem0 = S.Task('c_t1_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t1_mem0 >= 47
	c_t1_t2_t1_mem0 += MAS_MEM[0]

	c_t1_t2_t1_mem1 = S.Task('c_t1_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t1_mem1 >= 47
	c_t1_t2_t1_mem1 += MAS_MEM[1]

	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	S += c_t1_t40_in >= 47
	c_t1_t40_in += MAS_in[2]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 47
	c_t1_t40_mem0 += MAS_MEM[4]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 47
	c_t1_t40_mem1 += MAS_MEM[3]

	c_t3_t2_t2 = S.Task('c_t3_t2_t2', length=2, delay_cost=1)
	S += c_t3_t2_t2 >= 47
	c_t3_t2_t2 += MAS[1]

	c_t4_t2_t1 = S.Task('c_t4_t2_t1', length=11, delay_cost=1)
	S += c_t4_t2_t1 >= 47
	c_t4_t2_t1 += MM[1]

	c_t4_t2_t2 = S.Task('c_t4_t2_t2', length=2, delay_cost=1)
	S += c_t4_t2_t2 >= 47
	c_t4_t2_t2 += MAS[0]

	c_t4_t30 = S.Task('c_t4_t30', length=2, delay_cost=1)
	S += c_t4_t30 >= 47
	c_t4_t30 += MAS[2]

	c_t4_t3_t5_in = S.Task('c_t4_t3_t5_in', length=1, delay_cost=1)
	S += c_t4_t3_t5_in >= 47
	c_t4_t3_t5_in += MAS_in[0]

	c_t4_t3_t5_mem0 = S.Task('c_t4_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t3_t5_mem0 >= 47
	c_t4_t3_t5_mem0 += MM_MEM[0]

	c_t4_t3_t5_mem1 = S.Task('c_t4_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t3_t5_mem1 >= 47
	c_t4_t3_t5_mem1 += MM_MEM[3]

	c_t5_t3_t4 = S.Task('c_t5_t3_t4', length=11, delay_cost=1)
	S += c_t5_t3_t4 >= 47
	c_t5_t3_t4 += MM[0]

	c_s2010 = S.Task('c_s2010', length=2, delay_cost=1)
	S += c_s2010 >= 48
	c_s2010 += MAS[1]

	c_t0_t2_t4 = S.Task('c_t0_t2_t4', length=11, delay_cost=1)
	S += c_t0_t2_t4 >= 48
	c_t0_t2_t4 += MM[1]

	c_t1_t2_t1 = S.Task('c_t1_t2_t1', length=11, delay_cost=1)
	S += c_t1_t2_t1 >= 48
	c_t1_t2_t1 += MM[0]

	c_t1_t2_t4_in = S.Task('c_t1_t2_t4_in', length=1, delay_cost=1)
	S += c_t1_t2_t4_in >= 48
	c_t1_t2_t4_in += MM_in[1]

	c_t1_t2_t4_mem0 = S.Task('c_t1_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t4_mem0 >= 48
	c_t1_t2_t4_mem0 += MAS_MEM[6]

	c_t1_t2_t4_mem1 = S.Task('c_t1_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t4_mem1 >= 48
	c_t1_t2_t4_mem1 += MAS_MEM[5]

	c_t1_t40 = S.Task('c_t1_t40', length=2, delay_cost=1)
	S += c_t1_t40 >= 48
	c_t1_t40 += MAS[2]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 48
	c_t2_t31_in += MAS_in[0]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 48
	c_t2_t31_mem0 += MM_MEM[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 48
	c_t2_t31_mem1 += MAS_MEM[1]

	c_t4_t3_t5 = S.Task('c_t4_t3_t5', length=2, delay_cost=1)
	S += c_t4_t3_t5 >= 48
	c_t4_t3_t5 += MAS[0]

	c_t5_t2_t1_in = S.Task('c_t5_t2_t1_in', length=1, delay_cost=1)
	S += c_t5_t2_t1_in >= 48
	c_t5_t2_t1_in += MM_in[0]

	c_t5_t2_t1_mem0 = S.Task('c_t5_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t1_mem0 >= 48
	c_t5_t2_t1_mem0 += MAS_MEM[4]

	c_t5_t2_t1_mem1 = S.Task('c_t5_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t1_mem1 >= 48
	c_t5_t2_t1_mem1 += MAS_MEM[3]

	c_t0_t2_t1_in = S.Task('c_t0_t2_t1_in', length=1, delay_cost=1)
	S += c_t0_t2_t1_in >= 49
	c_t0_t2_t1_in += MM_in[0]

	c_t0_t2_t1_mem0 = S.Task('c_t0_t2_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t1_mem0 >= 49
	c_t0_t2_t1_mem0 += MAS_MEM[4]

	c_t0_t2_t1_mem1 = S.Task('c_t0_t2_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t1_mem1 >= 49
	c_t0_t2_t1_mem1 += MAS_MEM[1]

	c_t111_in = S.Task('c_t111_in', length=1, delay_cost=1)
	S += c_t111_in >= 49
	c_t111_in += MAS_in[0]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 49
	c_t111_mem0 += MAS_MEM[2]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 49
	c_t111_mem1 += MAS_MEM[3]

	c_t1_t2_t4 = S.Task('c_t1_t2_t4', length=11, delay_cost=1)
	S += c_t1_t2_t4 >= 49
	c_t1_t2_t4 += MM[1]

	c_t2_t31 = S.Task('c_t2_t31', length=2, delay_cost=1)
	S += c_t2_t31 >= 49
	c_t2_t31 += MAS[0]

	c_t5_t2_t1 = S.Task('c_t5_t2_t1', length=11, delay_cost=1)
	S += c_t5_t2_t1 >= 49
	c_t5_t2_t1 += MM[0]

	c_t5_t2_t2_in = S.Task('c_t5_t2_t2_in', length=1, delay_cost=1)
	S += c_t5_t2_t2_in >= 49
	c_t5_t2_t2_in += MAS_in[1]

	c_t5_t2_t2_mem0 = S.Task('c_t5_t2_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t2_mem0 >= 49
	c_t5_t2_t2_mem0 += MAS_MEM[0]

	c_t5_t2_t2_mem1 = S.Task('c_t5_t2_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t2_mem1 >= 49
	c_t5_t2_t2_mem1 += MAS_MEM[5]

	c_t5_t3_t5_in = S.Task('c_t5_t3_t5_in', length=1, delay_cost=1)
	S += c_t5_t3_t5_in >= 49
	c_t5_t3_t5_in += MAS_in[2]

	c_t5_t3_t5_mem0 = S.Task('c_t5_t3_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t3_t5_mem0 >= 49
	c_t5_t3_t5_mem0 += MM_MEM[2]

	c_t5_t3_t5_mem1 = S.Task('c_t5_t3_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t3_t5_mem1 >= 49
	c_t5_t3_t5_mem1 += MM_MEM[3]

	c_t0_t2_t1 = S.Task('c_t0_t2_t1', length=11, delay_cost=1)
	S += c_t0_t2_t1 >= 50
	c_t0_t2_t1 += MM[0]

	c_t111 = S.Task('c_t111', length=2, delay_cost=1)
	S += c_t111 >= 50
	c_t111 += MAS[0]

	c_t2_t41_in = S.Task('c_t2_t41_in', length=1, delay_cost=1)
	S += c_t2_t41_in >= 50
	c_t2_t41_in += MAS_in[2]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 50
	c_t2_t41_mem0 += MAS_MEM[0]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 50
	c_t2_t41_mem1 += MAS_MEM[3]

	c_t310_in = S.Task('c_t310_in', length=1, delay_cost=1)
	S += c_t310_in >= 50
	c_t310_in += MAS_in[1]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 50
	c_t310_mem0 += MAS_MEM[4]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 50
	c_t310_mem1 += MAS_MEM[5]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 50
	c_t3_t31_in += MAS_in[3]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 50
	c_t3_t31_mem0 += MM_MEM[0]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 50
	c_t3_t31_mem1 += MAS_MEM[1]

	c_t5_t2_t2 = S.Task('c_t5_t2_t2', length=2, delay_cost=1)
	S += c_t5_t2_t2 >= 50
	c_t5_t2_t2 += MAS[1]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 50
	c_t5_t30_in += MAS_in[0]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 50
	c_t5_t30_mem0 += MM_MEM[2]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 50
	c_t5_t30_mem1 += MM_MEM[3]

	c_t5_t3_t5 = S.Task('c_t5_t3_t5', length=2, delay_cost=1)
	S += c_t5_t3_t5 >= 50
	c_t5_t3_t5 += MAS[2]

	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	S += c_t0_t40_in >= 51
	c_t0_t40_in += MAS_in[2]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 51
	c_t0_t40_mem0 += MAS_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 51
	c_t0_t40_mem1 += MAS_MEM[5]

	c_t2_t41 = S.Task('c_t2_t41', length=2, delay_cost=1)
	S += c_t2_t41 >= 51
	c_t2_t41 += MAS[2]

	c_t310 = S.Task('c_t310', length=2, delay_cost=1)
	S += c_t310 >= 51
	c_t310 += MAS[1]

	c_t3_t31 = S.Task('c_t3_t31', length=2, delay_cost=1)
	S += c_t3_t31 >= 51
	c_t3_t31 += MAS[3]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 51
	c_t4_t31_in += MAS_in[0]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 51
	c_t4_t31_mem0 += MM_MEM[0]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 51
	c_t4_t31_mem1 += MAS_MEM[1]

	c_t5_t30 = S.Task('c_t5_t30', length=2, delay_cost=1)
	S += c_t5_t30 >= 51
	c_t5_t30 += MAS[0]

	c_t0_t40 = S.Task('c_t0_t40', length=2, delay_cost=1)
	S += c_t0_t40 >= 52
	c_t0_t40 += MAS[2]

	c_t0_t41_in = S.Task('c_t0_t41_in', length=1, delay_cost=1)
	S += c_t0_t41_in >= 52
	c_t0_t41_in += MAS_in[3]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 52
	c_t0_t41_mem0 += MAS_MEM[4]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 52
	c_t0_t41_mem1 += MAS_MEM[1]

	c_t1_t41_in = S.Task('c_t1_t41_in', length=1, delay_cost=1)
	S += c_t1_t41_in >= 52
	c_t1_t41_in += MAS_in[2]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 52
	c_t1_t41_mem0 += MAS_MEM[2]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 52
	c_t1_t41_mem1 += MAS_MEM[5]

	c_t311_in = S.Task('c_t311_in', length=1, delay_cost=1)
	S += c_t311_in >= 52
	c_t311_in += MAS_in[0]

	c_t311_mem0 = S.Task('c_t311_mem0', length=1, delay_cost=1)
	S += c_t311_mem0 >= 52
	c_t311_mem0 += MAS_MEM[6]

	c_t311_mem1 = S.Task('c_t311_mem1', length=1, delay_cost=1)
	S += c_t311_mem1 >= 52
	c_t311_mem1 += MAS_MEM[7]

	c_t4_t31 = S.Task('c_t4_t31', length=2, delay_cost=1)
	S += c_t4_t31 >= 52
	c_t4_t31 += MAS[0]

	c_s010_in = S.Task('c_s010_in', length=1, delay_cost=1)
	S += c_s010_in >= 53
	c_s010_in += MAS_in[0]

	c_s010_mem0 = S.Task('c_s010_mem0', length=1, delay_cost=1)
	S += c_s010_mem0 >= 53
	c_s010_mem0 += MAS_MEM[2]

	c_s010_mem1 = S.Task('c_s010_mem1', length=1, delay_cost=1)
	S += c_s010_mem1 >= 53
	c_s010_mem1 += MAS_MEM[3]

	c_t0_t41 = S.Task('c_t0_t41', length=2, delay_cost=1)
	S += c_t0_t41 >= 53
	c_t0_t41 += MAS[3]

	c_t1_t41 = S.Task('c_t1_t41', length=2, delay_cost=1)
	S += c_t1_t41 >= 53
	c_t1_t41 += MAS[2]

	c_t211_in = S.Task('c_t211_in', length=1, delay_cost=1)
	S += c_t211_in >= 53
	c_t211_in += MAS_in[1]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 53
	c_t211_mem0 += MAS_MEM[0]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 53
	c_t211_mem1 += MAS_MEM[1]

	c_t311 = S.Task('c_t311', length=2, delay_cost=1)
	S += c_t311 >= 53
	c_t311 += MAS[0]

	c_t410_in = S.Task('c_t410_in', length=1, delay_cost=1)
	S += c_t410_in >= 53
	c_t410_in += MAS_in[3]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	S += c_t410_mem0 >= 53
	c_t410_mem0 += MAS_MEM[4]

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	S += c_t410_mem1 >= 53
	c_t410_mem1 += MAS_MEM[5]

	c_s010 = S.Task('c_s010', length=2, delay_cost=1)
	S += c_s010 >= 54
	c_s010 += MAS[0]

	c_t011_in = S.Task('c_t011_in', length=1, delay_cost=1)
	S += c_t011_in >= 54
	c_t011_in += MAS_in[0]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 54
	c_t011_mem0 += MAS_MEM[4]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 54
	c_t011_mem1 += MAS_MEM[5]

	c_t211 = S.Task('c_t211', length=2, delay_cost=1)
	S += c_t211 >= 54
	c_t211 += MAS[1]

	c_t2_t2_t5_in = S.Task('c_t2_t2_t5_in', length=1, delay_cost=1)
	S += c_t2_t2_t5_in >= 54
	c_t2_t2_t5_in += MAS_in[3]

	c_t2_t2_t5_mem0 = S.Task('c_t2_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t5_mem0 >= 54
	c_t2_t2_t5_mem0 += MM_MEM[2]

	c_t2_t2_t5_mem1 = S.Task('c_t2_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t5_mem1 >= 54
	c_t2_t2_t5_mem1 += MM_MEM[3]

	c_t410 = S.Task('c_t410', length=2, delay_cost=1)
	S += c_t410 >= 54
	c_t410 += MAS[3]

	c_t510_in = S.Task('c_t510_in', length=1, delay_cost=1)
	S += c_t510_in >= 54
	c_t510_in += MAS_in[1]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	S += c_t510_mem0 >= 54
	c_t510_mem0 += MAS_MEM[0]

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	S += c_t510_mem1 >= 54
	c_t510_mem1 += MAS_MEM[1]

	c_t011 = S.Task('c_t011', length=2, delay_cost=1)
	S += c_t011 >= 55
	c_t011 += MAS[0]

	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	S += c_t0_t50_in >= 55
	c_t0_t50_in += MAS_in[3]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 55
	c_t0_t50_mem0 += MAS_MEM[0]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 55
	c_t0_t50_mem1 += MAS_MEM[5]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 55
	c_t2_t20_in += MAS_in[2]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 55
	c_t2_t20_mem0 += MM_MEM[2]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 55
	c_t2_t20_mem1 += MM_MEM[3]

	c_t2_t2_t4_in = S.Task('c_t2_t2_t4_in', length=1, delay_cost=1)
	S += c_t2_t2_t4_in >= 55
	c_t2_t2_t4_in += MM_in[0]

	c_t2_t2_t4_mem0 = S.Task('c_t2_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t2_t4_mem0 >= 55
	c_t2_t2_t4_mem0 += MAS_MEM[4]

	c_t2_t2_t4_mem1 = S.Task('c_t2_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t2_t4_mem1 >= 55
	c_t2_t2_t4_mem1 += MAS_MEM[1]

	c_t2_t2_t5 = S.Task('c_t2_t2_t5', length=2, delay_cost=1)
	S += c_t2_t2_t5 >= 55
	c_t2_t2_t5 += MAS[3]

	c_t510 = S.Task('c_t510', length=2, delay_cost=1)
	S += c_t510 >= 55
	c_t510 += MAS[1]

	c_t6_y1_0_in = S.Task('c_t6_y1_0_in', length=1, delay_cost=1)
	S += c_t6_y1_0_in >= 55
	c_t6_y1_0_in += MAS_in[1]

	c_t6_y1_0_mem0 = S.Task('c_t6_y1_0_mem0', length=1, delay_cost=1)
	S += c_t6_y1_0_mem0 >= 55
	c_t6_y1_0_mem0 += MAS_MEM[2]

	c_t6_y1_0_mem1 = S.Task('c_t6_y1_0_mem1', length=1, delay_cost=1)
	S += c_t6_y1_0_mem1 >= 55
	c_t6_y1_0_mem1 += MAS_MEM[3]

	c_s1110_in = S.Task('c_s1110_in', length=1, delay_cost=1)
	S += c_s1110_in >= 56
	c_s1110_in += MAS_in[3]

	c_s1110_mem0 = S.Task('c_s1110_mem0', length=1, delay_cost=1)
	S += c_s1110_mem0 >= 56
	c_s1110_mem0 += MAS_MEM[6]

	c_s1110_mem1 = S.Task('c_s1110_mem1', length=1, delay_cost=1)
	S += c_s1110_mem1 >= 56
	c_s1110_mem1 += MAS_MEM[3]

	c_t0_t50 = S.Task('c_t0_t50', length=2, delay_cost=1)
	S += c_t0_t50 >= 56
	c_t0_t50 += MAS[3]

	c_t2_t20 = S.Task('c_t2_t20', length=2, delay_cost=1)
	S += c_t2_t20 >= 56
	c_t2_t20 += MAS[2]

	c_t2_t2_t4 = S.Task('c_t2_t2_t4', length=11, delay_cost=1)
	S += c_t2_t2_t4 >= 56
	c_t2_t2_t4 += MM[0]

	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	S += c_t2_t40_in >= 56
	c_t2_t40_in += MAS_in[0]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 56
	c_t2_t40_mem0 += MAS_MEM[2]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 56
	c_t2_t40_mem1 += MAS_MEM[1]

	c_t3_t2_t5_in = S.Task('c_t3_t2_t5_in', length=1, delay_cost=1)
	S += c_t3_t2_t5_in >= 56
	c_t3_t2_t5_in += MAS_in[2]

	c_t3_t2_t5_mem0 = S.Task('c_t3_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t5_mem0 >= 56
	c_t3_t2_t5_mem0 += MM_MEM[0]

	c_t3_t2_t5_mem1 = S.Task('c_t3_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t5_mem1 >= 56
	c_t3_t2_t5_mem1 += MM_MEM[1]

	c_t3_t40_in = S.Task('c_t3_t40_in', length=1, delay_cost=1)
	S += c_t3_t40_in >= 56
	c_t3_t40_in += MAS_in[1]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	S += c_t3_t40_mem0 >= 56
	c_t3_t40_mem0 += MAS_MEM[4]

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	S += c_t3_t40_mem1 >= 56
	c_t3_t40_mem1 += MAS_MEM[7]

	c_t4_t2_t4_in = S.Task('c_t4_t2_t4_in', length=1, delay_cost=1)
	S += c_t4_t2_t4_in >= 56
	c_t4_t2_t4_in += MM_in[1]

	c_t4_t2_t4_mem0 = S.Task('c_t4_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t4_mem0 >= 56
	c_t4_t2_t4_mem0 += MAS_MEM[0]

	c_t4_t2_t4_mem1 = S.Task('c_t4_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t4_mem1 >= 56
	c_t4_t2_t4_mem1 += MAS_MEM[5]

	c_t6_y1_0 = S.Task('c_t6_y1_0', length=2, delay_cost=1)
	S += c_t6_y1_0 >= 56
	c_t6_y1_0 += MAS[1]

	c_s1110 = S.Task('c_s1110', length=2, delay_cost=1)
	S += c_s1110 >= 57
	c_s1110 += MAS[3]

	c_s210_in = S.Task('c_s210_in', length=1, delay_cost=1)
	S += c_s210_in >= 57
	c_s210_in += MAS_in[3]

	c_s210_mem0 = S.Task('c_s210_mem0', length=1, delay_cost=1)
	S += c_s210_mem0 >= 57
	c_s210_mem0 += MAS_MEM[2]

	c_s210_mem1 = S.Task('c_s210_mem1', length=1, delay_cost=1)
	S += c_s210_mem1 >= 57
	c_s210_mem1 += MAS_MEM[3]

	c_t0_t51_in = S.Task('c_t0_t51_in', length=1, delay_cost=1)
	S += c_t0_t51_in >= 57
	c_t0_t51_in += MAS_in[1]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	S += c_t0_t51_mem0 >= 57
	c_t0_t51_mem0 += MAS_MEM[4]

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	S += c_t0_t51_mem1 >= 57
	c_t0_t51_mem1 += MAS_MEM[7]

	c_t2_t40 = S.Task('c_t2_t40', length=2, delay_cost=1)
	S += c_t2_t40 >= 57
	c_t2_t40 += MAS[0]

	c_t3_t2_t5 = S.Task('c_t3_t2_t5', length=2, delay_cost=1)
	S += c_t3_t2_t5 >= 57
	c_t3_t2_t5 += MAS[2]

	c_t3_t40 = S.Task('c_t3_t40', length=2, delay_cost=1)
	S += c_t3_t40 >= 57
	c_t3_t40 += MAS[1]

	c_t411_in = S.Task('c_t411_in', length=1, delay_cost=1)
	S += c_t411_in >= 57
	c_t411_in += MAS_in[0]

	c_t411_mem0 = S.Task('c_t411_mem0', length=1, delay_cost=1)
	S += c_t411_mem0 >= 57
	c_t411_mem0 += MAS_MEM[0]

	c_t411_mem1 = S.Task('c_t411_mem1', length=1, delay_cost=1)
	S += c_t411_mem1 >= 57
	c_t411_mem1 += MAS_MEM[1]

	c_t4_t2_t4 = S.Task('c_t4_t2_t4', length=11, delay_cost=1)
	S += c_t4_t2_t4 >= 57
	c_t4_t2_t4 += MM[1]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 57
	c_t5_t31_in += MAS_in[2]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 57
	c_t5_t31_mem0 += MM_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 57
	c_t5_t31_mem1 += MAS_MEM[5]

	c_s210 = S.Task('c_s210', length=2, delay_cost=1)
	S += c_s210 >= 58
	c_s210 += MAS[3]

	c_t0_t51 = S.Task('c_t0_t51', length=2, delay_cost=1)
	S += c_t0_t51 >= 58
	c_t0_t51 += MAS[1]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 58
	c_t1_t20_in += MAS_in[3]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 58
	c_t1_t20_mem0 += MM_MEM[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 58
	c_t1_t20_mem1 += MM_MEM[1]

	c_t2_t51_in = S.Task('c_t2_t51_in', length=1, delay_cost=1)
	S += c_t2_t51_in >= 58
	c_t2_t51_in += MAS_in[1]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	S += c_t2_t51_mem0 >= 58
	c_t2_t51_mem0 += MAS_MEM[0]

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	S += c_t2_t51_mem1 >= 58
	c_t2_t51_mem1 += MAS_MEM[5]

	c_t411 = S.Task('c_t411', length=2, delay_cost=1)
	S += c_t411 >= 58
	c_t411 += MAS[0]

	c_t4_t40_in = S.Task('c_t4_t40_in', length=1, delay_cost=1)
	S += c_t4_t40_in >= 58
	c_t4_t40_in += MAS_in[0]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	S += c_t4_t40_mem0 >= 58
	c_t4_t40_mem0 += MAS_MEM[4]

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	S += c_t4_t40_mem1 >= 58
	c_t4_t40_mem1 += MAS_MEM[1]

	c_t5_t31 = S.Task('c_t5_t31', length=2, delay_cost=1)
	S += c_t5_t31 >= 58
	c_t5_t31 += MAS[2]

	c_t6_y1_1_in = S.Task('c_t6_y1_1_in', length=1, delay_cost=1)
	S += c_t6_y1_1_in >= 58
	c_t6_y1_1_in += MAS_in[2]

	c_t6_y1_1_mem0 = S.Task('c_t6_y1_1_mem0', length=1, delay_cost=1)
	S += c_t6_y1_1_mem0 >= 58
	c_t6_y1_1_mem0 += MAS_MEM[2]

	c_t6_y1_1_mem1 = S.Task('c_t6_y1_1_mem1', length=1, delay_cost=1)
	S += c_t6_y1_1_mem1 >= 58
	c_t6_y1_1_mem1 += MAS_MEM[3]

	c_s1011_in = S.Task('c_s1011_in', length=1, delay_cost=1)
	S += c_s1011_in >= 59
	c_s1011_in += MAS_in[3]

	c_s1011_mem0 = S.Task('c_s1011_mem0', length=1, delay_cost=1)
	S += c_s1011_mem0 >= 59
	c_s1011_mem0 += MAS_MEM[0]

	c_s1011_mem1 = S.Task('c_s1011_mem1', length=1, delay_cost=1)
	S += c_s1011_mem1 >= 59
	c_s1011_mem1 += MAS_MEM[3]

	c_t1_t20 = S.Task('c_t1_t20', length=2, delay_cost=1)
	S += c_t1_t20 >= 59
	c_t1_t20 += MAS[3]

	c_t1_t2_t5_in = S.Task('c_t1_t2_t5_in', length=1, delay_cost=1)
	S += c_t1_t2_t5_in >= 59
	c_t1_t2_t5_in += MAS_in[0]

	c_t1_t2_t5_mem0 = S.Task('c_t1_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t2_t5_mem0 >= 59
	c_t1_t2_t5_mem0 += MM_MEM[0]

	c_t1_t2_t5_mem1 = S.Task('c_t1_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t2_t5_mem1 >= 59
	c_t1_t2_t5_mem1 += MM_MEM[1]

	c_t2_t51 = S.Task('c_t2_t51', length=2, delay_cost=1)
	S += c_t2_t51 >= 59
	c_t2_t51 += MAS[1]

	c_t3_t2_t4_in = S.Task('c_t3_t2_t4_in', length=1, delay_cost=1)
	S += c_t3_t2_t4_in >= 59
	c_t3_t2_t4_in += MM_in[1]

	c_t3_t2_t4_mem0 = S.Task('c_t3_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t2_t4_mem0 >= 59
	c_t3_t2_t4_mem0 += MAS_MEM[2]

	c_t3_t2_t4_mem1 = S.Task('c_t3_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t2_t4_mem1 >= 59
	c_t3_t2_t4_mem1 += MAS_MEM[1]

	c_t3_t41_in = S.Task('c_t3_t41_in', length=1, delay_cost=1)
	S += c_t3_t41_in >= 59
	c_t3_t41_in += MAS_in[1]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	S += c_t3_t41_mem0 >= 59
	c_t3_t41_mem0 += MAS_MEM[6]

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	S += c_t3_t41_mem1 >= 59
	c_t3_t41_mem1 += MAS_MEM[5]

	c_t4_t40 = S.Task('c_t4_t40', length=2, delay_cost=1)
	S += c_t4_t40 >= 59
	c_t4_t40 += MAS[0]

	c_t6_y1_1 = S.Task('c_t6_y1_1', length=2, delay_cost=1)
	S += c_t6_y1_1 >= 59
	c_t6_y1_1 += MAS[2]

	c_s1011 = S.Task('c_s1011', length=2, delay_cost=1)
	S += c_s1011 >= 60
	c_s1011 += MAS[3]

	c_t0_t2_t5_in = S.Task('c_t0_t2_t5_in', length=1, delay_cost=1)
	S += c_t0_t2_t5_in >= 60
	c_t0_t2_t5_in += MAS_in[2]

	c_t0_t2_t5_mem0 = S.Task('c_t0_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t2_t5_mem0 >= 60
	c_t0_t2_t5_mem0 += MM_MEM[2]

	c_t0_t2_t5_mem1 = S.Task('c_t0_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t2_t5_mem1 >= 60
	c_t0_t2_t5_mem1 += MM_MEM[1]

	c_t1_t2_t5 = S.Task('c_t1_t2_t5', length=2, delay_cost=1)
	S += c_t1_t2_t5 >= 60
	c_t1_t2_t5 += MAS[0]

	c_t1_t51_in = S.Task('c_t1_t51_in', length=1, delay_cost=1)
	S += c_t1_t51_in >= 60
	c_t1_t51_in += MAS_in[3]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	S += c_t1_t51_mem0 >= 60
	c_t1_t51_mem0 += MAS_MEM[2]

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	S += c_t1_t51_mem1 >= 60
	c_t1_t51_mem1 += MAS_MEM[5]

	c_t3_t2_t4 = S.Task('c_t3_t2_t4', length=11, delay_cost=1)
	S += c_t3_t2_t4 >= 60
	c_t3_t2_t4 += MM[1]

	c_t3_t41 = S.Task('c_t3_t41', length=2, delay_cost=1)
	S += c_t3_t41 >= 60
	c_t3_t41 += MAS[1]

	c_t4_t2_t5_in = S.Task('c_t4_t2_t5_in', length=1, delay_cost=1)
	S += c_t4_t2_t5_in >= 60
	c_t4_t2_t5_in += MAS_in[0]

	c_t4_t2_t5_mem0 = S.Task('c_t4_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t2_t5_mem0 >= 60
	c_t4_t2_t5_mem0 += MM_MEM[0]

	c_t4_t2_t5_mem1 = S.Task('c_t4_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t2_t5_mem1 >= 60
	c_t4_t2_t5_mem1 += MM_MEM[3]

	c_t5_t41_in = S.Task('c_t5_t41_in', length=1, delay_cost=1)
	S += c_t5_t41_in >= 60
	c_t5_t41_in += MAS_in[1]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	S += c_t5_t41_mem0 >= 60
	c_t5_t41_mem0 += MAS_MEM[4]

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	S += c_t5_t41_mem1 >= 60
	c_t5_t41_mem1 += MAS_MEM[1]

	c_s2011_in = S.Task('c_s2011_in', length=1, delay_cost=1)
	S += c_s2011_in >= 61
	c_s2011_in += MAS_in[1]

	c_s2011_mem0 = S.Task('c_s2011_mem0', length=1, delay_cost=1)
	S += c_s2011_mem0 >= 61
	c_s2011_mem0 += MAS_MEM[2]

	c_s2011_mem1 = S.Task('c_s2011_mem1', length=1, delay_cost=1)
	S += c_s2011_mem1 >= 61
	c_s2011_mem1 += MAS_MEM[1]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 61
	c_t0_t20_in += MAS_in[0]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 61
	c_t0_t20_mem0 += MM_MEM[2]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 61
	c_t0_t20_mem1 += MM_MEM[1]

	c_t0_t2_t5 = S.Task('c_t0_t2_t5', length=2, delay_cost=1)
	S += c_t0_t2_t5 >= 61
	c_t0_t2_t5 += MAS[2]

	c_t1_t51 = S.Task('c_t1_t51', length=2, delay_cost=1)
	S += c_t1_t51 >= 61
	c_t1_t51 += MAS[3]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 61
	c_t4_t20_in += MAS_in[2]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 61
	c_t4_t20_mem0 += MM_MEM[0]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 61
	c_t4_t20_mem1 += MM_MEM[3]

	c_t4_t2_t5 = S.Task('c_t4_t2_t5', length=2, delay_cost=1)
	S += c_t4_t2_t5 >= 61
	c_t4_t2_t5 += MAS[0]

	c_t4_t41_in = S.Task('c_t4_t41_in', length=1, delay_cost=1)
	S += c_t4_t41_in >= 61
	c_t4_t41_in += MAS_in[3]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	S += c_t4_t41_mem0 >= 61
	c_t4_t41_mem0 += MAS_MEM[0]

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	S += c_t4_t41_mem1 >= 61
	c_t4_t41_mem1 += MAS_MEM[5]

	c_t5_t41 = S.Task('c_t5_t41', length=2, delay_cost=1)
	S += c_t5_t41 >= 61
	c_t5_t41 += MAS[1]

	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	S += c210_in >= 62
	c210_in += MAS_in[1]

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	S += c210_mem0 >= 62
	c210_mem0 += MAS_MEM[6]

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	S += c210_mem1 >= 62
	c210_mem1 += MAS_MEM[7]

	c_s0011_in = S.Task('c_s0011_in', length=1, delay_cost=1)
	S += c_s0011_in >= 62
	c_s0011_in += MAS_in[0]

	c_s0011_mem0 = S.Task('c_s0011_mem0', length=1, delay_cost=1)
	S += c_s0011_mem0 >= 62
	c_s0011_mem0 += MAS_MEM[0]

	c_s0011_mem1 = S.Task('c_s0011_mem1', length=1, delay_cost=1)
	S += c_s0011_mem1 >= 62
	c_s0011_mem1 += MAS_MEM[1]

	c_s2011 = S.Task('c_s2011', length=2, delay_cost=1)
	S += c_s2011 >= 62
	c_s2011 += MAS[1]

	c_t0_t20 = S.Task('c_t0_t20', length=2, delay_cost=1)
	S += c_t0_t20 >= 62
	c_t0_t20 += MAS[0]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 62
	c_t3_t20_in += MAS_in[2]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 62
	c_t3_t20_mem0 += MM_MEM[0]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 62
	c_t3_t20_mem1 += MM_MEM[1]

	c_t3_t50_in = S.Task('c_t3_t50_in', length=1, delay_cost=1)
	S += c_t3_t50_in >= 62
	c_t3_t50_in += MAS_in[3]

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	S += c_t3_t50_mem0 >= 62
	c_t3_t50_mem0 += MAS_MEM[4]

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	S += c_t3_t50_mem1 >= 62
	c_t3_t50_mem1 += MAS_MEM[3]

	c_t4_t20 = S.Task('c_t4_t20', length=2, delay_cost=1)
	S += c_t4_t20 >= 62
	c_t4_t20 += MAS[2]

	c_t4_t41 = S.Task('c_t4_t41', length=2, delay_cost=1)
	S += c_t4_t41 >= 62
	c_t4_t41 += MAS[3]

	c_t5_t2_t4_in = S.Task('c_t5_t2_t4_in', length=1, delay_cost=1)
	S += c_t5_t2_t4_in >= 62
	c_t5_t2_t4_in += MM_in[1]

	c_t5_t2_t4_mem0 = S.Task('c_t5_t2_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t4_mem0 >= 62
	c_t5_t2_t4_mem0 += MAS_MEM[2]

	c_t5_t2_t4_mem1 = S.Task('c_t5_t2_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t4_mem1 >= 62
	c_t5_t2_t4_mem1 += MAS_MEM[5]

	c210 = S.Task('c210', length=2, delay_cost=1)
	S += c210 >= 63
	c210 += MAS[1]

	c_s0011 = S.Task('c_s0011', length=2, delay_cost=1)
	S += c_s0011 >= 63
	c_s0011 += MAS[0]

	c_s1111_in = S.Task('c_s1111_in', length=1, delay_cost=1)
	S += c_s1111_in >= 63
	c_s1111_in += MAS_in[1]

	c_s1111_mem0 = S.Task('c_s1111_mem0', length=1, delay_cost=1)
	S += c_s1111_mem0 >= 63
	c_s1111_mem0 += MAS_MEM[0]

	c_s1111_mem1 = S.Task('c_s1111_mem1', length=1, delay_cost=1)
	S += c_s1111_mem1 >= 63
	c_s1111_mem1 += MAS_MEM[7]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 63
	c_t0_t21_in += MAS_in[0]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 63
	c_t0_t21_mem0 += MM_MEM[2]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 63
	c_t0_t21_mem1 += MAS_MEM[5]

	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	S += c_t2_t50_in >= 63
	c_t2_t50_in += MAS_in[2]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 63
	c_t2_t50_mem0 += MAS_MEM[2]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 63
	c_t2_t50_mem1 += MAS_MEM[1]

	c_t3_t20 = S.Task('c_t3_t20', length=2, delay_cost=1)
	S += c_t3_t20 >= 63
	c_t3_t20 += MAS[2]

	c_t3_t50 = S.Task('c_t3_t50', length=2, delay_cost=1)
	S += c_t3_t50 >= 63
	c_t3_t50 += MAS[3]

	c_t5_t2_t4 = S.Task('c_t5_t2_t4', length=11, delay_cost=1)
	S += c_t5_t2_t4 >= 63
	c_t5_t2_t4 += MM[1]

	c_t5_t2_t5_in = S.Task('c_t5_t2_t5_in', length=1, delay_cost=1)
	S += c_t5_t2_t5_in >= 63
	c_t5_t2_t5_in += MAS_in[3]

	c_t5_t2_t5_mem0 = S.Task('c_t5_t2_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t2_t5_mem0 >= 63
	c_t5_t2_t5_mem0 += MM_MEM[0]

	c_t5_t2_t5_mem1 = S.Task('c_t5_t2_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t2_t5_mem1 >= 63
	c_t5_t2_t5_mem1 += MM_MEM[1]

	c_s1111 = S.Task('c_s1111', length=2, delay_cost=1)
	S += c_s1111 >= 64
	c_s1111 += MAS[1]

	c_t000_in = S.Task('c_t000_in', length=1, delay_cost=1)
	S += c_t000_in >= 64
	c_t000_in += MAS_in[3]

	c_t000_mem0 = S.Task('c_t000_mem0', length=1, delay_cost=1)
	S += c_t000_mem0 >= 64
	c_t000_mem0 += MAS_MEM[0]

	c_t000_mem1 = S.Task('c_t000_mem1', length=1, delay_cost=1)
	S += c_t000_mem1 >= 64
	c_t000_mem1 += MAS_MEM[7]

	c_t0_t21 = S.Task('c_t0_t21', length=2, delay_cost=1)
	S += c_t0_t21 >= 64
	c_t0_t21 += MAS[0]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 64
	c_t1_t21_in += MAS_in[2]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 64
	c_t1_t21_mem0 += MM_MEM[2]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 64
	c_t1_t21_mem1 += MAS_MEM[1]

	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	S += c_t1_t50_in >= 64
	c_t1_t50_in += MAS_in[0]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 64
	c_t1_t50_mem0 += MAS_MEM[4]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 64
	c_t1_t50_mem1 += MAS_MEM[5]

	c_t2_t50 = S.Task('c_t2_t50', length=2, delay_cost=1)
	S += c_t2_t50 >= 64
	c_t2_t50 += MAS[2]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 64
	c_t5_t20_in += MAS_in[1]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 64
	c_t5_t20_mem0 += MM_MEM[0]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 64
	c_t5_t20_mem1 += MM_MEM[1]

	c_t5_t2_t5 = S.Task('c_t5_t2_t5', length=2, delay_cost=1)
	S += c_t5_t2_t5 >= 64
	c_t5_t2_t5 += MAS[3]

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	S += c210_w >= 65
	c210_w += MAIN_MEM_w

	c_s1_y1_0_in = S.Task('c_s1_y1_0_in', length=1, delay_cost=1)
	S += c_s1_y1_0_in >= 65
	c_s1_y1_0_in += MAS_in[1]

	c_s1_y1_0_mem0 = S.Task('c_s1_y1_0_mem0', length=1, delay_cost=1)
	S += c_s1_y1_0_mem0 >= 65
	c_s1_y1_0_mem0 += MAS_MEM[6]

	c_s1_y1_0_mem1 = S.Task('c_s1_y1_0_mem1', length=1, delay_cost=1)
	S += c_s1_y1_0_mem1 >= 65
	c_s1_y1_0_mem1 += MAS_MEM[3]

	c_s1_y1_1_in = S.Task('c_s1_y1_1_in', length=1, delay_cost=1)
	S += c_s1_y1_1_in >= 65
	c_s1_y1_1_in += MAS_in[0]

	c_s1_y1_1_mem0 = S.Task('c_s1_y1_1_mem0', length=1, delay_cost=1)
	S += c_s1_y1_1_mem0 >= 65
	c_s1_y1_1_mem0 += MAS_MEM[2]

	c_s1_y1_1_mem1 = S.Task('c_s1_y1_1_mem1', length=1, delay_cost=1)
	S += c_s1_y1_1_mem1 >= 65
	c_s1_y1_1_mem1 += MAS_MEM[7]

	c_t000 = S.Task('c_t000', length=2, delay_cost=1)
	S += c_t000 >= 65
	c_t000 += MAS[3]

	c_t1_t21 = S.Task('c_t1_t21', length=2, delay_cost=1)
	S += c_t1_t21 >= 65
	c_t1_t21 += MAS[2]

	c_t1_t50 = S.Task('c_t1_t50', length=2, delay_cost=1)
	S += c_t1_t50 >= 65
	c_t1_t50 += MAS[0]

	c_t4_t50_in = S.Task('c_t4_t50_in', length=1, delay_cost=1)
	S += c_t4_t50_in >= 65
	c_t4_t50_in += MAS_in[2]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	S += c_t4_t50_mem0 >= 65
	c_t4_t50_mem0 += MAS_MEM[4]

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	S += c_t4_t50_mem1 >= 65
	c_t4_t50_mem1 += MAS_MEM[1]

	c_t5_t20 = S.Task('c_t5_t20', length=2, delay_cost=1)
	S += c_t5_t20 >= 65
	c_t5_t20 += MAS[1]

	c_t5_t40_in = S.Task('c_t5_t40_in', length=1, delay_cost=1)
	S += c_t5_t40_in >= 65
	c_t5_t40_in += MAS_in[3]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	S += c_t5_t40_mem0 >= 65
	c_t5_t40_mem0 += MAS_MEM[0]

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	S += c_t5_t40_mem1 >= 65
	c_t5_t40_mem1 += MAS_MEM[5]

	c_s1_y1_0 = S.Task('c_s1_y1_0', length=2, delay_cost=1)
	S += c_s1_y1_0 >= 66
	c_s1_y1_0 += MAS[1]

	c_s1_y1_1 = S.Task('c_s1_y1_1', length=2, delay_cost=1)
	S += c_s1_y1_1 >= 66
	c_s1_y1_1 += MAS[0]

	c_t001_in = S.Task('c_t001_in', length=1, delay_cost=1)
	S += c_t001_in >= 66
	c_t001_in += MAS_in[1]

	c_t001_mem0 = S.Task('c_t001_mem0', length=1, delay_cost=1)
	S += c_t001_mem0 >= 66
	c_t001_mem0 += MAS_MEM[0]

	c_t001_mem1 = S.Task('c_t001_mem1', length=1, delay_cost=1)
	S += c_t001_mem1 >= 66
	c_t001_mem1 += MAS_MEM[3]

	c_t100_in = S.Task('c_t100_in', length=1, delay_cost=1)
	S += c_t100_in >= 66
	c_t100_in += MAS_in[2]

	c_t100_mem0 = S.Task('c_t100_mem0', length=1, delay_cost=1)
	S += c_t100_mem0 >= 66
	c_t100_mem0 += MAS_MEM[6]

	c_t100_mem1 = S.Task('c_t100_mem1', length=1, delay_cost=1)
	S += c_t100_mem1 >= 66
	c_t100_mem1 += MAS_MEM[1]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 66
	c_t2_t21_in += MAS_in[3]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 66
	c_t2_t21_mem0 += MM_MEM[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 66
	c_t2_t21_mem1 += MAS_MEM[7]

	c_t4_t50 = S.Task('c_t4_t50', length=2, delay_cost=1)
	S += c_t4_t50 >= 66
	c_t4_t50 += MAS[2]

	c_t511_in = S.Task('c_t511_in', length=1, delay_cost=1)
	S += c_t511_in >= 66
	c_t511_in += MAS_in[0]

	c_t511_mem0 = S.Task('c_t511_mem0', length=1, delay_cost=1)
	S += c_t511_mem0 >= 66
	c_t511_mem0 += MAS_MEM[4]

	c_t511_mem1 = S.Task('c_t511_mem1', length=1, delay_cost=1)
	S += c_t511_mem1 >= 66
	c_t511_mem1 += MAS_MEM[5]

	c_t5_t40 = S.Task('c_t5_t40', length=2, delay_cost=1)
	S += c_t5_t40 >= 66
	c_t5_t40 += MAS[3]

	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	S += c000_in >= 67
	c000_in += MAS_in[3]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 67
	c000_mem0 += MAS_MEM[6]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 67
	c000_mem1 += MAS_MEM[3]

	c_t001 = S.Task('c_t001', length=2, delay_cost=1)
	S += c_t001 >= 67
	c_t001 += MAS[1]

	c_t100 = S.Task('c_t100', length=2, delay_cost=1)
	S += c_t100 >= 67
	c_t100 += MAS[2]

	c_t200_in = S.Task('c_t200_in', length=1, delay_cost=1)
	S += c_t200_in >= 67
	c_t200_in += MAS_in[0]

	c_t200_mem0 = S.Task('c_t200_mem0', length=1, delay_cost=1)
	S += c_t200_mem0 >= 67
	c_t200_mem0 += MAS_MEM[4]

	c_t200_mem1 = S.Task('c_t200_mem1', length=1, delay_cost=1)
	S += c_t200_mem1 >= 67
	c_t200_mem1 += MAS_MEM[5]

	c_t2_t21 = S.Task('c_t2_t21', length=2, delay_cost=1)
	S += c_t2_t21 >= 67
	c_t2_t21 += MAS[3]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 67
	c_t4_t21_in += MAS_in[1]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 67
	c_t4_t21_mem0 += MM_MEM[2]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 67
	c_t4_t21_mem1 += MAS_MEM[1]

	c_t4_t51_in = S.Task('c_t4_t51_in', length=1, delay_cost=1)
	S += c_t4_t51_in >= 67
	c_t4_t51_in += MAS_in[2]

	c_t4_t51_mem0 = S.Task('c_t4_t51_mem0', length=1, delay_cost=1)
	S += c_t4_t51_mem0 >= 67
	c_t4_t51_mem0 += MAS_MEM[0]

	c_t4_t51_mem1 = S.Task('c_t4_t51_mem1', length=1, delay_cost=1)
	S += c_t4_t51_mem1 >= 67
	c_t4_t51_mem1 += MAS_MEM[7]

	c_t511 = S.Task('c_t511', length=2, delay_cost=1)
	S += c_t511 >= 67
	c_t511 += MAS[0]

	c000 = S.Task('c000', length=2, delay_cost=1)
	S += c000 >= 68
	c000 += MAS[3]

	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	S += c001_in >= 68
	c001_in += MAS_in[2]

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 68
	c001_mem0 += MAS_MEM[2]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 68
	c001_mem1 += MAS_MEM[1]

	c_s0000_in = S.Task('c_s0000_in', length=1, delay_cost=1)
	S += c_s0000_in >= 68
	c_s0000_in += MAS_in[3]

	c_s0000_mem0 = S.Task('c_s0000_mem0', length=1, delay_cost=1)
	S += c_s0000_mem0 >= 68
	c_s0000_mem0 += MAS_MEM[6]

	c_s0000_mem1 = S.Task('c_s0000_mem1', length=1, delay_cost=1)
	S += c_s0000_mem1 >= 68
	c_s0000_mem1 += MAS_MEM[5]

	c_s211_in = S.Task('c_s211_in', length=1, delay_cost=1)
	S += c_s211_in >= 68
	c_s211_in += MAS_in[0]

	c_s211_mem0 = S.Task('c_s211_mem0', length=1, delay_cost=1)
	S += c_s211_mem0 >= 68
	c_s211_mem0 += MAS_MEM[0]

	c_s211_mem1 = S.Task('c_s211_mem1', length=1, delay_cost=1)
	S += c_s211_mem1 >= 68
	c_s211_mem1 += MAS_MEM[3]

	c_t200 = S.Task('c_t200', length=2, delay_cost=1)
	S += c_t200 >= 68
	c_t200 += MAS[0]

	c_t300_in = S.Task('c_t300_in', length=1, delay_cost=1)
	S += c_t300_in >= 68
	c_t300_in += MAS_in[1]

	c_t300_mem0 = S.Task('c_t300_mem0', length=1, delay_cost=1)
	S += c_t300_mem0 >= 68
	c_t300_mem0 += MAS_MEM[4]

	c_t300_mem1 = S.Task('c_t300_mem1', length=1, delay_cost=1)
	S += c_t300_mem1 >= 68
	c_t300_mem1 += MAS_MEM[7]

	c_t4_t21 = S.Task('c_t4_t21', length=2, delay_cost=1)
	S += c_t4_t21 >= 68
	c_t4_t21 += MAS[1]

	c_t4_t51 = S.Task('c_t4_t51', length=2, delay_cost=1)
	S += c_t4_t51 >= 68
	c_t4_t51 += MAS[2]

	c001 = S.Task('c001', length=2, delay_cost=1)
	S += c001 >= 69
	c001 += MAS[2]

	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	S += c110_in >= 69
	c110_in += MAS_in[0]

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	S += c110_mem0 >= 69
	c110_mem0 += MAS_MEM[0]

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	S += c110_mem1 >= 69
	c110_mem1 += MAS_MEM[1]

	c_s0000 = S.Task('c_s0000', length=2, delay_cost=1)
	S += c_s0000 >= 69
	c_s0000 += MAS[3]

	c_s211 = S.Task('c_s211', length=2, delay_cost=1)
	S += c_s211 >= 69
	c_s211 += MAS[0]

	c_t101_in = S.Task('c_t101_in', length=1, delay_cost=1)
	S += c_t101_in >= 69
	c_t101_in += MAS_in[3]

	c_t101_mem0 = S.Task('c_t101_mem0', length=1, delay_cost=1)
	S += c_t101_mem0 >= 69
	c_t101_mem0 += MAS_MEM[4]

	c_t101_mem1 = S.Task('c_t101_mem1', length=1, delay_cost=1)
	S += c_t101_mem1 >= 69
	c_t101_mem1 += MAS_MEM[7]

	c_t201_in = S.Task('c_t201_in', length=1, delay_cost=1)
	S += c_t201_in >= 69
	c_t201_in += MAS_in[2]

	c_t201_mem0 = S.Task('c_t201_mem0', length=1, delay_cost=1)
	S += c_t201_mem0 >= 69
	c_t201_mem0 += MAS_MEM[6]

	c_t201_mem1 = S.Task('c_t201_mem1', length=1, delay_cost=1)
	S += c_t201_mem1 >= 69
	c_t201_mem1 += MAS_MEM[3]

	c_t300 = S.Task('c_t300', length=2, delay_cost=1)
	S += c_t300 >= 69
	c_t300 += MAS[1]

	c_t401_in = S.Task('c_t401_in', length=1, delay_cost=1)
	S += c_t401_in >= 69
	c_t401_in += MAS_in[1]

	c_t401_mem0 = S.Task('c_t401_mem0', length=1, delay_cost=1)
	S += c_t401_mem0 >= 69
	c_t401_mem0 += MAS_MEM[2]

	c_t401_mem1 = S.Task('c_t401_mem1', length=1, delay_cost=1)
	S += c_t401_mem1 >= 69
	c_t401_mem1 += MAS_MEM[5]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 70
	c000_w += MAIN_MEM_w

	c110 = S.Task('c110', length=2, delay_cost=1)
	S += c110 >= 70
	c110 += MAS[0]

	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	S += c211_in >= 70
	c211_in += MAS_in[2]

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	S += c211_mem0 >= 70
	c211_mem0 += MAS_MEM[0]

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	S += c211_mem1 >= 70
	c211_mem1 += MAS_MEM[1]

	c_s000_in = S.Task('c_s000_in', length=1, delay_cost=1)
	S += c_s000_in >= 70
	c_s000_in += MAS_in[1]

	c_s000_mem0 = S.Task('c_s000_mem0', length=1, delay_cost=1)
	S += c_s000_mem0 >= 70
	c_s000_mem0 += MAS_MEM[2]

	c_s000_mem1 = S.Task('c_s000_mem1', length=1, delay_cost=1)
	S += c_s000_mem1 >= 70
	c_s000_mem1 += MAS_MEM[7]

	c_t101 = S.Task('c_t101', length=2, delay_cost=1)
	S += c_t101 >= 70
	c_t101 += MAS[3]

	c_t201 = S.Task('c_t201', length=2, delay_cost=1)
	S += c_t201 >= 70
	c_t201 += MAS[2]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 70
	c_t3_t21_in += MAS_in[3]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 70
	c_t3_t21_mem0 += MM_MEM[2]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 70
	c_t3_t21_mem1 += MAS_MEM[5]

	c_t401 = S.Task('c_t401', length=2, delay_cost=1)
	S += c_t401 >= 70
	c_t401 += MAS[1]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 71
	c001_w += MAIN_MEM_w

	c211 = S.Task('c211', length=2, delay_cost=1)
	S += c211 >= 71
	c211 += MAS[2]

	c_s000 = S.Task('c_s000', length=2, delay_cost=1)
	S += c_s000 >= 71
	c_s000 += MAS[1]

	c_s0001_in = S.Task('c_s0001_in', length=1, delay_cost=1)
	S += c_s0001_in >= 71
	c_s0001_in += MAS_in[0]

	c_s0001_mem0 = S.Task('c_s0001_mem0', length=1, delay_cost=1)
	S += c_s0001_mem0 >= 71
	c_s0001_mem0 += MAS_MEM[2]

	c_s0001_mem1 = S.Task('c_s0001_mem1', length=1, delay_cost=1)
	S += c_s0001_mem1 >= 71
	c_s0001_mem1 += MAS_MEM[7]

	c_s011_in = S.Task('c_s011_in', length=1, delay_cost=1)
	S += c_s011_in >= 71
	c_s011_in += MAS_in[3]

	c_s011_mem0 = S.Task('c_s011_mem0', length=1, delay_cost=1)
	S += c_s011_mem0 >= 71
	c_s011_mem0 += MAS_MEM[0]

	c_s011_mem1 = S.Task('c_s011_mem1', length=1, delay_cost=1)
	S += c_s011_mem1 >= 71
	c_s011_mem1 += MAS_MEM[1]

	c_s1001_in = S.Task('c_s1001_in', length=1, delay_cost=1)
	S += c_s1001_in >= 71
	c_s1001_in += MAS_in[1]

	c_s1001_mem0 = S.Task('c_s1001_mem0', length=1, delay_cost=1)
	S += c_s1001_mem0 >= 71
	c_s1001_mem0 += MAS_MEM[6]

	c_s1001_mem1 = S.Task('c_s1001_mem1', length=1, delay_cost=1)
	S += c_s1001_mem1 >= 71
	c_s1001_mem1 += MAS_MEM[5]

	c_t3_t21 = S.Task('c_t3_t21', length=2, delay_cost=1)
	S += c_t3_t21 >= 71
	c_t3_t21 += MAS[3]

	c_t5_t51_in = S.Task('c_t5_t51_in', length=1, delay_cost=1)
	S += c_t5_t51_in >= 71
	c_t5_t51_in += MAS_in[2]

	c_t5_t51_mem0 = S.Task('c_t5_t51_mem0', length=1, delay_cost=1)
	S += c_t5_t51_mem0 >= 71
	c_t5_t51_mem0 += MAS_MEM[4]

	c_t5_t51_mem1 = S.Task('c_t5_t51_mem1', length=1, delay_cost=1)
	S += c_t5_t51_mem1 >= 71
	c_t5_t51_mem1 += MAS_MEM[3]

	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	S += c100_in >= 72
	c100_in += MAS_in[0]

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	S += c100_mem0 >= 72
	c100_mem0 += MAS_MEM[2]

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	S += c100_mem1 >= 72
	c100_mem1 += MAS_MEM[3]

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	S += c110_w >= 72
	c110_w += MAIN_MEM_w

	c_s0001 = S.Task('c_s0001', length=2, delay_cost=1)
	S += c_s0001 >= 72
	c_s0001 += MAS[0]

	c_s011 = S.Task('c_s011', length=2, delay_cost=1)
	S += c_s011 >= 72
	c_s011 += MAS[3]

	c_s1001 = S.Task('c_s1001', length=2, delay_cost=1)
	S += c_s1001 >= 72
	c_s1001 += MAS[1]

	c_t5_t50_in = S.Task('c_t5_t50_in', length=1, delay_cost=1)
	S += c_t5_t50_in >= 72
	c_t5_t50_in += MAS_in[2]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	S += c_t5_t50_mem0 >= 72
	c_t5_t50_mem0 += MAS_MEM[0]

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	S += c_t5_t50_mem1 >= 72
	c_t5_t50_mem1 += MAS_MEM[7]

	c_t5_t51 = S.Task('c_t5_t51', length=2, delay_cost=1)
	S += c_t5_t51 >= 72
	c_t5_t51 += MAS[2]

	c100 = S.Task('c100', length=2, delay_cost=1)
	S += c100 >= 73
	c100 += MAS[0]

	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	S += c111_in >= 73
	c111_in += MAS_in[3]

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	S += c111_mem0 >= 73
	c111_mem0 += MAS_MEM[6]

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	S += c111_mem1 >= 73
	c111_mem1 += MAS_MEM[5]

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	S += c211_w >= 73
	c211_w += MAIN_MEM_w

	c_s1101_in = S.Task('c_s1101_in', length=1, delay_cost=1)
	S += c_s1101_in >= 73
	c_s1101_in += MAS_in[0]

	c_s1101_mem0 = S.Task('c_s1101_mem0', length=1, delay_cost=1)
	S += c_s1101_mem0 >= 73
	c_s1101_mem0 += MAS_MEM[2]

	c_s1101_mem1 = S.Task('c_s1101_mem1', length=1, delay_cost=1)
	S += c_s1101_mem1 >= 73
	c_s1101_mem1 += MAS_MEM[3]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 73
	c_t5_t21_in += MAS_in[2]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 73
	c_t5_t21_mem0 += MM_MEM[2]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 73
	c_t5_t21_mem1 += MAS_MEM[7]

	c_t5_t50 = S.Task('c_t5_t50', length=2, delay_cost=1)
	S += c_t5_t50 >= 73
	c_t5_t50 += MAS[2]

	c111 = S.Task('c111', length=2, delay_cost=1)
	S += c111 >= 74
	c111 += MAS[3]

	c_s001_in = S.Task('c_s001_in', length=1, delay_cost=1)
	S += c_s001_in >= 74
	c_s001_in += MAS_in[2]

	c_s001_mem0 = S.Task('c_s001_mem0', length=1, delay_cost=1)
	S += c_s001_mem0 >= 74
	c_s001_mem0 += MAS_MEM[6]

	c_s001_mem1 = S.Task('c_s001_mem1', length=1, delay_cost=1)
	S += c_s001_mem1 >= 74
	c_s001_mem1 += MAS_MEM[1]

	c_s1101 = S.Task('c_s1101', length=2, delay_cost=1)
	S += c_s1101 >= 74
	c_s1101 += MAS[0]

	c_s2000_in = S.Task('c_s2000_in', length=1, delay_cost=1)
	S += c_s2000_in >= 74
	c_s2000_in += MAS_in[0]

	c_s2000_mem0 = S.Task('c_s2000_mem0', length=1, delay_cost=1)
	S += c_s2000_mem0 >= 74
	c_s2000_mem0 += MAS_MEM[0]

	c_s2000_mem1 = S.Task('c_s2000_mem1', length=1, delay_cost=1)
	S += c_s2000_mem1 >= 74
	c_s2000_mem1 += MAS_MEM[7]

	c_s2001_in = S.Task('c_s2001_in', length=1, delay_cost=1)
	S += c_s2001_in >= 74
	c_s2001_in += MAS_in[1]

	c_s2001_mem0 = S.Task('c_s2001_mem0', length=1, delay_cost=1)
	S += c_s2001_mem0 >= 74
	c_s2001_mem0 += MAS_MEM[4]

	c_s2001_mem1 = S.Task('c_s2001_mem1', length=1, delay_cost=1)
	S += c_s2001_mem1 >= 74
	c_s2001_mem1 += MAS_MEM[3]

	c_t500_in = S.Task('c_t500_in', length=1, delay_cost=1)
	S += c_t500_in >= 74
	c_t500_in += MAS_in[3]

	c_t500_mem0 = S.Task('c_t500_mem0', length=1, delay_cost=1)
	S += c_t500_mem0 >= 74
	c_t500_mem0 += MAS_MEM[2]

	c_t500_mem1 = S.Task('c_t500_mem1', length=1, delay_cost=1)
	S += c_t500_mem1 >= 74
	c_t500_mem1 += MAS_MEM[5]

	c_t5_t21 = S.Task('c_t5_t21', length=2, delay_cost=1)
	S += c_t5_t21 >= 74
	c_t5_t21 += MAS[2]

	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	S += c011_in >= 75
	c011_in += MAS_in[1]

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	S += c011_mem0 >= 75
	c011_mem0 += MAS_MEM[0]

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	S += c011_mem1 >= 75
	c011_mem1 += MAS_MEM[1]

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	S += c100_w >= 75
	c100_w += MAIN_MEM_w

	c_s001 = S.Task('c_s001', length=2, delay_cost=1)
	S += c_s001 >= 75
	c_s001 += MAS[2]

	c_s2000 = S.Task('c_s2000', length=2, delay_cost=1)
	S += c_s2000 >= 75
	c_s2000 += MAS[0]

	c_s2001 = S.Task('c_s2001', length=2, delay_cost=1)
	S += c_s2001 >= 75
	c_s2001 += MAS[1]

	c_t500 = S.Task('c_t500', length=2, delay_cost=1)
	S += c_t500 >= 75
	c_t500 += MAS[3]

	c_t501_in = S.Task('c_t501_in', length=1, delay_cost=1)
	S += c_t501_in >= 75
	c_t501_in += MAS_in[2]

	c_t501_mem0 = S.Task('c_t501_mem0', length=1, delay_cost=1)
	S += c_t501_mem0 >= 75
	c_t501_mem0 += MAS_MEM[4]

	c_t501_mem1 = S.Task('c_t501_mem1', length=1, delay_cost=1)
	S += c_t501_mem1 >= 75
	c_t501_mem1 += MAS_MEM[5]

	c011 = S.Task('c011', length=2, delay_cost=1)
	S += c011 >= 76
	c011 += MAS[1]

	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	S += c101_in >= 76
	c101_in += MAS_in[3]

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	S += c101_mem0 >= 76
	c101_mem0 += MAS_MEM[4]

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	S += c101_mem1 >= 76
	c101_mem1 += MAS_MEM[5]

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	S += c111_w >= 76
	c111_w += MAIN_MEM_w

	c_s200_in = S.Task('c_s200_in', length=1, delay_cost=1)
	S += c_s200_in >= 76
	c_s200_in += MAS_in[2]

	c_s200_mem0 = S.Task('c_s200_mem0', length=1, delay_cost=1)
	S += c_s200_mem0 >= 76
	c_s200_mem0 += MAS_MEM[6]

	c_s200_mem1 = S.Task('c_s200_mem1', length=1, delay_cost=1)
	S += c_s200_mem1 >= 76
	c_s200_mem1 += MAS_MEM[1]

	c_t501 = S.Task('c_t501', length=2, delay_cost=1)
	S += c_t501 >= 76
	c_t501 += MAS[2]

	c101 = S.Task('c101', length=2, delay_cost=1)
	S += c101 >= 77
	c101 += MAS[3]

	c_s200 = S.Task('c_s200', length=2, delay_cost=1)
	S += c_s200 >= 77
	c_s200 += MAS[2]

	c_s201_in = S.Task('c_s201_in', length=1, delay_cost=1)
	S += c_s201_in >= 77
	c_s201_in += MAS_in[0]

	c_s201_mem0 = S.Task('c_s201_mem0', length=1, delay_cost=1)
	S += c_s201_mem0 >= 77
	c_s201_mem0 += MAS_MEM[4]

	c_s201_mem1 = S.Task('c_s201_mem1', length=1, delay_cost=1)
	S += c_s201_mem1 >= 77
	c_s201_mem1 += MAS_MEM[3]

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	S += c011_w >= 78
	c011_w += MAIN_MEM_w

	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	S += c200_in >= 78
	c200_in += MAS_in[3]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 78
	c200_mem0 += MAS_MEM[4]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 78
	c200_mem1 += MAS_MEM[5]

	c_s201 = S.Task('c_s201', length=2, delay_cost=1)
	S += c_s201 >= 78
	c_s201 += MAS[0]

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	S += c101_w >= 79
	c101_w += MAIN_MEM_w

	c200 = S.Task('c200', length=2, delay_cost=1)
	S += c200 >= 79
	c200 += MAS[3]

	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	S += c201_in >= 79
	c201_in += MAS_in[2]

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 79
	c201_mem0 += MAS_MEM[6]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 79
	c201_mem1 += MAS_MEM[1]

	c201 = S.Task('c201', length=2, delay_cost=1)
	S += c201 >= 80
	c201 += MAS[2]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 81
	c200_w += MAIN_MEM_w

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 82
	c201_w += MAIN_MEM_w


	# new tasks
	c_t3_t51 = S.Task('c_t3_t51', length=2, delay_cost=1)
	c_t3_t51 += alt(MAS)
	c_t3_t51_in = S.Task('c_t3_t51_in', length=1, delay_cost=1)
	c_t3_t51_in += alt(MAS_in)
	S += c_t3_t51_in*MAS_in[0]<=c_t3_t51*MAS[0]

	S += c_t3_t51_in*MAS_in[1]<=c_t3_t51*MAS[1]

	S += c_t3_t51_in*MAS_in[2]<=c_t3_t51*MAS[2]

	S += c_t3_t51_in*MAS_in[3]<=c_t3_t51*MAS[3]

	S += c_t3_t51<73

	c_t3_t51_mem0 = S.Task('c_t3_t51_mem0', length=1, delay_cost=1)
	c_t3_t51_mem0 += MAS_MEM[6]
	S += 52 < c_t3_t51_mem0
	S += c_t3_t51_mem0 <= c_t3_t51

	c_t3_t51_mem1 = S.Task('c_t3_t51_mem1', length=1, delay_cost=1)
	c_t3_t51_mem1 += MAS_MEM[3]
	S += 61 < c_t3_t51_mem1
	S += c_t3_t51_mem1 <= c_t3_t51

	c_t301 = S.Task('c_t301', length=2, delay_cost=1)
	c_t301 += alt(MAS)
	c_t301_in = S.Task('c_t301_in', length=1, delay_cost=1)
	c_t301_in += alt(MAS_in)
	S += c_t301_in*MAS_in[0]<=c_t301*MAS[0]

	S += c_t301_in*MAS_in[1]<=c_t301*MAS[1]

	S += c_t301_in*MAS_in[2]<=c_t301*MAS[2]

	S += c_t301_in*MAS_in[3]<=c_t301*MAS[3]

	S += c_t301<75

	c_t301_mem0 = S.Task('c_t301_mem0', length=1, delay_cost=1)
	c_t301_mem0 += MAS_MEM[6]
	S += 72 < c_t301_mem0
	S += c_t301_mem0 <= c_t301

	c_t301_mem1 = S.Task('c_t301_mem1', length=1, delay_cost=1)
	c_t301_mem1 += alt(MAS_MEM)
	S += (c_t3_t51*MAS[0])-1 < c_t301_mem1*MAS_MEM[1]
	S += (c_t3_t51*MAS[1])-1 < c_t301_mem1*MAS_MEM[3]
	S += (c_t3_t51*MAS[2])-1 < c_t301_mem1*MAS_MEM[5]
	S += (c_t3_t51*MAS[3])-1 < c_t301_mem1*MAS_MEM[7]
	S += c_t301_mem1 <= c_t301

	c_t400 = S.Task('c_t400', length=2, delay_cost=1)
	c_t400 += alt(MAS)
	c_t400_in = S.Task('c_t400_in', length=1, delay_cost=1)
	c_t400_in += alt(MAS_in)
	S += c_t400_in*MAS_in[0]<=c_t400*MAS[0]

	S += c_t400_in*MAS_in[1]<=c_t400*MAS[1]

	S += c_t400_in*MAS_in[2]<=c_t400*MAS[2]

	S += c_t400_in*MAS_in[3]<=c_t400*MAS[3]

	S += c_t400<1000

	c_t400_mem0 = S.Task('c_t400_mem0', length=1, delay_cost=1)
	c_t400_mem0 += MAS_MEM[4]
	S += 63 < c_t400_mem0
	S += c_t400_mem0 <= c_t400

	c_t400_mem1 = S.Task('c_t400_mem1', length=1, delay_cost=1)
	c_t400_mem1 += MAS_MEM[5]
	S += 67 < c_t400_mem1
	S += c_t400_mem1 <= c_t400

	c_s1000 = S.Task('c_s1000', length=2, delay_cost=1)
	c_s1000 += alt(MAS)
	c_s1000_in = S.Task('c_s1000_in', length=1, delay_cost=1)
	c_s1000_in += alt(MAS_in)
	S += c_s1000_in*MAS_in[0]<=c_s1000*MAS[0]

	S += c_s1000_in*MAS_in[1]<=c_s1000*MAS[1]

	S += c_s1000_in*MAS_in[2]<=c_s1000*MAS[2]

	S += c_s1000_in*MAS_in[3]<=c_s1000*MAS[3]

	S += c_s1000<1000

	c_s1000_mem0 = S.Task('c_s1000_mem0', length=1, delay_cost=1)
	c_s1000_mem0 += MAS_MEM[4]
	S += 68 < c_s1000_mem0
	S += c_s1000_mem0 <= c_s1000

	c_s1000_mem1 = S.Task('c_s1000_mem1', length=1, delay_cost=1)
	c_s1000_mem1 += MAS_MEM[1]
	S += 69 < c_s1000_mem1
	S += c_s1000_mem1 <= c_s1000

	c_s1100 = S.Task('c_s1100', length=2, delay_cost=1)
	c_s1100 += alt(MAS)
	c_s1100_in = S.Task('c_s1100_in', length=1, delay_cost=1)
	c_s1100_in += alt(MAS_in)
	S += c_s1100_in*MAS_in[0]<=c_s1100*MAS[0]

	S += c_s1100_in*MAS_in[1]<=c_s1100*MAS[1]

	S += c_s1100_in*MAS_in[2]<=c_s1100*MAS[2]

	S += c_s1100_in*MAS_in[3]<=c_s1100*MAS[3]

	S += c_s1100<1000

	c_s1100_mem0 = S.Task('c_s1100_mem0', length=1, delay_cost=1)
	c_s1100_mem0 += alt(MAS_MEM)
	S += (c_t400*MAS[0])-1 < c_s1100_mem0*MAS_MEM[0]
	S += (c_t400*MAS[1])-1 < c_s1100_mem0*MAS_MEM[2]
	S += (c_t400*MAS[2])-1 < c_s1100_mem0*MAS_MEM[4]
	S += (c_t400*MAS[3])-1 < c_s1100_mem0*MAS_MEM[6]
	S += c_s1100_mem0 <= c_s1100

	c_s1100_mem1 = S.Task('c_s1100_mem1', length=1, delay_cost=1)
	c_s1100_mem1 += alt(MAS_MEM)
	S += (c_s1000*MAS[0])-1 < c_s1100_mem1*MAS_MEM[1]
	S += (c_s1000*MAS[1])-1 < c_s1100_mem1*MAS_MEM[3]
	S += (c_s1000*MAS[2])-1 < c_s1100_mem1*MAS_MEM[5]
	S += (c_s1000*MAS[3])-1 < c_s1100_mem1*MAS_MEM[7]
	S += c_s1100_mem1 <= c_s1100

	c010 = S.Task('c010', length=2, delay_cost=1)
	c010 += alt(MAS)
	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MAS_in)
	S += c010_in*MAS_in[0]<=c010*MAS[0]

	S += c010_in*MAS_in[1]<=c010*MAS[1]

	S += c010_in*MAS_in[2]<=c010*MAS[2]

	S += c010_in*MAS_in[3]<=c010*MAS[3]

	S += 34<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	S += c010<1000

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += MAS_MEM[6]
	S += 45 < c010_mem0
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += alt(MAS_MEM)
	S += (c_s1100*MAS[0])-1 < c010_mem1*MAS_MEM[1]
	S += (c_s1100*MAS[1])-1 < c010_mem1*MAS_MEM[3]
	S += (c_s1100*MAS[2])-1 < c010_mem1*MAS_MEM[5]
	S += (c_s1100*MAS[3])-1 < c010_mem1*MAS_MEM[7]
	S += c010_mem1 <= c010

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage2MAS4/SQR/schedule6.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

