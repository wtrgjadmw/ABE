# RELIC ep functions
from ECC_param import *
param = BLS12_381()
from ECC_fp import *
from ECC_ep import *
# ------------------????------------------
def bits_of_256(x):
    return [int(c) for c in "{0:0{1}b}".format(x,256)]

def fp_inv_mont(x):
    e=param.p-2
    a1=x
    a2=fp_mul(x,x)
    for kb in bits_of(e)[1:]:
        if(kb == 0):
            a2 = fp_mul(a1,a2)
            a1 = fp_mul(a1,a1)
        if(kb == 1):
            a1 = fp_mul(a1,a2)
            a2 = fp_mul(a2,a2)
    return a1

# ------------------????------------------
def ep_add_SM17(p:ep_t,q:ep_t,x_og:int)->ep_t: # q-p = (x_og,y_og)
    r1=(p.x)
    r2=(p.z)
    r3=(q.x)
    r4=(q.z)

    r6=fp_mul(r1,r4)
    r7=fp_mul(r1,r3)
    r5=fp_mul(r2,r4)
    r8=fp_mul(r3,r2)
    r3=fp_sub(r6,r8)
    r4=fp_mul(r3,r3)
    r3=fp_mul(x_og,r4)
    r8=fp_add(r8,r6)
    r6=fp_mul(param.curve_a,r5)
    r7=fp_add(r7,r6)
    r7=fp_mul(r7,r8)
    r5=fp_mul(r5,r5)
    r6=fp_mul(4*param.curve_b,r5)
    r7=fp_add(r7,r7)
    r7=fp_add(r7,r6)
    r3=fp_sub(r7,r3)

    x3=(r3)
    z3=(r4)
    r=ep_t(x3,0,z3)
    return r

def ep_dbl_SM17(p:ep_t)->ep_t:
    r1=(p.x)
    r2=(p.z)

    r7=fp_mul(r2,r2)
    r5=fp_mul(param.curve_a,r7)
    r8=fp_mul(r1,r1)
    r6=fp_add(r8,r5)
    r5=fp_sub(r8,r5)
    r5=fp_mul(r5,r5)
    r6=fp_mul(r1,r6)
    r7=fp_mul(4*param.curve_b,r7)
    r7=fp_mul(r7,r2)
    r8=fp_mul(r1,r7)
    r8=fp_add(r8,r8)
    r1=fp_sub(r5,r8)
    r6=fp_add(r6,r6)
    r6=fp_add(r6,r6)
    r6=fp_add(r6,r7)
    r2=fp_mul(r2,r6)

    x2=(r1)
    z2=(r2)
    r=ep_t(x2,0,z2)
    return r

def ep_recover_y_SM17(p:ep_t,q:ep_t,x_og:int,y_og:int)->int: # q-p = (x_og,y_og)
    x0=p.x
    z0=p.z
    x1=q.x
    z1=q.z

    r1=fp_mul(z1,z0)
    r2=fp_add(r1,r1) # 2z1z0
    #----------------
    r3=fp_mul(y_og,r2) # 2(yQ)z1z0
    x0p=fp_mul(r3,x0)
    z0p=fp_mul(r3,z0)
    #----------------
    r3=fp_mul(param.curve_b,r2)
    y0p_1=fp_mul(z0,r3) #2bz1z0z0
    r4=fp_mul(z0,x_og)
    r5=fp_mul(x0,x_og)
    r6=fp_mul(z0,param.curve_a)
    r7=fp_add(r6,r5)
    r8=fp_add(r4,x0)
    r9=fp_mul(z1,r7)
    y0p_2=fp_mul(r9,r8)
    r10=fp_sub(r4,x0)
    r11=fp_mul(r10,r10)
    y0p_3=fp_mul(r11,x1)
    r12=fp_add(y0p_1,y0p_2)
    y0p=fp_sub(r12,y0p_3)

    z0p_inv=fp_inv(z0p)

    x_recov=fp_mul(x0p,z0p_inv)
    y_recov=fp_mul(y0p,z0p_inv)
    return ep_t(x_recov,y_recov,1)

def ep_mul_SM17(p:ep_t,k:int)->ep_t:
    R0=ep_inf()
    R0.x=1
    R1=ep_t(p.x,0,p.z)
    x_og=p.x
    y_og=p.y
    for kb in bits_of_256(k):
        if(kb == 0):
            R1 = ep_add_SM17(R0,R1,x_og)
            R0 = ep_dbl_SM17(R0)
        if(kb == 1):
            R0 = ep_add_SM17(R0,R1,x_og)
            R1 = ep_dbl_SM17(R1)


    #finding y
    R=ep_recover_y_SM17(R0,R1,x_og,y_og)
    return (R)

# ------------------????------------------
def ep_add_BJ02(p:ep_t,q:ep_t,gx:int)->ep_t: # p-q = (x_og,y_og)
    r=ep_inf()
    t2=fp_mul(q.x,p.z)
    t3=fp_mul(p.z,q.z)
    t4=fp_mul(p.x,q.z)
    t6=fp_mul(p.x,q.x)
    t10=fp_mul(param.curve_a,t3)
    t12=fp_add(t4,t2)
    t13=fp_sub(t4,t2)
    t11=fp_mul(4*param.curve_b,t3)
    t14=fp_mul(t13,t13)
    t21=fp_sub(t6,t10)
    t22=fp_mul(t21,t21)
    t24=fp_mul(t11,t12)
    r.z=fp_mul(gx,t14)
    r.x=fp_sub(t22,t24)
    return r

def ep_dbl_BJ02(p:ep_t):
    r=ep_inf()
    t1=fp_mul(p.z,p.z)
    t5=fp_mul(p.x,p.x)
    t7=fp_mul(p.x,p.z)
    t8=fp_mul(4*param.curve_b,t1)
    t9=fp_mul(param.curve_a,t1)
    t15=fp_add(t7,t7)
    t16=fp_mul(t1,t8)
    t17=fp_mul(t8,t15)
    t18=fp_add(t5,t9)
    t19=fp_sub(t5,t9)
    t20=fp_mul(t15,t18)
    t23=fp_mul(t19,t19)
    t25=fp_add(t20,t20)
    r.z=fp_add(t16,t25)
    r.x=fp_sub(t23,t17)
    return r

def ep_recover_y_BJ02(x1:int,x2:int,gx:int,gy:int)->int:
    yt1=fp_mul(gx,x1)
    yt2=fp_add(param.curve_a,yt1)
    yt3=fp_add(gx,x1)
    yt4=fp_mul(yt2,yt3)

    yt5=fp_sub(gx,x1)
    yt6=fp_mul(yt5,yt5)
    yt7=fp_mul(yt6,x2)

    yt8=fp_add(2*param.curve_b,yt4)
    yt9=fp_sub(yt8,yt7)

    yt10=fp_inv(2*gy)

    return fp_mul(yt9,yt10)

def ep_mul_BJ02(p:ep_t,k:int)->ep_t:
    R0=ep_inf()
    R0.x=1
    R1=ep_t(p.x,0,p.z)
    gx=p.x
    gy=p.y
    for kb in bits_of_256(k):
        if(kb == 0):
            R1 = ep_add_BJ02(R1,R0,gx)
            R0 = ep_dbl_BJ02(R0)
        if(kb == 1):
            R0 = ep_add_BJ02(R1,R0,gx)
            R1 = ep_dbl_BJ02(R1)

    #finding y
    R0=ep_norm(R0)
    R1=ep_norm(R1)
    R0.y=ep_recover_y_BJ02(R0.x,R1.x,gx,gy)
    return (R0)

# ------------------????------------------
def ep_mul_BJ02_SM17(p:ep_t,k:int)->ep_t:
    R0=ep_inf()
    R0.x=1
    R1=ep_t(p.x,0,p.z)
    gx=p.x
    gy=p.y
    for kb in bits_of_256(k):
        if(kb == 0):
            R1 = ep_add_BJ02(R1,R0,gx)
            R0 = ep_dbl_BJ02(R0)
        if(kb == 1):
            R0 = ep_add_BJ02(R1,R0,gx)
            R1 = ep_dbl_BJ02(R1)

    #finding y
    R=ep_recover_y_SM17(R0,R1,gx,gy)
    return (R)
