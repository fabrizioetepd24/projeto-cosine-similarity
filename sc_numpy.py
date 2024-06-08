import numpy as np
from numpy.linalg import norm

A = np.array([9,9,3,2,4,5,10,4,6,1])
B = np.array([5,9,2,4,6,8,3,7,2,0])

print("Vetor A: {}".format(A))
print("Vetor B: {}".format(B))

# calcula cosine similarity
cosine = np.dot(A,B)/(norm(A)*norm(B))

print("A similaridade de cosseno entre A e B: {}".format(cosine))
