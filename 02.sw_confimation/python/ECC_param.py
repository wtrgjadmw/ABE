# Import other library
from typing import NamedTuple
from dataclasses import dataclass
from random import randrange
from typing import Tuple, List

# BLS12-381 Parameters
class BLS12_381(NamedTuple):
    # p is max value of interger in prime field
    p:int=0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
    # r is max number of point in curve (curve order)
    r:int=0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001
    # u is special number for BLS curve
    u:int=-0xd201000000010000
    # Curve function: y^2 = x^3 + ax + b
    curve_a: int = 0
    curve_b: int = 4

    mf_R:int = 2**381
    mf_R_inv:int = pow(mf_R, p-2, p)

# ------------------bn functions------------------
# void bn_rec_naf(int8_t *naf, int *len, const bn_t k, int w) {
def bn_rec_naf(max_len:int,k:int,w:int):
    naf=[0]*max_len
    mask=(1 << w)-1 # RLC_MASK(w);
    t=abs(k)
    i=0
    if(w==2):
        while(t!=0):
            if(t%2!=0):
                u_i = 2 - (t & mask)
                if(u_i<0):
                    t=t-u_i
                else:
                    t=t-u_i
                naf[i]=u_i
            else:
                naf[i]=0
            t = t >> 1 # t=int(t/2)
            i=i+1
    else:
        l = 1 << w
        while(t!=0):
            if(t%2!=0):
                u_i = t & mask
                if(u_i>l/2):
                    u_i = int(u_i-l)
                if(u_i<0):
                    t=t-u_i
                else:
                    t=t-u_i
                naf[i]=u_i
            else:
                naf[i]=0
            t = t >> 1 # t=int(t/2)
            i=i+1
    naf_len = i
    return naf,naf_len
