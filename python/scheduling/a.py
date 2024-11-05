

# template = "NX{0},NX{0}_,X,MUL\nk0_{1}_Z{2},k0_{1},Z_exp{2},MUL\nNX{2}_,NX{0},k0_{1}_Z{2},ADD"

# for i in range(8, 11):
#     print(template.format(i, 10-i, i+1))

# template = "DX{0},DX{0}_,X,MUL\nk1_{1}_Z{2},k1_{1},Z_exp{2},MUL\nDX{2}_,DX{0},k1_{1}_Z{2},ADD"

# for i in range(1, 10):
#     print(template.format(i, 9-i, i+2))

# template = "NY{0},NY{0}_,X,MUL\nk2_{1}_Z{2},k2_{1},Z_exp{2},MUL\nNY{2}_,NY{0},k2_{1}_Z{2},ADD"

# for i in range(1, 15):
#     print(template.format(i, 14-i, i+1))

template = "DY{0},DY{0}_,X,MUL\nk3_{1}_Z{2},k3_{1},Z_exp{2},MUL\nDY{2}_,DY{0},k3_{1}_Z{2},ADD"

for i in range(1, 15):
    print(template.format(i, 14-i, i+2))