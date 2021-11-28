from sympy import Matrix


def easy(B: Matrix):
    A = Matrix([
        [
            1 if jx-1 <= ix <= jx+1 and jy-1 <= iy <= jy+1 else 0
            for jx in range(3) for jy in range(3)
        ]
        for ix in range(3) for iy in range(3)
    ])
    return A.inv() * (-B) % 4
