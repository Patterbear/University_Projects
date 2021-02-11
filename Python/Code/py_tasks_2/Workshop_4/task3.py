def printToN(n):
    if n == 1:
        print(1)
    else:
        print(n)
        printToN(n-1)


def printSquares(n):
    if n == 1:
        print(1)
    else:
        print(n*n)
        printSquares(n-1)

def sumOfSquares(n):
    if n == 1:
        return 1
    else:
        return (n*n) + sumOfSquares(n-1)


printToN(5)
printSquares(5)
print(sumOfSquares(5))
