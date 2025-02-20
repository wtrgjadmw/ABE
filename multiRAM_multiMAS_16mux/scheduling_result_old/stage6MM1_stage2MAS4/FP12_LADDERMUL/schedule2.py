from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 150
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=6)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 0
	d_t0_t3_t1_in += MM_in[0]

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 0
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 0
	d_t1_a1_1_in += MAS_in[1]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 0
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 0
	d_t1_t10_in += MAS_in[2]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 0
	d_t3000_in += MAS_in[3]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 0
	d_t4001_in += MAS_in[0]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=6, delay_cost=1)
	S += d_t0_t3_t1 >= 1
	d_t0_t3_t1 += MM[0]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 1
	d_t0_t3_t2_in += MAS_in[0]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 1
	d_t1_a1_0_in += MAS_in[2]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=2, delay_cost=1)
	S += d_t1_a1_1 >= 1
	d_t1_a1_1 += MAS[1]

	d_t1_t10 = S.Task('d_t1_t10', length=2, delay_cost=1)
	S += d_t1_t10 >= 1
	d_t1_t10 += MAS[2]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 1
	d_t1_t3_t2_in += MAS_in[1]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 1
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 1
	d_t2_t3_t0_in += MM_in[0]

	d_t3000 = S.Task('d_t3000', length=2, delay_cost=1)
	S += d_t3000 >= 1
	d_t3000 += MAS[3]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 1
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 1
	d_t4000_in += MAS_in[3]

	d_t4001 = S.Task('d_t4001', length=2, delay_cost=1)
	S += d_t4001 >= 1
	d_t4001 += MAS[0]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 2
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 2
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=2, delay_cost=1)
	S += d_t0_t3_t2 >= 2
	d_t0_t3_t2 += MAS[0]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=2, delay_cost=1)
	S += d_t1_a1_0 >= 2
	d_t1_a1_0 += MAS[2]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 2
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=2, delay_cost=1)
	S += d_t1_t3_t2 >= 2
	d_t1_t3_t2 += MAS[1]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=6, delay_cost=1)
	S += d_t2_t3_t0 >= 2
	d_t2_t3_t0 += MM[0]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 2
	d_t2_t3_t3_in += MAS_in[3]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 2
	d_t3001_in += MAS_in[0]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 2
	d_t3010_in += MAS_in[2]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 2
	d_t3011_in += MAS_in[1]

	d_t4000 = S.Task('d_t4000', length=2, delay_cost=1)
	S += d_t4000 >= 2
	d_t4000 += MAS[3]

	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 3
	d_t0_a1_0_in += MAS_in[1]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 3
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 3
	d_t0_t3_t3_in += MAS_in[2]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 3
	d_t1_t11_in += MAS_in[3]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 3
	d_t1_t3_t0_in += MM_in[0]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=6, delay_cost=1)
	S += d_t1_t3_t1 >= 3
	d_t1_t3_t1 += MM[0]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 3
	d_t2_t3_t2_in += MAS_in[0]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=2, delay_cost=1)
	S += d_t2_t3_t3 >= 3
	d_t2_t3_t3 += MAS[3]

	d_t3001 = S.Task('d_t3001', length=2, delay_cost=1)
	S += d_t3001 >= 3
	d_t3001 += MAS[0]

	d_t3010 = S.Task('d_t3010', length=2, delay_cost=1)
	S += d_t3010 >= 3
	d_t3010 += MAS[2]

	d_t3011 = S.Task('d_t3011', length=2, delay_cost=1)
	S += d_t3011 >= 3
	d_t3011 += MAS[1]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 3
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=2, delay_cost=1)
	S += d_t0_a1_0 >= 4
	d_t0_a1_0 += MAS[1]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 4
	d_t0_t10_in += MAS_in[3]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 4
	d_t0_t11_in += MAS_in[2]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 4
	d_t0_t3_t0_in += MM_in[0]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 4
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=2, delay_cost=1)
	S += d_t0_t3_t3 >= 4
	d_t0_t3_t3 += MAS[2]

	d_t1_t11 = S.Task('d_t1_t11', length=2, delay_cost=1)
	S += d_t1_t11 >= 4
	d_t1_t11 += MAS[3]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=6, delay_cost=1)
	S += d_t1_t3_t0 >= 4
	d_t1_t3_t0 += MM[0]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 4
	d_t2_a1_1_in += MAS_in[0]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 4
	d_t2_t11_in += MAS_in[1]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=2, delay_cost=1)
	S += d_t2_t3_t2 >= 4
	d_t2_t3_t2 += MAS[0]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 4
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 5
	d_t0_a1_1_in += MAS_in[1]

	d_t0_t10 = S.Task('d_t0_t10', length=2, delay_cost=1)
	S += d_t0_t10 >= 5
	d_t0_t10 += MAS[3]

	d_t0_t11 = S.Task('d_t0_t11', length=2, delay_cost=1)
	S += d_t0_t11 >= 5
	d_t0_t11 += MAS[2]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=6, delay_cost=1)
	S += d_t0_t3_t0 >= 5
	d_t0_t3_t0 += MM[0]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 5
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 5
	d_t1_t3_t3_in += MAS_in[0]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 5
	d_t2_a1_0_in += MAS_in[3]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=2, delay_cost=1)
	S += d_t2_a1_1 >= 5
	d_t2_a1_1 += MAS[0]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 5
	d_t2_t10_in += MAS_in[2]

	d_t2_t11 = S.Task('d_t2_t11', length=2, delay_cost=1)
	S += d_t2_t11 >= 5
	d_t2_t11 += MAS[1]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 5
	d_t2_t3_t1_in += MM_in[0]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 5
	d_t3010_mem1 += MAIN_MEM_r[1]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 6
	c_t0_t30_in += MAS_in[2]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 6
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 6
	c_t1_t1_t2_in += MAS_in[0]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=2, delay_cost=1)
	S += d_t0_a1_1 >= 6
	d_t0_a1_1 += MAS[1]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 6
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=2, delay_cost=1)
	S += d_t1_t3_t3 >= 6
	d_t1_t3_t3 += MAS[0]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=2, delay_cost=1)
	S += d_t2_a1_0 >= 6
	d_t2_a1_0 += MAS[3]

	d_t2_t10 = S.Task('d_t2_t10', length=2, delay_cost=1)
	S += d_t2_t10 >= 6
	d_t2_t10 += MAS[2]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 6
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=6, delay_cost=1)
	S += d_t2_t3_t1 >= 6
	d_t2_t3_t1 += MM[0]

	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	S += d_t5000_in >= 6
	d_t5000_in += MAS_in[3]

	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	S += d_t5011_in >= 6
	d_t5011_in += MAS_in[1]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 7
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 7
	c_t0_t20_in += MAS_in[3]

	c_t0_t30 = S.Task('c_t0_t30', length=2, delay_cost=1)
	S += c_t0_t30 >= 7
	c_t0_t30 += MAS[2]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=6, delay_cost=1)
	S += c_t1_t0_t1 >= 7
	c_t1_t0_t1 += MM[0]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 7
	c_t1_t0_t3_in += MAS_in[2]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=2, delay_cost=1)
	S += c_t1_t1_t2 >= 7
	c_t1_t1_t2 += MAS[0]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 7
	c_t1_t1_t3_in += MAS_in[1]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 7
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 7
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t5000 = S.Task('d_t5000', length=2, delay_cost=1)
	S += d_t5000 >= 7
	d_t5000 += MAS[3]

	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	S += d_t5010_in >= 7
	d_t5010_in += MAS_in[0]

	d_t5011 = S.Task('d_t5011', length=2, delay_cost=1)
	S += d_t5011 >= 7
	d_t5011 += MAS[1]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=6, delay_cost=1)
	S += c_t0_t1_t0 >= 8
	c_t0_t1_t0 += MM[0]

	c_t0_t20 = S.Task('c_t0_t20', length=2, delay_cost=1)
	S += c_t0_t20 >= 8
	c_t0_t20 += MAS[3]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 8
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=2, delay_cost=1)
	S += c_t1_t0_t3 >= 8
	c_t1_t0_t3 += MAS[2]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=2, delay_cost=1)
	S += c_t1_t1_t3 >= 8
	c_t1_t1_t3 += MAS[1]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 8
	c_t1_t21_in += MAS_in[1]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 8
	c_t1_t30_in += MAS_in[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 8
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 8
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	S += d_t4010_in >= 8
	d_t4010_in += MAS_in[3]

	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	S += d_t5001_in >= 8
	d_t5001_in += MAS_in[2]

	d_t5010 = S.Task('d_t5010', length=2, delay_cost=1)
	S += d_t5010 >= 8
	d_t5010 += MAS[0]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 9
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 9
	c_t0_t0_t2_in += MAS_in[3]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 9
	c_t0_t21_in += MAS_in[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 9
	c_t0_t31_in += MAS_in[0]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=6, delay_cost=1)
	S += c_t1_t0_t0 >= 9
	c_t1_t0_t0 += MM[0]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 9
	c_t1_t0_t2_in += MAS_in[2]

	c_t1_t21 = S.Task('c_t1_t21', length=2, delay_cost=1)
	S += c_t1_t21 >= 9
	c_t1_t21 += MAS[1]

	c_t1_t30 = S.Task('c_t1_t30', length=2, delay_cost=1)
	S += c_t1_t30 >= 9
	c_t1_t30 += MAS[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 9
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 9
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t4010 = S.Task('d_t4010', length=2, delay_cost=1)
	S += d_t4010 >= 9
	d_t4010 += MAS[3]

	d_t5001 = S.Task('d_t5001', length=2, delay_cost=1)
	S += d_t5001 >= 9
	d_t5001 += MAS[2]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 10
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=6, delay_cost=1)
	S += c_t0_t0_t1 >= 10
	c_t0_t0_t1 += MM[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=2, delay_cost=1)
	S += c_t0_t0_t2 >= 10
	c_t0_t0_t2 += MAS[3]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 10
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t21 = S.Task('c_t0_t21', length=2, delay_cost=1)
	S += c_t0_t21 >= 10
	c_t0_t21 += MAS[1]

	c_t0_t31 = S.Task('c_t0_t31', length=2, delay_cost=1)
	S += c_t0_t31 >= 10
	c_t0_t31 += MAS[0]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=2, delay_cost=1)
	S += c_t1_t0_t2 >= 10
	c_t1_t0_t2 += MAS[2]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 10
	c_t1_t20_in += MAS_in[2]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 10
	c_t1_t31_in += MAS_in[1]

	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 10
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 10
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	S += d_t4011_in >= 10
	d_t4011_in += MAS_in[3]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=6, delay_cost=1)
	S += c_t0_t0_t0 >= 11
	c_t0_t0_t0 += MM[0]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 11
	c_t0_t0_t3_in += MAS_in[3]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 11
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 11
	c_t0_t1_t2_in += MAS_in[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=2, delay_cost=1)
	S += c_t0_t1_t3 >= 11
	c_t0_t1_t3 += MAS[0]

	c_t1_t20 = S.Task('c_t1_t20', length=2, delay_cost=1)
	S += c_t1_t20 >= 11
	c_t1_t20 += MAS[2]

	c_t1_t31 = S.Task('c_t1_t31', length=2, delay_cost=1)
	S += c_t1_t31 >= 11
	c_t1_t31 += MAS[1]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 11
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 11
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t4011 = S.Task('d_t4011', length=2, delay_cost=1)
	S += d_t4011 >= 11
	d_t4011 += MAS[3]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=2, delay_cost=1)
	S += c_t0_t0_t3 >= 12
	c_t0_t0_t3 += MAS[3]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=6, delay_cost=1)
	S += c_t0_t1_t1 >= 12
	c_t0_t1_t1 += MM[0]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=2, delay_cost=1)
	S += c_t0_t1_t2 >= 12
	c_t0_t1_t2 += MAS[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 12
	c_t1_t1_t1_in += MM_in[0]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 12
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 12
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 13
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=6, delay_cost=1)
	S += c_t1_t1_t1 >= 13
	c_t1_t1_t1 += MM[0]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 13
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 13
	d_t3011_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=6, delay_cost=1)
	S += c_t1_t1_t0 >= 14
	c_t1_t1_t0 += MM[0]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 14
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 14
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 15
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 15
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 16
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 16
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 17
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 17
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 18
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 18
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 19
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 19
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 20
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 20
	d_t4001_mem0 += MAIN_MEM_r[0]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 21
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 21
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 22
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 22
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 23
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 23
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 24
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 24
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 25
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 25
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 26
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 26
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 27
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 27
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 28
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 28
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 29
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 29
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 30
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 30
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 31
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 31
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 32
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 32
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 33
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 33
	d_t5001_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 34
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 34
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 35
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 35
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 36
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 36
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 37
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 37
	d_t5010_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 38
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 38
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 39
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 39
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 40
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 40
	d_t5000_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 41
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 41
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 42
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 42
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 43
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 43
	d_t5010_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 44
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 44
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 45
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 45
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 46
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 46
	d_t5001_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 47
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 47
	d_t4011_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 48
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 48
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 49
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 49
	d_t5011_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 50
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 50
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 51
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 51
	d_t5000_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 52
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 52
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 53
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 53
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 54
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 54
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 55
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 55
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 56
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 56
	d_t4011_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 57
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 57
	d_t4010_mem1 += MAIN_MEM_r[1]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 58
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 58
	d_t5011_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 59
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 59
	d_t4010_mem0 += MAIN_MEM_r[0]


	# new tasks
	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=6, delay_cost=1)
	c_t2_t0_t0 += alt(MM)
	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	c_t2_t0_t0_in += alt(MM_in)
	S += c_t2_t0_t0_in*MM_in[0]<=c_t2_t0_t0*MM[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]
	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]
	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=6, delay_cost=1)
	c_t2_t0_t1 += alt(MM)
	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	c_t2_t0_t1_in += alt(MM_in)
	S += c_t2_t0_t1_in*MM_in[0]<=c_t2_t0_t1*MM[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]
	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]
	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=2, delay_cost=1)
	c_t2_t0_t2 += alt(MAS)
	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	c_t2_t0_t2_in += alt(MAS_in)
	S += c_t2_t0_t2_in*MAS_in[0]<=c_t2_t0_t2*MAS[0]

	S += c_t2_t0_t2_in*MAS_in[1]<=c_t2_t0_t2*MAS[1]

	S += c_t2_t0_t2_in*MAS_in[2]<=c_t2_t0_t2*MAS[2]

	S += c_t2_t0_t2_in*MAS_in[3]<=c_t2_t0_t2*MAS[3]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]
	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]
	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=2, delay_cost=1)
	c_t2_t0_t3 += alt(MAS)
	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	c_t2_t0_t3_in += alt(MAS_in)
	S += c_t2_t0_t3_in*MAS_in[0]<=c_t2_t0_t3*MAS[0]

	S += c_t2_t0_t3_in*MAS_in[1]<=c_t2_t0_t3*MAS[1]

	S += c_t2_t0_t3_in*MAS_in[2]<=c_t2_t0_t3*MAS[2]

	S += c_t2_t0_t3_in*MAS_in[3]<=c_t2_t0_t3*MAS[3]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]
	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]
	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=6, delay_cost=1)
	c_t2_t1_t0 += alt(MM)
	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	c_t2_t1_t0_in += alt(MM_in)
	S += c_t2_t1_t0_in*MM_in[0]<=c_t2_t1_t0*MM[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]
	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]
	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=6, delay_cost=1)
	c_t2_t1_t1 += alt(MM)
	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	c_t2_t1_t1_in += alt(MM_in)
	S += c_t2_t1_t1_in*MM_in[0]<=c_t2_t1_t1*MM[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]
	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]
	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=2, delay_cost=1)
	c_t2_t1_t2 += alt(MAS)
	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	c_t2_t1_t2_in += alt(MAS_in)
	S += c_t2_t1_t2_in*MAS_in[0]<=c_t2_t1_t2*MAS[0]

	S += c_t2_t1_t2_in*MAS_in[1]<=c_t2_t1_t2*MAS[1]

	S += c_t2_t1_t2_in*MAS_in[2]<=c_t2_t1_t2*MAS[2]

	S += c_t2_t1_t2_in*MAS_in[3]<=c_t2_t1_t2*MAS[3]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]
	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]
	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=2, delay_cost=1)
	c_t2_t1_t3 += alt(MAS)
	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	c_t2_t1_t3_in += alt(MAS_in)
	S += c_t2_t1_t3_in*MAS_in[0]<=c_t2_t1_t3*MAS[0]

	S += c_t2_t1_t3_in*MAS_in[1]<=c_t2_t1_t3*MAS[1]

	S += c_t2_t1_t3_in*MAS_in[2]<=c_t2_t1_t3*MAS[2]

	S += c_t2_t1_t3_in*MAS_in[3]<=c_t2_t1_t3*MAS[3]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]
	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]
	c_t2_t20 = S.Task('c_t2_t20', length=2, delay_cost=1)
	c_t2_t20 += alt(MAS)
	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	c_t2_t20_in += alt(MAS_in)
	S += c_t2_t20_in*MAS_in[0]<=c_t2_t20*MAS[0]

	S += c_t2_t20_in*MAS_in[1]<=c_t2_t20*MAS[1]

	S += c_t2_t20_in*MAS_in[2]<=c_t2_t20*MAS[2]

	S += c_t2_t20_in*MAS_in[3]<=c_t2_t20*MAS[3]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	c_t2_t20_mem0 += MAIN_MEM_r[0]
	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	c_t2_t20_mem1 += MAIN_MEM_r[1]
	c_t2_t21 = S.Task('c_t2_t21', length=2, delay_cost=1)
	c_t2_t21 += alt(MAS)
	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	c_t2_t21_in += alt(MAS_in)
	S += c_t2_t21_in*MAS_in[0]<=c_t2_t21*MAS[0]

	S += c_t2_t21_in*MAS_in[1]<=c_t2_t21*MAS[1]

	S += c_t2_t21_in*MAS_in[2]<=c_t2_t21*MAS[2]

	S += c_t2_t21_in*MAS_in[3]<=c_t2_t21*MAS[3]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	c_t2_t21_mem0 += MAIN_MEM_r[0]
	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	c_t2_t21_mem1 += MAIN_MEM_r[1]
	c_t2_t30 = S.Task('c_t2_t30', length=2, delay_cost=1)
	c_t2_t30 += alt(MAS)
	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	c_t2_t30_in += alt(MAS_in)
	S += c_t2_t30_in*MAS_in[0]<=c_t2_t30*MAS[0]

	S += c_t2_t30_in*MAS_in[1]<=c_t2_t30*MAS[1]

	S += c_t2_t30_in*MAS_in[2]<=c_t2_t30*MAS[2]

	S += c_t2_t30_in*MAS_in[3]<=c_t2_t30*MAS[3]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	c_t2_t30_mem0 += MAIN_MEM_r[0]
	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	c_t2_t30_mem1 += MAIN_MEM_r[1]
	c_t2_t31 = S.Task('c_t2_t31', length=2, delay_cost=1)
	c_t2_t31 += alt(MAS)
	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	c_t2_t31_in += alt(MAS_in)
	S += c_t2_t31_in*MAS_in[0]<=c_t2_t31*MAS[0]

	S += c_t2_t31_in*MAS_in[1]<=c_t2_t31*MAS[1]

	S += c_t2_t31_in*MAS_in[2]<=c_t2_t31*MAS[2]

	S += c_t2_t31_in*MAS_in[3]<=c_t2_t31*MAS[3]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	c_t2_t31_mem0 += MAIN_MEM_r[0]
	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	c_t2_t31_mem1 += MAIN_MEM_r[1]
	c_t3000 = S.Task('c_t3000', length=2, delay_cost=1)
	c_t3000 += alt(MAS)
	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	c_t3000_in += alt(MAS_in)
	S += c_t3000_in*MAS_in[0]<=c_t3000*MAS[0]

	S += c_t3000_in*MAS_in[1]<=c_t3000*MAS[1]

	S += c_t3000_in*MAS_in[2]<=c_t3000*MAS[2]

	S += c_t3000_in*MAS_in[3]<=c_t3000*MAS[3]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	c_t3000_mem0 += MAIN_MEM_r[0]
	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	c_t3000_mem1 += MAIN_MEM_r[1]
	c_t3001 = S.Task('c_t3001', length=2, delay_cost=1)
	c_t3001 += alt(MAS)
	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	c_t3001_in += alt(MAS_in)
	S += c_t3001_in*MAS_in[0]<=c_t3001*MAS[0]

	S += c_t3001_in*MAS_in[1]<=c_t3001*MAS[1]

	S += c_t3001_in*MAS_in[2]<=c_t3001*MAS[2]

	S += c_t3001_in*MAS_in[3]<=c_t3001*MAS[3]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	c_t3001_mem0 += MAIN_MEM_r[0]
	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	c_t3001_mem1 += MAIN_MEM_r[1]
	c_t3010 = S.Task('c_t3010', length=2, delay_cost=1)
	c_t3010 += alt(MAS)
	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	c_t3010_in += alt(MAS_in)
	S += c_t3010_in*MAS_in[0]<=c_t3010*MAS[0]

	S += c_t3010_in*MAS_in[1]<=c_t3010*MAS[1]

	S += c_t3010_in*MAS_in[2]<=c_t3010*MAS[2]

	S += c_t3010_in*MAS_in[3]<=c_t3010*MAS[3]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	c_t3010_mem0 += MAIN_MEM_r[0]
	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	c_t3010_mem1 += MAIN_MEM_r[1]
	c_t3011 = S.Task('c_t3011', length=2, delay_cost=1)
	c_t3011 += alt(MAS)
	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	c_t3011_in += alt(MAS_in)
	S += c_t3011_in*MAS_in[0]<=c_t3011*MAS[0]

	S += c_t3011_in*MAS_in[1]<=c_t3011*MAS[1]

	S += c_t3011_in*MAS_in[2]<=c_t3011*MAS[2]

	S += c_t3011_in*MAS_in[3]<=c_t3011*MAS[3]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	c_t3011_mem0 += MAIN_MEM_r[0]
	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	c_t3011_mem1 += MAIN_MEM_r[1]
	c_t3100 = S.Task('c_t3100', length=2, delay_cost=1)
	c_t3100 += alt(MAS)
	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	c_t3100_in += alt(MAS_in)
	S += c_t3100_in*MAS_in[0]<=c_t3100*MAS[0]

	S += c_t3100_in*MAS_in[1]<=c_t3100*MAS[1]

	S += c_t3100_in*MAS_in[2]<=c_t3100*MAS[2]

	S += c_t3100_in*MAS_in[3]<=c_t3100*MAS[3]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	c_t3100_mem0 += MAIN_MEM_r[0]
	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	c_t3100_mem1 += MAIN_MEM_r[1]
	c_t3101 = S.Task('c_t3101', length=2, delay_cost=1)
	c_t3101 += alt(MAS)
	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	c_t3101_in += alt(MAS_in)
	S += c_t3101_in*MAS_in[0]<=c_t3101*MAS[0]

	S += c_t3101_in*MAS_in[1]<=c_t3101*MAS[1]

	S += c_t3101_in*MAS_in[2]<=c_t3101*MAS[2]

	S += c_t3101_in*MAS_in[3]<=c_t3101*MAS[3]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	c_t3101_mem0 += MAIN_MEM_r[0]
	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	c_t3101_mem1 += MAIN_MEM_r[1]
	c_t3110 = S.Task('c_t3110', length=2, delay_cost=1)
	c_t3110 += alt(MAS)
	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	c_t3110_in += alt(MAS_in)
	S += c_t3110_in*MAS_in[0]<=c_t3110*MAS[0]

	S += c_t3110_in*MAS_in[1]<=c_t3110*MAS[1]

	S += c_t3110_in*MAS_in[2]<=c_t3110*MAS[2]

	S += c_t3110_in*MAS_in[3]<=c_t3110*MAS[3]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	c_t3110_mem0 += MAIN_MEM_r[0]
	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	c_t3110_mem1 += MAIN_MEM_r[1]
	c_t3111 = S.Task('c_t3111', length=2, delay_cost=1)
	c_t3111 += alt(MAS)
	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	c_t3111_in += alt(MAS_in)
	S += c_t3111_in*MAS_in[0]<=c_t3111*MAS[0]

	S += c_t3111_in*MAS_in[1]<=c_t3111*MAS[1]

	S += c_t3111_in*MAS_in[2]<=c_t3111*MAS[2]

	S += c_t3111_in*MAS_in[3]<=c_t3111*MAS[3]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	c_t3111_mem0 += MAIN_MEM_r[0]
	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	c_t3111_mem1 += MAIN_MEM_r[1]
	c_t4000 = S.Task('c_t4000', length=2, delay_cost=1)
	c_t4000 += alt(MAS)
	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	c_t4000_in += alt(MAS_in)
	S += c_t4000_in*MAS_in[0]<=c_t4000*MAS[0]

	S += c_t4000_in*MAS_in[1]<=c_t4000*MAS[1]

	S += c_t4000_in*MAS_in[2]<=c_t4000*MAS[2]

	S += c_t4000_in*MAS_in[3]<=c_t4000*MAS[3]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	c_t4000_mem0 += MAIN_MEM_r[0]
	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	c_t4000_mem1 += MAIN_MEM_r[1]
	c_t4001 = S.Task('c_t4001', length=2, delay_cost=1)
	c_t4001 += alt(MAS)
	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	c_t4001_in += alt(MAS_in)
	S += c_t4001_in*MAS_in[0]<=c_t4001*MAS[0]

	S += c_t4001_in*MAS_in[1]<=c_t4001*MAS[1]

	S += c_t4001_in*MAS_in[2]<=c_t4001*MAS[2]

	S += c_t4001_in*MAS_in[3]<=c_t4001*MAS[3]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	c_t4001_mem0 += MAIN_MEM_r[0]
	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	c_t4001_mem1 += MAIN_MEM_r[1]
	c_t4010 = S.Task('c_t4010', length=2, delay_cost=1)
	c_t4010 += alt(MAS)
	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	c_t4010_in += alt(MAS_in)
	S += c_t4010_in*MAS_in[0]<=c_t4010*MAS[0]

	S += c_t4010_in*MAS_in[1]<=c_t4010*MAS[1]

	S += c_t4010_in*MAS_in[2]<=c_t4010*MAS[2]

	S += c_t4010_in*MAS_in[3]<=c_t4010*MAS[3]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	c_t4010_mem0 += MAIN_MEM_r[0]
	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	c_t4010_mem1 += MAIN_MEM_r[1]
	c_t4011 = S.Task('c_t4011', length=2, delay_cost=1)
	c_t4011 += alt(MAS)
	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	c_t4011_in += alt(MAS_in)
	S += c_t4011_in*MAS_in[0]<=c_t4011*MAS[0]

	S += c_t4011_in*MAS_in[1]<=c_t4011*MAS[1]

	S += c_t4011_in*MAS_in[2]<=c_t4011*MAS[2]

	S += c_t4011_in*MAS_in[3]<=c_t4011*MAS[3]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	c_t4011_mem0 += MAIN_MEM_r[0]
	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	c_t4011_mem1 += MAIN_MEM_r[1]
	c_t4100 = S.Task('c_t4100', length=2, delay_cost=1)
	c_t4100 += alt(MAS)
	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	c_t4100_in += alt(MAS_in)
	S += c_t4100_in*MAS_in[0]<=c_t4100*MAS[0]

	S += c_t4100_in*MAS_in[1]<=c_t4100*MAS[1]

	S += c_t4100_in*MAS_in[2]<=c_t4100*MAS[2]

	S += c_t4100_in*MAS_in[3]<=c_t4100*MAS[3]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	c_t4100_mem0 += MAIN_MEM_r[0]
	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	c_t4100_mem1 += MAIN_MEM_r[1]
	c_t4101 = S.Task('c_t4101', length=2, delay_cost=1)
	c_t4101 += alt(MAS)
	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	c_t4101_in += alt(MAS_in)
	S += c_t4101_in*MAS_in[0]<=c_t4101*MAS[0]

	S += c_t4101_in*MAS_in[1]<=c_t4101*MAS[1]

	S += c_t4101_in*MAS_in[2]<=c_t4101*MAS[2]

	S += c_t4101_in*MAS_in[3]<=c_t4101*MAS[3]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	c_t4101_mem0 += MAIN_MEM_r[0]
	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	c_t4101_mem1 += MAIN_MEM_r[1]
	c_t4110 = S.Task('c_t4110', length=2, delay_cost=1)
	c_t4110 += alt(MAS)
	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	c_t4110_in += alt(MAS_in)
	S += c_t4110_in*MAS_in[0]<=c_t4110*MAS[0]

	S += c_t4110_in*MAS_in[1]<=c_t4110*MAS[1]

	S += c_t4110_in*MAS_in[2]<=c_t4110*MAS[2]

	S += c_t4110_in*MAS_in[3]<=c_t4110*MAS[3]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	c_t4110_mem0 += MAIN_MEM_r[0]
	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	c_t4110_mem1 += MAIN_MEM_r[1]
	c_t4111 = S.Task('c_t4111', length=2, delay_cost=1)
	c_t4111 += alt(MAS)
	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	c_t4111_in += alt(MAS_in)
	S += c_t4111_in*MAS_in[0]<=c_t4111*MAS[0]

	S += c_t4111_in*MAS_in[1]<=c_t4111*MAS[1]

	S += c_t4111_in*MAS_in[2]<=c_t4111*MAS[2]

	S += c_t4111_in*MAS_in[3]<=c_t4111*MAS[3]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	c_t4111_mem0 += MAIN_MEM_r[0]
	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	c_t4111_mem1 += MAIN_MEM_r[1]
	c_t5000 = S.Task('c_t5000', length=2, delay_cost=1)
	c_t5000 += alt(MAS)
	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	c_t5000_in += alt(MAS_in)
	S += c_t5000_in*MAS_in[0]<=c_t5000*MAS[0]

	S += c_t5000_in*MAS_in[1]<=c_t5000*MAS[1]

	S += c_t5000_in*MAS_in[2]<=c_t5000*MAS[2]

	S += c_t5000_in*MAS_in[3]<=c_t5000*MAS[3]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	c_t5000_mem0 += MAIN_MEM_r[0]
	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	c_t5000_mem1 += MAIN_MEM_r[1]
	c_t5001 = S.Task('c_t5001', length=2, delay_cost=1)
	c_t5001 += alt(MAS)
	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	c_t5001_in += alt(MAS_in)
	S += c_t5001_in*MAS_in[0]<=c_t5001*MAS[0]

	S += c_t5001_in*MAS_in[1]<=c_t5001*MAS[1]

	S += c_t5001_in*MAS_in[2]<=c_t5001*MAS[2]

	S += c_t5001_in*MAS_in[3]<=c_t5001*MAS[3]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	c_t5001_mem0 += MAIN_MEM_r[0]
	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	c_t5001_mem1 += MAIN_MEM_r[1]
	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage6MM1_stage2MAS4/FP12_LADDERMUL/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

