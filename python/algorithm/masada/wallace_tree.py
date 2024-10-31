"""def mul_nbit(a, b, n):
    if(a > 2 ** n):
        a = a % 2 ** n
    if(b > 2 ** n):
        b = b % 2 ** n
    partial_product = []
    abin = bin(a)[2:]
    abin = "0" * (n - len(abin)) + abin
    bbin = bin(b)[2:]
    bbin = "0" * (n - len(bbin)) + bbin
    print(abin, bbin)
    for i in range(len(bbin)):
        s =
"""

def generate_mult(n):
    #nbit * nbit multiplier
    partial_product_field = []
    for i in range(n):
        s = "x" * (n - 1 - i) + "1" * n + "x" * i
        partial_product_field.append(s)
    print(partial_product_field)
    sum = []
    for i in range(2 * n - 1):
        counter = 0
        for j in range(n):
            if partial_product_field[j][i] == "1":
                counter += 1
        sum.append(counter)
    print(sum)