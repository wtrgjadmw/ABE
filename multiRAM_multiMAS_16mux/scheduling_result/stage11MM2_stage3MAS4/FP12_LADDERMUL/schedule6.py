from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 225
	S = Scenario("schedule6", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 0
	d_t1_t3_t0_in += MM_in[0]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 0
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 0
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 1
	d_t1_t10_in += MAS_in[2]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 1
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 1
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=11, delay_cost=1)
	S += d_t1_t3_t0 >= 1
	d_t1_t3_t0 += MM[0]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 2
	d_t0_a1_1_in += MAS_in[2]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 2
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 2
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_t10 = S.Task('d_t1_t10', length=3, delay_cost=1)
	S += d_t1_t10 >= 2
	d_t1_t10 += MAS[2]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=3, delay_cost=1)
	S += d_t0_a1_1 >= 3
	d_t0_a1_1 += MAS[2]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 3
	d_t2_t10_in += MAS_in[2]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 3
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 3
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t10 = S.Task('d_t2_t10', length=3, delay_cost=1)
	S += d_t2_t10 >= 4
	d_t2_t10 += MAS[2]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 4
	d_t3000_in += MAS_in[2]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 4
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 4
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 5
	d_t1_t3_t2_in += MAS_in[1]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 5
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 5
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t3000 = S.Task('d_t3000', length=3, delay_cost=1)
	S += d_t3000 >= 5
	d_t3000 += MAS[2]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=3, delay_cost=1)
	S += d_t1_t3_t2 >= 6
	d_t1_t3_t2 += MAS[1]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 6
	d_t2_t3_t1_in += MM_in[1]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 6
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 6
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=11, delay_cost=1)
	S += d_t2_t3_t1 >= 7
	d_t2_t3_t1 += MM[1]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 7
	d_t2_t3_t2_in += MAS_in[3]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 7
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 7
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 8
	d_t0_a1_0_in += MAS_in[1]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 8
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 8
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=3, delay_cost=1)
	S += d_t2_t3_t2 >= 8
	d_t2_t3_t2 += MAS[3]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=3, delay_cost=1)
	S += d_t0_a1_0 >= 9
	d_t0_a1_0 += MAS[1]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 9
	d_t1_a1_0_in += MAS_in[1]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 9
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 9
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=3, delay_cost=1)
	S += d_t1_a1_0 >= 10
	d_t1_a1_0 += MAS[1]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 10
	d_t1_t11_in += MAS_in[1]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 10
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 10
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 11
	d_t0_t11_in += MAS_in[3]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 11
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 11
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t1_t11 = S.Task('d_t1_t11', length=3, delay_cost=1)
	S += d_t1_t11 >= 11
	d_t1_t11 += MAS[1]

	d_t0_t11 = S.Task('d_t0_t11', length=3, delay_cost=1)
	S += d_t0_t11 >= 12
	d_t0_t11 += MAS[3]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 12
	d_t4000_in += MAS_in[3]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 12
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 12
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 13
	d_t0_t3_t0_in += MM_in[0]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 13
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 13
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t1_t2_t3_in = S.Task('d_t1_t2_t3_in', length=1, delay_cost=1)
	S += d_t1_t2_t3_in >= 13
	d_t1_t2_t3_in += MAS_in[3]

	d_t1_t2_t3_mem0 = S.Task('d_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem0 >= 13
	d_t1_t2_t3_mem0 += MAS_MEM[4]

	d_t1_t2_t3_mem1 = S.Task('d_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem1 >= 13
	d_t1_t2_t3_mem1 += MAS_MEM[3]

	d_t4000 = S.Task('d_t4000', length=3, delay_cost=1)
	S += d_t4000 >= 13
	d_t4000 += MAS[3]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=11, delay_cost=1)
	S += d_t0_t3_t0 >= 14
	d_t0_t3_t0 += MM[0]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 14
	d_t0_t3_t1_in += MM_in[0]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 14
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 14
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t1_t2_t3 = S.Task('d_t1_t2_t3', length=3, delay_cost=1)
	S += d_t1_t2_t3 >= 14
	d_t1_t2_t3 += MAS[3]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 15
	d_t0_t10_in += MAS_in[3]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 15
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 15
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=11, delay_cost=1)
	S += d_t0_t3_t1 >= 15
	d_t0_t3_t1 += MM[0]

	d_t0_t10 = S.Task('d_t0_t10', length=3, delay_cost=1)
	S += d_t0_t10 >= 16
	d_t0_t10 += MAS[3]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 16
	d_t0_t3_t2_in += MAS_in[3]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 16
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 16
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=3, delay_cost=1)
	S += d_t0_t3_t2 >= 17
	d_t0_t3_t2 += MAS[3]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 17
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 17
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 17
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t0_t2_t3_in = S.Task('d_t0_t2_t3_in', length=1, delay_cost=1)
	S += d_t0_t2_t3_in >= 18
	d_t0_t2_t3_in += MAS_in[3]

	d_t0_t2_t3_mem0 = S.Task('d_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem0 >= 18
	d_t0_t2_t3_mem0 += MAS_MEM[6]

	d_t0_t2_t3_mem1 = S.Task('d_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem1 >= 18
	d_t0_t2_t3_mem1 += MAS_MEM[7]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=11, delay_cost=1)
	S += d_t1_t3_t1 >= 18
	d_t1_t3_t1 += MM[0]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 18
	d_t2_a1_0_in += MAS_in[0]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 18
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 18
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t0_t2_t3 = S.Task('d_t0_t2_t3', length=3, delay_cost=1)
	S += d_t0_t2_t3 >= 19
	d_t0_t2_t3 += MAS[3]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=3, delay_cost=1)
	S += d_t2_a1_0 >= 19
	d_t2_a1_0 += MAS[0]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 19
	d_t3001_in += MAS_in[0]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 19
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 19
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 20
	d_t1_a1_1_in += MAS_in[0]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 20
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 20
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t3001 = S.Task('d_t3001', length=3, delay_cost=1)
	S += d_t3001 >= 20
	d_t3001 += MAS[0]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=3, delay_cost=1)
	S += d_t1_a1_1 >= 21
	d_t1_a1_1 += MAS[0]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 21
	d_t1_t3_t3_in += MAS_in[2]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 21
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 21
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=3, delay_cost=1)
	S += d_t1_t3_t3 >= 22
	d_t1_t3_t3 += MAS[2]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 22
	d_t2_t11_in += MAS_in[2]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 22
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 22
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t3_t3_t2_in = S.Task('d_t3_t3_t2_in', length=1, delay_cost=1)
	S += d_t3_t3_t2_in >= 22
	d_t3_t3_t2_in += MAS_in[0]

	d_t3_t3_t2_mem0 = S.Task('d_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem0 >= 22
	d_t3_t3_t2_mem0 += MAS_MEM[4]

	d_t3_t3_t2_mem1 = S.Task('d_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem1 >= 22
	d_t3_t3_t2_mem1 += MAS_MEM[1]

	d_t2_t11 = S.Task('d_t2_t11', length=3, delay_cost=1)
	S += d_t2_t11 >= 23
	d_t2_t11 += MAS[2]

	d_t3_t3_t2 = S.Task('d_t3_t3_t2', length=3, delay_cost=1)
	S += d_t3_t3_t2 >= 23
	d_t3_t3_t2 += MAS[0]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 23
	d_t4001_in += MAS_in[0]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 23
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 23
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t4_in = S.Task('d_t1_t3_t4_in', length=1, delay_cost=1)
	S += d_t1_t3_t4_in >= 24
	d_t1_t3_t4_in += MM_in[0]

	d_t1_t3_t4_mem0 = S.Task('d_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem0 >= 24
	d_t1_t3_t4_mem0 += MAS_MEM[2]

	d_t1_t3_t4_mem1 = S.Task('d_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem1 >= 24
	d_t1_t3_t4_mem1 += MAS_MEM[5]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 24
	d_t2_t3_t3_in += MAS_in[0]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 24
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 24
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t4001 = S.Task('d_t4001', length=3, delay_cost=1)
	S += d_t4001 >= 24
	d_t4001 += MAS[0]

	d_t0_t3_t5_in = S.Task('d_t0_t3_t5_in', length=1, delay_cost=1)
	S += d_t0_t3_t5_in >= 25
	d_t0_t3_t5_in += MAS_in[3]

	d_t0_t3_t5_mem0 = S.Task('d_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem0 >= 25
	d_t0_t3_t5_mem0 += MM_MEM[0]

	d_t0_t3_t5_mem1 = S.Task('d_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem1 >= 25
	d_t0_t3_t5_mem1 += MM_MEM[1]

	d_t1_t3_t4 = S.Task('d_t1_t3_t4', length=11, delay_cost=1)
	S += d_t1_t3_t4 >= 25
	d_t1_t3_t4 += MM[0]

	d_t2_t2_t3_in = S.Task('d_t2_t2_t3_in', length=1, delay_cost=1)
	S += d_t2_t2_t3_in >= 25
	d_t2_t2_t3_in += MAS_in[2]

	d_t2_t2_t3_mem0 = S.Task('d_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem0 >= 25
	d_t2_t2_t3_mem0 += MAS_MEM[4]

	d_t2_t2_t3_mem1 = S.Task('d_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem1 >= 25
	d_t2_t2_t3_mem1 += MAS_MEM[5]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=3, delay_cost=1)
	S += d_t2_t3_t3 >= 25
	d_t2_t3_t3 += MAS[0]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 25
	d_t3010_in += MAS_in[0]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 25
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 25
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t0_t30_in = S.Task('d_t0_t30_in', length=1, delay_cost=1)
	S += d_t0_t30_in >= 26
	d_t0_t30_in += MAS_in[0]

	d_t0_t30_mem0 = S.Task('d_t0_t30_mem0', length=1, delay_cost=1)
	S += d_t0_t30_mem0 >= 26
	d_t0_t30_mem0 += MM_MEM[0]

	d_t0_t30_mem1 = S.Task('d_t0_t30_mem1', length=1, delay_cost=1)
	S += d_t0_t30_mem1 >= 26
	d_t0_t30_mem1 += MM_MEM[1]

	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 26
	d_t0_t3_t3_in += MAS_in[1]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 26
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 26
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t5 = S.Task('d_t0_t3_t5', length=3, delay_cost=1)
	S += d_t0_t3_t5 >= 26
	d_t0_t3_t5 += MAS[3]

	d_t2_t2_t3 = S.Task('d_t2_t2_t3', length=3, delay_cost=1)
	S += d_t2_t2_t3 >= 26
	d_t2_t2_t3 += MAS[2]

	d_t3010 = S.Task('d_t3010', length=3, delay_cost=1)
	S += d_t3010 >= 26
	d_t3010 += MAS[0]

	d_t4_t3_t2_in = S.Task('d_t4_t3_t2_in', length=1, delay_cost=1)
	S += d_t4_t3_t2_in >= 26
	d_t4_t3_t2_in += MAS_in[2]

	d_t4_t3_t2_mem0 = S.Task('d_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem0 >= 26
	d_t4_t3_t2_mem0 += MAS_MEM[6]

	d_t4_t3_t2_mem1 = S.Task('d_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem1 >= 26
	d_t4_t3_t2_mem1 += MAS_MEM[1]

	d_t0_t30 = S.Task('d_t0_t30', length=3, delay_cost=1)
	S += d_t0_t30 >= 27
	d_t0_t30 += MAS[0]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=3, delay_cost=1)
	S += d_t0_t3_t3 >= 27
	d_t0_t3_t3 += MAS[1]

	d_t2_t3_t4_in = S.Task('d_t2_t3_t4_in', length=1, delay_cost=1)
	S += d_t2_t3_t4_in >= 27
	d_t2_t3_t4_in += MM_in[0]

	d_t2_t3_t4_mem0 = S.Task('d_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem0 >= 27
	d_t2_t3_t4_mem0 += MAS_MEM[6]

	d_t2_t3_t4_mem1 = S.Task('d_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem1 >= 27
	d_t2_t3_t4_mem1 += MAS_MEM[1]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 27
	d_t3011_in += MAS_in[0]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 27
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 27
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t4_t3_t2 = S.Task('d_t4_t3_t2', length=3, delay_cost=1)
	S += d_t4_t3_t2 >= 27
	d_t4_t3_t2 += MAS[2]

	d_t1_t3_t5_in = S.Task('d_t1_t3_t5_in', length=1, delay_cost=1)
	S += d_t1_t3_t5_in >= 28
	d_t1_t3_t5_in += MAS_in[1]

	d_t1_t3_t5_mem0 = S.Task('d_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem0 >= 28
	d_t1_t3_t5_mem0 += MM_MEM[0]

	d_t1_t3_t5_mem1 = S.Task('d_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem1 >= 28
	d_t1_t3_t5_mem1 += MM_MEM[1]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 28
	d_t2_a1_1_in += MAS_in[3]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 28
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 28
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t4 = S.Task('d_t2_t3_t4', length=11, delay_cost=1)
	S += d_t2_t3_t4 >= 28
	d_t2_t3_t4 += MM[0]

	d_t3011 = S.Task('d_t3011', length=3, delay_cost=1)
	S += d_t3011 >= 28
	d_t3011 += MAS[0]

	d_t3_t3_t0_in = S.Task('d_t3_t3_t0_in', length=1, delay_cost=1)
	S += d_t3_t3_t0_in >= 28
	d_t3_t3_t0_in += MM_in[1]

	d_t3_t3_t0_mem0 = S.Task('d_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem0 >= 28
	d_t3_t3_t0_mem0 += MAS_MEM[4]

	d_t3_t3_t0_mem1 = S.Task('d_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem1 >= 28
	d_t3_t3_t0_mem1 += MAS_MEM[1]

	d_t0_t3_t4_in = S.Task('d_t0_t3_t4_in', length=1, delay_cost=1)
	S += d_t0_t3_t4_in >= 29
	d_t0_t3_t4_in += MM_in[1]

	d_t0_t3_t4_mem0 = S.Task('d_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem0 >= 29
	d_t0_t3_t4_mem0 += MAS_MEM[6]

	d_t0_t3_t4_mem1 = S.Task('d_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem1 >= 29
	d_t0_t3_t4_mem1 += MAS_MEM[3]

	d_t1_t30_in = S.Task('d_t1_t30_in', length=1, delay_cost=1)
	S += d_t1_t30_in >= 29
	d_t1_t30_in += MAS_in[2]

	d_t1_t30_mem0 = S.Task('d_t1_t30_mem0', length=1, delay_cost=1)
	S += d_t1_t30_mem0 >= 29
	d_t1_t30_mem0 += MM_MEM[0]

	d_t1_t30_mem1 = S.Task('d_t1_t30_mem1', length=1, delay_cost=1)
	S += d_t1_t30_mem1 >= 29
	d_t1_t30_mem1 += MM_MEM[1]

	d_t1_t3_t5 = S.Task('d_t1_t3_t5', length=3, delay_cost=1)
	S += d_t1_t3_t5 >= 29
	d_t1_t3_t5 += MAS[1]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=3, delay_cost=1)
	S += d_t2_a1_1 >= 29
	d_t2_a1_1 += MAS[3]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 29
	d_t2_t3_t0_in += MM_in[0]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 29
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 29
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t3_t10_in = S.Task('d_t3_t10_in', length=1, delay_cost=1)
	S += d_t3_t10_in >= 29
	d_t3_t10_in += MAS_in[1]

	d_t3_t10_mem0 = S.Task('d_t3_t10_mem0', length=1, delay_cost=1)
	S += d_t3_t10_mem0 >= 29
	d_t3_t10_mem0 += MAS_MEM[4]

	d_t3_t10_mem1 = S.Task('d_t3_t10_mem1', length=1, delay_cost=1)
	S += d_t3_t10_mem1 >= 29
	d_t3_t10_mem1 += MAS_MEM[1]

	d_t3_t3_t0 = S.Task('d_t3_t3_t0', length=11, delay_cost=1)
	S += d_t3_t3_t0 >= 29
	d_t3_t3_t0 += MM[1]

	d_t0_t3_t4 = S.Task('d_t0_t3_t4', length=11, delay_cost=1)
	S += d_t0_t3_t4 >= 30
	d_t0_t3_t4 += MM[1]

	d_t1_t30 = S.Task('d_t1_t30', length=3, delay_cost=1)
	S += d_t1_t30 >= 30
	d_t1_t30 += MAS[2]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=11, delay_cost=1)
	S += d_t2_t3_t0 >= 30
	d_t2_t3_t0 += MM[0]

	d_t3_a1_1_in = S.Task('d_t3_a1_1_in', length=1, delay_cost=1)
	S += d_t3_a1_1_in >= 30
	d_t3_a1_1_in += MAS_in[3]

	d_t3_a1_1_mem0 = S.Task('d_t3_a1_1_mem0', length=1, delay_cost=1)
	S += d_t3_a1_1_mem0 >= 30
	d_t3_a1_1_mem0 += MAS_MEM[0]

	d_t3_a1_1_mem1 = S.Task('d_t3_a1_1_mem1', length=1, delay_cost=1)
	S += d_t3_a1_1_mem1 >= 30
	d_t3_a1_1_mem1 += MAS_MEM[1]

	d_t3_t10 = S.Task('d_t3_t10', length=3, delay_cost=1)
	S += d_t3_t10 >= 30
	d_t3_t10 += MAS[1]

	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	S += d_t4011_in >= 30
	d_t4011_in += MAS_in[2]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 30
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 30
	d_t4011_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 31
	c_t1_t1_t2_in += MAS_in[3]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 31
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 31
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	d_t3_a1_1 = S.Task('d_t3_a1_1', length=3, delay_cost=1)
	S += d_t3_a1_1 >= 31
	d_t3_a1_1 += MAS[3]

	d_t3_t3_t3_in = S.Task('d_t3_t3_t3_in', length=1, delay_cost=1)
	S += d_t3_t3_t3_in >= 31
	d_t3_t3_t3_in += MAS_in[0]

	d_t3_t3_t3_mem0 = S.Task('d_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem0 >= 31
	d_t3_t3_t3_mem0 += MAS_MEM[0]

	d_t3_t3_t3_mem1 = S.Task('d_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem1 >= 31
	d_t3_t3_t3_mem1 += MAS_MEM[1]

	d_t4011 = S.Task('d_t4011', length=3, delay_cost=1)
	S += d_t4011 >= 31
	d_t4011 += MAS[2]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 32
	c_t0_t0_t2_in += MAS_in[3]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 32
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 32
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=3, delay_cost=1)
	S += c_t1_t1_t2 >= 32
	c_t1_t1_t2 += MAS[3]

	d_t3_t3_t1_in = S.Task('d_t3_t3_t1_in', length=1, delay_cost=1)
	S += d_t3_t3_t1_in >= 32
	d_t3_t3_t1_in += MM_in[0]

	d_t3_t3_t1_mem0 = S.Task('d_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem0 >= 32
	d_t3_t3_t1_mem0 += MAS_MEM[0]

	d_t3_t3_t1_mem1 = S.Task('d_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem1 >= 32
	d_t3_t3_t1_mem1 += MAS_MEM[1]

	d_t3_t3_t3 = S.Task('d_t3_t3_t3', length=3, delay_cost=1)
	S += d_t3_t3_t3 >= 32
	d_t3_t3_t3 += MAS[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=3, delay_cost=1)
	S += c_t0_t0_t2 >= 33
	c_t0_t0_t2 += MAS[3]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 33
	c_t0_t20_in += MAS_in[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 33
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 33
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	d_t3_t3_t1 = S.Task('d_t3_t3_t1', length=11, delay_cost=1)
	S += d_t3_t3_t1 >= 33
	d_t3_t3_t1 += MM[0]

	d_t4_t11_in = S.Task('d_t4_t11_in', length=1, delay_cost=1)
	S += d_t4_t11_in >= 33
	d_t4_t11_in += MAS_in[2]

	d_t4_t11_mem0 = S.Task('d_t4_t11_mem0', length=1, delay_cost=1)
	S += d_t4_t11_mem0 >= 33
	d_t4_t11_mem0 += MAS_MEM[0]

	d_t4_t11_mem1 = S.Task('d_t4_t11_mem1', length=1, delay_cost=1)
	S += d_t4_t11_mem1 >= 33
	d_t4_t11_mem1 += MAS_MEM[5]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 34
	c_t0_t0_t3_in += MAS_in[2]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 34
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 34
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t20 = S.Task('c_t0_t20', length=3, delay_cost=1)
	S += c_t0_t20 >= 34
	c_t0_t20 += MAS[1]

	d_t4_t11 = S.Task('d_t4_t11', length=3, delay_cost=1)
	S += d_t4_t11 >= 34
	d_t4_t11 += MAS[2]

	d_t4_t3_t1_in = S.Task('d_t4_t3_t1_in', length=1, delay_cost=1)
	S += d_t4_t3_t1_in >= 34
	d_t4_t3_t1_in += MM_in[0]

	d_t4_t3_t1_mem0 = S.Task('d_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem0 >= 34
	d_t4_t3_t1_mem0 += MAS_MEM[0]

	d_t4_t3_t1_mem1 = S.Task('d_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem1 >= 34
	d_t4_t3_t1_mem1 += MAS_MEM[5]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=3, delay_cost=1)
	S += c_t0_t0_t3 >= 35
	c_t0_t0_t3 += MAS[2]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 35
	c_t1_t0_t2_in += MAS_in[2]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 35
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 35
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	d_t3_t11_in = S.Task('d_t3_t11_in', length=1, delay_cost=1)
	S += d_t3_t11_in >= 35
	d_t3_t11_in += MAS_in[0]

	d_t3_t11_mem0 = S.Task('d_t3_t11_mem0', length=1, delay_cost=1)
	S += d_t3_t11_mem0 >= 35
	d_t3_t11_mem0 += MAS_MEM[0]

	d_t3_t11_mem1 = S.Task('d_t3_t11_mem1', length=1, delay_cost=1)
	S += d_t3_t11_mem1 >= 35
	d_t3_t11_mem1 += MAS_MEM[1]

	d_t4_t3_t1 = S.Task('d_t4_t3_t1', length=11, delay_cost=1)
	S += d_t4_t3_t1 >= 35
	d_t4_t3_t1 += MM[0]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=3, delay_cost=1)
	S += c_t1_t0_t2 >= 36
	c_t1_t0_t2 += MAS[2]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 36
	c_t1_t21_in += MAS_in[2]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 36
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 36
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	d_t3_a1_0_in = S.Task('d_t3_a1_0_in', length=1, delay_cost=1)
	S += d_t3_a1_0_in >= 36
	d_t3_a1_0_in += MAS_in[0]

	d_t3_a1_0_mem0 = S.Task('d_t3_a1_0_mem0', length=1, delay_cost=1)
	S += d_t3_a1_0_mem0 >= 36
	d_t3_a1_0_mem0 += MAS_MEM[0]

	d_t3_a1_0_mem1 = S.Task('d_t3_a1_0_mem1', length=1, delay_cost=1)
	S += d_t3_a1_0_mem1 >= 36
	d_t3_a1_0_mem1 += MAS_MEM[1]

	d_t3_t11 = S.Task('d_t3_t11', length=3, delay_cost=1)
	S += d_t3_t11 >= 36
	d_t3_t11 += MAS[0]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 37
	c_t0_t0_t4_in += MM_in[1]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 37
	c_t0_t0_t4_mem0 += MAS_MEM[6]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 37
	c_t0_t0_t4_mem1 += MAS_MEM[5]

	c_t1_t21 = S.Task('c_t1_t21', length=3, delay_cost=1)
	S += c_t1_t21 >= 37
	c_t1_t21 += MAS[2]

	d_t3_a1_0 = S.Task('d_t3_a1_0', length=3, delay_cost=1)
	S += d_t3_a1_0 >= 37
	d_t3_a1_0 += MAS[0]

	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	S += d_t5010_in >= 37
	d_t5010_in += MAS_in[0]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 37
	d_t5010_mem0 += MAIN_MEM_r[0]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 37
	d_t5010_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=11, delay_cost=1)
	S += c_t0_t0_t4 >= 38
	c_t0_t0_t4 += MM[1]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 38
	c_t0_t30_in += MAS_in[2]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 38
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 38
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	d_t5010 = S.Task('d_t5010', length=3, delay_cost=1)
	S += d_t5010 >= 38
	d_t5010 += MAS[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 39
	c_t0_t1_t2_in += MAS_in[3]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 39
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 39
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t30 = S.Task('c_t0_t30', length=3, delay_cost=1)
	S += c_t0_t30 >= 39
	c_t0_t30 += MAS[2]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=3, delay_cost=1)
	S += c_t0_t1_t2 >= 40
	c_t0_t1_t2 += MAS[3]

	d_t2_t30_in = S.Task('d_t2_t30_in', length=1, delay_cost=1)
	S += d_t2_t30_in >= 40
	d_t2_t30_in += MAS_in[2]

	d_t2_t30_mem0 = S.Task('d_t2_t30_mem0', length=1, delay_cost=1)
	S += d_t2_t30_mem0 >= 40
	d_t2_t30_mem0 += MM_MEM[0]

	d_t2_t30_mem1 = S.Task('d_t2_t30_mem1', length=1, delay_cost=1)
	S += d_t2_t30_mem1 >= 40
	d_t2_t30_mem1 += MM_MEM[3]

	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	S += d_t5001_in >= 40
	d_t5001_in += MAS_in[3]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 40
	d_t5001_mem0 += MAIN_MEM_r[0]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 40
	d_t5001_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 41
	c_t0_t1_t1_in += MM_in[1]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 41
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 41
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 41
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 41
	c_t0_t4_t0_mem0 += MAS_MEM[2]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 41
	c_t0_t4_t0_mem1 += MAS_MEM[5]

	d_t2_t30 = S.Task('d_t2_t30', length=3, delay_cost=1)
	S += d_t2_t30 >= 41
	d_t2_t30 += MAS[2]

	d_t2_t3_t5_in = S.Task('d_t2_t3_t5_in', length=1, delay_cost=1)
	S += d_t2_t3_t5_in >= 41
	d_t2_t3_t5_in += MAS_in[1]

	d_t2_t3_t5_mem0 = S.Task('d_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem0 >= 41
	d_t2_t3_t5_mem0 += MM_MEM[0]

	d_t2_t3_t5_mem1 = S.Task('d_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem1 >= 41
	d_t2_t3_t5_mem1 += MM_MEM[3]

	d_t5001 = S.Task('d_t5001', length=3, delay_cost=1)
	S += d_t5001 >= 41
	d_t5001 += MAS[3]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=11, delay_cost=1)
	S += c_t0_t1_t1 >= 42
	c_t0_t1_t1 += MM[1]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=11, delay_cost=1)
	S += c_t0_t4_t0 >= 42
	c_t0_t4_t0 += MM[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 42
	c_t1_t20_in += MAS_in[1]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 42
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 42
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t5 = S.Task('d_t2_t3_t5', length=3, delay_cost=1)
	S += d_t2_t3_t5 >= 42
	d_t2_t3_t5 += MAS[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 43
	c_t0_t31_in += MAS_in[1]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 43
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 43
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t20 = S.Task('c_t1_t20', length=3, delay_cost=1)
	S += c_t1_t20 >= 43
	c_t1_t20 += MAS[1]

	c_t0_t31 = S.Task('c_t0_t31', length=3, delay_cost=1)
	S += c_t0_t31 >= 44
	c_t0_t31 += MAS[1]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 44
	c_t1_t0_t3_in += MAS_in[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 44
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 44
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=3, delay_cost=1)
	S += c_t1_t0_t3 >= 45
	c_t1_t0_t3 += MAS[1]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 45
	c_t1_t4_t2_in += MAS_in[1]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 45
	c_t1_t4_t2_mem0 += MAS_MEM[2]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 45
	c_t1_t4_t2_mem1 += MAS_MEM[5]

	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	S += d_t4010_in >= 45
	d_t4010_in += MAS_in[0]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 45
	d_t4010_mem0 += MAIN_MEM_r[0]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 45
	d_t4010_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 46
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 46
	c_t0_t4_t3_mem0 += MAS_MEM[4]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 46
	c_t0_t4_t3_mem1 += MAS_MEM[3]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 46
	c_t1_t1_t0_in += MM_in[1]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 46
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 46
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=3, delay_cost=1)
	S += c_t1_t4_t2 >= 46
	c_t1_t4_t2 += MAS[1]

	d_t4010 = S.Task('d_t4010', length=3, delay_cost=1)
	S += d_t4010 >= 46
	d_t4010 += MAS[0]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 47
	c_t0_t21_in += MAS_in[0]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 47
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 47
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=3, delay_cost=1)
	S += c_t0_t4_t3 >= 47
	c_t0_t4_t3 += MAS[1]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 47
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 47
	c_t1_t0_t4_mem0 += MAS_MEM[4]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 47
	c_t1_t0_t4_mem1 += MAS_MEM[3]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=11, delay_cost=1)
	S += c_t1_t1_t0 >= 47
	c_t1_t1_t0 += MM[1]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 48
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 48
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 48
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t21 = S.Task('c_t0_t21', length=3, delay_cost=1)
	S += c_t0_t21 >= 48
	c_t0_t21 += MAS[0]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=11, delay_cost=1)
	S += c_t1_t0_t4 >= 48
	c_t1_t0_t4 += MM[0]

	d_t4_t3_t0_in = S.Task('d_t4_t3_t0_in', length=1, delay_cost=1)
	S += d_t4_t3_t0_in >= 48
	d_t4_t3_t0_in += MM_in[1]

	d_t4_t3_t0_mem0 = S.Task('d_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem0 >= 48
	d_t4_t3_t0_mem0 += MAS_MEM[6]

	d_t4_t3_t0_mem1 = S.Task('d_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem1 >= 48
	d_t4_t3_t0_mem1 += MAS_MEM[1]

	d_t4_t3_t3_in = S.Task('d_t4_t3_t3_in', length=1, delay_cost=1)
	S += d_t4_t3_t3_in >= 48
	d_t4_t3_t3_in += MAS_in[2]

	d_t4_t3_t3_mem0 = S.Task('d_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem0 >= 48
	d_t4_t3_t3_mem0 += MAS_MEM[0]

	d_t4_t3_t3_mem1 = S.Task('d_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem1 >= 48
	d_t4_t3_t3_mem1 += MAS_MEM[5]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=3, delay_cost=1)
	S += c_t0_t1_t3 >= 49
	c_t0_t1_t3 += MAS[0]

	d_t4_a1_0_in = S.Task('d_t4_a1_0_in', length=1, delay_cost=1)
	S += d_t4_a1_0_in >= 49
	d_t4_a1_0_in += MAS_in[0]

	d_t4_a1_0_mem0 = S.Task('d_t4_a1_0_mem0', length=1, delay_cost=1)
	S += d_t4_a1_0_mem0 >= 49
	d_t4_a1_0_mem0 += MAS_MEM[0]

	d_t4_a1_0_mem1 = S.Task('d_t4_a1_0_mem1', length=1, delay_cost=1)
	S += d_t4_a1_0_mem1 >= 49
	d_t4_a1_0_mem1 += MAS_MEM[5]

	d_t4_a1_1_in = S.Task('d_t4_a1_1_in', length=1, delay_cost=1)
	S += d_t4_a1_1_in >= 49
	d_t4_a1_1_in += MAS_in[1]

	d_t4_a1_1_mem0 = S.Task('d_t4_a1_1_mem0', length=1, delay_cost=1)
	S += d_t4_a1_1_mem0 >= 49
	d_t4_a1_1_mem0 += MAS_MEM[4]

	d_t4_a1_1_mem1 = S.Task('d_t4_a1_1_mem1', length=1, delay_cost=1)
	S += d_t4_a1_1_mem1 >= 49
	d_t4_a1_1_mem1 += MAS_MEM[1]

	d_t4_t3_t0 = S.Task('d_t4_t3_t0', length=11, delay_cost=1)
	S += d_t4_t3_t0 >= 49
	d_t4_t3_t0 += MM[1]

	d_t4_t3_t3 = S.Task('d_t4_t3_t3', length=3, delay_cost=1)
	S += d_t4_t3_t3 >= 49
	d_t4_t3_t3 += MAS[2]

	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	S += d_t5011_in >= 49
	d_t5011_in += MAS_in[2]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 49
	d_t5011_mem0 += MAIN_MEM_r[0]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 49
	d_t5011_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 50
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 50
	c_t0_t4_t1_mem0 += MAS_MEM[0]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 50
	c_t0_t4_t1_mem1 += MAS_MEM[3]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 50
	c_t1_t0_t0_in += MM_in[1]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 50
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 50
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	d_t4_a1_0 = S.Task('d_t4_a1_0', length=3, delay_cost=1)
	S += d_t4_a1_0 >= 50
	d_t4_a1_0 += MAS[0]

	d_t4_a1_1 = S.Task('d_t4_a1_1', length=3, delay_cost=1)
	S += d_t4_a1_1 >= 50
	d_t4_a1_1 += MAS[1]

	d_t4_t10_in = S.Task('d_t4_t10_in', length=1, delay_cost=1)
	S += d_t4_t10_in >= 50
	d_t4_t10_in += MAS_in[0]

	d_t4_t10_mem0 = S.Task('d_t4_t10_mem0', length=1, delay_cost=1)
	S += d_t4_t10_mem0 >= 50
	d_t4_t10_mem0 += MAS_MEM[6]

	d_t4_t10_mem1 = S.Task('d_t4_t10_mem1', length=1, delay_cost=1)
	S += d_t4_t10_mem1 >= 50
	d_t4_t10_mem1 += MAS_MEM[1]

	d_t5011 = S.Task('d_t5011', length=3, delay_cost=1)
	S += d_t5011 >= 50
	d_t5011 += MAS[2]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 51
	c_t0_t1_t4_in += MM_in[1]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 51
	c_t0_t1_t4_mem0 += MAS_MEM[6]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 51
	c_t0_t1_t4_mem1 += MAS_MEM[1]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=11, delay_cost=1)
	S += c_t0_t4_t1 >= 51
	c_t0_t4_t1 += MM[0]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=11, delay_cost=1)
	S += c_t1_t0_t0 >= 51
	c_t1_t0_t0 += MM[1]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 51
	c_t1_t1_t3_in += MAS_in[1]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 51
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 51
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	d_t4_t10 = S.Task('d_t4_t10', length=3, delay_cost=1)
	S += d_t4_t10 >= 51
	d_t4_t10 += MAS[0]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=11, delay_cost=1)
	S += c_t0_t1_t4 >= 52
	c_t0_t1_t4 += MM[1]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=3, delay_cost=1)
	S += c_t1_t1_t3 >= 52
	c_t1_t1_t3 += MAS[1]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 52
	c_t1_t31_in += MAS_in[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 52
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 52
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	d_t5_a1_1_in = S.Task('d_t5_a1_1_in', length=1, delay_cost=1)
	S += d_t5_a1_1_in >= 52
	d_t5_a1_1_in += MAS_in[2]

	d_t5_a1_1_mem0 = S.Task('d_t5_a1_1_mem0', length=1, delay_cost=1)
	S += d_t5_a1_1_mem0 >= 52
	d_t5_a1_1_mem0 += MAS_MEM[4]

	d_t5_a1_1_mem1 = S.Task('d_t5_a1_1_mem1', length=1, delay_cost=1)
	S += d_t5_a1_1_mem1 >= 52
	d_t5_a1_1_mem1 += MAS_MEM[1]

	d_t5_t3_t1_in = S.Task('d_t5_t3_t1_in', length=1, delay_cost=1)
	S += d_t5_t3_t1_in >= 52
	d_t5_t3_t1_in += MM_in[0]

	d_t5_t3_t1_mem0 = S.Task('d_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem0 >= 52
	d_t5_t3_t1_mem0 += MAS_MEM[6]

	d_t5_t3_t1_mem1 = S.Task('d_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem1 >= 52
	d_t5_t3_t1_mem1 += MAS_MEM[5]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 53
	c_t0_t4_t2_in += MAS_in[2]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 53
	c_t0_t4_t2_mem0 += MAS_MEM[2]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 53
	c_t0_t4_t2_mem1 += MAS_MEM[1]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 53
	c_t1_t0_t1_in += MM_in[1]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 53
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 53
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=3, delay_cost=1)
	S += c_t1_t31 >= 53
	c_t1_t31 += MAS[1]

	d_t5_a1_1 = S.Task('d_t5_a1_1', length=3, delay_cost=1)
	S += d_t5_a1_1 >= 53
	d_t5_a1_1 += MAS[2]

	d_t5_t11_in = S.Task('d_t5_t11_in', length=1, delay_cost=1)
	S += d_t5_t11_in >= 53
	d_t5_t11_in += MAS_in[3]

	d_t5_t11_mem0 = S.Task('d_t5_t11_mem0', length=1, delay_cost=1)
	S += d_t5_t11_mem0 >= 53
	d_t5_t11_mem0 += MAS_MEM[6]

	d_t5_t11_mem1 = S.Task('d_t5_t11_mem1', length=1, delay_cost=1)
	S += d_t5_t11_mem1 >= 53
	d_t5_t11_mem1 += MAS_MEM[5]

	d_t5_t3_t1 = S.Task('d_t5_t3_t1', length=11, delay_cost=1)
	S += d_t5_t3_t1 >= 53
	d_t5_t3_t1 += MM[0]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 54
	c_t0_t1_t0_in += MM_in[1]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 54
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 54
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=3, delay_cost=1)
	S += c_t0_t4_t2 >= 54
	c_t0_t4_t2 += MAS[2]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=11, delay_cost=1)
	S += c_t1_t0_t1 >= 54
	c_t1_t0_t1 += MM[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 54
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 54
	c_t1_t1_t4_mem0 += MAS_MEM[6]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 54
	c_t1_t1_t4_mem1 += MAS_MEM[3]

	d_t5_t11 = S.Task('d_t5_t11', length=3, delay_cost=1)
	S += d_t5_t11 >= 54
	d_t5_t11 += MAS[3]

	d_t5_t3_t3_in = S.Task('d_t5_t3_t3_in', length=1, delay_cost=1)
	S += d_t5_t3_t3_in >= 54
	d_t5_t3_t3_in += MAS_in[1]

	d_t5_t3_t3_mem0 = S.Task('d_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem0 >= 54
	d_t5_t3_t3_mem0 += MAS_MEM[0]

	d_t5_t3_t3_mem1 = S.Task('d_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem1 >= 54
	d_t5_t3_t3_mem1 += MAS_MEM[5]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=11, delay_cost=1)
	S += c_t0_t1_t0 >= 55
	c_t0_t1_t0 += MM[1]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 55
	c_t1_t1_t1_in += MM_in[1]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 55
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 55
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=11, delay_cost=1)
	S += c_t1_t1_t4 >= 55
	c_t1_t1_t4 += MM[0]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 55
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 55
	c_t1_t4_t1_mem0 += MAS_MEM[4]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 55
	c_t1_t4_t1_mem1 += MAS_MEM[3]

	d_t5_a1_0_in = S.Task('d_t5_a1_0_in', length=1, delay_cost=1)
	S += d_t5_a1_0_in >= 55
	d_t5_a1_0_in += MAS_in[1]

	d_t5_a1_0_mem0 = S.Task('d_t5_a1_0_mem0', length=1, delay_cost=1)
	S += d_t5_a1_0_mem0 >= 55
	d_t5_a1_0_mem0 += MAS_MEM[0]

	d_t5_a1_0_mem1 = S.Task('d_t5_a1_0_mem1', length=1, delay_cost=1)
	S += d_t5_a1_0_mem1 >= 55
	d_t5_a1_0_mem1 += MAS_MEM[5]

	d_t5_t3_t3 = S.Task('d_t5_t3_t3', length=3, delay_cost=1)
	S += d_t5_t3_t3 >= 55
	d_t5_t3_t3 += MAS[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=11, delay_cost=1)
	S += c_t1_t1_t1 >= 56
	c_t1_t1_t1 += MM[1]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 56
	c_t1_t30_in += MAS_in[2]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 56
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 56
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=11, delay_cost=1)
	S += c_t1_t4_t1 >= 56
	c_t1_t4_t1 += MM[0]

	d_t5_a1_0 = S.Task('d_t5_a1_0', length=3, delay_cost=1)
	S += d_t5_a1_0 >= 56
	d_t5_a1_0 += MAS[1]

	c_t1_t30 = S.Task('c_t1_t30', length=3, delay_cost=1)
	S += c_t1_t30 >= 57
	c_t1_t30 += MAS[2]

	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	S += d_t5000_in >= 57
	d_t5000_in += MAS_in[3]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 57
	d_t5000_mem0 += MAIN_MEM_r[0]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 57
	d_t5000_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 58
	c_t0_t0_t1_in += MM_in[1]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 58
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 58
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	d_t5000 = S.Task('d_t5000', length=3, delay_cost=1)
	S += d_t5000 >= 58
	d_t5000 += MAS[3]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 59
	c_t0_t0_t0_in += MM_in[1]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 59
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 59
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=11, delay_cost=1)
	S += c_t0_t0_t1 >= 59
	c_t0_t0_t1 += MM[1]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 59
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 59
	c_t1_t4_t0_mem0 += MAS_MEM[2]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 59
	c_t1_t4_t0_mem1 += MAS_MEM[5]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 59
	c_t1_t4_t3_in += MAS_in[2]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 59
	c_t1_t4_t3_mem0 += MAS_MEM[4]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 59
	c_t1_t4_t3_mem1 += MAS_MEM[3]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=11, delay_cost=1)
	S += c_t0_t0_t0 >= 60
	c_t0_t0_t0 += MM[1]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=11, delay_cost=1)
	S += c_t1_t4_t0 >= 60
	c_t1_t4_t0 += MM[0]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=3, delay_cost=1)
	S += c_t1_t4_t3 >= 60
	c_t1_t4_t3 += MAS[2]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 60
	c_t4111_in += MAS_in[0]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 60
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 60
	c_t4111_mem1 += MAIN_MEM_r[1]

	d_t5_t3_t0_in = S.Task('d_t5_t3_t0_in', length=1, delay_cost=1)
	S += d_t5_t3_t0_in >= 60
	d_t5_t3_t0_in += MM_in[0]

	d_t5_t3_t0_mem0 = S.Task('d_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem0 >= 60
	d_t5_t3_t0_mem0 += MAS_MEM[6]

	d_t5_t3_t0_mem1 = S.Task('d_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem1 >= 60
	d_t5_t3_t0_mem1 += MAS_MEM[1]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 61
	c_t2_t1_t3_in += MAS_in[2]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 61
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 61
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t4111 = S.Task('c_t4111', length=3, delay_cost=1)
	S += c_t4111 >= 61
	c_t4111 += MAS[0]

	d_t5_t3_t0 = S.Task('d_t5_t3_t0', length=11, delay_cost=1)
	S += d_t5_t3_t0 >= 61
	d_t5_t3_t0 += MM[0]

	d_t5_t3_t2_in = S.Task('d_t5_t3_t2_in', length=1, delay_cost=1)
	S += d_t5_t3_t2_in >= 61
	d_t5_t3_t2_in += MAS_in[0]

	d_t5_t3_t2_mem0 = S.Task('d_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem0 >= 61
	d_t5_t3_t2_mem0 += MAS_MEM[6]

	d_t5_t3_t2_mem1 = S.Task('d_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem1 >= 61
	d_t5_t3_t2_mem1 += MAS_MEM[7]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=3, delay_cost=1)
	S += c_t2_t1_t3 >= 62
	c_t2_t1_t3 += MAS[2]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 62
	c_t3111_in += MAS_in[3]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 62
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 62
	c_t3111_mem1 += MAIN_MEM_r[1]

	d_t5_t10_in = S.Task('d_t5_t10_in', length=1, delay_cost=1)
	S += d_t5_t10_in >= 62
	d_t5_t10_in += MAS_in[1]

	d_t5_t10_mem0 = S.Task('d_t5_t10_mem0', length=1, delay_cost=1)
	S += d_t5_t10_mem0 >= 62
	d_t5_t10_mem0 += MAS_MEM[6]

	d_t5_t10_mem1 = S.Task('d_t5_t10_mem1', length=1, delay_cost=1)
	S += d_t5_t10_mem1 >= 62
	d_t5_t10_mem1 += MAS_MEM[1]

	d_t5_t3_t2 = S.Task('d_t5_t3_t2', length=3, delay_cost=1)
	S += d_t5_t3_t2 >= 62
	d_t5_t3_t2 += MAS[0]

	c_t3111 = S.Task('c_t3111', length=3, delay_cost=1)
	S += c_t3111 >= 63
	c_t3111 += MAS[3]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 63
	c_t4011_in += MAS_in[0]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 63
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 63
	c_t4011_mem1 += MAIN_MEM_r[1]

	d_t5_t10 = S.Task('d_t5_t10', length=3, delay_cost=1)
	S += d_t5_t10 >= 63
	d_t5_t10 += MAS[1]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 64
	c_t1_t00_in += MAS_in[2]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 64
	c_t1_t00_mem0 += MM_MEM[2]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 64
	c_t1_t00_mem1 += MM_MEM[3]

	c_t4011 = S.Task('c_t4011', length=3, delay_cost=1)
	S += c_t4011 >= 64
	c_t4011 += MAS[0]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 64
	c_t4101_in += MAS_in[0]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 64
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 64
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 65
	c_t0_t10_in += MAS_in[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 65
	c_t0_t10_mem0 += MM_MEM[2]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 65
	c_t0_t10_mem1 += MM_MEM[3]

	c_t1_t00 = S.Task('c_t1_t00', length=3, delay_cost=1)
	S += c_t1_t00 >= 65
	c_t1_t00 += MAS[2]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 65
	c_t3000_in += MAS_in[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 65
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 65
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t4101 = S.Task('c_t4101', length=3, delay_cost=1)
	S += c_t4101 >= 65
	c_t4101 += MAS[0]

	c_t0_t10 = S.Task('c_t0_t10', length=3, delay_cost=1)
	S += c_t0_t10 >= 66
	c_t0_t10 += MAS[1]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 66
	c_t0_t1_t5_in += MAS_in[1]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 66
	c_t0_t1_t5_mem0 += MM_MEM[2]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 66
	c_t0_t1_t5_mem1 += MM_MEM[3]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 66
	c_t2_t1_t0_in += MM_in[1]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 66
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 66
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t3000 = S.Task('c_t3000', length=3, delay_cost=1)
	S += c_t3000 >= 66
	c_t3000 += MAS[3]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 66
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 66
	c_t4_t1_t1_mem0 += MAS_MEM[0]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 66
	c_t4_t1_t1_mem1 += MAS_MEM[1]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=3, delay_cost=1)
	S += c_t0_t1_t5 >= 67
	c_t0_t1_t5 += MAS[1]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 67
	c_t1_t10_in += MAS_in[3]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 67
	c_t1_t10_mem0 += MM_MEM[2]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 67
	c_t1_t10_mem1 += MM_MEM[3]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=11, delay_cost=1)
	S += c_t2_t1_t0 >= 67
	c_t2_t1_t0 += MM[1]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 67
	c_t3110_in += MAS_in[1]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 67
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 67
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=11, delay_cost=1)
	S += c_t4_t1_t1 >= 67
	c_t4_t1_t1 += MM[0]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 67
	c_t4_t31_in += MAS_in[2]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 67
	c_t4_t31_mem0 += MAS_MEM[0]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 67
	c_t4_t31_mem1 += MAS_MEM[1]

	c_t1_t10 = S.Task('c_t1_t10', length=3, delay_cost=1)
	S += c_t1_t10 >= 68
	c_t1_t10 += MAS[3]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 68
	c_t1_t1_t5_in += MAS_in[2]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 68
	c_t1_t1_t5_mem0 += MM_MEM[2]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 68
	c_t1_t1_t5_mem1 += MM_MEM[3]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 68
	c_t2_t0_t1_in += MM_in[1]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 68
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 68
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t3110 = S.Task('c_t3110', length=3, delay_cost=1)
	S += c_t3110 >= 68
	c_t3110 += MAS[1]

	c_t4_t31 = S.Task('c_t4_t31', length=3, delay_cost=1)
	S += c_t4_t31 >= 68
	c_t4_t31 += MAS[2]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 69
	c_t1_t0_t5_in += MAS_in[2]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 69
	c_t1_t0_t5_mem0 += MM_MEM[2]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 69
	c_t1_t0_t5_mem1 += MM_MEM[3]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=3, delay_cost=1)
	S += c_t1_t1_t5 >= 69
	c_t1_t1_t5 += MAS[2]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=11, delay_cost=1)
	S += c_t2_t0_t1 >= 69
	c_t2_t0_t1 += MM[1]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 69
	c_t3100_in += MAS_in[0]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 69
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 69
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 70
	c_t0_t0_t5_in += MAS_in[2]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 70
	c_t0_t0_t5_mem0 += MM_MEM[2]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 70
	c_t0_t0_t5_mem1 += MM_MEM[3]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=3, delay_cost=1)
	S += c_t1_t0_t5 >= 70
	c_t1_t0_t5 += MAS[2]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 70
	c_t2_t0_t2_in += MAS_in[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 70
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 70
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t3100 = S.Task('c_t3100', length=3, delay_cost=1)
	S += c_t3100 >= 70
	c_t3100 += MAS[0]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 70
	c_t3_t1_t3_in += MAS_in[3]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 70
	c_t3_t1_t3_mem0 += MAS_MEM[2]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 70
	c_t3_t1_t3_mem1 += MAS_MEM[7]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 71
	c_t0_t00_in += MAS_in[2]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 71
	c_t0_t00_mem0 += MM_MEM[2]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 71
	c_t0_t00_mem1 += MM_MEM[3]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=3, delay_cost=1)
	S += c_t0_t0_t5 >= 71
	c_t0_t0_t5 += MAS[2]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=3, delay_cost=1)
	S += c_t2_t0_t2 >= 71
	c_t2_t0_t2 += MAS[0]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 71
	c_t3001_in += MAS_in[1]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 71
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 71
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=3, delay_cost=1)
	S += c_t3_t1_t3 >= 71
	c_t3_t1_t3 += MAS[3]

	c_t0_t00 = S.Task('c_t0_t00', length=3, delay_cost=1)
	S += c_t0_t00 >= 72
	c_t0_t00 += MAS[2]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 72
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 72
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 72
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=3, delay_cost=1)
	S += c_t3001 >= 72
	c_t3001 += MAS[1]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 72
	c_t3_t0_t0_in += MM_in[1]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 72
	c_t3_t0_t0_mem0 += MAS_MEM[6]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 72
	c_t3_t0_t0_mem1 += MAS_MEM[1]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 72
	c_t3_t30_in += MAS_in[2]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 72
	c_t3_t30_mem0 += MAS_MEM[0]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 72
	c_t3_t30_mem1 += MAS_MEM[3]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=11, delay_cost=1)
	S += c_t2_t0_t0 >= 73
	c_t2_t0_t0 += MM[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 73
	c_t2_t0_t3_in += MAS_in[1]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 73
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 73
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=11, delay_cost=1)
	S += c_t3_t0_t0 >= 73
	c_t3_t0_t0 += MM[1]

	c_t3_t30 = S.Task('c_t3_t30', length=3, delay_cost=1)
	S += c_t3_t30 >= 73
	c_t3_t30 += MAS[2]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=3, delay_cost=1)
	S += c_t2_t0_t3 >= 74
	c_t2_t0_t3 += MAS[1]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 74
	c_t3010_in += MAS_in[1]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 74
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 74
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 74
	c_t3_t0_t2_in += MAS_in[2]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 74
	c_t3_t0_t2_mem0 += MAS_MEM[6]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 74
	c_t3_t0_t2_mem1 += MAS_MEM[3]

	c_t3010 = S.Task('c_t3010', length=3, delay_cost=1)
	S += c_t3010 >= 75
	c_t3010 += MAS[1]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=3, delay_cost=1)
	S += c_t3_t0_t2 >= 75
	c_t3_t0_t2 += MAS[2]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 75
	c_t5001_in += MAS_in[2]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 75
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 75
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 76
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 76
	c_t2_t0_t4_mem0 += MAS_MEM[0]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 76
	c_t2_t0_t4_mem1 += MAS_MEM[3]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 76
	c_t2_t20_in += MAS_in[3]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 76
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 76
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t5001 = S.Task('c_t5001', length=3, delay_cost=1)
	S += c_t5001 >= 76
	c_t5001 += MAS[2]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=11, delay_cost=1)
	S += c_t2_t0_t4 >= 77
	c_t2_t0_t4 += MM[0]

	c_t2_t20 = S.Task('c_t2_t20', length=3, delay_cost=1)
	S += c_t2_t20 >= 77
	c_t2_t20 += MAS[3]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 77
	c_t3_t20_in += MAS_in[2]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 77
	c_t3_t20_mem0 += MAS_MEM[6]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 77
	c_t3_t20_mem1 += MAS_MEM[3]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 77
	c_t4110_in += MAS_in[0]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 77
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 77
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 78
	c_t2_t1_t2_in += MAS_in[0]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 78
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 78
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 78
	c_t3_t1_t0_in += MM_in[1]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 78
	c_t3_t1_t0_mem0 += MAS_MEM[2]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 78
	c_t3_t1_t0_mem1 += MAS_MEM[3]

	c_t3_t20 = S.Task('c_t3_t20', length=3, delay_cost=1)
	S += c_t3_t20 >= 78
	c_t3_t20 += MAS[2]

	c_t4110 = S.Task('c_t4110', length=3, delay_cost=1)
	S += c_t4110 >= 78
	c_t4110 += MAS[0]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=3, delay_cost=1)
	S += c_t2_t1_t2 >= 79
	c_t2_t1_t2 += MAS[0]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=11, delay_cost=1)
	S += c_t3_t1_t0 >= 79
	c_t3_t1_t0 += MM[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 79
	c_t4010_in += MAS_in[0]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 79
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 79
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 80
	c_t4001_in += MAS_in[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 80
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 80
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4010 = S.Task('c_t4010', length=3, delay_cost=1)
	S += c_t4010 >= 80
	c_t4010 += MAS[0]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 80
	c_t4_t1_t3_in += MAS_in[0]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 80
	c_t4_t1_t3_mem0 += MAS_MEM[0]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 80
	c_t4_t1_t3_mem1 += MAS_MEM[1]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 81
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 81
	c_t2_t1_t4_mem0 += MAS_MEM[0]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 81
	c_t2_t1_t4_mem1 += MAS_MEM[5]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 81
	c_t4000_in += MAS_in[0]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 81
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 81
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4001 = S.Task('c_t4001', length=3, delay_cost=1)
	S += c_t4001 >= 81
	c_t4001 += MAS[1]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=3, delay_cost=1)
	S += c_t4_t1_t3 >= 81
	c_t4_t1_t3 += MAS[0]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=11, delay_cost=1)
	S += c_t2_t1_t4 >= 82
	c_t2_t1_t4 += MM[0]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 82
	c_t2_t31_in += MAS_in[1]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 82
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 82
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t4000 = S.Task('c_t4000', length=3, delay_cost=1)
	S += c_t4000 >= 82
	c_t4000 += MAS[0]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 82
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 82
	c_t4_t1_t0_mem0 += MAS_MEM[0]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 82
	c_t4_t1_t0_mem1 += MAS_MEM[1]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 83
	c_t2_t0_t5_in += MAS_in[3]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 83
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 83
	c_t2_t0_t5_mem1 += MM_MEM[3]

	c_t2_t31 = S.Task('c_t2_t31', length=3, delay_cost=1)
	S += c_t2_t31 >= 83
	c_t2_t31 += MAS[1]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=11, delay_cost=1)
	S += c_t4_t1_t0 >= 83
	c_t4_t1_t0 += MM[0]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 83
	c_t4_t1_t2_in += MAS_in[1]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 83
	c_t4_t1_t2_mem0 += MAS_MEM[0]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 83
	c_t4_t1_t2_mem1 += MAS_MEM[1]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 83
	c_t5000_in += MAS_in[0]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 83
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 83
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 84
	c_t2_t00_in += MAS_in[3]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 84
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 84
	c_t2_t00_mem1 += MM_MEM[3]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=3, delay_cost=1)
	S += c_t2_t0_t5 >= 84
	c_t2_t0_t5 += MAS[3]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 84
	c_t3011_in += MAS_in[2]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 84
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 84
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 84
	c_t4_t0_t2_in += MAS_in[1]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 84
	c_t4_t0_t2_mem0 += MAS_MEM[0]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 84
	c_t4_t0_t2_mem1 += MAS_MEM[3]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=3, delay_cost=1)
	S += c_t4_t1_t2 >= 84
	c_t4_t1_t2 += MAS[1]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 84
	c_t4_t21_in += MAS_in[0]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 84
	c_t4_t21_mem0 += MAS_MEM[2]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 84
	c_t4_t21_mem1 += MAS_MEM[1]

	c_t5000 = S.Task('c_t5000', length=3, delay_cost=1)
	S += c_t5000 >= 84
	c_t5000 += MAS[0]

	c_t2_t00 = S.Task('c_t2_t00', length=3, delay_cost=1)
	S += c_t2_t00 >= 85
	c_t2_t00 += MAS[3]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 85
	c_t2_t30_in += MAS_in[0]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 85
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 85
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t3011 = S.Task('c_t3011', length=3, delay_cost=1)
	S += c_t3011 >= 85
	c_t3011 += MAS[2]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=3, delay_cost=1)
	S += c_t4_t0_t2 >= 85
	c_t4_t0_t2 += MAS[1]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 85
	c_t4_t20_in += MAS_in[2]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 85
	c_t4_t20_mem0 += MAS_MEM[0]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 85
	c_t4_t20_mem1 += MAS_MEM[1]

	c_t4_t21 = S.Task('c_t4_t21', length=3, delay_cost=1)
	S += c_t4_t21 >= 85
	c_t4_t21 += MAS[0]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 86
	c_t2_t21_in += MAS_in[0]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 86
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 86
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t2_t30 = S.Task('c_t2_t30', length=3, delay_cost=1)
	S += c_t2_t30 >= 86
	c_t2_t30 += MAS[0]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 86
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 86
	c_t4_t0_t1_mem0 += MAS_MEM[2]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 86
	c_t4_t0_t1_mem1 += MAS_MEM[1]

	c_t4_t20 = S.Task('c_t4_t20', length=3, delay_cost=1)
	S += c_t4_t20 >= 86
	c_t4_t20 += MAS[2]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 86
	c_t5_t0_t2_in += MAS_in[2]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 86
	c_t5_t0_t2_mem0 += MAS_MEM[0]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 86
	c_t5_t0_t2_mem1 += MAS_MEM[5]

	c_t2_t21 = S.Task('c_t2_t21', length=3, delay_cost=1)
	S += c_t2_t21 >= 87
	c_t2_t21 += MAS[0]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 87
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 87
	c_t3_t1_t1_mem0 += MAS_MEM[4]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 87
	c_t3_t1_t1_mem1 += MAS_MEM[7]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 87
	c_t3_t21_in += MAS_in[2]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 87
	c_t3_t21_mem0 += MAS_MEM[2]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 87
	c_t3_t21_mem1 += MAS_MEM[5]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 87
	c_t4100_in += MAS_in[1]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 87
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 87
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=11, delay_cost=1)
	S += c_t4_t0_t1 >= 87
	c_t4_t0_t1 += MM[0]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=3, delay_cost=1)
	S += c_t5_t0_t2 >= 87
	c_t5_t0_t2 += MAS[2]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 88
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 88
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 88
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 88
	c_t2_t4_t0_in += MM_in[1]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 88
	c_t2_t4_t0_mem0 += MAS_MEM[6]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 88
	c_t2_t4_t0_mem1 += MAS_MEM[1]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 88
	c_t2_t4_t3_in += MAS_in[2]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 88
	c_t2_t4_t3_mem0 += MAS_MEM[0]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 88
	c_t2_t4_t3_mem1 += MAS_MEM[3]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=11, delay_cost=1)
	S += c_t3_t1_t1 >= 88
	c_t3_t1_t1 += MM[0]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 88
	c_t3_t1_t2_in += MAS_in[0]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 88
	c_t3_t1_t2_mem0 += MAS_MEM[2]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 88
	c_t3_t1_t2_mem1 += MAS_MEM[5]

	c_t3_t21 = S.Task('c_t3_t21', length=3, delay_cost=1)
	S += c_t3_t21 >= 88
	c_t3_t21 += MAS[2]

	c_t4100 = S.Task('c_t4100', length=3, delay_cost=1)
	S += c_t4100 >= 88
	c_t4100 += MAS[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=11, delay_cost=1)
	S += c_t2_t1_t1 >= 89
	c_t2_t1_t1 += MM[0]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=11, delay_cost=1)
	S += c_t2_t4_t0 >= 89
	c_t2_t4_t0 += MM[1]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 89
	c_t2_t4_t1_in += MM_in[1]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 89
	c_t2_t4_t1_mem0 += MAS_MEM[0]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 89
	c_t2_t4_t1_mem1 += MAS_MEM[3]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 89
	c_t2_t4_t2_in += MAS_in[0]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 89
	c_t2_t4_t2_mem0 += MAS_MEM[6]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 89
	c_t2_t4_t2_mem1 += MAS_MEM[1]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=3, delay_cost=1)
	S += c_t2_t4_t3 >= 89
	c_t2_t4_t3 += MAS[2]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 89
	c_t3101_in += MAS_in[2]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 89
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 89
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=3, delay_cost=1)
	S += c_t3_t1_t2 >= 89
	c_t3_t1_t2 += MAS[0]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=11, delay_cost=1)
	S += c_t2_t4_t1 >= 90
	c_t2_t4_t1 += MM[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=3, delay_cost=1)
	S += c_t2_t4_t2 >= 90
	c_t2_t4_t2 += MAS[0]

	c_t3101 = S.Task('c_t3101', length=3, delay_cost=1)
	S += c_t3101 >= 90
	c_t3101 += MAS[2]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 90
	c_t4_t0_t0_in += MM_in[1]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 90
	c_t4_t0_t0_mem0 += MAS_MEM[0]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 90
	c_t4_t0_t0_mem1 += MAS_MEM[3]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 90
	c_t4_t0_t3_in += MAS_in[2]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 90
	c_t4_t0_t3_mem0 += MAS_MEM[2]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 90
	c_t4_t0_t3_mem1 += MAS_MEM[1]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 90
	c_t5101_in += MAS_in[0]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 90
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 90
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=11, delay_cost=1)
	S += c_t4_t0_t0 >= 91
	c_t4_t0_t0 += MM[1]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=3, delay_cost=1)
	S += c_t4_t0_t3 >= 91
	c_t4_t0_t3 += MAS[2]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 91
	c_t4_t30_in += MAS_in[0]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 91
	c_t4_t30_mem0 += MAS_MEM[2]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 91
	c_t4_t30_mem1 += MAS_MEM[1]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 91
	c_t5010_in += MAS_in[3]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 91
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 91
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5101 = S.Task('c_t5101', length=3, delay_cost=1)
	S += c_t5101 >= 91
	c_t5101 += MAS[0]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 92
	c_t3_t0_t1_in += MM_in[1]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 92
	c_t3_t0_t1_mem0 += MAS_MEM[2]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 92
	c_t3_t0_t1_mem1 += MAS_MEM[5]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 92
	c_t3_t31_in += MAS_in[2]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 92
	c_t3_t31_mem0 += MAS_MEM[4]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 92
	c_t3_t31_mem1 += MAS_MEM[7]

	c_t4_t30 = S.Task('c_t4_t30', length=3, delay_cost=1)
	S += c_t4_t30 >= 92
	c_t4_t30 += MAS[0]

	c_t5010 = S.Task('c_t5010', length=3, delay_cost=1)
	S += c_t5010 >= 92
	c_t5010 += MAS[3]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 92
	c_t5110_in += MAS_in[0]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 92
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 92
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=11, delay_cost=1)
	S += c_t3_t0_t1 >= 93
	c_t3_t0_t1 += MM[1]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 93
	c_t3_t0_t3_in += MAS_in[0]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 93
	c_t3_t0_t3_mem0 += MAS_MEM[0]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 93
	c_t3_t0_t3_mem1 += MAS_MEM[5]

	c_t3_t31 = S.Task('c_t3_t31', length=3, delay_cost=1)
	S += c_t3_t31 >= 93
	c_t3_t31 += MAS[2]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 93
	c_t5011_in += MAS_in[3]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 93
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 93
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5110 = S.Task('c_t5110', length=3, delay_cost=1)
	S += c_t5110 >= 93
	c_t5110 += MAS[0]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 93
	c_t5_t0_t1_in += MM_in[1]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 93
	c_t5_t0_t1_mem0 += MAS_MEM[4]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 93
	c_t5_t0_t1_mem1 += MAS_MEM[1]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=3, delay_cost=1)
	S += c_t3_t0_t3 >= 94
	c_t3_t0_t3 += MAS[0]

	c_t5011 = S.Task('c_t5011', length=3, delay_cost=1)
	S += c_t5011 >= 94
	c_t5011 += MAS[3]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 94
	c_t5111_in += MAS_in[3]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 94
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 94
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=11, delay_cost=1)
	S += c_t5_t0_t1 >= 94
	c_t5_t0_t1 += MM[1]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 95
	c_t5100_in += MAS_in[0]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 95
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 95
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5111 = S.Task('c_t5111', length=3, delay_cost=1)
	S += c_t5111 >= 95
	c_t5111 += MAS[3]

	c_t5100 = S.Task('c_t5100', length=3, delay_cost=1)
	S += c_t5100 >= 96
	c_t5100 += MAS[0]

	d_t2_t00_in = S.Task('d_t2_t00_in', length=1, delay_cost=1)
	S += d_t2_t00_in >= 96
	d_t2_t00_in += MAS_in[3]

	d_t2_t00_mem0 = S.Task('d_t2_t00_mem0', length=1, delay_cost=1)
	S += d_t2_t00_mem0 >= 96
	d_t2_t00_mem0 += MAIN_MEM_r[0]

	d_t2_t00_mem1 = S.Task('d_t2_t00_mem1', length=1, delay_cost=1)
	S += d_t2_t00_mem1 >= 96
	d_t2_t00_mem1 += MAS_MEM[1]

	d_t1_t01_in = S.Task('d_t1_t01_in', length=1, delay_cost=1)
	S += d_t1_t01_in >= 97
	d_t1_t01_in += MAS_in[1]

	d_t1_t01_mem0 = S.Task('d_t1_t01_mem0', length=1, delay_cost=1)
	S += d_t1_t01_mem0 >= 97
	d_t1_t01_mem0 += MAIN_MEM_r[0]

	d_t1_t01_mem1 = S.Task('d_t1_t01_mem1', length=1, delay_cost=1)
	S += d_t1_t01_mem1 >= 97
	d_t1_t01_mem1 += MAS_MEM[1]

	d_t2_t00 = S.Task('d_t2_t00', length=3, delay_cost=1)
	S += d_t2_t00 >= 97
	d_t2_t00 += MAS[3]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 98
	c_t5_t0_t0_in += MM_in[1]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 98
	c_t5_t0_t0_mem0 += MAS_MEM[0]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 98
	c_t5_t0_t0_mem1 += MAS_MEM[1]

	d_t1_t00_in = S.Task('d_t1_t00_in', length=1, delay_cost=1)
	S += d_t1_t00_in >= 98
	d_t1_t00_in += MAS_in[2]

	d_t1_t00_mem0 = S.Task('d_t1_t00_mem0', length=1, delay_cost=1)
	S += d_t1_t00_mem0 >= 98
	d_t1_t00_mem0 += MAIN_MEM_r[0]

	d_t1_t00_mem1 = S.Task('d_t1_t00_mem1', length=1, delay_cost=1)
	S += d_t1_t00_mem1 >= 98
	d_t1_t00_mem1 += MAS_MEM[3]

	d_t1_t01 = S.Task('d_t1_t01', length=3, delay_cost=1)
	S += d_t1_t01 >= 98
	d_t1_t01 += MAS[1]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 99
	c_t2_t1_t5_in += MAS_in[0]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 99
	c_t2_t1_t5_mem0 += MM_MEM[2]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 99
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=11, delay_cost=1)
	S += c_t5_t0_t0 >= 99
	c_t5_t0_t0 += MM[1]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 99
	c_t5_t0_t3_in += MAS_in[3]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 99
	c_t5_t0_t3_mem0 += MAS_MEM[0]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 99
	c_t5_t0_t3_mem1 += MAS_MEM[1]

	d_t1_t00 = S.Task('d_t1_t00', length=3, delay_cost=1)
	S += d_t1_t00 >= 99
	d_t1_t00 += MAS[2]

	d_t2_t01_in = S.Task('d_t2_t01_in', length=1, delay_cost=1)
	S += d_t2_t01_in >= 99
	d_t2_t01_in += MAS_in[1]

	d_t2_t01_mem0 = S.Task('d_t2_t01_mem0', length=1, delay_cost=1)
	S += d_t2_t01_mem0 >= 99
	d_t2_t01_mem0 += MAIN_MEM_r[0]

	d_t2_t01_mem1 = S.Task('d_t2_t01_mem1', length=1, delay_cost=1)
	S += d_t2_t01_mem1 >= 99
	d_t2_t01_mem1 += MAS_MEM[7]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 100
	c_t2_t10_in += MAS_in[2]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 100
	c_t2_t10_mem0 += MM_MEM[2]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 100
	c_t2_t10_mem1 += MM_MEM[1]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=3, delay_cost=1)
	S += c_t2_t1_t5 >= 100
	c_t2_t1_t5 += MAS[0]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=3, delay_cost=1)
	S += c_t5_t0_t3 >= 100
	c_t5_t0_t3 += MAS[3]

	d_t0_t01_in = S.Task('d_t0_t01_in', length=1, delay_cost=1)
	S += d_t0_t01_in >= 100
	d_t0_t01_in += MAS_in[0]

	d_t0_t01_mem0 = S.Task('d_t0_t01_mem0', length=1, delay_cost=1)
	S += d_t0_t01_mem0 >= 100
	d_t0_t01_mem0 += MAIN_MEM_r[0]

	d_t0_t01_mem1 = S.Task('d_t0_t01_mem1', length=1, delay_cost=1)
	S += d_t0_t01_mem1 >= 100
	d_t0_t01_mem1 += MAS_MEM[5]

	d_t2_t01 = S.Task('d_t2_t01', length=3, delay_cost=1)
	S += d_t2_t01 >= 100
	d_t2_t01 += MAS[1]

	c_t2_t10 = S.Task('c_t2_t10', length=3, delay_cost=1)
	S += c_t2_t10 >= 101
	c_t2_t10 += MAS[2]

	d_t0_t00_in = S.Task('d_t0_t00_in', length=1, delay_cost=1)
	S += d_t0_t00_in >= 101
	d_t0_t00_in += MAS_in[2]

	d_t0_t00_mem0 = S.Task('d_t0_t00_mem0', length=1, delay_cost=1)
	S += d_t0_t00_mem0 >= 101
	d_t0_t00_mem0 += MAIN_MEM_r[0]

	d_t0_t00_mem1 = S.Task('d_t0_t00_mem1', length=1, delay_cost=1)
	S += d_t0_t00_mem1 >= 101
	d_t0_t00_mem1 += MAS_MEM[3]

	d_t0_t01 = S.Task('d_t0_t01', length=3, delay_cost=1)
	S += d_t0_t01 >= 101
	d_t0_t01 += MAS[0]

	d_t0_t00 = S.Task('d_t0_t00', length=3, delay_cost=1)
	S += d_t0_t00 >= 102
	d_t0_t00 += MAS[2]


	# new tasks
	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=11, delay_cost=1)
	c_t5_t1_t0 += alt(MM)
	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	c_t5_t1_t0_in += alt(MM_in)
	S += c_t5_t1_t0_in*MM_in[0]<=c_t5_t1_t0*MM[0]
	S += c_t5_t1_t0_in*MM_in[1]<=c_t5_t1_t0*MM[1]
	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	c_t5_t1_t0_mem0 += MAS_MEM[6]
	S += 94 < c_t5_t1_t0_mem0
	S += c_t5_t1_t0_mem0 <= c_t5_t1_t0

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	c_t5_t1_t0_mem1 += MAS_MEM[1]
	S += 95 < c_t5_t1_t0_mem1
	S += c_t5_t1_t0_mem1 <= c_t5_t1_t0

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=11, delay_cost=1)
	c_t5_t1_t1 += alt(MM)
	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	c_t5_t1_t1_in += alt(MM_in)
	S += c_t5_t1_t1_in*MM_in[0]<=c_t5_t1_t1*MM[0]
	S += c_t5_t1_t1_in*MM_in[1]<=c_t5_t1_t1*MM[1]
	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	c_t5_t1_t1_mem0 += MAS_MEM[6]
	S += 96 < c_t5_t1_t1_mem0
	S += c_t5_t1_t1_mem0 <= c_t5_t1_t1

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	c_t5_t1_t1_mem1 += MAS_MEM[7]
	S += 97 < c_t5_t1_t1_mem1
	S += c_t5_t1_t1_mem1 <= c_t5_t1_t1

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=3, delay_cost=1)
	c_t5_t1_t2 += alt(MAS)
	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	c_t5_t1_t2_in += alt(MAS_in)
	S += c_t5_t1_t2_in*MAS_in[0]<=c_t5_t1_t2*MAS[0]

	S += c_t5_t1_t2_in*MAS_in[1]<=c_t5_t1_t2*MAS[1]

	S += c_t5_t1_t2_in*MAS_in[2]<=c_t5_t1_t2*MAS[2]

	S += c_t5_t1_t2_in*MAS_in[3]<=c_t5_t1_t2*MAS[3]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	c_t5_t1_t2_mem0 += MAS_MEM[6]
	S += 94 < c_t5_t1_t2_mem0
	S += c_t5_t1_t2_mem0 <= c_t5_t1_t2

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	c_t5_t1_t2_mem1 += MAS_MEM[7]
	S += 96 < c_t5_t1_t2_mem1
	S += c_t5_t1_t2_mem1 <= c_t5_t1_t2

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=3, delay_cost=1)
	c_t5_t1_t3 += alt(MAS)
	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	c_t5_t1_t3_in += alt(MAS_in)
	S += c_t5_t1_t3_in*MAS_in[0]<=c_t5_t1_t3*MAS[0]

	S += c_t5_t1_t3_in*MAS_in[1]<=c_t5_t1_t3*MAS[1]

	S += c_t5_t1_t3_in*MAS_in[2]<=c_t5_t1_t3*MAS[2]

	S += c_t5_t1_t3_in*MAS_in[3]<=c_t5_t1_t3*MAS[3]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	c_t5_t1_t3_mem0 += MAS_MEM[0]
	S += 95 < c_t5_t1_t3_mem0
	S += c_t5_t1_t3_mem0 <= c_t5_t1_t3

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	c_t5_t1_t3_mem1 += MAS_MEM[7]
	S += 97 < c_t5_t1_t3_mem1
	S += c_t5_t1_t3_mem1 <= c_t5_t1_t3

	c_t5_t20 = S.Task('c_t5_t20', length=3, delay_cost=1)
	c_t5_t20 += alt(MAS)
	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	c_t5_t20_in += alt(MAS_in)
	S += c_t5_t20_in*MAS_in[0]<=c_t5_t20*MAS[0]

	S += c_t5_t20_in*MAS_in[1]<=c_t5_t20*MAS[1]

	S += c_t5_t20_in*MAS_in[2]<=c_t5_t20*MAS[2]

	S += c_t5_t20_in*MAS_in[3]<=c_t5_t20*MAS[3]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	c_t5_t20_mem0 += MAS_MEM[0]
	S += 86 < c_t5_t20_mem0
	S += c_t5_t20_mem0 <= c_t5_t20

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	c_t5_t20_mem1 += MAS_MEM[7]
	S += 94 < c_t5_t20_mem1
	S += c_t5_t20_mem1 <= c_t5_t20

	c_t5_t21 = S.Task('c_t5_t21', length=3, delay_cost=1)
	c_t5_t21 += alt(MAS)
	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	c_t5_t21_in += alt(MAS_in)
	S += c_t5_t21_in*MAS_in[0]<=c_t5_t21*MAS[0]

	S += c_t5_t21_in*MAS_in[1]<=c_t5_t21*MAS[1]

	S += c_t5_t21_in*MAS_in[2]<=c_t5_t21*MAS[2]

	S += c_t5_t21_in*MAS_in[3]<=c_t5_t21*MAS[3]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	c_t5_t21_mem0 += MAS_MEM[4]
	S += 78 < c_t5_t21_mem0
	S += c_t5_t21_mem0 <= c_t5_t21

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	c_t5_t21_mem1 += MAS_MEM[7]
	S += 96 < c_t5_t21_mem1
	S += c_t5_t21_mem1 <= c_t5_t21

	c_t5_t30 = S.Task('c_t5_t30', length=3, delay_cost=1)
	c_t5_t30 += alt(MAS)
	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	c_t5_t30_in += alt(MAS_in)
	S += c_t5_t30_in*MAS_in[0]<=c_t5_t30*MAS[0]

	S += c_t5_t30_in*MAS_in[1]<=c_t5_t30*MAS[1]

	S += c_t5_t30_in*MAS_in[2]<=c_t5_t30*MAS[2]

	S += c_t5_t30_in*MAS_in[3]<=c_t5_t30*MAS[3]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	c_t5_t30_mem0 += MAS_MEM[0]
	S += 98 < c_t5_t30_mem0
	S += c_t5_t30_mem0 <= c_t5_t30

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	c_t5_t30_mem1 += MAS_MEM[1]
	S += 95 < c_t5_t30_mem1
	S += c_t5_t30_mem1 <= c_t5_t30

	c_t5_t31 = S.Task('c_t5_t31', length=3, delay_cost=1)
	c_t5_t31 += alt(MAS)
	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	c_t5_t31_in += alt(MAS_in)
	S += c_t5_t31_in*MAS_in[0]<=c_t5_t31*MAS[0]

	S += c_t5_t31_in*MAS_in[1]<=c_t5_t31*MAS[1]

	S += c_t5_t31_in*MAS_in[2]<=c_t5_t31*MAS[2]

	S += c_t5_t31_in*MAS_in[3]<=c_t5_t31*MAS[3]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	c_t5_t31_mem0 += MAS_MEM[0]
	S += 93 < c_t5_t31_mem0
	S += c_t5_t31_mem0 <= c_t5_t31

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	c_t5_t31_mem1 += MAS_MEM[7]
	S += 97 < c_t5_t31_mem1
	S += c_t5_t31_mem1 <= c_t5_t31

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage3MAS4/FP12_LADDERMUL/schedule6.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 6))

	return solution

