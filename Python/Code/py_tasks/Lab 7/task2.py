import numpy as np

num_list = [10, -3, -4, 50, 32, 55, -98, -54, -12, -5, 90]

def count_negatives_1(num_list):
    t = tuple(num_list)
    neg_tuple = ()
    total = 0
    for i in range(len(t)):
        if t[i] < 0:
            neg_tuple = neg_tuple + (t[i],)
            total = total + t[i]
    return(neg_tuple ,total / len(neg_tuple))


def count_negatives_2(num_list):
    a = np.array(num_list)
    neg_tuple = ()
    total =  0
    for i in range(len(a)):
        if a[i] < 0:
            neg_tuple = neg_tuple + (a[i],)
            total = total + a[i]
    return(neg_tuple, total / len(neg_tuple))
            
    
    
    


print(count_negatives_1(num_list))
print(count_negatives_2(num_list))
            
