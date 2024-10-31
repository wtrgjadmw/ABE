from field import Fp
from point import PointFp
from constants import *

"""
def sign(t, num):
    #num is Fp and in montmode
    assert type(t) == int and type(num) == field.Fp
    assert num.is_mont == 1
    num_notmont = num.value_
    if t % 2 == num_notmont % 2:
        return num
    else
        return zero - num"""

def SSWU_before_isogney(t, mont_flag = 0):

    # prepare t as Fp in montmode------------------
    #input t as integer and not in mont mode
    assert type(t) == int and mont_flag == 0
    original_t = t
    t_mont = Fp(t, mont_flag)
    t_mont.Mont_change()
    #----------------------------------------------

    t2 = t_mont ** 2
    t4 = t_mont ** 4
    z2 = z_mont ** 2
    z2t4 = z2 * t4
    zt2 = z_mont * t2
    D_ = z2t4 + zt2
    N_ = D_ + one
    N = b * N_
    D = D_ * nega
    # branch, if denominator is zero then change it-------
    if(D.value == 0):
        print("branch: denominator is zero")
        D = a * z_mont
    # branch end -----------------------------------------
    D2 = D ** 2
    D3 = D ** 3
    N2 = N ** 2
    N3 = N ** 3
    ND2 = N * D2
    aND2 = a * ND2
    bD3 = b * D3
    U = N3 + aND2 + bD3
    V = D3
    V2 = V ** 2
    UV = U * V
    UV3 = UV * V2
    
    #for 2-k ary exponentiation, k = 3------------------
    """
    UV_list = []
    for i in range(1, 8):
        UV_list.append(UV3 ** i)
    """
    #---------------------------------------------------

    UV3_exp = UV3 ** ((UV3.p - 3) // 4)
    alpha = UV3_exp * UV
    alpha2 = alpha ** 2
    alpha2V = alpha2 * V
    ND = N * D
    alphaD3 = alpha * D3
    signedy1 = alpha.sign(original_t)
    y1 = signedy1 * D3
    zt2ND = zt2 * ND
    t3 = t_mont ** 3
    z3 = z_mont ** 3
    negz3 = zero - z3
    y2 = alpha * sqrt_negz3 * t3
    signed_y2 = y2.sign(original_t)
    y2 = signed_y2 * D3
    if(alpha2V.value == U.value):
        mapped_point = PointFp(ND, y1, D)
        mapped_point.on_curve(a, b)
        

    else:
        mapped_point = PointFp(zt2ND, y2, D)
        mapped_point.on_curve(a, b)
        
    mapped_point.X.pr("newX")
    mapped_point.Y.pr("newY")
    mapped_point.Z.pr("newZ")
    return mapped_point

def isogeny(mapped_point):
    X = mapped_point.X
    Y = mapped_point.Y
    Z = mapped_point.Z
    #computing Nx
    Nx = zero
    Dx = zero
    Ny = zero
    Dy = zero
    for i in range(len(mont_K_list[0])):
        Nx += mont_K_list[0][i] * (Z ** (22 - 2 * i)) * (X ** i)
    for i in range(len(mont_K_list[1])):
        Dx += mont_K_list[1][i] * (Z ** (20 - 2 * i)) * (X ** i)
    Dx = Dx * (Z ** 2)
    for i in range(len(mont_K_list[2])):
        Ny += mont_K_list[2][i] * (Z ** (30 - 2 * i)) * (X ** i)
    Ny = Ny * Y
    for i in range(len(mont_K_list[3])):
        Dy += mont_K_list[3][i] * (Z ** (30 - 2 * i)) * (X ** i)
    Dy = Dy * (Z ** 3)

    #return values in Jacobian coordinates
    Z0 = Dx * Dy
    X0 = Nx * Dy * Z0
    Y0 = Ny * Dx * (Z0 ** 2)
    after_isogeny_point = PointFp(X0, Y0, Z0)
    after_isogeny_point.on_curve()
    return after_isogeny_point

def SSWU_and_isogeny(t):
    mapped_point = SSWU_before_isogney(t)
    result = isogeny(mapped_point)
    result.X.pr("resultX")
    result.Y.pr("resultY")
    result.Z.pr("resultZ")
    return result

def encode_to_curve(t):
    point_after_isogeny = SSWU_and_isogeny(t)
    point_after_isogeny.change_to("p")
    point_on_g1 = point_after_isogeny.scalar_mul(heff)
    point_on_g1.subgroup_check(point_on_g1.r)
    return point_on_g1

def hash_to_curve(t1, t2):
    mapped_point1 = SSWU_and_isogeny(t1)
    mapped_point2 = SSWU_and_isogeny(t2)
    print(mapped_point1.coord)
    mapped_point1.pr("point1")
    mapped_point2.pr("point2")
    #mapped_point1.change_to("p")
    #mapped_point2.change_to("p")
    after_isogeny_point = mapped_point1 + mapped_point2
    after_isogeny_point.pr("after_isogeny_point")
    return
    point_on_g1 = after_isogeny_point.scalar_mul(heff)
    point_on_g1.subgroup_check(point_on_g1.r)
    return point_on_g1

def hash_to_curve_change_coordinate(t1, t2):
    mapped_point1 = SSWU_and_isogeny(t1)
    mapped_point2 = SSWU_and_isogeny(t2)
    mapped_point1.change_to("p")
    mapped_point2.change_to("p")
    after_isogeny_point = mapped_point1 + mapped_point2
    point_on_g1 = after_isogeny_point.scalar_mul(heff)
    point_on_g1.subgroup_check(point_on_g1.r)
    return point_on_g1

u0 = 0x0ba14bd907ad64a016293ee7c2d276b8eae71f25a4b941eece7b0d89f17f75cb3ae5438a614fb61d6835ad59f29c564f
u1 = 0x019b9bd7979f12657976de2884c7cce192b82c177c80e0ec604436a7f538d231552f0d96d9f7babe5fa3b19b3ff25ac9

assert len(u0_list) == len(u1_list)
assert len(u0_list) == len(hash_to_curve_result_list)
for i in range(len(u0_list)):
    print("-----------------------------------------------------------")
    print("index:", i)
    u0 = u0_list[i]
    u1 = u1_list[i]
    correct_result_x = hash_to_curve_result_list[i][0]
    correct_result_y = hash_to_curve_result_list[i][1]
    print("correct_x:", hex(correct_result_x))
    print("correct_y:", hex(correct_result_y))
    result = hash_to_curve(u0, u0)
    result_x, result_y = result.affine_coordinates()
    result_x.pr("result_x")
    result_y.pr("result_y")
    assert correct_result_x == result_x.value
    assert correct_result_y == result_y.value
