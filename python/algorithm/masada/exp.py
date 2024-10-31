from field import Fp
import copy
x1 = Fp(0xcf83b2fc8c0f3cc74bb7bb04cf7d8f2501bd8181defa264a8f24e83a82047c2f6ce594f3e954bbcc59a3cd34e26edac)
x2 = Fp(0x197957ba2e9eee73c9d2cf218065853a30ed3f3fc3cf5b351da892c957d0bdb7aa56cd053bdb65e8557893f23ec35998)
current10 = Fp(1, 0)
current20 = Fp(1, 0)
current10.Mont_change()
current20.Mont_change()

current11 = copy.copy(x1)
current21 = copy.copy(x2)
p = x1.p
p_3div4 = bin((p - 3) // 4)[2:]
true_exponent = 0
for i in range(len(p_3div4)):
    if p_3div4[i] == "1":
        current10, current11 = current10 * current11, current11 * current11
        current20, current21 = current20 * current21, current21 * current21
        true_exponent = true_exponent * 2 + 1
    else:
        current10, current11 = current10 * current10, current11 * current10
        current20, current21 = current20 * current20, current20 * current21
        true_exponent = true_exponent * 2
    print("i: ", i, "------------------------------------------------------------------")
    current10.pr("current10")
    current11.pr("current11")
    current20.pr("current20")
    current21.pr("current21")
    true1 = x1 ** true_exponent
    true2 = x2 ** true_exponent
    true1.pr("true1")
    true2.pr("true2")    
    