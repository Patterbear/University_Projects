import random

rolled = 0
values = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

while rolled < 100:
    values[random.randint(1, 6)] += 1
    rolled += 1

for i in values:
    print("Dice " + str(i) + ": " + str(values[i]) + " times")
    
