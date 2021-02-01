def removeNegatives(aQueue):
    numberSeen = 0
    n = len(aQueue)
    while numberSeen <= n:
        item = aQueue.pop(0)
        numberSeen+=1
        if item >=0:
            aQueue.append(item)
    return aQueue


print(removeNegatives([-1, 2, 5, -2, -4, -1, 5]))
