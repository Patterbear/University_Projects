import math

sum = 0
i = 1

while(i < 8):
    sum = sum + (i+1)/math.factorial(i)
    i += 1

print(sum)
    
