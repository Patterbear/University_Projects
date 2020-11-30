import random

sum = 0

def user_loop(sum):

    start = int(input("Where should I start? "))
    stop = int(input("Where should I stop? "))

    for i in range(start,stop):
        print(i)
        sum  += 3*i
    print("The result for the sum of 3i from " + str(start) + " to " + str(stop) + " is " + str(sum))


def rand_loop(sum):
    start = random.randint(1,10)
    stop = random.randint(1,10)

    for i in range(start,stop):
        print(i)
        sum  += 3*i
    print("The result for the sum of 3i from " + str(start) + " to " + str(stop) + " is " + str(sum))


user_loop(sum)
rand_loop(sum)


