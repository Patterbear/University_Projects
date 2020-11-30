numList1 = [4, -21, 2, -20]
numList2 = [3, -5, 2, -6, -1]

def abs_val(numList):
    ctz = numList[0]
    for i in range(1, len(numList)):
        if abs(numList[i]) < abs(ctz):
            ctz = numList[i]
    return ctz


print(abs_val(numList1))
print(abs_val(numList2))
