# Program to multiply two matrices using numpy
import numpy as np
np.random.seed(0)
N = 250

def matrix_multiply():
    # NxN matrix
    X = np.random.randint(0, 100, (N, N))
    #print(X)

    # Nx(N+1) matrix
    Y = np.random.randint(0, 100, (N, N+1))
    #print(Y)
    return np.dot(X, Y)

print(matrix_multiply())