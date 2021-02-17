def printNumbers(N):
    print(N)
    if N == 1:
        pass
    else:
        printNumbers(N-1)

printNumbers(5)
