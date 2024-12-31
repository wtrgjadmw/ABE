from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 142
	S = Scenario("schedule1", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=1, size=7)
	MM_in = S.Resources('MM_in', num=1)
	MAS_in = S.Resources('MAS_in', num=2)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=2, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=2)
	MAS_MEM = S.Resources('MAS_MEM', num=4)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling
	c_qinv_denom_inv0_in = S.Task('c_qinv_denom_inv0_in', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_in >= 0
	c_qinv_denom_inv0_in += MM_in[0]

	c_qinv_denom_inv0_mem0 = S.Task('c_qinv_denom_inv0_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem0 >= 0
	c_qinv_denom_inv0_mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv0_mem1 = S.Task('c_qinv_denom_inv0_mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem1 >= 0
	c_qinv_denom_inv0_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv0 = S.Task('c_qinv_denom_inv0', length=7, delay_cost=1)
	S += c_qinv_denom_inv0 >= 1
	c_qinv_denom_inv0 += MM[0]

	c_qinv_denom_inv1__in = S.Task('c_qinv_denom_inv1__in', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__in >= 1
	c_qinv_denom_inv1__in += MM_in[0]

	c_qinv_denom_inv1__mem0 = S.Task('c_qinv_denom_inv1__mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem0 >= 1
	c_qinv_denom_inv1__mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv1__mem1 = S.Task('c_qinv_denom_inv1__mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem1 >= 1
	c_qinv_denom_inv1__mem1 += MAIN_MEM_r[1]

	c0_t20_in = S.Task('c0_t20_in', length=1, delay_cost=1)
	S += c0_t20_in >= 2
	c0_t20_in += MAS_in[1]

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	S += c0_t20_mem0 >= 2
	c0_t20_mem0 += MAIN_MEM_r[0]

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	S += c0_t20_mem1 >= 2
	c0_t20_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv1_ = S.Task('c_qinv_denom_inv1_', length=7, delay_cost=1)
	S += c_qinv_denom_inv1_ >= 2
	c_qinv_denom_inv1_ += MM[0]

	c0_t20 = S.Task('c0_t20', length=2, delay_cost=1)
	S += c0_t20 >= 3
	c0_t20 += MAS[1]

	c0_t21_in = S.Task('c0_t21_in', length=1, delay_cost=1)
	S += c0_t21_in >= 3
	c0_t21_in += MAS_in[1]

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	S += c0_t21_mem0 >= 3
	c0_t21_mem0 += MAIN_MEM_r[0]

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	S += c0_t21_mem1 >= 3
	c0_t21_mem1 += MAIN_MEM_r[1]

	c0_t21 = S.Task('c0_t21', length=2, delay_cost=1)
	S += c0_t21 >= 4
	c0_t21 += MAS[1]

	c1_t21_in = S.Task('c1_t21_in', length=1, delay_cost=1)
	S += c1_t21_in >= 4
	c1_t21_in += MAS_in[0]

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	S += c1_t21_mem0 >= 4
	c1_t21_mem0 += MAIN_MEM_r[0]

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	S += c1_t21_mem1 >= 4
	c1_t21_mem1 += MAIN_MEM_r[1]

	c0_t4_t2_in = S.Task('c0_t4_t2_in', length=1, delay_cost=1)
	S += c0_t4_t2_in >= 5
	c0_t4_t2_in += MAS_in[1]

	c0_t4_t2_mem0 = S.Task('c0_t4_t2_mem0', length=1, delay_cost=1)
	S += c0_t4_t2_mem0 >= 5
	c0_t4_t2_mem0 += MAS_MEM[2]

	c0_t4_t2_mem1 = S.Task('c0_t4_t2_mem1', length=1, delay_cost=1)
	S += c0_t4_t2_mem1 >= 5
	c0_t4_t2_mem1 += MAS_MEM[3]

	c1_t20_in = S.Task('c1_t20_in', length=1, delay_cost=1)
	S += c1_t20_in >= 5
	c1_t20_in += MAS_in[0]

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	S += c1_t20_mem0 >= 5
	c1_t20_mem0 += MAIN_MEM_r[0]

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	S += c1_t20_mem1 >= 5
	c1_t20_mem1 += MAIN_MEM_r[1]

	c1_t21 = S.Task('c1_t21', length=2, delay_cost=1)
	S += c1_t21 >= 5
	c1_t21 += MAS[0]

	c0_t4_t2 = S.Task('c0_t4_t2', length=2, delay_cost=1)
	S += c0_t4_t2 >= 6
	c0_t4_t2 += MAS[1]

	c1_t20 = S.Task('c1_t20', length=2, delay_cost=1)
	S += c1_t20 >= 6
	c1_t20 += MAS[0]

	c2_t21_in = S.Task('c2_t21_in', length=1, delay_cost=1)
	S += c2_t21_in >= 6
	c2_t21_in += MAS_in[0]

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	S += c2_t21_mem0 >= 6
	c2_t21_mem0 += MAIN_MEM_r[0]

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	S += c2_t21_mem1 >= 6
	c2_t21_mem1 += MAIN_MEM_r[1]

	c1_t4_t2_in = S.Task('c1_t4_t2_in', length=1, delay_cost=1)
	S += c1_t4_t2_in >= 7
	c1_t4_t2_in += MAS_in[1]

	c1_t4_t2_mem0 = S.Task('c1_t4_t2_mem0', length=1, delay_cost=1)
	S += c1_t4_t2_mem0 >= 7
	c1_t4_t2_mem0 += MAS_MEM[0]

	c1_t4_t2_mem1 = S.Task('c1_t4_t2_mem1', length=1, delay_cost=1)
	S += c1_t4_t2_mem1 >= 7
	c1_t4_t2_mem1 += MAS_MEM[1]

	c2_t20_in = S.Task('c2_t20_in', length=1, delay_cost=1)
	S += c2_t20_in >= 7
	c2_t20_in += MAS_in[0]

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	S += c2_t20_mem0 >= 7
	c2_t20_mem0 += MAIN_MEM_r[0]

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	S += c2_t20_mem1 >= 7
	c2_t20_mem1 += MAIN_MEM_r[1]

	c2_t21 = S.Task('c2_t21', length=2, delay_cost=1)
	S += c2_t21 >= 7
	c2_t21 += MAS[0]

	c0_t0_t2_in = S.Task('c0_t0_t2_in', length=1, delay_cost=1)
	S += c0_t0_t2_in >= 8
	c0_t0_t2_in += MAS_in[1]

	c0_t0_t2_mem0 = S.Task('c0_t0_t2_mem0', length=1, delay_cost=1)
	S += c0_t0_t2_mem0 >= 8
	c0_t0_t2_mem0 += MAIN_MEM_r[0]

	c0_t0_t2_mem1 = S.Task('c0_t0_t2_mem1', length=1, delay_cost=1)
	S += c0_t0_t2_mem1 >= 8
	c0_t0_t2_mem1 += MAIN_MEM_r[1]

	c1_t4_t2 = S.Task('c1_t4_t2', length=2, delay_cost=1)
	S += c1_t4_t2 >= 8
	c1_t4_t2 += MAS[1]

	c2_t20 = S.Task('c2_t20', length=2, delay_cost=1)
	S += c2_t20 >= 8
	c2_t20 += MAS[0]

	c_qinv0_t3_in = S.Task('c_qinv0_t3_in', length=1, delay_cost=1)
	S += c_qinv0_t3_in >= 8
	c_qinv0_t3_in += MAS_in[0]

	c_qinv0_t3_mem0 = S.Task('c_qinv0_t3_mem0', length=1, delay_cost=1)
	S += c_qinv0_t3_mem0 >= 8
	c_qinv0_t3_mem0 += MM_MEM[0]

	c_qinv0_t3_mem1 = S.Task('c_qinv0_t3_mem1', length=1, delay_cost=1)
	S += c_qinv0_t3_mem1 >= 8
	c_qinv0_t3_mem1 += MM_MEM[1]

	c0_t0_t2 = S.Task('c0_t0_t2', length=2, delay_cost=1)
	S += c0_t0_t2 >= 9
	c0_t0_t2 += MAS[1]

	c2_t4_t2_in = S.Task('c2_t4_t2_in', length=1, delay_cost=1)
	S += c2_t4_t2_in >= 9
	c2_t4_t2_in += MAS_in[0]

	c2_t4_t2_mem0 = S.Task('c2_t4_t2_mem0', length=1, delay_cost=1)
	S += c2_t4_t2_mem0 >= 9
	c2_t4_t2_mem0 += MAS_MEM[0]

	c2_t4_t2_mem1 = S.Task('c2_t4_t2_mem1', length=1, delay_cost=1)
	S += c2_t4_t2_mem1 >= 9
	c2_t4_t2_mem1 += MAS_MEM[1]

	c_qinv0_t3 = S.Task('c_qinv0_t3', length=2, delay_cost=1)
	S += c_qinv0_t3 >= 9
	c_qinv0_t3 += MAS[0]

	c_qinv1__t0_in = S.Task('c_qinv1__t0_in', length=1, delay_cost=1)
	S += c_qinv1__t0_in >= 9
	c_qinv1__t0_in += MM_in[0]

	c_qinv1__t0_mem0 = S.Task('c_qinv1__t0_mem0', length=1, delay_cost=1)
	S += c_qinv1__t0_mem0 >= 9
	c_qinv1__t0_mem0 += MAIN_MEM_r[0]

	c_qinv1__t0_mem1 = S.Task('c_qinv1__t0_mem1', length=1, delay_cost=1)
	S += c_qinv1__t0_mem1 >= 9
	c_qinv1__t0_mem1 += MM_MEM[1]

	c1_t0_t2_in = S.Task('c1_t0_t2_in', length=1, delay_cost=1)
	S += c1_t0_t2_in >= 10
	c1_t0_t2_in += MAS_in[0]

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	S += c1_t0_t2_mem0 >= 10
	c1_t0_t2_mem0 += MAIN_MEM_r[0]

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	S += c1_t0_t2_mem1 >= 10
	c1_t0_t2_mem1 += MAIN_MEM_r[1]

	c2_t4_t2 = S.Task('c2_t4_t2', length=2, delay_cost=1)
	S += c2_t4_t2 >= 10
	c2_t4_t2 += MAS[0]

	c_qinv1__t0 = S.Task('c_qinv1__t0', length=7, delay_cost=1)
	S += c_qinv1__t0 >= 10
	c_qinv1__t0 += MM[0]

	c_qinv1__t3_in = S.Task('c_qinv1__t3_in', length=1, delay_cost=1)
	S += c_qinv1__t3_in >= 10
	c_qinv1__t3_in += MAS_in[1]

	c_qinv1__t3_mem0 = S.Task('c_qinv1__t3_mem0', length=1, delay_cost=1)
	S += c_qinv1__t3_mem0 >= 10
	c_qinv1__t3_mem0 += MM_MEM[0]

	c_qinv1__t3_mem1 = S.Task('c_qinv1__t3_mem1', length=1, delay_cost=1)
	S += c_qinv1__t3_mem1 >= 10
	c_qinv1__t3_mem1 += MM_MEM[1]

	c1_t0_t2 = S.Task('c1_t0_t2', length=2, delay_cost=1)
	S += c1_t0_t2 >= 11
	c1_t0_t2 += MAS[0]

	c2_t0_t2_in = S.Task('c2_t0_t2_in', length=1, delay_cost=1)
	S += c2_t0_t2_in >= 11
	c2_t0_t2_in += MAS_in[0]

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	S += c2_t0_t2_mem0 >= 11
	c2_t0_t2_mem0 += MAIN_MEM_r[0]

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	S += c2_t0_t2_mem1 >= 11
	c2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t3 = S.Task('c_qinv1__t3', length=2, delay_cost=1)
	S += c_qinv1__t3 >= 11
	c_qinv1__t3 += MAS[1]

	c2_t0_t2 = S.Task('c2_t0_t2', length=2, delay_cost=1)
	S += c2_t0_t2 >= 12
	c2_t0_t2 += MAS[0]

	c_qinv0_t2_in = S.Task('c_qinv0_t2_in', length=1, delay_cost=1)
	S += c_qinv0_t2_in >= 12
	c_qinv0_t2_in += MAS_in[1]

	c_qinv0_t2_mem0 = S.Task('c_qinv0_t2_mem0', length=1, delay_cost=1)
	S += c_qinv0_t2_mem0 >= 12
	c_qinv0_t2_mem0 += MAIN_MEM_r[0]

	c_qinv0_t2_mem1 = S.Task('c_qinv0_t2_mem1', length=1, delay_cost=1)
	S += c_qinv0_t2_mem1 >= 12
	c_qinv0_t2_mem1 += MAIN_MEM_r[1]

	c2_t1_t2_in = S.Task('c2_t1_t2_in', length=1, delay_cost=1)
	S += c2_t1_t2_in >= 13
	c2_t1_t2_in += MAS_in[0]

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	S += c2_t1_t2_mem0 >= 13
	c2_t1_t2_mem0 += MAIN_MEM_r[0]

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	S += c2_t1_t2_mem1 >= 13
	c2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t2 = S.Task('c_qinv0_t2', length=2, delay_cost=1)
	S += c_qinv0_t2 >= 13
	c_qinv0_t2 += MAS[1]

	c2_t1_t2 = S.Task('c2_t1_t2', length=2, delay_cost=1)
	S += c2_t1_t2 >= 14
	c2_t1_t2 += MAS[0]

	c_qinv0_t0_in = S.Task('c_qinv0_t0_in', length=1, delay_cost=1)
	S += c_qinv0_t0_in >= 14
	c_qinv0_t0_in += MM_in[0]

	c_qinv0_t0_mem0 = S.Task('c_qinv0_t0_mem0', length=1, delay_cost=1)
	S += c_qinv0_t0_mem0 >= 14
	c_qinv0_t0_mem0 += MAIN_MEM_r[0]

	c_qinv0_t0_mem1 = S.Task('c_qinv0_t0_mem1', length=1, delay_cost=1)
	S += c_qinv0_t0_mem1 >= 14
	c_qinv0_t0_mem1 += MM_MEM[1]

	c_qinv0_t0 = S.Task('c_qinv0_t0', length=7, delay_cost=1)
	S += c_qinv0_t0 >= 15
	c_qinv0_t0 += MM[0]

	c_qinv1__t1_in = S.Task('c_qinv1__t1_in', length=1, delay_cost=1)
	S += c_qinv1__t1_in >= 15
	c_qinv1__t1_in += MM_in[0]

	c_qinv1__t1_mem0 = S.Task('c_qinv1__t1_mem0', length=1, delay_cost=1)
	S += c_qinv1__t1_mem0 >= 15
	c_qinv1__t1_mem0 += MAIN_MEM_r[0]

	c_qinv1__t1_mem1 = S.Task('c_qinv1__t1_mem1', length=1, delay_cost=1)
	S += c_qinv1__t1_mem1 >= 15
	c_qinv1__t1_mem1 += MM_MEM[1]

	c1_t1_t2_in = S.Task('c1_t1_t2_in', length=1, delay_cost=1)
	S += c1_t1_t2_in >= 16
	c1_t1_t2_in += MAS_in[0]

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	S += c1_t1_t2_mem0 >= 16
	c1_t1_t2_mem0 += MAIN_MEM_r[0]

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	S += c1_t1_t2_mem1 >= 16
	c1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t1 = S.Task('c_qinv1__t1', length=7, delay_cost=1)
	S += c_qinv1__t1 >= 16
	c_qinv1__t1 += MM[0]

	c1_t1_t2 = S.Task('c1_t1_t2', length=2, delay_cost=1)
	S += c1_t1_t2 >= 17
	c1_t1_t2 += MAS[0]

	c_qinv0_t1_in = S.Task('c_qinv0_t1_in', length=1, delay_cost=1)
	S += c_qinv0_t1_in >= 17
	c_qinv0_t1_in += MM_in[0]

	c_qinv0_t1_mem0 = S.Task('c_qinv0_t1_mem0', length=1, delay_cost=1)
	S += c_qinv0_t1_mem0 >= 17
	c_qinv0_t1_mem0 += MAIN_MEM_r[0]

	c_qinv0_t1_mem1 = S.Task('c_qinv0_t1_mem1', length=1, delay_cost=1)
	S += c_qinv0_t1_mem1 >= 17
	c_qinv0_t1_mem1 += MM_MEM[1]

	c_qinv0_t1 = S.Task('c_qinv0_t1', length=7, delay_cost=1)
	S += c_qinv0_t1 >= 18
	c_qinv0_t1 += MM[0]

	c_qinv1__t2_in = S.Task('c_qinv1__t2_in', length=1, delay_cost=1)
	S += c_qinv1__t2_in >= 18
	c_qinv1__t2_in += MAS_in[1]

	c_qinv1__t2_mem0 = S.Task('c_qinv1__t2_mem0', length=1, delay_cost=1)
	S += c_qinv1__t2_mem0 >= 18
	c_qinv1__t2_mem0 += MAIN_MEM_r[0]

	c_qinv1__t2_mem1 = S.Task('c_qinv1__t2_mem1', length=1, delay_cost=1)
	S += c_qinv1__t2_mem1 >= 18
	c_qinv1__t2_mem1 += MAIN_MEM_r[1]

	c0_t1_t2_in = S.Task('c0_t1_t2_in', length=1, delay_cost=1)
	S += c0_t1_t2_in >= 19
	c0_t1_t2_in += MAS_in[0]

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	S += c0_t1_t2_mem0 >= 19
	c0_t1_t2_mem0 += MAIN_MEM_r[0]

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	S += c0_t1_t2_mem1 >= 19
	c0_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t2 = S.Task('c_qinv1__t2', length=2, delay_cost=1)
	S += c_qinv1__t2 >= 19
	c_qinv1__t2 += MAS[1]

	c0_t1_t2 = S.Task('c0_t1_t2', length=2, delay_cost=1)
	S += c0_t1_t2 >= 20
	c0_t1_t2 += MAS[0]


	# new tasks
	c_qinv0_t4 = S.Task('c_qinv0_t4', length=7, delay_cost=1)
	c_qinv0_t4 += alt(MM)
	c_qinv0_t4_in = S.Task('c_qinv0_t4_in', length=1, delay_cost=1)
	c_qinv0_t4_in += alt(MM_in)
	S += c_qinv0_t4_in*MM_in[0]<=c_qinv0_t4*MM[0]
	c_qinv0_t4_mem0 = S.Task('c_qinv0_t4_mem0', length=1, delay_cost=1)
	c_qinv0_t4_mem0 += MAS_MEM[2]
	S += 14 < c_qinv0_t4_mem0
	S += c_qinv0_t4_mem0 <= c_qinv0_t4

	c_qinv0_t4_mem1 = S.Task('c_qinv0_t4_mem1', length=1, delay_cost=1)
	c_qinv0_t4_mem1 += MAS_MEM[1]
	S += 10 < c_qinv0_t4_mem1
	S += c_qinv0_t4_mem1 <= c_qinv0_t4

	c_qinv00 = S.Task('c_qinv00', length=2, delay_cost=1)
	c_qinv00 += alt(MAS)
	c_qinv00_in = S.Task('c_qinv00_in', length=1, delay_cost=1)
	c_qinv00_in += alt(MAS_in)
	S += c_qinv00_in*MAS_in[0]<=c_qinv00*MAS[0]

	S += c_qinv00_in*MAS_in[1]<=c_qinv00*MAS[1]

	c_qinv00_mem0 = S.Task('c_qinv00_mem0', length=1, delay_cost=1)
	c_qinv00_mem0 += MM_MEM[0]
	S += 21 < c_qinv00_mem0
	S += c_qinv00_mem0 <= c_qinv00

	c_qinv00_mem1 = S.Task('c_qinv00_mem1', length=1, delay_cost=1)
	c_qinv00_mem1 += MM_MEM[1]
	S += 24 < c_qinv00_mem1
	S += c_qinv00_mem1 <= c_qinv00

	c_qinv0_t5 = S.Task('c_qinv0_t5', length=2, delay_cost=1)
	c_qinv0_t5 += alt(MAS)
	c_qinv0_t5_in = S.Task('c_qinv0_t5_in', length=1, delay_cost=1)
	c_qinv0_t5_in += alt(MAS_in)
	S += c_qinv0_t5_in*MAS_in[0]<=c_qinv0_t5*MAS[0]

	S += c_qinv0_t5_in*MAS_in[1]<=c_qinv0_t5*MAS[1]

	c_qinv0_t5_mem0 = S.Task('c_qinv0_t5_mem0', length=1, delay_cost=1)
	c_qinv0_t5_mem0 += MM_MEM[0]
	S += 21 < c_qinv0_t5_mem0
	S += c_qinv0_t5_mem0 <= c_qinv0_t5

	c_qinv0_t5_mem1 = S.Task('c_qinv0_t5_mem1', length=1, delay_cost=1)
	c_qinv0_t5_mem1 += MM_MEM[1]
	S += 24 < c_qinv0_t5_mem1
	S += c_qinv0_t5_mem1 <= c_qinv0_t5

	c_qinv1__t4 = S.Task('c_qinv1__t4', length=7, delay_cost=1)
	c_qinv1__t4 += alt(MM)
	c_qinv1__t4_in = S.Task('c_qinv1__t4_in', length=1, delay_cost=1)
	c_qinv1__t4_in += alt(MM_in)
	S += c_qinv1__t4_in*MM_in[0]<=c_qinv1__t4*MM[0]
	c_qinv1__t4_mem0 = S.Task('c_qinv1__t4_mem0', length=1, delay_cost=1)
	c_qinv1__t4_mem0 += MAS_MEM[2]
	S += 20 < c_qinv1__t4_mem0
	S += c_qinv1__t4_mem0 <= c_qinv1__t4

	c_qinv1__t4_mem1 = S.Task('c_qinv1__t4_mem1', length=1, delay_cost=1)
	c_qinv1__t4_mem1 += MAS_MEM[3]
	S += 12 < c_qinv1__t4_mem1
	S += c_qinv1__t4_mem1 <= c_qinv1__t4

	c_qinv1_0 = S.Task('c_qinv1_0', length=2, delay_cost=1)
	c_qinv1_0 += alt(MAS)
	c_qinv1_0_in = S.Task('c_qinv1_0_in', length=1, delay_cost=1)
	c_qinv1_0_in += alt(MAS_in)
	S += c_qinv1_0_in*MAS_in[0]<=c_qinv1_0*MAS[0]

	S += c_qinv1_0_in*MAS_in[1]<=c_qinv1_0*MAS[1]

	c_qinv1_0_mem0 = S.Task('c_qinv1_0_mem0', length=1, delay_cost=1)
	c_qinv1_0_mem0 += MM_MEM[0]
	S += 16 < c_qinv1_0_mem0
	S += c_qinv1_0_mem0 <= c_qinv1_0

	c_qinv1_0_mem1 = S.Task('c_qinv1_0_mem1', length=1, delay_cost=1)
	c_qinv1_0_mem1 += MM_MEM[1]
	S += 22 < c_qinv1_0_mem1
	S += c_qinv1_0_mem1 <= c_qinv1_0

	c_qinv1__t5 = S.Task('c_qinv1__t5', length=2, delay_cost=1)
	c_qinv1__t5 += alt(MAS)
	c_qinv1__t5_in = S.Task('c_qinv1__t5_in', length=1, delay_cost=1)
	c_qinv1__t5_in += alt(MAS_in)
	S += c_qinv1__t5_in*MAS_in[0]<=c_qinv1__t5*MAS[0]

	S += c_qinv1__t5_in*MAS_in[1]<=c_qinv1__t5*MAS[1]

	c_qinv1__t5_mem0 = S.Task('c_qinv1__t5_mem0', length=1, delay_cost=1)
	c_qinv1__t5_mem0 += MM_MEM[0]
	S += 16 < c_qinv1__t5_mem0
	S += c_qinv1__t5_mem0 <= c_qinv1__t5

	c_qinv1__t5_mem1 = S.Task('c_qinv1__t5_mem1', length=1, delay_cost=1)
	c_qinv1__t5_mem1 += MM_MEM[1]
	S += 22 < c_qinv1__t5_mem1
	S += c_qinv1__t5_mem1 <= c_qinv1__t5

	c_qinv01 = S.Task('c_qinv01', length=2, delay_cost=1)
	c_qinv01 += alt(MAS)
	c_qinv01_in = S.Task('c_qinv01_in', length=1, delay_cost=1)
	c_qinv01_in += alt(MAS_in)
	S += c_qinv01_in*MAS_in[0]<=c_qinv01*MAS[0]

	S += c_qinv01_in*MAS_in[1]<=c_qinv01*MAS[1]

	c_qinv01_mem0 = S.Task('c_qinv01_mem0', length=1, delay_cost=1)
	c_qinv01_mem0 += alt(MM_MEM)
	S += (c_qinv0_t4*MM[0])-1 < c_qinv01_mem0*MM_MEM[0]
	S += c_qinv01_mem0 <= c_qinv01

	c_qinv01_mem1 = S.Task('c_qinv01_mem1', length=1, delay_cost=1)
	c_qinv01_mem1 += alt(MAS_MEM)
	S += (c_qinv0_t5*MAS[0])-1 < c_qinv01_mem1*MAS_MEM[1]
	S += (c_qinv0_t5*MAS[1])-1 < c_qinv01_mem1*MAS_MEM[3]
	S += c_qinv01_mem1 <= c_qinv01

	c_qinv1_1 = S.Task('c_qinv1_1', length=2, delay_cost=1)
	c_qinv1_1 += alt(MAS)
	c_qinv1_1_in = S.Task('c_qinv1_1_in', length=1, delay_cost=1)
	c_qinv1_1_in += alt(MAS_in)
	S += c_qinv1_1_in*MAS_in[0]<=c_qinv1_1*MAS[0]

	S += c_qinv1_1_in*MAS_in[1]<=c_qinv1_1*MAS[1]

	c_qinv1_1_mem0 = S.Task('c_qinv1_1_mem0', length=1, delay_cost=1)
	c_qinv1_1_mem0 += alt(MM_MEM)
	S += (c_qinv1__t4*MM[0])-1 < c_qinv1_1_mem0*MM_MEM[0]
	S += c_qinv1_1_mem0 <= c_qinv1_1

	c_qinv1_1_mem1 = S.Task('c_qinv1_1_mem1', length=1, delay_cost=1)
	c_qinv1_1_mem1 += alt(MAS_MEM)
	S += (c_qinv1__t5*MAS[0])-1 < c_qinv1_1_mem1*MAS_MEM[1]
	S += (c_qinv1__t5*MAS[1])-1 < c_qinv1_1_mem1*MAS_MEM[3]
	S += c_qinv1_1_mem1 <= c_qinv1_1

	c0_t0_t0 = S.Task('c0_t0_t0', length=7, delay_cost=1)
	c0_t0_t0 += alt(MM)
	c0_t0_t0_in = S.Task('c0_t0_t0_in', length=1, delay_cost=1)
	c0_t0_t0_in += alt(MM_in)
	S += c0_t0_t0_in*MM_in[0]<=c0_t0_t0*MM[0]
	c0_t0_t0_mem0 = S.Task('c0_t0_t0_mem0', length=1, delay_cost=1)
	c0_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c0_t0_t0_mem0 <= c0_t0_t0

	c0_t0_t0_mem1 = S.Task('c0_t0_t0_mem1', length=1, delay_cost=1)
	c0_t0_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c0_t0_t0_mem1*MAS_MEM[1]
	S += (c_qinv00*MAS[1])-1 < c0_t0_t0_mem1*MAS_MEM[3]
	S += c0_t0_t0_mem1 <= c0_t0_t0

	c0_t1_t0 = S.Task('c0_t1_t0', length=7, delay_cost=1)
	c0_t1_t0 += alt(MM)
	c0_t1_t0_in = S.Task('c0_t1_t0_in', length=1, delay_cost=1)
	c0_t1_t0_in += alt(MM_in)
	S += c0_t1_t0_in*MM_in[0]<=c0_t1_t0*MM[0]
	c0_t1_t0_mem0 = S.Task('c0_t1_t0_mem0', length=1, delay_cost=1)
	c0_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c0_t1_t0_mem0 <= c0_t1_t0

	c0_t1_t0_mem1 = S.Task('c0_t1_t0_mem1', length=1, delay_cost=1)
	c0_t1_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c0_t1_t0_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c0_t1_t0_mem1*MAS_MEM[3]
	S += c0_t1_t0_mem1 <= c0_t1_t0

	c0_t30 = S.Task('c0_t30', length=2, delay_cost=1)
	c0_t30 += alt(MAS)
	c0_t30_in = S.Task('c0_t30_in', length=1, delay_cost=1)
	c0_t30_in += alt(MAS_in)
	S += c0_t30_in*MAS_in[0]<=c0_t30*MAS[0]

	S += c0_t30_in*MAS_in[1]<=c0_t30*MAS[1]

	c0_t30_mem0 = S.Task('c0_t30_mem0', length=1, delay_cost=1)
	c0_t30_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c0_t30_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c0_t30_mem0*MAS_MEM[2]
	S += c0_t30_mem0 <= c0_t30

	c0_t30_mem1 = S.Task('c0_t30_mem1', length=1, delay_cost=1)
	c0_t30_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c0_t30_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c0_t30_mem1*MAS_MEM[3]
	S += c0_t30_mem1 <= c0_t30

	c1_t0_t0 = S.Task('c1_t0_t0', length=7, delay_cost=1)
	c1_t0_t0 += alt(MM)
	c1_t0_t0_in = S.Task('c1_t0_t0_in', length=1, delay_cost=1)
	c1_t0_t0_in += alt(MM_in)
	S += c1_t0_t0_in*MM_in[0]<=c1_t0_t0*MM[0]
	c1_t0_t0_mem0 = S.Task('c1_t0_t0_mem0', length=1, delay_cost=1)
	c1_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c1_t0_t0_mem0 <= c1_t0_t0

	c1_t0_t0_mem1 = S.Task('c1_t0_t0_mem1', length=1, delay_cost=1)
	c1_t0_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c1_t0_t0_mem1*MAS_MEM[1]
	S += (c_qinv00*MAS[1])-1 < c1_t0_t0_mem1*MAS_MEM[3]
	S += c1_t0_t0_mem1 <= c1_t0_t0

	c1_t1_t0 = S.Task('c1_t1_t0', length=7, delay_cost=1)
	c1_t1_t0 += alt(MM)
	c1_t1_t0_in = S.Task('c1_t1_t0_in', length=1, delay_cost=1)
	c1_t1_t0_in += alt(MM_in)
	S += c1_t1_t0_in*MM_in[0]<=c1_t1_t0*MM[0]
	c1_t1_t0_mem0 = S.Task('c1_t1_t0_mem0', length=1, delay_cost=1)
	c1_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c1_t1_t0_mem0 <= c1_t1_t0

	c1_t1_t0_mem1 = S.Task('c1_t1_t0_mem1', length=1, delay_cost=1)
	c1_t1_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c1_t1_t0_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c1_t1_t0_mem1*MAS_MEM[3]
	S += c1_t1_t0_mem1 <= c1_t1_t0

	c1_t30 = S.Task('c1_t30', length=2, delay_cost=1)
	c1_t30 += alt(MAS)
	c1_t30_in = S.Task('c1_t30_in', length=1, delay_cost=1)
	c1_t30_in += alt(MAS_in)
	S += c1_t30_in*MAS_in[0]<=c1_t30*MAS[0]

	S += c1_t30_in*MAS_in[1]<=c1_t30*MAS[1]

	c1_t30_mem0 = S.Task('c1_t30_mem0', length=1, delay_cost=1)
	c1_t30_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c1_t30_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c1_t30_mem0*MAS_MEM[2]
	S += c1_t30_mem0 <= c1_t30

	c1_t30_mem1 = S.Task('c1_t30_mem1', length=1, delay_cost=1)
	c1_t30_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c1_t30_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c1_t30_mem1*MAS_MEM[3]
	S += c1_t30_mem1 <= c1_t30

	c2_t0_t0 = S.Task('c2_t0_t0', length=7, delay_cost=1)
	c2_t0_t0 += alt(MM)
	c2_t0_t0_in = S.Task('c2_t0_t0_in', length=1, delay_cost=1)
	c2_t0_t0_in += alt(MM_in)
	S += c2_t0_t0_in*MM_in[0]<=c2_t0_t0*MM[0]
	c2_t0_t0_mem0 = S.Task('c2_t0_t0_mem0', length=1, delay_cost=1)
	c2_t0_t0_mem0 += MAIN_MEM_r[0]
	S += c2_t0_t0_mem0 <= c2_t0_t0

	c2_t0_t0_mem1 = S.Task('c2_t0_t0_mem1', length=1, delay_cost=1)
	c2_t0_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c2_t0_t0_mem1*MAS_MEM[1]
	S += (c_qinv00*MAS[1])-1 < c2_t0_t0_mem1*MAS_MEM[3]
	S += c2_t0_t0_mem1 <= c2_t0_t0

	c2_t1_t0 = S.Task('c2_t1_t0', length=7, delay_cost=1)
	c2_t1_t0 += alt(MM)
	c2_t1_t0_in = S.Task('c2_t1_t0_in', length=1, delay_cost=1)
	c2_t1_t0_in += alt(MM_in)
	S += c2_t1_t0_in*MM_in[0]<=c2_t1_t0*MM[0]
	c2_t1_t0_mem0 = S.Task('c2_t1_t0_mem0', length=1, delay_cost=1)
	c2_t1_t0_mem0 += MAIN_MEM_r[0]
	S += c2_t1_t0_mem0 <= c2_t1_t0

	c2_t1_t0_mem1 = S.Task('c2_t1_t0_mem1', length=1, delay_cost=1)
	c2_t1_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c2_t1_t0_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c2_t1_t0_mem1*MAS_MEM[3]
	S += c2_t1_t0_mem1 <= c2_t1_t0

	c2_t30 = S.Task('c2_t30', length=2, delay_cost=1)
	c2_t30 += alt(MAS)
	c2_t30_in = S.Task('c2_t30_in', length=1, delay_cost=1)
	c2_t30_in += alt(MAS_in)
	S += c2_t30_in*MAS_in[0]<=c2_t30*MAS[0]

	S += c2_t30_in*MAS_in[1]<=c2_t30*MAS[1]

	c2_t30_mem0 = S.Task('c2_t30_mem0', length=1, delay_cost=1)
	c2_t30_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c2_t30_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c2_t30_mem0*MAS_MEM[2]
	S += c2_t30_mem0 <= c2_t30

	c2_t30_mem1 = S.Task('c2_t30_mem1', length=1, delay_cost=1)
	c2_t30_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c2_t30_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c2_t30_mem1*MAS_MEM[3]
	S += c2_t30_mem1 <= c2_t30

	c0_t0_t1 = S.Task('c0_t0_t1', length=7, delay_cost=1)
	c0_t0_t1 += alt(MM)
	c0_t0_t1_in = S.Task('c0_t0_t1_in', length=1, delay_cost=1)
	c0_t0_t1_in += alt(MM_in)
	S += c0_t0_t1_in*MM_in[0]<=c0_t0_t1*MM[0]
	c0_t0_t1_mem0 = S.Task('c0_t0_t1_mem0', length=1, delay_cost=1)
	c0_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c0_t0_t1_mem0 <= c0_t0_t1

	c0_t0_t1_mem1 = S.Task('c0_t0_t1_mem1', length=1, delay_cost=1)
	c0_t0_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c0_t0_t1_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c0_t0_t1_mem1*MAS_MEM[3]
	S += c0_t0_t1_mem1 <= c0_t0_t1

	c0_t0_t3 = S.Task('c0_t0_t3', length=2, delay_cost=1)
	c0_t0_t3 += alt(MAS)
	c0_t0_t3_in = S.Task('c0_t0_t3_in', length=1, delay_cost=1)
	c0_t0_t3_in += alt(MAS_in)
	S += c0_t0_t3_in*MAS_in[0]<=c0_t0_t3*MAS[0]

	S += c0_t0_t3_in*MAS_in[1]<=c0_t0_t3*MAS[1]

	c0_t0_t3_mem0 = S.Task('c0_t0_t3_mem0', length=1, delay_cost=1)
	c0_t0_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c0_t0_t3_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c0_t0_t3_mem0*MAS_MEM[2]
	S += c0_t0_t3_mem0 <= c0_t0_t3

	c0_t0_t3_mem1 = S.Task('c0_t0_t3_mem1', length=1, delay_cost=1)
	c0_t0_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c0_t0_t3_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c0_t0_t3_mem1*MAS_MEM[3]
	S += c0_t0_t3_mem1 <= c0_t0_t3

	c0_t1_t1 = S.Task('c0_t1_t1', length=7, delay_cost=1)
	c0_t1_t1 += alt(MM)
	c0_t1_t1_in = S.Task('c0_t1_t1_in', length=1, delay_cost=1)
	c0_t1_t1_in += alt(MM_in)
	S += c0_t1_t1_in*MM_in[0]<=c0_t1_t1*MM[0]
	c0_t1_t1_mem0 = S.Task('c0_t1_t1_mem0', length=1, delay_cost=1)
	c0_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c0_t1_t1_mem0 <= c0_t1_t1

	c0_t1_t1_mem1 = S.Task('c0_t1_t1_mem1', length=1, delay_cost=1)
	c0_t1_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c0_t1_t1_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c0_t1_t1_mem1*MAS_MEM[3]
	S += c0_t1_t1_mem1 <= c0_t1_t1

	c0_t1_t3 = S.Task('c0_t1_t3', length=2, delay_cost=1)
	c0_t1_t3 += alt(MAS)
	c0_t1_t3_in = S.Task('c0_t1_t3_in', length=1, delay_cost=1)
	c0_t1_t3_in += alt(MAS_in)
	S += c0_t1_t3_in*MAS_in[0]<=c0_t1_t3*MAS[0]

	S += c0_t1_t3_in*MAS_in[1]<=c0_t1_t3*MAS[1]

	c0_t1_t3_mem0 = S.Task('c0_t1_t3_mem0', length=1, delay_cost=1)
	c0_t1_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c0_t1_t3_mem0*MAS_MEM[0]
	S += (c_qinv1_0*MAS[1])-1 < c0_t1_t3_mem0*MAS_MEM[2]
	S += c0_t1_t3_mem0 <= c0_t1_t3

	c0_t1_t3_mem1 = S.Task('c0_t1_t3_mem1', length=1, delay_cost=1)
	c0_t1_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c0_t1_t3_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c0_t1_t3_mem1*MAS_MEM[3]
	S += c0_t1_t3_mem1 <= c0_t1_t3

	c0_t31 = S.Task('c0_t31', length=2, delay_cost=1)
	c0_t31 += alt(MAS)
	c0_t31_in = S.Task('c0_t31_in', length=1, delay_cost=1)
	c0_t31_in += alt(MAS_in)
	S += c0_t31_in*MAS_in[0]<=c0_t31*MAS[0]

	S += c0_t31_in*MAS_in[1]<=c0_t31*MAS[1]

	c0_t31_mem0 = S.Task('c0_t31_mem0', length=1, delay_cost=1)
	c0_t31_mem0 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c0_t31_mem0*MAS_MEM[0]
	S += (c_qinv01*MAS[1])-1 < c0_t31_mem0*MAS_MEM[2]
	S += c0_t31_mem0 <= c0_t31

	c0_t31_mem1 = S.Task('c0_t31_mem1', length=1, delay_cost=1)
	c0_t31_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c0_t31_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c0_t31_mem1*MAS_MEM[3]
	S += c0_t31_mem1 <= c0_t31

	c0_t4_t0 = S.Task('c0_t4_t0', length=7, delay_cost=1)
	c0_t4_t0 += alt(MM)
	c0_t4_t0_in = S.Task('c0_t4_t0_in', length=1, delay_cost=1)
	c0_t4_t0_in += alt(MM_in)
	S += c0_t4_t0_in*MM_in[0]<=c0_t4_t0*MM[0]
	c0_t4_t0_mem0 = S.Task('c0_t4_t0_mem0', length=1, delay_cost=1)
	c0_t4_t0_mem0 += MAS_MEM[2]
	S += 4 < c0_t4_t0_mem0
	S += c0_t4_t0_mem0 <= c0_t4_t0

	c0_t4_t0_mem1 = S.Task('c0_t4_t0_mem1', length=1, delay_cost=1)
	c0_t4_t0_mem1 += alt(MAS_MEM)
	S += (c0_t30*MAS[0])-1 < c0_t4_t0_mem1*MAS_MEM[1]
	S += (c0_t30*MAS[1])-1 < c0_t4_t0_mem1*MAS_MEM[3]
	S += c0_t4_t0_mem1 <= c0_t4_t0

	c1_t0_t1 = S.Task('c1_t0_t1', length=7, delay_cost=1)
	c1_t0_t1 += alt(MM)
	c1_t0_t1_in = S.Task('c1_t0_t1_in', length=1, delay_cost=1)
	c1_t0_t1_in += alt(MM_in)
	S += c1_t0_t1_in*MM_in[0]<=c1_t0_t1*MM[0]
	c1_t0_t1_mem0 = S.Task('c1_t0_t1_mem0', length=1, delay_cost=1)
	c1_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c1_t0_t1_mem0 <= c1_t0_t1

	c1_t0_t1_mem1 = S.Task('c1_t0_t1_mem1', length=1, delay_cost=1)
	c1_t0_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c1_t0_t1_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c1_t0_t1_mem1*MAS_MEM[3]
	S += c1_t0_t1_mem1 <= c1_t0_t1

	c1_t0_t3 = S.Task('c1_t0_t3', length=2, delay_cost=1)
	c1_t0_t3 += alt(MAS)
	c1_t0_t3_in = S.Task('c1_t0_t3_in', length=1, delay_cost=1)
	c1_t0_t3_in += alt(MAS_in)
	S += c1_t0_t3_in*MAS_in[0]<=c1_t0_t3*MAS[0]

	S += c1_t0_t3_in*MAS_in[1]<=c1_t0_t3*MAS[1]

	c1_t0_t3_mem0 = S.Task('c1_t0_t3_mem0', length=1, delay_cost=1)
	c1_t0_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c1_t0_t3_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c1_t0_t3_mem0*MAS_MEM[2]
	S += c1_t0_t3_mem0 <= c1_t0_t3

	c1_t0_t3_mem1 = S.Task('c1_t0_t3_mem1', length=1, delay_cost=1)
	c1_t0_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c1_t0_t3_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c1_t0_t3_mem1*MAS_MEM[3]
	S += c1_t0_t3_mem1 <= c1_t0_t3

	c1_t1_t1 = S.Task('c1_t1_t1', length=7, delay_cost=1)
	c1_t1_t1 += alt(MM)
	c1_t1_t1_in = S.Task('c1_t1_t1_in', length=1, delay_cost=1)
	c1_t1_t1_in += alt(MM_in)
	S += c1_t1_t1_in*MM_in[0]<=c1_t1_t1*MM[0]
	c1_t1_t1_mem0 = S.Task('c1_t1_t1_mem0', length=1, delay_cost=1)
	c1_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c1_t1_t1_mem0 <= c1_t1_t1

	c1_t1_t1_mem1 = S.Task('c1_t1_t1_mem1', length=1, delay_cost=1)
	c1_t1_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c1_t1_t1_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c1_t1_t1_mem1*MAS_MEM[3]
	S += c1_t1_t1_mem1 <= c1_t1_t1

	c1_t1_t3 = S.Task('c1_t1_t3', length=2, delay_cost=1)
	c1_t1_t3 += alt(MAS)
	c1_t1_t3_in = S.Task('c1_t1_t3_in', length=1, delay_cost=1)
	c1_t1_t3_in += alt(MAS_in)
	S += c1_t1_t3_in*MAS_in[0]<=c1_t1_t3*MAS[0]

	S += c1_t1_t3_in*MAS_in[1]<=c1_t1_t3*MAS[1]

	c1_t1_t3_mem0 = S.Task('c1_t1_t3_mem0', length=1, delay_cost=1)
	c1_t1_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c1_t1_t3_mem0*MAS_MEM[0]
	S += (c_qinv1_0*MAS[1])-1 < c1_t1_t3_mem0*MAS_MEM[2]
	S += c1_t1_t3_mem0 <= c1_t1_t3

	c1_t1_t3_mem1 = S.Task('c1_t1_t3_mem1', length=1, delay_cost=1)
	c1_t1_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c1_t1_t3_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c1_t1_t3_mem1*MAS_MEM[3]
	S += c1_t1_t3_mem1 <= c1_t1_t3

	c1_t31 = S.Task('c1_t31', length=2, delay_cost=1)
	c1_t31 += alt(MAS)
	c1_t31_in = S.Task('c1_t31_in', length=1, delay_cost=1)
	c1_t31_in += alt(MAS_in)
	S += c1_t31_in*MAS_in[0]<=c1_t31*MAS[0]

	S += c1_t31_in*MAS_in[1]<=c1_t31*MAS[1]

	c1_t31_mem0 = S.Task('c1_t31_mem0', length=1, delay_cost=1)
	c1_t31_mem0 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c1_t31_mem0*MAS_MEM[0]
	S += (c_qinv01*MAS[1])-1 < c1_t31_mem0*MAS_MEM[2]
	S += c1_t31_mem0 <= c1_t31

	c1_t31_mem1 = S.Task('c1_t31_mem1', length=1, delay_cost=1)
	c1_t31_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c1_t31_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c1_t31_mem1*MAS_MEM[3]
	S += c1_t31_mem1 <= c1_t31

	c1_t4_t0 = S.Task('c1_t4_t0', length=7, delay_cost=1)
	c1_t4_t0 += alt(MM)
	c1_t4_t0_in = S.Task('c1_t4_t0_in', length=1, delay_cost=1)
	c1_t4_t0_in += alt(MM_in)
	S += c1_t4_t0_in*MM_in[0]<=c1_t4_t0*MM[0]
	c1_t4_t0_mem0 = S.Task('c1_t4_t0_mem0', length=1, delay_cost=1)
	c1_t4_t0_mem0 += MAS_MEM[0]
	S += 7 < c1_t4_t0_mem0
	S += c1_t4_t0_mem0 <= c1_t4_t0

	c1_t4_t0_mem1 = S.Task('c1_t4_t0_mem1', length=1, delay_cost=1)
	c1_t4_t0_mem1 += alt(MAS_MEM)
	S += (c1_t30*MAS[0])-1 < c1_t4_t0_mem1*MAS_MEM[1]
	S += (c1_t30*MAS[1])-1 < c1_t4_t0_mem1*MAS_MEM[3]
	S += c1_t4_t0_mem1 <= c1_t4_t0

	c2_t0_t1 = S.Task('c2_t0_t1', length=7, delay_cost=1)
	c2_t0_t1 += alt(MM)
	c2_t0_t1_in = S.Task('c2_t0_t1_in', length=1, delay_cost=1)
	c2_t0_t1_in += alt(MM_in)
	S += c2_t0_t1_in*MM_in[0]<=c2_t0_t1*MM[0]
	c2_t0_t1_mem0 = S.Task('c2_t0_t1_mem0', length=1, delay_cost=1)
	c2_t0_t1_mem0 += MAIN_MEM_r[0]
	S += c2_t0_t1_mem0 <= c2_t0_t1

	c2_t0_t1_mem1 = S.Task('c2_t0_t1_mem1', length=1, delay_cost=1)
	c2_t0_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c2_t0_t1_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c2_t0_t1_mem1*MAS_MEM[3]
	S += c2_t0_t1_mem1 <= c2_t0_t1

	c2_t0_t3 = S.Task('c2_t0_t3', length=2, delay_cost=1)
	c2_t0_t3 += alt(MAS)
	c2_t0_t3_in = S.Task('c2_t0_t3_in', length=1, delay_cost=1)
	c2_t0_t3_in += alt(MAS_in)
	S += c2_t0_t3_in*MAS_in[0]<=c2_t0_t3*MAS[0]

	S += c2_t0_t3_in*MAS_in[1]<=c2_t0_t3*MAS[1]

	c2_t0_t3_mem0 = S.Task('c2_t0_t3_mem0', length=1, delay_cost=1)
	c2_t0_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c2_t0_t3_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c2_t0_t3_mem0*MAS_MEM[2]
	S += c2_t0_t3_mem0 <= c2_t0_t3

	c2_t0_t3_mem1 = S.Task('c2_t0_t3_mem1', length=1, delay_cost=1)
	c2_t0_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c2_t0_t3_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c2_t0_t3_mem1*MAS_MEM[3]
	S += c2_t0_t3_mem1 <= c2_t0_t3

	c2_t1_t1 = S.Task('c2_t1_t1', length=7, delay_cost=1)
	c2_t1_t1 += alt(MM)
	c2_t1_t1_in = S.Task('c2_t1_t1_in', length=1, delay_cost=1)
	c2_t1_t1_in += alt(MM_in)
	S += c2_t1_t1_in*MM_in[0]<=c2_t1_t1*MM[0]
	c2_t1_t1_mem0 = S.Task('c2_t1_t1_mem0', length=1, delay_cost=1)
	c2_t1_t1_mem0 += MAIN_MEM_r[0]
	S += c2_t1_t1_mem0 <= c2_t1_t1

	c2_t1_t1_mem1 = S.Task('c2_t1_t1_mem1', length=1, delay_cost=1)
	c2_t1_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c2_t1_t1_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c2_t1_t1_mem1*MAS_MEM[3]
	S += c2_t1_t1_mem1 <= c2_t1_t1

	c2_t1_t3 = S.Task('c2_t1_t3', length=2, delay_cost=1)
	c2_t1_t3 += alt(MAS)
	c2_t1_t3_in = S.Task('c2_t1_t3_in', length=1, delay_cost=1)
	c2_t1_t3_in += alt(MAS_in)
	S += c2_t1_t3_in*MAS_in[0]<=c2_t1_t3*MAS[0]

	S += c2_t1_t3_in*MAS_in[1]<=c2_t1_t3*MAS[1]

	c2_t1_t3_mem0 = S.Task('c2_t1_t3_mem0', length=1, delay_cost=1)
	c2_t1_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c2_t1_t3_mem0*MAS_MEM[0]
	S += (c_qinv1_0*MAS[1])-1 < c2_t1_t3_mem0*MAS_MEM[2]
	S += c2_t1_t3_mem0 <= c2_t1_t3

	c2_t1_t3_mem1 = S.Task('c2_t1_t3_mem1', length=1, delay_cost=1)
	c2_t1_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c2_t1_t3_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c2_t1_t3_mem1*MAS_MEM[3]
	S += c2_t1_t3_mem1 <= c2_t1_t3

	c2_t31 = S.Task('c2_t31', length=2, delay_cost=1)
	c2_t31 += alt(MAS)
	c2_t31_in = S.Task('c2_t31_in', length=1, delay_cost=1)
	c2_t31_in += alt(MAS_in)
	S += c2_t31_in*MAS_in[0]<=c2_t31*MAS[0]

	S += c2_t31_in*MAS_in[1]<=c2_t31*MAS[1]

	c2_t31_mem0 = S.Task('c2_t31_mem0', length=1, delay_cost=1)
	c2_t31_mem0 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c2_t31_mem0*MAS_MEM[0]
	S += (c_qinv01*MAS[1])-1 < c2_t31_mem0*MAS_MEM[2]
	S += c2_t31_mem0 <= c2_t31

	c2_t31_mem1 = S.Task('c2_t31_mem1', length=1, delay_cost=1)
	c2_t31_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c2_t31_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c2_t31_mem1*MAS_MEM[3]
	S += c2_t31_mem1 <= c2_t31

	c2_t4_t0 = S.Task('c2_t4_t0', length=7, delay_cost=1)
	c2_t4_t0 += alt(MM)
	c2_t4_t0_in = S.Task('c2_t4_t0_in', length=1, delay_cost=1)
	c2_t4_t0_in += alt(MM_in)
	S += c2_t4_t0_in*MM_in[0]<=c2_t4_t0*MM[0]
	c2_t4_t0_mem0 = S.Task('c2_t4_t0_mem0', length=1, delay_cost=1)
	c2_t4_t0_mem0 += MAS_MEM[0]
	S += 9 < c2_t4_t0_mem0
	S += c2_t4_t0_mem0 <= c2_t4_t0

	c2_t4_t0_mem1 = S.Task('c2_t4_t0_mem1', length=1, delay_cost=1)
	c2_t4_t0_mem1 += alt(MAS_MEM)
	S += (c2_t30*MAS[0])-1 < c2_t4_t0_mem1*MAS_MEM[1]
	S += (c2_t30*MAS[1])-1 < c2_t4_t0_mem1*MAS_MEM[3]
	S += c2_t4_t0_mem1 <= c2_t4_t0

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage7MM1_stage2MAS2/FP12_INV_AFTER_FPINV/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 3))

	return solution

