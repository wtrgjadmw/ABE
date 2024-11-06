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

def SSWU_before_isogeny(t_: int) -> pointFp:
    if t_ == 0 or t_ == 1 or t_ == -1:
        raise Exception("value t is %d" % t)
    t = Fp(t_)

    t2 = t * t
    xit2 = xi * t2
    xi2t4 = xit2 * xit2
    D_a_ = xi2t4 + xit2
    D_ = D_a_ * A_
    Z = zero - D_
    N_b = D_a_ + one
    X = B_ * N_b
    if Z == zero:
        Z = xi * A_

    D2 = Z * Z
    D3 = D2 * Z
    N2 = X * X
    N3 = N2 * X
    ND2 = X * D2
    aND2 = A_ * ND2
    bD3 = B_ * D3
    U = N3 + aND2 + bD3
    V = D3

    UV = U * V
    V2 = V * V
    UV3 = UV * V2
    UV3_exp = UV3 ** ((UV3.p - 3) // 4)

    alpha = UV3_exp * UV

    alphaD = alpha * Z

    alpha2 = alpha * alpha
    alpha2V = alpha2 * V
    if alpha2V == U:
        Y = t.sign() * alphaD
    else:
        X = xit2 * X
        t3 = t * t2
        Y = t3 * alphaD

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


if __name__ == "__main__":
    t_list = hash_to_field("abc".encode("utf-8"), 2)
    M = map_to_curve_BLS12381G1(t_list)
    M.check_on_curve()
    # t_list = hash_to_field("abc".encode("utf-8"), 2)
    # Q0 = SSWU_before_isogeny(t_list[0][0])
    # Q1 = SSWU_before_isogeny(t_list[1][0])
    # Q = Q0 + Q1
    # P = isogeny(Q)