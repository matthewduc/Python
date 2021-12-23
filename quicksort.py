#This file quicksorts a files of unsorted numbers
#Splits aroud pivot as first item for n numbers O(n log n)
#Worst case O(n^2)

#Pivots at random on average is better

import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

"""
For strings of i.e. names
from load import load_strings
names = load_strings(sys.argv[1])

e.g. redirect unsorted into sorted files
python quicksort.py names/unsorted.txt > names/sorted.txt
"""

#using pivot or selection sort
def quicksort(values):
    if len(values) <= 1:
        return values
    lessThanPivot = []
    greaterThanPivot = []
    pivot = values[0]
    for value in values [1:]:
        if value <= pivot:
            lessThanPivot.append(value)
        else:
            greaterThanPivot.append(value)
    return quicksort(lessThanPivot) + [pivot] + quicksort(greaterThanPivot)
    

sorted_numbers = quicksort(numbers)
print(sorted_numbers)
