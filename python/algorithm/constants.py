import random
from util import bits_of, is_qr

# BLS12-381


class Fp:
    def __init__(self, value) -> None:
        self.p = 0x1A0111EA397FE69A4B1BA7B6434BACD764774B84F38512BF6730D2A0F6B0F6241EABFFFEB153FFFFB9FEFFFFFFFFAAAB
        self.value = value

    def __add__(self, other):
        result = (self.value + other.value) % self.p
        return Fp(result)

    def __sub__(self, other):
        result = (self.value - other.value) % self.p
        return Fp(result)

    def __mul__(self, other):
        result = (self.value * other.value) % self.p
        return Fp(result)

    def inv(self):
        result = pow(self.value, (self.p - 2), self.p)
        return Fp(result)

    def __truediv__(self, other):
        other_inv = other.inv()
        return self * other_inv

    def __pow__(self, exponent: int):
        result = pow(self.value, exponent, self.p)
        return Fp(result)

    # reference: https://zenn.dev/peria/articles/c6afc72b6b003c
    def sqrt(self):
        if not is_qr(self.value, self.p):
            return Fp(0), False
        pmod8 = self.p % 8
        if pmod8 == 3 or pmod8 == 7:
            res = self ** ((self.p + 1) >> 2)
            return res, True
        if pmod8 == 5:
            res = self ** ((self.p + 3) >> 3)
            if res**2 == self:
                res *= Fp(2) ** ((self.p - 1) >> 2)
            return res, True
        if pmod8 == 1:
            z = random.randint(0, self.p - 1)
            while is_qr(z, self.p):
                z = random.randint(0, self.p - 1)
            z = Fp(z)
            t = self.p - 1
            s = 0
            while t % 2 == 0:
                t >>= 1
                s += 1
            A = self**t
            D = z**t
            m = 0
            for i in range(s):
                tmp = (A * (D**m)) ** (2 ** (s - 1 - i))
                if tmp.value == self.p - 1:
                    m = m + (2**i)
            res = (self ** ((t + 1) // 2)) * (D ** (m // 2))
            return res, True
        return Fp(0), False

    def sign(self):
        if self.value > ((self.p - 1) / 2):
            return Fp(-1)
        return Fp(1)


u = -(2**63 + 2**62 + 2**60 + 2**57 + 2**48 + 2**16)
r = u**4 - u**2 + 1
p = (((u - 1) ** 2) * r) // 3 + u
h1 = ((u - 1) ** 2) // 3
h2 = (
    u**8 - 4 * (u**7) + 5 * (u**6) - 4 * (u**4) + 6 * (u**3) - 4 * (u**2) - 4 * u + 13
) // 9

a = Fp(0)
b = Fp(4)
A_ = Fp(
    0x144698A3B8E9433D693A02C96D4982B0EA985383EE66A8D8E8981AEFD881AC98936F8DA0E0F97F5CF428082D584C1D
)
B_ = Fp(
    0x12E2908D11688030018B12E8753EEE3B2016C1F0F24F4070A0B9C14FCEF35EF55A23215A316CEAA5D1CC48E98E172BE0
)
xi = Fp(-1)
zero = Fp(0)
one = Fp(1)
k_ = [
    [
        0x11A05F2B1E833340B809101DD99815856B303E88A2D7005FF2627B56CDB4E2C85610C2D5F2E62D6EAEAC1662734649B7,
        0x17294ED3E943AB2F0588BAB22147A81C7C17E75B2F6A8417F565E33C70D1E86B4838F2A6F318C356E834EEF1B3CB83BB,
        0xD54005DB97678EC1D1048C5D10A9A1BCE032473295983E56878E501EC68E25C958C3E3D2A09729FE0179F9DAC9EDCB0,
        0x1778E7166FCC6DB74E0609D307E55412D7F5E4656A8DBF25F1B33289F1B330835336E25CE3107193C5B388641D9B6861,
        0xE99726A3199F4436642B4B3E4118E5499DB995A1257FB3F086EEB65982FAC18985A286F301E77C451154CE9AC8895D9,
        0x1630C3250D7313FF01D1201BF7A74AB5DB3CB17DD952799B9ED3AB9097E68F90A0870D2DCAE73D19CD13C1C66F652983,
        0xD6ED6553FE44D296A3726C38AE652BFB11586264F0F8CE19008E218F9C86B2A8DA25128C1052ECADDD7F225A139ED84,
        0x17B81E7701ABDBE2E8743884D1117E53356DE5AB275B4DB1A682C62EF0F2753339B7C8F8C8F475AF9CCB5618E3F0C88E,
        0x80D3CF1F9A78FC47B90B33563BE990DC43B756CE79F5574A2C596C928C5D1DE4FA295F296B74E956D71986A8497E317,
        0x169B1F8E1BCFA7C42E0C37515D138F22DD2ECB803A0C5C99676314BAF4BB1B7FA3190B2EDC0327797F241067BE390C9E,
        0x10321DA079CE07E272D8EC09D2565B0DFA7DCCDDE6787F96D50AF36003B14866F69B771F8C285DECCA67DF3F1605FB7B,
        0x6E08C248E260E70BD1E962381EDEE3D31D79D7E22C837BC23C0BF1BC24C6B68C24B1B80B64D391FA9C8BA2E8BA2D229,
    ],
    [
        0x8CA8D548CFF19AE18B2E62F4BD3FA6F01D5EF4BA35B48BA9C9588617FC8AC62B558D681BE343DF8993CF9FA40D21B1C,
        0x12561A5DEB559C4348B4711298E536367041E8CA0CF0800C0126C2588C48BF5713DAA8846CB026E9E5C8276EC82B3BFF,
        0xB2962FE57A3225E8137E629BFF2991F6F89416F5A718CD1FCA64E00B11ACEACD6A3D0967C94FEDCFCC239BA5CB83E19,
        0x3425581A58AE2FEC83AAFEF7C40EB545B08243F16B1655154CCA8ABC28D6FD04976D5243EECF5C4130DE8938DC62CD8,
        0x13A8E162022914A80A6F1D5F43E7A07DFFDFC759A12062BB8D6B44E833B306DA9BD29BA81F35781D539D395B3532A21E,
        0xE7355F8E4E667B955390F7F0506C6E9395735E9CE9CAD4D0A43BCEF24B8982F7400D24BC4228F11C02DF9A29F6304A5,
        0x772CAACF16936190F3E0C63E0596721570F5799AF53A1894E2E073062AEDE9CEA73B3538F0DE06CEC2574496EE84A3A,
        0x14A7AC2A9D64A8B230B3F5B074CF01996E7F63C21BCA68A81996E1CDF9822C580FA5B9489D11E2D311F7D99BBDCC5A5E,
        0xA10ECF6ADA54F825E920B3DAFC7A3CCE07F8D1D7161366B74100DA67F39883503826692ABBA43704776EC3A79A1D641,
        0x95FC13AB9E92AD4476D6E3EB3A56680F682B4EE96F7D03776DF533978F31C1593174E4B4B7865002D6384D168ECDD0A,
    ],
    [
        0x90D97C81BA24EE0259D1F094980DCFA11AD138E48A869522B52AF6C956543D3CD0C7AEE9B3BA3C2BE9845719707BB33,
        0x134996A104EE5811D51036D776FB46831223E96C254F383D0F906343EB67AD34D6C56711962FA8BFE097E75A2E41C696,
        0xCC786BAA966E66F4A384C86A3B49942552E2D658A31CE2C344BE4B91400DA7D26D521628B00523B8DFE240C72DE1F6,
        0x1F86376E8981C217898751AD8746757D42AA7B90EEB791C09E4A3EC03251CF9DE405ABA9EC61DECA6355C77B0E5F4CB,
        0x8CC03FDEFE0FF135CAF4FE2A21529C4195536FBE3CE50B879833FD221351ADC2EE7F8DC099040A841B6DAECF2E8FEDB,
        0x16603FCA40634B6A2211E11DB8F0A6A074A7D0D4AFADB7BD76505C3D3AD5544E203F6326C95A807299B23AB13633A5F0,
        0x4AB0B9BCFAC1BBCB2C977D027796B3CE75BB8CA2BE184CB5231413C4D634F3747A87AC2460F415EC961F8855FE9D6F2,
        0x987C8D5333AB86FDE9926BD2CA6C674170A05BFE3BDD81FFD038DA6C26C842642F64550FEDFE935A15E4CA31870FB29,
        0x9FC4018BD96684BE88C9E221E4DA1BB8F3ABD16679DC26C1E8B6E6A1F20CABE69D65201C78607A360370E577BDBA587,
        0xE1BBA7A1186BDB5223ABDE7ADA14A23C42A0CA7915AF6FE06985E7ED1E4D43B9B3F7055DD4EBA6F2BAFAAEBCA731C30,
        0x19713E47937CD1BE0DFD0B8F1D43FB93CD2FCBCB6CAF493FD1183E416389E61031BF3A5CCE3FBAFCE813711AD011C132,
        0x18B46A908F36F6DEB918C143FED2EDCC523559B8AAF0C2462E6BFE7F911F643249D9CDF41B44D606CE07C8A4D0074D8E,
        0xB182CAC101B9399D155096004F53F447AA7B12A3426B08EC02710E807B4633F06C851C1919211F20D4C04F00B971EF8,
        0x245A394AD1ECA9B72FC00AE7BE315DC757B3B080D4C158013E6632D3C40659CC6CF90AD1C232A6442D9D3F5DB980133,
        0x5C129645E44CF1102A159F748C4A3FC5E673D81D7E86568D9AB0F5D396A7CE46BA1049B6579AFB7866B1E715475224B,
        0x15E6BE4E990F03CE4EA50B3B42DF2EB5CB181D8F84965A3957ADD4FA95AF01B2B665027EFEC01C7704B456BE69C8B604,
    ],
    [
        0x16112C4C3A9C98B252181140FAD0EAE9601A6DE578980BE6EEC3232B5BE72E7A07F3688EF60C206D01479253B03663C1,
        0x1962D75C2381201E1A0CBD6C43C348B885C84FF731C4D59CA4A10356F453E01F78A4260763529E3532F6102C2E49A03D,
        0x58DF3306640DA276FAAAE7D6E8EB15778C4855551AE7F310C35A5DD279CD2ECA6757CD636F96F891E2538B53DBF67F2,
        0x16B7D288798E5395F20D23BF89EDB4D1D115C5DBDDBCD30E123DA489E726AF41727364F2C28297ADA8D26D98445F5416,
        0xBE0E079545F43E4B00CC912F8228DDCC6D19C9F0F69BBB0542EDA0FC9DEC916A20B15DC0FD2EDEDDA39142311A5001D,
        0x8D9E5297186DB2D9FB266EAAC783182B70152C65550D881C5ECD87B6F0F5A6449F38DB9DFA9CCE202C6477FAAF9B7AC,
        0x166007C08A99DB2FC3BA8734ACE9824B5EECFDFA8D0CF8EF5DD365BC400A0051D5FA9C01A58B1FB93D1A1399126A775C,
        0x16A3EF08BE3EA7EA03BCDDFABBA6FF6EE5A4375EFA1F4FD7FEB34FD206357132B920F5B00801DEE460EE415A15812ED9,
        0x1866C8ED336C61231A1BE54FD1D74CC4F9FB0CE4C6AF5920ABC5750C4BF39B4852CFE2F7BB9248836B233D9D55535D4A,
        0x167A55CDA70A6E1CEA820597D94A84903216F763E13D87BB5308592E7EA7D4FBC7385EA3D529B35E346EF48BB8913F55,
        0x4D2F259EEA405BD48F010A01AD2911D9C6DD039BB61A6290E591B36E636A5C871A5C29F4F83060400F8B49CBA8F6AA8,
        0xACCBB67481D033FF5852C1E48C50C477F94FF8AEFCE42D28C0F9A88CEA7913516F968986F7EBBEA9684B529E2561092,
        0xAD6B9514C767FE3C3613144B45F1496543346D98ADF02267D5CEEF9A00D9B8693000763E3B90AC11E99B138573345CC,
        0x2660400EB2E4F3B628BDD0D53CD76F2BF565B94E72927C1CB748DF27942480E420517BD8714CC80D1FADC1326ED06F7,
        0xE0FA1D816DDC03E6B24255E0D7819C171C40F65E273B853324EFCD6356CAA205CA2F570F13497804415473A1D634B8F,
    ],
]
k = [[Fp(k_[i][j]) for j in range(len(k_[i]))] for i in range(len(k_))]


class pointFp:
    def __init__(self, coord_type, coordinate: list[Fp], coefficients: list[Fp]):
        self.p = 0x1A0111EA397FE69A4B1BA7B6434BACD764774B84F38512BF6730D2A0F6B0F6241EABFFFEB153FFFFB9FEFFFFFFFFAAAB
        self.coord_type = coord_type
        self.X = coordinate[0]
        self.Y = coordinate[1]
        self.Z = coordinate[2]
        self.a = coefficients[0]
        self.b = coefficients[1]
        self.b3 = Fp(3) * self.b

    # For projective coordinate
    # Reference:
    # Renes, Joost, Craig Costello, and Lejla Batina.
    # "Complete addition formulas for prime order elliptic curves."
    # Advances in Cryptology–EUROCRYPT 2016: 35th Annual International Conference on the Theory and Applications of Cryptographic Techniques,
    # Vienna, Austria, May 8-12, 2016.
    # Computation cost: 8M + 3S + 3m_a + 2m_3b + 15a (for the case a != 0)
    def __add__(self, other):
        assert self.a == other.a and self.b == other.b, "their curves are different"
        assert self.coord_type == "projective", (
            "the coordinate type is %s" % self.coord_type
        )

        t0 = self.X * other.X
        t1 = self.Y * other.Y
        t2 = self.Z * other.Z
        t3 = self.X + self.Y
        t4 = other.X + other.Y
        t3 = t3 * t4
        t4 = t0 + t1
        t3 = t3 - t4
        t4 = self.X + self.Z
        t5 = other.X + other.Z
        t4 = t4 * t5
        t5 = t0 + t2
        t4 = t4 - t5
        t5 = self.Y + self.Z
        X2_new = other.Y + other.Z
        t5 = t5 * X2_new
        X2_new = t1 + t2
        t5 = t5 - X2_new
        Z2_new = self.a * t4
        X2_new = self.b3 * t2
        Z2_new = X2_new + Z2_new
        X2_new = t1 - Z2_new
        Z2_new = t1 + Z2_new
        Y3 = X2_new * Z2_new
        t1 = t0 + t0
        t1 = t1 + t0
        t2 = self.a * t2
        t4 = self.b3 * t4
        t1 = t1 + t2
        t2 = t0 - t2
        t2 = self.a * t2
        t4 = t4 + t2
        t0 = t1 * t4
        Y3 = Y3 + t0
        t0 = t5 * t4
        X2_new = t3 * X2_new
        X2_new = X2_new - t0
        t0 = t3 * t1
        Z2_new = t5 * Z2_new
        Z2_new = Z2_new + t0
        return pointFp(
            coord_type="projective",
            coordinate=[X2_new, Y3, Z2_new],
            coefficients=[self.a, self.b],
        )

    def double(self):
        t0 = self.X * self.X
        t1 = self.Y * self.Y
        t2 = self.Z * self.Z
        t3 = self.X * self.Y
        t3 = t3 + t3
        Z2_new = self.X * self.Z
        Z2_new = Z2_new + Z2_new
        X2_new = self.a * Z2_new
        Y3 = self.b3 * t2
        Y3 = X2_new + Y3
        X2_new = t1 - Y3
        Y3 = t1 + Y3
        Y3 = X2_new * Y3
        X2_new = t3 * X2_new
        Z2_new = self.b3 * Z2_new
        t2 = self.a * t2
        t3 = t0 - t2
        t3 = self.a * t3
        t3 = t3 + Z2_new
        Z2_new = t0 + t0
        t0 = Z2_new + t0
        t0 = t0 + t2
        t0 = t0 * t3
        Y3 = Y3 + t0
        t2 = self.Y * self.Z
        t2 = t2 + t2
        t0 = t2 * t3
        X2_new = X2_new - t0
        Z2_new = t2 * t1
        Z2_new = Z2_new + Z2_new
        Z2_new = Z2_new + Z2_new
        return pointFp(
            coord_type="projective",
            coordinate=[X2_new, Y3, Z2_new],
            coefficients=[self.a, self.b],
        )

    def scalar_mul(self, n):
        res = self
        for nb in bits_of(n)[1:]:
            res = self.double()
            if nb == 1:
                res = res + self
        return res

    def check_on_curve(self):
        if self.coord_type == "projective":
            X_ = self.X / self.Z
            Y_ = self.Y / self.Z
            gx = X_**3 + self.a * X_ + self.b
            y2 = Y_**2
            assert gx.value == y2.value, "\ng(x) = %x\ny    = %x" % (gx.value, y2.value)
        else:
            raise Exception("not implemented")

    def check_rP_is_inf(self):
        tmp = self
        # if self.coord_type != "affine":
        #     tmp = pointFp(coord_type="affine", coordinate=[self.X / self.Z, self.Y / self.Z, Fp(1)], coefficients=[self.a, self.b])
        inf = tmp.scalar_mul(r)
        if inf.Z.value == 0:
            return True
        print(inf.X.value, inf.Y.value, inf.Z.value)
        return False


def random_pointFp(p: int, coefficients: list[Fp]):
    sqrtIsExist = False
    while not sqrtIsExist:
        X2_new = Fp(random.randint(0, p - 1))
        Y3, sqrtIsExist = (
            X2_new**3 + coefficients[0] * X2_new + coefficients[1]
        ).sqrt()
    res = pointFp(
        coord_type="projective",
        coordinate=[X2_new, Y3, Fp(1)],
        coefficients=coefficients,
    )
    res.check_on_curve()
    hashed_point = res.scalar_mul(h1)
    hashed_point.check_on_curve()
    # TODO: check if rP is infinity point
    return hashed_point


if __name__ == "__main__":
    random_point = random_pointFp(p, [a, b])
