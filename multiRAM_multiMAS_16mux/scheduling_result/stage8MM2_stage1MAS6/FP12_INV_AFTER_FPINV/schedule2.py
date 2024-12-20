from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 156
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=8)
	MM_in = S.Resources('MM_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=1, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_qinv_denom_inv1__in = S.Task('c_qinv_denom_inv1__in', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__in >= 0
	c_qinv_denom_inv1__in += MM_in[1]

	c_qinv_denom_inv1__mem0 = S.Task('c_qinv_denom_inv1__mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem0 >= 0
	c_qinv_denom_inv1__mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv1__mem1 = S.Task('c_qinv_denom_inv1__mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem1 >= 0
	c_qinv_denom_inv1__mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv0_in = S.Task('c_qinv_denom_inv0_in', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_in >= 1
	c_qinv_denom_inv0_in += MM_in[0]

	c_qinv_denom_inv0_mem0 = S.Task('c_qinv_denom_inv0_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem0 >= 1
	c_qinv_denom_inv0_mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv0_mem1 = S.Task('c_qinv_denom_inv0_mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem1 >= 1
	c_qinv_denom_inv0_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv1_ = S.Task('c_qinv_denom_inv1_', length=8, delay_cost=1)
	S += c_qinv_denom_inv1_ >= 1
	c_qinv_denom_inv1_ += MM[1]

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	S += c2_t21_mem0 >= 2
	c2_t21_mem0 += MAIN_MEM_r[0]

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	S += c2_t21_mem1 >= 2
	c2_t21_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv0 = S.Task('c_qinv_denom_inv0', length=8, delay_cost=1)
	S += c_qinv_denom_inv0 >= 2
	c_qinv_denom_inv0 += MM[0]

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	S += c2_t20_mem0 >= 3
	c2_t20_mem0 += MAIN_MEM_r[0]

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	S += c2_t20_mem1 >= 3
	c2_t20_mem1 += MAIN_MEM_r[1]

	c2_t21 = S.Task('c2_t21', length=1, delay_cost=1)
	S += c2_t21 >= 3
	c2_t21 += MAS[5]

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	S += c0_t21_mem0 >= 4
	c0_t21_mem0 += MAIN_MEM_r[0]

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	S += c0_t21_mem1 >= 4
	c0_t21_mem1 += MAIN_MEM_r[1]

	c2_t20 = S.Task('c2_t20', length=1, delay_cost=1)
	S += c2_t20 >= 4
	c2_t20 += MAS[1]

	c2_t4_t2_mem0 = S.Task('c2_t4_t2_mem0', length=1, delay_cost=1)
	S += c2_t4_t2_mem0 >= 4
	c2_t4_t2_mem0 += MAS_MEM[2]

	c2_t4_t2_mem1 = S.Task('c2_t4_t2_mem1', length=1, delay_cost=1)
	S += c2_t4_t2_mem1 >= 4
	c2_t4_t2_mem1 += MAS_MEM[11]

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	S += c0_t20_mem0 >= 5
	c0_t20_mem0 += MAIN_MEM_r[0]

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	S += c0_t20_mem1 >= 5
	c0_t20_mem1 += MAIN_MEM_r[1]

	c0_t21 = S.Task('c0_t21', length=1, delay_cost=1)
	S += c0_t21 >= 5
	c0_t21 += MAS[4]

	c2_t4_t2 = S.Task('c2_t4_t2', length=1, delay_cost=1)
	S += c2_t4_t2 >= 5
	c2_t4_t2 += MAS[2]

	c0_t20 = S.Task('c0_t20', length=1, delay_cost=1)
	S += c0_t20 >= 6
	c0_t20 += MAS[3]

	c0_t4_t2_mem0 = S.Task('c0_t4_t2_mem0', length=1, delay_cost=1)
	S += c0_t4_t2_mem0 >= 6
	c0_t4_t2_mem0 += MAS_MEM[6]

	c0_t4_t2_mem1 = S.Task('c0_t4_t2_mem1', length=1, delay_cost=1)
	S += c0_t4_t2_mem1 >= 6
	c0_t4_t2_mem1 += MAS_MEM[9]

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	S += c1_t21_mem0 >= 6
	c1_t21_mem0 += MAIN_MEM_r[0]

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	S += c1_t21_mem1 >= 6
	c1_t21_mem1 += MAIN_MEM_r[1]

	c0_t4_t2 = S.Task('c0_t4_t2', length=1, delay_cost=1)
	S += c0_t4_t2 >= 7
	c0_t4_t2 += MAS[0]

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	S += c1_t20_mem0 >= 7
	c1_t20_mem0 += MAIN_MEM_r[0]

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	S += c1_t20_mem1 >= 7
	c1_t20_mem1 += MAIN_MEM_r[1]

	c1_t21 = S.Task('c1_t21', length=1, delay_cost=1)
	S += c1_t21 >= 7
	c1_t21 += MAS[5]

	c1_t20 = S.Task('c1_t20', length=1, delay_cost=1)
	S += c1_t20 >= 8
	c1_t20 += MAS[0]

	c1_t4_t2_mem0 = S.Task('c1_t4_t2_mem0', length=1, delay_cost=1)
	S += c1_t4_t2_mem0 >= 8
	c1_t4_t2_mem0 += MAS_MEM[0]

	c1_t4_t2_mem1 = S.Task('c1_t4_t2_mem1', length=1, delay_cost=1)
	S += c1_t4_t2_mem1 >= 8
	c1_t4_t2_mem1 += MAS_MEM[11]

	c_qinv1__t1_in = S.Task('c_qinv1__t1_in', length=1, delay_cost=1)
	S += c_qinv1__t1_in >= 8
	c_qinv1__t1_in += MM_in[0]

	c_qinv1__t1_mem0 = S.Task('c_qinv1__t1_mem0', length=1, delay_cost=1)
	S += c_qinv1__t1_mem0 >= 8
	c_qinv1__t1_mem0 += MAIN_MEM_r[0]

	c_qinv1__t1_mem1 = S.Task('c_qinv1__t1_mem1', length=1, delay_cost=1)
	S += c_qinv1__t1_mem1 >= 8
	c_qinv1__t1_mem1 += MM_MEM[3]

	c1_t4_t2 = S.Task('c1_t4_t2', length=1, delay_cost=1)
	S += c1_t4_t2 >= 9
	c1_t4_t2 += MAS[3]

	c_qinv1__t0_in = S.Task('c_qinv1__t0_in', length=1, delay_cost=1)
	S += c_qinv1__t0_in >= 9
	c_qinv1__t0_in += MM_in[0]

	c_qinv1__t0_mem0 = S.Task('c_qinv1__t0_mem0', length=1, delay_cost=1)
	S += c_qinv1__t0_mem0 >= 9
	c_qinv1__t0_mem0 += MAIN_MEM_r[0]

	c_qinv1__t0_mem1 = S.Task('c_qinv1__t0_mem1', length=1, delay_cost=1)
	S += c_qinv1__t0_mem1 >= 9
	c_qinv1__t0_mem1 += MM_MEM[1]

	c_qinv1__t1 = S.Task('c_qinv1__t1', length=8, delay_cost=1)
	S += c_qinv1__t1 >= 9
	c_qinv1__t1 += MM[0]

	c_qinv1__t3_mem0 = S.Task('c_qinv1__t3_mem0', length=1, delay_cost=1)
	S += c_qinv1__t3_mem0 >= 9
	c_qinv1__t3_mem0 += MM_MEM[0]

	c_qinv1__t3_mem1 = S.Task('c_qinv1__t3_mem1', length=1, delay_cost=1)
	S += c_qinv1__t3_mem1 >= 9
	c_qinv1__t3_mem1 += MM_MEM[3]

	c_qinv0_t0_in = S.Task('c_qinv0_t0_in', length=1, delay_cost=1)
	S += c_qinv0_t0_in >= 10
	c_qinv0_t0_in += MM_in[1]

	c_qinv0_t0_mem0 = S.Task('c_qinv0_t0_mem0', length=1, delay_cost=1)
	S += c_qinv0_t0_mem0 >= 10
	c_qinv0_t0_mem0 += MAIN_MEM_r[0]

	c_qinv0_t0_mem1 = S.Task('c_qinv0_t0_mem1', length=1, delay_cost=1)
	S += c_qinv0_t0_mem1 >= 10
	c_qinv0_t0_mem1 += MM_MEM[1]

	c_qinv0_t3_mem0 = S.Task('c_qinv0_t3_mem0', length=1, delay_cost=1)
	S += c_qinv0_t3_mem0 >= 10
	c_qinv0_t3_mem0 += MM_MEM[0]

	c_qinv0_t3_mem1 = S.Task('c_qinv0_t3_mem1', length=1, delay_cost=1)
	S += c_qinv0_t3_mem1 >= 10
	c_qinv0_t3_mem1 += MM_MEM[3]

	c_qinv1__t0 = S.Task('c_qinv1__t0', length=8, delay_cost=1)
	S += c_qinv1__t0 >= 10
	c_qinv1__t0 += MM[0]

	c_qinv1__t3 = S.Task('c_qinv1__t3', length=1, delay_cost=1)
	S += c_qinv1__t3 >= 10
	c_qinv1__t3 += MAS[0]

	c_qinv0_t0 = S.Task('c_qinv0_t0', length=8, delay_cost=1)
	S += c_qinv0_t0 >= 11
	c_qinv0_t0 += MM[1]

	c_qinv0_t1_in = S.Task('c_qinv0_t1_in', length=1, delay_cost=1)
	S += c_qinv0_t1_in >= 11
	c_qinv0_t1_in += MM_in[0]

	c_qinv0_t1_mem0 = S.Task('c_qinv0_t1_mem0', length=1, delay_cost=1)
	S += c_qinv0_t1_mem0 >= 11
	c_qinv0_t1_mem0 += MAIN_MEM_r[0]

	c_qinv0_t1_mem1 = S.Task('c_qinv0_t1_mem1', length=1, delay_cost=1)
	S += c_qinv0_t1_mem1 >= 11
	c_qinv0_t1_mem1 += MM_MEM[3]

	c_qinv0_t3 = S.Task('c_qinv0_t3', length=1, delay_cost=1)
	S += c_qinv0_t3 >= 11
	c_qinv0_t3 += MAS[4]

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	S += c2_t0_t2_mem0 >= 12
	c2_t0_t2_mem0 += MAIN_MEM_r[0]

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	S += c2_t0_t2_mem1 >= 12
	c2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t1 = S.Task('c_qinv0_t1', length=8, delay_cost=1)
	S += c_qinv0_t1 >= 12
	c_qinv0_t1 += MM[0]

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	S += c1_t1_t2_mem0 >= 13
	c1_t1_t2_mem0 += MAIN_MEM_r[0]

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	S += c1_t1_t2_mem1 >= 13
	c1_t1_t2_mem1 += MAIN_MEM_r[1]

	c2_t0_t2 = S.Task('c2_t0_t2', length=1, delay_cost=1)
	S += c2_t0_t2 >= 13
	c2_t0_t2 += MAS[0]

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	S += c0_t1_t2_mem0 >= 14
	c0_t1_t2_mem0 += MAIN_MEM_r[0]

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	S += c0_t1_t2_mem1 >= 14
	c0_t1_t2_mem1 += MAIN_MEM_r[1]

	c1_t1_t2 = S.Task('c1_t1_t2', length=1, delay_cost=1)
	S += c1_t1_t2 >= 14
	c1_t1_t2 += MAS[2]

	c0_t1_t2 = S.Task('c0_t1_t2', length=1, delay_cost=1)
	S += c0_t1_t2 >= 15
	c0_t1_t2 += MAS[2]

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	S += c2_t1_t2_mem0 >= 15
	c2_t1_t2_mem0 += MAIN_MEM_r[0]

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	S += c2_t1_t2_mem1 >= 15
	c2_t1_t2_mem1 += MAIN_MEM_r[1]

	c2_t1_t2 = S.Task('c2_t1_t2', length=1, delay_cost=1)
	S += c2_t1_t2 >= 16
	c2_t1_t2 += MAS[2]

	c_qinv1__t2_mem0 = S.Task('c_qinv1__t2_mem0', length=1, delay_cost=1)
	S += c_qinv1__t2_mem0 >= 16
	c_qinv1__t2_mem0 += MAIN_MEM_r[0]

	c_qinv1__t2_mem1 = S.Task('c_qinv1__t2_mem1', length=1, delay_cost=1)
	S += c_qinv1__t2_mem1 >= 16
	c_qinv1__t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t2_mem0 = S.Task('c_qinv0_t2_mem0', length=1, delay_cost=1)
	S += c_qinv0_t2_mem0 >= 17
	c_qinv0_t2_mem0 += MAIN_MEM_r[0]

	c_qinv0_t2_mem1 = S.Task('c_qinv0_t2_mem1', length=1, delay_cost=1)
	S += c_qinv0_t2_mem1 >= 17
	c_qinv0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1_0_mem0 = S.Task('c_qinv1_0_mem0', length=1, delay_cost=1)
	S += c_qinv1_0_mem0 >= 17
	c_qinv1_0_mem0 += MM_MEM[0]

	c_qinv1_0_mem1 = S.Task('c_qinv1_0_mem1', length=1, delay_cost=1)
	S += c_qinv1_0_mem1 >= 17
	c_qinv1_0_mem1 += MM_MEM[1]

	c_qinv1__t2 = S.Task('c_qinv1__t2', length=1, delay_cost=1)
	S += c_qinv1__t2 >= 17
	c_qinv1__t2 += MAS[0]

	c_qinv1__t4_in = S.Task('c_qinv1__t4_in', length=1, delay_cost=1)
	S += c_qinv1__t4_in >= 17
	c_qinv1__t4_in += MM_in[0]

	c_qinv1__t4_mem0 = S.Task('c_qinv1__t4_mem0', length=1, delay_cost=1)
	S += c_qinv1__t4_mem0 >= 17
	c_qinv1__t4_mem0 += MAS_MEM[0]

	c_qinv1__t4_mem1 = S.Task('c_qinv1__t4_mem1', length=1, delay_cost=1)
	S += c_qinv1__t4_mem1 >= 17
	c_qinv1__t4_mem1 += MAS_MEM[1]

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	S += c1_t0_t2_mem0 >= 18
	c1_t0_t2_mem0 += MAIN_MEM_r[0]

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	S += c1_t0_t2_mem1 >= 18
	c1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t2 = S.Task('c_qinv0_t2', length=1, delay_cost=1)
	S += c_qinv0_t2 >= 18
	c_qinv0_t2 += MAS[0]

	c_qinv0_t4_in = S.Task('c_qinv0_t4_in', length=1, delay_cost=1)
	S += c_qinv0_t4_in >= 18
	c_qinv0_t4_in += MM_in[0]

	c_qinv0_t4_mem0 = S.Task('c_qinv0_t4_mem0', length=1, delay_cost=1)
	S += c_qinv0_t4_mem0 >= 18
	c_qinv0_t4_mem0 += MAS_MEM[0]

	c_qinv0_t4_mem1 = S.Task('c_qinv0_t4_mem1', length=1, delay_cost=1)
	S += c_qinv0_t4_mem1 >= 18
	c_qinv0_t4_mem1 += MAS_MEM[9]

	c_qinv1_0 = S.Task('c_qinv1_0', length=1, delay_cost=1)
	S += c_qinv1_0 >= 18
	c_qinv1_0 += MAS[1]

	c_qinv1__t4 = S.Task('c_qinv1__t4', length=8, delay_cost=1)
	S += c_qinv1__t4 >= 18
	c_qinv1__t4 += MM[0]

	c_qinv1__t5_mem0 = S.Task('c_qinv1__t5_mem0', length=1, delay_cost=1)
	S += c_qinv1__t5_mem0 >= 18
	c_qinv1__t5_mem0 += MM_MEM[0]

	c_qinv1__t5_mem1 = S.Task('c_qinv1__t5_mem1', length=1, delay_cost=1)
	S += c_qinv1__t5_mem1 >= 18
	c_qinv1__t5_mem1 += MM_MEM[1]

	c0_t0_t2_mem0 = S.Task('c0_t0_t2_mem0', length=1, delay_cost=1)
	S += c0_t0_t2_mem0 >= 19
	c0_t0_t2_mem0 += MAIN_MEM_r[0]

	c0_t0_t2_mem1 = S.Task('c0_t0_t2_mem1', length=1, delay_cost=1)
	S += c0_t0_t2_mem1 >= 19
	c0_t0_t2_mem1 += MAIN_MEM_r[1]

	c1_t0_t2 = S.Task('c1_t0_t2', length=1, delay_cost=1)
	S += c1_t0_t2 >= 19
	c1_t0_t2 += MAS[0]

	c_qinv00_mem0 = S.Task('c_qinv00_mem0', length=1, delay_cost=1)
	S += c_qinv00_mem0 >= 19
	c_qinv00_mem0 += MM_MEM[2]

	c_qinv00_mem1 = S.Task('c_qinv00_mem1', length=1, delay_cost=1)
	S += c_qinv00_mem1 >= 19
	c_qinv00_mem1 += MM_MEM[1]

	c_qinv0_t4 = S.Task('c_qinv0_t4', length=8, delay_cost=1)
	S += c_qinv0_t4 >= 19
	c_qinv0_t4 += MM[0]

	c_qinv1__t5 = S.Task('c_qinv1__t5', length=1, delay_cost=1)
	S += c_qinv1__t5 >= 19
	c_qinv1__t5 += MAS[3]

	c0_t0_t2 = S.Task('c0_t0_t2', length=1, delay_cost=1)
	S += c0_t0_t2 >= 20
	c0_t0_t2 += MAS[0]

	c1_t0_t0_in = S.Task('c1_t0_t0_in', length=1, delay_cost=1)
	S += c1_t0_t0_in >= 20
	c1_t0_t0_in += MM_in[1]

	c1_t0_t0_mem0 = S.Task('c1_t0_t0_mem0', length=1, delay_cost=1)
	S += c1_t0_t0_mem0 >= 20
	c1_t0_t0_mem0 += MAIN_MEM_r[0]

	c1_t0_t0_mem1 = S.Task('c1_t0_t0_mem1', length=1, delay_cost=1)
	S += c1_t0_t0_mem1 >= 20
	c1_t0_t0_mem1 += MAS_MEM[5]

	c1_t30_mem0 = S.Task('c1_t30_mem0', length=1, delay_cost=1)
	S += c1_t30_mem0 >= 20
	c1_t30_mem0 += MAS_MEM[4]

	c1_t30_mem1 = S.Task('c1_t30_mem1', length=1, delay_cost=1)
	S += c1_t30_mem1 >= 20
	c1_t30_mem1 += MAS_MEM[3]

	c_qinv00 = S.Task('c_qinv00', length=1, delay_cost=1)
	S += c_qinv00 >= 20
	c_qinv00 += MAS[2]

	c_qinv0_t5_mem0 = S.Task('c_qinv0_t5_mem0', length=1, delay_cost=1)
	S += c_qinv0_t5_mem0 >= 20
	c_qinv0_t5_mem0 += MM_MEM[2]

	c_qinv0_t5_mem1 = S.Task('c_qinv0_t5_mem1', length=1, delay_cost=1)
	S += c_qinv0_t5_mem1 >= 20
	c_qinv0_t5_mem1 += MM_MEM[1]

	c0_t0_t0_in = S.Task('c0_t0_t0_in', length=1, delay_cost=1)
	S += c0_t0_t0_in >= 21
	c0_t0_t0_in += MM_in[0]

	c0_t0_t0_mem0 = S.Task('c0_t0_t0_mem0', length=1, delay_cost=1)
	S += c0_t0_t0_mem0 >= 21
	c0_t0_t0_mem0 += MAIN_MEM_r[0]

	c0_t0_t0_mem1 = S.Task('c0_t0_t0_mem1', length=1, delay_cost=1)
	S += c0_t0_t0_mem1 >= 21
	c0_t0_t0_mem1 += MAS_MEM[5]

	c0_t30_mem0 = S.Task('c0_t30_mem0', length=1, delay_cost=1)
	S += c0_t30_mem0 >= 21
	c0_t30_mem0 += MAS_MEM[4]

	c0_t30_mem1 = S.Task('c0_t30_mem1', length=1, delay_cost=1)
	S += c0_t30_mem1 >= 21
	c0_t30_mem1 += MAS_MEM[3]

	c1_t0_t0 = S.Task('c1_t0_t0', length=8, delay_cost=1)
	S += c1_t0_t0 >= 21
	c1_t0_t0 += MM[1]

	c1_t30 = S.Task('c1_t30', length=1, delay_cost=1)
	S += c1_t30 >= 21
	c1_t30 += MAS[4]

	c1_t4_t0_in = S.Task('c1_t4_t0_in', length=1, delay_cost=1)
	S += c1_t4_t0_in >= 21
	c1_t4_t0_in += MM_in[1]

	c1_t4_t0_mem0 = S.Task('c1_t4_t0_mem0', length=1, delay_cost=1)
	S += c1_t4_t0_mem0 >= 21
	c1_t4_t0_mem0 += MAS_MEM[0]

	c1_t4_t0_mem1 = S.Task('c1_t4_t0_mem1', length=1, delay_cost=1)
	S += c1_t4_t0_mem1 >= 21
	c1_t4_t0_mem1 += MAS_MEM[9]

	c_qinv0_t5 = S.Task('c_qinv0_t5', length=1, delay_cost=1)
	S += c_qinv0_t5 >= 21
	c_qinv0_t5 += MAS[5]

	c0_t0_t0 = S.Task('c0_t0_t0', length=8, delay_cost=1)
	S += c0_t0_t0 >= 22
	c0_t0_t0 += MM[0]

	c0_t30 = S.Task('c0_t30', length=1, delay_cost=1)
	S += c0_t30 >= 22
	c0_t30 += MAS[3]

	c0_t4_t0_in = S.Task('c0_t4_t0_in', length=1, delay_cost=1)
	S += c0_t4_t0_in >= 22
	c0_t4_t0_in += MM_in[0]

	c0_t4_t0_mem0 = S.Task('c0_t4_t0_mem0', length=1, delay_cost=1)
	S += c0_t4_t0_mem0 >= 22
	c0_t4_t0_mem0 += MAS_MEM[6]

	c0_t4_t0_mem1 = S.Task('c0_t4_t0_mem1', length=1, delay_cost=1)
	S += c0_t4_t0_mem1 >= 22
	c0_t4_t0_mem1 += MAS_MEM[7]

	c1_t4_t0 = S.Task('c1_t4_t0', length=8, delay_cost=1)
	S += c1_t4_t0 >= 22
	c1_t4_t0 += MM[1]

	c2_t0_t0_in = S.Task('c2_t0_t0_in', length=1, delay_cost=1)
	S += c2_t0_t0_in >= 22
	c2_t0_t0_in += MM_in[1]

	c2_t0_t0_mem0 = S.Task('c2_t0_t0_mem0', length=1, delay_cost=1)
	S += c2_t0_t0_mem0 >= 22
	c2_t0_t0_mem0 += MAIN_MEM_r[0]

	c2_t0_t0_mem1 = S.Task('c2_t0_t0_mem1', length=1, delay_cost=1)
	S += c2_t0_t0_mem1 >= 22
	c2_t0_t0_mem1 += MAS_MEM[5]

	c2_t30_mem0 = S.Task('c2_t30_mem0', length=1, delay_cost=1)
	S += c2_t30_mem0 >= 22
	c2_t30_mem0 += MAS_MEM[4]

	c2_t30_mem1 = S.Task('c2_t30_mem1', length=1, delay_cost=1)
	S += c2_t30_mem1 >= 22
	c2_t30_mem1 += MAS_MEM[3]

	c0_t4_t0 = S.Task('c0_t4_t0', length=8, delay_cost=1)
	S += c0_t4_t0 >= 23
	c0_t4_t0 += MM[0]

	c1_t1_t0_in = S.Task('c1_t1_t0_in', length=1, delay_cost=1)
	S += c1_t1_t0_in >= 23
	c1_t1_t0_in += MM_in[0]

	c1_t1_t0_mem0 = S.Task('c1_t1_t0_mem0', length=1, delay_cost=1)
	S += c1_t1_t0_mem0 >= 23
	c1_t1_t0_mem0 += MAIN_MEM_r[0]

	c1_t1_t0_mem1 = S.Task('c1_t1_t0_mem1', length=1, delay_cost=1)
	S += c1_t1_t0_mem1 >= 23
	c1_t1_t0_mem1 += MAS_MEM[3]

	c2_t0_t0 = S.Task('c2_t0_t0', length=8, delay_cost=1)
	S += c2_t0_t0 >= 23
	c2_t0_t0 += MM[1]

	c2_t30 = S.Task('c2_t30', length=1, delay_cost=1)
	S += c2_t30 >= 23
	c2_t30 += MAS[0]

	c2_t4_t0_in = S.Task('c2_t4_t0_in', length=1, delay_cost=1)
	S += c2_t4_t0_in >= 23
	c2_t4_t0_in += MM_in[1]

	c2_t4_t0_mem0 = S.Task('c2_t4_t0_mem0', length=1, delay_cost=1)
	S += c2_t4_t0_mem0 >= 23
	c2_t4_t0_mem0 += MAS_MEM[2]

	c2_t4_t0_mem1 = S.Task('c2_t4_t0_mem1', length=1, delay_cost=1)
	S += c2_t4_t0_mem1 >= 23
	c2_t4_t0_mem1 += MAS_MEM[1]

	c1_t1_t0 = S.Task('c1_t1_t0', length=8, delay_cost=1)
	S += c1_t1_t0 >= 24
	c1_t1_t0 += MM[0]

	c2_t1_t0_in = S.Task('c2_t1_t0_in', length=1, delay_cost=1)
	S += c2_t1_t0_in >= 24
	c2_t1_t0_in += MM_in[1]

	c2_t1_t0_mem0 = S.Task('c2_t1_t0_mem0', length=1, delay_cost=1)
	S += c2_t1_t0_mem0 >= 24
	c2_t1_t0_mem0 += MAIN_MEM_r[0]

	c2_t1_t0_mem1 = S.Task('c2_t1_t0_mem1', length=1, delay_cost=1)
	S += c2_t1_t0_mem1 >= 24
	c2_t1_t0_mem1 += MAS_MEM[3]

	c2_t4_t0 = S.Task('c2_t4_t0', length=8, delay_cost=1)
	S += c2_t4_t0 >= 24
	c2_t4_t0 += MM[1]

	c0_t1_t0_in = S.Task('c0_t1_t0_in', length=1, delay_cost=1)
	S += c0_t1_t0_in >= 25
	c0_t1_t0_in += MM_in[0]

	c0_t1_t0_mem0 = S.Task('c0_t1_t0_mem0', length=1, delay_cost=1)
	S += c0_t1_t0_mem0 >= 25
	c0_t1_t0_mem0 += MAIN_MEM_r[0]

	c0_t1_t0_mem1 = S.Task('c0_t1_t0_mem1', length=1, delay_cost=1)
	S += c0_t1_t0_mem1 >= 25
	c0_t1_t0_mem1 += MAS_MEM[3]

	c2_t1_t0 = S.Task('c2_t1_t0', length=8, delay_cost=1)
	S += c2_t1_t0 >= 25
	c2_t1_t0 += MM[1]

	c_qinv1_1_mem0 = S.Task('c_qinv1_1_mem0', length=1, delay_cost=1)
	S += c_qinv1_1_mem0 >= 25
	c_qinv1_1_mem0 += MM_MEM[0]

	c_qinv1_1_mem1 = S.Task('c_qinv1_1_mem1', length=1, delay_cost=1)
	S += c_qinv1_1_mem1 >= 25
	c_qinv1_1_mem1 += MAS_MEM[7]

	c0_t1_t0 = S.Task('c0_t1_t0', length=8, delay_cost=1)
	S += c0_t1_t0 >= 26
	c0_t1_t0 += MM[0]

	c0_t1_t1_in = S.Task('c0_t1_t1_in', length=1, delay_cost=1)
	S += c0_t1_t1_in >= 26
	c0_t1_t1_in += MM_in[0]

	c0_t1_t1_mem0 = S.Task('c0_t1_t1_mem0', length=1, delay_cost=1)
	S += c0_t1_t1_mem0 >= 26
	c0_t1_t1_mem0 += MAIN_MEM_r[0]

	c0_t1_t1_mem1 = S.Task('c0_t1_t1_mem1', length=1, delay_cost=1)
	S += c0_t1_t1_mem1 >= 26
	c0_t1_t1_mem1 += MAS_MEM[7]

	c_qinv01_mem0 = S.Task('c_qinv01_mem0', length=1, delay_cost=1)
	S += c_qinv01_mem0 >= 26
	c_qinv01_mem0 += MM_MEM[0]

	c_qinv01_mem1 = S.Task('c_qinv01_mem1', length=1, delay_cost=1)
	S += c_qinv01_mem1 >= 26
	c_qinv01_mem1 += MAS_MEM[11]

	c_qinv1_1 = S.Task('c_qinv1_1', length=1, delay_cost=1)
	S += c_qinv1_1 >= 26
	c_qinv1_1 += MAS[3]

	c0_t1_t1 = S.Task('c0_t1_t1', length=8, delay_cost=1)
	S += c0_t1_t1 >= 27
	c0_t1_t1 += MM[0]

	c2_t0_t1_in = S.Task('c2_t0_t1_in', length=1, delay_cost=1)
	S += c2_t0_t1_in >= 27
	c2_t0_t1_in += MM_in[0]

	c2_t0_t1_mem0 = S.Task('c2_t0_t1_mem0', length=1, delay_cost=1)
	S += c2_t0_t1_mem0 >= 27
	c2_t0_t1_mem0 += MAIN_MEM_r[0]

	c2_t0_t1_mem1 = S.Task('c2_t0_t1_mem1', length=1, delay_cost=1)
	S += c2_t0_t1_mem1 >= 27
	c2_t0_t1_mem1 += MAS_MEM[11]

	c2_t1_t3_mem0 = S.Task('c2_t1_t3_mem0', length=1, delay_cost=1)
	S += c2_t1_t3_mem0 >= 27
	c2_t1_t3_mem0 += MAS_MEM[2]

	c2_t1_t3_mem1 = S.Task('c2_t1_t3_mem1', length=1, delay_cost=1)
	S += c2_t1_t3_mem1 >= 27
	c2_t1_t3_mem1 += MAS_MEM[7]

	c_qinv01 = S.Task('c_qinv01', length=1, delay_cost=1)
	S += c_qinv01 >= 27
	c_qinv01 += MAS[5]

	c0_t0_t3_mem0 = S.Task('c0_t0_t3_mem0', length=1, delay_cost=1)
	S += c0_t0_t3_mem0 >= 28
	c0_t0_t3_mem0 += MAS_MEM[4]

	c0_t0_t3_mem1 = S.Task('c0_t0_t3_mem1', length=1, delay_cost=1)
	S += c0_t0_t3_mem1 >= 28
	c0_t0_t3_mem1 += MAS_MEM[11]

	c1_t1_t1_in = S.Task('c1_t1_t1_in', length=1, delay_cost=1)
	S += c1_t1_t1_in >= 28
	c1_t1_t1_in += MM_in[0]

	c1_t1_t1_mem0 = S.Task('c1_t1_t1_mem0', length=1, delay_cost=1)
	S += c1_t1_t1_mem0 >= 28
	c1_t1_t1_mem0 += MAIN_MEM_r[0]

	c1_t1_t1_mem1 = S.Task('c1_t1_t1_mem1', length=1, delay_cost=1)
	S += c1_t1_t1_mem1 >= 28
	c1_t1_t1_mem1 += MAS_MEM[7]

	c2_t0_t1 = S.Task('c2_t0_t1', length=8, delay_cost=1)
	S += c2_t0_t1 >= 28
	c2_t0_t1 += MM[0]

	c2_t1_t3 = S.Task('c2_t1_t3', length=1, delay_cost=1)
	S += c2_t1_t3 >= 28
	c2_t1_t3 += MAS[0]

	c0_t0_t1_in = S.Task('c0_t0_t1_in', length=1, delay_cost=1)
	S += c0_t0_t1_in >= 29
	c0_t0_t1_in += MM_in[1]

	c0_t0_t1_mem0 = S.Task('c0_t0_t1_mem0', length=1, delay_cost=1)
	S += c0_t0_t1_mem0 >= 29
	c0_t0_t1_mem0 += MAIN_MEM_r[0]

	c0_t0_t1_mem1 = S.Task('c0_t0_t1_mem1', length=1, delay_cost=1)
	S += c0_t0_t1_mem1 >= 29
	c0_t0_t1_mem1 += MAS_MEM[11]

	c0_t0_t3 = S.Task('c0_t0_t3', length=1, delay_cost=1)
	S += c0_t0_t3 >= 29
	c0_t0_t3 += MAS[0]

	c1_t1_t1 = S.Task('c1_t1_t1', length=8, delay_cost=1)
	S += c1_t1_t1 >= 29
	c1_t1_t1 += MM[0]

	c2_t31_mem0 = S.Task('c2_t31_mem0', length=1, delay_cost=1)
	S += c2_t31_mem0 >= 29
	c2_t31_mem0 += MAS_MEM[10]

	c2_t31_mem1 = S.Task('c2_t31_mem1', length=1, delay_cost=1)
	S += c2_t31_mem1 >= 29
	c2_t31_mem1 += MAS_MEM[7]

	c0_t0_t1 = S.Task('c0_t0_t1', length=8, delay_cost=1)
	S += c0_t0_t1 >= 30
	c0_t0_t1 += MM[1]

	c1_t0_t3_mem0 = S.Task('c1_t0_t3_mem0', length=1, delay_cost=1)
	S += c1_t0_t3_mem0 >= 30
	c1_t0_t3_mem0 += MAS_MEM[4]

	c1_t0_t3_mem1 = S.Task('c1_t0_t3_mem1', length=1, delay_cost=1)
	S += c1_t0_t3_mem1 >= 30
	c1_t0_t3_mem1 += MAS_MEM[11]

	c2_t1_t1_in = S.Task('c2_t1_t1_in', length=1, delay_cost=1)
	S += c2_t1_t1_in >= 30
	c2_t1_t1_in += MM_in[0]

	c2_t1_t1_mem0 = S.Task('c2_t1_t1_mem0', length=1, delay_cost=1)
	S += c2_t1_t1_mem0 >= 30
	c2_t1_t1_mem0 += MAIN_MEM_r[0]

	c2_t1_t1_mem1 = S.Task('c2_t1_t1_mem1', length=1, delay_cost=1)
	S += c2_t1_t1_mem1 >= 30
	c2_t1_t1_mem1 += MAS_MEM[7]

	c2_t31 = S.Task('c2_t31', length=1, delay_cost=1)
	S += c2_t31 >= 30
	c2_t31 += MAS[1]

	c1_t0_t1_in = S.Task('c1_t0_t1_in', length=1, delay_cost=1)
	S += c1_t0_t1_in >= 31
	c1_t0_t1_in += MM_in[0]

	c1_t0_t1_mem0 = S.Task('c1_t0_t1_mem0', length=1, delay_cost=1)
	S += c1_t0_t1_mem0 >= 31
	c1_t0_t1_mem0 += MAIN_MEM_r[0]

	c1_t0_t1_mem1 = S.Task('c1_t0_t1_mem1', length=1, delay_cost=1)
	S += c1_t0_t1_mem1 >= 31
	c1_t0_t1_mem1 += MAS_MEM[11]

	c1_t0_t3 = S.Task('c1_t0_t3', length=1, delay_cost=1)
	S += c1_t0_t3 >= 31
	c1_t0_t3 += MAS[0]

	c1_t31_mem0 = S.Task('c1_t31_mem0', length=1, delay_cost=1)
	S += c1_t31_mem0 >= 31
	c1_t31_mem0 += MAS_MEM[10]

	c1_t31_mem1 = S.Task('c1_t31_mem1', length=1, delay_cost=1)
	S += c1_t31_mem1 >= 31
	c1_t31_mem1 += MAS_MEM[7]

	c2_t1_t1 = S.Task('c2_t1_t1', length=8, delay_cost=1)
	S += c2_t1_t1 >= 31
	c2_t1_t1 += MM[0]

	c0_t1_t3_mem0 = S.Task('c0_t1_t3_mem0', length=1, delay_cost=1)
	S += c0_t1_t3_mem0 >= 32
	c0_t1_t3_mem0 += MAS_MEM[2]

	c0_t1_t3_mem1 = S.Task('c0_t1_t3_mem1', length=1, delay_cost=1)
	S += c0_t1_t3_mem1 >= 32
	c0_t1_t3_mem1 += MAS_MEM[7]

	c1_t0_t1 = S.Task('c1_t0_t1', length=8, delay_cost=1)
	S += c1_t0_t1 >= 32
	c1_t0_t1 += MM[0]

	c1_t31 = S.Task('c1_t31', length=1, delay_cost=1)
	S += c1_t31 >= 32
	c1_t31 += MAS[0]

	c2_t0_t3_mem0 = S.Task('c2_t0_t3_mem0', length=1, delay_cost=1)
	S += c2_t0_t3_mem0 >= 32
	c2_t0_t3_mem0 += MAS_MEM[4]

	c2_t0_t3_mem1 = S.Task('c2_t0_t3_mem1', length=1, delay_cost=1)
	S += c2_t0_t3_mem1 >= 32
	c2_t0_t3_mem1 += MAS_MEM[11]

	c0_t1_t3 = S.Task('c0_t1_t3', length=1, delay_cost=1)
	S += c0_t1_t3 >= 33
	c0_t1_t3 += MAS[0]

	c1_t1_t3_mem0 = S.Task('c1_t1_t3_mem0', length=1, delay_cost=1)
	S += c1_t1_t3_mem0 >= 33
	c1_t1_t3_mem0 += MAS_MEM[2]

	c1_t1_t3_mem1 = S.Task('c1_t1_t3_mem1', length=1, delay_cost=1)
	S += c1_t1_t3_mem1 >= 33
	c1_t1_t3_mem1 += MAS_MEM[7]

	c2_t0_t3 = S.Task('c2_t0_t3', length=1, delay_cost=1)
	S += c2_t0_t3 >= 33
	c2_t0_t3 += MAS[5]

	c0_t31_mem0 = S.Task('c0_t31_mem0', length=1, delay_cost=1)
	S += c0_t31_mem0 >= 34
	c0_t31_mem0 += MAS_MEM[10]

	c0_t31_mem1 = S.Task('c0_t31_mem1', length=1, delay_cost=1)
	S += c0_t31_mem1 >= 34
	c0_t31_mem1 += MAS_MEM[7]

	c1_t1_t3 = S.Task('c1_t1_t3', length=1, delay_cost=1)
	S += c1_t1_t3 >= 34
	c1_t1_t3 += MAS[5]

	c0_t31 = S.Task('c0_t31', length=1, delay_cost=1)
	S += c0_t31 >= 35
	c0_t31 += MAS[5]


	# new tasks
	c0_t0_t4 = S.Task('c0_t0_t4', length=8, delay_cost=1)
	c0_t0_t4 += alt(MM)
	c0_t0_t4_in = S.Task('c0_t0_t4_in', length=1, delay_cost=1)
	c0_t0_t4_in += alt(MM_in)
	S += c0_t0_t4_in*MM_in[0]<=c0_t0_t4*MM[0]
	S += c0_t0_t4_in*MM_in[1]<=c0_t0_t4*MM[1]
	c0_t0_t4_mem0 = S.Task('c0_t0_t4_mem0', length=1, delay_cost=1)
	c0_t0_t4_mem0 += MAS_MEM[0]
	S += 20 < c0_t0_t4_mem0
	S += c0_t0_t4_mem0 <= c0_t0_t4

	c0_t0_t4_mem1 = S.Task('c0_t0_t4_mem1', length=1, delay_cost=1)
	c0_t0_t4_mem1 += MAS_MEM[1]
	S += 29 < c0_t0_t4_mem1
	S += c0_t0_t4_mem1 <= c0_t0_t4

	c0_t00 = S.Task('c0_t00', length=1, delay_cost=1)
	c0_t00 += alt(MAS)
	c0_t00_mem0 = S.Task('c0_t00_mem0', length=1, delay_cost=1)
	c0_t00_mem0 += MM_MEM[0]
	S += 29 < c0_t00_mem0
	S += c0_t00_mem0 <= c0_t00

	c0_t00_mem1 = S.Task('c0_t00_mem1', length=1, delay_cost=1)
	c0_t00_mem1 += MM_MEM[3]
	S += 37 < c0_t00_mem1
	S += c0_t00_mem1 <= c0_t00

	c0_t0_t5 = S.Task('c0_t0_t5', length=1, delay_cost=1)
	c0_t0_t5 += alt(MAS)
	c0_t0_t5_mem0 = S.Task('c0_t0_t5_mem0', length=1, delay_cost=1)
	c0_t0_t5_mem0 += MM_MEM[0]
	S += 29 < c0_t0_t5_mem0
	S += c0_t0_t5_mem0 <= c0_t0_t5

	c0_t0_t5_mem1 = S.Task('c0_t0_t5_mem1', length=1, delay_cost=1)
	c0_t0_t5_mem1 += MM_MEM[3]
	S += 37 < c0_t0_t5_mem1
	S += c0_t0_t5_mem1 <= c0_t0_t5

	c0_t1_t4 = S.Task('c0_t1_t4', length=8, delay_cost=1)
	c0_t1_t4 += alt(MM)
	c0_t1_t4_in = S.Task('c0_t1_t4_in', length=1, delay_cost=1)
	c0_t1_t4_in += alt(MM_in)
	S += c0_t1_t4_in*MM_in[0]<=c0_t1_t4*MM[0]
	S += c0_t1_t4_in*MM_in[1]<=c0_t1_t4*MM[1]
	c0_t1_t4_mem0 = S.Task('c0_t1_t4_mem0', length=1, delay_cost=1)
	c0_t1_t4_mem0 += MAS_MEM[4]
	S += 15 < c0_t1_t4_mem0
	S += c0_t1_t4_mem0 <= c0_t1_t4

	c0_t1_t4_mem1 = S.Task('c0_t1_t4_mem1', length=1, delay_cost=1)
	c0_t1_t4_mem1 += MAS_MEM[1]
	S += 33 < c0_t1_t4_mem1
	S += c0_t1_t4_mem1 <= c0_t1_t4

	c0_t10 = S.Task('c0_t10', length=1, delay_cost=1)
	c0_t10 += alt(MAS)
	c0_t10_mem0 = S.Task('c0_t10_mem0', length=1, delay_cost=1)
	c0_t10_mem0 += MM_MEM[0]
	S += 34 < c0_t10_mem0
	S += c0_t10_mem0 <= c0_t10

	c0_t10_mem1 = S.Task('c0_t10_mem1', length=1, delay_cost=1)
	c0_t10_mem1 += MM_MEM[1]
	S += 33 < c0_t10_mem1
	S += c0_t10_mem1 <= c0_t10

	c0_t1_t5 = S.Task('c0_t1_t5', length=1, delay_cost=1)
	c0_t1_t5 += alt(MAS)
	c0_t1_t5_mem0 = S.Task('c0_t1_t5_mem0', length=1, delay_cost=1)
	c0_t1_t5_mem0 += MM_MEM[0]
	S += 33 < c0_t1_t5_mem0
	S += c0_t1_t5_mem0 <= c0_t1_t5

	c0_t1_t5_mem1 = S.Task('c0_t1_t5_mem1', length=1, delay_cost=1)
	c0_t1_t5_mem1 += MM_MEM[1]
	S += 34 < c0_t1_t5_mem1
	S += c0_t1_t5_mem1 <= c0_t1_t5

	c0_t4_t1 = S.Task('c0_t4_t1', length=8, delay_cost=1)
	c0_t4_t1 += alt(MM)
	c0_t4_t1_in = S.Task('c0_t4_t1_in', length=1, delay_cost=1)
	c0_t4_t1_in += alt(MM_in)
	S += c0_t4_t1_in*MM_in[0]<=c0_t4_t1*MM[0]
	S += c0_t4_t1_in*MM_in[1]<=c0_t4_t1*MM[1]
	c0_t4_t1_mem0 = S.Task('c0_t4_t1_mem0', length=1, delay_cost=1)
	c0_t4_t1_mem0 += MAS_MEM[8]
	S += 5 < c0_t4_t1_mem0
	S += c0_t4_t1_mem0 <= c0_t4_t1

	c0_t4_t1_mem1 = S.Task('c0_t4_t1_mem1', length=1, delay_cost=1)
	c0_t4_t1_mem1 += MAS_MEM[11]
	S += 35 < c0_t4_t1_mem1
	S += c0_t4_t1_mem1 <= c0_t4_t1

	c0_t4_t3 = S.Task('c0_t4_t3', length=1, delay_cost=1)
	c0_t4_t3 += alt(MAS)
	c0_t4_t3_mem0 = S.Task('c0_t4_t3_mem0', length=1, delay_cost=1)
	c0_t4_t3_mem0 += MAS_MEM[6]
	S += 22 < c0_t4_t3_mem0
	S += c0_t4_t3_mem0 <= c0_t4_t3

	c0_t4_t3_mem1 = S.Task('c0_t4_t3_mem1', length=1, delay_cost=1)
	c0_t4_t3_mem1 += MAS_MEM[11]
	S += 35 < c0_t4_t3_mem1
	S += c0_t4_t3_mem1 <= c0_t4_t3

	c1_t0_t4 = S.Task('c1_t0_t4', length=8, delay_cost=1)
	c1_t0_t4 += alt(MM)
	c1_t0_t4_in = S.Task('c1_t0_t4_in', length=1, delay_cost=1)
	c1_t0_t4_in += alt(MM_in)
	S += c1_t0_t4_in*MM_in[0]<=c1_t0_t4*MM[0]
	S += c1_t0_t4_in*MM_in[1]<=c1_t0_t4*MM[1]
	c1_t0_t4_mem0 = S.Task('c1_t0_t4_mem0', length=1, delay_cost=1)
	c1_t0_t4_mem0 += MAS_MEM[0]
	S += 19 < c1_t0_t4_mem0
	S += c1_t0_t4_mem0 <= c1_t0_t4

	c1_t0_t4_mem1 = S.Task('c1_t0_t4_mem1', length=1, delay_cost=1)
	c1_t0_t4_mem1 += MAS_MEM[1]
	S += 31 < c1_t0_t4_mem1
	S += c1_t0_t4_mem1 <= c1_t0_t4

	c1_t00 = S.Task('c1_t00', length=1, delay_cost=1)
	c1_t00 += alt(MAS)
	c1_t00_mem0 = S.Task('c1_t00_mem0', length=1, delay_cost=1)
	c1_t00_mem0 += MM_MEM[2]
	S += 28 < c1_t00_mem0
	S += c1_t00_mem0 <= c1_t00

	c1_t00_mem1 = S.Task('c1_t00_mem1', length=1, delay_cost=1)
	c1_t00_mem1 += MM_MEM[1]
	S += 39 < c1_t00_mem1
	S += c1_t00_mem1 <= c1_t00

	c1_t0_t5 = S.Task('c1_t0_t5', length=1, delay_cost=1)
	c1_t0_t5 += alt(MAS)
	c1_t0_t5_mem0 = S.Task('c1_t0_t5_mem0', length=1, delay_cost=1)
	c1_t0_t5_mem0 += MM_MEM[2]
	S += 28 < c1_t0_t5_mem0
	S += c1_t0_t5_mem0 <= c1_t0_t5

	c1_t0_t5_mem1 = S.Task('c1_t0_t5_mem1', length=1, delay_cost=1)
	c1_t0_t5_mem1 += MM_MEM[1]
	S += 39 < c1_t0_t5_mem1
	S += c1_t0_t5_mem1 <= c1_t0_t5

	c1_t1_t4 = S.Task('c1_t1_t4', length=8, delay_cost=1)
	c1_t1_t4 += alt(MM)
	c1_t1_t4_in = S.Task('c1_t1_t4_in', length=1, delay_cost=1)
	c1_t1_t4_in += alt(MM_in)
	S += c1_t1_t4_in*MM_in[0]<=c1_t1_t4*MM[0]
	S += c1_t1_t4_in*MM_in[1]<=c1_t1_t4*MM[1]
	c1_t1_t4_mem0 = S.Task('c1_t1_t4_mem0', length=1, delay_cost=1)
	c1_t1_t4_mem0 += MAS_MEM[4]
	S += 14 < c1_t1_t4_mem0
	S += c1_t1_t4_mem0 <= c1_t1_t4

	c1_t1_t4_mem1 = S.Task('c1_t1_t4_mem1', length=1, delay_cost=1)
	c1_t1_t4_mem1 += MAS_MEM[11]
	S += 34 < c1_t1_t4_mem1
	S += c1_t1_t4_mem1 <= c1_t1_t4

	c1_t10 = S.Task('c1_t10', length=1, delay_cost=1)
	c1_t10 += alt(MAS)
	c1_t10_mem0 = S.Task('c1_t10_mem0', length=1, delay_cost=1)
	c1_t10_mem0 += MM_MEM[0]
	S += 36 < c1_t10_mem0
	S += c1_t10_mem0 <= c1_t10

	c1_t10_mem1 = S.Task('c1_t10_mem1', length=1, delay_cost=1)
	c1_t10_mem1 += MM_MEM[1]
	S += 31 < c1_t10_mem1
	S += c1_t10_mem1 <= c1_t10

	c1_t1_t5 = S.Task('c1_t1_t5', length=1, delay_cost=1)
	c1_t1_t5 += alt(MAS)
	c1_t1_t5_mem0 = S.Task('c1_t1_t5_mem0', length=1, delay_cost=1)
	c1_t1_t5_mem0 += MM_MEM[0]
	S += 31 < c1_t1_t5_mem0
	S += c1_t1_t5_mem0 <= c1_t1_t5

	c1_t1_t5_mem1 = S.Task('c1_t1_t5_mem1', length=1, delay_cost=1)
	c1_t1_t5_mem1 += MM_MEM[1]
	S += 36 < c1_t1_t5_mem1
	S += c1_t1_t5_mem1 <= c1_t1_t5

	c1_t4_t1 = S.Task('c1_t4_t1', length=8, delay_cost=1)
	c1_t4_t1 += alt(MM)
	c1_t4_t1_in = S.Task('c1_t4_t1_in', length=1, delay_cost=1)
	c1_t4_t1_in += alt(MM_in)
	S += c1_t4_t1_in*MM_in[0]<=c1_t4_t1*MM[0]
	S += c1_t4_t1_in*MM_in[1]<=c1_t4_t1*MM[1]
	c1_t4_t1_mem0 = S.Task('c1_t4_t1_mem0', length=1, delay_cost=1)
	c1_t4_t1_mem0 += MAS_MEM[10]
	S += 7 < c1_t4_t1_mem0
	S += c1_t4_t1_mem0 <= c1_t4_t1

	c1_t4_t1_mem1 = S.Task('c1_t4_t1_mem1', length=1, delay_cost=1)
	c1_t4_t1_mem1 += MAS_MEM[1]
	S += 32 < c1_t4_t1_mem1
	S += c1_t4_t1_mem1 <= c1_t4_t1

	c1_t4_t3 = S.Task('c1_t4_t3', length=1, delay_cost=1)
	c1_t4_t3 += alt(MAS)
	c1_t4_t3_mem0 = S.Task('c1_t4_t3_mem0', length=1, delay_cost=1)
	c1_t4_t3_mem0 += MAS_MEM[8]
	S += 21 < c1_t4_t3_mem0
	S += c1_t4_t3_mem0 <= c1_t4_t3

	c1_t4_t3_mem1 = S.Task('c1_t4_t3_mem1', length=1, delay_cost=1)
	c1_t4_t3_mem1 += MAS_MEM[1]
	S += 32 < c1_t4_t3_mem1
	S += c1_t4_t3_mem1 <= c1_t4_t3

	c2_t0_t4 = S.Task('c2_t0_t4', length=8, delay_cost=1)
	c2_t0_t4 += alt(MM)
	c2_t0_t4_in = S.Task('c2_t0_t4_in', length=1, delay_cost=1)
	c2_t0_t4_in += alt(MM_in)
	S += c2_t0_t4_in*MM_in[0]<=c2_t0_t4*MM[0]
	S += c2_t0_t4_in*MM_in[1]<=c2_t0_t4*MM[1]
	c2_t0_t4_mem0 = S.Task('c2_t0_t4_mem0', length=1, delay_cost=1)
	c2_t0_t4_mem0 += MAS_MEM[0]
	S += 13 < c2_t0_t4_mem0
	S += c2_t0_t4_mem0 <= c2_t0_t4

	c2_t0_t4_mem1 = S.Task('c2_t0_t4_mem1', length=1, delay_cost=1)
	c2_t0_t4_mem1 += MAS_MEM[11]
	S += 33 < c2_t0_t4_mem1
	S += c2_t0_t4_mem1 <= c2_t0_t4

	c2_t00 = S.Task('c2_t00', length=1, delay_cost=1)
	c2_t00 += alt(MAS)
	c2_t00_mem0 = S.Task('c2_t00_mem0', length=1, delay_cost=1)
	c2_t00_mem0 += MM_MEM[2]
	S += 30 < c2_t00_mem0
	S += c2_t00_mem0 <= c2_t00

	c2_t00_mem1 = S.Task('c2_t00_mem1', length=1, delay_cost=1)
	c2_t00_mem1 += MM_MEM[1]
	S += 35 < c2_t00_mem1
	S += c2_t00_mem1 <= c2_t00

	c2_t0_t5 = S.Task('c2_t0_t5', length=1, delay_cost=1)
	c2_t0_t5 += alt(MAS)
	c2_t0_t5_mem0 = S.Task('c2_t0_t5_mem0', length=1, delay_cost=1)
	c2_t0_t5_mem0 += MM_MEM[2]
	S += 30 < c2_t0_t5_mem0
	S += c2_t0_t5_mem0 <= c2_t0_t5

	c2_t0_t5_mem1 = S.Task('c2_t0_t5_mem1', length=1, delay_cost=1)
	c2_t0_t5_mem1 += MM_MEM[1]
	S += 35 < c2_t0_t5_mem1
	S += c2_t0_t5_mem1 <= c2_t0_t5

	c2_t1_t4 = S.Task('c2_t1_t4', length=8, delay_cost=1)
	c2_t1_t4 += alt(MM)
	c2_t1_t4_in = S.Task('c2_t1_t4_in', length=1, delay_cost=1)
	c2_t1_t4_in += alt(MM_in)
	S += c2_t1_t4_in*MM_in[0]<=c2_t1_t4*MM[0]
	S += c2_t1_t4_in*MM_in[1]<=c2_t1_t4*MM[1]
	c2_t1_t4_mem0 = S.Task('c2_t1_t4_mem0', length=1, delay_cost=1)
	c2_t1_t4_mem0 += MAS_MEM[4]
	S += 16 < c2_t1_t4_mem0
	S += c2_t1_t4_mem0 <= c2_t1_t4

	c2_t1_t4_mem1 = S.Task('c2_t1_t4_mem1', length=1, delay_cost=1)
	c2_t1_t4_mem1 += MAS_MEM[1]
	S += 28 < c2_t1_t4_mem1
	S += c2_t1_t4_mem1 <= c2_t1_t4

	c2_t10 = S.Task('c2_t10', length=1, delay_cost=1)
	c2_t10 += alt(MAS)
	c2_t10_mem0 = S.Task('c2_t10_mem0', length=1, delay_cost=1)
	c2_t10_mem0 += MM_MEM[0]
	S += 38 < c2_t10_mem0
	S += c2_t10_mem0 <= c2_t10

	c2_t10_mem1 = S.Task('c2_t10_mem1', length=1, delay_cost=1)
	c2_t10_mem1 += MM_MEM[3]
	S += 32 < c2_t10_mem1
	S += c2_t10_mem1 <= c2_t10

	c2_t1_t5 = S.Task('c2_t1_t5', length=1, delay_cost=1)
	c2_t1_t5 += alt(MAS)
	c2_t1_t5_mem0 = S.Task('c2_t1_t5_mem0', length=1, delay_cost=1)
	c2_t1_t5_mem0 += MM_MEM[2]
	S += 32 < c2_t1_t5_mem0
	S += c2_t1_t5_mem0 <= c2_t1_t5

	c2_t1_t5_mem1 = S.Task('c2_t1_t5_mem1', length=1, delay_cost=1)
	c2_t1_t5_mem1 += MM_MEM[1]
	S += 38 < c2_t1_t5_mem1
	S += c2_t1_t5_mem1 <= c2_t1_t5

	c2_t4_t1 = S.Task('c2_t4_t1', length=8, delay_cost=1)
	c2_t4_t1 += alt(MM)
	c2_t4_t1_in = S.Task('c2_t4_t1_in', length=1, delay_cost=1)
	c2_t4_t1_in += alt(MM_in)
	S += c2_t4_t1_in*MM_in[0]<=c2_t4_t1*MM[0]
	S += c2_t4_t1_in*MM_in[1]<=c2_t4_t1*MM[1]
	c2_t4_t1_mem0 = S.Task('c2_t4_t1_mem0', length=1, delay_cost=1)
	c2_t4_t1_mem0 += MAS_MEM[10]
	S += 3 < c2_t4_t1_mem0
	S += c2_t4_t1_mem0 <= c2_t4_t1

	c2_t4_t1_mem1 = S.Task('c2_t4_t1_mem1', length=1, delay_cost=1)
	c2_t4_t1_mem1 += MAS_MEM[3]
	S += 30 < c2_t4_t1_mem1
	S += c2_t4_t1_mem1 <= c2_t4_t1

	c2_t4_t3 = S.Task('c2_t4_t3', length=1, delay_cost=1)
	c2_t4_t3 += alt(MAS)
	c2_t4_t3_mem0 = S.Task('c2_t4_t3_mem0', length=1, delay_cost=1)
	c2_t4_t3_mem0 += MAS_MEM[0]
	S += 23 < c2_t4_t3_mem0
	S += c2_t4_t3_mem0 <= c2_t4_t3

	c2_t4_t3_mem1 = S.Task('c2_t4_t3_mem1', length=1, delay_cost=1)
	c2_t4_t3_mem1 += MAS_MEM[3]
	S += 30 < c2_t4_t3_mem1
	S += c2_t4_t3_mem1 <= c2_t4_t3

	c0_t01 = S.Task('c0_t01', length=1, delay_cost=1)
	c0_t01 += alt(MAS)
	c0_t01_mem0 = S.Task('c0_t01_mem0', length=1, delay_cost=1)
	c0_t01_mem0 += alt(MM_MEM)
	S += (c0_t0_t4*MM[0])-1 < c0_t01_mem0*MM_MEM[0]
	S += (c0_t0_t4*MM[1])-1 < c0_t01_mem0*MM_MEM[2]
	S += c0_t01_mem0 <= c0_t01

	c0_t01_mem1 = S.Task('c0_t01_mem1', length=1, delay_cost=1)
	c0_t01_mem1 += alt(MAS_MEM)
	S += (c0_t0_t5*MAS[0])-1 < c0_t01_mem1*MAS_MEM[1]
	S += (c0_t0_t5*MAS[1])-1 < c0_t01_mem1*MAS_MEM[3]
	S += (c0_t0_t5*MAS[2])-1 < c0_t01_mem1*MAS_MEM[5]
	S += (c0_t0_t5*MAS[3])-1 < c0_t01_mem1*MAS_MEM[7]
	S += (c0_t0_t5*MAS[4])-1 < c0_t01_mem1*MAS_MEM[9]
	S += (c0_t0_t5*MAS[5])-1 < c0_t01_mem1*MAS_MEM[11]
	S += c0_t01_mem1 <= c0_t01

	c0_t11 = S.Task('c0_t11', length=1, delay_cost=1)
	c0_t11 += alt(MAS)
	c0_t11_mem0 = S.Task('c0_t11_mem0', length=1, delay_cost=1)
	c0_t11_mem0 += alt(MM_MEM)
	S += (c0_t1_t4*MM[0])-1 < c0_t11_mem0*MM_MEM[0]
	S += (c0_t1_t4*MM[1])-1 < c0_t11_mem0*MM_MEM[2]
	S += c0_t11_mem0 <= c0_t11

	c0_t11_mem1 = S.Task('c0_t11_mem1', length=1, delay_cost=1)
	c0_t11_mem1 += alt(MAS_MEM)
	S += (c0_t1_t5*MAS[0])-1 < c0_t11_mem1*MAS_MEM[1]
	S += (c0_t1_t5*MAS[1])-1 < c0_t11_mem1*MAS_MEM[3]
	S += (c0_t1_t5*MAS[2])-1 < c0_t11_mem1*MAS_MEM[5]
	S += (c0_t1_t5*MAS[3])-1 < c0_t11_mem1*MAS_MEM[7]
	S += (c0_t1_t5*MAS[4])-1 < c0_t11_mem1*MAS_MEM[9]
	S += (c0_t1_t5*MAS[5])-1 < c0_t11_mem1*MAS_MEM[11]
	S += c0_t11_mem1 <= c0_t11

	c0_t4_t4 = S.Task('c0_t4_t4', length=8, delay_cost=1)
	c0_t4_t4 += alt(MM)
	c0_t4_t4_in = S.Task('c0_t4_t4_in', length=1, delay_cost=1)
	c0_t4_t4_in += alt(MM_in)
	S += c0_t4_t4_in*MM_in[0]<=c0_t4_t4*MM[0]
	S += c0_t4_t4_in*MM_in[1]<=c0_t4_t4*MM[1]
	c0_t4_t4_mem0 = S.Task('c0_t4_t4_mem0', length=1, delay_cost=1)
	c0_t4_t4_mem0 += MAS_MEM[0]
	S += 7 < c0_t4_t4_mem0
	S += c0_t4_t4_mem0 <= c0_t4_t4

	c0_t4_t4_mem1 = S.Task('c0_t4_t4_mem1', length=1, delay_cost=1)
	c0_t4_t4_mem1 += alt(MAS_MEM)
	S += (c0_t4_t3*MAS[0])-1 < c0_t4_t4_mem1*MAS_MEM[1]
	S += (c0_t4_t3*MAS[1])-1 < c0_t4_t4_mem1*MAS_MEM[3]
	S += (c0_t4_t3*MAS[2])-1 < c0_t4_t4_mem1*MAS_MEM[5]
	S += (c0_t4_t3*MAS[3])-1 < c0_t4_t4_mem1*MAS_MEM[7]
	S += (c0_t4_t3*MAS[4])-1 < c0_t4_t4_mem1*MAS_MEM[9]
	S += (c0_t4_t3*MAS[5])-1 < c0_t4_t4_mem1*MAS_MEM[11]
	S += c0_t4_t4_mem1 <= c0_t4_t4

	c0_t40 = S.Task('c0_t40', length=1, delay_cost=1)
	c0_t40 += alt(MAS)
	c0_t40_mem0 = S.Task('c0_t40_mem0', length=1, delay_cost=1)
	c0_t40_mem0 += MM_MEM[0]
	S += 30 < c0_t40_mem0
	S += c0_t40_mem0 <= c0_t40

	c0_t40_mem1 = S.Task('c0_t40_mem1', length=1, delay_cost=1)
	c0_t40_mem1 += alt(MM_MEM)
	S += (c0_t4_t1*MM[0])-1 < c0_t40_mem1*MM_MEM[1]
	S += (c0_t4_t1*MM[1])-1 < c0_t40_mem1*MM_MEM[3]
	S += c0_t40_mem1 <= c0_t40

	c0_t4_t5 = S.Task('c0_t4_t5', length=1, delay_cost=1)
	c0_t4_t5 += alt(MAS)
	c0_t4_t5_mem0 = S.Task('c0_t4_t5_mem0', length=1, delay_cost=1)
	c0_t4_t5_mem0 += MM_MEM[0]
	S += 30 < c0_t4_t5_mem0
	S += c0_t4_t5_mem0 <= c0_t4_t5

	c0_t4_t5_mem1 = S.Task('c0_t4_t5_mem1', length=1, delay_cost=1)
	c0_t4_t5_mem1 += alt(MM_MEM)
	S += (c0_t4_t1*MM[0])-1 < c0_t4_t5_mem1*MM_MEM[1]
	S += (c0_t4_t1*MM[1])-1 < c0_t4_t5_mem1*MM_MEM[3]
	S += c0_t4_t5_mem1 <= c0_t4_t5

	c0_t50 = S.Task('c0_t50', length=1, delay_cost=1)
	c0_t50 += alt(MAS)
	c0_t50_mem0 = S.Task('c0_t50_mem0', length=1, delay_cost=1)
	c0_t50_mem0 += alt(MAS_MEM)
	S += (c0_t00*MAS[0])-1 < c0_t50_mem0*MAS_MEM[0]
	S += (c0_t00*MAS[1])-1 < c0_t50_mem0*MAS_MEM[2]
	S += (c0_t00*MAS[2])-1 < c0_t50_mem0*MAS_MEM[4]
	S += (c0_t00*MAS[3])-1 < c0_t50_mem0*MAS_MEM[6]
	S += (c0_t00*MAS[4])-1 < c0_t50_mem0*MAS_MEM[8]
	S += (c0_t00*MAS[5])-1 < c0_t50_mem0*MAS_MEM[10]
	S += c0_t50_mem0 <= c0_t50

	c0_t50_mem1 = S.Task('c0_t50_mem1', length=1, delay_cost=1)
	c0_t50_mem1 += alt(MAS_MEM)
	S += (c0_t10*MAS[0])-1 < c0_t50_mem1*MAS_MEM[1]
	S += (c0_t10*MAS[1])-1 < c0_t50_mem1*MAS_MEM[3]
	S += (c0_t10*MAS[2])-1 < c0_t50_mem1*MAS_MEM[5]
	S += (c0_t10*MAS[3])-1 < c0_t50_mem1*MAS_MEM[7]
	S += (c0_t10*MAS[4])-1 < c0_t50_mem1*MAS_MEM[9]
	S += (c0_t10*MAS[5])-1 < c0_t50_mem1*MAS_MEM[11]
	S += c0_t50_mem1 <= c0_t50

	c1_t01 = S.Task('c1_t01', length=1, delay_cost=1)
	c1_t01 += alt(MAS)
	c1_t01_mem0 = S.Task('c1_t01_mem0', length=1, delay_cost=1)
	c1_t01_mem0 += alt(MM_MEM)
	S += (c1_t0_t4*MM[0])-1 < c1_t01_mem0*MM_MEM[0]
	S += (c1_t0_t4*MM[1])-1 < c1_t01_mem0*MM_MEM[2]
	S += c1_t01_mem0 <= c1_t01

	c1_t01_mem1 = S.Task('c1_t01_mem1', length=1, delay_cost=1)
	c1_t01_mem1 += alt(MAS_MEM)
	S += (c1_t0_t5*MAS[0])-1 < c1_t01_mem1*MAS_MEM[1]
	S += (c1_t0_t5*MAS[1])-1 < c1_t01_mem1*MAS_MEM[3]
	S += (c1_t0_t5*MAS[2])-1 < c1_t01_mem1*MAS_MEM[5]
	S += (c1_t0_t5*MAS[3])-1 < c1_t01_mem1*MAS_MEM[7]
	S += (c1_t0_t5*MAS[4])-1 < c1_t01_mem1*MAS_MEM[9]
	S += (c1_t0_t5*MAS[5])-1 < c1_t01_mem1*MAS_MEM[11]
	S += c1_t01_mem1 <= c1_t01

	c1_t11 = S.Task('c1_t11', length=1, delay_cost=1)
	c1_t11 += alt(MAS)
	c1_t11_mem0 = S.Task('c1_t11_mem0', length=1, delay_cost=1)
	c1_t11_mem0 += alt(MM_MEM)
	S += (c1_t1_t4*MM[0])-1 < c1_t11_mem0*MM_MEM[0]
	S += (c1_t1_t4*MM[1])-1 < c1_t11_mem0*MM_MEM[2]
	S += c1_t11_mem0 <= c1_t11

	c1_t11_mem1 = S.Task('c1_t11_mem1', length=1, delay_cost=1)
	c1_t11_mem1 += alt(MAS_MEM)
	S += (c1_t1_t5*MAS[0])-1 < c1_t11_mem1*MAS_MEM[1]
	S += (c1_t1_t5*MAS[1])-1 < c1_t11_mem1*MAS_MEM[3]
	S += (c1_t1_t5*MAS[2])-1 < c1_t11_mem1*MAS_MEM[5]
	S += (c1_t1_t5*MAS[3])-1 < c1_t11_mem1*MAS_MEM[7]
	S += (c1_t1_t5*MAS[4])-1 < c1_t11_mem1*MAS_MEM[9]
	S += (c1_t1_t5*MAS[5])-1 < c1_t11_mem1*MAS_MEM[11]
	S += c1_t11_mem1 <= c1_t11

	c1_t4_t4 = S.Task('c1_t4_t4', length=8, delay_cost=1)
	c1_t4_t4 += alt(MM)
	c1_t4_t4_in = S.Task('c1_t4_t4_in', length=1, delay_cost=1)
	c1_t4_t4_in += alt(MM_in)
	S += c1_t4_t4_in*MM_in[0]<=c1_t4_t4*MM[0]
	S += c1_t4_t4_in*MM_in[1]<=c1_t4_t4*MM[1]
	c1_t4_t4_mem0 = S.Task('c1_t4_t4_mem0', length=1, delay_cost=1)
	c1_t4_t4_mem0 += MAS_MEM[6]
	S += 9 < c1_t4_t4_mem0
	S += c1_t4_t4_mem0 <= c1_t4_t4

	c1_t4_t4_mem1 = S.Task('c1_t4_t4_mem1', length=1, delay_cost=1)
	c1_t4_t4_mem1 += alt(MAS_MEM)
	S += (c1_t4_t3*MAS[0])-1 < c1_t4_t4_mem1*MAS_MEM[1]
	S += (c1_t4_t3*MAS[1])-1 < c1_t4_t4_mem1*MAS_MEM[3]
	S += (c1_t4_t3*MAS[2])-1 < c1_t4_t4_mem1*MAS_MEM[5]
	S += (c1_t4_t3*MAS[3])-1 < c1_t4_t4_mem1*MAS_MEM[7]
	S += (c1_t4_t3*MAS[4])-1 < c1_t4_t4_mem1*MAS_MEM[9]
	S += (c1_t4_t3*MAS[5])-1 < c1_t4_t4_mem1*MAS_MEM[11]
	S += c1_t4_t4_mem1 <= c1_t4_t4

	c1_t40 = S.Task('c1_t40', length=1, delay_cost=1)
	c1_t40 += alt(MAS)
	c1_t40_mem0 = S.Task('c1_t40_mem0', length=1, delay_cost=1)
	c1_t40_mem0 += MM_MEM[2]
	S += 29 < c1_t40_mem0
	S += c1_t40_mem0 <= c1_t40

	c1_t40_mem1 = S.Task('c1_t40_mem1', length=1, delay_cost=1)
	c1_t40_mem1 += alt(MM_MEM)
	S += (c1_t4_t1*MM[0])-1 < c1_t40_mem1*MM_MEM[1]
	S += (c1_t4_t1*MM[1])-1 < c1_t40_mem1*MM_MEM[3]
	S += c1_t40_mem1 <= c1_t40

	c1_t4_t5 = S.Task('c1_t4_t5', length=1, delay_cost=1)
	c1_t4_t5 += alt(MAS)
	c1_t4_t5_mem0 = S.Task('c1_t4_t5_mem0', length=1, delay_cost=1)
	c1_t4_t5_mem0 += MM_MEM[2]
	S += 29 < c1_t4_t5_mem0
	S += c1_t4_t5_mem0 <= c1_t4_t5

	c1_t4_t5_mem1 = S.Task('c1_t4_t5_mem1', length=1, delay_cost=1)
	c1_t4_t5_mem1 += alt(MM_MEM)
	S += (c1_t4_t1*MM[0])-1 < c1_t4_t5_mem1*MM_MEM[1]
	S += (c1_t4_t1*MM[1])-1 < c1_t4_t5_mem1*MM_MEM[3]
	S += c1_t4_t5_mem1 <= c1_t4_t5

	c1_t50 = S.Task('c1_t50', length=1, delay_cost=1)
	c1_t50 += alt(MAS)
	c1_t50_mem0 = S.Task('c1_t50_mem0', length=1, delay_cost=1)
	c1_t50_mem0 += alt(MAS_MEM)
	S += (c1_t00*MAS[0])-1 < c1_t50_mem0*MAS_MEM[0]
	S += (c1_t00*MAS[1])-1 < c1_t50_mem0*MAS_MEM[2]
	S += (c1_t00*MAS[2])-1 < c1_t50_mem0*MAS_MEM[4]
	S += (c1_t00*MAS[3])-1 < c1_t50_mem0*MAS_MEM[6]
	S += (c1_t00*MAS[4])-1 < c1_t50_mem0*MAS_MEM[8]
	S += (c1_t00*MAS[5])-1 < c1_t50_mem0*MAS_MEM[10]
	S += c1_t50_mem0 <= c1_t50

	c1_t50_mem1 = S.Task('c1_t50_mem1', length=1, delay_cost=1)
	c1_t50_mem1 += alt(MAS_MEM)
	S += (c1_t10*MAS[0])-1 < c1_t50_mem1*MAS_MEM[1]
	S += (c1_t10*MAS[1])-1 < c1_t50_mem1*MAS_MEM[3]
	S += (c1_t10*MAS[2])-1 < c1_t50_mem1*MAS_MEM[5]
	S += (c1_t10*MAS[3])-1 < c1_t50_mem1*MAS_MEM[7]
	S += (c1_t10*MAS[4])-1 < c1_t50_mem1*MAS_MEM[9]
	S += (c1_t10*MAS[5])-1 < c1_t50_mem1*MAS_MEM[11]
	S += c1_t50_mem1 <= c1_t50

	c2_t01 = S.Task('c2_t01', length=1, delay_cost=1)
	c2_t01 += alt(MAS)
	c2_t01_mem0 = S.Task('c2_t01_mem0', length=1, delay_cost=1)
	c2_t01_mem0 += alt(MM_MEM)
	S += (c2_t0_t4*MM[0])-1 < c2_t01_mem0*MM_MEM[0]
	S += (c2_t0_t4*MM[1])-1 < c2_t01_mem0*MM_MEM[2]
	S += c2_t01_mem0 <= c2_t01

	c2_t01_mem1 = S.Task('c2_t01_mem1', length=1, delay_cost=1)
	c2_t01_mem1 += alt(MAS_MEM)
	S += (c2_t0_t5*MAS[0])-1 < c2_t01_mem1*MAS_MEM[1]
	S += (c2_t0_t5*MAS[1])-1 < c2_t01_mem1*MAS_MEM[3]
	S += (c2_t0_t5*MAS[2])-1 < c2_t01_mem1*MAS_MEM[5]
	S += (c2_t0_t5*MAS[3])-1 < c2_t01_mem1*MAS_MEM[7]
	S += (c2_t0_t5*MAS[4])-1 < c2_t01_mem1*MAS_MEM[9]
	S += (c2_t0_t5*MAS[5])-1 < c2_t01_mem1*MAS_MEM[11]
	S += c2_t01_mem1 <= c2_t01

	c2_t11 = S.Task('c2_t11', length=1, delay_cost=1)
	c2_t11 += alt(MAS)
	c2_t11_mem0 = S.Task('c2_t11_mem0', length=1, delay_cost=1)
	c2_t11_mem0 += alt(MM_MEM)
	S += (c2_t1_t4*MM[0])-1 < c2_t11_mem0*MM_MEM[0]
	S += (c2_t1_t4*MM[1])-1 < c2_t11_mem0*MM_MEM[2]
	S += c2_t11_mem0 <= c2_t11

	c2_t11_mem1 = S.Task('c2_t11_mem1', length=1, delay_cost=1)
	c2_t11_mem1 += alt(MAS_MEM)
	S += (c2_t1_t5*MAS[0])-1 < c2_t11_mem1*MAS_MEM[1]
	S += (c2_t1_t5*MAS[1])-1 < c2_t11_mem1*MAS_MEM[3]
	S += (c2_t1_t5*MAS[2])-1 < c2_t11_mem1*MAS_MEM[5]
	S += (c2_t1_t5*MAS[3])-1 < c2_t11_mem1*MAS_MEM[7]
	S += (c2_t1_t5*MAS[4])-1 < c2_t11_mem1*MAS_MEM[9]
	S += (c2_t1_t5*MAS[5])-1 < c2_t11_mem1*MAS_MEM[11]
	S += c2_t11_mem1 <= c2_t11

	c2_t4_t4 = S.Task('c2_t4_t4', length=8, delay_cost=1)
	c2_t4_t4 += alt(MM)
	c2_t4_t4_in = S.Task('c2_t4_t4_in', length=1, delay_cost=1)
	c2_t4_t4_in += alt(MM_in)
	S += c2_t4_t4_in*MM_in[0]<=c2_t4_t4*MM[0]
	S += c2_t4_t4_in*MM_in[1]<=c2_t4_t4*MM[1]
	c2_t4_t4_mem0 = S.Task('c2_t4_t4_mem0', length=1, delay_cost=1)
	c2_t4_t4_mem0 += MAS_MEM[4]
	S += 5 < c2_t4_t4_mem0
	S += c2_t4_t4_mem0 <= c2_t4_t4

	c2_t4_t4_mem1 = S.Task('c2_t4_t4_mem1', length=1, delay_cost=1)
	c2_t4_t4_mem1 += alt(MAS_MEM)
	S += (c2_t4_t3*MAS[0])-1 < c2_t4_t4_mem1*MAS_MEM[1]
	S += (c2_t4_t3*MAS[1])-1 < c2_t4_t4_mem1*MAS_MEM[3]
	S += (c2_t4_t3*MAS[2])-1 < c2_t4_t4_mem1*MAS_MEM[5]
	S += (c2_t4_t3*MAS[3])-1 < c2_t4_t4_mem1*MAS_MEM[7]
	S += (c2_t4_t3*MAS[4])-1 < c2_t4_t4_mem1*MAS_MEM[9]
	S += (c2_t4_t3*MAS[5])-1 < c2_t4_t4_mem1*MAS_MEM[11]
	S += c2_t4_t4_mem1 <= c2_t4_t4

	c2_t40 = S.Task('c2_t40', length=1, delay_cost=1)
	c2_t40 += alt(MAS)
	c2_t40_mem0 = S.Task('c2_t40_mem0', length=1, delay_cost=1)
	c2_t40_mem0 += MM_MEM[2]
	S += 31 < c2_t40_mem0
	S += c2_t40_mem0 <= c2_t40

	c2_t40_mem1 = S.Task('c2_t40_mem1', length=1, delay_cost=1)
	c2_t40_mem1 += alt(MM_MEM)
	S += (c2_t4_t1*MM[0])-1 < c2_t40_mem1*MM_MEM[1]
	S += (c2_t4_t1*MM[1])-1 < c2_t40_mem1*MM_MEM[3]
	S += c2_t40_mem1 <= c2_t40

	c2_t4_t5 = S.Task('c2_t4_t5', length=1, delay_cost=1)
	c2_t4_t5 += alt(MAS)
	c2_t4_t5_mem0 = S.Task('c2_t4_t5_mem0', length=1, delay_cost=1)
	c2_t4_t5_mem0 += MM_MEM[2]
	S += 31 < c2_t4_t5_mem0
	S += c2_t4_t5_mem0 <= c2_t4_t5

	c2_t4_t5_mem1 = S.Task('c2_t4_t5_mem1', length=1, delay_cost=1)
	c2_t4_t5_mem1 += alt(MM_MEM)
	S += (c2_t4_t1*MM[0])-1 < c2_t4_t5_mem1*MM_MEM[1]
	S += (c2_t4_t1*MM[1])-1 < c2_t4_t5_mem1*MM_MEM[3]
	S += c2_t4_t5_mem1 <= c2_t4_t5

	c2_t50 = S.Task('c2_t50', length=1, delay_cost=1)
	c2_t50 += alt(MAS)
	c2_t50_mem0 = S.Task('c2_t50_mem0', length=1, delay_cost=1)
	c2_t50_mem0 += alt(MAS_MEM)
	S += (c2_t00*MAS[0])-1 < c2_t50_mem0*MAS_MEM[0]
	S += (c2_t00*MAS[1])-1 < c2_t50_mem0*MAS_MEM[2]
	S += (c2_t00*MAS[2])-1 < c2_t50_mem0*MAS_MEM[4]
	S += (c2_t00*MAS[3])-1 < c2_t50_mem0*MAS_MEM[6]
	S += (c2_t00*MAS[4])-1 < c2_t50_mem0*MAS_MEM[8]
	S += (c2_t00*MAS[5])-1 < c2_t50_mem0*MAS_MEM[10]
	S += c2_t50_mem0 <= c2_t50

	c2_t50_mem1 = S.Task('c2_t50_mem1', length=1, delay_cost=1)
	c2_t50_mem1 += alt(MAS_MEM)
	S += (c2_t10*MAS[0])-1 < c2_t50_mem1*MAS_MEM[1]
	S += (c2_t10*MAS[1])-1 < c2_t50_mem1*MAS_MEM[3]
	S += (c2_t10*MAS[2])-1 < c2_t50_mem1*MAS_MEM[5]
	S += (c2_t10*MAS[3])-1 < c2_t50_mem1*MAS_MEM[7]
	S += (c2_t10*MAS[4])-1 < c2_t50_mem1*MAS_MEM[9]
	S += (c2_t10*MAS[5])-1 < c2_t50_mem1*MAS_MEM[11]
	S += c2_t50_mem1 <= c2_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage8MM2_stage1MAS6/FP12_INV_AFTER_FPINV/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

