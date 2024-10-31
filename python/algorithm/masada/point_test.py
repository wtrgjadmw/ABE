from point import PointFp
from field import Fp
#projective point addition and Jacobian point addition probably correct if on_curve is ok
#rand_point_j = PointFp(coord="j", is_random=1)
rand_point_p = PointFp(coord="p", is_random=1)
#rand_point_j.on_curve()
#rand_point_p.on_curve()
#x, y = rand_point_p.affine_coordinates()
#left = x ** 3 + Fp(4, 0)
#right = y ** 2
#left.pr("left")
#right.pr("right")

P1x = Fp(0xcf83b2fc8c0f3cc74bb7bb04cf7d8f2501bd8181defa264a8f24e83a82047c2f6ce594f3e954bbcc59a3cd34e26edac)
P1y = Fp(0x197957ba2e9eee73c9d2cf218065853a30ed3f3fc3cf5b351da892c957d0bdb7aa56cd053bdb65e8557893f23ec35998)
P1z = Fp(0x1170e43c0a5cfe3960351bb97241ee0c2f577aa7fa6383ae153f07ca13afbb5a31fbc8560c9b623d0e581f0e1ba5db73)
P2x = Fp(0x16d6ea084534b9c17b910f374a382245052e8cce5190b30708a5e5aa4cf7a496744a901afe9bfdcb9d0eadc5174e7342)
P2y = Fp(0x1354bafd9e151ce14d082e11cc7d822f7ad429760869ccd3877f22fbb08624d494a819b6c34ec4a6b84b58ba03e786e4)
P2z = Fp(0x1480367005925473e8caa846368b857b29da769f1bd441196099846ee542aad67c9250aa1d89711e1c0209f7c5a51148)

fixed_random_point1 = PointFp(P1x, P1y, P1z, "p", 1, 0)
fixed_random_point2 = PointFp(P2x, P2y, P2z, "p", 1, 0)
fixed_random_point1.on_curve()
fixed_random_point2.on_curve()
#add_result = fixed_random_point1 + fixed_random_point2
#dbl_result = fixed_random_point1.dbl()
#add_result.pr("add_result")
#dbl_result.pr("dbl_result")
#add_result.on_curve()
#dbl_result.on_curve()
#scalar multiplication check: r * P goes to O or not
#if maybe_O_p.Y is non-zero and X, Z are zero then maybe_O is O in projective coordinates
#if maybe_O_j.X, Y is non-zero and Z is zero then maybe_O is O in Jacobian coordinates
#maybe_O = rand_point_p.scalar_mul(rand_point_p.r)
#maybe_O.pr("maybe_O_p")
#maybe_O = rand_point_j.scalar_mul(rand_point_j.r)
#maybe_O.pr("maybe_O_j")
secr = 37446310348075798564380156715550048345970861198765670041724256431922912945954
b3 = Fp(4 * 3, 0)
b3.Mont_change()
three = Fp(3, 0)
three.Mont_change()
print(hex(three.value))
#fixed_random_point1.scalar_mul_montlad(secr)
#fixed_random_point1.scalar_mul(secr)
fx, fy = fixed_random_point1.affine_coordinates()
fx.pr("fx")
fy.pr("fy")
#maybe_O = fixed_random_point2.scalar_mul_montlad(secr)
#maybe_O = fixed_random_point1.scalar_mul(fixed_random_point1.r)
#maybe_O.pr("sm fixed_point")

X = Fp(0x058b1c1031f5ee5927a09fb004349ef6f5de5579ba41b2e1e5326dd1f8a045295696283458cbab7d9588eb39e7749b5e, 1)
Y = Fp(0x128e97fd915a4b6bdcf57340bf713039de5f6a036e6f756b0e20c99921e8f99438546d0b6adb7e2e9f2a0b96b9191dff, 1)
Z = Fp(0x126743e0261ded187272c7a79683340cc7ed204b6e1571e0aa568931c9378d897e018786c80fc2e3f1359698937f1377, 1)
real_X = X / Z
real_Y = Y / Z
real_X.Mont_change()
real_Y.Mont_change()
print("real_x", real_X.value)
print("real_y", real_Y.value)
resultX = Fp(0x167f7690071e4d38f5f9129b891545108faddc03e08a4177eac8075d7c0050fe9d518ed187cf7a53ffe06289e58cfdae, 1)
resultY = Fp(0x142cbd5d882661ea5d0d1ae2f6b9162b2cf70a8232c37d389936e700972abedc1a7b5176cef90340385999f36dcaf5a3, 1)
resultZ = Fp(0x64a365de88e2b633180fcf0299628bea293b684239b9dacf30ac6a1ea23a6217a8e5e41e199816ee1834c1388b563bb, 1)

scr = 4268913534975731775746350662846454717840984587257904485112530228823140120227
P1x = Fp(0x4992eb28f0121a1df7d094534f14784b54491d303060ad52bc6c8432c53266e6c92fb6bba170743925574037a7dcd72)
P1y = Fp(0x13b7363907ce0fca687045ef35cd65830caf9e06f1a1445b88fee44cef3f93413561151f2a243fa02cd5244752097b6e)
P1z = Fp(0x2c0d9d239488cc249e7d7cfb0716ddc60ebeb6ef61749dc3d3f894c9d3be84a66b1bb8d586723b136327ad0518ee6ad)

fixed_random_point1 = PointFp(P1x, P1y, P1z, "p", 1, 0)
fixed_random_point1.on_curve()
fixed_random_point1.scalar_mul_montlad(scr)