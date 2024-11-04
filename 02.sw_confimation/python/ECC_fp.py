# RELIC fp functions
from ECC_param import *
param = BLS12_381()
# ------------------fp utilities------------------
def fp_print(x):
    s = ("{0:#0{1}X}".format(x,98))[2:]
    ss = " ".join(s[i*16:i*16+16] for i in range(6))
    print(ss)

def fp_print_(x):
    print ("{0:#0{1}X}".format(x,98))

def bits_of(x):
    return [int(c) for c in "{0:b}".format(x)]

def fp_sgn0(x):
    return bits_of(x)[-1]

def fp_rand():
    return randrange(param.p)

# ------------------fp arithmatics------------------
def fp_add(x,y):
    return (x+y)%param.p

def fp_neg(x):
    return param.p-x

def fp_sub(x,y):
    return (x-y)%param.p

def fp_mul(x,y):
    return (x*y)%param.p

def fp_sqr(x):
    return (x*x)%param.p

def fp_inv(x):
    return pow(x, param.p-2, param.p)

def fp_srt(x):
    # for finding square root, if prime mod8==3 or ==7 can compute x^((p+1)/4)
    # (p+1)/4 = 0X0680447A8E5FF9A692C6E9ED90D2EB35D91DD2E13CE144AFD9CC34A83DAC3D8907AAFFFFAC54FFFFEE7FBFFFFFFFEAAB
    #         = 0b1101000000001000100011110101000111001011111111110011010011010010010110001101110100111101101100100001101001011101011001101011101100100011101110100101110000100111100111000010100010010101111110110011100110000110100101010000011110110101100001111011000100100000111101010101111111111111111101011000101010011111111111111111110111001111111101111111111111111111111111111111110101010101011
    xx = 0X0680447A8E5FF9A692C6E9ED90D2EB35D91DD2E13CE144AFD9CC34A83DAC3D8907AAFFFFAC54FFFFEE7FBFFFFFFFEAAB
    res = pow(x, xx, param.p)
    if(fp_sqr(res)==x):
        # case correct answer
        return 1,res
    else:
        # case wrong answer
        return 0, None

def fp_hlv(x):
    if(x%2==0):
        return x >> 1
    else:
        return (x+param.p) >> 1
