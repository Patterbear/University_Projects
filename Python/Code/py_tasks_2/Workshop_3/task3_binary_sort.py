def duplicate(aList, bList):
    dupes = []

    for i in range(len(aList)):
        target = aList[i]
        low = 0
        high = len(aList)-1

        while low <= high:
            mid = (low+high) // 2

            if bList[mid] == target:
                dupes.append(bList[mid])
                break
            
            elif bList[mid] > target:
                high = mid-1

            else:
                low = mid+1

    return dupes
        




aList = [1, 2, 3, 4]
bList = [2, 4]
print(duplicate(aList, bList))
