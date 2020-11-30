import random
n = []
total = 0

for i in range(20):
    n.append(random.randint(1, 50))
    if (n[i] % 3 == 0 and n[i] % 2 == 0):
        total += 1
        print("The generated number that meets the requirement, item number " + str(total) + " is: " + str(n[i]))

print("The total number of generated values which are divisible by 2 and 3 is:  " + str(total))
