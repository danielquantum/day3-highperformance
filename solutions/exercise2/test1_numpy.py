import numpy as np
# Create a null vector of size 10 but the fifth value which is 1
a = np.zeros(10)
a[4] = 1
#print(a)

# Create a vector with values ranging from 10 to 49
b = np.arange(10, 50)
#print(b)

# Reverse a vector (first element becomes last)
c = np.arange(50)
c = c[::-1]
#print(c)

# Create a 3x3 matrix with values ranging from 0 to 8
d = np.arange(9).reshape(3, 3)
#print(d)

# Find indices of non-zero elements from [1,2,0,0,4,0]
e = np.array([1, 2, 0, 0, 4, 0])
e = np.nonzero(e)
#print(e)

# Create a random vector of size 30 with a random seed =  3 and find the mean value
np.random.seed(3)  # set the seed for reproducibility
f = np.random.random(30)
f = np.mean(f)
#print(f)

# Create a 2d array with 1 on the border and 0 inside
g = np.ones((5, 5))
g[1:-1, 1:-1] = 0
#print(g)

# Create a 8x8 matrix and fill it with a checkerboard pattern
h = np.zeros((8, 8), dtype=int)
h[1::2, ::2] = 1
h[::2, 1::2] = 1
#print(h)

# Create a checkerboard 8x8 matrix using the tile function
i = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
#print(i)

# Given a 1D array, negate all elements which are between 3 and 8, in place.
j = np.arange(11)
j[(3 < j) & (j < 8)] *= -1
#print(j)

# Create a random vector of size 10 and sort it
k = np.random.random(10)
k.sort()
#print(k)

# Consider two random array A anb B, check if they are equal
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.allclose(A, B)
#print(equal)
#print(A)
#print(B)

# How to convert an integer (32 bits) array into a float (32 bits) in place
A = np.arange(10, dtype=np.int32)
A = A.astype(np.float32, copy=False)
#print(A)
#print(A.dtype)
#print(A.flags)

# How to get the diagonal of a dot product?
A = np.arange(9).reshape(3, 3)
B = A + 1
C = np.dot(A, B)
D = np.diag(C)
print(D)






