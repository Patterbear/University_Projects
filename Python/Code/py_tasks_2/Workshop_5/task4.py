def merge(A, B):
    merged=[]
    i,j=0,0
    
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            merged.append(A[i])
            i=i+1
        else:
            merged.append(B[j])
            j=j+1
   
    if i < len(A):
        merged += A[i:]
    if j < len(B):
        merged += B[j:]
    return merged


def reverse_mergesort(xs):
    if len(xs) <= 1:
        return xs
    midpoint = len(xs)//2
    l, r = xs[0:midpoint], xs[midpoint:]
    l2, r2 = reverse_mergesort(l), reverse_mergesort(r)
    return merge(l2,r2)


arr=[14,2,16,11,5,7,66,4,3]
print(reverse_mergesort(arr))
