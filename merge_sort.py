def merge_sort(list):
    #Sorts a list in ascending order, Divide & Conquer
    #Returns a new sorted list
    #Divide: Find midpoint of the list and divide into sublists
    #Conquer: Recursively sort the sublists created in previous step
    #Comobine: Merge the sorted sublists created in previous step

    #Takes O(nlogn) time
    #Reality O(k n log n) with list slice

    #Takes O(n) space complexity 

    if len(list) <= 1:
        return list

    LH, RH = split(list) #splits list at midpoint
    L = merge_sort(LH) #calls recursively
    R = merge_sort(RH)

    return merge(L,R)

def split(list):
    #Divide the unsorted list at midpoint into sublists
    #Returns twoo sublists - RH and LH
    #Takes averall O(logn) time
    mid = len(list)//2
    left = list[:mid] #starts beginning up to not including midpoint
    right = list[mid:] #Takes O(k), k = slice size

    

    return left, right

def merge(left, right):
    #Merges two lists, sorting them in the process
    #Returns a new merged list
    #Takes O(n) merge steps

    l = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while i <len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1
    return l

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] <= list[1] and verify_sorted(list[1:])

alist = [10, 4 , 15, 15, 7, 14, 1, 25, 63, 71]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
    




    
