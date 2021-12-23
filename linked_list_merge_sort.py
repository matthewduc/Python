from linked_list import linkedList


def merge_sort(linked_list):
    #Sorts a linked list in ascending order
    #Recursively divide linked list into sublists containing single node
    #Repeat merge the sublists to produce sorted sublists until one remains
    #Returns a sorted linked list

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(linked_list):
    #Divide the unsorted list at midport into sublists
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = linkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    #Merges two linked list, sorting by data in nodes
    #Returns a new, merged list

    #merging left and right
    merged = linkedList()
    #add a fake head that is discarded later
    merged.add(0)
    #set surrent to the head of the linked list
    current = merged.head
    #obtain head nodes for the left and right linked lists
    left_head = left.head
    right_head = right.head

    #iterate over left and right until we reach tail node of either
    while left_head or right_head:
        #If head node of left is None, add node from right to merged linkedList
        if left_head is None:
            current.next_node = right_head
            #call next on right to set loop condition to false
            right_head = right_head.next_node
        #If head node of right is None, add node from left to mergerd linkedList
        elif right_head is None:
            current.next_node = left_head
            #call next on left to set loop condition to false
            left_head = left_head.next_node
        else:
            #not at either tail node
            #obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            #if left data is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                #move left head to next node
                left_head = left_head.next_node
            #if data on left is larger, set current to right node
            else:
                current.next_node = right_head
                #move right head to next node
                right_head = right_head.next_node
        #move current to next node
        current = current.next_node
    #discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged
    
l = linkedList()
l.add(10)
l.add(200)
l.add(20)
l.add(30)

print(l)
sortedL = merge_sort(l)
print(sortedL)
    
    









