def retrieve_five_smallest(aList):
    aList.sort()
    return aList[0:5]



aList = [1, 3, 2, 8, 3, 4, 7, 9, 10]
print(retrieve_five_smallest(aList))
