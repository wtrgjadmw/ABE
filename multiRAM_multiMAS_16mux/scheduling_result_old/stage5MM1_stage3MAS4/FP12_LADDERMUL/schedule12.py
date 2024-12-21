from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 199
	S = Scenario("schedule12", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 0
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 0
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 0
	d_t0_t11_in += MAS_in[2]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 0
	d_t0_t3_t0_in += MM_in[0]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 0
	d_t2_a1_1_in += MAS_in[1]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 0
	d_t2_t10_in += MAS_in[0]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 0
	d_t3010_in += MAS_in[3]

	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 1
	d_t0_a1_0_in += MAS_in[2]

	d_t0_t11 = S.Task('d_t0_t11', length=3, delay_cost=1)
	S += d_t0_t11 >= 1
	d_t0_t11 += MAS[2]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=5, delay_cost=1)
	S += d_t0_t3_t0 >= 1
	d_t0_t3_t0 += MM[0]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 1
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 1
	d_t1_t3_t0_in += MM_in[0]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 1
	d_t2_a1_0_in += MAS_in[3]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=3, delay_cost=1)
	S += d_t2_a1_1 >= 1
	d_t2_a1_1 += MAS[1]

	d_t2_t10 = S.Task('d_t2_t10', length=3, delay_cost=1)
	S += d_t2_t10 >= 1
	d_t2_t10 += MAS[0]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 1
	d_t2_t3_t3_in += MAS_in[0]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 1
	d_t3000_in += MAS_in[1]

	d_t3010 = S.Task('d_t3010', length=3, delay_cost=1)
	S += d_t3010 >= 1
	d_t3010 += MAS[3]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 1
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=3, delay_cost=1)
	S += d_t0_a1_0 >= 2
	d_t0_a1_0 += MAS[2]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 2
	d_t0_t3_t2_in += MAS_in[3]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 2
	d_t1_t11_in += MAS_in[0]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=5, delay_cost=1)
	S += d_t1_t3_t0 >= 2
	d_t1_t3_t0 += MM[0]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=3, delay_cost=1)
	S += d_t2_a1_0 >= 2
	d_t2_a1_0 += MAS[3]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 2
	d_t2_t3_t0_in += MM_in[0]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=3, delay_cost=1)
	S += d_t2_t3_t3 >= 2
	d_t2_t3_t3 += MAS[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 2
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3000 = S.Task('d_t3000', length=3, delay_cost=1)
	S += d_t3000 >= 2
	d_t3000 += MAS[1]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 2
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 2
	d_t3011_in += MAS_in[2]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 2
	d_t4001_in += MAS_in[1]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 3
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 3
	d_t0_t3_t1_in += MM_in[0]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=3, delay_cost=1)
	S += d_t0_t3_t2 >= 3
	d_t0_t3_t2 += MAS[3]

	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 3
	d_t0_t3_t3_in += MAS_in[1]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 3
	d_t1_t10_in += MAS_in[3]

	d_t1_t11 = S.Task('d_t1_t11', length=3, delay_cost=1)
	S += d_t1_t11 >= 3
	d_t1_t11 += MAS[0]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 3
	d_t1_t3_t3_in += MAS_in[2]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=5, delay_cost=1)
	S += d_t2_t3_t0 >= 3
	d_t2_t3_t0 += MM[0]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 3
	d_t3001_in += MAS_in[0]

	d_t3011 = S.Task('d_t3011', length=3, delay_cost=1)
	S += d_t3011 >= 3
	d_t3011 += MAS[2]

	d_t4001 = S.Task('d_t4001', length=3, delay_cost=1)
	S += d_t4001 >= 3
	d_t4001 += MAS[1]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 3
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 4
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 4
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=5, delay_cost=1)
	S += d_t0_t3_t1 >= 4
	d_t0_t3_t1 += MM[0]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=3, delay_cost=1)
	S += d_t0_t3_t3 >= 4
	d_t0_t3_t3 += MAS[1]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 4
	d_t1_a1_0_in += MAS_in[3]

	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 4
	d_t1_a1_1_in += MAS_in[2]

	d_t1_t10 = S.Task('d_t1_t10', length=3, delay_cost=1)
	S += d_t1_t10 >= 4
	d_t1_t10 += MAS[3]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 4
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 4
	d_t1_t3_t2_in += MAS_in[0]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=3, delay_cost=1)
	S += d_t1_t3_t3 >= 4
	d_t1_t3_t3 += MAS[2]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 4
	d_t2_t3_t2_in += MAS_in[1]

	d_t3001 = S.Task('d_t3001', length=3, delay_cost=1)
	S += d_t3001 >= 4
	d_t3001 += MAS[0]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 5
	d_t0_a1_1_in += MAS_in[1]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 5
	d_t0_t10_in += MAS_in[2]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 5
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=3, delay_cost=1)
	S += d_t1_a1_0 >= 5
	d_t1_a1_0 += MAS[3]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=3, delay_cost=1)
	S += d_t1_a1_1 >= 5
	d_t1_a1_1 += MAS[2]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=5, delay_cost=1)
	S += d_t1_t3_t1 >= 5
	d_t1_t3_t1 += MM[0]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=3, delay_cost=1)
	S += d_t1_t3_t2 >= 5
	d_t1_t3_t2 += MAS[0]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 5
	d_t2_t11_in += MAS_in[3]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 5
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 5
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=3, delay_cost=1)
	S += d_t2_t3_t2 >= 5
	d_t2_t3_t2 += MAS[1]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 5
	d_t4000_in += MAS_in[0]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 6
	c_t0_t1_t3_in += MAS_in[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 6
	c_t0_t31_in += MAS_in[3]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 6
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 6
	c_t1_t1_t2_in += MAS_in[0]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=3, delay_cost=1)
	S += d_t0_a1_1 >= 6
	d_t0_a1_1 += MAS[1]

	d_t0_t10 = S.Task('d_t0_t10', length=3, delay_cost=1)
	S += d_t0_t10 >= 6
	d_t0_t10 += MAS[2]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 6
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t11 = S.Task('d_t2_t11', length=3, delay_cost=1)
	S += d_t2_t11 >= 6
	d_t2_t11 += MAS[3]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=5, delay_cost=1)
	S += d_t2_t3_t1 >= 6
	d_t2_t3_t1 += MM[0]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 6
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t4000 = S.Task('d_t4000', length=3, delay_cost=1)
	S += d_t4000 >= 6
	d_t4000 += MAS[0]

	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	S += d_t4011_in >= 6
	d_t4011_in += MAS_in[2]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 7
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=3, delay_cost=1)
	S += c_t0_t1_t3 >= 7
	c_t0_t1_t3 += MAS[1]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 7
	c_t0_t20_in += MAS_in[3]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 7
	c_t0_t30_in += MAS_in[2]

	c_t0_t31 = S.Task('c_t0_t31', length=3, delay_cost=1)
	S += c_t0_t31 >= 7
	c_t0_t31 += MAS[3]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=5, delay_cost=1)
	S += c_t1_t0_t0 >= 7
	c_t1_t0_t0 += MM[0]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=3, delay_cost=1)
	S += c_t1_t1_t2 >= 7
	c_t1_t1_t2 += MAS[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 7
	c_t1_t20_in += MAS_in[1]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 7
	c_t1_t31_in += MAS_in[0]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 7
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 7
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t4011 = S.Task('d_t4011', length=3, delay_cost=1)
	S += d_t4011 >= 7
	d_t4011 += MAS[2]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=5, delay_cost=1)
	S += c_t0_t0_t0 >= 8
	c_t0_t0_t0 += MM[0]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 8
	c_t0_t0_t2_in += MAS_in[0]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 8
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t20 = S.Task('c_t0_t20', length=3, delay_cost=1)
	S += c_t0_t20 >= 8
	c_t0_t20 += MAS[3]

	c_t0_t30 = S.Task('c_t0_t30', length=3, delay_cost=1)
	S += c_t0_t30 >= 8
	c_t0_t30 += MAS[2]

	c_t1_t20 = S.Task('c_t1_t20', length=3, delay_cost=1)
	S += c_t1_t20 >= 8
	c_t1_t20 += MAS[1]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 8
	c_t1_t30_in += MAS_in[2]

	c_t1_t31 = S.Task('c_t1_t31', length=3, delay_cost=1)
	S += c_t1_t31 >= 8
	c_t1_t31 += MAS[0]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 8
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 8
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	S += d_t5001_in >= 8
	d_t5001_in += MAS_in[3]

	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	S += d_t5011_in >= 8
	d_t5011_in += MAS_in[1]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 9
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=3, delay_cost=1)
	S += c_t0_t0_t2 >= 9
	c_t0_t0_t2 += MAS[0]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=5, delay_cost=1)
	S += c_t0_t1_t0 >= 9
	c_t0_t1_t0 += MM[0]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 9
	c_t0_t21_in += MAS_in[2]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 9
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t30 = S.Task('c_t1_t30', length=3, delay_cost=1)
	S += c_t1_t30 >= 9
	c_t1_t30 += MAS[2]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 9
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 9
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	S += d_t4010_in >= 9
	d_t4010_in += MAS_in[3]

	d_t5001 = S.Task('d_t5001', length=3, delay_cost=1)
	S += d_t5001 >= 9
	d_t5001 += MAS[3]

	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	S += d_t5010_in >= 9
	d_t5010_in += MAS_in[1]

	d_t5011 = S.Task('d_t5011', length=3, delay_cost=1)
	S += d_t5011 >= 9
	d_t5011 += MAS[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=5, delay_cost=1)
	S += c_t0_t0_t1 >= 10
	c_t0_t0_t1 += MM[0]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 10
	c_t0_t0_t3_in += MAS_in[1]

	c_t0_t21 = S.Task('c_t0_t21', length=3, delay_cost=1)
	S += c_t0_t21 >= 10
	c_t0_t21 += MAS[2]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=3, delay_cost=1)
	S += c_t1_t0_t2 >= 10
	c_t1_t0_t2 += MAS[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 10
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 10
	c_t1_t1_t3_in += MAS_in[0]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 10
	c_t1_t21_in += MAS_in[2]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 10
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 10
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t4010 = S.Task('d_t4010', length=3, delay_cost=1)
	S += d_t4010 >= 10
	d_t4010 += MAS[3]

	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	S += d_t5000_in >= 10
	d_t5000_in += MAS_in[3]

	d_t5010 = S.Task('d_t5010', length=3, delay_cost=1)
	S += d_t5010 >= 10
	d_t5010 += MAS[1]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=3, delay_cost=1)
	S += c_t0_t0_t3 >= 11
	c_t0_t0_t3 += MAS[1]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 11
	c_t0_t1_t2_in += MAS_in[0]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 11
	c_t1_t0_t3_in += MAS_in[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=5, delay_cost=1)
	S += c_t1_t1_t0 >= 11
	c_t1_t1_t0 += MM[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 11
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=3, delay_cost=1)
	S += c_t1_t1_t3 >= 11
	c_t1_t1_t3 += MAS[0]

	c_t1_t21 = S.Task('c_t1_t21', length=3, delay_cost=1)
	S += c_t1_t21 >= 11
	c_t1_t21 += MAS[2]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 11
	c_t4000_in += MAS_in[3]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 11
	c_t4111_in += MAS_in[2]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 11
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 11
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t5000 = S.Task('d_t5000', length=3, delay_cost=1)
	S += d_t5000 >= 11
	d_t5000 += MAS[3]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=3, delay_cost=1)
	S += c_t0_t1_t2 >= 12
	c_t0_t1_t2 += MAS[0]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 12
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=3, delay_cost=1)
	S += c_t1_t0_t3 >= 12
	c_t1_t0_t3 += MAS[1]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=5, delay_cost=1)
	S += c_t1_t1_t1 >= 12
	c_t1_t1_t1 += MM[0]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 12
	c_t2_t31_in += MAS_in[0]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 12
	c_t3000_in += MAS_in[2]

	c_t4000 = S.Task('c_t4000', length=3, delay_cost=1)
	S += c_t4000 >= 12
	c_t4000 += MAS[3]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 12
	c_t4011_in += MAS_in[3]

	c_t4111 = S.Task('c_t4111', length=3, delay_cost=1)
	S += c_t4111 >= 12
	c_t4111 += MAS[2]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 12
	c_t5001_in += MAS_in[1]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 12
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 12
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 13
	c_t0_t1_t1_in += MM_in[0]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=5, delay_cost=1)
	S += c_t1_t0_t1 >= 13
	c_t1_t0_t1 += MM[0]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 13
	c_t2_t0_t2_in += MAS_in[1]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 13
	c_t2_t1_t3_in += MAS_in[0]

	c_t2_t31 = S.Task('c_t2_t31', length=3, delay_cost=1)
	S += c_t2_t31 >= 13
	c_t2_t31 += MAS[0]

	c_t3000 = S.Task('c_t3000', length=3, delay_cost=1)
	S += c_t3000 >= 13
	c_t3000 += MAS[2]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 13
	c_t3100_in += MAS_in[3]

	c_t4011 = S.Task('c_t4011', length=3, delay_cost=1)
	S += c_t4011 >= 13
	c_t4011 += MAS[3]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 13
	c_t4100_in += MAS_in[2]

	c_t5001 = S.Task('c_t5001', length=3, delay_cost=1)
	S += c_t5001 >= 13
	c_t5001 += MAS[1]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 13
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 13
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=5, delay_cost=1)
	S += c_t0_t1_t1 >= 14
	c_t0_t1_t1 += MM[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=3, delay_cost=1)
	S += c_t2_t0_t2 >= 14
	c_t2_t0_t2 += MAS[1]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 14
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=3, delay_cost=1)
	S += c_t2_t1_t3 >= 14
	c_t2_t1_t3 += MAS[0]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 14
	c_t2_t20_in += MAS_in[1]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 14
	c_t2_t21_in += MAS_in[2]

	c_t3100 = S.Task('c_t3100', length=3, delay_cost=1)
	S += c_t3100 >= 14
	c_t3100 += MAS[3]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 14
	c_t3111_in += MAS_in[3]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 14
	c_t4001_in += MAS_in[0]

	c_t4100 = S.Task('c_t4100', length=3, delay_cost=1)
	S += c_t4100 >= 14
	c_t4100 += MAS[2]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 14
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 14
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=5, delay_cost=1)
	S += c_t2_t1_t0 >= 15
	c_t2_t1_t0 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 15
	c_t2_t1_t1_in += MM_in[0]

	c_t2_t20 = S.Task('c_t2_t20', length=3, delay_cost=1)
	S += c_t2_t20 >= 15
	c_t2_t20 += MAS[1]

	c_t2_t21 = S.Task('c_t2_t21', length=3, delay_cost=1)
	S += c_t2_t21 >= 15
	c_t2_t21 += MAS[2]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 15
	c_t3001_in += MAS_in[2]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 15
	c_t3110_in += MAS_in[1]

	c_t3111 = S.Task('c_t3111', length=3, delay_cost=1)
	S += c_t3111 >= 15
	c_t3111 += MAS[3]

	c_t4001 = S.Task('c_t4001', length=3, delay_cost=1)
	S += c_t4001 >= 15
	c_t4001 += MAS[0]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 15
	c_t4010_in += MAS_in[0]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 15
	c_t5000_in += MAS_in[3]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 15
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 15
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 16
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 16
	c_t2_t0_t3_in += MAS_in[1]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=5, delay_cost=1)
	S += c_t2_t1_t1 >= 16
	c_t2_t1_t1 += MM[0]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 16
	c_t2_t1_t2_in += MAS_in[3]

	c_t3001 = S.Task('c_t3001', length=3, delay_cost=1)
	S += c_t3001 >= 16
	c_t3001 += MAS[2]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 16
	c_t3010_in += MAS_in[2]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 16
	c_t3011_in += MAS_in[0]

	c_t3110 = S.Task('c_t3110', length=3, delay_cost=1)
	S += c_t3110 >= 16
	c_t3110 += MAS[1]

	c_t4010 = S.Task('c_t4010', length=3, delay_cost=1)
	S += c_t4010 >= 16
	c_t4010 += MAS[0]

	c_t5000 = S.Task('c_t5000', length=3, delay_cost=1)
	S += c_t5000 >= 16
	c_t5000 += MAS[3]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 16
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 16
	d_t3010_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 17
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=5, delay_cost=1)
	S += c_t2_t0_t1 >= 17
	c_t2_t0_t1 += MM[0]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=3, delay_cost=1)
	S += c_t2_t0_t3 >= 17
	c_t2_t0_t3 += MAS[1]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=3, delay_cost=1)
	S += c_t2_t1_t2 >= 17
	c_t2_t1_t2 += MAS[3]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 17
	c_t2_t30_in += MAS_in[2]

	c_t3010 = S.Task('c_t3010', length=3, delay_cost=1)
	S += c_t3010 >= 17
	c_t3010 += MAS[2]

	c_t3011 = S.Task('c_t3011', length=3, delay_cost=1)
	S += c_t3011 >= 17
	c_t3011 += MAS[0]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 17
	c_t3101_in += MAS_in[3]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 17
	c_t4101_in += MAS_in[1]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 17
	c_t4110_in += MAS_in[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 17
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 17
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 18
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 18
	c_t0_t4_t0_mem0 += MAS_MEM[6]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 18
	c_t0_t4_t0_mem1 += MAS_MEM[5]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=5, delay_cost=1)
	S += c_t2_t0_t0 >= 18
	c_t2_t0_t0 += MM[0]

	c_t2_t30 = S.Task('c_t2_t30', length=3, delay_cost=1)
	S += c_t2_t30 >= 18
	c_t2_t30 += MAS[2]

	c_t3101 = S.Task('c_t3101', length=3, delay_cost=1)
	S += c_t3101 >= 18
	c_t3101 += MAS[3]

	c_t4101 = S.Task('c_t4101', length=3, delay_cost=1)
	S += c_t4101 >= 18
	c_t4101 += MAS[1]

	c_t4110 = S.Task('c_t4110', length=3, delay_cost=1)
	S += c_t4110 >= 18
	c_t4110 += MAS[0]

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	S += c_t5011_in >= 18
	c_t5011_in += MAS_in[1]

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	S += c_t5100_in >= 18
	c_t5100_in += MAS_in[3]

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	S += c_t5110_in >= 18
	c_t5110_in += MAS_in[2]

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	S += c_t5111_in >= 18
	c_t5111_in += MAS_in[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 18
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 18
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=5, delay_cost=1)
	S += c_t0_t4_t0 >= 19
	c_t0_t4_t0 += MM[0]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 19
	c_t5010_in += MAS_in[2]

	c_t5011 = S.Task('c_t5011', length=3, delay_cost=1)
	S += c_t5011 >= 19
	c_t5011 += MAS[1]

	c_t5100 = S.Task('c_t5100', length=3, delay_cost=1)
	S += c_t5100 >= 19
	c_t5100 += MAS[3]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 19
	c_t5101_in += MAS_in[0]

	c_t5110 = S.Task('c_t5110', length=3, delay_cost=1)
	S += c_t5110 >= 19
	c_t5110 += MAS[2]

	c_t5111 = S.Task('c_t5111', length=3, delay_cost=1)
	S += c_t5111 >= 19
	c_t5111 += MAS[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 19
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 19
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t3_t3_t0_in = S.Task('d_t3_t3_t0_in', length=1, delay_cost=1)
	S += d_t3_t3_t0_in >= 19
	d_t3_t3_t0_in += MM_in[0]

	d_t3_t3_t0_mem0 = S.Task('d_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem0 >= 19
	d_t3_t3_t0_mem0 += MAS_MEM[2]

	d_t3_t3_t0_mem1 = S.Task('d_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem1 >= 19
	d_t3_t3_t0_mem1 += MAS_MEM[7]

	d_t3_t3_t3_in = S.Task('d_t3_t3_t3_in', length=1, delay_cost=1)
	S += d_t3_t3_t3_in >= 19
	d_t3_t3_t3_in += MAS_in[1]

	d_t3_t3_t3_mem0 = S.Task('d_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem0 >= 19
	d_t3_t3_t3_mem0 += MAS_MEM[6]

	d_t3_t3_t3_mem1 = S.Task('d_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem1 >= 19
	d_t3_t3_t3_mem1 += MAS_MEM[5]

	d_t4_t3_t2_in = S.Task('d_t4_t3_t2_in', length=1, delay_cost=1)
	S += d_t4_t3_t2_in >= 19
	d_t4_t3_t2_in += MAS_in[3]

	d_t4_t3_t2_mem0 = S.Task('d_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem0 >= 19
	d_t4_t3_t2_mem0 += MAS_MEM[0]

	d_t4_t3_t2_mem1 = S.Task('d_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem1 >= 19
	d_t4_t3_t2_mem1 += MAS_MEM[3]

	c_t5010 = S.Task('c_t5010', length=3, delay_cost=1)
	S += c_t5010 >= 20
	c_t5010 += MAS[2]

	c_t5101 = S.Task('c_t5101', length=3, delay_cost=1)
	S += c_t5101 >= 20
	c_t5101 += MAS[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 20
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t5_in = S.Task('d_t1_t3_t5_in', length=1, delay_cost=1)
	S += d_t1_t3_t5_in >= 20
	d_t1_t3_t5_in += MAS_in[1]

	d_t1_t3_t5_mem0 = S.Task('d_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem0 >= 20
	d_t1_t3_t5_mem0 += MM_MEM[0]

	d_t1_t3_t5_mem1 = S.Task('d_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem1 >= 20
	d_t1_t3_t5_mem1 += MM_MEM[1]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 20
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t4_in = S.Task('d_t2_t3_t4_in', length=1, delay_cost=1)
	S += d_t2_t3_t4_in >= 20
	d_t2_t3_t4_in += MM_in[0]

	d_t2_t3_t4_mem0 = S.Task('d_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem0 >= 20
	d_t2_t3_t4_mem0 += MAS_MEM[2]

	d_t2_t3_t4_mem1 = S.Task('d_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem1 >= 20
	d_t2_t3_t4_mem1 += MAS_MEM[1]

	d_t3_a1_1_in = S.Task('d_t3_a1_1_in', length=1, delay_cost=1)
	S += d_t3_a1_1_in >= 20
	d_t3_a1_1_in += MAS_in[2]

	d_t3_a1_1_mem0 = S.Task('d_t3_a1_1_mem0', length=1, delay_cost=1)
	S += d_t3_a1_1_mem0 >= 20
	d_t3_a1_1_mem0 += MAS_MEM[4]

	d_t3_a1_1_mem1 = S.Task('d_t3_a1_1_mem1', length=1, delay_cost=1)
	S += d_t3_a1_1_mem1 >= 20
	d_t3_a1_1_mem1 += MAS_MEM[7]

	d_t3_t11_in = S.Task('d_t3_t11_in', length=1, delay_cost=1)
	S += d_t3_t11_in >= 20
	d_t3_t11_in += MAS_in[0]

	d_t3_t11_mem0 = S.Task('d_t3_t11_mem0', length=1, delay_cost=1)
	S += d_t3_t11_mem0 >= 20
	d_t3_t11_mem0 += MAS_MEM[0]

	d_t3_t11_mem1 = S.Task('d_t3_t11_mem1', length=1, delay_cost=1)
	S += d_t3_t11_mem1 >= 20
	d_t3_t11_mem1 += MAS_MEM[5]

	d_t3_t3_t0 = S.Task('d_t3_t3_t0', length=5, delay_cost=1)
	S += d_t3_t3_t0 >= 20
	d_t3_t3_t0 += MM[0]

	d_t3_t3_t3 = S.Task('d_t3_t3_t3', length=3, delay_cost=1)
	S += d_t3_t3_t3 >= 20
	d_t3_t3_t3 += MAS[1]

	d_t4_t3_t2 = S.Task('d_t4_t3_t2', length=3, delay_cost=1)
	S += d_t4_t3_t2 >= 20
	d_t4_t3_t2 += MAS[3]

	d_t5_t10_in = S.Task('d_t5_t10_in', length=1, delay_cost=1)
	S += d_t5_t10_in >= 20
	d_t5_t10_in += MAS_in[3]

	d_t5_t10_mem0 = S.Task('d_t5_t10_mem0', length=1, delay_cost=1)
	S += d_t5_t10_mem0 >= 20
	d_t5_t10_mem0 += MAS_MEM[6]

	d_t5_t10_mem1 = S.Task('d_t5_t10_mem1', length=1, delay_cost=1)
	S += d_t5_t10_mem1 >= 20
	d_t5_t10_mem1 += MAS_MEM[3]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 21
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t5_in = S.Task('d_t0_t3_t5_in', length=1, delay_cost=1)
	S += d_t0_t3_t5_in >= 21
	d_t0_t3_t5_in += MAS_in[2]

	d_t0_t3_t5_mem0 = S.Task('d_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem0 >= 21
	d_t0_t3_t5_mem0 += MM_MEM[0]

	d_t0_t3_t5_mem1 = S.Task('d_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem1 >= 21
	d_t0_t3_t5_mem1 += MM_MEM[1]

	d_t1_t2_t3_in = S.Task('d_t1_t2_t3_in', length=1, delay_cost=1)
	S += d_t1_t2_t3_in >= 21
	d_t1_t2_t3_in += MAS_in[3]

	d_t1_t2_t3_mem0 = S.Task('d_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem0 >= 21
	d_t1_t2_t3_mem0 += MAS_MEM[6]

	d_t1_t2_t3_mem1 = S.Task('d_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem1 >= 21
	d_t1_t2_t3_mem1 += MAS_MEM[1]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 21
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t5 = S.Task('d_t1_t3_t5', length=3, delay_cost=1)
	S += d_t1_t3_t5 >= 21
	d_t1_t3_t5 += MAS[1]

	d_t2_t3_t4 = S.Task('d_t2_t3_t4', length=5, delay_cost=1)
	S += d_t2_t3_t4 >= 21
	d_t2_t3_t4 += MM[0]

	d_t3_a1_1 = S.Task('d_t3_a1_1', length=3, delay_cost=1)
	S += d_t3_a1_1 >= 21
	d_t3_a1_1 += MAS[2]

	d_t3_t11 = S.Task('d_t3_t11', length=3, delay_cost=1)
	S += d_t3_t11 >= 21
	d_t3_t11 += MAS[0]

	d_t3_t3_t1_in = S.Task('d_t3_t3_t1_in', length=1, delay_cost=1)
	S += d_t3_t3_t1_in >= 21
	d_t3_t3_t1_in += MM_in[0]

	d_t3_t3_t1_mem0 = S.Task('d_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem0 >= 21
	d_t3_t3_t1_mem0 += MAS_MEM[0]

	d_t3_t3_t1_mem1 = S.Task('d_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem1 >= 21
	d_t3_t3_t1_mem1 += MAS_MEM[5]

	d_t4_a1_1_in = S.Task('d_t4_a1_1_in', length=1, delay_cost=1)
	S += d_t4_a1_1_in >= 21
	d_t4_a1_1_in += MAS_in[0]

	d_t4_a1_1_mem0 = S.Task('d_t4_a1_1_mem0', length=1, delay_cost=1)
	S += d_t4_a1_1_mem0 >= 21
	d_t4_a1_1_mem0 += MAS_MEM[4]

	d_t4_a1_1_mem1 = S.Task('d_t4_a1_1_mem1', length=1, delay_cost=1)
	S += d_t4_a1_1_mem1 >= 21
	d_t4_a1_1_mem1 += MAS_MEM[7]

	d_t5_a1_0_in = S.Task('d_t5_a1_0_in', length=1, delay_cost=1)
	S += d_t5_a1_0_in >= 21
	d_t5_a1_0_in += MAS_in[1]

	d_t5_a1_0_mem0 = S.Task('d_t5_a1_0_mem0', length=1, delay_cost=1)
	S += d_t5_a1_0_mem0 >= 21
	d_t5_a1_0_mem0 += MAS_MEM[2]

	d_t5_a1_0_mem1 = S.Task('d_t5_a1_0_mem1', length=1, delay_cost=1)
	S += d_t5_a1_0_mem1 >= 21
	d_t5_a1_0_mem1 += MAS_MEM[3]

	d_t5_t10 = S.Task('d_t5_t10', length=3, delay_cost=1)
	S += d_t5_t10 >= 21
	d_t5_t10 += MAS[3]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 22
	c_t0_t00_in += MAS_in[1]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 22
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 22
	c_t0_t00_mem1 += MM_MEM[1]

	d_t0_t2_t3_in = S.Task('d_t0_t2_t3_in', length=1, delay_cost=1)
	S += d_t0_t2_t3_in >= 22
	d_t0_t2_t3_in += MAS_in[3]

	d_t0_t2_t3_mem0 = S.Task('d_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem0 >= 22
	d_t0_t2_t3_mem0 += MAS_MEM[4]

	d_t0_t2_t3_mem1 = S.Task('d_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem1 >= 22
	d_t0_t2_t3_mem1 += MAS_MEM[5]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 22
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t5 = S.Task('d_t0_t3_t5', length=3, delay_cost=1)
	S += d_t0_t3_t5 >= 22
	d_t0_t3_t5 += MAS[2]

	d_t1_t2_t3 = S.Task('d_t1_t2_t3', length=3, delay_cost=1)
	S += d_t1_t2_t3 >= 22
	d_t1_t2_t3 += MAS[3]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 22
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t3_t3_t1 = S.Task('d_t3_t3_t1', length=5, delay_cost=1)
	S += d_t3_t3_t1 >= 22
	d_t3_t3_t1 += MM[0]

	d_t3_t3_t2_in = S.Task('d_t3_t3_t2_in', length=1, delay_cost=1)
	S += d_t3_t3_t2_in >= 22
	d_t3_t3_t2_in += MAS_in[0]

	d_t3_t3_t2_mem0 = S.Task('d_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem0 >= 22
	d_t3_t3_t2_mem0 += MAS_MEM[2]

	d_t3_t3_t2_mem1 = S.Task('d_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem1 >= 22
	d_t3_t3_t2_mem1 += MAS_MEM[1]

	d_t4_a1_1 = S.Task('d_t4_a1_1', length=3, delay_cost=1)
	S += d_t4_a1_1 >= 22
	d_t4_a1_1 += MAS[0]

	d_t4_t10_in = S.Task('d_t4_t10_in', length=1, delay_cost=1)
	S += d_t4_t10_in >= 22
	d_t4_t10_in += MAS_in[2]

	d_t4_t10_mem0 = S.Task('d_t4_t10_mem0', length=1, delay_cost=1)
	S += d_t4_t10_mem0 >= 22
	d_t4_t10_mem0 += MAS_MEM[0]

	d_t4_t10_mem1 = S.Task('d_t4_t10_mem1', length=1, delay_cost=1)
	S += d_t4_t10_mem1 >= 22
	d_t4_t10_mem1 += MAS_MEM[7]

	d_t5_a1_0 = S.Task('d_t5_a1_0', length=3, delay_cost=1)
	S += d_t5_a1_0 >= 22
	d_t5_a1_0 += MAS[1]

	d_t5_t3_t0_in = S.Task('d_t5_t3_t0_in', length=1, delay_cost=1)
	S += d_t5_t3_t0_in >= 22
	d_t5_t3_t0_in += MM_in[0]

	d_t5_t3_t0_mem0 = S.Task('d_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem0 >= 22
	d_t5_t3_t0_mem0 += MAS_MEM[6]

	d_t5_t3_t0_mem1 = S.Task('d_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem1 >= 22
	d_t5_t3_t0_mem1 += MAS_MEM[3]

	c_t0_t00 = S.Task('c_t0_t00', length=3, delay_cost=1)
	S += c_t0_t00 >= 23
	c_t0_t00 += MAS[1]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 23
	c_t4_t30_in += MAS_in[2]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 23
	c_t4_t30_mem0 += MAS_MEM[4]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 23
	c_t4_t30_mem1 += MAS_MEM[1]

	d_t0_t2_t3 = S.Task('d_t0_t2_t3', length=3, delay_cost=1)
	S += d_t0_t2_t3 >= 23
	d_t0_t2_t3 += MAS[3]

	d_t0_t30_in = S.Task('d_t0_t30_in', length=1, delay_cost=1)
	S += d_t0_t30_in >= 23
	d_t0_t30_in += MAS_in[0]

	d_t0_t30_mem0 = S.Task('d_t0_t30_mem0', length=1, delay_cost=1)
	S += d_t0_t30_mem0 >= 23
	d_t0_t30_mem0 += MM_MEM[0]

	d_t0_t30_mem1 = S.Task('d_t0_t30_mem1', length=1, delay_cost=1)
	S += d_t0_t30_mem1 >= 23
	d_t0_t30_mem1 += MM_MEM[1]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 23
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_t2_t3_in = S.Task('d_t2_t2_t3_in', length=1, delay_cost=1)
	S += d_t2_t2_t3_in >= 23
	d_t2_t2_t3_in += MAS_in[3]

	d_t2_t2_t3_mem0 = S.Task('d_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem0 >= 23
	d_t2_t2_t3_mem0 += MAS_MEM[0]

	d_t2_t2_t3_mem1 = S.Task('d_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem1 >= 23
	d_t2_t2_t3_mem1 += MAS_MEM[7]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 23
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3_t3_t2 = S.Task('d_t3_t3_t2', length=3, delay_cost=1)
	S += d_t3_t3_t2 >= 23
	d_t3_t3_t2 += MAS[0]

	d_t4_t10 = S.Task('d_t4_t10', length=3, delay_cost=1)
	S += d_t4_t10 >= 23
	d_t4_t10 += MAS[2]

	d_t4_t3_t1_in = S.Task('d_t4_t3_t1_in', length=1, delay_cost=1)
	S += d_t4_t3_t1_in >= 23
	d_t4_t3_t1_in += MM_in[0]

	d_t4_t3_t1_mem0 = S.Task('d_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem0 >= 23
	d_t4_t3_t1_mem0 += MAS_MEM[2]

	d_t4_t3_t1_mem1 = S.Task('d_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem1 >= 23
	d_t4_t3_t1_mem1 += MAS_MEM[5]

	d_t5_t11_in = S.Task('d_t5_t11_in', length=1, delay_cost=1)
	S += d_t5_t11_in >= 23
	d_t5_t11_in += MAS_in[1]

	d_t5_t11_mem0 = S.Task('d_t5_t11_mem0', length=1, delay_cost=1)
	S += d_t5_t11_mem0 >= 23
	d_t5_t11_mem0 += MAS_MEM[6]

	d_t5_t11_mem1 = S.Task('d_t5_t11_mem1', length=1, delay_cost=1)
	S += d_t5_t11_mem1 >= 23
	d_t5_t11_mem1 += MAS_MEM[3]

	d_t5_t3_t0 = S.Task('d_t5_t3_t0', length=5, delay_cost=1)
	S += d_t5_t3_t0 >= 23
	d_t5_t3_t0 += MM[0]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 24
	c_t3_t21_in += MAS_in[1]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 24
	c_t3_t21_mem0 += MAS_MEM[4]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 24
	c_t3_t21_mem1 += MAS_MEM[1]

	c_t4_t30 = S.Task('c_t4_t30', length=3, delay_cost=1)
	S += c_t4_t30 >= 24
	c_t4_t30 += MAS[2]

	d_t0_t30 = S.Task('d_t0_t30', length=3, delay_cost=1)
	S += d_t0_t30 >= 24
	d_t0_t30 += MAS[0]

	d_t2_t2_t3 = S.Task('d_t2_t2_t3', length=3, delay_cost=1)
	S += d_t2_t2_t3 >= 24
	d_t2_t2_t3 += MAS[3]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 24
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t5_in = S.Task('d_t2_t3_t5_in', length=1, delay_cost=1)
	S += d_t2_t3_t5_in >= 24
	d_t2_t3_t5_in += MAS_in[0]

	d_t2_t3_t5_mem0 = S.Task('d_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem0 >= 24
	d_t2_t3_t5_mem0 += MM_MEM[0]

	d_t2_t3_t5_mem1 = S.Task('d_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem1 >= 24
	d_t2_t3_t5_mem1 += MM_MEM[1]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 24
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t4_t3_t0_in = S.Task('d_t4_t3_t0_in', length=1, delay_cost=1)
	S += d_t4_t3_t0_in >= 24
	d_t4_t3_t0_in += MM_in[0]

	d_t4_t3_t0_mem0 = S.Task('d_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem0 >= 24
	d_t4_t3_t0_mem0 += MAS_MEM[0]

	d_t4_t3_t0_mem1 = S.Task('d_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem1 >= 24
	d_t4_t3_t0_mem1 += MAS_MEM[7]

	d_t4_t3_t1 = S.Task('d_t4_t3_t1', length=5, delay_cost=1)
	S += d_t4_t3_t1 >= 24
	d_t4_t3_t1 += MM[0]

	d_t4_t3_t3_in = S.Task('d_t4_t3_t3_in', length=1, delay_cost=1)
	S += d_t4_t3_t3_in >= 24
	d_t4_t3_t3_in += MAS_in[2]

	d_t4_t3_t3_mem0 = S.Task('d_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem0 >= 24
	d_t4_t3_t3_mem0 += MAS_MEM[6]

	d_t4_t3_t3_mem1 = S.Task('d_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem1 >= 24
	d_t4_t3_t3_mem1 += MAS_MEM[5]

	d_t5_t11 = S.Task('d_t5_t11', length=3, delay_cost=1)
	S += d_t5_t11 >= 24
	d_t5_t11 += MAS[1]

	d_t5_t3_t3_in = S.Task('d_t5_t3_t3_in', length=1, delay_cost=1)
	S += d_t5_t3_t3_in >= 24
	d_t5_t3_t3_in += MAS_in[3]

	d_t5_t3_t3_mem0 = S.Task('d_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem0 >= 24
	d_t5_t3_t3_mem0 += MAS_MEM[2]

	d_t5_t3_t3_mem1 = S.Task('d_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem1 >= 24
	d_t5_t3_t3_mem1 += MAS_MEM[3]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 25
	c_t0_t1_t4_in += MM_in[0]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 25
	c_t0_t1_t4_mem0 += MAS_MEM[0]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 25
	c_t0_t1_t4_mem1 += MAS_MEM[3]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 25
	c_t0_t1_t5_in += MAS_in[0]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 25
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 25
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 25
	c_t2_t4_t3_in += MAS_in[3]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 25
	c_t2_t4_t3_mem0 += MAS_MEM[4]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 25
	c_t2_t4_t3_mem1 += MAS_MEM[1]

	c_t3_t21 = S.Task('c_t3_t21', length=3, delay_cost=1)
	S += c_t3_t21 >= 25
	c_t3_t21 += MAS[1]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 25
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t5 = S.Task('d_t2_t3_t5', length=3, delay_cost=1)
	S += d_t2_t3_t5 >= 25
	d_t2_t3_t5 += MAS[0]

	d_t3_t10_in = S.Task('d_t3_t10_in', length=1, delay_cost=1)
	S += d_t3_t10_in >= 25
	d_t3_t10_in += MAS_in[2]

	d_t3_t10_mem0 = S.Task('d_t3_t10_mem0', length=1, delay_cost=1)
	S += d_t3_t10_mem0 >= 25
	d_t3_t10_mem0 += MAS_MEM[2]

	d_t3_t10_mem1 = S.Task('d_t3_t10_mem1', length=1, delay_cost=1)
	S += d_t3_t10_mem1 >= 25
	d_t3_t10_mem1 += MAS_MEM[7]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 25
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t4_a1_0_in = S.Task('d_t4_a1_0_in', length=1, delay_cost=1)
	S += d_t4_a1_0_in >= 25
	d_t4_a1_0_in += MAS_in[1]

	d_t4_a1_0_mem0 = S.Task('d_t4_a1_0_mem0', length=1, delay_cost=1)
	S += d_t4_a1_0_mem0 >= 25
	d_t4_a1_0_mem0 += MAS_MEM[6]

	d_t4_a1_0_mem1 = S.Task('d_t4_a1_0_mem1', length=1, delay_cost=1)
	S += d_t4_a1_0_mem1 >= 25
	d_t4_a1_0_mem1 += MAS_MEM[5]

	d_t4_t3_t0 = S.Task('d_t4_t3_t0', length=5, delay_cost=1)
	S += d_t4_t3_t0 >= 25
	d_t4_t3_t0 += MM[0]

	d_t4_t3_t3 = S.Task('d_t4_t3_t3', length=3, delay_cost=1)
	S += d_t4_t3_t3 >= 25
	d_t4_t3_t3 += MAS[2]

	d_t5_t3_t3 = S.Task('d_t5_t3_t3', length=3, delay_cost=1)
	S += d_t5_t3_t3 >= 25
	d_t5_t3_t3 += MAS[3]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 26
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 26
	c_t0_t0_t4_mem0 += MAS_MEM[0]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 26
	c_t0_t0_t4_mem1 += MAS_MEM[3]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=5, delay_cost=1)
	S += c_t0_t1_t4 >= 26
	c_t0_t1_t4 += MM[0]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=3, delay_cost=1)
	S += c_t0_t1_t5 >= 26
	c_t0_t1_t5 += MAS[0]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=3, delay_cost=1)
	S += c_t2_t4_t3 >= 26
	c_t2_t4_t3 += MAS[3]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 26
	c_t3_t1_t2_in += MAS_in[2]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 26
	c_t3_t1_t2_mem0 += MAS_MEM[4]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 26
	c_t3_t1_t2_mem1 += MAS_MEM[1]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 26
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_t30_in = S.Task('d_t2_t30_in', length=1, delay_cost=1)
	S += d_t2_t30_in >= 26
	d_t2_t30_in += MAS_in[3]

	d_t2_t30_mem0 = S.Task('d_t2_t30_mem0', length=1, delay_cost=1)
	S += d_t2_t30_mem0 >= 26
	d_t2_t30_mem0 += MM_MEM[0]

	d_t2_t30_mem1 = S.Task('d_t2_t30_mem1', length=1, delay_cost=1)
	S += d_t2_t30_mem1 >= 26
	d_t2_t30_mem1 += MM_MEM[1]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 26
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t3_t10 = S.Task('d_t3_t10', length=3, delay_cost=1)
	S += d_t3_t10 >= 26
	d_t3_t10 += MAS[2]

	d_t4_a1_0 = S.Task('d_t4_a1_0', length=3, delay_cost=1)
	S += d_t4_a1_0 >= 26
	d_t4_a1_0 += MAS[1]

	d_t4_t11_in = S.Task('d_t4_t11_in', length=1, delay_cost=1)
	S += d_t4_t11_in >= 26
	d_t4_t11_in += MAS_in[1]

	d_t4_t11_mem0 = S.Task('d_t4_t11_mem0', length=1, delay_cost=1)
	S += d_t4_t11_mem0 >= 26
	d_t4_t11_mem0 += MAS_MEM[2]

	d_t4_t11_mem1 = S.Task('d_t4_t11_mem1', length=1, delay_cost=1)
	S += d_t4_t11_mem1 >= 26
	d_t4_t11_mem1 += MAS_MEM[5]

	d_t5_t3_t2_in = S.Task('d_t5_t3_t2_in', length=1, delay_cost=1)
	S += d_t5_t3_t2_in >= 26
	d_t5_t3_t2_in += MAS_in[0]

	d_t5_t3_t2_mem0 = S.Task('d_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem0 >= 26
	d_t5_t3_t2_mem0 += MAS_MEM[6]

	d_t5_t3_t2_mem1 = S.Task('d_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem1 >= 26
	d_t5_t3_t2_mem1 += MAS_MEM[7]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=5, delay_cost=1)
	S += c_t0_t0_t4 >= 27
	c_t0_t0_t4 += MM[0]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 27
	c_t0_t0_t5_in += MAS_in[3]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 27
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 27
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 27
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 27
	c_t0_t4_t1_mem0 += MAS_MEM[4]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 27
	c_t0_t4_t1_mem1 += MAS_MEM[7]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=3, delay_cost=1)
	S += c_t3_t1_t2 >= 27
	c_t3_t1_t2 += MAS[2]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 27
	c_t5_t31_in += MAS_in[0]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 27
	c_t5_t31_mem0 += MAS_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 27
	c_t5_t31_mem1 += MAS_MEM[1]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 27
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 27
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t30 = S.Task('d_t2_t30', length=3, delay_cost=1)
	S += d_t2_t30 >= 27
	d_t2_t30 += MAS[3]

	d_t3_a1_0_in = S.Task('d_t3_a1_0_in', length=1, delay_cost=1)
	S += d_t3_a1_0_in >= 27
	d_t3_a1_0_in += MAS_in[2]

	d_t3_a1_0_mem0 = S.Task('d_t3_a1_0_mem0', length=1, delay_cost=1)
	S += d_t3_a1_0_mem0 >= 27
	d_t3_a1_0_mem0 += MAS_MEM[6]

	d_t3_a1_0_mem1 = S.Task('d_t3_a1_0_mem1', length=1, delay_cost=1)
	S += d_t3_a1_0_mem1 >= 27
	d_t3_a1_0_mem1 += MAS_MEM[5]

	d_t4_t11 = S.Task('d_t4_t11', length=3, delay_cost=1)
	S += d_t4_t11 >= 27
	d_t4_t11 += MAS[1]

	d_t5_a1_1_in = S.Task('d_t5_a1_1_in', length=1, delay_cost=1)
	S += d_t5_a1_1_in >= 27
	d_t5_a1_1_in += MAS_in[1]

	d_t5_a1_1_mem0 = S.Task('d_t5_a1_1_mem0', length=1, delay_cost=1)
	S += d_t5_a1_1_mem0 >= 27
	d_t5_a1_1_mem0 += MAS_MEM[2]

	d_t5_a1_1_mem1 = S.Task('d_t5_a1_1_mem1', length=1, delay_cost=1)
	S += d_t5_a1_1_mem1 >= 27
	d_t5_a1_1_mem1 += MAS_MEM[3]

	d_t5_t3_t2 = S.Task('d_t5_t3_t2', length=3, delay_cost=1)
	S += d_t5_t3_t2 >= 27
	d_t5_t3_t2 += MAS[0]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=3, delay_cost=1)
	S += c_t0_t0_t5 >= 28
	c_t0_t0_t5 += MAS[3]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 28
	c_t0_t10_in += MAS_in[2]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 28
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 28
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=5, delay_cost=1)
	S += c_t0_t4_t1 >= 28
	c_t0_t4_t1 += MM[0]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 28
	c_t4_t20_in += MAS_in[0]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 28
	c_t4_t20_mem0 += MAS_MEM[6]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 28
	c_t4_t20_mem1 += MAS_MEM[1]

	c_t5_t31 = S.Task('c_t5_t31', length=3, delay_cost=1)
	S += c_t5_t31 >= 28
	c_t5_t31 += MAS[0]

	d_t0_t01_in = S.Task('d_t0_t01_in', length=1, delay_cost=1)
	S += d_t0_t01_in >= 28
	d_t0_t01_in += MAS_in[3]

	d_t0_t01_mem1 = S.Task('d_t0_t01_mem1', length=1, delay_cost=1)
	S += d_t0_t01_mem1 >= 28
	d_t0_t01_mem1 += MAS_MEM[3]

	d_t1_t3_t4_in = S.Task('d_t1_t3_t4_in', length=1, delay_cost=1)
	S += d_t1_t3_t4_in >= 28
	d_t1_t3_t4_in += MM_in[0]

	d_t1_t3_t4_mem0 = S.Task('d_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem0 >= 28
	d_t1_t3_t4_mem0 += MAS_MEM[0]

	d_t1_t3_t4_mem1 = S.Task('d_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem1 >= 28
	d_t1_t3_t4_mem1 += MAS_MEM[5]

	d_t2_t00_in = S.Task('d_t2_t00_in', length=1, delay_cost=1)
	S += d_t2_t00_in >= 28
	d_t2_t00_in += MAS_in[1]

	d_t2_t00_mem1 = S.Task('d_t2_t00_mem1', length=1, delay_cost=1)
	S += d_t2_t00_mem1 >= 28
	d_t2_t00_mem1 += MAS_MEM[7]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 28
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 28
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3_a1_0 = S.Task('d_t3_a1_0', length=3, delay_cost=1)
	S += d_t3_a1_0 >= 28
	d_t3_a1_0 += MAS[2]

	d_t5_a1_1 = S.Task('d_t5_a1_1', length=3, delay_cost=1)
	S += d_t5_a1_1 >= 28
	d_t5_a1_1 += MAS[1]

	c_t0_t10 = S.Task('c_t0_t10', length=3, delay_cost=1)
	S += c_t0_t10 >= 29
	c_t0_t10 += MAS[2]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 29
	c_t1_t4_t3_in += MAS_in[0]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 29
	c_t1_t4_t3_mem0 += MAS_MEM[4]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 29
	c_t1_t4_t3_mem1 += MAS_MEM[1]

	c_t4_t20 = S.Task('c_t4_t20', length=3, delay_cost=1)
	S += c_t4_t20 >= 29
	c_t4_t20 += MAS[0]

	d_t0_t00_in = S.Task('d_t0_t00_in', length=1, delay_cost=1)
	S += d_t0_t00_in >= 29
	d_t0_t00_in += MAS_in[2]

	d_t0_t00_mem1 = S.Task('d_t0_t00_mem1', length=1, delay_cost=1)
	S += d_t0_t00_mem1 >= 29
	d_t0_t00_mem1 += MAS_MEM[5]

	d_t0_t01 = S.Task('d_t0_t01', length=3, delay_cost=1)
	S += d_t0_t01 >= 29
	d_t0_t01 += MAS[3]

	d_t1_t00_in = S.Task('d_t1_t00_in', length=1, delay_cost=1)
	S += d_t1_t00_in >= 29
	d_t1_t00_in += MAS_in[3]

	d_t1_t00_mem1 = S.Task('d_t1_t00_mem1', length=1, delay_cost=1)
	S += d_t1_t00_mem1 >= 29
	d_t1_t00_mem1 += MAS_MEM[7]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 29
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t30_in = S.Task('d_t1_t30_in', length=1, delay_cost=1)
	S += d_t1_t30_in >= 29
	d_t1_t30_in += MAS_in[1]

	d_t1_t30_mem0 = S.Task('d_t1_t30_mem0', length=1, delay_cost=1)
	S += d_t1_t30_mem0 >= 29
	d_t1_t30_mem0 += MM_MEM[0]

	d_t1_t30_mem1 = S.Task('d_t1_t30_mem1', length=1, delay_cost=1)
	S += d_t1_t30_mem1 >= 29
	d_t1_t30_mem1 += MM_MEM[1]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 29
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t4 = S.Task('d_t1_t3_t4', length=5, delay_cost=1)
	S += d_t1_t3_t4 >= 29
	d_t1_t3_t4 += MM[0]

	d_t2_t00 = S.Task('d_t2_t00', length=3, delay_cost=1)
	S += d_t2_t00 >= 29
	d_t2_t00 += MAS[1]

	d_t5_t3_t1_in = S.Task('d_t5_t3_t1_in', length=1, delay_cost=1)
	S += d_t5_t3_t1_in >= 29
	d_t5_t3_t1_in += MM_in[0]

	d_t5_t3_t1_mem0 = S.Task('d_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem0 >= 29
	d_t5_t3_t1_mem0 += MAS_MEM[6]

	d_t5_t3_t1_mem1 = S.Task('d_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem1 >= 29
	d_t5_t3_t1_mem1 += MAS_MEM[3]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 30
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 30
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=3, delay_cost=1)
	S += c_t1_t4_t3 >= 30
	c_t1_t4_t3 += MAS[0]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 30
	c_t2_t10_in += MAS_in[3]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 30
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 30
	c_t2_t10_mem1 += MM_MEM[1]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 30
	c_t3_t1_t3_in += MAS_in[0]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 30
	c_t3_t1_t3_mem0 += MAS_MEM[2]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 30
	c_t3_t1_t3_mem1 += MAS_MEM[7]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 30
	c_t5_t1_t3_in += MAS_in[2]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 30
	c_t5_t1_t3_mem0 += MAS_MEM[4]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 30
	c_t5_t1_t3_mem1 += MAS_MEM[1]

	d_t0_t00 = S.Task('d_t0_t00', length=3, delay_cost=1)
	S += d_t0_t00 >= 30
	d_t0_t00 += MAS[2]

	d_t0_t3_t4_in = S.Task('d_t0_t3_t4_in', length=1, delay_cost=1)
	S += d_t0_t3_t4_in >= 30
	d_t0_t3_t4_in += MM_in[0]

	d_t0_t3_t4_mem0 = S.Task('d_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem0 >= 30
	d_t0_t3_t4_mem0 += MAS_MEM[6]

	d_t0_t3_t4_mem1 = S.Task('d_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem1 >= 30
	d_t0_t3_t4_mem1 += MAS_MEM[3]

	d_t1_t00 = S.Task('d_t1_t00', length=3, delay_cost=1)
	S += d_t1_t00 >= 30
	d_t1_t00 += MAS[3]

	d_t1_t01_in = S.Task('d_t1_t01_in', length=1, delay_cost=1)
	S += d_t1_t01_in >= 30
	d_t1_t01_in += MAS_in[1]

	d_t1_t01_mem1 = S.Task('d_t1_t01_mem1', length=1, delay_cost=1)
	S += d_t1_t01_mem1 >= 30
	d_t1_t01_mem1 += MAS_MEM[5]

	d_t1_t30 = S.Task('d_t1_t30', length=3, delay_cost=1)
	S += d_t1_t30 >= 30
	d_t1_t30 += MAS[1]

	d_t5_t3_t1 = S.Task('d_t5_t3_t1', length=5, delay_cost=1)
	S += d_t5_t3_t1 >= 30
	d_t5_t3_t1 += MM[0]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 31
	c_t1_t00_in += MAS_in[3]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 31
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 31
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 31
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 31
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=3, delay_cost=1)
	S += c_t2_t10 >= 31
	c_t2_t10 += MAS[3]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 31
	c_t3_t0_t2_in += MAS_in[2]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 31
	c_t3_t0_t2_mem0 += MAS_MEM[4]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 31
	c_t3_t0_t2_mem1 += MAS_MEM[5]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 31
	c_t3_t0_t3_in += MAS_in[1]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 31
	c_t3_t0_t3_mem0 += MAS_MEM[6]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 31
	c_t3_t0_t3_mem1 += MAS_MEM[7]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=3, delay_cost=1)
	S += c_t3_t1_t3 >= 31
	c_t3_t1_t3 += MAS[0]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 31
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 31
	c_t4_t1_t0_mem0 += MAS_MEM[0]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 31
	c_t4_t1_t0_mem1 += MAS_MEM[1]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=3, delay_cost=1)
	S += c_t5_t1_t3 >= 31
	c_t5_t1_t3 += MAS[2]

	d_t0_t3_t4 = S.Task('d_t0_t3_t4', length=5, delay_cost=1)
	S += d_t0_t3_t4 >= 31
	d_t0_t3_t4 += MM[0]

	d_t1_t01 = S.Task('d_t1_t01', length=3, delay_cost=1)
	S += d_t1_t01 >= 31
	d_t1_t01 += MAS[1]

	d_t2_t01_in = S.Task('d_t2_t01_in', length=1, delay_cost=1)
	S += d_t2_t01_in >= 31
	d_t2_t01_in += MAS_in[0]

	d_t2_t01_mem1 = S.Task('d_t2_t01_mem1', length=1, delay_cost=1)
	S += d_t2_t01_mem1 >= 31
	d_t2_t01_mem1 += MAS_MEM[3]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 32
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t00 = S.Task('c_t1_t00', length=3, delay_cost=1)
	S += c_t1_t00 >= 32
	c_t1_t00 += MAS[3]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 32
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 32
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 32
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 32
	c_t1_t1_t4_mem1 += MAS_MEM[1]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 32
	c_t1_t1_t5_in += MAS_in[1]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 32
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 32
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=3, delay_cost=1)
	S += c_t3_t0_t2 >= 32
	c_t3_t0_t2 += MAS[2]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=3, delay_cost=1)
	S += c_t3_t0_t3 >= 32
	c_t3_t0_t3 += MAS[1]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 32
	c_t3_t31_in += MAS_in[2]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 32
	c_t3_t31_mem0 += MAS_MEM[6]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 32
	c_t3_t31_mem1 += MAS_MEM[7]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 32
	c_t4_t0_t3_in += MAS_in[3]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 32
	c_t4_t0_t3_mem0 += MAS_MEM[4]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 32
	c_t4_t0_t3_mem1 += MAS_MEM[3]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=5, delay_cost=1)
	S += c_t4_t1_t0 >= 32
	c_t4_t1_t0 += MM[0]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 32
	c_t4_t31_in += MAS_in[0]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 32
	c_t4_t31_mem0 += MAS_MEM[2]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 32
	c_t4_t31_mem1 += MAS_MEM[5]

	d_t2_t01 = S.Task('d_t2_t01', length=3, delay_cost=1)
	S += d_t2_t01 >= 32
	d_t2_t01 += MAS[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 33
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 33
	c_t1_t0_t5_in += MAS_in[2]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 33
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 33
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=5, delay_cost=1)
	S += c_t1_t1_t4 >= 33
	c_t1_t1_t4 += MM[0]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=3, delay_cost=1)
	S += c_t1_t1_t5 >= 33
	c_t1_t1_t5 += MAS[1]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 33
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 33
	c_t1_t4_t1_mem0 += MAS_MEM[4]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 33
	c_t1_t4_t1_mem1 += MAS_MEM[1]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 33
	c_t1_t4_t2_in += MAS_in[3]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 33
	c_t1_t4_t2_mem0 += MAS_MEM[2]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 33
	c_t1_t4_t2_mem1 += MAS_MEM[5]

	c_t3_t31 = S.Task('c_t3_t31', length=3, delay_cost=1)
	S += c_t3_t31 >= 33
	c_t3_t31 += MAS[2]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=3, delay_cost=1)
	S += c_t4_t0_t3 >= 33
	c_t4_t0_t3 += MAS[3]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 33
	c_t4_t21_in += MAS_in[1]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 33
	c_t4_t21_mem0 += MAS_MEM[0]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 33
	c_t4_t21_mem1 += MAS_MEM[7]

	c_t4_t31 = S.Task('c_t4_t31', length=3, delay_cost=1)
	S += c_t4_t31 >= 33
	c_t4_t31 += MAS[0]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 33
	c_t5_t0_t2_in += MAS_in[0]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 33
	c_t5_t0_t2_mem0 += MAS_MEM[6]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 33
	c_t5_t0_t2_mem1 += MAS_MEM[3]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 33
	d_t5010_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 34
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 34
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 34
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 34
	c_t0_t4_t3_mem0 += MAS_MEM[4]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 34
	c_t0_t4_t3_mem1 += MAS_MEM[7]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 34
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 34
	c_t1_t0_t4_mem0 += MAS_MEM[0]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 34
	c_t1_t0_t4_mem1 += MAS_MEM[3]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=3, delay_cost=1)
	S += c_t1_t0_t5 >= 34
	c_t1_t0_t5 += MAS[2]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 34
	c_t1_t10_in += MAS_in[3]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 34
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 34
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=5, delay_cost=1)
	S += c_t1_t4_t1 >= 34
	c_t1_t4_t1 += MM[0]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=3, delay_cost=1)
	S += c_t1_t4_t2 >= 34
	c_t1_t4_t2 += MAS[3]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 34
	c_t2_t4_t2_in += MAS_in[0]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 34
	c_t2_t4_t2_mem0 += MAS_MEM[2]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 34
	c_t2_t4_t2_mem1 += MAS_MEM[5]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 34
	c_t4_t0_t2_in += MAS_in[2]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 34
	c_t4_t0_t2_mem0 += MAS_MEM[6]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 34
	c_t4_t0_t2_mem1 += MAS_MEM[1]

	c_t4_t21 = S.Task('c_t4_t21', length=3, delay_cost=1)
	S += c_t4_t21 >= 34
	c_t4_t21 += MAS[1]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=3, delay_cost=1)
	S += c_t5_t0_t2 >= 34
	c_t5_t0_t2 += MAS[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 35
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=3, delay_cost=1)
	S += c_t0_t4_t3 >= 35
	c_t0_t4_t3 += MAS[1]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=5, delay_cost=1)
	S += c_t1_t0_t4 >= 35
	c_t1_t0_t4 += MM[0]

	c_t1_t10 = S.Task('c_t1_t10', length=3, delay_cost=1)
	S += c_t1_t10 >= 35
	c_t1_t10 += MAS[3]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 35
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 35
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 35
	c_t2_t0_t4_mem0 += MAS_MEM[2]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 35
	c_t2_t0_t4_mem1 += MAS_MEM[3]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 35
	c_t2_t0_t5_in += MAS_in[0]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 35
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 35
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=3, delay_cost=1)
	S += c_t2_t4_t2 >= 35
	c_t2_t4_t2 += MAS[0]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 35
	c_t3_t20_in += MAS_in[1]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 35
	c_t3_t20_mem0 += MAS_MEM[4]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 35
	c_t3_t20_mem1 += MAS_MEM[5]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=3, delay_cost=1)
	S += c_t4_t0_t2 >= 35
	c_t4_t0_t2 += MAS[2]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 35
	c_t4_t1_t2_in += MAS_in[2]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 35
	c_t4_t1_t2_mem0 += MAS_MEM[0]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 35
	c_t4_t1_t2_mem1 += MAS_MEM[7]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 35
	c_t5_t0_t3_in += MAS_in[3]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 35
	c_t5_t0_t3_mem0 += MAS_MEM[6]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 35
	c_t5_t0_t3_mem1 += MAS_MEM[1]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 36
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 36
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 36
	c_t2_t00_in += MAS_in[1]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 36
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 36
	c_t2_t00_mem1 += MM_MEM[1]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=5, delay_cost=1)
	S += c_t2_t0_t4 >= 36
	c_t2_t0_t4 += MM[0]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=3, delay_cost=1)
	S += c_t2_t0_t5 >= 36
	c_t2_t0_t5 += MAS[0]

	c_t3_t20 = S.Task('c_t3_t20', length=3, delay_cost=1)
	S += c_t3_t20 >= 36
	c_t3_t20 += MAS[1]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 36
	c_t3_t30_in += MAS_in[3]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 36
	c_t3_t30_mem0 += MAS_MEM[6]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 36
	c_t3_t30_mem1 += MAS_MEM[3]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=3, delay_cost=1)
	S += c_t4_t1_t2 >= 36
	c_t4_t1_t2 += MAS[2]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 36
	c_t4_t1_t3_in += MAS_in[2]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 36
	c_t4_t1_t3_mem0 += MAS_MEM[0]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 36
	c_t4_t1_t3_mem1 += MAS_MEM[5]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 36
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 36
	c_t5_t0_t1_mem0 += MAS_MEM[2]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 36
	c_t5_t0_t1_mem1 += MAS_MEM[1]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=3, delay_cost=1)
	S += c_t5_t0_t3 >= 36
	c_t5_t0_t3 += MAS[3]

	d_t0_t2_t2_in = S.Task('d_t0_t2_t2_in', length=1, delay_cost=1)
	S += d_t0_t2_t2_in >= 36
	d_t0_t2_t2_in += MAS_in[0]

	d_t0_t2_t2_mem0 = S.Task('d_t0_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t2_mem0 >= 36
	d_t0_t2_t2_mem0 += MAS_MEM[4]

	d_t0_t2_t2_mem1 = S.Task('d_t0_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t2_mem1 >= 36
	d_t0_t2_t2_mem1 += MAS_MEM[7]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 37
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 37
	c_t0_t4_t2_in += MAS_in[3]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 37
	c_t0_t4_t2_mem0 += MAS_MEM[6]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 37
	c_t0_t4_t2_mem1 += MAS_MEM[5]

	c_t2_t00 = S.Task('c_t2_t00', length=3, delay_cost=1)
	S += c_t2_t00 >= 37
	c_t2_t00 += MAS[1]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 37
	c_t2_t1_t5_in += MAS_in[2]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 37
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 37
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t3_t30 = S.Task('c_t3_t30', length=3, delay_cost=1)
	S += c_t3_t30 >= 37
	c_t3_t30 += MAS[3]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 37
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 37
	c_t4_t0_t1_mem0 += MAS_MEM[0]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 37
	c_t4_t0_t1_mem1 += MAS_MEM[3]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=3, delay_cost=1)
	S += c_t4_t1_t3 >= 37
	c_t4_t1_t3 += MAS[2]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=5, delay_cost=1)
	S += c_t5_t0_t1 >= 37
	c_t5_t0_t1 += MM[0]

	d_t0_t2_t2 = S.Task('d_t0_t2_t2', length=3, delay_cost=1)
	S += d_t0_t2_t2 >= 37
	d_t0_t2_t2 += MAS[0]

	d_t110_in = S.Task('d_t110_in', length=1, delay_cost=1)
	S += d_t110_in >= 37
	d_t110_in += MAS_in[1]

	d_t110_mem0 = S.Task('d_t110_mem0', length=1, delay_cost=1)
	S += d_t110_mem0 >= 37
	d_t110_mem0 += MAS_MEM[2]

	d_t3_t2_t3_in = S.Task('d_t3_t2_t3_in', length=1, delay_cost=1)
	S += d_t3_t2_t3_in >= 37
	d_t3_t2_t3_in += MAS_in[0]

	d_t3_t2_t3_mem0 = S.Task('d_t3_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t3_mem0 >= 37
	d_t3_t2_t3_mem0 += MAS_MEM[4]

	d_t3_t2_t3_mem1 = S.Task('d_t3_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t3_mem1 >= 37
	d_t3_t2_t3_mem1 += MAS_MEM[1]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 37
	d_t5011_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=3, delay_cost=1)
	S += c_t0_t4_t2 >= 38
	c_t0_t4_t2 += MAS[3]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 38
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=3, delay_cost=1)
	S += c_t2_t1_t5 >= 38
	c_t2_t1_t5 += MAS[2]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 38
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 38
	c_t3_t1_t0_mem0 += MAS_MEM[4]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 38
	c_t3_t1_t0_mem1 += MAS_MEM[3]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=5, delay_cost=1)
	S += c_t4_t0_t1 >= 38
	c_t4_t0_t1 += MM[0]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 38
	c_t5_t30_in += MAS_in[0]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 38
	c_t5_t30_mem0 += MAS_MEM[6]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 38
	c_t5_t30_mem1 += MAS_MEM[5]

	d_t010_in = S.Task('d_t010_in', length=1, delay_cost=1)
	S += d_t010_in >= 38
	d_t010_in += MAS_in[3]

	d_t010_mem0 = S.Task('d_t010_mem0', length=1, delay_cost=1)
	S += d_t010_mem0 >= 38
	d_t010_mem0 += MAS_MEM[0]

	d_t110 = S.Task('d_t110', length=3, delay_cost=1)
	S += d_t110 >= 38
	d_t110 += MAS[1]

	d_t2_t2_t2_in = S.Task('d_t2_t2_t2_in', length=1, delay_cost=1)
	S += d_t2_t2_t2_in >= 38
	d_t2_t2_t2_in += MAS_in[2]

	d_t2_t2_t2_mem0 = S.Task('d_t2_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t2_mem0 >= 38
	d_t2_t2_t2_mem0 += MAS_MEM[2]

	d_t2_t2_t2_mem1 = S.Task('d_t2_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t2_mem1 >= 38
	d_t2_t2_t2_mem1 += MAS_MEM[1]

	d_t3_t2_t3 = S.Task('d_t3_t2_t3', length=3, delay_cost=1)
	S += d_t3_t2_t3 >= 38
	d_t3_t2_t3 += MAS[0]

	d_t4_t3_t5_in = S.Task('d_t4_t3_t5_in', length=1, delay_cost=1)
	S += d_t4_t3_t5_in >= 38
	d_t4_t3_t5_in += MAS_in[1]

	d_t4_t3_t5_mem0 = S.Task('d_t4_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t5_mem0 >= 38
	d_t4_t3_t5_mem0 += MM_MEM[0]

	d_t4_t3_t5_mem1 = S.Task('d_t4_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t5_mem1 >= 38
	d_t4_t3_t5_mem1 += MM_MEM[1]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 38
	d_t5001_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 39
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 39
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=5, delay_cost=1)
	S += c_t3_t1_t0 >= 39
	c_t3_t1_t0 += MM[0]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 39
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 39
	c_t3_t1_t1_mem0 += MAS_MEM[0]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 39
	c_t3_t1_t1_mem1 += MAS_MEM[7]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 39
	c_t5_t1_t2_in += MAS_in[1]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 39
	c_t5_t1_t2_mem0 += MAS_MEM[4]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 39
	c_t5_t1_t2_mem1 += MAS_MEM[3]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 39
	c_t5_t20_in += MAS_in[2]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 39
	c_t5_t20_mem0 += MAS_MEM[6]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 39
	c_t5_t20_mem1 += MAS_MEM[5]

	c_t5_t30 = S.Task('c_t5_t30', length=3, delay_cost=1)
	S += c_t5_t30 >= 39
	c_t5_t30 += MAS[0]

	d_t010 = S.Task('d_t010', length=3, delay_cost=1)
	S += d_t010 >= 39
	d_t010 += MAS[3]

	d_t2_t2_t2 = S.Task('d_t2_t2_t2', length=3, delay_cost=1)
	S += d_t2_t2_t2 >= 39
	d_t2_t2_t2 += MAS[2]

	d_t4_t01_in = S.Task('d_t4_t01_in', length=1, delay_cost=1)
	S += d_t4_t01_in >= 39
	d_t4_t01_in += MAS_in[3]

	d_t4_t01_mem0 = S.Task('d_t4_t01_mem0', length=1, delay_cost=1)
	S += d_t4_t01_mem0 >= 39
	d_t4_t01_mem0 += MAS_MEM[2]

	d_t4_t01_mem1 = S.Task('d_t4_t01_mem1', length=1, delay_cost=1)
	S += d_t4_t01_mem1 >= 39
	d_t4_t01_mem1 += MAS_MEM[1]

	d_t4_t3_t5 = S.Task('d_t4_t3_t5', length=3, delay_cost=1)
	S += d_t4_t3_t5 >= 39
	d_t4_t3_t5 += MAS[1]

	d_t5_t3_t5_in = S.Task('d_t5_t3_t5_in', length=1, delay_cost=1)
	S += d_t5_t3_t5_in >= 39
	d_t5_t3_t5_in += MAS_in[0]

	d_t5_t3_t5_mem0 = S.Task('d_t5_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t5_mem0 >= 39
	d_t5_t3_t5_mem0 += MM_MEM[0]

	d_t5_t3_t5_mem1 = S.Task('d_t5_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t5_mem1 >= 39
	d_t5_t3_t5_mem1 += MM_MEM[1]

	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	S += c_t0_t4_t5_in >= 40
	c_t0_t4_t5_in += MAS_in[0]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem0 >= 40
	c_t0_t4_t5_mem0 += MM_MEM[0]

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem1 >= 40
	c_t0_t4_t5_mem1 += MM_MEM[1]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 40
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 40
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 40
	c_t3_t0_t1_in += MM_in[0]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 40
	c_t3_t0_t1_mem0 += MAS_MEM[4]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 40
	c_t3_t0_t1_mem1 += MAS_MEM[7]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=5, delay_cost=1)
	S += c_t3_t1_t1 >= 40
	c_t3_t1_t1 += MM[0]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=3, delay_cost=1)
	S += c_t5_t1_t2 >= 40
	c_t5_t1_t2 += MAS[1]

	c_t5_t20 = S.Task('c_t5_t20', length=3, delay_cost=1)
	S += c_t5_t20 >= 40
	c_t5_t20 += MAS[2]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 40
	c_t5_t21_in += MAS_in[3]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 40
	c_t5_t21_mem0 += MAS_MEM[2]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 40
	c_t5_t21_mem1 += MAS_MEM[3]

	d_t210_in = S.Task('d_t210_in', length=1, delay_cost=1)
	S += d_t210_in >= 40
	d_t210_in += MAS_in[2]

	d_t210_mem0 = S.Task('d_t210_mem0', length=1, delay_cost=1)
	S += d_t210_mem0 >= 40
	d_t210_mem0 += MAS_MEM[6]

	d_t3_t01_in = S.Task('d_t3_t01_in', length=1, delay_cost=1)
	S += d_t3_t01_in >= 40
	d_t3_t01_in += MAS_in[1]

	d_t3_t01_mem0 = S.Task('d_t3_t01_mem0', length=1, delay_cost=1)
	S += d_t3_t01_mem0 >= 40
	d_t3_t01_mem0 += MAS_MEM[0]

	d_t3_t01_mem1 = S.Task('d_t3_t01_mem1', length=1, delay_cost=1)
	S += d_t3_t01_mem1 >= 40
	d_t3_t01_mem1 += MAS_MEM[5]

	d_t4_t01 = S.Task('d_t4_t01', length=3, delay_cost=1)
	S += d_t4_t01 >= 40
	d_t4_t01 += MAS[3]

	d_t5_t3_t5 = S.Task('d_t5_t3_t5', length=3, delay_cost=1)
	S += d_t5_t3_t5 >= 40
	d_t5_t3_t5 += MAS[0]

	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	S += c_t0_t40_in >= 41
	c_t0_t40_in += MAS_in[0]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 41
	c_t0_t40_mem0 += MM_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 41
	c_t0_t40_mem1 += MM_MEM[1]

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=3, delay_cost=1)
	S += c_t0_t4_t5 >= 41
	c_t0_t4_t5 += MAS[0]

	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	S += c_t0_t50_in >= 41
	c_t0_t50_in += MAS_in[3]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 41
	c_t0_t50_mem0 += MAS_MEM[2]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 41
	c_t0_t50_mem1 += MAS_MEM[5]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 41
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 41
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=5, delay_cost=1)
	S += c_t3_t0_t1 >= 41
	c_t3_t0_t1 += MM[0]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 41
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 41
	c_t5_t0_t0_mem0 += MAS_MEM[6]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 41
	c_t5_t0_t0_mem1 += MAS_MEM[7]

	c_t5_t21 = S.Task('c_t5_t21', length=3, delay_cost=1)
	S += c_t5_t21 >= 41
	c_t5_t21 += MAS[3]

	c_t5_t4_t3_in = S.Task('c_t5_t4_t3_in', length=1, delay_cost=1)
	S += c_t5_t4_t3_in >= 41
	c_t5_t4_t3_in += MAS_in[2]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem0 >= 41
	c_t5_t4_t3_mem0 += MAS_MEM[0]

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem1 >= 41
	c_t5_t4_t3_mem1 += MAS_MEM[1]

	d_t210 = S.Task('d_t210', length=3, delay_cost=1)
	S += d_t210 >= 41
	d_t210 += MAS[2]

	d_t3_t01 = S.Task('d_t3_t01', length=3, delay_cost=1)
	S += d_t3_t01 >= 41
	d_t3_t01 += MAS[1]

	d_t4_t2_t3_in = S.Task('d_t4_t2_t3_in', length=1, delay_cost=1)
	S += d_t4_t2_t3_in >= 41
	d_t4_t2_t3_in += MAS_in[1]

	d_t4_t2_t3_mem0 = S.Task('d_t4_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t3_mem0 >= 41
	d_t4_t2_t3_mem0 += MAS_MEM[4]

	d_t4_t2_t3_mem1 = S.Task('d_t4_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t3_mem1 >= 41
	d_t4_t2_t3_mem1 += MAS_MEM[3]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 42
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t40 = S.Task('c_t0_t40', length=3, delay_cost=1)
	S += c_t0_t40 >= 42
	c_t0_t40 += MAS[0]

	c_t0_t50 = S.Task('c_t0_t50', length=3, delay_cost=1)
	S += c_t0_t50 >= 42
	c_t0_t50 += MAS[3]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 42
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	S += c_t2_t50_in >= 42
	c_t2_t50_in += MAS_in[2]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 42
	c_t2_t50_mem0 += MAS_MEM[2]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 42
	c_t2_t50_mem1 += MAS_MEM[7]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 42
	c_t4_t0_t0_in += MM_in[0]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 42
	c_t4_t0_t0_mem0 += MAS_MEM[6]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 42
	c_t4_t0_t0_mem1 += MAS_MEM[5]

	c_t4_t4_t3_in = S.Task('c_t4_t4_t3_in', length=1, delay_cost=1)
	S += c_t4_t4_t3_in >= 42
	c_t4_t4_t3_in += MAS_in[0]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem0 >= 42
	c_t4_t4_t3_mem0 += MAS_MEM[4]

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem1 >= 42
	c_t4_t4_t3_mem1 += MAS_MEM[1]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=5, delay_cost=1)
	S += c_t5_t0_t0 >= 42
	c_t5_t0_t0 += MM[0]

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=3, delay_cost=1)
	S += c_t5_t4_t3 >= 42
	c_t5_t4_t3 += MAS[2]

	d_t3_t30_in = S.Task('d_t3_t30_in', length=1, delay_cost=1)
	S += d_t3_t30_in >= 42
	d_t3_t30_in += MAS_in[3]

	d_t3_t30_mem0 = S.Task('d_t3_t30_mem0', length=1, delay_cost=1)
	S += d_t3_t30_mem0 >= 42
	d_t3_t30_mem0 += MM_MEM[0]

	d_t3_t30_mem1 = S.Task('d_t3_t30_mem1', length=1, delay_cost=1)
	S += d_t3_t30_mem1 >= 42
	d_t3_t30_mem1 += MM_MEM[1]

	d_t4_t00_in = S.Task('d_t4_t00_in', length=1, delay_cost=1)
	S += d_t4_t00_in >= 42
	d_t4_t00_in += MAS_in[1]

	d_t4_t00_mem0 = S.Task('d_t4_t00_mem0', length=1, delay_cost=1)
	S += d_t4_t00_mem0 >= 42
	d_t4_t00_mem0 += MAS_MEM[0]

	d_t4_t00_mem1 = S.Task('d_t4_t00_mem1', length=1, delay_cost=1)
	S += d_t4_t00_mem1 >= 42
	d_t4_t00_mem1 += MAS_MEM[3]

	d_t4_t2_t3 = S.Task('d_t4_t2_t3', length=3, delay_cost=1)
	S += d_t4_t2_t3 >= 42
	d_t4_t2_t3 += MAS[1]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 43
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 43
	c_t1_t11_in += MAS_in[3]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 43
	c_t1_t11_mem0 += MM_MEM[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 43
	c_t1_t11_mem1 += MAS_MEM[3]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 43
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	S += c_t1_t50_in >= 43
	c_t1_t50_in += MAS_in[2]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 43
	c_t1_t50_mem0 += MAS_MEM[6]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 43
	c_t1_t50_mem1 += MAS_MEM[7]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 43
	c_t2_t4_t1_in += MM_in[0]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 43
	c_t2_t4_t1_mem0 += MAS_MEM[4]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 43
	c_t2_t4_t1_mem1 += MAS_MEM[1]

	c_t2_t50 = S.Task('c_t2_t50', length=3, delay_cost=1)
	S += c_t2_t50 >= 43
	c_t2_t50 += MAS[2]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=5, delay_cost=1)
	S += c_t4_t0_t0 >= 43
	c_t4_t0_t0 += MM[0]

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=3, delay_cost=1)
	S += c_t4_t4_t3 >= 43
	c_t4_t4_t3 += MAS[0]

	d_t3_t00_in = S.Task('d_t3_t00_in', length=1, delay_cost=1)
	S += d_t3_t00_in >= 43
	d_t3_t00_in += MAS_in[0]

	d_t3_t00_mem0 = S.Task('d_t3_t00_mem0', length=1, delay_cost=1)
	S += d_t3_t00_mem0 >= 43
	d_t3_t00_mem0 += MAS_MEM[2]

	d_t3_t00_mem1 = S.Task('d_t3_t00_mem1', length=1, delay_cost=1)
	S += d_t3_t00_mem1 >= 43
	d_t3_t00_mem1 += MAS_MEM[5]

	d_t3_t30 = S.Task('d_t3_t30', length=3, delay_cost=1)
	S += d_t3_t30 >= 43
	d_t3_t30 += MAS[3]

	d_t4_t00 = S.Task('d_t4_t00', length=3, delay_cost=1)
	S += d_t4_t00 >= 43
	d_t4_t00 += MAS[1]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 44
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 44
	c_t1_t01_in += MAS_in[3]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 44
	c_t1_t01_mem0 += MM_MEM[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 44
	c_t1_t01_mem1 += MAS_MEM[5]

	c_t1_t11 = S.Task('c_t1_t11', length=3, delay_cost=1)
	S += c_t1_t11 >= 44
	c_t1_t11 += MAS[3]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 44
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t50 = S.Task('c_t1_t50', length=3, delay_cost=1)
	S += c_t1_t50 >= 44
	c_t1_t50 += MAS[2]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 44
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 44
	c_t2_t1_t4_mem0 += MAS_MEM[6]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 44
	c_t2_t1_t4_mem1 += MAS_MEM[1]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=5, delay_cost=1)
	S += c_t2_t4_t1 >= 44
	c_t2_t4_t1 += MM[0]

	c_t4_t4_t2_in = S.Task('c_t4_t4_t2_in', length=1, delay_cost=1)
	S += c_t4_t4_t2_in >= 44
	c_t4_t4_t2_in += MAS_in[2]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem0 >= 44
	c_t4_t4_t2_mem0 += MAS_MEM[0]

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem1 >= 44
	c_t4_t4_t2_mem1 += MAS_MEM[3]

	c_t5_t4_t2_in = S.Task('c_t5_t4_t2_in', length=1, delay_cost=1)
	S += c_t5_t4_t2_in >= 44
	c_t5_t4_t2_in += MAS_in[0]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem0 >= 44
	c_t5_t4_t2_mem0 += MAS_MEM[4]

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem1 >= 44
	c_t5_t4_t2_mem1 += MAS_MEM[7]

	d_t3_t00 = S.Task('d_t3_t00', length=3, delay_cost=1)
	S += d_t3_t00 >= 44
	d_t3_t00 += MAS[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 45
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t01 = S.Task('c_t1_t01', length=3, delay_cost=1)
	S += c_t1_t01 >= 45
	c_t1_t01 += MAS[3]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=5, delay_cost=1)
	S += c_t2_t1_t4 >= 45
	c_t2_t1_t4 += MM[0]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 45
	c_t3_t0_t0_in += MM_in[0]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 45
	c_t3_t0_t0_mem0 += MAS_MEM[4]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 45
	c_t3_t0_t0_mem1 += MAS_MEM[7]

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=3, delay_cost=1)
	S += c_t4_t4_t2 >= 45
	c_t4_t4_t2 += MAS[2]

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=3, delay_cost=1)
	S += c_t5_t4_t2 >= 45
	c_t5_t4_t2 += MAS[0]

	d_t0_t31_in = S.Task('d_t0_t31_in', length=1, delay_cost=1)
	S += d_t0_t31_in >= 45
	d_t0_t31_in += MAS_in[2]

	d_t0_t31_mem0 = S.Task('d_t0_t31_mem0', length=1, delay_cost=1)
	S += d_t0_t31_mem0 >= 45
	d_t0_t31_mem0 += MM_MEM[0]

	d_t0_t31_mem1 = S.Task('d_t0_t31_mem1', length=1, delay_cost=1)
	S += d_t0_t31_mem1 >= 45
	d_t0_t31_mem1 += MAS_MEM[5]

	d_t1_t2_t2_in = S.Task('d_t1_t2_t2_in', length=1, delay_cost=1)
	S += d_t1_t2_t2_in >= 45
	d_t1_t2_t2_in += MAS_in[0]

	d_t1_t2_t2_mem0 = S.Task('d_t1_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t2_mem0 >= 45
	d_t1_t2_t2_mem0 += MAS_MEM[6]

	d_t1_t2_t2_mem1 = S.Task('d_t1_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t2_mem1 >= 45
	d_t1_t2_t2_mem1 += MAS_MEM[3]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 45
	d_t5001_mem1 += MAIN_MEM_r[1]

	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	S += c_t010_in >= 46
	c_t010_in += MAS_in[1]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 46
	c_t010_mem0 += MAS_MEM[0]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 46
	c_t010_mem1 += MAS_MEM[7]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 46
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 46
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 46
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 46
	c_t2_t4_t0_mem0 += MAS_MEM[2]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 46
	c_t2_t4_t0_mem1 += MAS_MEM[5]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=5, delay_cost=1)
	S += c_t3_t0_t0 >= 46
	c_t3_t0_t0 += MM[0]

	d_t0_t31 = S.Task('d_t0_t31', length=3, delay_cost=1)
	S += d_t0_t31 >= 46
	d_t0_t31 += MAS[2]

	d_t1_t2_t2 = S.Task('d_t1_t2_t2', length=3, delay_cost=1)
	S += d_t1_t2_t2 >= 46
	d_t1_t2_t2 += MAS[0]

	d_t2_t31_in = S.Task('d_t2_t31_in', length=1, delay_cost=1)
	S += d_t2_t31_in >= 46
	d_t2_t31_in += MAS_in[2]

	d_t2_t31_mem0 = S.Task('d_t2_t31_mem0', length=1, delay_cost=1)
	S += d_t2_t31_mem0 >= 46
	d_t2_t31_mem0 += MM_MEM[0]

	d_t2_t31_mem1 = S.Task('d_t2_t31_mem1', length=1, delay_cost=1)
	S += d_t2_t31_mem1 >= 46
	d_t2_t31_mem1 += MAS_MEM[1]

	d_t5_t00_in = S.Task('d_t5_t00_in', length=1, delay_cost=1)
	S += d_t5_t00_in >= 46
	d_t5_t00_in += MAS_in[0]

	d_t5_t00_mem0 = S.Task('d_t5_t00_mem0', length=1, delay_cost=1)
	S += d_t5_t00_mem0 >= 46
	d_t5_t00_mem0 += MAS_MEM[6]

	d_t5_t00_mem1 = S.Task('d_t5_t00_mem1', length=1, delay_cost=1)
	S += d_t5_t00_mem1 >= 46
	d_t5_t00_mem1 += MAS_MEM[3]

	c_t010 = S.Task('c_t010', length=3, delay_cost=1)
	S += c_t010 >= 47
	c_t010 += MAS[1]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 47
	c_t0_t11_in += MAS_in[1]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 47
	c_t0_t11_mem0 += MM_MEM[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 47
	c_t0_t11_mem1 += MAS_MEM[1]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 47
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 47
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 47
	c_t1_t4_t0_mem0 += MAS_MEM[2]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 47
	c_t1_t4_t0_mem1 += MAS_MEM[5]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=5, delay_cost=1)
	S += c_t2_t4_t0 >= 47
	c_t2_t4_t0 += MM[0]

	d_s2010_in = S.Task('d_s2010_in', length=1, delay_cost=1)
	S += d_s2010_in >= 47
	d_s2010_in += MAS_in[0]

	d_s2010_mem0 = S.Task('d_s2010_mem0', length=1, delay_cost=1)
	S += d_s2010_mem0 >= 47
	d_s2010_mem0 += MAS_MEM[4]

	d_s2010_mem1 = S.Task('d_s2010_mem1', length=1, delay_cost=1)
	S += d_s2010_mem1 >= 47
	d_s2010_mem1 += MAS_MEM[7]

	d_t2_t31 = S.Task('d_t2_t31', length=3, delay_cost=1)
	S += d_t2_t31 >= 47
	d_t2_t31 += MAS[2]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 47
	d_t5000_mem1 += MAIN_MEM_r[1]

	d_t5_t00 = S.Task('d_t5_t00', length=3, delay_cost=1)
	S += d_t5_t00 >= 47
	d_t5_t00 += MAS[0]

	d_t5_t2_t3_in = S.Task('d_t5_t2_t3_in', length=1, delay_cost=1)
	S += d_t5_t2_t3_in >= 47
	d_t5_t2_t3_in += MAS_in[3]

	d_t5_t2_t3_mem0 = S.Task('d_t5_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t3_mem0 >= 47
	d_t5_t2_t3_mem0 += MAS_MEM[6]

	d_t5_t2_t3_mem1 = S.Task('d_t5_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t3_mem1 >= 47
	d_t5_t2_t3_mem1 += MAS_MEM[3]

	c_t0_t11 = S.Task('c_t0_t11', length=3, delay_cost=1)
	S += c_t0_t11 >= 48
	c_t0_t11 += MAS[1]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 48
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=5, delay_cost=1)
	S += c_t1_t4_t0 >= 48
	c_t1_t4_t0 += MM[0]

	c_t3_t4_t2_in = S.Task('c_t3_t4_t2_in', length=1, delay_cost=1)
	S += c_t3_t4_t2_in >= 48
	c_t3_t4_t2_in += MAS_in[2]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem0 >= 48
	c_t3_t4_t2_mem0 += MAS_MEM[2]

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem1 >= 48
	c_t3_t4_t2_mem1 += MAS_MEM[3]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 48
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 48
	c_t4_t1_t1_mem0 += MAS_MEM[6]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 48
	c_t4_t1_t1_mem1 += MAS_MEM[5]

	d_s2010 = S.Task('d_s2010', length=3, delay_cost=1)
	S += d_s2010 >= 48
	d_s2010 += MAS[0]

	d_t0_t41_in = S.Task('d_t0_t41_in', length=1, delay_cost=1)
	S += d_t0_t41_in >= 48
	d_t0_t41_in += MAS_in[3]

	d_t0_t41_mem0 = S.Task('d_t0_t41_mem0', length=1, delay_cost=1)
	S += d_t0_t41_mem0 >= 48
	d_t0_t41_mem0 += MAS_MEM[4]

	d_t0_t41_mem1 = S.Task('d_t0_t41_mem1', length=1, delay_cost=1)
	S += d_t0_t41_mem1 >= 48
	d_t0_t41_mem1 += MAS_MEM[1]

	d_t3_t3_t5_in = S.Task('d_t3_t3_t5_in', length=1, delay_cost=1)
	S += d_t3_t3_t5_in >= 48
	d_t3_t3_t5_in += MAS_in[0]

	d_t3_t3_t5_mem0 = S.Task('d_t3_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t5_mem0 >= 48
	d_t3_t3_t5_mem0 += MM_MEM[0]

	d_t3_t3_t5_mem1 = S.Task('d_t3_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t5_mem1 >= 48
	d_t3_t3_t5_mem1 += MM_MEM[1]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 48
	d_t5011_mem1 += MAIN_MEM_r[1]

	d_t5_t2_t3 = S.Task('d_t5_t2_t3', length=3, delay_cost=1)
	S += d_t5_t2_t3 >= 48
	d_t5_t2_t3 += MAS[3]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 49
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=3, delay_cost=1)
	S += c_t3_t4_t2 >= 49
	c_t3_t4_t2 += MAS[2]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=5, delay_cost=1)
	S += c_t4_t1_t1 >= 49
	c_t4_t1_t1 += MM[0]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 49
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 49
	c_t5_t1_t0_mem0 += MAS_MEM[4]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 49
	c_t5_t1_t0_mem1 += MAS_MEM[5]

	d_t0_t41 = S.Task('d_t0_t41', length=3, delay_cost=1)
	S += d_t0_t41 >= 49
	d_t0_t41 += MAS[3]

	d_t3_t3_t5 = S.Task('d_t3_t3_t5', length=3, delay_cost=1)
	S += d_t3_t3_t5 >= 49
	d_t3_t3_t5 += MAS[0]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 49
	d_t4011_mem1 += MAIN_MEM_r[1]

	d_t4_t2_t2_in = S.Task('d_t4_t2_t2_in', length=1, delay_cost=1)
	S += d_t4_t2_t2_in >= 49
	d_t4_t2_t2_in += MAS_in[1]

	d_t4_t2_t2_mem0 = S.Task('d_t4_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t2_mem0 >= 49
	d_t4_t2_t2_mem0 += MAS_MEM[2]

	d_t4_t2_t2_mem1 = S.Task('d_t4_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t2_mem1 >= 49
	d_t4_t2_t2_mem1 += MAS_MEM[7]

	d_t5_t01_in = S.Task('d_t5_t01_in', length=1, delay_cost=1)
	S += d_t5_t01_in >= 49
	d_t5_t01_in += MAS_in[2]

	d_t5_t01_mem0 = S.Task('d_t5_t01_mem0', length=1, delay_cost=1)
	S += d_t5_t01_mem0 >= 49
	d_t5_t01_mem0 += MAS_MEM[6]

	d_t5_t01_mem1 = S.Task('d_t5_t01_mem1', length=1, delay_cost=1)
	S += d_t5_t01_mem1 >= 49
	d_t5_t01_mem1 += MAS_MEM[3]

	d_t5_t30_in = S.Task('d_t5_t30_in', length=1, delay_cost=1)
	S += d_t5_t30_in >= 49
	d_t5_t30_in += MAS_in[3]

	d_t5_t30_mem0 = S.Task('d_t5_t30_mem0', length=1, delay_cost=1)
	S += d_t5_t30_mem0 >= 49
	d_t5_t30_mem0 += MM_MEM[0]

	d_t5_t30_mem1 = S.Task('d_t5_t30_mem1', length=1, delay_cost=1)
	S += d_t5_t30_mem1 >= 49
	d_t5_t30_mem1 += MM_MEM[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 50
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 50
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_s00_in = S.Task('c_t1_s00_in', length=1, delay_cost=1)
	S += c_t1_s00_in >= 50
	c_t1_s00_in += MAS_in[1]

	c_t1_s00_mem0 = S.Task('c_t1_s00_mem0', length=1, delay_cost=1)
	S += c_t1_s00_mem0 >= 50
	c_t1_s00_mem0 += MAS_MEM[6]

	c_t1_s00_mem1 = S.Task('c_t1_s00_mem1', length=1, delay_cost=1)
	S += c_t1_s00_mem1 >= 50
	c_t1_s00_mem1 += MAS_MEM[7]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 50
	c_t2_t11_in += MAS_in[2]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 50
	c_t2_t11_mem0 += MM_MEM[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 50
	c_t2_t11_mem1 += MAS_MEM[5]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=5, delay_cost=1)
	S += c_t5_t1_t0 >= 50
	c_t5_t1_t0 += MM[0]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 50
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 50
	c_t5_t1_t1_mem0 += MAS_MEM[2]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 50
	c_t5_t1_t1_mem1 += MAS_MEM[1]

	d_t211_in = S.Task('d_t211_in', length=1, delay_cost=1)
	S += d_t211_in >= 50
	d_t211_in += MAS_in[3]

	d_t211_mem0 = S.Task('d_t211_mem0', length=1, delay_cost=1)
	S += d_t211_mem0 >= 50
	d_t211_mem0 += MAS_MEM[4]

	d_t3_t2_t2_in = S.Task('d_t3_t2_t2_in', length=1, delay_cost=1)
	S += d_t3_t2_t2_in >= 50
	d_t3_t2_t2_in += MAS_in[0]

	d_t3_t2_t2_mem0 = S.Task('d_t3_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t2_mem0 >= 50
	d_t3_t2_t2_mem0 += MAS_MEM[0]

	d_t3_t2_t2_mem1 = S.Task('d_t3_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t2_mem1 >= 50
	d_t3_t2_t2_mem1 += MAS_MEM[3]

	d_t4_t2_t2 = S.Task('d_t4_t2_t2', length=3, delay_cost=1)
	S += d_t4_t2_t2 >= 50
	d_t4_t2_t2 += MAS[1]

	d_t5_t01 = S.Task('d_t5_t01', length=3, delay_cost=1)
	S += d_t5_t01 >= 50
	d_t5_t01 += MAS[2]

	d_t5_t30 = S.Task('d_t5_t30', length=3, delay_cost=1)
	S += d_t5_t30 >= 50
	d_t5_t30 += MAS[3]

	c_t1_s00 = S.Task('c_t1_s00', length=3, delay_cost=1)
	S += c_t1_s00 >= 51
	c_t1_s00 += MAS[1]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 51
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 51
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t11 = S.Task('c_t2_t11', length=3, delay_cost=1)
	S += c_t2_t11 >= 51
	c_t2_t11 += MAS[2]

	c_t3_t4_t3_in = S.Task('c_t3_t4_t3_in', length=1, delay_cost=1)
	S += c_t3_t4_t3_in >= 51
	c_t3_t4_t3_in += MAS_in[1]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem0 >= 51
	c_t3_t4_t3_mem0 += MAS_MEM[6]

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem1 >= 51
	c_t3_t4_t3_mem1 += MAS_MEM[5]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=5, delay_cost=1)
	S += c_t5_t1_t1 >= 51
	c_t5_t1_t1 += MM[0]

	d_t1_t2_t1_in = S.Task('d_t1_t2_t1_in', length=1, delay_cost=1)
	S += d_t1_t2_t1_in >= 51
	d_t1_t2_t1_in += MM_in[0]

	d_t1_t2_t1_mem0 = S.Task('d_t1_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t1_mem0 >= 51
	d_t1_t2_t1_mem0 += MAS_MEM[2]

	d_t1_t2_t1_mem1 = S.Task('d_t1_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t1_mem1 >= 51
	d_t1_t2_t1_mem1 += MAS_MEM[1]

	d_t1_t31_in = S.Task('d_t1_t31_in', length=1, delay_cost=1)
	S += d_t1_t31_in >= 51
	d_t1_t31_in += MAS_in[2]

	d_t1_t31_mem0 = S.Task('d_t1_t31_mem0', length=1, delay_cost=1)
	S += d_t1_t31_mem0 >= 51
	d_t1_t31_mem0 += MM_MEM[0]

	d_t1_t31_mem1 = S.Task('d_t1_t31_mem1', length=1, delay_cost=1)
	S += d_t1_t31_mem1 >= 51
	d_t1_t31_mem1 += MAS_MEM[3]

	d_t211 = S.Task('d_t211', length=3, delay_cost=1)
	S += d_t211 >= 51
	d_t211 += MAS[3]

	d_t2_t41_in = S.Task('d_t2_t41_in', length=1, delay_cost=1)
	S += d_t2_t41_in >= 51
	d_t2_t41_in += MAS_in[0]

	d_t2_t41_mem0 = S.Task('d_t2_t41_mem0', length=1, delay_cost=1)
	S += d_t2_t41_mem0 >= 51
	d_t2_t41_mem0 += MAS_MEM[4]

	d_t2_t41_mem1 = S.Task('d_t2_t41_mem1', length=1, delay_cost=1)
	S += d_t2_t41_mem1 >= 51
	d_t2_t41_mem1 += MAS_MEM[7]

	d_t3_t2_t2 = S.Task('d_t3_t2_t2', length=3, delay_cost=1)
	S += d_t3_t2_t2 >= 51
	d_t3_t2_t2 += MAS[0]

	c_t0_s00_in = S.Task('c_t0_s00_in', length=1, delay_cost=1)
	S += c_t0_s00_in >= 52
	c_t0_s00_in += MAS_in[3]

	c_t0_s00_mem0 = S.Task('c_t0_s00_mem0', length=1, delay_cost=1)
	S += c_t0_s00_mem0 >= 52
	c_t0_s00_mem0 += MAS_MEM[4]

	c_t0_s00_mem1 = S.Task('c_t0_s00_mem1', length=1, delay_cost=1)
	S += c_t0_s00_mem1 >= 52
	c_t0_s00_mem1 += MAS_MEM[3]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 52
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	S += c_t2_t40_in >= 52
	c_t2_t40_in += MAS_in[0]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 52
	c_t2_t40_mem0 += MM_MEM[0]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 52
	c_t2_t40_mem1 += MM_MEM[1]

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=3, delay_cost=1)
	S += c_t3_t4_t3 >= 52
	c_t3_t4_t3 += MAS[1]

	d_s1010_in = S.Task('d_s1010_in', length=1, delay_cost=1)
	S += d_s1010_in >= 52
	d_s1010_in += MAS_in[1]

	d_s1010_mem0 = S.Task('d_s1010_mem0', length=1, delay_cost=1)
	S += d_s1010_mem0 >= 52
	d_s1010_mem0 += MAS_MEM[2]

	d_s1010_mem1 = S.Task('d_s1010_mem1', length=1, delay_cost=1)
	S += d_s1010_mem1 >= 52
	d_s1010_mem1 += MAS_MEM[5]

	d_t1_t2_t1 = S.Task('d_t1_t2_t1', length=5, delay_cost=1)
	S += d_t1_t2_t1 >= 52
	d_t1_t2_t1 += MM[0]

	d_t1_t31 = S.Task('d_t1_t31', length=3, delay_cost=1)
	S += d_t1_t31 >= 52
	d_t1_t31 += MAS[2]

	d_t2_t2_t1_in = S.Task('d_t2_t2_t1_in', length=1, delay_cost=1)
	S += d_t2_t2_t1_in >= 52
	d_t2_t2_t1_in += MM_in[0]

	d_t2_t2_t1_mem0 = S.Task('d_t2_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t1_mem0 >= 52
	d_t2_t2_t1_mem0 += MAS_MEM[0]

	d_t2_t2_t1_mem1 = S.Task('d_t2_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t1_mem1 >= 52
	d_t2_t2_t1_mem1 += MAS_MEM[7]

	d_t2_t41 = S.Task('d_t2_t41', length=3, delay_cost=1)
	S += d_t2_t41 >= 52
	d_t2_t41 += MAS[0]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 52
	d_t5000_mem0 += MAIN_MEM_r[0]

	d_t510_in = S.Task('d_t510_in', length=1, delay_cost=1)
	S += d_t510_in >= 52
	d_t510_in += MAS_in[2]

	d_t510_mem0 = S.Task('d_t510_mem0', length=1, delay_cost=1)
	S += d_t510_mem0 >= 52
	d_t510_mem0 += MAS_MEM[6]

	c_t0_s00 = S.Task('c_t0_s00', length=3, delay_cost=1)
	S += c_t0_s00 >= 53
	c_t0_s00 += MAS[3]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 53
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 53
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t2_s01_in = S.Task('c_t2_s01_in', length=1, delay_cost=1)
	S += c_t2_s01_in >= 53
	c_t2_s01_in += MAS_in[2]

	c_t2_s01_mem0 = S.Task('c_t2_s01_mem0', length=1, delay_cost=1)
	S += c_t2_s01_mem0 >= 53
	c_t2_s01_mem0 += MAS_MEM[4]

	c_t2_s01_mem1 = S.Task('c_t2_s01_mem1', length=1, delay_cost=1)
	S += c_t2_s01_mem1 >= 53
	c_t2_s01_mem1 += MAS_MEM[7]

	c_t2_t40 = S.Task('c_t2_t40', length=3, delay_cost=1)
	S += c_t2_t40 >= 53
	c_t2_t40 += MAS[0]

	d_s0010_in = S.Task('d_s0010_in', length=1, delay_cost=1)
	S += d_s0010_in >= 53
	d_s0010_in += MAS_in[3]

	d_s0010_mem0 = S.Task('d_s0010_mem0', length=1, delay_cost=1)
	S += d_s0010_mem0 >= 53
	d_s0010_mem0 += MAS_MEM[6]

	d_s0010_mem1 = S.Task('d_s0010_mem1', length=1, delay_cost=1)
	S += d_s0010_mem1 >= 53
	d_s0010_mem1 += MAS_MEM[3]

	d_s1010 = S.Task('d_s1010', length=3, delay_cost=1)
	S += d_s1010 >= 53
	d_s1010 += MAS[1]

	d_t0_t40_in = S.Task('d_t0_t40_in', length=1, delay_cost=1)
	S += d_t0_t40_in >= 53
	d_t0_t40_in += MAS_in[0]

	d_t0_t40_mem0 = S.Task('d_t0_t40_mem0', length=1, delay_cost=1)
	S += d_t0_t40_mem0 >= 53
	d_t0_t40_mem0 += MAS_MEM[0]

	d_t0_t40_mem1 = S.Task('d_t0_t40_mem1', length=1, delay_cost=1)
	S += d_t0_t40_mem1 >= 53
	d_t0_t40_mem1 += MAS_MEM[5]

	d_t2_t2_t0_in = S.Task('d_t2_t2_t0_in', length=1, delay_cost=1)
	S += d_t2_t2_t0_in >= 53
	d_t2_t2_t0_in += MM_in[0]

	d_t2_t2_t0_mem0 = S.Task('d_t2_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t0_mem0 >= 53
	d_t2_t2_t0_mem0 += MAS_MEM[2]

	d_t2_t2_t0_mem1 = S.Task('d_t2_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t0_mem1 >= 53
	d_t2_t2_t0_mem1 += MAS_MEM[1]

	d_t2_t2_t1 = S.Task('d_t2_t2_t1', length=5, delay_cost=1)
	S += d_t2_t2_t1 >= 53
	d_t2_t2_t1 += MM[0]

	d_t4_t30_in = S.Task('d_t4_t30_in', length=1, delay_cost=1)
	S += d_t4_t30_in >= 53
	d_t4_t30_in += MAS_in[1]

	d_t4_t30_mem0 = S.Task('d_t4_t30_mem0', length=1, delay_cost=1)
	S += d_t4_t30_mem0 >= 53
	d_t4_t30_mem0 += MM_MEM[0]

	d_t4_t30_mem1 = S.Task('d_t4_t30_mem1', length=1, delay_cost=1)
	S += d_t4_t30_mem1 >= 53
	d_t4_t30_mem1 += MM_MEM[1]

	d_t510 = S.Task('d_t510', length=3, delay_cost=1)
	S += d_t510 >= 53
	d_t510 += MAS[2]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 54
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	S += c_t1_t40_in >= 54
	c_t1_t40_in += MAS_in[1]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 54
	c_t1_t40_mem0 += MM_MEM[0]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 54
	c_t1_t40_mem1 += MM_MEM[1]

	c_t2_s01 = S.Task('c_t2_s01', length=3, delay_cost=1)
	S += c_t2_s01 >= 54
	c_t2_s01 += MAS[2]

	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	S += c_t2_t4_t4_in >= 54
	c_t2_t4_t4_in += MM_in[0]

	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem0 >= 54
	c_t2_t4_t4_mem0 += MAS_MEM[0]

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem1 >= 54
	c_t2_t4_t4_mem1 += MAS_MEM[7]

	d_s0010 = S.Task('d_s0010', length=3, delay_cost=1)
	S += d_s0010 >= 54
	d_s0010 += MAS[3]

	d_t0_t40 = S.Task('d_t0_t40', length=3, delay_cost=1)
	S += d_t0_t40 >= 54
	d_t0_t40 += MAS[0]

	d_t1_t40_in = S.Task('d_t1_t40_in', length=1, delay_cost=1)
	S += d_t1_t40_in >= 54
	d_t1_t40_in += MAS_in[3]

	d_t1_t40_mem0 = S.Task('d_t1_t40_mem0', length=1, delay_cost=1)
	S += d_t1_t40_mem0 >= 54
	d_t1_t40_mem0 += MAS_MEM[2]

	d_t1_t40_mem1 = S.Task('d_t1_t40_mem1', length=1, delay_cost=1)
	S += d_t1_t40_mem1 >= 54
	d_t1_t40_mem1 += MAS_MEM[5]

	d_t1_t41_in = S.Task('d_t1_t41_in', length=1, delay_cost=1)
	S += d_t1_t41_in >= 54
	d_t1_t41_in += MAS_in[2]

	d_t1_t41_mem0 = S.Task('d_t1_t41_mem0', length=1, delay_cost=1)
	S += d_t1_t41_mem0 >= 54
	d_t1_t41_mem0 += MAS_MEM[4]

	d_t1_t41_mem1 = S.Task('d_t1_t41_mem1', length=1, delay_cost=1)
	S += d_t1_t41_mem1 >= 54
	d_t1_t41_mem1 += MAS_MEM[3]

	d_t2_t2_t0 = S.Task('d_t2_t2_t0', length=5, delay_cost=1)
	S += d_t2_t2_t0 >= 54
	d_t2_t2_t0 += MM[0]

	d_t310_in = S.Task('d_t310_in', length=1, delay_cost=1)
	S += d_t310_in >= 54
	d_t310_in += MAS_in[0]

	d_t310_mem0 = S.Task('d_t310_mem0', length=1, delay_cost=1)
	S += d_t310_mem0 >= 54
	d_t310_mem0 += MAS_MEM[6]

	d_t4_t30 = S.Task('d_t4_t30', length=3, delay_cost=1)
	S += d_t4_t30 >= 54
	d_t4_t30 += MAS[1]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 54
	d_t5010_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 55
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t40 = S.Task('c_t1_t40', length=3, delay_cost=1)
	S += c_t1_t40 >= 55
	c_t1_t40 += MAS[1]

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=5, delay_cost=1)
	S += c_t2_t4_t4 >= 55
	c_t2_t4_t4 += MM[0]

	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	S += c_t2_t4_t5_in >= 55
	c_t2_t4_t5_in += MAS_in[2]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem0 >= 55
	c_t2_t4_t5_mem0 += MM_MEM[0]

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem1 >= 55
	c_t2_t4_t5_mem1 += MM_MEM[1]

	d_t111_in = S.Task('d_t111_in', length=1, delay_cost=1)
	S += d_t111_in >= 55
	d_t111_in += MAS_in[3]

	d_t111_mem0 = S.Task('d_t111_mem0', length=1, delay_cost=1)
	S += d_t111_mem0 >= 55
	d_t111_mem0 += MAS_MEM[4]

	d_t1_t2_t0_in = S.Task('d_t1_t2_t0_in', length=1, delay_cost=1)
	S += d_t1_t2_t0_in >= 55
	d_t1_t2_t0_in += MM_in[0]

	d_t1_t2_t0_mem0 = S.Task('d_t1_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t0_mem0 >= 55
	d_t1_t2_t0_mem0 += MAS_MEM[6]

	d_t1_t2_t0_mem1 = S.Task('d_t1_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t0_mem1 >= 55
	d_t1_t2_t0_mem1 += MAS_MEM[7]

	d_t1_t40 = S.Task('d_t1_t40', length=3, delay_cost=1)
	S += d_t1_t40 >= 55
	d_t1_t40 += MAS[3]

	d_t1_t41 = S.Task('d_t1_t41', length=3, delay_cost=1)
	S += d_t1_t41 >= 55
	d_t1_t41 += MAS[2]

	d_t310 = S.Task('d_t310', length=3, delay_cost=1)
	S += d_t310 >= 55
	d_t310 += MAS[0]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 55
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t5_t2_t2_in = S.Task('d_t5_t2_t2_in', length=1, delay_cost=1)
	S += d_t5_t2_t2_in >= 55
	d_t5_t2_t2_in += MAS_in[0]

	d_t5_t2_t2_mem0 = S.Task('d_t5_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t2_mem0 >= 55
	d_t5_t2_t2_mem0 += MAS_MEM[0]

	d_t5_t2_t2_mem1 = S.Task('d_t5_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t2_mem1 >= 55
	d_t5_t2_t2_mem1 += MAS_MEM[5]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 56
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 56
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	S += c_t1_t4_t5_in >= 56
	c_t1_t4_t5_in += MAS_in[1]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem0 >= 56
	c_t1_t4_t5_mem0 += MM_MEM[0]

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem1 >= 56
	c_t1_t4_t5_mem1 += MM_MEM[1]

	c_t1_t51_in = S.Task('c_t1_t51_in', length=1, delay_cost=1)
	S += c_t1_t51_in >= 56
	c_t1_t51_in += MAS_in[0]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	S += c_t1_t51_mem0 >= 56
	c_t1_t51_mem0 += MAS_MEM[6]

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	S += c_t1_t51_mem1 >= 56
	c_t1_t51_mem1 += MAS_MEM[7]

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=3, delay_cost=1)
	S += c_t2_t4_t5 >= 56
	c_t2_t4_t5 += MAS[2]

	d_t0_t2_t0_in = S.Task('d_t0_t2_t0_in', length=1, delay_cost=1)
	S += d_t0_t2_t0_in >= 56
	d_t0_t2_t0_in += MM_in[0]

	d_t0_t2_t0_mem0 = S.Task('d_t0_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t0_mem0 >= 56
	d_t0_t2_t0_mem0 += MAS_MEM[4]

	d_t0_t2_t0_mem1 = S.Task('d_t0_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t0_mem1 >= 56
	d_t0_t2_t0_mem1 += MAS_MEM[5]

	d_t0_t50_in = S.Task('d_t0_t50_in', length=1, delay_cost=1)
	S += d_t0_t50_in >= 56
	d_t0_t50_in += MAS_in[3]

	d_t0_t50_mem0 = S.Task('d_t0_t50_mem0', length=1, delay_cost=1)
	S += d_t0_t50_mem0 >= 56
	d_t0_t50_mem0 += MAS_MEM[0]

	d_t0_t50_mem1 = S.Task('d_t0_t50_mem1', length=1, delay_cost=1)
	S += d_t0_t50_mem1 >= 56
	d_t0_t50_mem1 += MAS_MEM[1]

	d_t111 = S.Task('d_t111', length=3, delay_cost=1)
	S += d_t111 >= 56
	d_t111 += MAS[3]

	d_t1_t2_t0 = S.Task('d_t1_t2_t0', length=5, delay_cost=1)
	S += d_t1_t2_t0 >= 56
	d_t1_t2_t0 += MM[0]

	d_t410_in = S.Task('d_t410_in', length=1, delay_cost=1)
	S += d_t410_in >= 56
	d_t410_in += MAS_in[2]

	d_t410_mem0 = S.Task('d_t410_mem0', length=1, delay_cost=1)
	S += d_t410_mem0 >= 56
	d_t410_mem0 += MAS_MEM[2]

	d_t5_t2_t2 = S.Task('d_t5_t2_t2', length=3, delay_cost=1)
	S += d_t5_t2_t2 >= 56
	d_t5_t2_t2 += MAS[0]

	c_t0_s01_in = S.Task('c_t0_s01_in', length=1, delay_cost=1)
	S += c_t0_s01_in >= 57
	c_t0_s01_in += MAS_in[0]

	c_t0_s01_mem0 = S.Task('c_t0_s01_mem0', length=1, delay_cost=1)
	S += c_t0_s01_mem0 >= 57
	c_t0_s01_mem0 += MAS_MEM[2]

	c_t0_s01_mem1 = S.Task('c_t0_s01_mem1', length=1, delay_cost=1)
	S += c_t0_s01_mem1 >= 57
	c_t0_s01_mem1 += MAS_MEM[5]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 57
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_s01_in = S.Task('c_t1_s01_in', length=1, delay_cost=1)
	S += c_t1_s01_in >= 57
	c_t1_s01_in += MAS_in[1]

	c_t1_s01_mem0 = S.Task('c_t1_s01_mem0', length=1, delay_cost=1)
	S += c_t1_s01_mem0 >= 57
	c_t1_s01_mem0 += MAS_MEM[6]

	c_t1_s01_mem1 = S.Task('c_t1_s01_mem1', length=1, delay_cost=1)
	S += c_t1_s01_mem1 >= 57
	c_t1_s01_mem1 += MAS_MEM[7]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 57
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=3, delay_cost=1)
	S += c_t1_t4_t5 >= 57
	c_t1_t4_t5 += MAS[1]

	c_t1_t51 = S.Task('c_t1_t51', length=3, delay_cost=1)
	S += c_t1_t51 >= 57
	c_t1_t51 += MAS[0]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 57
	c_t2_t01_in += MAS_in[3]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 57
	c_t2_t01_mem0 += MM_MEM[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 57
	c_t2_t01_mem1 += MAS_MEM[1]

	d_t011_in = S.Task('d_t011_in', length=1, delay_cost=1)
	S += d_t011_in >= 57
	d_t011_in += MAS_in[2]

	d_t011_mem0 = S.Task('d_t011_mem0', length=1, delay_cost=1)
	S += d_t011_mem0 >= 57
	d_t011_mem0 += MAS_MEM[4]

	d_t0_t2_t0 = S.Task('d_t0_t2_t0', length=5, delay_cost=1)
	S += d_t0_t2_t0 >= 57
	d_t0_t2_t0 += MM[0]

	d_t0_t50 = S.Task('d_t0_t50', length=3, delay_cost=1)
	S += d_t0_t50 >= 57
	d_t0_t50 += MAS[3]

	d_t3_t3_t4_in = S.Task('d_t3_t3_t4_in', length=1, delay_cost=1)
	S += d_t3_t3_t4_in >= 57
	d_t3_t3_t4_in += MM_in[0]

	d_t3_t3_t4_mem0 = S.Task('d_t3_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t4_mem0 >= 57
	d_t3_t3_t4_mem0 += MAS_MEM[0]

	d_t3_t3_t4_mem1 = S.Task('d_t3_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t4_mem1 >= 57
	d_t3_t3_t4_mem1 += MAS_MEM[3]

	d_t410 = S.Task('d_t410', length=3, delay_cost=1)
	S += d_t410 >= 57
	d_t410 += MAS[2]

	c_t0_s01 = S.Task('c_t0_s01', length=3, delay_cost=1)
	S += c_t0_s01 >= 58
	c_t0_s01 += MAS[0]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 58
	c_t0_t01_in += MAS_in[0]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 58
	c_t0_t01_mem0 += MM_MEM[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 58
	c_t0_t01_mem1 += MAS_MEM[7]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 58
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_s01 = S.Task('c_t1_s01', length=3, delay_cost=1)
	S += c_t1_s01 >= 58
	c_t1_s01 += MAS[1]

	c_t2_t01 = S.Task('c_t2_t01', length=3, delay_cost=1)
	S += c_t2_t01 >= 58
	c_t2_t01 += MAS[3]

	d_s210_in = S.Task('d_s210_in', length=1, delay_cost=1)
	S += d_s210_in >= 58
	d_s210_in += MAS_in[3]

	d_s210_mem0 = S.Task('d_s210_mem0', length=1, delay_cost=1)
	S += d_s210_mem0 >= 58
	d_s210_mem0 += MAS_MEM[4]

	d_s210_mem1 = S.Task('d_s210_mem1', length=1, delay_cost=1)
	S += d_s210_mem1 >= 58
	d_s210_mem1 += MAS_MEM[1]

	d_t011 = S.Task('d_t011', length=3, delay_cost=1)
	S += d_t011 >= 58
	d_t011 += MAS[2]

	d_t0_t2_t1_in = S.Task('d_t0_t2_t1_in', length=1, delay_cost=1)
	S += d_t0_t2_t1_in >= 58
	d_t0_t2_t1_in += MM_in[0]

	d_t0_t2_t1_mem0 = S.Task('d_t0_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t1_mem0 >= 58
	d_t0_t2_t1_mem0 += MAS_MEM[6]

	d_t0_t2_t1_mem1 = S.Task('d_t0_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t1_mem1 >= 58
	d_t0_t2_t1_mem1 += MAS_MEM[5]

	d_t3_t3_t4 = S.Task('d_t3_t3_t4', length=5, delay_cost=1)
	S += d_t3_t3_t4 >= 58
	d_t3_t3_t4 += MM[0]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 58
	d_t4010_mem0 += MAIN_MEM_r[0]

	c_t0_t01 = S.Task('c_t0_t01', length=3, delay_cost=1)
	S += c_t0_t01 >= 59
	c_t0_t01 += MAS[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 59
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	S += c_t110_in >= 59
	c_t110_in += MAS_in[1]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 59
	c_t110_mem0 += MAS_MEM[2]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 59
	c_t110_mem1 += MAS_MEM[5]

	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	S += c_t1_t4_t4_in >= 59
	c_t1_t4_t4_in += MM_in[0]

	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem0 >= 59
	c_t1_t4_t4_mem0 += MAS_MEM[6]

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem1 >= 59
	c_t1_t4_t4_mem1 += MAS_MEM[1]

	c_t3_t0_t5_in = S.Task('c_t3_t0_t5_in', length=1, delay_cost=1)
	S += c_t3_t0_t5_in >= 59
	c_t3_t0_t5_in += MAS_in[3]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem0 >= 59
	c_t3_t0_t5_mem0 += MM_MEM[0]

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem1 >= 59
	c_t3_t0_t5_mem1 += MM_MEM[1]

	d_s210 = S.Task('d_s210', length=3, delay_cost=1)
	S += d_s210 >= 59
	d_s210 += MAS[3]

	d_t0_t2_t1 = S.Task('d_t0_t2_t1', length=5, delay_cost=1)
	S += d_t0_t2_t1 >= 59
	d_t0_t2_t1 += MM[0]

	d_t0_t51_in = S.Task('d_t0_t51_in', length=1, delay_cost=1)
	S += d_t0_t51_in >= 59
	d_t0_t51_in += MAS_in[0]

	d_t0_t51_mem0 = S.Task('d_t0_t51_mem0', length=1, delay_cost=1)
	S += d_t0_t51_mem0 >= 59
	d_t0_t51_mem0 += MAS_MEM[4]

	d_t0_t51_mem1 = S.Task('d_t0_t51_mem1', length=1, delay_cost=1)
	S += d_t0_t51_mem1 >= 59
	d_t0_t51_mem1 += MAS_MEM[7]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 59
	d_t4010_mem1 += MAIN_MEM_r[1]

	c_t110 = S.Task('c_t110', length=3, delay_cost=1)
	S += c_t110 >= 60
	c_t110 += MAS[1]

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=5, delay_cost=1)
	S += c_t1_t4_t4 >= 60
	c_t1_t4_t4 += MM[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 60
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 60
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=3, delay_cost=1)
	S += c_t3_t0_t5 >= 60
	c_t3_t0_t5 += MAS[3]

	c_t3_t1_t5_in = S.Task('c_t3_t1_t5_in', length=1, delay_cost=1)
	S += c_t3_t1_t5_in >= 60
	c_t3_t1_t5_in += MAS_in[0]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem0 >= 60
	c_t3_t1_t5_mem0 += MM_MEM[0]

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem1 >= 60
	c_t3_t1_t5_mem1 += MM_MEM[1]

	d_s1110_in = S.Task('d_s1110_in', length=1, delay_cost=1)
	S += d_s1110_in >= 60
	d_s1110_in += MAS_in[3]

	d_s1110_mem0 = S.Task('d_s1110_mem0', length=1, delay_cost=1)
	S += d_s1110_mem0 >= 60
	d_s1110_mem0 += MAS_MEM[4]

	d_s1110_mem1 = S.Task('d_s1110_mem1', length=1, delay_cost=1)
	S += d_s1110_mem1 >= 60
	d_s1110_mem1 += MAS_MEM[3]

	d_t0_t51 = S.Task('d_t0_t51', length=3, delay_cost=1)
	S += d_t0_t51 >= 60
	d_t0_t51 += MAS[0]

	d_t1_t50_in = S.Task('d_t1_t50_in', length=1, delay_cost=1)
	S += d_t1_t50_in >= 60
	d_t1_t50_in += MAS_in[1]

	d_t1_t50_mem0 = S.Task('d_t1_t50_mem0', length=1, delay_cost=1)
	S += d_t1_t50_mem0 >= 60
	d_t1_t50_mem0 += MAS_MEM[2]

	d_t1_t50_mem1 = S.Task('d_t1_t50_mem1', length=1, delay_cost=1)
	S += d_t1_t50_mem1 >= 60
	d_t1_t50_mem1 += MAS_MEM[7]

	d_t4_t3_t4_in = S.Task('d_t4_t3_t4_in', length=1, delay_cost=1)
	S += d_t4_t3_t4_in >= 60
	d_t4_t3_t4_in += MM_in[0]

	d_t4_t3_t4_mem0 = S.Task('d_t4_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t4_mem0 >= 60
	d_t4_t3_t4_mem0 += MAS_MEM[6]

	d_t4_t3_t4_mem1 = S.Task('d_t4_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t4_mem1 >= 60
	d_t4_t3_t4_mem1 += MAS_MEM[5]

	c_t2_t51_in = S.Task('c_t2_t51_in', length=1, delay_cost=1)
	S += c_t2_t51_in >= 61
	c_t2_t51_in += MAS_in[3]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	S += c_t2_t51_mem0 >= 61
	c_t2_t51_mem0 += MAS_MEM[6]

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	S += c_t2_t51_mem1 >= 61
	c_t2_t51_mem1 += MAS_MEM[5]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 61
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=3, delay_cost=1)
	S += c_t3_t1_t5 >= 61
	c_t3_t1_t5 += MAS[0]

	c_t4_t1_t5_in = S.Task('c_t4_t1_t5_in', length=1, delay_cost=1)
	S += c_t4_t1_t5_in >= 61
	c_t4_t1_t5_in += MAS_in[2]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem0 >= 61
	c_t4_t1_t5_mem0 += MM_MEM[0]

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem1 >= 61
	c_t4_t1_t5_mem1 += MM_MEM[1]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 61
	c_t5000_mem1 += MAIN_MEM_r[1]

	d_s1110 = S.Task('d_s1110', length=3, delay_cost=1)
	S += d_s1110 >= 61
	d_s1110 += MAS[3]

	d_t1_t50 = S.Task('d_t1_t50', length=3, delay_cost=1)
	S += d_t1_t50 >= 61
	d_t1_t50 += MAS[1]

	d_t2_t51_in = S.Task('d_t2_t51_in', length=1, delay_cost=1)
	S += d_t2_t51_in >= 61
	d_t2_t51_in += MAS_in[0]

	d_t2_t51_mem0 = S.Task('d_t2_t51_mem0', length=1, delay_cost=1)
	S += d_t2_t51_mem0 >= 61
	d_t2_t51_mem0 += MAS_MEM[4]

	d_t2_t51_mem1 = S.Task('d_t2_t51_mem1', length=1, delay_cost=1)
	S += d_t2_t51_mem1 >= 61
	d_t2_t51_mem1 += MAS_MEM[1]

	d_t4_t3_t4 = S.Task('d_t4_t3_t4', length=5, delay_cost=1)
	S += d_t4_t3_t4 >= 61
	d_t4_t3_t4 += MM[0]

	d_t5_t3_t4_in = S.Task('d_t5_t3_t4_in', length=1, delay_cost=1)
	S += d_t5_t3_t4_in >= 61
	d_t5_t3_t4_in += MM_in[0]

	d_t5_t3_t4_mem0 = S.Task('d_t5_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t4_mem0 >= 61
	d_t5_t3_t4_mem0 += MAS_MEM[0]

	d_t5_t3_t4_mem1 = S.Task('d_t5_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t4_mem1 >= 61
	d_t5_t3_t4_mem1 += MAS_MEM[7]

	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	S += c_t0_t4_t4_in >= 62
	c_t0_t4_t4_in += MM_in[0]

	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem0 >= 62
	c_t0_t4_t4_mem0 += MAS_MEM[6]

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem1 >= 62
	c_t0_t4_t4_mem1 += MAS_MEM[3]

	c_t210_in = S.Task('c_t210_in', length=1, delay_cost=1)
	S += c_t210_in >= 62
	c_t210_in += MAS_in[0]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 62
	c_t210_mem0 += MAS_MEM[0]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 62
	c_t210_mem1 += MAS_MEM[5]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 62
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t51 = S.Task('c_t2_t51', length=3, delay_cost=1)
	S += c_t2_t51 >= 62
	c_t2_t51 += MAS[3]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 62
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4_t0_t5_in = S.Task('c_t4_t0_t5_in', length=1, delay_cost=1)
	S += c_t4_t0_t5_in >= 62
	c_t4_t0_t5_in += MAS_in[1]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem0 >= 62
	c_t4_t0_t5_mem0 += MM_MEM[0]

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem1 >= 62
	c_t4_t0_t5_mem1 += MM_MEM[1]

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=3, delay_cost=1)
	S += c_t4_t1_t5 >= 62
	c_t4_t1_t5 += MAS[2]

	d_s0011_in = S.Task('d_s0011_in', length=1, delay_cost=1)
	S += d_s0011_in >= 62
	d_s0011_in += MAS_in[2]

	d_s0011_mem0 = S.Task('d_s0011_mem0', length=1, delay_cost=1)
	S += d_s0011_mem0 >= 62
	d_s0011_mem0 += MAS_MEM[4]

	d_s0011_mem1 = S.Task('d_s0011_mem1', length=1, delay_cost=1)
	S += d_s0011_mem1 >= 62
	d_s0011_mem1 += MAS_MEM[7]

	d_t2_t51 = S.Task('d_t2_t51', length=3, delay_cost=1)
	S += d_t2_t51 >= 62
	d_t2_t51 += MAS[0]

	d_t5_t3_t4 = S.Task('d_t5_t3_t4', length=5, delay_cost=1)
	S += d_t5_t3_t4 >= 62
	d_t5_t3_t4 += MM[0]

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=5, delay_cost=1)
	S += c_t0_t4_t4 >= 63
	c_t0_t4_t4 += MM[0]

	c_t0_t51_in = S.Task('c_t0_t51_in', length=1, delay_cost=1)
	S += c_t0_t51_in >= 63
	c_t0_t51_in += MAS_in[0]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	S += c_t0_t51_mem0 >= 63
	c_t0_t51_mem0 += MAS_MEM[0]

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	S += c_t0_t51_mem1 >= 63
	c_t0_t51_mem1 += MAS_MEM[3]

	c_t210 = S.Task('c_t210', length=3, delay_cost=1)
	S += c_t210 >= 63
	c_t210 += MAS[0]

	c_t2_s00_in = S.Task('c_t2_s00_in', length=1, delay_cost=1)
	S += c_t2_s00_in >= 63
	c_t2_s00_in += MAS_in[3]

	c_t2_s00_mem0 = S.Task('c_t2_s00_mem0', length=1, delay_cost=1)
	S += c_t2_s00_mem0 >= 63
	c_t2_s00_mem0 += MAS_MEM[6]

	c_t2_s00_mem1 = S.Task('c_t2_s00_mem1', length=1, delay_cost=1)
	S += c_t2_s00_mem1 >= 63
	c_t2_s00_mem1 += MAS_MEM[5]

	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	S += c_t3_t00_in >= 63
	c_t3_t00_in += MAS_in[2]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 63
	c_t3_t00_mem0 += MM_MEM[0]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 63
	c_t3_t00_mem1 += MM_MEM[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 63
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 63
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	S += c_t4_t0_t4_in >= 63
	c_t4_t0_t4_in += MM_in[0]

	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem0 >= 63
	c_t4_t0_t4_mem0 += MAS_MEM[4]

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem1 >= 63
	c_t4_t0_t4_mem1 += MAS_MEM[7]

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=3, delay_cost=1)
	S += c_t4_t0_t5 >= 63
	c_t4_t0_t5 += MAS[1]

	d_s0011 = S.Task('d_s0011', length=3, delay_cost=1)
	S += d_s0011 >= 63
	d_s0011 += MAS[2]

	c_t000_in = S.Task('c_t000_in', length=1, delay_cost=1)
	S += c_t000_in >= 64
	c_t000_in += MAS_in[0]

	c_t000_mem0 = S.Task('c_t000_mem0', length=1, delay_cost=1)
	S += c_t000_mem0 >= 64
	c_t000_mem0 += MAS_MEM[2]

	c_t000_mem1 = S.Task('c_t000_mem1', length=1, delay_cost=1)
	S += c_t000_mem1 >= 64
	c_t000_mem1 += MAS_MEM[7]

	c_t0_t51 = S.Task('c_t0_t51', length=3, delay_cost=1)
	S += c_t0_t51 >= 64
	c_t0_t51 += MAS[0]

	c_t2_s00 = S.Task('c_t2_s00', length=3, delay_cost=1)
	S += c_t2_s00 >= 64
	c_t2_s00 += MAS[3]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 64
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t3_t00 = S.Task('c_t3_t00', length=3, delay_cost=1)
	S += c_t3_t00 >= 64
	c_t3_t00 += MAS[2]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 64
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=5, delay_cost=1)
	S += c_t4_t0_t4 >= 64
	c_t4_t0_t4 += MM[0]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 64
	c_t5_t10_in += MAS_in[2]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 64
	c_t5_t10_mem0 += MM_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 64
	c_t5_t10_mem1 += MM_MEM[1]

	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	S += c_t5_t4_t0_in >= 64
	c_t5_t4_t0_in += MM_in[0]

	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem0 >= 64
	c_t5_t4_t0_mem0 += MAS_MEM[4]

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem1 >= 64
	c_t5_t4_t0_mem1 += MAS_MEM[1]

	d_t2_t40_in = S.Task('d_t2_t40_in', length=1, delay_cost=1)
	S += d_t2_t40_in >= 64
	d_t2_t40_in += MAS_in[3]

	d_t2_t40_mem0 = S.Task('d_t2_t40_mem0', length=1, delay_cost=1)
	S += d_t2_t40_mem0 >= 64
	d_t2_t40_mem0 += MAS_MEM[6]

	d_t2_t40_mem1 = S.Task('d_t2_t40_mem1', length=1, delay_cost=1)
	S += d_t2_t40_mem1 >= 64
	d_t2_t40_mem1 += MAS_MEM[5]

	c_t000 = S.Task('c_t000', length=3, delay_cost=1)
	S += c_t000 >= 65
	c_t000 += MAS[0]

	c_t001_in = S.Task('c_t001_in', length=1, delay_cost=1)
	S += c_t001_in >= 65
	c_t001_in += MAS_in[3]

	c_t001_mem0 = S.Task('c_t001_mem0', length=1, delay_cost=1)
	S += c_t001_mem0 >= 65
	c_t001_mem0 += MAS_MEM[0]

	c_t001_mem1 = S.Task('c_t001_mem1', length=1, delay_cost=1)
	S += c_t001_mem1 >= 65
	c_t001_mem1 += MAS_MEM[1]

	c_t201_in = S.Task('c_t201_in', length=1, delay_cost=1)
	S += c_t201_in >= 65
	c_t201_in += MAS_in[1]

	c_t201_mem0 = S.Task('c_t201_mem0', length=1, delay_cost=1)
	S += c_t201_mem0 >= 65
	c_t201_mem0 += MAS_MEM[6]

	c_t201_mem1 = S.Task('c_t201_mem1', length=1, delay_cost=1)
	S += c_t201_mem1 >= 65
	c_t201_mem1 += MAS_MEM[5]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 65
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 65
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 65
	c_t3_t10_in += MAS_in[2]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 65
	c_t3_t10_mem0 += MM_MEM[0]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 65
	c_t3_t10_mem1 += MM_MEM[1]

	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	S += c_t3_t4_t0_in >= 65
	c_t3_t4_t0_in += MM_in[0]

	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem0 >= 65
	c_t3_t4_t0_mem0 += MAS_MEM[2]

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem1 >= 65
	c_t3_t4_t0_mem1 += MAS_MEM[7]

	c_t5_t10 = S.Task('c_t5_t10', length=3, delay_cost=1)
	S += c_t5_t10 >= 65
	c_t5_t10 += MAS[2]

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=5, delay_cost=1)
	S += c_t5_t4_t0 >= 65
	c_t5_t4_t0 += MM[0]

	d_t2_t40 = S.Task('d_t2_t40', length=3, delay_cost=1)
	S += d_t2_t40 >= 65
	d_t2_t40 += MAS[3]

	c_t001 = S.Task('c_t001', length=3, delay_cost=1)
	S += c_t001 >= 66
	c_t001 += MAS[3]

	c_t200_in = S.Task('c_t200_in', length=1, delay_cost=1)
	S += c_t200_in >= 66
	c_t200_in += MAS_in[1]

	c_t200_mem0 = S.Task('c_t200_mem0', length=1, delay_cost=1)
	S += c_t200_mem0 >= 66
	c_t200_mem0 += MAS_MEM[2]

	c_t200_mem1 = S.Task('c_t200_mem1', length=1, delay_cost=1)
	S += c_t200_mem1 >= 66
	c_t200_mem1 += MAS_MEM[7]

	c_t201 = S.Task('c_t201', length=3, delay_cost=1)
	S += c_t201 >= 66
	c_t201 += MAS[1]

	c_t3_t10 = S.Task('c_t3_t10', length=3, delay_cost=1)
	S += c_t3_t10 >= 66
	c_t3_t10 += MAS[2]

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=5, delay_cost=1)
	S += c_t3_t4_t0 >= 66
	c_t3_t4_t0 += MM[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 66
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 66
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t5_t0_t5_in = S.Task('c_t5_t0_t5_in', length=1, delay_cost=1)
	S += c_t5_t0_t5_in >= 66
	c_t5_t0_t5_in += MAS_in[3]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem0 >= 66
	c_t5_t0_t5_mem0 += MM_MEM[0]

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem1 >= 66
	c_t5_t0_t5_mem1 += MM_MEM[1]

	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	S += c_t5_t4_t1_in >= 66
	c_t5_t4_t1_in += MM_in[0]

	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem0 >= 66
	c_t5_t4_t1_mem0 += MAS_MEM[6]

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem1 >= 66
	c_t5_t4_t1_mem1 += MAS_MEM[1]

	d_t1_t51_in = S.Task('d_t1_t51_in', length=1, delay_cost=1)
	S += d_t1_t51_in >= 66
	d_t1_t51_in += MAS_in[0]

	d_t1_t51_mem0 = S.Task('d_t1_t51_mem0', length=1, delay_cost=1)
	S += d_t1_t51_mem0 >= 66
	d_t1_t51_mem0 += MAS_MEM[4]

	d_t1_t51_mem1 = S.Task('d_t1_t51_mem1', length=1, delay_cost=1)
	S += d_t1_t51_mem1 >= 66
	d_t1_t51_mem1 += MAS_MEM[5]

	c_t100_in = S.Task('c_t100_in', length=1, delay_cost=1)
	S += c_t100_in >= 67
	c_t100_in += MAS_in[0]

	c_t100_mem0 = S.Task('c_t100_mem0', length=1, delay_cost=1)
	S += c_t100_mem0 >= 67
	c_t100_mem0 += MAS_MEM[6]

	c_t100_mem1 = S.Task('c_t100_mem1', length=1, delay_cost=1)
	S += c_t100_mem1 >= 67
	c_t100_mem1 += MAS_MEM[3]

	c_t200 = S.Task('c_t200', length=3, delay_cost=1)
	S += c_t200 >= 67
	c_t200 += MAS[1]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 67
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 67
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	S += c_t3_t4_t1_in >= 67
	c_t3_t4_t1_in += MM_in[0]

	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem0 >= 67
	c_t3_t4_t1_mem0 += MAS_MEM[2]

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem1 >= 67
	c_t3_t4_t1_mem1 += MAS_MEM[5]

	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	S += c_t4_t00_in >= 67
	c_t4_t00_in += MAS_in[2]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 67
	c_t4_t00_mem0 += MM_MEM[0]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 67
	c_t4_t00_mem1 += MM_MEM[1]

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=3, delay_cost=1)
	S += c_t5_t0_t5 >= 67
	c_t5_t0_t5 += MAS[3]

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=5, delay_cost=1)
	S += c_t5_t4_t1 >= 67
	c_t5_t4_t1 += MM[0]

	d_t1_t51 = S.Task('d_t1_t51', length=3, delay_cost=1)
	S += d_t1_t51 >= 67
	d_t1_t51 += MAS[0]

	d_t6_y1_0_in = S.Task('d_t6_y1_0_in', length=1, delay_cost=1)
	S += d_t6_y1_0_in >= 67
	d_t6_y1_0_in += MAS_in[1]

	d_t6_y1_0_mem0 = S.Task('d_t6_y1_0_mem0', length=1, delay_cost=1)
	S += d_t6_y1_0_mem0 >= 67
	d_t6_y1_0_mem0 += MAS_MEM[4]

	d_t6_y1_0_mem1 = S.Task('d_t6_y1_0_mem1', length=1, delay_cost=1)
	S += d_t6_y1_0_mem1 >= 67
	d_t6_y1_0_mem1 += MAS_MEM[7]

	c_t100 = S.Task('c_t100', length=3, delay_cost=1)
	S += c_t100 >= 68
	c_t100 += MAS[0]

	c_t101_in = S.Task('c_t101_in', length=1, delay_cost=1)
	S += c_t101_in >= 68
	c_t101_in += MAS_in[0]

	c_t101_mem0 = S.Task('c_t101_mem0', length=1, delay_cost=1)
	S += c_t101_mem0 >= 68
	c_t101_mem0 += MAS_MEM[6]

	c_t101_mem1 = S.Task('c_t101_mem1', length=1, delay_cost=1)
	S += c_t101_mem1 >= 68
	c_t101_mem1 += MAS_MEM[3]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 68
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 68
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=5, delay_cost=1)
	S += c_t3_t4_t1 >= 68
	c_t3_t4_t1 += MM[0]

	c_t3_t50_in = S.Task('c_t3_t50_in', length=1, delay_cost=1)
	S += c_t3_t50_in >= 68
	c_t3_t50_in += MAS_in[1]

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	S += c_t3_t50_mem0 >= 68
	c_t3_t50_mem0 += MAS_MEM[4]

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	S += c_t3_t50_mem1 >= 68
	c_t3_t50_mem1 += MAS_MEM[5]

	c_t4_t00 = S.Task('c_t4_t00', length=3, delay_cost=1)
	S += c_t4_t00 >= 68
	c_t4_t00 += MAS[2]

	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	S += c_t4_t4_t1_in >= 68
	c_t4_t4_t1_in += MM_in[0]

	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem0 >= 68
	c_t4_t4_t1_mem0 += MAS_MEM[2]

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem1 >= 68
	c_t4_t4_t1_mem1 += MAS_MEM[1]

	c_t5_t1_t5_in = S.Task('c_t5_t1_t5_in', length=1, delay_cost=1)
	S += c_t5_t1_t5_in >= 68
	c_t5_t1_t5_in += MAS_in[3]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem0 >= 68
	c_t5_t1_t5_mem0 += MM_MEM[0]

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem1 >= 68
	c_t5_t1_t5_mem1 += MM_MEM[1]

	d_s010_in = S.Task('d_s010_in', length=1, delay_cost=1)
	S += d_s010_in >= 68
	d_s010_in += MAS_in[2]

	d_s010_mem0 = S.Task('d_s010_mem0', length=1, delay_cost=1)
	S += d_s010_mem0 >= 68
	d_s010_mem0 += MAS_MEM[0]

	d_s010_mem1 = S.Task('d_s010_mem1', length=1, delay_cost=1)
	S += d_s010_mem1 >= 68
	d_s010_mem1 += MAS_MEM[7]

	d_t6_y1_0 = S.Task('d_t6_y1_0', length=3, delay_cost=1)
	S += d_t6_y1_0 >= 68
	d_t6_y1_0 += MAS[1]

	c_t101 = S.Task('c_t101', length=3, delay_cost=1)
	S += c_t101 >= 69
	c_t101 += MAS[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 69
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t3_t50 = S.Task('c_t3_t50', length=3, delay_cost=1)
	S += c_t3_t50 >= 69
	c_t3_t50 += MAS[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 69
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=5, delay_cost=1)
	S += c_t4_t4_t1 >= 69
	c_t4_t4_t1 += MM[0]

	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	S += c_t5_t00_in >= 69
	c_t5_t00_in += MAS_in[3]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 69
	c_t5_t00_mem0 += MM_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 69
	c_t5_t00_mem1 += MM_MEM[1]

	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	S += c_t5_t0_t4_in >= 69
	c_t5_t0_t4_in += MM_in[0]

	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem0 >= 69
	c_t5_t0_t4_mem0 += MAS_MEM[0]

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem1 >= 69
	c_t5_t0_t4_mem1 += MAS_MEM[7]

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=3, delay_cost=1)
	S += c_t5_t1_t5 >= 69
	c_t5_t1_t5 += MAS[3]

	d_s010 = S.Task('d_s010', length=3, delay_cost=1)
	S += d_s010 >= 69
	d_s010 += MAS[2]

	d_s2011_in = S.Task('d_s2011_in', length=1, delay_cost=1)
	S += d_s2011_in >= 69
	d_s2011_in += MAS_in[1]

	d_s2011_mem0 = S.Task('d_s2011_mem0', length=1, delay_cost=1)
	S += d_s2011_mem0 >= 69
	d_s2011_mem0 += MAS_MEM[6]

	d_s2011_mem1 = S.Task('d_s2011_mem1', length=1, delay_cost=1)
	S += d_s2011_mem1 >= 69
	d_s2011_mem1 += MAS_MEM[5]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 70
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 70
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	S += c_t3_t0_t4_in >= 70
	c_t3_t0_t4_in += MM_in[0]

	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem0 >= 70
	c_t3_t0_t4_mem0 += MAS_MEM[4]

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem1 >= 70
	c_t3_t0_t4_mem1 += MAS_MEM[3]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 70
	c_t4_t10_in += MAS_in[2]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 70
	c_t4_t10_mem0 += MM_MEM[0]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 70
	c_t4_t10_mem1 += MM_MEM[1]

	c_t5_t00 = S.Task('c_t5_t00', length=3, delay_cost=1)
	S += c_t5_t00 >= 70
	c_t5_t00 += MAS[3]

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=5, delay_cost=1)
	S += c_t5_t0_t4 >= 70
	c_t5_t0_t4 += MM[0]

	d_s2011 = S.Task('d_s2011', length=3, delay_cost=1)
	S += d_s2011 >= 70
	d_s2011 += MAS[1]

	d_t6_y1_1_in = S.Task('d_t6_y1_1_in', length=1, delay_cost=1)
	S += d_t6_y1_1_in >= 70
	d_t6_y1_1_in += MAS_in[3]

	d_t6_y1_1_mem0 = S.Task('d_t6_y1_1_mem0', length=1, delay_cost=1)
	S += d_t6_y1_1_mem0 >= 70
	d_t6_y1_1_mem0 += MAS_MEM[6]

	d_t6_y1_1_mem1 = S.Task('d_t6_y1_1_mem1', length=1, delay_cost=1)
	S += d_t6_y1_1_mem1 >= 70
	d_t6_y1_1_mem1 += MAS_MEM[5]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 71
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 71
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=5, delay_cost=1)
	S += c_t3_t0_t4 >= 71
	c_t3_t0_t4 += MM[0]

	c_t4_t10 = S.Task('c_t4_t10', length=3, delay_cost=1)
	S += c_t4_t10 >= 71
	c_t4_t10 += MAS[2]

	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	S += c_t5_t1_t4_in >= 71
	c_t5_t1_t4_in += MM_in[0]

	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem0 >= 71
	c_t5_t1_t4_mem0 += MAS_MEM[2]

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem1 >= 71
	c_t5_t1_t4_mem1 += MAS_MEM[5]

	d_t2_t20_in = S.Task('d_t2_t20_in', length=1, delay_cost=1)
	S += d_t2_t20_in >= 71
	d_t2_t20_in += MAS_in[0]

	d_t2_t20_mem0 = S.Task('d_t2_t20_mem0', length=1, delay_cost=1)
	S += d_t2_t20_mem0 >= 71
	d_t2_t20_mem0 += MM_MEM[0]

	d_t2_t20_mem1 = S.Task('d_t2_t20_mem1', length=1, delay_cost=1)
	S += d_t2_t20_mem1 >= 71
	d_t2_t20_mem1 += MM_MEM[1]

	d_t2_t50_in = S.Task('d_t2_t50_in', length=1, delay_cost=1)
	S += d_t2_t50_in >= 71
	d_t2_t50_in += MAS_in[3]

	d_t2_t50_mem0 = S.Task('d_t2_t50_mem0', length=1, delay_cost=1)
	S += d_t2_t50_mem0 >= 71
	d_t2_t50_mem0 += MAS_MEM[6]

	d_t2_t50_mem1 = S.Task('d_t2_t50_mem1', length=1, delay_cost=1)
	S += d_t2_t50_mem1 >= 71
	d_t2_t50_mem1 += MAS_MEM[7]

	d_t6_y1_1 = S.Task('d_t6_y1_1', length=3, delay_cost=1)
	S += d_t6_y1_1 >= 71
	d_t6_y1_1 += MAS[3]

	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	S += c_t3_t1_t4_in >= 72
	c_t3_t1_t4_in += MM_in[0]

	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem0 >= 72
	c_t3_t1_t4_mem0 += MAS_MEM[4]

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem1 >= 72
	c_t3_t1_t4_mem1 += MAS_MEM[1]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 72
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 72
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=5, delay_cost=1)
	S += c_t5_t1_t4 >= 72
	c_t5_t1_t4 += MM[0]

	c_t5_t50_in = S.Task('c_t5_t50_in', length=1, delay_cost=1)
	S += c_t5_t50_in >= 72
	c_t5_t50_in += MAS_in[3]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	S += c_t5_t50_mem0 >= 72
	c_t5_t50_mem0 += MAS_MEM[6]

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	S += c_t5_t50_mem1 >= 72
	c_t5_t50_mem1 += MAS_MEM[5]

	d_t0_t20_in = S.Task('d_t0_t20_in', length=1, delay_cost=1)
	S += d_t0_t20_in >= 72
	d_t0_t20_in += MAS_in[2]

	d_t0_t20_mem0 = S.Task('d_t0_t20_mem0', length=1, delay_cost=1)
	S += d_t0_t20_mem0 >= 72
	d_t0_t20_mem0 += MM_MEM[0]

	d_t0_t20_mem1 = S.Task('d_t0_t20_mem1', length=1, delay_cost=1)
	S += d_t0_t20_mem1 >= 72
	d_t0_t20_mem1 += MM_MEM[1]

	d_t2_t20 = S.Task('d_t2_t20', length=3, delay_cost=1)
	S += d_t2_t20 >= 72
	d_t2_t20 += MAS[0]

	d_t2_t50 = S.Task('d_t2_t50', length=3, delay_cost=1)
	S += d_t2_t50 >= 72
	d_t2_t50 += MAS[3]

	c_t0_t41_in = S.Task('c_t0_t41_in', length=1, delay_cost=1)
	S += c_t0_t41_in >= 73
	c_t0_t41_in += MAS_in[0]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 73
	c_t0_t41_mem0 += MM_MEM[0]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 73
	c_t0_t41_mem1 += MAS_MEM[1]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 73
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=5, delay_cost=1)
	S += c_t3_t1_t4 >= 73
	c_t3_t1_t4 += MM[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 73
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	S += c_t4_t4_t0_in >= 73
	c_t4_t4_t0_in += MM_in[0]

	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem0 >= 73
	c_t4_t4_t0_mem0 += MAS_MEM[0]

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem1 >= 73
	c_t4_t4_t0_mem1 += MAS_MEM[5]

	c_t5_t50 = S.Task('c_t5_t50', length=3, delay_cost=1)
	S += c_t5_t50 >= 73
	c_t5_t50 += MAS[3]

	d_s1011_in = S.Task('d_s1011_in', length=1, delay_cost=1)
	S += d_s1011_in >= 73
	d_s1011_in += MAS_in[2]

	d_s1011_mem0 = S.Task('d_s1011_mem0', length=1, delay_cost=1)
	S += d_s1011_mem0 >= 73
	d_s1011_mem0 += MAS_MEM[6]

	d_s1011_mem1 = S.Task('d_s1011_mem1', length=1, delay_cost=1)
	S += d_s1011_mem1 >= 73
	d_s1011_mem1 += MAS_MEM[7]

	d_t0_t20 = S.Task('d_t0_t20', length=3, delay_cost=1)
	S += d_t0_t20 >= 73
	d_t0_t20 += MAS[2]

	c_t0_t41 = S.Task('c_t0_t41', length=3, delay_cost=1)
	S += c_t0_t41 >= 74
	c_t0_t41 += MAS[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 74
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 74
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	S += c_t4_t1_t4_in >= 74
	c_t4_t1_t4_in += MM_in[0]

	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem0 >= 74
	c_t4_t1_t4_mem0 += MAS_MEM[4]

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem1 >= 74
	c_t4_t1_t4_mem1 += MAS_MEM[5]

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=5, delay_cost=1)
	S += c_t4_t4_t0 >= 74
	c_t4_t4_t0 += MM[0]

	d_s1011 = S.Task('d_s1011', length=3, delay_cost=1)
	S += d_s1011 >= 74
	d_s1011 += MAS[2]

	d_t4_t31_in = S.Task('d_t4_t31_in', length=1, delay_cost=1)
	S += d_t4_t31_in >= 74
	d_t4_t31_in += MAS_in[2]

	d_t4_t31_mem0 = S.Task('d_t4_t31_mem0', length=1, delay_cost=1)
	S += d_t4_t31_mem0 >= 74
	d_t4_t31_mem0 += MM_MEM[0]

	d_t4_t31_mem1 = S.Task('d_t4_t31_mem1', length=1, delay_cost=1)
	S += d_t4_t31_mem1 >= 74
	d_t4_t31_mem1 += MAS_MEM[3]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 75
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=5, delay_cost=1)
	S += c_t4_t1_t4 >= 75
	c_t4_t1_t4 += MM[0]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 75
	c_t5001_mem0 += MAIN_MEM_r[0]

	d_t1_t20_in = S.Task('d_t1_t20_in', length=1, delay_cost=1)
	S += d_t1_t20_in >= 75
	d_t1_t20_in += MAS_in[0]

	d_t1_t20_mem0 = S.Task('d_t1_t20_mem0', length=1, delay_cost=1)
	S += d_t1_t20_mem0 >= 75
	d_t1_t20_mem0 += MM_MEM[0]

	d_t1_t20_mem1 = S.Task('d_t1_t20_mem1', length=1, delay_cost=1)
	S += d_t1_t20_mem1 >= 75
	d_t1_t20_mem1 += MM_MEM[1]

	d_t4_t31 = S.Task('d_t4_t31', length=3, delay_cost=1)
	S += d_t4_t31 >= 75
	d_t4_t31 += MAS[2]

	d_t5_t2_t1_in = S.Task('d_t5_t2_t1_in', length=1, delay_cost=1)
	S += d_t5_t2_t1_in >= 75
	d_t5_t2_t1_in += MM_in[0]

	d_t5_t2_t1_mem0 = S.Task('d_t5_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t1_mem0 >= 75
	d_t5_t2_t1_mem0 += MAS_MEM[4]

	d_t5_t2_t1_mem1 = S.Task('d_t5_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t1_mem1 >= 75
	d_t5_t2_t1_mem1 += MAS_MEM[3]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 76
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 76
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4_t50_in = S.Task('c_t4_t50_in', length=1, delay_cost=1)
	S += c_t4_t50_in >= 76
	c_t4_t50_in += MAS_in[2]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	S += c_t4_t50_mem0 >= 76
	c_t4_t50_mem0 += MAS_MEM[4]

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	S += c_t4_t50_mem1 >= 76
	c_t4_t50_mem1 += MAS_MEM[5]

	d_t0_t2_t4_in = S.Task('d_t0_t2_t4_in', length=1, delay_cost=1)
	S += d_t0_t2_t4_in >= 76
	d_t0_t2_t4_in += MM_in[0]

	d_t0_t2_t4_mem0 = S.Task('d_t0_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t4_mem0 >= 76
	d_t0_t2_t4_mem0 += MAS_MEM[0]

	d_t0_t2_t4_mem1 = S.Task('d_t0_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t4_mem1 >= 76
	d_t0_t2_t4_mem1 += MAS_MEM[7]

	d_t1_t20 = S.Task('d_t1_t20', length=3, delay_cost=1)
	S += d_t1_t20 >= 76
	d_t1_t20 += MAS[0]

	d_t5_t2_t1 = S.Task('d_t5_t2_t1', length=5, delay_cost=1)
	S += d_t5_t2_t1 >= 76
	d_t5_t2_t1 += MM[0]

	d_t5_t31_in = S.Task('d_t5_t31_in', length=1, delay_cost=1)
	S += d_t5_t31_in >= 76
	d_t5_t31_in += MAS_in[3]

	d_t5_t31_mem0 = S.Task('d_t5_t31_mem0', length=1, delay_cost=1)
	S += d_t5_t31_mem0 >= 76
	d_t5_t31_mem0 += MM_MEM[0]

	d_t5_t31_mem1 = S.Task('d_t5_t31_mem1', length=1, delay_cost=1)
	S += d_t5_t31_mem1 >= 76
	d_t5_t31_mem1 += MAS_MEM[1]

	c_t011_in = S.Task('c_t011_in', length=1, delay_cost=1)
	S += c_t011_in >= 77
	c_t011_in += MAS_in[1]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 77
	c_t011_mem0 += MAS_MEM[0]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 77
	c_t011_mem1 += MAS_MEM[1]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 77
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 77
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t4_t50 = S.Task('c_t4_t50', length=3, delay_cost=1)
	S += c_t4_t50 >= 77
	c_t4_t50 += MAS[2]

	d_t0_t2_t4 = S.Task('d_t0_t2_t4', length=5, delay_cost=1)
	S += d_t0_t2_t4 >= 77
	d_t0_t2_t4 += MM[0]

	d_t1_t2_t5_in = S.Task('d_t1_t2_t5_in', length=1, delay_cost=1)
	S += d_t1_t2_t5_in >= 77
	d_t1_t2_t5_in += MAS_in[3]

	d_t1_t2_t5_mem0 = S.Task('d_t1_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t5_mem0 >= 77
	d_t1_t2_t5_mem0 += MM_MEM[0]

	d_t1_t2_t5_mem1 = S.Task('d_t1_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t5_mem1 >= 77
	d_t1_t2_t5_mem1 += MM_MEM[1]

	d_t2_t2_t4_in = S.Task('d_t2_t2_t4_in', length=1, delay_cost=1)
	S += d_t2_t2_t4_in >= 77
	d_t2_t2_t4_in += MM_in[0]

	d_t2_t2_t4_mem0 = S.Task('d_t2_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t4_mem0 >= 77
	d_t2_t2_t4_mem0 += MAS_MEM[4]

	d_t2_t2_t4_mem1 = S.Task('d_t2_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t4_mem1 >= 77
	d_t2_t2_t4_mem1 += MAS_MEM[7]

	d_t4_t40_in = S.Task('d_t4_t40_in', length=1, delay_cost=1)
	S += d_t4_t40_in >= 77
	d_t4_t40_in += MAS_in[0]

	d_t4_t40_mem0 = S.Task('d_t4_t40_mem0', length=1, delay_cost=1)
	S += d_t4_t40_mem0 >= 77
	d_t4_t40_mem0 += MAS_MEM[2]

	d_t4_t40_mem1 = S.Task('d_t4_t40_mem1', length=1, delay_cost=1)
	S += d_t4_t40_mem1 >= 77
	d_t4_t40_mem1 += MAS_MEM[5]

	d_t5_t31 = S.Task('d_t5_t31', length=3, delay_cost=1)
	S += d_t5_t31 >= 77
	d_t5_t31 += MAS[3]

	c_t011 = S.Task('c_t011', length=3, delay_cost=1)
	S += c_t011 >= 78
	c_t011 += MAS[1]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 78
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 78
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	d_t0_t2_t5_in = S.Task('d_t0_t2_t5_in', length=1, delay_cost=1)
	S += d_t0_t2_t5_in >= 78
	d_t0_t2_t5_in += MAS_in[1]

	d_t0_t2_t5_mem0 = S.Task('d_t0_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t5_mem0 >= 78
	d_t0_t2_t5_mem0 += MM_MEM[0]

	d_t0_t2_t5_mem1 = S.Task('d_t0_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t5_mem1 >= 78
	d_t0_t2_t5_mem1 += MM_MEM[1]

	d_t1_t2_t5 = S.Task('d_t1_t2_t5', length=3, delay_cost=1)
	S += d_t1_t2_t5 >= 78
	d_t1_t2_t5 += MAS[3]

	d_t2_t2_t4 = S.Task('d_t2_t2_t4', length=5, delay_cost=1)
	S += d_t2_t2_t4 >= 78
	d_t2_t2_t4 += MM[0]

	d_t411_in = S.Task('d_t411_in', length=1, delay_cost=1)
	S += d_t411_in >= 78
	d_t411_in += MAS_in[2]

	d_t411_mem0 = S.Task('d_t411_mem0', length=1, delay_cost=1)
	S += d_t411_mem0 >= 78
	d_t411_mem0 += MAS_MEM[4]

	d_t4_t2_t1_in = S.Task('d_t4_t2_t1_in', length=1, delay_cost=1)
	S += d_t4_t2_t1_in >= 78
	d_t4_t2_t1_in += MM_in[0]

	d_t4_t2_t1_mem0 = S.Task('d_t4_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t1_mem0 >= 78
	d_t4_t2_t1_mem0 += MAS_MEM[6]

	d_t4_t2_t1_mem1 = S.Task('d_t4_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t1_mem1 >= 78
	d_t4_t2_t1_mem1 += MAS_MEM[3]

	d_t4_t40 = S.Task('d_t4_t40', length=3, delay_cost=1)
	S += d_t4_t40 >= 78
	d_t4_t40 += MAS[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 79
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 79
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t41_in = S.Task('c_t2_t41_in', length=1, delay_cost=1)
	S += c_t2_t41_in >= 79
	c_t2_t41_in += MAS_in[0]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 79
	c_t2_t41_mem0 += MM_MEM[0]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 79
	c_t2_t41_mem1 += MAS_MEM[5]

	d_t0_t2_t5 = S.Task('d_t0_t2_t5', length=3, delay_cost=1)
	S += d_t0_t2_t5 >= 79
	d_t0_t2_t5 += MAS[1]

	d_t3_t2_t1_in = S.Task('d_t3_t2_t1_in', length=1, delay_cost=1)
	S += d_t3_t2_t1_in >= 79
	d_t3_t2_t1_in += MM_in[0]

	d_t3_t2_t1_mem0 = S.Task('d_t3_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t1_mem0 >= 79
	d_t3_t2_t1_mem0 += MAS_MEM[2]

	d_t3_t2_t1_mem1 = S.Task('d_t3_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t1_mem1 >= 79
	d_t3_t2_t1_mem1 += MAS_MEM[1]

	d_t411 = S.Task('d_t411', length=3, delay_cost=1)
	S += d_t411 >= 79
	d_t411 += MAS[2]

	d_t4_t2_t1 = S.Task('d_t4_t2_t1', length=5, delay_cost=1)
	S += d_t4_t2_t1 >= 79
	d_t4_t2_t1 += MM[0]

	d_t4_t41_in = S.Task('d_t4_t41_in', length=1, delay_cost=1)
	S += d_t4_t41_in >= 79
	d_t4_t41_in += MAS_in[2]

	d_t4_t41_mem0 = S.Task('d_t4_t41_mem0', length=1, delay_cost=1)
	S += d_t4_t41_mem0 >= 79
	d_t4_t41_mem0 += MAS_MEM[4]

	d_t4_t41_mem1 = S.Task('d_t4_t41_mem1', length=1, delay_cost=1)
	S += d_t4_t41_mem1 >= 79
	d_t4_t41_mem1 += MAS_MEM[3]

	d_t5_t40_in = S.Task('d_t5_t40_in', length=1, delay_cost=1)
	S += d_t5_t40_in >= 79
	d_t5_t40_in += MAS_in[3]

	d_t5_t40_mem0 = S.Task('d_t5_t40_mem0', length=1, delay_cost=1)
	S += d_t5_t40_mem0 >= 79
	d_t5_t40_mem0 += MAS_MEM[6]

	d_t5_t40_mem1 = S.Task('d_t5_t40_mem1', length=1, delay_cost=1)
	S += d_t5_t40_mem1 >= 79
	d_t5_t40_mem1 += MAS_MEM[7]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 80
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t2_t41 = S.Task('c_t2_t41', length=3, delay_cost=1)
	S += c_t2_t41 >= 80
	c_t2_t41 += MAS[0]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 80
	c_t3011_mem0 += MAIN_MEM_r[0]

	d_t2_t2_t5_in = S.Task('d_t2_t2_t5_in', length=1, delay_cost=1)
	S += d_t2_t2_t5_in >= 80
	d_t2_t2_t5_in += MAS_in[0]

	d_t2_t2_t5_mem0 = S.Task('d_t2_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t5_mem0 >= 80
	d_t2_t2_t5_mem0 += MM_MEM[0]

	d_t2_t2_t5_mem1 = S.Task('d_t2_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t5_mem1 >= 80
	d_t2_t2_t5_mem1 += MM_MEM[1]

	d_t3_t2_t1 = S.Task('d_t3_t2_t1', length=5, delay_cost=1)
	S += d_t3_t2_t1 >= 80
	d_t3_t2_t1 += MM[0]

	d_t4_t41 = S.Task('d_t4_t41', length=3, delay_cost=1)
	S += d_t4_t41 >= 80
	d_t4_t41 += MAS[2]

	d_t511_in = S.Task('d_t511_in', length=1, delay_cost=1)
	S += d_t511_in >= 80
	d_t511_in += MAS_in[1]

	d_t511_mem0 = S.Task('d_t511_mem0', length=1, delay_cost=1)
	S += d_t511_mem0 >= 80
	d_t511_mem0 += MAS_MEM[6]

	d_t5_t2_t0_in = S.Task('d_t5_t2_t0_in', length=1, delay_cost=1)
	S += d_t5_t2_t0_in >= 80
	d_t5_t2_t0_in += MM_in[0]

	d_t5_t2_t0_mem0 = S.Task('d_t5_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t0_mem0 >= 80
	d_t5_t2_t0_mem0 += MAS_MEM[0]

	d_t5_t2_t0_mem1 = S.Task('d_t5_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t0_mem1 >= 80
	d_t5_t2_t0_mem1 += MAS_MEM[7]

	d_t5_t40 = S.Task('d_t5_t40', length=3, delay_cost=1)
	S += d_t5_t40 >= 80
	d_t5_t40 += MAS[3]

	c_t1_t41_in = S.Task('c_t1_t41_in', length=1, delay_cost=1)
	S += c_t1_t41_in >= 81
	c_t1_t41_in += MAS_in[2]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 81
	c_t1_t41_mem0 += MM_MEM[0]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 81
	c_t1_t41_mem1 += MAS_MEM[3]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 81
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 81
	c_t4011_mem0 += MAIN_MEM_r[0]

	d_t2_t2_t5 = S.Task('d_t2_t2_t5', length=3, delay_cost=1)
	S += d_t2_t2_t5 >= 81
	d_t2_t2_t5 += MAS[0]

	d_t4_t2_t0_in = S.Task('d_t4_t2_t0_in', length=1, delay_cost=1)
	S += d_t4_t2_t0_in >= 81
	d_t4_t2_t0_in += MM_in[0]

	d_t4_t2_t0_mem0 = S.Task('d_t4_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t0_mem0 >= 81
	d_t4_t2_t0_mem0 += MAS_MEM[2]

	d_t4_t2_t0_mem1 = S.Task('d_t4_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t0_mem1 >= 81
	d_t4_t2_t0_mem1 += MAS_MEM[5]

	d_t511 = S.Task('d_t511', length=3, delay_cost=1)
	S += d_t511 >= 81
	d_t511 += MAS[1]

	d_t5_t2_t0 = S.Task('d_t5_t2_t0', length=5, delay_cost=1)
	S += d_t5_t2_t0 >= 81
	d_t5_t2_t0 += MM[0]

	d_t5_t41_in = S.Task('d_t5_t41_in', length=1, delay_cost=1)
	S += d_t5_t41_in >= 81
	d_t5_t41_in += MAS_in[0]

	d_t5_t41_mem0 = S.Task('d_t5_t41_mem0', length=1, delay_cost=1)
	S += d_t5_t41_mem0 >= 81
	d_t5_t41_mem0 += MAS_MEM[6]

	d_t5_t41_mem1 = S.Task('d_t5_t41_mem1', length=1, delay_cost=1)
	S += d_t5_t41_mem1 >= 81
	d_t5_t41_mem1 += MAS_MEM[7]

	c_t1_t41 = S.Task('c_t1_t41', length=3, delay_cost=1)
	S += c_t1_t41 >= 82
	c_t1_t41 += MAS[2]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 82
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 82
	c_t5000_mem0 += MAIN_MEM_r[0]

	d_t1_t2_t4_in = S.Task('d_t1_t2_t4_in', length=1, delay_cost=1)
	S += d_t1_t2_t4_in >= 82
	d_t1_t2_t4_in += MM_in[0]

	d_t1_t2_t4_mem0 = S.Task('d_t1_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t4_mem0 >= 82
	d_t1_t2_t4_mem0 += MAS_MEM[0]

	d_t1_t2_t4_mem1 = S.Task('d_t1_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t4_mem1 >= 82
	d_t1_t2_t4_mem1 += MAS_MEM[7]

	d_t3_t31_in = S.Task('d_t3_t31_in', length=1, delay_cost=1)
	S += d_t3_t31_in >= 82
	d_t3_t31_in += MAS_in[1]

	d_t3_t31_mem0 = S.Task('d_t3_t31_mem0', length=1, delay_cost=1)
	S += d_t3_t31_mem0 >= 82
	d_t3_t31_mem0 += MM_MEM[0]

	d_t3_t31_mem1 = S.Task('d_t3_t31_mem1', length=1, delay_cost=1)
	S += d_t3_t31_mem1 >= 82
	d_t3_t31_mem1 += MAS_MEM[1]

	d_t4_t2_t0 = S.Task('d_t4_t2_t0', length=5, delay_cost=1)
	S += d_t4_t2_t0 >= 82
	d_t4_t2_t0 += MM[0]

	d_t5_t41 = S.Task('d_t5_t41', length=3, delay_cost=1)
	S += d_t5_t41 >= 82
	d_t5_t41 += MAS[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 83
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 83
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t5_t11_in = S.Task('c_t5_t11_in', length=1, delay_cost=1)
	S += c_t5_t11_in >= 83
	c_t5_t11_in += MAS_in[0]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 83
	c_t5_t11_mem0 += MM_MEM[0]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 83
	c_t5_t11_mem1 += MAS_MEM[7]

	d_t1_t2_t4 = S.Task('d_t1_t2_t4', length=5, delay_cost=1)
	S += d_t1_t2_t4 >= 83
	d_t1_t2_t4 += MM[0]

	d_t3_t2_t0_in = S.Task('d_t3_t2_t0_in', length=1, delay_cost=1)
	S += d_t3_t2_t0_in >= 83
	d_t3_t2_t0_in += MM_in[0]

	d_t3_t2_t0_mem0 = S.Task('d_t3_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t0_mem0 >= 83
	d_t3_t2_t0_mem0 += MAS_MEM[0]

	d_t3_t2_t0_mem1 = S.Task('d_t3_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t0_mem1 >= 83
	d_t3_t2_t0_mem1 += MAS_MEM[5]

	d_t3_t31 = S.Task('d_t3_t31', length=3, delay_cost=1)
	S += d_t3_t31 >= 83
	d_t3_t31 += MAS[1]

	c_t111_in = S.Task('c_t111_in', length=1, delay_cost=1)
	S += c_t111_in >= 84
	c_t111_in += MAS_in[2]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 84
	c_t111_mem0 += MAS_MEM[4]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 84
	c_t111_mem1 += MAS_MEM[1]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 84
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t5_in = S.Task('c_t3_t4_t5_in', length=1, delay_cost=1)
	S += c_t3_t4_t5_in >= 84
	c_t3_t4_t5_in += MAS_in[0]

	c_t3_t4_t5_mem0 = S.Task('c_t3_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem0 >= 84
	c_t3_t4_t5_mem0 += MM_MEM[0]

	c_t3_t4_t5_mem1 = S.Task('c_t3_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem1 >= 84
	c_t3_t4_t5_mem1 += MM_MEM[1]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 84
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5_t11 = S.Task('c_t5_t11', length=3, delay_cost=1)
	S += c_t5_t11 >= 84
	c_t5_t11 += MAS[0]

	c_t5_t4_t4_in = S.Task('c_t5_t4_t4_in', length=1, delay_cost=1)
	S += c_t5_t4_t4_in >= 84
	c_t5_t4_t4_in += MM_in[0]

	c_t5_t4_t4_mem0 = S.Task('c_t5_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem0 >= 84
	c_t5_t4_t4_mem0 += MAS_MEM[0]

	c_t5_t4_t4_mem1 = S.Task('c_t5_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem1 >= 84
	c_t5_t4_t4_mem1 += MAS_MEM[5]

	d_t3_t2_t0 = S.Task('d_t3_t2_t0', length=5, delay_cost=1)
	S += d_t3_t2_t0 >= 84
	d_t3_t2_t0 += MM[0]

	c_t111 = S.Task('c_t111', length=3, delay_cost=1)
	S += c_t111 >= 85
	c_t111 += MAS[2]

	c_t211_in = S.Task('c_t211_in', length=1, delay_cost=1)
	S += c_t211_in >= 85
	c_t211_in += MAS_in[1]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 85
	c_t211_mem0 += MAS_MEM[0]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 85
	c_t211_mem1 += MAS_MEM[7]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 85
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 85
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t5 = S.Task('c_t3_t4_t5', length=3, delay_cost=1)
	S += c_t3_t4_t5 >= 85
	c_t3_t4_t5 += MAS[0]

	c_t4_t4_t4_in = S.Task('c_t4_t4_t4_in', length=1, delay_cost=1)
	S += c_t4_t4_t4_in >= 85
	c_t4_t4_t4_in += MM_in[0]

	c_t4_t4_t4_mem0 = S.Task('c_t4_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem0 >= 85
	c_t4_t4_t4_mem0 += MAS_MEM[4]

	c_t4_t4_t4_mem1 = S.Task('c_t4_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem1 >= 85
	c_t4_t4_t4_mem1 += MAS_MEM[1]

	c_t5_t4_t4 = S.Task('c_t5_t4_t4', length=5, delay_cost=1)
	S += c_t5_t4_t4 >= 85
	c_t5_t4_t4 += MM[0]

	c_t5_t4_t5_in = S.Task('c_t5_t4_t5_in', length=1, delay_cost=1)
	S += c_t5_t4_t5_in >= 85
	c_t5_t4_t5_in += MAS_in[3]

	c_t5_t4_t5_mem0 = S.Task('c_t5_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem0 >= 85
	c_t5_t4_t5_mem0 += MM_MEM[0]

	c_t5_t4_t5_mem1 = S.Task('c_t5_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem1 >= 85
	c_t5_t4_t5_mem1 += MM_MEM[1]

	d_t311_in = S.Task('d_t311_in', length=1, delay_cost=1)
	S += d_t311_in >= 85
	d_t311_in += MAS_in[2]

	d_t311_mem0 = S.Task('d_t311_mem0', length=1, delay_cost=1)
	S += d_t311_mem0 >= 85
	d_t311_mem0 += MAS_MEM[2]

	d_t3_t40_in = S.Task('d_t3_t40_in', length=1, delay_cost=1)
	S += d_t3_t40_in >= 85
	d_t3_t40_in += MAS_in[0]

	d_t3_t40_mem0 = S.Task('d_t3_t40_mem0', length=1, delay_cost=1)
	S += d_t3_t40_mem0 >= 85
	d_t3_t40_mem0 += MAS_MEM[6]

	d_t3_t40_mem1 = S.Task('d_t3_t40_mem1', length=1, delay_cost=1)
	S += d_t3_t40_mem1 >= 85
	d_t3_t40_mem1 += MAS_MEM[3]

	c_t211 = S.Task('c_t211', length=3, delay_cost=1)
	S += c_t211 >= 86
	c_t211 += MAS[1]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 86
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 86
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t4_in = S.Task('c_t3_t4_t4_in', length=1, delay_cost=1)
	S += c_t3_t4_t4_in >= 86
	c_t3_t4_t4_in += MM_in[0]

	c_t3_t4_t4_mem0 = S.Task('c_t3_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem0 >= 86
	c_t3_t4_t4_mem0 += MAS_MEM[4]

	c_t3_t4_t4_mem1 = S.Task('c_t3_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem1 >= 86
	c_t3_t4_t4_mem1 += MAS_MEM[3]

	c_t4_t4_t4 = S.Task('c_t4_t4_t4', length=5, delay_cost=1)
	S += c_t4_t4_t4 >= 86
	c_t4_t4_t4 += MM[0]

	c_t4_t4_t5_in = S.Task('c_t4_t4_t5_in', length=1, delay_cost=1)
	S += c_t4_t4_t5_in >= 86
	c_t4_t4_t5_in += MAS_in[3]

	c_t4_t4_t5_mem0 = S.Task('c_t4_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem0 >= 86
	c_t4_t4_t5_mem0 += MM_MEM[0]

	c_t4_t4_t5_mem1 = S.Task('c_t4_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem1 >= 86
	c_t4_t4_t5_mem1 += MM_MEM[1]

	c_t5_t4_t5 = S.Task('c_t5_t4_t5', length=3, delay_cost=1)
	S += c_t5_t4_t5 >= 86
	c_t5_t4_t5 += MAS[3]

	d_t311 = S.Task('d_t311', length=3, delay_cost=1)
	S += d_t311 >= 86
	d_t311 += MAS[2]

	d_t3_t40 = S.Task('d_t3_t40', length=3, delay_cost=1)
	S += d_t3_t40 >= 86
	d_t3_t40 += MAS[0]

	d_t3_t41_in = S.Task('d_t3_t41_in', length=1, delay_cost=1)
	S += d_t3_t41_in >= 86
	d_t3_t41_in += MAS_in[1]

	d_t3_t41_mem0 = S.Task('d_t3_t41_mem0', length=1, delay_cost=1)
	S += d_t3_t41_mem0 >= 86
	d_t3_t41_mem0 += MAS_MEM[2]

	d_t3_t41_mem1 = S.Task('d_t3_t41_mem1', length=1, delay_cost=1)
	S += d_t3_t41_mem1 >= 86
	d_t3_t41_mem1 += MAS_MEM[7]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 87
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 87
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t4 = S.Task('c_t3_t4_t4', length=5, delay_cost=1)
	S += c_t3_t4_t4 >= 87
	c_t3_t4_t4 += MM[0]

	c_t4_t4_t5 = S.Task('c_t4_t4_t5', length=3, delay_cost=1)
	S += c_t4_t4_t5 >= 87
	c_t4_t4_t5 += MAS[3]

	c_t5_t01_in = S.Task('c_t5_t01_in', length=1, delay_cost=1)
	S += c_t5_t01_in >= 87
	c_t5_t01_in += MAS_in[2]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 87
	c_t5_t01_mem0 += MM_MEM[0]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 87
	c_t5_t01_mem1 += MAS_MEM[7]

	d_t3_t41 = S.Task('d_t3_t41', length=3, delay_cost=1)
	S += d_t3_t41 >= 87
	d_t3_t41 += MAS[1]

	d_t4_t2_t4_in = S.Task('d_t4_t2_t4_in', length=1, delay_cost=1)
	S += d_t4_t2_t4_in >= 87
	d_t4_t2_t4_in += MM_in[0]

	d_t4_t2_t4_mem0 = S.Task('d_t4_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t4_mem0 >= 87
	d_t4_t2_t4_mem0 += MAS_MEM[2]

	d_t4_t2_t4_mem1 = S.Task('d_t4_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t4_mem1 >= 87
	d_t4_t2_t4_mem1 += MAS_MEM[3]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 88
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t3_t01_in = S.Task('c_t3_t01_in', length=1, delay_cost=1)
	S += c_t3_t01_in >= 88
	c_t3_t01_in += MAS_in[1]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 88
	c_t3_t01_mem0 += MM_MEM[0]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 88
	c_t3_t01_mem1 += MAS_MEM[7]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 88
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t5_t01 = S.Task('c_t5_t01', length=3, delay_cost=1)
	S += c_t5_t01 >= 88
	c_t5_t01 += MAS[2]

	d_t3_t2_t4_in = S.Task('d_t3_t2_t4_in', length=1, delay_cost=1)
	S += d_t3_t2_t4_in >= 88
	d_t3_t2_t4_in += MM_in[0]

	d_t3_t2_t4_mem0 = S.Task('d_t3_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t4_mem0 >= 88
	d_t3_t2_t4_mem0 += MAS_MEM[0]

	d_t3_t2_t4_mem1 = S.Task('d_t3_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t4_mem1 >= 88
	d_t3_t2_t4_mem1 += MAS_MEM[1]

	d_t4_t2_t4 = S.Task('d_t4_t2_t4', length=5, delay_cost=1)
	S += d_t4_t2_t4 >= 88
	d_t4_t2_t4 += MM[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 89
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t3_t01 = S.Task('c_t3_t01', length=3, delay_cost=1)
	S += c_t3_t01 >= 89
	c_t3_t01 += MAS[1]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 89
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4_t11_in = S.Task('c_t4_t11_in', length=1, delay_cost=1)
	S += c_t4_t11_in >= 89
	c_t4_t11_in += MAS_in[2]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 89
	c_t4_t11_mem0 += MM_MEM[0]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 89
	c_t4_t11_mem1 += MAS_MEM[5]

	d_t3_t2_t4 = S.Task('d_t3_t2_t4', length=5, delay_cost=1)
	S += d_t3_t2_t4 >= 89
	d_t3_t2_t4 += MM[0]

	d_t5_t2_t4_in = S.Task('d_t5_t2_t4_in', length=1, delay_cost=1)
	S += d_t5_t2_t4_in >= 89
	d_t5_t2_t4_in += MM_in[0]

	d_t5_t2_t4_mem0 = S.Task('d_t5_t2_t4_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t4_mem0 >= 89
	d_t5_t2_t4_mem0 += MAS_MEM[0]

	d_t5_t2_t4_mem1 = S.Task('d_t5_t2_t4_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t4_mem1 >= 89
	d_t5_t2_t4_mem1 += MAS_MEM[7]

	c_t4_t11 = S.Task('c_t4_t11', length=3, delay_cost=1)
	S += c_t4_t11 >= 90
	c_t4_t11 += MAS[2]

	c_t4_t40_in = S.Task('c_t4_t40_in', length=1, delay_cost=1)
	S += c_t4_t40_in >= 90
	c_t4_t40_in += MAS_in[2]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	S += c_t4_t40_mem0 >= 90
	c_t4_t40_mem0 += MM_MEM[0]

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	S += c_t4_t40_mem1 >= 90
	c_t4_t40_mem1 += MM_MEM[1]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 90
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 90
	c_t5100_mem1 += MAIN_MEM_r[1]

	d_t5_t2_t4 = S.Task('d_t5_t2_t4', length=5, delay_cost=1)
	S += d_t5_t2_t4 >= 90
	d_t5_t2_t4 += MM[0]

	c_t4_t40 = S.Task('c_t4_t40', length=3, delay_cost=1)
	S += c_t4_t40 >= 91
	c_t4_t40 += MAS[2]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 91
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 91
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5_t40_in = S.Task('c_t5_t40_in', length=1, delay_cost=1)
	S += c_t5_t40_in >= 91
	c_t5_t40_in += MAS_in[3]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	S += c_t5_t40_mem0 >= 91
	c_t5_t40_mem0 += MM_MEM[0]

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	S += c_t5_t40_mem1 >= 91
	c_t5_t40_mem1 += MM_MEM[1]

	c_t3_t40_in = S.Task('c_t3_t40_in', length=1, delay_cost=1)
	S += c_t3_t40_in >= 92
	c_t3_t40_in += MAS_in[2]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	S += c_t3_t40_mem0 >= 92
	c_t3_t40_mem0 += MM_MEM[0]

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	S += c_t3_t40_mem1 >= 92
	c_t3_t40_mem1 += MM_MEM[1]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 92
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 92
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5_t40 = S.Task('c_t5_t40', length=3, delay_cost=1)
	S += c_t5_t40 >= 92
	c_t5_t40 += MAS[3]

	c_t3_t40 = S.Task('c_t3_t40', length=3, delay_cost=1)
	S += c_t3_t40 >= 93
	c_t3_t40 += MAS[2]

	c_t4_t01_in = S.Task('c_t4_t01_in', length=1, delay_cost=1)
	S += c_t4_t01_in >= 93
	c_t4_t01_in += MAS_in[0]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 93
	c_t4_t01_mem0 += MM_MEM[0]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 93
	c_t4_t01_mem1 += MAS_MEM[3]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 93
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 93
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t3_t11_in = S.Task('c_t3_t11_in', length=1, delay_cost=1)
	S += c_t3_t11_in >= 94
	c_t3_t11_in += MAS_in[0]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 94
	c_t3_t11_mem0 += MM_MEM[0]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 94
	c_t3_t11_mem1 += MAS_MEM[1]

	c_t4_t01 = S.Task('c_t4_t01', length=3, delay_cost=1)
	S += c_t4_t01 >= 94
	c_t4_t01 += MAS[0]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 94
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 94
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t310_in = S.Task('c_t310_in', length=1, delay_cost=1)
	S += c_t310_in >= 95
	c_t310_in += MAS_in[2]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 95
	c_t310_mem0 += MAS_MEM[4]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 95
	c_t310_mem1 += MAS_MEM[3]

	c_t3_t11 = S.Task('c_t3_t11', length=3, delay_cost=1)
	S += c_t3_t11 >= 95
	c_t3_t11 += MAS[0]

	c_t3_t41_in = S.Task('c_t3_t41_in', length=1, delay_cost=1)
	S += c_t3_t41_in >= 95
	c_t3_t41_in += MAS_in[3]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	S += c_t3_t41_mem0 >= 95
	c_t3_t41_mem0 += MM_MEM[0]

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	S += c_t3_t41_mem1 >= 95
	c_t3_t41_mem1 += MAS_MEM[1]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 95
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 95
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t310 = S.Task('c_t310', length=3, delay_cost=1)
	S += c_t310 >= 96
	c_t310 += MAS[2]

	c_t3_t41 = S.Task('c_t3_t41', length=3, delay_cost=1)
	S += c_t3_t41 >= 96
	c_t3_t41 += MAS[3]

	d_t1_t01_mem0 = S.Task('d_t1_t01_mem0', length=1, delay_cost=1)
	S += d_t1_t01_mem0 >= 96
	d_t1_t01_mem0 += MAIN_MEM_r[0]

	d_t3_t2_t5_in = S.Task('d_t3_t2_t5_in', length=1, delay_cost=1)
	S += d_t3_t2_t5_in >= 96
	d_t3_t2_t5_in += MAS_in[3]

	d_t3_t2_t5_mem0 = S.Task('d_t3_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t5_mem0 >= 96
	d_t3_t2_t5_mem0 += MM_MEM[0]

	d_t3_t2_t5_mem1 = S.Task('d_t3_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t5_mem1 >= 96
	d_t3_t2_t5_mem1 += MM_MEM[1]

	c_t3_s01_in = S.Task('c_t3_s01_in', length=1, delay_cost=1)
	S += c_t3_s01_in >= 97
	c_t3_s01_in += MAS_in[0]

	c_t3_s01_mem0 = S.Task('c_t3_s01_mem0', length=1, delay_cost=1)
	S += c_t3_s01_mem0 >= 97
	c_t3_s01_mem0 += MAS_MEM[0]

	c_t3_s01_mem1 = S.Task('c_t3_s01_mem1', length=1, delay_cost=1)
	S += c_t3_s01_mem1 >= 97
	c_t3_s01_mem1 += MAS_MEM[5]

	c_t3_t51_in = S.Task('c_t3_t51_in', length=1, delay_cost=1)
	S += c_t3_t51_in >= 97
	c_t3_t51_in += MAS_in[3]

	c_t3_t51_mem0 = S.Task('c_t3_t51_mem0', length=1, delay_cost=1)
	S += c_t3_t51_mem0 >= 97
	c_t3_t51_mem0 += MAS_MEM[2]

	c_t3_t51_mem1 = S.Task('c_t3_t51_mem1', length=1, delay_cost=1)
	S += c_t3_t51_mem1 >= 97
	c_t3_t51_mem1 += MAS_MEM[1]

	d_t1_t00_mem0 = S.Task('d_t1_t00_mem0', length=1, delay_cost=1)
	S += d_t1_t00_mem0 >= 97
	d_t1_t00_mem0 += MAIN_MEM_r[0]

	d_t3_t2_t5 = S.Task('d_t3_t2_t5', length=3, delay_cost=1)
	S += d_t3_t2_t5 >= 97
	d_t3_t2_t5 += MAS[3]

	d_t4_t2_t5_in = S.Task('d_t4_t2_t5_in', length=1, delay_cost=1)
	S += d_t4_t2_t5_in >= 97
	d_t4_t2_t5_in += MAS_in[2]

	d_t4_t2_t5_mem0 = S.Task('d_t4_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t5_mem0 >= 97
	d_t4_t2_t5_mem0 += MM_MEM[0]

	d_t4_t2_t5_mem1 = S.Task('d_t4_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t5_mem1 >= 97
	d_t4_t2_t5_mem1 += MM_MEM[1]

	c_t3_s00_in = S.Task('c_t3_s00_in', length=1, delay_cost=1)
	S += c_t3_s00_in >= 98
	c_t3_s00_in += MAS_in[1]

	c_t3_s00_mem0 = S.Task('c_t3_s00_mem0', length=1, delay_cost=1)
	S += c_t3_s00_mem0 >= 98
	c_t3_s00_mem0 += MAS_MEM[4]

	c_t3_s00_mem1 = S.Task('c_t3_s00_mem1', length=1, delay_cost=1)
	S += c_t3_s00_mem1 >= 98
	c_t3_s00_mem1 += MAS_MEM[1]

	c_t3_s01 = S.Task('c_t3_s01', length=3, delay_cost=1)
	S += c_t3_s01 >= 98
	c_t3_s01 += MAS[0]

	c_t3_t51 = S.Task('c_t3_t51', length=3, delay_cost=1)
	S += c_t3_t51 >= 98
	c_t3_t51 += MAS[3]

	d_t0_t01_mem0 = S.Task('d_t0_t01_mem0', length=1, delay_cost=1)
	S += d_t0_t01_mem0 >= 98
	d_t0_t01_mem0 += MAIN_MEM_r[0]

	d_t4_t20_in = S.Task('d_t4_t20_in', length=1, delay_cost=1)
	S += d_t4_t20_in >= 98
	d_t4_t20_in += MAS_in[2]

	d_t4_t20_mem0 = S.Task('d_t4_t20_mem0', length=1, delay_cost=1)
	S += d_t4_t20_mem0 >= 98
	d_t4_t20_mem0 += MM_MEM[0]

	d_t4_t20_mem1 = S.Task('d_t4_t20_mem1', length=1, delay_cost=1)
	S += d_t4_t20_mem1 >= 98
	d_t4_t20_mem1 += MM_MEM[1]

	d_t4_t2_t5 = S.Task('d_t4_t2_t5', length=3, delay_cost=1)
	S += d_t4_t2_t5 >= 98
	d_t4_t2_t5 += MAS[2]

	c_t3_s00 = S.Task('c_t3_s00', length=3, delay_cost=1)
	S += c_t3_s00 >= 99
	c_t3_s00 += MAS[1]

	d_t0_t00_mem0 = S.Task('d_t0_t00_mem0', length=1, delay_cost=1)
	S += d_t0_t00_mem0 >= 99
	d_t0_t00_mem0 += MAIN_MEM_r[0]

	d_t4_t20 = S.Task('d_t4_t20', length=3, delay_cost=1)
	S += d_t4_t20 >= 99
	d_t4_t20 += MAS[2]

	d_t5_t20_in = S.Task('d_t5_t20_in', length=1, delay_cost=1)
	S += d_t5_t20_in >= 99
	d_t5_t20_in += MAS_in[0]

	d_t5_t20_mem0 = S.Task('d_t5_t20_mem0', length=1, delay_cost=1)
	S += d_t5_t20_mem0 >= 99
	d_t5_t20_mem0 += MM_MEM[0]

	d_t5_t20_mem1 = S.Task('d_t5_t20_mem1', length=1, delay_cost=1)
	S += d_t5_t20_mem1 >= 99
	d_t5_t20_mem1 += MM_MEM[1]

	d_t2_t00_mem0 = S.Task('d_t2_t00_mem0', length=1, delay_cost=1)
	S += d_t2_t00_mem0 >= 100
	d_t2_t00_mem0 += MAIN_MEM_r[0]

	d_t5_t20 = S.Task('d_t5_t20', length=3, delay_cost=1)
	S += d_t5_t20 >= 100
	d_t5_t20 += MAS[0]

	d_t5_t2_t5_in = S.Task('d_t5_t2_t5_in', length=1, delay_cost=1)
	S += d_t5_t2_t5_in >= 100
	d_t5_t2_t5_in += MAS_in[0]

	d_t5_t2_t5_mem0 = S.Task('d_t5_t2_t5_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t5_mem0 >= 100
	d_t5_t2_t5_mem0 += MM_MEM[0]

	d_t5_t2_t5_mem1 = S.Task('d_t5_t2_t5_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t5_mem1 >= 100
	d_t5_t2_t5_mem1 += MM_MEM[1]

	d_t2_t01_mem0 = S.Task('d_t2_t01_mem0', length=1, delay_cost=1)
	S += d_t2_t01_mem0 >= 101
	d_t2_t01_mem0 += MAIN_MEM_r[0]

	d_t3_t20_in = S.Task('d_t3_t20_in', length=1, delay_cost=1)
	S += d_t3_t20_in >= 101
	d_t3_t20_in += MAS_in[3]

	d_t3_t20_mem0 = S.Task('d_t3_t20_mem0', length=1, delay_cost=1)
	S += d_t3_t20_mem0 >= 101
	d_t3_t20_mem0 += MM_MEM[0]

	d_t3_t20_mem1 = S.Task('d_t3_t20_mem1', length=1, delay_cost=1)
	S += d_t3_t20_mem1 >= 101
	d_t3_t20_mem1 += MM_MEM[1]

	d_t5_t2_t5 = S.Task('d_t5_t2_t5', length=3, delay_cost=1)
	S += d_t5_t2_t5 >= 101
	d_t5_t2_t5 += MAS[0]

	d_t1_t21_in = S.Task('d_t1_t21_in', length=1, delay_cost=1)
	S += d_t1_t21_in >= 102
	d_t1_t21_in += MAS_in[0]

	d_t1_t21_mem0 = S.Task('d_t1_t21_mem0', length=1, delay_cost=1)
	S += d_t1_t21_mem0 >= 102
	d_t1_t21_mem0 += MM_MEM[0]

	d_t1_t21_mem1 = S.Task('d_t1_t21_mem1', length=1, delay_cost=1)
	S += d_t1_t21_mem1 >= 102
	d_t1_t21_mem1 += MAS_MEM[7]

	d_t3_t20 = S.Task('d_t3_t20', length=3, delay_cost=1)
	S += d_t3_t20 >= 102
	d_t3_t20 += MAS[3]

	d_t0_t21_in = S.Task('d_t0_t21_in', length=1, delay_cost=1)
	S += d_t0_t21_in >= 103
	d_t0_t21_in += MAS_in[1]

	d_t0_t21_mem0 = S.Task('d_t0_t21_mem0', length=1, delay_cost=1)
	S += d_t0_t21_mem0 >= 103
	d_t0_t21_mem0 += MM_MEM[0]

	d_t0_t21_mem1 = S.Task('d_t0_t21_mem1', length=1, delay_cost=1)
	S += d_t0_t21_mem1 >= 103
	d_t0_t21_mem1 += MAS_MEM[3]

	d_t1_t21 = S.Task('d_t1_t21', length=3, delay_cost=1)
	S += d_t1_t21 >= 103
	d_t1_t21 += MAS[0]

	d_t0_t21 = S.Task('d_t0_t21', length=3, delay_cost=1)
	S += d_t0_t21 >= 104
	d_t0_t21 += MAS[1]

	d_t2_t21_in = S.Task('d_t2_t21_in', length=1, delay_cost=1)
	S += d_t2_t21_in >= 104
	d_t2_t21_in += MAS_in[2]

	d_t2_t21_mem0 = S.Task('d_t2_t21_mem0', length=1, delay_cost=1)
	S += d_t2_t21_mem0 >= 104
	d_t2_t21_mem0 += MM_MEM[0]

	d_t2_t21_mem1 = S.Task('d_t2_t21_mem1', length=1, delay_cost=1)
	S += d_t2_t21_mem1 >= 104
	d_t2_t21_mem1 += MAS_MEM[1]

	c_t4_t41_in = S.Task('c_t4_t41_in', length=1, delay_cost=1)
	S += c_t4_t41_in >= 105
	c_t4_t41_in += MAS_in[1]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	S += c_t4_t41_mem0 >= 105
	c_t4_t41_mem0 += MM_MEM[0]

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	S += c_t4_t41_mem1 >= 105
	c_t4_t41_mem1 += MAS_MEM[7]

	d_t2_t21 = S.Task('d_t2_t21', length=3, delay_cost=1)
	S += d_t2_t21 >= 105
	d_t2_t21 += MAS[2]

	c_t4_t41 = S.Task('c_t4_t41', length=3, delay_cost=1)
	S += c_t4_t41 >= 106
	c_t4_t41 += MAS[1]


	# new tasks
	c_t4_s00 = S.Task('c_t4_s00', length=3, delay_cost=1)
	c_t4_s00 += alt(MAS)
	c_t4_s00_in = S.Task('c_t4_s00_in', length=1, delay_cost=1)
	c_t4_s00_in += alt(MAS_in)
	S += c_t4_s00_in*MAS_in[0]<=c_t4_s00*MAS[0]

	S += c_t4_s00_in*MAS_in[1]<=c_t4_s00*MAS[1]

	S += c_t4_s00_in*MAS_in[2]<=c_t4_s00*MAS[2]

	S += c_t4_s00_in*MAS_in[3]<=c_t4_s00*MAS[3]

	c_t4_s00_mem0 = S.Task('c_t4_s00_mem0', length=1, delay_cost=1)
	c_t4_s00_mem0 += MAS_MEM[4]
	S += 73 < c_t4_s00_mem0
	S += c_t4_s00_mem0 <= c_t4_s00

	c_t4_s00_mem1 = S.Task('c_t4_s00_mem1', length=1, delay_cost=1)
	c_t4_s00_mem1 += MAS_MEM[5]
	S += 92 < c_t4_s00_mem1
	S += c_t4_s00_mem1 <= c_t4_s00

	c_t4_s01 = S.Task('c_t4_s01', length=3, delay_cost=1)
	c_t4_s01 += alt(MAS)
	c_t4_s01_in = S.Task('c_t4_s01_in', length=1, delay_cost=1)
	c_t4_s01_in += alt(MAS_in)
	S += c_t4_s01_in*MAS_in[0]<=c_t4_s01*MAS[0]

	S += c_t4_s01_in*MAS_in[1]<=c_t4_s01*MAS[1]

	S += c_t4_s01_in*MAS_in[2]<=c_t4_s01*MAS[2]

	S += c_t4_s01_in*MAS_in[3]<=c_t4_s01*MAS[3]

	c_t4_s01_mem0 = S.Task('c_t4_s01_mem0', length=1, delay_cost=1)
	c_t4_s01_mem0 += MAS_MEM[4]
	S += 92 < c_t4_s01_mem0
	S += c_t4_s01_mem0 <= c_t4_s01

	c_t4_s01_mem1 = S.Task('c_t4_s01_mem1', length=1, delay_cost=1)
	c_t4_s01_mem1 += MAS_MEM[5]
	S += 73 < c_t4_s01_mem1
	S += c_t4_s01_mem1 <= c_t4_s01

	c_t4_t51 = S.Task('c_t4_t51', length=3, delay_cost=1)
	c_t4_t51 += alt(MAS)
	c_t4_t51_in = S.Task('c_t4_t51_in', length=1, delay_cost=1)
	c_t4_t51_in += alt(MAS_in)
	S += c_t4_t51_in*MAS_in[0]<=c_t4_t51*MAS[0]

	S += c_t4_t51_in*MAS_in[1]<=c_t4_t51*MAS[1]

	S += c_t4_t51_in*MAS_in[2]<=c_t4_t51*MAS[2]

	S += c_t4_t51_in*MAS_in[3]<=c_t4_t51*MAS[3]

	c_t4_t51_mem0 = S.Task('c_t4_t51_mem0', length=1, delay_cost=1)
	c_t4_t51_mem0 += MAS_MEM[0]
	S += 96 < c_t4_t51_mem0
	S += c_t4_t51_mem0 <= c_t4_t51

	c_t4_t51_mem1 = S.Task('c_t4_t51_mem1', length=1, delay_cost=1)
	c_t4_t51_mem1 += MAS_MEM[5]
	S += 92 < c_t4_t51_mem1
	S += c_t4_t51_mem1 <= c_t4_t51

	c_t410 = S.Task('c_t410', length=3, delay_cost=1)
	c_t410 += alt(MAS)
	c_t410_in = S.Task('c_t410_in', length=1, delay_cost=1)
	c_t410_in += alt(MAS_in)
	S += c_t410_in*MAS_in[0]<=c_t410*MAS[0]

	S += c_t410_in*MAS_in[1]<=c_t410*MAS[1]

	S += c_t410_in*MAS_in[2]<=c_t410*MAS[2]

	S += c_t410_in*MAS_in[3]<=c_t410*MAS[3]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	c_t410_mem0 += MAS_MEM[4]
	S += 93 < c_t410_mem0
	S += c_t410_mem0 <= c_t410

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	c_t410_mem1 += MAS_MEM[5]
	S += 79 < c_t410_mem1
	S += c_t410_mem1 <= c_t410

	c_t5_t41 = S.Task('c_t5_t41', length=3, delay_cost=1)
	c_t5_t41 += alt(MAS)
	c_t5_t41_in = S.Task('c_t5_t41_in', length=1, delay_cost=1)
	c_t5_t41_in += alt(MAS_in)
	S += c_t5_t41_in*MAS_in[0]<=c_t5_t41*MAS[0]

	S += c_t5_t41_in*MAS_in[1]<=c_t5_t41*MAS[1]

	S += c_t5_t41_in*MAS_in[2]<=c_t5_t41*MAS[2]

	S += c_t5_t41_in*MAS_in[3]<=c_t5_t41*MAS[3]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	c_t5_t41_mem0 += MM_MEM[0]
	S += 89 < c_t5_t41_mem0
	S += c_t5_t41_mem0 <= c_t5_t41

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	c_t5_t41_mem1 += MAS_MEM[7]
	S += 88 < c_t5_t41_mem1
	S += c_t5_t41_mem1 <= c_t5_t41

	c_t5_s00 = S.Task('c_t5_s00', length=3, delay_cost=1)
	c_t5_s00 += alt(MAS)
	c_t5_s00_in = S.Task('c_t5_s00_in', length=1, delay_cost=1)
	c_t5_s00_in += alt(MAS_in)
	S += c_t5_s00_in*MAS_in[0]<=c_t5_s00*MAS[0]

	S += c_t5_s00_in*MAS_in[1]<=c_t5_s00*MAS[1]

	S += c_t5_s00_in*MAS_in[2]<=c_t5_s00*MAS[2]

	S += c_t5_s00_in*MAS_in[3]<=c_t5_s00*MAS[3]

	c_t5_s00_mem0 = S.Task('c_t5_s00_mem0', length=1, delay_cost=1)
	c_t5_s00_mem0 += MAS_MEM[4]
	S += 67 < c_t5_s00_mem0
	S += c_t5_s00_mem0 <= c_t5_s00

	c_t5_s00_mem1 = S.Task('c_t5_s00_mem1', length=1, delay_cost=1)
	c_t5_s00_mem1 += MAS_MEM[1]
	S += 86 < c_t5_s00_mem1
	S += c_t5_s00_mem1 <= c_t5_s00

	c_t5_s01 = S.Task('c_t5_s01', length=3, delay_cost=1)
	c_t5_s01 += alt(MAS)
	c_t5_s01_in = S.Task('c_t5_s01_in', length=1, delay_cost=1)
	c_t5_s01_in += alt(MAS_in)
	S += c_t5_s01_in*MAS_in[0]<=c_t5_s01*MAS[0]

	S += c_t5_s01_in*MAS_in[1]<=c_t5_s01*MAS[1]

	S += c_t5_s01_in*MAS_in[2]<=c_t5_s01*MAS[2]

	S += c_t5_s01_in*MAS_in[3]<=c_t5_s01*MAS[3]

	c_t5_s01_mem0 = S.Task('c_t5_s01_mem0', length=1, delay_cost=1)
	c_t5_s01_mem0 += MAS_MEM[0]
	S += 86 < c_t5_s01_mem0
	S += c_t5_s01_mem0 <= c_t5_s01

	c_t5_s01_mem1 = S.Task('c_t5_s01_mem1', length=1, delay_cost=1)
	c_t5_s01_mem1 += MAS_MEM[5]
	S += 67 < c_t5_s01_mem1
	S += c_t5_s01_mem1 <= c_t5_s01

	c_t5_t51 = S.Task('c_t5_t51', length=3, delay_cost=1)
	c_t5_t51 += alt(MAS)
	c_t5_t51_in = S.Task('c_t5_t51_in', length=1, delay_cost=1)
	c_t5_t51_in += alt(MAS_in)
	S += c_t5_t51_in*MAS_in[0]<=c_t5_t51*MAS[0]

	S += c_t5_t51_in*MAS_in[1]<=c_t5_t51*MAS[1]

	S += c_t5_t51_in*MAS_in[2]<=c_t5_t51*MAS[2]

	S += c_t5_t51_in*MAS_in[3]<=c_t5_t51*MAS[3]

	c_t5_t51_mem0 = S.Task('c_t5_t51_mem0', length=1, delay_cost=1)
	c_t5_t51_mem0 += MAS_MEM[4]
	S += 90 < c_t5_t51_mem0
	S += c_t5_t51_mem0 <= c_t5_t51

	c_t5_t51_mem1 = S.Task('c_t5_t51_mem1', length=1, delay_cost=1)
	c_t5_t51_mem1 += MAS_MEM[1]
	S += 86 < c_t5_t51_mem1
	S += c_t5_t51_mem1 <= c_t5_t51

	c_t510 = S.Task('c_t510', length=3, delay_cost=1)
	c_t510 += alt(MAS)
	c_t510_in = S.Task('c_t510_in', length=1, delay_cost=1)
	c_t510_in += alt(MAS_in)
	S += c_t510_in*MAS_in[0]<=c_t510*MAS[0]

	S += c_t510_in*MAS_in[1]<=c_t510*MAS[1]

	S += c_t510_in*MAS_in[2]<=c_t510*MAS[2]

	S += c_t510_in*MAS_in[3]<=c_t510*MAS[3]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	c_t510_mem0 += MAS_MEM[6]
	S += 94 < c_t510_mem0
	S += c_t510_mem0 <= c_t510

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	c_t510_mem1 += MAS_MEM[7]
	S += 75 < c_t510_mem1
	S += c_t510_mem1 <= c_t510

	c_t6010 = S.Task('c_t6010', length=3, delay_cost=1)
	c_t6010 += alt(MAS)
	c_t6010_in = S.Task('c_t6010_in', length=1, delay_cost=1)
	c_t6010_in += alt(MAS_in)
	S += c_t6010_in*MAS_in[0]<=c_t6010*MAS[0]

	S += c_t6010_in*MAS_in[1]<=c_t6010*MAS[1]

	S += c_t6010_in*MAS_in[2]<=c_t6010*MAS[2]

	S += c_t6010_in*MAS_in[3]<=c_t6010*MAS[3]

	c_t6010_mem0 = S.Task('c_t6010_mem0', length=1, delay_cost=1)
	c_t6010_mem0 += MAS_MEM[2]
	S += 49 < c_t6010_mem0
	S += c_t6010_mem0 <= c_t6010

	c_t6010_mem1 = S.Task('c_t6010_mem1', length=1, delay_cost=1)
	c_t6010_mem1 += MAS_MEM[3]
	S += 62 < c_t6010_mem1
	S += c_t6010_mem1 <= c_t6010

	c_t7010 = S.Task('c_t7010', length=3, delay_cost=1)
	c_t7010 += alt(MAS)
	c_t7010_in = S.Task('c_t7010_in', length=1, delay_cost=1)
	c_t7010_in += alt(MAS_in)
	S += c_t7010_in*MAS_in[0]<=c_t7010*MAS[0]

	S += c_t7010_in*MAS_in[1]<=c_t7010*MAS[1]

	S += c_t7010_in*MAS_in[2]<=c_t7010*MAS[2]

	S += c_t7010_in*MAS_in[3]<=c_t7010*MAS[3]

	c_t7010_mem0 = S.Task('c_t7010_mem0', length=1, delay_cost=1)
	c_t7010_mem0 += MAS_MEM[2]
	S += 62 < c_t7010_mem0
	S += c_t7010_mem0 <= c_t7010

	c_t7010_mem1 = S.Task('c_t7010_mem1', length=1, delay_cost=1)
	c_t7010_mem1 += MAS_MEM[1]
	S += 65 < c_t7010_mem1
	S += c_t7010_mem1 <= c_t7010

	c_t8010 = S.Task('c_t8010', length=3, delay_cost=1)
	c_t8010 += alt(MAS)
	c_t8010_in = S.Task('c_t8010_in', length=1, delay_cost=1)
	c_t8010_in += alt(MAS_in)
	S += c_t8010_in*MAS_in[0]<=c_t8010*MAS[0]

	S += c_t8010_in*MAS_in[1]<=c_t8010*MAS[1]

	S += c_t8010_in*MAS_in[2]<=c_t8010*MAS[2]

	S += c_t8010_in*MAS_in[3]<=c_t8010*MAS[3]

	c_t8010_mem0 = S.Task('c_t8010_mem0', length=1, delay_cost=1)
	c_t8010_mem0 += MAS_MEM[0]
	S += 65 < c_t8010_mem0
	S += c_t8010_mem0 <= c_t8010

	c_t8010_mem1 = S.Task('c_t8010_mem1', length=1, delay_cost=1)
	c_t8010_mem1 += MAS_MEM[3]
	S += 49 < c_t8010_mem1
	S += c_t8010_mem1 <= c_t8010

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage3MAS4/FP12_LADDERMUL/schedule12.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

