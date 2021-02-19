def minsort(aList):
    r_list = []

    while len(aList) != 0:
        smallest = aList[0]
        for i in range(len(aList)):
            if aList[i] < smallest:
                smallest = aList[i]
        r_list.append(smallest)
        aList.remove(smallest)
    return r_list


print(minsort([3, 2, 4, 1]))
