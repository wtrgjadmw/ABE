#class Fp and hash functions
#mont mode: 1
#not mont mode: 0
import copy
class Fp:
    value = 0
    value_ = 0
    name = ""
    p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
    R = 2**381
    montgomery_inv = pow(R, p-2, p)
    is_mont = 0

    def __init__(self, num, mont_flag=1):
        if(mont_flag == 1):
            self.value = num
            self.value_ = self.MontInvnum(num)
            self.is_mont = mont_flag
        else:
            self.value = num
            self.value_ = self.MontConvnum(num)
            self.is_mont = mont_flag

    def Mont_change(self):
        self.value, self.value_ = self.value_, self.value
        if(self.is_mont == 0):
            self.is_mont = 1
        else:
            self.is_mont = 0

    def MontConvnum(self, num):
        num_mont = (num * self.R) % self.p
        return num_mont

    def MontInvnum(self, num):
        num_invmont = (num*self.montgomery_inv) % self.p
        return num_invmont

    def __add__(self, other):
        if(self.is_mont != other.is_mont):
            print("is_mont not same!!!")
        x = self.value
        y = other.value
        result = (x + y) % self.p
        return Fp(result, self.is_mont)

    def __mul__(self, other):
        if(self.is_mont != other.is_mont):
            print("is_mont not same!!!")
        x = self.value
        y = other.value
        if(self.is_mont == 1):
            result = (x*y % self.p)*self.montgomery_inv % self.p
        else:
            result = x * y % self.p
        return Fp(result, self.is_mont)
    
    def __sub__(self, other):
        if(self.is_mont != other.is_mont):
            print("is_mont not same!!!")
        x = self.value
        y = other.value
        if(x < y):
            x = x + self.p
        result = x - y
        return Fp(result, self.is_mont)
    
    def __pow__(self, exponent):
        #Montconvinv the number to use the pow function
        if(self.is_mont == 1):
            num = self.value_
        else:
            num = self.value
        exp_num = pow(num, exponent, self.p)
        if(self.is_mont == 1):
            return Fp(self.MontConvnum(exp_num))
        else:
            return Fp(exp_num, self.is_mont)
    
    def __truediv__(self, other):
        if(self.is_mont != other.is_mont):
            print("is_mont not same!!!")
        other_inv = other ** (self.p-2)
        return self * other_inv
        
    def check_values(self):
        assert self.value >= self.p
        assert self.value_ >= self.p
        if(self.is_mont == 1):
            assert MontInvnum(self.value) == self.value_
        else:
            assert MontConv(self.value) == self.value_

    def pr(self, name, is_hex=1):
        if(is_hex == 1):
            print(name, hex(self.value))
        else:
            print(name, self.value)
        return name + hex(self.value)
        
    def sign(self, t):
        assert type(t) == int and self.is_mont == 1
        if t % 2 == self.value_ % 2:
            return copy.deepcopy(self)
        else:
            return Fp(0) - self

