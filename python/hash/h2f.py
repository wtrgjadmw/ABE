import math
from sha256 import sha256
# expand_message_xmd(msg, DST, len_in_bytes)
# Parameters:
# - H, a hash function (see requirements above).
# - b_in_bytes, b / 8 for b the output size of H in bits.
#  For example, for b = 256, b_in_bytes = 32.
# - s_in_bytes, the input block size of H, measured in bytes (see discussion above). For example, for SHA-256, s_in_bytes = 64.
# Input:
# - msg, a byte string.
# - DST, a byte string of at most 255 bytes.
# - len_in_bytes, the length of the requested output in bytes, not greater than the lesser of (255 * b_in_bytes) or 2^16-1.
# Output:
# - uniform_bytes, a byte string.
# Steps:
# 1. ell = ceil(len_in_bytes / b_in_bytes)
# 2. ABORT if ell > 255 or len_in_bytes > 65535 or len(DST) > 255
# 3. DST_prime = DST || I2OSP(len(DST), 1)
# 4. Z_pad = I2OSP(0, s_in_bytes)
# 5. l_i_b_str = I2OSP(len_in_bytes, 2)
# 6. msg_prime = Z_pad || msg || l_i_b_str || I2OSP(0, 1) || DST_prime
# 7. b_0 = H(msg_prime)
# 8. b_1 = H(b_0 || I2OSP(1, 1) || DST_prime)
# 9. for i in (2, ..., ell):
# 10. b_i = H(strxor(b_0, b_(i - 1)) || I2OSP(i, 1) || DST_prime)
# 11. uniform_bytes = b_1 || ... || b_ell
# 12. return substr(uniform_bytes, 0, len_in_bytes)

b_in_bytes = 32
s_in_bytes = 64


def I2OSP(x: int, xLen: int) -> bytes:
    if x >= 256**xLen:
        raise Exception("I2OSP: integer too large")
    return x.to_bytes(xLen, 'big')

def OS2IP(X: bytes) -> int:
    return int.from_bytes(X, 'big')
    
def strxor(s1: bytes, s2: bytes):    
    # returns the bitwise XOR of the two strings
    # For example, strxor("abc", "XYZ") == "9;9" (ASCII literal)
    return bytes(a ^ b for a, b in zip(s1, s2))

def expand_message(msg: bytes, dst: bytes, len_in_bytes: int) -> bytes:
    ell =  math.ceil(len_in_bytes / b_in_bytes)
    if ell > 255 or len_in_bytes > 65535 or len(dst) > 255:
        raise Exception("The length of the requested output in bytes is greater than the lesser of (255 * b_in_bytes) or 2^16-1")
    dst_prime = dst + I2OSP(len(dst), 1)
    Z_pad = I2OSP(0, s_in_bytes)
    l_i_b_str = I2OSP(len_in_bytes, 2)
    msg_prime = Z_pad + msg + l_i_b_str + I2OSP(0, 1) + dst_prime
    b_0 = sha256(msg_prime)
    b_1 = sha256(b_0 + I2OSP(1, 1) + dst_prime)
    uniform_bytes = b_1
    b_i_1 = b_1
    for i in (2, ell+1):
        b_i = sha256(strxor(b_0, b_i_1) + I2OSP(i, 1) + dst_prime)
        uniform_bytes = uniform_bytes + b_i
        b_i_1 = b_i
    return uniform_bytes[:len_in_bytes]

# hash_to_field(msg, count)
# Parameters:
# - DST, a domain separation tag (see Section 3.1).
# - F, a finite field of characteristic p and order q = p^m.
# - p, the characteristic of F (see immediately above).
# - m, the extension degree of F, m >= 1 (see immediately above).
# - L = ceil((ceil(log2(p)) + k) / 8), where k is the security
#  parameter of the suite (e.g., k = 128).
# - expand_message, a function that expands a byte string and
#  domain separation tag into a uniformly random byte string
#  (see Section 5.3).
# Input:
# - msg, a byte string containing the message to hash.
# - count, the number of elements of F to output.
# Output:
# - (u_0, ..., u_(count - 1)), a list of field elements.
# Steps:
# 1. len_in_bytes = count * m * L
# 2. uniform_bytes = expand_message(msg, DST, len_in_bytes)
# 3. for i in (0, ..., count - 1):
# 4. for j in (0, ..., m - 1):
# 5. elm_offset = L * (j + i * m)
# 6. tv = substr(uniform_bytes, elm_offset, L)
# 7. e_j = OS2IP(tv) mod p
# 8. u_i = (e_0, ..., e_(m - 1))
# 9. return (u_0, ..., u_(count - 1))


##### for BLS12-381
xx = "01"               # two-digit numbers indicating the version?
yy = "02"               # two-digit numbers indicating the version?
CURVE_ID = "BLS12381G1" # a human-readable representation of the target elliptic curve. 
EXP_TAG = "XMD"         # expand_message_xmd
HASH_NAME = "SHA-256"   # a human-readable name for the underlying hash primitive. 
HASH_ID = "{}:{}".format(EXP_TAG, HASH_NAME)    # a human-readable representation of the expand_message function and any underlying hash primitives used in hash_to_feld
MAP_ID = "SSWU"         # a human-readable representation of the map_to_curve function. Simplified SWU
ENC_VAR = "RO"          # a string indicating the encoding type and other information. hash_to_curve
suiteID = "{}_{}_{}_{}_".format(CURVE_ID, HASH_ID, MAP_ID, ENC_VAR)
DST = "QUUX-V{}-CS{}-{}".format(xx, yy, suiteID)
p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabffeb153fffb9feffffaaab 
m = 1   # the extension degree of field that curve is defined
L = 64

def hash_to_field(msg: bytes, count: int) -> list[list[int]]:
    len_in_bytes = count * m * L
    uniform_bytes = expand_message(msg, DST.encode('utf-8'), len_in_bytes)
    u = [[0] * m for i in range(count)]
    for i in range(count):
        e = [0] * m
        for j in range(m):
            elm_offset = L * (j + i * m)
            tv = uniform_bytes[elm_offset: elm_offset+L]
            e[j] = OS2IP(tv) % p
        u[i] = e
    return u

if __name__ == "__main__":
    print(hash_to_field("abc".encode('utf-8'), 2))