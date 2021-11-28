from sympy import Matrix


def easy(B: Matrix):
    A = Matrix([
        [
            1 if jx-1 <= ix <= jx+1 and jy-1 <= iy <= jy+1 else 0
            for jx in range(4) for jy in range(4)
        ]
        for ix in range(4) for iy in range(4)
    ])
    return A.inv() * (-B) % 4
