#this file searches for a name in a sorted list of names
#O(log n) runtime
import sys
from load import load_strings

names = load_strings(sys.argv[1])

search_names = names.toarray() #search_names is an array from files

def binary_search(collection, target):
    first = 0
    last = len(collection)
    while first <= last:
        midpoint = (first+last)//2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None
for n in search_name:
    index = binary_search(names, n)
    print(index)
