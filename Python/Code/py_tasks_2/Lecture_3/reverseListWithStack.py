def reverseListWithStack(aList):
    stack = []
    for item in aList:
        stack.append(item)

    position = 0
    while len(stack)>0:
        aList[position] = stack.pop()

        position+=1
    return aList



print(reverseListWithStack(["This", "is", "a", "test", "."]))

