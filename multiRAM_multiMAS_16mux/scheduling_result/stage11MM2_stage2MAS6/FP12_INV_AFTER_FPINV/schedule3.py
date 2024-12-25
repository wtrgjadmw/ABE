from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 181
	S = Scenario("schedule3", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=11)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_qinv_denom_inv1__in = S.Task('c_qinv_denom_inv1__in', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__in >= 0
	c_qinv_denom_inv1__in += MM_in[0]

	c_qinv_denom_inv1__mem0 = S.Task('c_qinv_denom_inv1__mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem0 >= 0
	c_qinv_denom_inv1__mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv1__mem1 = S.Task('c_qinv_denom_inv1__mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem1 >= 0
	c_qinv_denom_inv1__mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv0_in = S.Task('c_qinv_denom_inv0_in', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_in >= 1
	c_qinv_denom_inv0_in += MM_in[1]

	c_qinv_denom_inv0_mem0 = S.Task('c_qinv_denom_inv0_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem0 >= 1
	c_qinv_denom_inv0_mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv0_mem1 = S.Task('c_qinv_denom_inv0_mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem1 >= 1
	c_qinv_denom_inv0_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv1_ = S.Task('c_qinv_denom_inv1_', length=11, delay_cost=1)
	S += c_qinv_denom_inv1_ >= 1
	c_qinv_denom_inv1_ += MM[0]

	c0_t20_in = S.Task('c0_t20_in', length=1, delay_cost=1)
	S += c0_t20_in >= 2
	c0_t20_in += MAS_in[2]

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	S += c0_t20_mem0 >= 2
	c0_t20_mem0 += MAIN_MEM_r[0]

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	S += c0_t20_mem1 >= 2
	c0_t20_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv0 = S.Task('c_qinv_denom_inv0', length=11, delay_cost=1)
	S += c_qinv_denom_inv0 >= 2
	c_qinv_denom_inv0 += MM[1]

	c0_t20 = S.Task('c0_t20', length=2, delay_cost=1)
	S += c0_t20 >= 3
	c0_t20 += MAS[2]

	c0_t21_in = S.Task('c0_t21_in', length=1, delay_cost=1)
	S += c0_t21_in >= 3
	c0_t21_in += MAS_in[2]

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	S += c0_t21_mem0 >= 3
	c0_t21_mem0 += MAIN_MEM_r[0]

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	S += c0_t21_mem1 >= 3
	c0_t21_mem1 += MAIN_MEM_r[1]

	c0_t21 = S.Task('c0_t21', length=2, delay_cost=1)
	S += c0_t21 >= 4
	c0_t21 += MAS[2]

	c1_t20_in = S.Task('c1_t20_in', length=1, delay_cost=1)
	S += c1_t20_in >= 4
	c1_t20_in += MAS_in[4]

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	S += c1_t20_mem0 >= 4
	c1_t20_mem0 += MAIN_MEM_r[0]

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	S += c1_t20_mem1 >= 4
	c1_t20_mem1 += MAIN_MEM_r[1]

	c0_t4_t2_in = S.Task('c0_t4_t2_in', length=1, delay_cost=1)
	S += c0_t4_t2_in >= 5
	c0_t4_t2_in += MAS_in[4]

	c0_t4_t2_mem0 = S.Task('c0_t4_t2_mem0', length=1, delay_cost=1)
	S += c0_t4_t2_mem0 >= 5
	c0_t4_t2_mem0 += MAS_MEM[4]

	c0_t4_t2_mem1 = S.Task('c0_t4_t2_mem1', length=1, delay_cost=1)
	S += c0_t4_t2_mem1 >= 5
	c0_t4_t2_mem1 += MAS_MEM[5]

	c1_t20 = S.Task('c1_t20', length=2, delay_cost=1)
	S += c1_t20 >= 5
	c1_t20 += MAS[4]

	c1_t21_in = S.Task('c1_t21_in', length=1, delay_cost=1)
	S += c1_t21_in >= 5
	c1_t21_in += MAS_in[2]

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	S += c1_t21_mem0 >= 5
	c1_t21_mem0 += MAIN_MEM_r[0]

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	S += c1_t21_mem1 >= 5
	c1_t21_mem1 += MAIN_MEM_r[1]

	c0_t4_t2 = S.Task('c0_t4_t2', length=2, delay_cost=1)
	S += c0_t4_t2 >= 6
	c0_t4_t2 += MAS[4]

	c1_t21 = S.Task('c1_t21', length=2, delay_cost=1)
	S += c1_t21 >= 6
	c1_t21 += MAS[2]

	c2_t20_in = S.Task('c2_t20_in', length=1, delay_cost=1)
	S += c2_t20_in >= 6
	c2_t20_in += MAS_in[5]

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	S += c2_t20_mem0 >= 6
	c2_t20_mem0 += MAIN_MEM_r[0]

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	S += c2_t20_mem1 >= 6
	c2_t20_mem1 += MAIN_MEM_r[1]

	c1_t4_t2_in = S.Task('c1_t4_t2_in', length=1, delay_cost=1)
	S += c1_t4_t2_in >= 7
	c1_t4_t2_in += MAS_in[5]

	c1_t4_t2_mem0 = S.Task('c1_t4_t2_mem0', length=1, delay_cost=1)
	S += c1_t4_t2_mem0 >= 7
	c1_t4_t2_mem0 += MAS_MEM[8]

	c1_t4_t2_mem1 = S.Task('c1_t4_t2_mem1', length=1, delay_cost=1)
	S += c1_t4_t2_mem1 >= 7
	c1_t4_t2_mem1 += MAS_MEM[5]

	c2_t20 = S.Task('c2_t20', length=2, delay_cost=1)
	S += c2_t20 >= 7
	c2_t20 += MAS[5]

	c2_t21_in = S.Task('c2_t21_in', length=1, delay_cost=1)
	S += c2_t21_in >= 7
	c2_t21_in += MAS_in[4]

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	S += c2_t21_mem0 >= 7
	c2_t21_mem0 += MAIN_MEM_r[0]

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	S += c2_t21_mem1 >= 7
	c2_t21_mem1 += MAIN_MEM_r[1]

	c1_t0_t2_in = S.Task('c1_t0_t2_in', length=1, delay_cost=1)
	S += c1_t0_t2_in >= 8
	c1_t0_t2_in += MAS_in[0]

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	S += c1_t0_t2_mem0 >= 8
	c1_t0_t2_mem0 += MAIN_MEM_r[0]

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	S += c1_t0_t2_mem1 >= 8
	c1_t0_t2_mem1 += MAIN_MEM_r[1]

	c1_t4_t2 = S.Task('c1_t4_t2', length=2, delay_cost=1)
	S += c1_t4_t2 >= 8
	c1_t4_t2 += MAS[5]

	c2_t21 = S.Task('c2_t21', length=2, delay_cost=1)
	S += c2_t21 >= 8
	c2_t21 += MAS[4]

	c1_t0_t2 = S.Task('c1_t0_t2', length=2, delay_cost=1)
	S += c1_t0_t2 >= 9
	c1_t0_t2 += MAS[0]

	c1_t1_t2_in = S.Task('c1_t1_t2_in', length=1, delay_cost=1)
	S += c1_t1_t2_in >= 9
	c1_t1_t2_in += MAS_in[1]

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	S += c1_t1_t2_mem0 >= 9
	c1_t1_t2_mem0 += MAIN_MEM_r[0]

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	S += c1_t1_t2_mem1 >= 9
	c1_t1_t2_mem1 += MAIN_MEM_r[1]

	c2_t4_t2_in = S.Task('c2_t4_t2_in', length=1, delay_cost=1)
	S += c2_t4_t2_in >= 9
	c2_t4_t2_in += MAS_in[5]

	c2_t4_t2_mem0 = S.Task('c2_t4_t2_mem0', length=1, delay_cost=1)
	S += c2_t4_t2_mem0 >= 9
	c2_t4_t2_mem0 += MAS_MEM[10]

	c2_t4_t2_mem1 = S.Task('c2_t4_t2_mem1', length=1, delay_cost=1)
	S += c2_t4_t2_mem1 >= 9
	c2_t4_t2_mem1 += MAS_MEM[9]

	c1_t1_t2 = S.Task('c1_t1_t2', length=2, delay_cost=1)
	S += c1_t1_t2 >= 10
	c1_t1_t2 += MAS[1]

	c2_t1_t2_in = S.Task('c2_t1_t2_in', length=1, delay_cost=1)
	S += c2_t1_t2_in >= 10
	c2_t1_t2_in += MAS_in[0]

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	S += c2_t1_t2_mem0 >= 10
	c2_t1_t2_mem0 += MAIN_MEM_r[0]

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	S += c2_t1_t2_mem1 >= 10
	c2_t1_t2_mem1 += MAIN_MEM_r[1]

	c2_t4_t2 = S.Task('c2_t4_t2', length=2, delay_cost=1)
	S += c2_t4_t2 >= 10
	c2_t4_t2 += MAS[5]

	c0_t0_t2_in = S.Task('c0_t0_t2_in', length=1, delay_cost=1)
	S += c0_t0_t2_in >= 11
	c0_t0_t2_in += MAS_in[1]

	c0_t0_t2_mem0 = S.Task('c0_t0_t2_mem0', length=1, delay_cost=1)
	S += c0_t0_t2_mem0 >= 11
	c0_t0_t2_mem0 += MAIN_MEM_r[0]

	c0_t0_t2_mem1 = S.Task('c0_t0_t2_mem1', length=1, delay_cost=1)
	S += c0_t0_t2_mem1 >= 11
	c0_t0_t2_mem1 += MAIN_MEM_r[1]

	c2_t1_t2 = S.Task('c2_t1_t2', length=2, delay_cost=1)
	S += c2_t1_t2 >= 11
	c2_t1_t2 += MAS[0]

	c0_t0_t2 = S.Task('c0_t0_t2', length=2, delay_cost=1)
	S += c0_t0_t2 >= 12
	c0_t0_t2 += MAS[1]

	c_qinv0_t2_in = S.Task('c_qinv0_t2_in', length=1, delay_cost=1)
	S += c_qinv0_t2_in >= 12
	c_qinv0_t2_in += MAS_in[0]

	c_qinv0_t2_mem0 = S.Task('c_qinv0_t2_mem0', length=1, delay_cost=1)
	S += c_qinv0_t2_mem0 >= 12
	c_qinv0_t2_mem0 += MAIN_MEM_r[0]

	c_qinv0_t2_mem1 = S.Task('c_qinv0_t2_mem1', length=1, delay_cost=1)
	S += c_qinv0_t2_mem1 >= 12
	c_qinv0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t3_in = S.Task('c_qinv1__t3_in', length=1, delay_cost=1)
	S += c_qinv1__t3_in >= 12
	c_qinv1__t3_in += MAS_in[5]

	c_qinv1__t3_mem0 = S.Task('c_qinv1__t3_mem0', length=1, delay_cost=1)
	S += c_qinv1__t3_mem0 >= 12
	c_qinv1__t3_mem0 += MM_MEM[2]

	c_qinv1__t3_mem1 = S.Task('c_qinv1__t3_mem1', length=1, delay_cost=1)
	S += c_qinv1__t3_mem1 >= 12
	c_qinv1__t3_mem1 += MM_MEM[1]

	c_qinv0_t0_in = S.Task('c_qinv0_t0_in', length=1, delay_cost=1)
	S += c_qinv0_t0_in >= 13
	c_qinv0_t0_in += MM_in[1]

	c_qinv0_t0_mem0 = S.Task('c_qinv0_t0_mem0', length=1, delay_cost=1)
	S += c_qinv0_t0_mem0 >= 13
	c_qinv0_t0_mem0 += MAIN_MEM_r[0]

	c_qinv0_t0_mem1 = S.Task('c_qinv0_t0_mem1', length=1, delay_cost=1)
	S += c_qinv0_t0_mem1 >= 13
	c_qinv0_t0_mem1 += MM_MEM[3]

	c_qinv0_t2 = S.Task('c_qinv0_t2', length=2, delay_cost=1)
	S += c_qinv0_t2 >= 13
	c_qinv0_t2 += MAS[0]

	c_qinv0_t3_in = S.Task('c_qinv0_t3_in', length=1, delay_cost=1)
	S += c_qinv0_t3_in >= 13
	c_qinv0_t3_in += MAS_in[1]

	c_qinv0_t3_mem0 = S.Task('c_qinv0_t3_mem0', length=1, delay_cost=1)
	S += c_qinv0_t3_mem0 >= 13
	c_qinv0_t3_mem0 += MM_MEM[2]

	c_qinv0_t3_mem1 = S.Task('c_qinv0_t3_mem1', length=1, delay_cost=1)
	S += c_qinv0_t3_mem1 >= 13
	c_qinv0_t3_mem1 += MM_MEM[1]

	c_qinv1__t3 = S.Task('c_qinv1__t3', length=2, delay_cost=1)
	S += c_qinv1__t3 >= 13
	c_qinv1__t3 += MAS[5]

	c2_t0_t2_in = S.Task('c2_t0_t2_in', length=1, delay_cost=1)
	S += c2_t0_t2_in >= 14
	c2_t0_t2_in += MAS_in[5]

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	S += c2_t0_t2_mem0 >= 14
	c2_t0_t2_mem0 += MAIN_MEM_r[0]

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	S += c2_t0_t2_mem1 >= 14
	c2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t0 = S.Task('c_qinv0_t0', length=11, delay_cost=1)
	S += c_qinv0_t0 >= 14
	c_qinv0_t0 += MM[1]

	c_qinv0_t3 = S.Task('c_qinv0_t3', length=2, delay_cost=1)
	S += c_qinv0_t3 >= 14
	c_qinv0_t3 += MAS[1]

	c2_t0_t2 = S.Task('c2_t0_t2', length=2, delay_cost=1)
	S += c2_t0_t2 >= 15
	c2_t0_t2 += MAS[5]

	c_qinv0_t4_in = S.Task('c_qinv0_t4_in', length=1, delay_cost=1)
	S += c_qinv0_t4_in >= 15
	c_qinv0_t4_in += MM_in[1]

	c_qinv0_t4_mem0 = S.Task('c_qinv0_t4_mem0', length=1, delay_cost=1)
	S += c_qinv0_t4_mem0 >= 15
	c_qinv0_t4_mem0 += MAS_MEM[0]

	c_qinv0_t4_mem1 = S.Task('c_qinv0_t4_mem1', length=1, delay_cost=1)
	S += c_qinv0_t4_mem1 >= 15
	c_qinv0_t4_mem1 += MAS_MEM[3]

	c_qinv1__t0_in = S.Task('c_qinv1__t0_in', length=1, delay_cost=1)
	S += c_qinv1__t0_in >= 15
	c_qinv1__t0_in += MM_in[0]

	c_qinv1__t0_mem0 = S.Task('c_qinv1__t0_mem0', length=1, delay_cost=1)
	S += c_qinv1__t0_mem0 >= 15
	c_qinv1__t0_mem0 += MAIN_MEM_r[0]

	c_qinv1__t0_mem1 = S.Task('c_qinv1__t0_mem1', length=1, delay_cost=1)
	S += c_qinv1__t0_mem1 >= 15
	c_qinv1__t0_mem1 += MM_MEM[3]

	c_qinv0_t4 = S.Task('c_qinv0_t4', length=11, delay_cost=1)
	S += c_qinv0_t4 >= 16
	c_qinv0_t4 += MM[1]

	c_qinv1__t0 = S.Task('c_qinv1__t0', length=11, delay_cost=1)
	S += c_qinv1__t0 >= 16
	c_qinv1__t0 += MM[0]

	c_qinv1__t2_in = S.Task('c_qinv1__t2_in', length=1, delay_cost=1)
	S += c_qinv1__t2_in >= 16
	c_qinv1__t2_in += MAS_in[3]

	c_qinv1__t2_mem0 = S.Task('c_qinv1__t2_mem0', length=1, delay_cost=1)
	S += c_qinv1__t2_mem0 >= 16
	c_qinv1__t2_mem0 += MAIN_MEM_r[0]

	c_qinv1__t2_mem1 = S.Task('c_qinv1__t2_mem1', length=1, delay_cost=1)
	S += c_qinv1__t2_mem1 >= 16
	c_qinv1__t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t1_in = S.Task('c_qinv1__t1_in', length=1, delay_cost=1)
	S += c_qinv1__t1_in >= 17
	c_qinv1__t1_in += MM_in[0]

	c_qinv1__t1_mem0 = S.Task('c_qinv1__t1_mem0', length=1, delay_cost=1)
	S += c_qinv1__t1_mem0 >= 17
	c_qinv1__t1_mem0 += MAIN_MEM_r[0]

	c_qinv1__t1_mem1 = S.Task('c_qinv1__t1_mem1', length=1, delay_cost=1)
	S += c_qinv1__t1_mem1 >= 17
	c_qinv1__t1_mem1 += MM_MEM[1]

	c_qinv1__t2 = S.Task('c_qinv1__t2', length=2, delay_cost=1)
	S += c_qinv1__t2 >= 17
	c_qinv1__t2 += MAS[3]

	c0_t1_t2_in = S.Task('c0_t1_t2_in', length=1, delay_cost=1)
	S += c0_t1_t2_in >= 18
	c0_t1_t2_in += MAS_in[0]

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	S += c0_t1_t2_mem0 >= 18
	c0_t1_t2_mem0 += MAIN_MEM_r[0]

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	S += c0_t1_t2_mem1 >= 18
	c0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t1 = S.Task('c_qinv1__t1', length=11, delay_cost=1)
	S += c_qinv1__t1 >= 18
	c_qinv1__t1 += MM[0]

	c_qinv1__t4_in = S.Task('c_qinv1__t4_in', length=1, delay_cost=1)
	S += c_qinv1__t4_in >= 18
	c_qinv1__t4_in += MM_in[0]

	c_qinv1__t4_mem0 = S.Task('c_qinv1__t4_mem0', length=1, delay_cost=1)
	S += c_qinv1__t4_mem0 >= 18
	c_qinv1__t4_mem0 += MAS_MEM[6]

	c_qinv1__t4_mem1 = S.Task('c_qinv1__t4_mem1', length=1, delay_cost=1)
	S += c_qinv1__t4_mem1 >= 18
	c_qinv1__t4_mem1 += MAS_MEM[11]

	c0_t1_t2 = S.Task('c0_t1_t2', length=2, delay_cost=1)
	S += c0_t1_t2 >= 19
	c0_t1_t2 += MAS[0]

	c_qinv0_t1_in = S.Task('c_qinv0_t1_in', length=1, delay_cost=1)
	S += c_qinv0_t1_in >= 19
	c_qinv0_t1_in += MM_in[0]

	c_qinv0_t1_mem0 = S.Task('c_qinv0_t1_mem0', length=1, delay_cost=1)
	S += c_qinv0_t1_mem0 >= 19
	c_qinv0_t1_mem0 += MAIN_MEM_r[0]

	c_qinv0_t1_mem1 = S.Task('c_qinv0_t1_mem1', length=1, delay_cost=1)
	S += c_qinv0_t1_mem1 >= 19
	c_qinv0_t1_mem1 += MM_MEM[1]

	c_qinv1__t4 = S.Task('c_qinv1__t4', length=11, delay_cost=1)
	S += c_qinv1__t4 >= 19
	c_qinv1__t4 += MM[0]

	c_qinv0_t1 = S.Task('c_qinv0_t1', length=11, delay_cost=1)
	S += c_qinv0_t1 >= 20
	c_qinv0_t1 += MM[0]

	c_qinv1_0_in = S.Task('c_qinv1_0_in', length=1, delay_cost=1)
	S += c_qinv1_0_in >= 28
	c_qinv1_0_in += MAS_in[4]

	c_qinv1_0_mem0 = S.Task('c_qinv1_0_mem0', length=1, delay_cost=1)
	S += c_qinv1_0_mem0 >= 28
	c_qinv1_0_mem0 += MM_MEM[0]

	c_qinv1_0_mem1 = S.Task('c_qinv1_0_mem1', length=1, delay_cost=1)
	S += c_qinv1_0_mem1 >= 28
	c_qinv1_0_mem1 += MM_MEM[1]

	c_qinv1_0 = S.Task('c_qinv1_0', length=2, delay_cost=1)
	S += c_qinv1_0 >= 29
	c_qinv1_0 += MAS[4]

	c_qinv1__t5_in = S.Task('c_qinv1__t5_in', length=1, delay_cost=1)
	S += c_qinv1__t5_in >= 29
	c_qinv1__t5_in += MAS_in[5]

	c_qinv1__t5_mem0 = S.Task('c_qinv1__t5_mem0', length=1, delay_cost=1)
	S += c_qinv1__t5_mem0 >= 29
	c_qinv1__t5_mem0 += MM_MEM[0]

	c_qinv1__t5_mem1 = S.Task('c_qinv1__t5_mem1', length=1, delay_cost=1)
	S += c_qinv1__t5_mem1 >= 29
	c_qinv1__t5_mem1 += MM_MEM[1]

	c1_t1_t0_in = S.Task('c1_t1_t0_in', length=1, delay_cost=1)
	S += c1_t1_t0_in >= 30
	c1_t1_t0_in += MM_in[1]

	c1_t1_t0_mem0 = S.Task('c1_t1_t0_mem0', length=1, delay_cost=1)
	S += c1_t1_t0_mem0 >= 30
	c1_t1_t0_mem0 += MAIN_MEM_r[0]

	c1_t1_t0_mem1 = S.Task('c1_t1_t0_mem1', length=1, delay_cost=1)
	S += c1_t1_t0_mem1 >= 30
	c1_t1_t0_mem1 += MAS_MEM[9]

	c_qinv00_in = S.Task('c_qinv00_in', length=1, delay_cost=1)
	S += c_qinv00_in >= 30
	c_qinv00_in += MAS_in[3]

	c_qinv00_mem0 = S.Task('c_qinv00_mem0', length=1, delay_cost=1)
	S += c_qinv00_mem0 >= 30
	c_qinv00_mem0 += MM_MEM[2]

	c_qinv00_mem1 = S.Task('c_qinv00_mem1', length=1, delay_cost=1)
	S += c_qinv00_mem1 >= 30
	c_qinv00_mem1 += MM_MEM[1]

	c_qinv1__t5 = S.Task('c_qinv1__t5', length=2, delay_cost=1)
	S += c_qinv1__t5 >= 30
	c_qinv1__t5 += MAS[5]

	c1_t1_t0 = S.Task('c1_t1_t0', length=11, delay_cost=1)
	S += c1_t1_t0 >= 31
	c1_t1_t0 += MM[1]

	c2_t1_t0_in = S.Task('c2_t1_t0_in', length=1, delay_cost=1)
	S += c2_t1_t0_in >= 31
	c2_t1_t0_in += MM_in[0]

	c2_t1_t0_mem0 = S.Task('c2_t1_t0_mem0', length=1, delay_cost=1)
	S += c2_t1_t0_mem0 >= 31
	c2_t1_t0_mem0 += MAIN_MEM_r[0]

	c2_t1_t0_mem1 = S.Task('c2_t1_t0_mem1', length=1, delay_cost=1)
	S += c2_t1_t0_mem1 >= 31
	c2_t1_t0_mem1 += MAS_MEM[9]

	c_qinv00 = S.Task('c_qinv00', length=2, delay_cost=1)
	S += c_qinv00 >= 31
	c_qinv00 += MAS[3]

	c_qinv0_t5_in = S.Task('c_qinv0_t5_in', length=1, delay_cost=1)
	S += c_qinv0_t5_in >= 31
	c_qinv0_t5_in += MAS_in[1]

	c_qinv0_t5_mem0 = S.Task('c_qinv0_t5_mem0', length=1, delay_cost=1)
	S += c_qinv0_t5_mem0 >= 31
	c_qinv0_t5_mem0 += MM_MEM[2]

	c_qinv0_t5_mem1 = S.Task('c_qinv0_t5_mem1', length=1, delay_cost=1)
	S += c_qinv0_t5_mem1 >= 31
	c_qinv0_t5_mem1 += MM_MEM[1]

	c_qinv1_1_in = S.Task('c_qinv1_1_in', length=1, delay_cost=1)
	S += c_qinv1_1_in >= 31
	c_qinv1_1_in += MAS_in[2]

	c_qinv1_1_mem0 = S.Task('c_qinv1_1_mem0', length=1, delay_cost=1)
	S += c_qinv1_1_mem0 >= 31
	c_qinv1_1_mem0 += MM_MEM[0]

	c_qinv1_1_mem1 = S.Task('c_qinv1_1_mem1', length=1, delay_cost=1)
	S += c_qinv1_1_mem1 >= 31
	c_qinv1_1_mem1 += MAS_MEM[11]

	c1_t0_t0_in = S.Task('c1_t0_t0_in', length=1, delay_cost=1)
	S += c1_t0_t0_in >= 32
	c1_t0_t0_in += MM_in[1]

	c1_t0_t0_mem0 = S.Task('c1_t0_t0_mem0', length=1, delay_cost=1)
	S += c1_t0_t0_mem0 >= 32
	c1_t0_t0_mem0 += MAIN_MEM_r[0]

	c1_t0_t0_mem1 = S.Task('c1_t0_t0_mem1', length=1, delay_cost=1)
	S += c1_t0_t0_mem1 >= 32
	c1_t0_t0_mem1 += MAS_MEM[7]

	c2_t1_t0 = S.Task('c2_t1_t0', length=11, delay_cost=1)
	S += c2_t1_t0 >= 32
	c2_t1_t0 += MM[0]

	c2_t30_in = S.Task('c2_t30_in', length=1, delay_cost=1)
	S += c2_t30_in >= 32
	c2_t30_in += MAS_in[5]

	c2_t30_mem0 = S.Task('c2_t30_mem0', length=1, delay_cost=1)
	S += c2_t30_mem0 >= 32
	c2_t30_mem0 += MAS_MEM[6]

	c2_t30_mem1 = S.Task('c2_t30_mem1', length=1, delay_cost=1)
	S += c2_t30_mem1 >= 32
	c2_t30_mem1 += MAS_MEM[9]

	c_qinv0_t5 = S.Task('c_qinv0_t5', length=2, delay_cost=1)
	S += c_qinv0_t5 >= 32
	c_qinv0_t5 += MAS[1]

	c_qinv1_1 = S.Task('c_qinv1_1', length=2, delay_cost=1)
	S += c_qinv1_1 >= 32
	c_qinv1_1 += MAS[2]

	c1_t0_t0 = S.Task('c1_t0_t0', length=11, delay_cost=1)
	S += c1_t0_t0 >= 33
	c1_t0_t0 += MM[1]

	c1_t1_t3_in = S.Task('c1_t1_t3_in', length=1, delay_cost=1)
	S += c1_t1_t3_in >= 33
	c1_t1_t3_in += MAS_in[2]

	c1_t1_t3_mem0 = S.Task('c1_t1_t3_mem0', length=1, delay_cost=1)
	S += c1_t1_t3_mem0 >= 33
	c1_t1_t3_mem0 += MAS_MEM[8]

	c1_t1_t3_mem1 = S.Task('c1_t1_t3_mem1', length=1, delay_cost=1)
	S += c1_t1_t3_mem1 >= 33
	c1_t1_t3_mem1 += MAS_MEM[5]

	c1_t30_in = S.Task('c1_t30_in', length=1, delay_cost=1)
	S += c1_t30_in >= 33
	c1_t30_in += MAS_in[1]

	c1_t30_mem0 = S.Task('c1_t30_mem0', length=1, delay_cost=1)
	S += c1_t30_mem0 >= 33
	c1_t30_mem0 += MAS_MEM[6]

	c1_t30_mem1 = S.Task('c1_t30_mem1', length=1, delay_cost=1)
	S += c1_t30_mem1 >= 33
	c1_t30_mem1 += MAS_MEM[9]

	c2_t0_t0_in = S.Task('c2_t0_t0_in', length=1, delay_cost=1)
	S += c2_t0_t0_in >= 33
	c2_t0_t0_in += MM_in[1]

	c2_t0_t0_mem0 = S.Task('c2_t0_t0_mem0', length=1, delay_cost=1)
	S += c2_t0_t0_mem0 >= 33
	c2_t0_t0_mem0 += MAIN_MEM_r[0]

	c2_t0_t0_mem1 = S.Task('c2_t0_t0_mem1', length=1, delay_cost=1)
	S += c2_t0_t0_mem1 >= 33
	c2_t0_t0_mem1 += MAS_MEM[7]

	c2_t30 = S.Task('c2_t30', length=2, delay_cost=1)
	S += c2_t30 >= 33
	c2_t30 += MAS[5]

	c_qinv01_in = S.Task('c_qinv01_in', length=1, delay_cost=1)
	S += c_qinv01_in >= 33
	c_qinv01_in += MAS_in[0]

	c_qinv01_mem0 = S.Task('c_qinv01_mem0', length=1, delay_cost=1)
	S += c_qinv01_mem0 >= 33
	c_qinv01_mem0 += MM_MEM[2]

	c_qinv01_mem1 = S.Task('c_qinv01_mem1', length=1, delay_cost=1)
	S += c_qinv01_mem1 >= 33
	c_qinv01_mem1 += MAS_MEM[3]

	c0_t0_t0_in = S.Task('c0_t0_t0_in', length=1, delay_cost=1)
	S += c0_t0_t0_in >= 34
	c0_t0_t0_in += MM_in[1]

	c0_t0_t0_mem0 = S.Task('c0_t0_t0_mem0', length=1, delay_cost=1)
	S += c0_t0_t0_mem0 >= 34
	c0_t0_t0_mem0 += MAIN_MEM_r[0]

	c0_t0_t0_mem1 = S.Task('c0_t0_t0_mem1', length=1, delay_cost=1)
	S += c0_t0_t0_mem1 >= 34
	c0_t0_t0_mem1 += MAS_MEM[7]

	c0_t30_in = S.Task('c0_t30_in', length=1, delay_cost=1)
	S += c0_t30_in >= 34
	c0_t30_in += MAS_in[5]

	c0_t30_mem0 = S.Task('c0_t30_mem0', length=1, delay_cost=1)
	S += c0_t30_mem0 >= 34
	c0_t30_mem0 += MAS_MEM[6]

	c0_t30_mem1 = S.Task('c0_t30_mem1', length=1, delay_cost=1)
	S += c0_t30_mem1 >= 34
	c0_t30_mem1 += MAS_MEM[9]

	c1_t1_t3 = S.Task('c1_t1_t3', length=2, delay_cost=1)
	S += c1_t1_t3 >= 34
	c1_t1_t3 += MAS[2]

	c1_t30 = S.Task('c1_t30', length=2, delay_cost=1)
	S += c1_t30 >= 34
	c1_t30 += MAS[1]

	c2_t0_t0 = S.Task('c2_t0_t0', length=11, delay_cost=1)
	S += c2_t0_t0 >= 34
	c2_t0_t0 += MM[1]

	c2_t1_t3_in = S.Task('c2_t1_t3_in', length=1, delay_cost=1)
	S += c2_t1_t3_in >= 34
	c2_t1_t3_in += MAS_in[2]

	c2_t1_t3_mem0 = S.Task('c2_t1_t3_mem0', length=1, delay_cost=1)
	S += c2_t1_t3_mem0 >= 34
	c2_t1_t3_mem0 += MAS_MEM[8]

	c2_t1_t3_mem1 = S.Task('c2_t1_t3_mem1', length=1, delay_cost=1)
	S += c2_t1_t3_mem1 >= 34
	c2_t1_t3_mem1 += MAS_MEM[5]

	c2_t4_t0_in = S.Task('c2_t4_t0_in', length=1, delay_cost=1)
	S += c2_t4_t0_in >= 34
	c2_t4_t0_in += MM_in[0]

	c2_t4_t0_mem0 = S.Task('c2_t4_t0_mem0', length=1, delay_cost=1)
	S += c2_t4_t0_mem0 >= 34
	c2_t4_t0_mem0 += MAS_MEM[10]

	c2_t4_t0_mem1 = S.Task('c2_t4_t0_mem1', length=1, delay_cost=1)
	S += c2_t4_t0_mem1 >= 34
	c2_t4_t0_mem1 += MAS_MEM[11]

	c_qinv01 = S.Task('c_qinv01', length=2, delay_cost=1)
	S += c_qinv01 >= 34
	c_qinv01 += MAS[0]

	c0_t0_t0 = S.Task('c0_t0_t0', length=11, delay_cost=1)
	S += c0_t0_t0 >= 35
	c0_t0_t0 += MM[1]

	c0_t1_t0_in = S.Task('c0_t1_t0_in', length=1, delay_cost=1)
	S += c0_t1_t0_in >= 35
	c0_t1_t0_in += MM_in[1]

	c0_t1_t0_mem0 = S.Task('c0_t1_t0_mem0', length=1, delay_cost=1)
	S += c0_t1_t0_mem0 >= 35
	c0_t1_t0_mem0 += MAIN_MEM_r[0]

	c0_t1_t0_mem1 = S.Task('c0_t1_t0_mem1', length=1, delay_cost=1)
	S += c0_t1_t0_mem1 >= 35
	c0_t1_t0_mem1 += MAS_MEM[9]

	c0_t30 = S.Task('c0_t30', length=2, delay_cost=1)
	S += c0_t30 >= 35
	c0_t30 += MAS[5]

	c1_t31_in = S.Task('c1_t31_in', length=1, delay_cost=1)
	S += c1_t31_in >= 35
	c1_t31_in += MAS_in[4]

	c1_t31_mem0 = S.Task('c1_t31_mem0', length=1, delay_cost=1)
	S += c1_t31_mem0 >= 35
	c1_t31_mem0 += MAS_MEM[0]

	c1_t31_mem1 = S.Task('c1_t31_mem1', length=1, delay_cost=1)
	S += c1_t31_mem1 >= 35
	c1_t31_mem1 += MAS_MEM[5]

	c1_t4_t0_in = S.Task('c1_t4_t0_in', length=1, delay_cost=1)
	S += c1_t4_t0_in >= 35
	c1_t4_t0_in += MM_in[0]

	c1_t4_t0_mem0 = S.Task('c1_t4_t0_mem0', length=1, delay_cost=1)
	S += c1_t4_t0_mem0 >= 35
	c1_t4_t0_mem0 += MAS_MEM[8]

	c1_t4_t0_mem1 = S.Task('c1_t4_t0_mem1', length=1, delay_cost=1)
	S += c1_t4_t0_mem1 >= 35
	c1_t4_t0_mem1 += MAS_MEM[3]

	c2_t0_t3_in = S.Task('c2_t0_t3_in', length=1, delay_cost=1)
	S += c2_t0_t3_in >= 35
	c2_t0_t3_in += MAS_in[2]

	c2_t0_t3_mem0 = S.Task('c2_t0_t3_mem0', length=1, delay_cost=1)
	S += c2_t0_t3_mem0 >= 35
	c2_t0_t3_mem0 += MAS_MEM[6]

	c2_t0_t3_mem1 = S.Task('c2_t0_t3_mem1', length=1, delay_cost=1)
	S += c2_t0_t3_mem1 >= 35
	c2_t0_t3_mem1 += MAS_MEM[1]

	c2_t1_t3 = S.Task('c2_t1_t3', length=2, delay_cost=1)
	S += c2_t1_t3 >= 35
	c2_t1_t3 += MAS[2]

	c2_t4_t0 = S.Task('c2_t4_t0', length=11, delay_cost=1)
	S += c2_t4_t0 >= 35
	c2_t4_t0 += MM[0]

	c0_t1_t0 = S.Task('c0_t1_t0', length=11, delay_cost=1)
	S += c0_t1_t0 >= 36
	c0_t1_t0 += MM[1]

	c0_t4_t0_in = S.Task('c0_t4_t0_in', length=1, delay_cost=1)
	S += c0_t4_t0_in >= 36
	c0_t4_t0_in += MM_in[0]

	c0_t4_t0_mem0 = S.Task('c0_t4_t0_mem0', length=1, delay_cost=1)
	S += c0_t4_t0_mem0 >= 36
	c0_t4_t0_mem0 += MAS_MEM[4]

	c0_t4_t0_mem1 = S.Task('c0_t4_t0_mem1', length=1, delay_cost=1)
	S += c0_t4_t0_mem1 >= 36
	c0_t4_t0_mem1 += MAS_MEM[11]

	c1_t0_t3_in = S.Task('c1_t0_t3_in', length=1, delay_cost=1)
	S += c1_t0_t3_in >= 36
	c1_t0_t3_in += MAS_in[5]

	c1_t0_t3_mem0 = S.Task('c1_t0_t3_mem0', length=1, delay_cost=1)
	S += c1_t0_t3_mem0 >= 36
	c1_t0_t3_mem0 += MAS_MEM[6]

	c1_t0_t3_mem1 = S.Task('c1_t0_t3_mem1', length=1, delay_cost=1)
	S += c1_t0_t3_mem1 >= 36
	c1_t0_t3_mem1 += MAS_MEM[1]

	c1_t31 = S.Task('c1_t31', length=2, delay_cost=1)
	S += c1_t31 >= 36
	c1_t31 += MAS[4]

	c1_t4_t0 = S.Task('c1_t4_t0', length=11, delay_cost=1)
	S += c1_t4_t0 >= 36
	c1_t4_t0 += MM[0]

	c2_t0_t3 = S.Task('c2_t0_t3', length=2, delay_cost=1)
	S += c2_t0_t3 >= 36
	c2_t0_t3 += MAS[2]

	c2_t1_t1_in = S.Task('c2_t1_t1_in', length=1, delay_cost=1)
	S += c2_t1_t1_in >= 36
	c2_t1_t1_in += MM_in[1]

	c2_t1_t1_mem0 = S.Task('c2_t1_t1_mem0', length=1, delay_cost=1)
	S += c2_t1_t1_mem0 >= 36
	c2_t1_t1_mem0 += MAIN_MEM_r[0]

	c2_t1_t1_mem1 = S.Task('c2_t1_t1_mem1', length=1, delay_cost=1)
	S += c2_t1_t1_mem1 >= 36
	c2_t1_t1_mem1 += MAS_MEM[5]

	c0_t31_in = S.Task('c0_t31_in', length=1, delay_cost=1)
	S += c0_t31_in >= 37
	c0_t31_in += MAS_in[2]

	c0_t31_mem0 = S.Task('c0_t31_mem0', length=1, delay_cost=1)
	S += c0_t31_mem0 >= 37
	c0_t31_mem0 += MAS_MEM[0]

	c0_t31_mem1 = S.Task('c0_t31_mem1', length=1, delay_cost=1)
	S += c0_t31_mem1 >= 37
	c0_t31_mem1 += MAS_MEM[5]

	c0_t4_t0 = S.Task('c0_t4_t0', length=11, delay_cost=1)
	S += c0_t4_t0 >= 37
	c0_t4_t0 += MM[0]

	c1_t0_t1_in = S.Task('c1_t0_t1_in', length=1, delay_cost=1)
	S += c1_t0_t1_in >= 37
	c1_t0_t1_in += MM_in[0]

	c1_t0_t1_mem0 = S.Task('c1_t0_t1_mem0', length=1, delay_cost=1)
	S += c1_t0_t1_mem0 >= 37
	c1_t0_t1_mem0 += MAIN_MEM_r[0]

	c1_t0_t1_mem1 = S.Task('c1_t0_t1_mem1', length=1, delay_cost=1)
	S += c1_t0_t1_mem1 >= 37
	c1_t0_t1_mem1 += MAS_MEM[1]

	c1_t0_t3 = S.Task('c1_t0_t3', length=2, delay_cost=1)
	S += c1_t0_t3 >= 37
	c1_t0_t3 += MAS[5]

	c1_t4_t1_in = S.Task('c1_t4_t1_in', length=1, delay_cost=1)
	S += c1_t4_t1_in >= 37
	c1_t4_t1_in += MM_in[1]

	c1_t4_t1_mem0 = S.Task('c1_t4_t1_mem0', length=1, delay_cost=1)
	S += c1_t4_t1_mem0 >= 37
	c1_t4_t1_mem0 += MAS_MEM[4]

	c1_t4_t1_mem1 = S.Task('c1_t4_t1_mem1', length=1, delay_cost=1)
	S += c1_t4_t1_mem1 >= 37
	c1_t4_t1_mem1 += MAS_MEM[9]

	c2_t1_t1 = S.Task('c2_t1_t1', length=11, delay_cost=1)
	S += c2_t1_t1 >= 37
	c2_t1_t1 += MM[1]

	c0_t0_t3_in = S.Task('c0_t0_t3_in', length=1, delay_cost=1)
	S += c0_t0_t3_in >= 38
	c0_t0_t3_in += MAS_in[2]

	c0_t0_t3_mem0 = S.Task('c0_t0_t3_mem0', length=1, delay_cost=1)
	S += c0_t0_t3_mem0 >= 38
	c0_t0_t3_mem0 += MAS_MEM[6]

	c0_t0_t3_mem1 = S.Task('c0_t0_t3_mem1', length=1, delay_cost=1)
	S += c0_t0_t3_mem1 >= 38
	c0_t0_t3_mem1 += MAS_MEM[1]

	c0_t1_t1_in = S.Task('c0_t1_t1_in', length=1, delay_cost=1)
	S += c0_t1_t1_in >= 38
	c0_t1_t1_in += MM_in[0]

	c0_t1_t1_mem0 = S.Task('c0_t1_t1_mem0', length=1, delay_cost=1)
	S += c0_t1_t1_mem0 >= 38
	c0_t1_t1_mem0 += MAIN_MEM_r[0]

	c0_t1_t1_mem1 = S.Task('c0_t1_t1_mem1', length=1, delay_cost=1)
	S += c0_t1_t1_mem1 >= 38
	c0_t1_t1_mem1 += MAS_MEM[5]

	c0_t31 = S.Task('c0_t31', length=2, delay_cost=1)
	S += c0_t31 >= 38
	c0_t31 += MAS[2]

	c1_t0_t1 = S.Task('c1_t0_t1', length=11, delay_cost=1)
	S += c1_t0_t1 >= 38
	c1_t0_t1 += MM[0]

	c1_t4_t1 = S.Task('c1_t4_t1', length=11, delay_cost=1)
	S += c1_t4_t1 >= 38
	c1_t4_t1 += MM[1]

	c1_t4_t3_in = S.Task('c1_t4_t3_in', length=1, delay_cost=1)
	S += c1_t4_t3_in >= 38
	c1_t4_t3_in += MAS_in[5]

	c1_t4_t3_mem0 = S.Task('c1_t4_t3_mem0', length=1, delay_cost=1)
	S += c1_t4_t3_mem0 >= 38
	c1_t4_t3_mem0 += MAS_MEM[2]

	c1_t4_t3_mem1 = S.Task('c1_t4_t3_mem1', length=1, delay_cost=1)
	S += c1_t4_t3_mem1 >= 38
	c1_t4_t3_mem1 += MAS_MEM[9]

	c0_t0_t3 = S.Task('c0_t0_t3', length=2, delay_cost=1)
	S += c0_t0_t3 >= 39
	c0_t0_t3 += MAS[2]

	c0_t1_t1 = S.Task('c0_t1_t1', length=11, delay_cost=1)
	S += c0_t1_t1 >= 39
	c0_t1_t1 += MM[0]

	c0_t1_t3_in = S.Task('c0_t1_t3_in', length=1, delay_cost=1)
	S += c0_t1_t3_in >= 39
	c0_t1_t3_in += MAS_in[5]

	c0_t1_t3_mem0 = S.Task('c0_t1_t3_mem0', length=1, delay_cost=1)
	S += c0_t1_t3_mem0 >= 39
	c0_t1_t3_mem0 += MAS_MEM[8]

	c0_t1_t3_mem1 = S.Task('c0_t1_t3_mem1', length=1, delay_cost=1)
	S += c0_t1_t3_mem1 >= 39
	c0_t1_t3_mem1 += MAS_MEM[5]

	c1_t0_t4_in = S.Task('c1_t0_t4_in', length=1, delay_cost=1)
	S += c1_t0_t4_in >= 39
	c1_t0_t4_in += MM_in[0]

	c1_t0_t4_mem0 = S.Task('c1_t0_t4_mem0', length=1, delay_cost=1)
	S += c1_t0_t4_mem0 >= 39
	c1_t0_t4_mem0 += MAS_MEM[0]

	c1_t0_t4_mem1 = S.Task('c1_t0_t4_mem1', length=1, delay_cost=1)
	S += c1_t0_t4_mem1 >= 39
	c1_t0_t4_mem1 += MAS_MEM[11]

	c1_t4_t3 = S.Task('c1_t4_t3', length=2, delay_cost=1)
	S += c1_t4_t3 >= 39
	c1_t4_t3 += MAS[5]

	c2_t0_t1_in = S.Task('c2_t0_t1_in', length=1, delay_cost=1)
	S += c2_t0_t1_in >= 39
	c2_t0_t1_in += MM_in[1]

	c2_t0_t1_mem0 = S.Task('c2_t0_t1_mem0', length=1, delay_cost=1)
	S += c2_t0_t1_mem0 >= 39
	c2_t0_t1_mem0 += MAIN_MEM_r[0]

	c2_t0_t1_mem1 = S.Task('c2_t0_t1_mem1', length=1, delay_cost=1)
	S += c2_t0_t1_mem1 >= 39
	c2_t0_t1_mem1 += MAS_MEM[1]

	c0_t0_t1_in = S.Task('c0_t0_t1_in', length=1, delay_cost=1)
	S += c0_t0_t1_in >= 40
	c0_t0_t1_in += MM_in[0]

	c0_t0_t1_mem0 = S.Task('c0_t0_t1_mem0', length=1, delay_cost=1)
	S += c0_t0_t1_mem0 >= 40
	c0_t0_t1_mem0 += MAIN_MEM_r[0]

	c0_t0_t1_mem1 = S.Task('c0_t0_t1_mem1', length=1, delay_cost=1)
	S += c0_t0_t1_mem1 >= 40
	c0_t0_t1_mem1 += MAS_MEM[1]

	c0_t1_t3 = S.Task('c0_t1_t3', length=2, delay_cost=1)
	S += c0_t1_t3 >= 40
	c0_t1_t3 += MAS[5]

	c1_t0_t4 = S.Task('c1_t0_t4', length=11, delay_cost=1)
	S += c1_t0_t4 >= 40
	c1_t0_t4 += MM[0]

	c1_t4_t4_in = S.Task('c1_t4_t4_in', length=1, delay_cost=1)
	S += c1_t4_t4_in >= 40
	c1_t4_t4_in += MM_in[1]

	c1_t4_t4_mem0 = S.Task('c1_t4_t4_mem0', length=1, delay_cost=1)
	S += c1_t4_t4_mem0 >= 40
	c1_t4_t4_mem0 += MAS_MEM[10]

	c1_t4_t4_mem1 = S.Task('c1_t4_t4_mem1', length=1, delay_cost=1)
	S += c1_t4_t4_mem1 >= 40
	c1_t4_t4_mem1 += MAS_MEM[11]

	c2_t0_t1 = S.Task('c2_t0_t1', length=11, delay_cost=1)
	S += c2_t0_t1 >= 40
	c2_t0_t1 += MM[1]

	c2_t31_in = S.Task('c2_t31_in', length=1, delay_cost=1)
	S += c2_t31_in >= 40
	c2_t31_in += MAS_in[5]

	c2_t31_mem0 = S.Task('c2_t31_mem0', length=1, delay_cost=1)
	S += c2_t31_mem0 >= 40
	c2_t31_mem0 += MAS_MEM[0]

	c2_t31_mem1 = S.Task('c2_t31_mem1', length=1, delay_cost=1)
	S += c2_t31_mem1 >= 40
	c2_t31_mem1 += MAS_MEM[5]

	c0_t0_t1 = S.Task('c0_t0_t1', length=11, delay_cost=1)
	S += c0_t0_t1 >= 41
	c0_t0_t1 += MM[0]

	c0_t1_t4_in = S.Task('c0_t1_t4_in', length=1, delay_cost=1)
	S += c0_t1_t4_in >= 41
	c0_t1_t4_in += MM_in[1]

	c0_t1_t4_mem0 = S.Task('c0_t1_t4_mem0', length=1, delay_cost=1)
	S += c0_t1_t4_mem0 >= 41
	c0_t1_t4_mem0 += MAS_MEM[0]

	c0_t1_t4_mem1 = S.Task('c0_t1_t4_mem1', length=1, delay_cost=1)
	S += c0_t1_t4_mem1 >= 41
	c0_t1_t4_mem1 += MAS_MEM[11]

	c1_t1_t1_in = S.Task('c1_t1_t1_in', length=1, delay_cost=1)
	S += c1_t1_t1_in >= 41
	c1_t1_t1_in += MM_in[0]

	c1_t1_t1_mem0 = S.Task('c1_t1_t1_mem0', length=1, delay_cost=1)
	S += c1_t1_t1_mem0 >= 41
	c1_t1_t1_mem0 += MAIN_MEM_r[0]

	c1_t1_t1_mem1 = S.Task('c1_t1_t1_mem1', length=1, delay_cost=1)
	S += c1_t1_t1_mem1 >= 41
	c1_t1_t1_mem1 += MAS_MEM[5]

	c1_t4_t4 = S.Task('c1_t4_t4', length=11, delay_cost=1)
	S += c1_t4_t4 >= 41
	c1_t4_t4 += MM[1]

	c2_t31 = S.Task('c2_t31', length=2, delay_cost=1)
	S += c2_t31 >= 41
	c2_t31 += MAS[5]

	c0_t1_t4 = S.Task('c0_t1_t4', length=11, delay_cost=1)
	S += c0_t1_t4 >= 42
	c0_t1_t4 += MM[1]

	c0_t4_t3_in = S.Task('c0_t4_t3_in', length=1, delay_cost=1)
	S += c0_t4_t3_in >= 42
	c0_t4_t3_in += MAS_in[1]

	c0_t4_t3_mem0 = S.Task('c0_t4_t3_mem0', length=1, delay_cost=1)
	S += c0_t4_t3_mem0 >= 42
	c0_t4_t3_mem0 += MAS_MEM[10]

	c0_t4_t3_mem1 = S.Task('c0_t4_t3_mem1', length=1, delay_cost=1)
	S += c0_t4_t3_mem1 >= 42
	c0_t4_t3_mem1 += MAS_MEM[5]

	c1_t1_t1 = S.Task('c1_t1_t1', length=11, delay_cost=1)
	S += c1_t1_t1 >= 42
	c1_t1_t1 += MM[0]

	c2_t4_t1_in = S.Task('c2_t4_t1_in', length=1, delay_cost=1)
	S += c2_t4_t1_in >= 42
	c2_t4_t1_in += MM_in[1]

	c2_t4_t1_mem0 = S.Task('c2_t4_t1_mem0', length=1, delay_cost=1)
	S += c2_t4_t1_mem0 >= 42
	c2_t4_t1_mem0 += MAS_MEM[8]

	c2_t4_t1_mem1 = S.Task('c2_t4_t1_mem1', length=1, delay_cost=1)
	S += c2_t4_t1_mem1 >= 42
	c2_t4_t1_mem1 += MAS_MEM[11]

	c0_t4_t1_in = S.Task('c0_t4_t1_in', length=1, delay_cost=1)
	S += c0_t4_t1_in >= 43
	c0_t4_t1_in += MM_in[0]

	c0_t4_t1_mem0 = S.Task('c0_t4_t1_mem0', length=1, delay_cost=1)
	S += c0_t4_t1_mem0 >= 43
	c0_t4_t1_mem0 += MAS_MEM[4]

	c0_t4_t1_mem1 = S.Task('c0_t4_t1_mem1', length=1, delay_cost=1)
	S += c0_t4_t1_mem1 >= 43
	c0_t4_t1_mem1 += MAS_MEM[5]

	c0_t4_t3 = S.Task('c0_t4_t3', length=2, delay_cost=1)
	S += c0_t4_t3 >= 43
	c0_t4_t3 += MAS[1]

	c2_t4_t1 = S.Task('c2_t4_t1', length=11, delay_cost=1)
	S += c2_t4_t1 >= 43
	c2_t4_t1 += MM[1]

	c2_t4_t3_in = S.Task('c2_t4_t3_in', length=1, delay_cost=1)
	S += c2_t4_t3_in >= 43
	c2_t4_t3_in += MAS_in[1]

	c2_t4_t3_mem0 = S.Task('c2_t4_t3_mem0', length=1, delay_cost=1)
	S += c2_t4_t3_mem0 >= 43
	c2_t4_t3_mem0 += MAS_MEM[10]

	c2_t4_t3_mem1 = S.Task('c2_t4_t3_mem1', length=1, delay_cost=1)
	S += c2_t4_t3_mem1 >= 43
	c2_t4_t3_mem1 += MAS_MEM[11]

	c0_t4_t1 = S.Task('c0_t4_t1', length=11, delay_cost=1)
	S += c0_t4_t1 >= 44
	c0_t4_t1 += MM[0]

	c0_t4_t4_in = S.Task('c0_t4_t4_in', length=1, delay_cost=1)
	S += c0_t4_t4_in >= 44
	c0_t4_t4_in += MM_in[1]

	c0_t4_t4_mem0 = S.Task('c0_t4_t4_mem0', length=1, delay_cost=1)
	S += c0_t4_t4_mem0 >= 44
	c0_t4_t4_mem0 += MAS_MEM[8]

	c0_t4_t4_mem1 = S.Task('c0_t4_t4_mem1', length=1, delay_cost=1)
	S += c0_t4_t4_mem1 >= 44
	c0_t4_t4_mem1 += MAS_MEM[3]

	c2_t0_t4_in = S.Task('c2_t0_t4_in', length=1, delay_cost=1)
	S += c2_t0_t4_in >= 44
	c2_t0_t4_in += MM_in[0]

	c2_t0_t4_mem0 = S.Task('c2_t0_t4_mem0', length=1, delay_cost=1)
	S += c2_t0_t4_mem0 >= 44
	c2_t0_t4_mem0 += MAS_MEM[10]

	c2_t0_t4_mem1 = S.Task('c2_t0_t4_mem1', length=1, delay_cost=1)
	S += c2_t0_t4_mem1 >= 44
	c2_t0_t4_mem1 += MAS_MEM[5]

	c2_t4_t3 = S.Task('c2_t4_t3', length=2, delay_cost=1)
	S += c2_t4_t3 >= 44
	c2_t4_t3 += MAS[1]

	c0_t4_t4 = S.Task('c0_t4_t4', length=11, delay_cost=1)
	S += c0_t4_t4 >= 45
	c0_t4_t4 += MM[1]

	c2_t0_t4 = S.Task('c2_t0_t4', length=11, delay_cost=1)
	S += c2_t0_t4 >= 45
	c2_t0_t4 += MM[0]

	c2_t1_t4_in = S.Task('c2_t1_t4_in', length=1, delay_cost=1)
	S += c2_t1_t4_in >= 45
	c2_t1_t4_in += MM_in[1]

	c2_t1_t4_mem0 = S.Task('c2_t1_t4_mem0', length=1, delay_cost=1)
	S += c2_t1_t4_mem0 >= 45
	c2_t1_t4_mem0 += MAS_MEM[0]

	c2_t1_t4_mem1 = S.Task('c2_t1_t4_mem1', length=1, delay_cost=1)
	S += c2_t1_t4_mem1 >= 45
	c2_t1_t4_mem1 += MAS_MEM[5]

	c2_t4_t4_in = S.Task('c2_t4_t4_in', length=1, delay_cost=1)
	S += c2_t4_t4_in >= 45
	c2_t4_t4_in += MM_in[0]

	c2_t4_t4_mem0 = S.Task('c2_t4_t4_mem0', length=1, delay_cost=1)
	S += c2_t4_t4_mem0 >= 45
	c2_t4_t4_mem0 += MAS_MEM[10]

	c2_t4_t4_mem1 = S.Task('c2_t4_t4_mem1', length=1, delay_cost=1)
	S += c2_t4_t4_mem1 >= 45
	c2_t4_t4_mem1 += MAS_MEM[3]

	c0_t0_t4_in = S.Task('c0_t0_t4_in', length=1, delay_cost=1)
	S += c0_t0_t4_in >= 46
	c0_t0_t4_in += MM_in[1]

	c0_t0_t4_mem0 = S.Task('c0_t0_t4_mem0', length=1, delay_cost=1)
	S += c0_t0_t4_mem0 >= 46
	c0_t0_t4_mem0 += MAS_MEM[2]

	c0_t0_t4_mem1 = S.Task('c0_t0_t4_mem1', length=1, delay_cost=1)
	S += c0_t0_t4_mem1 >= 46
	c0_t0_t4_mem1 += MAS_MEM[5]

	c2_t1_t4 = S.Task('c2_t1_t4', length=11, delay_cost=1)
	S += c2_t1_t4 >= 46
	c2_t1_t4 += MM[1]

	c2_t4_t4 = S.Task('c2_t4_t4', length=11, delay_cost=1)
	S += c2_t4_t4 >= 46
	c2_t4_t4 += MM[0]

	c0_t0_t4 = S.Task('c0_t0_t4', length=11, delay_cost=1)
	S += c0_t0_t4 >= 47
	c0_t0_t4 += MM[1]

	c1_t1_t4_in = S.Task('c1_t1_t4_in', length=1, delay_cost=1)
	S += c1_t1_t4_in >= 47
	c1_t1_t4_in += MM_in[0]

	c1_t1_t4_mem0 = S.Task('c1_t1_t4_mem0', length=1, delay_cost=1)
	S += c1_t1_t4_mem0 >= 47
	c1_t1_t4_mem0 += MAS_MEM[2]

	c1_t1_t4_mem1 = S.Task('c1_t1_t4_mem1', length=1, delay_cost=1)
	S += c1_t1_t4_mem1 >= 47
	c1_t1_t4_mem1 += MAS_MEM[5]

	c2_t10_in = S.Task('c2_t10_in', length=1, delay_cost=1)
	S += c2_t10_in >= 47
	c2_t10_in += MAS_in[3]

	c2_t10_mem0 = S.Task('c2_t10_mem0', length=1, delay_cost=1)
	S += c2_t10_mem0 >= 47
	c2_t10_mem0 += MM_MEM[2]

	c2_t10_mem1 = S.Task('c2_t10_mem1', length=1, delay_cost=1)
	S += c2_t10_mem1 >= 47
	c2_t10_mem1 += MM_MEM[1]

	c2_t1_t5_in = S.Task('c2_t1_t5_in', length=1, delay_cost=1)
	S += c2_t1_t5_in >= 47
	c2_t1_t5_in += MAS_in[0]

	c2_t1_t5_mem0 = S.Task('c2_t1_t5_mem0', length=1, delay_cost=1)
	S += c2_t1_t5_mem0 >= 47
	c2_t1_t5_mem0 += MM_MEM[0]

	c2_t1_t5_mem1 = S.Task('c2_t1_t5_mem1', length=1, delay_cost=1)
	S += c2_t1_t5_mem1 >= 47
	c2_t1_t5_mem1 += MM_MEM[3]

	c1_t0_t5_in = S.Task('c1_t0_t5_in', length=1, delay_cost=1)
	S += c1_t0_t5_in >= 48
	c1_t0_t5_in += MAS_in[0]

	c1_t0_t5_mem0 = S.Task('c1_t0_t5_mem0', length=1, delay_cost=1)
	S += c1_t0_t5_mem0 >= 48
	c1_t0_t5_mem0 += MM_MEM[2]

	c1_t0_t5_mem1 = S.Task('c1_t0_t5_mem1', length=1, delay_cost=1)
	S += c1_t0_t5_mem1 >= 48
	c1_t0_t5_mem1 += MM_MEM[1]

	c1_t1_t4 = S.Task('c1_t1_t4', length=11, delay_cost=1)
	S += c1_t1_t4 >= 48
	c1_t1_t4 += MM[0]

	c1_t4_t5_in = S.Task('c1_t4_t5_in', length=1, delay_cost=1)
	S += c1_t4_t5_in >= 48
	c1_t4_t5_in += MAS_in[2]

	c1_t4_t5_mem0 = S.Task('c1_t4_t5_mem0', length=1, delay_cost=1)
	S += c1_t4_t5_mem0 >= 48
	c1_t4_t5_mem0 += MM_MEM[0]

	c1_t4_t5_mem1 = S.Task('c1_t4_t5_mem1', length=1, delay_cost=1)
	S += c1_t4_t5_mem1 >= 48
	c1_t4_t5_mem1 += MM_MEM[3]

	c2_t10 = S.Task('c2_t10', length=2, delay_cost=1)
	S += c2_t10 >= 48
	c2_t10 += MAS[3]

	c2_t1_t5 = S.Task('c2_t1_t5', length=2, delay_cost=1)
	S += c2_t1_t5 >= 48
	c2_t1_t5 += MAS[0]

	c0_t10_in = S.Task('c0_t10_in', length=1, delay_cost=1)
	S += c0_t10_in >= 49
	c0_t10_in += MAS_in[3]

	c0_t10_mem0 = S.Task('c0_t10_mem0', length=1, delay_cost=1)
	S += c0_t10_mem0 >= 49
	c0_t10_mem0 += MM_MEM[0]

	c0_t10_mem1 = S.Task('c0_t10_mem1', length=1, delay_cost=1)
	S += c0_t10_mem1 >= 49
	c0_t10_mem1 += MM_MEM[3]

	c0_t1_t5_in = S.Task('c0_t1_t5_in', length=1, delay_cost=1)
	S += c0_t1_t5_in >= 49
	c0_t1_t5_in += MAS_in[2]

	c0_t1_t5_mem0 = S.Task('c0_t1_t5_mem0', length=1, delay_cost=1)
	S += c0_t1_t5_mem0 >= 49
	c0_t1_t5_mem0 += MM_MEM[2]

	c0_t1_t5_mem1 = S.Task('c0_t1_t5_mem1', length=1, delay_cost=1)
	S += c0_t1_t5_mem1 >= 49
	c0_t1_t5_mem1 += MM_MEM[1]

	c1_t0_t5 = S.Task('c1_t0_t5', length=2, delay_cost=1)
	S += c1_t0_t5 >= 49
	c1_t0_t5 += MAS[0]

	c1_t4_t5 = S.Task('c1_t4_t5', length=2, delay_cost=1)
	S += c1_t4_t5 >= 49
	c1_t4_t5 += MAS[2]

	c0_t10 = S.Task('c0_t10', length=2, delay_cost=1)
	S += c0_t10 >= 50
	c0_t10 += MAS[3]

	c0_t1_t5 = S.Task('c0_t1_t5', length=2, delay_cost=1)
	S += c0_t1_t5 >= 50
	c0_t1_t5 += MAS[2]

	c1_t01_in = S.Task('c1_t01_in', length=1, delay_cost=1)
	S += c1_t01_in >= 50
	c1_t01_in += MAS_in[0]

	c1_t01_mem0 = S.Task('c1_t01_mem0', length=1, delay_cost=1)
	S += c1_t01_mem0 >= 50
	c1_t01_mem0 += MM_MEM[0]

	c1_t01_mem1 = S.Task('c1_t01_mem1', length=1, delay_cost=1)
	S += c1_t01_mem1 >= 50
	c1_t01_mem1 += MAS_MEM[1]

	c2_t00_in = S.Task('c2_t00_in', length=1, delay_cost=1)
	S += c2_t00_in >= 50
	c2_t00_in += MAS_in[2]

	c2_t00_mem0 = S.Task('c2_t00_mem0', length=1, delay_cost=1)
	S += c2_t00_mem0 >= 50
	c2_t00_mem0 += MM_MEM[2]

	c2_t00_mem1 = S.Task('c2_t00_mem1', length=1, delay_cost=1)
	S += c2_t00_mem1 >= 50
	c2_t00_mem1 += MM_MEM[3]

	c0_t00_in = S.Task('c0_t00_in', length=1, delay_cost=1)
	S += c0_t00_in >= 51
	c0_t00_in += MAS_in[5]

	c0_t00_mem0 = S.Task('c0_t00_mem0', length=1, delay_cost=1)
	S += c0_t00_mem0 >= 51
	c0_t00_mem0 += MM_MEM[2]

	c0_t00_mem1 = S.Task('c0_t00_mem1', length=1, delay_cost=1)
	S += c0_t00_mem1 >= 51
	c0_t00_mem1 += MM_MEM[1]

	c1_t01 = S.Task('c1_t01', length=2, delay_cost=1)
	S += c1_t01 >= 51
	c1_t01 += MAS[0]

	c1_t40_in = S.Task('c1_t40_in', length=1, delay_cost=1)
	S += c1_t40_in >= 51
	c1_t40_in += MAS_in[1]

	c1_t40_mem0 = S.Task('c1_t40_mem0', length=1, delay_cost=1)
	S += c1_t40_mem0 >= 51
	c1_t40_mem0 += MM_MEM[0]

	c1_t40_mem1 = S.Task('c1_t40_mem1', length=1, delay_cost=1)
	S += c1_t40_mem1 >= 51
	c1_t40_mem1 += MM_MEM[3]

	c2_t00 = S.Task('c2_t00', length=2, delay_cost=1)
	S += c2_t00 >= 51
	c2_t00 += MAS[2]

	c0_t00 = S.Task('c0_t00', length=2, delay_cost=1)
	S += c0_t00 >= 52
	c0_t00 += MAS[5]

	c1_t00_in = S.Task('c1_t00_in', length=1, delay_cost=1)
	S += c1_t00_in >= 52
	c1_t00_in += MAS_in[3]

	c1_t00_mem0 = S.Task('c1_t00_mem0', length=1, delay_cost=1)
	S += c1_t00_mem0 >= 52
	c1_t00_mem0 += MM_MEM[2]

	c1_t00_mem1 = S.Task('c1_t00_mem1', length=1, delay_cost=1)
	S += c1_t00_mem1 >= 52
	c1_t00_mem1 += MM_MEM[1]

	c1_t10_in = S.Task('c1_t10_in', length=1, delay_cost=1)
	S += c1_t10_in >= 52
	c1_t10_in += MAS_in[0]

	c1_t10_mem0 = S.Task('c1_t10_mem0', length=1, delay_cost=1)
	S += c1_t10_mem0 >= 52
	c1_t10_mem0 += MM_MEM[0]

	c1_t10_mem1 = S.Task('c1_t10_mem1', length=1, delay_cost=1)
	S += c1_t10_mem1 >= 52
	c1_t10_mem1 += MM_MEM[3]

	c1_t40 = S.Task('c1_t40', length=2, delay_cost=1)
	S += c1_t40 >= 52
	c1_t40 += MAS[1]

	c2_t50_in = S.Task('c2_t50_in', length=1, delay_cost=1)
	S += c2_t50_in >= 52
	c2_t50_in += MAS_in[2]

	c2_t50_mem0 = S.Task('c2_t50_mem0', length=1, delay_cost=1)
	S += c2_t50_mem0 >= 52
	c2_t50_mem0 += MAS_MEM[4]

	c2_t50_mem1 = S.Task('c2_t50_mem1', length=1, delay_cost=1)
	S += c2_t50_mem1 >= 52
	c2_t50_mem1 += MAS_MEM[7]

	c0_t0_t5_in = S.Task('c0_t0_t5_in', length=1, delay_cost=1)
	S += c0_t0_t5_in >= 53
	c0_t0_t5_in += MAS_in[4]

	c0_t0_t5_mem0 = S.Task('c0_t0_t5_mem0', length=1, delay_cost=1)
	S += c0_t0_t5_mem0 >= 53
	c0_t0_t5_mem0 += MM_MEM[2]

	c0_t0_t5_mem1 = S.Task('c0_t0_t5_mem1', length=1, delay_cost=1)
	S += c0_t0_t5_mem1 >= 53
	c0_t0_t5_mem1 += MM_MEM[1]

	c0_t50_in = S.Task('c0_t50_in', length=1, delay_cost=1)
	S += c0_t50_in >= 53
	c0_t50_in += MAS_in[1]

	c0_t50_mem0 = S.Task('c0_t50_mem0', length=1, delay_cost=1)
	S += c0_t50_mem0 >= 53
	c0_t50_mem0 += MAS_MEM[10]

	c0_t50_mem1 = S.Task('c0_t50_mem1', length=1, delay_cost=1)
	S += c0_t50_mem1 >= 53
	c0_t50_mem1 += MAS_MEM[7]

	c1_t00 = S.Task('c1_t00', length=2, delay_cost=1)
	S += c1_t00 >= 53
	c1_t00 += MAS[3]

	c1_t10 = S.Task('c1_t10', length=2, delay_cost=1)
	S += c1_t10 >= 53
	c1_t10 += MAS[0]

	c2_t4_t5_in = S.Task('c2_t4_t5_in', length=1, delay_cost=1)
	S += c2_t4_t5_in >= 53
	c2_t4_t5_in += MAS_in[3]

	c2_t4_t5_mem0 = S.Task('c2_t4_t5_mem0', length=1, delay_cost=1)
	S += c2_t4_t5_mem0 >= 53
	c2_t4_t5_mem0 += MM_MEM[0]

	c2_t4_t5_mem1 = S.Task('c2_t4_t5_mem1', length=1, delay_cost=1)
	S += c2_t4_t5_mem1 >= 53
	c2_t4_t5_mem1 += MM_MEM[3]

	c2_t50 = S.Task('c2_t50', length=2, delay_cost=1)
	S += c2_t50 >= 53
	c2_t50 += MAS[2]

	c0_t0_t5 = S.Task('c0_t0_t5', length=2, delay_cost=1)
	S += c0_t0_t5 >= 54
	c0_t0_t5 += MAS[4]

	c0_t40_in = S.Task('c0_t40_in', length=1, delay_cost=1)
	S += c0_t40_in >= 54
	c0_t40_in += MAS_in[3]

	c0_t40_mem0 = S.Task('c0_t40_mem0', length=1, delay_cost=1)
	S += c0_t40_mem0 >= 54
	c0_t40_mem0 += MM_MEM[0]

	c0_t40_mem1 = S.Task('c0_t40_mem1', length=1, delay_cost=1)
	S += c0_t40_mem1 >= 54
	c0_t40_mem1 += MM_MEM[1]

	c0_t50 = S.Task('c0_t50', length=2, delay_cost=1)
	S += c0_t50 >= 54
	c0_t50 += MAS[1]

	c1_t50_in = S.Task('c1_t50_in', length=1, delay_cost=1)
	S += c1_t50_in >= 54
	c1_t50_in += MAS_in[1]

	c1_t50_mem0 = S.Task('c1_t50_mem0', length=1, delay_cost=1)
	S += c1_t50_mem0 >= 54
	c1_t50_mem0 += MAS_MEM[6]

	c1_t50_mem1 = S.Task('c1_t50_mem1', length=1, delay_cost=1)
	S += c1_t50_mem1 >= 54
	c1_t50_mem1 += MAS_MEM[1]

	c2_t0_t5_in = S.Task('c2_t0_t5_in', length=1, delay_cost=1)
	S += c2_t0_t5_in >= 54
	c2_t0_t5_in += MAS_in[5]

	c2_t0_t5_mem0 = S.Task('c2_t0_t5_mem0', length=1, delay_cost=1)
	S += c2_t0_t5_mem0 >= 54
	c2_t0_t5_mem0 += MM_MEM[2]

	c2_t0_t5_mem1 = S.Task('c2_t0_t5_mem1', length=1, delay_cost=1)
	S += c2_t0_t5_mem1 >= 54
	c2_t0_t5_mem1 += MM_MEM[3]

	c2_t4_t5 = S.Task('c2_t4_t5', length=2, delay_cost=1)
	S += c2_t4_t5 >= 54
	c2_t4_t5 += MAS[3]

	c0_t40 = S.Task('c0_t40', length=2, delay_cost=1)
	S += c0_t40 >= 55
	c0_t40 += MAS[3]

	c1_t1_t5_in = S.Task('c1_t1_t5_in', length=1, delay_cost=1)
	S += c1_t1_t5_in >= 55
	c1_t1_t5_in += MAS_in[4]

	c1_t1_t5_mem0 = S.Task('c1_t1_t5_mem0', length=1, delay_cost=1)
	S += c1_t1_t5_mem0 >= 55
	c1_t1_t5_mem0 += MM_MEM[2]

	c1_t1_t5_mem1 = S.Task('c1_t1_t5_mem1', length=1, delay_cost=1)
	S += c1_t1_t5_mem1 >= 55
	c1_t1_t5_mem1 += MM_MEM[1]

	c1_t50 = S.Task('c1_t50', length=2, delay_cost=1)
	S += c1_t50 >= 55
	c1_t50 += MAS[1]

	c2_t0_t5 = S.Task('c2_t0_t5', length=2, delay_cost=1)
	S += c2_t0_t5 >= 55
	c2_t0_t5 += MAS[5]

	c2_t40_in = S.Task('c2_t40_in', length=1, delay_cost=1)
	S += c2_t40_in >= 55
	c2_t40_in += MAS_in[2]

	c2_t40_mem0 = S.Task('c2_t40_mem0', length=1, delay_cost=1)
	S += c2_t40_mem0 >= 55
	c2_t40_mem0 += MM_MEM[0]

	c2_t40_mem1 = S.Task('c2_t40_mem1', length=1, delay_cost=1)
	S += c2_t40_mem1 >= 55
	c2_t40_mem1 += MM_MEM[3]

	c0_t4_t5_in = S.Task('c0_t4_t5_in', length=1, delay_cost=1)
	S += c0_t4_t5_in >= 56
	c0_t4_t5_in += MAS_in[0]

	c0_t4_t5_mem0 = S.Task('c0_t4_t5_mem0', length=1, delay_cost=1)
	S += c0_t4_t5_mem0 >= 56
	c0_t4_t5_mem0 += MM_MEM[0]

	c0_t4_t5_mem1 = S.Task('c0_t4_t5_mem1', length=1, delay_cost=1)
	S += c0_t4_t5_mem1 >= 56
	c0_t4_t5_mem1 += MM_MEM[1]

	c1_t1_t5 = S.Task('c1_t1_t5', length=2, delay_cost=1)
	S += c1_t1_t5 >= 56
	c1_t1_t5 += MAS[4]

	c2_t11_in = S.Task('c2_t11_in', length=1, delay_cost=1)
	S += c2_t11_in >= 56
	c2_t11_in += MAS_in[2]

	c2_t11_mem0 = S.Task('c2_t11_mem0', length=1, delay_cost=1)
	S += c2_t11_mem0 >= 56
	c2_t11_mem0 += MM_MEM[2]

	c2_t11_mem1 = S.Task('c2_t11_mem1', length=1, delay_cost=1)
	S += c2_t11_mem1 >= 56
	c2_t11_mem1 += MAS_MEM[1]

	c2_t40 = S.Task('c2_t40', length=2, delay_cost=1)
	S += c2_t40 >= 56
	c2_t40 += MAS[2]

	c0_t01_in = S.Task('c0_t01_in', length=1, delay_cost=1)
	S += c0_t01_in >= 57
	c0_t01_in += MAS_in[3]

	c0_t01_mem0 = S.Task('c0_t01_mem0', length=1, delay_cost=1)
	S += c0_t01_mem0 >= 57
	c0_t01_mem0 += MM_MEM[2]

	c0_t01_mem1 = S.Task('c0_t01_mem1', length=1, delay_cost=1)
	S += c0_t01_mem1 >= 57
	c0_t01_mem1 += MAS_MEM[9]

	c0_t4_t5 = S.Task('c0_t4_t5', length=2, delay_cost=1)
	S += c0_t4_t5 >= 57
	c0_t4_t5 += MAS[0]

	c2_t01_in = S.Task('c2_t01_in', length=1, delay_cost=1)
	S += c2_t01_in >= 57
	c2_t01_in += MAS_in[5]

	c2_t01_mem0 = S.Task('c2_t01_mem0', length=1, delay_cost=1)
	S += c2_t01_mem0 >= 57
	c2_t01_mem0 += MM_MEM[0]

	c2_t01_mem1 = S.Task('c2_t01_mem1', length=1, delay_cost=1)
	S += c2_t01_mem1 >= 57
	c2_t01_mem1 += MAS_MEM[11]

	c2_t11 = S.Task('c2_t11', length=2, delay_cost=1)
	S += c2_t11 >= 57
	c2_t11 += MAS[2]

	c0_t01 = S.Task('c0_t01', length=2, delay_cost=1)
	S += c0_t01 >= 58
	c0_t01 += MAS[3]

	c0_t11_in = S.Task('c0_t11_in', length=1, delay_cost=1)
	S += c0_t11_in >= 58
	c0_t11_in += MAS_in[1]

	c0_t11_mem0 = S.Task('c0_t11_mem0', length=1, delay_cost=1)
	S += c0_t11_mem0 >= 58
	c0_t11_mem0 += MM_MEM[2]

	c0_t11_mem1 = S.Task('c0_t11_mem1', length=1, delay_cost=1)
	S += c0_t11_mem1 >= 58
	c0_t11_mem1 += MAS_MEM[5]

	c1_t11_in = S.Task('c1_t11_in', length=1, delay_cost=1)
	S += c1_t11_in >= 58
	c1_t11_in += MAS_in[2]

	c1_t11_mem0 = S.Task('c1_t11_mem0', length=1, delay_cost=1)
	S += c1_t11_mem0 >= 58
	c1_t11_mem0 += MM_MEM[0]

	c1_t11_mem1 = S.Task('c1_t11_mem1', length=1, delay_cost=1)
	S += c1_t11_mem1 >= 58
	c1_t11_mem1 += MAS_MEM[9]

	c2_t01 = S.Task('c2_t01', length=2, delay_cost=1)
	S += c2_t01 >= 58
	c2_t01 += MAS[5]

	c0_t11 = S.Task('c0_t11', length=2, delay_cost=1)
	S += c0_t11 >= 59
	c0_t11 += MAS[1]

	c1_t11 = S.Task('c1_t11', length=2, delay_cost=1)
	S += c1_t11 >= 59
	c1_t11 += MAS[2]


	# new tasks
	c0_t41 = S.Task('c0_t41', length=2, delay_cost=1)
	c0_t41 += alt(MAS)
	c0_t41_in = S.Task('c0_t41_in', length=1, delay_cost=1)
	c0_t41_in += alt(MAS_in)
	S += c0_t41_in*MAS_in[0]<=c0_t41*MAS[0]

	S += c0_t41_in*MAS_in[1]<=c0_t41*MAS[1]

	S += c0_t41_in*MAS_in[2]<=c0_t41*MAS[2]

	S += c0_t41_in*MAS_in[3]<=c0_t41*MAS[3]

	S += c0_t41_in*MAS_in[4]<=c0_t41*MAS[4]

	S += c0_t41_in*MAS_in[5]<=c0_t41*MAS[5]

	c0_t41_mem0 = S.Task('c0_t41_mem0', length=1, delay_cost=1)
	c0_t41_mem0 += MM_MEM[2]
	S += 55 < c0_t41_mem0
	S += c0_t41_mem0 <= c0_t41

	c0_t41_mem1 = S.Task('c0_t41_mem1', length=1, delay_cost=1)
	c0_t41_mem1 += MAS_MEM[1]
	S += 58 < c0_t41_mem1
	S += c0_t41_mem1 <= c0_t41

	c0_s00 = S.Task('c0_s00', length=2, delay_cost=1)
	c0_s00 += alt(MAS)
	c0_s00_in = S.Task('c0_s00_in', length=1, delay_cost=1)
	c0_s00_in += alt(MAS_in)
	S += c0_s00_in*MAS_in[0]<=c0_s00*MAS[0]

	S += c0_s00_in*MAS_in[1]<=c0_s00*MAS[1]

	S += c0_s00_in*MAS_in[2]<=c0_s00*MAS[2]

	S += c0_s00_in*MAS_in[3]<=c0_s00*MAS[3]

	S += c0_s00_in*MAS_in[4]<=c0_s00*MAS[4]

	S += c0_s00_in*MAS_in[5]<=c0_s00*MAS[5]

	c0_s00_mem0 = S.Task('c0_s00_mem0', length=1, delay_cost=1)
	c0_s00_mem0 += MAS_MEM[6]
	S += 51 < c0_s00_mem0
	S += c0_s00_mem0 <= c0_s00

	c0_s00_mem1 = S.Task('c0_s00_mem1', length=1, delay_cost=1)
	c0_s00_mem1 += MAS_MEM[3]
	S += 60 < c0_s00_mem1
	S += c0_s00_mem1 <= c0_s00

	c0_s01 = S.Task('c0_s01', length=2, delay_cost=1)
	c0_s01 += alt(MAS)
	c0_s01_in = S.Task('c0_s01_in', length=1, delay_cost=1)
	c0_s01_in += alt(MAS_in)
	S += c0_s01_in*MAS_in[0]<=c0_s01*MAS[0]

	S += c0_s01_in*MAS_in[1]<=c0_s01*MAS[1]

	S += c0_s01_in*MAS_in[2]<=c0_s01*MAS[2]

	S += c0_s01_in*MAS_in[3]<=c0_s01*MAS[3]

	S += c0_s01_in*MAS_in[4]<=c0_s01*MAS[4]

	S += c0_s01_in*MAS_in[5]<=c0_s01*MAS[5]

	c0_s01_mem0 = S.Task('c0_s01_mem0', length=1, delay_cost=1)
	c0_s01_mem0 += MAS_MEM[6]
	S += 51 < c0_s01_mem0
	S += c0_s01_mem0 <= c0_s01

	c0_s01_mem1 = S.Task('c0_s01_mem1', length=1, delay_cost=1)
	c0_s01_mem1 += MAS_MEM[3]
	S += 60 < c0_s01_mem1
	S += c0_s01_mem1 <= c0_s01

	c0_t51 = S.Task('c0_t51', length=2, delay_cost=1)
	c0_t51 += alt(MAS)
	c0_t51_in = S.Task('c0_t51_in', length=1, delay_cost=1)
	c0_t51_in += alt(MAS_in)
	S += c0_t51_in*MAS_in[0]<=c0_t51*MAS[0]

	S += c0_t51_in*MAS_in[1]<=c0_t51*MAS[1]

	S += c0_t51_in*MAS_in[2]<=c0_t51*MAS[2]

	S += c0_t51_in*MAS_in[3]<=c0_t51*MAS[3]

	S += c0_t51_in*MAS_in[4]<=c0_t51*MAS[4]

	S += c0_t51_in*MAS_in[5]<=c0_t51*MAS[5]

	c0_t51_mem0 = S.Task('c0_t51_mem0', length=1, delay_cost=1)
	c0_t51_mem0 += MAS_MEM[6]
	S += 59 < c0_t51_mem0
	S += c0_t51_mem0 <= c0_t51

	c0_t51_mem1 = S.Task('c0_t51_mem1', length=1, delay_cost=1)
	c0_t51_mem1 += MAS_MEM[3]
	S += 60 < c0_t51_mem1
	S += c0_t51_mem1 <= c0_t51

	c010 = S.Task('c010', length=2, delay_cost=1)
	c010 += alt(MAS)
	c010_in = S.Task('c010_in', length=1, delay_cost=1)
	c010_in += alt(MAS_in)
	S += c010_in*MAS_in[0]<=c010*MAS[0]

	S += c010_in*MAS_in[1]<=c010*MAS[1]

	S += c010_in*MAS_in[2]<=c010*MAS[2]

	S += c010_in*MAS_in[3]<=c010*MAS[3]

	S += c010_in*MAS_in[4]<=c010*MAS[4]

	S += c010_in*MAS_in[5]<=c010*MAS[5]

	S += 0<c010

	c010_w = S.Task('c010_w', length=1, delay_cost=1)
	c010_w += alt(MAIN_MEM_w)
	S += c010 <= c010_w

	c010_mem0 = S.Task('c010_mem0', length=1, delay_cost=1)
	c010_mem0 += MAS_MEM[6]
	S += 56 < c010_mem0
	S += c010_mem0 <= c010

	c010_mem1 = S.Task('c010_mem1', length=1, delay_cost=1)
	c010_mem1 += MAS_MEM[3]
	S += 55 < c010_mem1
	S += c010_mem1 <= c010

	c1_t41 = S.Task('c1_t41', length=2, delay_cost=1)
	c1_t41 += alt(MAS)
	c1_t41_in = S.Task('c1_t41_in', length=1, delay_cost=1)
	c1_t41_in += alt(MAS_in)
	S += c1_t41_in*MAS_in[0]<=c1_t41*MAS[0]

	S += c1_t41_in*MAS_in[1]<=c1_t41*MAS[1]

	S += c1_t41_in*MAS_in[2]<=c1_t41*MAS[2]

	S += c1_t41_in*MAS_in[3]<=c1_t41*MAS[3]

	S += c1_t41_in*MAS_in[4]<=c1_t41*MAS[4]

	S += c1_t41_in*MAS_in[5]<=c1_t41*MAS[5]

	c1_t41_mem0 = S.Task('c1_t41_mem0', length=1, delay_cost=1)
	c1_t41_mem0 += MM_MEM[2]
	S += 51 < c1_t41_mem0
	S += c1_t41_mem0 <= c1_t41

	c1_t41_mem1 = S.Task('c1_t41_mem1', length=1, delay_cost=1)
	c1_t41_mem1 += MAS_MEM[5]
	S += 50 < c1_t41_mem1
	S += c1_t41_mem1 <= c1_t41

	c1_s00 = S.Task('c1_s00', length=2, delay_cost=1)
	c1_s00 += alt(MAS)
	c1_s00_in = S.Task('c1_s00_in', length=1, delay_cost=1)
	c1_s00_in += alt(MAS_in)
	S += c1_s00_in*MAS_in[0]<=c1_s00*MAS[0]

	S += c1_s00_in*MAS_in[1]<=c1_s00*MAS[1]

	S += c1_s00_in*MAS_in[2]<=c1_s00*MAS[2]

	S += c1_s00_in*MAS_in[3]<=c1_s00*MAS[3]

	S += c1_s00_in*MAS_in[4]<=c1_s00*MAS[4]

	S += c1_s00_in*MAS_in[5]<=c1_s00*MAS[5]

	c1_s00_mem0 = S.Task('c1_s00_mem0', length=1, delay_cost=1)
	c1_s00_mem0 += MAS_MEM[0]
	S += 54 < c1_s00_mem0
	S += c1_s00_mem0 <= c1_s00

	c1_s00_mem1 = S.Task('c1_s00_mem1', length=1, delay_cost=1)
	c1_s00_mem1 += MAS_MEM[5]
	S += 60 < c1_s00_mem1
	S += c1_s00_mem1 <= c1_s00

	c1_s01 = S.Task('c1_s01', length=2, delay_cost=1)
	c1_s01 += alt(MAS)
	c1_s01_in = S.Task('c1_s01_in', length=1, delay_cost=1)
	c1_s01_in += alt(MAS_in)
	S += c1_s01_in*MAS_in[0]<=c1_s01*MAS[0]

	S += c1_s01_in*MAS_in[1]<=c1_s01*MAS[1]

	S += c1_s01_in*MAS_in[2]<=c1_s01*MAS[2]

	S += c1_s01_in*MAS_in[3]<=c1_s01*MAS[3]

	S += c1_s01_in*MAS_in[4]<=c1_s01*MAS[4]

	S += c1_s01_in*MAS_in[5]<=c1_s01*MAS[5]

	c1_s01_mem0 = S.Task('c1_s01_mem0', length=1, delay_cost=1)
	c1_s01_mem0 += MAS_MEM[0]
	S += 54 < c1_s01_mem0
	S += c1_s01_mem0 <= c1_s01

	c1_s01_mem1 = S.Task('c1_s01_mem1', length=1, delay_cost=1)
	c1_s01_mem1 += MAS_MEM[5]
	S += 60 < c1_s01_mem1
	S += c1_s01_mem1 <= c1_s01

	c1_t51 = S.Task('c1_t51', length=2, delay_cost=1)
	c1_t51 += alt(MAS)
	c1_t51_in = S.Task('c1_t51_in', length=1, delay_cost=1)
	c1_t51_in += alt(MAS_in)
	S += c1_t51_in*MAS_in[0]<=c1_t51*MAS[0]

	S += c1_t51_in*MAS_in[1]<=c1_t51*MAS[1]

	S += c1_t51_in*MAS_in[2]<=c1_t51*MAS[2]

	S += c1_t51_in*MAS_in[3]<=c1_t51*MAS[3]

	S += c1_t51_in*MAS_in[4]<=c1_t51*MAS[4]

	S += c1_t51_in*MAS_in[5]<=c1_t51*MAS[5]

	c1_t51_mem0 = S.Task('c1_t51_mem0', length=1, delay_cost=1)
	c1_t51_mem0 += MAS_MEM[0]
	S += 52 < c1_t51_mem0
	S += c1_t51_mem0 <= c1_t51

	c1_t51_mem1 = S.Task('c1_t51_mem1', length=1, delay_cost=1)
	c1_t51_mem1 += MAS_MEM[5]
	S += 60 < c1_t51_mem1
	S += c1_t51_mem1 <= c1_t51

	c110 = S.Task('c110', length=2, delay_cost=1)
	c110 += alt(MAS)
	c110_in = S.Task('c110_in', length=1, delay_cost=1)
	c110_in += alt(MAS_in)
	S += c110_in*MAS_in[0]<=c110*MAS[0]

	S += c110_in*MAS_in[1]<=c110*MAS[1]

	S += c110_in*MAS_in[2]<=c110*MAS[2]

	S += c110_in*MAS_in[3]<=c110*MAS[3]

	S += c110_in*MAS_in[4]<=c110*MAS[4]

	S += c110_in*MAS_in[5]<=c110*MAS[5]

	S += 0<c110

	c110_w = S.Task('c110_w', length=1, delay_cost=1)
	c110_w += alt(MAIN_MEM_w)
	S += c110 <= c110_w

	c110_mem0 = S.Task('c110_mem0', length=1, delay_cost=1)
	c110_mem0 += MAS_MEM[2]
	S += 53 < c110_mem0
	S += c110_mem0 <= c110

	c110_mem1 = S.Task('c110_mem1', length=1, delay_cost=1)
	c110_mem1 += MAS_MEM[3]
	S += 56 < c110_mem1
	S += c110_mem1 <= c110

	c2_t41 = S.Task('c2_t41', length=2, delay_cost=1)
	c2_t41 += alt(MAS)
	c2_t41_in = S.Task('c2_t41_in', length=1, delay_cost=1)
	c2_t41_in += alt(MAS_in)
	S += c2_t41_in*MAS_in[0]<=c2_t41*MAS[0]

	S += c2_t41_in*MAS_in[1]<=c2_t41*MAS[1]

	S += c2_t41_in*MAS_in[2]<=c2_t41*MAS[2]

	S += c2_t41_in*MAS_in[3]<=c2_t41*MAS[3]

	S += c2_t41_in*MAS_in[4]<=c2_t41*MAS[4]

	S += c2_t41_in*MAS_in[5]<=c2_t41*MAS[5]

	c2_t41_mem0 = S.Task('c2_t41_mem0', length=1, delay_cost=1)
	c2_t41_mem0 += MM_MEM[0]
	S += 56 < c2_t41_mem0
	S += c2_t41_mem0 <= c2_t41

	c2_t41_mem1 = S.Task('c2_t41_mem1', length=1, delay_cost=1)
	c2_t41_mem1 += MAS_MEM[7]
	S += 55 < c2_t41_mem1
	S += c2_t41_mem1 <= c2_t41

	c2_s00 = S.Task('c2_s00', length=2, delay_cost=1)
	c2_s00 += alt(MAS)
	c2_s00_in = S.Task('c2_s00_in', length=1, delay_cost=1)
	c2_s00_in += alt(MAS_in)
	S += c2_s00_in*MAS_in[0]<=c2_s00*MAS[0]

	S += c2_s00_in*MAS_in[1]<=c2_s00*MAS[1]

	S += c2_s00_in*MAS_in[2]<=c2_s00*MAS[2]

	S += c2_s00_in*MAS_in[3]<=c2_s00*MAS[3]

	S += c2_s00_in*MAS_in[4]<=c2_s00*MAS[4]

	S += c2_s00_in*MAS_in[5]<=c2_s00*MAS[5]

	c2_s00_mem0 = S.Task('c2_s00_mem0', length=1, delay_cost=1)
	c2_s00_mem0 += MAS_MEM[6]
	S += 49 < c2_s00_mem0
	S += c2_s00_mem0 <= c2_s00

	c2_s00_mem1 = S.Task('c2_s00_mem1', length=1, delay_cost=1)
	c2_s00_mem1 += MAS_MEM[5]
	S += 58 < c2_s00_mem1
	S += c2_s00_mem1 <= c2_s00

	c2_s01 = S.Task('c2_s01', length=2, delay_cost=1)
	c2_s01 += alt(MAS)
	c2_s01_in = S.Task('c2_s01_in', length=1, delay_cost=1)
	c2_s01_in += alt(MAS_in)
	S += c2_s01_in*MAS_in[0]<=c2_s01*MAS[0]

	S += c2_s01_in*MAS_in[1]<=c2_s01*MAS[1]

	S += c2_s01_in*MAS_in[2]<=c2_s01*MAS[2]

	S += c2_s01_in*MAS_in[3]<=c2_s01*MAS[3]

	S += c2_s01_in*MAS_in[4]<=c2_s01*MAS[4]

	S += c2_s01_in*MAS_in[5]<=c2_s01*MAS[5]

	c2_s01_mem0 = S.Task('c2_s01_mem0', length=1, delay_cost=1)
	c2_s01_mem0 += MAS_MEM[6]
	S += 49 < c2_s01_mem0
	S += c2_s01_mem0 <= c2_s01

	c2_s01_mem1 = S.Task('c2_s01_mem1', length=1, delay_cost=1)
	c2_s01_mem1 += MAS_MEM[5]
	S += 58 < c2_s01_mem1
	S += c2_s01_mem1 <= c2_s01

	c2_t51 = S.Task('c2_t51', length=2, delay_cost=1)
	c2_t51 += alt(MAS)
	c2_t51_in = S.Task('c2_t51_in', length=1, delay_cost=1)
	c2_t51_in += alt(MAS_in)
	S += c2_t51_in*MAS_in[0]<=c2_t51*MAS[0]

	S += c2_t51_in*MAS_in[1]<=c2_t51*MAS[1]

	S += c2_t51_in*MAS_in[2]<=c2_t51*MAS[2]

	S += c2_t51_in*MAS_in[3]<=c2_t51*MAS[3]

	S += c2_t51_in*MAS_in[4]<=c2_t51*MAS[4]

	S += c2_t51_in*MAS_in[5]<=c2_t51*MAS[5]

	c2_t51_mem0 = S.Task('c2_t51_mem0', length=1, delay_cost=1)
	c2_t51_mem0 += MAS_MEM[10]
	S += 59 < c2_t51_mem0
	S += c2_t51_mem0 <= c2_t51

	c2_t51_mem1 = S.Task('c2_t51_mem1', length=1, delay_cost=1)
	c2_t51_mem1 += MAS_MEM[5]
	S += 58 < c2_t51_mem1
	S += c2_t51_mem1 <= c2_t51

	c210 = S.Task('c210', length=2, delay_cost=1)
	c210 += alt(MAS)
	c210_in = S.Task('c210_in', length=1, delay_cost=1)
	c210_in += alt(MAS_in)
	S += c210_in*MAS_in[0]<=c210*MAS[0]

	S += c210_in*MAS_in[1]<=c210*MAS[1]

	S += c210_in*MAS_in[2]<=c210*MAS[2]

	S += c210_in*MAS_in[3]<=c210*MAS[3]

	S += c210_in*MAS_in[4]<=c210*MAS[4]

	S += c210_in*MAS_in[5]<=c210*MAS[5]

	S += 0<c210

	c210_w = S.Task('c210_w', length=1, delay_cost=1)
	c210_w += alt(MAIN_MEM_w)
	S += c210 <= c210_w

	c210_mem0 = S.Task('c210_mem0', length=1, delay_cost=1)
	c210_mem0 += MAS_MEM[4]
	S += 57 < c210_mem0
	S += c210_mem0 <= c210

	c210_mem1 = S.Task('c210_mem1', length=1, delay_cost=1)
	c210_mem1 += MAS_MEM[5]
	S += 54 < c210_mem1
	S += c210_mem1 <= c210

	c000 = S.Task('c000', length=2, delay_cost=1)
	c000 += alt(MAS)
	c000_in = S.Task('c000_in', length=1, delay_cost=1)
	c000_in += alt(MAS_in)
	S += c000_in*MAS_in[0]<=c000*MAS[0]

	S += c000_in*MAS_in[1]<=c000*MAS[1]

	S += c000_in*MAS_in[2]<=c000*MAS[2]

	S += c000_in*MAS_in[3]<=c000*MAS[3]

	S += c000_in*MAS_in[4]<=c000*MAS[4]

	S += c000_in*MAS_in[5]<=c000*MAS[5]

	S += 0<c000

	c000_w = S.Task('c000_w', length=1, delay_cost=1)
	c000_w += alt(MAIN_MEM_w)
	S += c000 <= c000_w

	c000_mem0 = S.Task('c000_mem0', length=1, delay_cost=1)
	c000_mem0 += MAS_MEM[10]
	S += 53 < c000_mem0
	S += c000_mem0 <= c000

	c000_mem1 = S.Task('c000_mem1', length=1, delay_cost=1)
	c000_mem1 += alt(MAS_MEM)
	S += (c0_s00*MAS[0])-1 < c000_mem1*MAS_MEM[1]
	S += (c0_s00*MAS[1])-1 < c000_mem1*MAS_MEM[3]
	S += (c0_s00*MAS[2])-1 < c000_mem1*MAS_MEM[5]
	S += (c0_s00*MAS[3])-1 < c000_mem1*MAS_MEM[7]
	S += (c0_s00*MAS[4])-1 < c000_mem1*MAS_MEM[9]
	S += (c0_s00*MAS[5])-1 < c000_mem1*MAS_MEM[11]
	S += c000_mem1 <= c000

	c001 = S.Task('c001', length=2, delay_cost=1)
	c001 += alt(MAS)
	c001_in = S.Task('c001_in', length=1, delay_cost=1)
	c001_in += alt(MAS_in)
	S += c001_in*MAS_in[0]<=c001*MAS[0]

	S += c001_in*MAS_in[1]<=c001*MAS[1]

	S += c001_in*MAS_in[2]<=c001*MAS[2]

	S += c001_in*MAS_in[3]<=c001*MAS[3]

	S += c001_in*MAS_in[4]<=c001*MAS[4]

	S += c001_in*MAS_in[5]<=c001*MAS[5]

	S += 0<c001

	c001_w = S.Task('c001_w', length=1, delay_cost=1)
	c001_w += alt(MAIN_MEM_w)
	S += c001 <= c001_w

	c001_mem0 = S.Task('c001_mem0', length=1, delay_cost=1)
	c001_mem0 += MAS_MEM[6]
	S += 59 < c001_mem0
	S += c001_mem0 <= c001

	c001_mem1 = S.Task('c001_mem1', length=1, delay_cost=1)
	c001_mem1 += alt(MAS_MEM)
	S += (c0_s01*MAS[0])-1 < c001_mem1*MAS_MEM[1]
	S += (c0_s01*MAS[1])-1 < c001_mem1*MAS_MEM[3]
	S += (c0_s01*MAS[2])-1 < c001_mem1*MAS_MEM[5]
	S += (c0_s01*MAS[3])-1 < c001_mem1*MAS_MEM[7]
	S += (c0_s01*MAS[4])-1 < c001_mem1*MAS_MEM[9]
	S += (c0_s01*MAS[5])-1 < c001_mem1*MAS_MEM[11]
	S += c001_mem1 <= c001

	c011 = S.Task('c011', length=2, delay_cost=1)
	c011 += alt(MAS)
	c011_in = S.Task('c011_in', length=1, delay_cost=1)
	c011_in += alt(MAS_in)
	S += c011_in*MAS_in[0]<=c011*MAS[0]

	S += c011_in*MAS_in[1]<=c011*MAS[1]

	S += c011_in*MAS_in[2]<=c011*MAS[2]

	S += c011_in*MAS_in[3]<=c011*MAS[3]

	S += c011_in*MAS_in[4]<=c011*MAS[4]

	S += c011_in*MAS_in[5]<=c011*MAS[5]

	S += 0<c011

	c011_w = S.Task('c011_w', length=1, delay_cost=1)
	c011_w += alt(MAIN_MEM_w)
	S += c011 <= c011_w

	c011_mem0 = S.Task('c011_mem0', length=1, delay_cost=1)
	c011_mem0 += alt(MAS_MEM)
	S += (c0_t41*MAS[0])-1 < c011_mem0*MAS_MEM[0]
	S += (c0_t41*MAS[1])-1 < c011_mem0*MAS_MEM[2]
	S += (c0_t41*MAS[2])-1 < c011_mem0*MAS_MEM[4]
	S += (c0_t41*MAS[3])-1 < c011_mem0*MAS_MEM[6]
	S += (c0_t41*MAS[4])-1 < c011_mem0*MAS_MEM[8]
	S += (c0_t41*MAS[5])-1 < c011_mem0*MAS_MEM[10]
	S += c011_mem0 <= c011

	c011_mem1 = S.Task('c011_mem1', length=1, delay_cost=1)
	c011_mem1 += alt(MAS_MEM)
	S += (c0_t51*MAS[0])-1 < c011_mem1*MAS_MEM[1]
	S += (c0_t51*MAS[1])-1 < c011_mem1*MAS_MEM[3]
	S += (c0_t51*MAS[2])-1 < c011_mem1*MAS_MEM[5]
	S += (c0_t51*MAS[3])-1 < c011_mem1*MAS_MEM[7]
	S += (c0_t51*MAS[4])-1 < c011_mem1*MAS_MEM[9]
	S += (c0_t51*MAS[5])-1 < c011_mem1*MAS_MEM[11]
	S += c011_mem1 <= c011

	c100 = S.Task('c100', length=2, delay_cost=1)
	c100 += alt(MAS)
	c100_in = S.Task('c100_in', length=1, delay_cost=1)
	c100_in += alt(MAS_in)
	S += c100_in*MAS_in[0]<=c100*MAS[0]

	S += c100_in*MAS_in[1]<=c100*MAS[1]

	S += c100_in*MAS_in[2]<=c100*MAS[2]

	S += c100_in*MAS_in[3]<=c100*MAS[3]

	S += c100_in*MAS_in[4]<=c100*MAS[4]

	S += c100_in*MAS_in[5]<=c100*MAS[5]

	S += 0<c100

	c100_w = S.Task('c100_w', length=1, delay_cost=1)
	c100_w += alt(MAIN_MEM_w)
	S += c100 <= c100_w

	c100_mem0 = S.Task('c100_mem0', length=1, delay_cost=1)
	c100_mem0 += MAS_MEM[6]
	S += 54 < c100_mem0
	S += c100_mem0 <= c100

	c100_mem1 = S.Task('c100_mem1', length=1, delay_cost=1)
	c100_mem1 += alt(MAS_MEM)
	S += (c1_s00*MAS[0])-1 < c100_mem1*MAS_MEM[1]
	S += (c1_s00*MAS[1])-1 < c100_mem1*MAS_MEM[3]
	S += (c1_s00*MAS[2])-1 < c100_mem1*MAS_MEM[5]
	S += (c1_s00*MAS[3])-1 < c100_mem1*MAS_MEM[7]
	S += (c1_s00*MAS[4])-1 < c100_mem1*MAS_MEM[9]
	S += (c1_s00*MAS[5])-1 < c100_mem1*MAS_MEM[11]
	S += c100_mem1 <= c100

	c101 = S.Task('c101', length=2, delay_cost=1)
	c101 += alt(MAS)
	c101_in = S.Task('c101_in', length=1, delay_cost=1)
	c101_in += alt(MAS_in)
	S += c101_in*MAS_in[0]<=c101*MAS[0]

	S += c101_in*MAS_in[1]<=c101*MAS[1]

	S += c101_in*MAS_in[2]<=c101*MAS[2]

	S += c101_in*MAS_in[3]<=c101*MAS[3]

	S += c101_in*MAS_in[4]<=c101*MAS[4]

	S += c101_in*MAS_in[5]<=c101*MAS[5]

	S += 0<c101

	c101_w = S.Task('c101_w', length=1, delay_cost=1)
	c101_w += alt(MAIN_MEM_w)
	S += c101 <= c101_w

	c101_mem0 = S.Task('c101_mem0', length=1, delay_cost=1)
	c101_mem0 += MAS_MEM[0]
	S += 52 < c101_mem0
	S += c101_mem0 <= c101

	c101_mem1 = S.Task('c101_mem1', length=1, delay_cost=1)
	c101_mem1 += alt(MAS_MEM)
	S += (c1_s01*MAS[0])-1 < c101_mem1*MAS_MEM[1]
	S += (c1_s01*MAS[1])-1 < c101_mem1*MAS_MEM[3]
	S += (c1_s01*MAS[2])-1 < c101_mem1*MAS_MEM[5]
	S += (c1_s01*MAS[3])-1 < c101_mem1*MAS_MEM[7]
	S += (c1_s01*MAS[4])-1 < c101_mem1*MAS_MEM[9]
	S += (c1_s01*MAS[5])-1 < c101_mem1*MAS_MEM[11]
	S += c101_mem1 <= c101

	c111 = S.Task('c111', length=2, delay_cost=1)
	c111 += alt(MAS)
	c111_in = S.Task('c111_in', length=1, delay_cost=1)
	c111_in += alt(MAS_in)
	S += c111_in*MAS_in[0]<=c111*MAS[0]

	S += c111_in*MAS_in[1]<=c111*MAS[1]

	S += c111_in*MAS_in[2]<=c111*MAS[2]

	S += c111_in*MAS_in[3]<=c111*MAS[3]

	S += c111_in*MAS_in[4]<=c111*MAS[4]

	S += c111_in*MAS_in[5]<=c111*MAS[5]

	S += 0<c111

	c111_w = S.Task('c111_w', length=1, delay_cost=1)
	c111_w += alt(MAIN_MEM_w)
	S += c111 <= c111_w

	c111_mem0 = S.Task('c111_mem0', length=1, delay_cost=1)
	c111_mem0 += alt(MAS_MEM)
	S += (c1_t41*MAS[0])-1 < c111_mem0*MAS_MEM[0]
	S += (c1_t41*MAS[1])-1 < c111_mem0*MAS_MEM[2]
	S += (c1_t41*MAS[2])-1 < c111_mem0*MAS_MEM[4]
	S += (c1_t41*MAS[3])-1 < c111_mem0*MAS_MEM[6]
	S += (c1_t41*MAS[4])-1 < c111_mem0*MAS_MEM[8]
	S += (c1_t41*MAS[5])-1 < c111_mem0*MAS_MEM[10]
	S += c111_mem0 <= c111

	c111_mem1 = S.Task('c111_mem1', length=1, delay_cost=1)
	c111_mem1 += alt(MAS_MEM)
	S += (c1_t51*MAS[0])-1 < c111_mem1*MAS_MEM[1]
	S += (c1_t51*MAS[1])-1 < c111_mem1*MAS_MEM[3]
	S += (c1_t51*MAS[2])-1 < c111_mem1*MAS_MEM[5]
	S += (c1_t51*MAS[3])-1 < c111_mem1*MAS_MEM[7]
	S += (c1_t51*MAS[4])-1 < c111_mem1*MAS_MEM[9]
	S += (c1_t51*MAS[5])-1 < c111_mem1*MAS_MEM[11]
	S += c111_mem1 <= c111

	c200 = S.Task('c200', length=2, delay_cost=1)
	c200 += alt(MAS)
	c200_in = S.Task('c200_in', length=1, delay_cost=1)
	c200_in += alt(MAS_in)
	S += c200_in*MAS_in[0]<=c200*MAS[0]

	S += c200_in*MAS_in[1]<=c200*MAS[1]

	S += c200_in*MAS_in[2]<=c200*MAS[2]

	S += c200_in*MAS_in[3]<=c200*MAS[3]

	S += c200_in*MAS_in[4]<=c200*MAS[4]

	S += c200_in*MAS_in[5]<=c200*MAS[5]

	S += 0<c200

	c200_w = S.Task('c200_w', length=1, delay_cost=1)
	c200_w += alt(MAIN_MEM_w)
	S += c200 <= c200_w

	c200_mem0 = S.Task('c200_mem0', length=1, delay_cost=1)
	c200_mem0 += MAS_MEM[4]
	S += 52 < c200_mem0
	S += c200_mem0 <= c200

	c200_mem1 = S.Task('c200_mem1', length=1, delay_cost=1)
	c200_mem1 += alt(MAS_MEM)
	S += (c2_s00*MAS[0])-1 < c200_mem1*MAS_MEM[1]
	S += (c2_s00*MAS[1])-1 < c200_mem1*MAS_MEM[3]
	S += (c2_s00*MAS[2])-1 < c200_mem1*MAS_MEM[5]
	S += (c2_s00*MAS[3])-1 < c200_mem1*MAS_MEM[7]
	S += (c2_s00*MAS[4])-1 < c200_mem1*MAS_MEM[9]
	S += (c2_s00*MAS[5])-1 < c200_mem1*MAS_MEM[11]
	S += c200_mem1 <= c200

	c201 = S.Task('c201', length=2, delay_cost=1)
	c201 += alt(MAS)
	c201_in = S.Task('c201_in', length=1, delay_cost=1)
	c201_in += alt(MAS_in)
	S += c201_in*MAS_in[0]<=c201*MAS[0]

	S += c201_in*MAS_in[1]<=c201*MAS[1]

	S += c201_in*MAS_in[2]<=c201*MAS[2]

	S += c201_in*MAS_in[3]<=c201*MAS[3]

	S += c201_in*MAS_in[4]<=c201*MAS[4]

	S += c201_in*MAS_in[5]<=c201*MAS[5]

	S += 0<c201

	c201_w = S.Task('c201_w', length=1, delay_cost=1)
	c201_w += alt(MAIN_MEM_w)
	S += c201 <= c201_w

	c201_mem0 = S.Task('c201_mem0', length=1, delay_cost=1)
	c201_mem0 += MAS_MEM[10]
	S += 59 < c201_mem0
	S += c201_mem0 <= c201

	c201_mem1 = S.Task('c201_mem1', length=1, delay_cost=1)
	c201_mem1 += alt(MAS_MEM)
	S += (c2_s01*MAS[0])-1 < c201_mem1*MAS_MEM[1]
	S += (c2_s01*MAS[1])-1 < c201_mem1*MAS_MEM[3]
	S += (c2_s01*MAS[2])-1 < c201_mem1*MAS_MEM[5]
	S += (c2_s01*MAS[3])-1 < c201_mem1*MAS_MEM[7]
	S += (c2_s01*MAS[4])-1 < c201_mem1*MAS_MEM[9]
	S += (c2_s01*MAS[5])-1 < c201_mem1*MAS_MEM[11]
	S += c201_mem1 <= c201

	c211 = S.Task('c211', length=2, delay_cost=1)
	c211 += alt(MAS)
	c211_in = S.Task('c211_in', length=1, delay_cost=1)
	c211_in += alt(MAS_in)
	S += c211_in*MAS_in[0]<=c211*MAS[0]

	S += c211_in*MAS_in[1]<=c211*MAS[1]

	S += c211_in*MAS_in[2]<=c211*MAS[2]

	S += c211_in*MAS_in[3]<=c211*MAS[3]

	S += c211_in*MAS_in[4]<=c211*MAS[4]

	S += c211_in*MAS_in[5]<=c211*MAS[5]

	S += 0<c211

	c211_w = S.Task('c211_w', length=1, delay_cost=1)
	c211_w += alt(MAIN_MEM_w)
	S += c211 <= c211_w

	c211_mem0 = S.Task('c211_mem0', length=1, delay_cost=1)
	c211_mem0 += alt(MAS_MEM)
	S += (c2_t41*MAS[0])-1 < c211_mem0*MAS_MEM[0]
	S += (c2_t41*MAS[1])-1 < c211_mem0*MAS_MEM[2]
	S += (c2_t41*MAS[2])-1 < c211_mem0*MAS_MEM[4]
	S += (c2_t41*MAS[3])-1 < c211_mem0*MAS_MEM[6]
	S += (c2_t41*MAS[4])-1 < c211_mem0*MAS_MEM[8]
	S += (c2_t41*MAS[5])-1 < c211_mem0*MAS_MEM[10]
	S += c211_mem0 <= c211

	c211_mem1 = S.Task('c211_mem1', length=1, delay_cost=1)
	c211_mem1 += alt(MAS_MEM)
	S += (c2_t51*MAS[0])-1 < c211_mem1*MAS_MEM[1]
	S += (c2_t51*MAS[1])-1 < c211_mem1*MAS_MEM[3]
	S += (c2_t51*MAS[2])-1 < c211_mem1*MAS_MEM[5]
	S += (c2_t51*MAS[3])-1 < c211_mem1*MAS_MEM[7]
	S += (c2_t51*MAS[4])-1 < c211_mem1*MAS_MEM[9]
	S += (c2_t51*MAS[5])-1 < c211_mem1*MAS_MEM[11]
	S += c211_mem1 <= c211

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage11MM2_stage2MAS6/FP12_INV_AFTER_FPINV/schedule3.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

