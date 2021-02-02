def duplicate(aList, bList):
    dupes = []
    for i in range(len(aList)):
        for j in range(len(bList)):
            if aList[i] == bList[j]:
                dupes.append(aList[i])
            else:
                continue

    return dupes



aList = [1, 2, 3, 4]
bList = [2, 4]
print(duplicate(aList, bList))
