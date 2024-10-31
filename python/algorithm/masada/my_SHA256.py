import copy
import random
import hashlib

p = 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559787

def pad_message(msg):
    len_in_bytes = len(msg)
    #print(len_in_bytes)
    len_mod_64byte = len_in_bytes % 64
    #print(len_mod_64byte)
    pad_one = (0x80).to_bytes(1, byteorder="big")
    #print(pad_one)
    zero_byte = (0).to_bytes(1, byteorder="big")
    counter = 1
    while len_in_bytes * 8 >= 256 ** counter:
        counter += 1
    #pad_length = 64bit = 8byte
    #print(hex(len_in_bytes * 8)[2:])
    #print(bytes.fromhex("3e8"))
    #pad_length = zero_byte * (8 - len(bytes.fromhex(hex(len_in_bytes * 8)[2:]))) + bytes.fromhex(hex(len_in_bytes * 8)[2:])
    pad_length = zero_byte * (8 - counter) + (len_in_bytes * 8).to_bytes(counter, byteorder = "big")
    if len_mod_64byte > 55:
        zero_byte_number = 64 + 55 - len_mod_64byte
    else:
        zero_byte_number = 55 - len_mod_64byte
    padded_message = msg + pad_one + ((0).to_bytes(1, byteorder="big")) * zero_byte_number + pad_length
    # print("padded_message", padded_message.hex())
    #for i in range(len(padded_message.hex()) // 8):
        #print("padded_message[" + str(i) + "] <= 32'h" + padded_message.hex()[i*8:i*8 + 8])
    #print(len(padded_message))
    return padded_message

#input integer x return integer x
def rotr(shift, x, length):
    shift_x = x >> shift
    #print("shift_x", shift_x)
    #print("upper_bits", )
    result = shift_x + (x % 2 ** shift) * (2 ** (length - shift))
    return result

def large_sum(x, index, length):
    if index == 0:
        x1 = rotr(2, x, length)
        x2 = rotr(13, x, length)
        x3 = rotr(22, x, length)
    elif index == 1:
        x1 = rotr(6, x, length)
        x2 = rotr(11, x, length)
        x3 = rotr(25, x, length)

    result = x1 ^ x2 ^ x3
    return result

def sigma(x, index, length):
    if index == 0:
        x1 = rotr(7, x, length)
        x2 = rotr(18, x, length)
        x3 = x >> 3
        
    elif index == 1:
        x1 = rotr(17, x, length)
        x2 = rotr(19, x, length)
        x3 = x >> 10
        #print(format(x, "032b"))
        #print(format(x1, "032b"))
        #print(format(x2, "032b"))
        #print(format(x3, "032b"))
    result = x1 ^ x2 ^ x3
    return result

def Ch(x, y, z):
    not_x = (x ^ 0xffffffff)
    result = (x & y) ^ (not_x & z)
    return result

def Maj(x, y, z):
    result = (x & y) ^ (x & z) ^ (y & z)
    return result

def Wt_gen(W_list, t, length):
    #print(W_list)

    W1 = sigma(W_list[t - 2], 1, length)
    W2 = W_list[t - 7]
    W3 = sigma(W_list[t - 15], 0, length)
    W4 = W_list[t - 16]
    #print("W1", format(W1, "08x"))
    #print("W2", format(W2, "08x"))
    #print("W3", format(W3, "08x"))
    #print("W4", format(W4, "08x"))
    result = (W1 + W2 + W3 + W4) % 2 ** length
    return result

def W_list_gen(W_list, M_list_i):
    M_LENGTH = 16
    W_LIST_LENGTH = 64
    W_LENGTH = 32
    assert len(M_list_i) == M_LENGTH
    for j in range(M_LENGTH):
        W_list[j] = int.from_bytes(M_list_i[j], byteorder="big")
        #print(W_list[j])
    for j in range(M_LENGTH, W_LIST_LENGTH):
        W_list[j] = Wt_gen(W_list, j, W_LENGTH)
        #print(j, hex(W_list[j]))
        #print(format(W_list[j], "032b"))

def K_list_gen(K):
    K[0] = 0x428a2f98
    K[1] = 0x71374491
    K[2] = 0xb5c0fbcf
    K[3] = 0xe9b5dba5
    K[4] = 0x3956c25b
    K[5] = 0x59f111f1
    K[6] = 0x923f82a4
    K[7] = 0xab1c5ed5
    K[8] = 0xd807aa98
    K[9] = 0x12835b01
    K[10] = 0x243185be
    K[11] = 0x550c7dc3
    K[12] = 0x72be5d74
    K[13] = 0x80deb1fe
    K[14] = 0x9bdc06a7
    K[15] = 0xc19bf174
    K[16] = 0xe49b69c1
    K[17] = 0xefbe4786
    K[18] = 0x0fc19dc6
    K[19] = 0x240ca1cc
    K[20] = 0x2de92c6f
    K[21] = 0x4a7484aa
    K[22] = 0x5cb0a9dc
    K[23] = 0x76f988da
    K[24] = 0x983e5152
    K[25] = 0xa831c66d
    K[26] = 0xb00327c8
    K[27] = 0xbf597fc7
    K[28] = 0xc6e00bf3
    K[29] = 0xd5a79147
    K[30] = 0x06ca6351
    K[31] = 0x14292967
    K[32] = 0x27b70a85
    K[33] = 0x2e1b2138
    K[34] = 0x4d2c6dfc
    K[35] = 0x53380d13
    K[36] = 0x650a7354
    K[37] = 0x766a0abb
    K[38] = 0x81c2c92e
    K[39] = 0x92722c85
    K[40] = 0xa2bfe8a1
    K[41] = 0xa81a664b
    K[42] = 0xc24b8b70
    K[43] = 0xc76c51a3
    K[44] = 0xd192e819
    K[45] = 0xd6990624
    K[46] = 0xf40e3585
    K[47] = 0x106aa070
    K[48] = 0x19a4c116
    K[49] = 0x1e376c08
    K[50] = 0x2748774c
    K[51] = 0x34b0bcb5
    K[52] = 0x391c0cb3
    K[53] = 0x4ed8aa4a
    K[54] = 0x5b9cca4f
    K[55] = 0x682e6ff3
    K[56] = 0x748f82ee
    K[57] = 0x78a5636f
    K[58] = 0x84c87814
    K[59] = 0x8cc70208
    K[60] = 0x90befffa
    K[61] = 0xa4506ceb
    K[62] = 0xbef9a3f7
    K[63] = 0xc67178f2


def my_SHA256(msg):
    #msg in bytes 
    #constants
    W_LENGTH = 32
    W_LIST_LENGTH = 64
    M_LENGTH = 16
    
    assert len(msg) < 2 ** 64
    padded_message = pad_message(msg)
    M_list = [[padded_message[64*i + 4*j:64*i + 4*(j + 1)] for j in range(64 // 4)] for i in range(len(padded_message) // 64)]
    N = len(M_list)

    #for i in range(len(M_list)):
        #for j in range(len(M_list[i])):
            #print(M_list[i][j].hex())

    #generate constants list Kt
    K_list = [0 for i in range(W_LIST_LENGTH)]
    K_list_gen(K_list)

    #a, b, c, ..., e, f
    wv_list = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    current_H_list = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    a = 0; b = 1; c = 2; d = 3; e = 4; f = 5; g = 6; h = 7;
    for i in range(N):
        #generate W_list
        W_list = [0 for i in range(W_LIST_LENGTH)]
        W_list_gen(W_list, M_list[i])
        
        wv_list = copy.copy(current_H_list)
        for t in range(W_LIST_LENGTH):
            #print("t = ", t, "----------------------------------------")
            
            #print(format(wv_list[0], "08x"))
            
            T1 = wv_list[h] + large_sum(wv_list[e], 1, W_LENGTH) + Ch(wv_list[e], wv_list[f], wv_list[g]) + K_list[t] + W_list[t]
            T1 = T1 % (2 ** W_LENGTH)
            #print("T1", format(T1, "08x"))
            #print("large_sum", format(large_sum(wv_list[e], 1, W_LENGTH), "08x"))
            #print("Ch", format(Ch(wv_list[e], wv_list[f], wv_list[g]), "08x"))
            #print("Klist[t]", format(K_list[t], "08x"))
            #print("W_list[t]", format(W_list[t], "08x"))
            T2 = large_sum(wv_list[a], 0, W_LENGTH) + Maj(wv_list[a], wv_list[b], wv_list[c])
            T2 = T2 % 2 ** W_LENGTH
            #print("T2", format(T2, "08x"))
            wv_list[h] = wv_list[g]
            wv_list[g] = wv_list[f]
            wv_list[f] = wv_list[e]
            wv_list[e] = (wv_list[d] + T1) % 2 ** W_LENGTH
            wv_list[d] = wv_list[c]
            wv_list[c] = wv_list[b]
            wv_list[b] = wv_list[a]
            wv_list[a] = (T1 + T2) % 2 ** W_LENGTH
            #for i in range(8):
            #    assert wv_list[i] < 2 ** 32
        for j in range(len(current_H_list)):
            current_H_list[j] = (wv_list[j] + current_H_list[j]) % 2 ** W_LENGTH
    #print("final currentH")
    # for i in range(8):
    #     print(hex(current_H_list[i]))
    result = ""
    for i in range(len(current_H_list)):
        result = result + format(current_H_list[i], "08x")
    #print("N-------------------:", N)
    return result

if __name__ ==  "__main__":
    f = open("shabytetestvectors/SHA256LongMsg.rsp", "r")
    previous_line = ""

    counter = 0
    old_result = ""
    current_length = 0
    for line in f:
        #print(previous_line[0:3])
        if line[0:3] == "Len":
            current_length = int(line[6:(len(line) - 1)]) // 8
        elif line[0:3] == "Msg":
            #print(line)
            
            filename1 = "SHA256_testvectors/testcaseLongMsg" + str(counter) + ".txt"
            filename2 = "SHA256_testvectors/resultLongMsg" + str(counter) + ".txt"
            f1 = open(filename1, "w")
            f2 = open(filename2, "w")
            input_string = line[6:(len(line) - 1)]
            #print(len(input_string))
            hexstr = int(input_string, 16)
            #print(hex(hexstr)[2:])
            length = len(hex(hexstr)[2:])
            input_byte = (hexstr).to_bytes(current_length, "big")
            #print("myhash_result")
            s = my_SHA256(input_byte)
            
            #correct_result = hashlib.sha256(bytes.fromhex(input_string)).hexdigest()
            correct_result = hashlib.sha256(input_byte).hexdigest()
            print("correct_result:", correct_result)
            print("s", s)
            #assert s == correct_result
            padded_message = pad_message(input_byte)
            pad_msg_hex = padded_message.hex()
            #print(s)
            #print()
            f1.write(str(len(pad_msg_hex) // (8 * 16) + len(pad_msg_hex) % (8 * 16)) + "\n")
            for i in range(len(pad_msg_hex) // 8):
                f1.write(pad_msg_hex[i * 8:i * 8 + 8] + "\n")
            f1.close()
            f2.write(correct_result)
            f2.close()
            if counter % 2 == 1:
                f3 = open("verilog_testvector/modp" + str(counter // 2) + ".txt", "w")
                total = old_result + s
                total_hex = int(total, 16)
                total_hex_modp = total_hex % p
                f3.write(str(total_hex_modp))
                f3.close()
            old_result = s
            counter += 1
            #if counter == 5:
            #    break
            #print("H.hex()", H.hexdigest())
        elif line[0:2] == "MD":
            MD = line[5:(len(line) - 1)]
            print("MD", MD)
            print("s", s)
            assert MD == s
            assert correct_result == MD

        
        previous_line = line

"""
#test my_SHA256
for i in range(10):
    a = random.randint(0, 2 ** 3000 -1)
    #a = 0x1f604280d2d6810881ed27fd34b27c03a7b9bfbb8b82863e9b368c0b4f1142f71f3c6e315fb76b3cd1208c5992a58f7f442127e437d75f84bdd6b9d2dd152e3f21d14d37324b35da79cfd0b36fd719c3ddd291b96fce7a65c22fcf2064da97c8adf51818d2b1d941df309832a421b0db62269c874b5576ce45f0ad7799

    a_in_bytes = (a).to_bytes(len(hex(a)[2:]) // 2 + len(hex(a)[2:]) % 2, byteorder="big")
    H = hashlib.sha256()    #SHA256 used as hash function
    print("a:\n", a_in_bytes.hex())
    H.update(a_in_bytes)
    #print("H.hex()", H.hexdigest())
    hashlib_result = H.hexdigest()
    mySHA_result = my_SHA256(a_in_bytes)
    print(hashlib_result)
    print(mySHA_result)
    assert hashlib_result == mySHA_result"""

    #SHA256 used as hash function
