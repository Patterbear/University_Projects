def Power(x, N):
    if N == 0:
        return 1
    else:
        return x*Power(x, N-1)

print(Power(3, 4))
