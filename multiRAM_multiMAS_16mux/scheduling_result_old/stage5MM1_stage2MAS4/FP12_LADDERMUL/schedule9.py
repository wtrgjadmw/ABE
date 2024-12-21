from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 192
	S = Scenario("schedule9", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=5)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	d_t0_a1_1_mem1 = S.Task('d_t0_a1_1_mem1', length=1, delay_cost=1)
	S += d_t0_a1_1_mem1 >= 0
	d_t0_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_a1_1_in = S.Task('d_t1_a1_1_in', length=1, delay_cost=1)
	S += d_t1_a1_1_in >= 0
	d_t1_a1_1_in += MAS_in[1]

	d_t1_t10_in = S.Task('d_t1_t10_in', length=1, delay_cost=1)
	S += d_t1_t10_in >= 0
	d_t1_t10_in += MAS_in[3]

	d_t1_t3_t0_in = S.Task('d_t1_t3_t0_in', length=1, delay_cost=1)
	S += d_t1_t3_t0_in >= 0
	d_t1_t3_t0_in += MM_in[0]

	d_t2_t11_in = S.Task('d_t2_t11_in', length=1, delay_cost=1)
	S += d_t2_t11_in >= 0
	d_t2_t11_in += MAS_in[2]

	d_t3000_mem0 = S.Task('d_t3000_mem0', length=1, delay_cost=1)
	S += d_t3000_mem0 >= 0
	d_t3000_mem0 += MAIN_MEM_r[0]

	d_t3011_in = S.Task('d_t3011_in', length=1, delay_cost=1)
	S += d_t3011_in >= 0
	d_t3011_in += MAS_in[0]

	d_t0_t3_t2_mem1 = S.Task('d_t0_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem1 >= 1
	d_t0_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t3_in = S.Task('d_t0_t3_t3_in', length=1, delay_cost=1)
	S += d_t0_t3_t3_in >= 1
	d_t0_t3_t3_in += MAS_in[1]

	d_t1_a1_1 = S.Task('d_t1_a1_1', length=2, delay_cost=1)
	S += d_t1_a1_1 >= 1
	d_t1_a1_1 += MAS[1]

	d_t1_t10 = S.Task('d_t1_t10', length=2, delay_cost=1)
	S += d_t1_t10 >= 1
	d_t1_t10 += MAS[3]

	d_t1_t3_t0 = S.Task('d_t1_t3_t0', length=5, delay_cost=1)
	S += d_t1_t3_t0 >= 1
	d_t1_t3_t0 += MM[0]

	d_t1_t3_t2_in = S.Task('d_t1_t3_t2_in', length=1, delay_cost=1)
	S += d_t1_t3_t2_in >= 1
	d_t1_t3_t2_in += MAS_in[0]

	d_t1_t3_t3_in = S.Task('d_t1_t3_t3_in', length=1, delay_cost=1)
	S += d_t1_t3_t3_in >= 1
	d_t1_t3_t3_in += MAS_in[2]

	d_t2_t11 = S.Task('d_t2_t11', length=2, delay_cost=1)
	S += d_t2_t11 >= 1
	d_t2_t11 += MAS[2]

	d_t2_t3_t1_in = S.Task('d_t2_t3_t1_in', length=1, delay_cost=1)
	S += d_t2_t3_t1_in >= 1
	d_t2_t3_t1_in += MM_in[0]

	d_t2_t3_t2_mem0 = S.Task('d_t2_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem0 >= 1
	d_t2_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t3000_in = S.Task('d_t3000_in', length=1, delay_cost=1)
	S += d_t3000_in >= 1
	d_t3000_in += MAS_in[3]

	d_t3011 = S.Task('d_t3011', length=2, delay_cost=1)
	S += d_t3011 >= 1
	d_t3011 += MAS[0]

	d_t0_a1_0_in = S.Task('d_t0_a1_0_in', length=1, delay_cost=1)
	S += d_t0_a1_0_in >= 2
	d_t0_a1_0_in += MAS_in[0]

	d_t0_a1_1_in = S.Task('d_t0_a1_1_in', length=1, delay_cost=1)
	S += d_t0_a1_1_in >= 2
	d_t0_a1_1_in += MAS_in[2]

	d_t0_t10_mem1 = S.Task('d_t0_t10_mem1', length=1, delay_cost=1)
	S += d_t0_t10_mem1 >= 2
	d_t0_t10_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t3 = S.Task('d_t0_t3_t3', length=2, delay_cost=1)
	S += d_t0_t3_t3 >= 2
	d_t0_t3_t3 += MAS[1]

	d_t1_t3_t2 = S.Task('d_t1_t3_t2', length=2, delay_cost=1)
	S += d_t1_t3_t2 >= 2
	d_t1_t3_t2 += MAS[0]

	d_t1_t3_t3 = S.Task('d_t1_t3_t3', length=2, delay_cost=1)
	S += d_t1_t3_t3 >= 2
	d_t1_t3_t3 += MAS[2]

	d_t2_t3_t0_in = S.Task('d_t2_t3_t0_in', length=1, delay_cost=1)
	S += d_t2_t3_t0_in >= 2
	d_t2_t3_t0_in += MM_in[0]

	d_t2_t3_t1 = S.Task('d_t2_t3_t1', length=5, delay_cost=1)
	S += d_t2_t3_t1 >= 2
	d_t2_t3_t1 += MM[0]

	d_t2_t3_t2_in = S.Task('d_t2_t3_t2_in', length=1, delay_cost=1)
	S += d_t2_t3_t2_in >= 2
	d_t2_t3_t2_in += MAS_in[1]

	d_t3000 = S.Task('d_t3000', length=2, delay_cost=1)
	S += d_t3000 >= 2
	d_t3000 += MAS[3]

	d_t3001_in = S.Task('d_t3001_in', length=1, delay_cost=1)
	S += d_t3001_in >= 2
	d_t3001_in += MAS_in[3]

	d_t3010_mem0 = S.Task('d_t3010_mem0', length=1, delay_cost=1)
	S += d_t3010_mem0 >= 2
	d_t3010_mem0 += MAIN_MEM_r[0]

	d_t0_a1_0 = S.Task('d_t0_a1_0', length=2, delay_cost=1)
	S += d_t0_a1_0 >= 3
	d_t0_a1_0 += MAS[0]

	d_t0_a1_1 = S.Task('d_t0_a1_1', length=2, delay_cost=1)
	S += d_t0_a1_1 >= 3
	d_t0_a1_1 += MAS[2]

	d_t0_t11_in = S.Task('d_t0_t11_in', length=1, delay_cost=1)
	S += d_t0_t11_in >= 3
	d_t0_t11_in += MAS_in[0]

	d_t0_t3_t1_in = S.Task('d_t0_t3_t1_in', length=1, delay_cost=1)
	S += d_t0_t3_t1_in >= 3
	d_t0_t3_t1_in += MM_in[0]

	d_t2_t3_t0 = S.Task('d_t2_t3_t0', length=5, delay_cost=1)
	S += d_t2_t3_t0 >= 3
	d_t2_t3_t0 += MM[0]

	d_t2_t3_t2 = S.Task('d_t2_t3_t2', length=2, delay_cost=1)
	S += d_t2_t3_t2 >= 3
	d_t2_t3_t2 += MAS[1]

	d_t2_t3_t3_in = S.Task('d_t2_t3_t3_in', length=1, delay_cost=1)
	S += d_t2_t3_t3_in >= 3
	d_t2_t3_t3_in += MAS_in[2]

	d_t3001 = S.Task('d_t3001', length=2, delay_cost=1)
	S += d_t3001 >= 3
	d_t3001 += MAS[3]

	d_t3010_in = S.Task('d_t3010_in', length=1, delay_cost=1)
	S += d_t3010_in >= 3
	d_t3010_in += MAS_in[3]

	d_t3011_mem1 = S.Task('d_t3011_mem1', length=1, delay_cost=1)
	S += d_t3011_mem1 >= 3
	d_t3011_mem1 += MAIN_MEM_r[1]

	d_t4000_in = S.Task('d_t4000_in', length=1, delay_cost=1)
	S += d_t4000_in >= 3
	d_t4000_in += MAS_in[1]

	d_t4000_mem0 = S.Task('d_t4000_mem0', length=1, delay_cost=1)
	S += d_t4000_mem0 >= 3
	d_t4000_mem0 += MAIN_MEM_r[0]

	d_t0_t11 = S.Task('d_t0_t11', length=2, delay_cost=1)
	S += d_t0_t11 >= 4
	d_t0_t11 += MAS[0]

	d_t0_t3_t0_in = S.Task('d_t0_t3_t0_in', length=1, delay_cost=1)
	S += d_t0_t3_t0_in >= 4
	d_t0_t3_t0_in += MM_in[0]

	d_t0_t3_t1 = S.Task('d_t0_t3_t1', length=5, delay_cost=1)
	S += d_t0_t3_t1 >= 4
	d_t0_t3_t1 += MM[0]

	d_t0_t3_t1_mem1 = S.Task('d_t0_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem1 >= 4
	d_t0_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t0_t3_t2_in = S.Task('d_t0_t3_t2_in', length=1, delay_cost=1)
	S += d_t0_t3_t2_in >= 4
	d_t0_t3_t2_in += MAS_in[0]

	d_t1_a1_0_in = S.Task('d_t1_a1_0_in', length=1, delay_cost=1)
	S += d_t1_a1_0_in >= 4
	d_t1_a1_0_in += MAS_in[2]

	d_t1_t3_t3_mem0 = S.Task('d_t1_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem0 >= 4
	d_t1_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_in = S.Task('d_t2_a1_1_in', length=1, delay_cost=1)
	S += d_t2_a1_1_in >= 4
	d_t2_a1_1_in += MAS_in[1]

	d_t2_t10_in = S.Task('d_t2_t10_in', length=1, delay_cost=1)
	S += d_t2_t10_in >= 4
	d_t2_t10_in += MAS_in[3]

	d_t2_t3_t3 = S.Task('d_t2_t3_t3', length=2, delay_cost=1)
	S += d_t2_t3_t3 >= 4
	d_t2_t3_t3 += MAS[2]

	d_t3010 = S.Task('d_t3010', length=2, delay_cost=1)
	S += d_t3010 >= 4
	d_t3010 += MAS[3]

	d_t4000 = S.Task('d_t4000', length=2, delay_cost=1)
	S += d_t4000 >= 4
	d_t4000 += MAS[1]

	d_t0_t10_in = S.Task('d_t0_t10_in', length=1, delay_cost=1)
	S += d_t0_t10_in >= 5
	d_t0_t10_in += MAS_in[1]

	d_t0_t11_mem0 = S.Task('d_t0_t11_mem0', length=1, delay_cost=1)
	S += d_t0_t11_mem0 >= 5
	d_t0_t11_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0 = S.Task('d_t0_t3_t0', length=5, delay_cost=1)
	S += d_t0_t3_t0 >= 5
	d_t0_t3_t0 += MM[0]

	d_t0_t3_t2 = S.Task('d_t0_t3_t2', length=2, delay_cost=1)
	S += d_t0_t3_t2 >= 5
	d_t0_t3_t2 += MAS[0]

	d_t1_a1_0 = S.Task('d_t1_a1_0', length=2, delay_cost=1)
	S += d_t1_a1_0 >= 5
	d_t1_a1_0 += MAS[2]

	d_t1_t11_in = S.Task('d_t1_t11_in', length=1, delay_cost=1)
	S += d_t1_t11_in >= 5
	d_t1_t11_in += MAS_in[2]

	d_t1_t3_t1_in = S.Task('d_t1_t3_t1_in', length=1, delay_cost=1)
	S += d_t1_t3_t1_in >= 5
	d_t1_t3_t1_in += MM_in[0]

	d_t1_t3_t2_mem1 = S.Task('d_t1_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem1 >= 5
	d_t1_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_a1_0_in = S.Task('d_t2_a1_0_in', length=1, delay_cost=1)
	S += d_t2_a1_0_in >= 5
	d_t2_a1_0_in += MAS_in[0]

	d_t2_a1_1 = S.Task('d_t2_a1_1', length=2, delay_cost=1)
	S += d_t2_a1_1 >= 5
	d_t2_a1_1 += MAS[1]

	d_t2_t10 = S.Task('d_t2_t10', length=2, delay_cost=1)
	S += d_t2_t10 >= 5
	d_t2_t10 += MAS[3]

	d_t4001_in = S.Task('d_t4001_in', length=1, delay_cost=1)
	S += d_t4001_in >= 5
	d_t4001_in += MAS_in[3]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 6
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 6
	c_t0_t30_in += MAS_in[1]

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 6
	c_t0_t31_in += MAS_in[3]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 6
	c_t1_t30_in += MAS_in[0]

	d_t0_t10 = S.Task('d_t0_t10', length=2, delay_cost=1)
	S += d_t0_t10 >= 6
	d_t0_t10 += MAS[1]

	d_t0_t3_t3_mem0 = S.Task('d_t0_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem0 >= 6
	d_t0_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t1_t11 = S.Task('d_t1_t11', length=2, delay_cost=1)
	S += d_t1_t11 >= 6
	d_t1_t11 += MAS[2]

	d_t1_t11_mem1 = S.Task('d_t1_t11_mem1', length=1, delay_cost=1)
	S += d_t1_t11_mem1 >= 6
	d_t1_t11_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t1 = S.Task('d_t1_t3_t1', length=5, delay_cost=1)
	S += d_t1_t3_t1 >= 6
	d_t1_t3_t1 += MM[0]

	d_t2_a1_0 = S.Task('d_t2_a1_0', length=2, delay_cost=1)
	S += d_t2_a1_0 >= 6
	d_t2_a1_0 += MAS[0]

	d_t4001 = S.Task('d_t4001', length=2, delay_cost=1)
	S += d_t4001 >= 6
	d_t4001 += MAS[3]

	d_t5010_in = S.Task('d_t5010_in', length=1, delay_cost=1)
	S += d_t5010_in >= 6
	d_t5010_in += MAS_in[2]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=5, delay_cost=1)
	S += c_t0_t1_t0 >= 7
	c_t0_t1_t0 += MM[0]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 7
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 7
	c_t0_t21_in += MAS_in[0]

	c_t0_t30 = S.Task('c_t0_t30', length=2, delay_cost=1)
	S += c_t0_t30 >= 7
	c_t0_t30 += MAS[1]

	c_t0_t31 = S.Task('c_t0_t31', length=2, delay_cost=1)
	S += c_t0_t31 >= 7
	c_t0_t31 += MAS[3]

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 7
	c_t1_t0_t3_in += MAS_in[1]

	c_t1_t30 = S.Task('c_t1_t30', length=2, delay_cost=1)
	S += c_t1_t30 >= 7
	c_t1_t30 += MAS[0]

	d_t0_t11_mem1 = S.Task('d_t0_t11_mem1', length=1, delay_cost=1)
	S += d_t0_t11_mem1 >= 7
	d_t0_t11_mem1 += MAIN_MEM_r[1]

	d_t2_t10_mem0 = S.Task('d_t2_t10_mem0', length=1, delay_cost=1)
	S += d_t2_t10_mem0 >= 7
	d_t2_t10_mem0 += MAIN_MEM_r[0]

	d_t4010_in = S.Task('d_t4010_in', length=1, delay_cost=1)
	S += d_t4010_in >= 7
	d_t4010_in += MAS_in[2]

	d_t4011_in = S.Task('d_t4011_in', length=1, delay_cost=1)
	S += d_t4011_in >= 7
	d_t4011_in += MAS_in[3]

	d_t5010 = S.Task('d_t5010', length=2, delay_cost=1)
	S += d_t5010 >= 7
	d_t5010 += MAS[2]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 8
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=5, delay_cost=1)
	S += c_t0_t1_t1 >= 8
	c_t0_t1_t1 += MM[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 8
	c_t0_t1_t2_in += MAS_in[2]

	c_t0_t21 = S.Task('c_t0_t21', length=2, delay_cost=1)
	S += c_t0_t21 >= 8
	c_t0_t21 += MAS[0]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=2, delay_cost=1)
	S += c_t1_t0_t3 >= 8
	c_t1_t0_t3 += MAS[1]

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 8
	c_t1_t31_in += MAS_in[3]

	d_t1_t3_t0_mem0 = S.Task('d_t1_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem0 >= 8
	d_t1_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t2_t3_t0_mem1 = S.Task('d_t2_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem1 >= 8
	d_t2_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t4010 = S.Task('d_t4010', length=2, delay_cost=1)
	S += d_t4010 >= 8
	d_t4010 += MAS[2]

	d_t4011 = S.Task('d_t4011', length=2, delay_cost=1)
	S += d_t4011 >= 8
	d_t4011 += MAS[3]

	d_t5001_in = S.Task('d_t5001_in', length=1, delay_cost=1)
	S += d_t5001_in >= 8
	d_t5001_in += MAS_in[1]

	d_t5011_in = S.Task('d_t5011_in', length=1, delay_cost=1)
	S += d_t5011_in >= 8
	d_t5011_in += MAS_in[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=5, delay_cost=1)
	S += c_t0_t0_t0 >= 9
	c_t0_t0_t0 += MM[0]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 9
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 9
	c_t0_t0_t2_in += MAS_in[2]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=2, delay_cost=1)
	S += c_t0_t1_t2 >= 9
	c_t0_t1_t2 += MAS[2]

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 9
	c_t1_t0_t2_in += MAS_in[1]

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 9
	c_t1_t1_t2_in += MAS_in[0]

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 9
	c_t1_t1_t3_in += MAS_in[3]

	c_t1_t31 = S.Task('c_t1_t31', length=2, delay_cost=1)
	S += c_t1_t31 >= 9
	c_t1_t31 += MAS[3]

	d_t2_t11_mem0 = S.Task('d_t2_t11_mem0', length=1, delay_cost=1)
	S += d_t2_t11_mem0 >= 9
	d_t2_t11_mem0 += MAIN_MEM_r[0]

	d_t4000_mem1 = S.Task('d_t4000_mem1', length=1, delay_cost=1)
	S += d_t4000_mem1 >= 9
	d_t4000_mem1 += MAIN_MEM_r[1]

	d_t5001 = S.Task('d_t5001', length=2, delay_cost=1)
	S += d_t5001 >= 9
	d_t5001 += MAS[1]

	d_t5011 = S.Task('d_t5011', length=2, delay_cost=1)
	S += d_t5011 >= 9
	d_t5011 += MAS[0]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=5, delay_cost=1)
	S += c_t0_t0_t1 >= 10
	c_t0_t0_t1 += MM[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=2, delay_cost=1)
	S += c_t0_t0_t2 >= 10
	c_t0_t0_t2 += MAS[2]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 10
	c_t0_t1_t3_in += MAS_in[1]

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 10
	c_t0_t20_in += MAS_in[3]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=2, delay_cost=1)
	S += c_t1_t0_t2 >= 10
	c_t1_t0_t2 += MAS[1]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 10
	c_t1_t1_t0_in += MM_in[0]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=2, delay_cost=1)
	S += c_t1_t1_t2 >= 10
	c_t1_t1_t2 += MAS[0]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=2, delay_cost=1)
	S += c_t1_t1_t3 >= 10
	c_t1_t1_t3 += MAS[3]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 10
	c_t1_t21_in += MAS_in[2]

	d_t1_a1_1_mem1 = S.Task('d_t1_a1_1_mem1', length=1, delay_cost=1)
	S += d_t1_a1_1_mem1 >= 10
	d_t1_a1_1_mem1 += MAIN_MEM_r[1]

	d_t1_t3_t2_mem0 = S.Task('d_t1_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t2_mem0 >= 10
	d_t1_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t5000_in = S.Task('d_t5000_in', length=1, delay_cost=1)
	S += d_t5000_in >= 10
	d_t5000_in += MAS_in[0]

	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 11
	c_t0_t0_t3_in += MAS_in[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=2, delay_cost=1)
	S += c_t0_t1_t3 >= 11
	c_t0_t1_t3 += MAS[1]

	c_t0_t20 = S.Task('c_t0_t20', length=2, delay_cost=1)
	S += c_t0_t20 >= 11
	c_t0_t20 += MAS[3]

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 11
	c_t1_t0_t1_in += MM_in[0]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=5, delay_cost=1)
	S += c_t1_t1_t0 >= 11
	c_t1_t1_t0 += MM[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 11
	c_t1_t20_in += MAS_in[2]

	c_t1_t21 = S.Task('c_t1_t21', length=2, delay_cost=1)
	S += c_t1_t21 >= 11
	c_t1_t21 += MAS[2]

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	S += c_t2_t20_in >= 11
	c_t2_t20_in += MAS_in[1]

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	S += c_t4011_in >= 11
	c_t4011_in += MAS_in[3]

	d_t0_t3_t3_mem1 = S.Task('d_t0_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t3_mem1 >= 11
	d_t0_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3001_mem0 = S.Task('d_t3001_mem0', length=1, delay_cost=1)
	S += d_t3001_mem0 >= 11
	d_t3001_mem0 += MAIN_MEM_r[0]

	d_t5000 = S.Task('d_t5000', length=2, delay_cost=1)
	S += d_t5000 >= 11
	d_t5000 += MAS[0]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=2, delay_cost=1)
	S += c_t0_t0_t3 >= 12
	c_t0_t0_t3 += MAS[0]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 12
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=5, delay_cost=1)
	S += c_t1_t0_t1 >= 12
	c_t1_t0_t1 += MM[0]

	c_t1_t20 = S.Task('c_t1_t20', length=2, delay_cost=1)
	S += c_t1_t20 >= 12
	c_t1_t20 += MAS[2]

	c_t2_t20 = S.Task('c_t2_t20', length=2, delay_cost=1)
	S += c_t2_t20 >= 12
	c_t2_t20 += MAS[1]

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	S += c_t2_t31_in >= 12
	c_t2_t31_in += MAS_in[1]

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	S += c_t3011_in >= 12
	c_t3011_in += MAS_in[0]

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	S += c_t3111_in >= 12
	c_t3111_in += MAS_in[3]

	c_t4011 = S.Task('c_t4011', length=2, delay_cost=1)
	S += c_t4011 >= 12
	c_t4011 += MAS[3]

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	S += c_t4101_in >= 12
	c_t4101_in += MAS_in[2]

	d_t1_a1_0_mem0 = S.Task('d_t1_a1_0_mem0', length=1, delay_cost=1)
	S += d_t1_a1_0_mem0 >= 12
	d_t1_a1_0_mem0 += MAIN_MEM_r[0]

	d_t1_a1_0_mem1 = S.Task('d_t1_a1_0_mem1', length=1, delay_cost=1)
	S += d_t1_a1_0_mem1 >= 12
	d_t1_a1_0_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=5, delay_cost=1)
	S += c_t1_t0_t0 >= 13
	c_t1_t0_t0 += MM[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 13
	c_t1_t1_t1_in += MM_in[0]

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 13
	c_t2_t0_t2_in += MAS_in[2]

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	S += c_t2_t21_in >= 13
	c_t2_t21_in += MAS_in[1]

	c_t2_t31 = S.Task('c_t2_t31', length=2, delay_cost=1)
	S += c_t2_t31 >= 13
	c_t2_t31 += MAS[1]

	c_t3011 = S.Task('c_t3011', length=2, delay_cost=1)
	S += c_t3011 >= 13
	c_t3011 += MAS[0]

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	S += c_t3110_in >= 13
	c_t3110_in += MAS_in[3]

	c_t3111 = S.Task('c_t3111', length=2, delay_cost=1)
	S += c_t3111 >= 13
	c_t3111 += MAS[3]

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	S += c_t4001_in >= 13
	c_t4001_in += MAS_in[0]

	c_t4101 = S.Task('c_t4101', length=2, delay_cost=1)
	S += c_t4101 >= 13
	c_t4101 += MAS[2]

	d_t1_t10_mem1 = S.Task('d_t1_t10_mem1', length=1, delay_cost=1)
	S += d_t1_t10_mem1 >= 13
	d_t1_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t1_mem0 = S.Task('d_t2_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem0 >= 13
	d_t2_t3_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=5, delay_cost=1)
	S += c_t1_t1_t1 >= 14
	c_t1_t1_t1 += MM[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=2, delay_cost=1)
	S += c_t2_t0_t2 >= 14
	c_t2_t0_t2 += MAS[2]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 14
	c_t2_t0_t3_in += MAS_in[1]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 14
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	S += c_t2_t1_t2_in >= 14
	c_t2_t1_t2_in += MAS_in[0]

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	S += c_t2_t1_t3_in >= 14
	c_t2_t1_t3_in += MAS_in[3]

	c_t2_t21 = S.Task('c_t2_t21', length=2, delay_cost=1)
	S += c_t2_t21 >= 14
	c_t2_t21 += MAS[1]

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	S += c_t3101_in >= 14
	c_t3101_in += MAS_in[2]

	c_t3110 = S.Task('c_t3110', length=2, delay_cost=1)
	S += c_t3110 >= 14
	c_t3110 += MAS[3]

	c_t4001 = S.Task('c_t4001', length=2, delay_cost=1)
	S += c_t4001 >= 14
	c_t4001 += MAS[0]

	d_t0_a1_0_mem1 = S.Task('d_t0_a1_0_mem1', length=1, delay_cost=1)
	S += d_t0_a1_0_mem1 >= 14
	d_t0_a1_0_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t0_mem0 = S.Task('d_t2_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t0_mem0 >= 14
	d_t2_t3_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 15
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=2, delay_cost=1)
	S += c_t2_t0_t3 >= 15
	c_t2_t0_t3 += MAS[1]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=5, delay_cost=1)
	S += c_t2_t1_t0 >= 15
	c_t2_t1_t0 += MM[0]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=2, delay_cost=1)
	S += c_t2_t1_t2 >= 15
	c_t2_t1_t2 += MAS[0]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=2, delay_cost=1)
	S += c_t2_t1_t3 >= 15
	c_t2_t1_t3 += MAS[3]

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	S += c_t3000_in >= 15
	c_t3000_in += MAS_in[0]

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	S += c_t3001_in >= 15
	c_t3001_in += MAS_in[3]

	c_t3101 = S.Task('c_t3101', length=2, delay_cost=1)
	S += c_t3101 >= 15
	c_t3101 += MAS[2]

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	S += c_t4000_in >= 15
	c_t4000_in += MAS_in[1]

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	S += c_t4111_in >= 15
	c_t4111_in += MAS_in[2]

	d_t0_a1_1_mem0 = S.Task('d_t0_a1_1_mem0', length=1, delay_cost=1)
	S += d_t0_a1_1_mem0 >= 15
	d_t0_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_a1_0_mem1 = S.Task('d_t2_a1_0_mem1', length=1, delay_cost=1)
	S += d_t2_a1_0_mem1 >= 15
	d_t2_a1_0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=5, delay_cost=1)
	S += c_t2_t0_t0 >= 16
	c_t2_t0_t0 += MM[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 16
	c_t2_t1_t1_in += MM_in[0]

	c_t3000 = S.Task('c_t3000', length=2, delay_cost=1)
	S += c_t3000 >= 16
	c_t3000 += MAS[0]

	c_t3001 = S.Task('c_t3001', length=2, delay_cost=1)
	S += c_t3001 >= 16
	c_t3001 += MAS[3]

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	S += c_t3010_in >= 16
	c_t3010_in += MAS_in[2]

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	S += c_t3100_in >= 16
	c_t3100_in += MAS_in[0]

	c_t4000 = S.Task('c_t4000', length=2, delay_cost=1)
	S += c_t4000 >= 16
	c_t4000 += MAS[1]

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	S += c_t4010_in >= 16
	c_t4010_in += MAS_in[1]

	c_t4111 = S.Task('c_t4111', length=2, delay_cost=1)
	S += c_t4111 >= 16
	c_t4111 += MAS[2]

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	S += c_t5001_in >= 16
	c_t5001_in += MAS_in[3]

	d_t1_t3_t1_mem1 = S.Task('d_t1_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem1 >= 16
	d_t1_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t2_a1_0_mem0 = S.Task('d_t2_a1_0_mem0', length=1, delay_cost=1)
	S += d_t2_a1_0_mem0 >= 16
	d_t2_a1_0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 17
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=5, delay_cost=1)
	S += c_t2_t1_t1 >= 17
	c_t2_t1_t1 += MM[0]

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	S += c_t2_t30_in >= 17
	c_t2_t30_in += MAS_in[2]

	c_t3010 = S.Task('c_t3010', length=2, delay_cost=1)
	S += c_t3010 >= 17
	c_t3010 += MAS[2]

	c_t3100 = S.Task('c_t3100', length=2, delay_cost=1)
	S += c_t3100 >= 17
	c_t3100 += MAS[0]

	c_t4010 = S.Task('c_t4010', length=2, delay_cost=1)
	S += c_t4010 >= 17
	c_t4010 += MAS[1]

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	S += c_t4100_in >= 17
	c_t4100_in += MAS_in[1]

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	S += c_t4110_in >= 17
	c_t4110_in += MAS_in[0]

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	S += c_t5000_in >= 17
	c_t5000_in += MAS_in[3]

	c_t5001 = S.Task('c_t5001', length=2, delay_cost=1)
	S += c_t5001 >= 17
	c_t5001 += MAS[3]

	d_t0_t3_t0_mem0 = S.Task('d_t0_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem0 >= 17
	d_t0_t3_t0_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t0_mem1 = S.Task('d_t0_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t0_mem1 >= 17
	d_t0_t3_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=5, delay_cost=1)
	S += c_t2_t0_t1 >= 18
	c_t2_t0_t1 += MM[0]

	c_t2_t30 = S.Task('c_t2_t30', length=2, delay_cost=1)
	S += c_t2_t30 >= 18
	c_t2_t30 += MAS[2]

	c_t4100 = S.Task('c_t4100', length=2, delay_cost=1)
	S += c_t4100 >= 18
	c_t4100 += MAS[1]

	c_t4110 = S.Task('c_t4110', length=2, delay_cost=1)
	S += c_t4110 >= 18
	c_t4110 += MAS[0]

	c_t5000 = S.Task('c_t5000', length=2, delay_cost=1)
	S += c_t5000 >= 18
	c_t5000 += MAS[3]

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

	d_t0_t3_t2_mem0 = S.Task('d_t0_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t2_mem0 >= 18
	d_t0_t3_t2_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t3_mem1 = S.Task('d_t1_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t3_mem1 >= 18
	d_t1_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3_t3_t1_in = S.Task('d_t3_t3_t1_in', length=1, delay_cost=1)
	S += d_t3_t3_t1_in >= 18
	d_t3_t3_t1_in += MM_in[0]

	d_t3_t3_t1_mem0 = S.Task('d_t3_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem0 >= 18
	d_t3_t3_t1_mem0 += MAS_MEM[6]

	d_t3_t3_t1_mem1 = S.Task('d_t3_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t1_mem1 >= 18
	d_t3_t3_t1_mem1 += MAS_MEM[1]

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	S += c_t5010_in >= 19
	c_t5010_in += MAS_in[2]

	c_t5011 = S.Task('c_t5011', length=2, delay_cost=1)
	S += c_t5011 >= 19
	c_t5011 += MAS[1]

	c_t5100 = S.Task('c_t5100', length=2, delay_cost=1)
	S += c_t5100 >= 19
	c_t5100 += MAS[3]

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	S += c_t5101_in >= 19
	c_t5101_in += MAS_in[0]

	c_t5110 = S.Task('c_t5110', length=2, delay_cost=1)
	S += c_t5110 >= 19
	c_t5110 += MAS[2]

	c_t5111 = S.Task('c_t5111', length=2, delay_cost=1)
	S += c_t5111 >= 19
	c_t5111 += MAS[0]

	d_t1_t3_t4_in = S.Task('d_t1_t3_t4_in', length=1, delay_cost=1)
	S += d_t1_t3_t4_in >= 19
	d_t1_t3_t4_in += MM_in[0]

	d_t1_t3_t4_mem0 = S.Task('d_t1_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem0 >= 19
	d_t1_t3_t4_mem0 += MAS_MEM[0]

	d_t1_t3_t4_mem1 = S.Task('d_t1_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t4_mem1 >= 19
	d_t1_t3_t4_mem1 += MAS_MEM[5]

	d_t1_t3_t5_in = S.Task('d_t1_t3_t5_in', length=1, delay_cost=1)
	S += d_t1_t3_t5_in >= 19
	d_t1_t3_t5_in += MAS_in[3]

	d_t1_t3_t5_mem0 = S.Task('d_t1_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem0 >= 19
	d_t1_t3_t5_mem0 += MM_MEM[0]

	d_t1_t3_t5_mem1 = S.Task('d_t1_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t5_mem1 >= 19
	d_t1_t3_t5_mem1 += MM_MEM[1]

	d_t3010_mem1 = S.Task('d_t3010_mem1', length=1, delay_cost=1)
	S += d_t3010_mem1 >= 19
	d_t3010_mem1 += MAIN_MEM_r[1]

	d_t3_a1_0_in = S.Task('d_t3_a1_0_in', length=1, delay_cost=1)
	S += d_t3_a1_0_in >= 19
	d_t3_a1_0_in += MAS_in[1]

	d_t3_a1_0_mem0 = S.Task('d_t3_a1_0_mem0', length=1, delay_cost=1)
	S += d_t3_a1_0_mem0 >= 19
	d_t3_a1_0_mem0 += MAS_MEM[6]

	d_t3_a1_0_mem1 = S.Task('d_t3_a1_0_mem1', length=1, delay_cost=1)
	S += d_t3_a1_0_mem1 >= 19
	d_t3_a1_0_mem1 += MAS_MEM[1]

	d_t3_t3_t1 = S.Task('d_t3_t3_t1', length=5, delay_cost=1)
	S += d_t3_t3_t1 >= 19
	d_t3_t3_t1 += MM[0]

	d_t4001_mem0 = S.Task('d_t4001_mem0', length=1, delay_cost=1)
	S += d_t4001_mem0 >= 19
	d_t4001_mem0 += MAIN_MEM_r[0]

	c_t5010 = S.Task('c_t5010', length=2, delay_cost=1)
	S += c_t5010 >= 20
	c_t5010 += MAS[2]

	c_t5101 = S.Task('c_t5101', length=2, delay_cost=1)
	S += c_t5101 >= 20
	c_t5101 += MAS[0]

	d_t0_t3_t4_in = S.Task('d_t0_t3_t4_in', length=1, delay_cost=1)
	S += d_t0_t3_t4_in >= 20
	d_t0_t3_t4_in += MM_in[0]

	d_t0_t3_t4_mem0 = S.Task('d_t0_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem0 >= 20
	d_t0_t3_t4_mem0 += MAS_MEM[0]

	d_t0_t3_t4_mem1 = S.Task('d_t0_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t4_mem1 >= 20
	d_t0_t3_t4_mem1 += MAS_MEM[3]

	d_t1_t30_in = S.Task('d_t1_t30_in', length=1, delay_cost=1)
	S += d_t1_t30_in >= 20
	d_t1_t30_in += MAS_in[1]

	d_t1_t30_mem0 = S.Task('d_t1_t30_mem0', length=1, delay_cost=1)
	S += d_t1_t30_mem0 >= 20
	d_t1_t30_mem0 += MM_MEM[0]

	d_t1_t30_mem1 = S.Task('d_t1_t30_mem1', length=1, delay_cost=1)
	S += d_t1_t30_mem1 >= 20
	d_t1_t30_mem1 += MM_MEM[1]

	d_t1_t3_t4 = S.Task('d_t1_t3_t4', length=5, delay_cost=1)
	S += d_t1_t3_t4 >= 20
	d_t1_t3_t4 += MM[0]

	d_t1_t3_t5 = S.Task('d_t1_t3_t5', length=2, delay_cost=1)
	S += d_t1_t3_t5 >= 20
	d_t1_t3_t5 += MAS[3]

	d_t2_t3_t3_mem0 = S.Task('d_t2_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem0 >= 20
	d_t2_t3_t3_mem0 += MAIN_MEM_r[0]

	d_t3000_mem1 = S.Task('d_t3000_mem1', length=1, delay_cost=1)
	S += d_t3000_mem1 >= 20
	d_t3000_mem1 += MAIN_MEM_r[1]

	d_t3_a1_0 = S.Task('d_t3_a1_0', length=2, delay_cost=1)
	S += d_t3_a1_0 >= 20
	d_t3_a1_0 += MAS[1]

	d_t3_t11_in = S.Task('d_t3_t11_in', length=1, delay_cost=1)
	S += d_t3_t11_in >= 20
	d_t3_t11_in += MAS_in[2]

	d_t3_t11_mem0 = S.Task('d_t3_t11_mem0', length=1, delay_cost=1)
	S += d_t3_t11_mem0 >= 20
	d_t3_t11_mem0 += MAS_MEM[6]

	d_t3_t11_mem1 = S.Task('d_t3_t11_mem1', length=1, delay_cost=1)
	S += d_t3_t11_mem1 >= 20
	d_t3_t11_mem1 += MAS_MEM[1]

	d_t4_t10_in = S.Task('d_t4_t10_in', length=1, delay_cost=1)
	S += d_t4_t10_in >= 20
	d_t4_t10_in += MAS_in[3]

	d_t4_t10_mem0 = S.Task('d_t4_t10_mem0', length=1, delay_cost=1)
	S += d_t4_t10_mem0 >= 20
	d_t4_t10_mem0 += MAS_MEM[2]

	d_t4_t10_mem1 = S.Task('d_t4_t10_mem1', length=1, delay_cost=1)
	S += d_t4_t10_mem1 >= 20
	d_t4_t10_mem1 += MAS_MEM[5]

	d_t4_t3_t3_in = S.Task('d_t4_t3_t3_in', length=1, delay_cost=1)
	S += d_t4_t3_t3_in >= 20
	d_t4_t3_t3_in += MAS_in[0]

	d_t4_t3_t3_mem0 = S.Task('d_t4_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem0 >= 20
	d_t4_t3_t3_mem0 += MAS_MEM[4]

	d_t4_t3_t3_mem1 = S.Task('d_t4_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t3_mem1 >= 20
	d_t4_t3_t3_mem1 += MAS_MEM[7]

	d_t0_t10_mem0 = S.Task('d_t0_t10_mem0', length=1, delay_cost=1)
	S += d_t0_t10_mem0 >= 21
	d_t0_t10_mem0 += MAIN_MEM_r[0]

	d_t0_t3_t4 = S.Task('d_t0_t3_t4', length=5, delay_cost=1)
	S += d_t0_t3_t4 >= 21
	d_t0_t3_t4 += MM[0]

	d_t1_t2_t3_in = S.Task('d_t1_t2_t3_in', length=1, delay_cost=1)
	S += d_t1_t2_t3_in >= 21
	d_t1_t2_t3_in += MAS_in[0]

	d_t1_t2_t3_mem0 = S.Task('d_t1_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem0 >= 21
	d_t1_t2_t3_mem0 += MAS_MEM[6]

	d_t1_t2_t3_mem1 = S.Task('d_t1_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t3_mem1 >= 21
	d_t1_t2_t3_mem1 += MAS_MEM[5]

	d_t1_t30 = S.Task('d_t1_t30', length=2, delay_cost=1)
	S += d_t1_t30 >= 21
	d_t1_t30 += MAS[1]

	d_t2_t11_mem1 = S.Task('d_t2_t11_mem1', length=1, delay_cost=1)
	S += d_t2_t11_mem1 >= 21
	d_t2_t11_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t5_in = S.Task('d_t2_t3_t5_in', length=1, delay_cost=1)
	S += d_t2_t3_t5_in >= 21
	d_t2_t3_t5_in += MAS_in[1]

	d_t2_t3_t5_mem0 = S.Task('d_t2_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem0 >= 21
	d_t2_t3_t5_mem0 += MM_MEM[0]

	d_t2_t3_t5_mem1 = S.Task('d_t2_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t5_mem1 >= 21
	d_t2_t3_t5_mem1 += MM_MEM[1]

	d_t3_t11 = S.Task('d_t3_t11', length=2, delay_cost=1)
	S += d_t3_t11 >= 21
	d_t3_t11 += MAS[2]

	d_t4_a1_0_in = S.Task('d_t4_a1_0_in', length=1, delay_cost=1)
	S += d_t4_a1_0_in >= 21
	d_t4_a1_0_in += MAS_in[3]

	d_t4_a1_0_mem0 = S.Task('d_t4_a1_0_mem0', length=1, delay_cost=1)
	S += d_t4_a1_0_mem0 >= 21
	d_t4_a1_0_mem0 += MAS_MEM[4]

	d_t4_a1_0_mem1 = S.Task('d_t4_a1_0_mem1', length=1, delay_cost=1)
	S += d_t4_a1_0_mem1 >= 21
	d_t4_a1_0_mem1 += MAS_MEM[7]

	d_t4_t10 = S.Task('d_t4_t10', length=2, delay_cost=1)
	S += d_t4_t10 >= 21
	d_t4_t10 += MAS[3]

	d_t4_t3_t3 = S.Task('d_t4_t3_t3', length=2, delay_cost=1)
	S += d_t4_t3_t3 >= 21
	d_t4_t3_t3 += MAS[0]

	d_t5_t3_t1_in = S.Task('d_t5_t3_t1_in', length=1, delay_cost=1)
	S += d_t5_t3_t1_in >= 21
	d_t5_t3_t1_in += MM_in[0]

	d_t5_t3_t1_mem0 = S.Task('d_t5_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem0 >= 21
	d_t5_t3_t1_mem0 += MAS_MEM[2]

	d_t5_t3_t1_mem1 = S.Task('d_t5_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t1_mem1 >= 21
	d_t5_t3_t1_mem1 += MAS_MEM[1]

	d_t5_t3_t2_in = S.Task('d_t5_t3_t2_in', length=1, delay_cost=1)
	S += d_t5_t3_t2_in >= 21
	d_t5_t3_t2_in += MAS_in[2]

	d_t5_t3_t2_mem0 = S.Task('d_t5_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem0 >= 21
	d_t5_t3_t2_mem0 += MAS_MEM[0]

	d_t5_t3_t2_mem1 = S.Task('d_t5_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t2_mem1 >= 21
	d_t5_t3_t2_mem1 += MAS_MEM[3]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 22
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 22
	c_t0_t4_t0_mem0 += MAS_MEM[6]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 22
	c_t0_t4_t0_mem1 += MAS_MEM[3]

	d_t0_t3_t1_mem0 = S.Task('d_t0_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t1_mem0 >= 22
	d_t0_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t1_t2_t3 = S.Task('d_t1_t2_t3', length=2, delay_cost=1)
	S += d_t1_t2_t3 >= 22
	d_t1_t2_t3 += MAS[0]

	d_t2_t10_mem1 = S.Task('d_t2_t10_mem1', length=1, delay_cost=1)
	S += d_t2_t10_mem1 >= 22
	d_t2_t10_mem1 += MAIN_MEM_r[1]

	d_t2_t30_in = S.Task('d_t2_t30_in', length=1, delay_cost=1)
	S += d_t2_t30_in >= 22
	d_t2_t30_in += MAS_in[1]

	d_t2_t30_mem0 = S.Task('d_t2_t30_mem0', length=1, delay_cost=1)
	S += d_t2_t30_mem0 >= 22
	d_t2_t30_mem0 += MM_MEM[0]

	d_t2_t30_mem1 = S.Task('d_t2_t30_mem1', length=1, delay_cost=1)
	S += d_t2_t30_mem1 >= 22
	d_t2_t30_mem1 += MM_MEM[1]

	d_t2_t3_t5 = S.Task('d_t2_t3_t5', length=2, delay_cost=1)
	S += d_t2_t3_t5 >= 22
	d_t2_t3_t5 += MAS[1]

	d_t4_a1_0 = S.Task('d_t4_a1_0', length=2, delay_cost=1)
	S += d_t4_a1_0 >= 22
	d_t4_a1_0 += MAS[3]

	d_t4_t3_t2_in = S.Task('d_t4_t3_t2_in', length=1, delay_cost=1)
	S += d_t4_t3_t2_in >= 22
	d_t4_t3_t2_in += MAS_in[3]

	d_t4_t3_t2_mem0 = S.Task('d_t4_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem0 >= 22
	d_t4_t3_t2_mem0 += MAS_MEM[2]

	d_t4_t3_t2_mem1 = S.Task('d_t4_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t2_mem1 >= 22
	d_t4_t3_t2_mem1 += MAS_MEM[7]

	d_t5_a1_0_in = S.Task('d_t5_a1_0_in', length=1, delay_cost=1)
	S += d_t5_a1_0_in >= 22
	d_t5_a1_0_in += MAS_in[0]

	d_t5_a1_0_mem0 = S.Task('d_t5_a1_0_mem0', length=1, delay_cost=1)
	S += d_t5_a1_0_mem0 >= 22
	d_t5_a1_0_mem0 += MAS_MEM[4]

	d_t5_a1_0_mem1 = S.Task('d_t5_a1_0_mem1', length=1, delay_cost=1)
	S += d_t5_a1_0_mem1 >= 22
	d_t5_a1_0_mem1 += MAS_MEM[1]

	d_t5_t10_in = S.Task('d_t5_t10_in', length=1, delay_cost=1)
	S += d_t5_t10_in >= 22
	d_t5_t10_in += MAS_in[2]

	d_t5_t10_mem0 = S.Task('d_t5_t10_mem0', length=1, delay_cost=1)
	S += d_t5_t10_mem0 >= 22
	d_t5_t10_mem0 += MAS_MEM[0]

	d_t5_t10_mem1 = S.Task('d_t5_t10_mem1', length=1, delay_cost=1)
	S += d_t5_t10_mem1 >= 22
	d_t5_t10_mem1 += MAS_MEM[5]

	d_t5_t3_t1 = S.Task('d_t5_t3_t1', length=5, delay_cost=1)
	S += d_t5_t3_t1 >= 22
	d_t5_t3_t1 += MM[0]

	d_t5_t3_t2 = S.Task('d_t5_t3_t2', length=2, delay_cost=1)
	S += d_t5_t3_t2 >= 22
	d_t5_t3_t2 += MAS[2]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 23
	c_t0_t1_t4_in += MM_in[0]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 23
	c_t0_t1_t4_mem0 += MAS_MEM[4]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 23
	c_t0_t1_t4_mem1 += MAS_MEM[3]

	c_t0_t1_t5_in = S.Task('c_t0_t1_t5_in', length=1, delay_cost=1)
	S += c_t0_t1_t5_in >= 23
	c_t0_t1_t5_in += MAS_in[0]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 23
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 23
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=5, delay_cost=1)
	S += c_t0_t4_t0 >= 23
	c_t0_t4_t0 += MM[0]

	d_t0_a1_0_mem0 = S.Task('d_t0_a1_0_mem0', length=1, delay_cost=1)
	S += d_t0_a1_0_mem0 >= 23
	d_t0_a1_0_mem0 += MAIN_MEM_r[0]

	d_t2_t30 = S.Task('d_t2_t30', length=2, delay_cost=1)
	S += d_t2_t30 >= 23
	d_t2_t30 += MAS[1]

	d_t2_t3_t1_mem1 = S.Task('d_t2_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t1_mem1 >= 23
	d_t2_t3_t1_mem1 += MAIN_MEM_r[1]

	d_t3_t10_in = S.Task('d_t3_t10_in', length=1, delay_cost=1)
	S += d_t3_t10_in >= 23
	d_t3_t10_in += MAS_in[2]

	d_t3_t10_mem0 = S.Task('d_t3_t10_mem0', length=1, delay_cost=1)
	S += d_t3_t10_mem0 >= 23
	d_t3_t10_mem0 += MAS_MEM[6]

	d_t3_t10_mem1 = S.Task('d_t3_t10_mem1', length=1, delay_cost=1)
	S += d_t3_t10_mem1 >= 23
	d_t3_t10_mem1 += MAS_MEM[7]

	d_t4_t3_t2 = S.Task('d_t4_t3_t2', length=2, delay_cost=1)
	S += d_t4_t3_t2 >= 23
	d_t4_t3_t2 += MAS[3]

	d_t5_a1_0 = S.Task('d_t5_a1_0', length=2, delay_cost=1)
	S += d_t5_a1_0 >= 23
	d_t5_a1_0 += MAS[0]

	d_t5_a1_1_in = S.Task('d_t5_a1_1_in', length=1, delay_cost=1)
	S += d_t5_a1_1_in >= 23
	d_t5_a1_1_in += MAS_in[3]

	d_t5_a1_1_mem0 = S.Task('d_t5_a1_1_mem0', length=1, delay_cost=1)
	S += d_t5_a1_1_mem0 >= 23
	d_t5_a1_1_mem0 += MAS_MEM[0]

	d_t5_a1_1_mem1 = S.Task('d_t5_a1_1_mem1', length=1, delay_cost=1)
	S += d_t5_a1_1_mem1 >= 23
	d_t5_a1_1_mem1 += MAS_MEM[5]

	d_t5_t10 = S.Task('d_t5_t10', length=2, delay_cost=1)
	S += d_t5_t10 >= 23
	d_t5_t10 += MAS[2]

	d_t5_t11_in = S.Task('d_t5_t11_in', length=1, delay_cost=1)
	S += d_t5_t11_in >= 23
	d_t5_t11_in += MAS_in[1]

	d_t5_t11_mem0 = S.Task('d_t5_t11_mem0', length=1, delay_cost=1)
	S += d_t5_t11_mem0 >= 23
	d_t5_t11_mem0 += MAS_MEM[2]

	d_t5_t11_mem1 = S.Task('d_t5_t11_mem1', length=1, delay_cost=1)
	S += d_t5_t11_mem1 >= 23
	d_t5_t11_mem1 += MAS_MEM[1]

	c_t0_t00_in = S.Task('c_t0_t00_in', length=1, delay_cost=1)
	S += c_t0_t00_in >= 24
	c_t0_t00_in += MAS_in[3]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 24
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 24
	c_t0_t00_mem1 += MM_MEM[1]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=5, delay_cost=1)
	S += c_t0_t1_t4 >= 24
	c_t0_t1_t4 += MM[0]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=2, delay_cost=1)
	S += c_t0_t1_t5 >= 24
	c_t0_t1_t5 += MAS[0]

	d_t1_t3_t1_mem0 = S.Task('d_t1_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t3_t1_mem0 >= 24
	d_t1_t3_t1_mem0 += MAIN_MEM_r[0]

	d_t2_a1_1_mem1 = S.Task('d_t2_a1_1_mem1', length=1, delay_cost=1)
	S += d_t2_a1_1_mem1 >= 24
	d_t2_a1_1_mem1 += MAIN_MEM_r[1]

	d_t2_t01_in = S.Task('d_t2_t01_in', length=1, delay_cost=1)
	S += d_t2_t01_in >= 24
	d_t2_t01_in += MAS_in[0]

	d_t2_t01_mem1 = S.Task('d_t2_t01_mem1', length=1, delay_cost=1)
	S += d_t2_t01_mem1 >= 24
	d_t2_t01_mem1 += MAS_MEM[3]

	d_t2_t3_t4_in = S.Task('d_t2_t3_t4_in', length=1, delay_cost=1)
	S += d_t2_t3_t4_in >= 24
	d_t2_t3_t4_in += MM_in[0]

	d_t2_t3_t4_mem0 = S.Task('d_t2_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem0 >= 24
	d_t2_t3_t4_mem0 += MAS_MEM[2]

	d_t2_t3_t4_mem1 = S.Task('d_t2_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t4_mem1 >= 24
	d_t2_t3_t4_mem1 += MAS_MEM[5]

	d_t3_t10 = S.Task('d_t3_t10', length=2, delay_cost=1)
	S += d_t3_t10 >= 24
	d_t3_t10 += MAS[2]

	d_t3_t3_t2_in = S.Task('d_t3_t3_t2_in', length=1, delay_cost=1)
	S += d_t3_t3_t2_in >= 24
	d_t3_t3_t2_in += MAS_in[1]

	d_t3_t3_t2_mem0 = S.Task('d_t3_t3_t2_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem0 >= 24
	d_t3_t3_t2_mem0 += MAS_MEM[6]

	d_t3_t3_t2_mem1 = S.Task('d_t3_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t2_mem1 >= 24
	d_t3_t3_t2_mem1 += MAS_MEM[7]

	d_t5_a1_1 = S.Task('d_t5_a1_1', length=2, delay_cost=1)
	S += d_t5_a1_1 >= 24
	d_t5_a1_1 += MAS[3]

	d_t5_t11 = S.Task('d_t5_t11', length=2, delay_cost=1)
	S += d_t5_t11 >= 24
	d_t5_t11 += MAS[1]

	d_t5_t3_t3_in = S.Task('d_t5_t3_t3_in', length=1, delay_cost=1)
	S += d_t5_t3_t3_in >= 24
	d_t5_t3_t3_in += MAS_in[2]

	d_t5_t3_t3_mem0 = S.Task('d_t5_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem0 >= 24
	d_t5_t3_t3_mem0 += MAS_MEM[4]

	d_t5_t3_t3_mem1 = S.Task('d_t5_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t3_mem1 >= 24
	d_t5_t3_t3_mem1 += MAS_MEM[1]

	c_t0_t00 = S.Task('c_t0_t00', length=2, delay_cost=1)
	S += c_t0_t00 >= 25
	c_t0_t00 += MAS[3]

	d_t0_t3_t5_in = S.Task('d_t0_t3_t5_in', length=1, delay_cost=1)
	S += d_t0_t3_t5_in >= 25
	d_t0_t3_t5_in += MAS_in[1]

	d_t0_t3_t5_mem0 = S.Task('d_t0_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem0 >= 25
	d_t0_t3_t5_mem0 += MM_MEM[0]

	d_t0_t3_t5_mem1 = S.Task('d_t0_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t0_t3_t5_mem1 >= 25
	d_t0_t3_t5_mem1 += MM_MEM[1]

	d_t1_a1_1_mem0 = S.Task('d_t1_a1_1_mem0', length=1, delay_cost=1)
	S += d_t1_a1_1_mem0 >= 25
	d_t1_a1_1_mem0 += MAIN_MEM_r[0]

	d_t1_t01_in = S.Task('d_t1_t01_in', length=1, delay_cost=1)
	S += d_t1_t01_in >= 25
	d_t1_t01_in += MAS_in[3]

	d_t1_t01_mem1 = S.Task('d_t1_t01_mem1', length=1, delay_cost=1)
	S += d_t1_t01_mem1 >= 25
	d_t1_t01_mem1 += MAS_MEM[3]

	d_t2_t01 = S.Task('d_t2_t01', length=2, delay_cost=1)
	S += d_t2_t01 >= 25
	d_t2_t01 += MAS[0]

	d_t2_t3_t2_mem1 = S.Task('d_t2_t3_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t2_mem1 >= 25
	d_t2_t3_t2_mem1 += MAIN_MEM_r[1]

	d_t2_t3_t4 = S.Task('d_t2_t3_t4', length=5, delay_cost=1)
	S += d_t2_t3_t4 >= 25
	d_t2_t3_t4 += MM[0]

	d_t3_a1_1_in = S.Task('d_t3_a1_1_in', length=1, delay_cost=1)
	S += d_t3_a1_1_in >= 25
	d_t3_a1_1_in += MAS_in[2]

	d_t3_a1_1_mem0 = S.Task('d_t3_a1_1_mem0', length=1, delay_cost=1)
	S += d_t3_a1_1_mem0 >= 25
	d_t3_a1_1_mem0 += MAS_MEM[0]

	d_t3_a1_1_mem1 = S.Task('d_t3_a1_1_mem1', length=1, delay_cost=1)
	S += d_t3_a1_1_mem1 >= 25
	d_t3_a1_1_mem1 += MAS_MEM[7]

	d_t3_t3_t2 = S.Task('d_t3_t3_t2', length=2, delay_cost=1)
	S += d_t3_t3_t2 >= 25
	d_t3_t3_t2 += MAS[1]

	d_t3_t3_t3_in = S.Task('d_t3_t3_t3_in', length=1, delay_cost=1)
	S += d_t3_t3_t3_in >= 25
	d_t3_t3_t3_in += MAS_in[0]

	d_t3_t3_t3_mem0 = S.Task('d_t3_t3_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem0 >= 25
	d_t3_t3_t3_mem0 += MAS_MEM[6]

	d_t3_t3_t3_mem1 = S.Task('d_t3_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t3_mem1 >= 25
	d_t3_t3_t3_mem1 += MAS_MEM[1]

	d_t4_t3_t0_in = S.Task('d_t4_t3_t0_in', length=1, delay_cost=1)
	S += d_t4_t3_t0_in >= 25
	d_t4_t3_t0_in += MM_in[0]

	d_t4_t3_t0_mem0 = S.Task('d_t4_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem0 >= 25
	d_t4_t3_t0_mem0 += MAS_MEM[2]

	d_t4_t3_t0_mem1 = S.Task('d_t4_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t0_mem1 >= 25
	d_t4_t3_t0_mem1 += MAS_MEM[5]

	d_t5_t3_t3 = S.Task('d_t5_t3_t3', length=2, delay_cost=1)
	S += d_t5_t3_t3 >= 25
	d_t5_t3_t3 += MAS[2]

	c_t0_t10_in = S.Task('c_t0_t10_in', length=1, delay_cost=1)
	S += c_t0_t10_in >= 26
	c_t0_t10_in += MAS_in[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 26
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 26
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 26
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 26
	c_t0_t4_t1_mem0 += MAS_MEM[0]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 26
	c_t0_t4_t1_mem1 += MAS_MEM[7]

	c_t2_t4_t3_in = S.Task('c_t2_t4_t3_in', length=1, delay_cost=1)
	S += c_t2_t4_t3_in >= 26
	c_t2_t4_t3_in += MAS_in[2]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 26
	c_t2_t4_t3_mem0 += MAS_MEM[4]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 26
	c_t2_t4_t3_mem1 += MAS_MEM[3]

	d_t0_t2_t3_in = S.Task('d_t0_t2_t3_in', length=1, delay_cost=1)
	S += d_t0_t2_t3_in >= 26
	d_t0_t2_t3_in += MAS_in[0]

	d_t0_t2_t3_mem0 = S.Task('d_t0_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem0 >= 26
	d_t0_t2_t3_mem0 += MAS_MEM[2]

	d_t0_t2_t3_mem1 = S.Task('d_t0_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t3_mem1 >= 26
	d_t0_t2_t3_mem1 += MAS_MEM[1]

	d_t0_t3_t5 = S.Task('d_t0_t3_t5', length=2, delay_cost=1)
	S += d_t0_t3_t5 >= 26
	d_t0_t3_t5 += MAS[1]

	d_t1_t01 = S.Task('d_t1_t01', length=2, delay_cost=1)
	S += d_t1_t01 >= 26
	d_t1_t01 += MAS[3]

	d_t2_a1_1_mem0 = S.Task('d_t2_a1_1_mem0', length=1, delay_cost=1)
	S += d_t2_a1_1_mem0 >= 26
	d_t2_a1_1_mem0 += MAIN_MEM_r[0]

	d_t2_t2_t3_in = S.Task('d_t2_t2_t3_in', length=1, delay_cost=1)
	S += d_t2_t2_t3_in >= 26
	d_t2_t2_t3_in += MAS_in[3]

	d_t2_t2_t3_mem0 = S.Task('d_t2_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem0 >= 26
	d_t2_t2_t3_mem0 += MAS_MEM[6]

	d_t2_t2_t3_mem1 = S.Task('d_t2_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t3_mem1 >= 26
	d_t2_t2_t3_mem1 += MAS_MEM[5]

	d_t3001_mem1 = S.Task('d_t3001_mem1', length=1, delay_cost=1)
	S += d_t3001_mem1 >= 26
	d_t3001_mem1 += MAIN_MEM_r[1]

	d_t3_a1_1 = S.Task('d_t3_a1_1', length=2, delay_cost=1)
	S += d_t3_a1_1 >= 26
	d_t3_a1_1 += MAS[2]

	d_t3_t3_t3 = S.Task('d_t3_t3_t3', length=2, delay_cost=1)
	S += d_t3_t3_t3 >= 26
	d_t3_t3_t3 += MAS[0]

	d_t4_t3_t0 = S.Task('d_t4_t3_t0', length=5, delay_cost=1)
	S += d_t4_t3_t0 >= 26
	d_t4_t3_t0 += MM[0]

	c_t0_t0_t5_in = S.Task('c_t0_t0_t5_in', length=1, delay_cost=1)
	S += c_t0_t0_t5_in >= 27
	c_t0_t0_t5_in += MAS_in[1]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 27
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 27
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t10 = S.Task('c_t0_t10', length=2, delay_cost=1)
	S += c_t0_t10 >= 27
	c_t0_t10 += MAS[1]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=5, delay_cost=1)
	S += c_t0_t4_t1 >= 27
	c_t0_t4_t1 += MM[0]

	c_t2_t4_t2_in = S.Task('c_t2_t4_t2_in', length=1, delay_cost=1)
	S += c_t2_t4_t2_in >= 27
	c_t2_t4_t2_in += MAS_in[0]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 27
	c_t2_t4_t2_mem0 += MAS_MEM[2]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 27
	c_t2_t4_t2_mem1 += MAS_MEM[3]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=2, delay_cost=1)
	S += c_t2_t4_t3 >= 27
	c_t2_t4_t3 += MAS[2]

	d_t0_t2_t3 = S.Task('d_t0_t2_t3', length=2, delay_cost=1)
	S += d_t0_t2_t3 >= 27
	d_t0_t2_t3 += MAS[0]

	d_t1_t10_mem0 = S.Task('d_t1_t10_mem0', length=1, delay_cost=1)
	S += d_t1_t10_mem0 >= 27
	d_t1_t10_mem0 += MAIN_MEM_r[0]

	d_t1_t3_t0_mem1 = S.Task('d_t1_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t3_t0_mem1 >= 27
	d_t1_t3_t0_mem1 += MAIN_MEM_r[1]

	d_t2_t00_in = S.Task('d_t2_t00_in', length=1, delay_cost=1)
	S += d_t2_t00_in >= 27
	d_t2_t00_in += MAS_in[2]

	d_t2_t00_mem1 = S.Task('d_t2_t00_mem1', length=1, delay_cost=1)
	S += d_t2_t00_mem1 >= 27
	d_t2_t00_mem1 += MAS_MEM[1]

	d_t2_t2_t3 = S.Task('d_t2_t2_t3', length=2, delay_cost=1)
	S += d_t2_t2_t3 >= 27
	d_t2_t2_t3 += MAS[3]

	d_t4_t11_in = S.Task('d_t4_t11_in', length=1, delay_cost=1)
	S += d_t4_t11_in >= 27
	d_t4_t11_in += MAS_in[3]

	d_t4_t11_mem0 = S.Task('d_t4_t11_mem0', length=1, delay_cost=1)
	S += d_t4_t11_mem0 >= 27
	d_t4_t11_mem0 += MAS_MEM[6]

	d_t4_t11_mem1 = S.Task('d_t4_t11_mem1', length=1, delay_cost=1)
	S += d_t4_t11_mem1 >= 27
	d_t4_t11_mem1 += MAS_MEM[7]

	d_t5_t3_t0_in = S.Task('d_t5_t3_t0_in', length=1, delay_cost=1)
	S += d_t5_t3_t0_in >= 27
	d_t5_t3_t0_in += MM_in[0]

	d_t5_t3_t0_mem0 = S.Task('d_t5_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem0 >= 27
	d_t5_t3_t0_mem0 += MAS_MEM[0]

	d_t5_t3_t0_mem1 = S.Task('d_t5_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t0_mem1 >= 27
	d_t5_t3_t0_mem1 += MAS_MEM[5]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=2, delay_cost=1)
	S += c_t0_t0_t5 >= 28
	c_t0_t0_t5 += MAS[1]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=2, delay_cost=1)
	S += c_t2_t4_t2 >= 28
	c_t2_t4_t2 += MAS[0]

	c_t4_t20_in = S.Task('c_t4_t20_in', length=1, delay_cost=1)
	S += c_t4_t20_in >= 28
	c_t4_t20_in += MAS_in[2]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 28
	c_t4_t20_mem0 += MAS_MEM[2]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 28
	c_t4_t20_mem1 += MAS_MEM[3]

	d_t0_t00_in = S.Task('d_t0_t00_in', length=1, delay_cost=1)
	S += d_t0_t00_in >= 28
	d_t0_t00_in += MAS_in[3]

	d_t0_t00_mem1 = S.Task('d_t0_t00_mem1', length=1, delay_cost=1)
	S += d_t0_t00_mem1 >= 28
	d_t0_t00_mem1 += MAS_MEM[1]

	d_t0_t01_in = S.Task('d_t0_t01_in', length=1, delay_cost=1)
	S += d_t0_t01_in >= 28
	d_t0_t01_in += MAS_in[1]

	d_t0_t01_mem1 = S.Task('d_t0_t01_mem1', length=1, delay_cost=1)
	S += d_t0_t01_mem1 >= 28
	d_t0_t01_mem1 += MAS_MEM[5]

	d_t0_t30_in = S.Task('d_t0_t30_in', length=1, delay_cost=1)
	S += d_t0_t30_in >= 28
	d_t0_t30_in += MAS_in[0]

	d_t0_t30_mem0 = S.Task('d_t0_t30_mem0', length=1, delay_cost=1)
	S += d_t0_t30_mem0 >= 28
	d_t0_t30_mem0 += MM_MEM[0]

	d_t0_t30_mem1 = S.Task('d_t0_t30_mem1', length=1, delay_cost=1)
	S += d_t0_t30_mem1 >= 28
	d_t0_t30_mem1 += MM_MEM[1]

	d_t1_t11_mem0 = S.Task('d_t1_t11_mem0', length=1, delay_cost=1)
	S += d_t1_t11_mem0 >= 28
	d_t1_t11_mem0 += MAIN_MEM_r[0]

	d_t2_t00 = S.Task('d_t2_t00', length=2, delay_cost=1)
	S += d_t2_t00 >= 28
	d_t2_t00 += MAS[2]

	d_t3_t3_t0_in = S.Task('d_t3_t3_t0_in', length=1, delay_cost=1)
	S += d_t3_t3_t0_in >= 28
	d_t3_t3_t0_in += MM_in[0]

	d_t3_t3_t0_mem0 = S.Task('d_t3_t3_t0_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem0 >= 28
	d_t3_t3_t0_mem0 += MAS_MEM[6]

	d_t3_t3_t0_mem1 = S.Task('d_t3_t3_t0_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t0_mem1 >= 28
	d_t3_t3_t0_mem1 += MAS_MEM[7]

	d_t4001_mem1 = S.Task('d_t4001_mem1', length=1, delay_cost=1)
	S += d_t4001_mem1 >= 28
	d_t4001_mem1 += MAIN_MEM_r[1]

	d_t4_t11 = S.Task('d_t4_t11', length=2, delay_cost=1)
	S += d_t4_t11 >= 28
	d_t4_t11 += MAS[3]

	d_t5_t3_t0 = S.Task('d_t5_t3_t0', length=5, delay_cost=1)
	S += d_t5_t3_t0 >= 28
	d_t5_t3_t0 += MM[0]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 29
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 29
	c_t0_t0_t4_mem0 += MAS_MEM[4]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 29
	c_t0_t0_t4_mem1 += MAS_MEM[1]

	c_t2_t00_in = S.Task('c_t2_t00_in', length=1, delay_cost=1)
	S += c_t2_t00_in >= 29
	c_t2_t00_in += MAS_in[1]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 29
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 29
	c_t2_t00_mem1 += MM_MEM[1]

	c_t4_t1_t2_in = S.Task('c_t4_t1_t2_in', length=1, delay_cost=1)
	S += c_t4_t1_t2_in >= 29
	c_t4_t1_t2_in += MAS_in[2]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 29
	c_t4_t1_t2_mem0 += MAS_MEM[2]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 29
	c_t4_t1_t2_mem1 += MAS_MEM[7]

	c_t4_t20 = S.Task('c_t4_t20', length=2, delay_cost=1)
	S += c_t4_t20 >= 29
	c_t4_t20 += MAS[2]

	d_t0_t00 = S.Task('d_t0_t00', length=2, delay_cost=1)
	S += d_t0_t00 >= 29
	d_t0_t00 += MAS[3]

	d_t0_t01 = S.Task('d_t0_t01', length=2, delay_cost=1)
	S += d_t0_t01 >= 29
	d_t0_t01 += MAS[1]

	d_t0_t30 = S.Task('d_t0_t30', length=2, delay_cost=1)
	S += d_t0_t30 >= 29
	d_t0_t30 += MAS[0]

	d_t2_t3_t3_mem1 = S.Task('d_t2_t3_t3_mem1', length=1, delay_cost=1)
	S += d_t2_t3_t3_mem1 >= 29
	d_t2_t3_t3_mem1 += MAIN_MEM_r[1]

	d_t3011_mem0 = S.Task('d_t3011_mem0', length=1, delay_cost=1)
	S += d_t3011_mem0 >= 29
	d_t3011_mem0 += MAIN_MEM_r[0]

	d_t3_t3_t0 = S.Task('d_t3_t3_t0', length=5, delay_cost=1)
	S += d_t3_t3_t0 >= 29
	d_t3_t3_t0 += MM[0]

	d_t4_a1_1_in = S.Task('d_t4_a1_1_in', length=1, delay_cost=1)
	S += d_t4_a1_1_in >= 29
	d_t4_a1_1_in += MAS_in[0]

	d_t4_a1_1_mem0 = S.Task('d_t4_a1_1_mem0', length=1, delay_cost=1)
	S += d_t4_a1_1_mem0 >= 29
	d_t4_a1_1_mem0 += MAS_MEM[6]

	d_t4_a1_1_mem1 = S.Task('d_t4_a1_1_mem1', length=1, delay_cost=1)
	S += d_t4_a1_1_mem1 >= 29
	d_t4_a1_1_mem1 += MAS_MEM[5]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=5, delay_cost=1)
	S += c_t0_t0_t4 >= 30
	c_t0_t0_t4 += MM[0]

	c_t2_t00 = S.Task('c_t2_t00', length=2, delay_cost=1)
	S += c_t2_t00 >= 30
	c_t2_t00 += MAS[1]

	c_t2_t10_in = S.Task('c_t2_t10_in', length=1, delay_cost=1)
	S += c_t2_t10_in >= 30
	c_t2_t10_in += MAS_in[1]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 30
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 30
	c_t2_t10_mem1 += MM_MEM[1]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=2, delay_cost=1)
	S += c_t4_t1_t2 >= 30
	c_t4_t1_t2 += MAS[2]

	c_t4_t30_in = S.Task('c_t4_t30_in', length=1, delay_cost=1)
	S += c_t4_t30_in >= 30
	c_t4_t30_in += MAS_in[2]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 30
	c_t4_t30_mem0 += MAS_MEM[2]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 30
	c_t4_t30_mem1 += MAS_MEM[1]

	c_t5_t1_t2_in = S.Task('c_t5_t1_t2_in', length=1, delay_cost=1)
	S += c_t5_t1_t2_in >= 30
	c_t5_t1_t2_in += MAS_in[3]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 30
	c_t5_t1_t2_mem0 += MAS_MEM[4]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 30
	c_t5_t1_t2_mem1 += MAS_MEM[3]

	d_t1_t00_in = S.Task('d_t1_t00_in', length=1, delay_cost=1)
	S += d_t1_t00_in >= 30
	d_t1_t00_in += MAS_in[0]

	d_t1_t00_mem1 = S.Task('d_t1_t00_mem1', length=1, delay_cost=1)
	S += d_t1_t00_mem1 >= 30
	d_t1_t00_mem1 += MAS_MEM[5]

	d_t4010_mem0 = S.Task('d_t4010_mem0', length=1, delay_cost=1)
	S += d_t4010_mem0 >= 30
	d_t4010_mem0 += MAIN_MEM_r[0]

	d_t4_a1_1 = S.Task('d_t4_a1_1', length=2, delay_cost=1)
	S += d_t4_a1_1 >= 30
	d_t4_a1_1 += MAS[0]

	d_t4_t3_t1_in = S.Task('d_t4_t3_t1_in', length=1, delay_cost=1)
	S += d_t4_t3_t1_in >= 30
	d_t4_t3_t1_in += MM_in[0]

	d_t4_t3_t1_mem0 = S.Task('d_t4_t3_t1_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem0 >= 30
	d_t4_t3_t1_mem0 += MAS_MEM[6]

	d_t4_t3_t1_mem1 = S.Task('d_t4_t3_t1_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t1_mem1 >= 30
	d_t4_t3_t1_mem1 += MAS_MEM[7]

	d_t5001_mem1 = S.Task('d_t5001_mem1', length=1, delay_cost=1)
	S += d_t5001_mem1 >= 30
	d_t5001_mem1 += MAIN_MEM_r[1]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 31
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t10_in = S.Task('c_t1_t10_in', length=1, delay_cost=1)
	S += c_t1_t10_in >= 31
	c_t1_t10_in += MAS_in[2]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 31
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 31
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 31
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t2_in = S.Task('c_t1_t4_t2_in', length=1, delay_cost=1)
	S += c_t1_t4_t2_in >= 31
	c_t1_t4_t2_in += MAS_in[3]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 31
	c_t1_t4_t2_mem0 += MAS_MEM[4]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 31
	c_t1_t4_t2_mem1 += MAS_MEM[5]

	c_t1_t4_t3_in = S.Task('c_t1_t4_t3_in', length=1, delay_cost=1)
	S += c_t1_t4_t3_in >= 31
	c_t1_t4_t3_in += MAS_in[1]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 31
	c_t1_t4_t3_mem0 += MAS_MEM[0]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 31
	c_t1_t4_t3_mem1 += MAS_MEM[7]

	c_t2_t10 = S.Task('c_t2_t10', length=2, delay_cost=1)
	S += c_t2_t10 >= 31
	c_t2_t10 += MAS[1]

	c_t3_t21_in = S.Task('c_t3_t21_in', length=1, delay_cost=1)
	S += c_t3_t21_in >= 31
	c_t3_t21_in += MAS_in[0]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 31
	c_t3_t21_mem0 += MAS_MEM[6]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 31
	c_t3_t21_mem1 += MAS_MEM[1]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 31
	c_t4_t0_t0_in += MM_in[0]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 31
	c_t4_t0_t0_mem0 += MAS_MEM[2]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 31
	c_t4_t0_t0_mem1 += MAS_MEM[3]

	c_t4_t30 = S.Task('c_t4_t30', length=2, delay_cost=1)
	S += c_t4_t30 >= 31
	c_t4_t30 += MAS[2]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=2, delay_cost=1)
	S += c_t5_t1_t2 >= 31
	c_t5_t1_t2 += MAS[3]

	d_t1_t00 = S.Task('d_t1_t00', length=2, delay_cost=1)
	S += d_t1_t00 >= 31
	d_t1_t00 += MAS[0]

	d_t4_t3_t1 = S.Task('d_t4_t3_t1', length=5, delay_cost=1)
	S += d_t4_t3_t1 >= 31
	d_t4_t3_t1 += MM[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 32
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 32
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 32
	c_t1_t0_t4_mem0 += MAS_MEM[2]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 32
	c_t1_t0_t4_mem1 += MAS_MEM[3]

	c_t1_t10 = S.Task('c_t1_t10', length=2, delay_cost=1)
	S += c_t1_t10 >= 32
	c_t1_t10 += MAS[2]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 32
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=2, delay_cost=1)
	S += c_t1_t4_t2 >= 32
	c_t1_t4_t2 += MAS[3]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=2, delay_cost=1)
	S += c_t1_t4_t3 >= 32
	c_t1_t4_t3 += MAS[1]

	c_t2_t1_t5_in = S.Task('c_t2_t1_t5_in', length=1, delay_cost=1)
	S += c_t2_t1_t5_in >= 32
	c_t2_t1_t5_in += MAS_in[0]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 32
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 32
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t3_t1_t2_in = S.Task('c_t3_t1_t2_in', length=1, delay_cost=1)
	S += c_t3_t1_t2_in >= 32
	c_t3_t1_t2_in += MAS_in[2]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 32
	c_t3_t1_t2_mem0 += MAS_MEM[4]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 32
	c_t3_t1_t2_mem1 += MAS_MEM[1]

	c_t3_t1_t3_in = S.Task('c_t3_t1_t3_in', length=1, delay_cost=1)
	S += c_t3_t1_t3_in >= 32
	c_t3_t1_t3_in += MAS_in[3]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 32
	c_t3_t1_t3_mem0 += MAS_MEM[6]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 32
	c_t3_t1_t3_mem1 += MAS_MEM[7]

	c_t3_t21 = S.Task('c_t3_t21', length=2, delay_cost=1)
	S += c_t3_t21 >= 32
	c_t3_t21 += MAS[0]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=5, delay_cost=1)
	S += c_t4_t0_t0 >= 32
	c_t4_t0_t0 += MM[0]

	c_t4_t1_t3_in = S.Task('c_t4_t1_t3_in', length=1, delay_cost=1)
	S += c_t4_t1_t3_in >= 32
	c_t4_t1_t3_in += MAS_in[1]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 32
	c_t4_t1_t3_mem0 += MAS_MEM[0]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 32
	c_t4_t1_t3_mem1 += MAS_MEM[5]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 33
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t2_in = S.Task('c_t0_t4_t2_in', length=1, delay_cost=1)
	S += c_t0_t4_t2_in >= 33
	c_t0_t4_t2_in += MAS_in[2]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 33
	c_t0_t4_t2_mem0 += MAS_MEM[6]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 33
	c_t0_t4_t2_mem1 += MAS_MEM[1]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 33
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=5, delay_cost=1)
	S += c_t1_t0_t4 >= 33
	c_t1_t0_t4 += MM[0]

	c_t1_t0_t5_in = S.Task('c_t1_t0_t5_in', length=1, delay_cost=1)
	S += c_t1_t0_t5_in >= 33
	c_t1_t0_t5_in += MAS_in[0]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 33
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 33
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 33
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 33
	c_t2_t0_t4_mem0 += MAS_MEM[4]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 33
	c_t2_t0_t4_mem1 += MAS_MEM[3]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=2, delay_cost=1)
	S += c_t2_t1_t5 >= 33
	c_t2_t1_t5 += MAS[0]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=2, delay_cost=1)
	S += c_t3_t1_t2 >= 33
	c_t3_t1_t2 += MAS[2]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=2, delay_cost=1)
	S += c_t3_t1_t3 >= 33
	c_t3_t1_t3 += MAS[3]

	c_t3_t30_in = S.Task('c_t3_t30_in', length=1, delay_cost=1)
	S += c_t3_t30_in >= 33
	c_t3_t30_in += MAS_in[3]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 33
	c_t3_t30_mem0 += MAS_MEM[0]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 33
	c_t3_t30_mem1 += MAS_MEM[7]

	c_t4_t0_t3_in = S.Task('c_t4_t0_t3_in', length=1, delay_cost=1)
	S += c_t4_t0_t3_in >= 33
	c_t4_t0_t3_in += MAS_in[1]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 33
	c_t4_t0_t3_mem0 += MAS_MEM[2]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 33
	c_t4_t0_t3_mem1 += MAS_MEM[5]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=2, delay_cost=1)
	S += c_t4_t1_t3 >= 33
	c_t4_t1_t3 += MAS[1]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 34
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 34
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=2, delay_cost=1)
	S += c_t0_t4_t2 >= 34
	c_t0_t4_t2 += MAS[2]

	c_t1_t00_in = S.Task('c_t1_t00_in', length=1, delay_cost=1)
	S += c_t1_t00_in >= 34
	c_t1_t00_in += MAS_in[1]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 34
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 34
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=2, delay_cost=1)
	S += c_t1_t0_t5 >= 34
	c_t1_t0_t5 += MAS[0]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=5, delay_cost=1)
	S += c_t2_t0_t4 >= 34
	c_t2_t0_t4 += MM[0]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 34
	c_t2_t4_t1_in += MM_in[0]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 34
	c_t2_t4_t1_mem0 += MAS_MEM[2]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 34
	c_t2_t4_t1_mem1 += MAS_MEM[3]

	c_t3_t0_t3_in = S.Task('c_t3_t0_t3_in', length=1, delay_cost=1)
	S += c_t3_t0_t3_in >= 34
	c_t3_t0_t3_in += MAS_in[0]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 34
	c_t3_t0_t3_mem0 += MAS_MEM[0]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 34
	c_t3_t0_t3_mem1 += MAS_MEM[5]

	c_t3_t30 = S.Task('c_t3_t30', length=2, delay_cost=1)
	S += c_t3_t30 >= 34
	c_t3_t30 += MAS[3]

	c_t3_t31_in = S.Task('c_t3_t31_in', length=1, delay_cost=1)
	S += c_t3_t31_in >= 34
	c_t3_t31_in += MAS_in[2]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 34
	c_t3_t31_mem0 += MAS_MEM[4]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 34
	c_t3_t31_mem1 += MAS_MEM[7]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=2, delay_cost=1)
	S += c_t4_t0_t3 >= 34
	c_t4_t0_t3 += MAS[1]

	c_t5_t0_t3_in = S.Task('c_t5_t0_t3_in', length=1, delay_cost=1)
	S += c_t5_t0_t3_in >= 34
	c_t5_t0_t3_in += MAS_in[3]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 34
	c_t5_t0_t3_mem0 += MAS_MEM[6]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 34
	c_t5_t0_t3_mem1 += MAS_MEM[1]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 35
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t00 = S.Task('c_t1_t00', length=2, delay_cost=1)
	S += c_t1_t00 >= 35
	c_t1_t00 += MAS[1]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 35
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t5_in = S.Task('c_t2_t0_t5_in', length=1, delay_cost=1)
	S += c_t2_t0_t5_in >= 35
	c_t2_t0_t5_in += MAS_in[2]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 35
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 35
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=5, delay_cost=1)
	S += c_t2_t4_t1 >= 35
	c_t2_t4_t1 += MM[0]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=2, delay_cost=1)
	S += c_t3_t0_t3 >= 35
	c_t3_t0_t3 += MAS[0]

	c_t3_t31 = S.Task('c_t3_t31', length=2, delay_cost=1)
	S += c_t3_t31 >= 35
	c_t3_t31 += MAS[2]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 35
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 35
	c_t4_t1_t0_mem0 += MAS_MEM[2]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 35
	c_t4_t1_t0_mem1 += MAS_MEM[1]

	c_t4_t21_in = S.Task('c_t4_t21_in', length=1, delay_cost=1)
	S += c_t4_t21_in >= 35
	c_t4_t21_in += MAS_in[0]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 35
	c_t4_t21_mem0 += MAS_MEM[0]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 35
	c_t4_t21_mem1 += MAS_MEM[7]

	c_t4_t31_in = S.Task('c_t4_t31_in', length=1, delay_cost=1)
	S += c_t4_t31_in >= 35
	c_t4_t31_in += MAS_in[3]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 35
	c_t4_t31_mem0 += MAS_MEM[4]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 35
	c_t4_t31_mem1 += MAS_MEM[5]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=2, delay_cost=1)
	S += c_t5_t0_t3 >= 35
	c_t5_t0_t3 += MAS[3]

	c_t5_t21_in = S.Task('c_t5_t21_in', length=1, delay_cost=1)
	S += c_t5_t21_in >= 35
	c_t5_t21_in += MAS_in[1]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 35
	c_t5_t21_mem0 += MAS_MEM[6]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 35
	c_t5_t21_mem1 += MAS_MEM[3]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 36
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 36
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t5_in = S.Task('c_t1_t1_t5_in', length=1, delay_cost=1)
	S += c_t1_t1_t5_in >= 36
	c_t1_t1_t5_in += MAS_in[0]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 36
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 36
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 36
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 36
	c_t1_t4_t0_mem0 += MAS_MEM[4]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 36
	c_t1_t4_t0_mem1 += MAS_MEM[1]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=2, delay_cost=1)
	S += c_t2_t0_t5 >= 36
	c_t2_t0_t5 += MAS[2]

	c_t3_t20_in = S.Task('c_t3_t20_in', length=1, delay_cost=1)
	S += c_t3_t20_in >= 36
	c_t3_t20_in += MAS_in[2]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 36
	c_t3_t20_mem0 += MAS_MEM[0]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 36
	c_t3_t20_mem1 += MAS_MEM[5]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=5, delay_cost=1)
	S += c_t4_t1_t0 >= 36
	c_t4_t1_t0 += MM[0]

	c_t4_t21 = S.Task('c_t4_t21', length=2, delay_cost=1)
	S += c_t4_t21 >= 36
	c_t4_t21 += MAS[0]

	c_t4_t31 = S.Task('c_t4_t31', length=2, delay_cost=1)
	S += c_t4_t31 >= 36
	c_t4_t31 += MAS[3]

	c_t5_t0_t2_in = S.Task('c_t5_t0_t2_in', length=1, delay_cost=1)
	S += c_t5_t0_t2_in >= 36
	c_t5_t0_t2_in += MAS_in[3]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 36
	c_t5_t0_t2_mem0 += MAS_MEM[6]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 36
	c_t5_t0_t2_mem1 += MAS_MEM[7]

	c_t5_t21 = S.Task('c_t5_t21', length=2, delay_cost=1)
	S += c_t5_t21 >= 36
	c_t5_t21 += MAS[1]

	d_t110_in = S.Task('d_t110_in', length=1, delay_cost=1)
	S += d_t110_in >= 36
	d_t110_in += MAS_in[1]

	d_t110_mem0 = S.Task('d_t110_mem0', length=1, delay_cost=1)
	S += d_t110_mem0 >= 36
	d_t110_mem0 += MAS_MEM[2]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 37
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 37
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=2, delay_cost=1)
	S += c_t1_t1_t5 >= 37
	c_t1_t1_t5 += MAS[0]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=5, delay_cost=1)
	S += c_t1_t4_t0 >= 37
	c_t1_t4_t0 += MM[0]

	c_t3_t0_t2_in = S.Task('c_t3_t0_t2_in', length=1, delay_cost=1)
	S += c_t3_t0_t2_in >= 37
	c_t3_t0_t2_in += MAS_in[0]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 37
	c_t3_t0_t2_mem0 += MAS_MEM[0]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 37
	c_t3_t0_t2_mem1 += MAS_MEM[7]

	c_t3_t20 = S.Task('c_t3_t20', length=2, delay_cost=1)
	S += c_t3_t20 >= 37
	c_t3_t20 += MAS[2]

	c_t4_t0_t2_in = S.Task('c_t4_t0_t2_in', length=1, delay_cost=1)
	S += c_t4_t0_t2_in >= 37
	c_t4_t0_t2_in += MAS_in[3]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 37
	c_t4_t0_t2_mem0 += MAS_MEM[2]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 37
	c_t4_t0_t2_mem1 += MAS_MEM[1]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 37
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 37
	c_t4_t1_t1_mem0 += MAS_MEM[6]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 37
	c_t4_t1_t1_mem1 += MAS_MEM[5]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=2, delay_cost=1)
	S += c_t5_t0_t2 >= 37
	c_t5_t0_t2 += MAS[3]

	d_t110 = S.Task('d_t110', length=2, delay_cost=1)
	S += d_t110 >= 37
	d_t110 += MAS[1]

	d_t5_t2_t3_in = S.Task('d_t5_t2_t3_in', length=1, delay_cost=1)
	S += d_t5_t2_t3_in >= 37
	d_t5_t2_t3_in += MAS_in[1]

	d_t5_t2_t3_mem0 = S.Task('d_t5_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t5_t2_t3_mem0 >= 37
	d_t5_t2_t3_mem0 += MAS_MEM[4]

	d_t5_t2_t3_mem1 = S.Task('d_t5_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t5_t2_t3_mem1 >= 37
	d_t5_t2_t3_mem1 += MAS_MEM[3]

	d_t5_t30_in = S.Task('d_t5_t30_in', length=1, delay_cost=1)
	S += d_t5_t30_in >= 37
	d_t5_t30_in += MAS_in[2]

	d_t5_t30_mem0 = S.Task('d_t5_t30_mem0', length=1, delay_cost=1)
	S += d_t5_t30_mem0 >= 37
	d_t5_t30_mem0 += MM_MEM[0]

	d_t5_t30_mem1 = S.Task('d_t5_t30_mem1', length=1, delay_cost=1)
	S += d_t5_t30_mem1 >= 37
	d_t5_t30_mem1 += MM_MEM[1]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 38
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t3_in = S.Task('c_t0_t4_t3_in', length=1, delay_cost=1)
	S += c_t0_t4_t3_in >= 38
	c_t0_t4_t3_in += MAS_in[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 38
	c_t0_t4_t3_mem0 += MAS_MEM[2]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 38
	c_t0_t4_t3_mem1 += MAS_MEM[7]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 38
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 38
	c_t3_t0_t1_in += MM_in[0]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 38
	c_t3_t0_t1_mem0 += MAS_MEM[6]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 38
	c_t3_t0_t1_mem1 += MAS_MEM[5]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=2, delay_cost=1)
	S += c_t3_t0_t2 >= 38
	c_t3_t0_t2 += MAS[0]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=2, delay_cost=1)
	S += c_t4_t0_t2 >= 38
	c_t4_t0_t2 += MAS[3]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=5, delay_cost=1)
	S += c_t4_t1_t1 >= 38
	c_t4_t1_t1 += MM[0]

	c_t5_t31_in = S.Task('c_t5_t31_in', length=1, delay_cost=1)
	S += c_t5_t31_in >= 38
	c_t5_t31_in += MAS_in[0]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 38
	c_t5_t31_mem0 += MAS_MEM[0]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 38
	c_t5_t31_mem1 += MAS_MEM[1]

	d_t4_t3_t5_in = S.Task('d_t4_t3_t5_in', length=1, delay_cost=1)
	S += d_t4_t3_t5_in >= 38
	d_t4_t3_t5_in += MAS_in[2]

	d_t4_t3_t5_mem0 = S.Task('d_t4_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t5_mem0 >= 38
	d_t4_t3_t5_mem0 += MM_MEM[0]

	d_t4_t3_t5_mem1 = S.Task('d_t4_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t5_mem1 >= 38
	d_t4_t3_t5_mem1 += MM_MEM[1]

	d_t5_t2_t3 = S.Task('d_t5_t2_t3', length=2, delay_cost=1)
	S += d_t5_t2_t3 >= 38
	d_t5_t2_t3 += MAS[1]

	d_t5_t30 = S.Task('d_t5_t30', length=2, delay_cost=1)
	S += d_t5_t30 >= 38
	d_t5_t30 += MAS[2]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 39
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 39
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=2, delay_cost=1)
	S += c_t0_t4_t3 >= 39
	c_t0_t4_t3 += MAS[1]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 39
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 39
	c_t2_t4_t0_mem0 += MAS_MEM[2]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 39
	c_t2_t4_t0_mem1 += MAS_MEM[5]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=5, delay_cost=1)
	S += c_t3_t0_t1 >= 39
	c_t3_t0_t1 += MM[0]

	c_t5_t1_t3_in = S.Task('c_t5_t1_t3_in', length=1, delay_cost=1)
	S += c_t5_t1_t3_in >= 39
	c_t5_t1_t3_in += MAS_in[2]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 39
	c_t5_t1_t3_mem0 += MAS_MEM[4]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 39
	c_t5_t1_t3_mem1 += MAS_MEM[1]

	c_t5_t31 = S.Task('c_t5_t31', length=2, delay_cost=1)
	S += c_t5_t31 >= 39
	c_t5_t31 += MAS[0]

	d_t1_t2_t2_in = S.Task('d_t1_t2_t2_in', length=1, delay_cost=1)
	S += d_t1_t2_t2_in >= 39
	d_t1_t2_t2_in += MAS_in[1]

	d_t1_t2_t2_mem0 = S.Task('d_t1_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t2_mem0 >= 39
	d_t1_t2_t2_mem0 += MAS_MEM[0]

	d_t1_t2_t2_mem1 = S.Task('d_t1_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t2_mem1 >= 39
	d_t1_t2_t2_mem1 += MAS_MEM[7]

	d_t3_t00_in = S.Task('d_t3_t00_in', length=1, delay_cost=1)
	S += d_t3_t00_in >= 39
	d_t3_t00_in += MAS_in[3]

	d_t3_t00_mem0 = S.Task('d_t3_t00_mem0', length=1, delay_cost=1)
	S += d_t3_t00_mem0 >= 39
	d_t3_t00_mem0 += MAS_MEM[6]

	d_t3_t00_mem1 = S.Task('d_t3_t00_mem1', length=1, delay_cost=1)
	S += d_t3_t00_mem1 >= 39
	d_t3_t00_mem1 += MAS_MEM[3]

	d_t4_t30_in = S.Task('d_t4_t30_in', length=1, delay_cost=1)
	S += d_t4_t30_in >= 39
	d_t4_t30_in += MAS_in[0]

	d_t4_t30_mem0 = S.Task('d_t4_t30_mem0', length=1, delay_cost=1)
	S += d_t4_t30_mem0 >= 39
	d_t4_t30_mem0 += MM_MEM[0]

	d_t4_t30_mem1 = S.Task('d_t4_t30_mem1', length=1, delay_cost=1)
	S += d_t4_t30_mem1 >= 39
	d_t4_t30_mem1 += MM_MEM[1]

	d_t4_t3_t5 = S.Task('d_t4_t3_t5', length=2, delay_cost=1)
	S += d_t4_t3_t5 >= 39
	d_t4_t3_t5 += MAS[2]

	c_t0_t01_in = S.Task('c_t0_t01_in', length=1, delay_cost=1)
	S += c_t0_t01_in >= 40
	c_t0_t01_in += MAS_in[0]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 40
	c_t0_t01_mem0 += MM_MEM[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 40
	c_t0_t01_mem1 += MAS_MEM[3]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 40
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 40
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=5, delay_cost=1)
	S += c_t2_t4_t0 >= 40
	c_t2_t4_t0 += MM[0]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 40
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 40
	c_t5_t0_t0_mem0 += MAS_MEM[6]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 40
	c_t5_t0_t0_mem1 += MAS_MEM[7]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=2, delay_cost=1)
	S += c_t5_t1_t3 >= 40
	c_t5_t1_t3 += MAS[2]

	d_t1_t2_t2 = S.Task('d_t1_t2_t2', length=2, delay_cost=1)
	S += d_t1_t2_t2 >= 40
	d_t1_t2_t2 += MAS[1]

	d_t210_in = S.Task('d_t210_in', length=1, delay_cost=1)
	S += d_t210_in >= 40
	d_t210_in += MAS_in[1]

	d_t210_mem0 = S.Task('d_t210_mem0', length=1, delay_cost=1)
	S += d_t210_mem0 >= 40
	d_t210_mem0 += MAS_MEM[2]

	d_t3_t00 = S.Task('d_t3_t00', length=2, delay_cost=1)
	S += d_t3_t00 >= 40
	d_t3_t00 += MAS[3]

	d_t3_t2_t3_in = S.Task('d_t3_t2_t3_in', length=1, delay_cost=1)
	S += d_t3_t2_t3_in >= 40
	d_t3_t2_t3_in += MAS_in[2]

	d_t3_t2_t3_mem0 = S.Task('d_t3_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t3_t2_t3_mem0 >= 40
	d_t3_t2_t3_mem0 += MAS_MEM[4]

	d_t3_t2_t3_mem1 = S.Task('d_t3_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t3_t2_t3_mem1 >= 40
	d_t3_t2_t3_mem1 += MAS_MEM[5]

	d_t4_t30 = S.Task('d_t4_t30', length=2, delay_cost=1)
	S += d_t4_t30 >= 40
	d_t4_t30 += MAS[0]

	d_t5_t00_in = S.Task('d_t5_t00_in', length=1, delay_cost=1)
	S += d_t5_t00_in >= 40
	d_t5_t00_in += MAS_in[3]

	d_t5_t00_mem0 = S.Task('d_t5_t00_mem0', length=1, delay_cost=1)
	S += d_t5_t00_mem0 >= 40
	d_t5_t00_mem0 += MAS_MEM[0]

	d_t5_t00_mem1 = S.Task('d_t5_t00_mem1', length=1, delay_cost=1)
	S += d_t5_t00_mem1 >= 40
	d_t5_t00_mem1 += MAS_MEM[1]

	c_t0_t01 = S.Task('c_t0_t01', length=2, delay_cost=1)
	S += c_t0_t01 >= 41
	c_t0_t01 += MAS[0]

	c_t0_t50_in = S.Task('c_t0_t50_in', length=1, delay_cost=1)
	S += c_t0_t50_in >= 41
	c_t0_t50_in += MAS_in[3]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 41
	c_t0_t50_mem0 += MAS_MEM[6]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 41
	c_t0_t50_mem1 += MAS_MEM[3]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 41
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 41
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 41
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 41
	c_t4_t0_t1_mem0 += MAS_MEM[0]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 41
	c_t4_t0_t1_mem1 += MAS_MEM[5]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=5, delay_cost=1)
	S += c_t5_t0_t0 >= 41
	c_t5_t0_t0 += MM[0]

	d_t210 = S.Task('d_t210', length=2, delay_cost=1)
	S += d_t210 >= 41
	d_t210 += MAS[1]

	d_t2_t2_t2_in = S.Task('d_t2_t2_t2_in', length=1, delay_cost=1)
	S += d_t2_t2_t2_in >= 41
	d_t2_t2_t2_in += MAS_in[2]

	d_t2_t2_t2_mem0 = S.Task('d_t2_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t2_mem0 >= 41
	d_t2_t2_t2_mem0 += MAS_MEM[4]

	d_t2_t2_t2_mem1 = S.Task('d_t2_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t2_mem1 >= 41
	d_t2_t2_t2_mem1 += MAS_MEM[1]

	d_t3_t2_t3 = S.Task('d_t3_t2_t3', length=2, delay_cost=1)
	S += d_t3_t2_t3 >= 41
	d_t3_t2_t3 += MAS[2]

	d_t3_t30_in = S.Task('d_t3_t30_in', length=1, delay_cost=1)
	S += d_t3_t30_in >= 41
	d_t3_t30_in += MAS_in[0]

	d_t3_t30_mem0 = S.Task('d_t3_t30_mem0', length=1, delay_cost=1)
	S += d_t3_t30_mem0 >= 41
	d_t3_t30_mem0 += MM_MEM[0]

	d_t3_t30_mem1 = S.Task('d_t3_t30_mem1', length=1, delay_cost=1)
	S += d_t3_t30_mem1 >= 41
	d_t3_t30_mem1 += MM_MEM[1]

	d_t4_t00_in = S.Task('d_t4_t00_in', length=1, delay_cost=1)
	S += d_t4_t00_in >= 41
	d_t4_t00_in += MAS_in[1]

	d_t4_t00_mem0 = S.Task('d_t4_t00_mem0', length=1, delay_cost=1)
	S += d_t4_t00_mem0 >= 41
	d_t4_t00_mem0 += MAS_MEM[2]

	d_t4_t00_mem1 = S.Task('d_t4_t00_mem1', length=1, delay_cost=1)
	S += d_t4_t00_mem1 >= 41
	d_t4_t00_mem1 += MAS_MEM[7]

	d_t5_t00 = S.Task('d_t5_t00', length=2, delay_cost=1)
	S += d_t5_t00 >= 41
	d_t5_t00 += MAS[3]

	c_t0_t50 = S.Task('c_t0_t50', length=2, delay_cost=1)
	S += c_t0_t50 >= 42
	c_t0_t50 += MAS[3]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 42
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 42
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 42
	c_t1_t4_t1_mem0 += MAS_MEM[4]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 42
	c_t1_t4_t1_mem1 += MAS_MEM[7]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=5, delay_cost=1)
	S += c_t4_t0_t1 >= 42
	c_t4_t0_t1 += MM[0]

	c_t5_t30_in = S.Task('c_t5_t30_in', length=1, delay_cost=1)
	S += c_t5_t30_in >= 42
	c_t5_t30_in += MAS_in[2]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 42
	c_t5_t30_mem0 += MAS_MEM[6]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 42
	c_t5_t30_mem1 += MAS_MEM[5]

	d_t010_in = S.Task('d_t010_in', length=1, delay_cost=1)
	S += d_t010_in >= 42
	d_t010_in += MAS_in[1]

	d_t010_mem0 = S.Task('d_t010_mem0', length=1, delay_cost=1)
	S += d_t010_mem0 >= 42
	d_t010_mem0 += MAS_MEM[0]

	d_t2_t2_t2 = S.Task('d_t2_t2_t2', length=2, delay_cost=1)
	S += d_t2_t2_t2 >= 42
	d_t2_t2_t2 += MAS[2]

	d_t2_t31_in = S.Task('d_t2_t31_in', length=1, delay_cost=1)
	S += d_t2_t31_in >= 42
	d_t2_t31_in += MAS_in[0]

	d_t2_t31_mem0 = S.Task('d_t2_t31_mem0', length=1, delay_cost=1)
	S += d_t2_t31_mem0 >= 42
	d_t2_t31_mem0 += MM_MEM[0]

	d_t2_t31_mem1 = S.Task('d_t2_t31_mem1', length=1, delay_cost=1)
	S += d_t2_t31_mem1 >= 42
	d_t2_t31_mem1 += MAS_MEM[3]

	d_t3_t30 = S.Task('d_t3_t30', length=2, delay_cost=1)
	S += d_t3_t30 >= 42
	d_t3_t30 += MAS[0]

	d_t4011_mem0 = S.Task('d_t4011_mem0', length=1, delay_cost=1)
	S += d_t4011_mem0 >= 42
	d_t4011_mem0 += MAIN_MEM_r[0]

	d_t4_t00 = S.Task('d_t4_t00', length=2, delay_cost=1)
	S += d_t4_t00 >= 42
	d_t4_t00 += MAS[1]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 43
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t0_t40_in = S.Task('c_t0_t40_in', length=1, delay_cost=1)
	S += c_t0_t40_in >= 43
	c_t0_t40_in += MAS_in[0]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 43
	c_t0_t40_mem0 += MM_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 43
	c_t0_t40_mem1 += MM_MEM[1]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 43
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 43
	c_t1_t1_t4_mem0 += MAS_MEM[0]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 43
	c_t1_t1_t4_mem1 += MAS_MEM[7]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=5, delay_cost=1)
	S += c_t1_t4_t1 >= 43
	c_t1_t4_t1 += MM[0]

	c_t2_t50_in = S.Task('c_t2_t50_in', length=1, delay_cost=1)
	S += c_t2_t50_in >= 43
	c_t2_t50_in += MAS_in[1]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 43
	c_t2_t50_mem0 += MAS_MEM[2]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 43
	c_t2_t50_mem1 += MAS_MEM[3]

	c_t4_t4_t2_in = S.Task('c_t4_t4_t2_in', length=1, delay_cost=1)
	S += c_t4_t4_t2_in >= 43
	c_t4_t4_t2_in += MAS_in[2]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem0 >= 43
	c_t4_t4_t2_mem0 += MAS_MEM[4]

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem1 >= 43
	c_t4_t4_t2_mem1 += MAS_MEM[1]

	c_t5_t20_in = S.Task('c_t5_t20_in', length=1, delay_cost=1)
	S += c_t5_t20_in >= 43
	c_t5_t20_in += MAS_in[3]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 43
	c_t5_t20_mem0 += MAS_MEM[6]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 43
	c_t5_t20_mem1 += MAS_MEM[5]

	c_t5_t30 = S.Task('c_t5_t30', length=2, delay_cost=1)
	S += c_t5_t30 >= 43
	c_t5_t30 += MAS[2]

	d_t010 = S.Task('d_t010', length=2, delay_cost=1)
	S += d_t010 >= 43
	d_t010 += MAS[1]

	d_t2_t31 = S.Task('d_t2_t31', length=2, delay_cost=1)
	S += d_t2_t31 >= 43
	d_t2_t31 += MAS[0]

	d_t5011_mem1 = S.Task('d_t5011_mem1', length=1, delay_cost=1)
	S += d_t5011_mem1 >= 43
	d_t5011_mem1 += MAIN_MEM_r[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 44
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t0_t40 = S.Task('c_t0_t40', length=2, delay_cost=1)
	S += c_t0_t40 >= 44
	c_t0_t40 += MAS[0]

	c_t0_t4_t5_in = S.Task('c_t0_t4_t5_in', length=1, delay_cost=1)
	S += c_t0_t4_t5_in >= 44
	c_t0_t4_t5_in += MAS_in[3]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem0 >= 44
	c_t0_t4_t5_mem0 += MM_MEM[0]

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem1 >= 44
	c_t0_t4_t5_mem1 += MM_MEM[1]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 44
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=5, delay_cost=1)
	S += c_t1_t1_t4 >= 44
	c_t1_t1_t4 += MM[0]

	c_t1_t50_in = S.Task('c_t1_t50_in', length=1, delay_cost=1)
	S += c_t1_t50_in >= 44
	c_t1_t50_in += MAS_in[0]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 44
	c_t1_t50_mem0 += MAS_MEM[2]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 44
	c_t1_t50_mem1 += MAS_MEM[5]

	c_t2_t50 = S.Task('c_t2_t50', length=2, delay_cost=1)
	S += c_t2_t50 >= 44
	c_t2_t50 += MAS[1]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 44
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 44
	c_t3_t1_t1_mem0 += MAS_MEM[0]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 44
	c_t3_t1_t1_mem1 += MAS_MEM[7]

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=2, delay_cost=1)
	S += c_t4_t4_t2 >= 44
	c_t4_t4_t2 += MAS[2]

	c_t5_t20 = S.Task('c_t5_t20', length=2, delay_cost=1)
	S += c_t5_t20 >= 44
	c_t5_t20 += MAS[3]

	d_t4_t01_in = S.Task('d_t4_t01_in', length=1, delay_cost=1)
	S += d_t4_t01_in >= 44
	d_t4_t01_in += MAS_in[2]

	d_t4_t01_mem0 = S.Task('d_t4_t01_mem0', length=1, delay_cost=1)
	S += d_t4_t01_mem0 >= 44
	d_t4_t01_mem0 += MAS_MEM[6]

	d_t4_t01_mem1 = S.Task('d_t4_t01_mem1', length=1, delay_cost=1)
	S += d_t4_t01_mem1 >= 44
	d_t4_t01_mem1 += MAS_MEM[1]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 45
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=2, delay_cost=1)
	S += c_t0_t4_t5 >= 45
	c_t0_t4_t5 += MAS[3]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 45
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t50 = S.Task('c_t1_t50', length=2, delay_cost=1)
	S += c_t1_t50 >= 45
	c_t1_t50 += MAS[0]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 45
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 45
	c_t2_t1_t4_mem0 += MAS_MEM[0]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 45
	c_t2_t1_t4_mem1 += MAS_MEM[7]

	c_t2_t4_t5_in = S.Task('c_t2_t4_t5_in', length=1, delay_cost=1)
	S += c_t2_t4_t5_in >= 45
	c_t2_t4_t5_in += MAS_in[0]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem0 >= 45
	c_t2_t4_t5_mem0 += MM_MEM[0]

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem1 >= 45
	c_t2_t4_t5_mem1 += MM_MEM[1]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=5, delay_cost=1)
	S += c_t3_t1_t1 >= 45
	c_t3_t1_t1 += MM[0]

	c_t5_t4_t3_in = S.Task('c_t5_t4_t3_in', length=1, delay_cost=1)
	S += c_t5_t4_t3_in >= 45
	c_t5_t4_t3_in += MAS_in[2]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem0 >= 45
	c_t5_t4_t3_mem0 += MAS_MEM[4]

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem1 >= 45
	c_t5_t4_t3_mem1 += MAS_MEM[1]

	d_t0_t2_t2_in = S.Task('d_t0_t2_t2_in', length=1, delay_cost=1)
	S += d_t0_t2_t2_in >= 45
	d_t0_t2_t2_in += MAS_in[3]

	d_t0_t2_t2_mem0 = S.Task('d_t0_t2_t2_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t2_mem0 >= 45
	d_t0_t2_t2_mem0 += MAS_MEM[6]

	d_t0_t2_t2_mem1 = S.Task('d_t0_t2_t2_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t2_mem1 >= 45
	d_t0_t2_t2_mem1 += MAS_MEM[3]

	d_t4_t01 = S.Task('d_t4_t01', length=2, delay_cost=1)
	S += d_t4_t01 >= 45
	d_t4_t01 += MAS[2]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 46
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 46
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=5, delay_cost=1)
	S += c_t2_t1_t4 >= 46
	c_t2_t1_t4 += MM[0]

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=2, delay_cost=1)
	S += c_t2_t4_t5 >= 46
	c_t2_t4_t5 += MAS[0]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 46
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 46
	c_t3_t1_t0_mem0 += MAS_MEM[4]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 46
	c_t3_t1_t0_mem1 += MAS_MEM[7]

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=2, delay_cost=1)
	S += c_t5_t4_t3 >= 46
	c_t5_t4_t3 += MAS[2]

	d_t0_t2_t2 = S.Task('d_t0_t2_t2', length=2, delay_cost=1)
	S += d_t0_t2_t2 >= 46
	d_t0_t2_t2 += MAS[3]

	d_t0_t31_in = S.Task('d_t0_t31_in', length=1, delay_cost=1)
	S += d_t0_t31_in >= 46
	d_t0_t31_in += MAS_in[3]

	d_t0_t31_mem0 = S.Task('d_t0_t31_mem0', length=1, delay_cost=1)
	S += d_t0_t31_mem0 >= 46
	d_t0_t31_mem0 += MM_MEM[0]

	d_t0_t31_mem1 = S.Task('d_t0_t31_mem1', length=1, delay_cost=1)
	S += d_t0_t31_mem1 >= 46
	d_t0_t31_mem1 += MAS_MEM[3]

	d_t3_t01_in = S.Task('d_t3_t01_in', length=1, delay_cost=1)
	S += d_t3_t01_in >= 46
	d_t3_t01_in += MAS_in[2]

	d_t3_t01_mem0 = S.Task('d_t3_t01_mem0', length=1, delay_cost=1)
	S += d_t3_t01_mem0 >= 46
	d_t3_t01_mem0 += MAS_MEM[6]

	d_t3_t01_mem1 = S.Task('d_t3_t01_mem1', length=1, delay_cost=1)
	S += d_t3_t01_mem1 >= 46
	d_t3_t01_mem1 += MAS_MEM[5]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 47
	c_t3_t0_t0_in += MM_in[0]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 47
	c_t3_t0_t0_mem0 += MAS_MEM[0]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 47
	c_t3_t0_t0_mem1 += MAS_MEM[1]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=5, delay_cost=1)
	S += c_t3_t1_t0 >= 47
	c_t3_t1_t0 += MM[0]

	d_t0_t31 = S.Task('d_t0_t31', length=2, delay_cost=1)
	S += d_t0_t31 >= 47
	d_t0_t31 += MAS[3]

	d_t3_t01 = S.Task('d_t3_t01', length=2, delay_cost=1)
	S += d_t3_t01 >= 47
	d_t3_t01 += MAS[2]

	d_t4_t2_t3_in = S.Task('d_t4_t2_t3_in', length=1, delay_cost=1)
	S += d_t4_t2_t3_in >= 47
	d_t4_t2_t3_in += MAS_in[0]

	d_t4_t2_t3_mem0 = S.Task('d_t4_t2_t3_mem0', length=1, delay_cost=1)
	S += d_t4_t2_t3_mem0 >= 47
	d_t4_t2_t3_mem0 += MAS_MEM[6]

	d_t4_t2_t3_mem1 = S.Task('d_t4_t2_t3_mem1', length=1, delay_cost=1)
	S += d_t4_t2_t3_mem1 >= 47
	d_t4_t2_t3_mem1 += MAS_MEM[7]

	d_t5000_mem1 = S.Task('d_t5000_mem1', length=1, delay_cost=1)
	S += d_t5000_mem1 >= 47
	d_t5000_mem1 += MAIN_MEM_r[1]

	d_t5011_mem0 = S.Task('d_t5011_mem0', length=1, delay_cost=1)
	S += d_t5011_mem0 >= 47
	d_t5011_mem0 += MAIN_MEM_r[0]

	d_t5_t3_t5_in = S.Task('d_t5_t3_t5_in', length=1, delay_cost=1)
	S += d_t5_t3_t5_in >= 47
	d_t5_t3_t5_in += MAS_in[3]

	d_t5_t3_t5_mem0 = S.Task('d_t5_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t5_mem0 >= 47
	d_t5_t3_t5_mem0 += MM_MEM[0]

	d_t5_t3_t5_mem1 = S.Task('d_t5_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t5_mem1 >= 47
	d_t5_t3_t5_mem1 += MM_MEM[1]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 48
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 48
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t40_in = S.Task('c_t1_t40_in', length=1, delay_cost=1)
	S += c_t1_t40_in >= 48
	c_t1_t40_in += MAS_in[3]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 48
	c_t1_t40_mem0 += MM_MEM[0]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 48
	c_t1_t40_mem1 += MM_MEM[1]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=5, delay_cost=1)
	S += c_t3_t0_t0 >= 48
	c_t3_t0_t0 += MM[0]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 48
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 48
	c_t5_t0_t1_mem0 += MAS_MEM[6]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 48
	c_t5_t0_t1_mem1 += MAS_MEM[1]

	d_t4_t2_t3 = S.Task('d_t4_t2_t3', length=2, delay_cost=1)
	S += d_t4_t2_t3 >= 48
	d_t4_t2_t3 += MAS[0]

	d_t5_t01_in = S.Task('d_t5_t01_in', length=1, delay_cost=1)
	S += d_t5_t01_in >= 48
	d_t5_t01_in += MAS_in[2]

	d_t5_t01_mem0 = S.Task('d_t5_t01_mem0', length=1, delay_cost=1)
	S += d_t5_t01_mem0 >= 48
	d_t5_t01_mem0 += MAS_MEM[2]

	d_t5_t01_mem1 = S.Task('d_t5_t01_mem1', length=1, delay_cost=1)
	S += d_t5_t01_mem1 >= 48
	d_t5_t01_mem1 += MAS_MEM[7]

	d_t5_t3_t5 = S.Task('d_t5_t3_t5', length=2, delay_cost=1)
	S += d_t5_t3_t5 >= 48
	d_t5_t3_t5 += MAS[3]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 49
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t40 = S.Task('c_t1_t40', length=2, delay_cost=1)
	S += c_t1_t40 >= 49
	c_t1_t40 += MAS[3]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=5, delay_cost=1)
	S += c_t5_t0_t1 >= 49
	c_t5_t0_t1 += MM[0]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 49
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 49
	c_t5_t1_t0_mem0 += MAS_MEM[4]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 49
	c_t5_t1_t0_mem1 += MAS_MEM[5]

	c_t5_t4_t2_in = S.Task('c_t5_t4_t2_in', length=1, delay_cost=1)
	S += c_t5_t4_t2_in >= 49
	c_t5_t4_t2_in += MAS_in[0]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem0 >= 49
	c_t5_t4_t2_mem0 += MAS_MEM[6]

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem1 >= 49
	c_t5_t4_t2_mem1 += MAS_MEM[3]

	d_t1_t31_in = S.Task('d_t1_t31_in', length=1, delay_cost=1)
	S += d_t1_t31_in >= 49
	d_t1_t31_in += MAS_in[1]

	d_t1_t31_mem0 = S.Task('d_t1_t31_mem0', length=1, delay_cost=1)
	S += d_t1_t31_mem0 >= 49
	d_t1_t31_mem0 += MM_MEM[0]

	d_t1_t31_mem1 = S.Task('d_t1_t31_mem1', length=1, delay_cost=1)
	S += d_t1_t31_mem1 >= 49
	d_t1_t31_mem1 += MAS_MEM[7]

	d_t5010_mem1 = S.Task('d_t5010_mem1', length=1, delay_cost=1)
	S += d_t5010_mem1 >= 49
	d_t5010_mem1 += MAIN_MEM_r[1]

	d_t5_t01 = S.Task('d_t5_t01', length=2, delay_cost=1)
	S += d_t5_t01 >= 49
	d_t5_t01 += MAS[2]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 50
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t5_in = S.Task('c_t1_t4_t5_in', length=1, delay_cost=1)
	S += c_t1_t4_t5_in >= 50
	c_t1_t4_t5_in += MAS_in[1]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem0 >= 50
	c_t1_t4_t5_mem0 += MM_MEM[0]

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem1 >= 50
	c_t1_t4_t5_mem1 += MM_MEM[1]

	c_t3_t4_t3_in = S.Task('c_t3_t4_t3_in', length=1, delay_cost=1)
	S += c_t3_t4_t3_in >= 50
	c_t3_t4_t3_in += MAS_in[0]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem0 >= 50
	c_t3_t4_t3_mem0 += MAS_MEM[6]

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem1 >= 50
	c_t3_t4_t3_mem1 += MAS_MEM[5]

	c_t4_t4_t3_in = S.Task('c_t4_t4_t3_in', length=1, delay_cost=1)
	S += c_t4_t4_t3_in >= 50
	c_t4_t4_t3_in += MAS_in[3]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem0 >= 50
	c_t4_t4_t3_mem0 += MAS_MEM[4]

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem1 >= 50
	c_t4_t4_t3_mem1 += MAS_MEM[7]

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

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=2, delay_cost=1)
	S += c_t5_t4_t2 >= 50
	c_t5_t4_t2 += MAS[0]

	d_t1_t31 = S.Task('d_t1_t31', length=2, delay_cost=1)
	S += d_t1_t31 >= 50
	d_t1_t31 += MAS[1]

	d_t5010_mem0 = S.Task('d_t5010_mem0', length=1, delay_cost=1)
	S += d_t5010_mem0 >= 50
	d_t5010_mem0 += MAIN_MEM_r[0]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 51
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 51
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=2, delay_cost=1)
	S += c_t1_t4_t5 >= 51
	c_t1_t4_t5 += MAS[1]

	c_t2_t01_in = S.Task('c_t2_t01_in', length=1, delay_cost=1)
	S += c_t2_t01_in >= 51
	c_t2_t01_in += MAS_in[0]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 51
	c_t2_t01_mem0 += MM_MEM[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 51
	c_t2_t01_mem1 += MAS_MEM[5]

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=2, delay_cost=1)
	S += c_t3_t4_t3 >= 51
	c_t3_t4_t3 += MAS[0]

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=2, delay_cost=1)
	S += c_t4_t4_t3 >= 51
	c_t4_t4_t3 += MAS[3]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=5, delay_cost=1)
	S += c_t5_t1_t1 >= 51
	c_t5_t1_t1 += MM[0]

	d_t3_t3_t4_in = S.Task('d_t3_t3_t4_in', length=1, delay_cost=1)
	S += d_t3_t3_t4_in >= 51
	d_t3_t3_t4_in += MM_in[0]

	d_t3_t3_t4_mem0 = S.Task('d_t3_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t4_mem0 >= 51
	d_t3_t3_t4_mem0 += MAS_MEM[2]

	d_t3_t3_t4_mem1 = S.Task('d_t3_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t4_mem1 >= 51
	d_t3_t3_t4_mem1 += MAS_MEM[1]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 52
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t2_t01 = S.Task('c_t2_t01', length=2, delay_cost=1)
	S += c_t2_t01 >= 52
	c_t2_t01 += MAS[0]

	c_t2_t40_in = S.Task('c_t2_t40_in', length=1, delay_cost=1)
	S += c_t2_t40_in >= 52
	c_t2_t40_in += MAS_in[3]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 52
	c_t2_t40_mem0 += MM_MEM[0]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 52
	c_t2_t40_mem1 += MM_MEM[1]

	c_t3_t4_t2_in = S.Task('c_t3_t4_t2_in', length=1, delay_cost=1)
	S += c_t3_t4_t2_in >= 52
	c_t3_t4_t2_in += MAS_in[2]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem0 >= 52
	c_t3_t4_t2_mem0 += MAS_MEM[4]

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem1 >= 52
	c_t3_t4_t2_mem1 += MAS_MEM[1]

	d_t2_t2_t1_in = S.Task('d_t2_t2_t1_in', length=1, delay_cost=1)
	S += d_t2_t2_t1_in >= 52
	d_t2_t2_t1_in += MM_in[0]

	d_t2_t2_t1_mem0 = S.Task('d_t2_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t1_mem0 >= 52
	d_t2_t2_t1_mem0 += MAS_MEM[0]

	d_t2_t2_t1_mem1 = S.Task('d_t2_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t1_mem1 >= 52
	d_t2_t2_t1_mem1 += MAS_MEM[5]

	d_t3_t3_t4 = S.Task('d_t3_t3_t4', length=5, delay_cost=1)
	S += d_t3_t3_t4 >= 52
	d_t3_t3_t4 += MM[0]

	d_t5001_mem0 = S.Task('d_t5001_mem0', length=1, delay_cost=1)
	S += d_t5001_mem0 >= 52
	d_t5001_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 53
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t01_in = S.Task('c_t1_t01_in', length=1, delay_cost=1)
	S += c_t1_t01_in >= 53
	c_t1_t01_in += MAS_in[3]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 53
	c_t1_t01_mem0 += MM_MEM[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 53
	c_t1_t01_mem1 += MAS_MEM[1]

	c_t2_t40 = S.Task('c_t2_t40', length=2, delay_cost=1)
	S += c_t2_t40 >= 53
	c_t2_t40 += MAS[3]

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=2, delay_cost=1)
	S += c_t3_t4_t2 >= 53
	c_t3_t4_t2 += MAS[2]

	d_t0_t2_t0_in = S.Task('d_t0_t2_t0_in', length=1, delay_cost=1)
	S += d_t0_t2_t0_in >= 53
	d_t0_t2_t0_in += MM_in[0]

	d_t0_t2_t0_mem0 = S.Task('d_t0_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t0_mem0 >= 53
	d_t0_t2_t0_mem0 += MAS_MEM[6]

	d_t0_t2_t0_mem1 = S.Task('d_t0_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t0_mem1 >= 53
	d_t0_t2_t0_mem1 += MAS_MEM[3]

	d_t2_t2_t1 = S.Task('d_t2_t2_t1', length=5, delay_cost=1)
	S += d_t2_t2_t1 >= 53
	d_t2_t2_t1 += MM[0]

	d_t5000_mem0 = S.Task('d_t5000_mem0', length=1, delay_cost=1)
	S += d_t5000_mem0 >= 53
	d_t5000_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 54
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 54
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t01 = S.Task('c_t1_t01', length=2, delay_cost=1)
	S += c_t1_t01 >= 54
	c_t1_t01 += MAS[3]

	c_t1_t11_in = S.Task('c_t1_t11_in', length=1, delay_cost=1)
	S += c_t1_t11_in >= 54
	c_t1_t11_in += MAS_in[2]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 54
	c_t1_t11_mem0 += MM_MEM[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 54
	c_t1_t11_mem1 += MAS_MEM[1]

	d_t0_t2_t0 = S.Task('d_t0_t2_t0', length=5, delay_cost=1)
	S += d_t0_t2_t0 >= 54
	d_t0_t2_t0 += MM[0]

	d_t5_t3_t4_in = S.Task('d_t5_t3_t4_in', length=1, delay_cost=1)
	S += d_t5_t3_t4_in >= 54
	d_t5_t3_t4_in += MM_in[0]

	d_t5_t3_t4_mem0 = S.Task('d_t5_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t5_t3_t4_mem0 >= 54
	d_t5_t3_t4_mem0 += MAS_MEM[4]

	d_t5_t3_t4_mem1 = S.Task('d_t5_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t5_t3_t4_mem1 >= 54
	d_t5_t3_t4_mem1 += MAS_MEM[5]

	c_t1_t11 = S.Task('c_t1_t11', length=2, delay_cost=1)
	S += c_t1_t11 >= 55
	c_t1_t11 += MAS[2]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 55
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 55
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t11_in = S.Task('c_t2_t11_in', length=1, delay_cost=1)
	S += c_t2_t11_in >= 55
	c_t2_t11_in += MAS_in[1]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 55
	c_t2_t11_mem0 += MM_MEM[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 55
	c_t2_t11_mem1 += MAS_MEM[1]

	d_t2_t2_t0_in = S.Task('d_t2_t2_t0_in', length=1, delay_cost=1)
	S += d_t2_t2_t0_in >= 55
	d_t2_t2_t0_in += MM_in[0]

	d_t2_t2_t0_mem0 = S.Task('d_t2_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t2_t2_t0_mem0 >= 55
	d_t2_t2_t0_mem0 += MAS_MEM[4]

	d_t2_t2_t0_mem1 = S.Task('d_t2_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t2_t2_t0_mem1 >= 55
	d_t2_t2_t0_mem1 += MAS_MEM[7]

	d_t5_t3_t4 = S.Task('d_t5_t3_t4', length=5, delay_cost=1)
	S += d_t5_t3_t4 >= 55
	d_t5_t3_t4 += MM[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 56
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t11 = S.Task('c_t2_t11', length=2, delay_cost=1)
	S += c_t2_t11 >= 56
	c_t2_t11 += MAS[1]

	d_t1_t2_t0_in = S.Task('d_t1_t2_t0_in', length=1, delay_cost=1)
	S += d_t1_t2_t0_in >= 56
	d_t1_t2_t0_in += MM_in[0]

	d_t1_t2_t0_mem0 = S.Task('d_t1_t2_t0_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t0_mem0 >= 56
	d_t1_t2_t0_mem0 += MAS_MEM[0]

	d_t1_t2_t0_mem1 = S.Task('d_t1_t2_t0_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t0_mem1 >= 56
	d_t1_t2_t0_mem1 += MAS_MEM[7]

	d_t2_t2_t0 = S.Task('d_t2_t2_t0', length=5, delay_cost=1)
	S += d_t2_t2_t0 >= 56
	d_t2_t2_t0 += MM[0]

	d_t3_t3_t5_in = S.Task('d_t3_t3_t5_in', length=1, delay_cost=1)
	S += d_t3_t3_t5_in >= 56
	d_t3_t3_t5_in += MAS_in[1]

	d_t3_t3_t5_mem0 = S.Task('d_t3_t3_t5_mem0', length=1, delay_cost=1)
	S += d_t3_t3_t5_mem0 >= 56
	d_t3_t3_t5_mem0 += MM_MEM[0]

	d_t3_t3_t5_mem1 = S.Task('d_t3_t3_t5_mem1', length=1, delay_cost=1)
	S += d_t3_t3_t5_mem1 >= 56
	d_t3_t3_t5_mem1 += MM_MEM[1]

	d_t4010_mem1 = S.Task('d_t4010_mem1', length=1, delay_cost=1)
	S += d_t4010_mem1 >= 56
	d_t4010_mem1 += MAIN_MEM_r[1]

	c_t0_t11_in = S.Task('c_t0_t11_in', length=1, delay_cost=1)
	S += c_t0_t11_in >= 57
	c_t0_t11_in += MAS_in[3]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 57
	c_t0_t11_mem0 += MM_MEM[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 57
	c_t0_t11_mem1 += MAS_MEM[1]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 57
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 57
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	S += c_t2_t4_t4_in >= 57
	c_t2_t4_t4_in += MM_in[0]

	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem0 >= 57
	c_t2_t4_t4_mem0 += MAS_MEM[0]

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem1 >= 57
	c_t2_t4_t4_mem1 += MAS_MEM[5]

	d_t1_t2_t0 = S.Task('d_t1_t2_t0', length=5, delay_cost=1)
	S += d_t1_t2_t0 >= 57
	d_t1_t2_t0 += MM[0]

	d_t3_t3_t5 = S.Task('d_t3_t3_t5', length=2, delay_cost=1)
	S += d_t3_t3_t5 >= 57
	d_t3_t3_t5 += MAS[1]

	c_t0_t11 = S.Task('c_t0_t11', length=2, delay_cost=1)
	S += c_t0_t11 >= 58
	c_t0_t11 += MAS[3]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 58
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 58
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=5, delay_cost=1)
	S += c_t2_t4_t4 >= 58
	c_t2_t4_t4 += MM[0]

	c_t5_t00_in = S.Task('c_t5_t00_in', length=1, delay_cost=1)
	S += c_t5_t00_in >= 58
	c_t5_t00_in += MAS_in[3]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 58
	c_t5_t00_mem0 += MM_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 58
	c_t5_t00_mem1 += MM_MEM[1]

	d_t0_t2_t1_in = S.Task('d_t0_t2_t1_in', length=1, delay_cost=1)
	S += d_t0_t2_t1_in >= 58
	d_t0_t2_t1_in += MM_in[0]

	d_t0_t2_t1_mem0 = S.Task('d_t0_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t0_t2_t1_mem0 >= 58
	d_t0_t2_t1_mem0 += MAS_MEM[2]

	d_t0_t2_t1_mem1 = S.Task('d_t0_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t0_t2_t1_mem1 >= 58
	d_t0_t2_t1_mem1 += MAS_MEM[1]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 59
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t3_t10_in = S.Task('c_t3_t10_in', length=1, delay_cost=1)
	S += c_t3_t10_in >= 59
	c_t3_t10_in += MAS_in[2]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 59
	c_t3_t10_mem0 += MM_MEM[0]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 59
	c_t3_t10_mem1 += MM_MEM[1]

	c_t5_t00 = S.Task('c_t5_t00', length=2, delay_cost=1)
	S += c_t5_t00 >= 59
	c_t5_t00 += MAS[3]

	d_t0_t2_t1 = S.Task('d_t0_t2_t1', length=5, delay_cost=1)
	S += d_t0_t2_t1 >= 59
	d_t0_t2_t1 += MM[0]

	d_t1_t2_t1_in = S.Task('d_t1_t2_t1_in', length=1, delay_cost=1)
	S += d_t1_t2_t1_in >= 59
	d_t1_t2_t1_in += MM_in[0]

	d_t1_t2_t1_mem0 = S.Task('d_t1_t2_t1_mem0', length=1, delay_cost=1)
	S += d_t1_t2_t1_mem0 >= 59
	d_t1_t2_t1_mem0 += MAS_MEM[6]

	d_t1_t2_t1_mem1 = S.Task('d_t1_t2_t1_mem1', length=1, delay_cost=1)
	S += d_t1_t2_t1_mem1 >= 59
	d_t1_t2_t1_mem1 += MAS_MEM[5]

	d_t4011_mem1 = S.Task('d_t4011_mem1', length=1, delay_cost=1)
	S += d_t4011_mem1 >= 59
	d_t4011_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 60
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t3_t10 = S.Task('c_t3_t10', length=2, delay_cost=1)
	S += c_t3_t10 >= 60
	c_t3_t10 += MAS[2]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 60
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t5_in = S.Task('c_t5_t0_t5_in', length=1, delay_cost=1)
	S += c_t5_t0_t5_in >= 60
	c_t5_t0_t5_in += MAS_in[1]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem0 >= 60
	c_t5_t0_t5_mem0 += MM_MEM[0]

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem1 >= 60
	c_t5_t0_t5_mem1 += MM_MEM[1]

	d_t1_t2_t1 = S.Task('d_t1_t2_t1', length=5, delay_cost=1)
	S += d_t1_t2_t1 >= 60
	d_t1_t2_t1 += MM[0]

	d_t4_t3_t4_in = S.Task('d_t4_t3_t4_in', length=1, delay_cost=1)
	S += d_t4_t3_t4_in >= 60
	d_t4_t3_t4_in += MM_in[0]

	d_t4_t3_t4_mem0 = S.Task('d_t4_t3_t4_mem0', length=1, delay_cost=1)
	S += d_t4_t3_t4_mem0 >= 60
	d_t4_t3_t4_mem0 += MAS_MEM[6]

	d_t4_t3_t4_mem1 = S.Task('d_t4_t3_t4_mem1', length=1, delay_cost=1)
	S += d_t4_t3_t4_mem1 >= 60
	d_t4_t3_t4_mem1 += MAS_MEM[1]

	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	S += c_t0_t4_t4_in >= 61
	c_t0_t4_t4_in += MM_in[0]

	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem0 >= 61
	c_t0_t4_t4_mem0 += MAS_MEM[4]

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem1 >= 61
	c_t0_t4_t4_mem1 += MAS_MEM[3]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 61
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t4_t0_t5_in = S.Task('c_t4_t0_t5_in', length=1, delay_cost=1)
	S += c_t4_t0_t5_in >= 61
	c_t4_t0_t5_in += MAS_in[2]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem0 >= 61
	c_t4_t0_t5_mem0 += MM_MEM[0]

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem1 >= 61
	c_t4_t0_t5_mem1 += MM_MEM[1]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 61
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=2, delay_cost=1)
	S += c_t5_t0_t5 >= 61
	c_t5_t0_t5 += MAS[1]

	d_t4_t3_t4 = S.Task('d_t4_t3_t4', length=5, delay_cost=1)
	S += d_t4_t3_t4 >= 61
	d_t4_t3_t4 += MM[0]

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=5, delay_cost=1)
	S += c_t0_t4_t4 >= 62
	c_t0_t4_t4 += MM[0]

	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	S += c_t1_t4_t4_in >= 62
	c_t1_t4_t4_in += MM_in[0]

	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem0 >= 62
	c_t1_t4_t4_mem0 += MAS_MEM[6]

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem1 >= 62
	c_t1_t4_t4_mem1 += MAS_MEM[3]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 62
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 62
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t4_t00_in = S.Task('c_t4_t00_in', length=1, delay_cost=1)
	S += c_t4_t00_in >= 62
	c_t4_t00_in += MAS_in[2]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 62
	c_t4_t00_mem0 += MM_MEM[0]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 62
	c_t4_t00_mem1 += MM_MEM[1]

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=2, delay_cost=1)
	S += c_t4_t0_t5 >= 62
	c_t4_t0_t5 += MAS[2]

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=5, delay_cost=1)
	S += c_t1_t4_t4 >= 63
	c_t1_t4_t4 += MM[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 63
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 63
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t5_in = S.Task('c_t3_t0_t5_in', length=1, delay_cost=1)
	S += c_t3_t0_t5_in >= 63
	c_t3_t0_t5_in += MAS_in[2]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem0 >= 63
	c_t3_t0_t5_mem0 += MM_MEM[0]

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem1 >= 63
	c_t3_t0_t5_mem1 += MM_MEM[1]

	c_t4_t00 = S.Task('c_t4_t00', length=2, delay_cost=1)
	S += c_t4_t00 >= 63
	c_t4_t00 += MAS[2]

	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	S += c_t5_t4_t0_in >= 63
	c_t5_t4_t0_in += MM_in[0]

	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem0 >= 63
	c_t5_t4_t0_mem0 += MAS_MEM[6]

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem1 >= 63
	c_t5_t4_t0_mem1 += MAS_MEM[5]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 64
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 64
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=2, delay_cost=1)
	S += c_t3_t0_t5 >= 64
	c_t3_t0_t5 += MAS[2]

	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	S += c_t3_t4_t0_in >= 64
	c_t3_t4_t0_in += MM_in[0]

	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem0 >= 64
	c_t3_t4_t0_mem0 += MAS_MEM[4]

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem1 >= 64
	c_t3_t4_t0_mem1 += MAS_MEM[7]

	c_t5_t1_t5_in = S.Task('c_t5_t1_t5_in', length=1, delay_cost=1)
	S += c_t5_t1_t5_in >= 64
	c_t5_t1_t5_in += MAS_in[1]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem0 >= 64
	c_t5_t1_t5_mem0 += MM_MEM[0]

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem1 >= 64
	c_t5_t1_t5_mem1 += MM_MEM[1]

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=5, delay_cost=1)
	S += c_t5_t4_t0 >= 64
	c_t5_t4_t0 += MM[0]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 65
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 65
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3_t1_t5_in = S.Task('c_t3_t1_t5_in', length=1, delay_cost=1)
	S += c_t3_t1_t5_in >= 65
	c_t3_t1_t5_in += MAS_in[2]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem0 >= 65
	c_t3_t1_t5_mem0 += MM_MEM[0]

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem1 >= 65
	c_t3_t1_t5_mem1 += MM_MEM[1]

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=5, delay_cost=1)
	S += c_t3_t4_t0 >= 65
	c_t3_t4_t0 += MM[0]

	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	S += c_t4_t0_t4_in >= 65
	c_t4_t0_t4_in += MM_in[0]

	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem0 >= 65
	c_t4_t0_t4_mem0 += MAS_MEM[6]

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem1 >= 65
	c_t4_t0_t4_mem1 += MAS_MEM[3]

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=2, delay_cost=1)
	S += c_t5_t1_t5 >= 65
	c_t5_t1_t5 += MAS[1]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 66
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=2, delay_cost=1)
	S += c_t3_t1_t5 >= 66
	c_t3_t1_t5 += MAS[2]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 66
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=5, delay_cost=1)
	S += c_t4_t0_t4 >= 66
	c_t4_t0_t4 += MM[0]

	c_t5_t10_in = S.Task('c_t5_t10_in', length=1, delay_cost=1)
	S += c_t5_t10_in >= 66
	c_t5_t10_in += MAS_in[3]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 66
	c_t5_t10_mem0 += MM_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 66
	c_t5_t10_mem1 += MM_MEM[1]

	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	S += c_t5_t4_t1_in >= 66
	c_t5_t4_t1_in += MM_in[0]

	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem0 >= 66
	c_t5_t4_t1_mem0 += MAS_MEM[2]

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem1 >= 66
	c_t5_t4_t1_mem1 += MAS_MEM[1]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 67
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	S += c_t3_t0_t4_in >= 67
	c_t3_t0_t4_in += MM_in[0]

	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem0 >= 67
	c_t3_t0_t4_mem0 += MAS_MEM[0]

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem1 >= 67
	c_t3_t0_t4_mem1 += MAS_MEM[1]

	c_t4_t10_in = S.Task('c_t4_t10_in', length=1, delay_cost=1)
	S += c_t4_t10_in >= 67
	c_t4_t10_in += MAS_in[2]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 67
	c_t4_t10_mem0 += MM_MEM[0]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 67
	c_t4_t10_mem1 += MM_MEM[1]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 67
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5_t10 = S.Task('c_t5_t10', length=2, delay_cost=1)
	S += c_t5_t10 >= 67
	c_t5_t10 += MAS[3]

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=5, delay_cost=1)
	S += c_t5_t4_t1 >= 67
	c_t5_t4_t1 += MM[0]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 68
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 68
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=5, delay_cost=1)
	S += c_t3_t0_t4 >= 68
	c_t3_t0_t4 += MM[0]

	c_t4_t10 = S.Task('c_t4_t10', length=2, delay_cost=1)
	S += c_t4_t10 >= 68
	c_t4_t10 += MAS[2]

	c_t4_t1_t5_in = S.Task('c_t4_t1_t5_in', length=1, delay_cost=1)
	S += c_t4_t1_t5_in >= 68
	c_t4_t1_t5_in += MAS_in[0]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem0 >= 68
	c_t4_t1_t5_mem0 += MM_MEM[0]

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem1 >= 68
	c_t4_t1_t5_mem1 += MM_MEM[1]

	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	S += c_t4_t4_t1_in >= 68
	c_t4_t4_t1_in += MM_in[0]

	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem0 >= 68
	c_t4_t4_t1_mem0 += MAS_MEM[0]

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem1 >= 68
	c_t4_t4_t1_mem1 += MAS_MEM[7]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 69
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 69
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3_t00_in = S.Task('c_t3_t00_in', length=1, delay_cost=1)
	S += c_t3_t00_in >= 69
	c_t3_t00_in += MAS_in[2]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 69
	c_t3_t00_mem0 += MM_MEM[0]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 69
	c_t3_t00_mem1 += MM_MEM[1]

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=2, delay_cost=1)
	S += c_t4_t1_t5 >= 69
	c_t4_t1_t5 += MAS[0]

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=5, delay_cost=1)
	S += c_t4_t4_t1 >= 69
	c_t4_t4_t1 += MM[0]

	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	S += c_t5_t1_t4_in >= 69
	c_t5_t1_t4_in += MM_in[0]

	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem0 >= 69
	c_t5_t1_t4_mem0 += MAS_MEM[6]

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem1 >= 69
	c_t5_t1_t4_mem1 += MAS_MEM[5]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 70
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 70
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t3_t00 = S.Task('c_t3_t00', length=2, delay_cost=1)
	S += c_t3_t00 >= 70
	c_t3_t00 += MAS[2]

	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	S += c_t4_t1_t4_in >= 70
	c_t4_t1_t4_in += MM_in[0]

	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem0 >= 70
	c_t4_t1_t4_mem0 += MAS_MEM[4]

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem1 >= 70
	c_t4_t1_t4_mem1 += MAS_MEM[3]

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=5, delay_cost=1)
	S += c_t5_t1_t4 >= 70
	c_t5_t1_t4 += MM[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 71
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	S += c_t3_t1_t4_in >= 71
	c_t3_t1_t4_in += MM_in[0]

	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem0 >= 71
	c_t3_t1_t4_mem0 += MAS_MEM[4]

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem1 >= 71
	c_t3_t1_t4_mem1 += MAS_MEM[7]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 71
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=5, delay_cost=1)
	S += c_t4_t1_t4 >= 71
	c_t4_t1_t4 += MM[0]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 72
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=5, delay_cost=1)
	S += c_t3_t1_t4 >= 72
	c_t3_t1_t4 += MM[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 72
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	S += c_t4_t4_t0_in >= 72
	c_t4_t4_t0_in += MM_in[0]

	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem0 >= 72
	c_t4_t4_t0_mem0 += MAS_MEM[4]

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem1 >= 72
	c_t4_t4_t0_mem1 += MAS_MEM[5]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 73
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 73
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=5, delay_cost=1)
	S += c_t4_t4_t0 >= 73
	c_t4_t4_t0 += MM[0]

	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	S += c_t5_t0_t4_in >= 73
	c_t5_t0_t4_in += MM_in[0]

	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem0 >= 73
	c_t5_t0_t4_mem0 += MAS_MEM[6]

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem1 >= 73
	c_t5_t0_t4_mem1 += MAS_MEM[7]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 74
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	S += c_t3_t4_t1_in >= 74
	c_t3_t4_t1_in += MM_in[0]

	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem0 >= 74
	c_t3_t4_t1_mem0 += MAS_MEM[0]

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem1 >= 74
	c_t3_t4_t1_mem1 += MAS_MEM[5]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 74
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=5, delay_cost=1)
	S += c_t5_t0_t4 >= 74
	c_t5_t0_t4 += MM[0]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 75
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 75
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=5, delay_cost=1)
	S += c_t3_t4_t1 >= 75
	c_t3_t4_t1 += MM[0]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 76
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 76
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 77
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 77
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 78
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 78
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 79
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 79
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 80
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 80
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 81
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 81
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 82
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 82
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 83
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 83
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 84
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 84
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 85
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 85
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 86
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 86
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 87
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 87
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 88
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 88
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 89
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 89
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 90
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 90
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 91
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 91
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 92
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 92
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 93
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 93
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 94
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 94
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 95
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 95
	c_t5010_mem1 += MAIN_MEM_r[1]

	d_t1_t00_mem0 = S.Task('d_t1_t00_mem0', length=1, delay_cost=1)
	S += d_t1_t00_mem0 >= 96
	d_t1_t00_mem0 += MAIN_MEM_r[0]

	d_t1_t01_mem0 = S.Task('d_t1_t01_mem0', length=1, delay_cost=1)
	S += d_t1_t01_mem0 >= 97
	d_t1_t01_mem0 += MAIN_MEM_r[0]

	d_t2_t00_mem0 = S.Task('d_t2_t00_mem0', length=1, delay_cost=1)
	S += d_t2_t00_mem0 >= 98
	d_t2_t00_mem0 += MAIN_MEM_r[0]

	d_t0_t01_mem0 = S.Task('d_t0_t01_mem0', length=1, delay_cost=1)
	S += d_t0_t01_mem0 >= 99
	d_t0_t01_mem0 += MAIN_MEM_r[0]

	d_t0_t00_mem0 = S.Task('d_t0_t00_mem0', length=1, delay_cost=1)
	S += d_t0_t00_mem0 >= 100
	d_t0_t00_mem0 += MAIN_MEM_r[0]

	d_t2_t01_mem0 = S.Task('d_t2_t01_mem0', length=1, delay_cost=1)
	S += d_t2_t01_mem0 >= 101
	d_t2_t01_mem0 += MAIN_MEM_r[0]


	# new tasks
	d_t0_t2_t4 = S.Task('d_t0_t2_t4', length=5, delay_cost=1)
	d_t0_t2_t4 += alt(MM)
	d_t0_t2_t4_in = S.Task('d_t0_t2_t4_in', length=1, delay_cost=1)
	d_t0_t2_t4_in += alt(MM_in)
	S += d_t0_t2_t4_in*MM_in[0]<=d_t0_t2_t4*MM[0]

	d_t0_t2_t4_mem0 = S.Task('d_t0_t2_t4_mem0', length=1, delay_cost=1)
	d_t0_t2_t4_mem0 += MAS_MEM[6]
	S += 47 < d_t0_t2_t4_mem0
	S += d_t0_t2_t4_mem0 <= d_t0_t2_t4

	d_t0_t2_t4_mem1 = S.Task('d_t0_t2_t4_mem1', length=1, delay_cost=1)
	d_t0_t2_t4_mem1 += MAS_MEM[1]
	S += 28 < d_t0_t2_t4_mem1
	S += d_t0_t2_t4_mem1 <= d_t0_t2_t4

	d_t0_t20 = S.Task('d_t0_t20', length=2, delay_cost=1)
	d_t0_t20 += alt(MAS)
	d_t0_t20_in = S.Task('d_t0_t20_in', length=1, delay_cost=1)
	d_t0_t20_in += alt(MAS_in)
	S += d_t0_t20_in*MAS_in[0]<=d_t0_t20*MAS[0]

	S += d_t0_t20_in*MAS_in[1]<=d_t0_t20*MAS[1]

	S += d_t0_t20_in*MAS_in[2]<=d_t0_t20*MAS[2]

	S += d_t0_t20_in*MAS_in[3]<=d_t0_t20*MAS[3]

	d_t0_t20_mem0 = S.Task('d_t0_t20_mem0', length=1, delay_cost=1)
	d_t0_t20_mem0 += MM_MEM[0]
	S += 58 < d_t0_t20_mem0
	S += d_t0_t20_mem0 <= d_t0_t20

	d_t0_t20_mem1 = S.Task('d_t0_t20_mem1', length=1, delay_cost=1)
	d_t0_t20_mem1 += MM_MEM[1]
	S += 63 < d_t0_t20_mem1
	S += d_t0_t20_mem1 <= d_t0_t20

	d_t0_t2_t5 = S.Task('d_t0_t2_t5', length=2, delay_cost=1)
	d_t0_t2_t5 += alt(MAS)
	d_t0_t2_t5_in = S.Task('d_t0_t2_t5_in', length=1, delay_cost=1)
	d_t0_t2_t5_in += alt(MAS_in)
	S += d_t0_t2_t5_in*MAS_in[0]<=d_t0_t2_t5*MAS[0]

	S += d_t0_t2_t5_in*MAS_in[1]<=d_t0_t2_t5*MAS[1]

	S += d_t0_t2_t5_in*MAS_in[2]<=d_t0_t2_t5*MAS[2]

	S += d_t0_t2_t5_in*MAS_in[3]<=d_t0_t2_t5*MAS[3]

	d_t0_t2_t5_mem0 = S.Task('d_t0_t2_t5_mem0', length=1, delay_cost=1)
	d_t0_t2_t5_mem0 += MM_MEM[0]
	S += 58 < d_t0_t2_t5_mem0
	S += d_t0_t2_t5_mem0 <= d_t0_t2_t5

	d_t0_t2_t5_mem1 = S.Task('d_t0_t2_t5_mem1', length=1, delay_cost=1)
	d_t0_t2_t5_mem1 += MM_MEM[1]
	S += 63 < d_t0_t2_t5_mem1
	S += d_t0_t2_t5_mem1 <= d_t0_t2_t5

	d_t0_t40 = S.Task('d_t0_t40', length=2, delay_cost=1)
	d_t0_t40 += alt(MAS)
	d_t0_t40_in = S.Task('d_t0_t40_in', length=1, delay_cost=1)
	d_t0_t40_in += alt(MAS_in)
	S += d_t0_t40_in*MAS_in[0]<=d_t0_t40*MAS[0]

	S += d_t0_t40_in*MAS_in[1]<=d_t0_t40*MAS[1]

	S += d_t0_t40_in*MAS_in[2]<=d_t0_t40*MAS[2]

	S += d_t0_t40_in*MAS_in[3]<=d_t0_t40*MAS[3]

	d_t0_t40_mem0 = S.Task('d_t0_t40_mem0', length=1, delay_cost=1)
	d_t0_t40_mem0 += MAS_MEM[0]
	S += 30 < d_t0_t40_mem0
	S += d_t0_t40_mem0 <= d_t0_t40

	d_t0_t40_mem1 = S.Task('d_t0_t40_mem1', length=1, delay_cost=1)
	d_t0_t40_mem1 += MAS_MEM[7]
	S += 48 < d_t0_t40_mem1
	S += d_t0_t40_mem1 <= d_t0_t40

	d_t0_t41 = S.Task('d_t0_t41', length=2, delay_cost=1)
	d_t0_t41 += alt(MAS)
	d_t0_t41_in = S.Task('d_t0_t41_in', length=1, delay_cost=1)
	d_t0_t41_in += alt(MAS_in)
	S += d_t0_t41_in*MAS_in[0]<=d_t0_t41*MAS[0]

	S += d_t0_t41_in*MAS_in[1]<=d_t0_t41*MAS[1]

	S += d_t0_t41_in*MAS_in[2]<=d_t0_t41*MAS[2]

	S += d_t0_t41_in*MAS_in[3]<=d_t0_t41*MAS[3]

	d_t0_t41_mem0 = S.Task('d_t0_t41_mem0', length=1, delay_cost=1)
	d_t0_t41_mem0 += MAS_MEM[6]
	S += 48 < d_t0_t41_mem0
	S += d_t0_t41_mem0 <= d_t0_t41

	d_t0_t41_mem1 = S.Task('d_t0_t41_mem1', length=1, delay_cost=1)
	d_t0_t41_mem1 += MAS_MEM[1]
	S += 30 < d_t0_t41_mem1
	S += d_t0_t41_mem1 <= d_t0_t41

	d_t011 = S.Task('d_t011', length=2, delay_cost=1)
	d_t011 += alt(MAS)
	d_t011_in = S.Task('d_t011_in', length=1, delay_cost=1)
	d_t011_in += alt(MAS_in)
	S += d_t011_in*MAS_in[0]<=d_t011*MAS[0]

	S += d_t011_in*MAS_in[1]<=d_t011*MAS[1]

	S += d_t011_in*MAS_in[2]<=d_t011*MAS[2]

	S += d_t011_in*MAS_in[3]<=d_t011*MAS[3]

	d_t011_mem0 = S.Task('d_t011_mem0', length=1, delay_cost=1)
	d_t011_mem0 += MAS_MEM[6]
	S += 48 < d_t011_mem0
	S += d_t011_mem0 <= d_t011

	d_t1_t2_t4 = S.Task('d_t1_t2_t4', length=5, delay_cost=1)
	d_t1_t2_t4 += alt(MM)
	d_t1_t2_t4_in = S.Task('d_t1_t2_t4_in', length=1, delay_cost=1)
	d_t1_t2_t4_in += alt(MM_in)
	S += d_t1_t2_t4_in*MM_in[0]<=d_t1_t2_t4*MM[0]

	d_t1_t2_t4_mem0 = S.Task('d_t1_t2_t4_mem0', length=1, delay_cost=1)
	d_t1_t2_t4_mem0 += MAS_MEM[2]
	S += 41 < d_t1_t2_t4_mem0
	S += d_t1_t2_t4_mem0 <= d_t1_t2_t4

	d_t1_t2_t4_mem1 = S.Task('d_t1_t2_t4_mem1', length=1, delay_cost=1)
	d_t1_t2_t4_mem1 += MAS_MEM[1]
	S += 23 < d_t1_t2_t4_mem1
	S += d_t1_t2_t4_mem1 <= d_t1_t2_t4

	d_t1_t20 = S.Task('d_t1_t20', length=2, delay_cost=1)
	d_t1_t20 += alt(MAS)
	d_t1_t20_in = S.Task('d_t1_t20_in', length=1, delay_cost=1)
	d_t1_t20_in += alt(MAS_in)
	S += d_t1_t20_in*MAS_in[0]<=d_t1_t20*MAS[0]

	S += d_t1_t20_in*MAS_in[1]<=d_t1_t20*MAS[1]

	S += d_t1_t20_in*MAS_in[2]<=d_t1_t20*MAS[2]

	S += d_t1_t20_in*MAS_in[3]<=d_t1_t20*MAS[3]

	d_t1_t20_mem0 = S.Task('d_t1_t20_mem0', length=1, delay_cost=1)
	d_t1_t20_mem0 += MM_MEM[0]
	S += 61 < d_t1_t20_mem0
	S += d_t1_t20_mem0 <= d_t1_t20

	d_t1_t20_mem1 = S.Task('d_t1_t20_mem1', length=1, delay_cost=1)
	d_t1_t20_mem1 += MM_MEM[1]
	S += 64 < d_t1_t20_mem1
	S += d_t1_t20_mem1 <= d_t1_t20

	d_t1_t2_t5 = S.Task('d_t1_t2_t5', length=2, delay_cost=1)
	d_t1_t2_t5 += alt(MAS)
	d_t1_t2_t5_in = S.Task('d_t1_t2_t5_in', length=1, delay_cost=1)
	d_t1_t2_t5_in += alt(MAS_in)
	S += d_t1_t2_t5_in*MAS_in[0]<=d_t1_t2_t5*MAS[0]

	S += d_t1_t2_t5_in*MAS_in[1]<=d_t1_t2_t5*MAS[1]

	S += d_t1_t2_t5_in*MAS_in[2]<=d_t1_t2_t5*MAS[2]

	S += d_t1_t2_t5_in*MAS_in[3]<=d_t1_t2_t5*MAS[3]

	d_t1_t2_t5_mem0 = S.Task('d_t1_t2_t5_mem0', length=1, delay_cost=1)
	d_t1_t2_t5_mem0 += MM_MEM[0]
	S += 61 < d_t1_t2_t5_mem0
	S += d_t1_t2_t5_mem0 <= d_t1_t2_t5

	d_t1_t2_t5_mem1 = S.Task('d_t1_t2_t5_mem1', length=1, delay_cost=1)
	d_t1_t2_t5_mem1 += MM_MEM[1]
	S += 64 < d_t1_t2_t5_mem1
	S += d_t1_t2_t5_mem1 <= d_t1_t2_t5

	d_t1_t40 = S.Task('d_t1_t40', length=2, delay_cost=1)
	d_t1_t40 += alt(MAS)
	d_t1_t40_in = S.Task('d_t1_t40_in', length=1, delay_cost=1)
	d_t1_t40_in += alt(MAS_in)
	S += d_t1_t40_in*MAS_in[0]<=d_t1_t40*MAS[0]

	S += d_t1_t40_in*MAS_in[1]<=d_t1_t40*MAS[1]

	S += d_t1_t40_in*MAS_in[2]<=d_t1_t40*MAS[2]

	S += d_t1_t40_in*MAS_in[3]<=d_t1_t40*MAS[3]

	d_t1_t40_mem0 = S.Task('d_t1_t40_mem0', length=1, delay_cost=1)
	d_t1_t40_mem0 += MAS_MEM[2]
	S += 22 < d_t1_t40_mem0
	S += d_t1_t40_mem0 <= d_t1_t40

	d_t1_t40_mem1 = S.Task('d_t1_t40_mem1', length=1, delay_cost=1)
	d_t1_t40_mem1 += MAS_MEM[3]
	S += 51 < d_t1_t40_mem1
	S += d_t1_t40_mem1 <= d_t1_t40

	d_t1_t41 = S.Task('d_t1_t41', length=2, delay_cost=1)
	d_t1_t41 += alt(MAS)
	d_t1_t41_in = S.Task('d_t1_t41_in', length=1, delay_cost=1)
	d_t1_t41_in += alt(MAS_in)
	S += d_t1_t41_in*MAS_in[0]<=d_t1_t41*MAS[0]

	S += d_t1_t41_in*MAS_in[1]<=d_t1_t41*MAS[1]

	S += d_t1_t41_in*MAS_in[2]<=d_t1_t41*MAS[2]

	S += d_t1_t41_in*MAS_in[3]<=d_t1_t41*MAS[3]

	d_t1_t41_mem0 = S.Task('d_t1_t41_mem0', length=1, delay_cost=1)
	d_t1_t41_mem0 += MAS_MEM[2]
	S += 51 < d_t1_t41_mem0
	S += d_t1_t41_mem0 <= d_t1_t41

	d_t1_t41_mem1 = S.Task('d_t1_t41_mem1', length=1, delay_cost=1)
	d_t1_t41_mem1 += MAS_MEM[3]
	S += 22 < d_t1_t41_mem1
	S += d_t1_t41_mem1 <= d_t1_t41

	d_t111 = S.Task('d_t111', length=2, delay_cost=1)
	d_t111 += alt(MAS)
	d_t111_in = S.Task('d_t111_in', length=1, delay_cost=1)
	d_t111_in += alt(MAS_in)
	S += d_t111_in*MAS_in[0]<=d_t111*MAS[0]

	S += d_t111_in*MAS_in[1]<=d_t111*MAS[1]

	S += d_t111_in*MAS_in[2]<=d_t111*MAS[2]

	S += d_t111_in*MAS_in[3]<=d_t111*MAS[3]

	d_t111_mem0 = S.Task('d_t111_mem0', length=1, delay_cost=1)
	d_t111_mem0 += MAS_MEM[2]
	S += 51 < d_t111_mem0
	S += d_t111_mem0 <= d_t111

	d_t2_t2_t4 = S.Task('d_t2_t2_t4', length=5, delay_cost=1)
	d_t2_t2_t4 += alt(MM)
	d_t2_t2_t4_in = S.Task('d_t2_t2_t4_in', length=1, delay_cost=1)
	d_t2_t2_t4_in += alt(MM_in)
	S += d_t2_t2_t4_in*MM_in[0]<=d_t2_t2_t4*MM[0]

	d_t2_t2_t4_mem0 = S.Task('d_t2_t2_t4_mem0', length=1, delay_cost=1)
	d_t2_t2_t4_mem0 += MAS_MEM[4]
	S += 43 < d_t2_t2_t4_mem0
	S += d_t2_t2_t4_mem0 <= d_t2_t2_t4

	d_t2_t2_t4_mem1 = S.Task('d_t2_t2_t4_mem1', length=1, delay_cost=1)
	d_t2_t2_t4_mem1 += MAS_MEM[7]
	S += 28 < d_t2_t2_t4_mem1
	S += d_t2_t2_t4_mem1 <= d_t2_t2_t4

	d_t2_t20 = S.Task('d_t2_t20', length=2, delay_cost=1)
	d_t2_t20 += alt(MAS)
	d_t2_t20_in = S.Task('d_t2_t20_in', length=1, delay_cost=1)
	d_t2_t20_in += alt(MAS_in)
	S += d_t2_t20_in*MAS_in[0]<=d_t2_t20*MAS[0]

	S += d_t2_t20_in*MAS_in[1]<=d_t2_t20*MAS[1]

	S += d_t2_t20_in*MAS_in[2]<=d_t2_t20*MAS[2]

	S += d_t2_t20_in*MAS_in[3]<=d_t2_t20*MAS[3]

	d_t2_t20_mem0 = S.Task('d_t2_t20_mem0', length=1, delay_cost=1)
	d_t2_t20_mem0 += MM_MEM[0]
	S += 60 < d_t2_t20_mem0
	S += d_t2_t20_mem0 <= d_t2_t20

	d_t2_t20_mem1 = S.Task('d_t2_t20_mem1', length=1, delay_cost=1)
	d_t2_t20_mem1 += MM_MEM[1]
	S += 57 < d_t2_t20_mem1
	S += d_t2_t20_mem1 <= d_t2_t20

	d_t2_t2_t5 = S.Task('d_t2_t2_t5', length=2, delay_cost=1)
	d_t2_t2_t5 += alt(MAS)
	d_t2_t2_t5_in = S.Task('d_t2_t2_t5_in', length=1, delay_cost=1)
	d_t2_t2_t5_in += alt(MAS_in)
	S += d_t2_t2_t5_in*MAS_in[0]<=d_t2_t2_t5*MAS[0]

	S += d_t2_t2_t5_in*MAS_in[1]<=d_t2_t2_t5*MAS[1]

	S += d_t2_t2_t5_in*MAS_in[2]<=d_t2_t2_t5*MAS[2]

	S += d_t2_t2_t5_in*MAS_in[3]<=d_t2_t2_t5*MAS[3]

	d_t2_t2_t5_mem0 = S.Task('d_t2_t2_t5_mem0', length=1, delay_cost=1)
	d_t2_t2_t5_mem0 += MM_MEM[0]
	S += 60 < d_t2_t2_t5_mem0
	S += d_t2_t2_t5_mem0 <= d_t2_t2_t5

	d_t2_t2_t5_mem1 = S.Task('d_t2_t2_t5_mem1', length=1, delay_cost=1)
	d_t2_t2_t5_mem1 += MM_MEM[1]
	S += 57 < d_t2_t2_t5_mem1
	S += d_t2_t2_t5_mem1 <= d_t2_t2_t5

	d_t2_t40 = S.Task('d_t2_t40', length=2, delay_cost=1)
	d_t2_t40 += alt(MAS)
	d_t2_t40_in = S.Task('d_t2_t40_in', length=1, delay_cost=1)
	d_t2_t40_in += alt(MAS_in)
	S += d_t2_t40_in*MAS_in[0]<=d_t2_t40*MAS[0]

	S += d_t2_t40_in*MAS_in[1]<=d_t2_t40*MAS[1]

	S += d_t2_t40_in*MAS_in[2]<=d_t2_t40*MAS[2]

	S += d_t2_t40_in*MAS_in[3]<=d_t2_t40*MAS[3]

	d_t2_t40_mem0 = S.Task('d_t2_t40_mem0', length=1, delay_cost=1)
	d_t2_t40_mem0 += MAS_MEM[2]
	S += 24 < d_t2_t40_mem0
	S += d_t2_t40_mem0 <= d_t2_t40

	d_t2_t40_mem1 = S.Task('d_t2_t40_mem1', length=1, delay_cost=1)
	d_t2_t40_mem1 += MAS_MEM[1]
	S += 44 < d_t2_t40_mem1
	S += d_t2_t40_mem1 <= d_t2_t40

	d_t2_t41 = S.Task('d_t2_t41', length=2, delay_cost=1)
	d_t2_t41 += alt(MAS)
	d_t2_t41_in = S.Task('d_t2_t41_in', length=1, delay_cost=1)
	d_t2_t41_in += alt(MAS_in)
	S += d_t2_t41_in*MAS_in[0]<=d_t2_t41*MAS[0]

	S += d_t2_t41_in*MAS_in[1]<=d_t2_t41*MAS[1]

	S += d_t2_t41_in*MAS_in[2]<=d_t2_t41*MAS[2]

	S += d_t2_t41_in*MAS_in[3]<=d_t2_t41*MAS[3]

	d_t2_t41_mem0 = S.Task('d_t2_t41_mem0', length=1, delay_cost=1)
	d_t2_t41_mem0 += MAS_MEM[0]
	S += 44 < d_t2_t41_mem0
	S += d_t2_t41_mem0 <= d_t2_t41

	d_t2_t41_mem1 = S.Task('d_t2_t41_mem1', length=1, delay_cost=1)
	d_t2_t41_mem1 += MAS_MEM[3]
	S += 24 < d_t2_t41_mem1
	S += d_t2_t41_mem1 <= d_t2_t41

	d_t211 = S.Task('d_t211', length=2, delay_cost=1)
	d_t211 += alt(MAS)
	d_t211_in = S.Task('d_t211_in', length=1, delay_cost=1)
	d_t211_in += alt(MAS_in)
	S += d_t211_in*MAS_in[0]<=d_t211*MAS[0]

	S += d_t211_in*MAS_in[1]<=d_t211*MAS[1]

	S += d_t211_in*MAS_in[2]<=d_t211*MAS[2]

	S += d_t211_in*MAS_in[3]<=d_t211*MAS[3]

	d_t211_mem0 = S.Task('d_t211_mem0', length=1, delay_cost=1)
	d_t211_mem0 += MAS_MEM[0]
	S += 44 < d_t211_mem0
	S += d_t211_mem0 <= d_t211

	d_t3_t2_t0 = S.Task('d_t3_t2_t0', length=5, delay_cost=1)
	d_t3_t2_t0 += alt(MM)
	d_t3_t2_t0_in = S.Task('d_t3_t2_t0_in', length=1, delay_cost=1)
	d_t3_t2_t0_in += alt(MM_in)
	S += d_t3_t2_t0_in*MM_in[0]<=d_t3_t2_t0*MM[0]

	d_t3_t2_t0_mem0 = S.Task('d_t3_t2_t0_mem0', length=1, delay_cost=1)
	d_t3_t2_t0_mem0 += MAS_MEM[6]
	S += 41 < d_t3_t2_t0_mem0
	S += d_t3_t2_t0_mem0 <= d_t3_t2_t0

	d_t3_t2_t0_mem1 = S.Task('d_t3_t2_t0_mem1', length=1, delay_cost=1)
	d_t3_t2_t0_mem1 += MAS_MEM[5]
	S += 25 < d_t3_t2_t0_mem1
	S += d_t3_t2_t0_mem1 <= d_t3_t2_t0

	d_t3_t2_t1 = S.Task('d_t3_t2_t1', length=5, delay_cost=1)
	d_t3_t2_t1 += alt(MM)
	d_t3_t2_t1_in = S.Task('d_t3_t2_t1_in', length=1, delay_cost=1)
	d_t3_t2_t1_in += alt(MM_in)
	S += d_t3_t2_t1_in*MM_in[0]<=d_t3_t2_t1*MM[0]

	d_t3_t2_t1_mem0 = S.Task('d_t3_t2_t1_mem0', length=1, delay_cost=1)
	d_t3_t2_t1_mem0 += MAS_MEM[4]
	S += 48 < d_t3_t2_t1_mem0
	S += d_t3_t2_t1_mem0 <= d_t3_t2_t1

	d_t3_t2_t1_mem1 = S.Task('d_t3_t2_t1_mem1', length=1, delay_cost=1)
	d_t3_t2_t1_mem1 += MAS_MEM[5]
	S += 22 < d_t3_t2_t1_mem1
	S += d_t3_t2_t1_mem1 <= d_t3_t2_t1

	d_t3_t2_t2 = S.Task('d_t3_t2_t2', length=2, delay_cost=1)
	d_t3_t2_t2 += alt(MAS)
	d_t3_t2_t2_in = S.Task('d_t3_t2_t2_in', length=1, delay_cost=1)
	d_t3_t2_t2_in += alt(MAS_in)
	S += d_t3_t2_t2_in*MAS_in[0]<=d_t3_t2_t2*MAS[0]

	S += d_t3_t2_t2_in*MAS_in[1]<=d_t3_t2_t2*MAS[1]

	S += d_t3_t2_t2_in*MAS_in[2]<=d_t3_t2_t2*MAS[2]

	S += d_t3_t2_t2_in*MAS_in[3]<=d_t3_t2_t2*MAS[3]

	d_t3_t2_t2_mem0 = S.Task('d_t3_t2_t2_mem0', length=1, delay_cost=1)
	d_t3_t2_t2_mem0 += MAS_MEM[6]
	S += 41 < d_t3_t2_t2_mem0
	S += d_t3_t2_t2_mem0 <= d_t3_t2_t2

	d_t3_t2_t2_mem1 = S.Task('d_t3_t2_t2_mem1', length=1, delay_cost=1)
	d_t3_t2_t2_mem1 += MAS_MEM[5]
	S += 48 < d_t3_t2_t2_mem1
	S += d_t3_t2_t2_mem1 <= d_t3_t2_t2

	d_t3_t31 = S.Task('d_t3_t31', length=2, delay_cost=1)
	d_t3_t31 += alt(MAS)
	d_t3_t31_in = S.Task('d_t3_t31_in', length=1, delay_cost=1)
	d_t3_t31_in += alt(MAS_in)
	S += d_t3_t31_in*MAS_in[0]<=d_t3_t31*MAS[0]

	S += d_t3_t31_in*MAS_in[1]<=d_t3_t31*MAS[1]

	S += d_t3_t31_in*MAS_in[2]<=d_t3_t31*MAS[2]

	S += d_t3_t31_in*MAS_in[3]<=d_t3_t31*MAS[3]

	d_t3_t31_mem0 = S.Task('d_t3_t31_mem0', length=1, delay_cost=1)
	d_t3_t31_mem0 += MM_MEM[0]
	S += 56 < d_t3_t31_mem0
	S += d_t3_t31_mem0 <= d_t3_t31

	d_t3_t31_mem1 = S.Task('d_t3_t31_mem1', length=1, delay_cost=1)
	d_t3_t31_mem1 += MAS_MEM[3]
	S += 58 < d_t3_t31_mem1
	S += d_t3_t31_mem1 <= d_t3_t31

	d_t310 = S.Task('d_t310', length=2, delay_cost=1)
	d_t310 += alt(MAS)
	d_t310_in = S.Task('d_t310_in', length=1, delay_cost=1)
	d_t310_in += alt(MAS_in)
	S += d_t310_in*MAS_in[0]<=d_t310*MAS[0]

	S += d_t310_in*MAS_in[1]<=d_t310*MAS[1]

	S += d_t310_in*MAS_in[2]<=d_t310*MAS[2]

	S += d_t310_in*MAS_in[3]<=d_t310*MAS[3]

	d_t310_mem0 = S.Task('d_t310_mem0', length=1, delay_cost=1)
	d_t310_mem0 += MAS_MEM[0]
	S += 43 < d_t310_mem0
	S += d_t310_mem0 <= d_t310

	d_t4_t2_t0 = S.Task('d_t4_t2_t0', length=5, delay_cost=1)
	d_t4_t2_t0 += alt(MM)
	d_t4_t2_t0_in = S.Task('d_t4_t2_t0_in', length=1, delay_cost=1)
	d_t4_t2_t0_in += alt(MM_in)
	S += d_t4_t2_t0_in*MM_in[0]<=d_t4_t2_t0*MM[0]

	d_t4_t2_t0_mem0 = S.Task('d_t4_t2_t0_mem0', length=1, delay_cost=1)
	d_t4_t2_t0_mem0 += MAS_MEM[2]
	S += 43 < d_t4_t2_t0_mem0
	S += d_t4_t2_t0_mem0 <= d_t4_t2_t0

	d_t4_t2_t0_mem1 = S.Task('d_t4_t2_t0_mem1', length=1, delay_cost=1)
	d_t4_t2_t0_mem1 += MAS_MEM[7]
	S += 22 < d_t4_t2_t0_mem1
	S += d_t4_t2_t0_mem1 <= d_t4_t2_t0

	d_t4_t2_t1 = S.Task('d_t4_t2_t1', length=5, delay_cost=1)
	d_t4_t2_t1 += alt(MM)
	d_t4_t2_t1_in = S.Task('d_t4_t2_t1_in', length=1, delay_cost=1)
	d_t4_t2_t1_in += alt(MM_in)
	S += d_t4_t2_t1_in*MM_in[0]<=d_t4_t2_t1*MM[0]

	d_t4_t2_t1_mem0 = S.Task('d_t4_t2_t1_mem0', length=1, delay_cost=1)
	d_t4_t2_t1_mem0 += MAS_MEM[4]
	S += 46 < d_t4_t2_t1_mem0
	S += d_t4_t2_t1_mem0 <= d_t4_t2_t1

	d_t4_t2_t1_mem1 = S.Task('d_t4_t2_t1_mem1', length=1, delay_cost=1)
	d_t4_t2_t1_mem1 += MAS_MEM[7]
	S += 29 < d_t4_t2_t1_mem1
	S += d_t4_t2_t1_mem1 <= d_t4_t2_t1

	d_t4_t2_t2 = S.Task('d_t4_t2_t2', length=2, delay_cost=1)
	d_t4_t2_t2 += alt(MAS)
	d_t4_t2_t2_in = S.Task('d_t4_t2_t2_in', length=1, delay_cost=1)
	d_t4_t2_t2_in += alt(MAS_in)
	S += d_t4_t2_t2_in*MAS_in[0]<=d_t4_t2_t2*MAS[0]

	S += d_t4_t2_t2_in*MAS_in[1]<=d_t4_t2_t2*MAS[1]

	S += d_t4_t2_t2_in*MAS_in[2]<=d_t4_t2_t2*MAS[2]

	S += d_t4_t2_t2_in*MAS_in[3]<=d_t4_t2_t2*MAS[3]

	d_t4_t2_t2_mem0 = S.Task('d_t4_t2_t2_mem0', length=1, delay_cost=1)
	d_t4_t2_t2_mem0 += MAS_MEM[2]
	S += 43 < d_t4_t2_t2_mem0
	S += d_t4_t2_t2_mem0 <= d_t4_t2_t2

	d_t4_t2_t2_mem1 = S.Task('d_t4_t2_t2_mem1', length=1, delay_cost=1)
	d_t4_t2_t2_mem1 += MAS_MEM[5]
	S += 46 < d_t4_t2_t2_mem1
	S += d_t4_t2_t2_mem1 <= d_t4_t2_t2

	d_t4_t31 = S.Task('d_t4_t31', length=2, delay_cost=1)
	d_t4_t31 += alt(MAS)
	d_t4_t31_in = S.Task('d_t4_t31_in', length=1, delay_cost=1)
	d_t4_t31_in += alt(MAS_in)
	S += d_t4_t31_in*MAS_in[0]<=d_t4_t31*MAS[0]

	S += d_t4_t31_in*MAS_in[1]<=d_t4_t31*MAS[1]

	S += d_t4_t31_in*MAS_in[2]<=d_t4_t31*MAS[2]

	S += d_t4_t31_in*MAS_in[3]<=d_t4_t31*MAS[3]

	d_t4_t31_mem0 = S.Task('d_t4_t31_mem0', length=1, delay_cost=1)
	d_t4_t31_mem0 += MM_MEM[0]
	S += 65 < d_t4_t31_mem0
	S += d_t4_t31_mem0 <= d_t4_t31

	d_t4_t31_mem1 = S.Task('d_t4_t31_mem1', length=1, delay_cost=1)
	d_t4_t31_mem1 += MAS_MEM[5]
	S += 40 < d_t4_t31_mem1
	S += d_t4_t31_mem1 <= d_t4_t31

	d_t410 = S.Task('d_t410', length=2, delay_cost=1)
	d_t410 += alt(MAS)
	d_t410_in = S.Task('d_t410_in', length=1, delay_cost=1)
	d_t410_in += alt(MAS_in)
	S += d_t410_in*MAS_in[0]<=d_t410*MAS[0]

	S += d_t410_in*MAS_in[1]<=d_t410*MAS[1]

	S += d_t410_in*MAS_in[2]<=d_t410*MAS[2]

	S += d_t410_in*MAS_in[3]<=d_t410*MAS[3]

	d_t410_mem0 = S.Task('d_t410_mem0', length=1, delay_cost=1)
	d_t410_mem0 += MAS_MEM[0]
	S += 41 < d_t410_mem0
	S += d_t410_mem0 <= d_t410

	d_t5_t2_t0 = S.Task('d_t5_t2_t0', length=5, delay_cost=1)
	d_t5_t2_t0 += alt(MM)
	d_t5_t2_t0_in = S.Task('d_t5_t2_t0_in', length=1, delay_cost=1)
	d_t5_t2_t0_in += alt(MM_in)
	S += d_t5_t2_t0_in*MM_in[0]<=d_t5_t2_t0*MM[0]

	d_t5_t2_t0_mem0 = S.Task('d_t5_t2_t0_mem0', length=1, delay_cost=1)
	d_t5_t2_t0_mem0 += MAS_MEM[6]
	S += 42 < d_t5_t2_t0_mem0
	S += d_t5_t2_t0_mem0 <= d_t5_t2_t0

	d_t5_t2_t0_mem1 = S.Task('d_t5_t2_t0_mem1', length=1, delay_cost=1)
	d_t5_t2_t0_mem1 += MAS_MEM[5]
	S += 24 < d_t5_t2_t0_mem1
	S += d_t5_t2_t0_mem1 <= d_t5_t2_t0

	d_t5_t2_t1 = S.Task('d_t5_t2_t1', length=5, delay_cost=1)
	d_t5_t2_t1 += alt(MM)
	d_t5_t2_t1_in = S.Task('d_t5_t2_t1_in', length=1, delay_cost=1)
	d_t5_t2_t1_in += alt(MM_in)
	S += d_t5_t2_t1_in*MM_in[0]<=d_t5_t2_t1*MM[0]

	d_t5_t2_t1_mem0 = S.Task('d_t5_t2_t1_mem0', length=1, delay_cost=1)
	d_t5_t2_t1_mem0 += MAS_MEM[4]
	S += 50 < d_t5_t2_t1_mem0
	S += d_t5_t2_t1_mem0 <= d_t5_t2_t1

	d_t5_t2_t1_mem1 = S.Task('d_t5_t2_t1_mem1', length=1, delay_cost=1)
	d_t5_t2_t1_mem1 += MAS_MEM[3]
	S += 25 < d_t5_t2_t1_mem1
	S += d_t5_t2_t1_mem1 <= d_t5_t2_t1

	d_t5_t2_t2 = S.Task('d_t5_t2_t2', length=2, delay_cost=1)
	d_t5_t2_t2 += alt(MAS)
	d_t5_t2_t2_in = S.Task('d_t5_t2_t2_in', length=1, delay_cost=1)
	d_t5_t2_t2_in += alt(MAS_in)
	S += d_t5_t2_t2_in*MAS_in[0]<=d_t5_t2_t2*MAS[0]

	S += d_t5_t2_t2_in*MAS_in[1]<=d_t5_t2_t2*MAS[1]

	S += d_t5_t2_t2_in*MAS_in[2]<=d_t5_t2_t2*MAS[2]

	S += d_t5_t2_t2_in*MAS_in[3]<=d_t5_t2_t2*MAS[3]

	d_t5_t2_t2_mem0 = S.Task('d_t5_t2_t2_mem0', length=1, delay_cost=1)
	d_t5_t2_t2_mem0 += MAS_MEM[6]
	S += 42 < d_t5_t2_t2_mem0
	S += d_t5_t2_t2_mem0 <= d_t5_t2_t2

	d_t5_t2_t2_mem1 = S.Task('d_t5_t2_t2_mem1', length=1, delay_cost=1)
	d_t5_t2_t2_mem1 += MAS_MEM[5]
	S += 50 < d_t5_t2_t2_mem1
	S += d_t5_t2_t2_mem1 <= d_t5_t2_t2

	d_t5_t31 = S.Task('d_t5_t31', length=2, delay_cost=1)
	d_t5_t31 += alt(MAS)
	d_t5_t31_in = S.Task('d_t5_t31_in', length=1, delay_cost=1)
	d_t5_t31_in += alt(MAS_in)
	S += d_t5_t31_in*MAS_in[0]<=d_t5_t31*MAS[0]

	S += d_t5_t31_in*MAS_in[1]<=d_t5_t31*MAS[1]

	S += d_t5_t31_in*MAS_in[2]<=d_t5_t31*MAS[2]

	S += d_t5_t31_in*MAS_in[3]<=d_t5_t31*MAS[3]

	d_t5_t31_mem0 = S.Task('d_t5_t31_mem0', length=1, delay_cost=1)
	d_t5_t31_mem0 += MM_MEM[0]
	S += 59 < d_t5_t31_mem0
	S += d_t5_t31_mem0 <= d_t5_t31

	d_t5_t31_mem1 = S.Task('d_t5_t31_mem1', length=1, delay_cost=1)
	d_t5_t31_mem1 += MAS_MEM[7]
	S += 49 < d_t5_t31_mem1
	S += d_t5_t31_mem1 <= d_t5_t31

	d_t510 = S.Task('d_t510', length=2, delay_cost=1)
	d_t510 += alt(MAS)
	d_t510_in = S.Task('d_t510_in', length=1, delay_cost=1)
	d_t510_in += alt(MAS_in)
	S += d_t510_in*MAS_in[0]<=d_t510*MAS[0]

	S += d_t510_in*MAS_in[1]<=d_t510*MAS[1]

	S += d_t510_in*MAS_in[2]<=d_t510*MAS[2]

	S += d_t510_in*MAS_in[3]<=d_t510*MAS[3]

	d_t510_mem0 = S.Task('d_t510_mem0', length=1, delay_cost=1)
	d_t510_mem0 += MAS_MEM[4]
	S += 39 < d_t510_mem0
	S += d_t510_mem0 <= d_t510

	d_s0010 = S.Task('d_s0010', length=2, delay_cost=1)
	d_s0010 += alt(MAS)
	d_s0010_in = S.Task('d_s0010_in', length=1, delay_cost=1)
	d_s0010_in += alt(MAS_in)
	S += d_s0010_in*MAS_in[0]<=d_s0010*MAS[0]

	S += d_s0010_in*MAS_in[1]<=d_s0010*MAS[1]

	S += d_s0010_in*MAS_in[2]<=d_s0010*MAS[2]

	S += d_s0010_in*MAS_in[3]<=d_s0010*MAS[3]

	d_s0010_mem0 = S.Task('d_s0010_mem0', length=1, delay_cost=1)
	d_s0010_mem0 += MAS_MEM[2]
	S += 44 < d_s0010_mem0
	S += d_s0010_mem0 <= d_s0010

	d_s0010_mem1 = S.Task('d_s0010_mem1', length=1, delay_cost=1)
	d_s0010_mem1 += MAS_MEM[3]
	S += 38 < d_s0010_mem1
	S += d_s0010_mem1 <= d_s0010

	d_s1010 = S.Task('d_s1010', length=2, delay_cost=1)
	d_s1010 += alt(MAS)
	d_s1010_in = S.Task('d_s1010_in', length=1, delay_cost=1)
	d_s1010_in += alt(MAS_in)
	S += d_s1010_in*MAS_in[0]<=d_s1010*MAS[0]

	S += d_s1010_in*MAS_in[1]<=d_s1010*MAS[1]

	S += d_s1010_in*MAS_in[2]<=d_s1010*MAS[2]

	S += d_s1010_in*MAS_in[3]<=d_s1010*MAS[3]

	d_s1010_mem0 = S.Task('d_s1010_mem0', length=1, delay_cost=1)
	d_s1010_mem0 += MAS_MEM[2]
	S += 38 < d_s1010_mem0
	S += d_s1010_mem0 <= d_s1010

	d_s1010_mem1 = S.Task('d_s1010_mem1', length=1, delay_cost=1)
	d_s1010_mem1 += MAS_MEM[3]
	S += 42 < d_s1010_mem1
	S += d_s1010_mem1 <= d_s1010

	d_s2010 = S.Task('d_s2010', length=2, delay_cost=1)
	d_s2010 += alt(MAS)
	d_s2010_in = S.Task('d_s2010_in', length=1, delay_cost=1)
	d_s2010_in += alt(MAS_in)
	S += d_s2010_in*MAS_in[0]<=d_s2010*MAS[0]

	S += d_s2010_in*MAS_in[1]<=d_s2010*MAS[1]

	S += d_s2010_in*MAS_in[2]<=d_s2010*MAS[2]

	S += d_s2010_in*MAS_in[3]<=d_s2010*MAS[3]

	d_s2010_mem0 = S.Task('d_s2010_mem0', length=1, delay_cost=1)
	d_s2010_mem0 += MAS_MEM[2]
	S += 42 < d_s2010_mem0
	S += d_s2010_mem0 <= d_s2010

	d_s2010_mem1 = S.Task('d_s2010_mem1', length=1, delay_cost=1)
	d_s2010_mem1 += MAS_MEM[3]
	S += 44 < d_s2010_mem1
	S += d_s2010_mem1 <= d_s2010

	c_t0_t41 = S.Task('c_t0_t41', length=2, delay_cost=1)
	c_t0_t41 += alt(MAS)
	c_t0_t41_in = S.Task('c_t0_t41_in', length=1, delay_cost=1)
	c_t0_t41_in += alt(MAS_in)
	S += c_t0_t41_in*MAS_in[0]<=c_t0_t41*MAS[0]

	S += c_t0_t41_in*MAS_in[1]<=c_t0_t41*MAS[1]

	S += c_t0_t41_in*MAS_in[2]<=c_t0_t41*MAS[2]

	S += c_t0_t41_in*MAS_in[3]<=c_t0_t41*MAS[3]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	c_t0_t41_mem0 += MM_MEM[0]
	S += 66 < c_t0_t41_mem0
	S += c_t0_t41_mem0 <= c_t0_t41

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	c_t0_t41_mem1 += MAS_MEM[7]
	S += 46 < c_t0_t41_mem1
	S += c_t0_t41_mem1 <= c_t0_t41

	c_t0_s00 = S.Task('c_t0_s00', length=2, delay_cost=1)
	c_t0_s00 += alt(MAS)
	c_t0_s00_in = S.Task('c_t0_s00_in', length=1, delay_cost=1)
	c_t0_s00_in += alt(MAS_in)
	S += c_t0_s00_in*MAS_in[0]<=c_t0_s00*MAS[0]

	S += c_t0_s00_in*MAS_in[1]<=c_t0_s00*MAS[1]

	S += c_t0_s00_in*MAS_in[2]<=c_t0_s00*MAS[2]

	S += c_t0_s00_in*MAS_in[3]<=c_t0_s00*MAS[3]

	c_t0_s00_mem0 = S.Task('c_t0_s00_mem0', length=1, delay_cost=1)
	c_t0_s00_mem0 += MAS_MEM[2]
	S += 28 < c_t0_s00_mem0
	S += c_t0_s00_mem0 <= c_t0_s00

	c_t0_s00_mem1 = S.Task('c_t0_s00_mem1', length=1, delay_cost=1)
	c_t0_s00_mem1 += MAS_MEM[7]
	S += 59 < c_t0_s00_mem1
	S += c_t0_s00_mem1 <= c_t0_s00

	c_t0_s01 = S.Task('c_t0_s01', length=2, delay_cost=1)
	c_t0_s01 += alt(MAS)
	c_t0_s01_in = S.Task('c_t0_s01_in', length=1, delay_cost=1)
	c_t0_s01_in += alt(MAS_in)
	S += c_t0_s01_in*MAS_in[0]<=c_t0_s01*MAS[0]

	S += c_t0_s01_in*MAS_in[1]<=c_t0_s01*MAS[1]

	S += c_t0_s01_in*MAS_in[2]<=c_t0_s01*MAS[2]

	S += c_t0_s01_in*MAS_in[3]<=c_t0_s01*MAS[3]

	c_t0_s01_mem0 = S.Task('c_t0_s01_mem0', length=1, delay_cost=1)
	c_t0_s01_mem0 += MAS_MEM[6]
	S += 59 < c_t0_s01_mem0
	S += c_t0_s01_mem0 <= c_t0_s01

	c_t0_s01_mem1 = S.Task('c_t0_s01_mem1', length=1, delay_cost=1)
	c_t0_s01_mem1 += MAS_MEM[3]
	S += 28 < c_t0_s01_mem1
	S += c_t0_s01_mem1 <= c_t0_s01

	c_t0_t51 = S.Task('c_t0_t51', length=2, delay_cost=1)
	c_t0_t51 += alt(MAS)
	c_t0_t51_in = S.Task('c_t0_t51_in', length=1, delay_cost=1)
	c_t0_t51_in += alt(MAS_in)
	S += c_t0_t51_in*MAS_in[0]<=c_t0_t51*MAS[0]

	S += c_t0_t51_in*MAS_in[1]<=c_t0_t51*MAS[1]

	S += c_t0_t51_in*MAS_in[2]<=c_t0_t51*MAS[2]

	S += c_t0_t51_in*MAS_in[3]<=c_t0_t51*MAS[3]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	c_t0_t51_mem0 += MAS_MEM[0]
	S += 42 < c_t0_t51_mem0
	S += c_t0_t51_mem0 <= c_t0_t51

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	c_t0_t51_mem1 += MAS_MEM[7]
	S += 59 < c_t0_t51_mem1
	S += c_t0_t51_mem1 <= c_t0_t51

	c_t010 = S.Task('c_t010', length=2, delay_cost=1)
	c_t010 += alt(MAS)
	c_t010_in = S.Task('c_t010_in', length=1, delay_cost=1)
	c_t010_in += alt(MAS_in)
	S += c_t010_in*MAS_in[0]<=c_t010*MAS[0]

	S += c_t010_in*MAS_in[1]<=c_t010*MAS[1]

	S += c_t010_in*MAS_in[2]<=c_t010*MAS[2]

	S += c_t010_in*MAS_in[3]<=c_t010*MAS[3]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	c_t010_mem0 += MAS_MEM[0]
	S += 45 < c_t010_mem0
	S += c_t010_mem0 <= c_t010

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	c_t010_mem1 += MAS_MEM[7]
	S += 43 < c_t010_mem1
	S += c_t010_mem1 <= c_t010

	c_t1_t41 = S.Task('c_t1_t41', length=2, delay_cost=1)
	c_t1_t41 += alt(MAS)
	c_t1_t41_in = S.Task('c_t1_t41_in', length=1, delay_cost=1)
	c_t1_t41_in += alt(MAS_in)
	S += c_t1_t41_in*MAS_in[0]<=c_t1_t41*MAS[0]

	S += c_t1_t41_in*MAS_in[1]<=c_t1_t41*MAS[1]

	S += c_t1_t41_in*MAS_in[2]<=c_t1_t41*MAS[2]

	S += c_t1_t41_in*MAS_in[3]<=c_t1_t41*MAS[3]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	c_t1_t41_mem0 += MM_MEM[0]
	S += 67 < c_t1_t41_mem0
	S += c_t1_t41_mem0 <= c_t1_t41

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	c_t1_t41_mem1 += MAS_MEM[3]
	S += 52 < c_t1_t41_mem1
	S += c_t1_t41_mem1 <= c_t1_t41

	c_t1_s00 = S.Task('c_t1_s00', length=2, delay_cost=1)
	c_t1_s00 += alt(MAS)
	c_t1_s00_in = S.Task('c_t1_s00_in', length=1, delay_cost=1)
	c_t1_s00_in += alt(MAS_in)
	S += c_t1_s00_in*MAS_in[0]<=c_t1_s00*MAS[0]

	S += c_t1_s00_in*MAS_in[1]<=c_t1_s00*MAS[1]

	S += c_t1_s00_in*MAS_in[2]<=c_t1_s00*MAS[2]

	S += c_t1_s00_in*MAS_in[3]<=c_t1_s00*MAS[3]

	c_t1_s00_mem0 = S.Task('c_t1_s00_mem0', length=1, delay_cost=1)
	c_t1_s00_mem0 += MAS_MEM[4]
	S += 33 < c_t1_s00_mem0
	S += c_t1_s00_mem0 <= c_t1_s00

	c_t1_s00_mem1 = S.Task('c_t1_s00_mem1', length=1, delay_cost=1)
	c_t1_s00_mem1 += MAS_MEM[5]
	S += 56 < c_t1_s00_mem1
	S += c_t1_s00_mem1 <= c_t1_s00

	c_t1_s01 = S.Task('c_t1_s01', length=2, delay_cost=1)
	c_t1_s01 += alt(MAS)
	c_t1_s01_in = S.Task('c_t1_s01_in', length=1, delay_cost=1)
	c_t1_s01_in += alt(MAS_in)
	S += c_t1_s01_in*MAS_in[0]<=c_t1_s01*MAS[0]

	S += c_t1_s01_in*MAS_in[1]<=c_t1_s01*MAS[1]

	S += c_t1_s01_in*MAS_in[2]<=c_t1_s01*MAS[2]

	S += c_t1_s01_in*MAS_in[3]<=c_t1_s01*MAS[3]

	c_t1_s01_mem0 = S.Task('c_t1_s01_mem0', length=1, delay_cost=1)
	c_t1_s01_mem0 += MAS_MEM[4]
	S += 56 < c_t1_s01_mem0
	S += c_t1_s01_mem0 <= c_t1_s01

	c_t1_s01_mem1 = S.Task('c_t1_s01_mem1', length=1, delay_cost=1)
	c_t1_s01_mem1 += MAS_MEM[5]
	S += 33 < c_t1_s01_mem1
	S += c_t1_s01_mem1 <= c_t1_s01

	c_t1_t51 = S.Task('c_t1_t51', length=2, delay_cost=1)
	c_t1_t51 += alt(MAS)
	c_t1_t51_in = S.Task('c_t1_t51_in', length=1, delay_cost=1)
	c_t1_t51_in += alt(MAS_in)
	S += c_t1_t51_in*MAS_in[0]<=c_t1_t51*MAS[0]

	S += c_t1_t51_in*MAS_in[1]<=c_t1_t51*MAS[1]

	S += c_t1_t51_in*MAS_in[2]<=c_t1_t51*MAS[2]

	S += c_t1_t51_in*MAS_in[3]<=c_t1_t51*MAS[3]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	c_t1_t51_mem0 += MAS_MEM[6]
	S += 55 < c_t1_t51_mem0
	S += c_t1_t51_mem0 <= c_t1_t51

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	c_t1_t51_mem1 += MAS_MEM[5]
	S += 56 < c_t1_t51_mem1
	S += c_t1_t51_mem1 <= c_t1_t51

	c_t110 = S.Task('c_t110', length=2, delay_cost=1)
	c_t110 += alt(MAS)
	c_t110_in = S.Task('c_t110_in', length=1, delay_cost=1)
	c_t110_in += alt(MAS_in)
	S += c_t110_in*MAS_in[0]<=c_t110*MAS[0]

	S += c_t110_in*MAS_in[1]<=c_t110*MAS[1]

	S += c_t110_in*MAS_in[2]<=c_t110*MAS[2]

	S += c_t110_in*MAS_in[3]<=c_t110*MAS[3]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	c_t110_mem0 += MAS_MEM[6]
	S += 50 < c_t110_mem0
	S += c_t110_mem0 <= c_t110

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	c_t110_mem1 += MAS_MEM[1]
	S += 46 < c_t110_mem1
	S += c_t110_mem1 <= c_t110

	c_t2_t41 = S.Task('c_t2_t41', length=2, delay_cost=1)
	c_t2_t41 += alt(MAS)
	c_t2_t41_in = S.Task('c_t2_t41_in', length=1, delay_cost=1)
	c_t2_t41_in += alt(MAS_in)
	S += c_t2_t41_in*MAS_in[0]<=c_t2_t41*MAS[0]

	S += c_t2_t41_in*MAS_in[1]<=c_t2_t41*MAS[1]

	S += c_t2_t41_in*MAS_in[2]<=c_t2_t41*MAS[2]

	S += c_t2_t41_in*MAS_in[3]<=c_t2_t41*MAS[3]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	c_t2_t41_mem0 += MM_MEM[0]
	S += 62 < c_t2_t41_mem0
	S += c_t2_t41_mem0 <= c_t2_t41

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	c_t2_t41_mem1 += MAS_MEM[1]
	S += 47 < c_t2_t41_mem1
	S += c_t2_t41_mem1 <= c_t2_t41

	c_t2_s00 = S.Task('c_t2_s00', length=2, delay_cost=1)
	c_t2_s00 += alt(MAS)
	c_t2_s00_in = S.Task('c_t2_s00_in', length=1, delay_cost=1)
	c_t2_s00_in += alt(MAS_in)
	S += c_t2_s00_in*MAS_in[0]<=c_t2_s00*MAS[0]

	S += c_t2_s00_in*MAS_in[1]<=c_t2_s00*MAS[1]

	S += c_t2_s00_in*MAS_in[2]<=c_t2_s00*MAS[2]

	S += c_t2_s00_in*MAS_in[3]<=c_t2_s00*MAS[3]

	c_t2_s00_mem0 = S.Task('c_t2_s00_mem0', length=1, delay_cost=1)
	c_t2_s00_mem0 += MAS_MEM[2]
	S += 32 < c_t2_s00_mem0
	S += c_t2_s00_mem0 <= c_t2_s00

	c_t2_s00_mem1 = S.Task('c_t2_s00_mem1', length=1, delay_cost=1)
	c_t2_s00_mem1 += MAS_MEM[3]
	S += 57 < c_t2_s00_mem1
	S += c_t2_s00_mem1 <= c_t2_s00

	c_t2_s01 = S.Task('c_t2_s01', length=2, delay_cost=1)
	c_t2_s01 += alt(MAS)
	c_t2_s01_in = S.Task('c_t2_s01_in', length=1, delay_cost=1)
	c_t2_s01_in += alt(MAS_in)
	S += c_t2_s01_in*MAS_in[0]<=c_t2_s01*MAS[0]

	S += c_t2_s01_in*MAS_in[1]<=c_t2_s01*MAS[1]

	S += c_t2_s01_in*MAS_in[2]<=c_t2_s01*MAS[2]

	S += c_t2_s01_in*MAS_in[3]<=c_t2_s01*MAS[3]

	c_t2_s01_mem0 = S.Task('c_t2_s01_mem0', length=1, delay_cost=1)
	c_t2_s01_mem0 += MAS_MEM[2]
	S += 57 < c_t2_s01_mem0
	S += c_t2_s01_mem0 <= c_t2_s01

	c_t2_s01_mem1 = S.Task('c_t2_s01_mem1', length=1, delay_cost=1)
	c_t2_s01_mem1 += MAS_MEM[3]
	S += 32 < c_t2_s01_mem1
	S += c_t2_s01_mem1 <= c_t2_s01

	c_t2_t51 = S.Task('c_t2_t51', length=2, delay_cost=1)
	c_t2_t51 += alt(MAS)
	c_t2_t51_in = S.Task('c_t2_t51_in', length=1, delay_cost=1)
	c_t2_t51_in += alt(MAS_in)
	S += c_t2_t51_in*MAS_in[0]<=c_t2_t51*MAS[0]

	S += c_t2_t51_in*MAS_in[1]<=c_t2_t51*MAS[1]

	S += c_t2_t51_in*MAS_in[2]<=c_t2_t51*MAS[2]

	S += c_t2_t51_in*MAS_in[3]<=c_t2_t51*MAS[3]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	c_t2_t51_mem0 += MAS_MEM[0]
	S += 53 < c_t2_t51_mem0
	S += c_t2_t51_mem0 <= c_t2_t51

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	c_t2_t51_mem1 += MAS_MEM[3]
	S += 57 < c_t2_t51_mem1
	S += c_t2_t51_mem1 <= c_t2_t51

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage5MM1_stage2MAS4/FP12_LADDERMUL/schedule9.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

