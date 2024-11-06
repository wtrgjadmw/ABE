# RELIC ep2 functions
from ECC_param import *
param = BLS12_381()
from ECC_ep import *
from ECC_fp import *
from ECC_fp2 import *
# ------------------ep2 class definition------------------
@dataclass
class ep2_t:
    x: fp2_t = fp2_t(0,0)
    y: fp2_t = fp2_t(0,0)
    z: fp2_t = fp2_t(0,0)
# ------------------ep2 utilities------------------
def ep2_print(p:ep2_t):
    fp2_print(p.x)
    fp2_print(p.y)
    fp2_print(p.z)

def ep2_print_(p:ep2_t):
    fp2_print_(p.x)
    fp2_print_(p.y)
    fp2_print_(p.z)

def ep2_inf()->ep2_t:
    return ep2_t(fp2_t(0,0),fp2_t(0,0),fp2_t(0,0))

def ep2_is_infty(p:ep2_t)->bool:
    fp2_zero=fp2_t(0,0)
    return fp2_cmp(p.x,fp2_zero) & fp2_cmp(p.y,fp2_zero) & fp2_cmp(p.z,fp2_zero)

def ep2_rhs(p:ep2_t)->fp2_t:
    # Curve function: y^2 = x^3 + ax + b
    yt1=fp2_mul(p.x,p.x)
    yt2=fp2_add(fp2_t(param.curve_a,param.curve_a),yt1)
    yt3=fp2_mul(yt2,p.x)
    yt4=fp2_add(yt3,fp2_t(param.curve_b,param.curve_b))
    return yt4

def ep2_on_curve(p:ep2_t)->bool:
    rhs=ep2_rhs(p)
    lhs=fp2_sqr(p.y)
    return fp2_cmp(lhs,rhs) or ep2_is_infty(p)

# def ep2_read_bin(bin:str,len:int)->ep2_t:

def ep2_norm(p:ep2_t)->ep2_t:
    if(ep2_is_infty(p)):
        return ep2_inf()
    else:
        zinv=fp2_inv(p.z)
        x=fp2_mul(p.x,zinv)
        y=fp2_mul(p.y,zinv)
        return ep2_t(x,y,fp2_t(1,0))

def ep2_copy(p:ep2_t)->ep2_t:
    return ep2_t(fp2_t(p.x.r,p.x.i),fp2_t(p.y.r,p.y.i),fp2_t(p.z.r,p.z.i))

def ep2_cmp(p:ep2_t,q:ep2_t)->bool:
    return fp2_cmp(p.x,q.x) & fp2_cmp(p.y,q.y) & fp2_cmp(p.z,q.z)

def ep2_curve_get_gen():
    xr=0x024AA2B2F08F0A91260805272DC51051C6E47AD4FA403B02B4510B647AE3D1770BAC0326A805BBEFD48056C8C121BDB8
    xi=0x13E02B6052719F607DACD3A088274F65596BD0D09920B61AB5DA61BBDC7F5049334CF11213945D57E5AC7D055D042B7E
    yr=0x0CE5D527727D6E118CC9CDC6DA2E351AADFD9BAA8CBDD3A76D429A695160D12C923AC9CC3BACA289E193548608B82801
    yi=0x0606C4A02EA734CC32ACD2B02BC28B99CB3E287E85A763AF267492AB572E99AB3F370D275CEC1DA1AAA9075FF05F79BE
    return ep2_t(fp2_t(xr,xi),fp2_t(yr,yi),fp2_t(1,0))

# ------------------ep2 arithmatics------------------
def ep2_add(p:ep2_t,q:ep2_t)->ep2_t:
    if(ep2_is_infty(p)):
        return ep2_copy(q)
    elif(ep2_is_infty(q)):
        return ep2_copy(p)
    else:
        t0 = fp2_mul(p.y, q.z)
        t1 = fp2_mul(p.x, q.z)
        t2 = fp2_mul(p.z, q.z)
        t3 = fp2_mul(q.y, p.z)
        t4 = fp2_sub(t3, t0)
        t5 = fp2_mul(t4, t4)
        t6 = fp2_mul(q.x, p.z)
        t7 = fp2_sub(t6, t1)
        t8 = fp2_mul(t7, t7)
        t9 = fp2_mul(t7, t8)
        t10 = fp2_mul(t8, t1)
        t11 = fp2_mul(t5, t2)
        t12 = fp2_sub(t11, t9)
        t13 = fp2_add(t10, t10)
        A = fp2_sub(t12, t13)
        X3 = fp2_mul(t7, A)
        t14 = fp2_sub(t10, A)
        t15 = fp2_mul(t4, t14)
        t16 = fp2_mul(t9, t0)
        Y3 = fp2_sub(t15, t16)
        Z3 = fp2_mul(t9, t2)
        return ep2_t(X3,Y3,Z3)

def ep2_neg(p:ep2_t)->ep2_t:
    if(ep2_is_infty(p)):
        return ep2_inf()
    else:
        return ep2_t(p.x,fp2_neg(p.y),p.z)

def ep2_sub(p:ep2_t,q:ep2_t)->ep2_t:
    if(ep2_cmp(p,q)):
        return ep2_inf()
    else:
        t=ep2_neg(q)
        return ep2_add(p,t)

def ep2_dbl(p:ep2_t):
    if(ep2_is_infty(p)):
        return ep2_inf()
    else:
        XX = fp2_mul(p.x, p.x)
        ZZ = fp2_mul(p.z, p.z)
        t0 = fp2_add(XX, XX)
        w = fp2_add(t0, XX)
        t1 = fp2_mul(p.y, p.z)
        s = fp2_add(t1, t1)
        ss = fp2_mul(s, s)
        Z3 = fp2_mul(ss, s)
        R = fp2_mul(p.y, s)
        RR = fp2_mul(R, R)
        t2 = fp2_add(p.x, R)
        t3 = fp2_mul(t2, t2)
        t4 = fp2_sub(t3, XX)
        B = fp2_sub(t4, RR)
        t5 = fp2_mul(w, w)
        t6 = fp2_add(B, B)
        h = fp2_sub(t5, t6)
        X3 = fp2_mul(h, s)
        t7 = fp2_sub(B, h)
        t8 = fp2_mul(w, t7)
        t9 = fp2_add(RR, RR)
        Y3 = fp2_sub(t8, t9)
        return ep2_t(X3,Y3,Z3)

# multiplication
def ep2_mul(p:ep2_t,k:int)->ep2_t: # double and add
    r=p
    for b in bits_of(k)[1:]:
        r=ep2_dbl(r)
        if(b==1):
            r=ep2_add(r,p)
    return ep2_norm(r)

def ep2_mul_naf(p:ep2_t,k:int)->ep2_t: #ep2_mul_naf_imp
    EP_WIDTH=4
    tab=[None]*EP_WIDTH
    tab[0]=ep2_dbl(p)
    tab[1]=ep2_add(tab[0],p)      # = 3p
    tab[2]=ep2_add(tab[1],tab[0]) # = 5p
    tab[3]=ep2_add(tab[2],tab[0]) # = 7p
    tab[0]=ep2_copy(p)             # = p

    for i in range(1,EP_WIDTH):
        tab[i]=ep2_norm(tab[i])

    _k = k % param.r
    naf,naf_len=bn_rec_naf(383,_k,EP_WIDTH)

    r=ep2_t()
    for i in range(naf_len,0,-1):
        r=ep2_dbl(r)
        u=naf[i-1]
        if(u>0):
            r=ep2_add(r,tab[int(u/2)])
        elif(u<0):
            r=ep2_sub(r,tab[int(-u/2)])

    r=ep2_norm(r)
    if(k<0):
        r=ep2_neg(r)
    return r

def ep2_mul_monty(p:ep2_t,k:int)->ep2_t:
    R0=ep2_t()
    R1=ep2_copy(p)
    for kb in bits_of(k):
        if(kb == 0):
            R1 = ep2_add(R0, R1)
            R0 = ep2_dbl(R0)
        if(kb == 1):
            R0 = ep2_add(R0, R1)
            R1 = ep2_dbl(R1)
    return ep2_norm(R0)

# ============================================================
# 2002 Eric Brier and Marc Joye: Weierstraß Elliptic Curves and Side-Channel Attacks
# Chapter 4: Genralizing Montgomery's Technique
# Computing montgomery ladder without y-coordinate
def ep2_add_gen_mon87(p:ep2_t,q:ep2_t,gx:fp2_t)->ep2_t:
    if(ep2_is_infty(p)):
        return ep2_copy(q)
    elif(ep2_is_infty(q)):
        return ep2_copy(p)
    else:
        r=ep2_inf()
        t2=fp2_mul(q.x,p.z)
        t3=fp2_mul(p.z,q.z)
        t4=fp2_mul(p.x,q.z)
        t6=fp2_mul(p.x,q.x)
        t10=fp2_mul(fp2_t(param.curve_a,param.curve_a),t3)
        t12=fp2_add(t4,t2)
        t13=fp2_sub(t4,t2)
        t11=fp2_mul(fp2_t(4*param.curve_b,4*param.curve_b),t3)
        t14=fp2_mul(t13,t13)
        t21=fp2_sub(t6,t10)
        t22=fp2_mul(t21,t21)
        t24=fp2_mul(t11,t12)
        r.z=fp2_mul(gx,t14)
        r.x=fp2_sub(t22,t24)
        return r

def ep2_dbl_gen_mon87(q):
    if(ep2_is_infty(q)):
        return ep2_inf()
    else:
        r=ep2_inf()
        t1=fp2_mul(q.z,q.z)
        t5=fp2_mul(q.x,q.x)
        t7=fp2_mul(q.x,q.z)
        t8=fp2_mul(fp2_t(4*param.curve_b,4*param.curve_b),t1)
        t9=fp2_mul(fp2_t(param.curve_a,param.curve_a),t1)
        t15=fp2_add(t7,t7)
        t16=fp2_mul(t1,t8)
        t17=fp2_mul(t8,t15)
        t18=fp2_add(t5,t9)
        t19=fp2_sub(t5,t9)
        t20=fp2_mul(t15,t18)
        t23=fp2_mul(t19,t19)
        t25=fp2_add(t20,t20)
        r.z=fp2_add(t16,t25)
        r.x=fp2_sub(t23,t17)
        return r

def ep2_recover_y_mon87(x1:fp2_t,x2:fp2_t,gx:fp2_t,gy:fp2_t)->fp2_t:
    yt1=fp2_mul(gx,x1)
    yt2=fp2_add(fp2_t(param.curve_a,param.curve_a),yt1)
    yt3=fp2_add(gx,x1)
    yt4=fp2_mul(yt2,yt3)

    yt5=fp2_sub(gx,x1)
    yt6=fp2_mul(yt5,yt5)
    yt7=fp2_mul(yt6,x2)

    yt8=fp2_add(fp2_t(2*param.curve_b,2*param.curve_b),yt4)
    yt9=fp2_sub(yt8,yt7)

    yt10=fp2_inv(fp2_dbl(gy))

    return fp2_mul(yt9,yt10)

def ep2_mul_gen_mon87(p:ep2_t,k:int)->ep2_t:
    R0=ep2_inf()
    R1=ep2_t(p.x,fp2_t(0,0),p.z)
    gx=p.x
    gy=p.y
    for kb in bits_of(k):
        if(kb == 0):
            R1 = ep2_add_gen_mon87(R1,R0,gx)
            R0 = ep2_dbl_gen_mon87(R0)
        if(kb == 1):
            R0 = ep2_add_gen_mon87(R1,R0,gx)
            R1 = ep2_dbl_gen_mon87(R1)

    #finding y
    R0=ep2_norm(R0)
    R1=ep2_norm(R1)
    R0.y=ep2_recover_y_mon87(R0.x,R1.x,gx,gy)
    return (R0)

# ============================================================
def ep2_rand():
    return ep2_mul(ep2_curve_get_gen(),randrange(param.r))

# ------------------ep2 map from field------------------
# def ep2_map_sswu(t):
#
# def ep2_iso(p:ep2_t):
#
# def ep2_map_from_field(inp_bin:str):
