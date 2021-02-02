def subsetOf(L, M):
    for i in range(len(M)):
        for j in range(len(L)):
            if L[j] == M[i]:
                L[j] = 1
            else:
                continue
    for i in range(len(L)):
        if L[i] != 1:
            L[i] = 0
                
    return L

L = [2, 17, 12, 5, 66, 20, 7]
M = [2, 12, 66]

print(subsetOf(L, M))
