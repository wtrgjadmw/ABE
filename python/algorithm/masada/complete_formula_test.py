from point import PointFp
from field import Fp
import copy
import random


P1x = Fp(0xcf83b2fc8c0f3cc74bb7bb04cf7d8f2501bd8181defa264a8f24e83a82047c2f6ce594f3e954bbcc59a3cd34e26edac)
P1y = Fp(0x197957ba2e9eee73c9d2cf218065853a30ed3f3fc3cf5b351da892c957d0bdb7aa56cd053bdb65e8557893f23ec35998)
P1z = Fp(0x1170e43c0a5cfe3960351bb97241ee0c2f577aa7fa6383ae153f07ca13afbb5a31fbc8560c9b623d0e581f0e1ba5db73)
P2x = Fp(0x16d6ea084534b9c17b910f374a382245052e8cce5190b30708a5e5aa4cf7a496744a901afe9bfdcb9d0eadc5174e7342)
P2y = Fp(0x1354bafd9e151ce14d082e11cc7d822f7ad429760869ccd3877f22fbb08624d494a819b6c34ec4a6b84b58ba03e786e4)
P2z = Fp(0x1480367005925473e8caa846368b857b29da769f1bd441196099846ee542aad67c9250aa1d89711e1c0209f7c5a51148)

fixed_random_point1 = PointFp(P1x, P1y, P1z, "p", 1, 0)
fixed_random_point2 = PointFp(P2x, P2y, P2z, "p", 1, 0)
result = open("complete_result.txt", "w")
test_case = open("complete_testcase.txt", "w")
for i in range(100):
    n = random.randint(1, fixed_random_point1.r - 1)
    rand_point = PointFp( coord="p", is_random=1)
    rand_point.on_curve()
    rand_point.pr("rand_point------------------------------")
    smul_result = rand_point.scalar_mul_montlad(n)
    rand_point.pr("rand_point------------------------------")
    print(n)
    #rand_point_copy.pr("rand_point_deepcopy-------")
    test_case.write( str(n) + "\n")
    test_case.write(hex(rand_point.X.value)[2:]+ "\n")
    test_case.write(hex(rand_point.Y.value)[2:]+ "\n")
    test_case.write(hex(rand_point.Z.value)[2:]+ "\n")
    result.write(hex(smul_result.X.value)[2:] + "\n")
    result.write(hex(smul_result.Y.value)[2:] + "\n")
    result.write(hex(smul_result.Z.value)[2:] + "\n")
result.close()
test_case.close()

