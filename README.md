Este projeto contém três arquivos que calculam a similaridade de cosseno
de três maneiras diferentes:

1.cosine = np.dot(A,B)/(norm(A)*norm(B))

2.cosine = 1 - spatial.distance.cosine(A, B)

3.cosine = cosine_similarity([A],[B])
