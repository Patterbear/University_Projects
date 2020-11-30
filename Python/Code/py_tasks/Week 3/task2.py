import random

N = int(input("Number: "))
for i in range(N):
    if random.random() > 0.5:
        print("Head")
    else:
        print("Tails")
