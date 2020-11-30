import random


num1 = int(input("Number: "))

if (10<num1<50):
    r = random.randint(10, 100)
    if r % 7 == 0 and num1 >= r:
        print(r + num1)
    else:
        print(r * num1)
else:
    print("Please enter the correct value.")
