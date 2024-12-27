from pyschedule import Scenario, solvers, plotters, alt


def solve():
	horizon = 120
	S = Scenario("schedule0", horizon=horizon)

	# resource
	MM = S.Resources('MM', num=2, size=10)
	MM_in = S.Resources('MM_in', num=2)
	MAS_in = S.Resources('MAS_in', num=6)
	CSEL = S.Resource('CSEL')
	MAS = S.Resources('MAS', num=6, size=2, periods=range(1, horizon))
	MM_MEM = S.Resources('MM_MEM', num=4)
	MAS_MEM = S.Resources('MAS_MEM', num=12)
	MAIN_MEM_w = S.Resource('MAIN_MEM_w', size=1)
	MAIN_MEM_r = S.Resources('MAIN_MEM_r', num=2)

	# result of previous scheduling

	# new tasks
	c_qinv_denom_inv0 = S.Task('c_qinv_denom_inv0', length=10, delay_cost=1)
	c_qinv_denom_inv0 += alt(MM)
	c_qinv_denom_inv0_in = S.Task('c_qinv_denom_inv0_in', length=1, delay_cost=1)
	c_qinv_denom_inv0_in += alt(MM_in)
	S += c_qinv_denom_inv0_in*MM_in[0]<=c_qinv_denom_inv0*MM[0]
	S += c_qinv_denom_inv0_in*MM_in[1]<=c_qinv_denom_inv0*MM[1]
	c_qinv_denom_inv0_mem0 = S.Task('c_qinv_denom_inv0_mem0', length=1, delay_cost=1)
	c_qinv_denom_inv0_mem0 += MAIN_MEM_r[0]
	S += c_qinv_denom_inv0_mem0 <= c_qinv_denom_inv0

	c_qinv_denom_inv0_mem1 = S.Task('c_qinv_denom_inv0_mem1', length=1, delay_cost=1)
	c_qinv_denom_inv0_mem1 += MAIN_MEM_r[1]
	S += c_qinv_denom_inv0_mem1 <= c_qinv_denom_inv0

	c_qinv_denom_inv1_ = S.Task('c_qinv_denom_inv1_', length=10, delay_cost=1)
	c_qinv_denom_inv1_ += alt(MM)
	c_qinv_denom_inv1__in = S.Task('c_qinv_denom_inv1__in', length=1, delay_cost=1)
	c_qinv_denom_inv1__in += alt(MM_in)
	S += c_qinv_denom_inv1__in*MM_in[0]<=c_qinv_denom_inv1_*MM[0]
	S += c_qinv_denom_inv1__in*MM_in[1]<=c_qinv_denom_inv1_*MM[1]
	c_qinv_denom_inv1__mem0 = S.Task('c_qinv_denom_inv1__mem0', length=1, delay_cost=1)
	c_qinv_denom_inv1__mem0 += MAIN_MEM_r[0]
	S += c_qinv_denom_inv1__mem0 <= c_qinv_denom_inv1_

	c_qinv_denom_inv1__mem1 = S.Task('c_qinv_denom_inv1__mem1', length=1, delay_cost=1)
	c_qinv_denom_inv1__mem1 += MAIN_MEM_r[1]
	S += c_qinv_denom_inv1__mem1 <= c_qinv_denom_inv1_

	c_qinv0_t2 = S.Task('c_qinv0_t2', length=2, delay_cost=1)
	c_qinv0_t2 += alt(MAS)
	c_qinv0_t2_in = S.Task('c_qinv0_t2_in', length=1, delay_cost=1)
	c_qinv0_t2_in += alt(MAS_in)
	S += c_qinv0_t2_in*MAS_in[0]<=c_qinv0_t2*MAS[0]

	S += c_qinv0_t2_in*MAS_in[1]<=c_qinv0_t2*MAS[1]

	S += c_qinv0_t2_in*MAS_in[2]<=c_qinv0_t2*MAS[2]

	S += c_qinv0_t2_in*MAS_in[3]<=c_qinv0_t2*MAS[3]

	S += c_qinv0_t2_in*MAS_in[4]<=c_qinv0_t2*MAS[4]

	S += c_qinv0_t2_in*MAS_in[5]<=c_qinv0_t2*MAS[5]

	c_qinv0_t2_mem0 = S.Task('c_qinv0_t2_mem0', length=1, delay_cost=1)
	c_qinv0_t2_mem0 += MAIN_MEM_r[0]
	S += c_qinv0_t2_mem0 <= c_qinv0_t2

	c_qinv0_t2_mem1 = S.Task('c_qinv0_t2_mem1', length=1, delay_cost=1)
	c_qinv0_t2_mem1 += MAIN_MEM_r[1]
	S += c_qinv0_t2_mem1 <= c_qinv0_t2

	c_qinv1__t2 = S.Task('c_qinv1__t2', length=2, delay_cost=1)
	c_qinv1__t2 += alt(MAS)
	c_qinv1__t2_in = S.Task('c_qinv1__t2_in', length=1, delay_cost=1)
	c_qinv1__t2_in += alt(MAS_in)
	S += c_qinv1__t2_in*MAS_in[0]<=c_qinv1__t2*MAS[0]

	S += c_qinv1__t2_in*MAS_in[1]<=c_qinv1__t2*MAS[1]

	S += c_qinv1__t2_in*MAS_in[2]<=c_qinv1__t2*MAS[2]

	S += c_qinv1__t2_in*MAS_in[3]<=c_qinv1__t2*MAS[3]

	S += c_qinv1__t2_in*MAS_in[4]<=c_qinv1__t2*MAS[4]

	S += c_qinv1__t2_in*MAS_in[5]<=c_qinv1__t2*MAS[5]

	c_qinv1__t2_mem0 = S.Task('c_qinv1__t2_mem0', length=1, delay_cost=1)
	c_qinv1__t2_mem0 += MAIN_MEM_r[0]
	S += c_qinv1__t2_mem0 <= c_qinv1__t2

	c_qinv1__t2_mem1 = S.Task('c_qinv1__t2_mem1', length=1, delay_cost=1)
	c_qinv1__t2_mem1 += MAIN_MEM_r[1]
	S += c_qinv1__t2_mem1 <= c_qinv1__t2

	c0_t0_t2 = S.Task('c0_t0_t2', length=2, delay_cost=1)
	c0_t0_t2 += alt(MAS)
	c0_t0_t2_in = S.Task('c0_t0_t2_in', length=1, delay_cost=1)
	c0_t0_t2_in += alt(MAS_in)
	S += c0_t0_t2_in*MAS_in[0]<=c0_t0_t2*MAS[0]

	S += c0_t0_t2_in*MAS_in[1]<=c0_t0_t2*MAS[1]

	S += c0_t0_t2_in*MAS_in[2]<=c0_t0_t2*MAS[2]

	S += c0_t0_t2_in*MAS_in[3]<=c0_t0_t2*MAS[3]

	S += c0_t0_t2_in*MAS_in[4]<=c0_t0_t2*MAS[4]

	S += c0_t0_t2_in*MAS_in[5]<=c0_t0_t2*MAS[5]

	c0_t0_t2_mem0 = S.Task('c0_t0_t2_mem0', length=1, delay_cost=1)
	c0_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c0_t0_t2_mem0 <= c0_t0_t2

	c0_t0_t2_mem1 = S.Task('c0_t0_t2_mem1', length=1, delay_cost=1)
	c0_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c0_t0_t2_mem1 <= c0_t0_t2

	c0_t1_t2 = S.Task('c0_t1_t2', length=2, delay_cost=1)
	c0_t1_t2 += alt(MAS)
	c0_t1_t2_in = S.Task('c0_t1_t2_in', length=1, delay_cost=1)
	c0_t1_t2_in += alt(MAS_in)
	S += c0_t1_t2_in*MAS_in[0]<=c0_t1_t2*MAS[0]

	S += c0_t1_t2_in*MAS_in[1]<=c0_t1_t2*MAS[1]

	S += c0_t1_t2_in*MAS_in[2]<=c0_t1_t2*MAS[2]

	S += c0_t1_t2_in*MAS_in[3]<=c0_t1_t2*MAS[3]

	S += c0_t1_t2_in*MAS_in[4]<=c0_t1_t2*MAS[4]

	S += c0_t1_t2_in*MAS_in[5]<=c0_t1_t2*MAS[5]

	c0_t1_t2_mem0 = S.Task('c0_t1_t2_mem0', length=1, delay_cost=1)
	c0_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c0_t1_t2_mem0 <= c0_t1_t2

	c0_t1_t2_mem1 = S.Task('c0_t1_t2_mem1', length=1, delay_cost=1)
	c0_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c0_t1_t2_mem1 <= c0_t1_t2

	c0_t20 = S.Task('c0_t20', length=2, delay_cost=1)
	c0_t20 += alt(MAS)
	c0_t20_in = S.Task('c0_t20_in', length=1, delay_cost=1)
	c0_t20_in += alt(MAS_in)
	S += c0_t20_in*MAS_in[0]<=c0_t20*MAS[0]

	S += c0_t20_in*MAS_in[1]<=c0_t20*MAS[1]

	S += c0_t20_in*MAS_in[2]<=c0_t20*MAS[2]

	S += c0_t20_in*MAS_in[3]<=c0_t20*MAS[3]

	S += c0_t20_in*MAS_in[4]<=c0_t20*MAS[4]

	S += c0_t20_in*MAS_in[5]<=c0_t20*MAS[5]

	c0_t20_mem0 = S.Task('c0_t20_mem0', length=1, delay_cost=1)
	c0_t20_mem0 += MAIN_MEM_r[0]
	S += c0_t20_mem0 <= c0_t20

	c0_t20_mem1 = S.Task('c0_t20_mem1', length=1, delay_cost=1)
	c0_t20_mem1 += MAIN_MEM_r[1]
	S += c0_t20_mem1 <= c0_t20

	c0_t21 = S.Task('c0_t21', length=2, delay_cost=1)
	c0_t21 += alt(MAS)
	c0_t21_in = S.Task('c0_t21_in', length=1, delay_cost=1)
	c0_t21_in += alt(MAS_in)
	S += c0_t21_in*MAS_in[0]<=c0_t21*MAS[0]

	S += c0_t21_in*MAS_in[1]<=c0_t21*MAS[1]

	S += c0_t21_in*MAS_in[2]<=c0_t21*MAS[2]

	S += c0_t21_in*MAS_in[3]<=c0_t21*MAS[3]

	S += c0_t21_in*MAS_in[4]<=c0_t21*MAS[4]

	S += c0_t21_in*MAS_in[5]<=c0_t21*MAS[5]

	c0_t21_mem0 = S.Task('c0_t21_mem0', length=1, delay_cost=1)
	c0_t21_mem0 += MAIN_MEM_r[0]
	S += c0_t21_mem0 <= c0_t21

	c0_t21_mem1 = S.Task('c0_t21_mem1', length=1, delay_cost=1)
	c0_t21_mem1 += MAIN_MEM_r[1]
	S += c0_t21_mem1 <= c0_t21

	c1_t0_t2 = S.Task('c1_t0_t2', length=2, delay_cost=1)
	c1_t0_t2 += alt(MAS)
	c1_t0_t2_in = S.Task('c1_t0_t2_in', length=1, delay_cost=1)
	c1_t0_t2_in += alt(MAS_in)
	S += c1_t0_t2_in*MAS_in[0]<=c1_t0_t2*MAS[0]

	S += c1_t0_t2_in*MAS_in[1]<=c1_t0_t2*MAS[1]

	S += c1_t0_t2_in*MAS_in[2]<=c1_t0_t2*MAS[2]

	S += c1_t0_t2_in*MAS_in[3]<=c1_t0_t2*MAS[3]

	S += c1_t0_t2_in*MAS_in[4]<=c1_t0_t2*MAS[4]

	S += c1_t0_t2_in*MAS_in[5]<=c1_t0_t2*MAS[5]

	c1_t0_t2_mem0 = S.Task('c1_t0_t2_mem0', length=1, delay_cost=1)
	c1_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c1_t0_t2_mem0 <= c1_t0_t2

	c1_t0_t2_mem1 = S.Task('c1_t0_t2_mem1', length=1, delay_cost=1)
	c1_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c1_t0_t2_mem1 <= c1_t0_t2

	c1_t1_t2 = S.Task('c1_t1_t2', length=2, delay_cost=1)
	c1_t1_t2 += alt(MAS)
	c1_t1_t2_in = S.Task('c1_t1_t2_in', length=1, delay_cost=1)
	c1_t1_t2_in += alt(MAS_in)
	S += c1_t1_t2_in*MAS_in[0]<=c1_t1_t2*MAS[0]

	S += c1_t1_t2_in*MAS_in[1]<=c1_t1_t2*MAS[1]

	S += c1_t1_t2_in*MAS_in[2]<=c1_t1_t2*MAS[2]

	S += c1_t1_t2_in*MAS_in[3]<=c1_t1_t2*MAS[3]

	S += c1_t1_t2_in*MAS_in[4]<=c1_t1_t2*MAS[4]

	S += c1_t1_t2_in*MAS_in[5]<=c1_t1_t2*MAS[5]

	c1_t1_t2_mem0 = S.Task('c1_t1_t2_mem0', length=1, delay_cost=1)
	c1_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c1_t1_t2_mem0 <= c1_t1_t2

	c1_t1_t2_mem1 = S.Task('c1_t1_t2_mem1', length=1, delay_cost=1)
	c1_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c1_t1_t2_mem1 <= c1_t1_t2

	c1_t20 = S.Task('c1_t20', length=2, delay_cost=1)
	c1_t20 += alt(MAS)
	c1_t20_in = S.Task('c1_t20_in', length=1, delay_cost=1)
	c1_t20_in += alt(MAS_in)
	S += c1_t20_in*MAS_in[0]<=c1_t20*MAS[0]

	S += c1_t20_in*MAS_in[1]<=c1_t20*MAS[1]

	S += c1_t20_in*MAS_in[2]<=c1_t20*MAS[2]

	S += c1_t20_in*MAS_in[3]<=c1_t20*MAS[3]

	S += c1_t20_in*MAS_in[4]<=c1_t20*MAS[4]

	S += c1_t20_in*MAS_in[5]<=c1_t20*MAS[5]

	c1_t20_mem0 = S.Task('c1_t20_mem0', length=1, delay_cost=1)
	c1_t20_mem0 += MAIN_MEM_r[0]
	S += c1_t20_mem0 <= c1_t20

	c1_t20_mem1 = S.Task('c1_t20_mem1', length=1, delay_cost=1)
	c1_t20_mem1 += MAIN_MEM_r[1]
	S += c1_t20_mem1 <= c1_t20

	c1_t21 = S.Task('c1_t21', length=2, delay_cost=1)
	c1_t21 += alt(MAS)
	c1_t21_in = S.Task('c1_t21_in', length=1, delay_cost=1)
	c1_t21_in += alt(MAS_in)
	S += c1_t21_in*MAS_in[0]<=c1_t21*MAS[0]

	S += c1_t21_in*MAS_in[1]<=c1_t21*MAS[1]

	S += c1_t21_in*MAS_in[2]<=c1_t21*MAS[2]

	S += c1_t21_in*MAS_in[3]<=c1_t21*MAS[3]

	S += c1_t21_in*MAS_in[4]<=c1_t21*MAS[4]

	S += c1_t21_in*MAS_in[5]<=c1_t21*MAS[5]

	c1_t21_mem0 = S.Task('c1_t21_mem0', length=1, delay_cost=1)
	c1_t21_mem0 += MAIN_MEM_r[0]
	S += c1_t21_mem0 <= c1_t21

	c1_t21_mem1 = S.Task('c1_t21_mem1', length=1, delay_cost=1)
	c1_t21_mem1 += MAIN_MEM_r[1]
	S += c1_t21_mem1 <= c1_t21

	c2_t0_t2 = S.Task('c2_t0_t2', length=2, delay_cost=1)
	c2_t0_t2 += alt(MAS)
	c2_t0_t2_in = S.Task('c2_t0_t2_in', length=1, delay_cost=1)
	c2_t0_t2_in += alt(MAS_in)
	S += c2_t0_t2_in*MAS_in[0]<=c2_t0_t2*MAS[0]

	S += c2_t0_t2_in*MAS_in[1]<=c2_t0_t2*MAS[1]

	S += c2_t0_t2_in*MAS_in[2]<=c2_t0_t2*MAS[2]

	S += c2_t0_t2_in*MAS_in[3]<=c2_t0_t2*MAS[3]

	S += c2_t0_t2_in*MAS_in[4]<=c2_t0_t2*MAS[4]

	S += c2_t0_t2_in*MAS_in[5]<=c2_t0_t2*MAS[5]

	c2_t0_t2_mem0 = S.Task('c2_t0_t2_mem0', length=1, delay_cost=1)
	c2_t0_t2_mem0 += MAIN_MEM_r[0]
	S += c2_t0_t2_mem0 <= c2_t0_t2

	c2_t0_t2_mem1 = S.Task('c2_t0_t2_mem1', length=1, delay_cost=1)
	c2_t0_t2_mem1 += MAIN_MEM_r[1]
	S += c2_t0_t2_mem1 <= c2_t0_t2

	c2_t1_t2 = S.Task('c2_t1_t2', length=2, delay_cost=1)
	c2_t1_t2 += alt(MAS)
	c2_t1_t2_in = S.Task('c2_t1_t2_in', length=1, delay_cost=1)
	c2_t1_t2_in += alt(MAS_in)
	S += c2_t1_t2_in*MAS_in[0]<=c2_t1_t2*MAS[0]

	S += c2_t1_t2_in*MAS_in[1]<=c2_t1_t2*MAS[1]

	S += c2_t1_t2_in*MAS_in[2]<=c2_t1_t2*MAS[2]

	S += c2_t1_t2_in*MAS_in[3]<=c2_t1_t2*MAS[3]

	S += c2_t1_t2_in*MAS_in[4]<=c2_t1_t2*MAS[4]

	S += c2_t1_t2_in*MAS_in[5]<=c2_t1_t2*MAS[5]

	c2_t1_t2_mem0 = S.Task('c2_t1_t2_mem0', length=1, delay_cost=1)
	c2_t1_t2_mem0 += MAIN_MEM_r[0]
	S += c2_t1_t2_mem0 <= c2_t1_t2

	c2_t1_t2_mem1 = S.Task('c2_t1_t2_mem1', length=1, delay_cost=1)
	c2_t1_t2_mem1 += MAIN_MEM_r[1]
	S += c2_t1_t2_mem1 <= c2_t1_t2

	c2_t20 = S.Task('c2_t20', length=2, delay_cost=1)
	c2_t20 += alt(MAS)
	c2_t20_in = S.Task('c2_t20_in', length=1, delay_cost=1)
	c2_t20_in += alt(MAS_in)
	S += c2_t20_in*MAS_in[0]<=c2_t20*MAS[0]

	S += c2_t20_in*MAS_in[1]<=c2_t20*MAS[1]

	S += c2_t20_in*MAS_in[2]<=c2_t20*MAS[2]

	S += c2_t20_in*MAS_in[3]<=c2_t20*MAS[3]

	S += c2_t20_in*MAS_in[4]<=c2_t20*MAS[4]

	S += c2_t20_in*MAS_in[5]<=c2_t20*MAS[5]

	c2_t20_mem0 = S.Task('c2_t20_mem0', length=1, delay_cost=1)
	c2_t20_mem0 += MAIN_MEM_r[0]
	S += c2_t20_mem0 <= c2_t20

	c2_t20_mem1 = S.Task('c2_t20_mem1', length=1, delay_cost=1)
	c2_t20_mem1 += MAIN_MEM_r[1]
	S += c2_t20_mem1 <= c2_t20

	c2_t21 = S.Task('c2_t21', length=2, delay_cost=1)
	c2_t21 += alt(MAS)
	c2_t21_in = S.Task('c2_t21_in', length=1, delay_cost=1)
	c2_t21_in += alt(MAS_in)
	S += c2_t21_in*MAS_in[0]<=c2_t21*MAS[0]

	S += c2_t21_in*MAS_in[1]<=c2_t21*MAS[1]

	S += c2_t21_in*MAS_in[2]<=c2_t21*MAS[2]

	S += c2_t21_in*MAS_in[3]<=c2_t21*MAS[3]

	S += c2_t21_in*MAS_in[4]<=c2_t21*MAS[4]

	S += c2_t21_in*MAS_in[5]<=c2_t21*MAS[5]

	c2_t21_mem0 = S.Task('c2_t21_mem0', length=1, delay_cost=1)
	c2_t21_mem0 += MAIN_MEM_r[0]
	S += c2_t21_mem0 <= c2_t21

	c2_t21_mem1 = S.Task('c2_t21_mem1', length=1, delay_cost=1)
	c2_t21_mem1 += MAIN_MEM_r[1]
	S += c2_t21_mem1 <= c2_t21

	c_qinv0_t0 = S.Task('c_qinv0_t0', length=10, delay_cost=1)
	c_qinv0_t0 += alt(MM)
	c_qinv0_t0_in = S.Task('c_qinv0_t0_in', length=1, delay_cost=1)
	c_qinv0_t0_in += alt(MM_in)
	S += c_qinv0_t0_in*MM_in[0]<=c_qinv0_t0*MM[0]
	S += c_qinv0_t0_in*MM_in[1]<=c_qinv0_t0*MM[1]
	c_qinv0_t0_mem0 = S.Task('c_qinv0_t0_mem0', length=1, delay_cost=1)
	c_qinv0_t0_mem0 += MAIN_MEM_r[0]
	S += c_qinv0_t0_mem0 <= c_qinv0_t0

	c_qinv0_t0_mem1 = S.Task('c_qinv0_t0_mem1', length=1, delay_cost=1)
	c_qinv0_t0_mem1 += alt(MM_MEM)
	S += (c_qinv_denom_inv0*MM[0])-1 < c_qinv0_t0_mem1*MM_MEM[1]
	S += (c_qinv_denom_inv0*MM[1])-1 < c_qinv0_t0_mem1*MM_MEM[3]
	S += c_qinv0_t0_mem1 <= c_qinv0_t0

	c_qinv0_t1 = S.Task('c_qinv0_t1', length=10, delay_cost=1)
	c_qinv0_t1 += alt(MM)
	c_qinv0_t1_in = S.Task('c_qinv0_t1_in', length=1, delay_cost=1)
	c_qinv0_t1_in += alt(MM_in)
	S += c_qinv0_t1_in*MM_in[0]<=c_qinv0_t1*MM[0]
	S += c_qinv0_t1_in*MM_in[1]<=c_qinv0_t1*MM[1]
	c_qinv0_t1_mem0 = S.Task('c_qinv0_t1_mem0', length=1, delay_cost=1)
	c_qinv0_t1_mem0 += MAIN_MEM_r[0]
	S += c_qinv0_t1_mem0 <= c_qinv0_t1

	c_qinv0_t1_mem1 = S.Task('c_qinv0_t1_mem1', length=1, delay_cost=1)
	c_qinv0_t1_mem1 += alt(MM_MEM)
	S += (c_qinv_denom_inv1_*MM[0])-1 < c_qinv0_t1_mem1*MM_MEM[1]
	S += (c_qinv_denom_inv1_*MM[1])-1 < c_qinv0_t1_mem1*MM_MEM[3]
	S += c_qinv0_t1_mem1 <= c_qinv0_t1

	c_qinv0_t3 = S.Task('c_qinv0_t3', length=2, delay_cost=1)
	c_qinv0_t3 += alt(MAS)
	c_qinv0_t3_in = S.Task('c_qinv0_t3_in', length=1, delay_cost=1)
	c_qinv0_t3_in += alt(MAS_in)
	S += c_qinv0_t3_in*MAS_in[0]<=c_qinv0_t3*MAS[0]

	S += c_qinv0_t3_in*MAS_in[1]<=c_qinv0_t3*MAS[1]

	S += c_qinv0_t3_in*MAS_in[2]<=c_qinv0_t3*MAS[2]

	S += c_qinv0_t3_in*MAS_in[3]<=c_qinv0_t3*MAS[3]

	S += c_qinv0_t3_in*MAS_in[4]<=c_qinv0_t3*MAS[4]

	S += c_qinv0_t3_in*MAS_in[5]<=c_qinv0_t3*MAS[5]

	c_qinv0_t3_mem0 = S.Task('c_qinv0_t3_mem0', length=1, delay_cost=1)
	c_qinv0_t3_mem0 += alt(MM_MEM)
	S += (c_qinv_denom_inv0*MM[0])-1 < c_qinv0_t3_mem0*MM_MEM[0]
	S += (c_qinv_denom_inv0*MM[1])-1 < c_qinv0_t3_mem0*MM_MEM[2]
	S += c_qinv0_t3_mem0 <= c_qinv0_t3

	c_qinv0_t3_mem1 = S.Task('c_qinv0_t3_mem1', length=1, delay_cost=1)
	c_qinv0_t3_mem1 += alt(MM_MEM)
	S += (c_qinv_denom_inv1_*MM[0])-1 < c_qinv0_t3_mem1*MM_MEM[1]
	S += (c_qinv_denom_inv1_*MM[1])-1 < c_qinv0_t3_mem1*MM_MEM[3]
	S += c_qinv0_t3_mem1 <= c_qinv0_t3

	c_qinv1__t0 = S.Task('c_qinv1__t0', length=10, delay_cost=1)
	c_qinv1__t0 += alt(MM)
	c_qinv1__t0_in = S.Task('c_qinv1__t0_in', length=1, delay_cost=1)
	c_qinv1__t0_in += alt(MM_in)
	S += c_qinv1__t0_in*MM_in[0]<=c_qinv1__t0*MM[0]
	S += c_qinv1__t0_in*MM_in[1]<=c_qinv1__t0*MM[1]
	c_qinv1__t0_mem0 = S.Task('c_qinv1__t0_mem0', length=1, delay_cost=1)
	c_qinv1__t0_mem0 += MAIN_MEM_r[0]
	S += c_qinv1__t0_mem0 <= c_qinv1__t0

	c_qinv1__t0_mem1 = S.Task('c_qinv1__t0_mem1', length=1, delay_cost=1)
	c_qinv1__t0_mem1 += alt(MM_MEM)
	S += (c_qinv_denom_inv0*MM[0])-1 < c_qinv1__t0_mem1*MM_MEM[1]
	S += (c_qinv_denom_inv0*MM[1])-1 < c_qinv1__t0_mem1*MM_MEM[3]
	S += c_qinv1__t0_mem1 <= c_qinv1__t0

	c_qinv1__t1 = S.Task('c_qinv1__t1', length=10, delay_cost=1)
	c_qinv1__t1 += alt(MM)
	c_qinv1__t1_in = S.Task('c_qinv1__t1_in', length=1, delay_cost=1)
	c_qinv1__t1_in += alt(MM_in)
	S += c_qinv1__t1_in*MM_in[0]<=c_qinv1__t1*MM[0]
	S += c_qinv1__t1_in*MM_in[1]<=c_qinv1__t1*MM[1]
	c_qinv1__t1_mem0 = S.Task('c_qinv1__t1_mem0', length=1, delay_cost=1)
	c_qinv1__t1_mem0 += MAIN_MEM_r[0]
	S += c_qinv1__t1_mem0 <= c_qinv1__t1

	c_qinv1__t1_mem1 = S.Task('c_qinv1__t1_mem1', length=1, delay_cost=1)
	c_qinv1__t1_mem1 += alt(MM_MEM)
	S += (c_qinv_denom_inv1_*MM[0])-1 < c_qinv1__t1_mem1*MM_MEM[1]
	S += (c_qinv_denom_inv1_*MM[1])-1 < c_qinv1__t1_mem1*MM_MEM[3]
	S += c_qinv1__t1_mem1 <= c_qinv1__t1

	c_qinv1__t3 = S.Task('c_qinv1__t3', length=2, delay_cost=1)
	c_qinv1__t3 += alt(MAS)
	c_qinv1__t3_in = S.Task('c_qinv1__t3_in', length=1, delay_cost=1)
	c_qinv1__t3_in += alt(MAS_in)
	S += c_qinv1__t3_in*MAS_in[0]<=c_qinv1__t3*MAS[0]

	S += c_qinv1__t3_in*MAS_in[1]<=c_qinv1__t3*MAS[1]

	S += c_qinv1__t3_in*MAS_in[2]<=c_qinv1__t3*MAS[2]

	S += c_qinv1__t3_in*MAS_in[3]<=c_qinv1__t3*MAS[3]

	S += c_qinv1__t3_in*MAS_in[4]<=c_qinv1__t3*MAS[4]

	S += c_qinv1__t3_in*MAS_in[5]<=c_qinv1__t3*MAS[5]

	c_qinv1__t3_mem0 = S.Task('c_qinv1__t3_mem0', length=1, delay_cost=1)
	c_qinv1__t3_mem0 += alt(MM_MEM)
	S += (c_qinv_denom_inv0*MM[0])-1 < c_qinv1__t3_mem0*MM_MEM[0]
	S += (c_qinv_denom_inv0*MM[1])-1 < c_qinv1__t3_mem0*MM_MEM[2]
	S += c_qinv1__t3_mem0 <= c_qinv1__t3

	c_qinv1__t3_mem1 = S.Task('c_qinv1__t3_mem1', length=1, delay_cost=1)
	c_qinv1__t3_mem1 += alt(MM_MEM)
	S += (c_qinv_denom_inv1_*MM[0])-1 < c_qinv1__t3_mem1*MM_MEM[1]
	S += (c_qinv_denom_inv1_*MM[1])-1 < c_qinv1__t3_mem1*MM_MEM[3]
	S += c_qinv1__t3_mem1 <= c_qinv1__t3

	c0_t4_t2 = S.Task('c0_t4_t2', length=2, delay_cost=1)
	c0_t4_t2 += alt(MAS)
	c0_t4_t2_in = S.Task('c0_t4_t2_in', length=1, delay_cost=1)
	c0_t4_t2_in += alt(MAS_in)
	S += c0_t4_t2_in*MAS_in[0]<=c0_t4_t2*MAS[0]

	S += c0_t4_t2_in*MAS_in[1]<=c0_t4_t2*MAS[1]

	S += c0_t4_t2_in*MAS_in[2]<=c0_t4_t2*MAS[2]

	S += c0_t4_t2_in*MAS_in[3]<=c0_t4_t2*MAS[3]

	S += c0_t4_t2_in*MAS_in[4]<=c0_t4_t2*MAS[4]

	S += c0_t4_t2_in*MAS_in[5]<=c0_t4_t2*MAS[5]

	c0_t4_t2_mem0 = S.Task('c0_t4_t2_mem0', length=1, delay_cost=1)
	c0_t4_t2_mem0 += alt(MAS_MEM)
	S += (c0_t20*MAS[0])-1 < c0_t4_t2_mem0*MAS_MEM[0]
	S += (c0_t20*MAS[1])-1 < c0_t4_t2_mem0*MAS_MEM[2]
	S += (c0_t20*MAS[2])-1 < c0_t4_t2_mem0*MAS_MEM[4]
	S += (c0_t20*MAS[3])-1 < c0_t4_t2_mem0*MAS_MEM[6]
	S += (c0_t20*MAS[4])-1 < c0_t4_t2_mem0*MAS_MEM[8]
	S += (c0_t20*MAS[5])-1 < c0_t4_t2_mem0*MAS_MEM[10]
	S += c0_t4_t2_mem0 <= c0_t4_t2

	c0_t4_t2_mem1 = S.Task('c0_t4_t2_mem1', length=1, delay_cost=1)
	c0_t4_t2_mem1 += alt(MAS_MEM)
	S += (c0_t21*MAS[0])-1 < c0_t4_t2_mem1*MAS_MEM[1]
	S += (c0_t21*MAS[1])-1 < c0_t4_t2_mem1*MAS_MEM[3]
	S += (c0_t21*MAS[2])-1 < c0_t4_t2_mem1*MAS_MEM[5]
	S += (c0_t21*MAS[3])-1 < c0_t4_t2_mem1*MAS_MEM[7]
	S += (c0_t21*MAS[4])-1 < c0_t4_t2_mem1*MAS_MEM[9]
	S += (c0_t21*MAS[5])-1 < c0_t4_t2_mem1*MAS_MEM[11]
	S += c0_t4_t2_mem1 <= c0_t4_t2

	c1_t4_t2 = S.Task('c1_t4_t2', length=2, delay_cost=1)
	c1_t4_t2 += alt(MAS)
	c1_t4_t2_in = S.Task('c1_t4_t2_in', length=1, delay_cost=1)
	c1_t4_t2_in += alt(MAS_in)
	S += c1_t4_t2_in*MAS_in[0]<=c1_t4_t2*MAS[0]

	S += c1_t4_t2_in*MAS_in[1]<=c1_t4_t2*MAS[1]

	S += c1_t4_t2_in*MAS_in[2]<=c1_t4_t2*MAS[2]

	S += c1_t4_t2_in*MAS_in[3]<=c1_t4_t2*MAS[3]

	S += c1_t4_t2_in*MAS_in[4]<=c1_t4_t2*MAS[4]

	S += c1_t4_t2_in*MAS_in[5]<=c1_t4_t2*MAS[5]

	c1_t4_t2_mem0 = S.Task('c1_t4_t2_mem0', length=1, delay_cost=1)
	c1_t4_t2_mem0 += alt(MAS_MEM)
	S += (c1_t20*MAS[0])-1 < c1_t4_t2_mem0*MAS_MEM[0]
	S += (c1_t20*MAS[1])-1 < c1_t4_t2_mem0*MAS_MEM[2]
	S += (c1_t20*MAS[2])-1 < c1_t4_t2_mem0*MAS_MEM[4]
	S += (c1_t20*MAS[3])-1 < c1_t4_t2_mem0*MAS_MEM[6]
	S += (c1_t20*MAS[4])-1 < c1_t4_t2_mem0*MAS_MEM[8]
	S += (c1_t20*MAS[5])-1 < c1_t4_t2_mem0*MAS_MEM[10]
	S += c1_t4_t2_mem0 <= c1_t4_t2

	c1_t4_t2_mem1 = S.Task('c1_t4_t2_mem1', length=1, delay_cost=1)
	c1_t4_t2_mem1 += alt(MAS_MEM)
	S += (c1_t21*MAS[0])-1 < c1_t4_t2_mem1*MAS_MEM[1]
	S += (c1_t21*MAS[1])-1 < c1_t4_t2_mem1*MAS_MEM[3]
	S += (c1_t21*MAS[2])-1 < c1_t4_t2_mem1*MAS_MEM[5]
	S += (c1_t21*MAS[3])-1 < c1_t4_t2_mem1*MAS_MEM[7]
	S += (c1_t21*MAS[4])-1 < c1_t4_t2_mem1*MAS_MEM[9]
	S += (c1_t21*MAS[5])-1 < c1_t4_t2_mem1*MAS_MEM[11]
	S += c1_t4_t2_mem1 <= c1_t4_t2

	c2_t4_t2 = S.Task('c2_t4_t2', length=2, delay_cost=1)
	c2_t4_t2 += alt(MAS)
	c2_t4_t2_in = S.Task('c2_t4_t2_in', length=1, delay_cost=1)
	c2_t4_t2_in += alt(MAS_in)
	S += c2_t4_t2_in*MAS_in[0]<=c2_t4_t2*MAS[0]

	S += c2_t4_t2_in*MAS_in[1]<=c2_t4_t2*MAS[1]

	S += c2_t4_t2_in*MAS_in[2]<=c2_t4_t2*MAS[2]

	S += c2_t4_t2_in*MAS_in[3]<=c2_t4_t2*MAS[3]

	S += c2_t4_t2_in*MAS_in[4]<=c2_t4_t2*MAS[4]

	S += c2_t4_t2_in*MAS_in[5]<=c2_t4_t2*MAS[5]

	c2_t4_t2_mem0 = S.Task('c2_t4_t2_mem0', length=1, delay_cost=1)
	c2_t4_t2_mem0 += alt(MAS_MEM)
	S += (c2_t20*MAS[0])-1 < c2_t4_t2_mem0*MAS_MEM[0]
	S += (c2_t20*MAS[1])-1 < c2_t4_t2_mem0*MAS_MEM[2]
	S += (c2_t20*MAS[2])-1 < c2_t4_t2_mem0*MAS_MEM[4]
	S += (c2_t20*MAS[3])-1 < c2_t4_t2_mem0*MAS_MEM[6]
	S += (c2_t20*MAS[4])-1 < c2_t4_t2_mem0*MAS_MEM[8]
	S += (c2_t20*MAS[5])-1 < c2_t4_t2_mem0*MAS_MEM[10]
	S += c2_t4_t2_mem0 <= c2_t4_t2

	c2_t4_t2_mem1 = S.Task('c2_t4_t2_mem1', length=1, delay_cost=1)
	c2_t4_t2_mem1 += alt(MAS_MEM)
	S += (c2_t21*MAS[0])-1 < c2_t4_t2_mem1*MAS_MEM[1]
	S += (c2_t21*MAS[1])-1 < c2_t4_t2_mem1*MAS_MEM[3]
	S += (c2_t21*MAS[2])-1 < c2_t4_t2_mem1*MAS_MEM[5]
	S += (c2_t21*MAS[3])-1 < c2_t4_t2_mem1*MAS_MEM[7]
	S += (c2_t21*MAS[4])-1 < c2_t4_t2_mem1*MAS_MEM[9]
	S += (c2_t21*MAS[5])-1 < c2_t4_t2_mem1*MAS_MEM[11]
	S += c2_t4_t2_mem1 <= c2_t4_t2

	solvers.mip.solve(S,msg=1,kind='CPLEX',ratio_gap=1.01)

	solution = [['hoge']*len(S.solution()[1]) for i in range(len(S.solution()))]
	for i in range(len(S.solution())):
		for j in range(len(S.solution()[i])):
			solution[i][j]=str(S.solution()[i][j])
	print(solution)

	cycles = int(solution[-1][3])

	pic_file_name = "/mnt/rose/usr1/fukuda/ABE/multiRAM_multiMAS_16mux/scheduling_result/stage10MM2_stage2MAS6/FP12_INV_AFTER_FPINV/schedule0.png"
	if(S.solution() != []):
		plotters.matplotlib.plot(S,img_filename=pic_file_name, show_task_labels=False, fig_size=(cycles*0.25+3, 8))

	return solution

