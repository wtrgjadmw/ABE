import hashlib

####### operations
def SHR(x, n):
    return x >> n

def ROTR(x, n):
    return (x >> n) | (x << (32 - n))

def ROTL(x, n):
    return (x << n) | (x >> (32 - n))

def Ch(x, y, z):
    return (x & y) ^ (~x & z)

def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def SIGMA0(x):
    return ROTR(x, 2) ^ ROTR(x, 13) ^ ROTR(x, 22)

def SIGMA1(x):
    return ROTR(x, 6) ^ ROTR(x, 11) ^ ROTR(x, 25)

def sigma0(x):
    return ROTR(x, 7) ^ ROTR(x, 18) ^ SHR(x, 3)

def sigma1(x):
    return ROTR(x, 17) ^ ROTR(x, 19) ^ SHR(x, 10)

####### constants

K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

# H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

####### algorithm

# input: a message of any length less than 2^64 bits
def padding(msg: bytes):
    msg_len = len(msg)
    counter = 1
    while msg_len * 8 >= 256 ** counter:
        counter += 1
    if (msg_len % 64 < 56):
        zero_num = 64 - (msg_len % 64) - 1 - counter
    else:
        zero_num = 128 - (msg_len % 64) - 1 - counter
    M = msg + (0x80).to_bytes(1, byteorder="big") + ((0).to_bytes(zero_num, byteorder="big")) + (msg_len*8).to_bytes(counter, 'big')
    print("%dbits: %s" % (len(M)*8, M.hex()))
    return M

def hash(M_bytes: bytes):
    M = int.from_bytes(M_bytes, 'big')
    M_len = len(M_bytes) * 8
    N = (M_len // 512) + 1 if M_len % 512 else M_len // 512
    print("%d block" % N)
    H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    for i in range(N):
        W = [0] * 64
        Mi = (M >> (512 * (N - i - 1))) & ((1 << 512) - 1)
        for j in range(64):
            if (j < 16):
                W[j] = (Mi >> (32 * (15 - j))) & ((1 << 32) - 1)
            else:
                W[j] = (sigma1(W[j-2]) + W[j-7] + sigma0(W[j-15]) + W[j-16]) & 0xffffffff
        [a, b, c, d, e, f, g, h] = H
        for j in range(64):
            T1 = (h + SIGMA1(e) + Ch(e, f, g) + K[j] + W[j]) & 0xffffffff
            T2 = (SIGMA0(a) + Maj(a, b, c)) & 0xffffffff
            h = g
            g = f
            f = e
            e = (d + T1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (T1 + T2) & 0xffffffff
        H[0] = (a + H[0]) & 0xffffffff         
        H[1] = (b + H[1]) & 0xffffffff         
        H[2] = (c + H[2]) & 0xffffffff         
        H[3] = (d + H[3]) & 0xffffffff         
        H[4] = (e + H[4]) & 0xffffffff         
        H[5] = (f + H[5]) & 0xffffffff         
        H[6] = (g + H[6]) & 0xffffffff         
        H[7] = (h + H[7]) & 0xffffffff  
    res = 0
    for i in range(8):
        res = (res << 32) | H[i]
    return res

def sha256(msg: bytes) -> bytes: 
    pad_msg = padding(msg)
    hashed_msg = hash(pad_msg)
    return hashed_msg.to_bytes(32, 'big')  

def lib_sha256(msg: bytes):
    H = hashlib.sha256()    #SHA256 used as hash function
    H.update(msg)
    #print("H.hex()", H.hexdigest())
    return H.digest()

if __name__ == "__main__":

    Len = 64
    Msg = 0x5738c929c4f4ccb6
    MD = 0x963bb88f27f512777aab6c8b1a02c70ec0ad651d428f870036e1917120fb48bf
    
    Msg_bytes = Msg.to_bytes(Len, 'big')
    MD_bytes = MD.to_bytes(32, 'big')

    res = sha256(Msg_bytes)
    res = int.from_bytes(res, 'big')
    
    assert res == MD, "Failed...\nmy_ans = %x\nMD     = %s" % (res, MD)
