from field import Fp

a = Fp(4, 1)
b = Fp(3, 0)
c = a.sign(5)
c.pr("c")
print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))