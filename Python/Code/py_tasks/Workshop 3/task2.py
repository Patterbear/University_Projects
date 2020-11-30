sum = 0

i = int(input("Start Value: "))
n = int(input("Stop Value: "))

for i in range(i, n):
    sum += (2*i)**2 + (4*i)
print(sum)
