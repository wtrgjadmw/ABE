from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 158
	S = Scenario("schedule7", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=4)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 0
	c_t1_t0_t1_in += MM_in[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 0
	c_t2_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 0
	c_t2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 1
	c_t0_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=1, delay_cost=1)
	S += c_t0_t1_t2 >= 1
	c_t0_t1_t2 += MAS[1]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=4, delay_cost=1)
	S += c_t1_t0_t1 >= 1
	c_t1_t0_t1 += MM[0]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 1
	c_t1_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	S += c_t1_t20 >= 1
	c_t1_t20 += MAS[2]

	c_t1_t21 = S.Task('c_t1_t21', length=1, delay_cost=1)
	S += c_t1_t21 >= 1
	c_t1_t21 += MAS[3]

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 1
	c_t2_t0_t1_in += MM_in[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=1, delay_cost=1)
	S += c_t2_t0_t2 >= 1
	c_t2_t0_t2 += MAS[0]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=1, delay_cost=1)
	S += c_t0_t0_t3 >= 2
	c_t0_t0_t3 += MAS[3]

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 2
	c_t0_t1_t0_in += MM_in[0]

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=1, delay_cost=1)
	S += c_t0_t1_t3 >= 2
	c_t0_t1_t3 += MAS[0]

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	S += c_t0_t20 >= 2
	c_t0_t20 += MAS[1]

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	S += c_t0_t31 >= 2
	c_t0_t31 += MAS[2]

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 2
	c_t1_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=4, delay_cost=1)
	S += c_t2_t0_t1 >= 2
	c_t2_t0_t1 += MM[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 2
	c_t2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 3
	c_t0_t0_t0_in += MM_in[0]

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=4, delay_cost=1)
	S += c_t0_t1_t0 >= 3
	c_t0_t1_t0 += MM[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 3
	c_t0_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=1, delay_cost=1)
	S += c_t1_t0_t2 >= 3
	c_t1_t0_t2 += MAS[1]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=1, delay_cost=1)
	S += c_t1_t0_t3 >= 3
	c_t1_t0_t3 += MAS[2]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=1, delay_cost=1)
	S += c_t1_t1_t3 >= 3
	c_t1_t1_t3 += MAS[3]

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 3
	c_t1_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	S += c_t1_t31 >= 3
	c_t1_t31 += MAS[0]

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=4, delay_cost=1)
	S += c_t0_t0_t0 >= 4
	c_t0_t0_t0 += MM[0]

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=1, delay_cost=1)
	S += c_t0_t0_t2 >= 4
	c_t0_t0_t2 += MAS[2]

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 4
	c_t0_t1_t1_in += MM_in[0]

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 4
	c_t0_t30 += MAS[0]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=1, delay_cost=1)
	S += c_t1_t1_t2 >= 4
	c_t1_t1_t2 += MAS[1]

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 4
	c_t1_t20_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=1, delay_cost=1)
	S += c_t2_t0_t3 >= 4
	c_t2_t0_t3 += MAS[3]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 4
	c_t2_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 5
	c_t0_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=4, delay_cost=1)
	S += c_t0_t1_t1 >= 5
	c_t0_t1_t1 += MM[0]

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	S += c_t0_t21 >= 5
	c_t0_t21 += MAS[0]

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 5
	c_t1_t30 += MAS[2]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 5
	c_t2_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 5
	c_t2_t1_t1_in += MM_in[0]

	c_t3101 = S.Task('c_t3101', length=1, delay_cost=1)
	S += c_t3101 >= 5
	c_t3101 += MAS[3]

	c_t3110 = S.Task('c_t3110', length=1, delay_cost=1)
	S += c_t3110 >= 5
	c_t3110 += MAS[1]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 6
	c_t0_t0_t1_in += MM_in[0]

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 6
	c_t0_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 6
	c_t0_t21_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=4, delay_cost=1)
	S += c_t2_t1_t1 >= 6
	c_t2_t1_t1 += MM[0]

	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=1, delay_cost=1)
	S += c_t2_t1_t3 >= 6
	c_t2_t1_t3 += MAS[2]

	c_t2_t21 = S.Task('c_t2_t21', length=1, delay_cost=1)
	S += c_t2_t21 >= 6
	c_t2_t21 += MAS[0]

	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	S += c_t2_t31 >= 6
	c_t2_t31 += MAS[3]

	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	S += c_t5010 >= 6
	c_t5010 += MAS[1]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=4, delay_cost=1)
	S += c_t0_t0_t1 >= 7
	c_t0_t0_t1 += MM[0]

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 7
	c_t1_t1_t1_in += MM_in[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 7
	c_t1_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 7
	c_t2_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	S += c_t3001 >= 7
	c_t3001 += MAS[1]

	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	S += c_t3010 >= 7
	c_t3010 += MAS[3]

	c_t3100 = S.Task('c_t3100', length=1, delay_cost=1)
	S += c_t3100 >= 7
	c_t3100 += MAS[0]

	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	S += c_t5000 >= 7
	c_t5000 += MAS[2]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 8
	c_t1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=4, delay_cost=1)
	S += c_t1_t1_t1 >= 8
	c_t1_t1_t1 += MM[0]

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 8
	c_t2_t0_t0_in += MM_in[0]

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 8
	c_t2_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t3111 = S.Task('c_t3111', length=1, delay_cost=1)
	S += c_t3111 >= 8
	c_t3111 += MAS[3]

	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	S += c_t4000 >= 8
	c_t4000 += MAS[0]

	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	S += c_t4010 >= 8
	c_t4010 += MAS[2]

	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	S += c_t5011 >= 8
	c_t5011 += MAS[1]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 9
	c_t0_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 9
	c_t1_t0_t0_in += MM_in[0]

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 9
	c_t1_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=4, delay_cost=1)
	S += c_t2_t0_t0 >= 9
	c_t2_t0_t0 += MM[0]

	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	S += c_t3000 >= 9
	c_t3000 += MAS[0]

	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	S += c_t3011 >= 9
	c_t3011 += MAS[1]

	c_t4100 = S.Task('c_t4100', length=1, delay_cost=1)
	S += c_t4100 >= 9
	c_t4100 += MAS[2]

	c_t5111 = S.Task('c_t5111', length=1, delay_cost=1)
	S += c_t5111 >= 9
	c_t5111 += MAS[3]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 10
	c_t0_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=4, delay_cost=1)
	S += c_t1_t0_t0 >= 10
	c_t1_t0_t0 += MM[0]

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 10
	c_t1_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 10
	c_t2_t1_t0_in += MM_in[0]

	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	S += c_t2_t20 >= 10
	c_t2_t20 += MAS[0]

	c_t4110 = S.Task('c_t4110', length=1, delay_cost=1)
	S += c_t4110 >= 10
	c_t4110 += MAS[2]

	c_t5100 = S.Task('c_t5100', length=1, delay_cost=1)
	S += c_t5100 >= 10
	c_t5100 += MAS[1]

	c_t5110 = S.Task('c_t5110', length=1, delay_cost=1)
	S += c_t5110 >= 10
	c_t5110 += MAS[3]

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 11
	c_t0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 11
	c_t0_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 11
	c_t1_t1_t0_in += MM_in[0]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=4, delay_cost=1)
	S += c_t2_t1_t0 >= 11
	c_t2_t1_t0 += MM[0]

	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=1, delay_cost=1)
	S += c_t2_t1_t2 >= 11
	c_t2_t1_t2 += MAS[3]

	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	S += c_t4011 >= 11
	c_t4011 += MAS[2]

	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	S += c_t5001 >= 11
	c_t5001 += MAS[0]

	c_t5101 = S.Task('c_t5101', length=1, delay_cost=1)
	S += c_t5101 >= 11
	c_t5101 += MAS[1]

	c_t0_t10_mem0 = S.Task('c_t0_t10_mem0', length=1, delay_cost=1)
	S += c_t0_t10_mem0 >= 12
	c_t0_t10_mem0 += MM_MEM[0]

	c_t0_t10_mem1 = S.Task('c_t0_t10_mem1', length=1, delay_cost=1)
	S += c_t0_t10_mem1 >= 12
	c_t0_t10_mem1 += MM_MEM[1]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 12
	c_t0_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 12
	c_t0_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=4, delay_cost=1)
	S += c_t1_t1_t0 >= 12
	c_t1_t1_t0 += MM[0]

	c_t1_t4_t1_in = S.Task('c_t1_t4_t1_in', length=1, delay_cost=1)
	S += c_t1_t4_t1_in >= 12
	c_t1_t4_t1_in += MM_in[0]

	c_t1_t4_t1_mem0 = S.Task('c_t1_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem0 >= 12
	c_t1_t4_t1_mem0 += MAS_MEM[6]

	c_t1_t4_t1_mem1 = S.Task('c_t1_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t1_mem1 >= 12
	c_t1_t4_t1_mem1 += MAS_MEM[1]

	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	S += c_t2_t30 >= 12
	c_t2_t30 += MAS[1]

	c_t3_t1_t3_mem0 = S.Task('c_t3_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem0 >= 12
	c_t3_t1_t3_mem0 += MAS_MEM[2]

	c_t3_t1_t3_mem1 = S.Task('c_t3_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t3_mem1 >= 12
	c_t3_t1_t3_mem1 += MAS_MEM[7]

	c_t3_t30_mem0 = S.Task('c_t3_t30_mem0', length=1, delay_cost=1)
	S += c_t3_t30_mem0 >= 12
	c_t3_t30_mem0 += MAS_MEM[0]

	c_t3_t30_mem1 = S.Task('c_t3_t30_mem1', length=1, delay_cost=1)
	S += c_t3_t30_mem1 >= 12
	c_t3_t30_mem1 += MAS_MEM[3]

	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	S += c_t4001 >= 12
	c_t4001 += MAS[0]

	c_t4101 = S.Task('c_t4101', length=1, delay_cost=1)
	S += c_t4101 >= 12
	c_t4101 += MAS[2]

	c_t4111 = S.Task('c_t4111', length=1, delay_cost=1)
	S += c_t4111 >= 12
	c_t4111 += MAS[3]

	c_t4_t1_t2_mem0 = S.Task('c_t4_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem0 >= 12
	c_t4_t1_t2_mem0 += MAS_MEM[4]

	c_t4_t1_t2_mem1 = S.Task('c_t4_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t2_mem1 >= 12
	c_t4_t1_t2_mem1 += MAS_MEM[5]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 13
	c_t0_t0_t2_mem0 += MAIN_MEM_r[0]

	c_t0_t10 = S.Task('c_t0_t10', length=1, delay_cost=1)
	S += c_t0_t10 >= 13
	c_t0_t10 += MAS[3]

	c_t1_t0_t4_in = S.Task('c_t1_t0_t4_in', length=1, delay_cost=1)
	S += c_t1_t0_t4_in >= 13
	c_t1_t0_t4_in += MM_in[0]

	c_t1_t0_t4_mem0 = S.Task('c_t1_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem0 >= 13
	c_t1_t0_t4_mem0 += MAS_MEM[2]

	c_t1_t0_t4_mem1 = S.Task('c_t1_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t4_mem1 >= 13
	c_t1_t0_t4_mem1 += MAS_MEM[5]

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 13
	c_t1_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t1 = S.Task('c_t1_t4_t1', length=4, delay_cost=1)
	S += c_t1_t4_t1 >= 13
	c_t1_t4_t1 += MM[0]

	c_t1_t4_t3_mem0 = S.Task('c_t1_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem0 >= 13
	c_t1_t4_t3_mem0 += MAS_MEM[4]

	c_t1_t4_t3_mem1 = S.Task('c_t1_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t3_mem1 >= 13
	c_t1_t4_t3_mem1 += MAS_MEM[1]

	c_t2_t0_t5_mem0 = S.Task('c_t2_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem0 >= 13
	c_t2_t0_t5_mem0 += MM_MEM[0]

	c_t2_t0_t5_mem1 = S.Task('c_t2_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t5_mem1 >= 13
	c_t2_t0_t5_mem1 += MM_MEM[1]

	c_t3_t0_t2_mem0 = S.Task('c_t3_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem0 >= 13
	c_t3_t0_t2_mem0 += MAS_MEM[0]

	c_t3_t0_t2_mem1 = S.Task('c_t3_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t2_mem1 >= 13
	c_t3_t0_t2_mem1 += MAS_MEM[3]

	c_t3_t1_t3 = S.Task('c_t3_t1_t3', length=1, delay_cost=1)
	S += c_t3_t1_t3 >= 13
	c_t3_t1_t3 += MAS[0]

	c_t3_t30 = S.Task('c_t3_t30', length=1, delay_cost=1)
	S += c_t3_t30 >= 13
	c_t3_t30 += MAS[1]

	c_t3_t31_mem0 = S.Task('c_t3_t31_mem0', length=1, delay_cost=1)
	S += c_t3_t31_mem0 >= 13
	c_t3_t31_mem0 += MAS_MEM[6]

	c_t3_t31_mem1 = S.Task('c_t3_t31_mem1', length=1, delay_cost=1)
	S += c_t3_t31_mem1 >= 13
	c_t3_t31_mem1 += MAS_MEM[7]

	c_t4_t1_t2 = S.Task('c_t4_t1_t2', length=1, delay_cost=1)
	S += c_t4_t1_t2 >= 13
	c_t4_t1_t2 += MAS[2]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 14
	c_t0_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t4 = S.Task('c_t1_t0_t4', length=4, delay_cost=1)
	S += c_t1_t0_t4 >= 14
	c_t1_t0_t4 += MM[0]

	c_t1_t4_t3 = S.Task('c_t1_t4_t3', length=1, delay_cost=1)
	S += c_t1_t4_t3 >= 14
	c_t1_t4_t3 += MAS[0]

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 14
	c_t2_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t5 = S.Task('c_t2_t0_t5', length=1, delay_cost=1)
	S += c_t2_t0_t5 >= 14
	c_t2_t0_t5 += MAS[3]

	c_t2_t10_mem0 = S.Task('c_t2_t10_mem0', length=1, delay_cost=1)
	S += c_t2_t10_mem0 >= 14
	c_t2_t10_mem0 += MM_MEM[0]

	c_t2_t10_mem1 = S.Task('c_t2_t10_mem1', length=1, delay_cost=1)
	S += c_t2_t10_mem1 >= 14
	c_t2_t10_mem1 += MM_MEM[1]

	c_t2_t1_t4_in = S.Task('c_t2_t1_t4_in', length=1, delay_cost=1)
	S += c_t2_t1_t4_in >= 14
	c_t2_t1_t4_in += MM_in[0]

	c_t2_t1_t4_mem0 = S.Task('c_t2_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem0 >= 14
	c_t2_t1_t4_mem0 += MAS_MEM[6]

	c_t2_t1_t4_mem1 = S.Task('c_t2_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t4_mem1 >= 14
	c_t2_t1_t4_mem1 += MAS_MEM[5]

	c_t2_t4_t2_mem0 = S.Task('c_t2_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem0 >= 14
	c_t2_t4_t2_mem0 += MAS_MEM[0]

	c_t2_t4_t2_mem1 = S.Task('c_t2_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t2_mem1 >= 14
	c_t2_t4_t2_mem1 += MAS_MEM[1]

	c_t3_t0_t2 = S.Task('c_t3_t0_t2', length=1, delay_cost=1)
	S += c_t3_t0_t2 >= 14
	c_t3_t0_t2 += MAS[1]

	c_t3_t21_mem0 = S.Task('c_t3_t21_mem0', length=1, delay_cost=1)
	S += c_t3_t21_mem0 >= 14
	c_t3_t21_mem0 += MAS_MEM[2]

	c_t3_t21_mem1 = S.Task('c_t3_t21_mem1', length=1, delay_cost=1)
	S += c_t3_t21_mem1 >= 14
	c_t3_t21_mem1 += MAS_MEM[3]

	c_t3_t31 = S.Task('c_t3_t31', length=1, delay_cost=1)
	S += c_t3_t31 >= 14
	c_t3_t31 += MAS[2]

	c_t4_t1_t3_mem0 = S.Task('c_t4_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem0 >= 14
	c_t4_t1_t3_mem0 += MAS_MEM[4]

	c_t4_t1_t3_mem1 = S.Task('c_t4_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t3_mem1 >= 14
	c_t4_t1_t3_mem1 += MAS_MEM[7]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 15
	c_t0_t30_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t5_mem0 = S.Task('c_t1_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem0 >= 15
	c_t1_t1_t5_mem0 += MM_MEM[0]

	c_t1_t1_t5_mem1 = S.Task('c_t1_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t5_mem1 >= 15
	c_t1_t1_t5_mem1 += MM_MEM[1]

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 15
	c_t2_t0_t0_mem1 += MAIN_MEM_r[1]

	c_t2_t10 = S.Task('c_t2_t10', length=1, delay_cost=1)
	S += c_t2_t10 >= 15
	c_t2_t10 += MAS[1]

	c_t2_t1_t4 = S.Task('c_t2_t1_t4', length=4, delay_cost=1)
	S += c_t2_t1_t4 >= 15
	c_t2_t1_t4 += MM[0]

	c_t2_t4_t2 = S.Task('c_t2_t4_t2', length=1, delay_cost=1)
	S += c_t2_t4_t2 >= 15
	c_t2_t4_t2 += MAS[3]

	c_t2_t4_t3_mem0 = S.Task('c_t2_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem0 >= 15
	c_t2_t4_t3_mem0 += MAS_MEM[2]

	c_t2_t4_t3_mem1 = S.Task('c_t2_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t3_mem1 >= 15
	c_t2_t4_t3_mem1 += MAS_MEM[7]

	c_t3_t1_t0_in = S.Task('c_t3_t1_t0_in', length=1, delay_cost=1)
	S += c_t3_t1_t0_in >= 15
	c_t3_t1_t0_in += MM_in[0]

	c_t3_t1_t0_mem0 = S.Task('c_t3_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem0 >= 15
	c_t3_t1_t0_mem0 += MAS_MEM[6]

	c_t3_t1_t0_mem1 = S.Task('c_t3_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t0_mem1 >= 15
	c_t3_t1_t0_mem1 += MAS_MEM[3]

	c_t3_t21 = S.Task('c_t3_t21', length=1, delay_cost=1)
	S += c_t3_t21 >= 15
	c_t3_t21 += MAS[0]

	c_t4_t0_t2_mem0 = S.Task('c_t4_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem0 >= 15
	c_t4_t0_t2_mem0 += MAS_MEM[0]

	c_t4_t0_t2_mem1 = S.Task('c_t4_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t2_mem1 >= 15
	c_t4_t0_t2_mem1 += MAS_MEM[1]

	c_t4_t0_t3_mem0 = S.Task('c_t4_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem0 >= 15
	c_t4_t0_t3_mem0 += MAS_MEM[4]

	c_t4_t0_t3_mem1 = S.Task('c_t4_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t3_mem1 >= 15
	c_t4_t0_t3_mem1 += MAS_MEM[5]

	c_t4_t1_t3 = S.Task('c_t4_t1_t3', length=1, delay_cost=1)
	S += c_t4_t1_t3 >= 15
	c_t4_t1_t3 += MAS[2]

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 16
	c_t0_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t0_in = S.Task('c_t0_t4_t0_in', length=1, delay_cost=1)
	S += c_t0_t4_t0_in >= 16
	c_t0_t4_t0_in += MM_in[0]

	c_t0_t4_t0_mem0 = S.Task('c_t0_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem0 >= 16
	c_t0_t4_t0_mem0 += MAS_MEM[2]

	c_t0_t4_t0_mem1 = S.Task('c_t0_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t0_mem1 >= 16
	c_t0_t4_t0_mem1 += MAS_MEM[1]

	c_t0_t4_t3_mem0 = S.Task('c_t0_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem0 >= 16
	c_t0_t4_t3_mem0 += MAS_MEM[0]

	c_t0_t4_t3_mem1 = S.Task('c_t0_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t3_mem1 >= 16
	c_t0_t4_t3_mem1 += MAS_MEM[5]

	c_t1_t10_mem0 = S.Task('c_t1_t10_mem0', length=1, delay_cost=1)
	S += c_t1_t10_mem0 >= 16
	c_t1_t10_mem0 += MM_MEM[0]

	c_t1_t10_mem1 = S.Task('c_t1_t10_mem1', length=1, delay_cost=1)
	S += c_t1_t10_mem1 >= 16
	c_t1_t10_mem1 += MM_MEM[1]

	c_t1_t1_t5 = S.Task('c_t1_t1_t5', length=1, delay_cost=1)
	S += c_t1_t1_t5 >= 16
	c_t1_t1_t5 += MAS[2]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 16
	c_t1_t20_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t2_mem0 = S.Task('c_t1_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem0 >= 16
	c_t1_t4_t2_mem0 += MAS_MEM[4]

	c_t1_t4_t2_mem1 = S.Task('c_t1_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t2_mem1 >= 16
	c_t1_t4_t2_mem1 += MAS_MEM[7]

	c_t2_t4_t3 = S.Task('c_t2_t4_t3', length=1, delay_cost=1)
	S += c_t2_t4_t3 >= 16
	c_t2_t4_t3 += MAS[3]

	c_t3_t1_t0 = S.Task('c_t3_t1_t0', length=4, delay_cost=1)
	S += c_t3_t1_t0 >= 16
	c_t3_t1_t0 += MM[0]

	c_t3_t1_t2_mem0 = S.Task('c_t3_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem0 >= 16
	c_t3_t1_t2_mem0 += MAS_MEM[6]

	c_t3_t1_t2_mem1 = S.Task('c_t3_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t2_mem1 >= 16
	c_t3_t1_t2_mem1 += MAS_MEM[3]

	c_t4_t0_t2 = S.Task('c_t4_t0_t2', length=1, delay_cost=1)
	S += c_t4_t0_t2 >= 16
	c_t4_t0_t2 += MAS[1]

	c_t4_t0_t3 = S.Task('c_t4_t0_t3', length=1, delay_cost=1)
	S += c_t4_t0_t3 >= 16
	c_t4_t0_t3 += MAS[0]

	c_t0_t4_t0 = S.Task('c_t0_t4_t0', length=4, delay_cost=1)
	S += c_t0_t4_t0 >= 17
	c_t0_t4_t0 += MM[0]

	c_t0_t4_t2_mem0 = S.Task('c_t0_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem0 >= 17
	c_t0_t4_t2_mem0 += MAS_MEM[2]

	c_t0_t4_t2_mem1 = S.Task('c_t0_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t2_mem1 >= 17
	c_t0_t4_t2_mem1 += MAS_MEM[1]

	c_t0_t4_t3 = S.Task('c_t0_t4_t3', length=1, delay_cost=1)
	S += c_t0_t4_t3 >= 17
	c_t0_t4_t3 += MAS[2]

	c_t1_t10 = S.Task('c_t1_t10', length=1, delay_cost=1)
	S += c_t1_t10 >= 17
	c_t1_t10 += MAS[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 17
	c_t1_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 17
	c_t1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t4_t2 = S.Task('c_t1_t4_t2', length=1, delay_cost=1)
	S += c_t1_t4_t2 >= 17
	c_t1_t4_t2 += MAS[3]

	c_t2_t1_t5_mem0 = S.Task('c_t2_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem0 >= 17
	c_t2_t1_t5_mem0 += MM_MEM[0]

	c_t2_t1_t5_mem1 = S.Task('c_t2_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t5_mem1 >= 17
	c_t2_t1_t5_mem1 += MM_MEM[1]

	c_t3_t1_t2 = S.Task('c_t3_t1_t2', length=1, delay_cost=1)
	S += c_t3_t1_t2 >= 17
	c_t3_t1_t2 += MAS[1]

	c_t3_t20_mem0 = S.Task('c_t3_t20_mem0', length=1, delay_cost=1)
	S += c_t3_t20_mem0 >= 17
	c_t3_t20_mem0 += MAS_MEM[0]

	c_t3_t20_mem1 = S.Task('c_t3_t20_mem1', length=1, delay_cost=1)
	S += c_t3_t20_mem1 >= 17
	c_t3_t20_mem1 += MAS_MEM[7]

	c_t4_t1_t0_in = S.Task('c_t4_t1_t0_in', length=1, delay_cost=1)
	S += c_t4_t1_t0_in >= 17
	c_t4_t1_t0_in += MM_in[0]

	c_t4_t1_t0_mem0 = S.Task('c_t4_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem0 >= 17
	c_t4_t1_t0_mem0 += MAS_MEM[4]

	c_t4_t1_t0_mem1 = S.Task('c_t4_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t0_mem1 >= 17
	c_t4_t1_t0_mem1 += MAS_MEM[5]

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 18
	c_t0_t0_t1_mem1 += MAIN_MEM_r[1]

	c_t0_t4_t2 = S.Task('c_t0_t4_t2', length=1, delay_cost=1)
	S += c_t0_t4_t2 >= 18
	c_t0_t4_t2 += MAS[3]

	c_t1_t0_t5_mem0 = S.Task('c_t1_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem0 >= 18
	c_t1_t0_t5_mem0 += MM_MEM[0]

	c_t1_t0_t5_mem1 = S.Task('c_t1_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t5_mem1 >= 18
	c_t1_t0_t5_mem1 += MM_MEM[1]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 18
	c_t1_t31_mem0 += MAIN_MEM_r[0]

	c_t1_t4_t0_in = S.Task('c_t1_t4_t0_in', length=1, delay_cost=1)
	S += c_t1_t4_t0_in >= 18
	c_t1_t4_t0_in += MM_in[0]

	c_t1_t4_t0_mem0 = S.Task('c_t1_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem0 >= 18
	c_t1_t4_t0_mem0 += MAS_MEM[4]

	c_t1_t4_t0_mem1 = S.Task('c_t1_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t0_mem1 >= 18
	c_t1_t4_t0_mem1 += MAS_MEM[5]

	c_t2_t1_t5 = S.Task('c_t2_t1_t5', length=1, delay_cost=1)
	S += c_t2_t1_t5 >= 18
	c_t2_t1_t5 += MAS[0]

	c_t3_t0_t3_mem0 = S.Task('c_t3_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem0 >= 18
	c_t3_t0_t3_mem0 += MAS_MEM[0]

	c_t3_t0_t3_mem1 = S.Task('c_t3_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t3_mem1 >= 18
	c_t3_t0_t3_mem1 += MAS_MEM[7]

	c_t3_t20 = S.Task('c_t3_t20', length=1, delay_cost=1)
	S += c_t3_t20 >= 18
	c_t3_t20 += MAS[1]

	c_t4_t1_t0 = S.Task('c_t4_t1_t0', length=4, delay_cost=1)
	S += c_t4_t1_t0 >= 18
	c_t4_t1_t0 += MM[0]

	c_t5_t1_t2_mem0 = S.Task('c_t5_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem0 >= 18
	c_t5_t1_t2_mem0 += MAS_MEM[2]

	c_t5_t1_t2_mem1 = S.Task('c_t5_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t2_mem1 >= 18
	c_t5_t1_t2_mem1 += MAS_MEM[3]

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 19
	c_t0_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t4_in = S.Task('c_t0_t1_t4_in', length=1, delay_cost=1)
	S += c_t0_t1_t4_in >= 19
	c_t0_t1_t4_in += MM_in[0]

	c_t0_t1_t4_mem0 = S.Task('c_t0_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem0 >= 19
	c_t0_t1_t4_mem0 += MAS_MEM[2]

	c_t0_t1_t4_mem1 = S.Task('c_t0_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t4_mem1 >= 19
	c_t0_t1_t4_mem1 += MAS_MEM[1]

	c_t1_t00_mem0 = S.Task('c_t1_t00_mem0', length=1, delay_cost=1)
	S += c_t1_t00_mem0 >= 19
	c_t1_t00_mem0 += MM_MEM[0]

	c_t1_t00_mem1 = S.Task('c_t1_t00_mem1', length=1, delay_cost=1)
	S += c_t1_t00_mem1 >= 19
	c_t1_t00_mem1 += MM_MEM[1]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 19
	c_t1_t0_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t5 = S.Task('c_t1_t0_t5', length=1, delay_cost=1)
	S += c_t1_t0_t5 >= 19
	c_t1_t0_t5 += MAS[2]

	c_t1_t4_t0 = S.Task('c_t1_t4_t0', length=4, delay_cost=1)
	S += c_t1_t4_t0 >= 19
	c_t1_t4_t0 += MM[0]

	c_t3_t0_t3 = S.Task('c_t3_t0_t3', length=1, delay_cost=1)
	S += c_t3_t0_t3 >= 19
	c_t3_t0_t3 += MAS[1]

	c_t4_t20_mem0 = S.Task('c_t4_t20_mem0', length=1, delay_cost=1)
	S += c_t4_t20_mem0 >= 19
	c_t4_t20_mem0 += MAS_MEM[0]

	c_t4_t20_mem1 = S.Task('c_t4_t20_mem1', length=1, delay_cost=1)
	S += c_t4_t20_mem1 >= 19
	c_t4_t20_mem1 += MAS_MEM[5]

	c_t5_t1_t2 = S.Task('c_t5_t1_t2', length=1, delay_cost=1)
	S += c_t5_t1_t2 >= 19
	c_t5_t1_t2 += MAS[0]

	c_t5_t1_t3_mem0 = S.Task('c_t5_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem0 >= 19
	c_t5_t1_t3_mem0 += MAS_MEM[6]

	c_t5_t1_t3_mem1 = S.Task('c_t5_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t3_mem1 >= 19
	c_t5_t1_t3_mem1 += MAS_MEM[7]

	c_t5_t20_mem0 = S.Task('c_t5_t20_mem0', length=1, delay_cost=1)
	S += c_t5_t20_mem0 >= 19
	c_t5_t20_mem0 += MAS_MEM[4]

	c_t5_t20_mem1 = S.Task('c_t5_t20_mem1', length=1, delay_cost=1)
	S += c_t5_t20_mem1 >= 19
	c_t5_t20_mem1 += MAS_MEM[3]

	c_t0_t1_t4 = S.Task('c_t0_t1_t4', length=4, delay_cost=1)
	S += c_t0_t1_t4 >= 20
	c_t0_t1_t4 += MM[0]

	c_t0_t1_t5_mem0 = S.Task('c_t0_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem0 >= 20
	c_t0_t1_t5_mem0 += MM_MEM[0]

	c_t0_t1_t5_mem1 = S.Task('c_t0_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t5_mem1 >= 20
	c_t0_t1_t5_mem1 += MM_MEM[1]

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 20
	c_t0_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t00 = S.Task('c_t1_t00', length=1, delay_cost=1)
	S += c_t1_t00 >= 20
	c_t1_t00 += MAS[3]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 20
	c_t1_t0_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t0_t4_in = S.Task('c_t2_t0_t4_in', length=1, delay_cost=1)
	S += c_t2_t0_t4_in >= 20
	c_t2_t0_t4_in += MM_in[0]

	c_t2_t0_t4_mem0 = S.Task('c_t2_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem0 >= 20
	c_t2_t0_t4_mem0 += MAS_MEM[0]

	c_t2_t0_t4_mem1 = S.Task('c_t2_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t4_mem1 >= 20
	c_t2_t0_t4_mem1 += MAS_MEM[7]

	c_t4_t20 = S.Task('c_t4_t20', length=1, delay_cost=1)
	S += c_t4_t20 >= 20
	c_t4_t20 += MAS[1]

	c_t5_t0_t2_mem0 = S.Task('c_t5_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem0 >= 20
	c_t5_t0_t2_mem0 += MAS_MEM[4]

	c_t5_t0_t2_mem1 = S.Task('c_t5_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t2_mem1 >= 20
	c_t5_t0_t2_mem1 += MAS_MEM[1]

	c_t5_t0_t3_mem0 = S.Task('c_t5_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem0 >= 20
	c_t5_t0_t3_mem0 += MAS_MEM[2]

	c_t5_t0_t3_mem1 = S.Task('c_t5_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t3_mem1 >= 20
	c_t5_t0_t3_mem1 += MAS_MEM[3]

	c_t5_t1_t3 = S.Task('c_t5_t1_t3', length=1, delay_cost=1)
	S += c_t5_t1_t3 >= 20
	c_t5_t1_t3 += MAS[0]

	c_t5_t20 = S.Task('c_t5_t20', length=1, delay_cost=1)
	S += c_t5_t20 >= 20
	c_t5_t20 += MAS[2]

	c_t0_t0_t5_mem0 = S.Task('c_t0_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem0 >= 21
	c_t0_t0_t5_mem0 += MM_MEM[0]

	c_t0_t0_t5_mem1 = S.Task('c_t0_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t5_mem1 >= 21
	c_t0_t0_t5_mem1 += MM_MEM[1]

	c_t0_t1_t5 = S.Task('c_t0_t1_t5', length=1, delay_cost=1)
	S += c_t0_t1_t5 >= 21
	c_t0_t1_t5 += MAS[3]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 21
	c_t1_t21_mem0 += MAIN_MEM_r[0]

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 21
	c_t1_t21_mem1 += MAIN_MEM_r[1]

	c_t1_t50_mem0 = S.Task('c_t1_t50_mem0', length=1, delay_cost=1)
	S += c_t1_t50_mem0 >= 21
	c_t1_t50_mem0 += MAS_MEM[6]

	c_t1_t50_mem1 = S.Task('c_t1_t50_mem1', length=1, delay_cost=1)
	S += c_t1_t50_mem1 >= 21
	c_t1_t50_mem1 += MAS_MEM[1]

	c_t2_t0_t4 = S.Task('c_t2_t0_t4', length=4, delay_cost=1)
	S += c_t2_t0_t4 >= 21
	c_t2_t0_t4 += MM[0]

	c_t2_t4_t1_in = S.Task('c_t2_t4_t1_in', length=1, delay_cost=1)
	S += c_t2_t4_t1_in >= 21
	c_t2_t4_t1_in += MM_in[0]

	c_t2_t4_t1_mem0 = S.Task('c_t2_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem0 >= 21
	c_t2_t4_t1_mem0 += MAS_MEM[0]

	c_t2_t4_t1_mem1 = S.Task('c_t2_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t1_mem1 >= 21
	c_t2_t4_t1_mem1 += MAS_MEM[7]

	c_t4_t30_mem0 = S.Task('c_t4_t30_mem0', length=1, delay_cost=1)
	S += c_t4_t30_mem0 >= 21
	c_t4_t30_mem0 += MAS_MEM[4]

	c_t4_t30_mem1 = S.Task('c_t4_t30_mem1', length=1, delay_cost=1)
	S += c_t4_t30_mem1 >= 21
	c_t4_t30_mem1 += MAS_MEM[5]

	c_t5_t0_t2 = S.Task('c_t5_t0_t2', length=1, delay_cost=1)
	S += c_t5_t0_t2 >= 21
	c_t5_t0_t2 += MAS[0]

	c_t5_t0_t3 = S.Task('c_t5_t0_t3', length=1, delay_cost=1)
	S += c_t5_t0_t3 >= 21
	c_t5_t0_t3 += MAS[2]

	c_t0_t0_t5 = S.Task('c_t0_t0_t5', length=1, delay_cost=1)
	S += c_t0_t0_t5 >= 22
	c_t0_t0_t5 += MAS[3]

	c_t1_t50 = S.Task('c_t1_t50', length=1, delay_cost=1)
	S += c_t1_t50 >= 22
	c_t1_t50 += MAS[1]

	c_t2_t00_mem0 = S.Task('c_t2_t00_mem0', length=1, delay_cost=1)
	S += c_t2_t00_mem0 >= 22
	c_t2_t00_mem0 += MM_MEM[0]

	c_t2_t00_mem1 = S.Task('c_t2_t00_mem1', length=1, delay_cost=1)
	S += c_t2_t00_mem1 >= 22
	c_t2_t00_mem1 += MM_MEM[1]

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 22
	c_t2_t0_t3_mem1 += MAIN_MEM_r[1]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 22
	c_t2_t1_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t4_t1 = S.Task('c_t2_t4_t1', length=4, delay_cost=1)
	S += c_t2_t4_t1 >= 22
	c_t2_t4_t1 += MM[0]

	c_t3_t4_t2_mem0 = S.Task('c_t3_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem0 >= 22
	c_t3_t4_t2_mem0 += MAS_MEM[2]

	c_t3_t4_t2_mem1 = S.Task('c_t3_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t2_mem1 >= 22
	c_t3_t4_t2_mem1 += MAS_MEM[1]

	c_t4_t0_t1_in = S.Task('c_t4_t0_t1_in', length=1, delay_cost=1)
	S += c_t4_t0_t1_in >= 22
	c_t4_t0_t1_in += MM_in[0]

	c_t4_t0_t1_mem0 = S.Task('c_t4_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem0 >= 22
	c_t4_t0_t1_mem0 += MAS_MEM[0]

	c_t4_t0_t1_mem1 = S.Task('c_t4_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t1_mem1 >= 22
	c_t4_t0_t1_mem1 += MAS_MEM[5]

	c_t4_t30 = S.Task('c_t4_t30', length=1, delay_cost=1)
	S += c_t4_t30 >= 22
	c_t4_t30 += MAS[0]

	c_t4_t31_mem0 = S.Task('c_t4_t31_mem0', length=1, delay_cost=1)
	S += c_t4_t31_mem0 >= 22
	c_t4_t31_mem0 += MAS_MEM[4]

	c_t4_t31_mem1 = S.Task('c_t4_t31_mem1', length=1, delay_cost=1)
	S += c_t4_t31_mem1 >= 22
	c_t4_t31_mem1 += MAS_MEM[7]

	c_t0_t00_mem0 = S.Task('c_t0_t00_mem0', length=1, delay_cost=1)
	S += c_t0_t00_mem0 >= 23
	c_t0_t00_mem0 += MM_MEM[0]

	c_t0_t00_mem1 = S.Task('c_t0_t00_mem1', length=1, delay_cost=1)
	S += c_t0_t00_mem1 >= 23
	c_t0_t00_mem1 += MM_MEM[1]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 23
	c_t1_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 23
	c_t1_t1_t1_mem1 += MAIN_MEM_r[1]

	c_t2_t00 = S.Task('c_t2_t00', length=1, delay_cost=1)
	S += c_t2_t00 >= 23
	c_t2_t00 += MAS[3]

	c_t3_t1_t1_in = S.Task('c_t3_t1_t1_in', length=1, delay_cost=1)
	S += c_t3_t1_t1_in >= 23
	c_t3_t1_t1_in += MM_in[0]

	c_t3_t1_t1_mem0 = S.Task('c_t3_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem0 >= 23
	c_t3_t1_t1_mem0 += MAS_MEM[2]

	c_t3_t1_t1_mem1 = S.Task('c_t3_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t1_mem1 >= 23
	c_t3_t1_t1_mem1 += MAS_MEM[7]

	c_t3_t4_t2 = S.Task('c_t3_t4_t2', length=1, delay_cost=1)
	S += c_t3_t4_t2 >= 23
	c_t3_t4_t2 += MAS[0]

	c_t4_t0_t1 = S.Task('c_t4_t0_t1', length=4, delay_cost=1)
	S += c_t4_t0_t1 >= 23
	c_t4_t0_t1 += MM[0]

	c_t4_t31 = S.Task('c_t4_t31', length=1, delay_cost=1)
	S += c_t4_t31 >= 23
	c_t4_t31 += MAS[1]

	c_t5_t21_mem0 = S.Task('c_t5_t21_mem0', length=1, delay_cost=1)
	S += c_t5_t21_mem0 >= 23
	c_t5_t21_mem0 += MAS_MEM[0]

	c_t5_t21_mem1 = S.Task('c_t5_t21_mem1', length=1, delay_cost=1)
	S += c_t5_t21_mem1 >= 23
	c_t5_t21_mem1 += MAS_MEM[3]

	c_t0_t00 = S.Task('c_t0_t00', length=1, delay_cost=1)
	S += c_t0_t00 >= 24
	c_t0_t00 += MAS[1]

	c_t0_t0_t4_in = S.Task('c_t0_t0_t4_in', length=1, delay_cost=1)
	S += c_t0_t0_t4_in >= 24
	c_t0_t0_t4_in += MM_in[0]

	c_t0_t0_t4_mem0 = S.Task('c_t0_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem0 >= 24
	c_t0_t0_t4_mem0 += MAS_MEM[4]

	c_t0_t0_t4_mem1 = S.Task('c_t0_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t4_mem1 >= 24
	c_t0_t0_t4_mem1 += MAS_MEM[7]

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 24
	c_t0_t1_t0_mem1 += MAIN_MEM_r[1]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 24
	c_t0_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t2_t11_mem0 = S.Task('c_t2_t11_mem0', length=1, delay_cost=1)
	S += c_t2_t11_mem0 >= 24
	c_t2_t11_mem0 += MM_MEM[0]

	c_t2_t11_mem1 = S.Task('c_t2_t11_mem1', length=1, delay_cost=1)
	S += c_t2_t11_mem1 >= 24
	c_t2_t11_mem1 += MAS_MEM[1]

	c_t2_t50_mem0 = S.Task('c_t2_t50_mem0', length=1, delay_cost=1)
	S += c_t2_t50_mem0 >= 24
	c_t2_t50_mem0 += MAS_MEM[6]

	c_t2_t50_mem1 = S.Task('c_t2_t50_mem1', length=1, delay_cost=1)
	S += c_t2_t50_mem1 >= 24
	c_t2_t50_mem1 += MAS_MEM[3]

	c_t3_t1_t1 = S.Task('c_t3_t1_t1', length=4, delay_cost=1)
	S += c_t3_t1_t1 >= 24
	c_t3_t1_t1 += MM[0]

	c_t4_t21_mem0 = S.Task('c_t4_t21_mem0', length=1, delay_cost=1)
	S += c_t4_t21_mem0 >= 24
	c_t4_t21_mem0 += MAS_MEM[0]

	c_t4_t21_mem1 = S.Task('c_t4_t21_mem1', length=1, delay_cost=1)
	S += c_t4_t21_mem1 >= 24
	c_t4_t21_mem1 += MAS_MEM[5]

	c_t5_t21 = S.Task('c_t5_t21', length=1, delay_cost=1)
	S += c_t5_t21 >= 24
	c_t5_t21 += MAS[0]

	c_t0_t0_t4 = S.Task('c_t0_t0_t4', length=4, delay_cost=1)
	S += c_t0_t0_t4 >= 25
	c_t0_t0_t4 += MM[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 25
	c_t0_t1_t0_mem0 += MAIN_MEM_r[0]

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 25
	c_t0_t30_mem1 += MAIN_MEM_r[1]

	c_t1_t01_mem0 = S.Task('c_t1_t01_mem0', length=1, delay_cost=1)
	S += c_t1_t01_mem0 >= 25
	c_t1_t01_mem0 += MM_MEM[0]

	c_t1_t01_mem1 = S.Task('c_t1_t01_mem1', length=1, delay_cost=1)
	S += c_t1_t01_mem1 >= 25
	c_t1_t01_mem1 += MAS_MEM[5]

	c_t1_t1_t4_in = S.Task('c_t1_t1_t4_in', length=1, delay_cost=1)
	S += c_t1_t1_t4_in >= 25
	c_t1_t1_t4_in += MM_in[0]

	c_t1_t1_t4_mem0 = S.Task('c_t1_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem0 >= 25
	c_t1_t1_t4_mem0 += MAS_MEM[2]

	c_t1_t1_t4_mem1 = S.Task('c_t1_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t4_mem1 >= 25
	c_t1_t1_t4_mem1 += MAS_MEM[7]

	c_t2_t11 = S.Task('c_t2_t11', length=1, delay_cost=1)
	S += c_t2_t11 >= 25
	c_t2_t11 += MAS[1]

	c_t2_t50 = S.Task('c_t2_t50', length=1, delay_cost=1)
	S += c_t2_t50 >= 25
	c_t2_t50 += MAS[2]

	c_t4_t21 = S.Task('c_t4_t21', length=1, delay_cost=1)
	S += c_t4_t21 >= 25
	c_t4_t21 += MAS[0]

	c_t4_t4_t3_mem0 = S.Task('c_t4_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem0 >= 25
	c_t4_t4_t3_mem0 += MAS_MEM[0]

	c_t4_t4_t3_mem1 = S.Task('c_t4_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t3_mem1 >= 25
	c_t4_t4_t3_mem1 += MAS_MEM[3]

	c_t5_t4_t2_mem0 = S.Task('c_t5_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem0 >= 25
	c_t5_t4_t2_mem0 += MAS_MEM[4]

	c_t5_t4_t2_mem1 = S.Task('c_t5_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t2_mem1 >= 25
	c_t5_t4_t2_mem1 += MAS_MEM[1]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 26
	c_t0_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t01 = S.Task('c_t1_t01', length=1, delay_cost=1)
	S += c_t1_t01 >= 26
	c_t1_t01 += MAS[2]

	c_t1_t1_t4 = S.Task('c_t1_t1_t4', length=4, delay_cost=1)
	S += c_t1_t1_t4 >= 26
	c_t1_t1_t4 += MM[0]

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 26
	c_t1_t31_mem1 += MAIN_MEM_r[1]

	c_t1_t40_mem0 = S.Task('c_t1_t40_mem0', length=1, delay_cost=1)
	S += c_t1_t40_mem0 >= 26
	c_t1_t40_mem0 += MM_MEM[0]

	c_t1_t40_mem1 = S.Task('c_t1_t40_mem1', length=1, delay_cost=1)
	S += c_t1_t40_mem1 >= 26
	c_t1_t40_mem1 += MM_MEM[1]

	c_t4_t0_t0_in = S.Task('c_t4_t0_t0_in', length=1, delay_cost=1)
	S += c_t4_t0_t0_in >= 26
	c_t4_t0_t0_in += MM_in[0]

	c_t4_t0_t0_mem0 = S.Task('c_t4_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem0 >= 26
	c_t4_t0_t0_mem0 += MAS_MEM[0]

	c_t4_t0_t0_mem1 = S.Task('c_t4_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t0_mem1 >= 26
	c_t4_t0_t0_mem1 += MAS_MEM[5]

	c_t4_t4_t3 = S.Task('c_t4_t4_t3', length=1, delay_cost=1)
	S += c_t4_t4_t3 >= 26
	c_t4_t4_t3 += MAS[0]

	c_t5_t31_mem0 = S.Task('c_t5_t31_mem0', length=1, delay_cost=1)
	S += c_t5_t31_mem0 >= 26
	c_t5_t31_mem0 += MAS_MEM[2]

	c_t5_t31_mem1 = S.Task('c_t5_t31_mem1', length=1, delay_cost=1)
	S += c_t5_t31_mem1 >= 26
	c_t5_t31_mem1 += MAS_MEM[7]

	c_t5_t4_t2 = S.Task('c_t5_t4_t2', length=1, delay_cost=1)
	S += c_t5_t4_t2 >= 26
	c_t5_t4_t2 += MAS[3]

	c_t0_t4_t1_in = S.Task('c_t0_t4_t1_in', length=1, delay_cost=1)
	S += c_t0_t4_t1_in >= 27
	c_t0_t4_t1_in += MM_in[0]

	c_t0_t4_t1_mem0 = S.Task('c_t0_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem0 >= 27
	c_t0_t4_t1_mem0 += MAS_MEM[0]

	c_t0_t4_t1_mem1 = S.Task('c_t0_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t1_mem1 >= 27
	c_t0_t4_t1_mem1 += MAS_MEM[5]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 27
	c_t1_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 27
	c_t1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_t1_t40 = S.Task('c_t1_t40', length=1, delay_cost=1)
	S += c_t1_t40 >= 27
	c_t1_t40 += MAS[1]

	c_t3_t1_t5_mem0 = S.Task('c_t3_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem0 >= 27
	c_t3_t1_t5_mem0 += MM_MEM[0]

	c_t3_t1_t5_mem1 = S.Task('c_t3_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t5_mem1 >= 27
	c_t3_t1_t5_mem1 += MM_MEM[1]

	c_t4_t0_t0 = S.Task('c_t4_t0_t0', length=4, delay_cost=1)
	S += c_t4_t0_t0 >= 27
	c_t4_t0_t0 += MM[0]

	c_t5_t30_mem0 = S.Task('c_t5_t30_mem0', length=1, delay_cost=1)
	S += c_t5_t30_mem0 >= 27
	c_t5_t30_mem0 += MAS_MEM[2]

	c_t5_t30_mem1 = S.Task('c_t5_t30_mem1', length=1, delay_cost=1)
	S += c_t5_t30_mem1 >= 27
	c_t5_t30_mem1 += MAS_MEM[7]

	c_t5_t31 = S.Task('c_t5_t31', length=1, delay_cost=1)
	S += c_t5_t31 >= 27
	c_t5_t31 += MAS[2]

	c_t0_t11_mem0 = S.Task('c_t0_t11_mem0', length=1, delay_cost=1)
	S += c_t0_t11_mem0 >= 28
	c_t0_t11_mem0 += MM_MEM[0]

	c_t0_t11_mem1 = S.Task('c_t0_t11_mem1', length=1, delay_cost=1)
	S += c_t0_t11_mem1 >= 28
	c_t0_t11_mem1 += MAS_MEM[7]

	c_t0_t4_t1 = S.Task('c_t0_t4_t1', length=4, delay_cost=1)
	S += c_t0_t4_t1 >= 28
	c_t0_t4_t1 += MM[0]

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 28
	c_t1_t30_mem1 += MAIN_MEM_r[1]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 28
	c_t2_t0_t1_mem0 += MAIN_MEM_r[0]

	c_t2_t4_t0_in = S.Task('c_t2_t4_t0_in', length=1, delay_cost=1)
	S += c_t2_t4_t0_in >= 28
	c_t2_t4_t0_in += MM_in[0]

	c_t2_t4_t0_mem0 = S.Task('c_t2_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem0 >= 28
	c_t2_t4_t0_mem0 += MAS_MEM[0]

	c_t2_t4_t0_mem1 = S.Task('c_t2_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t0_mem1 >= 28
	c_t2_t4_t0_mem1 += MAS_MEM[3]

	c_t3_t1_t5 = S.Task('c_t3_t1_t5', length=1, delay_cost=1)
	S += c_t3_t1_t5 >= 28
	c_t3_t1_t5 += MAS[1]

	c_t3_t4_t3_mem0 = S.Task('c_t3_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem0 >= 28
	c_t3_t4_t3_mem0 += MAS_MEM[2]

	c_t3_t4_t3_mem1 = S.Task('c_t3_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t3_mem1 >= 28
	c_t3_t4_t3_mem1 += MAS_MEM[5]

	c_t5_t30 = S.Task('c_t5_t30', length=1, delay_cost=1)
	S += c_t5_t30 >= 28
	c_t5_t30 += MAS[0]

	c_t0_s00_mem0 = S.Task('c_t0_s00_mem0', length=1, delay_cost=1)
	S += c_t0_s00_mem0 >= 29
	c_t0_s00_mem0 += MAS_MEM[6]

	c_t0_s00_mem1 = S.Task('c_t0_s00_mem1', length=1, delay_cost=1)
	S += c_t0_s00_mem1 >= 29
	c_t0_s00_mem1 += MAS_MEM[1]

	c_t0_t11 = S.Task('c_t0_t11', length=1, delay_cost=1)
	S += c_t0_t11 >= 29
	c_t0_t11 += MAS[0]

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 29
	c_t0_t20_mem1 += MAIN_MEM_r[1]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 29
	c_t1_t30_mem0 += MAIN_MEM_r[0]

	c_t2_t4_t0 = S.Task('c_t2_t4_t0', length=4, delay_cost=1)
	S += c_t2_t4_t0 >= 29
	c_t2_t4_t0 += MM[0]

	c_t3_t0_t1_in = S.Task('c_t3_t0_t1_in', length=1, delay_cost=1)
	S += c_t3_t0_t1_in >= 29
	c_t3_t0_t1_in += MM_in[0]

	c_t3_t0_t1_mem0 = S.Task('c_t3_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem0 >= 29
	c_t3_t0_t1_mem0 += MAS_MEM[2]

	c_t3_t0_t1_mem1 = S.Task('c_t3_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t1_mem1 >= 29
	c_t3_t0_t1_mem1 += MAS_MEM[7]

	c_t3_t10_mem0 = S.Task('c_t3_t10_mem0', length=1, delay_cost=1)
	S += c_t3_t10_mem0 >= 29
	c_t3_t10_mem0 += MM_MEM[0]

	c_t3_t10_mem1 = S.Task('c_t3_t10_mem1', length=1, delay_cost=1)
	S += c_t3_t10_mem1 >= 29
	c_t3_t10_mem1 += MM_MEM[1]

	c_t3_t4_t3 = S.Task('c_t3_t4_t3', length=1, delay_cost=1)
	S += c_t3_t4_t3 >= 29
	c_t3_t4_t3 += MAS[2]

	c_t5_t4_t3_mem0 = S.Task('c_t5_t4_t3_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem0 >= 29
	c_t5_t4_t3_mem0 += MAS_MEM[0]

	c_t5_t4_t3_mem1 = S.Task('c_t5_t4_t3_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t3_mem1 >= 29
	c_t5_t4_t3_mem1 += MAS_MEM[5]

	c_t0_s00 = S.Task('c_t0_s00', length=1, delay_cost=1)
	S += c_t0_s00 >= 30
	c_t0_s00 += MAS[0]

	c_t1_t4_t5_mem0 = S.Task('c_t1_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem0 >= 30
	c_t1_t4_t5_mem0 += MM_MEM[0]

	c_t1_t4_t5_mem1 = S.Task('c_t1_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t5_mem1 >= 30
	c_t1_t4_t5_mem1 += MM_MEM[1]

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	S += c_t3110_mem1 >= 30
	c_t3110_mem1 += MAIN_MEM_r[1]

	c_t3_t0_t1 = S.Task('c_t3_t0_t1', length=4, delay_cost=1)
	S += c_t3_t0_t1 >= 30
	c_t3_t0_t1 += MM[0]

	c_t3_t10 = S.Task('c_t3_t10', length=1, delay_cost=1)
	S += c_t3_t10 >= 30
	c_t3_t10 += MAS[2]

	c_t4_t1_t1_in = S.Task('c_t4_t1_t1_in', length=1, delay_cost=1)
	S += c_t4_t1_t1_in >= 30
	c_t4_t1_t1_in += MM_in[0]

	c_t4_t1_t1_mem0 = S.Task('c_t4_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem0 >= 30
	c_t4_t1_t1_mem0 += MAS_MEM[4]

	c_t4_t1_t1_mem1 = S.Task('c_t4_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t1_mem1 >= 30
	c_t4_t1_t1_mem1 += MAS_MEM[7]

	c_t4_t4_t2_mem0 = S.Task('c_t4_t4_t2_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem0 >= 30
	c_t4_t4_t2_mem0 += MAS_MEM[2]

	c_t4_t4_t2_mem1 = S.Task('c_t4_t4_t2_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t2_mem1 >= 30
	c_t4_t4_t2_mem1 += MAS_MEM[1]

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	S += c_t5010_mem0 >= 30
	c_t5010_mem0 += MAIN_MEM_r[0]

	c_t5_t4_t3 = S.Task('c_t5_t4_t3', length=1, delay_cost=1)
	S += c_t5_t4_t3 >= 30
	c_t5_t4_t3 += MAS[1]

	c_t0_t50_mem0 = S.Task('c_t0_t50_mem0', length=1, delay_cost=1)
	S += c_t0_t50_mem0 >= 31
	c_t0_t50_mem0 += MAS_MEM[2]

	c_t0_t50_mem1 = S.Task('c_t0_t50_mem1', length=1, delay_cost=1)
	S += c_t0_t50_mem1 >= 31
	c_t0_t50_mem1 += MAS_MEM[7]

	c_t1_t11_mem0 = S.Task('c_t1_t11_mem0', length=1, delay_cost=1)
	S += c_t1_t11_mem0 >= 31
	c_t1_t11_mem0 += MM_MEM[0]

	c_t1_t11_mem1 = S.Task('c_t1_t11_mem1', length=1, delay_cost=1)
	S += c_t1_t11_mem1 >= 31
	c_t1_t11_mem1 += MAS_MEM[5]

	c_t1_t4_t5 = S.Task('c_t1_t4_t5', length=1, delay_cost=1)
	S += c_t1_t4_t5 >= 31
	c_t1_t4_t5 += MAS[0]

	c_t3_t0_t0_in = S.Task('c_t3_t0_t0_in', length=1, delay_cost=1)
	S += c_t3_t0_t0_in >= 31
	c_t3_t0_t0_in += MM_in[0]

	c_t3_t0_t0_mem0 = S.Task('c_t3_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem0 >= 31
	c_t3_t0_t0_mem0 += MAS_MEM[0]

	c_t3_t0_t0_mem1 = S.Task('c_t3_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t0_mem1 >= 31
	c_t3_t0_t0_mem1 += MAS_MEM[1]

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	S += c_t4101_mem0 >= 31
	c_t4101_mem0 += MAIN_MEM_r[0]

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	S += c_t4101_mem1 >= 31
	c_t4101_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t1 = S.Task('c_t4_t1_t1', length=4, delay_cost=1)
	S += c_t4_t1_t1 >= 31
	c_t4_t1_t1 += MM[0]

	c_t4_t4_t2 = S.Task('c_t4_t4_t2', length=1, delay_cost=1)
	S += c_t4_t4_t2 >= 31
	c_t4_t4_t2 += MAS[1]

	c_t0_t4_t5_mem0 = S.Task('c_t0_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem0 >= 32
	c_t0_t4_t5_mem0 += MM_MEM[0]

	c_t0_t4_t5_mem1 = S.Task('c_t0_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t5_mem1 >= 32
	c_t0_t4_t5_mem1 += MM_MEM[1]

	c_t0_t50 = S.Task('c_t0_t50', length=1, delay_cost=1)
	S += c_t0_t50 >= 32
	c_t0_t50 += MAS[0]

	c_t1_s01_mem0 = S.Task('c_t1_s01_mem0', length=1, delay_cost=1)
	S += c_t1_s01_mem0 >= 32
	c_t1_s01_mem0 += MAS_MEM[6]

	c_t1_s01_mem1 = S.Task('c_t1_s01_mem1', length=1, delay_cost=1)
	S += c_t1_s01_mem1 >= 32
	c_t1_s01_mem1 += MAS_MEM[1]

	c_t1_t11 = S.Task('c_t1_t11', length=1, delay_cost=1)
	S += c_t1_t11 >= 32
	c_t1_t11 += MAS[3]

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem1 >= 32
	c_t2_t1_t3_mem1 += MAIN_MEM_r[1]

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	S += c_t3001_mem0 >= 32
	c_t3001_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t0 = S.Task('c_t3_t0_t0', length=4, delay_cost=1)
	S += c_t3_t0_t0 >= 32
	c_t3_t0_t0 += MM[0]

	c_t5_t1_t1_in = S.Task('c_t5_t1_t1_in', length=1, delay_cost=1)
	S += c_t5_t1_t1_in >= 32
	c_t5_t1_t1_in += MM_in[0]

	c_t5_t1_t1_mem0 = S.Task('c_t5_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem0 >= 32
	c_t5_t1_t1_mem0 += MAS_MEM[2]

	c_t5_t1_t1_mem1 = S.Task('c_t5_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t1_mem1 >= 32
	c_t5_t1_t1_mem1 += MAS_MEM[7]

	c_t000_mem0 = S.Task('c_t000_mem0', length=1, delay_cost=1)
	S += c_t000_mem0 >= 33
	c_t000_mem0 += MAS_MEM[2]

	c_t000_mem1 = S.Task('c_t000_mem1', length=1, delay_cost=1)
	S += c_t000_mem1 >= 33
	c_t000_mem1 += MAS_MEM[1]

	c_t0_t01_mem0 = S.Task('c_t0_t01_mem0', length=1, delay_cost=1)
	S += c_t0_t01_mem0 >= 33
	c_t0_t01_mem0 += MM_MEM[0]

	c_t0_t01_mem1 = S.Task('c_t0_t01_mem1', length=1, delay_cost=1)
	S += c_t0_t01_mem1 >= 33
	c_t0_t01_mem1 += MAS_MEM[7]

	c_t0_t4_t5 = S.Task('c_t0_t4_t5', length=1, delay_cost=1)
	S += c_t0_t4_t5 >= 33
	c_t0_t4_t5 += MAS[1]

	c_t1_s01 = S.Task('c_t1_s01', length=1, delay_cost=1)
	S += c_t1_s01 >= 33
	c_t1_s01 += MAS[3]

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem0 >= 33
	c_t2_t1_t2_mem0 += MAIN_MEM_r[0]

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t2_mem1 >= 33
	c_t2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_t5_t0_t1_in = S.Task('c_t5_t0_t1_in', length=1, delay_cost=1)
	S += c_t5_t0_t1_in >= 33
	c_t5_t0_t1_in += MM_in[0]

	c_t5_t0_t1_mem0 = S.Task('c_t5_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem0 >= 33
	c_t5_t0_t1_mem0 += MAS_MEM[0]

	c_t5_t0_t1_mem1 = S.Task('c_t5_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t1_mem1 >= 33
	c_t5_t0_t1_mem1 += MAS_MEM[3]

	c_t5_t1_t1 = S.Task('c_t5_t1_t1', length=4, delay_cost=1)
	S += c_t5_t1_t1 >= 33
	c_t5_t1_t1 += MM[0]

	c_t000 = S.Task('c_t000', length=1, delay_cost=1)
	S += c_t000 >= 34
	c_t000 += MAS[2]

	c_t0_s01_mem0 = S.Task('c_t0_s01_mem0', length=1, delay_cost=1)
	S += c_t0_s01_mem0 >= 34
	c_t0_s01_mem0 += MAS_MEM[0]

	c_t0_s01_mem1 = S.Task('c_t0_s01_mem1', length=1, delay_cost=1)
	S += c_t0_s01_mem1 >= 34
	c_t0_s01_mem1 += MAS_MEM[7]

	c_t0_t01 = S.Task('c_t0_t01', length=1, delay_cost=1)
	S += c_t0_t01 >= 34
	c_t0_t01 += MAS[1]

	c_t0_t51_mem0 = S.Task('c_t0_t51_mem0', length=1, delay_cost=1)
	S += c_t0_t51_mem0 >= 34
	c_t0_t51_mem0 += MAS_MEM[2]

	c_t0_t51_mem1 = S.Task('c_t0_t51_mem1', length=1, delay_cost=1)
	S += c_t0_t51_mem1 >= 34
	c_t0_t51_mem1 += MAS_MEM[1]

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	S += c_t4100_mem0 >= 34
	c_t4100_mem0 += MAIN_MEM_r[0]

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	S += c_t4100_mem1 >= 34
	c_t4100_mem1 += MAIN_MEM_r[1]

	c_t4_t10_mem0 = S.Task('c_t4_t10_mem0', length=1, delay_cost=1)
	S += c_t4_t10_mem0 >= 34
	c_t4_t10_mem0 += MM_MEM[0]

	c_t4_t10_mem1 = S.Task('c_t4_t10_mem1', length=1, delay_cost=1)
	S += c_t4_t10_mem1 >= 34
	c_t4_t10_mem1 += MM_MEM[1]

	c_t5_t0_t0_in = S.Task('c_t5_t0_t0_in', length=1, delay_cost=1)
	S += c_t5_t0_t0_in >= 34
	c_t5_t0_t0_in += MM_in[0]

	c_t5_t0_t0_mem0 = S.Task('c_t5_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem0 >= 34
	c_t5_t0_t0_mem0 += MAS_MEM[4]

	c_t5_t0_t0_mem1 = S.Task('c_t5_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t0_mem1 >= 34
	c_t5_t0_t0_mem1 += MAS_MEM[3]

	c_t5_t0_t1 = S.Task('c_t5_t0_t1', length=4, delay_cost=1)
	S += c_t5_t0_t1 >= 34
	c_t5_t0_t1 += MM[0]

	c_t0_s01 = S.Task('c_t0_s01', length=1, delay_cost=1)
	S += c_t0_s01 >= 35
	c_t0_s01 += MAS[1]

	c_t0_t51 = S.Task('c_t0_t51', length=1, delay_cost=1)
	S += c_t0_t51 >= 35
	c_t0_t51 += MAS[2]

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	S += c_t3010_mem0 >= 35
	c_t3010_mem0 += MAIN_MEM_r[0]

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	S += c_t3111_mem1 >= 35
	c_t3111_mem1 += MAIN_MEM_r[1]

	c_t3_t00_mem0 = S.Task('c_t3_t00_mem0', length=1, delay_cost=1)
	S += c_t3_t00_mem0 >= 35
	c_t3_t00_mem0 += MM_MEM[0]

	c_t3_t00_mem1 = S.Task('c_t3_t00_mem1', length=1, delay_cost=1)
	S += c_t3_t00_mem1 >= 35
	c_t3_t00_mem1 += MM_MEM[1]

	c_t4_t10 = S.Task('c_t4_t10', length=1, delay_cost=1)
	S += c_t4_t10 >= 35
	c_t4_t10 += MAS[0]

	c_t5_t0_t0 = S.Task('c_t5_t0_t0', length=4, delay_cost=1)
	S += c_t5_t0_t0 >= 35
	c_t5_t0_t0 += MM[0]

	c_t5_t1_t0_in = S.Task('c_t5_t1_t0_in', length=1, delay_cost=1)
	S += c_t5_t1_t0_in >= 35
	c_t5_t1_t0_in += MM_in[0]

	c_t5_t1_t0_mem0 = S.Task('c_t5_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem0 >= 35
	c_t5_t1_t0_mem0 += MAS_MEM[2]

	c_t5_t1_t0_mem1 = S.Task('c_t5_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t0_mem1 >= 35
	c_t5_t1_t0_mem1 += MAS_MEM[7]

	c_t0_t40_mem0 = S.Task('c_t0_t40_mem0', length=1, delay_cost=1)
	S += c_t0_t40_mem0 >= 36
	c_t0_t40_mem0 += MM_MEM[0]

	c_t0_t40_mem1 = S.Task('c_t0_t40_mem1', length=1, delay_cost=1)
	S += c_t0_t40_mem1 >= 36
	c_t0_t40_mem1 += MM_MEM[1]

	c_t1_t51_mem0 = S.Task('c_t1_t51_mem0', length=1, delay_cost=1)
	S += c_t1_t51_mem0 >= 36
	c_t1_t51_mem0 += MAS_MEM[4]

	c_t1_t51_mem1 = S.Task('c_t1_t51_mem1', length=1, delay_cost=1)
	S += c_t1_t51_mem1 >= 36
	c_t1_t51_mem1 += MAS_MEM[7]

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t3_mem0 >= 36
	c_t2_t1_t3_mem0 += MAIN_MEM_r[0]

	c_t3_t00 = S.Task('c_t3_t00', length=1, delay_cost=1)
	S += c_t3_t00 >= 36
	c_t3_t00 += MAS[3]

	c_t3_t50_mem0 = S.Task('c_t3_t50_mem0', length=1, delay_cost=1)
	S += c_t3_t50_mem0 >= 36
	c_t3_t50_mem0 += MAS_MEM[6]

	c_t3_t50_mem1 = S.Task('c_t3_t50_mem1', length=1, delay_cost=1)
	S += c_t3_t50_mem1 >= 36
	c_t3_t50_mem1 += MAS_MEM[5]

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	S += c_t4111_mem1 >= 36
	c_t4111_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t4_in = S.Task('c_t4_t0_t4_in', length=1, delay_cost=1)
	S += c_t4_t0_t4_in >= 36
	c_t4_t0_t4_in += MM_in[0]

	c_t4_t0_t4_mem0 = S.Task('c_t4_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem0 >= 36
	c_t4_t0_t4_mem0 += MAS_MEM[2]

	c_t4_t0_t4_mem1 = S.Task('c_t4_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t4_mem1 >= 36
	c_t4_t0_t4_mem1 += MAS_MEM[1]

	c_t5_t1_t0 = S.Task('c_t5_t1_t0', length=4, delay_cost=1)
	S += c_t5_t1_t0 >= 36
	c_t5_t1_t0 += MM[0]

	c_t0_t40 = S.Task('c_t0_t40', length=1, delay_cost=1)
	S += c_t0_t40 >= 37
	c_t0_t40 += MAS[0]

	c_t1_s00_mem0 = S.Task('c_t1_s00_mem0', length=1, delay_cost=1)
	S += c_t1_s00_mem0 >= 37
	c_t1_s00_mem0 += MAS_MEM[0]

	c_t1_s00_mem1 = S.Task('c_t1_s00_mem1', length=1, delay_cost=1)
	S += c_t1_s00_mem1 >= 37
	c_t1_s00_mem1 += MAS_MEM[7]

	c_t1_t51 = S.Task('c_t1_t51', length=1, delay_cost=1)
	S += c_t1_t51 >= 37
	c_t1_t51 += MAS[1]

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	S += c_t2_t21_mem1 >= 37
	c_t2_t21_mem1 += MAIN_MEM_r[1]

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	S += c_t3011_mem0 >= 37
	c_t3011_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t5_mem0 = S.Task('c_t3_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem0 >= 37
	c_t3_t0_t5_mem0 += MM_MEM[0]

	c_t3_t0_t5_mem1 = S.Task('c_t3_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t5_mem1 >= 37
	c_t3_t0_t5_mem1 += MM_MEM[1]

	c_t3_t1_t4_in = S.Task('c_t3_t1_t4_in', length=1, delay_cost=1)
	S += c_t3_t1_t4_in >= 37
	c_t3_t1_t4_in += MM_in[0]

	c_t3_t1_t4_mem0 = S.Task('c_t3_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem0 >= 37
	c_t3_t1_t4_mem0 += MAS_MEM[2]

	c_t3_t1_t4_mem1 = S.Task('c_t3_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t1_t4_mem1 >= 37
	c_t3_t1_t4_mem1 += MAS_MEM[1]

	c_t3_t50 = S.Task('c_t3_t50', length=1, delay_cost=1)
	S += c_t3_t50 >= 37
	c_t3_t50 += MAS[3]

	c_t4_t0_t4 = S.Task('c_t4_t0_t4', length=4, delay_cost=1)
	S += c_t4_t0_t4 >= 37
	c_t4_t0_t4 += MM[0]

	c_t110_mem0 = S.Task('c_t110_mem0', length=1, delay_cost=1)
	S += c_t110_mem0 >= 38
	c_t110_mem0 += MAS_MEM[2]

	c_t110_mem1 = S.Task('c_t110_mem1', length=1, delay_cost=1)
	S += c_t110_mem1 >= 38
	c_t110_mem1 += MAS_MEM[3]

	c_t1_s00 = S.Task('c_t1_s00', length=1, delay_cost=1)
	S += c_t1_s00 >= 38
	c_t1_s00 += MAS[1]

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	S += c_t3110_mem0 >= 38
	c_t3110_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t5 = S.Task('c_t3_t0_t5', length=1, delay_cost=1)
	S += c_t3_t0_t5 >= 38
	c_t3_t0_t5 += MAS[3]

	c_t3_t1_t4 = S.Task('c_t3_t1_t4', length=4, delay_cost=1)
	S += c_t3_t1_t4 >= 38
	c_t3_t1_t4 += MM[0]

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	S += c_t4110_mem1 >= 38
	c_t4110_mem1 += MAIN_MEM_r[1]

	c_t4_t1_t5_mem0 = S.Task('c_t4_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem0 >= 38
	c_t4_t1_t5_mem0 += MM_MEM[0]

	c_t4_t1_t5_mem1 = S.Task('c_t4_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t5_mem1 >= 38
	c_t4_t1_t5_mem1 += MM_MEM[1]

	c_t5_t4_t0_in = S.Task('c_t5_t4_t0_in', length=1, delay_cost=1)
	S += c_t5_t4_t0_in >= 38
	c_t5_t4_t0_in += MM_in[0]

	c_t5_t4_t0_mem0 = S.Task('c_t5_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem0 >= 38
	c_t5_t4_t0_mem0 += MAS_MEM[4]

	c_t5_t4_t0_mem1 = S.Task('c_t5_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t0_mem1 >= 38
	c_t5_t4_t0_mem1 += MAS_MEM[1]

	c_t010_mem0 = S.Task('c_t010_mem0', length=1, delay_cost=1)
	S += c_t010_mem0 >= 39
	c_t010_mem0 += MAS_MEM[0]

	c_t010_mem1 = S.Task('c_t010_mem1', length=1, delay_cost=1)
	S += c_t010_mem1 >= 39
	c_t010_mem1 += MAS_MEM[1]

	c_t110 = S.Task('c_t110', length=1, delay_cost=1)
	S += c_t110 >= 39
	c_t110 += MAS[0]

	c_t2_t01_mem0 = S.Task('c_t2_t01_mem0', length=1, delay_cost=1)
	S += c_t2_t01_mem0 >= 39
	c_t2_t01_mem0 += MM_MEM[0]

	c_t2_t01_mem1 = S.Task('c_t2_t01_mem1', length=1, delay_cost=1)
	S += c_t2_t01_mem1 >= 39
	c_t2_t01_mem1 += MAS_MEM[7]

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	S += c_t3011_mem1 >= 39
	c_t3011_mem1 += MAIN_MEM_r[1]

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	S += c_t3101_mem0 >= 39
	c_t3101_mem0 += MAIN_MEM_r[0]

	c_t3_t0_t4_in = S.Task('c_t3_t0_t4_in', length=1, delay_cost=1)
	S += c_t3_t0_t4_in >= 39
	c_t3_t0_t4_in += MM_in[0]

	c_t3_t0_t4_mem0 = S.Task('c_t3_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem0 >= 39
	c_t3_t0_t4_mem0 += MAS_MEM[2]

	c_t3_t0_t4_mem1 = S.Task('c_t3_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t0_t4_mem1 >= 39
	c_t3_t0_t4_mem1 += MAS_MEM[3]

	c_t4_t1_t5 = S.Task('c_t4_t1_t5', length=1, delay_cost=1)
	S += c_t4_t1_t5 >= 39
	c_t4_t1_t5 += MAS[1]

	c_t5_t4_t0 = S.Task('c_t5_t4_t0', length=4, delay_cost=1)
	S += c_t5_t4_t0 >= 39
	c_t5_t4_t0 += MM[0]

	c_t010 = S.Task('c_t010', length=1, delay_cost=1)
	S += c_t010 >= 40
	c_t010 += MAS[0]

	c_t101_mem0 = S.Task('c_t101_mem0', length=1, delay_cost=1)
	S += c_t101_mem0 >= 40
	c_t101_mem0 += MAS_MEM[4]

	c_t101_mem1 = S.Task('c_t101_mem1', length=1, delay_cost=1)
	S += c_t101_mem1 >= 40
	c_t101_mem1 += MAS_MEM[7]

	c_t2_t01 = S.Task('c_t2_t01', length=1, delay_cost=1)
	S += c_t2_t01 >= 40
	c_t2_t01 += MAS[3]

	c_t2_t40_mem0 = S.Task('c_t2_t40_mem0', length=1, delay_cost=1)
	S += c_t2_t40_mem0 >= 40
	c_t2_t40_mem0 += MM_MEM[0]

	c_t2_t40_mem1 = S.Task('c_t2_t40_mem1', length=1, delay_cost=1)
	S += c_t2_t40_mem1 >= 40
	c_t2_t40_mem1 += MM_MEM[1]

	c_t2_t51_mem0 = S.Task('c_t2_t51_mem0', length=1, delay_cost=1)
	S += c_t2_t51_mem0 >= 40
	c_t2_t51_mem0 += MAS_MEM[6]

	c_t2_t51_mem1 = S.Task('c_t2_t51_mem1', length=1, delay_cost=1)
	S += c_t2_t51_mem1 >= 40
	c_t2_t51_mem1 += MAS_MEM[3]

	c_t3_t0_t4 = S.Task('c_t3_t0_t4', length=4, delay_cost=1)
	S += c_t3_t0_t4 >= 40
	c_t3_t0_t4 += MM[0]

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	S += c_t4010_mem1 >= 40
	c_t4010_mem1 += MAIN_MEM_r[1]

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	S += c_t4111_mem0 >= 40
	c_t4111_mem0 += MAIN_MEM_r[0]

	c_t5_t4_t1_in = S.Task('c_t5_t4_t1_in', length=1, delay_cost=1)
	S += c_t5_t4_t1_in >= 40
	c_t5_t4_t1_in += MM_in[0]

	c_t5_t4_t1_mem0 = S.Task('c_t5_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem0 >= 40
	c_t5_t4_t1_mem0 += MAS_MEM[0]

	c_t5_t4_t1_mem1 = S.Task('c_t5_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t1_mem1 >= 40
	c_t5_t4_t1_mem1 += MAS_MEM[5]

	c_t101 = S.Task('c_t101', length=1, delay_cost=1)
	S += c_t101 >= 41
	c_t101 += MAS[2]

	c_t210_mem0 = S.Task('c_t210_mem0', length=1, delay_cost=1)
	S += c_t210_mem0 >= 41
	c_t210_mem0 += MAS_MEM[6]

	c_t210_mem1 = S.Task('c_t210_mem1', length=1, delay_cost=1)
	S += c_t210_mem1 >= 41
	c_t210_mem1 += MAS_MEM[5]

	c_t2_t40 = S.Task('c_t2_t40', length=1, delay_cost=1)
	S += c_t2_t40 >= 41
	c_t2_t40 += MAS[3]

	c_t2_t51 = S.Task('c_t2_t51', length=1, delay_cost=1)
	S += c_t2_t51 >= 41
	c_t2_t51 += MAS[0]

	c_t3_t4_t0_in = S.Task('c_t3_t4_t0_in', length=1, delay_cost=1)
	S += c_t3_t4_t0_in >= 41
	c_t3_t4_t0_in += MM_in[0]

	c_t3_t4_t0_mem0 = S.Task('c_t3_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem0 >= 41
	c_t3_t4_t0_mem0 += MAS_MEM[2]

	c_t3_t4_t0_mem1 = S.Task('c_t3_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t0_mem1 >= 41
	c_t3_t4_t0_mem1 += MAS_MEM[3]

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	S += c_t4000_mem1 >= 41
	c_t4000_mem1 += MAIN_MEM_r[1]

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	S += c_t5111_mem0 >= 41
	c_t5111_mem0 += MAIN_MEM_r[0]

	c_t5_t10_mem0 = S.Task('c_t5_t10_mem0', length=1, delay_cost=1)
	S += c_t5_t10_mem0 >= 41
	c_t5_t10_mem0 += MM_MEM[0]

	c_t5_t10_mem1 = S.Task('c_t5_t10_mem1', length=1, delay_cost=1)
	S += c_t5_t10_mem1 >= 41
	c_t5_t10_mem1 += MM_MEM[1]

	c_t5_t4_t1 = S.Task('c_t5_t4_t1', length=4, delay_cost=1)
	S += c_t5_t4_t1 >= 41
	c_t5_t4_t1 += MM[0]

	c_t6010_mem0 = S.Task('c_t6010_mem0', length=1, delay_cost=1)
	S += c_t6010_mem0 >= 41
	c_t6010_mem0 += MAS_MEM[0]

	c_t6010_mem1 = S.Task('c_t6010_mem1', length=1, delay_cost=1)
	S += c_t6010_mem1 >= 41
	c_t6010_mem1 += MAS_MEM[1]

	c_t210 = S.Task('c_t210', length=1, delay_cost=1)
	S += c_t210 >= 42
	c_t210 += MAS[1]

	c_t2_s01_mem0 = S.Task('c_t2_s01_mem0', length=1, delay_cost=1)
	S += c_t2_s01_mem0 >= 42
	c_t2_s01_mem0 += MAS_MEM[2]

	c_t2_s01_mem1 = S.Task('c_t2_s01_mem1', length=1, delay_cost=1)
	S += c_t2_s01_mem1 >= 42
	c_t2_s01_mem1 += MAS_MEM[3]

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	S += c_t3100_mem1 >= 42
	c_t3100_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t0 = S.Task('c_t3_t4_t0', length=4, delay_cost=1)
	S += c_t3_t4_t0 >= 42
	c_t3_t4_t0 += MM[0]

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	S += c_t5011_mem0 >= 42
	c_t5011_mem0 += MAIN_MEM_r[0]

	c_t5_t0_t5_mem0 = S.Task('c_t5_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem0 >= 42
	c_t5_t0_t5_mem0 += MM_MEM[0]

	c_t5_t0_t5_mem1 = S.Task('c_t5_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t5_mem1 >= 42
	c_t5_t0_t5_mem1 += MM_MEM[1]

	c_t5_t10 = S.Task('c_t5_t10', length=1, delay_cost=1)
	S += c_t5_t10 >= 42
	c_t5_t10 += MAS[0]

	c_t5_t1_t4_in = S.Task('c_t5_t1_t4_in', length=1, delay_cost=1)
	S += c_t5_t1_t4_in >= 42
	c_t5_t1_t4_in += MM_in[0]

	c_t5_t1_t4_mem0 = S.Task('c_t5_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem0 >= 42
	c_t5_t1_t4_mem0 += MAS_MEM[0]

	c_t5_t1_t4_mem1 = S.Task('c_t5_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t4_mem1 >= 42
	c_t5_t1_t4_mem1 += MAS_MEM[1]

	c_t6010 = S.Task('c_t6010', length=1, delay_cost=1)
	S += c_t6010 >= 42
	c_t6010 += MAS[3]

	c_t201_mem0 = S.Task('c_t201_mem0', length=1, delay_cost=1)
	S += c_t201_mem0 >= 43
	c_t201_mem0 += MAS_MEM[6]

	c_t201_mem1 = S.Task('c_t201_mem1', length=1, delay_cost=1)
	S += c_t201_mem1 >= 43
	c_t201_mem1 += MAS_MEM[1]

	c_t2_s00_mem0 = S.Task('c_t2_s00_mem0', length=1, delay_cost=1)
	S += c_t2_s00_mem0 >= 43
	c_t2_s00_mem0 += MAS_MEM[2]

	c_t2_s00_mem1 = S.Task('c_t2_s00_mem1', length=1, delay_cost=1)
	S += c_t2_s00_mem1 >= 43
	c_t2_s00_mem1 += MAS_MEM[3]

	c_t2_s01 = S.Task('c_t2_s01', length=1, delay_cost=1)
	S += c_t2_s01 >= 43
	c_t2_s01 += MAS[0]

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	S += c_t3100_mem0 >= 43
	c_t3100_mem0 += MAIN_MEM_r[0]

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	S += c_t3101_mem1 >= 43
	c_t3101_mem1 += MAIN_MEM_r[1]

	c_t3_t4_t1_in = S.Task('c_t3_t4_t1_in', length=1, delay_cost=1)
	S += c_t3_t4_t1_in >= 43
	c_t3_t4_t1_in += MM_in[0]

	c_t3_t4_t1_mem0 = S.Task('c_t3_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem0 >= 43
	c_t3_t4_t1_mem0 += MAS_MEM[0]

	c_t3_t4_t1_mem1 = S.Task('c_t3_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t1_mem1 >= 43
	c_t3_t4_t1_mem1 += MAS_MEM[5]

	c_t5_t00_mem0 = S.Task('c_t5_t00_mem0', length=1, delay_cost=1)
	S += c_t5_t00_mem0 >= 43
	c_t5_t00_mem0 += MM_MEM[0]

	c_t5_t00_mem1 = S.Task('c_t5_t00_mem1', length=1, delay_cost=1)
	S += c_t5_t00_mem1 >= 43
	c_t5_t00_mem1 += MM_MEM[1]

	c_t5_t0_t5 = S.Task('c_t5_t0_t5', length=1, delay_cost=1)
	S += c_t5_t0_t5 >= 43
	c_t5_t0_t5 += MAS[1]

	c_t5_t1_t4 = S.Task('c_t5_t1_t4', length=4, delay_cost=1)
	S += c_t5_t1_t4 >= 43
	c_t5_t1_t4 += MM[0]

	c_t201 = S.Task('c_t201', length=1, delay_cost=1)
	S += c_t201 >= 44
	c_t201 += MAS[2]

	c_t2_s00 = S.Task('c_t2_s00', length=1, delay_cost=1)
	S += c_t2_s00 >= 44
	c_t2_s00 += MAS[0]

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	S += c_t2_t31_mem0 >= 44
	c_t2_t31_mem0 += MAIN_MEM_r[0]

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	S += c_t2_t31_mem1 >= 44
	c_t2_t31_mem1 += MAIN_MEM_r[1]

	c_t2_t4_t4_in = S.Task('c_t2_t4_t4_in', length=1, delay_cost=1)
	S += c_t2_t4_t4_in >= 44
	c_t2_t4_t4_in += MM_in[0]

	c_t2_t4_t4_mem0 = S.Task('c_t2_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem0 >= 44
	c_t2_t4_t4_mem0 += MAS_MEM[6]

	c_t2_t4_t4_mem1 = S.Task('c_t2_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t4_mem1 >= 44
	c_t2_t4_t4_mem1 += MAS_MEM[7]

	c_t2_t4_t5_mem0 = S.Task('c_t2_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem0 >= 44
	c_t2_t4_t5_mem0 += MM_MEM[0]

	c_t2_t4_t5_mem1 = S.Task('c_t2_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t2_t4_t5_mem1 >= 44
	c_t2_t4_t5_mem1 += MM_MEM[1]

	c_t3_t4_t1 = S.Task('c_t3_t4_t1', length=4, delay_cost=1)
	S += c_t3_t4_t1 >= 44
	c_t3_t4_t1 += MM[0]

	c_t5_t00 = S.Task('c_t5_t00', length=1, delay_cost=1)
	S += c_t5_t00 >= 44
	c_t5_t00 += MAS[3]

	c_t7001_mem0 = S.Task('c_t7001_mem0', length=1, delay_cost=1)
	S += c_t7001_mem0 >= 44
	c_t7001_mem0 += MAS_MEM[4]

	c_t7001_mem1 = S.Task('c_t7001_mem1', length=1, delay_cost=1)
	S += c_t7001_mem1 >= 44
	c_t7001_mem1 += MAS_MEM[5]

	c_t7010_mem0 = S.Task('c_t7010_mem0', length=1, delay_cost=1)
	S += c_t7010_mem0 >= 44
	c_t7010_mem0 += MAS_MEM[0]

	c_t7010_mem1 = S.Task('c_t7010_mem1', length=1, delay_cost=1)
	S += c_t7010_mem1 >= 44
	c_t7010_mem1 += MAS_MEM[3]

	c_t8010_mem0 = S.Task('c_t8010_mem0', length=1, delay_cost=1)
	S += c_t8010_mem0 >= 44
	c_t8010_mem0 += MAS_MEM[2]

	c_t8010_mem1 = S.Task('c_t8010_mem1', length=1, delay_cost=1)
	S += c_t8010_mem1 >= 44
	c_t8010_mem1 += MAS_MEM[1]

	c_t001_mem0 = S.Task('c_t001_mem0', length=1, delay_cost=1)
	S += c_t001_mem0 >= 45
	c_t001_mem0 += MAS_MEM[2]

	c_t001_mem1 = S.Task('c_t001_mem1', length=1, delay_cost=1)
	S += c_t001_mem1 >= 45
	c_t001_mem1 += MAS_MEM[3]

	c_t2_t4_t4 = S.Task('c_t2_t4_t4', length=4, delay_cost=1)
	S += c_t2_t4_t4 >= 45
	c_t2_t4_t4 += MM[0]

	c_t2_t4_t5 = S.Task('c_t2_t4_t5', length=1, delay_cost=1)
	S += c_t2_t4_t5 >= 45
	c_t2_t4_t5 += MAS[2]

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	S += c_t4010_mem0 >= 45
	c_t4010_mem0 += MAIN_MEM_r[0]

	c_t4_t0_t5_mem0 = S.Task('c_t4_t0_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem0 >= 45
	c_t4_t0_t5_mem0 += MM_MEM[0]

	c_t4_t0_t5_mem1 = S.Task('c_t4_t0_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t0_t5_mem1 >= 45
	c_t4_t0_t5_mem1 += MM_MEM[1]

	c_t4_t1_t4_in = S.Task('c_t4_t1_t4_in', length=1, delay_cost=1)
	S += c_t4_t1_t4_in >= 45
	c_t4_t1_t4_in += MM_in[0]

	c_t4_t1_t4_mem0 = S.Task('c_t4_t1_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem0 >= 45
	c_t4_t1_t4_mem0 += MAS_MEM[4]

	c_t4_t1_t4_mem1 = S.Task('c_t4_t1_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t1_t4_mem1 >= 45
	c_t4_t1_t4_mem1 += MAS_MEM[5]

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	S += c_t5111_mem1 >= 45
	c_t5111_mem1 += MAIN_MEM_r[1]

	c_t5_t50_mem0 = S.Task('c_t5_t50_mem0', length=1, delay_cost=1)
	S += c_t5_t50_mem0 >= 45
	c_t5_t50_mem0 += MAS_MEM[6]

	c_t5_t50_mem1 = S.Task('c_t5_t50_mem1', length=1, delay_cost=1)
	S += c_t5_t50_mem1 >= 45
	c_t5_t50_mem1 += MAS_MEM[1]

	c_t7001 = S.Task('c_t7001', length=1, delay_cost=1)
	S += c_t7001 >= 45
	c_t7001 += MAS[1]

	c_t7010 = S.Task('c_t7010', length=1, delay_cost=1)
	S += c_t7010 >= 45
	c_t7010 += MAS[3]

	c_t8010 = S.Task('c_t8010', length=1, delay_cost=1)
	S += c_t8010 >= 45
	c_t8010 += MAS[0]

	c_t001 = S.Task('c_t001', length=1, delay_cost=1)
	S += c_t001 >= 46
	c_t001 += MAS[1]

	c_t1_t4_t4_in = S.Task('c_t1_t4_t4_in', length=1, delay_cost=1)
	S += c_t1_t4_t4_in >= 46
	c_t1_t4_t4_in += MM_in[0]

	c_t1_t4_t4_mem0 = S.Task('c_t1_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem0 >= 46
	c_t1_t4_t4_mem0 += MAS_MEM[6]

	c_t1_t4_t4_mem1 = S.Task('c_t1_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t1_t4_t4_mem1 >= 46
	c_t1_t4_t4_mem1 += MAS_MEM[1]

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	S += c_t4001_mem0 >= 46
	c_t4001_mem0 += MAIN_MEM_r[0]

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	S += c_t4001_mem1 >= 46
	c_t4001_mem1 += MAIN_MEM_r[1]

	c_t4_t0_t5 = S.Task('c_t4_t0_t5', length=1, delay_cost=1)
	S += c_t4_t0_t5 >= 46
	c_t4_t0_t5 += MAS[0]

	c_t4_t1_t4 = S.Task('c_t4_t1_t4', length=4, delay_cost=1)
	S += c_t4_t1_t4 >= 46
	c_t4_t1_t4 += MM[0]

	c_t5_t1_t5_mem0 = S.Task('c_t5_t1_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem0 >= 46
	c_t5_t1_t5_mem0 += MM_MEM[0]

	c_t5_t1_t5_mem1 = S.Task('c_t5_t1_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t1_t5_mem1 >= 46
	c_t5_t1_t5_mem1 += MM_MEM[1]

	c_t5_t50 = S.Task('c_t5_t50', length=1, delay_cost=1)
	S += c_t5_t50 >= 46
	c_t5_t50 += MAS[3]

	c_t6001_mem0 = S.Task('c_t6001_mem0', length=1, delay_cost=1)
	S += c_t6001_mem0 >= 46
	c_t6001_mem0 += MAS_MEM[2]

	c_t6001_mem1 = S.Task('c_t6001_mem1', length=1, delay_cost=1)
	S += c_t6001_mem1 >= 46
	c_t6001_mem1 += MAS_MEM[5]

	c_t8001_mem0 = S.Task('c_t8001_mem0', length=1, delay_cost=1)
	S += c_t8001_mem0 >= 46
	c_t8001_mem0 += MAS_MEM[4]

	c_t8001_mem1 = S.Task('c_t8001_mem1', length=1, delay_cost=1)
	S += c_t8001_mem1 >= 46
	c_t8001_mem1 += MAS_MEM[3]

	c_t1_t4_t4 = S.Task('c_t1_t4_t4', length=4, delay_cost=1)
	S += c_t1_t4_t4 >= 47
	c_t1_t4_t4 += MM[0]

	c_t200_mem0 = S.Task('c_t200_mem0', length=1, delay_cost=1)
	S += c_t200_mem0 >= 47
	c_t200_mem0 += MAS_MEM[6]

	c_t200_mem1 = S.Task('c_t200_mem1', length=1, delay_cost=1)
	S += c_t200_mem1 >= 47
	c_t200_mem1 += MAS_MEM[1]

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	S += c_t3001_mem1 >= 47
	c_t3001_mem1 += MAIN_MEM_r[1]

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	S += c_t4000_mem0 >= 47
	c_t4000_mem0 += MAIN_MEM_r[0]

	c_t4_t00_mem0 = S.Task('c_t4_t00_mem0', length=1, delay_cost=1)
	S += c_t4_t00_mem0 >= 47
	c_t4_t00_mem0 += MM_MEM[0]

	c_t4_t00_mem1 = S.Task('c_t4_t00_mem1', length=1, delay_cost=1)
	S += c_t4_t00_mem1 >= 47
	c_t4_t00_mem1 += MM_MEM[1]

	c_t5_t0_t4_in = S.Task('c_t5_t0_t4_in', length=1, delay_cost=1)
	S += c_t5_t0_t4_in >= 47
	c_t5_t0_t4_in += MM_in[0]

	c_t5_t0_t4_mem0 = S.Task('c_t5_t0_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem0 >= 47
	c_t5_t0_t4_mem0 += MAS_MEM[0]

	c_t5_t0_t4_mem1 = S.Task('c_t5_t0_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t0_t4_mem1 >= 47
	c_t5_t0_t4_mem1 += MAS_MEM[5]

	c_t5_t1_t5 = S.Task('c_t5_t1_t5', length=1, delay_cost=1)
	S += c_t5_t1_t5 >= 47
	c_t5_t1_t5 += MAS[3]

	c_t6001 = S.Task('c_t6001', length=1, delay_cost=1)
	S += c_t6001 >= 47
	c_t6001 += MAS[0]

	c_t8001 = S.Task('c_t8001', length=1, delay_cost=1)
	S += c_t8001 >= 47
	c_t8001 += MAS[1]

	c_t100_mem0 = S.Task('c_t100_mem0', length=1, delay_cost=1)
	S += c_t100_mem0 >= 48
	c_t100_mem0 += MAS_MEM[6]

	c_t100_mem1 = S.Task('c_t100_mem1', length=1, delay_cost=1)
	S += c_t100_mem1 >= 48
	c_t100_mem1 += MAS_MEM[3]

	c_t200 = S.Task('c_t200', length=1, delay_cost=1)
	S += c_t200 >= 48
	c_t200 += MAS[0]

	c_t3_t40_mem0 = S.Task('c_t3_t40_mem0', length=1, delay_cost=1)
	S += c_t3_t40_mem0 >= 48
	c_t3_t40_mem0 += MM_MEM[0]

	c_t3_t40_mem1 = S.Task('c_t3_t40_mem1', length=1, delay_cost=1)
	S += c_t3_t40_mem1 >= 48
	c_t3_t40_mem1 += MM_MEM[1]

	c_t4_t00 = S.Task('c_t4_t00', length=1, delay_cost=1)
	S += c_t4_t00 >= 48
	c_t4_t00 += MAS[2]

	c_t4_t4_t0_in = S.Task('c_t4_t4_t0_in', length=1, delay_cost=1)
	S += c_t4_t4_t0_in >= 48
	c_t4_t4_t0_in += MM_in[0]

	c_t4_t4_t0_mem0 = S.Task('c_t4_t4_t0_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem0 >= 48
	c_t4_t4_t0_mem0 += MAS_MEM[2]

	c_t4_t4_t0_mem1 = S.Task('c_t4_t4_t0_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t0_mem1 >= 48
	c_t4_t4_t0_mem1 += MAS_MEM[1]

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	S += c_t5001_mem1 >= 48
	c_t5001_mem1 += MAIN_MEM_r[1]

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	S += c_t5100_mem0 >= 48
	c_t5100_mem0 += MAIN_MEM_r[0]

	c_t5_t0_t4 = S.Task('c_t5_t0_t4', length=4, delay_cost=1)
	S += c_t5_t0_t4 >= 48
	c_t5_t0_t4 += MM[0]

	c_t8000_mem0 = S.Task('c_t8000_mem0', length=1, delay_cost=1)
	S += c_t8000_mem0 >= 48
	c_t8000_mem0 += MAS_MEM[0]

	c_t8000_mem1 = S.Task('c_t8000_mem1', length=1, delay_cost=1)
	S += c_t8000_mem1 >= 48
	c_t8000_mem1 += MAS_MEM[5]

	c_t100 = S.Task('c_t100', length=1, delay_cost=1)
	S += c_t100 >= 49
	c_t100 += MAS[1]

	c_t2_t41_mem0 = S.Task('c_t2_t41_mem0', length=1, delay_cost=1)
	S += c_t2_t41_mem0 >= 49
	c_t2_t41_mem0 += MM_MEM[0]

	c_t2_t41_mem1 = S.Task('c_t2_t41_mem1', length=1, delay_cost=1)
	S += c_t2_t41_mem1 >= 49
	c_t2_t41_mem1 += MAS_MEM[5]

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	S += c_t3000_mem0 >= 49
	c_t3000_mem0 += MAIN_MEM_r[0]

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	S += c_t3000_mem1 >= 49
	c_t3000_mem1 += MAIN_MEM_r[1]

	c_t310_mem0 = S.Task('c_t310_mem0', length=1, delay_cost=1)
	S += c_t310_mem0 >= 49
	c_t310_mem0 += MAS_MEM[6]

	c_t310_mem1 = S.Task('c_t310_mem1', length=1, delay_cost=1)
	S += c_t310_mem1 >= 49
	c_t310_mem1 += MAS_MEM[7]

	c_t3_t40 = S.Task('c_t3_t40', length=1, delay_cost=1)
	S += c_t3_t40 >= 49
	c_t3_t40 += MAS[3]

	c_t4_t4_t0 = S.Task('c_t4_t4_t0', length=4, delay_cost=1)
	S += c_t4_t4_t0 >= 49
	c_t4_t4_t0 += MM[0]

	c_t4_t4_t1_in = S.Task('c_t4_t4_t1_in', length=1, delay_cost=1)
	S += c_t4_t4_t1_in >= 49
	c_t4_t4_t1_in += MM_in[0]

	c_t4_t4_t1_mem0 = S.Task('c_t4_t4_t1_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem0 >= 49
	c_t4_t4_t1_mem0 += MAS_MEM[0]

	c_t4_t4_t1_mem1 = S.Task('c_t4_t4_t1_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t1_mem1 >= 49
	c_t4_t4_t1_mem1 += MAS_MEM[3]

	c_t4_t50_mem0 = S.Task('c_t4_t50_mem0', length=1, delay_cost=1)
	S += c_t4_t50_mem0 >= 49
	c_t4_t50_mem0 += MAS_MEM[4]

	c_t4_t50_mem1 = S.Task('c_t4_t50_mem1', length=1, delay_cost=1)
	S += c_t4_t50_mem1 >= 49
	c_t4_t50_mem1 += MAS_MEM[1]

	c_t8000 = S.Task('c_t8000', length=1, delay_cost=1)
	S += c_t8000 >= 49
	c_t8000 += MAS[0]

	c_t0_t4_t4_in = S.Task('c_t0_t4_t4_in', length=1, delay_cost=1)
	S += c_t0_t4_t4_in >= 50
	c_t0_t4_t4_in += MM_in[0]

	c_t0_t4_t4_mem0 = S.Task('c_t0_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem0 >= 50
	c_t0_t4_t4_mem0 += MAS_MEM[6]

	c_t0_t4_t4_mem1 = S.Task('c_t0_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t0_t4_t4_mem1 >= 50
	c_t0_t4_t4_mem1 += MAS_MEM[5]

	c_t211_mem0 = S.Task('c_t211_mem0', length=1, delay_cost=1)
	S += c_t211_mem0 >= 50
	c_t211_mem0 += MAS_MEM[0]

	c_t211_mem1 = S.Task('c_t211_mem1', length=1, delay_cost=1)
	S += c_t211_mem1 >= 50
	c_t211_mem1 += MAS_MEM[1]

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	S += c_t2_t20_mem0 >= 50
	c_t2_t20_mem0 += MAIN_MEM_r[0]

	c_t2_t41 = S.Task('c_t2_t41', length=1, delay_cost=1)
	S += c_t2_t41 >= 50
	c_t2_t41 += MAS[0]

	c_t310 = S.Task('c_t310', length=1, delay_cost=1)
	S += c_t310 >= 50
	c_t310 += MAS[2]

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	S += c_t4011_mem1 >= 50
	c_t4011_mem1 += MAIN_MEM_r[1]

	c_t4_t4_t1 = S.Task('c_t4_t4_t1', length=4, delay_cost=1)
	S += c_t4_t4_t1 >= 50
	c_t4_t4_t1 += MM[0]

	c_t4_t50 = S.Task('c_t4_t50', length=1, delay_cost=1)
	S += c_t4_t50 >= 50
	c_t4_t50 += MAS[1]

	c_t5_t11_mem0 = S.Task('c_t5_t11_mem0', length=1, delay_cost=1)
	S += c_t5_t11_mem0 >= 50
	c_t5_t11_mem0 += MM_MEM[0]

	c_t5_t11_mem1 = S.Task('c_t5_t11_mem1', length=1, delay_cost=1)
	S += c_t5_t11_mem1 >= 50
	c_t5_t11_mem1 += MAS_MEM[7]

	c_t6000_mem0 = S.Task('c_t6000_mem0', length=1, delay_cost=1)
	S += c_t6000_mem0 >= 50
	c_t6000_mem0 += MAS_MEM[4]

	c_t6000_mem1 = S.Task('c_t6000_mem1', length=1, delay_cost=1)
	S += c_t6000_mem1 >= 50
	c_t6000_mem1 += MAS_MEM[3]

	c_t0_t4_t4 = S.Task('c_t0_t4_t4', length=4, delay_cost=1)
	S += c_t0_t4_t4 >= 51
	c_t0_t4_t4 += MM[0]

	c_t1_t41_mem0 = S.Task('c_t1_t41_mem0', length=1, delay_cost=1)
	S += c_t1_t41_mem0 >= 51
	c_t1_t41_mem0 += MM_MEM[0]

	c_t1_t41_mem1 = S.Task('c_t1_t41_mem1', length=1, delay_cost=1)
	S += c_t1_t41_mem1 >= 51
	c_t1_t41_mem1 += MAS_MEM[1]

	c_t211 = S.Task('c_t211', length=1, delay_cost=1)
	S += c_t211 >= 51
	c_t211 += MAS[3]

	c_t3_t4_t4_in = S.Task('c_t3_t4_t4_in', length=1, delay_cost=1)
	S += c_t3_t4_t4_in >= 51
	c_t3_t4_t4_in += MM_in[0]

	c_t3_t4_t4_mem0 = S.Task('c_t3_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem0 >= 51
	c_t3_t4_t4_mem0 += MAS_MEM[0]

	c_t3_t4_t4_mem1 = S.Task('c_t3_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t4_mem1 >= 51
	c_t3_t4_t4_mem1 += MAS_MEM[5]

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	S += c_t5110_mem0 >= 51
	c_t5110_mem0 += MAIN_MEM_r[0]

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	S += c_t5110_mem1 >= 51
	c_t5110_mem1 += MAIN_MEM_r[1]

	c_t5_t11 = S.Task('c_t5_t11', length=1, delay_cost=1)
	S += c_t5_t11 >= 51
	c_t5_t11 += MAS[2]

	c_t6000 = S.Task('c_t6000', length=1, delay_cost=1)
	S += c_t6000 >= 51
	c_t6000 += MAS[1]

	c_t610_mem0 = S.Task('c_t610_mem0', length=1, delay_cost=1)
	S += c_t610_mem0 >= 51
	c_t610_mem0 += MAS_MEM[4]

	c_t610_mem1 = S.Task('c_t610_mem1', length=1, delay_cost=1)
	S += c_t610_mem1 >= 51
	c_t610_mem1 += MAS_MEM[7]

	c_t9_y1_1_mem0 = S.Task('c_t9_y1_1_mem0', length=1, delay_cost=1)
	S += c_t9_y1_1_mem0 >= 51
	c_t9_y1_1_mem0 += MAS_MEM[6]

	c_t9_y1_1_mem1 = S.Task('c_t9_y1_1_mem1', length=1, delay_cost=1)
	S += c_t9_y1_1_mem1 >= 51
	c_t9_y1_1_mem1 += MAS_MEM[3]

	c_t1_t41 = S.Task('c_t1_t41', length=1, delay_cost=1)
	S += c_t1_t41 >= 52
	c_t1_t41 += MAS[0]

	c_t3_t4_t4 = S.Task('c_t3_t4_t4', length=4, delay_cost=1)
	S += c_t3_t4_t4 >= 52
	c_t3_t4_t4 += MM[0]

	c_t4_t01_mem0 = S.Task('c_t4_t01_mem0', length=1, delay_cost=1)
	S += c_t4_t01_mem0 >= 52
	c_t4_t01_mem0 += MM_MEM[0]

	c_t4_t01_mem1 = S.Task('c_t4_t01_mem1', length=1, delay_cost=1)
	S += c_t4_t01_mem1 >= 52
	c_t4_t01_mem1 += MAS_MEM[1]

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	S += c_t5101_mem0 >= 52
	c_t5101_mem0 += MAIN_MEM_r[0]

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	S += c_t5101_mem1 >= 52
	c_t5101_mem1 += MAIN_MEM_r[1]

	c_t5_s00_mem0 = S.Task('c_t5_s00_mem0', length=1, delay_cost=1)
	S += c_t5_s00_mem0 >= 52
	c_t5_s00_mem0 += MAS_MEM[0]

	c_t5_s00_mem1 = S.Task('c_t5_s00_mem1', length=1, delay_cost=1)
	S += c_t5_s00_mem1 >= 52
	c_t5_s00_mem1 += MAS_MEM[5]

	c_t5_t4_t4_in = S.Task('c_t5_t4_t4_in', length=1, delay_cost=1)
	S += c_t5_t4_t4_in >= 52
	c_t5_t4_t4_in += MM_in[0]

	c_t5_t4_t4_mem0 = S.Task('c_t5_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem0 >= 52
	c_t5_t4_t4_mem0 += MAS_MEM[6]

	c_t5_t4_t4_mem1 = S.Task('c_t5_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t4_mem1 >= 52
	c_t5_t4_t4_mem1 += MAS_MEM[3]

	c_t610 = S.Task('c_t610', length=1, delay_cost=1)
	S += c_t610 >= 52
	c_t610 += MAS[1]

	c_t9_y1_0_mem0 = S.Task('c_t9_y1_0_mem0', length=1, delay_cost=1)
	S += c_t9_y1_0_mem0 >= 52
	c_t9_y1_0_mem0 += MAS_MEM[2]

	c_t9_y1_0_mem1 = S.Task('c_t9_y1_0_mem1', length=1, delay_cost=1)
	S += c_t9_y1_0_mem1 >= 52
	c_t9_y1_0_mem1 += MAS_MEM[7]

	c_t9_y1_1 = S.Task('c_t9_y1_1', length=1, delay_cost=1)
	S += c_t9_y1_1 >= 52
	c_t9_y1_1 += MAS[3]

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	S += c_t4011_mem0 >= 53
	c_t4011_mem0 += MAIN_MEM_r[0]

	c_t4_t01 = S.Task('c_t4_t01', length=1, delay_cost=1)
	S += c_t4_t01 >= 53
	c_t4_t01 += MAS[1]

	c_t4_t11_mem0 = S.Task('c_t4_t11_mem0', length=1, delay_cost=1)
	S += c_t4_t11_mem0 >= 53
	c_t4_t11_mem0 += MM_MEM[0]

	c_t4_t11_mem1 = S.Task('c_t4_t11_mem1', length=1, delay_cost=1)
	S += c_t4_t11_mem1 >= 53
	c_t4_t11_mem1 += MAS_MEM[3]

	c_t4_t4_t4_in = S.Task('c_t4_t4_t4_in', length=1, delay_cost=1)
	S += c_t4_t4_t4_in >= 53
	c_t4_t4_t4_in += MM_in[0]

	c_t4_t4_t4_mem0 = S.Task('c_t4_t4_t4_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem0 >= 53
	c_t4_t4_t4_mem0 += MAS_MEM[2]

	c_t4_t4_t4_mem1 = S.Task('c_t4_t4_t4_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t4_mem1 >= 53
	c_t4_t4_t4_mem1 += MAS_MEM[1]

	c_t500_mem0 = S.Task('c_t500_mem0', length=1, delay_cost=1)
	S += c_t500_mem0 >= 53
	c_t500_mem0 += MAS_MEM[6]

	c_t500_mem1 = S.Task('c_t500_mem1', length=1, delay_cost=1)
	S += c_t500_mem1 >= 53
	c_t500_mem1 += MAS_MEM[7]

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	S += c_t5010_mem1 >= 53
	c_t5010_mem1 += MAIN_MEM_r[1]

	c_t5_s00 = S.Task('c_t5_s00', length=1, delay_cost=1)
	S += c_t5_s00 >= 53
	c_t5_s00 += MAS[3]

	c_t5_t4_t4 = S.Task('c_t5_t4_t4', length=4, delay_cost=1)
	S += c_t5_t4_t4 >= 53
	c_t5_t4_t4 += MM[0]

	c_t9_y1_0 = S.Task('c_t9_y1_0', length=1, delay_cost=1)
	S += c_t9_y1_0 >= 53
	c_t9_y1_0 += MAS[2]

	c_t111_mem0 = S.Task('c_t111_mem0', length=1, delay_cost=1)
	S += c_t111_mem0 >= 54
	c_t111_mem0 += MAS_MEM[0]

	c_t111_mem1 = S.Task('c_t111_mem1', length=1, delay_cost=1)
	S += c_t111_mem1 >= 54
	c_t111_mem1 += MAS_MEM[3]

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	S += c_t2_t30_mem0 >= 54
	c_t2_t30_mem0 += MAIN_MEM_r[0]

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	S += c_t3010_mem1 >= 54
	c_t3010_mem1 += MAIN_MEM_r[1]

	c_t4_s01_mem0 = S.Task('c_t4_s01_mem0', length=1, delay_cost=1)
	S += c_t4_s01_mem0 >= 54
	c_t4_s01_mem0 += MAS_MEM[2]

	c_t4_s01_mem1 = S.Task('c_t4_s01_mem1', length=1, delay_cost=1)
	S += c_t4_s01_mem1 >= 54
	c_t4_s01_mem1 += MAS_MEM[1]

	c_t4_t11 = S.Task('c_t4_t11', length=1, delay_cost=1)
	S += c_t4_t11 >= 54
	c_t4_t11 += MAS[1]

	c_t4_t4_t4 = S.Task('c_t4_t4_t4', length=4, delay_cost=1)
	S += c_t4_t4_t4 >= 54
	c_t4_t4_t4 += MM[0]

	c_t4_t4_t5_mem0 = S.Task('c_t4_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem0 >= 54
	c_t4_t4_t5_mem0 += MM_MEM[0]

	c_t4_t4_t5_mem1 = S.Task('c_t4_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t4_t4_t5_mem1 >= 54
	c_t4_t4_t5_mem1 += MM_MEM[1]

	c_t500 = S.Task('c_t500', length=1, delay_cost=1)
	S += c_t500 >= 54
	c_t500 += MAS[0]

	c_t0_t41_mem0 = S.Task('c_t0_t41_mem0', length=1, delay_cost=1)
	S += c_t0_t41_mem0 >= 55
	c_t0_t41_mem0 += MM_MEM[0]

	c_t0_t41_mem1 = S.Task('c_t0_t41_mem1', length=1, delay_cost=1)
	S += c_t0_t41_mem1 >= 55
	c_t0_t41_mem1 += MAS_MEM[3]

	c_t111 = S.Task('c_t111', length=1, delay_cost=1)
	S += c_t111 >= 55
	c_t111 += MAS[0]

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	S += c_t3111_mem0 >= 55
	c_t3111_mem0 += MAIN_MEM_r[0]

	c_t401_mem0 = S.Task('c_t401_mem0', length=1, delay_cost=1)
	S += c_t401_mem0 >= 55
	c_t401_mem0 += MAS_MEM[2]

	c_t401_mem1 = S.Task('c_t401_mem1', length=1, delay_cost=1)
	S += c_t401_mem1 >= 55
	c_t401_mem1 += MAS_MEM[5]

	c_t4_s01 = S.Task('c_t4_s01', length=1, delay_cost=1)
	S += c_t4_s01 >= 55
	c_t4_s01 += MAS[2]

	c_t4_t4_t5 = S.Task('c_t4_t4_t5', length=1, delay_cost=1)
	S += c_t4_t4_t5 >= 55
	c_t4_t4_t5 += MAS[1]

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	S += c_t5011_mem1 >= 55
	c_t5011_mem1 += MAIN_MEM_r[1]

	c_t5_s01_mem0 = S.Task('c_t5_s01_mem0', length=1, delay_cost=1)
	S += c_t5_s01_mem0 >= 55
	c_t5_s01_mem0 += MAS_MEM[4]

	c_t5_s01_mem1 = S.Task('c_t5_s01_mem1', length=1, delay_cost=1)
	S += c_t5_s01_mem1 >= 55
	c_t5_s01_mem1 += MAS_MEM[1]

	c_t7011_mem0 = S.Task('c_t7011_mem0', length=1, delay_cost=1)
	S += c_t7011_mem0 >= 55
	c_t7011_mem0 += MAS_MEM[0]

	c_t7011_mem1 = S.Task('c_t7011_mem1', length=1, delay_cost=1)
	S += c_t7011_mem1 >= 55
	c_t7011_mem1 += MAS_MEM[7]

	c_t011_mem0 = S.Task('c_t011_mem0', length=1, delay_cost=1)
	S += c_t011_mem0 >= 56
	c_t011_mem0 += MAS_MEM[6]

	c_t011_mem1 = S.Task('c_t011_mem1', length=1, delay_cost=1)
	S += c_t011_mem1 >= 56
	c_t011_mem1 += MAS_MEM[5]

	c_t0_t41 = S.Task('c_t0_t41', length=1, delay_cost=1)
	S += c_t0_t41 >= 56
	c_t0_t41 += MAS[3]

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	S += c_t2_t30_mem1 >= 56
	c_t2_t30_mem1 += MAIN_MEM_r[1]

	c_t401 = S.Task('c_t401', length=1, delay_cost=1)
	S += c_t401 >= 56
	c_t401 += MAS[2]

	c_t4_s00_mem0 = S.Task('c_t4_s00_mem0', length=1, delay_cost=1)
	S += c_t4_s00_mem0 >= 56
	c_t4_s00_mem0 += MAS_MEM[0]

	c_t4_s00_mem1 = S.Task('c_t4_s00_mem1', length=1, delay_cost=1)
	S += c_t4_s00_mem1 >= 56
	c_t4_s00_mem1 += MAS_MEM[3]

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	S += c_t5000_mem0 >= 56
	c_t5000_mem0 += MAIN_MEM_r[0]

	c_t5_s01 = S.Task('c_t5_s01', length=1, delay_cost=1)
	S += c_t5_s01 >= 56
	c_t5_s01 += MAS[0]

	c_t5_t40_mem0 = S.Task('c_t5_t40_mem0', length=1, delay_cost=1)
	S += c_t5_t40_mem0 >= 56
	c_t5_t40_mem0 += MM_MEM[0]

	c_t5_t40_mem1 = S.Task('c_t5_t40_mem1', length=1, delay_cost=1)
	S += c_t5_t40_mem1 >= 56
	c_t5_t40_mem1 += MM_MEM[1]

	c_t7000_mem0 = S.Task('c_t7000_mem0', length=1, delay_cost=1)
	S += c_t7000_mem0 >= 56
	c_t7000_mem0 += MAS_MEM[2]

	c_t7000_mem1 = S.Task('c_t7000_mem1', length=1, delay_cost=1)
	S += c_t7000_mem1 >= 56
	c_t7000_mem1 += MAS_MEM[1]

	c_t7011 = S.Task('c_t7011', length=1, delay_cost=1)
	S += c_t7011 >= 56
	c_t7011 += MAS[1]

	c_t011 = S.Task('c_t011', length=1, delay_cost=1)
	S += c_t011 >= 57
	c_t011 += MAS[0]

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	S += c_t2_t20_mem1 >= 57
	c_t2_t20_mem1 += MAIN_MEM_r[1]

	c_t3_t01_mem0 = S.Task('c_t3_t01_mem0', length=1, delay_cost=1)
	S += c_t3_t01_mem0 >= 57
	c_t3_t01_mem0 += MM_MEM[0]

	c_t3_t01_mem1 = S.Task('c_t3_t01_mem1', length=1, delay_cost=1)
	S += c_t3_t01_mem1 >= 57
	c_t3_t01_mem1 += MAS_MEM[7]

	c_t400_mem0 = S.Task('c_t400_mem0', length=1, delay_cost=1)
	S += c_t400_mem0 >= 57
	c_t400_mem0 += MAS_MEM[4]

	c_t400_mem1 = S.Task('c_t400_mem1', length=1, delay_cost=1)
	S += c_t400_mem1 >= 57
	c_t400_mem1 += MAS_MEM[5]

	c_t4_s00 = S.Task('c_t4_s00', length=1, delay_cost=1)
	S += c_t4_s00 >= 57
	c_t4_s00 += MAS[2]

	c_t4_t51_mem0 = S.Task('c_t4_t51_mem0', length=1, delay_cost=1)
	S += c_t4_t51_mem0 >= 57
	c_t4_t51_mem0 += MAS_MEM[2]

	c_t4_t51_mem1 = S.Task('c_t4_t51_mem1', length=1, delay_cost=1)
	S += c_t4_t51_mem1 >= 57
	c_t4_t51_mem1 += MAS_MEM[3]

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	S += c_t5001_mem0 >= 57
	c_t5001_mem0 += MAIN_MEM_r[0]

	c_t5_t40 = S.Task('c_t5_t40', length=1, delay_cost=1)
	S += c_t5_t40 >= 57
	c_t5_t40 += MAS[3]

	c_t7000 = S.Task('c_t7000', length=1, delay_cost=1)
	S += c_t7000 >= 57
	c_t7000 += MAS[1]

	c_t8011_mem0 = S.Task('c_t8011_mem0', length=1, delay_cost=1)
	S += c_t8011_mem0 >= 57
	c_t8011_mem0 += MAS_MEM[6]

	c_t8011_mem1 = S.Task('c_t8011_mem1', length=1, delay_cost=1)
	S += c_t8011_mem1 >= 57
	c_t8011_mem1 += MAS_MEM[1]

	c_t3_t01 = S.Task('c_t3_t01', length=1, delay_cost=1)
	S += c_t3_t01 >= 58
	c_t3_t01 += MAS[0]

	c_t400 = S.Task('c_t400', length=1, delay_cost=1)
	S += c_t400 >= 58
	c_t400 += MAS[2]

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	S += c_t4110_mem0 >= 58
	c_t4110_mem0 += MAIN_MEM_r[0]

	c_t4_t51 = S.Task('c_t4_t51', length=1, delay_cost=1)
	S += c_t4_t51 >= 58
	c_t4_t51 += MAS[3]

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	S += c_t5100_mem1 >= 58
	c_t5100_mem1 += MAIN_MEM_r[1]

	c_t510_mem0 = S.Task('c_t510_mem0', length=1, delay_cost=1)
	S += c_t510_mem0 >= 58
	c_t510_mem0 += MAS_MEM[6]

	c_t510_mem1 = S.Task('c_t510_mem1', length=1, delay_cost=1)
	S += c_t510_mem1 >= 58
	c_t510_mem1 += MAS_MEM[7]

	c_t5_t01_mem0 = S.Task('c_t5_t01_mem0', length=1, delay_cost=1)
	S += c_t5_t01_mem0 >= 58
	c_t5_t01_mem0 += MM_MEM[0]

	c_t5_t01_mem1 = S.Task('c_t5_t01_mem1', length=1, delay_cost=1)
	S += c_t5_t01_mem1 >= 58
	c_t5_t01_mem1 += MAS_MEM[3]

	c_t6011_mem0 = S.Task('c_t6011_mem0', length=1, delay_cost=1)
	S += c_t6011_mem0 >= 58
	c_t6011_mem0 += MAS_MEM[0]

	c_t6011_mem1 = S.Task('c_t6011_mem1', length=1, delay_cost=1)
	S += c_t6011_mem1 >= 58
	c_t6011_mem1 += MAS_MEM[1]

	c_t8011 = S.Task('c_t8011', length=1, delay_cost=1)
	S += c_t8011 >= 58
	c_t8011 += MAS[1]

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	S += c_t2_t21_mem0 >= 59
	c_t2_t21_mem0 += MAIN_MEM_r[0]

	c_t3_t4_t5_mem0 = S.Task('c_t3_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem0 >= 59
	c_t3_t4_t5_mem0 += MM_MEM[0]

	c_t3_t4_t5_mem1 = S.Task('c_t3_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t3_t4_t5_mem1 >= 59
	c_t3_t4_t5_mem1 += MM_MEM[1]

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	S += c_t5000_mem1 >= 59
	c_t5000_mem1 += MAIN_MEM_r[1]

	c_t510 = S.Task('c_t510', length=1, delay_cost=1)
	S += c_t510 >= 59
	c_t510 += MAS[3]

	c_t5_t01 = S.Task('c_t5_t01', length=1, delay_cost=1)
	S += c_t5_t01 >= 59
	c_t5_t01 += MAS[0]

	c_t5_t51_mem0 = S.Task('c_t5_t51_mem0', length=1, delay_cost=1)
	S += c_t5_t51_mem0 >= 59
	c_t5_t51_mem0 += MAS_MEM[0]

	c_t5_t51_mem1 = S.Task('c_t5_t51_mem1', length=1, delay_cost=1)
	S += c_t5_t51_mem1 >= 59
	c_t5_t51_mem1 += MAS_MEM[5]

	c_t6011 = S.Task('c_t6011', length=1, delay_cost=1)
	S += c_t6011 >= 59
	c_t6011 += MAS[2]

	c_t810_mem0 = S.Task('c_t810_mem0', length=1, delay_cost=1)
	S += c_t810_mem0 >= 59
	c_t810_mem0 += MAS_MEM[6]

	c_t810_mem1 = S.Task('c_t810_mem1', length=1, delay_cost=1)
	S += c_t810_mem1 >= 59
	c_t810_mem1 += MAS_MEM[1]

	c_t3_t11_mem0 = S.Task('c_t3_t11_mem0', length=1, delay_cost=1)
	S += c_t3_t11_mem0 >= 60
	c_t3_t11_mem0 += MM_MEM[0]

	c_t3_t11_mem1 = S.Task('c_t3_t11_mem1', length=1, delay_cost=1)
	S += c_t3_t11_mem1 >= 60
	c_t3_t11_mem1 += MAS_MEM[3]

	c_t3_t4_t5 = S.Task('c_t3_t4_t5', length=1, delay_cost=1)
	S += c_t3_t4_t5 >= 60
	c_t3_t4_t5 += MAS[1]

	c_t501_mem0 = S.Task('c_t501_mem0', length=1, delay_cost=1)
	S += c_t501_mem0 >= 60
	c_t501_mem0 += MAS_MEM[0]

	c_t501_mem1 = S.Task('c_t501_mem1', length=1, delay_cost=1)
	S += c_t501_mem1 >= 60
	c_t501_mem1 += MAS_MEM[1]

	c_t5_t51 = S.Task('c_t5_t51', length=1, delay_cost=1)
	S += c_t5_t51 >= 60
	c_t5_t51 += MAS[0]

	c_t810 = S.Task('c_t810', length=1, delay_cost=1)
	S += c_t810 >= 60
	c_t810 += MAS[2]

	c_t3_s00_mem0 = S.Task('c_t3_s00_mem0', length=1, delay_cost=1)
	S += c_t3_s00_mem0 >= 61
	c_t3_s00_mem0 += MAS_MEM[4]

	c_t3_s00_mem1 = S.Task('c_t3_s00_mem1', length=1, delay_cost=1)
	S += c_t3_s00_mem1 >= 61
	c_t3_s00_mem1 += MAS_MEM[1]

	c_t3_s01_mem0 = S.Task('c_t3_s01_mem0', length=1, delay_cost=1)
	S += c_t3_s01_mem0 >= 61
	c_t3_s01_mem0 += MAS_MEM[0]

	c_t3_s01_mem1 = S.Task('c_t3_s01_mem1', length=1, delay_cost=1)
	S += c_t3_s01_mem1 >= 61
	c_t3_s01_mem1 += MAS_MEM[5]

	c_t3_t11 = S.Task('c_t3_t11', length=1, delay_cost=1)
	S += c_t3_t11 >= 61
	c_t3_t11 += MAS[0]

	c_t4_t40_mem0 = S.Task('c_t4_t40_mem0', length=1, delay_cost=1)
	S += c_t4_t40_mem0 >= 61
	c_t4_t40_mem0 += MM_MEM[0]

	c_t4_t40_mem1 = S.Task('c_t4_t40_mem1', length=1, delay_cost=1)
	S += c_t4_t40_mem1 >= 61
	c_t4_t40_mem1 += MM_MEM[1]

	c_t501 = S.Task('c_t501', length=1, delay_cost=1)
	S += c_t501 >= 61
	c_t501 += MAS[1]

	c_t300_mem0 = S.Task('c_t300_mem0', length=1, delay_cost=1)
	S += c_t300_mem0 >= 62
	c_t300_mem0 += MAS_MEM[6]

	c_t300_mem1 = S.Task('c_t300_mem1', length=1, delay_cost=1)
	S += c_t300_mem1 >= 62
	c_t300_mem1 += MAS_MEM[5]

	c_t3_s00 = S.Task('c_t3_s00', length=1, delay_cost=1)
	S += c_t3_s00 >= 62
	c_t3_s00 += MAS[2]

	c_t3_s01 = S.Task('c_t3_s01', length=1, delay_cost=1)
	S += c_t3_s01 >= 62
	c_t3_s01 += MAS[1]

	c_t410_mem0 = S.Task('c_t410_mem0', length=1, delay_cost=1)
	S += c_t410_mem0 >= 62
	c_t410_mem0 += MAS_MEM[0]

	c_t410_mem1 = S.Task('c_t410_mem1', length=1, delay_cost=1)
	S += c_t410_mem1 >= 62
	c_t410_mem1 += MAS_MEM[3]

	c_t4_t40 = S.Task('c_t4_t40', length=1, delay_cost=1)
	S += c_t4_t40 >= 62
	c_t4_t40 += MAS[0]

	c_t5_t4_t5_mem0 = S.Task('c_t5_t4_t5_mem0', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem0 >= 62
	c_t5_t4_t5_mem0 += MM_MEM[0]

	c_t5_t4_t5_mem1 = S.Task('c_t5_t4_t5_mem1', length=1, delay_cost=1)
	S += c_t5_t4_t5_mem1 >= 62
	c_t5_t4_t5_mem1 += MM_MEM[1]

	c_t300 = S.Task('c_t300', length=1, delay_cost=1)
	S += c_t300 >= 63
	c_t300 += MAS[1]

	c_t3_t51_mem0 = S.Task('c_t3_t51_mem0', length=1, delay_cost=1)
	S += c_t3_t51_mem0 >= 63
	c_t3_t51_mem0 += MAS_MEM[0]

	c_t3_t51_mem1 = S.Task('c_t3_t51_mem1', length=1, delay_cost=1)
	S += c_t3_t51_mem1 >= 63
	c_t3_t51_mem1 += MAS_MEM[1]

	c_t410 = S.Task('c_t410', length=1, delay_cost=1)
	S += c_t410 >= 63
	c_t410 += MAS[3]

	c_t4_t41_mem0 = S.Task('c_t4_t41_mem0', length=1, delay_cost=1)
	S += c_t4_t41_mem0 >= 63
	c_t4_t41_mem0 += MM_MEM[0]

	c_t4_t41_mem1 = S.Task('c_t4_t41_mem1', length=1, delay_cost=1)
	S += c_t4_t41_mem1 >= 63
	c_t4_t41_mem1 += MAS_MEM[3]

	c_t5_t4_t5 = S.Task('c_t5_t4_t5', length=1, delay_cost=1)
	S += c_t5_t4_t5 >= 63
	c_t5_t4_t5 += MAS[0]

	c_t7110_mem0 = S.Task('c_t7110_mem0', length=1, delay_cost=1)
	S += c_t7110_mem0 >= 63
	c_t7110_mem0 += MAS_MEM[6]

	c_t7110_mem1 = S.Task('c_t7110_mem1', length=1, delay_cost=1)
	S += c_t7110_mem1 >= 63
	c_t7110_mem1 += MAS_MEM[7]

	c_t301_mem0 = S.Task('c_t301_mem0', length=1, delay_cost=1)
	S += c_t301_mem0 >= 64
	c_t301_mem0 += MAS_MEM[0]

	c_t301_mem1 = S.Task('c_t301_mem1', length=1, delay_cost=1)
	S += c_t301_mem1 >= 64
	c_t301_mem1 += MAS_MEM[3]

	c_t3_t51 = S.Task('c_t3_t51', length=1, delay_cost=1)
	S += c_t3_t51 >= 64
	c_t3_t51 += MAS[3]

	c_t411_mem0 = S.Task('c_t411_mem0', length=1, delay_cost=1)
	S += c_t411_mem0 >= 64
	c_t411_mem0 += MAS_MEM[4]

	c_t411_mem1 = S.Task('c_t411_mem1', length=1, delay_cost=1)
	S += c_t411_mem1 >= 64
	c_t411_mem1 += MAS_MEM[7]

	c_t4_t41 = S.Task('c_t4_t41', length=1, delay_cost=1)
	S += c_t4_t41 >= 64
	c_t4_t41 += MAS[2]

	c_t5_t41_mem0 = S.Task('c_t5_t41_mem0', length=1, delay_cost=1)
	S += c_t5_t41_mem0 >= 64
	c_t5_t41_mem0 += MM_MEM[0]

	c_t5_t41_mem1 = S.Task('c_t5_t41_mem1', length=1, delay_cost=1)
	S += c_t5_t41_mem1 >= 64
	c_t5_t41_mem1 += MAS_MEM[1]

	c_t7110 = S.Task('c_t7110', length=1, delay_cost=1)
	S += c_t7110 >= 64
	c_t7110 += MAS[0]

	c_t301 = S.Task('c_t301', length=1, delay_cost=1)
	S += c_t301 >= 65
	c_t301 += MAS[3]

	c_t3_t41_mem0 = S.Task('c_t3_t41_mem0', length=1, delay_cost=1)
	S += c_t3_t41_mem0 >= 65
	c_t3_t41_mem0 += MM_MEM[0]

	c_t3_t41_mem1 = S.Task('c_t3_t41_mem1', length=1, delay_cost=1)
	S += c_t3_t41_mem1 >= 65
	c_t3_t41_mem1 += MAS_MEM[3]

	c_t411 = S.Task('c_t411', length=1, delay_cost=1)
	S += c_t411 >= 65
	c_t411 += MAS[1]

	c_t511_mem0 = S.Task('c_t511_mem0', length=1, delay_cost=1)
	S += c_t511_mem0 >= 65
	c_t511_mem0 += MAS_MEM[0]

	c_t511_mem1 = S.Task('c_t511_mem1', length=1, delay_cost=1)
	S += c_t511_mem1 >= 65
	c_t511_mem1 += MAS_MEM[1]

	c_t5_t41 = S.Task('c_t5_t41', length=1, delay_cost=1)
	S += c_t5_t41 >= 65
	c_t5_t41 += MAS[0]

	c_t311_mem0 = S.Task('c_t311_mem0', length=1, delay_cost=1)
	S += c_t311_mem0 >= 66
	c_t311_mem0 += MAS_MEM[4]

	c_t311_mem1 = S.Task('c_t311_mem1', length=1, delay_cost=1)
	S += c_t311_mem1 >= 66
	c_t311_mem1 += MAS_MEM[7]

	c_t3_t41 = S.Task('c_t3_t41', length=1, delay_cost=1)
	S += c_t3_t41 >= 66
	c_t3_t41 += MAS[2]

	c_t511 = S.Task('c_t511', length=1, delay_cost=1)
	S += c_t511 >= 66
	c_t511 += MAS[1]

	c_t311 = S.Task('c_t311', length=1, delay_cost=1)
	S += c_t311 >= 67
	c_t311 += MAS[2]


	# new tasks
	c_t600 = S.Task('c_t600', length=1, delay_cost=1)
	c_t600 += alt(MAS)

	c_t600_mem0 = S.Task('c_t600_mem0', length=1, delay_cost=1)
	c_t600_mem0 += MAS_MEM[2]
	S += 63 < c_t600_mem0
	S += c_t600_mem0 <= c_t600

	c_t600_mem1 = S.Task('c_t600_mem1', length=1, delay_cost=1)
	c_t600_mem1 += MAS_MEM[3]
	S += 51 < c_t600_mem1
	S += c_t600_mem1 <= c_t600

	c_t601 = S.Task('c_t601', length=1, delay_cost=1)
	c_t601 += alt(MAS)

	c_t601_mem0 = S.Task('c_t601_mem0', length=1, delay_cost=1)
	c_t601_mem0 += MAS_MEM[6]
	S += 65 < c_t601_mem0
	S += c_t601_mem0 <= c_t601

	c_t601_mem1 = S.Task('c_t601_mem1', length=1, delay_cost=1)
	c_t601_mem1 += MAS_MEM[1]
	S += 47 < c_t601_mem1
	S += c_t601_mem1 <= c_t601

	c_t611 = S.Task('c_t611', length=1, delay_cost=1)
	c_t611 += alt(MAS)

	c_t611_mem0 = S.Task('c_t611_mem0', length=1, delay_cost=1)
	c_t611_mem0 += MAS_MEM[4]
	S += 67 < c_t611_mem0
	S += c_t611_mem0 <= c_t611

	c_t611_mem1 = S.Task('c_t611_mem1', length=1, delay_cost=1)
	c_t611_mem1 += MAS_MEM[5]
	S += 59 < c_t611_mem1
	S += c_t611_mem1 <= c_t611

	c110 = S.Task('c110', length=1, delay_cost=1)
	c110 += alt(MAS)

	S += 12<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[2]
	S += 52 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MAS_MEM[1]
	S += 48 < c110_mem1
	S += c110_mem1 <= c110

	c_t7100 = S.Task('c_t7100', length=1, delay_cost=1)
	c_t7100 += alt(MAS)

	c_t7100_mem0 = S.Task('c_t7100_mem0', length=1, delay_cost=1)
	c_t7100_mem0 += MAS_MEM[4]
	S += 58 < c_t7100_mem0
	S += c_t7100_mem0 <= c_t7100

	c_t7100_mem1 = S.Task('c_t7100_mem1', length=1, delay_cost=1)
	c_t7100_mem1 += MAS_MEM[3]
	S += 57 < c_t7100_mem1
	S += c_t7100_mem1 <= c_t7100

	c_t7101 = S.Task('c_t7101', length=1, delay_cost=1)
	c_t7101 += alt(MAS)

	c_t7101_mem0 = S.Task('c_t7101_mem0', length=1, delay_cost=1)
	c_t7101_mem0 += MAS_MEM[4]
	S += 56 < c_t7101_mem0
	S += c_t7101_mem0 <= c_t7101

	c_t7101_mem1 = S.Task('c_t7101_mem1', length=1, delay_cost=1)
	c_t7101_mem1 += MAS_MEM[3]
	S += 45 < c_t7101_mem1
	S += c_t7101_mem1 <= c_t7101

	c_t7111 = S.Task('c_t7111', length=1, delay_cost=1)
	c_t7111 += alt(MAS)

	c_t7111_mem0 = S.Task('c_t7111_mem0', length=1, delay_cost=1)
	c_t7111_mem0 += MAS_MEM[2]
	S += 65 < c_t7111_mem0
	S += c_t7111_mem0 <= c_t7111

	c_t7111_mem1 = S.Task('c_t7111_mem1', length=1, delay_cost=1)
	c_t7111_mem1 += MAS_MEM[3]
	S += 56 < c_t7111_mem1
	S += c_t7111_mem1 <= c_t7111

	c_t800 = S.Task('c_t800', length=1, delay_cost=1)
	c_t800 += alt(MAS)

	c_t800_mem0 = S.Task('c_t800_mem0', length=1, delay_cost=1)
	c_t800_mem0 += MAS_MEM[0]
	S += 54 < c_t800_mem0
	S += c_t800_mem0 <= c_t800

	c_t800_mem1 = S.Task('c_t800_mem1', length=1, delay_cost=1)
	c_t800_mem1 += MAS_MEM[1]
	S += 49 < c_t800_mem1
	S += c_t800_mem1 <= c_t800

	c_t801 = S.Task('c_t801', length=1, delay_cost=1)
	c_t801 += alt(MAS)

	c_t801_mem0 = S.Task('c_t801_mem0', length=1, delay_cost=1)
	c_t801_mem0 += MAS_MEM[2]
	S += 61 < c_t801_mem0
	S += c_t801_mem0 <= c_t801

	c_t801_mem1 = S.Task('c_t801_mem1', length=1, delay_cost=1)
	c_t801_mem1 += MAS_MEM[3]
	S += 47 < c_t801_mem1
	S += c_t801_mem1 <= c_t801

	c_t811 = S.Task('c_t811', length=1, delay_cost=1)
	c_t811 += alt(MAS)

	c_t811_mem0 = S.Task('c_t811_mem0', length=1, delay_cost=1)
	c_t811_mem0 += MAS_MEM[2]
	S += 66 < c_t811_mem0
	S += c_t811_mem0 <= c_t811

	c_t811_mem1 = S.Task('c_t811_mem1', length=1, delay_cost=1)
	c_t811_mem1 += MAS_MEM[3]
	S += 58 < c_t811_mem1
	S += c_t811_mem1 <= c_t811

	c210 = S.Task('c210', length=1, delay_cost=1)
	c210 += alt(MAS)

	S += 12<c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MAS_MEM[4]
	S += 60 < c210_mem0
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MAS_MEM[1]
	S += 39 < c210_mem1
	S += c210_mem1 <= c210

	c100 = S.Task('c100', length=1, delay_cost=1)
	c100 += alt(MAS)

	S += 10<c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += alt(MAS_MEM)
	S += (c_t600*MAS[0])-1 < c100_mem0*MAS_MEM[0]
	S += (c_t600*MAS[1])-1 < c100_mem0*MAS_MEM[2]
	S += (c_t600*MAS[2])-1 < c100_mem0*MAS_MEM[4]
	S += (c_t600*MAS[3])-1 < c100_mem0*MAS_MEM[6]
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += MAS_MEM[5]
	S += 53 < c100_mem1
	S += c100_mem1 <= c100

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(MAS)

	S += 12<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += alt(MAS_MEM)
	S += (c_t601*MAS[0])-1 < c101_mem0*MAS_MEM[0]
	S += (c_t601*MAS[1])-1 < c101_mem0*MAS_MEM[2]
	S += (c_t601*MAS[2])-1 < c101_mem0*MAS_MEM[4]
	S += (c_t601*MAS[3])-1 < c101_mem0*MAS_MEM[6]
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += MAS_MEM[7]
	S += 52 < c101_mem1
	S += c101_mem1 <= c101

	c111 = S.Task('c111', length=1, delay_cost=1)
	c111 += alt(MAS)

	S += 12<c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += alt(MAS_MEM)
	S += (c_t611*MAS[0])-1 < c111_mem0*MAS_MEM[0]
	S += (c_t611*MAS[1])-1 < c111_mem0*MAS_MEM[2]
	S += (c_t611*MAS[2])-1 < c111_mem0*MAS_MEM[4]
	S += (c_t611*MAS[3])-1 < c111_mem0*MAS_MEM[6]
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += MAS_MEM[5]
	S += 44 < c111_mem1
	S += c111_mem1 <= c111

	c_t7_y1_0 = S.Task('c_t7_y1_0', length=1, delay_cost=1)
	c_t7_y1_0 += alt(MAS)

	c_t7_y1_0_mem0 = S.Task('c_t7_y1_0_mem0', length=1, delay_cost=1)
	c_t7_y1_0_mem0 += MAS_MEM[0]
	S += 64 < c_t7_y1_0_mem0
	S += c_t7_y1_0_mem0 <= c_t7_y1_0

	c_t7_y1_0_mem1 = S.Task('c_t7_y1_0_mem1', length=1, delay_cost=1)
	c_t7_y1_0_mem1 += alt(MAS_MEM)
	S += (c_t7111*MAS[0])-1 < c_t7_y1_0_mem1*MAS_MEM[1]
	S += (c_t7111*MAS[1])-1 < c_t7_y1_0_mem1*MAS_MEM[3]
	S += (c_t7111*MAS[2])-1 < c_t7_y1_0_mem1*MAS_MEM[5]
	S += (c_t7111*MAS[3])-1 < c_t7_y1_0_mem1*MAS_MEM[7]
	S += c_t7_y1_0_mem1 <= c_t7_y1_0

	c_t7_y1_1 = S.Task('c_t7_y1_1', length=1, delay_cost=1)
	c_t7_y1_1 += alt(MAS)

	c_t7_y1_1_mem0 = S.Task('c_t7_y1_1_mem0', length=1, delay_cost=1)
	c_t7_y1_1_mem0 += alt(MAS_MEM)
	S += (c_t7111*MAS[0])-1 < c_t7_y1_1_mem0*MAS_MEM[0]
	S += (c_t7111*MAS[1])-1 < c_t7_y1_1_mem0*MAS_MEM[2]
	S += (c_t7111*MAS[2])-1 < c_t7_y1_1_mem0*MAS_MEM[4]
	S += (c_t7111*MAS[3])-1 < c_t7_y1_1_mem0*MAS_MEM[6]
	S += c_t7_y1_1_mem0 <= c_t7_y1_1

	c_t7_y1_1_mem1 = S.Task('c_t7_y1_1_mem1', length=1, delay_cost=1)
	c_t7_y1_1_mem1 += MAS_MEM[1]
	S += 64 < c_t7_y1_1_mem1
	S += c_t7_y1_1_mem1 <= c_t7_y1_1

	c010 = S.Task('c010', length=1, delay_cost=1)
	c010 += alt(MAS)

	S += 10<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += MAS_MEM[0]
	S += 40 < c010_mem0
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += alt(MAS_MEM)
	S += (c_t7100*MAS[0])-1 < c010_mem1*MAS_MEM[1]
	S += (c_t7100*MAS[1])-1 < c010_mem1*MAS_MEM[3]
	S += (c_t7100*MAS[2])-1 < c010_mem1*MAS_MEM[5]
	S += (c_t7100*MAS[3])-1 < c010_mem1*MAS_MEM[7]
	S += c010_mem1 <= c010

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(MAS)

	S += 9<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MAS_MEM[0]
	S += 57 < c011_mem0
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(MAS_MEM)
	S += (c_t7101*MAS[0])-1 < c011_mem1*MAS_MEM[1]
	S += (c_t7101*MAS[1])-1 < c011_mem1*MAS_MEM[3]
	S += (c_t7101*MAS[2])-1 < c011_mem1*MAS_MEM[5]
	S += (c_t7101*MAS[3])-1 < c011_mem1*MAS_MEM[7]
	S += c011_mem1 <= c011

	c200 = S.Task('c200', length=1, delay_cost=1)
	c200 += alt(MAS)

	S += 12<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += alt(MAS_MEM)
	S += (c_t800*MAS[0])-1 < c200_mem0*MAS_MEM[0]
	S += (c_t800*MAS[1])-1 < c200_mem0*MAS_MEM[2]
	S += (c_t800*MAS[2])-1 < c200_mem0*MAS_MEM[4]
	S += (c_t800*MAS[3])-1 < c200_mem0*MAS_MEM[6]
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += MAS_MEM[3]
	S += 49 < c200_mem1
	S += c200_mem1 <= c200

	c201 = S.Task('c201', length=1, delay_cost=1)
	c201 += alt(MAS)

	S += 12<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += alt(MAS_MEM)
	S += (c_t801*MAS[0])-1 < c201_mem0*MAS_MEM[0]
	S += (c_t801*MAS[1])-1 < c201_mem0*MAS_MEM[2]
	S += (c_t801*MAS[2])-1 < c201_mem0*MAS_MEM[4]
	S += (c_t801*MAS[3])-1 < c201_mem0*MAS_MEM[6]
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += MAS_MEM[5]
	S += 41 < c201_mem1
	S += c201_mem1 <= c201

	c211 = S.Task('c211', length=1, delay_cost=1)
	c211 += alt(MAS)

	S += 12<c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(MAS_MEM)
	S += (c_t811*MAS[0])-1 < c211_mem0*MAS_MEM[0]
	S += (c_t811*MAS[1])-1 < c211_mem0*MAS_MEM[2]
	S += (c_t811*MAS[2])-1 < c211_mem0*MAS_MEM[4]
	S += (c_t811*MAS[3])-1 < c211_mem0*MAS_MEM[6]
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += MAS_MEM[1]
	S += 55 < c211_mem1
	S += c211_mem1 <= c211

	c000 = S.Task('c000', length=1, delay_cost=1)
	c000 += alt(MAS)

	S += 10<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[4]
	S += 34 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (c_t7_y1_0*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (c_t7_y1_0*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (c_t7_y1_0*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (c_t7_y1_0*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += c000_mem1 <= c000

	c001 = S.Task('c001', length=1, delay_cost=1)
	c001 += alt(MAS)

	S += 11<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[2]
	S += 46 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (c_t7_y1_1*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += (c_t7_y1_1*MAS[1])-1 < c001_mem1*MAS_MEM[3]
	S += (c_t7_y1_1*MAS[2])-1 < c001_mem1*MAS_MEM[5]
	S += (c_t7_y1_1*MAS[3])-1 < c001_mem1*MAS_MEM[7]
	S += c001_mem1 <= c001

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage1MAS4/MUL/schedule7.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

