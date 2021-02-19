def reverse_list_stack(aList):
    r_list = []
    for i in range(len(aList)):
        r_list.append(aList[-1])
        aList.pop()

    return r_list


print(reverse_list_stack([1,2,3]))
