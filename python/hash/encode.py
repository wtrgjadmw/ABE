from h2f import hash_to_field
from m2c import map_to_curve_BLS12381G1

# hash_to_curve(msg)
# Input: msg, an arbitrary-length byte string.
# Output: P, a point in G.
# Steps:
# 1. u = hash_to_field(msg, 2)
# 2. Q0 = map_to_curve(u[0])
# 3. Q1 = map_to_curve(u[1])
# 4. R = Q0 + Q1 # Point addition
# 5. P = clear_cofactor(R)
# 6. return P

def hash_to_curve(msg):
    t_list = hash_to_field("abc".encode('utf-8'), 2)
    M = map_to_curve_BLS12381G1(t_list)