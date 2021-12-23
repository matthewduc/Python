#This python file mergesorts a file of unsorted numbers called with a file as
#an argument  
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def mergesort(values):
    if len(values) <= 1:
        return values
    middleIndex = len(values)//2 #floor divisioon rounds down
    left_values = mergesort(values[:middleIndex])
    right_values = mergesort(values[middleIndex:])
    sorted_values = []

    left_index = 0
    right_index = 0

    while leeft index < len(left_values) and right _index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    #add remaining values if any list content remains
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values

sorted_numbers = mergesort(numbers)
print(sorted_numbers)





    
