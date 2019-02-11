##########################################
# Time Complexity depend upon where you insert
# and delete data. θ(n)
##########################################

'''
Traverse a linked list
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # pointer intitally points to nothing

    def _traverse(self):
        node = self # start from head node
        while node != None:
            print(node.value) # take out value
            node = node.next # move to next node



if __name__ == "__main__":

    # create a linked list
    node1 = Node(12)
    node2 = Node(99)
    node3 = Node(37)

    #pointers
    node1.next = node2
    node2.next = node3
    
    # the entire linked list now looks like: 12->99->37
    # traverse
    node1._traverse()

