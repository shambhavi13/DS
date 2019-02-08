'''
Remove duplicates from linked list
'''

import linkedlist

class Node(linkedlist.Node):
    def remove_duplicates(self):
        lst = []
        node = self
        prev = None

        while node != None:
            if node.value in lst:
                # remove node
                prev.next = node.next
            else:
                # no dups
                lst.append(node.value)
            prev = node
            node = node.next

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.remove_duplicates()
    node1._traverse()
