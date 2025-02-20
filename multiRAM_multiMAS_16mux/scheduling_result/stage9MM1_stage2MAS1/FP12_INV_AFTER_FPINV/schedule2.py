from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 188
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=9)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=1)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=1, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=2)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c1_t21_in = S.Task('c1_t21_in', length=1, delay_cost=1)
	S += c1_t21_in >= 0
	c1_t21_in += MAS_in[0]

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	S += c1_t21_mem0 >= 0
	c1_t21_mem0 += MAIN_MEM_r[0]

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	S += c1_t21_mem1 >= 0
	c1_t21_mem1 += MAIN_MEM_r[1]

	c1_t20_in = S.Task('c1_t20_in', length=1, delay_cost=1)
	S += c1_t20_in >= 1
	c1_t20_in += MAS_in[0]

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	S += c1_t20_mem0 >= 1
	c1_t20_mem0 += MAIN_MEM_r[0]

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	S += c1_t20_mem1 >= 1
	c1_t20_mem1 += MAIN_MEM_r[1]

	c1_t21 = S.Task('c1_t21', length=2, delay_cost=1)
	S += c1_t21 >= 1
	c1_t21 += MAS[0]

	c1_t20 = S.Task('c1_t20', length=2, delay_cost=1)
	S += c1_t20 >= 2
	c1_t20 += MAS[0]

	c2_t21_in = S.Task('c2_t21_in', length=1, delay_cost=1)
	S += c2_t21_in >= 2
	c2_t21_in += MAS_in[0]

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	S += c2_t21_mem0 >= 2
	c2_t21_mem0 += MAIN_MEM_r[0]

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	S += c2_t21_mem1 >= 2
	c2_t21_mem1 += MAIN_MEM_r[1]

	c1_t4_t2_in = S.Task('c1_t4_t2_in', length=1, delay_cost=1)
	S += c1_t4_t2_in >= 3
	c1_t4_t2_in += MAS_in[0]

	c1_t4_t2_mem0 = S.Task('c1_t4_t2_mem0', length=1, delay_cost=1)
	S += c1_t4_t2_mem0 >= 3
	c1_t4_t2_mem0 += MAS_MEM[0]

	c1_t4_t2_mem1 = S.Task('c1_t4_t2_mem1', length=1, delay_cost=1)
	S += c1_t4_t2_mem1 >= 3
	c1_t4_t2_mem1 += MAS_MEM[1]

	c2_t21 = S.Task('c2_t21', length=2, delay_cost=1)
	S += c2_t21 >= 3
	c2_t21 += MAS[0]

	c_qinv_denom_inv0_in = S.Task('c_qinv_denom_inv0_in', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_in >= 3
	c_qinv_denom_inv0_in += MM_in[0]

	c_qinv_denom_inv0_mem0 = S.Task('c_qinv_denom_inv0_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem0 >= 3
	c_qinv_denom_inv0_mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv0_mem1 = S.Task('c_qinv_denom_inv0_mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem1 >= 3
	c_qinv_denom_inv0_mem1 += MAIN_MEM_r[1]

	c1_t4_t2 = S.Task('c1_t4_t2', length=2, delay_cost=1)
	S += c1_t4_t2 >= 4
	c1_t4_t2 += MAS[0]

	c2_t20_in = S.Task('c2_t20_in', length=1, delay_cost=1)
	S += c2_t20_in >= 4
	c2_t20_in += MAS_in[0]

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	S += c2_t20_mem0 >= 4
	c2_t20_mem0 += MAIN_MEM_r[0]

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	S += c2_t20_mem1 >= 4
	c2_t20_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv0 = S.Task('c_qinv_denom_inv0', length=9, delay_cost=1)
	S += c_qinv_denom_inv0 >= 4
	c_qinv_denom_inv0 += MM[0]

	c0_t20_in = S.Task('c0_t20_in', length=1, delay_cost=1)
	S += c0_t20_in >= 5
	c0_t20_in += MAS_in[0]

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	S += c0_t20_mem0 >= 5
	c0_t20_mem0 += MAIN_MEM_r[0]

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	S += c0_t20_mem1 >= 5
	c0_t20_mem1 += MAIN_MEM_r[1]

	c2_t20 = S.Task('c2_t20', length=2, delay_cost=1)
	S += c2_t20 >= 5
	c2_t20 += MAS[0]

	c0_t20 = S.Task('c0_t20', length=2, delay_cost=1)
	S += c0_t20 >= 6
	c0_t20 += MAS[0]

	c2_t4_t2_in = S.Task('c2_t4_t2_in', length=1, delay_cost=1)
	S += c2_t4_t2_in >= 6
	c2_t4_t2_in += MAS_in[0]

	c2_t4_t2_mem0 = S.Task('c2_t4_t2_mem0', length=1, delay_cost=1)
	S += c2_t4_t2_mem0 >= 6
	c2_t4_t2_mem0 += MAS_MEM[0]

	c2_t4_t2_mem1 = S.Task('c2_t4_t2_mem1', length=1, delay_cost=1)
	S += c2_t4_t2_mem1 >= 6
	c2_t4_t2_mem1 += MAS_MEM[1]

	c_qinv_denom_inv1__in = S.Task('c_qinv_denom_inv1__in', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__in >= 6
	c_qinv_denom_inv1__in += MM_in[0]

	c_qinv_denom_inv1__mem0 = S.Task('c_qinv_denom_inv1__mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem0 >= 6
	c_qinv_denom_inv1__mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv1__mem1 = S.Task('c_qinv_denom_inv1__mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem1 >= 6
	c_qinv_denom_inv1__mem1 += MAIN_MEM_r[1]

	c0_t21_in = S.Task('c0_t21_in', length=1, delay_cost=1)
	S += c0_t21_in >= 7
	c0_t21_in += MAS_in[0]

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	S += c0_t21_mem0 >= 7
	c0_t21_mem0 += MAIN_MEM_r[0]

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	S += c0_t21_mem1 >= 7
	c0_t21_mem1 += MAIN_MEM_r[1]

	c2_t4_t2 = S.Task('c2_t4_t2', length=2, delay_cost=1)
	S += c2_t4_t2 >= 7
	c2_t4_t2 += MAS[0]

	c_qinv_denom_inv1_ = S.Task('c_qinv_denom_inv1_', length=9, delay_cost=1)
	S += c_qinv_denom_inv1_ >= 7
	c_qinv_denom_inv1_ += MM[0]

	c0_t21 = S.Task('c0_t21', length=2, delay_cost=1)
	S += c0_t21 >= 8
	c0_t21 += MAS[0]

	c_qinv0_t2_in = S.Task('c_qinv0_t2_in', length=1, delay_cost=1)
	S += c_qinv0_t2_in >= 8
	c_qinv0_t2_in += MAS_in[0]

	c_qinv0_t2_mem0 = S.Task('c_qinv0_t2_mem0', length=1, delay_cost=1)
	S += c_qinv0_t2_mem0 >= 8
	c_qinv0_t2_mem0 += MAIN_MEM_r[0]

	c_qinv0_t2_mem1 = S.Task('c_qinv0_t2_mem1', length=1, delay_cost=1)
	S += c_qinv0_t2_mem1 >= 8
	c_qinv0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t2 = S.Task('c_qinv0_t2', length=2, delay_cost=1)
	S += c_qinv0_t2 >= 9
	c_qinv0_t2 += MAS[0]

	c_qinv1__t2_in = S.Task('c_qinv1__t2_in', length=1, delay_cost=1)
	S += c_qinv1__t2_in >= 9
	c_qinv1__t2_in += MAS_in[0]

	c_qinv1__t2_mem0 = S.Task('c_qinv1__t2_mem0', length=1, delay_cost=1)
	S += c_qinv1__t2_mem0 >= 9
	c_qinv1__t2_mem0 += MAIN_MEM_r[0]

	c_qinv1__t2_mem1 = S.Task('c_qinv1__t2_mem1', length=1, delay_cost=1)
	S += c_qinv1__t2_mem1 >= 9
	c_qinv1__t2_mem1 += MAIN_MEM_r[1]

	c2_t1_t2_in = S.Task('c2_t1_t2_in', length=1, delay_cost=1)
	S += c2_t1_t2_in >= 10
	c2_t1_t2_in += MAS_in[0]

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	S += c2_t1_t2_mem0 >= 10
	c2_t1_t2_mem0 += MAIN_MEM_r[0]

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	S += c2_t1_t2_mem1 >= 10
	c2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t2 = S.Task('c_qinv1__t2', length=2, delay_cost=1)
	S += c_qinv1__t2 >= 10
	c_qinv1__t2 += MAS[0]

	c0_t0_t2_in = S.Task('c0_t0_t2_in', length=1, delay_cost=1)
	S += c0_t0_t2_in >= 11
	c0_t0_t2_in += MAS_in[0]

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
	c0_t0_t2 += MAS[0]

	c0_t4_t2_in = S.Task('c0_t4_t2_in', length=1, delay_cost=1)
	S += c0_t4_t2_in >= 12
	c0_t4_t2_in += MAS_in[0]

	c0_t4_t2_mem0 = S.Task('c0_t4_t2_mem0', length=1, delay_cost=1)
	S += c0_t4_t2_mem0 >= 12
	c0_t4_t2_mem0 += MAS_MEM[0]

	c0_t4_t2_mem1 = S.Task('c0_t4_t2_mem1', length=1, delay_cost=1)
	S += c0_t4_t2_mem1 >= 12
	c0_t4_t2_mem1 += MAS_MEM[1]

	c_qinv0_t0_in = S.Task('c_qinv0_t0_in', length=1, delay_cost=1)
	S += c_qinv0_t0_in >= 12
	c_qinv0_t0_in += MM_in[0]

	c_qinv0_t0_mem0 = S.Task('c_qinv0_t0_mem0', length=1, delay_cost=1)
	S += c_qinv0_t0_mem0 >= 12
	c_qinv0_t0_mem0 += MAIN_MEM_r[0]

	c_qinv0_t0_mem1 = S.Task('c_qinv0_t0_mem1', length=1, delay_cost=1)
	S += c_qinv0_t0_mem1 >= 12
	c_qinv0_t0_mem1 += MM_MEM[1]

	c0_t4_t2 = S.Task('c0_t4_t2', length=2, delay_cost=1)
	S += c0_t4_t2 >= 13
	c0_t4_t2 += MAS[0]

	c1_t1_t2_in = S.Task('c1_t1_t2_in', length=1, delay_cost=1)
	S += c1_t1_t2_in >= 13
	c1_t1_t2_in += MAS_in[0]

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	S += c1_t1_t2_mem0 >= 13
	c1_t1_t2_mem0 += MAIN_MEM_r[0]

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	S += c1_t1_t2_mem1 >= 13
	c1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t0 = S.Task('c_qinv0_t0', length=9, delay_cost=1)
	S += c_qinv0_t0 >= 13
	c_qinv0_t0 += MM[0]

	c1_t0_t2_in = S.Task('c1_t0_t2_in', length=1, delay_cost=1)
	S += c1_t0_t2_in >= 14
	c1_t0_t2_in += MAS_in[0]

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	S += c1_t0_t2_mem0 >= 14
	c1_t0_t2_mem0 += MAIN_MEM_r[0]

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	S += c1_t0_t2_mem1 >= 14
	c1_t0_t2_mem1 += MAIN_MEM_r[1]

	c1_t1_t2 = S.Task('c1_t1_t2', length=2, delay_cost=1)
	S += c1_t1_t2 >= 14
	c1_t1_t2 += MAS[0]

	c1_t0_t2 = S.Task('c1_t0_t2', length=2, delay_cost=1)
	S += c1_t0_t2 >= 15
	c1_t0_t2 += MAS[0]

	c_qinv1__t1_in = S.Task('c_qinv1__t1_in', length=1, delay_cost=1)
	S += c_qinv1__t1_in >= 15
	c_qinv1__t1_in += MM_in[0]

	c_qinv1__t1_mem0 = S.Task('c_qinv1__t1_mem0', length=1, delay_cost=1)
	S += c_qinv1__t1_mem0 >= 15
	c_qinv1__t1_mem0 += MAIN_MEM_r[0]

	c_qinv1__t1_mem1 = S.Task('c_qinv1__t1_mem1', length=1, delay_cost=1)
	S += c_qinv1__t1_mem1 >= 15
	c_qinv1__t1_mem1 += MM_MEM[1]

	c2_t0_t2_in = S.Task('c2_t0_t2_in', length=1, delay_cost=1)
	S += c2_t0_t2_in >= 16
	c2_t0_t2_in += MAS_in[0]

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	S += c2_t0_t2_mem0 >= 16
	c2_t0_t2_mem0 += MAIN_MEM_r[0]

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	S += c2_t0_t2_mem1 >= 16
	c2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t1 = S.Task('c_qinv1__t1', length=9, delay_cost=1)
	S += c_qinv1__t1 >= 16
	c_qinv1__t1 += MM[0]

	c0_t1_t2_in = S.Task('c0_t1_t2_in', length=1, delay_cost=1)
	S += c0_t1_t2_in >= 17
	c0_t1_t2_in += MAS_in[0]

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	S += c0_t1_t2_mem0 >= 17
	c0_t1_t2_mem0 += MAIN_MEM_r[0]

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	S += c0_t1_t2_mem1 >= 17
	c0_t1_t2_mem1 += MAIN_MEM_r[1]

	c2_t0_t2 = S.Task('c2_t0_t2', length=2, delay_cost=1)
	S += c2_t0_t2 >= 17
	c2_t0_t2 += MAS[0]

	c0_t1_t2 = S.Task('c0_t1_t2', length=2, delay_cost=1)
	S += c0_t1_t2 >= 18
	c0_t1_t2 += MAS[0]

	c_qinv0_t3_in = S.Task('c_qinv0_t3_in', length=1, delay_cost=1)
	S += c_qinv0_t3_in >= 18
	c_qinv0_t3_in += MAS_in[0]

	c_qinv0_t3_mem0 = S.Task('c_qinv0_t3_mem0', length=1, delay_cost=1)
	S += c_qinv0_t3_mem0 >= 18
	c_qinv0_t3_mem0 += MM_MEM[0]

	c_qinv0_t3_mem1 = S.Task('c_qinv0_t3_mem1', length=1, delay_cost=1)
	S += c_qinv0_t3_mem1 >= 18
	c_qinv0_t3_mem1 += MM_MEM[1]

	c_qinv0_t3 = S.Task('c_qinv0_t3', length=2, delay_cost=1)
	S += c_qinv0_t3 >= 19
	c_qinv0_t3 += MAS[0]

	c_qinv1__t0_in = S.Task('c_qinv1__t0_in', length=1, delay_cost=1)
	S += c_qinv1__t0_in >= 19
	c_qinv1__t0_in += MM_in[0]

	c_qinv1__t0_mem0 = S.Task('c_qinv1__t0_mem0', length=1, delay_cost=1)
	S += c_qinv1__t0_mem0 >= 19
	c_qinv1__t0_mem0 += MAIN_MEM_r[0]

	c_qinv1__t0_mem1 = S.Task('c_qinv1__t0_mem1', length=1, delay_cost=1)
	S += c_qinv1__t0_mem1 >= 19
	c_qinv1__t0_mem1 += MM_MEM[1]

	c_qinv0_t1_in = S.Task('c_qinv0_t1_in', length=1, delay_cost=1)
	S += c_qinv0_t1_in >= 20
	c_qinv0_t1_in += MM_in[0]

	c_qinv0_t1_mem0 = S.Task('c_qinv0_t1_mem0', length=1, delay_cost=1)
	S += c_qinv0_t1_mem0 >= 20
	c_qinv0_t1_mem0 += MAIN_MEM_r[0]

	c_qinv0_t1_mem1 = S.Task('c_qinv0_t1_mem1', length=1, delay_cost=1)
	S += c_qinv0_t1_mem1 >= 20
	c_qinv0_t1_mem1 += MM_MEM[1]

	c_qinv1__t0 = S.Task('c_qinv1__t0', length=9, delay_cost=1)
	S += c_qinv1__t0 >= 20
	c_qinv1__t0 += MM[0]

	c_qinv0_t1 = S.Task('c_qinv0_t1', length=9, delay_cost=1)
	S += c_qinv0_t1 >= 21
	c_qinv0_t1 += MM[0]

	c_qinv0_t4_in = S.Task('c_qinv0_t4_in', length=1, delay_cost=1)
	S += c_qinv0_t4_in >= 21
	c_qinv0_t4_in += MM_in[0]

	c_qinv0_t4_mem0 = S.Task('c_qinv0_t4_mem0', length=1, delay_cost=1)
	S += c_qinv0_t4_mem0 >= 21
	c_qinv0_t4_mem0 += MAS_MEM[0]

	c_qinv0_t4_mem1 = S.Task('c_qinv0_t4_mem1', length=1, delay_cost=1)
	S += c_qinv0_t4_mem1 >= 21
	c_qinv0_t4_mem1 += MAS_MEM[1]

	c_qinv1__t3_in = S.Task('c_qinv1__t3_in', length=1, delay_cost=1)
	S += c_qinv1__t3_in >= 21
	c_qinv1__t3_in += MAS_in[0]

	c_qinv1__t3_mem0 = S.Task('c_qinv1__t3_mem0', length=1, delay_cost=1)
	S += c_qinv1__t3_mem0 >= 21
	c_qinv1__t3_mem0 += MM_MEM[0]

	c_qinv1__t3_mem1 = S.Task('c_qinv1__t3_mem1', length=1, delay_cost=1)
	S += c_qinv1__t3_mem1 >= 21
	c_qinv1__t3_mem1 += MM_MEM[1]

	c_qinv0_t4 = S.Task('c_qinv0_t4', length=9, delay_cost=1)
	S += c_qinv0_t4 >= 22
	c_qinv0_t4 += MM[0]

	c_qinv1__t3 = S.Task('c_qinv1__t3', length=2, delay_cost=1)
	S += c_qinv1__t3 >= 22
	c_qinv1__t3 += MAS[0]

	c_qinv1__t4_in = S.Task('c_qinv1__t4_in', length=1, delay_cost=1)
	S += c_qinv1__t4_in >= 23
	c_qinv1__t4_in += MM_in[0]

	c_qinv1__t4_mem0 = S.Task('c_qinv1__t4_mem0', length=1, delay_cost=1)
	S += c_qinv1__t4_mem0 >= 23
	c_qinv1__t4_mem0 += MAS_MEM[0]

	c_qinv1__t4_mem1 = S.Task('c_qinv1__t4_mem1', length=1, delay_cost=1)
	S += c_qinv1__t4_mem1 >= 23
	c_qinv1__t4_mem1 += MAS_MEM[1]

	c_qinv1__t4 = S.Task('c_qinv1__t4', length=9, delay_cost=1)
	S += c_qinv1__t4 >= 24
	c_qinv1__t4 += MM[0]

	c_qinv1_0_in = S.Task('c_qinv1_0_in', length=1, delay_cost=1)
	S += c_qinv1_0_in >= 28
	c_qinv1_0_in += MAS_in[0]

	c_qinv1_0_mem0 = S.Task('c_qinv1_0_mem0', length=1, delay_cost=1)
	S += c_qinv1_0_mem0 >= 28
	c_qinv1_0_mem0 += MM_MEM[0]

	c_qinv1_0_mem1 = S.Task('c_qinv1_0_mem1', length=1, delay_cost=1)
	S += c_qinv1_0_mem1 >= 28
	c_qinv1_0_mem1 += MM_MEM[1]

	c_qinv00_in = S.Task('c_qinv00_in', length=1, delay_cost=1)
	S += c_qinv00_in >= 29
	c_qinv00_in += MAS_in[0]

	c_qinv00_mem0 = S.Task('c_qinv00_mem0', length=1, delay_cost=1)
	S += c_qinv00_mem0 >= 29
	c_qinv00_mem0 += MM_MEM[0]

	c_qinv00_mem1 = S.Task('c_qinv00_mem1', length=1, delay_cost=1)
	S += c_qinv00_mem1 >= 29
	c_qinv00_mem1 += MM_MEM[1]

	c_qinv1_0 = S.Task('c_qinv1_0', length=2, delay_cost=1)
	S += c_qinv1_0 >= 29
	c_qinv1_0 += MAS[0]

	c1_t1_t0_in = S.Task('c1_t1_t0_in', length=1, delay_cost=1)
	S += c1_t1_t0_in >= 30
	c1_t1_t0_in += MM_in[0]

	c1_t1_t0_mem0 = S.Task('c1_t1_t0_mem0', length=1, delay_cost=1)
	S += c1_t1_t0_mem0 >= 30
	c1_t1_t0_mem0 += MAIN_MEM_r[0]

	c1_t1_t0_mem1 = S.Task('c1_t1_t0_mem1', length=1, delay_cost=1)
	S += c1_t1_t0_mem1 >= 30
	c1_t1_t0_mem1 += MAS_MEM[1]

	c_qinv00 = S.Task('c_qinv00', length=2, delay_cost=1)
	S += c_qinv00 >= 30
	c_qinv00 += MAS[0]

	c_qinv1__t5_in = S.Task('c_qinv1__t5_in', length=1, delay_cost=1)
	S += c_qinv1__t5_in >= 30
	c_qinv1__t5_in += MAS_in[0]

	c_qinv1__t5_mem0 = S.Task('c_qinv1__t5_mem0', length=1, delay_cost=1)
	S += c_qinv1__t5_mem0 >= 30
	c_qinv1__t5_mem0 += MM_MEM[0]

	c_qinv1__t5_mem1 = S.Task('c_qinv1__t5_mem1', length=1, delay_cost=1)
	S += c_qinv1__t5_mem1 >= 30
	c_qinv1__t5_mem1 += MM_MEM[1]

	c1_t1_t0 = S.Task('c1_t1_t0', length=9, delay_cost=1)
	S += c1_t1_t0 >= 31
	c1_t1_t0 += MM[0]

	c2_t1_t0_in = S.Task('c2_t1_t0_in', length=1, delay_cost=1)
	S += c2_t1_t0_in >= 31
	c2_t1_t0_in += MM_in[0]

	c2_t1_t0_mem0 = S.Task('c2_t1_t0_mem0', length=1, delay_cost=1)
	S += c2_t1_t0_mem0 >= 31
	c2_t1_t0_mem0 += MAIN_MEM_r[0]

	c2_t1_t0_mem1 = S.Task('c2_t1_t0_mem1', length=1, delay_cost=1)
	S += c2_t1_t0_mem1 >= 31
	c2_t1_t0_mem1 += MAS_MEM[1]

	c_qinv0_t5_in = S.Task('c_qinv0_t5_in', length=1, delay_cost=1)
	S += c_qinv0_t5_in >= 31
	c_qinv0_t5_in += MAS_in[0]

	c_qinv0_t5_mem0 = S.Task('c_qinv0_t5_mem0', length=1, delay_cost=1)
	S += c_qinv0_t5_mem0 >= 31
	c_qinv0_t5_mem0 += MM_MEM[0]

	c_qinv0_t5_mem1 = S.Task('c_qinv0_t5_mem1', length=1, delay_cost=1)
	S += c_qinv0_t5_mem1 >= 31
	c_qinv0_t5_mem1 += MM_MEM[1]

	c_qinv1__t5 = S.Task('c_qinv1__t5', length=2, delay_cost=1)
	S += c_qinv1__t5 >= 31
	c_qinv1__t5 += MAS[0]

	c2_t1_t0 = S.Task('c2_t1_t0', length=9, delay_cost=1)
	S += c2_t1_t0 >= 32
	c2_t1_t0 += MM[0]

	c_qinv0_t5 = S.Task('c_qinv0_t5', length=2, delay_cost=1)
	S += c_qinv0_t5 >= 32
	c_qinv0_t5 += MAS[0]

	c_qinv1_1_in = S.Task('c_qinv1_1_in', length=1, delay_cost=1)
	S += c_qinv1_1_in >= 32
	c_qinv1_1_in += MAS_in[0]

	c_qinv1_1_mem0 = S.Task('c_qinv1_1_mem0', length=1, delay_cost=1)
	S += c_qinv1_1_mem0 >= 32
	c_qinv1_1_mem0 += MM_MEM[0]

	c_qinv1_1_mem1 = S.Task('c_qinv1_1_mem1', length=1, delay_cost=1)
	S += c_qinv1_1_mem1 >= 32
	c_qinv1_1_mem1 += MAS_MEM[1]

	c2_t0_t0_in = S.Task('c2_t0_t0_in', length=1, delay_cost=1)
	S += c2_t0_t0_in >= 33
	c2_t0_t0_in += MM_in[0]

	c2_t0_t0_mem0 = S.Task('c2_t0_t0_mem0', length=1, delay_cost=1)
	S += c2_t0_t0_mem0 >= 33
	c2_t0_t0_mem0 += MAIN_MEM_r[0]

	c2_t0_t0_mem1 = S.Task('c2_t0_t0_mem1', length=1, delay_cost=1)
	S += c2_t0_t0_mem1 >= 33
	c2_t0_t0_mem1 += MAS_MEM[1]

	c_qinv1_1 = S.Task('c_qinv1_1', length=2, delay_cost=1)
	S += c_qinv1_1 >= 33
	c_qinv1_1 += MAS[0]

	c2_t0_t0 = S.Task('c2_t0_t0', length=9, delay_cost=1)
	S += c2_t0_t0 >= 34
	c2_t0_t0 += MM[0]

	c2_t30_in = S.Task('c2_t30_in', length=1, delay_cost=1)
	S += c2_t30_in >= 34
	c2_t30_in += MAS_in[0]

	c2_t30_mem0 = S.Task('c2_t30_mem0', length=1, delay_cost=1)
	S += c2_t30_mem0 >= 34
	c2_t30_mem0 += MAS_MEM[0]

	c2_t30_mem1 = S.Task('c2_t30_mem1', length=1, delay_cost=1)
	S += c2_t30_mem1 >= 34
	c2_t30_mem1 += MAS_MEM[1]

	c1_t1_t3_in = S.Task('c1_t1_t3_in', length=1, delay_cost=1)
	S += c1_t1_t3_in >= 35
	c1_t1_t3_in += MAS_in[0]

	c1_t1_t3_mem0 = S.Task('c1_t1_t3_mem0', length=1, delay_cost=1)
	S += c1_t1_t3_mem0 >= 35
	c1_t1_t3_mem0 += MAS_MEM[0]

	c1_t1_t3_mem1 = S.Task('c1_t1_t3_mem1', length=1, delay_cost=1)
	S += c1_t1_t3_mem1 >= 35
	c1_t1_t3_mem1 += MAS_MEM[1]

	c2_t30 = S.Task('c2_t30', length=2, delay_cost=1)
	S += c2_t30 >= 35
	c2_t30 += MAS[0]

	c1_t1_t3 = S.Task('c1_t1_t3', length=2, delay_cost=1)
	S += c1_t1_t3 >= 36
	c1_t1_t3 += MAS[0]

	c2_t1_t1_in = S.Task('c2_t1_t1_in', length=1, delay_cost=1)
	S += c2_t1_t1_in >= 36
	c2_t1_t1_in += MM_in[0]

	c2_t1_t1_mem0 = S.Task('c2_t1_t1_mem0', length=1, delay_cost=1)
	S += c2_t1_t1_mem0 >= 36
	c2_t1_t1_mem0 += MAIN_MEM_r[0]

	c2_t1_t1_mem1 = S.Task('c2_t1_t1_mem1', length=1, delay_cost=1)
	S += c2_t1_t1_mem1 >= 36
	c2_t1_t1_mem1 += MAS_MEM[1]

	c2_t1_t1 = S.Task('c2_t1_t1', length=9, delay_cost=1)
	S += c2_t1_t1 >= 37
	c2_t1_t1 += MM[0]

	c_qinv01_in = S.Task('c_qinv01_in', length=1, delay_cost=1)
	S += c_qinv01_in >= 37
	c_qinv01_in += MAS_in[0]

	c_qinv01_mem0 = S.Task('c_qinv01_mem0', length=1, delay_cost=1)
	S += c_qinv01_mem0 >= 37
	c_qinv01_mem0 += MM_MEM[0]

	c_qinv01_mem1 = S.Task('c_qinv01_mem1', length=1, delay_cost=1)
	S += c_qinv01_mem1 >= 37
	c_qinv01_mem1 += MAS_MEM[1]

	c0_t0_t0_in = S.Task('c0_t0_t0_in', length=1, delay_cost=1)
	S += c0_t0_t0_in >= 38
	c0_t0_t0_in += MM_in[0]

	c0_t0_t0_mem0 = S.Task('c0_t0_t0_mem0', length=1, delay_cost=1)
	S += c0_t0_t0_mem0 >= 38
	c0_t0_t0_mem0 += MAIN_MEM_r[0]

	c0_t0_t0_mem1 = S.Task('c0_t0_t0_mem1', length=1, delay_cost=1)
	S += c0_t0_t0_mem1 >= 38
	c0_t0_t0_mem1 += MAS_MEM[1]

	c_qinv01 = S.Task('c_qinv01', length=2, delay_cost=1)
	S += c_qinv01 >= 38
	c_qinv01 += MAS[0]

	c0_t0_t0 = S.Task('c0_t0_t0', length=9, delay_cost=1)
	S += c0_t0_t0 >= 39
	c0_t0_t0 += MM[0]

	c0_t30_in = S.Task('c0_t30_in', length=1, delay_cost=1)
	S += c0_t30_in >= 39
	c0_t30_in += MAS_in[0]

	c0_t30_mem0 = S.Task('c0_t30_mem0', length=1, delay_cost=1)
	S += c0_t30_mem0 >= 39
	c0_t30_mem0 += MAS_MEM[0]

	c0_t30_mem1 = S.Task('c0_t30_mem1', length=1, delay_cost=1)
	S += c0_t30_mem1 >= 39
	c0_t30_mem1 += MAS_MEM[1]

	c0_t1_t0_in = S.Task('c0_t1_t0_in', length=1, delay_cost=1)
	S += c0_t1_t0_in >= 40
	c0_t1_t0_in += MM_in[0]

	c0_t1_t0_mem0 = S.Task('c0_t1_t0_mem0', length=1, delay_cost=1)
	S += c0_t1_t0_mem0 >= 40
	c0_t1_t0_mem0 += MAIN_MEM_r[0]

	c0_t1_t0_mem1 = S.Task('c0_t1_t0_mem1', length=1, delay_cost=1)
	S += c0_t1_t0_mem1 >= 40
	c0_t1_t0_mem1 += MAS_MEM[1]

	c0_t30 = S.Task('c0_t30', length=2, delay_cost=1)
	S += c0_t30 >= 40
	c0_t30 += MAS[0]

	c0_t0_t1_in = S.Task('c0_t0_t1_in', length=1, delay_cost=1)
	S += c0_t0_t1_in >= 41
	c0_t0_t1_in += MM_in[0]

	c0_t0_t1_mem0 = S.Task('c0_t0_t1_mem0', length=1, delay_cost=1)
	S += c0_t0_t1_mem0 >= 41
	c0_t0_t1_mem0 += MAIN_MEM_r[0]

	c0_t0_t1_mem1 = S.Task('c0_t0_t1_mem1', length=1, delay_cost=1)
	S += c0_t0_t1_mem1 >= 41
	c0_t0_t1_mem1 += MAS_MEM[1]

	c0_t1_t0 = S.Task('c0_t1_t0', length=9, delay_cost=1)
	S += c0_t1_t0 >= 41
	c0_t1_t0 += MM[0]

	c0_t0_t1 = S.Task('c0_t0_t1', length=9, delay_cost=1)
	S += c0_t0_t1 >= 42
	c0_t0_t1 += MM[0]

	c2_t31_in = S.Task('c2_t31_in', length=1, delay_cost=1)
	S += c2_t31_in >= 42
	c2_t31_in += MAS_in[0]

	c2_t31_mem0 = S.Task('c2_t31_mem0', length=1, delay_cost=1)
	S += c2_t31_mem0 >= 42
	c2_t31_mem0 += MAS_MEM[0]

	c2_t31_mem1 = S.Task('c2_t31_mem1', length=1, delay_cost=1)
	S += c2_t31_mem1 >= 42
	c2_t31_mem1 += MAS_MEM[1]

	c1_t31_in = S.Task('c1_t31_in', length=1, delay_cost=1)
	S += c1_t31_in >= 43
	c1_t31_in += MAS_in[0]

	c1_t31_mem0 = S.Task('c1_t31_mem0', length=1, delay_cost=1)
	S += c1_t31_mem0 >= 43
	c1_t31_mem0 += MAS_MEM[0]

	c1_t31_mem1 = S.Task('c1_t31_mem1', length=1, delay_cost=1)
	S += c1_t31_mem1 >= 43
	c1_t31_mem1 += MAS_MEM[1]

	c2_t31 = S.Task('c2_t31', length=2, delay_cost=1)
	S += c2_t31 >= 43
	c2_t31 += MAS[0]

	c1_t31 = S.Task('c1_t31', length=2, delay_cost=1)
	S += c1_t31 >= 44
	c1_t31 += MAS[0]

	c2_t4_t0_in = S.Task('c2_t4_t0_in', length=1, delay_cost=1)
	S += c2_t4_t0_in >= 44
	c2_t4_t0_in += MM_in[0]

	c2_t4_t0_mem0 = S.Task('c2_t4_t0_mem0', length=1, delay_cost=1)
	S += c2_t4_t0_mem0 >= 44
	c2_t4_t0_mem0 += MAS_MEM[0]

	c2_t4_t0_mem1 = S.Task('c2_t4_t0_mem1', length=1, delay_cost=1)
	S += c2_t4_t0_mem1 >= 44
	c2_t4_t0_mem1 += MAS_MEM[1]

	c2_t1_t3_in = S.Task('c2_t1_t3_in', length=1, delay_cost=1)
	S += c2_t1_t3_in >= 45
	c2_t1_t3_in += MAS_in[0]

	c2_t1_t3_mem0 = S.Task('c2_t1_t3_mem0', length=1, delay_cost=1)
	S += c2_t1_t3_mem0 >= 45
	c2_t1_t3_mem0 += MAS_MEM[0]

	c2_t1_t3_mem1 = S.Task('c2_t1_t3_mem1', length=1, delay_cost=1)
	S += c2_t1_t3_mem1 >= 45
	c2_t1_t3_mem1 += MAS_MEM[1]

	c2_t4_t0 = S.Task('c2_t4_t0', length=9, delay_cost=1)
	S += c2_t4_t0 >= 45
	c2_t4_t0 += MM[0]

	c2_t0_t3_in = S.Task('c2_t0_t3_in', length=1, delay_cost=1)
	S += c2_t0_t3_in >= 46
	c2_t0_t3_in += MAS_in[0]

	c2_t0_t3_mem0 = S.Task('c2_t0_t3_mem0', length=1, delay_cost=1)
	S += c2_t0_t3_mem0 >= 46
	c2_t0_t3_mem0 += MAS_MEM[0]

	c2_t0_t3_mem1 = S.Task('c2_t0_t3_mem1', length=1, delay_cost=1)
	S += c2_t0_t3_mem1 >= 46
	c2_t0_t3_mem1 += MAS_MEM[1]

	c2_t1_t3 = S.Task('c2_t1_t3', length=2, delay_cost=1)
	S += c2_t1_t3 >= 46
	c2_t1_t3 += MAS[0]

	c1_t30_in = S.Task('c1_t30_in', length=1, delay_cost=1)
	S += c1_t30_in >= 47
	c1_t30_in += MAS_in[0]

	c1_t30_mem0 = S.Task('c1_t30_mem0', length=1, delay_cost=1)
	S += c1_t30_mem0 >= 47
	c1_t30_mem0 += MAS_MEM[0]

	c1_t30_mem1 = S.Task('c1_t30_mem1', length=1, delay_cost=1)
	S += c1_t30_mem1 >= 47
	c1_t30_mem1 += MAS_MEM[1]

	c2_t0_t3 = S.Task('c2_t0_t3', length=2, delay_cost=1)
	S += c2_t0_t3 >= 47
	c2_t0_t3 += MAS[0]

	c1_t30 = S.Task('c1_t30', length=2, delay_cost=1)
	S += c1_t30 >= 48
	c1_t30 += MAS[0]

	c2_t0_t1_in = S.Task('c2_t0_t1_in', length=1, delay_cost=1)
	S += c2_t0_t1_in >= 48
	c2_t0_t1_in += MM_in[0]

	c2_t0_t1_mem0 = S.Task('c2_t0_t1_mem0', length=1, delay_cost=1)
	S += c2_t0_t1_mem0 >= 48
	c2_t0_t1_mem0 += MAIN_MEM_r[0]

	c2_t0_t1_mem1 = S.Task('c2_t0_t1_mem1', length=1, delay_cost=1)
	S += c2_t0_t1_mem1 >= 48
	c2_t0_t1_mem1 += MAS_MEM[1]

	c1_t0_t1_in = S.Task('c1_t0_t1_in', length=1, delay_cost=1)
	S += c1_t0_t1_in >= 49
	c1_t0_t1_in += MM_in[0]

	c1_t0_t1_mem0 = S.Task('c1_t0_t1_mem0', length=1, delay_cost=1)
	S += c1_t0_t1_mem0 >= 49
	c1_t0_t1_mem0 += MAIN_MEM_r[0]

	c1_t0_t1_mem1 = S.Task('c1_t0_t1_mem1', length=1, delay_cost=1)
	S += c1_t0_t1_mem1 >= 49
	c1_t0_t1_mem1 += MAS_MEM[1]

	c2_t0_t1 = S.Task('c2_t0_t1', length=9, delay_cost=1)
	S += c2_t0_t1 >= 49
	c2_t0_t1 += MM[0]

	c0_t4_t0_in = S.Task('c0_t4_t0_in', length=1, delay_cost=1)
	S += c0_t4_t0_in >= 50
	c0_t4_t0_in += MM_in[0]

	c0_t4_t0_mem0 = S.Task('c0_t4_t0_mem0', length=1, delay_cost=1)
	S += c0_t4_t0_mem0 >= 50
	c0_t4_t0_mem0 += MAS_MEM[0]

	c0_t4_t0_mem1 = S.Task('c0_t4_t0_mem1', length=1, delay_cost=1)
	S += c0_t4_t0_mem1 >= 50
	c0_t4_t0_mem1 += MAS_MEM[1]

	c1_t0_t1 = S.Task('c1_t0_t1', length=9, delay_cost=1)
	S += c1_t0_t1 >= 50
	c1_t0_t1 += MM[0]

	c0_t4_t0 = S.Task('c0_t4_t0', length=9, delay_cost=1)
	S += c0_t4_t0 >= 51
	c0_t4_t0 += MM[0]

	c1_t1_t1_in = S.Task('c1_t1_t1_in', length=1, delay_cost=1)
	S += c1_t1_t1_in >= 51
	c1_t1_t1_in += MM_in[0]

	c1_t1_t1_mem0 = S.Task('c1_t1_t1_mem0', length=1, delay_cost=1)
	S += c1_t1_t1_mem0 >= 51
	c1_t1_t1_mem0 += MAIN_MEM_r[0]

	c1_t1_t1_mem1 = S.Task('c1_t1_t1_mem1', length=1, delay_cost=1)
	S += c1_t1_t1_mem1 >= 51
	c1_t1_t1_mem1 += MAS_MEM[1]

	c1_t0_t0_in = S.Task('c1_t0_t0_in', length=1, delay_cost=1)
	S += c1_t0_t0_in >= 52
	c1_t0_t0_in += MM_in[0]

	c1_t0_t0_mem0 = S.Task('c1_t0_t0_mem0', length=1, delay_cost=1)
	S += c1_t0_t0_mem0 >= 52
	c1_t0_t0_mem0 += MAIN_MEM_r[0]

	c1_t0_t0_mem1 = S.Task('c1_t0_t0_mem1', length=1, delay_cost=1)
	S += c1_t0_t0_mem1 >= 52
	c1_t0_t0_mem1 += MAS_MEM[1]

	c1_t1_t1 = S.Task('c1_t1_t1', length=9, delay_cost=1)
	S += c1_t1_t1 >= 52
	c1_t1_t1 += MM[0]

	c0_t31_in = S.Task('c0_t31_in', length=1, delay_cost=1)
	S += c0_t31_in >= 53
	c0_t31_in += MAS_in[0]

	c0_t31_mem0 = S.Task('c0_t31_mem0', length=1, delay_cost=1)
	S += c0_t31_mem0 >= 53
	c0_t31_mem0 += MAS_MEM[0]

	c0_t31_mem1 = S.Task('c0_t31_mem1', length=1, delay_cost=1)
	S += c0_t31_mem1 >= 53
	c0_t31_mem1 += MAS_MEM[1]

	c1_t0_t0 = S.Task('c1_t0_t0', length=9, delay_cost=1)
	S += c1_t0_t0 >= 53
	c1_t0_t0 += MM[0]

	c0_t31 = S.Task('c0_t31', length=2, delay_cost=1)
	S += c0_t31 >= 54
	c0_t31 += MAS[0]

	c1_t0_t3_in = S.Task('c1_t0_t3_in', length=1, delay_cost=1)
	S += c1_t0_t3_in >= 54
	c1_t0_t3_in += MAS_in[0]

	c1_t0_t3_mem0 = S.Task('c1_t0_t3_mem0', length=1, delay_cost=1)
	S += c1_t0_t3_mem0 >= 54
	c1_t0_t3_mem0 += MAS_MEM[0]

	c1_t0_t3_mem1 = S.Task('c1_t0_t3_mem1', length=1, delay_cost=1)
	S += c1_t0_t3_mem1 >= 54
	c1_t0_t3_mem1 += MAS_MEM[1]

	c0_t1_t3_in = S.Task('c0_t1_t3_in', length=1, delay_cost=1)
	S += c0_t1_t3_in >= 55
	c0_t1_t3_in += MAS_in[0]

	c0_t1_t3_mem0 = S.Task('c0_t1_t3_mem0', length=1, delay_cost=1)
	S += c0_t1_t3_mem0 >= 55
	c0_t1_t3_mem0 += MAS_MEM[0]

	c0_t1_t3_mem1 = S.Task('c0_t1_t3_mem1', length=1, delay_cost=1)
	S += c0_t1_t3_mem1 >= 55
	c0_t1_t3_mem1 += MAS_MEM[1]

	c1_t0_t3 = S.Task('c1_t0_t3', length=2, delay_cost=1)
	S += c1_t0_t3 >= 55
	c1_t0_t3 += MAS[0]

	c0_t0_t3_in = S.Task('c0_t0_t3_in', length=1, delay_cost=1)
	S += c0_t0_t3_in >= 56
	c0_t0_t3_in += MAS_in[0]

	c0_t0_t3_mem0 = S.Task('c0_t0_t3_mem0', length=1, delay_cost=1)
	S += c0_t0_t3_mem0 >= 56
	c0_t0_t3_mem0 += MAS_MEM[0]

	c0_t0_t3_mem1 = S.Task('c0_t0_t3_mem1', length=1, delay_cost=1)
	S += c0_t0_t3_mem1 >= 56
	c0_t0_t3_mem1 += MAS_MEM[1]

	c0_t1_t3 = S.Task('c0_t1_t3', length=2, delay_cost=1)
	S += c0_t1_t3 >= 56
	c0_t1_t3 += MAS[0]

	c0_t0_t3 = S.Task('c0_t0_t3', length=2, delay_cost=1)
	S += c0_t0_t3 >= 57
	c0_t0_t3 += MAS[0]

	c1_t4_t0_in = S.Task('c1_t4_t0_in', length=1, delay_cost=1)
	S += c1_t4_t0_in >= 57
	c1_t4_t0_in += MM_in[0]

	c1_t4_t0_mem0 = S.Task('c1_t4_t0_mem0', length=1, delay_cost=1)
	S += c1_t4_t0_mem0 >= 57
	c1_t4_t0_mem0 += MAS_MEM[0]

	c1_t4_t0_mem1 = S.Task('c1_t4_t0_mem1', length=1, delay_cost=1)
	S += c1_t4_t0_mem1 >= 57
	c1_t4_t0_mem1 += MAS_MEM[1]

	c0_t1_t1_in = S.Task('c0_t1_t1_in', length=1, delay_cost=1)
	S += c0_t1_t1_in >= 58
	c0_t1_t1_in += MM_in[0]

	c0_t1_t1_mem0 = S.Task('c0_t1_t1_mem0', length=1, delay_cost=1)
	S += c0_t1_t1_mem0 >= 58
	c0_t1_t1_mem0 += MAIN_MEM_r[0]

	c0_t1_t1_mem1 = S.Task('c0_t1_t1_mem1', length=1, delay_cost=1)
	S += c0_t1_t1_mem1 >= 58
	c0_t1_t1_mem1 += MAS_MEM[1]

	c1_t4_t0 = S.Task('c1_t4_t0', length=9, delay_cost=1)
	S += c1_t4_t0 >= 58
	c1_t4_t0 += MM[0]

	c0_t1_t1 = S.Task('c0_t1_t1', length=9, delay_cost=1)
	S += c0_t1_t1 >= 59
	c0_t1_t1 += MM[0]


	# new tasks
	c0_t0_t4 = S.Task('c0_t0_t4', length=9, delay_cost=1)
	c0_t0_t4 += alt(MM)
	c0_t0_t4_in = S.Task('c0_t0_t4_in', length=1, delay_cost=1)
	c0_t0_t4_in += alt(MM_in)
	S += c0_t0_t4_in*MM_in[0]<=c0_t0_t4*MM[0]
	c0_t0_t4_mem0 = S.Task('c0_t0_t4_mem0', length=1, delay_cost=1)
	c0_t0_t4_mem0 += MAS_MEM[0]
	S += 13 < c0_t0_t4_mem0
	S += c0_t0_t4_mem0 <= c0_t0_t4

	c0_t0_t4_mem1 = S.Task('c0_t0_t4_mem1', length=1, delay_cost=1)
	c0_t0_t4_mem1 += MAS_MEM[1]
	S += 58 < c0_t0_t4_mem1
	S += c0_t0_t4_mem1 <= c0_t0_t4

	c0_t00 = S.Task('c0_t00', length=2, delay_cost=1)
	c0_t00 += alt(MAS)
	c0_t00_in = S.Task('c0_t00_in', length=1, delay_cost=1)
	c0_t00_in += alt(MAS_in)
	S += c0_t00_in*MAS_in[0]<=c0_t00*MAS[0]

	c0_t00_mem0 = S.Task('c0_t00_mem0', length=1, delay_cost=1)
	c0_t00_mem0 += MM_MEM[0]
	S += 47 < c0_t00_mem0
	S += c0_t00_mem0 <= c0_t00

	c0_t00_mem1 = S.Task('c0_t00_mem1', length=1, delay_cost=1)
	c0_t00_mem1 += MM_MEM[1]
	S += 50 < c0_t00_mem1
	S += c0_t00_mem1 <= c0_t00

	c0_t0_t5 = S.Task('c0_t0_t5', length=2, delay_cost=1)
	c0_t0_t5 += alt(MAS)
	c0_t0_t5_in = S.Task('c0_t0_t5_in', length=1, delay_cost=1)
	c0_t0_t5_in += alt(MAS_in)
	S += c0_t0_t5_in*MAS_in[0]<=c0_t0_t5*MAS[0]

	c0_t0_t5_mem0 = S.Task('c0_t0_t5_mem0', length=1, delay_cost=1)
	c0_t0_t5_mem0 += MM_MEM[0]
	S += 47 < c0_t0_t5_mem0
	S += c0_t0_t5_mem0 <= c0_t0_t5

	c0_t0_t5_mem1 = S.Task('c0_t0_t5_mem1', length=1, delay_cost=1)
	c0_t0_t5_mem1 += MM_MEM[1]
	S += 50 < c0_t0_t5_mem1
	S += c0_t0_t5_mem1 <= c0_t0_t5

	c0_t1_t4 = S.Task('c0_t1_t4', length=9, delay_cost=1)
	c0_t1_t4 += alt(MM)
	c0_t1_t4_in = S.Task('c0_t1_t4_in', length=1, delay_cost=1)
	c0_t1_t4_in += alt(MM_in)
	S += c0_t1_t4_in*MM_in[0]<=c0_t1_t4*MM[0]
	c0_t1_t4_mem0 = S.Task('c0_t1_t4_mem0', length=1, delay_cost=1)
	c0_t1_t4_mem0 += MAS_MEM[0]
	S += 19 < c0_t1_t4_mem0
	S += c0_t1_t4_mem0 <= c0_t1_t4

	c0_t1_t4_mem1 = S.Task('c0_t1_t4_mem1', length=1, delay_cost=1)
	c0_t1_t4_mem1 += MAS_MEM[1]
	S += 57 < c0_t1_t4_mem1
	S += c0_t1_t4_mem1 <= c0_t1_t4

	c0_t10 = S.Task('c0_t10', length=2, delay_cost=1)
	c0_t10 += alt(MAS)
	c0_t10_in = S.Task('c0_t10_in', length=1, delay_cost=1)
	c0_t10_in += alt(MAS_in)
	S += c0_t10_in*MAS_in[0]<=c0_t10*MAS[0]

	c0_t10_mem0 = S.Task('c0_t10_mem0', length=1, delay_cost=1)
	c0_t10_mem0 += MM_MEM[0]
	S += 67 < c0_t10_mem0
	S += c0_t10_mem0 <= c0_t10

	c0_t10_mem1 = S.Task('c0_t10_mem1', length=1, delay_cost=1)
	c0_t10_mem1 += MM_MEM[1]
	S += 49 < c0_t10_mem1
	S += c0_t10_mem1 <= c0_t10

	c0_t1_t5 = S.Task('c0_t1_t5', length=2, delay_cost=1)
	c0_t1_t5 += alt(MAS)
	c0_t1_t5_in = S.Task('c0_t1_t5_in', length=1, delay_cost=1)
	c0_t1_t5_in += alt(MAS_in)
	S += c0_t1_t5_in*MAS_in[0]<=c0_t1_t5*MAS[0]

	c0_t1_t5_mem0 = S.Task('c0_t1_t5_mem0', length=1, delay_cost=1)
	c0_t1_t5_mem0 += MM_MEM[0]
	S += 49 < c0_t1_t5_mem0
	S += c0_t1_t5_mem0 <= c0_t1_t5

	c0_t1_t5_mem1 = S.Task('c0_t1_t5_mem1', length=1, delay_cost=1)
	c0_t1_t5_mem1 += MM_MEM[1]
	S += 67 < c0_t1_t5_mem1
	S += c0_t1_t5_mem1 <= c0_t1_t5

	c0_t4_t1 = S.Task('c0_t4_t1', length=9, delay_cost=1)
	c0_t4_t1 += alt(MM)
	c0_t4_t1_in = S.Task('c0_t4_t1_in', length=1, delay_cost=1)
	c0_t4_t1_in += alt(MM_in)
	S += c0_t4_t1_in*MM_in[0]<=c0_t4_t1*MM[0]
	c0_t4_t1_mem0 = S.Task('c0_t4_t1_mem0', length=1, delay_cost=1)
	c0_t4_t1_mem0 += MAS_MEM[0]
	S += 9 < c0_t4_t1_mem0
	S += c0_t4_t1_mem0 <= c0_t4_t1

	c0_t4_t1_mem1 = S.Task('c0_t4_t1_mem1', length=1, delay_cost=1)
	c0_t4_t1_mem1 += MAS_MEM[1]
	S += 55 < c0_t4_t1_mem1
	S += c0_t4_t1_mem1 <= c0_t4_t1

	c0_t4_t3 = S.Task('c0_t4_t3', length=2, delay_cost=1)
	c0_t4_t3 += alt(MAS)
	c0_t4_t3_in = S.Task('c0_t4_t3_in', length=1, delay_cost=1)
	c0_t4_t3_in += alt(MAS_in)
	S += c0_t4_t3_in*MAS_in[0]<=c0_t4_t3*MAS[0]

	c0_t4_t3_mem0 = S.Task('c0_t4_t3_mem0', length=1, delay_cost=1)
	c0_t4_t3_mem0 += MAS_MEM[0]
	S += 41 < c0_t4_t3_mem0
	S += c0_t4_t3_mem0 <= c0_t4_t3

	c0_t4_t3_mem1 = S.Task('c0_t4_t3_mem1', length=1, delay_cost=1)
	c0_t4_t3_mem1 += MAS_MEM[1]
	S += 55 < c0_t4_t3_mem1
	S += c0_t4_t3_mem1 <= c0_t4_t3

	c1_t0_t4 = S.Task('c1_t0_t4', length=9, delay_cost=1)
	c1_t0_t4 += alt(MM)
	c1_t0_t4_in = S.Task('c1_t0_t4_in', length=1, delay_cost=1)
	c1_t0_t4_in += alt(MM_in)
	S += c1_t0_t4_in*MM_in[0]<=c1_t0_t4*MM[0]
	c1_t0_t4_mem0 = S.Task('c1_t0_t4_mem0', length=1, delay_cost=1)
	c1_t0_t4_mem0 += MAS_MEM[0]
	S += 16 < c1_t0_t4_mem0
	S += c1_t0_t4_mem0 <= c1_t0_t4

	c1_t0_t4_mem1 = S.Task('c1_t0_t4_mem1', length=1, delay_cost=1)
	c1_t0_t4_mem1 += MAS_MEM[1]
	S += 56 < c1_t0_t4_mem1
	S += c1_t0_t4_mem1 <= c1_t0_t4

	c1_t00 = S.Task('c1_t00', length=2, delay_cost=1)
	c1_t00 += alt(MAS)
	c1_t00_in = S.Task('c1_t00_in', length=1, delay_cost=1)
	c1_t00_in += alt(MAS_in)
	S += c1_t00_in*MAS_in[0]<=c1_t00*MAS[0]

	c1_t00_mem0 = S.Task('c1_t00_mem0', length=1, delay_cost=1)
	c1_t00_mem0 += MM_MEM[0]
	S += 61 < c1_t00_mem0
	S += c1_t00_mem0 <= c1_t00

	c1_t00_mem1 = S.Task('c1_t00_mem1', length=1, delay_cost=1)
	c1_t00_mem1 += MM_MEM[1]
	S += 58 < c1_t00_mem1
	S += c1_t00_mem1 <= c1_t00

	c1_t0_t5 = S.Task('c1_t0_t5', length=2, delay_cost=1)
	c1_t0_t5 += alt(MAS)
	c1_t0_t5_in = S.Task('c1_t0_t5_in', length=1, delay_cost=1)
	c1_t0_t5_in += alt(MAS_in)
	S += c1_t0_t5_in*MAS_in[0]<=c1_t0_t5*MAS[0]

	c1_t0_t5_mem0 = S.Task('c1_t0_t5_mem0', length=1, delay_cost=1)
	c1_t0_t5_mem0 += MM_MEM[0]
	S += 61 < c1_t0_t5_mem0
	S += c1_t0_t5_mem0 <= c1_t0_t5

	c1_t0_t5_mem1 = S.Task('c1_t0_t5_mem1', length=1, delay_cost=1)
	c1_t0_t5_mem1 += MM_MEM[1]
	S += 58 < c1_t0_t5_mem1
	S += c1_t0_t5_mem1 <= c1_t0_t5

	c1_t1_t4 = S.Task('c1_t1_t4', length=9, delay_cost=1)
	c1_t1_t4 += alt(MM)
	c1_t1_t4_in = S.Task('c1_t1_t4_in', length=1, delay_cost=1)
	c1_t1_t4_in += alt(MM_in)
	S += c1_t1_t4_in*MM_in[0]<=c1_t1_t4*MM[0]
	c1_t1_t4_mem0 = S.Task('c1_t1_t4_mem0', length=1, delay_cost=1)
	c1_t1_t4_mem0 += MAS_MEM[0]
	S += 15 < c1_t1_t4_mem0
	S += c1_t1_t4_mem0 <= c1_t1_t4

	c1_t1_t4_mem1 = S.Task('c1_t1_t4_mem1', length=1, delay_cost=1)
	c1_t1_t4_mem1 += MAS_MEM[1]
	S += 37 < c1_t1_t4_mem1
	S += c1_t1_t4_mem1 <= c1_t1_t4

	c1_t10 = S.Task('c1_t10', length=2, delay_cost=1)
	c1_t10 += alt(MAS)
	c1_t10_in = S.Task('c1_t10_in', length=1, delay_cost=1)
	c1_t10_in += alt(MAS_in)
	S += c1_t10_in*MAS_in[0]<=c1_t10*MAS[0]

	c1_t10_mem0 = S.Task('c1_t10_mem0', length=1, delay_cost=1)
	c1_t10_mem0 += MM_MEM[0]
	S += 60 < c1_t10_mem0
	S += c1_t10_mem0 <= c1_t10

	c1_t10_mem1 = S.Task('c1_t10_mem1', length=1, delay_cost=1)
	c1_t10_mem1 += MM_MEM[1]
	S += 39 < c1_t10_mem1
	S += c1_t10_mem1 <= c1_t10

	c1_t1_t5 = S.Task('c1_t1_t5', length=2, delay_cost=1)
	c1_t1_t5 += alt(MAS)
	c1_t1_t5_in = S.Task('c1_t1_t5_in', length=1, delay_cost=1)
	c1_t1_t5_in += alt(MAS_in)
	S += c1_t1_t5_in*MAS_in[0]<=c1_t1_t5*MAS[0]

	c1_t1_t5_mem0 = S.Task('c1_t1_t5_mem0', length=1, delay_cost=1)
	c1_t1_t5_mem0 += MM_MEM[0]
	S += 39 < c1_t1_t5_mem0
	S += c1_t1_t5_mem0 <= c1_t1_t5

	c1_t1_t5_mem1 = S.Task('c1_t1_t5_mem1', length=1, delay_cost=1)
	c1_t1_t5_mem1 += MM_MEM[1]
	S += 60 < c1_t1_t5_mem1
	S += c1_t1_t5_mem1 <= c1_t1_t5

	c1_t4_t1 = S.Task('c1_t4_t1', length=9, delay_cost=1)
	c1_t4_t1 += alt(MM)
	c1_t4_t1_in = S.Task('c1_t4_t1_in', length=1, delay_cost=1)
	c1_t4_t1_in += alt(MM_in)
	S += c1_t4_t1_in*MM_in[0]<=c1_t4_t1*MM[0]
	c1_t4_t1_mem0 = S.Task('c1_t4_t1_mem0', length=1, delay_cost=1)
	c1_t4_t1_mem0 += MAS_MEM[0]
	S += 2 < c1_t4_t1_mem0
	S += c1_t4_t1_mem0 <= c1_t4_t1

	c1_t4_t1_mem1 = S.Task('c1_t4_t1_mem1', length=1, delay_cost=1)
	c1_t4_t1_mem1 += MAS_MEM[1]
	S += 45 < c1_t4_t1_mem1
	S += c1_t4_t1_mem1 <= c1_t4_t1

	c1_t4_t3 = S.Task('c1_t4_t3', length=2, delay_cost=1)
	c1_t4_t3 += alt(MAS)
	c1_t4_t3_in = S.Task('c1_t4_t3_in', length=1, delay_cost=1)
	c1_t4_t3_in += alt(MAS_in)
	S += c1_t4_t3_in*MAS_in[0]<=c1_t4_t3*MAS[0]

	c1_t4_t3_mem0 = S.Task('c1_t4_t3_mem0', length=1, delay_cost=1)
	c1_t4_t3_mem0 += MAS_MEM[0]
	S += 49 < c1_t4_t3_mem0
	S += c1_t4_t3_mem0 <= c1_t4_t3

	c1_t4_t3_mem1 = S.Task('c1_t4_t3_mem1', length=1, delay_cost=1)
	c1_t4_t3_mem1 += MAS_MEM[1]
	S += 45 < c1_t4_t3_mem1
	S += c1_t4_t3_mem1 <= c1_t4_t3

	c2_t0_t4 = S.Task('c2_t0_t4', length=9, delay_cost=1)
	c2_t0_t4 += alt(MM)
	c2_t0_t4_in = S.Task('c2_t0_t4_in', length=1, delay_cost=1)
	c2_t0_t4_in += alt(MM_in)
	S += c2_t0_t4_in*MM_in[0]<=c2_t0_t4*MM[0]
	c2_t0_t4_mem0 = S.Task('c2_t0_t4_mem0', length=1, delay_cost=1)
	c2_t0_t4_mem0 += MAS_MEM[0]
	S += 18 < c2_t0_t4_mem0
	S += c2_t0_t4_mem0 <= c2_t0_t4

	c2_t0_t4_mem1 = S.Task('c2_t0_t4_mem1', length=1, delay_cost=1)
	c2_t0_t4_mem1 += MAS_MEM[1]
	S += 48 < c2_t0_t4_mem1
	S += c2_t0_t4_mem1 <= c2_t0_t4

	c2_t00 = S.Task('c2_t00', length=2, delay_cost=1)
	c2_t00 += alt(MAS)
	c2_t00_in = S.Task('c2_t00_in', length=1, delay_cost=1)
	c2_t00_in += alt(MAS_in)
	S += c2_t00_in*MAS_in[0]<=c2_t00*MAS[0]

	c2_t00_mem0 = S.Task('c2_t00_mem0', length=1, delay_cost=1)
	c2_t00_mem0 += MM_MEM[0]
	S += 42 < c2_t00_mem0
	S += c2_t00_mem0 <= c2_t00

	c2_t00_mem1 = S.Task('c2_t00_mem1', length=1, delay_cost=1)
	c2_t00_mem1 += MM_MEM[1]
	S += 57 < c2_t00_mem1
	S += c2_t00_mem1 <= c2_t00

	c2_t0_t5 = S.Task('c2_t0_t5', length=2, delay_cost=1)
	c2_t0_t5 += alt(MAS)
	c2_t0_t5_in = S.Task('c2_t0_t5_in', length=1, delay_cost=1)
	c2_t0_t5_in += alt(MAS_in)
	S += c2_t0_t5_in*MAS_in[0]<=c2_t0_t5*MAS[0]

	c2_t0_t5_mem0 = S.Task('c2_t0_t5_mem0', length=1, delay_cost=1)
	c2_t0_t5_mem0 += MM_MEM[0]
	S += 42 < c2_t0_t5_mem0
	S += c2_t0_t5_mem0 <= c2_t0_t5

	c2_t0_t5_mem1 = S.Task('c2_t0_t5_mem1', length=1, delay_cost=1)
	c2_t0_t5_mem1 += MM_MEM[1]
	S += 57 < c2_t0_t5_mem1
	S += c2_t0_t5_mem1 <= c2_t0_t5

	c2_t1_t4 = S.Task('c2_t1_t4', length=9, delay_cost=1)
	c2_t1_t4 += alt(MM)
	c2_t1_t4_in = S.Task('c2_t1_t4_in', length=1, delay_cost=1)
	c2_t1_t4_in += alt(MM_in)
	S += c2_t1_t4_in*MM_in[0]<=c2_t1_t4*MM[0]
	c2_t1_t4_mem0 = S.Task('c2_t1_t4_mem0', length=1, delay_cost=1)
	c2_t1_t4_mem0 += MAS_MEM[0]
	S += 12 < c2_t1_t4_mem0
	S += c2_t1_t4_mem0 <= c2_t1_t4

	c2_t1_t4_mem1 = S.Task('c2_t1_t4_mem1', length=1, delay_cost=1)
	c2_t1_t4_mem1 += MAS_MEM[1]
	S += 47 < c2_t1_t4_mem1
	S += c2_t1_t4_mem1 <= c2_t1_t4

	c2_t10 = S.Task('c2_t10', length=2, delay_cost=1)
	c2_t10 += alt(MAS)
	c2_t10_in = S.Task('c2_t10_in', length=1, delay_cost=1)
	c2_t10_in += alt(MAS_in)
	S += c2_t10_in*MAS_in[0]<=c2_t10*MAS[0]

	c2_t10_mem0 = S.Task('c2_t10_mem0', length=1, delay_cost=1)
	c2_t10_mem0 += MM_MEM[0]
	S += 45 < c2_t10_mem0
	S += c2_t10_mem0 <= c2_t10

	c2_t10_mem1 = S.Task('c2_t10_mem1', length=1, delay_cost=1)
	c2_t10_mem1 += MM_MEM[1]
	S += 40 < c2_t10_mem1
	S += c2_t10_mem1 <= c2_t10

	c2_t1_t5 = S.Task('c2_t1_t5', length=2, delay_cost=1)
	c2_t1_t5 += alt(MAS)
	c2_t1_t5_in = S.Task('c2_t1_t5_in', length=1, delay_cost=1)
	c2_t1_t5_in += alt(MAS_in)
	S += c2_t1_t5_in*MAS_in[0]<=c2_t1_t5*MAS[0]

	c2_t1_t5_mem0 = S.Task('c2_t1_t5_mem0', length=1, delay_cost=1)
	c2_t1_t5_mem0 += MM_MEM[0]
	S += 40 < c2_t1_t5_mem0
	S += c2_t1_t5_mem0 <= c2_t1_t5

	c2_t1_t5_mem1 = S.Task('c2_t1_t5_mem1', length=1, delay_cost=1)
	c2_t1_t5_mem1 += MM_MEM[1]
	S += 45 < c2_t1_t5_mem1
	S += c2_t1_t5_mem1 <= c2_t1_t5

	c2_t4_t1 = S.Task('c2_t4_t1', length=9, delay_cost=1)
	c2_t4_t1 += alt(MM)
	c2_t4_t1_in = S.Task('c2_t4_t1_in', length=1, delay_cost=1)
	c2_t4_t1_in += alt(MM_in)
	S += c2_t4_t1_in*MM_in[0]<=c2_t4_t1*MM[0]
	c2_t4_t1_mem0 = S.Task('c2_t4_t1_mem0', length=1, delay_cost=1)
	c2_t4_t1_mem0 += MAS_MEM[0]
	S += 4 < c2_t4_t1_mem0
	S += c2_t4_t1_mem0 <= c2_t4_t1

	c2_t4_t1_mem1 = S.Task('c2_t4_t1_mem1', length=1, delay_cost=1)
	c2_t4_t1_mem1 += MAS_MEM[1]
	S += 44 < c2_t4_t1_mem1
	S += c2_t4_t1_mem1 <= c2_t4_t1

	c2_t4_t3 = S.Task('c2_t4_t3', length=2, delay_cost=1)
	c2_t4_t3 += alt(MAS)
	c2_t4_t3_in = S.Task('c2_t4_t3_in', length=1, delay_cost=1)
	c2_t4_t3_in += alt(MAS_in)
	S += c2_t4_t3_in*MAS_in[0]<=c2_t4_t3*MAS[0]

	c2_t4_t3_mem0 = S.Task('c2_t4_t3_mem0', length=1, delay_cost=1)
	c2_t4_t3_mem0 += MAS_MEM[0]
	S += 36 < c2_t4_t3_mem0
	S += c2_t4_t3_mem0 <= c2_t4_t3

	c2_t4_t3_mem1 = S.Task('c2_t4_t3_mem1', length=1, delay_cost=1)
	c2_t4_t3_mem1 += MAS_MEM[1]
	S += 44 < c2_t4_t3_mem1
	S += c2_t4_t3_mem1 <= c2_t4_t3

	c0_t01 = S.Task('c0_t01', length=2, delay_cost=1)
	c0_t01 += alt(MAS)
	c0_t01_in = S.Task('c0_t01_in', length=1, delay_cost=1)
	c0_t01_in += alt(MAS_in)
	S += c0_t01_in*MAS_in[0]<=c0_t01*MAS[0]

	c0_t01_mem0 = S.Task('c0_t01_mem0', length=1, delay_cost=1)
	c0_t01_mem0 += alt(MM_MEM)
	S += (c0_t0_t4*MM[0])-1 < c0_t01_mem0*MM_MEM[0]
	S += c0_t01_mem0 <= c0_t01

	c0_t01_mem1 = S.Task('c0_t01_mem1', length=1, delay_cost=1)
	c0_t01_mem1 += alt(MAS_MEM)
	S += (c0_t0_t5*MAS[0])-1 < c0_t01_mem1*MAS_MEM[1]
	S += c0_t01_mem1 <= c0_t01

	c0_t11 = S.Task('c0_t11', length=2, delay_cost=1)
	c0_t11 += alt(MAS)
	c0_t11_in = S.Task('c0_t11_in', length=1, delay_cost=1)
	c0_t11_in += alt(MAS_in)
	S += c0_t11_in*MAS_in[0]<=c0_t11*MAS[0]

	c0_t11_mem0 = S.Task('c0_t11_mem0', length=1, delay_cost=1)
	c0_t11_mem0 += alt(MM_MEM)
	S += (c0_t1_t4*MM[0])-1 < c0_t11_mem0*MM_MEM[0]
	S += c0_t11_mem0 <= c0_t11

	c0_t11_mem1 = S.Task('c0_t11_mem1', length=1, delay_cost=1)
	c0_t11_mem1 += alt(MAS_MEM)
	S += (c0_t1_t5*MAS[0])-1 < c0_t11_mem1*MAS_MEM[1]
	S += c0_t11_mem1 <= c0_t11

	c0_t4_t4 = S.Task('c0_t4_t4', length=9, delay_cost=1)
	c0_t4_t4 += alt(MM)
	c0_t4_t4_in = S.Task('c0_t4_t4_in', length=1, delay_cost=1)
	c0_t4_t4_in += alt(MM_in)
	S += c0_t4_t4_in*MM_in[0]<=c0_t4_t4*MM[0]
	c0_t4_t4_mem0 = S.Task('c0_t4_t4_mem0', length=1, delay_cost=1)
	c0_t4_t4_mem0 += MAS_MEM[0]
	S += 14 < c0_t4_t4_mem0
	S += c0_t4_t4_mem0 <= c0_t4_t4

	c0_t4_t4_mem1 = S.Task('c0_t4_t4_mem1', length=1, delay_cost=1)
	c0_t4_t4_mem1 += alt(MAS_MEM)
	S += (c0_t4_t3*MAS[0])-1 < c0_t4_t4_mem1*MAS_MEM[1]
	S += c0_t4_t4_mem1 <= c0_t4_t4

	c0_t40 = S.Task('c0_t40', length=2, delay_cost=1)
	c0_t40 += alt(MAS)
	c0_t40_in = S.Task('c0_t40_in', length=1, delay_cost=1)
	c0_t40_in += alt(MAS_in)
	S += c0_t40_in*MAS_in[0]<=c0_t40*MAS[0]

	c0_t40_mem0 = S.Task('c0_t40_mem0', length=1, delay_cost=1)
	c0_t40_mem0 += MM_MEM[0]
	S += 59 < c0_t40_mem0
	S += c0_t40_mem0 <= c0_t40

	c0_t40_mem1 = S.Task('c0_t40_mem1', length=1, delay_cost=1)
	c0_t40_mem1 += alt(MM_MEM)
	S += (c0_t4_t1*MM[0])-1 < c0_t40_mem1*MM_MEM[1]
	S += c0_t40_mem1 <= c0_t40

	c0_t4_t5 = S.Task('c0_t4_t5', length=2, delay_cost=1)
	c0_t4_t5 += alt(MAS)
	c0_t4_t5_in = S.Task('c0_t4_t5_in', length=1, delay_cost=1)
	c0_t4_t5_in += alt(MAS_in)
	S += c0_t4_t5_in*MAS_in[0]<=c0_t4_t5*MAS[0]

	c0_t4_t5_mem0 = S.Task('c0_t4_t5_mem0', length=1, delay_cost=1)
	c0_t4_t5_mem0 += MM_MEM[0]
	S += 59 < c0_t4_t5_mem0
	S += c0_t4_t5_mem0 <= c0_t4_t5

	c0_t4_t5_mem1 = S.Task('c0_t4_t5_mem1', length=1, delay_cost=1)
	c0_t4_t5_mem1 += alt(MM_MEM)
	S += (c0_t4_t1*MM[0])-1 < c0_t4_t5_mem1*MM_MEM[1]
	S += c0_t4_t5_mem1 <= c0_t4_t5

	c0_t50 = S.Task('c0_t50', length=2, delay_cost=1)
	c0_t50 += alt(MAS)
	c0_t50_in = S.Task('c0_t50_in', length=1, delay_cost=1)
	c0_t50_in += alt(MAS_in)
	S += c0_t50_in*MAS_in[0]<=c0_t50*MAS[0]

	c0_t50_mem0 = S.Task('c0_t50_mem0', length=1, delay_cost=1)
	c0_t50_mem0 += alt(MAS_MEM)
	S += (c0_t00*MAS[0])-1 < c0_t50_mem0*MAS_MEM[0]
	S += c0_t50_mem0 <= c0_t50

	c0_t50_mem1 = S.Task('c0_t50_mem1', length=1, delay_cost=1)
	c0_t50_mem1 += alt(MAS_MEM)
	S += (c0_t10*MAS[0])-1 < c0_t50_mem1*MAS_MEM[1]
	S += c0_t50_mem1 <= c0_t50

	c1_t01 = S.Task('c1_t01', length=2, delay_cost=1)
	c1_t01 += alt(MAS)
	c1_t01_in = S.Task('c1_t01_in', length=1, delay_cost=1)
	c1_t01_in += alt(MAS_in)
	S += c1_t01_in*MAS_in[0]<=c1_t01*MAS[0]

	c1_t01_mem0 = S.Task('c1_t01_mem0', length=1, delay_cost=1)
	c1_t01_mem0 += alt(MM_MEM)
	S += (c1_t0_t4*MM[0])-1 < c1_t01_mem0*MM_MEM[0]
	S += c1_t01_mem0 <= c1_t01

	c1_t01_mem1 = S.Task('c1_t01_mem1', length=1, delay_cost=1)
	c1_t01_mem1 += alt(MAS_MEM)
	S += (c1_t0_t5*MAS[0])-1 < c1_t01_mem1*MAS_MEM[1]
	S += c1_t01_mem1 <= c1_t01

	c1_t11 = S.Task('c1_t11', length=2, delay_cost=1)
	c1_t11 += alt(MAS)
	c1_t11_in = S.Task('c1_t11_in', length=1, delay_cost=1)
	c1_t11_in += alt(MAS_in)
	S += c1_t11_in*MAS_in[0]<=c1_t11*MAS[0]

	c1_t11_mem0 = S.Task('c1_t11_mem0', length=1, delay_cost=1)
	c1_t11_mem0 += alt(MM_MEM)
	S += (c1_t1_t4*MM[0])-1 < c1_t11_mem0*MM_MEM[0]
	S += c1_t11_mem0 <= c1_t11

	c1_t11_mem1 = S.Task('c1_t11_mem1', length=1, delay_cost=1)
	c1_t11_mem1 += alt(MAS_MEM)
	S += (c1_t1_t5*MAS[0])-1 < c1_t11_mem1*MAS_MEM[1]
	S += c1_t11_mem1 <= c1_t11

	c1_t4_t4 = S.Task('c1_t4_t4', length=9, delay_cost=1)
	c1_t4_t4 += alt(MM)
	c1_t4_t4_in = S.Task('c1_t4_t4_in', length=1, delay_cost=1)
	c1_t4_t4_in += alt(MM_in)
	S += c1_t4_t4_in*MM_in[0]<=c1_t4_t4*MM[0]
	c1_t4_t4_mem0 = S.Task('c1_t4_t4_mem0', length=1, delay_cost=1)
	c1_t4_t4_mem0 += MAS_MEM[0]
	S += 5 < c1_t4_t4_mem0
	S += c1_t4_t4_mem0 <= c1_t4_t4

	c1_t4_t4_mem1 = S.Task('c1_t4_t4_mem1', length=1, delay_cost=1)
	c1_t4_t4_mem1 += alt(MAS_MEM)
	S += (c1_t4_t3*MAS[0])-1 < c1_t4_t4_mem1*MAS_MEM[1]
	S += c1_t4_t4_mem1 <= c1_t4_t4

	c1_t40 = S.Task('c1_t40', length=2, delay_cost=1)
	c1_t40 += alt(MAS)
	c1_t40_in = S.Task('c1_t40_in', length=1, delay_cost=1)
	c1_t40_in += alt(MAS_in)
	S += c1_t40_in*MAS_in[0]<=c1_t40*MAS[0]

	c1_t40_mem0 = S.Task('c1_t40_mem0', length=1, delay_cost=1)
	c1_t40_mem0 += MM_MEM[0]
	S += 66 < c1_t40_mem0
	S += c1_t40_mem0 <= c1_t40

	c1_t40_mem1 = S.Task('c1_t40_mem1', length=1, delay_cost=1)
	c1_t40_mem1 += alt(MM_MEM)
	S += (c1_t4_t1*MM[0])-1 < c1_t40_mem1*MM_MEM[1]
	S += c1_t40_mem1 <= c1_t40

	c1_t4_t5 = S.Task('c1_t4_t5', length=2, delay_cost=1)
	c1_t4_t5 += alt(MAS)
	c1_t4_t5_in = S.Task('c1_t4_t5_in', length=1, delay_cost=1)
	c1_t4_t5_in += alt(MAS_in)
	S += c1_t4_t5_in*MAS_in[0]<=c1_t4_t5*MAS[0]

	c1_t4_t5_mem0 = S.Task('c1_t4_t5_mem0', length=1, delay_cost=1)
	c1_t4_t5_mem0 += MM_MEM[0]
	S += 66 < c1_t4_t5_mem0
	S += c1_t4_t5_mem0 <= c1_t4_t5

	c1_t4_t5_mem1 = S.Task('c1_t4_t5_mem1', length=1, delay_cost=1)
	c1_t4_t5_mem1 += alt(MM_MEM)
	S += (c1_t4_t1*MM[0])-1 < c1_t4_t5_mem1*MM_MEM[1]
	S += c1_t4_t5_mem1 <= c1_t4_t5

	c1_t50 = S.Task('c1_t50', length=2, delay_cost=1)
	c1_t50 += alt(MAS)
	c1_t50_in = S.Task('c1_t50_in', length=1, delay_cost=1)
	c1_t50_in += alt(MAS_in)
	S += c1_t50_in*MAS_in[0]<=c1_t50*MAS[0]

	c1_t50_mem0 = S.Task('c1_t50_mem0', length=1, delay_cost=1)
	c1_t50_mem0 += alt(MAS_MEM)
	S += (c1_t00*MAS[0])-1 < c1_t50_mem0*MAS_MEM[0]
	S += c1_t50_mem0 <= c1_t50

	c1_t50_mem1 = S.Task('c1_t50_mem1', length=1, delay_cost=1)
	c1_t50_mem1 += alt(MAS_MEM)
	S += (c1_t10*MAS[0])-1 < c1_t50_mem1*MAS_MEM[1]
	S += c1_t50_mem1 <= c1_t50

	c2_t01 = S.Task('c2_t01', length=2, delay_cost=1)
	c2_t01 += alt(MAS)
	c2_t01_in = S.Task('c2_t01_in', length=1, delay_cost=1)
	c2_t01_in += alt(MAS_in)
	S += c2_t01_in*MAS_in[0]<=c2_t01*MAS[0]

	c2_t01_mem0 = S.Task('c2_t01_mem0', length=1, delay_cost=1)
	c2_t01_mem0 += alt(MM_MEM)
	S += (c2_t0_t4*MM[0])-1 < c2_t01_mem0*MM_MEM[0]
	S += c2_t01_mem0 <= c2_t01

	c2_t01_mem1 = S.Task('c2_t01_mem1', length=1, delay_cost=1)
	c2_t01_mem1 += alt(MAS_MEM)
	S += (c2_t0_t5*MAS[0])-1 < c2_t01_mem1*MAS_MEM[1]
	S += c2_t01_mem1 <= c2_t01

	c2_t11 = S.Task('c2_t11', length=2, delay_cost=1)
	c2_t11 += alt(MAS)
	c2_t11_in = S.Task('c2_t11_in', length=1, delay_cost=1)
	c2_t11_in += alt(MAS_in)
	S += c2_t11_in*MAS_in[0]<=c2_t11*MAS[0]

	c2_t11_mem0 = S.Task('c2_t11_mem0', length=1, delay_cost=1)
	c2_t11_mem0 += alt(MM_MEM)
	S += (c2_t1_t4*MM[0])-1 < c2_t11_mem0*MM_MEM[0]
	S += c2_t11_mem0 <= c2_t11

	c2_t11_mem1 = S.Task('c2_t11_mem1', length=1, delay_cost=1)
	c2_t11_mem1 += alt(MAS_MEM)
	S += (c2_t1_t5*MAS[0])-1 < c2_t11_mem1*MAS_MEM[1]
	S += c2_t11_mem1 <= c2_t11

	c2_t4_t4 = S.Task('c2_t4_t4', length=9, delay_cost=1)
	c2_t4_t4 += alt(MM)
	c2_t4_t4_in = S.Task('c2_t4_t4_in', length=1, delay_cost=1)
	c2_t4_t4_in += alt(MM_in)
	S += c2_t4_t4_in*MM_in[0]<=c2_t4_t4*MM[0]
	c2_t4_t4_mem0 = S.Task('c2_t4_t4_mem0', length=1, delay_cost=1)
	c2_t4_t4_mem0 += MAS_MEM[0]
	S += 8 < c2_t4_t4_mem0
	S += c2_t4_t4_mem0 <= c2_t4_t4

	c2_t4_t4_mem1 = S.Task('c2_t4_t4_mem1', length=1, delay_cost=1)
	c2_t4_t4_mem1 += alt(MAS_MEM)
	S += (c2_t4_t3*MAS[0])-1 < c2_t4_t4_mem1*MAS_MEM[1]
	S += c2_t4_t4_mem1 <= c2_t4_t4

	c2_t40 = S.Task('c2_t40', length=2, delay_cost=1)
	c2_t40 += alt(MAS)
	c2_t40_in = S.Task('c2_t40_in', length=1, delay_cost=1)
	c2_t40_in += alt(MAS_in)
	S += c2_t40_in*MAS_in[0]<=c2_t40*MAS[0]

	c2_t40_mem0 = S.Task('c2_t40_mem0', length=1, delay_cost=1)
	c2_t40_mem0 += MM_MEM[0]
	S += 53 < c2_t40_mem0
	S += c2_t40_mem0 <= c2_t40

	c2_t40_mem1 = S.Task('c2_t40_mem1', length=1, delay_cost=1)
	c2_t40_mem1 += alt(MM_MEM)
	S += (c2_t4_t1*MM[0])-1 < c2_t40_mem1*MM_MEM[1]
	S += c2_t40_mem1 <= c2_t40

	c2_t4_t5 = S.Task('c2_t4_t5', length=2, delay_cost=1)
	c2_t4_t5 += alt(MAS)
	c2_t4_t5_in = S.Task('c2_t4_t5_in', length=1, delay_cost=1)
	c2_t4_t5_in += alt(MAS_in)
	S += c2_t4_t5_in*MAS_in[0]<=c2_t4_t5*MAS[0]

	c2_t4_t5_mem0 = S.Task('c2_t4_t5_mem0', length=1, delay_cost=1)
	c2_t4_t5_mem0 += MM_MEM[0]
	S += 53 < c2_t4_t5_mem0
	S += c2_t4_t5_mem0 <= c2_t4_t5

	c2_t4_t5_mem1 = S.Task('c2_t4_t5_mem1', length=1, delay_cost=1)
	c2_t4_t5_mem1 += alt(MM_MEM)
	S += (c2_t4_t1*MM[0])-1 < c2_t4_t5_mem1*MM_MEM[1]
	S += c2_t4_t5_mem1 <= c2_t4_t5

	c2_t50 = S.Task('c2_t50', length=2, delay_cost=1)
	c2_t50 += alt(MAS)
	c2_t50_in = S.Task('c2_t50_in', length=1, delay_cost=1)
	c2_t50_in += alt(MAS_in)
	S += c2_t50_in*MAS_in[0]<=c2_t50*MAS[0]

	c2_t50_mem0 = S.Task('c2_t50_mem0', length=1, delay_cost=1)
	c2_t50_mem0 += alt(MAS_MEM)
	S += (c2_t00*MAS[0])-1 < c2_t50_mem0*MAS_MEM[0]
	S += c2_t50_mem0 <= c2_t50

	c2_t50_mem1 = S.Task('c2_t50_mem1', length=1, delay_cost=1)
	c2_t50_mem1 += alt(MAS_MEM)
	S += (c2_t10*MAS[0])-1 < c2_t50_mem1*MAS_MEM[1]
	S += c2_t50_mem1 <= c2_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage9MM1_stage2MAS1/FP12_INV_AFTER_FPINV/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 2))

	return solution

