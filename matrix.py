class Matrix:
    
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        return str(self.matrix)


def multiply_matrices(A: Matrix, B: Matrix):
    l = len(A.matrix)
    m = len(A.matrix[0])
    n = len(B.matrix[0])

    C = [0]*l
    for i in range(n):
        C[i] = [0]*n
    C = Matrix(C)

    for i in range(l):
        for j in range(n):
            sum = 0
            for k in range(m):
                sum = sum + A.matrix[i][k] * B.matrix[k][j]
            C.matrix[i][j] = sum

    return C