from constants import *
from h2f import hash_to_field

# map_to_curve(u)
# Input: u, an element of field F.
# Output: Q, a point on the elliptic curve E.
# Steps: defined in Section 6.


# Simplified SWU for AB == 0:
# 1. (x', y') = map_to_curve_simple_swu(u) # (x', y') is on E'
# 2. (x, y) = iso_map(x', y') # (x, y) is on E
# 3. return (x, y)

# map_to_curve_simple_swu algorithm is referenced from chapter 4.2 of 
# Wahby, R. S., & Boneh, D. (2019). "Fast and simple constant-time hashing
# to the BLS12-381 elliptic curve". Cryptology ePrint Archive.

h2c_exponent = 0x680447a8e5ff9a692c6e9ed90d2eb35d91dd2e13ce144afd9cc34a83dac3d8907aaffffac54ffffee7fbfffffffeaaa

# xi = Fp(11)
# print((zero-(xi**3)).value)
# sqrt_negxi3, is_sqr = (zero-(xi**3)).sqrt()
# print((sqrt_negxi3**2).value)
# print((sqrt_negxi3).value)

def g(x):
    return x**3 + A_*x + B_

negA = xi * A_
half_p_1 = (p - 1) // 2

def SSWU_before_isogeny(t_: int) -> pointFp:
    if t_ == 0 or t_ == 1 or t_ == -1:
        raise Exception("value t is %d" % t)
    t = Fp(t_)

    t2 = t * t
    xit2 = xi * t2
    xi2t4 = xit2 * xit2
    D_a_ = xi2t4 + xit2
    D_ = D_a_ * A_
    D = zero - D_
    N_b = D_a_ + one
    N = B_ * N_b
    Z = CMOV(negA, D, D.value, zero.value)

    D2 = Z * Z
    D3 = D2 * Z
    N2 = N * N
    N3 = N2 * N
    ND2 = N * D2
    aND2 = A_ * ND2
    bD3 = B_ * D3
    U = N3 + aND2 + bD3
    V = D3

    UV = U * V
    V2 = V * V
    UV3 = UV * V2
    UV3_exp = UV3 ** ((p-3)//4)
    # UV3_exp = UV3 ** h2c_exponent
    alpha = UV3_exp * UV
    alphaD = alpha * Z
    alpha2 = alpha * alpha
    alpha2V = alpha2 * V

    xit2N = xit2 * N
    t3 = t * t2
    t3alphaD = t3 * alphaD
    X = CMOV(N, xit2N, alpha2V.value, U.value)
    Y = CMOV(t.sign()*alphaD, t3alphaD, alpha2V.value, U.value)

    Q = pointFp(coord_type="projective", coordinate=[X, Y, Z], coefficients=[A_, B_])
    Q.check_on_curve()
    return Q


def isogeny(point: pointFp) -> pointFp:
    X = point.X
    Y = point.Y
    Z = point.Z
    # computing Z**i
    Z_exp = [1] * 17
    Z_exp[1] = Z
    for i in range(2,len(Z_exp)):
        Z_exp[i] = Z_exp[i-1] * Z
    # computing Nx
    Ny = zero
    Dy = zero
    Nx = k[0][11]
    for i in range(1, len(k[0])):  # len(k[0]) = 12
        Nx *= X
        Nx += k[0][11-i] * Z_exp[i]
    Dx = Z_exp[1]
    for i in range(len(k[1])):  # len(k[1]) = 10
        Dx *= X
        Dx += k[1][9-i] * Z_exp[i+2] 
    Ny = k[2][15]
    for i in range(1, len(k[2])):  # len(k[2]) = 16
        Ny *= X
        Ny += k[2][15-i] * Z_exp[i]
    Ny *= Y
    Dy = Z_exp[1]
    for i in range(len(k[3])):  # len(k[3]) = 15
        Dy *= X
        Dy += k[3][14-i] * Z_exp[i+2] 

    # return values in Jacobian coordinates
    Z0 = Dx * Dy
    X0 = Nx * Dy
    Y0 = Ny * Dx
    P = pointFp(coord_type="projective", coordinate=[X0, Y0, Z0], coefficients=[a, b])
    P.check_on_curve()
    return P


# scalar mul *h (h: cofactor)
def cofactor_clearing(point: pointFp) -> pointFp:
    return point.scalar_mul(h1)


def map_to_curve_BLS12381G1(t_list: list[list[int]]) -> pointFp:
    Q0 = SSWU_before_isogeny(t_list[0][0])
    Q1 = SSWU_before_isogeny(t_list[1][0])
    Q = Q0 + Q1
    Q.check_on_curve()
    P = isogeny(Q)
    M = cofactor_clearing(P)
    return M


def test_SSWU():
    p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
    for i in range(100):
        t = random.randint(1, p-1)
        Q = SSWU_before_isogeny(t)


if __name__ == "__main__":
    # t_list = hash_to_field("abc".encode("utf-8"), 2)
    # M = map_to_curve_BLS12381G1(t_list)
    # M.check_on_curve()
    # MX = M.X / M.Z
    # MY = M.Y / M.Z
    # print("%x" % MX.value)
    # print("%x" % MY.value)
    test_SSWU()