#hash to field for G1 hash_to_curve for sage
def hash_to_field_sage(msg, count):
    #constants
    m = 1                                               #extention degree of the finite field
    L = 64                                              #required output of expanded message(512bits) in bytes
    suite = "BLS12381G1_XMD:SHA-256_SSWU_RO_"           #suite
    #DST = b"BLS12381G1_XMD:SHA-256_SSWU_RO_TESTGEN"     #DST for BLS12-381
    DST = bytes.fromhex("515555582d5630312d435330322d776974682d424c53313233383147315f584d443a5348412d3235365f535357555f524f5f")
    p = 0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab  #character of finite field
    #count = 2                                           #number of 381bits numbers needed
    len_in_bytes = count * m * L                        #total length of the hashed value befor mod p
    #msg_in_bytes = convert_msg_to_ascii(msg)
    msg_in_bytes = msg.encode()
    #DST_in_bytes = convert_msg_to_ascii(DST)
    print("msg_in_bytes", msg_in_bytes)
    pseudo_random_bytes = expand_message_xmd(msg_in_bytes, DST, len_in_bytes)
    u_list = []
    for i in range(count):
        e = ""
        for j in range(m):
            elm_offset = L * (j + i * m)
            tv = substr(pseudo_random_bytes, elm_offset, L)
            print("tv", tv)
            assert len(tv) == 2 * L
            print("num(tv)", hex(OS2IP(tv)))
            e_j = OS2IP(tv) % p
            e = e + hex(e_j)[2:]
        u_list.append(e)
    return u_list

u_list = hash_to_field_sage("asdf", 2)
print(u_list)

def expand_message_xmd_sage(msg, DST, len_in_bytes):
    #constants
    b_in_bytes = 32         #output length of hash function(SHA256) in bytes
    r_in_bytes = 64         #input block size of hash function, 64 for SHA256   
    ell = ceil(len_in_bytes, b_in_bytes)                 #128 / 32 = 4 for BLS12-381, actually ceiling function is recommended
    print("DST", DST)
    print("len(DST)", len(DST))
    DST_prime = I2OSP(len(DST), 1) + DST        #DST prime in string
    DST_prime_sage = DST + I2OSP(len(DST), 1)
    print("DST_prime", DST_prime.hex())
    Z_pad = I2OSP(0, r_in_bytes)
    l_i_b_str = I2OSP(len_in_bytes, 2)
    print("Z_pad", Z_pad.hex())
    print("l_i_b_str", l_i_b_str.hex())
    print("I2OSP(len(DST),1)", I2OSP(len(DST), 1))
    print("I2OSP(len(DST) = 50,1)", I2OSP(50,1))
    b0_input = Z_pad + msg + l_i_b_str + I2OSP(0,1) + DST_prime
    b0_input_sage = Z_pad + msg + l_i_b_str + I2OSP(0,1) + DST_prime_sage
    print(b0_input.hex())
    print(b0_input_sage.hex())
    b0 = hash_func(b0_input)
    b0_sage = hash_func(b0_input_sage)
    assert len(b0) == b_in_bytes
    print("b0", b0)
    print("b0_sage", b0_sage.hex())
    b1_input = b0 + I2OSP(1, 1) + DST_prime
    b1_input_sage = b0_sage + I2OSP(1,1) + DST_prime_sage
    b1 = hash_func(b1_input)
    b1_sage = hash_func(b1_input_sage)
    print("b1_input_sage", b1_input_sage.hex())
    print("b1_sage", b1_sage.hex())
    assert len(b1) == b_in_bytes
    b_list = b1_sage
    b_previous = b1_sage
    print("ell", ell)
    for i in range(2, ell + 1):
        b_next_input = strxor(b0_sage, b_previous,b_in_bytes) + I2OSP(i, 1) + DST_prime_sage
        print("b_next_input", b_next_input.hex())
        b_next = hash_func(b_next_input)
        assert len(b_next) == b_in_bytes
        b_previous = b_next
        b_list = b_list + b_next
    pseudo_random_bytes = b_list
    #print("blist", b_list)
    
    #for i in range(len(b_list) - 1):
        #pseudo_random_bytes = pseudo_random_bytes + b_list[i + 1]
    print("pseudo", pseudo_random_bytes.hex())
    result = substr(pseudo_random_bytes, 0, len_in_bytes)
    return result