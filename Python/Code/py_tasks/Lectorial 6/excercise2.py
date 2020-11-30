def list_ratio(L1, L2): 
    """ Inputs: two lists L1 and L2  of equal size 
    Output: a list ratios containing L1[i]/L2[i] """ 
    ratios = [] 
    for i in range(len(L1)):
        try:
            ratios.append(L1[i]/L2[i])
        except ZeroDivisionError:
            ratios.append(None)
    return ratios

print(list_ratio([3, 6, -9], [2, 5, 0]))
