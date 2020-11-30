sum = 0

n = int(input("n: "))
x = int(input("x: "))

for i in range(1, n+1):
    if(i%2 == 0):
        sum = sum + i / (i*x)
        print(sum)
    else:
        continue
        

print("Final sum: " + str(sum))
