marks = input("").split()
sum = 0

for i in range(len(marks)):
    sum += float(marks[i])

print("Average: " + str(sum / len(marks)))
