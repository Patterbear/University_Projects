def maxNum(t):
    max = 0
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i] [j] > max:
                max = t[i] [j]
    return max

t = [[10, 20, 30], [40, 50, 60]]

print(maxNum(t))
