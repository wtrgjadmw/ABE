from constants import *
from h2f import hash_to_field

# map_to_curve(u)
# Input: u, an element of field F.
# Output: Q, a point on the elliptic curve E.
# Steps: defined in Section 6.

xi = Fp(11)
sqrt_negxi3 = Fp(0x03D689D1E0E762CEF9F2BEC6130316806B4C80EDA6FC10CE77AE83EAB1EA8B8B8A407C9C6DB195E06F2DBEABC2BAEFF5)
exp_lad_srt = 0x680447A8E5FF9A692C6E9ED90D2EB35D91DD2E13CE144AFD9CC34A83DAC3D8907AAFFFFAC54FFFFEE7FBFFFFFFFEAAA

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
    #print("UV3: ", hex(UV3.value))
    #print("xiA: ", hex((xi*A_).value))
    UV3_exp = UV3 ** exp_lad_srt
    #print("UV3_exp: ", hex(UV3_exp.value))
    alpha = UV3_exp * UV

    alphaD = alpha * D

    alpha2 = alpha * alpha
    alpha2V = alpha2 * V
    if alpha2V == U:
        X = N
        Y = alphaD
        Z = D
    else:
        X = xit2 * N
        t3 = t * t2
        Y = sqrt_negxi3 * t3 * alphaD
        #Y = t3 * alphaD
        Z = D
    if t.value%2 != Y.value%2:
        Y = zero-Y
    # print("X: ", hex(X.value))
    # print("Y: ", hex(Y.value))
    # print("Z: ", hex(Z.value))
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
    return point.scalar_mul(1-u)


def map_to_curve_BLS12381G1(t_list: list[list[int]]) -> pointFp:
    Q0 = SSWU_before_isogeny(t_list[0][0])
    Q1 = SSWU_before_isogeny(t_list[1][0])
    # print("X: ", hex(Q0.X.value))
    # print("Y: ", hex(Q0.Y.value))
    # print("Z: ", hex(Q0.Z.value))
    # print("X: ", hex(Q1.X.value))
    # print("Y: ", hex(Q1.Y.value))
    # print("Z: ", hex(Q1.Z.value))
    Q = Q0 + Q1
    # print("X: ", hex(Q.X.value))
    # print("Y: ", hex(Q.Y.value))
    # print("Z: ", hex(Q.Z.value))
    Q.check_on_curve()
    P = isogeny(Q)
    # print("X: ", hex(P.X.value))
    # print("Y: ", hex(P.Y.value))
    # print("Z: ", hex(P.Z.value))
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
    # t_list = hash_to_field("abc".encode("utf-8"), 2)
    t_list=[[0x14DEF24C5CD6507F034DE23C06827F91A1C1CEA3409B438EB008909EE49C86C4301E0B449708AB6E46F8CE7D050EAF3B], [0x0769F3B27F8E5A84A864A1B6916CEEE5C8C32C7FAAA178C9612D575C883DB63DDC2DB890331E51B1CCF5F1D66DAC2C6D]]
    M = map_to_curve_BLS12381G1(t_list)
    M.check_on_curve()
    MX = M.X / M.Z
    MY = M.Y / M.Z
    print("result point: ")
    print("%x" % MX.value)
    print("%x" % MY.value)
    # M = map_to_curve_BLS12381G1_2iso(t_list)
    # M.check_on_curve()
    # MX = M.X / M.Z
    # MY = M.Y / M.Z
    # print("result point: ")
    # print("%x" % MX.value)
    # print("%x" % MY.value)
    # # test_SSWU()
    # Q0 = SSWU_before_isogeny(0x14DEF24C5CD6507F034DE23C06827F91A1C1CEA3409B438EB008909EE49C86C4301E0B449708AB6E46F8CE7D050EAF3B)
    # Q1 = SSWU_before_isogeny(0x0769F3B27F8E5A84A864A1B6916CEEE5C8C32C7FAAA178C9612D575C883DB63DDC2DB890331E51B1CCF5F1D66DAC2C6D)
