def find_min(aList):
    if len(aList) == 1:
       return aList[0]

    else:
       return min(aList[0], find_min(aList[1:]))

aList = [2, 4, 5, 1, 3, 8]
print(find_min(aList))
