class Node:
    data = None
    next_node= None
    #Class Constructor
    def __init__(self, data):
        self.data = data

    #repr string presentation of node and data
    def __repr__(self):
        return "<Node data: %s>" % self.data

    #>>> N1
    #<Node data: 10>

class linkedList:
    #Methods for linked list data structure
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        #Linear time O(n), visit every node to determine size
        current = self.head
        count = 0
        while current:
            count+=1
            current = current.next_node
        return count

    def add(self, data):
        #Adds new node with data at head, Takes O(1) time
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        #search for first node with data that matches the key
        #Returns node of none if not found, takes O(n) worst case
        current = self.head
        
        while current: #aka while current != None
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self,data,index):
        #Insert a new node containing data at the index position
        #insertion take O(1) time, finding the node at the insertion node takes
        #O(n) worst case overall
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position >1:
                current = node.next_node
                positon -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self,key):
        #Removes node containing data that matches the key
        #Returns the node or None if key doesn't exist, takes O(n) time
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == ket and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
                
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        #Returns string representation of the list, takes O(n) time
        #Add strings to python list called nodes
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)

















        
