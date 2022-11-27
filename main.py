from matrix import multiply_matrices as mm
from matrix import Matrix


def linear_regression(X,Y):

    XY = [0]*len(X)
    X_square = [0]*len(X)
    Y_square = [0]*len(X)

    for i in range(len(X)):
        XY[i] = X[i] * Y[i]
        X_square[i] = X[i] * X[i]
        Y_square[i] = Y[i] * Y[i]

    sumX = sum(X)
    sumY = sum(Y)
    sumXY = sum(XY)
    sumX_square = sum(X_square)

    b0 = ((sumY*sumX_square) - (sumX*sumXY)) / ((len(X) * sumX_square) - (sumX*sumX))
    b1 = ((len(X)*sumXY) - (sumX*sumY)) / ((len(X)*sumX_square) - (sumX*sumX))

    return [b0, b1]

if __name__ == '__main__':
    X = [140,155,159,179,192,200,212]
    Y = [60,62,67,70,71,72,75]
    print(linear_regression(X,Y))


    A = Matrix([[1,2,3],[4,5,6]])
    B = Matrix([[7,8],[9,10],[11,12]])
    print(mm(A,B))

    print(Matrix([[1,2,3],[4,5,6]]))