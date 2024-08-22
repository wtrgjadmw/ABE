from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 110
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MUL = S.Resources('MUL', num=1, size=4)
	MUL_in = S.Resources('MUL_in', num=1)
	INV = S.Resource('INV')
	MAS = S.Resources('MAS', num=1, size=1, periods=range(1, horizon))
	MAS_in = S.Resources('MAS_in', num=1)
	INPUT_mem_w = S.Resource('INPUT_mem_w', size=2)
	INPUT_mem_r = S.Resource('INPUT_mem_r', size=4)

	# result of previous scheduling
	c_t0_t0_t3_in = S.Task('c_t0_t0_t3_in', length=1, delay_cost=1)
	S += c_t0_t0_t3_in >= 0
	c_t0_t0_t3_in += MAS_in[0]

	c_t2_t1_t0_in = S.Task('c_t2_t1_t0_in', length=1, delay_cost=1)
	S += c_t2_t1_t0_in >= 0
	c_t2_t1_t0_in += MUL_in[0]

	c_t0_t0_t3 = S.Task('c_t0_t0_t3', length=1, delay_cost=1)
	S += c_t0_t0_t3 >= 1
	c_t0_t0_t3 += MAS[0]

	c_t0_t0_t3_mem0 = S.Task('c_t0_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem0 >= 1
	c_t0_t0_t3_mem0 += INPUT_mem_r

	c_t0_t0_t3_mem1 = S.Task('c_t0_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t3_mem1 >= 1
	c_t0_t0_t3_mem1 += INPUT_mem_r

	c_t0_t1_t0_in = S.Task('c_t0_t1_t0_in', length=1, delay_cost=1)
	S += c_t0_t1_t0_in >= 1
	c_t0_t1_t0_in += MUL_in[0]

	c_t2_t0_t3_in = S.Task('c_t2_t0_t3_in', length=1, delay_cost=1)
	S += c_t2_t0_t3_in >= 1
	c_t2_t0_t3_in += MAS_in[0]

	c_t2_t1_t0 = S.Task('c_t2_t1_t0', length=4, delay_cost=1)
	S += c_t2_t1_t0 >= 1
	c_t2_t1_t0 += MUL[0]

	c_t2_t1_t0_mem0 = S.Task('c_t2_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem0 >= 1
	c_t2_t1_t0_mem0 += INPUT_mem_r

	c_t2_t1_t0_mem1 = S.Task('c_t2_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t0_mem1 >= 1
	c_t2_t1_t0_mem1 += INPUT_mem_r

	c_t0_t1_t0 = S.Task('c_t0_t1_t0', length=4, delay_cost=1)
	S += c_t0_t1_t0 >= 2
	c_t0_t1_t0 += MUL[0]

	c_t0_t1_t0_mem0 = S.Task('c_t0_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem0 >= 2
	c_t0_t1_t0_mem0 += INPUT_mem_r

	c_t0_t1_t0_mem1 = S.Task('c_t0_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t0_mem1 >= 2
	c_t0_t1_t0_mem1 += INPUT_mem_r

	c_t1_t1_t2_in = S.Task('c_t1_t1_t2_in', length=1, delay_cost=1)
	S += c_t1_t1_t2_in >= 2
	c_t1_t1_t2_in += MAS_in[0]

	c_t2_t0_t3 = S.Task('c_t2_t0_t3', length=1, delay_cost=1)
	S += c_t2_t0_t3 >= 2
	c_t2_t0_t3 += MAS[0]

	c_t2_t0_t3_mem0 = S.Task('c_t2_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem0 >= 2
	c_t2_t0_t3_mem0 += INPUT_mem_r

	c_t2_t0_t3_mem1 = S.Task('c_t2_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t3_mem1 >= 2
	c_t2_t0_t3_mem1 += INPUT_mem_r

	c_t2_t1_t1_in = S.Task('c_t2_t1_t1_in', length=1, delay_cost=1)
	S += c_t2_t1_t1_in >= 2
	c_t2_t1_t1_in += MUL_in[0]

	c_t0_t0_t0_in = S.Task('c_t0_t0_t0_in', length=1, delay_cost=1)
	S += c_t0_t0_t0_in >= 3
	c_t0_t0_t0_in += MUL_in[0]

	c_t0_t1_t2_in = S.Task('c_t0_t1_t2_in', length=1, delay_cost=1)
	S += c_t0_t1_t2_in >= 3
	c_t0_t1_t2_in += MAS_in[0]

	c_t1_t1_t2 = S.Task('c_t1_t1_t2', length=1, delay_cost=1)
	S += c_t1_t1_t2 >= 3
	c_t1_t1_t2 += MAS[0]

	c_t1_t1_t2_mem0 = S.Task('c_t1_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem0 >= 3
	c_t1_t1_t2_mem0 += INPUT_mem_r

	c_t1_t1_t2_mem1 = S.Task('c_t1_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t2_mem1 >= 3
	c_t1_t1_t2_mem1 += INPUT_mem_r

	c_t2_t1_t1 = S.Task('c_t2_t1_t1', length=4, delay_cost=1)
	S += c_t2_t1_t1 >= 3
	c_t2_t1_t1 += MUL[0]

	c_t2_t1_t1_mem0 = S.Task('c_t2_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem0 >= 3
	c_t2_t1_t1_mem0 += INPUT_mem_r

	c_t2_t1_t1_mem1 = S.Task('c_t2_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t1_t1_mem1 >= 3
	c_t2_t1_t1_mem1 += INPUT_mem_r

	c_t0_t0_t0 = S.Task('c_t0_t0_t0', length=4, delay_cost=1)
	S += c_t0_t0_t0 >= 4
	c_t0_t0_t0 += MUL[0]

	c_t0_t0_t0_mem0 = S.Task('c_t0_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem0 >= 4
	c_t0_t0_t0_mem0 += INPUT_mem_r

	c_t0_t0_t0_mem1 = S.Task('c_t0_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t0_mem1 >= 4
	c_t0_t0_t0_mem1 += INPUT_mem_r

	c_t0_t1_t2 = S.Task('c_t0_t1_t2', length=1, delay_cost=1)
	S += c_t0_t1_t2 >= 4
	c_t0_t1_t2 += MAS[0]

	c_t0_t1_t2_mem0 = S.Task('c_t0_t1_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem0 >= 4
	c_t0_t1_t2_mem0 += INPUT_mem_r

	c_t0_t1_t2_mem1 = S.Task('c_t0_t1_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t2_mem1 >= 4
	c_t0_t1_t2_mem1 += INPUT_mem_r

	c_t1_t0_t2_in = S.Task('c_t1_t0_t2_in', length=1, delay_cost=1)
	S += c_t1_t0_t2_in >= 4
	c_t1_t0_t2_in += MAS_in[0]

	c_t1_t1_t0_in = S.Task('c_t1_t1_t0_in', length=1, delay_cost=1)
	S += c_t1_t1_t0_in >= 4
	c_t1_t1_t0_in += MUL_in[0]

	c_t0_t0_t1_in = S.Task('c_t0_t0_t1_in', length=1, delay_cost=1)
	S += c_t0_t0_t1_in >= 5
	c_t0_t0_t1_in += MUL_in[0]

	c_t1_t0_t2 = S.Task('c_t1_t0_t2', length=1, delay_cost=1)
	S += c_t1_t0_t2 >= 5
	c_t1_t0_t2 += MAS[0]

	c_t1_t0_t2_mem0 = S.Task('c_t1_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem0 >= 5
	c_t1_t0_t2_mem0 += INPUT_mem_r

	c_t1_t0_t2_mem1 = S.Task('c_t1_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t2_mem1 >= 5
	c_t1_t0_t2_mem1 += INPUT_mem_r

	c_t1_t1_t0 = S.Task('c_t1_t1_t0', length=4, delay_cost=1)
	S += c_t1_t1_t0 >= 5
	c_t1_t1_t0 += MUL[0]

	c_t1_t1_t0_mem0 = S.Task('c_t1_t1_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem0 >= 5
	c_t1_t1_t0_mem0 += INPUT_mem_r

	c_t1_t1_t0_mem1 = S.Task('c_t1_t1_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t0_mem1 >= 5
	c_t1_t1_t0_mem1 += INPUT_mem_r

	c_t2_t0_t2_in = S.Task('c_t2_t0_t2_in', length=1, delay_cost=1)
	S += c_t2_t0_t2_in >= 5
	c_t2_t0_t2_in += MAS_in[0]

	c_t0_t0_t1 = S.Task('c_t0_t0_t1', length=4, delay_cost=1)
	S += c_t0_t0_t1 >= 6
	c_t0_t0_t1 += MUL[0]

	c_t0_t0_t1_mem0 = S.Task('c_t0_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem0 >= 6
	c_t0_t0_t1_mem0 += INPUT_mem_r

	c_t0_t0_t1_mem1 = S.Task('c_t0_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t1_mem1 >= 6
	c_t0_t0_t1_mem1 += INPUT_mem_r

	c_t0_t1_t1_in = S.Task('c_t0_t1_t1_in', length=1, delay_cost=1)
	S += c_t0_t1_t1_in >= 6
	c_t0_t1_t1_in += MUL_in[0]

	c_t1_t21_in = S.Task('c_t1_t21_in', length=1, delay_cost=1)
	S += c_t1_t21_in >= 6
	c_t1_t21_in += MAS_in[0]

	c_t2_t0_t2 = S.Task('c_t2_t0_t2', length=1, delay_cost=1)
	S += c_t2_t0_t2 >= 6
	c_t2_t0_t2 += MAS[0]

	c_t2_t0_t2_mem0 = S.Task('c_t2_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem0 >= 6
	c_t2_t0_t2_mem0 += INPUT_mem_r

	c_t2_t0_t2_mem1 = S.Task('c_t2_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t2_mem1 >= 6
	c_t2_t0_t2_mem1 += INPUT_mem_r

	c_t0_t1_t1 = S.Task('c_t0_t1_t1', length=4, delay_cost=1)
	S += c_t0_t1_t1 >= 7
	c_t0_t1_t1 += MUL[0]

	c_t0_t1_t1_mem0 = S.Task('c_t0_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem0 >= 7
	c_t0_t1_t1_mem0 += INPUT_mem_r

	c_t0_t1_t1_mem1 = S.Task('c_t0_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t1_mem1 >= 7
	c_t0_t1_t1_mem1 += INPUT_mem_r

	c_t1_t0_t3_in = S.Task('c_t1_t0_t3_in', length=1, delay_cost=1)
	S += c_t1_t0_t3_in >= 7
	c_t1_t0_t3_in += MAS_in[0]

	c_t1_t21 = S.Task('c_t1_t21', length=1, delay_cost=1)
	S += c_t1_t21 >= 7
	c_t1_t21 += MAS[0]

	c_t1_t21_mem0 = S.Task('c_t1_t21_mem0', length=1, delay_cost=1)
	S += c_t1_t21_mem0 >= 7
	c_t1_t21_mem0 += INPUT_mem_r

	c_t1_t21_mem1 = S.Task('c_t1_t21_mem1', length=1, delay_cost=1)
	S += c_t1_t21_mem1 >= 7
	c_t1_t21_mem1 += INPUT_mem_r

	c_t2_t0_t1_in = S.Task('c_t2_t0_t1_in', length=1, delay_cost=1)
	S += c_t2_t0_t1_in >= 7
	c_t2_t0_t1_in += MUL_in[0]

	c_t1_t0_t3 = S.Task('c_t1_t0_t3', length=1, delay_cost=1)
	S += c_t1_t0_t3 >= 8
	c_t1_t0_t3 += MAS[0]

	c_t1_t0_t3_mem0 = S.Task('c_t1_t0_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem0 >= 8
	c_t1_t0_t3_mem0 += INPUT_mem_r

	c_t1_t0_t3_mem1 = S.Task('c_t1_t0_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t3_mem1 >= 8
	c_t1_t0_t3_mem1 += INPUT_mem_r

	c_t1_t1_t1_in = S.Task('c_t1_t1_t1_in', length=1, delay_cost=1)
	S += c_t1_t1_t1_in >= 8
	c_t1_t1_t1_in += MUL_in[0]

	c_t1_t20_in = S.Task('c_t1_t20_in', length=1, delay_cost=1)
	S += c_t1_t20_in >= 8
	c_t1_t20_in += MAS_in[0]

	c_t2_t0_t1 = S.Task('c_t2_t0_t1', length=4, delay_cost=1)
	S += c_t2_t0_t1 >= 8
	c_t2_t0_t1 += MUL[0]

	c_t2_t0_t1_mem0 = S.Task('c_t2_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem0 >= 8
	c_t2_t0_t1_mem0 += INPUT_mem_r

	c_t2_t0_t1_mem1 = S.Task('c_t2_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t1_mem1 >= 8
	c_t2_t0_t1_mem1 += INPUT_mem_r

	c_t0_t20_in = S.Task('c_t0_t20_in', length=1, delay_cost=1)
	S += c_t0_t20_in >= 9
	c_t0_t20_in += MAS_in[0]

	c_t1_t0_t0_in = S.Task('c_t1_t0_t0_in', length=1, delay_cost=1)
	S += c_t1_t0_t0_in >= 9
	c_t1_t0_t0_in += MUL_in[0]

	c_t1_t1_t1 = S.Task('c_t1_t1_t1', length=4, delay_cost=1)
	S += c_t1_t1_t1 >= 9
	c_t1_t1_t1 += MUL[0]

	c_t1_t1_t1_mem0 = S.Task('c_t1_t1_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem0 >= 9
	c_t1_t1_t1_mem0 += INPUT_mem_r

	c_t1_t1_t1_mem1 = S.Task('c_t1_t1_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t1_mem1 >= 9
	c_t1_t1_t1_mem1 += INPUT_mem_r

	c_t1_t20 = S.Task('c_t1_t20', length=1, delay_cost=1)
	S += c_t1_t20 >= 9
	c_t1_t20 += MAS[0]

	c_t1_t20_mem0 = S.Task('c_t1_t20_mem0', length=1, delay_cost=1)
	S += c_t1_t20_mem0 >= 9
	c_t1_t20_mem0 += INPUT_mem_r

	c_t1_t20_mem1 = S.Task('c_t1_t20_mem1', length=1, delay_cost=1)
	S += c_t1_t20_mem1 >= 9
	c_t1_t20_mem1 += INPUT_mem_r

	c_t0_t20 = S.Task('c_t0_t20', length=1, delay_cost=1)
	S += c_t0_t20 >= 10
	c_t0_t20 += MAS[0]

	c_t0_t20_mem0 = S.Task('c_t0_t20_mem0', length=1, delay_cost=1)
	S += c_t0_t20_mem0 >= 10
	c_t0_t20_mem0 += INPUT_mem_r

	c_t0_t20_mem1 = S.Task('c_t0_t20_mem1', length=1, delay_cost=1)
	S += c_t0_t20_mem1 >= 10
	c_t0_t20_mem1 += INPUT_mem_r

	c_t0_t30_in = S.Task('c_t0_t30_in', length=1, delay_cost=1)
	S += c_t0_t30_in >= 10
	c_t0_t30_in += MAS_in[0]

	c_t1_t0_t0 = S.Task('c_t1_t0_t0', length=4, delay_cost=1)
	S += c_t1_t0_t0 >= 10
	c_t1_t0_t0 += MUL[0]

	c_t1_t0_t0_mem0 = S.Task('c_t1_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem0 >= 10
	c_t1_t0_t0_mem0 += INPUT_mem_r

	c_t1_t0_t0_mem1 = S.Task('c_t1_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t0_mem1 >= 10
	c_t1_t0_t0_mem1 += INPUT_mem_r

	c_t2_t0_t0_in = S.Task('c_t2_t0_t0_in', length=1, delay_cost=1)
	S += c_t2_t0_t0_in >= 10
	c_t2_t0_t0_in += MUL_in[0]

	c_t0_t30 = S.Task('c_t0_t30', length=1, delay_cost=1)
	S += c_t0_t30 >= 11
	c_t0_t30 += MAS[0]

	c_t0_t30_mem0 = S.Task('c_t0_t30_mem0', length=1, delay_cost=1)
	S += c_t0_t30_mem0 >= 11
	c_t0_t30_mem0 += INPUT_mem_r

	c_t0_t30_mem1 = S.Task('c_t0_t30_mem1', length=1, delay_cost=1)
	S += c_t0_t30_mem1 >= 11
	c_t0_t30_mem1 += INPUT_mem_r

	c_t1_t0_t1_in = S.Task('c_t1_t0_t1_in', length=1, delay_cost=1)
	S += c_t1_t0_t1_in >= 11
	c_t1_t0_t1_in += MUL_in[0]

	c_t1_t30_in = S.Task('c_t1_t30_in', length=1, delay_cost=1)
	S += c_t1_t30_in >= 11
	c_t1_t30_in += MAS_in[0]

	c_t2_t0_t0 = S.Task('c_t2_t0_t0', length=4, delay_cost=1)
	S += c_t2_t0_t0 >= 11
	c_t2_t0_t0 += MUL[0]

	c_t2_t0_t0_mem0 = S.Task('c_t2_t0_t0_mem0', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem0 >= 11
	c_t2_t0_t0_mem0 += INPUT_mem_r

	c_t2_t0_t0_mem1 = S.Task('c_t2_t0_t0_mem1', length=1, delay_cost=1)
	S += c_t2_t0_t0_mem1 >= 11
	c_t2_t0_t0_mem1 += INPUT_mem_r

	c_t0_t0_t2_in = S.Task('c_t0_t0_t2_in', length=1, delay_cost=1)
	S += c_t0_t0_t2_in >= 12
	c_t0_t0_t2_in += MAS_in[0]

	c_t1_t0_t1 = S.Task('c_t1_t0_t1', length=4, delay_cost=1)
	S += c_t1_t0_t1 >= 12
	c_t1_t0_t1 += MUL[0]

	c_t1_t0_t1_mem0 = S.Task('c_t1_t0_t1_mem0', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem0 >= 12
	c_t1_t0_t1_mem0 += INPUT_mem_r

	c_t1_t0_t1_mem1 = S.Task('c_t1_t0_t1_mem1', length=1, delay_cost=1)
	S += c_t1_t0_t1_mem1 >= 12
	c_t1_t0_t1_mem1 += INPUT_mem_r

	c_t1_t30 = S.Task('c_t1_t30', length=1, delay_cost=1)
	S += c_t1_t30 >= 12
	c_t1_t30 += MAS[0]

	c_t1_t30_mem0 = S.Task('c_t1_t30_mem0', length=1, delay_cost=1)
	S += c_t1_t30_mem0 >= 12
	c_t1_t30_mem0 += INPUT_mem_r

	c_t1_t30_mem1 = S.Task('c_t1_t30_mem1', length=1, delay_cost=1)
	S += c_t1_t30_mem1 >= 12
	c_t1_t30_mem1 += INPUT_mem_r

	c_t0_t0_t2 = S.Task('c_t0_t0_t2', length=1, delay_cost=1)
	S += c_t0_t0_t2 >= 13
	c_t0_t0_t2 += MAS[0]

	c_t0_t0_t2_mem0 = S.Task('c_t0_t0_t2_mem0', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem0 >= 13
	c_t0_t0_t2_mem0 += INPUT_mem_r

	c_t0_t0_t2_mem1 = S.Task('c_t0_t0_t2_mem1', length=1, delay_cost=1)
	S += c_t0_t0_t2_mem1 >= 13
	c_t0_t0_t2_mem1 += INPUT_mem_r

	c_t0_t31_in = S.Task('c_t0_t31_in', length=1, delay_cost=1)
	S += c_t0_t31_in >= 13
	c_t0_t31_in += MAS_in[0]

	c_t0_t1_t3_in = S.Task('c_t0_t1_t3_in', length=1, delay_cost=1)
	S += c_t0_t1_t3_in >= 14
	c_t0_t1_t3_in += MAS_in[0]

	c_t0_t31 = S.Task('c_t0_t31', length=1, delay_cost=1)
	S += c_t0_t31 >= 14
	c_t0_t31 += MAS[0]

	c_t0_t31_mem0 = S.Task('c_t0_t31_mem0', length=1, delay_cost=1)
	S += c_t0_t31_mem0 >= 14
	c_t0_t31_mem0 += INPUT_mem_r

	c_t0_t31_mem1 = S.Task('c_t0_t31_mem1', length=1, delay_cost=1)
	S += c_t0_t31_mem1 >= 14
	c_t0_t31_mem1 += INPUT_mem_r

	c_t0_t1_t3 = S.Task('c_t0_t1_t3', length=1, delay_cost=1)
	S += c_t0_t1_t3 >= 15
	c_t0_t1_t3 += MAS[0]

	c_t0_t1_t3_mem0 = S.Task('c_t0_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem0 >= 15
	c_t0_t1_t3_mem0 += INPUT_mem_r

	c_t0_t1_t3_mem1 = S.Task('c_t0_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t0_t1_t3_mem1 >= 15
	c_t0_t1_t3_mem1 += INPUT_mem_r

	c_t1_t31_in = S.Task('c_t1_t31_in', length=1, delay_cost=1)
	S += c_t1_t31_in >= 15
	c_t1_t31_in += MAS_in[0]

	c_t0_t21_in = S.Task('c_t0_t21_in', length=1, delay_cost=1)
	S += c_t0_t21_in >= 16
	c_t0_t21_in += MAS_in[0]

	c_t1_t31 = S.Task('c_t1_t31', length=1, delay_cost=1)
	S += c_t1_t31 >= 16
	c_t1_t31 += MAS[0]

	c_t1_t31_mem0 = S.Task('c_t1_t31_mem0', length=1, delay_cost=1)
	S += c_t1_t31_mem0 >= 16
	c_t1_t31_mem0 += INPUT_mem_r

	c_t1_t31_mem1 = S.Task('c_t1_t31_mem1', length=1, delay_cost=1)
	S += c_t1_t31_mem1 >= 16
	c_t1_t31_mem1 += INPUT_mem_r

	c_t0_t21 = S.Task('c_t0_t21', length=1, delay_cost=1)
	S += c_t0_t21 >= 17
	c_t0_t21 += MAS[0]

	c_t0_t21_mem0 = S.Task('c_t0_t21_mem0', length=1, delay_cost=1)
	S += c_t0_t21_mem0 >= 17
	c_t0_t21_mem0 += INPUT_mem_r

	c_t0_t21_mem1 = S.Task('c_t0_t21_mem1', length=1, delay_cost=1)
	S += c_t0_t21_mem1 >= 17
	c_t0_t21_mem1 += INPUT_mem_r

	c_t1_t1_t3_in = S.Task('c_t1_t1_t3_in', length=1, delay_cost=1)
	S += c_t1_t1_t3_in >= 17
	c_t1_t1_t3_in += MAS_in[0]

	c_t1_t1_t3 = S.Task('c_t1_t1_t3', length=1, delay_cost=1)
	S += c_t1_t1_t3 >= 18
	c_t1_t1_t3 += MAS[0]

	c_t1_t1_t3_mem0 = S.Task('c_t1_t1_t3_mem0', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem0 >= 18
	c_t1_t1_t3_mem0 += INPUT_mem_r

	c_t1_t1_t3_mem1 = S.Task('c_t1_t1_t3_mem1', length=1, delay_cost=1)
	S += c_t1_t1_t3_mem1 >= 18
	c_t1_t1_t3_mem1 += INPUT_mem_r


	# new tasks
	c_t2_t1_t2_in = S.Task('c_t2_t1_t2_in', length=1, delay_cost=1)
	c_t2_t1_t2_in += alt(MAS_in)
	c_t2_t1_t2 = S.Task('c_t2_t1_t2', length=1, delay_cost=1)
	c_t2_t1_t2 += alt(MAS)

	S += c_t2_t1_t2>=c_t2_t1_t2_in

	c_t2_t1_t2_mem0 = S.Task('c_t2_t1_t2_mem0', length=1, delay_cost=1)
	c_t2_t1_t2_mem0 += INPUT_mem_r
	S += c_t2_t1_t2_mem0-1 <= c_t2_t1_t2

	c_t2_t1_t2_mem1 = S.Task('c_t2_t1_t2_mem1', length=1, delay_cost=1)
	c_t2_t1_t2_mem1 += INPUT_mem_r
	S += c_t2_t1_t2_mem1-1 <= c_t2_t1_t2

	c_t2_t1_t3_in = S.Task('c_t2_t1_t3_in', length=1, delay_cost=1)
	c_t2_t1_t3_in += alt(MAS_in)
	c_t2_t1_t3 = S.Task('c_t2_t1_t3', length=1, delay_cost=1)
	c_t2_t1_t3 += alt(MAS)

	S += c_t2_t1_t3>=c_t2_t1_t3_in

	c_t2_t1_t3_mem0 = S.Task('c_t2_t1_t3_mem0', length=1, delay_cost=1)
	c_t2_t1_t3_mem0 += INPUT_mem_r
	S += c_t2_t1_t3_mem0-1 <= c_t2_t1_t3

	c_t2_t1_t3_mem1 = S.Task('c_t2_t1_t3_mem1', length=1, delay_cost=1)
	c_t2_t1_t3_mem1 += INPUT_mem_r
	S += c_t2_t1_t3_mem1-1 <= c_t2_t1_t3

	c_t2_t20_in = S.Task('c_t2_t20_in', length=1, delay_cost=1)
	c_t2_t20_in += alt(MAS_in)
	c_t2_t20 = S.Task('c_t2_t20', length=1, delay_cost=1)
	c_t2_t20 += alt(MAS)

	S += c_t2_t20>=c_t2_t20_in

	c_t2_t20_mem0 = S.Task('c_t2_t20_mem0', length=1, delay_cost=1)
	c_t2_t20_mem0 += INPUT_mem_r
	S += c_t2_t20_mem0-1 <= c_t2_t20

	c_t2_t20_mem1 = S.Task('c_t2_t20_mem1', length=1, delay_cost=1)
	c_t2_t20_mem1 += INPUT_mem_r
	S += c_t2_t20_mem1-1 <= c_t2_t20

	c_t2_t21_in = S.Task('c_t2_t21_in', length=1, delay_cost=1)
	c_t2_t21_in += alt(MAS_in)
	c_t2_t21 = S.Task('c_t2_t21', length=1, delay_cost=1)
	c_t2_t21 += alt(MAS)

	S += c_t2_t21>=c_t2_t21_in

	c_t2_t21_mem0 = S.Task('c_t2_t21_mem0', length=1, delay_cost=1)
	c_t2_t21_mem0 += INPUT_mem_r
	S += c_t2_t21_mem0-1 <= c_t2_t21

	c_t2_t21_mem1 = S.Task('c_t2_t21_mem1', length=1, delay_cost=1)
	c_t2_t21_mem1 += INPUT_mem_r
	S += c_t2_t21_mem1-1 <= c_t2_t21

	c_t2_t30_in = S.Task('c_t2_t30_in', length=1, delay_cost=1)
	c_t2_t30_in += alt(MAS_in)
	c_t2_t30 = S.Task('c_t2_t30', length=1, delay_cost=1)
	c_t2_t30 += alt(MAS)

	S += c_t2_t30>=c_t2_t30_in

	c_t2_t30_mem0 = S.Task('c_t2_t30_mem0', length=1, delay_cost=1)
	c_t2_t30_mem0 += INPUT_mem_r
	S += c_t2_t30_mem0-1 <= c_t2_t30

	c_t2_t30_mem1 = S.Task('c_t2_t30_mem1', length=1, delay_cost=1)
	c_t2_t30_mem1 += INPUT_mem_r
	S += c_t2_t30_mem1-1 <= c_t2_t30

	c_t2_t31_in = S.Task('c_t2_t31_in', length=1, delay_cost=1)
	c_t2_t31_in += alt(MAS_in)
	c_t2_t31 = S.Task('c_t2_t31', length=1, delay_cost=1)
	c_t2_t31 += alt(MAS)

	S += c_t2_t31>=c_t2_t31_in

	c_t2_t31_mem0 = S.Task('c_t2_t31_mem0', length=1, delay_cost=1)
	c_t2_t31_mem0 += INPUT_mem_r
	S += c_t2_t31_mem0-1 <= c_t2_t31

	c_t2_t31_mem1 = S.Task('c_t2_t31_mem1', length=1, delay_cost=1)
	c_t2_t31_mem1 += INPUT_mem_r
	S += c_t2_t31_mem1-1 <= c_t2_t31

	c_t3000_in = S.Task('c_t3000_in', length=1, delay_cost=1)
	c_t3000_in += alt(MAS_in)
	c_t3000 = S.Task('c_t3000', length=1, delay_cost=1)
	c_t3000 += alt(MAS)

	S += c_t3000>=c_t3000_in

	c_t3000_mem0 = S.Task('c_t3000_mem0', length=1, delay_cost=1)
	c_t3000_mem0 += INPUT_mem_r
	S += c_t3000_mem0-1 <= c_t3000

	c_t3000_mem1 = S.Task('c_t3000_mem1', length=1, delay_cost=1)
	c_t3000_mem1 += INPUT_mem_r
	S += c_t3000_mem1-1 <= c_t3000

	c_t3001_in = S.Task('c_t3001_in', length=1, delay_cost=1)
	c_t3001_in += alt(MAS_in)
	c_t3001 = S.Task('c_t3001', length=1, delay_cost=1)
	c_t3001 += alt(MAS)

	S += c_t3001>=c_t3001_in

	c_t3001_mem0 = S.Task('c_t3001_mem0', length=1, delay_cost=1)
	c_t3001_mem0 += INPUT_mem_r
	S += c_t3001_mem0-1 <= c_t3001

	c_t3001_mem1 = S.Task('c_t3001_mem1', length=1, delay_cost=1)
	c_t3001_mem1 += INPUT_mem_r
	S += c_t3001_mem1-1 <= c_t3001

	c_t3010_in = S.Task('c_t3010_in', length=1, delay_cost=1)
	c_t3010_in += alt(MAS_in)
	c_t3010 = S.Task('c_t3010', length=1, delay_cost=1)
	c_t3010 += alt(MAS)

	S += c_t3010>=c_t3010_in

	c_t3010_mem0 = S.Task('c_t3010_mem0', length=1, delay_cost=1)
	c_t3010_mem0 += INPUT_mem_r
	S += c_t3010_mem0-1 <= c_t3010

	c_t3010_mem1 = S.Task('c_t3010_mem1', length=1, delay_cost=1)
	c_t3010_mem1 += INPUT_mem_r
	S += c_t3010_mem1-1 <= c_t3010

	c_t3011_in = S.Task('c_t3011_in', length=1, delay_cost=1)
	c_t3011_in += alt(MAS_in)
	c_t3011 = S.Task('c_t3011', length=1, delay_cost=1)
	c_t3011 += alt(MAS)

	S += c_t3011>=c_t3011_in

	c_t3011_mem0 = S.Task('c_t3011_mem0', length=1, delay_cost=1)
	c_t3011_mem0 += INPUT_mem_r
	S += c_t3011_mem0-1 <= c_t3011

	c_t3011_mem1 = S.Task('c_t3011_mem1', length=1, delay_cost=1)
	c_t3011_mem1 += INPUT_mem_r
	S += c_t3011_mem1-1 <= c_t3011

	c_t3100_in = S.Task('c_t3100_in', length=1, delay_cost=1)
	c_t3100_in += alt(MAS_in)
	c_t3100 = S.Task('c_t3100', length=1, delay_cost=1)
	c_t3100 += alt(MAS)

	S += c_t3100>=c_t3100_in

	c_t3100_mem0 = S.Task('c_t3100_mem0', length=1, delay_cost=1)
	c_t3100_mem0 += INPUT_mem_r
	S += c_t3100_mem0-1 <= c_t3100

	c_t3100_mem1 = S.Task('c_t3100_mem1', length=1, delay_cost=1)
	c_t3100_mem1 += INPUT_mem_r
	S += c_t3100_mem1-1 <= c_t3100

	c_t3101_in = S.Task('c_t3101_in', length=1, delay_cost=1)
	c_t3101_in += alt(MAS_in)
	c_t3101 = S.Task('c_t3101', length=1, delay_cost=1)
	c_t3101 += alt(MAS)

	S += c_t3101>=c_t3101_in

	c_t3101_mem0 = S.Task('c_t3101_mem0', length=1, delay_cost=1)
	c_t3101_mem0 += INPUT_mem_r
	S += c_t3101_mem0-1 <= c_t3101

	c_t3101_mem1 = S.Task('c_t3101_mem1', length=1, delay_cost=1)
	c_t3101_mem1 += INPUT_mem_r
	S += c_t3101_mem1-1 <= c_t3101

	c_t3110_in = S.Task('c_t3110_in', length=1, delay_cost=1)
	c_t3110_in += alt(MAS_in)
	c_t3110 = S.Task('c_t3110', length=1, delay_cost=1)
	c_t3110 += alt(MAS)

	S += c_t3110>=c_t3110_in

	c_t3110_mem0 = S.Task('c_t3110_mem0', length=1, delay_cost=1)
	c_t3110_mem0 += INPUT_mem_r
	S += c_t3110_mem0-1 <= c_t3110

	c_t3110_mem1 = S.Task('c_t3110_mem1', length=1, delay_cost=1)
	c_t3110_mem1 += INPUT_mem_r
	S += c_t3110_mem1-1 <= c_t3110

	c_t3111_in = S.Task('c_t3111_in', length=1, delay_cost=1)
	c_t3111_in += alt(MAS_in)
	c_t3111 = S.Task('c_t3111', length=1, delay_cost=1)
	c_t3111 += alt(MAS)

	S += c_t3111>=c_t3111_in

	c_t3111_mem0 = S.Task('c_t3111_mem0', length=1, delay_cost=1)
	c_t3111_mem0 += INPUT_mem_r
	S += c_t3111_mem0-1 <= c_t3111

	c_t3111_mem1 = S.Task('c_t3111_mem1', length=1, delay_cost=1)
	c_t3111_mem1 += INPUT_mem_r
	S += c_t3111_mem1-1 <= c_t3111

	c_t4000_in = S.Task('c_t4000_in', length=1, delay_cost=1)
	c_t4000_in += alt(MAS_in)
	c_t4000 = S.Task('c_t4000', length=1, delay_cost=1)
	c_t4000 += alt(MAS)

	S += c_t4000>=c_t4000_in

	c_t4000_mem0 = S.Task('c_t4000_mem0', length=1, delay_cost=1)
	c_t4000_mem0 += INPUT_mem_r
	S += c_t4000_mem0-1 <= c_t4000

	c_t4000_mem1 = S.Task('c_t4000_mem1', length=1, delay_cost=1)
	c_t4000_mem1 += INPUT_mem_r
	S += c_t4000_mem1-1 <= c_t4000

	c_t4001_in = S.Task('c_t4001_in', length=1, delay_cost=1)
	c_t4001_in += alt(MAS_in)
	c_t4001 = S.Task('c_t4001', length=1, delay_cost=1)
	c_t4001 += alt(MAS)

	S += c_t4001>=c_t4001_in

	c_t4001_mem0 = S.Task('c_t4001_mem0', length=1, delay_cost=1)
	c_t4001_mem0 += INPUT_mem_r
	S += c_t4001_mem0-1 <= c_t4001

	c_t4001_mem1 = S.Task('c_t4001_mem1', length=1, delay_cost=1)
	c_t4001_mem1 += INPUT_mem_r
	S += c_t4001_mem1-1 <= c_t4001

	c_t4010_in = S.Task('c_t4010_in', length=1, delay_cost=1)
	c_t4010_in += alt(MAS_in)
	c_t4010 = S.Task('c_t4010', length=1, delay_cost=1)
	c_t4010 += alt(MAS)

	S += c_t4010>=c_t4010_in

	c_t4010_mem0 = S.Task('c_t4010_mem0', length=1, delay_cost=1)
	c_t4010_mem0 += INPUT_mem_r
	S += c_t4010_mem0-1 <= c_t4010

	c_t4010_mem1 = S.Task('c_t4010_mem1', length=1, delay_cost=1)
	c_t4010_mem1 += INPUT_mem_r
	S += c_t4010_mem1-1 <= c_t4010

	c_t4011_in = S.Task('c_t4011_in', length=1, delay_cost=1)
	c_t4011_in += alt(MAS_in)
	c_t4011 = S.Task('c_t4011', length=1, delay_cost=1)
	c_t4011 += alt(MAS)

	S += c_t4011>=c_t4011_in

	c_t4011_mem0 = S.Task('c_t4011_mem0', length=1, delay_cost=1)
	c_t4011_mem0 += INPUT_mem_r
	S += c_t4011_mem0-1 <= c_t4011

	c_t4011_mem1 = S.Task('c_t4011_mem1', length=1, delay_cost=1)
	c_t4011_mem1 += INPUT_mem_r
	S += c_t4011_mem1-1 <= c_t4011

	c_t4100_in = S.Task('c_t4100_in', length=1, delay_cost=1)
	c_t4100_in += alt(MAS_in)
	c_t4100 = S.Task('c_t4100', length=1, delay_cost=1)
	c_t4100 += alt(MAS)

	S += c_t4100>=c_t4100_in

	c_t4100_mem0 = S.Task('c_t4100_mem0', length=1, delay_cost=1)
	c_t4100_mem0 += INPUT_mem_r
	S += c_t4100_mem0-1 <= c_t4100

	c_t4100_mem1 = S.Task('c_t4100_mem1', length=1, delay_cost=1)
	c_t4100_mem1 += INPUT_mem_r
	S += c_t4100_mem1-1 <= c_t4100

	c_t4101_in = S.Task('c_t4101_in', length=1, delay_cost=1)
	c_t4101_in += alt(MAS_in)
	c_t4101 = S.Task('c_t4101', length=1, delay_cost=1)
	c_t4101 += alt(MAS)

	S += c_t4101>=c_t4101_in

	c_t4101_mem0 = S.Task('c_t4101_mem0', length=1, delay_cost=1)
	c_t4101_mem0 += INPUT_mem_r
	S += c_t4101_mem0-1 <= c_t4101

	c_t4101_mem1 = S.Task('c_t4101_mem1', length=1, delay_cost=1)
	c_t4101_mem1 += INPUT_mem_r
	S += c_t4101_mem1-1 <= c_t4101

	c_t4110_in = S.Task('c_t4110_in', length=1, delay_cost=1)
	c_t4110_in += alt(MAS_in)
	c_t4110 = S.Task('c_t4110', length=1, delay_cost=1)
	c_t4110 += alt(MAS)

	S += c_t4110>=c_t4110_in

	c_t4110_mem0 = S.Task('c_t4110_mem0', length=1, delay_cost=1)
	c_t4110_mem0 += INPUT_mem_r
	S += c_t4110_mem0-1 <= c_t4110

	c_t4110_mem1 = S.Task('c_t4110_mem1', length=1, delay_cost=1)
	c_t4110_mem1 += INPUT_mem_r
	S += c_t4110_mem1-1 <= c_t4110

	c_t4111_in = S.Task('c_t4111_in', length=1, delay_cost=1)
	c_t4111_in += alt(MAS_in)
	c_t4111 = S.Task('c_t4111', length=1, delay_cost=1)
	c_t4111 += alt(MAS)

	S += c_t4111>=c_t4111_in

	c_t4111_mem0 = S.Task('c_t4111_mem0', length=1, delay_cost=1)
	c_t4111_mem0 += INPUT_mem_r
	S += c_t4111_mem0-1 <= c_t4111

	c_t4111_mem1 = S.Task('c_t4111_mem1', length=1, delay_cost=1)
	c_t4111_mem1 += INPUT_mem_r
	S += c_t4111_mem1-1 <= c_t4111

	c_t5000_in = S.Task('c_t5000_in', length=1, delay_cost=1)
	c_t5000_in += alt(MAS_in)
	c_t5000 = S.Task('c_t5000', length=1, delay_cost=1)
	c_t5000 += alt(MAS)

	S += c_t5000>=c_t5000_in

	c_t5000_mem0 = S.Task('c_t5000_mem0', length=1, delay_cost=1)
	c_t5000_mem0 += INPUT_mem_r
	S += c_t5000_mem0-1 <= c_t5000

	c_t5000_mem1 = S.Task('c_t5000_mem1', length=1, delay_cost=1)
	c_t5000_mem1 += INPUT_mem_r
	S += c_t5000_mem1-1 <= c_t5000

	c_t5001_in = S.Task('c_t5001_in', length=1, delay_cost=1)
	c_t5001_in += alt(MAS_in)
	c_t5001 = S.Task('c_t5001', length=1, delay_cost=1)
	c_t5001 += alt(MAS)

	S += c_t5001>=c_t5001_in

	c_t5001_mem0 = S.Task('c_t5001_mem0', length=1, delay_cost=1)
	c_t5001_mem0 += INPUT_mem_r
	S += c_t5001_mem0-1 <= c_t5001

	c_t5001_mem1 = S.Task('c_t5001_mem1', length=1, delay_cost=1)
	c_t5001_mem1 += INPUT_mem_r
	S += c_t5001_mem1-1 <= c_t5001

	c_t5010_in = S.Task('c_t5010_in', length=1, delay_cost=1)
	c_t5010_in += alt(MAS_in)
	c_t5010 = S.Task('c_t5010', length=1, delay_cost=1)
	c_t5010 += alt(MAS)

	S += c_t5010>=c_t5010_in

	c_t5010_mem0 = S.Task('c_t5010_mem0', length=1, delay_cost=1)
	c_t5010_mem0 += INPUT_mem_r
	S += c_t5010_mem0-1 <= c_t5010

	c_t5010_mem1 = S.Task('c_t5010_mem1', length=1, delay_cost=1)
	c_t5010_mem1 += INPUT_mem_r
	S += c_t5010_mem1-1 <= c_t5010

	c_t5011_in = S.Task('c_t5011_in', length=1, delay_cost=1)
	c_t5011_in += alt(MAS_in)
	c_t5011 = S.Task('c_t5011', length=1, delay_cost=1)
	c_t5011 += alt(MAS)

	S += c_t5011>=c_t5011_in

	c_t5011_mem0 = S.Task('c_t5011_mem0', length=1, delay_cost=1)
	c_t5011_mem0 += INPUT_mem_r
	S += c_t5011_mem0-1 <= c_t5011

	c_t5011_mem1 = S.Task('c_t5011_mem1', length=1, delay_cost=1)
	c_t5011_mem1 += INPUT_mem_r
	S += c_t5011_mem1-1 <= c_t5011

	c_t5100_in = S.Task('c_t5100_in', length=1, delay_cost=1)
	c_t5100_in += alt(MAS_in)
	c_t5100 = S.Task('c_t5100', length=1, delay_cost=1)
	c_t5100 += alt(MAS)

	S += c_t5100>=c_t5100_in

	c_t5100_mem0 = S.Task('c_t5100_mem0', length=1, delay_cost=1)
	c_t5100_mem0 += INPUT_mem_r
	S += c_t5100_mem0-1 <= c_t5100

	c_t5100_mem1 = S.Task('c_t5100_mem1', length=1, delay_cost=1)
	c_t5100_mem1 += INPUT_mem_r
	S += c_t5100_mem1-1 <= c_t5100

	c_t5101_in = S.Task('c_t5101_in', length=1, delay_cost=1)
	c_t5101_in += alt(MAS_in)
	c_t5101 = S.Task('c_t5101', length=1, delay_cost=1)
	c_t5101 += alt(MAS)

	S += c_t5101>=c_t5101_in

	c_t5101_mem0 = S.Task('c_t5101_mem0', length=1, delay_cost=1)
	c_t5101_mem0 += INPUT_mem_r
	S += c_t5101_mem0-1 <= c_t5101

	c_t5101_mem1 = S.Task('c_t5101_mem1', length=1, delay_cost=1)
	c_t5101_mem1 += INPUT_mem_r
	S += c_t5101_mem1-1 <= c_t5101

	c_t5110_in = S.Task('c_t5110_in', length=1, delay_cost=1)
	c_t5110_in += alt(MAS_in)
	c_t5110 = S.Task('c_t5110', length=1, delay_cost=1)
	c_t5110 += alt(MAS)

	S += c_t5110>=c_t5110_in

	c_t5110_mem0 = S.Task('c_t5110_mem0', length=1, delay_cost=1)
	c_t5110_mem0 += INPUT_mem_r
	S += c_t5110_mem0-1 <= c_t5110

	c_t5110_mem1 = S.Task('c_t5110_mem1', length=1, delay_cost=1)
	c_t5110_mem1 += INPUT_mem_r
	S += c_t5110_mem1-1 <= c_t5110

	c_t5111_in = S.Task('c_t5111_in', length=1, delay_cost=1)
	c_t5111_in += alt(MAS_in)
	c_t5111 = S.Task('c_t5111', length=1, delay_cost=1)
	c_t5111 += alt(MAS)

	S += c_t5111>=c_t5111_in

	c_t5111_mem0 = S.Task('c_t5111_mem0', length=1, delay_cost=1)
	c_t5111_mem0 += INPUT_mem_r
	S += c_t5111_mem0-1 <= c_t5111

	c_t5111_mem1 = S.Task('c_t5111_mem1', length=1, delay_cost=1)
	c_t5111_mem1 += INPUT_mem_r
	S += c_t5111_mem1-1 <= c_t5111

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/python/scheduling/result/MUL_mul1_4_add1_1/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

