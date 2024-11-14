from constants import *
from h2f import hash_to_field

# map_to_curve(u)
# Input: u, an element of field F.
# Output: Q, a point on the elliptic curve E.
# Steps: defined in Section 6.

# xi = Fp(11)
# sqrt_negxi3, is_sqr = (zero-(xi**3)).sqrt()

def SSWU_before_isogeny(t_: int) -> pointFp:
    if t_ == 0 or t_ == 1 or t_ == -1:
        raise Exception("value t is %d" % t_)
    t = Fp(t_)

    t2 = t * t
    xit2 = xi * t2
    xi2t4 = xit2 * xit2
    D_a_ = xi2t4 + xit2
    D_ = D_a_ * A_
    D = zero - D_
    N_b = D_a_ + one
    N = B_ * N_b
    if D == zero:
        print("D == zero")
        D = xi * A_

    D2 = D * D
    D3 = D2 * D
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
    UV3_exp = UV3 ** ((p - 3) // 4)
    alpha = UV3_exp * UV

    alphaD = alpha * D

    alpha2 = alpha * alpha
    alpha2V = alpha2 * V
    if alpha2V == U:
        X = N
        Y = t.sign() * alphaD
        Z = D
    else:
        X = xit2 * N
        t3 = t * t2
        # Y = sqrt_negxi3 * t3 * alphaD
        Y = t3 * alphaD
        Z = D

    Q = pointFp(coord_type="projective", coordinate=[X, Y, Z], coefficients=[A_, B_])
    Q.check_on_curve()
    return Q


def isogeny(point: pointFp) -> pointFp:
    X = point.X
    Y = point.Y
    Z = point.Z
    # computing Nx
    Nx = zero
    Dx = zero
    Ny = zero
    Dy = zero
    for i in range(len(k[0])):  # 12
        Nx = Nx + k[0][i] * (Z ** (11 - i)) * (X**i)
    for i in range(len(k[1])):  # 10
        Dx = Dx + k[1][i] * (Z ** (10 - i)) * (X**i)
    Dx = Dx + X**10
    Dx = Dx * Z
    for i in range(len(k[2])):  # 16
        Ny = Ny + k[2][i] * (Z ** (15 - i)) * (X**i)
    Ny = Ny * Y
    for i in range(len(k[3])):  # 15
        Dy = Dy + k[3][i] * (Z ** (15 - i)) * (X**i)
    Dy = Dy + X**15
    Dy = Dy * Z

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

def map_to_curve_BLS12381G1_2iso(t_list: list[list[int]]) -> pointFp:
    Q0 = SSWU_before_isogeny(t_list[0][0])
    Q1 = SSWU_before_isogeny(t_list[1][0])
    P0 = isogeny(Q0)
    P1 = isogeny(Q1)
    P = P0 + P1
    P.check_on_curve()
    M = cofactor_clearing(P)
    return M

def test_SSWU():
    p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
    for i in range(100):
        t = random.randint(1, p-1)
        Q = SSWU_before_isogeny(t)


if __name__ == "__main__":
    t_list = hash_to_field("abc".encode("utf-8"), 2)
    M = map_to_curve_BLS12381G1(t_list)
    M.check_on_curve()
    MX = M.X / M.Z
    MY = M.Y / M.Z
    print("result point: ")
    print("%x" % MX.value)
    print("%x" % MY.value)
    M = map_to_curve_BLS12381G1_2iso(t_list)
    M.check_on_curve()
    MX = M.X / M.Z
    MY = M.Y / M.Z
    print("result point: ")
    print("%x" % MX.value)
    print("%x" % MY.value)
    # test_SSWU()
