def reverse_list(aList):
    r_list = []
    i = -1
    while i >= -(len(aList)):
        r_list.append(aList[i])
        i-=1
    return r_list


test_list = [3, 5, 1, 2, 7, 4, 6, 8]
print(reverse_list(test_list))
        
