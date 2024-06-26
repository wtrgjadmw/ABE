
def bits_of(k):
    return [int(c) for c in "{0:b}".format(k)]

def is_qr(a: int, p: int):
    p_ = (p-1) >> 1
    x = pow(a, p_, p)
    return x == 1