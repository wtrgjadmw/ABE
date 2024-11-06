import random
from constants import p, a, b, random_pointFp

class PK:
    def __init__(self) -> None:
        P = random_pointFp(p, [a, b])
        alpha = random.randint(0, p-1)
        delta = random.randint(0, p-1)
        P_alpha = P.scalar_mul(alpha)
        P_delta = P.scalar_mul(delta)