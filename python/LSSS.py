def generate_LSSS(F):
    M, L, m, d = [[1]], F, 1, 1
    z = 0
    while z != -1:
        z = -1
        for i in range(len(L)):
            if isinstance(L[i], list):
                z = i
                break
        if z != -1:
            Fz = L[z]
            m2 = len(Fz) - 1
            d2 = Fz[-1]
            M1, L1, m1, d1 = M, L, m, d
            M = [[0 for j in range(d1 + d2 - 1)] for i in range(m1 + m2 - 1)]
            L = [0 for i in range(m1 + m2 - 1)]
            for i in range(z):
                L[i] = L1[i]
                for j in range(d1):
                    M[i][j] = M1[i][j]
                for j in range(d1, d1 + d2 - 1):
                    M[i][j] = 0
            for i in range(z, z + m2):
                L[i] = Fz[i-z]
                for j in range(d1):
                    M[i][j] = M1[z][j]
                a = i - z + 1
                x = a
                for j in range(d1, d1 + d2 - 1):
                    M[i][j] = x
                    x = x * a
            for i in range(z + m2, m1 + m2 - 1):
                L[i] = L1[i-m2+1]
                for j in range(d1):
                    M[i][j] = M1[i-m2+1][j]
                for j in range(d1, d1 + d2 - 1):
                    M[i][j] = 0
            m = m1 + m2 - 1
            d = d1 + d2 - 1   
            print(m, d)   
            print(M)
            print(L)
    return M

M = generate_LSSS([[[["B", ["A", "C", 1], 2], ["C", "D", "E", 2], 1], ["E", "F", "G", "H", 3], 2]])
print(M)