from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 110
	S = Scenario("schedule1", horizon=horizon)

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
	c0_t0_t2_mem0 = S.Task('c0_t0_t2_mem0', length=1, delay_cost=1)
	S += c0_t0_t2_mem0 >= 0
	c0_t0_t2_mem0 += MAIN_MEM_r[0]

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	S += c1_t1_t2_mem1 >= 0
	c1_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv_denom_inv1__in = S.Task('c_qinv_denom_inv1__in', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__in >= 0
	c_qinv_denom_inv1__in += MM_in[0]

	c0_t20 = S.Task('c0_t20', length=1, delay_cost=1)
	S += c0_t20 >= 1
	c0_t20 += MAS[3]

	c0_t21 = S.Task('c0_t21', length=1, delay_cost=1)
	S += c0_t21 >= 1
	c0_t21 += MAS[2]

	c0_t4_t2_mem0 = S.Task('c0_t4_t2_mem0', length=1, delay_cost=1)
	S += c0_t4_t2_mem0 >= 1
	c0_t4_t2_mem0 += MAS_MEM[6]

	c0_t4_t2_mem1 = S.Task('c0_t4_t2_mem1', length=1, delay_cost=1)
	S += c0_t4_t2_mem1 >= 1
	c0_t4_t2_mem1 += MAS_MEM[5]

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	S += c2_t1_t2_mem0 >= 1
	c2_t1_t2_mem0 += MAIN_MEM_r[0]

	c2_t20 = S.Task('c2_t20', length=1, delay_cost=1)
	S += c2_t20 >= 1
	c2_t20 += MAS[0]

	c2_t21 = S.Task('c2_t21', length=1, delay_cost=1)
	S += c2_t21 >= 1
	c2_t21 += MAS[1]

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	S += c2_t21_mem1 >= 1
	c2_t21_mem1 += MAIN_MEM_r[1]

	c2_t4_t2_mem0 = S.Task('c2_t4_t2_mem0', length=1, delay_cost=1)
	S += c2_t4_t2_mem0 >= 1
	c2_t4_t2_mem0 += MAS_MEM[0]

	c2_t4_t2_mem1 = S.Task('c2_t4_t2_mem1', length=1, delay_cost=1)
	S += c2_t4_t2_mem1 >= 1
	c2_t4_t2_mem1 += MAS_MEM[3]

	c_qinv_denom_inv0_in = S.Task('c_qinv_denom_inv0_in', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_in >= 1
	c_qinv_denom_inv0_in += MM_in[0]

	c_qinv_denom_inv1_ = S.Task('c_qinv_denom_inv1_', length=4, delay_cost=1)
	S += c_qinv_denom_inv1_ >= 1
	c_qinv_denom_inv1_ += MM[0]

	c0_t4_t2 = S.Task('c0_t4_t2', length=1, delay_cost=1)
	S += c0_t4_t2 >= 2
	c0_t4_t2 += MAS[1]

	c1_t20 = S.Task('c1_t20', length=1, delay_cost=1)
	S += c1_t20 >= 2
	c1_t20 += MAS[3]

	c1_t21 = S.Task('c1_t21', length=1, delay_cost=1)
	S += c1_t21 >= 2
	c1_t21 += MAS[0]

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	S += c1_t21_mem1 >= 2
	c1_t21_mem1 += MAIN_MEM_r[1]

	c1_t4_t2_mem0 = S.Task('c1_t4_t2_mem0', length=1, delay_cost=1)
	S += c1_t4_t2_mem0 >= 2
	c1_t4_t2_mem0 += MAS_MEM[6]

	c1_t4_t2_mem1 = S.Task('c1_t4_t2_mem1', length=1, delay_cost=1)
	S += c1_t4_t2_mem1 >= 2
	c1_t4_t2_mem1 += MAS_MEM[1]

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	S += c2_t21_mem0 >= 2
	c2_t21_mem0 += MAIN_MEM_r[0]

	c2_t4_t2 = S.Task('c2_t4_t2', length=1, delay_cost=1)
	S += c2_t4_t2 >= 2
	c2_t4_t2 += MAS[2]

	c_qinv_denom_inv0 = S.Task('c_qinv_denom_inv0', length=4, delay_cost=1)
	S += c_qinv_denom_inv0 >= 2
	c_qinv_denom_inv0 += MM[0]

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	S += c0_t20_mem0 >= 3
	c0_t20_mem0 += MAIN_MEM_r[0]

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	S += c0_t20_mem1 >= 3
	c0_t20_mem1 += MAIN_MEM_r[1]

	c1_t0_t2 = S.Task('c1_t0_t2', length=1, delay_cost=1)
	S += c1_t0_t2 >= 3
	c1_t0_t2 += MAS[2]

	c1_t4_t2 = S.Task('c1_t4_t2', length=1, delay_cost=1)
	S += c1_t4_t2 >= 3
	c1_t4_t2 += MAS[0]

	c2_t1_t2 = S.Task('c2_t1_t2', length=1, delay_cost=1)
	S += c2_t1_t2 >= 3
	c2_t1_t2 += MAS[1]

	c_qinv0_t2 = S.Task('c_qinv0_t2', length=1, delay_cost=1)
	S += c_qinv0_t2 >= 3
	c_qinv0_t2 += MAS[3]

	c0_t0_t2 = S.Task('c0_t0_t2', length=1, delay_cost=1)
	S += c0_t0_t2 >= 4
	c0_t0_t2 += MAS[3]

	c0_t1_t2 = S.Task('c0_t1_t2', length=1, delay_cost=1)
	S += c0_t1_t2 >= 4
	c0_t1_t2 += MAS[2]

	c1_t1_t2 = S.Task('c1_t1_t2', length=1, delay_cost=1)
	S += c1_t1_t2 >= 4
	c1_t1_t2 += MAS[1]

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	S += c1_t20_mem0 >= 4
	c1_t20_mem0 += MAIN_MEM_r[0]

	c_qinv0_t1_in = S.Task('c_qinv0_t1_in', length=1, delay_cost=1)
	S += c_qinv0_t1_in >= 4
	c_qinv0_t1_in += MM_in[0]

	c_qinv0_t1_mem1 = S.Task('c_qinv0_t1_mem1', length=1, delay_cost=1)
	S += c_qinv0_t1_mem1 >= 4
	c_qinv0_t1_mem1 += MM_MEM[1]

	c_qinv1__t2 = S.Task('c_qinv1__t2', length=1, delay_cost=1)
	S += c_qinv1__t2 >= 4
	c_qinv1__t2 += MAS[0]

	c_qinv_denom_inv1__mem1 = S.Task('c_qinv_denom_inv1__mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem1 >= 4
	c_qinv_denom_inv1__mem1 += MAIN_MEM_r[1]

	c2_t0_t2 = S.Task('c2_t0_t2', length=1, delay_cost=1)
	S += c2_t0_t2 >= 5
	c2_t0_t2 += MAS[2]

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	S += c2_t1_t2_mem1 >= 5
	c2_t1_t2_mem1 += MAIN_MEM_r[1]

	c_qinv0_t1 = S.Task('c_qinv0_t1', length=4, delay_cost=1)
	S += c_qinv0_t1 >= 5
	c_qinv0_t1 += MM[0]

	c_qinv0_t2_mem0 = S.Task('c_qinv0_t2_mem0', length=1, delay_cost=1)
	S += c_qinv0_t2_mem0 >= 5
	c_qinv0_t2_mem0 += MAIN_MEM_r[0]

	c_qinv1__t3_mem0 = S.Task('c_qinv1__t3_mem0', length=1, delay_cost=1)
	S += c_qinv1__t3_mem0 >= 5
	c_qinv1__t3_mem0 += MM_MEM[0]

	c_qinv1__t3_mem1 = S.Task('c_qinv1__t3_mem1', length=1, delay_cost=1)
	S += c_qinv1__t3_mem1 >= 5
	c_qinv1__t3_mem1 += MM_MEM[1]

	c_qinv0_t0_in = S.Task('c_qinv0_t0_in', length=1, delay_cost=1)
	S += c_qinv0_t0_in >= 6
	c_qinv0_t0_in += MM_in[0]

	c_qinv0_t0_mem1 = S.Task('c_qinv0_t0_mem1', length=1, delay_cost=1)
	S += c_qinv0_t0_mem1 >= 6
	c_qinv0_t0_mem1 += MM_MEM[1]

	c_qinv1__t2_mem1 = S.Task('c_qinv1__t2_mem1', length=1, delay_cost=1)
	S += c_qinv1__t2_mem1 >= 6
	c_qinv1__t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t3 = S.Task('c_qinv1__t3', length=1, delay_cost=1)
	S += c_qinv1__t3 >= 6
	c_qinv1__t3 += MAS[1]

	c_qinv_denom_inv0_mem0 = S.Task('c_qinv_denom_inv0_mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem0 >= 6
	c_qinv_denom_inv0_mem0 += MAIN_MEM_r[0]

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	S += c1_t20_mem1 >= 7
	c1_t20_mem1 += MAIN_MEM_r[1]

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	S += c2_t20_mem0 >= 7
	c2_t20_mem0 += MAIN_MEM_r[0]

	c_qinv0_t0 = S.Task('c_qinv0_t0', length=4, delay_cost=1)
	S += c_qinv0_t0 >= 7
	c_qinv0_t0 += MM[0]

	c_qinv1__t0_in = S.Task('c_qinv1__t0_in', length=1, delay_cost=1)
	S += c_qinv1__t0_in >= 7
	c_qinv1__t0_in += MM_in[0]

	c_qinv1__t0_mem1 = S.Task('c_qinv1__t0_mem1', length=1, delay_cost=1)
	S += c_qinv1__t0_mem1 >= 7
	c_qinv1__t0_mem1 += MM_MEM[1]

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	S += c0_t21_mem1 >= 8
	c0_t21_mem1 += MAIN_MEM_r[1]

	c_qinv0_t3_mem0 = S.Task('c_qinv0_t3_mem0', length=1, delay_cost=1)
	S += c_qinv0_t3_mem0 >= 8
	c_qinv0_t3_mem0 += MM_MEM[0]

	c_qinv0_t3_mem1 = S.Task('c_qinv0_t3_mem1', length=1, delay_cost=1)
	S += c_qinv0_t3_mem1 >= 8
	c_qinv0_t3_mem1 += MM_MEM[1]

	c_qinv1__t0 = S.Task('c_qinv1__t0', length=4, delay_cost=1)
	S += c_qinv1__t0 >= 8
	c_qinv1__t0 += MM[0]

	c_qinv1__t0_mem0 = S.Task('c_qinv1__t0_mem0', length=1, delay_cost=1)
	S += c_qinv1__t0_mem0 >= 8
	c_qinv1__t0_mem0 += MAIN_MEM_r[0]

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	S += c0_t1_t2_mem1 >= 9
	c0_t1_t2_mem1 += MAIN_MEM_r[1]

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	S += c1_t0_t2_mem0 >= 9
	c1_t0_t2_mem0 += MAIN_MEM_r[0]

	c_qinv0_t3 = S.Task('c_qinv0_t3', length=1, delay_cost=1)
	S += c_qinv0_t3 >= 9
	c_qinv0_t3 += MAS[2]

	c_qinv1__t1_in = S.Task('c_qinv1__t1_in', length=1, delay_cost=1)
	S += c_qinv1__t1_in >= 9
	c_qinv1__t1_in += MM_in[0]

	c_qinv1__t1_mem1 = S.Task('c_qinv1__t1_mem1', length=1, delay_cost=1)
	S += c_qinv1__t1_mem1 >= 9
	c_qinv1__t1_mem1 += MM_MEM[1]

	c_qinv0_t2_mem1 = S.Task('c_qinv0_t2_mem1', length=1, delay_cost=1)
	S += c_qinv0_t2_mem1 >= 10
	c_qinv0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t1 = S.Task('c_qinv1__t1', length=4, delay_cost=1)
	S += c_qinv1__t1 >= 10
	c_qinv1__t1 += MM[0]

	c_qinv1__t2_mem0 = S.Task('c_qinv1__t2_mem0', length=1, delay_cost=1)
	S += c_qinv1__t2_mem0 >= 10
	c_qinv1__t2_mem0 += MAIN_MEM_r[0]

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	S += c2_t0_t2_mem0 >= 11
	c2_t0_t2_mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv0_mem1 = S.Task('c_qinv_denom_inv0_mem1', length=1, delay_cost=1)
	S += c_qinv_denom_inv0_mem1 >= 11
	c_qinv_denom_inv0_mem1 += MAIN_MEM_r[1]

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	S += c0_t21_mem0 >= 12
	c0_t21_mem0 += MAIN_MEM_r[0]

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	S += c1_t0_t2_mem1 >= 12
	c1_t0_t2_mem1 += MAIN_MEM_r[1]

	c0_t0_t2_mem1 = S.Task('c0_t0_t2_mem1', length=1, delay_cost=1)
	S += c0_t0_t2_mem1 >= 13
	c0_t0_t2_mem1 += MAIN_MEM_r[1]

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	S += c0_t1_t2_mem0 >= 13
	c0_t1_t2_mem0 += MAIN_MEM_r[0]

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	S += c1_t1_t2_mem0 >= 14
	c1_t1_t2_mem0 += MAIN_MEM_r[0]

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	S += c2_t20_mem1 >= 14
	c2_t20_mem1 += MAIN_MEM_r[1]

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	S += c1_t21_mem0 >= 15
	c1_t21_mem0 += MAIN_MEM_r[0]

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	S += c2_t0_t2_mem1 >= 15
	c2_t0_t2_mem1 += MAIN_MEM_r[1]

	c_qinv1__t1_mem0 = S.Task('c_qinv1__t1_mem0', length=1, delay_cost=1)
	S += c_qinv1__t1_mem0 >= 16
	c_qinv1__t1_mem0 += MAIN_MEM_r[0]

	c_qinv0_t0_mem0 = S.Task('c_qinv0_t0_mem0', length=1, delay_cost=1)
	S += c_qinv0_t0_mem0 >= 17
	c_qinv0_t0_mem0 += MAIN_MEM_r[0]

	c_qinv0_t1_mem0 = S.Task('c_qinv0_t1_mem0', length=1, delay_cost=1)
	S += c_qinv0_t1_mem0 >= 18
	c_qinv0_t1_mem0 += MAIN_MEM_r[0]

	c_qinv_denom_inv1__mem0 = S.Task('c_qinv_denom_inv1__mem0', length=1, delay_cost=1)
	S += c_qinv_denom_inv1__mem0 >= 19
	c_qinv_denom_inv1__mem0 += MAIN_MEM_r[0]


	# new tasks
	c_qinv0_t4_in = S.Task('c_qinv0_t4_in', length=1, delay_cost=1)
	c_qinv0_t4_in += alt(MM_in)
	c_qinv0_t4 = S.Task('c_qinv0_t4', length=4, delay_cost=1)
	c_qinv0_t4 += alt(MM)
	S += c_qinv0_t4>=c_qinv0_t4_in

	c_qinv0_t4_mem0 = S.Task('c_qinv0_t4_mem0', length=1, delay_cost=1)
	c_qinv0_t4_mem0 += MAS_MEM[6]
	S += 3 < c_qinv0_t4_mem0
	S += c_qinv0_t4_mem0 <= c_qinv0_t4

	c_qinv0_t4_mem1 = S.Task('c_qinv0_t4_mem1', length=1, delay_cost=1)
	c_qinv0_t4_mem1 += MAS_MEM[5]
	S += 9 < c_qinv0_t4_mem1
	S += c_qinv0_t4_mem1 <= c_qinv0_t4

	c_qinv00 = S.Task('c_qinv00', length=1, delay_cost=1)
	c_qinv00 += alt(MAS)

	c_qinv00_mem0 = S.Task('c_qinv00_mem0', length=1, delay_cost=1)
	c_qinv00_mem0 += MM_MEM[0]
	S += 10 < c_qinv00_mem0
	S += c_qinv00_mem0 <= c_qinv00

	c_qinv00_mem1 = S.Task('c_qinv00_mem1', length=1, delay_cost=1)
	c_qinv00_mem1 += MM_MEM[1]
	S += 8 < c_qinv00_mem1
	S += c_qinv00_mem1 <= c_qinv00

	c_qinv0_t5 = S.Task('c_qinv0_t5', length=1, delay_cost=1)
	c_qinv0_t5 += alt(MAS)

	c_qinv0_t5_mem0 = S.Task('c_qinv0_t5_mem0', length=1, delay_cost=1)
	c_qinv0_t5_mem0 += MM_MEM[0]
	S += 10 < c_qinv0_t5_mem0
	S += c_qinv0_t5_mem0 <= c_qinv0_t5

	c_qinv0_t5_mem1 = S.Task('c_qinv0_t5_mem1', length=1, delay_cost=1)
	c_qinv0_t5_mem1 += MM_MEM[1]
	S += 8 < c_qinv0_t5_mem1
	S += c_qinv0_t5_mem1 <= c_qinv0_t5

	c_qinv1__t4_in = S.Task('c_qinv1__t4_in', length=1, delay_cost=1)
	c_qinv1__t4_in += alt(MM_in)
	c_qinv1__t4 = S.Task('c_qinv1__t4', length=4, delay_cost=1)
	c_qinv1__t4 += alt(MM)
	S += c_qinv1__t4>=c_qinv1__t4_in

	c_qinv1__t4_mem0 = S.Task('c_qinv1__t4_mem0', length=1, delay_cost=1)
	c_qinv1__t4_mem0 += MAS_MEM[0]
	S += 4 < c_qinv1__t4_mem0
	S += c_qinv1__t4_mem0 <= c_qinv1__t4

	c_qinv1__t4_mem1 = S.Task('c_qinv1__t4_mem1', length=1, delay_cost=1)
	c_qinv1__t4_mem1 += MAS_MEM[3]
	S += 6 < c_qinv1__t4_mem1
	S += c_qinv1__t4_mem1 <= c_qinv1__t4

	c_qinv1_0 = S.Task('c_qinv1_0', length=1, delay_cost=1)
	c_qinv1_0 += alt(MAS)

	c_qinv1_0_mem0 = S.Task('c_qinv1_0_mem0', length=1, delay_cost=1)
	c_qinv1_0_mem0 += MM_MEM[0]
	S += 11 < c_qinv1_0_mem0
	S += c_qinv1_0_mem0 <= c_qinv1_0

	c_qinv1_0_mem1 = S.Task('c_qinv1_0_mem1', length=1, delay_cost=1)
	c_qinv1_0_mem1 += MM_MEM[1]
	S += 13 < c_qinv1_0_mem1
	S += c_qinv1_0_mem1 <= c_qinv1_0

	c_qinv1__t5 = S.Task('c_qinv1__t5', length=1, delay_cost=1)
	c_qinv1__t5 += alt(MAS)

	c_qinv1__t5_mem0 = S.Task('c_qinv1__t5_mem0', length=1, delay_cost=1)
	c_qinv1__t5_mem0 += MM_MEM[0]
	S += 11 < c_qinv1__t5_mem0
	S += c_qinv1__t5_mem0 <= c_qinv1__t5

	c_qinv1__t5_mem1 = S.Task('c_qinv1__t5_mem1', length=1, delay_cost=1)
	c_qinv1__t5_mem1 += MM_MEM[1]
	S += 13 < c_qinv1__t5_mem1
	S += c_qinv1__t5_mem1 <= c_qinv1__t5

	c_qinv01 = S.Task('c_qinv01', length=1, delay_cost=1)
	c_qinv01 += alt(MAS)

	c_qinv01_mem0 = S.Task('c_qinv01_mem0', length=1, delay_cost=1)
	c_qinv01_mem0 += alt(MM_MEM)
	S += (c_qinv0_t4*MM[0])-1 < c_qinv01_mem0*MM_MEM[0]
	S += c_qinv01_mem0 <= c_qinv01

	c_qinv01_mem1 = S.Task('c_qinv01_mem1', length=1, delay_cost=1)
	c_qinv01_mem1 += alt(MAS_MEM)
	S += (c_qinv0_t5*MAS[0])-1 < c_qinv01_mem1*MAS_MEM[1]
	S += (c_qinv0_t5*MAS[1])-1 < c_qinv01_mem1*MAS_MEM[3]
	S += (c_qinv0_t5*MAS[2])-1 < c_qinv01_mem1*MAS_MEM[5]
	S += (c_qinv0_t5*MAS[3])-1 < c_qinv01_mem1*MAS_MEM[7]
	S += c_qinv01_mem1 <= c_qinv01

	c_qinv1_1 = S.Task('c_qinv1_1', length=1, delay_cost=1)
	c_qinv1_1 += alt(MAS)

	c_qinv1_1_mem0 = S.Task('c_qinv1_1_mem0', length=1, delay_cost=1)
	c_qinv1_1_mem0 += alt(MM_MEM)
	S += (c_qinv1__t4*MM[0])-1 < c_qinv1_1_mem0*MM_MEM[0]
	S += c_qinv1_1_mem0 <= c_qinv1_1

	c_qinv1_1_mem1 = S.Task('c_qinv1_1_mem1', length=1, delay_cost=1)
	c_qinv1_1_mem1 += alt(MAS_MEM)
	S += (c_qinv1__t5*MAS[0])-1 < c_qinv1_1_mem1*MAS_MEM[1]
	S += (c_qinv1__t5*MAS[1])-1 < c_qinv1_1_mem1*MAS_MEM[3]
	S += (c_qinv1__t5*MAS[2])-1 < c_qinv1_1_mem1*MAS_MEM[5]
	S += (c_qinv1__t5*MAS[3])-1 < c_qinv1_1_mem1*MAS_MEM[7]
	S += c_qinv1_1_mem1 <= c_qinv1_1

	c0_t0_t0_in = S.Task('c0_t0_t0_in', length=1, delay_cost=1)
	c0_t0_t0_in += alt(MM_in)
	c0_t0_t0 = S.Task('c0_t0_t0', length=4, delay_cost=1)
	c0_t0_t0 += alt(MM)
	S += c0_t0_t0>=c0_t0_t0_in

	c0_t0_t0_mem0 = S.Task('c0_t0_t0_mem0', length=1, delay_cost=1)
	c0_t0_t0_mem0 += MAIN_MEM_r[0]
	c0_t0_t0_mem1 = S.Task('c0_t0_t0_mem1', length=1, delay_cost=1)
	c0_t0_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c0_t0_t0_mem1*MAS_MEM[1]
	S += (c_qinv00*MAS[1])-1 < c0_t0_t0_mem1*MAS_MEM[3]
	S += (c_qinv00*MAS[2])-1 < c0_t0_t0_mem1*MAS_MEM[5]
	S += (c_qinv00*MAS[3])-1 < c0_t0_t0_mem1*MAS_MEM[7]
	S += c0_t0_t0_mem1 <= c0_t0_t0

	c0_t1_t0_in = S.Task('c0_t1_t0_in', length=1, delay_cost=1)
	c0_t1_t0_in += alt(MM_in)
	c0_t1_t0 = S.Task('c0_t1_t0', length=4, delay_cost=1)
	c0_t1_t0 += alt(MM)
	S += c0_t1_t0>=c0_t1_t0_in

	c0_t1_t0_mem0 = S.Task('c0_t1_t0_mem0', length=1, delay_cost=1)
	c0_t1_t0_mem0 += MAIN_MEM_r[0]
	c0_t1_t0_mem1 = S.Task('c0_t1_t0_mem1', length=1, delay_cost=1)
	c0_t1_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c0_t1_t0_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c0_t1_t0_mem1*MAS_MEM[3]
	S += (c_qinv1_0*MAS[2])-1 < c0_t1_t0_mem1*MAS_MEM[5]
	S += (c_qinv1_0*MAS[3])-1 < c0_t1_t0_mem1*MAS_MEM[7]
	S += c0_t1_t0_mem1 <= c0_t1_t0

	c0_t30 = S.Task('c0_t30', length=1, delay_cost=1)
	c0_t30 += alt(MAS)

	c0_t30_mem0 = S.Task('c0_t30_mem0', length=1, delay_cost=1)
	c0_t30_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c0_t30_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c0_t30_mem0*MAS_MEM[2]
	S += (c_qinv00*MAS[2])-1 < c0_t30_mem0*MAS_MEM[4]
	S += (c_qinv00*MAS[3])-1 < c0_t30_mem0*MAS_MEM[6]
	S += c0_t30_mem0 <= c0_t30

	c0_t30_mem1 = S.Task('c0_t30_mem1', length=1, delay_cost=1)
	c0_t30_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c0_t30_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c0_t30_mem1*MAS_MEM[3]
	S += (c_qinv1_0*MAS[2])-1 < c0_t30_mem1*MAS_MEM[5]
	S += (c_qinv1_0*MAS[3])-1 < c0_t30_mem1*MAS_MEM[7]
	S += c0_t30_mem1 <= c0_t30

	c1_t0_t0_in = S.Task('c1_t0_t0_in', length=1, delay_cost=1)
	c1_t0_t0_in += alt(MM_in)
	c1_t0_t0 = S.Task('c1_t0_t0', length=4, delay_cost=1)
	c1_t0_t0 += alt(MM)
	S += c1_t0_t0>=c1_t0_t0_in

	c1_t0_t0_mem0 = S.Task('c1_t0_t0_mem0', length=1, delay_cost=1)
	c1_t0_t0_mem0 += MAIN_MEM_r[0]
	c1_t0_t0_mem1 = S.Task('c1_t0_t0_mem1', length=1, delay_cost=1)
	c1_t0_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c1_t0_t0_mem1*MAS_MEM[1]
	S += (c_qinv00*MAS[1])-1 < c1_t0_t0_mem1*MAS_MEM[3]
	S += (c_qinv00*MAS[2])-1 < c1_t0_t0_mem1*MAS_MEM[5]
	S += (c_qinv00*MAS[3])-1 < c1_t0_t0_mem1*MAS_MEM[7]
	S += c1_t0_t0_mem1 <= c1_t0_t0

	c1_t1_t0_in = S.Task('c1_t1_t0_in', length=1, delay_cost=1)
	c1_t1_t0_in += alt(MM_in)
	c1_t1_t0 = S.Task('c1_t1_t0', length=4, delay_cost=1)
	c1_t1_t0 += alt(MM)
	S += c1_t1_t0>=c1_t1_t0_in

	c1_t1_t0_mem0 = S.Task('c1_t1_t0_mem0', length=1, delay_cost=1)
	c1_t1_t0_mem0 += MAIN_MEM_r[0]
	c1_t1_t0_mem1 = S.Task('c1_t1_t0_mem1', length=1, delay_cost=1)
	c1_t1_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c1_t1_t0_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c1_t1_t0_mem1*MAS_MEM[3]
	S += (c_qinv1_0*MAS[2])-1 < c1_t1_t0_mem1*MAS_MEM[5]
	S += (c_qinv1_0*MAS[3])-1 < c1_t1_t0_mem1*MAS_MEM[7]
	S += c1_t1_t0_mem1 <= c1_t1_t0

	c1_t30 = S.Task('c1_t30', length=1, delay_cost=1)
	c1_t30 += alt(MAS)

	c1_t30_mem0 = S.Task('c1_t30_mem0', length=1, delay_cost=1)
	c1_t30_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c1_t30_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c1_t30_mem0*MAS_MEM[2]
	S += (c_qinv00*MAS[2])-1 < c1_t30_mem0*MAS_MEM[4]
	S += (c_qinv00*MAS[3])-1 < c1_t30_mem0*MAS_MEM[6]
	S += c1_t30_mem0 <= c1_t30

	c1_t30_mem1 = S.Task('c1_t30_mem1', length=1, delay_cost=1)
	c1_t30_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c1_t30_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c1_t30_mem1*MAS_MEM[3]
	S += (c_qinv1_0*MAS[2])-1 < c1_t30_mem1*MAS_MEM[5]
	S += (c_qinv1_0*MAS[3])-1 < c1_t30_mem1*MAS_MEM[7]
	S += c1_t30_mem1 <= c1_t30

	c2_t0_t0_in = S.Task('c2_t0_t0_in', length=1, delay_cost=1)
	c2_t0_t0_in += alt(MM_in)
	c2_t0_t0 = S.Task('c2_t0_t0', length=4, delay_cost=1)
	c2_t0_t0 += alt(MM)
	S += c2_t0_t0>=c2_t0_t0_in

	c2_t0_t0_mem0 = S.Task('c2_t0_t0_mem0', length=1, delay_cost=1)
	c2_t0_t0_mem0 += MAIN_MEM_r[0]
	c2_t0_t0_mem1 = S.Task('c2_t0_t0_mem1', length=1, delay_cost=1)
	c2_t0_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c2_t0_t0_mem1*MAS_MEM[1]
	S += (c_qinv00*MAS[1])-1 < c2_t0_t0_mem1*MAS_MEM[3]
	S += (c_qinv00*MAS[2])-1 < c2_t0_t0_mem1*MAS_MEM[5]
	S += (c_qinv00*MAS[3])-1 < c2_t0_t0_mem1*MAS_MEM[7]
	S += c2_t0_t0_mem1 <= c2_t0_t0

	c2_t1_t0_in = S.Task('c2_t1_t0_in', length=1, delay_cost=1)
	c2_t1_t0_in += alt(MM_in)
	c2_t1_t0 = S.Task('c2_t1_t0', length=4, delay_cost=1)
	c2_t1_t0 += alt(MM)
	S += c2_t1_t0>=c2_t1_t0_in

	c2_t1_t0_mem0 = S.Task('c2_t1_t0_mem0', length=1, delay_cost=1)
	c2_t1_t0_mem0 += MAIN_MEM_r[0]
	c2_t1_t0_mem1 = S.Task('c2_t1_t0_mem1', length=1, delay_cost=1)
	c2_t1_t0_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c2_t1_t0_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c2_t1_t0_mem1*MAS_MEM[3]
	S += (c_qinv1_0*MAS[2])-1 < c2_t1_t0_mem1*MAS_MEM[5]
	S += (c_qinv1_0*MAS[3])-1 < c2_t1_t0_mem1*MAS_MEM[7]
	S += c2_t1_t0_mem1 <= c2_t1_t0

	c2_t30 = S.Task('c2_t30', length=1, delay_cost=1)
	c2_t30 += alt(MAS)

	c2_t30_mem0 = S.Task('c2_t30_mem0', length=1, delay_cost=1)
	c2_t30_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c2_t30_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c2_t30_mem0*MAS_MEM[2]
	S += (c_qinv00*MAS[2])-1 < c2_t30_mem0*MAS_MEM[4]
	S += (c_qinv00*MAS[3])-1 < c2_t30_mem0*MAS_MEM[6]
	S += c2_t30_mem0 <= c2_t30

	c2_t30_mem1 = S.Task('c2_t30_mem1', length=1, delay_cost=1)
	c2_t30_mem1 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c2_t30_mem1*MAS_MEM[1]
	S += (c_qinv1_0*MAS[1])-1 < c2_t30_mem1*MAS_MEM[3]
	S += (c_qinv1_0*MAS[2])-1 < c2_t30_mem1*MAS_MEM[5]
	S += (c_qinv1_0*MAS[3])-1 < c2_t30_mem1*MAS_MEM[7]
	S += c2_t30_mem1 <= c2_t30

	c0_t0_t1_in = S.Task('c0_t0_t1_in', length=1, delay_cost=1)
	c0_t0_t1_in += alt(MM_in)
	c0_t0_t1 = S.Task('c0_t0_t1', length=4, delay_cost=1)
	c0_t0_t1 += alt(MM)
	S += c0_t0_t1>=c0_t0_t1_in

	c0_t0_t1_mem0 = S.Task('c0_t0_t1_mem0', length=1, delay_cost=1)
	c0_t0_t1_mem0 += MAIN_MEM_r[0]
	c0_t0_t1_mem1 = S.Task('c0_t0_t1_mem1', length=1, delay_cost=1)
	c0_t0_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c0_t0_t1_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c0_t0_t1_mem1*MAS_MEM[3]
	S += (c_qinv01*MAS[2])-1 < c0_t0_t1_mem1*MAS_MEM[5]
	S += (c_qinv01*MAS[3])-1 < c0_t0_t1_mem1*MAS_MEM[7]
	S += c0_t0_t1_mem1 <= c0_t0_t1

	c0_t0_t3 = S.Task('c0_t0_t3', length=1, delay_cost=1)
	c0_t0_t3 += alt(MAS)

	c0_t0_t3_mem0 = S.Task('c0_t0_t3_mem0', length=1, delay_cost=1)
	c0_t0_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c0_t0_t3_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c0_t0_t3_mem0*MAS_MEM[2]
	S += (c_qinv00*MAS[2])-1 < c0_t0_t3_mem0*MAS_MEM[4]
	S += (c_qinv00*MAS[3])-1 < c0_t0_t3_mem0*MAS_MEM[6]
	S += c0_t0_t3_mem0 <= c0_t0_t3

	c0_t0_t3_mem1 = S.Task('c0_t0_t3_mem1', length=1, delay_cost=1)
	c0_t0_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c0_t0_t3_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c0_t0_t3_mem1*MAS_MEM[3]
	S += (c_qinv01*MAS[2])-1 < c0_t0_t3_mem1*MAS_MEM[5]
	S += (c_qinv01*MAS[3])-1 < c0_t0_t3_mem1*MAS_MEM[7]
	S += c0_t0_t3_mem1 <= c0_t0_t3

	c0_t1_t1_in = S.Task('c0_t1_t1_in', length=1, delay_cost=1)
	c0_t1_t1_in += alt(MM_in)
	c0_t1_t1 = S.Task('c0_t1_t1', length=4, delay_cost=1)
	c0_t1_t1 += alt(MM)
	S += c0_t1_t1>=c0_t1_t1_in

	c0_t1_t1_mem0 = S.Task('c0_t1_t1_mem0', length=1, delay_cost=1)
	c0_t1_t1_mem0 += MAIN_MEM_r[0]
	c0_t1_t1_mem1 = S.Task('c0_t1_t1_mem1', length=1, delay_cost=1)
	c0_t1_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c0_t1_t1_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c0_t1_t1_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c0_t1_t1_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c0_t1_t1_mem1*MAS_MEM[7]
	S += c0_t1_t1_mem1 <= c0_t1_t1

	c0_t1_t3 = S.Task('c0_t1_t3', length=1, delay_cost=1)
	c0_t1_t3 += alt(MAS)

	c0_t1_t3_mem0 = S.Task('c0_t1_t3_mem0', length=1, delay_cost=1)
	c0_t1_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c0_t1_t3_mem0*MAS_MEM[0]
	S += (c_qinv1_0*MAS[1])-1 < c0_t1_t3_mem0*MAS_MEM[2]
	S += (c_qinv1_0*MAS[2])-1 < c0_t1_t3_mem0*MAS_MEM[4]
	S += (c_qinv1_0*MAS[3])-1 < c0_t1_t3_mem0*MAS_MEM[6]
	S += c0_t1_t3_mem0 <= c0_t1_t3

	c0_t1_t3_mem1 = S.Task('c0_t1_t3_mem1', length=1, delay_cost=1)
	c0_t1_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c0_t1_t3_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c0_t1_t3_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c0_t1_t3_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c0_t1_t3_mem1*MAS_MEM[7]
	S += c0_t1_t3_mem1 <= c0_t1_t3

	c0_t31 = S.Task('c0_t31', length=1, delay_cost=1)
	c0_t31 += alt(MAS)

	c0_t31_mem0 = S.Task('c0_t31_mem0', length=1, delay_cost=1)
	c0_t31_mem0 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c0_t31_mem0*MAS_MEM[0]
	S += (c_qinv01*MAS[1])-1 < c0_t31_mem0*MAS_MEM[2]
	S += (c_qinv01*MAS[2])-1 < c0_t31_mem0*MAS_MEM[4]
	S += (c_qinv01*MAS[3])-1 < c0_t31_mem0*MAS_MEM[6]
	S += c0_t31_mem0 <= c0_t31

	c0_t31_mem1 = S.Task('c0_t31_mem1', length=1, delay_cost=1)
	c0_t31_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c0_t31_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c0_t31_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c0_t31_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c0_t31_mem1*MAS_MEM[7]
	S += c0_t31_mem1 <= c0_t31

	c0_t4_t0_in = S.Task('c0_t4_t0_in', length=1, delay_cost=1)
	c0_t4_t0_in += alt(MM_in)
	c0_t4_t0 = S.Task('c0_t4_t0', length=4, delay_cost=1)
	c0_t4_t0 += alt(MM)
	S += c0_t4_t0>=c0_t4_t0_in

	c0_t4_t0_mem0 = S.Task('c0_t4_t0_mem0', length=1, delay_cost=1)
	c0_t4_t0_mem0 += MAS_MEM[6]
	S += 1 < c0_t4_t0_mem0
	S += c0_t4_t0_mem0 <= c0_t4_t0

	c0_t4_t0_mem1 = S.Task('c0_t4_t0_mem1', length=1, delay_cost=1)
	c0_t4_t0_mem1 += alt(MAS_MEM)
	S += (c0_t30*MAS[0])-1 < c0_t4_t0_mem1*MAS_MEM[1]
	S += (c0_t30*MAS[1])-1 < c0_t4_t0_mem1*MAS_MEM[3]
	S += (c0_t30*MAS[2])-1 < c0_t4_t0_mem1*MAS_MEM[5]
	S += (c0_t30*MAS[3])-1 < c0_t4_t0_mem1*MAS_MEM[7]
	S += c0_t4_t0_mem1 <= c0_t4_t0

	c1_t0_t1_in = S.Task('c1_t0_t1_in', length=1, delay_cost=1)
	c1_t0_t1_in += alt(MM_in)
	c1_t0_t1 = S.Task('c1_t0_t1', length=4, delay_cost=1)
	c1_t0_t1 += alt(MM)
	S += c1_t0_t1>=c1_t0_t1_in

	c1_t0_t1_mem0 = S.Task('c1_t0_t1_mem0', length=1, delay_cost=1)
	c1_t0_t1_mem0 += MAIN_MEM_r[0]
	c1_t0_t1_mem1 = S.Task('c1_t0_t1_mem1', length=1, delay_cost=1)
	c1_t0_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c1_t0_t1_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c1_t0_t1_mem1*MAS_MEM[3]
	S += (c_qinv01*MAS[2])-1 < c1_t0_t1_mem1*MAS_MEM[5]
	S += (c_qinv01*MAS[3])-1 < c1_t0_t1_mem1*MAS_MEM[7]
	S += c1_t0_t1_mem1 <= c1_t0_t1

	c1_t0_t3 = S.Task('c1_t0_t3', length=1, delay_cost=1)
	c1_t0_t3 += alt(MAS)

	c1_t0_t3_mem0 = S.Task('c1_t0_t3_mem0', length=1, delay_cost=1)
	c1_t0_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c1_t0_t3_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c1_t0_t3_mem0*MAS_MEM[2]
	S += (c_qinv00*MAS[2])-1 < c1_t0_t3_mem0*MAS_MEM[4]
	S += (c_qinv00*MAS[3])-1 < c1_t0_t3_mem0*MAS_MEM[6]
	S += c1_t0_t3_mem0 <= c1_t0_t3

	c1_t0_t3_mem1 = S.Task('c1_t0_t3_mem1', length=1, delay_cost=1)
	c1_t0_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c1_t0_t3_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c1_t0_t3_mem1*MAS_MEM[3]
	S += (c_qinv01*MAS[2])-1 < c1_t0_t3_mem1*MAS_MEM[5]
	S += (c_qinv01*MAS[3])-1 < c1_t0_t3_mem1*MAS_MEM[7]
	S += c1_t0_t3_mem1 <= c1_t0_t3

	c1_t1_t1_in = S.Task('c1_t1_t1_in', length=1, delay_cost=1)
	c1_t1_t1_in += alt(MM_in)
	c1_t1_t1 = S.Task('c1_t1_t1', length=4, delay_cost=1)
	c1_t1_t1 += alt(MM)
	S += c1_t1_t1>=c1_t1_t1_in

	c1_t1_t1_mem0 = S.Task('c1_t1_t1_mem0', length=1, delay_cost=1)
	c1_t1_t1_mem0 += MAIN_MEM_r[0]
	c1_t1_t1_mem1 = S.Task('c1_t1_t1_mem1', length=1, delay_cost=1)
	c1_t1_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c1_t1_t1_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c1_t1_t1_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c1_t1_t1_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c1_t1_t1_mem1*MAS_MEM[7]
	S += c1_t1_t1_mem1 <= c1_t1_t1

	c1_t1_t3 = S.Task('c1_t1_t3', length=1, delay_cost=1)
	c1_t1_t3 += alt(MAS)

	c1_t1_t3_mem0 = S.Task('c1_t1_t3_mem0', length=1, delay_cost=1)
	c1_t1_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c1_t1_t3_mem0*MAS_MEM[0]
	S += (c_qinv1_0*MAS[1])-1 < c1_t1_t3_mem0*MAS_MEM[2]
	S += (c_qinv1_0*MAS[2])-1 < c1_t1_t3_mem0*MAS_MEM[4]
	S += (c_qinv1_0*MAS[3])-1 < c1_t1_t3_mem0*MAS_MEM[6]
	S += c1_t1_t3_mem0 <= c1_t1_t3

	c1_t1_t3_mem1 = S.Task('c1_t1_t3_mem1', length=1, delay_cost=1)
	c1_t1_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c1_t1_t3_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c1_t1_t3_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c1_t1_t3_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c1_t1_t3_mem1*MAS_MEM[7]
	S += c1_t1_t3_mem1 <= c1_t1_t3

	c1_t31 = S.Task('c1_t31', length=1, delay_cost=1)
	c1_t31 += alt(MAS)

	c1_t31_mem0 = S.Task('c1_t31_mem0', length=1, delay_cost=1)
	c1_t31_mem0 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c1_t31_mem0*MAS_MEM[0]
	S += (c_qinv01*MAS[1])-1 < c1_t31_mem0*MAS_MEM[2]
	S += (c_qinv01*MAS[2])-1 < c1_t31_mem0*MAS_MEM[4]
	S += (c_qinv01*MAS[3])-1 < c1_t31_mem0*MAS_MEM[6]
	S += c1_t31_mem0 <= c1_t31

	c1_t31_mem1 = S.Task('c1_t31_mem1', length=1, delay_cost=1)
	c1_t31_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c1_t31_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c1_t31_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c1_t31_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c1_t31_mem1*MAS_MEM[7]
	S += c1_t31_mem1 <= c1_t31

	c1_t4_t0_in = S.Task('c1_t4_t0_in', length=1, delay_cost=1)
	c1_t4_t0_in += alt(MM_in)
	c1_t4_t0 = S.Task('c1_t4_t0', length=4, delay_cost=1)
	c1_t4_t0 += alt(MM)
	S += c1_t4_t0>=c1_t4_t0_in

	c1_t4_t0_mem0 = S.Task('c1_t4_t0_mem0', length=1, delay_cost=1)
	c1_t4_t0_mem0 += MAS_MEM[6]
	S += 2 < c1_t4_t0_mem0
	S += c1_t4_t0_mem0 <= c1_t4_t0

	c1_t4_t0_mem1 = S.Task('c1_t4_t0_mem1', length=1, delay_cost=1)
	c1_t4_t0_mem1 += alt(MAS_MEM)
	S += (c1_t30*MAS[0])-1 < c1_t4_t0_mem1*MAS_MEM[1]
	S += (c1_t30*MAS[1])-1 < c1_t4_t0_mem1*MAS_MEM[3]
	S += (c1_t30*MAS[2])-1 < c1_t4_t0_mem1*MAS_MEM[5]
	S += (c1_t30*MAS[3])-1 < c1_t4_t0_mem1*MAS_MEM[7]
	S += c1_t4_t0_mem1 <= c1_t4_t0

	c2_t0_t1_in = S.Task('c2_t0_t1_in', length=1, delay_cost=1)
	c2_t0_t1_in += alt(MM_in)
	c2_t0_t1 = S.Task('c2_t0_t1', length=4, delay_cost=1)
	c2_t0_t1 += alt(MM)
	S += c2_t0_t1>=c2_t0_t1_in

	c2_t0_t1_mem0 = S.Task('c2_t0_t1_mem0', length=1, delay_cost=1)
	c2_t0_t1_mem0 += MAIN_MEM_r[0]
	c2_t0_t1_mem1 = S.Task('c2_t0_t1_mem1', length=1, delay_cost=1)
	c2_t0_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c2_t0_t1_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c2_t0_t1_mem1*MAS_MEM[3]
	S += (c_qinv01*MAS[2])-1 < c2_t0_t1_mem1*MAS_MEM[5]
	S += (c_qinv01*MAS[3])-1 < c2_t0_t1_mem1*MAS_MEM[7]
	S += c2_t0_t1_mem1 <= c2_t0_t1

	c2_t0_t3 = S.Task('c2_t0_t3', length=1, delay_cost=1)
	c2_t0_t3 += alt(MAS)

	c2_t0_t3_mem0 = S.Task('c2_t0_t3_mem0', length=1, delay_cost=1)
	c2_t0_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv00*MAS[0])-1 < c2_t0_t3_mem0*MAS_MEM[0]
	S += (c_qinv00*MAS[1])-1 < c2_t0_t3_mem0*MAS_MEM[2]
	S += (c_qinv00*MAS[2])-1 < c2_t0_t3_mem0*MAS_MEM[4]
	S += (c_qinv00*MAS[3])-1 < c2_t0_t3_mem0*MAS_MEM[6]
	S += c2_t0_t3_mem0 <= c2_t0_t3

	c2_t0_t3_mem1 = S.Task('c2_t0_t3_mem1', length=1, delay_cost=1)
	c2_t0_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c2_t0_t3_mem1*MAS_MEM[1]
	S += (c_qinv01*MAS[1])-1 < c2_t0_t3_mem1*MAS_MEM[3]
	S += (c_qinv01*MAS[2])-1 < c2_t0_t3_mem1*MAS_MEM[5]
	S += (c_qinv01*MAS[3])-1 < c2_t0_t3_mem1*MAS_MEM[7]
	S += c2_t0_t3_mem1 <= c2_t0_t3

	c2_t1_t1_in = S.Task('c2_t1_t1_in', length=1, delay_cost=1)
	c2_t1_t1_in += alt(MM_in)
	c2_t1_t1 = S.Task('c2_t1_t1', length=4, delay_cost=1)
	c2_t1_t1 += alt(MM)
	S += c2_t1_t1>=c2_t1_t1_in

	c2_t1_t1_mem0 = S.Task('c2_t1_t1_mem0', length=1, delay_cost=1)
	c2_t1_t1_mem0 += MAIN_MEM_r[0]
	c2_t1_t1_mem1 = S.Task('c2_t1_t1_mem1', length=1, delay_cost=1)
	c2_t1_t1_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c2_t1_t1_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c2_t1_t1_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c2_t1_t1_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c2_t1_t1_mem1*MAS_MEM[7]
	S += c2_t1_t1_mem1 <= c2_t1_t1

	c2_t1_t3 = S.Task('c2_t1_t3', length=1, delay_cost=1)
	c2_t1_t3 += alt(MAS)

	c2_t1_t3_mem0 = S.Task('c2_t1_t3_mem0', length=1, delay_cost=1)
	c2_t1_t3_mem0 += alt(MAS_MEM)
	S += (c_qinv1_0*MAS[0])-1 < c2_t1_t3_mem0*MAS_MEM[0]
	S += (c_qinv1_0*MAS[1])-1 < c2_t1_t3_mem0*MAS_MEM[2]
	S += (c_qinv1_0*MAS[2])-1 < c2_t1_t3_mem0*MAS_MEM[4]
	S += (c_qinv1_0*MAS[3])-1 < c2_t1_t3_mem0*MAS_MEM[6]
	S += c2_t1_t3_mem0 <= c2_t1_t3

	c2_t1_t3_mem1 = S.Task('c2_t1_t3_mem1', length=1, delay_cost=1)
	c2_t1_t3_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c2_t1_t3_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c2_t1_t3_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c2_t1_t3_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c2_t1_t3_mem1*MAS_MEM[7]
	S += c2_t1_t3_mem1 <= c2_t1_t3

	c2_t31 = S.Task('c2_t31', length=1, delay_cost=1)
	c2_t31 += alt(MAS)

	c2_t31_mem0 = S.Task('c2_t31_mem0', length=1, delay_cost=1)
	c2_t31_mem0 += alt(MAS_MEM)
	S += (c_qinv01*MAS[0])-1 < c2_t31_mem0*MAS_MEM[0]
	S += (c_qinv01*MAS[1])-1 < c2_t31_mem0*MAS_MEM[2]
	S += (c_qinv01*MAS[2])-1 < c2_t31_mem0*MAS_MEM[4]
	S += (c_qinv01*MAS[3])-1 < c2_t31_mem0*MAS_MEM[6]
	S += c2_t31_mem0 <= c2_t31

	c2_t31_mem1 = S.Task('c2_t31_mem1', length=1, delay_cost=1)
	c2_t31_mem1 += alt(MAS_MEM)
	S += (c_qinv1_1*MAS[0])-1 < c2_t31_mem1*MAS_MEM[1]
	S += (c_qinv1_1*MAS[1])-1 < c2_t31_mem1*MAS_MEM[3]
	S += (c_qinv1_1*MAS[2])-1 < c2_t31_mem1*MAS_MEM[5]
	S += (c_qinv1_1*MAS[3])-1 < c2_t31_mem1*MAS_MEM[7]
	S += c2_t31_mem1 <= c2_t31

	c2_t4_t0_in = S.Task('c2_t4_t0_in', length=1, delay_cost=1)
	c2_t4_t0_in += alt(MM_in)
	c2_t4_t0 = S.Task('c2_t4_t0', length=4, delay_cost=1)
	c2_t4_t0 += alt(MM)
	S += c2_t4_t0>=c2_t4_t0_in

	c2_t4_t0_mem0 = S.Task('c2_t4_t0_mem0', length=1, delay_cost=1)
	c2_t4_t0_mem0 += MAS_MEM[0]
	S += 1 < c2_t4_t0_mem0
	S += c2_t4_t0_mem0 <= c2_t4_t0

	c2_t4_t0_mem1 = S.Task('c2_t4_t0_mem1', length=1, delay_cost=1)
	c2_t4_t0_mem1 += alt(MAS_MEM)
	S += (c2_t30*MAS[0])-1 < c2_t4_t0_mem1*MAS_MEM[1]
	S += (c2_t30*MAS[1])-1 < c2_t4_t0_mem1*MAS_MEM[3]
	S += (c2_t30*MAS[2])-1 < c2_t4_t0_mem1*MAS_MEM[5]
	S += (c2_t30*MAS[3])-1 < c2_t4_t0_mem1*MAS_MEM[7]
	S += c2_t4_t0_mem1 <= c2_t4_t0

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/home/mfukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage4MM1_stage1MAS4/FP12_INV_AFTER_FPINV/schedule1.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 5))

	return solution

