from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 184
	S = Scenario("schedule2", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=14)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=4)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=4, size=3, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=8)
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
	c_qinv_denom_inv0_in += MM_in[0]

	c_qinv_denom_inv0_mem0 = S.Task('c_qinv_denom_inv0_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem0 >= 1
	c_qinv_denom_inv0_mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv0_mem1 = S.Task('c_qinv_denom_inv0_mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem1 >= 1
	c_qinv_denom_inv0_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv1_ = S.Task('c_qinv_denom_inv1_', length=14, delay_cost=1)
	S += c_qinv_denom_inv1_ >= 1
	c_qinv_denom_inv1_ += MM[0]

	c1_t20_in = S.Task('c1_t20_in', length=1, delay_cost=1)
	S += c1_t20_in >= 2
	c1_t20_in += MAS_in[2]

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	S += c1_t20_mem0 >= 2
	c1_t20_mem0 += MAIN_MEM_r[0]

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	S += c1_t20_mem1 >= 2
	c1_t20_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv0 = S.Task('c_qinv_denom_inv0', length=14, delay_cost=1)
	S += c_qinv_denom_inv0 >= 2
	c_qinv_denom_inv0 += MM[0]

	c1_t20 = S.Task('c1_t20', length=3, delay_cost=1)
	S += c1_t20 >= 3
	c1_t20 += MAS[2]

	c1_t21_in = S.Task('c1_t21_in', length=1, delay_cost=1)
	S += c1_t21_in >= 3
	c1_t21_in += MAS_in[3]

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	S += c1_t21_mem0 >= 3
	c1_t21_mem0 += MAIN_MEM_r[0]

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	S += c1_t21_mem1 >= 3
	c1_t21_mem1 += MAIN_MEM_r[1]

	c1_t21 = S.Task('c1_t21', length=3, delay_cost=1)
	S += c1_t21 >= 4
	c1_t21 += MAS[3]

	c2_t21_in = S.Task('c2_t21_in', length=1, delay_cost=1)
	S += c2_t21_in >= 4
	c2_t21_in += MAS_in[1]

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	S += c2_t21_mem0 >= 4
	c2_t21_mem0 += MAIN_MEM_r[0]

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	S += c2_t21_mem1 >= 4
	c2_t21_mem1 += MAIN_MEM_r[1]

	c2_t20_in = S.Task('c2_t20_in', length=1, delay_cost=1)
	S += c2_t20_in >= 5
	c2_t20_in += MAS_in[2]

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	S += c2_t20_mem0 >= 5
	c2_t20_mem0 += MAIN_MEM_r[0]

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	S += c2_t20_mem1 >= 5
	c2_t20_mem1 += MAIN_MEM_r[1]

	c2_t21 = S.Task('c2_t21', length=3, delay_cost=1)
	S += c2_t21 >= 5
	c2_t21 += MAS[1]

	c0_t21_in = S.Task('c0_t21_in', length=1, delay_cost=1)
	S += c0_t21_in >= 6
	c0_t21_in += MAS_in[2]

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	S += c0_t21_mem0 >= 6
	c0_t21_mem0 += MAIN_MEM_r[0]

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	S += c0_t21_mem1 >= 6
	c0_t21_mem1 += MAIN_MEM_r[1]

	c1_t4_t2_in = S.Task('c1_t4_t2_in', length=1, delay_cost=1)
	S += c1_t4_t2_in >= 6
	c1_t4_t2_in += MAS_in[0]

	c1_t4_t2_mem0 = S.Task('c1_t4_t2_mem0', length=1, delay_cost=1)
	S += c1_t4_t2_mem0 >= 6
	c1_t4_t2_mem0 += MAS_MEM[4]

	c1_t4_t2_mem1 = S.Task('c1_t4_t2_mem1', length=1, delay_cost=1)
	S += c1_t4_t2_mem1 >= 6
	c1_t4_t2_mem1 += MAS_MEM[7]

	c2_t20 = S.Task('c2_t20', length=3, delay_cost=1)
	S += c2_t20 >= 6
	c2_t20 += MAS[2]

	c0_t20_in = S.Task('c0_t20_in', length=1, delay_cost=1)
	S += c0_t20_in >= 7
	c0_t20_in += MAS_in[1]

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	S += c0_t20_mem0 >= 7
	c0_t20_mem0 += MAIN_MEM_r[0]

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	S += c0_t20_mem1 >= 7
	c0_t20_mem1 += MAIN_MEM_r[1]

	c0_t21 = S.Task('c0_t21', length=3, delay_cost=1)
	S += c0_t21 >= 7
	c0_t21 += MAS[2]

	c1_t4_t2 = S.Task('c1_t4_t2', length=3, delay_cost=1)
	S += c1_t4_t2 >= 7
	c1_t4_t2 += MAS[0]

	c0_t20 = S.Task('c0_t20', length=3, delay_cost=1)
	S += c0_t20 >= 8
	c0_t20 += MAS[1]

	c2_t4_t2_in = S.Task('c2_t4_t2_in', length=1, delay_cost=1)
	S += c2_t4_t2_in >= 8
	c2_t4_t2_in += MAS_in[3]

	c2_t4_t2_mem0 = S.Task('c2_t4_t2_mem0', length=1, delay_cost=1)
	S += c2_t4_t2_mem0 >= 8
	c2_t4_t2_mem0 += MAS_MEM[4]

	c2_t4_t2_mem1 = S.Task('c2_t4_t2_mem1', length=1, delay_cost=1)
	S += c2_t4_t2_mem1 >= 8
	c2_t4_t2_mem1 += MAS_MEM[3]

	c_qinv1__t2_in = S.Task('c_qinv1__t2_in', length=1, delay_cost=1)
	S += c_qinv1__t2_in >= 8
	c_qinv1__t2_in += MAS_in[1]

	c_qinv1__t2_mem0 = S.Task('c_qinv1__t2_mem0', length=1, delay_cost=1)
	S += c_qinv1__t2_mem0 >= 8
	c_qinv1__t2_mem0 += MAIN_MEM_r[0]

	c_qinv1__t2_mem1 = S.Task('c_qinv1__t2_mem1', length=1, delay_cost=1)
	S += c_qinv1__t2_mem1 >= 8
	c_qinv1__t2_mem1 += MAIN_MEM_r[1]

	c0_t1_t2_in = S.Task('c0_t1_t2_in', length=1, delay_cost=1)
	S += c0_t1_t2_in >= 9
	c0_t1_t2_in += MAS_in[1]

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	S += c0_t1_t2_mem0 >= 9
	c0_t1_t2_mem0 += MAIN_MEM_r[0]

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	S += c0_t1_t2_mem1 >= 9
	c0_t1_t2_mem1 += MAIN_MEM_r[1]

	c2_t4_t2 = S.Task('c2_t4_t2', length=3, delay_cost=1)
	S += c2_t4_t2 >= 9
	c2_t4_t2 += MAS[3]

	c_qinv1__t2 = S.Task('c_qinv1__t2', length=3, delay_cost=1)
	S += c_qinv1__t2 >= 9
	c_qinv1__t2 += MAS[1]

	c0_t1_t2 = S.Task('c0_t1_t2', length=3, delay_cost=1)
	S += c0_t1_t2 >= 10
	c0_t1_t2 += MAS[1]

	c0_t4_t2_in = S.Task('c0_t4_t2_in', length=1, delay_cost=1)
	S += c0_t4_t2_in >= 10
	c0_t4_t2_in += MAS_in[1]

	c0_t4_t2_mem0 = S.Task('c0_t4_t2_mem0', length=1, delay_cost=1)
	S += c0_t4_t2_mem0 >= 10
	c0_t4_t2_mem0 += MAS_MEM[2]

	c0_t4_t2_mem1 = S.Task('c0_t4_t2_mem1', length=1, delay_cost=1)
	S += c0_t4_t2_mem1 >= 10
	c0_t4_t2_mem1 += MAS_MEM[5]

	c_qinv0_t2_in = S.Task('c_qinv0_t2_in', length=1, delay_cost=1)
	S += c_qinv0_t2_in >= 10
	c_qinv0_t2_in += MAS_in[3]

	c_qinv0_t2_mem0 = S.Task('c_qinv0_t2_mem0', length=1, delay_cost=1)
	S += c_qinv0_t2_mem0 >= 10
	c_qinv0_t2_mem0 += MAIN_MEM_r[0]

	c_qinv0_t2_mem1 = S.Task('c_qinv0_t2_mem1', length=1, delay_cost=1)
	S += c_qinv0_t2_mem1 >= 10
	c_qinv0_t2_mem1 += MAIN_MEM_r[1]

	c0_t4_t2 = S.Task('c0_t4_t2', length=3, delay_cost=1)
	S += c0_t4_t2 >= 11
	c0_t4_t2 += MAS[1]

	c2_t1_t2_in = S.Task('c2_t1_t2_in', length=1, delay_cost=1)
	S += c2_t1_t2_in >= 11
	c2_t1_t2_in += MAS_in[2]

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	S += c2_t1_t2_mem0 >= 11
	c2_t1_t2_mem0 += MAIN_MEM_r[0]

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	S += c2_t1_t2_mem1 >= 11
	c2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t2 = S.Task('c_qinv0_t2', length=3, delay_cost=1)
	S += c_qinv0_t2 >= 11
	c_qinv0_t2 += MAS[3]

	c2_t0_t2_in = S.Task('c2_t0_t2_in', length=1, delay_cost=1)
	S += c2_t0_t2_in >= 12
	c2_t0_t2_in += MAS_in[0]

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	S += c2_t0_t2_mem0 >= 12
	c2_t0_t2_mem0 += MAIN_MEM_r[0]

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	S += c2_t0_t2_mem1 >= 12
	c2_t0_t2_mem1 += MAIN_MEM_r[1]

	c2_t1_t2 = S.Task('c2_t1_t2', length=3, delay_cost=1)
	S += c2_t1_t2 >= 12
	c2_t1_t2 += MAS[2]

	c1_t1_t2_in = S.Task('c1_t1_t2_in', length=1, delay_cost=1)
	S += c1_t1_t2_in >= 13
	c1_t1_t2_in += MAS_in[1]

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	S += c1_t1_t2_mem0 >= 13
	c1_t1_t2_mem0 += MAIN_MEM_r[0]

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	S += c1_t1_t2_mem1 >= 13
	c1_t1_t2_mem1 += MAIN_MEM_r[1]

	c2_t0_t2 = S.Task('c2_t0_t2', length=3, delay_cost=1)
	S += c2_t0_t2 >= 13
	c2_t0_t2 += MAS[0]

	c1_t1_t2 = S.Task('c1_t1_t2', length=3, delay_cost=1)
	S += c1_t1_t2 >= 14
	c1_t1_t2 += MAS[1]

	c_qinv0_t1_in = S.Task('c_qinv0_t1_in', length=1, delay_cost=1)
	S += c_qinv0_t1_in >= 14
	c_qinv0_t1_in += MM_in[0]

	c_qinv0_t1_mem0 = S.Task('c_qinv0_t1_mem0', length=1, delay_cost=1)
	S += c_qinv0_t1_mem0 >= 14
	c_qinv0_t1_mem0 += MAIN_MEM_r[0]

	c_qinv0_t1_mem1 = S.Task('c_qinv0_t1_mem1', length=1, delay_cost=1)
	S += c_qinv0_t1_mem1 >= 14
	c_qinv0_t1_mem1 += MM_MEM[1]

	c1_t0_t2_in = S.Task('c1_t0_t2_in', length=1, delay_cost=1)
	S += c1_t0_t2_in >= 15
	c1_t0_t2_in += MAS_in[3]

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	S += c1_t0_t2_mem0 >= 15
	c1_t0_t2_mem0 += MAIN_MEM_r[0]

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	S += c1_t0_t2_mem1 >= 15
	c1_t0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t1 = S.Task('c_qinv0_t1', length=14, delay_cost=1)
	S += c_qinv0_t1 >= 15
	c_qinv0_t1 += MM[0]

	c_qinv0_t3_in = S.Task('c_qinv0_t3_in', length=1, delay_cost=1)
	S += c_qinv0_t3_in >= 15
	c_qinv0_t3_in += MAS_in[1]

	c_qinv0_t3_mem0 = S.Task('c_qinv0_t3_mem0', length=1, delay_cost=1)
	S += c_qinv0_t3_mem0 >= 15
	c_qinv0_t3_mem0 += MM_MEM[0]

	c_qinv0_t3_mem1 = S.Task('c_qinv0_t3_mem1', length=1, delay_cost=1)
	S += c_qinv0_t3_mem1 >= 15
	c_qinv0_t3_mem1 += MM_MEM[1]

	c0_t0_t2_in = S.Task('c0_t0_t2_in', length=1, delay_cost=1)
	S += c0_t0_t2_in >= 16
	c0_t0_t2_in += MAS_in[0]

	c0_t0_t2_mem0 = S.Task('c0_t0_t2_mem0', length=1, delay_cost=1)
	S += c0_t0_t2_mem0 >= 16
	c0_t0_t2_mem0 += MAIN_MEM_r[0]

	c0_t0_t2_mem1 = S.Task('c0_t0_t2_mem1', length=1, delay_cost=1)
	S += c0_t0_t2_mem1 >= 16
	c0_t0_t2_mem1 += MAIN_MEM_r[1]

	c1_t0_t2 = S.Task('c1_t0_t2', length=3, delay_cost=1)
	S += c1_t0_t2 >= 16
	c1_t0_t2 += MAS[3]

	c_qinv0_t3 = S.Task('c_qinv0_t3', length=3, delay_cost=1)
	S += c_qinv0_t3 >= 16
	c_qinv0_t3 += MAS[1]

	c_qinv1__t3_in = S.Task('c_qinv1__t3_in', length=1, delay_cost=1)
	S += c_qinv1__t3_in >= 16
	c_qinv1__t3_in += MAS_in[2]

	c_qinv1__t3_mem0 = S.Task('c_qinv1__t3_mem0', length=1, delay_cost=1)
	S += c_qinv1__t3_mem0 >= 16
	c_qinv1__t3_mem0 += MM_MEM[0]

	c_qinv1__t3_mem1 = S.Task('c_qinv1__t3_mem1', length=1, delay_cost=1)
	S += c_qinv1__t3_mem1 >= 16
	c_qinv1__t3_mem1 += MM_MEM[1]

	c0_t0_t2 = S.Task('c0_t0_t2', length=3, delay_cost=1)
	S += c0_t0_t2 >= 17
	c0_t0_t2 += MAS[0]

	c_qinv1__t1_in = S.Task('c_qinv1__t1_in', length=1, delay_cost=1)
	S += c_qinv1__t1_in >= 17
	c_qinv1__t1_in += MM_in[0]

	c_qinv1__t1_mem0 = S.Task('c_qinv1__t1_mem0', length=1, delay_cost=1)
	S += c_qinv1__t1_mem0 >= 17
	c_qinv1__t1_mem0 += MAIN_MEM_r[0]

	c_qinv1__t1_mem1 = S.Task('c_qinv1__t1_mem1', length=1, delay_cost=1)
	S += c_qinv1__t1_mem1 >= 17
	c_qinv1__t1_mem1 += MM_MEM[1]

	c_qinv1__t3 = S.Task('c_qinv1__t3', length=3, delay_cost=1)
	S += c_qinv1__t3 >= 17
	c_qinv1__t3 += MAS[2]

	c_qinv1__t0_in = S.Task('c_qinv1__t0_in', length=1, delay_cost=1)
	S += c_qinv1__t0_in >= 18
	c_qinv1__t0_in += MM_in[0]

	c_qinv1__t0_mem0 = S.Task('c_qinv1__t0_mem0', length=1, delay_cost=1)
	S += c_qinv1__t0_mem0 >= 18
	c_qinv1__t0_mem0 += MAIN_MEM_r[0]

	c_qinv1__t0_mem1 = S.Task('c_qinv1__t0_mem1', length=1, delay_cost=1)
	S += c_qinv1__t0_mem1 >= 18
	c_qinv1__t0_mem1 += MM_MEM[1]

	c_qinv1__t1 = S.Task('c_qinv1__t1', length=14, delay_cost=1)
	S += c_qinv1__t1 >= 18
	c_qinv1__t1 += MM[0]

	c_qinv0_t0_in = S.Task('c_qinv0_t0_in', length=1, delay_cost=1)
	S += c_qinv0_t0_in >= 19
	c_qinv0_t0_in += MM_in[0]

	c_qinv0_t0_mem0 = S.Task('c_qinv0_t0_mem0', length=1, delay_cost=1)
	S += c_qinv0_t0_mem0 >= 19
	c_qinv0_t0_mem0 += MAIN_MEM_r[0]

	c_qinv0_t0_mem1 = S.Task('c_qinv0_t0_mem1', length=1, delay_cost=1)
	S += c_qinv0_t0_mem1 >= 19
	c_qinv0_t0_mem1 += MM_MEM[1]

	c_qinv1__t0 = S.Task('c_qinv1__t0', length=14, delay_cost=1)
	S += c_qinv1__t0 >= 19
	c_qinv1__t0 += MM[0]

	c_qinv0_t0 = S.Task('c_qinv0_t0', length=14, delay_cost=1)
	S += c_qinv0_t0 >= 20
	c_qinv0_t0 += MM[0]

	c_qinv1__t4_in = S.Task('c_qinv1__t4_in', length=1, delay_cost=1)
	S += c_qinv1__t4_in >= 20
	c_qinv1__t4_in += MM_in[0]

	c_qinv1__t4_mem0 = S.Task('c_qinv1__t4_mem0', length=1, delay_cost=1)
	S += c_qinv1__t4_mem0 >= 20
	c_qinv1__t4_mem0 += MAS_MEM[2]

	c_qinv1__t4_mem1 = S.Task('c_qinv1__t4_mem1', length=1, delay_cost=1)
	S += c_qinv1__t4_mem1 >= 20
	c_qinv1__t4_mem1 += MAS_MEM[5]

	c_qinv0_t4_in = S.Task('c_qinv0_t4_in', length=1, delay_cost=1)
	S += c_qinv0_t4_in >= 21
	c_qinv0_t4_in += MM_in[0]

	c_qinv0_t4_mem0 = S.Task('c_qinv0_t4_mem0', length=1, delay_cost=1)
	S += c_qinv0_t4_mem0 >= 21
	c_qinv0_t4_mem0 += MAS_MEM[6]

	c_qinv0_t4_mem1 = S.Task('c_qinv0_t4_mem1', length=1, delay_cost=1)
	S += c_qinv0_t4_mem1 >= 21
	c_qinv0_t4_mem1 += MAS_MEM[3]

	c_qinv1__t4 = S.Task('c_qinv1__t4', length=14, delay_cost=1)
	S += c_qinv1__t4 >= 21
	c_qinv1__t4 += MM[0]

	c_qinv0_t4 = S.Task('c_qinv0_t4', length=14, delay_cost=1)
	S += c_qinv0_t4 >= 22
	c_qinv0_t4 += MM[0]

	c_qinv1_0_in = S.Task('c_qinv1_0_in', length=1, delay_cost=1)
	S += c_qinv1_0_in >= 32
	c_qinv1_0_in += MAS_in[2]

	c_qinv1_0_mem0 = S.Task('c_qinv1_0_mem0', length=1, delay_cost=1)
	S += c_qinv1_0_mem0 >= 32
	c_qinv1_0_mem0 += MM_MEM[0]

	c_qinv1_0_mem1 = S.Task('c_qinv1_0_mem1', length=1, delay_cost=1)
	S += c_qinv1_0_mem1 >= 32
	c_qinv1_0_mem1 += MM_MEM[1]

	c_qinv1_0 = S.Task('c_qinv1_0', length=3, delay_cost=1)
	S += c_qinv1_0 >= 33
	c_qinv1_0 += MAS[2]

	c_qinv1__t5_in = S.Task('c_qinv1__t5_in', length=1, delay_cost=1)
	S += c_qinv1__t5_in >= 33
	c_qinv1__t5_in += MAS_in[1]

	c_qinv1__t5_mem0 = S.Task('c_qinv1__t5_mem0', length=1, delay_cost=1)
	S += c_qinv1__t5_mem0 >= 33
	c_qinv1__t5_mem0 += MM_MEM[0]

	c_qinv1__t5_mem1 = S.Task('c_qinv1__t5_mem1', length=1, delay_cost=1)
	S += c_qinv1__t5_mem1 >= 33
	c_qinv1__t5_mem1 += MM_MEM[1]

	c_qinv00_in = S.Task('c_qinv00_in', length=1, delay_cost=1)
	S += c_qinv00_in >= 34
	c_qinv00_in += MAS_in[3]

	c_qinv00_mem0 = S.Task('c_qinv00_mem0', length=1, delay_cost=1)
	S += c_qinv00_mem0 >= 34
	c_qinv00_mem0 += MM_MEM[0]

	c_qinv00_mem1 = S.Task('c_qinv00_mem1', length=1, delay_cost=1)
	S += c_qinv00_mem1 >= 34
	c_qinv00_mem1 += MM_MEM[1]

	c_qinv1__t5 = S.Task('c_qinv1__t5', length=3, delay_cost=1)
	S += c_qinv1__t5 >= 34
	c_qinv1__t5 += MAS[1]

	c2_t1_t0_in = S.Task('c2_t1_t0_in', length=1, delay_cost=1)
	S += c2_t1_t0_in >= 35
	c2_t1_t0_in += MM_in[0]

	c2_t1_t0_mem0 = S.Task('c2_t1_t0_mem0', length=1, delay_cost=1)
	S += c2_t1_t0_mem0 >= 35
	c2_t1_t0_mem0 += MAIN_MEM_r[0]

	c2_t1_t0_mem1 = S.Task('c2_t1_t0_mem1', length=1, delay_cost=1)
	S += c2_t1_t0_mem1 >= 35
	c2_t1_t0_mem1 += MAS_MEM[5]

	c_qinv00 = S.Task('c_qinv00', length=3, delay_cost=1)
	S += c_qinv00 >= 35
	c_qinv00 += MAS[3]

	c_qinv0_t5_in = S.Task('c_qinv0_t5_in', length=1, delay_cost=1)
	S += c_qinv0_t5_in >= 35
	c_qinv0_t5_in += MAS_in[1]

	c_qinv0_t5_mem0 = S.Task('c_qinv0_t5_mem0', length=1, delay_cost=1)
	S += c_qinv0_t5_mem0 >= 35
	c_qinv0_t5_mem0 += MM_MEM[0]

	c_qinv0_t5_mem1 = S.Task('c_qinv0_t5_mem1', length=1, delay_cost=1)
	S += c_qinv0_t5_mem1 >= 35
	c_qinv0_t5_mem1 += MM_MEM[1]

	c0_t1_t0_in = S.Task('c0_t1_t0_in', length=1, delay_cost=1)
	S += c0_t1_t0_in >= 36
	c0_t1_t0_in += MM_in[0]

	c0_t1_t0_mem0 = S.Task('c0_t1_t0_mem0', length=1, delay_cost=1)
	S += c0_t1_t0_mem0 >= 36
	c0_t1_t0_mem0 += MAIN_MEM_r[0]

	c0_t1_t0_mem1 = S.Task('c0_t1_t0_mem1', length=1, delay_cost=1)
	S += c0_t1_t0_mem1 >= 36
	c0_t1_t0_mem1 += MAS_MEM[5]

	c2_t1_t0 = S.Task('c2_t1_t0', length=14, delay_cost=1)
	S += c2_t1_t0 >= 36
	c2_t1_t0 += MM[0]

	c_qinv0_t5 = S.Task('c_qinv0_t5', length=3, delay_cost=1)
	S += c_qinv0_t5 >= 36
	c_qinv0_t5 += MAS[1]

	c_qinv1_1_in = S.Task('c_qinv1_1_in', length=1, delay_cost=1)
	S += c_qinv1_1_in >= 36
	c_qinv1_1_in += MAS_in[1]

	c_qinv1_1_mem0 = S.Task('c_qinv1_1_mem0', length=1, delay_cost=1)
	S += c_qinv1_1_mem0 >= 36
	c_qinv1_1_mem0 += MM_MEM[0]

	c_qinv1_1_mem1 = S.Task('c_qinv1_1_mem1', length=1, delay_cost=1)
	S += c_qinv1_1_mem1 >= 36
	c_qinv1_1_mem1 += MAS_MEM[3]

	c0_t0_t0_in = S.Task('c0_t0_t0_in', length=1, delay_cost=1)
	S += c0_t0_t0_in >= 37
	c0_t0_t0_in += MM_in[0]

	c0_t0_t0_mem0 = S.Task('c0_t0_t0_mem0', length=1, delay_cost=1)
	S += c0_t0_t0_mem0 >= 37
	c0_t0_t0_mem0 += MAIN_MEM_r[0]

	c0_t0_t0_mem1 = S.Task('c0_t0_t0_mem1', length=1, delay_cost=1)
	S += c0_t0_t0_mem1 >= 37
	c0_t0_t0_mem1 += MAS_MEM[7]

	c0_t1_t0 = S.Task('c0_t1_t0', length=14, delay_cost=1)
	S += c0_t1_t0 >= 37
	c0_t1_t0 += MM[0]

	c1_t30_in = S.Task('c1_t30_in', length=1, delay_cost=1)
	S += c1_t30_in >= 37
	c1_t30_in += MAS_in[3]

	c1_t30_mem0 = S.Task('c1_t30_mem0', length=1, delay_cost=1)
	S += c1_t30_mem0 >= 37
	c1_t30_mem0 += MAS_MEM[6]

	c1_t30_mem1 = S.Task('c1_t30_mem1', length=1, delay_cost=1)
	S += c1_t30_mem1 >= 37
	c1_t30_mem1 += MAS_MEM[5]

	c_qinv1_1 = S.Task('c_qinv1_1', length=3, delay_cost=1)
	S += c_qinv1_1 >= 37
	c_qinv1_1 += MAS[1]

	c0_t0_t0 = S.Task('c0_t0_t0', length=14, delay_cost=1)
	S += c0_t0_t0 >= 38
	c0_t0_t0 += MM[0]

	c0_t30_in = S.Task('c0_t30_in', length=1, delay_cost=1)
	S += c0_t30_in >= 38
	c0_t30_in += MAS_in[3]

	c0_t30_mem0 = S.Task('c0_t30_mem0', length=1, delay_cost=1)
	S += c0_t30_mem0 >= 38
	c0_t30_mem0 += MAS_MEM[6]

	c0_t30_mem1 = S.Task('c0_t30_mem1', length=1, delay_cost=1)
	S += c0_t30_mem1 >= 38
	c0_t30_mem1 += MAS_MEM[5]

	c1_t30 = S.Task('c1_t30', length=3, delay_cost=1)
	S += c1_t30 >= 38
	c1_t30 += MAS[3]

	c2_t0_t0_in = S.Task('c2_t0_t0_in', length=1, delay_cost=1)
	S += c2_t0_t0_in >= 38
	c2_t0_t0_in += MM_in[0]

	c2_t0_t0_mem0 = S.Task('c2_t0_t0_mem0', length=1, delay_cost=1)
	S += c2_t0_t0_mem0 >= 38
	c2_t0_t0_mem0 += MAIN_MEM_r[0]

	c2_t0_t0_mem1 = S.Task('c2_t0_t0_mem1', length=1, delay_cost=1)
	S += c2_t0_t0_mem1 >= 38
	c2_t0_t0_mem1 += MAS_MEM[7]

	c_qinv01_in = S.Task('c_qinv01_in', length=1, delay_cost=1)
	S += c_qinv01_in >= 38
	c_qinv01_in += MAS_in[0]

	c_qinv01_mem0 = S.Task('c_qinv01_mem0', length=1, delay_cost=1)
	S += c_qinv01_mem0 >= 38
	c_qinv01_mem0 += MM_MEM[0]

	c_qinv01_mem1 = S.Task('c_qinv01_mem1', length=1, delay_cost=1)
	S += c_qinv01_mem1 >= 38
	c_qinv01_mem1 += MAS_MEM[3]

	c0_t1_t3_in = S.Task('c0_t1_t3_in', length=1, delay_cost=1)
	S += c0_t1_t3_in >= 39
	c0_t1_t3_in += MAS_in[0]

	c0_t1_t3_mem0 = S.Task('c0_t1_t3_mem0', length=1, delay_cost=1)
	S += c0_t1_t3_mem0 >= 39
	c0_t1_t3_mem0 += MAS_MEM[4]

	c0_t1_t3_mem1 = S.Task('c0_t1_t3_mem1', length=1, delay_cost=1)
	S += c0_t1_t3_mem1 >= 39
	c0_t1_t3_mem1 += MAS_MEM[3]

	c0_t30 = S.Task('c0_t30', length=3, delay_cost=1)
	S += c0_t30 >= 39
	c0_t30 += MAS[3]

	c1_t0_t0_in = S.Task('c1_t0_t0_in', length=1, delay_cost=1)
	S += c1_t0_t0_in >= 39
	c1_t0_t0_in += MM_in[0]

	c1_t0_t0_mem0 = S.Task('c1_t0_t0_mem0', length=1, delay_cost=1)
	S += c1_t0_t0_mem0 >= 39
	c1_t0_t0_mem0 += MAIN_MEM_r[0]

	c1_t0_t0_mem1 = S.Task('c1_t0_t0_mem1', length=1, delay_cost=1)
	S += c1_t0_t0_mem1 >= 39
	c1_t0_t0_mem1 += MAS_MEM[7]

	c2_t0_t0 = S.Task('c2_t0_t0', length=14, delay_cost=1)
	S += c2_t0_t0 >= 39
	c2_t0_t0 += MM[0]

	c2_t30_in = S.Task('c2_t30_in', length=1, delay_cost=1)
	S += c2_t30_in >= 39
	c2_t30_in += MAS_in[3]

	c2_t30_mem0 = S.Task('c2_t30_mem0', length=1, delay_cost=1)
	S += c2_t30_mem0 >= 39
	c2_t30_mem0 += MAS_MEM[6]

	c2_t30_mem1 = S.Task('c2_t30_mem1', length=1, delay_cost=1)
	S += c2_t30_mem1 >= 39
	c2_t30_mem1 += MAS_MEM[5]

	c_qinv01 = S.Task('c_qinv01', length=3, delay_cost=1)
	S += c_qinv01 >= 39
	c_qinv01 += MAS[0]

	c0_t1_t3 = S.Task('c0_t1_t3', length=3, delay_cost=1)
	S += c0_t1_t3 >= 40
	c0_t1_t3 += MAS[0]

	c1_t0_t0 = S.Task('c1_t0_t0', length=14, delay_cost=1)
	S += c1_t0_t0 >= 40
	c1_t0_t0 += MM[0]

	c1_t1_t0_in = S.Task('c1_t1_t0_in', length=1, delay_cost=1)
	S += c1_t1_t0_in >= 40
	c1_t1_t0_in += MM_in[0]

	c1_t1_t0_mem0 = S.Task('c1_t1_t0_mem0', length=1, delay_cost=1)
	S += c1_t1_t0_mem0 >= 40
	c1_t1_t0_mem0 += MAIN_MEM_r[0]

	c1_t1_t0_mem1 = S.Task('c1_t1_t0_mem1', length=1, delay_cost=1)
	S += c1_t1_t0_mem1 >= 40
	c1_t1_t0_mem1 += MAS_MEM[5]

	c2_t1_t3_in = S.Task('c2_t1_t3_in', length=1, delay_cost=1)
	S += c2_t1_t3_in >= 40
	c2_t1_t3_in += MAS_in[1]

	c2_t1_t3_mem0 = S.Task('c2_t1_t3_mem0', length=1, delay_cost=1)
	S += c2_t1_t3_mem0 >= 40
	c2_t1_t3_mem0 += MAS_MEM[4]

	c2_t1_t3_mem1 = S.Task('c2_t1_t3_mem1', length=1, delay_cost=1)
	S += c2_t1_t3_mem1 >= 40
	c2_t1_t3_mem1 += MAS_MEM[3]

	c2_t30 = S.Task('c2_t30', length=3, delay_cost=1)
	S += c2_t30 >= 40
	c2_t30 += MAS[3]

	c0_t31_in = S.Task('c0_t31_in', length=1, delay_cost=1)
	S += c0_t31_in >= 41
	c0_t31_in += MAS_in[0]

	c0_t31_mem0 = S.Task('c0_t31_mem0', length=1, delay_cost=1)
	S += c0_t31_mem0 >= 41
	c0_t31_mem0 += MAS_MEM[0]

	c0_t31_mem1 = S.Task('c0_t31_mem1', length=1, delay_cost=1)
	S += c0_t31_mem1 >= 41
	c0_t31_mem1 += MAS_MEM[3]

	c0_t4_t0_in = S.Task('c0_t4_t0_in', length=1, delay_cost=1)
	S += c0_t4_t0_in >= 41
	c0_t4_t0_in += MM_in[0]

	c0_t4_t0_mem0 = S.Task('c0_t4_t0_mem0', length=1, delay_cost=1)
	S += c0_t4_t0_mem0 >= 41
	c0_t4_t0_mem0 += MAS_MEM[2]

	c0_t4_t0_mem1 = S.Task('c0_t4_t0_mem1', length=1, delay_cost=1)
	S += c0_t4_t0_mem1 >= 41
	c0_t4_t0_mem1 += MAS_MEM[7]

	c1_t1_t0 = S.Task('c1_t1_t0', length=14, delay_cost=1)
	S += c1_t1_t0 >= 41
	c1_t1_t0 += MM[0]

	c2_t0_t3_in = S.Task('c2_t0_t3_in', length=1, delay_cost=1)
	S += c2_t0_t3_in >= 41
	c2_t0_t3_in += MAS_in[2]

	c2_t0_t3_mem0 = S.Task('c2_t0_t3_mem0', length=1, delay_cost=1)
	S += c2_t0_t3_mem0 >= 41
	c2_t0_t3_mem0 += MAS_MEM[6]

	c2_t0_t3_mem1 = S.Task('c2_t0_t3_mem1', length=1, delay_cost=1)
	S += c2_t0_t3_mem1 >= 41
	c2_t0_t3_mem1 += MAS_MEM[1]

	c2_t1_t3 = S.Task('c2_t1_t3', length=3, delay_cost=1)
	S += c2_t1_t3 >= 41
	c2_t1_t3 += MAS[1]

	c0_t0_t3_in = S.Task('c0_t0_t3_in', length=1, delay_cost=1)
	S += c0_t0_t3_in >= 42
	c0_t0_t3_in += MAS_in[2]

	c0_t0_t3_mem0 = S.Task('c0_t0_t3_mem0', length=1, delay_cost=1)
	S += c0_t0_t3_mem0 >= 42
	c0_t0_t3_mem0 += MAS_MEM[6]

	c0_t0_t3_mem1 = S.Task('c0_t0_t3_mem1', length=1, delay_cost=1)
	S += c0_t0_t3_mem1 >= 42
	c0_t0_t3_mem1 += MAS_MEM[1]

	c0_t31 = S.Task('c0_t31', length=3, delay_cost=1)
	S += c0_t31 >= 42
	c0_t31 += MAS[0]

	c0_t4_t0 = S.Task('c0_t4_t0', length=14, delay_cost=1)
	S += c0_t4_t0 >= 42
	c0_t4_t0 += MM[0]

	c1_t4_t0_in = S.Task('c1_t4_t0_in', length=1, delay_cost=1)
	S += c1_t4_t0_in >= 42
	c1_t4_t0_in += MM_in[0]

	c1_t4_t0_mem0 = S.Task('c1_t4_t0_mem0', length=1, delay_cost=1)
	S += c1_t4_t0_mem0 >= 42
	c1_t4_t0_mem0 += MAS_MEM[4]

	c1_t4_t0_mem1 = S.Task('c1_t4_t0_mem1', length=1, delay_cost=1)
	S += c1_t4_t0_mem1 >= 42
	c1_t4_t0_mem1 += MAS_MEM[7]

	c2_t0_t3 = S.Task('c2_t0_t3', length=3, delay_cost=1)
	S += c2_t0_t3 >= 42
	c2_t0_t3 += MAS[2]

	c2_t31_in = S.Task('c2_t31_in', length=1, delay_cost=1)
	S += c2_t31_in >= 42
	c2_t31_in += MAS_in[3]

	c2_t31_mem0 = S.Task('c2_t31_mem0', length=1, delay_cost=1)
	S += c2_t31_mem0 >= 42
	c2_t31_mem0 += MAS_MEM[0]

	c2_t31_mem1 = S.Task('c2_t31_mem1', length=1, delay_cost=1)
	S += c2_t31_mem1 >= 42
	c2_t31_mem1 += MAS_MEM[3]

	c0_t0_t3 = S.Task('c0_t0_t3', length=3, delay_cost=1)
	S += c0_t0_t3 >= 43
	c0_t0_t3 += MAS[2]

	c1_t0_t3_in = S.Task('c1_t0_t3_in', length=1, delay_cost=1)
	S += c1_t0_t3_in >= 43
	c1_t0_t3_in += MAS_in[0]

	c1_t0_t3_mem0 = S.Task('c1_t0_t3_mem0', length=1, delay_cost=1)
	S += c1_t0_t3_mem0 >= 43
	c1_t0_t3_mem0 += MAS_MEM[6]

	c1_t0_t3_mem1 = S.Task('c1_t0_t3_mem1', length=1, delay_cost=1)
	S += c1_t0_t3_mem1 >= 43
	c1_t0_t3_mem1 += MAS_MEM[1]

	c1_t31_in = S.Task('c1_t31_in', length=1, delay_cost=1)
	S += c1_t31_in >= 43
	c1_t31_in += MAS_in[1]

	c1_t31_mem0 = S.Task('c1_t31_mem0', length=1, delay_cost=1)
	S += c1_t31_mem0 >= 43
	c1_t31_mem0 += MAS_MEM[0]

	c1_t31_mem1 = S.Task('c1_t31_mem1', length=1, delay_cost=1)
	S += c1_t31_mem1 >= 43
	c1_t31_mem1 += MAS_MEM[3]

	c1_t4_t0 = S.Task('c1_t4_t0', length=14, delay_cost=1)
	S += c1_t4_t0 >= 43
	c1_t4_t0 += MM[0]

	c2_t31 = S.Task('c2_t31', length=3, delay_cost=1)
	S += c2_t31 >= 43
	c2_t31 += MAS[3]

	c2_t4_t0_in = S.Task('c2_t4_t0_in', length=1, delay_cost=1)
	S += c2_t4_t0_in >= 43
	c2_t4_t0_in += MM_in[0]

	c2_t4_t0_mem0 = S.Task('c2_t4_t0_mem0', length=1, delay_cost=1)
	S += c2_t4_t0_mem0 >= 43
	c2_t4_t0_mem0 += MAS_MEM[4]

	c2_t4_t0_mem1 = S.Task('c2_t4_t0_mem1', length=1, delay_cost=1)
	S += c2_t4_t0_mem1 >= 43
	c2_t4_t0_mem1 += MAS_MEM[7]

	c1_t0_t1_in = S.Task('c1_t0_t1_in', length=1, delay_cost=1)
	S += c1_t0_t1_in >= 44
	c1_t0_t1_in += MM_in[0]

	c1_t0_t1_mem0 = S.Task('c1_t0_t1_mem0', length=1, delay_cost=1)
	S += c1_t0_t1_mem0 >= 44
	c1_t0_t1_mem0 += MAIN_MEM_r[0]

	c1_t0_t1_mem1 = S.Task('c1_t0_t1_mem1', length=1, delay_cost=1)
	S += c1_t0_t1_mem1 >= 44
	c1_t0_t1_mem1 += MAS_MEM[1]

	c1_t0_t3 = S.Task('c1_t0_t3', length=3, delay_cost=1)
	S += c1_t0_t3 >= 44
	c1_t0_t3 += MAS[0]

	c1_t1_t3_in = S.Task('c1_t1_t3_in', length=1, delay_cost=1)
	S += c1_t1_t3_in >= 44
	c1_t1_t3_in += MAS_in[3]

	c1_t1_t3_mem0 = S.Task('c1_t1_t3_mem0', length=1, delay_cost=1)
	S += c1_t1_t3_mem0 >= 44
	c1_t1_t3_mem0 += MAS_MEM[4]

	c1_t1_t3_mem1 = S.Task('c1_t1_t3_mem1', length=1, delay_cost=1)
	S += c1_t1_t3_mem1 >= 44
	c1_t1_t3_mem1 += MAS_MEM[3]

	c1_t31 = S.Task('c1_t31', length=3, delay_cost=1)
	S += c1_t31 >= 44
	c1_t31 += MAS[1]

	c2_t4_t0 = S.Task('c2_t4_t0', length=14, delay_cost=1)
	S += c2_t4_t0 >= 44
	c2_t4_t0 += MM[0]

	c1_t0_t1 = S.Task('c1_t0_t1', length=14, delay_cost=1)
	S += c1_t0_t1 >= 45
	c1_t0_t1 += MM[0]

	c1_t1_t3 = S.Task('c1_t1_t3', length=3, delay_cost=1)
	S += c1_t1_t3 >= 45
	c1_t1_t3 += MAS[3]

	c2_t0_t1_in = S.Task('c2_t0_t1_in', length=1, delay_cost=1)
	S += c2_t0_t1_in >= 45
	c2_t0_t1_in += MM_in[0]

	c2_t0_t1_mem0 = S.Task('c2_t0_t1_mem0', length=1, delay_cost=1)
	S += c2_t0_t1_mem0 >= 45
	c2_t0_t1_mem0 += MAIN_MEM_r[0]

	c2_t0_t1_mem1 = S.Task('c2_t0_t1_mem1', length=1, delay_cost=1)
	S += c2_t0_t1_mem1 >= 45
	c2_t0_t1_mem1 += MAS_MEM[1]

	c2_t0_t1 = S.Task('c2_t0_t1', length=14, delay_cost=1)
	S += c2_t0_t1 >= 46
	c2_t0_t1 += MM[0]

	c2_t1_t1_in = S.Task('c2_t1_t1_in', length=1, delay_cost=1)
	S += c2_t1_t1_in >= 46
	c2_t1_t1_in += MM_in[0]

	c2_t1_t1_mem0 = S.Task('c2_t1_t1_mem0', length=1, delay_cost=1)
	S += c2_t1_t1_mem0 >= 46
	c2_t1_t1_mem0 += MAIN_MEM_r[0]

	c2_t1_t1_mem1 = S.Task('c2_t1_t1_mem1', length=1, delay_cost=1)
	S += c2_t1_t1_mem1 >= 46
	c2_t1_t1_mem1 += MAS_MEM[3]

	c0_t0_t1_in = S.Task('c0_t0_t1_in', length=1, delay_cost=1)
	S += c0_t0_t1_in >= 47
	c0_t0_t1_in += MM_in[0]

	c0_t0_t1_mem0 = S.Task('c0_t0_t1_mem0', length=1, delay_cost=1)
	S += c0_t0_t1_mem0 >= 47
	c0_t0_t1_mem0 += MAIN_MEM_r[0]

	c0_t0_t1_mem1 = S.Task('c0_t0_t1_mem1', length=1, delay_cost=1)
	S += c0_t0_t1_mem1 >= 47
	c0_t0_t1_mem1 += MAS_MEM[1]

	c2_t1_t1 = S.Task('c2_t1_t1', length=14, delay_cost=1)
	S += c2_t1_t1 >= 47
	c2_t1_t1 += MM[0]

	c0_t0_t1 = S.Task('c0_t0_t1', length=14, delay_cost=1)
	S += c0_t0_t1 >= 48
	c0_t0_t1 += MM[0]

	c0_t1_t1_in = S.Task('c0_t1_t1_in', length=1, delay_cost=1)
	S += c0_t1_t1_in >= 48
	c0_t1_t1_in += MM_in[0]

	c0_t1_t1_mem0 = S.Task('c0_t1_t1_mem0', length=1, delay_cost=1)
	S += c0_t1_t1_mem0 >= 48
	c0_t1_t1_mem0 += MAIN_MEM_r[0]

	c0_t1_t1_mem1 = S.Task('c0_t1_t1_mem1', length=1, delay_cost=1)
	S += c0_t1_t1_mem1 >= 48
	c0_t1_t1_mem1 += MAS_MEM[3]

	c0_t1_t1 = S.Task('c0_t1_t1', length=14, delay_cost=1)
	S += c0_t1_t1 >= 49
	c0_t1_t1 += MM[0]

	c1_t1_t1_in = S.Task('c1_t1_t1_in', length=1, delay_cost=1)
	S += c1_t1_t1_in >= 49
	c1_t1_t1_in += MM_in[0]

	c1_t1_t1_mem0 = S.Task('c1_t1_t1_mem0', length=1, delay_cost=1)
	S += c1_t1_t1_mem0 >= 49
	c1_t1_t1_mem0 += MAIN_MEM_r[0]

	c1_t1_t1_mem1 = S.Task('c1_t1_t1_mem1', length=1, delay_cost=1)
	S += c1_t1_t1_mem1 >= 49
	c1_t1_t1_mem1 += MAS_MEM[3]

	c1_t1_t1 = S.Task('c1_t1_t1', length=14, delay_cost=1)
	S += c1_t1_t1 >= 50
	c1_t1_t1 += MM[0]


	# new tasks
	c0_t0_t4 = S.Task('c0_t0_t4', length=14, delay_cost=1)
	c0_t0_t4 += alt(MM)
	c0_t0_t4_in = S.Task('c0_t0_t4_in', length=1, delay_cost=1)
	c0_t0_t4_in += alt(MM_in)
	S += c0_t0_t4_in*MM_in[0]<=c0_t0_t4*MM[0]
	c0_t0_t4_mem0 = S.Task('c0_t0_t4_mem0', length=1, delay_cost=1)
	c0_t0_t4_mem0 += MAS_MEM[0]
	S += 19 < c0_t0_t4_mem0
	S += c0_t0_t4_mem0 <= c0_t0_t4

	c0_t0_t4_mem1 = S.Task('c0_t0_t4_mem1', length=1, delay_cost=1)
	c0_t0_t4_mem1 += MAS_MEM[5]
	S += 45 < c0_t0_t4_mem1
	S += c0_t0_t4_mem1 <= c0_t0_t4

	c0_t00 = S.Task('c0_t00', length=3, delay_cost=1)
	c0_t00 += alt(MAS)
	c0_t00_in = S.Task('c0_t00_in', length=1, delay_cost=1)
	c0_t00_in += alt(MAS_in)
	S += c0_t00_in*MAS_in[0]<=c0_t00*MAS[0]

	S += c0_t00_in*MAS_in[1]<=c0_t00*MAS[1]

	S += c0_t00_in*MAS_in[2]<=c0_t00*MAS[2]

	S += c0_t00_in*MAS_in[3]<=c0_t00*MAS[3]

	c0_t00_mem0 = S.Task('c0_t00_mem0', length=1, delay_cost=1)
	c0_t00_mem0 += MM_MEM[0]
	S += 51 < c0_t00_mem0
	S += c0_t00_mem0 <= c0_t00

	c0_t00_mem1 = S.Task('c0_t00_mem1', length=1, delay_cost=1)
	c0_t00_mem1 += MM_MEM[1]
	S += 61 < c0_t00_mem1
	S += c0_t00_mem1 <= c0_t00

	c0_t0_t5 = S.Task('c0_t0_t5', length=3, delay_cost=1)
	c0_t0_t5 += alt(MAS)
	c0_t0_t5_in = S.Task('c0_t0_t5_in', length=1, delay_cost=1)
	c0_t0_t5_in += alt(MAS_in)
	S += c0_t0_t5_in*MAS_in[0]<=c0_t0_t5*MAS[0]

	S += c0_t0_t5_in*MAS_in[1]<=c0_t0_t5*MAS[1]

	S += c0_t0_t5_in*MAS_in[2]<=c0_t0_t5*MAS[2]

	S += c0_t0_t5_in*MAS_in[3]<=c0_t0_t5*MAS[3]

	c0_t0_t5_mem0 = S.Task('c0_t0_t5_mem0', length=1, delay_cost=1)
	c0_t0_t5_mem0 += MM_MEM[0]
	S += 51 < c0_t0_t5_mem0
	S += c0_t0_t5_mem0 <= c0_t0_t5

	c0_t0_t5_mem1 = S.Task('c0_t0_t5_mem1', length=1, delay_cost=1)
	c0_t0_t5_mem1 += MM_MEM[1]
	S += 61 < c0_t0_t5_mem1
	S += c0_t0_t5_mem1 <= c0_t0_t5

	c0_t1_t4 = S.Task('c0_t1_t4', length=14, delay_cost=1)
	c0_t1_t4 += alt(MM)
	c0_t1_t4_in = S.Task('c0_t1_t4_in', length=1, delay_cost=1)
	c0_t1_t4_in += alt(MM_in)
	S += c0_t1_t4_in*MM_in[0]<=c0_t1_t4*MM[0]
	c0_t1_t4_mem0 = S.Task('c0_t1_t4_mem0', length=1, delay_cost=1)
	c0_t1_t4_mem0 += MAS_MEM[2]
	S += 12 < c0_t1_t4_mem0
	S += c0_t1_t4_mem0 <= c0_t1_t4

	c0_t1_t4_mem1 = S.Task('c0_t1_t4_mem1', length=1, delay_cost=1)
	c0_t1_t4_mem1 += MAS_MEM[1]
	S += 42 < c0_t1_t4_mem1
	S += c0_t1_t4_mem1 <= c0_t1_t4

	c0_t10 = S.Task('c0_t10', length=3, delay_cost=1)
	c0_t10 += alt(MAS)
	c0_t10_in = S.Task('c0_t10_in', length=1, delay_cost=1)
	c0_t10_in += alt(MAS_in)
	S += c0_t10_in*MAS_in[0]<=c0_t10*MAS[0]

	S += c0_t10_in*MAS_in[1]<=c0_t10*MAS[1]

	S += c0_t10_in*MAS_in[2]<=c0_t10*MAS[2]

	S += c0_t10_in*MAS_in[3]<=c0_t10*MAS[3]

	c0_t10_mem0 = S.Task('c0_t10_mem0', length=1, delay_cost=1)
	c0_t10_mem0 += MM_MEM[0]
	S += 62 < c0_t10_mem0
	S += c0_t10_mem0 <= c0_t10

	c0_t10_mem1 = S.Task('c0_t10_mem1', length=1, delay_cost=1)
	c0_t10_mem1 += MM_MEM[1]
	S += 50 < c0_t10_mem1
	S += c0_t10_mem1 <= c0_t10

	c0_t1_t5 = S.Task('c0_t1_t5', length=3, delay_cost=1)
	c0_t1_t5 += alt(MAS)
	c0_t1_t5_in = S.Task('c0_t1_t5_in', length=1, delay_cost=1)
	c0_t1_t5_in += alt(MAS_in)
	S += c0_t1_t5_in*MAS_in[0]<=c0_t1_t5*MAS[0]

	S += c0_t1_t5_in*MAS_in[1]<=c0_t1_t5*MAS[1]

	S += c0_t1_t5_in*MAS_in[2]<=c0_t1_t5*MAS[2]

	S += c0_t1_t5_in*MAS_in[3]<=c0_t1_t5*MAS[3]

	c0_t1_t5_mem0 = S.Task('c0_t1_t5_mem0', length=1, delay_cost=1)
	c0_t1_t5_mem0 += MM_MEM[0]
	S += 50 < c0_t1_t5_mem0
	S += c0_t1_t5_mem0 <= c0_t1_t5

	c0_t1_t5_mem1 = S.Task('c0_t1_t5_mem1', length=1, delay_cost=1)
	c0_t1_t5_mem1 += MM_MEM[1]
	S += 62 < c0_t1_t5_mem1
	S += c0_t1_t5_mem1 <= c0_t1_t5

	c0_t4_t1 = S.Task('c0_t4_t1', length=14, delay_cost=1)
	c0_t4_t1 += alt(MM)
	c0_t4_t1_in = S.Task('c0_t4_t1_in', length=1, delay_cost=1)
	c0_t4_t1_in += alt(MM_in)
	S += c0_t4_t1_in*MM_in[0]<=c0_t4_t1*MM[0]
	c0_t4_t1_mem0 = S.Task('c0_t4_t1_mem0', length=1, delay_cost=1)
	c0_t4_t1_mem0 += MAS_MEM[4]
	S += 9 < c0_t4_t1_mem0
	S += c0_t4_t1_mem0 <= c0_t4_t1

	c0_t4_t1_mem1 = S.Task('c0_t4_t1_mem1', length=1, delay_cost=1)
	c0_t4_t1_mem1 += MAS_MEM[1]
	S += 44 < c0_t4_t1_mem1
	S += c0_t4_t1_mem1 <= c0_t4_t1

	c0_t4_t3 = S.Task('c0_t4_t3', length=3, delay_cost=1)
	c0_t4_t3 += alt(MAS)
	c0_t4_t3_in = S.Task('c0_t4_t3_in', length=1, delay_cost=1)
	c0_t4_t3_in += alt(MAS_in)
	S += c0_t4_t3_in*MAS_in[0]<=c0_t4_t3*MAS[0]

	S += c0_t4_t3_in*MAS_in[1]<=c0_t4_t3*MAS[1]

	S += c0_t4_t3_in*MAS_in[2]<=c0_t4_t3*MAS[2]

	S += c0_t4_t3_in*MAS_in[3]<=c0_t4_t3*MAS[3]

	c0_t4_t3_mem0 = S.Task('c0_t4_t3_mem0', length=1, delay_cost=1)
	c0_t4_t3_mem0 += MAS_MEM[6]
	S += 41 < c0_t4_t3_mem0
	S += c0_t4_t3_mem0 <= c0_t4_t3

	c0_t4_t3_mem1 = S.Task('c0_t4_t3_mem1', length=1, delay_cost=1)
	c0_t4_t3_mem1 += MAS_MEM[1]
	S += 44 < c0_t4_t3_mem1
	S += c0_t4_t3_mem1 <= c0_t4_t3

	c1_t0_t4 = S.Task('c1_t0_t4', length=14, delay_cost=1)
	c1_t0_t4 += alt(MM)
	c1_t0_t4_in = S.Task('c1_t0_t4_in', length=1, delay_cost=1)
	c1_t0_t4_in += alt(MM_in)
	S += c1_t0_t4_in*MM_in[0]<=c1_t0_t4*MM[0]
	c1_t0_t4_mem0 = S.Task('c1_t0_t4_mem0', length=1, delay_cost=1)
	c1_t0_t4_mem0 += MAS_MEM[6]
	S += 18 < c1_t0_t4_mem0
	S += c1_t0_t4_mem0 <= c1_t0_t4

	c1_t0_t4_mem1 = S.Task('c1_t0_t4_mem1', length=1, delay_cost=1)
	c1_t0_t4_mem1 += MAS_MEM[1]
	S += 46 < c1_t0_t4_mem1
	S += c1_t0_t4_mem1 <= c1_t0_t4

	c1_t00 = S.Task('c1_t00', length=3, delay_cost=1)
	c1_t00 += alt(MAS)
	c1_t00_in = S.Task('c1_t00_in', length=1, delay_cost=1)
	c1_t00_in += alt(MAS_in)
	S += c1_t00_in*MAS_in[0]<=c1_t00*MAS[0]

	S += c1_t00_in*MAS_in[1]<=c1_t00*MAS[1]

	S += c1_t00_in*MAS_in[2]<=c1_t00*MAS[2]

	S += c1_t00_in*MAS_in[3]<=c1_t00*MAS[3]

	c1_t00_mem0 = S.Task('c1_t00_mem0', length=1, delay_cost=1)
	c1_t00_mem0 += MM_MEM[0]
	S += 53 < c1_t00_mem0
	S += c1_t00_mem0 <= c1_t00

	c1_t00_mem1 = S.Task('c1_t00_mem1', length=1, delay_cost=1)
	c1_t00_mem1 += MM_MEM[1]
	S += 58 < c1_t00_mem1
	S += c1_t00_mem1 <= c1_t00

	c1_t0_t5 = S.Task('c1_t0_t5', length=3, delay_cost=1)
	c1_t0_t5 += alt(MAS)
	c1_t0_t5_in = S.Task('c1_t0_t5_in', length=1, delay_cost=1)
	c1_t0_t5_in += alt(MAS_in)
	S += c1_t0_t5_in*MAS_in[0]<=c1_t0_t5*MAS[0]

	S += c1_t0_t5_in*MAS_in[1]<=c1_t0_t5*MAS[1]

	S += c1_t0_t5_in*MAS_in[2]<=c1_t0_t5*MAS[2]

	S += c1_t0_t5_in*MAS_in[3]<=c1_t0_t5*MAS[3]

	c1_t0_t5_mem0 = S.Task('c1_t0_t5_mem0', length=1, delay_cost=1)
	c1_t0_t5_mem0 += MM_MEM[0]
	S += 53 < c1_t0_t5_mem0
	S += c1_t0_t5_mem0 <= c1_t0_t5

	c1_t0_t5_mem1 = S.Task('c1_t0_t5_mem1', length=1, delay_cost=1)
	c1_t0_t5_mem1 += MM_MEM[1]
	S += 58 < c1_t0_t5_mem1
	S += c1_t0_t5_mem1 <= c1_t0_t5

	c1_t1_t4 = S.Task('c1_t1_t4', length=14, delay_cost=1)
	c1_t1_t4 += alt(MM)
	c1_t1_t4_in = S.Task('c1_t1_t4_in', length=1, delay_cost=1)
	c1_t1_t4_in += alt(MM_in)
	S += c1_t1_t4_in*MM_in[0]<=c1_t1_t4*MM[0]
	c1_t1_t4_mem0 = S.Task('c1_t1_t4_mem0', length=1, delay_cost=1)
	c1_t1_t4_mem0 += MAS_MEM[2]
	S += 16 < c1_t1_t4_mem0
	S += c1_t1_t4_mem0 <= c1_t1_t4

	c1_t1_t4_mem1 = S.Task('c1_t1_t4_mem1', length=1, delay_cost=1)
	c1_t1_t4_mem1 += MAS_MEM[7]
	S += 47 < c1_t1_t4_mem1
	S += c1_t1_t4_mem1 <= c1_t1_t4

	c1_t10 = S.Task('c1_t10', length=3, delay_cost=1)
	c1_t10 += alt(MAS)
	c1_t10_in = S.Task('c1_t10_in', length=1, delay_cost=1)
	c1_t10_in += alt(MAS_in)
	S += c1_t10_in*MAS_in[0]<=c1_t10*MAS[0]

	S += c1_t10_in*MAS_in[1]<=c1_t10*MAS[1]

	S += c1_t10_in*MAS_in[2]<=c1_t10*MAS[2]

	S += c1_t10_in*MAS_in[3]<=c1_t10*MAS[3]

	c1_t10_mem0 = S.Task('c1_t10_mem0', length=1, delay_cost=1)
	c1_t10_mem0 += MM_MEM[0]
	S += 63 < c1_t10_mem0
	S += c1_t10_mem0 <= c1_t10

	c1_t10_mem1 = S.Task('c1_t10_mem1', length=1, delay_cost=1)
	c1_t10_mem1 += MM_MEM[1]
	S += 54 < c1_t10_mem1
	S += c1_t10_mem1 <= c1_t10

	c1_t1_t5 = S.Task('c1_t1_t5', length=3, delay_cost=1)
	c1_t1_t5 += alt(MAS)
	c1_t1_t5_in = S.Task('c1_t1_t5_in', length=1, delay_cost=1)
	c1_t1_t5_in += alt(MAS_in)
	S += c1_t1_t5_in*MAS_in[0]<=c1_t1_t5*MAS[0]

	S += c1_t1_t5_in*MAS_in[1]<=c1_t1_t5*MAS[1]

	S += c1_t1_t5_in*MAS_in[2]<=c1_t1_t5*MAS[2]

	S += c1_t1_t5_in*MAS_in[3]<=c1_t1_t5*MAS[3]

	c1_t1_t5_mem0 = S.Task('c1_t1_t5_mem0', length=1, delay_cost=1)
	c1_t1_t5_mem0 += MM_MEM[0]
	S += 54 < c1_t1_t5_mem0
	S += c1_t1_t5_mem0 <= c1_t1_t5

	c1_t1_t5_mem1 = S.Task('c1_t1_t5_mem1', length=1, delay_cost=1)
	c1_t1_t5_mem1 += MM_MEM[1]
	S += 63 < c1_t1_t5_mem1
	S += c1_t1_t5_mem1 <= c1_t1_t5

	c1_t4_t1 = S.Task('c1_t4_t1', length=14, delay_cost=1)
	c1_t4_t1 += alt(MM)
	c1_t4_t1_in = S.Task('c1_t4_t1_in', length=1, delay_cost=1)
	c1_t4_t1_in += alt(MM_in)
	S += c1_t4_t1_in*MM_in[0]<=c1_t4_t1*MM[0]
	c1_t4_t1_mem0 = S.Task('c1_t4_t1_mem0', length=1, delay_cost=1)
	c1_t4_t1_mem0 += MAS_MEM[6]
	S += 6 < c1_t4_t1_mem0
	S += c1_t4_t1_mem0 <= c1_t4_t1

	c1_t4_t1_mem1 = S.Task('c1_t4_t1_mem1', length=1, delay_cost=1)
	c1_t4_t1_mem1 += MAS_MEM[3]
	S += 46 < c1_t4_t1_mem1
	S += c1_t4_t1_mem1 <= c1_t4_t1

	c1_t4_t3 = S.Task('c1_t4_t3', length=3, delay_cost=1)
	c1_t4_t3 += alt(MAS)
	c1_t4_t3_in = S.Task('c1_t4_t3_in', length=1, delay_cost=1)
	c1_t4_t3_in += alt(MAS_in)
	S += c1_t4_t3_in*MAS_in[0]<=c1_t4_t3*MAS[0]

	S += c1_t4_t3_in*MAS_in[1]<=c1_t4_t3*MAS[1]

	S += c1_t4_t3_in*MAS_in[2]<=c1_t4_t3*MAS[2]

	S += c1_t4_t3_in*MAS_in[3]<=c1_t4_t3*MAS[3]

	c1_t4_t3_mem0 = S.Task('c1_t4_t3_mem0', length=1, delay_cost=1)
	c1_t4_t3_mem0 += MAS_MEM[6]
	S += 40 < c1_t4_t3_mem0
	S += c1_t4_t3_mem0 <= c1_t4_t3

	c1_t4_t3_mem1 = S.Task('c1_t4_t3_mem1', length=1, delay_cost=1)
	c1_t4_t3_mem1 += MAS_MEM[3]
	S += 46 < c1_t4_t3_mem1
	S += c1_t4_t3_mem1 <= c1_t4_t3

	c2_t0_t4 = S.Task('c2_t0_t4', length=14, delay_cost=1)
	c2_t0_t4 += alt(MM)
	c2_t0_t4_in = S.Task('c2_t0_t4_in', length=1, delay_cost=1)
	c2_t0_t4_in += alt(MM_in)
	S += c2_t0_t4_in*MM_in[0]<=c2_t0_t4*MM[0]
	c2_t0_t4_mem0 = S.Task('c2_t0_t4_mem0', length=1, delay_cost=1)
	c2_t0_t4_mem0 += MAS_MEM[0]
	S += 15 < c2_t0_t4_mem0
	S += c2_t0_t4_mem0 <= c2_t0_t4

	c2_t0_t4_mem1 = S.Task('c2_t0_t4_mem1', length=1, delay_cost=1)
	c2_t0_t4_mem1 += MAS_MEM[5]
	S += 44 < c2_t0_t4_mem1
	S += c2_t0_t4_mem1 <= c2_t0_t4

	c2_t00 = S.Task('c2_t00', length=3, delay_cost=1)
	c2_t00 += alt(MAS)
	c2_t00_in = S.Task('c2_t00_in', length=1, delay_cost=1)
	c2_t00_in += alt(MAS_in)
	S += c2_t00_in*MAS_in[0]<=c2_t00*MAS[0]

	S += c2_t00_in*MAS_in[1]<=c2_t00*MAS[1]

	S += c2_t00_in*MAS_in[2]<=c2_t00*MAS[2]

	S += c2_t00_in*MAS_in[3]<=c2_t00*MAS[3]

	c2_t00_mem0 = S.Task('c2_t00_mem0', length=1, delay_cost=1)
	c2_t00_mem0 += MM_MEM[0]
	S += 52 < c2_t00_mem0
	S += c2_t00_mem0 <= c2_t00

	c2_t00_mem1 = S.Task('c2_t00_mem1', length=1, delay_cost=1)
	c2_t00_mem1 += MM_MEM[1]
	S += 59 < c2_t00_mem1
	S += c2_t00_mem1 <= c2_t00

	c2_t0_t5 = S.Task('c2_t0_t5', length=3, delay_cost=1)
	c2_t0_t5 += alt(MAS)
	c2_t0_t5_in = S.Task('c2_t0_t5_in', length=1, delay_cost=1)
	c2_t0_t5_in += alt(MAS_in)
	S += c2_t0_t5_in*MAS_in[0]<=c2_t0_t5*MAS[0]

	S += c2_t0_t5_in*MAS_in[1]<=c2_t0_t5*MAS[1]

	S += c2_t0_t5_in*MAS_in[2]<=c2_t0_t5*MAS[2]

	S += c2_t0_t5_in*MAS_in[3]<=c2_t0_t5*MAS[3]

	c2_t0_t5_mem0 = S.Task('c2_t0_t5_mem0', length=1, delay_cost=1)
	c2_t0_t5_mem0 += MM_MEM[0]
	S += 52 < c2_t0_t5_mem0
	S += c2_t0_t5_mem0 <= c2_t0_t5

	c2_t0_t5_mem1 = S.Task('c2_t0_t5_mem1', length=1, delay_cost=1)
	c2_t0_t5_mem1 += MM_MEM[1]
	S += 59 < c2_t0_t5_mem1
	S += c2_t0_t5_mem1 <= c2_t0_t5

	c2_t1_t4 = S.Task('c2_t1_t4', length=14, delay_cost=1)
	c2_t1_t4 += alt(MM)
	c2_t1_t4_in = S.Task('c2_t1_t4_in', length=1, delay_cost=1)
	c2_t1_t4_in += alt(MM_in)
	S += c2_t1_t4_in*MM_in[0]<=c2_t1_t4*MM[0]
	c2_t1_t4_mem0 = S.Task('c2_t1_t4_mem0', length=1, delay_cost=1)
	c2_t1_t4_mem0 += MAS_MEM[4]
	S += 14 < c2_t1_t4_mem0
	S += c2_t1_t4_mem0 <= c2_t1_t4

	c2_t1_t4_mem1 = S.Task('c2_t1_t4_mem1', length=1, delay_cost=1)
	c2_t1_t4_mem1 += MAS_MEM[3]
	S += 43 < c2_t1_t4_mem1
	S += c2_t1_t4_mem1 <= c2_t1_t4

	c2_t10 = S.Task('c2_t10', length=3, delay_cost=1)
	c2_t10 += alt(MAS)
	c2_t10_in = S.Task('c2_t10_in', length=1, delay_cost=1)
	c2_t10_in += alt(MAS_in)
	S += c2_t10_in*MAS_in[0]<=c2_t10*MAS[0]

	S += c2_t10_in*MAS_in[1]<=c2_t10*MAS[1]

	S += c2_t10_in*MAS_in[2]<=c2_t10*MAS[2]

	S += c2_t10_in*MAS_in[3]<=c2_t10*MAS[3]

	c2_t10_mem0 = S.Task('c2_t10_mem0', length=1, delay_cost=1)
	c2_t10_mem0 += MM_MEM[0]
	S += 60 < c2_t10_mem0
	S += c2_t10_mem0 <= c2_t10

	c2_t10_mem1 = S.Task('c2_t10_mem1', length=1, delay_cost=1)
	c2_t10_mem1 += MM_MEM[1]
	S += 49 < c2_t10_mem1
	S += c2_t10_mem1 <= c2_t10

	c2_t1_t5 = S.Task('c2_t1_t5', length=3, delay_cost=1)
	c2_t1_t5 += alt(MAS)
	c2_t1_t5_in = S.Task('c2_t1_t5_in', length=1, delay_cost=1)
	c2_t1_t5_in += alt(MAS_in)
	S += c2_t1_t5_in*MAS_in[0]<=c2_t1_t5*MAS[0]

	S += c2_t1_t5_in*MAS_in[1]<=c2_t1_t5*MAS[1]

	S += c2_t1_t5_in*MAS_in[2]<=c2_t1_t5*MAS[2]

	S += c2_t1_t5_in*MAS_in[3]<=c2_t1_t5*MAS[3]

	c2_t1_t5_mem0 = S.Task('c2_t1_t5_mem0', length=1, delay_cost=1)
	c2_t1_t5_mem0 += MM_MEM[0]
	S += 49 < c2_t1_t5_mem0
	S += c2_t1_t5_mem0 <= c2_t1_t5

	c2_t1_t5_mem1 = S.Task('c2_t1_t5_mem1', length=1, delay_cost=1)
	c2_t1_t5_mem1 += MM_MEM[1]
	S += 60 < c2_t1_t5_mem1
	S += c2_t1_t5_mem1 <= c2_t1_t5

	c2_t4_t1 = S.Task('c2_t4_t1', length=14, delay_cost=1)
	c2_t4_t1 += alt(MM)
	c2_t4_t1_in = S.Task('c2_t4_t1_in', length=1, delay_cost=1)
	c2_t4_t1_in += alt(MM_in)
	S += c2_t4_t1_in*MM_in[0]<=c2_t4_t1*MM[0]
	c2_t4_t1_mem0 = S.Task('c2_t4_t1_mem0', length=1, delay_cost=1)
	c2_t4_t1_mem0 += MAS_MEM[2]
	S += 7 < c2_t4_t1_mem0
	S += c2_t4_t1_mem0 <= c2_t4_t1

	c2_t4_t1_mem1 = S.Task('c2_t4_t1_mem1', length=1, delay_cost=1)
	c2_t4_t1_mem1 += MAS_MEM[7]
	S += 45 < c2_t4_t1_mem1
	S += c2_t4_t1_mem1 <= c2_t4_t1

	c2_t4_t3 = S.Task('c2_t4_t3', length=3, delay_cost=1)
	c2_t4_t3 += alt(MAS)
	c2_t4_t3_in = S.Task('c2_t4_t3_in', length=1, delay_cost=1)
	c2_t4_t3_in += alt(MAS_in)
	S += c2_t4_t3_in*MAS_in[0]<=c2_t4_t3*MAS[0]

	S += c2_t4_t3_in*MAS_in[1]<=c2_t4_t3*MAS[1]

	S += c2_t4_t3_in*MAS_in[2]<=c2_t4_t3*MAS[2]

	S += c2_t4_t3_in*MAS_in[3]<=c2_t4_t3*MAS[3]

	c2_t4_t3_mem0 = S.Task('c2_t4_t3_mem0', length=1, delay_cost=1)
	c2_t4_t3_mem0 += MAS_MEM[6]
	S += 42 < c2_t4_t3_mem0
	S += c2_t4_t3_mem0 <= c2_t4_t3

	c2_t4_t3_mem1 = S.Task('c2_t4_t3_mem1', length=1, delay_cost=1)
	c2_t4_t3_mem1 += MAS_MEM[7]
	S += 45 < c2_t4_t3_mem1
	S += c2_t4_t3_mem1 <= c2_t4_t3

	c0_t01 = S.Task('c0_t01', length=3, delay_cost=1)
	c0_t01 += alt(MAS)
	c0_t01_in = S.Task('c0_t01_in', length=1, delay_cost=1)
	c0_t01_in += alt(MAS_in)
	S += c0_t01_in*MAS_in[0]<=c0_t01*MAS[0]

	S += c0_t01_in*MAS_in[1]<=c0_t01*MAS[1]

	S += c0_t01_in*MAS_in[2]<=c0_t01*MAS[2]

	S += c0_t01_in*MAS_in[3]<=c0_t01*MAS[3]

	c0_t01_mem0 = S.Task('c0_t01_mem0', length=1, delay_cost=1)
	c0_t01_mem0 += alt(MM_MEM)
	S += (c0_t0_t4*MM[0])-1 < c0_t01_mem0*MM_MEM[0]
	S += c0_t01_mem0 <= c0_t01

	c0_t01_mem1 = S.Task('c0_t01_mem1', length=1, delay_cost=1)
	c0_t01_mem1 += alt(MAS_MEM)
	S += (c0_t0_t5*MAS[0])-1 < c0_t01_mem1*MAS_MEM[1]
	S += (c0_t0_t5*MAS[1])-1 < c0_t01_mem1*MAS_MEM[3]
	S += (c0_t0_t5*MAS[2])-1 < c0_t01_mem1*MAS_MEM[5]
	S += (c0_t0_t5*MAS[3])-1 < c0_t01_mem1*MAS_MEM[7]
	S += c0_t01_mem1 <= c0_t01

	c0_t11 = S.Task('c0_t11', length=3, delay_cost=1)
	c0_t11 += alt(MAS)
	c0_t11_in = S.Task('c0_t11_in', length=1, delay_cost=1)
	c0_t11_in += alt(MAS_in)
	S += c0_t11_in*MAS_in[0]<=c0_t11*MAS[0]

	S += c0_t11_in*MAS_in[1]<=c0_t11*MAS[1]

	S += c0_t11_in*MAS_in[2]<=c0_t11*MAS[2]

	S += c0_t11_in*MAS_in[3]<=c0_t11*MAS[3]

	c0_t11_mem0 = S.Task('c0_t11_mem0', length=1, delay_cost=1)
	c0_t11_mem0 += alt(MM_MEM)
	S += (c0_t1_t4*MM[0])-1 < c0_t11_mem0*MM_MEM[0]
	S += c0_t11_mem0 <= c0_t11

	c0_t11_mem1 = S.Task('c0_t11_mem1', length=1, delay_cost=1)
	c0_t11_mem1 += alt(MAS_MEM)
	S += (c0_t1_t5*MAS[0])-1 < c0_t11_mem1*MAS_MEM[1]
	S += (c0_t1_t5*MAS[1])-1 < c0_t11_mem1*MAS_MEM[3]
	S += (c0_t1_t5*MAS[2])-1 < c0_t11_mem1*MAS_MEM[5]
	S += (c0_t1_t5*MAS[3])-1 < c0_t11_mem1*MAS_MEM[7]
	S += c0_t11_mem1 <= c0_t11

	c0_t4_t4 = S.Task('c0_t4_t4', length=14, delay_cost=1)
	c0_t4_t4 += alt(MM)
	c0_t4_t4_in = S.Task('c0_t4_t4_in', length=1, delay_cost=1)
	c0_t4_t4_in += alt(MM_in)
	S += c0_t4_t4_in*MM_in[0]<=c0_t4_t4*MM[0]
	c0_t4_t4_mem0 = S.Task('c0_t4_t4_mem0', length=1, delay_cost=1)
	c0_t4_t4_mem0 += MAS_MEM[2]
	S += 13 < c0_t4_t4_mem0
	S += c0_t4_t4_mem0 <= c0_t4_t4

	c0_t4_t4_mem1 = S.Task('c0_t4_t4_mem1', length=1, delay_cost=1)
	c0_t4_t4_mem1 += alt(MAS_MEM)
	S += (c0_t4_t3*MAS[0])-1 < c0_t4_t4_mem1*MAS_MEM[1]
	S += (c0_t4_t3*MAS[1])-1 < c0_t4_t4_mem1*MAS_MEM[3]
	S += (c0_t4_t3*MAS[2])-1 < c0_t4_t4_mem1*MAS_MEM[5]
	S += (c0_t4_t3*MAS[3])-1 < c0_t4_t4_mem1*MAS_MEM[7]
	S += c0_t4_t4_mem1 <= c0_t4_t4

	c0_t40 = S.Task('c0_t40', length=3, delay_cost=1)
	c0_t40 += alt(MAS)
	c0_t40_in = S.Task('c0_t40_in', length=1, delay_cost=1)
	c0_t40_in += alt(MAS_in)
	S += c0_t40_in*MAS_in[0]<=c0_t40*MAS[0]

	S += c0_t40_in*MAS_in[1]<=c0_t40*MAS[1]

	S += c0_t40_in*MAS_in[2]<=c0_t40*MAS[2]

	S += c0_t40_in*MAS_in[3]<=c0_t40*MAS[3]

	c0_t40_mem0 = S.Task('c0_t40_mem0', length=1, delay_cost=1)
	c0_t40_mem0 += MM_MEM[0]
	S += 55 < c0_t40_mem0
	S += c0_t40_mem0 <= c0_t40

	c0_t40_mem1 = S.Task('c0_t40_mem1', length=1, delay_cost=1)
	c0_t40_mem1 += alt(MM_MEM)
	S += (c0_t4_t1*MM[0])-1 < c0_t40_mem1*MM_MEM[1]
	S += c0_t40_mem1 <= c0_t40

	c0_t4_t5 = S.Task('c0_t4_t5', length=3, delay_cost=1)
	c0_t4_t5 += alt(MAS)
	c0_t4_t5_in = S.Task('c0_t4_t5_in', length=1, delay_cost=1)
	c0_t4_t5_in += alt(MAS_in)
	S += c0_t4_t5_in*MAS_in[0]<=c0_t4_t5*MAS[0]

	S += c0_t4_t5_in*MAS_in[1]<=c0_t4_t5*MAS[1]

	S += c0_t4_t5_in*MAS_in[2]<=c0_t4_t5*MAS[2]

	S += c0_t4_t5_in*MAS_in[3]<=c0_t4_t5*MAS[3]

	c0_t4_t5_mem0 = S.Task('c0_t4_t5_mem0', length=1, delay_cost=1)
	c0_t4_t5_mem0 += MM_MEM[0]
	S += 55 < c0_t4_t5_mem0
	S += c0_t4_t5_mem0 <= c0_t4_t5

	c0_t4_t5_mem1 = S.Task('c0_t4_t5_mem1', length=1, delay_cost=1)
	c0_t4_t5_mem1 += alt(MM_MEM)
	S += (c0_t4_t1*MM[0])-1 < c0_t4_t5_mem1*MM_MEM[1]
	S += c0_t4_t5_mem1 <= c0_t4_t5

	c0_t50 = S.Task('c0_t50', length=3, delay_cost=1)
	c0_t50 += alt(MAS)
	c0_t50_in = S.Task('c0_t50_in', length=1, delay_cost=1)
	c0_t50_in += alt(MAS_in)
	S += c0_t50_in*MAS_in[0]<=c0_t50*MAS[0]

	S += c0_t50_in*MAS_in[1]<=c0_t50*MAS[1]

	S += c0_t50_in*MAS_in[2]<=c0_t50*MAS[2]

	S += c0_t50_in*MAS_in[3]<=c0_t50*MAS[3]

	c0_t50_mem0 = S.Task('c0_t50_mem0', length=1, delay_cost=1)
	c0_t50_mem0 += alt(MAS_MEM)
	S += (c0_t00*MAS[0])-1 < c0_t50_mem0*MAS_MEM[0]
	S += (c0_t00*MAS[1])-1 < c0_t50_mem0*MAS_MEM[2]
	S += (c0_t00*MAS[2])-1 < c0_t50_mem0*MAS_MEM[4]
	S += (c0_t00*MAS[3])-1 < c0_t50_mem0*MAS_MEM[6]
	S += c0_t50_mem0 <= c0_t50

	c0_t50_mem1 = S.Task('c0_t50_mem1', length=1, delay_cost=1)
	c0_t50_mem1 += alt(MAS_MEM)
	S += (c0_t10*MAS[0])-1 < c0_t50_mem1*MAS_MEM[1]
	S += (c0_t10*MAS[1])-1 < c0_t50_mem1*MAS_MEM[3]
	S += (c0_t10*MAS[2])-1 < c0_t50_mem1*MAS_MEM[5]
	S += (c0_t10*MAS[3])-1 < c0_t50_mem1*MAS_MEM[7]
	S += c0_t50_mem1 <= c0_t50

	c1_t01 = S.Task('c1_t01', length=3, delay_cost=1)
	c1_t01 += alt(MAS)
	c1_t01_in = S.Task('c1_t01_in', length=1, delay_cost=1)
	c1_t01_in += alt(MAS_in)
	S += c1_t01_in*MAS_in[0]<=c1_t01*MAS[0]

	S += c1_t01_in*MAS_in[1]<=c1_t01*MAS[1]

	S += c1_t01_in*MAS_in[2]<=c1_t01*MAS[2]

	S += c1_t01_in*MAS_in[3]<=c1_t01*MAS[3]

	c1_t01_mem0 = S.Task('c1_t01_mem0', length=1, delay_cost=1)
	c1_t01_mem0 += alt(MM_MEM)
	S += (c1_t0_t4*MM[0])-1 < c1_t01_mem0*MM_MEM[0]
	S += c1_t01_mem0 <= c1_t01

	c1_t01_mem1 = S.Task('c1_t01_mem1', length=1, delay_cost=1)
	c1_t01_mem1 += alt(MAS_MEM)
	S += (c1_t0_t5*MAS[0])-1 < c1_t01_mem1*MAS_MEM[1]
	S += (c1_t0_t5*MAS[1])-1 < c1_t01_mem1*MAS_MEM[3]
	S += (c1_t0_t5*MAS[2])-1 < c1_t01_mem1*MAS_MEM[5]
	S += (c1_t0_t5*MAS[3])-1 < c1_t01_mem1*MAS_MEM[7]
	S += c1_t01_mem1 <= c1_t01

	c1_t11 = S.Task('c1_t11', length=3, delay_cost=1)
	c1_t11 += alt(MAS)
	c1_t11_in = S.Task('c1_t11_in', length=1, delay_cost=1)
	c1_t11_in += alt(MAS_in)
	S += c1_t11_in*MAS_in[0]<=c1_t11*MAS[0]

	S += c1_t11_in*MAS_in[1]<=c1_t11*MAS[1]

	S += c1_t11_in*MAS_in[2]<=c1_t11*MAS[2]

	S += c1_t11_in*MAS_in[3]<=c1_t11*MAS[3]

	c1_t11_mem0 = S.Task('c1_t11_mem0', length=1, delay_cost=1)
	c1_t11_mem0 += alt(MM_MEM)
	S += (c1_t1_t4*MM[0])-1 < c1_t11_mem0*MM_MEM[0]
	S += c1_t11_mem0 <= c1_t11

	c1_t11_mem1 = S.Task('c1_t11_mem1', length=1, delay_cost=1)
	c1_t11_mem1 += alt(MAS_MEM)
	S += (c1_t1_t5*MAS[0])-1 < c1_t11_mem1*MAS_MEM[1]
	S += (c1_t1_t5*MAS[1])-1 < c1_t11_mem1*MAS_MEM[3]
	S += (c1_t1_t5*MAS[2])-1 < c1_t11_mem1*MAS_MEM[5]
	S += (c1_t1_t5*MAS[3])-1 < c1_t11_mem1*MAS_MEM[7]
	S += c1_t11_mem1 <= c1_t11

	c1_t4_t4 = S.Task('c1_t4_t4', length=14, delay_cost=1)
	c1_t4_t4 += alt(MM)
	c1_t4_t4_in = S.Task('c1_t4_t4_in', length=1, delay_cost=1)
	c1_t4_t4_in += alt(MM_in)
	S += c1_t4_t4_in*MM_in[0]<=c1_t4_t4*MM[0]
	c1_t4_t4_mem0 = S.Task('c1_t4_t4_mem0', length=1, delay_cost=1)
	c1_t4_t4_mem0 += MAS_MEM[0]
	S += 9 < c1_t4_t4_mem0
	S += c1_t4_t4_mem0 <= c1_t4_t4

	c1_t4_t4_mem1 = S.Task('c1_t4_t4_mem1', length=1, delay_cost=1)
	c1_t4_t4_mem1 += alt(MAS_MEM)
	S += (c1_t4_t3*MAS[0])-1 < c1_t4_t4_mem1*MAS_MEM[1]
	S += (c1_t4_t3*MAS[1])-1 < c1_t4_t4_mem1*MAS_MEM[3]
	S += (c1_t4_t3*MAS[2])-1 < c1_t4_t4_mem1*MAS_MEM[5]
	S += (c1_t4_t3*MAS[3])-1 < c1_t4_t4_mem1*MAS_MEM[7]
	S += c1_t4_t4_mem1 <= c1_t4_t4

	c1_t40 = S.Task('c1_t40', length=3, delay_cost=1)
	c1_t40 += alt(MAS)
	c1_t40_in = S.Task('c1_t40_in', length=1, delay_cost=1)
	c1_t40_in += alt(MAS_in)
	S += c1_t40_in*MAS_in[0]<=c1_t40*MAS[0]

	S += c1_t40_in*MAS_in[1]<=c1_t40*MAS[1]

	S += c1_t40_in*MAS_in[2]<=c1_t40*MAS[2]

	S += c1_t40_in*MAS_in[3]<=c1_t40*MAS[3]

	c1_t40_mem0 = S.Task('c1_t40_mem0', length=1, delay_cost=1)
	c1_t40_mem0 += MM_MEM[0]
	S += 56 < c1_t40_mem0
	S += c1_t40_mem0 <= c1_t40

	c1_t40_mem1 = S.Task('c1_t40_mem1', length=1, delay_cost=1)
	c1_t40_mem1 += alt(MM_MEM)
	S += (c1_t4_t1*MM[0])-1 < c1_t40_mem1*MM_MEM[1]
	S += c1_t40_mem1 <= c1_t40

	c1_t4_t5 = S.Task('c1_t4_t5', length=3, delay_cost=1)
	c1_t4_t5 += alt(MAS)
	c1_t4_t5_in = S.Task('c1_t4_t5_in', length=1, delay_cost=1)
	c1_t4_t5_in += alt(MAS_in)
	S += c1_t4_t5_in*MAS_in[0]<=c1_t4_t5*MAS[0]

	S += c1_t4_t5_in*MAS_in[1]<=c1_t4_t5*MAS[1]

	S += c1_t4_t5_in*MAS_in[2]<=c1_t4_t5*MAS[2]

	S += c1_t4_t5_in*MAS_in[3]<=c1_t4_t5*MAS[3]

	c1_t4_t5_mem0 = S.Task('c1_t4_t5_mem0', length=1, delay_cost=1)
	c1_t4_t5_mem0 += MM_MEM[0]
	S += 56 < c1_t4_t5_mem0
	S += c1_t4_t5_mem0 <= c1_t4_t5

	c1_t4_t5_mem1 = S.Task('c1_t4_t5_mem1', length=1, delay_cost=1)
	c1_t4_t5_mem1 += alt(MM_MEM)
	S += (c1_t4_t1*MM[0])-1 < c1_t4_t5_mem1*MM_MEM[1]
	S += c1_t4_t5_mem1 <= c1_t4_t5

	c1_t50 = S.Task('c1_t50', length=3, delay_cost=1)
	c1_t50 += alt(MAS)
	c1_t50_in = S.Task('c1_t50_in', length=1, delay_cost=1)
	c1_t50_in += alt(MAS_in)
	S += c1_t50_in*MAS_in[0]<=c1_t50*MAS[0]

	S += c1_t50_in*MAS_in[1]<=c1_t50*MAS[1]

	S += c1_t50_in*MAS_in[2]<=c1_t50*MAS[2]

	S += c1_t50_in*MAS_in[3]<=c1_t50*MAS[3]

	c1_t50_mem0 = S.Task('c1_t50_mem0', length=1, delay_cost=1)
	c1_t50_mem0 += alt(MAS_MEM)
	S += (c1_t00*MAS[0])-1 < c1_t50_mem0*MAS_MEM[0]
	S += (c1_t00*MAS[1])-1 < c1_t50_mem0*MAS_MEM[2]
	S += (c1_t00*MAS[2])-1 < c1_t50_mem0*MAS_MEM[4]
	S += (c1_t00*MAS[3])-1 < c1_t50_mem0*MAS_MEM[6]
	S += c1_t50_mem0 <= c1_t50

	c1_t50_mem1 = S.Task('c1_t50_mem1', length=1, delay_cost=1)
	c1_t50_mem1 += alt(MAS_MEM)
	S += (c1_t10*MAS[0])-1 < c1_t50_mem1*MAS_MEM[1]
	S += (c1_t10*MAS[1])-1 < c1_t50_mem1*MAS_MEM[3]
	S += (c1_t10*MAS[2])-1 < c1_t50_mem1*MAS_MEM[5]
	S += (c1_t10*MAS[3])-1 < c1_t50_mem1*MAS_MEM[7]
	S += c1_t50_mem1 <= c1_t50

	c2_t01 = S.Task('c2_t01', length=3, delay_cost=1)
	c2_t01 += alt(MAS)
	c2_t01_in = S.Task('c2_t01_in', length=1, delay_cost=1)
	c2_t01_in += alt(MAS_in)
	S += c2_t01_in*MAS_in[0]<=c2_t01*MAS[0]

	S += c2_t01_in*MAS_in[1]<=c2_t01*MAS[1]

	S += c2_t01_in*MAS_in[2]<=c2_t01*MAS[2]

	S += c2_t01_in*MAS_in[3]<=c2_t01*MAS[3]

	c2_t01_mem0 = S.Task('c2_t01_mem0', length=1, delay_cost=1)
	c2_t01_mem0 += alt(MM_MEM)
	S += (c2_t0_t4*MM[0])-1 < c2_t01_mem0*MM_MEM[0]
	S += c2_t01_mem0 <= c2_t01

	c2_t01_mem1 = S.Task('c2_t01_mem1', length=1, delay_cost=1)
	c2_t01_mem1 += alt(MAS_MEM)
	S += (c2_t0_t5*MAS[0])-1 < c2_t01_mem1*MAS_MEM[1]
	S += (c2_t0_t5*MAS[1])-1 < c2_t01_mem1*MAS_MEM[3]
	S += (c2_t0_t5*MAS[2])-1 < c2_t01_mem1*MAS_MEM[5]
	S += (c2_t0_t5*MAS[3])-1 < c2_t01_mem1*MAS_MEM[7]
	S += c2_t01_mem1 <= c2_t01

	c2_t11 = S.Task('c2_t11', length=3, delay_cost=1)
	c2_t11 += alt(MAS)
	c2_t11_in = S.Task('c2_t11_in', length=1, delay_cost=1)
	c2_t11_in += alt(MAS_in)
	S += c2_t11_in*MAS_in[0]<=c2_t11*MAS[0]

	S += c2_t11_in*MAS_in[1]<=c2_t11*MAS[1]

	S += c2_t11_in*MAS_in[2]<=c2_t11*MAS[2]

	S += c2_t11_in*MAS_in[3]<=c2_t11*MAS[3]

	c2_t11_mem0 = S.Task('c2_t11_mem0', length=1, delay_cost=1)
	c2_t11_mem0 += alt(MM_MEM)
	S += (c2_t1_t4*MM[0])-1 < c2_t11_mem0*MM_MEM[0]
	S += c2_t11_mem0 <= c2_t11

	c2_t11_mem1 = S.Task('c2_t11_mem1', length=1, delay_cost=1)
	c2_t11_mem1 += alt(MAS_MEM)
	S += (c2_t1_t5*MAS[0])-1 < c2_t11_mem1*MAS_MEM[1]
	S += (c2_t1_t5*MAS[1])-1 < c2_t11_mem1*MAS_MEM[3]
	S += (c2_t1_t5*MAS[2])-1 < c2_t11_mem1*MAS_MEM[5]
	S += (c2_t1_t5*MAS[3])-1 < c2_t11_mem1*MAS_MEM[7]
	S += c2_t11_mem1 <= c2_t11

	c2_t4_t4 = S.Task('c2_t4_t4', length=14, delay_cost=1)
	c2_t4_t4 += alt(MM)
	c2_t4_t4_in = S.Task('c2_t4_t4_in', length=1, delay_cost=1)
	c2_t4_t4_in += alt(MM_in)
	S += c2_t4_t4_in*MM_in[0]<=c2_t4_t4*MM[0]
	c2_t4_t4_mem0 = S.Task('c2_t4_t4_mem0', length=1, delay_cost=1)
	c2_t4_t4_mem0 += MAS_MEM[6]
	S += 11 < c2_t4_t4_mem0
	S += c2_t4_t4_mem0 <= c2_t4_t4

	c2_t4_t4_mem1 = S.Task('c2_t4_t4_mem1', length=1, delay_cost=1)
	c2_t4_t4_mem1 += alt(MAS_MEM)
	S += (c2_t4_t3*MAS[0])-1 < c2_t4_t4_mem1*MAS_MEM[1]
	S += (c2_t4_t3*MAS[1])-1 < c2_t4_t4_mem1*MAS_MEM[3]
	S += (c2_t4_t3*MAS[2])-1 < c2_t4_t4_mem1*MAS_MEM[5]
	S += (c2_t4_t3*MAS[3])-1 < c2_t4_t4_mem1*MAS_MEM[7]
	S += c2_t4_t4_mem1 <= c2_t4_t4

	c2_t40 = S.Task('c2_t40', length=3, delay_cost=1)
	c2_t40 += alt(MAS)
	c2_t40_in = S.Task('c2_t40_in', length=1, delay_cost=1)
	c2_t40_in += alt(MAS_in)
	S += c2_t40_in*MAS_in[0]<=c2_t40*MAS[0]

	S += c2_t40_in*MAS_in[1]<=c2_t40*MAS[1]

	S += c2_t40_in*MAS_in[2]<=c2_t40*MAS[2]

	S += c2_t40_in*MAS_in[3]<=c2_t40*MAS[3]

	c2_t40_mem0 = S.Task('c2_t40_mem0', length=1, delay_cost=1)
	c2_t40_mem0 += MM_MEM[0]
	S += 57 < c2_t40_mem0
	S += c2_t40_mem0 <= c2_t40

	c2_t40_mem1 = S.Task('c2_t40_mem1', length=1, delay_cost=1)
	c2_t40_mem1 += alt(MM_MEM)
	S += (c2_t4_t1*MM[0])-1 < c2_t40_mem1*MM_MEM[1]
	S += c2_t40_mem1 <= c2_t40

	c2_t4_t5 = S.Task('c2_t4_t5', length=3, delay_cost=1)
	c2_t4_t5 += alt(MAS)
	c2_t4_t5_in = S.Task('c2_t4_t5_in', length=1, delay_cost=1)
	c2_t4_t5_in += alt(MAS_in)
	S += c2_t4_t5_in*MAS_in[0]<=c2_t4_t5*MAS[0]

	S += c2_t4_t5_in*MAS_in[1]<=c2_t4_t5*MAS[1]

	S += c2_t4_t5_in*MAS_in[2]<=c2_t4_t5*MAS[2]

	S += c2_t4_t5_in*MAS_in[3]<=c2_t4_t5*MAS[3]

	c2_t4_t5_mem0 = S.Task('c2_t4_t5_mem0', length=1, delay_cost=1)
	c2_t4_t5_mem0 += MM_MEM[0]
	S += 57 < c2_t4_t5_mem0
	S += c2_t4_t5_mem0 <= c2_t4_t5

	c2_t4_t5_mem1 = S.Task('c2_t4_t5_mem1', length=1, delay_cost=1)
	c2_t4_t5_mem1 += alt(MM_MEM)
	S += (c2_t4_t1*MM[0])-1 < c2_t4_t5_mem1*MM_MEM[1]
	S += c2_t4_t5_mem1 <= c2_t4_t5

	c2_t50 = S.Task('c2_t50', length=3, delay_cost=1)
	c2_t50 += alt(MAS)
	c2_t50_in = S.Task('c2_t50_in', length=1, delay_cost=1)
	c2_t50_in += alt(MAS_in)
	S += c2_t50_in*MAS_in[0]<=c2_t50*MAS[0]

	S += c2_t50_in*MAS_in[1]<=c2_t50*MAS[1]

	S += c2_t50_in*MAS_in[2]<=c2_t50*MAS[2]

	S += c2_t50_in*MAS_in[3]<=c2_t50*MAS[3]

	c2_t50_mem0 = S.Task('c2_t50_mem0', length=1, delay_cost=1)
	c2_t50_mem0 += alt(MAS_MEM)
	S += (c2_t00*MAS[0])-1 < c2_t50_mem0*MAS_MEM[0]
	S += (c2_t00*MAS[1])-1 < c2_t50_mem0*MAS_MEM[2]
	S += (c2_t00*MAS[2])-1 < c2_t50_mem0*MAS_MEM[4]
	S += (c2_t00*MAS[3])-1 < c2_t50_mem0*MAS_MEM[6]
	S += c2_t50_mem0 <= c2_t50

	c2_t50_mem1 = S.Task('c2_t50_mem1', length=1, delay_cost=1)
	c2_t50_mem1 += alt(MAS_MEM)
	S += (c2_t10*MAS[0])-1 < c2_t50_mem1*MAS_MEM[1]
	S += (c2_t10*MAS[1])-1 < c2_t50_mem1*MAS_MEM[3]
	S += (c2_t10*MAS[2])-1 < c2_t50_mem1*MAS_MEM[5]
	S += (c2_t10*MAS[3])-1 < c2_t50_mem1*MAS_MEM[7]
	S += c2_t50_mem1 <= c2_t50

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage14MM1_stage3MAS4/FP12_INV_AFTER_FPINV/schedule2.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

