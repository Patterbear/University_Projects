numbers = input("Enter numbers: ").split()
highest = 0
for i in range(len(numbers)):
    if int(numbers[i]) > highest:
        highest = int(numbers[i])

print("Highest value: " + str(highest))
