from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 116
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=8)
	MM_in = S.Resources('MM_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=5, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=10)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	S += c001_mem0 >= 0
	c001_mem0 += MAIN_MEM_r[0]

	c20_t3_mem1 = S.Task('c20_t3_mem1', length=1, delay_cost=1)
	S += c20_t3_mem1 >= 0
	c20_t3_mem1 += MAIN_MEM_r[1]

	c21_t0_in = S.Task('c21_t0_in', length=1, delay_cost=1)
	S += c21_t0_in >= 0
	c21_t0_in += MM_in[0]

	c001 = S.Task('c001', length=1, delay_cost=1)
	S += c001 >= 1
	c001 += MAS[4]

	c01_t2_mem0 = S.Task('c01_t2_mem0', length=1, delay_cost=1)
	S += c01_t2_mem0 >= 1
	c01_t2_mem0 += MAIN_MEM_r[0]

	c10_t3 = S.Task('c10_t3', length=1, delay_cost=1)
	S += c10_t3 >= 1
	c10_t3 += MAS[0]

	c20_t0_in = S.Task('c20_t0_in', length=1, delay_cost=1)
	S += c20_t0_in >= 1
	c20_t0_in += MM_in[0]

	c20_t2 = S.Task('c20_t2', length=1, delay_cost=1)
	S += c20_t2 >= 1
	c20_t2 += MAS[3]

	c20_t3 = S.Task('c20_t3', length=1, delay_cost=1)
	S += c20_t3 >= 1
	c20_t3 += MAS[1]

	c21_t0 = S.Task('c21_t0', length=8, delay_cost=1)
	S += c21_t0 >= 1
	c21_t0 += MM[0]

	c21_t2_mem1 = S.Task('c21_t2_mem1', length=1, delay_cost=1)
	S += c21_t2_mem1 >= 1
	c21_t2_mem1 += MAIN_MEM_r[1]

	c21_t3 = S.Task('c21_t3', length=1, delay_cost=1)
	S += c21_t3 >= 1
	c21_t3 += MAS[2]

	c000 = S.Task('c000', length=1, delay_cost=1)
	S += c000 >= 2
	c000 += MAS[1]

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	S += c000_mem0 >= 2
	c000_mem0 += MAIN_MEM_r[0]

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	S += c001_w >= 2
	c001_w += MAIN_MEM_w

	c01_t2 = S.Task('c01_t2', length=1, delay_cost=1)
	S += c01_t2 >= 2
	c01_t2 += MAS[4]

	c01_t3 = S.Task('c01_t3', length=1, delay_cost=1)
	S += c01_t3 >= 2
	c01_t3 += MAS[3]

	c11_t0_in = S.Task('c11_t0_in', length=1, delay_cost=1)
	S += c11_t0_in >= 2
	c11_t0_in += MM_in[0]

	c11_t3 = S.Task('c11_t3', length=1, delay_cost=1)
	S += c11_t3 >= 2
	c11_t3 += MAS[0]

	c20_t0 = S.Task('c20_t0', length=8, delay_cost=1)
	S += c20_t0 >= 2
	c20_t0 += MM[0]

	c21_t0_mem1 = S.Task('c21_t0_mem1', length=1, delay_cost=1)
	S += c21_t0_mem1 >= 2
	c21_t0_mem1 += MAIN_MEM_r[1]

	c21_t2 = S.Task('c21_t2', length=1, delay_cost=1)
	S += c21_t2 >= 2
	c21_t2 += MAS[2]

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	S += c000_w >= 3
	c000_w += MAIN_MEM_w

	c01_t0_mem0 = S.Task('c01_t0_mem0', length=1, delay_cost=1)
	S += c01_t0_mem0 >= 3
	c01_t0_mem0 += MAIN_MEM_r[0]

	c01_t0_mem1 = S.Task('c01_t0_mem1', length=1, delay_cost=1)
	S += c01_t0_mem1 >= 3
	c01_t0_mem1 += MAIN_MEM_r[1]

	c10_t1_in = S.Task('c10_t1_in', length=1, delay_cost=1)
	S += c10_t1_in >= 3
	c10_t1_in += MM_in[0]

	c10_t2 = S.Task('c10_t2', length=1, delay_cost=1)
	S += c10_t2 >= 3
	c10_t2 += MAS[2]

	c11_t0 = S.Task('c11_t0', length=8, delay_cost=1)
	S += c11_t0 >= 3
	c11_t0 += MM[0]

	c11_t2 = S.Task('c11_t2', length=1, delay_cost=1)
	S += c11_t2 >= 3
	c11_t2 += MAS[1]

	c01_t0_in = S.Task('c01_t0_in', length=1, delay_cost=1)
	S += c01_t0_in >= 4
	c01_t0_in += MM_in[0]

	c01_t3_mem1 = S.Task('c01_t3_mem1', length=1, delay_cost=1)
	S += c01_t3_mem1 >= 4
	c01_t3_mem1 += MAIN_MEM_r[1]

	c10_t1 = S.Task('c10_t1', length=8, delay_cost=1)
	S += c10_t1 >= 4
	c10_t1 += MM[0]

	c21_t1_mem0 = S.Task('c21_t1_mem0', length=1, delay_cost=1)
	S += c21_t1_mem0 >= 4
	c21_t1_mem0 += MAIN_MEM_r[0]

	c01_t0 = S.Task('c01_t0', length=8, delay_cost=1)
	S += c01_t0 >= 5
	c01_t0 += MM[0]

	c11_t1_in = S.Task('c11_t1_in', length=1, delay_cost=1)
	S += c11_t1_in >= 5
	c11_t1_in += MM_in[0]

	c11_t1_mem1 = S.Task('c11_t1_mem1', length=1, delay_cost=1)
	S += c11_t1_mem1 >= 5
	c11_t1_mem1 += MAIN_MEM_r[1]

	c20_t3_mem0 = S.Task('c20_t3_mem0', length=1, delay_cost=1)
	S += c20_t3_mem0 >= 5
	c20_t3_mem0 += MAIN_MEM_r[0]

	c01_t1_in = S.Task('c01_t1_in', length=1, delay_cost=1)
	S += c01_t1_in >= 6
	c01_t1_in += MM_in[0]

	c11_t1 = S.Task('c11_t1', length=8, delay_cost=1)
	S += c11_t1 >= 6
	c11_t1 += MM[0]

	c11_t3_mem0 = S.Task('c11_t3_mem0', length=1, delay_cost=1)
	S += c11_t3_mem0 >= 6
	c11_t3_mem0 += MAIN_MEM_r[0]

	c20_t1_mem1 = S.Task('c20_t1_mem1', length=1, delay_cost=1)
	S += c20_t1_mem1 >= 6
	c20_t1_mem1 += MAIN_MEM_r[1]

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	S += c000_mem1 >= 7
	c000_mem1 += MAIN_MEM_r[1]

	c01_t1 = S.Task('c01_t1', length=8, delay_cost=1)
	S += c01_t1 >= 7
	c01_t1 += MM[0]

	c10_t0_in = S.Task('c10_t0_in', length=1, delay_cost=1)
	S += c10_t0_in >= 7
	c10_t0_in += MM_in[0]

	c20_t1_mem0 = S.Task('c20_t1_mem0', length=1, delay_cost=1)
	S += c20_t1_mem0 >= 7
	c20_t1_mem0 += MAIN_MEM_r[0]

	c01_t2_mem1 = S.Task('c01_t2_mem1', length=1, delay_cost=1)
	S += c01_t2_mem1 >= 8
	c01_t2_mem1 += MAIN_MEM_r[1]

	c10_t0 = S.Task('c10_t0', length=8, delay_cost=1)
	S += c10_t0 >= 8
	c10_t0 += MM[0]

	c21_t1_in = S.Task('c21_t1_in', length=1, delay_cost=1)
	S += c21_t1_in >= 8
	c21_t1_in += MM_in[0]

	c21_t2_mem0 = S.Task('c21_t2_mem0', length=1, delay_cost=1)
	S += c21_t2_mem0 >= 8
	c21_t2_mem0 += MAIN_MEM_r[0]

	c11_t2_mem0 = S.Task('c11_t2_mem0', length=1, delay_cost=1)
	S += c11_t2_mem0 >= 9
	c11_t2_mem0 += MAIN_MEM_r[0]

	c11_t3_mem1 = S.Task('c11_t3_mem1', length=1, delay_cost=1)
	S += c11_t3_mem1 >= 9
	c11_t3_mem1 += MAIN_MEM_r[1]

	c20_t1_in = S.Task('c20_t1_in', length=1, delay_cost=1)
	S += c20_t1_in >= 9
	c20_t1_in += MM_in[0]

	c21_t1 = S.Task('c21_t1', length=8, delay_cost=1)
	S += c21_t1 >= 9
	c21_t1 += MM[0]

	c20_t0_mem0 = S.Task('c20_t0_mem0', length=1, delay_cost=1)
	S += c20_t0_mem0 >= 10
	c20_t0_mem0 += MAIN_MEM_r[0]

	c20_t0_mem1 = S.Task('c20_t0_mem1', length=1, delay_cost=1)
	S += c20_t0_mem1 >= 10
	c20_t0_mem1 += MAIN_MEM_r[1]

	c20_t1 = S.Task('c20_t1', length=8, delay_cost=1)
	S += c20_t1 >= 10
	c20_t1 += MM[0]

	c21_t4_in = S.Task('c21_t4_in', length=1, delay_cost=1)
	S += c21_t4_in >= 10
	c21_t4_in += MM_in[0]

	c21_t4_mem0 = S.Task('c21_t4_mem0', length=1, delay_cost=1)
	S += c21_t4_mem0 >= 10
	c21_t4_mem0 += MAS_MEM[4]

	c21_t4_mem1 = S.Task('c21_t4_mem1', length=1, delay_cost=1)
	S += c21_t4_mem1 >= 10
	c21_t4_mem1 += MAS_MEM[5]

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	S += c001_mem1 >= 11
	c001_mem1 += MAIN_MEM_r[1]

	c01_t3_mem0 = S.Task('c01_t3_mem0', length=1, delay_cost=1)
	S += c01_t3_mem0 >= 11
	c01_t3_mem0 += MAIN_MEM_r[0]

	c20_t4_in = S.Task('c20_t4_in', length=1, delay_cost=1)
	S += c20_t4_in >= 11
	c20_t4_in += MM_in[0]

	c20_t4_mem0 = S.Task('c20_t4_mem0', length=1, delay_cost=1)
	S += c20_t4_mem0 >= 11
	c20_t4_mem0 += MAS_MEM[6]

	c20_t4_mem1 = S.Task('c20_t4_mem1', length=1, delay_cost=1)
	S += c20_t4_mem1 >= 11
	c20_t4_mem1 += MAS_MEM[3]

	c21_t4 = S.Task('c21_t4', length=8, delay_cost=1)
	S += c21_t4 >= 11
	c21_t4 += MM[0]

	c01_t1_mem0 = S.Task('c01_t1_mem0', length=1, delay_cost=1)
	S += c01_t1_mem0 >= 12
	c01_t1_mem0 += MAIN_MEM_r[0]

	c01_t1_mem1 = S.Task('c01_t1_mem1', length=1, delay_cost=1)
	S += c01_t1_mem1 >= 12
	c01_t1_mem1 += MAIN_MEM_r[1]

	c01_t4_in = S.Task('c01_t4_in', length=1, delay_cost=1)
	S += c01_t4_in >= 12
	c01_t4_in += MM_in[0]

	c01_t4_mem0 = S.Task('c01_t4_mem0', length=1, delay_cost=1)
	S += c01_t4_mem0 >= 12
	c01_t4_mem0 += MAS_MEM[8]

	c01_t4_mem1 = S.Task('c01_t4_mem1', length=1, delay_cost=1)
	S += c01_t4_mem1 >= 12
	c01_t4_mem1 += MAS_MEM[7]

	c20_t4 = S.Task('c20_t4', length=8, delay_cost=1)
	S += c20_t4 >= 12
	c20_t4 += MM[0]

	c01_t4 = S.Task('c01_t4', length=8, delay_cost=1)
	S += c01_t4 >= 13
	c01_t4 += MM[0]

	c10_t4_in = S.Task('c10_t4_in', length=1, delay_cost=1)
	S += c10_t4_in >= 13
	c10_t4_in += MM_in[0]

	c10_t4_mem0 = S.Task('c10_t4_mem0', length=1, delay_cost=1)
	S += c10_t4_mem0 >= 13
	c10_t4_mem0 += MAS_MEM[4]

	c10_t4_mem1 = S.Task('c10_t4_mem1', length=1, delay_cost=1)
	S += c10_t4_mem1 >= 13
	c10_t4_mem1 += MAS_MEM[1]

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	S += c110_mem0 >= 13
	c110_mem0 += MM_MEM[0]

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	S += c110_mem1 >= 13
	c110_mem1 += MM_MEM[1]

	c20_t2_mem0 = S.Task('c20_t2_mem0', length=1, delay_cost=1)
	S += c20_t2_mem0 >= 13
	c20_t2_mem0 += MAIN_MEM_r[0]

	c21_t1_mem1 = S.Task('c21_t1_mem1', length=1, delay_cost=1)
	S += c21_t1_mem1 >= 13
	c21_t1_mem1 += MAIN_MEM_r[1]

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	S += c010_mem0 >= 14
	c010_mem0 += MM_MEM[0]

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	S += c010_mem1 >= 14
	c010_mem1 += MM_MEM[1]

	c10_t0_mem1 = S.Task('c10_t0_mem1', length=1, delay_cost=1)
	S += c10_t0_mem1 >= 14
	c10_t0_mem1 += MAIN_MEM_r[1]

	c10_t4 = S.Task('c10_t4', length=8, delay_cost=1)
	S += c10_t4 >= 14
	c10_t4 += MM[0]

	c110 = S.Task('c110', length=1, delay_cost=1)
	S += c110 >= 14
	c110 += MAS[4]

	c11_t4_in = S.Task('c11_t4_in', length=1, delay_cost=1)
	S += c11_t4_in >= 14
	c11_t4_in += MM_in[0]

	c11_t4_mem0 = S.Task('c11_t4_mem0', length=1, delay_cost=1)
	S += c11_t4_mem0 >= 14
	c11_t4_mem0 += MAS_MEM[2]

	c11_t4_mem1 = S.Task('c11_t4_mem1', length=1, delay_cost=1)
	S += c11_t4_mem1 >= 14
	c11_t4_mem1 += MAS_MEM[1]

	c21_t0_mem0 = S.Task('c21_t0_mem0', length=1, delay_cost=1)
	S += c21_t0_mem0 >= 14
	c21_t0_mem0 += MAIN_MEM_r[0]

	c010 = S.Task('c010', length=1, delay_cost=1)
	S += c010 >= 15
	c010 += MAS[0]

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	S += c100_mem0 >= 15
	c100_mem0 += MM_MEM[0]

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	S += c100_mem1 >= 15
	c100_mem1 += MM_MEM[1]

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	S += c110_w >= 15
	c110_w += MAIN_MEM_w

	c11_t4 = S.Task('c11_t4', length=8, delay_cost=1)
	S += c11_t4 >= 15
	c11_t4 += MM[0]

	c20_t2_mem1 = S.Task('c20_t2_mem1', length=1, delay_cost=1)
	S += c20_t2_mem1 >= 15
	c20_t2_mem1 += MAIN_MEM_r[1]

	c21_t3_mem0 = S.Task('c21_t3_mem0', length=1, delay_cost=1)
	S += c21_t3_mem0 >= 15
	c21_t3_mem0 += MAIN_MEM_r[0]

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	S += c010_w >= 16
	c010_w += MAIN_MEM_w

	c100 = S.Task('c100', length=1, delay_cost=1)
	S += c100 >= 16
	c100 += MAS[3]

	c11_t1_mem0 = S.Task('c11_t1_mem0', length=1, delay_cost=1)
	S += c11_t1_mem0 >= 16
	c11_t1_mem0 += MAIN_MEM_r[0]

	c11_t2_mem1 = S.Task('c11_t2_mem1', length=1, delay_cost=1)
	S += c11_t2_mem1 >= 16
	c11_t2_mem1 += MAIN_MEM_r[1]

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	S += c210_mem0 >= 16
	c210_mem0 += MM_MEM[0]

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	S += c210_mem1 >= 16
	c210_mem1 += MM_MEM[1]

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	S += c100_w >= 17
	c100_w += MAIN_MEM_w

	c10_t3_mem0 = S.Task('c10_t3_mem0', length=1, delay_cost=1)
	S += c10_t3_mem0 >= 17
	c10_t3_mem0 += MAIN_MEM_r[0]

	c11_t0_mem1 = S.Task('c11_t0_mem1', length=1, delay_cost=1)
	S += c11_t0_mem1 >= 17
	c11_t0_mem1 += MAIN_MEM_r[1]

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	S += c200_mem0 >= 17
	c200_mem0 += MM_MEM[0]

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	S += c200_mem1 >= 17
	c200_mem1 += MM_MEM[1]

	c210 = S.Task('c210', length=1, delay_cost=1)
	S += c210 >= 17
	c210 += MAS[4]

	c11_t0_mem0 = S.Task('c11_t0_mem0', length=1, delay_cost=1)
	S += c11_t0_mem0 >= 18
	c11_t0_mem0 += MAIN_MEM_r[0]

	c200 = S.Task('c200', length=1, delay_cost=1)
	S += c200 >= 18
	c200 += MAS[2]

	c20_t5_mem0 = S.Task('c20_t5_mem0', length=1, delay_cost=1)
	S += c20_t5_mem0 >= 18
	c20_t5_mem0 += MM_MEM[0]

	c20_t5_mem1 = S.Task('c20_t5_mem1', length=1, delay_cost=1)
	S += c20_t5_mem1 >= 18
	c20_t5_mem1 += MM_MEM[1]

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	S += c210_w >= 18
	c210_w += MAIN_MEM_w

	c21_t3_mem1 = S.Task('c21_t3_mem1', length=1, delay_cost=1)
	S += c21_t3_mem1 >= 18
	c21_t3_mem1 += MAIN_MEM_r[1]

	c10_t0_mem0 = S.Task('c10_t0_mem0', length=1, delay_cost=1)
	S += c10_t0_mem0 >= 19
	c10_t0_mem0 += MAIN_MEM_r[0]

	c10_t3_mem1 = S.Task('c10_t3_mem1', length=1, delay_cost=1)
	S += c10_t3_mem1 >= 19
	c10_t3_mem1 += MAIN_MEM_r[1]

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	S += c200_w >= 19
	c200_w += MAIN_MEM_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	S += c201_mem0 >= 19
	c201_mem0 += MM_MEM[0]

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	S += c201_mem1 >= 19
	c201_mem1 += MAS_MEM[5]

	c20_t5 = S.Task('c20_t5', length=1, delay_cost=1)
	S += c20_t5 >= 19
	c20_t5 += MAS[2]

	c10_t2_mem0 = S.Task('c10_t2_mem0', length=1, delay_cost=1)
	S += c10_t2_mem0 >= 20
	c10_t2_mem0 += MAIN_MEM_r[0]

	c10_t2_mem1 = S.Task('c10_t2_mem1', length=1, delay_cost=1)
	S += c10_t2_mem1 >= 20
	c10_t2_mem1 += MAIN_MEM_r[1]

	c201 = S.Task('c201', length=1, delay_cost=1)
	S += c201 >= 20
	c201 += MAS[2]

	c21_t5_mem0 = S.Task('c21_t5_mem0', length=1, delay_cost=1)
	S += c21_t5_mem0 >= 20
	c21_t5_mem0 += MM_MEM[0]

	c21_t5_mem1 = S.Task('c21_t5_mem1', length=1, delay_cost=1)
	S += c21_t5_mem1 >= 20
	c21_t5_mem1 += MM_MEM[1]

	c10_t1_mem0 = S.Task('c10_t1_mem0', length=1, delay_cost=1)
	S += c10_t1_mem0 >= 21
	c10_t1_mem0 += MAIN_MEM_r[0]

	c10_t1_mem1 = S.Task('c10_t1_mem1', length=1, delay_cost=1)
	S += c10_t1_mem1 >= 21
	c10_t1_mem1 += MAIN_MEM_r[1]

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	S += c201_w >= 21
	c201_w += MAIN_MEM_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	S += c211_mem0 >= 21
	c211_mem0 += MM_MEM[0]

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	S += c211_mem1 >= 21
	c211_mem1 += MAS_MEM[3]

	c21_t5 = S.Task('c21_t5', length=1, delay_cost=1)
	S += c21_t5 >= 21
	c21_t5 += MAS[1]

	c11_t5_mem0 = S.Task('c11_t5_mem0', length=1, delay_cost=1)
	S += c11_t5_mem0 >= 22
	c11_t5_mem0 += MM_MEM[0]

	c11_t5_mem1 = S.Task('c11_t5_mem1', length=1, delay_cost=1)
	S += c11_t5_mem1 >= 22
	c11_t5_mem1 += MM_MEM[1]

	c211 = S.Task('c211', length=1, delay_cost=1)
	S += c211 >= 22
	c211 += MAS[2]

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	S += c111_mem0 >= 23
	c111_mem0 += MM_MEM[0]

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	S += c111_mem1 >= 23
	c111_mem1 += MAS_MEM[7]

	c11_t5 = S.Task('c11_t5', length=1, delay_cost=1)
	S += c11_t5 >= 23
	c11_t5 += MAS[3]

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	S += c211_w >= 23
	c211_w += MAIN_MEM_w

	c111 = S.Task('c111', length=1, delay_cost=1)
	S += c111 >= 24
	c111 += MAS[4]

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	S += c111_w >= 25
	c111_w += MAIN_MEM_w


	# new tasks
	c10_t5 = S.Task('c10_t5', length=1, delay_cost=1)
	c10_t5 += alt(MAS)

	S += c10_t5<1000

	c10_t5_mem0 = S.Task('c10_t5_mem0', length=1, delay_cost=1)
	c10_t5_mem0 += MM_MEM[0]
	S += 15 < c10_t5_mem0
	S += c10_t5_mem0 <= c10_t5

	c10_t5_mem1 = S.Task('c10_t5_mem1', length=1, delay_cost=1)
	c10_t5_mem1 += MM_MEM[1]
	S += 11 < c10_t5_mem1
	S += c10_t5_mem1 <= c10_t5

	c01_t5 = S.Task('c01_t5', length=1, delay_cost=1)
	c01_t5 += alt(MAS)

	S += c01_t5<1000

	c01_t5_mem0 = S.Task('c01_t5_mem0', length=1, delay_cost=1)
	c01_t5_mem0 += MM_MEM[0]
	S += 12 < c01_t5_mem0
	S += c01_t5_mem0 <= c01_t5

	c01_t5_mem1 = S.Task('c01_t5_mem1', length=1, delay_cost=1)
	c01_t5_mem1 += MM_MEM[1]
	S += 14 < c01_t5_mem1
	S += c01_t5_mem1 <= c01_t5

	c101 = S.Task('c101', length=1, delay_cost=1)
	c101 += alt(MAS)

	S += 4<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	S += c101<1000

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += MM_MEM[0]
	S += 21 < c101_mem0
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(MAS_MEM)
	S += (c10_t5*MAS[0])-1 < c101_mem1*MAS_MEM[1]
	S += (c10_t5*MAS[1])-1 < c101_mem1*MAS_MEM[3]
	S += (c10_t5*MAS[2])-1 < c101_mem1*MAS_MEM[5]
	S += (c10_t5*MAS[3])-1 < c101_mem1*MAS_MEM[7]
	S += (c10_t5*MAS[4])-1 < c101_mem1*MAS_MEM[9]
	S += c101_mem1 <= c101

	c011 = S.Task('c011', length=1, delay_cost=1)
	c011 += alt(MAS)

	S += 7<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	S += c011<1000

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += MM_MEM[0]
	S += 20 < c011_mem0
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(MAS_MEM)
	S += (c01_t5*MAS[0])-1 < c011_mem1*MAS_MEM[1]
	S += (c01_t5*MAS[1])-1 < c011_mem1*MAS_MEM[3]
	S += (c01_t5*MAS[2])-1 < c011_mem1*MAS_MEM[5]
	S += (c01_t5*MAS[3])-1 < c011_mem1*MAS_MEM[7]
	S += (c01_t5*MAS[4])-1 < c011_mem1*MAS_MEM[9]
	S += c011_mem1 <= c011

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM1_stage1MAS5/FROB/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

