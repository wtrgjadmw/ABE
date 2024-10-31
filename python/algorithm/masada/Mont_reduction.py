import random
p = 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559787
R = 2**381
w = 2260841021275534791313679861075179938841727708619644906357975021971563801293839809136504047877488722451865865617405
montgomery_inv = pow(R, p-2, p)
montconv = 2919048491419553598000189368909058870522704139286885631285637946182619063200016518177619514895813310825994757640968
print("2 ** 682", pow(2, 762, p))
#num is a 512 bit random number
print("montconv", R * R % p)


def mont_red(num):
    s2 = (num % R) * w
    s3 = (s2 % R) * p
    s4 = num + s3
    #print("s2:", s2)
    #print("s3:", s3)
    #print("s4:", s4)
    #print(s4 % R)
    assert s4 % R == 0
    s4 = s4 // R
    if s4 > p:
        s4 = s4 - p
    assert s4 == (num * montgomery_inv % p)
    return s4

for i in range(100):
    num = random.randint(1, 2 ** 512 - 1)
    result = mont_red(num)
    num_mont = mont_red(result * montconv)
    print("num % p", num % p)
    print("num_mont", num_mont)
    assert result == (num * montgomery_inv) % p
    assert num % p == mont_red(result * montconv)
    print("ok")
    