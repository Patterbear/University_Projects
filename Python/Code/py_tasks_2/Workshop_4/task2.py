def list_sum(aList):
    n = len(aList)
    if n == 0:
        return 0
    else:
        return aList[0] + list_sum(aList[1:])

L = [1, 2, 3, 4, 5]

print(list_sum(L))
