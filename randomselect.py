#This function selects the smallest element in an unsorted array
#Trivial solution, sort A, then select A[i] in O(nlogn) with mergesort

def randselect(a, rank):
    n = len(a)
    if n <= 1:
        return a[0]
    pivot = a[random.randint(0,n-1)]
    L,R, = [],[]
    for x in a:
        if a <pivot:
            L+=[x]
        else:
            R+=[x]
    if rank <= len(L):
        return randselect(L,rank)
    else:
        return randselect(R, rank-len(L))
