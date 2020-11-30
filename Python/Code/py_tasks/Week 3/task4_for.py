import math
sum = 0

for i in range(1, 8):
    sum = sum + (i+1)/math.factorial(i)

print(sum)
    
