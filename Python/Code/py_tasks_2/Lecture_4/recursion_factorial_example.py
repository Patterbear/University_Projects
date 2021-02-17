def getFactorial(N):
    if N == 0:
        return 1
    else:
        return N*getFactorial(N-1)

print(getFactorial(5))
