#Select i-th smallest element iin linear time
#Select recursively with array division into groups of 5 elements
#Pivot is the middle of medians from each group

def selection(a, rank):
    n = len(a)
    if n < 5:
        return rank_by_sorting(a,rank) #Sort and select in linear time
    medians = [rank_by_sorting(a[i:i+5], 3)
        for i in range(0, n-4, 5)]
            median = selection(medians, (len(medians) + 1) // 2) L, R = [], []
    for x in a:
        if x < median:
            L += [x]
    else:
        R += [x]
    if rank <= len(L):
        return selection(L, rank)
    else:
        return selection(R, rank - len(L))
