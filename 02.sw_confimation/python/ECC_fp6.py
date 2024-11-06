from ECC_param import *
param = BLS12_381()
from ECC_fp import *
from ECC_fp2 import *

# ------------------fp6 class definition------------------
@dataclass
class fp6_t:
    _0: fp2_t = fp2_t(0,0)
    _1: fp2_t = fp2_t(0,0)
    _2: fp2_t = fp2_t(0,0)

    def __getitem__(self, indices):
        if(indices==0):
            return self._0
        elif(indices==1):
            return self._1
        elif(indices==2):
            return self._2
        else:
            raise ValueError('wrong indices type or value')

    def __setitem__(self, indices, value):
        if (not isinstance(value, fp2_t)):
            raise TypeError('value must be an fp2_t')
        if(indices==0):
            self._0 = value
        elif(indices==1):
            self._1 = value
        elif(indices==2):
            self._2 = value
        else:
            raise ValueError('wrong indices type or value')
# ------------------fp6 utilities------------------
def fp6_print(a:fp6_t):
    fp2_print(a[0])
    fp2_print(a[1])
    fp2_print(a[2])

def fp6_zero()->fp6_t:
    return fp6_t(fp2_t(0,0),fp2_t(0,0),fp2_t(0,0))

# def fp6_is_zero(a:fp6_t)->bool:

def fp6_copy(a:fp6_t)->fp6_t:
    c=fp6_zero()
    c[0]=fp2_copy(a[0])
    c[1]=fp2_copy(a[1])
    c[2]=fp2_copy(a[2])
    return c

def fp6_cmp(a:fp6_t,b:fp6_t)->bool:
    return (fp2_cmp(a[0],b[0]) & fp2_cmp(a[1],b[1]) & fp2_cmp(a[2],b[2]))

# def fp6_rand()->fp6_t:

# ------------------fp6 arithmatics------------------
def fp6_add(a:fp6_t,b:fp6_t)->fp6_t:
    r=fp6_zero()
    r[0]=fp2_add(a[0],b[0])
    r[1]=fp2_add(a[1],b[1])
    r[2]=fp2_add(a[2],b[2])
    return r

def fp6_neg(a:fp6_t)->fp6_t:
    r=fp6_zero()
    r[0]=fp2_neg(a[0])
    r[1]=fp2_neg(a[1])
    r[2]=fp2_neg(a[2])
    return r

def fp6_sub(a:fp6_t,b:fp6_t)->fp6_t:
    r=fp6_zero()
    r[0]=fp2_sub(a[0],b[0])
    r[1]=fp2_sub(a[1],b[1])
    r[2]=fp2_sub(a[2],b[2])
    return r

def fp6_dbl(a:fp6_t)->fp6_t:
    r=fp6_zero()
    r[0]=fp2_dbl(a[0])
    r[1]=fp2_dbl(a[1])
    r[2]=fp2_dbl(a[2])
    return r

def fp6_mul(a:fp6_t,b:fp6_t)->fp6_t: #fp6_mul_basic
    c=fp6_zero()

    # v0 = a_0b_0
    v0=fp2_mul(a[0], b[0])

    # v1 = a_1b_1
    v1=fp2_mul(a[1], b[1])

    # v2 = a_2b_2
    v2=fp2_mul(a[2], b[2])

    # t2 (c_0) = v0 + E((a_1 + a_2)(b_1 + b_2) - v1 - v2)
    t0=fp2_add(a[1], a[2])
    t1=fp2_add(b[1], b[2])
    t2=fp2_mul(t0, t1)
    t2=fp2_sub(t2, v1)
    t2=fp2_sub(t2, v2)
    t0=fp2_mul_nor(t2)
    t2=fp2_add(t0, v0)

    # c_1 = (a_0 + a_1)(b_0 + b_1) - v0 - v1 + Ev2
    t0=fp2_add(a[0], a[1])
    t1=fp2_add(b[0], b[1])
    c[1]=fp2_mul(t0, t1)
    c[1]=fp2_sub(c[1], v0)
    c[1]=fp2_sub(c[1], v1)
    t0=fp2_mul_nor(v2)
    c[1]=fp2_add(c[1], t0)

    # c_2 = (a_0 + a_2)(b_0 + b_2) - v0 + v1 - v2
    t0=fp2_add(a[0], a[2])
    t1=fp2_add(b[0], b[2])
    c[2]=fp2_mul(t0, t1)
    c[2]=fp2_sub(c[2], v0)
    c[2]=fp2_add(c[2], v1)
    c[2]=fp2_sub(c[2], v2)

    # c_0 = t2
    c[0]=fp2_copy(t2)

    return c

def fp6_sqr(a:fp6_t)->fp6_t: # fp6_sqr_basic
    c=fp6_zero()
    # t0 = a_0^2
    t0=fp2_sqr(a[0])

    # t1 = 2 * a_1 * a_2
    t1=fp2_mul(a[1], a[2])
    t1=fp2_dbl(t1)

    # t2 = a_2^2
    t2=fp2_sqr(a[2])

    # c2 = a_0 + a_2
    c[2]=fp2_add(a[0], a[2])

    # t3 = (a_0 + a_2 + a_1)^2
    t3=fp2_add(c[2], a[1])
    t3=fp2_sqr(t3)

    # c2 = (a_0 + a_2 - a_1)^2
    c[2]=fp2_sub(c[2], a[1])
    c[2]=fp2_sqr(c[2])

    # c2 = (c2 + t3)/2
    c[2]=fp2_add(c[2], t3)
    c[2][0]=fp_hlv(c[2][0])
    c[2][1]=fp_hlv(c[2][1])

    # t3 = t3 - c2 - t1
    t3=fp2_sub(t3, c[2])
    t3=fp2_sub(t3, t1)

    # c2 = c2 - t0 - t2
    c[2]=fp2_sub(c[2], t0)
    c[2]=fp2_sub(c[2], t2)

    # c0 = t0 + t1 * E
    t4=fp2_mul_nor(t1)
    c[0]=fp2_add(t0, t4)

    # c1 = t3 + t2 * E
    t4=fp2_mul_nor(t2)
    c[1]=fp2_add(t3, t4)

    return c

def fp6_inv(a:fp6_t)->fp6_t:
    c=fp6_zero()
    # v0 = a_0^2 - E * a_1 * a_2
    t0=fp2_sqr(a[0])
    v0=fp2_mul(a[1], a[2])
    v2=fp2_mul_nor(v0)
    v0=fp2_sub(t0, v2)

    # v1 = E * a_2^2 - a_0 * a_1
    t0=fp2_sqr(a[2])
    v2=fp2_mul_nor(t0)
    v1=fp2_mul(a[0], a[1])
    v1=fp2_sub(v2, v1)

    # v2 = a_1^2 - a_0 * a_2
    t0=fp2_sqr(a[1])
    v2=fp2_mul(a[0], a[2])
    v2=fp2_sub(t0, v2)

    t0=fp2_mul(a[1], v2)
    c[1]=fp2_mul_nor(t0)

    c[0]=fp2_mul(a[0], v0)

    t0=fp2_mul(a[2], v1)
    c[2]=fp2_mul_nor(t0)

    t0=fp2_add(c[0], c[1])
    t0=fp2_add(t0, c[2])
    t0=fp2_inv(t0)

    c[0]=fp2_mul(v0, t0)
    c[1]=fp2_mul(v1, t0)
    c[2]=fp2_mul(v2, t0)
    return c

# ------------------fp6 for pairing------------------
def fp6_mul_art(a:fp6_t)->fp6_t:
    c=fp6_zero()
    # (a_0 + a_1 * v + a_2 * v^2) * v = a_2 + a_0 * v + a_1 * v^2
    c[0]=fp2_mul_nor(a[2])
    c[2]=fp2_copy(a[1])
    c[1]=fp2_copy(a[0])
    return c

def fp6_mul_dxs(a,b):
    c=fp6_zero()
    # v0 = a_0b_0
    v0=fp2_mul(a[0], b[0])

    # v1 = a_1b_1
    v1=fp2_mul(a[1], b[1])

    # v2 = a_2b_2 = 0

    # t2 (c0) = v0 + E((a_1 + a_2)(b_1 + b_2) - v1 - v2)
    t0=fp2_add(a[1], a[2])
    t0=fp2_mul(t0, b[1])
    t0=fp2_sub(t0, v1)
    t2=fp2_mul_nor(t0)
    t2=fp2_add(t2, v0)

    # c1 = (a_0 + a_1)(b_0 + b_1) - v0 - v1 + Ev2
    t0=fp2_add(a[0], a[1])
    t1=fp2_add(b[0], b[1])
    c[1]=fp2_mul(t0, t1)
    c[1]=fp2_sub(c[1], v0)
    c[1]=fp2_sub(c[1], v1)

    # c2 = (a_0 + a_2)(b_0 + b_2) - v0 + v1 - v2
    t0=fp2_add(a[0], a[2])
    c[2]=fp2_mul(t0, b[0])
    c[2]=fp2_sub(c[2], v0)
    c[2]=fp2_add(c[2], v1)

    # c0 = t2 */
    c[0]=fp2_copy(t2)
    return c

def fp6_frb(a:fp6_t,i:int)->fp6_t:
    c=fp6_copy(a)
    for k in range(i%6,0,-1):
        c[0]=fp2_frb(c[0], 1)
        c[1]=fp2_frb(c[1], 1)
        c[2]=fp2_frb(c[2], 1)
        c[1]=fp2_mul_frb(c[1], 1, 2)
        c[2]=fp2_mul_frb(c[2], 1, 4)
    return c
