# RELIC fp2 functions
from ECC_param import *
param = BLS12_381()
from ECC_fp import *
# ------------------fp2 class definition------------------
@dataclass
class fp2_t:
    r: int = 0
    i: int = 0

    def __getitem__(self, indices):
        if(indices==0):
            return self.r
        elif(indices==1):
            return self.i
        else:
            raise ValueError('wrong indices type or value')

    def __setitem__(self, indices, value):
        if (not isinstance(value, int)):
            raise TypeError('value must be an fp_t(int)')
        if(indices==0):
            self.r = value
        elif(indices==1):
            self.i = value
        else:
            raise ValueError('wrong indices type or value')
# ------------------fp2 utilities------------------
def fp2_print(x):
    fp_print(x.r)
    fp_print(x.i)

def fp2_print_(x):
    fp2_print_(x.r)
    fp2_print_(x.i)

def fp2_zero():
    return fp2_t(0,0)

def fp2_is_zero(a:fp2_t)->bool:
    return (a.r==0) & (a.i==0)

def fp2_copy(a:fp2_t)->fp2_t:
    c=fp2_zero()
    c[0]=a[0]
    c[1]=a[1]
    return c

def fp2_cmp(a:fp2_t,b:fp2_t)->bool:
    return (a.r==b.r) & (a.i==b.i)

def fp2_rand()->fp2_t:
    return fp2_t(fp_rand(),fp_rand())

# ------------------fp2 arithmatics------------------
def fp2_add(a:fp2_t,b:fp2_t)->fp2_t:
    c0=fp_add(a.r,b.r)
    c1=fp_add(a.i,b.i)
    return fp2_t(c0,c1)

def fp2_neg(a:fp2_t)->fp2_t:
    c0=fp_neg(a.r)
    c1=fp_neg(a.i)
    return fp2_t(c0,c1)

def fp2_sub(a:fp2_t,b:fp2_t)->fp2_t:
    c0=fp_sub(a.r,b.r)
    c1=fp_sub(a.i,b.i)
    return fp2_t(c0,c1)

def fp2_dbl(a:fp2_t)->fp2_t:
    c0=(a.r*2)%param.p
    c1=(a.i*2)%param.p
    return fp2_t(c0,c1)

def fp2_mul(a:fp2_t,b:fp2_t)->fp2_t:
    # Karatsuba
    t2=fp_add(a.r,a.i)
    t1=fp_add(b.r,b.i)
    t3=t2*t1
    t0=a.r*b.r
    t4=a.i*b.i
    t2=t0+t4
    t1=t0-t4
    c0=t1%param.p
    t4=t3-t2
    c1=t4%param.p
    return fp2_t(c0,c1)

def fp2_sqr(a:fp2_t)->fp2_t:
    t0=fp_sqr(a.r)
    t1=fp_sqr(a.i)
    c0=fp_sub(t0,t1)
    c1=fp_mul(2*a.r,a.i)
    return fp2_t(c0,c1)

def fp2_inv(a:fp2_t)->fp2_t:
    t0=fp_sqr(a.r)
    t1=fp_sqr(a.i)
    t0=fp_add(t0,t1)
    t1=fp_inv(t0)

    # c_0 = a_0/(a_0^2 + a_1^2)
    c0=fp_mul(a.r, t1)
    # c_1 = - a_1/(a_0^2 + a_1^2)
    c1=fp_mul(a.i, t1)
    c1=fp_neg(c1)
    return fp2_t(c0,c1)

#def fp2_srt(x):

# ------------------fp2 for pairing------------------
"""
 * Multiplies a quadratic extension field by the quadratic/cubic non-residue.
 * Computes C = A * E, where E is a non-square/non-cube in the quadratic
 * extension.
 *
 * @param[out] C			- the result.
 * @param[in] A				- the quadratic extension field element to multiply.
"""
def fp2_mul_nor(x:fp2_t)->fp2_t:
    # If p = 3 mod 8, (1 + i) is a QNR, i^2 = -1
    # (a_0 + a_1 * i) * (1 + i) = (a_0 - a_1) + (a_0 + a_1) * i
    a=fp_sub(x[0],x[1])
    b=fp_add(x[0],x[1])
    return fp2_t(a,b)

def fp2_frb(a:fp2_t,i:int)->fp2_t:
    c=fp2_zero()
    if(i%2==0):
        c=fp2_copy(a)
    elif(i%2==1):
        c[0]=a[0]
        c[1]=fp_neg(a[1])
    return c

def fp2_mul_frb(a:fp2_t,i:int,j:int)->fp2_t:
    frb_fp2_p1=[fp2_zero(),fp2_zero(),fp2_zero(),fp2_zero(),fp2_zero()]
    frb_fp2_p2=[fp2_zero(),fp2_zero(),fp2_zero(),fp2_zero(),fp2_zero()]

    frb_fp2_p1[0].r=0x1904D3BF02BB0667C231BEB4202C0D1F0FD603FD3CBD5F4F7B2443D784BAB9C4F67EA53D63E7813D8D0775ED92235FB8
    frb_fp2_p1[0].i=0x00FC3E2B36C4E03288E9E902231F9FB854A14787B6C7B36FEC0C8EC971F63C5F282D5AC14D6C7EC22CF78A126DDC4AF3
    frb_fp2_p2[0].r=0
    frb_fp2_p2[0].i=0x0E62DC8741C129371710B9FDD712C786A8FEA21D166C9C2717A49F2A65CEE28DF1CD3DC5FE79031D1343E8551F01B256

    frb_fp2_p1[1].r=0
    frb_fp2_p1[1].i=0x1A0111EA397FE699EC02408663D4DE85AA0D857D89759AD4897D29650FB85F9B409427EB4F49FFFD8BFD00000000AAAC
    frb_fp2_p2[1].r=0x079A25C7A698DB74AFA0A6E674C50EF03B455C473FDCC4A1CA0AAF49F7FD3F028C7AB8CDADFD350168905F0504C0E2BF
    frb_fp2_p2[1].i=0x1266EC2292E70B259B7B00CFCE869DE72931EF3DB3A84E1D9D262356FEB3B721923147310356CAFE516EA0FAFB3EC7EC

    frb_fp2_p1[2].r=0x06AF0E0437FF400B6831E36D6BD17FFE48395DABC2D3435E77F76E17009241C5EE67992F72EC05F4C81084FBEDE3CC09
    frb_fp2_p1[2].i=0x06AF0E0437FF400B6831E36D6BD17FFE48395DABC2D3435E77F76E17009241C5EE67992F72EC05F4C81084FBEDE3CC09
    frb_fp2_p2[2].r=0x01165817155C94451E5D8CE11698CD6ED5B205E5FD54992AE7064F9802C276C1832EF0AE36AC78EA70BCACA7BB9A10BD
    frb_fp2_p2[2].i=0x01165817155C94451E5D8CE11698CD6ED5B205E5FD54992AE7064F9802C276C1832EF0AE36AC78EA70BCACA7BB9A10BD

    frb_fp2_p1[3].r=0x1A0111EA397FE699EC02408663D4DE85AA0D857D89759AD4897D29650FB85F9B409427EB4F49FFFD8BFD00000000AAAD
    frb_fp2_p1[3].i=0
    frb_fp2_p2[3].r=0x079A25C7A698DB74AFA0A6E674C50EF03B455C473FDCC4A1CA0AAF49F7FD3F028C7AB8CDADFD350168905F0504C0E2BF
    frb_fp2_p2[3].i=0x1266EC2292E70B259B7B00CFCE869DE72931EF3DB3A84E1D9D262356FEB3B721923147310356CAFE516EA0FAFB3EC7EC

    frb_fp2_p1[4].r=0x05B2CFD9013A5FD8DF47FA6B48B1E045F39816240C0B8FEE8BEADF4D8E9C0566C63A3E6E257F87329B18FAE980078116
    frb_fp2_p1[4].i=0x144E4211384586C16BD3AD4AFA99CC9170DF3560E77982D0DB45F3536814F0BD5871C1908BD478CD1EE605167FF82995
    frb_fp2_p2[4].r=0x16D4E12F9921A5FD326286FE43690ADC60096D232326A3473673EAD833F98ECE6424E6CFC200714D406F3B647986C421
    frb_fp2_p2[4].i=0x13757AC741E239D345150BE48A7B891C84019EBF72CC3972E7B9DC354B450A945C0A88DA71228D35C9B148F41FAB9022

    if(i==1):
        c=fp2_mul(a,frb_fp2_p1[j-1])
    elif(i==2):
        c=fp2_mul(a,frb_fp2_p2[j-1])
    return c
