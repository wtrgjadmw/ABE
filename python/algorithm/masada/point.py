from field import Fp
from constants import *
import random, copy

class PointFp:
    X = Fp(0)
    Y = Fp(0)
    Z = Fp(0)
    Z2 = Fp(0)
    Z3 = Fp(0)
    is_mont = 0
    r = 0x73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001
    px = Fp(3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507, 0)
    px.Mont_change()
    py = Fp(1339506544944476473020471379941921221584933875938349620426543736416511423956333506472724655353366534992391756441569, 0)
    py.Mont_change()
    four = Fp(4, 0)
    four.Mont_change()
    one = Fp(1,0)
    one.Mont_change()
    coord = ""
    def __init__(self, X=0, Y=0, Z=0, coord="j", mont_flag=1, is_random=0):
        self.coord = coord
        self.is_mont = mont_flag
        if(is_random == 1):
            a = random.randint(1, self.r-1)
            #assert (px ** 3 + four).value == (py**2).value
            one = Fp(1, 0)
            one.Mont_change()
            newP = PointFp(self.px, self.py, one, self.coord, self.is_mont)
            newP.on_curve()
            newP2 = newP + newP
            newP2.pr("newP2")
            randomP = newP.scalar_mul(a)
            randomP.on_curve()
            randomP.pr("randomP")
            self.X = randomP.X
            self.Y = randomP.Y
            self.Z = randomP.Z
            self.Z2 = randomP.Z2
            self.Z3 = randomP.Z3
        else:
            self.X = X
            self.Y = Y
            self.Z = Z
            self.Z2 = self.Z ** 2
            self.Z3 = self.Z ** 3
    
    def __add__(self, other):
        #check if two points are the same in affine coordinates
        point_double_flag = 0
        self_affx, self_affy = self.affine_coordinates()
        other_affx, other_affy = other.affine_coordinates()
        if(self.is_mont != other.is_mont):
            print("is_mont different")
        else:
            if(self.coord != other.coord):
                print("coord different")
            if(self_affx.value == other_affx.value and self_affy.value == other_affy.value):
                point_double_flag = 1
                print("double using addition formula!")
            else:
                pass
                #print("not double")
        if(self.is_mont != other.is_mont):
            print("is_mont different")
        if(self.coord != other.coord):
            print("coordinate different")
        #if(point_double_flag == 1 and self.coord == "j"):
            #pass
            #return self.dbl()
        elif(self.coord == "j"):
            #exception exists
            X1 = self.X
            Y1 = self.Y
            Z1 = self.Z
            Z1_2 = self.Z2
            Z1_3 = self.Z3
            X2 = other.X
            Y2 = other.Y
            Z2 = other.Z
            Z2_2 = other.Z2
            Z2_3 = other.Z3
            U1 = X1 * Z2_2
            U2 = X2 * Z1_2
            U1.pr("U1")
            U2.pr("U2")
            S1 = Y1 * Z2_3
            S2 = Y2 * Z1_3
            S1.pr("S1")
            S2.pr("S2")
            Z1Z2 = Z1 * Z2
            H = U2 - U1
            R_ = S2 - S1
            R = R_ + R_
            H2 = H + H
            I = H2 * H2
            I.pr("I")
            R_2 = R * R
            R_2.pr("R_2")
            newZ = H2 * Z1Z2
            newZ.pr("newZ")
            S12 = S1 + S1
            J1 = I * H
            J2 = I * U1
            J1.pr("J1")
            J2.pr("J2")
            newZ2 = newZ * newZ    
            J22 = J2 + J2
            newX_ = R_2 - J1
            newX = newX_ - J22
            newX.pr("newX")
            J2_X3 = J2 - newX
            newY_ = R * J2_X3
            S12_J1 = S12 * J1
            #newZ3 = newZ2 * newZ
            newY = newY_ - S12_J1
            newY.pr("newY")
            return PointFp(newX, newY, newZ, self.coord, self.is_mont)
        elif(self.coord=="p"):
            #print("exception_free_add executed")
            X1 = copy.deepcopy(self.X)
            Y1 = copy.deepcopy(self.Y)
            Z1 = copy.deepcopy(self.Z)
            X2 = copy.deepcopy(other.X)
            Y2 = copy.deepcopy(other.Y)
            Z2 = copy.deepcopy(other.Z)
            #b3 = 3 * b
            b3 = Fp(4 * 3, 0)
            b3.Mont_change()
            #Complete addition formulas for prime order elliptic curves
            t0 = X1 * X2
            t1 = Y1 * Y2
            t2 = Z1 * Z2
            t0.pr("XX")
            t1.pr("YY")
            t2.pr("ZZ")
            t3 = X1 + Y1
            t4 = X2 + Y2
            t3 = t3 * t4
            t4 = t0 + t1
            t3 = t3 - t4
            t3.pr("XY + YX")
            t4 = Y1 + Z1
            X3 = Y2 + Z2
            t4 = t4 * X3
            X3 = t1 + t2
            t4 = t4 - X3
            t4.pr("YZ + ZY")
            X3 = X1 + Z1
            Y3 = X2 + Z2#15
            X3 = X3 * Y3
            Y3 = t0 + t2
            Y3 = X3 - Y3
            X3 = t0 + t0
            t0 = X3 + t0
            t2 = b3 * t2
            t2.pr("b3ZZ")
            Z3 = t1 + t2
            Z3.pr("YY + b3ZZ")
            t1 = t1 - t2
            t1.pr("YY - b3ZZ")
            Y3 = b3 * Y3
            X3 = t4 * Y3
            t2 = t3 * t1
            X3 = t2 - X3
            Y3 = Y3 * t0
            t1 = t1 * Z3
            Y3 = t1 + Y3
            t0 = t0 * t3
            Z3 = Z3 * t4
            Z3 = Z3 + t0
            return PointFp(X3, Y3, Z3, self.coord, self.is_mont)
        
    def dbl(self):
        if self.coord == "j":
            X = copy.deepcopy(self.X)
            Y = copy.deepcopy(self.Y)
            Z = copy.deepcopy(self.Z)
            Z2 = self.Z2
            Z3 = self.Z3
            Y2 = Y + Y
            X_2 = X * X
            Y4_2 = Y2 * Y2
            Y2_2 = Y * Y2
            newZ = Y2 * Z
            X2_2 = X_2 + X_2
            S = X * Y4_2
            M = X2_2 + X_2
            M_2 = M * M
            newZ2 = newZ * newZ
            MS = S * M
            #MS.pr("MS")
            S2 = S + S
            newX = M_2 - S2
            Y8_4 = Y4_2 * Y2_2
            MnewX = M * newX
            newZ3 = newZ2 * newZ
            MS_8Y4 = MS - Y8_4
            #MS_8Y4.pr("MS_8Y4")
            newY = MS_8Y4 - MnewX
            return PointFp(newX, newY, newZ, self.coord, self.is_mont)
        elif self.coord == "p":
            #print("exception_free_dbl executed")
            X = copy.deepcopy(self.X)
            Y = copy.deepcopy(self.Y)
            Z = copy.deepcopy(self.Z)
            b3 = Fp(4 * 3, 0)
            b3.Mont_change()
            three = Fp(3, 0)
            three.Mont_change()
            t0 = Z * Z
            t1 = X * Y
            t2 = Y * Y
            t0.pr("TZ2")
            t1.pr("TXTY")
            t2.pr("TY2")
            t3 = b3 * t0
            t3.pr("b3TZ2")
            t4 = t3 * three    #9bZ2
            t5 = Y * Z         
            t6 = t2 + t2
            t6.pr("2Ty2")
            t6 = t6 + t6
            t7 = t6 + t6        #8Y2
            t7.pr("8TY2")
            t8 = t2 - t4        #Y2 - 9bZ2
            t8.pr("Y2 - 9bZ2")
            t9 = t1 + t1        #2XY
            t10 = t2 + t3       #Y2 + 3bZ2
            t10.pr("Y2 + 3bZ2")
            newX = t9 * t8      #2XY(Y2 - 9bZ2)
            newZ = t7 * t5       #8Y3Z   newZ
            t12 = t7 * t3       #24bY2Z2
            t13 = t8 * t10      #(Y2 - 9bZ2)(Y2 + 3bZ2)
            newY = t13 + t12     #newY
            return PointFp(newX, newY, newZ, self.coord, self.is_mont)

        else:
            print("other coordinates not available yet, returning self")
            return self
    def pr(self, name, is_hex=1):
        self.X.pr(name + " X", is_hex)
        self.Y.pr(name + " Y", is_hex)
        self.Z.pr(name + " Z", is_hex)
        self.Z2.pr(name + " Z2", is_hex)
        self.Z3.pr(name + " Z3", is_hex)
    
    
    def scalar_mul(self, num):
        R = copy.deepcopy(self)
        num_bits = [int(c) for c in "{0:b}".format(num)]
        #R.pr("R")
        index = 0
        for nb in num_bits[1:]:
            R = R.dbl()
            #R2 = R.dbl()
            #Rx, Ry = R.affine_coordinates()
            #R2x, R2y = R.affine_coordinates()
            
            #print("exception free point double")
            #print(Rx.value, Ry.value)
            #print(R2x.value, R2y.value)
            #assert Rx.value == R2x.value
            #assert Ry.value == R2y.value
            #R.pr("R")
            if(nb == 1):
                R = self + R
                #R.pr("R")
            #print("------------------------- index", index, "---------------------------")
            #R.pr("R")
            Rx, Ry = R.affine_coordinates()
            #Rx.pr("Rx")
            #Ry.pr("Ry")
            index += 1
        return R
    
    def scalar_mul_montlad(self, num):
        Q = copy.deepcopy(self)
        P = PointFp(Fp(0), self.one, Fp(0), "p", 1, 0)  #infinity
        num_bits = "0" * (256 - len(bin(num)[2:])) + bin(num)[2:]
        #num_bits = [int(c) for c in "{0:b}".format(num)]
        print(num_bits)
        print(len(num_bits))
        #R.pr("R")
        index = 0
        neg_one = Fp(0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaaa, 0)
        neg_one.Mont_change()
        for i in range(len(num_bits)):
            """
            R = R + R
            R2 = R.dbl()
            Rx, Ry = R.affine_coordinates()
            R2x, R2y = R.affine_coordinates()
            
            #print("exception free point double")
            #print(Rx.value, Ry.value)
            #print(R2x.value, R2y.value)
            assert Rx.value == R2x.value
            assert Ry.value == R2y.value"""
            if num_bits[i] == "1":
                P = P + Q
                Q = Q.dbl()
            else:
                Q = P + Q
                P = P.dbl()
            Pinv = copy.deepcopy(P)
            Pinv.Y = Pinv.Y * neg_one
            #diff = Q + Pinv
            #self_x, self_y = self.affine_coordinates()
            #diff_x, diff_y = self.affine_coordinates()
            #self_x.pr("self_x")
            #self_y.pr("self_y")
            #diff_x.pr("diff_x")
            #diff_y.pr("diff_y")
            #P.on_curve()
            Px, Py = P.affine_coordinates()
            #Px.pr("Px")
            #Py.pr("Py")
            P.pr("P")
            Q.pr("Q")
            #Q.on_curve()
            print("------------------------- index", index, "---------------------------")
            index += 1
        #R = self.scalar_mul(num)
        #R.on_curve()
        #confirm_x, confirm_y = R.affine_coordinates()
        Px, Py = P.affine_coordinates()
        #assert Px.value == confirm_x.value
        #assert Py.value == confirm_y.value
        return P
    
    def on_curve(self, curve_a=zero, curve_b=four):
        if(self.coord == "j"):
            left = self.Y * self.Y
            X3 = self.X ** 3
            bZ6 = self.Z ** 6 * curve_b
            aXZ4 = curve_a * self.X * (self.Z ** 4)
            right = X3 + bZ6 + aXZ4
            if(left.value == right.value):
                print("on curve")
                s = "on curve"
            else:
                print("not on curve")
                s = "not on curve"
        elif(self.coord == "p"):
            left = (self.Y ** 2) * self.Z
            right = (self.X ** 3) + curve_a * self.X *(self.Z ** 2) + (curve_b * self.Z ** 3)
            if(left.value == right.value):
                print("on curve")
                s = "on curve"
            else:
                print("not on curve")
                s = "not on curve"
        return s
    
    def random_point(self, coord):
        a = random.randint(1, self.r-1)
        #assert (px ** 3 + four).value == (py**2).value
        one = Fp(1, 0)
        one.Mont_change()
        newP = PointFp(self.px, self.py, one, coord="j")
        newP.on_curve()
        randomP = newP.scalar_mul(a)
        
        randomP.on_curve()
        randomP.pr("randomP")
        self.X = randomP.X
        self.Y = randomP.Y
        self.Z = randomP.Z
        self.Z2 = randomP.Z2
        self.Z3 = randomP.Z3
    
    def affine_coordinates(self, is_mont=0):
        if(self.coord == "p"):
            aff_x = self.X / self.Z
            aff_y = self.Y / self.Z
        elif(self.coord == "j"):
            aff_x = self.X / self.Z2
            aff_y = self.Y / self.Z3
        elif(self.coord == "a"):
            aff_x = self.X
            aff_y = self.Y
        if(is_mont == 0 and self.is_mont == 1):
            aff_x.Mont_change()
            aff_y.Mont_change()
        return aff_x, aff_y
    
    def change_to(self, coord):
        current_coord = self.coord
        if(current_coord == "j" and coord == "p"):
            self.X = self.X * self.Z
            self.Z = copy.deepcopy(self.Z3)
            self.Z2 = self.Z ** 2
            self.Z3 = self.Z ** 3
            self.coord = "p"
        elif(current_coord == "p" and coord == "j"):
            self.X = self.X * self.Z
            self.Y = self.Y * self.Z2
            self.coord = "j"
    
    def subgroup_check(self, order):
        point_mul_order = self.scalar_mul(order)
        if point_mul_order.Z.value == 0:
            s = "Z coordinate 0"
        else:
            s = "Z coordinate not 0"
        print(s)
        assert point_mul_order.Z.value == 0
        
"""
#newPoint1 = PointFp(0, 0, 0)
#newPoint1.random_point()
x = Fp(0x5947d7d16522883aecc9839b3b5bfe00d8fc5b7c8ed307031d2784ac52dcca50f12b1f1bddc169d62cb3f5e8b9daaa)
y = Fp(0x93b824db726dc6d66766b1eeb3a09d24ebdbdfeedcb0aaf7ff27af218c0c1ee8817ce98e56c2e138697b2bb34e827ec)
z = Fp(0x124fcefc712c4ca082453d47de8f46129e929f98688628a618e7ae0f6cc092cc0429e367403f1de06795d7f9a3d17265)
print("from here---------------------------------------------------------")
print("-------------------------------------------------------------------")
print("------------------------------------------------------------------")
for i in range(5):
    print()
newPoint = PointFp(x, y, z)
one = Fp(1, 0)
one.Mont_change()
Point_zero = PointFp(one, one, Fp(0))
Point3 = newPoint + Point_zero

b = random.randint(1, newPoint1.r - 1)
print(b)
newPoint1.scalar_mul(b)"""
    
