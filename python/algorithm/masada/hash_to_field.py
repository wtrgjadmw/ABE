import hashlib
from my_SHA256 import my_SHA256
"""
m = hashlib.sha256()
m.update(b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq")
print(m.hexdigest())
"""
def ceil(numerator, denominator):
    if numerator % denominator == 0:
        return numerator // denominator
    else:
        return numerator // denominator + 1

def xor(a, b):
    assert len(a) == 1
    assert len(b) == 1
    if a == b:
        result = "0"
    else:
        result = "1"
    return result

def convert_msg_to_ascii(msg):
    result = ""
    for i in range(len(msg)):
        #print(str(msg[i]))
        result = result + hex(ord(str(msg[i])))[2:]
    return result
def strxor(str1, str2, b_in_bytes):
    #str1, str2 input as hex string
    result = int(str1.hex(),16) ^ int(str2.hex(),16)
    #print(str1.hex())
    #print(str2.hex())
    #print(result.to_bytes(b_in_bytes, "big").hex())
    return result.to_bytes(b_in_bytes, "big")

def substr(hex_string, sstart, slen):
    #str in hex!
    result = hex_string[sstart:sstart + slen]
    return result

def I2OSP(x, length):   #output string
    result = b""
    assert x < 256 ** length
    x_hex = hex(x)[2:]
    x_hex = "0" * (2 * length - len(x_hex)) + x_hex
    #print(x_hex)
    current_x = x 
    for i in range(length):
        result = (current_x % 256).to_bytes(1, "big") + result
        current_x = current_x // 256
    return result

def OS2IP(x):           #output integer
    return int(x.hex(), 16)

def my_hash_func(input_byte):
    result = my_SHA256(input_byte)
    return result

def hash_func(input_byte):
    H = hashlib.sha256()    #SHA256 used as hash function
    H.update(input_byte)
    #print("H.hex()", H.hexdigest())
    return H.digest()

def expand_message_xmd(msg, DST, len_in_bytes):
    #constants
    b_in_bytes = 32         #output length of hash function(SHA256) in bytes
    s_in_bytes = 64         #input block size of hash function, 64 for SHA256   
    ell = ceil(len_in_bytes, b_in_bytes)                 #128 / 32 = 4 for BLS12-381, actually ceiling function is recommended
    print("DST", DST)
    print("len(DST)", len(DST))
    DST_prime =  DST + I2OSP(len(DST), 1)       #DST prime in string
    print("DST_prime", DST_prime.hex())
    Z_pad = I2OSP(0, s_in_bytes)
    l_i_b_str = I2OSP(len_in_bytes, 2)
    print("Z_pad", Z_pad.hex())
    print("l_i_b_str", l_i_b_str.hex())
    # print("I2OSP(len(DST),1)", I2OSP(len(DST), 1))
    # print("I2OSP(len(DST) = 50,1)", I2OSP(50,1))
    b0_input = Z_pad + msg + l_i_b_str + I2OSP(0,1) + DST_prime
    print("b0_input", b0_input.hex())
    print("b0_input_len", len(b0_input))
    b0_ = my_hash_func(b0_input)
    b0 = hash_func(b0_input)
    #print("b0_", b0_)
    #print("b0", b0.hex())
    print("b0 == b0_", b0.hex() == b0_)
    assert len(b0) == b_in_bytes
    #print("b0", b0.hex())
    b1_input = b0 + I2OSP(1, 1) + DST_prime
    print("b1_input", b1_input.hex())
    b1 = hash_func(b1_input)
    b1_ = my_hash_func(b1_input)
    print("b1 == b1_", b1.hex() == b1_)
    print("b1_len", len(b1_input))
    assert len(b1) == b_in_bytes
    b_list = b1
    b_previous = b1
    #print("ell", ell)
    for i in range(2, ell + 1):
        b_next_input = strxor(b0, b_previous,b_in_bytes) + I2OSP(i, 1) + DST_prime
        print("b_next_input", b_next_input.hex())
        print(len(strxor(b0, b_previous, b_in_bytes)))
        print(len(I2OSP(i, 1)))
        print(len(DST_prime))
        print("b", str(i), "_input", len(b_next_input))
        b_next = hash_func(b_next_input)
        b_next_ = my_hash_func(b_next_input)
        print("b_next == b_next_", b_next.hex() == b_next_)
        assert len(b_next) == b_in_bytes
        b_previous = b_next
        b_list = b_list + b_next
    pseudo_random_bytes = b_list
    #print("blist", b_list)
    
    #for i in range(len(b_list) - 1):
        #pseudo_random_bytes = pseudo_random_bytes + b_list[i + 1]
    # print("pseudo", pseudo_random_bytes.hex())
    result = substr(pseudo_random_bytes, 0, len_in_bytes)
    return result

def hash_to_field(msg,count):
    #constants
    m = 1                                               #extention degree of the finite field
    L = 64                                              #required output of expanded message(512bits) in bytes
    suite = "BLS12381G1_XMD:SHA-256_SSWU_RO_"           #suite
    DST = b"QUUX-V01-CS02-with-BLS12381G1_XMD:SHA-256_SSWU_RO_"     #DST for BLS12-381
    p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab  #character of finite field
    #count = 2                                           #number of 381bits numbers needed
    len_in_bytes = count * m * L                        #total length of the hashed value befor mod p
    msg_in_bytes = msg.encode('utf-8')
    print("msg_in_bytes", msg_in_bytes)
    pseudo_random_bytes = expand_message_xmd(msg_in_bytes, DST, len_in_bytes)
    print("pseudo", pseudo_random_bytes.hex())
    u_list = []
    for i in range(count):
        e = ""
        for j in range(m):
            elm_offset = L * (j + i * m)
            tv = substr(pseudo_random_bytes, elm_offset, L)
            print("tv", tv.hex())
            #print("len(tv)", len(tv))
            # tv_to_hex = tv.hex()
            assert len(tv) == L
            #print("num(tv)", hex(OS2IP(tv)))
            e_j = OS2IP(tv) % p
            print(OS2IP(tv))
            print(p)
            print(e_j)
            e = e + hex(e_j)[2:]
        u_list.append(int(e, 16))
    return u_list

#count = 2
#testbench at ietf website (hash to curve)
# u_list = hash_to_field("", 2)
# print("u[0]", hex(u_list[0]))
# print("u[1]", hex(u_list[1]))

# u_list = hash_to_field("abc", 2)
# print("u[0]", hex(u_list[0]))
# print("u[1]", hex(u_list[1]))

# u_list = hash_to_field("abcdef0123456789", 2)
# print("u[0]", hex(u_list[0]))
# print("u[1]", hex(u_list[1]))

# longmsg = "q128_" + "q"*128
# u_list = hash_to_field(longmsg, 2)
# print("u[0]", hex(u_list[0]))
# print("u[1]", hex(u_list[1]))

# longmsg = "a512_" + "a"*512
# u_list = hash_to_field(longmsg, 2)
# print("u[0]", hex(u_list[0]))
# print("u[1]", hex(u_list[1]))

longmsg = "abc"
u_list = hash_to_field(longmsg, 2)
print("u[0]", hex(u_list[0]))
print("u[1]", hex(u_list[1]))