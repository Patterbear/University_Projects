data = open(input("Enter a file name: ")).read().splitlines()
for i in range(len(data)):
    data[i] = data[i].split(",")

def printList(list_a):
    for i in range(len(list_a)):
        print(list_a[i][0] + " Miles, £" + list_a[i][1])

print(data)
printList(data)
