'''
Insert given node into correct sorted position in
given sorted linked list

1. if linked list is empty then make the node as head and
return it
2. value of the node is smaller than the head node then
insert the node at start and make it head
3.In loop find appropriate node after the input node is to
be inserted. keep moving until the GN is found the node just
before GN is appropriate node
4. Insert node after the appropriate node
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # func to initialise head
    def __init__(self):
        self.head = None

    def sortedInsert(self, new_node):

        # check for empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            # loop until GN is found
            while(current.next is not None and
                  current.next.data < new_node.data):
                # increment
                current = current.next
            # insertion of new node
            new_node.next = current.next
            current.next = new_node

    # print list
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # insert node at begining
    def push(self, new_data):
        # create a new node
        new_node = Node(new_data)
        # make new node head
        new_node.next = self.head
        self.head = new_node

# Driver program
llist = LinkedList()
new_node = Node(5)
llist.sortedInsert(new_node)
new_node = Node(10)
llist.sortedInsert(new_node)
new_node = Node(7)
llist.sortedInsert(new_node)
new_node = Node(3)
llist.sortedInsert(new_node)
new_node = Node(1)
llist.sortedInsert(new_node)
new_node = Node(9)
llist.sortedInsert(new_node)
print ("Create Linked List")
llist.printlist()




