aList = ["I", "hate", "you"]
seperator = " "

def joinList(aList, seperator):
    full = ""
    for i in range(len(aList)):
        full += aList[i] + seperator
    return full


print(joinList(aList, seperator))
    
