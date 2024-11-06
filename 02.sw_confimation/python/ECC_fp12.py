from ECC_param import *
param = BLS12_381()
from ECC_fp import *
from ECC_fp2 import *
from ECC_fp6 import *

# ------------------fp12 class definition------------------
@dataclass
class fp12_t:
    _0: fp2_t = fp6_t(fp2_t(0,0),fp2_t(0,0),fp2_t(0,0))
    _1: fp2_t = fp6_t(fp2_t(0,0),fp2_t(0,0),fp2_t(0,0))

    def __getitem__(self, indices):
        if(indices==0):
            return self._0
        elif(indices==1):
            return self._1
        else:
            raise ValueError('wrong indices type or value')

    def __setitem__(self, indices, value):
        if (not isinstance(value, fp6_t)):
            raise TypeError('value must be an fp6_t')
        if(indices==0):
            self._0 = value
        elif(indices==1):
            self._1 = value
        else:
            raise ValueError('wrong indices type or value')

# ------------------fp12 utilities------------------
def fp12_print(a:fp12_t):
    fp6_print(a[0])
    fp6_print(a[1])

def fp12_zero()->fp12_t:
    return fp12_t(fp6_zero(),fp6_zero())

# def fp12_is_zero(a:fp12_t)->bool:

def fp12_copy(a:fp12_t)->fp12_t:
    c=fp12_zero()
    c[0]=fp6_copy(a[0])
    c[1]=fp6_copy(a[1])
    return c

def fp12_cmp(a:fp12_t,b:fp12_t)->bool:
    return (fp6_cmp(a[0],b[0]) & fp6_cmp(a[1],b[1]))

# def fp12_rand()->fp12_t:

# ------------------fp12 arithmatics------------------
def fp12_add(a:fp12_t,b:fp12_t)->fp12_t:
    r=fp12_zero()
    r[0]=fp6_add(a[0],b[0])
    r[1]=fp6_add(a[1],b[1])
    return r

def fp12_neg(a:fp12_t)->fp12_t:
    r=fp12_zero()
    r[0]=fp6_neg(a[0])
    r[1]=fp6_neg(a[1])
    return r

def fp12_sub(a:fp12_t,b:fp12_t)->fp12_t:
    r=fp12_zero()
    r[0]=fp6_sub(a[0],b[0])
    r[1]=fp6_sub(a[1],b[1])
    return r

def fp12_dbl(a:fp12_t)->fp12_t:
    r=fp12_zero()
    r[0]=fp6_dbl(a[0])
    r[1]=fp6_dbl(a[1])
    return r

def fp12_mul(a:fp12_t,b:fp12_t)->fp12_t: # fp12_mul_basic
    t0=fp6_zero()
    t1=fp6_zero()
    t2=fp6_zero()
    c=fp12_zero()

    # Karatsuba algorithm
    # t0 = a_0 * b_0
    t0=fp6_mul(a[0], b[0])
    # t1 = a_1 * b_1
    t1=fp6_mul(a[1], b[1])
    # t2 = b_0 + b_1. */
    t2=fp6_add(b[0], b[1])

    # c_1 = a_0 + a_1
    c[1]=fp6_add(a[0], a[1])

    # c_1 = (a_0 + a_1) * (b_0 + b_1)
    c[1]=fp6_mul(c[1], t2)
    c[1]=fp6_sub(c[1], t0)
    c[1]=fp6_sub(c[1], t1)

    # c_0 = a_0b_0 + v * a_1b_1
    t1=fp6_mul_art(t1)
    c[0]=fp6_add(t0, t1)
    return c

def fp12_sqr(a:fp12_t)->fp12_t: #fp12_sqr_basic
    c=fp12_zero()
    t0=fp6_add(a[0], a[1])
    t1=fp6_mul_art(a[1])
    t1=fp6_add(a[0], t1)
    t0=fp6_mul(t0, t1)
    c[1]=fp6_mul(a[0], a[1])
    c[0]=fp6_sub(t0, c[1])
    t1=fp6_mul_art(c[1])
    c[0]=fp6_sub(c[0], t1)
    c[1]=fp6_dbl(c[1])
    return c

def fp12_inv(a:fp12_t)->fp12_t: # a^(-1)
    c=fp12_zero()
    t0=fp6_sqr(a[0])
    t1=fp6_sqr(a[1])
    t1=fp6_mul_art(t1)
    t0=fp6_sub(t0,t1)
    t0=fp6_inv(t0)

    c[0]=fp6_mul(a[0],t0)
    c[1]=fp6_neg(a[1])
    c[1]=fp6_mul(c[1],t0)
    return c

def fp12_exp_dig(a:fp12_t,b:int)->fp12_t: # gt_exp_dig for b < 64 bit
    t=fp12_copy(a)
    for i in bits_of(b)[1:]:
        t=fp12_sqr(t)
        if(i):
            t=fp12_mul(t,a)
    return t

def fp12_exp(a:fp12_t,b:int)->fp12_t:
    if(b>0):
        return fp12_exp_dig(a,b)
    elif(b<0):
        c=fp12_exp_dig(a,-b)
        return fp12_inv(c)
    else:
        return fp12_zero()

# ------------------fp12 for pairing------------------
def fp12_frb(a:fp12_t,i:int)->fp12_t:
    c=fp12_copy(a)
    for k in range(i%12,0,-1):
        c[0]=fp6_frb(c[0], 1)
        c[1][0]=fp2_frb(c[1][0], 1)
        c[1][1]=fp2_frb(c[1][1], 1)
        c[1][2]=fp2_frb(c[1][2], 1)
        c[1][0]=fp2_mul_frb(c[1][0], 1, 1)
        c[1][1]=fp2_mul_frb(c[1][1], 1, 3)
        c[1][2]=fp2_mul_frb(c[1][2], 1, 5)
    return c

"""
 * Multiples a dense dodecic extension field element by a sparse element using
 * basic arithmetic.
 *
 * @param[out] c			- the result.
 * @param[in] a				- the dense dodecic extension field element.
 * @param[in] b				- the sparse dodecic extension field element.
void fp12_mul_dxs_basic(fp12_t c, fp12_t a, fp12_t b);
"""
def fp12_mul_dxs(a:fp12_t, b:fp12_t):
    c=fp12_zero()
    t1=fp6_zero()
    t2=fp6_zero()

    # t0 = a_0 * b_0
    t0=fp6_mul_dxs(a[0], b[0])

    # t1 = a_1 * b_1
    t2[0]=fp2_mul(a[1][2], b[1][1])
    t1[0]=fp2_mul_nor(t2[0])
    t1[1]=fp2_mul(a[1][0], b[1][1])
    t1[2]=fp2_mul(a[1][1], b[1][1])

    # t2 = b_0 + b_1
    t2[0]=fp2_copy(b[0][0])
    t2[1]=fp2_add(b[0][1],b[1][1])

    # c_1 = a_0 + a_1
    c[1]=fp6_add(a[0],a[1])

    # c_1 = (a_0 + a_1) * (b_0 + b_1) - a_0 * b_0 - a_1 * b_1
    c[1]=fp6_mul_dxs(c[1], t2)
    c[1]=fp6_sub(c[1],t0)
    c[1]=fp6_sub(c[1],t1)
    # c_0 = a_0 * b_0 + v * a_1 * b_1
    t1=fp6_mul_art(t1)
    c[0]=fp6_add(t0,t1)

    return c

# cyclotomic group
"""
 * Computes the inverse of a cyclotomic dodecic extension field element.
 * For unitary elements, this is equivalent to computing the conjugate.
 * A unitary element is one previously raised to the (p^6 - 1)-th power.
 *
 * @param[out] c			- the result.
 * @param[in] a				- the dodecic extension field element to invert.
"""
def fp12_inv_cyc(a:fp12_t)->fp12_t: # a^(p^6)
    c=fp12_zero()
    c[0]=fp6_copy(a[0])
    c[1]=fp6_neg(a[1])
    return c

"""
 * Converts a dodecic extension field element to a cyclotomic element.
 * Computes c = a^(p^6 - 1)*(p^2 + 1).
 *
 * @param[out] c			- the result.
 * @param[in] a				- a dodecic extension field element.
"""
def fp12_conv_cyc(a:fp12_t)->fp12_t:
    # First, compute c = a^(p^6 - 1)
    # t = a^{-1}
    t=fp12_inv(a)
    # c = a^(p^6)
    c=fp12_inv_cyc(a)
    # c = a^(p^6 - 1)
    c=fp12_mul(c, t)

    # Second, compute c^(p^2 + 1)
    # t = c^(p^2)
    t=fp12_frb(c, 2)

    # c = c^(p^2 + 1)
    c=fp12_mul(c, t)

    return c

def fp12_sqr_cyc(a:fp12_t)->fp12_t: #fp12_sqr_cyc_basic
    c=fp12_zero()
    # Define z = sqrt(E)

    # Now a is seen as (t0,t1) + (t2,t3) * w + (t4,t5) * w^2

    # (t0, t1) = (a00 + a11*z)^2
    t2=fp2_sqr(a[0][0])
    t3=fp2_sqr(a[1][1])
    t1=fp2_add(a[0][0], a[1][1])

    t0=fp2_mul_nor(t3)
    t0=fp2_add(t0, t2)

    t1=fp2_sqr(t1)
    t1=fp2_sub(t1, t2)
    t1=fp2_sub(t1, t3)

    c[0][0]=fp2_sub(t0, a[0][0])
    c[0][0]=fp2_add(c[0][0], c[0][0])
    c[0][0]=fp2_add(t0, c[0][0])

    c[1][1]=fp2_add(t1, a[1][1])
    c[1][1]=fp2_add(c[1][1], c[1][1])
    c[1][1]=fp2_add(t1, c[1][1])

    t0=fp2_sqr(a[0][1])
    t1=fp2_sqr(a[1][2])
    t5=fp2_add(a[0][1], a[1][2])
    t2=fp2_sqr(t5)

    t3=fp2_add(t0, t1)
    t5=fp2_sub(t2, t3)

    t6=fp2_add(a[1][0], a[0][2])
    t3=fp2_sqr(t6)
    t2=fp2_sqr(a[1][0])

    t6=fp2_mul_nor(t5)
    t5=fp2_add(t6, a[1][0])
    t5=fp2_dbl(t5)
    c[1][0]=fp2_add(t5, t6)

    t4=fp2_mul_nor(t1)
    t5=fp2_add(t0, t4)
    t6=fp2_sub(t5, a[0][2])

    t1=fp2_sqr(a[0][2])

    t6=fp2_dbl(t6)
    c[0][2]=fp2_add(t6, t5)

    t4=fp2_mul_nor(t1)
    t5=fp2_add(t2, t4)
    t6=fp2_sub(t5, a[0][1])
    t6=fp2_dbl(t6)
    c[0][1]=fp2_add(t6, t5)

    t0=fp2_add(t2, t1)
    t5=fp2_sub(t3, t0)
    t6=fp2_add(t5, a[1][2])
    t6=fp2_dbl(t6)
    c[1][2]=fp2_add(t5, t6)

    return c

"""
 * Squares a dodecic extension field element in the cyclotomic subgroup in
 * compressed form. Computes C = A * A.
 *
 * @param[out] C			- the result.
 * @param[in] A				- the dodecic extension field element to square.
"""
def fp12_sqr_pck(a:fp12_t)->fp12_t: # fp12_sqr_pck_basic
    c=fp12_zero()
    c[0][0]=fp2_copy(a[0][0])
    c[0][1]=fp2_copy(a[0][1])
    c[1][1]=fp2_copy(a[1][1])

    t0=fp2_sqr(a[0][1])
    t1=fp2_sqr(a[1][2])
    t5=fp2_add(a[0][1], a[1][2])
    t2=fp2_sqr(t5)

    t3=fp2_add(t0, t1)
    t5=fp2_sub(t2, t3)

    t6=fp2_add(a[1][0], a[0][2])
    t3=fp2_sqr(t6)
    t2=fp2_sqr(a[1][0])

    t6=fp2_mul_nor(t5)
    t5=fp2_add(t6, a[1][0])
    t5=fp2_dbl(t5)
    c[1][0]=fp2_add(t5, t6)

    t4=fp2_mul_nor(t1)
    t5=fp2_add(t0, t4)
    t6=fp2_sub(t5, a[0][2])

    t1=fp2_sqr(a[0][2])

    t6=fp2_dbl(t6)
    c[0][2]=fp2_add(t6, t5)

    t4=fp2_mul_nor(t1)
    t5=fp2_add(t2, t4)
    t6=fp2_sub(t5, a[0][1])
    t6=fp2_dbl(t6)
    c[0][1]=fp2_add(t6, t5)

    t0=fp2_add(t2, t1)
    t5=fp2_sub(t3, t0)
    t6=fp2_add(t5, a[1][2])
    t6=fp2_dbl(t6)
    c[1][2]=fp2_add(t5, t6)

    return c

"""
 * Decompresses multiple compressed cyclotomic extension field elements.
 *
 * @param[out] c			- the result.
 * @param[in] a				- the dodecic field elements to decompress.
 * @param[in] n				- the number of field elements to decompress.
void fp12_back_cyc_sim(fp12_t c[], fp12_t a[], int n)
"""
def fp12_back_cyc_sim(c:List[fp12_t],a:List[fp12_t],n:int)->List[fp12_t]:
    t0=[fp2_t(0,0)]*n
    t1=[fp2_t(0,0)]*n
    t2=[fp2_t(0,0)]*n

    for i in range(n):
        # t0 = g4^2
        t0[i]=fp2_sqr(a[i][0][1])
        # t1 = 3 * g4^2 - 2 * g3
        t1[i]=fp2_sub(t0[i], a[i][0][2])
        t1[i]=fp2_dbl(t1[i])
        t1[i]=fp2_add(t1[i], t0[i])
        # t0 = E * g5^2 + t1
        t2[i]=fp2_sqr(a[i][1][2])
        t0[i]=fp2_mul_nor(t2[i])
        t0[i]=fp2_add(t0[i], t1[i])
        # t1 = (4 * g2)
        t1[i]=fp2_dbl(a[i][1][0])
        t1[i]=fp2_dbl(t1[i])

    # t1 = 1 / t1
    for i in range(n):
        t1[i]=fp2_inv(t1[i])

    for i in range(n):
        # t0 = g1
        c[i][1][1]=fp2_mul(t0[i], t1[i])

        # t1 = g3 * g4
        t1[i]=fp2_mul(a[i][0][2], a[i][0][1])
        # t2 = 2 * g1^2 - 3 * g3 * g4
        t2[i]=fp2_sqr(c[i][1][1])
        t2[i]=fp2_sub(t2[i], t1[i])
        t2[i]=fp2_dbl(t2[i])
        t2[i]=fp2_sub(t2[i], t1[i])
        # t1 = g2 * g5
        t1[i]=fp2_mul(a[i][1][0], a[i][1][2])
        # t2 = E * (2 * g1^2 + g2 * g5 - 3 * g3 * g4) + 1
        t2[i]=fp2_add(t2[i], t1[i])
        c[i][0][0]=fp2_mul_nor(t2[i])
        c[i][0][0][0]=fp_add(c[i][0][0][0],1)

        c[i][0][1]=fp2_copy(a[i][0][1])
        c[i][0][2]=fp2_copy(a[i][0][2])
        c[i][1][0]=fp2_copy(a[i][1][0])
        c[i][1][2]=fp2_copy(a[i][1][2])

def fp12_exp_cyc_sps(a:fp12_t,b,b_len:int)->fp12_t:
    c=fp12_zero()
    u=[None]*b_len
    t=fp12_copy(a)

    for i in range(b_len):
        k=abs(b[i])
        for j in range(k):
            t=fp12_sqr_pck(t)
        if(b[i] < 0):
            u[i]=fp12_inv_cyc(t)
        else:
            u[i]=fp12_copy(t)

    fp12_back_cyc_sim(u, u, b_len)

    c=fp12_copy(u[0])
    for i in range(1,b_len):
        c=fp12_mul(c,u[i])

    c=fp12_inv_cyc(c) # if (sign == RLC_NEG)

    return c
