from sympy import Matrix


def hard(B: Matrix):
    N = 4
    A = Matrix([
        [
            1 if (
                i > 1-N and max(v*v for v in [x-i, y-j, z-k]) <= 1
            ) or (
                i == x and j == y and k == z
            ) else 0
            for x in range(1-N, N) for y in range(1-N, N) for z in range(1-N, N) if x+y+z == 0
        ]
        for i in range(1-N, N) for j in range(1-N, N) for k in range(1-N, N) if i+j+k == 0
    ])
    B = B.copy()
    for i in range(4):
        B[i] = 0
    X = A.inv() * (-B)
    for i in range(37):
        if X[i].denominator % 5 == 0:
            X[i] *= X[i].denominator ** 2
    return X % 6
