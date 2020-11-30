def fac(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return(f)

sum = (2/fac(2)) - (4/fac(4)) + (6/fac(6)) - (8/fac(8))

print(sum)
