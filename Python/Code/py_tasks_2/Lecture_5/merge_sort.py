

# merge sort (naive version) -------------------------------------------
def merge(A, B):
    merged=[]
    i,j=0,0 #initialize i and j to 0
    
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
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


 
def mergesort(xs):
    """Mergesort."""
    if len(xs) <= 1:
        # NOTE list is very small... and already sorted
        return xs
    midpoint = len(xs)//2  # NOTE integer division
    l, r = xs[0:midpoint], xs[midpoint:]
    l2, r2 = mergesort(l), mergesort(r)
    return merge(l2,r2)


# example --------------------------------------------------------------

arr=[14,2,16,11,5,7,66,4,3]
print("Mergesort example: ",str(mergesort(arr)))

