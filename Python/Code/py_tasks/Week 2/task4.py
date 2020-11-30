import random

g = int(input("Guess: "))
if(g == random.randrange(0, 10)):
   print("Correct")
else:
    print("Incorrect")
