from point import PointFp
from field import Fp
import copy
import random
#be careful: when scalar = 0 result can be wrong
"""
def Sugiyama_montlad_old(P, scalar):
    f = open("sugiyama.txt", "w")
    result_txt = open("result.txt", "w")
    assert type(P) == PointFp
    #assert type(Q) == PointFp
    scalar_bin = "{:0256b}".format(scalar)
    print(scalar_bin)
    print(bin(scalar))
    X0 = P.X
    Y0 = P.Y
    Z0 = P.Z
    X0.pr("X0")
    Y0.pr("Y0")
    Z0.pr("Z0")
    #point R0 (X1, Z1) point R1 (X2, Z2
    # 2Ri (X4, Z4), R0 + R1 (X3, Z3)
    original_x = X0 / Z0
    original_x.pr("original_x")
    X1 = Fp(1, 0)
    X1.Mont_change()
    Z1 = Fp(0, 0)
    Z1.Mont_change()
    X2 = copy.copy(P.X)
    Z2 = copy.copy(P.Z)
    fourb = Fp(4 * 4, 0)
    b = Fp(4, 0)
    fourb.Mont_change()
    b.Mont_change()
    point_inf = PointFp(Fp(0), copy.copy(X1), Fp(0), coord="p")
    current_R0 = copy.copy(point_inf)
    current_R1 = copy.copy(P)
    index = 0
    for i in range(len(scalar_bin)):
        if(scalar_bin[i] == "1"):
            X = copy.copy(X2)
            Z = copy.copy(Z2)
        elif(scalar_bin[i] == "0"):
            X = copy.copy(X1)
            Z = copy.copy(Z1)
        Z_2 = Z * Z
        Z_2.pr("Z2")
        Z1Z2 = Z1 * Z2
        Z1Z2.pr("Z1Z2")
        X1Z2 = X1 * Z2
        X1.pr("X1")
        Z2.pr("Z2")
        f.write(Z_2.pr("Z^2") + "\n")
        X2Z1 = X2 * Z1
        X2Z1.pr("X2Z1")
        X1Z2.pr("X1Z2")
        XZ = X * Z
        XZ.pr("XZ")
        X1X2 = X1 * X2

        X1Z2_plus_X2Z1 = X1Z2 + X2Z1
        X1Z2_min_X2Z1 = X1Z2 - X2Z1
        f.write(X1Z2_min_X2Z1.pr("SUB1") + "\n")
        f.write(X1Z2_plus_X2Z1.pr("ADD1") + "\n") 
        
        XZ2 = XZ + XZ
        f.write(XZ2.pr("ADD2") + "\n")
        X2 = X * X
        Z24b = fourb * Z_2
        f.write(Z24b.pr("Z24b") + "\n")
        #f.write(X40.pr("X^4") + "\n")
        Z1Z24b = fourb * Z1Z2
        #expressions
        #X3_ = X30 - X31
        #X3 = X3_ * Z0
        #Z3 = X0 * Z30
        #X4 = Z40 - Z41
        #Z4 = Z40 + Z41
        Z30 = X1Z2_min_X2Z1 * X1Z2_min_X2Z1
        X3Z2 = X2 * XZ2                     #2 * X3Z
        X30 = X1X2 * X1X2
        X31 = Z1Z24b * X1Z2_plus_X2Z1
        X41 = Z24b * XZ2
        Z41 = Z24b * Z_2
        f.write(Z41.pr("4bZ4") + "\n")
        X40 = X2 * X2
        f.write(X40.pr("X^4") + "\n")
        Z3 = X0 * Z30
        X3_ = X30 - X31
        X3 = Z0 * X3_
        X4 = X40 - X41
        Z40 = X3Z2 + X3Z2
        Z4 = Z40 + Z41
        X3.pr("X3")
        Z3.pr("Z3")
        X4.pr("X4")
        Z4.pr("Z4")
        if(scalar_bin[i] == "1"):
            X1 = copy.copy(X3)
            Z1 = copy.copy(Z3)
            X2 = copy.copy(X4)
            Z2 = copy.copy(Z4)
        elif(scalar_bin[i] == "0"):
            X1 = copy.copy(X4)
            Z1 = copy.copy(Z4)
            X2 = copy.copy(X3)
            Z2 = copy.copy(Z3)
        
        #checking the results
        if(scalar_bin[i] == "1"):
            current_R0, current_R1 = current_R0 + current_R1, current_R1 + current_R1
        elif(scalar_bin[i] == "0"):
            current_R0, current_R1 = current_R0 + current_R0, current_R0 + current_R1
        current_x = X1 / Z1
        correct_x = current_R0.X / current_R0.Z
        f.write(str(index) + "--------------------------------------------------------------\n")
        f.write(hex(Z3.value)+ "\n")
        f.write(hex(X4.value)+ "\n")
        f.write(hex(Z4.value)+ "\n")
        f.write(hex(X3.value)+ "\n")
        index += 1
    #y_recovery
    X0X1 = X0 * X1
    X1Z0 = X1 * Z0
    Z1Z2 = Z1 * Z2
    Y0Z0 = Y0 * Z0
    Z0Z1 = Z0 * Z1
    X0Z1 = X0 * Z1
    bZ2 = b * Z2
    X0X1.pr("X0X1")
    X1Z0.pr("X1Z0")
    Z1Z2.pr("Z1Z2")
    Y0Z0.pr("Y0Z0")
    Z0Z1.pr("Z0Z1")
    X0Z1.pr("X0Z1")
    bZ2.pr("bZ2")
    ((X1 * X0) * (X0 * Z1 + X1 * Z0)).pr("(X1 * X0) * (X0 * Z1 + X1 * Z0)")
    ((X0 * Z1 - X1 * Z0) ** 2).pr("(X0 * Z1 - X1 * Z0) ** 2")
    (Y0 * Z0 * Z1 * Z2).pr("Y0 * Z0 * Z1 * Z2")
    (Z0 ** 2 * Z1 ** 2).pr("Z0 ** 2 * Z1 ** 2")
    (Y0 * Z1 * Z2 * Z0).pr("Y0 * Z1 * Z2 * Z0")

    result_x_ = Y0 * X1 * Z1 * Z2 * Z0
    result_x = result_x_ + result_x_
    result_y0_ = b * Z0 ** 2 * Z1 ** 2 * Z2
    result_y0 = result_y0_ + result_y0_
    result_y1 = Z2 * (X1 * X0) * (X0 * Z1 + X1 * Z0)
    result_y2 = X2 * (X0 * Z1 - X1 * Z0) ** 2
    result_y = result_y0 + result_y1 - result_y2
    result_z_ = Y0 * Z0 * Z1 ** 2 * Z2
    result_z = result_z_ + result_z_
    result_x_.pr("X'")
    result_x.pr("X")
    result_y0_.pr("Y0")
    result_y1.pr("Y1")
    result_y2.pr("Y2")
    result_y.pr("Y")
    result_z_.pr("Z'")
    result_z.pr("Z")
    #Y0_2_inv = Y0_2 ** (Y0.p - 2)
    #one = Fp(1, 0)
    #one.Mont_change()
    #assert one.value == (Y0_2 * Y0_2_inv).value
    #recovered_y = Y0_2_inv * num
    result = PointFp(result_x, result_y, result_z, coord="p")
    result.on_curve()
    aff_x, aff_y = result.affine_coordinates()
    aff_x.pr("aff_x")
    aff_y.pr("aff_y")
    correct_x, correct_y = current_R0.affine_coordinates()
    correct_x.pr("correct_x")
    correct_y.pr("correct_y")
    assert correct_x.value == aff_x.value
    assert correct_y.value == aff_y.value
    f.close()
    return result.on_curve()
"""
def Sugiyama_montlad(P, scalar, result):
    f = open("sugiyama.txt", "w")
    result_txt = open("result.txt", "w")
    assert type(P) == PointFp
    #assert type(Q) == PointFp
    scalar_bin = "{:0256b}".format(scalar)
    print(scalar_bin)
    print(bin(scalar))
    X0 = P.X
    Y0 = P.Y
    Z0 = P.Z
    X0.pr("X0")
    Y0.pr("Y0")
    Z0.pr("Z0")
    #point R0 (X1, Z1) point R1 (X2, Z2
    # 2Ri (X4, Z4), R0 + R1 (X3, Z3)
    original_x = X0 / Z0
    original_x.pr("original_x")
    X1 = Fp(1, 0)
    X1.Mont_change()
    Z1 = Fp(0, 0)
    Z1.Mont_change()
    X2 = copy.copy(P.X)
    Z2 = copy.copy(P.Z)
    fourb = Fp(4 * 4, 0)
    b = Fp(4, 0)
    fourb.Mont_change()
    b.Mont_change()
    point_inf = PointFp(Fp(0), copy.copy(X1), Fp(0), coord="p")
    current_R0 = copy.copy(point_inf)
    current_R1 = copy.copy(P)
    index = 0
    for i in range(len(scalar_bin)):
        if(scalar_bin[i] == "1"):
            X = copy.copy(X2)
            Z = copy.copy(Z2)
        elif(scalar_bin[i] == "0"):
            X = copy.copy(X1)
            Z = copy.copy(Z1)
        f.write("current_bit:" + str(scalar_bin[i]) + "\n")
        Z_2 = Z * Z
        Z_2.pr("Z2")
        Z1Z2 = Z1 * Z2
        Z1Z2.pr("Z1Z2")
        X12 = X1 + X1
        X1Z2 = X1 * Z2
        X1.pr("X1")
        Z2.pr("Z2")
        f.write(Z_2.pr("Z^2") + "\n")
        X2Z1 = X2 * Z1
        X2Z1.pr("X2Z1")
        X1Z2.pr("X1Z2")
        XZ = X * Z
        XZ.pr("XZ")
        X12X2 = X12 * X2
        X_2 = X * X
        Z24b = fourb * Z_2
        Z1Z24b = fourb * Z1Z2
        Z1Z2.pr("Z1Z2")
        Z1Z24b.pr("Z1Z24b")
        X1Z2_plus_X2Z1 = X1Z2 + X2Z1
        X1Z2_min_X2Z1 = X1Z2 - X2Z1
        f.write(X1Z2_min_X2Z1.pr("SUB1") + "\n")
        f.write(X1Z2_plus_X2Z1.pr("ADD1") + "\n") 
        
        XZ2 = XZ + XZ
        f.write(XZ2.pr("ADD2") + "\n")
        
        
        f.write(Z24b.pr("Z24b") + "\n")
        #f.write(X40.pr("X^4") + "\n")
        
        #expressions
        #X3_ = X30 - X31
        #X3 = X3_ * Z0
        #Z3 = X0 * Z30
        #X4 =  X40 - X41
        #Z4 = Z40 + Z41
        Z30 = X1Z2_min_X2Z1 * X1Z2_min_X2Z1
        X12X2_X1Z2_plus_X2Z1 = X12X2 * X1Z2_plus_X2Z1
        Z12Z224b = Z1Z24b * Z1Z2
        X3Z2 = X_2 * XZ2    #2 * X3Z
        X41 = Z24b * XZ2
        Z41 = Z24b * Z_2    
        
        X40 = X_2 * X_2
        X31 = X0 * Z30
        X30 = X12X2_X1Z2_plus_X2Z1 + Z12Z224b
        X12X2_X1Z2_plus_X2Z1.pr("X30_left")
        Z12Z224b.pr("X30.right")
        X30 = Z0 * X30
        Z3 = Z0 * Z30
        
        
        
        f.write(Z41.pr("4bZ4") + "\n")
        
        f.write(X40.pr("X^4") + "\n")
        
        X3 = X30 - X31
        X30.pr("X30")
        X31.pr("X31")
        X4 = X40 - X41
        X40.pr("X40")
        X41.pr("X41")
        Z40 = X3Z2 + X3Z2
        Z4 = Z40 + Z41
        Z40.pr("Z40")
        Z41.pr("Z41")
        X3.pr("X3")
        Z3.pr("Z3")
        X4.pr("X4")
        Z4.pr("Z4")
        print("expected results")
        a = ((X1 * Z2 + X2 * Z1) * (X1 * X2) + (X1 * Z2 + X2 * Z1) * (X1 * X2) + fourb * (Z1 * Z2) ** 2) * Z0 - X0 * (X1*Z2 - X2 * Z1) ** 2
        a0 = ((X1 * Z2 + X2 * Z1) * (X1 * X2) + (X1 * Z2 + X2 * Z1) * (X1 * X2) + fourb * (Z1 * Z2) ** 2) * Z0
        a1 = X0 * (X1*Z2 - X2 * Z1) ** 2
        a0left = (X1 * Z2 + X2 * Z1) * (X1 * X2) + (X1 * Z2 + X2 * Z1) * (X1 * X2)
        a0right =  fourb * (Z1 * Z2) ** 2
        a0.pr("a0") 
        a1.pr("a1")
        a0left.pr("a0left")
        a0right.pr("a0right")
        
        b = Z0 * (X1*Z2 - X2*Z1) ** 2
        c = X ** 4 - fourb * X * Z ** 3 - fourb * X * Z ** 3
        four = Fp(4, 0)
        four.Mont_change()
        d = four * X ** 3 * Z + fourb * Z **4
        a.pr("a")
        b.pr("b")
        c.pr("c")
        d.pr("d")
        adivb = a / b
        cdivd = c / d
        adivb.pr("adivb")
        cdivd.pr("cdivd")
        if(scalar_bin[i] == "1"):
            X1 = copy.copy(X3)
            Z1 = copy.copy(Z3)
            X2 = copy.copy(X4)
            Z2 = copy.copy(Z4)
        elif(scalar_bin[i] == "0"):
            X1 = copy.copy(X4)
            Z1 = copy.copy(Z4)
            X2 = copy.copy(X3)
            Z2 = copy.copy(Z3)
        
        #checking the results
        if(scalar_bin[i] == "1"):
            current_R0, current_R1 = current_R0 + current_R1, current_R1 + current_R1
        elif(scalar_bin[i] == "0"):
            current_R0, current_R1 = current_R0 + current_R0, current_R0 + current_R1
        current_x = X1 / Z1
        current_x2 = X2 / Z2
        correct_x = current_R0.X / current_R0.Z
        correct_x2 = current_R1.X / current_R1.Z
        
        f.write(str(index) + "--------------------------------------------------------------\n")
        f.write(hex(X3.value)+ "\n")
        f.write(hex(Z3.value)+ "\n")
        f.write(hex(X4.value)+ "\n")
        f.write(hex(Z4.value)+ "\n")
        
        f.write(hex(current_x.value) + "\n")
        f.write(hex(correct_x.value) + "\n")
        f.write(hex(correct_x2.value) + "\n")
        assert current_x.value == correct_x.value
        assert current_x2.value == correct_x2.value
        current_R0.on_curve()
        current_R1.on_curve()
        index += 1
        print("index: ", i, "-----------------------------------------------")
        #if i == 10:
        #    break
    result.write(hex(X1.value)[2:] + "\n")
    result.write(hex(Z1.value)[2:] + "\n")
    result.write(hex(X2.value)[2:] + "\n")
    result.write(hex(Z2.value)[2:] + "\n")
    f.close()
    return  current_x, current_x2

scalar = 37446310348075798564380156715550048345970861198765670041724256431922912945954

P1x = Fp(0xcf83b2fc8c0f3cc74bb7bb04cf7d8f2501bd8181defa264a8f24e83a82047c2f6ce594f3e954bbcc59a3cd34e26edac)
P1y = Fp(0x197957ba2e9eee73c9d2cf218065853a30ed3f3fc3cf5b351da892c957d0bdb7aa56cd053bdb65e8557893f23ec35998)
P1z = Fp(0x1170e43c0a5cfe3960351bb97241ee0c2f577aa7fa6383ae153f07ca13afbb5a31fbc8560c9b623d0e581f0e1ba5db73)

fixed_random_point1 = PointFp(P1x, P1y, P1z, "p", 1, 0)
#Sugiyama_montlad(fixed_random_point1, scalar)
scalar_bin = "{:0256b}".format(scalar)
print(scalar_bin)
print(bin(scalar))
#result_txt = open("result.txt", "w")
#for i in range(100):
#    rand_point_p = PointFp(coord="p", is_random=1)
#    Sugiyama_montlad(rand_point_p, secr)
#result_txt.close()
fourb = Fp(4 * 4, 0)
fourb.Mont_change()
fourb.pr("fourb")

result = open("sugiyama_result.txt", "w")
test_case = open("sugiyama_testcase.txt", "w")
for i in range(100):
    n = random.randint(1, fixed_random_point1.r - 1)
    rand_point = PointFp( coord="p", is_random=1)
    rand_point.on_curve()
    rand_point.pr("rand_point------------------------------")
    Sugiyama_montlad(rand_point, n, result)
    rand_point.pr("rand_point------------------------------")
    print(n)
    #rand_point_copy.pr("rand_point_deepcopy-------")
    test_case.write( str(n) + "\n")
    test_case.write(hex(rand_point.X.value)[2:]+ "\n")
    test_case.write(hex(rand_point.Y.value)[2:]+ "\n")
    test_case.write(hex(rand_point.Z.value)[2:]+ "\n")
result.close()
test_case.close()