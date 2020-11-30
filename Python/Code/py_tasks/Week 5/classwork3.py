def joinList(aList, seperator):
    joined = ""
    for i in range(len(aList)):
        joined = joined + aList[i] + seperator
    return joined

aList = ["fuck", "you"]
seperator = ","
print(joinList(aList, seperator))
