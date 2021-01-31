data = open(input("Enter a file name: ")).read().splitlines()
for i in range(len(data)):
    data[i] = data[i].split(",")


def selectionSortDistance(list_a):
    for i in range(len(list_a)):
        min_pos = i
        for j in range(i+1, len(list_a)):
            if int(list_a[min_pos][0]) > int(list_a[j][0]):
                min_pos = j

        temp = list_a[i]
        list_a[i] = list_a[min_pos]
        list_a[min_pos] = temp

    return list_a


def selectionSortPrice(list_a):
    for i in range(len(list_a)):
        min_pos = i
        for j in range(i+1, len(list_a)):
            if float(list_a[min_pos][1]) > float(list_a[j][1]):
                min_pos = j

        temp = list_a[i]
        list_a[i] = list_a[min_pos]
        list_a[min_pos] = temp

    return list_a


def printList(list_a):
    for i in range(len(list_a)):
        print(list_a[i][0] + " Miles, £" + list_a[i][1])


printList(selectionSortPrice(data))
