import itertools, copy

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

def det_mat(matrix: list[list[float]]):
    # Base case for 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]
    
    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(len(matrix)):
        sub_matrix = [row[:c] + row[c+1:] for row in (matrix[:0] + matrix[1:])]
        det += ((-1) ** c) * matrix[0][c] * det_mat(sub_matrix)
    
    return det

def inv_mat(mat: list[list[float]]):
    det = det_mat(mat)
    inv = copy.deepcopy(mat)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            cofac_mat = []
            for ii in range(len(mat)):
                if ii == i:
                    continue
                cofac_mat.append([])
                for jj in range(len(mat[0])):
                    if jj != j:
                        cofac_mat[-1].append(mat[ii][jj])
            print(cofac_mat)
            cofac_det = det_mat(cofac_mat)
            print(cofac_det)
            cofactor = cofac_det / det
            if (i + j) % 2:
                cofactor *= -1
            inv[j][i] = cofactor
    return inv

# M = generate_LSSS([[[["B", ["A", "C", 1], 2], ["C", "D", "E", 2], 1], ["E", "F", "G", "H", 3], 2]])
# print(M)
print(inv_mat([[1, 1, -1], [-2, 0, 1], [0, 2, 1]]))