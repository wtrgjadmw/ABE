from ECC_param import *
param = BLS12_381()
from ECC_fp import *
from ECC_fp2 import *
from ECC_fp6 import *
from ECC_fp12 import *
from ECC_ep import *
from ECC_ep2 import *

#void pp_dbl_k12_projc_basic(fp12_t l, ep2_t r, ep2_t q, ep_t p) {
def pp_dbl_k12_projc(l:fp12_t,r:ep2_t,q:ep2_t,p:ep_t):
    # A = x1^2
    t0=fp2_sqr(q.x)
    # B = y1^2
    t1=fp2_sqr(q.y)
    # C = z1^2
    t2=fp2_sqr(q.z)
    # D = 3bC, for general b
    t3=fp2_dbl(t2)
    t3=fp2_add(t3, t2)
    t3=fp2_mul(t3, fp2_t(param.curve_b,param.curve_b))
    # E = (x1 + y1)^2 - A - B
    t4=fp2_add(q.x, q.y)
    t4=fp2_sqr(t4)
    t4=fp2_sub(t4, t0)
    t4=fp2_sub(t4, t1)

    # F = (y1 + z1)^2 - B - C
    t5=fp2_add(q.y, q.z)
    t5=fp2_sqr(t5)
    t5=fp2_sub(t5, t1)
    t5=fp2_sub(t5, t2)

    # G = 3D
    t6=fp2_dbl(t3)
    t6=fp2_add(t6, t3)

    # x3 = E * (B - G)
    r.x=fp2_sub(t1, t6)
    r.x=fp2_mul(r.x, t4)

    # y3 = (B + G)^2 -12D^2
    t6=fp2_add(t6, t1)
    t6=fp2_sqr(t6)
    t2=fp2_sqr(t3)
    r.y=fp2_dbl(t2)
    t2=fp2_dbl(r.y)
    r.y=fp2_dbl(t2)
    r.y=fp2_add(r.y, t2)
    r.y=fp2_sub(t6, r.y)

    # z3 = 4B * F
    r.z=fp2_dbl(t1)
    r.z=fp2_dbl(r.z)
    r.z=fp2_mul(r.z, t5)

    # l00 = D - B
    l[0][0]=fp2_sub(t3, t1)

    # l10 = (3 * xp) * A
    l[0][1][0]=fp_mul(p.x, t0[0])
    l[0][1][1]=fp_mul(p.x, t0[1])

    # l01 = F * (-yp). */
    l[1][1][0]=fp_mul(t5[0], p.y)
    l[1][1][1]=fp_mul(t5[1], p.y)

#void pp_add_k12_projc_basic(fp12_t l, ep2_t r, ep2_t q, ep_t p) {
def pp_add_k12_projc(l:fp12_t,r:ep2_t,q:ep2_t,p:ep_t):
    t4=fp2_zero()

    # B = t0 = x1 - x2 * z1
    t0=fp2_mul(r.z, q.x)
    t0=fp2_sub(r.x, t0)
    # A = t1 = y1 - y2 * z1
    t1=fp2_mul(r.z, q.y)
    t1=fp2_sub(r.y, t1)

    # D = B^2
    t2=fp2_sqr(t0)
    # G = x1 * D
    r.x=fp2_mul(t2, r.x)
    # E = B^3
    t2=fp2_mul(t0, t2)
    # C = A^2
    t3=fp2_sqr(t1)
    # F = E + z1 * C
    t3=fp2_mul(t3, r.z)
    t3=fp2_add(t2, t3)

    # l10 = - (A * xp)
    t4[0]=fp_neg(p.x)
    l[0][1][0]=fp_mul(t1[0], t4[0])
    l[0][1][1]=fp_mul(t1[1], t4[0])

    # t4 = B * x2
    t4=fp2_mul(q.x, t1)

    # H = F - 2 * G
    t3=fp2_sub(t3, r.x)
    t3=fp2_sub(t3, r.x)
    # y3 = A * (G - H) - y1 * E
    r.x=fp2_sub(r.x, t3)
    t1=fp2_mul(t1, r.x)
    r.y=fp2_mul(t2, r.y)
    r.y=fp2_sub(t1, r.y)
    # x3 = B * H
    r.x=fp2_mul(t0, t3)
    # z3 = z1 * E
    r.z=fp2_mul(r.z, t2)

    # l11 = J = A * x2 - B * y2
    t2=fp2_mul(q.y, t0)
    l[0][0]=fp2_sub(t4, t2)

    # l00 = B * yp
    l[1][1][0]=fp_mul(t0[0],p.y)
    l[1][1][1]=fp_mul(t0[1],p.y)

"""
 * Compute the Miller loop for pairings of type G_2 x G_1 over the bits of a
 * given parameter represented in sparse form.
 *
 * @param[out] r			- the result.
 * @param[out] t			- the resulting point.
 * @param[in] q				- the vector of first arguments in affine coordinates.
 * @param[in] p				- the vector of second arguments in affine coordinates.
 * @param[in] n 			- the number of pairings to evaluate.
 * @param[in] a				- the loop parameter.
static void pp_mil_k12(fp12_t r, ep2_t *t, ep2_t *q, ep_t *p, int m, bn_t a) {
"""
def pp_mil_k12(q:ep2_t,p:ep_t,a:int):
    len_= len(bits_of(a))+1
    l=fp12_zero()

    t=ep2_copy(q)
    _q=ep2_neg(q)
    _p=ep_t(0,0,1)
    _p.x=fp_add(p.x,p.x)
    _p.x=fp_add(_p.x,p.x)
    _p.y=fp_neg(p.y)

    l=fp12_zero()
    r=fp12_zero()
    naf,naf_len = bn_rec_naf(len_,a,2)

    pp_dbl_k12_projc(r, t, t, _p)

    if(naf[naf_len-2]>0):
        pp_add_k12_projc(l, t, q, p)
        r=fp12_mul_dxs(r,l)
    elif(naf[naf_len-2]<0):
        pp_add_k12_projc(l, t, _q, p)
        r=fp12_mul_dxs_lazyr(r,l)

    for i in range(naf_len-2,0,-1):
        r=fp12_sqr(r)
        pp_dbl_k12_projc(l, t, t, _p)
        r=fp12_mul_dxs(r,l)
        if(naf[i-1]>0):
            pp_add_k12_projc(l, t, q, p)
            r=fp12_mul_dxs(r,l)
        elif(naf[i-1]<0):
            pp_add_k12_projc(l, t, _q, p)
            r=fp12_mul_dxs(r,l)

    return r,t

"""
 * Computes the final exponentiation of a pairing defined over a
 * Barreto-Lynn-Scott curve.
 *
 * @param[out] c			- the result.
 * @param[in] a				- the extension field element to exponentiate.
static void pp_exp_b12(fp12_t c, fp12_t a) {
"""
def pp_exp_b12(a:fp12_t)->fp12_t:
#      * Final exponentiation following Ghammam and Fouotsa:
#      * On the Computation of Optimal Ate Pairing at the 192-bit Level.
    b=[None]*6
    b[0]=16 #16
    b[1]=32 #48
    b[2]=9 #57
    b[3]=3 #60
    b[4]=-2 #-62
    b[5]=2 #64
    l=6  # b = fp_prime_get_par_sps(&l);

    # First, compute m^(p^6 - 1)(p^2 + 1)
    c=fp12_conv_cyc(a)

    # Now compute m^((p^4 - p^2 + 1) / r)
    # t0 = f^2
    t0=fp12_sqr_cyc(c)

    # t1 = f^x
    t1=fp12_exp_cyc_sps(c, b, l)

    # t2 = f^(x^2)
    t2=fp12_exp_cyc_sps(t1, b, l)

    # t1 = t2/(t1^2 * f)
    t3=fp12_inv_cyc(c)
    t1=fp12_sqr_cyc(t1)
    t1=fp12_mul(t1, t3)
    t1=fp12_inv_cyc(t1)
    t1=fp12_mul(t1, t2)

    # t2 = t1^x
    t2=fp12_exp_cyc_sps(t1, b, l)

    # t3 = t2^x/t1
    t3=fp12_exp_cyc_sps(t2, b, l)
    t1=fp12_inv_cyc(t1)
    t3=fp12_mul(t1, t3)

    # t1 = t1^(-p^3 ) * t2^(p^2)
    t1=fp12_inv_cyc(t1)
    t1=fp12_frb(t1, 3)
    t2=fp12_frb(t2, 2)
    t1=fp12_mul(t1, t2)

    # t2 = f * f^2 * t3^x
    t2=fp12_exp_cyc_sps(t3, b, l)
    t2=fp12_mul(t2, t0)
    t2=fp12_mul(t2, c)

    # Compute t1 * t2 * t3^p
    t1=fp12_mul(t1, t2)
    t2=fp12_frb(t3, 1)
    c=fp12_mul(t1, t2)
    return c

def pp_map_oatep_k12(p:ep_t,q:ep2_t)->fp12_t:
    r=fp12_zero()
    r[0][0][0]=1
    _p=ep_norm(p)
    _q=ep2_norm(q)
    if((not ep_is_infty(p)) and (not ep2_is_infty(q))):
        # EP_B12
        r,t=pp_mil_k12(_q,_p,-param.u) # -(-0xD201000000010000) need to make it positive
        r=fp12_inv_cyc(r) # if (bn_sign(a) == RLC_NEG)
        r=pp_exp_b12(r)
    return r
