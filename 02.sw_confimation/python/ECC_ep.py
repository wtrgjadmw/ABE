# RELIC ep functions
from ECC_param import *
param = BLS12_381()
from ECC_fp import *
# ------------------ep class definition------------------
@dataclass
class ep_t:
    x: int = 0
    y: int = 0
    z: int = 0
# ------------------ep utilities------------------
def ep_print(p:ep_t):
    fp_print(p.x)
    fp_print(p.y)
    fp_print(p.z)

def ep_print_(p:ep_t):
    fp_print_(p.x)
    fp_print_(p.y)
    fp_print_(p.z)

def ep_inf()->ep_t:
    return ep_t(0,0,0)

def ep_is_infty(p:ep_t)->bool:
    return (p.x==0) & (p.y==0) & (p.z==0)

def ep_rhs(p:ep_t)->int:
    # Curve function: y^2 = x^3 + ax + b
    yt1=fp_mul(p.x,p.x)
    yt2=fp_add(param.curve_a,yt1)
    yt3=fp_mul(yt2,p.x)
    yt4=fp_add(yt3,param.curve_b)
    return yt4

def ep_on_curve(p:ep_t)->bool:
    rhs=ep_rhs(p)
    lhs=fp_sqr(p.y)
    return (lhs==rhs) or ep_is_infty(p)

def ep_read_bin(bin:str,len:int)->ep_t:
    r=ep_t(0,0,0)
    if(len==194) & (bin[0:2]=='04'):
        r.x = int(RELIC_out[2:98],16)
        r.y = int(RELIC_out[98:],16)
        r.z = 1
    return r

def ep_norm(p:ep_t)->ep_t:
    if ep_is_infty(p):
        return ep_t()
    else:
        zinv=fp_inv(p.z)
        x=fp_mul(p.x,zinv)
        y=fp_mul(p.y,zinv)
        return ep_t(x,y,1)

def ep_copy(p:ep_t)->ep_t:
    return ep_t(p.x,p.y,p.z)

def ep_cmp(p:ep_t,q:ep_t)->bool:
    return (p.x==q.x) & (p.y==q.y) & (p.z==q.z)

def ep_curve_get_gen()->ep_t:
    x=0x17F1D3A73197D7942695638C4FA9AC0FC3688C4F9774B905A14E3A3F171BAC586C55E83FF97A1AEFFB3AF00ADB22C6BB
    y=0x08B3F481E3AAA0F1A09E30ED741D8AE4FCF5E095D5D00AF600DB18CB2C04B3EDD03CC744A2888AE40CAA232946C5E7E1
    return ep_t(x,y,1)

# ------------------ep arithmatics------------------
def ep_add(p:ep_t,q:ep_t)->ep_t: #ep_add_projc_imp
    if(ep_is_infty(p)):
        return q
    elif(ep_is_infty(q)):
        return p
    else:
        r=ep_t()
        t0=fp_mul(p.x,q.x)
        t1=fp_mul(p.y,q.y)
        t2=fp_mul(p.z,q.z)
        t3=fp_add(p.x,p.y)
        t4=fp_add(q.x,q.y)
        t3=fp_mul(t3,t4)
        t4=fp_add(t0,t1)
        t3=fp_sub(t3,t4)
        # (ep_curve_opt_a() == RLC_ZERO)
        # /* Cost of 12M + 2m_3b + 19a. */
        t4=fp_add(p.y,p.z)
        t5=fp_add(q.y,q.z)
        t4=fp_mul(t4,t5)
        t5=fp_add(t1,t2)
        t4=fp_sub(t4,t5)
        r.y=fp_add(q.x,q.z)
        r.x=fp_add(p.x,p.z)
        r.x=fp_mul(r.x,r.y)
        r.y=fp_add(t0,t2)
        r.y=fp_sub(r.x,r.y)
        r.x=fp_add(t0,t0) #fp_dbl
        t0=fp_add(t0,r.x)
        t2=fp_mul(t2,0xC)
        r.z=fp_add(t1,t2)
        t1=fp_sub(t1,t2)
        r.y=fp_mul(r.y,0xC)
        r.x=fp_mul(t4,r.y)
        t2=fp_mul(t3,t1)
        r.x=fp_sub(t2,r.x)
        r.y=fp_mul(t0,r.y)
        t1=fp_mul(t1,r.z)
        r.y=fp_add(t1,r.y)
        t0=fp_mul(t0,t3)
        r.z=fp_mul(r.z,t4)
        r.z=fp_add(r.z,t0)
        return r

def ep_neg(p:ep_t)->ep_t:
    if(ep_is_infty(p)):
        return ep_t()
    else:
        return ep_t(p.x,fp_neg(p.y),p.z)

def ep_sub(p:ep_t,q:ep_t)->ep_t:
    if(ep_cmp(p,q)):
        return ep_t()
    else:
        t=ep_neg(q)
        return ep_add(p,t)

def ep_dbl(p:ep_t)->ep_t: # need fix
    if(ep_is_infty(p)):
        return ep_t()
    else:
        return ep_add(p,p)

# multiplication
def ep_mul(p:ep_t,k:int)->ep_t: # double and add
    r=ep_copy(p)
    for b in bits_of(k)[1:]:
        r=ep_dbl(r)
        if(b==1):
            r=ep_add(r,p)
    return ep_norm(r)

def ep_mul_naf(p:ep_t,k:int)->ep_t: #ep_mul_naf_imp
    EP_WIDTH=4
    tab=[None]*EP_WIDTH
    tab[0]=ep_dbl(p)
    tab[1]=ep_add(tab[0],p)      # = 3p
    tab[2]=ep_add(tab[1],tab[0]) # = 5p
    tab[3]=ep_add(tab[2],tab[0]) # = 7p
    tab[0]=p                     # = p
    for i in range(1,EP_WIDTH):
        tab[i]=ep_norm(tab[i])

    _k = k % param.r
    naf,naf_len=bn_rec_naf(383,_k,EP_WIDTH)

    r=ep_t()
    for i in range(naf_len,0,-1):
        r=ep_dbl(r)
        u=naf[i-1]
        if(u>0):
            r=ep_add(r,tab[int(u/2)])
        elif(u<0):
            r=ep_sub(r,tab[int(-u/2)])

    r=ep_norm(r)
    if(k<0):
        r=ep_neg(r)
    return r

def ep_mul_monty(p:ep_t,k:int)->ep_t:
    R0=ep_t()
    R1=p
    for kb in bits_of(k):
        if(kb == 0):
            R1 = ep_add(R0, R1)
            R0 = ep_dbl(R0)
        if(kb == 1):
            R0 = ep_add(R0, R1)
            R1 = ep_dbl(R1)
    return ep_norm(R0)

# ============================================================
# 2002 Eric Brier and Marc Joye: Weierstraß Elliptic Curves and Side-Channel Attacks
# Chapter 4: Genralizing Montgomery's Technique
# Computing montgomery ladder without y-coordinate
def ep_add_gen_mon87(p:ep_t,q:ep_t,gx:int)->ep_t:
    r=ep_inf()
    if(ep_is_infty(p)):
        r=ep_copy(q)
    elif(ep_is_infty(q)):
        r=ep_copy(p)
    else:
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

def ep_dbl_gen_mon87(p:ep_t):
    r=ep_inf()
    if(not ep_is_infty(p)):
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

def ep_recover_y_mon87(x1:int,x2:int,gx:int,gy:int)->int:
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

def ep_mul_gen_mon87(p:ep_t,k:int)->ep_t:
    R0=ep_inf()
    R1=ep_t(p.x,0,p.z)
    gx=p.x
    gy=p.y
    for kb in bits_of(k):
        if(kb == 0):
            R1 = ep_add_gen_mon87(R1,R0,gx)
            R0 = ep_dbl_gen_mon87(R0)
        if(kb == 1):
            R0 = ep_add_gen_mon87(R1,R0,gx)
            R1 = ep_dbl_gen_mon87(R1)

    #finding y
    R0=ep_norm(R0)
    R1=ep_norm(R1)
    R0.y=ep_recover_y_mon87(R0.x,R1.x,gx,gy)
    return (R0)

# ============================================================
def ep_rand()->ep_t:
    return ep_mul(ep_curve_get_gen(),randrange(param.r))

# ------------------ep map from field------------------
def ep_map_sswu(t):
    ep_map_c0 = 0x0793154FD85631D966EF2470460C78F6A928AD9F5BDBFAC21DF39753AA278BA751BDFCF95A84188E29D670675E4C9C7C
    ep_map_c2 = 0x00144698A3B8E9433D693A02C96D4982B0EA985383EE66A8D8E8981AEFD881AC98936F8DA0E0F97F5CF428082D584C1D
    ep_map_c3 = 0x12E2908D11688030018B12E8753EEE3B2016C1F0F24F4070A0B9C14FCEF35EF55A23215A316CEAA5D1CC48E98E172BE0
    ep_map_u = 0x0B
    t0 = fp_sqr(t)
    t0=fp_mul(t0,ep_map_u)
    t1=fp_sqr(t0)
    t2=fp_add(t1,t0)
    if(t2!=0):
        t2=fp_inv(t2)
        t2=t2+1 #t2=(1 + 1 / (u^2 * t^4 + u * t^2))
    else:
        t2=fp_inv(fp_neg(ep_map_u)) #t2=-1/u
    x=fp_mul(ep_map_c0,t2)
    y=fp_sqr(x)
    y=fp_add(y,ep_map_c2)
    y=fp_mul(y,x)
    y=fp_add(y,ep_map_c3)

    t2=fp_mul(t0,x)
    t1=fp_mul(t0,t1)
    t3=fp_mul(t1,y)

    chk,y=fp_srt(y)
    if(chk==0):
        x=t2
        _chk,y=fp_srt(t3)

    return ep_t(x,y,1)

def ep_iso(p:ep_t):
    deg_xn=12
    deg_yn=16
    deg_xd=11
    deg_yd=16

    coef_xn=[None]*deg_xn
    coef_yn=[None]*deg_yn
    coef_xd=[None]*deg_xd
    coef_yd=[None]*deg_yd

    coef_xn[11]=0x06E08C248E260E70BD1E962381EDEE3D31D79D7E22C837BC23C0BF1BC24C6B68C24B1B80B64D391FA9C8BA2E8BA2D229
    coef_xn[10]=0x10321DA079CE07E272D8EC09D2565B0DFA7DCCDDE6787F96D50AF36003B14866F69B771F8C285DECCA67DF3F1605FB7B
    coef_xn[9]=0x169B1F8E1BCFA7C42E0C37515D138F22DD2ECB803A0C5C99676314BAF4BB1B7FA3190B2EDC0327797F241067BE390C9E
    coef_xn[8]=0x080D3CF1F9A78FC47B90B33563BE990DC43B756CE79F5574A2C596C928C5D1DE4FA295F296B74E956D71986A8497E317
    coef_xn[7]=0x17B81E7701ABDBE2E8743884D1117E53356DE5AB275B4DB1A682C62EF0F2753339B7C8F8C8F475AF9CCB5618E3F0C88E
    coef_xn[6]=0x0D6ED6553FE44D296A3726C38AE652BFB11586264F0F8CE19008E218F9C86B2A8DA25128C1052ECADDD7F225A139ED84
    coef_xn[5]=0x1630C3250D7313FF01D1201BF7A74AB5DB3CB17DD952799B9ED3AB9097E68F90A0870D2DCAE73D19CD13C1C66F652983
    coef_xn[4]=0x0E99726A3199F4436642B4B3E4118E5499DB995A1257FB3F086EEB65982FAC18985A286F301E77C451154CE9AC8895D9
    coef_xn[3]=0x1778E7166FCC6DB74E0609D307E55412D7F5E4656A8DBF25F1B33289F1B330835336E25CE3107193C5B388641D9B6861
    coef_xn[2]=0x0D54005DB97678EC1D1048C5D10A9A1BCE032473295983E56878E501EC68E25C958C3E3D2A09729FE0179F9DAC9EDCB0
    coef_xn[1]=0x17294ED3E943AB2F0588BAB22147A81C7C17E75B2F6A8417F565E33C70D1E86B4838F2A6F318C356E834EEF1B3CB83BB
    coef_xn[0]=0x11A05F2B1E833340B809101DD99815856B303E88A2D7005FF2627B56CDB4E2C85610C2D5F2E62D6EAEAC1662734649B7

    coef_yn[15]=0x15E6BE4E990F03CE4EA50B3B42DF2EB5CB181D8F84965A3957ADD4FA95AF01B2B665027EFEC01C7704B456BE69C8B604
    coef_yn[14]=0x05C129645E44CF1102A159F748C4A3FC5E673D81D7E86568D9AB0F5D396A7CE46BA1049B6579AFB7866B1E715475224B
    coef_yn[13]=0x0245A394AD1ECA9B72FC00AE7BE315DC757B3B080D4C158013E6632D3C40659CC6CF90AD1C232A6442D9D3F5DB980133
    coef_yn[12]=0x0B182CAC101B9399D155096004F53F447AA7B12A3426B08EC02710E807B4633F06C851C1919211F20D4C04F00B971EF8
    coef_yn[11]=0x18B46A908F36F6DEB918C143FED2EDCC523559B8AAF0C2462E6BFE7F911F643249D9CDF41B44D606CE07C8A4D0074D8E
    coef_yn[10]=0x19713E47937CD1BE0DFD0B8F1D43FB93CD2FCBCB6CAF493FD1183E416389E61031BF3A5CCE3FBAFCE813711AD011C132
    coef_yn[9]=0x0E1BBA7A1186BDB5223ABDE7ADA14A23C42A0CA7915AF6FE06985E7ED1E4D43B9B3F7055DD4EBA6F2BAFAAEBCA731C30
    coef_yn[8]=0x09FC4018BD96684BE88C9E221E4DA1BB8F3ABD16679DC26C1E8B6E6A1F20CABE69D65201C78607A360370E577BDBA587
    coef_yn[7]=0x0987C8D5333AB86FDE9926BD2CA6C674170A05BFE3BDD81FFD038DA6C26C842642F64550FEDFE935A15E4CA31870FB29
    coef_yn[6]=0x04AB0B9BCFAC1BBCB2C977D027796B3CE75BB8CA2BE184CB5231413C4D634F3747A87AC2460F415EC961F8855FE9D6F2
    coef_yn[5]=0x16603FCA40634B6A2211E11DB8F0A6A074A7D0D4AFADB7BD76505C3D3AD5544E203F6326C95A807299B23AB13633A5F0
    coef_yn[4]=0x08CC03FDEFE0FF135CAF4FE2A21529C4195536FBE3CE50B879833FD221351ADC2EE7F8DC099040A841B6DAECF2E8FEDB
    coef_yn[3]=0x01F86376E8981C217898751AD8746757D42AA7B90EEB791C09E4A3EC03251CF9DE405ABA9EC61DECA6355C77B0E5F4CB
    coef_yn[2]=0x00CC786BAA966E66F4A384C86A3B49942552E2D658A31CE2C344BE4B91400DA7D26D521628B00523B8DFE240C72DE1F6
    coef_yn[1]=0x134996A104EE5811D51036D776FB46831223E96C254F383D0F906343EB67AD34D6C56711962FA8BFE097E75A2E41C696
    coef_yn[0]=0x090D97C81BA24EE0259D1F094980DCFA11AD138E48A869522B52AF6C956543D3CD0C7AEE9B3BA3C2BE9845719707BB33

    coef_xd[10]=0x1
    coef_xd[9]=0x095FC13AB9E92AD4476D6E3EB3A56680F682B4EE96F7D03776DF533978F31C1593174E4B4B7865002D6384D168ECDD0A
    coef_xd[8]=0x0A10ECF6ADA54F825E920B3DAFC7A3CCE07F8D1D7161366B74100DA67F39883503826692ABBA43704776EC3A79A1D641
    coef_xd[7]=0x14A7AC2A9D64A8B230B3F5B074CF01996E7F63C21BCA68A81996E1CDF9822C580FA5B9489D11E2D311F7D99BBDCC5A5E
    coef_xd[6]=0x0772CAACF16936190F3E0C63E0596721570F5799AF53A1894E2E073062AEDE9CEA73B3538F0DE06CEC2574496EE84A3A
    coef_xd[5]=0x0E7355F8E4E667B955390F7F0506C6E9395735E9CE9CAD4D0A43BCEF24B8982F7400D24BC4228F11C02DF9A29F6304A5
    coef_xd[4]=0x13A8E162022914A80A6F1D5F43E7A07DFFDFC759A12062BB8D6B44E833B306DA9BD29BA81F35781D539D395B3532A21E
    coef_xd[3]=0x03425581A58AE2FEC83AAFEF7C40EB545B08243F16B1655154CCA8ABC28D6FD04976D5243EECF5C4130DE8938DC62CD8
    coef_xd[2]=0x0B2962FE57A3225E8137E629BFF2991F6F89416F5A718CD1FCA64E00B11ACEACD6A3D0967C94FEDCFCC239BA5CB83E19
    coef_xd[1]=0x12561A5DEB559C4348B4711298E536367041E8CA0CF0800C0126C2588C48BF5713DAA8846CB026E9E5C8276EC82B3BFF
    coef_xd[0]=0x08CA8D548CFF19AE18B2E62F4BD3FA6F01D5EF4BA35B48BA9C9588617FC8AC62B558D681BE343DF8993CF9FA40D21B1C

    coef_yd[15]=0x1
    coef_yd[14]=0x0E0FA1D816DDC03E6B24255E0D7819C171C40F65E273B853324EFCD6356CAA205CA2F570F13497804415473A1D634B8F
    coef_yd[13]=0x02660400EB2E4F3B628BDD0D53CD76F2BF565B94E72927C1CB748DF27942480E420517BD8714CC80D1FADC1326ED06F7
    coef_yd[12]=0x0AD6B9514C767FE3C3613144B45F1496543346D98ADF02267D5CEEF9A00D9B8693000763E3B90AC11E99B138573345CC
    coef_yd[11]=0x0ACCBB67481D033FF5852C1E48C50C477F94FF8AEFCE42D28C0F9A88CEA7913516F968986F7EBBEA9684B529E2561092
    coef_yd[10]=0x04D2F259EEA405BD48F010A01AD2911D9C6DD039BB61A6290E591B36E636A5C871A5C29F4F83060400F8B49CBA8F6AA8
    coef_yd[9]=0x167A55CDA70A6E1CEA820597D94A84903216F763E13D87BB5308592E7EA7D4FBC7385EA3D529B35E346EF48BB8913F55
    coef_yd[8]=0x1866C8ED336C61231A1BE54FD1D74CC4F9FB0CE4C6AF5920ABC5750C4BF39B4852CFE2F7BB9248836B233D9D55535D4A
    coef_yd[7]=0x16A3EF08BE3EA7EA03BCDDFABBA6FF6EE5A4375EFA1F4FD7FEB34FD206357132B920F5B00801DEE460EE415A15812ED9
    coef_yd[6]=0x166007C08A99DB2FC3BA8734ACE9824B5EECFDFA8D0CF8EF5DD365BC400A0051D5FA9C01A58B1FB93D1A1399126A775C
    coef_yd[5]=0x08D9E5297186DB2D9FB266EAAC783182B70152C65550D881C5ECD87B6F0F5A6449F38DB9DFA9CCE202C6477FAAF9B7AC
    coef_yd[4]=0x0BE0E079545F43E4B00CC912F8228DDCC6D19C9F0F69BBB0542EDA0FC9DEC916A20B15DC0FD2EDEDDA39142311A5001D
    coef_yd[3]=0x16B7D288798E5395F20D23BF89EDB4D1D115C5DBDDBCD30E123DA489E726AF41727364F2C28297ADA8D26D98445F5416
    coef_yd[2]=0x058DF3306640DA276FAAAE7D6E8EB15778C4855551AE7F310C35A5DD279CD2ECA6757CD636F96F891E2538B53DBF67F2
    coef_yd[1]=0x1962D75C2381201E1A0CBD6C43C348B885C84FF731C4D59CA4A10356F453E01F78A4260763529E3532F6102C2E49A03D
    coef_yd[0]=0x16112C4C3A9C98B252181140FAD0EAE9601A6DE578980BE6EEC3232B5BE72E7A07F3688EF60C206D01479253B03663C1

    t0=coef_xn[deg_xn-1]
    for i in range(deg_xn-1,0,-1):
        t0=fp_mul(t0,p.x)
        t0=fp_add(t0,coef_xn[i-1])
    t1=coef_yn[deg_yn-1]
    for i in range(deg_yn-1,0,-1):
        t1=fp_mul(t1,p.x)
        t1=fp_add(t1,coef_yn[i-1])
    t2=coef_yd[deg_yd-1]
    for i in range(deg_yd-1,0,-1):
        t2=fp_mul(t2,p.x)
        t2=fp_add(t2,coef_yd[i-1])
    t3=coef_xd[deg_xd-1]
    for i in range(deg_xd-1,0,-1):
        t3=fp_mul(t3,p.x)
        t3=fp_add(t3,coef_xd[i-1])

    #PROJ coord for "fp"
    zo=fp_mul(t2,t3)
    xo=fp_mul(t0,t2)
    yo=fp_mul(p.y,t1)
    yo=fp_mul(yo,t3)

    return ep_t(xo,yo,zo)

def ep_map_from_field(inp_bin:str):
    len_per_elm = 64*2 # *2 because 1 byte = 2 hex character

    # First map invocation
    fp1=int(inp_bin[0:len_per_elm],16)%param.p
    p=ep_map_sswu(fp1)
    if(fp_sgn0(fp1)!=fp_sgn0(p.y)):
        p.y=fp_neg(p.y)
    p=ep_iso(p)
    # Second map invocation
    fp2=int(inp_bin[len_per_elm:2*len_per_elm],16)%param.p
    q=ep_map_sswu(fp2)
    if(fp_sgn0(fp2)!=fp_sgn0(q.y)):
        q.y=fp_neg(q.y)
    q=ep_iso(q)
    # Sum the result
    r=ep_add(p,q)
    r=ep_norm(r)
    # Clear cofactor
    r=ep_mul(r,-param.u+1)
    return r
